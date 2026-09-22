**Serves:** spec-audit TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7

# aReapedSpinner — Tier-2 spec audit, round 1

*Adversarial pre-code pass over the seven-unit spec set for `tools/process-monitor/`. Node `a`, 2026-09-08, base `e2b82a53`. Findings below are pre-code: nothing here is a bug in shipped software, every one is a defect in a document that would become one.*

**Range — ROUND 1**, seven subjects pinned at these blobs: `memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-1.md@41bf032586360053e25ab6bf5fef0eec46066e98`, `…-2.md@94eaeb33cb3d30009ecf056a0bf01ea8ef903775`, `…-3.md@ecc8febe72e0884257a3e52048ae0719623088dd`, `…-4.md@24b35a61dd2ed8d04cf9a8297eaf1b97e2c901db`, `…-5.md@2684ea187096d46cf622ed25cb842529f0f21c0e`, `…-6.md@7b8669a0f2bdbe93700d0f1e6b45c9da0fdc3625`, `…-7.md@8656771170a094f6c9237c747aa04e6f271ec325`.

## Verdict: BLOCKED

Six defects are blockers and none of them is a wording problem. Two of them (D8, D9) mean the reaper as specified either signals the wrong process namespace or refuses to signal at all; one (D11) means adopting the kit as written lets it kill other agent sessions on the machine; two (D1, D10) mean an acceptance criterion is unreachable or unfailable at the unit the ordering depends on; one (D13) means the census admits rows a corpus-recorded hazard already produces on this host. The build is not ready to dispatch its first pass. The repairs are all spec edits — no unit needs re-scoping except unit 7, which needs re-justifying against the source it misreads.

### Review shape

Raw 65 · confirmed 24 · refuted 41 · unverified 0 · precision 0.37.

**Run integrity — all clean.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline. No arm of this run failed to report, so the zero counts here are evidence rather than absence of evidence, and the finding set is complete as far as four lenses reach.

**Consolidation, and how the counts below relate to the 24.** The pipeline discarded no duplicates, but the 24 confirmed findings describe 15 distinct defects: several lenses landed on the same contradiction from different sides. Each row carries its raw finding ids so nothing is lost. Severities are the ones adjudicated HERE: a merged defect takes the maximum severity in its cluster, and one finding was promoted (raw 41, HIGH → BLOCKER, see D11). Adjudicated totals across the 15 rows: **6 blockers, 7 highs, 2 mediums, 0 lows.**

| # | Sev | Unit | Address | Defect | Raw ids |
|---|-----|------|---------|--------|---------|
| D1 | BLOCKER | 6 | §4 Inventory vs §3 non-goal 1, AC1, AC6 | `version_from` pins the kit version to `census.py`, a file this unit is forbidden to ship | 19, 38, 2 |
| D8 | BLOCKER | 4 | §4 "The walk", S1 | The signal's namespace is never stated; a resolved `win32` python `os.kill`s an MSYS pid | 35 |
| D9 | BLOCKER | 4 | S3 vs AC1/AC4 | The all-or-nothing fence check aborts on every realistic tree, because real leaf argv names no root | 36 |
| D10 | BLOCKER | 7 | §1, §4, AC1 | The premise that run-gates cannot reach a grandchild is stale; AC1 passes against the unchanged runner | 37, 48 |
| D11 | BLOCKER | 2 | §4 "The containment test, both ways" | Substring containment over raw argv admits every sibling agent session once the scratch root is declared | 41 |
| D13 | BLOCKER | 1 | §4 "Windows: the join", §5 | No numeric guard against cygwin raw-argv continuation rows, a hazard this repo already recorded | 49 |
| D2 | HIGH | 6 | AC4 | The does-not-check README section is witnessed by a placeholder checker that never reads a README | 8, 26, 61 |
| D4 | HIGH | 3 | S3 vs S4/AC6 | `OVERAGE` has no reachable producing condition; AC1's closed-set arm passes on a dead member | 23 |
| D5 | HIGH | 3 | §3 Edges vs `order 3`, S5/AC7 | Unit 3 consumes unit 2 while declared in the same parallel group | 24, 58 |
| D6 | HIGH | 7 | §4 Detection vs AC3/AC6 | Profile-time detection cannot know the roots will refuse; the announcement AC3 requires is unreachable | 27 |
| D7 | HIGH | 4 | AC6 | "byte-identical to the non-dry run" is unsatisfiable given the separately-printed survivor set | 28 |
| D12 | HIGH | 4 | §10 Reuse audit | The one rejection ground is false at the lines it cites, under an explicit verified-against-source claim | 47, 50 |
| D14 | HIGH | 1 | §10 Reuse audit | "It reads no process table at all" is contradicted eleven lines inside the cited range | 51 |
| D3 | MEDIUM | 2 | S6 vs AC6/AC7 | The scope-to-acceptance join is off by one, and AC6's rule is owned by no scope item | 16, 30, 65 |
| D15 | MEDIUM | 3 | S3 vs §4 vs AC4 | Three statements of the ORPHAN predicate disagree on the reparented case the kit exists for | 60 |

