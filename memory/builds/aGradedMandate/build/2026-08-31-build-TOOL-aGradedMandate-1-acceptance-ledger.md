# aGradedMandate — the acceptance ledger

**Serves:** journal TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11

*Node `a`, 2026-08-31. One line per numbered criterion, in one of the ledger's two forms and no third.
The measurements it cites, once, so no line repeats them: the driver suite
`bash tools/unattended/unattended.test.sh` is GREEN at 895 assertions, up from 864; the gate leg
`bash tools/unattended/check-unattended.sh` is GREEN end to end over this tree; and the leg's own
suite `check-unattended.test.sh` was NOT run, on an explicit owner instruction given mid-build, which
is why several criteria carry the AMENDED form rather than a false OBSERVED one. No count is written
here for those: the lines below are the population, and a number typed beside a set it does not derive
is this repo's own named defect.*

## What a staged break bought, since four criteria rest on it

Five refusals were driven RED against staged breaks and then reverted, each with its passing control:

| Break staged | Refusal observed |
|---|---|
| `DOD_NO_OVERRIDE` gains `bogus-item` | check 16, the driver-side direction, naming `bogus-item` |
| the Skill paragraph gains `invented-item` | check 16, the Skill-side direction, naming `invented-item` |
| `PARK_ACTS_OWED="retire supercede"` | check 2, the parked-ACT taxonomy, naming `supercede` |
| `CORE_FLOOR="12:10"` | check 3, `declared against core: 10 against 11` |
| units 10 and 11 flipped `WONTDO`, unit 3's retire row deleted | check 24 three times and check 2 once |

The last row is the one worth reading twice. `TOOL-aGradedMandate-10` and `-11` are the units the
closing review named as provably outside the roster at the pinned BASE, and its BLOCKER was that they
could be flipped to `WONTDO` with no rescope row and no output at all. After the fold they produce
three refusals, one per dropped unit, and the promotion clause fires alongside. The regression the
review found is closed by the scenario the review used to describe it.

## The pinned-roster census, which two criteria cite

`pinned_units` run over all 28 tracked `RUN.md`: it RESOLVES for 14 and REFUSES for 14. Of the
refusals, twelve are `no units region at the pinned commit` — build READMEs predating the region —
and **two are the empty-roster refusal this build added**, `aBoundedCeiling` and `aLexedStripper`.
Without that refusal both would have returned success with an empty roster and every `WONTDO` unit in
them would have been graded against nothing.

**And the skip branch those 14 would take is NEVER REACHED on this tree, which is worth saying
plainly rather than leaving to be inferred.** Check 24's population is the NON-TERMINAL run-state
records that carry a README — two of them here, `aGradedMandate` and `aThawedCorpus` — and
`pinned_units` RESOLVES for both. Every one of the 14 refusals is a TERMINAL record check 24 does not
grade. A full leg run under `GOV_UNATTENDED_REPORT=1` emitted exactly two report lines and both were
check 23's. So the census proves the refusal is real and common; it does not prove the skip branch
runs, and `TOOL-aGradedMandate-6` AC3 records that branch as unexercised.

**Evidences:** TOOL-aGradedMandate-1
- AC1 — `unattended.test.sh` — an arm strips `bcopen`'s round with `crdrop` and asserts `--close` blocks naming the absent loop; green in the 895-assertion run.
- AC2 — `unattended.test.sh` — an arm records `BLOCKED · blockers 1` with no terminal token and asserts the block plus the quoted count.
- AC3 — `unattended.test.sh` — an arm records `CONVERGED` at three blockers and asserts the hand-edit refusal.
- AC4 — `unattended.test.sh` — three arms, one per legal exit, each asserting the item is not reported.
- AC5 — `grep -c "46 records" tools/unattended/unattended.sh` — returns 0, and the replacement sentence names the measured 208/170 pair.
- AC6 — amended rev-4 — see the section 9 line: `run-unattended-gates.sh --checks` reports all three checks `ok` and then reds the WRAPPER on a 845s-against-120s budget breach caused by measured contention, so the criterion names the three verdicts rather than the wrapper's exit.
- AC7 — `build/2026-08-31-build-TOOL-aGradedMandate-11-closing-loop-census.md` — the probe was executed over all 28 tracked records, 7 pass and 21 refuse, and the record carries its own re-runnable bytes.
- AC8 — `bash tools/unattended/unattended.sh --status aGradedMandate` — this run's closing rounds are recorded under the bare slug `aGradedMandate`, so its own record satisfies the exact-subject join.

