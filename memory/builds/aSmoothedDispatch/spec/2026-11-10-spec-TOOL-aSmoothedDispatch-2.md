# TOOL-aSmoothedDispatch-2 — `--dispatch` removes the run-state file from its declared writes with a note instead of refusing

**Status:** SPECCED · rev-2 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md) | research | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-token-fix.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-token-fix.md) | research | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-3 |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-2-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-2-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A `--dispatch --writes` path that IS the run's own run-state file is removed from the declaration
with one printed note, and the dispatch goes on with the other paths. Today that path is refused
with check 49, although every pass commit carries the file and both readers of a declaration already
leave it out. A path that only contains the file, such as its build directory, keeps refusing.

## 2. Scope (IN)

- **S1** — A driver helper `remove_run_state_writes` takes the run-state file and the `--writes`
  paths. It keeps every path whose `normpath` spelling differs from the file's in an array, and sets
  a flag when one matched. Equality only: a container, a sibling or a prefix-sharing name is kept.
  Observed by AC1.
- **S2** — `verb_dispatch` calls the helper after `refuse_if_terminal` and before the condition-3
  flat-half loop. When the file was among the paths, it prints one note on stderr and resets its
  positional parameters to the kept paths. Every later reader of `"$@"` sees the reduced set: the
  shared-record loop, the generated-index pairing, condition 1, and the `want` composition the row
  is parked from. Observed by AC2 and AC3.
- **S3** — A declaration left empty by the removal refuses with check 49 and a new message, because a
  row naming no path is never closed by `check_pass_open` and is read by `--check-commit` as no open
  pass. Observed by AC4.
- **S4** — The containment refusal's message no longer claims the exact file, which can no longer
  reach it. It reads `--dispatch declares a path containing the run-state file, ...` with the rest
  unchanged, and the suite's `RELF_MSG` moves with it. Observed by AC2 and AC4.
- **S5** — The `--dispatch` bullet of the verbs reference gains one sentence: a `--writes` naming the
  run-state file is left out of the declaration with a note, and a path containing it is still
  refused. It lands in the kit template and its rendered copy. Observed by AC5.

## 3. Non-goals (OUT)

- `--check-commit` and check 23 do not change. Both already leave the file out of a pass's graded
  writes (`tools/unattended/unattended.sh:14244`, `tools/unattended/check-unattended.sh:4587`).
- The `--writes` argument grammar is unit 1's. This unit's arms pass one path per `--writes`, the
  grammar at base.
- No case-folded match. A `run.md` spelling on a case-insensitive filesystem is declared as an
  ordinary path today and stays so.
- The shared-records refusal, the generated-index pairing and condition 1 are untouched, and a path
  overlapping a sibling or a `SHARED_RECORDS` entry still refuses (brief Non-goals).
- No help page. `help/` holds no page on the unattended verbs (`grep -rl -- --dispatch help/` finds
  none), and the verbs reference is that surface.
- No kit version bump by hand. The lander's `mint` moves it (build README rules).

### Edges

none

## 4. Design

### Where the refusal is today

`verb_dispatch` derives `rel` from `runmd_of` (`tools/unattended/unattended.sh:14280`, the helper at
:1540 spells `$M/builds/<slug>/RUN.md`). The condition-3 flat-half loop at :14533-14536 refuses any
`--writes` path that `overlaps` `rel`, which is `covers` both ways (`tools/unattended/lib-unattended.sh:746-751`).
So the exact file and every directory above it get one message. The containment direction is the
fix TOOL-dUnstalledConvoy-21 made, and the suite pins it at
`tools/unattended/unattended.test.sh:8848-8849` (`--writes memory`, `--writes memory/builds`).
The exact-file arm is :8786.

The file needs no declaration. `--check-commit` skips it by equality (`unattended.sh:14244`), check 23
removes it with `grep -v -x -F "$f"` (`check-unattended.sh:4587`), and `--dispatch` itself stages it
(`stage_or_fail "$rel"`, :14675). Declaring it buys nothing and refusing it costs a re-dispatch.

### The helper

Placed directly above `verb_dispatch`. `normpath` leaves its answer in `_np` and forks nothing
(`lib-unattended.sh:720-737`), so the loop spawns no process.

```bash
# TOOL-aSmoothedDispatch-2: THE RUN-STATE FILE ITSELF IS REMOVED FROM A DECLARATION, never refused.
# Every pass commit carries it, and --check-commit and check 23 already leave it out, so a pass that
# names it has declared nothing a comparison reads. EQUALITY ONLY, over `normpath`: a path CONTAINING
# the file stays in the set and the containment refusal in verb_dispatch still answers it.
remove_run_state_writes() { # run-state file · writes... -> _rw_keep (array) · _rw_removed (1 when one was)
  local _rs _p
  normpath "$1" >/dev/null; _rs=$_np; shift
  _rw_keep=(); _rw_removed=""
  for _p in "$@"; do
    normpath "$_p" >/dev/null
    [ "$_np" = "$_rs" ] && { _rw_removed=1; continue; }
    _rw_keep+=("$_p")
  done
}
```