---

## Blockers

### D1 — BLOCKER — unit 6 §4 Inventory, against §3 non-goal 1 and AC1/AC6

The descriptor's `version_from` is declared as pointing into `census.py`. Unit 6 is `order 1` and its §3 forbids it from shipping any engine file: "`census.py`, `scope.py`, `classify.py`, `reap.py` and the hook belong to units 1 to 5, and this unit must land green WITHOUT them."

`tools/govkit/govkit.py:1194` fails with `entry '<eid>' version_from names a file that does not exist`. The only escapes the checker offers are a real file whose pattern matches exactly one line, or `version_from = { none = "<reason>" }` with a non-empty reason; unit 6 declares neither. `tools/gate-legs.json` carries both `govkit selfcheck` and `kit version markers` as `subject: repo` with no guard, so they run and red on **every** bar until unit 1 lands. AC1 (`govkit selfcheck` exits 0) and AC6 (a green full bar with no engine file present) are therefore both unreachable at the unit the whole ordering starts from. Nor does unit 1 repair it: spec-1 §2 never declares `KIT_PROCESS_MONITOR_VERSION` and its §6 has no criterion for it, so no unit in this build actually creates the marker.

**Fix.** Declare `version_from = { none = "<reason>" }` in unit 6's S1, or pin it at a file unit 6 itself ships (`adopt-process-monitor.sh`, matching the sibling kits' shell carriers). Move the `KIT_PROCESS_MONITOR_VERSION` row out of unit 6's §4 Inventory and into unit 1's §2 with its own AC, and add an AC to unit 6 asserting the descriptor's `version_from` resolves against files this unit ships.

**Left-shift gate.** A spec-lint arm in `check-memory-hygiene.sh`: every §4 Inventory row's `Where` cell must name a path that the same unit's §2 or its "Files touched" list declares as new or edited. An inventory row pointing at another unit's file is exactly this defect, is mechanical, and would have reded at authoring time.

### D8 — BLOCKER — unit 4 §4 "The walk" and S1: the signal's namespace is never stated

§4 says "signal each in that order" and never says what issues the signal. S1 puts the whole reaper in a `.py` module. Measured on this node: `. tools/lib/resolve-python.sh; resolve_python` yields an interpreter whose `sys.platform` is `win32`, reporting `os.getpid()` 7144 while the calling MSYS shell's `$$` was 2581555 — two disjoint namespaces. The stdlib reach for a python reaper is `os.kill`, which on `win32` hands whatever integer it is given to `TerminateProcess` against a **Windows** pid.

