# TOOL-aTrimmedWait-6 — the role gate refuses a role agent's polling wait, and steps past an option cluster such as `-eo pipefail`

**Status:** CLOSED · rev-2 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aTrimmedWait-6-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aTrimmedWait-6-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-aTrimmedWait-1-arms-observed.md](../build/2026-11-15-build-TOOL-aTrimmedWait-1-arms-observed.md) | journal | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-7 TOOL-aTrimmedWait-8 TOOL-aTrimmedWait-9 TOOL-aTrimmedWait-10 |
| [2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md) | research | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-7 |
| [2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md](../reviews/2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md) | diff-review | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-7 |

<!-- /gen:spec-records -->

## 1. Goal

Builders in session `db957487` waited on their own background work by polling it, with
`timeout 590 tail -f <output> | grep -m1 exit=`, `sleep 240; cat <output>` and
`until ...; do sleep 5; done`. The harness already notifies an agent when its background command
exits, so each poll is pure waiting, about 12 h across that session by the brief's count. This unit
makes the scratch guard's role-gate arm refuse those three shapes for a role agent. It also closes
the one option gap the kickoff probe found: `bash -eo pipefail <suite>` reaches a role agent
unrefused, because only a bare `-o` takes an argument in the option table.

## 2. Scope (IN)

- **S1** — Option clusters. In the shell row of `GATE_OPTION_RULES`, a single-dash or plus option
  cluster takes one following word for each `o` or `O` letter it carries, so `-eo pipefail`,
  `-euxo pipefail` and `+o posix` step past their arguments. A cluster that also carries `c` scans the
  word after those arguments as its body. A cluster carrying `n` still ends the command first. A
  bare `-o`, `+o`, `-O` and `+O` behave as today. Observed by AC1, AC2 and AC3.
- **S2** — The polling refusal. `checkRoleGate` refuses a role agent's Bash or PowerShell command
  that holds any of these:
  - **P1 tail follow**: a `tail` whose words carry a follow option;
  - **P2 sleep in a loop**: a `sleep` in a command that also holds a `while` or `until` loop;
  - **P3 sleep at or over 5 s**: a `sleep` of 5 s or more, or one whose duration it cannot read. <!-- DERIVED from POLL_SLEEP_FLOOR_S -->

  It refuses with a reason naming the row and the notification that replaces the wait. It binds where
  the role arm binds, and only when no gate row has already refused the command. Observed by AC2,
  AC3 and AC4.
- **S3** — The near misses stay admitted: a `sleep` under 5 s outside a `while` or `until` loop, a <!-- DERIVED from POLL_SLEEP_FLOOR_S -->
  `tail` without a follow option, and every command the main loop runs. Observed by AC2 and AC3.
- **S4** — The hook's header, the hooks README's role-gate section and the roles help page state the
  P rows. The option-gap example drops out of both ceiling sentences, which otherwise stand as
  written. Observed by AC5.
- **S5** — The acceptance ledger records the hook timed over one polling payload, with the base hook
  and with the built one, on node a. Observed by AC6.

## 3. Non-goals (OUT)

- No G1, G2 or G3 change beyond S1. The brief's Non-goals keep the evasion ceiling as written. A
  gate behind `do`, `then` or `if` stays unseen by the gate rows, because S2's reserved-word step is
  read by the polling rows alone.
- No other launcher's clusters. Python's and Node's option rows are unchanged.
- No refusal for the main loop, which carries no `agent_type`, and none for the `Monitor` tool or
  any other tool outside the guard's `TOOLS` list.
- No PowerShell spelling of a wait: `Start-Sleep` and `Get-Content -Wait` are not read. A PowerShell
  payload is scanned as text, as the gate rows scan it, so its `sleep` alias is read.
- No allowlist entry for polling and no policy key. A role agent's poll is never a gate run.
- No kit version bump. The build README moves kit versions once, after the last code move.
- Not the open ask `TOOL-aCarriedStop-7`, the scratch-guard self-test red on the daily held job at
  `8db6f4be`.

### Edges

none

## 4. Design

### Evidence

Read at `a25c84fc0`, byte-identical to the base `846d51d3` under `tools/`.

- `GATE_OPTION_RULES.shell` is
  `{ plus: true, takes: ['-o', '+o', '-O', '+O', '--rcfile', '--init-file'], ends: /^-[A-Za-z]*n[A-Za-z]*$/, body: /^-[A-Za-z]*c[A-Za-z]*$/ }`
  (`tools/hooks/scratch-guard.js@7c31933f6258:1463-1471`). `scanLauncherOptions` tests `takes`
  exactly, then `ends`, then `body`, and steps past any other option word alone (`:1503-1517`).
