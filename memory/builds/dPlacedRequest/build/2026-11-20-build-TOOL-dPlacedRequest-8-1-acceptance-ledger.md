# TOOL-dPlacedRequest-8 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-8

The unit was built from its spec at rev-7 (PINNED) on base `bf6abc3b2`. The item kind's schema,
`tools/loop/item-schema.toml`, gained the `seed`, `map` and `unfolds` field rows, each scalar's `widens`
order its value set; thirteen (DERIVED) role items of `tools/loop/loop.toml` declare a `seed`. The loop
reader gained `tools/loop/loop_lib.py#check_item_seeds`, `tools/loop/loop_lib.py#read_seed_values`,
`tools/loop/loop_lib.py#resolve_item_seed`, `tools/loop/loop_lib.py#resolve_seed_path` and the `seed`
command, `tools/loop/loop_lib.py#run_seed_command`, with four plants. The driver's token test moved
into `tools/unattended/unattended.sh#read_path_tokens`, which
`tools/unattended/unattended.sh#read_files_touched` now pipes the Files touched lines into, and the
read-only verb `--path-tokens [--files-touched <rev> <spec> ...]` joins the header, the verb carrier,
the Skill and `help/loop.md`.

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe of the changed
code: the loop reader's own `--fixture --plant` command, a `python -c` call of its functions, or the
driver run over this tree and over a scratch repository holding only a one-line `.unattended.conf`.

**Evidences:** TOOL-dPlacedRequest-8
- AC1 — `grep -n -A3` over the schema prints the three rows with their shapes and directions. The
  playbook kit's `tools/playbook/overlay_rows.py#read_field_decl`, called on each row, returned no red:
  `seed` and `map` read as scalar orders, `unfolds` as a set widening by `add`. The composed check
  `python loop_items.py check` reads HEAD, so it is owed at the close.
- AC2 — `check_item_seeds` over `read_items` of this tree printed `loop: seed <tag> · <value>` for each
  item and `loop: seeds · 13 declared · 54 none` (DERIVED), no refusal; the 13 (DERIVED) declared lines
  are exactly the items of the spec's declarations table, each with its value.
- AC3 — `--fixture --plant seed-bad` exited 1 (PINNED) with two refusals naming
  `item.plan.place seed 'write-set'` on its `command:plan.place` actor and `item.build.unit-pass seed
  'diff'` outside the four values.
- AC4 — `--fixture --plant seed-write` exited 0 (PINNED): `seed item.build.unit-pass --build tFix --unit
  TOOL-tFix-1`, run in the plant's scratch repository, printed `fx/seed-plant.txt` once, without its
  `./`. Over this tree, `seed item.build.unit-pass --build dPlacedRequest --unit TOOL-dPlacedRequest-8`
  printed the 13 (DERIVED) Files touched paths, the last with its trailing `/` dropped.
- AC5 — `--fixture --plant seed-question` exited 0 (PINNED): with a question naming two backticked
  paths the command printed both, and with no `--question` it exited 2 (PINNED) naming the flag. The
  plant's paths sit under its own scratch `fx/` folder, since a shipped kit file spells no tool-root
  path; the question's shape is the criterion's.
- AC6 — `--fixture --plant seed-scope` exited 0 (PINNED) printing the one line `unarmed — scope-paths: no
  plan record carries a scope; dRankedPlan's plan.record arms it`.
- AC7 — `bash tools/unattended/unattended.sh --path-tokens --files-touched HEAD <this spec>` exited 0
  (PINNED) and printed 13 (DERIVED) paths, byte-identical to what the base's own `read_files_touched`,
  extracted from `bf6abc3b2` and sourced alone, printed for the same spec.
- AC8 — `grep -n "question-paths" loop.md` in `help/` finds the new section on the seed, which names the
  four values and the `seed` command, and the item kind's field list.
- Other answers, by probe: a missing `--unit`, a `--build` of `../x`, a unit no spec defines, an item no
  row declares, a repeated flag and no item each exited 2 (PINNED) naming why; with the driver made
  unresolvable a `question-paths` seed printed `unarmed — question-paths: no unattended driver
  resolves`; from a directory in no work tree the command exited 2 (PINNED) naming it. The verb's three
  refusals, no spec after `--files-touched`, another flag, and a spec git cannot read, each exited 2
  (PINNED) with one `path-tokens not read` line. The `conf-readers-declared` plant still held.

**Owed at the close.** The two `New arm:` lines of section 7: the four seed plants under the `loop
definition` leg's `--selftest`, RED-first on `seed-bad`'s staged break; and the `--path-tokens` block of
`tools/unattended/unattended.test.sh`, 8 assertions (DERIVED: 7 `same`, 1 `hit`) in region one beside a
parity row, RED-first by dropping the `/`-or-extension half of the token test; the suite is waived for
this build's landing by README rule 8. `FLOOR_ASSERTIONS` and `FLOOR_SHARD_1` rose by 12 (DERIVED). The
`loop item kind` leg's `check`, `loop_lib.py --check` over the tree, the docs leg, the kit gate's check
26 and the size leg are the close's. The Skill's size row rose by the 56 bytes (DERIVED) of its new
line under the run-raise terms of `tools/template-size-limits.txt`; its decision row is the main loop's.
