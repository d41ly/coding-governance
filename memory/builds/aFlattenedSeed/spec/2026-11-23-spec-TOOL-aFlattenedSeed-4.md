# TOOL-aFlattenedSeed-4 — the positional and encoding ledgers leave frozen records alone

**Status:** INPROGRESS · rev-1 · 2026-11-23 · node a · Tier-1 · base 4b5054df · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The seeds TOOL-aFlattenedSeed-1 armed on inCMS hold rows for frozen records. `positional-refs` lists
every file:line citation under `<MEMORY_ROOT>/archive/`, because the positional check treats only
`builds/` as frozen. The three encoding ledgers list sites in `<MEMORY_ROOT>/builds/` scripts,
because the encoding legs grade `memory/`, which the shell legs stopped doing in
TOOL-aFlattenedSeed-3. A frozen record is never rewritten, so a ratchet over it can only hold rows.
On inCMS those rows also copy brand-bearing paths out of exempt records into a swept ledger. After
this unit, no ledger the positional and encoding legs seed holds a row for a frozen record.

## 2. Scope (IN)

- **S1** — `tools/playbook/positional.py#derive_frozen` names `<MEMORY_ROOT>/builds/` and
  `<MEMORY_ROOT>/archive/`, and the check's three frozen readers read it: the grandfathering of
  unlisted citations, and the printing of unresolved pins and symbols. Observed by AC1.
  **Readers:** by name: `read_held_rows`, `check_positional` · by value: `positional.py list`, the
  population's seed, which prints the held rows less the grandfathered.
- **S2** — An empty registry argument to `encoding_posture.py` reads the population's home, as no
  argument does, in every mode. The default mode's flag is the empty string, so the argument filter
  no longer drops it. Observed by AC2.
  **Readers:** by name: `main` · by value: NO VALUE READERS, since the home it reads is unchanged.
- **S3** — The kit's three encoding rows pass the adopter `"" . :!memory`, and gov's own rows and the
  three seeds add `:!memory`. Observed by AC3.

## 3. Non-goals (OUT)

- A frozen prefix configured per adopter: `archive/` and `builds/` are the memory tree's own.
- Draining any adopter's existing rows: an adopter drops them with its next reseed.

### Edges

- **consumes-from** `TOOL-aFlattenedSeed-3` — the default-home reading and the `:!memory` population
  this extends to the encoding legs

## 4. Design

### Mechanism

`derive_frozen` returns a tuple, which `str.startswith` takes as it took the one prefix. The encoding
filter keeps an argument equal to the mode flag only when the mode is the default one.

### Files touched (estimate)

- `tools/playbook/positional.py`, `tools/playbook/gov_tag.py`
- `tools/gate-lint/encoding_posture.py`, `tools/gate-lint/kit.toml`

## 5. Acceptance criteria

- **AC1** — When `positional.py --selftest` plants a record under `memory/archive/` on a branch
  forked before the check lands, the check exits 0 and prints it grandfathered. Red when: it reads
  as unlisted. Observed red with `archive/` removed from S1 on 2026-11-23: the `positional-archived`
  plant failed with rc=1.
- **AC2** — When `encoding_posture.py --selftest` runs the default mode with an empty registry
  argument, then `.` and an exclusion of the memory root, from a planted root whose home declares
  the one site outside it, the run exits 0. Red when: it exits 2. Observed red against the base
  filter on 2026-11-23: got 2.
- **AC3** — When inCMS at branch/eager-booth-8ad943 runs the positional check with `archive/` frozen
  and its archive rows dropped, the check reports no unlisted and no stale row. Red when: an archive
  citation reads as unlisted. Observed 2026-11-23: 0 unlisted, 0 stale, and each archive citation
  grandfathered.

## 6. Gates

`tags positional selftest` · `encoding posture (text IO names its encoding)` · `policy fixtures` · `ratchet (seed laundering)` · `memory hygiene` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/positional.py · covers AC1 · the `positional-archived` plant; staged red with `archive/` removed from S1 · none
New arm: tools/gate-lint/encoding_posture.py · covers AC2 · `--selftest` runs the default mode with an empty registry argument over a pathspec; staged red against the base filter · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-23 · initial draft.
