# TOOL-dQuietDisk-11 — govkit's scratch targets come from the template cache, so `selftest.py` builds each distinct target once

**Status:** SPECCED · rev-2 · 2026-11-22 · node d · Tier-2 · base 609cd40b · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/govkit/selftest.py` calls `build_target` 97 times at `609cd40b1`, and each call spends 8 git
processes on a repository 66 of those calls already built once with the same content. This unit
points `build_target` and `build_scratch_gov` at TOOL-dQuietDisk-7's python face, so each distinct
target is built once per runner invocation and copied per call, with every arm's verdict unchanged.

## 2. Scope (IN)

- **S1** — `build_target(tmp, deploy, name, files)` in `tools/govkit/fixture_target.py` asks unit
  7's python face for the template its arguments describe, then copies that template to
  `tmp / name` with `shutil.copytree(..., symlinks=True)` and returns the copy. The template's
  builder is today's body (`tools/govkit/fixture_target.py#build_target`), run once per key.
  Observed by AC1 and AC2.
- **S2** — `build_scratch_gov(g)` does the same with today's six-step body
  (`tools/govkit/fixture_target.py#build_scratch_gov`) as its builder, one template for every call.
  Observed by AC1 and AC2.
- **S3** — The key is unit 7's key over the builder's own code, the blob of
  `tools/govkit/fixture_target.py`, plus a digest of the arguments that shape the content: `deploy`
  and `files` for a target, nothing for a scratch gov. `name` and `tmp` pick only the destination and
  are not in the key. The kit tree is not in the key: neither builder reads it. Observed by AC3.
- **S4** — Every caller of the two factories takes the change with no edit of its own: the arms of
  `tools/govkit/selftest.py`, `tools/govkit/docs_leg.py`, `tools/govkit/upgrade_walk.py`,
  `tools/govkit/upgrade_steps.py` and `tools/govkit/fixtures/retired_edits.py` and
  `fixtures/stale_edges.py`. Observed by AC2 and AC5.
- **S5** — Under unit 7's switch at its other value, today's behaviour, each call runs the builder
  into its own destination as today. That branch is the factory's. Observed by AC2.
- **S6** — `check_inherited_config`, the module's `--selftest`, still holds every observation: a
  planted global signing program, global `core.hooksPath` and `init.templateDir` reach no target,
  because the template is built under the same pinned config and the copy carries it. Observed by AC4.
- **S7** — The saving is counted, and every arm of `selftest.py` keeps its verdict. Observed by AC5.

## 3. Non-goals (OUT)

- The 60 inline `"init"` sites of `selftest.py` at `609cd40b1`, spread over about forty local helpers
  that each build a distinct base (`build_rename_target`, `hook_target`, `runner_target` and the
  rest). A template used once costs what the inline build costs.
- The clone of gov at `tools/govkit/selftest.py@609cd40b1:5867` and the upgrade walk's gov clone:
  TOOL-dQuietDisk-8, the shared snapshot.
- `rmtree(ignore_errors=True)` and `TemporaryDirectory(ignore_cleanup_errors=True)` in these files:
  TOOL-dQuietDisk-9.
- `tools/run-gates/adopt-run-gates.test.sh`'s own bash `build_target`, a different function.
- The factory, its store, its switch and its concurrency: TOOL-dQuietDisk-7.

### Edges

- **consumes-from** `TOOL-dQuietDisk-7` — the python face that builds a template once per runner invocation under the runner's owned root and returns its path, with a key composition admitting a caller's code blob and argument digest, and its switch. Without it there is nothing to copy from.
- **hands-off** `TOOL-dQuietDisk-19` — the `selftest.py` shard's before and after readings.

## 4. Design

### The two factories after the change

```python
def build_scratch_gov(g):
    tpl = CACHE.resolve_template(BUILDER_BLOB, (), _init_scratch_gov)   # unit 7's python face
    shutil.copytree(tpl, g, symlinks=True)
    return g

def build_target(tmp, deploy, name="target", files=None):
    tpl = CACHE.resolve_template(BUILDER_BLOB, (deploy, sorted_digest(files)),
                                 lambda d: _build_target_into(d, deploy, files))
    t = tmp / name
    shutil.copytree(tpl, t, symlinks=True)
    return t
```

