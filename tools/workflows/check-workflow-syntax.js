#!/usr/bin/env node
// check-workflow-syntax.js — parse every workflow script in the dialect its RUNTIME evaluates.
//
//   node <prefix>/workflows/check-workflow-syntax.js            # every workflow script git can see
//   node <prefix>/workflows/check-workflow-syntax.js <file>...   # explicit files (used by the self-test)
//
// Exit 0 = every file parsed · 1 = at least one SyntaxError (printed with its file) · 2 = bad usage.
//
// WHY NOT `node --check`: measured on node v24, `node --check` exits 0 on a file whose parse
// genuinely fails (`export const x=1` + `let y=(` → exit 0, no output). Module auto-detection retries
// the parse and swallows the failure, so `--check` is a gate that cannot go red. It was written into
// this unit's acceptance criteria and caught by RUNNING it — see review 1, finding R1.
//
// WHY AN ASYNC FUNCTION BODY: a workflow script is neither CommonJS nor an ES module. It uses
// `export const meta`, top-level `await` AND top-level `return`, and no standard parser mode accepts
// all three. The Workflow runtime evaluates the body as an async function with the hooks injected as
// parameters, so that is the shape this gate parses: strip the leading `export` keyword, then hand
// the source to the AsyncFunction constructor. Constructing does NOT execute it.
//
// A SECOND PASS OVER THE SAME POPULATION (TOOL-aGraftedHelix-32 S2): a code line carrying a
// `git commit` ANYWHERE, `git -C <dir> commit` and `git -c <k=v> commit` included, and no ` -- `
// exits 1, naming the file and the line. A pathless commit takes the WHOLE index, so an entry staged
// before the block an agent runs - the run's own RUN.md, which the driver's verbs leave staged -
// rides a commit nobody meant it to. A line whose trimmed text opens `//` or `*` is a comment and is
// not graded; `git commit-tree` reads no index and is not in the population. The pass prints how
// many lines it graded, and in discovery mode a zero beside the build harness's render, which
// carries a commit line by construction, is a DEAD PROBE that exits 1 (TOOL-aGraftedHelix-36 S7);
// any other zero is printed as the count it is.
// WHAT THE PASS DOES NOT CHECK: a commit command built at run time from pieces, a commit an agent
// composes from prose, a ` -- ` that sits inside a message argument, which reads as a pathspec, a
// `git` reached through a variable or a wrapper function, a global option other than `-c` or `-C`
// between `git` and `commit`, a command continued across lines, and a trailing `//` comment on a
// code line, which is graded as code.
'use strict'
const fs = require('fs')
const { execFileSync } = require('child_process')

const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor
// The globals the Workflow runtime injects. They are declared as parameters so a reference to one is
// a plain identifier resolution at parse time rather than an undefined-variable question.
const HOOKS = ['args', 'agent', 'parallel', 'pipeline', 'phase', 'log', 'budget', 'workflow']
// A workflow script IDENTIFIES ITSELF by exporting `meta`. Deriving the population from that marker
// instead of a path list means a new workflow is covered the day it lands, and a gate/helper script
// that happens to live in the same directory is not mis-parsed as one.
const MARKER = /^\s*export\s+const\s+meta\s*=/m
// A `git commit` anywhere on a code line, through any `-c`/`-C` global options (S2's pass, widened by
// TOOL-aGraftedHelix-36 S7). The `(?![-\w])` tail keeps `git commit-tree` out of the population.
const COMMIT_LITERAL = /\bgit(\s+-[cC]\s+\S+)*\s+commit(?![-\w])/

