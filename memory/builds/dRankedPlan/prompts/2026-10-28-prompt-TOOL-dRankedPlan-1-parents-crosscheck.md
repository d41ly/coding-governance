**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 TOOL-dRankedPlan-48 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-57 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-64 TOOL-dRankedPlan-67 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 TOOL-dRankedPlan-81

# Brief: dRankedPlan's specs cross-checked against dBoundRoles' and dTotalRecall's re-grounded specs

## The prompt

> Re-ground the landed spec sets of `dWellOiledMachine` (125 specs) and `dRankedPlan` (80 specs)
> against two parent re-grounds they were specced without: dBoundRoles' re-ground merge `fffe4aadf`
> and dTotalRecall's re-ground merge `2bd5e10d4`. [...] dRankedPlan is second, because it frees
> `dTendedCadence`.

— the dClosedLoop re-ground session's hand-off to this session, 2026-10-28, relaying the owner's hold
on dTendedCadence's spec run until this pass lands.

## The brief

### Goal

Classify every assumption the named dRankedPlan specs make about a parent unit as AGREES, MISMATCH or
UNKNOWN UNTIL BUILT, against the parents' specs as they stand on origin/main at `d1721ef20`.
dRankedPlan's spec run began at `911a70393`, the parent of its first spec commit `7f1846d4c`. That
base holds dDeclaredLoop's re-ground (`e5de11e9e`) and the other second-wave re-grounds, but not these
two:

- **dBoundRoles** re-grounded at `ac8ab8d5f`, landed as `fffe4aadf`. It revised units 1, 2, 3, 5, 6,
  11, 12, 14, 20, 21, 22, 23, 25, 43 and 60. Its record is
  `memory/builds/dBoundRoles/build/2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md`, and
  each revised spec's newest §9 line says what moved.
- **dTotalRecall** re-grounded at `794a0f5fb`, landed as `2bd5e10d4`. It revised units 1, 2, 4, 8, 9,
  11, 15, 18, 19, 20, 22, 25, 26, 43 and 76. Its record is
  `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md`.

Specs 82 and 83 were written after both merges and are out of scope.

The first population is by citation: every spec that cites a revised unit, as `TOOL-<build>-<n>` or
a bare `<build>-<n>` (10 specs). By the revised units each cites (`br` dBoundRoles, `tr`
dTotalRecall): 1 (tr1, tr4) · 2 (br1) · 3 (tr1, tr2) · 10 (tr1) · 11 (tr9) · 13 (br11, tr8) · 16
(tr1, tr2, tr4, tr9) · 33 (tr2) · 48 (tr8) · 52 (tr8).

The second population is by rule (36 specs). The re-grounds applied rules that bind specs that never
cite the unit stating them. A text probe over the other 70 specs named these candidates, by the rule
each hit:

- R1: 15, 27, 29, 31, 37, 45, 61 and 62.
- R2: 4, 6, 9, 12, 14, 15, 21, 28 and 37.
- R3: 9, 21, 22, 30, 32, 37, 38, 42, 45, 51, 62, 67, 74, 77 and 81.
- R4: 4, 5, 6, 9, 12, 14, 15 and 24.
- R7: 57 and 64. R5 and R6: none.
- R8: 4, 5, 7, 9, 12, 14, 15, 19, 21, 22, 23, 25, 26, 29, 37 and 45.
- R9: 7, 8, 9, 29 and 60.

The probe is a heuristic. Verify every hit: a hit the rule does not bind, such as a kit importing its
own library, or the word `budget` meaning something other than dl33's edges, is a line in your
return, not a row.

The rules, as the parents now apply them. The parent specs win where this summary differs:

- **R1, a new leg's `enforces`.** PLAY-dOrderedCharter-7 S3 reds a leg with no `enforces`, and the
  pending list only shrinks after dOrderedCharter's pass (oc7:58-63), so a later build cannot excuse
  its leg there. dWitnessedBar unit 11 declares each leg once, in its kit's `[[gate_leg]]` row or a
  `tools/govkit/registry.toml` `[[exempt_leg]]` row, and `leg_factory.py --write` renders
  `tools/gate-legs.json` (wb11:36-49, :154). The re-grounds gave br25's and br60's legs, and every
  dTotalRecall leg, their `enforces`, and moved tr8's leg to memory-tree's `kit.toml`. A spec that
  adds, reshapes or re-guards a leg by hand in `tools/gate-legs.json`, or names no `enforces` for it,
  is a MISMATCH.
