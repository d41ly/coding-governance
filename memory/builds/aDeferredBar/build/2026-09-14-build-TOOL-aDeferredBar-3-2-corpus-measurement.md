# The corpus measurement — the shipped predicate over every shell call this node has issued

**Serves:** journal TOOL-aDeferredBar-3

Spec §4 pinned a first-cut table to 2026-09-13 and AC11 said the build re-derives it from the
SHIPPED predicate. This is that reading, taken on node `a` on 2026-09-14 by the probe below, which
`require`s the hook's exported `scanDenyHits`, `scanSegments` and `buildCommandView` and READS the
transcript store: it builds nothing and runs nothing. Two readings were taken, because the first
one changed the spec.

## The corpus

`~/.claude/projects/C--projects-coding-governance*/**/*.jsonl`: 3134 files, 104 559 `Bash` or
`PowerShell` `tool_use` commands, 79 514 of them with `isSidechain` set. The store grows while a
session runs — this pass's own calls are in it, and the count moved by 9 between the two readings —
so every figure here is the reading at the moment it was taken and nothing else.

## Reading 1 — the rev-3 grammar, and what it missed

The predicate as the spec's rev-3 §4 spelled it (separators `;` `&&` `||` `|` `(` `then` `do`
`else`; prefix words `env`, `export`, `NAME=value`, `timeout N`, `bash`/`sh` with one short
option) measured D4 at 1471 hits and 7289 near-misses. A near-miss is the row's token present in
the raw text with no hit for that row, and AC11 reds when a listed near-miss is a RUN. Walking the
D4 near-misses whose token survived in the blanked view and sat after `bash` or `sh` — the shape a
run has — found 89, and classifying each by the word before `bash` gave:

| word before `bash` | calls | what it is |
|---|---|---|
| `time` (bare, after `(`, at line start) | 31 | a run, timed |
| `nohup` | 4 | a run, backgrounded |
| `{` | 3 | a run inside a brace group |
| a shell function (`t(){ "$@" …}`, `run(){ … }`) | 3 | the assembled-at-run-time class §3 states as the ceiling |
| a quote or heredoc tag, `-eL`, `25`, `420` | 8 | mentions, or a `timeout` behind `time` |
| the rest | 40 | `cat`, `sed`, `wc`, `grep`, `git diff`, `cp`, `python - <<'PY'` — mentions |

Thirty-eight runs among the near-misses is the RED that criterion defines, so the spec moved:
rev-4 adds `{` to the separators and `time` and `nohup` to the prefix words, and the hook follows
it. The D2 count of 74 against the spec's 148 is NOT a miss of the same kind: 64 of the rev-3
command-position D2 calls carry `--check` (31), `--list` (24), `--rank` (7) or `--help` (2), and
this predicate excludes them by design (§8 F6) where the 2026-09-13 probe admitted them; walking
the 696 D2 near-misses visible in the view found no run at all. Likewise 67 D4 calls carry
`--render` (60) or `--check` (7). The first cut also counted per TOKEN where this probe counts per
COMMAND: per token the shipped predicate reads D1 314, D2 84, D3 38, D4 1816, which with the
read-only forms added back (D2 +93, D3 +6, D4 +73 segments) brackets the first cut's figures.

## Reading 2 — the shipped predicate, rev-4

Printed by the probe in about 14 s:

```
corpus: 3134 files · 104559 Bash/PowerShell tool_use commands · 79514 sidechain
| shape | hits | sidechain | near-misses | via D5 |
|---|---|---|---|---|
| D1 GATE_FULL= | 253 | 62 | 212 | 0 |
| D1 GATE_SELFTESTS= | 53 | 1 | 88 | 0 |
| D2 | 74 | 32 | 811 | 0 |
| D3 | 31 | 5 | 671 | 0 |
| D4 | 1518 | 574 | 7244 | 8 |
| plain bar, allowed | 422 | 155 | — | — |
```

