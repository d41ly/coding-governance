// **Serves:** journal TOOL-aMendedFleet-73
//
// The vague-brief trial, run ONCE by the main loop as one Workflow call. P against S, five cells
// each, on the three-sentence brief in the journal beside this file; the decision rule is the spec's
// section 4 and the harness's `aggregate` verb, both fixed before this runs.
//
//   Workflow { scriptPath: '<this file>',
//              args: { repo: '<abs repo path>', root: '<short %TEMP% dir, e.g. C:/Users/x/AppData/Local/Temp/t73>',
//                      python: 'python' } }
//
// SIX STAGES: verify the suite and freeze it, a pilot for headroom, the two arms, decision probes over
// the blinded tools plus the exit-0 stub, blind scorers, document judges. Every agent's prompt OPENS
// with a `[t73:<tag>]` tag naming its cell or stage, which is how the harness's `tokens` verb joins
// usage to a cell; a prompt without one is an untagged agent and reds that verb.
//
// FAN-OUT goes only through `boundedParallel`, inlined from the tier-2 review harness because scripts
// cannot import, over array LITERALS of at most five; a stage that splits tools into groups fans over
// a literal of group numbers and does the picking inside the thunk, never by reshaping the receiver.
//
// AFTER IT RETURNS, the main loop runs `aggregate --collect <root>` and `tokens --session <id>`, then
// commits the rows and the trial report. This script writes nothing itself; its agents do.
//
// WHAT THIS DOES NOT CHECK: that an agent stayed inside its cell. The prompts forbid it and nothing
// enforces it; a cell that read another would show as correlated tools, which the report must look for.
export const meta = {
  name: 'trial-73',
  version: '1.0',
  description:
    'The vague-brief arm: P (plan then build) against S (Tier-2 spec, then a separate builder), five cells each, graded by a frozen hidden suite, blinded decision probes, blind scorers and document judges.',
  phases: [
    { title: 'Verify', detail: 'one agent re-tags the suite, makes the cells, freezes, runs the stub' },
    { title: 'Pilot', detail: 'one build from the vague brief, one grading run; stop above 0.8 intent' },
    { title: 'Arms', detail: 'five P cells, five S spec writers, five S builders; at most five at once' },
    { title: 'Probe', detail: 'at most four agents probe every blinded tool per decision row' },
    { title: 'Score', detail: 'at most two blind scorers, at most two document judges' },
  ],
}

async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap)
    out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout
  return out
}

let cfg = args
if (typeof cfg === 'string') cfg = JSON.parse(cfg)
if (!cfg || !cfg.repo || !cfg.root || !cfg.python) {
  throw new Error('trial-73: args must carry repo, root and python; none is defaulted')
}
const REPO = cfg.repo
const ROOT = cfg.root
const STEM = REPO + '/memory/builds/aMendedFleet/build/2026-10-06-build-TOOL-aMendedFleet-73-'
const HARNESS = cfg.python + ' ' + STEM + 'harness.py'
const JOURNAL = STEM + 'brief.md'
const SUITE = STEM + 'hidden-suite.py'

const P_CELLS = ['P1', 'P2', 'P3', 'P4', 'P5'] // gov:fixed-verifiers
const S_CELLS = ['S1', 'S2', 'S3', 'S4', 'S5'] // gov:fixed-verifiers
const PROBE_GROUPS = [0, 1, 2, 3] // gov:fixed-verifiers
const SCORERS = [0, 1] // gov:fixed-verifiers
const JUDGES = ['P', 'S'] // gov:fixed-verifiers

const OK = { type: 'object', required: ['ok', 'note'], properties: { ok: { type: 'boolean' }, note: { type: 'string' } } }
const GRADE = {
  type: 'object',
  required: ['pass', 'total', 'note'],
  properties: { pass: { type: 'integer' }, total: { type: 'integer' }, note: { type: 'string' } },
}
const CODES = { type: 'object', required: ['codes', 'note'], properties: { codes: { type: 'array', items: { type: 'string' } }, note: { type: 'string' } } }

