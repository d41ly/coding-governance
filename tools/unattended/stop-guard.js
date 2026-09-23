#!/usr/bin/env node
/**
 * stop-guard — a `Stop` hook that refuses the turn end of a session bound to a non-terminal
 * unattended run, and continues the conversation with the absent-owner instruction instead.
 *
 * gov:kit unattended@1.31 — a courtesy marker; the kit version gate pairs the four named `.sh`
 * carriers and every `*.template.md`, and does not read this one.
 *
 * Contract: the spec for TOOL-aWokenSentinel-3 under the build folder of that slug.
 *
 * WHY THIS IS A HOOK. Four of six recorded stalls are class E: the run parked and ended its turn to
 * wait for an owner who had left, and nothing saw that act. The rule ("never end the turn by
 * asking") sits in the protocol, the Skill and the build method, and a run inside a compacted
 * context still types the question. The `Stop` event is the one surface that sees the decision
 * to end the turn, and a hook there can refuse it (research record, section 6: a
 * `{"decision":"block","reason":…}` on exit 0 reaches the model as `Stop hook feedback:`).
 *
 * THE KEY. The payload's `session_id` against the `session:` fact of every run-state record under
 * `<MEMORY_ROOT>/builds/<slug>/RUN.md` (run-lease.js). No record binds: exit 0, nothing written,
 * which is every session on the node that holds no run — one directory listing and one small read
 * per build folder, no spawn. A record with no `session:` fact keys nothing, so every run
 * preflighted before TOOL-aWokenSentinel-1 landed is invisible until `--resume --keepalive-id`
 * re-records its lease: the hook lands DARK for the run that builds it.
 *
 * THE DECISION on a bound session, in this order (spec §4 table, amended by TOOL-aWokenSentinel-8):
 *   verdict TERMINAL              allow   `terminal`
 *   no verdict, non-zero exit,
 *     or the liveness bound       allow   `liveness-unreadable`
 *   background_tasks non-empty    allow   `background-tasks` — the harness re-invokes the session
 *                                         when a task completes; a block there is a wasted turn
 *   STOP_GUARD_BLOCKS malformed   allow   `knob-malformed`
 *   blocks so far >= the knob     allow   `blocks-exhausted`
 *   verdict FINISHED-UNSTAMPED    BLOCK   `landing-unstamped` — the one act left is `--landed`
 *   otherwise                     BLOCK   `run-open`
 * The verdict comes from `bash <this dir>/unattended.sh --liveness <slug>`, run with cwd at the
 * repo root and bounded at LIVENESS_BOUND_MS; this hook reads no mtime, transcript or git of its
 * own. `stop_hook_active` changes nothing but the reason text, which says so.
 *
 * WHY `landing-unstamped` BLOCKS. `--landed` runs after the lander, so its refusals fire when the
 * witness is already on `origin/<default>` and `--liveness` reads FINISHED-UNSTAMPED; each refusal
 * ends the turn on the promise that this hook records the harness's cron listing and continues
 * the session. An allow here is the wedge the aWokenSentinel spec-audit's B1 names: the turn ends,
 * nothing resumes the session, and the record sits at LANDING with its work on `main`. A bound
 * session at that verdict is therefore blocked, under the same cap as `run-open`, and told that
 * `--landed` is the one act left — never `--plan` or `--abort`, because a finished run has no unit
 * to build and nothing to abort. An UNBOUND record at LANDING never reaches this table: every
 * pre-unit-1 record in the tree keeps ending its turns silently, by construction of the key.
 *
 * TWO BOUNDS, SIDE BY SIDE. The HARNESS ends a turn after 8 consecutive stop-hook blocks
 * (HARNESS_CONSECUTIVE_CAP, measured in the aReplayedCard orientation record cited beside it), so
 * inside one turn no knob above 8 is reachable. THE HOOK bounds the session's LIFETIME blocks:
 * the count is derived from the sidecar and persists across resumes, so BLOCKS_DEFAULT = 6 sits
 * below the harness cap and the hook's ANNOUNCED exhaustion — a sidecar line and a reason naming
 * `--abort` — precedes the harness's silent one.
 *
 * THE KNOB diverges from the driver's `read_bound_key` in ONE way: a declared value that is not a
 * positive integer ALLOWS with reason `knob-malformed` and one stderr line. The driver exits 2 on
 * the same input, which is right for a verb; for a `Stop` hook exit 2 is a BLOCK, so the driver's
 * shape would turn a conf typo into a session that cannot end its turn (spec §8 F4).
 *
 * THE SIDECAR. Every stop on a bound session, allowed or blocked, appends one compact JSON line to
 * `<git-dir>/unattended/stop.<slug>.log` carrying the payload's `session_crons` VERBATIM — the
 * harness's own listing of the cron store no script can reach, which is what `--landed` checks
 * `keepalive-reaped` against (TOOL-aWokenSentinel-7). The block count is derived from that file
 * and from nothing else. An UNWRITABLE sidecar allows with `sidecar-unwritable` on stderr: a
 * bound the hook cannot derive is a bound it cannot enforce, and a hook that blocks without one
 * loops.
 *
 * WHAT THIS DOES NOT CHECK. It does not fire for a sub-agent (`Stop` is the main agent's event;
 * a payload carrying `agent_id`, or any event but `Stop`, exits 0 silently). It does not grade the
 * run's units, does not know what the session is doing, and cannot tell a healthy long bar from a
 * hung one — that is `--liveness`'s STALE verdict and the process-monitor kit. It does not prove
 * it is WIRED: the adopter's `--check` and `check-hook-destinations.sh` own that. A broken hook
 * never blocks a stop — every failure path is an allow, and an uncaught error exits 0.
 */
