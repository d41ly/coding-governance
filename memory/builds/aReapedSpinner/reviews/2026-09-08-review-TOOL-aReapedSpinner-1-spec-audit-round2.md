**Serves:** spec-audit TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7

# aReapedSpinner — Tier-2 spec audit, round 2

*Adversarial pre-code pass over the seven-unit spec set for `tools/process-monitor/`, at rev-2. Node `a`, 2026-09-08, base `e2b82a53`. Findings are pre-code: nothing here is a bug in shipped software, every one is a defect in a document that would become one. Round 1's fifteen defects were all repaired before this pass; this round's job was the repairs.*

**Range — ROUND 2**, seven subjects pinned at these blobs: `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-1.md@7dedc8f0f20fd122072dee24bb3ce489ed866aee`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-2.md@097547c41904bfae37652fe83c925a77973dbcab`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-3.md@b593737338a64cdfe9602249c81a0a6bf29150fa`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-4.md@d83a66d7407d10377d9b7b4c3cab63efb7d04413`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-5.md@0c740c5bc2afc4fcd9acb2d9163022f0a01f25c4`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-6.md@b79df3f30dc8490b9010cb5ab35f5bd1330abca3`, `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-7.md@22ee10ee5ef69f7a4151a53c82bacc751bd75703`.

## Verdict: BLOCKED

Five blockers, and **eight of the sixteen defects below were created or left standing by a round-1 repair**. That is the headline: this set is not drifting toward green, it is trading defects. The repair that closes D11's substring hole writes a safety rule (unit 6 §4) that the very same unit's S3 forbids obeying, so the one conf value the whole safety property rests on cannot be written at all. The repair that closes D9's all-or-nothing fence overshoots into a per-member check that can never refuse. The repair that closes D15's predicate disagreement folds `ppid 0` into "parentless" on the strength of a measurement that says the opposite, and the kit's DEFAULT mode then kills live-parented in-scope processes. The build is still not ready to dispatch its first pass. Every fix below is a spec edit; no unit needs re-scoping, but unit 7 now owes a one-line change to `run-gates.sh` that three separate defects are waiting on.

### Review shape

Raw 45 · confirmed 21 · refuted 24 · unverified 0 · precision 0.47.

**Run integrity — all clean.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline. No arm of this run failed to report, so the zero counts here are evidence rather than an absence of evidence, and the finding set is complete as far as four lenses reach. This run is complete.

**Consolidation, and how the sixteen rows relate to the 21.** The pipeline discarded no duplicates, but the 21 confirmed findings describe **16 distinct defects**: four lenses landed on the `PROCMON_ROOTS` contradiction from four different sides, two on the vacuous inheritance clause, two on the missing hook fragment. Each row carries its raw ids so nothing is lost. Severities are the ones adjudicated HERE; a merged defect takes the maximum severity in its cluster, which promoted raw 29 (HIGH) into D16 and raw 16 (HIGH) into D17. Adjudicated totals across the 16 rows: **5 blockers, 6 highs, 5 mediums, 0 lows.**

| # | Sev | Unit | Address | Defect | Raw ids | New at rev-2? |
|---|-----|------|---------|--------|---------|---------------|
| D16 | BLOCKER | 6, 7 | 6 §2 S3 vs §4 "WHAT … MAY NOT CONTAIN", 6 AC2, 7 S4/AC4 | `PROCMON_ROOTS` must contain the scratch parent and must not contain the temp root — on this node they are one directory, and AC2 grades neither rule | 1, 14, 36, 29 | yes — §4 is D11's repair |
| D17 | BLOCKER | 4 | §2 S3 and §4 "Descendant inheritance", AC4 | Inheritance inside the walked set admits every member unconditionally; the per-member fence re-check can never refuse | 27, 16 | yes — D9's repair overshot |
| D18 | BLOCKER | 3 | §4 "The ORPHAN predicate, stated ONCE", AC4/AC5 | `ppid 0` folded into "parentless" against the measurement that produced it; the default mode reaps live-parented in-scope rows | 13 | yes — D15 + D11 combined |
| D19 | BLOCKER | 2 | §4 "What is matched, and what is NOT" (env-assignment sentence), AC8 | The env-assignment carve-out does not describe the input it was written for, and AC8 cannot be staged from the snapshot it pins | 26 | yes — D11's repair is incomplete |
| D20 | BLOCKER | 7, 4 | 7 §2 S2/S4, 7 AC5, against 4 AC8 | The delegated kill's walk root is a leg shell whose argv is a relative script path, so unit 4 AC8 refuses every delegated `run_kill` | 28 | yes — D6's repair claims this path is closed |
| D21 | HIGH | 1, 4 | 1 §4 "Data model" and S2, against 4 S4 | `pid` is not one namespace: the MSYS `kill` binary cannot reach the non-MSYS rows, and the six-field row contract carries no flag | 20 | partly — D8's repair named the binary, not the split |
| D22 | HIGH | 4 | §4 "The walk", AC1 | The child map's edges are MSYS-only, so the descendant closure structurally excludes native Windows children; AC1's fixture is all-MSYS | 30 | no — pre-existing, unreached by round 1 |
| D23 | HIGH | 5, 6 | 5 §2 S4 and §4 Files touched, 5 AC5/AC6 | The hook needs `*.fragment.json` files; neither unit's scope, Edges or file list contains one, and the destination lands five units before the file | 18, 39 | no — D1's class, repaired as an instance |
| D24 | HIGH | 7 | §2 S1 and §4 "Where it hooks in" | An unbounded reap is inserted ahead of `ts_release; ts_drop_ticket`, and no criterion asserts the beacon and ticket still release | 41 | no |
| D25 | HIGH | 4 | §2 S5 against §6 | The sweep's five counts are graded by no criterion and carry no `figure: DERIVED` marker | 4 | yes — D5's migration dropped the guard |
| D26 | HIGH | 6 | §6 AC5, against §7 | "that probe has been RUN and observed to exit non-zero" is attributed to `govkit selfcheck`, which only sees the declaration | 19 | yes — D2's shape, re-introduced next door |
| D27 | MEDIUM | 7 | §7 "New arm", the ARMS_FLOORS sentence | The claimed assertion floor does not exist and cannot: `run-gates.sh` is not in check-arms' discovered population | 44 | no |
| D28 | MEDIUM | 5 | §2 S2 vs §4 "The throttle check itself must be cheap", AC3 | The early path needs a conf key the same section forbids it from reading, and AC3 cannot observe the half it names | 45 | no |
| D29 | MEDIUM | 1 | §2 S9 against AC10 | S9 declares two partial-row classes and requires both counts; AC10 grades the wrong two | 22 | no — D3's class, in unit 1 |
| D30 | MEDIUM | 7, 4 | 7 §2 S2 and §5 perf/scale | Unit 4 offers only per-pid entry points, so a teardown pays a python start and two censuses per recorded leg pid | 33 | no |
| D31 | MEDIUM | 6 | §2 S5 → AC4 | S5 cites AC4, which grades a descriptor concern; AC4 is now declared by no scope item at all | 9 | yes — D2's split left the join behind |

---

## The four questions this round was sent to answer

**1. What did the round-1 repairs introduce?** Eight of the sixteen. D16, D17, D18, D19, D20, D25, D26 and D31 exist because of a rev-2 edit, and they are not cosmetic: three of them are blockers and one (D16) makes a required conf value unwritable. The pattern is consistent enough to name — each repair was applied where the round-1 finding pointed, and none of them was re-checked against the sections that consume it. D11 was repaired in unit 2 §4 and its new safety rule was never reconciled with unit 6 S3 (D16) or with the ORPHAN predicate that now inherits its wider admission (D18). D5's figure was moved from unit 3 to unit 4 without the `figure: DERIVED` guard that made it gradeable (D25). D2's AC was split and S5's citation was left pointing at both halves (D31). This is the repair-in-place-without-re-reading-the-consumers class, and it is worth a fold rule rather than sixteen more findings.

**2. Is the ordering now satisfiable end to end?** On the DECLARED edges, yes. Unit 6 is `order 1` and consumes only external; unit 1 `order 2` consumes 6; unit 2 `order 3` consumes 1 and 6; unit 3 `order 4` consumes 1, 2 and 6; unit 4 `order 5` consumes 1, 2, 3 and 6; units 5 and 7 share `order 6` and neither consumes the other. The graph is acyclic and every `consumes-from` points strictly backwards. D5 is closed.

But **two UNDECLARED edges point forwards**, and both are load-bearing. Unit 6 at `order 1` must write a `PROCMON_ROOTS` naming a scratch parent that only unit 7 (`order 6`) can create (D16), and unit 6's adopter is assigned a hook destination that only unit 5 (`order 6`) ships (D23). Neither appears in either unit's Edges. So the honest answer is: the ordering is satisfiable as declared and *not* satisfiable as specified, because two units at `order 1` and `order 6` depend on each other in the direction the order forbids. Both fixes below name the edge that has to be declared.

**3. Does unit 4's descendant inheritance re-open the hole unit 2 AC8 closes?** Yes, and the question turns out to be generous — AC8 does not close a hole in the first place. D19 shows AC8's precondition ("a row whose ONLY occurrence of a declared root is inside an environment assignment") cannot be staged from the real snapshot it pins, because in all nine live rows carrying `export TEMP=` the temp root also appears as a genuine path-shaped argument. So unit 2's carve-out is untested by construction. D17 then removes the second opinion: after the root is admitted standalone, inheritance admits every walked member, so nothing in the reaper consults the fence again. The blast radius is whatever the census's `ppid` edges say — and D18 and D22 both record that those edges are wrong for the majority population on this host. Three defects, one compound hazard: a fence whose carve-out is unstaged, a re-check that cannot refuse, and an edge graph that mis-parents 300-odd rows.

**4. Criteria that still cannot fail.** Six, on top of the two round 1 found. AC4 in unit 4 (D17 — passable only by injecting a member the walk cannot construct). AC5's second conjunct in unit 6 (D26 — no observer). Unit 4's five sweep counts (D25 — no criterion at all). AC3's stated red in unit 5 (D28 — half of it is unobservable by the arm). AC1 in unit 4 (D22 — the fixture is entirely MSYS, so the class the kit exists for is never touched). And the inverse in unit 2's AC8 (D19 — a criterion that cannot PASS is as useless as one that cannot fail, and it will be weakened by whoever hits it). §7's "a new gate is not landed until its failing case has been observed" is the rule; five of these six are it, stated in a spec.

**Round-1 defects NOT re-reported.** D1, D3, D4, D5, D7, D10, D12, D13 and D14 drew no confirmed finding this round; as far as four lenses reached, their repairs hold. Two are repaired but INCOMPLETE and appear below under new numbers rather than as re-reports: **D8** (the signal's namespace was named as the MSYS `kill` binary, which is right and insufficient — the census carries two namespaces and nothing tells them apart, D21) and **D11** (substring containment became program-path matching, which is right and does not cover its own measured input, D19). **D9's** repair overshot rather than fell short (D17). **D6's** repair made the profile-time announcement reachable but the delegated path it announces refuses in production (D20). **D2's** and **D3's** instances are closed and their class recurs at D26, D31 and D29 — three more instances of "the criterion and the scope item that declares it disagree", which is now the single most common shape in this set and the strongest candidate for the left-shift gate at the bottom of this record.

---

## Blockers

### D16 — BLOCKER — unit 6 §2 S3 against §4 "WHAT THIS REPO'S OWN PROCMON_ROOTS MAY NOT CONTAIN", with unit 6 AC2 and unit 7 S4/§4/AC4

*Raw ids 1, 14, 36, 29 — four lenses, one defect.*

S3 requires `.process-monitor.conf` to hold "the scope roots INCLUDING the gate runner's scratch parent". §4, new at rev-2 as D11's repair, forbids this repo's `PROCMON_ROOTS` from naming the shared temp root, as a safety rule rather than a preference. **On this node those are the same directory.** `tools/run-gates/run-gates.sh:940` is a bare `WORK=$(mktemp -d)` with no `-p` and no `TMPDIR` override anywhere in the file — `grep -n TMPDIR tools/run-gates/run-gates.sh` returns nothing — so `$WORK` sits directly under the ambient temp root. `mktemp -d` yields `/tmp/tmp.XXXX` here and `cygpath -w /tmp` resolves to `C:\Users\DAILY-~1\AppData\Local\Temp`, byte-identical to the directory §4 names as the one thing a root may not be, and to the `export TEMP=` value D11 measured in every Bash-tool shell.

§4's escape does not close it. It offers "unit 7 grades the specific `mktemp -d` directory it created rather than the temp root", but unit 2 S2/S5 admit a path only when a DECLARED root prefix-matches it, separator-anchored, and the per-run `$WORK` name is random. No static conf can admit a random child without declaring its parent, and a partial-name prefix like `<temp>/tmp.` is refused by the separator anchoring AC5 demands. Unit 7 is forbidden from editing the conf, so it cannot resolve this either; its §4 item 3 probes `scope.py --check-path "$TMPDIR"` and then asserts two paragraphs later that "the runner declares its SCRATCH PARENT, not the shared temp root", contradicting itself within one section.

**And no criterion grades either rule.** Unit 6 AC2 observes only a BLANK roots list. So whichever way the author silently resolves it, every AC in the set stays green: declare the temp root and D11 re-opens wholesale — every sibling session's scratchpad- and mktemp-rooted processes admit by ordinary path-shaped argument, with `reap-orphans` killing them, through a vector AC8 does not cover — or omit it and unit 7 S4's probe answers REFUSED on every bar, AC4's fallback becomes the permanent answer, and AC5's delegation is unreachable in production. Unit 6 §8 F1 makes the `reap-orphans` default conditional on exactly this exclusion, so the fork also silently decides the kit's default mode.

**Fix.** Resolve the fork in S3 and say which branch was taken. The one that costs least: scope a dedicated scratch parent into unit 7, which already edits `run-gates.sh` — create `${TMPDIR}/gov-run-gates/` before line 940 and make it `WORK=$(mktemp -d -p "$GOV_GATE_SCRATCH")` — then declare THAT path in unit 6 S3, name it (not `$TMPDIR`) in unit 7 §4 item 3, and add it to §4's list of what a root may be. Declare the unit 6 → unit 7 edge in both Edges sections, since unit 6 at `order 1` is now writing a value unit 7 at `order 6` makes true. Add an AC to unit 6 asserting the SHIPPED value: `PROCMON_ROOTS` contains no ancestor of the system temp root, and `scope.py --check-path` answers ADMITTED for the real scratch path a run will use. Change unit 7 AC4 from "a refusal is announced" to "the probe answers ADMITTED for the path this runner actually creates". Note the same question for the per-leg hermetic `mktemp -d` scratches if their processes must be admissible.

**Left-shift gate.** A spec-lint arm in `check-memory-hygiene.sh`: a `§4` section headed with a prohibition ("MAY NOT CONTAIN", "must not", "never") whose object string also appears in a `§2` scope item of the SAME unit reds. Crude, cheap, and it catches exactly the shape where one document tells its own author two things. Beyond the spec, the durable gate is a `.process-monitor.conf` lint in the kit's own adopter test: refuse a `PROCMON_ROOTS` entry that is an ancestor of `$TMPDIR`, and refuse a conf whose declared roots do not admit the runner's scratch path — the pair, checked together, is the only thing that keeps this from being re-litigated at every adoption.

### D17 — BLOCKER — unit 4 §2 S3 and §4 "Descendant inheritance", with AC4

*Raw ids 27, 16. D9's repair overshot.*

S1 builds the walked set as the transitive descendant closure of the target plus the target, and AC2 puts the root last in it. AC8 grades the root in scope STANDALONE and refuses before the walk starts. S3's rev-2 inheritance clause then admits a member if it is in scope standalone **or an ancestor of it inside the same walked set is**. Every member's ancestor chain inside that set terminates at the root, and the root was just admitted — so **inheritance admits every member unconditionally** and the per-member refusal S3 retains has no reachable failing case through `run_kill(pid, census, conf)`.

AC4 concedes it in its own wording: the member with an out-of-scope ancestor chain "is injected into the walked set". A criterion stageable only by reaching past the unit's public entry point is the could-not-fail class this build already folded twice, as D4 and D10, and it is now sitting on the only irreversible thing the kit does.

§4's justification is worse than vacuous, it is backwards. It says the retained refusal exists for "a walk that has wandered out of the tree" — but a row pulled in by a stale, recycled or simply wrong `ppid` edge is a descendant of the root *by that same edge*, so it inherits from the root and is admitted. The one case the refusal is written for is the one case inheritance guarantees passes. And unit 3 §4 records that `ps -W` gives every non-MSYS Windows process `ppid 0`, so mis-parenting on this host is measured, not hypothetical.

The weight this carries makes it a blocker rather than a high: §3 Edges sells S3 as "the fence, re-run per member rather than trusted", and §5 lists it FIRST among the mitigations for the kill path. After the root check, nothing in the reaper consults unit 2 again — the blast radius is whatever the edge graph says, not what the fence says.

**Fix.** Either delete the per-member re-check and state plainly that the root grading is the whole fence, moving §5's mitigation weight onto AC8 and saying so in §3 Edges — or make the re-check non-vacuous. The non-vacuous form: a walked member is admitted if it is admissible standalone, OR by inheritance from an ancestor that is itself admissible standalone AND whose edge to the member is corroborated (the member's own age is less than the ancestor's, which rejects a recycled-pid attachment). A member whose `command` is `None`, or whose program path prefix-matches no declared root and whose parent edge is not corroborated, is DROPPED from the kill set and reported rather than inherited. Re-point AC4 at that dropped-member case over a set the walk itself produced, and keep the whole-set refusal only for a root that fails AC8. Add an AC staging a row attached to an in-scope root by a `ppid` whose real parent is dead, asserting it is refused.

**Left-shift gate.** A spec-lint arm: an acceptance criterion whose staging verb is `injected`, `inserted`, `forced`, `monkeypatched` or `stubbed into` against a structure the unit's own §2 says it BUILDS reds, and demands either a rewrite or an explicit `staging: past-entry-point` marker with a reason. Every could-not-fail criterion this build has produced — D4, D10, D17 — announced itself in exactly that verb.

### D18 — BLOCKER — unit 3 §4 "The ORPHAN predicate, stated ONCE", against AC4 and AC5, with unit 1 §4/AC2 and unit 6 §8 F1

*Raw id 13. D15's repair, colliding with D11's.*

The rev-2 predicate folds `ppid 0` into "parentless" on the strength of a measurement that says the opposite. §4's own sentence is that `ps -W` reports EVERY non-MSYS Windows process with `ppid 0` — that is "parent not visible in this backend", not "parent dead", and the live-predicate record calls it out by name as what "the naive orphan predicate reads as parent is dead" (297 of 315 rows). AC5 then forbids liveness from rescuing such a row: it rescues only "a ppid naming a LIVE census row that is not 0 or 1". And unit 1 §4/AC2 deliberately discard CIM's `ParentProcessId`, which is the only parent data those rows have. So the rescue is closed on both sides by design.

The two round-1 repairs combine into the hazard. D15 added `ppid 0` to the predicate; D11 replaced raw-string matching with program-path admission, which admits any `python.exe` or `node.exe` whose executable path sits under a declared root — which is what a gate leg and a dev server look like. So every in-scope non-MSYS process grades ORPHAN the moment it passes `PROCMON_AGE_CEILING`, with a live parent. Unit 6 §8 F1 resolves the default mode to `reap-orphans` on the stated ground that an ORPHAN "has no live claimant by construction", which is precisely the property that fails here. **The kit's default behaviour is to kill healthy, live-parented, in-scope processes.**

§4's mitigation does not reach it. "Only the age ceiling separates them" covers the age-0 shells §4 names, not anything legitimately long-running past the ceiling, and unit 6 §4 requires only that the ceiling sit above the bar's 3600 s `GATE_BOUND` — while this repo's own bar has a 26-minute floor, 2940 s leg ceilings, and full bars on this node that have run for hours.

**Fix.** Split the predicate in §4. A `ppid` absent from the census, or `ppid == 1`, is PARENTLESS. A `ppid == 0` is PARENT-UNKNOWN and grades `UNKNOWN`, never `ORPHAN`. Re-point AC4 at `ppid 1` and add an arm asserting a `ppid 0` row with a live CIM parent is NOT reaped under `reap-orphans`. If `ppid 0` must stay reapable, §4 has to name the second source that establishes the parent is actually dead and reconcile it with unit 1 AC2's ban on CIM's parent graph — those two cannot both stand. The split may also give §3's `UNKNOWN` member a producing condition; this round did not check whether it has another one, so verify that rather than assuming it.

**Left-shift gate.** A spec-lint arm binding a predicate to the measurement it cites: where a §4 predicate names a sentinel value (`0`, `1`, `None`) that the same section's prose also calls "not visible", "unknown", "not reported" or "absent", the criterion set must contain an arm staging that sentinel with the underlying condition FALSE. Mechanical, and it is the difference between "parent is dead" and "parent is not in this table" — the distinction the whole reaper hangs on.

### D19 — BLOCKER — unit 2 §4 "What is matched, and what is NOT", the env-assignment sentence, and AC8

*Raw id 26. D11's repair does not cover its own input.*

The repair defines an environment assignment as "`NAME=value` before the first program token". The measured shape it was written for is `export TEMP=…` **inside a `bash -c` script body**: the real Bash-tool argv is `"…bash.exe" -c "source … && export TEMP='C:\Users\DAILY-~1\AppData\Local\Temp' TMP='…' && …"`. That assignment sits after `bash.exe`, after `source`, behind `export` — it is neither a leading prefix assignment nor a program token, so the new rule does not describe the input D11 was written for. Under the definition as written, `TEMP=<tempdir>` is an ARGUMENT, and it contains separators, so it is a PATH-SHAPED ARGUMENT and admits.

Worse for the criterion: AC8's precondition is "a row whose ONLY occurrence of a declared root is inside an environment assignment — the real Bash-tool shape, taken from a captured snapshot of this machine". I checked all nine live rows carrying `export TEMP=` on this node, and in **zero** of them is the assignment the only occurrence — every one also names a genuine path under the temp root (`pwd -P >| '/c/Users/DAILY-~1/AppData/Local/Temp/claude-4a06-cwd'`, plus eval'd scratchpad paths). AC8 cannot be staged from the snapshot it pins. An implementer meeting it will either weaken the criterion or invent an unspecified tokenizer, and either way declaring the temp root still admits every agent session on the box through ordinary path-shaped arguments — so §4's diagnosis of D11 is incomplete, not only its wording.

One mechanism claim from the raw finding is NOT endorsed here: it argued the whole `-c` body admits by containment. §4 specifies an anchored, separator-terminated PREFIX match, under which a token beginning `source` or `TEMP='` matches nothing. The defect stands on the two grounds above without it.

