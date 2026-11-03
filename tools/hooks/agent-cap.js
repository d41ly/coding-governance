#!/usr/bin/env node
/**
 * agent-cap — project-agnostic PreToolUse guard on the `Workflow` and `Agent` tool calls.
 *
 * THE AGENT LIMIT IS NOT THIS FILE'S (TOOL-dGroundRules-10). How many agents run at once is the policy
 * key `runtime.agents-in-flight`, which the policy kit renders into the harness's own two concurrency
 * settings in `.claude/settings.json` (`policy.py settings --write`). The harness counts agents in
 * flight and knows when each one ends, which a PreToolUse hook cannot. What a call-time check CAN see
 * is the settings files the harness started from, and RULE 7 holds them to the landed limit.
 *
 * THE RULES IT KEEPS, in the order `main()` runs them: rule 6, then rule 7, then the call is admitted.
 * Rules 0, 2 and 5 left for the review kit (TOOL-dFairHearing-16, the owner's NT-27): the verify-stage
 * total and the loop markers are its `check-verifier-fanout.js`, the ref-keyed verdict join ban its
 * `check-review-join.js`, both run by the merge bar's gates beside them over every committed harness,
 * and the spec-audit opt-in its `spec-audit-optin.js`, a PreToolUse hook on `Workflow` calls. They
 * read this file's views, constants and readers through its exports; requiring it runs no rule. Every
 * `--only=` argument is refused, naming the two script homes.
 *
 * RULE 6 (TOOL-aOrientedCast-7) — every agent prompt is a rendered handoff. Armed by
 * `.claude/roles.json` at the checkout root of the payload `cwd`, else of `CLAUDE_PROJECT_DIR`
 * (TOOL-aOrientedCast-14; neither resolving adds no rule, with one stderr line when
 * `CLAUDE_PROJECT_DIR` is set), read through the sibling hook's `resolveRoleRoot` and `loadRoleIndex`:
 * absent adds no rule; broken refuses both tools; no `agent`-true role refuses every `Agent` call, and
 * an empty `harnesses` list every `Workflow` call, as UNARMED. An `Agent` call is admitted only when
 * its `subagent_type` is an `agent`-true role and its `prompt` is, line endings folded and its ends
 * trimmed, exactly one `gov:handoff` marker line naming that role, blank lines, and the `## Task`
 * section of the file the marker's `path` names under `builds/<build>/prompts/`, that file holding the
 * same single marker and a section whose SHA-256 prefix is the marker's `task-sha`, and its
 * `description`, ends trimmed, the name the renderer prints on stderr: `<build> · <unit> · <workflow>`
 * from the marker and the index's `workflow` for that role, the unit part left out for a `-` unit
 * (TOOL-aOrientedCast-27). That step stops a stale or freeform name, never a forged one. A `Workflow`
 * call is admitted only by a `scriptPath` listed in `harnesses`, with `args.roles` a non-empty object
 * whose every value is an `agent`-true role. A throw inside it refuses.
 * CEILING, said rather than implied: it stops forgetting, not evasion. A hook-less or `--bare` run,
 * the agents a running harness spawns through its own `agent()`, a session-to-session message, a
 * self-consistent hand-written prompt file and a hand-edited index all pass it, and it never compares
 * `role-sha` with the role an agent type was rendered from.
 *
 * RULE 7 (TOOL-dGroundRules-10) — the settings in force. With the policy kit's `policy-mirror.js` in
 * the `policy` kit beside this hooks kit, every `Agent` and `Workflow` call reads the landed limit
 * through `readPolicy`, then every settings layer `readSettingsLayers` reads at the payload `cwd`'s
 * checkout root, and refuses when no layer sets a harness variable, or any layer that sets one holds
 * a value that is not a positive integer, or is above the limit (TOOL-dGroundRules-61). No policy kit beside this one adds
 * no rule; a `cwd` in no checkout refuses, naming it (TOOL-dGroundRules-21 S38). A throw inside it refuses.
 *
 * Wiring (per project): run `python <prefix>/settings-merge.py` (idempotent) — it merges the block
 * below into .claude/settings.json; or merge it by hand:
 *   "hooks": { "PreToolUse": [ { "matcher": "Workflow|Agent",
 *     "hooks": [ { "type": "command",
 *       "command": "node \"${CLAUDE_PROJECT_DIR}/<path>/agent-cap.js\"" } ] } ] }
 * The matcher is a LIST OF EXACT STRINGS separated by `|`, in ONE group — not a regular expression.
 * `Workflow` is a harness call rules 6 and 7 judge; `Agent` is a direct spawn they judge too.
 * main() exits 0 on any other tool_name.
 * Blocks via exit 2 + stderr (version-robust; no JSON-schema dependency).
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

const KIT_AGENT_CAP_VERSION = '1.42' // gov:kit agent-cap@1.42 — engine identity (this file is deployed verbatim; the constant is the deployer's version marker)

// The review harness a deny message points at, DERIVED (TOOL-aRepatriatedFork-2 S6): probed in the
// workflows kit beside this hook's own directory, and the bare name when that probe misses, because
// a path spelled at gov's prefix sends an adopter's reader to a file that is not there.
function resolveHarnessName() {
  const path = require('path')
  const p = path.join(path.dirname(__dirname), 'workflows', 'tier2-review.js')
  if (!require('fs').existsSync(p)) return 'tier2-review.js'
  return path.relative(process.env.CLAUDE_PROJECT_DIR || process.cwd(), p).split(path.sep).join('/')
}

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

// THE VERIFY TOTAL. Since TOOL-dFairHearing-16 no rule of this file reads it: rule 2, the verify-stage
// total, is the review kit's `check-verifier-fanout.js`, which reads it through this file's exports,
// and `check-playbook-parity.sh` reads it by source line. It stays here, with the views, until
// dBoundRoles retires this hook and moves it. The lens allowance that sat beside it left with its last
// reader (TOOL-dFairHearing-27 S16): its one home is `LENS_SLOTS` in `check-verifier-fanout.js`.
const MAX_VERIFIERS = 5
// TOOL-dGroundRules-10 F2 — a VERIFIER split's comparand is MAX_VERIFIERS, the verify total. TOOL-dGroundRules-18 — a WRITER
// split's is the agent limit (receiver (a)), read through rule 7's `readPolicy` once, only for a script carrying the marker.
const POLICY_HELPER = require('path').join(require('path').dirname(__dirname), 'policy', 'policy-mirror.js')
function readWriterBound(repo) {
  if (!require('fs').existsSync(POLICY_HELPER)) return { n: MAX_VERIFIERS, key: 'MAX_VERIFIERS, as no policy kit sits beside this hooks kit' }
  let v
  try { v = require(POLICY_HELPER).readPolicy('runtime.agents-in-flight', { repo }).value } catch (e) { return { why: `the agent limit could not be read: ${(e && e.message) || e}` } }
  return Number.isInteger(v) && v > 0 ? { n: v, key: 'runtime.agents-in-flight' } : { why: `runtime.agents-in-flight reads ${JSON.stringify(v)}, not a positive integer` }
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


// The CHECKOUT root: the nearest directory holding `.git`, a directory in a primary tree and a FILE
// in a linked worktree. Resolved without shelling out to git — this runs on every call.
function resolveCheckoutRoot(start) {
  const fs = require('fs')
  const path = require('path')
  let dir = path.resolve(start)
  for (let i = 0; i < 64; i++) {
    try {
      fs.statSync(path.join(dir, '.git'))
      return dir
    } catch { /* not here; keep walking */ }
    const up = path.dirname(dir)
    if (up === dir) return null
    dir = up
  }
  return null
}


