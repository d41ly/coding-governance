# TOOL-aGraftedHelix-27 — the driver resolves generated indexes the same inside a git hook as outside one, so a pass commits the index its generator rewrote

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-2 · base 5266d22e · streams tooling · order 4 · ratified 2026-10-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aGraftedHelix-27-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aGraftedHelix-27-1-spec-brief.md) | journal | TOOL-aGraftedHelix-28 |

<!-- /gen:spec-records -->

## 1. Goal

Inside a linked worktree's `commit-msg` hook, git exports an absolute `GIT_DIR`. The unattended
kit's library asks git where its own directory sits, gets the wrong answer, and so `--check-commit`
resolves no kit's `[[generated]]` outputs. A pass that edits a generator then cannot commit the
index it regenerated: `--check-commit` refuses the index as undeclared, and `--dispatch` refuses
declaring it beside its generator. Unit 3's pass hit exactly that, and its acceptance ledger records
the index riding a later records commit. This unit derives the kit's place by the logical walk the
kits already share. A hook, a shell and a junctioned install then resolve one set, and a class record
carries the defect's shape to every probe this unit does not reach.

## 2. Scope (IN)

- **S1** — `tools/unattended/lib-unattended.sh` carries the `derive_self_rel` block of
  `tools/lib/kit-rel.sh` inline, byte-identical between its `# >>>` and `# <<<` marker lines, as
  every shipped suite already does. Observed by AC5.
- **S2** — `resolve_generated_indexes` derives its kit directory's repository-relative path with
  `derive_self_rel`, and asks git nothing to do it. The tool root it takes from that path, the
  `kit.toml` glob and everything after the glob are unchanged. Observed by AC1 and AC2.
- **S3** — `check_commit_message` in `tools/unattended/unattended.sh` derives the kit path its
  printed `--dispatch` remedy names with the same function. Its fallback to `$KIT_DIR`, for a walk
  that finds no repository, stays. Observed by AC1.
- **S4** — When `derive_self_rel` finds no repository above the library's directory,
  `resolve_generated_indexes` prints one stderr line naming that directory and saying only the
  repository-root kits and the conf pairs were read, then proceeds exactly as it does today.
  Observed by AC3.
- **S5** — `--check-commit` admits a generated output a kit declares when it is staged beside its
  generator in the commit of the pass that declared that generator, under the hook as in a shell.
  The subtraction that admits it is unchanged (§8 F1). Observed by AC1.
- **S6** — Check 49 in `--dispatch` is unchanged. It still refuses one declaration, and two open
  sibling declarations, that name a generated index together with its generator (§8 F2). Observed
  by AC4.
- **S7** — Three arms in the driver's self-test: the hook-shaped commit, the junctioned kit and the
  announcement. A pass observes each as a slice. Observed by AC1, AC2 and AC3.
- **S8** — The sweep of the kit's location probes in §4, each one fixed or left with its reason. One
  `class` record in the bug-class catalogue, anchored on the two fixed files, the reference hook and
  the probes left. Its basename is a new map key in the unattended-mandate dossier, and the
  catalogue index and the map are re-rendered. Observed by AC6 and AC7.
- **S9** — The unattended kit version, bumped once after the last move, in every carrier
  `tools/check-kit-versions.sh` enumerates. Observed by AC8.
- **S10** — The pass's own build commit carries the index it regenerated, through this run's own
  `commit-msg` hook. Observed by AC9.

## 3. Non-goals (OUT)

- No edit to `.githooks/commit-msg`. The kit README has every adopter wire `--check-commit` into
  its own hook, so a fix in gov's hook reaches gov alone.
- No scrub of `GIT_INDEX_FILE` anywhere. On a partial commit git points it at a `next-index` lock
  file, and `--check-commit` must grade the index the commit records (§4, measured).
- No change to check 49, to the subtraction set `--check-commit` shares with check 23, or to which
  paths count as generated (§8 F1 and F2).
- No fix to the three probes §4 leaves. None of them runs under a git hook, and each is named with
  the answer it would give under one.
- No class gate over the repository's other `git -C <dir> rev-parse --show-...` probes. The §4
  predicate finds 26 lines across the tree, and a gate over them is a mechanism of its own (M2).
