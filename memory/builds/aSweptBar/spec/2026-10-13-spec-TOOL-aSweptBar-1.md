# TOOL-aSweptBar-1 — stale suite fixtures re-armed against the code the bar-less landings left

**Status:** SPECCED · rev-1 · 2026-10-13 · node a · Tier-1 · base 53b25884 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aSweptBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-aSweptBar-1-brief.md) | research | TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6 |

<!-- /gen:spec-records -->

## 1. Goal

Nine suites read red over local main `53b25884` because a landing moved the code under an arm and no
bar ran. Each red is a stale fixture or a stale pin, not a product defect. This unit re-arms each arm
against the code as it stands, so it goes green and reds again on its own staged break.

## 2. Scope (IN)

- **S1** — transition-audit AC11: the sed at `tools/memory-tree/transition-audit.test.sh:503` takes a
  space between `-n` and its script. Observed by AC1.
- **S2** — unattended-build F2: the refusal set at `tools/workflows/unattended-build.test.sh:1036`
  is derived from the `check_run_state` calls inside each `verb_*` body of the driver, and the
  comment above it names `check_run_state` instead of `fail 4N`. Observed by AC2.
- **S3** — agent-cap no-regress: `buildPayload` in the suite's `nr.js` gives every payload a `cwd`
  of the resolved fixture directory, which no checkout holds. Observed by AC3.
- **S4** — manifest-check AC4: the node arm at `skills/session-kickoff/manifest-check.test.sh:921`
  expects `node — a · daily-agent @ COMPEETO-AGENT`. Observed by AC4.
- **S5** — the unattended driver suite roots its two harness tallies and its two namespace snapshots,
  `harness-fns.sourced` and `harness-fns.now`, under `$TMP/.git/`. Observed by AC5.
- **S6** — run-gates run-log AC4: the arm admits exactly one exec beyond the baseline, the `cat` the
  writer keeps on purpose, and the suite header's AC4 line says so. Observed by AC6.
- **S7** — run-gates run-log AC8 EXITS: the exit table gains one exempt row for each of the three
  exits inside the runner's `REUSE_DIGEST=$( … )` substitution. Observed by AC7.
- **S8** — runlog selftest: the newest RAISED block above `ASSERTION_FLOOR` at
  `tools/runlog/selftest.py:331` gains its arithmetic line, `# 1 + 1 = 2`. Observed by AC8.
- **S9** — memory-hygiene self-test: `_pyexempt` names `GIT_INDEX_FILE`, and the environment line of
  the comment above it names it with its reader. Observed by AC9.
- **S10** — govkit selftest: the `ORDER|project-owned` pin at `tools/govkit/selftest.py:6385` moves
  from 32 to 34, with a ledger line above it naming the two rows and the landings that added them.
  Observed by AC10.

## 3. Non-goals (OUT)

- No product code. The driver, the hooks, the runner, the hygiene engine and govkit stay as they are;
  every red here is its suite's.
- The verbs that refuse through a `run_*` function rather than a `verb_*` body, such as `--hold`,
  `--handoff` and `--settle`, stay outside F2's derivation, as the brief scopes it. A reading of the
  dispatch table would cover them; that is a follow-up, and the attended prompt names none today.
- The kit-path literals in `tools/hooks/agent-cap.test.sh` belong to `TOOL-aSweptBar-4`. The fork
  idioms in `tools/run-gates/run-gates.runlog.test.sh` and `tools/workflows/unattended-build.test.sh`
  belong to `TOOL-aSweptBar-5`.
- The roles reds stay aOrientedCast's. That includes govkit selftest's `OC8 AC4` arms and its
  `re-stamps the receipt at the new commit` arm, which the bar log shows beside a roles render that
  failed. That attribution is UNVERIFIED; if the arm still reds once aOrientedCast lands, it returns
  to the main loop.
- The unattended kit gate's check 9 reds on remote tips this clone never fetched. That is a fetch,
  not a fixture.

## 4. Design

Every edit is inside a suite or a suite's pin, and each restores what the arm's own comment says it
observes.

**S1.** `sed -n's/…/p'` hands GNU sed the option cluster `-ns/…`, which it refuses with its usage
text, so `after` is empty and AC11 compares a real `delta()` result with nothing. TOOL-aSparedSpawn-8
fused the flag. The fix is one space.

