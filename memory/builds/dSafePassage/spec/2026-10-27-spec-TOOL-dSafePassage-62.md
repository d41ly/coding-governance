# TOOL-dSafePassage-62 — `update` writes the receipt its file pass moved before the first step, so a walk killed below schema 4 leaves rows a rollback can return

**Status:** CLOSED · rev-1 · 2026-10-27 · node d · Tier-2 · base 60d90cb7 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0022@4bc8eba9 part 2/2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dSafePassage-62-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-62-ledger.md) | journal | — |
| [2026-10-27-prompt-TOOL-dSafePassage-62-build-brief.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-62-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md) | research | TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-5 TOOL-dSafePassage-51 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-59 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-5's build measured a release-0 walk killed during `govkit/receipt-schema-4`'s up,
then rolled back to the pin: the rollback exited 0, wrote no file, and left every file the killed
run's file pass had moved at the tip. The receipt the kill left still named release-0's bytes in
every `files` row, because below schema 4 the walk persists nothing (TOOL-dSafePassage-15 S1), so
the rows the write loop stamped in memory never reached the disk, and the rollback read each moved
file as an adopter's edit. This unit writes that in-memory receipt, `gov_commit` unmoved, before the
walk spawns its first step, which is the on-disk state TOOL-dSafePassage-2 S3 already promises at
every later step. Then a kill at any step leaves rows that name the bytes on disk, and
`update --rollback --to <the receipt's gov_commit> --write` returns them.

## 2. Scope (IN)

- **S1** — The write before the walk. In `_cmd_update`'s branch that walks the steps
  (`tools/govkit/govkit.py:11761-11763` at the branch head `41062397`), the run writes its in-memory
  receipt, with the rows its write loop stamped, `schema` as loaded and `gov_commit` unmoved, and
  the `install.sums` that receipt derives, before `upgrade_steps.run_step_walk` is called. A run that
  does not walk, a `--kits` run or one with a finding already, writes nothing here and keeps the
  findings path's write (`:12979-12988`). Observed by AC1 and AC2.
- **S2** — One writer of the receipt and its sidecar. `write_install_receipt(target, receipt_path, doc)`
  writes `.governance/install.sums` from every `doc["files"]` row carrying `sha256`, then the
  receipt as `json.dumps(doc, indent=2)` and a newline, each through `write_atomic`, in that order
  (TOOL-dRedressedBar-19 S40). S1 calls it, and so do the five sites that spell the pair today:
  `apply` (`:8614-8616`), `update`'s findings path (`:12980-12982`), its unattributed path
  (`:13025-13027`) and its stamp (`:13032-13034`), and `adopt` (`:13668-13670`). The comment over
  `ADOPTER_BAR_PATHS` (`:4279-4289`), which counts those sites, names the one writer, and the
  writer spells the declared member `"install.sums"` so the self-test's routing assertion
  (`tools/govkit/selftest.py:18073`) still finds it. Observed by AC3.
- **S3** — The plant. The `rollback-update` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `schema-up-kill`: over a target installed at A with a schema-3 receipt, `update --to B
  --write` is killed once the schema step's up has renamed schema 4 into place, the trigger
  `schema.block-after` TOOL-dSafePassage-19 added; the fixture prints the killed receipt's
  `gov_commit` and the vintage its `tools/demo/one.txt` row names, then runs
  `update --rollback --to A --write` from that state and prints that file's bytes, the receipt's
  `schema`, whether it holds `steps`, and its `gov_commit`. Observed by AC1 and AC2.
- **S4** — The docs. The "After a kill" paragraph of `help/upgrade-steps.md` says that a writing
  `update` records the files its file pass moved in the receipt before its first step, with
  `gov_commit` unmoved, so a rollback from a killed run's state to that commit returns those files.
  Observed by AC4.

## 3. Non-goals (OUT)

- A kill inside the write loop itself, before the walk. The clause asks for a step killed after its
  first write; the file pass's own index writes are journaled by TOOL-dSafePassage-2 S8 and a re-run
  converges over them.
