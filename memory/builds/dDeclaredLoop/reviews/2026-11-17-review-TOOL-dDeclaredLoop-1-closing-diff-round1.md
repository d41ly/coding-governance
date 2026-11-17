**Serves:** diff-review TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112

# Tier-2 diff review — dDeclaredLoop (the Spine build of the dClosedLoop chain), round 1

Provenance: gov-diff-reviewer finders over five lenses, gov-skeptic batches, synthesis by gov-synthesizer, at head 520e5125c on branch/unattended-declared-loop-d56bf0.

Range reviewed: 2ba17e9d690eb26ef8796fc0eddf190daba3b43b...520e5125c581f2dcb1b4df6f550956555c126f0e (ROUND 1).

## Verdict: CLEAN WITH FIXES

No blocker survived the skeptics.
Six items stand: 2 HIGH, 2 MEDIUM, 2 LOW.
By raw confirmed finding the tally is 7: 2 high, 3 medium, 2 low.
Every item is owed a fix, or a close deviation for the records items, before the close's merge bar and RED-first observations run.

Review shape: intensity full, raw 8, confirmed 7, refuted 0, merged 1, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 0 | 0 | 1 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- Demotions: 0 contradictory verdicts and 0 orphaned duplicate refutations demoted to unverified.
- 1 duplicate refutation was counted as a merged confirmation (finding 2, merged into finding 1).
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 2 judged sound, 0 UNSOUND, 5 INSTANCE-ONLY (curing the cited instance and leaving its class standing), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (finding 5, high to medium).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 1 spec document supplied as `specs`, beside the range's commit messages.
- Checklist: 152 items from --for-diff over the range, split security 31, correctness 31, seams 30, verification 30, intent 30.
- By design: the caller's byDesign plus 3 invariants from the checklist's by-design block.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twin flags.
- Dispositions: unclassed refuse; 152 class slugs and 198 leg names handed.

Every counter that would mark the run incomplete is zero, so this run is complete.

## Items

### 1. HIGH — a merge whose first parent lacks the policy file is never graded (finding 1; finding 2 merged)

- Where: tools/loop/guard.py@13a73d3e:479 (the first-parent read at :477, the early `continue` at :479-482).
- What is wrong: the push arm reads `old` from the first parent only. When that parent lacks .governance/policy.toml, it prints 'adds ... not graded' and continues, for merges as well as commits. That skips the merge skip at :486, read_remerge_policy at :491 and all parents-only or every-parent grading.
- Consequence: a merge with an orphan (or file-deleting) first parent and the default branch as its other parent can change any policy value with no Gov-Policy trailer and no change record. The finder's probe confirmed it: `guard.py --push-range B..M` printed '0 finding(s)' and exit 0 on agents-in-flight 6 to 60, while the plain-commit control exited 1. help/policy.md:293-311 exempts only a commit that adds the file.
- Grade: high (binding). The path needs a first parent without the file, so it is narrow.
- Merged finding: finding 2 (correctness lens) is the same defect at the same lines, with the 'main deleted the file, then merged the run branch' topology. Its skeptic counted it as a merged confirmation. It is not a separate item and is not counted again.
- Fix (judged SOUND by the skeptic): treat the file as added only when NO parent holds it. For a merge, read every parent's blob. If any parent holds the file, grade the merge on the merge path (clean re-merge, or against every parent that holds it), never 'adds, not graded'.
- Left-shift gate: add a plant to the loop guard fixtures leg: an orphan first parent merged with a base that holds the policy file, with a changed value, must exit 1. Observe it RED against the current code first.

### 2. HIGH — the move to resolve_memory_root was half applied: five loop readers still take the builds root from .memory-tree.conf alone (findings 3, 4)

