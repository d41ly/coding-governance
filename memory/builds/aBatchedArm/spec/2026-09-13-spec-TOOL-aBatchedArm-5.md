# TOOL-aBatchedArm-5 — the evidence-derived pooled hang bound, and the flip

**Status:** CLOSED · rev-8 · 2026-09-14 · node a · Tier-2 · base 1c736fd9 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-aBatchedArm-5-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aBatchedArm-5-1-acceptance-ledger.md) | journal | — |
| [2026-09-14-build-TOOL-aBatchedArm-5-2-closing-fix-ledger.md](../build/2026-09-14-build-TOOL-aBatchedArm-5-2-closing-fix-ledger.md) | journal | TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 |
| [2026-09-15-build-TOOL-aBatchedArm-5-3-landing-ledger.md](../build/2026-09-15-build-TOOL-aBatchedArm-5-3-landing-ledger.md) | journal | TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 |
| [2026-09-23-build-TOOL-aBatchedArm-5-4-landing-pass-2.md](../build/2026-09-23-build-TOOL-aBatchedArm-5-4-landing-pass-2.md) | journal | TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 |
| [2026-09-14-prompt-TOOL-aBatchedArm-5-build-brief.md](../prompts/2026-09-14-prompt-TOOL-aBatchedArm-5-build-brief.md) | journal | — |
| [2026-09-14-prompt-TOOL-aBatchedArm-5-closing-fix-brief.md](../prompts/2026-09-14-prompt-TOOL-aBatchedArm-5-closing-fix-brief.md) | journal | TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 |
| [2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round1.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round1.md) | diff-review | TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 TOOL-aBatchedArm-4 |
| [2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round2.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round2.md) | diff-review | TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 TOOL-aBatchedArm-4 |
| [2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round1.md) | spec-audit | — |
| [2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round2.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round2.md) | spec-audit | — |
| [2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round3.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round3.md) | spec-audit | — |
| [2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round4.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round4.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`--pooled` exists (`TOOL-aBatchedArm-4`) and the eight shard rows exist (`TOOL-aBatchedArm-3`), and
the pooled run still bounds every row at `budget x sweep-ceiling-factor` — the shape that killed 14
of 58 suites in the full sweep of 2026-09-08 and that three records refused as a predictor. Replace
that bound with the evidence RULE the tree already owns, in the runner's own evidence file, with a
declared calibration mode that grades nothing; make the pooled VERDICT mean parity with the
calibrated baseline, so a red-by-design suite that ran to its end is GREEN and a crash, a kill or an
unrun row is RED; and land the DoD flip DARK, so the kit-work DoD moves from a serial self-test pass
to that pooled one plus `--checks` only as the build's landing step, after the one gate pass has
printed the pooled GREEN. The serial pass stays available on demand, declared, as the cost pass —
never as a DoD line.

## 2. Scope (IN)

- **S1** — a pooled row's HANG bound is derived from OBSERVED pooled readings, not from its serial
  budget: `max(<serial budget>, <worst reading>)` under this node and the runner's own condition
  token (`pooled@<outer>x<inner>` at the text `SWEEP_CONDITION=`), monotone, plus
  `tools/run-gates/ceiling-margin.txt`'s headroom of `max(<floor>, <fraction> x that)` READ from the
  file beside the runner (`$HERE/ceiling-margin.txt`; the runner REFUSES when it is absent, naming
  the file — the refusal `derive-ceilings.py` makes, reused as a rule and not imported, because the
  runner is bash). The serial-budget floor is the guard against a fast red: a pooled row cannot
  legitimately need less than its serial budget, so a 0.3 s refusal recorded as a reading never
  bounds a repaired suite below what it costs alone; the verdict prints which term won. **A row with
  NO reading under (row, token, node) REFUSES the pooled run naming the row, the token and
  `--calibrate`, and executes no suite — the whole population `--pooled` or `--sweep` reaches, not
  only the filtered one.** There is no fallback: the `sweep-ceiling-factor:` header in
  `selftest-budgets.txt`, its refusal arm at the text `declares no sweep-ceiling-factor`, and the
  `at its <budget x factor>s bound` verdict text are RETIRED in the same commit. **The graded run's
  WALL** is derived from the evidence bounds by the shape the runner already uses for the factor:
  `ceil(sum of bounds / OUTER)`, floored at the largest bound; `SELFTEST_WALL` still overrides and
  the existing below-the-largest refusal compares against the largest evidence bound. Every pooled
  verdict prints the reading, token, node and date it was bounded by. Observed by **AC1**, **AC2**
  and **AC7**.
- **S2** — the bootstrap is DECLARED: `--pooled --calibrate` runs EVERY row the invocation selects
  (bare, or `--kit <dir>`), evidenced or not, under ONE wall, the SUM of the selected rows' serial
  budgets, undivided — the population fully serialised, the largest backstop derivable with no
  typed number; a pooled pass exceeding its own serial sum is a hang and not a cost —
  `SELFTEST_WALL` tightening it only, the derived wall and which term won printed. No per-row
  bound. It withholds every verdict and records a reading ONLY for a row that is a READING by
  `TOOL-aBatchedArm-3` AC4's ratified rule: it exited on its own — rc captured, not killed by the
  wall — AND its filed output (the runner already keeps it at the text `"$d/out"`) carries the
  suite's TRAILER, which the runner recognises by ONE regex constant: `PASS (` for a green suite,
  the executed-count line at the text `assertions executed` for a shard, `this leg ran shard` for
  a shard leg. A completed exit with no trailer writes NO reading and is named under its own word,
  `untrailed`, red like `walled` — because a red-by-design row exits 1 at 0.3 s on an unbound
  variable exactly as it does after 1300 s of work, and the `ab-arm-never-did-the-work` class asks
  for an artifact of the work beside the exit. Beside rc the reading carries the count of `^FAIL`
  lines and, where the trailer is the executed-count line, the executed count; suites that print
  no trailer of any shape — at this base `check-brief-recorded.test.sh` and
  `check-pass-order.test.sh`, which exit `$st` with no `PASS` line — are DECLARED in the evidence
  file's header as rc-plus-`FAIL` rows whose completion the runner cannot witness, so the gap is
  printed and not silent. A row the wall killed writes NO reading, is named, and makes the
  calibrate run exit RED. Readings are written AFTER the sweep's closing fingerprint (`FP_AFTER`,
  the text `read_tree_fingerprint`), in one pass over the collected verdicts, because the evidence
  file is tracked and a write inside the fingerprinted window reds the runner's own run as UNSOUND.
  Every reading raises its (row, token, node) SECONDS monotone — never lowers them — while the
  `rc`, `fails` and `executed` columns are the LATEST reading's, so a repaired suite updates its
  baseline on the next calibrate without a reset. `--reset <row>` on the same invocation lowers
  that row's seconds and NARROWS the calibrate to the reset rows, since a reset row is uncalibrated
  by construction and the refusal has nothing else to refuse; it prints the decision; a reset row
  the narrowed calibrate then walls or finds untrailed stays uncalibrated, named, and the next
  graded run refuses it by name — the intended outcome, since a row nobody has seen complete has
  no bound. The summary line is `calibrated <n> row(s), <r> red, graded none` on green and
  `calibrated <n> row(s), <r> red, <w> walled, <u> untrailed, graded none` on red — `walled` and
  not `killed`, because a calibrate has no per-row bound and every kill there is the wall's —
  neither of which the kit runner's `sweep GREEN` / `WITHHELD` parser can read as a verdict.
  `--calibrate` with any verb or mode other than `--pooled` REFUSES naming the pair. Observed by
  **AC3**, **AC8** and **AC10**.