// The `builds/<slug>` a repo-relative path sits under, or null: no `builds` segment, any `..`
// segment, or a spelling that is not repo-relative at all — absolute (`/…`, `X:…`) or `~`-rooted
// (round 2, R1). A direct spec-audit subject is repo-relative by the harness's own contract, and a
// slug walk over an absolute path answers the SLUG axis while a second checkout with the same slug
// sits on the ROOT axis it never asked about. One walk for every subject so containment cannot be
// tested one way (closing review F2).
function extractBuildSlug(p) {
  const q = String(p).replace(/\\/g, '/')
  if (q.startsWith('~') || /^([A-Za-z]:|\/)/.test(q)) return null
  const parts = q.split('/')
  if (parts.indexOf('..') !== -1) return null
  const i = parts.indexOf('builds')
  return i === -1 || !parts[i + 1] ? null : parts[i + 1]
}


// A Workflow call's structured `args`, parsed ONCE for rules 0 and 6: a JSON string is parsed, and
// anything that is not then a plain object — a string that does not parse included — is null. Rule 0
// admits on null, as it always has; rule 6 refuses on it.
function extractWorkflowArgs(data) {
  let a = data && data.tool_input && data.tool_input.args
  if (typeof a === 'string') {
    try { a = JSON.parse(a) } catch { return null }
  }
  return a && typeof a === 'object' && !Array.isArray(a) ? a : null
}