**S2.** TOOL-aSparedSpawn-14 folded every no-run-state refusal into `check_run_state`
(`tools/unattended/unattended.sh:798`), whose message is `fail 10 "no run-state file…"`, so the
arm's `fail 4[0-9]` predicate matches nothing and F2 derives 0 verbs. The awk opens a body on a
`^verb_[a-z_]+()` line, turns the verb's underscores into dashes, closes the body on any other
function definition, and prints `--<verb>` at the first `check_run_state "` line inside an open body.
The underscore class admits `verb_record_set` and `verb_record_piece`, which refuse the same way
and dispatch as `--record-set` and `--record-piece`; the brief's count of 13 is the `[a-z]+` reading,
which stops at the underscore. The close on any other definition is load-bearing: without it, the
open `verb_list` body runs into a later helper's call and prints a stale `--list`, observed at spec
time. The arm's floor of three and its absence loop stay as they are. `tools/workflows/unattended-unit.js`
lines 236-247 name `--dispatch`, `--brief` and `--rescope` in the attended text but never with the
slug after them, so every absence needle still holds over the wider set.

**S3.** Rule 6 (TOOL-aOrientedCast-7) refuses every inline Workflow script once the payload's
checkout holds `.claude/roles.json`. `nr.js` sends no `cwd`, so the hook falls back to
`process.cwd()`, which is this checkout, and every denial the property needs to ratify is a rule 6
denial instead: the bar log reads `84 denied at BASE, 0 denial(s) lost, 0 ratified`. With `cwd` set
to `path.resolve(fixdir)` and `CLAUDE_PROJECT_DIR` already unset at the suite's line 9,
`resolveRoleRoot` finds no checkout and rule 6 stays unarmed. Rule 0 reads only `args`, which these
payloads lack, so the property compares rules 1 to 5 with BASE `d65da7ab`, which predates rule 6.
The parity mode shares `buildPayload`, so both modes send one shape. Unmasking rules 1 to 5 can surface
a denial that rule 6 has hidden since it landed. Such a loss is a finding for the main loop, never a
reason to keep the payload as it was.

**S4.** The card prints the whole Machine/user cell that matched, by equality or by the `<user> @`
prefix (`skills/session-kickoff/manifest-check.sh` line 374). The v4.0 registry's node-a cell is
`daily-agent @ COMPEETO-AGENT`, so the expected literal takes the whole cell. The arm's skip on any
other user stays.

**S5.** `TMP` is the fixture repository's work tree (`git init` at line 200). The tallies at lines
550-551 and the snapshot at line 556 are untracked files in it, so the first `run` of an arm dirties
the tree and `--preflight` refuses check 2, naming `harness-proc.tally`. Every `reset_tree` also
`git clean`s them away, which empties the namespace arm's source file. Under `$TMP/.git/` neither
happens, which is where line 818 already keeps `askstub` for the same reason. The tail's
`harness-fns.now` moves with its pair, so both sides of the namespace compare stay in one place.

**S6.** `write_runlog_verdict` appends its line through `printf … | cat >>`, one write per line,
because two concurrent bars tore lines without it (TOOL-aPairedSlots-7). The arm compares the
writer's post-leg exec list with a baseline copy that never calls the writer, so it reds on that `cat`
by construction. The arm keeps both traces and asserts the difference is exactly `cat ` and the
count exactly one more, in the `comm -13` shape the mkdir arm beside it already uses. Line 23 of the
header reads that the writer adds one sanctioned exec, its `cat`.

**S7.** The three exits sit at `tools/run-gates/run-gates.sh` lines 3349, 3357 and 3367, below the
`trap cleanup EXIT` line at 2529, and each exits the command substitution's subshell, which runs no
trap of the runner's. The first came with TOOL-aSparedSpawn-1 and the other two with
TOOL-aSparedSpawn-33. Each row is the trimmed line text, a count of 1 and the reason
`exempt: the reuse digest's $( … ) substitution, from TOOL-aSparedSpawn-1 and TOOL-aSparedSpawn-33,
which runs no trap of the runner's`, in the shape of the wall watcher's rows. The arm-join loop
already skips `exempt:` rows. The staged and control arms red today only because they read the same
three unknown exits, so they clear with the rows.

**S8.** The record AC2 arm reads the last `<a> + <b> = <n>` line inside the newest RAISED block and
wants its sum equal to the move. TOOL-aHeardState-8's block names two checks and no sum. One line,
in the predecessors' form.

**S9.** `gen_build_index.py:903` carries `GIT_INDEX_FILE` from `os.environ` into the hook's git
environment, which the example-conf arm reads as a dict key the example conf does not declare. It is
the environment, the same class as `GIT_DIR` and `GIT_GRAFT_FILE`, so it joins `_pyexempt` in sorted
position and the comment's environment line, with TOOL-aTrimmedHook-4 as its source.