D4 rose 1471 to 1518 — the 47 runs the widened grammar reaches, the 38 classified above plus the
ones a `time` in front of a `timeout` hid. After rev-4 the same walk over run-shaped near-misses
found ONE call, a shell function `t(){ …; "$@"; }` invoking a suite through `"$@"`, which is the
run-time-assembly ceiling and stays a near-miss by design — **and that count was wrong; Reading 3
below replaces it.** The walk read only the tokens that SURVIVED in the blanked view, so it could
not see a suite inside a double-quoted `$( … )`, which the view blanked as string content, and it
filed `-eL` and `120` as mention heads when they were `stdbuf -oL -eL bash <suite>` and
`timeout -k 5 120 bash <suite>`, both runs. Every D1 near-miss is one of two kinds:
166 carry the token only inside a string or a heredoc body, and 91 are the empty assignment or a
bare `grep GATE_FULL=` argument — the OFF spelling and a mention, neither a flagged bar. The D3
near-misses are `sed -n`, `grep -n`, `wc -l` and `cat` over the runner's own source.

The near-miss examples the probe printed, first six per row, every one a mention and not a run:
python heredocs editing a file that spells the token, `git commit -q -F - <<'MSG'` messages,
`cat > memory/builds/…` records, `echo "=== is run-selftests.…"`, `sed -n '1,60p'` and `grep -n`
over the runner and suite sources, and `bash tools/unattended/unattended.sh --dispatch … --writes
tools/unattended/check-unattended.test.sh`, where the suite name is a `--writes` argument behind
`unattended.sh` at command position.

**A third reading came from the wired hook itself.** Minutes after S4, the hook denied this pass's
`bash -n gate-guard.test.sh` — a syntax check that executes nothing. The corpus holds 412 raw
`bash -n <suite>` mentions (57 on the driver suite alone), so a hook denying them would be switched
off within a day. Spec rev-5 admits `bash -n`/`sh -n` in front of a D2 to D4 token. This record
first said nothing else in the tables above moved "because those forms were never hits", which
was false: under rev-4 the head after `bash -n` WAS the suite, so every one of those calls was a
D4 hit, and rev-5 moved D4 down by about 210 commands. Reading 3 carries the rev-5 figure.

The ORDER is the finding either way: D4 is 1518 of the 1929 command-level hits and 574 of them
came from a sidechain, which is the population the child prompt's instruction cannot reach and the
hook can.

## Reading 3 — the closing round's fold, an A/B over one corpus

Taken 2026-09-14 on node `a` at the closing review's fold of F2, F7 and F8, by the probe below with
one addition — a `D4 selftest.py` row, keyed on a D4 or D5 hit whose token ends `selftest.py`, so
the whole-suite python legs F2 added to row D4 are counted apart from the `.test.sh` ones. BOTH
hooks were run over the SAME store in one sitting — the shipped rev-5 hook as `8b5b3f0c` holds it,
and the fold — because the store grows while a session runs and a figure from Reading 2 is not
comparable to one taken now. 3157 files, 105 497 commands, 80 423 sidechain.

| shape | rev-5 hits | sidechain | near-misses | fold hits | sidechain | near-misses |
|---|---|---|---|---|---|---|
| D1 GATE_FULL= | 253 | 62 | 233 | 253 | 62 | 233 |
| D1 GATE_SELFTESTS= | 53 | 1 | 102 | 53 | 1 | 102 |
| D2 | 44 | 31 | 849 | 47 | 34 | 846 |
| D3 | 21 | 4 | 682 | 22 | 5 | 681 |
| D4 `.test.sh` | 1305 | 546 | 7640 | 1372 | 585 | 7573 |
| D4 `selftest.py` | 0 | 0 | 3513 | 782 | 357 | 2731 |
| plain bar, allowed | 423 | 156 | — | 434 | 165 | — |

