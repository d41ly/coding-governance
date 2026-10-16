#!/usr/bin/env node
/**
 * scratch-guard — a PreToolUse guard that keeps agent scratch out of the home directory.
 *
 * WHY THIS IS A HOOK AND NOT A RULE. The defect it exists for was eighteen files in the operator's
 * home, written by tool calls shaped like `bash <prefix>/run-gates/run-gates.sh > ~/.merge-bar.log`.
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
 * ponytail: the predicate is TEXTUAL. It resolves no variable beyond `~`, `$HOME` and the three temp
 * spellings, follows no `cd`, and reads nothing inside a heredoc'd python script — `cd ~ && echo x > y`
 * walks straight past it. It catches the literal shapes that produced every one of the observed
 * files, which is the job. The upgrade path, if that stops being enough, is a real tokenizer rather
 * than more regexes.
 *
 * FAILS OPEN. Unparseable stdin, an unknown tool, or a missing command all exit 0. This is a hygiene
 * rule, not a containment boundary; a security control would have to fail the other way. The THIRD
 * check below, the write gate, is one exception: it fails closed. The role-gate arm is the other,
 * for a payload carrying an `agent_type` only.
 *
 * Protocol: deny = stderr text + exit 2. Allow = print nothing, exit 0. Matches agent-cap.js, which
 * records the choice as version-robust and free of any JSON-schema dependency — with ONE departure,
 * stated next: the orientation check below writes a WITNESS line on some exit-0 paths.
 *
 * THE SECOND CHECK: ORIENTATION (TOOL-aReplayedCard-1). After the scratch verdict, a `git commit`
 * issued by the main loop is refused while this session's orientation card — written by the kickoff
 * kit's `manifest-check.sh --card --write` at session start, under `<git-common-dir>/orientation/`
 * — still holds the writer's sentinel `READY — none yet`, or names a different tree than the one
 * the commit targets. The remedy is in the reason: `/session-kickoff`, from the target tree when the
 * trees differ. `checkOriented` is the predicate and its comment is the ONE evaluation order.
 *
 * WHAT ESCAPES IT, so nobody reads this as containment: a commit made by a script, a heredoc, a
 * non-git tool, a `$(git commit)` (the token must be followed by whitespace or the end); a deleted
 * card, a hand-written card, a card the writer refused to write, a `cd`/`-C` target that is not a
 * literal path or does not exist (the last `cd <dir>` before the git token IS read, F3), and a
 * session that started before the wiring and never restarted — an ABSENT card and a card the replay
 * wrote fresh (`--card --replay` in its header) both ALLOW, because a session the writer never ran
 * for cannot run the remedy. The guard stops forgetting, not evasion. A READY line's PRESENCE is
 * asserted, never its correctness. `--git-dir` or `--work-tree` pointing outside the resolved tree
 * is compared as the resolved tree. The drive fold lowercases, so on a case-SENSITIVE filesystem the
 * walk finds no `.git` and allows with the witness line — every registered node is Windows.
 *
 * THE WITNESS LINES depart from "Allow = print nothing" above: an absent card, a replay-written
 * card, an unwalkable target and the README exemption each write one line to stderr and exit 0.
 * The harness discards stderr on exit 0, so those lines reach the debug log and the self-test and
 * NOBODY ELSE; a present `--write` card that passes prints nothing. Nothing here claims more.
 *
 * THE THIRD CHECK: THE WRITE GATE (TOOL-aRoutedQuill-2). An Edit, Write, MultiEdit or NotebookEdit
 * whose target lies under the repository's declared product paths — `ROUTED_PATHS` in the target
 * toplevel's `.memory-tree.conf` — is refused unless this session's orientation card carries a
 * `## route` naming a unit whose spec is BUILDABLE: Tier-2 at INPROGRESS, Tier-1 at INPROGRESS, or
 * Tier-1 at SPECCED once `SPEC_TIER1_CUTOFF` graded it. `checkRouted` is the predicate and its
 * comment is the ONE evaluation order. It binds a subagent exactly as the main loop: a subagent's
 * payload carries the parent's `session_id` (measured, the aRoutedQuill probe record), so it reads
 * the parent's card. A conf that declares MEMORY_ROOT or ROUTED_PATHS blank, or an entry that is
 * absolute, climbs through `..` or covers MEMORY_ROOT, is UNARMED: every write in that repository
 * refuses except one to the conf. A target in no repository, or in one that is not the session's,
 * is not gated; neither is a repository with no conf (one witness line).
 *
 * WHAT ESCAPES THE WRITE GATE — it stops forgetting, not evasion: a Bash or PowerShell write (`sed
 * -i`, an interpreter, a redirect) is never seen, and the push-time leg owns that guarantee; a
 * hook-less or `--bare` run fires no hook; a narrowed ROUTED_PATHS is a conf diff, not a refusal; a
 * hand-written card with a `## route` is read like the writer's; and a spec status flipped to
 * INPROGRESS without the owner's approval admits, because the gate reads a status the agent writes.
 *
 * THE ROLE ARM (TOOL-aOrientedCast-6). The same gate reads WHO writes, from the payload's
 * `agent_type`, against the role index `.claude/roles.json` at the target toplevel (`loadRoleIndex`,
 * exported so agent-cap.js reads the index through this one reader). A write under
 * `<MEMORY_ROOT>/builds/<build>/spec/` is admitted only from a role declaring `writes = spec`; a
 * product write admitted by the route arm above is then admitted only from a role declaring
 * `writes = product`. The main loop, which carries no `agent_type`, and an untyped harness agent
 * (`workflow-subagent`) are refused both — except a spec edit that moves only the status and date
 * cells of its `**Status:**` line, admitted from the main loop and from a `product` role on a spec
 * its card routes. An ABSENT index adds no arm; a broken one refuses both classes; an index naming
 * no writer for a class refuses that class as UNARMED. What escapes it, besides everything that
 * escapes the gate: a hand-edited index, and a session launched AS a role, whose payload carries
 * that role's type. It grades two write classes; `none`, `review` and `records` are declared in the
 * index and read by nothing here.
 *
 * THE FOURTH CHECK: THE ROLE-GATE ARM (TOOL-aOrientedCast-11). Gates are the main session's, at the
 * merge or push threshold. On a Bash or PowerShell payload carrying an `agent_type`, AFTER the
 * scratch verdict and the orientation check, `checkRoleGate` refuses a simple command that runs a
 * gate the role's allowlist does not name: G1, the argv of a leg of the gate manifest the role
 * index names (`gates.manifest`), compared word for word from its script on; G2, the bar runner,
 * the self-test runner or the unattended gates runner, by basename, in any form; G3, a `*.test.sh`
 * or `*selftest.py` script, or a script carrying `--selftest`, unless it carries `--render`,
 * `--list` or `--help`. The allowlist is the index's `gates` list for that type, rendered from the
 * roles kit's policy; a type the index does not name, `workflow-subagent` among them, may run
 * nothing. `checkRoleGate` is the predicate and its comment is the ONE evaluation order. A
 * launcher's options and a prefix word's options are stepped past by `GATE_OPTION_RULES`
 * (TOOL-aOrientedCast-14): an option that takes an argument takes it, a shell's `-n`, a Python `-c`
 * or `-m`, a Node `-e` or `-p` and `command -v` end the command, and a shell's `-c` and `env -S`
 * scan their body once. The index is read at the checkout root of the payload `cwd`, else of
 * `CLAUDE_PROJECT_DIR`; neither resolving adds no arm, with one witness line when
 * `CLAUDE_PROJECT_DIR` is set. An absent
 * index adds no arm; a broken one refuses a candidate; a manifest that does not read leaves G1
 * unarmed with one witness line while G2 and G3 bind; a throw refuses a role agent. THE CEILING:
 * the match is textual, so a gate reached through an interpreter, an alias, a function, an
 * assembled path, a `$(…)` inside quotes, a scoped variant of a leg with an extra argument, or an
 * option missing from the table that takes an argument (`bash -eo pipefail` among them, since only
 * a bare `-o` is in the table) passes it. It stops forgetting, not evasion, and the push-boundary
 * bar is still the guarantee.
 *
 * THE THIRD EVENT: SUBAGENTSTART (TOOL-aRoutedQuill-4). A subagent inherits the hooks but not the
 * parent's card, so it would meet the write gate blind. Wired by `scratch-guard-subagent.fragment.json`
 * (matcher `*`), a payload whose `hook_event_name` is `SubagentStart` is answered on stdout with
 * `hookSpecificOutput.additionalContext`: the card's `## route` lines byte for byte, each routed unit's
 * `checkBuildable` verdict, and what the gate refuses under `ROUTED_PATHS`. `renderRouteContext` is
 * the predicate and its comment is the ONE evaluation order. Its silence rules: nothing when the
 * session directory is in no repository or its toplevel holds no conf (the gate admits every write
 * there); ONE line when the conf is unreadable or UNARMED, or the session routes no unit. Every
 * sentence states what holds and none directs, because injected imperatives can trip a model's
 * prompt-injection defences. Capped at ROUTE_CONTEXT_CAP characters, the harness's own cap: route
 * lines are cut at a line boundary and a closing line counts what was left out. It never blocks and
 * never surfaces an error: a throw prints nothing and exits 0.
 */
