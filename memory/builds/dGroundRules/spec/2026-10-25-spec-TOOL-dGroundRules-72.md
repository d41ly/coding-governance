# TOOL-dGroundRules-72 — the pre-commit policy guard reads the index git hands the hook, so `git commit -a` and `git commit <path>` are graded

**Status:** CLOSED · rev-2 · 2026-10-25 · node d · Tier-1 · base fce5603f · streams tooling · order 26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 |
| [2026-10-25-build-TOOL-dGroundRules-72-ledger.md](../build/2026-10-25-build-TOOL-dGroundRules-72-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-72-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-72-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-72-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-72-spec-brief.md) | research | — |
| [2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md](../reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md) | diff-review | TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 |

<!-- /gen:spec-records -->

## 1. Goal

The policy guard in `.githooks/pre-commit` admits an agent's commit of a guarded path when the
commit is made with `git commit -a` or `git commit <path>`. In both, git hands the hook a temporary
index through `GIT_INDEX_FILE`. The hook unsets that variable at `:8`, so the guard block's staged
reads see the real index, which stages nothing, and the hook exits 0. This unit saves the handed
index before the unset and passes it to the guard block's two staged reads and to the guard itself.
A plain `git add` and `git commit` is judged as it is today.

## 2. Scope (IN)

- **S1** — The handed index reaches the policy guard. In `.githooks/pre-commit`, three lines go in
  above the comment at `:6`: `hook_index` saved from `GIT_INDEX_FILE`, made absolute when relative,
  and a one-line function `with_hook_index` that runs its arguments with that index. The block's
  `git diff --cached` at `:195`, its `"$py" "$g" --staged` at `:204` and its `git diff --cached` at
  `:211` each run through `with_hook_index`. In `.githooks/pre-commit.test.sh`, three arms go in:
  two after the AC9 arm at `:223` and one after the S21 arm at `:229`, as §4 "The arms" gives.
  `tools/policy/guard.py` does not change. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- `tools/policy/guard.py`. Every staged read it makes goes through `run_git`, which passes the
  environment on (§4 "Evidence"), so the index the hook passes reaches all of them.
- The other staged legs of the hook: memory-tree hygiene at `:219`, kickoff-manifest at `:230`,
  unattended wiring at `:239`, the charter leg at `:248` and the codebase-map leg at `:272`. Each
  reads the real index too, and §8's rev-1 entry names them as a follow-up.
- The left-shift gate the report proposes, a hook lint over every staged read after the unset.
  §8's rev-1 entry names it as a follow-up.
- `help/policy.md`. Its guard section at `:145-200` already describes the behaviour this unit
  restores, and does not name `-a` among what passes the guard, so it stays current.
- The `govkit:branch-guard` block at `:18-87`, which is all the push-main kit ships of this file
  (`tools/govkit/entries/push-main.kit.toml:38-52`). The edit lands outside it.
- The other findings of the closing review, the inherited reds the close recorded, and any other
  spec.

### Edges

none

This unit repairs the policy-guard block that `TOOL-dGroundRules-6` (CLOSED) built and
`TOOL-dGroundRules-21` (CLOSED) extended with S21. It changes neither unit's verdict on a staged
commit.

## 4. Design

### Evidence

Read at `fce5603f8`. `.githooks/pre-commit:8` unsets `GIT_INDEX_FILE` with seven other location
variables. The policy-guard block at `:191-216` runs after it. `:195` reads the staged names with a
bare `git diff --cached`, `:204` runs the guard, and the `else` branch at `:211` reads them again
when no `guard.py` resolves.

The guard reads the index only through `run_git` (`tools/policy/guard.py:46-61`), which calls
`subprocess.run` with no `env`, so a variable set on the guard's process reaches every git call.
Those reads are `read_touched_paths` (`:86`) and every `read_blob_id("", p)` (`:66`), which asks
for `:<path>`. The mirror render at `:121` runs `policy.py mirror --print` as a subprocess. That
reader drops `GIT_INDEX_FILE` from its own git calls (`tools/policy/policy.py:71-84`) and renders
`HEAD`, so passing the index does not change it.

