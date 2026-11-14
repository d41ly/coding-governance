#!/usr/bin/env node
/**
 * gate-guard — a PreToolUse guard that refuses the flagged merge bar and every self-test suite
 * while the unattended run on the current branch is in a phase before VERIFYING, and refuses an
 * `AskUserQuestion` call from the session holding a non-terminal run's lease.
 *
 * gov:kit unattended@1.121 — a courtesy marker; the kit version gate pairs the four named `.sh`
 * carriers and every `*.template.md`, and does not read this one.
 *
 * Contract: the spec for TOOL-aDeferredBar-3 under the build folder of that slug.
 *
 * WHY THIS IS A HOOK AND NOT A RULE. The rule already exists in five carriers a build agent reads
 * (TOOL-aDeferredBar-1) and the memory gate refuses a spec that names the bar as an observation
 * (TOOL-aDeferredBar-2). Neither reaches the act: an agent inside a `Workflow` sidechain holds the
 * instruction and still types `GATE_SELFTESTS=1 bash <prefix>/run-gates/run-gates.sh` into a unit
 * pass, and the run stalls for the hours the close will spend again. The tool call is the only
 * surface that sees the act, and a `Bash|PowerShell` PreToolUse hook fires inside a sidechain
 * (`TOOL-cRefutedPremise-1`). Close to half of the corpus runs come from there.
 *
 * WHAT IT DENIES, at COMMAND POSITION in a string-blanked view of the command — the head word after
 * any of `env`, `export`, `time`, `nohup`, `NAME=value` words, `timeout` with its options
 * (`-k`/`-s`/`--kill-after`/`--signal` take a value) and a duration that is a literal, a decimal
 * or a `$` expansion (round 3 T5), `stdbuf`/`nice`/`ionice` with their options, and a launcher
 * with one option:
 *   D1  `GATE_FULL=<value>` or `GATE_SELFTESTS=<value>` with a NON-EMPTY value, bare or after
 *       `export`, and the PowerShell-native spellings too — `$env:`/`$Env:`/`$ENV:` and
 *       `${env:NAME}`, glued or with whitespace on either side of the `=` (closing review F8;
 *       round 2 R4; round 3 T2 for `NAME= value`); the empty assignment, bare or quoted, is the
 *       OFF spelling the runner's own `-n` test reads, so it is the plain bar and is not a hit.
 *   D2  a word ending `run-selftests.sh`           — every declared self-test
 *   D3  a word ending `run-unattended-gates.sh`    — this kit's own suites
 *   D4  a word ending `.test.sh` or `selftest.py`  — any one suite, other kits' included; the
 *       launcher in front may be `bash`, `sh`, `python`, `python3`, a versioned `python3.x` or
 *       `py` (round 2 R12: the resolver's own third candidate), carrying one short option, `py`'s
 *       version selector (`-3`, `-3.12`) or `-X` with its value (round 3 T6). A bare `--selftest`
 *       FLAG on some other file (`gotchas.py --selftest`) is the seconds-long direct check the
 *       child prompt names and is NOT a hit; the whole-suite `selftest.py` FILE is (closing
 *       review F2 — six of the manifest's `chunk = selftests` legs are that file, govkit's at
 *       3445 s among them).
 *   D5  the quoted body of `bash -c` / `sh -c`, scanned once as a command of its own
 *   D6  a script the gate manifest declares a suite by cost (TOOL-aClearedLedger-3, and
 *       TOOL-aClearedLedger-11 for the match): ANY word of a simple command, and the words after
 *       it, spell a `chunk = selftests` leg of MANIFEST_BASENAME, read in the directory above this
 *       file, whose `ceiling` is above DIRECT_CHECK_BOUND and whose argv carries one of
 *       DIRECT_CHECK_WORDS. The word need not be the head the grammar above resolves, so a
 *       launcher it does not skip (`"$PY"`, `python.exe`, `python3 -u -B`, `python -m pdb`, an
 *       `if`) hides nothing. The word names the leg's script with `\` folded to `/`, case ignored
 *       and leading `./` taken off, by a trailing path in EITHER direction: `<dir>/<script>` and
 *       the bare file name after a `cd` both do. A SHORTER spelling that still reaches the leg's
 *       direct-check word is a hit (`check_policy.py --fixture` runs every case), and so is one
 *       whose option VALUE differs from the leg's (`--strict-from <other dir>` scopes nothing);
 *       a LONGER one, or one whose option name differs, is a scoped variant and is not
 *       (`check_policy.py --fixture <case>`, `--fixture --list`). Redirection words are taken out
 *       before the compare, and a word ends at a glued `>` or `<`, which rows D2 to D4 gain too.
 *       A direct-check form at or under the bound stays the direct check a spec names.
 *       WHAT ROW D6 DOES NOT TELL APART OR SEE: two files that share a file name, or a trailing
 *       path, read alike; an unquoted mention of a script and its direct-check word at an argument
 *       position (`echo <script> --selftest`) reads as a run; a path assembled at run time, a
 *       module name after `-m` with no path, and a python heredoc walk past it; a spelling whose
 *       option name differs from the leg's is read as scoped, whatever the script does with it;
 *       a redirection carrying `&` ahead of the direct-check word cuts the command there
 *       (`<script> 2>&1 --selftest`, `<script> &>x.log --selftest`), so the script and its word
 *       fall into two commands though bash runs the suite (TOOL-aClearedLedger-13);
 *       and it does not see a suite the manifest does not declare or declares in another chunk,
 *       and reads the manifest uncommitted. The spec lint's bar join holds the same rule and reads
 *       these spellings this row does not: a redirection carrying `&`
 *       ahead of the direct-check word, a glued variable prefix (`${DIR}<script>`), a quoted
 *       mention, a quoted operator character before a redirection (`'&'>x.log`, `'>'>x.log`),
 *       which this row keeps as an argument, and a `bash -c` body inside another.
 * A D2, D3 or D4 token is NOT a hit when the same simple command carries one of READ_ONLY_VERBS:
 * those forms answer in seconds and one of them is how the memory-tree kit re-renders its guides.
 * Row D6 does not consult them: a command carrying one is a longer spelling and misses.
 * The rows are measured against the manifest rather than restated beside it: the suite's parity arm
 * feeds every `chunk = selftests` argv to this predicate, exempting a direct-check form only at or
 * under the bound and printing each exemption (round 2 R3). Rows D2 to D4 are textual; row D6 is
 * the one that reads a ceiling, so a flag-form suite above the bound is denied and not declared.
 *
 * THE QUESTION ARM (TOOL-aOrientedCast-22). An unattended run never asks (BUILD-METHOD M10): nobody
 * is there to answer, and a run that called `AskUserQuestion` stalled until the owner came back. A
 * payload whose `tool_name` is `AskUserQuestion` goes to `checkAsk`, which keys on the SESSION and
 * not the branch: `run-lease.js`, required by `__dirname` as stop-guard.js requires it, returns the
 * records whose `session:` fact under `## Run facts` equals the payload's `session_id`. A lease whose
 * phase is empty, `absent` or in PHASES_TERMINAL is not live and costs no spawn. For each lease left
 * the arm asks the driver whether the run is finished (TOOL-aOrientedCast-24): `runLiveness` and
 * `parseLiveness`, required from stop-guard.js by `__dirname`, run `unattended.sh --liveness <slug>`
 * under stop-guard's bound, so the two hooks read one answer. A lease whose liveness reads TERMINAL
 * is finished and allows; any other verdict denies and is named in the deny; an unreadable liveness
 * leaves the recorded phase standing and the deny says so. The deny names the run, its phase, its
 * liveness and record, and the driver's `--park` route, or `--landed` at FINISHED-UNSTAMPED, with
 * each question and its option labels quoted
 * from the payload, each value cut to ASK_QUOTE_MAX characters and stripped of control characters.
 * It does NOT check whether the question is one the protocol lets the run decide, whether the
 * session is alive, or which branch it is on; and it sees nothing the harness does not route
 * through PreToolUse, which only a live session can observe (the spec's AC7).
 *
 * WHAT IT NEVER DENIES. The plain bar — `run-gates.sh` with neither flag — is the scoped form the
 * owner allows at the main loop, and this hook cannot tell a child from the main loop; the child
 * prompt forbids it there by instruction. Nor the pass-leg runner `pass-legs.sh` with neither
 * flag: it matches none of rows D1 to D6, and scratch-guard's row G2 refuses it to a role agent.
 * A quoted MENTION of any of the shapes — a commit
 * message, a `grep` argument, a heredoc body — is invisible by construction of the view, with one
 * exception read on purpose: a `$( … )` or backtick span inside DOUBLE quotes, or inside an
 * UNQUOTED heredoc body (`<<EOF`, which bash expands before the consumer reads a line; a
 * `<<'EOF'` body stays content — round 3 T1), is a command (closing review F7; round 2 R5 R6
 * R13), scanned as one of its own the way row D5 scans a `bash -c` body, so
 * `printf '%s' "$(bash <suite>)"` is the run it is, a grep argument or a string tail beside the
 * span stays content, and the same span in single quotes stays content. Under PowerShell the
 * backtick inside double quotes is the escape character and opens no span (round 3 T3). Nor does
 * it deny a question from a session holding no lease — an owner's attended session on the run's
 * branch may still ask — or from one whose run is at `LANDED` or `ABORTED`, or whose `--liveness`
 * reads TERMINAL.
 *
 * THE KEY. The predicate runs first, and the filesystem is read only on a hit or a row D6
 * candidate — a simple command carrying one of DIRECT_CHECK_WORDS: the overwhelming
 * majority of tool calls carry neither and cost one scan of one string. The manifest is read
 * once, and only after a live run is found. On a hit or a candidate the hook
 * walks up from the payload's `cwd` to `.git`, reads the PER-WORKTREE `HEAD` (never the common
 * dir's, whose HEAD is the primary tree's branch), reads `MEMORY_ROOT` from `.unattended.conf`,
 * and reads every `<MEMORY_ROOT>/builds/<slug>/RUN.md` whose `run-branch:` — else `branch-ref:`,
 * for a record written before that fact existed — equals the ref `HEAD` names. Two stale BUILDING
 * records on branches nobody has checked out for days must key nothing, which is why the key is
 * the branch and never the existence of a record. A matched record in a phase outside
 * PHASES_ALLOW denies, naming that record.
 *
 * NO PATH OUTSIDE THIS FILE IS SPELLED. The conf key, the conf basename, the record basename and
 * the manifest basename are the only names; the kit dir, the memory root and the record path are
 * derived from the walk, and the manifest is read in the directory above this file's own.
 * The four allowed phase names are restated here deliberately (spec §8 F5): reading them from the
 * driver at run time would switch this hook off silently the day the driver could not be read,
 * because the hook fails open; four literals pinned by a direct read and a suite arm fail loudly.
 * PHASES_TERMINAL restates the driver's terminal pair for the same reason, pinned by its own arm.
 * The question arm requires `run-lease.js` and `stop-guard.js`, sibling basenames of this kit, by
 * `__dirname`, and names the driver by its bare file name, as the bar arm names the runner.
 *
 * ponytail: the predicate is TEXTUAL, the same ceiling scratch-guard.js states of itself. A path
 * assembled at run time (`s=<dir>; bash $s/x.test.sh`) and a python heredoc that spawns a suite
 * both walk past it. No call in the corpus has either shape; the upgrade path is a tokenizer.
 * ponytail: READ_ONLY_VERBS is textual and generic — a suite that ignores an unparsed `--check`
 * would run whole behind it. No call in the corpus has that shape either.
 *
 * FAILS OPEN. Unparseable stdin, an unknown tool, a missing command, no `.git`, a detached HEAD,
 * no conf, no record on this branch, no lease for the session, an unloadable `run-lease.js`:
 * every one exits 0. An absent manifest, one that does not parse and one that is no list leave
 * row D6 unarmed and rows D1 to D5 standing. This is a hygiene rule, not a containment
 * boundary; a security control would have to fail the other way. ONE input does not allow: an
 * unreadable liveness (no `verdict:` line, a non-zero exit, the bound, or stop-guard.js failing to
 * load) leaves a leased run's recorded phase standing, because an allow there would switch the
 * question arm off on every node whose driver cannot run, which is the silent switch-off
 * PHASES_TERMINAL is restated to avoid.
 *
 * Protocol: deny = stderr text + exit 2. Allow = print nothing, exit 0. Matches the sibling hooks.
 */
