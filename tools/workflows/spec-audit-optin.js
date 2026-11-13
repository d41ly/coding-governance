#!/usr/bin/env node
/**
 * spec-audit-optin.js — the review kit's spec-audit opt-in pack: a PreToolUse hook on `Workflow`
 * calls holding RULE 0 of the agent-cap hook whole, moved here by TOOL-dFairHearing-16 (the owner's
 * NT-27), since the opt-in is the review kit's rule and not a fan-out guard's.
 *
 * gov:kit agent-cap@1.48 — the hooks kit's marker, declared in its `marker_carriers`: this pack reads
 * agent-cap.js's exports, so a scoped update of either kit moves both (TOOL-dFairHearing-27 S12).
 *
 * Wiring (per project), through its fragment beside it, which declares the event, the `Workflow`
 * matcher, the marker and the hook path:
 *   python <prefix>/settings-merge.py --fragment <prefix>/workflows/spec-audit-optin.fragment.json
 * A default install lands and wires it through govkit; <prefix>/check-wiring.sh reports it UNWIRED in
 * a tree that unwired it. Blocks via exit 2 + stderr; exits 0 on any other tool and any admitted call.
 *
 * ITS READERS ARE THE HOOKS KIT'S, one copy each: `extractWorkflowArgs` and `extractBuildSlug` from
 * agent-cap.js's exports, `readFrontMatterKey` and `readConfKey` from scratch-guard.js, both read from
 * the directory `resolveKitDir` finds the hooks kit in, as agent-cap finds this pack: the install
 * receipt's row, then the two sibling probes. That location
 * rests on the working-tree receipt, so a forged row chooses the code this pack loads
 * (TOOL-dFairHearing-48 F1). A call it cannot load them for is judged without them: one
 * whose `args` may be a spec audit is DENIED by name, naming the reader, and every other call is
 * admitted, since a missing reader must not turn the one call this rule refuses into an admission.
 */
'use strict'

// Bound by `loadReaders` before the rule runs; the rule reads them by these names.
let extractWorkflowArgs, extractBuildSlug, readFrontMatterKey, readConfKey

// TOOL-dFairHearing-43 S4 - agent-cap.js's resolver, carried inline because the pack needs it to find
// agent-cap.js. `resolve_kit_dir.py` in gov's lib dir is its canonical, and the resolve-python suite
// holds this block byte-identical to the hook's.
// >>> resolveKitDir
function resolveKitDir(home, anchor, here) {
  const path = require('path')
  const fs = require('fs')
  const checkFile = (f) => { try { return fs.statSync(f).isFile() } catch { return false } }
  here = path.resolve(here)
  let root = here
  for (let d = here; ; d = path.dirname(d)) {
    if (fs.existsSync(path.join(d, '.git'))) { root = d; break }
    if (path.dirname(d) === d) break
  }
  const receipt = path.join(root, '.governance', 'install.json')
  let rows = []
  try {
    const data = JSON.parse(fs.readFileSync(receipt, 'utf8'))
    rows = data && typeof data === 'object' && Array.isArray(data.files) ? data.files : []
  } catch { rows = [] }
  for (const row of rows) {
    if (!row || typeof row !== 'object' || Array.isArray(row) || !row.path) continue
    const src = String(row.source || '').split('/')
    const n = src.length
    const made = row.role === 'rendered' && String(row.path).split('/').pop() === anchor
    if (!(n >= 2 && src[n - 2] === home && (src[n - 1] === anchor || made))) continue
    const hit = path.resolve(root, String(row.path))
    const rel = path.relative(root, hit)
    const inside = rel !== '' && !path.isAbsolute(rel) && rel.split(path.sep)[0] !== '..'
    if (checkFile(hit) && inside && !String(row.path).split(/[\\/]/).includes('..')) return path.dirname(hit)
  }
  const probes = [path.join(here, home), path.join(path.dirname(here), home)]
  for (const cand of probes) if (checkFile(path.join(cand, anchor))) return cand
  const renderPosix = (f) => f.split(path.sep).join('/')
  const e = new Error(`no ${home} kit holding ${anchor} in this install: looked in ${renderPosix(receipt)}, ${renderPosix(probes[0])} and ${renderPosix(probes[1])}`)
  e.receipt = receipt
  throw e
}
// <<< resolveKitDir

