# dFoldedAudit — the promoted units' cross-read return

**Serves:** journal TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15

All eight items are done: six of the seven specs are folded, unit 12 needed no change, and nothing is committed. `unattended.sh --plan dFoldedAudit` reads READY for all seven on the working tree, before commit.

## Specs by rev

| Unit | Rev | Scope | Interface | Ordering | Acceptance |
|---|---|---|---|---|---|
| TOOL-dFoldedAudit-14 | rev-2 | clean | clean | fixed | clean |
| TOOL-dFoldedAudit-13 | rev-2 | fixed | clean | fixed | clean |
| TOOL-dFoldedAudit-10 | rev-2 | fixed | clean | clean | clean |
| TOOL-dFoldedAudit-11 | rev-2 | clean | fixed | clean | clean |
| TOOL-dFoldedAudit-9 | rev-2 | fixed | clean | fixed | clean |
| TOOL-dFoldedAudit-12 | rev-1, no change | clean | clean | clean | clean |
| TOOL-dFoldedAudit-15 | rev-2 | fixed | fixed | fixed | clean |

On the acceptance axis, report items H1 to H6, M1 to M17 and L1 to L4 each have an owning unit.

## Items 1 to 7
- **Unit 9:** F1 and F2 are RESOLVED to (a). F2 cites the decision row at 2026-11-02T03:29:31Z.
- **Unit 15:**
  - F1 is RESOLVED to (c), F2 to (b), and F3 to (a).
  - §3 and §4 are rewritten to (a), with S30 to S34 and AC31 to AC36 added.
  - `memory/guides/SESSION-KICKOFF.md` joins the write set, with its stamp and `Manifest delta:` line.
- **M4:** the new first test adds 94 bytes, so the render reads 30659 of 30720, leaving 61. I measured this by applying the text to the render with CRs stripped.
- **Edges:** units 11 and 13 now hand off to unit 15, unit 14 to unit 9, and unit 15 carries the mirror lines.
- **Fixture cutoffs:** unit 10's fixture C and unit 11's fixture R each declare `SPEC_FOLD_CUTOFF="2000-01-01"`.
- **`routed-commits selftest`:** added to unit 10. Units 9 and 14, the other two touching `lib-unattended.sh`, already carry it.

## Disagreements fixed by the cross-read
Each is fixed in one spec and named in its §9 line.
- **Unit 10:** its M4 edge said M4 stays as shipped, which item 3 made false, so it is now a `hands-off` to unit 15. Item 3 named only units 11 and 13.
- **Unit 11:** its `folds` array and unit 13's scalar `folds` shared one name in one function. Unit 11 now retypes the scalar and moves the test, because `$folds` over an empty array is unbound under `set -u`.
- **Unit 13:** its edge said unit 15 leaves the carrier alone. The fixture edge is retired, and §4 and §5 no longer point at the old edges.
- **Unit 9:**
  - AC7 wrote its records through a verb unit 13 refuses there, so they are now committed by hand.
  - §4 named unit 10 the owner of a presence term that unit 10's §3 rules out.
- **Unit 14:** fixture T carried no `base:`, so its arms would red once unit 9 lands.
- **Unit 15:**
  - S15 named `print_chain_verdict`, but the status loop moves to `read_chain_verdict`.
  - S16 spelled `adopt-roles.sh` with no flag, which exits 2.
  - Fixture R had no `base:`, and AC4 blanked the cutoff where it is no longer read.
  - Fixture F's specs were at rev-1, where unit 11 refuses a `local` row, and it had no `gen:build-units` region for `--plan`.
  - AC7's "no check 2 line" would red on unit 10's attended announcement.

## Reported, not decided
1. **Unit 13's refusal is left off the `--record-round` list.** Item 3 names only units 11 and 15's changes, so unit 13 keeps a `hands-off external` line for S3's refusal, and unit 15's §3 says so. If you want it listed, one clause joins S30 and that edge goes.
2. **Wider than item 3's list, but inside option (a).**
   - S32 adds `rev` to the verbs guide's "Drive the build as ONE program" bullet.
   - S31 adds the fifth field to the `--plan` bullet.
   - F3 itself names the verbs-guide `rev` sentence.
3. **F3's basis differs slightly from your wording.** The accepted brief's item 1 says "M4's text and its carriers". The list naming `VERBS.template.md` and the protocol is in unit 1's spec brief, and the F3 mark cites that. The `/build` Skill is on neither list, so `rev` there rests on your ruling alone.
4. **The `/build` Skill grows to 103 lines.** S16's bullet needs a third line. No limits row pins the file, but unit 13's AC10 pins 102 and reads red if re-observed after unit 15.
5. **Unit 14's header gained `ratified 2026-11-02`,** because the format requires it. Its F1 text is unchanged.

## Verification
- **Hygiene:** I ran the full gate in a scratch clone with the specs committed and the index rendered there, so the edge joins were live.
  - Checks 5, 12 and 25 are clean, and no failing or advisory line names a spec of this build.
  - The gate exited 1 on one line: check 13 says `TOOL-dFoldedAudit-8` is claimed by both dClosedLoop and dFoldedAudit.
  - That traces to `memory/builds/dClosedLoop/build/2026-11-01-build-TOOL-dFoldedAudit-8-deviation-81.md`, landed by unit 8 at 63669d505. I traced the cause but did not run the gate at base.
- **`tools/check-spec-tokens.py`:** not run, as it is yours after this pass. My scratch re-derivation of its guards join finds no missing leg; its other joins are unchecked.
- **Cross-read:** done by reading. No fixture was executed.

Files are in C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\:
- 2026-11-02-spec-TOOL-dFoldedAudit-9.md
- 2026-11-02-spec-TOOL-dFoldedAudit-10.md
- 2026-11-02-spec-TOOL-dFoldedAudit-11.md
- 2026-11-02-spec-TOOL-dFoldedAudit-13.md
- 2026-11-02-spec-TOOL-dFoldedAudit-14.md
- 2026-11-02-spec-TOOL-dFoldedAudit-15.md
