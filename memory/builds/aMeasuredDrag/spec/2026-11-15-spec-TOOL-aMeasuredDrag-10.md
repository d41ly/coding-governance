# TOOL-aMeasuredDrag-10 — `.githooks/pre-commit` reads the staged list once and resolves python once, each leg keeping its own trigger

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-1 · base aebbb4a7 · streams tooling · order 10 · advances TOOL-aTrimmedHook-8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aMeasuredDrag-1-runlog-6d98c39c.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-runlog-6d98c39c.md) | journal | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-11 TOOL-aMeasuredDrag-12 |
| [2026-11-15-build-TOOL-aMeasuredDrag-10-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-10-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-10-1-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-10-1-builder.md) | journal | — |
| [2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md](../reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md) | diff-review | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-11 |

<!-- /gen:spec-records -->

## 1. Goal

Every commit runs `.githooks/pre-commit`, and the hook runs `git diff --cached` five times to answer
one question per leg, and resolves the python launcher up to three times (finding spawns-9 of the
2026-11-15 performance review). This unit reads the staged list once per index and resolves the
launcher once per hook run, so each leg's trigger is a shell match against one list. Every leg
still reads the index it reads today, and no verdict, refusal or printed line moves.

## 2. Scope (IN)

- **S1** — One staged read of the real index, `git diff --cached --name-status --no-renames`,
  placed above the policy guard. One `while read` loop over it fills `st_names` and four trigger
  flags, `st_memory`, `st_wiring`, `st_template` and `st_map`, with the patterns of §4 "The
  triggers". Observed by AC1 and AC2.
- **S2** — The memory hygiene leg, the unattended wiring leg, the template size leg and the
  codebase-map leg test their flag instead of running `git diff --cached`
  (`.githooks/pre-commit@468b13e420e3:228`, `:265`, `:274`, `:298`). Observed by AC1 and AC2.
- **S3** — A function `read_hook_staged` gives the policy guard the names staged in the index git
  handed the hook. Where that index is the real one, it prints `st_names` and spawns nothing;
  otherwise it runs the guard's read as today. Both guard reads call it (`:204`, `:220`). Observed
  by AC1 and AC2.
- **S4** — A function `resolve_hook_python` sources the tracked resolver and runs `resolve_python`
  at the first leg that needs a launcher, keeps a success in `hook_py`, and sets `py` from it. The
  three resolution sites call it (`:207-210`, `:242-243`, `:300-304`), and their `pg_r`, `rf_r` and
  `r` lookups go. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- Which index a leg reads. The four legs of S2 read the real index and the policy guard reads the
  one git handed the hook (TOOL-dGroundRules-72). Under `git commit -a` or `git commit <path>` the
  two differ, and a memory edit committed that way does not trigger the hygiene leg today. The
  probe's `commit-all` and `commit-only` cases show it. Pointing the legs at the handed index would
  move that verdict, so it stays.
- The straggler guard, `resolve_kit_gate`'s receipt read, and the ask's 30 s target (PINNED in
  the ask). They are the other two clauses of `TOOL-aTrimmedHook-8`, which this unit advances and
  does not close.
- Printing only a leg's non-`ok` lines, which the review's row 30 also names. The brief's item 10
  does not.
- The `govkit:branch-guard` region (`:25-94`), which govkit emits. No line inside it moves.
- `tools/lib/resolve-python.sh`, its inline copies, and `GOV_PYTHON` handling. That is unit 11's
  ground (`TOOL-aMeasuredDrag-11`), and this hook is not a bar leg.
- Any help page. The pages under `help/` that name the hook describe what it refuses, which does not
  move (grep, 2026-11-15).

## 4. Design

### Evidence

Read at `6d98c39ca`. The hook and the resolver are byte-identical at the base `aebbb4a7`.

- The policy guard reads the handed index through `with_hook_index`, with `--name-only
  --no-renames` (`.githooks/pre-commit@468b13e420e3:9-11`, `:204`, `:220`). Its two reads sit in
  exclusive branches, so it runs at most one.
