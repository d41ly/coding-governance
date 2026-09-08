#!/usr/bin/env node
/**
 * procmon-hook — put the process monitor's verdict where a session actually reads it.
 *
 * gov:kit process-monitor@0.1
 *
 * Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-5.md
 *
 * WHY A HOOK AT ALL. The kit's report is a command, and a command nobody runs is the state this
 * whole fleet was in when the sweep found two spin loops 11.4 hours old. The verdict has to arrive
 * without being asked for.
 *
 * THREE DISTINGUISHABLE STATES, and keeping them apart is the point:
 *   nothing flagged      -> SILENT. A "0 flagged" line on every window is the noise that gets a
 *                           hook removed, and a removed hook reports nothing at all.
 *   something flagged    -> a short list, each row with its pid, verdict and age.
 *   the monitor is broken-> ONE line naming the failure. Never silence: "nothing flagged" and
 *                           "the probe could not run" are different facts and this is the file
 *                           where they would otherwise become the same one.
 *
 * THE THROTTLE CHECK IS ONE `stat` AND NOTHING ELSE. It runs on the overwhelming majority of tool
 * calls, so the early-exit path parses no conf, imports no python and spawns no census. A census
 * measured ~1.2s over a 320ms PowerShell floor; at the declared window that is a fraction of a
 * percent of a session's tool-call time, and paying it per call would not be.
 *
 * IT FAILS OPEN, ALWAYS. A monitoring fault may not block a tool call. Every path here exits 0.
 *
 * AND IT NEVER KILLS. Reporting and killing are separate authorities in this kit; the hook runs the
 * report path whatever `PROCMON_REAP_MODE` says.
 */
'use strict'

const { execFileSync } = require('child_process')
const fs = require('fs')
const path = require('path')

const DEFAULT_THROTTLE_S = 300
const CENSUS_BOUND_MS = 90000

function readInput() {
  try {
    return JSON.parse(fs.readFileSync(0, 'utf8') || '{}')
  } catch {
    return {}
  }
}

function resolveRoot() {
  const fromEnv = process.env.CLAUDE_PROJECT_DIR || process.env.PROCMON_ROOT
  if (fromEnv && fs.existsSync(path.join(fromEnv, '.process-monitor.conf'))) return fromEnv
  let dir = process.cwd()
  for (let i = 0; i < 12; i += 1) {
    if (fs.existsSync(path.join(dir, '.process-monitor.conf'))) return dir
    const up = path.dirname(dir)
    if (up === dir) break
    dir = up
  }
  return null
}

function readThrottleSeconds(root) {
  try {
    const text = fs.readFileSync(path.join(root, '.process-monitor.conf'), 'utf8')
    const hit = /^PROCMON_THROTTLE_S=\s*"?(\d+)"?/m.exec(text)
    return hit ? Number(hit[1]) : DEFAULT_THROTTLE_S
  } catch {
    return DEFAULT_THROTTLE_S
  }
}

/**
 * The stamp lives in the git COMMON dir, for the reason `.unattended.conf` records about its own
 * lander marker: in a linked worktree `.git` is a FILE, so a tree-relative path fails outright.
 * It also makes the window shared across concurrent sessions on one repo, which is correct — the
 * standing population is shared too, and N sessions should not each pay for a census of it.
 */
function resolveStamp(root) {
  try {
    const common = execFileSync('git', ['-C', root, 'rev-parse', '--git-common-dir'], {
      encoding: 'utf8',
      timeout: 10000,
    }).trim()
    const dir = path.isAbsolute(common) ? common : path.join(root, common)
    return path.join(dir, 'procmon-stamp')
  } catch {
    return null
  }
}

function checkThrottled(stamp, windowS) {
  try {
    const age = (Date.now() - fs.statSync(stamp).mtimeMs) / 1000
    return age < windowS
  } catch {
    return false // no stamp yet: this is the first run, and it must not be throttled
  }
}

function main() {
  const input = readInput()
  const sessionStart = input.hook_event_name === 'SessionStart'
  const root = resolveRoot()
  if (!root) return 0 // not adopted here; silence is correct

  const stamp = resolveStamp(root)
  const windowS = readThrottleSeconds(root)

  // SessionStart ignores the window deliberately: a fresh session inherits another session's stamp
  // and would otherwise report nothing, which is precisely how a two-day-old orphan goes unseen.
  if (!sessionStart && stamp && checkThrottled(stamp, windowS)) return 0

  // The stamp is written AFTER the work, not before it. Written first, a crashing hook throttles
  // itself out of ever running again and the silence reads exactly like a clean tree.
  let out = ''
  try {
    out = execFileSync(
      process.env.PROCMON_PYTHON || 'python',
      [path.join(root, 'tools', 'process-monitor', 'reap.py'), '--sweep', '--dry-run'],
      {
        cwd: root,
        encoding: 'utf8',
        timeout: CENSUS_BOUND_MS,
        env: { ...process.env, PROCMON_ROOT: root, PROCMON_REAP_MODE: 'report' },
      },
    )
  } catch (err) {
    const why = err && err.signal === 'SIGTERM' ? 'the census did not answer within its bound'
      : (err && (err.stderr || err.message) ? String(err.stderr || err.message).trim().split('\n')[0]
        : 'unknown failure')
    // A named failure, never silence, and never a non-zero exit.
    process.stdout.write(`process-monitor: could NOT run — ${why}\n`)
    writeStamp(stamp)
    return 0
  }
  writeStamp(stamp)

  const lines = out.split('\n').filter((l) => l.trim())
  const flagged = lines.filter((l) => /^(ORPHAN|SPIN|IDLE|UNKNOWN)\s/.test(l))
  if (!flagged.length) return 0 // SILENT on clean

  process.stdout.write(
    `process-monitor: ${flagged.length} process(es) past the declared ceiling and still running:\n`,
  )
  for (const l of flagged.slice(0, 8)) process.stdout.write(`  ${l}\n`)
  if (flagged.length > 8) process.stdout.write(`  ... and ${flagged.length - 8} more\n`)
  // DERIVED, never a literal: this kit sits wherever the adopter installed it, and a `tools/`
  // literal in shipped bytes prints a command that does not exist at another prefix.
  const rel = path.relative(root, path.join(__dirname, 'reap.py')).split(path.sep).join('/')
  process.stdout.write(
    `  reap them with: python ${rel} --sweep   (--dry-run to look first)\n`,
  )
  return 0
}

function writeStamp(stamp) {
  if (!stamp) return
  try {
    fs.mkdirSync(path.dirname(stamp), { recursive: true })
    fs.writeFileSync(stamp, String(Date.now()))
  } catch {
    /* a stamp we cannot write costs a repeated census, never a blocked tool call */
  }
}

process.exit(main())