'use strict'

const KIT_SCRATCH_GUARD_VERSION = '1.2' // gov:kit agent-cap@1.40 — ships inside the hooks kit entry

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
 *
 * The set must be as wide as the roots it guards, and `private` and `volumes` put macOS in scope
 * while `users`, `applications`, `library` and `system` — the other four names every macOS root
 * carries — were missing, so `echo x > /Users/Shared/f` was denied as NEW top-level litter on a
 * host where `/Users` is where every home lives (the drive set already lists `users`, and
 * `resolveHomeRoots` mines `/users/<name>` homes). `nix` and `snap` are the same class on Linux:
 * a package-manager root that is conventional on every host that has it. No registered node is
 * macOS; the kit is copy-installed and project-agnostic, which is why the list is wider than the
 * corpus that measured it. Closing diff review round 1, cluster J.
 */
const POSIX_ROOT_CONVENTIONAL = new Set([
  'dev', 'proc', 'sys', 'usr', 'etc', 'var', 'opt', 'home', 'root', 'mnt', 'media', 'srv', 'bin',
  'sbin', 'lib', 'lib64', 'run', 'boot', 'private', 'volumes', 'cygdrive', 'workspace', 'workspaces',
  'users', 'applications', 'library', 'system', 'nix', 'snap',
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

// ---- the orientation check ---------------------------------------------------------------------

/** The seven git global options that take the NEXT token as their value unless written `--x=v`. */
const GIT_VALUE_FLAGS = ['-C', '-c', '--git-dir', '--work-tree', '--namespace', '--exec-path', '--config-env']
/**
 * A token of the string-blanked VIEW: a quoted run whose bytes were blanked (so a space inside it is
 * not a boundary) or a run of bare characters, in any mix. `git -C "C:/p q" commit` is four tokens.
 */
const VIEW_TOKEN = `(?:"[^"]*"|'[^']*'|[^\\s"'])+`
const VALUE_FLAG = `(?:${GIT_VALUE_FLAGS.join('|')})`
/**
 * The argv token `git`, then any number of dash-prefixed tokens — each value flag taking its one
 * value token, and REFUSED as a bare dash token so `git -C commit -m y` is a directory named
 * `commit` and not a commit — then the whole token `commit` followed by whitespace or the end.
 * `merge-base`, `commit-tree`, `log --grep commit` and a quoted `commit` never match; `merge` and
 * `push` are deliberately outside the set (the engine's own fast-forward is a `merge --ff-only`).
 */
const COMMIT_SHAPED = new RegExp(
  `(?:^|[\\s;&|(])git(?:\\s+(?:${VALUE_FLAG}\\s+${VIEW_TOKEN}|(?!${VALUE_FLAG}(?:\\s|$))-${VIEW_TOKEN}))*\\s+commit(?=\\s|$)`
)
/** The `authorized-by:` values that exempt a NEW build README — the unattended driver's own set. */
const ANCHOR_MODES = ['prompt', 'recipe']
const SENTINEL = 'READY — none yet'

/**
 * The directories the commit's tree resolves through, in order: the LAST `cd <dir>` before the git
 * token (`cd <tree> && git commit` is the compound shape a session that opens at the worktrees'
 * parent writes — it was judged against the payload cwd, a wrong deny in one direction and a silent
 * cross-tree allow in the other; the aReplayedCard closing review, F3), then every `-C` value inside
 * the matched span. Each is read from the ORIGINAL at the offset the view located.
 */
function extractCommitTarget(cmd, view, from, to) {
  const out = []
  const cdRx = /(?:^|[\s;&|(])cd\s+/g
  const before = view.slice(0, from)
  let m
  let cd = null
  while ((m = cdRx.exec(before)) !== null) cd = readTokenAt(cmd, m.index + m[0].length)
  if (cd !== null) out.push(cd)
  const rx = /(?:^|\s)-C\s+/g
  const span = view.slice(from, to)
  while ((m = rx.exec(span)) !== null) out.push(readTokenAt(cmd, from + m.index + m[0].length))
  return out
}

/**
 * A target the walk must not resolve: empty (`cd &&`), `-` (OLDPWD), or one the shell would expand
 * (`$ROOT`, `~/x`, `${X}`, a backtick) — `path.resolve` then names a directory that does not exist
 * and the walk lands on the nearest ancestor's `.git`, which in a `.claude/worktrees/` layout is the
 * PRIMARY tree (F4). Such a target, like one absent from disk, is a witness, never a verdict.
 */
function checkUnwalkableTarget(tok) {
  return tok === '' || tok === '-' || /^[$~]|\$\{|`/.test(tok)
}

/** Walk up from a drive-folded start to the directory holding `.git` — the toplevel — or null. */
function resolveToplevel(start) {
  const fs = require('fs')
  const path = require('path')
  let dir = path.resolve(start)
  for (let i = 0; i < 64; i++) {
    const g = path.join(dir, '.git')
    let st = null
    try { st = fs.statSync(g) } catch { st = null }
    if (st) return { toplevel: dir, gitPath: g, isFile: st.isFile() }
    const up = path.dirname(dir)
    if (up === dir) return null
    dir = up
  }
  return null
}

/**
 * The common dir: the `.git` directory itself, or — in a linked worktree, where `.git` is a FILE —
 * its `gitdir:` target's `commondir`, relative paths resolved against each. The same walk as
 * agent-cap.js makes for its slot ledger, and the branch every real session in this repo takes.
 */
function resolveCommonDir(hit) {
  const fs = require('fs')
  const path = require('path')
  if (!hit.isFile) return hit.gitPath
  const m = /gitdir:\s*(.+)/.exec(fs.readFileSync(hit.gitPath, 'utf8'))
  if (!m) return null
  const gd = path.resolve(hit.toplevel, m[1].trim())
  try {
    return path.resolve(gd, fs.readFileSync(path.join(gd, 'commondir'), 'utf8').trim())
  } catch {
    return gd
  }
}

/** The card's bytes, or `text: null` when none exists, with `shown` its one comparable spelling; a non-id-shaped session id is never joined into a path. */
function readCard(commonDir, sessionId) {
  const fs = require('fs')
  const path = require('path')
  const sid = String(sessionId)
  const card = { path: path.join(commonDir, 'orientation', sid + '.md'), text: null }
  card.shown = buildComparablePath(card.path)
  if (!/^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(sid)) return card
  try { card.text = fs.readFileSync(card.path, 'utf8') } catch { /* absent */ }
  return card
}

/**
 * The ONE front-matter reader both hooks in this home use: the single-token value of `<key>:` on
 * its own line inside a build README's front matter, or null. FRONT MATTER ONLY — the slice between
 * the opening `---` on line 1 and the next `---` line, the scope the unattended driver reads its
 * keys in. Matching the whole file exempted a README whose BODY carried `authorized-by:` in a fenced
 * example while the driver authorized nothing (F10); agent-cap.js's spec-audit rule reads
 * `spec-audit:` through the same slice for the same reason (TOOL-aBlindedTrial-4). Takes BYTES, not
 * a path, because the staged-blob caller below has no file on disk to name. The key is compared as
 * a string, never interpolated into a regex (the `conf-value-interpolated-into-a-regex` class).
 */
function readFrontMatterKey(bytes, key) {
  const fm = /^---[ \t]*\r?\n([\s\S]*?)\r?\n---[ \t]*(?:\r?\n|$)/.exec(bytes || '')
  if (!fm) return null
  for (const line of fm[1].split(/\r?\n/)) {
    const m = /^([^:\s]+):[ \t]*(\S+)[ \t]*$/.exec(line)
    if (m && m[1] === key) return m[2]
  }
  return null
}

/**
 * S4's exemption: the commit that CREATES the authorization. A `README.md` directly under a
 * `builds/<one>/` segment, NEW — staged as added, or untracked (the single-call `git add … &&
 * git commit` form has an empty index at PreToolUse) — whose bytes carry `authorized-by:` with a
 * value in ANCHOR_MODES. Git runs at the resolved toplevel; the pathspec is a coarse filter and the
 * regex is the rule, so `rebuilds/z/`, `builds/a/b/` and `docs/` never exempt. The staged BLOB is
 * read for a staged file, never the worktree copy. A folder already in HEAD exempts nothing.
 */
function checkAuthorizedReadme(toplevel) {
  const fs = require('fs')
  const path = require('path')
  const { spawnSync } = require('child_process')
  const runGit = (args) => spawnSync('git', args, { cwd: toplevel, encoding: 'utf8' })
  const readPaths = (args) => {
    const r = runGit(args)
    return r.status === 0 ? r.stdout.split(/\r?\n/).filter((p) => /(^|\/)builds\/[^/]+\/README\.md$/.test(p)) : []
  }
  const readMode = (bytes) => {
    const v = readFrontMatterKey(bytes, 'authorized-by')
    return v && ANCHOR_MODES.includes(v) ? v : null
  }
  for (const p of readPaths(['diff', '--cached', '--name-only', '--diff-filter=A', '--', '*builds/*/README.md'])) {
    const r = runGit(['show', ':' + p])
    const mode = r.status === 0 ? readMode(r.stdout) : null
    if (mode) return { path: p, mode }
  }
  for (const p of readPaths(['ls-files', '--others', '--exclude-standard', '--', '*builds/*/README.md'])) {
    let bytes = ''
    try { bytes = fs.readFileSync(path.join(toplevel, p), 'utf8') } catch { continue }
    const mode = readMode(bytes)
    if (mode) return { path: p, mode }
  }
  return null
}

function renderOrientationDeny(card, condition, cardTree, here) {
  const remedy = buildComparablePath(cardTree) === here ? '/session-kickoff' : `cd ${here} && /session-kickoff`
  const what = condition === 'sentinel'
    ? `holds the writer's sentinel \`${SENTINEL}\` and no real READY line — this session has not kicked off`
    : `names tree ${cardTree || '(none)'} and this commit targets ${here} — the card was written in another tree`
  return (
    `BLOCKED by scratch-guard: orientation card ${card.shown} ${what}.\n\n` +
    `Run ${remedy} before this session's first commit: the kickoff's --card --append writes the READY ` +
    'line and rewrites the card\'s tree cell to the tree it runs in. A subagent, a session with no card, ' +
    `and a commit that CREATES a build README declaring authorized-by: ${ANCHOR_MODES.join(' or ')} are not gated.\n`
  )
}

/**
 * THE ONE EVALUATION ORDER, each step allowing on its own condition. Returns null to print nothing,
 * `{ witness }` to allow with one stderr line, `{ deny }` to refuse.
 *  1. not a `git commit` by COMMIT_SHAPED → null
 *  2. `agent_id` present → null (a subagent's shell calls are never gated)
 *  3. `session_id` or `cwd` missing → null, silently; `tool_use_id` is not read
 *  4. a `cd`/`-C` target that is not a literal path, does not exist, or — drive-folded — walks to
 *     no `.git` → witness (a walk from a missing start would land on an ancestor's `.git`)
 *  5. no card for this session, or a replay-written one → witness
 *  6. a real READY line AND the card's tree equals the resolved toplevel → null
 *  7. a NEW authorized README (checkAuthorizedReadme — the only step that spawns) → witness; else deny
 */
function checkOriented(cmd, data) {
  const path = require('path')
  const view = buildCommandView(cmd)
  const m = COMMIT_SHAPED.exec(view)
  if (!m) return null
  if (data.agent_id) return null
  if (!data.session_id || !data.cwd) return null
  const targets = extractCommitTarget(cmd, view, m.index, m.index + m[0].length)
  const unwalkable = targets.find(checkUnwalkableTarget)
  if (unwalkable !== undefined) return { witness: `orientation not checked — target ${unwalkable || '(empty)'} is not a literal path; git will refuse the commit itself, or resolve it where this hook cannot` }
  const start = path.resolve(buildComparablePath(data.cwd), ...targets.map(buildComparablePath))
  if (!require('fs').existsSync(start)) return { witness: `orientation not checked — target ${buildComparablePath(start)} does not exist; git will refuse the commit itself` }
  const hit = resolveToplevel(start)
  if (!hit) return { witness: `orientation not checked — no .git above ${buildComparablePath(start)}, git will refuse the commit itself` }
  const common = resolveCommonDir(hit)
  if (!common) return { witness: `orientation not checked — ${hit.gitPath} names no gitdir` }
  const card = readCard(common, data.session_id)
  if (card.text === null) return { witness: `orientation card absent — ${card.shown}; the session started before the writer was wired, or is not a kickoff-kit session` }
  const lines = card.text.split(/\r?\n/)
  if (/--card --replay(\s|$)/.test(lines[0])) return { witness: `orientation card replay-written — ${card.shown}; the session started before the writer was wired` }
  // The optional leading `- ` is the charter's [r1] rule: an emitted micro-format is a markdown list
  // item, while the writer's sentinel and every card already on disk are bare. Both forms are read
  // here for the same reason the writer reads both — a card that OBEYS the charter must not look
  // like one that never kicked off (TOOL-cMendedVintage-16).
  const ready = lines.some((l) => { const s = l.replace(/^- /, ''); return s.startsWith('READY — ') && s.trim() !== SENTINEL })
  const treeLine = lines.find((l) => l.startsWith('tree — '))
  const cardTree = treeLine ? treeLine.slice('tree — '.length).split(' · ')[0] : ''
  const here = buildComparablePath(hit.toplevel)
  if (ready && buildComparablePath(cardTree) === here) return null
  const auth = checkAuthorizedReadme(hit.toplevel)
  if (auth) return { witness: `orientation exempt — ${auth.path} creates a build authorized-by: ${auth.mode}` }
  return { deny: renderOrientationDeny(card, ready ? 'tree' : 'sentinel', cardTree, here) }
}

// ---- the write gate (TOOL-aRoutedQuill-2) -------------------------------------------------------

const WRITE_TOOLS = ['Edit', 'Write', 'MultiEdit', 'NotebookEdit']
/** The statuses that admit a write, per tier. A Tier-1 SPECCED admits only when graded (F4). */
const BUILDABLE_STATUS = { 'Tier-1': ['INPROGRESS', 'SPECCED'], 'Tier-2': ['INPROGRESS'] }
/** The memory-tree conf at the target's toplevel; precedent for a root-level conf literal: agent-cap.js. */
const ROUTE_CONF = '.memory-tree.conf'

/**
 * The LAST `<key>=` assignment's value in a shell-style conf, as the shell reads it: double- or
 * single-quoted or bare, an optional `export`, a trailing `# comment` only behind whitespace — a `#`
 * glued to a bare word is part of the word. null when no assignment exists; the value is RAW. The
 * key is compared as a string and never put into a regex (`conf-value-interpolated-into-a-regex`).
 * Lifted from agent-cap.js's `readSpecAuditDefault`, which now delegates here: one conf grammar
 * in this home. Ceiling: a multi-line quoted value elsewhere in the conf can hold a line that
 * reads as an assignment; the shell would not read it so.
 */
function readConfKey(bytes, key) {
  let v = null
  for (const line of String(bytes || '').split(/\r?\n/)) {
    const m = /^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=(?:"([^"]*)"|'([^']*)'|(\S*))(?:\s+#.*)?\s*$/.exec(line)
    if (m && m[1] === key) v = m[2] !== undefined ? m[2] : m[3] !== undefined ? m[3] : m[4]
  }
  return v
}

/** An MSYS drive spelling (`/c/x`) folded to the native one on Windows, case kept, for the walk. */
function buildNativePath(p) {
  return process.platform === 'win32' ? String(p).replace(/^\/([A-Za-z])(\/|$)/, '$1:/') : String(p)
}

/** The common dir in comparable form, 8.3 names expanded, or '' when `start` walks to no `.git`. */
function resolveComparableCommon(start) {
  const hit = resolveToplevel(start)
  if (!hit) return { hit: null, common: '', key: '' }
  const common = resolveCommonDir(hit)
  if (!common) return { hit, common: '', key: '' }
  return { hit, common, key: buildComparablePath(resolveRealPath(common) || common) }
}

/**
 * Every `- unit:` line of every `## route` section, a section running from its heading to the next
 * `## ` heading or READY line, backticks stripped. `{ build, units: [{ unit, spec }] }`, `spec` ''
 * when the line names none. The `- brief:` line is not read here. `lines` is every non-blank line of
 * those sections, the heading included, as the card holds it, each with the unit it names or null —
 * what the subagent context copies.
 */
function extractRouteUnits(text) {
  let inRoute = false
  let build = ''
  let seen = false
  const units = []
  const lines = []
  for (const raw of String(text || '').split(/\r?\n/)) {
    const line = raw.replace(/`/g, '').trim()
    if (line === '## route') { inRoute = true; seen = true; lines.push({ text: raw, unit: null }); continue }
    if (line.startsWith('## ') || line.replace(/^- /, '').startsWith('READY — ')) { inRoute = false; continue }
    if (!inRoute || line === '') continue
    let unit = null
    const b = /^- build:\s*(\S+)\s*$/.exec(line)
    const u = /^- unit:\s*(\S+)(?:\s*·\s*spec\s+(\S+))?\s*$/.exec(line)
    if (b) build = b[1]
    else if (u) units.push(unit = { unit: u[1], spec: u[2] || '' })
    lines.push({ text: raw, unit })
  }
  return { seen, build, units, lines }
}

/** The status header's first cell and its `Tier-<n>` cell: `{ status, tier }`, '(none)' and '' when absent. */
function readStatusCells(text) {
  const st = String(text || '').split(/\r?\n/).find((l) => l.startsWith('**Status:**')) || ''
  const cells = st.slice('**Status:**'.length).split('·').map((c) => c.trim())
  return { status: cells[0] || '(none)', tier: cells.find((c) => /^Tier-\d$/.test(c)) || '' }
}

/**
 * S3: is this routed unit BUILDABLE? '' when it is, else the reason. The spec path is repo-relative
 * under `<MEMORY_ROOT>/builds/<build>/spec/`, the file exists, its H1 names the unit, and its status
 * header's tier and status admit by BUILDABLE_STATUS — a Tier-1 SPECCED only when the conf's
 * `SPEC_TIER1_CUTOFF` is set and the spec's filename date is on or after it.
 */
function checkBuildable(u, build, top, memRoot, confBytes) {
  const fs = require('fs')
  const path = require('path')
  if (!u.spec) return 'the route line names no spec'
  if (!build) return 'the route names no - build: line, so the spec\'s build folder cannot be checked'
  const rel = buildComparablePath(u.spec)
  if (/^([a-z]:|\/|~)/.test(rel) || rel.split('/').includes('..')) return `spec ${u.spec} is not a repo-relative path`
  const want = buildComparablePath(memRoot) + '/builds/' + buildComparablePath(build) + '/spec/'
  // Any depth under the spec folder, as KICK R4 and parse_spec_h1 admit (TOOL-aRoutedQuill-12 S10).
  if (!rel.startsWith(want)) return `spec ${u.spec} is outside ${want}`
  let text
  try { text = fs.readFileSync(path.join(top, buildNativePath(u.spec)), 'utf8') } catch { return `spec ${u.spec} does not exist` }
  // The H1 read R4 and tree_lib.parse_spec_h1 make (S8): the first UNFENCED `#` line, its first token
  // with backticks and asterisks stripped and trailing `:.,;` dropped, compared whole.
  let fenced = false
  let h1Id = ''
  for (const l of text.split(/\r?\n/)) {
    if (/^ ? ? ?(```|~~~)/.test(l)) { fenced = !fenced; continue }
    if (fenced || !/^#[ \t]/.test(l)) continue
    h1Id = (l.split(/[ \t]+/)[1] || '').replace(/[`*]/g, '').replace(/[:.,;]+$/, '')
    break
  }
  if (h1Id !== u.unit) return `spec ${u.spec} has H1 naming ${h1Id || '(nothing)'}, not ${u.unit}`
  const { status, tier } = readStatusCells(text)
  const admits = BUILDABLE_STATUS[tier]
  if (!admits) return `spec ${u.spec} names no Tier-1 or Tier-2 on its status header`
  if (!admits.includes(status)) {
    return tier === 'Tier-2'
      ? `${tier} at ${status}: a Tier-2 unit admits writes at INPROGRESS, which follows the owner's scope approval`
      : `${tier} at ${status}: a Tier-1 unit admits writes at INPROGRESS, or at SPECCED once graded`
  }
  if (tier === 'Tier-1' && status === 'SPECCED') {
    const cutoff = readConfKey(confBytes, 'SPEC_TIER1_CUTOFF') || ''
    const dated = /^(\d{4}-\d{2}-\d{2})-/.exec(path.basename(u.spec))
    // Facts, not a remedy: the subagent context quotes these reasons, and the deny carries its own.
    if (!/^\d{4}-\d{2}-\d{2}$/.test(cutoff)) return `Tier-1 at SPECCED, and SPEC_TIER1_CUTOFF is blank, so no check graded its micro-spec; a Tier-1 unit at INPROGRESS admits`
    if (!dated || dated[1] < cutoff) return `Tier-1 at SPECCED, dated before SPEC_TIER1_CUTOFF ${cutoff}, so no check graded its micro-spec; a Tier-1 unit at INPROGRESS admits`
  }
  return ''
}

/** S6: why the conf leaves the gate UNARMED, or '' when it is armed. */
function checkUnarmed(memRoot, routed) {
  if (!memRoot || !memRoot.trim()) return 'MEMORY_ROOT is blank or absent'
  if (!routed || !routed.trim()) return 'ROUTED_PATHS is blank or absent'
  const mem = buildComparablePath(memRoot.trim()).replace(/^\.\//, '')
  for (const e of routed.trim().split(/\s+/)) {
    const c = buildComparablePath(e).replace(/^\.\//, '')
    if (/^([a-z]:|\/|~)/.test(c)) return `ROUTED_PATHS entry ${e} is absolute`
    if (c.split('/').includes('..')) return `ROUTED_PATHS entry ${e} climbs through ..`
    // Two-way (TOOL-aRoutedQuill-12 S6): an entry under MEMORY_ROOT covers it as surely as one above it.
    if (c === '' || c === '.' || checkUnderRoot(mem, c) || checkUnderRoot(c, mem)) return `ROUTED_PATHS entry ${e} covers MEMORY_ROOT (${memRoot}), so writing a spec would need a spec first`
  }
  return ''
}

/** The product-path refusal: target, entry, state, remedy, and what the gate does not reach. */
function renderRouteDeny(tool, target, entry, conf, state, remedy) {
  return (
    `BLOCKED by scratch-guard: this ${tool} targets ${target}, a product path under ROUTED_PATHS entry ` +
    `\`${entry}\` in ${conf}, and ${state}.\n\n${remedy}\n\nA write outside ROUTED_PATHS — the unit's ` +
    'spec and the orientation card included — is not gated.\n'
  )
}

// ---- the role arm (TOOL-aOrientedCast-6) --------------------------------------------------------

/** The role index at the target toplevel, generated by the roles kit; precedent for a root-level literal: ROUTE_CONF. */
const ROLE_INDEX = '.claude/roles.json'

/**
 * S1: the role index, in one of three states. `{ state: 'absent', shown }` when the file does not
 * exist; `{ state: 'broken', shown, why }` when it cannot be read, is not JSON, or is not the shape
 * `{ roles: { <name>: { writes: <string>, agent: <boolean>, … } }, harnesses: [<string>] }`;
 * `{ state: 'ok', shown, roles, harnesses, gates }` otherwise. Only the shape is checked: the value set of
 * `writes` belongs to the index's generator, and a value outside it simply admits no class here.
 * TOOL-aOrientedCast-11 adds two OPTIONAL keys, graded only when present: a role's `gates`, a list of
 * strings, and the top-level `gates`, `{ manifest: <string|null> }`; `gates` is null when absent.
 */
function loadRoleIndex(top) {
  const fs = require('fs')
  const path = require('path')
  const p = path.join(top, ROLE_INDEX)
  const shown = buildComparablePath(p)
  let bytes
  try {
    bytes = fs.readFileSync(p, 'utf8')
  } catch (e) {
    if (e && e.code === 'ENOENT') return { state: 'absent', shown }
    return { state: 'broken', shown, why: `cannot be read (${(e && e.code) || e})` }
  }
  let d
  try {
    d = JSON.parse(bytes)
  } catch (e) {
    return { state: 'broken', shown, why: `is not JSON (${(e && e.message) || e})` }
  }
  const shape = 'is not the shape { roles: { <name>: { writes: <string>, agent: <boolean> } }, harnesses: [<string>] }'
  if (!d || typeof d !== 'object' || Array.isArray(d) || !d.roles || typeof d.roles !== 'object' || Array.isArray(d.roles)
    || !Array.isArray(d.harnesses) || !d.harnesses.every((h) => typeof h === 'string')) return { state: 'broken', shown, why: shape }
  for (const [n, r] of Object.entries(d.roles)) {
    if (!r || typeof r !== 'object' || Array.isArray(r) || typeof r.writes !== 'string' || typeof r.agent !== 'boolean') {
      return { state: 'broken', shown, why: `${shape}: role ${n} is not` }
    }
    // TOOL-aOrientedCast-11 S3: a role's `gates`, when present, is a list of leg names.
    if (r.gates !== undefined && (!Array.isArray(r.gates) || !r.gates.every((g) => typeof g === 'string'))) {
      return { state: 'broken', shown, why: `${shape}: role ${n}'s gates is not a list of strings` }
    }
  }
  // ...and the top-level `gates`, when present, is `{ manifest: <string|null> }`. Absent reads as no manifest.
  const gates = d.gates
  if (gates !== undefined && (!gates || typeof gates !== 'object' || Array.isArray(gates)
    || !(gates.manifest === null || typeof gates.manifest === 'string'))) {
    return { state: 'broken', shown, why: `${shape}: gates is not { manifest: <string|null> }` }
  }
  return { state: 'ok', shown, roles: d.roles, harnesses: d.harnesses, gates: gates || null }
}

/**
 * The file as the tool would leave it, or null when that cannot be known. An `Edit` replaces its
 * `old_string` once, or everywhere under `replace_all`; an `old_string` the text does not hold, or
 * holds twice without `replace_all`, yields null. A `MultiEdit` applies its `edits` in order under
 * the same rule. A `Write` yields its `content`. A `NotebookEdit` yields null.
 */
function buildEditResult(text, tool, ti) {
  let edits
  if (tool === 'Write') return typeof ti.content === 'string' ? ti.content : null
  if (tool === 'Edit') edits = [ti]
  else if (tool === 'MultiEdit') edits = Array.isArray(ti.edits) ? ti.edits : []
  else return null
  if (edits.length === 0) return null
  let out = text
  for (const e of edits) {
    if (!e || typeof e.old_string !== 'string' || e.old_string === '' || typeof e.new_string !== 'string') return null
    const n = out.split(e.old_string).length - 1
    if (n === 0 || (n > 1 && e.replace_all !== true)) return null
    if (e.replace_all === true) { out = out.split(e.old_string).join(e.new_string); continue }
    const i = out.indexOf(e.old_string)
    out = out.slice(0, i) + e.new_string + out.slice(i + e.old_string.length)
  }
  return out
}

/**
 * S4's predicate: `after` differs from `before` in exactly one line, that line is the first one
 * opening `**Status:**` in both (the line readStatusCells reads), and of its `·`-split trimmed cells
 * only the first (the status) and the third (the date) moved. The first cell still reads
 * `**Status:**` and one word. Neither the word nor the date is graded: check 12 owns both.
 */
function checkStatusOnlyEdit(before, after) {
  const a = String(before).split(/\r?\n/)
  const b = String(after).split(/\r?\n/)
  if (a.length !== b.length) return false
  const moved = []
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) moved.push(i)
  if (moved.length !== 1) return false
  const i = moved[0]
  if (a.findIndex((l) => l.startsWith('**Status:**')) !== i || b.findIndex((l) => l.startsWith('**Status:**')) !== i) return false
  const ca = a[i].split('·').map((c) => c.trim())
  const cb = b[i].split('·').map((c) => c.trim())
  if (ca.length !== cb.length || cb.length < 3) return false
  for (let k = 1; k < cb.length; k++) if (k !== 2 && ca[k] !== cb[k]) return false
  return /^\*\*Status:\*\*\s*\S+$/.test(cb[0])
}

/** S6: the role refusal — target, class, writer, the roles the index admits, the index, the route to a role. */
function renderRoleDeny(cls, index, writers, w) {
  const r = w.agentType && Object.prototype.hasOwnProperty.call(index.roles, w.agentType) ? index.roles[w.agentType] : null
  const who = !w.agentType ? 'the main loop, whose payload carries no agent_type'
    : !r ? `agent type ${w.agentType}, which ${index.shown} does not name`
      : r.agent !== true ? `role ${w.agentType}, which ${index.shown} declares agent: false`
        : `role ${w.agentType}, whose writes is ${r.writes}`
  const routes = writers.map((n) => `To write it as ${n}, render that role's handoff with handoff.py render --role ${n} --build ${w.slug || '<slug>'} --part task and pass the output as the prompt of an Agent call whose subagent_type is ${n}, or name ${n} in its harness's roles argument.`)
  const flip = cls === 'spec'
    ? '\n\nAn edit moving only the status and date cells of the spec\'s **Status:** line is admitted from the main loop, and from the routed unit\'s builder on a spec its card routes.'
    : ''
  return (
    `BLOCKED by scratch-guard: this ${w.tool} targets ${w.target}, a ${cls} path, and its writer is ${who}. ` +
    `The role index ${index.shown} lets ${writers.join(', ')} write the ${cls} class, and no other writer.\n\n` +
    `${routes.join('\n')}${flip}\n`
  )
}

/**
 * Steps 6a and 9a: the role verdict on a write of class `cls` ('spec' or 'product'). null admits,
 * `{ deny }` refuses. `w` carries `tool`, `ti` (the tool_input), `native` (the target on disk),
 * `target` (its comparable form), `agentType`, `slug` and `routed` (the comparable spec paths the
 * session card's `## route` names). An absent index admits; a broken one refuses; no `agent`-true
 * role with `writes = cls` refuses as UNARMED; a role in the class admits. Last, and for a spec only,
 * S4's status flip admits from the main loop on any spec and from a `product` role on a routed one.
 */
function checkRoleWrite(cls, index, w) {
  if (index.state === 'absent') return null
  const head = `BLOCKED by scratch-guard: this ${w.tool} targets ${w.target}, a ${cls} path,`
  if (index.state === 'broken') {
    return { deny: `${head} and the role index ${index.shown} ${index.why}. Every spec and product write in this repository refuses until the index is sound; it is generated, so re-render it rather than hand-edit it.\n` }
  }
  const writers = Object.keys(index.roles).filter((n) => index.roles[n].agent === true && index.roles[n].writes === cls).sort()
  if (writers.length === 0) {
    return { deny: `${head} and the role arm is UNARMED for the ${cls} class: ${index.shown} names no role with agent: true and writes = ${cls}, so every ${cls} write refuses until one is declared.\n` }
  }
  if (w.agentType && writers.includes(w.agentType)) return null
  if (cls === 'spec') {
    const r = w.agentType && Object.prototype.hasOwnProperty.call(index.roles, w.agentType) ? index.roles[w.agentType] : null
    const builder = r && r.agent === true && r.writes === 'product' && w.routed.includes(w.target)
    if (!w.agentType || builder) {
      let before = null
      try { before = require('fs').readFileSync(w.native, 'utf8') } catch { before = null }
      const after = before === null ? null : buildEditResult(before, w.tool, w.ti)
      if (after !== null && checkStatusOnlyEdit(before, after)) return null
    }
  }
  return { deny: renderRoleDeny(cls, index, writers, w) }
}

/**
 * THE ONE EVALUATION ORDER of the write gate. Returns null to print nothing, `{ witness }` to allow
 * with one stderr line, `{ deny }` to refuse.
 *  1. `tool_name` outside WRITE_TOOLS → null
 *  2. no non-empty `file_path` / `notebook_path`, or a relative one with no payload `cwd` → deny
 *  3. session repository = common dir of `CLAUDE_PROJECT_DIR`, else of `cwd`; no `.git` above the
 *     target, no session repository, or a target common dir that differs → null
 *  4. `<target toplevel>/.memory-tree.conf` absent → witness; present and unreadable → deny
 *  5. UNARMED (checkUnarmed) → null when the target is the conf, else deny
 *  6. the target's CLASS: product when it falls under a ROUTED_PATHS entry; spec when its path
 *     opens `<MEMORY_ROOT>/builds/<one segment>/spec/`; else neither → null. Only a spec or a
 *     product path reads further, and only those read the role index.
 * 6a. spec → checkRoleWrite('spec') over loadRoleIndex(top): absent → null; broken → deny; no
 *     `agent`-true role with `writes = spec` → deny, UNARMED; the payload's `agent_type` names such a
 *     role → null; a status-and-date-only flip (checkStatusOnlyEdit) from the main loop, or from a
 *     `product` role on a spec its card's `## route` names → null; else deny
 *  7. product, and `session_id` missing or no card for it under the common dir → deny, absent
 *  8. no `## route`, or no `- unit:` line in it → deny, unrouted
 *  9. no routed unit BUILDABLE (checkBuildable) → deny listing each unit's reason; else step 9a
 * 9a. checkRoleWrite('product'): absent → null; broken → deny; no `agent`-true role with
 *     `writes = product` → deny, UNARMED; the payload's `agent_type` names such a role → null; else
 *     deny. The route arm runs first and never instead: a builder with no buildable route meets
 *     step 7, 8 or 9's refusal word for word.
 * No `agent_id` exemption: a subagent's write is judged by the same order (S7).
 */
function checkRouted(data, env) {
  const fs = require('fs')
  const path = require('path')
  if (!WRITE_TOOLS.includes(data.tool_name)) return null
  const tool = data.tool_name
  const ti = data.tool_input && typeof data.tool_input === 'object' ? data.tool_input : {}
  const raw = [ti.file_path, ti.notebook_path].find((v) => typeof v === 'string' && v !== '')
  const cwd = typeof data.cwd === 'string' && data.cwd !== '' ? data.cwd : ''
  if (raw === undefined) {
    return { deny: `BLOCKED by scratch-guard: this ${tool} payload carries neither tool_input.file_path nor tool_input.notebook_path as a non-empty string, so the write gate cannot place its target and refuses.\n` }
  }
  const native = buildNativePath(raw)
  if (!path.isAbsolute(native) && !cwd) {
    return { deny: `BLOCKED by scratch-guard: this ${tool} names a relative target (${raw}) in tool_input.file_path or tool_input.notebook_path, and the payload carries no cwd to resolve it against, so the write gate refuses.\n` }
  }
  // The target's REAL place (TOOL-aRoutedQuill-12 S4): the realpath of its deepest existing ancestor
  // with the not-yet-existing tail appended, so a product file reached through a junction or a symlink
  // is placed, and gated, like its repository spelling.
  let target = cwd ? path.resolve(buildNativePath(cwd), native) : path.resolve(native)
  for (let head = target, tail = ''; ;) {
    if (fs.existsSync(head)) { target = path.join(resolveRealPath(head) || head, tail); break }
    const up = path.dirname(head)
    if (up === head) break
    tail = tail ? path.join(path.basename(head), tail) : path.basename(head)
    head = up
  }
  const sessionStart = env.CLAUDE_PROJECT_DIR || cwd
  if (!sessionStart) return null
  const session = resolveComparableCommon(path.resolve(buildNativePath(sessionStart)))
  const mine = resolveComparableCommon(target)
  if (!session.key || !mine.key || session.key !== mine.key) return null
  const top = mine.hit.toplevel
  const confPath = path.join(top, ROUTE_CONF)
  const confShown = buildComparablePath(confPath)
  let confBytes
  try {
    confBytes = fs.readFileSync(confPath, 'utf8')
  } catch (e) {
    if (e && e.code === 'ENOENT') return { witness: `write gate not armed — no ${ROUTE_CONF} at ${buildComparablePath(top)}` }
    return { deny: `BLOCKED by scratch-guard: ${confShown} exists and cannot be read (${(e && e.code) || e}), so the write gate cannot decide this ${tool} and refuses.\n` }
  }
  const targetC = buildComparablePath(target)
  const memRoot = readConfKey(confBytes, 'MEMORY_ROOT')
  const routed = readConfKey(confBytes, 'ROUTED_PATHS')
  const unarmed = checkUnarmed(memRoot, routed)
  if (unarmed) {
    if (targetC === confShown) return null
    return { deny: `BLOCKED by scratch-guard: the write gate is UNARMED in this repository — ${confShown}: ${unarmed}. The gate reads MEMORY_ROOT and ROUTED_PATHS from that conf, and every write here refuses until both are sound; the one write admitted is to ${confShown} itself.\n` }
  }
  const rel = targetC.slice(buildComparablePath(top).length + 1)
  const entry = routed.trim().split(/\s+/).find((e) => {
    const c = buildComparablePath(e).replace(/^\.\//, '')
    return /[\\/]$/.test(e) ? checkUnderRoot(rel, c) : rel === c
  })
  const sid = data.session_id ? String(data.session_id) : ''
  const agentType = typeof data.agent_type === 'string' ? data.agent_type : ''
  if (entry === undefined) {
    // Step 6: the spec class, on the comparable form, MEMORY_ROOT normalized as checkUnarmed does it.
    const mem = buildComparablePath(memRoot.trim()).replace(/^\.\//, '')
    const pre = (mem === '.' ? '' : mem + '/') + 'builds/'
    if (!rel.startsWith(pre) || !/^[^/]+\/spec\/./.test(rel.slice(pre.length))) return null
    // The slug keeps its case: the same segment of the target's own spelling.
    const slug = path.relative(top, target).replace(/\\/g, '/').split('/')[pre.split('/').length - 1] || ''
    const cardText = sid ? readCard(mine.common, sid).text : null
    const routed = extractRouteUnits(cardText).units.filter((u) => u.spec).map((u) => buildComparablePath(path.join(top, buildNativePath(u.spec))))
    return checkRoleWrite('spec', loadRoleIndex(top), { tool, ti, native: target, target: targetC, agentType, slug, routed })
  }
  const card = sid ? readCard(mine.common, sid) : null
  if (!card || card.text === null) {
    const where = card ? `this session has no orientation card at ${card.shown} (session ${sid})` : 'the payload carries no session_id, so no orientation card can be read'
    return { deny: renderRouteDeny(tool, targetC, entry, confShown, where, `Create the card with manifest-check.sh --card --write --session ${sid || '<session id>'} from the kickoff kit, then run /session-kickoff, which specs the unit, writes its brief and appends a ## route naming it.`) }
  }
  const route = extractRouteUnits(card.text)
  if (!route.seen || route.units.length === 0) {
    const what = route.seen ? `its ## route at ${card.shown} carries no - unit: line` : `its orientation card ${card.shown} carries no ## route`
    return { deny: renderRouteDeny(tool, targetC, entry, confShown, what, `Run /session-kickoff: give the unit its spec, then append a ## route naming it through manifest-check.sh --card --append --session ${sid}.`) }
  }
  const reasons = []
  for (const u of route.units) {
    const why = checkBuildable(u, route.build, top, memRoot.trim(), confBytes)
    if (!why) {
      // Step 9a: the route admits; the writer's role decides. The slug is the unit id's middle.
      const slug = (/^[A-Za-z]+-(.+)-\d+$/.exec(u.unit) || [])[1] || route.build
      return checkRoleWrite('product', loadRoleIndex(top), { tool, ti, native: target, target: targetC, agentType, slug, routed: [] })
    }
    reasons.push(`  ${u.unit}: ${why}`)
  }
  return { deny: renderRouteDeny(tool, targetC, entry, confShown, `no unit its card ${card.shown} routes is buildable:\n${reasons.join('\n')}`, 'Make one routed unit buildable — its spec at the status that admits writes — or route the unit that owns this write through /session-kickoff and manifest-check.sh --card --append.') }
}

// ---- the role-gate arm (TOOL-aOrientedCast-11) --------------------------------------------------

/** The launchers whose script is the head; `python3.<n>` is matched by shape. */
const GATE_LAUNCHERS = ['bash', 'sh', 'python', 'python3', 'py', 'node']
/** Leading words that change nothing about what runs; `timeout` is read apart for its duration. */
const GATE_PREFIX_WORDS = ['env', 'export', 'nohup', 'time', 'exec', 'command', 'nice']
/**
 * The options of a launcher family or a prefix word (TOOL-aOrientedCast-14): `takes` consume the
 * next word as their argument; an `ends` option ends the simple command, which runs no script; a
 * `body` option's next word is a command of its own. Any other option is stepped past alone. A
 * prefix word with no row (`export`, `nohup`, `time`) takes the empty rule. A shell's `n` cluster is
 * tested before its `c` cluster, because `bash -nc '<x>'` only checks the syntax of `<x>`.
 */
const GATE_OPTION_RULES = {
  shell: { plus: true, takes: ['-o', '+o', '-O', '+O', '--rcfile', '--init-file'], ends: /^-[A-Za-z]*n[A-Za-z]*$/, body: /^-[A-Za-z]*c[A-Za-z]*$/ },
  python: { takes: ['-W', '-X', '-Q'], ends: /^-[A-Za-z]*[cm]$/ },
  node: { takes: ['-r', '--require', '--import'], ends: /^(?:-e|--eval|-p|--print)$/ },
  env: { takes: ['-u', '--unset', '-C', '--chdir'], body: /^(?:-S|--split-string)$/ },
  nice: { takes: ['-n', '--adjustment'] },
  exec: { takes: ['-a'] },
  command: { takes: [], ends: /^-[vV]$/ },
}
/** G2, by basename and in any form: the bar runner, the self-test runner, the unattended gates runner. */
const GATE_RUNNERS = ['run-gates.sh', 'run-selftests.sh', 'run-unattended-gates.sh']
/** G3's admitting words: a render, a listing or a usage text runs no arm. */
const GATE_SUITE_ADMITS = ['--render', '--list', '--help']

/** The last segment of a word, either slash, lower-cased, `.exe` dropped. */
function buildBaseName(w) {
  return String(w || '').replace(/\\/g, '/').split('/').pop().toLowerCase().replace(/\.exe$/, '')
}

/**
 * A word as G1 compares it: a path-bearing word (a slash of either kind) resolved against <base>
 * in buildComparablePath's form, made relative to the toplevel when it sits under it; any other
 * word unchanged. One function for the command's words and the manifest's, so the two cannot fold
 * a path two ways.
 */
function buildGateWord(w, base, topC) {
  if (!/[\\/]/.test(w)) return w
  const c = buildComparablePath(require('path').resolve(base, w))
  return c.startsWith(topC + '/') ? c.slice(topC.length + 1) : c
}

/**
 * From word <k> of <a>, past every option of <rule>: a word opening `-`, or `+` for a shell. Returns
 * the index of the next non-option word, or -1 when the simple command ends. A body option scans its
 * next word ONCE through scanCommandHeads into <out>, at depth 0 only, then ends it. A `--` is stepped
 * past and ends the options.
 */
function scanLauncherOptions(a, k, rule, depth, out) {
  const r = rule || {}
  for (; k < a.length; k++) {
    const w = a[k]
    if (w === '--') return k + 1
    if (!w.startsWith('-') && !(r.plus && w.startsWith('+'))) return k
    if (r.takes && r.takes.includes(w)) { k++; continue }
    if (r.ends && r.ends.test(w)) return -1
    if (r.body && r.body.test(w)) {
      if (depth === 0 && a[k + 1] !== undefined) out.push(...scanCommandHeads(a[k + 1], depth + 1))
      return -1
    }
  }
  return k
}

/**
 * The simple commands of <cmd> and their heads. A simple command is a segment of the blanked view
 * between `;`, `|`, `&`, `(`, `)` and a newline, its words read from the original text with their
 * quotes dropped and its redirections removed. The HEAD is the first word after any `NAME=value`,
 * any prefix word with its options, and `timeout` with its options and duration, then past a
 * launcher and its options, each stepped by GATE_OPTION_RULES through scanLauncherOptions: a shell's
 * `-c` scans its body ONCE as a command of its own, a shell's `-n` executes nothing, and a Python
 * `-c` or `-m` names no script — each ends the segment.
 * Returns `[{ text, head, argv, launched }]`, argv being the head and every word after it.
 */
function scanCommandHeads(cmd, depth = 0) {
  const view = buildCommandView(cmd)
  const out = []
  const seg = /[^;|&()\n]+/g
  let m
  while ((m = seg.exec(view)) !== null) {
    const tok = new RegExp(VIEW_TOKEN, 'g')
    const words = []
    let t
    while ((t = tok.exec(m[0])) !== null) {
      const at = m.index + t.index
      words.push(cmd.slice(at, at + t[0].length).replace(/"([^"]*)"|'([^']*)'/g, (_, d, s) => (d !== undefined ? d : s)))
    }
    const a = []
    for (let i = 0; i < words.length; i++) {
      const r = /^(?:\d*|&)(?:>>?|<{1,3})(.*)$/.exec(words[i])
      if (!r) a.push(words[i])
      else if (r[1] === '') i++
    }
    let k = 0
    for (;;) {
      while (k < a.length && /^[A-Za-z_][A-Za-z0-9_]*=/.test(a[k])) k++
      if (GATE_PREFIX_WORDS.includes(a[k])) {
        k = scanLauncherOptions(a, k + 1, GATE_OPTION_RULES[a[k]], depth, out)
        if (k < 0) break
        continue
      }
      if (a[k] === 'timeout') {
        k++
        while (k < a.length && a[k].startsWith('-')) k += /^(?:-[sk]|--signal|--kill-after)$/.test(a[k]) ? 2 : 1
        if (k < a.length && /^\d/.test(a[k])) k++
        continue
      }
      break
    }
    if (k < 0 || k >= a.length) continue
    const lb = buildBaseName(a[k])
    let launched = false
    if (GATE_LAUNCHERS.includes(lb) || /^python3\.\d+$/.test(lb)) {
      const family = lb === 'bash' || lb === 'sh' ? 'shell' : lb === 'node' ? 'node' : 'python'
      k = scanLauncherOptions(a, k + 1, GATE_OPTION_RULES[family], depth, out)
      if (k < 0 || k >= a.length) continue
      launched = true
    }
    out.push({ text: cmd.slice(m.index, m.index + m[0].length).trim(), head: a[k], argv: a.slice(k), launched })
  }
  return out
}

/** G2: the head's basename is a runner. */
function checkGateRunner(c) {
  return GATE_RUNNERS.includes(buildBaseName(c.head))
}

/** G3: the head is a suite or a self-test script, or a script carrying `--selftest`, and no admitting word. */
function checkGateSuite(c) {
  const b = buildBaseName(c.head)
  const script = c.launched || /[\\/]/.test(c.head)
  const hit = b.endsWith('.test.sh') || b.endsWith('selftest.py') || (script && c.argv.includes('--selftest'))
  return hit && !c.argv.some((w) => GATE_SUITE_ADMITS.includes(w))
}

/**
 * The manifest's legs, each `{ name, words }` from its first path-bearing word on with `{prefix}`
 * resolved to the manifest's own directory, or `{ legs: null, why }` when the index names no
 * manifest or it does not read as a list. A row with no path-bearing word cannot be a script's
 * argv and is left out.
 */
function readGateLegs(top, index) {
  const fs = require('fs')
  const path = require('path')
  const rel = index.gates && index.gates.manifest
  if (typeof rel !== 'string' || !rel) return { legs: null, why: `the role index ${index.shown} names no gate manifest` }
  const p = path.resolve(top, rel)
  const shown = buildComparablePath(p)
  let rows
  try {
    rows = JSON.parse(fs.readFileSync(p, 'utf8'))
  } catch (e) {
    return { legs: null, why: `the gate manifest ${shown} does not read (${(e && (e.code || e.message)) || e})` }
  }
  if (!Array.isArray(rows)) return { legs: null, why: `the gate manifest ${shown} is not a list` }
  const dir = path.dirname(p)
  const topC = buildComparablePath(top)
  const legs = []
  for (const g of rows) {
    if (!g || typeof g.name !== 'string' || !Array.isArray(g.argv) || !g.argv.every((w) => typeof w === 'string')) continue
    const words = g.argv.map((w) => w.split('{prefix}').join(dir))
    const at = words.findIndex((w) => /[\\/]/.test(w))
    if (at >= 0) legs.push({ name: g.name, words: words.slice(at).map((w) => buildGateWord(w, top, topC)) })
  }
  return { legs }
}

/** G1: the leg whose words equal the command's argv, paths resolved against the payload cwd, or null. */
function checkGateLeg(c, legs, cwd, top) {
  if (!legs || !/[\\/]/.test(c.head)) return null
  const topC = buildComparablePath(top)
  const argv = c.argv.map((w) => buildGateWord(w, cwd, topC))
  return legs.find((g) => g.words.length === argv.length && g.words.every((w, i) => w === argv[i])) || null
}

function renderGateDeny(type, c, row, leg, allow, shown) {
  return (
    `BLOCKED by scratch-guard: a role agent runs no gate. Agent type ${type} ran \`${c.text}\`, which is ` +
    `row ${row}${leg ? `, the leg "${leg.name}"` : ''}.\n\n` +
    `The allowlist of ${type} in the role index ${shown} is ${allow.length ? allow.map((n) => `"${n}"`).join(', ') : 'empty'}. ` +
    'Gates run in the main session at the merge or push threshold, so return the need in your result, ' +
    'and verify your change with a fixture or a probe of your own code.\n'
  )
}

/**
 * The checkout root a role arm reads its index at (TOOL-aOrientedCast-14): the toplevel above the
 * payload <cwd>, else above `env.CLAUDE_PROJECT_DIR`, each start resolved as checkRouted resolves its
 * session start, else null. The cwd comes first because the command or spawn runs there.
 */
function resolveRoleRoot(cwd, env) {
  const path = require('path')
  for (const start of [cwd, env && env.CLAUDE_PROJECT_DIR]) {
    if (typeof start !== 'string' || start === '') continue
    const hit = resolveToplevel(path.resolve(buildNativePath(start)))
    if (hit) return hit.toplevel
  }
  return null
}

/**
 * THE ONE EVALUATION ORDER of the role-gate arm. Returns null to admit, `{ witness }` to admit with
 * one stderr line, `{ deny }` to refuse.
 *  1. `agent_type` absent or empty → null (the main loop runs every gate)
 *  2. no simple command whose head is a launched script, a path-bearing word, or a G2 or G3 shape
 *     → null, with no file read
 *  3. no root by resolveRoleRoot (the payload `cwd`, then `CLAUDE_PROJECT_DIR`) → null, or one
 *     witness naming both starts when `CLAUDE_PROJECT_DIR` is set
 *  4. loadRoleIndex: absent → null; broken → deny naming the index
 *  5. the allowlist: the index's `gates` list for the type, else empty — `workflow-subagent` and
 *     every type the index does not name may run nothing
 *  6. readGateLegs: no manifest, an absent one or one that does not parse leaves G1 unarmed and
 *     returns a witness naming it; G2 and G3 still bind
 *  7. each simple command: an allowlisted G1 leg is admitted whole; else G2, G3, then G1 refuses
 */
function checkRoleGate(cmd, data, env) {
  const path = require('path')
  const type = typeof data.agent_type === 'string' ? data.agent_type : ''
  if (!type) return null
  const cands = scanCommandHeads(cmd).filter((c) => c.launched || /[\\/]/.test(c.head) || checkGateRunner(c) || checkGateSuite(c))
  if (cands.length === 0) return null
  const raw = typeof data.cwd === 'string' ? data.cwd : ''
  const project = env && env.CLAUDE_PROJECT_DIR
  const top = resolveRoleRoot(raw, env)
  if (!top) {
    if (!project) return null
    return { witness: `role-gate unarmed — neither the payload cwd ${raw || '(none)'} nor CLAUDE_PROJECT_DIR ${project} lies in a checkout, so no role index was read` }
  }
  // G1 resolves the command's paths against the payload cwd, and against the root when it has none.
  const cwd = raw ? path.resolve(raw) : top
  const index = loadRoleIndex(top)
  if (index.state === 'absent') return null
  if (index.state === 'broken') {
    return { deny: `BLOCKED by scratch-guard: a role agent runs no gate, and the role index ${index.shown} ${index.why}, so the allowlist of ${type} cannot be read. Repair or re-render the index; gates run in the main session at the merge or push threshold.\n` }
  }
  const role = index.roles[type]
  const allow = role && Array.isArray(role.gates) ? role.gates : []
  const g = readGateLegs(top, index)
  for (const c of cands) {
    const leg = checkGateLeg(c, g.legs, cwd, top)
    if (leg && allow.includes(leg.name)) continue
    const row = checkGateRunner(c) ? 'G2 runner' : checkGateSuite(c) ? 'G3 suite' : leg ? 'G1 leg' : null
    if (row) return { deny: renderGateDeny(type, c, row, leg, allow, index.shown) }
  }
  return g.legs ? null : { witness: `role-gate row G1 leg unarmed — ${g.why}; rows G2 runner and G3 suite still bind` }
}

// ---- the subagent context (TOOL-aRoutedQuill-4) ------------------------------------------------

/** The harness's cap on a hook's additionalContext, in characters (Claude Code's documentation). */
const ROUTE_CONTEXT_CAP = 10000
const WRITE_TOOLS_PROSE = 'an Edit, Write, MultiEdit or NotebookEdit'

/**
 * What a subagent is told at SubagentStart, or '' to print nothing. THE ONE EVALUATION ORDER:
 *  1. session directory = `CLAUDE_PROJECT_DIR`, else the payload `cwd`; under no `.git` → ''
 *  2. no `.memory-tree.conf` at its toplevel → '' (the gate admits every write there)
 *  3. the conf unreadable, or UNARMED (checkUnarmed) → its one line
 *  4. `session_id` missing, no card under the common dir, no `## route`, no `- unit:` → one line
 *  5. otherwise the card path, its route lines byte for byte, one checkBuildable verdict per unit
 *     line, the ROUTED_PATHS value and what the gate refuses — route lines cut at a line boundary
 *     to ROUTE_CONTEXT_CAP, a cut unit line taking its verdict with it, and a closing count line
 * The card is located as checkRouted locates it, so the context and the gate read one card.
 */
function renderRouteContext(data, env) {
  const fs = require('fs')
  const path = require('path')
  const start = env.CLAUDE_PROJECT_DIR || (typeof data.cwd === 'string' ? data.cwd : '')
  if (!start) return ''
  const hit = resolveToplevel(path.resolve(buildNativePath(start)))
  const common = hit && resolveCommonDir(hit)
  if (!common) return ''
  const top = hit.toplevel
  const confShown = buildComparablePath(path.join(top, ROUTE_CONF))
  let confBytes
  try {
    confBytes = fs.readFileSync(path.join(top, ROUTE_CONF), 'utf8')
  } catch (e) {
    if (e && e.code === 'ENOENT') return ''
    return `${confShown} could not be read (${(e && e.code) || e}), so scratch-guard refuses every Edit, Write, MultiEdit or NotebookEdit in this repository.`
  }
  const memRoot = readConfKey(confBytes, 'MEMORY_ROOT')
  const routed = readConfKey(confBytes, 'ROUTED_PATHS')
  const unarmed = checkUnarmed(memRoot, routed)
  if (unarmed) return `${confShown} leaves the write gate UNARMED: ${unarmed}, so scratch-guard refuses every Edit, Write, MultiEdit or NotebookEdit in this repository except to that file.`
  const value = routed.trim()
  const refuses = `so scratch-guard refuses ${WRITE_TOOLS_PROSE} under ROUTED_PATHS (${value}).`
  const sid = data.session_id ? String(data.session_id) : ''
  if (!sid) return `No unit is routed in this session: the payload carries no session_id, ${refuses}`
  const card = readCard(common, sid)
  if (card.text === null) return `No unit is routed in this session: ${card.shown} is absent, ${refuses}`
  const route = extractRouteUnits(card.text)
  if (!route.seen) return `No unit is routed in this session: ${card.shown} holds no route, ${refuses}`
  if (route.units.length === 0) return `No unit is routed in this session: the route in ${card.shown} names no unit, ${refuses}`
  const head = `The parent session's orientation card, ${card.shown}, holds this route:`
  const tail = [
    `ROUTED_PATHS in ${ROUTE_CONF} is: ${value}`,
    `scratch-guard refuses ${WRITE_TOOLS_PROSE} under those paths unless a routed unit is buildable.`,
  ]
  const renderVerdict = (u) => {
    const why = checkBuildable(u, route.build, top, memRoot.trim(), confBytes)
    if (why) return `${u.unit} is not buildable: ${why}.`
    const st = readStatusCells(fs.readFileSync(path.join(top, buildNativePath(u.spec)), 'utf8'))
    return `${u.unit} is buildable: ${st.tier} at ${st.status}.`
  }
  const renderClosing = (n) => `${n} more route lines of ${card.shown} are left out of this context, which is capped at ${ROUTE_CONTEXT_CAP} characters.`
  // Budgeted with the closing line at its longest, so whatever count it ends up naming still fits.
  let budget = ROUTE_CONTEXT_CAP - head.length - tail.reduce((s, l) => s + l.length + 1, 0) - (renderClosing(route.lines.length).length + 1)
  const kept = []
  const verdicts = []
  for (const l of route.lines) {
    const v = l.unit ? renderVerdict(l.unit) : ''
    const cost = l.text.length + 1 + (v ? v.length + 1 : 0)
    if (cost > budget) break
    budget -= cost
    kept.push(l.text)
    if (v) verdicts.push(v)
  }
  const out = [head, ...kept, ...verdicts, ...tail]
  if (kept.length < route.lines.length) out.push(renderClosing(route.lines.length - kept.length))
  return out.join('\n')
}

function main() {
  let data
  try {
    data = JSON.parse(readStdin())
  } catch {
    process.exit(0)
  }
  if (data && data.hook_event_name === 'SubagentStart') {
    // NEVER BLOCKS, NEVER SURFACES AN ERROR: a throw prints nothing. Returning rather than exiting
    // lets node flush a piped stdout, which process.exit does not wait for on every platform.
    let text = ''
    try {
      text = renderRouteContext(data, process.env)
    } catch {
      text = ''
    }
    if (text) process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: 'SubagentStart', additionalContext: text } }) + '\n')
    return
  }
  if (data && WRITE_TOOLS.includes(data.tool_name)) {
    // FAILS CLOSED, unlike the two Bash checks below: a write gate that throws and admits is the
    // silent off D7 gives no bypass. agent-cap.js keeps the same rule for its spec-audit kind (S8).
    let gate
    try {
      gate = checkRouted(data, process.env)
    } catch (e) {
      gate = { deny: `BLOCKED by scratch-guard: the write gate threw (${(e && e.message) || e}) and fails closed on a ${data.tool_name}.\n` }
    }
    if (gate && gate.deny) {
      process.stderr.write(gate.deny)
      process.exit(2)
    }
    if (gate && gate.witness) process.stderr.write(`scratch-guard: ${gate.witness}\n`)
    process.exit(0)
  }
  if (!data || !TOOLS.includes(data.tool_name)) process.exit(0)
  const cmd = (data.tool_input && data.tool_input.command) || ''
  if (!cmd) process.exit(0)

  // The predicate is wrapped because a hygiene guard that THROWS is worse than one that misses: an
  // uncaught error exits 1, which surfaces noise on a command that was probably fine. Fail open and
  // stay consistent with the stdin handling above. The self-test pins this arm so the catch cannot
  // quietly become the normal path.
  // A throw in either of the first two checks skips what remains of THEM and nothing else: the
  // role-gate arm below still runs (TOOL-aOrientedCast-11 S6).
  let verdict = null
  try {
    verdict = checkCommand(cmd, process.env)
  } catch {
    verdict = null
  }
  if (verdict && verdict.bad.length > 0) {
    process.stderr.write(renderDeny(verdict.bad, verdict.allowed))
    process.exit(2)
  }
  // The orientation check, AFTER the scratch verdict and under the same fail-open wrap.
  let orient = null
  if (verdict) {
    try {
      orient = checkOriented(cmd, data)
    } catch {
      orient = null
    }
  }
  if (orient && orient.deny) {
    process.stderr.write(orient.deny)
    process.exit(2)
  }
  if (orient && orient.witness) process.stderr.write(`scratch-guard: ${orient.witness}\n`)
  // The role-gate arm, LAST, and it FAILS CLOSED for a role agent as the write gate does: under a
  // fail-open catch a defect in it would be a silent off (§8 F5). The main loop is never refused.
  let gate = null
  try {
    gate = checkRoleGate(cmd, data, process.env)
  } catch (e) {
    gate = data.agent_type ? { deny: `BLOCKED by scratch-guard: the role-gate arm threw (${(e && e.message) || e}) and refuses a role agent's ${data.tool_name} call.\n` } : null
  }
  if (gate && gate.deny) {
    process.stderr.write(gate.deny)
    process.exit(2)
  }
  if (gate && gate.witness) process.stderr.write(`scratch-guard: ${gate.witness}\n`)
  process.exit(0)
}

if (require.main === module) main()
module.exports = { resolveToplevel, resolveCommonDir, checkCommand, buildCommandView, buildComparablePath, resolveAllowedRoots, readFrontMatterKey, ANCHOR_MODES, KIT_SCRATCH_GUARD_VERSION, checkRouted, checkBuildable, extractRouteUnits, readConfKey, checkUnarmed, readCard, WRITE_TOOLS, ROUTE_CONF, renderRouteContext, ROUTE_CONTEXT_CAP, loadRoleIndex, ROLE_INDEX, checkStatusOnlyEdit, buildEditResult, checkRoleGate, scanCommandHeads, resolveRoleRoot }
