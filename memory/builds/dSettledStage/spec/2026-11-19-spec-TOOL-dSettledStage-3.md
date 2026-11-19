# TOOL-dSettledStage-3 — a failed stage refuses: the lander's stage helper answers 2 and every caller aborts on it

**Status:** SPECCED · rev-1 · 2026-11-19 · node d · Tier-2 · base 12764ec2 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-prompt-TOOL-dSettledStage-3-promotion-brief.md](../prompts/2026-11-19-prompt-TOOL-dSettledStage-3-promotion-brief.md) | research | TOOL-dSettledStage-4 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 closing review of this build found one HIGH defect, its item 1: `write_staged_change`
never reads the exit status of `git add -A`, so a stage that fails reads as "nothing staged". The
lander then skips its mint, gov-first and regen commits without a word and pushes, and the
prepared merge's fold reports success without folding. This unit gives the helper a third answer
for a failed stage, makes every caller refuse on it with its own stage's line, and records the
class in the bug-class catalogue.

## 2. Scope (IN)

- **S1** — `tools/push-main.sh#write_staged_change` answers 2 when staging fails. It reads the
  dirty predicate into a `local dirt` and answers 2 when `git status` exits non-zero, 1 when the
  status prints nothing, and 2 when `git add -A` exits non-zero. Its answers 0 and 1 keep their
  meaning. The comment above the definition and the return-contract comment on its line name the
  answer 2. Observed by AC2, AC3 and AC8.
- **S2** — The three attended commit sites, mint, gov-first and regen, each read the helper's
  answer into `staged` with `write_staged_change; staged=$?`. On 2 the site prints its own stage
  refusal on stderr and runs `exit 1`, before any commit and before the push. On 0 the site runs
  its existing commit block. On 1 it commits nothing, as today. Each site's `read_mint_unit` call,
  its `git commit -q --no-verify` line, its `Pass: none` trailer and its commit refusal line stay
  byte-identical. Observed by AC1, AC4 and AC5.
- **S3** — `tools/push-main.sh#write_merge_fold` maps the helper's 1 to `return 0` and its 2 to
  `return 1`, so a failed stage refuses the fold instead of reporting the tree as HEAD's. Its two
  callers in `cmd_prepare` already refuse on its 1 with their own lines and do not change. The
  return-contract comment on its line names a failed stage beside the failed commit and ref move.
  Observed by AC2.
- **S4** — `tools/push-main.test.sh` gains arm 44: the attended landing over a planted `regen.py`
  that writes a real change and then holds the git dir's `index.lock`. Observed by AC1.
- **S5** — `tools/push-main.test.sh` gains arm 45: `write_staged_change` and `write_merge_fold`
  cut from the lander and run with `index.lock` held over a real change, with an unlocked control.
  Observed by AC2.
- **S6** — `memory/project/unarmed-branches.txt` gains a pin row for the mint and the gov-first
  stage refusals, the two arm 44 does not stage. The regen stage refusal gets no row, because arm
  44 arms it. Observed by AC6.
- **S7** — The bug-class catalogue gains the class `failed-stage-reads-as-nothing-staged`, as the
  record `memory/gotchas/failed-stage-reads-as-nothing-staged.md`, with the catalogue's index
  re-rendered by `python tools/memory-tree/gotchas.py --write`. The push-main dossier's
  `gotcha-classes` list claims `failed-stage-reads-as-nothing-staged.md`, and
  `python tools/codebase-map/gen_map.py --write` renders the map in the same commit. Observed by
  AC7.
- **S8** — The lander's header paragraph on regenerated outputs states that a stage which fails
  refuses the landing with no push. Observed by AC8.

## 3. Non-goals (OUT)

- No change to `run_regen`, `regen.py`, any generator, `.gitattributes`, `.githooks/pre-push`, the
  merge bar or `tools/run-gates/`.
- No edit to the CLOSED specs of TOOL-dSettledStage-1 and TOOL-dSettledStage-2. They stay frozen.
- No change to `tools/gate-lint/sh_hygiene.py` or to arm 43. The scan's gaps and arm 43's
  liveness markers are the closing review's items 2 to 6, which are TOOL-dSettledStage-4's. The
  review's suggested left-shift, a scan mode that reds a `git add` whose exit status a stager
  never reads, is a new scan mode and a separate mechanism. This unit records the class as a
  catalogue entry instead, as the brief directs, and the entry states that no gate reads it.