What each delta is. **F2**: 782 commands in this store ran a whole-suite `selftest.py`, 357 of
them from a sidechain, and the shipped hook admitted every one — the largest single hole the
predicate had, and invisible to Reading 2 because its token set was the `.test.sh` convention. The
2731 remaining `selftest.py` near-misses were walked the same way as the `.test.sh` ones: NONE
carries a python launcher in front of a `selftest.py` token in the blanked view — every one is a
mention, `grep`/`sed`/`cat`/`git diff` over the file, its name inside a heredoc or a quoted
string. (The `--selftest` FLAG form is not in this row at all: its token is `--selftest`, not
`selftest.py`, and the hook admits it at BUILDING because the flag is textual. What the parity
arms assert about it, amended at closing round 2 R3 — the round-1 sentence here said they assert
its admission, and they asserted nothing about it, having dropped the flag form by rule: every
`chunk = selftests` leg of the manifest is in the population; a `--selftest` leg whose ceiling is
at or under the arms' declared 300 s bound is printed as the exempt direct check it is; a
`--selftest` leg above the bound is declared by name with its ceiling — `corpus_ids.py` at 2690 s
and `gen_build_index.py` at 350 s today — or reds; and graded plus printed exemptions must equal
the manifest's count. The hook still admits those two; the arms now say so instead of hiding
them.) **F7**: the 67 `.test.sh` commands, 3 `run-selftests.sh` commands and 1
`run-unattended-gates.sh` command that joined the hit columns are the three shapes the review named
— a suite inside a double-quoted `$( … )`, `timeout` with options before its duration, and
`stdbuf`/`nice`/`ionice` in front of the launcher — plus a fourth the re-walk surfaced, `time` by
path (`/usr/bin/time -f '%e' bash <suite>`). The plain-bar column rose by the 11 `timeout -k`
invocations of the plain bar the grammar now reads through. **F8**: D1 does not move — the
`$env:` spelling has zero corpus instances, as spec §3 recorded; the arm exists because it is the
second wired tool's only spelling of the act, not because the store holds one.

**The near-miss walk, corrected.** Run over the blanked VIEW of every `.test.sh` command the hook
does not deny, keeping only a `bash`/`sh` launcher followed by a `.test.sh` token that survives
blanking, in a simple command carrying none of `READ_ONLY_VERBS` and no `-n` — the same method
Reading 2 used, with the two exclusions it applied by hand made explicit. Against the rev-5 hook
it finds FIVE run-shaped near-misses, not one: `stdbuf -oL -eL bash <suite>`,
`timeout -k 5 120 bash <suite>`, `/usr/bin/time -f 'real %e' bash <suite>`, and two shell
functions (`t(){ …; "$@"; }` and `run(){ …; "$@"; }`) invoking a suite through `"$@"`. The
double-quoted `$( … )` shape does not appear in that count because the rev-5 view blanks it —
which is exactly what the earlier walk could not see, and why its ONE was wrong. Against the
fold's hook the same walk finds TWO, both the shell-function `"$@"` class, the run-time-assembly
ceiling spec §3 states and the header's `ponytail:` line owns. Every other class the raw text
offers — 132 `&&`-led, 75 `PY`-led, 16 `PYEOF`-led — is a token inside a heredoc body or a quoted
string, a mention, and the walk over the raw text that produced those figures is the
over-inclusive one this correction retires.

## Reading 4 — closing round 2, the substitution scan, an A/B over one corpus