**S10.** A default `plan` into a scratch target, run at spec time over `53b25884`, previews 34
`ORDER [project-owned]` rows. The two that arrived after the pin are run-gates'
`windows-only-legs.txt` (TOOL-aSparedSpawn-5 S3) and the hooks kit's `format-guard.test.sh`
(TOOL-aHeardState-1). Neither landing is an ancestor of the pin's commit `15588db9`, and no
`project-owned` rule left a default kit between the two trees, so 32 + 2 = 34. The ledger line follows
its predecessors: the move, both landings, both rows, and the date of the measurement.

### Files touched (estimate)

- `tools/memory-tree/transition-audit.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/hooks/agent-cap.test.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `tools/unattended/unattended.test.sh`
- `tools/run-gates/run-gates.runlog.test.sh`
- `tools/runlog/selftest.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/govkit/selftest.py`

### Alternatives rejected

- S2 keeping the `[a-z]+` verb class: it drops `--record-set` and `--record-piece`, which refuse
  exactly as the other verbs do, so two absence arms would be missing by accident of spelling.
- S3 exporting a `CLAUDE_PROJECT_DIR` under no checkout: the payload `cwd` is the hook's first input,
  so a payload that carries one does not depend on where the suite or the bar happens to run.
- S4 deriving the expected cell from `AGENTS.md` at run time: the arm would compare the card with a
  second reading of the registry the card reads, which is two generated answers compared.
- S6 counting execs and allowing one more of anything: that admits a different exec in place of
  `cat`, which is the regression the arm exists to see.

## 5. Acceptance criteria

- **AC1** — When `sed -n 503p tools/memory-tree/transition-audit.test.sh` runs, the expression reads
  `sed -n 's/^entry`. Applied to `entry 0cc07741 · TOOL-aSeed-1 · changed · cc4db6cf · ok`, the line
  shape `tools/memory-tree/transition_audit.py:946` prints, it prints `TOOL-aSeed-1|changed|cc4db6cf`.
  Red when: `-n` is fused to the script again and sed prints its usage, so `after` is empty.
- **AC2** — When the F2 awk program is run alone over `tools/unattended/unattended.sh`, its output
  holds `--status`, `--record-set` and `--record-piece`, holds no `--list`, and is at least the arm's
  floor of three lines. Red when: it keys on `fail 4N` and derives nothing, or a body is left open
  across a non-verb function and prints a stale `--list`.
  figure: DERIVED from the driver at observation.
- **AC3** — When `node tools/hooks/agent-cap.js` reads, with `CLAUDE_PROJECT_DIR` unset, a `Workflow`
  payload whose script is the suite's `seq-marked-bounded.js` fixture and whose `cwd` is a directory
  under no checkout, it exits 0. The same payload with every `gov:sequential-agents` token removed
  exits 2, and the BASE hook from `git show d65da7ab:tools/hooks/agent-cap.js` exits 2 on the marked
  one. Red when: the payload carries no `cwd`, the hook reads this checkout's `.claude/roles.json`,
  and rule 6 denies the marked fixture, so nothing is ratified.
  fixture: the three payloads were built and observed at spec time over `53b25884`.
- **AC4** — When `grep -n 'daily-agent' AGENTS.md` reads node a's registry row, its Machine/user cell
  is `daily-agent @ COMPEETO-AGENT`, and `sed -n 921p skills/session-kickoff/manifest-check.test.sh`
  expects `node — a · daily-agent @ COMPEETO-AGENT`. Red when: the expected string stops at the user
  and the card's whole cell does not equal it.
- **AC5** — When `grep -n 'harness-' tools/unattended/unattended.test.sh` runs, every tally and
  snapshot path it lists roots at `$TMP/.git/`. In a scratch repository, a file written under `.git/`
  leaves `git status --porcelain` empty while one written at the root does not. Red when: a tally
  roots at `$TMP`, the first `run` of an arm leaves `harness-proc.tally` untracked, and `--preflight`
  refuses check 2.
  cost: the suite-level observation is a driver shard, which takes hours on node a; the probe takes
  seconds.
- **AC6** — When `awk '/^write_runlog_verdict/,/^}/' tools/run-gates/run-gates.sh` is piped to
  `grep -c 'cat >>'`, it reads 1, and `grep -n 'AC4 the writer' tools/run-gates/run-gates.runlog.test.sh`
  shows the arm requiring the writer's exec names to be the baseline's plus exactly `cat`. Red when:
  the arm still demands equality and reds on the sanctioned `cat`, or it accepts any other exec in
  that place.
- **AC7** — When `grep -c 'exempt: the reuse digest' tools/run-gates/run-gates.runlog.test.sh` runs,
  it reads 3. Each row's text equals, byte for byte, the trimmed line at
  `tools/run-gates/run-gates.sh:3349`, `tools/run-gates/run-gates.sh:3357` and
  `tools/run-gates/run-gates.sh:3367`. Red when: a row is missing or differs by a byte, and AC8 EXITS
  names that exit as having no row.