- No new reset, clean or restore on a stage refusal. The commit refusals beside it leave the tree
  as it stands, and a held lock refuses a reset too.
- No change to how `cmd_prepare` cleans up after a refused fold. Under a held lock its own
  `git reset` and `git checkout` fail as well; section 5 states what that leaves.
- No change to the commit sites in `tools/unattended/`. The registry row for
  `tools/unattended/unattended.sh` stays the owner's follow-up.
- No `--allow-empty` commit, no new `--no-verify` and no `set -e`.

The helper this unit extends is in the tree at the build's head, landed by the CLOSED unit 1, so
nothing here rests on unbuilt work. TOOL-dSettledStage-4 follows this unit only because both write
`tools/push-main.test.sh`, which is an order and not an edge.

### Edges

none

## 4. Design

### The defect, reproduced

Reproduced on node d with Git 2.54.0.windows.1 on 2026-11-19, in scratch repositories under
`%TEMP%`. With a tracked file modified and an empty `index.lock` in the git dir,
`git status --porcelain --ignore-submodules=untracked` exits 0 and names the file, `git add -A`
exits 128 with git's `Unable to create ... index.lock` line, `git diff --cached --quiet` exits 0,
and `git write-tree` exits 128. The helper as built answered 1, and `write_merge_fold` answered 0
with HEAD unmoved.

The attended landing was reproduced on a clone of this repository at ce7e513b, whose `tools/`
equals the review head 41e57fca5. A planted `tools/run-gates/regen.py` rewrote a tracked file and
then wrote an empty `index.lock` into the git dir. The lander minted, walked gov first, skipped the
regen commit, printed `gating + pushing`, pushed, and exited 0, with the change uncommitted and the
lock still held. The same clone, with S1 and the regen half of S2 applied and committed, exited 1
with the regen stage refusal, and `origin/main` stayed at its base.

With `.git/index` overwritten by garbage bytes, `git status` exits 128, and the helper as built
answered 1, reading the failure as a clean tree.

### The helper

```bash
write_staged_change() {  # -> 0 the index differs from HEAD · 1 the tree was clean, or staging left nothing · 2 staging failed
  local dirt
  dirt=$(git status --porcelain --ignore-submodules=untracked 2>/dev/null) || return 2
  [ -n "$dirt" ] || return 1
  git add -A || return 2
  git diff --cached --quiet && return 1
  return 0
}
```

- **A failed `git status` answers 2.** The lander's two opening checks already read a failed
  status as dirt and refuse (`tools/push-main.sh@f8e4540deccb:1106`, `:1329`). The helper as built
  read it as a clean tree, which is the same class as the failed add, so S1 closes both in the one
  function the class lives in. The predicate's spelling stays as it is, because arm 13 counts it
  (`tools/push-main.test.sh@a4ace06ab2db:490`).
- **`local dirt`.** The attended loop runs at top level and binds `dirt` for its opening check, and
  `cmd_prepare` declares its own `local dirt`. The helper's `local` shadows both for the call alone.
- **git's own line names the cause.** `git add -A` prints its lock or I/O error on stderr, and the
  caller's refusal follows it. The helper prints nothing of its own.
- **An error from `git diff --cached --quiet` still answers 0**, as unit 1 designed it: the
  caller's commit runs and refuses with its own line.
- The comment above the definition gains one sentence: a failed status or stage answers 2, and
  every caller refuses on it rather than reading it as nothing staged, the closing review's item 1.

### The attended sites

Each of the three sites (`tools/push-main.sh@f8e4540deccb:1361`, `:1385`, `:1408`) takes this
shape, shown for the mint:

```bash
  write_staged_change; staged=$?
  if [ "$staged" = 2 ]; then
    echo "push-main: could not stage the minted versions. Aborted (no push)." >&2
    exit 1
  fi
  if [ "$staged" = 0 ]; then
    mint_unit=$(read_mint_unit "$mt..HEAD")
    if ! git commit -q --no-verify -m "mint: …" -m "Pass: none"; then   # unchanged
      …
```

| Site | Stage refusal line |
|---|---|
| mint | `push-main: could not stage the minted versions. Aborted (no push).` |
| gov-first | `push-main: could not stage gov's receipt of the upgrade steps. Aborted (no push).` |
| regen | `push-main: could not stage the regenerated outputs. Aborted (no push).` |