A kept path keeps its raw spelling, because the `want` composition at :14641-14643 normalises every
path before the row is parked.

### The call site

Inserted between `refuse_if_terminal "$rel" --dispatch || return 1` (:14525) and the condition-3
comment block that opens at :14526:

```bash
  remove_run_state_writes "$rel" "$@"
  if [ -n "$_rw_removed" ]; then
    echo "unattended: dispatch — $rel is this run's run-state file, which every pass commit carries and --check-commit and check 23 already leave out, so it is removed from this declaration rather than declared: $unit" >&2
    [ "${#_rw_keep[@]}" -gt 0 ] || { fail 49 "--dispatch was given no --writes path except the run's run-state file, which is never declared, so the declaration would name no path: $unit"; return 1; }
    set -- "${_rw_keep[@]}"
  fi
```

The note goes to stderr, as the sibling notes at :14390 and :14582 do. Placing the call after the
shape loop at :14502-14524 means a malformed path is still refused first. Placing it before the
condition-3 loop means every reader of `"$@"` below sees the reduced set.

The message at :14535 becomes:

```text
--dispatch declares a path containing the run-state file, and every pass in the run shares that file, so two passes declaring it are not disjoint by construction: $p
```

### Why the empty case refuses

`check_verb_flag` at :14285 already requires one `--writes`. A row parked with an empty set would
never close, because `check_pass_open` loops over no declared path (:14142), and `--check-commit`
reads an empty set as no open pass (:14235). That defect is the one the refusal at :14504 names for
an empty path, so the same reason refuses here and no fork arises.

### Bug classes read

`guard-above-a-fold-makes-its-fallback-dead`: the helper settles the equal case above the `overlaps`
loop, so that loop's equal case is dead. S4 rewords its message so it no longer names that case, and
the containment arms at :8848-8849 keep it live. `two-guards-one-question-two-answers`: three sites
now ask whether a path is the run-state file. `--check-commit` and check 23 compare git's spelling
exactly, and this helper compares `normpath` spellings, so it removes every spelling they would skip
and none they would grade. `a-helper-extraction-blinds-a-per-function-rule`: no per-function source
rule pairs anything this helper holds.

### Pinned ordinals

`tools/unattended/unarmed-branches.txt` pins `fail 49` ordinals 8, 18, 21 and 22 of the driver, the
last at :14383. The new branch lands after :14525, so its ordinal follows every pinned one and no pin
moves. PINNED, counted at base `ae6735c1` with `grep -n "fail 49 "`. A unit built earlier that adds
a `fail 49` above :14383 moves those pins itself.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `remove_run_state_writes` | shell function | `sh.function`, which `python tools/lexicon/lexicon.py --suggest remove_run_state_writes --as sh.function` answered OK |
| `_rw_keep`, `_rw_removed` | shell globals the helper leaves its answer in | none, a variable is not a graded surface |

### Rollout

Units 1, 2, 3, 4 and 6 all edit `tools/unattended/unattended.sh`, so they build one at a time (build
README rules). This unit is order 2, so it builds after unit 1. Line numbers here are at base
`ae6735c1` and drift once unit 1 lands, so the builder anchors on the quoted text. Unit 1 may also
reword the same verbs bullet. This unit's sentence follows the sentence ending
`only the index WITH its generator is refused.`, which unit 1 has no reason to move.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

### The verbs sentence

In the bullet that opens `- **Before dispatching a pass, DECLARE its write set** (M6)`, directly after
the sentence ending `only the index WITH its generator is refused.`, the bullet gains:

```text
A `--writes` naming the run's own run-state file is removed from the declaration with a note,
because every pass commit carries that file, and a path containing it is still refused.
```

The template and `memory/guides/UNATTENDED-VERBS.md` are byte-identical at base (`cmp` exits 0), so
the builder applies the same bytes to both and re-wraps the bullet at its existing width.

### Alternatives rejected

- **Remove the file silently.** The brief asks for one printed note, and a silent drop hides a
  mis-aimed declaration from the agent that wrote it.
- **Remove any path that `overlaps` the file.** That would drop `--writes memory/builds/tRun`, a real
  directory claim, and the brief keeps it refused.
- **Inline the loop in `verb_dispatch`.** The only direct observation would then need the suite's
  several-hundred-line fixture. A sourced helper is probed in one line, as `normpath` is.
- **Park an empty row when only the file was named.** It never closes and grades nothing.

## 5. Production-readiness checklist

- security: no new write path. The set only shrinks, and every path still passes the shape and
  overlap refusals.
- perf / scale: one `normpath` per path, no fork.
- error / empty / loading states: an all-removed declaration refuses with check 49 (S3).
- observability: the stderr note names the file and the unit, and the run log records the call.
- risks: a later unit adding a `fail 49` above :14383 moves the pinned ordinals; that unit owns them.
- testing: AC1 and AC2 are direct probes, and AC3 and AC4 are suite arms the main loop observes.
- migration: N/A — rows already parked are untouched, and none can name the file today.
- user docs: the verbs reference sentence (S5).

## 6. Acceptance criteria