- **AC8** — When `grep -n -A4 'RAISED 1578 -> 1580' tools/runlog/selftest.py` runs, the last line of
  the block before `ASSERTION_FLOOR = 1580` is `# 1 + 1 = 2`. Red when: the block states no sum and
  the record AC2 arm reads `None`.
- **AC9** — When `grep -n 'GIT_INDEX_FILE' tools/memory-tree/check-memory-hygiene.test.sh` runs, it
  hits the `_pyexempt` assignment and the environment line of the comment above it. Red when: the
  list lacks the name and the python example-conf arm reports that the example conf does not
  declare `GIT_INDEX_FILE`.
- **AC10** — When `python tools/govkit/govkit.py plan --target <t>` runs into a scratch target whose
  `.governance/deploy.toml` declares no `kits` line, it previews 34 `ORDER [project-owned]` rows,
  among them `windows-only-legs.txt` and `format-guard.test.sh`. Then `sed -n 6385p tools/govkit/selftest.py`
  pins 34, and the ledger line above it names TOOL-aSparedSpawn-5 and TOOL-aHeardState-1. Red when:
  the pin still reads 32 against a plan that previews 34.
  figure: PINNED, measured 2026-10-13 over `53b25884` by that plan.
  fixture: a fresh `git init` target under `%TEMP%/<short-name>`, never inside the worktree.

## 6. Gates

`transition-audit arms` · `unattended-build self-test` · `agent-cap self-test` · `manifest-check self-test` · `run-gates run-log line` · `runlog selftest` · `memory-hygiene self-test` · `govkit selftest` · `scratch-guard self-test` · `pre-push run-log line` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `recall floor arms` · `hook destinations self-test` · `lexicon naming predicates` · `govkit refusal join` · `govkit acceptance matrix`

The unattended driver suite has no row in the manifest. It runs as the self-test tier's
`unattended driver selftest shard <i>/8` rows, so the close observes S5 there.

New arm: tools/memory-tree/transition-audit.test.sh · covers AC1 · fuse `-n` to the AC11 script again and AC11 reds with an empty after · none
New arm: tools/workflows/unattended-build.test.sh · covers AC2 · restore the `fail 4[0-9]` predicate and F2 reds deriving 0 verbs · none
New arm: tools/hooks/agent-cap.test.sh · covers AC3 · drop `cwd` from `buildPayload` and the no-regress property reds with 0 ratified · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC4 · cut the expected cell back to the user and AC4 node reds on node a · none
New arm: tools/unattended/unattended.test.sh · covers AC5 · root the proc tally at `$TMP` again and the first preflight arm of shard 8/8 reds on check 2 · none
New arm: tools/run-gates/run-gates.runlog.test.sh · covers AC6 AC7 · add a second exec to `write_runlog_verdict` and AC4 reds; delete one digest row and AC8 EXITS reds naming its exit · none
New arm: tools/runlog/selftest.py · covers AC8 · delete the `# 1 + 1 = 2` line and record AC2 reads None · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC9 · drop `GIT_INDEX_FILE` from `_pyexempt` and the example-conf arm reds naming it · none
New arm: tools/govkit/selftest.py · covers AC10 · restore the pin to 32 and the ORDER arm reds printing 34 · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft from the build brief, every cause re-read at `53b25884`.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py "re-arm a suite arm a landing disarmed so its staged break reds
again"` returned name-stem neighbours only, such as `arm`, `armed` and `run_arms`, and none of them is
a seam for a fixture edit, so no existing seam fits as a helper and this unit mints none. The seams
it extends are the arms themselves and their neighbours. S5 follows `askstub` at
`tools/unattended/unattended.test.sh:818`. S6 copies the mkdir arm's `comm -13` shape at
`tools/run-gates/run-gates.runlog.test.sh:582`. S7 copies the wall watcher's exempt rows in the same
table. S8 and S10 write into the comment ledgers above their pins. The recall probe returned
TOOL-aWokenSentinel-31, the record of suites held off the bar shipping red through three landings,
which is this build's cause in another build. The brief and the code disagree in one place: the brief
counts 13 verbs for F2, and the driver holds two more under an underscore, which §4 takes.

Recall terms used: `python tools/memory-recall/query.py "why did suite arms go red after landings
merged without a bar, and which fixture or helper re-arms them" --terms "bar-less landing stale
fixture arm disarmed probe marker WHOLE_RUN cover pass gate-bar-green reuse digest GATE_FULL key"`
