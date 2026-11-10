# TOOL-aSmoothedDispatch-21 — the reconcile merge with aSwiftRefusal on local main: one spec-token check, through `run_spec_token_check`, after every cheap refusal

**Status:** SPECCED · rev-1 · 2026-11-11 · node a · Tier-2 · base b904a0f9 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-21-reconcile.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-21-reconcile.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The owner said "Land both together" on 2026-11-10. aSwiftRefusal sits merged and unpushed on local
`main` at `b904a0f91`, and both builds rewrote `--dispatch`'s spec-token check in
`tools/unattended/unattended.sh`. This unit makes the `--no-ff` merge of `b904a0f91` into
`branch/aSmoothedDispatch` with both builds' behaviour intact: the check runs once, through this
build's scoped and cached `run_spec_token_check`, at aSwiftRefusal's position after every cheap
refusal and before the claim read. Cross-stream merge, so Tier-2 (`memory/TEMPLATE-SPEC.md`, "Tiers").

## 2. Scope (IN)

The conflict set is the trial merge `git merge-tree --write-tree HEAD b904a0f91` run at `440c2994e`
while this spec was written, tree `f8905038`. The merge base is `ae6735c1`. Every line number below
cited as "trial" is in that tree. The builder re-takes the conflict set at the merge and records any
difference in the acceptance ledger.

| File | Hunks | Kind |
|---|---|---|
| `tools/unattended/unattended.sh` | 1 | product |
| `tools/unattended/unattended.test.sh` | 2 | suite |
| `tools/unattended/unarmed-branches.txt` | 1 | pin |
| `tools/unattended/VERBS.template.md` | 1 | doc template |
| `memory/guides/UNATTENDED-VERBS.md` | 1 | rendered copy |
| `memory/project/readme-contract.txt` | 1 | record |

- **S1** — The merge. `git merge --no-ff --no-commit b904a0f91` on the run branch, the sha and never
  the moving name `main`. The merge commit has two parents, the branch's pre-merge tip and
  `b904a0f91`, and no conflict marker survives in any of the six files. Every file git auto-merged
  is carried as git merged it, except the generated outputs S7 re-renders. Observed by AC1, AC2
  and AC9.
- **S2** — The driver. The one conflict hunk (trial `tools/unattended/unattended.sh:14456-14460`)
  resolves to neither side: this build's early `run_spec_token_check "$slug" || return 1` is not
  kept there. aSwiftRefusal's inline `if [ -n "${SPEC_TOKENS_CLI:-}" ]` … `fi` block below
  condition 1 (trial `tools/unattended/unattended.sh:14785-14801`) gives its place to that one call.
  The call-site comment is §4's. No refusal message changes, and no refusal is added or lost.
  Observed by AC3 and AC4.
- **S3** — The driver suite. Both builds' arms are kept. This build's unit 4 and unit 8 cache and
  verdict arms are re-fixtured as §4 states, because under aSwiftRefusal's order a glob `--writes`
  path is refused before the check is reached. `FLOOR_ASSERTIONS`, `FLOOR_SHARD_3` and
  `FLOOR_SHARD_4` carry both sides' raises and both sides' comment lines, plus one `MERGED` line
  each. Observed by AC6.
- **S4** — The pin file. Every `unattended.sh` row of `tools/unattended/unarmed-branches.txt` is
  keyed to the ordinal it takes in the merged driver, and one `RE-KEYED` comment names this unit.
  Observed by AC5.
- **S5** — The verbs guide. One paragraph in `tools/unattended/VERBS.template.md` states both
  behaviours and why, and `memory/guides/UNATTENDED-VERBS.md` is re-rendered from it by the kit's
  adopter, never by hand. Observed by AC7.
- **S6** — The README contract. `memory/project/readme-contract.txt` keeps both sides' rows: this
  build's README beside aSwiftRefusal's and aProfiledEffort's. Observed by AC8.
