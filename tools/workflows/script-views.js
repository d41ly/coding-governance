#!/usr/bin/env node
/**
 * script-views.js — the review kit's ONE scanner of a harness script (TOOL-dBoundRoles-25 S4, §4 "Disposition").
 * The views, `runBothViews`, the verify total, the writer bound and the harness name the review kit's two
 * merge-bar gates read: `check-verifier-fanout.js` (rule 2, the verify-stage total and the loop markers) and
 * `check-review-join.js` (rule 5, the ref-keyed join ban), each requiring this module from beside itself.
 * They sat in the hooks kit's agent limit hook until TOOL-dBoundRoles-25 retired it; only these two gates
 * read them, so they live in this kit. ONE copy: a view reads the mode `runBothViews` switches, so the
 * views and it stay one module, and a copy in each gate would be two scanners of one script, the drift
 * TOOL-dFairHearing-16 §4 rejected. Requiring it runs nothing.
 *
 * WHAT A QUOTE IS, since the views exported to rules 2 and 5 turn on it. A quote opens a string literal
 * only where one may legally BEGIN (`checkLiteralOpen`): glued to the character
 * that ends an expression it is TEXT — the apostrophe in `don't` — and so it is
 * after a bare word that is not a JS keyword. A quote that opens nothing is left
 * as text and its line is still blanked, EXCEPT inside a same-line template span,
 * which is emitted whole: a quoted `'http://x'` written in one therefore survives
 * into the line-comment strip. That channel is not closed by wording, it is
 * bounded by the no-regression property below — every rule is evaluated over the
 * SHIPPED views as well, and a denial from either stands, so nothing this hook
 * denied before the quote rule changed can be admitted after it.
 */
'use strict'

// TOOL-dMispairedQuote-1 — the ONE decision this file makes about what OPENS a string literal.
// All three views below ask it; none of them walks a line looking for a partner itself.
//
// A quote opens a literal only where one may legally BEGIN. In valid JavaScript a string's opening
// quote is never GLUED to the character that ends an expression, and never follows a bare word that
// is not a keyword — so `don't`, `won't`, `it's`, `y'all` and `run 'em` are TEXT, while `return 'x'`,
// `case 'y':` and `throw 'z'` are ordinary openers. `LITERAL_OPENERS` is that keyword set, and it
// omits `in`, `of` and `do`: those are ordinary English connectives, and admitting them let a
// comment reading "one of 'em" open a span that swallowed a fan-out.
//
// WHY THIS AND NOT A REGEX-LITERAL MODEL, since the reported instance was `/won't/` sharing its line
// with a fan-out and the obvious repair is to model `/…/`. That closes ONE spelling. Measured against
// the pre-fix hook, four more admit the same raw `parallel(` and none of them is a regex: a
// double-quoted `"don't"`, a block comment, a backticked `don't`, and loose prose. The APOSTROPHE is
// the mechanism; the construct around it is not, and a fix keyed on the construct gates the instance.
// Four of this file's five rules were defeated, rule 5's join ban included.
//
// WHAT THE PAIR TEST COULD NOT REACH. `addc6169` already required a matching PAIR before blanking,
// which fixed an unpaired quote swallowing the rest of its line. A pair exists for
// `/won't/ … agent('a'` too — the prose apostrophe and the quote opening the call — and blanking
// between them erased the very call the rules count. Asking what a quote OPENS is the question a
// partner test cannot ask, and it is why that repair looked like it closed the class and did not.
//
// THREE RESIDUALS, stated rather than closed, each with a fixture in the suite and a backlog row:
//   (a) a BALANCED set of loose prose quotes straddling a fan-out — every quote finds a partner and
//       none is left over, so nothing is left to notice;
//   (b) prose whose last word before the apostrophe is one of the keywords below;
//   (c) prose that puts the apostrophe after an OPERATOR — `/* rock - 'n roll */` — which is a legal
//       opener position in code and which this predicate cannot tell from prose.
// None of the three is a regression: all admit at the pre-fix revision too. What bounds them is the
// dual evaluation in `runBothViews` — a denial from the shipped views still stands.
const LITERAL_OPENERS = new Set([
  'return', 'case', 'throw', 'typeof', 'instanceof', 'new', 'delete', 'void', 'yield', 'await', 'else',
])

