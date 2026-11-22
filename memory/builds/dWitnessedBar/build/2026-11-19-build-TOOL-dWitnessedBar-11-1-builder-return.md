**Serves:** journal TOOL-dWitnessedBar-11

# TOOL-dWitnessedBar-11 — builder return 1 (run `wf_5b84961d-ee4`), a divergence, nothing committed

## Why

DIVERGENCE: spec rev-6 was grounded at e0236c47e, which is before units 12 (6b3f271c6), 22 (d92f12115) and 19 (e4e4e7ef0) landed. The 7h block they built does not match what §2 S7 and §4 "The gate" describe. The brief says to hand this back rather than build around it.

(1) §2 S7 and §4 "The gate" do not cover unit 19's purpose block. That block is tools/govkit/govkit.py@60b8fa09:2943-2975 at HEAD blob 60b8fa09, headed "7h: THE LEG'S PURPOSE". It grades every manifest row with three arms: presence, shape (not-a-string, 1 to 60 characters, one line) and uniqueness (two legs sharing a purpose), and it prints a `purposes: … pending` note. S7 only retires cf818f88cfd1:2764-2914, and that range ends before this block. The gate table's `purpose` row moves only "unit 19's shape arm" to the factory. Unit 19's hands-off says presence goes to the factory "once unit 11 retires 7h", but unit 51 S8 is the unit that adds `purpose presence` to `--conform`. So this spec has to say four things:
- which of the block's arms leave govkit in this unit;
- whether presence stays in 7h until unit 51 lands, or goes ungraded in the gap;
- whether the uniqueness arm is part of "unit 19's shape arm";
- where `PURPOSE_MAX_CHARS` (tools/govkit/govkit.py@60b8fa09:6116, read only by this block) lives once the factory grades the shape. Without that answer it is either an import of govkit or a second copy.
If I picked an option myself, AC9's red-when could fire (two graders for one fact), or the presence grading would be silently lost.

(2) S7's list of selftest plants to move is pinned at selftest blob b19bf481bc8a. Seven checks, runs f, g, h1-h3 and i1-i2, landed after it, at tools/govkit/selftest.py@45513099:1757-1817 (HEAD blob 45513099). Run f is the tag agreement (unit 12), run g is tests/enforces agreement (unit 22), and runs h1-h3 and i1-i2 are the purpose presence, shape, uniqueness and agreement checks (unit 19). S7 does not say which of these move to `leg_factory.py --selftest` (and under which arm, for example `fresh` for the agreement plants) and which are deleted with their arms. The brief names a run letter like these as a hand-back.

(3) The S7 population of comments naming 7h (`git grep -nP "\b7h(?![0-9a-z])"` over tools/) has grown from 18 lines at e0236c47e to 34 lines. The new lines are:
- tools/govkit/govkit.py@60b8fa09:2943 and :6115;
- the comments on selftest runs f to i;
- tools/run-gates/README.md:976 and :979;
- tools/run-gates/run-gates.gov.test.sh@d660e8c8:611, which is not in §4 Files touched.

(4) Files touched does not list four paths the change and its hooks need. I would normally declare these myself, so they are listed here only to complete the report:
- memory/guides/SESSION-KICKOFF.md, which needs a re-stamp because its watch line names tools/gate-legs.json;
- the codebase-map dossier claiming the two new legs (owed_rows.py's "leg added" population needs a dossier claim, and so does the gov canary's tests/claims join);
- memory/map/generated/symbols.json, for the new module;
- memory/builds/dWitnessedBar/RUN.md.

The claims that do still hold against the tree:
- `LEG_KEYS` at tools/run-gates/run-gates.test.sh@59f72ea6:354 holds tag, tests and purpose;
- 70 `[[gate_leg]]` rows across 27 descriptors, and 128 `[[exempt_leg]]` rows;
- 198 manifest rows, 51 carrying enforces;
- 147 `leg` pending rows, plus the `kind.gate-leg` pending row and its empty factory and gate;
- pass_legs.py's derive_pass_legs, render_pass_field, read_pass_evidence and read_ceilings;
- core.py's run_new, check_kind_row, run_meta_check and read_value;
- upgrade_steps.resolve_tokens, the `# >>> resolve_kit_dir` marker population, and both read_descriptors;
- the agreement arms for tag, tests/enforces and purpose, which §4's fold paragraph already covers.

## Summary

TOOL-dWitnessedBar-11 is not built and nothing was committed: its spec (rev-6, grounded at e0236c47e) no longer matches the 7h code units 12, 22 and 19 landed, so it goes back to the spec writer. The tree is clean, HEAD is unchanged at 22a4a128b, no path was written and nothing beyond the main loop's dispatch was declared.

The spec writer needs to settle three things before this unit is dispatched again:
- **Unit 19's purpose block** (tools/govkit/govkit.py@60b8fa09:2943-2975): which of its three arms leave govkit in this unit, whether the presence arm stays in 7h until unit 51 adds it to `--conform`, whether the uniqueness arm counts as "unit 19's shape arm", and where `PURPOSE_MAX_CHARS` lives once the factory grades the shape.
- **Selftest runs f to i** (tools/govkit/selftest.py@45513099:1757-1817): which of them move to `leg_factory.py --selftest`, and under which arm, and which are deleted with their arms.
- **The comments naming 7h**: there are now 34 lines in tools/ instead of 18, and one of them, tools/run-gates/run-gates.gov.test.sh@d660e8c8:611, is outside Files touched.

I can declare four further paths with `--dispatch` on the next pass: memory/guides/SESSION-KICKOFF.md for the watch re-stamp, the codebase-map dossier claiming the two new legs, memory/map/generated/symbols.json and RUN.md.

What I checked: the spec's claims about current code, read with grep and git show against HEAD and the cited blobs. This is the builder's pre-build check and stands in for no gate. The brief is already recorded in RUN.md (row 155, the same path), so I did not run `--brief` again, because that would only have changed a file I then had to restore. I ran no gate, suite or selftest. `gotchas.py --for-diff` did not run because there is no commit to give it.

Still owed to the close once the unit is built: AC1 to AC10 and the RED-first observation of the new arm `tools/run-gates/leg_factory.py --selftest`, which covers AC1, AC4 and AC5.
