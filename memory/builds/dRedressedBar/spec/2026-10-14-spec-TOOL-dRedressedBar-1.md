# TOOL-dRedressedBar-1 — stale suite fixtures re-armed against the code the bar-less landings moved

**Status:** SPECCED · rev-1 · 2026-10-14 · node d · Tier-1 · base ebce889c · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md) | research | TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 |

<!-- /gen:spec-records -->

## 1. Goal

Five suites read red in the full bar with self-tests over local main `ebce889c`. In each, a landing
moved the code under an arm, or the bar's own environment reached an arm, and no bar ran to see it.
Every red is the suite's own, not a product defect. This unit re-arms each arm against the code as it
stands, so it grades its subject again and reds again on its own staged break.

## 2. Scope (IN)

- **S1** — unattended-build GH33: each of the 13 calls that glue a unit id to its authored JSON,
  such as `build_gh33_writer A-tB-1'["A-tB-1"]'`, takes a space between the two words, at
  `tools/workflows/unattended-build.test.sh` lines 2471, 2483, 2496, 2503 and 2512. Observed by AC1.
- **S2** — tier2-review prelude: the extraction at `tools/workflows/tier2-review.test.sh:70-79` stops
  on the line after the `}` that closes the `if (!baseLooksPinned)` ladder, found from the
  `const baseLooksPinned` line, instead of at `const reviewDir = a.reviewDir`. Each anchor keeps its
  die, and the three-needle liveness die stays as it is. Observed by AC2.
- **S3** — run-gates turnstile arm 44: the `sed` at `tools/run-gates/run-gates.turnstile.test.sh:1500`
  routes the builtin pid read `IFS= read -r hpid < "$d/pid"` through `read_pid_and_swap "$d"`. The
  reader at line 1501 reads the pid into `hpid` with the same builtin and then swaps the nonce. The
  routed-count assertion of 2 stays. Observed by AC3.
- **S4** — pre-push: `.githooks/pre-push.test.sh` unsets `GATE_SELFTESTS` once, beside the suite's
  other environment pins at lines 109-118. The comment says why: it is an input to predicate 8 and the
  bar exports it. Observed by AC4.
- **S5** — foreign-prefix parity: `tools/roles/adopt-roles.test.sh` takes the probe stop its sibling
  suites carry, after arm 1's last assertion at line 83 and before arm 2. It reads this suite's own
  counters, `fail` and `n`. Observed by AC5.

## 3. Non-goals (OUT)

- No product code. The build harness, the review harness, the runner, the pre-push hook and the roles
  adopter stay as they are. Every red here is its suite's.
- No floor moves. No arm is added or removed, so `FLOOR_ASSERTIONS` in each touched suite stays.
- No `WHOLE_RUN` row for `roles adopter self-test` in `tools/run-gates/foreign-prefix.gov.test.sh`.
  The suite is a shell suite whose arms are separate blocks, so a probe stop can sit between them.
  The declared whole runs are `--selftest` modes and the one node-process suite.
- No lexicon kit in the pre-push fixtures, and no arm reading past the merge-loss skip line. The
  brief offered both remedies; §4 S4 says why the cause is elsewhere.
- No conversion of the fork idioms in `tools/workflows/unattended-build.test.sh`, which belongs to
  `TOOL-dRedressedBar-5`. No edit to `tools/roles/adopt-roles.test.sh` line 228, which belongs to
  `TOOL-dRedressedBar-4`, and no new adopter arm, which belongs to `TOOL-dRedressedBar-6`.
- No kit version bump for the bytes moved here; `TOOL-dRedressedBar-7` measures that over the
  finished tree.

### Edges

- **hands-off** `TOOL-dRedressedBar-6` — `tools/roles/adopt-roles.test.sh` carries the probe stop
  after arm 1, so arms that unit appends run only in a whole run.
- **hands-off** `TOOL-dRedressedBar-7` — the moved suite bytes, `.githooks/pre-push.test.sh` among
  them, are part of the tree that unit measures.

## 4. Design

Every edit is inside a suite, and each one restores what the arm's own comment says it observes.

**S1.** TOOL-aOrientedCast-27 made `build_gh33_writer` take `<unit id> <authored-json>`, a label
`tB · <id> · spec-write` and the authored list as `$2`
(`tools/workflows/unattended-build.test.sh:2460-2463`). Every call site still passes one word, so
under `set -u` the function aborts with `$2: unbound variable` at line 2462. All 26 failures in the
bar log are GH33 arms. The one call already spaced, `build_gh33_writer B-tB-1 '[]'` at line 2496,
is the shape the other 13 take. The double the run reads keys on the whole label first
(`run_wf` at line 190), and the build harness renders that label as `[slug, scope, stage]` joined by
` · ` (`tools/workflows/unattended-build.js:542-544`), so the spaced calls address the writers the
script spawns.