function checkLiteralOpen(line, i) {
  let p = i - 1
  while (p >= 0 && (line[p] === ' ' || line[p] === '\t')) p--
  if (p < 0) return true
  if (!/[A-Za-z0-9_$)\]\\]/.test(line[p])) return true
  // Walk the IDENTIFIER backwards. This read `/([A-Za-z_$][\w$]*)$/.exec(line.slice(0, p + 1))`,
  // which copies the whole line prefix and rescans it FOR EVERY QUOTE — quadratic in line length,
  // and every ordinary `return 'x'` pays it. Measured by the closing review on one long line:
  // 253 KB took 33.8 s against 62 ms before this build, ~4x per doubling, so about half a megabyte
  // clears the 60 s hook timeout. **A PreToolUse hook that times out is NON-BLOCKING**, so the cost
  // was not slowness, it was a fan-out walking straight past the guard. The same measurement after
  // this rewrite: 87 ms. The walk is bounded by the identifier, never by the line.
  let s = p
  while (s >= 0 && /[A-Za-z0-9_$]/.test(line[s])) s--
  if (s === p) return false
  return LITERAL_OPENERS.has(line.slice(s + 1, p + 1))
}

function resolveLiteralEnd(line, i) {
  if (!checkLiteralOpen(line, i)) return -1
  const q = line[i]
  let e = i + 1
  while (e < line.length && line[e] !== q) e += line[e] === '\\' ? 2 : 1
  return e < line.length ? e : -1
}

// Blank the CONTENTS of single/double-quoted string literals so a `parallel(`
// mentioned in prose (a meta.description, a log message) isn't read as a call.
// ONE ORDERED PASS, not two `replace()` sweeps: the single-quote sweep used to run first and pair
// the apostrophe inside a DOUBLE-quoted `"don't"` with the quote opening `agent('a'`, blanking the
// `parallel(` between them. A single pass consumes `"don't"` whole and never sees its apostrophe.
// A same-line template span is skipped WHOLE — its prose contributes no opener — but its text is
// KEPT, so a primitive named inside a lens prompt still denies exactly as it did before
// (`TOOL-aLexedStripper-3` owns that false positive and this build does not touch it). The cost is
// that a quoted `'http://x'` inside such a span survives into the line-comment strip below, which
// the dual evaluation bounds rather than this function.
// Run BEFORE the line-comment strip so a `//` inside a string can't truncate it.
function renderStrippedLine(line) {
  let out = ''
  let i = 0
  while (i < line.length) {
    const ch = line[i]
    if (ch === '`') {
      let e = i + 1
      while (e < line.length && line[e] !== '`') e += line[e] === '\\' ? 2 : 1
      if (e < line.length) { out += line.slice(i, e + 1); i = e + 1; continue }
      out += ch; i++; continue
    }
    if (ch === "'" || ch === '"') {
      const e = resolveLiteralEnd(line, i)
      if (e >= 0) { out += ch + ch; i = e + 1; continue }
      out += ch; i++; continue
    }
    out += ch
    i++
  }
  return out
}

// ---------------------------------------------------------------------------
// TOOL-dMispairedQuote-3 — the NO-REGRESSION guarantee.
//
// The three views below are the SHIPPED ones, kept VERBATIM. They are not dead code and they are
// not a second answer to the question the new views answer: every rule is evaluated over BOTH,
// and a denial from EITHER stands. That makes the change monotone in the DENY direction by
// construction, so no script this hook denies today can be admitted after it.
//
// WHY A PROPERTY AND NOT THREE FIXTURES. Correcting what counts as a string literal does not only
// un-hide fan-outs; it un-hides every OTHER character the old mispairing was blanking, and this
// file's rules 2 and 3 walk brackets and balance parens ACROSS lines. Three separate DENY-to-ADMIT
// moves were reproduced against the improved views alone: a backtick inside a regex literal
// reaching the template-mode switch, a regex-borne `)` closing a multi-line call site early so a
// declared cap of 50 fell through to the helper default, and a `//` inside a quoted span inside a
// template truncating rule 1's line. Each has its own fixture below, and each was ALSO closed by
// this one property — which is what makes the property worth its bytes: the next repair to these
// views inherits it without knowing these three shapes.
// ---------------------------------------------------------------------------
function renderShippedLine(line) {
  return line.replace(/'(?:\\.|[^'\\])*'/g, "''").replace(/"(?:\\.|[^"\\])*"/g, '""')
}

