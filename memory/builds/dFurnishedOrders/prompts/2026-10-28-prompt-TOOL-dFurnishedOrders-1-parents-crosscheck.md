**Serves:** research TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61

# Brief: dFurnishedOrders' specs cross-checked against dBoundRoles' re-grounded specs

## The prompt

> Cross-check and re-ground two landed dClosedLoop spec sets against their re-grounded parents, then
> land each one: [...] dFurnishedOrders (60 specs; parent dBoundRoles) [...] Scope the exposure in two
> ways.

— the dClosedLoop re-ground session's hand-off to this session, 2026-10-28, relaying the owner's hold
on the dependent spec runs until the third wave's children are re-grounded.

## The brief

### Goal

Classify every assumption the named dFurnishedOrders specs make about a parent unit as AGREES,
MISMATCH or UNKNOWN UNTIL BUILT, against the parents' specs as they stand on origin/main at
`1a61f21a2`. dFurnishedOrders' spec run began at `1a3ce03dd`, the parent of its first spec commit
`4d726ef27`. That base holds the second wave's re-grounds (dDeclaredLoop, dWitnessedBar,
dPlacedRequest) but none of the third wave's:

- **dBoundRoles**, the parent, re-grounded at `ac8ab8d5f` and landed as `fffe4aadf`. It revised units
  1, 2, 3, 5, 6, 11, 12, 14, 20, 21, 22, 23, 25, 43 and 60. Its record,
  `memory/builds/dBoundRoles/build/2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md`, and
  each revised spec's new §9 line say what moved.
- **dTotalRecall**, which specs 11, 17, 41 and 45 cite, re-grounded at `794a0f5fb` and landed as
  `2bd5e10d4`. It revised units 1, 2, 4, 8, 9, 11, 15, 18, 19, 20, 22, 25, 26, 43 and 76. Its record
  is `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md`.
- **dKeptSession**, which specs 42 and 46 cite, re-grounded at `ff44fb2a2` and landed as `0689e7fa1`.
  It revised units 1, 5, 7, 8, 9, 10, 11, 12, 13, 18, 20, 25, 36, 44 and 56. Its record is
  `memory/builds/dKeptSession/build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`.

The first population is by citation: every spec that cites a revised unit, as `<FAMILY>-<build>-<n>`
or a bare `<build>-<n>` (30 specs). By the revised units each cites (`br` dBoundRoles, `tr`
dTotalRecall, `ks` dKeptSession): 1 (br12) · 2 (br2, br5, br21, br22) · 3 (br5) · 4 (br3, br23) · 5
(br1, br2, br3, br20, br21) · 6 (br5, br25) · 7 (br2, br5, br11) · 8 (br1, br2, br21) · 9 (br1, br3,
br20) · 10 (br5) · 11 (tr9) · 12 (br1, br2, br3) · 14 (br3, br25) · 15 (br1, br2, br5, br43) · 16
(br11, br21) · 17 (tr8) · 18 (br3, br21, br23) · 19 (br2, br3, br5) · 20 (br3, br23) · 22 (br1, br2) ·
24 (br5) · 27 (br11) · 28 (br11) · 29 (br5, br20, br21) · 32 (br1) · 37 (br5) · 41 (tr20) · 42 (br1,
br5, br43, ks44) · 45 (tr20) · 46 (ks44).

The second population is by rule (21 specs). The parents' re-grounds applied rules that bind specs
that never cite the unit stating them. A text probe over the other 30 specs named these candidates,
by the rule each hit: 23, 30, 48, 50, 52, 53, 54, 55, 56, 58, 59, 60 and 61 (a leg named,
`tools/gate-legs.json` edited or `enforces` missing), 13, 25, 26, 31, 33, 34, 39, 48, 54, 58 and 61 (a
module of another kit named, `sys.path`, `importlib` or an in-process read), and 49 and 60 (budget
contention). The probe is a heuristic. Verify every hit: a hit the rule does not bind, such as the
roles kit importing its own `roles_lib`, is a line in your return, not a row.

The rules, each as the parents now apply it. The parent specs win where this summary differs; the
full statements, with their parent cites, are the R1 to R8 bullets of
`memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md`:

- **R1, a new leg's `enforces`.** PLAY-dOrderedCharter-7 S3 reds a leg with no `enforces`, and the
  pending list only shrinks after dOrderedCharter's pass (oc7:58-63), so a later build cannot excuse
  its leg there. dWitnessedBar unit 11 declares each leg once, in its kit's `[[gate_leg]]` row or a
  `tools/govkit/registry.toml` `[[exempt_leg]]` row, and `leg_factory.py --write` renders
  `tools/gate-legs.json`. The re-grounds gave br25's and br60's legs, and every dTotalRecall leg,
  their `enforces`, and moved tr8's leg to memory-tree's `kit.toml`. A spec that adds,
  reshapes or re-guards a leg by hand in `tools/gate-legs.json`, or names no `enforces` for it, is a
  MISMATCH.