- No change to the canonical `derive_self_rel` in `tools/lib/kit-rel.sh`. Its per-level forks are
  its cost (§5), and changing the block moves every byte-identical copy at once.
- No edit to the unattended protocol, verbs or stops templates beyond their version marker line
  (shared invariant 10, §8 F3). The verbs template already says the generated outputs are
  subtracted, which this unit makes true under a hook.

### Edges

- **consumes-from** external — git exporting an absolute `GIT_DIR` and `GIT_INDEX_FILE` into a
  linked worktree's `commit-msg` hook, and no `GIT_DIR` into a primary tree's, measured on git
  2.54.0.windows.1. This unit builds neither, and its hook-shaped arm announces itself when git
  exports no `GIT_DIR`.
- **hands-off** external — a class gate over the location probes outside this driver: 22 unscrubbed
  code lines tree-wide at `f0971667`, 20 of them after this unit. It is its own mechanism, so this
  run's orchestrator adopts it as a unit or parks it.

## 4. Design

### The defect, measured

`resolve_generated_indexes` computes `_rg_here` from `BASH_SOURCE`, then asks
`git -C "$_rg_here" rev-parse --show-prefix` for the kit's repository-relative path. It cuts the
tool root from that path and globs `<tool root>/*/kit.toml` in the repository root. With `GIT_DIR`
set and `GIT_WORK_TREE` unset, git takes the current directory as the work tree's top, so `-C` into
the kit directory answers an empty prefix. The tool root is then empty, the glob `*/kit.toml` matches
no prefixed kit, and only the conf pairs survive. `.unattended.conf` here declares
`GENERATED_INDEXES=""`, so under the hook gov resolves no generated output at all.

Measured on node `a`, 2026-10-05, at `f0971667`, PINNED:

| environment | `resolve_generated_indexes "$ROOT" "" memory` |
|---|---|
| a shell in this worktree | six pairs, `memory/gotchas/INDEX.md:tools/memory-tree/gotchas.py` among them |
| the same, `GIT_DIR` exported to the worktree's absolute git dir | empty |

The hook environment itself, measured in a fixture repository with a `commit-msg` hook that printed
its `GIT_*` variables. A primary tree's hook got `GIT_INDEX_FILE=.git/index` and no `GIT_DIR`. A
linked worktree's hook got `GIT_DIR=<common dir>/worktrees/<name>` and an absolute
`GIT_INDEX_FILE`, both absolute. On `git commit -- <path>` that index was
`<worktree git dir>/next-index-<pid>.lock`, while a second path stayed staged in the real index. So
the defect bites a LINKED worktree only, which is where every unattended run commits, and only at a
prefixed install: at a root install the kit's prefix has no slash, the tool root is empty in both
environments, and the glob is `*/kit.toml` either way.

The same probe feeds the remedy text. `check_commit_message` asks
`git -C "$KIT_DIR" rev-parse --show-prefix` for the path its printed `--dispatch` names. Read-only
on this worktree with `GIT_DIR` exported, `--check-commit` over a message whose trailer names a unit
with no open dispatch printed `declare it first: bash /c/projects/...` where a shell prints
`bash tools/unattended/unattended.sh`.

### The mechanism

`derive_self_rel` walks up from a directory's LOGICAL path to the first ancestor holding a `.git`
entry, file or directory, and prints the walked path. It asks git nothing, so no inherited variable
reaches it. `tools/lib/kit-rel.sh` is its canonical copy, and the walk is the one the unattended
adopter, `check-wiring.sh` and every shipped suite already carry. Its header records the junction
contract: a kit directory that is a junction inside the adopting repository anchors to the ADOPTING
repository, while git answers with the junction's target.

The library carries the block inline, between the markers and byte-identical, because a
copy-installed kit cannot source `<prefix>/lib/`. The python-resolver leg's parity row finds copies
by `git grep -l '^# >>> derive_self_rel'` over tracked `*.sh`, so the library joins that population
with no edit to the leg. The suites that already define the function and then source the library
define it twice with identical bytes, which is harmless.

`resolve_generated_indexes` calls it on the library's own directory. A non-empty answer feeds the
existing tool-root cut unchanged, with no trailing slash to strip. `check_commit_message` calls it on
`$KIT_DIR` and keeps its `$KIT_DIR` fallback for an empty answer.

### The announcement