// TOOL-aRepatriatedFork-7 S2 — THIS VIEW KEEPS THE NESTED-INTERPOLATION DEFECT, on purpose. Its one
// `interpDepth` is zeroed by a nested `${` and never restored, which `renderLexedView` now fixes. The
// frozen body is the no-regression BASELINE (the S10 byte arm compares it to `d65da7ab`), and a
// corrupted view can only LOSE code, so its failure is a false negative: `runBothViews` denies when
// EITHER view denies, and the corrected lexed view decides every case this one misses. Editing it
// would move the baseline the S9 property measures against for no verdict the union lacks.
function renderShippedView(script) {
  const out = []
  let mode = 'code' // code | tmpl
  const stack = [] // 'tmpl' | 'interp', innermost last
  let interpDepth = 0 // brace depth inside the current interpolation
  for (const raw of script.split(/\r?\n/)) {
    let res = ''
    let i = 0
    while (i < raw.length) {
      const ch = raw[i]
      const two = raw.slice(i, i + 2)
      if (mode === 'code') {
        if (two === '//') break
        if (ch === '`') { stack.push('tmpl'); mode = 'tmpl'; res += '`'; i++; continue }
        if (ch === "'" || ch === '"') {
          // An UNPAIRED quote is ordinary text, not a string. This used to run to end of line
          // and then append a closer the source never had, swallowing the rest of that line --
          // and any fan-out sitting on it went too, ADMITTING a script the shipped hook DENIES.
          // The measured case is an apostrophe inside a regex literal, /won't/. `stripStrings`
          // needs a matching PAIR before it blanks anything, and so does this now.
          const q = ch
          let e = i + 1
          while (e < raw.length && raw[e] !== q) e += raw[e] === '\\' ? 2 : 1
          if (e >= raw.length) { res += ch; i++; continue }
          res += q + q
          i = e + 1
          continue
        }
        // Inside an interpolation, the matching `}` returns to the template it came from. Depth is
        // counted so an object literal or a block inside the expression does not close it early.
        if (stack.length && stack[stack.length - 1] === 'interp') {
          if (ch === '{') interpDepth++
          else if (ch === '}') {
            if (interpDepth === 0) { stack.pop(); mode = 'tmpl'; res += ' '; i++; continue }
            interpDepth--
          }
        }
        res += ch
        i++
      } else if (mode === 'tmpl') {
        if (ch === '\\') { i += 2; continue }
        if (two === '${') { stack.push('interp'); interpDepth = 0; mode = 'code'; res += '  '; i += 2; continue }
        if (ch === '`') { stack.pop(); mode = 'code'; res += '`'; i++; continue }
        i++
      }
    }
    out.push(res)
  }
  // THIS VIEW DOES NOT BLANK BLOCK COMMENTS, and that is the fix rather than an omission. It cannot
  // tell a real block-comment opener from one inside a regex literal, so every blanking it did on
  // hide a fan-out: a regex-borne opener closed by a later ordinary closer ends the scan back in
  // code mode with an empty stack, no flag fires, and the span between is gone from the view. Two
  // closing-review rounds measured that, and the second one measured the smaller repair -- widening
  // the flag -- as insufficient for exactly this shape. The view this replaced blanked no block
  // comment either, so leaving them alone cannot regress against it, and un-blanked comment text can
  // only ADD apparent code, never hide it. That is the same fail-closed posture rule 1 already
  // documents for a primitive named inside a block comment.
  //
  // The flag still reports every mode that outlives the scan, which now means an unterminated
  // TEMPLATE only.
  return { code: out, unterminated: stack.length > 0 || mode !== 'code' }
}

