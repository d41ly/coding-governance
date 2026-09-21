# cMendedVintage — the acceptance ledger for unit 5

**Serves:** journal TOOL-cMendedVintage-5

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh` suite
ran in this pass. Every line below was taken by running the gate itself at the shell, in the
worktree, and every red was staged and then removed rather than described.*

## The one thing worth reading twice

**The spec's Data model table was re-measured before a byte was edited, and its absolute figures were
wrong while its prediction was right.** Re-running the gate's own population derivation and all three
candidate regexes over it gives a population of 229 shipped source paths — unchanged — and occurrence
counts of 1148 as shipped, 1150 with `-` dropped, 1351 with `/` dropped. The table recorded 1307,
1317 and 1511 at BASE. So the live deltas are +2 and +203 rather than +10 and +204, and the brief's
own claim of 11 and "roughly 240" reproduced neither. That is not a defect in the spec: it named the
two survivors in advance, they are exactly the two occurrences the widening newly sees, and the
figure was written DERIVED for this reason. Logged as rev-3.

**`/` was re-measured, not inherited.** Dropping it too takes the count to 1351, and the addition is
dominated by correct spellings of gov's own checkout. It stays in the class, and the new test arm's
green control is what reds if a later pass forgets why.

**The one-shot rebaseline was spent in the mandated order and the diff proves it.** Predicate widened,
epoch bumped, then `--rebaseline` — and it moved exactly three lines: the epoch header, and the two
argv-default rows. Nothing else in 136 rows changed, which is the strongest evidence available that
the widening admits the class it was measured to admit and nothing beside it.

**This unit's own new bytes were checked against its own widened predicate, twice.** The trap the
previous unit found is real and `-` leaving the lead class makes it wider: a comment quoting a kit
path is now a hit at one more character than before. Measured on both files: the gate body counts 10
occurrences at HEAD and 10 after this unit's fourteen new comment lines, and the suite counts 8 at
HEAD and 8 after its 27 new lines. Neither moved, so neither needed a reason column it should not
have had.

**Evidences:** TOOL-cMendedVintage-5

- AC1 — `bash tools/check-install-prefix.sh --check` run twice over the real tree. With a staged
  break appending
  `ENGINE=${GOV_X:-tools/hooks/agent-cap.js}`
  to a file in the shipped population, the run prints
  `ROSE  tools/check-install-prefix.test.sh  8 -> 9`
  and exits 1 — the file is named and its count is one higher than its row. With the break removed
  the same command exits 0. The counter-proof for the criterion's own "Red when" was taken
  separately and is below.
- AC2 — `bash tools/check-install-prefix.sh --rebaseline` run after S1 and S2 were in the tree
  prints
  `install-prefix: REBASELINED for predicate epoch 3 -> 4.`
  and
  `install-prefix: rows 136 -> 136. Every hand-written reason column was preserved.`
  The second invocation prints
  `install-prefix: REFUSING to rebaseline. The recorded predicate epoch is 4 and the`
  and exits 1, and `git diff --stat` over the ban list after it shows the same three changed lines as
  before, so the refusal wrote nothing.
- AC3 — `tools/install-prefix-carried.txt` read after the rebaseline. Exactly two rows carry a count
  higher than at BASE `859daa67`: `tools/check-agent-cap-restatement.sh` 3 -> 4 and
  `tools/check-line-length.sh` 6 -> 7. Both were given a fourth-column reason by hand in this same
  commit, and the run after that edit reports 40 hand-justified rows against 38 before it. No other
  row moved in either direction, so there is no third row that could have arrived without one.
- AC4 — `bash tools/check-install-prefix.sh --check` against the unmodified tree after the
  rebaseline exits 0 and prints
  `install-prefix: carried-prefix clean — 136 recorded file(s), 40 hand-justified, none rising`
  above a first-arm line naming 268 shipped files. The graded population is non-zero on both arms,
  so `carried_live()` did not collapse under the rewrite.

Nothing is OWED. The spec numbers four criteria and all four were observed against the real gate.

## What did not run, and why

`tools/check-install-prefix.test.sh` gained two arms and was NOT executed as a suite, by this pass's
own mandate. **Its failing case was observed rather than assumed.** The two arms' bodies were
replayed verbatim in a scratch harness built from this same file's preamble, `mkfix_source` and
`carried_arm`, so the arms ran against the real gate through the real helpers:

| predicate in the tree | the `:-` default arm | the `/`-preceded control |
|---|---|---|
| epoch 4, as committed | ok | ok |
| `-` put back in the lead class | FAIL, rc 0 wanted 1 | ok |

The second row is the RED, and it is the two-sided one that matters: with the widening reverted the
red arm reports the gate clean at 2 recorded files while the control still holds, so the pair can
tell "the gate caught the default" apart from "the gate rejects everything". The gate was restored
from a byte copy afterwards and `diff` reports the file identical. The suite passes `bash -n` and
carries no CR bytes.

No gate ran here beyond the one under test. `install-prefix self-test`, `check-wiring self-test`,
`line length` and `dead-path carriers (deleted files still named)` are owed to the bar this run closes
with. `install-prefix (shipped surface)` is the one this pass ran directly, in its `--check` form,
because the ban list had to be rewritten in the same commit and a baseline left unwritten is a red bar
on a repair. `python tools/check-spec-tokens.py` was also run directly and exits 0, because
`--dispatch` refuses every unit of a build while that checker is red. It was run with this spec's
status held at SPECCED rather than CLOSED, because a CLOSED spec is terminal and goes ungraded: the
graded set went 44 live specs and 988 tokens to 45 and 1000, so the twelve tokens rev-3 adds were
actually examined rather than skipped past.

## What the bug-class checklist changed

`python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` named fourteen classes and two of them
landed on this commit's own bytes.

`amendment-leaves-its-other-half-standing` — rev-3 corrected the Data model table's figures and left
the `/` non-goal two sections above it stating the BASE reading in the present tense, so one
measurement answered in two figures. The non-goal now carries both readings and rev-3 names section
3 as well. This is the class the PREVIOUS unit's last commit was also about, which is the argument
for running the checklist rather than reading it.

`two-answers-to-one-question` — the epoch-4 comment block said the widening was measured over a
229-file population. That is a live count of a derived set written in prose beside the script that
derives it, and this file's own header already bans exactly that. The figure is gone; the delta
stays, because a delta is what an epoch cost when it was spent and it does not move afterwards.

`line-keyed-registry-reds-on-a-file-that-grew` was checked and does not apply: this commit inserts
eighteen lines into the gate, and no row in `tools/install-prefix-waivers.txt` is keyed to it.
`inline-fence-swallows-the-rest-of-the-file` was checked by counting added triple-backtick lines in
the two shell files: zero.

**Every observation in this ledger was then REPLAYED against the committed tree, after the last fold,
with the worktree clean.** An observation taken before a commit's final amendment is an observation
of a tree the commit never held. All returned identical verdicts.

Two things this unit deliberately left standing, both recorded in the ban list rather than repaired.
The waiver-registry default in `tools/check-agent-cap-restatement.sh` is overridden by the argv the
shipped gate leg passes, so it strands only a bare hand-run at another prefix. The declaration default
in `tools/check-line-length.sh` is not overridden by anything: its descriptor ships no declaration and
its gate leg passes no path, so an adopter at any other prefix is told NOT ADOPTED and grades nothing.
That is the better of the two arguments for having spent an epoch here, and draining it is a follow-up
nobody in this build carries.