- The walk's records. `run_step_walk` still persists no step row below schema 4, as
  TOOL-dSafePassage-15 S1 and AC2 require; the write of S1 is `_cmd_update`'s, before the walk.
- Staging the receipt. `update` leaves `.governance/install.json` and its sidecar unstaged today and
  this unit keeps that.
- The release-0 leg and its cases, which TOOL-dSafePassage-5 owns.
- The re-measure of `rendered` rows, `carry`, and the index mode rule, each of which TOOL-dSafePassage-5
  rev-8 compares under the record that declares it.

### Edges

- **hands-off** `TOOL-dSafePassage-5` — the `kill` case's rollback from the killed state of `govkit/receipt-schema-4`, which reaches release-0's digest only once the killed receipt's rows name the bytes on disk

Read and closed, so named here rather than joined: TOOL-dSafePassage-2's `run_step_walk` and its S3
on-disk state, TOOL-dSafePassage-15's rule that the walk persists nothing below schema 4,
TOOL-dSafePassage-4's `update --rollback`, and TOOL-dSafePassage-19's `rollback-update` plants and
their `schema.block-after` trigger.

## 4. Design

### Why the rollback kept the tip

Measured at `41062397` by TOOL-dSafePassage-5's builder (2026-10-27) and re-measured by this spec's
writer the same day over a fresh release-0: killed during the schema step's up, the receipt read
schema 4, `steps` empty and `gov_commit` the pin, its `files` rows still naming release-0's blobs.
The rollback left 38 paths different from release-0: the 36 files the file pass had moved, the
receipt and the index. `update --rollback --to <pin> --write` had classified every moved file by
`classify_row` (`tools/govkit/govkit.py:9079`): OURS, the target's index blob, which the killed file
pass had staged at the tip, differs from the row's stored `gov_oid`, the pin's; THEIRS, gov at `--to`, equals gov at
the row's `commit`, both the pin. `VERDICT_GRID` (`:8633-8645`) reads that pair `patched`, a local
edit, which the run keeps: `wrote 0`. Killed one step later, at the floor step, the same rollback
wrote 36 files and left none at the tip, because the schema step's `applied` record had written the
whole in-memory receipt (`write_step_record`, `tools/govkit/upgrade_steps.py:1175-1181`), rows
included, so OURS equalled the row and THEIRS differed: `stale`, written back to the pin's bytes.

So the defect is the window between the write loop and the first persisted step record. Above schema
4 the walk's first record closes it; below schema 4 nothing does until the run ends, and a kill in
that window leaves a receipt that does not describe the tree.

### The write

```
_cmd_update, --write, unscoped, no finding yet:
  write loop        rows stamped in memory, files written and staged (unchanged)
  S1                write_install_receipt(target, receipt_path, receipt)   # gov_commit unmoved
  run_step_walk     per step, as TOOL-dSafePassage-2 and -15 specify (unchanged)
  re-render, verify, stamp or findings path (unchanged; both now call write_install_receipt)
```

The schema step's up reads the receipt from disk and rewrites it whole
(`tools/govkit/steps/receipt_schema_4.py`), so after S1 its first write carries the moved rows too.
An uninterrupted run ends with the same bytes as today: the walk's next record and the final stamp
write the same in-memory receipt.

### Inventory

Minted: the function `write_install_receipt` in `tools/govkit/govkit.py`; the plant `schema-up-kill`
of the `rollback-update` family. Naming cell: `py.function`
(`python tools/lexicon/lexicon.py --suggest write_install_receipt --as py.function`, OK, 2026-10-27).
No conf key, gate leg, policy key or receipt field.

### Migration

None. The receipt's shape is unchanged; only the moment of one write moves earlier.

### Rollout

Live at landing. It sits in order 5 with TOOL-dSafePassage-5, which consumes from it, so it builds
first in that group.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Persist from inside the walk below schema 4.** TOOL-dSafePassage-15 S1 and its AC2 require the
  walk to write nothing on a schema-3 receipt, and that spec is closed.
