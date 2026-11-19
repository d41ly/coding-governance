# TOOL-dLandedOwners-6 — the two legs the close's bar read red: the policy-fixtures guard covers its import closure, and the unscanned-readers row stops reading as a spec citation

**Status:** INPROGRESS · rev-1 · 2026-11-19 · node d · Tier-2 · base fcbd7efe · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-prompt-TOOL-dLandedOwners-6-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-6-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-6-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-6-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dLandedOwners-6-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-6-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The merge bar at this build's tip read two legs red, and this build's own units caused both. The
`policy fixtures` guard gains the one module its import closure now reaches and the guard does not
name. Drift signal 2's evidence stops reading the authored list of unscanned readers, whose row
spells a non-terminal spec's id inside a file path and claims no work shipped.

## 2. Scope (IN)

- **S1** — In `tools/gate-legs.json`, the `guard` list of the `policy fixtures` row gains the entry
  `"{prefix}/memory-tree/commit_trailers.py"`, on the line after
  `"{prefix}/memory-tree/routed_commits.py"`, the module that imports it. No other row and no other
  entry changes. Observed by AC1 and AC2.
- **S2** — `tools/drift-audit/drift_signals.py#EVIDENCE_GLOBS` gains the entry
  `":(exclude)*/unscanned-readers.txt"` as its last element, after the size-registry exclusion, with
  the comment of §4 "The evidence exclusion" above it. No other list and no baseline changes.
  Observed by AC3 and AC4.
- **S3** — `memory/guides/SESSION-KICKOFF.md` re-stamps its `last-audit` line, because S1 edits a
  path its `watch:` line names. Observed by AC5.

## 3. Non-goals (OUT)

- Any change to the mechanisms of units 1 to 4. Unit 1's import of `gen_build_index` in
  `tools/policy/check_policy.py#load_run_readers` stays, and so do unit 3's list grammar and its row.
  Both specs are CLOSED and frozen.
- Any edit to a dClosedLoop record or instrument, the deviations instrument's file name included.
- Any other drift signal, pin or baseline. `BASELINES` keeps its one signal-2 id, and gains none.
- Any other leg's `guard`, and any edit to `tools/run-gates/py_reads.py` or to the drift-audit engine
  `tools/drift-audit/drift_report.py`.
- The owner's flagged bar.
- Closing `PLAY-dClosedLoop-1`, which belongs to its own build.

### Edges

none

## 4. Design

### What the tree holds today

- `tools/policy/check_policy.py#load_run_readers` imports `backlog`, `gen_build_index` and
  `row_grammar` from the memory-tree kit, the import unit 1 added.
- `tools/memory-tree/gen_build_index.py#cmd_selftest` imports `routed_commits` inside the function
  body (`tools/memory-tree/gen_build_index.py@a1bfa9b944d24be88fb3037c302a1bfccf6c2e18:7302`).
- `routed_commits` imports `derive_attribution` and `read_commits` from `commit_trailers` at module
  level (`tools/memory-tree/routed_commits.py@d48d1dc8d6f5b7f975592b865a1365cdae2a2a21:106`).
- `tools/run-gates/py_reads.py#derive_closure` walks every import a file holds, a function-local one
  included, and skips only the `dynamic` rows of the import walk. `tools/run-gates/py_reads.py#derive_guard_gaps`
  reds each walked module that no guard entry covers exactly or as a directory ending `/`.
- The `policy fixtures` guard already names `gen_build_index.py`, `routed_commits.py` and the other
  memory-tree modules of the closure, but not `commit_trailers.py`
  (`tools/gate-legs.json@d2f27f18b4ef782989a7ec592a48553e691499cd:2741`).
- On 2026-11-19 at `fcbd7efe`, `py_reads.py --guards "policy fixtures"` printed the closure and one
  red, `py-reads: RED guard · policy fixtures · tools/memory-tree/commit_trailers.py is imported and outside its guard`,
  and exited 1.
- `tools/drift-audit/drift_report.py#signal_spec_status` greps each non-terminal spec's own id,
  whole-word and fixed-string, over the evidence globs, with the project layer excluded. A `-` is no
  word character, so the id inside a file name matches.
