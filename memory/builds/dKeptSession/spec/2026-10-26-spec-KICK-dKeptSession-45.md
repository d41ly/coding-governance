# KICK-dKeptSession-45 — the window scan's default root resolved by `resolve_projects_root`, never a literal profile path

**Status:** DEFERRED · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 14 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-45-deviation-451.md](../build/2026-10-26-build-KICK-dKeptSession-45-deviation-451.md) | deviation | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 28 at HIGH**, report item **H1**. Id 38 shares the item and is promoted as
`KICK-dKeptSession-46`; id 18 is the same defect at MEDIUM, item M12, batched into
`KICK-dKeptSession-56`, whose item observes this unit's fix.

`KICK-dKeptSession-30` S1 defaults the window scan's `root` to the literal `~/.claude/projects`.
`tools/runlog/extract.py:185` already resolves that root as `resolve_projects_root`, which honours an
override and then `$CLAUDE_CONFIG_DIR/projects` before the profile's `.claude/projects`, and every
`runlog.py` verb routes through it (`tools/runlog/runlog.py:246`, `:300`, `:324`, `:360`). On a node
with `CLAUDE_CONFIG_DIR` set the literal scans an empty tree, finds no observation and reads the
200000 rung, which is the defect unit 30 exists to repair. This unit makes the scan's default root
that resolver's answer. It repairs `KICK-dKeptSession-30` and builds one step after it (order 14).

## 2. Scope (IN)

- **S1** — id 28. The default. `derive_context_window(model, root=None)` resolves a `None` root as
  `resolve_projects_root()` (`tools/runlog/extract.py:185`), called with no argument so it reads the
  process environment exactly as the `runlog.py` verbs do. No other spelling of the projects root is
  written in the window code. Observed by AC1 and AC2.
- **S2** — id 28. No root resolves. Where `resolve_projects_root()` raises its `ValueError` (both
  `CLAUDE_CONFIG_DIR` and the profile's home unset), the window reads the bottom rung with source
  `no root: <the error's text>`, the same direction as unit 30 S1's `no observation`. Observed by AC3.
- **S3** — id 28. The sibling text superseded by name. `KICK-dKeptSession-30` S1's "`root` defaults
  to the harness's projects root, `~/.claude/projects`" and S2's "the default root" read as S1 here,
  and unit 30's §10 gains `resolve_projects_root` as a reused seam. Each is answered in unit 30's
  acceptance ledger. Observed by AC2.

## 3. Non-goals (OUT)

- Which root the fill's callers pass: id 38, `KICK-dKeptSession-46`.
- The observation itself, its compactions and its rungs: `KICK-dKeptSession-30`,
  `KICK-dKeptSession-47` and `KICK-dKeptSession-48`.
- The report's left-shift checklist entry, that a spec naming a filesystem root cites the module's
  resolver. No clause of this build names that checklist; AC2 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-30` — `derive_context_window` and its `root` argument, whose default this unit resolves through `resolve_projects_root` (id 28)
- **hands-off** `KICK-dKeptSession-56` — `derive_context_window`'s resolved default root, which the batch's item for id 18, the same defect at MEDIUM, observes
- **hands-off** `KICK-dKeptSession-62` — AC1, AC2 and §4's evidence, which the batch's S27 to S30 restate (ids 38, 8, 16, 39)

## 4. Design

### Evidence

- `resolve_projects_root(env=None, platform=None, override=None)` returns `override`, else
  `$CLAUDE_CONFIG_DIR/projects`, else `<home>/.claude/projects`, and raises `ValueError` naming
  `--transcripts` when no root resolves (`tools/runlog/extract.py:185-198`, read at base).
- The runlog selftest aims `CLAUDE_CONFIG_DIR` at a decoy among its `DECOY_VARS`
  (`tools/runlog/selftest.py:348-349`), so a literal profile path is the one root the suite's
  isolation cannot reach.

### The read

```
CLAUDE_CONFIG_DIR=<cfg>   derive_context_window("m")  -> scans <cfg>/projects
unset, HOME=<h>           derive_context_window("m")  -> scans <h>/.claude/projects
neither                   derive_context_window("m")  -> (200000, "no root: runlog: no transcripts root resolves ...")
```

### Inventory

No identifier is minted.

### Migration

None: no stored state holds a window.

### Files touched (estimate)

- `tools/runlog/extract.py`: S1 and S2 in `derive_context_window`
- `tools/runlog/selftest.py`: the `CLAUDE_CONFIG_DIR` case

### Alternatives rejected

- **Keeping the literal and documenting `CLAUDE_CONFIG_DIR` as unsupported.** It is a second answer
  to "where are the transcripts" beside the resolver every verb already uses.
- **Raising when no root resolves.** A fill read at a boundary hook would then fail the hook for a
  node with no profile; the bottom rung errs towards going fresh, the cheaper error.

## 5. Production-readiness checklist

- security — the resolver reads two environment variables and writes nothing.
- perf / scale — one resolver call per derivation, no file read.
- error / empty / loading states — S2's `no root:` source, never a raise.
- observability — `runlog.py context` already prints the window's source on stderr (unit 30 S2).
- risks — none new: the resolver is the one every verb already trusts.
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — none: `help/orientation-card.md`'s window paragraph (unit 30 S5) names no root.

## 6. Acceptance criteria

The fixture is unit 30's `context-window-sibling` scenario written under a scratch config directory
`<cfg>/projects/<project>/` beneath `%TEMP%`.

- **AC1** — When a probe runs `python -c "import extract; print(extract.derive_context_window('fixture-model'))"`
  in the runlog kit with `CLAUDE_CONFIG_DIR=<cfg>` and `HOME` aimed at an empty directory, it
  prints `(1000000, 'observed 900000 on fixture-model')`.
  Red when: a copy defaulting to the profile's `.claude/projects` prints `(200000, 'no observation')`.
- **AC2** — When `grep -n "resolve_projects_root()" extract.py` runs in the runlog kit, it prints the
  line inside `derive_context_window`, and `grep -c '".claude"' extract.py` prints the count it
  printed at base.
  Red when: the window code spells the profile path a second time.
- **AC3** — When the AC1 probe runs with `CLAUDE_CONFIG_DIR`, `HOME` and `USERPROFILE` all removed
  from its environment, it prints `(200000, 'no root: ...')` and exits 0.
  Red when: the derivation raises, so a fill read with no profile fails its caller.

## 7. Gates

`runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runlog/selftest.py · covers AC1 AC3 · the scenario under a scratch `CLAUDE_CONFIG_DIR`, and every root variable removed, staged red by a copy of `extract.py` whose default root is the literal profile path · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H1 (id 28).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared

## 10. Reuse audit

The seam reused is `resolve_projects_root` (`tools/runlog/extract.py:185`), the resolver every
`runlog.py` verb calls; this unit adds no resolver and no path literal. `python
tools/codebase-map/reuse_lookup.py "resolve the transcripts projects root honouring
CLAUDE_CONFIG_DIR"` ranked `resolve` (`tools/memory-recall/recall_conf.py`), `repo_root` and
`resolve_kit_dir` by name stem; none resolves a transcripts root, and the map's symbol tier did not
surface `resolve_projects_root`, which the source read above found, so the probe and the source
disagree and the source is the seam.

Recall terms used: `python tools/memory-recall/query.py "where does the runlog kit find the
harness transcripts root" --terms "resolve_projects_root CLAUDE_CONFIG_DIR projects root transcripts
override decoy build_arm_env window scan"`