Spec-1 §4 fixes the row contract as "`pid` — the id the REAPER can kill, in the backend's own namespace", which holds only if the signal is issued from the MSYS side. This is the mixed-graph defect this build's own research record measured — `taskkill /PID <winpid> /T /F` printing SUCCESS over one death of four — relocated from the census to the kill, inside the unit the spec itself calls the only irreversible thing the kit does. The research record's winning arm was a bash `kill`, not a python one.

**Fix.** State in §4 that the signal is issued through the MSYS `kill` binary (or a named MSYS-namespace equivalent) and declare that dependency in §2. Add an AC that kills a staged MSYS process and asserts death by re-read, and a second asserting the signal is never issued via native `os.kill` on a Windows build.

**Left-shift gate.** A grep leg over `tools/process-monitor/`: `os.kill(` and `subprocess` calls to `taskkill` are refused outright, with the reason in the leg header. It is a class ban, not an instance fix, and it survives the next person who reaches for the obvious stdlib call.

### D9 — BLOCKER — unit 4 S3 against AC1 and AC4: the fence refuses every real tree

S3 refuses the ENTIRE kill when any walked member is out of scope, and §4 reinforces it: an inadmissible member "aborts the whole call… and kills nothing." Unit 2 S2 admits a row only when its `command` contains a declared `PROCMON_ROOTS` prefix, with no descendant inheritance, no name inference (§3) and no cwd probing (§3, explicitly rejected).

Measured: a staged descendant reads `sleep 45` in `ps -ef` and `"C:\Program Files\Git\usr\bin\sleep.exe" 45` in CIM. Neither names any repo path. The same is true of a real leg shell, which carries a relative script path. Every realistic tree — bash → `bash -c` → sleep — therefore contains at least one bare-argv leaf, the fence refuses that member, and S3 aborts. The reaper can never kill anything.

AC1 ("the tree dies completely") and AC4 ("an out-of-scope member aborts the call") are jointly satisfiable only by fixtures that contradict each other, and AC1's fixture note is wrong on its own terms: creating a `sleep` under a declared root does not put that root into the `sleep`'s command string.

**Fix.** State the attribution rule for a descendant reached by the walk — a member inherits scope from an in-scope ancestor **in the same walked set**, rather than being re-graded standalone against the root list. Then AC4's out-of-scope member has to be a member whose ancestor chain is also out of scope, which is the case the refusal is actually for. Add an AC staging a tree whose leaf command carries no path and asserting the tree still dies.

**Left-shift gate.** In the kit's own test file, one arm that stages the three-deep `bash → bash -c → sleep` tree from the research record and asserts 3 of 3 dead. That arm is the whole build's reason to exist and nothing currently grades it.

### D10 — BLOCKER — unit 7 §1 Goal, §4 "Where it hooks in", AC1: the premise is stale and AC1 cannot fail

At BASE `e2b82a53`, `tools/run-gates/run-gates.sh:428-474` already holds `scan_descendants` (a depth-8 ppid walk over one pre-kill `ps -ef` snapshot) and `remove_descendants`, which SIGKILLs every walked member at `:449-452` and then re-reads with `kill -0` at `:466-468` and reports survivors. The file's own header at `:416-417` reads: "The wall kills RECORDED PER-LEG PIDS and their descendants, touching nothing outside that set." That is the opposite of §1's premise that the runner "kills the leg pids it recorded and its own header explains why it cannot do better."

So AC1's Red-when — "only the recorded leg pid dies — today's behaviour" — is already false on the wall path. The criterion passes against the unchanged runner and certifies nothing.

The genuinely open gaps go unnamed. `remove_descendants` is called only from the wall watcher at `:1517`; the INT/TERM/HUP traps at `:955-957` run `cleanup()` (`:953`), which is `rm -rf "$WORK"; ts_release; ts_drop_ticket` and kills nothing at all. The walk is also capped at depth 8. And `TOOL-aQuenchedHarness-1` rev-6 records that the descendant walk is itself ungraded.

