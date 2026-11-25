# TOOL-aTemperedLane-1 — the Red-fix lane's L3 reads a spec change confined to the `gen:spec-records` region as no spec edit

**Status:** CLOSED · rev-1 · 2026-11-25 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aTemperedLane-1-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-aTemperedLane-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-25-build-TOOL-aTemperedLane-1-agent-ledger.md](../build/2026-11-25-build-TOOL-aTemperedLane-1-agent-ledger.md) | journal | TOOL-aTemperedLane-2 TOOL-aTemperedLane-3 |
| [2026-11-25-prompt-TOOL-aTemperedLane-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aTemperedLane-1-brief.md) | research | TOOL-aTemperedLane-2 |
| [2026-11-25-review-TOOL-aTemperedLane-1-closing-diff-review-round1.md](../reviews/2026-11-25-review-TOOL-aTemperedLane-1-closing-diff-review-round1.md) | diff-review | TOOL-aTemperedLane-2 |

<!-- /gen:spec-records -->

## 1. Goal

Limit L3 refuses a `Red-fix:` commit that changes any path under a build's `spec/` folder. The index
generator writes one record row into a spec whenever a record is added, so a fix commit that carries
its index regen is refused for a row nobody authored. This unit exempts exactly that change: a plain
modification whose every byte outside the one `gen:spec-records` region is unchanged.

## 2. Scope (IN)

- **S1** — `check_red_fix_limits` in `tools/memory-tree/routed_commits.py` leaves a spec path out of its
  L3 finding when all of these hold for that path in that commit. The raw status is exactly `M`. The
  two modes are equal. Each side's blob holds exactly one open and one close `gen:spec-records`
  marker, as whole lines, the open before the close. The two blobs are byte-identical once the bytes
  between the marker lines are cut, the marker lines themselves kept. Any other spec path stays a
  finding. Observed by AC1, AC2, AC3, AC4, AC5 and AC6.
- **S2** — The blobs are read by the object ids of the limits pass's own raw lines, in ONE
  `git cat-file --batch` per population, made only where the population holds a spec path that
  passes S1's status and mode halves. The pass's git calls are therefore none with no fix commit, one
  with no such path, and two otherwise, whatever the commit count. Observed by AC7.
- **S3** — One function of `routed_commits.py`, `read_blob_batch`, frames the batch stream for S2 and
  for the two reads that frame it inline today, `load_spec_paths` and the leg-manifest read in
  `check_routed_commits`. Both keep their verdicts and their spawn counts. Observed by AC8.
- **S4** — `SPEC_RECORDS_OPEN`, `SPEC_RECORDS_CLOSE`, `check_marker_line` and the `CR` constant that
  function reads are defined in `tools/memory-tree/tree_lib.py`, and
  `tools/memory-tree/gen_build_index.py` imports them from there under the same names. The
  source-level arm of `tools/memory-tree/marker-contract.test.sh` that greps the predicate's line
  reads it in its new file. Observed by AC9.
- **S5** — The docstrings of `routed_commits.py`, its row in `tools/memory-tree/README.md` and
  `help/red-fix-lane.md` state the exemption, the git-call figure where they state one, and what L3
  no longer checks. Observed by AC10.

## 3. Non-goals (OUT)

- Any other generated region, and any file outside a build's `spec/` folder.
- Limit L2 and the guarded list. That is TOOL-aTemperedLane-2.
- L1, L4, the waiver's reach, the lane's switch, the write gate and the record join.
- Grading what the region holds. The index generator's `--check` grades it at the tip.
- `.governance/instructions.toml`. Its unit `repo.kickoff.f06` says limit L3 refuses the index regen's
  row, the file is owner-guarded, and the stale sentence is reported to the owner.
- `help/README.md`. Its one line on the lane names the four limits and none of their bounds.
- The kit version, which the lander's `mint` moves once, after the last unit.

### Edges

- **hands-off** `TOOL-aTemperedLane-2` — `check_red_fix_limits` and the docstring's limits paragraph as
  this unit leaves them, the git-call figure included, which that unit's read moves again.
- **hands-off** external — the owner's edit of the instruction unit `repo.kickoff.f06`.

## 4. Design

### Evidence