- **S7** — Generated outputs. The build index, LIVE, the ledger and `memory/map/generated/symbols.json`
  are re-rendered by their generators after the hand-resolved sources are staged, never hand-merged.
  Observed by AC9.

## 3. Non-goals (OUT)

- Any change to what either build's refusals decide, or to their messages.
- The inherited driver-suite reds filed as asks `TOOL-aSmoothedDispatch-10` to
  `TOOL-aSmoothedDispatch-13`.
- Pushing, and the `--no-ff` merge of this branch into `main`. Both are the main loop's.
- A kit version mint. Local `main` carries `KIT_UNATTENDED_VERSION=1.116`, which the merge takes
  as git merged it; the lander's `mint` moves it past this build's bytes.
- Re-deriving local `main`'s own records, decisions or backlog rows. They arrive as written.
- A contradiction between the two sides that keeping both cannot resolve is not decided here. The
  pass runs `git merge --abort`, leaves the branch at its pre-merge tip, and returns the hunk and
  both sides' intent to the owner.

### Edges

- **consumes-from** external — local `main` at `b904a0f91`, carrying aSwiftRefusal and
  aProfiledEffort merged and unpushed. If `git rev-parse main` reads another sha when the pass
  starts, the pass still merges `b904a0f91` and records the moved sha in the ledger.

## 4. Design

### Why the two sides conflict, read at `440c2994e` and `b904a0f91`

- This build (unit 4) moved the inline block into `run_spec_token_check`, defined above
  `verb_dispatch` (`tools/unattended/unattended.sh:14367` at `440c2994e`), and called it right after
  the THIN refusal (`tools/unattended/unattended.sh:14438` at `440c2994e`). The function scopes the
  verdict through `check_spec_token_hits` and caches through `derive_spec_token_key`.
- aSwiftRefusal (unit 1) moved the same inline block below condition 1
  (`tools/unattended/unattended.sh:14633-14665` at `b904a0f91`), so every refusal decided from the
  run-state file, the spec headers or `git` answers before the tree-wide scan.
- At the merge, git puts this build's early call in conflict against nothing, and auto-merges
  aSwiftRefusal's inline block in below condition 1. Left alone, that is two checks, one of them
  unscoped and uncached.

### S2 — the driver resolution

1. The conflict hunk resolves to no lines: neither the early call nor its one-line comment is kept.
2. The inline block at trial `tools/unattended/unattended.sh:14785-14801` gives its place to the one
   line `  run_spec_token_check "$slug" || return 1`.
3. The comment above it (trial `tools/unattended/unattended.sh:14769-14784`) keeps its first line,
   the `aDeferredBar closing review F3 (unit 2)` rule, then one pointer line and aSwiftRefusal's own
   three lines, verbatim:

```bash
  # ------------------------------------------------- aDeferredBar closing review F3 (unit 2)
  # THE SPEC-TOKEN CHECK, `run_spec_token_check`: its header says what it runs, scopes and caches.
  # IT RUNS LAST AMONG THE LOCAL REFUSALS (TOOL-aSwiftRefusal-1): it is the one that costs a tree-wide
  # scan, and every refusal above it is decided from the run-state file, the spec headers or `git` in
  # seconds, so an out-of-order or overlapping dispatch is refused before the checker runs at all.
  run_spec_token_check "$slug" || return 1
```

The rest of that comment, the live-spec rationale and the launcher note, already sits in the
function's header (trial `tools/unattended/unattended.sh:14366-14378`). Keeping a second copy at the
call site is one fact in two places, so the call site points at it.

The trial resolution was simulated in scratch. The call lands at line 14780, after condition 1's
refusal at 14758 and before the claim read `check_claim_writable "$slug" holder "$_dk"` at 14811.
The merged driver then carries 319 `fail` call sites, the same multiset of `(check, message)` pairs
as this branch's tip. A second copy of the inline block would add three.

### S3 — the suite resolution and the re-fixtured arms

