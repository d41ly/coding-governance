#!/usr/bin/env node
/**
 * stall-recorder — a `StopFailure` hook that writes an API-error stall of a session bound to an
 * unattended run to disk, at zero API cost, after the turn the API refused.
 *
 * gov:kit unattended@1.28 — a courtesy marker; the kit version gate pairs the four named `.sh`
 * carriers and every `*.template.md`, and does not read this one.
 *
 * Contract: the spec for TOOL-aWokenSentinel-4 under the build folder of that slug.
 *
 * WHY THIS IS A HOOK. A turn that ends on `rate_limit`, `overloaded`, `server_error` or
 * `max_output_tokens` leaves nothing on disk that names the run, and four Tier-2 reviews that died
 * on limits were found by a human reading a journal. `StopFailure` is the one surface that sees
 * the API refuse a turn, and the harness discards this event's output by documentation — so this
 * hook RECORDS and CANNOT BLOCK: nothing on stdout in any case, exit 0 in any case.
 *
 * THE KEY is run-lease.js's: the payload's `session_id` against the `session:` fact of every
 * run-state record under `<MEMORY_ROOT>/builds/<slug>/RUN.md`. No record binds: exit 0, nothing
 * written. A bound run gets ONE appended line in `<git-dir>/unattended/stall.<slug>.log`:
 *
 *   <utc> <session> <error-class-or-unknown> <the whole stdin JSON, compact>
 *
 * The first three fields are space-free by construction, so a reader that splits on the first
 * three spaces gets the payload whole; `--liveness` prints the LAST line verbatim as `last-stall:`.
 *
 * ONE FIELD IS ASSUMED, AND IT IS UNVERIFIED. The `StopFailure` stdin was never measured on this
 * fleet; the harness documentation shows an `error` field carrying the matcher value, inferred
 * from the page's pattern rather than quoted. The hook tries `error` and falls back to `unknown`,
 * and the whole compact payload rides the line for that reason: the first recorded stall is the
 * measurement, and a later reader parses what was actually handed over.
 *
 * WHAT THIS DOES NOT CHECK. It does not grade the run's phase, does not resume, notify or block,
 * and does not prove it is WIRED — the adopter's `--check` and `check-hook-destinations.sh` own
 * that. An unwritable sidecar prints one stderr sentence, which the harness discards, and exits 0;
 * an uncaught error exits 0. Every failure path is silence.
 */
'use strict'

const path = require('path')
const lease = require(path.join(__dirname, 'run-lease.js'))

const KIT_STALL_RECORDER_VERSION = '1.0'
const CLASS_UNKNOWN = 'unknown'

/**
 * The payload's `error` when it is a non-empty string, its whitespace folded to `-` so the class
 * stays one space-free field; `unknown` otherwise — absent, empty, or not a string at all.
 */
function extractErrorClass(data) {
  const e = data && data.error
  if (typeof e !== 'string' || !e.trim()) return CLASS_UNKNOWN
  return e.trim().replace(/\s+/g, '-')
}

function main() {
  let data
  try {
    data = JSON.parse(lease.readStdin())
  } catch {
    process.exit(0)
  }
  const sessionId = data && typeof data.session_id === 'string' ? data.session_id : ''
  if (!sessionId) process.exit(0)
  // Wrapped because a recorder that THROWS is noise on an event whose output is discarded anyway:
  // an uncaught error exits 1, which the harness surfaces as a hook error. Fail silent.
  try {
    const cwd = data.cwd || process.env.CLAUDE_PROJECT_DIR || process.cwd()
    const repo = lease.resolveRepo(cwd)
    if (!repo) process.exit(0)
    const memoryRoot = lease.readMemoryRoot(repo.root)
    if (!memoryRoot) process.exit(0)
    const leases = lease.resolveLease(repo.root, memoryRoot, sessionId)
    const cls = extractErrorClass(data)
    const line = `${lease.renderUtc()} ${sessionId} ${cls} ${JSON.stringify(data)}`
    // Two records claiming one session cannot come from the driver; a hand-edited tree that
    // produces them is recorded under each, the way stop-guard.js reads them all.
    for (const l of leases) {
      const sidecar = lease.deriveSidecarPath(repo.gitDir, 'stall', l.slug)
      try {
        lease.writeSidecarLine(sidecar, line)
      } catch (e) {
        process.stderr.write(`stall-recorder: sidecar-unwritable — ${sidecar}: ${e && e.message ? e.message : e}; ` +
          'the stall is not recorded, and this hook cannot block.\n')
      }
    }
  } catch {
    process.exit(0)
  }
  process.exit(0)
}

if (require.main === module) main()
module.exports = { extractErrorClass, main, KIT_STALL_RECORDER_VERSION, CLASS_UNKNOWN }