**Fix.** Re-read `run-gates.sh:407-474` and rewrite §1 and §4 against it. Re-scope the unit to what is actually open: the interrupt path, which kills nothing; the depth-8 bound; verification by re-read, which the existing `kill -0` sweep provides only as a message. Promote AC5's interrupt path to the unit's primary criterion. Stage AC1 RED against today's code before accepting it, or replace it with a criterion the current runner fails.

**Left-shift gate.** The charter already says a new gate is not landed until its failing case has been observed; the same rule belongs on acceptance criteria that claim to fix existing behaviour. Add to the spec template's §6 guidance: an AC whose Red-when describes "today's behaviour" carries the observed-RED command in the criterion itself. Machine arm: a spec-lint check that every `path:line` citation in a spec resolves — the file exists, the line range exists — which also catches D12 and D14.

### D11 — BLOCKER (promoted from HIGH) — unit 2 §4 "The containment test, both ways"

§4 treats the command string as a path-like token; its only anchoring rule is separator-termination, which rejects `repo-other` and says nothing about a root appearing inside an environment assignment or an unrelated argument. Reproduced on this node: every Claude Bash-tool shell carries `export TEMP='C:\Users\DAILY-~1\AppData\Local\Temp'` plus a shell-snapshot path inside its argv, and `mktemp -d` resolves under that same temp root.

Unit 7 §4 **requires** the scratch root be declared so the runner's `mktemp -d` legs are admissible. Declaring it therefore admits every agent session on the machine, in every repository — because the substring appears in their env assignments, not in their program path. S3's self fence excludes only the caller's own ancestry, so a sibling session's shell stays in scope and killable, and one such shell in the live table already has PPID 1, which is ORPHAN under the resolved default `reap-orphans` mode.

**Promotion rationale.** This was reported HIGH. It is adjudicated BLOCKER because it is not a gap in a criterion, it is the safety property of the kit inverted: unit 2 §1 claims positive attribution as *the* guarantee, and following unit 7's own requirement turns the guarantee into a licence to kill unrelated agent sessions. Severity here is blast radius, and the blast radius is other people's work.

**Fix.** State that matching is against the resolved PROGRAM PATH and the path-shaped arguments of the row, never the raw string. Add an AC staging a command line whose only occurrence of a declared root is inside an environment assignment, asserting REFUSED. Separately, reconsider whether unit 7 should declare the temp root at all, or grade the specific `mktemp -d` directory it created.

**Left-shift gate.** An arm in the fence's own test that feeds a fixture snapshot captured from this machine's real `ps -ef` (env assignments and all) and asserts the admitted set is exactly the staged tree. A synthetic fixture would not have caught this; a real one does.

### D13 — BLOCKER — unit 1 §4 "Windows: the join" and §5: no guard against raw-argv continuation rows

`run-gates.sh:432-436` records the hazard verbatim: cygwin `ps -ef` prints argv RAW, so a command line containing a newline splits one process across rows "whose field 2 and 3 are attacker-or-accident-chosen text"; snapshots on this box "already carry about ten such continuation rows from other sessions' multi-line `bash -c`"; and without the guard "this walk feeds arbitrary text to `kill -9`". Reproduced here — the live table shows one `bash -c` whose argv spans dozens of rows of comment prose.

No unit's spec requires a numeric guard. Unit 1 §4 fixes a column contract for `ps -W` and `ps -eo` with no mention of continuation rows, and AC1's row contract asserts only that "no row carries a `None` pid or ppid" — a garbage row whose leading token happens to be numeric satisfies it. A continuation row is a fragment of a REAL in-scope command line, so unit 2's positive fence admits it, unit 3 grades it, and unit 4 kills whatever integer that fragment spells. The row contract certifies coverage it does not have.

That the corpus's one existing walker already carries this guard, and that unit 1's §10 denies that walker exists (D14), is why the correction was not inherited.

