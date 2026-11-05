#!/usr/bin/env python3
"""Build deterministic data files for the Bridge site (site-bridge/data/).

Inputs (read-only):
  metadata/corpus.json                                   papers, internal_work_ids
  atlas/semantic-admission/corpus_semantic_contracts.v0.6.jsonl   concept -> paper bindings
  papers/current/**/*.md                                 paper text, for the Galaxy layout
  SEMANTIC_USE_CONTRACT.json                             question -> concept bindings

Outputs:
  site-bridge/data/atlas.json      node positions, related-paper links, concept counts
  site-bridge/data/questions.json  question entry points resolved to papers

Determinism: no randomness, no wall-clock values, sorted iteration, fixed iteration
count, coordinates rounded to 0.1. Re-running on the same inputs yields byte-identical
outputs; the input SHA-256 values are recorded in each output.

Standing: internal_work_ids are the [A1]-[A7] cross-links in each paper, annotated
"priority cross-link selected by corpus profile and similarity review". They are shown
as "related papers", not as author citations.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "metadata" / "corpus.json"
CONTRACTS = ROOT / "atlas" / "semantic-admission" / "corpus_semantic_contracts.v0.6.jsonl"
USE_CONTRACT = ROOT / "SEMANTIC_USE_CONTRACT.json"
CLUSTERS = ROOT / "curation" / "clusters.json"   # read only for "pinned_galaxies"; names are the site's business
OUT = ROOT / "site-bridge" / "data"

# Question wording is interface text, copied verbatim from site/app.js (QUESTIONS).
QUESTION_TEXT = {
    "Q01": "Can AI hallucination be addressed by changing the architecture beneath the model?",
    "Q02": "How can we constrain AI as power while universalizing bounded capabilities?",
    "Q03": "What comes after today’s application-centered computing stack?",
    "Q04": "Can systems compose without silently dropping their constraints?",
    "Q05": "How can people regain inspectable, renegotiable control of their computers?",
    "Q06": "How can meaning survive translation across models, systems, and institutions?",
    "Q07": "How do we turn a powerful idea into a testable, evidence-bearing system?",
    "Q08": "What structures determine which futures can become real?",
}

W, H, MARGIN = 1000.0, 700.0, 40.0
ITERATIONS = 500


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def layout(ids: list[str], edges: list[tuple[str, str]], radii: list[float]) -> dict[str, tuple[float, float]]:
    """Fruchterman-Reingold with a deterministic golden-angle spiral start."""
    n = len(ids)
    index = {a: i for i, a in enumerate(ids)}
    golden = math.pi * (3 - math.sqrt(5))
    pos = []
    for i in range(n):
        r = 300.0 * math.sqrt((i + 0.5) / n)
        pos.append([W / 2 + r * math.cos(i * golden), H / 2 + r * math.sin(i * golden)])
    k = math.sqrt((W * H) / n) * 0.9
    pairs = [(index[a], index[b]) for a, b in edges]
    temp = W / 10
    for step in range(ITERATIONS):
        disp = [[0.0, 0.0] for _ in range(n)]
        for i in range(n):
            xi, yi = pos[i]
            for j in range(i + 1, n):
                dx, dy = xi - pos[j][0], yi - pos[j][1]
                d2 = dx * dx + dy * dy or 0.01
                f = (k * k) / d2
                disp[i][0] += dx * f; disp[i][1] += dy * f
                disp[j][0] -= dx * f; disp[j][1] -= dy * f
        for i, j in pairs:
            dx, dy = pos[i][0] - pos[j][0], pos[i][1] - pos[j][1]
            d = math.sqrt(dx * dx + dy * dy) or 0.01
            f = d / k
            disp[i][0] -= dx * f; disp[i][1] -= dy * f
            disp[j][0] += dx * f; disp[j][1] += dy * f
        for i in range(n):  # mild gravity keeps disconnected papers on the canvas
            disp[i][0] += (W / 2 - pos[i][0]) * 0.02
            disp[i][1] += (H / 2 - pos[i][1]) * 0.02
        for i in range(n):
            dx, dy = disp[i]
            d = math.sqrt(dx * dx + dy * dy) or 0.01
            pos[i][0] += dx / d * min(d, temp)
            pos[i][1] += dy / d * min(d, temp)
        temp = max(0.5, temp * 0.985)
    xs = [p[0] for p in pos]; ys = [p[1] for p in pos]
    sx = (W - 2 * MARGIN) / ((max(xs) - min(xs)) or 1)
    sy = (H - 2 * MARGIN) / ((max(ys) - min(ys)) or 1)
    pos = [[MARGIN + (p[0] - min(xs)) * sx, MARGIN + (p[1] - min(ys)) * sy] for p in pos]
    # Overlap removal in canvas units, so every paper stays clickable. Node radius must
    # match site-bridge/app.js: 2.6 + sqrt(in) * 1.15, plus a 6-unit gap.
    for _ in range(200):
        moved = False
        for i in range(n):
            for j in range(i + 1, n):
                need = radii[i] + radii[j] + 6
                dx, dy = pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]
                d = math.sqrt(dx * dx + dy * dy)
                if d < need:
                    if d < 1e-6:
                        dx, dy, d = 1.0, 0.0, 1.0
                    push = (need - d) / 2
                    ux, uy = dx / d, dy / d
                    pos[i][0] -= ux * push; pos[i][1] -= uy * push
                    pos[j][0] += ux * push; pos[j][1] += uy * push
                    moved = True
        for p in pos:
            p[0] = min(max(p[0], MARGIN), W - MARGIN); p[1] = min(max(p[1], MARGIN), H - MARGIN)
        if not moved:
            break
    return {a: (round(pos[i][0], 1), round(pos[i][1], 1)) for a, i in index.items()}


# ---------------------------------------------------------------------------
# Jurisdictions view: a 4-ellipse Venn diagram. Every territory combination gets its
# own connected region; each paper is placed inside the exact region for its
# territories, and the related-paper links arrange papers within their region.
#
# Geometry chosen on 2026-10-25 by a grid search over symmetric 4-ellipse layouts and
# territory assignments, maximizing the worst region's capacity / need. The values are
# fixed here (not searched at build time); check_capacity() fails the build if the
# corpus outgrows any region.
VENN_TERRITORIES = ["Intelligence", "Possibility", "Coordination", "Computation"]  # outer-left, inner-left, inner-right, outer-right
VENN = {"dx_outer": 130, "dy_outer": 50, "dx_inner": 25, "dy_inner": 10, "rx": 390, "ry": 190, "angle_deg": 36}
VENN_AREA_PER_PAPER = 420.0   # canvas units^2 each paper needs, including spacing
VENN_INSET = 9.0              # papers stay this far inside region borders
VENN_GRID = 4                 # candidate-point spacing
VENN_ITERATIONS = 300
VENN_ROOM = 18.0              # a candidate point needs usable region within this radius


def venn_ellipses() -> list[tuple[float, float, float, float, float]]:
    v, cx, cy = VENN, W / 2, H / 2
    a = math.radians(v["angle_deg"])
    return [
        (cx - v["dx_outer"], cy + v["dy_outer"], v["rx"], v["ry"], a),
        (cx - v["dx_inner"], cy - v["dy_inner"], v["rx"], v["ry"], a),
        (cx + v["dx_inner"], cy - v["dy_inner"], v["rx"], v["ry"], -a),
        (cx + v["dx_outer"], cy + v["dy_outer"], v["rx"], v["ry"], -a),
    ]


def ellipse_value(e, x: float, y: float, grow: float = 0.0) -> float:
    """<= 1 inside. `grow` enlarges (positive) or shrinks (negative) both semi-axes."""
    cx, cy, rx, ry, ang = e
    c, s = math.cos(ang), math.sin(ang)
    dx, dy = x - cx, y - cy
    u, v = dx * c + dy * s, -dx * s + dy * c
    return (u / (rx + grow)) ** 2 + (v / (ry + grow)) ** 2


def region_mask(E, x: float, y: float) -> int:
    return sum(1 << i for i, e in enumerate(E) if ellipse_value(e, x, y) <= 1)


def inset_ok(E, mask: int, x: float, y: float, d: float) -> bool:
    for i, e in enumerate(E):
        if mask >> i & 1:
            if ellipse_value(e, x, y, -d) > 1:
                return False
        elif ellipse_value(e, x, y, d) <= 1:
            return False
    return d <= x <= W - d and d <= y <= H - d


def venn_layout(ids, territories, undirected, sim_pos, radii):
    E = venn_ellipses()
    masks = {a: sum(1 << i for i, t in enumerate(VENN_TERRITORIES) if t in territories[a]) for a in ids}
    # candidate points per region (inset from borders) and full-region areas
    points: dict[int, list[tuple[float, float]]] = {}
    area: dict[int, float] = {}
    for gx in range(0, int(W), VENN_GRID):
        for gy in range(0, int(H), VENN_GRID):
            x, y = gx + VENN_GRID / 2, gy + VENN_GRID / 2
            m = region_mask(E, x, y)
            if not m:
                continue
            area[m] = area.get(m, 0.0) + VENN_GRID * VENN_GRID
            if inset_ok(E, m, x, y, VENN_INSET):
                points.setdefault(m, []).append((x, y))
    # Drop points in narrow slivers and tips: keep a point only if most of the disc of
    # radius VENN_ROOM around it is usable region, so papers cannot wedge into a tip.
    for m, pts in points.items():
        have = set(pts)
        offs = [(dx * VENN_GRID, dy * VENN_GRID) for dx in range(-8, 9) for dy in range(-8, 9)
                if (dx * VENN_GRID) ** 2 + (dy * VENN_GRID) ** 2 <= VENN_ROOM ** 2]
        roomy = [p for p in pts if sum((p[0] + ox, p[1] + oy) in have for ox, oy in offs) >= 0.7 * len(offs)]
        points[m] = roomy or pts
    need: dict[int, int] = {}
    for a in ids:
        need[masks[a]] = need.get(masks[a], 0) + 1
    regions = []
    for m in range(1, 16):
        n = need.get(m, 0)
        ratio = area.get(m, 0.0) / (n * VENN_AREA_PER_PAPER) if n else None
        regions.append({"territories": [t for i, t in enumerate(VENN_TERRITORIES) if m >> i & 1], "papers": n,
                        "area": area.get(m, 0.0), "capacity_ratio": round(ratio, 2) if ratio is not None else None})
        if n and (ratio < 1.0 or not points.get(m)):
            raise SystemExit(f"Venn region {regions[-1]['territories']} cannot hold {n} papers (capacity ratio {ratio:.2f}). "
                             "Adjust VENN geometry before rebuilding.")

    def snap(a, x, y):
        m = masks[a]
        if inset_ok(E, m, x, y, VENN_INSET):
            return [x, y]
        best = min(points[m], key=lambda p: ((p[0] - x) ** 2 + (p[1] - y) ** 2, p))
        return [best[0], best[1]]

    index = {a: i for i, a in enumerate(ids)}
    n = len(ids)
    # Start from the similarity position, nudged by a small deterministic golden-angle
    # offset so papers that snap to the same border point can separate.
    golden = math.pi * (3 - math.sqrt(5))
    pos = [snap(a, sim_pos[a][0] + 6 * math.cos(i * golden), sim_pos[a][1] + 6 * math.sin(i * golden))
           for i, a in enumerate(ids)]
    # Only links within a region pull: they arrange similar papers near each other inside
    # their zone. Links between zones would drag papers onto region borders.
    pairs = [(index[a], index[b]) for a, b in undirected if masks[a] == masks[b]]
    # Per-region spacing: papers in the same region repel so they fill it evenly.
    kreg = {m: 0.85 * math.sqrt(len(points[m]) * VENN_GRID * VENN_GRID / c) for m, c in need.items()}
    temp = 14.0
    for _ in range(VENN_ITERATIONS):
        disp = [[0.0, 0.0] for _ in range(n)]
        for i in range(n):
            mi = masks[ids[i]]
            for j in range(i + 1, n):
                if masks[ids[j]] != mi:
                    continue
                k = kreg[mi]
                dx, dy = pos[i][0] - pos[j][0], pos[i][1] - pos[j][1]
                d2 = dx * dx + dy * dy or 0.01
                if d2 > 9 * k * k:
                    continue
                f = (k * k) / d2
                disp[i][0] += dx * f; disp[i][1] += dy * f
                disp[j][0] -= dx * f; disp[j][1] -= dy * f
        for i, j in pairs:
            k = kreg[masks[ids[i]]]
            dx, dy = pos[i][0] - pos[j][0], pos[i][1] - pos[j][1]
            d = math.sqrt(dx * dx + dy * dy) or 0.01
            f = 0.5 * d / k
            disp[i][0] -= dx * f; disp[i][1] -= dy * f
            disp[j][0] += dx * f; disp[j][1] += dy * f
        for i, a in enumerate(ids):
            dx, dy = disp[i]
            d = math.sqrt(dx * dx + dy * dy) or 0.01
            pos[i] = snap(a, pos[i][0] + dx / d * min(d, temp), pos[i][1] + dy / d * min(d, temp))
        temp = max(1.0, temp * 0.99)
    for _ in range(600):  # overlap removal, staying inside each region
        moved = False
        for i in range(n):
            for j in range(i + 1, n):
                need_d = radii[i] + radii[j] + 4
                dx, dy = pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]
                d = math.sqrt(dx * dx + dy * dy)
                if d < need_d:
                    if d < 1e-6:
                        dx, dy, d = 1.0, 0.0, 1.0
                    push = (need_d - d) / 2
                    ux, uy = dx / d, dy / d
                    pos[i] = snap(ids[i], pos[i][0] - ux * push, pos[i][1] - uy * push)
                    pos[j] = snap(ids[j], pos[j][0] + ux * push, pos[j][1] + uy * push)
                    moved = True
        if not moved:
            break
    out = {a: (round(pos[i][0], 1), round(pos[i][1], 1)) for a, i in index.items()}
    misplaced = [a for a in ids if region_mask(E, *out[a]) != masks[a]]
    if misplaced:
        raise SystemExit(f"Papers outside their Venn region after layout: {misplaced}")
    # label anchor for each territory: centroid of its exclusive region
    labels = []
    for i, t in enumerate(VENN_TERRITORIES):
        pts = points.get(1 << i, [])
        lx = sum(p[0] for p in pts) / len(pts); ly = sum(p[1] for p in pts) / len(pts)
        labels.append({"territory": t, "x": round(lx, 1), "y": round(ly, 1)})
    geometry = [{"territory": t, "cx": round(e[0], 1), "cy": round(e[1], 1), "rx": e[2], "ry": e[3],
                 "angle_deg": round(math.degrees(e[4]), 3)} for t, e in zip(VENN_TERRITORIES, E)]
    return out, {"ellipses": geometry, "labels": labels, "regions": regions,
                 "params": dict(VENN, area_per_paper=VENN_AREA_PER_PAPER, inset=VENN_INSET, room=VENN_ROOM, iterations=VENN_ITERATIONS)}


# ---------------------------------------------------------------------------
# Galaxy layout: 3D positions from combined closeness (paper wording + generated links),
# organised at two scales (galaxies and families) with empty space between galaxies.
# Pure Python and deterministic: sorted iteration, fixed iteration counts, no randomness.
GAL_K = 7                    # neighbours per paper in the closeness graph
GAL_TEXT_WEIGHT = 0.5        # closeness = 0.5 * wording similarity + 0.5 * generated link
GAL_FAMILY_MIN = 3           # families smaller than this merge into their closest sibling
GAL_BRIDGE_SHARE = 0.4       # a paper with this share of its closeness in another galaxy is a bridge
GAL_ITER = 400
STOPWORDS = set("""a about above after again against all also am an and any are as at be because been before being below
between both but by can could did do does doing down during each either else even ever every few for from further had has
have having he her here hers herself him himself his how however i if in into is it its itself just least less let like
made make many may me might more most much must my myself neither no nor not now of off often on once one only or other
otherwise our ours ourselves out over own per perhaps rather same see seem seems several shall she should since so some
such than that the their theirs them themselves then there therefore these they this those though through thus to too
toward towards under until up upon us use used uses using very via was we well were what whatever when where whether
which while who whom whose why will with within without would yet you your yours yourself yourselves paper papers section
sections figure table example examples case cases work works approach following given provide provides provided
particular specific general different without within also such may must can one two three first second third new
mathcal mathrm mathbf frac textit textbf left right begin end cdot ldots dots operatorname text emph quad qquad leq geq
mathsf mapsto rightarrow leftarrow infty sum prod forall exists http https www doi org com""".split())


def paper_body(text: str) -> str:
    cut = [text.find(h) for h in ("Corpus-Wide Reference Positioning", "Corpus-wide reference positioning", "Reference-pass",
                                   "## References", "P2 Corpus-Wide Integration") if text.find(h) > 0]
    return text[:min(cut)] if cut else text


def tfidf_vectors(texts: list[str]) -> list[dict[str, float]]:
    tok = re.compile(r"[a-z][a-z-]{2,}")
    tfs = []
    for t in texts:
        c: dict[str, int] = {}
        for w in tok.findall(t.lower()):
            w = w.strip("-")
            if len(w) > 2 and w not in STOPWORDS:
                c[w] = c.get(w, 0) + 1
        tfs.append(c)
    n = len(texts)
    df: dict[str, int] = {}
    for c in tfs:
        for w in c:
            df[w] = df.get(w, 0) + 1
    keep = {w for w, d in df.items() if 2 <= d <= n * 0.5}
    vecs = []
    for c in tfs:
        v = {w: (1 + math.log(f)) * (math.log((1 + n) / (1 + df[w])) + 1) for w, f in sorted(c.items()) if w in keep}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vecs.append({w: x / norm for w, x in v.items()})
    return vecs


def louvain(nodes: list[str], adj: dict[str, dict[str, float]], resolution: float = 1.0) -> dict[str, int]:
    """Deterministic Louvain: nodes visited in sorted order, ties go to the lowest community id."""
    part = {u: i for i, u in enumerate(sorted(nodes))}          # node -> community (original nodes)
    cur_nodes = sorted(nodes); cur_adj = {u: dict(adj.get(u, {})) for u in cur_nodes}
    member = {u: [u] for u in cur_nodes}                         # super-node -> original nodes
    while True:
        m2 = sum(sum(nb.values()) for nb in cur_adj.values()) or 1.0
        deg = {u: sum(cur_adj[u].values()) for u in cur_nodes}
        com = {u: i for i, u in enumerate(cur_nodes)}
        tot = {i: deg[u] for i, u in enumerate(cur_nodes)}
        moved_any, improved = True, False
        while moved_any:
            moved_any = False
            for u in cur_nodes:
                cu = com[u]
                links: dict[int, float] = {}
                for v, w in cur_adj[u].items():
                    if v != u:
                        links[com[v]] = links.get(com[v], 0.0) + w
                tot[cu] -= deg[u]
                best, best_gain = cu, links.get(cu, 0.0) - resolution * tot[cu] * deg[u] / m2
                for c in sorted(links):
                    g = links[c] - resolution * tot[c] * deg[u] / m2
                    if g > best_gain + 1e-12 or (abs(g - best_gain) <= 1e-12 and c < best):
                        best, best_gain = c, g
                tot[best] += deg[u]
                if best != cu:
                    com[u] = best; moved_any = True; improved = True
        if not improved:
            break
        labels = {c: i for i, c in enumerate(sorted(set(com.values())))}
        new_member: dict[int, list[str]] = {}
        for u in cur_nodes:
            new_member.setdefault(labels[com[u]], []).extend(member[u])
        new_adj: dict[int, dict[int, float]] = {i: {} for i in new_member}
        for u in cur_nodes:
            for v, w in cur_adj[u].items():
                a, b = labels[com[u]], labels[com[v]]
                new_adj[a][b] = new_adj[a].get(b, 0.0) + w
        cur_nodes = sorted(new_member); cur_adj = new_adj; member = new_member
        if len(cur_nodes) == 1:
            break
    out = {}
    for i, sn in enumerate(sorted(member, key=lambda k: min(member[k]))):
        for u in member[sn]:
            out[u] = i
    return out


def modularity(adj: dict[str, dict[str, float]], part: dict[str, int]) -> float:
    m2 = sum(sum(nb.values()) for nb in adj.values()) or 1.0
    deg = {u: sum(nb.values()) for u, nb in adj.items()}
    inside, tot = {}, {}
    for u, nb in adj.items():
        tot[part[u]] = tot.get(part[u], 0.0) + deg[u]
        for v, w in nb.items():
            if part[u] == part[v]:
                inside[part[u]] = inside.get(part[u], 0.0) + w
    return sum(inside.get(c, 0.0) / m2 - (tot[c] / m2) ** 2 for c in tot)


def fib_sphere(n: int, r: float) -> list[list[float]]:
    g = math.pi * (3 - math.sqrt(5))
    pts = []
    for i in range(n):
        y = 1 - 2 * (i + .5) / max(n, 1); rr = math.sqrt(max(0.0, 1 - y * y))
        pts.append([r * rr * math.cos(i * g), r * y, r * rr * math.sin(i * g)])
    return pts


def load_pins(known: set[str]) -> list[tuple[str, list[str]]]:
    """Author-pinned galaxies from curation/clusters.json. Any problem stops the build (nothing is guessed)."""
    if not CLUSTERS.exists():
        return []
    try:
        raw = json.loads(CLUSTERS.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"curation/clusters.json is not valid JSON: {e}")
    pins, seen, errs = [], {}, []
    lst = raw.get("pinned_galaxies", [])
    if not isinstance(lst, list):
        raise SystemExit('curation/clusters.json: "pinned_galaxies" must be a list.')
    for i, g in enumerate(lst):
        gid = g.get("id") if isinstance(g, dict) else None
        if not isinstance(gid, str) or not re.fullmatch(r"G:[A-Z0-9][A-Z0-9-]*", gid) or re.fullmatch(r"G:AC-\d{4}", gid):
            errs.append(f'pinned galaxy {i + 1}: id "{gid}" must look like G:NAME (capitals, digits, hyphens) and not like G:AC-####'); continue
        if any(gid == p for p, _ in pins):
            errs.append(f"{gid} is pinned twice"); continue
        mem = g.get("members")
        if not isinstance(mem, list) or len(mem) < GAL_FAMILY_MIN:
            errs.append(f"{gid}: needs a members list of at least {GAL_FAMILY_MIN} accession IDs"); continue
        ok = []
        for a in mem:
            if a not in known:
                errs.append(f'{gid}: "{a}" is not an accession ID in metadata/corpus.json')
            elif a in seen:
                errs.append(f"{a} is pinned to both {seen[a]} and {gid}")
            else:
                seen[a] = gid; ok.append(a)
        pins.append((gid, sorted(ok)))
    if errs:
        raise SystemExit("curation/clusters.json pinned_galaxies problems:\n  " + "\n  ".join(errs))
    return sorted(pins)


def galaxy_layout(ids, titles_in, directed, texts, in_count, radii, pins=()):
    n = len(ids); idx = {a: i for i, a in enumerate(ids)}
    vecs = tfidf_vectors([paper_body(t) for t in texts])
    sim = [[0.0] * n for _ in range(n)]
    for i in range(n):
        vi = vecs[i]
        for j in range(i + 1, n):
            vj = vecs[j]
            small, big = (vi, vj) if len(vi) < len(vj) else (vj, vi)
            s = sum(x * big.get(w, 0.0) for w, x in small.items())
            sim[i][j] = sim[j][i] = s
    smax = max(max(r) for r in sim) or 1.0
    link = set()
    for a, b in directed:
        link.add((idx[a], idx[b])); link.add((idx[b], idx[a]))
    close = [[GAL_TEXT_WEIGHT * sim[i][j] / smax + (1 - GAL_TEXT_WEIGHT) * (1.0 if (i, j) in link else 0.0) if i != j else 0.0
              for j in range(n)] for i in range(n)]
    nn = {ids[i]: [ids[j] for j in sorted(range(n), key=lambda j: (-close[i][j], j))[:GAL_K]] for i in range(n)}
    adj: dict[str, dict[str, float]] = {a: {} for a in ids}
    for a, nb in nn.items():
        for b in nb:
            w = close[idx[a]][idx[b]]
            adj[a][b] = max(adj[a].get(b, 0.0), w); adj[b][a] = max(adj[b].get(a, 0.0), w)
    # galaxies are found over all papers exactly as without pins; pinned papers are then moved into
    # their own galaxies, so pinning moves only the pinned papers and leaves every other grouping as it was
    gpart = louvain(ids, adj, 1.0)
    pin_label: dict[int, str] = {}
    nxt = max(gpart.values(), default=-1) + 1
    for gid, mem in pins:
        pin_label[nxt] = gid
        for a in mem:
            gpart[a] = nxt
        nxt += 1
    gq = modularity(adj, gpart)
    galaxies: dict[int, list[str]] = {}
    for a in ids:
        galaxies.setdefault(gpart[a], []).append(a)
    # families inside each galaxy
    fam_of: dict[str, tuple[int, int]] = {}
    families: dict[int, dict[int, list[str]]] = {}
    for g, mem in sorted(galaxies.items()):
        sub = {a: {b: w for b, w in adj[a].items() if gpart[b] == g} for a in mem}
        fp = louvain(mem, sub, 1.0)
        fams: dict[int, list[str]] = {}
        for a in mem:
            fams.setdefault(fp[a], []).append(a)
        changed = True                       # merge tiny families into their closest sibling
        while changed and len(fams) > 1:
            changed = False
            for f in sorted(fams, key=lambda k: (len(fams[k]), k)):
                if len(fams[f]) >= GAL_FAMILY_MIN:
                    continue
                aff = {h: sum(sub[a].get(b, 0.0) for a in fams[f] for b in fams[h]) for h in fams if h != f}
                tgt = sorted(aff, key=lambda h: (-aff[h], h))[0]
                fams[tgt] = sorted(fams[tgt] + fams.pop(f)); changed = True
                break
        families[g] = {i: sorted(v) for i, (k, v) in enumerate(sorted(fams.items(), key=lambda kv: min(kv[1])))}
        for fi, v in families[g].items():
            for a in v:
                fam_of[a] = (g, fi)
    # bridges: a large share of closeness into one other galaxy
    bridge = {}
    for a in ids:
        tot_w = sum(adj[a].values()) or 1.0
        per: dict[int, float] = {}
        for b, w in adj[a].items():
            if gpart[b] != gpart[a]:
                per[gpart[b]] = per.get(gpart[b], 0.0) + w
        if per:
            h = sorted(per, key=lambda k: (-per[k], k))[0]
            if per[h] / tot_w >= GAL_BRIDGE_SHARE:
                bridge[a] = h
    # galaxy centres: spread in the map plane (not on a sphere, which stacks galaxies behind each
    # other in the front view), pulled together by affinity, kept apart by size; depth comes from
    # each galaxy's own 3D shell of papers
    gids = sorted(galaxies)
    grad = {g: 150.0 * math.sqrt(len(galaxies[g]) / 50.0) for g in gids}
    aff = {(g, h): sum(adj[a].get(b, 0.0) for a in galaxies[g] for b in galaxies[h]) / (len(galaxies[g]) * len(galaxies[h]))
           for g in gids for h in gids if g < h}
    amax = max(aff.values()) if aff else 1.0
    gc = {g: [520.0 * math.cos(2 * math.pi * i / len(gids)), 360.0 * math.sin(2 * math.pi * i / len(gids)), 0.0]
          for i, g in enumerate(gids)}
    for it in range(300):
        for g in gids:
            fx = [0.0, 0.0, 0.0]
            for h in gids:
                if h == g:
                    continue
                d = [gc[g][0] - gc[h][0], gc[g][1] - gc[h][1]]; dist = math.sqrt(d[0] * d[0] + d[1] * d[1]) or 1.0
                want = (grad[g] + grad[h]) * (1.9 - 0.5 * aff[(min(g, h), max(g, h))] / amax)   # empty space between galaxies
                f = (want - dist) * 0.05 if dist < want else (want - dist) * 0.01   # push apart firmly, pull together gently
                for k in range(2):
                    fx[k] += d[k] / dist * f
            for k in range(2):
                gc[g][k] += fx[k]
        cen = [sum(gc[g][k] for g in gids) / len(gids) for k in range(3)]
        for g in gids:
            for k in range(3):
                gc[g][k] -= cen[k]
    # family centres within each galaxy, papers around family centres
    pos: dict[str, list[float]] = {}
    fcent: dict[tuple[int, int], list[float]] = {}
    frad: dict[tuple[int, int], float] = {}
    for g in gids:
        fams = families[g]; fk = sorted(fams)
        offs = [[o[0], o[1], o[2] * 0.5] for o in fib_sphere(len(fk), grad[g] * (0.55 if len(fk) > 1 else 0.0))]
        for f, o in zip(fk, offs):
            fcent[(g, f)] = [gc[g][k] + o[k] for k in range(3)]
            frad[(g, f)] = max(28.0, grad[g] * 0.5 * math.sqrt(len(fams[f]) / len(galaxies[g])))
            mem = sorted(fams[f], key=lambda a: (-in_count[a], a))           # most-linked papers start at the core
            sp = fib_sphere(len(mem), frad[(g, f)])
            sp.sort(key=lambda p: p[0] ** 2 + p[1] ** 2 + p[2] ** 2)
            for a, p in zip(mem, sp):
                pos[a] = [fcent[(g, f)][k] + p[k] * (0.35 + 0.65 * (mem.index(a) + 1) / len(mem)) for k in range(3)]
    # refinement: closeness springs, anchors to family and galaxy centres, local repulsion
    temp = 18.0
    order = list(ids)
    for it in range(GAL_ITER):
        disp = {a: [0.0, 0.0, 0.0] for a in order}
        for a in order:
            pa = pos[a]
            for b, w in adj[a].items():
                if b <= a:
                    continue
                pb = pos[b]; d = [pb[k] - pa[k] for k in range(3)]
                same = fam_of[a] == fam_of[b]
                k_s = (0.020 if same else 0.006 if gpart[a] == gpart[b] else 0.0015) * w
                if gpart[a] != gpart[b] and (gpart[a] in pin_label or gpart[b] in pin_label):
                    k_s = 0.0                                                     # a pinned galaxy holds together: no pull from outside it
                for k in range(3):
                    disp[a][k] += d[k] * k_s; disp[b][k] -= d[k] * k_s
        for i, a in enumerate(order):
            pa = pos[a]
            for b in order[i + 1:]:
                pb = pos[b]; d = [pa[k] - pb[k] for k in range(3)]
                d2 = d[0] * d[0] + d[1] * d[1] + d[2] * d[2]
                if d2 > 3600 or d2 == 0:
                    continue
                f = 220.0 / d2
                for k in range(3):
                    disp[a][k] += d[k] * f; disp[b][k] -= d[k] * f
        for a in order:
            g, f = fam_of[a]
            core = 0.03 + 0.05 * min(1.0, in_count[a] / 40.0)            # hubs sit near their family's core
            anchor = fcent[(g, f)]
            if a in bridge and g not in pin_label:                        # bridges lean toward the other galaxy (pinned papers stay put)
                anchor = [0.65 * anchor[k] + 0.35 * gc[bridge[a]][k] for k in range(3)]
            for k in range(3):
                disp[a][k] += (anchor[k] - pos[a][k]) * core + (gc[g][k] - pos[a][k]) * 0.004
        for a in order:
            d = disp[a]; L = math.sqrt(sum(x * x for x in d)) or 1.0; s = min(L, temp)
            for k in range(3):
                pos[a][k] += d[k] / L * s
        temp = max(0.6, temp * 0.99)
    # fit into the map frame: x in [40, 960], y in [40, 660], z in [-ZS, ZS] (ZS = 520 in app.js)
    ZS = 520.0
    lo = [min(pos[a][k] for a in ids) for k in range(3)]; hi = [max(pos[a][k] for a in ids) for k in range(3)]
    span = [max(1e-6, hi[k] - lo[k]) for k in range(3)]
    s = min(920 / span[0], 620 / span[1], 2 * ZS * 0.9 / span[2])
    mid = [(hi[k] + lo[k]) / 2 for k in range(3)]
    fit = lambda p: [500 + (p[0] - mid[0]) * s, 350 + (p[1] - mid[1]) * s, (p[2] - mid[2]) * s]
    out = {a: fit(pos[a]) for a in ids}
    # overlap removal in 3D, same radius formula as the site
    ri = {a: radii[idx[a]] for a in ids}
    for _ in range(200):
        moved = False
        for i, a in enumerate(ids):
            for b in ids[i + 1:]:
                d = [out[b][k] - out[a][k] for k in range(3)]; dist = math.sqrt(sum(x * x for x in d))
                need = ri[a] + ri[b] + 5
                if dist < need:
                    if dist < 1e-6:
                        d, dist = [1.0, 0.0, 0.0], 1.0
                    push = (need - dist) / 2
                    for k in range(3):
                        out[a][k] -= d[k] / dist * push; out[b][k] += d[k] / dist * push
                    moved = True
        if not moved:
            break
    out = {a: [round(v, 1) for v in p] for a, p in out.items()}
    # neighbour preservation: how many of each paper's 7 closest (by closeness) are among its 7 nearest in space
    def keep(ref):
        tot = 0.0
        for a in ids:
            near = sorted((b for b in ids if b != a), key=lambda b: (sum((out[a][k] - out[b][k]) ** 2 for k in range(3)), b))[:GAL_K]
            tot += len(set(near) & set(ref[a])) / GAL_K
        return round(tot / len(ids), 3)
    link_nb = {a: [] for a in ids}
    for a, b in directed:
        link_nb[a].append(b); link_nb[b].append(a)
    stats = {"modularity_galaxies": round(gq, 3), "keeps_closeness_neighbours": keep(nn), "keeps_link_neighbours": keep(link_nb)}
    # summaries with top terms (interface synthesis, for drafting names)
    def top_terms(mem, k=6):
        acc: dict[str, float] = {}
        for a in mem:
            for w, x in vecs[idx[a]].items():
                acc[w] = acc.get(w, 0.0) + x
        return [w for w, _ in sorted(acc.items(), key=lambda kv: (-kv[1], kv[0]))[:k]]
    hub = lambda mem: sorted(mem, key=lambda a: (-in_count[a], a))[0]
    fitr = lambda r: round(r * s, 1)
    gid_of = {g: pin_label.get(g, "G:" + hub(galaxies[g])) for g in gids}
    gal_out = []
    for g in gids:
        fl = []
        for f in sorted(families[g]):
            mem = families[g][f]
            fl.append({"id": "F:" + hub(mem), "size": len(mem), "center": [round(v, 1) for v in fit(fcent[(g, f)])],
                       "radius": fitr(frad[(g, f)]), "top_terms": top_terms(mem, 5)})
        mem = galaxies[g]
        gal_out.append({"id": gid_of[g], "pinned": g in pin_label, "size": len(mem), "center": [round(v, 1) for v in fit(gc[g])],
                        "radius": fitr(grad[g]), "top_terms": top_terms(mem), "families": fl})
    per_node = {a: {"galaxy": gid_of[gpart[a]], "family": "F:" + hub(families[gpart[a]][fam_of[a][1]]),
                    "bridge": gid_of[bridge[a]] if a in bridge else None} for a in ids}
    params = {"k": GAL_K, "text_weight": GAL_TEXT_WEIGHT, "family_min": GAL_FAMILY_MIN, "bridge_share": GAL_BRIDGE_SHARE,
              "iterations": GAL_ITER, "clustering": "deterministic Louvain, resolution 1.0 (galaxies), 1.0 within each galaxy (families)",
              "text": "TF-IDF over each paper's main text (generated reference sections removed)"}
    return out, per_node, {"galaxies": gal_out, "pins": [{"id": gid, "members": mem} for gid, mem in pins], "params": params, "stats": stats}


def main() -> None:
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    papers = sorted(corpus["papers"], key=lambda p: p["accession_number"])
    by_work = {p["work_id"]: p["accession_id"] for p in papers}
    by_title = {norm_title(p["title"]): p["accession_id"] for p in papers}
    ids = [p["accession_id"] for p in papers]

    directed: list[tuple[str, str]] = []
    unresolved_links = 0
    for p in papers:
        for w in p.get("internal_work_ids", []):
            if w in by_work:
                directed.append((p["accession_id"], by_work[w]))
            else:
                unresolved_links += 1
    directed.sort()
    undirected = sorted({tuple(sorted(e)) for e in directed})
    in_count = {a: 0 for a in ids}
    for _, b in directed:
        in_count[b] += 1

    concepts: dict[str, dict] = {}
    for line in CONTRACTS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rec = json.loads(line)
            concepts[rec["identity"]["concept_id"]] = rec
    concept_count = {a: 0 for a in ids}
    unmatched_titles: set[str] = set()
    for cid in sorted(concepts):
        for b in concepts[cid].get("artifact_bindings", []):
            a = by_title.get(norm_title(b.get("artifact_title", "")))
            if a:
                concept_count[a] += 1
            else:
                unmatched_titles.add(b.get("artifact_title", ""))

    radii = [2.6 + math.sqrt(in_count[a]) * 1.15 for a in ids]
    pos = layout(ids, undirected, radii)
    vpos, venn = venn_layout(ids, {p["accession_id"]: p["territories"] for p in papers}, undirected, pos, radii)
    texts, md_hash = [], hashlib.sha256()
    for p in papers:
        raw = (ROOT / p["formats"]["markdown"]["path"]).read_bytes()
        md_hash.update(p["accession_id"].encode() + b"\0" + hashlib.sha256(raw).digest())
        texts.append(raw.decode("utf-8", errors="replace"))
    pins = load_pins(set(ids))
    gpos, gnode, galaxy = galaxy_layout(ids, None, directed, texts, in_count, radii, pins)
    pins_hash = hashlib.sha256(json.dumps([[g, m] for g, m in pins], separators=(",", ":")).encode()).hexdigest().upper()
    inputs = {
        "metadata/corpus.json": sha256(CORPUS),
        "atlas/semantic-admission/corpus_semantic_contracts.v0.6.jsonl": sha256(CONTRACTS),
        "SEMANTIC_USE_CONTRACT.json": sha256(USE_CONTRACT),
        "papers/current/**/*.md (combined, by accession)": md_hash.hexdigest().upper(),
        "curation/clusters.json pinned_galaxies (canonical: sorted ids and members)": pins_hash,
    }
    atlas = {
        "schema": "ableman.bridge-atlas.v0.4",
        "inputs_sha256": inputs,
        "layout": {"algorithm": "fruchterman-reingold", "start": "golden-angle spiral by accession",
                   "iterations": ITERATIONS, "overlap_removal": "radius 2.6 + sqrt(in) * 1.15, gap 6", "width": W, "height": H},
        "link_standing": "GENERATED_CROSS_LINK: priority cross-link selected by corpus profile and similarity review",
        "concept_standing": "REVIEWED_PROVISIONAL / AUTHOR_CONFIRMATION_REQUIRED",
        "counts": {"papers": len(ids), "directed_links": len(directed), "undirected_links": len(undirected),
                   "unresolved_links": unresolved_links,
                   "concept_bindings_matched": sum(concept_count.values()),
                   "concept_binding_titles_unmatched": len(unmatched_titles)},
        "unmatched_concept_titles": sorted(unmatched_titles),
        "venn": venn,
        "galaxy": galaxy,
        "nodes": [{"a": a, "x": pos[a][0], "y": pos[a][1], "vx": vpos[a][0], "vy": vpos[a][1],
                   "gx": gpos[a][0], "gy": gpos[a][1], "gz": gpos[a][2], **gnode[a],
                   "in": in_count[a], "concepts": concept_count[a]} for a in ids],
        "links": [list(e) for e in directed],
    }

    use = json.loads(USE_CONTRACT.read_text(encoding="utf-8"))
    questions = []
    for b in sorted(use["semantic_bindings"], key=lambda x: x["binding_id"]):
        qid = b["binding_id"]
        rows, union = [], []
        for cid in b["concept_ids"]:
            rec = concepts.get(cid)
            if rec is None:
                rows.append({"concept_id": cid, "name": None, "status": "CONCEPT_NOT_IN_REGISTRY", "papers": []})
                continue
            found = []
            for ab in rec.get("artifact_bindings", []):
                a = by_title.get(norm_title(ab.get("artifact_title", "")))
                if a and a not in found:
                    found.append(a)
            rows.append({"concept_id": cid, "name": rec["representation"]["RPZ1"]["bound_name"],
                         "status": "BOUND" if found else "NO_PAPER_BINDING", "papers": found})
            union += [a for a in found if a not in union]
        questions.append({"id": qid, "text": QUESTION_TEXT.get(qid), "text_standing": "INTERFACE_TEXT",
                          "concepts": rows, "papers": union})
    qout = {"schema": "ableman.bridge-questions.v0.1", "inputs_sha256": inputs,
            "binding_source": "SEMANTIC_USE_CONTRACT.json semantic_bindings[].concept_ids",
            "questions": questions}

    OUT.mkdir(parents=True, exist_ok=True)
    for name, obj in (("atlas.json", atlas), ("questions.json", qout)):
        (OUT / name).write_text(
            json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(f"wrote {name}  sha256 {sha256(OUT / name)}")
    print(json.dumps(atlas["counts"]))


if __name__ == "__main__":
    main()
