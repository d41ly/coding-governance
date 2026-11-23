# TOOL-dQuietDisk-18 — `govkit apply` reads both of its verdict maps through the target's reuse cache

**Status:** CLOSED · rev-4 · 2026-11-22 · node d · Tier-2 · base 7b8c737b · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-22-build-TOOL-dQuietDisk-18-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-18-1-acceptance-ledger.md) | journal | — |
| [2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md](../build/2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-18-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-18-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-18-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-18-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md) | research | TOOL-dQuietDisk-6 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 |
| [2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md) | diff-review | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit apply` runs the target's whole bar twice, once before it writes and once after
(`tools/govkit/govkit.py@17ca55fbb521:7864` and `:8566`), though the target's reuse cache can already
hold a green verdict for most legs and the install moves the inputs of few. This unit runs both reads
with the runner's reuse mode on, so a leg whose input key holds an `ok` is reused rather than
executed, while "green before, red after" stays computed per leg and a red after is still refused.

The saving, counted from the code:

- **AFTER**, the large half. The BEFORE read runs on a clean tree, so it writes a cache entry for
  every leg that executed `ok`. The AFTER read then reuses each guarded leg whose guard the install
  did not reach, less the sampled quarter. It executes the legs the install reached, every
  unguarded leg (keyed on the whole-tree fingerprint, which any write moves), and the sampled ones.
  Today it executes every leg its guards do not skip.
- **BEFORE**, usually nothing. apply runs both reads under `GATE_REGEN_CHECK=0`
  (`tools/govkit/govkit.py@17ca55fbb521:6359`). The runner's environment digest hashes every
  `GATE_*` name except the reuse knobs, the turnstile names, the run id and the two bases
  (`tools/run-gates/run-gates.sh@7848b83f22c0:3800-3802`). So no entry an operator's plain bar wrote
  matches the BEFORE read's keys. It reuses only what an earlier apply's read wrote on the same tree
  under the same environment: a retried or resumed apply. Section 8 holds the fork this raises.
- **The cost.** The AFTER read now builds input keys, which today's AFTER read skips: keys are built
  only when the mode is not `off` or the tree is clean (`tools/run-gates/run-gates.sh@7848b83f22c0:3955`).
  For plain guards that is two git processes [DERIVED from `#build_input_keys`: one `ls-files -s`
  over the guard union, one `hash-object --stdin-paths`], plus two per leg whose guard the bulk path
  refuses (`#input_key`). Each reused leg saves its own whole process tree. So the read launches
  fewer git processes whenever the reused legs between them spend more than that.

govkit's own git spawns do not change. AC8 measures the saving on a real runner.

## 2. Scope (IN)

- **S1** — `read_gate_verdicts(target, gr, reuse=False)` (`tools/govkit/govkit.py#read_gate_verdicts`)
  gains one keyword argument. When `reuse` is true the runner's environment carries `GATE_REUSE=1`
  beside the `GATE_REGEN_CHECK=0` it carries today. When false it is today's call. The parse is
  unchanged. The default keeps the suite's direct two-argument call
  (`tools/govkit/selftest.py@c2b02d780af9:19328`) as it is. Observed by AC1 and AC5.
- **S2** — `_cmd_apply` passes `reuse` to both reads, the BASELINE read and the AFTER read, from one
  value read once per apply by S5's reader. Observed by AC1 and AC2.
- **S3** — A leg the BASELINE read prints as `reused` counts as green before, at the three places that
  test a before state:
  - the dead-probe refusal (`tools/govkit/govkit.py@17ca55fbb521:7870`);
  - the `on_baseline_red` reds (`:7876`);
  - the green-before rows of the AFTER comparison (`:8568`).

  One function, `derive_leg_state(state)`, maps `reused` to `green` and returns every other state
  unchanged, and all three read through it. Observed by AC2 and AC3.
- **S4** — The receipt records `reused` as `green` in `baseline.legs` and in `after`, through
  `derive_leg_state`. `baseline.legs` is a mapped copy, taken where `baseline["legs"]` is set
  (`:7865`), because `before_map` itself stays the comparison's input. `after` is mapped where the
  RECEIPT step sets it (`:8608`). The comparison and its printed notes read the runner's own word.
  Observed by AC4.