- **S3** — pooled readings live in their OWN tracked file, `tools/run-gates/selftest-pooled-evidence.txt`,
  one row per (row name, condition token, node), nine tab fields:
  `<row>\t<condition>\t<node>\t<max seconds>\t<rc>\t<fails>\t<executed>\t<readings>\t<date>`,
  `executed` being `-` where the trailer is not the executed-count line; the header stating that
  seconds are monotone, that `rc`/`fails`/`executed` are the latest reading's, and naming the rows
  whose suites print no trailer and are therefore rc-plus-`FAIL` only. The node is the
  charter's §2 registry TAG: `GOV_NODE` when set, else `USERNAME`/`USER` resolved against the
  registry table of `$ROOT/AGENTS.md`, then `$ROOT/CLAUDE.md` — the charter-file precedent at
  `run-gates.gov.test.sh`, the text `CHARTER="$ROOT/AGENTS.md"` — with the row regex
  `tools/drift-audit/drift_report.py`'s `_resolve_node_tag` uses, REFUSING by name when no row
  matches; never a hostname, which the registry does not know. Its SHAPE is graded by
  `run-selftests.sh --check`, the unguarded bar leg: every non-comment line has nine tab fields,
  seconds, rc, fails, executed and readings parse, readings is at least one, the node is a tag the registry
  table carries, no (row, token, node) key repeats, and every row names a row the budget file
  declares — a hand-edited, truncated or orphaned row reds on the bar, and an orphan is the right
  red: a deleted budget row takes its evidence with it or the file lies. It ships to no adopter:
  `tools/run-gates/kit.toml` gains a `project-owned` rule for it beside the `project-owned` rules it
  already carries for the same reason. NOT in `ceiling-evidence.txt` and NOT in
  `selftest-budgets.txt`'s fourth column, so `--rank`'s refusal of `pooled@` readings
  (`TOOL-aQuenchedHarness-6` S3a) is untouched and shard budgets stay serial. Observed by **AC4**
  and **AC9**.
- **S4** — THE POOLED VERDICT IS PARITY, and every red source the render loop already has is
  KEPT. Under `--pooled` with evidence present, a row that ran to its own end whose (rc, fails,
  executed) equals its evidence row's renders `ok (rc <n>, <f> FAIL, <e> executed matched)`
  APPENDED to the row after its `cost withheld` text, never in its place; one whose triple differs,
  or whose filed output carries no trailer where its evidence row has one, renders `MISMATCH`
  naming both triples and the acceptance (`--calibrate` to take the new baseline, `--reset <row>` to
  lower seconds), and keeps beneath it the output grep the `FAIL` branch prints today (the text
  `grep -E '^(FAIL|nope|.*FAILED)'`), the only debug surface a pooled red has. **The ONLY change to
  `st` is that a completed, trailed, matched row no longer sets it**: the seven places the render
  loop sets `st=1` today — the unresolved row at the text `could not be resolved into a runnable
  suite`, the could-not-start row at the text `no verdict was written, so this suite could not
  start`, the wall-breached rows (`WALL`, `UNRUN`), the own-bound kill (`TIMEOUT`), the `FAIL`
  branch that parity replaces, and the pool-ran-wider guard at the text `THE POOL RAN WIDER THAN
  ITS BOUND` — all survive by name, beside the tree fingerprint. The summary line prints every
  non-completion outcome the loop has, each from its own source, by name:
  `killed <a> · walled <b> · unrun <c> · unstarted <d> · mismatched <e>`, where `unstarted` is a
  row with no verdict file under no wall breach (the worker-death class the runner's own comment
  at the text `leaving no verdict file` records) or an unresolved row, its reason printed on the
  row; `mismatched` is computed over rows with a verdict file only, which is why the other four
  need their own words. The GREEN and RED summary lines keep `NO cost verdict was issued` and the
  `cost verdict(s) WITHHELD` line the kit runner parses at the text `cost verdict(s) WITHHELD`
  survives, because §3's first non-goal keeps the cost verdict withheld and `TOOL-aPooledSweep-2`
  S2 is the per-row rule this preserves. So GREEN means: every row ran to its own end under its
  bound with its trailer and matched its baseline, the pool ran no wider than its bound, and the
  tree is sound. `run-unattended-gates.sh`'s `st` follows the runner's, so a perfect pass over the
  eight red-by-design rows prints GREEN; the runner's usage sentence (`did any suite fail`) and its
  RED-ambiguity text at the text `the serial re-run` are re-worded to the parity question, since a
  parity red is not told to confirm itself serially. Observed by **AC11** and **AC5**.
