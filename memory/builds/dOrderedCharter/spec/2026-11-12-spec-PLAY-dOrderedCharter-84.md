# PLAY-dOrderedCharter-84 — a live unattended run's branch may commit a guarded path

**Status:** CLOSED · rev-2 · 2026-11-12 · node a · Tier-2 · base 5177028b6 · streams tooling · order 46 · advances PLAY-dOrderedCharter-38 · ratified 2026-11-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 PLAY-dOrderedCharter-85 PLAY-dOrderedCharter-86 PLAY-dOrderedCharter-87 PLAY-dOrderedCharter-88 |
| [2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md](../build/2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 PLAY-dOrderedCharter-85 PLAY-dOrderedCharter-86 PLAY-dOrderedCharter-87 PLAY-dOrderedCharter-88 |
| [2026-11-12-build-PLAY-dOrderedCharter-84-1-builder-return.md](../build/2026-11-12-build-PLAY-dOrderedCharter-84-1-builder-return.md) | journal | — |
| [2026-11-12-build-PLAY-dOrderedCharter-84-deviation-841.md](../build/2026-11-12-build-PLAY-dOrderedCharter-84-deviation-841.md) | deviation | — |
| [2026-11-12-build-PLAY-dOrderedCharter-84-ledger.md](../build/2026-11-12-build-PLAY-dOrderedCharter-84-ledger.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-84-1-spec-writer.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-84-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-84-build-brief.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-84-build-brief.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-84-spec-brief.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-84-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

This run cannot land itself. One reason is that the policy guard refuses every agent commit of the
two files the run's upgrade step writes, and of the deploy-rule edit the owner ordered mid-run. The
owner ruled on 2026-11-12 that no file is owner-only to a run working under its build's mandate.
This unit makes the minimal policy guard admit a guarded change committed on the run branch of a
live unattended run. The other reason, the lander's prepare regenerating over uncommitted step
output, is the sibling unit PLAY-dOrderedCharter-85.

## 2. Scope (IN)

- **S1** — `tools/policy/guard.py` gains one admission, `check_run_mandate`. It applies when the
  existing verdict refuses. The commit's branch must be the `run-branch:` of a run-state file at
  HEAD whose recorded phase at HEAD is not terminal. It reads no policy key and imports no other
  kit's code. When it holds, the guard prints one admission line and exits 0, with no decision row
  or change record demanded. When it fails, the guard prints its existing refusal lines, one line
  saying why no live run admits the commit, and the reworded remedy, then exits 1 (section 4, "The
  admission"). Observed by AC1, AC2, AC3 and AC6.
  After this unit, the default value `owner-only` admits a live run's branch with no recorded
  reason, while TOOL-dDeclaredLoop-2's `agents-within-mandate` row demands one. That build
  reconciles the two when it builds (section 3, Edges).
  **Readers:** by name: `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-2.md`,
  whose section 4 "The verdict" admits under its default row exactly what the minimal guard
  admits, and whose Alternatives rejected says the policy kit has no dependency on the run-state
  grammar. That unit is unbuilt, so its spec is the reader ·
  by value: `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-2.md`, whose two
  mandate fixture cases and AC7 expect the exits of a guard on a live run's branch and on a branch
  no run names.
- **S2** — `tools/policy/check_policy.py` gains three outcome cases of the guard, registered
  beside the other `guard-*` cases: `guard-run-live`, `guard-run-terminal` and
  `guard-run-other-branch` (section 4, "The fixture cases"). Observed by AC1, AC2 and AC3.
- **S3** — The documents state the admission. These are the `help/policy.md` section "Who may change
  the policy file", the "The guard" section of `tools/policy/README.md`, the guard's module docstring,
  and the one clause of the `.githooks/pre-commit` policy-guard block comment that calls the guard
  owner-only (section 4, "Docs"). Observed by AC4.

## 3. Non-goals (OUT)

- The lander's prepare fold. That is the sibling unit PLAY-dOrderedCharter-85, at the same order.
  Neither unit reads or writes the other's files, and they can land in either order. This run's
  landing needs both.
- A reader of `policy-file.guard` or `policy-file.proof`, a TTY policy command, or a floor. Those
  stay TOOL-dDeclaredLoop-2's. The admission holds whatever `policy-file.guard` says, by the
  owner's ruling.
- Any edit to TOOL-dDeclaredLoop-2's spec. Its reader line is S1's `**Readers:**` and the hands-off
  edge below.
- Any change to what the `.githooks/pre-commit` block runs, its terminal test, or its refusal when
  no launcher resolves. Only one clause of the block's comment changes (S3).
- The unattended kit's derived phase. The guard reads the recorded `phase:` fact at HEAD and does not
  observe the remote (section 4, "What it does not check").
- The `branch-ref` fact. Only `run-branch:` names a run's branch here, as the dDeclaredLoop-2 row
  states the condition.
- A bump of `KIT_POLICY_VERSION`. Kit versions are minted at the landing
  (`tools/push-main.sh@efee7864:26-29`).
- A wider guard for the `policy fixtures` leg, a count floor, or a ceiling move.

### Edges

- **consumes-from** external — the unattended kit's run-state grammar, read as text and never
  imported: the `## Run facts` section and its `phase:` and `run-branch:` facts
  (`tools/unattended/unattended.sh@2a59172f:1567-1583`), and its `PHASES_TERMINAL` declaration
  (`tools/unattended/unattended.sh@2a59172f:993`). If that grammar moves, the admission refuses,
  which is deny by default.
- **hands-off** external — TOOL-dDeclaredLoop-2, when it builds, reads S1's admission as the
  minimal guard's verdict. Under its default `owner-only` row, the guard it wraps then admits a live
  run's branch with no recorded reason. Its `agents-within-mandate` row demands a reason, so that
  row would be stricter than the default. That build owns the reconciliation through its own spec
  revision. This unit writes nothing in it. The main loop files an ask naming the inversion at this
  build's close (F2).

## 4. Design

### Evidence

Read at `5177028b6`.

- The hold: the guard refuses an agent's commit of `.governance/deploy.toml` or
  `.governance/instructions.toml`, the two files the step `playbook/adopter-rules-to-overlay` writes
  (`memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-1-owner-landing.md`).
- The prepare's fold is `git commit-tree` over the detached merge, chosen so that no pre-commit hook
  fires (`tools/push-main.sh@efee7864:1098-1103`). The policy guard therefore never judges that
  fold. The brief says the fold lands under this admission, which is not how the code works. The
  admission is what lets this run commit its other guarded change, the deploy-rule hunk the owner
  ordered mid-run (the owner-landing record, its step 1), as an ordinary agent commit on the run
  branch.
- The guard refuses every guarded path except one cap raise and the mirror's render
  (`tools/policy/guard.py@cf78b705:194-223`). Its remedy names the owner's terminal as the only
  other route (`tools/policy/guard.py@cf78b705:40-41`). The hook runs it only when a listed path is
  staged and stderr is not a terminal (`.githooks/pre-commit@418c235e:198-213`).
- The guard ruling (`memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-1-owner-guard-ruling.md`):
  the owner-only default came from R4.2 for who may change a policy. TOOL-dGroundRules-6 enforced
  it without the key's switch, over three neighbours as well. Nothing changed those three files
  between 2026-10-24 and this build.
- The mandate condition, as TOOL-dDeclaredLoop-2 states it: "the branch is the `run-branch:` of a
  run-state file whose derived phase is not terminal"
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-2.md@261f96d8:203`).
- A run-state file is `<MEMORY_ROOT>/builds/<slug>/RUN.md` (`tools/unattended/unattended.sh@2a59172f:1555`).
  The unattended kit lists them by the glob `$M/builds/*/RUN.md`
  (`tools/unattended/unattended.sh@2a59172f:3521`). This run's record carries
  `run-branch: refs/heads/branch/unattended-dorderedcharter-725f52` and `phase: VERIFYING` at
  `5177028b6`.
- The leg `brief-recorded` reads the terminal set from the driver's `PHASES_TERMINAL` line,
  "PARSED, never sourced", and treats a set it cannot read as a dead probe, never as an empty set
  (`tools/unattended/check-brief-recorded.sh@e1220547:225-246`).
- The probes ran at `5177028b6` from this worktree. A `git grep -l` for this branch's name over the
  run-state glob at HEAD returned `memory/builds/dOrderedCharter/RUN.md` alone, in 0.09 s (PINNED,
  one timed run). A `git grep` for the `PHASES_TERMINAL` line over the driver glob returned one
  line, `LANDED ABORTED`.

### The admission (S1)

`main` is unchanged up to the point where `refused` is non-empty. There it calls
`check_run_mandate()` before printing. A commit the existing verdict admits never reaches this check.
A cap raise keeps its own admission line, and an ordinary commit pays nothing more.

`check_run_mandate()` returns `(admission, whys)`. `admission` is `"<run-state path>, phase <PHASE>"`
when a live run names the branch, else `None`. `whys` is the list of reasons no run admits it. Every
read goes through the guard's own `run_git`, so a git failure exits 2 as today. The steps, in order,
each stopping at its first miss:

1. **The branch.** `git symbolic-ref -q HEAD`, with `missing=True`. When it answers nothing, HEAD is
   detached: why `HEAD is detached`. Otherwise the branch is the answer with `refs/heads/` stripped.
2. **The candidates.** Run `git grep -l -z -F -e <branch> HEAD -- ':(glob)**/builds/*/RUN.md'`,
   with `missing=True`, so that exit 1 means no candidate. This reads HEAD's tree, never the index or
   the working tree, so a run-state file staged in the same commit grants nothing. The glob matches
   every memory root, the repository root included. Each name it prints is `HEAD:<path>`. Each blob
   is read with `git cat-file blob`. A candidate is kept when its `run-branch` fact, with
   `refs/heads/` stripped, equals the branch. When no candidate is kept: why
   `no run-state file at HEAD names <branch> as its run-branch`.
3. **The terminal set.** Run
   `git grep -h -E '^PHASES_TERMINAL="[^"]*"[[:space:]]*$' HEAD -- ':(glob)**/unattended/unattended.sh'`,
   with `missing=True`. Each line's quoted value is split on whitespace. When no line matches: why
   `no unattended driver at HEAD declares PHASES_TERMINAL, so no phase reads live`. When the distinct
   values are not exactly one, or any token is not `[A-Z]+`: why
   `the PHASES_TERMINAL declarations at HEAD read <values joined by " | ">, not one set of phase tokens`.
   The set is read, never copied, so no second spelling needs a parity gate.
4. **The phase.** Read each kept candidate's `phase` fact in path order. A phase that fully matches
   `[A-Z]+` and is not in the set is live, and the first live candidate is the admission. Otherwise
   there is one why per candidate: `<path> names <branch> and its phase at HEAD, <PHASE>, is terminal`,
   or, for an empty or malformed value, `<path> names <branch> and its phase at HEAD, '<value>', is no phase token`.

`read_run_fact(text, key)` returns the value of `<key>:` in the text of a run-state file, or None.
It follows the driver's `fact` grammar (`tools/unattended/unattended.sh@2a59172f:1567-1583`): one
trailing CR is stripped from each line, the section runs from a line opening `## Run facts` to the
next line opening `## `, the first line opening `<key>:` wins, and leading spaces are stripped from
the value. `check_run_mandate` calls it twice per candidate.

On an admission the guard prints one line and exits 0:

```
policy-guard: admitted · <every touched path, sorted, space-joined> · the run-branch of <run-state path>, phase <PHASE>
```

On a refusal it prints the existing `policy-guard: refused · <path> · <why>` lines, then one
`policy-guard: not a live run's branch · <why>` line per why, then the remedy, and exits 1. The
remedy becomes:

```
policy-guard: an agent may raise one measured-file cap in this shape, or commit on the run branch of a live unattended run; any other change to these files is the owner's, committed from a terminal.
```

**No decision row and no change record are demanded.** This follows from three facts. First, the
brief asks for "the mandate condition", which is the second clause of the dDeclaredLoop-2 row. The
first clause is the `agents-with-reason` conditions, which require "only `.governance/policy.toml`
changed". That would refuse the `deploy.toml` and overlay changes the ruling admits. Second, the
change record kind is not in the minimal guard's population. Third, every commit on a run branch
is joined to a specced unit by the routed-commits leg, which records why it was made.

### What it does not check

- **Evasion.** An agent can commit a run-state file naming its own branch with a live phase, and the
  next commit is admitted. The guard stops forgetting, not evasion, as its header already says of
  `--no-verify` and a pty wrapper. The admission adds this one route to that list. The commit that
  carries the run-state file is not itself admitted, because the guard reads HEAD.
- **The derived phase.** The guard reads the recorded phase. The unattended kit derives LANDED for
  two cases: a LANDING record whose landing commit the advertised tip contains, and a HELD hand-off
  an owner landed (`tools/unattended/unattended.sh@2a59172f:1608-1621`). Both read as live here
  until a terminal phase is committed, because a pre-commit hook observes no remote.
- **Who commits.** Any process without a terminal that commits on that branch is admitted alike,
  whatever its session.
- **What is changed.** It does not ask whether the guarded change belongs to the run's units.
- **The lander's fold.** It fires no hook, before and after PLAY-dOrderedCharter-85, so no guard
  judges it.

### The fixture cases (S2)

There is a new tuple, `GUARD_RUN`, holding the three names. Each runs inside `run_guard_case` over
`build_guard_repo` (`tools/policy/check_policy.py@3148be18:2349-2451`). Before its scenarios, each
case commits two files on a branch `run/t`. The first is `tools/unattended/unattended.sh`, holding
the single line `PHASES_TERMINAL="LANDED ABORTED"`. The second is `memory/builds/tRun/RUN.md`,
holding `## Run facts` and the case's `phase:` and `run-branch:` lines. Both are written as
literals, so the case reads no source file and the guard trace joins nothing new
(`tools/policy/check_policy.py@3148be18:4117-4160`). Each scenario stages
`.governance/deploy.toml` and `.governance/instructions.toml` edits as `guard-other-paths` does. It
then runs `guard.py --staged`, judges the exit code and stdout needles, and resets to the case's
commit.

| Case | Scenario | Guard exit | Stdout carries |
|---|---|---|---|
| `guard-run-live` | `phase: BUILDING`, `run-branch: refs/heads/run/t` | 0 | `policy-guard: admitted · .governance/deploy.toml .governance/instructions.toml · the run-branch of memory/builds/tRun/RUN.md, phase BUILDING` |
| `guard-run-live` | `run-branch: run/t`, with no `refs/heads/` | 0 | the same line |
| `guard-run-terminal` | `phase: LANDED` | 1 | `refused · .governance/deploy.toml`, and `its phase at HEAD, LANDED, is terminal` |
| `guard-run-terminal` | `phase: ABORTED` | 1 | `its phase at HEAD, ABORTED, is terminal` |
| `guard-run-terminal` | `phase: BUILDING`, the driver removed in a commit | 1 | `no unattended driver at HEAD declares PHASES_TERMINAL` |
| `guard-run-other-branch` | `run-branch: refs/heads/run/other` | 1 | `no run-state file at HEAD names run/t as its run-branch` |
| `guard-run-other-branch` | the HEAD record removed in a commit, a live record naming `run/t` staged | 1 | `no run-state file at HEAD names run/t as its run-branch` |
| `guard-run-other-branch` | `git checkout --detach` | 1 | `HEAD is detached` |

The module docstring's `guard-*` paragraph gains one sentence naming the three cases. The existing
guard cases run on a branch with no run-state file. Their exits do not move, and their needles do
not read the remedy line.

### Docs (S3)

- `help/policy.md`, "Who may change the policy file": a bullet after the mirror bullet. Its bold lead
  is "An agent's commit on a live run's branch is admitted." It states the condition, that the guard
  reads HEAD and not the staged run-state file, the admission line, the `not a live run's branch`
  refusal line, and that no decision row is asked. The "What the guard does not catch" bullet gains
  the committed run-state file and the recorded-phase gap.
- `tools/policy/README.md`, "The guard": one paragraph after the cap-raise conditions. It states the
  four steps and their whys, and the exit 1 sentence gains the `not a live run's branch` lines.
- `tools/policy/guard.py`'s docstring: the admitted shapes add the live run's branch, and the
  "IT STOPS FORGETTING" list adds a committed run-state file.
- `.githooks/pre-commit@418c235e:187`: "owner-only and the TTY proof" becomes "owner-only outside a
  live unattended run's branch, and the TTY proof". No line the hook runs changes.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `check_run_mandate` | `tools/policy/guard.py` | `py.function`, `OK` by `--suggest` at design |
| `read_run_fact` | `tools/policy/guard.py` | `py.function`, `OK` by `--suggest` at design |
| `GUARD_RUN` | `tools/policy/check_policy.py` | `py.constant` is not a declared cell |
| `guard-run-live`, `guard-run-terminal`, `guard-run-other-branch` | the fixture's case names | no cell grades a case name |
| `policy-guard: not a live run's branch · ` | the guard's stdout | none |

### Files touched (estimate)

- `tools/policy/guard.py` (S1, S3)
- `tools/policy/check_policy.py` (S2)
- `tools/policy/README.md` (S3)
- `help/policy.md` (S3)
- `.githooks/pre-commit` (S3)

### Alternatives rejected

- **A copy of the terminal set in the guard, held by a parity case.** The parity case would read
  `tools/unattended/unattended.sh` in the fixture process. The guard trace then requires the
  `policy fixtures` guard to cover that file, and widening a guard reds every live spec that touches
  it without naming the leg, as PLAY-dOrderedCharter-82's rev-2 measured.
- **Reading the run state through the unattended kit's `read_derived_phase`.** That is a shell
  function in another kit that observes the remote. The guard is the policy kit's, and a pre-commit
  hook makes no network call.
- **Reading `MEMORY_ROOT` from `.memory-tree.conf` to place the glob.** It is one more file read and
  one more grammar. The glob already matches every root, and a stray `builds/<x>/RUN.md` outside the
  memory root admits only a branch it names with a live phase, which is the evasion already listed.
- **The admission as the guard's first check.** It would print a run line where a cap raise prints
  its own admission. Placed after the verdict, it applies only where the verdict refuses.

## 5. Production-readiness checklist

- security — This widens a deny guard, and the owner ruled for it. The grant is narrow. It covers
  only the branch a committed run-state file names, while that file's phase at HEAD is live, and
  the terminal set must be readable. Every miss refuses. The guard reads HEAD, so a commit cannot
  grant itself. The evasion it adds is listed (section 4).
- perf / scale — The new reads run only on a commit the guard would otherwise refuse: one
  `symbolic-ref`, one `git grep` (0.09 s, PINNED, section 4), one `cat-file` per candidate and one
  `git grep` for the driver.
- error / empty / loading states — A detached HEAD, no candidate, no driver, an unreadable set, and a
  malformed phase each print their own why and refuse. A git failure exits 2 as today.
- observability — The admission names the run-state file and its phase. Each refusal names why.
- risks — The recorded phase lags the derived phase after a landing (section 4). TOOL-dDeclaredLoop-2's
  rows become stricter than its default (section 3, Edges, and F2).
- testing — AC1 to AC4 are direct probes, and AC6 is the run's own commit. The guard cases are
  declared in section 7, and the main loop observes them red at the base and green at the close.
- migration — N/A: no schema, record shape or conf key moves, and the admission needs no upgrade
  step.
- user docs — `help/policy.md` (S3).

## 6. Acceptance criteria

- **AC1** — When `python tools/policy/check_policy.py --fixture guard-run-live` runs after the build,
  it prints two `policy-fixture: guard-run-live` lines, neither carrying `WRONG`, then
  a count line ending `· 0 wrong`, and exits 0. Each line observes the guard
  exit 0 printing the admission line that section 4's table gives.
  Red when: the guard refuses a staged guarded change on the branch that a live run's committed
  record names, in either `run-branch` spelling.
- **AC2** — When `python tools/policy/check_policy.py --fixture guard-run-terminal` runs after the
  build, it prints three lines carrying no `WRONG` and exits 0. Each line observes the guard exit 1
  with the why that the table gives for `LANDED`, `ABORTED` and a missing driver.
  Red when: a run in a terminal phase, or a tree with no terminal set to read, admits the commit.
- **AC3** — When `python tools/policy/check_policy.py --fixture guard-run-other-branch` runs after the
  build, it prints three lines carrying no `WRONG` and exits 0. Each line observes the guard exit 1
  for a branch that no record at HEAD names, for a record that is only staged, and for a detached
  HEAD.
  Red when: the guard admits a branch that no committed run-state file names, or reads the index
  in place of HEAD.
- **AC4** — When `grep -c "live run's branch" help/policy.md tools/policy/README.md` runs after the
  build, it prints a count of at least 1 for each file. The base prints 0 for both.
  Red when: either document still says the four files are the owner's alone outside a cap raise.
- **AC6** — When this run's deploy-rule hunk (the owner-landing record, its step 1) is staged on this
  run's branch and `python tools/policy/guard.py --staged` runs from a shell with no terminal, it
  prints a line opening
  `policy-guard: admitted · .governance/deploy.toml · the run-branch of memory/builds/dOrderedCharter/RUN.md`
  and exits 0. At the base it prints `policy-guard: refused · .governance/deploy.toml` and exits 1.
  Red when: the guard refuses the live run's own branch.
  permission: the main loop makes this commit after the build. A role agent's scratch guard refuses
  the write.

## 7. Gates

`policy fixtures` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

`policy fixtures` is the one guarded leg the estimate trips that is not broad. It is tripped by
`tools/policy/` and by `help/policy.md`, as DERIVED by the spec-token checker's `--legs-for` over
the estimate at `5177028b6`. Every other leg those paths trip has a broad guard.
`lexicon naming predicates` grades the two minted functions. The leg's ceiling of 1290 stands
(`tools/gate-legs.json@83fb3a5f`). This spec does not re-measure it.

New arm: tools/policy/check_policy.py · covers AC1 · `guard-run-live`: at the base there is no such case (exit 2), and a guard without the admission refuses the run branch · none
New arm: tools/policy/check_policy.py · covers AC2 · `guard-run-terminal`: staged red by an admission that skips the terminal-set test · none
New arm: tools/policy/check_policy.py · covers AC3 · `guard-run-other-branch`: staged red by an admission that reads the index in place of HEAD · none

## 8. Open questions

- **F1 — One unit or two?** BUILD-METHOD M2 asks for one mechanism per spec. rev-1 held two: the
  policy kit's admission and the lander's fold. They share no file and no criterion.
  - (a) Split. This unit keeps S1 to S3, AC1 to AC4 and AC6. A sibling unit at order 46 takes the
    lander's fold, its arm and its two criteria.
  - (b) Keep one unit, as the brief and the ruling record frame it.
  Recommendation: (a). M2 states its reason, an unreviewable closing diff, and rev-1 matched it.
  RESOLVED (agent, 2026-11-12, delegated): (a), under the owner's 2026-11-10 "take forks'
  recommendations, land it"
  (`memory/builds/dOrderedCharter/build/2026-11-10-build-PLAY-dOrderedCharter-1-owner-fork-picks.md`).
  The lander's half is PLAY-dOrderedCharter-85.
- **F2 — Does TOOL-dDeclaredLoop-2 need an ask filed now?** That unit's default row becomes looser
  than its `agents-within-mandate` row once this lands.
  - (a) The hands-off edge alone.
  - (b) Also file an ask in this build's BACKLOG at the close, naming the inversion.
  Recommendation: (b). A hands-off to an unbuilt unit in another build is read only if someone
  regrounds that build, and an ask is the record a kickoff surfaces.
  RESOLVED (agent, 2026-11-12, delegated): (b), under the same ruling. The main loop files the ask
  at the close.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft from the brief
  `2026-11-12-prompt-PLAY-dOrderedCharter-84-1-spec-writer`, grounded at `5177028b6`. The brief
  said the prepare's fold lands under the guard's admission. The fold is `commit-tree` and fires no
  hook, so section 4 says the admission is for the run's ordinary agent commits instead. The brief
  pointed to an `upgrade steps` block in the lander. The stage is `run_gov_first`, gov first.
- rev-2 · 2026-11-12 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S4 S5 · AC5 AC7 · F1 and F2 resolved by the main
  loop under the owner's standing fork picks. Per F1, the lander's fold moves to the sibling
  PLAY-dOrderedCharter-85: S4, S5, AC5, AC7, arm 41, the lander's design, inventory row, files and
  rejected alternative, and the fold's recall query. The remaining criteria keep their labels. The
  header gains `ratified 2026-11-12`.

## 10. Reuse audit

Seams extended: the guard's own `run_git`, `missing=True` exit-1 convention and HEAD-only reads
(`tools/policy/guard.py@cf78b705:46-80`); the driver's `fact` grammar, re-read rather than imported
(`tools/unattended/unattended.sh@2a59172f:1567-1583`); the `brief-recorded` leg's text parse of
`PHASES_TERMINAL` (`tools/unattended/check-brief-recorded.sh@e1220547:225-246`); and the
`run_guard_case` and `build_guard_repo` fixture with its `GUARD_PLANTS` staging.
`tools/codebase-map/reuse_lookup.py` ranked the generic stems `read`, `run_git`, `fact` and `phases`
for the run-state query. `fact` and `phases` are the unattended kit's shell, which the policy kit may
not import. `run_git` is the guard's own. No other seam fits.

Recall terms used: `reuse_lookup.py "read a run-state fact phase run-branch from a committed RUN.md and decide whether the run is live"`