const CELL_RULES =
  'Work ONLY inside your cell directory; read nothing outside it, and never read or search the repository at ' +
  REPO + ' or any other cell. Python 3.11+, standard library only, one file named declared.py at the cell root. ' +
  'You may write and run your own tests inside the cell. Commit your work in the cell repository with git when done. '

// ---- Stage 1: verify ----------------------------------------------------------------------------
phase('Verify')
const v = await agent(
  '[t73:verifier] You verify the hidden suite of a blinded trial before any tool exists. Read the FULL brief ' +
    '(section "The full brief it was cut from") and the vague brief in ' + JOURNAL + ', then the suite at ' + SUITE + '. ' +
    'A test named test_intent_* may assert only what the VAGUE brief\'s stated purpose implies, reached only through ' +
    'declared.py, kits.toml [[kit]] rows with name and path, and tools/. A test that asserts a spelling, exit code, file ' +
    'name or option only the FULL brief pins must be named test_contract_*. Rename any mis-tagged test by changing ' +
    'only its name; change no assertion. Then run, in order: `' + HARNESS + ' cells --root ' + ROOT + '`, `' + HARNESS +
    ' freeze`, `' + HARNESS + ' stub --root ' + ROOT + '`. Return ok=true only if all three exit 0; put every rename and ' +
    'the stub line in note.',
  { label: 'verifier', schema: OK },
)
if (!v || !v.ok) return { stopped: 'verify', note: (v && v.note) || 'the verifier returned nothing' }

// ---- Stage 2: pilot -----------------------------------------------------------------------------
phase('Pilot')
await agent(
  '[t73:pilot] Your cell is ' + ROOT + '/cells/pilot. Read brief.md there and build what it asks. Write no plan and ' +
    'no spec first: go straight to the code. ' + CELL_RULES,
  { label: 'pilot', schema: OK },
)
const pg = await agent(
  '[t73:runner-pilot] Run `' + HARNESS + ' hidden --root ' + ROOT + ' --cells pilot` and return the `intent` ' +
    'numbers it prints for cell pilot as pass and total. Change no file.',
  { label: 'runner-pilot', schema: GRADE },
)
if (!pg || !pg.total) return { stopped: 'pilot', note: 'the pilot was not graded' }
log('pilot intent ' + pg.pass + '/' + pg.total)
if (pg.pass * 5 > pg.total * 4) {
  return { stopped: 'headroom', note: 'pilot intent ' + pg.pass + '/' + pg.total + ' is above 0.8; the measure has no headroom' }
}

// ---- Stage 3: the arms --------------------------------------------------------------------------
phase('Arms')
await boundedParallel(
  P_CELLS.map((c) => () =>
    agent(
      '[t73:' + c + '] Your cell is ' + ROOT + '/cells/' + c + '. Read brief.md. FIRST write PLAN.md, at most 40 ' +
        'lines, deciding how the tool behaves, and commit it. THEN build declared.py from that plan. ' + CELL_RULES,
      { label: c, schema: OK },
    ),
  ),
)
await boundedParallel(
  S_CELLS.map((c) => () =>
    agent(
      '[t73:' + c + '-spec] Your cell is ' + ROOT + '/cells/' + c + '. Read brief.md and SPEC-FORMAT.md. Write ' +
        'SPEC.md: a Tier-2 spec of the tool brief.md asks for, following the skeleton in SPEC-FORMAT.md. Resolve every ' +
        'open question in its section 8 yourself, marking each RESOLVED with its reason. Write NO code. Commit SPEC.md. ' +
        CELL_RULES,
      { label: c + '-spec', schema: OK },
    ),
  ),
)
await boundedParallel(
  S_CELLS.map((c) => () =>
    agent(
      '[t73:' + c + '-build] Your cell is ' + ROOT + '/cells/' + c + '. Read SPEC.md and brief.md, then build ' +
        'declared.py as the spec says. Where you must diverge, FIRST bump the spec\'s rev with a section 9 line saying ' +
        'what moved and why, then change the code. ' + CELL_RULES,
      { label: c + '-build', schema: OK },
    ),
  ),
)
const blind = await agent(
  '[t73:runner-arms] Run `' + HARNESS + ' hidden --root ' + ROOT + '` and then `' + HARNESS + ' cells --blind --root ' +
    ROOT + '`. Return in codes the directory names under ' + ROOT + '/blind, sorted, and NOTHING about which cell ' +
    'each one is. Do not read blind-key.tsv. Put the hidden verb\'s per-cell lines in note.',
  { label: 'runner-arms', schema: CODES },
)
if (!blind || !blind.codes || blind.codes.length !== 11) {
  return { stopped: 'blind', note: 'expected 11 code names (10 tools and the stub), got ' + JSON.stringify(blind && blind.codes) }
}
const codes = blind.codes