- **Let the rollback read the dead holder's staging journal** to tell gov's writes from an adopter's.
  The journal names index blobs, not vintages, the reclaim consumes it, and a second reading of
  "who wrote this" beside the receipt is a second fact.
- **Stamp `gov_commit` at the tip before the walk.** A stopped walk must leave the stamp unmoved
  (TOOL-dSafePassage-2 S4), so the next run resumes from the commit it came from.

## 5. Production-readiness checklist

- security: no new spawn, path or input; one more atomic write of a file `update` already writes.
- perf / scale: one receipt and sidecar write per walking run, a few hundred rows.
- error / empty / loading states: a run that walks nothing writes nothing new; `write_atomic` keeps a
  kill from leaving half a receipt.
- observability: none new; the killed receipt is what a later run reads.
- risks: a site left spelling its own pair would let the sidecar order drift; AC3 counts the sites.
- testing: the `schema-up-kill` plant through the arm of §7.
- migration: none.
- user docs: `help/upgrade-steps.md`, "After a kill" (S4).

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update --plant schema-up-kill`
  runs, the rollback from the killed state exits 0 and the fixture prints the demo kit's `one.txt` reading
  `v1`, the receipt at schema 3 with no `steps` and `gov_commit` A, and exits 0.
  Red when: the write before the walk is absent, so the killed receipt's row still names A's blob,
  the rollback reads B's bytes as `patched`, and `one.txt` stays `v2`.
  cost: under a minute, two scratch repositories.
- **AC2** — When the same command runs, the line it prints after the kill names the receipt's
  `gov_commit` as A and its demo `one.txt` row as B's vintage.
  Red when: the receipt is written only after the walk, so the killed receipt names A's vintage for
  that row.
- **AC3** — When `git grep -n -F 'write_atomic(target / ".governance" / "install.sums"' -- tools/govkit/govkit.py`
  runs, it prints exactly one line, inside `write_install_receipt`; at `41062397` it prints five.
  Red when: any of the five sites keeps its own copy of the pair.
  figure: the five is PINNED, counted at `41062397` on 2026-10-27.
- **AC4** — When `git grep -n -e "before its first step" -- help/upgrade-steps.md` runs, it prints the
  "After a kill" sentence, and `python "tools/govkit/docs_leg.py"` exits 0.
  Red when: the page still says nothing of what the receipt holds after a kill.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · a `check_step_rollback` row running the `rollback-update` plant `schema-up-kill`, its failing case staged by the write before the walk taken out of a working copy · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, from TOOL-dSafePassage-5's build-run measurement of a rollback
  from a walk killed at the schema step, by `2026-10-27-prompt-TOOL-dSafePassage-5-4-spec-writer.md`.

## 10. Reuse audit

The seam extended is `_cmd_update`'s own receipt write: the findings path's
(`tools/govkit/govkit.py:12979-12988`), which TOOL-dSafePassage-2 S3 names as the walk's on-disk state,
called once more before the walk, and the pair of `write_atomic` calls five sites already spell,
extracted at this sixth caller as the charter's factory rule asks. `python
tools/codebase-map/reuse_lookup.py "write the receipt and its sums sidecar before a step walk so a
killed update leaves rows naming the bytes on disk"` ranked `rows`, `row`, `write`, `sum` and
`write_text`, name-token matches, and `write_record` (`tools/runlog/record.py`), a run log's: none
writes an install receipt, so no existing seam fits beyond the five copies named in S2. The recall
probe found TOOL-dSafePassage-15's ledger, whose killed re-run compared without `carry` because the
killed run persisted no receipt, and TOOL-dSafePassage-19's `rollback-update` plants this unit's
plant joins.

Recall terms used: `python tools/memory-recall/query.py "how does update leave the receipt when a run is killed or stops before the stamp, and what does a rollback read from it" --terms "receipt re-stamp withheld findings path partial update gov_commit rows killed walk rollback schema-3 persist"`