'use strict'

const path = require('path')
const { spawnSync } = require('child_process')
const lease = require(path.join(__dirname, 'run-lease.js'))

const KIT_STOP_GUARD_VERSION = '1.0'
const KNOB = 'STOP_GUARD_BLOCKS'
// The harness ends a turn after this many CONSECUTIVE stop-hook blocks. Measured, not chosen:
// memory/builds/aReplayedCard/build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md:299,
// verdicts 8 and 22 against the hooks documentation. A default above it promises blocks a single
// turn can never deliver.
const HARNESS_CONSECUTIVE_CAP = 8
// Two under the harness cap, so the hook's announced exhaustion precedes the harness's silent one.
const BLOCKS_DEFAULT = 6
// The driver's startup is seconds; sixty is the ceiling past which a hung liveness reads as
// unreadable and allows. STOP_GUARD_LIVENESS_BOUND_MS overrides it — the fixture's seam.
const LIVENESS_BOUND_MS = 60000
const REASONS = ['terminal', 'liveness-unreadable', 'background-tasks', 'knob-malformed',
                 'blocks-exhausted', 'landing-unstamped', 'run-open']

/**
 * `bash <kitDir>/unattended.sh --liveness <slug>` with cwd at the root, because the driver sources
 * the conf of the tree it runs in; the driver path is forward-slashed because MSYS mangles a
 * backslash path handed to a shell (charter §11). Returns `{stdout, ok}` where `ok` is a zero exit
 * within the bound; a spawn error, a non-zero exit or the bound is `ok: false`.
 */
function runLiveness(kitDir, root, slug) {
  const driver = path.join(kitDir, 'unattended.sh').replace(/\\/g, '/')
  const bound = Number(process.env.STOP_GUARD_LIVENESS_BOUND_MS) > 0
    ? Number(process.env.STOP_GUARD_LIVENESS_BOUND_MS) : LIVENESS_BOUND_MS
  const r = spawnSync('bash', [driver, '--liveness', slug],
                      { cwd: root, encoding: 'utf8', timeout: bound, killSignal: 'SIGKILL',
                        stdio: ['ignore', 'pipe', 'pipe'], windowsHide: true })
  return { stdout: r.stdout || '', ok: !r.error && r.status === 0 }
}

/** `{verdict, phase}` from the driver's `key: value` lines; null when no `verdict:` line exists. */
function parseLiveness(stdout) {
  const read = (key) => {
    const m = new RegExp('^' + key + ':[ \\t]*(.*)$', 'm').exec(stdout)
    return m ? m[1].replace(/\r$/, '').trim() : ''
  }
  const verdict = read('verdict')
  if (!verdict) return null
  return { verdict, phase: read('phase') || 'unknown' }
}

/** The block count for this session: lines of the sidecar with its `session` and decision `block`. */
function measureBlocks(sidecar, sessionId) {
  return lease.readSidecarLines(sidecar)
    .filter((l) => l && l.session === sessionId && l.decision === 'block').length
}

/**
 * The §4 table over `{liveness, backgroundTasks, knob, blocks}`: `{decision, reason}`. `liveness`
 * is parseLiveness's result or null; `knob` is readBoundKey's `{value, source}`; `blocks` is the
 * count BEFORE this stop.
 */
function checkStop(liveness, backgroundTasks, knob, blocks) {
  if (!liveness) return { decision: 'allow', reason: 'liveness-unreadable' }
  if (liveness.verdict === 'TERMINAL') return { decision: 'allow', reason: 'terminal' }
  if (backgroundTasks > 0) return { decision: 'allow', reason: 'background-tasks' }
  if (knob.source === 'malformed') return { decision: 'allow', reason: 'knob-malformed' }
  if (blocks >= knob.value) return { decision: 'allow', reason: 'blocks-exhausted' }
  if (liveness.verdict === 'FINISHED-UNSTAMPED') return { decision: 'block', reason: 'landing-unstamped' }
  return { decision: 'block', reason: 'run-open' }
}

