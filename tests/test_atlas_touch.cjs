"use strict";

const assert = require("node:assert/strict");
const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const appPath = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.join(__dirname, "..", "site-bridge", "app.js");
const appSource = fs.readFileSync(appPath, "utf8");
const start = appSource.indexOf("  // pointer gestures on the canvas:");
const end = appSource.indexOf('  box.addEventListener("pointerleave"', start);
assert.ok(start >= 0 && end > start, "The Atlas pointer-handler source must be present.");
const gestureSource = appSource.slice(start, end);

function createHarness({ hit = null } = {}) {
  const handlers = new Map();
  const captured = new Set();
  const calls = { pan: [], turn: [], zoom: [], pick: [] };
  const finite = (name, values) => {
    assert.ok(values.every(Number.isFinite), `${name} must receive finite coordinates.`);
  };
  const canvas = {
    style: {},
    addEventListener(name, callback) {
      if (!handlers.has(name)) handlers.set(name, []);
      handlers.get(name).push(callback);
    },
    setPointerCapture(id) { captured.add(id); },
    releasePointerCapture(id) { captured.delete(id); },
    hasPointerCapture(id) { return captured.has(id); },
  };
  const context = {
    canvas,
    S: { camMode: "orbit" },
    m: { sel: null },
    lastPointer: "touch",
    blockCtxUntil: 0,
    card: { hidden: true, dataset: {} },
    menu: { hidden: true, dataset: {} },
    hideTimer: null,
    performance: { now: () => 1000 },
    clearTimeout() {},
    engage() {},
    closeMenu() {},
    hitTest: () => hit,
    pivotOn() {},
    stopAnim() {},
    schedule() {},
    hideCard() {},
    showCard() {},
    openMenu() {},
    api: { select() {} },
    pan(dx, dy) {
      finite("pan", [dx, dy]);
      calls.pan.push([dx, dy]);
    },
    turn(dx, dy) {
      finite("turn", [dx, dy]);
      calls.turn.push([dx, dy]);
    },
    zoomAt(x, y, factor) {
      finite("zoomAt", [x, y, factor]);
      assert.ok(factor > 0, "Pinch zoom must use a positive factor.");
      calls.zoom.push([x, y, factor]);
    },
    pick(id, x, y) { calls.pick.push([id, x, y]); },
  };
  vm.runInNewContext(gestureSource, context, { filename: appPath });
  const send = (type, pointerId, x, y, extra = {}) => {
    const event = {
      type,
      pointerId,
      clientX: x,
      clientY: y,
      pointerType: "touch",
      button: 0,
      shiftKey: false,
      preventDefault() {},
      ...extra,
    };
    for (const callback of handlers.get(type) || []) callback(event);
  };
  return { send, calls };
}

function sourceBlock(firstMarker, lastMarker) {
  const first = appSource.indexOf(firstMarker);
  const last = appSource.indexOf(lastMarker, first);
  assert.ok(first >= 0 && last > first, `Missing source block ${firstMarker}`);
  return appSource.slice(first, last);
}

function cameraSnapshot(camera) {
  return {
    q: Array.from(camera.q),
    cam: Array.from(camera.cam),
    target: Array.from(camera.target),
  };
}

function createCameraHarness(saved) {
  const homeCamera = { q: [1, 0, 0, 0], cam: [0, 0, -1400], target: [0, 0, 0] };
  const context = {
    S: { cams: { home: saved }, ch: { depth: "off" }, mapMode: "galaxy" },
    o: { key: "home", selected: null },
    modeW: () => ({ g: 1, j: 0, s: 0 }),
    home: () => cameraSnapshot(homeCamera),
    canvas: { getBoundingClientRect: () => ({ width: 390, height: 273 }) },
    VW: 1000,
    F: 1290,
    reduceMotion: () => true,
    cancelAnimationFrame() {},
    updates: 0,
    shifts: 0,
  };
  const math = sourceBlock("const qmul =", "function createMap(");
  const camera = sourceBlock("  const finiteCamera =", "  const focusSet =");
  const basis = sourceBlock("  const basis =", "  const FONT =");
  const pan = sourceBlock("  function pan(dxPx, dyPx)", "  function zoomAt(");
  const animate = sourceBlock("  function animate(partial, dur = 450)", "  const stopAnim =");
  const glue = `
    function update() { keepCameraFinite(); updates += 1; }
    function shiftBoth(shift) {
      shifts += 1;
      m.cam = vadd(m.cam, shift);
      m.target = vadd(m.target, shift);
    }
    globalThis.cameraFixture = {
      state: m,
      finiteCamera,
      copyCamera,
      keepCameraFinite,
      pan,
      animate,
    };
  `;
  vm.runInNewContext(math + camera + basis + pan + animate + glue, context, { filename: appPath });
  return { api: context.cameraFixture, context, homeCamera };
}