**Evidences:** TOOL-aGradedMandate-2
- AC1 — `unattended.test.sh` — an arm removes the fixture's audit record and asserts `--close` blocks naming `ARCH-tRun-1`.
- AC2 — `unattended.test.sh` — an arm restores a record binding the id and asserts the item is not reported.
- AC3 — `unattended.test.sh` — an arm leaves the record untracked and asserts the item still blocks, since the join reads the index.
- AC4 — `bash tools/unattended/check-unattended.sh` — green at `CORE_FLOOR="12:11"` in both conf carriers, and RED with `12:10` at `check 3 ... declared against core: 10 against 11`, with the control observed clean.
- AC4a — amended rev-3 — see the section 9 line: the criterion named the suite the owner instructed this run to skip.
- AC4b — `bash tools/unattended/check-unattended.sh` — check 16 is green with the protocol reading `Eleven kit-owned core items.` against an eleven-member `DOD_CORE`.
- AC4c — `unattended.test.sh` — two arms: `ARCH-tRun-1..3` satisfies `ARCH-tRun-1`, and `ARCH-tRun-19` does not.
- AC5 — `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` — byte-identical after both edits.

**Evidences:** TOOL-aGradedMandate-3
- AC1 — amended rev-3 — the unit is RETIRED before any code; every criterion below describes an escalation that was never built, and the section 8 fork records why.
- AC2 — amended rev-3 — as AC1.
- AC3 — amended rev-3 — as AC1.
- AC4 — amended rev-3 — as AC1.
- AC5 — amended rev-3 — as AC1.

**Evidences:** TOOL-aGradedMandate-4
- AC1 — `unattended.test.sh` — an arm points the fixture at a dated spec whose section 6 is empty and asserts `--close` blocks naming the unit.
- AC2 — `unattended.test.sh` — the same fixture under a cutoff after its filename date is not reported.
- AC3 — `unattended.test.sh` — the same spec with an acceptance criterion added is not reported.
- AC4 — `unattended.test.sh` — `--plan` prints `DONE (THIN)` for a closed thin unit and a bare `DONE` for a closed complete one; the second half is the arm that can fail, since `DONE` alone is contained by both.
- AC5 — `bash tools/unattended/check-unattended.sh` — green with `SPEC_THIN_CUTOFF` declared in the project conf, the kit example and the protocol's section 8 table, which is check 22's three-way key join.
- AC6 — `unattended.test.sh` — covered by AC1's arm, which runs against a fixture whose other terms pass, so the THIN message is the one returned.
- AC7 — `bash tools/unattended/unattended.sh --status aGradedMandate` — the driver runs under `set -u` against this project's conf and every fixture conf, including the one declaring no cutoff at all.

**Evidences:** TOOL-aGradedMandate-5
- AC1 — `unattended.test.sh` — an arm records a retire row, attests a count of 0, asserts the mismatch refusal, then attests 1 and asserts it clears.
- AC2 — `unattended.test.sh` — an `add` row is not counted among the decisions the owner is owed.
- AC3 — `bash tools/unattended/unattended.sh --status aGradedMandate` — on this run's own record the counts moved from `parked 1 · noted 6` to `parked 2 · noted 5` when the act axis landed.
- AC4 — `bash tools/unattended/check-unattended.sh` — green in both arms that read the set, and check 2's act arm observed RED against `PARK_ACTS_OWED="retire supercede"`.
- AC5 — `bash tools/unattended/adopt-unattended.sh --check` — the protocol pair is byte-identical after fact 3's correction.
- AC6 — `grep -c 'of eight kinds' memory/guides/UNATTENDED-PROTOCOL.md` — the enumeration now names all eight kinds and the surfaced sentence names both axes.
- AC7 — `grep -c 'Membership is declared once'` — returns 0; the replacement names both declarations and both axes.
- AC8 — `bash tools/unattended/check-unattended.sh` — the staged `supercede` break fired `the parked-ACT taxonomy names an act --rescope's own closed case cannot accept`.

**Evidences:** TOOL-aGradedMandate-6
- AC1 — `bash tools/unattended/check-unattended.sh` — staged over the live record rather than a fixture: units 10 and 11 flipped `WONTDO` and unit 3's retire row deleted produced three check-24 refusals naming each unit.
- AC2 — `bash tools/unattended/check-unattended.sh` — with the retire row restored, the leg is green over the same records.
- AC3 — amended rev-4 — see the section 9 line: the branch is UNEXERCISED on this tree, because check 24's population is the two non-terminal records and `pinned_units` resolves for both; a full leg run under `GOV_UNATTENDED_REPORT=1` emitted two report lines and neither was this one.
- AC3b — amended rev-4 — the mirror direction needs a record whose live-phase baseline fails while its pinned BASE resolves, which no tracked record is in and no fixture was built, so it is recorded as unobserved rather than claimed.
- AC3c — `pinned_units "" <readme>` — a blank base returns the named sha-shape refusal at rc 1, which is the arm that matters: an empty value is INDEX syntax and would otherwise have graded the working index.
- AC4 — the pinned-roster census above — `pinned_units` over all 28 tracked records, 14 resolve and 14 refuse, with every refusal reason named.
- AC5 — `bash tools/unattended/check-unattended.sh` — green at HEAD.

