# TOOL-aTrimmedWait-9 — closing-review repair, hooks and roles: the role gate reads no shell comment as words, the P3 rows are tested at the floor, and arm 23 tells a resumed read from a cold re-parse

**Status:** SPECCED · rev-2 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 8 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-prompt-TOOL-aTrimmedWait-8-ruling.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-8-ruling.md) | research | TOOL-aTrimmedWait-8 |
| [2026-11-14-prompt-TOOL-aTrimmedWait-9-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-9-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-9-promotion.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-9-promotion.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of TOOL-aTrimmedWait-1..7, round 1
(`memory/builds/aTrimmedWait/reviews/2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md`),
exited CONVERGED with verdict CLEAN WITH FIXES. BUILD-METHOD M4 batches its MEDIUM and LOW items by
disjoint write set. This unit takes the hooks and roles set: M2, L2 and M7. M2 is a false refusal
inside unit 6's polling class. L2 and M7 are verification gaps, where a regression of unit 6 or
unit 7 passes every arm. Each item takes the fix the record's skeptic judged sound, and for L2 and
M7 the skeptic's class-level or corrected fix. Every line cited below was read at `2a13de8b6`, whose
blobs of the three files equal the record's pins (`scratch-guard.js@3220edce`,
`scratch-guard.test.sh@1eaa4530`, `adopt-roles.test.sh@0deeb156`).

| Review item | Severity | Finding | Scope item | Criteria |
|---|---|---|---|---|
| M2 | MEDIUM | 2 | S1 | AC1, AC2, AC3, AC5 |
| L2 | LOW | 11 | S2 | AC4, AC5 |
| M7 | MEDIUM | 10 | S3 | AC6, AC7 |

## 2. Scope (IN)

- **S1** — Review item "M2 — P3 reads a shell comment as a sleep duration and refuses a sub-floor
  pause". The class the record's appendix names is `shell-comment-word-read-as-an-argument`, and the
  fix is the record's better form: comments are cut once in `scanCommandHeads`, so every role-gate
  row reads the same words. `scanCommandHeads` blanks each shell comment in its quote-blanked view
  before it splits the view into simple commands. A comment opens at a `#` that begins a word,
  outside quotes and heredoc bodies, and runs to the end of its line. The hook's header and the
  scanner's doc comment each gain one sentence stating it. The suite gains rows C1 to C6 of §4.
  Observed by AC1, AC2, AC3 and AC5.
- **S2** — Review item "L2 — The P3 rows test only far from the 5 s floor and no unit suffix", with
  the skeptic's class-level fix. The suite gains rows F1 to F7 of §4: `sleep 5`, `sleep 1m`,
  `sleep 1h`, `sleep 1d` and `sleep infinity` each refused naming P3, and `sleep 4.9` and `sleep 4s`
  each admitted with empty stderr. `FLOOR_ASSERTIONS` rises by the 13 rows S1 and S2 add, with a
  history line. No code moves for S2: every row already reads as the record says at `2a13de8b6`.
  Observed by AC4 and AC5.
- **S3** — Review item "M7 — Arm 23's append and torn arms cannot tell a resumed read from a cold
  re-parse", with the skeptic's corrected fix. In `tools/roles/adopt-roles.test.sh`, the append arm
  and the torn arm each seed the first run's record with a value only a resumed read can carry, then
  append the rest and assert both the cold stdout lines and that seeded value. The seeded value is
  the record's `bad` count, set to 7 by a new `A23_EDIT` mode. Arm 23's header comment states what
  the two arms now prove. Observed by AC6 and AC7.

## 3. Non-goals (OUT)

- No item of the review record but M2, L2 and M7. M1, M3, M4, M5, M6 and L1 are TOOL-aTrimmedWait-8's.
- No cut in `buildCommandView`. Its other three readers are the scratch arm's write and redirect
  checks (`tools/hooks/scratch-guard.js@3220edce42ac:369`, `:532`, `:789`), whose verdicts no item
  names.
- No change to `deriveSleepSeconds`, `checkPollWait`, `POLL_SLEEP_FLOOR_S` or any P row's predicate.
- No change to `handoff.py`. M7 is a test that cannot go red, not a defect in the resume.
- No PowerShell block comment (`<# … #>`) reading beyond its first line, and no other shell grammar.
- No `tools/hooks/README.md` or `help/roles.md` edit: neither states how the scanner reads a word, and
  every sentence of both stays true. The README's role-gate section (`@516a574d0e46:635-678`) says the
  arm splits the command into simple commands and that its match is textual.