`derive_self_rel` returns 1 when the walk reaches the filesystem root with no `.git` on the way.
That is the one state in which the resolver cannot know its tool root, so S4 announces it on stderr
and proceeds with today's empty tool root. It is a note and not a refusal. Under `--check-commit` a
dead probe already fails closed, because unresolved outputs are refused as undeclared writes, so a
refusal would add nothing but a second message.

What it does not check: a kit directory that IS a repository root returns 0 with an empty path,
which `tools/lib/kit-rel.sh` defines as legal. That layout keeps today's root glob silently, because
no supported install produces it.

### Admission and check 49

The subtraction in `check_commit_message` admits any staged path a resolved `[[generated]]` row
covers. Check 23 subtracts the same set at the close, through the same resolver. Once the resolver
answers under the hook, a pass that declared `tools/memory-tree/gotchas.py` and staged
`memory/gotchas/INDEX.md` beside it commits both, and nothing in either verb changes (§8 F1). A pass
therefore never needs to declare a generated output, so check 49's refusal of an index declared
beside its generator, in one declaration or across two open siblings, costs nothing and stays (§8 F2).

### The hook-shaped arm

The arm sits beside the `--check-commit` arms in the driver's self-test and reuses
`build_check_commit_fixture`. It writes a fixture kit under `${PFX}` whose `kit.toml` declares one
`[[generated]]` row, an output under the memory root from a generator in that kit, and commits it.
The primary tree leaves the run's branch, and the arm checks that branch out in a linked worktree at
a short path under the system temp directory. An open pass declares the fixture generator alone.
`core.hooksPath` names a hook directory whose `commit-msg` records whether `GIT_DIR` was set and runs
the driver's `--check-commit "$1"`.

A real `git commit`, with no `--no-verify`, then stages the edited generator and the output with a
`Pass:` trailer naming the pass. The arm asserts the commit landed, that `git show --stat` of it
lists both paths, and that the hook saw `GIT_DIR`. A second commit stages an undeclared path. The arm
asserts it is refused and that the remedy names `bash ${KIT_REL}/unattended.sh --dispatch`, never an
absolute path.

Two skips announce themselves. With an empty `PFX` the defect cannot reproduce, so the arm says its
red half is unexercisable at a root install. When the hook saw no `GIT_DIR`, the arm names that
precondition as unmet rather than passing.

The junction arm builds a second repository holding a fixture kit under a different prefix, links
the kit directory into it, symlink first and a junction on Windows as
`tools/codebase-map/adopt-codebase-map.test.sh` already does, and calls `resolve_generated_indexes`
through the link. It asserts the second repository's row, and announces when no link can be made.
The announcement arm calls the resolver from a library copy in a directory no repository contains
and asserts the stderr line and an exit of 0.

### The kit's location probes, fixed and left

The predicate, run over the real tree at `f0971667` on 2026-10-05:

```bash
git grep -nE '(git|GIT) +(-c [^ ]+ +)*-C +[^ ]+ +rev-parse +(--[a-z-]+ +)*--show-(prefix|toplevel|cdup)' -- '*.sh' '.githooks/*' ':!*.test.sh'
```

It printed 26 lines: 2 comments, 2 already scrubbed (`tools/workflows/check-review-join.sh` and
`tools/workflows/check-verifier-fanout.sh`), and 22 code lines. Inside `tools/unattended/`:

| site | runs under a git hook? | under an inherited `GIT_DIR` | disposition |
|---|---|---|---|
| `resolve_generated_indexes` in `tools/unattended/lib-unattended.sh` | yes, at every driver load, so at `commit-msg` | empty prefix, no kit rows | FIXED by S2 |
| `check_commit_message` in `tools/unattended/unattended.sh` | yes, `--check-commit` | absolute remedy path | FIXED by S3 |
| `tools/unattended/resume-tick.sh`, the `_top` probe | no, a scheduled tick | asks `$ROOT` itself, so it can only agree with how `$ROOT` was derived | LEFT |
| `tools/unattended/run-unattended-gates.sh`, `ROOT` and `KIT_REL` | no, the main loop runs it on demand | would answer the kit directory as the root | LEFT, named |