- **S5** — the flip lands DARK, the carriers are CLASSIFIED, and the flip is the build's landing
  step. Both predicates below are PATH-SCOPED, because unscoped either matches the frozen records
  and the charter's own §7 rule — round 4 measured 87 and 32 hits over the tracked tree — and a
  landing step with no owner turn must not be left to infer a scope from a count. The CARRIER
  predicate `a line spelling --selftests --serial, run-unattended-gates.sh --serial, or
  run-unattended-gates.sh --all --serial`, scoped `-- .githooks/gate-env.sh AGENTS.md
  memory/guides/SESSION-KICKOFF.md tools/unattended/`, yields eight lines at this base, re-derived
  at build time and pasted in the ledger, in TWO classes by role: **DoD carriers** — lines stating the serial pass
  as the criterion: `.githooks/gate-env.sh:27`, `tools/unattended/kit.toml:125` and `:126`,
  `tools/unattended/run-unattended-gates.sh:27` — and **pointers** that already state the post-flip
  fact and are BYTE-UNCHANGED at both steps: `AGENTS.md:519` (`On demand:`, measured 9 bytes under
  its cap), `tools/unattended/README.md:66` (`ON DEMAND ONLY`), `run-unattended-gates.sh:233` (a
  COST question, which `--pooled` withholds), and `memory/guides/SESSION-KICKOFF.md:169` (the
  owner's dated correction entry, which no ruling licenses this run to edit, and whose manifest is
  measured 10 bytes under `MAX_MANIFEST_BYTES`). Inside this unit the four DoD carriers gain,
  beside `--serial`, the words `--pooled after calibration` — `land dark`, unit 4 r2 B1's rule.
  **The flip is the BUILD's landing step, not this unit's**, in this order on the MERGED tree
  (`TOOL-aLoosenedCeiling-3`). **Step (0), rev-8, precedes everything below**: the eight direct
  shard runs of `check-unattended.test.sh --shard k/8`, the paste of each group's observed set from
  the `observed:` lines into its `check_emitted` call with the run named beside it, and re-runs
  until no `FAIL check_emitted:` line remains — unit 1's golden-writing step, which S5 as first
  written left unordered against the calibrate; the runner now refuses a sentinel-carrying row as
  UNTRAILED, so the order is enforced as well as stated. Then (1) `run-selftests.sh --kit tools/unattended --pooled --calibrate`
  over the population `run-selftests.sh --kit tools/unattended --list` resolves (fourteen rows at
  this base — the list's number); on a red, the walled rows are named in the landing record, the
  build lands WITHOUT the flip, and AC3's real-row half is ledgered amended naming them; (2) the
  evidence file is committed; (3) `run-unattended-gates.sh --pooled` runs and prints GREEN — parity
  GREEN, S4's — pasted with its summary line; (4) ONLY THEN the flip commit, whose contents are exactly two sets. The DoD-PHRASE
  predicate `GREEN verdict|not done until|DoD path|DoD command|landed dark`, scoped
  `-- .githooks/gate-env.sh tools/unattended/ tools/run-gates/run-selftests.sh`, yields six lines
  at this base, re-derived at the landing and pasted: FIVE re-worded to the pooled criterion —
  `.githooks/gate-env.sh:26`, `tools/unattended/kit.toml:123` and `:130` (the `landed dark`
  comment), `tools/unattended/run-unattended-gates.sh:27` and `:187` (the mode-refusal text at the
  text `the recorded DoD path`); ONE byte-unchanged with the reason — `tools/run-gates/run-selftests.sh:15`
  names no mode and is true under parity; and the lines OUTSIDE the scope are excluded by path with
  the reason — `AGENTS.md:265` and `coding-governance-agents.template.md:193` are the charter's §7
  rule about regression tests, `memory/archive/` is frozen snapshots, `memory/builds/` is frozen
  records, none a carrier. Plus the four DoD carriers' argv spelled `--pooled` verbatim with the
  dark marker removed, `kit.toml:126` spelled `--checks` (its `--all --serial` runs the self-tests
  AND the checks — `ONLY=""` at the text `--all)` — so keeping it would add a pooled pass to a serial
  one), one ADDED line in `tools/unattended/README.md` naming the pooled DoD beside the on-demand
  serial line, and `last-audit` re-stamped. The post-commit witness re-runs BOTH scoped predicates
  and pastes both: the carrier predicate returns the four pointer lines byte-identical to BASE and
  the four carriers spelling `--pooled` with no `--serial`; the phrase predicate returns zero lines
  naming `--serial` or `landed dark` within its scope. On a red at
  step (3) the carriers stay as landed, AC5's landing half is ledgered amended naming the red, and
  the build lands without the flip. Observed by **AC5** and **AC6**.

## 3. Non-goals (OUT)

- **A contention model that makes a pooled COST verdict sound.** Still withheld under `--pooled`.
  The evidence bound is a HANG bound; it says when a run has stopped answering, never what it cost.
- **Observing the host's LOAD.** `pooled@8x1` names a width and a node, not whether another
  worktree's bar is running. Taking the turnstile or recording beacon state is named and not built;
  the evidence shape tolerates it by being monotone over whatever was observed, and `--calibrate`
  re-run on a loaded day raises the row rather than being refused.
- **Calibrating any row outside the population the DoD command resolves.** A bare `--pooled` over
  the whole declaration refuses until every row it reaches is calibrated, by name; nobody is
  obliged to calibrate them by this unit, and the refusal is the announced-unarmed state. The count
  of those rows is the budget file's to report.
- **Deciding the arity or the 20-minute question.** Unit 3's AC4 arm two is read at the same final
  pass; this unit's bound grades whatever that reading is.
- **A per-row FAIL-SET oracle in the runner.** Parity is (rc, `^FAIL` count) against the calibrated
  baseline, a cheap positive artifact; the FAIL-set equivalence unit 3 established is unit 3's AC6,
  observed there, not re-derived by the pooled pass.
- **Editing the owner's correction entry or the charter's on-demand sentence.** Both already state
  the post-flip fact; neither is a DoD carrier; neither is this run's to re-word. Nor is anything
  the two predicates match OUTSIDE their declared scopes — the charter's §7 regression-test rule,
  the template, the archive snapshots, the build records including this spec — a carrier; the
  scopes exist so the flip never reads them as one.

### Edges

- **consumes-from** `TOOL-aBatchedArm-4` — the `--pooled` mode, the kit runner's pooled path, and
  the carriers it landed dark.
- **consumes-from** `TOOL-aBatchedArm-3` — the eight shard rows, part of the population this unit's
  S2 calibrates at the final pass, and the baseline oracle its AC6 established.
- **hands-off** `none`

## 4. Design

### Why the evidence shape and not a factor

Three records and one measurement. `TOOL-dRetiredFork-40` measured 443 s under load against 583 s
quiet and refused to predict one from the other by multiplying. `TOOL-aPooledSweep-2` §3 refused a
factor "derived from one suite … applied to fifty-eight it was never measured on". The full-sweep
record's own remedy is re-sizing against pooled readings. And `derive-ceilings.py` already owns the
rule: worst observed under the condition, monotone, floor-plus-fraction headroom, refusing to report
with no evidence, `--reset` as the one lowering path. Its fifth part — readings from `ok` runs only,
because "a leg that FAILED may have failed fast" — is DEPARTED from here, deliberately: the eight
shard rows are red by design and exit 1 when complete, so an ok-only reader would refuse them
forever. What replaces it is two things: the serial-budget floor under the bound, which makes a
fast red harmless to the BOUND, and the `^FAIL` count beside the rc, which makes a fast red visible
to the VERDICT — a shard that dies at 0.3 s on an unbound variable exits 1 with zero `FAIL` lines
where its baseline carries three, and mismatches.

### Why the pooled verdict is parity

Unit 3's AC6 and the build README's rule — "the baseline is RED and is the oracle; equivalence is
the `FAIL` line set plus the executed assertion count" — make GREEN-by-exit-code impossible for the
population the DoD names: the driver exits 1 on a perfect pass over eight red-by-design rows,
forever. `ceiling-margin.txt`'s header (`TOOL-dRetiredFork-40`) records a verdict that fires on a
healthy run as strictly worse than a loose bound, and unit 4's AC7 reds a DoD command pointing at a
refusal. So the verdict is re-based: GREEN means every row ran to its own end and matched the
(rc, fails) it was calibrated at. That keeps `kit.toml`'s "not done until this prints GREEN"
sentence true at the word, dissolves the question of what a landing reads instead of GREEN, and
makes the landing's witness one word plus its summary line.

### Why the calibrate wall is the serial SUM and not a division

Round 2 did the arithmetic the fold had not: `ceil(sum / OUTER)` floored at the largest serial
budget gives 3860 s for the fourteen-row population at width 8, and the tree's own sweep record
(`TOOL-aPooledSweep-1`'s full-sweep rows, slot 54) shows the driver suite alive at 7722 s under that
width — the divided wall is killed by the record this spec cites as its motivation. The bootstrap's
wall is a backstop against a HANG and not a prediction of cost, so it is the population fully
serialised: nothing pooled can honestly need longer than everything run one after another. It is
derivable, prints itself, and puts no typed number in the DoD.

### Why the bootstrap is a declared mode, and why it refuses in four places

The evidence shape cannot bound a row that has never been observed, and `--sweep`'s own S7 forbids
an unbounded pooled row. So the first observation is taken under the serial-sum wall, in a mode that
says it is calibrating and grades nothing. It refuses a walled row (a truncation is not a reading —
the `ab-arm` class), refuses any mode but `--pooled` (a `--serial --calibrate` that ran the serial
loop and wrote nothing would be silent in a mode whose point is announcing itself), refuses a file
that does not parse, and refuses an absent margin file, because a silent zero-margin default is a
bound nobody chose.

### Why the flip is the build's landing step and not this unit's

`TOOL-aBatchedArm-4` landed `--pooled` dark because the bound it inherits killed five of the seven
current unattended rows. Re-pointing the carriers is the act that makes the fast path the recorded
DoD verdict, and it happens only after the bound that would grade it is the evidence one and the
parity GREEN has been printed over every row the DoD command resolves — fourteen at this base, not
the eight a draft of this spec typed. Two owner rulings (2026-09-13, 2026-09-14) defer every gate
run to one pass when every unit is built, so the observation that licenses the flip cannot happen
inside this unit; landing the flip as text before it would record a DoD command with no completing
run, which is the false-green shape one level up and what unit 4's AC7 reds by name. Hence dark on
the four carriers that state the criterion, and byte-unchanged on the four pointers that already
state the post-flip fact — round 3 found the earlier fold applying one edit to both classes, which
would have re-worded the owner's own correction entry and redded the manifest ratchet by a measured
17 bytes.

### Why the node is the registry tag, and how the fixture has one

Unit 3 measured a checker invocation at 47 to 60 s on node `a` against the ~2 s another host
records; a 2x headroom cannot absorb that spread, so the key carries the node. It carries the
REGISTRY tag and not a hostname because `GOV_NODE` is set nowhere in the tree, so a hostname would
be what every real invocation wrote — a name the charter's §2 table does not know and the sibling
`ceiling-evidence.txt` does not use. The runner resolves it from the charter file at the repo root,
as `run-gates.gov.test.sh` already does. The self-test fixture is a bare `git init` with no charter,
so `build_repo` writes a charter stub `AGENTS.md` carrying one registry row that maps the current
user (`${USERNAME:-$USER}`) to a fixture tag, every seeded evidence row is keyed on that tag, and
AC2's no-row clause is staged by deleting the row.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` (the fixture rebuild:
`build_repo` gains the charter stub with its registry row, a fixture `ceiling-margin.txt` with a
small floor, and a seeded, TRACKED evidence file covering every token the arms produce —
`pooled@2x1` by default, since `W` falls to 2 without `run-gates.sh`, and `pooled@1x2` under the
arms that set `SELFTEST_OUTER_WIDTH=1` — every row an arm appends at run time seeded in that arm's
setup under the token it runs at; the readings seeded are sized so the `SELFTEST_WALL=10` kill arm,
the `SELFTEST_WALL=5` below-largest arm and the `suite-mid` arm at the text `4 x 2 = 8 s` — a 5 s
sleep at budget 4 that the factor bounded at 8 s and the evidence bound must clear — stay
reachable, the fixture margin's floor and fraction named beside the seeds; every new arm's sleep
at most 3 s) ·
`tools/gate-legs.json` and `tools/run-gates/selftest-budgets.txt`'s `run-selftests self-test` row
(the leg is at `ceiling: 300` and its last ledger row is `300.333 fail`, exit 124 — killed at its
own bound before this unit adds an arm; both are re-declared at the build's final gate pass from
that pass's observed wall, pasted, since the ruling forbids the observing run now) ·
`tools/run-gates/selftest-pooled-evidence.txt` (new, tracked, names row NAMES and no path, so it
takes no `install-prefix-carried.txt` row) · `tools/run-gates/kit.toml` (the `project-owned` rule)
· `tools/run-gates/selftest-budgets.txt` (the retired factor header) · the four dark DoD carriers ·
`tools/unattended/run-unattended-gates.sh` (its `st` follows parity; the summary it prints) ·
`memory/guides/SESSION-KICKOFF.md` (`run-selftests.sh` is on its `watch:` line, so `last-audit` is
re-stamped in the same commit; no body edit) · this build's records.

## 5. Production-readiness checklist

- security — N/A. Bound derivation and verdict wording.
- perf / scale — the pooled path becomes the recorded kit-work DoD only at the build's landing; its
  wall clock is whatever the final pass measures, graded rather than hand-run from then on. The
  flip REMOVES the serial self-test pass from the DoD (`--all --serial` becomes `--checks`) rather
  than adding a pooled one beside it. The `run-selftests self-test` leg is already killed at its
  300 s ceiling before this unit; its re-declaration is owed at the final pass, from that pass.
- error / empty / loading states — a row with no evidence under this node and token REFUSES the
  pooled run by name; a calibration run prints that it graded nothing and reds on a walled row; an
  evidence file that will not parse refuses rather than defaulting; an absent margin file refuses;
  `--calibrate` off `--pooled` refuses; a node with no registry row refuses naming the user;
  `--check` reds a malformed, duplicated or orphaned evidence row; a MISMATCH names both pairs and
  the acceptance.
- observability — every pooled verdict names the reading, token, node and date it was bounded by
  and which term of the bound won; the pooled summary counts killed, walled, unrun and mismatched
  rows separately; the calibrate prints its derived wall and which term won and counts walled rows.
- risks — seconds are monotone over whatever was observed, so a calibration taken on a loaded box
  sets a loose bound for that row until `--reset`; a first reading taken on a quiet box is raised
  by the next `--calibrate`; a fast red cannot bound a row below its serial budget and cannot match
  a baseline with a non-zero `fails`. The direction NOT covered: a reading taken on a day slower
  than any later day is never lowered except by `--reset`, and that is the monotone rule's price,
  stated. A mismatch after a genuine repair is one `--calibrate` away and says so.
- testing — the runner's self-test gains arms for: the no-evidence refusal; the foreign-node
  refusal; the no-registry-row refusal; the absent-margin refusal; the calibrate mode grading
  nothing; a bound derived from a staged evidence row, with the serial-budget floor taking over for
  a tiny reading; the walled-row RED with no reading written; the monotone raise of seconds with
  rc and fails following the latest reading; `--reset <row>` lowering exactly that row and
  narrowing the calibrate; `--reset` off `--calibrate` and on an absent row refusing; `--calibrate`
  off `--pooled` refusing; the unparseable file refusing; `--check` redding a duplicated key, a
  seven-field row and an orphaned row; the wall derived from evidence bounds and the below-largest
  refusal against it; a calibrate over a clean fixture reporting `fingerprint MATCHED` with the
  file changed; the parity verdict — a red-by-design row with a matching (rc, fails) exits 0 under
  `--pooled`, a mismatching one exits 1, a row exiting 1 in under a second with zero `FAIL` lines
  against a baseline of three is `MISMATCH`; the summary counting a killed, a walled, an unrun and
  a mismatched row each under its own word, with the landing predicate FALSE on each; a worker that
  dies before writing its verdict file (an unbound variable under `set -u`, the class the runner's
  own comment names) read as `unstarted` with the run RED; a suite that exits 0 in under a second
  with no trailer written as NO reading under `untrailed` at calibrate and rendered `MISMATCH`
  against a seeded green row at grade. Each observed RED first.
- migration — the four carriers gain the dark spelling in this unit, reversible by one line each;
  the flip is the build's landing step and reverts the same way.
- user docs — the runner's `--help` names `--calibrate` and `--reset` and the parity question; the
  kit runner's names the dark spelling, the landing order, and that `--selftests --serial` is the
  cost pass on demand.

## 6. Acceptance criteria

- **AC1** — When a fixture row has a reading in `selftest-pooled-evidence.txt` under the fixture's
  condition token and tag, `run-selftests.sh --pooled` bounds it at `max(serial budget, reading)`
  plus the fixture `ceiling-margin.txt`'s headroom, prints the reading, token, node, date and which
  term won, and the run's wall line is `ceil(sum of bounds / OUTER)` floored at the largest bound;
  a fixture row whose seeded reading is far below its serial budget is bounded from the budget; and
  with the margin file removed the run REFUSES naming it.
  `fixture:` the runner's own test fixture with staged evidence rows, run by
  `bash tools/run-gates/run-selftests.test.sh`; no real suite runs.
  Red when: the bound or the wall is the serial budget times any factor, the verdict names no
  reading, a tiny reading bounds a row below its serial budget, or a pooled run proceeds with the
  margin file absent.
- **AC2** — When a fixture row has NO reading under this tag and token, `run-selftests.sh --pooled`
  REFUSES naming the row, the token and `--calibrate`, and executes no suite; a row evidenced under
  a FOREIGN tag refuses the same way; and with the fixture charter's registry row deleted, the run
  refuses naming the user.
  `fixture:` as AC1.
  Red when: it runs the row under any bound, which is a factor wearing a refusal's name.
- **AC3** — When `run-selftests.sh --pooled --calibrate` runs over the fixture rows, each is bounded
  by the serial-sum wall only, no `OVER BUDGET` and no `TIMEOUT` verdict is printed, each completed
  row's reading is written with its token, tag, rc and `fails` after `fingerprint MATCHED`, a second
  calibrate with a lower reading and a different rc updates rc and `fails` and not seconds, and the
  summary says `calibrated <n> row(s), <r> red, graded none`; and when one fixture row sleeps past
  the wall, that row writes NO reading, is named, and the run exits RED with `<w> walled` in its
  summary.
  `fixture:` as AC1, inside this unit; the real population at the build's landing, step (1) of S5.
  `cost:` at the landing, one pooled pass of the population `--kit tools/unattended --list`
  resolves under the serial-sum wall, its longest row the floor of that pass.
  Red when: a calibration prints a verdict, a walled or untrailed row's seconds land in the file,
  a second calibrate with a lower reading lowers seconds, the write lands inside the fingerprinted
  window, or the real pass walls a row and the landing has no record naming it.
- **AC4** — When `run-selftests.sh --rank` runs in the fixture after a calibrate, it exits 0; and on
  the real tree `grep -c pooled@ tools/run-gates/selftest-budgets.txt` is 0 before and after the
  unit, and `--rank`'s unbacked list is the same list before and after.
  `fixture:` as AC1 for the first half; a grep and a diff on the real tree for the second.
  Red when: a `pooled@` token appears in the budget file, or the unbacked list moved.
- **AC5** — When the lines the S5 predicate yields are read as text after this unit's commit, the
  four DoD carriers name `--pooled after calibration` beside `--serial` and the four pointers are
  byte-identical to BASE; and at the build's landing, `bash tools/unattended/run-unattended-gates.sh
  --pooled` on the merged tree over the population `--kit tools/unattended --list` resolves prints
  GREEN with a summary of `killed 0 · walled 0 · unrun 0 · unstarted 0 · mismatched 0` and `fingerprint MATCHED`,
  pasted, and the flip commit follows it with both predicate hit lists and the post-commit
  DoD-phrase re-run's empty result pasted — that half owed until then, in the amended form.
  `figure:` both sets are DERIVED by the S5 predicates under their declared path scopes at build
  time and pasted in the ledger with hits and exclusions.
  `cost:` one real pooled pass on the merged tree, at the landing.
  Red when: a DoD line names `--pooled` alone before the pasted GREEN, any pointer moved, the
  landing pass is not GREEN and the flip lands anyway, after the flip `kit.toml:126` still runs the
  self-tests, an argv carrier still spells `--serial` after the flip, the scoped DoD-phrase re-run
  names `--serial` or `landed dark`, or any line outside the two scopes moved.
- **AC6** — When the existing `--serial` arms of `run-selftests.test.sh` run after this unit, they
  are GREEN unchanged: the serial mode still issues `OVER BUDGET` cost verdicts, because this unit
  touched no serial path; and every pre-existing `--pooled`/`--sweep` arm NOT enumerated in §7 is
  GREEN unchanged.
  `fixture:` as AC1.
  Red when: any pre-existing serial arm moved, or an unenumerated pooled arm moved.
- **AC7** — When `selftest-budgets.txt` is read after this unit, it carries no
  `sweep-ceiling-factor:` header, and `run-selftests.sh --pooled` over the fixture with a factor
  header staged back in ignores it — the bound and wall are the evidence ones.
  `fixture:` as AC1.
  Red when: any factor-derived bound or wall prints.
- **AC8** — When `run-selftests.sh --serial --calibrate`, `--check --calibrate` or bare `--calibrate`
  runs, each REFUSES naming the pair and executes no suite.
  `fixture:` as AC1.
  Red when: any of them runs a row or writes a reading.
- **AC9** — When `run-selftests.sh --check` runs over an evidence file with a duplicated
  (row, token, node) key, a seven-field row, a row whose node is no tag the registry carries, or a
  row naming no declared budget row, it REDS naming the line; and `--pooled` over a file that will
  not parse REFUSES naming the file.
  `fixture:` as AC1.
  Red when: `--check` is green over any of the four, or `--pooled` defaults past the parse.
- **AC10** — When `run-selftests.sh --pooled --calibrate --reset <row>` runs in the fixture, exactly
  that row's seconds are lowered to the new reading, the calibrate ran that row and no other, and
  the decision is printed; `--reset` off `--calibrate`, and `--reset` naming a row the file lacks,
  each REFUSE by name.
  `fixture:` as AC1.
  Red when: any other row moves, the calibrate runs the whole population, or the reset runs silently.
- **AC11** — When `run-selftests.sh --pooled` runs in the fixture over a red-by-design row whose
  (rc, `fails`, `executed`) matches its evidence row, it renders `ok (rc 1, 3 FAIL, 81 executed
  matched)` and the run exits 0; over a row whose pair differs it renders `MISMATCH` naming both pairs and the acceptance, and
  exits 1; a row exiting 1 in under a second with zero `FAIL` lines against a baseline of three is
  `MISMATCH`; and the summary line prints `killed`, `walled`, `unrun`, `unstarted` and
  `mismatched` each from its own source, one fixture row staged into each class — the `unstarted`
  one a worker dying under `set -u` before its verdict file — the run RED on every one.
  `fixture:` as AC1.
  Red when: a red-by-design row with a matching triple exits 1, a mismatching triple exits 0, a
  fast crash reads as matched, a row with no verdict file and no wall breach reads GREEN, a
  trailer-less run is matched at grade, or any non-completion outcome the render loop sets `st`
  for is absent from the summary.

## 7. Gates

`memory hygiene` · `run-selftests self-test` · `every held leg is budgeted, every budget row resolves`
· `install-prefix (shipped surface)` · `charter size` · `kickoff-manifest ratchet` · `run-gates canary`
· `run-gates gov canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates adopter e2e`
· `profile-bar selftest` · `lexicon naming predicates` · `govkit selfcheck` · `push-main self-test`
· `check-wiring self-test`

The list names the legs whose SUBJECT this unit changes; the full bar at the final pass decides the
rest by its own guards. **This is KIT work, and nine of these legs are HELD** under the run's
declared `GATE_CMD` (`bash tools/run-gates/run-gates.sh`, bare): `run-selftests self-test`,
`run-gates canary`, `run-gates gov canary`, `run-gates evidence`, `run-gates turnstile`,
`run-gates adopter e2e`, `profile-bar selftest`, `push-main self-test`, `check-wiring self-test` —
`chunk: selftests` or `subject: kit`, written `ondemand` by the bare bar since the owner's 2026-08-27
ruling. `run-selftests self-test` is the ONLY leg that executes the fixture arms behind AC1, AC2,
AC6 through AC11 and the fixture halves of AC3 and AC4, so the build's final gate pass runs the
kit-work DoD `AGENTS.md` names, `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`,
and pastes its verdict beside `gates-green` in the landing record rather than assuming it inside.
**That leg is already killed at its own 300 s ceiling** (its last ledger row, `300.333 fail`, exit
124) before this unit adds an arm, so the final pass also pastes the leg's new ledger row and
re-declares its ceiling in `gate-legs.json` and its budget row in `selftest-budgets.txt` from that
observed wall, with the reason beside each — the observing run the re-declaration needs is the one
the ruling defers, so it cannot be taken at the DoR.

New arm: `tools/run-gates/run-selftests.test.sh` · the arms §5 testing lists, each staged RED then
unstaged, over the rebuilt fixture · every pooled arm the factor arithmetic reached is RE-CUT to the
evidence shape and enumerated in the ledger: the factor `TIMEOUT` arm, `run wall 140s`, the UNRUN
arm (its appended rows seeded), the `SELFTEST_WALL=10` kill arm, the `SELFTEST_WALL=5`
below-largest arm, and the `suite-mid` arm at the text `4 x 2 = 8 s`, whose seed is sized above
its 5 s sleep; the factor-absent refusal arm is RETIRED with the header · the PARITY-REACHED arms,
every `--pooled`/`--sweep` arm the test file carries, derived by grep at build time and pasted, at
this base: the arm at the text `a RED pooled run points at the` RE-CUT to the parity wording, since
it asserts the RED-ambiguity text S4 removes; the two arms wanting a suite's own `FAIL` line
beneath its row (`FAIL something`, `FAIL scratch-under-tmpdir`) RE-LABELLED as `MISMATCH` reds
against a (0, 0, -) seed, their want-strings kept by the beneath-row grep S4 preserves; the arms
wanting `NO cost verdict was issued` and `cost withheld` UNCHANGED, because S4 keeps both · floor
to move: the suite's own, up by the arms added and down by the one retired, both counts derived at
build time.

## 8. Open questions

- **F1 · Does the evidence file take a per-row condition token, or one per run?** Per row.
  RESOLVED (agent, 2026-09-14, delegated): per (row, token, node) in the runner's OWN evidence file;
  rev-1 named `derive-ceilings.py`'s reader as the seam and that was wrong at source — its file has
  no condition column, is generated from bar leg files, and refuses hand rows by its header.
- **F2 · What if unit 3's AC4 measurement misses 20 minutes?** Then the flip still happens if the
  bound is sound — the goal is the owner's target and the flip is about correctness, not speed — and
  the miss is recorded against the host's spawn path per `TOOL-aBatchedArm-4` §4. RESOLVED (agent,
  2026-09-13, delegated): the flip is gated on the bound, not on the 20 minutes.
- **F3 · Refuse or fall back for an uncalibrated row?** RESOLVED (agent, 2026-09-14, delegated):
  REFUSE, and retire the factor so nothing survives to fall back on. A fallback is the bound that
  killed 14 of 58, and a refusal names what to type.
- **F4 · Where does the flip land?** RESOLVED (agent, 2026-09-14, delegated): dark in this unit on
  the four DoD carriers, flipped as the build's landing step after the pasted parity GREEN on the
  merged tree. The alternative — a DoD line naming a command with no completing run — is the shape
  unit 4 AC7 reds.
- **F5 · Which wall bounds a calibration?** RESOLVED (agent, 2026-09-14, delegated): the SUM of the
  selected rows' serial budgets, undivided, `SELFTEST_WALL` tightening only. The divided form,
  `ceil(sum / OUTER)` floored at the largest budget, was rejected at round 2 because the tree's own
  sweep record kills it (3860 s against a 7722 s driver row at width 8); the profile row is the
  borrow `TOOL-aPooledSweep-1` rev-3 refused; a REQUIRED `SELFTEST_WALL` would put a typed number
  in the DoD.
- **F6 · Is GREEN the landing criterion?** RESOLVED (agent, 2026-09-14, delegated): YES, once the
  pooled verdict means parity (S4). Round 2's answer — no, because eight rows are red by design and
  the driver exits 1 on a perfect pass — was true of the exit code as it stood and would have left
  the recorded DoD command printing RED on success forever; round 3 found the summary tokens that
  replaced it counted one of the runner's three non-completion classes. Re-basing the exit on parity
  answers both: GREEN is the word, and it is earned only when every row completed and matched.

## 9. Revision log

- rev-8 · 2026-09-14 · §2 S5 · the landing order, re-stated after the round-1 closing diff
  review (D3(a)): S5 ordered the calibrate as step (1) with no paste before it, while unit 1's
  golden-writing step was owed "at the final pass" with no order pinned between them — calibrate
  first baselined the fourteen `FAIL check_emitted:` sentinels as the parity oracle, paste first
  left the calibrate unable to reuse the shard runs' output. Step (0) now precedes (1): the eight
  direct shard runs, the paste of each group's observed set with its run named, re-runs until no
  sentinel line remains; then the calibrate, the evidence commit, `run-unattended-gates.sh
  --pooled` GREEN, the flip. The mechanism half (D3(b)) landed in the runner in the same closing
  fix: a sentinel-carrying row is UNTRAILED at calibrate and MISMATCH under --pooled, and each
  row's output is kept under `<git-dir>/gate-logs/selftests/`. The same order is written in
  `RUN.md`'s Landing order block. Records only; the unit stays CLOSED.
- rev-7 · 2026-09-14 · §2 S5 · §6 AC5 · build-time corrections, written BEFORE the first edit as
  the brief requires. The DoD-phrase predicate run over the tree at `e82d4053` under its declared
  scope yields SIX lines, which are exactly the six rev-6 enumerates (five re-worded, one
  byte-unchanged); rev-6's "eight" was the carrier predicate's count carried across, and the word
  is corrected — the enumeration was right. AC5's landing summary is S4's five-word line,
  `unstarted` between `unrun` and `mismatched`, which rev-6 added to S4 and AC11 and not to AC5's
  quote. Under the owner rulings of 2026-09-13 and 2026-09-14 this unit ran NO suite, fixture,
  self-test leg or bar: every one of AC1 through AC11 is ledgered in the AMENDED form naming the
  command the build's final gate pass observes it by, and every new arm is written with its red case
  stated in its comment and marked `NOT YET OBSERVED RED`. Built and CLOSED as it stands, two commits:
  45 arms added and one retired (the factor-absent refusal), `SELFTEST_FLOOR` 55 to 99; the manifest
  re-stamp rode in the S1 through S4 commit because `run-selftests.sh` is on the `watch:` line and
  the ratchet grades the staging commit, not the S5 one the brief paired it with; the kit runner's
  `--help` gained five lines naming the parity verdict, the landing order and the serial cost pass
  (§5 user docs), so its `:187` and `:233` lines are byte-identical at `:192` and `:238`; the dark
  spelling on the four carriers is `--pooled after calibration` and contains none of the phrase
  predicate's words, so the flip's yield is still the six lines. The two trailer-less rows are
  declared in the evidence header as `# no-trailer: <row>` lines, which the runner reads.
- rev-6 · 2026-09-14 · §2 S2 · S3 · S4 · S5 · §3 · §4 Files touched · §5 · §6 AC3 · AC5 · AC6 ·
  AC11 · §7 · §10 · folded spec-audit round 4 (BLOCKED, 2 blocker rows in one defect, 6 highs, 2
  mediums, 10 confirmed rows in 4 defects, precision 0.43 — NOT strictly smaller than round 3's one
  blocker, so the loop EXITS here with disposition FOLD; this spec is not re-reviewed). Both
  predicates are PATH-SCOPED and their yields enumerated by role — the phrase predicate's five
  re-worded lines, one byte-unchanged, and the charter rule, template, archive and records excluded
  by path — and the post-commit witness re-runs both scoped predicates; round 4 measured the
  unscoped phrase predicate at 87 hits, 18 of the 21 it would have filtered to being frozen
  records, so its zero-result witness was red by construction and blind to three of the four argv
  carriers (B1). Every `st=1` source the render loop has is KEPT by name, `unstarted` is the fifth
  summary word for a row with no verdict file under no wall breach, and the surviving emissions —
  the appended parity clause, the beneath-row grep, `NO cost verdict was issued`, the `WITHHELD`
  line — are stated so a builder cannot depart from a non-goal by accident (H2, H1). The reading
  witness is unit 3 AC4's ratified trailer rule, `untrailed` beside `walled`, the executed count a
  ninth column, the two trailer-less suites declared in the file header; ten of the fourteen DoD
  rows baseline at (0, 0) and an early `exit 0` produces that pair (H3). The parity-reached arms
  are enumerated in §7 beside the factor set and AC6 guards the unenumerated ones (H1).
- rev-5 · 2026-09-14 · §1 · §2 S1 through S5 · §3 · Edges · §4 · §5 · §6 AC1 through AC11 · §7 ·
  F4 · F6 · §10 · folded spec-audit round 3 (BLOCKED, 1 blocker, 13 highs, 5 mediums, 1 low, 20
  confirmed rows in 12 defects, precision 0.44, CONVERGING from 2). The lever: the pooled verdict
  is now PARITY (new S4) — (rc, `^FAIL` count) against the calibrated baseline, the exit derived
  from `killed + walled + unrun + mismatched + soundness`, all four counts on the summary from the
  lists the runner already keeps — which makes GREEN the landing criterion again and dissolves the
  summary-token witness that counted one of three non-completion classes (B1), the post-flip
  carriers still promising a GREEN the old exit could not print (H2, M3), and the recorded DoD
  command printing RED on success forever (H3). The `^FAIL` count is the positive artifact beside
  rc, so a 0.3 s crash exiting 1 cannot match a baseline of three (H4); rc and fails follow the
  LATEST reading while seconds stay monotone, a mismatch names its acceptance, and `--reset <row>`
  narrows the calibrate and gets AC10 (H5, M1). The carrier predicate's eight lines are classified
  by ROLE: four DoD carriers go dark and flip, four pointers are byte-unchanged at both steps — the
  `SESSION-KICKOFF.md:169` re-wording and the `AGENTS.md:519` swap withdrawn, the manifest measured
  10 under its cap (H1). The fixture gets a charter stub with one registry row so the tag resolves
  there (H6, M4). The `run-selftests self-test` leg is named as already killed at its 300 s ceiling,
  its re-declaration owed at the final pass from that pass, `gate-legs.json` and its budget row in
  Files touched (H7). The absent-margin refusal gets its arm and AC1's red-when (M2); the oracle
  cite is unit 3 AC6 and the README's rule, not AC11 (M5); the typed `three` is dropped (L1).


- rev-4 · 2026-09-14 · §1 · §2 S1 through S4 · §3 · §4 · §5 · §6 AC1 through AC9 · §7 · F5 · F6 ·
  §10 · folded spec-audit round 2 (BLOCKED, 2 blockers, 15 highs, 7 mediums, 1 low, 25 confirmed
  rows in 11 defects, precision 0.49, CONVERGING from 3). The landing criterion is no longer GREEN,
  which the red-by-design oracle forbids, but the pooled summary's `killed 0` / `rc-mismatched 0` /
  `fingerprint MATCHED`, the kit runner's pooled branch gaining those two counts (B1). The calibrate
  wall is the serial SUM undivided, since the divided form is killed by slot 54 of the sweep record
  the spec cites; the step-one red lands without the flip (B2, H1). The flip REMOVES the serial DoD
  pass: `kit.toml:126` becomes `--checks`, the binding sentence and `SESSION-KICKOFF.md:169` are
  re-worded at the flip, `--selftests --serial` is the cost pass on demand (H2, M1). `AGENTS.md:519`
  takes no dark spelling, eight bytes for eight at the flip, measured 9 under its cap (H3). The
  reading witness is rc captured with the bound floored at the serial budget, `derive-ceilings`'
  ok-only clause DEPARTED from by name (H4, M3). Readings are written after `FP_AFTER`; the fixture
  evidence file is tracked (H5). The seed covers both tokens the arms produce and the rows arms
  append; every pooled arm re-cut is enumerated (H6, M4). §7 marks the nine held legs and names
  `GATE_FULL=1 GATE_SELFTESTS=1` as the final pass's kit-work invocation (H7, M5). The carrier set
  is a stated predicate whose output is the list, `:142` excluded by it (H8, M2). The node is the
  registry tag via `_resolve_node_tag`'s rule (M6). The `unattended skill wiring` claim is dropped
  and the parity arm's home is `govkit selfcheck` (M7); §7's derivation sentence corrected (L1).


- rev-3 · 2026-09-14 · §1 · §2 S1 through S4 · §3 · Edges · §4 · §5 · §6 AC1 through AC9 · §7 ·
  F3 · F4 · F5 · §10 · folded spec-audit round 1 (BLOCKED, 3 blockers, 13 highs, 11 mediums, 1
  low, 28 confirmed rows in 11 defects, precision 0.52). The four scope decisions first: the
  population is the DoD command's RESOLVED one (`--kit tools/unattended --list`, fourteen rows at
  this base, never typed — B1, B2, H1, M1); the flip lands DARK here and flips as the build's
  landing step on the merged tree after the pasted GREEN, with the landing order and the red
  outcome written (B3, H2, M2); an uncalibrated row REFUSES and the factor header, its arm and its
  verdict text are retired, the graded wall derived from the evidence bounds and the calibrate wall
  from the serial budgets (H3 through H7); the rule is reused WHOLE — readings only from rows that
  exited on their own with a RED calibrate on a killed one, every row raised monotone on every
  calibrate, `--reset <row>` as the lowering path, node in the key (H8 through H11, M10). Then the
  mechanical set: the fixture rebuild with a seeded margin and evidence file and the two factor-shape
  arms re-cut (H12); AC4's witness is the fixture's `--rank` plus the real tree's `pooled@` grep and
  an unchanged unbacked list, since `--rank` exits 1 at this base for unit 3's derived shard-8 row
  (H13, M3); the carriers enumerated by grep as eight lines in six files with `kit.toml:126`
  declared the cost line and AC5's red-when corrected (M4, M5); the `kit.toml` `project-owned` rule
  and the manifest re-stamp in Files touched (M6 through M9); §7 re-derived over `gate-legs.json`
  (M11); the unparseable-file arm and the `--calibrate`-off-`--pooled` refusal (L1). AC6 is no
  longer a flip diff, since no flip lands here; it is the existing serial arms unchanged.


- rev-2 · 2026-09-14 · §2 S1 · S3 · S4 · §3 · §4 · §6 AC1 · AC3 · AC5 · AC6 · §7 · F1 · §10 · base ·
  pre-audit correction of a seam claim verified false at source, plus the owner rulings. rev-1 put
  pooled readings in `ceiling-evidence.txt` keyed by name and condition token; that file is
  GENERATED from `<git-dir>/gate-run/*/*.leg` by `derive-ceilings.py --write`, has five columns and
  no condition, says `Do not hand-edit`, and its `--check` prints a stale-row note for every row
  naming no manifest leg — so a self-test row there is a second writer to a generated artifact. The
  store is now the runner's own `selftest-pooled-evidence.txt`, same monotone/margin RULE, the
  margin READ from `ceiling-margin.txt`. The 2026-09-14 ruling (no gate until every unit is built)
  moves AC3's and AC5's real-row observations to the build's final gate pass; AC6 becomes a diff.
  The `ceiling evidence` gate leaves §7, since this unit no longer touches its file. Base bumped to
  `1c736fd9`, where units 3 and 4 are CLOSED and the eight rows exist.
- rev-1 · 2026-09-13 · initial draft, from `TOOL-aBatchedArm-4`'s three audit rounds, which
  specified this unit's shape while refusing it inside that one: the evidence-derived bound (r1 B5),
  the flip landed dark and owned here (r2 B1), and the declared bootstrap. Authored now rather than
  after unit 3 because memory hygiene check 14 reds on a cited id with no spec, and the id was cited
  at `9b00bc7b`.
## 10. Reuse audit


- **The seam is the RULE in `tools/run-gates/derive-ceilings.py`** — worst-observed, monotone,
  `max(floor, fraction x max)`, refusing with no evidence — and the margin file it reads,
  `tools/run-gates/ceiling-margin.txt`, verified at source. Its FILE, `ceiling-evidence.txt`, is
  NOT reused: verified at source on 2026-09-14, it is generated from bar leg files, keyed by leg
  name with no condition column, and its header forbids hand rows; rev-1's claim that it was the
  seam was wrong. The condition token `pooled@<outer>x<inner>` is the runner's own at the text
  `SWEEP_CONDITION=`. The `--rank` refusal of `pooled@` at the text `REFUSED = [re.compile(r"pooled@")]`
  is REUSED by keeping pooled readings OUT of the budget file. The
  reuse probe was run —
  `python tools/codebase-map/reuse_lookup.py "derive a pooled hang bound from observed readings under a condition token with monotone evidence and declared headroom"`
  — and returned `read_text`, `read` and `derive_scope`, none of which is this seam; it reports
  `unscanned layers: .sh` and `derive-ceilings.py` is Python it did not rank, so its result is not
  evidence either way. The seam was found by reading `derive-ceilings.py` and the two files beside
  it.
- **The parts of that rule this spec now carries by name**, because round 1 found the reuse was
  the file's header and not the rule: `read_runs` counts completed runs only (`derive-ceilings.py`,
  the text `may have failed fast`); `--write` raises every measured row monotone; `--reset <leg>` is
  the one lowering path; `GOV_NODE` is its node spelling, which the runner reuses with the registry
  table as the fallback the script does not have (it defaults to `a`, which is wrong on every other node
  and is not reused; the runner's fallback is the registry table, never a hostname).
- **The `ok`-only clause of that rule is DEPARTED from**, by name: unit 3's shard rows exit 1 when
  complete, so an ok-only reader refuses them forever; the replacement is the serial-budget floor
  under the bound, which makes a fast red harmless. Round 2 caught the paraphrase claiming the
  clause was reused; it is not.
- **The node resolver is `tools/drift-audit/drift_report.py`'s `_resolve_node_tag`** — `USERNAME`
  or `USER` against the charter's §2 registry table, read from the charter file at the repo root
  the way `run-gates.gov.test.sh` spells it — whose rule S3 reuses, refusing where it returns
  nothing; `TOOL-aCollapsedScan-9` (OPEN) names the per-node reading as a candidate.
  `derive-ceilings.py`'s `GOV_NODE ... or "a"` default is the same class and is a backlog follow-up,
  not this unit's.
- **The completion oracle is unit 3's AC6 and the build README's rule** — the `FAIL` line set plus
  the executed count — and the READING witness is unit 3 AC4's ratified trailer rule, reused by id:
  a reading exists only when the filed output carries the suite's trailer, `PASS (` or the
  executed-count line or the shard trailer; the `^FAIL` and executed counts S2 records are the
  cheap half of the oracle; the `ab-arm-never-did-the-work` gotcha is the class. The runner's
  non-completion lists at the text `killed=0; walled=""; unrun=""` and its other `st=1` sources —
  the could-not-start and unresolved rows and the pool-ran-wider guard — are reused as the summary's
  counts rather than re-derived, every one of them, because round 3 and round 4 each found a summary
  counting fewer outcomes than the loop has. `TOOL-aPooledSweep-2` S2 is the per-row withheld-cost
  rule S4 preserves.
- **The carrier-parity arm** round 1 asked for has its home in `govkit selfcheck`, the one reader of
  every `kit.toml`, or `tools/check-playbook-parity.sh`, whose job is retyped constants against the
  source that owns them — named here and not built by this unit. The `unattended skill wiring` leg
  is `adopt-unattended.sh --check` and reads neither carrier, so rev-3's claim that it did is
  withdrawn.
- **The retrieval arguments, verbatim:**
  `python tools/memory-recall/query.py "why does the self-test runner run suites serially by default and pool only under sweep, and what was measured about cost attribution under contention" --terms "run-selftests OUTER pool sweep serial budget contention dilation attribution width verdict withheld mode declared"`.
  Run for unit 4; it surfaced `TOOL-dRetiredFork-40`, `TOOL-aPooledSweep-2` and the full-sweep record
  this unit's §4 rests on.
