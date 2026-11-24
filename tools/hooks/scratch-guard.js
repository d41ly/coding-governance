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
 * second, `> "$HOME/.x"` is missed. The review kit's script views draw the same distinction (script-views.js
 * `stripStrings`), for the same reason.
 *
 * ponytail: the predicate is TEXTUAL. It resolves no variable beyond `~`, `$HOME` and the three temp
 * spellings, follows no `cd`, and reads a heredoc body only where a `python -`, `python3 -` or `node`
 * with no script, or a `git apply`, reads it (TOOL-dBoundRoles-7) — `cd ~ && echo x > y` walks
 * straight past it. It catches the literal shapes that produced every one of the observed files,
 * which is the job. The upgrade path, if that stops being enough, is a real tokenizer rather than
 * more regexes.
 *
 * FAILS OPEN. Unparseable stdin, an unknown tool, or a missing command all exit 0. This is a hygiene
 * rule, not a containment boundary; a security control would have to fail the other way. The THIRD
 * check below, the write gate, is one exception: it fails closed. The role-gate arm and the
 * shell-write arm are the others, for a payload carrying an `agent_type` only.
 *
 * Protocol: deny = stderr text + exit 2. Allow = print nothing, exit 0. Matches the roles kit's spawn-guard.js, which
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
 * Tier-1 at SPECCED once `SPEC_TIER1_CUTOFF` graded it, or a unit that route's build's run-state
 * file records as dispatched and whose spec is buildable. `checkRouted` is the predicate and its
 * comment is the ONE evaluation order. It binds a subagent exactly as the main loop: a subagent's
 * payload carries the parent's `session_id` (measured, the aRoutedQuill probe record), so it reads
 * the parent's card. A conf that declares MEMORY_ROOT or ROUTED_PATHS blank, or an entry that is
 * absolute, climbs through `..` or covers MEMORY_ROOT, is UNARMED: every write in that repository
 * refuses except one to the conf. A target in no repository, or in one that is not the session's,
 * is not gated; neither is a repository with no conf (one witness line).
 *
 * WHAT ESCAPES THE WRITE GATE — it stops forgetting, not evasion: the main loop's Bash or PowerShell
 * write (`sed -i`, an interpreter, a redirect) is never seen, and the push-time leg owns that
 * guarantee; a role agent's is held by the shell-write arm below to the same verdict, for the shapes
 * scanWriteTargets reads (a redirect, `tee`, `touch`, `mkdir`, the PowerShell write cmdlets, the
 * last operand of `cp`, `mv`, `install` and `rsync` or the first three's target directory, `sed -i`,
 * `perl -i`, an interpreter's literal write call and `git apply`), and a role agent's other shell writes still escape; a
 * hook-less or `--bare` run fires no hook; a narrowed ROUTED_PATHS is a conf diff, not a refusal; a
 * hand-written card with a `## route` is read like the writer's; and a spec status flipped to
 * INPROGRESS without the owner's approval admits, because the gate reads a status the agent writes.
 *
 * THE ROLE ARM (TOOL-aOrientedCast-6). The same gate reads WHO writes, from the payload's
 * `agent_type`, against the role index `.claude/roles.json` at the target toplevel (`loadRoleIndex`,
 * exported so the roles kit's spawn-guard.js reads the index through this one reader). A write under
 * `<MEMORY_ROOT>/builds/<build>/spec/` is admitted only from a role declaring `writes = spec`; a
 * product write admitted by the route arm above is then admitted only from a role declaring
 * `writes = product`. The main loop, which carries no `agent_type`, and an untyped harness agent
 * (`workflow-subagent`) are refused both — except a spec edit that moves only the status and date
 * cells of its `**Status:**` line, admitted from the main loop and from a `product` role on a spec
 * its card routes. An ABSENT index adds no arm in a tree that never adopted the roles kit, and
 * refuses both classes in a GOVERNED one, a tree whose `.claude/agents/` holds a rendered gov agent
 * file (`checkRoleGoverned`, TOOL-dBoundRoles-6 S3); a broken one refuses both classes; an index
 * naming no writer for a class refuses that class as UNARMED. The renders themselves, the index and
 * the agent file of every role it names, are refused to every writer at step 5a, naming
 * `render_agents.py --write` (TOOL-dBoundRoles-6 S1); an adopter's own agent file is not. What
 * escapes it, besides everything that escapes the gate: the main loop's shell write to the renders,
 * which the policy kit's commit guard holds, a tree whose index and every rendered agent file were both
 * deleted, and a session launched AS a role, whose payload carries that role's type. It grades four
 * write classes (TOOL-dBoundRoles-9): `spec` and `product` above, and, on a target in neither, step
 * 6b's two: a role declaring `writes = none` writes nothing in the repository, and one declaring
 * `writes = review` writes only under the review class's folder, which the index's `classes` map
 * spells from the roles kit's one table (`checkWriteClass`, `checkRoleClass`); with no map, that
 * role's write refuses naming the re-render. The main loop and an agent type the index does not
 * name are not read there; a role agent's write there meets the absent and broken verdicts above.
 * `records` alone is declared in the index and read by nothing here.
 *
 * THE RED-FIX LANE (TOOL-aNimbleMend-8, bounded by TOOL-aNimbleMend-14). A product write the route
 * arm or the role arm is about to refuse is admitted, with one witness line, while the gate ledger
 * under the worktree's own git dir (`gate-ledger.tsv`, written by the bar runner and by a pass-leg
 * run) holds an OPEN red and the policy key `bar.inline-red-fixes` reads `on`, or no policy kit
 * resolves. A row is an open red when it has the nine-field form with status `fail` or `timeout`,
 * names a leg of the manifest the conf key `LEG_MANIFEST` names, and its head field is `HEAD` or an
 * ancestor of `HEAD` the landed revision does not reach: the runner carries old rows forward, so a
 * row is bounded by its own head. A blank `LEG_MANIFEST` reads as `gate-legs.json` beside the
 * run-gates kit this install holds, and closes the lane where none resolves. The writer is the main
 * loop or a role declaring `writes = product`; any other writer, a broken role index, an absent one
 * in a governed tree (TOOL-dBoundRoles-6 S3), the key
 * `off`, a refused key read and any other value each leave the refusal standing. `readOpenReds`
 * reads the ledger, `checkRedLane` is the decision, and the commit owes a `Red-fix: <leg>` trailer
 * beside `Pass: none`, which the commit grader reads. A spec write never reaches it. WHAT THE LANE
 * DOES NOT CHECK: whether the write fixes the red, since any product path is admitted while any row
 * is open; whether the tree the run graded was clean, since a run over a dirty tree stamps `HEAD`;
 * whether a later commit of the branch already fixed the red, since a row at an unlanded ancestor
 * stays open until a run measures its leg again or the branch lands; and a ledger edited by hand
 * or a manifest edited in the working tree, each read like the runner's.
 *
 * THE FOURTH CHECK: THE ROLE-GATE ARM (TOOL-aOrientedCast-11). Gates are the main session's, at the
 * merge or push threshold. On a Bash or PowerShell payload carrying an `agent_type`, AFTER the
 * scratch verdict and the orientation check, `checkRoleGate` refuses a simple command that runs a
 * gate the role's allowlist does not name: G1, the argv of a leg of the gate manifest the role
 * index names (`gates.manifest`), compared word for word from its script on; G2, the bar runner,
 * the self-test runner, the unattended gates runner or the pass-leg runner `pass-legs.sh`
 * (TOOL-aNimbleMend-6), by basename, in any form; G3, a `*.test.sh`
 * or `*selftest.py` script, or a script carrying `--selftest`, unless it carries `--render`,
 * `--list` or `--help`. The allowlist is the index's `gates` list for that type, rendered from the
 * roles kit's policy; a type the index does not name, `workflow-subagent` among them, may run
 * nothing. `checkRoleGate` is the predicate and its comment is the ONE evaluation order. A
 * launcher's options and a prefix word's options are stepped past by `GATE_OPTION_RULES`
 * (TOOL-aOrientedCast-14): an option that takes an argument takes it, a shell's `-n`, a Python `-c`
 * or `-m`, a Node `-e` or `-p` and `command -v` end the command, and a shell's `-c` and `env -S`
 * scan their body once. A shell option cluster takes one word for each `o` or `O` it carries
 * (TOOL-aTrimmedWait-6), so `-eo pipefail` steps past `pipefail`. The same arm refuses a role
 * agent's polling wait, read by `checkPollWait` with the shell's reserved words stepped, `coproc` and
 * `function` with the name each takes among them (TOOL-dBoundRoles-87): P1 tail
 * follow, a `tail` carrying a follow option; P2 sleep in a loop, a `sleep` in a command holding a
 * `while` or `until` loop; P3 sleep at or over 5 s, a `sleep` of `POLL_SLEEP_FLOOR_S` or more, or
 * of a duration that does not read. A shell comment is read by no row. A gate row refusing the same command wins, and the background
 * command's exit notification is the wait. The index is read at the checkout root of the payload `cwd`, else of
 * `CLAUDE_PROJECT_DIR`, else of the directory of a candidate's launched script, resolved against the
 * payload `cwd` (TOOL-dBoundRoles-8 S1), so a gate run by absolute path from outside every checkout
 * reads the index of the checkout holding the script. None resolving, G2 and G3 still refuse with an
 * empty allowlist, saying no checkout root was found, and G1 and the polling rows are unarmed with one
 * witness line naming the three starts. THE FIELD MEASUREMENT (TOOL-dBoundRoles-8, gap-orient-09):
 * the typed gate runs a field count found admitted were commands naming a gate script as an
 * argument, a `sed` read, a `grep` alternation inside quotes, a path assigned to a variable, which
 * this arm correctly admits; a census of role gate runs replays the recorded commands through the
 * exported `checkRoleGate` and `scanCommandHeads`, never a regex of its own. An absent
 * index adds no arm, except in a governed tree, where it refuses a candidate naming the re-render
 * (TOOL-dBoundRoles-6 S3); a broken one refuses a candidate; a manifest that does not read leaves G1
 * unarmed with one witness line while G2 and G3 bind; a throw refuses a role agent. THE CEILING:
 * the match is textual, so a gate reached through an interpreter, an alias, a function, an
 * assembled path, a `$(…)` inside quotes, a scoped variant of a leg with an extra argument, or an
 * option missing from the table that takes an argument passes it. The polling rows do not see a
 * poll through a script, an interpreter, a function or an alias, a short `sleep` in a `for` loop, a
 * `sleep` under a shorter `timeout`, a file named like a follow option without `--`, or PowerShell's
 * own wait cmdlets, and they refuse a backgrounded poll too. It stops forgetting, not evasion, and
 * the push-boundary bar is still the guarantee.
 *
 * THE FIFTH CHECK: THE SHELL-WRITE ARM (TOOL-dBoundRoles-7). On a Bash or PowerShell payload
 * carrying an `agent_type`, AFTER the role-gate arm, `checkShellWrites` takes each target the one
 * scanner, scanWriteTargets, finds — `sed -i` and `sed --in-place`, `perl -i`, an interpreter's
 * write call on a string literal (`open(<lit>, "w")`, `Path(<lit>).write_text(`, `writeFileSync(`,
 * `appendFileSync(`, PowerShell's `[IO.File]::WriteAllText(`) in a `python -c`, `node -e` or
 * `python -` / `node` heredoc, each `+++ b/` and `rename to` path of a `git apply` patch, and the
 * shapes checkCommand reads, a redirect through scanRedirects and the operands of a write word through
 * scanWriteOperands, each from its own simple command (TOOL-dBoundRoles-86), its leading reserved words
 * stepped as the polling rows step them (TOOL-dBoundRoles-87) — places it against the
 * payload `cwd`, and judges one in the session's repository with checkRouted on a synthetic `Write` of it, so the route arm, the role arm
 * and step 6b class it exactly as they class an `Edit`. Where the agent's work order, the first
 * `user` record of its transcript, hands an `### allowance` block in its `## Task` section
 * (readWorkOrderAllowance), a target the class admits must also lie under one of its entries
 * (checkRoutedEntry, the matcher the product class reads); a `none` allowance admits no repository
 * write. No transcript, no readable first record or no block holds the write to its class alone,
 * with one witness line. `checkShellWrites` is the predicate and its comment is the ONE evaluation
 * order; a throw refuses a role agent, and the main loop is never judged by it. WHAT STILL ESCAPES:
 * a write from inside a script file the command runs; a target computed at run time (a variable,
 * `os.path.join`, a template literal); a heredoc fed to an interpreter the list does not name; a
 * `sed`, `perl`, `git` or interpreter that does not head its simple command (`xargs sed -i`,
 * `sudo python -c`); `rm`, `mv` of a
 * file out of a folder, `git checkout`, `git restore`, `git stash`, `git merge` and `git am`; a patch
 * read from a pipe, or one whose paths `-p` or `--directory` move, its paths placed against the
 * payload `cwd`; and a transcript an agent rewrites, since it lives outside the repository. Of the
 * redirects and operands (TOOL-dBoundRoles-86): one inside a quoted `$( )` or backticks; an operand
 * after an escaped separator (`a\&b`), or after an unquoted substitution whose parentheses do not
 * balance; a PowerShell operand built in parentheses, and a PowerShell alias or cmdlet the list does not
 * name; a target directory glued to a longer cluster (`-vtDIR`) or an abbreviated `--target-directory`;
 * and the `-d` form of `install`, of which the last operand is read. Three spellings refuse rather than
 * escape, quoting being the remedy: a comparison in more than one nested parenthesis level, one across
 * lines, and an unquoted arrow inside `${ }`. A word like `install` or `touch` heading no command but unquoted in one (`grep -n install x`) still reads
 * as a write, as checkCommand reads it; quoting it is the agent's remedy.
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

const KIT_SCRATCH_GUARD_VERSION = '1.2' // gov:kit agent-cap@1.52 — ships inside the hooks kit entry
// TOOL-dBoundRoles-25 S8: the hooks kit's version, which the retired hook file carried until TOOL-dBoundRoles-25; the kit keeps its
// registry id `agent-cap` (§8 F5), and its `version_from` reads this constant.
const KIT_AGENT_CAP_VERSION = '1.52' // gov:kit agent-cap@1.52 — engine identity (this file is deployed verbatim; the constant is the deployer's version marker)

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
 * Every heredoc of <cmd>, left to right: `[{ open, from, to }]`, `open` the offset of its `<<`
 * opener, and `cmd.slice(from, to)` its body, the lines between the opener's line and the line
 * holding its tag alone. `to <= from` is reachable: an EMPTY body puts the terminator on the line
 * immediately after the opener, so the computed span is -1. Found by the corpus probe, not by
 * reasoning — the smoke fixtures all had non-empty bodies. A body is skipped whole, so an opener
 * spelled inside one is not read as another. buildCommandView blanks these bodies, and the
 * shell-write scan reads the one a simple command opens (TOOL-dBoundRoles-7 S1).
 */
function readHeredocBodies(cmd) {
  const out = []
  const here = /<<-?\s*(['"]?)([A-Za-z_][A-Za-z0-9_]*)\1/g
  let hm
  while ((hm = here.exec(cmd)) !== null) {
    const bodyStart = cmd.indexOf('\n', hm.index)
    if (bodyStart === -1) break
    const end = cmd.slice(bodyStart).search(new RegExp('\\n[ \\t]*' + hm[2] + '[ \\t]*(?:\\n|$)'))
    const bodyEnd = end === -1 ? cmd.length : bodyStart + end
    out.push({ open: hm.index, from: bodyStart + 1, to: bodyEnd })
    here.lastIndex = Math.max(bodyEnd, hm.index + hm[0].length)
  }
  return out
}

/**
 * Blank the CONTENTS of quoted strings and heredoc bodies, preserving length so offsets still line
 * up with the original. Operators are then located in this view and targets read from the original.
 * A backslash escapes a quote in a double-quoted run, except where <tool> is `PowerShell`.
 */
function buildCommandView(cmd, tool) {
  const buildBlankedRun = (s, from, to) =>
    to <= from ? s : s.slice(0, from) + ' '.repeat(to - from) + s.slice(to)
  let view = cmd

  // Heredoc bodies first: their contents can hold anything, including quotes that would desync a
  // naive quote scanner.
  for (const h of readHeredocBodies(cmd)) view = buildBlankedRun(view, h.from, h.to)

  // Then quoted runs, single and double, left to right.
  let out = ''
  let i = 0
  while (i < view.length) {
    const ch = view[i]
    if (ch === "'" || ch === '"') {
      let j = i + 1
      while (j < view.length && view[j] !== ch) {
        if (ch === '"' && view[j] === '\\' && tool !== 'PowerShell') j++
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

/** The write words: every operand after one of the first list is a target, the last operand of one of the second. */
const WRITE_ANY_ARG = ['tee', 'touch', 'mkdir', 'Out-File', 'Set-Content', 'Add-Content', 'New-Item']
const WRITE_LAST_ARG = ['cp', 'mv', 'install', 'rsync']
/** Every redirect operator, its descriptor only where one opens a word (TOOL-dBoundRoles-86 S3). */
const REDIRECT = /(?:(?<![^\s;|&()<>])(?:\{[A-Za-z_]\w*\}|\d+))?(?:&>>?|<>|[<>]&|>>?\|?|<{1,3}-?)/g
/** A redirect's word in the view, where a quoted run is blank and a substitution may be a filler. */
const REDIRECT_WORD = /(?:"[^"]*"|'[^']*'|[^\s;|&()<>"'])+/y
/**
 * The spans whose arrows compare (S4): a `(( ))` whose parentheses balance up to the closing pair, which
 * the fallback `((echo x) > f; (true))` does not; and a `[[ ... ]]` on one line that opens at command
 * position, which `echo [[ a > f ]]` does not.
 */
const COMPARISON = /\(\((?:[^()]|\([^()]*\))*\)\)|(?:^|(?<![\\>])[;&|\n]|(?<!\\)\(|\(\))[ \t]*(?:(?:if|elif|while|until|then|else|do|!|\{)[ \t]+)*\[\[[ \t][^\n]*?[ \t]\]\]/g
const TMP_ASSIGN = /(?:^|[\s;&|(])(TMPDIR|TMP|TEMP)=/g

/**
 * The text of one shell word without its quotes. In a double-quoted run an escaped quote is part of the
 * run and loses its backslash, so a `bash -c` body is read as the shell reads it (TOOL-dBoundRoles-86
 * S6); no other backslash goes, so a Windows path keeps its own.
 */
function readWordText(raw) {
  return raw.replace(/"((?:\\[\s\S]|[^"\\])*)"|'([^']*)'|"([^"]*)"/g, (_, d, s, e) =>
    d !== undefined ? d.replace(/\\([\s\S])/g, (w, c) => (c === '"' ? c : w)) : s !== undefined ? s : e)
}

/**
 * The redirects of a command (TOOL-dBoundRoles-86 S3, S4): `{ targets, view }`, the word of each output
 * redirect in order, read from <cmd>, and <view> with every operator and its word blanked to the same
 * length, so offsets hold. <view> is string- and comment-blanked; an operator is matched after any
 * character and its word starts past blanks, so a glued `a>f`, `>|`, `&>>`, `<>`, `>&f` and, in
 * PowerShell, `*>` each read `f`. The word ends at unquoted whitespace, `;`, `|`, `&`, `(`, `)`, `<` or
 * `>`. No target comes from an input redirect, a duplication or a close (`n>&m`, `n>&-`), a process
 * substitution, or, outside PowerShell, an arrow of a COMPARISON span or one behind a backslash. An arrow
 * after `=` or `-` is a redirect like any other. What it does not see: an operator inside quotes, a
 * quoted `$( )` included. A word before a closing backtick keeps it, and a comparison in more nested
 * parentheses than COMPARISON holds, or one across lines, reads as a redirect, as does an unquoted arrow
 * inside `${ }`.
 */
function scanRedirects(cmd, view, tool) {
  const ps = tool === 'PowerShell'
  const seen = ps ? view : view
    .replace(COMPARISON, (w) => w.replace(/[<>]/g, ' '))
    .replace(/\\[\s\S]/g, (w) => (/[<>]/.test(w) ? '  ' : w))
  const targets = []
  let out = ''
  let from = 0
  let m
  REDIRECT.lastIndex = 0
  while ((m = REDIRECT.exec(seen)) !== null) {
    const op = m[0]
    const star = ps && seen[m.index - 1] === '*' && (m.index === 1 || /[\s;|&({]/.test(seen[m.index - 2]))
    const at = star ? m.index - 1 : m.index
    let end = m.index + op.length
    if (seen[end] !== '(') {
      const copy = /[<>]&$/.test(op) ? (ps ? /[ \t]*\d+/y : /[ \t]*(?:\d+-?|-)(?![^\s;&|()<>`])/y) : null
      if (copy) copy.lastIndex = end
      const dup = copy && copy.exec(view)
      if (dup) end += dup[0].length
      else {
        while (view[end] === ' ' || view[end] === '\t') end++
        REDIRECT_WORD.lastIndex = end
        const w = REDIRECT_WORD.exec(view)
        if (w) {
          if (op.includes('>')) targets.push(readWordText(cmd.slice(end, end + w[0].length)))
          end += w[0].length
        }
      }
    }
    out += view.slice(from, at) + ' '.repeat(end - at)
    from = end
    REDIRECT.lastIndex = end
  }
  return { targets, view: out + view.slice(from) }
}

/**
 * The outermost unquoted substitutions of <view>, `$( )`, `<( )` and `>( )`, left to right, each
 * `{ from, to, body }`, `body` the bounds of the text it runs. One whose parentheses do not balance is
 * left out. The body of a `$((` keeps the outer parentheses, so an arithmetic one reads as one.
 */
function scanSubstitutions(view, tool) {
  const open = []
  const spans = []
  for (let i = 0; i < view.length; i++) {
    const ch = view[i]
    if (ch === '\\' && tool !== 'PowerShell') i++
    else if (ch === '(') open.push(i)
    else if (ch === ')' && open.length) {
      const at = open.pop()
      if (at === 0 || !'$<>'.includes(view[at - 1])) continue
      while (spans.length && spans[spans.length - 1].from > at) spans.pop()
      spans.push({ from: at - 1, to: i + 1, body: view[at - 1] === '$' && view[at + 1] === '(' ? [at, i + 1] : [at + 1, i] })
    }
  }
  return spans
}

/**
 * The write targets of one inline entry <c> of scanCommandHeads, as `[value, why]` pairs
 * (TOOL-dBoundRoles-86 S1, S2). A write word counts as the head, by basename, or as an unquoted word at
 * any later place of the same simple command, so `sudo cp`, `xargs touch` and a `cp` behind a reserved
 * word are read. A WRITE_ANY_ARG word takes every operand after it, a WRITE_LAST_ARG word the last one,
 * and `cp`, `mv` and `install` the directory of `-t <dir>`, a short cluster ending in `t`, `-t<dir>` or
 * `--target-directory`, their operands then being sources. An option word is no operand, nor is the
 * backslash `find`'s escaped `;` leaves.
 */
function scanWriteOperands(c) {
  const out = []
  c.raw.forEach((raw, i) => {
    const base = i === 0 ? buildBaseName(c.head) : ''
    const name = [...WRITE_ANY_ARG, ...WRITE_LAST_ARG].find((w) => (i === 0 ? w.toLowerCase() === base : w === raw))
    if (!name) return
    const rest = c.argv.slice(i + 1)
    const ops = rest.filter((w) => w !== '' && w !== '\\' && !w.startsWith('-'))
    if (WRITE_ANY_ARG.includes(name)) {
      for (const v of ops) out.push([v, name])
      return
    }
    let dest = ops[ops.length - 1]
    for (let k = 0; name !== 'rsync' && k < rest.length && rest[k] !== '--'; k++) {
      const glued = /^(?:-t|--target-directory=)([\s\S]+)$/.exec(rest[k])
      if (glued) dest = glued[1]
      else if (/^(?:-[A-Za-z]*t|--target-directory)$/.test(rest[k]) && rest[k + 1] !== undefined) dest = rest[k + 1]
      else continue
      break
    }
    if (dest !== undefined) out.push([dest, `${name} destination`])
  })
  return out
}

/**
 * TOOL-dBoundRoles-7 S1: an interpreter's write call whose first argument is a string literal, the
 * literal being group 2. Python's `open(<lit>, <mode>)` is a write only where the mode literal holds
 * `w`, `a`, `x` or `+`, which the caller tests on group 4; a computed path or mode matches nothing.
 */
const INTERPRETER_WRITES = [
  /\bopen\(\s*[rR]?(['"])([^'"\n]+)\1\s*,\s*(?:mode\s*=\s*)?[rRbB]?(['"])([^'"\n]*)\3/g,
  /\bPath\(\s*[rR]?(['"])([^'"\n]+)\1\s*\)\s*\.\s*write_(?:text|bytes)\(/g,
  /\b(?:writeFileSync|appendFileSync)\(\s*(['"`])([^'"`\n]+)\1/g,
  /\[(?:System\.)?IO\.File\]::(?:WriteAllText|WriteAllBytes|AppendAllText)\(\s*(['"])([^'"\n]+)\1/gi,
]
/** The bound on a patch file the `git apply` shape reads, in bytes. */
const PATCH_READ_BOUND = 256 * 1024

/** The string-literal path of every INTERPRETER_WRITES call in <body>; a template literal holding `${` is computed. */
function scanInterpreterWrites(body) {
  const out = []
  for (const rx of INTERPRETER_WRITES) {
    rx.lastIndex = 0
    let m
    while ((m = rx.exec(String(body))) !== null) {
      if (m[4] !== undefined && !/[wax+]/.test(m[4])) continue
      if (!m[2].includes('${')) out.push(m[2])
    }
  }
  return out
}

/** The perl short switches whose value is the rest of their word, per perlrun. */
const PERL_VALUE_SWITCHES = 'MmIFCDxV'
/**
 * The file operands of a `sed` or `perl` simple command's <argv> that edits in place, or [] when it
 * carries no in-place option. In a short cluster `i` takes the rest as its backup suffix, so `-Ei`
 * is in place and `-ie` is in place with suffix `e`, as GNU sed reads them; `--in-place[=<suffix>]`
 * is sed's long form. The script is the first operand unless an `-e` or `-f` (perl `-e` or `-E`)
 * named it; an empty word, BSD sed's `-i ''` suffix, is no operand. A switch of PERL_VALUE_SWITCHES ends
 * a perl cluster, and a bare `-I` takes the next word, so `-MList::Util` is not in place. A `--` ends
 * the options and no more: the first word after it is still the script while none was named.
 */
function scanInPlaceOperands(argv) {
  const perl = buildBaseName(argv[0]) === 'perl'
  let inPlace = false
  let script = false
  let ended = false
  const files = []
  for (let k = 1; k < argv.length; k++) {
    const w = argv[k]
    if (w === '') continue
    if (!ended && w === '--') { ended = true; continue }
    if (!ended && !perl && /^--in-place(?:=|$)/.test(w)) { inPlace = true; continue }
    if (!ended && !perl && /^--(?:expression|file)$/.test(w)) { script = true; k++; continue }
    if (!ended && /^--/.test(w)) { if (/^--(?:expression|file)=/.test(w)) script = true; else if (w === '--line-length') k++; continue }
    if (!ended && /^-[A-Za-z0-9]/.test(w)) {
      for (let i = 1; i < w.length; i++) {
        const ch = w[i]
        if (perl && PERL_VALUE_SWITCHES.includes(ch)) {
          if (ch === 'I' && i === w.length - 1) k++
          break
        }
        if (ch === 'i') { inPlace = true; break }
        if ((perl ? 'eE' : 'ef').includes(ch) || (!perl && ch === 'l')) {
          if (ch !== 'l') script = true
          if (i === w.length - 1) k++
          break
        }
      }
      continue
    }
    if (!script) { script = true; continue }
    files.push(w)
  }
  return inPlace ? files : []
}

/**
 * The paths a `git` simple command's patch writes, or [] when it is no `git apply`, or one of
 * `--check`, `--stat`, `--numstat` and `--summary` makes it write nothing. Each patch operand is
 * read, resolved against <cwd> when relative (a relative one with no <cwd> is not read), up to
 * PATCH_READ_BOUND bytes; with no operand, or `-`, the heredoc the command opens, <here>, is the
 * patch. A path is each `+++ b/<path>` line's, tab and its tail dropped, and each `rename to <path>`
 * line's. A patch read from a pipe is not seen.
 */
function scanPatchTargets(argv, here, cwd) {
  const fs = require('fs')
  const path = require('path')
  let k = 1
  for (; k < argv.length && argv[k].startsWith('-'); k++) if (GIT_VALUE_FLAGS.includes(argv[k])) k++
  if (argv[k] !== 'apply') return []
  const ops = argv.slice(k + 1)
  if (ops.some((w) => /^--(?:check|stat|numstat|summary)$/.test(w)) && !ops.includes('--apply')) return []
  const files = []
  for (let i = 0; i < ops.length; i++) {
    if (['--directory', '--exclude', '--include', '--whitespace'].includes(ops[i])) i++
    else if (ops[i] === '-' || !ops[i].startsWith('-')) files.push(ops[i])
  }
  const texts = []
  if (files.length === 0 || files.includes('-')) texts.push(here || '')
  for (const f of files.filter((x) => x !== '-')) {
    const native = buildNativePath(f)
    if (!path.isAbsolute(native) && !cwd) continue
    let fd = null
    try {
      fd = fs.openSync(cwd ? path.resolve(buildNativePath(cwd), native) : native, 'r')
      const buf = Buffer.alloc(PATCH_READ_BOUND)
      texts.push(buf.toString('utf8', 0, fs.readSync(fd, buf, 0, PATCH_READ_BOUND, 0)))
    } catch { /* an unreadable patch writes nothing this scan can name */ } finally { if (fd !== null) fs.closeSync(fd) }
  }
  const out = []
  for (const t of texts) {
    for (const l of t.split('\n')) {
      const m = /^\+\+\+ "?b\/(.+?)"?(?:\t.*)?\r?$/.exec(l) || /^rename to (.+?)\r?$/.exec(l)
      if (m) out.push(m[1])
    }
  }
  return out
}

/**
 * Locate write targets, each `value` and `why` pair once. Redirects and operands come from the entries
 * scanCommandHeads yields in its inline mode, so neither is read past its own simple command
 * (TOOL-dBoundRoles-86): scanRedirects reads the redirects, one of a `-c` body included, and
 * scanWriteOperands the operands of `tee`, `touch`, `mkdir`, the PowerShell write cmdlets, `cp`, `mv`,
 * `install` and `rsync`. The last four take their LAST operand only, or a target-directory option's
 * directory: they read a source first, and a home-rooted SOURCE is a read. A word opening with `<(` or
 * `>(` is no target. A temp-root assignment is located in the blanked VIEW and read from the ORIGINAL,
 * so a quoted target still resolves while a quoted operator stays invisible. <tool>, the tool's name,
 * tells scanRedirects which syntax the command is in; without it the command reads as Bash.
 *
 * TOOL-dBoundRoles-7 S1 adds four shapes, read per simple command through scanCommandHeads' inline
 * mode: the file operands of `sed -i` (and `perl -i`, its own `why`); the string-literal first
 * argument of an INTERPRETER_WRITES call inside a `python`, `python3` or `py` `-c` body, a `node -e`
 * body, or the heredoc a `python -`, `python3 -` or `node` with no script reads; PowerShell's
 * `[IO.File]::` write calls in the command itself; and each path a `git apply` patch names. <cwd>,
 * the payload's, places a relative patch file; without it only an absolute one is read.
 */
function scanWriteTargets(cmd, cwd, tool) {
  const view = buildCommandView(cmd)
  const found = []
  const pairs = new Set()
  const addTarget = (value, why) => {
    if (!value || /^(?:-|[<>]\()/.test(value) || pairs.has(`${why}\0${value}`)) return
    pairs.add(`${why}\0${value}`)
    found.push({ value, why })
  }
  for (const c of scanCommandHeads(cmd, 0, { inline: true, reserved: true, tool })) {
    if (c.redirect !== undefined) {
      addTarget(c.redirect, 'redirect')
      continue
    }
    if (c.inline !== undefined) {
      for (const v of scanInterpreterWrites(c.inline)) addTarget(v, 'interpreter write')
      continue
    }
    for (const [v, why] of scanWriteOperands(c)) addTarget(v, why)
    const base = buildBaseName(c.head)
    if (base === 'sed' || base === 'perl') for (const v of scanInPlaceOperands(c.argv)) addTarget(v, `${base} -i`)
    else if (base === 'git') for (const v of scanPatchTargets(c.argv, c.here, cwd)) addTarget(v, 'git apply')
  }
  // PowerShell's write calls, located in the VIEW so a quoted mention is invisible, the literal read
  // from the ORIGINAL at the same offset.
  const call = new RegExp(INTERPRETER_WRITES[3].source, 'gi')
  const opener = /\[(?:System\.)?IO\.File\]::(?:WriteAllText|WriteAllBytes|AppendAllText)\(/gi
  let pm
  while ((pm = opener.exec(view)) !== null) {
    call.lastIndex = pm.index
    const lit = call.exec(cmd)
    if (lit && lit.index === pm.index) addTarget(lit[2], 'interpreter write')
  }

  TMP_ASSIGN.lastIndex = 0
  let m
  while ((m = TMP_ASSIGN.exec(view)) !== null) addTarget(readTokenAt(cmd, m.index + m[0].length), 'temp-root assignment')
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
 * the retired agent limit hook made for its slot ledger, and the branch every real session in this repo takes.
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

/** The bound on the kickoff checker's `--card --path` answer, in milliseconds. */
const CARD_PATH_BOUND_MS = 10000

/**
 * The kickoff checker `manifest-check.sh`, the one reader of where a card lives (TOOL-dPlacedRequest-2
 * S10), resolved from this hook's OWN install and nowhere else: the kit resolver from this hook's own
 * directory, else the ONE file of that name the hook's own repository tracks — gov homes that kit
 * under `skills/`, where no probe walks, as the roles kit's `resolve_card_path` finds it. The commit
 * or edit target's tree is never a rung (TOOL-dPlacedRequest-95): its tracked checker is code that
 * repository authored, and it would run inside PreToolUse on this node. null when neither answers.
 */
function resolveKickoffChecker() {
  const fs = require('fs')
  const path = require('path')
  const { spawnSync } = require('child_process')
  try {
    return path.join(resolveKitDir('session-kickoff', 'manifest-check.sh', __dirname), 'manifest-check.sh')
  } catch { /* the next rung */ }
  const hit = resolveToplevel(__dirname)
  if (!hit) return null
  let r
  try {
    r = spawnSync('git', ['ls-files', '--', 'manifest-check.sh', '*/manifest-check.sh'], { cwd: hit.toplevel, encoding: 'utf8', timeout: 20000, windowsHide: true })
  } catch { return null }
  const hits = r && r.status === 0 ? String(r.stdout || '').split(/\r?\n/).filter(Boolean) : []
  if (hits.length === 1 && fs.existsSync(path.join(hit.toplevel, hits[0]))) return path.join(hit.toplevel, hits[0])
  return null
}

/**
 * The bash that can SEE `checker`, by RUNNING each candidate (TOOL-dPlacedRequest-34 S28), in
 * the order of `resolve_bash` in the lib kit's resolve_bash.py, as the policy kit's policy-mirror.js
 * `resolveBash` ports it: GOV_BASH, then each `bash` PATH names in order, then Git for Windows' two, then the bare name,
 * each kept only when `test -f "$1"` on the checker exits 0 under it, so a WSL launcher or a stub on
 * PATH is skipped rather than trusted. null with none, `why` naming the last miss.
 */
function resolveCardBash(checker) {
  const fs = require('fs')
  const path = require('path')
  const { spawnSync } = require('child_process')
  const onPath = (process.env.PATH || process.env.Path || '').split(path.delimiter).filter(Boolean)
    .flatMap((d) => [path.join(d, 'bash.exe'), path.join(d, 'bash')]).filter((p) => { try { return fs.statSync(p).isFile() } catch { return false } })
  const cands = [process.env.GOV_BASH || '', ...onPath, 'C:/Program Files/Git/bin/bash.exe', 'C:/Program Files/Git/usr/bin/bash.exe', 'bash']
  let why = 'no candidate ran'
  for (const c of cands.filter((b, i, all) => b && all.indexOf(b) === i)) {
    let r
    try {
      r = spawnSync(c, ['-c', 'test -f "$1"', '_', checker], { encoding: 'utf8', input: '', timeout: CARD_PATH_BOUND_MS, windowsHide: true })
    } catch (e) { why = `${c}: ${String((e && e.message) || e)}`; continue }
    if (r && !r.error && r.status === 0) return { bash: c, why: '' }
    why = `${c}: ${r && r.error ? String(r.error.message || r.error) : `test -f exited ${r ? r.status : '?'}`}`
  }
  return { bash: null, why }
}

/**
 * The card's bytes, or `text: null` when none exists, with `shown` its one comparable spelling. The
 * path is the kickoff checker's `--card --path --session <sid>` answer, run from the common dir's
 * work tree with stdin closed and a bound, so this hook never derives it beside the checker, by the
 * bash `resolveCardBash` finds; an MSYS `/c/…` answer is folded by `buildNativePath`. A checker that
 * resolves nowhere, no bash that can see it, or a checker that runs silent reads as no card, `shown`
 * naming why. `checker` overrides the resolved one, for the self-test's stub. A non-id-shaped
 * session id is never passed on.
 */
function readCard(commonDir, sessionId, checker) {
  const fs = require('fs')
  const path = require('path')
  const { spawnSync } = require('child_process')
  const sid = String(sessionId)
  const card = { path: null, text: null, shown: '' }
  if (!/^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(sid)) {
    card.shown = `(no card: the session id ${JSON.stringify(sid)} is not id-shaped)`
    return card
  }
  const cwd = path.basename(commonDir) === '.git' ? path.dirname(commonDir) : commonDir
  const engine = checker === undefined ? resolveKickoffChecker() : checker
  if (!engine) {
    card.shown = '(no card: no kickoff checker manifest-check.sh resolves to answer --card --path)'
    return card
  }
  const found = resolveCardBash(engine)
  if (!found.bash) {
    card.shown = `(no card: no bash can see the kickoff checker ${engine}: ${found.why})`
    return card
  }
  const bash = found.bash
  let why = ''
  let r
  try {
    // RUN AS runLiveness RUNS THE DRIVER (TOOL-dPlacedRequest-43 S18): the bound kills with SIGKILL, and
    // stdin is closed rather than piped, so a checker that never answers, or a grandchild holding its
    // stdout, reads as no card within the bound.
    r = spawnSync(bash, [engine, '--card', '--path', '--session', sid], { cwd, encoding: 'utf8', timeout: CARD_PATH_BOUND_MS, killSignal: 'SIGKILL', stdio: ['ignore', 'pipe', 'pipe'], windowsHide: true })
  } catch (e) { why = String((e && e.message) || e) }
  const out = r && !r.error && r.status === 0 ? String(r.stdout || '').trim().split(/\r?\n/)[0] : ''
  if (out) {
    // An MSYS bash prints /c/…, folded by buildNativePath; any other POSIX spelling on Windows, a
    // /tmp/… mount say, is asked of the same bash's cygpath, and kept as printed where that does not answer.
    let native = buildNativePath(out)
    if (native === out && process.platform === 'win32' && out.startsWith('/')) {
      try {
        const c = spawnSync(bash, ['-c', 'cygpath -m -- "$1"', '_', out], { encoding: 'utf8', timeout: CARD_PATH_BOUND_MS, killSignal: 'SIGKILL', stdio: ['ignore', 'pipe', 'pipe'], windowsHide: true })
        const w = c && c.status === 0 ? String(c.stdout || '').trim() : ''
        if (/^[A-Za-z]:\//.test(w)) native = w
      } catch { /* kept as printed */ }
    }
    card.path = native
    card.shown = buildComparablePath(card.path)
    try { card.text = fs.readFileSync(card.path, 'utf8') } catch { /* absent */ }
    return card
  }
  if (!why) why = r && r.error ? String(r.error.message || r.error) : `exit ${r ? r.status : '?'}: ${String((r && (r.stdout || r.stderr)) || '').trim().split(/\r?\n/)[0] || 'nothing printed'}`
  card.shown = `(no card: the kickoff checker's --card --path did not answer: ${why})`
  return card
}

/**
 * The ONE front-matter reader both hooks in this home use: the single-token value of `<key>:` on
 * its own line inside a build README's front matter, or null. FRONT MATTER ONLY — the slice between
 * the opening `---` on line 1 and the next `---` line, the scope the unattended driver reads its
 * keys in. Matching the whole file exempted a README whose BODY carried `authorized-by:` in a fenced
 * example while the driver authorized nothing (F10); the review kit's spec-audit-optin.js reads
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
/** The memory-tree conf at the target's toplevel; precedent for a root-level conf literal: the retired agent limit hook's conf. */
const ROUTE_CONF = '.memory-tree.conf'

/**
 * The LAST `<key>=` assignment's value in a shell-style conf, as the shell reads it: double- or
 * single-quoted or bare, an optional `export`, a trailing `# comment` only behind whitespace — a `#`
 * glued to a bare word is part of the word. null when no assignment exists; the value is RAW. The
 * key is compared as a string and never put into a regex (`conf-value-interpolated-into-a-regex`).
 * Lifted from the agent limit hook's `readSpecAuditDefault`, which delegated here: one conf grammar
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
 * TOOL-dBoundRoles-38 S3 - the hooks' one fence walker, the roles kit's `read_unfenced_lines` spelled again,
 * as a kit imports no sibling kit: `[line number, line]` for every line of `text` outside a fence, split on
 * LF with any CR kept, then `[opened at, null]` when the text ends inside one. A fence opens on a line of at
 * most three spaces of indent and then three or more backticks or three or more tildes, and closes only on a
 * line of the same character whose run is at least as long, with nothing after it but whitespace; a fence
 * line is yielded by neither end. So a shorter run inside a longer fence is content, and a fact or marker
 * line quoted inside handed content is read as neither. CommonMark's info-string rule holds too
 * (TOOL-dBoundRoles-50 S9): a backtick run whose line holds a backtick after the run opens no fence, so an
 * inline span of three backticks is a line of text. The hooks kit holds no other walker: the H1 scan
 * `readSpecH1Id` and format-guard's `scanMessageLines` both read their lines here.
 */
function * readUnfencedLines(text) {
  let fence = ''
  let openedAt = 0
  const lines = String(text).split('\n')
  for (let i = 0; i < lines.length; i++) {
    const m = /^ {0,3}(`{3,}|~{3,})([\s\S]*)$/.exec(lines[i])
    if (!fence) {
      if (m && !(m[1][0] === '`' && m[2].includes('`'))) { fence = m[1]; openedAt = i + 1; continue }
      yield [i + 1, lines[i]]
    } else if (m && m[1][0] === fence[0] && m[1].length >= fence.length && /^[ \t\r]*$/.test(m[2])) {
      fence = ''
    }
  }
  if (fence) yield [openedAt, null]
}

/**
 * A spec's H1 id, '' when it has none (S8): the first UNFENCED `#` line, its first token with backticks and
 * asterisks stripped and trailing `:.,;` dropped. checkBuildable and readDispatchedUnits both read it here
 * (TOOL-aSmoothedDispatch-6 S4), its lines those `readUnfencedLines` yields. Its two twins are KICK R4, which is
 * manifest-check.sh's `check_card_route`, and tree_lib's `parse_spec_h1`, which walks `unfenced_lines` with
 * `by_length`. All three share one fence rule, the length rule (TOOL-dBoundRoles-50 S9, TOOL-dBoundRoles-56): a
 * fence opens on at most three spaces and a run of three or more, a backtick run whose line holds a backtick
 * after it opens nothing, and the fence closes only on a run of its character at least as long with nothing but
 * whitespace after it. Beyond fences they differ: R4 takes any unfenced H1 naming the unit, the other two the first.
 */
function readSpecH1Id(text) {
  for (const [, raw] of readUnfencedLines(String(text || ''))) {
    const l = raw === null ? '' : raw.replace(/\r$/, '')
    if (!/^#[ \t]/.test(l)) continue
    return (l.split(/[ \t]+/)[1] || '').replace(/[`*]/g, '').replace(/[:.,;]+$/, '')
  }
  return ''
}

/** The unattended driver's run-state file in a build folder; the suite holds it equal to the driver's `runmd_of`. */
const RUN_STATE_FILE = 'RUN.md'

/**
 * TOOL-aSmoothedDispatch-6 S1: the units the build's run-state file records as dispatched.
 * `{ file, units: [{ unit, spec }] }`, `file` the comparable path of `<MEMORY_ROOT>/builds/<build>/RUN.md`,
 * units in first-appearance order, each once. A row is the driver's `--dispatch` row, matched as its
 * order gate matches it. `spec` is the repo-relative path of the first `.md` under the build's `spec/`,
 * at any depth, whose H1 names the unit, spelled with the prefix checkBuildable accepts, or '' when
 * none does. An empty build, or a file that is absent or unreadable, is an empty list: the fallback
 * only ever adds an admission, so a failed read leaves the card's verdict standing.
 */
function readDispatchedUnits(top, memRoot, build) {
  const fs = require('fs')
  const path = require('path')
  const folder = path.join(top, buildNativePath(memRoot), 'builds', buildNativePath(build))
  const file = buildComparablePath(path.join(folder, RUN_STATE_FILE))
  if (!build) return { file, units: [] }
  let text
  try { text = fs.readFileSync(path.join(folder, RUN_STATE_FILE), 'utf8') } catch { return { file, units: [] } }
  const ids = []
  for (const l of text.split('\n')) {
    const m = /^\d{4}-\d{2}-\d{2}T[0-9:]+Z dispatch · item [0-9a-f]+ (\S+) · reason /.exec(l.replace(/\r/g, ''))
    if (m && !ids.includes(m[1])) ids.push(m[1])
  }
  if (ids.length === 0) return { file, units: [] }
  const found = new Map()
  const scanSpecs = (dir, rel) => {
    let ents
    try { ents = fs.readdirSync(dir, { withFileTypes: true }) } catch { return }
    for (const e of ents.sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0))) {
      const r = `${rel}/${e.name}`
      if (e.isDirectory()) { scanSpecs(path.join(dir, e.name), r); continue }
      if (!e.isFile() || !e.name.endsWith('.md')) continue
      let t
      try { t = fs.readFileSync(path.join(dir, e.name), 'utf8') } catch { continue }
      const id = readSpecH1Id(t)
      if (ids.includes(id) && !found.has(id)) found.set(id, r)
    }
  }
  scanSpecs(path.join(folder, 'spec'), `${memRoot}/builds/${build}/spec`)
  return { file, units: ids.map((unit) => ({ unit, spec: found.get(unit) || '' })) }
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
  const h1Id = readSpecH1Id(text)
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
 * `{ state: 'ok', shown, roles, harnesses, gates, effort }` otherwise. Only the shape is checked: the value set of
 * `writes` belongs to the index's generator, and a value outside it simply admits no class here.
 * TOOL-aOrientedCast-11 adds two OPTIONAL keys, graded only when present: a role's `gates`, a list of
 * strings, and the top-level `gates`, `{ manifest: <string|null> }`; `gates` is null when absent.
 * TOOL-aGuardedEffort-1 adds a third: the top-level `effort`, a plain object whose `default`,
 * `profiles`, `harnesses` and `unset` are plain objects; `effort` is null when absent.
 * TOOL-dBoundRoles-6 S5 adds a fourth: a role's `role-sha`, 12 lowercase hex digits, the hash of the
 * `## Role` section a handoff of it carries, which the spawn guard's rule 6 (spawn-guard.js) compares at spawn.
 * TOOL-dBoundRoles-9 S3 adds a fifth: the top-level `classes`, a plain object whose every value is a
 * string, each write class's folder as the roles kit's `WRITE_FOLDERS` spells it; null when absent.
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
    // TOOL-dBoundRoles-6 S5: a role's `role-sha`, when present, is 12 lowercase hex digits.
    if (r['role-sha'] !== undefined && !(typeof r['role-sha'] === 'string' && /^[0-9a-f]{12}$/.test(r['role-sha']))) {
      return { state: 'broken', shown, why: `${shape}: role ${n}'s role-sha is not 12 lowercase hex digits` }
    }
  }
  // ...and the top-level `gates`, when present, is `{ manifest: <string|null> }`. Absent reads as no manifest.
  const gates = d.gates
  if (gates !== undefined && (!gates || typeof gates !== 'object' || Array.isArray(gates)
    || !(gates.manifest === null || typeof gates.manifest === 'string'))) {
    return { state: 'broken', shown, why: `${shape}: gates is not { manifest: <string|null> }` }
  }
  // TOOL-aGuardedEffort-1 S2: the top-level `effort`, when present, is a plain object whose four keys
  // are plain objects; spawn-guard.js's rule 8 reads it. Absent reads as null, which adds no rule there.
  const effort = d.effort
  const checkPlain = (v) => !!v && typeof v === 'object' && !Array.isArray(v)
  if (effort !== undefined && !(checkPlain(effort) && ['default', 'profiles', 'harnesses', 'unset'].every((k) => checkPlain(effort[k])))) {
    return { state: 'broken', shown, why: `${shape}: effort is not { default: {…}, profiles: {…}, harnesses: {…}, unset: {…} }` }
  }
  // TOOL-dBoundRoles-9 S3: the top-level `classes`, when present, maps each write class to its folder.
  const classes = d.classes
  if (classes !== undefined && !(checkPlain(classes) && Object.values(classes).every((v) => typeof v === 'string'))) {
    return { state: 'broken', shown, why: `${shape}: classes is not { <class>: <string> }` }
  }
  return { state: 'ok', shown, roles: d.roles, harnesses: d.harnesses, gates: gates || null, effort: effort || null, classes: classes || null }
}

/** The folder the roles kit renders agent types into, beside the index: `.claude/agents/`. */
const ROLE_AGENTS_DIR = ROLE_INDEX.replace(/[^/]+$/, 'agents/')

/**
 * TOOL-dBoundRoles-6 §4 "A governed tree": true when `.claude/agents/` at `top` holds a `.md` file whose
 * front matter, read by readFrontMatterKey, carries both `workflow` and `writes`, the two gov keys the
 * roles kit's renderer writes and Claude Code's own agent files never carry. Exported beside
 * loadRoleIndex, so spawn-guard.js reads it through this one reader. Asked only where the index is absent,
 * so a tree whose index was deleted while its renders remain is governed and refused, and a tree that
 * never adopted the roles kit keeps its no-arm verdict. A folder or file that does not read is not
 * governed. WHAT IT DOES NOT SEE: a tree whose index and every rendered agent file were both deleted.
 */
function checkRoleGoverned(top) {
  const fs = require('fs')
  const path = require('path')
  let names
  try { names = fs.readdirSync(path.join(top, ROLE_AGENTS_DIR)) } catch { return false }
  for (const n of names.filter((x) => x.toLowerCase().endsWith('.md')).sort()) {
    let text = null
    try { text = fs.readFileSync(path.join(top, ROLE_AGENTS_DIR, n), 'utf8') } catch { text = null }
    if (text !== null && readFrontMatterKey(text, 'workflow') !== null && readFrontMatterKey(text, 'writes') !== null) return true
  }
  return false
}

/**
 * Step 5a of the write gate (TOOL-dBoundRoles-6 S1): `{ deny }` when `rel`, the target's comparable
 * repo-relative path at `top`, is the role index, or the agent file `.claude/agents/<name>.md` of a
 * role the index at `top` names; null otherwise. Every writer is refused, a role agent and the main
 * loop alike: the renderer writes both, and its `--write` is the one door. An adopter's own file under
 * `.claude/agents/`, named by no index row, and any agent file while the index does not read as ok,
 * fall through to the steps after it.
 */
function checkRenderedRole(tool, targetC, rel, top) {
  const dir = ROLE_AGENTS_DIR.toLowerCase()
  let owned = rel === ROLE_INDEX.toLowerCase()
  if (!owned && rel.startsWith(dir) && rel.endsWith('.md') && !rel.slice(dir.length).includes('/')) {
    const index = loadRoleIndex(top)
    const name = rel.slice(dir.length, -'.md'.length)
    owned = index.state === 'ok' && Object.keys(index.roles).some((n) => n.toLowerCase() === name)
  }
  if (!owned) return null
  return { deny: `BLOCKED by scratch-guard: ${targetC} is rendered by render_agents.py --write, and no writer edits it by hand. This ${tool} is refused for a role agent and the main loop alike: change the role's definition in the roles kit, then run render_agents.py --write, which renders the role index and every agent file it names (TOOL-dBoundRoles-6).\n` }
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

/** The memory-root token a class folder of the index's `classes` map carries, as the roles kit spells it. */
const MEMORY_ROOT_TOKEN = '{{MEMORY_ROOT}}'
/** The placeholder a class folder carries for one build's segment. */
const SLUG_PLACEHOLDER = '<slug>'

/**
 * TOOL-dBoundRoles-9 S4: whether `rel`, a target's comparable repo-relative path, lies in class `cls`'s
 * folder as the index's `classes` map spells it. `{{MEMORY_ROOT}}` reads as the conf's `memRoot`,
 * normalised as checkUnarmed normalises it; `<slug>` matches exactly one non-empty segment; a trailing
 * `/` means the folder and everything under it, and a folder without one matches that path alone. A
 * class the map does not spell, or no map, matches nothing. Never asked about `product`, whose value
 * names the conf key holding its paths: step 6 places a product target through `ROUTED_PATHS`.
 */
function checkWriteClass(rel, cls, index, memRoot) {
  const folder = index && index.classes && typeof index.classes[cls] === 'string' ? index.classes[cls] : ''
  if (!folder) return false
  const mem = buildComparablePath(String(memRoot || '').trim()).replace(/^\.\//, '')
  const under = folder.endsWith('/')
  const spelled = buildComparablePath(folder.split(MEMORY_ROOT_TOKEN + '/').join(mem === '.' ? '' : mem + '/').split(MEMORY_ROOT_TOKEN).join(mem))
  const want = spelled.split('/')
  const got = String(rel).split('/')
  if (under ? got.length < want.length : got.length !== want.length) return false
  return want.every((s, i) => (s === SLUG_PLACEHOLDER ? got[i] !== '' : s === got[i]))
}

/**
 * TOOL-dBoundRoles-9 S6: whether a role declaring `writes` may write a target of class `cls` — `spec`,
 * `product`, `review` or `other`, a path in none of the three. Pure: it reads no file. A spec or
 * product target admits only its own class; a review target admits every class but `none`; any other
 * target admits every class but `none` and `review`. Steps 6a, 6b and 9a ask it, and the shell arm
 * asks the same question through it.
 */
function checkRoleClass(writes, cls) {
  if (cls === 'spec' || cls === 'product') return writes === cls
  if (cls === 'review') return writes !== 'none'
  return writes !== 'none' && writes !== 'review'
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

/** Step 6b's refusal (TOOL-dBoundRoles-9 S7): target, class, role and its `writes`, and each remedy's actor. */
function renderClassDeny(cls, index, r, w, memRoot) {
  const mem = buildComparablePath(String(memRoot || '').trim()).replace(/^\.\//, '')
  const folder = String(index.classes && index.classes.review || '').split(MEMORY_ROOT_TOKEN + '/').join(mem === '.' ? '' : mem + '/')
  const where = cls === 'review' ? `a path in the review class's folder ${folder}` : 'a path in none of the spec, product and review classes'
  const rule = r.writes === 'none' ? 'A role declaring writes = none writes nothing in this repository.'
    : `A role declaring writes = review writes only under ${folder}, the review class's folder as ${index.shown} spells it.`
  const covers = Object.keys(index.roles).filter((n) => index.roles[n].agent === true && checkRoleClass(index.roles[n].writes, cls)).sort()
  const caller = r.writes === 'review'
    ? `\n\nA review report the review harness writes under its default reviewDir lands outside that folder. The caller's remedy: pass reviewDir under ${folder} in the harness's args.`
    : ''
  return (
    `BLOCKED by scratch-guard: this ${w.tool} targets ${w.target}, ${where}, and its writer is role ${w.agentType}, whose writes is ${r.writes}. ${rule}\n\n` +
    `The driver's remedy: route this write to a role whose class covers it${covers.length ? ` (${covers.join(', ')})` : ''}, or leave it to the main loop.${caller}\n`
  )
}

/**
 * Steps 6a, 6b and 9a: the role verdict on a write of class `cls` ('spec', 'product', or step 6b's
 * 'review' or 'other'). null admits, `{ deny }` refuses. `w` carries `tool`, `ti` (the tool_input),
 * `native` (the target on disk), `target` (its comparable form), `agentType`, `slug`, `routed` (the
 * comparable spec paths the session card's `## route` names), `top` (the target's toplevel) and, for
 * step 6b, `memRoot`. An absent index admits, unless the tree is governed (checkRoleGoverned,
 * TOOL-dBoundRoles-6 S3), which refuses; a broken one refuses. Step 6b then reads the payload's role:
 * one the index does not name, or names `agent: false`, admits; a `review` role refuses, naming the
 * re-render, where the index's `classes` spells no review folder; else checkRoleClass decides. For a
 * spec or product write, no `agent`-true role with `writes = cls` refuses as UNARMED; a role in the
 * class admits. Last, and for a spec only, S4's status flip admits from the main loop on any spec and
 * from a `product` role on a routed one.
 */
function checkRoleWrite(cls, index, w) {
  const where = cls === 'other' ? 'a path in none of the spec, product and review classes' : `a ${cls} path`
  const head = `BLOCKED by scratch-guard: this ${w.tool} targets ${w.target}, ${where},`
  if (index.state === 'absent') {
    if (!checkRoleGoverned(w.top)) return null
    return { deny: `${head} and the role index ${index.shown} is absent while this tree carries rendered role agents. Every spec and product write, and every role agent's write outside them, refuses in this repository until the index is back; it is generated, so re-render it with render_agents.py --write (TOOL-dBoundRoles-6).\n` }
  }
  if (index.state === 'broken') {
    return { deny: `${head} and the role index ${index.shown} ${index.why}. Every spec and product write, and every role agent's write outside them, refuses in this repository until the index is sound; it is generated, so re-render it rather than hand-edit it.\n` }
  }
  if (cls === 'review' || cls === 'other') {
    // Step 6b (TOOL-dBoundRoles-9 S5): the `none` and `review` classes; every other role reads as at base.
    const r = Object.prototype.hasOwnProperty.call(index.roles, w.agentType) ? index.roles[w.agentType] : null
    if (!r || r.agent !== true) return null
    if (r.writes === 'review' && !(index.classes && typeof index.classes.review === 'string')) {
      return { deny: `${head} and its writer is role ${w.agentType}, whose writes is review. The role index ${index.shown} carries no classes map spelling the review class's folder, so the write cannot be placed and refuses. The index is generated: re-render it with render_agents.py --write, which adopt-roles.sh --scaffold runs in an adopting tree (TOOL-dBoundRoles-9).\n` }
    }
    return checkRoleClass(r.writes, cls) ? null : { deny: renderClassDeny(cls, index, r, w, w.memRoot) }
  }
  const writers = Object.keys(index.roles).filter((n) => index.roles[n].agent === true && checkRoleClass(index.roles[n].writes, cls)).sort()
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

// ---- the red-fix lane (TOOL-aNimbleMend-8) ------------------------------------------------------

/** The bar runner's ledger under a worktree's own git dir; the runner's `RG_GIT_DIR` holds it. */
const GATE_LEDGER_FILE = 'gate-ledger.tsv'

/**
 * The names of the legs the gate ledger under `gitDir` records red ON THIS BRANCH'S PRESENT STATE,
 * in ledger order (TOOL-aNimbleMend-14). The runner carries forward every row a run did not
 * measure, so a row is bounded by its own head field, never by its status alone. A row is open
 * when all four hold, tested in this order:
 *  - form: nine or more tab-separated fields, the third `fail` or `timeout`. A legacy five-field
 *    row, a short row and an `ok` or `retried` row are not open.
 *  - head shape: the ninth field is a full hex sha.
 *  - manifest: the first field is the `name` of a row of the JSON list the conf key `LEG_MANIFEST`
 *    of `<top>/.memory-tree.conf` names, read from the working tree. A blank or absent key reads
 *    as the commit grader reads it (TOOL-aNimbleMend-15 S7): `gate-legs.json` beside the run-gates
 *    kit `resolveKitDir` finds from this hook's own directory, and only where that file sits
 *    inside `top`. No `chunk`, `subject` or `pass_leg` is tested, so a held leg stays eligible.
 *  - head place: the ninth field is `HEAD` of `top`, or a commit `git rev-list HEAD --not <landed>`
 *    prints there, `<landed>` being the policy helper's `readLandedRevision(top)`. The landed read
 *    and the `rev-list` run only where a candidate's head differs from `HEAD`.
 * Every failure closes the lane and none throws: an empty `gitDir` or `top`, an absent or unreadable
 * ledger, a blank or absent key with no run-gates kit resolved or its manifest outside `top`, a
 * manifest that is unreadable, unparsable or no list, and an
 * unreadable `HEAD` each answer the empty list; no policy helper, a refused landed read and a failed
 * `rev-list` leave only the rows at `HEAD` open.
 */
function readOpenReds(gitDir, top) {
  if (!gitDir || !top) return []
  const fs = require('fs')
  const path = require('path')
  let text
  try { text = fs.readFileSync(path.join(gitDir, GATE_LEDGER_FILE), 'utf8') } catch { return [] }
  let rows = []
  for (const l of text.split('\n')) {
    // Split on the tab and count: the row's empty fields are kept, so the head stays the ninth.
    const f = l.replace(/\r$/, '').split('\t')
    if (f.length >= 9 && (f[2] === 'fail' || f[2] === 'timeout') && /^[0-9a-f]{40,64}$/.test(f[8])) rows.push({ name: f[0], head: f[8] })
  }
  if (rows.length === 0) return []
  let legs
  try {
    const rel = (readConfKey(fs.readFileSync(path.join(top, ROUTE_CONF), 'utf8'), 'LEG_MANIFEST') || '').trim()
    let file = rel ? path.join(top, buildNativePath(rel)) : ''
    if (!rel) {
      // A BLANK KEY (TOOL-aNimbleMend-15 S7), read as the commit grader's `resolve_leg_manifest` reads
      // it: `gate-legs.json` beside the run-gates kit this install holds, and only inside `top`. The
      // resolver throws where no such kit resolves, which the catch below answers.
      file = path.join(path.dirname(resolveKitDir('run-gates', 'run-gates.sh', __dirname)), 'gate-legs.json')
      const real = buildComparablePath(resolveRealPath(file))
      const root = buildComparablePath(resolveRealPath(top))
      if (!real || !root || real === root || !checkUnderRoot(real, root)) return []
    }
    const doc = JSON.parse(fs.readFileSync(file, 'utf8'))
    if (!Array.isArray(doc)) return []
    legs = new Set(doc.map((r) => (r && typeof r === 'object' ? r.name : null)).filter((n) => typeof n === 'string'))
  } catch { return [] }
  rows = rows.filter((r) => legs.has(r.name))
  if (rows.length === 0) return []
  const { spawnSync } = require('child_process')
  const runGit = (args) => {
    try { return spawnSync('git', args, { cwd: top, encoding: 'utf8', timeout: 20000, windowsHide: true }) } catch { return { status: 1, stdout: '' } }
  }
  const h = runGit(['rev-parse', '--verify', '-q', 'HEAD'])
  const head = h.status === 0 ? String(h.stdout || '').trim() : ''
  if (!head) return []
  const unlanded = new Set()
  if (rows.some((r) => r.head !== head)) {
    try {
      const helper = resolvePolicyHelper()
      const landed = helper && fs.existsSync(helper) ? require(helper).readLandedRevision(top) : ''
      if (/^[0-9a-f]{40,64}$/.test(landed)) {
        const r = runGit(['rev-list', 'HEAD', '--not', landed])
        if (r.status === 0) for (const sha of String(r.stdout || '').split(/\r?\n/)) if (sha) unlanded.add(sha)
      }
    } catch { unlanded.clear() }
  }
  return rows.filter((r) => r.head === head || unlanded.has(r.head)).map((r) => r.name)
}

/**
 * S2: the lane's one decision, first match wins. `w` carries `agentType`, `index` as loadRoleIndex
 * returns it, `governed` as checkRoleGoverned answers for an absent index, `lane` as `{ on, why }`
 * and `reds` as readOpenReds returns them. `{ witness }` admits, null leaves the refusal standing.
 *  1. `lane.on` is not true → null
 *  2. `reds` is empty → null
 *  3. the index is broken, or absent in a governed tree (TOOL-dBoundRoles-6 S3) → null
 *  4. `agentType` is empty, the main loop → witness
 *  5. the index is absent, in a tree that is not governed → witness
 *  6. `agentType` names an `agent`-true role declaring `writes = product` → witness
 *  7. anything else, the untyped harness agent included → null
 * It does not ask whether the write fixes the red: any product path is admitted while a leg is open.
 * The caller asks it TWICE (TOOL-aNimbleMend-15): first with `lane.on` taken as true, over the reds
 * and the index alone, so steps 2 to 7 decide before the key is read; then, only where that
 * admitted, with the lane as the key answered it, where step 1 decides.
 */
function checkRedLane(w) {
  if (!w.lane || w.lane.on !== true) return null
  if (!Array.isArray(w.reds) || w.reds.length === 0) return null
  if (!w.index || w.index.state === 'broken' || (w.index.state === 'absent' && w.governed === true)) return null
  const r = w.index.state === 'ok' && w.agentType && Object.prototype.hasOwnProperty.call(w.index.roles, w.agentType) ? w.index.roles[w.agentType] : null
  if (w.agentType && w.index.state !== 'absent' && !(r && r.agent === true && r.writes === 'product')) return null
  return { witness: `red-fix lane admits this write — open red leg(s): ${w.reds.join(', ')}; its commit owes a \`Red-fix: <leg>\` trailer beside \`Pass: none\`${w.lane.why ? ` · ${w.lane.why}` : ''}` }
}

/**
 * The policy file's arm (TOOL-dDeclaredLoop-2 S10): a deny when `target` is the policy file of the
 * repository at `top`, the path the policy kit's policy-mirror.js exports as POLICY_REL, found through
 * this file's resolvePolicyHelper; null otherwise, and null with no policy kit beside the hook. A
 * target that is no `.toml` file reads nothing. The policy file has one door, the loop kit's
 * policy_edit.py, which checks the value, writes the change record and stages both; the pre-commit
 * guard judges the commit.
 */
function checkPolicyFile(tool, target, top) {
  const fs = require('fs')
  const path = require('path')
  if (path.extname(target).toLowerCase() !== '.toml') return null
  const helper = resolvePolicyHelper()
  if (!helper || !fs.existsSync(helper)) return null
  const rel = require(helper).POLICY_REL
  if (typeof rel !== 'string' || buildComparablePath(target) !== buildComparablePath(path.join(top, buildNativePath(rel)))) return null
  return { deny: `BLOCKED by scratch-guard: this ${tool} targets the policy file ${rel}, which no tool write changes. Its door is the loop kit's policy_edit.py: \`set <key> <value>\` on a live run's branch or at the owner's terminal, \`raise <cap> <new>\` for one measured-file cap, \`propose <key> <value>\` to print the change; each writes the change record and stages it beside the file (TOOL-dDeclaredLoop-2).\n` }
}

/**
 * The target's REAL place (TOOL-aRoutedQuill-12 S4): <native> resolved against <cwd> where it is
 * relative, then the realpath of its deepest existing ancestor with the not-yet-existing tail
 * appended, so a product file reached through a junction or a symlink is placed, and gated, like its
 * repository spelling. checkRouted and checkShellWrites place a target through it alike.
 */
function resolveTargetPlace(native, cwd) {
  const fs = require('fs')
  const path = require('path')
  let target = cwd ? path.resolve(buildNativePath(cwd), native) : path.resolve(native)
  for (let head = target, tail = ''; ;) {
    if (fs.existsSync(head)) { target = path.join(resolveRealPath(head) || head, tail); break }
    const up = path.dirname(head)
    if (up === head) break
    tail = tail ? path.join(path.basename(head), tail) : path.basename(head)
    head = up
  }
  return target
}

/**
 * TOOL-dBoundRoles-7 S5: the first of <entries>, a list in the `ROUTED_PATHS` grammar, that covers
 * <rel>, a comparable repo-relative path, or undefined. An entry ending in a slash covers the folder
 * and everything under it, by whole segment; any other entry covers that exact path; a leading `./`
 * is dropped. checkRouted's product class and the work order's allowance read this one matcher.
 */
function checkRoutedEntry(rel, entries) {
  return entries.find((e) => {
    const c = buildComparablePath(e).replace(/^\.\//, '')
    return /[\\/]$/.test(e) ? checkUnderRoot(rel, c) : rel === c
  })
}

/**
 * THE ONE EVALUATION ORDER of the write gate. Returns null to print nothing, `{ witness }` to allow
 * with one stderr line, `{ deny }` to refuse.
 *  1. `tool_name` outside WRITE_TOOLS → null
 *  2. no non-empty `file_path` / `notebook_path`, or a relative one with no payload `cwd` → deny
 *  3. session repository = common dir of `CLAUDE_PROJECT_DIR`, else of `cwd`; no `.git` above the
 *     target, no session repository, or a target common dir that differs → null
 * 3a. the policy file of that repository, with a policy kit beside the hook (checkPolicyFile) → deny
 *     naming policy_edit.py, before the conf is read, so an unarmed or absent conf does not open it
 *  4. `<target toplevel>/.memory-tree.conf` absent → witness; present and unreadable → deny
 *  5. UNARMED (checkUnarmed) → null when the target is the conf, else deny
 * 5a. the role index `.claude/roles.json`, or the agent file `.claude/agents/<name>.md` of a role that
 *     index names (checkRenderedRole, TOOL-dBoundRoles-6 S1) → deny naming render_agents.py --write,
 *     for every writer; an adopter's own agent file, named by no index row, goes on to step 6
 *  6. the target's CLASS: product when it falls under a ROUTED_PATHS entry; spec when its path
 *     opens `<MEMORY_ROOT>/builds/<one segment>/spec/`; else neither → step 6b.
 * 6b. neither (TOOL-dBoundRoles-9 S5): no `agent_type` → null, the main loop reading no index; else
 *     checkRoleWrite over loadRoleIndex(top), the class `review` where checkWriteClass places the
 *     target in the index's `classes.review` folder, else `other`: absent → null, or deny where the
 *     tree is governed; broken → deny; a type the index does not name, or names `agent: false` →
 *     null; a `review` role and no `classes.review` → deny naming the re-render; else
 *     checkRoleClass(role.writes, class): `none` refuses everywhere, `review` admits its folder
 *     alone, `spec`, `product` and `records` admit as at base
 * 6a. spec → checkRoleWrite('spec') over loadRoleIndex(top): absent → null, or deny where the tree
 *     is governed (checkRoleGoverned, TOOL-dBoundRoles-6 S3); broken → deny; no
 *     `agent`-true role with `writes = spec` → deny, UNARMED; the payload's `agent_type` names such a
 *     role → null; a status-and-date-only flip (checkStatusOnlyEdit) from the main loop, or from a
 *     `product` role on a spec its card's `## route` names → null; else deny
 *  7. product, and `session_id` missing or no card for it under the common dir → deny, absent
 *  8. no `## route`, or no `- unit:` line in it → deny, unrouted
 *  9. a routed unit BUILDABLE (checkBuildable) → step 9a; else step 9b
 * 9b. the dispatch fallback (TOOL-aSmoothedDispatch-6): readDispatchedUnits reads the dispatch rows of
 *     RUN_STATE_FILE in the folder of the build the route's `- build:` line names; each unit those
 *     rows name that the card does not route is judged by checkBuildable against the spec under that
 *     build's `spec/` whose H1 names it, and the first buildable one → step 9a. None → deny listing
 *     each card unit's reason, plus one line naming the run-state file and its dispatched-unit count
 *     when it records any. It does not ask whether the pass committed: a pass's spec goes terminal in
 *     its own pass commit, so a pass committed with its spec left INPROGRESS keeps admitting; and a
 *     hand-appended row is read like the driver's.
 * 9a. checkRoleWrite('product'): absent → null, or deny in a governed tree; broken → deny; no `agent`-true role with
 *     `writes = product` → deny, UNARMED; the payload's `agent_type` names such a role → null; else
 *     deny. The route arm runs first and never instead: a builder with no buildable route meets
 *     step 7, 8 or 9b's refusal word for word.
 * 10. the red-fix lane (TOOL-aNimbleMend-8), on a product-class refusal from step 7, 8, 9b or 9a
 *     and on nothing else: read the gate ledger's open reds (readOpenReds over the worktree's git
 *     dir and toplevel: a row counts only at `HEAD` or at an unlanded ancestor of it, for a leg of
 *     `LEG_MANIFEST`, TOOL-aNimbleMend-14) and the role index FIRST. With no red open, a broken
 *     index or an absent one in a governed tree (TOOL-dBoundRoles-6 S3), or a writer checkRedLane's
 *     steps 4 to 6 would not admit, the refusal stands as
 *     composed and the lane key is not read (TOOL-aNimbleMend-15). Only then read the lane key
 *     `bar.inline-red-fixes`, and return checkRedLane's witness, or the refusal as composed. A key
 *     read that refused or answered another value appends its one line to the refusal, and only
 *     where a red is open and the writer is admissible; under `off` the refusal is byte for byte
 *     the one composed. An admitted write and every non-product write read neither.
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
  const target = resolveTargetPlace(native, cwd)
  const sessionStart = env.CLAUDE_PROJECT_DIR || cwd
  if (!sessionStart) return null
  const session = resolveComparableCommon(path.resolve(buildNativePath(sessionStart)))
  const mine = resolveComparableCommon(target)
  if (!session.key || !mine.key || session.key !== mine.key) return null
  const top = mine.hit.toplevel
  const policyFile = checkPolicyFile(tool, target, top)
  if (policyFile) return policyFile
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
  const rendered = checkRenderedRole(tool, targetC, rel, top)
  if (rendered) return rendered
  const entry = checkRoutedEntry(rel, routed.trim().split(/\s+/))
  const sid = data.session_id ? String(data.session_id) : ''
  const agentType = typeof data.agent_type === 'string' ? data.agent_type : ''
  if (entry === undefined) {
    // Step 6: the spec class, on the comparable form, MEMORY_ROOT normalized as checkUnarmed does it.
    const mem = buildComparablePath(memRoot.trim()).replace(/^\.\//, '')
    const pre = (mem === '.' ? '' : mem + '/') + 'builds/'
    if (!rel.startsWith(pre) || !/^[^/]+\/spec\/./.test(rel.slice(pre.length))) {
      // Step 6b (TOOL-dBoundRoles-9 S5): neither product nor spec. The main loop reads no index.
      if (!agentType) return null
      const index = loadRoleIndex(top)
      const cls = index.state === 'ok' && checkWriteClass(rel, 'review', index, memRoot) ? 'review' : 'other'
      return checkRoleWrite(cls, index, { tool, ti, native: target, target: targetC, agentType, slug: '', routed: [], top, memRoot })
    }
    // The slug keeps its case: the same segment of the target's own spelling.
    const slug = path.relative(top, target).replace(/\\/g, '/').split('/')[pre.split('/').length - 1] || ''
    const cardText = sid ? readCard(mine.common, sid).text : null
    const routed = extractRouteUnits(cardText).units.filter((u) => u.spec).map((u) => buildComparablePath(path.join(top, buildNativePath(u.spec))))
    return checkRoleWrite('spec', loadRoleIndex(top), { tool, ti, native: target, target: targetC, agentType, slug, routed, top })
  }
  // Step 10: the red-fix lane, asked with a product-class verdict already composed. An admit passes
  // through untouched, so the key and the ledger are read on a refusal only.
  const checkLane = (verdict) => {
    if (!verdict || !verdict.deny) return verdict
    // THE CHEAP TESTS FIRST (TOOL-aNimbleMend-15 S14). The ledger and the role index are files; the
    // key is a policy read that spawns git. So checkRedLane is asked once with the lane taken as
    // on: with no red open, a broken index or a writer its steps 4 to 6 would not admit, the
    // refusal stands as composed and the key is never read, which is every refusal of a tree with
    // no open red. A refused key read there appends no line.
    // The worktree's OWN git dir, where the runner wrote, never the common dir.
    let gitDir = mine.hit.gitPath
    if (mine.hit.isFile) {
      let m = null
      try { m = /gitdir:\s*(.+)/.exec(fs.readFileSync(mine.hit.gitPath, 'utf8')) } catch { m = null }
      gitDir = m ? path.resolve(top, m[1].trim()) : ''
    }
    const reds = readOpenReds(gitDir, top)
    const index = loadRoleIndex(top)
    const governed = index.state === 'absent' && checkRoleGoverned(top)
    if (!checkRedLane({ agentType, index, governed, lane: { on: true, why: '' }, reds })) return verdict
    let lane
    try {
      const helper = resolvePolicyHelper()
      if (!helper || !fs.existsSync(helper)) {
        lane = { on: true, why: 'NOTE — no policy kit resolves beside this hook, so bar.inline-red-fixes reads on' }
      } else {
        const v = require(helper).readPolicy('bar.inline-red-fixes', { repo: top }).value
        lane = v === 'on' ? { on: true, why: '' } : v === 'off' ? { on: false, why: '' }
          : { on: false, why: `bar.inline-red-fixes reads ${JSON.stringify(v)}, neither on nor off, so the red-fix lane is closed` }
      }
    } catch (e) {
      lane = { on: false, why: String((e && e.message) || e).split(/\r?\n/)[0] }
    }
    const admit = checkRedLane({ agentType, index, governed, lane, reds })
    if (admit) return admit
    return !lane.on && lane.why ? { deny: `${verdict.deny}${lane.why}\n` } : verdict
  }
  const card = sid ? readCard(mine.common, sid) : null
  if (!card || card.text === null) {
    const where = card ? `this session has no orientation card at ${card.shown} (session ${sid})` : 'the payload carries no session_id, so no orientation card can be read'
    return checkLane({ deny: renderRouteDeny(tool, targetC, entry, confShown, where, `Create the card with manifest-check.sh --card --write --session ${sid || '<session id>'} from the kickoff kit, then run /session-kickoff, which specs the unit, writes its brief and appends a ## route naming it.`) })
  }
  const route = extractRouteUnits(card.text)
  if (!route.seen || route.units.length === 0) {
    const what = route.seen ? `its ## route at ${card.shown} carries no - unit: line` : `its orientation card ${card.shown} carries no ## route`
    return checkLane({ deny: renderRouteDeny(tool, targetC, entry, confShown, what, `Run /session-kickoff: give the unit its spec, then append a ## route naming it through manifest-check.sh --card --append --session ${sid}.`) })
  }
  // Step 9a: the route admits; the writer's role decides. The slug is the unit id's middle.
  const checkUnitWrite = (u) => {
    const slug = (/^[A-Za-z]+-(.+)-\d+$/.exec(u.unit) || [])[1] || route.build
    return checkRoleWrite('product', loadRoleIndex(top), { tool, ti, native: target, target: targetC, agentType, slug, routed: [], top })
  }
  const reasons = []
  for (const u of route.units) {
    const why = checkBuildable(u, route.build, top, memRoot.trim(), confBytes)
    if (!why) return checkLane(checkUnitWrite(u))
    reasons.push(`  ${u.unit}: ${why}`)
  }
  // Step 9b: the units the build's run-state file records as dispatched, minus the card's own.
  const dispatched = readDispatchedUnits(top, memRoot.trim(), route.build)
  const onCard = new Set(route.units.map((u) => u.unit))
  for (const u of dispatched.units) {
    if (!onCard.has(u.unit) && !checkBuildable(u, route.build, top, memRoot.trim(), confBytes)) return checkLane(checkUnitWrite(u))
  }
  if (dispatched.units.length > 0) reasons.push(`  the run-state file ${dispatched.file} records a dispatch for ${dispatched.units.length} unit(s) of ${route.build}, and none is buildable`)
  return checkLane({ deny: renderRouteDeny(tool, targetC, entry, confShown, `no unit its card ${card.shown} routes is buildable:\n${reasons.join('\n')}`, 'Make one routed unit buildable — its spec at the status that admits writes — or route the unit that owns this write through /session-kickoff and manifest-check.sh --card --append.') })
}

// ---- the shell-write arm (TOOL-dBoundRoles-7) ---------------------------------------------------

/**
 * The shape an agent id and a Workflow run id must hold to reach a path, the Claude Code session directory's
 * folder of Workflow runs, and that directory's derivation (TOOL-dBoundRoles-43 S57): ONE home each, which
 * format-guard.js imports and readWorkOrderAllowance reads, so the layout is typed once.
 */
const RUN_ID_RE = /^[A-Za-z0-9_-]{1,64}$/
const WORKFLOW_RUNS_DIR = 'workflows'
/** The session directory beside a session transcript: its path, native form, without the `.jsonl` suffix. */
function resolveSessionDir(transcriptPath) {
  return buildNativePath(String(transcriptPath).replace(/\.jsonl$/i, ''))
}
/** The bound on the agent transcript's first record the allowance read takes, in bytes (TOOL-dBoundRoles-43 S39). */
const TRANSCRIPT_READ_BOUND = 8 * 1024 * 1024

/**
 * S4: the allowance of the work order a role agent was spawned with, read from its transcript, where
 * spawn-guard.js's rule 6 verified the prompt against its prompt file byte for byte. The transcript is
 * `<session dir>/subagents/agent-<agent_id>.jsonl`, else `<session dir>/subagents/workflows/<run id>/
 * agent-<agent_id>.jsonl` for the first run id in name order holding one, the session dir being
 * resolveSessionDir's; `agent_id` and each run id reach a path only in RUN_ID_RE's shape. Its first JSONL
 * line is read whole, up to TRANSCRIPT_READ_BOUND bytes, and must parse as a `user` record, whose content is
 * the prompt (TOOL-dBoundRoles-43 S39). The allowance is the one `### allowance` heading of the prompt's
 * `## Task` section, both read outside every fence by readUnfencedLines, so a heading quoted in a handed
 * block's fence is content (S35): its block runs up to the next heading, each `- <prefix>` bullet one entry,
 * a backtick pair around it stripped, and a body reading `none` the empty list.
 * `{ entries, from, marker }` when found, `from` the transcript and `marker` the prompt's first line
 * where it is the `gov:handoff` marker; `{ deny }` for a typed agent's work order that cannot be trusted to
 * narrow, rather than fall back to the class verdict: a first record past the bound or one that does not
 * parse (S39), and two or more `### allowance` headings outside every fence, naming the count (S35);
 * `{ why }` when no transcript, no user first record, no `## Task` section or no block is found. Reads no
 * other file and never throws on a missing one.
 */
function readWorkOrderAllowance(data) {
  const fs = require('fs')
  const path = require('path')
  const tp = typeof data.transcript_path === 'string' ? data.transcript_path : ''
  if (!tp.endsWith('.jsonl')) return { why: 'the payload carries no transcript_path naming a .jsonl file' }
  const aid = typeof data.agent_id === 'string' ? data.agent_id : ''
  if (!RUN_ID_RE.test(aid)) return { why: `the payload's agent_id ${JSON.stringify(aid.slice(0, 80))} is not in the shape ${RUN_ID_RE}` }
  const sub = path.join(resolveSessionDir(tp), 'subagents')
  const name = `agent-${aid}.jsonl`
  let runs = []
  try { runs = fs.readdirSync(path.join(sub, WORKFLOW_RUNS_DIR)).filter((r) => RUN_ID_RE.test(r)).sort() } catch { runs = [] }
  const file = [path.join(sub, name), ...runs.map((r) => path.join(sub, WORKFLOW_RUNS_DIR, r, name))].find((f) => fs.existsSync(f))
  if (!file) return { why: `no agent transcript ${name} under ${buildComparablePath(sub)}` }
  const from = buildComparablePath(file)
  const parts = []
  let fd = null
  let read = 0
  let whole = false
  try {
    fd = fs.openSync(file, 'r')
    const chunk = Buffer.alloc(1024 * 1024)
    while (read <= TRANSCRIPT_READ_BOUND) {
      const n = fs.readSync(fd, chunk, 0, chunk.length, read)
      if (n === 0) { whole = true; break }
      const nl = chunk.subarray(0, n).indexOf(0x0a)
      parts.push(Buffer.from(chunk.subarray(0, nl === -1 ? n : nl)))
      read += nl === -1 ? n : nl
      if (nl !== -1) { whole = true; break }
    }
  } catch (e) {
    return { why: `the agent transcript ${from} cannot be read (${(e && e.code) || e})` }
  } finally {
    if (fd !== null) fs.closeSync(fd)
  }
  if (!whole || read > TRANSCRIPT_READ_BOUND) return { deny: `the first record of the agent transcript ${from} runs past ${TRANSCRIPT_READ_BOUND} bytes, so the work order's allowance is not read and no write of this typed agent is admitted on its class verdict alone` }
  let d
  try { d = JSON.parse(Buffer.concat(parts).toString('utf8')) } catch { d = undefined }
  if (d === undefined) return { deny: `the first record of the agent transcript ${from} does not parse, so the work order's allowance is not read and no write of this typed agent is admitted on its class verdict alone` }
  if (!d || d.type !== 'user') return { why: `the first record of the agent transcript ${from} is no user record` }
  const c = d.message && d.message.content
  const prompt = typeof c === 'string' ? c
    : Array.isArray(c) ? c.filter((b) => b && b.type === 'text' && typeof b.text === 'string').map((b) => b.text).join('\n') : ''
  const walked = [...readUnfencedLines(prompt)]
  // TOOL-dBoundRoles-50 S17: a prompt the walk ends inside a fence holds no allowance anyone can read
  const open = walked.find(([, l]) => l === null)
  if (open) return { deny: `a fence opened at line ${open[0]} of the prompt in ${from} is never closed, so its allowance block cannot be read outside a fence and no write of this typed agent is admitted` }
  const lines = walked.map(([n, l]) => [n, l.replace(/\r$/, '')])
  const task = lines.findIndex(([, l]) => l === '## Task')
  if (task === -1) return { why: `the prompt in ${from} holds no ## Task section outside a fence` }
  const end = lines.findIndex(([, l], i) => i > task && /^## /.test(l))
  const heads = lines.map(([, l], i) => i).filter((i) => i > task && (end === -1 || i < end) && lines[i][1].trim() === '### allowance')
  if (heads.length === 0) return { why: `the ## Task section of the prompt in ${from} carries no ### allowance block` }
  if (heads.length > 1) return { deny: `the ## Task section of the prompt in ${from} carries ${heads.length} ### allowance headings outside every fence, and a work order holds one, so no write of this typed agent is admitted` }
  const entries = []
  for (const [, raw] of lines.slice(heads[0] + 1)) {
    const l = raw.trim()
    if (/^#{1,6}\s/.test(l)) break
    const b = /^- (.+)$/.exec(l)
    if (b) entries.push(b[1].trim().replace(/^`(.*)`$/, '$1'))
  }
  const first = prompt.split(/\r?\n/)[0]
  return { entries, from, marker: first.startsWith('<!-- gov:handoff') ? first.trim() : '' }
}

/** S7: a shell-write refusal — the command's target, the shape that wrote it, why, and the remedy's actor. */
function renderShellDeny(tool, t, shown, reason) {
  return (
    `BLOCKED by scratch-guard: this ${tool} command writes ${shown} through ${t.why} (\`${t.value}\`), and a role ` +
    `agent's shell write is held to what an Edit or Write of the same target meets. ${reason}\n\n` +
    'The remedy is the driver\'s: re-scope the work order, or route the write to a role whose class and ' +
    'allowance cover it (TOOL-dBoundRoles-7).\n'
  )
}

/**
 * THE ONE EVALUATION ORDER of the shell-write arm (TOOL-dBoundRoles-7). Returns null to admit,
 * `{ witness }` to admit with one stderr line, `{ deny }` to refuse.
 *  1. `agent_type` absent or empty → null (the main loop meets checkCommand and checkOriented alone)
 *  2. scanWriteTargets(cmd, cwd, tool_name) finds no target but a temp-root assignment → null, with no
 *     file read
 *  3. each target, with `~` and `$HOME` expanded; one still holding `$` or a backtick (a computed
 *     path, §8 F4), a relative one with no payload `cwd`, and a device name (`nul`, `con`, `/dev/…`)
 *     are not placed; the rest placed by resolveTargetPlace against the payload `cwd`:
 *     a. in no repository, or one whose common dir is not the session's (`CLAUDE_PROJECT_DIR`, else
 *        `cwd`) → skipped: checkCommand's rules own it
 *     b. checkRouted on a synthetic `Write` payload carrying the target as `tool_input.file_path` and
 *        the payload's `cwd`, `session_id` and `agent_type`: a deny → deny, renderShellDeny around
 *        it; a witness is kept
 *     c. readWorkOrderAllowance(data), read once per call: its `deny` (a first record past the bound or
 *        not parsing, two allowance headings outside every fence) → deny naming it (TOOL-dBoundRoles-43
 *        S35, S39); found, and checkRoutedEntry places the target's repo-relative path under none of
 *        its entries → deny naming the allowance and the work order; an empty list admits no target
 *  4. the witnesses step 3b kept, and, where step 3c read no allowance, one naming why, joined on one
 *     line → witness; else null
 * The synthetic payload carries no `content`, so no status-only flip is proven and a shell edit of a
 * spec by a role outside the spec class refuses; the admitted flip stays the `Edit` route.
 */
function checkShellWrites(cmd, data, env) {
  const path = require('path')
  const type = typeof data.agent_type === 'string' ? data.agent_type : ''
  if (!type) return null
  const cwd = typeof data.cwd === 'string' ? data.cwd : ''
  const tool = typeof data.tool_name === 'string' ? data.tool_name : 'Bash'
  const targets = scanWriteTargets(cmd, cwd, tool).filter((t) => t.why !== 'temp-root assignment')
  if (targets.length === 0) return null
  const sessionStart = env.CLAUDE_PROJECT_DIR || cwd
  if (!sessionStart) return null
  const session = resolveComparableCommon(path.resolve(buildNativePath(sessionStart)))
  if (!session.key) return null
  const home = env.HOME || env.USERPROFILE || ''
  const witnesses = []
  let allowance = null
  for (const t of targets) {
    let v = String(t.value)
    if (home) v = v.replace(/^(?:~|\$\{HOME\}|\$HOME)(?=\/|\\|$)/, () => home)
    if (/[$`]/.test(v) || v.startsWith('~') || /^(?:nul|con|\/dev\/.+)$/i.test(v)) continue
    const native = buildNativePath(v)
    if (!path.isAbsolute(native) && !cwd) continue
    const target = resolveTargetPlace(native, cwd)
    const mine = resolveComparableCommon(target)
    if (!mine.key || mine.key !== session.key) continue
    const shown = buildComparablePath(target)
    const verdict = checkRouted({ tool_name: 'Write', tool_input: { file_path: target }, cwd, session_id: data.session_id, agent_type: type }, env)
    if (verdict && verdict.deny) return { deny: renderShellDeny(tool, t, shown, `The write gate refuses that Write:\n\n${verdict.deny.trimEnd()}`) }
    if (verdict && verdict.witness && !witnesses.includes(verdict.witness)) witnesses.push(verdict.witness)
    if (allowance === null) allowance = readWorkOrderAllowance(data)
    if (allowance.deny) return { deny: renderShellDeny(tool, t, shown, `The work order's allowance is not read: ${allowance.deny}.`) }
    if (!allowance.entries) continue
    const rel = shown.slice(buildComparablePath(mine.hit.toplevel).length + 1)
    if (checkRoutedEntry(rel, allowance.entries) === undefined) {
      const listed = allowance.entries.length ? allowance.entries.join(', ') : 'none, which admits no repository write'
      const order = `the work order role ${type} was spawned with, the first record of ${allowance.from}${allowance.marker ? `, which opens ${allowance.marker}` : ''}`
      return { deny: renderShellDeny(tool, t, shown, `Its path ${rel} lies outside the allowance of ${order}: ${listed}.`) }
    }
  }
  if (allowance && !allowance.entries) witnesses.push(`allowance not located — ${allowance.why}, so a role agent's shell write is held to its class verdict alone`)
  return witnesses.length ? { witness: witnesses.join(' · ') } : null
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
 * tested before its `c` cluster, because `bash -nc '<x>'` only checks the syntax of `<x>`. A
 * `clusterTakes` letter (TOOL-aTrimmedWait-6) takes one following word for each time it appears in a
 * single-dash or plus cluster, so `-eo pipefail` and `-euxo pipefail` step past `pipefail`, and a
 * `body` cluster scans the word after those arguments.
 */
const GATE_OPTION_RULES = {
  shell: { plus: true, takes: ['--rcfile', '--init-file'], clusterTakes: /[oO]/g, ends: /^-[A-Za-z]*n[A-Za-z]*$/, body: /^-[A-Za-z]*c[A-Za-z]*$/ },
  python: { takes: ['-W', '-X', '-Q'], ends: /^-[A-Za-z]*[cm]$/ },
  node: { takes: ['-r', '--require', '--import'], ends: /^(?:-e|--eval|-p|--print)$/ },
  env: { takes: ['-u', '--unset', '-C', '--chdir'], body: /^(?:-S|--split-string)$/ },
  nice: { takes: ['-n', '--adjustment'] },
  exec: { takes: ['-a'] },
  command: { takes: [], ends: /^-[vV]$/ },
}
/**
 * G2, by basename and in any form: the bar runner, the self-test runner, the unattended gates
 * runner, and the pass-leg runner `pass-legs.sh` (TOOL-aNimbleMend-6), which is the main loop's.
 */
const GATE_RUNNERS = ['run-gates.sh', 'run-selftests.sh', 'run-unattended-gates.sh', 'pass-legs.sh']
/** G3's admitting words: a render, a listing or a usage text runs no arm. */
const GATE_SUITE_ADMITS = ['--render', '--list', '--help']
/**
 * The words the polling rows' scan (TOOL-aTrimmedWait-6) and the shell-write scan (TOOL-dBoundRoles-87)
 * step before a head; the gate rows step none. A new word here owes its spelling in the suite.
 */
const SHELL_RESERVED_WORDS = ['!', '{', 'do', 'then', 'else', 'elif', 'if', 'while', 'until', 'coproc', 'function']
/** The compound openers before which Bash reads the word after `coproc` as its name (TOOL-dBoundRoles-87). */
const NAMED_COPROC = ['{', 'if', 'while', 'until']
/** P3's floor in seconds: a flat `sleep` this long or longer is a poll. */
const POLL_SLEEP_FLOOR_S = 5

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
 * the index of the next non-option word, or a negative number when the simple command ends: -2 - <j>
 * where the `ends` option at index <j> ended it (TOOL-dBoundRoles-7 S1), else -1. A cluster takes one
 * word per `clusterTakes` letter it carries. A body option scans the word after those ONCE through
 * scanCommandHeads into <out>, with <opts> but their `tool`, a shell's body being shell text whatever
 * tool ran it, at depth 0 only, then ends it. A `--` is stepped past and ends the options.
 */
function scanLauncherOptions(a, k, rule, depth, out, opts) {
  const r = rule || {}
  for (; k < a.length; k++) {
    const w = a[k]
    if (w === '--') return k + 1
    if (!w.startsWith('-') && !(r.plus && w.startsWith('+'))) return k
    if (r.takes && r.takes.includes(w)) { k++; continue }
    if (r.ends && r.ends.test(w)) return -2 - k
    const j = r.clusterTakes && /^[-+][A-Za-z]+$/.test(w) ? (w.match(r.clusterTakes) || []).length : 0
    if (r.body && r.body.test(w)) {
      if (depth === 0 && a[k + 1 + j] !== undefined) out.push(...scanCommandHeads(a[k + 1 + j], depth + 1, { ...opts, tool: undefined }))
      return -1
    }
    k += j
  }
  return k
}

/**
 * The simple commands of <cmd> and their heads. A simple command is a segment of the blanked view
 * between `;`, `|`, `&`, `(`, `)` and a newline, its words read from the original text by readWordText,
 * their quotes dropped. scanRedirects first takes every redirect operator and its word out of the view,
 * wherever they stand, so none splits a command or is a word (TOOL-dBoundRoles-86), and a line
 * continuation is blanked: a backslash before a newline, or a backtick in PowerShell, `opts.tool` naming
 * the tool and Bash being read without one; a PowerShell `<# #>` comment is blanked too. The HEAD is the
 * first word after any `NAME=value`, any prefix word with its options, and `timeout` with its options and duration, then past a
 * launcher and its options, each stepped by GATE_OPTION_RULES through scanLauncherOptions: a shell's
 * `-c` scans its body ONCE as a command of its own, a shell's `-n` executes nothing, and a Python
 * `-c` or `-m` names no script — each ends the segment. With `opts.reserved` (the polling rows,
 * TOOL-aTrimmedWait-6, and the shell-write scan, TOOL-dBoundRoles-87) the prefix loop also steps a word
 * of SHELL_RESERVED_WORDS; `function` takes the word after it, its name, and so does `coproc` where the
 * word after that is in NAMED_COPROC and the first is no word of the list.
 * Returns `[{ text, head, argv, launched, reserved }]`, argv being the head and every word after it,
 * reserved the reserved words stepped. A `#` beginning a word, outside quotes and heredoc bodies,
 * blanks the rest of its line first, as the shell drops a comment (TOOL-aTrimmedWait-9).
 * With `opts.inline` (TOOL-dBoundRoles-7 S1, the shell-write scan alone) every entry also carries
 * `here`, the body of the heredoc its segment opens, or undefined; and a Python launcher ended by a
 * `-c` cluster, or a Node one by `-e`, `--eval`, `-p` or `--print`, yields an entry whose `inline` is
 * the word after it, as does a Python or Node launcher left with no script word, or a Python one
 * whose script is `-`, its `inline` being `here`, the program it reads from standard input. In that mode
 * too (TOOL-dBoundRoles-86) each output redirect is an entry of its own, `{ redirect }`, the word as
 * scanRedirects read it; each unquoted `$( )`, `<( )` and `>( )` of scanSubstitutions is scanned as a
 * command of its own at the same depth and stands in the outer command as one word; and an ordinary
 * entry carries `raw`, its argv words with their quotes kept.
 */
function scanCommandHeads(cmd, depth = 0, opts = {}) {
  const ps = opts.tool === 'PowerShell'
  const buildBlank = (w) => ' '.repeat(w.length)
  let view = buildCommandView(cmd, opts.tool)
  if (ps) view = view.replace(/<#[\s\S]*?#>/g, buildBlank)
  view = view.replace(/(^|[\s;&|()<>])#[^\n]*/g, (w, p) => p + ' '.repeat(w.length - p.length))
  view = ps ? view.replace(/`\r?\n/g, buildBlank) : view.replace(/\\(?:\r?\n|[\s\S])/g, (w) => (w.endsWith('\n') ? buildBlank(w) : w))
  const out = []
  if (opts.inline) {
    let masked = ''
    let from = 0
    for (const u of scanSubstitutions(view, opts.tool)) {
      out.push(...scanCommandHeads(cmd.slice(...u.body), depth, opts))
      masked += view.slice(from, u.from) + '_'.repeat(u.to - u.from)
      from = u.to
    }
    view = masked + view.slice(from)
  }
  const red = scanRedirects(cmd, view, opts.tool)
  view = red.view
  if (opts.inline) for (const v of red.targets) out.push({ redirect: v })
  const seg = /[^;|&()\n]+/g
  const bodies = opts.inline ? readHeredocBodies(cmd) : []
  let m
  while ((m = seg.exec(view)) !== null) {
    const opened = bodies.find((h) => h.open >= m.index && h.open < m.index + m[0].length)
    const here = opened ? cmd.slice(opened.from, Math.max(opened.from, opened.to)) : undefined
    // a quote left open takes the rest: `cp a "C:\x\"` from PowerShell, read as Bash, leaves one
    const tok = new RegExp(opts.inline ? `${VIEW_TOKEN}|["'][\\s\\S]*` : VIEW_TOKEN, 'g')
    const raw = []
    let t
    while ((t = tok.exec(m[0])) !== null) raw.push(cmd.slice(m.index + t.index, m.index + t.index + t[0].length))
    const a = raw.map(readWordText)
    let k = 0
    const reserved = []
    for (;;) {
      while (k < a.length && /^[A-Za-z_][A-Za-z0-9_]*=/.test(a[k])) k++
      if (opts.reserved && SHELL_RESERVED_WORDS.includes(a[k])) {
        const w = a[k++]
        reserved.push(w)
        if (w === 'function' || (w === 'coproc' && NAMED_COPROC.includes(a[k + 1]) && !SHELL_RESERVED_WORDS.includes(a[k]))) k++
        continue
      }
      if (GATE_PREFIX_WORDS.includes(a[k])) {
        k = scanLauncherOptions(a, k + 1, GATE_OPTION_RULES[a[k]], depth, out, opts)
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
    const text = cmd.slice(m.index, m.index + m[0].length).trim()
    let launched = false
    if (GATE_LAUNCHERS.includes(lb) || /^python3\.\d+$/.test(lb)) {
      const family = lb === 'bash' || lb === 'sh' ? 'shell' : lb === 'node' ? 'node' : 'python'
      const at = k
      k = scanLauncherOptions(a, k + 1, GATE_OPTION_RULES[family], depth, out, opts)
      if (opts.inline && family !== 'shell') {
        const e = k <= -2 ? a[-2 - k] : ''
        const inline = (family === 'python' ? /c$/.test(e) : /^(?:-e|--eval|-p|--print)$/.test(e)) ? a[-1 - k]
          : k >= a.length || (family === 'python' && a[k] === '-') ? here : undefined
        if (inline !== undefined) out.push({ text, head: a[at], argv: a.slice(at), launched: false, reserved, here, inline })
      }
      if (k < 0 || k >= a.length) continue
      launched = true
    }
    out.push(Object.assign({ text, head: a[k], argv: a.slice(k), launched, reserved }, opts.inline ? { here, raw: raw.slice(k) } : {}))
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
 * The seconds GNU `sleep` waits for <words>, summed: a decimal number with an optional `s`, `m`,
 * `h` or `d` suffix, or `infinity`. Any other word makes the sum null.
 */
function deriveSleepSeconds(words) {
  const unit = { '': 1, s: 1, m: 60, h: 3600, d: 86400 }
  let sum = 0
  for (const w of words) {
    if (w === 'infinity') { sum = Infinity; continue }
    const r = /^(\d+(?:\.\d*)?|\.\d+)([smhd]?)$/.exec(w)
    if (!r) return null
    sum += parseFloat(r[1]) * unit[r[2]]
  }
  return sum
}

/**
 * The polling rows (TOOL-aTrimmedWait-6): `{ row, c }` for the first simple command of <cmd>, its
 * reserved words stepped, that is P1 a `tail` with a follow option, P2 a `sleep` in a command holding
 * a `while` or `until` loop, or P3 a `sleep` of POLL_SLEEP_FLOOR_S or more, or of a duration that
 * does not read; else null. <tool>, the tool's name, is scanCommandHeads' `opts.tool`.
 */
function checkPollWait(cmd, tool) {
  const cs = scanCommandHeads(cmd, 0, { reserved: true, tool })
  const loop = cs.some((c) => c.reserved.includes('while') || c.reserved.includes('until'))
  for (const c of cs) {
    const b = buildBaseName(c.head)
    const rest = c.argv.slice(1)
    if (b === 'tail' && rest.some((w) => w === '--follow' || w.startsWith('--follow=') || /^-[A-Za-z0-9]*[fF][A-Za-z0-9]*$/.test(w))) return { row: 'P1 tail follow', c }
    if (b !== 'sleep') continue
    if (loop) return { row: 'P2 sleep in a loop', c }
    const s = deriveSleepSeconds(rest)
    if (s === null || s >= POLL_SLEEP_FLOOR_S) return { row: `P3 sleep at or over ${POLL_SLEEP_FLOOR_S} s`, c }
  }
  return null
}

function renderPollDeny(type, c, row) {
  return (
    `BLOCKED by scratch-guard: a role agent does not poll. Agent type ${type} ran \`${c.text}\`, which is row ${row}.\n\n` +
    'A command started with run_in_background notifies this agent when it exits, so that notification is the wait. ' +
    `A pause under ${POLL_SLEEP_FLOOR_S} s outside a while or until loop is admitted.\n`
  )
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
    (shown === null
      ? `No checkout root was found from the payload cwd, CLAUDE_PROJECT_DIR or the script's directory, so no role index was read and the allowlist of ${type} is empty. `
      : `The allowlist of ${type} in the role index ${shown} is ${allow.length ? allow.map((n) => `"${n}"`).join(', ') : 'empty'}. `) +
    'Gates run in the main session at the merge or push threshold, so return the need in your result, ' +
    'and verify your change with a fixture or a probe of your own code.\n'
  )
}

/**
 * The checkout root a role arm reads its index at (TOOL-aOrientedCast-14): the toplevel above the
 * payload <cwd>, else above `env.CLAUDE_PROJECT_DIR`, else above the directory of each of <cands>'
 * launched script, its head resolved against the payload <cwd> (TOOL-dBoundRoles-8 S1), each start
 * resolved as checkRouted resolves its session start, else null. The cwd comes first because the
 * command or spawn runs there; a relative head with no payload cwd is no start. Agent-cap's rule 6
 * passes no <cands>, so only the first two starts apply there.
 */
function resolveRoleRoot(cwd, env, cands) {
  const path = require('path')
  const starts = [cwd, env && env.CLAUDE_PROJECT_DIR]
  for (const c of cands || []) {
    const head = buildNativePath(c.head)
    if (typeof cwd === 'string' && cwd !== '') starts.push(path.dirname(path.resolve(buildNativePath(cwd), head)))
    else if (path.isAbsolute(head)) starts.push(path.dirname(path.resolve(head)))
  }
  for (const start of starts) {
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
 *  2. no simple command whose head is a launched script, a path-bearing word, or a G2 or G3 shape,
 *     and no polling hit by checkPollWait → null, with no file read
 *  3. no root by resolveRoleRoot (the payload `cwd`, then `CLAUDE_PROJECT_DIR`, then each candidate's
 *     launched script's directory, TOOL-dBoundRoles-8 S1) → each candidate tried against G2 and G3
 *     with an empty allowlist, a match refusing and saying no checkout root was found; otherwise one
 *     witness naming the three starts and that G1 and the polling rows are unarmed (§8 F4)
 *  4. loadRoleIndex: absent → null, or deny naming the index and its re-render where the tree is
 *     governed (checkRoleGoverned, TOOL-dBoundRoles-6 S3); broken → deny naming the index
 *  5. the allowlist: the index's `gates` list for the type, else empty — `workflow-subagent` and
 *     every type the index does not name may run nothing
 *  6. readGateLegs: no manifest, an absent one or one that does not parse leaves G1 unarmed and
 *     returns a witness naming it; G2 and G3 still bind
 *  7. each simple command: an allowlisted G1 leg is admitted whole; else G2, G3, then G1 refuses
 *  8. a polling hit refuses with renderPollDeny, so a gate row refusing the same command wins
 *  9. G1 unarmed → its witness; else null
 */
function checkRoleGate(cmd, data, env) {
  const path = require('path')
  const type = typeof data.agent_type === 'string' ? data.agent_type : ''
  if (!type) return null
  const cands = scanCommandHeads(cmd, 0, { tool: data.tool_name }).filter((c) => c.launched || /[\\/]/.test(c.head) || checkGateRunner(c) || checkGateSuite(c))
  const poll = checkPollWait(cmd, data.tool_name)
  if (cands.length === 0 && !poll) return null
  const raw = typeof data.cwd === 'string' ? data.cwd : ''
  const project = env && env.CLAUDE_PROJECT_DIR
  const top = resolveRoleRoot(raw, env, cands)
  if (!top) {
    for (const c of cands) {
      const row = checkGateRunner(c) ? 'G2 runner' : checkGateSuite(c) ? 'G3 suite' : null
      if (row) return { deny: renderGateDeny(type, c, row, null, [], null) }
    }
    return { witness: `role-gate rows G1 leg and P1 to P3 unarmed — neither the payload cwd ${raw || '(none)'}, CLAUDE_PROJECT_DIR ${project || '(unset)'} nor a launched script's directory lies in a checkout, so no role index was read; rows G2 runner and G3 suite still bind` }
  }
  // G1 resolves the command's paths against the payload cwd, and against the root when it has none.
  const cwd = raw ? path.resolve(raw) : top
  const index = loadRoleIndex(top)
  if (index.state === 'absent') {
    if (!checkRoleGoverned(top)) return null
    return { deny: `BLOCKED by scratch-guard: a role agent runs no gate, and the role index ${index.shown} is absent while this tree carries rendered role agents, so the allowlist of ${type} cannot be read. Re-render the index with render_agents.py --write; gates run in the main session at the merge or push threshold (TOOL-dBoundRoles-6).\n` }
  }
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
  if (poll) return { deny: renderPollDeny(type, poll.c, poll.row) }
  return g.legs ? null : { witness: `role-gate row G1 leg unarmed — ${g.why}; rows G2 runner and G3 suite still bind` }
}

// ---- the subagent context (TOOL-aRoutedQuill-4) ------------------------------------------------

/** The harness's cap on a hook's additionalContext, in characters (Claude Code's documentation). */
const ROUTE_CONTEXT_CAP = 10000
/** The card file the card engine renders into each session tree, ignored by every clone (PLAY-dOrderedCharter-8). */
const CARD_FILE_REL = '.claude/orientation-card.md'
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
 *  6. one line per unit the build's RUN_STATE_FILE records as dispatched, the card does not route,
 *     and checkBuildable admits — the gate's step 9b through the same readDispatchedUnits, budgeted
 *     after the route lines. A dispatched unit that is not buildable is not listed, as step 9b lists
 *     none; nor is whether its pass committed checked (TOOL-aSmoothedDispatch-6)
 * The card is located as checkRouted locates it, so the context and the gate read one card.
 * When the session tree holds the card file, every text from step 3 on is wrapped in that file's first
 * and last lines, its level-1 envelope (PLAY-dOrderedCharter-8 S6), counted inside ROUTE_CONTEXT_CAP.
 */
function renderRouteContext(data, env) {
  const path = require('path')
  const start = env.CLAUDE_PROJECT_DIR || (typeof data.cwd === 'string' ? data.cwd : '')
  if (!start) return ''
  const hit = resolveToplevel(path.resolve(buildNativePath(start)))
  const common = hit && resolveCommonDir(hit)
  if (!common) return ''
  const top = hit.toplevel
  const envelope = readCardEnvelope(top)
  const text = renderRouteText(data, top, common, envelope ? envelope.length + 2 : 0)
  if (!envelope || !text) return text
  const wrapped = `${envelope.open}\n${text}\n${envelope.close}`
  // ponytail: a pair too long for the cap leaves the text bare rather than cut; the file is the engine's render
  return wrapped.length <= ROUTE_CONTEXT_CAP ? wrapped : text
}

/** The card file's envelope, `{ open, close, length }`, its first and last non-empty lines copied and never
 *  typed here; null when `<top>/.claude/orientation-card.md` is absent, unreadable or holds one line. */
function readCardEnvelope(top) {
  const fs = require('fs')
  const path = require('path')
  let lines
  try {
    lines = fs.readFileSync(path.join(top, CARD_FILE_REL), 'utf8').split(/\r?\n/).filter((l) => l !== '')
  } catch {
    return null
  }
  if (lines.length < 2) return null
  const open = lines[0]
  const close = lines[lines.length - 1]
  return { open, close, length: open.length + close.length }
}

/** renderRouteContext's text before its envelope, `reserve` characters of the cap held back for it. */
function renderRouteText(data, top, common, reserve) {
  const fs = require('fs')
  const path = require('path')
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
  let budget = ROUTE_CONTEXT_CAP - reserve - head.length - tail.reduce((s, l) => s + l.length + 1, 0) - (renderClosing(route.lines.length).length + 1)
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
  // Step 6: the gate's step 9b, read through the same function; only a buildable unit is named. Read
  // only when no card unit is buildable, the set and test `checkRouted` walks at step 9a before it
  // reaches 9b (TOOL-aSmoothedDispatch-8 S6): a card unit that admits means no dispatch row is read.
  if (!route.units.some((u) => !checkBuildable(u, route.build, top, memRoot.trim(), confBytes))) {
    const dispatched = readDispatchedUnits(top, memRoot.trim(), route.build)
    const onCard = new Set(route.units.map((u) => u.unit))
    for (const u of dispatched.units) {
      if (onCard.has(u.unit) || checkBuildable(u, route.build, top, memRoot.trim(), confBytes)) continue
      const st = readStatusCells(fs.readFileSync(path.join(top, buildNativePath(u.spec)), 'utf8'))
      const v = `${u.unit} is buildable through its dispatch row in ${dispatched.file}, which scratch-guard counts as routed: ${st.tier} at ${st.status}.`
      if (v.length + 1 > budget) break
      budget -= v.length + 1
      verdicts.push(v)
    }
  }
  const out = [head, ...kept, ...verdicts, ...tail]
  if (kept.length < route.lines.length) out.push(renderClosing(route.lines.length - kept.length))
  return out.join('\n')
}

// The three read tools the main-loop read arm judges (TOOL-dBoundRoles-10 S2); `main` routes them to
// checkDriverRead and exits, so a read never reaches checkRouted or the Bash checks.
const READ_TOOLS = ['Read', 'Grep', 'Glob']

/**
 * THE MAIN-LOOP READ ARM (TOOL-dBoundRoles-10 S1): the policy key `driver.reads` over a `Read`,
 * `Grep` or `Glob` payload, first match wins. null admits, `{ witness }` admits with one line,
 * `{ deny }` refuses.
 *  1. the payload carries an `agent_type` -> null: a worker keeps its read-only probes (RL-5).
 *  2. the payload `cwd`, else `env.CLAUDE_PROJECT_DIR`, lies in no repository -> null, not this arm's.
 *  3. no policy kit resolves beside this hook (this file's resolvePolicyHelper) -> witness,
 *     `driver.reads unarmed`.
 *  4. `readPolicy('driver.reads')` at the toplevel, the landed revision's value, never the working
 *     tree's: a reader that throws or refuses -> witness naming the reader's line, the read admitted,
 *     since the reads that repair a broken policy mirror are the driver's (TOOL-dBoundRoles-43 S40).
 *  5. `read-only-probes` -> null; `state-reads-only` and a `Read` -> null; any other value and tool,
 *     `state-reads-only`'s `Grep` and `Glob` and every read under `none-scout-only` -> deny.
 * Each refusal names the key, its value, the driver's remedy, a scout dispatched through a rendered
 * handoff, and the owner's, another value set through the policy file's one door (S6). WHAT IT DOES
 * NOT CHECK: which file a `Read` names, since no record says what the driver was handed (§8 F1); and
 * the main loop's `grep`, `find` or `cat` run through Bash, which this arm never sees.
 */
function checkDriverRead(data, env) {
  if (data && typeof data.agent_type === 'string' && data.agent_type !== '') return null
  const fs = require('fs')
  const tool = data.tool_name
  const start = (typeof data.cwd === 'string' && data.cwd !== '') ? data.cwd : ((env && env.CLAUDE_PROJECT_DIR) || '')
  const hit = start ? resolveToplevel(start) : null
  if (!hit) return null
  const helper = resolvePolicyHelper()
  if (!helper || !fs.existsSync(helper)) {
    return { witness: `driver.reads unarmed — no policy kit resolves beside this hook, so the main loop's ${tool} is admitted (TOOL-dBoundRoles-10)` }
  }
  let v
  try {
    v = require(helper).readPolicy('driver.reads', { repo: hit.toplevel }).value
  } catch (e) {
    // TOOL-dBoundRoles-43 S40 (§8 F13): a broken policy mirror is no fault of the driver's, and the reads that
    // repair it are the driver's own, so a throw or a refusal of the reader admits the read with one witness
    return { witness: `driver.reads unread — the policy reader refused (${String((e && e.message) || e).split(/\r?\n/)[0]}), so the main loop's ${tool} is admitted while the policy is repaired (TOOL-dBoundRoles-43)` }
  }
  if (v === 'read-only-probes' || (v === 'state-reads-only' && tool === 'Read')) return null
  const why = v === 'state-reads-only'
    ? `driver.reads is state-reads-only, under which the main loop reads cheap state only: a Read of one named file, \`next\`, a short git state command; every ${tool} is a search, and anything exploratory is a scout's task`
    : v === 'none-scout-only'
      ? 'driver.reads is none-scout-only, under which every read the main loop would make is a scout\'s task'
      : `driver.reads reads ${JSON.stringify(v)}, none of none-scout-only, state-reads-only and read-only-probes, so no read is admitted under it`
  return { deny: `BLOCKED by scratch-guard: the main loop's ${tool} is refused (TOOL-dBoundRoles-10) — ${why}.\n` +
    'The driver\'s remedy: dispatch a scout, the gov-researcher role, through a rendered handoff, `handoff.py render --role gov-researcher --build <slug> --part task` passed unchanged as an Agent call\'s prompt, and read what it returns.\n' +
    'The owner\'s: set another value of driver.reads, read-only-probes to admit the main loop\'s searches, through the policy file\'s one door, the loop kit\'s policy_edit.py.\n' }
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
  if (data && READ_TOOLS.includes(data.tool_name)) {
    // The main-loop read arm (TOOL-dBoundRoles-10 S2). It FAILS CLOSED for the main loop, as the write
    // gate does: a throw that admitted would be a silent off. A worker returns at step 1 and is never refused.
    let read
    try {
      read = checkDriverRead(data, process.env)
    } catch (e) {
      read = data.agent_type ? null : { deny: `BLOCKED by scratch-guard: the main-loop read arm threw (${(e && e.message) || e}) and fails closed on a ${data.tool_name} (TOOL-dBoundRoles-10).\n` }
    }
    if (read && read.deny) {
      process.stderr.write(read.deny)
      process.exit(2)
    }
    if (read && read.witness) process.stderr.write(`scratch-guard: ${read.witness}\n`)
    process.exit(0)
  }
  if (data && WRITE_TOOLS.includes(data.tool_name)) {
    // FAILS CLOSED, unlike the two Bash checks below: a write gate that throws and admits is the
    // silent off D7 gives no bypass. spawn-guard.js keeps the same rule for its spec-audit kind (S8).
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
  // The shell-write arm (TOOL-dBoundRoles-7), after the role-gate arm, and it FAILS CLOSED for a role
  // agent as that arm does (S6). The main loop is never judged by it, and never refused by its throw.
  let shell = null
  try {
    shell = checkShellWrites(cmd, data, process.env)
  } catch (e) {
    shell = data.agent_type ? { deny: `BLOCKED by scratch-guard: the shell-write arm threw (${(e && e.message) || e}) and refuses a role agent's ${data.tool_name} call (TOOL-dBoundRoles-7).\n` } : null
  }
  if (shell && shell.deny) {
    process.stderr.write(shell.deny)
    process.exit(2)
  }
  if (shell && shell.witness) process.stderr.write(`scratch-guard: ${shell.witness}\n`)
  process.exit(0)
}


// TOOL-dBoundRoles-25 S4 — THE HELPERS TWO KITS READ, moved here from the retired agent limit hook (§8 F7). The
// roles kit's spawn guard (`<prefix>/roles/spawn-guard.js`) and this kit's own hooks read the marker reader,
// the args reader, the slug walk, the policy helper's locator and the sibling-kit resolver, and so does the
// review kit's spec-audit opt-in pack; a helper two kits read lives in this file's exports, over the roles
// kit's declared `requires_if` edge. ONE copy each, beside `readUnfencedLines`, which the marker reader walks.
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

// The roles kit's `MARKER_RE` spelled again with the same named groups (brief I5), since a kit imports no
// sibling kit: `item=` is optional, so a marker written before it still matches (TOOL-dBoundRoles-17 S1).
const HANDOFF_MARK_RE = /^<!-- gov:handoff role=(?<role>\S+) build=(?<build>\S+) unit=(?<unit>\S+)(?: item=(?<item>\S+))? path=(?<path>\S+) role-sha=(?<roleSha>[0-9a-f]{12}) task-sha=(?<taskSha>[0-9a-f]{12}) -->$/

// Every line of `text` outside a fence, carriage returns stripped, that is a whole marker line with its
// fields in order: `{ line, role, build, unit, item, path, roleSha, taskSha }` each, read by group name;
// `item` is the field's string, `-` included, or null for a marker carrying none. The lines are the ones
// scratch-guard's `readUnfencedLines` yields, so a marker quoted inside handed content, which the renderer
// fences, is content and is not counted (TOOL-dBoundRoles-38 S4).
function extractHandoffMarker(text) {
  const out = []
  for (const [, raw] of readUnfencedLines(text)) {
    if (raw === null) continue
    const line = raw.replace(/\r/g, '')
    const m = HANDOFF_MARK_RE.exec(line)
    if (!m) continue
    const g = m.groups
    out.push({ line, role: g.role, build: g.build, unit: g.unit, item: g.item === undefined ? null : g.item, path: g.path, roleSha: g.roleSha, taskSha: g.taskSha })
  }
  return out
}

// TOOL-dFairHearing-43 S6 - found through `resolveKitDir`; a refusal reads as the absent helper, an empty path.
function resolvePolicyHelper() {
  try { return require('path').join(resolveKitDir('policy', 'policy-mirror.js', __dirname), 'policy-mirror.js') } catch { return '' }
}

// TOOL-dFairHearing-32 S25 — THE SIBLING-KIT RESOLVER, ported from `resolve_kit_dir.py` in gov's lib dir
// rung for rung, and held to it row for row by that dir's resolve-python.test.sh (§2k), so it cannot
// drift silently the way a hand port did (TOOL-aMendedFleet-102). The directory holding <anchor> of the
// kit gov homes at <home>: 1. a `.governance/install.json` row, at the root the nearest `.git` names,
// whose `path` is a file inside the tree and whose `source` ends <home>/<anchor>, or a `rendered` row
// whose template sits under <home>/ and whose `path` names <anchor>; a row whose path escapes the tree,
// holds `..` or names no file is skipped; 2. <here>/<home>/<anchor>, then <here>/../<home>/<anchor>;
// 3. a thrown Error naming the three places looked, its `receipt` the receipt's path.
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

if (require.main === module) main()
module.exports = { resolveToplevel, resolveCommonDir, checkCommand, buildCommandView, buildComparablePath, resolveAllowedRoots, readFrontMatterKey, ANCHOR_MODES, KIT_SCRATCH_GUARD_VERSION, checkRouted, checkBuildable, extractRouteUnits, readConfKey, checkUnarmed, readCard, WRITE_TOOLS, ROUTE_CONF, renderRouteContext, ROUTE_CONTEXT_CAP, loadRoleIndex, checkRoleGoverned, ROLE_INDEX, checkStatusOnlyEdit, buildEditResult, checkRoleGate, checkWriteClass, checkRoleClass, checkPollWait, SHELL_RESERVED_WORDS, scanCommandHeads, resolveRoleRoot, RUN_STATE_FILE, readDispatchedUnits, readOpenReds, checkRedLane, readUnfencedLines, scanWriteTargets, checkShellWrites, readWorkOrderAllowance, checkRoutedEntry, checkDriverRead, RUN_ID_RE, WORKFLOW_RUNS_DIR, resolveSessionDir, KIT_AGENT_CAP_VERSION, extractBuildSlug, extractWorkflowArgs, HANDOFF_MARK_RE, extractHandoffMarker, resolvePolicyHelper, resolveKitDir }