const tests = [];
const test = (name, run) => tests.push({ name, run });

test("pinch-to-one continuation rebases the remaining finger", () => {
  const h = createHarness();
  h.send("pointerdown", 1, 100, 100);
  h.send("pointerdown", 2, 200, 100);
  h.send("pointerup", 2, 200, 100);
  h.send("pointermove", 1, 110, 105);
  assert.deepEqual(h.calls.pan, [[10, 5]]);
});

test("cancellation leaving one finger rebases its continuation", () => {
  const h = createHarness();
  h.send("pointerdown", 1, 100, 100);
  h.send("pointerdown", 2, 200, 100);
  h.send("pointercancel", 2, 200, 100);
  h.send("pointermove", 1, 110, 100);
  assert.deepEqual(h.calls.pan, [[10, 0]]);
});

test("lost pointer capture leaves the remaining contact usable", () => {
  const h = createHarness();
  h.send("pointerdown", 1, 100, 100);
  h.send("pointerdown", 2, 200, 100);
  h.send("lostpointercapture", 2, 200, 100);
  h.send("pointermove", 1, 110, 100);
  h.send("pointerup", 2, 200, 100);
  h.send("pointermove", 1, 120, 100);
  assert.deepEqual(h.calls.pan, [[10, 0], [10, 0]]);
});

test("nonfinite pointer input is ignored without contaminating the next move", () => {
  const h = createHarness();
  h.send("pointerdown", 1, NaN, 100);
  h.send("pointerdown", 2, 100, 100);
  h.send("pointermove", 2, Infinity, 105);
  h.send("pointermove", 2, 105, NaN);
  h.send("pointermove", 2, 110, 105);
  assert.deepEqual(h.calls.pan, [[10, 5]]);
  assert.equal(h.calls.zoom.length, 0);
});

test("repeated pinch and pan gestures keep independent baselines", () => {
  const h = createHarness();
  for (let i = 0; i < 30; i += 1) {
    const first = i * 2 + 1;
    const second = first + 1;
    h.send("pointerdown", first, 100, 100);
    h.send("pointerdown", second, 200, 100);
    h.send("pointermove", second, 210, 100);
    h.send("pointerup", second, 210, 100);
    h.send("pointermove", first, 105, 100);
    h.send("pointerup", first, 105, 100);
  }
  assert.equal(h.calls.pan.length, 30);
  for (const delta of h.calls.pan) assert.deepEqual(delta, [5, 0]);
  assert.ok(h.calls.zoom.length >= 30);
});

test("a third finger can arrive and leave before returning to pan", () => {
  const h = createHarness();
  h.send("pointerdown", 1, 100, 100);
  h.send("pointerdown", 2, 200, 100);
  h.send("pointerdown", 3, 300, 100);
  h.send("pointermove", 3, 310, 110);
  h.send("pointerup", 3, 310, 110);
  h.send("pointermove", 2, 210, 100);
  h.send("pointerup", 2, 210, 100);
  h.send("pointermove", 1, 110, 100);
  assert.deepEqual(h.calls.pan.at(-1), [10, 0]);
});

test("coincident pinch contacts never emit a nonfinite zoom factor", () => {
  const h = createHarness();
  h.send("pointerdown", 1, 100, 100);
  h.send("pointerdown", 2, 100, 100);
  h.send("pointermove", 2, 100, 100);
  h.send("pointermove", 2, 110, 100);
  h.send("pointermove", 2, 120, 100);
  assert.ok(h.calls.zoom.length > 0, "Pinch must resume after a valid separation is established.");
});

test("one touch pointer pans after the drag threshold", () => {
  const h = createHarness();
  h.send("pointerdown", 1, 100, 100);
  h.send("pointermove", 1, 102, 101);
  assert.equal(h.calls.pan.length, 0);
  h.send("pointermove", 1, 110, 105);
  h.send("pointerup", 1, 110, 105);
  assert.deepEqual(h.calls.pan, [[10, 5]]);
  assert.equal(h.calls.zoom.length, 0);
});

test("a cancelled single-pointer gesture stops responding", () => {
  const h = createHarness();
  h.send("pointerdown", 1, 100, 100);
  h.send("pointercancel", 1, 100, 100);
  h.send("pointermove", 1, 110, 100);
  assert.equal(h.calls.pan.length, 0);
  h.send("pointerdown", 2, 200, 100);
  h.send("pointermove", 2, 210, 105);
  assert.deepEqual(h.calls.pan, [[10, 5]]);
});

