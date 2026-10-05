# TOOL-aEvidencedLens-19 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-19

Unit 18's byte tie, re-taken with every filter off. On this node `git config --show-origin --get
core.autocrlf` prints `file:C:/Program Files/Git/etc/gitconfig true`, and `git check-attr text eol`
prints `text: set` and `eol: lf` for `tools/workflows/tier2-review.js`, so plain `git hash-object`
normalizes line endings before it hashes.

Both inputs were saved from bash in the run's scratch, `git cat-file blob 028b5cac:tools/workflows/tier2-review.js > base.js`
and `git cat-file blob HEAD:tools/workflows/tier2-review.js > head.js`, at the pass's HEAD `015dceafd`; no PowerShell redirect and no text-mode write touched either file.
The driver is unit 15's `u15-check.js`, present in the run's scratch and copied unchanged (`cmp` clean against unit 18's copy), so it was reused and not rebuilt.
Its two arg sets are unit 15's, `r1+checklist+specs` and `r2+priorFindings`.

Staged breaks, each a scratch copy of `head.js`:

- `head-crlf.js` — `head.js` through `sed 's/$/\r/'`, 125282 bytes against 123594.
- `head-x.js` — `head.js` with one byte, `x`, appended, 123595 bytes.

**Evidences:** TOOL-aEvidencedLens-19
- AC1 — BASE blob `54cf03a30ce84f777247baeca5ce54a3a6410540`: `git hash-object --no-filters base.js` equals `git rev-parse 028b5cac:tools/workflows/tier2-review.js`, and `cmp base.js` against `git cat-file blob 028b5cac:tools/workflows/tier2-review.js` reports no difference. HEAD blob `3faf86625e6007a6174d21f93134b6d4ddc3f051`: `git hash-object --no-filters head.js` equals `git rev-parse HEAD:tools/workflows/tier2-review.js`, and `cmp head.js` against `git cat-file blob HEAD:tools/workflows/tier2-review.js` reports no difference. Both forms GREEN for both files.
- AC2 — `head-crlf.js` against HEAD's blob: RED under both forms, naming the file; `git hash-object --no-filters head-crlf.js` printed `7732dff5caaf9174022d138d539ff558abf560c2`, not the HEAD blob, and `cmp` printed `head-crlf.js - differ: char 22, line 1`. `head-x.js` against HEAD's blob: RED under both forms, naming the file; `--no-filters` printed `e06cb593d10e880d97121c9f75f3b0bb2ddea66d`, and `cmp` printed `EOF on '-' after byte 123594`. Plain `git hash-object head-crlf.js`, run beside them, printed `3faf86625e6007a6174d21f93134b6d4ddc3f051`, the HEAD blob itself: the filtered form reads the CRLF copy as equal, and the filter-off form does not.
- AC3 — `node u15-check.js --mask-class base.js head.js` on the two tied files: GREEN, rc 0. `r1+checklist+specs` prints BASE `aada6477` and HEAD `6380ce0a`, one `resume:probe` prompt per run, byte-identical under the class mask, `<KEY>` count 1 in each run. `r2+priorFindings` prints BASE `30f26c60` and HEAD `62ba7747`, one `resume:probe` prompt per run, byte-identical, `<KEY>` count 1 in each run. AC1's two forms re-taken after the run over `base.js` and `head.js`: still equal under `--no-filters` and still no `cmp` difference, so the driver read the bytes this record names.
- AC4 — this record, under the build's `build/` folder, carries the journal Serves line and this Evidences block, naming both blob ids, both assertion forms per file with their outcomes, both break reds, the plain-form output over `head-crlf.js` and AC3's outcomes per arg set, so check 23 reads it.