- **S5** — The switch: a new policy key `install.baseline`, `allowed = ["reuse", "run"]`, default
  `reuse`, with its `summary` and `usage`, owner `dQuietDisk`, in `tools/policy/catalogue.toml`
  after `install.steps`, the last `install.` row. `run` is today's behaviour. One reader,
  `read_baseline_mode(target, gr)`, returns `reuse` only when both of these hold:
  - `read_policy_value("install.baseline", target)` answers `reuse`;
  - `gr` declares a non-empty `observed_reused`.

  Otherwise it returns `run` and prints one line naming why. A target that does not declare
  `observed_reused` never parses a `GATE reuse` line. Its reused legs would vanish from both maps,
  and a leg skipped after a green would no longer be refused. A reader refusal, no policy kit, or a
  value outside the two also reads as `run`. A failed read costs a saving, never a verdict, unlike
  `read_retired_edits_mode`, which refuses (`tools/govkit/govkit.py@17ca55fbb521:9627`). Observed by
  AC5.
- **S6** — When the mode is `reuse`, the apply prints one more line after today's BASELINE line:
  `govkit apply — the baseline will RUN, reusing each leg the target's reuse cache holds green`.
  Today's line, which prints the target's argv (`:7861-7862`), stays in both modes, because the
  block's contract is that the argv it runs is printed and recorded (`:7854-7857`). Observed by AC1.
- **S7** — `help/reference/policy.md` gains the key's section, re-rendered by
  `python tools/playbook/render_playbook.py --reference`. Observed by AC6.

## 3. Non-goals (OUT)

- Running only the legs whose guards meet the written files by a matcher in govkit. The runner's
  input key already composes each leg's guard listing, its share of the dirty files, its manifest
  row and, for an unguarded leg, the whole-tree fingerprint (`tools/run-gates/run-gates.sh#build_key_text`).
  So a leg the install reaches gets a new key and executes. A second matcher would be a second
  answer to that question.
- `GATE_REUSE_SAMPLE` and the age bound. The runner still executes a quarter of the reusable legs
  (`tools/run-gates/run-gates.sh@7848b83f22c0:3818`, `:4021`) and any leg reused ten runs in a row
  (`:4009`). This unit leaves both to the runner.
- The runner's environment digest, and with it the BEFORE read's misses (section 1, section 8). It is
  the run-gates kit's contract, and every reuse mode reads it.
- `govkit update`'s kit checks and batch reads: TOOL-dQuietDisk-16 and -17.
- A target whose runner predates the reuse cache (TOOL-aSparedSpawn-13), or whose wrapper clears
  `GATE_REUSE`. Such a runner executes every leg, which is today's behaviour, and nothing here
  detects it.
- The ask DEPL-dSettledRoster-2: apply runs the target's command twice, and that decision was never
  owner-reviewed. This unit keeps both runs and makes them cheaper, and the ask stays open.

### Edges

- **consumes-from** external — the target's runner honouring `GATE_REUSE` and printing `GATE reuse <name>` through the `observed_reused` template, which run-gates has shipped since TOOL-aSparedSpawn-13 (`tools/run-gates/kit.toml@eb6f4f2b5706:315`).

## 4. Design

### Why the runner's reuse mode answers both halves

The runner reads `GATE_REUSE` once and unsets it before any leg runs
(`tools/run-gates/run-gates.sh@7848b83f22c0:2850-2852`). With it set and `GATE_FULL` unset, the mode
is `env` (`:3705`, `:3721`). In that mode it reuses a leg whose key holds an `ok` entry under the git
common dir's `gate-cache`, and prints `GATE reuse <name>` (`:4007`, `:4485`). Whatever the mode, it
writes an entry for every leg that executed `ok` on its first attempt, on a tree that was clean at
the start and did not move (`:6047`). So:

- **BEFORE.** The tree is clean, so every leg that executes `ok` is cached. A leg reuses only an
  entry keyed under the same environment digest, which in practice only an earlier apply's read
  wrote (section 1).
