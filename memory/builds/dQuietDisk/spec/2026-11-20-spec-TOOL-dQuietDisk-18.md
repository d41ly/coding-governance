# TOOL-dQuietDisk-18 — `govkit apply` reads both of its verdict maps through the target's reuse cache

**Status:** SPECCED · rev-3 · 2026-11-22 · node d · Tier-2 · base 59e882af · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit apply` runs the target's whole bar twice, once before it writes and once after
(`tools/govkit/govkit.py@609cd40b1:7678` and `:8380`), though the target's reuse cache already holds a
green verdict for most legs and the install moves the inputs of few. This unit runs both reads with
the runner's reuse mode on, so a leg whose input key holds an `ok` is reused rather than executed,
while "green before, red after" stays computed per leg and a red after is still refused.

## 2. Scope (IN)

- **S1** — `read_gate_verdicts(target, gr, reuse)` (`tools/govkit/govkit.py#read_gate_verdicts`)
  gains one argument. When `reuse` is true the runner's environment carries `GATE_REUSE=1` beside the
  `GATE_REGEN_CHECK=0` it carries today; when false it is today's call. The parse is unchanged.
  Observed by AC1 and AC5.
- **S2** — `_cmd_apply` passes `reuse` to both reads, the BASELINE read and the AFTER read, from
  one value read once per apply (S5). Observed by AC1 and AC2.
- **S3** — A leg the BASELINE read prints as `reused` counts as green before, at the three places
  that test a before state: the dead-probe refusal, the `on_baseline_red` reds, and the
  green-before rows of the AFTER comparison. One function, `derive_before_state(state)`, maps `reused`
  to `green` and returns every other state unchanged, and all three read through it. Observed by AC2
  and AC3.
- **S4** — The receipt records `reused` as `green` in both `baseline.legs` and `after`, through the
  same mapping, applied once where `_cmd_apply` builds the receipt document. The comparison and its
  printed notes read the runner's own word. Observed by AC4.
- **S5** — The switch: a new policy key `install.baseline`, `allowed = ["reuse", "run"]`, default
  `reuse`, with its `summary` and `usage`, owner `dQuietDisk`, in `tools/policy/catalogue.toml`
  beside the other `install.` rows. `run` is today's behaviour. `_cmd_apply` reads it with
  `read_policy_value("install.baseline", target)`, as `read_retired_edits_mode` reads its key. A
  read the policy reader refuses, no policy kit, or a value outside the two reads as `run` and prints
  one line naming the key and why: a failed read costs a saving, never a verdict. A value outside
  the set normally never arrives, since the reader answers it by `policy-file.on-invalid`. Observed
  by AC5.
- **S6** — The apply's BASELINE line names the mode: `the baseline will RUN, reusing each leg the
  target's reuse cache holds green` under `reuse`, today's line under `run`. Observed by AC1.
- **S7** — `help/reference/policy.md` gains the key's section, re-rendered by
  `python tools/playbook/render_playbook.py --reference`. Observed by AC6.

## 3. Non-goals (OUT)

- Running only the legs whose guards meet the written files by a matcher in govkit. The runner's
  input key already composes each leg's guard listing, its share of the dirty files, its manifest row
  and, for an unguarded leg, the whole-tree fingerprint (`tools/run-gates/run-gates.sh#build_key_text`),
  so a leg the install reaches gets a new key and executes. A second matcher would be a second
  answer to that question.
- `GATE_REUSE_SAMPLE` and the age bound. The runner still executes a quarter of the reusable legs and
  any leg reused ten runs in a row (`tools/run-gates/run-gates.sh@609cd40b1:3719` and `:3906-3910`);
  this unit leaves both to the runner.
- `govkit update`'s kit checks and batch reads: TOOL-dQuietDisk-16 and -17.
- A target whose runner predates the reuse cache (TOOL-aSparedSpawn-13) or whose wrapper clears
  `GATE_REUSE`: such a runner executes every leg, which is today's behaviour, and nothing here detects
  it.
- The ask DEPL-dSettledRoster-2, that apply runs the target's command twice and the decision was never
  owner-reviewed. This unit keeps both runs and makes them cheaper; the ask stays open.

### Edges

- **consumes-from** external — the target's runner honouring `GATE_REUSE` and printing `GATE reuse <name>` through the `observed_reused` template, which run-gates has shipped since TOOL-aSparedSpawn-13 (`tools/run-gates/kit.toml@609cd40b1:315`).

## 4. Design

### Why the runner's reuse mode answers both halves

The runner writes a cache entry for every leg that executed `ok` on its first attempt, on a tree that
was clean at the start and did not move (`tools/run-gates/run-gates.sh@609cd40b1:5809-5832`). In the
`env` mode, which `GATE_REUSE` selects (`:3604-3627`), it reuses a leg whose key holds such an entry
and prints `GATE reuse <name>` (`:4363`). So:

