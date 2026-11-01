**Serves:** research TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-69

# Brief: dBoundRoles's specs cross-checked against dDeclaredLoop, dWitnessedBar and dPlacedRequest's re-grounded specs

## The prompt

> Cross-check and re-ground three landed dClosedLoop spec sets, then land each one: dKeptSession (64
> specs), dBoundRoles (59 specs) and dTotalRecall (91 specs). [...] Scope the exposure in two ways,
> not just by citation.

— the dClosedLoop housekeeping session's hand-off to this session, 2026-10-26, relaying the owner's
hold on the dFurnishedOrders, dLinkedLibrary, dRankedPlan and dWellOiledMachine spec runs until this
wave lands.

## The brief

### Goal

Classify every assumption the named dBoundRoles specs make about a parent unit as AGREES, MISMATCH or UNKNOWN
UNTIL BUILT, against the parents' specs as they stand on origin/main at `c8d46e188`. dBoundRoles's spec run
began at `4283cb44f`, which holds none of its parents' re-grounds:

- **dDeclaredLoop**, re-grounded at `783f1ad3a` and landed as `e5de11e9e`. It revised units
  1, 2, 3, 4, 5, 6, 12, 16, 17, 18, 22, 24, 25, 26, 27, 28, 33, 34, 46 and 56. Its record, `memory/builds/dDeclaredLoop/build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`, and each revised spec's new §9 line say what moved.
- **dWitnessedBar**, re-grounded at `443775a2f` and landed as `191ba7ab5`. It revised units
  1, 3, 6, 8, 11, 12, 14, 15, 16, 18, 23, 25, 28, 51 and 56. Its record, `memory/builds/dWitnessedBar/build/2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck.md`, and each revised spec's new §9 line say what moved.
- **dPlacedRequest**, re-grounded at `2740f0a3d` and landed as `60d90cb71`. It revised units
  1, 2, 3, 4, 5, 6, 7, 9, 21 and 34. Its record, `memory/builds/dPlacedRequest/build/2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md`, and each revised spec's new §9 line say what moved.

The first population is by citation: every spec that cites a revised unit, as `<FAMILY>-<build>-<n>`
or a bare `<build>-<n>` (14 specs). By the revised units each cites (`dl` dDeclaredLoop, `wb`
dWitnessedBar, `pr` dPlacedRequest): 1 (dl24, wb23) · 2 (dl24, wb23) · 5 (pr4) · 11 (dl6) · 12 (dl16, pr3, pr4) · 14 (dl18, dl24, wb12) · 15 (wb23) · 17 (wb15) · 20 (dl24) · 21 (dl18) · 22 (dl1, dl6, dl27) · 37 (wb23) · 43 (pr4) · 54 (wb23).