// ---- Stage 4: decision probes -------------------------------------------------------------------
phase('Probe')
await boundedParallel(
  PROBE_GROUPS.map((g) => () =>
    agent(
      '[t73:probe' + (g + 1) + '] You probe command-line tools against a decision list. Read ONLY the section "The ' +
        'decision list" of ' + JOURNAL + '. Your tools are ' + ROOT + '/blind/<name>/declared.py for name in ' +
        JSON.stringify(codes.filter((x, i) => i % 4 === g)) + '. A directory with no declared.py is a missing tool: ' +
        'record that once for it. For each tool and EACH D row, discover the tool\'s own interface from its source and ' +
        '--help, build a fixture tree under ' + ROOT + '/fixtures/<name>/<D>, run it, and write to ' + ROOT +
        '/probes/<name>.md one section per D: the exact command, the fixture you built, and the observed exit status, ' +
        'stdout and stderr. Observe; do not judge. Never read ' + ROOT + '/blind-key.tsv, ' + ROOT + '/cells or ' + REPO +
        ' beyond that one section.',
      { label: 'probe' + (g + 1), schema: OK },
    ),
  ),
)

// ---- Stage 5 and 6: blind scorers, then document judges ----------------------------------------
phase('Score')
await boundedParallel(
  SCORERS.map((k) => () =>
    agent(
      '[t73:scorer' + (k + 1) + '] You score observations against a brief, blind. Read the full brief and the decision ' +
        'list in ' + JOURNAL + ', then ' + ROOT + '/probes/<name>.md for name in ' +
        JSON.stringify(codes.filter((x, i) => i % 2 === k)) + '. Read no tool source and nothing else. For every name ' +
        'and every D row write one line `<name>\\t<D>\\t<mark>` to ' + ROOT + '/scores/scorer' + (k + 1) + '.tsv, where ' +
        'mark is met (the observation shows the behaviour), unmet (it does not, or there is no observation) or ' +
        'contradicted (the tool does the opposite).',
      { label: 'scorer' + (k + 1), schema: OK },
    ),
  ),
)
await boundedParallel(
  JUDGES.map((arm) => () =>
    agent(
      '[t73:judge-' + arm + '] You judge design documents against a decision list. Read the full brief and the ' +
        'decision list in ' + JOURNAL + '. Then for each cell ' + arm + '1..' + arm + '5 read ' + ROOT + '/cells/<cell>/' +
        (arm === 'P' ? 'PLAN.md' : 'SPEC.md') + ' and nothing else in the cell. For every cell and every D row write one ' +
        'line `<cell>\\t<D>\\t<mark>` to ' + ROOT + '/judges/judge-' + arm + '.tsv, where mark is decided-compatible (the ' +
        'document decides it as the full brief does), decided-incompatible (it decides otherwise) or silent.',
      { label: 'judge-' + arm, schema: OK },
    ),
  ),
)

log('trial-73 complete: run aggregate --collect ' + ROOT + ' and tokens --session <this session> next')
return { stopped: '', note: 'all six stages ran; the main loop collects, aggregates and commits the record' }