`CACHE` is a `TemplateCache`, and `resolve_template(builder_id, inputs, build)` is its method as
TOOL-dQuietDisk-7 rev-2 spells it; the copy is `shutil.copytree`, as S1 states, so this unit mints
no function of its own. `_init_scratch_gov` and `_build_target_into` are today's two bodies,
moved and not edited.

### Why a copy and not a clone

A copy of a template spends 0 git processes. A `git clone --shared` spends 1, and its config holds
none of the template's pins, since a clone writes a fresh `.git/config`. Restoring them takes five
`-c` arguments, and the clone adds an `origin` remote that `build_target` never made and the
dirty-tree and upstream readers of `govkit.py` can see. A worktree detaches `HEAD`. The measurement
in TOOL-dQuietDisk-10 §4 gives the entry counts: a copy and a shared clone make about the same number.

### What the copy changes, and why no arm reads it

Every copy of one template holds the same commit, so two targets built from one key share a `base`
sha where today two builds in different seconds do not. No arm can rely on the difference today:
two builds in the same second already share a sha. AC5's full run is the observation.

### The saving, derived from the code at `609cd40b1`

An AST walk of `selftest.py` finds 97 `build_target` calls over 31 distinct `(deploy, files)`
argument expressions, so 66 calls repeat a key. Three of those name the loop variable `deploy`,
whose values may differ, so at least 63 repeat a built key. Each repeat spends 0 git processes where
today's spends 8: at least 504 fewer per full run, and more for calls inside loops. Temp entries
per call stay about equal, since the copy writes what the build wrote. The figure is DERIVED from
the static walk; unit 19 measures one shard.

### Order

This unit writes no line of `tools/govkit/selftest.py`, but its AC5 observes that file, and
TOOL-dQuietDisk-18 writes arms into it, so the two are not disjoint (BUILD-METHOD M6, clause 2). The spec brief says to order this
unit after unit 18 when both touch the file, so this unit takes order 4. TOOL-dQuietDisk-19, also at
order 4, measures a `selftest.py` shard, so it reads this unit's output and must sit after it.

### Files touched (estimate)

`tools/govkit/fixture_target.py`

### Alternatives rejected

- Re-pointing each `selftest.py` call site at the face instead of the two factories: 97 edits where
  two serve, and the five other callers would keep paying.
- A `git clone --shared` per call: rejected above.

## 5. Production-readiness checklist

- security: N/A — no new write path; the copy lands only at the destination the caller names, as today.
- perf / scale: at least 504 fewer git processes per full `selftest.py` run (§4).
- error / empty / loading states: a failed template build raises `OSError` naming the argv, as
  `run_git` does today (`tools/govkit/fixture_target.py#run_git`); a failed copy raises `OSError`
  naming the destination.
- observability: none added.
- risks: a template built while a commit moves the tree
  (`memory/gotchas/suite-invalidated-by-a-commit-under-it.md`). The builders read no tracked file, so
  a commit under the run cannot change what a template holds.
- testing: AC1 to AC4 are probes; the module's `--selftest` and AC5's suite run are the main loop's.
- migration: N/A — templates live for one runner invocation.
- user docs: N/A — test fixtures; no `help/` page describes them.

## 6. Acceptance criteria

- **AC1** — When a probe imports `tools/govkit/fixture_target.py` and calls `build_target(tmp,
  DEPLOY, "a")` then `build_target(tmp, DEPLOY, "b")` under `GIT_TRACE2_EVENT=<dir>`, the second
  call adds 0 trace files. `build_scratch_gov` called twice adds 0 on the second call.
  Red when: a repeated key spawns git.
- **AC2** — When the probe builds the same target under unit 7's switch at each of its two values,
  `git ls-files -s`, `git for-each-ref`, `git config --local --list`, `git status --porcelain` and
  `git show -s --format=%T%x09%s HEAD` read byte-identical across the two, for `deploy` `None`, a
  `deploy` text, and a `files` map holding bytes and text.
  Red when: a copied target differs from a built one in any of the five reads.
