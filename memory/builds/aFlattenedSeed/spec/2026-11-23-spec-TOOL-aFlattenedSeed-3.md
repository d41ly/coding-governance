# TOOL-aFlattenedSeed-3 — an adopter's ledger legs grade the population their seeds armed

**Status:** CLOSED · rev-2 · 2026-11-23 · node a · Tier-1 · base 87c8a917 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

inCMS seeded its gate-lint populations, and its bar still reds on six legs, because the adopter's leg
rows name no registry. `--shell-role`, `--quoting`, `--path-literals` and the three encoding-posture
modes then grade against an empty declaration and never read the home the seed armed. On top of that,
the shell legs grade `memory/` while their seeds exclude it, and the `encoding-posture-sites` seed is a
read-back of a legacy registry the adopter never held. After this unit, each adopter leg grades the
home its seed armed, over the same population.

## 2. Scope (IN)

- **S1** — With no registry argument, `sh_hygiene.py`'s `--shell-role`, `--quoting` and
  `--path-literals`, and `encoding_posture.py`'s three modes, read the population's home through
  `derive_default_registry`, as TOOL-dHomeGraded-1 S7 made the other four modes do. Observed by AC1
  and AC2.
- **S2** — The gate-lint kit's adopter rows for the three shell legs pass the seed's population,
  `. :!memory`, after an empty registry argument, which S1 reads as the home. Observed by AC3.
- **S3** — The `encoding-posture-sites` seed measures with `encoding_posture.py --measure`, as its
  `--stdout` and `--js` siblings do. Observed by AC3.

## 3. Non-goals (OUT)

- The read-back seeds of the other converted registries: each has a home every adopter converted.
- A `{prefix}` that names the repo root on a flat install's seed: here it widens the encoding seeds to the
  whole tree, which is the adopter leg's own population.

### Edges

- **consumes-from** `TOOL-aFlattenedSeed-1` — the flat-install seed that armed these homes
- **consumes-from** `TOOL-dHomeGraded-1` — `derive_default_registry`, the default-home reader S1 extends

## 4. Design

### Mechanism

`default = derive_default_registry(root, <home>)` when no registry argument is given and the run is no
`--measure`. The run's posture line names the default it read. `encoding_posture.py` imports the
helper from `sh_hygiene.py` beside it rather than copying it.

### Files touched (estimate)

- `tools/gate-lint/sh_hygiene.py`, `tools/gate-lint/encoding_posture.py`, `tools/gate-lint/kit.toml`

## 5. Acceptance criteria

- **AC1** — When `sh_hygiene.py --selftest` runs `--shell-role` with an empty ledger argument from a
  root whose `<MEMORY_ROOT>/project/shell-role.txt` holds the file's row, the run exits 0 and names the
  default registry. Red when: the home is ignored and the file reads as a row-less finding.
  Observed red against S1 removed on 2026-11-23: `(1, False)`.
- **AC2** — When `encoding_posture.py --selftest` runs the default mode with no argument from a root
  whose home declares the one unencoded site, it exits 0. Red when: it exits 1.
  Observed red against S1 removed on 2026-11-23: exit 1.
- **AC3** — When the adopter argvs grade inCMS at branch/eager-booth-8ad943, with its shell-role,
  quoting and path-literal homes seeded, every one of the three shell legs reads OK. Red when: any
  reports a `memory/` file with no row. Observed 2026-11-23 against inCMS d61dc604: each reads OK.

## 6. Gates

`shell-hygiene selftest` · `policy fixtures` · `ratchet (seed laundering)` · `ratchet (never gains)` · `memory hygiene` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/gate-lint/sh_hygiene.py · covers AC1 · `--selftest` reads a planted shell-role home with no ledger argument; staged red with S1 removed · none
New arm: tools/gate-lint/encoding_posture.py · covers AC2 · `--selftest` runs the default mode from a planted root with no argument; staged red with S1 removed · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-23 · initial draft.
- rev-2 · 2026-11-23 · S2 · AC3 · the bar's govkit selfcheck and writing-practice legs: the pathspec drops its slash, which selfcheck reads as a path no rule produces, and AC3 states no unpinned count.
