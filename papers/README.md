# Papers

Each directory contains one current logical-work edition bundle:

- `Title -- <release-root>.md` — editable source state;
- `Title -- <release-root>.pdf` — Pandoc reading projection;
- `Title -- <release-root>.html` — Pandoc HTML projection;
- `Title -- <release-root>.receipt.json` — exact hashes and render relationship.

The shared short identifier is the first twelve hexadecimal characters of the edition release root. It is not the byte hash of any single representation. Exact file hashes appear in the receipt.

No PDF-to-Markdown round-trip is used to establish identity. Every projection descends from the Markdown source recorded in its receipt.