**Floors.** Both sides raised the same three floors from the merge base. The merged block carries
both sides' `RAISED` lines in date order, this build's then aSwiftRefusal's, and then one line per
floor in the shape of the region-five precedent above `FLOOR_SHARD_5`:
`# MERGED at TOOL-aSmoothedDispatch-21's reconcile: the base <b>, plus <ours>, plus <theirs> = <sum>.`

| floor | base `ae6735c1` | this build | aSwiftRefusal | merged |
|---|---|---|---|---|
| `FLOOR_ASSERTIONS` | 3256 | +42 (3298) | +31 (3287) | 3329 |
| `FLOOR_SHARD_3` | 405 | +29 (434) | +11 (416) | 445 |
| `FLOOR_SHARD_4` | 383 | +7 (390) | +20 (403) | 410 |

The merged figures are DERIVED from the six values above, read at the two parents. The builder
recounts the re-fixtured block off its own lines. The re-fixture below keeps every assertion line,
so the recount should agree; if it does not, the counted value wins and the `MERGED` line says why.

**The arms aSwiftRefusal's order now answers differently.** The unit 4 and unit 8 block (trial
`tools/unattended/unattended.test.sh:7646-7754`) makes 14 calls of
`run --dispatch tRun --pass ARCH-tRun-1 --writes "${PFX}*.sh"`. Each relied on the glob refusal
running AFTER the spec-token check, so the checker ran and no row was written. In the merged driver
the glob refusal (trial `tools/unattended/unattended.sh:14632`) runs before the call at 14780, so
none of those 14 calls reaches the checker. Every admit, skip, cache-off and refuse assertion on
their output would read red. The assertions stay as written, and only their producers move:

| step | assertions on the output | producer in the merged suite |
|---|---|---|
| cache step a, both calls | admit, skip, `miss "spec-tokens: "` | `o=$( ( load_driver_conf && run_spec_token_check tRun ) 2>&1 )` |
| cache step a, both glob `hit`s | the glob refusal | the glob dispatch, kept for those two lines only |
| cache steps b and c | admit, no skip | the in-process form |
| cache step d, the tRun re-record | none | the in-process form, output discarded |
| cache step e, both calls | refuse, no skip | `run --dispatch tRun --pass ARCH-tRun-1 --writes ${PFX}a.sh` |
| cache step f, both calls | cache off | the in-process form |
| the five verdict arms of unit 8 | refuse | `run --dispatch tRun --pass ARCH-tRun-1 --writes ${PFX}a.sh` |

The in-process form is step d's own (trial `tools/unattended/unattended.test.sh:7700`), there because a
second dispatch would need its own run-state file. It reaches the function directly and writes no
row, so the tree does not move between two calls. A declared dispatch cannot stand in for it: the
row it writes moves the run-state file, which moves the fingerprint, so the next call never skips.

A refusing arm dispatches the declarable path `${PFX}a.sh` instead, so it stays a dispatch-level
observation. Every cheap refusal admits that path, because the blank-key arm above already declared
ARCH-tRun-1 with it and a unit's own rows are not siblings. The checker then refuses, and a refusal
writes no row. The `rm -f` key lines before each verdict arm stay.

Two header comments state the old order and are reworded. The block header's sentence "The two glob
`--writes` calls are refused by a check that runs AFTER the spec-token one" becomes: the cache steps
call `run_spec_token_check` in process, because every refusal that writes no row now precedes the
check (TOOL-aSwiftRefusal-1), and step a's glob dispatch is kept for its glob assertions. The unit 8
S3 header's "dispatches a glob the check after the spec-token one refuses, so no row is written"
becomes: dispatches the declared path, which every cheap refusal admits, and the checker's refusal
writes no row.

aSwiftRefusal's own arms (trial `tools/unattended/unattended.test.sh:7770-7801`) meet this build's
function unchanged. Their stub exits 1 and prints nothing, so `check_spec_token_hits` finds no
summary line and refuses with the same check-49 text the L1 positive control asserts. A refusal
records no key, so the cache cannot stand in for that run.

### S4 — the pin file