- `tools/policy/unscanned-readers.txt` holds one row. Its path field is
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py`
  (`tools/policy/unscanned-readers.txt@6a7b6f580b01f94be85aded90e8828148089fbf0:6`).
- `PLAY-dClosedLoop-1`'s spec reads INPROGRESS
  (`memory/builds/dClosedLoop/spec/2026-10-20-spec-PLAY-dClosedLoop-1.md@87ff111e7025a322024044c5c9bc32c1c76fa611:3`).
- On 2026-11-19 at `fcbd7efe`, `drift_report.py --offenders` printed one line and exited 1. The line
  was signal `non_terminal_specs_cited_by_product_source`, id `PLAY-dClosedLoop-1`, cited in
  `tools/policy/unscanned-readers.txt` alone.
- `tools/drift-audit/drift_report.py#build_baseline_findings` reds any id the working `BASELINES` set
  gains against the base, so listing the id is refused by the engine.
- `EVIDENCE_GLOBS` already excludes the size registries with their reason beside the line: a row keyed
  by a file path names a spec's path without claiming any of its work shipped
  (`tools/drift-audit/drift_signals.py#EVIDENCE_GLOBS`).
- `tools/drift-audit/drift_signals.py` is project-owned and never installed
  (`tools/drift-audit/kit.toml@dd963339f023b13f23ff1a52befc0eb22aeaa2fa:44`), and
  `tools/policy/unscanned-readers.txt` is withheld from installs by the policy kit's `project-owned`
  rule (`tools/policy/kit.toml@da41b1f18986442d5465db015b7c9f40d5a467b2:35`). Both are gov's alone.

### The guard line

S1 adds the module by its exact path, as the class record
`memory/gotchas/held-suite-guard-misses-a-sibling-kit.md` orders. Its fix names the module a suite
imports and what that module imports, and prefers exact files to the sibling's directory, which would
tip a shared guard past the spec-token checker's breadth floor.

The entry names a tracked file, so `tools/policy/check_policy.py#check_guard_lines` reads it live.
On 2026-11-19 at `fcbd7efe`, no OPEN, SPECCED, INPROGRESS or BLOCKED spec named
`tools/memory-tree/commit_trailers.py`, by `git grep` over every spec. So the spec-token guards join
owes `policy fixtures` to no live spec it did not owe before.

### The evidence exclusion

The entry and the comment above it, verbatim:

```
    # THE UNSCANNED-READERS LIST, for the size registries' reason. Policy reader coverage keys each
    # row by the tracked FILE PATH where a key's value is consumed, and a record's file name carries
    # its unit id, so a row names that id without claiming any of its work shipped.
    ":(exclude)*/unscanned-readers.txt",
```

The comment spells no unit id. The pathspec carries no kit path, as the size-registry line carries
none, so it holds at whatever tool root the kits are checked out under. The leading `*/` is needed,
because a pathspec without it names a file at the repository root and matches nothing.

The report-only sibling signal `open_asks_cited_by_product_source` reads the same globs. The list
spells no ask id, so its value does not move.

### Decision by M3

Both choices are derived, not open: in each, only one option survives the build method's vetoes.

| Red | Option | Outcome |
|---|---|---|
| guard | the guard gains `commit_trailers.py` | survives: one entry, no new surface, the class record's fix |
| guard | the closure loses it: `check_policy` stops importing `gen_build_index` | vetoed by veto 1, a §3 non-goal, unit 1's mechanism |
| guard | the closure loses it: `gen_build_index` imports `routed_commits` through `importlib` | refused: it hides the edge in a `dynamic` row the walk does not read, and edits another kit |
| guard | the guard names `{prefix}/memory-tree/` | refused: the class record prefers exact files, and the directory already counts as broad |
| citation | `EVIDENCE_GLOBS` excludes the list | survives: one entry with its reason, the size registries' precedent |
| citation | `BASELINES` gains `PLAY-dClosedLoop-1` | refused by `build_baseline_findings`, and the brief forbids it |
| citation | the row names a directory, or another spelling of the path | vetoed by veto 1: unit 3's row grammar reads a tracked file exactly |
| citation | the instrument is renamed | vetoed by veto 1, a §3 non-goal: a dClosedLoop record |
| citation | `PLAY-dClosedLoop-1` is closed | outside this build: its own build's work |