Taken 2026-09-14 on node `a` at the round-2 fold of R5, R6 and R13, by the Reading 3 probe
unchanged, both hooks over one store in one sitting — the rev-6 hook as `4d177329` holds it and the
fold. 3172 files, 106 161 commands, 81 080 sidechain. The fold reads a double-quoted `$( … )` or
backtick span as a command of its own instead of keeping it in the view, and every row moves the
way that predicts: rev-6 → fold, D2 47 → 44, D3 22 → 23, D4 `.test.sh` 1383 → 1318, D4
`selftest.py` 782 → 766, the plain bar 435 → 424, D1 unmoved at 253 and 53; the near-miss columns
rise by exactly what the hit columns lose. A diff probe over the same store listed every command
the two predicates classify differently: 84 distinct commands rev-6 denied and the fold reads as
mentions — every one a `sed -n "$(grep -n … <suite>),+Np" <suite>`, `echo "… $(grep -c … <suite>)"`
or a string tail after a substitution, the false-deny class R5 and R6 named, and one of them the
`sed -n` read this very fold typed and was denied on — and ONE the fold denies that rev-6 admitted:
a `python -c "…"` whose double-quoted source carries the prose `` `run-unattended-gates.sh` `` in
backticks. Bash runs that span before python sees it, so the deny is the truth about the command
as typed; the author got an empty substitution in the source either way. The near-miss walk of
Reading 3 stands: the two shell-function `"$@"` cases are the only run-shaped near-misses, and the
84 retired hits joined the mentions rather than the runs.

## Reading 5 — closing round 3, a diff probe over one corpus

Taken 2026-09-14 on node `a` at the round-3 fold of T1 to T8, as a DIFF and not a table: both hooks
— the rev-7 hook as `67a11487` holds it and the fold — over one store in one sitting, 3187 files,
106 653 commands, each hook handed the record's own `tool_name` (the fold reads it; the rev-7 hook
ignores a fourth argument), printing every command the two classify differently. Nine distinct
commands, and every one is a round-3 review lens's or skeptic's own probe of the shapes it was
reporting: one the rev-7 hook denied and the fold admits — a PowerShell probe whose double-quoted
string carries a backtick-escaped `$env:`, the T3 false-deny class — and eight the fold denies and
rev-7 admitted, each a scratch-tree harness feeding `<<EOF` bodies, `$Env:GATE_FULL= 1` or a
`bash -c` inside a span to a stub suite. No working command of any session moves. The unquoted
heredoc (T1) is the shape with the widest reach in principle — `git commit -F - <<EOF` and
`python - <<EOF` are common spellings — and the diff says this store holds no such body carrying a deny
shape inside a `$( … )` or backticks outside the probes, which is why the table was not re-taken:
a diff of nine probes moves no row. The near-miss walk of Reading 3 stands.

## The probe, verbatim (Reading 3 form — the `D4 selftest.py` key is its one addition over Reading 2)