**Fix.** Restate §4's rule as two rules. (a) Strip a `NAME=value` token wherever it appears, including after `export`, `env` or `declare`, and including inside a `-c` body. (b) State explicitly how a `-c` / `-Command` string argument is handled: word-split it and grade the resulting tokens, never treat the body as one path-shaped token. Then add an AC pinning both shapes from the captured snapshot — one row whose only root occurrence is `export TEMP=` inside a `-c` body (REFUSED), and one whose `-c` body runs a program at an absolute repo path (ADMITTED). If no row of the first shape exists in the real snapshot, say so in §4 and construct the fixture explicitly rather than claiming it is "the real Bash-tool shape".

**Left-shift gate.** The scope fence's own test suite gets a corpus arm rather than a hand-written fixture: capture one `census.py --print` snapshot into the kit as a frozen fixture, and assert `scope.py` over it admits a declared, hand-checked set of pids and no others. A carve-out whose precondition does not occur in the corpus reds at authoring time instead of at adoption. This is the same "run a candidate predicate over the real tree before wiring it" rule §7 already states, applied to a spec.

### D20 — BLOCKER — unit 7 §2 S2/S4 and AC5, against unit 4 AC8 and unit 2 S2/S5

*Raw id 28. The interrupt leak stays open on the delegated path.*

