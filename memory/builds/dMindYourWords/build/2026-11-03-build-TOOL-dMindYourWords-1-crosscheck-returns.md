**Serves:** research TOOL-dMindYourWords-1 TOOL-dMindYourWords-11

# dMindYourWords — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record [`2026-11-03-build-TOOL-dMindYourWords-1-parents-crosscheck`](2026-11-03-build-TOOL-dMindYourWords-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-03-prompt-TOOL-dMindYourWords-1-parents-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dMindYourWords-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group, led by spec 11

I found one MISMATCH, one UNKNOWN UNTIL BUILT and two AGREES in spec 11. The mismatch was already in the text at `ba8b3c8c4`; the revision in `66f7b8d32` did not cause it. Every line below was read at `66c5b8dbf`.

1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 11 | S10's `lexicon-declaration` row (form `rows`) may carry `writer = hand`, and tr2 leaves it there | cite | AGREES | myw11:110-115 "schema form `rows` … the writer is `hand`". tr2:80-84 "a `hand` row of another form keeps `hand`". tr2:300-301: AC9 checks only the `fields` rows. tr1:194 "`hand` is legal until TOOL-dTotalRecall-2 registers a door". |
| 11 | tr2 will later register a door for the declaration, so `hand` is temporary ("until TOOL-dTotalRecall-2 registers a door") | cite | MISMATCH | myw11:114-115 against tr2:57-58, tr2:80-84, tr2:175-176 and tr2:350-351 (the ordering) |
| 11 | The stand-in `build_records.py new change` writes gov's first vocabulary record (S10, AC10) and is the command S7's refusal names. tr2 S1 makes that verb its door's adapter. | cite | UNKNOWN UNTIL BUILT | myw11:37-40, :90-92, :117-119, :344-346. tr2:44-46 "The factory's own stand-in verb `build_records.py new <kind>` … calls the same function". tr2:48-53 refuses "a kind whose `writer` names another door". tr2:185: `<n>` is minted under "the build's lease or claim". tr2:356 "The pass builds the lease rung of §4 "Minting" against that verb". At base, `ba8b3c8c4` read "the pass builds no lease rung before the pick". |
| 11 | RH: the spec reads no lease `session`, `lease`-mode class or `epoch`; it does not read `--claims` or a lease commit, files no ask, and does not read tr2 F6 as open | RH | AGREES | The probe for `--claims\|read_claims\|holder\|epoch\|refs/gov/leases\|\blease\b\|§8 F6` over spec 11 found no match. Its only tr2 text is myw11:114. Any lease read happens inside tr2's door (tr2:192-199), and spec 11 adds none. |

2. MISMATCH

- **myw11:114-115** says "the writer is `hand` because the declaration is edited by hand and admitted by S3, until TOOL-dTotalRecall-2 registers a door". tr2 says otherwise:
  - tr2:57-58: "A row whose `schema.form` is not `fields` is written only by a kind verb of S7."
  - tr2:175-176: "This unit adds two, `build-readme` and `spec`".
  - tr2:80-84: "a `hand` row of another form keeps `hand`, and the pass commit's `Decided:` trailer names the unit or kit owning its door".
  - tr2:350-351: tr2's run "builds before dWellOiledMachine", which is a parent of dMindYourWords. So tr2 has already been built when S10 adds the row. It registers no door for a `rows` kind, and its S9 sweep runs before the row exists.

  The "until" therefore points at a door that tr2 never adds. It reads like the general rule at tr1:194, applied to a row that tr2 explicitly leaves as `hand`.

  **Change:** drop "until TOOL-dTotalRecall-2 registers a door". State that the row keeps `writer = hand` permanently, because it is a `rows` kind tr2 S9 leaves at `hand` (tr2:80-84). If a future door is wanted, name its owner the way tr2 S9's `Decided:` trailer does, or state that none is planned.

  **Cause:** pre-existing. At `ba8b3c8c4`, tr2:55, :77-80 and :171 already said the same; `66f7b8d32` changed only the header, the record rows, §3's external edge, §4 "Minting", §8 F6 and §9.

3. UNKNOWN UNTIL BUILT

- **The stand-in `new change` door (myw11:37-40, :117-119):** tr2's build run decides this:
  - whether S2's writer refusal (tr2:48-53) applies when a call comes through the factory's own verb for the `change` row, whose writer cell tr1:190-195 leaves to the build run to set;
  - whether the lease rung now built against the holder verb (tr2:192-199, :356) lets this build mint `change-<n>`, or falls back to the session rule at tr2:199-201.

  Spec 11 should name tr2 S1 as the door its stand-in now runs through, so S10 and AC10 are re-grounded on that landed code.

4. Rule-wide hits RH does not bind

- myw14:45, :121, :124, :221-222, :250: `holder` is a JavaScript variable in the IIFE lexicon fixture, not a lease holder.
- myw4:200, myw6:200, myw8:303: `epoch` is the gate leg name `kit epoch (shipped bytes move, the version moves)`, not a lease epoch.
- myw17:70, :88, :233: the hits are `placeholder`, a substring match on "holder".
- myw1:47: "§8 F6" is spec 1's own fork, "Which classes does `Offender.grade` carry?" (myw1:445), not tr2 F6.
- Parent text that looks wrong (no verdict): tr2:352 says the ask "serves this unit's S2 and S9", but tr2's lease read sits in S6 and §4 "Minting" (tr2:70, :192). S2 and S9 are the writer refusal and the hand-row rewrite.

5. Spec 11: none of its assumptions depend on tr2's §3 external edge (tr2:128-131) or §8 F6 (tr2:340-357). tr2's §4 "Minting" lease rung (tr2:192-199) matters only through row 3's UNKNOWN. Spec 11 does not cite TOOL-dWellOiledMachine-6, -41 or -58.

Probes run, all read-only:
- `git show 66c5b8dbf:<spec>` on spec 11, tr2 and tr1, plus the `change` and stand-in lines of PLAY-dOrderedCharter-7 and -15.
- `git diff ba8b3c8c4 66c5b8dbf -- <tr2>`: one commit, `66f7b8d32`, 21 lines added and 6 removed, none in S1 to S9.
- `git show ba8b3c8c4:<tr2> | grep` on the S9, S3 and handler lines: identical text at base.
- A grep of the RH terms and the revised unit ids over all 48 spec files at `66c5b8dbf`; the hits are the ones listed above.

Files:
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dMindYourWords\spec\2026-10-29-spec-TOOL-dMindYourWords-11.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-2.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTotalRecall\spec\2026-10-25-spec-TOOL-dTotalRecall-1.md (shown above as `$(ls …-TOOL-dTotalRecall-1.md)`; exact date prefix not printed)
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-7.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-15.md