- **AFTER.** The tree is dirty with what apply wrote, so nothing is cached. A guarded leg's key moves
  exactly when the install touched a path under its guard or rewrote its manifest row. An unguarded
  leg's key moves on any write. Those legs execute, and the rest reuse the entries the BEFORE read
  wrote.

A key composes its own guard listing and dirt share (`#build_key_text`), so the selection rule stays
the runner's and is never restated in govkit.

### The comparison

```python
def derive_leg_state(state):
    return "green" if state == "reused" else state

# BASELINE
if before_map and not any(derive_leg_state(v) in ("green", "red") for v in before_map.values()):
    raise Refusal("DEAD PROBE: ...")          # unchanged text
reds = [n for n, v in before_map.items() if derive_leg_state(v) == "red"]
# AFTER: `b = derive_leg_state(before_map.get(nm))`, then today's table
```

The cache holds only `ok` entries (`tools/run-gates/run-gates.sh@7848b83f22c0:4007`), so a leg reused
before is a leg proven green under the same input key. A leg reused after keeps today's row: `green`
before and `reused` after prints the carried note and is no failure
(`tools/govkit/govkit.py@17ca55fbb521:8577-8579`). A leg green before and red after is refused as
today (`:8569-8570`), whether it was reused or executed before.

### The receipt

`baseline.legs` and `after` are both taken through `derive_leg_state` (S4). Under `reuse`, a leg
reused and a leg executed green record the same word. So the receipt is the same bytes whichever legs
the sample drew, and the same bytes a `run` apply writes for the same verdicts. The `attestations`
key TOOL-dQuietDisk-14 added is derived from gov's root and commit
(`tools/govkit/govkit.py@17ca55fbb521:8612`), so two applies from one gov commit agree on it too.

### Adopters

- incms declares `observed_reused` (incms `.governance/deploy.toml#gate_runner.observed_reused`). Its
  command, `scripts/gov-bar.sh`, keeps `GATE_REUSE`: its `unset` line drops `GATE_REUSE_PUSH` and no
  other reuse knob. So once its govkit is updated, its applies read in the `reuse` mode.
- nicocares declares only `observed_ran`, `observed_failed` and `observed_skipped`
  (nicocares `.governance/deploy.toml#gate_runner`). It reads as `run`, with one line
  naming the missing template, until its descriptor gains one.
- The change reaches both only through a minted govkit and `govkit update`.

### Inventory

