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
 * THE RULES IT KEEPS, in the order `main()` runs them: rule 6, rule 7, then an `Agent` call is admitted;
 * a `Workflow` call goes on to rule 0, the script read, rule 2 and rule 5.
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
 * whose every value is an `agent`-true role. Skipped under `--only=`. A throw inside it refuses.
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
 * no rule; a `cwd` in no checkout refuses, naming it (TOOL-dGroundRules-21 S38). Skipped under `--only=`. A throw inside it refuses.
 *
 * RULE 0 (TOOL-aBlindedTrial-6) denies a `Workflow` call whose structured `args` carry
 * `kind: "spec-audit"` unless the build README under `args.repo` declares `spec-audit: <YYYY-MM-DD>`
 * in its front matter, or (TOOL-aBlindedTrial-7) that README carries no key and
 * `<args.repo>/.unattended.conf` declares `SPEC_AUDIT_DEFAULT="<YYYY-MM-DD>"`. What it does NOT see,
 * said here rather than implied: the `workflow()` a running harness calls from INSIDE its script is a
 * runtime call and not a tool call, so the programmatic route is the driver's to refuse
 * (TOOL-aBlindedTrial-3); an `args` string that does not parse shows it no `kind`; and it reads the
 * WORKTREE README and conf while the unattended driver reads both at BASE, so the two can disagree for
 * exactly one uncommitted edit.
 *
 * RULE 2 — the verify-stage TOTAL. A review's verify stage spawns at most `MAX_VERIFIERS` agents, the
 * review protocol's verify total, whatever the finding count: an `agent(` reached through an iteration
 * construct must fan over a receiver this file can PROVE bounded. It reads the `Workflow` call's inline
 * `script`, or the file its `scriptPath` names; a `name:` run supplies no source. The verify total is
 * not the agent limit: the limit bounds how many run AT ONCE, and N findings still spawn N agents.
 *
 * RULE 5 (TOOL-dTieredTribunal-14) — the ref-keyed verdict join, refused in a script.
 *
 * `--only=join` runs rule 5 alone and `--only=scripts` rules 2 and 5, the rules that read a script; a
 * WIRED command never carries either, which `check-wiring.sh` asserts.
 *
 * Wiring (per project): run `python <prefix>/settings-merge.py` (idempotent) — it merges the block
 * below into .claude/settings.json; or merge it by hand:
 *   "hooks": { "PreToolUse": [ { "matcher": "Workflow|Agent",
 *     "hooks": [ { "type": "command",
 *       "command": "node \"${CLAUDE_PROJECT_DIR}/<path>/agent-cap.js\"" } ] } ] }
 * The matcher is a LIST OF EXACT STRINGS separated by `|`, in ONE group — not a regular expression.
 * `Workflow` is where this file reads a script; `Agent` is where rules 6 and 7 judge a direct spawn.
 * main() exits 0 on any other tool_name.
 * Blocks via exit 2 + stderr (version-robust; no JSON-schema dependency).
 *
 * WHAT A QUOTE IS, since rules 2 and 5 turn on it. A quote opens a string literal
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

const KIT_AGENT_CAP_VERSION = '1.40' // gov:kit agent-cap@1.40 — engine identity (this file is deployed verbatim; the constant is the deployer's version marker)

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