**Evidences:** TOOL-aGradedMandate-7
- AC1 — `bash tools/unattended/check-unattended.sh` — with units 10 and 11 flipped `WONTDO`, check 2 fired `review loops that ran past the ceiling, stalled without recording it, or exited without promoting`.
- AC2 — `bash tools/unattended/check-unattended.sh` — with the same ids `CLOSED`, the leg is green; this run's own loop exited NON-CONVERGENT and its two promotions discharge it.
- AC3 — `grep -o "This is a LOWER BOUND[^)]*"` — the message states it demands one surviving id per exited SUBJECT and not one per standing BLOCKER.
- AC4 — `bash tools/unattended/check-unattended.sh` — green over all 28 records with the filter in place, so the tightening added no hit.
- AC5 — `bash tools/unattended/check-unattended.sh` — green at HEAD.

**Evidences:** TOOL-aGradedMandate-8
- AC1 — `grep -c "pieces-complete" .claude/skills/unattended/SKILL.md` — 2, measured 0 before the edit.
- AC2 — `grep -c "not retired" .claude/skills/unattended/SKILL.md` — 1, measured 0 before.
- AC3 — `grep -c "gotchas.py" .claude/skills/unattended/SKILL.md` — 1, measured 0 before.
- AC4 — `grep -c -- "--verdict FAIL" .claude/skills/unattended/SKILL.md` — 1, measured 0 before.
- AC5 — `bash tools/check-wiring.sh --check` — the installed Skill matches the tracked render.
- AC6 — `bash tools/unattended/check-unattended.sh` — green, which is every shape check the kit applies to the render; section 5 records that no size ceiling exists for it anywhere in this tree.
- AC7 — `grep -c "owner's one turn" .claude/skills/unattended/SKILL.md` — 1, measured 0 before, which is why this spelling replaced `retire` at 2.

**Evidences:** TOOL-aGradedMandate-9
- AC1 — `bash tools/unattended/check-unattended.sh` — a Skill paragraph naming only `authorization-reachable` while the driver holds a second member fired the driver-side refusal, observed against a staged `bogus-item`.
- AC2 — `bash tools/unattended/check-unattended.sh` — a Skill paragraph naming `invented-item` fired the Skill-side refusal.
- AC3 — the check's own `awk` selector — run over a Skill whose sentence was renamed, it yields zero lines, which is the input the empty-population refusal reads.
- AC4 — `bash tools/unattended/check-unattended.sh` — green at HEAD with both members named on both sides.
- AC5 — amended rev-4 — see the section 9 line: the criterion named the suite the owner instructed this run to skip.

**Evidences:** TOOL-aGradedMandate-10
- AC1 — `bash tools/unattended/unattended.sh --status aGradedMandate` — one retire row reads `parked` and does not inflate `noted`; the live record moved from `parked 1 · noted 6` to `parked 2 · noted 5`.
- AC2 — `bash tools/unattended/unattended.sh --status aGradedMandate` — on the live record `parked 2` plus `noted 5` equals the 7 parked rows the file holds, and an arm in `unattended.test.sh` asserts the same partition over one row of every shape with the rescope act pinned to `retire`.
- AC3 — `unattended.test.sh` — the partition arm pins the act because with `add` it is green before the fix, which is recorded in the arm's own comment.
- AC4 — `grep -c 'park_kinds_unowed' tools/unattended/unattended.sh` — 2, one definition and one consumer, measured at 2 before the edit and asserted as a no-change criterion.
- AC5 — amended rev-3 — see the section 9 line: the second half named the suite the owner instructed this run to skip; the first half, the gate leg, is green.

**Evidences:** TOOL-aGradedMandate-11
- AC1 — `python tools/memory-tree/gen_build_index.py --print-bindings` — the census record is tracked and classifies as `journal` naming both ids.
- AC2 — the census record's own probe block — re-running it reproduces 7 pass and 21 refuse, and the record names both counts.
- AC3 — `grep -c 'closing-loop-census' memory/builds/aGradedMandate/spec/2026-08-31-spec-TOOL-aGradedMandate-1.md` — 1, measured 0 before the edit.
- AC4 — the census record — it names both NON-TERMINAL refusers, `aGradedMandate` at `FOLDING` and `aThawedCorpus` at `LANDING`, and disposes of each by name.
- AC5 — `bash tools/memory-tree/check-memory-hygiene.sh` — green over the new record's filename and binding line, run at every commit through the pre-commit leg.