The guard route reds no other spec's join, as §4 "The guard line" measures. That is what made the
guard route fail for `PLAY-dOrderedCharter-82`, whose wider guard tripped other builds' live specs.

### What it does not check

- S1 is held by the `python reads (a name never bound, an import outside its guard)` leg only while
  the closure reaches `commit_trailers.py`. If the import goes, the entry is surplus and nothing reds
  it.
- S2 is held only while `PLAY-dClosedLoop-1` is non-terminal and the row stands. After either goes,
  dropping the exclusion reds nothing. No selftest arm reads the shipped line, and this unit adds
  none: the live tree is today's failing case.
- The exclusion drops every citation the list might carry, a real one included. A row's reason that
  named a shipped unit would not be read as evidence either.
- Another product file that names a record's path still cites that record's id:
  `.claude/settings.json@0428723eeeee94543d96dcfda3661a29193007a7:98` and
  `tools/loop/loop.toml@f1e32350ceaec51508f3854e2ff31420fb8907e8:1159` each name a dTrackedAtlas
  build record. Neither reds today, and this unit leaves them.

### Rollout

The builder sets this spec to INPROGRESS before the first write. One build commit carries S1 to S3,
since S1 and the stamp of S3 must land in one commit, and its message carries the kickoff manifest's
`manifest-audit:` delta line. The commit hooks re-render the build's README and `memory/LIVE.md`.

### Files touched (estimate)

`tools/gate-legs.json`
`tools/drift-audit/drift_signals.py`
`memory/guides/SESSION-KICKOFF.md`
`memory/builds/dLandedOwners/build/2026-11-19-build-TOOL-dLandedOwners-6-ledger.md`
`memory/builds/dLandedOwners/README.md`
`memory/LIVE.md`

The last two are re-rendered by the commit hooks, as at unit 3's build commit `b8297f701`.

### Alternatives rejected

The rows of §4 "Decision by M3" that do not survive, each with its reason there.

## 5. Production-readiness checklist

- security — N/A — two declaration lines and a stamp. Nothing is executed or written by them.
- perf / scale — An edit to `commit_trailers.py` alone now selects the `policy fixtures` leg, which a
  scoped bar skipped before. That is the guard's purpose. The evidence set shrinks by one file.
- error / empty / loading states — The evidence set stays non-empty, so signal 2 stays live, as AC3
  observes.
- observability — Both legs print their verdicts unchanged; the exclusion's reason sits beside it.
- risks — An exclusion hides a citation; §4 "What it does not check" names what that costs.
- testing — AC1 to AC5, each a direct probe. No suite arm is added or moved.
- migration — N/A — no data or format changes.
- user docs — N/A — gov's own leg manifest and its own project-owned drift declarations, neither
  installed nor described under `help/`.

## 6. Acceptance criteria

Commands run from the worktree root after `. tools/lib/resolve-python.sh && PY=$(resolve_python)`.

- **AC1** — When `"$PY" -B tools/run-gates/py_reads.py --guards "policy fixtures"` runs, it prints
  `py-reads: closure · policy fixtures · tools/memory-tree/commit_trailers.py`, prints no line holding
  `RED guard`, and exits 0.
  Red when: S1's entry is absent, as at `fcbd7efe`, where it printed
  `py-reads: RED guard · policy fixtures · tools/memory-tree/commit_trailers.py is imported and outside its guard`
  and exited 1.
- **AC2** — When `printf '%s\n' tools/memory-tree/commit_trailers.py | "$PY" -B tools/check-spec-tokens.py --legs-for - | grep -c "policy fixtures <- tools/memory-tree/commit_trailers.py \[selftests"`
  runs, it prints `1`.
  Red when: S1's entry is absent or misspelled, where it prints `0`, as at `fcbd7efe`.
