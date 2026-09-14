#!/usr/bin/env node
/**
 * scratch-guard — a PreToolUse guard that keeps agent scratch out of the home directory.
 *
 * WHY THIS IS A HOOK AND NOT A RULE. The defect it exists for was eighteen files in the operator's
 * home, written by tool calls shaped like `bash tools/run-gates/run-gates.sh > ~/.merge-bar.log`.
 * No script was involved, so no script could have caught it, and the charter rule against it was
 * loaded in every session that broke it. The tool call is the only surface that sees the act.
 *
 * WHAT IT DENIES. A command whose text names a write target under the operator's home directory
 * that is not under one of the sanctioned scratch roots (`home`); one that creates a NEW top-level
 * entry at a drive root (`drive-root`); one rooted in a temp variable that is EMPTY in this session,
 * so the bytes land at the filesystem root (`empty-var`); one under `/tmp` (`tmp`, an owner ruling —
 * the habit is what is being ended, even on a Git-Bash host where `/tmp` is a mount onto TEMP); and
 * one that creates a new top-level entry at the POSIX root, `/mir/x` (`posix-root`). The CLI's own
 * scratch base, `<os.tmpdir()>/claude`, stays allowed INSIDE the denied `/tmp` prefix, because that
 * is the one destination every agent is told to use and a rule that denies it is the class
 * memory/gotchas/allowlist-narrower-than-the-root-it-guards.md names.
 *
 * THE ALLOWLIST IS DERIVED, NEVER AUTHORED, and that is the whole subtlety of this file. On Windows
 * the scratch roots are INSIDE the home directory: TEMP is C:\Users\<user>\AppData\Local\Temp and
 * the session scratchpad is a subtree of it. A hardcoded `<home>/.claude` allowlist therefore denies
 * every legitimate temp write. Measured during the design pass over 23,966 real Bash tool calls, that
 * spelling produced 123 denials of which 73 were legitimate — including the `export TMPDIR=...`
 * workaround the kickoff manifest itself prescribes. So the roots come from TMPDIR/TEMP/TMP at run
 * time, plus `<home>/.claude`, and the guard self-corrects if any of them ever move.
 *
 * TWO VIEWS OF ONE COMMAND, which is how it avoids denying the prose that describes it. Operators are
 * located in a STRING-BLANKED view, so a `>` inside a quoted argument is invisible; the target is then
 * read from the ORIGINAL text at that offset, so a legitimately quoted redirect target still resolves.
 * Without the first half, `git commit -m "fixes the > ~/.merge-bar.log litter"` is denied. Without the
 * second, `> "$HOME/.x"` is missed. The sibling hook draws the same distinction (agent-cap.js
 * `stripStrings`), for the same reason.
 *
 * ponytail: the predicate is TEXTUAL. It does not resolve a variable, follow a `cd`, or read inside a
 * heredoc'd python script — `cd ~ && echo x > y` walks straight past it. It catches the literal shapes
 * that produced every one of the observed files, which is the job. The upgrade path, if that stops
 * being enough, is a real tokenizer rather than more regexes.
 *
 * FAILS OPEN. Unparseable stdin, an unknown tool, or a missing command all exit 0. This is a hygiene
 * rule, not a containment boundary; a security control would have to fail the other way.
 *
 * Protocol: deny = stderr text + exit 2. Allow = print nothing, exit 0. Matches agent-cap.js, which
 * records the choice as version-robust and free of any JSON-schema dependency.
 */
'use strict'

const KIT_SCRATCH_GUARD_VERSION = '1.0' // gov:kit agent-cap@1.14 — ships inside the hooks kit entry

const TOOLS = ['Bash', 'PowerShell']
const MAX_FINDINGS = 6

function readStdin() {
  try {
    return require('fs').readFileSync(0, 'utf8')
  } catch {
    return ''
  }
}

/**
 * Lower-case, forward-slashed, drive-folded, trailing-slash-free — the one comparable form.
 *
 * The drive fold is load-bearing and was found by the smoke test, not by reasoning. Git-Bash hands a
 * native Windows binary `HOME=C:\Users\<user>` even when the shell itself holds `/c/Users/<user>`,
 * while the commands this hook reads use the MSYS spelling. Without folding `/c/...` onto `c:/...`
 * the roots and the targets are written in two different alphabets, every absolute MSYS home path
 * misses every root, and the guard reports a clean ALLOW — passing for the reason it exists to catch.
 */
