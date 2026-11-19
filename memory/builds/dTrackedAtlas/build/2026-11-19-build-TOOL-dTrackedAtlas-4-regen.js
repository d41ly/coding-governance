// **Serves:** research TOOL-dTrackedAtlas-4
/**
 * regen — the Closed Loop Atlas page regenerates on node d after `main` moves, with no command typed for it.
 *
 * Contract: memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md
 *
 * ONE FILE, TWO MODES.
 *   no argument -> the PostToolUse hook `.claude/settings.json` runs after every Bash and PowerShell
 *                  tool call. It reads the conf, stats the page's folder and the stamp, and only when
 *                  the throttle window has passed writes the stamp and starts the runner detached.
 *                  It starts no other process, never reads `.git`, and every path through it exits 0.
 *   --run       -> the runner. Under a lock it reads the tip of refs/remotes/origin/main, asks the
 *                  generator's `--check --page` whether the page is current at that tip, and when it
 *                  is not, regenerates the page in a scratch checkout of the tip, checks the result
 *                  and renames it over the page.
 *
 * THE SWITCH lives in the conf beside this file, `2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json`:
 *   "atlas.regenerate": "on" (the default, also when the key is missing) or "off". Any other value
 *                       skips, and the log names it: deny by default.
 *   "atlas.page":       the page, an absolute path ending in `.html` with no `..` segment. Its folder
 *                       is never created; a node without it does nothing, and says so on a lander call.
 * To switch off, set "atlas.regenerate" to "off" in the conf: an uncommitted edit turns it off for that
 * checkout alone, a landed one for every checkout carrying it. A line opening with `//` is a comment.
 *
 * THE SIDECARS, every one in the page's folder, for a page <folder>/<stem>.html:
 *   <stem>.regen.stamp      the fast path's throttle stamp, written at each runner start
 *   <stem>.regen.lock       the runner's lock, held for its lifetime
 *   <stem>.regen.tip        the tip the runner last handled; delete it to have the present tip handled again
 *   <stem>.regen.log        one line per handled tip: `<UTC time> <tip12> <outcome> — <why>`
 *   <stem>.regen-<pid>.html the generator's temp page, renamed over the page or deleted
 *   regen-<pid>/            the scratch checkout, removed in every case
 *
 * It never commits, pushes or fetches. The one write outside the page's folder is git's admin entry for
 * the scratch checkout, which `git worktree remove` deletes.
 */
'use strict'

const { spawn } = require('child_process')
const fs = require('fs')
const path = require('path')

const CONF_NAME = '2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json'
const SWITCH = 'atlas.regenerate'
const PAGE_KEY = 'atlas.page'
const ALLOWED = ['on', 'off']
const DEFAULT = 'on'
const TIP_REF = 'refs/remotes/origin/main'
const GENERATOR = 'memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py'
const THROTTLE_S = 60
const GIT_BOUND_S = 300
const CHECK_BOUND_S = 300
const GEN_BOUND_S = 1500
const RUN_BOUND_S = 2400
const ROUNDS = 3
// The family tools/run-gates/post-merge.sh drops before its first git call: under a hook they point git
// at the caller's repository.
const SCRUB = ['GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_COMMON_DIR', 'GIT_OBJECT_DIRECTORY',
  'GIT_ALTERNATE_OBJECT_DIRECTORIES', 'GIT_NAMESPACE', 'GIT_PREFIX']

// What the run-bound timer needs to reach: the child it kills, the tip it names, the sidecars it clears.
const runState = { child: null, key: 'unresolved', paths: null, locked: false }

function readInput() {
  try {
    return JSON.parse(fs.readFileSync(0, 'utf8') || '{}')
  } catch {
    return {}
  }
}

/** `{regenerate, page}` from the conf beside this file, or null when it is absent, does not parse, or
 * names no usable page. Whole-line `//` comments are dropped first: the conf carries its record binding. */