The conflict hunk holds both sides' `RE-KEYED` history and each side's resolver row. The merged file
keeps both history comments and adds one, with no `<<<<<<<` side left. The new comment says that at
TOOL-aSmoothedDispatch-21's reconcile the three spec-token refusals sit in `run_spec_token_check`
above `verb_dispatch` again. So the resolver reads 38 -> 15, and the sibling malformed-order row,
which auto-merged at aSwiftRefusal's 18, reads 18 -> 21. The order-gate row stays out, armed by
TOOL-aSwiftRefusal-1.

| signature, leading words | ordinal in the merged driver |
|---|---|
| `cannot hash the brief, so the row would carry no join` | 8 |
| `--dispatch: the inline resolver found no usable python` | 15 |
| `a sibling spec status header carries something shaped like the build-order verb` | 21 |

These ordinals were DERIVED while this spec was written, by loading `branches()` from
`tools/memory-tree/check-arms.py` by path over the simulated resolution. AC5 re-derives them from the
merged source.

### S5 — the verbs paragraph

The conflict region in `tools/unattended/VERBS.template.md` (trial lines 237-253) resolves to the
text below. It keeps aSwiftRefusal's ordering sentence and reason, keeps this build's scoping and
cache sentences, and leaves out aSwiftRefusal's "refuses the dispatch when it exits non-zero", which
the scoped verdict makes false. The three phrases AC7 greps each stay on one line.

```text
  its subject, and `Pass: none` names no unit. After every cheap refusal and before the claim read it runs the DECLARED spec-token checker, `SPEC_TOKENS_CLI`, over the
  live tree: the checker's bar join grades LIVE specs, an unattended build closes each unit spec in its
  own build commit, and this verb is the one point that sees a spec before its unit builds. It runs
  last because it costs a tree-wide scan, and every refusal above it — the order gate, the edge and
  hold gates, the path and shared-record refusals, condition 1 — is decided from the run-state file,
  the spec headers or `git` in seconds. It refuses on any red but a hit in another build's spec,
  which it notes and admits, because the bar's whole-tree leg still grades that build.
  It skips the run when its inputs match the last check it admitted for this build, keyed on the
  slug, the checker, the launcher, HEAD and the run-gates working-tree fingerprint, recorded under
  the sidecar root; with no fingerprint it announces that the cache is off and runs the checker. A blank or absent key is an ANNOUNCED skip on stdout,
```

Then `bash tools/unattended/adopt-unattended.sh`, no flag, from the repo root. Its verb-carrier step
(`tools/unattended/adopt-unattended.sh:1074-1076`) rewrites `memory/guides/UNATTENDED-VERBS.md`
from the template whenever the two differ. The guide's own conflict markers are overwritten by that
render and are never hand-resolved. The template's marker line reads `unattended@1.116` at the
merge, and the render carries it. Any other file the adopter writes is listed in the ledger.

### S6 and S7

`memory/project/readme-contract.txt` (trial lines 229-234) keeps all three rows, in the order
`aSmoothedDispatch`, `aSwiftRefusal`, `aProfiledEffort`.

After S2 to S6 are staged: `python tools/memory-tree/gen_build_index.py --write`, then
`python tools/codebase-map/gen_map.py --write`, and stage what they change. This clone has the
`merge=rows` driver wired: the trial merge printed its `merge-rows:` line, clean.

### The commits

The shape follows `TOOL-aSparedSpawn-34` and the merge `2c2715fdd`. The merge commit's subject is
`merge: local main b904a0f91 into aSmoothedDispatch — TOOL-aSmoothedDispatch-21, one spec-token check after every cheap refusal`.
Its body names each conflicted file's resolution, and its trailer is `Pass: none`, because a
merge's index holds every path local `main` moved. A pass commit follows it, trailer
`Pass: TOOL-aSmoothedDispatch-21`, carrying this spec's CLOSED header, the acceptance ledger and
the index re-render.

### The fail-site probe, `$SCRATCH/sd21-fails.py`