- `tools/memory-tree/routed_commits.py#check_red_fix_limits` makes one `git log --raw --numstat -z
  --no-renames --root --diff-merges=first-parent` over the fix commits, and each raw token carries
  both modes, both blob ids and the status. The ids are abbreviated today; `--no-abbrev` makes them
  whole. It is called by `routed_commits.py#check_routed_commits` and by the `--red-fix-limits` verb
  in `routed_commits.py#main`, and by nothing else under `tools/`.
- `--no-renames` makes a rename a `D` and an `A`, and `--root` makes a root commit's paths `A`, so
  the status half of S1 already leaves both as findings.
- `gen_build_index.py#apply_region` refuses a file holding other than one pair in order, and reads a
  marker by `gen_build_index.py#check_marker_line`: column 0, exact equality after one trailing CR.
- `gen_build_index.py#render_spec_records` writes both marker lines bare and everything between them.
  Its render is compared with the file for every spec that has the region, so an interior that is not
  the render is a stale artifact under `gen_build_index.py --check`.
- `row_grammar.py#scan_engine_imports` refuses an import of `gen_build_index` by any sibling engine,
  so the three names S4 moves cannot be imported from where they are. The docstring of
  `tools/memory-tree/tree_lib.py` is the rule: a name two engines read lives there, and the module
  that defined it re-imports it.
- `routed_commits.py` frames a `cat-file --batch` stream inline twice, in `load_spec_paths` and in
  the manifest read of `check_routed_commits`. A third inline copy is what S3 avoids.
- PINNED 2026-11-25: a probe of S1's content predicate over the eight commits of AC1 called the one
  spec path of each identical outside the region. Of 3137 tracked specs, 5 hold no single ordered
  pair, so a fix commit changing one of those stays refused.
- PINNED 2026-11-25: no sha in `ROUTED_COMMIT_WAIVED` carries a `Red-fix:` trailer, so the exemption
  can make no waiver stale.

### The predicate

`extract_outside_records(body)` takes a blob's bytes, or None, and returns the text outside the
region or None. It decodes as latin-1, which is lossless over any bytes, splits on LF alone, and
finds the marker lines with `check_marker_line`. With one open and one close, the open first, it
returns the lines up to and including the open marker joined to the lines from the close marker on.
Anything else is None. No CRLF is folded, so a marker line that gained or lost a CR differs, and so
does a line ending anywhere outside the region.

A spec path is exempt when both sides' results are not None and are equal. A missing object, a
submodule entry and a side with no pair each read None, so the answer defaults to a finding.

### The pass

The loop over the log records keeps what it collects per commit, and collects beside it the blob ids
of each spec path whose status is `M` with equal modes. After the loop, one `read_blob_batch` call
reads every collected id, and only where there is one. The findings are then built per commit in the
order L1 to L4, the L3 line naming the paths left. The output's shape, the exit codes and the
summary line are unchanged.

`read_blob_batch(repo, names)` returns one entry per name, the body's bytes or None where the answer
is not a blob with a size. It goes through `run_git`, so the call is counted and pinned. A stream
that ends early is a `Refusal`.

### What L3 no longer checks

- What a fix commit writes between two unchanged marker lines. Whether it is the generator's row is
  `gen_build_index.py --check`'s answer, at the graded tip and never per commit, so a hand-written
  line inside the region that a later commit removes is seen by nothing.
- Where the pair sits. The region's extent is the parent's, so a pair an earlier commit widened
  widens what a fix commit may write.

### Inventory

| Minted or moved | Where | Cell |
|---|---|---|
| function `extract_outside_records` | `routed_commits.py` | `py.function` |
| function `read_blob_batch` | `routed_commits.py` | `py.function` |
| function `check_marker_line` (moved) | `tree_lib.py` | `py.function` |
| constants `SPEC_RECORDS_OPEN`, `SPEC_RECORDS_CLOSE`, `CR` (moved) | `tree_lib.py` | `py.constant` |

### The fixture

One scratch repository by `routed_commits.py#build_fixture`, its conf `set_fixture_conf`'s defaults.
Its first commit, before the cutoff, holds `src/a.txt` and two specs, each with a heading, one
`gen:spec-records` pair holding one row, and a section after it; the second spec also holds one
`gen:build-index` pair. Every other commit names the unit, carries `Red-fix: leg one`, and takes the
first commit as its parent. `build_fixture` writes mode 100644 alone, so it gains an optional `exec`
list of paths per commit, which it writes at 100755.