- No kit version move. The build README moves kit versions once, after the last code move.
- No verdict change outside the defects the items name, and no narrowing of the bar or the full
  hygiene run.
- One exception to the build rule "No verdict moves", ruled by the owner (§8 F1): a G3 verdict moves
  toward refusal. A suite whose only admitting word, such as `--render`, sits in a shell comment is
  refused where it was admitted. No other gate verdict moves.

### Edges

none

## 4. Design

### Evidence

- `scanCommandHeads` (`tools/hooks/scratch-guard.js@3220edce42ac:1549-1601`) builds its view with
  `buildCommandView` (`:289-331`). That view blanks heredoc bodies, then the contents of single- and
  double-quoted runs, preserving length. The scanner splits the view at `;`, `|`, `&`, `(`, `)` and
  newlines, and reads each segment's words from the original text at the view's token offsets.
  Nothing in either function reads `#`.
- `checkPollWait` (`:1638-1651`) hands `c.argv.slice(1)` to `deriveSleepSeconds` (`:1620-1630`),
  which returns null on any word it cannot read. Null is refused as P3.
- `checkRoleGate` (`:1743-1775`) reads `scanCommandHeads(cmd)` for the gate rows and `checkPollWait`
  for the polling rows. No module outside `scratch-guard.js` calls either, by a grep over `tools/`
  and `skills/`.
- Bash, observed here: `#` opens a comment after whitespace, `;`, `(` and `>`, and the comment
  swallows a later `;`. `q#r` prints `q#r`, `$#` and `${#a[@]}` expand, and `echo a>#b` is a syntax
  error, so `#` after `>` opens a comment too.
- `load_session_calls` (`tools/roles/handoff.py@cb2874a363ac:893-942`) resumes from a valid record by
  loading its `calls`, `notified` and `bad`, rebuilding `by_id` from `calls`, and parsing from
  `offset`. `print_agent_lines` (`:1149-1150`) turns a non-zero `bad` into the stderr note
  `<session>: <bad> line(s) did not parse as JSON and were skipped`. It matches a call to the handoff
  by the `gov:handoff` marker first (`:1171-1173`), and only then reads its `result`.

### S1 — the comment cut

The first line of `scanCommandHeads` becomes:

```js
const view = buildCommandView(cmd).replace(/(^|[\s;&|()<>])#[^\n]*/g, (w, p) => p + ' '.repeat(w.length - p.length))
```

The cut runs on the quote-blanked view, so a quoted `#` and a heredoc body are already spaces. The
blanked run keeps its length, so every later offset still indexes the original text. A blanked
comment holds no token and no separator, so its words and any `;` in it reach no row. A `-c` body is
scanned by the same function, so a comment inside it is cut there. The doc comment above the
function gains: "A `#` beginning a word, outside quotes and heredoc bodies, blanks the rest of its
line first, as the shell drops a comment (TOOL-aTrimmedWait-9)." The header's role-arm paragraph
(`:125-156`) gains, after the P3 sentence: "A shell comment is read by no row."

The cut moves one class of gate verdict, a comment holding a gate word. The measured case:
`bash tools/hooks/agent-cap.test.sh # --render` is admitted at `2a13de8b6`, because G3 reads
`--render` from the comment as an admitting word, and it is refused on G3 with the cut. That is the
same defect class, read the other way, and the record's fix names it: "so every gate row sees the
same argv". Over the measured corpus, no verdict moves (the corpus probe below). The owner accepted
this move as the build rule's one exception (§8 F1).

### S1 and S2 — the suite rows

After row `W-AC3 N7` (`tools/hooks/scratch-guard.test.sh@1eaa4530a1fc:1478`), under a comment block
naming this unit, the record's items and each row's staged break:

```bash
run_role_bash "W9-AC1 C1 sleep 3 # brief pause -> allow, stderr EMPTY" 0 empty gov-builder Bash 'sleep 3 # brief pause'
run_role_bash "W9-AC1 C2 sleep 9 # x -> deny naming P3" 2 "any;;P3 sleep at or over 5 s" gov-builder Bash 'sleep 9 # x'
run_role_bash "W9-AC1 C3 a comment's ; starts no command -> allow, stderr EMPTY" 0 empty gov-builder Bash 'sleep 3 # a; sleep 9'
run_role_bash "W9-AC1 C4 a quoted ' #' opens no comment -> deny naming P3" 2 "any;;P3 sleep at or over 5 s" gov-builder Bash "echo ' #'; sleep 9"
run_role_bash "W9-AC1 C5 a # inside a word opens no comment -> deny naming P3" 2 "any;;P3 sleep at or over 5 s" gov-builder Bash 'sleep 3#x'
run_role_bash "W9-AC2 C6 <suite> # --render -> deny naming G3" 2 "any;;G3 suite" gov-builder Bash "bash kit/$SG_K_HOOKS/agent-cap.test.sh # --render"
run_role_bash "W9-AC4 F1 sleep 5, at the floor -> deny naming P3" 2 "any;;P3 sleep at or over 5 s" gov-builder Bash 'sleep 5'
run_role_bash "W9-AC4 F2 sleep 1m -> deny naming P3" 2 "any;;P3 sleep at or over 5 s" gov-builder Bash 'sleep 1m'
run_role_bash "W9-AC4 F3 sleep 1h -> deny naming P3" 2 "any;;P3 sleep at or over 5 s" gov-builder Bash 'sleep 1h'
run_role_bash "W9-AC4 F4 sleep 1d -> deny naming P3" 2 "any;;P3 sleep at or over 5 s" gov-builder Bash 'sleep 1d'
run_role_bash "W9-AC4 F5 sleep infinity -> deny naming P3" 2 "any;;P3 sleep at or over 5 s" gov-builder Bash 'sleep infinity'
run_role_bash "W9-AC4 F6 sleep 4.9, under the floor -> allow, stderr EMPTY" 0 empty gov-builder Bash 'sleep 4.9'
run_role_bash "W9-AC4 F7 sleep 4s, under the floor -> allow, stderr EMPTY" 0 empty gov-builder Bash 'sleep 4s'
```

Each row sits where the role index is written and the manifest reads, so an admit's stderr is empty,
as row `W-AC3 N1`'s is. `FLOOR_ASSERTIONS` (`:1724`) moves from 375 to 388, and the history above it
gains: "388 = 375 + the 13 run_role_bash rows TOOL-aTrimmedWait-9 added (6 for its S1 and 7 for its
S2), counted by hand under the same rule." <!-- DERIVED from the 13 rows above -->

### S3 — arm 23's two resumed arms

`A23_EDIT` (`tools/roles/adopt-roles.test.sh@0deeb156e7db:1029-1040`) gains a mode:

```python
elif mode == "bad":
    rec["bad"] = 7
```

The append arm (`:1054-1056`) and the torn arm (`:1057-1060`) each become: write the first part, run,
seed the record with mode `bad`, append the rest, run, and assert. The append arm:

```bash
head -n 1 "$TMP_ROOT/a23.full" > "$A23S"; run_agents23
"$PY" -B -c "$A23_EDIT" "$A23D" bad; _e23=$?; tail -n +2 "$TMP_ROOT/a23.full" >> "$A23S"; run_agents23
check_arm "arm 23 ...a record taken on the first line, its bad count seeded, then the rest appended, prints the cold lines and the seeded count" \
   "$([ "$_e23" = 0 ] && check_cold23 && grep -q ': 7 line(s) did not parse' "$TMP_ROOT/a23.err" && echo 1 || echo 0)"
```

The torn arm takes the same three steps over its `head -c` and `tail -c` split, and keeps its `cmp`.
Each arm asserts two things, and each needs the resume:

- The note naming 7 lines prints only when the record seeded the read. A cold re-parse of the
  fixture counts 0, so it prints no note.
- The `returned` line prints only when the appended `res` line attached its `agentId` to the call
  through `by_id`, which the resume rebuilt from the record's `calls`. The appended notification
  line also lands in `notified`. Without the rebuild, the call has no `result` and
  `print_agent_lines` raises.

`A23_EDIT` empties `notified` in every mode. That is harmless here: a first-line record and a torn
first-run record hold no notification, which sits on the transcript's last line. The two arms are
rewritten in place, so the suite's `FLOOR_ASSERTIONS` stays 69. Arm 23's header (`:1017-1024`) says
of the two arms: "each resumed from the record's offset, which only a resumed read shows: the
record's bad count, seeded to 7, prints as a note, and the returned line needs the appended result
to reach the call through the rebuilt by_id".

