**Serves:** research TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102

# Brief: dLinkedLibrary's specs cross-checked against dTotalRecall's re-grounded specs

## The prompt

> Cross-check and re-ground two landed dClosedLoop spec sets against their re-grounded parents, then
> land each one: dLinkedLibrary (91 specs; parent dTotalRecall) [...] Scope the exposure in two ways.

— the dClosedLoop re-ground session's hand-off to this session, 2026-10-28, relaying the owner's hold
on dIndexedDesign's spec run until dLinkedLibrary is re-grounded.

## The brief

### Goal

Classify every assumption the named dLinkedLibrary specs make about a parent unit as AGREES, MISMATCH
or UNKNOWN UNTIL BUILT, against the parents' specs as they stand on origin/main at `1a61f21a2`.
dLinkedLibrary's spec run began at `82a392696`, the parent of its first spec commit `5a9183011`. That
base holds the second wave's re-grounds (dDeclaredLoop, dWitnessedBar, dPlacedRequest) but none of the
third wave's:

- **dTotalRecall**, the parent, re-grounded at `794a0f5fb` and landed as `2bd5e10d4`. It revised units
  1, 2, 4, 8, 9, 11, 15, 18, 19, 20, 22, 25, 26, 43 and 76. Its record,
  `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md`, and
  each revised spec's new §9 line say what moved.
- **dBoundRoles**, which spec 20 cites, re-grounded at `ac8ab8d5f` and landed as `fffe4aadf`. It
  revised units 1, 2, 3, 5, 6, 11, 12, 14, 20, 21, 22, 23, 25, 43 and 60. Its record is
  `memory/builds/dBoundRoles/build/2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md`.
- **dKeptSession**, re-grounded at `ff44fb2a2` and landed as `0689e7fa1`. No dLinkedLibrary spec cites
  a unit it revised; its record states rules the readers apply below.

The first population is by citation: every spec that cites a revised unit, as `<FAMILY>-<build>-<n>`
or a bare `<build>-<n>` (23 specs). By the revised units each cites (`tr` dTotalRecall, `br`
dBoundRoles): 1 (tr1) · 2 (tr8) · 3 (tr1, tr9) · 4 (tr1, tr8, tr9) · 5 (tr4) · 7 (tr8) · 8 (tr1, tr2,
tr18) · 9 (tr2, tr9, tr19) · 12 (tr9) · 13 (tr1, tr2, tr18) · 14 (tr8) · 15 (tr8) · 16 (tr8) · 17
(tr8, tr9) · 19 (tr8, tr9) · 20 (br14, tr9) · 21 (tr8) · 22 (tr1) · 37 (tr2) · 40 (tr9) · 46 (tr8) ·
47 (tr1) · 52 (tr1).

The second population is by rule (30 specs). The parents' re-grounds applied rules that bind specs
that never cite the unit stating them. A text probe over the other 68 specs named these candidates,
by the rule each hit: 10, 23, 49, 53, 61, 64, 96 and 102 (a leg named, `tools/gate-legs.json` edited
or `enforces` missing), 6, 24, 25, 49, 61, 67 and 86 (a record kind), 23 (a loop row), and 10, 11,
18, 25, 43, 51, 67, 69, 74, 75, 80, 86, 90, 91, 92, 94, 96, 97, 98, 99, 100, 101 and 102 (a module of
another kit named, `sys.path`, `importlib` or an in-process read). The probe is a heuristic. Verify
every hit: a hit the rule does not bind, such as a kit importing its own library, is a line in your
return, not a row.

The rules, each as the parents now apply it. The parent specs win where this summary differs; the
full statements, with their parent cites, are the R1 to R8 bullets of
`memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md`:

