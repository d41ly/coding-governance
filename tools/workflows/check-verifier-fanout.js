#!/usr/bin/env node
/**
 * check-verifier-fanout.js — RULE 2 of the agent-cap hook until TOOL-dFairHearing-16, the review
 * kit's since the owner's NT-27: the verify-stage TOTAL and the loop markers. A review's verify stage
 * spawns at most the hook's MAX_VERIFIERS agents whatever the finding count, and the three markers
 * `gov:fixed-verifiers`, `gov:fixed-writers` and `gov:sequential-agents` are claims this file checks.
 * The merge bar runs it over every committed harness through `check-verifier-fanout.sh` beside it.
 * An inline `script` on a Workflow call is no longer judged at the tool call: the harness's own
 * concurrency settings bound it, and the rule judges what is committed.
 *
 * ONE SCANNER. The views this rule reads, and `runBothViews`, which unions the lexed and the shipped
 * views so no denial is lost, are agent-cap's, loaded from the hook `--hook` names: each view reads the
 * mode `runBothViews` switches, so a copy here would be a second scanner of one script, the drift
 * TOOL-aBatchedTribunal-1d ruled out. MAX_VERIFIERS and the writer bound are the hook's too. Everything
 * below `loadHook` is the hook's rule 2, moved verbatim, but for its array-literal bound, which reads
 * LENS_SLOTS (TOOL-dFairHearing-23 S42).
 *
 * THE SLOT COUNT (TOOL-dFairHearing-13, here since TOOL-dFairHearing-23). `--slots` takes `<file>:<line>`
 * locations, each a marker line `render_lenses.py --markers` printed, so the renderer's own anchored
 * regex is the one predicate finding a marked literal. Each literal, from that line's `[` to its matching
 * `]` in the hook's literal-blanked view, holds exactly LENS_SLOTS top-level elements, counted by
 * `topLevelArgs`, the counter rule 2 uses, so a comma inside parentheses, braces or a string is no slot.
 *
 *   node <prefix>/workflows/check-verifier-fanout.js --hook <prefix>/hooks/agent-cap.js <file>...
 *   node <prefix>/workflows/check-verifier-fanout.js --hook <prefix>/hooks/agent-cap.js --slots <file>:<line>...
 *
 * Exit 0 = clean · 1 = a finding, each file's printed on stderr as the hook printed it · 2 = refused:
 * no `--hook` or no file, an argument it does not take, agent-cap's exports not loadable, or a file it
 * cannot read. A writer split's bound is the hook's `readWriterBound` read at this process's working
 * directory, where the hook's `--only=scripts` read it.
 */
'use strict'

// The hook's exports, bound by `loadHook` before any rule runs; the rule reads them by these names.
let MAX_VERIFIERS, renderCodeView, renderStrippedView, renderBlankedLiterals, runBothViews, readWriterBound, resolveHarnessName

function loadHook(hook) {
  const m = require(require('path').resolve(hook))
  const need = ['MAX_VERIFIERS', 'renderCodeView', 'renderStrippedView', 'renderBlankedLiterals', 'runBothViews', 'readWriterBound', 'resolveHarnessName']
  const miss = need.filter((k) => m[k] === undefined)
  if (miss.length) throw new Error(`it exports no ${miss.join(', ')}`)
  ;({ MAX_VERIFIERS, renderCodeView, renderStrippedView, renderBlankedLiterals, runBothViews, readWriterBound, resolveHarnessName } = m)
  return m
}

// THE LENS COUNT, its one home (TOOL-dFairHearing-23 S42): a marked lens literal holds exactly this many
// slots, and rule 2's array-literal bound admits a literal of at most this many elements. It was two
// numbers, the hook's lens bound and the fan-out gate's shell constant, which agreed only by hand.
const LENS_SLOTS = 5