### Why not the record's example poison

The record's example strips the `gov:handoff` marker from the record's `calls[0].input.prompt`. That
proves the record seeded the read, but not the rest the record says it proves. `print_agent_lines`
filters calls on the marker before it reads any `result` (`handoff.py@cb2874a363ac:1171-1173`), so a
stripped marker raises "no Agent call … opens its prompt with the marker" whether or not the appended
`res` attached. The record offers the marker strip "for example". The `bad` seed is a poison of the
same kind that keeps the call matched, so the arm also reads the attachment.

### What the arms do not check

- C rows: a comment after `{`, `=` or a backslash, each correctly not a comment and not pinned. A
  PowerShell block comment's lines after its first. A `#` the shell would read inside `$(…)` across a
  line break.
- F5 reds only if `infinity` reads as a finite number under the floor. Dropping the `infinity` branch
  leaves the word unreadable, and an unreadable duration is refused anyway.
- Arm 23: a resumed read that carries `bad` but drops `notified`. The seeded record's `notified` is
  empty, and the appended notification line refills it.

### The pass probe, `$SCRATCH/p9.sh`

Run from the worktree root, over this checkout's role index. With no argument it runs the built hook.

```bash
# bash p9.sh [<hook module>], from the worktree root: the argv two comment shapes scan to, then one
# line per payload through the hook as gov-builder
set -u
HOOK=${1:-tools/hooks/scratch-guard.js}; ROOT=$(pwd -W); E=$(mktemp)
node -e 'const s=require(require("path").resolve(process.argv[1]));for(const c of process.argv.slice(2))console.log("argv",JSON.stringify(c),JSON.stringify(s.scanCommandHeads(c).map(h=>h.argv)))' \
  "$HOOK" 'sleep 9 # x' 'bash tools/hooks/agent-cap.test.sh # --render'
row() { # label · command
  node -e 'process.stdout.write(JSON.stringify({tool_name:"Bash",agent_type:"gov-builder",cwd:process.argv[1],tool_input:{command:process.argv[2]}}))' "$ROOT" "$2" \
    | node "$HOOK" 2>"$E"
  echo "row $1 exit $? $(grep -oE 'row [PG][0-9] [a-z0-9 ]+' "$E" | head -1)"
}
row C1 'sleep 3 # brief pause'
row C2 'sleep 9 # x'
row C3 'sleep 3 # a; sleep 9'
row C4 "echo ' #'; sleep 9"
row C5 'sleep 3#x'
row C6 'bash tools/hooks/agent-cap.test.sh # --render'
row F1 'sleep 5'
row F2 'sleep 1m'
row F3 'sleep 1h'
row F4 'sleep 1d'
row F5 'sleep infinity'
row F6 'sleep 4.9'
row F7 'sleep 4s'
```

This writer ran it at `2a13de8b6` on node a, once over the hook as it stands and once over a scratch
copy carrying §4's line (PINNED 2026-11-14):

| Row | at `2a13de8b6` | with the cut |
|---|---|---|
| argv of `sleep 9 # x` | `["sleep","9","#","x"]` | `["sleep","9"]` |
| argv of C6 | `["tools/hooks/agent-cap.test.sh","#","--render"]` | `["tools/hooks/agent-cap.test.sh"]` |
| C1, C3 | `exit 2 row P3` | `exit 0` |
| C2, C4, C5 | `exit 2 row P3` | `exit 2 row P3` |
| C6 | `exit 0` | `exit 2 row G3 suite` |
| F1 to F5 | `exit 2 row P3` | `exit 2 row P3` |
| F6, F7 | `exit 0` | `exit 0` |

### The corpus probe, `$SCRATCH/p9c.js`

It runs `checkRoleGate` as `gov-builder` in this checkout over every Bash call of session `db957487`,
through the module at `2a13de8b6` and the built one, and counts the commands whose verdict moved.