S2/AC5 delegate the teardown kill to `run_kill` with a RECORDED LEG PID as the walk root. Unit 4 AC8 grades that root STANDALONE — "inheritance is applied to the root" is its explicit Red-when. And unit 4 §4 itself measures that a real leg shell "carries a relative script path — neither names any repo path". Unit 2 S2/S5 match a declared ABSOLUTE root as a separator-anchored prefix of the resolved program path or of a path-shaped argument, and §3 refuses cwd probing. **So the root is refused and every delegated `run_kill` aborts before the walk.**

I confirmed the invocation shape at source: `AGENTS.md` and `.githooks/pre-push:292` (`bash $GOV_KITROOT/run-gates/run-gates.sh`, with `GOV_KITROOT=tools` at :71) both invoke the runner relatively, and `runleg` records `$BASHPID` of a subshell that inherits that argv at `run-gates.sh:1280`. AC5 ("the signal path's kill goes through `run_kill` and the grandchild is verified dead") therefore has no passing configuration in this repo. S4's profile-time probe cannot detect it either, because that probe grades only the SCRATCH PARENT PATH — so the refusal surfaces mid-kill, which is exactly the D6 failure mode rev-2 claims to have closed.

**Fix.** State in §4 what the walk root is and how it is admitted. Either have the runner pass its OWN pid, whose argv the profile line can be made absolute, as the root; or add a caller-asserted root admission to unit 4 — an explicit `--root-admitted-by <declared root>` the runner supplies at profile time, graded once by `--check-path` and refused if that root is not declared. Then extend S4's probe to cover the leg-root admission as well as the scratch path, and add an AC observing that the probe REDS when the leg root would be refused. Note the interaction with D16: both defects are unit 7 discovering at kill time that unit 2 will refuse it, and both fixes belong in the same profile-time probe.