function renderShippedBlanks(script) {
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

// ---------------------------------------------------------------------------
// TOOL-dMispairedQuote-3 — the NO-REGRESSION guarantee, as a DISPATCHER.
//
// Every rule below reads its view through one of these three names and none of them knows there are
// two implementations. `main()` runs the whole rule set, and if nothing denied, sets the mode to
// `shipped` and runs it again: a denial from EITHER pass stands, so no script this hook denies today
// can be admitted after the change.
//
// WHY A DISPATCHER AND NOT A PARAMETER. The first cut threaded a `shipped` flag through each rule
// function, which needs a CENSUS of which rule reads which view — and that census was wrong for two
// of the four: `fanoutFindings` reads the lexed view AND the per-line one on its fallback branch, and
// `scanJoinFindings` reads the blanked view AND the per-line one. A census that has to be right is a
// census that can be wrong, and getting it wrong silently drops half the guarantee. Here every read
// goes through a dispatcher by construction and no rule function changes at all.
//
// A MODULE-LEVEL MODE is safe here and nowhere near a general licence: this file is a one-shot CLI
// that reads stdin, decides, and exits. There is no concurrency, no second script in flight, and
// `main()` is the only writer.
let VIEW_MODE = 'lexed' // 'lexed' | 'shipped'

function renderStrippedView(line) {
  return VIEW_MODE === 'shipped' ? renderShippedLine(line) : renderStrippedLine(line)
}

function renderCodeView(script) {
  return VIEW_MODE === 'shipped' ? renderShippedView(script) : renderLexedView(script)
}

function renderBlankedLiterals(script) {
  // TOOL-aWeldedTribunal-3 — both arms return `{ code, unterminated }`, and the SHIPPED arm is
  // hard-coded `false` rather than reporting. That is not an oversight and not a shortcut.
  //
  // The three `renderShipped*` bodies are FROZEN: a self-test arm byte-compares them against BASE,
  // because they ARE the no-regression baseline that makes `runBothViews`'s union sound. Editing one
  // to add a report would break exactly the guarantee this whole dispatcher exists to provide — the
  // suite caught the first attempt at it, which is the arm working as designed.
  //
  // Nothing is lost. `runBothViews` UNIONS the two passes, so the corrected view's fallback ADDS the
  // findings the frozen view cannot see, and the frozen view keeps behaving exactly as it always
  // has. The improvement belongs to the corrected view; the baseline stays a baseline.
  return VIEW_MODE === 'shipped'
    ? { code: renderShippedBlanks(script), unterminated: false }
    : renderBlankedView(script)
}

// Run one rule over BOTH views and merge. The mode is restored before returning, so a rule that
// throws cannot leave the next one reading the wrong view. Findings merge on `n`, the 1-based line
// number every rule's finding shape carries — and on the `why` beside it where one exists, because
// a rule can push more than one finding for a single line and keying on `n` alone would drop the
// second.
function runBothViews(rule, script) {
  // BOTH passes are isolated, and neither may turn a crash into an admission. `main()` has no
  // top-level catch and a PreToolUse hook that exits 1 is NON-BLOCKING, so an unguarded lexed pass
  // handed a crashing script straight through — reproduced by the closing review with a
  // 9000-deep nested ternary that the pre-fix hook DENIES at exit 2. A throw in the corrected views
  // must fall through to the shipped ones, which is what this file did before this build.
  let lexed = []
  let lexedThrew = false
  try {
    lexed = rule(script)
  } catch (e) {
    lexedThrew = true
  }
  VIEW_MODE = 'shipped'
  let shipped = []
  let shippedThrew = false
  try {
    shipped = rule(script)
  } catch (e) {
    shippedThrew = true
  } finally {
    VIEW_MODE = 'lexed'
  }
  // BOTH threw: this file cannot read the script at all, and FAIL CLOSED is its stated posture
  // everywhere else. The pre-fix hook exited 1 here and admitted; denying is stricter than BASE and
  // is the one place this build deliberately is.
  if (lexedThrew && shippedThrew)
    return [{ n: 1, line: String(script).split(/\r?\n/)[0] || '', why: 'this file could not scan the script under EITHER view — a script it cannot read is not a script it may approve' }]
  const key = (f) => f.n + '\u0000' + (f.why === undefined ? '' : f.why)
  const seen = new Set(lexed.map(key))
  return lexed.concat(shipped.filter((f) => !seen.has(key(f))))
}

// THE VERIFY TOTAL. No rule of the spawn guard reads it: rule 2, the verify-stage total, is the review kit's
// `check-verifier-fanout.js`, which reads it from this module, and `check-playbook-parity.sh` reads it by source
// line. Its home since TOOL-dBoundRoles-25 retired the hook it sat in. The lens allowance that sat beside it left
// with its last reader (TOOL-dFairHearing-27 S16): its one home is `LENS_SLOTS` in `check-verifier-fanout.js`.
const MAX_VERIFIERS = 5

// TOOL-dGroundRules-10 F2 — a VERIFIER split's comparand is MAX_VERIFIERS, the verify total. TOOL-dGroundRules-18 — a WRITER
// split's is the agent limit (receiver (a)), read through the policy kit's `readPolicy` once, only for a script carrying the
// marker. TOOL-dBoundRoles-25 §8 F8: `helper` is the policy helper's path, which the fan-out gate takes from the hooks kit's
// `resolvePolicyHelper`, the `scratch-guard.js` its `--hook` names; '' or a path naming no file reads as no policy kit.
function readWriterBound(repo, helper) {
  if (!helper || !require('fs').existsSync(helper)) return { n: MAX_VERIFIERS, key: 'MAX_VERIFIERS, as no policy kit was found by resolveKitDir' }
  let v
  try { v = require(helper).readPolicy('runtime.agents-in-flight', { repo }).value } catch (e) { return { why: `the agent limit could not be read: ${(e && e.message) || e}` } }
  return Number.isInteger(v) && v > 0 ? { n: v, key: 'runtime.agents-in-flight' } : { why: `runtime.agents-in-flight reads ${JSON.stringify(v)}, not a positive integer` }
}

// The review harness a deny message points at, DERIVED (TOOL-aRepatriatedFork-2 S6): `tier2-review.js`, which this
// kit renders beside this module (`{kit}/tier2-review.js`), relative to the project root, so an adopter's reader is
// sent to the file the install holds and never to a path spelled at gov's prefix.
function resolveHarnessName() {
  const path = require('path')
  return path.relative(process.env.CLAUDE_PROJECT_DIR || process.cwd(), path.join(__dirname, 'tier2-review.js')).split(path.sep).join('/')
}

// TOOL-aLexedStripper-2 — the view RULE 2 reads, and the reason it is not `renderBlankedLiterals`.
//
// Rule 2 counts a lens array's elements and walks brackets to do it. `renderStrippedView` (line 70) blanks
// '…' and "…" per line and leaves backticks ALONE, so a lens PROMPT — which is a backticked template
// literal full of English — reaches those counters as though it were code. Measured against the
// shipped hook, five prose spellings DENIED a correct five-element fan in the multi-line array shape
// every harness here is written in: a literal `...` (read as a spread), and an unmatched `[`, `]`,
// `)` or `}` (read as bracket structure). None of them is code.
//
// `renderBlankedLiterals` cannot be that view, and this was measured rather than reasoned. It blanks template
// CONTENTS including `${…}` bodies, which hold real code — an `agent(` inside a multi-line
// interpolation is DENIED today and would have been ADMITTED. And its mode is carried across lines,
// so one unterminated backtick blanks every later line and an unbounded burst below it would have
// been ADMITTED too. Both are fail-open on the only mechanical control against an agent burst.
//
// So: LINE-ALIGNED (one output line per input line, because every walk here indexes by line),
// interpolation bodies COPIED, `${…}` nesting tracked so `` `a${`b`}c` `` balances, and a report of
// whether the scan ended inside a template literal.
//
// TOOL-aLexedStripper-5 — what that last flag is FOR, and what it is not. It does NOT fail closed.
// TOOL-dMispairedQuote-1 — and the sentence below is TRUE and is NOT the explanation anyone came
// looking for. A raw fan-out got past rule 1 whenever an apostrophe shared its line, and the regex
// literal in the report was one of five spellings: a double-quoted `"don't"`, a block comment, a
// backticked `don't` and loose prose all did it too. The mechanism was the APOSTROPHE, and the fix
// is `checkLiteralOpen` above, not a regex model. What modelling regex literals would buy is
// separate and is not built: a regex's CONTENTS supply the backtick, the `)` and the `//` that made
// correcting the quote rule un-hide delimiters, which is why the shipped views are still evaluated.
// This file models no regex literal (neither does `renderBlankedLiterals`), so a backtick inside `/…/`
// opens template mode and never closes — on a LEGAL script the shipped hook admits. Denying on the
// flag traded one false-positive class for another. Instead an unterminated scan FALLS BACK to the
// per-line view rule 2 read before, which returns the shipped hook's own verdict for that script:
// it cannot regress in either direction, because it IS the shipped behaviour. The fail-open the flag
// was written to close stays closed, because the shipped hook DENIES that script too (measured).
//
// RESIDUAL, named the way `memory/map/features/agent-cap.md` names rule 1's: a script containing a
// regex literal with an odd backtick count is judged at the shipped hook's precision, not the
// improved one. That is a smaller and stated loss.
function renderLexedView(script) {
  const out = []
  let mode = 'code' // code | tmpl
  const stack = [] // 'tmpl' | 'interp', innermost last
  let interpDepth = 0 // brace depth inside the current interpolation
  // TOOL-aRepatriatedFork-7 S1 — the depth of every ENCLOSING interpolation, saved when a nested `${`
  // opens and restored when it closes. One scalar zeroed on every `${` lost the outer depth, so in
  // `${ f({ k: `b ${ x } c` }) + fan }` the object's own `}` closed the OUTER interpolation and the
  // fan-out after it left the view: measured admitted at exit 0 by a7c78ad2, through a sanctioned
  // helper the raw-text rule has no reason to fire on. adopter ic's D1, absorbed.
  const interpDepths = []
  for (const raw of script.split(/\r?\n/)) {
    let res = ''
    let i = 0
    while (i < raw.length) {
      const ch = raw[i]
      const two = raw.slice(i, i + 2)
      if (mode === 'code') {
        if (two === '//') break
        if (ch === '`') { stack.push('tmpl'); mode = 'tmpl'; res += '`'; i++; continue }
        if (ch === "'" || ch === '"') {
          // An UNPAIRED quote is ordinary text, not a string, AND SO IS ONE WHOSE ONLY AVAILABLE
          // PARTNER IS THE WRONG ONE. This used to run to end of line and append a closer the source
          // never had, swallowing the rest of that line -- and any fan-out sitting on it went too.
          // `addc6169` fixed THAT by demanding a matching PAIR, which is where it stopped: for
          // `/won't/ ... agent('a'` a pair exists, the prose apostrophe and the quote opening the
          // call, and blanking between them erased the `agent(` this rule counts (TOOL-dMispairedQuote-1).
          // `resolveLiteralEnd` asks whether a literal opens here AT ALL, which a pair test cannot reach.
          const e = resolveLiteralEnd(raw, i)
          if (e < 0) { res += ch; i++; continue }
          res += ch + ch
          i = e + 1
          continue
        }
        // Inside an interpolation, the matching `}` returns to the template it came from. Depth is
        // counted so an object literal or a block inside the expression does not close it early.
        if (stack.length && stack[stack.length - 1] === 'interp') {
          if (ch === '{') interpDepth++
          else if (ch === '}') {
            if (interpDepth === 0) { stack.pop(); interpDepth = interpDepths.length ? interpDepths.pop() : 0; mode = 'tmpl'; res += ' '; i++; continue }
            interpDepth--
          }
        }
        res += ch
        i++
      } else if (mode === 'tmpl') {
        if (ch === '\\') { i += 2; continue }
        if (two === '${') { stack.push('interp'); interpDepths.push(interpDepth); interpDepth = 0; mode = 'code'; res += '  '; i += 2; continue }
        if (ch === '`') { stack.pop(); mode = 'code'; res += '`'; i++; continue }
        i++
      }
    }
    out.push(res)
  }
  // THIS VIEW DOES NOT BLANK BLOCK COMMENTS, and that is the fix rather than an omission. It cannot
  // tell a real block-comment opener from one inside a regex literal, so every blanking it did on
  // hide a fan-out: a regex-borne opener closed by a later ordinary closer ends the scan back in
  // code mode with an empty stack, no flag fires, and the span between is gone from the view. Two
  // closing-review rounds measured that, and the second one measured the smaller repair -- widening
  // the flag -- as insufficient for exactly this shape. The view this replaced blanked no block
  // comment either, so leaving them alone cannot regress against it, and un-blanked comment text can
  // only ADD apparent code, never hide it. That is the same fail-closed posture rule 1 already
  // documents for a primitive named inside a block comment.
  //
  // The flag still reports every mode that outlives the scan, which now means an unterminated
  // TEMPLATE only.
  return { code: out, unterminated: stack.length > 0 || mode !== 'code' }
}
// TOOL-dMispairedQuote-1 — the quote branch below asks `resolveLiteralEnd` whether a literal opens at
// all, which removes both of this view's old defects: it ran to end of line synthesizing a closer the
// source never had, and it paired a prose apostrophe with the next quote. The claim below that string
// AND template contents are gone therefore holds for every span this file can RESOLVE as a literal,
// and a quote it cannot resolve is left as text on a line that is still blanked.
//
// A literal-blanked view: string AND TEMPLATE contents gone, comments gone, delimiters and structure
// kept. Rule 5 reads it, through `renderBlankedLiterals`, so a banned join named inside a prompt
// string is prose and not code.
function renderBlankedView(script) {
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
          const e = resolveLiteralEnd(raw, i)
          if (e < 0) { res += ch; i++; continue }
          res += ch + ch
          i = e + 1
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
  // TOOL-aWeldedTribunal-3 — same report as the shipped sibling, so the dispatcher's two arms return
  // one shape. A dispatcher whose arms differ is a defect every caller has to know about, which is
  // the thing a dispatcher exists to prevent.
  return { code: out, unterminated: mode !== 'code' }
}

module.exports = { MAX_VERIFIERS, renderCodeView, renderStrippedView, renderBlankedLiterals, runBothViews, readWriterBound, resolveHarnessName }