// RULE 6 (TOOL-aOrientedCast-7) — every agent prompt is a rendered handoff. The marker line is the
// roles kit's interface, read here and never written; the renderer is named by its bare file name in
// every message, because a kit file names no sibling kit by literal.
const HANDOFF_MARK = 'gov:handoff'
const HANDOFF_MARK_RE = /^<!-- gov:handoff role=(\S+) build=(\S+) unit=(\S+) path=(\S+) role-sha=([0-9a-f]{12}) task-sha=([0-9a-f]{12}) -->$/

// Every line of `text`, carriage returns stripped, that is a whole marker line with its six fields in
// order: `{ line, role, build, unit, path, taskSha }` each.
function extractHandoffMarker(text) {
  const out = []
  for (const raw of String(text).split('\n')) {
    const line = raw.replace(/\r/g, '')
    const m = HANDOFF_MARK_RE.exec(line)
    if (m) out.push({ line, role: m[1], build: m[2], unit: m[3], path: m[4], taskSha: m[6] })
  }
  return out
}

// The `## Task` section: from the first line that is exactly `## Task` to the end of the text, CRLF
// folded to LF, or null. The renderer's span (`handoff.py`'s `check` hashes the same bytes). Walked
// by line, not by a multiline `$`, which in JS also matches before a lone CR and in Python does not.
function extractTaskSection(text) {
  const t = String(text).replace(/\r\n/g, '\n')
  let at = 0
  for (const line of t.split('\n')) {
    if (line === '## Task') return t.slice(at)
    at += line.length + 1
  }
  return null
}

// The first twelve lowercase hex digits of the SHA-256 of a section's UTF-8 bytes.
function buildTaskDigest(section) {
  return require('crypto').createHash('sha256').update(String(section), 'utf8').digest('hex').slice(0, 12)
}

// The refusal: the rule, the tool, the reason, and the route that passes.
function renderHandoffDeny(tool, why, index) {
  const roles = index && index.roles ? Object.keys(index.roles).filter((n) => index.roles[n].agent === true).sort() : []
  const route = tool === 'Agent'
    ? `The agent-true roles are: ${roles.join(', ') || '(none)'}. Render the handoff with ` +
      `\`handoff.py render --role <name> --build <slug> --part task\`, then pass its output unchanged as ` +
      `\`prompt\` with \`subagent_type\` that role and \`description\` the name it prints on stderr.`
    : `The declared harnesses are: ${(index && index.harnesses ? index.harnesses : []).join(', ') || '(none)'}. ` +
      `Run one by \`scriptPath\` and pass, in \`args\`, the \`roles\` object \`handoff.py harness-args <harness>\` prints.`
  return `BLOCKED by agent-cap: rule 6 (TOOL-aOrientedCast-7) refused this ${tool} call — ${why}\n${route}\n`
}