- **R2, a typed record kind.** PLAY-dOrderedCharter-42 S2, S3 and S5 make `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the factory's kind list, read a `-<kind>-<n>.md` file whose Serves
  kind differs as malformed, and keep the closed list in the HYGIENE template. No parent claims a
  `build_records.py new <kind>` door: a writer names the parent's own command or the factory and its
  per-kind flags (tr1, tr43 S4). tr1 now rows the four untyped tokens and joins the typed ones through
  `TYPED_RECORD_KINDS`; tr25 makes `stream-plan` typed; tr4's routing region routes every typed kind.
  A spec that adds a kind without joining all three, serves a typed record as `journal`, names a
  `new <kind>` door, or reads a parent's record under a kind the parent no longer serves, is a
  MISMATCH.
- **R3, a sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205;
  wb28:63-64). Code in one kit reaches another kit's verb by subprocess, found through an inline
  `resolve_kit_dir`; a policy key is read by `policy.py get` as a subprocess (oc7:379-380). The re-grounds
  applied it everywhere: dTotalRecall's govkit steps reach memory-tree and the playbook kit by
  subprocess or a fork (tr18, tr20), dBoundRoles' cross-kit reads go through roles-kit verbs
  (`handoff.py check-return-file`, `check_roles.py --print-tag-rows`, `check_roles.py
  --check-actor-patch`, `handoff.py agent-return`) or a declared `requires_if` row (br25), and
  dKeptSession's hooks spawn `node <policy kit>/policy-mirror.js get <key>` (ks8:62-66). A spec whose
  code imports or calls another kit's module in process, loads one by file (`importlib`,
  `spec_from_file_location`, `load_kit_module`), or puts another kit's directory on `sys.path`, is a
  MISMATCH unless a declared `requires_if` row admits it. Which kit a spec's code lives in is read
  from its Files touched.
- **R4, the loop program's rows.** dl12 S1 to S3: an item belongs to its own step's table; every input
  names a layer tag of `tools/playbook/layers.toml`; `returns` names a `record-kind.*` tag; `routes`
  holds exactly the outcomes as keys. br3 S1 now renders an item through `loop_lib.py declaration
  --item <tag> --json` in a subprocess, refusing with exit 1 and writing nothing when the loop does not
  declare the tag or no loop kit is found (br3:39-47); the verb is br3 F5's open ask to dDeclaredLoop.
- **R5, the disposition door.** dl16 claims no `build_records.py new disposition` verb.
- **R6, the overlay composition's reads.** Every read the composition makes passes `--rev HEAD`
  (oc46 S6, oc35 S5).
- **R7, dDeclaredLoop's guard.** dl2's `tools/loop/guard.py --staged` is the pre-commit verdict and
  reads no trailer; the `Gov-Policy:` trailer is checked by `--push-range`; dl2 refuses an agent
  commit to `guarded-paths.txt` under every value (br6 and br23 now apply it so).
- **R8, the witness channels and the budget edges.** dl3 S2 names the channel set a witness may use;
  dl33 S3 says contention never draws on the budget. dPlacedRequest's `--claims` prints fields 1 to 5
  only, and `read_claims` fetches `refs/gov/leases/*` from the remote in one bounded fetch
  (pr1:76-80, :206-208).
- **R9, a catalogue-default read.** br21 rev-3 gives `read_policy_setting(key, root)`, the roles kit's
  one runner of `policy.py get`, a `with_default` argument, and it is the form a read with a catalogue
  default takes (br21:41-50). br43 S21 makes every roles-kit caller use it, and says no file under
  `tools/roles/` runs `get` outside it or imports the policy kit (br43:105-110; AC21's predicate at
  br43:427-429). Without `with_default`, None means the key sits at its catalogue default or no policy
  kit was found; with it, None means only no policy kit. A roles-kit spec that reads None as the
  default and types the default's value, or reads a key outside `read_policy_setting`, is a MISMATCH.
  Outside the roles kit, R3's `policy.py get` subprocess is the rule.

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not a re-ground touched
  it.
- **MISMATCH:** today's parent text says something else: a renamed surface, a moved reader, a fork
  resolved another way, a refusal the parent now states, or a rule above that the spec breaks. Quote
  both sides with `file:line`, and state in one or two sentences the change the dRankedPlan spec
  needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other. A citation group checks every assumption about a revised unit and
applies R1 to R9 to its own specs. A rule-wide group checks only R1 to R9, on the hits named above:

- **Group A, citation, led by spec 1:** specs 1, 2, 3, 10, 11, 13, 16, 33, 48 and 52.
- **Group B1, rule-wide, led by spec 4:** specs 4, 5, 6, 7, 8, 9, 12, 14, 15, 19, 21, 22, 23, 24, 25,
  26, 27 and 28.
- **Group B2, rule-wide, led by spec 29:** specs 29, 30, 31, 32, 37, 38, 42, 45, 51, 57, 60, 61, 62,
  64, 67, 74, 77 and 81.

The spec files are `memory/builds/dRankedPlan/spec/2026-10-2?-spec-TOOL-dRankedPlan-<n>.md`. The
parents' are `memory/builds/dBoundRoles/spec/2026-10-2?-spec-TOOL-dBoundRoles-<n>.md`,
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`,
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`, and for the rules
`memory/builds/dKeptSession/spec/2026-10-2?-spec-KICK-dKeptSession-<n>.md`,
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`,
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md` and
`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`. Read every mention of
a parent unit in each of your specs, then the cited parent text, its §9 rev lines first.
`git show <re-ground commit> -- <spec>` shows what each re-ground moved; `git show 911a70393:<spec>`
reads a parent as dRankedPlan's spec run read it. The sibling build dFurnishedOrders was
cross-checked against the same two re-grounds; its record,
`memory/builds/dFurnishedOrders/build/2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck.md`,
shows the classes that turned up.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `rpN:L` for line L of dRankedPlan spec N, `brN:L` for dBoundRoles spec N, `trN:L` for
   dTotalRecall spec N, and `dlN:L`, `ksN:L`, `ocN:L`, `wbN:L`, `prN:L` for the others. `Rule` is
   `cite` for a citation assumption, else the R-number.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dRankedPlan spec
   needs, then `Cause:` either the re-ground (the parent text moved in the re-ground commit) or
   pre-existing (it already read so at `911a70393`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit the rule does not bind, one line saying why.
5. One line per citation spec: the revised parent units it cites that none of its assumptions depend
   on.

### Non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent restates one of their surfaces
  that the dRankedPlan spec relies on through it.
- No defect in dRankedPlan's own design that no parent causes.
- No verdict about specs 82 and 83, written after both merges.