- The policy key `install.baseline`, values `reuse` and `run`.
- The function `derive_leg_state` in `tools/govkit/govkit.py`, cell `py.function`; lexicon `--suggest` OK.
- The function `read_baseline_mode` in `tools/govkit/govkit.py`, cell `py.function`; lexicon `--suggest` OK.
- The keyword argument `reuse` of `read_gate_verdicts`.

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/govkit/selftest.py` · `tools/policy/catalogue.toml` ·
`help/reference/policy.md` · `memory/map/generated/symbols.json`

- The main loop re-renders gov's policy mirror with `policy.py mirror --write` after the pass commit, as it did for unit 7 (`08b1d3c42`).
- The two new column-0 functions join the codebase map's symbol index, re-rendered by
  the codebase map's generator, `gen_map.py --write`, never by hand. No leg, kit or dossier is added, so
  the map's other generated files do not move.

### Shared paths at order 3

- On the order-3 specs as they read at this re-ground, TOOL-dQuietDisk-28 shares
  `memory/map/generated/symbols.json` with this unit, so the two build in sequence.
- TOOL-dQuietDisk-6, -10, -12 and -13 name no path of this unit's.
- TOOL-dQuietDisk-11, at order 4, also writes `tools/govkit/selftest.py`, and builds after this unit,
  as the spec brief asks.

### Alternatives rejected

- Recording the runner's own word, `reused`, in the receipt. The receipt would differ from a `run`
  apply's for identical verdicts, and would differ between two applies of one tree by the sample's
  draw. That fails the build brief's acceptance that apply writes identical receipts on the fixtures.
- A new receipt field listing the carried legs. It changes the receipt schema every adopter's govkit
  reads, a shared contract (`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`,
  veto 2), for a fact the run record already holds.
- `GATE_BASE=HEAD` for the AFTER read, so legs untouched by the writes skip. A skipped leg after a
  green one is today's "the install broke its guard" refusal (`tools/govkit/govkit.py@17ca55fbb521:8580-8582`).
  Under that base a skip could no longer tell an untouched leg from a broken guard.
- Dropping `GATE_REGEN_CHECK=0` from the reads, so the BEFORE read meets an operator bar's keys. The
  runner's generated-output preflight would then exit before any leg line on a stale output, and both
  maps would parse empty (DEPL-aPrimedIndex-1, `tools/govkit/govkit.py@17ca55fbb521:6355-6357`).
- A govkit-side guard matcher over the written files: a second statement of the runner's rule.

## 5. Production-readiness checklist

- security: no new write path. The reads still execute the target's own command, printed and
  recorded as today (S6 keeps the argv line). `GATE_REUSE` makes that command trust its own cache in
  the target's git common dir, which only the target's own runs write. A reuse rewrites its entry's
  age count in place (`tools/run-gates/run-gates.sh@7848b83f22c0:4025-4027`), a write by the
  target's runner in the target's own store. The write surface does not widen.
- perf / scale: the AFTER read falls to the legs the install reached, every unguarded leg and the
  sampled quarter. The BEFORE read is unchanged unless an earlier read wrote its keys (section 1).
- error / empty / loading states:
  - an unreadable or foreign `install.baseline`, or a descriptor with no `observed_reused`, reads as
    `run`, named on one line;
  - a runner that ignores `GATE_REUSE` executes every leg;
  - a cache entry the runner cannot read executes its leg (`tools/run-gates/run-gates.sh@7848b83f22c0:4007`);
  - a target dirty at BASELINE caches nothing, so the AFTER read executes as today.
- observability: the BASELINE mode line (S6), and the runner's `GATE reuse` lines in the output
  apply already parses.
- risks: a leg whose guard is too narrow is reused after an install that reached its real inputs.
  The runner states that limit for its lineage reuse
  (`tools/run-gates/run-gates.sh@7848b83f22c0:4048-4052`), and it holds for any reuse by key. The
  sample and the age bound are its standing check, and `install.baseline = "run"` is the escape.
- testing: AC1 to AC6 are probes and fixtures of this unit's code. AC7 and AC8 are the main loop's.
- migration: additive. An unset key reads the default, `reuse`, and no receipt field is added.
- user docs: `help/reference/policy.md`'s section for the key (S7).

## 6. Acceptance criteria

- **AC1** — When `govkit apply` runs on a fixture target whose `[gate_runner]` declares
  `observed_reused` and whose command is a stub runner that appends `GATE_REUSE=<value>` to a log and
  prints one `GATE` line per leg, the log holds `GATE_REUSE=1` twice under
  `install.baseline = "reuse"`. The apply prints both `the baseline will RUN, from this target's own`
  and `the baseline will RUN, reusing`.
  Red when: either read runs without `GATE_REUSE`, or the argv line is gone.
- **AC2** — When the stub prints `GATE reuse a` and `GATE ok b` before the write, and `GATE reuse a`
  and `GATE FAIL  b` after it, `govkit apply` exits non-zero naming
  `leg 'b' was green before this install and is red after`, and names nothing about `a`.
  Red when: the red after is not refused, or the reused leg is.
- **AC3** — When the stub prints `GATE reuse a` before and `GATE FAIL  a` after, the apply refuses
  naming `leg 'a' was green before this install and is red after`. When it prints only `GATE reuse`
  lines before, the apply raises no `DEAD PROBE`.
  Red when: a leg reused before is read as no state, or an all-reused baseline is refused as dead.
- **AC4** — When the stub prints `GATE reuse a` before and after, the written
  `.governance/install.json` holds `"a": "green"` in `baseline.legs` and in `after`. Its bytes equal
  those of an apply from the same gov commit whose stub printed `GATE ok a` both times.
  Red when: the receipt records `reused`, or the two receipts differ.