- `scanCommandHeads` (`:1529-1576`) splits the blanked view at `;`, `|`, `&`, `(`, `)` and newlines.
  It steps `NAME=value` words, the prefix words and `timeout` with its duration, then a launcher and
  its options, and records `{ text, head, argv, launched }`. A reserved word such as `do` is not
  stepped, so `do sleep 5` records the head `do`.
- `checkRoleGate` (`:1671-1701`) is the ONE evaluation order of the role arm: no `agent_type`
  admits; no candidate admits with no file read; no root admits; an absent index admits and a broken
  one refuses; then each candidate meets G1, G2 and G3. `main` calls it last, and a throw refuses a
  role agent (`:1899-1913`).
- Probed at `a25c84fc0` with a fixture suite path after each launcher, `scanCommandHeads` reads the
  head `pipefail` for `bash -eo pipefail`, `bash -euxo pipefail` and `bash -co pipefail` with the
  suite in a quoted body. It reads no head for `bash -no pipefail`, and the suite path for
  `bash -o pipefail`.
  Through the hook, a `gov-builder` payload in this checkout exits 0 for
  `bash -eo pipefail tools/hooks/agent-cap.test.sh`, `timeout 590 tail -f /c/x.log` and
  `sleep 240; cat /c/x.out`. It exits 2 naming `G2 runner` for
  `bash -o pipefail tools/run-gates/run-gates.sh`.
- The roles help page ends its list of refusals with "All of these switch on only where
  `.claude/roles.json` exists" (`help/roles.md@edfba0e98377:179-191`), so S2 binds after the index
  read.

### What the builders ran, measured

Every Bash call of the 334 sub-agent transcripts of session `db957487`, deduplicated by tool-use id,
was classed by regular expressions approximating S2's rows. PINNED on 2026-11-14 on node a:

| Class | Commands |
|---|---|
| Bash calls | 9301 |
| P1, a `tail` with `-f`, `-F`, `--follow` or a cluster carrying `f` | 104 |
| P2, a `sleep` in a command holding `while` or `until` | 12 |
| P3, a flat `sleep` of 5 s or more, or unreadable | 69 <!-- DERIVED from POLL_SLEEP_FLOOR_S --> |
| refused by any row, distinct commands | 184 |
| a `sleep` admitted: under 5 s, no loop | 1, `kill <pid>; sleep 1; ps -ef ...` <!-- DERIVED from POLL_SLEEP_FLOOR_S --> |
| a `timeout <d> sleep <n>` shape | 0 |

Every refused command this writer sampled waited on a background command's output file or a
process, and the 184 were not read one by one. The one admitted
`sleep` paused for a killed process to leave the table. A foreground `sleep 6` ran unrefused in this
writer's own session, so the harness does not refuse it.

### S1 — the cluster rule

`GATE_OPTION_RULES.shell` drops `-o`, `+o`, `-O` and `+O` from `takes`, keeps `--rcfile` and
`--init-file`, and gains `clusterTakes: /[oO]/g`. In `scanLauncherOptions`, after the `takes` test
and the `ends` test, and before the `body` test:

1. `j` is the count of `clusterTakes` letters in the word, when the rule declares it and the word
   matches `^[-+][A-Za-z]+$`; otherwise 0. A long option such as `--noprofile` never matches.
2. A `body` word scans `a[k + 1 + j]` as its body, rather than `a[k + 1]`.
3. Any other option word steps past itself and its `j` arguments.

`ends` keeps precedence, so `-no pipefail <suite>` still runs nothing and is admitted as today. A
bare `-o` gives `j = 1`, the step `takes` gave it, so every arm the suite pins for `-o` and `-O` reads
as today. Python, Node and the prefix words declare no `clusterTakes` and do not change.

### S2 — the polling rows

**The scan.** `scanCommandHeads(cmd, depth, opts)` gains a third parameter. When `opts.reserved` is
set, the prefix loop also steps past a word in `SHELL_RESERVED_WORDS`, which holds `!`, `{`, `do`,
`then`, `else`, `elif`, `if`, `while` and `until`. Each entry records the reserved words it stepped
as `reserved`. `scanLauncherOptions` hands `opts` to the body scan. The gate rows call it with no
`opts`, so their heads do not move.

**The predicate.** `checkPollWait(cmd)` scans `cmd` with `{ reserved: true }`. It returns
`{ row, c }` for the first entry that matches a row, or null:

| Row | Matches |
|---|---|
| `P1 tail follow` | the head's base name is `tail`, and a later word is `--follow`, begins `--follow=`, or matches `^-[A-Za-z0-9]*[fF][A-Za-z0-9]*$` |
| `P2 sleep in a loop` | the head's base name is `sleep`, and some entry of the same command stepped `while` or `until` |
| `P3 sleep at or over 5 s` | the head's base name is `sleep`, and `deriveSleepSeconds` of its other words is null or at least `POLL_SLEEP_FLOOR_S`, which is 5 |

`deriveSleepSeconds(words)` sums the words as GNU `sleep` does: each word is a decimal number with an
optional `s`, `m`, `h` or `d` suffix, and `infinity` is infinite. Any other word, a `$W` among them,
makes the sum null, and a duration that cannot be read counts as at the floor.

**The order.** `checkRoleGate`'s ONE evaluation order becomes:

| Step | Today | After |
|---|---|---|
| 1 | no `agent_type` admits | unchanged |
| 2 | no candidate admits, with no file read | no candidate AND `checkPollWait` null admits, with no file read |
| 3 to 6 | the root, the index, the allowlist, the gate manifest | unchanged |
| 7 | each candidate meets G1, G2 and G3, and the first gate row refuses | unchanged |
| 8 | — | a polling hit refuses with `renderPollDeny` |
| 9 | the G1-unarmed witness, else admit | unchanged |

A command that both polls and runs a gate is refused by its gate row, as today, so no gate verdict
moves. A broken index refuses a polling command as it refuses a candidate.

**The refusal.** `renderPollDeny(type, c, row)` writes, ending in a newline:

```
BLOCKED by scratch-guard: a role agent does not poll. Agent type <type> ran `<simple command>`, which is row <row>.

A command started with run_in_background notifies this agent when it exits, so that notification is the wait. A pause under 5 s outside a while or until loop is admitted.
```

### S4 — the text

- The header's role-arm paragraph (`tools/hooks/scratch-guard.js@7c31933f6258:125-148`) adds the P
  rows, one sentence each, and the cluster rule beside `GATE_OPTION_RULES`. Its ceiling sentence
  drops the parenthesis quoted as text 1 below, and gains the polling ceiling.
- `tools/hooks/README.md`, section "scratch-guard's fourth check" (`@516a574d0e46:635-668`): the
  option sentence states the cluster rule. The rows table gains the three P rows, each admitted
  "never". The ceiling drops the clause quoted as text 2 and gains the polling ceiling. The README
  names no kit file by an install path, which the install-prefix leg grades.
- `help/roles.md`, list "What the hooks refuse": after the bullet on the bar and suites, the bullet
  quoted as text 3.

```text
1 (dropped)  (`bash -eo pipefail` among them, since only a bare `-o` is in the table)
2 (dropped)  , such as the `o` inside `bash -eo pipefail`
3 (added)    - A role agent's polling wait: a `tail` that follows a file, a `sleep` inside a `while`
               or `until` loop, or a `sleep` of 5 s or more.
```

### What the polling rows do not check

This is the ceiling S4 writes:

- Polling through a script, an interpreter, a function or an alias.
- A `sleep` under 5 s in a `for` loop. <!-- DERIVED from POLL_SLEEP_FLOOR_S -->
- A `sleep` under a shorter `timeout`, which is graded on its own duration. The measured corpus
  held none.
- A file named like a follow option without `--`.
- PowerShell's own wait cmdlets.
- Whether the command is backgrounded. The payload's `run_in_background` is not read, so a
  backgrounded poll is refused too.

### The pass probe, `$SCRATCH/p6.sh`

Run from the worktree root. It prints one line per payload through the built hook, and the heads
`scanCommandHeads` reads for the cluster shapes.