**Fix.** Add a scope item to unit 1 requiring an anchored numeric guard on `pid`/`ppid` plus explicit continuation-row rejection, with a criterion staged from a real multi-line `bash -c` snapshot — the recorded population makes this reproducible on node `a`. Restate it in unit 2 as an admission precondition rather than leaving it implicit in the census.

**Left-shift gate.** Adopt `run-gates.sh:435-436`'s predicate as a fixture-driven arm in the census test: a snapshot file containing a multi-line `bash -c` in, and an assertion that the parsed row count equals the process count and that no synthetic row survives. Cite `TOOL-aQuenchedHarness-1` in the arm header so the next parser inherits the correction rather than rediscovering it.

---

## High

### D2 — HIGH — unit 6 AC4: the criterion cannot fail on the property it states

AC4's condition is that `README.md` "carries a section stating what this kit does NOT check". Its named observer is `tools/check-kit-placeholders.py`, whose own header says it joins a descriptor's declared `[[files]]` placeholders against the adopter's literal `{{TOKEN}}` text and that "it grades DECLARATIONS, never rendered output." It never opens a README for prose. A README with no such section and no unfilled placeholders passes every listed observation. The AC's own Red-when ("ships with template placeholders unfilled") grades a different property than its condition.

This is `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`, first variant, landing on the one criterion that guards the kit's honesty about its own limits — the negative-scope section the charter §7 requires. Unit 6 §7 also omits the `kit placeholders` leg from its gate list, so the cited observer is not even on this unit's declared bar.

**Fix.** Split it. Keep the placeholder join as its own AC observed by `check-kit-placeholders.py`, and add that leg to §7. Write a second AC for the does-not-check section, observed by a named arm in `adopt-process-monitor.test.sh` that greps the README for the heading and fails when it is absent.

**Left-shift gate.** A spec-lint arm asserting every AC's observation token names a leg or test file listed in that unit's own §7. It would have caught the missing leg here, and it is a pure join over two sections of one document.

### D4 — HIGH — unit 3 S3 against S4 and AC6: `OVERAGE` is a dead vocabulary member

S3 produces `OVERAGE` "when the rate cannot be computed". S4 and AC6 give `cpu_s = None` the verdict `UNKNOWN`, "never folded to zero and never labelled IDLE". On a flagged row (`age_s > ceiling > 0`) the divisor cannot be zero, so `cpu_s = None` is the only input where the rate is uncomputable — the two scope items hand one input two verdicts, and AC6 settles it as `UNKNOWN`. No AC produces or observes `OVERAGE`.

AC1's closed-set arm asserts "exactly the six members S1 names" and passes on a vocabulary whose sixth member nothing can emit: a criterion satisfied by the spelling of the enum rather than by any behaviour. Unit 4's `reap-all` mode then kills "every flagged row", inheriting a verdict whose semantics nobody defined.

**Fix.** Name the condition `OVERAGE` actually covers — a flagged row whose rate IS computable and which is neither ORPHAN nor above the spin rate, if that is meant to be distinct from IDLE — and give it its own AC with a named arm. Otherwise delete it from S1's vocabulary and from AC1's count.

**Left-shift gate.** An arm asserting every member of the closed verdict vocabulary is produced by at least one staged fixture in the test file. Vocabulary coverage, not spelling: it is the same shape as the collection gate that asserts every test file contributes ≥1 collected item.

### D5 — HIGH — unit 3 §3 Edges against `order 3`, with S5/AC7

`memory/TEMPLATE-SPEC.md` defines the field: units sharing a value are the parallel group. Units 2 and 3 both carry `order 3` and are the whole group; the generated table in `memory/builds/aReapedSpinner/README.md` shows step 3 as `TOOL-aReapedSpinner-2, TOOL-aReapedSpinner-3` with Parallel = yes. Yet unit 3 declares `consumes-from TOOL-aReapedSpinner-2`, and its S5/AC7 require `classify.py --report` to print "the scoped size" — a figure only unit 2's `scope.py` can produce, since unit 3's non-goals forbid it from re-deriving scope.