- **AC1** — When this call to `remove_run_state_writes` runs from the repository root,
  ```bash
  bash -c '. tools/unattended/unattended.sh; remove_run_state_writes memory/builds/s/RUN.md a ./memory//builds/s/RUN.md memory/builds/s memory/builds/s/RUN.md/ memory/builds/s/RUN.md.bak; echo "${_rw_keep[*]} removed=$_rw_removed"'
  ```
  it prints:
  ```text
  a memory/builds/s memory/builds/s/RUN.md.bak removed=1
  ```
  The same call with only `a b` after the run-state file prints `a b removed=`.
  Red when: a raw string compare keeps the `.//`-spelled copy of the file, a containment test drops
  the build directory, or a prefix match drops the `RUN.md.bak` sibling.
- **AC2** — When the body of `verb_dispatch` is read with this pipeline,
  ```bash
  bash -c '. tools/unattended/unattended.sh; declare -f verb_dispatch' | grep -n -e refuse_if_terminal -e remove_run_state_writes -e '_rw_keep\[@\]' -e 'overlaps "$p" "$rel"'
  ```
  the four matches print in that line order. And
  `grep -c 'declares the run-state file, or a path containing it' tools/unattended/unattended.sh`
  prints 0.
  Red when: the call sits after the condition-3 loop, so the exact file is still refused, or after
  the `want` composition, so the file reaches the parked row; or the old message survives.
- **AC3** — When the driver suite's condition-3 flat-half block runs at the close, the call
  ```bash
  run --dispatch tRun --pass ARCH-tRun-1 --writes memory/builds/tRun/RUN.md --writes ${PFX}alpha.sh
  ```
  prints `dispatch declared` and the note `is removed from this declaration rather than declared`,
  and the parked `dispatch` row in the fixture's run-state file names `${PFX}alpha.sh` and not the
  run-state file.
  Red when: the call to `remove_run_state_writes` is removed from `verb_dispatch`, which turns the
  call into the containment refusal.
  permission: this pass runs no suite. The main loop observes it at the close under §7's `New arm:`.
- **AC4** — In that block, the call
  ```bash
  run --dispatch tRun --pass ARCH-tRun-1 --writes memory/builds/tRun/RUN.md
  ```
  prints `no --writes path except the run's run-state file`, and the call
  ```bash
  run --dispatch tRun --pass ARCH-tRun-1 --writes memory/builds/tRun
  ```
  prints the reworded
  `RELF_MSG`, `declares a path containing the run-state file`. The arms at
  `memory` and `memory/builds` still hit `RELF_MSG`.
  Red when: the empty case parks a row, or the helper removes by `overlaps` so the build directory is
  declared.
  permission: as AC3.
- **AC5** — When
  `tr -s '\n ' ' ' < tools/unattended/VERBS.template.md | grep -o 'run-state file is removed from the declaration' | wc -l`
  runs, it prints 1, and `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md`
  exits 0.
  Red when: the template lacks the sentence, or the rendered copy was not moved with it. The `tr`
  joins wrapped lines, so a phrase broken across two lines still counts.

## 7. Gates

`unattended kit gate` · `tier2-review self-test` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC3 AC4 · deleting the `remove_run_state_writes` call from `verb_dispatch` reds the exact-file and file-only arms, and swapping its equality for `overlaps` reds the build-directory arm · none

The exact-file arm at `tools/unattended/unattended.test.sh:8786` is replaced, not kept beside the new
one. `RELF_MSG` at :8853 takes the reworded text. The suite's count floor is shrink-only, so added
arms move nothing.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft from the brief's item 2 and acceptance 2.
- rev-2 · 2026-11-10 · §6 AC1 · AC2 · AC3 · AC4 · each command whose words the spec-token checker
  graded as untracked paths, and AC1's expected output, moved from inline backticks into an
  indented fenced block inside its bullet; no criterion's meaning, command or output changed
  (2026-11-10-prompt-TOOL-aSmoothedDispatch-1-token-fix).

## 10. Reuse audit

The seam is the condition-3 flat-half loop of `verb_dispatch` (`tools/unattended/unattended.sh:14533-14536`)
and the kit's `normpath` (`tools/unattended/lib-unattended.sh:720`), which every containment answer in the
kit already goes through. The exemption it copies is the one `--check-commit` makes at :14244 and check
23 at `tools/unattended/check-unattended.sh:4587`. `python tools/codebase-map/reuse_lookup.py "dispatch
refuses declared write path that is the run-state file"` ranked generic name stems only (`run`,
`write`, `declares`), so no existing seam fits beyond the loop being extended. The recall query
returned the dUnstalledConvoy lib-fix review, the TOOL-dUnstalledConvoy-21 containment arms and a
dFairHearing builder return confirming the hygiene leg's write-set comparison leaves the run-state file
out. No record argues for refusing the exact path. `gen_build_index.py --asks --path
tools/unattended/unattended.sh` named no ask on this refusal.

Recall terms used: `python tools/memory-recall/query.py "should dispatch drop the run-state file from a declared write set instead of refusing it" --terms "dispatch writes run-state RUN.md declared set check 49 condition 3 overlaps disjoint pass commit"`