```bash
set -u
ROOT=$(pwd -W)
node -e "const s=require('./tools/hooks/scratch-guard.js');for(const c of process.argv.slice(1))console.log('head',JSON.stringify(c),s.scanCommandHeads(c).map(h=>h.head).join(',')||'(none)')" \
  "bash -eo pipefail kit/a.test.sh" "bash -euxo pipefail kit/a.test.sh" "bash -co pipefail 'bash kit/a.test.sh'" \
  "bash -no pipefail kit/a.test.sh" "bash -o pipefail kit/a.test.sh"
row() { # label · agent type or - · command
  local t="$2"; [ "$t" = - ] && t=""
  node -e 'const d={tool_name:"Bash",cwd:process.argv[2],tool_input:{command:process.argv[3]}};if(process.argv[1])d.agent_type=process.argv[1];process.stdout.write(JSON.stringify(d))' "$t" "$ROOT" "$3" \
    | node tools/hooks/scratch-guard.js 2>"$SCRATCH/p6.err"
  echo "row $1 exit $? $(grep -oE 'row [PG][0-9] [a-z0-9 ]+' "$SCRATCH/p6.err" | head -1)"
}
row R1 gov-builder 'bash -eo pipefail tools/hooks/agent-cap.test.sh'
row R2 gov-builder 'timeout 590 tail -f /c/x.log'
row R3 gov-builder 'tail --pid=4242 -f /c/x.log | grep -m1 exit='
row R4 gov-builder 'until [ -s /c/x.out ]; do sleep 1; done'
row R5 gov-builder 'sleep 240; cat /c/x.out'
row R6 gov-builder 'sleep "$W"; cat /c/x.out'
row R7 gov-builder "bash -c 'sleep 30'"
row N1 gov-builder 'kill 4242; sleep 1; ps -ef'
row N2 gov-builder 'tail -n 5 /c/x.log'
row N3 gov-builder 'tail -5 /c/x.log; grep -f /c/p.txt /c/x.log'
row N4 - 'timeout 590 tail -f /c/x.log'
row N5 gov-builder 'for i in 1 2 3; do sleep 1; done'
row N6 gov-builder 'bash -no pipefail tools/hooks/agent-cap.test.sh'
row N7 gov-builder 'bash -o pipefail tools/run-gates/run-gates.sh'
```

This writer ran the block at `a25c84fc0`, before any build. The three cluster heads read
`pipefail`, the `-n` cluster `(none)` and the bare `-o` the suite path. Every row printed `exit 0`
but N7, which printed `exit 2 row G2 runner`.

### The corpus probe, `$SCRATCH/p6c.js`

It runs `checkRoleGate` as `gov-builder` in this checkout over every Bash call of the measured
corpus, through the base module and the built one, and classes each difference. A difference is
`poll` when the base admits and the built hook refuses with a P row. It is `cluster` when the
command carries a shell option cluster holding `o` or `O`. Anything else is `other`. This writer ran
it base against base at `a25c84fc0`, and it printed
`commands 9301 · same 9301 · poll 0 · cluster 0 · other 0` in 48 s. <!-- PINNED 2026-11-14 -->

```js
// node p6c.js <base module> <new module> <session transcript dir> <checkout root>
const [base, now, dir, root] = process.argv.slice(2)
const fs = require('fs'), path = require('path')
const B = require(path.resolve(base)), N = require(path.resolve(now))
const files = []
const walk = (d) => { for (const e of fs.readdirSync(d, { withFileTypes: true })) { const p = path.join(d, e.name); if (e.isDirectory()) walk(p); else if (/^agent-.*\.jsonl$/.test(e.name)) files.push(p) } }
walk(path.join(dir, 'subagents'))
const seen = new Set(), cmds = []
for (const f of files) for (const l of fs.readFileSync(f, 'utf8').split('\n')) {
  let o; try { o = JSON.parse(l) } catch { continue }
  const c = o && o.message && Array.isArray(o.message.content) ? o.message.content : []
  for (const b of c) if (b && b.type === 'tool_use' && b.name === 'Bash' && !seen.has(b.id)) { seen.add(b.id); cmds.push((b.input && b.input.command) || '') }
}
const cluster = /(?:^|[\s;&|(])(?:bash|sh)\s+(?:\S+\s+)*?[-+][A-Za-z]*[oO][A-Za-z]*\s/
const v = (m, cmd) => { try { const r = m.checkRoleGate(cmd, { agent_type: 'gov-builder', cwd: root }, {}); return r && r.deny ? (/row ([PG]\d)/.exec(r.deny) || [, 'deny'])[1] : 'admit' } catch (e) { return 'throw' } }
const n = { commands: cmds.length, same: 0, poll: 0, cluster: 0, other: 0 }
for (const cmd of cmds) {
  const a = v(B, cmd), b = v(N, cmd)
  if (a === b) n.same++
  else if (a === 'admit' && /^P/.test(b)) n.poll++
  else if (cluster.test(cmd)) n.cluster++
  else { n.other++; if (n.other <= 5) console.log('OTHER', a, '->', b, JSON.stringify(cmd.slice(0, 120))) }
}
console.log(Object.entries(n).map(([k, x]) => `${k} ${x}`).join(' · '))
```

