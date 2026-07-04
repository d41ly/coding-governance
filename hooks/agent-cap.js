#!/usr/bin/env node
/**
 * agent-cap — project-agnostic PreToolUse guard against unbounded Workflow fan-out.
 *
 * WHY: `Workflow` `parallel()` / `pipeline()` fan out to the harness cap
 * (min(16, cores-2) ≈ 14). Large concurrent agent bursts saturate server
 * throughput and trip the SERVER rate limiter — killing whole review phases
 * and burning millions of subagent tokens for zero output. That cap is NOT
 * lowerable from userland, and workflow sidechains don't run hooks — so the
 * only preventive lever is to scan the Workflow *tool call* (a main-loop call
 * that DOES fire PreToolUse) and reject scripts that use the raw fan-out
 * primitives instead of the capped helpers.
 *
 * CONTRACT: route ALL fan-out through boundedParallel(thunks, CAP) /
 * boundedPipeline(items, CAP, ...stages). The sanctioned helper bodies are the
 * ONLY place a raw `parallel(`/`pipeline(` may appear, and each such line
 * carries a `gov:bounded-fanout` marker. Any other raw primitive call = deny.
 *
 * CAP: default 4 (override with env AGENT_CAP). This guard doesn't verify the
 * numeric arg — it enforces "use the helper"; the helper is where CAP lives.
 *
 * Wiring (per project): merge into the discovered settings.json —
 *   "hooks": { "PreToolUse": [ { "matcher": "Workflow",
 *     "hooks": [ { "type": "command",
 *       "command": "node \"${CLAUDE_PROJECT_DIR}/<path>/agent-cap.js\"" } ] } ] }
 * Blocks via exit 2 + stderr (version-robust; no JSON-schema dependency).
 *
 * ponytail: a static scan can't prove a dynamically-built array is ≤CAP — this
 * enforces "use the helper", killing the exact `parallel(items.map(...))`
 * pattern that causes the bursts. Ceiling: only line comments are stripped
 * before the scan, not block comments that mention the primitive.
 */
'use strict'

const CAP = Number(process.env.AGENT_CAP) || 4

function readStdin() {
  try {
    return require('fs').readFileSync(0, 'utf8')
  } catch {
    return ''
  }
}

function offendingLines(script) {
  // Case-sensitive: primitives are lowercase `parallel`/`pipeline`; the helpers
  // are `boundedParallel`/`boundedPipeline` (capital P) so they never match.
  // Lookbehind rejects `.parallel(` / `xparallel(` member/identifier hits.
  const raw = /(?<![.\w$])(parallel|pipeline)\s*\(/
  return script
    .split(/\r?\n/)
    .map((line, i) => ({ line, n: i + 1 }))
    .filter(({ line }) => {
      if (line.includes('gov:bounded-fanout')) return false // sanctioned helper line
      const code = line.split('//')[0] // drop line-comments
      return raw.test(code)
    })
}

function main() {
  let data
  try {
    data = JSON.parse(readStdin())
  } catch {
    process.exit(0)
  }
  if (!data || data.tool_name !== 'Workflow') process.exit(0)

  const script = (data.tool_input && data.tool_input.script) || ''
  if (!script) process.exit(0) // scriptPath / saved-name runs: nothing to scan

  const bad = offendingLines(script)
  if (bad.length === 0) process.exit(0)

  const shown = bad
    .slice(0, 6)
    .map(({ n, line }) => `  L${n}: ${line.trim()}`)
    .join('\n')
  process.stderr.write(
    `BLOCKED by agent-cap: raw parallel()/pipeline() fans out to the harness ` +
      `cap (~14 agents) and trips the server rate limiter.\n\n` +
      `Route ALL fan-out through the cap-${CAP} helpers and call them instead:\n` +
      `  async function boundedParallel(thunks, cap = ${CAP}) {\n` +
      `    const out = []\n` +
      `    for (let i = 0; i < thunks.length; i += cap)\n` +
      `      out.push(...await parallel(thunks.slice(i, i + cap))) // gov:bounded-fanout\n` +
      `    return out\n` +
      `  }\n` +
      `  async function boundedPipeline(items, cap, ...stages) {\n` +
      `    const out = []\n` +
      `    for (let i = 0; i < items.length; i += cap)\n` +
      `      out.push(...await pipeline(items.slice(i, i + cap), ...stages)) // gov:bounded-fanout\n` +
      `    return out\n` +
      `  }\n\n` +
      `Consolidate before fanning: batch skeptics/items so total agents stay low.\n` +
      `Offending line(s):\n` +
      shown +
      `\n`,
  )
  process.exit(2)
}

main()
