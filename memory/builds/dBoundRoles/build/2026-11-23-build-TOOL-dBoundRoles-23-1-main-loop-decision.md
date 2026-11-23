**Serves:** journal TOOL-dBoundRoles-23

# TOOL-dBoundRoles-23 — the main loop's decision over the first builder's divergence

Run `wf_a398b95f-aed` read rev-7 against `5fed1e6b8` and wrote nothing. It handed back three things the spec leaves
open. First, the population "lister" that S2, S3 and AC3 lean on exists nowhere: the loop kit's item schema has no such
field, and the declaration verb `tools/roles/handoff.py#read_item_declaration` reads prints none. Second, AC1's heading
run contradicts S2 and the slot table. Third, an item's `upstream` field never reaches the render. Direct spawns of a
spec writer are still refused on this run: the session's spawn guard predates TOOL-dBoundRoles-17's `item=`. So the
main loop settles each item by M3 as a delegated resolution, and the next builder builds the result under the one
deviation record its brief names. widens: none · relaxes: the lister half of S2 and S3, cut below as a named gap.

1. **The population comes from the framing alone.** No unit of this build or the tree adds a lister, and the loop
   kit's item schema is outside the write set, so the lister branch is cut. The `population` slot holds
   `### framing:population`. Its entries are the lines that open with `- `. Past `FRAME_LIST_BOUND` entries, the block
   renders its text up to the twelfth entry and closes with `… and <n> more; the full list is <path>`. The path is
   the prompt writer's transcript, which `--framed-by` already resolves. That keeps the framing verbatim up to the cut,
   and the full list stays where it was written. S3's return bound for each `list` field is the population's entry
   count where `### framing:population` carries entries, else `FRAME_LIST_BOUND`. S2's refusal applies to a render
   carrying both `--item` and `--framed-by` whose framing has no `population`: it refuses naming
   `framing:population`. An unframed item render, which every harness stage is, has no framing to require it from,
   so it renders as today. The named gap is a lister an item declares, which belongs to whichever unit adds one to
   the loop kit's schema. No unit in this build's roster does.
2. **AC1 follows the slot table.** Its render adds `--item <fixture item>` and `--upstream <rows file>`. It runs over a
   fixture catalogue whose role reads `upstream:rows?`, as the roles suite's arm 23 fixture kit does, because no
   shipped role reads that key. The framing carries `job`, `population`, `added` and `nostop`. After the opening line
   the headings run: `### item`, `### framing:job`, the role's `reads` blocks, `### inputs` where the item hands
   inputs, `### allowance`, `### framing:population`, `### upstream:rows`, `### row contract`, `### framing:added`,
   `### framing:no-stop`, `### return`, then `### witness` last. Each `reads` block takes its slot by key, so
   `upstream:rows` sits in `upstream`, not in `material`. The arm is the render self-test's, over that fixture.
3. **S4 reads its upstream from the render's `--upstream`.** Its "where the item declares `upstream`" becomes "where
   the role reads `upstream:rows` and the render is handed `--upstream`", the path `UPSTREAM_KEY` in
   `tools/roles/handoff.py` already serves. The item's own `upstream` field reaching the render through the
   declaration verb belongs to the loop kit, outside this build, and stands as a second named gap.
4. **`check_return` gains its read of the work order.** §4 "The bound" says it already reads the work order for
   `answers`. At HEAD `tools/roles/roles_lib.py#check_return` compares the `(path, task_sha)` pair and reads no file.
   The bound check reads the work-order file at that pair's path, a new read and the only one.
5. **S7's plants are re-pinned at HEAD.** They are the render self-test's arm 11 and arm 19 profile plants in
   `tools/roles/render_agents.py#run_selftest`, and the roles suite's arms 19 and 21 in
   `tools/roles/adopt-roles.test.sh`. The builder records each blob-pinned line it moves in the deviation record.

The effort floor, S5 to S7, is unchanged: the builder found every seam it names at HEAD.
