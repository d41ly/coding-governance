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
finds ONE call, a shell function `t(){ …; "$@"; }` invoking a suite through `"$@"`, which is the
run-time-assembly ceiling and stays a near-miss by design. Every D1 near-miss is one of two kinds:
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
off within a day. Spec rev-5 admits `bash -n`/`sh -n` in front of a D2 to D4 token; nothing else
in the tables above moves, because those forms were never hits.

The ORDER is the finding either way: D4 is 1518 of the 1929 command-level hits and 574 of them
came from a sidechain, which is the population the child prompt's instruction cannot reach and the
hook can.

## The probe, verbatim

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
}
const keyOf = (h) => {
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