**S2.** TOOL-aOrientedCast-27 moved `const reviewDir = a.reviewDir` from below the base-shape ladder
(line 529 before it) to `tools/workflows/tier2-review.js:290`, above `badSubject` (`:357`) and
`baseLooksPinned` (`:534`). The extraction still stops at `reviewDir`, so the body holds neither
validator, the needle die fires, and 0 of the 322-assertion floor runs. The brief reads
`baseLooksPinned` as resolving nowhere; it is at `:534`, below the stop. The comment at
`tools/workflows/tier2-review.test.sh:68-69` already states the intended stop, the line after the
ladder. The new stop is the index of the first line equal to `}` after the `const baseLooksPinned`
line, plus one. That is a code anchor, not a comment anchor. Measured at spec time over `ebce889c`, the
ladder opens at line 534 and closes at 543, the body is lines 15 to 543 and holds all three needles,
an empty spec-audit subject list throws `reviews nothing`, and a round-2 `base` of `main` throws
`must be an immutable sha`. The die at line 73 names the new anchor.

**S3.** TOOL-aSweptBar-5 replaced `cat "$d/pid"` in `ts_try_reap` (`tools/run-gates/run-gates.sh:1735`)
and `scan_dead_docs_beacons` (`:1553`) with `hpid=""; { IFS= read -r hpid < "$d/pid"; } 2>/dev/null`.
The arm's `sed` still matches the `cat` spelling, so the routed count is 0 and both functions read
an unswapped nonce and remove the beacon. The new substitution is
`s|IFS= read -r hpid < "\$d/pid"|read_pid_and_swap "$d"|`, and the reader becomes
`read_pid_and_swap() { IFS= read -r hpid < "$1/pid"; printf 'successor' > "$1/nonce"; }`. Bash's
dynamic scoping writes the caller's local `hpid`. Probed at spec time over the arm cut out alone: the
old routing reads `routed=0`, with the slot reaped and the beacon swept. The new routing reads
`routed=2`, and both nonces read `successor`.

**S4.** The brief traced the eleven arms to the merge-loss skip line at `.githooks/pre-push:952`. The
bar log disagrees. That skip line is only the first line of `$_out`, which each failing arm prints whole
after `got:`. The arms read the decision line through `read_rp_line` (line 994), and the decision the
log shows is `FULL gate on main push … this push runs the kit self-tests and the recorded full green
was earned with them HELD`. That is predicate 8 (`.githooks/pre-push:1530-1531`), which forces FULL
whenever `GATE_SELFTESTS` is set and the planted record carries no `selftests 1`. The bar exports
`GATE_SELFTESTS`, so every RP arm and the TOOL-aSparedSpawn-33 AC1 arm took the forcing case. The
suite already names the class at line 255, and nineteen lines clear the variable one call at a time.
`run_rp_push` (line 991), the RP AC15 push at line 1036, and the three dg steps at lines 1222, 1226
and 1229 do not. One `unset GATE_SELFTESTS` at the top closes the class for every arm, these and
any later one. The arms that set it explicitly, such as line 274's `GATE_SELFTESTS=1` push, keep
their own value. No arm reads an inherited value.

**S5.** `foreign-prefix parity` runs every self-test row with `FOREIGN_PREFIX_PROBE=1` and reds a
probe row that prints no `foreign-prefix-probe: stopped after 1 arm`
(`tools/run-gates/foreign-prefix.gov.test.sh:453-456`). The roles adopter suite was added by
aOrientedCast without one. The line is the siblings' line, as at
`tools/agent-instructions/adopt-agent-instructions.test.sh:18-19`, with this suite's counter names:
`fail` for failures and `n` for assertions, as `check_arm` keeps them (line 65). Arm 1 builds its
own fixture and runs the adopter, so the probe touches the subject.

### Files touched (estimate)

- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/tier2-review.test.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `.githooks/pre-push.test.sh`
- `tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- S2 anchoring the stop on the comment line after the ladder,
  `// \`diffCmd\` is built AFTER the resume probe now`: a comment can be reworded with no code moving,
  and the extraction would then die for a reason unrelated to the code under test.
- S3 restoring a `cat` read in the runner so the old `sed` matches: a product edit to suit a fixture,
  and the shell-hygiene leg counts that fork.
- S4 clearing `GATE_SELFTESTS` at each of the five unguarded call sites: it leaves the class open for
  the next arm written without the clear, which is how these five were written.
- S4 installing the lexicon kit beside the RP fixture: the merge-loss check would then grade the
  fixture's pushes, and the decision would still be forced FULL by predicate 8.
- S5 a `WHOLE_RUN` row: it would run all thirteen arms at three prefixes on every bar, and the
  reason the declared rows carry does not apply to a shell suite.

## 5. Acceptance criteria

- **AC1** — When `grep -c "build_gh33_writer [A-Z]-tB-[0-9]'" tools/workflows/unattended-build.test.sh`
  runs, it reads 0, and the same pattern with a space before the quote reads 14. When the function
  alone is cut out with `sed -n '/^build_gh33_writer()/,/^}/p' tools/workflows/unattended-build.test.sh`,
  evaluated under `set -u` and called as `build_gh33_writer A-tB-1 '["A-tB-1"]'`, it prints
  `"tB · A-tB-1 · spec-write":{"authored":["A-tB-1"],"alreadyPresent":[],"refused":[],"summary":"s"}`.
  Red when: a call glues the id to its JSON again and `set -u` aborts with `$2: unbound variable`.