**Left-shift gate.** A cross-unit spec-lint arm, and the most valuable one this round suggests: where unit X's scope item names a function unit Y exposes, and unit Y has an AC that REFUSES on a property of that function's argument, unit X must carry a scope item stating how its argument satisfies the property. Mechanical enough to implement as "a `consumes-from` edge naming a symbol requires the consuming unit to cite the producing unit's refusal criteria by id". Both D20 and D16 are that missing citation.

---

## Highs

### D21 — HIGH — unit 1 §4 "Data model" and §2 S2, against unit 3 §4 and unit 4 S4

*Raw id 20. D8's repair named the binary and not the split.*

§4 asserts "`ppid` and `pid` are in ONE namespace per row" and the data model calls `pid` "the id the REAPER can kill". S2's source is `ps -W`, and one correction to the raw finding's wording is owed: `ps -W` does NOT put a raw Windows pid in the PID column, it puts `winpid | 0x400000` — all 321 rows measured here had `PID != WINPID`, e.g. PID 4223612 against WINPID 29308. The operational claim is nonetheless exactly right and worse than the finding stated. I spawned a native `PING.EXE`; both the bash builtin `kill` and `/usr/bin/kill` answered `No such process` for its PID and the process survived. Only `taskkill //PID 29308 //F` killed it.

