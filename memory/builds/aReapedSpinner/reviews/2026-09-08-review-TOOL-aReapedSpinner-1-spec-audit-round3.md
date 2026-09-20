**Serves:** spec-audit TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7

# aReapedSpinner — Tier-2 spec audit, round 3

*Adversarial pre-code pass over the seven-unit spec set for `tools/process-monitor/`, at rev-3. Node `a`, 2026-09-08, base `e2b82a53`. Findings are pre-code: nothing here is a bug in shipped software, every one is a defect in a document that would become one. Round 1 found 15 defects, 6 of them blockers. Round 2 found 16, 5 blockers, and eight of those sixteen were created by a round-1 repair. This round was sent at the pattern rather than at the defects: did the round-2 architectural repairs — the tree closure, the two parent graphs, the per-row signal — introduce new ones.*

**Range — ROUND 3**, seven subjects pinned at these blobs: `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-1.md@633b3c93d1ef6af2ba0799b51df8acbbd2688cbd`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-2.md@453e8c1653fbf5c1d23a748425706c19e1548379`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-3.md@ba77cde21235cf29042d307febe956c52ef3c3a2`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-4.md@5756ebd50658b50e620df402eb9090cf0bf60c44`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-5.md@203ab03b75ee2d1642f17ef5e08e84201112e97d`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-6.md@539098671a39c534ec86a37291fba8e61fc7e83b`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-7.md@df723ea0c28ce83225900a7310d0b57ed3bf7cae`.

## Verdict: BLOCKED

Eight blockers, three highs, five mediums, over sixteen distinct defects — and the answer to the question this round was sent to ask is yes, emphatically. **Ten of the sixteen defects below did not exist at rev-2: they were created by a round-2 repair.** Three more were half-created by one. Only three are pre-existing survivors. Round 2's ratio was 8 of 16; round 3's is 10 of 16, and the three defects that are genuinely new architecture — the tree closure, the graph union, the per-row signal — each shipped with a hole in it.

The pattern is now specific enough to name. **A repair is being applied at the address the finding named, and the consumers of that address are not being re-read.** D18's repair moved the parent question onto `win_ppid` in unit 3's prose and left the `PARENT-UNKNOWN` predicate keyed on `msys_ppid`, which is `None` for every native row — so the default reap mode is now structurally incapable of touching the ~300-row population the kit exists for. D20's repair moved unit 7's probe onto the runner's own process in S4 and §4 and did not touch AC4 or AC5, which still grade a scratch root that §4 now says no unit declares. D22's repair unioned the two parent graphs without naming the join that translates one namespace into the other, so the union degenerates back to the graph it started from. D21's repair introduced a `kind` field whose stated rule labels the entire table `msys`, and pinned the native kill as `taskkill //PID`, which is an MSYS shell idiom that a fixed-argv python caller cannot use. Round 2's own suggested fix text was folded verbatim in two places — unit 6 AC8 and unit 1 AC11 — and both are now defects, because the fix text was written against rev-2's data model and nobody re-derived it against rev-3's.

The safety story is worse than the arithmetic. Unit 2's self fence, as written, excludes the caller's whole ancestor chain from being a root, which in the deployment shape the kit ships into — invoked BY `run-gates.sh` — makes the in-scope set empty and every criterion that depends on a non-empty one unstageable. So the fence has zero coverage. Meanwhile the measured unscoped orphan predicate flagged 297 of 315 rows including `lsass.exe` and Defender. Those two facts sit either side of one conf value: if the fence is repaired by admitting the self chain and nothing else changes, the only thing between `reap-orphans` and `lsass.exe` is a predicate that unit 3 has just made incapable of firing on native rows anyway. Both directions are wrong, and neither is graded.

Nothing here needs a unit re-scoped. Every fix is a spec edit. But this set should not be dispatched until the closure's termination, the graph union's namespace join, and the self fence's root rule are all written down, because those three are the ones that get a builder to write code that hangs, kills the wrong subtree, or kills nothing at all.

### Review shape

Raw 63 · confirmed 34 · refuted 29 · unverified 0 · precision 0.54.

**Run integrity — all clean.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline. No arm of this run failed to report, so the zero counts here are evidence rather than an absence of evidence, and the finding set is complete as far as four lenses reach. This run is complete.

**Consolidation.** The pipeline discarded no duplicates, but the 34 confirmed findings describe **16 distinct defects**: four lenses landed on the `PARENT-UNKNOWN` predicate from four sides, four on unit 6's `--check-path` conjunct, four on unit 7's stale AC4/AC5, three each on the self fence, on unit 1 AC11 and on `taskkill //PID`. Each row carries its raw ids so nothing is lost. Severities are the ones adjudicated HERE; a merged defect takes the maximum severity in its cluster, which promoted raw 45 (HIGH) into D33 and raw 6 and 57 (HIGH) into D35. Adjudicated totals across the 16 rows: **8 blockers, 3 highs, 5 mediums, 0 lows.**

