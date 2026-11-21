const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const source = fs.readFileSync(path.join(root, "site-bridge", "app.js"), "utf8");
const helper = source.match(/function leaveMapImmersive\(\) \{[\s\S]*?\n\}/);
assert(helper, "leaveMapImmersive helper is present");
assert.match(source, /function route\(\) \{\s*\/\/[^\n]*\n\s*\/\/[^\n]*\n\s*leaveMapImmersive\(\);/, "routing releases fullscreen before rendering another page");

function load(overrides = {}) {
  const calls = [];
  const classes = new Set(["map-immersive"]);
  const context = {
    S: { activeMap: null },
    document: {
      body: { classList: { remove: value => { calls.push(["remove", value]); classes.delete(value); } } },
      fullscreenElement: null,
      exitFullscreen: () => { calls.push(["exitFullscreen"]); },
    },
    ...overrides,
  };
  vm.runInNewContext(`${helper[0]}; this.leaveMapImmersive = leaveMapImmersive;`, context);
  return { context, calls, classes };
}

{
  const { context, calls } = load();
  context.S.activeMap = { immersive: true, setImmersive: value => calls.push(["setImmersive", value]) };
  context.leaveMapImmersive();
  assert.deepEqual(calls, [["setImmersive", false]], "the connected map owns normal fullscreen teardown");
}

{
  const { context, calls, classes } = load();
  context.document.fullscreenElement = {};
  context.leaveMapImmersive();
  assert.equal(classes.has("map-immersive"), false, "a stale page scroll lock is removed");
  assert.deepEqual(calls, [["remove", "map-immersive"], ["exitFullscreen"]], "orphaned native fullscreen is also exited");
}

console.log("2/2 fullscreen-navigation checks passed");
