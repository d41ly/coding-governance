# TOOL-aMendedFleet-22 — the generated views merge by taking one side

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · order 22

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`memory/LIVE.md`, the month shards under `memory/ledger/` and `memory/gotchas/INDEX.md` are wholly
generated, yet a merge that touches them on both sides stops on a text conflict that a person then
reconciles by hand, against the charter's rule that a generated index is re-rendered and never
reconciled. Check 9 and check 17 already red a stale render, so a merge can safely take one side and
let those checks name the regeneration owed. This unit routes the three views through git's `ours`
merge driver and wires that driver per node. The month shards' frozen columns are the sibling unit
`TOOL-aMendedFleet-81`, split from this one at F1.

## 2. Scope (IN)

- **S1** — `.gitattributes` gains `merge=ours` on `memory/LIVE.md`, `memory/ledger/*.md` and
  `memory/gotchas/INDEX.md`, under a comment naming check 9 and check 17 as what reds the side taken
  and `gen_build_index.py --write` and `gotchas.py --write` as the remedy. Observed by AC1 and AC2.
- **S2** — `tools/check-wiring.sh` gains a merge-ours arm modelled on `check_merge_rows`: one
  `git check-attr --stdin merge` call over the tracked paths; a skip row when no path declares
  `ours`; an `UNWIRED` row naming the remedy when `merge.ours.driver` is unset; under `--fix` and
  `--session` it sets `merge.ours.driver` to `true`; a value already set to anything else is
  reported `UNWIRED` and never overwritten. Observed by AC3.
- **S3** — The memory-tree kit README's merge-driver section and the `.gitattributes` step of
  `WIRE-INTO-PROJECT.md` carry the three attribute lines and the one config line, so an adopter
  wires the same thing. Observed by AC4.
## 3. Non-goals (OUT)

- A regenerate merge driver or a post-merge hook. The merge-driver dossier records why a driver
  cannot render: `ort` checks the result out only after the per-path merges, so a generator run
  from a driver reads the pre-merge tree. A hook writing files after every merge is a write nobody
  asked for. The remedy stays the two `--write` commands the checks name.
- The backlog views and the authored indexes keep `merge=rows`; the synthesis says keep it, and the
  row driver's refusal of a shard edit into a view depends on it.
- Build README generated regions. Each README is authored around its regions, and taking one side
  would drop the other side's authored lines with nothing to red.
- The generated map artifacts under `memory/map/generated/`, which the report did not name; the
  codebase-map freshness leg reds them the same way, and the same attribute would serve them.
- LIVE.md's own columns, which units 12 and 13 change.
- The month shards' columns and the frozen claim the `HYGIENE.md` line makes about them, which
  `TOOL-aMendedFleet-81` owns since the F1 split.

## 4. Design

### Evidence

Read at base `7af5f564`; no file below moved between it and `6a88fbf7`.

- Git ships no `ours` merge DRIVER; `ours` is a merge strategy. Probed 2026-10-04 on node a with git
  2.54.0.windows.1 in a fixture repository: with `merge=ours` and no `merge.ours.driver`, a merge of
  two divergent edits fell back to the text merge and stopped on a conflict, printing no warning;
  with `merge.ours.driver` set to `true` the same merge completed and kept the current side.
- All three views are rendered whole. `gen_build_index.py --check` byte-compares `LIVE.md` and every
  shard to a fresh render, and `gotchas.py --check` compares `gotchas/INDEX.md` to `render` whole, so
  taking one side loses no authored byte and leaves a file both checks call stale.
- `check_merge_rows` in `tools/check-wiring.sh` is the per-node wiring precedent: attributes read
  through `git check-attr --stdin`, a config value checked, and `--fix` setting it.
- `git log --merges` counts 88 merges touching `memory/LIVE.md`, 73 touching the September shard and
  22 touching `memory/gotchas/INDEX.md`; PINNED, counted 2026-10-04 at `6a88fbf7`.

### The attribute block

```gitattributes
# Wholly GENERATED views: a merge takes this side, and check 9 (gen_build_index.py --check) or
# check 17 (gotchas.py --check) then reds the stale result until `--write` re-renders it.
memory/LIVE.md merge=ours
memory/ledger/*.md merge=ours
memory/gotchas/INDEX.md merge=ours
```

The per-node half is `git config merge.ours.driver true`, set by S2's arm.

### Files touched (estimate)

