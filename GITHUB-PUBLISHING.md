# GitHub Release Discipline

The repository publishes the current GitHub corpus edition. GitHub publication and provider archival publication are distinct: a paper can be a public corpus edition before it receives a Zenodo or OSF record.

## Pre-v0.1 private-review snapshot policy

Until Adam Ableman explicitly authorizes v0.1 as complete, every update to the private GitHub repository replaces `main` with one fresh, parentless root commit containing the complete current review candidate. Do not append incremental commits to the private remote during this period. Each replacement must be guarded against concurrent remote change, preserve the repository URL and settings, verify the complete candidate tree before transfer, and confirm the remote tree and one-commit state afterward. This policy governs private review snapshots only; it does not authorize public release, provider publication, or a change to corpus standing.

## Candidate review

1. Open the local reader with `python tools/serve.py`.
2. Confirm the explanatory text, territory descriptions, entry questions, and author identity.
3. Sample paper headers, endings, equations, references, PDF pagination, and HTML output.
4. Review `metadata/corpus.json`, especially DOI and publication-date associations.
5. Confirm that `Project57`, `AC-0185`, and `AC-0192` are absent under the author's evidence-gated withholding rulings while the two permanent accessions remain reserved.
6. Run the semantic projection linter and verify `MANIFEST.json`.
7. Confirm that no credentials, provider drafts, databases, or private evidence are present.
8. Clear the local PDF geometry report in `.candidate/PDF-LAYOUT-REPORT.json`; structurally readable PDFs are not publication-ready while out-of-page text boxes remain.

## Release sequence

1. Rebuild the exact public corpus edition from the authorized successor set.
2. Verify semantic bindings, representation hashes, PDFs, manifest closure, and exclusions.
3. Record the manifest root in the release evidence and GitHub release notes.
4. Commit and tag the exact verified tree.
5. Push only under explicit publication authorization.
6. Refresh provider identifiers and publication dates in later releases as Zenodo or OSF records become available.

This file records procedure; publication authority remains external to it.