- **AC5** — With the fixture target's committed `.governance/policy.toml` and its descriptor varied:
  - `install.baseline = "run"`: the stub's log holds no `GATE_REUSE` line;
  - `policy-file.on-invalid = "refuse"` with `install.baseline = "maybe"`, so the policy reader
    refuses: the apply prints one line naming `install.baseline`, completes, and the log holds none;
  - `install.baseline` unset and a descriptor with no `observed_reused`: the apply prints one line
    naming `observed_reused`, and the log holds none.

  Red when: `run` still passes `GATE_REUSE`, a refused read refuses the apply or turns reuse on, or a
  target that cannot parse `GATE reuse` is read in the `reuse` mode.
- **AC6** — When `python tools/playbook/render_playbook.py --reference` runs,
  `grep -c '^## .install.baseline.$' help/reference/policy.md` prints 1, and
  `python tools/policy/policy.py lists --check` exits 0.
  Red when: the key has no section, or it lacks a summary or a usage.
- **AC7** — When the main loop runs `extract-arms.sh` over the `govkit selftest` leg at the build base
  and at this unit's commit, every apply arm whose target declares `kind = "manifest"` keeps its
  verdict. `python tools/govkit/govkit.py check --target C:/projects/incms/main` and
  `--target C:/projects/nicocares/main`, run read-only from gov, read the same before and after.
  Red when: an arm changes verdict, or a check line changes.
  permission: a role pass may not run the deployer's suite (`tools/unattended/gate-guard.js` row
  D4); the main loop observes this at VERIFYING.
  fixture: AC1 to AC5's stub-runner targets are the new arms, built by `build_target` in the
  deployer's suite; no target under `tools/govkit/fixtures/` declares a manifest runner today.
- **AC8** — The main loop builds one scratch target and copies it twice, then runs
  `govkit apply --target <copy> --write` once per copy, under `install.baseline = "run"` and
  `"reuse"`, each with `GIT_TRACE2_EVENT` pointed at its own empty directory. The target:
  - runs gov's own run-gates kit at this unit's commit as its `[gate_runner]` command, as a
    copy-installed adopter holds it, with `observed_reused` declared;
  - has a manifest of three legs, `ga` guarded on `a/`, `gb` guarded on `b/` and `gall` unguarded,
    each running `git rev-parse HEAD` three times;
  - gets nothing under `a/` or `b/` from the apply, whose kit is the one `runner_target` selects.

  When the `reuse` copy's AFTER read prints at least one `GATE reuse` line, its trace directory holds
  fewer files than the `run` copy's, and the two receipts hold equal `baseline.legs` and `after`.
  Red when: a `GATE reuse` line after comes with no fewer trace files, or the receipts' maps differ.
  permission: a role pass runs no gate runner (`tools/unattended/gate-guard.js` row G2); the main
  loop observes this at VERIFYING and records the two counts in TOOL-dQuietDisk-19's record.
  fixture: the scratch target is the main loop's, under the session scratch root, never a worktree.

## 7. Gates

`govkit selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix` · `scratch-guard self-test` · `routed-commits selftest`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 · a stub runner that prints `GATE reuse` before and `GATE FAIL` after; the arm reds when `derive_leg_state` is bypassed and the red after passes · none

## 8. Open questions

- **F1 — the BEFORE read's misses.** Every key's environment digest hashes `GATE_REGEN_CHECK`, which
  apply sets and an operator's bar does not, so the BEFORE read reuses almost nothing (section 1).
  Options:
  - (a) keep this unit as written: the AFTER saving now, the BEFORE saving on a retried apply;
  - (b) add a run-gates unit that leaves `GATE_REGEN_CHECK` out of the digest, beside `GATE_BASE`.
    It is the run-gates kit's contract, every reuse mode reads it, and it reaches adopters only with
    their next run-gates.

  Recommendation: (a) here, and file (b) as an ask in this build's `BACKLOG.md`, so the build's owner
  decides whether the run takes it. By M2 it is a separate mechanism in another kit, and the digest's
  exclusions were set by the reuse cache's own builds.

  RESOLVED (agent, 2026-11-22, delegated): (a). Dropping `GATE_REGEN_CHECK` from the runner's key
  hash is a run-gates change, so it is filed as ask TOOL-dQuietDisk-31 in this build's `BACKLOG.md`.

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. The one minted
  function the lexicon refused, `effective_before`, is `derive_before_state`, checked by `--suggest`,
  everywhere the spec spells it. No criterion had the pass run a suite, a `--selftest`, a gate leg
  or the bar: AC7's suite reading was already the main loop's.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  4 and section 10 the rejected alternative's build-method citation names its tag, and dWitnessedBar's
  changed-line count is marked PINNED. Design, scope and acceptance unchanged.
