# TOOL-aCollapsedScan-1 — one awk pass per build, and `--plan` stops spawning per (unit, spec)

**Status:** CLOSED · rev-2 · 2026-08-26 · node a · Tier-1 · base da9e4cd2 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-build-TOOL-aCollapsedScan-1-1.md](../build/2026-08-26-build-TOOL-aCollapsedScan-1-1.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Make `unattended.sh --plan` cost a number of processes proportional to a build's UNITS rather than to
its units times its specs, without changing a byte of its output. Check 30 of
`check-unattended.sh` walks that verb over every tracked build on an unguarded merge-bar leg, so the
spawn count is paid by every node on every bar run and by every adopter of the kit.

## 2. Scope (IN)

- **S1** — Add `load_spec_facts`, one `awk` invocation over all of a build's tracked specs, emitting
  a path, heading id and status token per spec, and filling three `declare -A` maps: path to id,
  path to status, and id to path. A spec with no parseable heading or no status header yields an
  empty field, which is the same information the per-spec readers produced.
- **S2** — Replace the `NOT A UNIT` pass in `verb_plan` so it reads those maps instead of running two
  `awk` processes per spec, and replace its `basename` call with a parameter expansion.
- **S3** — Replace the region-id extraction, which runs a `printf` into `grep -oE` into `head -1` per
  row, with a single `awk` over the whole region that emits the first id match per row.
- **S4** — Replace the nested id-to-spec resolution loop, which runs an `awk` per (unit, spec) pair
  until it matches, with one read of the id-to-path map.
- **S5** — Replace the per-unit status re-read inside the grading loop with a map read.
- **S6** — Rewrite `spec_ids` so its per-build read is one `awk` rather than one per spec. It
  KEEPS its `dir` argument and stays stateless, and `missing_units` keeps its two-argument
  contract and its exit 3. Amended at rev-2: the first cut had `spec_ids` read the shared maps
  and had `missing_units` take the roster ids `verb_plan` had already derived, which broke the
  other caller. See §9.
- **S7** — Derive `_renderable` by counting map entries with both fields present, dropping the
  `sort` and `grep -c` that priced it.

## 3. Non-goals (OUT)

- Folding `plan_state` into the single pass. Both `tools/memory-tree/marker-contract.test.sh` and
  `tools/unattended/unattended.test.sh` lift its body out of the shipped bytes and evaluate it as a
  standalone function of one spec path. Its one `awk` per graded unit is the floor this unit accepts.
- A batch verb that plans many slugs in one process. It would save the per-invocation driver
  startup, measured at 0.28 s and therefore 20 s of the 235 s, and it would cost a new entry in
  `VERBS_INLINE`, the dispatch, the header docstring and the cross-file carrier join.
- Changing which builds check 30 walks. Recorded as a parked decision in the build README, to be
  reopened only if the measurement in AC3 leaves the leg above `BUDGET_kit_gate`.
- Any change to the output of `--plan`, its refusals, or their wording. AC1 exists to prove this.
- Declaring a per-leg wall-clock ceiling in `tools/gate-legs.json`. The manifest has no such field
  for any of its 85 legs, and adding one is a merge-bar contract change, not this unit.

## 4. Design

### Data model

`spec_facts` is the pure emitter: given spec paths it prints one row per spec and touches no
global. `load_spec_facts` calls it and fills three associative arrays for `verb_plan`'s own
lookups; `spec_ids` calls it directly and keeps no state, because `--close` reaches `spec_ids`
through `missing_units` with no `verb_plan` frame above it and would otherwise read maps nobody
had filled. The arrays are ASSIGNED at declaration with `=()`, not merely declared, because
`declare -A X` alone leaves X unset as far as `set -u` is concerned until something assigns to
it. `declare -A` is already used by
`tools/memory-tree/check-memory-hygiene.sh`, so bash 4 is an existing repo-wide assumption rather
than one this unit introduces.

| Map | Key | Value | An empty or absent value means |
|---|---|---|---|
| `SPEC_ID` | spec path | heading id | the heading does not parse as an id |
| `SPEC_ST` | spec path | status token | the file carries no status header |
| `SPEC_PATH` | heading id | spec path | absent: the region names an id no spec defines |

The single `awk` program emits one row per file using an `FNR==1` flush rather than the gawk-only
`ENDFILE`, so it stays POSIX awk for adopters. A zero-line spec file never triggers `FNR==1` and so
emits no row; `verb_plan` iterates the file list rather than the map, so that file still reports
`NOT A UNIT (no status header)` exactly as before.

`SPEC_PATH` keeps the FIRST path that claims an id, which is what the nested loop it replaces did by
breaking on its first match over the same `git ls-files` order.

### Inventory

Every reader of a spec's id or status inside `verb_plan`, with its cost before and after. `n` is the
build's spec count and `u` its unit count.

| Site | Before | After |
|---|---|---|
| the `NOT A UNIT` pass | `2n` awk | 0 |
| `_renderable` | 1 git, `n` awk, 1 sort, 1 grep | 0 |
| region id extraction | `2u` externals | 1 awk |
| id to spec resolution | up to `u` times `n` awk | 0 |
| per-unit status re-read | `u` awk | 0 |
| `missing_units` | 1 git, `n` awk, 1 sort | 1 git, 2 awk, 1 sort |
| `plan_state` | `u` awk | `u` awk, unchanged and deliberately so |

### Alternatives rejected

- **A pure-bash indexed-array scan instead of `declare -A`.** It removes a bash 4 dependency the
  repo already carries, and costs a linear scan per lookup for no measured benefit.
- **A helper returning values through command substitution.** Every call forks a subshell, and fork
  emulation on this platform is the cost this unit exists to remove. The maps are read inline.

### Files touched (estimate)

`tools/unattended/unattended.sh` only. No fixture, conf, manifest or gate-leg change.

## 5. Production-readiness checklist

- security — N/A. No new input, write path, credential or network call; the verb still only reads
  tracked files.
- perf / scale — the whole point. Measured before and after per AC3, on the real corpus.
- a11y — N/A. A shell verb with no user interface.
- i18n — N/A. Output is machine-graded ASCII and is required by AC1 to be unchanged.
- error / empty / loading states — the empty-spec-file case and the unparseable-heading case are the
  two that change shape internally, and both are pinned by AC1 and AC2.
- observability — unchanged. Every refusal keeps its id and its text.
- risks — a spec path containing whitespace would word-split, which is true of the code being
  replaced as well, so this is a pre-existing limit and not a regression. Recorded, not fixed.
- testing + left-shift gates — `bash tools/unattended/run-unattended-gates.sh --selftests` is the
  compensating check this kit's own header names as the DoD for work under `tools/unattended/`.
- migration / rollback — none. A single-file revert restores the prior driver.
- user docs — none owed. The contract in `memory/guides/UNATTENDED-PROTOCOL.md` describes behaviour,
  and behaviour does not change.

## 6. Acceptance criteria

- **AC1** — When `--plan` is run over every build under `memory/builds/`, its stdout and stderr are
  byte-identical to the pre-change driver's for all of them, proven by `diff` against output
  captured from the driver at `base da9e4cd2`.
- **AC2** — When `bash tools/unattended/run-unattended-gates.sh --selftests` runs, it reports a green
  verdict, including the `driver_selftest` suite that owns the `--plan` arms.
- **AC3** — When check 30's walk is timed over the same 70 builds on node `a`, it costs at most a
  third of the 235 s recorded at `base da9e4cd2`, and the figure is recorded in the build record.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs, it exits 0 and check 30's
  `_pv_seen` liveness assertion is satisfied by the same population as before.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs, the bar is green.

## 7. Gates

`unattended kit gate` · `playbook validity gate` · `unattended skill wiring` · the memory-tree
hygiene gate · the codebase-map coverage gate. No new gate: AC1 is a build-time proof over a corpus
that changes, not an invariant a leg can hold, and check 30 already gates the property that matters.

## 8. Open questions

- **F1 — Tier-1 or Tier-2?** A refactor inside a driver that a merge-bar gate parses could argue for
  Tier-2. Against it: no new write path, no migration, no auth or egress surface, and no shared
  contract moves. RESOLVED (agent, 2026-08-26, delegated): Tier-1, because AC1 diffs the entire
  output corpus against the prior driver, which is a stronger claim than a review lens produces.
- **F2 — fold `plan_state` in as well?** It would take the per-build cost close to the startup cost
  of the driver itself. RESOLVED (agent, 2026-08-26, delegated): no. Two harnesses slice its body
  out of the shipped bytes, so folding it breaks a cross-kit contract to buy `u` spawns.
- **F3 — build the change-scoping of check 30 in the same unit?** RESOLVED (owner, 2026-08-26): no.
  Scope approval was given for the spawn fix; the scoping is parked in the build README and is only
  reopened if AC3 leaves the leg above its declared ceiling.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft, written after the measurement that motivated it.
- rev-2 · 2026-08-26 · S6 amended after the driver suite went red on 12 arms. The rev-1 design
  had `spec_ids` read the shared maps and `missing_units` take a pre-derived roster, and
  `--close`'s build-complete term is a SECOND caller of both: it has no `verb_plan` frame to
  have filled the maps, and its `if ! _bcmiss=$(...)` depends on the exit 3 `missing_units`
  used to forward. Both contracts are restored and the awk emitter is shared instead.

## 10. Reuse audit

A `tools/codebase-map/reuse_lookup.py` pass for reading a spec status header and heading id returns
no shell seam. Every ranked candidate is Python in the memory-tree kit, and a cross-kit edge is what
that kit's conformance harness exists to forbid, so importing one is not available. The in-kit seam
is `spec_ids` in `unattended.sh`, which already answers which tracked specs parse as units and whose
own comment says it exists so two callers cannot disagree about what the id of a unit is. This unit
extends that function to read the new maps rather than adding a second reader beside it.
