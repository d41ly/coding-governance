**Serves:** journal TOOL-dDeclaredLoop-21

# Builder return — TOOL-dDeclaredLoop-21, dispatch 2: the new fail 37 branch moves the driver's refusal census past its ceiling, and rev-5 names no raise

## Why

DIVERGENCE: rev-5's §4 "Budgets and records" (and §4 "How the shell reads it", plus §4 Files touched) cannot be built as written. Building the spec's load_review_bounds would push the driver's refusal census over its REFUSAL_CEILINGS token, and the spec names no raise, no decision row and no .memory-tree.conf edit for it.

What §4 Budgets claims: "The driver's load-time refusal moves into `load_review_bounds`, one site for one ... so neither count is designed to rise."

What the tree shows: the load-time refusal being retired is not a census site.
- It sits in tools/unattended/unattended.sh#load_driver_conf as `echo "unattended: REFUSING - REVIEW_ROUNDS is ..." >&2; exit 2`.
- check-arms counts two kinds of site: fail branches matching `\bfail (\d+) "` (tools/memory-tree/check-arms.py#FAIL_RE) and refusal sites matching `exit 1` or `status=1` (check-arms.py#EXIT_RE and #STATUS_RE). An `exit 2` matches neither.
- .memory-tree.conf already records this. Its TOOL-dDerivedDocket-20 comment says "the driver pair does not move, because its conf-load refusal is an echo and not a fail branch".

What the spec asks for: §4 says "On a refusal it passes the module's stderr through, and `verb_review` fails 37".
- The driver's exit status comes only from `fail`. Its dispatcher ends in `exit "$status"`, and `fail()` is the only thing that sets status=1.
- So "fails 37" means a new `fail 37 "..."` branch, and the spec says load_review_bounds holds it.
- Removing the old refusal takes nothing out of the census, so the count goes from 326 to 327.

Measured at base 8a3bd0c8 with check-arms.py's own readers (branches and scan_refusal_sites, imported read-only):
- tools/unattended/unattended.sh: census 326 against the ceiling token `tools/unattended/unattended.sh:326:2026-11-15:TOOL-dDeclaredLoop-28`. Adding the branch makes it 327 against 326, and the `harness arms (fail branches armed or pinned)` leg reds.
- tools/unattended/check-unattended.sh: census 266, at its ceiling. S6 re-words check 2's existing `fail 2` in place and adds no branch to check 19, so this one stays flat as the spec says.
- Families in unattended.families.txt: missing-run-state 1/1, required-flag 11/11, field-shape 36/37. The new message must not contain `requires --`.

A raise needs:
- a row in memory/DECISIONS.md, which is under SHARED_RECORDS and so never in a pass's write set;
- .memory-tree.conf, which §4 Files touched does not list.

To make this buildable the spec must choose one of:
(a) Keep `verb_review fails 37`. Then §4 Budgets names the driver's raise from 326 to 327 under a decision id whose DECISIONS.md row lands ahead of the pass, as unit 30's did, and Files touched adds .memory-tree.conf (the REFUSAL_CEILINGS token and its comment line). Unit 30's planned raise from 326 to 328 then has to be re-based to 327 to 329, or the two units ordered so one decision covers both.
(b) Keep the census flat. The refusal stays a stderr echo with a non-fail exit, the shape of the one it replaces, and §4 drops "verb_review fails 37". The cost is that harness arms does not grade the refusal.

Every other rev-5 claim I probed holds at base 8a3bd0c8:
- REVIEW_ROUNDS readers: `git grep -n REVIEW_ROUNDS` matches S4's by-name and by-value lists, including loop_witness.py#HOLD_CONF, the conf of pass-tree.test.sh, check_policy.py#LEGACY_CONF and legacy-homes.txt.
- legacy-homes.txt already lists `.unattended.conf GATE_BOUND owner-policy`.
- The four catalogue keys and their defaults (3, one, 2, after-high) are in tools/policy/catalogue.toml and read through policy.py#resolve.
- review_state still tests zero, then non-decrease, then the ceiling (`-ge`), then the bound. verb_review still sets `bound=$RUNAWAY_CEILING` on the slug subject.
- In check-unattended.sh: `core_of RUNAWAY_CEILING`, check 2's empty-ceiling `fail 2`, and read_rounds_of with scan_round_writes are all there.
- The tier2-review.test.sh parity arm slices `^RUNAWAY_CEILING=` and review_state.
- fanout_cap.py, its [[upgrade]] row in tools/hooks/kit.toml (`needs-target = false`), its three usage.toml rows and its anchors on help/upgrade-steps.md are present.
- govkit selftest.py has the dSafePassage-1 arms block.
- The `loop upstream fixtures` companion rows that S2 follows are in gate-legs.json, registry.toml, subject-pins.tsv, selftest-budgets.txt and features/loop.md.

One constraint for the builder, not a divergence: memory/guides/BUILD-METHOD.md measures 30709 bytes against its 30720-byte cap, which leaves 11 bytes. The M4 rewording S4 asks for adds about 5 net (line 144's key name becomes `review.design.rounds`, and line 148 becomes "so no round bound bounds a chain"), so it fits only if worded that tightly.

## Summary

I committed nothing and changed nothing in the tree; HEAD is still 8a3bd0c8. TOOL-dDeclaredLoop-21 rev-5 cannot be built as written: the refusal the spec puts in the unattended driver would push its refusal count past the ceiling, and the spec provides no raise for it.

**The blocker:**
- §4 says the new function `load_review_bounds` holds the refusal and `verb_review` "fails 37". In this driver that has to be a new `fail 37` branch, because only `fail` sets a non-zero exit.
- The refusal it replaces is an `echo` followed by `exit 2`, which the refusal counter in `tools/memory-tree/check-arms.py` does not count. `.memory-tree.conf`'s own comments already say so.
- So the driver's count goes from 326, which is exactly its ceiling, to 327, and the `harness arms (fail branches armed or pinned)` leg goes red.
- A raise needs a decision row in `memory/DECISIONS.md`, which a pass may not write, and an edit to `.memory-tree.conf`, which §4 Files touched does not list.

**The spec writer has two ways out:**
- Keep the `fail 37`. A decision row raising the ceiling from 326 to 327 lands before the pass, and `.memory-tree.conf` joins Files touched. Unit 30's planned raise from 326 to 328 then has to be re-based to 327 to 329, or the two units ordered so one decision covers both.
- Keep the count flat by leaving the refusal as an echo with a non-`fail` exit, and drop "verb_review fails 37" from §4. The cost is that the harness arms leg does not grade it.

**What I checked:** I read the spec, the brief, the previous builder return and the build method in full. I probed rev-5's claims against the code with read-only greps and by reading the relevant functions. To measure the refusal counts I wrote a script at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/census21.py`, which imports check-arms.py's own readers without running the gate. It reported:
- driver: 326, at its ceiling of 326
- `tools/unattended/check-unattended.sh`: 266, at its ceiling, and this unit leaves it flat
- driver families: missing-run-state 1 of 1, required-flag 11 of 11, field-shape 36 of 37

That script stands in for the harness arms leg's ceiling check; nothing else stands in for any gate, and no gate, suite or bar ran. Every other rev-5 claim I probed still holds; the list is in `why`.

**Not done:**
- `--dispatch`: there is no dispatch row for this unit in `memory/builds/dDeclaredLoop/RUN.md`, and a divergence declares nothing.
- `--brief`: a brief row for this same brief file is already in `RUN.md` (03:05:42Z today), and a new one would have left an uncommitted change.
- `gotchas.py --for-diff`: there is no commit to run it over.
- No patch file: no product file was edited.

**Owed at the close once the spec is revised and the unit rebuilt:** the RED-first runs of the three `New arm:` lines (the review bounds fixtures for AC1–AC3, the govkit selftest arm for AC7–AC8, and the unattended and check-unattended suite arms for AC4 and AC6), plus the harness arms leg's census read after the build.

**For the next dispatch:** `memory/guides/BUILD-METHOD.md` is 11 bytes under its 30720-byte cap. The M4 rewording costs about 5 net bytes, so it only fits if worded tightly.