| Commit | Change | L3 |
|---|---|---|
| r1 | one row added inside the first spec's region, beside one line of `src/a.txt` | none |
| r2 | a row added and the section after the region edited | named |
| r3 | the heading above the region edited | named |
| r4 | every line ending outside the region made CRLF, the marker lines kept | named |
| r5 | the pair moved below the section | named |
| r6 | the pair removed | named |
| r7 | a second pair added | named |
| r8 | the close marker given a trailing space | named |
| r9 | both marker lines given a trailing CR | named |
| r10 | a new spec holding a pair | named |
| r11 | the first spec deleted | named |
| r12 | the first spec renamed, bytes unchanged | both paths named |
| r13 | a row added and the mode made 100755 | named |
| r14 | a row added to the first spec, the second's section edited | the second alone |
| r15 | a line changed inside the second spec's `gen:build-index` pair | named |

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/marker-contract.test.sh`
- `tools/memory-tree/README.md`
- `help/red-fix-lane.md`

### Alternatives rejected

- **Importing the three names from `gen_build_index`.** The sibling-import arm refuses it. A closure
  probe run 2026-11-25 over the leg manifest also showed `backlog migration selftest` would gain three
  policy modules outside its guard.
- **A second spelling of the markers in `routed_commits.py`.** A changed marker would then exempt
  nothing, or the wrong bytes, with no reader comparing the two.
- **`tree_lib.read_blobs_at`.** It folds CRLF and decodes, so two blobs that differ outside the
  region by line ending alone compare equal. It is keyed by `(rev, path)` and answers text, which is
  what TOOL-aTemperedLane-2 needs and this compare cannot use.
- **The unattended kit's `GEN_REGION_AWK`.** It cuts every generated region, drops the marker lines
  and folds CR, so it would exempt a moved marker and every other region.
- **Re-rendering the region from the commit's tree.** It costs a whole index render per fix commit,
  and the bar already holds the region to its render at the tip.

## 5. Production-readiness checklist

- security — this unit loosens a merge gate. The exemption is deny by default, reads blobs and runs
  no code from the graded commit, and §4 states what is no longer read.
- perf / scale — at most one more git call per population, and none where no fix commit modifies a
  spec.
- error / empty / loading states — an unreadable object leaves the finding standing; a truncated
  stream is the leg's exit 2.
- observability — no new line. An exempt path is absent from the L3 line, as any path inside a limit
  is.
- risks — moving the marker names changes what `gen_build_index.py` imports, so every reader of its
  old names is reached through the re-import, which AC9 observes.
- testing — the fixture above through the verb in the pass, and the arm of §7 at the close.
- migration — none. The output and the conf are unchanged.
- user docs — `help/red-fix-lane.md`, in this unit.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/routed_commits.py --red-fix-limits <sha>` runs for each of
  `dbc7bb6a`, `3fa017d5`, `918ffb5b`, `69a05280`, `b9a6d520`, `0b026d5c`, `e6196f84` and `f40a0e58`,
  it exits 0 and prints `is inside all four`.
  Red when: the exemption is absent, or reads abbreviated ids that name no object.
  fixture: the objects of `branch/unattended-dboundroles-62c3df`, present in this clone today.
- **AC2** — When the `--red-fix-limits` verb runs for r1, it exits 0.
  Red when: a row inside the region is read as a spec edit.
  fixture: the scratch repository of §4, "The fixture"; the tree holds none today, and AC3 to AC7
  use it too.
- **AC3** — When the `--red-fix-limits` verb runs for r2, r3, r4 and r15, each exits 1 naming
  `L3 spec edit` and the spec's path.
  Red when: an edit outside the region passes beside a row inside it, line endings are folded before
  the compare, or a second generated region is cut.
- **AC4** — When the `--red-fix-limits` verb runs for r5, r6, r7, r8 and r9, each exits 1 naming
  `L3 spec edit` and the spec's path.
  Red when: the marker lines are cut with the region, the pair count is not read, or a marker is
  matched after a strip.