// ---------------------------------------------------------------------------
// RULE 2 — the VERIFIER ARITY rule (memory/guides/REVIEW-PROTOCOL.md).
//
// A review's verify stage spawns at most MAX_VERIFIERS agents WHATEVER the finding count. The agent
// limit the harness enforces does not give that: it bounds CONCURRENCY, so N findings still spawn N
// agents, a limit's worth at a time. Concurrency is not a budget. The failure this rule exists for was written as an INLINE `script` on a Workflow
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
//       identifier bound in this file to one — or marked `gov:fixed-writers`, the same shape with K at most
//       the landed agent limit (MAX_VERIFIERS with no policy kit). The marker is the AUTHOR'S CLAIM; the
//       shape check is what stops the claim being made falsely — `chunk(all, 1) // gov:fixed-verifiers` reds.
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
// TOOL-dGroundRules-10 F2 — a VERIFIER split's comparand is MAX_VERIFIERS, the verify total. TOOL-dGroundRules-18 — a WRITER
// split's is the agent limit (receiver (a)), read through rule 7's `readPolicy` once, only for a script carrying the marker.
const WRITER_MARK = 'gov:fixed-writers'
const POLICY_HELPER = require('path').join(require('path').dirname(__dirname), 'policy', 'policy-mirror.js')
function readWriterBound(repo) {
  if (!require('fs').existsSync(POLICY_HELPER)) return { n: MAX_VERIFIERS, key: 'MAX_VERIFIERS, as no policy kit sits beside this hooks kit' }
  let v
  try { v = require(POLICY_HELPER).readPolicy('runtime.agents-in-flight', { repo }).value } catch (e) { return { why: `the agent limit could not be read: ${(e && e.message) || e}` } }
  return Number.isInteger(v) && v > 0 ? { n: v, key: 'runtime.agents-in-flight' } : { why: `runtime.agents-in-flight reads ${JSON.stringify(v)}, not a positive integer` }
}

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
// Measured before wiring, at 3ff9cc140 (2026-09-05), over all eight tracked *.js: ZERO lines
// matched the widened form and not the old one, so nothing admitted when this was written became
// denied. The widening reaches the evasions only.
const LOOP_KEYWORDS = 'for(?:\\s+await)?|while'
const LOOP_HEADER = new RegExp('\\b(?:' + LOOP_KEYWORDS + ')\\s*\\(|\\bdo\\s*\\{')
const LOOP_HEADER_G = new RegExp('\\b(?:' + LOOP_KEYWORDS + ')\\s*\\(|\\bdo\\s*\\{', 'g')
const LOOP_KEYWORD_TAIL = new RegExp('\\b(?:' + LOOP_KEYWORDS + ')\\s*$')

