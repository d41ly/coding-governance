**Serves:** research KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65

# Brief: dKeptSession's specs cross-checked against dDeclaredLoop and dPlacedRequest's re-grounded specs

## The prompt

> Cross-check and re-ground three landed dClosedLoop spec sets, then land each one: dKeptSession (64
> specs), dBoundRoles (59 specs) and dTotalRecall (91 specs). [...] Scope the exposure in two ways,
> not just by citation.

— the dClosedLoop housekeeping session's hand-off to this session, 2026-10-26, relaying the owner's
hold on the dFurnishedOrders, dLinkedLibrary, dRankedPlan and dWellOiledMachine spec runs until this
wave lands.

## The brief

### Goal

Classify every assumption the named dKeptSession specs make about a parent unit as AGREES, MISMATCH or UNKNOWN
UNTIL BUILT, against the parents' specs as they stand on origin/main at `c8d46e188`. dKeptSession's spec run
began at `e025029b8`, which holds none of its parents' re-grounds:

- **dDeclaredLoop**, re-grounded at `783f1ad3a` and landed as `e5de11e9e`. It revised units
  1, 2, 3, 4, 5, 6, 12, 16, 17, 18, 22, 24, 25, 26, 27, 28, 33, 34, 46 and 56. Its record, `memory/builds/dDeclaredLoop/build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`, and each revised spec's new §9 line say what moved.
- **dPlacedRequest**, re-grounded at `2740f0a3d` and landed as `60d90cb71`. It revised units
  1, 2, 3, 4, 5, 6, 7, 9, 21 and 34. Its record, `memory/builds/dPlacedRequest/build/2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md`, and each revised spec's new §9 line say what moved.

The first population is by citation: every spec that cites a revised unit, as `<FAMILY>-<build>-<n>`
or a bare `<build>-<n>` (26 specs). By the revised units each cites (`dl` dDeclaredLoop, `wb`
dWitnessedBar, `pr` dPlacedRequest): 1 (dl2, dl6) · 5 (dl1, dl3, pr1) · 6 (pr1) · 7 (dl3, pr1) · 8 (dl6, dl12, pr2, pr9) · 9 (dl1, dl3) · 10 (dl1, dl12) · 11 (dl1, dl3, dl6) · 12 (pr2, pr9) · 13 (dl6, pr2) · 14 (dl6, pr2) · 15 (pr2) · 16 (dl18) · 17 (dl1, dl6) · 18 (dl1, dl16, pr4, pr21) · 20 (dl27) · 24 (dl33) · 25 (dl1, dl12, dl33, pr1, pr3) · 26 (pr2) · 27 (pr1) · 28 (pr1) · 35 (dl3) · 39 (dl16) · 41 (dl6) · 44 (dl2) · 64 (pr2).

The second population is by rule (10 specs). A parent re-ground applied a rule that binds specs
that never cite the unit stating it. A text probe over the other specs named these candidates, by
the rule each hit: 2 and 3 (a composition read or an in-process sibling import), 22 (a loop item row), 36 (an in-process import), 45 (a loop item row), 56 (a record kind, a leg, an in-process import), 57 (a leg, an in-process import), 62, 63 and 65 (a leg with no `enforces`). The probe is a heuristic. Verify every hit: a hit the rule does not
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
  both sides with `file:line`, and state in one or two sentences the change the dKeptSession spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other. A citation group checks every assumption about a revised unit and
applies R1 to R8 to its own specs. A rule-wide group checks only R1 to R8, on the hits named above:

- **Group A, citation, led by spec 1:** specs 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 and 16.
- **Group B, citation, led by spec 17:** specs 17, 18, 20, 24, 25, 26, 27, 28, 35, 39, 41, 44 and 64.
- **Group C, rule-wide, led by spec 2:** specs 2, 3, 22, 36, 45, 56, 57, 62, 63 and 65.

The spec files are `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-<n>.md`. The parents' are
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`,
`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`,
and `memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`. Read every
mention of a parent unit in each of your specs, then the cited parent text, its §9 rev lines first.
`git show <re-ground commit> -- <spec>` shows what each re-ground moved.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `ksN:L` for line L of dKeptSession spec N, `dlN:L` for dDeclaredLoop spec N, `prN:L` for dPlacedRequest spec N, and `ocN:L` for dOrderedCharter spec N. `Rule`
   is `cite` for a citation assumption, else the R-number.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dKeptSession spec needs, then
   `Cause:` either the re-ground (the parent text moved in the re-ground commit) or pre-existing (it
   already read so at `e025029b8`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit the rule does not bind, one line saying why.
5. One line per citation spec: the revised parent units it cites that none of its assumptions depend
   on.

### Non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent restates one of their surfaces
  that the dKeptSession spec relies on through it.
- No defect in dKeptSession's own design that no parent causes.
- No verdict about a sibling build (dBoundRoles, dTotalRecall): none reads another's specs.
