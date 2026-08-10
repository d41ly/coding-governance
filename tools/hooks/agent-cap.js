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
 * CAP: 5, a FILE CONSTANT and not overridable. This guard RESOLVES the number
 * wherever a bound is written — the helper CALL SITE, the helper's own DEFAULT
 * PARAMETER, and the width a `gov:bounded-fanout` line claims — and denies one
 * it cannot resolve at or under the cap. Setting AGENT_CAP is REFUSED with a
 * message rather than ignored: a knob that used to appear to work is how the
 * override claim this version deletes survived two releases.
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

const KIT_AGENT_CAP_VERSION = '1.2' // gov:kit agent-cap@1.2 — engine identity (this file is deployed verbatim; the constant is the deployer's version marker)
// A BARE LITERAL, never an environment read. An env-settable ceiling is the defeatable class this
// guard exists to remove, and it leaves no diff behind when someone raises it.
const CAP = 5

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

// THE ONE BINDER, for every consumer of boundedK: the marker's K, the helper call site's cap
// argument and the helper's default parameter.
//
// An `<expr> || <int>` right-hand side does NOT bind. It reads as a bound and is not one: the
// literal is a FALLBACK, and `(args && args.cap) || 5` is a caller-settable knob wearing a
// constant's clothes — which is exactly how two shipped harnesses raised their own verifier count
// past the cap while this hook read the 5 and every gate stayed green. The form is left legal
// JavaScript and stays usable for constants nothing here resolves; only its use as a RESOLVED BOUND
// is refused, and it is recorded separately so the deny can name the form rather than shrug.
function intConsts(code) {
  const consts = new Map()
  const orBound = new Map()
  code.forEach((l) => {
    const m = /\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(\d+)\s*$/.exec(l.trim())
    if (m) { consts.set(m[1], Number(m[2])); return }
    const o = /\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*[^=]*\|\|\s*(\d+)\s*$/.exec(l.trim())
    if (o && !orBound.has(o[1])) orBound.set(o[1], Number(o[2]))
  })
  // A BARE REASSIGNMENT invalidates the binding, for the same reason it invalidates a bounded
  // receiver below: `let K = 5` followed by `K = 500` published a 5 this file could read and ran a
  // 500. The sweep existed for the receiver whitelist and was never mirrored onto the number.
  code.forEach((l) => {
    const m = /(?:^|[;{}]\s*)([A-Za-z_$][\w$]*)\s*=[^=]/.exec(l)
    if (m && !/\b(const|let|var)\s+$/.test(l.slice(0, m.index + m[0].indexOf(m[1])))) {
      if (!/\b(?:const|let|var)\s+[A-Za-z_$][\w$]*\s*=/.test(l)) {
        consts.delete(m[1])
        orBound.delete(m[1])
      }
    }
  })
  return { consts, orBound }
}