```js
#!/usr/bin/env node
// gate-guard corpus probe — TOOL-aDeferredBar-3 AC11. READS the transcript store, builds nothing.
//   node gate-guard-probe.js <hook.js> <store-dir> [project-prefix]
// For every Bash/PowerShell tool_use command in every *.jsonl under <store-dir>/<project-prefix>*,
// runs the SHIPPED predicate and prints, per row, hits at command position in the blanked view, of
// which sidechain, and near-misses: the row's token present in the raw text with no hit for that
// row. Also the plain-bar count (run-gates.sh at command position with no D1 hit). Near-miss
// examples are printed so a reader can confirm each is a mention and not a run.
'use strict'
const fs = require('fs')
const path = require('path')
const hook = require(path.resolve(process.argv[2]))
const store = process.argv[3]
const prefix = process.argv[4] || 'C--projects-coding-governance'

const TOKENS = {
  'D1 GATE_FULL=': /GATE_FULL=/,
  'D1 GATE_SELFTESTS=': /GATE_SELFTESTS=/,
  D2: /run-selftests\.sh/,
  D3: /run-unattended-gates\.sh/,
  D4: /\.test\.sh\b/,
  'D4 selftest.py': /selftest\.py\b/,
}
const keyOf = (h) => {
  if ((h.row === 'D4' || h.row === 'D5') && /selftest\.py$/.test(h.token)) return 'D4 selftest.py'
  const r = h.row === 'D1' ? (h.token.startsWith('GATE_FULL=') ? 'D1 GATE_FULL=' : 'D1 GATE_SELFTESTS=') : h.row
  if (r === 'D5') return h.what === 'flag' ? (h.token.startsWith('GATE_FULL=') ? 'D1 GATE_FULL=' : 'D1 GATE_SELFTESTS=')
    : (/run-selftests\.sh$/.test(h.token) ? 'D2' : /run-unattended-gates\.sh$/.test(h.token) ? 'D3' : 'D4')
  return r
}

const stats = {}
for (const k of Object.keys(TOKENS)) stats[k] = { hits: 0, side: 0, near: 0, nearEx: [], d5: 0 }
let plain = 0, plainSide = 0, files = 0, calls = 0, sideCalls = 0

function walk(dir, out) {
  let names
  try { names = fs.readdirSync(dir, { withFileTypes: true }) } catch { return }
  for (const e of names) {
    const p = path.join(dir, e.name)
    if (e.isDirectory()) walk(p, out)
    else if (e.name.endsWith('.jsonl')) out.push(p)
  }
}
const list = []
for (const e of fs.readdirSync(store)) if (e.startsWith(prefix)) walk(path.join(store, e), list)

for (const f of list) {
  files++
  let text
  try { text = fs.readFileSync(f, 'utf8') } catch { continue }
  for (const line of text.split('\n')) {
    if (!line.includes('"tool_use"')) continue
    let rec
    try { rec = JSON.parse(line) } catch { continue }
    const content = rec && rec.message && Array.isArray(rec.message.content) ? rec.message.content : []
    for (const c of content) {
      if (!c || c.type !== 'tool_use' || !hook.TOOLS.includes(c.name)) continue
      const cmd = c.input && typeof c.input.command === 'string' ? c.input.command : ''
      if (!cmd) continue
      calls++
      const side = !!rec.isSidechain
      if (side) sideCalls++
      const hits = hook.scanDenyHits(cmd, hook.buildCommandView(cmd), 0)
      const hitKeys = new Set(hits.map(keyOf))
      for (const h of hits) if (h.row === 'D5') stats[keyOf(h)].d5++
      for (const k of hitKeys) { stats[k].hits++; if (side) stats[k].side++ }
      for (const [k, rx] of Object.entries(TOKENS)) {
        if (!rx.test(cmd) || hitKeys.has(k)) continue
        stats[k].near++
        if (stats[k].nearEx.length < 6) stats[k].nearEx.push(cmd.replace(/\s+/g, ' ').slice(0, 110))
      }
      // the plain bar: run-gates.sh at command position with no D1 hit
      if (!hitKeys.has('D1 GATE_FULL=') && !hitKeys.has('D1 GATE_SELFTESTS=')) {
        const segs = hook.scanSegments(cmd, hook.buildCommandView(cmd))
        if (segs.some((t) => t.some((w, i) => /run-gates\.sh$/.test(w) && t.slice(0, i).every((p) => /^(bash|sh|env|timeout|\d+[smhd]?|[A-Za-z_][A-Za-z0-9_]*=.*|-[A-Za-z]+)$/.test(p))))) {
          plain++; if (side) plainSide++
        }
      }
    }
  }
}

console.log(`corpus: ${files} files · ${calls} Bash/PowerShell tool_use commands · ${sideCalls} sidechain`)
console.log('| shape | hits | sidechain | near-misses | via D5 |')
console.log('|---|---|---|---|---|')
for (const [k, s] of Object.entries(stats)) console.log(`| ${k} | ${s.hits} | ${s.side} | ${s.near} | ${s.d5} |`)
console.log(`| plain bar, allowed | ${plain} | ${plainSide} | — | — |`)
console.log('\nnear-miss examples (mentions, not runs):')
for (const [k, s] of Object.entries(stats)) for (const ex of s.nearEx) console.log(`  ${k}: ${ex}`)
```
