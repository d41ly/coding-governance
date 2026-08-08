#!/usr/bin/env node
/**
 * agent-cap — project-agnostic PreToolUse guard against unbounded Workflow fan-out.
 *
 * WHY: `Workflow` `parallel()` / `pipeline()` fan out to the harness cap
 * (min(16, cores-2) ≈ 14). Large concurrent agent bursts saturate server
 * throughput and trip the SERVER rate limiter — killing whole review phases
 * and burning millions of subagent tokens for zero output. That cap is NOT
 * lowerable from userland, and workflow sidechains don't run hooks — so the
 * only preventive lever is to scan the Workflow *tool call* (a main-loop call
 * that DOES fire PreToolUse) and reject scripts that use the raw fan-out
 * primitives instead of the capped helpers.
 *
 * CONTRACT: route ALL fan-out through boundedParallel(thunks, CAP) /
 * boundedPipeline(items, CAP, ...stages). The sanctioned helper bodies are the
 * ONLY place a raw `parallel(`/`pipeline(` may appear, and each such line
 * carries a `gov:bounded-fanout` marker. Any other raw primitive call = deny.
 *
 * CAP: default 5 (override with env AGENT_CAP). This guard doesn't verify the
 * numeric arg — it enforces "use the helper"; the helper is where CAP lives.
 *
 * Wiring (per project): run `python tools/settings-merge.py` (idempotent) — it merges the block
 * below into .claude/settings.json; or merge it by hand:
 *   "hooks": { "PreToolUse": [ { "matcher": "Workflow",
 *     "hooks": [ { "type": "command",
 *       "command": "node \"${CLAUDE_PROJECT_DIR}/<path>/agent-cap.js\"" } ] } ] }
 * Blocks via exit 2 + stderr (version-robust; no JSON-schema dependency).
 *
 * ponytail: a static scan can't prove a dynamically-built array is ≤CAP — this
 * enforces "use the helper", killing the exact `parallel(items.map(...))`
 * pattern that causes the bursts. Ceiling: line comments AND quoted-string
 * literals are stripped before the scan; block comments naming the primitive
 * are NOT — still trips the guard (benign, fail-closed).
 */
'use strict'

const KIT_AGENT_CAP_VERSION = '1.1' // gov:kit agent-cap@1.1 — engine identity (this file is deployed verbatim; the constant is the deployer's version marker)
const CAP = Number(process.env.AGENT_CAP) || 5

function readStdin() {
  try {
    return require('fs').readFileSync(0, 'utf8')
  } catch {
    return ''
  }
}

// Blank the CONTENTS of single/double-quoted string literals so a `parallel(`
// mentioned in prose (a meta.description, a log message) isn't read as a call.
// Template literals (backticks) are left ALONE — they can hold real ${code}.
// Escapes handled; an unbalanced quote (e.g. inside a comment) is left as-is.
// Run BEFORE the line-comment strip so a `//` inside a string can't truncate it.
function stripStrings(line) {
  return line.replace(/'(?:\\.|[^'\\])*'/g, "''").replace(/"(?:\\.|[^"\\])*"/g, '""')
}