The near-miss, outside the predicate because it asks `--git-common-dir`:
`tools/unattended/adopt-unattended.sh` compares the kit's repository identity with the adopting
repository's, asking git from each. An inherited `GIT_DIR` makes both answer the same id, so the
comparison would read "same repository". An owner runs the adopter by hand, never under a hook, so it
is LEFT and named. Every other git call `--check-commit` reaches runs from `$ROOT` and asks for the
git dir or the common dir, which an inherited `GIT_DIR` answers correctly. Measured: with the
worktree's `GIT_DIR` exported, `--git-common-dir`, `--git-dir` and `--show-toplevel` from the
worktree root matched a shell's.

### The class record

One `kind: class` record under `memory/gotchas/`, named
`inherited-git-dir-pins-the-work-tree-to-the-cwd`, with `universal: false`. The catalogue's
universal budget is 6 of 6 today. The record says that with `GIT_DIR` set and no `GIT_WORK_TREE`,
git takes the current directory as the work tree's top, so `git -C <dir>` answers about `<dir>` as
if it were the root. Git exports it into the hooks and merge drivers of a linked worktree or a
submodule, and into none of the primary-tree hooks measured, which is why each instance passed where
it was written.

It cites the prior instances by id, each verified present in the tree: `TOOL-aCollapsedScan-7`,
`TOOL-aCandidStub-4`, `TOOL-aPacedTurnstile-10`, `TOOL-aSealedCaravan-5`,
`TOOL-aRepatriatedFork-46`, `TOOL-dScrubbedConduit-1`, `TOOL-dRetiredFork-2`, and this unit. It names
the two fixes in use, the logical walk when the question is where a file sits and an
`unset GIT_DIR GIT_WORK_TREE` inside the substitution when git must answer. Its anchors are
`tools/unattended/lib-unattended.sh`, `tools/unattended/unattended.sh`, `.githooks/commit-msg`,
`tools/lib/kit-rel.sh`, `tools/unattended/run-unattended-gates.sh` and
`tools/unattended/adopt-unattended.sh`. It declares its resolution: the driver's instance is gated by
the self-test arm S7 adds, and the class has no machine gate, per the hands-off edge in §3.

### Inventory

| identifier | where | cell |
|---|---|---|
| `derive_self_rel` | `tools/unattended/lib-unattended.sh`, a new inline copy | `sh.function` |
| the S4 announcement line | `resolve_generated_indexes` | stderr text |
| three arms | the driver's self-test | n/a |
| `inherited-git-dir-pins-the-work-tree-to-the-cwd.md` | `memory/gotchas/` | map key, `gotcha-classes` |

