# Ableman Corpus

## [Explore the Ableman Corpus Atlas](https://ablemanmosaic.github.io/ableman-corpus/site-bridge/)

**The Atlas is the primary human entrypoint into the papers, concepts, systems, territories, questions, and relationships of the Ableman Corpus.**

The Ableman Corpus is the versioned research collection of Adam Ableman. It develops a connected program around constitutional computing, governed artificial intelligence, sovereign software, semantic architectures, institutional coordination, and distributed knowledge systems.

The repository is organized as a readable library and as a machine-inspectable source collection. Each paper edition may include Markdown source, a PDF reading edition, an HTML projection, metadata, and a detached receipt binding those representations to one release root.

## Enter the corpus

The public interface begins with four overlapping territories:

- **Intelligence** — constraining artificial intelligence as power while making bounded capabilities broadly accessible.
- **Computation** — rebuilding computing around inspectability, reconstruction, collaboration, and user sovereignty.
- **Coordination** — governing complex institutions through explicit authority, evidence, delegation, and revision.
- **Possibility** — studying how potential configurations become selected, realized, evaluated, and reopened.

Enter through the live [Ableman Corpus Atlas](https://ablemanmosaic.github.io/ableman-corpus/site-bridge/) for galaxy, jurisdiction, similarity, guided-tour, reading-route, question, and paper views. The [Ableman Corpus repository](https://github.com/AblemanMosaic/ableman-corpus) is the versioned source collection beneath that interface; its [current paper editions](papers/current/) remain directly browsable.

The Atlas's tours, routes, depth tiers, group names, and pinned topical regions are curation layers rather than changes to paper identity. Its source is maintained in [`site-bridge/`](site-bridge/), and `python tools/build_offline_atlas.py` produces the self-contained offline edition.

## Repository map

```text
papers/       Current paper edition bundles
metadata/     Corpus and per-paper publication metadata
atlas/        Semantic indexes and source-bound navigation data
systems/      System catalog and separately releasable system materials
site/         Static dark-mode corpus interface
tools/        Local build, render, receipt, and verification tools
LICENSES/     Exact license texts
```

## Permanent accessions and historical chronology

Every logical paper has a permanent accession such as `AC-0001`. The initial accession sequence follows the earliest documented corpus timestamp: exact Zenodo upload time for published works and the earliest admitted version-family file timestamp for local works. Alphabetical order is now a view, not an identity scheme.

Existing accessions never change. A later-discovered older work receives the next accession while its historical date places it correctly in chronology views. See [the frozen accession ledger](metadata/accession-ledger.json) and [the readable chronology](metadata/HISTORICAL-CHRONOLOGY.md).

Only the current edition of each logical work is presented in the library. Git history preserves repository change history without presenting prior files as competing current papers.

Project57 is excluded from this public edition under the author's not-ready ruling. Two works retain their permanent accessions but are withheld from the public projection: *Technical Brief: Context-Compiled Consciousness Mode for Language Models* (`AC-0185`) pending independent Project57 replication and external source review, and *Qualia Binding and Realization Mapping* (`AC-0192`) pending empirical data, baselines, ethics review, and external scholarly review. References to withheld work in other papers remain where they form part of those papers' scholarly context; a reference does not promote the withheld work to public-edition standing.

## Artifact identity

A logical work, an edition, and an exact file are not the same identity. Markdown, PDF, and HTML receive separate SHA-256 hashes. A detached receipt commits those hashes, the metadata state, and the render recipe under one release root. The Markdown file is the editable source; the PDF and HTML files are projections of that source.

## Licensing

Papers and their direct MD/PDF/HTML projections are licensed under Creative Commons Attribution-NoDerivatives 4.0 International unless a paper states otherwise. Software and repository tooling are licensed under the Apache License 2.0. See [LICENSE.md](LICENSE.md) for the path-level boundary.

## Author

Adam Ableman  
Constitutional Computing  
ableman.research@gmail.com