function offendingLines(script) {
  // Case-sensitive: primitives are lowercase `parallel`/`pipeline`; the helpers
  // are `boundedParallel`/`boundedPipeline` (capital P) so they never match.
  // Lookbehind rejects `.parallel(` / `xparallel(` member/identifier hits.
  const raw = /(?<![.\w$])(parallel|pipeline)\s*\(/
  return script
    .split(/\r?\n/)
    .map((line, i) => ({ line, n: i + 1 }))
    .filter(({ line }) => {
      if (line.includes('gov:bounded-fanout')) return false // sanctioned helper line
      const code = stripStrings(line).split('//')[0] // strings blanked, then line-comments
      return raw.test(code)
    })
}

// ---------------------------------------------------------------------------
// RULE 2 — the VERIFIER ARITY rule (memory/guides/REVIEW-PROTOCOL.md).
//
// A review's verify stage spawns at most 5 agents WHATEVER the finding count. Rule 1 above does not
// give that: it bounds CONCURRENCY, so N findings still spawn N agents, five at a time. Concurrency
// is not a budget. The failure this rule exists for was written as an INLINE `script` on a Workflow
// tool call — never a file — which is why the check lives here, at the tool call, and not only in a
// gate over `tools/**/*.js` that structurally cannot see one.
//
// WHY A WHITELIST. Provenance is undecidable from a line. `batches.map((g) => () => agent(...))` is
// the SAME TEXT whether `batches` came from a bounded split or from `chunk(all, 1)`, so a blacklist
// of banned spellings bans a spelling and not the defect. Instead: an `agent(` reached through an
// iteration construct must have a receiver this file can see is bounded.
//
// ALLOWED receivers:
//   (a) an identifier assigned on a line marked `gov:fixed-verifiers`, where that line spells
//       chunk(x, Math.ceil(x.length / K)) or splitInto(x, K) and K is an integer literal <= 5 or an
//       identifier bound in this file to one. The marker is the AUTHOR'S CLAIM; the shape check is
//       what stops the claim being made falsely — `chunk(all, 1) // gov:fixed-verifiers` reds.
//   (b) an identifier assigned from an ARRAY LITERAL with <= 6 elements — the finder-lens case,
//       where the agent count is a constant visible in the source.
// Everything else is denied, including a for/while/forEach body containing `agent(`: a loop-built
// thunk array is the evasion, not an edge case.
const FIXED_MARK = 'gov:fixed-verifiers'
const MAX_VERIFIERS = 5
const MAX_LENSES = 6
// Every array method that can carry an agent() call once per element. The list is closed and
// generous on purpose: a method missing from it used to mean ALLOW, which is the fail-open direction.
const ITER_CALL = /\.\s*(map|flatMap|forEach|filter|reduce|reduceRight|some|every|find|findIndex|sort|flat)\s*$/

// `K` resolved against this file: an integer literal, or an identifier bound to one.
function boundedK(tok, consts) {
  const t = String(tok).trim()
  if (/^\d+$/.test(t)) return Number(t) <= MAX_VERIFIERS
  if (/^[A-Za-z_$][\w$]*$/.test(t) && consts.has(t)) return consts.get(t) <= MAX_VERIFIERS
  return false
}

function fanoutFindings(script) {
  const lines = script.split(/\r?\n/)
  const code = lines.map((l) => stripStrings(l).split('//')[0])

  // integer consts bound in this file, e.g. `const MAX_VERIFIERS = 5` / `a.maxVerifiers || 5`
  const consts = new Map()
  code.forEach((l) => {
    let m = /\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(\d+)\s*$/.exec(l.trim())
    if (m) consts.set(m[1], Number(m[2]))
    m = /\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*[^=]*\|\|\s*(\d+)\s*$/.exec(l.trim())
    if (m && !consts.has(m[1])) consts.set(m[1], Number(m[2]))
  })

  // Receivers this file can prove are bounded. TWO PASSES, because a derived lens set is written
  // AFTER the literal it derives from (`const LENSES = ALL_LENSES.filter(…)`), and a single forward
  // pass would reject it on declaration order rather than on the property being checked.
  const ok = new Set()
  const scan = (raw, i) => {
    const l = code[i]
    const asg = /\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=/.exec(l)
    if (!asg) return
    const name = asg[1]
    if (raw.includes(FIXED_MARK)) {
      const c = /\bchunk\s*\(\s*[^,]+,\s*Math\.ceil\s*\(\s*[A-Za-z_$][\w$.]*\.length\s*\/\s*([^)]+)\)/.exec(l)
      const s = /\bsplitInto\s*\(\s*[^,]+,\s*([^),]+)\)/.exec(l)
      if ((c && boundedK(c[1], consts)) || (s && boundedK(s[1], consts))) {
        ok.add(name)
        return
      }
      // A marked DERIVATION from an array already known bounded — `ALL_LENSES.filter(…)`, a
      // `.slice()`, a ternary between two bounded sources. Neither filter nor slice can GROW an
      // array, so the bound is inherited. Only accepted WITH the marker, so it stays a deliberate
      // claim rather than something inferred from a name.
      //
      // The operations are a CLOSED list, and mentioning a bounded name is not enough: the first cut
      // accepted any line referencing one, which blessed `ALL_LENSES.concat(allFindings)` — a
      // derivation that grows without limit — on the strength of the word ALL_LENSES appearing.
      const rhs = l.slice(l.indexOf('=') + 1)
      const grows = /\b(concat|push|flat|flatMap|fill|repeat)\s*\(|\.\.\./.test(rhs)
      const shrinks = /\.\s*(filter|slice)\s*\(/.test(rhs) || /\?[^?]*:/.test(rhs)
      const refs = rhs.match(/[A-Za-z_$][\w$]*/g) || []
      if (!grows && shrinks && refs.some((r) => r !== name && ok.has(r))) ok.add(name)
      return
    }
    // an array literal whose element count is visible here. Counted on the FULL statement, which may
    // wrap: join forward until the brackets balance, so a multi-line LENSES array is measurable.
    if (!/=\s*\[/.test(l)) return
    let buf = l.slice(l.indexOf('['))
    let j = i
    let depth = 0
    let closed = false
    while (j < code.length) {
      for (const ch of j === i ? buf : code[j]) {
        if (ch === '[') depth++
        else if (ch === ']') { depth--; if (depth === 0) closed = true }
      }
      if (j > i) buf += '\n' + code[j]
      if (closed) break
      j++
    }
    if (!closed) return
    // The RHS must be the literal and NOTHING ELSE. `[].concat(allFindings)` starts with `[`, has an
    // empty inner, counted 0 elements and was blessed as bounded — an unbounded array wearing an
    // empty literal's clothes, and it needed no marker to do it.
    const tail = buf.slice(buf.lastIndexOf(']') + 1).replace(/[\s;]/g, '')
    if (tail !== '') return
    const inner = buf.slice(buf.indexOf('[') + 1, buf.lastIndexOf(']'))
    // A SPREAD makes the count invisible: `[...allFindings]` is one top-level element and any number
    // of agents.
    if (inner.includes('...')) return
    // top-level commas only
    let d = 0
    let n = inner.trim() ? 1 : 0
    for (const ch of inner) {
      if ('[{('.includes(ch)) d++
      else if (']})'.includes(ch)) d--
      else if (ch === ',' && d === 0) n++
    }
    if (n <= MAX_LENSES) ok.add(name)
  }
  lines.forEach(scan)
  lines.forEach(scan)
  // A BARE REASSIGNMENT invalidates the bound. `let items = [1, 2]` then `items = allFindings` was a
  // measured bypass: the whitelist was keyed on a name and nothing ever took the name back. The
  // protocol publishes "assigned exactly once", so anything assigned twice loses the claim.
  code.forEach((l) => {
    const m = /(?:^|[;{}]\s*)([A-Za-z_$][\w$]*)\s*=[^=]/.exec(l)
    if (m && !/\b(const|let|var)\s+$/.test(l.slice(0, m.index + m[0].indexOf(m[1])))) {
      if (!/\b(?:const|let|var)\s+[A-Za-z_$][\w$]*\s*=/.test(l)) ok.delete(m[1])
    }
  })

  const bad = []
  lines.forEach((raw, i) => {
    const l = code[i]
    if (!/\bagent\s*\(/.test(l)) return
    // NO MARKER ESCAPE ON THE agent() LINE. The first cut returned early here, so putting the marker
    // on the fan-out line itself blessed it with no shape check at all — the whole whitelist behind
    // one comment. Verified non-load-bearing before removal: all three shipped harnesses still pass
    // without it. The marker means something only on the ASSIGNMENT it annotates, where its shape IS
    // checked.
    // WHAT ENCLOSES THIS agent() CALL. Scanning the window right-to-left, a `)` is pending and a `(`
    // either matches a pending one or is an ENCLOSING opener — a call this agent() sits inside. Only
    // enclosing openers are judged, which is the difference between "the fan-out is a map" and "the
    // word map appears nearby". The synthesis stage of tier2-review.js is one agent() whose PROMPT
    // builds text with `allFindings.map(...)`; a window-wide regex read that as a fan-out and denied
    // a single-agent call — measured, and the reason this looks at structure and not at proximity.
    //
    // The walk stops at two enclosing openers — enough to hold `boundedParallel( x.map( … agent(` —
    // or 60 lines, so a pathological file cannot make this quadratic. A fixed 2-line window was the
    // first cut and was also a measured hole: a `.map((f) => () =>` whose agent() sits ten
    // prompt-lines below escaped it entirely, which is the commonest shape in these harnesses.
    const openersOf = (text) => {
      const out = []
      let pending = 0
      for (let k = text.length - 1; k >= 0; k--) {
        const ch = text[k]
        if (ch === ')') pending++
        else if (ch === '(') {
          if (pending > 0) pending--
          else out.push(k)
        }
      }
      return out
    }
    // The window is everything BEFORE the agent call, never the whole line: scanning right-to-left
    // from the end of `boundedParallel(all.map((f) => () => agent(f.c)), 5)` lets the trailing `)`s
    // cancel the very openers being looked for, and the one-line fan-out — the exact shape that
    // motivated this rule — reads as enclosed by nothing. Measured, twice.
    let win = l.slice(0, l.search(/\bagent\s*\(/))
    for (let k = i - 1; k >= 0 && k > i - 60 && openersOf(win).length < 2; k--) win = code[k] + '\n' + win

    // FAIL CLOSED. The first cut classified only three tidy spellings and fell through to ALLOW for
    // everything else, which meant a receiver it did not recognise was a receiver it blessed — five
    // independent bypasses, each one agent per finding, each reported clean. An iteration construct
    // this rule cannot PROVE bounded is denied; the burden is on the fan-out, not on the gate.
    let hit = null
    for (const pos of openersOf(win)) {
      const before = win.slice(0, pos)
      const m = ITER_CALL.exec(before)
      if (m) {
        // The receiver must be a BARE IDENTIFIER that this file shows to be bounded. A chain
        // (`x.filter(...).map`), a call result (`Object.values(b).map`) or a member expression is not
        // something this scan can size, and "cannot size" is a denial, not a pass.
        const recv = /([A-Za-z_$][\w$]*)\s*\.\s*[A-Za-z_$][\w$]*\s*$/.exec(before)
        const plain = recv && /(^|[^.\w$)\]])[A-Za-z_$][\w$]*\s*\.\s*[A-Za-z_$][\w$]*\s*$/.test(before)
        hit = { kind: 'iter', method: m[1], name: plain ? recv[1] : null, expr: before.slice(-60).trim() }
        break
      }
      if (/\bArray\s*\.\s*from\s*$/.test(before)) { hit = { kind: 'from' }; break }
      if (/\b(for|while)\s*$/.test(before)) { hit = { kind: 'loop' }; break }
    }
    if (hit && hit.kind === 'iter') {
      if (hit.name === null) {
        bad.push({ n: i + 1, line: raw, why: `agent() fanned through .${hit.method}() over an expression this file cannot size (\`${hit.expr}\`) — only a bare identifier proven bounded is accepted` })
      } else if (!ok.has(hit.name)) {
        bad.push({ n: i + 1, line: raw, why: `agent() fanned over \`${hit.name}\`, which this file does not show to be bounded` })
      }
      return
    }
    if (hit && hit.kind === 'from') {
      bad.push({ n: i + 1, line: raw, why: 'agent() fanned through Array.from() — the count is not visible here' })
      return
    }
    // A BRACELESS loop body: `for (const f of all) out.push(await agent(f))`. The brace walk below
    // cannot see it — there is no brace — and it was one of the measured bypasses.
    if (/\b(for|while)\s*\(/.test(l.slice(0, l.search(/\bagent\s*\(/)))) {
      bad.push({ n: i + 1, line: raw, why: 'agent() in a braceless loop body — a loop-built fan-out is the evasion this rule exists for' })
      return
    }
    // A loop BODY is a brace block, not a paren, so it never shows up as an enclosing opener. Judged
    // separately: an unclosed `for (`/`while (` block whose brace is still open above this line.
    let braces = 0
    for (let k = i; k >= 0 && k > i - 60; k--) {
      for (const ch of code[k]) {
        if (ch === '}') braces++
        else if (ch === '{') braces--
      }
      if (braces < 0 && /\b(for|while)\s*\(/.test(code[k])) {
        bad.push({ n: i + 1, line: raw, why: 'agent() inside a loop body — a loop-built thunk array is the evasion this rule exists for' })
        break
      }
      if (braces < 0) braces = 0 // a different block opened here; keep looking outward
    }
  })
  return bad
}

function main() {
  let data
  try {
    data = JSON.parse(readStdin())
  } catch {
    process.exit(0)
  }
  if (!data || data.tool_name !== 'Workflow') process.exit(0)

  // A saved script is a FILE, and a node hook has fs — exiting 0 here made the rules unenforceable
  // the moment anyone wrote the offending script to disk. A `name:`-only run supplies no source and
  // stays unscannable; that hole is covered by the merge-bar leg over tools/workflows/, and is
  // declared in memory/guides/REVIEW-PROTOCOL.md rather than implied away.
  let script = (data.tool_input && data.tool_input.script) || ''
  const spath = (data.tool_input && data.tool_input.scriptPath) || ''
  if (!script && spath) {
    try {
      script = require('fs').readFileSync(spath, 'utf8')
    } catch (e) {
      process.stderr.write(
        `BLOCKED by agent-cap: scriptPath ${spath} could not be read (${e.code || e.message}), so ` +
          `the fan-out rules could not be checked. A script this hook cannot read is not a script ` +
          `this hook may approve.\n`,
      )
      process.exit(2)
    }
  }
  if (!script) process.exit(0) // a `name:` run: no source reaches this hook (see the protocol)

  const fan = fanoutFindings(script)
  if (fan.length) {
    process.stderr.write(
      `BLOCKED by agent-cap: a verify/fan-out stage spawns one agent per item. The review protocol ` +
        `caps verify-stage agents at ${MAX_VERIFIERS} TOTAL — the batch size grows with the finding ` +
        `count, the agent count never does (memory/guides/REVIEW-PROTOCOL.md).\n\n` +
        fan.slice(0, 6).map(({ n, line, why }) => `  L${n}: ${line.trim()}\n        ${why}`).join('\n') +
        `\n\nSplit into a BOUNDED number of groups and mark the assignment:\n` +
        `  const MAX_VERIFIERS = ${MAX_VERIFIERS}\n` +
        `  const batches = chunk(items, Math.ceil(items.length / MAX_VERIFIERS)) // ${FIXED_MARK}\n` +
        `  await boundedParallel(batches.map((g) => () => agent(promptFor(g))), ${CAP})\n\n` +
        `A fixed lens array (<= ${MAX_LENSES} elements) is allowed as-is — its agent count is a ` +
        `constant. Ready-made: tools/workflows/tier2-review.js.\n`,
    )
    process.exit(2)
  }

  const bad = offendingLines(script)
  if (bad.length === 0) process.exit(0)

  const shown = bad
    .slice(0, 6)
    .map(({ n, line }) => `  L${n}: ${line.trim()}`)
    .join('\n')
  process.stderr.write(
    `BLOCKED by agent-cap: raw parallel()/pipeline() fans out to the harness ` +
      `cap (~14 agents) and trips the server rate limiter.\n\n` +
      `Route ALL fan-out through the cap-${CAP} helpers and call them instead:\n` +
      `  async function boundedParallel(thunks, cap = ${CAP}) {\n` +
      `    const out = []\n` +
      `    for (let i = 0; i < thunks.length; i += cap)\n` +
      `      out.push(...await parallel(thunks.slice(i, i + cap))) // gov:bounded-fanout\n` +
      `    return out\n` +
      `  }\n` +
      `  async function boundedPipeline(items, cap, ...stages) {\n` +
      `    const out = []\n` +
      `    for (let i = 0; i < items.length; i += cap)\n` +
      `      out.push(...await pipeline(items.slice(i, i + cap), ...stages)) // gov:bounded-fanout\n` +
      `    return out\n` +
      `  }\n\n` +
      `Consolidate before fanning: batch skeptics/items so total agents stay low.\n` +
      `Offending line(s):\n` +
      shown +
      `\n`,
  )
  process.exit(2)
}

main()