test("a mouse left drag still pans", () => {
  const h = createHarness();
  const mouse = { pointerType: "mouse", button: 0 };
  h.send("pointerdown", 1, 100, 100, mouse);
  h.send("pointermove", 1, 110, 105, mouse);
  h.send("pointerup", 1, 110, 105, mouse);
  assert.deepEqual(h.calls.pan, [[10, 5]]);
  assert.equal(h.calls.turn.length, 0);
});

test("mouse right and Shift drags still orbit", () => {
  for (const extra of [
    { pointerType: "mouse", button: 2 },
    { pointerType: "mouse", button: 0, shiftKey: true },
  ]) {
    const h = createHarness();
    h.send("pointerdown", 1, 100, 100, extra);
    h.send("pointermove", 1, 110, 105, extra);
    h.send("pointerup", 1, 110, 105, extra);
    assert.deepEqual(h.calls.turn, [[10, 5]]);
    assert.equal(h.calls.pan.length, 0);
  }
});

test("an unmoved tap still selects a paper", () => {
  const h = createHarness({ hit: "AC-0001" });
  h.send("pointerdown", 1, 100, 100);
  h.send("pointerup", 1, 100, 100);
  assert.deepEqual(h.calls.pick, [["AC-0001", 100, 100]]);
  assert.equal(h.calls.pan.length, 0);
});

test("contaminated saved cameras fall back to the home camera", () => {
  const invalidSaved = [
    { q: [1, 0, 0, 0], cam: [NaN, 0, -1400], target: [0, 0, 0] },
    { q: [1, 0, 0, 0], cam: [0, 0, -1400], target: [0, Infinity, 0] },
    { q: [0, 0, 0, 0], cam: [0, 0, -1400], target: [0, 0, 0] },
    { q: [1, 0, 0], cam: [0, 0, -1400], target: [0, 0, 0] },
    { q: [1, 0, 0, 0], cam: [0, 0, -1400] },
  ];
  for (const saved of invalidSaved) {
    const { api, homeCamera } = createCameraHarness(saved);
    assert.equal(api.finiteCamera(api.state), true);
    assert.deepEqual(cameraSnapshot(api.state), homeCamera);
  }
});

test("camera copies isolate saved and last-valid arrays", () => {
  const saved = { q: [1, 0, 0, 0], cam: [10, 20, -1000], target: [10, 20, 0] };
  const expected = cameraSnapshot(saved);
  const { api } = createCameraHarness(saved);
  saved.cam[0] = 999;
  saved.q[0] = 0;
  assert.deepEqual(cameraSnapshot(api.state), expected);
  api.state.cam[0] = NaN;
  api.state.target[1] = Infinity;
  api.state.q[0] = NaN;
  api.keepCameraFinite();
  assert.deepEqual(cameraSnapshot(api.state), expected);
});

test("actual pan rejects nonfinite deltas before changing camera state", () => {
  const { api, context } = createCameraHarness();
  const before = cameraSnapshot(api.state);
  api.pan(NaN, 1);
  api.pan(1, Infinity);
  assert.deepEqual(cameraSnapshot(api.state), before);
  assert.equal(context.shifts, 0);
  api.pan(10, 5);
  assert.equal(context.shifts, 1);
  assert.equal(api.finiteCamera(api.state), true);
});

test("actual animate repairs its starting camera before interpolation", () => {
  const { api, context, homeCamera } = createCameraHarness();
  api.state.cam = [NaN, NaN, NaN];
  api.state.target = [NaN, NaN, NaN];
  api.state.q = [NaN, NaN, NaN, NaN];
  const destination = { q: [1, 0, 0, 0], cam: [20, 30, -900], target: [20, 30, 0] };
  api.animate(destination, 0);
  assert.equal(api.finiteCamera(api.state), true);
  assert.deepEqual(cameraSnapshot(api.state), destination);
  assert.equal(context.updates, 1);
  assert.notDeepEqual(cameraSnapshot(api.state), homeCamera);
});

console.log(`Atlas app SHA-256 ${crypto.createHash("sha256").update(appSource).digest("hex")}`);
let failed = 0;
for (const { name, run } of tests) {
  try {
    run();
    console.log(`PASS ${name}`);
  } catch (error) {
    failed += 1;
    console.error(`FAIL ${name}\n  ${error.message}`);
  }
}
console.log(`${tests.length - failed}/${tests.length} passed`);
process.exitCode = failed ? 1 : 0;
