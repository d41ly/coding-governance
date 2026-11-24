#!/usr/bin/env node
/**
 * spawn-guard — the roles kit's PreToolUse guard on the `Workflow` and `Agent` tool calls
 * (TOOL-dBoundRoles-25, the night pass two's NT-27). It holds every rule the hooks kit's retired
 * agent limit hook still ran when it retired: rule 6, the spawn guard and harness admission, with admission held to the
 * landed blob (S3); rule 8, the effort level; rule 7, the settings in force (brief D4); and the spec-audit
 * opt-in pack's presence, in that order, after refusing every `--only=` argument. Each rule moved with its
 * predicate and its deny text, the prefix `BLOCKED by spawn-guard:` aside.
 *
 * THE AGENT LIMIT IS NOT THIS FILE'S (TOOL-dGroundRules-10). How many agents run at once is the policy
 * key `runtime.agents-in-flight`, which the policy kit renders into the harness's own two concurrency
 * settings in `.claude/settings.json` (`policy.py settings --write`). What a call-time check CAN see is the
 * settings files the harness started from, and RULE 7 holds them to the landed limit.
 *
 * THE HOOKS KIT'S READERS. The role index readers, the card reader, the fence walker, the marker reader, the
 * args reader, the slug walk and the policy helper's locator are `<prefix>/hooks/scratch-guard.js`'s exports,
 * found through this file's own `resolveKitDir` port (a receipt row, then `<here>/hooks/` and
 * `<here>/../hooks/`), the edge the roles kit's `requires_if` row declares (§8 F7). A guard that cannot load
 * them cannot read, and refuses every `Workflow` and `Agent` call, naming the hooks kit and the owner.
 *
 * RULE 6 (TOOL-aOrientedCast-7) — every agent prompt is a rendered handoff. Armed by
 * `.claude/roles.json` at the checkout root of the payload `cwd`, else of `CLAUDE_PROJECT_DIR`
 * (TOOL-aOrientedCast-14; neither resolving adds no rule, with one stderr line when
 * `CLAUDE_PROJECT_DIR` is set), read through the hooks kit's `resolveRoleRoot` and `loadRoleIndex`:
 * absent adds no rule, except in a governed tree, one whose `.claude/agents/` keeps a rendered role
 * agent (the hooks kit's `checkRoleGoverned`), where it refuses both tools naming the re-render
 * (TOOL-dBoundRoles-6 S3); broken refuses both tools; no `agent`-true role refuses every `Agent` call, and
 * an empty `harnesses` list every `Workflow` call, as UNARMED. An `Agent` call is admitted only when
 * its `subagent_type` is an `agent`-true role and its `prompt` is, line endings folded and its ends
 * trimmed, exactly one `gov:handoff` marker line naming that role, blank lines, and the `## Task`
 * section of the file the marker's `path` names under `builds/<build>/prompts/`, that file holding the
 * same single marker and a section whose SHA-256 prefix is the marker's `task-sha` and whose walk ends
 * outside every fence (TOOL-dBoundRoles-38 S5: a marker or fact line inside a fence is handed content,
 * counted and re-cut by no step, every line read through the hooks kit's `readUnfencedLines`), no typed
 * input's `### input:<name>` block holding a fact, marker or `Framed by:` line, fenced or not, or leaving a
 * fence open (TOOL-dBoundRoles-46 S2: a typed value is authored text, `TYPED_INPUTS`; read in the prompt and in the
 * file before either's markers are counted, TOOL-dBoundRoles-58 S25), every block opening
 * outside a fence and each handed block's content inside its own (TOOL-dBoundRoles-48 S3, `checkBlockFences`: an
 * unfenced fact line is the line two below an unfenced `### ` heading, the pair's next non-blank line opens its
 * fence, and only blank lines, or after the last one the envelope closer naming the marker's path, follow the
 * fence's closer up to the next unfenced heading), the marker's
 * `role-sha` the one the index holds for that role, the hash of the role text its agent type was
 * rendered from (TOOL-dBoundRoles-6 S6: an index holding none refuses naming the index's re-render, a
 * differing one naming both values and the handoff's re-render), every `gov:fact` line of the section
 * holding a `blob:` or `record:` key whose source, read now, still has the blob it was cut at
 * (TOOL-dBoundRoles-13 S4: `card/<sid>` read through the hooks kit's `readCard`, any other key from the
 * checkout root; a moved or vanished source refuses naming the key, both blobs and the re-render; a
 * `cmd:` key rides the task-sha and is not re-run; a handoff carrying no fact line re-derives nothing), a
 * marker whose `item=` is a tag binding its work order to this session (TOOL-dBoundRoles-3 S5, the stand-in
 * binding record until dWellOiledMachine's: the payload session's card, read through the hooks kit's `readCard`,
 * must route the marker's `unit=` among its `## route` units, read through `extractRouteUnits`; a refusal
 * names the unit and the card, `readCard`'s `shown` where no card reads; `item=-` or none is not judged), and its
 * `description`, ends trimmed, the name the renderer prints on stderr: `<build> · <unit> · <workflow>`
 * from the marker and the index's `workflow` for that role, the unit part left out for a `-` unit
 * (TOOL-aOrientedCast-27). That step stops a stale or freeform name, never a forged one. A `Workflow`
 * call is admitted only by a `scriptPath` listed in `harnesses`, with `args.roles` a non-empty object
 * whose every value is an `agent`-true role. A throw inside it refuses. An `Agent` call reads the policy
 * key `prompts.author` once (TOOL-dBoundRoles-10 S3, `resolvePromptsAuthor`), and every rule-6 refusal of
 * one ends with a line naming the key, the value in force and the remedy; no policy kit beside this hook
 * reads it as unarmed, and the check is the rendered-handoff check alone then and under
 * `requesting-worker-rendered`. Under `prompt-writer` a spawn of any role but `gov-prompt-writer`, once every
 * step above admits it, is admitted only when its task carries exactly one `### framing:job` block and exactly
 * one `Framed by: <path> task-sha=<12hex>` line inside it, outside every fence, the path a file under
 * `builds/<build>/prompts/` holding exactly one marker, of role `gov-prompt-writer` and that task-sha
 * (TOOL-dBoundRoles-4 S4, `checkFraming`); the refusal names the three-call route: render the prompt writer with
 * `--for`, spawn it, render the destination with `--framed-by`.
 * CEILING, said rather than implied: it stops forgetting, not evasion. A hook-less or `--bare` run,
 * the agents a running harness spawns through its own `agent()`, a nested harness call the text scan cannot
 * see (NESTED CEILING below), a session-to-session message, a self-consistent hand-written prompt file whose
 * marker copies the index's `role-sha`, and an index edited by shell, which the write gate's step 5a refuses
 * only to a tool write, all pass it.
 *
 * RULE 8 (TOOL-aGuardedEffort-1) — the level a call runs at is the one the effort policy gives its
 * model. Armed by the index's `effort` key, which the roles kit's renderer writes with every level
 * resolved; an index without it adds no rule and prints nothing. On a call rule 6 admitted, the model
 * is an `Agent` call's own `model`, else the `message.model` of the last main-chain assistant entry of
 * the payload's `transcript_path`, read whole, `<synthetic>` skipped. Its profile is the one whose
 * `match` holds a word of the id, else the default tables. An `Agent` call is refused unless its
 * `effort`, or with none its agent type's level, is the level that table gives its role. A `Workflow`
 * call is refused unless, for at least one workflow its harness runs, every stage key's level is the
 * table's. The stage level is the `args.efforts` value, or with none the level of the agent type the
 * call's `roles` names for the stage, and a stage neither names counts as differing
 * (TOOL-aGuardedEffort-2). A workflow's stage keys are those the index's `unset` and the matched
 * table's `stages` both hold for it. A refusal names
 * the role or stage, both levels, the model and where it was read, and the `handoff.py role-efforts`
 * or `stage-efforts` call that prints the right value. A level it cannot check is admitted with one
 * stderr line saying why: no `transcript_path`, an unreadable transcript, no entry naming a model, a
 * model two profiles match, a harness whose workflows hold no stage key, and an `Agent` call where
 * `CLAUDE_CODE_EFFORT_LEVEL` is set, since that session's tool offers no `effort`. A throw inside it,
 * tables that disagree on a stage key among them, refuses, naming a re-render.
 * WHAT IT DOES NOT CHECK: the agents a running harness spawns through its own `agent()`; the
 * `committer` and `probe` stages, which no `stages` table keys; which workflow a call to a harness
 * serving two runs, so a call right for one is admitted for both; a configured default subagent
 * model, and an effort ceiling in settings, which change what an agent runs at and are read by no
 * hook; a forged transcript and a hand-edited index.
 *
 * RULE 7 (TOOL-dGroundRules-10) — the settings in force. With the policy kit's `policy-mirror.js` found
 * through `resolveKitDir`, the receipt's row and then the sibling probes, every `Agent` and `Workflow`
 * call reads the landed limit through `readPolicy`, then every settings layer `readSettingsLayers` reads at the payload `cwd`'s
 * checkout root, and refuses when no layer sets a harness variable, or any layer that sets one holds
 * a value that is not a positive integer, or is above the limit (TOOL-dGroundRules-61). No policy kit found adds
 * no rule; a `cwd` in no checkout refuses, naming it (TOOL-dGroundRules-21 S38). A throw inside it refuses.
 * The limit is landed; the helper that reads it is not.
 * Its location rests on the working-tree receipt, so a forged row chooses the code this rule runs
 * (TOOL-dFairHearing-48 F1).
 *
 * ADMISSION HELD TO THE LANDED BLOB (TOOL-dBoundRoles-25 S3). A `Workflow` call whose `scriptPath` matched a
 * declared harness is admitted only where that file's working-tree blob id, `git hash-object` with the
 * repository's clean filters, equals its blob id at the landed revision the policy kit's `readLandedRevision`
 * names; absent there it is refused as not landed. No policy kit, or a refusal from it, refuses the call naming
 * the owner. It runs after the path match and before the `args.roles` checks: two git calls per file held.
 * An uncommitted edit and a committed but unlanded one are refused alike (§8 F2).
 * Every declared harness the admitted script nests through its own `workflow({ scriptPath: '<path>' })` call, and
 * every one those nest, is held the same way on every call, whatever the `args` (TOOL-dBoundRoles-88,
 * `checkHarnessClosure`): the refusal names the callee and the harness that runs it, and a nested call naming no
 * quoted declared harness refuses. So a swap to the landed bytes covers every nested harness for the whole call,
 * since a nested one is loaded when the script reaches it.
 * NESTED CEILING: the scan reads text, not JavaScript. It does not see a nested call not spelled `workflow(`, that
 * name bound to another among them; one on a line opening `//` that a template literal or a block comment spans; or
 * a second `scriptPath` key, or a spread, after the first in the same literal. Each needs a landed harness that hides
 * its call, and the bar read that harness. A block comment spelling `workflow(`, or a comment between the parenthesis
 * and the object, refuses rather than hides. A nested file edited after admission and before its call loads is not
 * compared again.
 *
 * Wiring (per project): run `python <prefix>/settings-merge.py` (idempotent), whose default fragment is this
 * kit's `spawn-guard.fragment.json`; or merge it by hand:
 *   "hooks": { "PreToolUse": [ { "matcher": "Workflow|Agent",
 *     "hooks": [ { "type": "command",
 *       "command": "node \"${CLAUDE_PROJECT_DIR}/<path>/spawn-guard.js\"" } ] } ] }
 * The matcher is a LIST OF EXACT STRINGS separated by `|`, in ONE group — not a regular expression.
 * main() exits 0 on any other tool_name. Blocks via exit 2 + stderr (version-robust; no JSON-schema dependency).
 */