function fanoutFindings(script) {
  const lines = script.split(/\r?\n/)
  const code = lines.map((l) => stripStrings(l).split('//')[0])

  // integer consts bound in this file, e.g. `const MAX_VERIFIERS = 5`
  const { consts } = intConsts(code)

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

// ---------------------------------------------------------------------------
// RULE 3 — the hook READS THE BOUND IT ENFORCES.
//
// Rules 1 and 2 above police the SHAPE of a fan-out: route it through the helper, and give the
// verify stage a bounded group count. Neither ever read the number. `CAP` reached the remediation
// text and decided nothing, so a shipped harness raised its own verifier count from the caller —
// `const CAP = (args && args.cap) || 5` — and every gate stayed green over a rule the charter calls
// BINDING. A cap enforced by convention is not enforced.
//
// THREE places a bound is written, and all three are resolved here:
//   S1  the CALL SITE          boundedParallel(thunks, K) / boundedPipeline(items, K, ...stages)
//   S2  the DEFAULT PARAMETER  async function boundedParallel(thunks, cap = K)
//   S4  the MARKER's width     out.push(...await parallel(thunks.slice(i, i + cap))) // gov:bounded-fanout
//
// S4 is the asymmetry the audit named as the clearest lesson in this file: `gov:fixed-verifiers` is
// a claim whose SHAPE is checked, while `gov:bounded-fanout` returned early and exempted a line
// slicing fifty wide. Both markers are claims now.
//
// FAIL CLOSED, like every other branch here: a K this file cannot resolve to an integer at or under
// MAX_VERIFIERS is a denial. The burden is on the fan-out.
const HELPERS = /(?<![.\w$])(boundedParallel|boundedPipeline)\s*\(/g

// A literal-blanked view: string AND TEMPLATE contents gone, comments gone, delimiters and structure
// kept. The per-line strip the two rules above run on cannot see a template literal spanning lines,
// and a `(` inside a prompt string unbalances a forward paren join — which is the one mechanism this
// rule is built on. Deliberately a SECOND view rather than a replacement: the existing strip carries
// three dozen measured arms and is not worth re-baselining for a rule that can afford its own pass.
function blankLiterals(script) {
  const out = []
  let mode = 'code' // code | tmpl | block
  for (const raw of script.split(/\r?\n/)) {
    let res = ''
    let i = 0
    while (i < raw.length) {
      const ch = raw[i]
      const two = raw.slice(i, i + 2)
      if (mode === 'code') {
        if (two === '//') break
        if (two === '/*') { mode = 'block'; i += 2; continue }
        if (ch === '`') { mode = 'tmpl'; res += '`'; i++; continue }
        if (ch === "'" || ch === '"') {
          res += ch
          const q = ch
          i++
          while (i < raw.length && raw[i] !== q) i += raw[i] === '\\' ? 2 : 1
          res += q
          i++
          continue
        }
        res += ch
        i++
      } else if (mode === 'tmpl') {
        if (ch === '\\') { i += 2; continue }
        if (ch === '`') { mode = 'code'; res += '`'; i++; continue }
        i++
      } else {
        if (two === '*/') { mode = 'code'; i += 2; continue }
        i++
      }
    }
    out.push(res)
  }
  return out
}

// Join forward from the `(` at code[i][col] until the parens BALANCE, and return the inside. The
// precedent is the bracket walk in the array-literal case above, which already joins lines until a
// literal closes; every shipped call site spans lines, so a per-line read of argument 2 sees nothing
// at all. Bounded by the balance point (and 200 lines), so the scan stays linear.
function joinCall(code, i, col) {
  let depth = 0
  let buf = ''
  for (let j = i; j < code.length && j < i + 200; j++) {
    for (const ch of j === i ? code[j].slice(col) : code[j]) {
      buf += ch
      if (ch === '(') depth++
      else if (ch === ')' && --depth === 0) return { text: buf.slice(1, -1), end: j }
    }
    buf += '\n'
  }
  return null
}

// Split on TOP-LEVEL commas only: `boundedParallel(all.map((f) => () => agent(f)), 5)` is two
// arguments, not four.
function topLevelArgs(text) {
  if (!text.trim()) return []
  const out = []
  let d = 0
  let cur = ''
  for (const ch of text) {
    if ('([{'.includes(ch)) d++
    else if (')]}'.includes(ch)) d--
    else if (ch === ',' && d === 0) { out.push(cur); cur = ''; continue }
    cur += ch
  }
  out.push(cur)
  // A TRAILING COMMA is not an argument. `boundedParallel(\n  LENSES.map(…),\n)` — the prettier-
  // formatted shape both shipped harnesses use — split into two, and the phantom second one read as
  // a cap argument of `(nothing)`: the predicate denied tier2-review.js, the repo's own review
  // harness, on its formatting. Measured against the real tree before this rule was trusted.
  while (out.length && !out[out.length - 1].trim()) out.pop()
  return out
}

function capFindings(script) {
  const lines = script.split(/\r?\n/)
  const code = blankLiterals(script)
  const { consts, orBound } = intConsts(code)
  const bad = []

  // ONE explanation per unresolvable K, naming the FORM rather than shrugging — an operator who
  // cannot tell which of three spellings the hook refused fixes it by guessing.
  const why = (tok, where) => {
    const t = String(tok).trim()
    if (orBound.has(t))
      return `${where} resolves \`${t}\`, bound by an \`<expr> || ${orBound.get(t)}\` FALLBACK form — a caller-settable knob is not a bound, so it no longer resolves`
    if (/^\d+$/.test(t))
      return `${where} is ${t}, above the ${MAX_VERIFIERS}-agent cap`
    if (/^[A-Za-z_$][\w$]*$/.test(t) && consts.has(t))
      return `${where} resolves \`${t}\` to ${consts.get(t)}, above the ${MAX_VERIFIERS}-agent cap`
    return `${where} is \`${t || '(nothing)'}\`, which this file cannot resolve to an integer at or under ${MAX_VERIFIERS}`
  }

  // --- S2: the helper DEFINITIONS, and the default each one carries ---------------------------
  // Keyed by helper name, because a bare `boundedParallel(thunks)` is governed by the default of
  // the helper it names.
  const defaults = new Map()
  const paramsOf = new Map()
  code.forEach((l, i) => {
    const d = /\bfunction\s+(boundedParallel|boundedPipeline)\s*\(/.exec(l)
    if (!d) return
    const j = joinCall(code, i, d.index + d[0].length - 1)
    if (!j) return
    const args = topLevelArgs(j.text)
    paramsOf.set(d[1], args.map((p) => (p.split('=')[0] || '').trim()).filter(Boolean))
    const second = args[1]
    if (second === undefined) { defaults.set(d[1], { tok: null, n: i + 1 }); return }
    const eq = second.indexOf('=')
    if (eq < 0) { defaults.set(d[1], { tok: null, n: i + 1 }); return }
    const tok = second.slice(eq + 1)
    defaults.set(d[1], { tok, n: i + 1 })
    if (!boundedK(tok, consts))
      bad.push({ n: i + 1, line: lines[i], why: why(tok, `the DEFAULT PARAMETER of ${d[1]}()`) })
  })

  // --- S1: every CALL SITE ---------------------------------------------------------------------
  code.forEach((l, i) => {
    HELPERS.lastIndex = 0
    let m
    while ((m = HELPERS.exec(l))) {
      if (/\bfunction\s+$/.test(l.slice(0, m.index))) continue // a definition — S2 judged it
      const name = m[1]
      const j = joinCall(code, i, m.index + m[0].length - 1)
      if (!j) {
        bad.push({ n: i + 1, line: lines[i], why: `the ${name}() CALL SITE never closes its parens within 200 lines, so the cap argument cannot be read — a call this hook cannot parse is not a call it may approve` })
        continue
      }
      const args = topLevelArgs(j.text)
      if (args.length >= 2) {
        if (!boundedK(args[1], consts))
          bad.push({ n: i + 1, line: lines[i], why: why(args[1], `the cap argument at the ${name}() CALL SITE`) })
        continue
      }
      // No cap argument: the helper's own DEFAULT governs. An undefined helper, or one whose second
      // parameter carries no default, leaves nothing to resolve — and nothing to resolve is a deny.
      const def = defaults.get(name)
      if (!def)
        bad.push({ n: i + 1, line: lines[i], why: `the ${name}() CALL SITE passes no cap and this file defines no ${name}(), so there is no DEFAULT PARAMETER to resolve the bound from` })
      else if (def.tok === null)
        bad.push({ n: i + 1, line: lines[i], why: `the ${name}() CALL SITE passes no cap and ${name}() (L${def.n}) declares no default for its second parameter, so nothing bounds this fan-out` })
      // A resolvable-but-wide default already denied at its definition; not reported twice.
    }
  })

  // --- S4: the `gov:bounded-fanout` marker is a CLAIM about a width ----------------------------
  lines.forEach((raw, i) => {
    if (!raw.includes('gov:bounded-fanout')) return
    const l = code[i]
    const s = /(?:^|[^.\w$)\]])([A-Za-z_$][\w$]*)\s*\.\s*slice\s*\(\s*[^,]*,\s*([^)]*)\)/.exec(l)
    if (!s) {
      bad.push({ n: i + 1, line: raw, why: 'the gov:bounded-fanout MARKED LINE does not slice a bare identifier by a visible width — the marker claims a bound and there is no bound here to check' })
      return
    }
    const width = s[2].replace(/^[^+]*\+\s*/, '').trim()
    // The enclosing helper's own `cap` PARAMETER is admitted explicitly: S2 has bounded its default
    // and S1 has bounded every call site, so the parameter is bounded wherever it comes from. This
    // is the token the three shipped harnesses use, and without this case S4 denies all of them.
    const holder = (() => {
      for (let k = i; k >= 0 && k > i - 40; k--) {
        const d = /\bfunction\s+([A-Za-z_$][\w$]*)\s*\(/.exec(code[k])
        if (d) return d[1]
      }
      return null
    })()
    if (holder && paramsOf.has(holder) && paramsOf.get(holder).includes(width)) return
    if (!boundedK(width, consts))
      bad.push({ n: i + 1, line: raw, why: why(width, 'the gov:bounded-fanout MARKED LINE slice width') })
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

  // AGENT_CAP used to raise the ceiling and no longer can. REFUSED rather than ignored: this hook's
  // own header advertised the override for two releases after it stopped deciding anything, and a
  // silently-ignored knob that appears to work is exactly how that claim survived. An operator who
  // sets it gets told, in the one place they will look.
  if (process.env.AGENT_CAP !== undefined && process.env.AGENT_CAP !== '') {
    process.stderr.write(
      `BLOCKED by agent-cap: AGENT_CAP is set (${process.env.AGENT_CAP}) and this guard NO LONGER ` +
        `reads it. The cap is the file constant ${MAX_VERIFIERS}, resolved at the call site, the ` +
        `default parameter and the gov:bounded-fanout width. An environment override would be a ` +
        `ceiling raise that leaves no diff behind. Unset AGENT_CAP and re-run; to change the number, ` +
        `change it in tools/hooks/agent-cap.js and in memory/guides/REVIEW-PROTOCOL.md, where the ` +
        `rule is stated.\n`,
    )
    process.exit(2)
  }

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

  // RULE 3 runs AFTER the arity rule on purpose. A one-argument `boundedParallel(all.map(…))` breaks
  // both, and the arity message is the one that names the defect an operator has to fix; reversing
  // the order would retitle the rule-2 corpus without changing a verdict.
  const caps = capFindings(script)
  if (caps.length) {
    process.stderr.write(
      `BLOCKED by agent-cap: a bound is written here that this file cannot resolve at or under ` +
        `${MAX_VERIFIERS}. The cap is enforced by reading the number, not by trusting the helper's ` +
        `name (memory/guides/REVIEW-PROTOCOL.md).\n\n` +
        caps.slice(0, 6).map(({ n, line, why }) => `  L${n}: ${String(line).trim()}\n        ${why}`).join('\n') +
        `\n\nWrite the bound as an integer literal at or under ${MAX_VERIFIERS}, or as an identifier ` +
        `bound DIRECTLY to one and never reassigned:\n` +
        `  const MAX_VERIFIERS = ${MAX_VERIFIERS}\n` +
        `  await boundedParallel(batches.map((g) => () => agent(promptFor(g))), MAX_VERIFIERS)\n`,
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
