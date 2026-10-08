# TOOL-aMeteredSweep-1 — every red of a full bar with self-tests on the reconciled main, fixed

**Status:** OPEN · rev-1 · 2026-10-08 · node a · Tier-1 · base fa68a767 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A `GATE_FULL=1 GATE_SELFTESTS=1` bar over local `main` at `fa68a767`, the reconcile of local `main`
with `origin/main`, ran red on nine legs. Fix each at its cause, so the same bar over the fix runs
green on a quiet host.

## 2. Scope (IN)

- S1. `python resolver` — three expected-prompt strings in the build harness suite carry the ban's
  own `gov:literal-python` marker. Observed by AC1.
- S2. `codebase-map kit selftest` — the AC2 customised-gate fixture names `CARDS.md`, which
  TOOL-aMendedFleet-43 added to the engine's writes. Observed by AC1.
- S3. `run-gates gov canary` — the charter arms read the merge-bar guide, where PLAY-aMendedFleet-1
  moved the section they guard, and the guide names the ledger again. Observed by AC1 and AC3.
- S4. `foreign-prefix parity` — the gotchas suite's backslash arm derives its path from the install
  prefix rather than spelling `tools`. Observed by AC1.
- S5. `spec-tokens self-test` — every file read in the checker folds CRLF to LF, so a spec checked out
  under `core.autocrlf=true` reaches its section headings. Observed by AC1 and AC3.
- S6. `manifest-check self-test` — the unattended library stops forking a subshell per path
  normalisation and per kit descriptor, so `--claims` answers inside the card's bound. Observed by
  AC1 and AC2.
- S7. `run-gates run-log line` — the exit table rows the census sampler's three exits that
  TOOL-aGraftedHelix-5 added. Observed by AC1.
- S8. `govkit selftest` — `cmd_mint` gets its spawn-site row, and the migration fixture's synthetic
  gov ships the by-design checker TOOL-aGraftedHelix-28 made the parity script require. Observed by
  AC1.
- S9. `run-gates canary` — its memory-pause arm re-run on a quiet host decides whether it is a
  defect or contention; a defect is fixed here. Observed by AC1.

## 3. Non-goals (OUT)

No speed work beyond S6; the measured levers are the research record's, proposed and not built. No
ceiling or budget is raised to turn a red green.

### Edges

none

## 4. Design

Each red was read from its leg log in the profiled bar's clone, reproduced where the log was silent,
and fixed in the file that owns the fact. S6 keeps `normpath`'s answer byte-identical, checked
differentially over nineteen spellings, and reads the `_np` global it already set instead of
capturing it through a command substitution; the descriptor scan becomes one `awk` over every
`kit.toml`, each row tagged with its own file so an empty descriptor cannot shift the attribution.

### Files touched (estimate)

- `tools/workflows/unattended-build.test.sh`
- `tools/codebase-map/selftest.py`
- `tools/run-gates/run-gates.gov.test.sh`
- `memory/guides/MERGE-BAR.md`
- `tools/memory-tree/gotchas.py`
- `tools/check-spec-tokens.py`
- `tools/unattended/lib-unattended.sh`
- `tools/run-gates/run-gates.runlog.test.sh`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

## 5. Production-readiness checklist

- risks — S6 changes a library every unattended verb sources; S5 changes every checker read.
- testing — AC1 to AC3.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When each of the nine red legs is re-run at the fix commit on a quiet host, through the
  argv `gate-legs.json` declares for it, it exits 0.
  Red when: any of them exits non-zero there.
- **AC2** — When `unattended.sh --claims` is timed on node `a` beside the profiled bar's load, it
  answers in under a third of the 66 s it took before the fix. Red when: the resolver still spawns
  per descriptor or per path.
- **AC3** — When the guide's two pointers are renamed, or the spec-tokens suite runs with
  `core.autocrlf=true`, the canary and the suite red and green respectively. Red when: the canary
  passes without the pointers, or the suite reds on a CRLF checkout.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `codebase-map kit selftest` ·
`run-gates gov canary` · `foreign-prefix parity (every self-test at three prefixes)` ·
`spec-tokens self-test` · `manifest-check self-test` · `run-gates run-log line` · `govkit selftest` ·
`run-gates canary` · `memory hygiene` · `codebase-map adopter e2e` · `codebase-map gate coverage` ·
`govkit acceptance matrix` · `govkit refusal join` · `recall floor` · `recall floor arms` ·
`review-join self-test` · `tier2-review self-test` · `unattended-build self-test` ·
`verifier fan-out self-test`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft.