/** The reason text the model reads under `Stop hook feedback:`, selected by the block's reason class. */
function renderBlock(reason, slug, phase, verdict, n, total, kitRel, stopHookActive) {
  let text = reason === 'landing-unstamped'
    ? `stop-guard: this session holds unattended run ${slug}, phase ${phase}, and its witness is already ` +
      'on the default branch, so the run is finished and unstamped; ' +
      `block ${n}/${total}. The stop-guard has just recorded the harness's cron listing. ` +
      `Run \`bash ${kitRel}/unattended.sh --landed ${slug}\` now: it reads that listing against the ` +
      'recorded keepalive id and stamps LANDED, or names the reap still owed. Never end the turn by asking.'
    : `stop-guard: this session holds unattended run ${slug}, phase ${phase}, liveness ${verdict}; ` +
      `block ${n}/${total}. The owner is absent. Run \`bash ${kitRel}/unattended.sh --plan ${slug}\` ` +
      'and build the next READY unit, or ' +
      `\`bash ${kitRel}/unattended.sh --abort ${slug} --reason <text> --code <halt-code>\` if the run ` +
      'cannot proceed. Never end the turn by asking: there is nobody to answer, and a question is a stall.'
  if (stopHookActive) text += ' This is a continuation the hook already blocked once.'
  return text
}

function main() {
  let data
  try {
    data = JSON.parse(lease.readStdin())
  } catch {
    process.exit(0)
  }
  if (!data || data.hook_event_name !== 'Stop' || data.agent_id) process.exit(0)
  const sessionId = typeof data.session_id === 'string' ? data.session_id : ''
  if (!sessionId) process.exit(0)
  // Wrapped because a guard that THROWS is worse than one that misses: an uncaught error exits 1,
  // which the harness reads as a non-blocking failure and surfaces as noise. Fail open.
  let block = null
  try {
    block = checkSession(data, sessionId)
  } catch {
    process.exit(0)
  }
  if (block) process.stdout.write(JSON.stringify({ decision: 'block', reason: block }))
  process.exit(0)
}

/** The whole decision for one payload; the first block's reason text, or null to allow. */
function checkSession(data, sessionId) {
  const cwd = data.cwd || process.env.CLAUDE_PROJECT_DIR || process.cwd()
  const repo = lease.resolveRepo(cwd)
  if (!repo) return null
  const memoryRoot = lease.readMemoryRoot(repo.root)
  if (!memoryRoot) return null
  const leases = lease.resolveLease(repo.root, memoryRoot, sessionId)
  if (leases.length === 0) return null
  const tasks = Array.isArray(data.background_tasks) ? data.background_tasks.length : 0
  const active = data.stop_hook_active === true
  const knob = lease.readBoundKey(repo.root, KNOB, BLOCKS_DEFAULT)
  if (knob.source === 'default') {
    process.stderr.write(`unattended: NOTE - this project declares no ${KNOB}, so a bound session is ` +
      `blocked at most ${BLOCKS_DEFAULT} times per run and session. Declare one in ${lease.CONF_BASENAME} to change it.\n`)
  } else if (knob.source === 'malformed') {
    process.stderr.write(`stop-guard: ${KNOB} is declared as '${knob.raw}', which is not a positive integer, ` +
      'so this stop is allowed with reason knob-malformed rather than refused — a conf typo must not ' +
      'become a session that cannot end its turn.\n')
  }
  const kitRel = path.relative(repo.root, __dirname).replace(/\\/g, '/') || '.'
  let first = null
  // Two records claiming one session cannot come from the driver; a hand-edited tree that produces
  // them is read whole, and the first that is open is the one named.
  for (const l of leases) {
    const sidecar = lease.deriveSidecarPath(repo.gitDir, 'stop', l.slug)
    const run = runLiveness(__dirname, repo.root, l.slug)
    const liveness = run.ok ? parseLiveness(run.stdout) : null
    const before = measureBlocks(sidecar, sessionId)
    const verdict = checkStop(liveness, tasks, knob, before)
    const blocks = verdict.decision === 'block' ? before + 1 : before
    const line = {
      utc: lease.renderUtc(), session: sessionId, decision: verdict.decision, reason: verdict.reason,
      phase: liveness ? liveness.phase : 'unknown', verdict: liveness ? liveness.verdict : 'unreadable',
      blocks, background_tasks: tasks, stop_hook_active: active,
      session_crons: data.session_crons === undefined ? null : data.session_crons,
    }
    try {
      lease.writeSidecarLine(sidecar, JSON.stringify(line))
    } catch (e) {
      process.stderr.write(`stop-guard: sidecar-unwritable — ${sidecar}: ${e && e.message ? e.message : e}; ` +
        'this stop is allowed because a bound the hook cannot derive is a bound it cannot enforce.\n')
      continue
    }
    if (verdict.decision === 'block' && first === null) {
      first = renderBlock(verdict.reason, l.slug, line.phase, line.verdict, blocks, knob.value, kitRel, active)
    }
  }
  return first
}

if (require.main === module) main()
module.exports = {
  runLiveness, parseLiveness, measureBlocks, checkStop, renderBlock, checkSession, main,
  KIT_STOP_GUARD_VERSION, BLOCKS_DEFAULT, HARNESS_CONSECUTIVE_CAP, LIVENESS_BOUND_MS, REASONS, KNOB,
}
