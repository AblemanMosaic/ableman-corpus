# Metadata

`corpus.json` is the public library index. Per-work JSON records preserve permanent accession identity, logical identity, edition identity, historical and publication dates, source and projection hashes, license, format links, publication identifiers where already known, and corpus navigation fields.

`accession-ledger.json` freezes the initial historically ordered accession sequence. `HISTORICAL-CHRONOLOGY.md` is its human-readable projection. Existing accessions are never renumbered. Later works receive the next accession even when their recovered historical date places them earlier in a chronological display.

Historical chronology and accession identity are deliberately separate. The initial sequence was assigned by ascending earliest documented timestamp. Publication records use their Zenodo upload timestamps; unpublished version families use the earliest preserved file timestamp across the two author-specified Papers trees. These timestamps are documentary evidence, not proof of when an idea was first conceived.

Provider credentials, unpublished provider drafts, and publication-control state are excluded.