`memory/guides/BUILD-METHOD.md`'s `parallel-when-disjoint` clause 2 forbids exactly this: neither pass may depend on the other's output, "as a contract… or as an acceptance input". Unit 3's acceptance input is unit 2's output. The asymmetry is visible in the set: unit 4 consumes the same two and sits at `order 4`.

Unit 4's S5 also declares the same census→fence→classify chain under `--sweep`. If both S5s stand, that chain is built twice with no contract between them.

**Fix.** Give the chain one owner — unit 4's `--sweep` — and reduce unit 3's `--report` to grading rows handed to it. If AC7 keeps the scoped count, move unit 3 to `order 4` and unit 4 to `order 5`, and say which in §3 Edges.

**Left-shift gate.** A `gen_build_index.py` arm: a `consumes-from` edge between two units sharing an `order` value is a refusal. The data to check it is already parsed for the order table — this is a predicate over rows the renderer holds.

### D6 — HIGH — unit 7 §4 Detection against AC3 and AC6

§4 states detection as a closed pair — "presence of `tools/process-monitor/reap.py` AND a readable `.process-monitor.conf`" — and says it resolves once, before the first leg is dispatched, so the announcement in S3 is printed with the profile line rather than at kill time. AC3 requires the announcement for a monitor that is absent OR REFUSING to appear with the profile line, and §5 makes "present but refusing" a distinct announced state.

AC6's refusing case is a non-blank `PROCMON_ROOTS` that does not admit the scratch root. There, the conf is readable and `reap.py` is present, so the declared predicate passes and the refusal can only surface mid-kill — the state §4 itself calls "reporting a monitoring fault as a gate fault". The same section concedes the path ("the reaper refuses every leg pid and the runner falls back — correctly, but silently unless S3 speaks"), contradicting its own profile-time claim. No unit ships a roots-admission probe: unit 2's only diagnostic verb is `scope.py --explain <pid>`, which needs a live pid.

**Fix.** Extend §4 Detection to a third condition resolved at profile time — grade the runner's scratch root (the `TMPDIR`/`mktemp -d` parent it will use) through unit 2's fence once, before dispatch, and treat a refusal as the announced fallback. Declare that probe in unit 2's §2, since it needs a path-mode entry point rather than a pid one. State the condition in unit 7's S2 and re-word AC3 to observe it.

**Left-shift gate.** An arm in the runner's canary that sets `PROCMON_ROOTS` to a root excluding the scratch dir and asserts the fallback line appears in the profile output, before any leg runs.

### D7 — HIGH — unit 4 AC6: the byte-identity criterion is unsatisfiable as written

S1 has `run_kill` return the killed set and the survivor set separately; S2 makes the survivor set derive from a SECOND census read, never from the kill's exit status; §5 repeats that both sets are printed separately. AC6 then demands the `--dry-run` stdout be "byte-identical to the non-dry run's except for its mode banner".

After a real sweep the re-read shows zero survivors. After a dry sweep the staged tree is alive, so its re-read shows every member as a survivor. The two runs' survivor lines cannot be the same bytes unless the dry path skips the verification the whole unit is built on — which is precisely the divergence AC6's Red-when exists to forbid. (The pid half is soluble by running dry then real against one staging; the killed/survivor half is not.) So AC6 will land as a normalized or quietly weakened comparison that still reads as verified, and its real intent — that `--dry-run` takes the same code path — goes unobserved.

**Fix.** Re-word AC6 to what is checkable: the dry run and the real run emit the same WALKED set and the same per-pid lines with pids normalized; the dry run's survivor set equals its walked set; the staged tree is alive afterwards. Add a separate structural assertion — one shared function, one `dry` flag — rather than a byte comparison of two runs.

**Left-shift gate.** No generic gate fits; this one is a review class. Add it to the build's own recurring-class list: an AC asserting byte-identity between two runs of a program whose output derives from live state is a finding, because the comparison will be relaxed at implementation time and nobody re-reads the criterion afterwards.