Measured on this node, git 2.54.0.windows.1, with a stand-in pre-commit hook in a scratch repository
that printed `GIT_INDEX_FILE` and its staged names before and after an unset:

| Commit | `GIT_INDEX_FILE` handed | staged after the unset |
|---|---|---|
| `git commit -am` | `<git dir>/index.lock`, absolute | nothing |
| `git commit -m … -- p` | `<git dir>/next-index-<pid>.lock`, absolute | nothing |
| `git add p`, then `git commit` | `.git/index`, relative | `p` |
| `git commit -am` in a linked worktree | `<git dir>/worktrees/w/index.lock` | nothing |
| `git commit -- ../p` from a subdirectory of that worktree | `.../worktrees/w/next-index-<pid>.lock` | nothing |

In every row the hook started at the top of the work tree, the subdirectory row included. The
premise holds on the real hook too. AC1's fixture, run against the hook at `fce5603f8`, printed
`am rc=0`, `path rc=0` and `noguard rc=0 0`, so all three bypasses commit. The same fixture with
`tools/policy/guard.py` copied in place of the stand-in gave the same three exit codes, and the
staged commit was refused with rc 1.

### The fix

The report's skeptic judged the finder's fix SOUND. This design follows it with one correction. The
report says a relative index is made absolute against the git dir. The probe shows git hands
`.git/index`, which is relative to the work tree top, where git starts the hook. So a relative value
is made absolute against `$PWD` before the hook's own `cd` at `:15`. Against the git dir it would
name `.git/.git/index`. A value that starts with a drive letter and a colon is already absolute.
Git on Windows hands one as `C:/...`.

These lines go in above `:6`, followed by one blank line, so the comment at `:6-7` stays above the
unset it describes:

```
# The index git handed this hook, saved before the unset below (TOOL-dGroundRules-72). Under
# `git commit -a` or `git commit <path>` it is a temporary index, and a staged read of the real one
# sees nothing staged. Relative, it is relative to the work tree top, where git starts a hook.
hook_index=${GIT_INDEX_FILE:-}
case $hook_index in ""|/*|[A-Za-z]:*) ;; *) hook_index=$PWD/$hook_index ;; esac
with_hook_index() { if [ -n "$hook_index" ]; then GIT_INDEX_FILE=$hook_index "$@"; else "$@"; fi; }
```

The three call sites change only by the prefix:

```
  [ -z "$pg_list" ] || pg_hit=$(with_hook_index git diff --cached --name-only --no-renames | grep -xF -- "$pg_list" || true)
    elif ! with_hook_index "$py" "$g" --staged; then
  if [ -n "$pg_list" ] && with_hook_index git diff --cached --name-only --no-renames | grep -qxF -- "$pg_list"; then
```

With no `GIT_INDEX_FILE`, as when the hook is run by hand, `with_hook_index` runs its arguments
unchanged, which is today's behaviour. An assignment before a command exports the variable to that
command only, so nothing after the block sees it. A prototype of exactly this text in a scratch copy
of the hook passed `bash -n` and gave AC1's and AC2's green lines.

The `git ls-files` at `:198` keeps reading the real index. It picks the python launcher and gives no
verdict. If the real index lacks the resolver, the block refuses, which fails closed.

### The arms

The current AC9 arms stage with `git add` (`.githooks/pre-commit.test.sh:206-223`), so they pass
whichever index the hook reads. The new arms commit the listed path without `git add`. Each first
runs `git reset -q`, so the real index stages nothing and only the handed index names the path. The
stand-in guard refuses only when its own staged read names the listed path, so an arm reds when
either the block's read or the guard's read misses it.

These lines go in directly after `:223`:

```
# TOOL-dGroundRules-72: a listed path committed by `git commit -a` or `git commit -- <path>`, never
# added. Git hands the hook a temporary index and the real one stages nothing, so the block and the
# guard must both read the handed one. This stand-in refuses only when ITS OWN staged read names the
# listed path, so an arm reds when either read misses it. Each arm resets the real index first.
printf 'import subprocess, sys\nseen = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True).stdout.split()\nprint("GUARD SAW", *seen)\nsys.exit(1 if "%s" in seen else 0)\n' "$pl" > "$pk/guard.py"
git reset -q; echo 5 > "$pl"
out=$(git commit -qam g5 2>&1); rc=$?
case "$out" in *"GUARD SAW"*"$pl"*) r=$rc ;; *) r=0 ;; esac
ck "S1 a listed path committed by git commit -a, never added: refused by a guard that saw it" "$r" 1
git reset -q; echo 6 > "$pl"
out=$(git commit -qm g6 -- "$pl" 2>&1); rc=$?
case "$out" in *"GUARD SAW"*"$pl"*) r=$rc ;; *) r=0 ;; esac
ck "S1 a listed path committed by git commit -- <path>, never added: refused by a guard that saw it" "$r" 1
```

These lines go in directly after `:229`, the S21 arm, while `guard.py` is still absent:

```
# TOOL-dGroundRules-72: the same guard-less refusal for a listed path committed by path, never added.
git reset -q; echo 7 > "$pl"
out=$(git commit -qm g7 -- "$pl" 2>&1); rc=$?
case "$out" in *"no guard.py resolves"*) r=$rc ;; *) r=0 ;; esac
ck "S1 guard.py removed and a listed path committed by git commit -- <path>, never added: refused" "$r" 1
```

What the arms do not check: the real guard's verdict, which the policy kit's `guard-*` fixture cases
own (the comment at `:197` says so), and a commit made with `git commit -i`, which no probe here
measured.

### The floors

The suite prints its own pass and fail counts and pins no floor. It is a row of
`memory/project/testsuite-count-waivers.txt:5`. No floor or pinned count moves. The rows for both
files in `memory/project/spawn-idiom-sites.txt:19-23` count sites per idiom class. The new lines
hold no substitution of a pure function, a `printf`, a path or a piped variable, so by reading no
count moves. The close's run of the leg is what confirms it.

### Alternatives rejected

- Dropping `GIT_INDEX_FILE` from the unset at `:8`. Every later leg would then inherit the handed
  index, and a leg that runs git in a scratch repository would read it there. `TOOL-dScrubbedConduit-1`
  scrubs the location variables against that class (`:6-7`, with its reason at
  `.githooks/pre-push:87-99`).
- Exporting the saved index once for the whole block. The block would then hand it to every command
  it runs, the launcher's `ls-files` included, and the unset at `:8` exists to stop that.
- A change in `tools/policy/guard.py` to read the index itself. The guard has no way to learn which
  index git handed the hook once the hook has unset it.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.

### Files touched (estimate)

- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. The criteria use two scratch
scripts. `f72.sh` builds a scratch repository with the hook it is given, a committed list naming
`.governance/policy.toml`, and a stand-in guard that refuses only when its own staged read names that
path. It prints one line per commit: by `-a`, by path, by path with `guard.py` absent, and by
`git add`.

```
cat > "$TEMP/f72.sh" <<'EOF'
H="$1"; R=$(git ls-files -- '*resolve-python.sh' | head -n 1); D=$(mktemp -d)
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@example.com GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@example.com GOV_DEFAULT_BRANCH=main
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
cp "$R" "$D/r.sh"; cd "$D" && git init -q --template= -b main && mkdir hk policy vendor .governance && cp "$H" hk/pre-commit && mv r.sh vendor/resolve-python.sh && git config core.hooksPath hk
printf '.governance/policy.toml\n' > policy/guarded-paths.txt
printf 'import subprocess, sys\nseen = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True).stdout.split()\nprint("GUARD SAW", *seen)\nsys.exit(1 if ".governance/policy.toml" in seen else 0)\n' > policy/guard.py
echo base > .governance/policy.toml; git add -A; git commit -q --no-verify -m fixture
echo a > .governance/policy.toml; out=$(git commit -qam a 2>&1); echo "am rc=$? $(printf '%s\n' "$out" | grep -o 'GUARD SAW.*')"
git reset -q --hard; echo b > .governance/policy.toml; out=$(git commit -qm b -- .governance/policy.toml 2>&1); echo "path rc=$? $(printf '%s\n' "$out" | grep -o 'GUARD SAW.*')"
git reset -q --hard; rm policy/guard.py; echo c > .governance/policy.toml; out=$(git commit -qm c -- .governance/policy.toml 2>&1); echo "noguard rc=$? $(printf '%s\n' "$out" | grep -c 'no guard.py resolves')"
git reset -q --hard; echo d > .governance/policy.toml; git add .governance/policy.toml; out=$(git commit -qm d 2>&1); echo "staged rc=$? $(printf '%s\n' "$out" | grep -o 'GUARD SAW.*')"
cd / && rm -rf "$D"
EOF
```