```js
// node p9c.js <base module> <new module> <session transcript dir> <checkout root>
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
const v = (m, cmd) => { try { const r = m.checkRoleGate(cmd, { agent_type: 'gov-builder', cwd: root }, {}); return r && r.deny ? (/row ([PG]\d)/.exec(r.deny) || [, 'deny'])[1] : 'admit' } catch (e) { return 'throw' } }
const n = { commands: cmds.length, same: 0, moved: 0, comment: 0 }
const shapes = {}
for (const cmd of cmds) {
  if (/(^|[\s;&|()<>])#/.test(cmd)) n.comment++
  const a = v(B, cmd), b = v(N, cmd)
  if (a === b) { n.same++; continue }
  n.moved++; const k = `${a} -> ${b}`; shapes[k] = (shapes[k] || 0) + 1
  if (n.moved <= 12) console.log('MOVED', k, JSON.stringify(cmd.slice(0, 160)))
}
console.log(Object.entries(n).map(([k, x]) => `${k} ${x}`).join(' · '))
console.log(JSON.stringify(shapes))
```

The base module is `git show 2a13de8b6:tools/hooks/scratch-guard.js`, written beside a copy of
`agent-cap.js` from the same commit, which it requires. The transcript directory is spec 6's:
`C:/Users/daily-agent/.claude/projects/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f`.
This writer ran it over the scratch copy carrying §4's line, and it printed
`commands 9301 · same 9301 · moved 0 · comment 155` in 11 s. The built module's verdicts there were
admit 9069, G1 63, G3 8, P1 104, P2 38 and P3 19, so the probe reads live verdicts. (PINNED 2026-11-14)

### The resume probe, `$SCRATCH/p9m7.py`

It drives `load_session_calls` alone over a three-line transcript: an `Agent` call, its `res` and
its notification. For the append case and the torn case it takes a record on the first part, seeds
`bad` to 7, writes the whole transcript, and reads it resumed and then cold.

```python
# python -I p9m7.py <handoff kit dir> <scratch dir>: the M7 poison, by load_session_calls alone
import json, pathlib, shutil, sys
sys.path.insert(0, sys.argv[1]); import handoff
d = pathlib.Path(sys.argv[2]); shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
lines = [json.dumps(x) + "\n" for x in (
    {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "toolu_A", "name": "Agent", "input": {"prompt": "m"}}]}},
    {"type": "user", "toolUseResult": {"status": "async_launched", "agentId": "a1"}, "message": {"content": [{"type": "tool_result", "tool_use_id": "toolu_A"}]}},
    {"type": "user", "message": {"content": "<task-notification>\n<tool-use-id>toolu_A</tool-use-id>\n<status>completed</status>\n</task-notification>"}})]
s, c = d / "s.jsonl", d / "rec"
def run(cache):
    calls, notified, bad = handoff.load_session_calls(s, cache)
    return "bad %d · result %s · notified %s" % (bad, (calls[0]["result"] or {}).get("agentId"), sorted(notified))
for case, first in (("append", lines[0]), ("torn", lines[0] + lines[1][:40])):
    shutil.rmtree(c, ignore_errors=True); s.write_text(first, encoding="utf-8"); run(c)
    rp = next(c.glob("*.json")); rec = json.loads(rp.read_text(encoding="utf-8")); rec["bad"] = 7
    rp.write_text(json.dumps(rec), encoding="utf-8"); s.write_text("".join(lines), encoding="utf-8")
    print(case, "resumed:", run(c), "| cold:", run(None))
```

This writer ran it at `2a13de8b6` on node a, and it printed (PINNED 2026-11-14):

```text
append resumed: bad 7 · result a1 · notified ['toolu_A'] | cold: bad 0 · result a1 · notified ['toolu_A']
torn resumed: bad 7 · result a1 · notified ['toolu_A'] | cold: bad 0 · result a1 · notified ['toolu_A']
```

### Inventory

| identifier | kind | lexicon |
|---|---|---|
| `bad` | a new `A23_EDIT` mode string in the roles suite | no declared cell |
| `W9-AC1` to `W9-AC4` row labels, C1 to C6 and F1 to F7 | suite row labels | no declared cell |

The comment cut mints no function, constant or export.

### Rollout

One pass, at order 8, beside TOOL-aTrimmedWait-8, whose write set holds none of these three files.
The close observes the three `New arm:` lines RED on their staged breaks and GREEN restored, and
confirms both floors from real runs.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- **Cut the comment in `checkPollWait` alone**, the record's first form. It cures the cited row and
  leaves C3 (a comment's `;` splits a command) and C6 (G3 admits on a comment's `--render`) standing.