'use strict'

const fs = require('fs')
const path = require('path')

const KIT_GATE_GUARD_VERSION = '1.0'

const TOOLS = ['Bash', 'PowerShell']
// The TAIL of PHASES_CORE in unattended.sh from VERIFYING onward. Pinned to the driver by a direct
// read (spec AC6) and by the parity arm in gate-guard.test.sh; every other phase denies, a
// project's PHASES_EXTRA members included, because an extra phase is by construction before landing.
const PHASES_ALLOW = ['VERIFYING', 'LANDING', 'LANDED', 'ABORTED']
// The question arm's tool, and the driver's PHASES_TERMINAL restated (pinned by its parity arm in
// gate-guard.test.sh): a leased run in any other phase, HELD included, refuses its session's question.
const ASK_TOOL = 'AskUserQuestion'
const PHASES_TERMINAL = ['LANDED', 'ABORTED']
const ASK_QUOTE_MAX = 300
// Measured on node a, 2026-09-13, each direct: --list 5 s · --check 17 s · --rank 3 s · --help 3 s ·
// --render 1 s. Generic over rows D2 to D4 and never over D1.
const READ_ONLY_VERBS = ['--list', '--check', '--rank', '--help', '--render']
const CONF_BASENAME = '.unattended.conf'
const CONF_KEY = 'MEMORY_ROOT'
const RECORD_BASENAME = 'RUN.md'
// Row D6 (TOOL-aClearedLedger-3). A leg whose `ceiling` is at or under the bound is a direct check;
// 300 is the manifest's default ceiling. The words are the arguments that make a script run its own
// checks. Both are restated in gate-guard.test.sh and pinned there against these exports.
const DIRECT_CHECK_BOUND = 300
const DIRECT_CHECK_WORDS = ['--selftest', '--fixture', 'fixture']
const MANIFEST_BASENAME = 'gate-legs.json'
const MAX_NEST = 1

