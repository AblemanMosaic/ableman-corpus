# Curation

Four author-editable files used by the Bridge site (`site-bridge/`). Each entry carries a
`standing`: `INTERFACE_DRAFT` (proposed by the interface) or `AUTHOR_CURATED` (yours).
Everything else on the map is generated (cross-links, galaxy membership, layouts) or comes
from the semantic contract (question entry points).

| File | What it controls |
|---|---|
| `routes.json` | Reading routes: ordered stops, each with a reason |
| `depth.json` | Front-to-back tiers for the Newcomer lens (start, core, deeper, specialist) |
| `clusters.json` | Names for the generated galaxies and families in the Galaxy layout |
| `tours.json` | Text-only camera tours, their opening highlights, pacing, and standing |

All four are read at page load: save and reload, no build step.

## Editing a guided tour

- `opening_stops` is the explicit highlight sequence. Its order is shown exactly.
- `narration` supplies shared, natural-language subtitles for highlighted papers. It remains
  interface-draft explanatory prose until separately reviewed by the author.
- A territory tour admits only papers assigned to that territory. The Steward Tour may
  draw from the whole corpus.
- The Full sequence starts with `opening_stops`, then orders every remaining eligible
  paper using the transparent draft factors recorded in `ordering_method`.
- `dwell_seconds` controls the default caption time shown by the circular countdown. Readers may
  pause, scrub, change speed, or move backward and forward with wraparound.
- Change `standing` to `AUTHOR_CURATED` only after the sequence and its framing reflect
  the author's judgment. This does not transfer author standing to generated ordering notes.

## Editing a route

- Reorder, add, or remove objects in `stops`. Each stop needs an `accession_id`
  (`AC-####`) and a `why` (one or two sentences shown to the reader).
- Change `title`, `intro`, or `purpose` freely.
- When a route reflects your own choices, change its `standing` from
  `INTERFACE_DRAFT` to `AUTHOR_CURATED`. The site then labels it "From the author"
  instead of "Draft route".
- Add more routes by appending objects to `routes`. Give each a unique `route_id`.
  The first route is the one expanded on the home page.

Reload the page after saving. No build step is needed.

## Pinning a galaxy

`pinned_galaxies` in `clusters.json` places papers by hand: each entry has an `id` (`G:` plus
capitals, digits or hyphens, e.g. `G:PHYSICAL-WORLD`), a `name`, a `standing`, a `why`, and at
least 3 `members` (accession IDs). Unlike names, pins move papers, so rerun
`python tools/build_bridge_data.py` after changing them; the site warns until you do. The build
refuses unknown accession IDs, a paper pinned twice, or a malformed id, and names the problem.
Pinning moves only the pinned papers; every other paper keeps its galaxy.

## Naming galaxies and families

`clusters.json` names groups; it cannot change who belongs to them. Membership comes from
`tools/build_bridge_data.py` (half shared wording, half cross-links). Each `id` is the group's
most-listed paper: `G:AC-0059` is the galaxy whose most-listed paper is AC-0059, `F:AC-0014`
a family. The About page lists every group with its papers count and top words, which helps
when choosing a name. Change `name` freely and set `standing` to `AUTHOR_CURATED` when it is
yours. A group with no entry shows its top words with "(unnamed)".

If a rebuild gives a group a different most-listed paper (because the corpus changed), its
old id no longer matches: the site reports it as unknown on the About page instead of moving
the name to some other group.

## What the site does with mistakes

The site does not drop or repair anything silently:

- An `accession_id` that is not in `metadata/corpus.json` is shown in place as an
  error stop, and a warning lists it at the top of the route.
- An unknown `standing` value is shown verbatim with a warning.
- A duplicate `route_id`, or a file that fails to parse, is reported on the home page.
- In `depth.json`, unknown accession IDs or tiers and duplicates are reported on the About
  page and in the map legend; unplaced papers sit on a "Not yet placed" plane.
- In `clusters.json`, unknown ids, duplicates, empty names and unknown standings are
  reported on the About page (and flagged in the Galaxy legend); a missing file just leaves
  every group unnamed.
- In `tours.json`, unknown tours, territories, accessions, duplicates, and standing values
  are reported. An opening paper outside the selected territory is ignored rather than moved.

## Current state

All four files are interface drafts awaiting author review: five tours, one route, tiers for all 196
papers, names for 9 galaxies and 19 families (drafted 2026-10-26 from each group's top
words and members), and two pinned galaxies: Physical World (8 papers) and Cryptography (10 papers).

`R01 · Start with the failure` is an interface draft (problem-first ordering),
proposed on 2026-10-25 for author review. Five of its six steps join papers that
the generated cross-links do not connect (only Meaning as Binding → Governed
Meaning Base is cross-linked), so the route visibly crosses the map; that is
expected for an authored ordering.