| # | Sev | Unit | Address | Defect | Raw ids | New at rev-3? |
|---|-----|------|---------|--------|---------|---------------|
| D32 | BLOCKER | 3 | §2 S3 and §4 "PARENTLESS and PARENT-UNKNOWN", vs AC3/AC4 | `PARENT-UNKNOWN` fires on absent `msys_ppid`, which is every native row, so no native process can ever grade `ORPHAN` and `reap-orphans` is inert over the whole target population | 1, 21, 34, 53 | yes — D18's repair, re-keyed onto the wrong graph |
| D33 | BLOCKER | 1, 4 | 1 §2 S3 and §4 "which side supplies what", AC2 | The `kind` rule labels the entire table `msys`: `ps -W` reports every Windows process under the synthetic id `winpid \| 0x400000`, and no section declares that bit as the discriminator | 17, 45 | partly — D21's repair added `kind`, never its test |
| D34 | BLOCKER | 2, 7, 4 | 2 §2 S2/S4 and §4 "The self fence", vs 7 S4/AC5 and 4 AC5/AC6 | A `self_chain` row may not be a root and rows reachable only through it are excluded, so a tool invoked BY the runner has an EMPTY in-scope set | 2, 20, 52 | yes — the self fence is D9/D17's repair |
| D35 | BLOCKER | 7 | §6 AC4 and AC5, vs S4 and §4 "Detection, at profile time" | Both criteria still grade admission of "the runner's scratch parent" after rev-3 removed the scratch root everywhere; AC4's precondition is permanently true, AC5's permanently false | 6, 23, 36, 57 | yes — D20's repair reached S4, not the criteria |
| D36 | BLOCKER | 6, 2 | 6 §6 AC8 second conjunct, vs 2 S7 and 6 §3 | AC8 requires `scope.py --check-path`, a mode no unit declares, from a file shipped two orders later, observed by this order-1 unit's own adopter suite | 5, 22, 37, 58 | yes — round 2's fix text folded literally; D1's class |
| D37 | BLOCKER | 2, 4 | 2 §2 S3 and §4 "The closure", vs 4 §4 "The walk" | The union of the two parent graphs is specified over raw ids, but `msys_ppid` holds MSYS ids and the map is keyed on `winpid`; no spec names the `msys_pid`→`winpid` join | 18 | yes — D22's repair, unioned without the translation |
| D38 | BLOCKER | 2 | §2 S3 and §4 "The closure, and why it is the whole fence" | The closure and the `self_chain` ancestor walk carry no visited-set and no termination statement, over a graph this build MEASURED to contain a cycle | 19 | yes — the closure is new at rev-3 |
| D39 | BLOCKER | 7, 4 | 7 §2 S1 and S2 | The runner records leg pids in bash (`$!`/`$BASHPID`), which are MSYS ids, and hands them to `run_kill(winpid, …)`; unit 4 AC8 then refuses every one and the refusal reads as correct behaviour | 35 | no — pre-existing since rev-2's delegation |
| D40 | HIGH | 1, 4 | 1 §6 AC11 | AC11 puts every row of the FROZEN fixture to a live liveness probe; the fixture's processes are dead, so the arm can neither pass on a correct implementation nor fail on a broken one | 8, 25, 54 | yes — round 2's left-shift text folded verbatim |
| D41 | HIGH | 4 | §2 S4, §3, §4 signal table, §8 F4, AC10 | The native kill is pinned as `taskkill //PID <winpid> //F`; the doubled slash is an MSYS shell idiom and is rejected as an invalid option by a fixed-argv caller | 27, 48, 56 | partly — D21's repair pinned the prose spelling |
| D42 | HIGH | 7, 2 | 7 §2 S4 and §4 condition 3, vs 2 S7/AC10 | The profile probe is `scope.py --explain $$`, an MSYS pid, against an interface unit 2 defines over a `winpid` | 24, 46 | yes — D20's repair introduced the probe |
| D43 | MEDIUM | 4, 2 | 4 §2 S1 and §4 "The walk" | The reaper rebuilds its own child map with no start-time corroboration, so the edges unit 2 refused to trust are live again inside the kill walk | 10 | yes — corroboration is new at rev-3, in unit 2 only |
| D44 | MEDIUM | 3, 2 | 3 §4 "PARENTLESS", vs 2 §4 start-time paragraph | One graph, two edge-validity rules: unit 2 drops a recycled parent edge, unit 3 trusts it, so a genuine orphan with a recycled parent pid grades not-ORPHAN | 61 | yes — both halves new at rev-3 |
| D45 | MEDIUM | 5, 6 | 5 §2 S4, §4 "Files touched", AC5, AC9 | No `*.fragment.json` is declared, so `settings-merge.py` cannot wire the hook and `check-hook-destinations.sh` never sees it; Files touched omits the two unit-6 files S4 mandates editing | 49, 59 | partly — D23's repair folded the `kit.toml` half only |
| D46 | MEDIUM | 5 | §6 AC2 | AC2's observation holds identically whether the throttle stamp is written before or after the work, which is precisely the failure its own Red-when names | 14 | no — pre-existing, unreached by rounds 1 and 2 |
| D47 | MEDIUM | 7 | §7 "New arm", the ARMS_FLOORS sentence | The claimed assertion floor still does not exist: `.memory-tree.conf` names no `run-gates` row and `check-arms.py` does not discover `run-gates.sh` at all | 62 | no — D27, repaired by deleting the falsifiable half |

---

## The four questions this round was sent to answer

**1. Is the tree closure sound?** No, in three separate ways, and the blast radius of each is a whole subtree rather than a row.

*Can an unrelated process attach to an in-scope tree?* Yes — D37. The closure is specified over "the union of the census's two parent graphs" with no statement that `msys_ppid` must be translated through the census's own `msys_pid`→`winpid` table first. Untranslated, an `msys_ppid` of 2315334 matches no row in a `winpid`-keyed map and the MSYS half of the union contributes nothing, which silently reverts the graph to the Windows-only one that D22 was raised to fix. Where a small MSYS id *does* collide with a live `winpid` — and MSYS ids are small integers while winpids are dense in the same range — an unrelated process is adopted into the tree and its entire subtree becomes killable. That is the founding bug class of this build reappearing inside the repair for a different instance of it.

*Does the closure terminate?* Not provably, and the build's own measurement says it does not. The union-graph record measures a cycle on this node's real process table and states that a depth-unbounded walk over it without a visited-set does not terminate. Unit 4 §8 F3 carries the visited-set guarantee in writing for its walk; unit 2, which owns both the closure AND the `self_chain` ancestor walk over the same graph, carries none, and §5's "one graph walk; linear in the table" asserts a cost property in place of the guard (D38). The ancestor walk is the more dangerous of the two: a chain walk is the exact shape that spins.

*Is the start-time corroboration correct, and can it be staged?* The rule itself is right and it is gated — unit 2 §4 drops an edge whose child predates its claimed parent, and AC9 stages it. Its problem is that it is the only place in the set that applies it. Unit 4 rebuilds the child map from scratch for the kill walk with no corroboration (D43), so a row admitted by root A can be dragged into target T's kill set through an edge unit 2 refused to trust; and unit 3's `PARENTLESS` trusts a `win_ppid` edge on the id alone (D44), so `--explain` and `--report` can describe one row two different ways. Two units, one graph, three trust rules.

*Does the self fence interact correctly with closure?* No, and this is D34, the worst defect in the set. Unit 2 S2 bars a `self_chain` row from being a root and S4 excludes rows reachable only through the chain. When `scope.py` or `reap.py` is invoked BY `run-gates.sh`, the runner and the invoking shell are ancestors of the caller, hence in `self_chain`, hence never roots — and every leg hangs off the runner and off nothing else. The whole in-scope set is empty in the shape the kit actually ships into. Unit 2's own AC4 red-when names this state ("would exclude everything the session started") while S4 as written produces it, and AC4's positive half is satisfiable only by a fixture that plants a second root outside the chain, which no live invocation has. The fence's blast radius grew to a subtree and its coverage fell to zero.