function loadReaders() {
  const path = require('path')
  const hooksDir = resolveKitDir('hooks', 'agent-cap.js', __dirname)
  for (const [file, names] of [['agent-cap.js', ['extractWorkflowArgs', 'extractBuildSlug']], ['scratch-guard.js', ['readFrontMatterKey', 'readConfKey']]]) {
    const at = path.join(hooksDir, file).split(path.sep).join('/')
    let m
    try { m = require(at) } catch (e) { throw new Error(`${file}'s ${names.join(' and ')} could not be loaded from ${at} (${(e && e.code) || (e && e.message) || e})`) }
    const miss = names.filter((n) => typeof m[n] !== 'function')
    if (miss.length) throw new Error(`${at} exports no ${miss.join(' and ')}`)
    if (file === 'agent-cap.js') ({ extractWorkflowArgs, extractBuildSlug } = m)
    else ({ readFrontMatterKey, readConfKey } = m)
  }
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
// either. Loaded before the rule runs, by `loadReaders`: a withdrawn sibling is a deny, not a crash.
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

// The LAST `SPEC_AUDIT_DEFAULT=` assignment's value in a shell-style conf, as the shell would read
// it: double- or single-quoted or bare, an optional `export`, a trailing `# comment` allowed after
// the value ONLY behind whitespace — a `#` glued to a bare word is part of the word to the shell
// (`2026-09-21#c` is the driver's fail 54), and rev-1 stopped the word there and admitted the date
// (closing review of units 7/8, R8). null when no assignment exists. The value is returned RAW; the
// caller decides whether it is a date, so a blank and a non-date are both visible to it. The grammar
// is the sibling hook's `readConfKey`, the one conf reader in this home (TOOL-aRoutedQuill-2 S9).
function readSpecAuditDefault(bytes) {
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

function main() {
  let data
  try {
    data = JSON.parse(require('fs').readFileSync(0, 'utf8'))
  } catch {
    process.exit(0)
  }
  if (!data || data.tool_name !== 'Workflow') process.exit(0)
  try {
    loadReaders()
  } catch (e) {
    // NO READER, NO PLACEMENT. Without agent-cap's `extractWorkflowArgs` this file cannot tell a spec
    // audit from any other call, so it asks the raw `args` text whether one may be: a mention of the
    // kind or of `specAudit` is denied naming the reader, and every other call is admitted.
    // ponytail: a text test over-reads in a broken install only, a diff review whose args mention the kind; the readers' probe is TOOL-dFairHearing-32's resolver port.
    const raw = data.tool_input && data.tool_input.args
    const text = typeof raw === 'string' ? raw : JSON.stringify(raw === undefined ? null : raw)
    if (!/spec-audit|specAudit/.test(String(text))) process.exit(0)
    process.stderr.write(
      `BLOCKED by spec-audit-optin: ${(e && e.message) || e}, so this Workflow call, whose args may be ` +
        `a spec audit, cannot be judged against its build's opt-in (TOOL-aBlindedTrial-6), and a call ` +
        `this rule cannot judge is not admitted. Install the hooks kit at a place that message names.\n`,
    )
    process.exit(2)
  }
  const deny = checkSpecAuditDeclared(data)
  if (deny) {
    process.stderr.write(deny)
    process.exit(2)
  }
  process.exit(0)
}

module.exports = { checkSpecAuditDeclared, readSpecAuditDefault, NO_AUDIT_PHASES, loadReaders }
if (require.main === module) main()