`python tools/lexicon/lexicon.py --suggest derive_self_rel --as sh.function` answered OK on
2026-10-05. No function name, conf key, leg or kit file is minted. The record's basename is the one
new map key. It belongs in the unattended-mandate dossier, whose path globs already cover the
library, because the unattended dossier measured 20478 bytes against its 20480-byte cap at
`f0971667`.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/README.md`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/SKILL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `memory/gotchas/INDEX.md`
- `memory/map/features/unattended-mandate.md`
- `memory/map/generated/`

The version bump also moves the marker on every other carrier `tools/check-kit-versions.sh`
enumerates. The class record itself is one new file under `memory/gotchas/`.

### Rollout

1. Write the hook-shaped arm first, and observe it red as a slice against the lib and driver at the
   pass's parent: the commit is refused by check 49 naming the output, and the remedy is absolute.
2. Inline the block, then rewire the two probes and add the announcement. Re-run the three slices.
3. Write the class record, claim its basename, then run `gotchas.py --write` and `gen_map.py --write`.
4. Bump the unattended version once, last, in every carrier, and re-adopt the rendered guides and
   the Skill so they match their templates.
5. Dispatch the pass declaring every path it writes except the outputs a `[[generated]]` row
   declares, then commit through the hook with no `--no-verify` (AC9). The rendered guides and the
   Skill are adopter renders, not `[[generated]]` outputs, so they are declared.

### Alternatives rejected

Each candidate was tested on node `a`, 2026-10-05, git 2.54.0.windows.1, by a probe that reads.

- **Unset `GIT_DIR` and `GIT_WORK_TREE` inside the substitution, then ask git.** This is the in-repo
  pattern of `TOOL-aRepatriatedFork-46`, and it answers the hook correctly: `sub/` from a fixture
  worktree's MSYS `/tmp` spelling, and `tools/unattended/` here, with `GIT_DIR` and
  `GIT_INDEX_FILE` exported. It loses on the junction. In a second repository reaching the kit
  through a junction, `git -C` answered the target repository's `tools/unattended/`, and today's
  resolver printed nothing. `derive_self_rel` answered the adopting repository's `kits/unattended`
  on the same link. The scrub is cheaper, at about 48 ms against 171 ms a call, but it fixes one of
  two defects in one probe.
- **Pin `GIT_WORK_TREE` to `$ROOT` beside the inherited `GIT_DIR`.** From the fixture worktree's
  MSYS `/tmp` spelling, `--show-prefix` printed empty where a shell printed `sub/`, because the
  cwd and the work tree are spelled differently.
- **Strip `$ROOT` from the kit directory's `pwd`.** The hook's `pwd` printed
  `C:/Users/DAILY-~1/...` where git printed `C:/Users/daily-agent/...` for one directory, and MSYS
  spells it `/tmp/...` too, so no strip matches. The comment in `check_commit_message` already
  records the drive-form half of this.
- **Scrub the environment in `.githooks/commit-msg`, as `pre-commit` and `pre-push` do.** Adopters
  wire their own hook, so this fixes gov alone. The siblings' list also includes `GIT_INDEX_FILE`,
  and on `git commit -- <path>` that variable named the `next-index` lock file while another path
  stayed staged in the real index. A copy of that scrub would make `--check-commit` grade the wrong
  index.
- **Unset the variables once at driver load.** `observe_anchor` reads `GIT_DIR` from the environment
  for check 22, the injected-config tripwire, so a load-time scrub would blind it. The three legs
  that source the library would also stay broken.

## 5. Production-readiness checklist

- security — No new surface, and nothing widened. The walk reads directory names only. Check 22
  still reads the environment as it does today, and the admitted set is the one check 23 already
  admits at the close.
- perf / scale — PINNED on node `a`, 2026-10-05, with 14 shells running: `derive_self_rel` costs
  about 171 ms a call against 48 ms for the git probe, once per driver load and once per leg run.
  It is two levels deep at gov's prefix, three forks a level.
- error / empty / loading states — No repository above the kit is the S4 announcement. An empty
  remedy path keeps the `$KIT_DIR` fallback. A root install keeps today's glob.
- observability — The S4 stderr line. The arm's two announced skips.
- risks — A shell that resolves `cd` physically would walk the target, not the link. Bash's `cd` is
  logical by default, and the junction arm observes it on each node that runs the suite.
- testing — Three arms in the driver's self-test, each observed red on a staged break: the lib and
  driver at the pass's parent for the hook arm, the git probe restored for the junction arm, and the
  announcement deleted for its arm.
- migration — None. Every layout this repository ships answers the same tool root as before.
- user docs — N/A. The verbs template and the kit README already state the behaviour this restores.

## 6. Acceptance criteria

- **AC1** — When the hook-shaped arm runs as a slice of the driver's self-test, meaning its
  prologue, `build_check_commit_fixture` and the new block in a temp script inside the kit dir, a
  real `git commit` in the fixture's linked worktree lands. Its `commit-msg` hook ran
  `--check-commit "$1"` with `GIT_DIR` set, and the commit carries the edited fixture generator
  and the output its `[[generated]]` row names, under a `Pass:` trailer naming the open pass. A
  second commit staging an undeclared path is refused, and its printed `--dispatch` remedy names
  the driver by the kit's repository-relative path, as a shell prints it. Run first against the lib
  and driver at the pass's parent, the first commit is refused by check 49 naming the output, and
  the remedy is absolute.
  Red when: the output is refused under the hook, the hook ran without `GIT_DIR` and the arm stayed
  silent, or the remedy names an absolute path.
  fixture: the arm builds its own linked worktree at a short path under the system temp directory.
  It reproduces only at a prefixed install, and announces that at a root install.
  permission: the whole driver self-test is the main loop's at VERIFYING.
- **AC2** — When a scratch repository holds a copy of `tools/unattended/lib-unattended.sh` in a
  prefixed kit dir beside a fixture kit whose `kit.toml` declares one `[[generated]]` row, the
  resolver's output does not depend on the hook. Called in a linked worktree of that repository,
  `resolve_generated_indexes` prints the fixture row with `GIT_DIR` exported to the worktree's
  absolute git dir, byte-identical to the call without it. Called through a directory link from a
  second repository that holds its fixture kit under another prefix, it prints the second
  repository's row.
  Red when: the exported call prints only the conf pairs, or the linked call prints nothing.
  fixture: built by the pass under the system temp directory, with a junction on Windows and a
  symlink elsewhere.
- **AC3** — When `resolve_generated_indexes` runs from a copy of `tools/unattended/lib-unattended.sh`
  in a directory no git repository contains, it exits 0, prints the conf pairs it was given on
  stdout, and prints one stderr line naming that directory. The line says only the repository-root
  kits and the conf pairs were read. With that line deleted from a staged copy, the arm S7 adds fails.
  Red when: the call is silent on stderr, or fails.
- **AC4** — When `git diff <the pass's parent sha> -- tools/unattended/unattended.sh` runs at the
  build commit, no hunk falls inside `verb_dispatch`. The `GENERATED_INDEXES` line of the
  subtraction loop in `check_commit_message` is unchanged.
  Red when: check 49 or the subtraction moved.
  permission: the existing check 49 arms run with the driver self-test at VERIFYING.