- **Cut it in `buildCommandView`.** That moves the scratch arm's write and redirect verdicts too, and
  no item names them.
- **A named constant or helper for the cut.** It has one caller.
- **Strip the marker from the record**, the record's example poison. It cannot show the appended
  `res` attaching, as §4 says.
- **Add the poisoned arms beside the two vacuous ones.** The vacuous arms prove nothing the poisoned
  ones do not, so they are rewritten in place.

## 5. Production-readiness checklist

- security — the role gate stays fail-closed, and a comment can no longer carry an admitting word
  past G3. No new write, path or input.
- perf / scale — one regular-expression pass over the command per scan, in microseconds.
- error / empty / loading states — an empty comment, a `#` at the end of the text and a `#` alone on
  a line each blank to spaces and read as no command.
- observability — unchanged: each refusal names its row and the simple command, now without the
  comment.
- risks — a `#` the shell reads as a word but the cut reads as a comment would hide a gate word. No
  such shape is known, and the cut's word-start set is bash's. A suite whose only admitting word sits
  in a comment is now refused on G3 where it was admitted, and the corpus held none. That G3 move is
  the build rule's one exception, ruled by the owner in §8 F1.
- testing — the probes of §4, and 13 suite rows and two rewritten arms observed RED then GREEN at the
  close.
- migration — none.
- user docs — none: `help/roles.md` and the hooks README state nothing the cut makes false.

## 6. Acceptance criteria

`$SCRATCH` is the run's scratch directory. The probes are the §4 blocks.

- **AC1** — When `bash "$SCRATCH/p9.sh"` runs from the worktree root, the `argv` line for
  `sleep 9 # x` reads `[["sleep","9"]]`, rows C1 and C3 print `exit 0` with nothing after it, and rows
  C2, C4 and C5 print `exit 2 row P3 sleep at or over 5 s`.
  Red when: the cut is absent, so C1 and C3 exit 2, as at `2a13de8b6`; or it opens at any `#`, so C5
  exits 0; or it runs on the raw text, not the view, so C4 exits 0.
- **AC2** — When `bash "$SCRATCH/p9.sh"` runs, the `argv` line for C6's command holds one word, the
  suite path alone with no `#` and no `--render`, and row C6 prints `exit 2 row G3 suite`.
  Red when: the gate rows still read a comment's words, so C6 exits 0, as at `2a13de8b6`.
- **AC3** — When `node "$SCRATCH/p9c.js"` runs over the module at `2a13de8b6` and the built
  `tools/hooks/scratch-guard.js`, it prints `moved 0`.
  Red when: the cut moves a verdict a real command reached, for example by blanking a `#` the shell
  reads as part of a word.
  fixture: the session transcript directory named in §4, on node a today.
  figure: DERIVED at observation. §4's 9301 commands and 155 comment-bearing commands are PINNED.
- **AC4** — When `bash "$SCRATCH/p9.sh"` runs, rows F1 to F5 print `exit 2 row P3 sleep at or over 5 s`,
  and rows F6 and F7 print `exit 0` with nothing after it.
  Red when: `>=` becomes `>` in `checkPollWait`, so F1 exits 0; a suffix multiplier breaks, so F2, F3
  or F4 exits 0; or the decimal or `s` reading breaks, so F6 or F7 exits 2.
- **AC5** — When `grep -c '^run_role_bash "W9-AC' tools/hooks/scratch-guard.test.sh` runs, it prints
  13, and `grep -c '^FLOOR_ASSERTIONS=388$' tools/hooks/scratch-guard.test.sh` prints 1.
  Red when: rows are added without the floor raised, or the floor is raised past the rows.
  figure: DERIVED, 388 is 375 plus the 13 rows.
- **AC6** — When `python -I "$SCRATCH/p9m7.py" tools/roles "$SCRATCH/p9m7"` runs, both its lines
  print `resumed: bad 7 · result a1` and `cold: bad 0`.
  Red when: a resumed read drops the record's `bad` or fails to rebuild `by_id`, so the resumed half
  reads `bad 0` or `result None`. The cold half is the negative the arm's assertion needs.
- **AC7** — When `grep -c '"$A23_EDIT" "$A23D" bad' tools/roles/adopt-roles.test.sh` runs, it prints
  2, and `grep -c ': 7 line(s) did not parse' tools/roles/adopt-roles.test.sh` prints 2.
  Red when: the append or torn arm still asserts only the cold lines, which a re-read from byte 0
  also prints.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `policy fixtures` · `roles adopter self-test` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

