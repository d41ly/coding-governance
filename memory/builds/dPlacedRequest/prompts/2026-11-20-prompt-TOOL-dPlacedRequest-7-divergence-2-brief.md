**Serves:** research TOOL-dPlacedRequest-7

# Brief — dPlacedRequest: TOOL-dPlacedRequest-7's second divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-7's builder returned a second DIVERGENCE (run `wf_1b6a10b9-c12`) and committed nothing: at rev-8
S2's `[[stand-in]]` rows name items no `[[transition]]` row names, which
`tools/loop/loop_table.py#check_transition_tables` refuses as stale; S8's `probe → item.probe.trigger` route on the
role items in a gov step is a cross-step route the same check's route join refuses; S8 on the probe program's own
items forms cycles `tools/loop/termination.py#check_counted` reports; two route targets in §4's table have no spelling
in `tools/loop/loop_lib.py#check_program`'s grammar; `trigger` takes no unit id the record's file name needs; and S9's
on-request observations name no request flag. The builder probed each refusal. Revise the spec to the main loop's
rulings, each a fork in §8 marked `RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none ·
relaxes: none`, and keep every change inside the unit's write set.

### Items

1. F-stand-in: drop the five `[[stand-in]]` rows; each unbuilt part rides its item's own `owner` field and a `stand-in:{prefix}/<home>/<file>` route. Reason: the stand-in table is one row per row item by its own grammar, and the probe items are no row items.
2. F-route: S8's `probe` outcome routes to the target `stand-in:{prefix}/loop/probe.py`, never to `item.probe.trigger`, so no route crosses a step and the route join owes no build row. Amend S8, AC9 and §6 to it.
3. F-cycle: the probe program's own items take no `probe` outcome; S8 and AC9 exclude them by name. Reason: a probe never asks for a probe of itself, and no counted cycle is formed.
4. F-targets: §4's `not-opened → the asker's next item` and `returned → the asker's re-entry` route to `stand-in:{prefix}/loop/probe.py`, the line `probe.py` prints naming the asker and its next item.
5. F-unit: S3's `trigger` takes `--unit <id>` beside `--build`, as `tools/memory-tree/build_records.py#write_record` needs a unit id for the record's file name.
6. F-observation: under `probe.observations=on-request`, an `observation` cause is refused at every position, and the owner opens a probe with `--cause owner`; S9 says so, and no new flag is minted.
7. §4 "The records" spells each field as a `- **Key:** value` bullet, the shape `build_records.py#FIELD` reads, under a `# <unit> <kind> <n> — <title>` head, as `write_record` writes.
8. S10: name the rows the new leg owes as `loop request fixtures` actually holds them (verify each registry against that leg; drop `tools/run-gates/ceiling-evidence.txt` from Files touched if that leg has no row there).
9. Name the `[[record-version]]` rows in `tools/loop/loop.toml` that items returning `record-kind.probe` or `record-kind.probe-trigger` owe under `tools/loop/loop_items.py`'s record join.

### Acceptance

Spec 7 at rev-9 carries the six resolved forks, S2, S3, S8, S9, S10, §4, §6 and AC9 amended, and one §9 line naming
this brief and the divergence; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest TOOL-dPlacedRequest-7` over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the driver's `--check-specs` and the naming
lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-7, and no fork left open: where a further choice appears, decide it by the same rung and record it
resolved. Pin every figure you write with DERIVED or PINNED, never let a section sign or a section number stand before
a unit word, never write a bare file-stem section reference, and never quote a check's hit literally in prose.