- **R2, a typed record kind.** PLAY-dOrderedCharter-42 S2, S3 and S5 make `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the factory's kind list, read a `-<kind>-<n>.md` file whose Serves
  kind differs as malformed, and keep the closed list in the HYGIENE template. No parent claims a
  `build_records.py new <kind>` door: a writer names the parent's own command or the factory and its
  per-kind flags (tr1, tr43 S4). tr1 now rows the four untyped tokens and joins the typed ones through
  `TYPED_RECORD_KINDS`; tr25 makes `stream-plan` typed; tr4's routing region routes every typed kind. A
  spec that adds a kind without joining all three, serves a typed record as `journal`, names a
  `new <kind>` door, or reads a parent's record under a kind the parent no longer serves, is a
  MISMATCH.
- **R3, a sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205;
  wb28:63-64). Code in one kit reaches another kit's verb by subprocess, found through an inline
  `resolve_kit_dir`; a policy key is read by `policy.py get` as a subprocess (oc7:379-380). The third
  wave applied it everywhere: dTotalRecall's govkit steps reach memory-tree and the playbook kit by
  subprocess or a fork (tr18, tr20), dBoundRoles' cross-kit reads go through roles-kit verbs
  (`handoff.py check-return-file`, `check_roles.py --print-tag-rows`, `check_roles.py
  --check-actor-patch`, `handoff.py agent-return`) or a declared `requires_if` row (br25), and
  dKeptSession's hooks spawn `policy-mirror.js get`. A spec whose code imports or calls another kit's
  module in process, or puts another kit's directory on `sys.path`, is a MISMATCH unless a declared
  `requires_if` row admits it. Which kit a spec's code lives in is read from its Files touched. dBoundRoles' re-ground also
  gave br21's `read_policy_setting` a `with_default` argument, br43 making it the one caller of
  `get`.
- **R4, the loop program's rows.** dl12 S1 to S3: an item belongs to its own step's table; every input
  names a layer tag of `tools/playbook/layers.toml`; `returns` names a `record-kind.*` tag; `routes`
  holds exactly the outcomes as keys.
- **R5 to R8**, as the dTotalRecall brief states them, with R7 as br6 and br23 now apply it
  (`tools/loop/guard.py --staged` the pre-commit verdict): no `new disposition` door (dl16), every overlay
  composition read at `--rev HEAD` (oc46 S6, oc35 S5), dl2's guard reads no trailer at pre-commit, and
  dl3 S2's witness channels with dl33 S3's budget edges. dPlacedRequest's `--claims` prints fields 1 to
  5 only, and `read_claims` fetches `refs/gov/leases/*` from the remote (pr1:206-208, :76-77).

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not a re-ground touched
  it.
- **MISMATCH:** today's parent text says something else: a renamed surface, a moved reader, a fork
  resolved another way, a refusal the parent now states, or a rule above that the spec breaks. Quote
  both sides with `file:line`, and state in one or two sentences the change the dFurnishedOrders spec
  needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other. A citation group checks every assumption about a revised unit and
applies R1 to R8 to its own specs. A rule-wide group checks only R1 to R8, on the hits named above:

- **Group A1, citation, led by spec 1:** specs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15 and 16.
- **Group A2, citation, led by spec 17:** specs 17, 18, 19, 20, 22, 24, 27, 28, 29, 32, 37, 41, 42, 45
  and 46.
- **Group B, rule-wide, led by spec 13:** specs 13, 23, 25, 26, 30, 31, 33, 34, 39, 48, 49, 50, 52, 53,
  54, 55, 56, 58, 59, 60 and 61.

The spec files are `memory/builds/dFurnishedOrders/spec/2026-10-2?-spec-TOOL-dFurnishedOrders-<n>.md`.
The parents' are `memory/builds/dBoundRoles/spec/2026-10-2?-spec-TOOL-dBoundRoles-<n>.md`,
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`,
`memory/builds/dKeptSession/spec/2026-10-2?-spec-KICK-dKeptSession-<n>.md`, and for the rules
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`,
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`,
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md` and
`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`. Read every mention of
a parent unit in each of your specs, then the cited parent text, its §9 rev lines first.
`git show <re-ground commit> -- <spec>` shows what each re-ground moved; `git show 1a3ce03dd:<spec>`
reads a parent as dFurnishedOrders' spec run read it.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `foN:L` for line L of dFurnishedOrders spec N, `brN:L` for dBoundRoles spec N, `trN:L` for
   dTotalRecall spec N, `ksN:L` for dKeptSession spec N, and `ocN:L`, `dlN:L`, `wbN:L`, `prN:L` for the ancestors. `Rule` is `cite` for
   a citation assumption, else the R-number.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dFurnishedOrders spec
   needs, then `Cause:` either the re-ground (the parent text moved in the re-ground commit) or
   pre-existing (it already read so at `1a3ce03dd`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit the rule does not bind, one line saying why.
5. One line per citation spec: the revised parent units it cites that none of its assumptions depend
   on.

### Non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent restates one of their surfaces
  that the dFurnishedOrders spec relies on through it.
- No defect in dFurnishedOrders' own design that no parent causes.
- No verdict about dLinkedLibrary, the sibling build cross-checked beside this one.