function readConf() {
  try {
    const text = fs.readFileSync(path.join(__dirname, CONF_NAME), 'utf8')
    const conf = JSON.parse(text.split(/\r?\n/).filter((line) => !/^\s*\/\//.test(line)).join('\n'))
    if (!conf || typeof conf !== 'object' || Array.isArray(conf)) return null
    const page = conf[PAGE_KEY]
    if (typeof page !== 'string' || !path.isAbsolute(page) || !/[^\\/]\.html$/.test(page)) return null
    if (page.split(/[\\/]/).includes('..')) return null
    return { regenerate: SWITCH in conf ? conf[SWITCH] : DEFAULT, page }
  } catch {
    return null
  }
}

/** The six paths of the page's folder, the pid's two included, beside the folder and the page. */
function deriveSidecars(page) {
  const folder = path.dirname(page)
  const stem = path.basename(page, '.html')
  return {
    folder,
    page,
    stamp: path.join(folder, `${stem}.regen.stamp`),
    lock: path.join(folder, `${stem}.regen.lock`),
    tip: path.join(folder, `${stem}.regen.tip`),
    log: path.join(folder, `${stem}.regen.log`),
    temp: path.join(folder, `${stem}.regen-${process.pid}.html`),
    scratch: path.join(folder, `regen-${process.pid}`),
  }
}

function checkFolder(folder) {
  try {
    return fs.statSync(folder).isDirectory()
  } catch {
    return false
  }
}

function renderNoHomeLine(folder) {
  return `atlas-regen: nothing done — no page home at ${folder} on this node`
}

/** The fast path. Returns 0 on every path: a fault here may never block a tool call. */
function runHook(input) {
  try {
    const conf = readConf()
    if (!conf) return 0
    const paths = deriveSidecars(conf.page)
    if (!checkFolder(paths.folder)) {
      const cmd = input && input.tool_input && input.tool_input.command
      if (typeof cmd === 'string' && cmd.includes('push-main.sh')) console.log(renderNoHomeLine(paths.folder))
      return 0
    }
    try {
      if ((Date.now() - fs.statSync(paths.stamp).mtimeMs) / 1000 < THROTTLE_S) return 0
    } catch {
      // no stamp yet: the first start is never throttled
    }
    // Written BEFORE the start: a runner that crashes is retried once per window, never once per call.
    fs.writeFileSync(paths.stamp, `${new Date().toISOString()}\n`)
    const child = spawn(process.execPath, [__filename, '--run'], { detached: true, stdio: 'ignore', windowsHide: true })
    child.on('error', () => {})
    child.unref()
  } catch {
    // fail open
  }
  return 0
}

/** Run one child under a bound: `{status, stdout, stderr, timedOut}`, status null when it could not start
 * or was killed. A killed child answers at once, without waiting on pipes a grandchild may hold open. */
function runChild(cmd, args, cwd, boundS) {
  return new Promise((resolve) => {
    const out = []
    const err = []
    let settled = false
    let timer = null
    function setAnswer(answer) {
      if (settled) return
      settled = true
      clearTimeout(timer)
      if (runState.child === child) runState.child = null
      resolve(answer)
    }
    let child
    try {
      child = spawn(cmd, args, { cwd, windowsHide: true, stdio: ['ignore', 'pipe', 'pipe'] })
    } catch (e) {
      setAnswer({ status: null, stdout: '', stderr: String(e.message), timedOut: false })
      return
    }
    runState.child = child
    child.stdout.on('data', (b) => out.push(b))
    child.stderr.on('data', (b) => err.push(b))
    child.on('error', (e) => setAnswer({ status: null, stdout: '', stderr: `${cmd} did not start: ${e.message}`, timedOut: false }))
    child.on('close', (status) => setAnswer({
      status, stdout: Buffer.concat(out).toString('utf8'), stderr: Buffer.concat(err).toString('utf8'), timedOut: false,
    }))
    timer = setTimeout(() => {
      try { child.kill() } catch { /* already gone */ }
      setAnswer({ status: null, stdout: Buffer.concat(out).toString('utf8'), stderr: '', timedOut: true })
    }, boundS * 1000)
  })
}

function extractFirstLine(text) {
  return (String(text || '').split(/\r?\n/).find((line) => line.trim()) || '').trim()
}

/** A child's answer in one line: its first stderr line, else its first stdout line, else its exit. */
function renderAnswer(answer, boundS) {
  if (answer.timedOut) return `no answer within ${boundS} s`
  return extractFirstLine(answer.stderr) || extractFirstLine(answer.stdout) || `exit ${answer.status}`
}

function writeLog(paths, text) {
  fs.appendFileSync(paths.log, `${new Date().toISOString()} ${text.replace(/[\r\n]+/g, ' ')}\n`)
}

function readTipSidecar(paths) {
  try {
    return fs.readFileSync(paths.tip, 'utf8').trim()
  } catch {
    return ''
  }
}

/** Take the lock, or answer false when a live runner holds it. A lock older than RUN_BOUND_S belongs to a
 * runner that died: it is removed, logged, and taken. */
function writeLock(paths) {
  for (let attempt = 0; attempt < 2; attempt += 1) {
    try {
      const fd = fs.openSync(paths.lock, 'wx')
      fs.writeSync(fd, `${process.pid} ${new Date().toISOString()}\n`)
      fs.closeSync(fd)
      runState.locked = true
      return true
    } catch (e) {
      if (e.code !== 'EEXIST' || attempt) return false
      let age
      try {
        age = (Date.now() - fs.statSync(paths.lock).mtimeMs) / 1000
      } catch {
        continue // released between the open and the stat: try once more
      }
      if (age < RUN_BOUND_S) return false
      fs.rmSync(paths.lock, { force: true })
      writeLog(paths, `stale lock removed — ${Math.round(age)} s old`)
    }
  }
  return false
}

function removeLock(paths) {
  if (!runState.locked) return
  runState.locked = false
  try { fs.rmSync(paths.lock, { force: true }) } catch { /* the next runner reads it as stale */ }
}

/** Remove one scratch checkout: git's own removal, then whatever it left, then git's admin entry. */
async function removeScratch(root, dir) {
  await runChild('git', ['worktree', 'remove', '--force', dir], root, GIT_BOUND_S)
  try { fs.rmSync(dir, { recursive: true, force: true }) } catch { /* the next runner's leftovers pass */ }
  await runChild('git', ['worktree', 'prune'], root, GIT_BOUND_S)
}

/** Every `regen-<digits>` folder a killed runner left in the page's folder. Never a link, never another name. */
async function removeLeftovers(root, folder) {
  const left = fs.readdirSync(folder, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && /^regen-\d+$/.test(entry.name))
  for (const entry of left) await removeScratch(root, path.join(folder, entry.name))
}

async function resolvePython(root) {
  const answer = await runChild('bash', ['-c', '. tools/lib/resolve-python.sh && resolve_python'], root, GIT_BOUND_S)
  return answer.status === 0 ? extractFirstLine(answer.stdout) : ''
}

/** Regenerate the page at `tip` in a scratch checkout: `{outcome, why}`, the page left as it was on failure. */
async function runRegeneration(root, tip, py, paths) {
  const started = Date.now()
  let step = 'git worktree add'
  let answer = null
  let bound = GIT_BOUND_S
  try {
    answer = await runChild('git', ['worktree', 'add', '--detach', paths.scratch, tip], root, bound)
    if (answer.status !== 0) return { outcome: 'failed', why: `${step} — ${renderAnswer(answer, bound)}` }
    const generator = path.join(paths.scratch, GENERATOR)
    step = 'generation'
    bound = GEN_BOUND_S
    answer = await runChild(py, [generator, '--out', paths.temp], paths.scratch, bound)
    if (answer.status !== 0 || !fs.existsSync(paths.temp)) {
      return { outcome: 'failed', why: `${step} — ${renderAnswer(answer, bound)}` }
    }
    step = 'check of the new page'
    bound = CHECK_BOUND_S
    answer = await runChild(py, [generator, '--check', '--page', paths.temp, '--ref', tip], paths.scratch, bound)
    if (answer.status !== 0 || !extractFirstLine(answer.stdout).startsWith('atlas: current')) {
      return { outcome: 'failed', why: `${step} — ${renderAnswer(answer, bound)}` }
    }
    step = 'rename'
    fs.renameSync(paths.temp, paths.page)
    const kb = Math.floor(fs.statSync(paths.page).size / 1024)
    return { outcome: 'regenerated', why: `in ${Math.round((Date.now() - started) / 1000)} s, ${kb} KB` }
  } catch (e) {
    return { outcome: 'failed', why: `${step} — ${extractFirstLine(e && e.message) || 'an error with no message'}` }
  } finally {
    try { fs.rmSync(paths.temp, { force: true }) } catch { /* nothing to delete */ }
    await removeScratch(root, paths.scratch)
  }
}

/** The run bound expired: kill the child, log, release the lock, exit 1. */
function runExpiry() {
  const { child, key, paths } = runState
  try { if (child) child.kill() } catch { /* already gone */ }
  try { writeLog(paths, `${key.slice(0, 12)} failed — no answer within ${RUN_BOUND_S} s`) } catch { /* the log is gone */ }
  try { fs.rmSync(paths.temp, { force: true }) } catch { /* nothing to delete */ }
  removeLock(paths)
  process.exit(1)
}

/** The runner: 0, or 1 when a regeneration in this run failed. */
async function runRunner() {
  for (const name of SCRUB) delete process.env[name]
  const conf = readConf()
  if (!conf) return 0
  const paths = deriveSidecars(conf.page)
  if (!checkFolder(paths.folder)) {
    console.log(renderNoHomeLine(paths.folder))
    return 0
  }
  const root = path.resolve(__dirname, '../../../..')
  if (!writeLock(paths)) return 0
  runState.paths = paths
  const timer = setTimeout(runExpiry, RUN_BOUND_S * 1000)
  let code = 0
  try {
    await removeLeftovers(root, paths.folder)
    let py = null
    for (let round = 0; round < ROUNDS; round += 1) {
      const answer = await runChild('git', ['rev-parse', '--verify', '-q', `${TIP_REF}^{commit}`], root, GIT_BOUND_S)
      const tip = extractFirstLine(answer.stdout)
      const key = answer.status === 0 && /^[0-9a-f]{40}([0-9a-f]{24})?$/.test(tip) ? tip : 'unresolved'
      if (readTipSidecar(paths) === key) break
      runState.key = key
      let result
      if (key === 'unresolved') {
        result = { outcome: 'failed', why: `${TIP_REF} does not resolve` }
      } else if (conf.regenerate === 'off') {
        result = { outcome: 'skipped', why: `${SWITCH} is off` }
      } else if (!ALLOWED.includes(conf.regenerate)) {
        result = { outcome: 'skipped', why: `${SWITCH} is '${String(conf.regenerate)}', outside ${ALLOWED.join(' ')}` }
      } else {
        if (py === null) py = await resolvePython(root)
        if (!py) {
          result = { outcome: 'failed', why: 'no python resolved' }
        } else {
          const check = await runChild(py, [path.join(root, GENERATOR), '--check', '--page', paths.page, '--ref', key],
            root, CHECK_BOUND_S)
          const first = extractFirstLine(check.stdout)
          if (check.status === 0 && first.startsWith('atlas: current')) {
            result = { outcome: 'current', why: first }
          } else {
            result = await runRegeneration(root, key, py, paths)
            result.why += `; the check answered ${renderAnswer({ ...check, stderr: '' }, CHECK_BOUND_S)}`
            if (result.outcome === 'failed') code = 1
          }
        }
      }
      writeLog(paths, `${key.slice(0, 12)} ${result.outcome} — ${result.why}`)
      fs.writeFileSync(paths.tip, `${key}\n`)
    }
  } finally {
    clearTimeout(timer)
    removeLock(paths)
  }
  return code
}

function main() {
  if (process.argv[2] === '--run') {
    runRunner().then(
      (code) => process.stdout.write('', () => process.exit(code)),
      () => process.stdout.write('', () => process.exit(1)),
    )
    return
  }
  process.exitCode = runHook(readInput())
}

if (require.main === module) main()