- **R1, a new leg's `enforces`.** PLAY-dOrderedCharter-7 S3 reds a leg with no `enforces`, and the
  pending list only shrinks after dOrderedCharter's pass (oc7:58-63), so a later build cannot excuse
  its leg there. dWitnessedBar unit 11 declares each leg once, in its kit's `[[gate_leg]]` row or a
  `tools/govkit/registry.toml` `[[exempt_leg]]` row, and `leg_factory.py --write` renders
  `tools/gate-legs.json`. The re-ground gave every dTotalRecall leg its `enforces` (tr1, tr8, tr11, tr15,
  tr19, tr22, tr26, tr43, tr76) and moved tr8's leg to memory-tree's `kit.toml`. A spec that adds,
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
  `requires_if` row admits it. Which kit a spec's code lives in is read from its Files touched.
- **R4, the loop program's rows.** dl12 S1 to S3: an item belongs to its own step's table; every input
  names a layer tag of `tools/playbook/layers.toml`; `returns` names a `record-kind.*` tag; `routes`
  holds exactly the outcomes as keys.
- **R5 to R8**, as the dTotalRecall brief states them: no `new disposition` door (dl16), every overlay
  composition read at `--rev HEAD` (oc46 S6, oc35 S5), dl2's guard reads no trailer at pre-commit, and
  dl3 S2's witness channels with dl33 S3's budget edges. dPlacedRequest's `--claims` prints fields 1 to
  5 only, and `read_claims` fetches `refs/gov/leases/*` from the remote (pr1:206-208, :76-77).

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not a re-ground touched
  it.
- **MISMATCH:** today's parent text says something else: a renamed surface, a moved reader, a fork
  resolved another way, a refusal the parent now states, or a rule above that the spec breaks. Quote
  both sides with `file:line`, and state in one or two sentences the change the dLinkedLibrary spec
  needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other. A citation group checks every assumption about a revised unit and
applies R1 to R8 to its own specs. A rule-wide group checks only R1 to R8, on the hits named above:

- **Group A1, citation, led by spec 1:** specs 1, 2, 3, 4, 5, 7, 8, 9, 12, 13, 14 and 15.
- **Group A2, citation, led by spec 16:** specs 16, 17, 19, 20, 21, 22, 37, 40, 46, 47 and 52.
- **Group B1, rule-wide, legs and kinds, led by spec 6:** specs 6, 10, 23, 24, 25, 49, 53, 61, 64, 67,
  86, 96 and 102.
- **Group B2, rule-wide, sibling kits, led by spec 11:** specs 11, 18, 43, 51, 69, 74, 75, 80, 90, 91,
  92, 94, 97, 98, 99, 100 and 101. R3 only, unless a spec plainly breaks another rule.

The spec files are `memory/builds/dLinkedLibrary/spec/2026-10-2?-spec-TOOL-dLinkedLibrary-<n>.md`. The
parents' are `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`,
`memory/builds/dBoundRoles/spec/2026-10-2?-spec-TOOL-dBoundRoles-<n>.md`, and for the rules
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`,
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`,
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md` and
`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`. Read every mention of
a parent unit in each of your specs, then the cited parent text, its §9 rev lines first.
`git show <re-ground commit> -- <spec>` shows what each re-ground moved; `git show 82a392696:<spec>`
reads a parent as dLinkedLibrary's spec run read it.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `llN:L` for line L of dLinkedLibrary spec N, `trN:L` for dTotalRecall spec N, `brN:L` for
   dBoundRoles spec N, and `ocN:L`, `dlN:L`, `wbN:L`, `prN:L` for the ancestors. `Rule` is `cite` for
   a citation assumption, else the R-number.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dLinkedLibrary spec
   needs, then `Cause:` either the re-ground (the parent text moved in the re-ground commit) or
   pre-existing (it already read so at `82a392696`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit the rule does not bind, one line saying why.
5. One line per citation spec: the revised parent units it cites that none of its assumptions depend
   on.

### Non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent restates one of their surfaces
  that the dLinkedLibrary spec relies on through it.
- No defect in dLinkedLibrary's own design that no parent causes.
- No verdict about dFurnishedOrders, the sibling build cross-checked beside this one.