The second population is by rule (21 specs). A parent re-ground applied a rule that binds specs
that never cite the unit stating it. A text probe over the other specs named these candidates, by
the rule each hit: 3 (a record kind, a loop item row), 6 and 23 (the guard's `--staged` or a `Gov-Policy:` trailer), 16, 24, 55 and 59 (an in-process sibling import), 49 and 63 (a leg and an in-process import), and 9, 25, 42, 50, 56, 57, 58, 60, 62, 64, 66 and 69 (a leg with no `enforces`). The probe is a heuristic. Verify every hit: a hit the rule does not
bind is a line in your return, not a row.

The rules, each as the parents now apply it. The parent specs win where this summary differs:

- **R1, a new leg's `enforces`.** PLAY-dOrderedCharter-7 S3 reds a `tools/gate-legs.json` row with no
  `enforces`, and the pending list `core-pending.txt` only shrinks after dOrderedCharter's pass
  (oc7:58-63, :228), so a later build cannot excuse its leg there. Under `core.bypass = never` the
  meta-check also reds a leg whose `enforces` is non-empty and that carries a `guard` (oc7:109-111).
  The parents' re-grounds gave their legs `enforces` (dl25, dl26, dl28, wb11, pr4, pr7, pr21). dl56 F5
  is still open on who writes it for other units, recommending each unit's own pass. A spec that adds
  or reshapes a leg row and names no `enforces` for it is a MISMATCH.
- **R2, a typed record kind.** PLAY-dOrderedCharter-42 S2 and S3 make `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the record factory's kind list, and read a `-<kind>-<n>.md` file
  whose Serves kind differs as malformed; S5 keeps the closed list in the HYGIENE template. The
  parents now serve their records as their own kinds: dl3, dl16, dl17 and dl22 (`transition`,
  `acceptance` and the rest), wb1, wb8, wb14, wb25 and wb51 (`gate-health`, `flake`, `widen`,
  `leg-tail`), pr2 (`card`) and pr7 (`probe`, `probe-trigger`). A spec that adds a kind without
  joining it to all three, serves a typed record as `journal`, or reads a parent's record under a kind
  the parent no longer serves, is a MISMATCH.
- **R3, a sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4, restated by
  oc7:202-203, dl12 S4, wb3 and wb28 at their re-grounds). Code in one kit reaches another kit's verb
  by subprocess, through an inline `resolve_kit_dir`; where the verb does not exist, the parents write
  a §8 fork for an ask. A spec whose code imports or calls another kit's module in process is a
  MISMATCH, unless a declared `requires_if` row admits it.
- **R4, the loop program's rows.** dl12 S1 to S3: an item belongs to its own step's table, and adopt,
  entry, lifecycle and probe items are never steps of the five (dl12:80-81); every input names a layer
  tag of `tools/playbook/layers.toml` (dl12:43); `returns` names a `record-kind.*` tag (dl12:113);
  `routes` holds exactly the outcomes as keys (dl12:147-148).
- **R5, the disposition door.** dl16 at rev-3 claims no `build_records.py new disposition` verb; a
  writer names the factory's flags and the build run re-grounds the call (pr3, pr5, pr21).
- **R6, the overlay composition's reads.** Every read the composition makes passes `--rev HEAD`
  (oc46 S6, oc35 S5), an unborn `HEAD` reading the default; a stale patch follows
  `instructions.stale`'s mode and files an order (oc35 S7, S8).
- **R7, dDeclaredLoop's guard.** dl2's `guard.py --staged` runs at pre-commit, when no commit message
  exists, so it reads no trailer; the `Gov-Policy:` trailer is checked by `--push-range`; the owner
  proof tests stderr (dl2 S5).
- **R8, the witness channels and the budget edges.** dl3 S2 names the channel set a witness may use
  (pr1's trailer-only witness was a mismatch); dl33 S3 says contention never draws on the budget.

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not a re-ground touched
  it.
- **MISMATCH:** today's parent text says something else: a renamed surface, a moved reader, a fork
  resolved another way, a refusal the parent now states, or a rule above that the spec breaks. Quote
  both sides with `file:line`, and state in one or two sentences the change the dBoundRoles spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other. A citation group checks every assumption about a revised unit and
applies R1 to R8 to its own specs. A rule-wide group checks only R1 to R8, on the hits named above:

- **Group A, citation, led by spec 1:** specs 1, 2, 5, 11, 12, 14, 15, 17, 20, 21, 22, 37, 43 and 54.
- **Group B, rule-wide, led by spec 3:** specs 3, 6, 9, 16, 23, 24, 25, 42, 49, 50, 55, 56, 57, 58, 59, 60, 62, 63, 64, 66 and 69.

The spec files are `memory/builds/dBoundRoles/spec/2026-10-2?-spec-TOOL-dBoundRoles-<n>.md`. The parents' are
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`,
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md`,
`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`,
and `memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`. Read every
mention of a parent unit in each of your specs, then the cited parent text, its §9 rev lines first.
`git show <re-ground commit> -- <spec>` shows what each re-ground moved.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `brN:L` for line L of dBoundRoles spec N, `dlN:L` for dDeclaredLoop spec N, `wbN:L` for dWitnessedBar spec N, `prN:L` for dPlacedRequest spec N, and `ocN:L` for dOrderedCharter spec N. `Rule`
   is `cite` for a citation assumption, else the R-number.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dBoundRoles spec needs, then
   `Cause:` either the re-ground (the parent text moved in the re-ground commit) or pre-existing (it
   already read so at `4283cb44f`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit the rule does not bind, one line saying why.
5. One line per citation spec: the revised parent units it cites that none of its assumptions depend
   on.

### Non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent restates one of their surfaces
  that the dBoundRoles spec relies on through it.
- No defect in dBoundRoles's own design that no parent causes.
- No verdict about a sibling build (dKeptSession, dTotalRecall): none reads another's specs.
