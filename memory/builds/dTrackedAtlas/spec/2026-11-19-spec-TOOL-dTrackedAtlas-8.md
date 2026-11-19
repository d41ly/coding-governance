# TOOL-dTrackedAtlas-8 — the fork scan passes no tree-derived text through shell source

**Status:** CLOSED · rev-1 · 2026-11-19 · node d · Tier-1 · base 9e21ac76 · streams tooling · records-only · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-8-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-8-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dTrackedAtlas-8-red-fix-8.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-8-red-fix-8.md) | red-fix | — |
| [2026-11-19-build-TOOL-dTrackedAtlas-8-red-fix-9.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-8-red-fix-9.md) | red-fix | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-8-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-8-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.md) | research | TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 |
| [2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 |

<!-- /gen:spec-records -->

## 1. Goal

The build-state derivation's fork scan stops putting spec file names, the fork cutoff and its own
temp path into bash source as raw text, and the derivation refuses an off-pattern spec file name
where it lists the specs. A commit at the ref read can then no longer choose shell code that runs
as the operator, and a temp path holding `'` no longer breaks the run. This closes H1 of the closing
review `2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1`.

## 2. Scope (IN)

- **S1** — `scan_forks` quotes every value it writes into shell text with `shlex.quote`: each
  blob's target path and the cutoff on each `plan_state` line of `grade.sh`, and the path of
  `grade.sh` in the `.` line handed to `tools/loop/breakpoints.py#run_sourced`. Observed by AC1 and
  AC2.
- **S2** — `derive` refuses, with `StateError`, any spec path of a chain build whose basename does
  not match `^[A-Za-z0-9._-]+\.md$`, at the listing that selects the build's specs and before any blob
  is read. The CLI then exits 2 with one `build-state: refused spec file name <path> at <commit12>`
  line on stderr. Observed by AC3 and AC4.
- **S3** — The module docstring names the refusal among the exit-2 causes and adds to WHAT IT DOES
  NOT CHECK the spec names git's listing quotes, which never reach the spec set. Observed by AC5.

## 3. Non-goals (OUT)

- The landed predicate and its default-branch ref: `TOOL-dTrackedAtlas-9` owns H2.
- The page's digest and `--check --page`: `TOOL-dTrackedAtlas-10` owns H3.
- The generator's option reader, the pane observations and ledger 1's stale line:
  `TOOL-dTrackedAtlas-11` owns M1, L1 and L2.
- Any edit under `tools/`, including a positional-argument channel in `run_sourced`. The build
  rules forbid it.
- Reading the listing with `git ls-tree -z`. The names git quotes are left out of the spec set
  today. Admitting them would widen the population the refusal guards, and no chain build holds one.
- A shape check on `FORK_ITEM_CUTOFF`: quoting makes any value inert, and the conf's own gate grades
  its shape.
- A gotcha file or a suite arm for the review's class `tree-text-interpolated-into-shell-source`.
  This repository's `review.left-shift` is `second-occurrence`, and this is the class's first, so
  the regression arm is this unit's acceptance, observed red then green.
- Editing units 1 to 3's specs, which are CLOSED and frozen.

### Edges

none

## 4. Design

### What is there now

`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#scan_forks`
writes each non-terminal spec's blob to `<top>/<i>/<basename>` under one
`tempfile.TemporaryDirectory`. It writes one line per blob into `grade.sh` with the target and the
cutoff inside bare single quotes
(memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@2b57a776e68945c686ea9538150f6eaa198b8649:221).
It then sources that script as `. '<script>'`, also bare-quoted
(memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@2b57a776e68945c686ea9538150f6eaa198b8649:225).
The basename comes from `git ls-tree` at the ref in
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive`,
and the cutoff from `.memory-tree.conf` at that commit through `#read_conf`.

`tools/loop/breakpoints.py#run_sourced` runs `bash -c '. "$1" || exit 2; <script>' _ <driver>`
with the environment `read_clean_env()` builds. Its argv carries only the driver and its environment
is not the caller's, so neither channel can carry a value without an edit under `tools/`. Text is the
one channel, and quoting is what makes it safe.

`plan_state` reads its spec as `"$1"` and takes the basename as `${1##*/}`
(`tools/unattended/unattended.sh#plan_state`), so a quoted path reaches it unchanged.

Measured on 2026-11-19 by the spec writer's scratch probe over a fixture clone (PINNED):

- the current `scan_forks`, called with a spec keyed `2026-11-19-spec-a'$(touch pwned)'.md` and
  `root` a fixture clone, created `pwned` in that clone and raised
  `StateError the driver's plan_state graded 0 of 1 specs`;
- the same call with a benign key and `TMPDIR`, `TEMP` and `TMP` set to a directory named `o'q`
  raised `StateError` with `unexpected EOF while looking for matching`;
- `git ls-tree -r --name-only` listed `2026-11-19-spec-a'$(touch pwned)'.md` raw, and listed a name
  holding `é` C-quoted inside double quotes, so that one does not end `.md`;
- `0` of the `3072` spec basenames under `memory/builds/*/spec/` at `2b57a776e` fall outside
  `^[A-Za-z0-9._-]+\.md$`, and `0` of the `3068` at `9e21ac760` (PINNED, 2026-11-19).

### The change

In `scan_forks`, the `plan_state` line becomes:

```python
lines.append(f"printf '%s %s\\n' {i} \"$(plan_state {shlex.quote(target.as_posix())} "
             f"{shlex.quote(cutoff)})\"")
```

The run becomes `breakpoints.run_sourced(Path(root).resolve(), f". {shlex.quote(script.as_posix())}")`.
The index `i` is an `enumerate` integer and stays bare. `import shlex` joins the imports.

In `derive`, a module constant beside `RUN_RECORD`, written as a raw string:

```python
SPEC_NAME = re.compile(r"^[A-Za-z0-9._-]+\.md$")
```

After the listing loop fills `files`, and before `wanted` is built, the first spec path, in row
order then path order, whose last `/` segment fails `SPEC_NAME` raises:

```python
StateError(f"refused spec file name {p} at {commit[:12]}: not [A-Za-z0-9._-]+\\.md")
```

The check covers every spec path of every chain build, whatever `detail` is, because the listing is
the one boundary every spec crosses. The schedule's `tree_state` and the Atlas's `derive_actual`
already turn a `StateError` into their own refusal line, so neither caller changes.

Run records and deviation records are not checked. `RUN_RECORD` already admits only its fixed
names, and a deviation path is read by Python alone.

### The docstring

The exit-2 sentence adds "a spec file name outside `[A-Za-z0-9._-]+\.md` is refused". WHAT IT DOES
NOT CHECK adds: a spec whose name git's listing quotes, such as one holding a non-ASCII byte, `"`
or `\`, is not listed as a spec at all.

### Files touched (estimate)

`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-8-ledger.md`

### Alternatives rejected

- Values through env or positional arguments, the review's first form: `run_sourced` exposes
  neither, as above, and changing it is an edit under `tools/`.
- A data file read by a fixed `while IFS= read -r -d ''` loop in `grade.sh`: the `.` line still
  carries the script's path as text, so it needs `shlex.quote` anyway. That makes two mechanisms
  where one covers every site.
- Skipping an off-pattern spec instead of refusing it: the build's counts would then change
  silently, and a refusal names the file.

## 5. Acceptance criteria

The commands run from a worktree root, with these names set. The probe file is a scratch file under
the run's scratchpad, never in the repository:

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
STATE=memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py
FX=$(cygpath -m "$TEMP")/ta8fx      # a --shared clone of this repository checked out at 9e21ac760
KEY_BAD="memory/builds/dX/spec/2026-11-19-spec-a'\$(touch pwned)'.md"
KEY_OK="memory/builds/dX/spec/2026-11-19-spec-TOOL-dX-1.md"
PLANT="memory/builds/dWitnessedBar/spec/2026-11-19-spec-a'\$(touch pwned)'.md"
```

The probe loads `"$STATE"` by path and calls `scan_forks("$FX", {key: TEXT}, "2026-09-30")`. TEXT is
a spec body with a `## 2. Scope (IN)`, a `## 5. Acceptance criteria` and a `## 6. Gates` section,
each holding one line, and a `## 7. Open questions` holding the unresolved item
`- **F1 — Which?** (a) or (b).`, so `plan_state` grades it FORKED.

- **AC1** — When the probe runs with the key `$KEY_BAD`, it returns a set holding that key,
  and `test -e "$FX/pwned"` fails.
  Red when: the code at `2b57a776e` runs the same probe, which creates `$FX/pwned` and raises
  `StateError` with `graded 0 of 1 specs`, observed 2026-11-19.
  figure: PINNED at `2b57a776e`.
- **AC2** — When the probe runs with the key `$KEY_OK` and `TMPDIR`, `TEMP` and `TMP` all set to
  the existing directory `"$FX/o'q"`, it returns a set holding that key.
  Red when: the code at `2b57a776e` runs it, which raises `StateError` with
  `unexpected EOF while looking for matching`, observed 2026-11-19.
- **AC3** — When the clone at `$FX` commits, on a scratch branch, a spec at `$PLANT` whose status
  header reads `OPEN`, then `"$PY" <worktree>/"$STATE" --ref HEAD --claims none` run in the clone
  exits 2, its stderr is one line beginning `build-state: refused spec file name` and naming that
  path, and `test -e "$FX/pwned"` fails.
  Red when: the code at `2b57a776e` runs it, which creates `$FX/pwned`; and with `SPEC_NAME`'s
  check staged out and the quoting kept, the run exits 0 and dWitnessedBar's `counts` reads `OPEN` 1.
  fixture: the clone and its scratch branch are planted by the pass and removed after; the real
  repository's refs are never written.
- **AC4** — When `"$PY" <worktree>/"$STATE" --ref 9e21ac760 --claims none` runs in the unplanted
  clone after the change, its JSON compares equal under `cmp` to the JSON the same command printed
  there before the change, taken at the unit's start.
  Red when: a staged `SPEC_NAME` without `-` in its class refuses the first spec, and the command
  exits 2.
- **AC5** — When `"$PY" -c` loads `"$STATE"` by path and prints its `__doc__`, the text holds
  `[A-Za-z0-9._-]+\.md` in its exit-2 sentence and names the spec names git's listing quotes under
  `WHAT IT DOES NOT CHECK`.
  Red when: the docstring at `2b57a776e`, which holds neither.

## 6. Gates

The close runs the plain bar once. The legs below are those the files touched keep green. No suite
arm is added or moved, so no arm line is declared: the fixture observations above are the unit's
regression record, in its acceptance ledger.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-19 · initial draft, from
  2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief and the closing review's H1.

## 9. Reuse audit

The seam extended is `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#scan_forks`
itself, and its one boundary, the spec listing in `#derive`. The quoting is the standard library's
`shlex.quote`, which `tools/govkit/shims.py` and `tools/memory-tree/gen_build_index.py` already use
for shell text. `tools/loop/breakpoints.py#run_sourced` is used as it stands, because it opens no
argument or environment channel.
`python tools/codebase-map/reuse_lookup.py "quote a value before interpolating it into a sourced bash script"`
ranked name-stem helpers only (`before`, `read_policy_value`, `resolve_bash`), none of them a
shell quoter. The recall probe returned this build's review H1, spec 1's fork-scan paragraph and the
sibling class `memory/gotchas/unvalidated-arg-reaches-an-agent-shell-line.md`. That class covers a
caller's argument pasted into an agent's command line, so it is a neighbour and not this occurrence.

Recall terms used: `python tools/memory-recall/query.py "how do python instruments pass untrusted file names into a sourced bash script without injection" --terms "shlex.quote run_sourced plan_state shell injection sourced script tree-derived file name quoting bash -c"`