- `.gitattributes`
- `tools/check-wiring.sh`
- `tools/check-wiring.test.sh`
- `tools/memory-tree/README.md`
- `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- **`merge=union`.** It concatenates both sides' rows, so the stale file carries duplicate rows that
  read as real until the next render.

## 5. Production-readiness checklist

- security — N/A: no new input or surface. The driver is the shell's `true`, which writes nothing.
- perf / scale — a merge of these paths no longer runs a text merge; one extra `check-attr` call
  in the wiring check.
- error / empty / loading states — an unwired node falls back to a conflict, which is today's
  behaviour, and the wiring check names it.
- observability — the stale side is named by check 9 or check 17 with its `--write` remedy.
- risks — a merge commit can carry a stale view until the next render; every push runs the bar,
  which reds it, so it cannot reach the remote unrendered.
- testing — direct runs in a scratch clone and one wiring self-test arm.
- migration — N/A: an attribute block and a per-node config value; no stored data changes.
- user docs — the kit README and the runbook step, S3.

## 6. Acceptance criteria

- **AC1** — When `git check-attr merge -- memory/LIVE.md memory/ledger/2026-10.md memory/gotchas/INDEX.md memory/DECISIONS.md`
  runs, it prints `ours` for the first three and `rows` for `memory/DECISIONS.md`.
  Red when: any of the three prints `unspecified`, or `memory/DECISIONS.md` no longer prints `rows`.
- **AC2** — When, in a `git clone --local` of the unit's branch under `%TEMP%` with
  `merge.ours.driver` set to `true`, two branches each commit a different extra line at the end of
  `memory/LIVE.md` and one is merged into the other with `git merge --no-edit`, the merge exits 0
  with no conflict marker in the file, and `python tools/memory-tree/gen_build_index.py --check`
  then exits non-zero naming `memory/LIVE.md`.
  Red when: the merge stops on a conflict in that file, or `--check` passes on the merged result.
- **AC3** — When, in that clone with `merge.ours.driver` unset, `bash tools/check-wiring.sh` runs,
  its merge rows include an `UNWIRED` row naming `merge.ours.driver`; after
  `bash tools/check-wiring.sh --fix`, `git config merge.ours.driver` prints `true`; and with the
  value set to `false` beforehand, `--fix` leaves `false` in place and the row stays `UNWIRED`.
  Red when: the unset driver reports `ok`, or `--fix` overwrites a value already set.
- **AC4** — When `grep -n "merge=ours" .gitattributes tools/memory-tree/README.md WIRE-INTO-PROJECT.md`
  runs, each file carries the three attribute lines, and the README names `merge.ours.driver`.
  Red when: either document lacks a line `.gitattributes` carries.
## 7. Gates

`memory hygiene` · `build-index selftest` · `check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `recall floor` · `recall floor arms` · `govkit runbook parity` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/check-wiring.test.sh · a scratch repo declaring merge=ours with the driver unset, set to true, and set to a foreign value · none

## 8. Open questions

- **F1 — Is S4 a second mechanism, owed its own unit?**
  The report bundles the shard columns with the attribute as one point, and both serve one goal: a
  generated view a merge never makes a person reconcile. They share no file, though, and each is
  built and observed alone: S1 to S3 are an attribute and its wiring, S4 is a renderer change.
  Options: keep one unit; split S4 and AC5 and AC6 into a new unit with `--rescope --act add`, this
  unit keeping S1 to S3 and AC1 to AC4. The build's rule is one mechanism per spec, so the
  recommendation is to split.
  RESOLVED (agent, 2026-10-04, delegated): split. S4, AC5, AC6 and F2 move to `TOOL-aMendedFleet-81`.
## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `render_shards`, `check_merge_rows`, the shard history
  and a fixture merge with and without the driver configured.
- rev-2 · 2026-10-04 · F1 resolved by split: S4, AC5, AC6 and F2 moved to `TOOL-aMendedFleet-81`.
- rev-3 · 2026-10-04 · §3 · §4 · §5 · §10 · M2 cross-read: the split left the shard half behind in
  prose. §3 still credited S4 with making the frozen claim true, and §4 evidence and alternatives,
  §5 testing and migration and the §10 `render_shards` seam described the column change
  `TOOL-aMendedFleet-81` now owns. Each moved to that spec or was cut.

## 10. Reuse audit

The seam extended is `check_merge_rows` in `tools/check-wiring.sh`, whose attribute read and
`--fix` path S2 copies for a second driver. Git's `merge.<driver>.driver` config is the platform
mechanism, so nothing new is built to take a side.
`python tools/codebase-map/reuse_lookup.py "merge attribute for a generated file so a merge conflict takes one side"`
named `merge` in `tools/memory-tree/merge-rows.py`, the row driver this unit leaves in place, and no
take-a-side seam, so none fits beyond git's own. Recall named `TOOL-aMendedLedger-1`, which made
LIVE.md and the shards generated, and a landing record of `TOOL-aHoistedPass-1` that re-rendered four
generated files by hand after a merge, the cost this unit removes. Where the report and the tree
disagree: its conflict data predates the 2026-09-28 switch-over,
after which version carriers cause most conflicts, so the size of this unit's effect is unmeasured.

Recall terms used: `python tools/memory-recall/query.py "how should a merge handle the generated LIVE.md and ledger shards, and was a merge driver for them declined" --terms "merge=ours merge=rows generated view LIVE.md ledger shard regenerate driver gitattributes check 9 stale render conflict"`