- **AC5** — When `diff` compares the `derive_self_rel` block cut from `tools/lib/kit-rel.sh` with
  the one cut from `tools/unattended/lib-unattended.sh`, each between its `# >>>` and `# <<<`
  marker lines, it prints nothing. `git grep -l '^# >>> derive_self_rel'` lists the library, which
  is how the python-resolver leg's parity row finds a copy.
  Red when: the copy differs, or its marker misses the row's discovery grep.
- **AC6** — When the §4 predicate runs at the build commit over `tools/unattended/`, excluding the
  self-tests, it prints the `_top` probe in `tools/unattended/resume-tick.sh`, the two probes in the
  kit's on-demand suite runner that §4 names, and the comment line in
  `tools/unattended/adopt-unattended.sh`. It prints nothing from `tools/unattended/lib-unattended.sh`
  or `tools/unattended/unattended.sh`.
  Red when: either fixed site still asks git for its prefix.
  figure: PINNED at four lines, from the six the predicate printed at `f0971667`.
- **AC7** — When `python tools/memory-tree/gotchas.py --for-paths tools/unattended/lib-unattended.sh`
  runs, its checklist names the new class record. `python tools/memory-tree/gotchas.py --check`
  exits 0, so `memory/gotchas/INDEX.md` is fresh, and `python tools/memory-tree/gotchas.py --declares`
  over the record prints `declares: yes`. `python tools/codebase-map/test_codebase_map.py` prints
  only `ok` lines.
  Red when: the record is unanchored, declares nothing, is unclaimed, or `INDEX.md` or the map is
  stale.
- **AC8** — When `bash tools/check-kit-versions.sh` runs at the build commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` reads `clean` for the
  unattended kit. `git diff <the pass's parent sha> -- tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md`
  changes line 1 of each and nothing else.
  Red when: a carrier keeps the old version, or a governance template's content moved.
- **AC9** — When `git show --stat --format= <the build commit>` runs, it lists
  `memory/gotchas/INDEX.md` beside the paths the pass declared. The commit's message carries the
  `Pass:` trailer naming this unit, and the unit's dispatch row in
  `memory/builds/aGraftedHelix/RUN.md` names no generated output.
  Red when: `--check-commit` refused the index and it rode a later records commit, the unit-3
  symptom.
  fixture: this run's own linked worktree. Its `core.hooksPath` names the primary tree's
  `.githooks/commit-msg`, which runs the worktree's own driver because it derives the top from the
  hook's working directory.

## 7. Gates