Each line mirrors its site's commit refusal, with `stage` for `commit`. `staged` is a new name in
`tools/push-main.sh`: `grep -n 'staged=' tools/push-main.sh` printed nothing on 2026-11-19. The
push follows the regen site (`tools/push-main.sh@f8e4540deccb:1427`), so an `exit 1` at any of the
three sites precedes it.

**The commit refusals stay live** (`memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md`).
The new branch settles only a failed stage. A stage that succeeds can still fail to commit, on a
lock taken between the add and the commit or on a missing identity, so each pinned commit refusal
row stays true.

**The stage-commit leg stays green on the lander.** `scan_stage_file` in
`tools/gate-lint/sh_hygiene.py` reads a call to a checked stager as a stage followed by a staged
test, and the helper stays checked, its `git diff --cached` test following its `git add`. So each
site's commit reads `admitted` and `memory/project/stage-commit-sites.txt` needs no row for the
lander.

### The fold

```bash
write_merge_fold() {  # first parent · second parent · message -> 0 HEAD is the merge over the tree, or the tree was HEAD's · 1 the stage, the commit or the ref move failed
  write_staged_change
  case $? in 1) return 0 ;; 2) return 1 ;; esac
  t=$(git commit-tree "$(git write-tree)" -p "$1" -p "$2" -m "$3") && git update-ref --no-deref HEAD "$t" || return 1
}
```

Its callers in `cmd_prepare` (`tools/push-main.sh@f8e4540deccb:1177`, `:1194`) refuse on its 1
with `could not fold the upgrade steps' output into the merge before the regeneration` and
`could not commit the minted versions into the merge`. Neither line changes.

### Arm 44 — the attended landing with the index locked over a real change

Arm 44 sits in the `if [ -n "$_rg_k" ]` block (`tools/push-main.test.sh@a4ace06ab2db:1130`),
directly after arm 42, and its skip line joins that block's. It runs in a subshell and reuses
`tools/push-main.test.sh#build_regen_fixture`, as arm 42 does.

1. `build_regen_fixture "$tmp/remote44.git" "$tmp/work44"`, then record `R44=$(git rev-parse HEAD)`.
2. Commit a tracked `lock-real.txt` holding `one`, and a planted regen.py written through a quoted
   heredoc, as arm 37 plants its own (`tools/push-main.test.sh@a4ace06ab2db:1532`). The regen.py
   rewrites `lock-real.txt` to `two`, then writes an empty `index.lock` into the directory
   `git rev-parse --git-dir` names. Commit with `--no-verify`. The quoted heredoc keeps the Python
   source byte for byte, so no shell escape reaches its string literals
   (`memory/gotchas/heredoc-escape-reaches-the-regex.md`).
3. `unset GATE_PUSH_BASE; bash "$lander" 2>&1`, then echo `rc=$?`.
4. **Liveness, after the landing.** Echo `locked=1` when the git dir holds `index.lock`, which
   proves the regeneration ran and held the lock at the stage. Echo `dirty=1` when
   `git status --porcelain -- lock-real.txt` prints a line. Echo `unpushed=1` when
   `git ls-remote origin refs/heads/main` prints `R44`. Then clear the lock with `rm -f`.

Passing means the output carries the regen stage refusal line, `rc=1`, `unpushed=1`, `locked=1`
and `dirty=1`, and does not carry `gating + pushing`. The test is a `case` over the output with the
refusal text as a positive pattern, as arm 32 tests its refusal
(`tools/push-main.test.sh@a4ace06ab2db:1217`). That positive assertion is what arms the regen stage
refusal for `check-arms.py`. The `bad` line prints the captured output whole.

The suite source spells no pinned refusal text. The mint and gov-first stage refusals are pinned by
S6 and the commit refusals are pinned already, and a positive assertion naming a pinned branch's
text reds the arms leg.

### Arm 45 — the fold with the index locked, and its control

Arm 45 sits after arm 43, before the suite's closing line
(`tools/push-main.test.sh@a4ace06ab2db:1724`). It cuts both functions with arm 38's
`eval "$(sed -n "/^$f() {/,/^}/p" "$lander")"` idiom and runs in a subshell, in a fresh
`git init` repository at `$tmp/fold45`.

1. Build the detached `--no-ff` merge arm 43 builds, without its line-ending steps, and record
   `P1`, `P2` and the merge `M`.
