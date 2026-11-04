#!/usr/bin/env node
/**
 * check-review-join.js — RULE 5 of the agent-cap hook until TOOL-dFairHearing-16, the review kit's
 * since the owner's NT-27: the ref-keyed verdict join, refused in a script. It holds the ban table and
 * its deny message, and `check-review-join.sh` beside it is the one thing that runs it, over every
 * script in its population, so nothing else carries the ban.
 *
 * ONE SCANNER. The literal-blanked view, the stripped view and `runBothViews`, which unions the lexed
 * and the shipped views so no denial is lost, are agent-cap's, loaded from the hook `--hook` names:
 * each view reads the mode `runBothViews` switches, so a copy here would be a second scanner of one
 * script. Everything below `loadHook` is the hook's rule 5, moved verbatim, its per-line fallback with it.
 *
 *   node <prefix>/workflows/check-review-join.js --hook <prefix>/hooks/agent-cap.js <file>...
 *
 * Exit 0 = clean · 1 = a join, each file's printed on stderr as the hook printed it, one `  L<n>:` line
 * per hit · 2 = refused: no `--hook` or no file, an argument it does not take, agent-cap's exports not
 * loadable, or a file it cannot read. This file holds the ban table as regex literals, which survive
 * the blanking, so the gate keeps it out of its own population.
 */
'use strict'

// The hook's exports, bound by `loadHook` before the rule runs; the rule reads them by these names.
let renderBlankedLiterals, renderStrippedView, runBothViews, resolveHarnessName

function loadHook(hook) {
  const m = require(require('path').resolve(hook))
  const need = ['renderBlankedLiterals', 'renderStrippedView', 'runBothViews', 'resolveHarnessName']
  const miss = need.filter((k) => m[k] === undefined)
  if (miss.length) throw new Error(`it exports no ${miss.join(', ')}`)
  ;({ renderBlankedLiterals, renderStrippedView, runBothViews, resolveHarnessName } = m)
  return m
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

// Rule 5 over one script under both views.
function scanJoin(script) {
  return runBothViews(scanJoinFindings, script)
}

// The deny the hook printed, byte for byte: the moved arms and the gate's own suite assert its text.
function renderJoinDeny(joins) {
  return (
    `BLOCKED by agent-cap: a ref-keyed verdict join. A review harness that joins each finding to ` +
    `its skeptic verdict on a \`file:line\` STRING loses findings to echo drift and COLLAPSES two ` +
    `findings at one location, so both inherit whichever verdict landed last. The class has no ` +
    `runtime signal - a mis-keyed harness reports a clean bill.\n\n` +
    joins.slice(0, 6).map(({ n, line, why }) => `  L${n}: ${String(line).trim()}\n        ${why}`).join('\n') +
    `\n\nKey the join on the integer id the orchestrator assigns, never on a string the skeptic ` +
    `reproduces. Ready-made: ${resolveHarnessName()}.\n`
  )
}

// THE CLI, the verifier check's contract: every refusal is exit 2 with its reason, never a pass, and a
// throw anywhere is a refusal too, since node's own exit 1 on an uncaught throw would read as a join.
// ponytail: this argv loop is check-verifier-fanout.js's twin; dBoundRoles' move of the shared readers is where one runner would live.
function main(argv) {
  const printRefusal = (why) => { process.stderr.write(`check-review-join: ${why}\n`); return 2 }
  let hook = null
  const files = []
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--hook') hook = argv[++i] || null
    else if (argv[i].startsWith('-')) return printRefusal(`${argv[i]} is no argument this check takes: it takes --hook <agent-cap.js> and the files to judge`)
    else files.push(argv[i])
  }
  if (!hook) return printRefusal('names no --hook, so agent-cap\'s views, which this rule reads, cannot be loaded')
  if (!files.length) return printRefusal('names no file, and a check over nothing is not a pass')
  try { loadHook(hook) } catch (e) { return printRefusal(`cannot load agent-cap's exports from ${hook}: ${(e && e.message) || e}`) }
  let status = 0
  for (const f of files) {
    let script
    try { script = require('fs').readFileSync(f, 'utf8') } catch (e) {
      return printRefusal(`${f} could not be read (${(e && e.code) || (e && e.message) || e}), and a script this check cannot read is not one it may pass`)
    }
    const joins = scanJoin(script)
    if (joins.length) { process.stderr.write(renderJoinDeny(joins)); status = 1 }
  }
  return status
}

module.exports = { loadHook, scanJoinFindings, scanJoin, renderJoinDeny }
if (require.main === module) {
  let code
  try { code = main(process.argv.slice(2)) } catch (e) {
    process.stderr.write(`check-review-join: refused — the check threw (${(e && e.message) || e}), and a check that cannot finish passes nothing\n`)
    code = 2
  }
  process.exit(code)
}