The base module is `git show 846d51d3:tools/hooks/scratch-guard.js > "$SCRATCH/base6/scratch-guard.js"`.
The transcript directory is
`C:/Users/daily-agent/.claude/projects/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f`.

### Inventory

| identifier | kind | lexicon |
|---|---|---|
| `checkPollWait` | js.function | `check`, OK by `lexicon.py --suggest` |
| `deriveSleepSeconds` | js.function | `derive`, OK by `lexicon.py --suggest` |
| `renderPollDeny` | js.function | `render`, OK by `lexicon.py --suggest` |
| `POLL_SLEEP_FLOOR_S` | constant | no declared cell |
| `SHELL_RESERVED_WORDS` | constant | no declared cell |
| `clusterTakes` | option-rule field | — |
| `P1 tail follow`, `P2 sleep in a loop`, `P3 sleep at or over 5 s` | refusal row labels | — |

`checkPollWait` joins the module's exports, so the probes and the suite can call it.

### Rollout

One pass at order 6. No other unit of this build names `tools/hooks/`. The suite's
`FLOOR_ASSERTIONS` (`tools/hooks/scratch-guard.test.sh@eccc92bcc809:1704`, 361) rises by the count
of new assertions, and the close confirms the count from a real run.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/README.md`
- `help/roles.md`

### Alternatives rejected

- **Refuse every `sleep`.** The corpus's one short pause after a `kill` is a legitimate probe, and
  fixtures space file times with `sleep 1`.
- **Step reserved words for the gate rows too.** It would close a G3 evasion behind `do` and `then`,
  which the brief's Non-goals keep out.
- **Read the floor from a policy key.** No caller needs another value, so the floor stays a constant.
- **Refuse only a foreground poll.** A backgrounded poll still waits for nothing, and the payload
  field would add a branch the corpus never needed.
- **List `-eo`, `-euo` and `-euxo` in `takes`.** Each new spelling would be a new miss, and the
  letter count covers every cluster.

## 5. Production-readiness checklist

- security — no new write, path or input. The arm stays fail-closed for a role agent, and the new
  rows read only the command text.
- perf / scale — one more scan of the command per role-agent call, in microseconds. The saving is the
  agent's wait: 240 s on the AC6 payload, and about 12 h over the measured session by the brief's <!-- DERIVED from the AC6 payload's own duration -->
  figure.
- error / empty / loading states — a duration that does not read is refused, with a message naming
  the row. An absent role index adds no arm, as the help page states.
- observability — each refusal names the agent type, the simple command and its P row.
- risks — a legitimate probe that sleeps 5 s or more on the command line is refused, and its remedy <!-- DERIVED from POLL_SLEEP_FLOOR_S -->
  is a script or a shorter pause. Adopters receive the rows with their next hooks install. The suite
  `TOOL-aCarriedStop-7` names is red on the daily held job, so the close reads this unit's new arms
  by their own rows rather than by the suite's exit.
- testing — the two pass probes, and the suite's new rows, observed RED then GREEN at the close.
- migration — none.
- user docs — `help/roles.md` gains the bullet in S4.

## 6. Acceptance criteria

`$SCRATCH` is the run's scratch directory. The two probes are the §4 blocks.

- **AC1** — When `bash "$SCRATCH/p6.sh"` runs, its `head` lines read the fixture suite path for
  `bash -eo pipefail`, `bash -euxo pipefail`, `bash -co pipefail` and `bash -o pipefail`, and
  `(none)` for `bash -no pipefail`.
  Red when: a cluster takes no argument, so the first three read `pipefail`, as at `a25c84fc0`.
- **AC2** — When `bash "$SCRATCH/p6.sh"` runs, rows R1 to R7 each print `exit 2`. R1 names
  `row G3 suite`, R2 and R3 name `row P1`, R4 names `row P2`, and R5, R6 and R7 name `row P3`.
  Red when: the polling step is absent, so R2 to R7 exit 0, or the cluster rule is absent, so R1
  exits 0. R1, R2 and R5 exited 0 at `a25c84fc0`.
- **AC3** — When `bash "$SCRATCH/p6.sh"` runs, rows N1 to N6 each print `exit 0` with nothing after
  it, and N7 prints `exit 2` naming `row G2 runner`.
  Red when: a short flat `sleep`, a non-following `tail`, a `-f` of another command, the main loop,
  a short `sleep` in a `for` loop or a syntax check is refused.
- **AC4** — When `node "$SCRATCH/p6c.js"` runs over the base and built modules as §4 states, it prints
  `other 0`, and its `poll` and `cluster` counts are recorded in the acceptance ledger.
  Red when: any gate verdict moves outside the two intended classes, for example a gate row
  displaced by a polling refusal.
  fixture: the session transcript directory named in §4, on node a today.
  figure: DERIVED at observation. The §4 table's 184 polling commands are PINNED from regular
  expressions, so `poll` may differ from it by the shapes those approximate.
  cost: about a minute.
- **AC5** — When `grep -c 'P1 tail follow' tools/hooks/scratch-guard.js tools/hooks/README.md` runs,
  each file counts at least 1, and `grep -c 'polling wait' help/roles.md` prints 1.
  `grep -n 'eo pipefail. among them' tools/hooks/scratch-guard.js` and
  `grep -n 'such as the .o. inside' tools/hooks/README.md` print nothing.
  Red when: one surface is edited without the others, or a ceiling sentence still names the closed
  gap.
- **AC6** — When the main loop times the hook over the R5 payload of `"$SCRATCH/p6.sh"`, through
  `node "$SCRATCH/base6/scratch-guard.js"` and then `node tools/hooks/scratch-guard.js`, one at a time
  on node a, the acceptance ledger records both readings with their exits: 0, then 2.
  Red when: the built hook exits 0, so the agent goes on to wait 240 s. <!-- DERIVED from the AC6 payload's own duration -->
  figure: DERIVED at observation. The 240 s is the payload's own duration.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `policy fixtures` · `docs` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

`python tools/check-spec-tokens.py --legs-for` over the files touched names the first seven legs as
guarded by `tools/hooks/` or by `tools/hooks/scratch-guard.js`, beside the broad `tools/` guards it
excludes; `help/roles.md` trips no guarded leg. `docs` reads the help page, `install-prefix (shipped
surface)` reads the README text, and the kit-version legs are graded once the build's single version
move lands.

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 · run_role_bash rows for R1 to R7 and N1 to N7 of the pass probe, under the suite's fixture kit names; staged by restoring the `-o` entries of `takes` without `clusterTakes`, which admits R1, and by removing the polling step, which admits R2 to R7 · `FLOOR_ASSERTIONS`, raised by the count of new assertions

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
`memory hygiene`, the lexicon and `check-spec-tokens.py --spec` over this file.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft from the brief `2026-11-14-prompt-TOOL-aTrimmedWait-1-brief`,
  item 6, grounded at `846d51d3`. The kickoff probe named `tail -f` and the option gap; the measured
  corpus added the `sleep` shapes and the 5 s floor. The roster pairs two mechanisms in one unit, <!-- DERIVED from POLL_SLEEP_FLOOR_S -->
  and this spec keeps the pairing as the roster wrote it.
- rev-2 · 2026-11-14 · §2, §4, §5, §6, §9 · each figure the pinned-facts arm named carries a pin on
  its line: PINNED where measured, DERIVED naming `POLL_SLEEP_FLOOR_S` or the AC6 payload where
  computed, no meaning changed, per `2026-11-14-prompt-TOOL-aTrimmedWait-7-writing-practice`. The
  two fenced literals that quote the shipped refusal and help text carry none.

## 10. Reuse audit

The seams this unit extends are `scanCommandHeads`, `scanLauncherOptions` and `GATE_OPTION_RULES`
in `tools/hooks/scratch-guard.js`, the scanner and rule table the brief names. The polling rows read
the scanner's entries, and its third parameter steps reserved words for them alone, rather than
adding a second tokenizer. The rows sit inside `checkRoleGate`, whose index read, fail-closed catch
and refusal protocol they take unchanged. `python tools/codebase-map/reuse_lookup.py "refuse a role
agent's shell command that waits by polling a file"` ranked name stems only (`PolicyRefused`,
`RolesError`, `resolve_shell_argv`), none of which reads a command, so no existing seam fits beyond
the scanner. Recall returned `TOOL-aOrientedCast-14`, which built the option table and named
`bash -o pipefail`, and its closing review's left-shift rows. It returned no record of a polling
refusal, and the open ask `TOOL-aCarriedStop-7` on this suite's held red.

Recall terms used: `python tools/memory-recall/query.py "how does scratch-guard refuse a role agent running a suite, and does anything refuse tail -f or sleep polling" --terms "scratch-guard checkRoleGate G3 suite launcher option GATE_OPTION_RULES pipefail polling tail sleep background notification"`
