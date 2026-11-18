# TOOL-aTrimmedWait-19 — the hygiene suite's partition helper takes back main's name, so the landing's merge-loss check clears

**Status:** SPECCED · rev-1 · 2026-11-18 · node a · Tier-1 · base 3cecd39a0 · streams tooling · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-18-prompt-TOOL-aTrimmedWait-19-1-spec-writer.md](../prompts/2026-11-18-prompt-TOOL-aTrimmedWait-19-1-spec-writer.md) | journal | — |
| [2026-11-18-prompt-TOOL-aTrimmedWait-19-brief.md](../prompts/2026-11-18-prompt-TOOL-aTrimmedWait-19-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The hygiene suite defines its partition helper as `extract_hs_lines`, the name main carried, with
this branch's body. The tip then carries the definition the reconcile merge `01aad1747` lost, so
the pre-push merge-loss check over the landing range reads no loss
(`prompts/2026-11-18-prompt-TOOL-aTrimmedWait-19-brief.md`, the owner's answer of 2026-11-18).

## 2. Scope (IN)

- **S1** — In `tools/memory-tree/check-memory-hygiene.test.sh`, every spelling of
  `derive_partition_lines` becomes `extract_hs_lines`: the definition, the calls and the two FAIL
  texts that name it. No other byte of the suite changes. Observed by AC1 and AC2.
- **S2** — `memory/map/generated/symbols.json` re-rendered by `gen_map.py --write`, so the map's
  symbol tier names `extract_hs_lines` at the suite, and the render changes no other generated
  file. Observed by AC3.
- **S3** — The lexicon kit's `--merge-losses` over `origin/main..HEAD` clears the loss at
  `01aad174` as `restored`. Observed by AC4.
- **S4** — The CLOSED specs and records citing the old name stay as written, and the spec-token
  checks still pass over the two CLOSED specs that cite it. Observed by AC5.

## 3. Non-goals (OUT)

- Any change to the helper's body or argument form. Main's form read stdin
  (`extract_hs_lines() { grep . | sed ... | sort -u; }`,
  `tools/memory-tree/check-memory-hygiene.test.sh@4c50ac3a1a3b:1307`); this branch's reads `$1` and
  also sets aside check 26's `cache recomputed` lines, and that body is the one that survives.
- Any change to what the partition arms compare, to `FLOOR_ASSERTIONS` or to any shard floor. The
  rename moves no assertion.
- Editing the substance of `2026-11-15-spec-TOOL-aTrimmedWait-11.md`,
  `2026-11-16-spec-TOOL-aTrimmedWait-12.md`, the build README's unit 12 row, or any build or prompt
  record that cites the old name.
- Rewriting any commit, `01aad1747` included, or adding a `superseded:` line anywhere.
- Running the hygiene self-test suite inside the pass. The brief owes none; running one is the
  owner's call.
- An edit after the commit that sets this spec CLOSED. The status flip is the last change of the
  pass, and the pass commit carries its acceptance ledger at
  `memory/builds/aTrimmedWait/build/2026-11-18-build-TOOL-aTrimmedWait-19-1-acceptance-ledger.md`.

## 4. Design

### Evidence

Read on 2026-11-18 at `7e9ce394c`. The suite's blob is the same at local main `3cecd39a0`
(`1edc4fef047f`).

- The helper is one line (`tools/memory-tree/check-memory-hygiene.test.sh@1edc4fef047f:1406`). The
  name occurs 15 times on 9 lines, all inside the AC8 partition block and the TOOL-aTrimmedWait-11
  fixture arm below it (`:1406-1429`). Two of the 15 are inside FAIL texts (`:1423`, `:1425`). No
  other file under `tools/` spells either name: `git grep` over `tools/` outside the suite printed
  nothing.
- `check_merge_losses` (`tools/lexicon/lexicon.py#check_merge_losses`) clears a candidate as
  `restored` when the range tip defines the name at the lost path
  (`tools/lexicon/lexicon.py@89a20c878771:4431`, `if path in at_tip or at_tip - old`). The lost
  pair is `(tools/memory-tree/check-memory-hygiene.test.sh, extract_hs_lines)`, so the renamed
  definition at the same path clears it. The `superseded:` route reads only the merge's own
  message, which the brief rules out.
- The pre-push hook runs the mode from the repo root over `$main_remote..$main_local`
  (`.githooks/pre-push@71f1b13c0d83:1094`); `push-main.sh`'s `check_merge_losses` runs the same
  mode over the prepared range. Run at `7e9ce394c` on 2026-11-18,
  `--merge-losses origin/main..HEAD` printed the one LOSS line, then
  `graded=3 skipped=0 paths=180 losses=1 masked=0 restored=0 superseded=0 seconds=16.77`, exit 1.
  <!-- PINNED 2026-11-18 -->
- The landing merge onto main adds no loss. Main at `3cecd39a0` defines `derive_partition_lines`,
  which is then the merge base. A name in the base and absent from the other parent is skipped as
  that side's deliberate removal (`tools/lexicon/lexicon.py@89a20c878771:4382`).
- `python tools/lexicon/lexicon.py --suggest extract_hs_lines --as sh.function` answered OK, exit 0,
  on 2026-11-18, so the staged naming check takes the name.
- `gen_map.py --check` exited 0 at `7e9ce394c`, so the map is fresh before the rename.
  `derive_partition_lines` appears under `memory/map/` only in `symbols.json`.

### How the spec-token checks treat a CLOSED spec citing a retired name

Nothing is owed, and nothing is edited.

- The full run grades only live specs in the legs, paths, cites, bar, guards, claims, source,
  hands-off, size, supersede and ac-order joins, and counts the rest as
  `terminal spec(s) not graded` (`tools/check-spec-tokens.py@7ecdf1aa777d:2559`).
- The two joins whose population includes CLOSED specs are `carries`, which reads binding lines
  (`tools/check-spec-tokens.py@7ecdf1aa777d:123`), and `arm-labels`, which reads bullets opening
  `The suite arm labels` (`:228`). A grep for both shapes over every file citing the old name
  printed nothing.
- No join resolves a bare code-symbol token against the tree. The paths join wants a slash and an
  extension, and the cites join wants `<path>:<line>`. The rename keeps the suite's line count, so a
  `path:line` citation into it keeps its range.
- Hygiene check 25 resolves by-name tokens only for a spec whose status is not CLOSED or WONTDO
  (`tools/memory-tree/check-memory-hygiene.sh@278926df8f85:2392`, the `rilive` test), and check
  12's base resolution exempts a terminal spec.

### Steps

1. `sed -i 's/derive_partition_lines/extract_hs_lines/g' tools/memory-tree/check-memory-hygiene.test.sh`.
2. `python tools/codebase-map/gen_map.py --write`.
3. The acceptance probes, the ledger, the pass commit, then the status flip.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.test.sh` · `memory/map/generated/symbols.json` ·
`memory/builds/aTrimmedWait/build/2026-11-18-build-TOOL-aTrimmedWait-19-1-acceptance-ledger.md`

## 5. Acceptance criteria

`$F` is `tools/memory-tree/check-memory-hygiene.test.sh`.
`$R` is `origin/main..HEAD`, the range the pre-push hook grades once the pass lands on main.

- **AC1** — When `git grep -n derive_partition_lines -- tools/` runs it prints nothing,
  `grep -c '^extract_hs_lines() { ' $F` prints 1, and `bash -n $F` exits 0.
  Red when: a call or FAIL text keeps the old name, the definition is doubled, or the suite no
  longer parses.
- **AC2** — When
  `cmp <(git show 3cecd39a0:$F | sed 's/derive_partition_lines/extract_hs_lines/g') $F` runs, it
  exits 0 silent.
  Red when: any byte besides the name changes, the body, an assertion or a floor included.
- **AC3** — When `python tools/codebase-map/gen_map.py --check` runs after step 1 and before
  step 2, it exits 1; after step 2 it exits 0. Then
  `grep -c '"id": "extract_hs_lines"' memory/map/generated/symbols.json` prints 1,
  `git grep -c derive_partition_lines -- memory/map/` prints nothing, and
  `git status --porcelain -- memory/map/` lists only `memory/map/generated/symbols.json`.
  Red when: the map is not re-rendered, or the render moves another generated file.
- **AC4** — When `python tools/lexicon/lexicon.py --merge-losses "$R"` runs from the repo root
  after the pass commit, it exits 0, prints no `merge-losses: LOSS` line, and its summary line
  carries `losses=0` and `restored=1`.
  Red when: the tip defines the name at another path or not at all, so the loss stays.
  cost: about 17 seconds.
  figure: `restored=1` is PINNED 2026-11-18 against the one loss the run at `7e9ce394c` printed.
- **AC5** — When
  `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md --spec memory/builds/aTrimmedWait/spec/2026-11-16-spec-TOOL-aTrimmedWait-12.md`
  runs after step 1 it exits 0, and `git diff --quiet 3cecd39a0 -- memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md memory/builds/aTrimmedWait/spec/2026-11-16-spec-TOOL-aTrimmedWait-12.md`
  exits 0.
  Red when: a join resolves a cited name against the tree, or the pass edits a CLOSED spec.

## 6. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness`

`python tools/check-spec-tokens.py --legs-for` over the suite names only broad guards; the two
recall floor legs are owed by the paths under `memory/`. No arm is added or moved: the partition
arms are renamed, not changed. The pre-push bar runs at the push, through `push-main.sh`, run by
the main loop.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-18 · initial draft.

## 9. Reuse audit

The seam is the `restored` clearance already in `tools/lexicon/lexicon.py#check_merge_losses`;
`reuse_lookup.py "clear a merge loss by restoring a lost shell function definition at the range tip"`
ranked `check_merge_losses` among its candidates, and this unit adds no code beside it.

Recall terms used: `query.py "how is a merge-loss refusal cleared after a reconcile merge dropped a definition" --terms "merge-losses restored superseded reconcile lexicon definition tip pre-push rename helper partition"`