'use strict'

// The hooks kit's `scratch-guard.js`, loaded once through `resolveKitDir`; a throw where it does not resolve,
// which `main()` turns into a refusal of the call (§4 "Disposition": a guard that cannot read does not admit).
function loadScratchGuard() {
  if (!loadScratchGuard.at) {
    const path = require('path')
    loadScratchGuard.at = require(path.join(resolveKitDir('hooks', 'scratch-guard.js', __dirname), 'scratch-guard.js'))
  }
  return loadScratchGuard.at
}

function readStdin() {
  try {
    return require('fs').readFileSync(0, 'utf8')
  } catch {
    return ''
  }
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


// RULE 6 (TOOL-aOrientedCast-7) — every agent prompt is a rendered handoff. The marker line is this
// kit's renderer's interface, read here through the hooks kit's `extractHandoffMarker` and never
// written; the renderer is named by its bare file name in every message.
const HANDOFF_MARK = 'gov:handoff'

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

// TOOL-dBoundRoles-13 S4 - a handed fact's line, the roles kit's `FACT_RE` spelled again with the same
// named groups, since a kit imports no sibling kit: the key `derive_fact_key` cut and the class
// `derive_fact_class` gave it, written atop each `reads` block of the `## Task` section.
const FACT_RE = /^<!-- gov:fact key=(?<key>\S+) class=(?<class>witnessed|decided|claimed) -->$/
const FACT_SOURCE_RE = /^(?<form>blob|record):(?<ref>.+)@(?<sha>[0-9a-f]{12})(?::[0-9]+-[0-9]+)?$/
// TOOL-dBoundRoles-46 S1 - the typed inputs: `handoff.py`'s `INPUT_NAMES` less its `PATH_INPUTS`, which this
// set equals, spelled again since a kit imports no sibling kit. A typed value is authored text, not handed
// content, so its block is held at the spawn to the line rule the renderer applies (`checkTypedBlocks`).
const TYPED_INPUTS = ['question', 'diff']

// TOOL-dBoundRoles-58 S16 - THE ONE BLOCK READER of a task section, built on the sibling's `readUnfencedLines`: each
// unfenced `### ` line opens a block, so a heading quoted inside a fence opens none. One object per block, in order:
// `heading`, the text after the hashes; `input`, the <name> of an `input:<name>` heading, else null; `first` and
// `last`, its line range, 1-based in the section, ending above the next unfenced `### ` line; and `fact`, the line of
// its own fact line, an unfenced `FACT_RE` line two below the heading, else null. Every carriage return is dropped.
function readTaskBlocks(section) {
  const lines = String(section).replace(/\r/g, '').split('\n')
  const blocks = []
  for (const [n, line] of loadScratchGuard().readUnfencedLines(lines.join('\n'))) {
    const at = blocks[blocks.length - 1]
    if (line === null) continue
    if (line.startsWith('### ')) {
      if (at) at.last = n - 1
      const heading = line.slice(4).trim()
      blocks.push({ heading, input: (/^input:(\S+)$/.exec(heading) || [])[1] || null, first: n, last: lines.length, fact: null })
    } else if (at && n === at.first + 2 && FACT_RE.test(line)) at.fact = n
  }
  return blocks
}

// TOOL-dBoundRoles-46 S2 - a typed block held to the authored-line rule. In each block `readTaskBlocks` yields whose
// `input` is in TYPED_INPUTS, every line after the block's own fact line is read, inside a fence or out: a `FACT_RE`
// line, a `HANDOFF_MARK_RE` line or a `Framed by:` line refuses, and so does a block whose own walk by the sibling's
// `readUnfencedLines` ends on its open-fence yield. That walk stops at the block's first `### ` line, which only a
// fence the block opened can hold: the renderer refuses one in a typed value, fenced or not, so it is the next
// block's heading swallowed. `lead` is the count of `where`'s lines before the section, so each refusal names the
// line there. null to admit, else the refusal naming the block and the line.
function checkTypedBlocks(section, lead, where) {
  const sg = loadScratchGuard()
  const lines = String(section).replace(/\r/g, '').split('\n')
  const remedy = 'a typed input\'s block is authored text, so it may hold no fact, marker or `Framed by:` line and must close every fence it opens; correct the value and re-render with handoff.py render.'
  for (const b of readTaskBlocks(section)) {
    if (!TYPED_INPUTS.includes(b.input)) continue
    for (let n = (b.fact || b.first) + 1; n <= b.last; n++) {
      const line = lines[n - 1]
      if (FACT_RE.test(line) || sg.HANDOFF_MARK_RE.test(line) || /^Framed by:/.test(line)) {
        return `input:${b.input}: line ${lead + n} of ${where} reads ${JSON.stringify(line.slice(0, 120))}, an executor line inside a typed block; ${remedy}`
      }
    }
    const body = lines.slice(b.first, b.last)
    const held = body.findIndex((l) => /^### /.test(l))
    for (const [n, line] of sg.readUnfencedLines(body.slice(0, held < 0 ? body.length : held).join('\n'))) {
      if (line === null) return `input:${b.input}: the block leaves a fence opened at line ${lead + b.first + n} of ${where} unclosed; ${remedy}`
    }
  }
  return null
}

// The count of `text`'s lines, CRLF folded, before its task section `section`.
function readSectionLead(text, section) {
  const t = String(text).replace(/\r\n/g, '\n')
  return t.slice(0, t.length - section.length).split('\n').length - 1
}

// TOOL-dBoundRoles-48 S3 - every block opens outside a fence, and a handed block's content lies inside its own.
// The section is walked by the sibling's `readUnfencedLines` and its blocks read by `readTaskBlocks`. An unfenced
// `FACT_RE` line that is no block's own fact line refuses; a block holding one is a handed block unless its
// heading names a typed input (`TYPED_INPUTS`), and a handed block refuses when its next non-blank line is not a
// fence opener, when a line up to that fence's closer is read outside it, or when anything but blank lines sits
// between that closer and the next unfenced heading. After the last handed block the one other line admitted is
// the task envelope's closer `[/<path>]`, `path` the marker's own, as the section's last non-blank line (§8 F4).
// `lead` is the count of the file's lines before the section, so each refusal names the line of the file. null to
// admit, else the refusal naming the block and the line.
function checkBlockFences(section, lead, docPath) {
  const sg = loadScratchGuard()
  const lines = String(section).split('\n').map((l) => l.replace(/\r/g, ''))
  const read = new Map()
  for (const [n, line] of sg.readUnfencedLines(lines.join('\n'))) if (line !== null) read.set(n, line)
  const remedy = 'every block of the task section opens outside a fence and a handed block\'s content lies inside its own; correct the value that moved the fence and re-render with handoff.py render.'
  const blocks = readTaskBlocks(section)
  for (const [n, line] of read) {
    if (!FACT_RE.test(line) || blocks.some((b) => b.fact === n)) continue
    const at = blocks.filter((b) => b.first < n).pop()
    return `${at ? at.heading : 'opening'}: line ${lead + n} of the file reads a fact line no unfenced \`### \` heading stands two lines above, so it would stand as an executor fact; ${remedy}`
  }
  const pairs = blocks.filter((b) => b.fact !== null)
  const last = pairs[pairs.length - 1]
  for (const b of pairs) {
    const name = b.heading
    if (TYPED_INPUTS.includes(b.input)) continue
    let k = b.fact + 1
    while (k <= lines.length && lines[k - 1].trim() === '') k++
    const open = k <= lines.length ? /^ {0,3}(`{3,}|~{3,})/.exec(lines[k - 1]) : null
    if (!open) return `${name}: line ${lead + k} of the file is not the opening line of the handed block's fence; ${remedy}`
    let c = k + 1
    for (; c <= lines.length; c++) {
      const m = /^ {0,3}(`{3,}|~{3,})([\s\S]*)$/.exec(lines[c - 1])
      if (m && m[1][0] === open[1][0] && m[1].length >= open[1].length && /^[ \t]*$/.test(m[2])) break
    }
    if (c > lines.length) return `${name}: the handed block's fence opened at line ${lead + k} of the file never closes; ${remedy}`
    for (let j = k + 1; j < c; j++) {
      if (read.has(j)) return `${name}: line ${lead + j} of the file, inside the handed block's fence, is read outside a fence, so the handed content would stand as executor lines; ${remedy}`
    }
    let j = c + 1
    const extra = []
    while (j <= b.last && !/^#{1,2} /.test(read.get(j) || '')) {
      if (lines[j - 1].trim() !== '') extra.push(j)
      j++
    }
    const closer = b === last && j > lines.length && extra.length === 1 && lines[extra[0] - 1].trimEnd() === `[/${docPath}]`
    if (extra.length && !closer) return `${name}: line ${lead + extra[0]} of the file sits between the handed block's fence and the next block, where only blank lines may; ${remedy}`
  }
  return null
}

// The first twelve hex digits of the git blob id of `buf` with CRLF folded to LF: the roles kit's
// `derive_fact_key` over the same bytes, so a fact keys one way on every checkout.
function deriveBlobId(buf) {
  const folded = Buffer.from(Buffer.from(buf).toString('latin1').replace(/\r\n/g, '\n'), 'latin1')
  return require('crypto').createHash('sha1').update(Buffer.concat([Buffer.from(`blob ${folded.length}\0`, 'latin1'), folded])).digest('hex').slice(0, 12)
}

// S4 - THE RE-CUT AT THE ACT LAUNCH: every fact line of the task section, each `blob:` and `record:` key
// re-derived from the bytes now at its source, `card/<sid>` through the sibling hook's `readCard`, a
// repo-relative path from the checkout root; a `cmd:` key is covered by the task-sha and not re-run.
// null when every key holds, else the refusal naming the key, both blobs and the re-render. Only the lines
// `readUnfencedLines` yields are read, so a fact line quoted inside handed content is content (TOOL-dBoundRoles-38 S4).
function checkFactKeys(section, root) {
  const fs = require('fs')
  const path = require('path')
  for (const [, line] of loadScratchGuard().readUnfencedLines(section)) {
    const f = line === null ? null : FACT_RE.exec(line)
    const m = f ? FACT_SOURCE_RE.exec(f.groups.key) : null
    if (!m) continue
    const g = m.groups
    let now = null
    const card = g.form === 'record' && g.ref.startsWith('card/') ? g.ref.slice(5) : null
    if (card !== null) {
      const sg = loadScratchGuard()
      const top = sg.resolveToplevel(root)
      const read = top ? sg.readCard(sg.resolveCommonDir(top), card) : { text: null, shown: '(no card: no checkout)' }
      now = read.text === null ? `nothing, ${read.shown}` : deriveBlobId(Buffer.from(read.text, 'utf8'))
    } else if (path.isAbsolute(g.ref) || /^[A-Za-z]:/.test(g.ref) || g.ref.split(/[\\/]/).includes('..')) {
      now = 'nothing: the key names no path inside the checkout'
    } else {
      try { now = deriveBlobId(fs.readFileSync(path.join(root, ...g.ref.split('/')))) } catch { now = 'nothing: no file is there' }
    }
    if (now !== g.sha) return `fact: ${f.groups.key} was cut at ${g.sha}, and its source now reads ${now}: re-render the handoff, which cuts it fresh, with handoff.py render.`
  }
  return null
}

// TOOL-dBoundRoles-3 S5 - THE STAND-IN BINDING RECORD, until dWellOiledMachine's session binding: a work order
// whose marker's `item=` is a tag spawns only in the session oriented for its unit. The session's card is read
// through the sibling hook's `readCard`, whose path is the kickoff checker's `--card --path --session <sid>`
// answer under `CARD_PATH_BOUND_MS`, and its `## route` units through `extractRouteUnits`; the marker's `unit=`
// must be one of them. null to admit, else the refusal naming the unit and the card, `readCard`'s `shown` where
// no card reads. A marker whose `item=` is `-` or absent is judged as before this rule. It does not see two
// sessions routing one unit, or a card edited by hand, which the write gate's card rules govern.
function checkItemBinding(m, sessionId, root) {
  if (m.item === null || m.item === '-') return null
  const path = require('path')
  const sg = loadScratchGuard()
  const top = sg.resolveToplevel(root)
  const common = top ? sg.resolveCommonDir(top) : null
  const card = typeof sessionId !== 'string' || sessionId === ''
    ? { text: null, shown: '(no card: the call carries no session_id)' }
    : common ? sg.readCard(common, sessionId) : { text: null, shown: '(no card: no git directory above the checkout)' }
  const remedy = `an item's work order spawns only in a session whose card routes its unit; spawn it from the session oriented for ${m.unit}, or re-render it with handoff.py render for a unit this session's card routes.`
  if (card.text === null) return `item ${m.item}: the work order is cut for unit ${m.unit}, and this session's card does not read, ${card.shown}: ${remedy}`
  const units = sg.extractRouteUnits(card.text).units.map((u) => u.unit)
  if (units.includes(m.unit)) return null
  return `item ${m.item}: the work order is cut for unit ${m.unit}, and the card ${card.shown} routes ${units.length ? units.join(', ') : 'no unit'}: ${remedy}`
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
  return `BLOCKED by spawn-guard: rule 6 (TOOL-aOrientedCast-7) refused this ${tool} call — ${why}\n${route}\n`
}

// TOOL-dBoundRoles-10 S3 - the policy key `prompts.author`, who writes a worker's task: `prompt-writer`, its
// default, or `requesting-worker-rendered`. The landed value through the policy kit's `readPolicy`, found
// through `resolvePolicyHelper`, the way rule 7 reads its key; null where no policy kit resolves beside this
// hook, so rule 6 runs as before the key; a refused read throws the reader's PolicyRefusal. Under
// `requesting-worker-rendered` rule 6 is the rendered-handoff check below; under `prompt-writer` it is that
// check and then the prompt writer's framing, `checkFraming` (TOOL-dBoundRoles-4 S4), which reads the value
// `renderAuthorNote` kept.
const PROMPTS_AUTHOR_KEY = 'prompts.author'
function resolvePromptsAuthor(root) {
  const helper = loadScratchGuard().resolvePolicyHelper()
  if (!helper || !require('fs').existsSync(helper)) return null
  return require(helper).readPolicy(PROMPTS_AUTHOR_KEY, { repo: root }).value
}

// The line every rule-6 refusal of an `Agent` call ends with (S6): the key, the value in force, and the remedy
// with its actor. The key is read once per call and root, kept with its value in `renderAuthorNote.at`, which
// `checkFraming` reads, and the line never throws: a refused read is named, its value kept as undefined, and
// rule 6 judges the call as the rendered-handoff check alone; rule 7 refuses a refused policy read.
function renderAuthorNote(root) {
  if (renderAuthorNote.at && renderAuthorNote.at.root === root) return renderAuthorNote.at.line
  const remedy = 'The driver renders the handoff the value requires; the owner may set another value of prompts.author through the policy file\'s one door, the loop kit\'s policy_edit.py.'
  let line
  let value
  try {
    const v = resolvePromptsAuthor(root)
    value = v
    line = v === null
      ? `${PROMPTS_AUTHOR_KEY} unarmed — no policy kit resolves beside this hook, so rule 6 is the rendered-handoff check alone (TOOL-dBoundRoles-10).`
      : v === 'requesting-worker-rendered'
        ? `${PROMPTS_AUTHOR_KEY} is requesting-worker-rendered (TOOL-dBoundRoles-10): every task is a handoff the requesting session rendered with handoff.py render, which rule 6 checks. ${remedy}`
        : `${PROMPTS_AUTHOR_KEY} is ${v} (TOOL-dBoundRoles-10): every worker's task is framed by the prompt writer, a handoff rendered with handoff.py render --framed-by, whose framing rule 6 checks on every spawn but the prompt writer's own (TOOL-dBoundRoles-4). ${remedy}`
  } catch (e) {
    line = `${PROMPTS_AUTHOR_KEY} could not be read (${String((e && e.message) || e).split(/\r?\n/)[0]}), so rule 6 judged this call as the rendered-handoff check alone (TOOL-dBoundRoles-10).`
  }
  renderAuthorNote.at = { root, line, value }
  return line
}

// Rule 6 on an `Agent` call (§4 "The evaluation order", step 2): null to admit, else a deny string.
function checkHandoffSpawn(data, index, root) {
  const fs = require('fs')
  const path = require('path')
  // TOOL-dBoundRoles-10 S3 - prompts.author, read once per Agent call here, at the rule's start; main ends
  // every rule-6 refusal of the call with the line this read composed.
  renderAuthorNote(root)
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
  // TOOL-dBoundRoles-58 S25 - the typed blocks first, before any marker is counted, so a marker forged in a typed
  // value is denied naming its block and its line, and not by the count alone; the file's own section below.
  const sent = extractTaskSection(ti.prompt)
  const forged = sent === null ? null : checkTypedBlocks(sent, readSectionLead(ti.prompt, sent), 'the prompt')
  if (forged) return renderHandoffDeny('Agent', forged, index)
  const marks = loadScratchGuard().extractHandoffMarker(ti.prompt)
  if (marks.length !== 1) return renderHandoffDeny('Agent', `the prompt carries ${marks.length} ${HANDOFF_MARK} marker lines; exactly one is required.`, index)
  const m = marks[0]
  if (m.role !== type) return renderHandoffDeny('Agent', `the marker's role ${m.role} is not the subagent_type ${type}.`, index)
  const parts = checkPromptPath(m.path, m.build)
  if (!parts) {
    return renderHandoffDeny('Agent', `the marker's path ${m.path} is not a repo-relative file under builds/${m.build}/prompts/ with no \`..\` segment.`, index)
  }
  const file = path.join(root, ...parts)
  let st = null
  try { st = fs.statSync(file) } catch { st = null }
  if (!st || !st.isFile()) return renderHandoffDeny('Agent', `the marker's path ${m.path} names no file under ${root.split(path.sep).join('/')}.`, index)
  const text = fs.readFileSync(file, 'utf8')
  // TOOL-dBoundRoles-46 S2 - each typed input's block held to the authored-line rule, before the file's markers are
  // counted, the role text and the fact re-cut, so a forged line is named here first.
  const section = extractTaskSection(text)
  const lead = section === null ? 0 : readSectionLead(text, section)
  const typed = section === null ? null : checkTypedBlocks(section, lead, 'the file')
  if (typed) return renderHandoffDeny('Agent', `${m.path}'s ${typed}`, index)
  const fileMarks = loadScratchGuard().extractHandoffMarker(text)
  if (fileMarks.length !== 1 || fileMarks[0].line !== m.line) {
    return renderHandoffDeny('Agent', `${m.path} does not hold exactly one marker line byte-equal to the prompt's (it holds ${fileMarks.length}).`, index)
  }
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
  // TOOL-dBoundRoles-38 S5 - a section whose walk ends inside a fence would hide every later fact line from
  // the re-cut below, so it is denied, naming the line of the file the fence opened at.
  let open = null
  for (const [n, line] of loadScratchGuard().readUnfencedLines(section)) if (line === null) open = n
  if (open !== null) {
    return renderHandoffDeny('Agent', `${m.path}'s \`## Task\` section ends inside a fence opened at line ${lead + open} of the file, so every fact line after it would be read as content; close it in the value that opened it and re-render with handoff.py render.`, index)
  }
  // TOOL-dBoundRoles-48 S3 - the fence state at every block: after the typed blocks, before the role text and the
  // fact re-cut, so a fact line a flipped fence surfaced from handed content is denied before it is read as one.
  const flipped = checkBlockFences(section, lead, m.path)
  if (flipped) return renderHandoffDeny('Agent', `${m.path}'s ${flipped}`, index)
  // TOOL-dBoundRoles-6 S6 - the role text: the marker's role-sha against the one the index carries for
  // the type, the hash of the `## Role` section the renderer composes, so a handoff rendered from role
  // text the agent type was not rendered from is refused. After the digest, before the description.
  const indexed = index.roles[type]['role-sha']
  if (indexed === undefined) {
    return renderHandoffDeny('Agent', `role-sha: ${index.shown} holds no role-sha for ${type}; re-render the index with render_agents.py --write.`, index)
  }
  if (indexed !== m.roleSha) {
    return renderHandoffDeny('Agent', `role-sha: the handoff was rendered from role text ${m.roleSha}, and ${type} was rendered from ${indexed}; re-render the handoff with handoff.py render, or the index with render_agents.py --write where the role's text moved after it.`, index)
  }
  // TOOL-dBoundRoles-13 S4 - the handed facts: each key re-derived from its source at the spawn, after the
  // role text and before the description. A handoff rendered before the fact line carries none: admitted.
  const moved = checkFactKeys(section, root)
  if (moved) return renderHandoffDeny('Agent', moved, index)
  // TOOL-dBoundRoles-3 S5 - an item's work order bound to its act: after the facts, before the description.
  const unbound = checkItemBinding(m, data.session_id, root)
  if (unbound) return renderHandoffDeny('Agent', unbound, index)
  // TOOL-aOrientedCast-27 step 2.10 - after the digest and the role text, so the one remedy left is the description.
  const workflow = index.roles[type].workflow
  if (typeof workflow !== 'string' || workflow === '') {
    return renderHandoffDeny('Agent', `${index.shown} declares no workflow for ${type}, so this spawn's name cannot be derived; re-render the role index.`, index)
  }
  const spawnName = renderSpawnName(m, workflow)
  if (typeof ti.description !== 'string' || ti.description.trim() !== spawnName) {
    return renderHandoffDeny('Agent', `the call's description ${JSON.stringify(ti.description === undefined ? null : ti.description)} is not this handoff's name ` +
      `${JSON.stringify(spawnName)}: the marker's build and unit and the ${type} role's workflow. Pass description exactly as handoff.py render prints it.`, index)
  }
  // TOOL-dBoundRoles-4 S4 - the prompt writer's framing, last, once every check above admits the handoff.
  const unframed = checkFraming(type, m, section, root)
  if (unframed) return renderHandoffDeny('Agent', unframed, index)
  return null
}

// The repo-relative path `p` split at its separators when it names a file under `builds/<build>/prompts/` with
// no `..`, empty or `.` segment below that folder, else null: the one test of a marker's path and of the file a
// `Framed by:` line names (TOOL-dBoundRoles-4 S4).
function checkPromptPath(p, build) {
  const parts = String(p).replace(/\\/g, '/').split('/')
  const at = parts.indexOf('builds')
  if (loadScratchGuard().extractBuildSlug(p) !== build || parts[at + 2] !== 'prompts' || parts.length < at + 4 || parts.slice(at + 3).some((s) => s === '' || s === '.')) return null
  return parts
}

// TOOL-dBoundRoles-4 S4 - THE FRAMING UNDER `prompts.author = prompt-writer`. The value is the one rule 6 read at
// its start, `renderAuthorNote.at.value`; any other value, no policy kit beside this hook, or a read that refused
// applies nothing, and neither does a spawn of the prompt writer itself, whose task is its driver's details
// rendered unframed. Otherwise the section, walked by the sibling's `readUnfencedLines`, holds exactly one
// `### framing:job` heading and exactly one `Framed by:` line, that line inside the block the heading opens (up to
// the next `### ` or `## ` heading), spelled `Framed by: <path> task-sha=<12hex>`, its path a file under
// `builds/<the marker's build>/prompts/` (`checkPromptPath`) holding exactly one marker, read by
// `extractHandoffMarker`, whose role is the prompt writer and whose task-sha is the line's. null to admit, else
// the refusal naming the key, its value and the three-call route. The task-sha binds the framing's bytes to the
// prompt writer's work order; WHAT IT DOES NOT CHECK: that the framing is that agent's return, which the
// renderer read, nor that the named work order was spawned at all.
const PROMPT_WRITER = 'gov-prompt-writer'
const FRAMED_BY_RE = /^Framed by: (?<path>\S+) task-sha=(?<taskSha>[0-9a-f]{12})$/
function checkFraming(type, m, section, root) {
  const fs = require('fs')
  const path = require('path')
  const author = renderAuthorNote.at && renderAuthorNote.at.root === root ? renderAuthorNote.at.value : undefined
  if (author !== 'prompt-writer' || type === PROMPT_WRITER) return null
  const route = `${PROMPTS_AUTHOR_KEY} is prompt-writer, so a ${type} task carries the prompt writer's framing: render the prompt writer with \`handoff.py render --role ${PROMPT_WRITER} --for ${type} --build ${m.build}${m.unit === '-' ? '' : ` --unit ${m.unit}`} --input question=<your details> ...\`, spawn it, then render this task with \`handoff.py render --role ${type} ... --framed-by <the prompt writer's agent id>\` and spawn that.`
  const lines = []
  for (const [n, raw] of loadScratchGuard().readUnfencedLines(section)) if (raw !== null) lines.push([n, raw.replace(/\r/g, '')])
  const heads = readTaskBlocks(section).filter((b) => b.heading === 'framing:job')
  if (heads.length !== 1) return `the task carries ${heads.length} \`### framing:job\` blocks; exactly one is required. ${route}`
  const framed = lines.filter(([, l]) => l.startsWith('Framed by:'))
  if (framed.length !== 1) return `the task carries ${framed.length} \`Framed by:\` lines; exactly one is required, inside its \`### framing:job\` block. ${route}`
  const next = lines.find(([n, l]) => n > heads[0].first && /^## /.test(l))
  if (framed[0][0] < heads[0].first || framed[0][0] > heads[0].last || (next && framed[0][0] > next[0])) return `the task's \`Framed by:\` line sits outside its \`### framing:job\` block. ${route}`
  const f = FRAMED_BY_RE.exec(framed[0][1].trimEnd())
  if (!f) return `the task's line ${JSON.stringify(framed[0][1].slice(0, 120))} is not \`Framed by: <path> task-sha=<12 hex>\`. ${route}`
  const parts = checkPromptPath(f.groups.path, m.build)
  if (!parts) return `the \`Framed by:\` path ${f.groups.path} is not a repo-relative file under builds/${m.build}/prompts/ with no \`..\` segment. ${route}`
  let text = null
  try { text = fs.readFileSync(path.join(root, ...parts), 'utf8') } catch { text = null }
  if (text === null) return `the \`Framed by:\` path ${f.groups.path} names no file under ${root.split(path.sep).join('/')}. ${route}`
  const marks = loadScratchGuard().extractHandoffMarker(text)
  if (marks.length !== 1) return `${f.groups.path} holds ${marks.length} ${HANDOFF_MARK} marker lines; the prompt writer's work order holds exactly one. ${route}`
  if (marks[0].role !== PROMPT_WRITER) return `${f.groups.path}'s marker names role=${marks[0].role}, not ${PROMPT_WRITER}: only the prompt writer's work order frames a task. ${route}`
  if (marks[0].taskSha !== f.groups.taskSha) return `${f.groups.path}'s marker says task-sha=${marks[0].taskSha}, and the \`Framed by:\` line names ${f.groups.taskSha}: the framing was cut from another render of it. ${route}`
  return null
}

// A direct spawn's name, `<build> · <unit> · <workflow>`, the unit part left out when the marker's is
// `-`. The renderer's `render_spawn_name` builds the same string; a kit file imports no sibling kit.
function renderSpawnName(marker, workflow) {
  return [marker.build, marker.unit === '-' ? '' : marker.unit, workflow].filter(Boolean).join(' · ')
}

// Rule 6 on a `Workflow` call (§4 "The evaluation order", step 3): null to admit, else a deny string.
function checkHarnessCall(data, index, root) {
  const ti = data.tool_input || {}
  if (!index.harnesses.length) return renderHandoffDeny('Workflow', `UNARMED: ${index.shown} declares no harness, so no Workflow call can be admitted.`, index)
  if (ti.script) return renderHandoffDeny('Workflow', 'an inline `script` is never a declared harness.', index)
  const sp = ti.scriptPath
  if (typeof sp !== 'string' || sp === '') return renderHandoffDeny('Workflow', 'the call names no `scriptPath` (a `name:` run is not a declared harness).', index)
  const entry = resolveHarnessEntry(data, index, root)
  if (entry === null) {
    return renderHandoffDeny('Workflow', `scriptPath ${sp} (${resolveHarnessEntry.rel} from the checkout root) is not a declared harness.`, index)
  }
  // TOOL-dBoundRoles-25 S3 - the declared harness runs only at its landed bytes: after the path match, so a call
  // refused for its path pays no git call, and before the args, so an edited harness is named first.
  // TOOL-dBoundRoles-88 - and so does every declared harness its text nests.
  const unlanded = checkHarnessClosure(entry, root, index)
  if (unlanded) return renderHandoffDeny('Workflow', unlanded, index)
  const a = loadScratchGuard().extractWorkflowArgs(data)
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

// The `harnesses` entry of the index a Workflow call's `scriptPath` names, as the index spells it, or
// null: the path resolved against the payload cwd, symlinks followed, compared repo-relative. Rule 6
// and rule 8 share it (TOOL-aGuardedEffort-1 S6); `.rel` is the path as compared, for rule 6's refusal.
function resolveHarnessEntry(data, index, root) {
  const fs = require('fs')
  const path = require('path')
  const sp = String((data.tool_input || {}).scriptPath)
  const folded = process.platform === 'win32' ? sp.replace(/\\/g, '/').replace(/^\/([A-Za-z])\//, '$1:/') : sp
  const abs = path.resolve(data.cwd || process.cwd(), folded)
  let real = abs
  try { real = fs.realpathSync(abs) } catch { real = abs }
  let top = root
  try { top = fs.realpathSync(root) } catch { top = root }
  const rel = buildHarnessKey(path.relative(top, real))
  resolveHarnessEntry.rel = rel
  const hit = index.harnesses.find((h) => buildHarnessKey(h) === rel)
  return hit === undefined ? null : hit
}

// A harness path as compared: the hooks kit's fold, a leading `./` ignored.
function buildHarnessKey(p) {
  return loadScratchGuard().buildComparablePath(p).replace(/^\.\//, '')
}

// TOOL-dBoundRoles-25 S3 - THE TWO BLOBS ADMISSION COMPARES, for the declared harness `rel` (repo-relative, as the
// index spells it) under the checkout `root`: `{ L, landed, worktree }`, `landed` the blob id of `rel` at the landed
// revision L or '' where L holds no such path, `worktree` the id `git hash-object` gives the working-tree file, which
// applies the repository's clean filters, so a CRLF checkout of an LF blob reads equal. L is the policy kit's
// `readLandedRevision`, the one JS reader of the landed revision (TOOL-dGroundRules-5 S5), found through the hooks
// kit's `resolvePolicyHelper` as rule 7 finds it. `{ why }` where it cannot be read: no policy kit, a refusal from
// it, an answer that is no commit, or a working-tree file git cannot hash. Two git calls; never throws.
function readHarnessBlobs(rel, root) {
  const fs = require('fs')
  const { spawnSync } = require('child_process')
  const helper = loadScratchGuard().resolvePolicyHelper()
  if (!helper || !fs.existsSync(helper)) {
    return { why: `no policy kit resolves beside the hooks kit, so the landed revision ${rel} is held to cannot be read, and a rule that cannot read does not admit; the owner installs the policy kit (govkit apply --kits policy)` }
  }
  let L
  try { L = String(require(helper).readLandedRevision(root)).trim() } catch (e) {
    return { why: `the landed revision ${rel} is held to cannot be read (${String((e && e.message) || e).split(/\r?\n/)[0]}), and a rule that cannot read does not admit; the owner clears the policy reader's refusal it names` }
  }
  if (!/^[0-9a-f]{40,64}$/.test(L)) return { why: `the landed revision reads ${JSON.stringify(L.slice(0, 80))}, which is no commit, so ${rel} cannot be held to it; the owner names the default branch the policy reader's ladder resolves` }
  const env = Object.assign({}, process.env)
  for (const k of ['GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_OBJECT_DIRECTORY', 'GIT_COMMON_DIR']) delete env[k]
  const runGit = (args) => spawnSync('git', ['-C', root, ...args], { encoding: 'utf8', env, timeout: 20000, windowsHide: true })
  const at = runGit(['rev-parse', '--verify', '--quiet', `${L}:${rel}`])
  const landed = at.status === 0 ? String(at.stdout || '').trim() : ''
  const now = runGit(['hash-object', '--', rel])
  const worktree = now.status === 0 ? String(now.stdout || '').trim() : ''
  if (!worktree) return { why: `git could not hash the working-tree file ${rel} (${String(now.stderr || (now.error && now.error.message) || 'no answer').trim().split(/\r?\n/)[0]}), and a rule that cannot read does not admit; the driver restores the file` }
  return { L, landed, worktree }
}

// TOOL-dBoundRoles-25 S3 - ADMISSION HELD TO THE LANDED BLOB (gap-roles-30): a declared harness runs only when its
// working-tree blob is its blob at the landed revision, so an edited harness never runs before the bar has read it.
// An uncommitted edit and a committed but unlanded one are refused alike (§8 F2). null to admit, else the reason,
// naming the harness, L's first eight hex digits and the remedy's actor: the driver, who lands the harness or runs
// it at its landed bytes, or the owner where the landed revision cannot be read at all.
function checkHarnessLanded(rel, root) {
  const b = readHarnessBlobs(rel, root)
  if (b.why) return b.why
  const L8 = b.L.slice(0, 8)
  if (!b.landed) return `harness ${rel} is not landed at ${L8}; land it before running it (the driver lands it, or runs a harness that is).`
  if (b.landed !== b.worktree) return `harness ${rel} differs from its blob at the landed revision ${L8}; an edited harness runs only after it lands, so the bar has read it (the driver lands the edit, or restores the landed bytes with git show ${L8}:${rel} for the call).`
  return null
}

// TOOL-dBoundRoles-88 S1 - the `harnesses` entries a harness script's text nests, `{ callees }`, or `{ why }` naming
// the line of the first nested call that cannot be placed. A nested call is `workflow(` on a line whose first
// non-blank characters are not `//`; its argument must open with an object literal whose first key is `scriptPath`
// and whose value is one quoted literal naming a declared harness. The literal is compared repository-relative, as
// the runtime resolves it. Lines end where JavaScript ends them, so a comment line hides no code behind a lone
// carriage return. The docblock's NESTED CEILING says what a text scan does not see.
function extractNestedHarnesses(text, index) {
  const code = text.split(/\r\n|[\n\r\u2028\u2029]/).map((l) => (/^\s*\/\//.test(l) ? '' : l)).join('\n')
  const callees = []
  for (const m of code.matchAll(/\bworkflow\s*\(/g)) {
    const line = code.slice(0, m.index).split('\n').length
    const rest = code.slice(m.index + m[0].length)
    const lit = /^\s*\{\s*scriptPath\s*:\s*(['"])([^'"\\\n]+)\1\s*[,}]/.exec(rest)
    if (!lit) return { why: `line ${line} nests workflow(${rest.trim().split('\n')[0].trim().slice(0, 80)}, whose argument does not open with a quoted { scriptPath: '<path>' }` }
    const hit = index.harnesses.find((h) => buildHarnessKey(h) === buildHarnessKey(lit[2]))
    if (hit === undefined) return { why: `line ${line} nests ${lit[2]}, which is not a declared harness` }
    callees.push(hit)
  }
  return { callees }
}

// TOOL-dBoundRoles-88 S2 - THE TRANSITIVE HOLD: `checkHarnessLanded` on the entry and on every declared harness it
// nests, each file's text read after its blob compared equal, so the bytes scanned are the bytes that run. Each entry
// is held once, so the index's list bounds the walk and a cycle ends it. null to admit, else the reason; the entry's
// own is `checkHarnessLanded`'s, unchanged.
function checkHarnessClosure(entry, root, index) {
  const path = require('path')
  const caller = new Map([[entry, null]])
  for (const [rel, by] of caller) { // a Map's walk reaches the entries added during it
    const unlanded = checkHarnessLanded(rel, root)
    if (unlanded) return by === null ? unlanded : `${unlanded} Harness ${by} runs it through a nested workflow() call, so the driver keeps both files at their landed bytes for the whole call.`
    let text
    try { text = require('fs').readFileSync(path.join(root, rel), 'utf8') } catch (e) {
      return `harness ${rel} could not be read for its nested calls (${(e && e.code) || e}), and a rule that cannot read does not admit; the driver restores the file.`
    }
    const nested = extractNestedHarnesses(text, index)
    if (nested.why) return `harness ${rel} ${nested.why}, so what it runs cannot be held to its landed blob; the driver lands it naming a declared harness by a quoted path.`
    for (const n of nested.callees) if (!caller.has(n)) caller.set(n, rel)
  }
  return null
}

// RULE 8 (TOOL-aGuardedEffort-1) — the level a call runs at is the one the effort policy gives its
// model. Every level is resolved by the roles kit's renderer into the index's `effort` key, so this
// rule only looks up: it spawns no interpreter and reads no policy file. The two verbs it names in a
// refusal are the roles kit's, by bare file name.

// The model of the last main-chain assistant entry of a transcript: `{ model }`, or `{ why }` when the
// path is absent, the read throws, or no entry names one. The file is read whole and walked from the
// end; a line that does not parse, a sidechain record and the model `<synthetic>` are skipped. Never throws.
function readSessionModel(transcriptPath) {
  if (typeof transcriptPath !== 'string' || transcriptPath === '') return { why: 'the payload carries no transcript_path' }
  let lines
  try { lines = require('fs').readFileSync(transcriptPath, 'utf8').split('\n') } catch (e) {
    return { why: `the transcript ${transcriptPath} is unreadable (${(e && e.code) || e})` }
  }
  for (let i = lines.length - 1; i >= 0; i--) {
    let rec
    try { rec = JSON.parse(lines[i]) } catch { continue }
    if (!rec || rec.type !== 'assistant' || rec.isSidechain === true) continue
    const model = rec.message && rec.message.model
    if (typeof model === 'string' && model !== '' && model !== '<synthetic>') return { model }
  }
  return { why: `the transcript ${transcriptPath} holds no main-chain assistant entry naming a model` }
}

// The names of every profile whose `match` holds a word of the model id, the words being the id's runs
// of letters and digits after lower-casing: the roles kit's `resolve_profile` rule, held to it by arm
// 20 of that kit's adopter suite. None is the default tables, one that profile, two or more no profile.
function resolveModelProfile(profiles, model) {
  const words = String(model).toLowerCase().match(/[a-z0-9]+/g) || []
  return Object.keys(profiles).filter((n) => profiles[n] && Array.isArray(profiles[n].match) && profiles[n].match.some((w) => words.includes(w)))
}

// The refusal: the rule, the tool, the reason, and the call that prints the right value.
function renderEffortDeny(tool, why, remedy) {
  return `BLOCKED by spawn-guard: rule 8 (TOOL-aGuardedEffort-1) refused this ${tool} call — ${why}\n${remedy}\n`
}

// Rule 8 on a call rule 6 admitted: null when it was graded and admitted, or when the index carries
// no `effort`; `{ deny }` with the refusal text; `{ note }` with the one line saying the level was not
// checked and why. A role or harness the index's tables do not hold, and a stage key they disagree
// on, throws, and `main()` refuses. A harness none of whose workflows has a stage key is a note.
function checkEffortLevel(data, index, root) {
  const e = index.effort
  if (!e) return null
  const tool = data.tool_name
  const ti = data.tool_input || {}
  const checkOwn = (o, k) => !!o && typeof o === 'object' && Object.prototype.hasOwnProperty.call(o, k)
  const renderShown = (v) => JSON.stringify(typeof v === 'string' ? v.slice(0, 80) : v === undefined ? null : v)
  const renderLevel = (v) => (typeof v === 'string' ? v.slice(0, 80) : renderShown(v))
  const renderNote = (why) => ({ note: `spawn-guard: rule 8 did not check this ${tool} call's effort level — ${why}` })
  // F2: a session whose environment fixes the level offers no `effort` on its Agent tool, so no call
  // could pass. An Agent call's step alone, before the model is read; a Workflow call is graded.
  if (tool === 'Agent' && process.env.CLAUDE_CODE_EFFORT_LEVEL) {
    return renderNote("CLAUDE_CODE_EFFORT_LEVEL is set, so this session's Agent tool carries no effort")
  }
  let model = tool === 'Agent' ? ti.model : undefined
  let source = 'the call'
  if (typeof model !== 'string' || model === '') {
    const read = readSessionModel(data.transcript_path)
    if (read.why) return renderNote(read.why)
    model = read.model
    source = 'the transcript'
  }
  const names = resolveModelProfile(e.profiles, model)
  // F1: the resolver refuses an id two profiles match, so no expected level exists to name.
  if (names.length > 1) return renderNote(`the model ${renderShown(model)} matches the profiles ${names.join(' and ')}, so no one profile's levels are its own`)
  const table = names.length ? e.profiles[names[0]] : e.default
  const giver = names.length ? `the ${names[0]} profile gives it` : 'the default tables give it'
  const where = `on the model ${renderShown(model)} (read from ${source})`
  if (tool === 'Agent') {
    const type = ti.subagent_type
    if (!checkOwn(e.default.roles, type) || !checkOwn(table.roles, type)) throw new Error(`the effort tables of ${index.shown} hold no level for the role ${type}`)
    const own = checkOwn(ti, 'effort')
    const seen = own ? ti.effort : e.default.roles[type]
    const expected = table.roles[type]
    if (seen === expected) return null
    return { deny: renderEffortDeny('Agent',
      `${type} would run at ${renderLevel(seen)} (${own ? "the call's own `effort`" : "its agent type's level; the call carries no `effort`"}), and ${giver} ${expected} ${where}.`,
      `Pass \`effort\` as \`handoff.py role-efforts --model ${renderShown(model)}\` prints it for ${type}.`) }
  }
  const entry = resolveHarnessEntry(data, index, root)
  const workflows = entry === null ? null : e.harnesses[entry]
  if (!Array.isArray(workflows) || !workflows.length) throw new Error(`the effort tables of ${index.shown} name no workflow for the harness ${entry}`)
  const a = loadScratchGuard().extractWorkflowArgs(data) || {}
  const efforts = a.efforts === undefined ? {} : a.efforts
  if (!efforts || typeof efforts !== 'object' || Array.isArray(efforts)) {
    return { deny: renderEffortDeny('Workflow', '`args.efforts` is present and not a plain object, so no stage level can be read from it.',
      workflows.map((w) => `Pass \`efforts\` as \`handoff.py stage-efforts ${w} --model ${renderShown(model)}\` prints it.`).join('\n')) }
  }
  // A harness serving two workflows: the hook cannot tell which one a call runs, so the call is
  // admitted when the levels of at least ONE whole workflow are its own, and never key by key.
  // A stage's level is the call's `efforts` value, or with none the level of the agent type the
  // call's `roles` names for the stage, and a stage neither names counts as differing: it would
  // spawn untyped at the session's level, which no table holds (TOOL-aGuardedEffort-2 S1). A
  // workflow's stage keys are those of `unset` joined with those of the matched table's `stages`,
  // and a key one side lacks throws; a workflow with no key adds no line and never admits (S2).
  const lines = []
  const keyed = []
  for (const w of workflows) {
    const stages = (checkOwn(table.stages, w) && table.stages[w]) || {}
    const unset = (checkOwn(e.unset, w) && e.unset[w]) || {}
    const keys = [...new Set([...Object.keys(unset), ...Object.keys(stages)])].sort()
    for (const key of keys) {
      if (!checkOwn(unset, key) || !checkOwn(stages, key)) throw new Error(`the effort tables of ${index.shown} disagree on stage ${key} of ${w}`)
    }
    if (!keys.length) continue
    keyed.push(w)
    const differing = []
    for (const key of keys) {
      let seen
      let how
      if (checkOwn(efforts, key)) {
        seen = efforts[key]
        how = `the call's own \`efforts.${key}\``
      } else if (checkOwn(a.roles, key)) {
        const role = a.roles[key]
        if (!checkOwn(e.default.roles, role)) throw new Error(`the effort tables of ${index.shown} hold no level for the role ${renderLevel(role)}`)
        seen = e.default.roles[role]
        how = `${role}, its agent type's level; the call's \`efforts\` names no ${key}`
      } else {
        differing.push(`stage ${key} would run untyped at the session's level (the call's \`roles\` and \`efforts\` name no ${key}), expected ${stages[key]}`)
        continue
      }
      if (seen === stages[key]) continue
      differing.push(`stage ${key} would run at ${renderLevel(seen)} (${how}), expected ${stages[key]}`)
    }
    if (!differing.length) return null
    lines.push(`${w}: ${differing.join('; ')}`)
  }
  if (!keyed.length) return renderNote(`the effort tables of ${index.shown} hold no stage key for ${workflows.join(' and ')}, which the harness ${entry} runs`)
  return { deny: renderEffortDeny('Workflow',
    `the harness ${entry} would run a stage at another level than ${giver} ${where}.\n${lines.join('\n')}`,
    `Pass \`efforts\` as ${keyed.map((w) => `\`handoff.py stage-efforts ${w} --model ${renderShown(model)}\``).join(' or ')} prints it, for the workflow this call runs.`) }
}

// RULE 7 (TOOL-dGroundRules-10) — the settings in force. The agent limit is the harness's to enforce,
// through the two variables the policy kit renders into `.claude/settings.json`; the harness reads
// them from the working tree, so a hand-raised `env`, or a render left behind a lowering, would run
// past the landed limit. This rule refuses that at the next call. It reads the landed limit through
// the policy kit's `readPolicy`, found through `resolveKitDir`, and never the working-tree mirror; a
// hooks kit that finds no `policy` kit adds no rule.
// The limit is landed; the helper that reads it is not.
// Its location rests on the working-tree receipt, so a forged row chooses the code this rule runs
// (TOOL-dFairHearing-48 F1).
// WHAT IT DOES NOT SEE: an environment override of the two variables, which the harness applies
// and no hook can read. UNVERIFIED: that a session started before a lowering keeps its settings until
// it restarts. Read: every layer readSettingsLayers returns (TOOL-dGroundRules-61 S1); a cwd in no checkout, or a throw at any step, refuses, naming it (TOOL-dGroundRules-21 S38). A refused policy read is no settings fault, so it denies under its own text, printing the reader's line and never the settings remedy (TOOL-dGroundRules-73). null = allow · string = deny.
const SETTINGS_VARS = ['CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS', 'CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS']

function checkSettingsInForce(data) {
  const fs = require('fs')
  const path = require('path')
  const helper = loadScratchGuard().resolvePolicyHelper()
  if (!fs.existsSync(helper)) return null
  const root = resolveCheckoutRoot(data.cwd || process.cwd())
  if (!root) return `BLOCKED by spawn-guard: rule 7 (TOOL-dGroundRules-10) refused this ${data.tool_name} call — the payload cwd ${String(data.cwd || process.cwd()).split(path.sep).join('/')} is in no git checkout, so the settings in force and the landed agent limit cannot be read, and a rule that cannot read does not admit.\n`
  const rel = path.relative(root, path.dirname(helper)).split(path.sep).join('/')  // the render's kit path: a hook names no prefix
  const remedy = `python ${rel ? rel + '/' : ''}policy.py settings --write`
  const renderSettingsDeny = (why) =>
    `BLOCKED by spawn-guard: rule 7 (TOOL-dGroundRules-10) refused this ${data.tool_name} call — the ` +
    `settings this checkout's harness starts from do not hold the landed agent limit.\n${why}\n` +
    `Render them from the policy: ${remedy}, run at ${root.split(path.sep).join('/')}. A session started ` +
    `before the render keeps the settings it started with until it restarts (UNVERIFIED).\n`
  const renderReadDeny = (why) =>
    `BLOCKED by spawn-guard: rule 7 (TOOL-dGroundRules-10) refused this ${data.tool_name} call — the ` +
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
      `spawn-guard: ${onlyArg} is refused — this hook runs no script rule since TOOL-dFairHearing-16. ` +
        `The verifier total and the loop markers run from the review kit's check-verifier-fanout.js, ` +
        `and the ref-keyed join ban from its check-review-join.js, each reading the review kit's script-views.js. ` +
        `Omit the flag to run this hook's rules 6, 8 and 7.\n`,
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

  // TOOL-dBoundRoles-25 - the hooks kit's readers, before any rule reads them: a pack that cannot load
  // scratch-guard.js cannot read the index, and refuses the call rather than admit it unread.
  try { loadScratchGuard() } catch (e) {
    process.stderr.write(`BLOCKED by spawn-guard: the hooks kit's scratch-guard.js could not be loaded (${String((e && e.message) || e).split(/\r?\n/)[0]}), so no rule of this guard can read the call, and a guard that cannot read does not admit. The owner installs the hooks kit beside the roles kit: govkit apply --kits agent-cap.\n`)
    process.exit(2)
  }

  // RULE 6 (TOOL-aOrientedCast-7) — first, so a call outside a declared harness is refused whatever its
  // args. An absent `.claude/roles.json` at the role root adds no rule, except in a governed tree, whose
  // `.claude/agents/` keeps a rendered role agent, where it refuses (TOOL-dBoundRoles-6 S3); a broken
  // one, or a throw anywhere in the rule, refuses: a rule that cannot finish does not admit.
  let index = null
  let root = null
  {
    let deny = null
    try {
      // TOOL-aOrientedCast-14: the root of the payload cwd, else of CLAUDE_PROJECT_DIR. No candidates
      // are passed, so the third start, a launched script's directory, never applies (TOOL-dBoundRoles-8 S2).
      const { loadRoleIndex, resolveRoleRoot, checkRoleGoverned } = loadScratchGuard()
      const cwd = data.cwd || process.cwd()
      root = resolveRoleRoot(cwd, process.env)
      if (root) {
        index = loadRoleIndex(root)
        if (index.state === 'absent' && checkRoleGoverned(root)) {
          deny = renderHandoffDeny(data.tool_name, `the role index ${index.shown} is absent while this tree carries rendered role agents; re-render it with render_agents.py --write.`, null)
        } else if (index.state === 'broken') deny = renderHandoffDeny(data.tool_name, `the role index ${index.shown} ${index.why}; fix or regenerate it.`, null)
        else if (index.state === 'ok') deny = data.tool_name === 'Agent' ? checkHandoffSpawn(data, index, root) : checkHarnessCall(data, index, root)
      } else if (process.env.CLAUDE_PROJECT_DIR) {
        process.stderr.write(`spawn-guard: rule 6 unarmed — neither the payload cwd ${cwd} nor CLAUDE_PROJECT_DIR ${process.env.CLAUDE_PROJECT_DIR} lies in a checkout, so no role index was read\n`)
      }
    } catch (e) {
      deny = renderHandoffDeny(data.tool_name, `the rule threw (${(e && e.message) || e}), and a rule that cannot finish does not admit.`, index)
    }
    // TOOL-dBoundRoles-10 S3 - every rule-6 refusal of an Agent call names prompts.author and the value in force.
    if (deny && data.tool_name === 'Agent' && root) deny += renderAuthorNote(root) + '\n'
    if (deny) {
      process.stderr.write(deny)
      process.exit(2)
    }
  }

  // RULE 8 (TOOL-aGuardedEffort-1) — the effort level, on a call rule 6 admitted through an index
  // carrying `effort`. A refusal exits 2; a level it could not check is one stderr line, and rule 7
  // runs as before. A throw refuses, naming a re-render: a rule that cannot finish does not admit.
  if (index && index.state === 'ok' && index.effort) {
    let verdict
    try {
      verdict = checkEffortLevel(data, index, root)
    } catch (e) {
      verdict = { deny: renderEffortDeny(data.tool_name, `the rule threw (${(e && e.message) || e}), and a rule that cannot finish does not admit.`,
        `Re-render the role index ${index.shown} with \`render_agents.py --write\`.`) }
    }
    if (verdict && verdict.deny) {
      process.stderr.write(verdict.deny)
      process.exit(2)
    }
    if (verdict && verdict.note) process.stderr.write(verdict.note + '\n')
  }

  // RULE 7 (TOOL-dGroundRules-10) — the settings in force, for both tools. A throw refuses: a rule that
  // cannot finish does not admit, and a hook that exits 1 is non-blocking.
  {
    let deny = null
    try {
      deny = checkSettingsInForce(data)
    } catch (e) {
      deny = `BLOCKED by spawn-guard: rule 7 (TOOL-dGroundRules-10) threw (while ${checkSettingsInForce.step || 'resolving the payload cwd'}: ${(e && e.message) || e}), and a rule that cannot finish does not admit.\n`
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
// TOOL-dBoundRoles-25 S4 - THE PACK'S EXPORTS, each read by the roles kit alone: rule 8's resolver and check, for
// that kit's adopter suite (arm 20) and a probe of the rule alone, and rule 6's typed inputs and prompts.author
// reader, for this kit's suite. `main()` runs only when this file is the entry point, so requiring it judges nothing.
module.exports = { resolveModelProfile, checkEffortLevel, TYPED_INPUTS, resolvePromptsAuthor, checkHarnessLanded, readHarnessBlobs }
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

// TOOL-dFairHearing-22 — THE OPT-IN PACK'S PRESENCE, after rules 6, 8 and 7. The spec-audit opt-in left
// this hook for the review kit's spec-audit-optin.js (TOOL-dFairHearing-16), and a partial update
// that names this kit alone lands the hook without it: the hooks kit cannot require the review kit,
// which requires it back, a cycle govkit refuses. So a Workflow call carrying the opt-in's own
// trigger, `kind: 'spec-audit'` or a `specAudit` key in its structured args, is refused unless the
// pack is found by `resolveKitDir` (TOOL-dFairHearing-32 S25), `resolve_kit_dir`'s three rungs: a
// receipt row, then `<here>/workflows/` and `<here>/../workflows/`. A stale or escaping row is skipped,
// never followed and never a deny; only the resolver's refusal denies, naming the three places looked.
// The receipt's `kits` picks the remedy (TOOL-dFairHearing-27 S13): `update` for a receipt claiming
// review-harness, else `apply`, since govkit's `update` refuses a kit its receipt does not claim; it is
// read a second time on the deny path alone. WHAT IT DOES NOT CHECK: that the pack is wired, which
// check-wiring.sh reports, or that it judges correctly, which its own suite does. A throw refuses.
// null = allow · string = deny.
function checkOptinPackPresent(data) {
  const path = require('path')
  const fs = require('fs')
  try {
    const a = data.tool_name === 'Workflow' ? loadScratchGuard().extractWorkflowArgs(data) : null
    if (!a || (String(a.kind) !== 'spec-audit' && a.specAudit === undefined)) return null
    let refusal
    try { resolveKitDir('workflows', 'spec-audit-optin.js', __dirname); return null } catch (e) { refusal = e }
    let receipt = null
    try { receipt = JSON.parse(fs.readFileSync(refusal.receipt, 'utf8')) } catch { receipt = null }
    const claimed = !!receipt && Array.isArray(receipt.kits) && receipt.kits.includes('review-harness')
    const kits = path.dirname(__dirname)
    const renderRel = (f) => path.relative(process.env.CLAUDE_PROJECT_DIR || process.cwd(), f).split(path.sep).join('/')
    return `BLOCKED by spawn-guard: this Workflow call is a spec audit, and the spec-audit opt-in pack was not found: ` +
      `${refusal.message}. The opt-in moved to the review kit (TOOL-dFairHearing-16), ` +
      `and a hook landed without its pack does not admit an audit nobody judged.\n` +
      `Install the pack: govkit ${claimed ? 'update' : 'apply'} --kits review-harness, or wire a hand copy with ` +
      `python ${renderRel(path.join(kits, 'settings-merge.py'))} --fragment ${renderRel(path.join(kits, 'workflows', 'spec-audit-optin.fragment.json'))}.\n`
  } catch (e) {
    return `BLOCKED by spawn-guard: the spec-audit pack check (TOOL-dFairHearing-22) threw (${(e && e.message) || e}), and a rule that cannot finish does not admit.\n`
  }
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