- The other four reads run after `GIT_INDEX_FILE` is unset (`:15`), so they read the real index:
  `--diff-filter=ACMR -- 'memory/**'` (`:228`), three pathspecs (`:265`), one path (`:274`), and
  `'*.py' '*.js'` (`:298`). Each only asks whether its answer is empty (`grep -q .`).
- Python is resolved at `:210` (policy guard, not at a terminal), `:243` (red-fix join, no memory
  path staged) and `:304` (codebase-map leg). Each first runs `git ls-files -- '*resolve-python.sh'`
  and sources the result.
- `resolve_python` prints its diagnosis to stderr only when no candidate runs
  (`tools/lib/resolve-python.sh@9ec71b5b6b9c:66-78`). It defines a function and runs nothing when
  sourced.
- Between the reads the hook runs only checks. A grep of the hygiene gate, the manifest check, the
  wiring adopter, the template size check, the policy guard and the red-fix join for an
  index-writing git verb found none outside a self-test's temporary repository (2026-11-15). So one
  read taken above them sees the list each later read saw.
- `gd` is set at `:75`, outside any branch, from `git rev-parse --path-format=absolute --git-dir`.
  The real index is `$gd/index`.

### What git was measured to do

Measured on 2026-11-15 with git for Windows in a scratch repository under `%TEMP%`:

- With a pathspec, git limits the paths before it pairs renames. A rename of `a.py` to `b.txt`
  answers `a.py` to `git diff --cached --name-only -- '*.py'`, and `--no-renames` lists it as
  `D a.py` and `A b.txt`. So "the old read is non-empty" equals "a line of the one read matches",
  for every pathspec this hook uses.
- `--diff-filter=ACMR` keeps renamed and copied paths under their new names. With `--no-renames`
  those are `A` lines, so `[AM]` with the `memory/` prefix selects the same paths.
- A non-ASCII name prints C-quoted in both forms, for example `"memory/caf\303\251.md"`. The
  quoted spelling keeps every ASCII character but `"` and `\` as it is.
- On a plain `git commit` git hands the hook `GIT_INDEX_FILE` spelled with the 8.3 short path,
  while `rev-parse` prints the long one, so the strings differ and `[ "$hook_index" -ef "$gd/index" ]`
  is true. Under `git commit -a` it hands `index.lock`, and under `git commit -- <path>` a
  `next-index-<pid>.lock`, and `-ef` is false. A linked worktree behaves the same way under its
  own `worktrees/<name>/index`.

### The triggers

`st_bare` is the path with one leading and one trailing `"` removed when it carries both. The
policy guard reads `st_names`, which keeps git's spelling, because its `grep -xF` matched that
spelling before.

| Leg | Today | Flag set when |
|---|---|---|
| memory hygiene (`:228`) | `--diff-filter=ACMR -- 'memory/**'` | status `A` or `M`, and `st_bare` matches `memory/*` |
| unattended wiring (`:265`) | `-- .unattended.conf '*SKILL.template.md' .claude/skills/unattended/SKILL.md` | `st_bare` matches either literal, or either literal followed by `/*`, or `*SKILL.template.md` |
| template size (`:274`) | `-- coding-governance-agents.template.md` | `st_bare` is that path, or that path followed by `/*` |
| codebase-map (`:298`) | `-- '*.py' '*.js'` | `st_bare` matches `*.py` or `*.js` |

A git pathspec with no magic is case-sensitive, a `*` in it matches `/`, and a literal one also
matches the paths under it as a directory. A shell `case` pattern is case-sensitive and its `*`
matches `/`, so the table's `/*` forms carry the directory rule.

### The code

Inserted after `print_kit_miss` (`:184`), above the policy guard's comment:

```bash
st_list=$(git diff --cached --name-status --no-renames)
st_names="" st_memory="" st_wiring="" st_template="" st_map=""
while IFS=$'\t' read -r st_status st_path; do
  [ -n "$st_path" ] || continue
  st_names+=$st_path$'\n'
  st_bare=$st_path; case $st_bare in \"*\") st_bare=${st_bare#\"}; st_bare=${st_bare%\"} ;; esac
  case $st_status:$st_bare in [AM]:memory/*) st_memory=1 ;; esac
  case $st_bare in .unattended.conf|.unattended.conf/*|*SKILL.template.md|.claude/skills/unattended/SKILL.md|.claude/skills/unattended/SKILL.md/*) st_wiring=1 ;; esac
  case $st_bare in coding-governance-agents.template.md|coding-governance-agents.template.md/*) st_template=1 ;; esac
  case $st_bare in *.py|*.js) st_map=1 ;; esac
done <<< "$st_list"
read_hook_staged() { # the names staged in the index git handed this hook (TOOL-dGroundRules-72)
  if [ -z "$hook_index" ] || [ "$hook_index" -ef "${gd:-}/index" ]; then printf '%s' "$st_names"
  else with_hook_index git diff --cached --name-only --no-renames; fi
}
hook_py=""
resolve_hook_python() { # -> py; rc 1 when no tracked resolver or no usable launcher
  local r p
  if [ -z "$hook_py" ]; then
    r=$(git ls-files -- '*resolve-python.sh' | head -n 1)
    [ -n "$r" ] && . "./$r" && p=$(resolve_python) || return 1
    hook_py=$p
  fi
  py=$hook_py
}
```

The builder adds a comment above the block naming this unit, the one-read rule, the quoting rule
and the `-ef` reason, in the hook's own style. The call sites become:

| Line | Becomes |
|---|---|
| `:204` | `[ -z "$pg_list" ] \|\| pg_hit=$(read_hook_staged \| grep -xF -- "$pg_list" \|\| true)` |
| `:207`, `:210` | the `pg_r` line goes; `elif ! resolve_hook_python; then` |
| `:220` | `if [ -n "$pg_list" ] && read_hook_staged \| grep -qxF -- "$pg_list"; then` |
| `:228` | `if [ -n "$st_memory" ]; then` |
| `:242-243` | the `rf_r` line goes; `if ! resolve_hook_python; then` |
| `:265` | `if [ -n "$st_wiring" ]; then` |
| `:274` | `if [ -n "$st_template" ]; then` |
| `:298` | `if [ -f .codebase-map.conf ] && [ -n "$st_map" ]; then` |
| `:300`, `:304` | the `r` line goes; `elif ! resolve_hook_python; then` |

Only a success is kept. A failed resolution resolves again at the next leg, so its stderr prints
there exactly as it did. `${gd:-}` keeps `set -u` from aborting if `gd` is ever unset; `-ef` then
reads false and the guard takes its own read, which costs a spawn and never moves a verdict.

### The probe

The builder saves this as `u10probe.sh` under the run's scratchpad and runs it from the worktree root,
with `<hook>` the hook to measure, `<fixture>` a short path under `%TEMP%` (the clone rule), and
`<out>` a folder under the scratchpad. Every leg is a stand-in at a root install that prints that it
ran. Each case stages a set, commits through the hook, and records the output, the exit status, the
`git diff --cached` count from `GIT_TRACE`, and the resolution count from a `GOV_PYTHON` wrapper,
which logs every argv and `resolve_python` echoes as given.

