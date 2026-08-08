#!/usr/bin/env node
// check-workflow-syntax.js — parse every workflow script in the dialect its RUNTIME evaluates.
//
//   node tools/workflows/check-workflow-syntax.js            # every tracked workflow script
//   node tools/workflows/check-workflow-syntax.js <file>...   # explicit files (used by the self-test)
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

function tracked() {
  const out = execFileSync('git', ['ls-files', '--', '*.js'], { encoding: 'utf8' })
  return out.split('\n').filter((p) => p.startsWith('tools/') && p.endsWith('.js'))
}

let files = process.argv.slice(2)
let explicit = files.length > 0
if (!explicit) {
  try {
    files = tracked()
  } catch (e) {
    console.error(`workflow-syntax: cannot list tracked files (${e.message})`)
    process.exit(2)
  }
}

let checked = 0
let bad = 0
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
  const body = src.replace(/^export\s+(const|let|var|function|class|async)\b/gm, '$1')
  try {
    new AsyncFunction(...HOOKS, body)
  } catch (e) {
    console.log(`workflow-syntax: ${f} — ${e.name}: ${e.message}`)
    bad++
  }
}

if (bad) {
  console.log(`workflow-syntax: ${bad} file(s) failed to parse`)
  process.exit(1)
}
// A discovery run that found NOTHING is not a pass — it is a gate whose population evaporated
// (a renamed directory, a dropped marker). Say so and fail rather than print a green line.
if (!explicit && checked === 0) {
  console.log('workflow-syntax: no workflow script found under tools/ — the population is empty, which is not a pass')
  process.exit(1)
}
console.log(`workflow-syntax: ${checked} workflow script(s) parsed clean`)