// Rule 6 on an `Agent` call (§4 "The evaluation order", step 2): null to admit, else a deny string.
function checkHandoffSpawn(data, index, root) {
  const fs = require('fs')
  const path = require('path')
  const ti = data.tool_input || {}
  const roles = Object.keys(index.roles).filter((n) => index.roles[n].agent === true)
  if (!roles.length) return renderHandoffDeny('Agent', `UNARMED: ${index.shown} declares no agent-true role, so no spawn can be admitted.`, index)
  const type = ti.subagent_type
  if (typeof type !== 'string' || !Object.prototype.hasOwnProperty.call(index.roles, type) || index.roles[type].agent !== true) {
    const research = roles.filter((n) => index.roles[n].workflow === 'research').sort()
    return renderHandoffDeny('Agent', `subagent_type ${JSON.stringify(type === undefined ? null : type)} is not an agent-true role of ${index.shown}; ` +
      `a built-in agent type is never admitted${research.length ? `, and research or mapping runs as the ${research.join(' or ')} role` : ''}.`, index)
  }
  if (typeof ti.prompt !== 'string') return renderHandoffDeny('Agent', 'the call carries no `prompt` string.', index)
  const marks = extractHandoffMarker(ti.prompt)
  if (marks.length !== 1) return renderHandoffDeny('Agent', `the prompt carries ${marks.length} ${HANDOFF_MARK} marker lines; exactly one is required.`, index)
  const m = marks[0]
  if (m.role !== type) return renderHandoffDeny('Agent', `the marker's role ${m.role} is not the subagent_type ${type}.`, index)
  const parts = m.path.replace(/\\/g, '/').split('/')
  const at = parts.indexOf('builds')
  if (extractBuildSlug(m.path) !== m.build || parts[at + 2] !== 'prompts' || parts.length < at + 4 || parts.slice(at + 3).some((s) => s === '' || s === '.')) {
    return renderHandoffDeny('Agent', `the marker's path ${m.path} is not a repo-relative file under builds/${m.build}/prompts/ with no \`..\` segment.`, index)
  }
  const file = path.join(root, ...parts)
  let st = null
  try { st = fs.statSync(file) } catch { st = null }
  if (!st || !st.isFile()) return renderHandoffDeny('Agent', `the marker's path ${m.path} names no file under ${root.split(path.sep).join('/')}.`, index)
  const text = fs.readFileSync(file, 'utf8')
  const fileMarks = extractHandoffMarker(text)
  if (fileMarks.length !== 1 || fileMarks[0].line !== m.line) {
    return renderHandoffDeny('Agent', `${m.path} does not hold exactly one marker line byte-equal to the prompt's (it holds ${fileMarks.length}).`, index)
  }
  const section = extractTaskSection(text)
  if (section === null) return renderHandoffDeny('Agent', `${m.path} holds no \`## Task\` line.`, index)
  // F4 (a): the whole prompt is the marker, blank lines and the section — line endings folded, the two
  // ends trimmed, and each line's trailing whitespace aside. Anything else is a freeform prompt.
  const got = ti.prompt.replace(/\r\n/g, '\n').trim().split('\n').map((l) => l.trimEnd())
  const want = section.replace(/\s+$/, '').split('\n').map((l) => l.trimEnd())
  let k = 1
  while (k < got.length && got[k] === '') k++
  if (got[0] !== m.line) return renderHandoffDeny('Agent', `prompt line 1 is not the marker line; it reads ${JSON.stringify(got[0].slice(0, 120))}.`, index)
  for (let j = 0; j <= want.length; j++) {
    const g = got[k + j]
    if (j === want.length ? g === undefined : g === want[j]) continue
    return renderHandoffDeny('Agent', `prompt line ${k + j + 1} differs from ${m.path}'s \`## Task\` section: the prompt reads ` +
      `${JSON.stringify(g === undefined ? '(end)' : g.slice(0, 120))}, the file ${JSON.stringify(j === want.length ? '(end)' : want[j].slice(0, 120))}. Resend the file's bytes.`, index)
  }
  const digest = buildTaskDigest(section)
  if (digest !== m.taskSha) return renderHandoffDeny('Agent', `${m.path}'s \`## Task\` section hashes to ${digest}, and its marker says task-sha=${m.taskSha}: the file was edited after rendering.`, index)
  // TOOL-aOrientedCast-27 step 2.10 - after the digest, so the one remedy left is the description.
  const workflow = index.roles[type].workflow
  if (typeof workflow !== 'string' || workflow === '') {
    return renderHandoffDeny('Agent', `${index.shown} declares no workflow for ${type}, so this spawn's name cannot be derived; re-render the role index.`, index)
  }
  const spawnName = renderSpawnName(m, workflow)
  if (typeof ti.description !== 'string' || ti.description.trim() !== spawnName) {
    return renderHandoffDeny('Agent', `the call's description ${JSON.stringify(ti.description === undefined ? null : ti.description)} is not this handoff's name ` +
      `${JSON.stringify(spawnName)}: the marker's build and unit and the ${type} role's workflow. Pass description exactly as handoff.py render prints it.`, index)
  }
  return null
}

// A direct spawn's name, `<build> · <unit> · <workflow>`, the unit part left out when the marker's is
// `-`. The renderer's `render_spawn_name` builds the same string; a kit file imports no sibling kit.
function renderSpawnName(marker, workflow) {
  return [marker.build, marker.unit === '-' ? '' : marker.unit, workflow].filter(Boolean).join(' · ')
}