- **AC5** — When the `--red-fix-limits` verb runs for r10, r11, r12 and r13, and for a parentless
  `Red-fix:` commit that adds the spec, each exits 1 naming `L3 spec edit` and the path.
  Red when: the status or the mode is not read, so anything but a plain modification is exempt.
- **AC6** — When the `--red-fix-limits` verb runs for r14, its L3 line names the second spec and not
  the first.
  Red when: one exempt path clears the commit, or one edited path puts an exempt one in the line.
- **AC7** — When `check_red_fix_limits` is called with no fix commit, with fix commits that modify no
  spec, with r1 alone, and with r1 to r15 together, `routed_commits.GIT_SPAWNS` rises by 0, 1, 2
  and 2.
  Red when: a blob read is made per commit or per path, or one is made where no spec was modified.
  figure: the four counts are PINNED for this unit's tree; TOOL-aTemperedLane-2 moves them.
- **AC8** — When a probe calls `load_spec_paths` over this tree from the built `routed_commits.py`
  and from the same file as `git show` prints it at the base sha 3d6c1702, the two
  maps are equal and not empty; and a fixture whose `LEG_MANIFEST` names a file grades a lane commit
  admitted where its tree holds that file, and `cannot be checked` where it does not.
  Red when: the shared framing misreads a missing object and shifts every answer after it.
- **AC9** — When `python -B -c` imports `tree_lib` and `gen_build_index`, the four names
  `SPEC_RECORDS_OPEN`, `SPEC_RECORDS_CLOSE`, `check_marker_line` and `CR` are the same objects in
  both. Also `grep -c "^def check_marker_line" tools/memory-tree/gen_build_index.py` prints 0, and
  the grep that the marker-contract suite's one-CR arm spells, run by itself with `KIT_MT` set to
  `tools/memory-tree`, exits 0 and names `tree_lib.py`.
  Red when: the predicate is copied rather than moved, or the arm still greps its old file.
- **AC10** — When `grep -c "gen:spec-records"` runs over `tools/memory-tree/routed_commits.py`,
  `tools/memory-tree/README.md` and `help/red-fix-lane.md`, each prints at least 1. Each names what
  L3 no longer checks, and no sentence of `routed_commits.py` still reads `any other exactly one`.
  Red when: a page keeps the old bound, or a docstring keeps the old git-call figure.

## 7. Gates

`routed commits name a specced unit` · `routed-commits selftest` · `policy fixtures` · `lexicon naming predicates` · `python reads (a name never bound, an import outside its guard)` · `marker contracts` · `build-index selftest` · `row-grammar selftest` · `tier2-review self-test` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The close's bar runs these once, after the last unit. The self-test legs are in the held tier, so
the close runs them where it asks for that tier.

New arm: tools/memory-tree/routed_commits.py · covers AC2 AC3 AC4 AC5 AC6 AC7 · the fixture's r2 to r15, each staged by dropping the one test of S1 it stands on, and the spawn counts by reading one blob per call · none
New arm: tools/memory-tree/marker-contract.test.sh · covers AC9 · a moved arm, its predicate made to strip every trailing CR in `tree_lib.py` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft.

## 10. Reuse audit

The seam is `routed_commits.py#check_red_fix_limits` and its one raw log, whose lines already carry
both blob ids. `python tools/codebase-map/reuse_lookup.py "compare a file at a commit and its parent
with a generated region blanked"` ranked no function that does it. For the region compare no existing
seam fits: `GEN_REGION_AWK` and `tree_lib.read_blobs_at` are the two nearest, and §4 says what each
would let through. What is reused is the marker contract, `check_marker_line` with the two
`SPEC_RECORDS_` constants, moved to `tree_lib.py` by that module's own rule, and the batched read
this file already frames twice. Recall ranked TOOL-aNimbleMend-10, which set the four limits and
whose one-call figure S2 moves, and TOOL-aMouldedFolio-4, which set the marker contract. Both were
read against source and agree with it.

Recall terms used: `python tools/memory-recall/query.py "Red-fix lane limit L3 spec edit, generated
spec-records region, marker line contract" --terms "red-fix lane limits L3 spec-edit gen:spec-records
generated-region marker blanked cat-file batch spawn-count routed_commits"`