2. Write `changed` to `f.txt` and create an empty `index.lock` in the git dir.
3. **Liveness.** Echo `lock-dirty=1` when `git status --porcelain -- f.txt` prints a line. Echo
   `lock-refuses=1` when `git add -A` exits non-zero, which proves this git refuses a stage under
   the lock.
4. `write_staged_change` and echo `stage-rc=$?`. Then `t=$M; write_merge_fold "$P1" "$P2" msg` and
   echo `fold-rc=$?`. Echo `head=same` when HEAD is still `M`.
5. **Control.** Clear the lock with `rm -f`, run the fold again and echo `free-rc=$?`. Echo
   `free-moved=1` when HEAD is no longer `M`, its parents are `P1` and `P2`, and `HEAD:f.txt`
   reads `changed`.

Passing means `lock-dirty=1`, `lock-refuses=1`, `stage-rc=2`, `fold-rc=1`, `head=same`,
`free-rc=0` and `free-moved=1`. The control stops a helper that answers 2 on every call from
passing. The content change gives the folded merge a new tree, so its sha differs from `M` without
arm 43's pinned dates.

### The pin rows

Two rows in `memory/project/unarmed-branches.txt`, in the five tab-separated fields of the rows
already pinned for `tools/push-main.sh`: the gate, `exit`, occurrence `1`, the refusal line as the
signature, and a reason. Each reason names the condition no arm stages, in the existing rows' form:
`no arm in tools/push-main.test.sh stages [ "$staged" = 2 ] holding`, with the condition in
backticks, at the mint site and at the gov-first site.

### The catalogue entry

`memory/gotchas/failed-stage-reads-as-nothing-staged.md` is a `kind: class` record with the
front matter and the five body sections its siblings carry, `signal-killed-hook-reads-as-success.md`
among them: Symptom, Where it bit, Why, The fix and Gate.

- **Symptom:** a commit step reports nothing to commit, or a fold reports the tree unchanged, while
  `git status` still shows the change, and the run goes on to push.
- **Where it bit:** the closing review of this build, item 1, on the lander's helper at the review
  head 41e57fca5. Its body backticks `tools/push-main.sh`, so the record anchors on the lander.
- **Why:** a staged-diff test cannot tell "the stage holds nothing new" from "the stage never
  happened", because a failed `git add` leaves the index equal to HEAD.
- **The fix:** read the stage's own exit status, and the status probe's, before the staged-diff
  test, and give the failure its own answer that every caller refuses on.
- **Gate:** arms 44 and 45 of `tools/push-main.test.sh` gate the lander's instance. No gate reads
  the class elsewhere: `tools/gate-lint/sh_hygiene.py`'s stage-commit mode reads whether a staged
  test follows a stage, never whether the stage's exit status was read.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `staged` | top-level shell variable in the attended loop of `tools/push-main.sh` | none | arm 44 |
| answer 2 of `write_staged_change` | return code | none | arms 44 and 45 |
| the three stage refusal lines | refusal sites | none | `harness arms (fail branches armed or pinned)`, by arm 44 or a pin row |
| arm 44 | suite arm in `tools/push-main.test.sh` | none | the suite's own `ok` and `bad` lines |
| arm 45 | suite arm in `tools/push-main.test.sh` | none | the suite's own `ok` and `bad` lines |
| `failed-stage-reads-as-nothing-staged` | bug class | none | `memory hygiene`, check 17 to 19 |

No function is minted. Arm 43 is the suite's highest arm today
(`tools/push-main.test.sh@a4ace06ab2db:1686`), so the new arms take 44 and 45.

### Files touched (estimate)

`tools/push-main.sh` · `tools/push-main.test.sh` · `memory/project/unarmed-branches.txt` ·
`memory/gotchas/failed-stage-reads-as-nothing-staged.md` · `memory/gotchas/INDEX.md` ·
`memory/map/features/push-main.md` · `memory/map/generated/`

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| `git add -A \|\| return 0`, so the caller's commit refuses | The brief forbids relying on the caller's later commit failing, and the skeptic judged it instance-only: it leaves the class standing. |
| `set -e` in the lander | The helper is called in conditions, where errexit does not apply, and the lander runs under `set -u` alone by design. |
| One refusal helper taking the stage's name | One interpolated line is one signature for `check-arms.py`, so arm 44's regen case would read as arming the mint and gov-first refusals it never stages. |
| One arm asserting both refusals | The attended half needs `regen.py` beside the lander and belongs in the block whose skip line names that precondition. The fold half needs neither, and would be skipped with it. |
| A scan mode in `tools/gate-lint/sh_hygiene.py` for an unread stage exit | A new mode is a separate mechanism, and that file is TOOL-dSettledStage-4's write set. |
| Reset the tree on a stage refusal | A held lock refuses the reset too, and the commit refusals beside it leave the tree as it is. |

