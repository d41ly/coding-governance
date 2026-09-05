#!/usr/bin/env node
/**
 * agent-cap — project-agnostic PreToolUse guard against unbounded agent fan-out.
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
 * TWO MODALITIES, not one. A `Workflow` call is read STATICALLY (its script).
 * A direct `Agent` call carries no script, so it is counted at RUNTIME: each
 * spawn claims a numbered slot with O_EXCL under a session+prompt-keyed dir in
 * the git common dir, and the spawn that finds every slot taken is denied. The
 * budget resets on the next user prompt. Agents spawned INSIDE a workflow
 * sidechain remain uncounted and always will be — no hook runs there.
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
 *   "hooks": { "PreToolUse": [ { "matcher": "Workflow|Agent",
 *     "hooks": [ { "type": "command",
 *       "command": "node \"${CLAUDE_PROJECT_DIR}/<path>/agent-cap.js\"" } ] } ] }
 * The matcher is a LIST OF EXACT STRINGS separated by `|`, in ONE group — not a regular expression.
 * `Workflow` is where this file reads a script; `Agent` is the modality it was blind to, where a
 * direct spawn met no rule at all. Widening it is inert on its own: main() exits 0 on any tool_name
 * that is not Workflow.
 * Blocks via exit 2 + stderr (version-robust; no JSON-schema dependency).
 *
 * ponytail: a static scan can't prove a dynamically-built array is ≤CAP — this
 * enforces "use the helper", killing the exact `parallel(items.map(...))`
 * pattern that causes the bursts. Ceiling: line comments AND quoted-string
 * literals are stripped before the scan; block comments naming the primitive
 * are NOT — still trips the guard (benign, fail-closed).
 *
 * WHAT A QUOTE IS, since three rules turn on it. A quote opens a string literal
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

const KIT_AGENT_CAP_VERSION = '1.12' // gov:kit agent-cap@1.12 — engine identity (this file is deployed verbatim; the constant is the deployer's version marker)
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

// TOOL-aWeldedTribunal-3 — THE FALLBACK VIEW for the blanked readers, and it is NOT
// `renderStrippedView`. Rule 2's fallback uses that one, which leaves backticks ALONE; the two rules
// that read the blanked view were given a view that blanks template CONTENTS as a deliberate
// narrowing (TOOL-dTieredTribunal-14 S2, pinned by two self-test fixtures), and falling back to a
// view that keeps those contents would regain exactly the false-positive class those fixtures exist
// to pin — `runBothViews` UNIONS the views, so a false positive under either DENIES.
//
// So the fallback is the SAME scan with the mode reset PER LINE. That is wrong as the primary view,
// because it un-blanks the second and later lines of every legal multi-line template; as a fallback
// it is right, because it runs only when the primary scan already ended inside a literal, and a
// per-line reset cannot carry one line's damage into the next. It preserves the narrowing within
// each line, which is what the unit's S6 requires.
function renderPerLineBlanked(script) {
  return script.split(/\r?\n/).map((line) => {
    const one = renderBlankedLiterals(line)
    return one.code[0] === undefined ? '' : one.code[0]
  })
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
// `capFindings` can push more than one finding for a single line and keying on `n` alone would drop
// the second.
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
      const code = renderStrippedView(line).split('//')[0] // strings blanked, then line-comments
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
//   (b) an identifier assigned from an ARRAY LITERAL with <= MAX_LENSES elements — the finder-lens
//       case, where the agent count is a constant visible in the source. The count drops a trailing
//       comma; counting it as an element is what made this allowance read as 6.
// Everything else is denied, including a for/while/forEach body containing `agent(`: a loop-built
// thunk array is the evasion, not an edge case.
const FIXED_MARK = 'gov:fixed-verifiers'
const MAX_VERIFIERS = 5
// ONE NUMBER, ratified by the owner 2026-08-10 (spec F2). The lens allowance used to sit at 6 and
// read as a deliberate find-stage affordance; it was not. It was the trailing-comma miscount above,
// and no shipped harness has ever had six lenses — tier2-review has four, both drift-audit waves
// have five. With the count fixed, 5 is what the charter says and what every harness already obeys.
const MAX_LENSES = 5
// THE THIRD MARKER, and the only one that admits a LOOP. Spelling ratified by the owner
// 2026-09-01: `gov:sequential-agents`, carrying its bound — `gov:sequential-agents(5)`.
//
// WHY IT EXISTS. `TOOL-cBriefedPilot-21` ratified `parallelism route: none`, while this hook denied
// an `agent()` in ANY loop body unconditionally. Bounded-parallel was PERMITTED by the hook and
// FORBIDDEN by the verdict; strictly sequential was REQUIRED by the verdict and FORBIDDEN by the
// hook. A harness iterating a build's units sat exactly in that gap and could not be written at all.
//
// THE MARKER IS A CLAIM, NEVER A PERMISSION. EVERY clause below must hold, and the two carrying the
// weight are the bounded RECEIVER — the loop must iterate a bare identifier this file already proves
// bounded, which is what `chunk(x, Math.ceil(x.length / K))` is for the fixed-verifiers marker — and
// the one-call sweep after the scan, which makes the number a SPAWN count rather than an ITERATION
// count. A bound with no bounded receiver is the shape the owner ruling names: it would admit
// `gov:sequential-agents 5` over an unbounded array while spawning one agent per element.
const SEQ_MARK = 'gov:sequential-agents'
// Every array method that can carry an agent() call once per element. The list is closed and
// generous on purpose: a method missing from it used to mean ALLOW, which is the fail-open direction.
const ITER_CALL = /\.\s*(map|flatMap|forEach|filter|reduce|reduceRight|some|every|find|findIndex|sort|flat)\s*$/

// TOOL-aWeldedTribunal-1 — THE LOOP KEYWORD SET, spelled ONCE. Six sites in this file used to ask
// "is this a loop" and each held its own `/\b(for|while)\s*\(/`, which is two answers to one
// question six times over. Two ordinary spellings matched none of them and were MEASURED at exit 0
// carrying an unmarked thunk-array fan past this hook (TOOL-dFoldedVerdict-8): `for await (` puts an
// identifier between the keyword and the paren, and a `do { … } while (…)` block's opening line
// carries no keyword at all because its `while` sits after the closing brace.
//
// THREE FORMS, because three sites ask the question differently and a single regex cannot serve all
// of them. `LOOP_HEADER` matches an opener anywhere on a line. `LOOP_HEADER_G` is the same with the
// global flag, for the site that COUNTS openers. `LOOP_KEYWORD_TAIL` matches a keyword at
// END-of-text, for the opener walk, which tests the text BEFORE a paren — a pattern ending in `\(`
// or `do\s*\{` can never match there. The `do` spelling is deliberately absent from the tail form: a
// `do` block opens with a BRACE, so it never appears as an enclosing paren opener.
//
// Measured before wiring, over all eight tracked *.js: ZERO lines match the widened form and not the
// old one, so nothing currently admitted becomes denied. The widening reaches the evasions only.
const LOOP_KEYWORDS = 'for(?:\\s+await)?|while'
const LOOP_HEADER = new RegExp('\\b(?:' + LOOP_KEYWORDS + ')\\s*\\(|\\bdo\\s*\\{')
const LOOP_HEADER_G = new RegExp('\\b(?:' + LOOP_KEYWORDS + ')\\s*\\(|\\bdo\\s*\\{', 'g')
const LOOP_KEYWORD_TAIL = new RegExp('\\b(?:' + LOOP_KEYWORDS + ')\\s*$')

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

// TOOL-dTieredTribunal-13 S2 - split an expression into its top-level VALUE branches. Depth-aware
// over (), [] and {}; skips `?.` and `??`, which are not ternaries; recurses into nested ternaries;
// and DROPS the condition, because a condition is not a value the fan-out ever iterates. A `?` whose
// `:` this walk cannot find yields a single null branch, and a null branch never qualifies — so an
// expression this file cannot delimit lands on the DENY side rather than being waved through.
function parseBranches(expr) {
  const t = String(expr)
  let d = 0
  for (let i = 0; i < t.length; i++) {
    const ch = t[i]
    if ('([{'.includes(ch)) { d++; continue }
    if (')]}'.includes(ch)) { d--; continue }
    if (d !== 0 || ch !== '?') continue
    if (t[i + 1] === '.' || t[i + 1] === '?') { i++; continue }
    let dd = 0
    let nest = 0
    for (let j = i + 1; j < t.length; j++) {
      const c = t[j]
      if ('([{'.includes(c)) { dd++; continue }
      if (')]}'.includes(c)) { dd--; continue }
      if (dd !== 0) continue
      if (c === '?') { if (t[j + 1] === '.' || t[j + 1] === '?') { j++; continue } nest++; continue }
      if (c === ':') {
        if (nest > 0) { nest--; continue }
        return parseBranches(t.slice(i + 1, j)).concat(parseBranches(t.slice(j + 1)))
      }
    }
    return [null]
  }
  return [t]
}

// TOOL-dTieredTribunal-13 S3 - the qualifying forms are a CLOSED list and each branch is judged on
// its OWN text. Three forms and no fourth: a bounded split whose K resolves through `boundedK`; an
// array LITERAL whose top-level element count is at or under MAX_LENSES, counted with the shared
// splitter so a trailing comma is not an element; or a bare identifier already proven bounded,
// alone or followed by a chain of operations that cannot grow it.
function boundedBranch(br, name, consts, ok) {
  if (br === null) return false
  const t = String(br).trim()
  if (!t) return false
  const c = /\bchunk\s*\(\s*[^,]+,\s*Math\.ceil\s*\(\s*[A-Za-z_$][\w$.]*\.length\s*\/\s*([^)]+)\)/.exec(t)
  const sp = /\bsplitInto\s*\(\s*[^,]+,\s*([^),]+)\)/.exec(t)
  if ((c && boundedK(c[1], consts)) || (sp && boundedK(sp[1], consts))) return true
  if (t.startsWith('[') && t.endsWith(']')) return topLevelArgs(t.slice(1, -1)).length <= MAX_LENSES
  const m = /^([A-Za-z_$][\w$]*)([\s\S]*)$/.exec(t)
  if (!m || m[1] === name || !ok.has(m[1])) return false
  const tail = m[2].trim()
  if (tail === '') return true
  // M8 closing review, HIGH: the tail used to be one greedy `[\s\S]*` inside an optional
  // filter/slice group. It matched the FIRST call and then swallowed the whole rest of the chain,
  // so `ALL.filter(x).reduce((a, b) => args.big, [])` was ADMITTED - and that returns a caller
  // array of any length. A bound escape through the very tightening written to close the class.
  // Every TOP-LEVEL call on the chain must now be shrink-only. Depth-aware, because the calls
  // inside a predicate body are not chain links: `.filter((L) => a.lenses.includes(L.slug))` is
  // the shipped user, and counting its `.includes(` would deny it. `.map` is denied too although
  // it preserves length - the qualifying forms are a closed list, and widening it is an edit.
  // ROUND 2 - the first cut of this walk counted links and returned `links > 0`, which asked only
  // whether a shrink call APPEARED. It never required the tail to be CONSUMED, so everything after
  // the last link went unexamined and an unbalanced tail was fine. That was a NET REGRESSION on the
  // regex it replaced, measured: `const LENSES = ALL.filter( // gov:fixed-verifiers` continued on
  // the next line was DENIED at eb4b0660 and ADMITTED at the tip, fanning agent() over whatever the
  // continuation built. The regex it replaced ended in `\)$`, and dropping that anchor is what cost
  // the property. Three separate escapes shared the one root, so the walk is now CONSUMING: each
  // segment must be a shrink call, each must CLOSE, and the tail must end with the last one.
  const SHRINK = ['filter', 'slice']
  let i = 0
  let links = 0
  while (i < tail.length) {
    if (/\s/.test(tail[i])) { i++; continue }
    // A segment that is not `.<name>(` at all - a computed `["concat"](…)` member, a trailing
    // `|| args.big`, an operator, anything - ends the walk in a refusal rather than being skipped.
    const call = /^\.\s*([A-Za-z_$][\w$]*)\s*\(/.exec(tail.slice(i))
    if (!call || SHRINK.indexOf(call[1]) === -1) return false
    let j = i + call[0].length
    let d = 1
    while (j < tail.length && d > 0) {
      const c = tail[j]
      if (c === '(' || c === '[' || c === '{') d++
      else if (c === ')' || c === ']' || c === '}') d--
      j++
    }
    // An unclosed segment is REFUSED, never assumed closed. `renderStrippedView` blanks '' and "" but not
    // a template literal, so a stray `(` inside one strands this counter - and the safe reading of
    // "this file cannot tell where the chain ends" is that it cannot prove the receiver bounded.
    if (d !== 0) return false
    i = j
    links++
  }
  return links > 0
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

function fanoutFindings(script) {
  const lines = script.split(/\r?\n/)
  // TOOL-aLexedStripper-5: an unterminated scan falls back to the per-line view, which returns
  // the verdict this hook reached before rule 2 moved. Not a fail-closed branch: that denied a
  // legal script carrying a regex literal with a backtick in it.
  // TOOL-dMispairedQuote-1 SUPERSEDES the "returns the verdict this hook reached before" half. That
  // record was CLOSED on the argument that this fallback IS the shipped behaviour and therefore
  // cannot regress in either direction; the per-line view has since been re-based, so the argument
  // no longer holds and is not the reason to trust this branch. What holds is the no-regression
  // property: `runBothViews` evaluates this rule over the SHIPPED views too.
  const view = renderCodeView(script)
  const code = view.unterminated ? lines.map((l) => renderStrippedView(l).split('//')[0]) : view.code

  // integer consts bound in this file, e.g. `const MAX_VERIFIERS = 5`
  const { consts } = intConsts(code)

  // Receivers this file can prove are bounded. TWO PASSES, because a derived lens set is written
  // AFTER the literal it derives from (`const LENSES = ALL_LENSES.filter(…)`), and a single forward
  // pass would reject it on declaration order rather than on the property being checked.
  const ok = new Set()
  // S4 - one reason per refused marked assignment, keyed by the name it binds.
  const markedWhy = new Map()
  // TOOL-aWeldedTribunal-2, closing-review fold: which bounded names a blessing LEANED ON, so a
  // take-back can follow the derivation instead of stopping at the mutated name.
  const derivedFrom = new Map()
  // TOOL-dFoldedVerdict-4: candidates admitted by `gov:sequential-agents`, judged again after the
  // scan by the one-call sweep. Collected rather than cleared immediately, because the ninth
  // condition is about a GROUP and no per-line pass can see one.
  const seqAdmitted = []
  const SEQ_BOUND = new RegExp(SEQ_MARK.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\s*\\(?\\s*([A-Za-z_$][\\w$]*|\\d+)\\s*\\)?')
  // Returns '' when NO claim was made — the unmarked denial keeps its exact shipped sentence, which
  // several arms assert by literal — a ` — <reason>` suffix naming the FIRST clause that failed, or
  // null when every clause holds.
  const checkSeqMarker = (h, i, c, l) => {
    const rawH = lines[h] || ''
    // C2: read the MARKER from the RAW line. Both views break their scan on `//`, so a marker is
    // invisible in `code` — the same reason FIXED_MARK is read from `raw` inside `scan`.
    if (!rawH.includes(SEQ_MARK)) return ''
    const mm = SEQ_BOUND.exec(rawH)
    // C3: a bare marker claims concurrency one with an UNBOUNDED TOTAL, which is the owner's
    // stated refusal — the two rules are separate and the marker must satisfy both.
    if (!mm) return ` — ${SEQ_MARK} carries no bound token, and a bare marker claims concurrency one with an unbounded total`
    // C4: the number is CHECKED, never trusted, and by the one resolver every other consumer uses.
    if (!boundedK(mm[1], consts)) return ` — ${SEQ_MARK}(${mm[1]}) names a bound this file does not resolve to an integer no greater than ${MAX_VERIFIERS}`
    const ch = code[h] || ''
    // C5: the SHAPE is read from the literal-blanked view, so a marker sitting inside a quoted
    // string on a line that is not really a loop header blesses nothing.
    if (!LOOP_HEADER.test(ch)) return ` — the marked line is not a loop header in the code view, so the marker sits inside a string and blesses nothing`
    // C6: THE CLAUSE THAT CARRIES THE WEIGHT. The bound is the author's claim; a receiver this file
    // already proves bounded is what makes the total real.
    // TWO OPENERS ON ONE LINE CANNOT BE ATTRIBUTED. `for (const g of OK) for (const f of ALL)`
    // put a bounded token on the header of a loop that iterates something else, and the brace walk
    // stops at the shared line so the inner loop never gets its own header. Refused outright.
    if ((ch.match(LOOP_HEADER_G) || []).length > 1) return ` — the marked header carries more than one loop opener, and this scan cannot tell which of them the call belongs to`
    // A STRICT for-of HEADER, matched as a whole from the `for (` itself. The earlier form read the
    // first `of <ident>)` ANYWHERE on the line, so a block comment, a guard clause or an outer loop
    // supplied the bounded token for free — measured, four ways. `while` is refused with no special
    // case: it has no iteration source this scan can size, and a bound over an unsizeable loop is
    // the claim the receiver clause exists to refuse.
    const rm = /\bfor\s*\(\s*(?:const|let|var)\s+[A-Za-z_$][\w$]*\s+of\s+([A-Za-z_$][\w$]*)\s*\)/.exec(ch)
    if (!rm) return ` — the marked loop is not a \`for (const x of <bounded identifier>)\` header, and an iteration source this scan cannot size is a denial rather than a pass`
    if (!ok.has(rm[1])) return ` — the marked loop iterates \`${rm[1]}\`, which this file does not show to be bounded; the marker names a number and the receiver is what makes it real`
    // C7: AWAIT-ADJACENCY on THIS occurrence, not "the line contains await" — a line may hold both
    // an awaited call and a deferred one.
    if (!/\bawait$/.test(l.slice(0, c).replace(/\s+$/, ''))) return ` — this agent() is not directly awaited, so the loop builds values instead of spending one turn each`
    // C8: a function boundary between the opener and the call makes it a THUNK, which is the
    // evasion the ban exists for.
    const body = code.slice(h, i).join('\n') + l.slice(0, c)
    if (/=>/.test(body) || /\bfunction\b/.test(body)) return ` — a function boundary sits between the loop header and this call, which makes it a deferred thunk`
    // NOTHING MAY ENCLOSE THE MARKED LOOP. The sweep bounds ONE body; an outer loop multiplies it by
    // a count nothing here can size, and that outer loop is never evaluated on its own because no
    // `agent(` line is attributed to it. Measured both ways: two honest nested markers spent 5 x 5
    // = 25 under a marker naming 5, and an UNMARKED outer loop did it unboundedly. `k !== h` so the
    // header's own opener is not counted against it.
    let ob = 0
    for (let k = h; k >= 0 && k > h - 60; k--) {
      for (const ch2 of code[k]) {
        if (ch2 === '}') ob++
        else if (ch2 === '{') ob--
      }
      if (ob < 0 && k !== h && LOOP_HEADER.test(code[k])) return ` — the marked loop is itself inside a loop opened at line ${k + 1}, which multiplies its bound by a count nothing here can size`
      if (ob < 0) ob = 0
    }
    return null
  }
  const scan = (raw, i) => {
    const l = code[i]
    const asg = /\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=/.exec(l)
    if (!asg) return
    const name = asg[1]
    if (raw.includes(FIXED_MARK)) {
      // TOOL-dTieredTribunal-13 S1 - EVERY top-level value branch is judged, not the first that
      // happens to match. This block used to be two sequential accepts, and either could return on a
      // SINGLE arm: a marked ternary whose other branch was caller-supplied passed, and an
      // args-supplied array of any length then reached agent() once per element. That is the same
      // defeat the `<expr> || <int>` binder was deleted for — a caller-settable knob wearing a
      // constant's clothes. Reproduced against this file before the rewrite.
      const rhs = l.slice(l.indexOf('=') + 1)
      // The whole-RHS growth veto is kept and still vetoes the assignment however the branches read.
      // The first cut of the derivation receiver accepted any line MENTIONING a bounded name, which
      // blessed `ALL_LENSES.concat(allFindings)` on the strength of the word appearing.
      const grows = /\b(concat|push|flat|flatMap|fill|repeat)\s*\(|\.\.\./.test(rhs)
      const branches = parseBranches(rhs)
      const bad0 = branches.find((b) => !boundedBranch(b, name, consts, ok))
      if (!grows && branches.length && bad0 === undefined) {
        // TOOL-aWeldedTribunal-2, closing-review fold. RECORD WHAT THIS BLESSING LEANED ON. A
        // derivation like `const groups = batches.filter(Boolean)` is bounded only because
        // `batches` was; when a later take-back removes `batches`, `groups` kept a bound nothing
        // supported any more, and an unbounded agent-per-finding fan was admitted one `.filter()`
        // away. The cascade below drops the derived name too.
        const srcs = new Set()
        for (const br of branches) {
          const lead = /^\s*([A-Za-z_$][\w$]*)/.exec(String(br))
          if (lead && lead[1] !== name && ok.has(lead[1])) srcs.add(lead[1])
        }
        if (srcs.size) derivedFrom.set(name, srcs)
        ok.add(name)
        // D10 - the reason is a CACHE and both scan passes write it. A name refused on pass 1 for a
        // declaration-order reason and ACCEPTED on pass 2 kept the pass-1 text, so a later refusal
        // printed an explanation of a branch this pass had just blessed. Clear it on accept: a
        // guard whose stated reason is wrong is a guard an operator cannot act on, which is the
        // exact failure the S4 note below says this map was added to remove.
        markedWhy.delete(name)
        return
      }
      // S4 - record WHY, keyed by the name bound. The refusal a caller saw was emitted at the
      // fan-out line and named only the receiver, while the author was looking at a marked
      // assignment two lines above. This is the convention `why()` already applies to every
      // unresolvable K: one explanation per refusal, naming the FORM, because an operator who
      // cannot tell which spelling was refused fixes it by guessing.
      markedWhy.set(
        name,
        grows
          ? `\`${name}\` carries ${FIXED_MARK} but its right-hand side can GROW the receiver`
          : !branches.length || bad0 === null
            ? `\`${name}\` carries ${FIXED_MARK} but this file cannot delimit its value branches`
            : /\b(chunk|splitInto)\s*\(/.test(String(bad0))
              // A branch that IS a bounded split and still fails, failed on its K. Saying only that
              // the branch is not a bounded form would send the author to rewrite a spelling that is
              // already correct, so the cap is named instead — and the phrase the generic refusal
              // uses is kept, because two self-test arms assert a marked K's refusal by that text and
              // a message edit that strands an arm is a recorded class in this repo.
              ? `\`${name}\` carries ${FIXED_MARK} but its bounded split names a cap which this file does not show to be bounded`
              : `\`${name}\` carries ${FIXED_MARK} but the branch \`${String(bad0).trim()}\` is not one of the bounded forms`,
      )
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
    // ONE splitter, shared with the call-site walk below, because a TRAILING COMMA is not an element
    // any more than it is an argument. Counting `1 + every top-level comma` made a 5-element lens
    // array measure 6 — which is the entire reason MAX_LENSES was 6. It never meant "six lenses are
    // allowed"; it meant "five lenses, plus the phantom the counter invented". Every shipped harness
    // is prettier-formatted, so every one of them was mis-measured, and the constant was raised to
    // fit the error rather than the error being found.
    if (topLevelArgs(inner).length <= MAX_LENSES) ok.add(name)
  }
  lines.forEach(scan)
  lines.forEach(scan)

  // THE TAKE-BACK SWEEPS READ `code` DIRECTLY, WITH NO COMMENT STRIP, and the four review rounds
  // that led here are the reason — this comment is the finding, not decoration.
  //
  // The closing review's round 1 reported a FALSE DENY: `/* never do LENSES.push(x) */` revoked a
  // legal bound, because `renderCodeView` deliberately does not blank block comments. Three separate
  // fixes for that cosmetic complaint each bought a FAIL-OPEN on the only mechanical control this
  // repo has against an agent burst:
  //
  //   round 2 — the blanked view erases `${…}` bodies, so `` `${LENSES.push(x)}` `` went invisible
  //   round 3 — a joined-text strip paired a regex literal's `/*` with the next real `*/` below it
  //   round 4 — a per-line strip did the same thing within one line
  //
  // The common cause is not any of those regexes. It is that THIS FILE MODELS NO REGEX LITERAL, by
  // a standing decision `renderLexedView`'s own header records, so every comment strip built on top
  // of it inherits that blindness in a new shape. Closing the class needs a regex-literal-aware
  // lexer, which this file has never had and which is not this unit's scope.
  //
  // So the strip is GONE and the false deny is ACCEPTED. That is the fail-CLOSED direction and the
  // charter's stated posture: a construct this rule cannot prove bounded is denied, and the burden
  // is on the fan-out rather than on the gate. Weighed plainly — a comment mentioning a growth costs
  // an author one reworded comment; a fail-open costs an unbounded agent burst nothing.
  //
  // THE RESIDUAL, named: a comment or a string that mentions `<bounded>.push(` revokes that name's
  // bound and denies the script. No tracked harness writes one — all five still exit 0 — and this is
  // exactly the behaviour that shipped before this build, so it is a preserved property rather than
  // a new cost. `memory/gotchas/` carries the class.
  const takeBackView = code

  // A BARE REASSIGNMENT invalidates the bound. `let items = [1, 2]` then `items = allFindings` was a
  // measured bypass: the whitelist was keyed on a name and nothing ever took the name back. The
  // protocol publishes "assigned exactly once", so anything assigned twice loses the claim.
  // R6: it reads the comment-free view too. The first fold gave that to the growth sweep alone, so a
  // block-commented reassignment still denied a legal harness — the same class, one sweep over.
  takeBackView.forEach((l) => {
    const m = /(?:^|[;{}]\s*)([A-Za-z_$][\w$]*)\s*=[^=]/.exec(l)
    if (m && !/\b(const|let|var)\s+$/.test(l.slice(0, m.index + m[0].indexOf(m[1])))) {
      if (!/\b(?:const|let|var)\s+[A-Za-z_$][\w$]*\s*=/.test(l)) {
        // ROUND 2 - the reason was written for EVERY reassigned name, including names this file had
        // never bounded, so a refusal could announce that a bound was taken back that was never
        // granted. That is D10's own failure mode inverted: right verdict, false reason. Only a name
        // actually in `ok` had a bound to lose, so only that name gets this explanation.
        const hadBound = ok.has(m[1])
        ok.delete(m[1])
        if (!hadBound) return
        // ...and this sweep runs AFTER both passes, so it states its own reason too. Without that, a
        // name accepted on pass 2 and taken back here falls through to whatever pass 1 happened to
        // write, or to the generic fan-out text - neither of which names the reassignment.
        markedWhy.set(m[1], `\`${m[1]}\` was REASSIGNED after its bounded assignment, which takes the bound back`)
      }
    }
  })

  // TOOL-aWeldedTribunal-2 — A GROWTH CALL TAKES THE BOUND BACK, exactly as a reassignment does.
  // `const batches = []` counts zero elements and is blessed by the array-literal case above; a
  // later `batches.push(...)` grows it to one entry per finding with the bound still standing
  // (TOOL-aCandidStub-1). Runs AFTER both scan passes and beside the reassignment sweep, for that
  // sweep's own stated reason: a name accepted on pass 2 and taken back earlier would fall through
  // to whatever pass 1 wrote.
  //
  // NOT THE RIGHT-HAND-SIDE VOCABULARY, and the difference was MEASURED rather than reasoned. The
  // marked-branch veto lists `concat|push|flat|flatMap|fill|repeat`, and three of those are
  // NON-MUTATING: `concat`, `flat` and `flatMap` return a NEW array and leave the receiver exactly
  // as long as it was. Run over this tree, that list took the bound back from `ALL_LENSES` on the
  // strength of a `.concat` that changes nothing. The two answer different questions — the RHS one
  // asks whether an expression can PRODUCE something bigger, this one whether a statement GROWS the
  // array named — so they share this comment and not a constant.
  //
  // RESIDUALS, named rather than implied: a mutation through an alias (`const b = batches; b.push`)
  // is not tracked, because this file tracks names and not values; and `batches[i] = x` past the end
  // and `batches.length = n` both grow an array and are not here, because a regex over
  // `name[<expr>] =` matches every ordinary element write and denies innocent files.
  // THE LEFT GUARD IS ZERO-WIDTH, and it took two rounds to get there. `\b` alone captured the LAST
  // segment of a member chain, so `state.lenses.push(x)` withdrew the bound from an unrelated
  // top-level `lenses`. The obvious repair — a consuming class `[^.\w$)\]]` — leaked TWICE from one
  // regex: it excluded `)` and `]`, so `if (x) LENSES.push(y)` never matched at all; and because it
  // CONSUMES the character it inspects, under `/g` a receiver sitting right after a previous match's
  // `(` was unreachable, so `sink.push(LENSES.push(9))` escaped. Both close with the LOOKBEHIND form
  // this file already uses in `offendingLines`: it asserts without consuming, and it excludes only
  // what actually makes a name a member — a dot or a name character.
  const GROWS_RECEIVER = /(?<![.\w$])([A-Za-z_$][\w$]*)\s*\.\s*(?:push|unshift|splice)\s*\(/g
  takeBackView.forEach((l, li) => {
    let g
    GROWS_RECEIVER.lastIndex = 0
    while ((g = GROWS_RECEIVER.exec(l))) {
      // Scoped to a name that HAD a bound, mirroring the reassignment sweep's `hadBound` guard:
      // announcing that a bound was withdrawn from a name that never had one is that guard's own
      // recorded defect, right verdict and false reason.
      if (!ok.has(g[1])) continue
      // A REMOVAL-ONLY `splice` SHRINKS. `LENSES.splice(0, 2)` takes two elements OUT, and revoking
      // a bound for that is a denial whose stated reason — "was GROWN" — is false about the array it
      // names. Only a 3-plus-argument splice inserts.
      //
      // TWO CORRECTIONS FROM ROUND 2, both fail-OPEN. The line was resolved by VALUE
      // (`indexOf(l)`), so two textually identical splice lines graded the later one against the
      // earlier one's arguments — the free `forEach` index is the whole fix. And counting top-level
      // commas cannot see through a SPREAD, so `LENSES.splice(...more)` read as a two-argument
      // shrink; a spread is unbounded growth, which the marked-branch veto forty lines above already
      // says, so it is treated as growth here rather than measured.
      if (/\.\s*splice\s*\($/.test(l.slice(0, g.index + g[0].length))) {
        // The spread test is over the TOP-LEVEL arguments, not the whole call text. Scanning the
        // text made `LENSES.splice(0, Math.min(...ns))` read as growth — a spread nested inside an
        // argument grows nothing, and denying it states "was GROWN" about an array that shrank.
        //
        // AND AN ARGUMENT LIST CARRYING A COMMENT IS NOT GRADED AT ALL. `splice(0, /*…*/ ...rest)`
        // put the comment in front of the spread, so a prefix test saw a two-argument shrink and
        // admitted a growth. Since this file models no regex literal, no comment strip here can be
        // trusted — that is the whole lesson of rounds 2 through 4 — so a call this scan cannot read
        // cleanly is DENIED rather than measured. Fail-closed, on a shape nothing writes.
        const call = joinCall(takeBackView, li, g.index + g[0].length - 1)
        const args = call && !/\/\*|\/\//.test(call.text) ? topLevelArgs(call.text) : null
        if (args && !args.some((a) => a.trim().startsWith('...')) && args.length < 3) continue
      }
      ok.delete(g[1])
      markedWhy.set(g[1], `\`${g[1]}\` was GROWN by a mutation after its bounded assignment, which takes the bound back`)
    }
  })

  // THE CASCADE. Both take-back sweeps above remove the name they matched and stop there, so a
  // DERIVED name kept a bound its source no longer has: `const groups = batches.filter(Boolean)`
  // with the marker still exits 0 after `batches.push(...)` revoked `batches`. Iterated to a fixed
  // point rather than one pass, because a derivation can lean on a derivation. The pre-existing
  // reassignment sweep had the same hole and is covered here too, since both write to the same
  // `ok` set and this runs after both.
  for (let pass = 0; pass < derivedFrom.size + 1; pass++) {
    let moved = false
    derivedFrom.forEach((srcs, n) => {
      if (!ok.has(n)) return
      srcs.forEach((s) => {
        if (ok.has(s)) return
        ok.delete(n)
        markedWhy.set(n, `\`${n}\` was derived from \`${s}\`, whose bound was taken back, so this one no longer holds either`)
        moved = true
      })
    })
    if (!moved) break
  }

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
      // The TAIL form: this tests the text BEFORE an opener position, so a pattern ending in `\(`
      // can never match here. `for await (` used to miss, leaving `hit` null so the walk continued
      // OUTWARD — and if the next enclosing opener was a bounded `.map(` receiver already in `ok`,
      // the call-site arm returned with no finding and the loop arms below were never reached.
      // A fail-open the header widening alone does not close (TOOL-aWeldedTribunal-1, H3).
      if (LOOP_KEYWORD_TAIL.test(before)) { hit = { kind: 'loop' }; break }
    }
    if (hit && hit.kind === 'iter') {
      if (hit.name === null) {
        bad.push({ n: i + 1, line: raw, why: `agent() fanned through .${hit.method}() over an expression this file cannot size (\`${hit.expr}\`) — only a bare identifier proven bounded is accepted` })
      } else if (!ok.has(hit.name)) {
        // S4 - prefer the marked assignment's own reason. The generic sentence is right and useless
        // when the author already wrote a marker and got no word about which branch failed.
        bad.push({ n: i + 1, line: raw, why: markedWhy.get(hit.name) || `agent() fanned over \`${hit.name}\`, which this file does not show to be bounded` })
      }
      return
    }
    if (hit && hit.kind === 'from') {
      bad.push({ n: i + 1, line: raw, why: 'agent() fanned through Array.from() — the count is not visible here' })
      return
    }
    // THE ENCLOSING LOOP HEADER IS LOCATED FIRST, THEN THE CALL IS JUDGED (TOOL-dFoldedVerdict-4).
    // Both branches used to deny in place; `gov:sequential-agents` is read off the HEADER line, so
    // the walk that finds it is hoisted and one predicate supplies both reasons.
    const c = l.search(/\bagent\s*\(/)
    let h = -1
    let braceless = false
    // A BRACELESS loop body: `for (const f of all) out.push(await agent(f))`. The brace walk below
    // cannot see it — there is no brace — and it was one of the measured bypasses.
    if (LOOP_HEADER.test(l.slice(0, c))) { h = i; braceless = true }
    else {
      // A loop BODY is a brace block, not a paren, so it never shows up as an enclosing opener.
      // Judged separately: an unclosed `for (`/`while (` block whose brace is still open above.
      let braces = 0
      for (let k = i; k >= 0 && k > i - 60; k--) {
        for (const ch of code[k]) {
          if (ch === '}') braces++
          else if (ch === '{') braces--
        }
        if (braces < 0 && LOOP_HEADER.test(code[k])) { h = k; break }
        if (braces < 0) braces = 0 // a different block opened here; keep looking outward
      }
    }
    if (h < 0) return
    // NESTED LOOPS FAIL CLOSED WITH NO EXTRA CLAUSE: the walk stops at the FIRST enclosing loop, so
    // an inner loop must carry its own marker and its own bounded receiver.
    const why = checkSeqMarker(h, i, c, l)
    if (why === null) {
      // EVERY OCCURRENCE ON THE LINE COUNTS, not the first. The scan is per-LINE and `c` is the
      // first match, so `await agent(u); await agent(u)` used to contribute one entry and the sweep
      // saw a group of one — the bound became a LINE count, which is not a bound at all.
      const calls = (l.match(/\bagent\s*\(/g) || []).length
      for (let q = 0; q < Math.max(1, calls); q++) seqAdmitted.push({ h, n: i + 1, line: raw })
      return
    }
    bad.push({
      n: i + 1,
      line: raw,
      why: braceless
        ? `agent() in a braceless loop body — a loop-built fan-out is the evasion this rule exists for${why}`
        : `agent() inside a loop body — a loop-built thunk array is the evasion this rule exists for${why}`,
    })
  })
  // THE ONE-CALL SWEEP, and it is what turns the marker's number from an ITERATION bound into a
  // SPAWN bound. Two awaited calls in one marked body spend twice what the marker names, so the
  // marker would be claiming a number the loop does not obey. Without this the shipped rule carries
  // a stated 2x fail-open in its own admission path, which is the thing this unit exists to avoid.
  const byHeader = new Map()
  for (const a of seqAdmitted) {
    if (!byHeader.has(a.h)) byHeader.set(a.h, [])
    byHeader.get(a.h).push(a)
  }
  // ONE MARKED LOOP PER SCRIPT. The per-header sweep below bounds a single body; it relates no two
  // headers, so two honest markers multiplied (nested) or summed (sequential) with every clause
  // satisfied. `MAX_VERIFIERS` is a TOTAL, and the only total this scan can actually prove is the
  // one belonging to a single admitted loop.
  if (byHeader.size > 1) {
    const hs = [...byHeader.keys()].map((x) => x + 1).join(', ')
    for (const [, group] of byHeader) {
      for (const a of group) {
        bad.push({ n: a.n, line: a.line, why: `${SEQ_MARK} appears on ${byHeader.size} loop headers in this script (lines ${hs}) and the bound is a TOTAL, so two marked loops multiply or sum it — only ONE marked loop per script can be proven bounded` })
      }
    }
  }
  for (const [hh, group] of byHeader) {
    if (group.length < 2) continue
    for (const a of group) {
      bad.push({
        n: a.n,
        line: a.line,
        why: `${SEQ_MARK} on line ${hh + 1} admits ONE awaited agent() in its body and this body holds ${group.length}, so the loop spends ${group.length} times the bound the marker names`,
      })
    }
  }
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
// slicing fifty wide. All three markers are claims now.
//
// FAIL CLOSED, like every other branch here: a K this file cannot resolve to an integer at or under
// MAX_VERIFIERS is a denial. The burden is on the fan-out.
const HELPERS = /(?<![.\w$])(boundedParallel|boundedPipeline)\s*\(/g

// TOOL-dMispairedQuote-1 — the re-baselining this header's author declined is DONE, and measured.
// The quote branch below now asks `resolveLiteralEnd` whether a literal opens at all, which removes
// both of this branch's defects: it ran to end of line synthesizing a closer the source never had,
// and it paired a prose apostrophe with the next quote. Rule 3 reads the BOUND through a cross-line
// paren join, so either one hid a declared width behind an ordinary-looking comment; a cap of 50 was
// reproduced as ADMITTED. The three dozen measured arms this header worried about all still pass,
// and eleven more were added. The claim below that string AND template contents are gone therefore
// holds for every span this file can RESOLVE as a literal, and a quote it cannot resolve is left as
// text on a line that is still blanked.
//
// A literal-blanked view: string AND TEMPLATE contents gone, comments gone, delimiters and structure
// kept. The per-line strip the two rules above run on cannot see a template literal spanning lines,
// and a `(` inside a prompt string unbalances a forward paren join — which is the one mechanism this
// rule is built on. Deliberately a SECOND view rather than a replacement: the existing strip carries
// three dozen measured arms and is not worth re-baselining for a rule that can afford its own pass.
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
  // TOOL-aWeldedTribunal-3 — an UNTERMINATED scan falls back to the per-line blanked view. The
  // primary view carries its mode across lines, so one unterminated backtick blanked every line
  // below it and this rule saw nothing under it (TOOL-aLexedStripper-4). Not a fail-closed branch:
  // `TOOL-aLexedStripper-5` measured that and it denied a legal script carrying a regex literal with
  // a backtick in it.
  const view = renderBlankedLiterals(script)
  const code = view.unterminated ? renderPerLineBlanked(script) : view.code
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

// ---------------------------------------------------------------------------
// RULE 4 — the ARITY of DIRECT `Agent` spawns, as an ATOMIC COUNT.
//
// Rules 1-3 read a workflow SCRIPT, so they reach exactly one of the two ways agents get spawned. A
// session that fans out with direct `Agent` tool calls met no rule at all — the charter calls the
// number BINDING and the commonest modality was unguarded.
//
// THE CASE THIS FILE'S OWN REJECTED ALTERNATIVE WAS ABOUT IS STILL REJECTED. Counting agents spawned
// INSIDE a workflow script is impossible: that script runs in a sidechain with no hooks, so nothing
// observes those spawns. A main-loop `Agent` call differs in kind — a hook DOES fire. MEASURED on
// node a before any of this was written: `tool_name` arrives as exactly `Agent`, and the payload
// carries `session_id`, `prompt_id` and `tool_use_id`.
//
// WHY SLOTS AND NOT A COUNT. Read-then-decide loses updates: measured on node a, a four-call burst
// overlapped its hook processes and two of four read the same count. Create-a-token-then-count does
// not fix it either — six concurrent processes each see between their own ordinal and six, so
// several deny and the arm requiring EXACTLY ONE deny fails nondeterministically. Claiming a
// NUMBERED slot with O_EXCL is decided entirely by the atomic create: exactly MAX_VERIFIERS slots
// can ever exist, so exactly one process out of the sixth-and-beyond is refused, every time.
//
// The budget is keyed per PROMPT, so a new user turn resets it with no cleanup step; a TTL sweep
// drops the directories a long-lived tree accumulates. The count does NOT distinguish a verifier
// from any other agent, because keying on "is this a verify agent" needs a session-to-build binding
// no payload field provides — and the concurrency rule binds every fan-out to the same number
// anyway, so a uniform cap needs no such binding.
const AGENT_TTL_MS = 12 * 60 * 60 * 1000
// A SLOT expires too, and that is a different clock from the turn-directory sweep above.
//
// WHY IT HAS TO. A slot is claimed with O_EXCL and there is no release path, because PreToolUse is
// the only event this hook is wired for and it fires BEFORE the work, never after. So the count is
// LIFETIME-PER-PROMPT, not concurrency: five agents that ran one after another, each finishing
// before the next began, exhaust the budget for the rest of the turn. Measured on node `a` — six
// sequential spawns in one prompt, distinct tool_use_ids, the sixth denied with every slot long
// since idle. The protocol's own words are "at most 5 run concurrently"; without an expiry this
// mechanism could not measure that, and a permanent budget is not the rule it is named after.
//
// WHY 45 MINUTES, and why erring long. The failure this whole rule exists to prevent is a BURST —
// ~40 agents at once, a tripped server rate limiter, ~3.65 M subagent tokens for nothing. A burst
// claims its slots within a second of each other, so no expiry short of absurd lets one through:
// the TTL is irrelevant to the case that matters. What the TTL trades is the opposite direction —
// if five agents genuinely run CONCURRENTLY for longer than the TTL, a sixth is admitted. So the
// value must exceed the longest realistic subagent, and it is set from measurement rather than
// taste: subagent durations observed on this fleet run 2 s to 34 min (a 999 s review lens, a
// 1 026 s engine split, a 2 029 s closing review). 45 min clears the longest by ~30%.
//
// ponytail: an expiry is a HEURISTIC standing in for a completion signal, and the ceiling is stated
// rather than buried — five long-running concurrent agents plus a sixth after 45 min is admitted.
// The precise fix is a release keyed on tool_use_id, which the harness guarantees to be the SAME id
// in PreToolUse and PostToolUse for one tool execution. It is NOT built here because it turns on one
// unmeasured fact: whether the `Agent` tool fires PostToolUse at all. The public hooks reference says
// Agent skips both tool events in favour of SubagentStart/Stop, and SubagentStop carries no
// tool_use_id to correlate on — while this repo's own protocol records, from measurement, that
// PreToolUse DOES fire for Agent — re-confirmed here by watching a real spawn claim a slot. Both
// cannot be right, and wiring a release for an event that never arrives would ship exactly the
// mechanism-that-cannot-fire this repo gates against. Settle it with a PostToolUse[Agent] probe plus
// a PostToolUse[Bash] CONTROL, in a FRESH session: settings are not hot-reloaded, which is why it
// could not be settled where it was found. Then the TTL demotes to the crash/interrupt backstop the
// hooks reference recommends and stops being the primary mechanism.
const SLOT_TTL_MS = 45 * 60 * 1000
const slug = (s) => String(s).replace(/[^A-Za-z0-9_-]/g, '_').slice(0, 120)

// The git COMMON dir, resolved without shelling out to git — this runs on every spawn.
function gitCommonDir(start) {
  const fs = require('fs')
  const path = require('path')
  let dir = path.resolve(start)
  for (let i = 0; i < 64; i++) {
    const g = path.join(dir, '.git')
    let st = null
    try { st = fs.statSync(g) } catch { st = null }
    if (st) {
      if (st.isDirectory()) return g
      // A WORKTREE: `.git` is a FILE holding `gitdir: <path>`, and that gitdir names the shared
      // common dir in its own `commondir`. One budget per repo, not per worktree — a session is a
      // session whichever checkout it stands in.
      try {
        const m = /gitdir:\s*(.+)/.exec(fs.readFileSync(g, 'utf8'))
        if (!m) return null
        const gd = path.resolve(dir, m[1].trim())
        try {
          return path.resolve(gd, fs.readFileSync(path.join(gd, 'commondir'), 'utf8').trim())
        } catch {
          return gd
        }
      } catch {
        return null
      }
    }
    const up = path.dirname(dir)
    if (up === dir) return null
    dir = up
  }
  return null
}

function sweepTurns(root, keep) {
  const fs = require('fs')
  const path = require('path')
  let names
  try { names = fs.readdirSync(root) } catch { return }
  const now = Date.now()
  for (const n of names) {
    const p = path.join(root, n)
    if (p === keep) continue
    // Never fatal: a concurrent hook process may be sweeping the same entry, and losing that race is
    // not a reason to refuse a spawn.
    try {
      if (now - fs.statSync(p).mtimeMs < AGENT_TTL_MS) continue
      fs.rmSync(p, { recursive: true, force: true })
    } catch { /* ignore */ }
  }
}

// null = allow · string = the deny message.
function guardAgentSpawn(data) {
  const fs = require('fs')
  const path = require('path')
  const { session_id: sid, prompt_id: pid, tool_use_id: uid } = data
  // FAIL OPEN, SILENTLY, when the budget cannot be KEYED or its directory cannot be resolved. The
  // split is stated rather than blurred: a hook that denies every spawn on a filesystem hiccup is
  // worse than the burst it prevents. A token that cannot be CREATED is a different fact and denies.
  if (!sid || !pid || !uid) return null
  const common = gitCommonDir(data.cwd || process.cwd())
  if (!common) return null
  const root = path.join(common, 'agent-cap')
  const turn = path.join(root, `${slug(sid)}__${slug(pid)}`)
  try { fs.mkdirSync(turn, { recursive: true }) } catch { return null }
  sweepTurns(root, turn)

  // IDEMPOTENT PER tool_use_id. A hook re-invoked for the same call must not spend a second slot.
  for (let n = 1; n <= MAX_VERIFIERS; n++) {
    let held
    try { held = fs.readFileSync(path.join(turn, `slot-${n}`), 'utf8') } catch { continue }
    if (held.trim() === uid) return null
  }

  for (let n = 1; n <= MAX_VERIFIERS; n++) {
    const slot = path.join(turn, `slot-${n}`)
    let fd
    try {
      fd = fs.openSync(slot, 'wx') // O_CREAT|O_EXCL — the atomic decision
    } catch (e) {
      // An EXPIRED slot is a free slot: unlink it and re-claim through the SAME O_EXCL create, so
      // two hooks racing on one stale slot still resolve in the create — the only place that
      // decides. A failed unlink (the other racer got there first) is not an error, and a failed
      // re-create means that racer won the slot, so this one moves to the next ordinal rather than
      // retrying. Nothing here ever overwrites a live claim: the age test gates the unlink, and the
      // create is still exclusive.
      if (e.code === 'EEXIST') {
        let age = 0
        try { age = Date.now() - fs.statSync(slot).mtimeMs } catch { age = 0 }
        if (age > SLOT_TTL_MS) {
          try { fs.unlinkSync(slot) } catch { /* another racer won it; the retry sees the truth */ }
          try {
            fd = fs.openSync(slot, 'wx')
          } catch { continue }
          try { fs.writeSync(fd, uid) } finally { try { fs.closeSync(fd) } catch { /* ignore */ } }
          return null
        }
        continue
      }
      return (
        `BLOCKED by agent-cap: this spawn's token could not be created in ${turn} ` +
        `(${e.code || e.message}), so the ${MAX_VERIFIERS}-agent budget could not be enforced for ` +
        `it. A spawn this hook cannot count is not a spawn it may approve.`
      )
    }
    try { fs.writeSync(fd, uid) } finally { try { fs.closeSync(fd) } catch { /* ignore */ } }
    return null
  }

  return (
    `BLOCKED by agent-cap: the direct-Agent spawn budget for this prompt is exhausted — ` +
    `${MAX_VERIFIERS} of ${MAX_VERIFIERS} claimed in this turn within the last ` +
    `${Math.round(SLOT_TTL_MS / 60000)} minutes. A review's verify stage spawns at most ` +
    `${MAX_VERIFIERS} agents TOTAL and the charter binds every other fan-out to the same number ` +
    `(memory/guides/REVIEW-PROTOCOL.md).\n\n` +
    `Consolidate instead of spawning again: batch the work so the BATCH SIZE grows with the item ` +
    `count and the agent count does not. For a review, tools/workflows/tier2-review.js already does ` +
    `it. A new user prompt resets the budget, and a slot idle longer than ` +
    `${Math.round(SLOT_TTL_MS / 60000)} minutes is reclaimed on the next spawn; nothing needs ` +
    `cleaning up either way.\n`
  )
}

// TOOL-dTieredTribunal-14 S1 - RULE 5, the ref-keyed verdict join. Ported from the awk in
// tools/workflows/check-review-join.sh, which is a FILE gate and therefore blind to the modality
// where this defect actually happens: an ad-hoc review harness is an inline `script` string on a
// Workflow tool call and is never a file. That gate covered four already-compliant committed
// harnesses and none of the observed failures. The three `why` strings are FROZEN at the bytes that
// gate's self-test asserts - those arms are this port's regression suite, and an unedited arm
// proving an unchanged verdict is worth more than a prettier string.
//
// S2 - the view is `renderBlankedLiterals`, the one this file already defines, rather than a second
// character scanner. That is a deliberate NARROWING: the awk kept string CONTENTS and only stripped
// comments, so it matched the retired identifier inside a string. Two fixtures in the self-test pin
// the difference in both directions. A regex LITERAL survives the blanking, which is why the gate
// excludes this file from its own population - the ban table below would otherwise match itself.
function scanJoinFindings(script) {
  const raws = script.split(/\r?\n/)
  // TOOL-aWeldedTribunal-3 — the SAME fallback rule 3 takes, for the same reason and over the same
  // view. Giving rule 3 the fallback and not this one would be the gate-the-class-not-the-instance
  // failure one level up: both read `renderBlankedLiterals` through the same dispatcher and both
  // went blind below an unterminated literal. The per-line view preserves S2's narrowing WITHIN each
  // line, which `renderStrippedView` would not — it leaves backticks alone.
  const view = renderBlankedLiterals(script)
  const code = view.unterminated ? renderPerLineBlanked(script) : view.code
  const out = []
  // S3 - one ban table, tested against every view of the line. It was three inline conditions per
  // view until the M8 closing review found the second view missing; duplicating them per view would
  // have been two answers to one question, which is the class this build spent a unit on.
  const BANS = [
    [/\[[A-Za-z_$][A-Za-z0-9_$.]*\.ref\]/, "object/Map literal keyed by a .ref string"],
    [/\.(get|set|has|delete)\([A-Za-z_$][A-Za-z0-9_$.]*\.ref[),]/, "Map keyed by a .ref string"],
    [/verdictByRef/, "the retired verdictByRef identifier"],
  ]
  for (let i = 0; i < code.length; i++) {
    const l = code[i]
    const raw = raws[i] === undefined ? l : raws[i]
    // M8 closing review, HIGH: `renderBlankedLiterals` blanks template CONTENTS, so a join written inside a
    // `${...}` interpolation was invisible - a coverage regression against the awk this rule
    // replaced, which kept string contents. These harnesses render every report through template
    // literals, so that is exactly where such an expression lives. The interpolation SPANS are
    // scanned as a second view, which restores the reach without restoring the awk's false
    // positives: a mention inside a plain string stays out of scope and both fixtures still hold.
    // A nested `${}` closes the span early; that costs reach on a shape none of these harnesses
    // writes, and the outer views still carry the identifier ban.
    // ROUND 2 - this took its spans from the RAW line, so the second view reached into COMMENTS and
    // into plain quoted strings and rule 5 started firing on prose. That refuted this rule's own
    // narrowing doctrine two lines above, and check-review-join.sh's, in the same commit that wrote
    // them both down. The span view is comment-stripped and quote-blanked first: `renderStrippedView`
    // leaves backticks alone, which is the whole point - a `${…}` is only an interpolation inside a
    // template literal, and inside a '' or "" string it is three characters of text.
    const interp = renderStrippedView(raw).split('//')[0]
    const views = [l].concat(interp.match(/\$\{[^}]*\}/g) || [])
    let why = null
    for (const b of BANS) {
      if (views.some((v) => b[0].test(v))) { why = b[1]; break }
    }
    if (why) out.push({ n: i + 1, line: raw, why })
  }
  return out
}

function main() {
  // TOOL-dTieredTribunal-14 S4 - a rule selector over a CLOSED set, so a second entry point can ask
  // for ONE rule. Absent runs every rule, which is the wiring's invocation and is unchanged.
  // Anything outside the set REFUSES rather than silently matching nothing, which would be this
  // repo's vacuous-selector-empty-population class arriving in the file whose job is to refuse what
  // it cannot resolve. A WIRED command must never carry it: tools/check-wiring.sh asserts that,
  // because `--only=join` in settings.json would turn the three cap rules off with no diff.
  const ONLY_RULES = ["join"]
  const onlyArg = process.argv.slice(2).find((a) => a.startsWith("--only="))
  const ONLY = onlyArg === undefined ? null : onlyArg.slice("--only=".length)
  if (ONLY !== null && ONLY_RULES.indexOf(ONLY) === -1) {
    process.stderr.write(
      "agent-cap: --only=" + ONLY + " names no rule this hook has. The closed set is: " +
        ONLY_RULES.join(", ") + ". Omit the flag to run every rule.\n",
    )
    process.exit(2)
  }

  let data
  try {
    data = JSON.parse(readStdin())
  } catch {
    process.exit(0)
  }
  if (!data || (data.tool_name !== 'Workflow' && data.tool_name !== 'Agent')) process.exit(0)

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
        `change it in tools/hooks/agent-cap.js, the source of truth -- .claude/hooks/agent-cap.js is a mirror the bar reverts.\n`,
    )
    process.exit(2)
  }

  // RULE 4 first for an `Agent` payload, and it is the ONLY thing that path runs: the rules below
  // all read a script, and an Agent spawn carries none.
  if (data.tool_name === 'Agent') {
    const deny = guardAgentSpawn(data)
    if (!deny) process.exit(0)
    process.stderr.write(deny)
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

  const fan = ONLY === null ? runBothViews(fanoutFindings, script) : []
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
  const caps = ONLY === null ? runBothViews(capFindings, script) : []
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

  // TOOL-dTieredTribunal-14 S3 - INVERTED. This block alone was written as an early exit-0, so any
  // rule appended after it never ran for a script carrying no raw parallel()/pipeline() - which is
  // every script the join ban exists to judge. The two rules above already use this additive shape.
  // Order is unchanged and still decides which message an operator sees: the three rules above all
  // prevent a BURST, the expensive failure this hook exists for, while a ref-keyed join is a wrong
  // verdict, which is cheap to re-run.
  const bad = ONLY === null ? runBothViews(offendingLines, script) : []
  if (bad.length) {
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

  // RULE 5 - the ref-keyed verdict join. LAST because it is the cheapest failure to recover from.
  const joins = runBothViews(scanJoinFindings, script)
  if (joins.length) {
    process.stderr.write(
      `BLOCKED by agent-cap: a ref-keyed verdict join. A review harness that joins each finding to ` +
        `its skeptic verdict on a \`file:line\` STRING loses findings to echo drift and COLLAPSES two ` +
        `findings at one location, so both inherit whichever verdict landed last. The class has no ` +
        `runtime signal - a mis-keyed harness reports a clean bill.\n\n` +
        joins.slice(0, 6).map(({ n, line, why }) => `  L${n}: ${String(line).trim()}\n        ${why}`).join('\n') +
        `\n\nKey the join on the integer id the orchestrator assigns, never on a string the skeptic ` +
        `reproduces. Ready-made: tools/workflows/tier2-review.js.\n`,
    )
    process.exit(2)
  }

  process.exit(0)
}

main()