- **AC3** — When the probe calls `build_target` with the same `deploy` and a different `files`
  map, and then with a different `name` only, the first builds a new template and the second
  reuses the old one.
  Red when: `files` is missing from the key, or `name` is in it.
- **AC4** — When the probe points `GIT_CONFIG_GLOBAL` at a planted config that signs with a failing
  program, sets `core.hooksPath` to a canary hook and names an `init.templateDir` holding a canary
  hook, and then calls `build_target` twice with a `TemplateCache`, both copied targets hold `base`,
  carry no canary path and no copied hook. When the main loop runs the module's own `--selftest` at
  the close, `check_inherited_config` prints `fixture-target: PASS` and exits 0.
  Red when: a planted global config reaches a copied target.
  permission: a role agent runs no `--selftest` (scratch-guard row G3), so the module's own run is
  owed to the main loop; the pass makes the planted-config probe.
- **AC5** — When the main loop runs `extract-arms.sh` over the `govkit selftest` leg at the build
  base and at this unit's commit, each in a scratch `git clone --shared` with `GIT_TRACE2_EVENT`,
  `TEMP`, `TMP` and `TMPDIR` pointed at scratch dirs, both inventories hold the same check labels
  with the same verdicts, the git process count falls by at least 504, and residual temp entries are
  0 both times.
  Red when: a check changes verdict, the count does not fall by the bound, or an entry remains.
  permission: a role pass may not run the deployer's suite (`tools/unattended/gate-guard.js` row D4);
  the main loop observes this at VERIFYING.
  cost: two full runs of the deployer's suite.
  figure: 504 is DERIVED from §4's static walk at `609cd40b1`.

## 7. Gates

`govkit selftest` · `policy fixtures` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/govkit/fixture_target.py · covers AC2 AC4 · its `--selftest` builds one target under each switch value and compares the five reads; a copy that skips `.git/config` reds it · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Ordered 4, not the roster's 3: TOOL-dQuietDisk-18 writes
  `tools/govkit/selftest.py`, which this unit's AC5 reads, and the spec brief orders this unit after
  18 when both touch the file. TOOL-dQuietDisk-19 at order 4 reads this unit's output.
- rev-2 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. Section 4's sketch
  spells unit 7's python face as TOOL-dQuietDisk-7 rev-2 renames it, `resolve_template`, and the copy
  as `shutil.copytree`, in place of the placeholders `template_path` and `copy_template`, which the
  lexicon would refuse. AC4 had the pass run the module's `--selftest`; it now has the pass run a
  planted-config probe, the module's own run is owed to the main loop, and the `New arm:` line
  covers AC4.

## 10. Reuse audit

The seam is `tools/govkit/fixture_target.py#build_target` and `#build_scratch_gov`, the one factory
per kind every govkit fixture already calls (TOOL-dSafePassage-5 S12), extended onto
TOOL-dQuietDisk-7's python face rather than beside it.
`python tools/codebase-map/reuse_lookup.py "build a scratch fixture repository once and clone it per test case"`
ranked `build_target` and `build_scratch_gov` in `tools/govkit/fixture_target.py` as seams, beside
`build_fixture` in `tools/lib/lib-selftest.sh`, which unit 7 generalises. Chain owner: dWitnessedBar
(Test); the deployer is dSafePassage's area. Its CLOSED unit 5 made `fixture_target.py` the one
factory per kind (S12), and this unit keeps that contract: each call still returns a repository
holding the same files, refs and config at the destination it names. dWitnessedBar's
branch changes 512 lines of `selftest.py` and none of `fixture_target.py` between `9e21ac760` and
`609cd40b1`, so this unit builds on its tip.

Recall terms used: `python tools/memory-recall/query.py "how does govkit selftest build its scratch target repositories" --terms "build_target build_scratch_gov fixture_target scratch target template copy clone selftest govkit run_git"`