// --cached AND --others: a workflow script is parsed the moment it exists rather than the moment it
// is staged, which is when its syntax actually matters — the runtime will happily be handed an
// unstaged file. --exclude-standard keeps ignored files out, so a scratch script opts out with a
// .gitignore line.
function discovered() {
  const out = execFileSync('git', ['ls-files', '--cached', '--others', '--exclude-standard', '--', '*.js'], { encoding: 'utf8' })
  // NO PREFIX FILTER. MARKER is applied to every candidate below, so the population is already
  // `a file declaring workflow meta` and a prefix would do nothing except hide the harnesses
  // adopters keep under `.claude/workflows/`. check-verifier-fanout.sh applies the same marker
  // and takes the same shape (TOOL-aRepatriatedFork-4); check-review-join.sh applies none, so it
  // keeps its derived prefix and adds `.claude/workflows/` to it. TOOL-dRetiredFork-10.
  // A `*.template.js` is a RENDER SOURCE and not a script any runtime evaluates: its
  // `{{FANOUT_CAP}}` token sits where a number goes (TOOL-aRepatriatedFork-7 S7). Its render is in
  // this population, and check-protocol-parity.test.sh pins that render to it.
  const seen = new Set(out.split('\n').filter((p) => p.endsWith('.js') && !p.endsWith('.template.js')))
  return [...seen].sort()
}

let files = process.argv.slice(2)
let explicit = files.length > 0
if (!explicit) {
  try {
    files = discovered()
  } catch (e) {
    console.error(`workflow-syntax: cannot list tracked files (${e.message})`)
    process.exit(2)
  }
}

let checked = 0
let bad = 0
let pathless = 0
let graded = 0
let carrier = false
for (const f of files) {
  let src
  try {
    src = fs.readFileSync(f, 'utf8')
  } catch (e) {
    console.log(`workflow-syntax: cannot read ${f} — ${e.message}`)
    bad++
    continue
  }
  // In discovery mode the marker selects the population. With explicit files the caller has already
  // decided, so an unmarked file is still parsed — otherwise a fixture would be skipped rather than
  // judged, and the self-test's RED arm would pass by not looking.
  if (!explicit && !MARKER.test(src)) continue
  checked++
  // The one render that carries a commit line by construction: the spec commit stage's.
  if (f === 'unattended-build.js' || f.endsWith('/unattended-build.js')) carrier = true
  const body = src.replace(/^export\s+(const|let|var|function|class|async)\b/gm, '$1')
  try {
    new AsyncFunction(...HOOKS, body)
  } catch (e) {
    console.log(`workflow-syntax: ${f} — ${e.name}: ${e.message}`)
    bad++
  }
  src.split('\n').forEach((line, i) => {
    const t = line.trim()
    if (t.startsWith('//') || t.startsWith('*')) return
    if (!COMMIT_LITERAL.test(line)) return
    graded++
    if (!line.includes(' -- ')) {
      console.log(`workflow-syntax: ${f}:${i + 1} — a git commit with no \` -- \` pathspec commits the whole index, so an entry staged before it rides the commit`)
      pathless++
    }
  })
}

if (bad) console.log(`workflow-syntax: ${bad} file(s) failed to parse`)
if (pathless) console.log(`workflow-syntax: ${pathless} pathless git commit line(s)`)
if (bad || pathless) process.exit(1)
// THE COMMIT PASS'S LIVENESS. The build harness's render carries the spec commit's `git commit` line,
// so a discovery run that graded none beside it matched nothing it exists to grade.
if (!explicit && graded === 0 && carrier) {
  console.log(`workflow-syntax: graded 0 git commit lines while the build harness render is present — the pass matched nothing it exists to grade`)
  process.exit(1)
}
console.log(`workflow-syntax: graded ${graded} git commit line(s)`)
// A discovery run that found NOTHING is not a pass — it is a gate whose population evaporated
// (a renamed directory, a dropped marker). Say so and fail rather than print a green line.
if (!explicit && checked === 0) {
  console.log('workflow-syntax: no file declaring workflow meta was found — the population is empty, which is not a pass')
  process.exit(1)
}
console.log(`workflow-syntax: ${checked} workflow script(s) parsed clean`)