### D12 — HIGH — unit 4 §10 Reuse audit: the rejection ground is false

The audit rejects the nearest seam because `run-gates.sh` "kills only pids it recorded, so it cannot reach a grandchild", explicitly "verified against source at BASE". At BASE, `:445-468` is `remove_descendants`: it snapshots `ps -ef` at `:447`, iterates `scan_descendants` — a depth-8 ppid walk — and SIGKILLs every member at `:451`, then re-reads with `kill -0` at `:466-468` and reports survivors. The header the audit cites continues at `:416-417` with the opposite of what the audit says it says. The secondary ground ("extending it would mean giving the gate runner a process-table reader") is false too: it already has one at `:447`.

So the corpus already holds a walk-kill-verify mechanism, and this unit re-derives it while inheriting none of that mechanism's four recorded corrections — the snapshot taken before any kill because killing a parent reparents its children (`:419-421`), the numeric field guard (`:432-436`, and see D13), the depth-8 bound (`:429`), and the survivor report that carries the walk's only liveness assertion (`:453-470`, corrected in `TOOL-aQuenchedHarness-7`).

**Fix.** Re-run the audit against `run-gates.sh:428-474`. State which of that walker's properties this unit genuinely adds — leaves-first ordering, verification by re-read as a return value rather than a message, the scope fence, no depth cap — and why those cannot be added to the existing function instead. Inherit the four corrections explicitly, by id.

**Left-shift gate.** The citation-resolution arm proposed under D10 covers the mechanical half. The judgement half belongs in the spec template: a §10 rejection of a named seam quotes the sentence it relies on, so a wrong reading is visible to a reviewer without opening the file.

### D14 — HIGH — unit 1 §10 Reuse audit: "it reads no process table at all"

The audit's nearest-prior-art sentence — `run-gates.sh:412-414` "is a statement of this problem rather than a seam… and it reads no process table at all" — is contradicted by `ps -ef > "$snap"` at `:447`, inside the same function block the audit is describing, in a file the audit claims to have verified at BASE. The sentence dismisses the corpus's only process-table reader: the one carrying the column assumptions, the `$2`/`$3` numeric guard and the depth-8 bound that unit 1's parser and AC1 row contract both lack.

**Fix.** Correct §10 to name `scan_descendants`/`remove_descendants` as a live process-table reader, and state which of its parsing decisions unit 1 adopts and which it deliberately differs from — in particular whether the `ps -ef` column contract is shared or re-derived.

**Left-shift gate.** Same citation-resolution arm as D10. A stronger variant, worth the cost here: when a §10 audit says "no X exists", require the negative to name the search that produced it (the `reuse_lookup.py` query is already recorded; the grep is not).

---

## Medium

### D3 — MEDIUM — unit 2 S6 against AC6 and AC7: the scope-to-acceptance join is off by one

Every sibling pointer is correct (S2→AC1/AC2, S3→AC3, S4→AC4, S5→AC5), then S6 (`scope.py --explain <pid>`) says "Observed by AC6" — but AC6 is `test_root_that_claims_everything`, the minimum-length refusal, and the explain criterion is AC7. From AC6 on the map is wrong by one: AC7 is claimed by no scope item, and AC6 — the mitigation §5 names for this unit's top risk, an over-broad declared root — is owned by no scope item either, its behaviour appearing only in §4 consequence 1.

`check-memory-hygiene.sh`'s scope-join arm (`SCOPE_JOIN_CUTOFF`, `TOOL-aJoinedCanon-3`) only asserts that each §2 item names some `AC[0-9]` token, never that the referenced criterion exists or is the right one, so this passes silently. The practical risk is small but real: a builder working from §2 can land every scope item and still fail AC6, and a later reviser can drop AC7 as an extra without noticing S6 loses its only observation.