// ---------------------------------------------------------------------------
// RULE 2 — the VERIFIER ARITY rule (memory/guides/REVIEW-PROTOCOL.md).
//
// A review's verify stage spawns at most MAX_VERIFIERS agents WHATEVER the finding count. The agent
// limit the harness enforces does not give that: it bounds CONCURRENCY, so N findings still spawn N
// agents, a limit's worth at a time. Concurrency is not a budget. The failure this rule exists for was written as an INLINE `script` on a Workflow
// tool call — never a file — which is why the check lived in the hook, at the tool call, until the
// owner's NT-27 moved it here, to the merge bar's harness check (TOOL-dFairHearing-16): an inline
// script is now bounded by the harness's own concurrency settings, and this rule judges what lands.
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
//   (b) an identifier assigned from an ARRAY LITERAL with <= LENS_SLOTS elements — the finder-lens
//       case, where the agent count is a constant visible in the source. The count drops a trailing
//       comma; counting it as an element is what made this allowance read as 6.
// Everything else is denied, including a for/while/forEach body containing `agent(`: a loop-built
// thunk array is the evasion, not an edge case.
const FIXED_MARK = 'gov:fixed-verifiers'
// TOOL-dGroundRules-18 — a WRITER split's comparand is the agent limit, the hook's `readWriterBound`.
const WRITER_MARK = 'gov:fixed-writers'

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
// array LITERAL whose top-level element count is at or under LENS_SLOTS, counted with the shared
// splitter so a trailing comma is not an element; or a bare identifier already proven bounded,
// alone or followed by a chain of operations that cannot grow it.
function boundedBranch(br, name, consts, ok, bound) {
  if (br === null) return false
  const t = String(br).trim()
  if (!t) return false
  const c = /\bchunk\s*\(\s*[^,]+,\s*Math\.ceil\s*\(\s*[A-Za-z_$][\w$.]*\.length\s*\/\s*([^)]+)\)/.exec(t)
  const sp = /\bsplitInto\s*\(\s*[^,]+,\s*([^),]+)\)/.exec(t)
  if ((c && boundedK(c[1], consts, bound)) || (sp && boundedK(sp[1], consts, bound))) return true
  if (t.startsWith('[') && t.endsWith(']')) return topLevelArgs(t.slice(1, -1)).length <= LENS_SLOTS
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
    // array measure 6 — which is the entire reason the hook's lens bound was 6. It never meant "six lenses are
    // allowed"; it meant "five lenses, plus the phantom the counter invented". Every shipped harness
    // is prettier-formatted, so every one of them was mis-measured, and the constant was raised to
    // fit the error rather than the error being found.
    if (topLevelArgs(inner).length <= LENS_SLOTS) ok.add(name)
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
    const scanOpeners = (text) => {
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
    for (let k = i - 1; k >= 0 && k > i - 60 && scanOpeners(win).length < 2; k--) win = code[k] + '\n' + win

    // FAIL CLOSED. The first cut classified only three tidy spellings and fell through to ALLOW for
    // everything else, which meant a receiver it did not recognise was a receiver it blessed — five
    // independent bypasses, each one agent per finding, each reported clean. An iteration construct
    // this rule cannot PROVE bounded is denied; the burden is on the fan-out, not on the gate.
    let hit = null
    for (const pos of scanOpeners(win)) {
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

// THE SLOT COUNT of one marked literal (TOOL-dFairHearing-23 S42): the top-level element count of the
// literal opened by the last `[` of 1-based line `n` in the hook's literal-blanked view, where strings,
// templates and comments are blank and the delimiters stay, so the walk to its matching `]` and
// `topLevelArgs` see structure alone. 'unterminated' when no `[` opens there or none closes it.
function measureLensSlots(script, n) {
  const code = renderBlankedLiterals(script).code
  const at = (code[n - 1] || '').lastIndexOf('[')
  if (at === -1) return 'unterminated'
  let depth = 0
  let body = ''
  for (let j = n - 1; j < code.length; j++) {
    for (const ch of j === n - 1 ? code[j].slice(at) : code[j]) {
      if ('([{'.includes(ch)) depth++
      else if (')]}'.includes(ch) && --depth === 0) return topLevelArgs(body.slice(1)).length
      body += ch
    }
    body += '\n'
  }
  return 'unterminated'
}

// Rule 2 over one script under both views, the writer bound read once and only for a marked script,
// at this process's working directory.
function scanFanout(script) {
  const writer = script.includes(WRITER_MARK) ? readWriterBound(process.cwd()) : null
  return runBothViews((s) => fanoutFindings(s, writer), script)
}

// The deny the hook printed, byte for byte: the moved arms assert its text.
function renderFanoutDeny(fan) {
  return (
    `BLOCKED by agent-cap: a verify/fan-out stage spawns one agent per item. The review protocol ` +
    `caps verify-stage agents at ${MAX_VERIFIERS} TOTAL, this hook's MAX_VERIFIERS — the batch size grows with the finding ` +
    `count, the agent count never does (memory/guides/REVIEW-PROTOCOL.md).\n\n` +
    fan.slice(0, 6).map(({ n, line, why }) => `  L${n}: ${line.trim()}\n        ${why}`).join('\n') +
    `\n\nSplit into a BOUNDED number of groups and mark the assignment:\n` +
    `  const MAX_VERIFIERS = ${MAX_VERIFIERS}\n` +
    `  const batches = chunk(items, Math.ceil(items.length / MAX_VERIFIERS)) // ${FIXED_MARK}\n` +
    `  await boundedParallel(batches.map((g) => () => agent(promptFor(g))), MAX_VERIFIERS)\n\n` +
    `A fixed lens array (<= ${LENS_SLOTS} elements) is allowed as-is — its agent count is a ` +
    `constant. Ready-made: ${resolveHarnessName()}.\n`
  )
}

// THE CLI. Every refusal is exit 2 with its reason, and never a pass: a check that could not load its
// predicate or read its file has measured nothing. A throw anywhere is a refusal too, since node's own
// exit 1 on an uncaught throw would read as a finding.
function main(argv) {
  const printRefusal = (why) => { process.stderr.write(`check-verifier-fanout: ${why}\n`); return 2 }
  let hook = null
  let slots = false
  const files = []
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--hook') hook = argv[++i] || null
    else if (argv[i] === '--slots') slots = true
    else if (argv[i].startsWith('-')) return printRefusal(`${argv[i]} is no argument this check takes: it takes --hook <agent-cap.js>, then the files to judge or --slots and their <file>:<line> marker locations`)
    else files.push(argv[i])
  }
  if (!hook) return printRefusal('names no --hook, so agent-cap\'s views, which this rule reads, cannot be loaded')
  if (!files.length) return printRefusal('names no file, and a check over nothing is not a pass')
  try { loadHook(hook) } catch (e) { return printRefusal(`cannot load agent-cap's exports from ${hook}: ${(e && e.message) || e}`) }
  if (slots) {
    // Each location is a marker line render_lenses.py --markers printed; the literal's name is the line's last word.
    let bad = 0
    for (const loc of files) {
      const cut = loc.lastIndexOf(':')
      const f = loc.slice(0, cut)
      const n = Number(loc.slice(cut + 1))
      let script
      try { script = require('fs').readFileSync(f, 'utf8') } catch (e) {
        return printRefusal(`${f} could not be read (${(e && e.code) || (e && e.message) || e}), and a literal this check cannot read is not one it may pass`)
      }
      const line = script.split(/\r?\n/)[n - 1]
      if (cut <= 0 || !Number.isInteger(n) || n < 1 || line === undefined) return printRefusal(`--slots ${loc} names no line of a file, so it is no marker location`)
      const count = measureLensSlots(script, n)
      if (count !== LENS_SLOTS) {
        process.stdout.write(`verifier-fanout: SLOTS — ${loc} literal ${line.trim().split(/\s+/).pop()} holds ${count} slot(s); a lens literal holds exactly ${LENS_SLOTS}\n`)
        bad++
      }
    }
    if (!bad) process.stdout.write(`verifier-fanout: slots — ${files.length} lens-slot literal(s), each holding ${LENS_SLOTS}\n`)
    return bad ? 1 : 0
  }
  let status = 0
  for (const f of files) {
    let script
    try { script = require('fs').readFileSync(f, 'utf8') } catch (e) {
      return printRefusal(`${f} could not be read (${(e && e.code) || (e && e.message) || e}), and a script this check cannot read is not one it may pass`)
    }
    const fan = scanFanout(script)
    if (fan.length) { process.stderr.write(renderFanoutDeny(fan)); status = 1 }
  }
  return status
}

module.exports = { loadHook, fanoutFindings, scanFanout, renderFanoutDeny, FIXED_MARK, WRITER_MARK, SEQ_MARK }
if (require.main === module) {
  let code
  try { code = main(process.argv.slice(2)) } catch (e) {
    process.stderr.write(`check-verifier-fanout: refused — the check threw (${(e && e.message) || e}), and a check that cannot finish passes nothing\n`)
    code = 2
  }
  process.exit(code)
}
