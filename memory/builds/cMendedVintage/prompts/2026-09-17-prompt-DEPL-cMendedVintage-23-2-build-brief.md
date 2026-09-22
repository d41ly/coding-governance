# Build brief — DEPL-cMendedVintage-23

**Serves:** journal DEPL-cMendedVintage-23

Read the spec whole first, then read finding **B2** in
`memory/builds/cMendedVintage/reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md`.
Your spec was authored from that finding by an agent who opened every line it cites; the review
section still carries evidence the spec compresses.

*Standing note: this unit exists because the closing review returned BLOCKED. The build is 31 units
done plus one blocker repaired, and cannot land until this and its two siblings are fixed. Treat the
spec and this brief as evidence, not authority — the last three units each amended their own spec
after measuring, and one of them found a repair the MAIN LOOP had shipped was itself broken.*

## The defect in one sentence, and why it is the most dangerous one left

gov joins a path it read out of the target's own `install.json` onto the target root and writes
there, with no containment check. A receipt value of `../../evil` puts gov's bytes outside the
operator's repository. `install.json` is committed, hand-editable and text-merged, so the value is
not gov's to trust.

The inconsistency is what makes it a blocker rather than a hardening note: the ROLLBACK for that same
row already guards its paths with a containment check. The diff guards the undo of a write it does
not guard.

## The structural arm is the half that outlives this unit

Two `demand_contained_dest` calls close today's hole. They do nothing about the next write site
somebody adds. The review's left-shift proposal is the valuable half and your spec adopts it: a
STRUCTURAL arm asserting that every join of the target root with a receipt-supplied value is preceded
by a containment check on that same expression.

Run that candidate predicate over the real tree BEFORE wiring it, and print hits AND near-misses.
Doing so routinely surfaces live instances the original symptom never reached, and it catches a
predicate that would red an innocent join. `DEPL-cMendedVintage-21` did exactly this two units ago
and its first draft was wrong — it propagated through any right-hand side mentioning a destination
and pulled in three innocent names. Report both lists in your ledger even if the answer is one file.

## Where to put the check, and the trap in the cheaper answer

The spec chose its form and says why. Note the trap the minimum form leaves: the classification read
that sets the pin write and the pin drop happens EARLIER than the write sites, and it `continue`s
before the row ever enters the acted set — so the write loop's own containment check is unreachable
for this row. A guard placed only at the two write sites leaves the classification read ungraded. If
your measurement disagrees with your spec about that, amend the spec and say so.

## Observe the escape, not the exit code

The red you want is a file existing OUTSIDE the fixture target's root after a run. An exit code will
not show it, and neither will a diff of the target. Build the fixture so the escape lands somewhere
you can assert on, and assert the file is NOT there after the fix.

## Line numbers

The review cites `tools/govkit/govkit.py:7209`, `:7213`, `:7245`, `:7275`, `:6762`, `:6778`, `:6767`,
`:8227`, `:2398`, `:2462` and `:3964`, read at `b6cc8f6f`. `DEPL-cMendedVintage-22` has since landed
in that file. Locate every site by symbol and by the text the review quotes.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`selftest.py` or `matrix.py`. Spell no `tools/<kit>/…` path in shipped prose or comments.

## Required of every unit

gov keeps no govkit receipt, so no criterion here is observable against this repo — each needs a
scratch fixture target under the run's scratch root. Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-23-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape.** The backticked witness sits on the bullet's FIRST line, immediately
after the label; check 23 reads form from that line alone, so a witness on a continuation line is
graded `bad` however tidy it looks. The AMENDED form is `- AC2 — amended rev-<n> — …` and carries no
backtick. The token must share content with the criterion's own backticked token, case-folded either
way round. Check 23 is HELD under `--staged`, so no commit hook will tell you.

**The suite is runnable and you should run it.** The run is in VERIFYING, so `gate-guard.js` no
longer denies it. `python tools/govkit/selftest.py` is its own program, not a deployer subcommand. It
currently reports roughly 1352 arms green and 42 red, and then dies with a `FileNotFoundError` in the
`-14` reap fixture at `tools/demo/one/conf.txt`. Most of the 42 name
`GOVKIT_NO_REMOTE_PROBE` or a currency the run cannot verify offline. **None of that is yours** — it
is under separate triage. Report your own arms' verdicts and say whether the totals moved, and do not
spend the pass chasing a red you did not cause.

Bound every command at 900s or more.