- BEFORE: a target whose last bar ran on the same clean tree reuses each leg that bar proved green.
  A leg with no entry, a sampled leg and an aged leg execute, as they would in any reusing bar.
- AFTER: the tree is dirty with what apply wrote, so no entry is written, and a leg's key moves
  exactly when the install touched a path under its guard, rewrote its manifest row, or, for an
  unguarded leg, changed anything. Those legs execute. The rest reuse the entry the BEFORE read, or
  an earlier clean bar, wrote.

A key composes its own guard listing and dirt share (`#build_key_text`), so the selection rule is the
runner's, unchanged, and the guard-matching rule is never restated in govkit.

### The comparison

```python
def derive_before_state(state):
    return "green" if state == "reused" else state

# BASELINE
if before_map and not any(derive_before_state(v) in ("green", "red") for v in before_map.values()):
    raise Refusal("DEAD PROBE: ...")          # unchanged text
reds = [n for n, v in before_map.items() if derive_before_state(v) == "red"]
# AFTER: `b = derive_before_state(before_map.get(nm))`, then today's table
```

The cache holds only `ok` entries (`tools/run-gates/run-gates.sh@609cd40b1:3904`), so a reused leg
before is a leg whose same input key was proven green. A reused leg after keeps today's row:
`green` before and `reused` after prints the carried note and is no failure
(`tools/govkit/govkit.py@609cd40b1:8391-8393`). A leg green before and red after is refused as
today, whether it was reused or executed before.

### The receipt

`_rcpt_doc` takes `baseline.legs` and `after` through `derive_before_state`. Under `reuse` a leg reused
and a leg executed green record the same word, so the receipt is the same bytes whichever the sample
drew, and the same bytes a `run` apply writes for the same verdicts.

### The saving

On a target whose last bar ran green on the same clean tree, the BASELINE read executes only the
legs with no entry plus the sampled quarter, and the AFTER read only the legs the install reached
plus the sampled quarter of the rest. The analysis estimated two whole bars falling to 0.1 to 0.3 of
one (K8). On a cold target, a fresh fixture included, the BASELINE read executes every leg as today
and writes the entries the AFTER read then reuses.

### Inventory

- The policy key `install.baseline`, values `reuse` and `run`.
- The function `derive_before_state` in `tools/govkit/govkit.py`, cell `py.function`; lexicon
  `--suggest` OK.