**2. Two parent graphs.** *Is the union acyclic?* No — measured, on this node, per D38. Nothing in the set says so and nothing guards it.

*What happens when the two graphs disagree about one row's parent?* Nothing is specified. The union takes both edges, so the row has two parents and the closure admits it from either subtree; the seven rows measured to disagree are counted by no criterion and reported by no diagnostic. In the D37 state — the join never named — the disagreement resolves silently in favour of the Windows edge every time, which is the direction that loses the MSYS parent the overlay exists to supply.

*Does `PARENTLESS` via `win_ppid` have a false-positive population on Windows?* Yes, and it is large. Windows does not reparent: when a parent exits normally its children keep a `win_ppid` naming a pid that no longer exists, so every child of any normally-exited launcher is `PARENTLESS` on the id test alone. The measured unscoped predicate flagged 297 of 315 rows including `lsass.exe` and Defender at rate 0.79. Pid recycling supplies the opposite error — a recycled parent pid makes a genuine orphan grade not-orphan (D44). So the predicate is wrong in both directions and its entire safety rests on the scope fence, which D34 says is empty and which, once repaired, is the only thing standing between `reap-orphans` and `lsass.exe`. That is why D32 and D34 are both blockers: one makes the default mode inert on the population it wants, the other governs whether it is inert on the population it must never touch.

**3. Per-row signal.** The kind test in unit 4 §4 is operational — `kill -0 <msys_pid>` answering decides the signal — and that is the right shape, because it asks the question the kill will ask rather than trusting a label. Three problems around it.

It is anchored to a criterion that grades nothing: unit 4 §4 names unit 1 AC11 as "the reason it exists on the census side", and AC11 puts a live liveness probe to a committed frozen fixture whose processes are long dead (D40). Under the liveness reading it can never pass; under the weaker "the probe returned something" reading it can never fail, because a dead row and an unaddressable live row both answer `No such process` — the exact distinction the criterion exists to draw. On a box that has recycled those pids it can also go green on an unrelated process.

The label is separately inverted and still load-bearing: unit 1 §3 hands `kind` to unit 4 "for the signal choice", while unit 1 S3's stated rule grades the whole table `msys` (D33). Two contracts, one field, and the measured 10-of-313 split is not reproducible from either.

*Can the kind test be staged?* Yes, but only against live processes the arm spawns itself — one MSYS, one native. It cannot be staged over the frozen fixture, which is what AC11 tries.

*Does the `taskkill //PID` path have a failure mode the `/T` measurement does not cover?* Yes, and it is fatal (D41). Every `taskkill` invocation in this build's records was typed at a Git-Bash prompt, where `//PID` is the escaping idiom that stops MSYS rewriting the argument. Unit 4 §3 pins the interpreter as native `win32` python and unit 1 §5 pins a fixed argv with no shell, so `taskkill.exe` receives `//PID` verbatim and rejects it: verified on this node, `taskkill //PID 999999 //F` returns rc 1 with `ERROR: Invalid argument/option - '//PID'`, while `/PID` reaches the pid lookup. The `/T` measurement covers taskkill's tree walk being unreliable; it does not cover the argv path at all, because no arm in any record ever issued taskkill from python. AC10 then pins the broken spelling AND asserts the process is dead by re-read, and those two cannot both hold.