`python tools/check-spec-tokens.py --legs-for` over the files touched names the first seven legs as
guarded by `tools/hooks/` or by `tools/hooks/scratch-guard.js`, beside the broad `tools/` guards it
excludes. `tools/roles/adopt-roles.test.sh` trips no guarded leg, and `roles adopter self-test` is
the unguarded leg that runs it. The kit-version legs are graded once the build's single version move
lands.

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 · rows W9-AC1 C1 to C5 and W9-AC2 C6; staged by removing the cut from `scanCommandHeads`, which refuses C1 and C3 and admits C6, and by cutting at any `#`, which admits C5 · `FLOOR_ASSERTIONS` 375 to 388, shared with the next line
New arm: tools/hooks/scratch-guard.test.sh · covers AC4 · rows W9-AC4 F1 to F7; staged by `>=` becoming `>` in `checkPollWait`, which admits F1, and by the `m` multiplier becoming 1, which admits F2 · the floor of the line above
New arm: tools/roles/adopt-roles.test.sh · covers AC7 · arm 23's append and torn arms, rewritten in place; staged by `read_session_record` taking a record only at `offset` equal to the file size, the record's own regression, which makes both resumes cold and drops the note · none, the floor stays 69

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
`memory hygiene`, the lexicon and `check-spec-tokens.py --spec` over this file.

## 8. Open questions

- **F1 — Where does M2's comment cut go, given that the build rule says no verdict moves?**
  - Shared cut in `scanCommandHeads`, the record's better form (recommended). Every role-gate row
    reads the same words, and the comment shapes C1, C3 and C6 are all cured. One G3 verdict moves
    toward refusal: a suite whose only admitting word sits in a comment, such as
    `bash <suite> # --render`. The measured corpus moved no verdict.
  - Cut in `checkPollWait` alone, the record's first form. No gate verdict moves, but it cures only
    the cited P3 row. A comment's `;` still splits a command (C3), and G3 still admits on a
    comment's `--render` (C6).

  RESOLVED (owner, 2026-11-14): shared cut in scanCommandHeads

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft from the promotion brief
  `2026-11-14-prompt-TOOL-aTrimmedWait-9-promotion`, taking review items M2, L2 and M7 of
  `2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1`, grounded at `2a13de8b6`.
- rev-2 · 2026-11-14 · §3 · §4 · §5 · §8 · the owner's ruling of 2026-11-14, relayed by the main loop,
  recorded as F1: the comment cut stays shared in `scanCommandHeads`, and the one G3 verdict it moves
  is stated as the build rule's exception in §3 and §5. The header gains `ratified 2026-11-14`. The
  `bad`-count poison for M7 stands as written. No design change.

## 10. Reuse audit

The seam this unit extends is `scanCommandHeads` in `tools/hooks/scratch-guard.js`, the one scanner
both the gate rows and the polling rows read. Its view, `buildCommandView`, already blanks quotes and
heredoc bodies, so the cut reuses that quote handling rather than adding a second tokenizer. S2 adds
rows through the suite's `run_role_bash`, and S3 extends arm 23's `A23_EDIT` and `run_agents23`.
`python tools/codebase-map/reuse_lookup.py "read a shell command's words with its trailing comment
removed"` and `"test that a resumed transcript read used its cached record rather than re-parsing"`
ranked name stems only (`read_text`, `read`, `parse`, `read_conf_key`), none of which reads a command
or a session record. `readConfKey` (`scratch-guard.js@3220edce42ac:838`) drops a trailing comment
from a conf assignment line, which is a different grammar, so no existing seam fits beyond the
scanner. Recall returned this review's M2, spec 6's inventory, and earlier specs naming
`scanCommandHeads` and `buildCommandView` as the scanner to extend (TOOL-dFurnishedOrders-14,
TOOL-dBoundRoles-8). It returned no record of a comment cut in the scanner.

Recall terms used: `python tools/memory-recall/query.py "how does a hook read past a shell comment, and how is a resumed cache read proven in a test" --terms "scratch-guard scanCommandHeads buildCommandView comment checkPollWait P3 floor deriveSleepSeconds handoff session record resume poison arm"`
