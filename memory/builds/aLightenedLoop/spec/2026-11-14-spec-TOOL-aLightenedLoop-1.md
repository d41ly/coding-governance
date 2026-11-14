# TOOL-aLightenedLoop-1 — the commit tail: `--write` writes only changed bytes, a render stamp answers the hook, check 9's staged skip admits a records edit, and check 29 exits early

**Status:** CLOSED · rev-2 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 1 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aLightenedLoop-1-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aLightenedLoop-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md](../build/2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md) | research | TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 |
| [2026-11-14-build-TOOL-aLightenedLoop-1-override-1.md](../build/2026-11-14-build-TOOL-aLightenedLoop-1-override-1.md) | override | — |
| [2026-11-14-build-TOOL-aLightenedLoop-1-red-fix-1.md](../build/2026-11-14-build-TOOL-aLightenedLoop-1-red-fix-1.md) | red-fix | — |
| [2026-11-14-build-TOOL-aLightenedLoop-1-red-fix-2.md](../build/2026-11-14-build-TOOL-aLightenedLoop-1-red-fix-2.md) | red-fix | — |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md) | research | TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5 |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-fork-answers.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-fork-answers.md) | research | TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-5 |
| [2026-11-14-prompt-TOOL-aLightenedLoop-1-fork-fold.md](../prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-fork-fold.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

A builder's commit renders the build index twice: once by its own `--write`, and once inside the
pre-commit hook's check 9. Check 29 then reads the whole carries join to report that it graded
nothing. This unit removes that fixed cost, measured at 68 to 230 s per commit in dSafePassage, and
moves no verdict, refusal text or rendered byte of checks 9 and 29.

## 2. Scope (IN)

- **S1** — `write_text` in `tools/memory-tree/gen_build_index.py` leaves a file alone when its
  bytes on disk already equal the bytes it would write. Observed by AC1 and AC2.
- **S2** — `--write` leaves a render stamp in the git directory when a `--check` of the tree it
  wrote would be green, and `--check --staged`, once a render is owed, answers from the stamp when
  the tree's render key still equals it. Option A of §8 F1, under the owner's override of `[class]`.
  Observed by AC3 and AC4.
- **S3** — `check_staged_render` admits a modified file under a build's `build/` folder whose
  binding head is unchanged, unless the file is a deviation record or sits in a folder a `DESIGN_*`
  key names. Such a file then goes through the cited-id comparison that already decides every
  non-structural file. Observed by AC5 and AC6.
- **S4** — `--check-coverage --staged`, once its trigger fires, prints its count line and exits 0
  without reading any spec history when no chain spec stands at INPROGRESS. Observed by AC7 and AC8.
- **S5** — `tools/memory-tree/README.md` states the stamp, the narrowed skip and the early exit.
  Observed by AC9.
- **S6** — The wall-clock cost of each touched verb is measured before and after on node `a` and
  recorded in this unit's acceptance ledger. Observed by AC10.
- **S7** — The selftest arms of §7 land in `gen_build_index.py --selftest` and
  `tools/check-spec-tokens.test.sh`. NOT OBSERVED by a criterion of this spec: a suite is no
  acceptance observation, so the main loop observes each arm red and then green at the close.

## 3. Non-goals (OUT)

- No change to `check_index_input`. It stays the trigger of check 29's and check 30's staged
  verbs, and those triggers do not move.
- No change to what check 9 or check 29 grades, or to any refusal text either prints.
- No change to `tools/memory-tree/check-memory-hygiene.sh`, `memory/HYGIENE.md` or its template.
  The hygiene text for checks 9 and 29 stays true as written (§4, "Documents").
- No stamp read by a full `--check`, `--check --with-verdicts` or any verb but `--check --staged`.
  The push boundary renders in full.
- No cache of `plan()`'s artifacts and no cache inside the carries join.
- No kit-version move. The lander mints it.
- No repair of the staged skip's existing blind spot over the nodes deriver's inputs outside build
  folders (§4, "What S3 does not check").

### Edges

- **hands-off** external — the staged skip treats `memory/DECISIONS.md`, `memory/gotchas/` and
  `memory/map/generated/` as non-structural today, while the nodes deriver `DESIGN_NODES` names
  reads them. A text edit there that cites no new id skips check 9 and can still move a coverage
  region. That gap predates this unit and is left for its own ask.

## 4. Design

### Evidence

Read at `846d51d3`. Line citations are blob-pinned to that commit.

| Claim | Where |
|---|---|
| `write_text` opens every path `"wb"` and writes, whatever is on disk | `tools/memory-tree/gen_build_index.py#write_text`, `tools/memory-tree/gen_build_index.py@846d51d3:296` |
| `cmd_write` writes every artifact `plan()` returns, then prints one count line | `tools/memory-tree/gen_build_index.py@846d51d3:3228`, `:3235` |
| `cmd_write` prints the verdicts and ignores their return | `tools/memory-tree/gen_build_index.py@846d51d3:3241` |
| Any path under a build's `spec`, `build`, `prompts` or `reviews` folder is structural | `tools/memory-tree/gen_build_index.py@846d51d3:927` |
| A structural staged path returns "render" before any blob is read | `tools/memory-tree/gen_build_index.py@846d51d3:1027` |
| The id comparison reads HEAD and index blobs of every modified non-structural file | `tools/memory-tree/gen_build_index.py#check_staged_render`, `:1060` |
| `--check --staged` prints the owed line, then runs the full `cmd_check` | `tools/memory-tree/gen_build_index.py@846d51d3:8922`, `:8924` |
| On exit 0, check 9 prints only a line opening `build-index: render SKIPPED` | `tools/memory-tree/check-memory-hygiene.sh@846d51d3:1510` |
| A record's bindings are read from its first `BIND_HEAD_LINES` unfenced lines only | `tools/memory-tree/tree_lib.py@846d51d3:558` |
| The as-built view reads every tracked `*/build/*-deviation-*.md` record's body | `tools/memory-tree/deviation_join.py#read_records` |
| The nodes deriver reads its own folder's records and runs `git status --porcelain` | `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py`, lines 121 to 305 and 450 |
| The render reads no clock | `tools/memory-tree/gen_build_index.py#derive_last_record` docstring, and a grep for `today()` finds only `--new-build` and `--new-spec` |
| Check 29's staged held test, then the whole coverage read | `tools/memory-tree/gen_build_index.py@846d51d3:2964`, `:2967` |
| Check 29's count line needs only `graded`, `holding`, the chain-build count and the cutoff | `tools/memory-tree/gen_build_index.py@846d51d3:2985` |
| The checker reads statuses, then the spec history, then runs the join | `tools/check-spec-tokens.py@846d51d3:996`, `:1151`, `:1152` |
| The coverage stub takes `(root, conf=None)` and nothing else | `tools/memory-tree/gen_build_index.py#test_coverage_stub` |

A probe on node `a` at `846d51d3`, run once with no other load, timed the coverage read's
phases: `read_design` 2.1 s, the status pass over 1,543 chain specs 1.3 s, `read_spec_revisions`
8.9 s, and `derive_carries_coverage` whole 15.8 s. No chain spec stood at INPROGRESS: 336 CLOSED,
1,200 DEFERRED and 7 WONTDO. Those figures are PINNED to that reading; AC10 re-measures.

### S1 — write only changed bytes

`write_text` reads the existing file's bytes when the path is a file. When they equal
`text.encode("utf-8")` it returns without opening the file for writing. Otherwise it writes as
today. Every caller gains the skip, the as-built view's write and the selftest fixtures' writes
included, and none of them reads a file's modification time.

`cmd_write` keeps printing `build-index: wrote <n> artifact(s)` with `n` the artifact count, not
the count of files written. That line's bytes do not move.

### S2 — the render stamp

§8 F1 resolved to option A: the stamp is consulted under `--check --staged` only, under the owner's
override of the charter's `[class]` practice (§8 F1 cites the record).

**The key.** `derive_render_key(root)` returns a hex SHA-256 digest, or the empty string when any
git call fails. Every git call goes through `_build_git_env()`, as the render's own reads do. The
digest covers these lines, in this order:

1. `HEAD <oid>`, from `git rev-parse --verify -q HEAD`. The commit and not its tree, because the
   carries join reads spec history.
2. Every tracked path, from `git ls-files -z`. The render reads the tracked set from the index.
3. For each path `git diff HEAD --name-only --no-renames -z` lists, the path and a digest of its
   working-tree bytes, or `absent`. This names the working tree's content wherever it differs
   from HEAD, staged or not.
4. Every untracked, unignored path, from `git ls-files --others --exclude-standard -z`. The nodes
   deriver's `git status --porcelain` reads them.

Staging a modified file moves none of the four, so the builder's `git add -u` after `--write` keeps
the key. Adding a new file moves line 2, which is right, because the render reads `git ls-files`.

**The stamp.** `resolve_render_stamp(root)` returns `git rev-parse --git-path
gen-build-index-render-stamp`, made absolute against `root`. The file is never tracked and never
seen by `git status`, so it is no input of the key.

**The writer.** `cmd_write` removes any stamp first, before it writes anything. After its last
print it writes the key when all four hold: `print_verdicts` returned 0, `unmanaged` is empty,
`guarded` is empty, and no view refusal is held. Those are the conditions under which `cmd_check`
exits 0 on the tree just written. A key that derives empty writes no stamp.

**The reader.** In `main`, after `build-index: render owed under --staged — <why>` prints, the
staged branch reads the stamp. When it is non-empty and equals `derive_render_key(root)`, the verb
prints this line and returns 0:

```text
build-index: render answered by the stamp --write left on this exact tree; the push boundary renders in full
```

Any other case runs the full `cmd_check` as today. The line does not open with
`build-index: render SKIPPED`, so check 9's exit-0 branch prints nothing for it, as it prints
nothing for today's green full render.

**What S2 does not check.** The stamp asserts that `--check` would be green on the tree `--write`
left. That holds when one `--write` is a fixed point, which today's hook confirms on every commit
and which the stamp stops confirming at the commit. A render that is not a fixed point is caught
at the push boundary's full render instead. The key does not cover the Python interpreter or the
process environment beyond git's. The stamp is a guard sharing state with what it guards, which
the charter's `[class]` rule forbids. The owner set that rule aside for this stamp at §8 F1, and
the builder records the override as a `memory/DECISIONS.md` row.

### S3 — the narrowed staged skip

A staged path is ADMITTED when its status is `M`, `check_index_input` answers true for it, and:

- the path is `<m>/builds/<slug>/build/<name>`, three parts or more under `builds/`, with
  `build` as the second;
- its name does not match `*-deviation-*.md`, the glob `deviation_join.read_records` reads;
- its folder is not the folder of any non-blank `DESIGN_RECORD`, `DESIGN_VIEW` or `DESIGN_NODES`
  value in the conf.

An admitted path is QUIET when `read_record_head` of its HEAD blob equals that of its index blob
and its cited id set is unchanged. `read_record_head(text)` returns
`list(unfenced(text))[:BIND_HEAD_LINES]`, the slice `read_bindings` reads, through the constant and
the function `gen_build_index.py` already imports from `tree_lib`. It takes the whole head and not
only its binding lines, so any head edit renders. Over-sensitive is the safe direction.

**The one rule: a render still owed prints today's reason.** The owed line rides inside check 9's
capture, which hygiene prints whole on a red render, so its bytes are refusal text. The loop
therefore walks the whole staged set in today's order and records `first`, the reason today's loop
returns first, admitted paths counted as structural exactly as today. It does not return at an
admitted path. It returns `(True, first)` at once only when a path that is not admitted would have
returned today. Admitted paths join `modified`, and the one `cat-file --batch` reads their blobs
with the rest. Then:

- an admitted path that is not quiet returns `(True, first)`;
- a non-admitted modified path whose ids change returns `(True, first or <today's id reason>)`;
- every git or decode failure after the loop returns `(True, first or <today's failure reason>)`;
- otherwise the render is skipped.

So the narrowed classifier skips exactly when every trigger today's classifier saw was a quiet
admitted path, and in every other case returns today's pair byte for byte. A skip with no admitted
path keeps today's reason. A skip with `k` admitted paths appends
`, {k} of them build records whose binding head is unchanged` before `, none changing` in today's
skip text.

**The one declared output delta.** A skip announces itself, as TOOL-aTrimmedHook-1 made every
skip do: on a commit that today rendered green and printed nothing, check 9 now prints its
`memory-hygiene: check 9: render SKIPPED` line. Its exit code is 0 either way.

**Why each exclusion.** A deviation record's body feeds the as-built view, which `--check`
compares. A file in a `DESIGN_*` folder feeds the view, the design record or the nodes deriver,
whose reads include its sibling records. Filenames, the other thing the renderer reads from a
record, cannot move on a modify.

**What S3 does not check.** It reads the index, and the renderer reads the working tree, as the
skip already says. A nodes deriver that starts reading a build folder other than its own is not
seen. The derived folder set catches only the folders the three keys name. The deriver's reads
outside build folders are the existing skip's business, unchanged here (§3, the hands-off edge).

### S4 — check 29's early exit

`derive_carries_coverage` gains a keyword `building=False`. `read_carries_specs` is split at its
history read. Its first half becomes `read_carries_texts`, which returns the texts, the statuses and
the skipped counts. `read_carries_specs` keeps its name and signature and calls the half, then
reads the history, so `tools/check-spec-tokens.test.sh` and every other caller are unchanged.

With `building=True`, after `read_design` and `read_carries_texts`, when no status is
`INPROGRESS`, it returns this value and reads nothing more:

```python
{"state": "armed", "cutoff": cutoff, "building": False,
 "builds": {b: {"specs": [(p, statuses[p]) for p in paths of b], "findings": None}
            for b in design["builds"]}}
```

`findings` is `None`, and never an empty list, so no reader can take the early value for a clean
coverage. `read_carries_coverage(root, conf, resolve=None, building=False)` passes
`building=True` to the derive call only when asked, so the stub's two-argument signature still
serves every arm that does not ask. `cmd_check_coverage` passes `building=staged`. Its loop already
skips a build whose findings are falsy, and with no INPROGRESS spec `graded` and `holding` stay 0,
so the count line prints byte for byte as the full read prints it. The plan's coverage read never
passes the keyword.

**What S4 does not check.** On the early path a failure of the history read is not reached, so a
git failure that exits 2 today exits 0 when no chain spec is INPROGRESS. `scan_carries` raises
nothing, and `read_design` and the status pass still run with their refusals.

### Documents

`tools/memory-tree/README.md` gains three sentences: the stamp beside the `--check --staged`
paragraph near line 602, the narrowed `build/` skip in the same paragraph, and the early exit in
the `--check-coverage` paragraph near line 372. `memory/HYGIENE.md` check 29 says the staged verb
runs on the render's trigger and otherwise holds, which stays true. No page under `help/` describes
check 9's or check 29's staged form: `grep -rln "render SKIPPED" help` finds none.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_render_key` | function | `tools/memory-tree/gen_build_index.py` |
| `resolve_render_stamp` | function | `tools/memory-tree/gen_build_index.py` |
| `read_record_head` | function | `tools/memory-tree/gen_build_index.py` |
| `gen-build-index-render-stamp` | git-dir file name | under `git rev-parse --git-path` |
| `read_carries_texts` | function | `tools/check-spec-tokens.py` |
| `building` | keyword | `derive_carries_coverage`, `read_carries_coverage` |

### The parity instrument

One scratch worktree, `%TEMP%/al1p`, two sides, one input tree. The builder scripts it and quotes
the script in the acceptance ledger.

1. `git worktree add --detach %TEMP%/al1p <tip>`. In it, blank `LIVE_LANDED_UNCLOSED` in
   `.memory-tree.conf`, run the tip's `gen_build_index.py --write`, and commit everything as P0.
   The Landed-unclosed column greps tracked source for ids, and the two sides' source differs in
   the ids its comments cite, so the column is held off on both. Its code is untouched here.
2. **Base side.** `git checkout 846d51d3 -- tools/memory-tree/gen_build_index.py
   tools/check-spec-tokens.py`, commit as Pb, run every scenario, `git reset --hard Pb` between
   scenarios.
3. **Tip side.** `git reset --hard P0`, run every scenario the same way.
4. Each scenario captures stdout and stderr merged, as check 9's `2>&1` does, the exit code, and
   the wall-clock time. `diff -r` over the two capture folders is the parity reading.

Pb touches no spec, so both sides read one spec history.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · `tools/check-spec-tokens.py` ·
`tools/memory-tree/README.md` · `memory/DECISIONS.md` (one row: the owner's override of `[class]`
for the S2 stamp, §8 F1)

### Alternatives rejected

- **S4 as written in the brief, an exit when no STAGED spec is an INPROGRESS chain spec.** A
  staged view row or carries-checker edit can turn an unstaged INPROGRESS spec's build red. Today
  that refuses. The brief's form would hold it, a verdict moved. Reading every chain spec's status
  costs 1.3 s and decides the same case without that hole.
- **S3 by narrowing `check_index_input` itself.** That predicate reads paths only, and the head
  comparison needs blobs. It is also check 29's and check 30's trigger, and check 30 must keep
  firing on a deviation record.
- **S2's key from `tools/run-gates/gate-fingerprint.sh`.** It digests `HEAD^{tree}`, which loses
  the commit the spec history hangs from, and its porcelain moves on `git add`. It also sits in the
  run-gates kit, which a memory-tree adopter may not install.

## 5. Production-readiness checklist

- security — N/A: no new write path outside the repository's git directory, no input from outside
  the tree, and the stamp holds one hex digest.
- perf / scale — the point of the unit. S2's key costs four git calls and a hash of the files that
  differ from HEAD; S1's skip keeps git's stat cache valid, so those calls stay cheap.
- error / empty / loading states — a git failure in the key derives empty, and an empty key is
  never stamped or matched. An empty chain population prints today's zero count line.
- observability — the stamp hit prints one named line. The early exit prints the same count line
  as the full read, so only AC10's timing shows it fired.
- risks — S2 trades the commit hook's fixed-point check for the push boundary's, the trade the
  owner took at §8 F1. The `build-index selftest` budget row in
  `tools/run-gates/selftest-budgets.txt` may need a re-measure once the arms land.
- testing — the arms of §7, each observed red then green at the close, and the parity instrument.
- migration — N/A: a stamp left by an older `--write` cannot exist, and a missing stamp is a miss.
- user docs — `tools/memory-tree/README.md` (S5). No `help/` page covers these verbs.

## 6. Acceptance criteria

- **AC1** — When the tip side runs `gen_build_index.py --write` twice on P0, touching a marker
  file between the runs, `find memory -type f -newer <marker>` prints nothing after the second
  run. On the base side the same probe lists every artifact.
  Red when: `write_text` opens an unchanged artifact for writing.
- **AC2** — When both sides run `gen_build_index.py --write` and then `git status --porcelain`,
  and then `gen_build_index.py --check`, `diff -r` over the two capture folders is empty and both
  porcelain readings are empty.
  Red when: any rendered byte, printed line or exit code differs between the sides.
- **AC3** — When the tip side edits one line of a spec body, runs `git add`, then
  `gen_build_index.py --write`, then `git add -u`, then `gen_build_index.py --check --staged`, the
  last prints the `render answered by the stamp` line and exits 0, and the base side's full check
  exits 0. Neither capture holds a line opening `build-index: render SKIPPED`.
  Red when: the key moves on `git add -u`, or the stamp line opens with the SKIPPED prefix.
- **AC4** — When the tip side repeats AC3 and edits one more working-tree byte before the staged
  check, and again when a committed text file under `memory/ledger/` that is no month shard makes
  `--write` warn of an unmanaged file, `gen_build_index.py --check --staged` prints no stamp line, and each capture and exit code
  equals the base side's.
  Red when: a stale key, or a `--write` whose check would be red, still answers from the stamp.
- **AC5** — When both sides append a line citing no id to
  `memory/builds/aLightenedLoop/build/2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md`, stage
  it and run `gen_build_index.py --check --staged`, both exit 0, the tip prints
  `render SKIPPED under --staged` naming one build record whose binding head is unchanged, and the
  base prints the `render owed` line.
  Red when: the tip renders, or either side exits non-zero.
- **AC6** — When both sides stage, one at a time, a changed `**Serves:**` line in that record, a
  body edit to `memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-1-deviation-11.md`,
  an appended line in `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`,
  and an appended id in the analysis record, then run `gen_build_index.py --check --staged`, every
  capture prints the `render owed` line on both sides and each pair diffs empty. A fifth staging,
  the quiet append of AC5 together with a hand edit inside a generated region of
  `memory/builds/aQueuedIndex/README.md`, a path git lists after the record, exits 1 on both sides
  with identical captures, the owed line naming the analysis record as today.
  Red when: any of the four skips on the tip, or the fifth names another path or another reason.
- **AC7** — When both sides stage the analysis record's appended line and run
  `gen_build_index.py --check-coverage --staged`, the two captures are byte-identical with exit 0,
  and a probe `python -B -c` calling `derive_carries_coverage(root, conf=conf, building=True)` on
  the tip returns a value whose every build carries `findings` of `None`.
  Red when: the count line differs, or the probe's value carries findings lists.
- **AC8** — When both sides flip a DEFERRED spec of a build the design view names, such as
  `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-1.md`, to
  INPROGRESS, stage it and run `gen_build_index.py --check-coverage --staged`, the two captures and
  exit codes are identical, and the tip's probe of AC7 returns findings lists.
  Red when: the early exit fires while a chain spec stands at INPROGRESS.
- **AC9** — When `grep -n "render answered by the stamp\|build/ folder\|no chain spec stands at INPROGRESS" tools/memory-tree/README.md`
  runs, it prints one line for each of the three phrases.
  Red when: a phrase is missing from the kit README.
- **AC10** — When the instrument times AC1's second `--write`, AC3's staged check, AC5's staged
  check and AC7's coverage check on both sides, the acceptance ledger records each pair of
  wall-clock seconds beside the instrument's commands, and each tip reading is below its base
  reading.
  Red when: a tip reading is not below its base, or a pair is missing.
  figure: PINNED, measured at observation on node `a` with both sides in one sitting.
  cost: about four full renders per side, several minutes.

## 7. Gates

`build-index selftest` · `memory-hygiene self-test` · `tier2-review self-test` · `policy fixtures` · `recall floor` · `recall floor arms`

New arm: `tools/memory-tree/gen_build_index.py --selftest` · covers AC1 · `write_text` over identical bytes keeps an `os.utime`-aged mtime, and different bytes move it · none
New arm: `tools/memory-tree/gen_build_index.py --selftest` · covers AC3 AC4 · a fixture repo where `--write`, `git add -u` and `--check --staged` answer from the stamp, and one more edit renders · none
New arm: `tools/memory-tree/gen_build_index.py --selftest` · covers AC5 AC6 · `test_staged_render` stages a no-id append under `build/` and sees a skip, then a head edit, a deviation record and a `DESIGN_VIEW`-folder file each see a render · none
New arm: `tools/check-spec-tokens.test.sh` · covers AC7 AC8 · a design fixture from `design_lib.write_design_fixture` with no INPROGRESS spec returns `findings` of `None` under `building=True`, and one INPROGRESS spec returns the full value · none

## 8. Open questions

- **F1 — Does `--check --staged` answer from a stamp that `--write` left?** The brief asks for "an
  input-hash cache [that] lets `--check` right after `--write` answer without a re-render". Any
  such cache is written by `--write` and read by `--check`, a guard sharing state with what it
  guards. The charter's `[class]` rule forbids that, and only the owner overrides a charter rule.
  - **A — the stamp of §4 S2, under `--staged` only.** The hook's render on a spec commit, about
    70 s, becomes four git calls. A render that is not a fixed point is caught at the push
    boundary instead of at the commit, the trade the staged skip already makes for unrendered
    paths. Needs the owner's override of `[class]`, recorded in `memory/DECISIONS.md`.
  - **B — a stamp only a full `--check` leaves.** No shared state with `--write`, but the hook's
    check is the first check after `--write`, so the measured case never hits.
  - **C — no cache in this unit.** S2, AC3, AC4 and their arm leave the spec at a rev bump. S1,
    S3 and S4 still remove the records-only commit's cost. Spec commits keep their second render.
  Recommendation: A, because the owner chose the cache at kickoff and the push boundary bounds
  the trade. C if the override is declined.
  - RESOLVED (owner, 2026-11-14): A, the stamp of §4 S2, consulted under `--check --staged` only.
    The owner's override of `[class]` is recorded at
    `memory/builds/aLightenedLoop/build/2026-11-14-build-TOOL-aLightenedLoop-1-override-1.md`,
    and its `memory/DECISIONS.md` row stays in §4's files touched.

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.
- rev-2 · 2026-11-14 · §2 S2 · §4 S2 · §4 files touched · §5 · §6 AC3 AC4 · §8 F1 · folded the owner's
  answer to F1 (option A) per `2026-11-14-prompt-TOOL-aLightenedLoop-1-fork-fold` and the override
  record `2026-11-14-build-TOOL-aLightenedLoop-1-override-1`; the gating notes on S2, AC3 and AC4 are
  dropped, and the header carries `ratified 2026-11-14`.

## 10. Reuse audit

The seams extended are `tools/memory-tree/gen_build_index.py#check_staged_render`, the staged
classifier TOOL-aTrimmedHook-1 built, for S3; `tools/memory-tree/gen_build_index.py#write_text`
for S1; and `tools/check-spec-tokens.py#derive_carries_coverage` with `read_carries_specs` for S4.
For S2 no existing seam fits. `tools/codebase-map/reuse_lookup.py` on "cache a render keyed by a
digest of the working tree" named `digest` in `tools/run-gates/gate-fingerprint.sh`, rejected in
§4 "Alternatives rejected": it digests the tree, not the commit, moves on `git add`, and lives in
another kit. On "skip rewriting a generated file whose bytes did not change" it named
`write_file` in `tools/memory-tree/migrate_backlog.py`, which writes unconditionally, so it is no
seam. The recall query returned TOOL-aTrimmedHook-1 and TOOL-aTrimmedHook-4, the classifier's
origin and its `GIT_INDEX_FILE` carry, both read and both still current at `846d51d3`.

Recall terms used: `python tools/memory-recall/query.py "skip an unchanged write and hold the staged index render for a records edit" --terms "gen_build_index write_text check_staged_render check_index_input staged skip render owed check 9 check 29 coverage held"`