**4. Criteria that still cannot fail.** Seven of the sixteen defects are this class, which makes it the dominant shape of the round for the third time running. D46 (unit 5 AC2 — the observation is identical whether the stamp is written before or after the work, so the ordering defect its own red-when names is ungradable). D40 (unit 1 AC11, unfailable in both readings). D32 (AC3 and AC4's first sentence are satisfiable entirely with MSYS fixture rows, so the dead native class is invisible). D33 (AC2 needs one native row and the ~4 unoverlaid rows supply it, so a rule that inverts ~300 rows passes). D34 (AC4's positive half needs a planted root that no live invocation has). D35 (AC4's precondition is permanently true and AC5's permanently false, so the delegated path — the build's highest-risk change — is graded by nothing at all). D37 and D43 (AC3's chain is reachable over Windows edges and AC1's fixture stages no bad edge, so both the missing join and the missing corroboration pass either way).

## Ordering, and the two units at order 6

**Is the declared ordering satisfiable?** Yes, with exactly one violation, and it is D36. Traced over every `consumes-from` edge in the set: unit 6 (order 1) declares no in-set consumes-from; unit 1 (2) ← 6; unit 2 (3) ← 1, 6; unit 3 (4) ← 1, 2, 6; unit 4 (5) ← 1, 2, 3, 6; unit 5 (6) ← 4, 6; unit 7 (6) ← 4, 2. Every edge points backwards in order, so `6, 1, 2, 3, 4, {5, 7}` satisfies all of them. The single back-edge is not in an Edges block at all — it is inside unit 6's AC8, which runs `scope.py --check-path` from an order-1 unit's own `adopt-process-monitor.test.sh` against a file unit 2 ships at order 3, in a mode unit 2 never declares. Round 2 proposed the exact lint that would have caught this ("every path named in a criterion's observer must be shipped by a unit whose order is no greater than this one") and it was not built; the very next revision violated it.

**Are units 5 and 7 genuinely disjoint at order 6?** On the true file sets, yes. Unit 7 edits `tools/run-gates/run-gates.sh` and `run-gates.test.sh` and explicitly declines to write `.process-monitor.conf` because unit 5 reads it. Unit 5 creates `procmon-hook.js` and edits `.claude/settings.json`, plus — per its own S4 and AC5, though not per its Files touched — `tools/process-monitor/kit.toml`, `adopt-process-monitor.sh` and `adopt-process-monitor.test.sh`. Those two sets do not intersect.

But the conclusion is right by luck, not by evidence. The disjointness argument rests on the Files touched lists, and unit 5's is incomplete by three files that its own scope item mandates editing (D45). A disjointness proof over a list that omits the files the unit actually edits proves nothing; it happened to hold this time. There is also one shared obligation neither spec names: unit 5's `kit.toml` edit drags `KIT_PROCESS_MONITOR_VERSION` and its marker carriers, and if unit 7 ever grows a kit-file edit the two passes collide on a version bump with no coordination declared.

---

## Blockers

### D32 — BLOCKER — unit 3 §2 S3 and §4 "PARENTLESS and PARENT-UNKNOWN", against AC3 and AC4

*Raw ids 1, 21, 34, 53. New at rev-3: D18's repair, re-keyed onto the wrong graph.*

§4 defines `PARENT-UNKNOWN` as "`msys_ppid` is absent, or `cpu_s` is `None`", and S3 applies labels first-match-wins with `UNKNOWN` first. Unit 1's data model makes `msys_ppid` `None` for every `kind == 'native'` row by construction, and AC7 makes every unjoined CIM row native — measured, that is 300-plus of 313. So every native row short-circuits to `UNKNOWN` before `PARENTLESS` is ever tested, and no native process can ever grade `ORPHAN`, `SPIN` or `IDLE`.

The consequence is that the kit's default mode is inert over the entire population it was built for. Unit 6 §8 F1 justifies `PROCMON_REAP_MODE=reap-orphans` on the strength of the `ORPHAN` class; `run-gates.sh` dispatches its legs as native `python.exe` rows; those rows can never be `ORPHAN` however long dead their parent is. The spec contradicts itself three ways over in the same revision: AC3 and AC4's first sentence both say a flagged row whose `win_ppid` names no census row IS `ORPHAN`; §4's own later sentence says the MSYS graph is used "for the descendant walk (unit 4) and for nothing else"; and §3 Edges, together with unit 1's hands-off line, hand this unit only `age_s`, `cpu_s` and `win_ppid`. Nothing reds, because AC3 and AC4's first sentence are stageable with MSYS fixture rows and AC4's second sentence blesses the swallowing case.

The cause is legible. Round 2's D18 fix was written against rev-2's MSYS-keyed census where `ppid == 0` was the sentinel; rev-3 removed the sentinel by defining `win_ppid` for every row, and the fix text was translated to "`msys_ppid` absent", which names a different population.

**Fix.** Drop the `msys_ppid` clause from `PARENT-UNKNOWN` entirely, leaving `cpu_s is None` and nothing else — rev-3 already moved the parent question onto `win_ppid`, which has no sentinel, so the MSYS graph carries no parent signal in this unit at all. Re-point AC4's second sentence at a `cpu_s is None` row. Add two criteria: a flagged NATIVE row (`msys_ppid` `None`) whose `win_ppid` names no census row grades `ORPHAN`, and the same row under `reap-orphans` is killed.

**Left-shift gate.** A field-provenance lint over the spec set: every field named in a unit's §4 predicates must appear in that unit's §3 `consumes-from` list. Unit 3's Edges names exactly `age_s`, `cpu_s`, `win_ppid`; `msys_ppid` appears in its §4 predicate and in no edge. That is a two-line check over parsed sections, no semantics, and it reds this defect at authoring time. It would also have caught D44.

### D33 — BLOCKER — unit 1 §2 S3 and §4 "Windows: which side supplies what", against AC2

*Raw ids 17, 45. Partly new at rev-3: D21's repair added `kind`, never its discriminator.*

S3 sets `kind = 'msys'` when "`ps -W` supplied an msys id for that winpid", else `native`. But the serving record states that `ps -W` reports every OTHER Windows process too, under the synthetic id `winpid | 0x400000`, and unit 1 §4 repeats it as universal — all 321 rows had `PID != WINPID`. So `ps -W` supplies a PID for every row and the stated rule labels the entire table `msys` with a non-`None` `msys_pid`, which contradicts the same section's measured "MSYS rows are 10 of 313" and the data model's "`msys_pid` present only for `kind == 'msys'`". The figure is only reproducible through the `0x400000` bit test, which no section declares — so the rule as written is not the rule that produced the number.

Downstream: AC2 requires at least one `native` row with `msys_pid is None` and is satisfied by the ~4 unoverlaid rows, so a rule that inverts ~300 rows passes. AC11 then probes every row with `kill -0` on a synthetic id that addresses nothing (and see D40 — that arm grades nothing anyway). Unit 1 §3's hands-off line still hands `kind` to unit 4 "for the signal choice" even though unit 4 §4 makes the choice operationally, so the two specs disagree about what the field is for while the field itself is measurably inverted.

**Fix.** State the discriminator in S3: a `ps -W` PID carrying the `0x400000` bit is a SYNTHETIC id for a non-cygwin process and yields `kind = 'native'` with `msys_pid = None`; only a PID without the bit is a real MSYS id. Have AC2 assert the split reproduces the fixture's shape — native is the MAJORITY, and a run grading fewer than half the rows native reds — rather than "at least one of each". Resolve the `kind` contract with unit 4 in one line: unit 4 chooses the signal operationally, and `kind` is the census's own classification, not the reaper's input.

**Left-shift gate.** Population-shape assertions instead of existence assertions, as a spec-review rule with teeth: any criterion whose subject is a partition of a measured population must assert the partition's SHAPE against the measurement, not the non-emptiness of each part. "At least one of each" is the could-not-fail idiom this build has now produced in AC2, AC3 and AC1; a grep for that phrasing across the seven §6 sections is a five-minute check.

### D34 — BLOCKER — unit 2 §2 S2 and S4 and §4 "The self fence", against unit 7 S4/AC5 and unit 4 AC5/AC6

*Raw ids 2, 20, 52. New at rev-3: the self fence is D9/D17's repair.*

S2 forbids a `self_chain` row from being a root; S4 excludes rows reached only through the chain. `self_chain` is the caller plus all its ancestors over the union graph. When the tool is invoked from inside the tree it must reap — which is every real invocation — the genuine root IS in the chain: the shell whose argv names the absolute repo path is an ancestor of the invoked `scope.py`. Every path to the runner runs through the self chain, no non-chain row admits it, and the in-scope set is empty.

The consequences reach three units. Unit 7 S4's third detection condition (`scope.py --explain $$` answers IN SCOPE for the runner) can never hold, because the probe is the runner's own child, so S2's delegation and AC5 are unreachable — and S4's stated rationale, "the runner is the walk root's ancestor, so if it is in scope every leg it dispatches is too", is exactly inverted: being the caller's ancestor is what guarantees exclusion. Unit 4's live arms (AC1, AC5, AC6) stage trees under the calling test process and fall under the same exclusion. Unit 2's own AC4 names the failure state from the other side ("would exclude everything the session started") and its positive half needs a fixture that plants a second root outside the chain, so it goes green while every live sweep resolves to nothing.

**Fix.** Split "ours" from "never a kill target". Delete `and it is not in self_chain` from S2, so a self-chain row that matches a declared root is still a root. Restate S4 as: self-chain rows are IN SCOPE, are never kill targets, and are never walk roots — unit 4 S3 already enforces the second half. Add a criterion that runs `derive_scope` with `self_chain` set to the real ancestry of the calling process over the frozen corpus and asserts a non-empty in-scope set, plus one asserting a leg spawned by the caller's own ancestor is in scope while the ancestor itself is not killable. Re-point unit 7 S4 at that criterion.

**Left-shift gate.** One arm, and it is the one this whole build needs: `derive_scope` invoked the way the product invokes it — from a process whose ancestry is the real session — must return a non-empty set on this node's live census, or red. Every fence defect in three rounds has been invisible because the fence was only ever exercised over planted fixtures. A liveness assertion on the fence itself is §7's "a probe that cannot move says so" applied to the one component whose failure mode is silent success.

### D35 — BLOCKER — unit 7 §6 AC4 and AC5, against S4 and §4 "Detection, at profile time"

*Raw ids 6, 23, 36, 57. New at rev-3: D20's repair reached S4 and §4, not the criteria.*

rev-3 moved the profile-time probe off the scratch path onto the runner's own process (`scope.py --explain $$`) and §4 now states flatly that "no scratch root is declared, by this unit or any other" — unit 6 §4 and AC8 forbid `PROCMON_ROOTS` from naming an ancestor of the temp root, and the scratch dir is a bare `mktemp -d` under it. AC4 and AC5 were not re-read. AC4 still grades "when `PROCMON_ROOTS` does not admit the runner's scratch parent", AC5 still grades "admits the scratch parent", and the arm is still named `test_unadmitted_scratch_root_is_announced_before_dispatch`; §7's staging list still carries "a monitor whose roots exclude the scratch parent".

So AC4's precondition is now permanently true by design, making it assert that the runner ALWAYS announces the fallback, which contradicts S2's delegation; and AC5's precondition is permanently false, so the delegated kill path — the highest-risk change in the build — is graded by no criterion at all. The rev-3 revision log lists S1, S4, §3, §4 and AC7 as revised and does not mention AC4 or AC5. This is the round's headline pattern in its purest form, occurring inside the unit that carried D20.

**Fix.** Rewrite AC4 as: when `scope.py --explain` does not admit the RUNNER'S OWN process, the fallback is announced with the profile line before any leg is dispatched and no leg reds. Rewrite AC5 as: when it DOES admit the runner's own process, the signal path's kill goes through `run_kill` and the staged grandchild is verified dead by re-read. Rename both arms off `scratch_root`, and fix §7's staging list.

**Left-shift gate.** A revision-log completeness check, run as part of every fold: for each section a revision touches, every criterion that cites that section by number, and every criterion whose text contains a noun the revision deleted from the spec, must appear in the revision log's touched list or be explicitly waived in it. "Scratch" was deleted from S4 and §4 and left standing in AC4, AC5 and §7 — a grep for deleted nouns against the unchanged half of the same file is mechanical and would have caught it in seconds.

### D36 — BLOCKER — unit 6 §6 AC8 second conjunct, against unit 2 S7 and unit 6 §3

*Raw ids 5, 22, 37, 58. New at rev-3: round 2's own suggested fix, folded literally.*

AC8's second conjunct requires `scope.py --check-path` to answer ADMITTED for the repository root. Grepped across the whole build, `--check-path` occurs in exactly two places: this criterion, and round 2's suggested fix text. Unit 2 declares one diagnostic verb — `--explain <winpid>` in S7, graded by AC10 — and unit 7 rev-3 deleted its path-mode probe precisely because path mode "grades the wrong thing" (D20). So the criterion names a mode no unit ships.

Worse, it is an order violation of the exact class rev-2 spent a repair closing. Unit 6 is order 1; its §3 says it must land green WITHOUT any engine file, and AC1/AC7 assert selfcheck green with no engine present. `scope.py` arrives at order 3. AC8 is observed by this unit's own `adopt-process-monitor.test.sh`, which is on its own gate list — so the arm reds on every bar from order 1 until order 3. That is D1's shape, reintroduced by the repair for D16, and it half-grades the temp-root prohibition that §8 F1 makes the `reap-orphans` default conditional on.

**Fix.** Split AC8. Keep the temp-root prohibition as a pure text assertion over the shipped conf, gradable at order 1: no `PROCMON_ROOTS` entry is an ancestor of the resolved system temp directory. Move "the declared roots actually admit this repo's own work" into unit 2 as an arm over `derive_scope` with the shipped conf against the frozen corpus, where both the census and the closure exist. Delete the `--check-path` reference, or add that mode to unit 2 S7 with its own criterion and give the moved conjunct to a unit at order 3 or later.

**Left-shift gate.** Build the check round 2 already specified and nobody wrote: every path and command named in a criterion's observer must be shipped by a unit whose `order` is no greater than the citing unit's. It is a path-existence check over the parsed set with no semantics, it catches D1, D16's backwards edge, D23 and this, and its absence is now directly responsible for a blocker in two consecutive rounds.

### D37 — BLOCKER — unit 2 §2 S3 and §4 "The closure", with unit 4 §4 "The walk"

*Raw id 18. New at rev-3: D22's repair, unioned without the translation.*

The closure is specified over "the UNION of the census's two parent graphs" and unit 4 spells it "a child map from `win_ppid ∪ msys_ppid`". But `msys_ppid` holds MSYS ids and the map is keyed on `winpid`, and no spec in the set names the translation. The union-graph record performs the join silently, in a table header: "MSYS parent, as a winpid".

Untranslated, the union is a namespace error at the heart of a build whose entire premise is that these two id spaces must not be confused. Every MSYS edge resolves to no row, the union degenerates to the Windows graph alone, D22's repair is inert, and the seven measured rows where the graphs disagree lose their MSYS parent. Where a small MSYS id collides with a live `winpid`, the opposite happens and an unrelated process is adopted into an in-scope tree, dragging its subtree into the kill set. Unit 2 AC3's fixture chain is reachable over Windows edges, so no criterion fails in either direction.

**Fix.** State in S3, and mirror in unit 4 §4, that `msys_ppid` is mapped to a `winpid` through the census's own `msys_pid`→`winpid` join before the union; that an `msys_ppid` with no such mapping contributes NO edge and is counted; and that raw MSYS ids are never looked up in the `winpid`-keyed map. Add an arm over a fixture where the MSYS parent and the Windows parent differ and only the MSYS edge reaches the child.

**Left-shift gate.** Namespace typing in the data model, enforced by a name convention the specs already half-use: every id-valued field carries its namespace in its name (`winpid`, `win_ppid`, `msys_pid`, `msys_ppid`), so a lint over the spec text can red any set operation, dict lookup or comparison whose two operands carry different namespace prefixes. `win_ppid ∪ msys_ppid` reds on sight. This is the cheapest possible guard against the bug class this entire kit exists to fix, and it works on the prose before it works on the code.

### D38 — BLOCKER — unit 2 §2 S3 and §4 "The closure, and why it is the whole fence"

*Raw id 19. New at rev-3: the closure is new at rev-3.*

Both the descendant closure (S3) and the `self_chain` ancestor walk (§4) are specified over the union graph with no visited-set and no termination statement. The union-graph record this same section cites measures a cycle on this node's real table and states plainly that a depth-unbounded walk over it without a visited-set does not terminate, calling the guard "load-bearing on this host, not defensive programming". Unit 4 §8 F3 carries that guarantee in writing for its walk. Unit 2 carries none, and §5's "one graph walk; linear in the table" asserts a cost property the graph does not support in place of the guard it needs.

So `derive_scope` — the safety unit every other unit's kill authority rests on — can hang on measured live input, and the same graph is walked twice under two different termination contracts.

**Fix.** Add the visited-set to S3 and §4 explicitly, matching unit 4 §8 F3's wording. Cite the measured cycle. Count cycle-broken edges alongside the start-time dropped-edge count, so a graph that is cyclic today is visible in the output rather than inferred from a hang. Add an AC staging a two-row cycle in the fixture and asserting the closure RETURNS.

**Left-shift gate.** Every walk in the set declares its termination guarantee in its own scope item, and a spec-lint reds a §2 item whose verb is "walks" or "closes over" with no visited-set or depth bound in the same item. Unit 4 had it and unit 2 did not, which is what happens when a guarantee lives in one unit's prose instead of in the format.

### D39 — BLOCKER — unit 7 §2 S1 and S2

*Raw id 35. Not new: pre-existing since rev-2's delegation.*

S1 reaps "the recorded leg pids" through unit 4's `run_kill(winpid, …)`. `run-gates.sh:1277-1280` records each leg as `printf '%s' "$BASHPID" > "$WORK/$i.pid"` — an MSYS id, fed elsewhere to `scan_descendants` over `ps -ef`, which unit 4 §10 itself describes as "purely in MSYS ids". Unit 1 measures `PID != WINPID` on all 321 rows. Neither unit 7 nor unit 4 declares the `msys_pid`→`winpid` lookup the census makes available.

The outcome is silent either way. Usually the recorded id is not a key in the `winpid`-keyed census, so the walk root is not in `scope_set` and unit 4 AC8 refuses before walking — the interrupt leak this entire unit exists to close stays open, behind a path the runner announces as "delegated". Where the small MSYS integer collides with a live Windows pid, `run_kill` walks and kills an unrelated subtree. AC8's refusal makes the first outcome look like correct behaviour, and D35 means the one criterion that would have caught it cannot be staged.

**Fix.** State in S2 that recorded leg pids are translated to winpids through the census's `msys_pid`→`winpid` join before `run_kill` is called, and that a leg pid with no census row is reported unresolvable rather than passed through. Add to AC5 that the winpid handed to `run_kill` is the census's winpid for the recorded leg, not the recorded number.

**Left-shift gate.** The same namespace-prefix lint as D37, extended one step into the runner: any value read from a `*.pid` file written by bash is MSYS-namespaced by construction, and passing it to a parameter named `winpid` reds. Cheaper still, and worth doing at code time: `run_kill` asserts its argument is a key in the census it was handed, and reports "unresolvable id, wrong namespace?" rather than the same refusal it gives an out-of-scope root — two failure modes that currently print the same thing.

## Highs

### D40 — HIGH — unit 1 §6 AC11

*Raw ids 8, 25, 54. New at rev-3: round 2's left-shift text, folded verbatim.*

AC11 puts "every row of the frozen fixture" to a live liveness probe — `kill -0 <msys_pid>`, a CIM presence check on `winpid` — and requires every row to answer. §4 Files touched pins the fixture as `tools/process-monitor/fixtures/census-node-a.tsv`, captured from this node and committed, so by the time the arm runs every one of those processes is dead.

Both readings fail. Under the liveness reading — which is the build's own vocabulary, since unit 4 §4 uses "answering" to mean the probe SUCCEEDS — the arm cannot pass on a correct implementation. Under the weaker "the probe returned a determinate answer" reading it cannot fail on a broken one, because a dead row and an unaddressable live row both answer `No such process`, which is exactly the distinction the criterion was adopted to draw. On a machine that has recycled those pids, some rows answer for unrelated live processes and the arm goes green on a false join. And unit 4 §4 anchors its per-row signal rule to this criterion by name, so a criterion that grades nothing is load-bearing on the repair for D21.

**Fix.** Re-target AC11 at a LIVE census read on this node, skipped with a named printed reason off Windows as AC2 already does: every row present in the live read answers the probe its own `kind` implies, and the count of non-answering rows is reported. Tolerate a row dying between the scan and the probe by re-reading that row once, so the arm is not flaky by construction. Keep the frozen fixture for the parsing arms, where deadness is irrelevant.

**Left-shift gate.** A fixture-freshness rule in the spec format: any criterion whose observation is a LIVE property (a probe, a signal, a clock) must name a live subject, and a criterion naming a committed fixture may only assert structural properties. One grep over §6 for the fixture's filename crossed against a verb list catches it, and it generalises to every future arm in this kit, which is going to be full of both kinds.

### D41 — HIGH — unit 4 §2 S4, §3 "No single signal", §4 signal table, §8 F4, AC10

*Raw ids 27, 48, 56. Partly new at rev-3: D21's repair pinned the prose spelling.*

The native kill is pinned as the literal `taskkill //PID <winpid> //F`. The doubled slash is MSYS argument-mangling protection and means nothing to `taskkill` itself. Unit 4 §3 rules out `os.kill` because the interpreter is native `win32` python, S4 speaks of resolving a signal binary per row, and unit 1 §5 pins a fixed argv with no shell — so `taskkill.exe` receives `//PID` verbatim. Verified on this node: `taskkill //PID 999999 //F` returns rc 1 with `ERROR: Invalid argument/option - '//PID'`, while `/PID` reaches the pid lookup and returns "process not found". Both build records' measured arms used the single slash (`taskkill /PID 46376 /F`, `taskkill /PID <winpid> /T /F`); only their prose conclusions carry `//`, written for a bash-issued command, and the spec propagated the prose.

So the one signal that reaches the non-MSYS population — the whole rationale for D21 — fails at every call site, and AC10 asserts BOTH that the target is dead by re-read AND that `taskkill //PID` was the signal used. Those cannot both hold: the literal implementation reds the death assertion, the working implementation reds the argv assertion. Meanwhile §7's namespace-ban leg spells the sibling switch `/T` with one slash, so the spec is not even internally consistent about it.

**Fix.** Spell `/PID` and `/F` in S4, §3, the §4 table and AC10; state that the invocation is a list argv through `subprocess` with no shell; have AC10 assert the argv the child actually received. Add one sentence recording that a bash-issued equivalent needs `//` and the python one must not, or the next reader will "correct" it back.

**Left-shift gate.** Two things, both cheap. At spec time: any command literal in a spec carries the context it was measured in, and a literal measured at a shell prompt may not be pinned as an exec'd argv without a re-measurement. At code time: the reaper asserts a non-zero exit from a signal binary is classified — invalid-argument, access-denied and no-such-process are three different outcomes and today all three would be reported as "survivor", which is D21's failure mode with a different cause.

### D42 — HIGH — unit 7 §2 S4 and §4 condition 3, against unit 2 S7 and AC10

*Raw ids 24, 46. New at rev-3: D20's repair introduced the probe.*

S4 pins the profile-time probe as `scope.py --explain $$`, run from the runner's MSYS bash, where `$$` is an MSYS pid. Unit 2 S7 and AC10 both spell the argument `<winpid>`, and `scope_set` is a set of winpids. Unit 1 §4 goes out of its way to establish the two as different ids.

A literal implementation looks a small MSYS integer up in a winpid-keyed set and answers NOT IN SCOPE every time — a detection probe with one possible answer, which is the reassuring-zero class on the path this unit exists to fix. On a collision with a live winpid it answers about an unrelated process, which is a false admit at the one probe that gates the kill path. This is distinct from D34: repairing the fence does not repair the namespace, and repairing the namespace does not repair the fence. Both must land or the probe is still wrong.

**Fix.** Pass a winpid. Either give `scope.py --explain` a documented `--msys-pid` form that joins through the census's own `msys_pid` column, or resolve the runner's winpid before the probe and pass that. Say which in §4 condition 3, grade it in the rewritten AC4, and state the namespace explicitly in unit 2 S7 — the caller is a shell and `$$` is the obvious thing to type, so the interface should refuse it loudly rather than answer wrongly.

**Left-shift gate.** `scope.py --explain` refuses an argument that is not a key in the census it just read, with a message naming the namespace it expected, instead of answering NOT IN SCOPE. Any diagnostic verb whose "no" is indistinguishable from "I could not look this up" is a probe that cannot move; this one gates a kill path.

## Mediums

### D43 — MEDIUM — unit 4 §2 S1 and §4 "The walk"

*Raw id 10. New at rev-3: corroboration is new at rev-3, in unit 2 only.*

The reaper builds its own child map from `win_ppid ∪ msys_ppid` with no mention of unit 2's start-time edge corroboration, so the edges unit 2 dropped are live again inside the kill walk, and no criterion compares the two graphs. The membership test bounds the damage to in-scope rows but does not eliminate it: a row admitted by root A, attached to target T through an edge unit 2 refused to trust, passes `winpid in scope_set` and is killed as T's descendant. Unit 4 §4's sentence about members dropped "whose edge failed corroboration" only catches rows that were never in scope at all. AC1 grades set size against a fixture that stages no bad edge, so the divergence is ungraded in both directions.

**Fix.** Say in S1 that the walk uses the SAME corroborated edge set unit 2 computed — returned alongside the scope set, not recomputed — and add a criterion staging an uncorroborated edge between two in-scope rows, asserting the child is not in the walked set.

**Left-shift gate.** The graph is derived once and passed, never re-derived. As a rule it is §5's "derive over author" one layer down; as a check it is an assertion that `reap.py` contains no second construction of a child map, which is one grep over the eventual source and one sentence in the spec that makes the grep meaningful.

### D44 — MEDIUM — unit 3 §4 "PARENTLESS", against unit 2 §4 start-time paragraph

*Raw id 61. New at rev-3: both halves are new at rev-3.*

Unit 2 drops a parent edge from the closure when the child predates its claimed parent, gated by AC9, on the explicit rationale that a recycled or stale parent edge must not smuggle a row in. Unit 3 defines `PARENTLESS` as "`win_ppid` names no row in this census" and trusts the same edge on the id alone. One graph, two validity rules, both written in the same revision.

A genuine orphan whose dead parent's pid has been recycled onto a live process is in scope when its own argv makes it a root, and then grades not-`ORPHAN` — the 52-to-61-hour dead-parent class this build was opened over, silently exempt from the default mode. It also lets `--explain` and `--report` tell an operator opposite stories about one row.

**Fix.** State `PARENTLESS` as: `win_ppid` names no census row, OR it names a row that started AFTER this one. That is the corroboration unit 2 already defines, cited rather than restated. Add an arm staging a flagged row whose `win_ppid` names a younger live row and asserting `ORPHAN`.

**Left-shift gate.** The same field-provenance lint as D32, plus its sibling: a predicate over an edge must cite the edge-validity rule it uses by section, and two units citing different rules for the same edge reds. Both of this round's graph-consistency defects (this and D43) are one unit reasoning about an edge without reference to the unit that owns edge validity.

### D45 — MEDIUM — unit 5 §2 S4, §4 "Files touched", AC5 and AC9

*Raw ids 49, 59. Partly new at rev-3: D23's repair folded the `kit.toml` half only.*

Verified against the live tooling. `tools/settings-merge.py` wires a non-default hook only from a `--fragment` JSON declaring `{name, event, matcher, marker, hook_path}`, one fragment per event, and `tools/check-hook-destinations.sh:27` derives its entire population from `git ls-files "*.fragment.json"`. Unit 5 needs two entries (PostToolUse `Bash|PowerShell`, and SessionStart) and declares no fragment file at all — so the entries cannot be merged and the `hook destinations` leg AC9 claims to turn green never sees this hook.

Separately, §4 Files touched names only `procmon-hook.js` and `.claude/settings.json`, while S4 says in bold that this unit adds the hook's `[[files]]` row and destination to `kit.toml`, and AC5's arm lives in `adopt-process-monitor.test.sh` — both unit 6 files. A `kit.toml` edit drags the `kit version markers` obligation on `KIT_PROCESS_MONITOR_VERSION` in `adopt-process-monitor.sh` (unit 6 S1, AC7), which no section of unit 5 names. And unit 6 §7's arm list does not contain `test_wiring_is_idempotent`, so AC5's arm is owned by nobody. "Estimate" in the heading does not cover a file the unit's own scope item mandates editing, and this list is what the order-6 disjointness argument against unit 7 rests on.

**Fix.** Add `tools/process-monitor/procmon-hook.fragment.json` (PostToolUse, matcher `Bash|PowerShell`) and the SessionStart declaration to S4 and to Files touched; state in S5 how the hook is told which form it is running (argv from the fragment). List `kit.toml`, `adopt-process-monitor.sh` and `adopt-process-monitor.test.sh` as edited, and state that touching the adopter bumps `KIT_PROCESS_MONITOR_VERSION` and re-stamps its carriers. Add `test_wiring_is_idempotent` to unit 6 §7's arm list, or move the criterion.

**Left-shift gate.** A Files-touched completeness lint: every file named in a unit's §2 items or in a criterion's observer must appear in that unit's Files touched, and every arm named by a criterion must appear in some unit's §7 arm list. Both halves are set operations over parsed sections. The second half is the orphaned-criterion check round 2 already proposed as the join-lint; this round supplies its third instance.

### D46 — MEDIUM — unit 5 §6 AC2

*Raw id 14. Not new: pre-existing, unreached by rounds 1 and 2.*

AC2's observation — the second run exits 0, prints nothing, runs no census — holds identically whether the stamp is written BEFORE the work or after it, which is precisely the failure its own Red-when names: a crashing hook that throttles itself out of running. No sibling criterion covers the ordering either; AC3 asserts the early-exit path spawns nothing and AC7 grades fail-open on a raising census, and neither inspects when the stamp is written. So the kit's only liveness protection for the hook is prose.

One correction to the Red-when's wording while it is being edited: "out of ever running again" overstates the hazard, since a stamp older than `PROCMON_THROTTLE_S` stops suppressing. The defect is real; the consequence is a throttle window of silence, not permanence.

**Fix.** Add the observation that makes the ordering visible: stage a census that RAISES, then assert the next run is NOT throttled — the stamp is absent or unchanged after a failed run. Keep AC2 for the happy path.

**Left-shift gate.** The generalisation this build keeps needing: for every criterion, name the defective implementation it distinguishes from the correct one. A criterion whose observation is identical under both is a documented gap, not a check. It is a review question rather than a script, but it is the single question that would have caught seven of this round's sixteen defects, and it belongs in the spec template beside "Red when".

### D47 — MEDIUM — unit 7 §7 "New arm", the ARMS_FLOORS sentence

*Raw id 62. Not new: D27, repaired by deleting the falsifiable half.*

The rev-3 rewrite deleted the number and kept the false claim. Verified against both sources: `.memory-tree.conf:419` holds exactly seven `ARMS_FLOORS` pairs and no `run-gates` row, and `check-arms.py`'s `HELPER_RE` (`^\s*fail\(\)\s*\{`) matches nothing in `run-gates.sh`, so that file is not in the discovered population at all. The sentence claims this suite carries an assertion floor that "MOVES with these arms"; both clauses are false, and a builder who adds the row trips `check-arms.py:279` with "ARMS_FLOORS names <gate>, which is NOT in the discovered population".

The highest-risk unit in the build is therefore shipping its new arms behind a ratchet that cannot exist. D27 stated this with the same verification and named the fix; the repair removed the falsifiable half and left the false one, which is a smaller version of the round's whole pattern.

**Fix.** Replace the sentence with what is true — this suite is behind no arms floor, because `run-gates.sh` does not use the `fail() {` helper protocol `check-arms` discovers — and name the compensating check. Or scope adopting that protocol in `run-gates.sh` and add the pair, read from `check-arms.py --report`, in the same commit.

**Left-shift gate.** Any spec sentence claiming a gate covers a file must name the file and the gate, and a lint resolves the pair against that gate's own discovered population. `check-arms.py --report` already prints the population; the check is one comparison. This is §7's "no count of a derived population is written in prose", applied to a claim of coverage rather than to a number.

---

## The gate this record would actually build

Seven of the sixteen defects above are one class: **a criterion whose observation is identical under the correct implementation and under the defect it names**. D32, D33, D34, D35, D37, D40, D43, D46 all carry it in some form. Rounds 1 and 2 found it as D4, D10, D17 and D25. Twelve instances across three rounds, in six of the seven units.

The gate is not a script, and pretending otherwise is why it has not been built. It is one required field in the spec format, beside "Red when": **"Distinguishes"** — name the defective implementation this criterion separates from the correct one, and say what the two do differently at the observation point. A criterion that cannot fill it is a documented gap rather than a check, and writing that sentence is what surfaces "AC2 is true either way", "AC11 cannot pass", "AC4's precondition is permanently true". It costs one line per criterion and it is the only thing in this record that addresses the class rather than its instances.

Three cheap mechanical checks should land with it, all of them over parsed spec sections, none needing semantics:

1. **Order-of-observers.** Every path and command named in a criterion's observer is shipped by a unit whose `order` is no greater than the citing unit's. Round 2 proposed it; not building it cost a blocker this round (D36).
2. **Field provenance.** Every field named in a unit's §4 predicates appears in that unit's §3 `consumes-from` list. Catches D32 and D44 at authoring time.
3. **Namespace prefixes.** Every id-valued field name carries its namespace, and any set operation, lookup or comparison whose operands carry different prefixes reds. Catches D37 and D39 — the two defects where this build reintroduced, inside its own repair, the exact bug class it exists to fix.

And one process rule, because the repair-induced ratio has now been 8/16 and 10/16 in consecutive rounds: **a repair is not folded until every consumer of the changed text has been re-read.** The revision log already lists what a fold touched. Cross that list against every criterion citing those sections and every occurrence of a noun the fold deleted, and D35, D36 and D40 all fall out mechanically — three of this round's eight blockers, from one grep.