`unattended kit gate` · `pass-order history` · `brief-recorded` · `unattended skill wiring` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `python resolver (behaviour + inline parity + idiom ban)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · a real commit through a commit-msg hook in a linked worktree, staging a kit-declared output beside its declared generator; stage the lib and driver at the pass's parent · the suite's floor rises by the arm's assertion count

New arm: tools/unattended/unattended.test.sh · the resolver reached through a directory link from a second repository; stage the kit-dir derivation restored to the git probe · the suite's floor rises by the arm's assertion count

New arm: tools/unattended/unattended.test.sh · the resolver called from a library copy outside any repository; stage the S4 line deleted · the suite's floor rises by the arm's assertion count

The unattended suites are not on the bar (`tools/unattended/README.md`), and the python-resolver
parity row is a held kit leg. A pass runs its arms as slices and AC5's `diff` directly, and the main
loop runs the suites once at VERIFYING.

## 8. Open questions

- **F1 — Does `--check-commit` admit a generated output only when the committing pass declared its
  generator, or any resolved generated output, as today?**
  Option A keeps today's subtraction, which covers any path a resolved row names. Option B narrows it
  to outputs whose generator the pass declared. B would make `--check-commit` and check 23 two
  answers to one question, because check 23 subtracts the same set unconditionally at the close. It
  would also refuse the hook-forced re-renders, `memory/LIVE.md` on any spec header move, in passes
  that touch no generator. A needs no code. B adds a refusal and fails the brief's own case.
  RESOLVED (agent, 2026-10-05, delegated): A. The subtraction is unchanged, and AC1 observes the
  brief's case admitted.
- **F2 — Is check 49 narrowed to refuse only two concurrent passes that split an index and its
  generator, or kept refusing one declaration that names both as well?**
  The brief asks to keep the refusal for a concurrent pair. At `f0971667` check 49 refuses both
  shapes, and the driver self-test arms both. Once F1's subtraction resolves under the hook, no pass
  needs to declare its generated output, so the single-declaration refusal costs nothing. Narrowing
  it moves a refusal no defect asks to move.
  RESOLVED (agent, 2026-10-05, delegated): keep both shapes, with no change, and AC4 observes it.
- **F3 — Does bumping the unattended version marker on the protocol, verbs and stops templates
  breach shared invariant 10, which reserves edits to them for unit 1?**
  Option A bumps the marker everywhere, so line 1 of those three templates and their renders moves.
  Option B leaves them stale, which reds `kit version markers` and breaks shared invariant 4. Option
  C leaves the kit unbumped, which reds `kit epoch (shipped bytes move, the version moves)`. The
  marker is a derived carrier of the version, and invariant 10 protects content. Unit 3's F1
  ratified the same reading for `memory/guides/BUILD-METHOD.md`. Unit 19's build commit `6a1a2feb`
  moved exactly one line in each of these templates.
  RESOLVED (agent, 2026-10-05, delegated): A, with AC8's line-1 diff as the observation.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the unit's section of the 2026-10-05 spec brief and the
  shared brief's invariants. Grounded against `tools/unattended/lib-unattended.sh`,
  `tools/unattended/unattended.sh` and `.githooks/commit-msg` at the run branch's `f0971667`. The
  defect, the hook environment and the four rejected candidates were measured on node `a` the same
  day.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "clear the git environment a hook inherits before probing a directory's repository prefix"`
ranked `git` in `tools/govkit/` first, a Python wrapper, and `build_git_env` in
`tools/memory-tree/transition_audit.py`, which pins a graft file and scrubs nothing. The probe
printed `unscanned layers: .sh`, so the shell layer was grepped by hand. Two seams turned up. One is
`derive_self_rel` in `tools/lib/kit-rel.sh`, the canonical logical walk with a parity row, which
this unit extends by one inline copy. The other is the `unset GIT_DIR GIT_WORK_TREE` substitution in
`tools/workflows/check-review-join.sh` and `tools/workflows/check-verifier-fanout.sh`, a sibling
kit's file and therefore a pattern rather than a callee, which lost on the junction in §4. The seam
this unit rewires is `resolve_generated_indexes` in `tools/unattended/lib-unattended.sh`, the one
resolver the driver and the three legs share. Recall surfaced the class's history:
`TOOL-aCollapsedScan-7` fixed the same root cause by walking up for a conf bounded by `.git`, and
`TOOL-dScrubbedConduit-1` measured that a primary clone exports no `GIT_DIR` into a hook while a
linked worktree does. Both agree with today's source. No catalogue record named the class, so S8
writes one.

Recall terms used: GIT_DIR inherited hook linked worktree show-prefix scrub unset environment leak commit-msg check-commit generated index

The question passed with them: "why does a git hook's inherited GIT_DIR break a kit's location
probe, and how was it scrubbed before".