function buildComparablePath(p) {
  return String(p || '')
    .replace(/\\/g, '/')
    .replace(/^\/([A-Za-z])\//, '$1:/')
    .replace(/\/+$/, '')
    .toLowerCase()
}

/**
 * Every spelling of the operator's home this machine might use.
 *
 * The 8.3 contraction is not hypothetical: node `a` reports USERPROFILE=C:\Users\daily-agent beside
 * TEMP=C:\Users\DAILY-~1\AppData\Local\Temp, and the real corpus carries both inside one session. So
 * rather than enumerate contractions, every home-ish variable is mined for its `.../users/<name>`
 * prefix — whatever that machine happens to call it.
 */
function resolveHomeRoots(env) {
  const roots = new Set()
  const addRoot = (v) => {
    const c = buildComparablePath(v)
    if (c) roots.add(c)
  }
  addRoot(env.HOME)
  addRoot(env.USERPROFILE)
  for (const v of [env.HOME, env.USERPROFILE, env.TEMP, env.TMP, env.TMPDIR]) {
    const m = buildComparablePath(v).match(/^(.*?\/users\/[^/]+)(?:\/|$)/)
    if (m) roots.add(m[1])
  }
  return [...roots]
}

/** Expand 8.3 to the long form where the path exists. Cheap, and the only fully general answer. */
function resolveRealPath(p) {
  try {
    return require('fs').realpathSync.native(p)
  } catch {
    return ''
  }
}

/**
 * Every spelling of one root, given every spelling of the home it may sit under.
 *
 * MEASURED, not anticipated: the corpus probe over 93,185 real Bash calls produced 259 false
 * positives before this existed. The machine hands `%TEMP%` as C:\Users\DAILY-~1\AppData\Local\Temp
 * while commands write C:/Users/daily-agent/AppData/Local/Temp — one directory, two alphabets, and a
 * prefix test sees two unrelated paths. So each root is also re-spelled under every OTHER known home
 * form, which covers roots that do not exist yet and cannot be realpath'd.
 */
function buildRootVariants(root, homes) {
  const out = new Set([root])
  const real = buildComparablePath(resolveRealPath(root))
  if (real) out.add(real)
  for (const h of homes) {
    if (!checkUnderRoot(root, h)) continue
    const tail = root.slice(h.length)
    for (const other of homes) out.add(other + tail)
  }
  return [...out]
}

/**
 * The sanctioned scratch roots. "scratchpad/temp and nowhere else", derived rather than authored.
 *
 * A temp variable whose value is exactly `/tmp` contributes NO root: the `tmp` rule denies the
 * spelling, and a variable is one more way to spell it. Without this, `TEMP=/tmp` would re-open every
 * `/tmp` write the rule closes — and the rule would have no observable failing case on a Windows
 * node. `/tmp/sub` as a value still joins, because a configured subdirectory is a destination, not
 * the habit. The CLI's scratch base `<os.tmpdir()>/claude` is added whole so a POSIX host whose
 * scratchpad sits under `/tmp` keeps the one destination the owner wants; `os.tmpdir()` ITSELF is
 * not, because that would allow every `/tmp` write on a host with no TMPDIR.
 */
function resolveAllowedRoots(env) {
  const homes = resolveHomeRoots(env)
  const roots = new Set()
  const addRoot = (v) => {
    const c = buildComparablePath(v)
    if (c && c !== '/tmp') for (const variant of buildRootVariants(c, homes)) roots.add(variant)
  }
  for (const v of [env.TMPDIR, env.TEMP, env.TMP]) addRoot(v)
  for (const h of homes) addRoot(h + '/.claude')
  addRoot(require('os').tmpdir() + '/claude')
  return [...roots]
}

/** Boundary-aware, so `~/.claudex` does not pass as `~/.claude`. */
function checkUnderRoot(pathC, rootC) {
  return pathC === rootC || pathC.startsWith(rootC + '/')
}

/**
 * Blank the CONTENTS of quoted strings and heredoc bodies, preserving length so offsets still line
 * up with the original. Operators are then located in this view and targets read from the original.
 */
function buildCommandView(cmd) {
  // `to <= from` is reachable: an EMPTY heredoc body puts the terminator on the line immediately
  // after the opener, so the computed span is -1. Found by the corpus probe, not by reasoning —
  // the smoke fixtures all had non-empty bodies.
  const buildBlankedRun = (s, from, to) =>
    to <= from ? s : s.slice(0, from) + ' '.repeat(to - from) + s.slice(to)
  let view = cmd

  // Heredoc bodies first: their contents can hold anything, including quotes that would desync a
  // naive quote scanner.
  const here = /<<-?\s*(['"]?)([A-Za-z_][A-Za-z0-9_]*)\1/g
  let hm
  while ((hm = here.exec(view)) !== null) {
    const tag = hm[2]
    const bodyStart = view.indexOf('\n', hm.index)
    if (bodyStart === -1) break
    const end = view.slice(bodyStart).search(new RegExp('\\n[ \\t]*' + tag + '[ \\t]*(?:\\n|$)'))
    const bodyEnd = end === -1 ? view.length : bodyStart + end
    view = buildBlankedRun(view, bodyStart + 1, bodyEnd)
    here.lastIndex = bodyEnd
  }

  // Then quoted runs, single and double, left to right.
  let out = ''
  let i = 0
  while (i < view.length) {
    const ch = view[i]
    if (ch === "'" || ch === '"') {
      let j = i + 1
      while (j < view.length && view[j] !== ch) {
        if (ch === '"' && view[j] === '\\') j++
        j++
      }
      const close = j < view.length ? j : view.length
      out += ch + ' '.repeat(Math.max(0, close - i - 1)) + (j < view.length ? ch : '')
      i = close + 1
    } else {
      out += ch
      i++
    }
  }
  return out
}

/** Read the whitespace-delimited token starting at `from` in the ORIGINAL text, unquoted. */
function readTokenAt(cmd, from) {
  let i = from
  while (i < cmd.length && /\s/.test(cmd[i])) i++
  let out = ''
  let quote = ''
  while (i < cmd.length) {
    const ch = cmd[i]
    if (quote) {
      if (ch === quote) quote = ''
      else out += ch
    } else if (ch === "'" || ch === '"') {
      quote = ch
    } else if (/[\s;|&)]/.test(ch)) {
      break
    } else {
      out += ch
    }
    i++
  }
  return out
}

const WRITE_ANY_ARG = /(?:^|[\s;&|(])(tee|touch|mkdir|Out-File|Set-Content|Add-Content|New-Item)\b/g
const WRITE_LAST_ARG = /(?:^|[\s;&|(])(cp|mv|install|rsync)\b/g
const REDIRECT = /(?:^|[\s;&|(])(?:\d?>>?|&>)/g
const TMP_ASSIGN = /(?:^|[\s;&|(])(TMPDIR|TMP|TEMP)=/g

/**
 * Locate write targets. Operators come from the blanked VIEW; the token itself is read from the
 * ORIGINAL, so a quoted target still resolves while a quoted operator stays invisible.
 *
 * `cp`/`mv`/`install`/`rsync` take their LAST argument only — those read a source first, and a
 * home-rooted SOURCE is a read. Getting this wrong would have denied this build's own inventory step.
 */
function scanWriteTargets(cmd) {
  const view = buildCommandView(cmd)
  const found = []
  const addTarget = (value, why) => {
    if (value && !value.startsWith('-')) found.push({ value, why })
  }

  for (const [rx, why] of [[REDIRECT, 'redirect'], [TMP_ASSIGN, 'temp-root assignment']]) {
    rx.lastIndex = 0
    let m
    while ((m = rx.exec(view)) !== null) {
      addTarget(readTokenAt(cmd, m.index + m[0].length), why)
    }
  }

  WRITE_ANY_ARG.lastIndex = 0
  let m
  while ((m = WRITE_ANY_ARG.exec(view)) !== null) {
    let at = m.index + m[0].length
    for (let k = 0; k < 8 && at < cmd.length; k++) {
      const tok = readTokenAt(cmd, at)
      if (!tok) break
      addTarget(tok, m[1])
      at = cmd.indexOf(tok.replace(/^["']|["']$/g, ''), at)
      at = at === -1 ? cmd.length : at + tok.length
    }
  }

  WRITE_LAST_ARG.lastIndex = 0
  while ((m = WRITE_LAST_ARG.exec(view)) !== null) {
    const seg = view.slice(m.index + m[0].length).split(/[;|&]/)[0]
    const args = []
    let at = m.index + m[0].length
    const stop = at + seg.length
    while (at < stop) {
      const tok = readTokenAt(cmd, at)
      if (!tok) break
      args.push({ tok, at })
      const hit = cmd.indexOf(tok.replace(/^["']|["']$/g, ''), at)
      at = hit === -1 ? stop : hit + tok.length
    }
    const last = args.filter((a) => !a.tok.startsWith('-')).pop()
    if (last) addTarget(last.tok, m[1] + ' destination')
  }
  return found
}

/**
 * A target that OPENS with one of the temp variables: `$TMPDIR/x`, `${TMP}/x`, `${TEMP:-/tmp}/x`.
 * Longest name first so `$TMP` cannot claim `$TMPDIR`; the lookahead keeps `$TMPX/x` out.
 */
const TEMP_VAR = /^\$\{?(TMPDIR|TMP|TEMP)(?::-([^}]*))?\}?(?=\/|$)/

/**
 * Expand the symbolic home spellings, and a leading temp variable, so a target can be compared
 * against the resolved roots. A non-empty variable becomes its value; an empty one with a spelled
 * `:-default` becomes the default (the shell would write there); an empty one with no default is
 * left as written, which is the `empty-var` rule's case and never reaches here.
 */
function buildResolvedTarget(value, env) {
  const home = (resolveHomeRoots(env)[0] || '')
  let v = String(value)
  if (v.startsWith('~/') || v === '~') v = home + v.slice(1)
  v = v.replace(/^\$\{HOME\}/, home).replace(/^\$HOME/, home)
  const t = TEMP_VAR.exec(v)
  if (t && (env[t[1]] || t[2] !== undefined)) v = (env[t[1]] || t[2]) + v.slice(t[0].length)
  return buildComparablePath(v)
}

/**
 * Does this target open with a temp variable that is EMPTY or UNSET in this hook's environment? The
 * variable NAME when it does, '' otherwise. `cp x $TMPDIR/y` with TMPDIR empty lands at `/y` — the
 * incident that motivated the rule was a backup written to the filesystem root on a Windows node.
 *
 * A variable the SAME command assigns (`TMP=$(mktemp -d); echo x > $TMP/f`) is not graded: its
 * value is unknowable textually, and the hook is fail-open on what it cannot read. A `:-default`
 * form is not this rule's either — the expansion above resolves it and the later rules grade it.
 */
function checkEmptyTempVar(value, env, view) {
  const m = TEMP_VAR.exec(String(value))
  if (!m || m[2] !== undefined || env[m[1]]) return ''
  return new RegExp('(?:^|[\\s;&|(])' + m[1] + '=').test(view) ? '' : m[1]
}

/** Under `/tmp`, boundary-aware, on the comparable form — `/tmpx` is not `/tmp`. */
function checkTmpRoot(resolved) {
  return checkUnderRoot(resolved, '/tmp')
}

/**
 * The conventional top-level names at a drive root. A write that creates a NEW sibling of these is
 * the litter class; a write UNDER one of them is somebody's ordinary working path and is none of
 * this guard's business.
 *
 * Hand-listed on purpose, unlike the scratch roots above: this is a fact about how a filesystem is
 * conventionally laid out, not about how THIS machine is configured, so there is nothing to derive
 * it from at run time. A name missing from the list costs one denial with a message naming the fix.
 */
const DRIVE_ROOT_CONVENTIONAL = new Set([
  'users', 'projects', 'windows', 'programdata', 'tmp', 'temp', 'perflogs', 'msys64', 'git',
  'program files', 'program files (x86)', '$recycle.bin', 'system volume information', 'recovery',
  'dev', 'proc', 'sys', 'etc', 'usr', 'var', 'opt', 'home', 'mnt', 'bin', 'sbin', 'lib', 'run',
])

/**
 * Does this target CREATE A NEW TOP-LEVEL ENTRY AT A DRIVE ROOT? `c:/gvi`, not `c:/projects/x`.
 *
 * WHY THIS IS A SECOND RULE AND NOT A WIDER FIRST ONE. The rule above is scoped to the home
 * directory because that is where the observed defect was. Everything outside home was therefore
 * unguarded, and an agent building a throwaway adopter fixture wrote 7.2 MB to `C:\gvi` — outside
 * the repo, outside the scratchpad, and outside this guard. It blocked a build for two hours.
 *
 * THE OBVIOUS WIDENING IS WRONG AND WAS MEASURED WRONG. "Deny any absolute write outside the repo,
 * the scratch roots and home" hits 2,449 distinct targets across 128,568 real tool calls in this
 * operator's history, almost all of them `/tmp/...` — a legitimate scratch root on every POSIX
 * machine. That predicate would red constantly and be turned off within a day.
 *
 * The NARROW one hits 16 calls across 10 targets in that same corpus — `/c/t2`, `/c/gvi`, `/c/gvt`,
 * `/c/gkt`, `/c/gk2`, `/c/gfclone`, `/c/temp-hyg.txt` — and every single one is agent throwaway.
 * ZERO legitimate uses. That is the whole justification for the shape of this predicate: it was
 * chosen by measuring two candidates against the real corpus, not by reasoning about which felt
 * safer. `memory/gotchas/` has the class; the numbers are in this build's records.
 */
function checkDriveRootLitter(resolved) {
  const m = /^([a-z]:)\/([^/]+)(\/.*)?$/.exec(resolved)
  if (!m) return false
  return !DRIVE_ROOT_CONVENTIONAL.has(m[2])
}

/**
 * The drive set's POSIX sibling, hand-listed for the same reason. `tmp` and `temp` are ABSENT on
 * purpose: a `/tmp` target that somehow escaped the `tmp` rule is still litter here, so the two
 * rules cannot disagree. Measured 2026-09-14 over 55,231 real Bash calls on node `a`: four targets,
 * `/mir` and `/xj` among them, every one agent throwaway.
 */
const POSIX_ROOT_CONVENTIONAL = new Set([
  'dev', 'proc', 'sys', 'usr', 'etc', 'var', 'opt', 'home', 'root', 'mnt', 'media', 'srv', 'bin',
  'sbin', 'lib', 'lib64', 'run', 'boot', 'private', 'volumes', 'cygdrive', 'workspace', 'workspaces',
])

/**
 * Does this target CREATE A NEW TOP-LEVEL ENTRY AT THE POSIX ROOT? `/mir/x`, not `/usr/local/x`.
 * A one-character top is a drive spelled without its slash (`/c`) and is the drive rule's business;
 * a UNC path (`//server/share`) has an empty first segment and never matches.
 */
function checkPosixRootLitter(resolved) {
  const m = /^\/([^/]+)(\/.*)?$/.exec(resolved)
  if (!m || m[1].length === 1) return false
  return !POSIX_ROOT_CONVENTIONAL.has(m[1])
}

function checkCommand(cmd, env) {
  const homes = resolveHomeRoots(env)
  const allowed = resolveAllowedRoots(env)
  const view = buildCommandView(cmd)
  const symbolic = /^(~(\/|$)|\$HOME(\/|$)|\$\{HOME\}(\/|$))/
  const bad = []
  for (const t of scanWriteTargets(cmd)) {
    // FIRST RULE THAT CLAIMS A TARGET WINS, so the kinds are disjoint by construction and the
    // per-kind sentence in the message is unambiguous. `empty-var` is decided on the RAW value,
    // before resolution, because an empty variable leaves nothing to resolve.
    const emptyVar = checkEmptyTempVar(t.value, env, view)
    let kind = emptyVar ? 'empty-var' : ''
    if (!kind) {
      const resolved = buildResolvedTarget(t.value, env)
      if (allowed.some((a) => checkUnderRoot(resolved, a))) continue
      const isHome = symbolic.test(t.value) || homes.some((h) => checkUnderRoot(resolved, h))
      // A drive-root target has a drive letter and a POSIX-root target has none, so neither is
      // ever under home and no two of these can fire on one target.
      kind = checkTmpRoot(resolved) ? 'tmp'
        : isHome ? 'home'
          : checkDriveRootLitter(resolved) ? 'drive-root'
            : checkPosixRootLitter(resolved) ? 'posix-root' : ''
      if (!kind) continue
    }
    bad.push(Object.assign({}, t, { kind, name: emptyVar }))
    if (bad.length >= MAX_FINDINGS) break
  }
  return { bad, allowed }
}

// FIVE RULES, FIVE SENTENCES. One message covering them all would have to say "home directory or
// drive root or ...", which names none accurately and leaves the reader working out which they hit.
const KIND_WHAT = {
  home: 'writes into the home directory',
  'drive-root': 'creates a NEW TOP-LEVEL entry at a drive root',
  'empty-var': 'writes through a temp variable that is EMPTY in this session',
  tmp: 'writes under /tmp',
  'posix-root': 'creates a NEW TOP-LEVEL entry at the POSIX root',
}

function renderDeny(bad, allowed) {
  const lines = bad.map((b) => `  ${b.why}: ${b.value}`).join('\n')
  const roots = allowed.length ? allowed.map((a) => `  ${a}`).join('\n') : '  (none resolved)'
  const kinds = [...new Set(bad.map((b) => b.kind))]
  const what = kinds.map((k) => KIND_WHAT[k]).join(' AND ')
  const names = [...new Set(bad.filter((b) => b.kind === 'empty-var').map((b) => '$' + b.name))].join(', ')
  return (
    `BLOCKED by scratch-guard: this command ${what}, outside every sanctioned scratch root.\n\n` +
    lines +
    '\n\nScratch belongs in the session scratchpad or the temp root; durable gate evidence already ' +
    'goes to <git-dir>/gate-logs/. Writable roots resolved on this machine:\n' +
    roots +
    '\n\nIf you need a log to outlive a backgrounded call, put it under one of those.' +
    (kinds.includes('drive-root')
      ? '\n\nA throwaway repo or fixture goes in the scratchpad, never at `C:/<name>` — that litter ' +
        'survives the session, is invisible to every gate, and nobody cleans it up. If the name you ' +
        'used is a real conventional root on this machine, add it to DRIVE_ROOT_CONVENTIONAL.'
      : '') +
    (kinds.includes('empty-var')
      ? `\n\n${names} is EMPTY in this session, so the write lands at the filesystem root. Spell the ` +
        'target under the session scratchpad, absolute, never through a temp variable you have not checked.'
      : '') +
    (kinds.includes('tmp')
      ? '\n\n/tmp is not a sanctioned destination on this machine: the session scratchpad and the temp ' +
        'root are the two that are. Spell the target under the scratchpad.'
      : '') +
    (kinds.includes('posix-root')
      ? '\n\nThe target creates a new top-level entry at the POSIX root, beside /usr and /etc — litter ' +
        'that survives the session. If the name you used is a real conventional root on this machine, ' +
        'add it to POSIX_ROOT_CONVENTIONAL.'
      : '') +
    '\n'
  )
}

function main() {
  let data
  try {
    data = JSON.parse(readStdin())
  } catch {
    process.exit(0)
  }
  if (!data || !TOOLS.includes(data.tool_name)) process.exit(0)
  const cmd = (data.tool_input && data.tool_input.command) || ''
  if (!cmd) process.exit(0)

  // The predicate is wrapped because a hygiene guard that THROWS is worse than one that misses: an
  // uncaught error exits 1, which surfaces noise on a command that was probably fine. Fail open and
  // stay consistent with the stdin handling above. The self-test pins this arm so the catch cannot
  // quietly become the normal path.
  let verdict
  try {
    verdict = checkCommand(cmd, process.env)
  } catch {
    process.exit(0)
  }
  if (verdict.bad.length === 0) process.exit(0)
  process.stderr.write(renderDeny(verdict.bad, verdict.allowed))
  process.exit(2)
}

if (require.main === module) main()
module.exports = { checkCommand, buildCommandView, resolveAllowedRoots, KIT_SCRATCH_GUARD_VERSION }
