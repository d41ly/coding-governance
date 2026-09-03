# Acceptance ledger — TOOL-dRetiredFork-17

**Serves:** journal TOOL-dRetiredFork-17

Tier-2 · node d · 2026-09-03

## The one change that converts a ratchet into a ban

`--write-ratchet` may now lower a count or drop a row that reached zero, and may **not** add one.
That is the whole conversion. Before it, the remedy the gate itself printed was a self-service
exemption form: a new literal redded the leg, the operator ran the suggested command, the baseline
was re-stamped, and the rise was gone without anyone deciding anything.

**Measured on this build, by me, an hour before writing the fix.** `DEPL-dRetiredFork-6` added one
runbook line naming the deployer's entry point, taking that file 28 → 29. The leg redded correctly.
I ran `--write-ratchet`, it absorbed the rise, and I only noticed because I diffed the file. That is
the defect, reproduced by its author on a live tree rather than argued for.

## Acceptance criteria

**Evidences:** TOOL-dRetiredFork-17

- AC0 — MET — the authoring rule is WRITTEN, in `AGENTS.md` §12 and `tools/hooks/README.md`,
  and NOT in the charter template whose remaining headroom S2 measured. rev-1 scoped it in S1
  and S2 and observed it nowhere, which is what this criterion was added to close.
- AC1 — MET, OBSERVED — a literal staged into `tools/codebase-map/README.md` makes
  `bash tools/check-install-prefix.sh` exit 1 with `UNRECORDED tools/codebase-map/README.md 1`.
  Reverted; green again. And two rises were caught for real before any staging: see below.
- AC2 — MET, OBSERVED — `bash tools/check-install-prefix.sh` exits 0 with the runbook literal
  carrying a hand-written reason column, reporting `118 recorded file(s), 1 hand-justified`.
- AC3 — MET, OBSERVED — a row naming `tools/lexicon/no-such-file.sh` makes
  `bash tools/check-install-prefix.sh` exit 1 with `SLACK ... 3 -> 0 (delete the row)`. A stale
  exception silently widens the surface it was written to narrow, so it reds in that direction
  too. Reverted; green again.
- AC4 — MET — `bash tools/check-install-prefix.sh` refuses an empty population rather than
  passing, via the pre-existing `carried_live` assertion, which this unit left intact and
  re-used for `--rebaseline` as well so the new mode cannot re-derive over a dead probe.
- AC5 — MET — a literal naming a LOOSE file directly under `tools/` is now caught, as predicate
  epoch 2. `bash tools/check-install-prefix.sh --rebaseline` took the ban list 105 -> 118 rows.
  This is `TOOL-aScouredKit-20`, and the measurement that shaped the fix is below.
- AC6 — MET, OBSERVED — `bash tools/check-install-prefix.sh --write-ratchet` run twice in
  succession leaves three consecutive states byte-identical, with `--check` green after each.
  This is `TOOL-dTieredTribunal-27` and it required a real fix, not just a measurement; the
  correction to my own brief is below.
- AC7 — MET — `grep -oHE` ran the candidate predicate over gov's tree BEFORE wiring, over a
  scratch copy of the same population `carried_population` derives, printing hits AND
  near-misses. It changed the design twice; the numbers are in the next section.
- AC8 — MET, with one correction owed and paid — `bash tools/check-testsuite-counts.sh` exits 0,
  and both legs declare a wall-clock ceiling in `tools/gate-legs.json`. The self-test leg's
  ceiling was 14x stale at HEAD; re-declared from measurement, and the class filed. Below.

## S5 changed the design twice, which is the whole argument for the rule

**First**, on class scope. The widened predicate finds 246 occurrences today's cannot see. Splitting
them by what S1 actually forbids — naming something *outside itself* — gives: **SELF 127 in 44
files, SIBLING 59 in 29, LOOSE 58 in 17.** The sibling set is the clean S1 violation, and roughly
half of it is `tools/lib/resolve-python.sh`, the one resolver every kit must source.

**Second**, on false positives. Of the 58 LOOSE hits, **76 occurrences across 7 files are FIXTURE
names** — `gate-a.sh`, `some-gate.sh`, `alpha.sh` — inside test helpers. A widened predicate wired
without this measurement would have redded seven innocent files on its first run. The fix is an
existence test: a loose-file literal counts only when the file is really there, which keeps 50 real
hits and drops all 76. Its one known false drop is `tools/manifest-check.sh`, real but shipped from
`skills/session-kickoff/`, so gov does not carry it at that path. Stated in the script, because a
heuristic with an unstated blind spot is how this arm acquired its first one.

## S4 — one defect fixed, one measurement corrected mid-flight

**`TOOL-aScouredKit-20` (loose files invisible) — FIXED**, as predicate epoch 2, with the existence
filter above. 105 → 118 rows.

**`TOOL-dTieredTribunal-27` (the writer does not reach a fixed point) — MY BRIEF RECORDED IT AS NOT
REPRODUCING, AND THAT WAS WRONG.** Under epoch 1 two consecutive writes were byte-identical, so I
wrote it down as already fixed. Under epoch 2 it fired immediately: `install-prefix-carried.txt`
rose 96 → 107 against itself. The ratchet was **grading itself** — every row in it IS a path, so
writing the file moves its own count, the next check reds, and no hand-edit settles it because the
edit changes the count again. Under the narrower predicate the number merely happened to sit still.

Fixed by excluding the file from its own population: a file whose entire content is a list of paths
cannot *carry* one, for the same reason the first arm already excludes this script and the waiver
registry. Verified after the fix: three consecutive writes byte-identical, and the check green after
each.

**A defect that reproduces only under a change you have not made yet reads exactly like a fixed
one.** That is the transferable part, and it is why the brief's measurement is quoted here rather
than silently replaced.

## The re-baseline, and why it is not the exemption form under a new name

A definitional widening makes many literals newly visible at once, so a ban with no re-baseline
would have to be hand-edited a hundred rows at a time or, realistically, switched off. So
`--rebaseline` exists — guarded by a `PREDICATE_EPOCH` declared beside the predicate and recorded in
the ban list's header. It refuses when the two agree, which makes it spendable once per predicate
change and useless for absorbing a literal. Observed refusing on its second invocation.

Hand-written reason columns survive every later write. Without that join the next legitimate drop
would erase every justification in the file, leaving a ban whose exceptions nobody could account
for.

## The correction owed under AC8, and the class behind it

The `install-prefix self-test` leg declared `ceiling: 1670`. Measured at **HEAD, unmodified**:
23066 ms and 24095 ms. Fourteen times over, and not caused by this unit — my five arms add about
300 ms, inside the noise. Nobody noticed because the leg is `chunk: selftests` behind a guard, so it
does not run unless asked: **a ceiling on a leg that never runs is a number nothing compares.**
Re-declared to 40000 from the measurement, with headroom for this node's threefold wall variance.
That fixes the instance; the class is filed as `TOOL-dRetiredFork-30`, since every other held
selftest ceiling is under the same blindness.

## The arms were mutation-tested, because five green arms prove nothing

B3's predicate was mutated `>` → `!=` and B2's `>` → `<`. Both redded with their intended messages;
both went green on restore. A first attempt mutating `>` → `>=` did NOT red, and it was my mutation
that was wrong rather than the arm — `1 >= 2` is still false. Recorded because I nearly accepted a
passing arm as proven by a control that could not have failed.