- Where:
  - tools/loop/adapt.py@1c930e56:236 (read_disposition_release, finding 3).
  - tools/loop/position.py@87072a03:569 (derive_position_into, plus the conf it passes to read_records at :607, finding 4).
  - tools/loop/loop_parents.py@d078c52c:110 (read_withdrawn_parents, finding 4).
  - tools/loop/loop_lib.py@637ea901:694 (read_builds_dir, finding 4).
  - tools/loop/upstream.py@43147593:297 (write_upstream_record), named by the skeptic as a fourth sibling.
- What is wrong: tools/loop/loop_lib.py@637ea901:794 calls resolve_memory_root 'the one reader every loop module takes the root from'. It returns the driver .unattended.conf root when that file exists. These sites instead build the builds path from read_design_conf(...)['MEMORY_ROOT'], which reads .memory-tree.conf only and falls back to 'memory'. Within adapt.py, :147 and :180 already use resolve_memory_root, and :236 does not.
- Consequence (finding 3, high): in a tree whose .unattended.conf sets MEMORY_ROOT=records and whose .memory-tree.conf leaves it unset, the disposition glob reads memory/builds. budget.py@ae3163cf:433 prints `disposed unrecorded` and breakpoints.py@790d996d:264 leaves an owner gate `held`, even though a disposition record exists. These are wrong verdicts on a supported configuration that resolve_memory_root_source accepts.
- Consequence (finding 4, medium): in the same tree, derive_position refuses with 'the slug names no build README under memory/builds'. read_withdrawn_parents raises 'not a build folder', and check_actor_list refuses actor-witness rows whose builds live under records/builds. These refusals are wrong but loud, so the effect is contained.
- Why nothing caught it: the no-own-conf-read fixtures grade only budget.py and breakpoints.py. The conf-readers-declared plant does not count a read_design_conf call as an open.
- Grades: finding 3 high, finding 4 medium, both binding. The item takes HIGH.
- Fix (both findings judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix): every loop module that reads a builds folder takes the root from resolve_memory_root. That covers adapt.read_disposition_release, position.derive_position_into including its read_records conf at :607, loop_parents.read_withdrawn_parents, loop_lib.read_builds_dir (which keeps read_design_conf only for DESIGN_RECORD) and upstream.write_upstream_record. Add a driver-only MEMORY_ROOT=records fixture case for each site.
- The finders' proposals cure only their cited instances. Finding 3's proposal passes the resolved root into tools/loop/adapt.py@1c930e56:236's read_records. Finding 4's proposal switches its three named sites. Neither covers tools/loop/upstream.py@43147593:297 or the rest of the population.
- Left-shift gate: extend the no-own-conf-read population in the loop definition fixtures leg to every tools/loop/*.py module, so any builds root derived outside resolve_memory_root is refused.

### 3. MEDIUM — derive_conf_openers cannot see a conf name or conf constant passed straight to open() (finding 5)

- Where: tools/loop/loop_lib.py@637ea901:1048 (the conf-path test at :1048-1052; the NOT SEEN list at :1029-1030).
- What is wrong: a conf path counts only as an operand of `/` or a positional argument of join/Path/PurePath. `open(".memory-tree.conf")` and `open(DRIVER_CONF_PLANT)` (where derive_conf_constants names the constant) are never derived as openers. The NOT SEEN list does not name this shape.
- Consequence: a future undeclared conf reader of either shape in loop_lib.py gets the plant's pass line 'conf readers declared' even though it is in neither CONF_READERS nor CONF_ROUTES. The finder's scratch-copy probe confirmed that both planted functions were missed. The live tree holds no such reader today.
- Grade: medium. The finder graded it high, and the skeptic re-graded it medium because it is a future blind spot with no wrong result now. I keep medium.
- Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix): treat any expression node in the function's own body as a conf path when check_conf_name answers it or it names a derive_conf_constants member. This covers open/parse_conf arguments, a local binding opened later, and the receiver of read_text/read_bytes. Any shape still deliberately excluded gets a NOT SEEN entry. Re-probe a scratch copy holding planted_a, planted_d and a local-variable variant.
- The finder's proposal cures only the cited instance. It counts the open-call's own argument or receiver, or adds the shape to NOT SEEN.
- Left-shift gate: carry the planted_a, planted_d and local-variable probes as standing selftest cases under the loop definition fixtures leg, each required to appear in derive_conf_openers' answer.

### 4. MEDIUM — no fixture exercises any refusal arm of the conf-readers-declared plant (finding 6)

- Where: tools/loop/loop_lib.py@637ea901:1627 (the plant branch at :1625-1627; PLANT_OWED at :244; the refusal arms at :1788-1792).
- What is wrong: the plant always reads pathlib.Path(__file__), and PLANT_OWED owes it exit 0 with the pass line. No selftest or fixture feeds check_conf_readers_plant a module with an undeclared opener or a declared member that opens nothing.
- Consequence: a regression in the refusal logic leaves the loop definition fixtures leg green. Examples are dropping the 'in neither CONF_READERS nor CONF_ROUTES' comprehension, or comparing the wrong tuple. Unit 100's one-off `python -I -c` probe is the only time this red was seen.
- Grade: medium (binding).
- Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix): cover every refusal arm against scratch copies, each asserting its refusal text and exit 1:
  1. an undeclared appended opener;
  2. a copy where resolve_memory_root_source no longer opens a conf, giving 'opens no conf';
  3. a copy with no opener, giving the empty-answer refusal;
  4. an unparsable copy, giving the LoopError refusal.
- Case 2 must change the function body, not the tuple, because the declared tuples come from the live module's globals.
- The finder's proposal cures only the cited instance. It adds two scratch-copy cases: an undeclared parse_conf opener, and a CONF_ROUTES member that opens nothing.
- Left-shift gate: the four cases run in --selftest under the loop definition fixtures leg. The harness arms leg (fail branches armed or pinned) should also count these refusal arms, so a later unarmed arm is refused.

### 5. LOW — unit 100's settled-items row S3 says `parse_conf` is a TREE_LIB_SYMBOLS member; S21, unit 95 and the code say it is not (finding 7)

- Where: memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-100.md@96299153:80.
- What is wrong: row S3 says '95 rev-3 §3 settles `parse_conf` as a member (its S1)'. Row S21 (line 98), spec-95's §3 row S1, and tools/loop/loop_lib.py@637ea901:900 all say it is not. `parse_conf` is a member of CONF_READERS (tools/loop/loop_lib.py@637ea901:962), a different tuple.
- Consequence: a later audit or child build reading S3 may add a wrong third TREE_LIB_SYMBOLS member, which would refuse an older memory-tree kit over a name nothing reads. The defect is in the records only, with no code effect today.
- Grade: low (binding).
- Fix (judged SOUND by the skeptic): correct row S3 at the close through the departures/deviation record, since the spec is CLOSED. State that 95 rev-3 §3 S1 settles `parse_conf` as no TREE_LIB_SYMBOLS member (it is a CONF_READERS member), so S3 agrees with S21 and tools/loop/loop_lib.py@637ea901:900.
- Left-shift gate: a spec-tokens check that resolves a settled row's claimed membership against the named tuple's live members would refuse S3. Until such an arm exists, add a bug-class checklist entry.

### 6. LOW — unit 99's hands-off edge claims a re-run by unit 100 that never happened (finding 8)

- Where: memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-99.md@c4913160:126.
- What is wrong: the edge says unit 100's 'AC6 re-runs [the conf-readers-declared plant] over the conf read it rewrites'. Unit 100 rev-2 drops AC1 to AC21, closes on AC22 alone, and writes nothing under `tools/` ('no read moves'; pass commit c9a4c606f). No conf read was rewritten, and the plant was not re-run.
- Consequence: the closed record counts coverage that was never run, which is an empty population read as coverage. The effect stays in the records, because the plant still runs under the loop definition fixtures leg.
- Grade: low (binding).
- Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix): write one close deviation covering all ten hands-off edges into unit 100 (specs 41, 60, 64, 72, 90, 92, 94, 95, 96 and 99). For each, state that unit 100 rev-2 settled the edge's ids in its §3 table with no write and no re-run, and give the standing observation where one exists. Edges of the same defect include:
  - 60 and 64 restate onto read_tree_conf, which does not exist;
  - 72 re-runs the confs-disagree plant over a read that never moves;
  - 90 says unit 100 'restates and re-runs' AC4 and AC5.
- The finder's proposal cures only the cited instance. It records one deviation for spec-99's edge (ids 10, 19 and 20, no AC6), naming the loop definition fixtures leg and the close's RED-first run as the only standing observation.
- Left-shift gate: when a unit's spec is revised, check every hands-off edge that names that unit, and refuse an edge that cites an AC the target spec no longer holds. This belongs with the spec-tokens legs.

review-shape kind=diff-review round=1 intensity=full at=synth raw=8 confirmed=7 refuted=0 merged=1 unverified=0 blocker=0 high=2 medium=3 low=2 agents=10 out-tokens=52805 trigger=owed shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=2 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/loop/guard.py@13a73d3e:479 | high | high | confirmed | guard.py is new in this diff (it is absent at 2ba17e9d6). At line 477 `old` is read from c['parents'][0] only. At 479-482 `if old is None:` prints 'adds ... not graded' when the merge's combined diff lists the file, and then `continue`s for both commits and merges. That happens before the merge's skip at 486, read_remerge_policy at 491 and the parents-only or every-parent grading. So a merge whose first parent lacks .governance/policy.toml and whose second parent holds it is never graded, whatever values it sets. help/policy.md:293-311 exempts only 'a commit that adds the policy file, as an adopter's scaffold does' and says merges are graded. A resolution that changes a value no parent holds, with no trailer, passes with exit 0. Every push-merge-resurrect plant (tools/loop/guard.py@13a73d3e:594-602, 951-973) uses the topology where the first parent holds the file, so no plant covers this one. The path needs a first parent without the file (an orphan, or a side that deleted it), so I grade it high, not blocker. | sound | - | class:a-merge-of-the-default-branch-read-as-additions |
| 2 | correctness | tools/loop/guard.py@13a73d3e:479 | high | - | refuted | duplicate of id=1. It is the same defect at the same lines, tools/loop/guard.py@13a73d3e:477-482: `old` comes from the first parent only, and the early `continue` on `old is None` keeps a merge out of all merge grading. Its 'main deleted the file, then merged the run branch' topology is one more instance of a first parent lacking the file. I checked it against the code: the plants at tools/loop/guard.py@13a73d3e:594-602 only cover the mirror topology. Its fix is also sound: reading the first parent as {} and falling through matches the parents-only path's rule at 528 that a lacking parent reads as {}, and it reaches the re-merge grading. | sound | - | - |
| 3 | seams | tools/loop/adapt.py@1c930e56:236 | high | high | confirmed | The claim holds, and the code is new: tools/loop/adapt.py does not exist at base 2ba17e9d6. In tools/loop/adapt.py@1c930e56:236, read_disposition_release calls read_records(root, read_design_conf(root), ...). tools/memory-tree/build_records.py@e689f3e9:249 takes MEMORY_ROOT only from that conf, falling back to 'memory'. tools/loop/adapt.py@1c930e56:147 and :180 instead use resolve_memory_root. That function (tools/loop/loop_lib.py@637ea901:773-790) returns the .unattended.conf root when that file exists, and only raises when both confs name different roots. So a driver-only MEMORY_ROOT=records is accepted, and the disposition glob still reads memory/builds. Both callers are affected: tools/loop/budget.py@ae3163cf:433 and tools/loop/breakpoints.py@790d996d:264, whose README read at :255 uses resolve_memory_root_source. The result is a wrong released/held verdict, but only in a narrow configuration, so high. | instance | two-readers-of-one-config-one-re-derived | class:two-readers-of-one-config-one-re-derived |
| 4 | seams | tools/loop/position.py@87072a03:569 | medium | medium | confirmed | I read the cited lines. tools/loop/position.py@87072a03:568-569 and tools/loop/loop_parents.py@d078c52c:110 build the builds path from read_design_conf(...)['MEMORY_ROOT'], and so does tools/loop/loop_lib.py@637ea901:694. All three ignore .unattended.conf. That contradicts tools/loop/loop_lib.py@637ea901:794's docstring, which calls resolve_memory_root 'the one reader every loop module takes the root from'. All of this code is new in the diff. When only the driver conf names the root, derive_position refuses because it finds no README under memory/builds, and read_withdrawn_parents raises 'not a build folder'. These are wrong refusals on a supported configuration, but they fail loudly rather than certify something false, so the damage is contained: medium. | instance | two-readers-of-one-config-one-re-derived | class:two-readers-of-one-config-one-re-derived |
| 5 | verification | tools/loop/loop_lib.py@637ea901:1048 | high | medium | confirmed | At tools/loop/loop_lib.py@637ea901:1048-1052 a conf path counts only if it is an operand of a `/` BinOp or a positional argument of a join/Path/PurePath call, and that operand must pass check_conf_name or name a derive_conf_constants member. `open(".memory-tree.conf")` and `open(DRIVER_CONF_PLANT)` contain neither shape, so builds is False and the function is never derived. check_conf_readers_plant (1776-1797) then prints its 'conf readers declared' pass line. The NOT SEEN list at 1029-1030 names three shapes: a path built in one function and opened in another, a run-time composed name, and subprocess reached under another name. A literal or constant passed straight to the open call is not among them. The live tree holds no such reader today, so this is a future blind spot in a guard, not a wrong result now. That makes it medium. | instance | - | new:opener-derivation-blind-to-a-direct-open-argument |
| 6 | verification | tools/loop/loop_lib.py@637ea901:1627 | medium | medium | confirmed | The plant branch at tools/loop/loop_lib.py@637ea901:1625-1627 always calls check_conf_readers_plant(pathlib.Path(__file__)), and PLANT_OWED at 244 owes it exit 0 with the pass line. A grep of tools/ for check_conf_readers_plant, derive_conf_openers, 'opens no conf' and 'in neither CONF_READERS' finds only the definitions, the one plant call and README prose. No selftest or fixture feeds a mutated module, so none of the refusal arms at 1788-1792 is ever exercised. Someone could break those arms and the leg would stay green. | instance | - | class:refusal-branch-with-no-arm |
| 7 | intent | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-100.md:80 | low | low | confirmed | Spec-100 line 80 (row S3) says '95 rev-3 §3 settles `parse_conf` as a member (its S1)'. Row S21 (line 98) says '`parse_conf` is no member (95 rev-3 §3, its S1)'. Spec-95's §3 row S1 rejects `parse_conf` as a third TREE_LIB_SYMBOLS member, and tools/loop/loop_lib.py@637ea901:900 holds only derive_docstring_ids and derive_constant_charges. Row S3 contradicts S21, unit 95 and the code. The defect is in the record only, so it has no effect on behaviour. | sound | - | class:two-answers-to-one-question |
| 8 | intent | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-99.md:126 | low | low | confirmed | Spec-99 line 126 says unit 100's 'AC6 re-runs [the conf-readers-declared plant] over the conf read it rewrites'. Spec-100 rev-2 drops AC1 to AC21 (lines 55 and 74) and closes on AC22 alone. Its write set (line 125) is 'None under `tools/`', and its S13 row says 'no read moves'. Its only mention of the plant (line 101) lists it as out of scope at order 50. So the edge claims a re-run that never happened. The effect stays in the records, because the plant still runs under the loop definition fixtures leg. | instance | - | class:observed-by-claim-no-arm-discharges |