// `K` resolved against this file: an integer literal, or an identifier bound to one, judged against
// `bound` — MAX_VERIFIERS, or readWriterBound's for a writer split.
function boundedK(tok, consts, bound) {
  const t = String(tok).trim()
  if (/^\d+$/.test(t)) return Number(t) <= bound
  if (/^[A-Za-z_$][\w$]*$/.test(t) && consts.has(t)) return consts.get(t) <= bound
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
// is refused.
function intConsts(code) {
  const consts = new Map()
  code.forEach((l) => {
    const m = /\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(\d+)\s*$/.exec(l.trim())
    if (m) consts.set(m[1], Number(m[2]))
  })
  // A BARE REASSIGNMENT invalidates the binding, for the same reason it invalidates a bounded
  // receiver below: `let K = 5` followed by `K = 500` published a 5 this file could read and ran a
  // 500. The sweep existed for the receiver whitelist and was never mirrored onto the number.
  code.forEach((l) => {
    const m = /(?:^|[;{}]\s*)([A-Za-z_$][\w$]*)\s*=[^=]/.exec(l)
    if (m && !/\b(const|let|var)\s+$/.test(l.slice(0, m.index + m[0].indexOf(m[1])))) {
      if (!/\b(?:const|let|var)\s+[A-Za-z_$][\w$]*\s*=/.test(l)) consts.delete(m[1])
    }
  })
  return { consts }
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
function boundedBranch(br, name, consts, ok, bound) {
  if (br === null) return false
  const t = String(br).trim()
  if (!t) return false
  const c = /\bchunk\s*\(\s*[^,]+,\s*Math\.ceil\s*\(\s*[A-Za-z_$][\w$.]*\.length\s*\/\s*([^)]+)\)/.exec(t)
  const sp = /\bsplitInto\s*\(\s*[^,]+,\s*([^),]+)\)/.exec(t)
  if ((c && boundedK(c[1], consts, bound)) || (sp && boundedK(sp[1], consts, bound))) return true
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

function fanoutFindings(script, writer) {
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
    if (!boundedK(mm[1], consts, MAX_VERIFIERS)) return ` — ${SEQ_MARK}(${mm[1]}) names a bound this file does not resolve to an integer no greater than MAX_VERIFIERS (${MAX_VERIFIERS})`
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
    const mark = raw.includes(FIXED_MARK) ? FIXED_MARK : raw.includes(WRITER_MARK) ? WRITER_MARK : null
    if (mark) {
      const bound = mark === WRITER_MARK ? writer : raw.includes(WRITER_MARK) ? { why: `the line carries ${WRITER_MARK} too, so its bound is ambiguous` } : { n: MAX_VERIFIERS, key: 'MAX_VERIFIERS' }
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
      const bad0 = branches.find((b) => !boundedBranch(b, name, consts, ok, bound.n))
      if (!grows && !bound.why && branches.length && bad0 === undefined) {
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
      const kTok = (/([\w$]+)\s*\)+\s*$/.exec(String(bad0)) || [])[1], k = consts.has(kTok) ? consts.get(kTok) : Number(kTok)
      markedWhy.set(
        name,
        bound.why ? `\`${name}\` carries ${mark} but ${bound.why}` : grows
          ? `\`${name}\` carries ${mark} but its right-hand side can GROW the receiver`
          : !branches.length || bad0 === null
            ? `\`${name}\` carries ${mark} but this file cannot delimit its value branches`
            : /\b(chunk|splitInto)\s*\(/.test(String(bad0))
              // A bounded split that still fails failed on its K, so the cap is named, with its value and
              // bound where it resolves above one (TOOL-dGroundRules-18); the generic phrase is kept, as
              // two self-test arms assert a marked K's refusal by it, and a stranded arm is a known class.
              ? `\`${name}\` carries ${mark} but its bounded split names a cap which this file does not show to be bounded` +
                (k > bound.n ? ` — its K ${kTok} resolves to ${k}, above the bound ${bound.n}: ${bound.key}` : '')
              : `\`${name}\` carries ${mark} but the branch \`${String(bad0).trim()}\` is not one of the bounded forms`,
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
  // `(` was unreachable, so `sink.push(LENSES.push(9))` escaped. Both close with a LOOKBEHIND form: it
  // asserts without consuming, and it excludes only what actually makes a name a member — a dot or a
  // name character.
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

// TOOL-dTieredTribunal-14 S1 - RULE 5, the ref-keyed verdict join. Ported from the awk in
// <prefix>/workflows/check-review-join.sh, which is a FILE gate and therefore blind to the modality
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
  // TOOL-aWeldedTribunal-3 — an UNTERMINATED scan falls back to the per-line blanked view: the
  // primary view carries its mode across lines, so one unterminated backtick blanked every line below
  // it and this rule saw nothing under it. The per-line view preserves S2's narrowing WITHIN each
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

// RULE 0 — a pre-code SPEC AUDIT is OPT-IN, and the opt-in is a key in the build README's front
// matter (TOOL-aBlindedTrial-6, ruled after a blinded trial found the audit bought nothing the frozen
// suites did not). This is the rule that makes it FORBIDDEN in an attended session, rather than
// merely not required. null = allow · string = the deny message.
//
// It reads `tool_input.args` and NOTHING ELSE: both shipped review harnesses spell `spec-audit` in
// comments and literals and would deny themselves under a text scan. The Workflow tool delivers
// `args` as a JSON STRING even when the caller hands it JSON, so a string is parsed first; a string
// that does not parse shows this hook no `kind` and is not this rule's business (the harness itself
// throws on it, so no audit runs). Placement is `<args.repo>/<parent of args.reviewDir>/README.md` —
// the harness REQUIRES `repo` and takes `reviewDir` repo-relative, and that parent must be a
// `builds/<slug>` folder. Never the git common dir of `cwd`: in a linked worktree that is the PRIMARY tree's
// `.git`, and the README read would be the wrong checkout's.
//
// FAIL CLOSED, for this kind only (F1, resolved): a spec-audit call this rule cannot PLACE — `repo`
// not a string, `reviewDir` outside a build folder, a README it cannot read — is denied by name, and
// EVERY throw is caught and returned as a deny, because a PreToolUse hook that exits 1 is
// non-blocking and a crash here would admit the one call the rule exists to refuse. The value must
// be a DATE: `spec-audit: yes` is a claim with no owner date behind it and reads as absent. The
// front-matter slice is the sibling hook's `readFrontMatterKey`, the same read scratch-guard.js makes
// for `authorized-by:` — one reader, so a body-only key (a fenced example) is not front matter for
// either. Required lazily and inside the try: a withdrawn sibling is a deny, not a crash.
//
// THREE MORE, from the closing review of units 2–5 (round 1). F1: `kind` is compared as
// `String(a.kind)`, because that is how the callee (tier2-review.js) derives it — under strict
// equality `["spec-audit"]` passed this guard and ran a full audit there; one predicate, two
// spellings, and the guard's was the narrower. F2: the declaration is read from where the RECORD
// lands, so every `subjects[].path` must sit under the same `builds/<slug>/` as `reviewDir`'s parent,
// else naming a declared build's reviews folder audits an undeclared build's specs; and a `..`
// segment anywhere in `reviewDir` or a subject is a deny, since the path's text no longer says where
// it lands. F5: `repo` is folded from MSYS spelling before `path.resolve` — on win32 a leading `/` is
// root-relative to the cwd's DRIVE, so `/c/projects/x` became `C:\c\projects\x` and a DECLARED build
// was denied with ENOENT. No lowercasing: an fs read must not.
//
// A PROJECT-WIDE DEFAULT (TOOL-aBlindedTrial-7). When the README is readable and carries NO key,
// `<args.repo>/.unattended.conf` is read for `SPEC_AUDIT_DEFAULT`: a date admits, a non-date DENIES
// by name (armed, never read as absent), a missing file or a blank value is no default and the
// README deny stands. Node cannot source shell, so `readSpecAuditDefault` is the deliberate second
// reader the two-readers gotcha warns of, kept honest by taking the three spellings the shell does
// — both quote styles, a trailing `# comment`, and last-assignment-wins — each pinned by an arm. The
// README wins whatever it says: a present-but-malformed key is the not-a-date deny and the conf is
// never consulted, because a typo falling back to the default is the silent opt-out the driver's
// fail 52 exists to refuse. An unreadable README is still the fail-closed deny with no conf read.
// Stated limit: a BARE `spec-audit:` line has no value for `readFrontMatterKey` and reads as
// absent here, so it falls to the conf, where the driver instead refuses it (fail 52) — the
// disagreement admits an audit, which is the safe direction. Second limit, the same direction: a
// `;`-joined line (`SPEC_AUDIT_DEFAULT="<date>"; X=1`) is no assignment to this reader and the
// README deny stands, while the shell reads the date. Worktree here, BASE there, for an ATTENDED
// session alone: beside a live run-state file the hook reads only the fact the driver pinned from
// the owner's side, and never the worktree README or conf (TOOL-aWardedAudit-2).

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

// The LAST `SPEC_AUDIT_DEFAULT=` assignment's value in a shell-style conf, as the shell would read
// it: double- or single-quoted or bare, an optional `export`, a trailing `# comment` allowed after
// the value ONLY behind whitespace — a `#` glued to a bare word is part of the word to the shell
// (`2026-09-21#c` is the driver's fail 54), and rev-1 stopped the word there and admitted the date
// (closing review of units 7/8, R8). null when no assignment exists. The value is returned RAW; the
// caller decides whether it is a date, so a blank and a non-date are both visible to it. The grammar
// is the sibling hook's `readConfKey`, the one conf reader in this home (TOOL-aRoutedQuill-2 S9).
function readSpecAuditDefault(bytes) {
  const { readConfKey } = require(require('path').join(__dirname, 'scratch-guard.js'))
  return readConfKey(bytes, 'SPEC_AUDIT_DEFAULT')
}

// The run-state phases past which no pre-code audit is owed: a record in one is no live run here.
const NO_AUDIT_PHASES = ['LANDING', 'LANDED', 'ABORTED']

function checkSpecAuditDeclared(data) {
  const ID = 'TOOL-aBlindedTrial-6'
  const renderDeny = (why) =>
    `BLOCKED by agent-cap: ${why} A pre-code spec audit is OPT-IN (${ID}): to run one, the build ` +
    `README's FRONT MATTER carries \`spec-audit: <YYYY-MM-DD>\` (the owner's date; a value that is ` +
    `not a date, or the key inside the body, reads as absent), or the project's .unattended.conf ` +
    `declares \`SPEC_AUDIT_DEFAULT="<YYYY-MM-DD>"\` for every build whose README declares no key ` +
    `(TOOL-aBlindedTrial-7). The opt-in is the OWNER's (TOOL-aWardedAudit-4): never a key in an ` +
    `\`authorized-by: prompt\` or \`recipe\` README, which the run writes itself, and in a live ` +
    `unattended run only the \`spec-audit:\` fact its preflight pinned. This rule reads the Workflow call's ` +
    `structured args only, never the script text.\n`
  let readme = '(unplaced)'
  try {
    const a = extractWorkflowArgs(data)
    if (!a) return null
    // TOOL-aWardedAudit-2 S4 — THE BUILD HARNESS'S `specAudit` IS THE SAME ACT ONE CALL EARLIER. The
    // harness runs its audit through a `workflow()` call inside its own script, a runtime call no
    // hook sees, so the only tool call there is to judge is the one carrying `specAudit`. It is placed
    // by the harness's own default, `memory/builds/<slug>/reviews`, when `reviewDir` is absent, and a
    // `slug` that is not one path segment cannot be placed. Presence is the test, whatever the value.
    const harness = a.specAudit !== undefined
    if (String(a.kind) !== 'spec-audit' && !harness) return null
    if (typeof a.repo !== 'string' || a.repo === '') {
      return renderDeny(`a spec-audit Workflow call whose \`repo\` is not a non-empty string cannot be placed, so it cannot be admitted.`)
    }
    let rdir = a.reviewDir
    if (harness && !rdir) {
      if (typeof a.slug !== 'string' || !/^[A-Za-z0-9_-]+$/.test(a.slug)) {
        return renderDeny(`a Workflow call carrying \`specAudit\` whose \`slug\` (${JSON.stringify(a.slug)}) is not one path segment, and which names no \`reviewDir\`, cannot be placed, so it cannot be admitted.`)
      }
      rdir = 'memory/builds/' + a.slug + '/reviews'
    }
    const parts = String(rdir === undefined || rdir === null ? '' : rdir)
      .replace(/\\/g, '/').replace(/\/+$/, '').split('/')
    const dir = parts.slice(0, -1) // reviewDir's parent: the build folder
    if (dir.length < 2 || dir[dir.length - 2] !== 'builds' || dir[dir.length - 1] === '' || parts.indexOf('..') !== -1) {
      return renderDeny(`a spec-audit Workflow call whose \`reviewDir\` (${JSON.stringify(rdir)}) is not directly under a \`builds/<slug>/\` folder, or climbs through \`..\`, cannot be placed, so it cannot be admitted.`)
    }
    // TOOL-aWardedAudit-6 S1 — A HARNESS CALL IS PLACED IN ITS OWN SLUG'S BUILD. Its nested audit reads
    // `units[].specPath` and writes to `reviewDir`, and nothing in the harness compares either with
    // `slug`, so a `reviewDir` under another build read THAT build's README and run-state file while
    // auditing this one's specs — a live run's pinned fact routed around by one argument. A unit with
    // no `specPath` is still to be specced and names nothing to place.
    if (harness && typeof a.slug === 'string' && a.slug !== '') {
      if (dir[dir.length - 1] !== a.slug) {
        return renderDeny(`a Workflow call carrying \`specAudit\` for \`slug\` ${JSON.stringify(a.slug)} names a \`reviewDir\` (${JSON.stringify(rdir)}) under another build, whose README and run-state file are not this run's, so it cannot be admitted.`)
      }
      const strayUnit = (Array.isArray(a.units) ? a.units : []).find((u) =>
        u && typeof u.specPath === 'string' && u.specPath !== '' && extractBuildSlug(u.specPath) !== a.slug)
      if (strayUnit !== undefined) {
        return renderDeny(`a Workflow call carrying \`specAudit\` for \`slug\` ${JSON.stringify(a.slug)} names a \`units[].specPath\` (${JSON.stringify(strayUnit.specPath)}) outside \`builds/${a.slug}/\`, so it would audit a build whose opt-in this rule never read.`)
      }
    }
    if (Array.isArray(a.subjects)) {
      const stray = a.subjects.find((s) => extractBuildSlug(s && s.path) !== dir[dir.length - 1])
      if (stray !== undefined) {
        return renderDeny(`a spec-audit Workflow call whose \`subjects\` name a path (${JSON.stringify(stray && stray.path)}) outside \`builds/${dir[dir.length - 1]}/\`, the build its \`reviewDir\` places it in, would audit a build whose README this rule never read, so it cannot be admitted.`)
      }
    }
    const path = require('path')
    // The MSYS fold corrects a WIN32 rule and runs there alone (round 2, R2): on POSIX a one-letter
    // first segment (`/w/repo`) is a real root, and the unguarded fold made it a cwd-relative
    // `w:/repo` that ENOENTs. What the fold cannot reach — a repo under any OTHER MSYS mount, `/tmp/…`
    // — is denied by name rather than resolved to `C:\tmp\…` and reported as a README that does not
    // exist, which hid the spelling that was actually tried.
    const repo = process.platform === 'win32' ? a.repo.replace(/\\/g, '/').replace(/^\/([A-Za-z])\//, '$1:/') : a.repo
    if (process.platform === 'win32' && repo.startsWith('/')) {
      return renderDeny(`a spec-audit Workflow call whose \`repo\` (${JSON.stringify(a.repo)}) is an MSYS mount path other than /<drive>/… cannot be placed from Node on Windows; pass the Windows or /<drive>/ spelling.`)
    }
    const root = path.resolve(data.cwd || process.cwd(), repo)
    readme = path.join(root, ...dir, 'README.md').split(path.sep).join('/')
    const bytes = require('fs').readFileSync(readme, 'utf8')
    const { readFrontMatterKey } = require(path.join(__dirname, 'scratch-guard.js'))
    const v = readFrontMatterKey(bytes, 'spec-audit')
    // TOOL-aWardedAudit-2 S1 — A LIVE UNATTENDED RUN IS DECIDED BY ITS RUN-STATE FACT, never by the
    // worktree. The driver's preflight pinned `spec-audit:` from the owner's side (a slug README at
    // BASE, or the default at the default-branch side), and a key or default the run writes into its
    // worktree afterwards is the self-opt-in that ruling refuses. `RUN.md` beside the README, with a
    // `phase:` fact outside NO_AUDIT_PHASES, is a live run; ENOENT is an attended session and
    // falls through; any other read failure is a deny, on the fail-closed rule above. Column-1 fact
    // lines only, the driver's own shape: a parked row opens with a timestamp and never matches.
    const runmd = path.join(root, ...dir, 'RUN.md').split(path.sep).join('/')
    let rbytes = null
    try { rbytes = require('fs').readFileSync(runmd, 'utf8') } catch (e) {
      if (!e || e.code !== 'ENOENT') return renderDeny(`${runmd} could not be read for its \`phase:\` and \`spec-audit:\` facts (${(e && e.code) || (e && e.message) || e}), and a run-state file this hook cannot read is not one it may approve from.`)
    }
    if (rbytes !== null) {
      // TOOL-aWardedAudit-6 S2 — READ AS THE DRIVER'S `fact()` READS: inside `## Run facts` alone, up to
      // the next `## ` heading, so a key-shaped line anywhere else decides nothing. NO_AUDIT_PHASES is
      // NOT a copy of the driver's terminal set: it adds LANDING, because a record past its close owes
      // no pre-code audit, and a committed LANDING outlives its push on every landed build in the tree.
      const facts = (/^## Run facts[ \t]*\r?$([\s\S]*?)(?=^## |(?![\s\S]))/m.exec(rbytes) || [])[1] || ''
      const phase = (/^phase:[ \t]*(\S+)[ \t]*\r?$/m.exec(facts) || [])[1] || ''
      if (NO_AUDIT_PHASES.indexOf(phase) === -1) {
        const f = (/^spec-audit:[ \t]*(\S+)[ \t]*\r?$/m.exec(facts) || [])[1] || ''
        // The harness's `specAudit` must BE the pinned date: a different date is a declaration the
        // preflight never read, which is the self-opt-in again with a fact standing beside it.
        if (/^\d{4}-\d{2}-\d{2}$/.test(f) && (!harness || a.specAudit === f)) return null
        if (/^\d{4}-\d{2}-\d{2}$/.test(f)) {
          return renderDeny(`${runmd} pins \`spec-audit: ${f}\`, and this call passes \`specAudit\` ${JSON.stringify(a.specAudit)}; the harness takes the pinned date or nothing.`)
        }
        return renderDeny(`${runmd} is a live unattended run (phase ${phase || '(none)'}) that pins no dated \`spec-audit:\` fact, so its preflight found no owner opt-in, and a key or default written into the worktree since is the run's own.`)
      }
    }
    // TOOL-aWardedAudit-2 S2 — a README the run writes itself admits nothing by its own key: the
    // driver refuses the same line at check 89, so admitting it here would spend an audit the run
    // can never record. Presence is the test, a non-date included, so the deny names the cause.
    const mode = readFrontMatterKey(bytes, 'authorized-by')
    if (v !== null && mode !== null && mode !== 'slug') {
      return renderDeny(`${readme} declares \`spec-audit: ${v}\` under \`authorized-by: ${mode}\`, a README the run writes itself, so the key admits nothing.`)
    }
    if (v !== null && /^\d{4}-\d{2}-\d{2}$/.test(v)) return null
    if (v === null) {
      // README silent: the project default, from the WORKTREE conf. ENOENT is no default; any other
      // read failure is a deny naming the conf, on the fail-closed rule above.
      const conf = path.join(root, '.unattended.conf').split(path.sep).join('/')
      let cbytes = null
      try { cbytes = require('fs').readFileSync(conf, 'utf8') } catch (e) {
        if (!e || e.code !== 'ENOENT') return renderDeny(`${conf} could not be read for its \`SPEC_AUDIT_DEFAULT\` key (${(e && e.code) || (e && e.message) || e}), and a conf this hook cannot read is not one it may approve from.`)
      }
      const d = cbytes === null ? null : readSpecAuditDefault(cbytes)
      if (d !== null && d !== '') {
        if (/^\d{4}-\d{2}-\d{2}$/.test(d)) return null
        return renderDeny(`${readme} declares no \`spec-audit:\` key, and the project's ${conf} declares \`SPEC_AUDIT_DEFAULT="${d}"\`, which is not a date — a project-wide opt-in is dated or it is not one.`)
      }
    }
    return renderDeny(
      `${readme} declares no \`spec-audit:\` date in its front matter` +
        (v === null ? '' : ` (it reads \`spec-audit: ${v}\`, which is not a date)`) + `.`,
    )
  } catch (e) {
    return renderDeny(`${readme} could not be read for its \`spec-audit:\` key (${(e && e.code) || (e && e.message) || e}), and a README this hook cannot read is not one it may approve.`)
  }
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
  // TOOL-dTieredTribunal-14 S4 - a rule selector over a CLOSED set, so a second entry point can ask
  // for ONE rule. Absent runs every rule, which is the wiring's invocation and is unchanged.
  // Anything outside the set REFUSES rather than silently matching nothing, which would be this
  // repo's vacuous-selector-empty-population class arriving in the file whose job is to refuse what
  // it cannot resolve. A WIRED command must never carry it: <prefix>/check-wiring.sh asserts that,
  // because `--only=join` in settings.json would turn the other rules off with no diff.
  // TOOL-aOrientedCast-7 S11 - `scripts` is rules 2 and 5, the rules that read a SCRIPT, and never
  // rules 0, 6 and 7, which judge the CALL. A file gate feeding committed scripts as inline
  // `script` payloads asks with it; rule 6 would refuse every such payload wherever an index exists.
  const ONLY_RULES = ["join", "scripts"]
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

  // RULE 6 (TOOL-aOrientedCast-7) — first, so a call outside a declared harness is refused whatever its
  // args. Skipped under any `--only=` selector, as rules 7 and 0 are. An absent `.claude/roles.json` at
  // the role root adds no rule; a broken one, or a throw anywhere in the rule, refuses: a rule that
  // cannot finish does not admit.
  if (ONLY === null) {
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
  if (ONLY === null) {
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

  // An `Agent` payload carries no script, and every rule below reads one.
  if (data.tool_name === 'Agent') process.exit(0)

  // RULE 0 sits ABOVE the script read on purpose: a `name:`-only run exits below with no source, and
  // a rule placed among the script rules would never see the spec-audit route invoked by name. It keys
  // on the structured args, so it needs no script at all. Skipped under `--only=`, so `--only=join`
  // stays exactly the join rule.
  if (ONLY === null) {
    const deny = checkSpecAuditDeclared(data)
    if (deny) {
      process.stderr.write(deny)
      process.exit(2)
    }
  }

  // A saved script is a FILE, and a node hook has fs — exiting 0 here made the rules unenforceable
  // the moment anyone wrote the offending script to disk. A `name:`-only run supplies no source and
  // stays unscannable; that hole is covered by the merge-bar leg over <prefix>/workflows/, and is
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

  const writer = ONLY !== 'join' && script.includes(WRITER_MARK) ? readWriterBound(ONLY === 'scripts' ? process.cwd() : data.cwd || process.cwd()) : null
  const fan = ONLY !== 'join' ? runBothViews((s) => fanoutFindings(s, writer), script) : []
  if (fan.length) {
    process.stderr.write(
      `BLOCKED by agent-cap: a verify/fan-out stage spawns one agent per item. The review protocol ` +
        `caps verify-stage agents at ${MAX_VERIFIERS} TOTAL, this hook's MAX_VERIFIERS — the batch size grows with the finding ` +
        `count, the agent count never does (memory/guides/REVIEW-PROTOCOL.md).\n\n` +
        fan.slice(0, 6).map(({ n, line, why }) => `  L${n}: ${line.trim()}\n        ${why}`).join('\n') +
        `\n\nSplit into a BOUNDED number of groups and mark the assignment:\n` +
        `  const MAX_VERIFIERS = ${MAX_VERIFIERS}\n` +
        `  const batches = chunk(items, Math.ceil(items.length / MAX_VERIFIERS)) // ${FIXED_MARK}\n` +
        `  await boundedParallel(batches.map((g) => () => agent(promptFor(g))), MAX_VERIFIERS)\n\n` +
        `A fixed lens array (<= ${MAX_LENSES} elements) is allowed as-is — its agent count is a ` +
        `constant. Ready-made: ${resolveHarnessName()}.\n`,
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
        `reproduces. Ready-made: ${resolveHarnessName()}.\n`,
    )
    process.exit(2)
  }

  process.exit(0)
}

main()

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