```bash
#!/usr/bin/env bash
set -u
hook=$1 fx=$2 out=$3 src=$PWD
rm -rf "$fx" "$out"; mkdir -p "$fx" "$out"
. "$src/tools/lib/resolve-python.sh"; realpy=$(resolve_python) || exit 2
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@e GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@e
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
export GOV_DEFAULT_BRANCH=main
cd "$fx" || exit 2
git init -q --template= -b main
mkdir -p hk memory-tree unattended policy .governance vendor gate map/generated memory src
cp "$hook" hk/pre-commit; chmod +x hk/pre-commit; git config core.hooksPath hk
cp "$src/tools/lib/resolve-python.sh" vendor/
printf '#!/usr/bin/env bash\necho "HYGIENE RAN $*"\n' > memory-tree/check-memory-hygiene.sh
printf 'import sys\nprint("JOIN RAN", *sys.argv[1:])\n' > memory-tree/build_records.py
printf '#!/usr/bin/env bash\necho "MANIFEST RAN $*"\n' > manifest-check.sh
printf '#!/usr/bin/env bash\necho "WIRING RAN $*"\n' > unattended/adopt-unattended.sh
printf '#!/usr/bin/env bash\necho "TEMPLATE RAN $*"\n' > check-template-size.sh
printf 'print("ok   map")\nprint("MAP RAN")\n' > gate/map.py
printf 'MAP_ROOT=map\nGATE_FILE=gate/map.py\n' > .codebase-map.conf
printf 'import sys\nprint("GUARD RAN", *sys.argv[1:])\n' > policy/guard.py
printf '.governance/policy.toml\n' > policy/guarded-paths.txt
echo base > .governance/policy.toml; echo '{}' > map/generated/x.json
printf 'a\n' > memory/a.md; printf 'x = 1\n' > a.py; echo 0 > src/app.txt
git add -A; git commit -q --no-verify -m base; base=$(git rev-parse HEAD)
wrap=$out/pywrap; pylog=$out/py.log
printf '#!/usr/bin/env bash\nprintf "%%s\\n" "$*" >> "%s"\nexec "%s" "$@"\n' "$pylog" "$realpy" > "$wrap"
chmod +x "$wrap"; export GOV_PYTHON=$wrap
trace=$out/trace.log
run_case() { # <name> <commit argv...>; the staged set is already in place
  local name=$1; shift
  : > "$trace"; : > "$pylog"
  local o rc; o=$(GIT_TRACE=$trace git commit -q --allow-empty-message -m "$name" "$@" 2>&1); rc=$?
  printf '== %s rc=%s\n%s\n' "$name" "$rc" "$o" >> "$out/transcript.txt"
  printf '%s diff-cached=%s py-resolutions=%s\n' "$name" \
    "$(grep -c 'built-in: git diff --cached' "$trace")" "$(grep -c '^-I -c' "$pylog")" >> "$out/counts.txt"
  git reset -q --hard "$base"; git clean -qfd -e hk
}
echo 1 > src/app.txt; git add src/app.txt; run_case plain-product
echo n > memory/n.md; git add memory/n.md; run_case memory-added
git rm -q memory/a.md; run_case memory-deleted
git mv memory/a.md memory/b.md; run_case memory-renamed-within
mkdir -p out; git mv memory/a.md out/a.md; run_case memory-renamed-out
echo c > "memory/café.md"; git add -A memory; run_case memory-non-ascii
git mv a.py a.txt; run_case py-renamed-away
echo 'f()' > e.js; git add e.js; run_case js-added
echo 'X=1' > .unattended.conf; git add .unattended.conf; run_case unattended-conf
mkdir -p deep/x; echo s > deep/x/SKILL.template.md; git add deep; run_case skill-template
echo t > coding-governance-agents.template.md; git add coding-governance-agents.template.md; run_case charter-template
echo 1 > .governance/policy.toml; git add .governance/policy.toml; run_case policy-path
echo 2 > .governance/policy.toml; echo 'y = 2' > b.py; git add -A; run_case policy-py-no-memory
echo 3 > .governance/policy.toml; echo b >> memory/a.md; run_case commit-all -a
echo c >> memory/a.md; run_case commit-only -- memory/a.md
rm -rf "$fx"
```

Run on 2026-11-15 over the hook at `6d98c39ca`, twice, it wrote byte-identical transcripts and
counts. Every case counted `diff-cached=5`, and `py-resolutions` read 0 to 3, with 3 on
`policy-py-no-memory`. The whole run took 50.2 s real on node a (PINNED, 2026-11-15). The
transcript shows the hygiene leg run on `memory-added`, `memory-renamed-within` and
`memory-non-ascii`, and not on `memory-deleted`, `memory-renamed-out`, `commit-all` or
`commit-only`.

The writer applied §4 "The code" and the call-site table to a scratch copy of that hook on the
same day, before writing the spec. Its transcript was byte-identical, its counts were the ones
AC2 and AC3 name, and the run took 46.0 s real beside a 0.39 s baseline (PINNED, node a, one run).

### What this does not check

- A staged read git itself refuses. Its error prints once where up to five reads each printed it.
  The legs' flags stay empty, as each failed read's answer was, so no verdict moves. No case
  reaches it.