function readStdin() {
  try {
    return fs.readFileSync(0, 'utf8')
  } catch {
    return ''
  }
}

/**
 * Every heredoc body in `cmd` as `{from, to, quoted}`; `quoted` when the delimiter was written
 * `<<'EOF'` or `<<"EOF"`. Bash expands an UNQUOTED body — parameters, `$( … )` and backticks —
 * before the consumer reads a line, and leaves a quoted one as content (closing round 3, T1: the
 * regex captured the quote and nothing read it). The view blanks both kinds; readQuotedSubstitutions
 * reads the unquoted ones back.
 */
function readHeredocs(cmd) {
  const out = []
  const here = /<<-?\s*(['"]?)([A-Za-z_][A-Za-z0-9_]*)\1/g
  let hm
  while ((hm = here.exec(cmd)) !== null) {
    const tag = hm[2]
    const bodyStart = cmd.indexOf('\n', hm.index)
    if (bodyStart === -1) break
    const end = cmd.slice(bodyStart).search(new RegExp('\\n[ \\t]*' + tag + '[ \\t]*(?:\\n|$)'))
    const bodyEnd = end === -1 ? cmd.length : bodyStart + end
    out.push({ from: bodyStart + 1, to: bodyEnd, quoted: hm[1] !== '' })
    here.lastIndex = bodyEnd
  }
  return out
}

/**
 * Blank the CONTENTS of quoted strings and heredoc bodies, preserving length so offsets still line
 * up with the original. Copied from scratch-guard.js rather than required from it: a `require` of
 * a sibling kit's file is a literal the install-prefix ban refuses, and an adopter may not hold
 * that kit at all.
 */
function buildHeredocView(cmd) {
  const buildBlankedRun = (s, from, to) =>
    to <= from ? s : s.slice(0, from) + ' '.repeat(to - from) + s.slice(to)
  let view = cmd
  for (const h of readHeredocs(cmd)) view = buildBlankedRun(view, h.from, h.to)
  return view
}

/**
 * Index of the `)` that closes a `$(` opened just before `from`, or `to` when none does. Parens
 * count toward the depth only outside quotes, so `grep -c 'foo(' <file>` does not open one and
 * `: ')'` does not close one. Shared by the view and the walker (closing round 3, T4): the two
 * used to disagree on where a span ends, and the view's answer un-blanked a string's tail.
 */
function readSpanEnd(s, from, to) {
  let depth = 1
  let q = ''
  let i = from
  while (i < to) {
    const c = s[i]
    if (q) {
      if (c === '\\' && q === '"') i++
      else if (c === q) q = ''
    } else if (c === "'" || c === '"') q = c
    else if (c === '\\') i++
    else if (c === '(') depth++
    else if (c === ')' && --depth === 0) return i
    i++
  }
  return to
}

function buildCommandView(cmd) {
  // Heredoc bodies first, in their own helper because readQuotedSubstitutions needs the same
  // half: a body can hold anything, backticks in prose included, and a walker that read the
  // original text found a "run" inside a commit message this fold itself was writing.
  const view = buildHeredocView(cmd)

  let out = ''
  let i = 0
  while (i < view.length) {
    const ch = view[i]
    if (ch === "'" || ch === '"') {
      let j = i + 1
      while (j < view.length && view[j] !== ch) {
        if (ch === '"') {
          if (view[j] === '\\') j++
          // A `$( … )` or backtick span inside the string is skipped WHOLE, past its own closing
          // paren or backtick, so a double-quoted argument inside it cannot pair with this quote
          // and un-blank the string's tail (closing round 3, T4). The span is content here;
          // readQuotedSubstitutions reads it back as a command of its own.
          else if (view[j] === '$' && view[j + 1] === '(') j = readSpanEnd(view, j + 2, view.length)
          else if (view[j] === '`') { const e = view.indexOf('`', j + 1); j = e === -1 ? view.length : e }
        }
        j++
      }
      const close = j < view.length ? j : view.length
      out += ch + ' '.repeat(Math.max(0, close - i - 1)) + (j < view.length ? ch : '')
      i = close + 1
    } else if (ch === '\\') {
      // Outside quotes a backslash escapes the next character, the rule readQuotedSubstitutions
      // already applied (closing round 3, T7): read as a quote, `\"` opened a bogus string here
      // that swallowed the rest of the line, suite included.
      out += ch + (view[i + 1] || '')
      i += 2
    } else {
      out += ch
      i++
    }
  }
  return out
}

/**
 * The bodies of every `$( … )` and `` ` … ` `` span inside a DOUBLE-quoted string, read from the
 * original text. Bash runs those as commands — `printf '%s' "$(bash <suite>)"` runs the suite — and
 * the view above blanks them as content, which is right for the string and wrong for the span.
 * Closing review F7 kept the span unblanked IN the view instead; round 2 (R5, R6, R13) found that
 * a quoted argument inside the span was then read as a command, the string's tail after the span
 * became a segment of its own, and the backtick spelling stayed content. So each body is handed
 * back to scanDenyHits as a command of its own, the way row D5 hands back a `bash -c` body:
 * blanked, segmented and scanned by the same code. Single-quoted strings stay content throughout.
 *
 * An UNQUOTED heredoc body (`<<EOF`, `<<-EOF`) is walked the same way, as one double-quoted region
 * with no closing quote — bash substitutes inside it before the consumer reads a line — while a
 * `<<'EOF'` or `<<"EOF"` body stays content (closing round 3, T1; round 2's R13 control arm had
 * pinned the unquoted form as prose, which bash disagreed with).
 *
 * Under PowerShell (`tool`) the backtick inside double quotes is the ESCAPE character and opens
 * nothing: `` `$env: `` is the only way to write that prefix literally and `` `" `` the only way to
 * embed a quote (closing round 3, T3, observed as a live block of a commit message). The `$( … )`
 * branch stays, because that is a PowerShell subexpression. The view's quote pairing above is
 * bash's under both tools; only the walker reads the tool.
 */
function readQuotedSubstitutions(text, tool) {
  const ps = tool === 'PowerShell'
  const cmd = buildHeredocView(text)   // no body opens or closes a quote here; the unquoted ones are read below
  // readRegion walks s[from, to) as the INSIDE of a double-quoted string: the spans it holds, and
  // where it stopped — at a `"` only when `closes` is set, since a heredoc body has no closing quote.
  const readRegion = (s, from, to, closes) => {
    const spans = []
    let i = from
    while (i < to) {
      const c = s[i]
      if (c === '\\') i++
      else if (ps && c === '`') i++
      else if (closes && c === '"') return { spans, end: i }
      else if (c === '$' && s[i + 1] === '(') {
        const end = readSpanEnd(s, i + 2, to)
        spans.push(s.slice(i + 2, end))
        i = end
      } else if (c === '`') {
        const end = s.indexOf('`', i + 1)
        const stop = end === -1 || end > to ? to : end
        spans.push(s.slice(i + 1, stop))
        i = stop
      }
      i++
    }
    return { spans, end: to }
  }
  const out = []
  let q = ''
  let i = 0
  while (i < cmd.length) {
    const c = cmd[i]
    if (q) {
      if (c === "'") q = ''
    } else if (c === '"') {
      const r = readRegion(cmd, i + 1, cmd.length, true)
      out.push(...r.spans)
      i = r.end
    } else if (c === "'") q = "'"
    else if (c === '\\') i++
    i++
  }
  for (const h of readHeredocs(text)) {
    if (!h.quoted) out.push(...readRegion(text, h.from, h.to, false).spans)
  }
  return out
}

/**
 * Read the whitespace-delimited token starting at `from` in the ORIGINAL text, unquoted. Inside a
 * double-quoted run a `$( … )` or backtick span is one piece of the token, whatever quotes it holds
 * (closing round 3, T4): pairing the outer `"` with the first `"` inside the span split
 * `msg="$(printf "%s" "run bash <suite> next")"` into an assignment word and a launcher at head.
 * Bash's rule under both tools; the span itself is read back by readQuotedSubstitutions.
 * A word also ends before an unquoted `>` or `<` once it holds quoting, an empty pair included, or
 * anything but descriptor digits and operator characters, outside `${…}` (TOOL-aClearedLedger-11,
 * narrowed by TOOL-aClearedLedger-12 so a two-character operator is one word, and by
 * TOOL-aClearedLedger-14 so a quoted character is never part of an operator). The reader is shared,
 * so rows D2 to D4 see a glued redirection too. It returns `quotedAt`, the offset in the word where
 * its quoting opened, -1 for a word with none.
 */
function readTokenAt(cmd, from, stop) {
  let i = from
  while (i < stop && /\s/.test(cmd[i])) i++
  let out = ''
  let quote = ''
  let quotedAt = -1   // where in `out` the word's first quote opened; -1 for a word with none
  let brace = false   // inside a `${…}` — its braces are the token's, not grouping (round 2, R4)
  while (i < stop) {
    const ch = cmd[i]
    if (quote) {
      if (ch === quote) quote = ''
      else if (quote === '"' && ch === '$' && cmd[i + 1] === '(') {
        const e = readSpanEnd(cmd, i + 2, stop)
        out += cmd.slice(i, e + 1)
        i = e
      } else if (quote === '"' && ch === '`') {
        const e = cmd.indexOf('`', i + 1)
        const end = e === -1 || e >= stop ? stop - 1 : e
        out += cmd.slice(i, end + 1)
        i = end
      } else out += ch
    } else if (ch === "'" || ch === '"') {
      quote = ch
      if (quotedAt < 0) quotedAt = out.length
    } else if (ch === '{' && cmd[i - 1] === '$') {
      brace = true
      out += ch
    } else if (ch === '}' && brace) {
      brace = false
      out += ch
    } else if (/[\s;|&(){}`]/.test(ch)) {
      break
    } else if ((ch === '>' || ch === '<') && !brace && (quotedAt >= 0 || !/^\d*[<>]*$/.test(out))) {
      // A glued redirection ends the word (TOOL-aClearedLedger-11): `x.py --selftest>x.log` is the
      // flag and then a redirection word. While the word so far is unquoted descriptor digits and
      // operator characters, it is read on (TOOL-aClearedLedger-12): `>>`, `2>>` and `<<<` stay one
      // word, so REDIRECT_RE drops the operator with its target, glued or spaced. A word holding
      // quoting ends here, as bash ends it: `'&'>x.log` and `'>'>x.log` are an argument and then
      // a redirection (TOOL-aClearedLedger-14). An empty pair is quoting too: `"">x.log` is an empty
      // argument and then a redirection (TOOL-aClearedLedger-16).
      break
    } else {
      out += ch
    }
    i++
  }
  return { text: out, end: i, quotedAt }
}

/**
 * Every simple command's tokens, read from the ORIGINAL at the segment boundaries the VIEW locates.
 *
 * Separators are read in the view, where every quoted character is blank, so a `;` inside a commit
 * message is not one. Tokens are read from the original, so a quoted path still resolves. A segment
 * whose view is all blank while its text is not can only be a heredoc body — a quoted string keeps
 * its quote marks — and is skipped whole; without that the body of `python - <<EOF` would be read
 * as commands, which is exactly what the view exists to prevent.
 *
 * Each token array carries a parallel array `quotedAt` as a property, each word's quoting offset
 * from readTokenAt; a word that unquotes to empty is kept by that fact (TOOL-aClearedLedger-14).
 */
function scanSegments(cmd, view) {
  const out = []
  let s = 0
  const readSegment = (e) => {
    if (e <= s) return
    if (/\S/.test(cmd.slice(s, e)) && !/\S/.test(view.slice(s, e))) return
    const toks = []
    const quotedAt = []
    let at = s
    while (at < e) {
      const t = readTokenAt(cmd, at, e)
      if (t.end <= at) break
      if (t.text !== '' || t.quotedAt >= 0) { toks.push(t.text); quotedAt.push(t.quotedAt) }
      at = t.end
    }
    // `then`, `do` and `else` open a command position; drop them so the word after is the head.
    while (toks.length && /^(then|do|else)$/.test(toks[0])) { toks.shift(); quotedAt.shift() }
    toks.quotedAt = quotedAt
    if (toks.length) out.push(toks)
  }
  let brace = false   // `${…}` is one word, not a group (round 2, R4); readTokenAt agrees
  for (let i = 0; i < view.length; i++) {
    if (view[i] === '{' && view[i - 1] === '$') { brace = true; continue }
    if (view[i] === '}' && brace) { brace = false; continue }
    if (/[;|&(){}`\n]/.test(view[i])) {
      readSegment(i)
      s = i + 1
    }
  }
  readSegment(view.length)
  return out
}

// The PowerShell-native spellings too (closing review F8; round 2 R4): under the second tool this
// hook is wired on, `NAME=value cmd` is not valid syntax and the assignment that runs the flagged
// bar there is `$env:GATE_SELFTESTS=1; bash …` — with the drive name in any case, in the
// `${env:NAME}` brace form, and with spaces around the `=` (`$Env:NAME = value` is the documented
// spelling). F8 read the lowercase glued form only. readTokenAt already unquotes, so
// `$env:GATE_FULL=""` is OFF; the spaced form is read in scanDenyHits from three tokens.
const FLAG_RE = /^(?:\$\{?[Ee][Nn][Vv]:)?(GATE_FULL|GATE_SELFTESTS)\}?=(.*)$/
const PS_FLAG_NAME_RE = /^\$\{?[Ee][Nn][Vv]:(GATE_FULL|GATE_SELFTESTS)\}?$/
const PS_ENV_PREFIX_RE = /^\$\{?[Ee][Nn][Vv]:/
const ASSIGN_RE = /^[A-Za-z_][A-Za-z0-9_]*=/
// A `timeout` duration: a literal with its unit, a decimal (`1.5`), or a `$` expansion — `$T`,
// `${T}s`, `"$GATE_BOUND"` (unquoted by readTokenAt), which is the driver's own `run_bounded`
// spelling (closing round 3, T5: the literal alone left `timeout` as the head and the run walked).
const DURATION_RE = /^(?:\d+(?:\.\d+)?[smhd]?|\$.+)$/
const SHORT_OPT_RE = /^-[A-Za-z]+$/
const VERSION_OPT_RE = /^-\d+(?:\.\d+)?$/   // `py -3`, `py -3.12`: the launcher's version selector (closing round 3, T6)
// A redirection word: `>`, `>>`, `2>`, `&>`, `<`, `<<<`, bare or with its target glued (row D6).
const REDIRECT_RE = /^(?:\d*|&)(?:>>?|<{1,3})/

function resolveFileRow(tok) {
  if (/run-selftests\.sh$/.test(tok)) return { row: 'D2', what: 'runner', shape: 'the self-test runner' }
  if (/run-unattended-gates\.sh$/.test(tok)) return { row: 'D3', what: 'runner', shape: 'the self-test runner' }
  if (/\.test\.sh$/.test(tok) || /selftest\.py$/.test(tok)) return { row: 'D4', what: 'suite', shape: 'a self-test suite' }
  return null
}

/**
 * Rows D1 to D5 over every simple command. Command position is the head word after any of `env`,
 * `export`, `time`, `nohup`, `NAME=value` words, `timeout N`, and `bash`/`sh` with one short option;
 * row D5 re-enters once on the argument of `-c`. `{`, `time` and `nohup` were added by the corpus
 * measurement (spec rev-4): 38 runs sat among the near-misses of the grammar without them.
 *
 * `candidates`, when passed, collects row D6's candidates and leaves the return value alone: each
 * simple command whose resolved head carries no D2 to D4 row and whose words include one of
 * DIRECT_CHECK_WORDS pushes `{ words }`, `words` being EVERY word of the simple command, the
 * launcher words included, with redirections taken out (TOOL-aClearedLedger-11: the head the
 * grammar resolved is not what names the script, and a segment it left with no head, behind
 * `python -m` say, is a candidate too). A redirection is a word to scanSegments, so `> x.log` and
 * `2>` would otherwise be compared as arguments. A word holding quoting is a redirection only when
 * the text before its quoting starts with an operator REDIRECT_RE matches, so `'&'` and `2'>'x` are
 * words, and `2>"x.log"` and `>'>x.log'` are redirections (TOOL-aClearedLedger-15). Only a word with
 * no quoting can be a bare operator whose target is the next word. Both recursions hand the array on.
 */
function scanDenyHits(cmd, view, depth, tool, candidates) {
  depth = depth || 0
  const hits = []
  for (const toks of scanSegments(cmd, view)) {
    const readOnly = toks.some((t) => READ_ONLY_VERBS.includes(t))
    let k = 0
    let head = null
    while (k < toks.length) {
      const t = toks[k]
      const flag = FLAG_RE.exec(t)
      if (flag && flag[2] !== '') {
        hits.push({ row: 'D1', what: 'flag', shape: 'the flagged merge bar', token: t })
        k++
      } else if (flag && PS_ENV_PREFIX_RE.test(t)) {
        // `$Env:GATE_FULL= 1` (closing round 3, T2): PowerShell's assignment takes whitespace on
        // either side of the `=`, so an EMPTY value group under the `$env:` prefix is read forward
        // one token like the spaced forms below — a present non-empty next token is the flagged
        // bar; an empty quoted one or the end of the segment stays OFF. There is no glued-empty
        // OFF spelling to protect: `$Env:X=;` is a parse error under pwsh. Reading forward is
        // safe under Bash too, where a `$env`-prefixed word is never an assignment.
        const v = k + 1
        if (v < toks.length && toks[v] !== '') {
          hits.push({ row: 'D1', what: 'flag', shape: 'the flagged merge bar', token: t + toks[v] })
        }
        k = v + 1
      } else if (PS_FLAG_NAME_RE.test(t)) {
        // The SPACED PowerShell assignment (round 2, R4): `$Env:GATE_FULL = 1` arrives as three
        // tokens and `$Env:GATE_FULL =1` as two. A value token that is present and non-empty is
        // the flagged bar; `$Env:GATE_FULL = ""` reads its quoted empty token and is OFF like the
        // glued form. The bash spelling never splits at `=`, so this branch is PowerShell's only.
        let v = k + 1
        let value = ''
        if (v < toks.length && toks[v] === '=') { v++; value = v < toks.length ? toks[v] : '' }   // `NAME = value`
        else if (v < toks.length && /^=/.test(toks[v])) value = toks[v].slice(1)         // `NAME =value`
        else { k++; continue }                                                           // a bare name, no assignment
        if (value !== '') {
          hits.push({ row: 'D1', what: 'flag', shape: 'the flagged merge bar', token: t + '=' + value })
        }
        k = v + 1
      } else if (t === 'env' || t === 'export' || t === 'nohup' || ASSIGN_RE.test(t)) {
        k++
      } else if (t === 'stdbuf' || t === 'nice' || t === 'ionice' || t === 'time' || /\/time$/.test(t)) {
        // Prefix words that take options before the launcher (closing review F7): `stdbuf -oL -eL
        // bash <suite>`, `nice -n 10 bash <suite>`, `/usr/bin/time -f '%e' bash <suite>` — the
        // last found by the corpus walk this fold re-ran. Their `-x` options and the value after
        // a bare `-n`, `-c`, `-f` or `-o` are skipped.
        k++
        while (k < toks.length && /^-/.test(toks[k])) {
          if (/^-[ncfo]$/.test(toks[k]) && k + 1 < toks.length) k++
          k++
        }
      } else if (t === 'timeout' && k + 1 < toks.length && (DURATION_RE.test(toks[k + 1]) || /^-/.test(toks[k + 1]))) {
        // `timeout [-k DURATION] [-s SIG] [--foreground] DURATION cmd` (closing review F7): the
        // options and their values are skipped before the duration, so `-k` no longer makes
        // `timeout` the head and `timeout -k 5 120 bash <suite>` is the run it is. The long
        // spellings `--kill-after N` and `--signal SIG` take a value too (round 2, R14); every
        // other option GNU timeout has — `--foreground`, `--preserve-status`, `-v`, `--x=y` —
        // is a bare word the `-` test skips. The duration is DURATION_RE's: a literal, a decimal
        // or a `$` expansion (round 3, T5).
        k++
        while (k < toks.length && /^-/.test(toks[k])) {
          if (/^(-[ks]|--kill-after|--signal)$/.test(toks[k]) && k + 1 < toks.length) k++
          k++
        }
        if (k < toks.length && DURATION_RE.test(toks[k])) k++
      } else if (t === 'python' || t === 'py' || /^python3(\.\d+)?$/.test(t)) {
        // The launcher of a `selftest.py` suite (closing review F2), `py` and a versioned `python3.x`
        // among them (round 2, R12): `py` is the third candidate the kit's own resolver falls to, the
        // Windows launcher a node meets when the MS-Store `python3` stub shadows the real one. One
        // option is skipped the way bash's is — a short one, `py`'s version selector `-3`/`-3.12`,
        // or `-X` with its value glued or as the next word (round 3, T6); `-c` and `-m` carry code
        // or a module and never a suite file, so the segment is left alone rather than read as
        // shell — python code is not this predicate's.
        k++
        if (k < toks.length && (SHORT_OPT_RE.test(toks[k]) || VERSION_OPT_RE.test(toks[k]) || /^-X\S+$/.test(toks[k]))) {
          const opt = toks[k]
          if (opt === '-c' || opt === '-m') { head = null; break }
          k++
          if (opt === '-X') k++
        }
      } else if (t === 'bash' || t === 'sh') {
        k++
        if (k < toks.length && SHORT_OPT_RE.test(toks[k])) {
          const opt = toks[k]
          k++
          // `bash -n <file>` parses and executes nothing — the syntax check every suite author
          // types, 412 times in the corpus. Spec rev-5, after the wired hook denied this build's own.
          if (opt === '-n') { head = null; break }
          if (opt === '-c' && depth < MAX_NEST && k < toks.length) {
            const body = toks[k]
            for (const h of scanDenyHits(body, buildCommandView(body), depth + 1, tool, candidates)) {
              hits.push(Object.assign({}, h, { row: 'D5' }))
            }
            head = null
            k = toks.length
            break
          }
        }
      } else {
        head = t
        break
      }
    }
    const cls = head === null ? null : resolveFileRow(head)
    if (cls && !readOnly) hits.push(Object.assign({ token: head }, cls))
    if (candidates && !cls) {
      const words = []
      for (let j = 0; j < toks.length; j++) {
        const q = toks.quotedAt[j]
        const redir = REDIRECT_RE.exec(q < 0 ? toks[j] : toks[j].slice(0, q))   // the operator is unquoted text: a quoted character never joins it
        if (!redir) words.push(toks[j])
        else if (q < 0 && redir[0] === toks[j]) j++   // a bare unquoted operator: its target is the next word
      }
      if (words.some((w) => DIRECT_CHECK_WORDS.includes(w))) candidates.push({ words })
    }
  }
  // A `$( … )` or backtick span inside a double-quoted string, or inside an unquoted heredoc body,
  // is a command of its own (round 2, R5 R6 R13; round 3, T1), scanned the way row D5 scans a
  // `bash -c` body and keeping the row it finds. Each body is strictly shorter than the text
  // holding it, so the recursion needs no cap of its own and SPENDS none: it passes `depth`
  // through unchanged, so a `bash -c` inside a span is opened exactly as one outside it would be
  // (round 3, T8: `depth + 1` here spent row D5's cap and the nested `-c` was never read).
  for (const body of readQuotedSubstitutions(cmd, tool)) {
    for (const h of scanDenyHits(body, buildCommandView(body), depth, tool, candidates)) hits.push(h)
  }
  return hits
}

/**
 * The manifest's suites by cost, as `[{ name, ceiling, words }]`: every row of the JSON list whose
 * `chunk` is `selftests`, whose `argv` is a list of strings and whose `ceiling` is a number above
 * DIRECT_CHECK_BOUND. `words` is the argv from its first word carrying `/` on, with a leading
 * `{prefix}/` taken off that word. The shape is scratch-guard.js's `readGateLegs`, copied and not
 * required for the reason buildHeredocView records. A read or parse failure, and a value that is
 * no list, answer the empty list: the row is unarmed, never a throw.
 */
function readSuiteLegs(file) {
  let rows
  try {
    rows = JSON.parse(fs.readFileSync(file, 'utf8'))
  } catch {
    return []
  }
  if (!Array.isArray(rows)) return []
  const legs = []
  for (const g of rows) {
    if (!g || g.chunk !== 'selftests' || !Array.isArray(g.argv) || !g.argv.every((w) => typeof w === 'string')) continue
    if (typeof g.ceiling !== 'number' || !(g.ceiling > DIRECT_CHECK_BOUND)) continue
    const at = g.argv.findIndex((w) => w.includes('/'))
    if (at < 0) continue
    const words = g.argv.slice(at)
    words[0] = words[0].replace(/^\{prefix\}\//, '')
    legs.push({ name: String(g.name), ceiling: g.ceiling, words })
  }
  return legs
}

/**
 * Row D6's match: the first leg the candidate spells, or null (TOOL-aClearedLedger-11). Every word
 * of the candidate is tried as the script word, in order, and the spelling is that word and every
 * word after it. Three rules, all of which hold, `at` being the place of the leg's first
 * DIRECT_CHECK_WORDS member:
 *   1  the word, folded (`\` to `/`, lower case, leading `./` segments off) and not empty, equals
 *      the leg's script, ends with `/` and that script, or is a trailing path of it after a `/`;
 *   2  the spelling has no more words than the leg, reaches `at`, and each word up to `at` equals
 *      the leg's at that place;
 *   3  each word after `at` equals the leg's, except at an option's VALUE — a leg word that does
 *      not open with `-` behind one that does — where any word holds.
 * So a shorter spelling that still runs the checks, and one with a changed option value, is a hit;
 * a longer one or one with another option name — a case name, a read-only verb — is a miss. A leg
 * whose argv carries no such member never matches: rows D2 to D4 own the word shapes.
 */
function checkSuiteLeg(candidate, legs) {
  const words = candidate.words
  for (let s = 0; s < words.length; s++) {
    const word = words[s].replace(/\\/g, '/').toLowerCase().replace(/^(?:\.\/+)+/, '')
    if (word === '') continue
    const n = words.length - s
    for (const leg of legs) {
      const script = leg.words[0].toLowerCase()
      if (word !== script && !word.endsWith('/' + script) && !script.endsWith('/' + word)) continue
      const at = leg.words.findIndex((w, i) => i > 0 && DIRECT_CHECK_WORDS.includes(w))
      if (at < 1 || n > leg.words.length || n < at + 1) continue
      let holds = true
      for (let i = 1; i < n && holds; i++) {
        const want = leg.words[i]
        const value = i > at && !want.startsWith('-') && leg.words[i - 1].startsWith('-')
        holds = value || words[s + i] === want
      }
      if (holds) return leg
    }
  }
  return null
}

/** `ref: refs/heads/x` → the ref; a bare sha → null, because a detached HEAD keys nothing. */
function readHeadRef(gitDir) {
  let text
  try {
    text = fs.readFileSync(path.join(gitDir, 'HEAD'), 'utf8')
  } catch {
    return null
  }
  const m = /^ref:\s*(\S+)/.exec(text.trim())
  return m ? m[1] : null
}

/**
 * Walk up from `cwd` to the nearest `.git`. A worktree's `.git` is a FILE holding `gitdir: <path>`
 * and THAT directory's HEAD is the worktree's branch — the common dir's HEAD is the primary tree's,
 * which is the one difference from agent-cap's `gitCommonDir`.
 */
function resolveRepoRoot(cwd) {
  let dir = path.resolve(cwd)
  for (let i = 0; i < 64; i++) {
    const g = path.join(dir, '.git')
    let st = null
    try { st = fs.statSync(g) } catch { st = null }
    if (st) {
      let gitDir = g
      if (!st.isDirectory()) {
        let m
        try { m = /gitdir:\s*(.+)/.exec(fs.readFileSync(g, 'utf8')) } catch { return null }
        if (!m) return null
        gitDir = path.resolve(dir, m[1].trim())
      }
      const headRef = readHeadRef(gitDir)
      return headRef ? { root: dir, headRef } : null
    }
    const up = path.dirname(dir)
    if (up === dir) return null
    dir = up
  }
  return null
}

/** `MEMORY_ROOT` from the conf beside `.git`; no conf keys nothing, an absent key means `memory`. */
function readMemoryRoot(root) {
  let text
  try {
    text = fs.readFileSync(path.join(root, CONF_BASENAME), 'utf8')
  } catch {
    return null
  }
  // The driver SOURCES this file; this is a second reader, so every legal shell spelling of the
  // line has to read the same here — a trailing comment or a quoted value must not turn into a
  // path that resolves nowhere and switch the hook off silently.
  let value = 'memory'
  for (const line of text.split(/\r?\n/)) {
    const m = new RegExp('^(?:export\\s+)?' + CONF_KEY + '=(.*)$').exec(line)
    if (m) value = m[1].replace(/\s+#.*$/, '').trim().replace(/^["']|["']$/g, '')
  }
  // A value that could escape the root is not a memory root; fail open rather than read outside it.
  if (!value || path.isAbsolute(value) || value.split(/[\\/]/).includes('..')) return null
  return value
}

/**
 * Every run-state record whose branch fact equals `ref`: `run-branch:` first, `branch-ref:` for a
 * record written before that fact existed. A record with neither, or with no phase, keys nothing.
 */
function resolveRunPhase(root, memoryRoot, ref) {
  const buildsDir = path.join(root, memoryRoot, 'builds')
  let slugs
  try { slugs = fs.readdirSync(buildsDir) } catch { return [] }
  const matched = []
  for (const slug of slugs) {
    let text
    try { text = fs.readFileSync(path.join(buildsDir, slug, RECORD_BASENAME), 'utf8') } catch { continue }
    // TOOL-aRepatriatedFork-6, closing review round 2 M1: the `## Run facts` section when the record
    // carries the heading, heading to next `## ` - run-lease.js's slice and the driver's `fact`
    // scope. Read whole, a `phase: LANDED` above the heading filtered a live record out through
    // PHASES_ALLOW while the driver still read BUILDING, and a CR-split park row under `## Parked`
    // (JS reads a CR as a line end under `m`) answered `run-branch` ahead of the real `branch-ref`.
    // A record with NO heading is still read whole, on purpose: the suite's AC4 keys one.
    let region = text
    const h = /^## Run facts/m.exec(text)
    if (h) {
      const rest = text.slice(h.index + h[0].length)
      const j = rest.search(/^## /m)
      region = j < 0 ? rest : rest.slice(0, j)
    }
    const readFact = (key) => {
      const m = new RegExp('^' + key + ': (.*)$', 'm').exec(region)
      return m ? m[1].trim() : ''
    }
    const branch = readFact('run-branch') || readFact('branch-ref')
    const phase = readFact('phase')
    if (!branch || !phase || branch !== ref) continue
    matched.push({ slug, phase, record: [memoryRoot, 'builds', slug, RECORD_BASENAME].join('/') })
  }
  return matched
}

/** The whole decision: hits and row D6's candidates first, the filesystem only on either, and the
 * manifest only once a live run is found. Null means allow. `tool` is the payload's `tool_name`,
 * read by the walker for the one rule that differs between the two wired tools (closing round 3, T3). */
function checkCommand(cmd, cwd, tool) {
  const candidates = []
  const hits = scanDenyHits(cmd, buildCommandView(cmd), 0, tool, candidates)
  if (hits.length === 0 && candidates.length === 0) return null
  const repo = resolveRepoRoot(cwd)
  if (!repo) return null
  const memoryRoot = readMemoryRoot(repo.root)
  if (!memoryRoot) return null
  const live = resolveRunPhase(repo.root, memoryRoot, repo.headRef).filter((r) => !PHASES_ALLOW.includes(r.phase))
  if (live.length === 0) return null
  if (candidates.length) {
    const legs = readSuiteLegs(path.join(__dirname, '..', MANIFEST_BASENAME))
    for (const c of candidates) {
      const leg = checkSuiteLeg(c, legs)
      if (leg) {
        hits.push({
          row: 'D6', what: 'suite', shape: 'a self-test suite',
          token: `${leg.words[0]} (the gate manifest's leg "${leg.name}", ceiling ${leg.ceiling} s)`,
        })
      }
    }
  }
  if (hits.length === 0) return null
  return { hits, live }
}

function renderDeny(hits, live) {
  const shapes = [...new Set(hits.map((h) => h.shape))].join(' and ')
  const where = live.map((r) => `${r.phase} (${r.record})`).join(' and ')
  const lines = hits.map((h) => `  ${h.what}: ${h.token}`).join('\n')
  return (
    `BLOCKED by gate-guard: this command runs ${shapes} while the unattended run on this\n` +
    `branch is at ${where}, which is before ${PHASES_ALLOW[0]}.\n\n` +
    lines +
    '\n\nInside a build pass a unit is observed by the direct check its spec names, in seconds. The\n' +
    `flagged bar and the self-test suites run once, at ${PHASES_ALLOW[0]}, by the main loop. A quoted mention\n` +
    'of the file is not a hit.\n'
  )
}

/**
 * Each question of an `AskUserQuestion` input as `{question, labels}`, every value cut to
 * ASK_QUOTE_MAX characters with its control characters removed. An input of another shape yields
 * one `(no question text)` entry rather than a throw: the deny must still name the park route.
 */
function extractAskQuestions(input) {
  const renderAskQuote = (v) => String(v).replace(/[\u0000-\u001f\u007f-\u009f]/g, '').slice(0, ASK_QUOTE_MAX)
  const list = input && Array.isArray(input.questions) ? input.questions : []
  const out = []
  for (const q of list) {
    if (!q || typeof q !== 'object') continue
    const text = typeof q.question === 'string' && q.question.trim() ? renderAskQuote(q.question) : '(no question text)'
    const opts = Array.isArray(q.options) ? q.options : []
    const labels = opts.filter((o) => o && typeof o.label === 'string').map((o) => renderAskQuote(o.label))
    out.push({ question: text, labels })
  }
  return out.length ? out : [{ question: '(no question text)', labels: [] }]
}

/**
 * The question arm's decision: the leases `run-lease.js` binds to the payload's `session_id` whose
 * phase is live — non-empty, not `absent`, not in PHASES_TERMINAL — and whose driver `--liveness`,
 * read through stop-guard.js's own reader, is not TERMINAL (TOOL-aOrientedCast-24 S3). Each lease
 * left carries `verdict`, empty when the liveness could not be read, and then its recorded phase
 * stands. Null means allow, and every other unreadable input answers null.
 */
function checkAsk(data) {
  const lease = require(path.join(__dirname, 'run-lease.js'))
  const repo = lease.resolveRepo(data.cwd || process.cwd())
  if (!repo) return null
  const memoryRoot = lease.readMemoryRoot(repo.root)
  if (!memoryRoot) return null
  const live = []
  for (const l of lease.resolveLease(repo.root, memoryRoot, data.session_id)) {
    if (!l.phase || l.phase === 'absent' || PHASES_TERMINAL.includes(l.phase)) continue
    // Its own try: a load failure, a throw or a bad read is an unreadable liveness, never an allow.
    let liveness = null
    try {
      const guard = require(path.join(__dirname, 'stop-guard.js'))
      const run = guard.runLiveness(__dirname, repo.root, l.slug)
      liveness = run.ok ? guard.parseLiveness(run.stdout) : null
    } catch {
      liveness = null
    }
    if (liveness && liveness.verdict === 'TERMINAL') continue
    live.push(Object.assign({}, l, { verdict: liveness ? liveness.verdict : '' }))
  }
  if (live.length === 0) return null
  return { live, questions: extractAskQuestions(data.tool_input) }
}

/**
 * The deny text: the first live lease with its liveness, the park route — or, at FINISHED-UNSTAMPED,
 * the landing stamp, as stop-guard's `landing-unstamped` reason says — and each question with its
 * option labels.
 */
function renderAskDeny(live, questions) {
  const r = live[0]
  const asked = questions
    .map((q) => `  - ${q.question} — options: ${q.labels.length ? q.labels.join(', ') : '(none)'}`)
    .join('\n')
  const head = r.verdict
    ? `BLOCKED by gate-guard: this session holds the lease of the unattended run ${r.slug}, at ${r.phase}, liveness ${r.verdict} (${r.record}).\n`
    : `BLOCKED by gate-guard: this session holds the lease of the unattended run ${r.slug}, at ${r.phase} (${r.record}); its liveness could not be read, so the recorded phase stands.\n`
  const route = r.verdict === 'FINISHED-UNSTAMPED'
    ? 'Its witness is already on the default branch, so the run is finished and unstamped. The one act\n' +
      'left is the landing stamp, not a question:\n\n' +
      `  unattended.sh --landed ${r.slug}\n\n`
    : 'An unattended run never asks: nobody is there to answer, so the question stalls the run until\n' +
      'the owner comes back. A question the protocol lets you decide is decided: take the option that\n' +
      'makes no measured observable worse, and record why. One no delegated resolver can take is parked,\n' +
      'and the run goes on to its next READY unit or holds:\n\n' +
      `  unattended.sh --park ${r.slug} --item "<the question, and its options>" --reason "<why no resolver the mandate delegates exists>"\n\n`
  return head + route + 'The question this call asked:\n' + asked + '\n'
}

function main() {
  let data
  try {
    data = JSON.parse(readStdin())
  } catch {
    process.exit(0)
  }
  if (data && data.tool_name === ASK_TOOL) {
    // Dispatched before the TOOLS test (TOOL-aOrientedCast-22). Wrapped and failing open like the
    // bar arm below: a throw here must not exit 1 on a question that was probably fine.
    let ask
    try {
      ask = checkAsk(data)
    } catch {
      process.exit(0)
    }
    if (!ask) process.exit(0)
    process.stderr.write(renderAskDeny(ask.live, ask.questions))
    process.exit(2)
  }
  if (!data || !TOOLS.includes(data.tool_name)) process.exit(0)
  const cmd = (data.tool_input && data.tool_input.command) || ''
  if (!cmd) process.exit(0)
  // Wrapped because a hygiene guard that THROWS is worse than one that misses: an uncaught error
  // exits 1 and surfaces noise on a command that was probably fine. Fail open.
  let verdict
  try {
    verdict = checkCommand(String(cmd), data.cwd || process.cwd(), data.tool_name)
  } catch {
    process.exit(0)
  }
  if (!verdict) process.exit(0)
  process.stderr.write(renderDeny(verdict.hits, verdict.live))
  process.exit(2)
}

if (require.main === module) main()
module.exports = {
  readStdin, readHeredocs, buildHeredocView, readSpanEnd, buildCommandView, readQuotedSubstitutions,
  scanSegments, scanDenyHits, readSuiteLegs, checkSuiteLeg,
  resolveRepoRoot, readHeadRef, readMemoryRoot,
  resolveRunPhase, checkCommand, renderDeny, extractAskQuestions, checkAsk, renderAskDeny, main,
  DIRECT_CHECK_BOUND, DIRECT_CHECK_WORDS, MANIFEST_BASENAME,
  PHASES_ALLOW, PHASES_TERMINAL, ASK_TOOL, ASK_QUOTE_MAX, READ_ONLY_VERBS, TOOLS, KIT_GATE_GUARD_VERSION,
}
