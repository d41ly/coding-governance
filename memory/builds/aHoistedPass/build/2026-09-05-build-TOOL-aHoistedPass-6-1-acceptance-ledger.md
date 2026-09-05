**Serves:** journal TOOL-aHoistedPass-6

# Acceptance ledger — TOOL-aHoistedPass-6

Tier-2 · node a · 2026-09-05 · spec rev-7

The harness stops driving the build. `tools/workflows/unattended-build.js` ends after SPEC, AUDIT and
a new whole-set DISPOSAL stage and returns the ordered roster; the run makes one main-loop `Workflow`
call per unit, which is a call the fan-out hook sees at all. `unattended.sh --plan <slug> --paths`
hands back the spec path that verb already resolved per unit and discarded.

**What is graded by nothing, and is not implied away.** Section 7 of the spec names it and this
ledger repeats it once: the two suites carrying every behavioural arm below are on NO gate leg.
`tools/workflows/unattended-build.test.sh` appears in no row of `tools/gate-legs.json`, and
`tools/unattended/unattended.test.sh`'s legs left the bar under the 2026-08-23 owner ruling. So AC4
through AC8, AC10 through AC14, AC17 and AC25 are observations THIS RUN made by executing both
suites by hand, and nothing standing re-checks them. Their exit codes are below.

## Acceptance criteria

**Evidences:** TOOL-aHoistedPass-6

- **AC1** — MET — `grep -c "label: 'build:"` returns `0`, and each of `label: 'spec:`,
  `label: 'audit:subjects:`, `label: 'audit:record:` and `label: 'dispose:` returns `1`. Four
  surviving `agent()` call sites, named rather than counted.
- **AC2** — MET — the five-alternative pattern returns `0`. It returned `5` at BASE.
- **AC2b** — MET, by reading each of the three survivors. The WHY block names MISSING and THIN as
  unconditional and marks the ORDER clause conditional on the unit *and the sibling ahead of it*
  carrying an `order` verb, with the `pass-order history` clause narrowed to a CLOSED unit whose
  build commit predates a conforming spec. Forced-shapes item 1 now reads `THE DISPOSAL STAGE IS ONE
  AGENT` and says DISPOSAL is the only stage the shape still applies to. Attended item 2 reads
  `--dispatch`'s SPEC-STATE AND ORDER REFUSAL with the same conditional marking.
- **AC3** — MET — `grep -c "BUILD_SCHEMA"` returns `0` and `grep -nE "^const (allIds|unbuilt|built|buildRoster|driverSteps) "` names no line. The
  tombstone comment above `DISPOSAL_SCHEMA` deliberately does not spell the identifier; rev-7's §9
  records why, and the unanchored grep is the stronger criterion because it also catches a stale
  `schema:` option pointing at a constant that is gone.
- **AC4** — MET — suite arm. On a CONVERGED verdict the trace carries no `agent:dispose:` entry and
  carries `disposal: skipped — the verdict is CONVERGED …`. Both halves, because an absence alone
  reads identically over a stage that was never written.
- **AC5** — MET — suite arms. With `{"disposed":false,"standing":["b1"],"summary":"x"}` the RESULT
  carries `"roster":[]`, a note beginning `DEGRADED — blockers were not disposed: b1`, and
  `agent:dispose:tB` is the LAST agent line in the trace. A second arm covers the dead-stage shape
  (`null`), which `d.disposed !== true` catches with the same branch.
- **AC6** — MET — suite arms, both exits. `CONVERGING` carries `"roster":[]`; attended mode with
  every unit terminal carries `"roster":[]` too. Neither carried the key before this change, and
  both arms were observed FAILING against the unchanged source (see AC17).
- **AC7** — MET — suite arm, asserting the roster WHOLE rather than by id:
  `"roster":[{"id":"A-tB-1","order":1,"specPath":"s1","briefPath":"b1"},{"id":"A-tB-2",…},{"id":"A-tB-3",…}]`
  — key set, key order, values and sequence in one comparison. `dispatch.scriptPath` is
  `tools/workflows/unattended-unit.js`, the path `TOOL-aHoistedPass-5` landed, and
  `dispatch.resolvePathsWith` ends `--plan tB --paths`.