- A path whose own name holds a glob character or a quote at a pattern's edge. Shell and pathspec
  agree on the spellings the probe stages, and the probe stages none of those.
- `core.quotePath=false`. Then a non-ASCII name prints bare and matches directly, and the probe
  runs under the default.

### Files touched (estimate)

- `.githooks/pre-commit`

## 5. Acceptance criteria

All commands run from the worktree root in Git Bash. The builder saves the hook as the pass's
parent holds it with `git show HEAD:.githooks/pre-commit`, before the commit, and runs the §4 probe
once over that copy and once over the edited `.githooks/pre-commit`, into two `<out>` folders.

- **AC1** — When `cmp` compares the two probe runs' `transcript.txt`, it prints nothing and exits 0:
  every case's output and exit status are byte-identical, the `commit-all` and `commit-only` cases
  included.
  Red when: a trigger pattern differs from its pathspec, for instance `[ADM]` for the memory leg,
  so `memory-deleted` runs the hygiene leg. Or the policy guard reads `st_names` under `git commit
  -a`, so `commit-all` runs no guard.
- **AC2** — When the edited hook's `counts.txt` is read, every case shows `diff-cached=1`, except
  `commit-all` and `commit-only`, which show `diff-cached=2`.
  Red when: `read_hook_staged` compares the two index paths as strings, so every plain commit
  shows `diff-cached=2`; or a leg keeps its own read.
  figure: PINNED for the parent hook: `diff-cached=5` on all 15 cases, at `6d98c39ca` on
  2026-11-15.
- **AC3** — When the edited hook's `counts.txt` is read, no case shows `py-resolutions` above 1, and
  every case the parent hook counted at 0 still shows 0.
  Red when: `resolve_hook_python` does not keep `hook_py`, so `policy-py-no-memory` shows 3.
  figure: PINNED for the parent hook: 3 on `policy-py-no-memory`, 2 on four cases, at `6d98c39ca`
  on 2026-11-15.
- **AC4** — When each probe run is timed with `time bash` beside
  `time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)` in the same shell, the builder
  records the two probe readings and the baseline in the acceptance ledger.
  Red when: the edited hook's run is not faster than the parent's by more than the baseline.
  figure: PINNED, 2026-11-15 at `6d98c39ca` on node a: parent hook 50.2 s for 15 commits.
  Baseline 0.35 s real, PINNED the same day.

## 6. Gates

`branch-guard self-test` · `straggler-guard arms` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates`

`python tools/check-spec-tokens.py --legs-for .githooks/pre-commit`, run on 2026-11-15 at
`6d98c39ca`, names only broad guards. The legs above drive this hook or read it: its own suite
commits through it, the straggler guard's arms commit through it, the resolver leg bans launcher
idioms in tracked shell, and the lexicon leg grades the two new function names. The main loop runs
them; this pass runs none. No arm is added or moved.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-15 · initial draft from the build brief
  `2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief`, item 10, grounded at `6d98c39ca`. The brief asks
  for one read; the policy guard's handed index differs from the real one under `git commit -a`
  and `git commit <path>`, so the design reads once where the two are one file and twice where
  they are not.

## 9. Reuse audit

The seams are the hook's own: the trigger tests are edited in place, `read_hook_staged` wraps the
existing `with_hook_index` read, and `resolve_hook_python` wraps the tracked resolver
`tools/lib/resolve-python.sh#resolve_python` that all three sites already source.
`python tools/codebase-map/reuse_lookup.py "read the staged file name list once in a commit hook"`
ranked name stems only (`read_text`, `read`, `read_git_output`), none of them a shell staged-list
reader, so no existing seam fits beyond the hook. The codebase map does not index the hook, which
has no extension. Recall returned `TOOL-aTrimmedHook-8`, whose first accept clause this unit
delivers, and `TOOL-dGroundRules-72`, which set the policy guard's handed-index rule kept here.

Recall terms used: `python tools/memory-recall/query.py "why does the pre-commit hook read the staged list through the hook's own index" --terms "pre-commit hook_index with_hook_index GIT_INDEX_FILE staged diff cached resolve_python policy guard commit -a"`