- rev-4 · 2026-11-22 · §1 to §10 · S1 S3 S4 S5 S6 · AC1 AC4 AC5 AC8 · F1 · re-grounded at 7b8c737b0
  (orders 1 and 2 built), under `2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task`. Every citation
  is re-pinned to its blob at HEAD. What moved:
  - The runner's environment digest hashes the `GATE_REGEN_CHECK=0` apply sets, so the BEFORE read
    meets no plain bar's keys. Section 1 now counts the saving as the AFTER read's, less the key build
    that read now pays. The goal is unchanged; the saving it was estimated at is not. F1 records the
    digest fork, and AC8 measures the saving on a real runner, the build brief's "with fewer git
    processes" for apply.
  - nicocares declares no `observed_reused`, so S5's reader also requires the template, and AC5 gains
    that case. Without it, a reused leg would vanish from both maps.
  - S6 keeps today's argv line in both modes. Replacing it under `reuse` would have broken the block's
    printed-argv contract.
  - S1's argument is a keyword with a default, so the suite's direct two-argument call stands.
  - S4 maps `baseline.legs` as a copy, since `before_map` is shared with it by reference.
  - AC4 names TOOL-dQuietDisk-14's `attestations` key.
  - The function is `derive_leg_state`, since it maps the after map too. `read_baseline_mode` is new.
  - Files touched gains `memory/map/generated/symbols.json`, Gates gains `recall floor`, and the path
    shared with TOOL-dQuietDisk-28 is named.
  - dWitnessedBar has landed (`40def53f7`).
- rev-4 · 2026-11-22 · §4 §8 · F1 · the run's ruling: F1 is resolved as (a), with (b) filed as ask
  TOOL-dQuietDisk-31. `.governance/policy.json` leaves Files touched and the pass's steps, because the
  main loop re-renders the mirror after the pass commit. Design, scope and acceptance unchanged.

## 10. Reuse audit

The seam is the runner's own reuse cache and its `env` mode (`tools/run-gates/run-gates.sh`, the
reuse block, TOOL-aSparedSpawn-13). It already answers, per leg, "is this leg's verdict already held
for these inputs". The switch reads through `read_policy_value` in `tools/govkit/govkit.py`.

`python tools/codebase-map/reuse_lookup.py "read recorded leg verdicts from the reuse cache instead of running the target bar"`
ranked name-token neighbours, `read_policy_value` among them and no cache reader. So govkit reads no
cache file itself, and asks the target's runner through the knob it already honours.

No existing policy key covers apply's baseline. The catalogue's six `install.` rows at `7b8c737b0`
are `install.from`, `install.guards`, `install.deprecation-window`, `install.on-shim-call`,
`install.retired-edits` and `install.steps`, and none is about the baseline.

Chain owners:
- dSafePassage (Supersession, govkit apply). Its CLOSED specs 5, 10 and 25 to 27 do not touch
  `read_gate_verdicts`.
- dWitnessedBar (Test). It has landed, merged into this build at `40def53f7`. Of its specs, only
  units 60, 63, 65 and 67 name `GATE_REUSE`, each for a hook or post-merge scrub list and never for
  apply's reads. Its unit 16 names "baseline" only for the map's own registries.

The recall probe surfaced DEPL-dSettledRoster-2, named in §3.

Recall terms used: `python tools/memory-recall/query.py "how does govkit apply compare the target bar before and after the install, and can it reuse cached verdicts" --terms "govkit apply baseline read_gate_verdicts before_map after_map GATE_REUSE reuse cache gate-cache observed_reused input key GATE_REGEN_CHECK digest"`