- **AC8** — MET — suite arms over the sliced `dispatch` block: `repo`, `slug`, `driver` and
  `checklist` present with their exact values, `perUnit` exactly
  `["unitId","specPath","briefPath"]`, and no `"roster"` anywhere inside. The child receives its own
  unit and never the list.
- **AC9** — MET — `grep -c "renderRoster"` returns `3` (definition, the top-level call, the spec
  fan's per-group call). `python3 tools/codebase-map/test_codebase_map.py` exits `0` and
  `gen_map.py --check` exits `0`; no map artifact is in the diff.
- **AC10** — MET, by hand and against the REAL tree, twice and the second time better. First:
  `bash tools/unattended/unattended.sh --plan aHoistedPass` captured BEFORE the driver edit and
  again after, `diff` empty. That capture is confounded once this unit's own spec header flips, so
  it was redone against the PRE-CHANGE DRIVER ITSELF — `git show HEAD:tools/unattended/unattended.sh`
  placed beside a copy of its sibling `lib-unattended.sh`, without which it refuses — over FOUR live
  builds: `aStagedLane` (6 lines), `aWeldedTribunal` (10), `aHonedRuleset` (8, including two FORKED
  rows) and `aHoistedPass` (12). All four **byte-identical**. That comparison grades the EMITTER
  rather than the tree's state, which the first one could not. The suite carries the durable half —
  the padded table contains not one TAB in any row class.
- **AC11** — MET — on the real tree every unit row of `--plan aHoistedPass --paths` carries exactly
  three TABs with the spec's repo-relative path as the fourth field, verified with `cat -A`. Suite
  arms cover both the graded row and a `MISSING` unit, whose fourth field is EMPTY rather than
  ABSENT — an absent field would shift a caller's index by one on exactly the rows it cannot see.
  The `roster:` and `next:` lines are present and unchanged.
- **AC12** — MET — suite arms: the `--paths` listing has the same line count as the padded table and
  the same id sequence. Order comes from the generated units region and no sort was added.
- **AC13** — MET — suite arms. The `NOT A UNIT` diagnostic is keyed on a FILENAME, keeps its padded
  shape in `--paths` mode and carries ZERO TABs, so a four-field split skips it.
- **AC14** — MET — suite arm. The empty-`units` refusal names `--plan <slug> --paths` and no longer
  names the bare `--plan` that cannot supply a spec path.
- **AC15** — MET — the nesting comment names a DEPTH limit, states that a parent may make several
  sequential nested calls at the same depth, and marks the `wf_9b984206-816` three-call evidence as
  CARRIED from an earlier pass and not re-run here. `grep -cE "\bspent\b|\bbudget\b"` over the whole
  file returns `0`; it returned `1` at BASE and the one hit WAS this comment, so the criterion has a
  failing case that was observed.
- **AC16** — MET — evaluating `meta` out of the file gives `phases` titled `Spec`, `Audit`,
  `Disposal`, and a `description` containing neither `BUILD` nor `-> BUILD`. **Graded by no leg**;
  `TOOL-aHoistedPass-34` is the row that survives this spec going CLOSED.
- **AC17** — MET, and this is the one criterion the rest lean on. Every new arm was staged into
  `unattended-build.test.sh` FIRST and the suite run against the UNCHANGED source: **exit 1, 40
  FAILs**, naming each new arm — `AC4 CONVERGED: the skip is ANNOUNCED`, `AC5 failed disposal: the
  roster is EMPTY`, `AC6 the CONVERGING exit carries an empty roster`, `AC7 the roster is the
  ordered array …`, every `AC8 dispatch.args …`, `AC25: units still counts the WHOLE ordered set`,
  and the rest. With the source change: **exit 0, 124 arms**. One arm was found green in that RED
  run and fixed before the source landed — `AC5 … the standing blocker is NAMED` grepped for a bare
  `b1`, which the fixture's own `"briefPath":"b1"` satisfied. It now asserts the note's text.
- **AC18** — MET — `bash tools/check-install-prefix.sh` exits `0`. `unattended-build.js` sits at `6`
  with its reason naming `dispatch.scriptPath` and stating that the `gotchas.py` line did not leave
  with the prompt but MOVED into `CHECKLIST`. `unattended-build.test.sh` went `2 -> 6`, DERIVED with
  `--list` rather than predicted, with its four new literals named in the row.
- **AC19** — MET — `bash tools/unattended/adopt-unattended.sh` regenerated the carrier and
  `--check` then reports `in sync`, exit `0`. `grep -c -- "--paths" memory/guides/UNATTENDED-VERBS.md`
  returns `2`.
- **AC20** — MET — `bash tools/unattended/check-unattended.sh` exits **0**. The brief's narrow form
  does NOT exist: `--only 26` answers
  `check-unattended: --only takes 28 and nothing else; checks 1-27 share state and are one unit` at
  exit 2, so the whole gate is the only way to reach check 26 and it was paid for in full. The usage
  line keeps the literal `#   unattended.sh --plan ` that check 26's join reads, at the same column
  as its siblings. Two things that gate PRINTS and does not fail on, noted because they read like
  findings: it excludes four LANDING records whose witness is already an ancestor of the advertised
  tip, and its check 23 lists a long tail of dispatched passes from the landed `dRetiredFork` build
  that committed paths outside their declared set — the same class this unit's own backlog write
  falls in, reported rather than refused.
- **AC21** — MET, and OBSERVED rather than read. In a scratch clone at a short root, the resolving
  mark was stripped from this spec's section 8 so `--plan` graded the unit `FORKED`, and
  `bash tools/unattended/unattended.sh --dispatch aHoistedPass --pass TOOL-aHoistedPass-6 --writes tools/probe-ac21.js`
  exited `0` and parked `dispatch · item c55b155b TOOL-aHoistedPass-6 · reason tools/probe-ac21.js`.
  Section 4's enumeration of what `--dispatch` does NOT refuse stands on a measurement. Clone removed.
- **AC22** — MET, both directions, each run WITHOUT a pipe so the status is the checker's and not
  `tail`'s. Landed: `bash tools/check-kit-versions.sh` exits `0` with all three tokens on
  `tier2-review.js:3` reading `1.7`. Staged break — `meta.version` at 1.7, the
  `gov:kit review-harness@` marker left at 1.6 — exits **1** with
  `gov:kit review-harness@ marker (1.6) != its meta.version (1.7)`. Restored, exit 0.
- **AC23** — MET for five of six as written, with one qualification stated rather than hidden.
  `node tools/workflows/check-workflow-syntax.js` 0 · `bash tools/workflows/check-verifier-fanout.sh`
  0 · `bash tools/workflows/check-review-join.sh` 0 · `python tools/memory-tree/check-arms.py --check`
  0 · `bash tools/check-kit-versions.sh` 0. The sixth,
  `bash tools/memory-tree/check-memory-hygiene.sh`, was run as `--staged` and exits `0`; it prints
  `check 23 HELD under --staged — a corpus-wide join over every closed Tier-2 unit; the push-boundary
  run is where they bind`. That check therefore has NOT run against this unit here, and the push
  boundary is where it does.
- **AC24** — MET — `memory/backlog/TOOL.md` carries `TOOL-aHoistedPass-33` (the
  `gov:kit unattended-build@` marker paired against no constant), `-34` (the ungraded `meta` pair)
  and `-35` (the hand-out's empty `specPath`). Ids minted by this session off its own high-water,
  which was `TOOL-aHoistedPass-32`.
- **AC25** — MET — suite arms. With the attended fixture holding one `DONE (FORKED)` unit and one
  `READY` one, the returned `roster` names only `A-tB-2`, `skippedTerminal` is `["A-tB-1"]`, and
  `units` is `2`. The two are different arrays, which is what rev-6 corrected and what no earlier
  criterion could distinguish.

## What this unit did not do, said here rather than left to be found

- **`memory/backlog/TOOL.md` is written by this commit and declared by no dispatch row.** The
  declaration was attempted WITH the path and `--dispatch` refused it: check 49, *a path overlapping
  a shared mutable record this project declares*, `memory/backlog/TOOL.md` against `memory/backlog`.
  The refusal is about a disjointness claim between concurrent passes and no declaration can carry
  the path; the residual is parked in `RUN.md` and rev-7's §9 records it.
- **One instruction is LOST rather than moved.** `driverSteps`' ATTENDED branch told a pass to write
  down the paths it would touch before touching them. That is a per-pass instruction, the child owns
  per-pass instructions, and the child is section 3's first non-goal. An attended run under the
  hand-out loses it unless the child carries it. Section 4 says so and this repeats it once.
- **Two test arms were retired with the prompt they graded** rather than re-pointed at a weaker
  witness; a third was re-pointed at `GROUND`, where the attended honesty sentence actually lives.
  rev-7's §9 names all three.
- **No gate leg is added.** The arms live in two suites the bar does not run. The compensating check
  is the hand-run, and it is the line below.
- **One thing beyond the criteria was checked anyway, because nothing else would have.** Section 3
  makes the child a non-goal and this unit asserts nothing about its contents, so no criterion joins
  the hand-out's key set to what the child actually reads. Read once here: `unattended-unit.js`
  consumes `cfg.repo`, `cfg.slug`, `cfg.driver`, `cfg.ground`, `cfg.checklist`, `cfg.unitId`,
  `cfg.specPath` and `cfg.briefPath` — exactly the union of `dispatch.args` and `dispatch.perUnit`,
  with nothing left over on either side. Nothing on the bar grades that join, and a future edit to
  either half will not be told.

## The hand-run, with exit codes

- `bash tools/workflows/unattended-build.test.sh` — **exit 0**, 124 arms, 0 FAIL.
- `bash tools/unattended/unattended.test.sh --shard 2/2` — **exit 1, 54 FAIL**, and every one of
  them PRE-EXISTING. That is attributed rather than asserted. The same shard was run in a clone of
  the pristine BASE-side tip `e4c7dd4d`, at a short root, with nothing of this unit in it: it fails
  **54 times too, and the two failure lists are byte-identical** after `sed 's/ -- .*//' | sort`,
  differing only in the repo path one arm prints. Not one of the new `--paths` arms is among them.
  The failures are the region-two arms of `--dispatch` and `--brief`, every one reporting the tRun
  fixture's unit as MISSING or absent from the units region, plus one arm at line 4297 that greps
  `PROTOCOL.template.md` for a sentence `TOOL-aHoistedPass-2` removed at `8c759e50` earlier in this
  same run. Read together they say the STANDALONE shard is rotted — region-two arms depending on
  region-one state, which is the exact hazard the suite's own shard-contract comment names and says
  has no gate. **This is a finding about the suite, not about this unit, and it is not this unit's
  to fix.**
- `bash tools/unattended/unattended.test.sh` UNSHARDED — started, and it is the run that covers
  region one. See the closing line: whatever state it is in when this pass ends is stated there
  rather than reported as a green nobody saw.
- **The one region-one exposure of the driver change, checked by hand instead.** Region one holds a
  `--plan` arm at line 1555 — the `--waive` refusal that proves `--plan` exits INSIDE the parse loop,
  which is the very property the `--paths` flag had to be parsed around. Three shapes were run
  against BOTH the pre-change driver (`git show HEAD:…` beside a copy of `lib-unattended.sh`) and the
  changed one: `--plan <slug> --waive minimal-prose --reason x` (check 37 refusal, exit 1 both),
  `--plan` with no slug (exit 1 both), and `--plan nosuchbuild` (exit 1 both). All three
  **byte-identical**, as are the four live-build listings under AC10.