- **AC3** — When `"$PY" -B -c "import subprocess, sys; sys.path.insert(0, 'tools/drift-audit'); import drift_signals as d; g = [*d.EVIDENCE_GLOBS, ':(exclude)tools/drift-audit/drift_signals.py']; run = lambda *a: subprocess.run(['git', *a], capture_output=True, text=True).stdout; print(len(run('ls-files', '--', *g).split()), run('grep', '-l', '-w', '-F', 'PLAY-dClosedLoop-1', '--', *g).strip() or 'none')"`
  runs, it prints `444 none`: signal 2's own read, the project layer excluded as the engine excludes
  it, finds no citation of the id, over an evidence set still non-empty.
  Red when: S2's entry is absent, or spelled without its leading `*/`, where it prints
  `445 tools/policy/unscanned-readers.txt`, as at `fcbd7efe`.
  figure: 445 is PINNED, measured on 2026-11-19 at `fcbd7efe`; 444 is that less the one excluded file.
- **AC4** — When `"$PY" -B tools/drift-audit/drift_report.py --offenders` runs, it prints nothing
  and exits 0. Its exit is `--check`'s (`tools/drift-audit/drift_report.py@57d928be183ad47bb291a7c374cd59130699ce9e:4403`), so the
  `drift-audit records` leg reads green on the same tree.
  Red when: S2's entry is absent, where it prints the one line naming
  `non_terminal_specs_cited_by_product_source` and `PLAY-dClosedLoop-1` and exits 1, as at `fcbd7efe`.
  cost: the whole report runs, minutes rather than seconds.
  figure: the one line is PINNED, the only offender on 2026-11-19 at `fcbd7efe`.
- **AC5** — When `git diff fcbd7efe -- memory/guides/SESSION-KICKOFF.md | grep -c "^+last-audit: "`
  runs, it prints `1`.
  Red when: `tools/gate-legs.json` changes and the stamp does not move, where it prints `0`, and
  `skills/session-kickoff/manifest-check.sh` refuses the commit that stages a watched path without
  moving the stamp, as `memory/TEMPLATE-SPEC.md` states under "A watched path brings its manifest".

## 7. Gates

The close runs the merge bar once. The first two legs are the reds this unit clears; both are
unguarded and run on every bar. The next five are the guarded legs the guards join owes the edited
manifest and the drift declarations, `run-gates canary` among them because its guard names
`tools/gate-legs.json` beside the broad `tools/`. `kickoff-manifest ratchet` grades S3's stamp. The recall
legs guard the build's records; the last three grade this spec. The broad legs under `tools/` are
excluded by the checker's floor, as its run prints.

`python reads (a name never bound, an import outside its guard)` · `drift-audit records` · `policy fixtures` · `run-gates gov canary` · `run-gates canary` · `measure-legs selftest` · `drift-audit selftest` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft, from the spec brief
  `memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-6-spec-brief.md`,
  grounded at `fcbd7efe2`.

## 10. Reuse audit

The seams extended: the `policy fixtures` guard of `tools/gate-legs.json`, the list
`TOOL-aClearedLedger-7` extended by fourteen entries in the same shape (PINNED, its commit
`7d58d947e`); and `tools/drift-audit/drift_signals.py#EVIDENCE_GLOBS`, whose size-registry exclusion
is the precedent S2 copies.
`python tools/codebase-map/reuse_lookup.py "exclude an authored path-keyed registry from the evidence a non-terminal spec shipped"`
and `python tools/codebase-map/reuse_lookup.py "a leg guard list covers every module its suite imports"`
ranked name-stem helpers only, among them `tools/memory-tree/import_walk.py#scan_imports`, the walk
`py_reads.py` already uses. Neither names a seam that widens a guard or narrows an evidence set.
The recall probe returned `TOOL-dGroundRules-69`, the same class: a manifest line spelling
`PLAY-dClosedLoop-1` became that spec's first product citation. Its §4 rejected narrowing the evidence
globs, because `tools/gate-legs.json` carries real citations; the list S2 excludes carries none. It
returned the class record `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`, whose fix S1
follows, and `PLAY-dOrderedCharter-82`, read in §4 "Decision by M3".

Recall terms used: `python tools/memory-recall/query.py "how is a red guard leg fixed when a suite's import closure reaches a module its guard does not name, and how is a non-terminal spec citation removed from drift signal 2 evidence" --terms "guard closure py_reads import gate-legs policy fixtures EVIDENCE_GLOBS exclusion drift signal citation registry"`