**Fix.** Re-point S6 at AC7, and add a scope item owning the minimum-length / root-claims-everything refusal that AC6 grades (or fold it into S4's refusal and point S4 at both).

**Left-shift gate.** Extend the existing scope-join arm in both directions: the referenced AC number must exist in §6, and every AC must be claimed by at least one §2 item. Both are one-line predicates over data that arm already parses, and the reverse direction is the one that catches an orphaned criterion.

### D15 — MEDIUM — unit 3 S3 against §4 and AC4: three statements of the ORPHAN predicate disagree

S3 flags ORPHAN when the ppid "names no live process in the census". §4 says "a ppid of 1 is treated as dead by definition". AC4 reds when "liveness is inferred from `ppid != 1` alone", and requires a flagged row whose ppid names a LIVE census row to be NOT ORPHAN. On the POSIX backend unit 1 S3 ships, pid 1 is a live census row — so a reparented orphan is simultaneously not-ORPHAN (S3, AC4) and ORPHAN (§4).

No criterion stages `ppid = 1`: AC3 stages a ppid naming no row, AC4 a live non-init parent. The disputed case is the reparented-orphan population the kit was opened for, `reap-orphans` is the resolved default mode, and the reading therefore decides whether the default kills anything at all.

**Fix.** State the predicate once — "ppid absent from the census OR equal to 1" — and give it its own arm staging `ppid = 1`. Delete the §4 and AC4 wording that contradicts it.

**Left-shift gate.** The vocabulary-coverage arm proposed under D4 extends to cover this: every verdict has a producing fixture, and the ORPHAN fixture set must include both the absent-ppid and the `ppid == 1` cases. A predicate stated three times in one document is otherwise only catchable by reading.

---

## The four questions the audit was asked

**(a) Are the §3 edge declarations consistent in both directions across the seven?** No. Unit 3 declares `consumes-from TOOL-aReapedSpinner-2` while sharing that unit's `order` value (D5). Unit 7's dependency on unit 2's fence is real but undeclared as a mechanism — §4 requires a roots admission it never asks unit 2 to build (D6). Unit 6's descriptor declares a dependency on unit 1's file through `version_from` without any edge saying so (D1). The remaining edges (1→2, 1→3, 1/2/3→4, 4→5, 4→7) are consistent in both directions.

**(b) Does any acceptance criterion rest on a mechanism no unit builds?** Four. Unit 6 AC1/AC6 rest on a version marker no unit mints (D1). Unit 7 AC3/AC6 rest on a profile-time roots-admission probe no unit ships (D6). Unit 4's §4 rests on an unnamed signalling mechanism that the resolved interpreter cannot provide (D8). Unit 1's AC1 row contract rests on a numeric guard nothing requires (D13).

**(c) Is the declared ordering satisfiable?** Not as written. It fails at the first step: unit 6 at `order 1` cannot land green (D1). It fails again at step 3, where units 2 and 3 are declared parallel while unit 3 consumes unit 2's output as an acceptance input (D5). Steps 4, 5 and 7 are satisfiable once those two are repaired, and the 5/7 parallel pair is genuinely disjoint.

**(d) Is any criterion written so it cannot fail?** Four. Unit 7 AC1 passes against the unchanged runner (D10). Unit 6 AC4's observer cannot read the property AC4 states (D2). Unit 3 AC1's closed-set arm passes on a vocabulary with a dead member (D4). Unit 4 AC6 is unsatisfiable and will therefore be implemented as something weaker that still reads as verified (D7). A fifth, unit 1 AC1's row contract, is satisfiable by a garbage row (D13).

## Sequencing note for the fix pass

D1, D5 and D10 are ordering defects and should be repaired first, together, because they change which units exist at which step. D8, D9, D11 and D13 are the safety cluster and are all unit 1/2/4 spec edits — repair them as one pass, since D9's inheritance rule and D11's path-matching rule interact and D13 is a precondition for both. D2, D3, D4, D6, D7, D12, D14 and D15 are independent and can be repaired in any order.
