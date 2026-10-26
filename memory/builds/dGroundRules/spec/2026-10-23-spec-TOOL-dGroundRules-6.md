# TOOL-dGroundRules-6 — the minimal guard over the policy file and its three neighbours

**Status:** CLOSED · rev-3 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dGroundRules-12

**Carries:** cl-dClosedLoop-0012@937c308e whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-6-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-6-ledger.md) | journal | — |
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 |
| [2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 |
| [2026-10-23-prompt-TOOL-dGroundRules-6-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-6-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-6-span-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-6-span-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-1-close-arms-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-1-close-arms-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-7 TOOL-dGroundRules-8 |
| [2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-1 TOOL-dGroundRules-11 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-10 TOOL-dGroundRules-9 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

Once policy lives in `.governance/policy.toml`, an agent that can commit a change to it can loosen
any rule, and dDeclaredLoop's guard, the one that reads `policy-file.guard` and `policy-file.proof`,
lands builds later. This unit is the stand-in until then: a commit-time guard that enforces those
two keys' defaults, owner-only and the TTY proof, without reading either key. It refuses an agent's
commit touching the policy file, its JSON mirror, the instruction manifest
`.governance/instructions.toml` or `.governance/deploy.toml`, and admits one agent shape: a single
measured-file cap under `budgets.*` raised, nothing else changed, with its change record attached,
which at this build is today's rule from `tools/template-size-limits.txt`, the RAISED argument in
place beside the cap and a `memory/DECISIONS.md` row in the same commit.

## 2. Scope (IN)

- **S1** — `tools/policy/guarded-paths.txt`, the one spelling of the guarded set: the four paths
  above, one per line, `#` comments allowed. Observed by AC11.
- **S2** — `tools/policy/guard.py --staged`, the verdict over the staged change. It reads the list
  at HEAD, intersects it with the staged paths, and admits when nothing guarded is staged, when each
  guarded path's staged blob equals its blob in a parent of the commit being concluded, or when the
  change is the one admitted shape of S3; it refuses every other change, naming each failed
  condition. It reads neither `policy-file.guard` nor `policy-file.proof`. Observed by AC1 to AC8,
  AC10.
- **S3** — The admitted shape: only `.governance/policy.toml` among the guarded paths changed;
  exactly one leaf differs between HEAD's table and the staged one, present on both sides, under
  `budgets`, neither `budgets.enforce` nor `budgets.pinned` nor under them, its last segment the
  path of a file tracked at HEAD, its value an integer that grew; the text change is that one line
  plus comment lines added directly above it, one carrying `RAISED <old> -> <new>`; and
  `memory/DECISIONS.md` is staged with at least one row added and every row HEAD holds kept.
  Observed by AC1 to AC7.
- **S4** — The hook seam: a block in `.githooks/pre-commit` beside the staged legs. When a guarded
  path is staged it admits on the owner's terminal proof, stderr being a terminal, and otherwise runs
  S2, refusing the commit on any exit but 0, a missing Python launcher included. Observed by AC9.
- **S5** — The guard's fixture cases in `tools/policy/check_policy.py`, one per admitted and refused
  shape the clause lists, each with its stated outcome. Observed by AC1 to AC8.
- **S6** — A section of `help/policy.md`, "Who may change the policy file": the four paths, the
  owner's terminal, the one agent shape with a worked example, and what the guard does not catch.
  Observed by AC12.

## 3. Non-goals (OUT)

- dDeclaredLoop's guard, its TTY CLI and its guarded policy command, which read `policy-file.guard`
  and `policy-file.proof` and replace this guard when they land; until then this guard is the
  enforcement and no key changes it.
- dOrderedCharter's instruction change-record kind. The change record here is today's rule, the
  RAISED argument and the decision row, until that kind lands and re-points it.
- The other conditions of `tools/template-size-limits.txt`, that the unit's own change takes the
  file past the cap and that the row's comment does not reserve its next movement: they are left to
  the record's argument, as today.
- A harness-level refusal at the tool call. An agent's working-tree edit of a guarded file is read
  by nothing, since the reader and the mirror's helper read landed revisions; the commit is the act.
- Adopter wiring. The block is gov's own pre-commit, and the runbook's copy instructions do not
  change.
- Moving any cap under `budgets.*`. dSafePassage's step does that; at this build the admitted shape
  is reached by the fixture alone.

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — the kit `tools/policy/`, its `kit.toml` file rows, `check_policy.py` with `CASES`, its `--fixture` mode and the policy leg, and the help page `help/policy.md`
- **hands-off** `TOOL-dGroundRules-9` — the spelling the admitted shape reads: a measured-file cap is a leaf under `budgets` whose last key segment is the measured file's repo-relative path and whose value is an integer
- **hands-off** external — dDeclaredLoop's guard, which reads `policy-file.guard` and `policy-file.proof`, admits the same raise through its guarded policy command, and retires this block
- **hands-off** `TOOL-dGroundRules-19` — the admission of a regenerated mirror equal to its render at HEAD, which replaces this unit's F6 pick once the render exists (finding 32)
- **hands-off** `TOOL-dGroundRules-21` — the hook block's kit-miss refusal and the guard cases' slashed and class keys (findings 25, 56)

## 4. Design

### Evidence

- No guard exists over `.governance/`. The files under `tools/` and `.githooks/` that name
  `.governance/deploy.toml` read it as the deployer's answers, and none refuses a write to it
  (`git grep -l "governance/deploy.toml" -- tools .githooks`, read 2026-10-23); `.governance/` holds
  `deploy.toml` alone at base.
- Today's rule: "a run may RAISE a measured-file row, in the commit of a unit of a build the owner
  mandated", argued in place as "RAISED <old> -> <new>", with the unit's row in `memory/DECISIONS.md`
  "before or with the raise"; "A class row, a lowering, a new row and a removal stay the owner's"
  (`tools/template-size-limits.txt:16-24`).
- The owner's FK-9-2, option (a): the minimal guard "admits that one write shape: a single
  measured-file cap raised, nothing else changed, with a change record attached. The other conditions
  are left to the record's argument"
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w9.md:55-58`).
- v2's `[witnesses]`: `tty-cli` "proves owner presence against a cooperative agent only", and the
  owner accepts the pty-wrapper threat for now (SA-1).
- The pre-commit hook resolves a kit file by its ladder, `resolve_kit_gate`
  (`.githooks/pre-commit:167`), finds the tracked Python resolver as the codebase-map leg does
  (`.githooks/pre-commit:235`), and treats a kit miss as an announced skip because its legs are "an
  early signal" (`.githooks/pre-commit:145`). Gov's kit root is `GOV_KITROOT=tools`
  (`.githooks/gate-env.sh:90`).
- The active hooks are the primary tree's: this worktree's `core.hooksPath` names
  `C:\projects\coding-governance\.githooks`, read with `git config --show-origin core.hooksPath`.
- The lander never fires pre-commit: `--prepare` writes the merge with `commit-tree`
  (`tools/push-main.sh:921`, the reason at `:900`) and the attended path commits with `--no-verify`
  (`tools/push-main.sh:1111`).
- An agent's shell has no terminal: on 2026-10-23, from this run's shell, `[ -t 0 ]`, `[ -t 1 ]`
  and `[ -t 2 ]` were all false and `/dev/tty` did not open.

### The verdict

`guard.py --staged`, run from the repository's top level, in one order:

1. The list: `git show HEAD:<kit>/guarded-paths.txt`, `<kit>` being `guard.py`'s directory relative
   to the top level, CR stripped, comments and blank lines dropped. Absent at HEAD: exit 0, nothing
   is guarded yet. A git failure: exit 2.
2. The touched set: `git diff --cached --name-only --no-renames HEAD` intersected with the list
   (with no HEAD, every staged path). Empty: exit 0, silently.
3. The parent rule: when `MERGE_HEAD` resolves, a touched path whose staged blob equals its blob at
   HEAD or at `MERGE_HEAD` leaves the set, because a merge taking a side writes nothing new. The
   set emptied: exit 0.
4. The shape: the set must be exactly `.governance/policy.toml`, modified, and S3's conditions must
   hold over `git show HEAD:.governance/policy.toml` and `git show :.governance/policy.toml`.
   - Both parse with `tomllib`, else "the policy file does not parse".
   - Flattened to leaf key tuples, exactly one tuple differs, present on both sides, else
     "N keys changed", "a key was added" or "a key was removed".
   - That tuple starts with `budgets` and is not `("budgets", "enforce")` or `("budgets", "pinned")`
     or under them, else "only a cap under budgets.* may be raised".
   - Its last segment names a file tracked at HEAD (`git cat-file -e HEAD:<segment>`), else "not a
     measured-file cap: a class row or no file", which covers a class label such as
     `memory/builds/*/spec/`.
   - Both values are integers, booleans excluded, and the new one is larger, else "a lowering" or
     "not a count".
   - Over the CR-stripped lines, `difflib`'s non-equal opcodes cover one old line and, on the new
     side, zero or more comment lines followed by one non-comment line, and nothing else, else
     "another line of the policy file changed".
   - One of those added comment lines matches `RAISED\s+<old>\s*->\s*<new>\b` with the two values,
     else "no RAISED <old> -> <new> argument above the cap".
5. The record: `git diff --cached -U0 HEAD -- memory/DECISIONS.md` adds at least one line opening
   `- ` and removes none, else "no memory/DECISIONS.md row in this commit".
6. Every condition met: exit 0, printing
   `policy-guard: admitted · budgets.<cap> <old> -> <new> · its change record attached`. Otherwise
   exit 1, printing every failed condition, each as `policy-guard: refused · <path> · <why>`, then
   one remedy line: an agent may raise one measured-file cap in this shape; any other change to these
   files is the owner's, committed from a terminal.

The mirror has no exception of its own. An agent's commit of `.governance/policy.json` is refused
even when it equals the render; the landing renders and commits it with no hook firing
(`TOOL-dGroundRules-5`), and the refusal's remedy line says so for that path:
`git restore --staged --worktree .governance/policy.json`.

"Nothing else changed" is read over the guarded set: other files may ride in the same commit,
because today's rule puts the raise in the commit of the unit whose change needed it (§8 F4).

### The hook block

Placed after `print_kit_miss` (`.githooks/pre-commit:174`) and before the memory-tree leg
(`.githooks/pre-commit:179`), so a refused commit is told before paying for the legs:

```bash
# policy guard (TOOL-dGroundRules-6) — the minimal guard over the paths the policy kit's
# guarded-paths.txt lists at HEAD: owner-only and the TTY proof, enforced without reading
# policy-file.guard or policy-file.proof, until dDeclaredLoop's guard lands.
if g=$(resolve_kit_gate policy guard.py); then
  pg_hit=<the staged names, --no-renames, that appear in "HEAD:${g%guard.py}guarded-paths.txt">
  if [ -n "$pg_hit" ]; then
    if [ -t 2 ]; then
      echo "pre-commit: policy guard — <paths> staged, admitted on the owner's terminal proof."
    elif <the tracked resolver yields no launcher>; then
      echo "pre-commit: policy guard REFUSING — <paths> staged and no python launcher to judge them."
      rc=1
    elif ! "$py" "$g" --staged; then
      rc=1
    fi
  fi
fi
```

Git sends a hook's stdout to stderr and leaves stderr as the caller's, so `[ -t 2 ]` reads whether
the committer sits at a terminal. The guard runs only when a guarded path is staged, so an ordinary
commit spawns no Python. A kit that resolves nowhere means no list exists to guard, and the block
prints nothing. A missing launcher refuses rather than skips, because this block is the enforcement
and not an early signal (§8 F7).

### What escapes it

It stops forgetting, not evasion, and says so in its header comment. `git commit --no-verify`; a pty
wrapper that gives an agent's commit a terminal, the threat the owner accepted (SA-1); a list line
removed in one commit and the file changed in the next; a commit made on another clone; a
cherry-pick or rebase, which fire no pre-commit; and a guard file deleted from the working tree,
since the hook resolves the kit there. The push-time bar does not re-judge authorship.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `read_guarded_paths`, `read_touched_paths`, `check_parent_sides` | function | `tools/policy/guard.py` |
| `check_raise_shape`, `check_decisions_row`, `derive_leaf_changes`, `main` | function | `tools/policy/guard.py` |
| `--staged` | CLI flag | `tools/policy/guard.py` |
| `guarded-paths.txt` | data file | `tools/policy/` |
| `guard-admits-raise`, `guard-lowered`, `guard-two-raised`, `guard-class-row` | `CASES` entries | `tools/policy/check_policy.py` |
| `guard-beside-change`, `guard-beside-path`, `guard-no-record`, `guard-no-argument`, `guard-no-row` | `CASES` entries | `tools/policy/check_policy.py` |
| `guard-other-paths`, `guard-new-row`, `guard-removed-row`, `guard-merge-side` | `CASES` entries | `tools/policy/check_policy.py` |

Each function leads with a verb `.lexicon.conf` declares, in `py.function`'s snake case. The policy
kit's version marker moves with this unit.

### The cases

Each case builds a repository from the fixture `TOOL-dGroundRules-1` gives every case, adds
`guard.py`, the list, a tracked `big.md` and `small.md`, a `memory/DECISIONS.md` and a policy file
whose `[budgets]` table sets `"big.md" = 100`, `"small.md" = 50` and `"docs/*/" = 10`, commits, then
stages its plant and runs `guard.py --staged`. The admitted plant raises `big.md` to 120 with
`# RAISED 100 -> 120, 2026-10-23, TOOL-x-1, measured 118 bytes` directly above it and adds one
decision row.

| Case | Plant | Outcome |
|---|---|---|
| `guard-admits-raise` | the admitted plant | exit 0; a refusal is RED |
| `guard-lowered` | `big.md` to 90, argument and row present | exit 1, "a lowering" |
| `guard-two-raised` | `big.md` and `small.md` raised, each argued, one row | exit 1, "2 keys changed" |
| `guard-class-row` | `docs/*/` raised, argued, row present | exit 1, "not a measured-file cap" |
| `guard-beside-change` | the admitted plant and `budgets.enforce` set to `refuse` | exit 1, "2 keys changed" |
| `guard-beside-path` | the admitted plant and a line added to `.governance/deploy.toml` | exit 1, naming `.governance/deploy.toml` |
| `guard-no-record` | the raise with neither the argument nor the row | exit 1, naming both |
| `guard-no-argument` | the raise and the row, no argument | exit 1, "no RAISED" |
| `guard-no-row` | the raise and the argument, no row | exit 1, "no memory/DECISIONS.md row" |
| `guard-other-paths` | each alone: the mirror rewritten, `.governance/instructions.toml` added, `.governance/deploy.toml` changed | exit 1 for each |
| `guard-new-row` | `"new.md" = 10` added, argued, row present | exit 1, "a key was added" |
| `guard-removed-row` | `small.md` removed, row present | exit 1, "a key was removed" |
| `guard-merge-side` | a conflicted merge of a branch whose policy file differs, concluded with the branch's side, then with a third text | exit 0, then exit 1 |

### Rollout

The guard binds once it is landed and the primary tree's checkout carries it, because every worktree
runs the primary tree's hooks. This build's later units therefore commit under main's hook as it is
at base, and the guard's first real refusal is in the next build. It shares
`tools/policy/check_policy.py` and `tools/policy/kit.toml` with `TOOL-dGroundRules-5`, so the two
passes sequence, by M6 clause 1, despite their shared order.

### Files touched (estimate)

- `tools/policy/guard.py`
- `tools/policy/guarded-paths.txt`
- `tools/policy/check_policy.py`
- `tools/policy/kit.toml`
- `tools/policy/README.md`
- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`
- `help/policy.md`
- `memory/map/generated/symbols.json`
- `memory/map/generated/inventories.json`

### Alternatives rejected

- **A verb on `policy.py`.** The guard reads no policy, and keeping it out of the reader's module is
  what makes "without reading either key" checkable by a grep (AC10).
- **The guard in the PreToolUse hook beside the scratch guard's write gate.** It sees a tool call's
  edit, never the decision row that must ride the same commit, and never a shell write (§8 F2).
- **Admitting a mirror equal to its render.** It needs the mirror's render inside the guard, a
  dependency on `TOOL-dGroundRules-5`, which builds beside it, and the landing already renders.

## 5. Production-readiness checklist

- security — deny by default: every change to a guarded path is refused without the owner's terminal
  unless it is the one shape, a missing launcher refuses, and an unreadable state exits 2, which the
  hook refuses. The admitted shape can only raise one existing measured-file cap; it cannot add,
  remove, lower or re-key one, nor touch another key or path. Its ceiling is §4's escapes list.
- perf / scale — an ordinary commit costs one `git show` and one `git diff --cached`; a commit staging
  a guarded path adds one Python spawn and about six git calls.
- error / empty / loading states — no list at HEAD admits silently; a policy file that does not parse
  is refused by name; no HEAD reads every staged path as touched.
- observability — every refusal names the path and each failed condition; an owner admission and an
  agent admission each print one line.
- risks — an agent stages a regenerated mirror by habit and is refused; the remedy line names the
  restore command. A false refusal stops an agent's commit, never an owner's at a terminal.
- testing — the thirteen cases by `check_policy.py --fixture`, the hook's arms in the pre-commit
  suite, and AC1 to AC12.
- migration — none: the four paths have no agent writer today.
- user docs — `help/policy.md`, S6.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`guard.py`, `guarded-paths.txt` and `check_policy.py`, and the help page as `policy.md` under
`help/`, because the spec-token checker grades a path-shaped token in a criterion against the tracked
set and this run creates them. Each fixture repository sits under `%TEMP%`, short-named.

- **AC1** — When `python check_policy.py --fixture guard-admits-raise` runs, `guard.py --staged`
  exits 0 printing `policy-guard: admitted`.
  Red when: the guard refuses a single measured-file cap raised, nothing else changed, its RAISED
  argument and decision row attached.
- **AC2** — When `--fixture guard-lowered` runs, `guard.py --staged` exits 1 naming the lowering.
  Red when: a lowered cap is admitted.
- **AC3** — When `--fixture guard-two-raised` runs, `guard.py --staged` exits 1 naming two keys
  changed. Red when: two caps raised in one commit are admitted.
- **AC4** — When `--fixture guard-class-row` runs, `guard.py --staged` exits 1 naming the class row
  as not a measured-file cap. Red when: a class row's raise is admitted.
- **AC5** — When `--fixture guard-beside-change` and `--fixture guard-beside-path` run, each exits 1,
  the first naming two keys changed and the second naming `.governance/deploy.toml`.
  Red when: a raise beside another change to a guarded file is admitted.
- **AC6** — When `--fixture guard-no-record`, `guard-no-argument` and `guard-no-row` run, each exits
  1; the first names both the RAISED argument and the decision row, the others the one missing.
  Red when: a raise lacking either part of its change record is admitted.
- **AC7** — When `--fixture guard-other-paths`, `guard-new-row` and `guard-removed-row` run, every
  plant exits 1, naming its path or "a key was added" or "a key was removed".
  Red when: an agent change to the mirror, the instruction manifest or `.governance/deploy.toml`, or
  a new or removed cap row, is admitted.
- **AC8** — When `--fixture guard-merge-side` runs, the merge concluded with the branch's own policy
  file exits 0 and the merge concluded with a third text exits 1.
  Red when: a merge taking a side is refused, or a merge writing a new text is admitted.
- **AC9** — When a scratch repository whose `core.hooksPath` holds a copy of `.githooks/pre-commit`
  and whose tree holds the policy kit at `tools/policy/` and `GOV_KITROOT=tools` in
  `.githooks/gate-env.sh` runs `git commit` of a lowered cap from this run's shell, the commit exits
  non-zero printing `policy-guard: refused`; a commit staging no guarded path succeeds and prints no
  `policy guard` line.
  Red when: the lowered cap is committed, or the guard runs on an unguarded commit.
  permission: the owner's terminal half, a commit at a terminal printing
  `admitted on the owner's terminal proof`, needs a terminal this run's shell lacks; the owner
  observes it.
- **AC10** — When `grep -nE "^\s*(import|from)\s+policy\b" guard.py` and `grep -c "resolve(" guard.py`
  run, the first prints nothing and the second prints `0`.
  Red when: the guard imports the reader or resolves a key, so it reads `policy-file.guard` or
  `policy-file.proof`.
- **AC11** — When `grep -vE "^\s*(#|$)" guarded-paths.txt` runs under `tools/policy/`, it prints
  exactly the four paths of §1, one per line: the policy file, its JSON mirror, the instruction
  manifest and `.governance/deploy.toml`. The instruction manifest is spelled here in prose because
  no revision tracks it yet and the spec-token checker grades a backticked path in a criterion.
  Red when: a path is missing, misspelt or extra.
- **AC12** — When `grep -n "RAISED"` and `grep -n "terminal"` run over `policy.md` under `help/`,
  each prints a line of the section "Who may change the policy file".
  Red when: the section is absent or names neither the agent shape nor the owner's proof.

## 7. Gates

`branch-guard self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `shell hygiene (a loop fed by a command substitution)` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the cases
below; they are named by the arm lines rather than on the leg line, because neither exists at this
spec's base.

New arm: tools/policy/check_policy.py (`--fixture guard-*`, the thirteen cases of §4) · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the guard staged to admit any change whose policy file parses, then staged to skip the decision-row check · none
New arm: .githooks/pre-commit.test.sh · covers AC9 · a throwaway repository with a stand-in guard exiting 1, then 2, then absent with its list present and no launcher, each refusing a commit that stages a listed path from the suite's non-terminal shell, and silent on a commit staging none · that suite's assertion count, raised by the arms added

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`, which the header
  regex at `tools/memory-tree/tree_lib.py:377` joins. Observation, 2026-10-23: the set is `OPEN
  SPECCED INPROGRESS BLOCKED DEFERRED CLOSED WONTDO`, so a `DRAFT` header parses as no header and the
  unit reads MISSING. Liveness: the tuple would carry `DRAFT` if the vocabulary admitted it.
  RESOLVED (agent, 2026-10-23, delegated): `OPEN`, the token `memory/TEMPLATE-SPEC.md` gives
  drafting. widens: none · relaxes: none
- **F2 — Which seam does the guard wire into?** (a) `.githooks/pre-commit`, over the staged change.
  (b) The PreToolUse write gate of `tools/hooks/scratch-guard.js`, at the tool call. (c) Both. (b)
  cannot see the decision row the admitted shape needs in the same commit, so it fails AC1 and veto 1
  discards it; (c) meets what (a) meets and adds a second mechanism in a second language, against
  M2's one mechanism per spec. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **FACT-QUESTION · F3 — What signal is the TTY proof?** (a) `[ -t 2 ]` in the hook. (b) A terminal
  and a proof trailer. (c) `/dev/tty` opening. Probe: each signal from this run's shell, which runs
  the hooks an agent's commit fires. Observation, 2026-10-23: `[ -t 0 ]`, `[ -t 1 ]` and `[ -t 2 ]`
  false, `/dev/tty` unopenable, so each reads an agent as absent. Liveness: each test answers true
  at an interactive terminal on a POSIX host, the case AC9's permission line hands the owner. The
  probe cannot rank (a) against (c); the preference is rung 3's: (b) adds no proof, the trailer
  being "text anyone can type" (v2's `[witnesses]`), and no writer of it exists until dDeclaredLoop.
  RESOLVED (agent, 2026-10-23, delegated): (a), the signal git's own stream wiring makes reliable.
  widens: none · relaxes: none
- **F4 — Does "nothing else changed" cover the whole commit or the guarded set?** (a) The guarded
  set: the policy file's other bytes and the other three paths. (b) Every path in the commit. Rung 1:
  the clause makes the change record "today's rule from `tools/template-size-limits.txt`", which puts
  the raise "in the commit of a unit of a build" (`tools/template-size-limits.txt:17`), beside that
  unit's change; (b) refuses that commit.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F5 — How does the guard know a measured-file cap before any cap is under `budgets.*`?** (a) A
  leaf under `budgets`, other than `enforce` and `pinned`, whose last segment is a file tracked at
  HEAD and whose value is an integer. (b) A sub-table this unit names, such as `[budgets.caps]`,
  which prescribes `TOOL-dGroundRules-9`'s layout. (a) reads any layout whose leaf names its file and
  rejects a class label by construction. Recommendation (a), handed to unit 9 in §3 Edges. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F6 — Is a regenerated mirror an agent write the guard admits?** (a) No: every agent change to
  the mirror is refused. (b) Yes, when it equals the render. Rung 1: the clause lists the mirror among
  the refused paths and admits one shape, a cap raised; the landing's render is committed with no
  hook firing (`tools/push-main.sh:921`, `:1111`).
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F7 — With a guarded path staged and no launcher, does the block skip or refuse?** (a) Refuse.
  (b) Announce a skip, as the hook's other legs do under the owner's F1 (c)
  (`.githooks/pre-commit:145`). That ruling's reason is that those legs are "an early signal" and a
  block on an absent kit "would stop ordinary work"; this block is the enforcement, and it blocks
  only a commit staging a guarded path. (b) admits every agent write on a host with no launcher,
  which fails AC2 there, so veto 1 discards it. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F8 — Does the build's grant lift veto 2 for the guard's surface?** `guard.py`, `guarded-paths.txt`
  and the pre-commit block are new public surface on a governance hook, and `cl-dClosedLoop-0012`
  names the minimal guard, its paths and its one admitted shape.
  RESOLVED (agent, 2026-10-23, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3.
  grants: PLAY-dClosedLoop-3 the minimal guard, its list and its pre-commit block ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the packet's Items 6, the brief's S7, the owner's FK-9-2,
  today's rule in `tools/template-size-limits.txt`, and the pre-commit hook and lander read at base
  `3708a705`.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-19, TOOL-dGroundRules-21 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit's findings that repair this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-24 · §6 · AC9: a criterion code span rejoined onto one line so hygiene check 23 reads the criterion's tokens; no meaning change.

## 10. Reuse audit

The seam extended is `.githooks/pre-commit`'s staged-leg pattern: its kit ladder `resolve_kit_gate`
(`.githooks/pre-commit:167`) and its tracked-resolver lookup (`.githooks/pre-commit:235`), with the
guard a new block beside the legs that already run there. No existing seam judges a staged diff's
shape: `python tools/codebase-map/reuse_lookup.py "refuse a commit that stages a protected file
unless the change has one admitted shape"` ranked name stems (`has`, `shape` in
`tools/govkit/matrix.py`, `changed` in `tools/run-gates/run-gates.sh`, `build_commit`) and none
inspects a staged change; the closest kin is the straggler guard the hook sources, which refuses a
staged path outright and admits no shape. So the predicate is new and the wiring is reused. The
recall probe returned the owner's FK-9-2, which agrees with the clause and is followed here, the
dDeclaredLoop packet's later guard, which this unit hands off to, and `TOOL-aTetheredScratch-1`'s
finding that a guard binds where the act is seen, which is why the commit and not the tool call is
the seam here. No hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does the minimal guard refuse agent
writes to the policy file and admit a single cap raise" --terms "minimal guard policy file agent
write refused owner-only tty-cli cap raise RAISED DECISIONS row pre-commit"`