So "the id the REAPER can kill" and "ONE namespace per row" are false for the entire non-MSYS population — unit 3 §4's own `ppid 0` rows, 300-plus of ~313 here, including every `python.exe`, `node.exe` and `pwsh.exe` the kit exists to reap. Unit 4 S4 signals every walked member through the MSYS `kill` binary because that is "the namespace the walk is in", and for these rows that integer reaches nothing: the row is reported as a survivor forever, or matches an unrelated MSYS process. No criterion covers it — AC9 stages an MSYS process, AC10 the absent binary, neither a non-MSYS row.

**Fix.** Add a `namespace` field to S1's row contract and to AC1's completeness check, with unit 4 S4 refusing to signal a non-MSYS row (or routing it explicitly, if `taskkill` is in scope — but the research record's `taskkill /T` arm killed one of four, so say why the single-pid form is different before relying on it). Or state in S2 that non-MSYS rows are excluded from the census and count them like S9's other partial classes. Either way add an arm to AC1 or AC2 asserting the chosen rule over a captured `ps -W` snapshot containing both row kinds. Reconcile with D22, which needs the same population split for a different reason.

**Left-shift gate.** A kit self-test arm over the frozen census fixture: every row the census emits must answer a liveness probe issued through the signal path the reaper would use — `kill -0` for MSYS rows, whatever the spec chooses for the rest. A row the reaper's own signal path cannot see is a row the census must not claim it can kill, and that assertion is one line per row over a fixture.

### D22 — HIGH — unit 4 §4 "The walk", with AC1

*Raw id 30. The promise excludes the population the kit exists for.*

The child map is built from the census's `ppid` edges, and unit 3 §4 measures those to be MSYS-only: "MSYS `ps -W` reports every non-MSYS Windows process with `ppid 0`", with MSYS rows (`ppid != 0`) at 10 of 313 in the live-predicate record. So the descendant closure **structurally cannot contain a native Windows child** of an MSYS process. §1 promises "kill a flagged process AND its descendants"; on this node's real population that promise excludes exactly the children the gate runner spawns, since `run-gates` dispatches with argv[0] rewritten to `$PYBIN` at `run-gates.sh:1281`.

AC1 cannot detect it: its staged tree is `bash → bash -c → sleep`, all MSYS binaries, the research record's 5-of-5 arm. The criterion passes while the reachable-descendant class the kit exists for is untouched — §7's "gate the CLASS, not the instance", broken in a spec. Unit 7 then inherits a delegation no better than the fallback it replaces, and S2's "survivors reported" names nothing, because the survivors were never walked.

**Fix.** State the edge semantics in unit 1 §4's data model — `ppid` edges exist only between MSYS rows; a native Windows row carries `ppid 0` and has no parent edge in this census — and repeat it in unit 4 §4. Then say what unit 4 DOES about it: either carry CIM's `ParentProcessId` as a SECOND, explicitly-named edge set used for the descendant walk only and never for the ORPHAN predicate (which keeps unit 1 AC2's ban intact for the purpose it was written for), or declare native descendants out of reach in §3 and put the negative in the README. Extend AC1's fixture with one native Windows grandchild (`python -c 'time.sleep(…)'`) and assert the walked set either contains it or the run names it as unreachable. State whether the MSYS `kill` binary can signal such a row at all — D21 measured that it cannot.

**Left-shift gate.** The reaper's own suite gets a two-namespace fixture as a floor, not an option: `bash → bash -c → python -c sleep`, asserted on every run. One fixture, and it fails the day someone assumes the edge graph is complete. Pair it with an arm asserting the walked-set size against the fixture's own process count, so a silently truncated walk reds rather than reporting a small green set.

### D23 — HIGH — unit 5 §2 S4 and §4 Files touched, with unit 6 §2 S4, §3 Edges and §4

*Raw ids 18, 39. D1's class, repaired as an instance.*

Unit 5's wiring is specified as an adopter-written `.claude/settings.json` edit with no `*.fragment.json`, while this repo's hook contract IS a tracked fragment. `tools/settings-merge.py` wires a non-default hook only from a `--fragment` file declaring `{name, event, matcher, marker, hook_path}`, one per event — so unit 5's two entries (PostToolUse `Bash|PowerShell`, plus SessionStart) need two fragments. `tools/check-hook-destinations.sh` derives its whole population from tracked `*.fragment.json` and REFUSES on an empty one; `check-wiring.sh`'s arms read the shipped fragment. `tools/memory-recall/recall-opened.fragment.json` is the precedent.

Neither spec's Files-touched, scope, Edges or §4 Inventory contains any fragment. Unit 6's scope covers conf keys, the descriptor, the adopter and the README only, and its §7 "New arm" list for `adopt-process-monitor.test.sh` does not include AC5's `test_wiring_is_idempotent`. So §7's `check-wiring self-test` and `hook destinations` legs — both `subject: repo`, listed by both units — cannot observe a hook nothing declares, and AC5's idempotence is graded only by the kit's own suite.

The ordering makes it worse. A fragment landing at `order 1` with `hook_path` naming `tools/process-monitor/procmon-hook.js` reds the `hook destinations` leg on every bar until unit 5 lands at `order 6`: arm 1 resolves `hook_path` against descriptor destinations, and `expand_rules` (`govkit.py:257-280`) enumerates only TRACKED files under `home`. Deferring it instead leaves AC5 gradeable by no file either unit owns. This is D1's shape — a destination declared five units before the file that satisfies it — repaired as an instance in the `version_from` row and not as a class. AC6's "SessionStart form" is separately mechanism-less: one fragment carries one event, and nothing says how the hook distinguishes its two invocations.

**Fix.** Give the fragments an owner and a §2 line. Cleanest: unit 5 ships `procmon-hook.fragment.json` (PostToolUse, matcher `Bash|PowerShell`) plus the SessionStart declaration, declares the edit of unit 6's `adopt-process-monitor.sh` and `.test.sh` in its own §4 Files touched, and takes AC5's observer with it — with unit 6 §3 gaining an explicit "the hook wiring lands with unit 5" non-goal so the `hook destinations` leg has no subject until then. Claim the files in unit 6's `[[files]]`, have the adopter merge through `settings-merge.py` as `adopt-memory-recall.sh` does (hand-writing the JSON is ruled out by unit 5 §10), and define in S5 how the hook is told which form it is running — argv from the fragment is the obvious answer and should be stated rather than left to the implementer.

**Left-shift gate.** Generalise D1's repair into the arm it should have been: a spec-lint check that every path named in a unit's §4 Inventory `Where` cell, §7 leg list, or acceptance-criterion observer is declared as new or edited by a unit whose `order` is less than or equal to this one. That single predicate catches D1, D23 and the unit 6 → unit 7 edge in D16, and it is a path-existence check over the spec set with no runtime.

### D24 — HIGH — unit 7 §2 S1 and §4 "Where it hooks in"

*Raw id 41. The reap lands in front of the beacon release.*

The reap is inserted into `cleanup()` ahead of `rm -rf "$WORK"`, and therefore ahead of `ts_release; ts_drop_ticket` — `cleanup()` is one line at `run-gates.sh:953`: `rm -rf "$WORK" 2>/dev/null || true; ts_release; ts_drop_ticket`. The header directly above it (`:941-952`) records why the trap was widened past EXIT: a beacon that releases only on a clean exit "turns every Ctrl-C into a repository that queues behind a run nobody is doing until the TTL expires" (TS_TTL 1800 s).

Unit 7 puts a census-plus-`run_kill` step — two ~1.2 s censuses by unit 4's own figures, with **no declared bound anywhere in unit 7**; unit 5 S6 declares one for its hook, unit 7 declares none — in front of that release. A hung or slow census now sits between a Ctrl-C and the beacon, and a second signal during it leaves both behind. That is the recorded wedge class of TOOL-aBoundedCeiling-12, where three dead tickets wedged a lander for 6858 s, and of TOOL-aSurfacedLexicon-25. No AC covers it: AC2 asserts exit STATUS only, and §5's risk paragraph claims the wedge risk is mitigated by being "ordered before an existing `rm -rf`" — which does not cover the release it is now also ahead of.

**Fix.** Bound the reaping step with a declared wall and make the release unconditional on its outcome: reap, `|| true`, then `ts_release; ts_drop_ticket`, then `rm -rf`. Or release first and reap after, which is simpler and costs only the theoretical case of a second run claiming the turnstile while the first is still killing — say which you chose and why. Either way add an AC to §6: after a TERM with the monitor hung or raising, the turnstile beacon and the ticket are gone. The existing suite already has fixtures for that arm.

**Left-shift gate.** Extend `run-gates.turnstile.test.sh` with an arm that stubs the monitor to `sleep 600` and asserts the beacon and ticket are released within the declared wall after a TERM. It is the check that would have caught TOOL-aBoundedCeiling-12 too, so it earns its place independently of this build — and it is the compensating check §7 demands for any step added to a trap.

### D25 — HIGH — unit 4 §2 S5 against §6

*Raw id 4. D5's migration dropped the guard.*

S5 promises `--sweep` prints "the population, scoped, flagged, killed and survivor counts" and cites AC5/AC6. AC5 grades mode behaviour plus "still prints the flagged rows" — rows, not a count — with a red-when of "any mode kills a row the classifier did not flag". AC6 grades the dry run's WALKED and SURVIVOR sets against the real run's, on the dry path only. **No criterion in unit 4 §6 observes any of the five counts as printed figures**, and unit 4 carries no `figure:` marker anywhere, though the convention is live in this set — unit 3 AC7 and unit 7 AC6 both carry `figure: DERIVED`.

The migration is on the record: unit 3 §3 and its rev-2 log show D5 stripping "the scoped size" from `--report` and handing the whole chain to unit 4's `--sweep`. Unit 3's AC7 red-when explicitly forbade a literal count. That guard did not travel with the figure. So the sweep's only human-readable summary — the thing a session reads, and the thing unit 5's hook surfaces — can print literals or omit the scoped count entirely and everything stays green. Unit 4 §5 asserts the counts are "returned and printed separately, never summed", graded by nothing.

**Fix.** Add an AC to unit 4 mirroring unit 3's AC7: over a fixture, the sweep's summary names all five counts, each compared against the fixture's own lengths, carrying `figure: DERIVED`. Re-point S5's observer list at it.

**Left-shift gate.** A spec-lint arm: a §2 item whose text contains "prints the … count(s)" or "reports … counts" must cite at least one criterion carrying a `figure:` marker. The marker convention already exists in this set; this makes it load-bearing instead of decorative, and it is the general form of "NO count of a derived population is written in prose" applied to specs.

### D26 — HIGH — unit 6 §6 AC5, against §7

*Raw id 19. D2's shape, re-introduced in the criterion next door.*

AC5's second conjunct — "that probe has been RUN against a blank `PROCMON_ROOTS` and observed to exit non-zero" — is attributed to `govkit.py selfcheck`, which cannot see it. Check 6 in `tools/govkit/govkit.py` (the `[[hole]]` loop, ~line 1344) asserts only that a declared hole carries a `discharge` probe and a non-empty `why`; it never executes the probe. Execution lives behind `--run-discharge` in `cmd_check`/`cmd_plan`, and none of unit 6 §7's legs runs it — `tools/gate-legs.json` has `govkit selfcheck` as plain `python tools/govkit/govkit.py selfcheck`, and `refusal join`, `acceptance matrix` and `kit placeholders` are separate scripts.

So the criterion passes on the declaration alone, which is precisely the red-when it states: "the hole is declared with a probe nobody staged a failure for". D2 was the same witness mismatch, and the fold repaired it in AC6 by moving the README witness to a real arm — while leaving the identical defect in the criterion beside it.

**Fix.** Split AC5. Keep the declaration half on `govkit.py selfcheck`. Move the staged-failure half to `adopt-process-monitor.test.sh` as a named arm — `test_roots_hole_probe_reds_on_blank_roots` — running `govkit.py check --run-discharge` against a scratch tree carrying a blank `PROCMON_ROOTS` and asserting non-zero. Add that command to §7 if it is meant to bind on the bar. Note the interaction with D16: once D16's fix lands, this arm should also assert the probe reds on a roots list containing an ancestor of the temp root.

**Left-shift gate.** A spec-lint arm over the acceptance matrix that `check-acceptance-matrix` already parses: a criterion whose observer is a named command must not contain the words "has been RUN", "was executed", "has been observed" about a DIFFERENT command. More usefully, the general form — one criterion, one observer, one assertion — reds any AC whose text contains a conjunction joining two verbs with different subjects. D2, D26 and D31 are all that shape.

---

## Mediums

### D27 — MEDIUM — unit 7 §7 "New arm", the ARMS_FLOORS sentence

*Raw id 44.*

"This suite carries an assertion floor in `ARMS_FLOORS` and it MOVES with these arms" is false, verified end to end. `.memory-tree.conf:419` holds seven rows — `check-playbook-parity`, `check-template-size`, `manifest-check`, `check-memory-hygiene`, `unattended.sh`, `check-unattended.sh`, `check-method-carriers` — and names no run-gates pair. `check-arms.py` discovers its population by `HELPER_RE` `^\s*fail\(\)\s*\{` over tracked non-`.test.sh` shell files (`:53-142`); `run-gates.sh` defines no such helper (its functions are `resolve_python`, `leg_log`, `changed`, `prof_die`, `scan_descendants`, `remove_descendants`, the `ts_*` family and `cleanup`), so the pair is not discoverable at all. A builder who adds a row reds check-arms with "names X, which is NOT in the discovered population — fix the gate or remove the floor". So the highest-risk unit in the build ships its new arms behind no ratchet, while the spec says otherwise.

**Fix.** Replace the sentence with what is true: this suite is behind no arms floor because `run-gates.sh` does not use the `fail() {` protocol `check-arms` discovers, and name the compensating check. Or scope adopting the protocol in `run-gates.sh` and add the measured `tools/run-gates/run-gates.sh:<branches>:<armed>` row in the same commit, read from `check-arms.py --report` rather than typed.

**Left-shift gate.** A spec-lint arm: a §7 sentence naming `ARMS_FLOORS` must name a pair that `check-arms.py --report` actually lists. One grep and one command, and it is the "a value stated in prose beside the source that OWNS it rots" rule with a machine behind it.

### D28 — MEDIUM — unit 5 §2 S2 against §4 "The throttle check itself must be cheap", and AC3

*Raw id 45.*

S2 compares the stamp against `PROCMON_THROTTLE_S`, a key unit 6 S3 puts in `.process-monitor.conf`, while §4 states the early-exit path is "a stat of one file and nothing else — no conf parse". The threshold cannot be obtained without reading that conf. So AC3's Red-when ("the conf is parsed … before the stamp is checked") names a condition the design requires, and its arm — which shims only the census backend and asserts a marker file is absent — cannot observe that half regardless. Two answers to one question, on the path that runs on nearly every tool call, with a criterion that passes over exactly the defect it describes.

**Fix.** Decide it in S2. Either write the deadline into the stamp file so the early path is one stat plus a small read and nothing else, or admit one bounded conf read on the common path and delete the §4 claim. Then re-point AC3 at an observable that fails on the wrong choice: assert no open of `.process-monitor.conf` on the early path, or assert the early path's wall against a declared ceiling.

**Left-shift gate.** Covered by D26's suggested arm — one criterion, one observer, one assertion. The specific instance here is worth an assertion in the hook's own suite too: the early path's syscall count or wall against a declared ceiling, since "cheap" with no number is not a claim anything can check.

### D29 — MEDIUM — unit 1 §2 S9 against §6 AC10

*Raw id 22. D3's class, in unit 1.*

S9 declares TWO partial-row classes — "no `command`, or no CIM join" — says both are counted, and requires `--print` to name "both counts", citing AC10 as its only observer. AC10 grades the total, the rejected-row count (which is S7's, not S9's) and the unjoined count. **The no-command count is graded nowhere in unit 1.** That is the 115-of-314 population §5 measures and calls out itself — "a third of the table is unattributable and that number must be visible, not swallowed" — and AC10's own red-when invokes "a third of the table" while its enumeration omits the count that measures it. It is also the exact figure unit 2 AC10 and §8 F1 rest on. An implementation reporting only the unjoined count satisfies AC10 and violates S9.

**Fix.** Name the no-command count explicitly in AC10 alongside the unjoined one — three derived counts plus the total — or collapse S9's two classes into one named class and use that one name in S9, §5 and AC10.

**Left-shift gate.** The same join-lint as D31: every §2 item's "Observed by" list must name a criterion whose text mentions each noun the item promises. A crude noun-overlap check catches D3, D29 and D31, which is three instances of one class across three units in two rounds.

### D30 — MEDIUM — unit 7 §2 S2 and §5 perf/scale

*Raw id 33.*

Unit 4 exposes only per-pid entry points — `run_kill(pid, census, conf)` and `--kill <pid>` — and `run-gates.sh` is shell and cannot import python, so delegation means one process start plus two censuses per recorded leg pid. Each invocation pays a python start plus its own census (~1.2 s: 1039 ms CIM + 128 ms `ps -W`, unit 1 §5) plus the S2 verification re-read, ~2.4 s per pid. `gate-profiles.txt` declares width 8 on the capable row, so a Ctrl-C on a full bar spends 20 s or more inside an INT handler, with the scratch dir still present and a second signal the user's only exit — on the one path this unit exists to make fast and complete. §5 accounts for "one census per kill" and never draws the per-run total, which is where the cost lands. Compounds with D24: this is the unbounded step sitting in front of the beacon release.

**Fix.** Add a batch entry point to unit 4 S5/S7 — `--kill pid[,pid…]` sharing ONE census read and one verification re-read — and have unit 7 S2 name it. Correct §5's perf line to "one census plus one verification re-read per teardown, not per pid", and add an AC asserting the delegated teardown reads the census at most twice regardless of how many leg pids were recorded.

**Left-shift gate.** §7's cost-is-a-verdict rule applied to the teardown: declare a wall for the interrupt path in unit 7 §5 and assert it in the turnstile suite. A teardown with no declared ceiling reds by that fact, which is the rule the repo already runs on its suites.

### D31 — MEDIUM — unit 6 §2 S5 → §6 AC4

*Raw id 9. D2's split left the join behind.*

Every join in unit 6 §2 reads S1→AC1,AC7 · S2→AC1 · S3→AC2 · S4→AC3 · S5→AC4,AC6 · S6→AC5. AC4 grades "when the descriptor declares a placeholder token the adopter never fills, `check-kit-placeholders.py` exits non-zero" — a descriptor concern — while S5 is the README item, whose real witness is AC6 ("when README.md is searched for the negative-scope heading…"). So S5 cites a criterion it does not declare, and **AC4 is now declared by no scope item at all**: the descriptor item S1 that would own it points only at AC1 and AC7. The rev-2 log confirms the cause — D2 split AC4, gave the README half AC6 and a real arm, and left S5's citation pointing at both halves. This is exactly the off-by-one D3 found in unit 2 S6→AC7 and repaired there, surviving one unit over.

**Fix.** Change S5's observer list to AC6 only, and add "Observed by AC4" to S1, which is the item that actually declares the descriptor's placeholder tokens.

**Left-shift gate.** The join-lint from D29, and it is worth building this round: for each §2 item, every criterion it cites must share at least one content noun with it, and every criterion in §6 must be cited by at least one §2 item. The second half alone catches D31 — an orphaned criterion is mechanically detectable, needs no semantics, and this build has now produced the shape three times.

---

## The one gate this record would actually build

Six of the sixteen defects above (D25, D26, D28, D29, D31, and half of D17) are the same class: **a scope item and the criterion that observes it do not describe the same thing**. Round 1 found it twice more, as D2 and D3. Eight instances across two rounds, in five of the seven units, is not a run of bad luck — it is an unguarded join in the spec format itself.

The arm is small. Parse a spec's §2 items and their "Observed by" lists and §6's criteria, then assert two things: every criterion is cited by at least one item, and every citation shares at least one content noun with the criterion it names. No semantics, no runtime, no fixtures. It would have reded D2, D3, D25, D26, D29 and D31 at authoring time and would have made D17's vacuity visible by leaving AC4 citing an item whose verb is "walks" against a criterion whose verb is "is injected".

Second, and cheaper: the path-ordering check from D23 — every path named in a §4 Inventory `Where` cell, a §7 leg, or a criterion's observer must be shipped by a unit whose `order` is no greater than this one. That is a path-existence check over the set, and it catches D1, D16's backwards edge and D23.

Everything else here is judgement. Those two are arithmetic.