## 5. Production-readiness checklist

- security: no new write path and no new surface. `--no-verify` stays on the three lander commits
  that carry it, and AC5 pins that. A failed stage now stops the push instead of publishing a tree
  the lander never committed.
- perf / scale: no new git call. The status output is captured into a variable instead of a test.
- error / empty / loading states: a failed status or stage answers 2 and its caller refuses with
  its own line after git's own error. An empty stage is still a silent skip.
- observability: three new refusal lines, each naming its stage, follow git's own error on stderr.
- risks: a refused `--prepare` under a held lock cannot run its own `git reset` and
  `git checkout`, so HEAD stays detached on the prepared merge with the change in the tree. The
  branch ref does not move, because the compare-and-swap after the fold never runs, so the
  landing's safety holds. The refusal's words "is checked out" are then untrue. Every
  `cmd_prepare` refusal shares that under a held lock, and this unit does not change it. The
  portability sweep (`memory/gotchas/portability-sweep.md`) is answered for the lock domain: git
  refuses an index write while `index.lock` exists on every platform, and arm 45's liveness step
  proves it on the host that runs the suite.
- testing: the probes of section 6 and arms 44 and 45 of section 7. Arms 29 and 42 stay the
  attended controls for a stage that holds a change and one that holds none, and arm 43 the fold's.
- migration: N/A — no stored data and no conf key changes; the lander is copied in whole.
- user docs: N/A — no page under `help/` describes the lander's stage or commit steps.
  `git grep -n push-main -- help/` names only the command line in `help/reference/drive.md`.

## 6. Acceptance criteria

- **AC1** — When the attended landing `tools/push-main.sh` runs in arm 44's fixture, it prints
  `push-main: could not stage the regenerated outputs. Aborted (no push).` and exits 1. The
  remote's `main` still names `R44`, the git dir still holds `index.lock`, and
  `git status --porcelain` names `lock-real.txt`. No `gating + pushing` line is printed.
  Red when: the lander at 41e57fca5 runs in the same fixture, prints `gating + pushing`, pushes,
  and exits 0, as observed on 2026-11-19.
  fixture: built by arm 44 under the suite's `$tmp`. By hand on Windows it needs a short
  `%TEMP%/<name>` path, because a clone under the run's scratchpad fails with Filename too long.
- **AC2** — When a `bash -c` probe cuts `write_staged_change` and `write_merge_fold` out of
  `tools/push-main.sh` with arm 38's `sed -n` idiom, and runs them on a detached merge whose
  `f.txt` holds a real change with an empty `index.lock` in the git dir, the helper returns 2,
  the fold returns 1, and `git rev-parse HEAD` is unchanged. With the lock cleared, the fold returns 0 and
  HEAD is a new merge with the same parents whose `f.txt` carries the change.
  Red when: the lander at 41e57fca5 is cut instead, whose helper returns 1 and whose fold returns
  0 under the lock, as observed on 2026-11-19.
- **AC3** — When the same `bash -c` probe runs the cut `write_staged_change` in a repository whose
  `.git/index` holds garbage bytes, so `git status` exits 128, the helper returns 2.
  Red when: the helper reads the failed status as a clean tree and returns 1, as the lander at
  41e57fca5 does.
- **AC4** — When `grep -c 'write_staged_change; staged=\$?' tools/push-main.sh` runs, it prints 3.
  When `grep -c 'if write_staged_change; then' tools/push-main.sh` runs, it prints 0. When
  `grep -cE 'could not stage (the minted versions|gov.s receipt of the upgrade steps|the regenerated outputs)\. Aborted \(no push\)\.' tools/push-main.sh`
  runs, it prints 3.
  Red when: a site keeps `if write_staged_change; then`, which reads 2 as a skip, or a site
  refuses with no line of its own.