- **AC2** — When the extraction block, cut out with
  `sed -n '/^const metaEnd/,/^ck(true/p' tools/workflows/tier2-review.test.sh`, is evaluated by `node`
  over the lines of `tools/workflows/tier2-review.js`, with `die` and `ck` stubbed to print, it prints
  the `the prelude extraction is live` line and no die message. The body it builds, run with an empty
  spec-audit subject list, throws a message holding `reviews nothing`.
  Red when: the stop is the `const reviewDir = a.reviewDir` line and the stub prints the die naming
  `badSubject`.
  figure: DERIVED from `tools/workflows/tier2-review.js` at observation; 529 lines at `ebce889c`.
- **AC3** — When the arm-44 block, cut out with
  `sed -n '/^# ---- 44:/,/^# ---- 45:/p' tools/run-gates/run-gates.turnstile.test.sh`, runs alone
  with `HERE` set to `tools/run-gates`, `tmp` set to a scratch directory, and `ok` and `nope` defined
  as `echo`, it prints `survived the reap` and `survived the sweep`, and `$tmp/reap44/routed` reads 2.
  Red when: the `sed` still routes `cat "$d/pid"`, the routed count reads 0, and both beacons are
  removed.
- **AC4** — When `grep -n '^unset GATE_SELFTESTS' .githooks/pre-push.test.sh` runs, it prints exactly
  one line, numbered below the first `git push` line that `grep -n 'git push'` finds, so it precedes
  every push the suite makes. In a scratch clone of the RP
  fixture shape, with the hook installed and a planted full green carrying no `selftests` field, a
  push decides `scoped gate on main push` with `GATE_SELFTESTS` unset and
  `FULL gate on main push` with it set to 1.
  Red when: the unset is removed and the RP arms, run under the bar's exported `GATE_SELFTESTS`, read
  the forced FULL decision again.
  fixture: the probe builds its remote and work repositories under `%TEMP%/<short-name>`, never
  inside the worktree.
- **AC5** — When `grep -n 'FOREIGN_PREFIX_PROBE' tools/roles/adopt-roles.test.sh` runs, it prints one
  line between the `# ---- arm 1` and `# ---- arm 2` headers, and that line prints
  `foreign-prefix-probe: stopped after 1 arm` and reads `fail` and `n`.
  Red when: the line is absent and the parity leg reports the roles row as an undeclared whole run,
  or it reads `pass`, which this suite never sets, so the probe always reports 1 assertion.

## 6. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `run-gates turnstile` · `pre-push self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `roles adopter self-test`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 · glue one GH33 writer call's id to its JSON again and the GH33 arms red on `$2: unbound variable` · none
New arm: tools/workflows/tier2-review.test.sh · covers AC2 · restore the `const reviewDir = a.reviewDir` stop and the runner dies naming `badSubject`, executing 0 of 322 · none
New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC3 · restore the `cat "$d/pid"` substitution and arm 44 reds with a routed count of 0 · none
New arm: .githooks/pre-push.test.sh · covers AC4 · delete the `unset GATE_SELFTESTS` line and run the suite with GATE_SELFTESTS exported as 1; the eleven RP and dg arms red on the forced FULL decision · none
New arm: tools/run-gates/foreign-prefix.gov.test.sh · covers AC5 · delete the roles adopter's probe stop and the parity leg reds `roles adopter self-test` as an undeclared whole run · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-14 · initial draft from the build brief, every cause re-read at `ebce889c`; S2 and
  S4 correct the brief's reading.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py "re-arm a suite fixture a landing disarmed so the arm grades its
subject again"` returned name-stem neighbours only, such as `arm`, `fixture`, `build_fixture` and
`check_arm`. None is a seam for an edit inside an existing arm, so no existing seam fits as a helper
and this unit mints none. The seams it extends are the arms and their neighbours. S2 takes the stop
its own comment at `tools/workflows/tier2-review.test.sh:68-69` names. S3 keeps the arm's
routed-count seam. S4 follows the suite's own `GATE_SELFTESTS` clear at
`.githooks/pre-push.test.sh:255-259` and its environment pins at lines 109-118. S5 copies the probe stop at
`tools/hooks/scratch-guard.test.sh:179-180`, whose shape TOOL-aSweptBar-2 spread to the sibling
suites. The gotchas checklist for these paths selects `fixture-inherits-ambient-machine-state`, which
is S4's class. The recall probe returned TOOL-aSweptBar-1, the same shape of build one day earlier.
The brief and the code disagree twice: S2's `baseLooksPinned` is present below the stop, and S4's
cause is predicate 8, not the skip line.

Recall terms used: `python tools/memory-recall/query.py "why do suite arms go red after a bar-less
landing moves the code under them, and how were they re-armed" --terms "bar-less landing stale
fixture re-armed probe marker WHOLE_RUN GATE_SELFTESTS cleared default-gained verb offender pin"`