- The argument `reuse` of `read_gate_verdicts`.

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/govkit/selftest.py` · `tools/policy/catalogue.toml` ·
`help/reference/policy.md`

### Alternatives rejected

- Recording the runner's own word, `reused`, in the receipt. The receipt would differ from a `run`
  apply's for identical verdicts, and differ between two applies of one tree by the sample's draw,
  which fails the build brief's acceptance that apply writes identical receipts on the fixtures.
- A new receipt field listing the carried legs. It changes the receipt schema every adopter's govkit
  reads, a shared contract
  (`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`, veto 2), for a
  fact the run record already holds.
- `GATE_BASE=HEAD` for the AFTER read, so legs untouched by the writes skip. A skipped leg after a
  green one is today's "the install broke its guard" refusal (`tools/govkit/govkit.py@609cd40b1:8394-8396`),
  and under that base a skip could no longer tell an untouched leg from a broken guard.
- A govkit-side guard matcher over the written files: a second statement of the runner's rule.

## 5. Production-readiness checklist

- security: no new write path. The reads still execute the target's own command, printed and
  recorded as today; `GATE_REUSE` makes that command trust its own cache in the target's git common
  dir, which only the target's own runs write. The write surface does not widen.
- perf / scale: two whole bars fall to the legs with no reusable entry, the legs the install
  reached, and the sampled quarter (§4).
- error / empty / loading states: an unreadable or foreign `install.baseline` reads as `run`, named
  on one line; a runner that ignores `GATE_REUSE` executes every leg; a cache entry the runner cannot
  read executes its leg (`tools/run-gates/run-gates.sh@609cd40b1:3904`).
- observability: the BASELINE line names the mode (S6); the runner's `GATE reuse` lines are in the
  output apply already parses.
- risks: a leg whose guard is too narrow is reused after an install that reached its real inputs.
  The runner states that limit for its lineage reuse (`tools/run-gates/run-gates.sh@609cd40b1:3945-3949`),
  and it holds for any reuse by key; the sample and the age bound are the runner's standing check,
  and `install.baseline = "run"` is the escape.
- testing: AC1 to AC6 are probes and fixtures of this unit's code; AC7 is the main loop's.
- migration: additive. An unset key reads the default, `reuse`; no receipt field is added.
- user docs: `help/reference/policy.md`'s section for the key (S7).

## 6. Acceptance criteria

- **AC1** — When `govkit apply` runs on a fixture target whose `[gate_runner].command` is a stub
  runner that appends `GATE_REUSE=<value>` to a log and prints one `GATE` line per leg, the log holds
  `GATE_REUSE=1` twice under `install.baseline = "reuse"`, and the apply prints
  `the baseline will RUN, reusing`.
  Red when: either read runs without `GATE_REUSE`.
- **AC2** — When the stub prints `GATE reuse a` and `GATE ok b` before the write and `GATE reuse a`
  and `GATE FAIL  b` after it, `govkit apply` exits non-zero naming
  `leg 'b' was green before this install and is red after`, and names nothing about `a`.
  Red when: the red after is not refused, or the reused leg is.
- **AC3** — When the stub prints `GATE reuse a` before and `GATE FAIL  a` after, the apply refuses
  naming `leg 'a' was green before this install and is red after`; and when it prints only
  `GATE reuse` lines before, the apply raises no `DEAD PROBE`.
  Red when: a reused-before leg is read as no state, or an all-reused baseline is refused as dead.
- **AC4** — When the stub prints `GATE reuse a` before and after, the written
  `.governance/install.json` holds `"a": "green"` in `baseline.legs` and in `after`, and its bytes
  equal those of an apply whose stub printed `GATE ok a` both times.
  Red when: the receipt records `reused`, or the two receipts differ.
- **AC5** — When the fixture target's committed `.governance/policy.toml` sets
  `install.baseline = "run"`, the stub's log holds no `GATE_REUSE` line. When it sets
  `policy-file.on-invalid = "refuse"` and `install.baseline = "maybe"`, so the policy reader refuses,
  the apply prints one line naming `install.baseline`, completes, and the log again holds none.
  Red when: `run` still passes `GATE_REUSE`, or a refused read refuses the apply or turns reuse on.
- **AC6** — When `python tools/playbook/render_playbook.py --reference` runs,
  `grep -c '^## .install.baseline.$' help/reference/policy.md` prints 1, and
  `python tools/policy/policy.py lists --check` exits 0.
  Red when: the key has no section, or it lacks a summary or a usage.
- **AC7** — When the main loop runs `extract-arms.sh` over the `govkit selftest` leg at the build
  base and at this unit's commit, every apply arm whose target declares `kind = "manifest"` keeps its
  verdict, and
  `python tools/govkit/govkit.py check --target C:/projects/incms/main` and `--target
  C:/projects/nicocares/main`, run read-only from gov, read the same before and after.
  Red when: an arm changes verdict, or a check line changes.
  permission: a role pass may not run the deployer's suite (`tools/unattended/gate-guard.js` row
  D4); the main loop observes this at VERIFYING.
  fixture: AC1 to AC5's stub-runner targets are the new arms, built by `build_target` in the
  deployer's suite; no target under `tools/govkit/fixtures/` declares a manifest runner today.

## 7. Gates

`govkit selftest` · `policy fixtures` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix` · `scratch-guard self-test` · `routed-commits selftest`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 · a stub runner that prints `GATE reuse` before and `GATE FAIL` after; the arm reds when `derive_before_state` is bypassed and the red after passes · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. The one minted
  function the lexicon refused, `effective_before`, is `derive_before_state`, checked by `--suggest`,
  everywhere the spec spells it. No criterion had the pass run a suite, a `--selftest`, a gate leg
  or the bar: AC7's suite reading was already the main loop's.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  4 and section 10 the rejected alternative's build-method citation names its tag, and dWitnessedBar's
  changed-line count is marked PINNED. Design, scope and acceptance unchanged.

## 10. Reuse audit

The seam is the runner's own reuse cache and its `env` mode (`tools/run-gates/run-gates.sh`, the
reuse block, TOOL-aSparedSpawn-13), which already answers "is this leg's verdict already held for
these inputs" per leg, and `read_policy_value` in `tools/govkit/govkit.py` for the switch.
`python tools/codebase-map/reuse_lookup.py "read recorded leg verdicts from the reuse cache instead of running the target bar"`
ranked name-token neighbours, `read_policy_value` among them and no cache reader, so govkit reads no
cache file itself and asks the target's runner through the knob it already honours. No existing
policy key covers apply's baseline: the catalogue's six `install.` rows at `59e882afd` are
`install.from`, `install.guards`, `install.deprecation-window`, `install.on-shim-call`,
`install.retired-edits` and `install.steps`, and none is about the baseline. Chain
owners: dSafePassage (Supersession, govkit apply), whose CLOSED specs 5, 10 and 25 to 27 do not touch
`read_gate_verdicts`, and dWitnessedBar (Test), whose branch changes 277 lines [PINNED] of `govkit.py` between
`9e21ac760` and `59e882afd` and no line of the BASELINE or AFTER blocks; its unit 16 names "baseline"
only for the map's own registries. The recall probe surfaced DEPL-dSettledRoster-2, named in §3.

Recall terms used: `python tools/memory-recall/query.py "how does govkit apply compare the target bar before and after the install, and can it reuse cached verdicts" --terms "govkit apply baseline read_gate_verdicts before_map after_map GATE_REUSE reuse cache gate-cache observed_reused input key"`