// Rule 6 on a `Workflow` call (§4 "The evaluation order", step 3): null to admit, else a deny string.
function checkHarnessCall(data, index, root) {
  const fs = require('fs')
  const path = require('path')
  const { buildComparablePath } = require(path.join(__dirname, 'scratch-guard.js'))
  const ti = data.tool_input || {}
  if (!index.harnesses.length) return renderHandoffDeny('Workflow', `UNARMED: ${index.shown} declares no harness, so no Workflow call can be admitted.`, index)
  if (ti.script) return renderHandoffDeny('Workflow', 'an inline `script` is never a declared harness.', index)
  const sp = ti.scriptPath
  if (typeof sp !== 'string' || sp === '') return renderHandoffDeny('Workflow', 'the call names no `scriptPath` (a `name:` run is not a declared harness).', index)
  const folded = process.platform === 'win32' ? sp.replace(/\\/g, '/').replace(/^\/([A-Za-z])\//, '$1:/') : sp
  const abs = path.resolve(data.cwd || process.cwd(), folded)
  let real = abs
  try { real = fs.realpathSync(abs) } catch { real = abs }
  let top = root
  try { top = fs.realpathSync(root) } catch { top = root }
  const rel = buildComparablePath(path.relative(top, real)).replace(/^\.\//, '')
  if (!index.harnesses.some((h) => buildComparablePath(h).replace(/^\.\//, '') === rel)) {
    return renderHandoffDeny('Workflow', `scriptPath ${sp} (${rel} from the checkout root) is not a declared harness.`, index)
  }
  const a = extractWorkflowArgs(data)
  if (!a) return renderHandoffDeny('Workflow', '`args` is not a plain object, or a JSON string of one.', index)
  const r = a.roles
  if (!r || typeof r !== 'object' || Array.isArray(r) || !Object.keys(r).length) {
    return renderHandoffDeny('Workflow', '`args.roles` is absent, not a plain object, or empty; take it from `handoff.py harness-args <harness>`.', index)
  }
  for (const [key, v] of Object.entries(r)) {
    if (typeof v !== 'string' || !Object.prototype.hasOwnProperty.call(index.roles, v) || index.roles[v].agent !== true) {
      return renderHandoffDeny('Workflow', `\`args.roles.${key}\` is ${JSON.stringify(v)}, not an agent-true role of ${index.shown}.`, index)
    }
  }
  return null
}

// RULE 7 (TOOL-dGroundRules-10) — the settings in force. The agent limit is the harness's to enforce,
// through the two variables the policy kit renders into `.claude/settings.json`; the harness reads
// them from the working tree, so a hand-raised `env`, or a render left behind a lowering, would run
// past the landed limit. This rule refuses that at the next call. It reads the landed limit through
// the policy kit's `readPolicy`, located beside this hooks kit as `resolveHarnessName` probes the
// workflows kit, and never the working-tree mirror; a hooks kit with no `policy` kit beside it adds no
// rule. WHAT IT DOES NOT SEE: an environment override of the two variables, which the harness applies
// and no hook can read. UNVERIFIED: that a session started before a lowering keeps its settings until
// it restarts. Read: every layer readSettingsLayers returns (TOOL-dGroundRules-61 S1); a cwd in no checkout, or a throw at any step, refuses, naming it (TOOL-dGroundRules-21 S38). A refused policy read is no settings fault, so it denies under its own text, printing the reader's line and never the settings remedy (TOOL-dGroundRules-73). null = allow · string = deny.
const SETTINGS_VARS = ['CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS', 'CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS']

function checkSettingsInForce(data) {
  const fs = require('fs')
  const path = require('path')
  const helper = POLICY_HELPER
  if (!fs.existsSync(helper)) return null
  const root = resolveCheckoutRoot(data.cwd || process.cwd())
  if (!root) return `BLOCKED by agent-cap: rule 7 (TOOL-dGroundRules-10) refused this ${data.tool_name} call — the payload cwd ${String(data.cwd || process.cwd()).split(path.sep).join('/')} is in no git checkout, so the settings in force and the landed agent limit cannot be read, and a rule that cannot read does not admit.\n`
  const rel = path.relative(root, path.dirname(helper)).split(path.sep).join('/')  // the render's kit path: a hook names no prefix
  const remedy = `python ${rel ? rel + '/' : ''}policy.py settings --write`
  const renderSettingsDeny = (why) =>
    `BLOCKED by agent-cap: rule 7 (TOOL-dGroundRules-10) refused this ${data.tool_name} call — the ` +
    `settings this checkout's harness starts from do not hold the landed agent limit.\n${why}\n` +
    `Render them from the policy: ${remedy}, run at ${root.split(path.sep).join('/')}. A session started ` +
    `before the render keeps the settings it started with until it restarts (UNVERIFIED).\n`
  const renderReadDeny = (why) =>
    `BLOCKED by agent-cap: rule 7 (TOOL-dGroundRules-10) refused this ${data.tool_name} call — the ` +
    `landed agent limit cannot be read, so the settings in force were not compared, and a rule that ` +
    `cannot read does not admit. Clear the policy reader's refusal, which names its cause:\n${why}\n`
  checkSettingsInForce.step = `reading the landed limit through ${helper.split(path.sep).join('/')}` // main names the step a throw left
  const { readPolicy, PolicyRefusal } = require(helper)
  let limit
  try {
    limit = readPolicy('runtime.agents-in-flight', { repo: root }).value
  } catch (e) {
    if (PolicyRefusal && e instanceof PolicyRefusal) return renderReadDeny(`  ${e.message}`)
    throw e
  }
  if (!Number.isInteger(limit) || limit < 1) return renderSettingsDeny(`  runtime.agents-in-flight reads ${JSON.stringify(limit)}, not a positive integer.`)
  // TOOL-dGroundRules-61 S2: the value the harness applies is one of the values its layers set, and the
  // declared file's place in its precedence is declared nowhere, so EVERY read layer that sets a
  // variable is bounded (§8 F1 (b)): a declared file never hides the project's, nor the project the
  // declared one. Unread, so unbounded here: the --settings flag layer, the managed-policy layer and an
  // exported variable (F2). A shadowed lower layer above the limit refuses too, naming its remedy.
  const layers = readSettingsLayers(root)
  const bad = []
  for (const v of SETTINGS_VARS) {
    const set = layers.filter((l) => Object.prototype.hasOwnProperty.call(l.env, v))
    if (!set.length) {
      bad.push(`  .claude/settings.json: env.${v} is absent, and runtime.agents-in-flight is ${limit} (layers read: ${layers.map((l) => l.name).join(', ')}).`)
      continue
    }
    for (const { name, env } of set) { // highest precedence first: the first violating layer is named
      const got = env[v]
      const s = typeof got === 'number' ? String(got) : got
      const why = typeof s !== 'string' || !/^[1-9][0-9]*$/.test(s)
        ? `is ${JSON.stringify(got)}, not a positive integer; runtime.agents-in-flight is ${limit}.`
        : Number(s) > limit ? `is ${s}, above runtime.agents-in-flight ${limit}.` : ''
      if (why) { bad.push(`  ${name}: env.${v} ${why}`); break }
    }
  }
  return bad.length ? renderSettingsDeny(bad.join('\n')) : null
}

function main() {
  // TOOL-dFairHearing-16 F7 — THE SELECTOR LEFT WITH ITS RULES. `--only=join` ran rule 5 and
  // `--only=scripts` rules 2 and 5 (TOOL-dTieredTribunal-14 S4, TOOL-aOrientedCast-7 S11), and both
  // rules now live in the review kit, so a selector kept here would read a script and run no rule: a
  // call that can never go red, the vacuous-selector class the set was built to refuse. So EVERY
  // argument opening `--only=` is refused, before stdin is read, naming where the script rules run. A
  // review gate older than this hook then reds by name, where ignoring the flag would pass every
  // harness with rule 2 run nowhere. A WIRED command never carries it: <prefix>/check-wiring.sh asserts that.
  const onlyArg = process.argv.slice(2).find((a) => a.startsWith('--only='))
  if (onlyArg !== undefined) {
    process.stderr.write(
      `agent-cap: ${onlyArg} is refused — this hook runs no script rule since TOOL-dFairHearing-16. ` +
        `The verifier total and the loop markers run from the review kit's check-verifier-fanout.js, ` +
        `and the ref-keyed join ban from its check-review-join.js, each given this hook as --hook. ` +
        `Omit the flag to run this hook's rules 6 and 7.\n`,
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

  // RULE 6 (TOOL-aOrientedCast-7) — first, so a call outside a declared harness is refused whatever its
  // args. An absent `.claude/roles.json` at the role root adds no rule; a broken one, or a throw
  // anywhere in the rule, refuses: a rule that cannot finish does not admit.
  {
    let deny = null
    let index = null
    try {
      // TOOL-aOrientedCast-14: the root of the payload cwd, else of CLAUDE_PROJECT_DIR.
      const { loadRoleIndex, resolveRoleRoot } = require(require('path').join(__dirname, 'scratch-guard.js'))
      const cwd = data.cwd || process.cwd()
      const root = resolveRoleRoot(cwd, process.env)
      if (root) {
        index = loadRoleIndex(root)
        if (index.state === 'broken') deny = renderHandoffDeny(data.tool_name, `the role index ${index.shown} ${index.why}; fix or regenerate it.`, null)
        else if (index.state === 'ok') deny = data.tool_name === 'Agent' ? checkHandoffSpawn(data, index, root) : checkHarnessCall(data, index, root)
      } else if (process.env.CLAUDE_PROJECT_DIR) {
        process.stderr.write(`agent-cap: rule 6 unarmed — neither the payload cwd ${cwd} nor CLAUDE_PROJECT_DIR ${process.env.CLAUDE_PROJECT_DIR} lies in a checkout, so no role index was read\n`)
      }
    } catch (e) {
      deny = renderHandoffDeny(data.tool_name, `the rule threw (${(e && e.message) || e}), and a rule that cannot finish does not admit.`, index)
    }
    if (deny) {
      process.stderr.write(deny)
      process.exit(2)
    }
  }

  // RULE 7 (TOOL-dGroundRules-10) — the settings in force, for both tools. A throw refuses: a rule that
  // cannot finish does not admit, and a hook that exits 1 is non-blocking.
  {
    let deny = null
    try {
      deny = checkSettingsInForce(data)
    } catch (e) {
      deny = `BLOCKED by agent-cap: rule 7 (TOOL-dGroundRules-10) threw (while ${checkSettingsInForce.step || 'resolving the payload cwd'}: ${(e && e.message) || e}), and a rule that cannot finish does not admit.\n`
    }
    if (deny) {
      process.stderr.write(deny)
      process.exit(2)
    }
  }

  // Last, the spec-audit opt-in pack's presence (TOOL-dFairHearing-22), defined below main(); the opt-in itself is the pack's.
  { const deny = checkOptinPackPresent(data); if (deny) { process.stderr.write(deny); process.exit(2) } }
  process.exit(0)
}

// TOOL-dFairHearing-16 S1 — THE SHARED READERS, exported to the homes that left with this file's
// rules: rule 2's `check-verifier-fanout.js` and rule 5's `check-review-join.js` read the views,
// `runBothViews`, the harness name and the verify total, rule 2 the writer bound too, and the review
// kit's spec-audit opt-in pack the args reader and the slug walk, which rule 6 here also calls. ONE
// copy each: a view reads the mode `runBothViews` switches, so the views and it stay one module.
// `main()` runs only when this file is the entry point, the idiom scratch-guard.js uses, so requiring
// it judges nothing. dBoundRoles retires this hook and moves these to their last home.
module.exports = {
  MAX_VERIFIERS, readWriterBound, runBothViews, renderCodeView, renderStrippedView,
  renderBlankedLiterals, resolveHarnessName, extractWorkflowArgs, extractBuildSlug,
}
if (require.main === module) main()

// TOOL-dGroundRules-61 S1 — the settings layers rule 7 reads, highest precedence first: the local file
// and the project file under the checkout root, then the file GOV_SETTINGS_JSON declares, a relative
// path read against that root. Below main() so no line above it moves; a declaration hoists. A declared
// path that is not a file throws, as check-wiring.sh's settings_json and `policy.py settings` refuse it,
// and one that resolves to the project or the local file is read once. An absent file is a layer that
// sets nothing; one that does not parse throws naming it (TOOL-dGroundRules-21 S38).
function readSettingsLayers(root) {
  const fs = require('fs')
  const path = require('path')
  const names = ['.claude/settings.local.json', '.claude/settings.json']
  const declared = process.env.GOV_SETTINGS_JSON
  if (declared) {
    checkSettingsInForce.step = `resolving GOV_SETTINGS_JSON ${declared}`
    const p = path.resolve(root, declared)
    let st = null
    try { st = fs.statSync(p) } catch { st = null }
    if (!st || !st.isFile()) throw new Error(`GOV_SETTINGS_JSON names ${declared}, which is not a file`)
    const real = fs.realpathSync(p)
    if (!names.some((n) => { try { return fs.realpathSync(path.resolve(root, n)) === real } catch { return false } })) names.push(declared)
  }
  return names.map((name) => {
    checkSettingsInForce.step = `reading ${name}`
    let text
    try { text = fs.readFileSync(path.resolve(root, name), 'utf8') } catch (e) {
      if (e && e.code === 'ENOENT') return { name, env: {} }
      throw e
    }
    let obj
    try { obj = JSON.parse(text) } catch (e) { throw new Error(`${name} does not parse as JSON: ${e.message}`) }
    return { name, env: obj && typeof obj === 'object' && obj.env && typeof obj.env === 'object' ? obj.env : {} }
  })
}

// TOOL-dFairHearing-22 — THE OPT-IN PACK'S PRESENCE, after rules 6 and 7. The spec-audit opt-in left
// this hook for the review kit's spec-audit-optin.js (TOOL-dFairHearing-16), and a partial update
// that names this kit alone lands the hook without it: the hooks kit cannot require the review kit,
// which requires it back, a cycle govkit refuses. So a Workflow call carrying the opt-in's own
// trigger, `kind: 'spec-audit'` or a `specAudit` key in its structured args, is refused unless the
// pack is found in `resolve_kit_dir`'s order (TOOL-dFairHearing-27 S20): first the install receipt,
// `.governance/install.json` at the root the nearest `.git` names, whose row `source` ends
// `workflows/spec-audit-optin.js` with a `path` that is a file inside the tree; then the probe in the
// workflows kit beside this hook's directory. A row whose `path` is no such file refuses naming it, and
// no `..` path is followed. The receipt's `kits` picks the remedy (S13): `update` for a receipt claiming
// review-harness, else `apply`, since govkit's `update` refuses a kit its receipt does not claim; an
// absent or unreadable receipt is the hand-copy case, and the probe decides. WHAT IT DOES NOT CHECK:
// that the pack is wired, which check-wiring.sh reports, or that it judges correctly, which its own
// suite does. A throw refuses. null = allow · string = deny.
function checkOptinPackPresent(data) {
  const path = require('path')
  const fs = require('fs')
  try {
    const a = data.tool_name === 'Workflow' ? extractWorkflowArgs(data) : null
    if (!a || (String(a.kind) !== 'spec-audit' && a.specAudit === undefined)) return null
    const kits = path.dirname(__dirname)
    let root = __dirname
    for (let d = __dirname; ; d = path.dirname(d)) {
      if (fs.existsSync(path.join(d, '.git'))) { root = d; break }
      if (path.dirname(d) === d) break
    }
    let receipt = null
    try { receipt = JSON.parse(fs.readFileSync(path.join(root, '.governance', 'install.json'), 'utf8')) } catch { receipt = null }
    const rows = receipt && Array.isArray(receipt.files) ? receipt.files : []
    const row = rows.find((r) => r && typeof r.path === 'string' && r.path && String(r.source || '').split('/').slice(-2).join('/') === 'workflows/spec-audit-optin.js')
    let p = path.join(kits, 'workflows', 'spec-audit-optin.js')
    let where = 'is not beside this hook'
    if (row) {
      p = path.resolve(root, row.path)
      const rel = path.relative(root, p)
      const inside = rel !== '' && !path.isAbsolute(rel) && !rel.split(path.sep).includes('..') && !row.path.split(/[\\/]/).includes('..')
      let isFile = false
      try { isFile = fs.statSync(p).isFile() } catch { isFile = false }
      if (inside && isFile) return null
      where = `is the path the install receipt names, and it is not a file inside this tree`
    } else if (fs.existsSync(p)) return null
    const claimed = !!receipt && Array.isArray(receipt.kits) && receipt.kits.includes('review-harness')
    const renderRel = (f) => path.relative(process.env.CLAUDE_PROJECT_DIR || process.cwd(), f).split(path.sep).join('/')
    return `BLOCKED by agent-cap: this Workflow call is a spec audit, and the spec-audit opt-in pack ` +
      `${row ? row.path : renderRel(p)} ${where}. The opt-in moved to the review kit (TOOL-dFairHearing-16), ` +
      `and a hook landed without its pack does not admit an audit nobody judged.\n` +
      `Install the pack: govkit ${claimed ? 'update' : 'apply'} --kits review-harness, or wire a hand copy with ` +
      `python ${renderRel(path.join(kits, 'settings-merge.py'))} --fragment ${renderRel(path.join(kits, 'workflows', 'spec-audit-optin.fragment.json'))}.\n`
  } catch (e) {
    return `BLOCKED by agent-cap: the spec-audit pack check (TOOL-dFairHearing-22) threw (${(e && e.message) || e}), and a rule that cannot finish does not admit.\n`
  }
}