- **AC5** — When
  `git grep -h -E -e '--no-verify|could not commit|could not fold' 41e57fca5 -- tools/push-main.sh`
  and `grep -E -e '--no-verify|could not commit|could not fold' tools/push-main.sh` run, they print
  the same lines in the same order.
  Red when: a commit line, a `--no-verify` use or a commit or fold refusal is reworded, added or
  taken out, which would also strand its pin row.
- **AC6** — When `grep -cF 'could not stage the minted versions' memory/project/unarmed-branches.txt`
  and `grep -cF "could not stage gov's receipt" memory/project/unarmed-branches.txt` run, each
  prints 1, and `grep -cF 'could not stage the regenerated outputs' memory/project/unarmed-branches.txt`
  prints 0.
  Red when: a stage refusal arm 44 does not stage has no pin row, or the regen refusal arm 44 arms
  is pinned too, which `check-arms.py` refuses.
- **AC7** — When `python tools/memory-tree/gotchas.py --for-paths tools/push-main.sh` runs, its
  checklist names `failed-stage-reads-as-nothing-staged`. When
  `grep -c 'failed-stage-reads-as-nothing-staged' memory/gotchas/INDEX.md memory/map/features/push-main.md memory/map/generated/MAP.md`
  runs, each file counts at least one.
  Red when: the record does not anchor on the lander, the index is not re-rendered, the dossier
  does not claim the class, or the map is not re-rendered.
- **AC8** — When
  `sed -n '/^# GENERATED OUTPUTS ARE REGENERATED HERE TOO/,/^# AFTER A LANDING/p' tools/push-main.sh`
  runs, the paragraph says that a stage which fails refuses the landing with no push. When
  `grep -n '^write_staged_change() {' tools/push-main.sh` runs, the line's return-contract comment
  names the answer 2.
  Red when: the paragraph and the contract comment still describe only the answers 0 and 1.

## 7. Gates

`push-main self-test` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `shell hygiene (a stage committed with no staged-diff test)` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `writing practice (records and units)` · `positional (the citation check alone)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

New arm: tools/push-main.test.sh · covers AC1 · arm 44, the attended landing over a planted regen.py that writes a real change and then holds the git dir's index.lock; its failing case is staged by restoring the lander of 41e57fca5, which skips the regen commit and pushes · none
New arm: tools/push-main.test.sh · covers AC2 · arm 45, write_staged_change and write_merge_fold cut from the lander and run with index.lock held over a real change, then unlocked as the control; its failing case is staged by restoring the helper and fold of 41e57fca5, which answer 1 and 0 under the lock · none

Neither arm moves a floor. `tools/push-main.test.sh` is listed in
`memory/project/testsuite-count-waivers.txt`, so no suite count is pinned for it. `ARMS_FLOORS` in
`.memory-tree.conf` bounds the census of `tools/push-main.sh` from below only, so the three new
refusal sites and the one new armed site do not red it, and no ceiling is declared for that gate.
AC3 to AC8 are observed by their own commands at the close. Arms 29, 42 and 43 stay the controls
that a stage holding a change still commits and folds.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft.

## 10. Reuse audit

The seam extended is `tools/push-main.sh#write_staged_change`, the one place the lander stages,
which unit 1 lifted out of its four sites. This unit gives it a third answer rather than adding a
second stager, and its four callers already route through it. The suite seams are
`tools/push-main.test.sh#build_regen_fixture` with arm 42's attended subshell and arm 32's
unpushed check for arm 44, arm 37's heredoc-planted regen.py, and arm 43's cut-and-merge fixture
with arm 38's function-cut idiom for arm 45.

`python tools/codebase-map/reuse_lookup.py "refuse when staging the working tree fails before a commit"`
ranked `tree`, `before`, `fail`, `remove_tree`, `write_commit` and `build_commit`. None stages a
shell working tree and answers on a failed stage. `build_commit` and `pass_commit` live in
`tools/unattended/lib-unattended.sh`, another kit the copy-installed lander cannot source. So no
existing seam fits beyond the lander's own helper.

Recall returned the closing review and this unit's brief as the source of the finding, unit 1's
spec as the helper's design, and TOOL-aTrimmedWait-8's spec as a precedent for a fixture that holds
`index.lock`. That precedent copies the index into the lock, and this spec's probe found an empty
file refuses every index write the same way. Recall named no earlier failed-stage defect in the
lander.

Recall terms used: push-main write_staged_change git add index.lock stage refusal lander abort no push fold