`$SCRATCH` is the run's scratch directory. Run it from the repository root with the merge commit's
sha as its one argument.

```python
import re, subprocess, sys
from collections import Counter
def sites(rev):
    t = subprocess.run(["git", "show", f"{rev}:tools/unattended/unattended.sh"],
                       capture_output=True, text=True, encoding="utf-8", check=True).stdout
    c = Counter()
    for l in t.split("\n"):
        if l.lstrip().startswith("#") or "fail() {" in l:
            continue
        m = re.search(r'\bfail (\d+) (".*)', l)
        if m:
            c[(m.group(1), m.group(2))] += 1
    return c
a, b = sites(sys.argv[1] + "^1"), sites(sys.argv[1])
print("first-parent", sum(a.values()), "merged", sum(b.values()),
      "lost", sum((a - b).values()), "added", sum((b - a).values()))
```

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/unarmed-branches.txt`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/project/readme-contract.txt`
- `memory/builds/aSmoothedDispatch/README.md`
- `memory/LIVE.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Keep this build's early call and let aSwiftRefusal's move go.** It undoes TOOL-aSwiftRefusal-1,
  and the owner asked for both builds to land.
- **Keep aSwiftRefusal's inline block and let the function go.** It undoes unit 4's scope and cache.
- **Inline the function's body at aSwiftRefusal's position.** Two homes for one check. Unit 4's
  AC8 grep for one call and one `run_bounded` line would read the copy.
- **Re-fixture the cache arms onto a refusal that follows the check.** The only one is the claim
  read's check 108, which needs `RUN_CLAIMS` on and a remote claim in the fixture. The in-process
  form is already in the block, at step d.
- **Let step a's two glob `hit`s go with their glob dispatch.** The glob refusal is armed elsewhere,
  but the brief forbids weakening an arm's assertions to fit, and the floors would fall by two.
- **Rebase the branch onto local `main`.** It rewrites the shas this build's ledgers and review
  records cite.

## 5. Production-readiness checklist

- security — both sides' refusals survive as one multiset, AC4's probe. The scoped verdict stays
  deny-by-default: only a counted red in a named other build is admitted.
- perf / scale — the check now runs after every cheap refusal, so a dispatch refused cheaply never
  pays the scan, and one that reaches it still gets unit 4's cache.
- error / empty / loading states — N/A: no new path. A blank `SPEC_TOKENS_CLI` is the function's
  announced skip, as on both sides.
- observability — the ledger records `main`'s sha at pass start, each file's resolution, the probe
  outputs and the adopter's writes.
- risks — a hunk resolved by picking a side silently loses a behaviour. AC3, AC4 and AC9 are the
  checks, and a contradiction aborts the merge rather than being decided in it.
- testing — the probes in §6 for the pass, and the driver suite's regions 2 to 4 at the close.
- migration — N/A: no record or schema moves.
- user docs — the verbs guide, S5. No `help/` page names `--dispatch`'s check order.

## 6. Acceptance criteria

- **AC1** — When `git rev-list --parents -n 1 <merge>` runs, it prints the merge sha, the branch's
  pre-merge tip and `b904a0f913957b13bfda3dc00e5d8f77bd3cffb7`.
  Red when: the merge is squashed, rebased or made from `main` after it moved, so a parent differs.
- **AC2** — When `grep -cE '^(<<<<<<<|>>>>>>>) |^=======$'` runs over each of the six conflicted
  files at the merge, each prints 0.
  Red when: a hunk is committed with its markers, as the trial tree carries 7 conflict regions.
- **AC3** — When these run over `tools/unattended/unattended.sh` at the merge, they print as stated.
  `grep -c 'run_spec_token_check "$slug"'` prints 1.
  `grep -c 'run_bounded "$_stpy" "$SPEC_TOKENS_CLI"'` prints 1.
  `grep -c 'if \[ -n "${SPEC_TOKENS_CLI:-}" \]'` prints 0.
  `grep -nF` for `run_spec_token_check "$slug" || return 1`, for
  `two passes claiming one file are not disjoint: $p also in` and for
  `check_claim_writable "$slug" holder "$_dk"` puts the call's line after the second and before the
  third.
  `grep -B6 -F 'run_spec_token_check "$slug" || return 1'` piped to
  `grep -c 'IT RUNS LAST AMONG THE LOCAL REFUSALS (TOOL-aSwiftRefusal-1)'` prints 1.
  `bash -n tools/unattended/unattended.sh` exits 0, and so does `bash -n` over the driver suite file.
  Red when: the early call is kept, so the first grep prints 2 and the order fails, or the inline
  block is kept, so the second prints 2.
- **AC4** — When `python "$SCRATCH/sd21-fails.py" <merge>` runs, it prints equal first-parent and
  merged counts and `lost 0 added 0`.
  Red when: the inline block is kept beside the function, so `added 3`, or a resolution loses a
  refusal.
  figure: the counts are DERIVED at observation; 319 was measured on the simulated resolution.
- **AC5** — When the `branches()` probe of TOOL-aSwiftRefusal-1's AC5 runs at the merge,
  ```
  python -c "import importlib.util as u;s=u.spec_from_file_location('a','tools/memory-tree/check-arms.py');m=u.module_from_spec(s);s.loader.exec_module(m);[print(b['ord'],b['sig'][:50]) for b in m.branches('.','tools/unattended/unattended.sh') if b['num']==49]"
  ```
  the brief-hash signature reads 8, the resolver's 15 and the sibling malformed-order 21.
  `grep -P '^unattended.sh\t49\t' tools/unattended/unarmed-branches.txt` prints exactly three rows,
  at those ordinals with those signatures, and none carrying `an earlier step still holds`.
  `grep -c 'RE-KEYED.*TOOL-aSmoothedDispatch-21' tools/unattended/unarmed-branches.txt` prints 1.
  Red when: a row keeps either side's ordinal, 18 or 38, or the order-gate row comes back.
  figure: the ordinals are DERIVED by the probe at observation; §4's table was measured on the
  simulated resolution.
- **AC6** — When these run over the driver suite file, the one both `New arm:` lines name, at the
  merge, they print as stated.
  `grep -cF 'run --dispatch tRun --pass ARCH-tRun-1 --writes "${PFX}*.sh"'` prints 2.
  `grep -cF '( load_driver_conf && run_spec_token_check tRun )'` prints 7.
  `grep -E '^FLOOR_ASSERTIONS=|^FLOOR_SHARD_3=|^FLOOR_SHARD_4='` prints `FLOOR_ASSERTIONS=3329`,
  `FLOOR_SHARD_3=445` and `FLOOR_SHARD_4=410`.
  `grep -c "MERGED at TOOL-aSmoothedDispatch-21's reconcile"` prints 3.
  `grep -c 'by TOOL-aSwiftRefusal-4'` and `grep -c 'by TOOL-aSmoothedDispatch-8 on 2026-11-10'`
  each print 3, one per floor, both sides' comment lines kept.
  Red when: a cache step still dispatches a glob, so the first count exceeds 2, or a floor takes
  one side's value, 3298 or 3287 say.
  figure: the floor values are DERIVED from both parents' floors as §4's table states; a recount that
  differs moves them by a rev of this spec.
- **AC7** — When these run at the merge, they print as stated.
  `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` prints nothing.
  Over `memory/guides/UNATTENDED-VERBS.md`, `grep -c 'After every cheap refusal and before the claim read'`,
  `grep -c 'skips the run when its inputs match'` and
  `grep -c "It refuses on any red but a hit in another build's spec"` each print 1, and
  `grep -c 'refuses the dispatch when it exits non-zero'` prints 0.
  Red when: one side's sentences are lost, the false non-zero sentence is kept, or the guide is
  hand-edited apart from the template.
- **AC8** — When `grep -cx` runs over `memory/project/readme-contract.txt` for each of the three
  build READMEs, each prints 1:
  `grep -cx memory/builds/aSmoothedDispatch/README.md memory/project/readme-contract.txt`,
  `grep -cx 'memory.builds.aSwiftRefusal.README.md' memory/project/readme-contract.txt` and
  `grep -cx 'memory.builds.aProfiledEffort.README.md' memory/project/readme-contract.txt`.
  The last two READMEs arrive with the merge, so their patterns spell each slash as a regex dot.
  Red when: a side's row is lost to the conflict.
- **AC9** — When `git merge-tree --write-tree <merge>^1 <merge>^2` is re-run and its first line,
  the tree `<trial>`, is compared by `git diff --name-only <trial> <merge> -- tools skills`, it lists
  only the driver `tools/unattended/unattended.sh`, its suite file,
  `tools/unattended/unarmed-branches.txt` and `tools/unattended/VERBS.template.md`. On the pass
  commit, `python tools/memory-tree/gen_build_index.py --write` then
  `python tools/codebase-map/gen_map.py --write` leave `git status --porcelain` empty.
  Red when: a product file git auto-merged is hand-edited, or a generated file is committed stale or
  hand-merged.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `scratch-guard self-test` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `shell hygiene (a location probe asked from a moved directory)` · `install-prefix (shipped surface)` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `codebase-map coverage + freshness` · `pass-order history` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/unattended/unattended.test.sh · covers AC6 · unit 4 and unit 8's cache steps a, b, c, d and f, moved to the in-process `run_spec_token_check tRun` form in region three; staged by deleting the key write in `run_spec_token_check`, which reds step a's skip `hit` · none, the floors move by the merge as AC6 states
New arm: tools/unattended/unattended.test.sh · covers AC6 · step e and unit 8's five verdict arms, moved to a `${PFX}a.sh` dispatch in region three; staged by making `check_spec_token_hits` return 0 on every input, which reds each refuse `hit` · none

The main loop also reads regions 2, 3 and 4 of the driver suite at the close, and they print no FAIL
line beyond the inherited ones filed as asks 10 to 13. The bar runs once after that, through the
lander. This spec's author ran no gate but `memory hygiene`, the lexicon and the spec-token
checker's one-spec mode over this file.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-11 · initial draft from brief `2026-11-10-prompt-TOOL-aSmoothedDispatch-21-reconcile`,
  grounded on the trial merge of `b904a0f91` into `440c2994e`. Item 1's "keep aSwiftRefusal's
  comment paragraph at the call site" is read as its own three `IT RUNS LAST` lines, with a pointer
  to the function header for the aDeferredBar text the header already carries. Item 2's example ran
  the other way: it is this build's cache arms that meet aSwiftRefusal's order, and §4 re-fixtures
  them.

## 10. Reuse audit

The seams this unit extends: `run_spec_token_check` (`tools/unattended/unattended.sh:14367` at
`440c2994e`), called once at aSwiftRefusal's position; the suite's in-process call form at cache step
d (trial `tools/unattended/unattended.test.sh:7700`); the adopter's verb-carrier install
(`tools/unattended/adopt-unattended.sh:1074-1076`); `branches()` in `tools/memory-tree/check-arms.py:244`
for the ordinals; and the reconcile shape of `TOOL-aSparedSpawn-34`, two-parent merge then pass
commit. `tools/codebase-map/reuse_lookup.py` ranked only generic name stems (`check`, `build`) for
"reconcile two builds that both moved the dispatch spec-token check into one call site", so no
existing code seam fits a merge, which is a git operation. Recall's hits were this unit's own brief,
the `[reconcile]` rule that a generated region is re-rendered and never merged (`PLAY-dClosedLoop-35`),
and the `merge=rows` driver records of `TOOL-dDerivedDocket-34`.

Recall terms used: `python tools/memory-recall/query.py "how was a reconcile merge of two builds that rewrote the same driver block recorded and specced" --terms "reconcile merge conflict driver dispatch spec-token floors re-keyed unarmed ordinals land both"`