`h72.sh` cuts the saved-index lines out of the hook it is given and sources them under four values
of `GIT_INDEX_FILE`: relative, a drive-letter path, a POSIX absolute path, and empty. It prints each
result with the current directory spelled `<cwd>`:

```
cat > "$TEMP/h72.sh" <<'EOF'
sed -n '/^hook_index=/,/^with_hook_index() /p' "$1" > "$TEMP/h72.src"
mkdir -p "$TEMP/x72" && cd "$TEMP/x72" || exit 2
for v in .git/index C:/r/.git/index /r/.git/index ''; do (GIT_INDEX_FILE=$v; . "$TEMP/h72.src"; printf '[%s] ' "${hook_index/#$PWD/<cwd>}"); done; echo
EOF
```

The hook's suite is a self-test this pass may not run. The main loop runs it at the close, and that
run prints an `ok` line for each of the three `S1` arms.

- **AC1** — When `bash "$TEMP/f72.sh" "$PWD/.githooks/pre-commit"` runs, it prints `am rc=1 GUARD SAW .governance/policy.toml`, then `path rc=1 GUARD SAW .governance/policy.toml`, then `noguard rc=1 1`, then `staged rc=1 GUARD SAW .governance/policy.toml`.
  At `fce5603f8` the first three lines were `am rc=0`, `path rc=0` and `noguard rc=0 0`.
  Red when: the block's first read misses the handed index. `sed 's/pg_hit=$(with_hook_index git/pg_hit=$(git/' .githooks/pre-commit > "$TEMP/b72a"` stages it, and over `"$TEMP/b72a"` the script prints `am rc=0` and `path rc=0`.
  Red also when the guard misses it. `sed 's/! with_hook_index "$py"/! "$py"/' .githooks/pre-commit > "$TEMP/b72b"` stages it, and the script prints `am rc=0 GUARD SAW` with no path.
  Red also when the `else` branch misses it. `sed 's/&& with_hook_index git diff/\&\& git diff/' .githooks/pre-commit > "$TEMP/b72c"` stages it, and the script prints `noguard rc=0 0`.
  All three breaks were measured on a prototype of §4's text.
  permission: the suite that will hold the arms is a self-test this pass may not run.
- **AC2** — When `bash "$TEMP/h72.sh" .githooks/pre-commit` runs, it prints `[<cwd>/.git/index] [C:/r/.git/index] [/r/.git/index] []`.
  At `fce5603f8` it printed `[] [] [] []`, since no such lines exist.
  Red when: the relative value is left as it is. `sed '/^case \$hook_index/d' .githooks/pre-commit > "$TEMP/b72d"` stages it, and over `"$TEMP/b72d"` the first field is `[.git/index]`.
  Red also when a drive-letter path is read as relative. `sed 's/\[A-Za-z\]:\*/\/\/\*/' .githooks/pre-commit > "$TEMP/b72e"` stages it, and the second field is `[<cwd>/C:/r/.git/index]`.
- **AC3** — When `grep -c '^ck "S1 ' .githooks/pre-commit.test.sh` runs, it prints `3`.
  At `fce5603f8` it printed `0`.
  Red when: an arm §4 gives is missing, or is named other than §4 names it, so the close's run of the
  suite does not stand for the three commits AC1 observes.

## 6. Gates

`branch-guard self-test` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `remote literals (kit code names no remote)` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: `.githooks/pre-commit.test.sh` · covers AC1 AC3 · the three `S1` arms §4 gives, each red against the hook at `fce5603f8` and green after S1 · none

The guards join owes no leg for either touched file. Run through `derive_guarded_legs`
(`tools/check-spec-tokens.py:589`) over `tools/gate-legs.json` at `fce5603f8`, it joined no leg for
`.githooks/pre-commit` or `.githooks/pre-commit.test.sh`. Their only guard is `.githooks/`, which
nine legs carry, over `BROAD_LEG_FLOOR = 5` (`:362`), so it is broad. `branch-guard self-test`
(`tools/gate-legs.json:605`) runs the suite S1 extends, so it is named for the new arms. The four
shell-hygiene scans read the hook as a tracked shell file, and `remote literals` reads every file
under `.githooks/`. `govkit selfcheck` and `kit epoch` read the hook as a file the push-main kit
claims. Those legs carry no guard and are named because the edit is in what they read. No floor or
pinned count moves (§4 "The floors").

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the closing review's finding B1 (id 1) and this unit's spec
  brief, grounded at `fce5603f8`. The premise was checked twice: by a stand-in hook that printed the
  handed index for five commit shapes, and by AC1's fixture against the real hook, with the stand-in
  guard and with `tools/policy/guard.py`. Follows the skeptic's SOUND fix, corrected on one point:
  a relative index is relative to the work tree top, not to the git dir, as the probe measured. Two
  follow-ups are for the main loop to file as asks, because neither is one arm of this mechanism.
  The first is the report's left-shift gate, a hook-lint leg that fails any `.githooks/*` block
  reading the index after the `GIT_INDEX_FILE` unset without the saved one, with a `-a` arm and a
  `<path>` arm owed by every staged-reading block in `.githooks/pre-commit.test.sh`. The second is
  the same defect in the hook's other staged legs §3 lists, for which `with_hook_index` is the seam
  and the backlog ask `TOOL-aTrimmedHook-8` the natural home. The brief's leg item
  names §6; in this Tier-1 shape the Gates section is §6, and the leg lines sit there. The review
  report and the brief, both untracked when this draft was written:

```
memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-72-spec-brief.md
```

- rev-2 · 2026-10-25 · the two follow-ups move from §7 into the rev-1 entry as prose, so §7 reads
  `none` and check 12 grades no bullet outside an F-item at the CLOSED flip; §3 points at them there.

## 9. Reuse audit

The seam is the index-carrying pattern that `read_staged_paths` and `check_staged_render` already use
(`tools/memory-tree/gen_build_index.py:961-967` and `:995-1002`): run the staged read with the
`GIT_INDEX_FILE` git handed the hook, and leave every other git call scrubbed. S1 applies it in the
hook's shell, where the policy guard's reads start, and builds no second mechanism. The guard needs
no change because `run_git` (`tools/policy/guard.py:46`) already carries the environment. The arms
reuse the suite's own policy-guard fixture at `.githooks/pre-commit.test.sh:198-205` and its `ck`
helper (`:19-23`).
`python tools/codebase-map/reuse_lookup.py "carry the index git handed a hook into a staged read after the hook scrubs GIT_INDEX_FILE"`
ranked only name stems (`read`, `git`, `run_git`), and none of them carries a hook's index in shell.
The recall probe returned the closing review and this unit's brief, the earlier finding of the same
class in `TOOL-aTrimmedHook-1`'s closing review, the backlog ask `TOOL-aTrimmedHook-8`, and the
gotcha `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md`, which measured the same
relative and `next-index` values.

Recall terms used: `python tools/memory-recall/query.py "pre-commit hook temporary index git commit -a staged read bypass" --terms "GIT_INDEX_FILE next-index index.lock read_staged_paths policy guard"`
