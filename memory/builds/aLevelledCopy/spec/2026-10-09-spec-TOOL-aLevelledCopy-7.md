# TOOL-aLevelledCopy-7 — the ssh arm stands back when the operator chose an SSH program

**Status:** CLOSED · rev-2 · 2026-10-09 · node a · Tier-2 · base ce9192c0 · streams tooling · order 3 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aLevelledCopy-7-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aLevelledCopy-7-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aLevelledCopy-7-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-7-1-spec-brief.md) | journal | TOOL-aLevelledCopy-8 TOOL-aLevelledCopy-9 |

<!-- /gen:spec-records -->

## 1. Goal

git picks the SSH program as `GIT_SSH_COMMAND`, then `core.sshCommand`, then `GIT_SSH`. The ssh arm
that `check-wiring.sh` gained in this build writes a repo-local `core.sshCommand` whenever no config
scope sets one, so on a node whose operator chose plink or Windows OpenSSH through `GIT_SSH`, every
SessionStart silently replaces that program with the bundled OpenSSH, which cannot reach Pageant or
the Windows agent. This unit makes the arm treat `GIT_SSH`, `GIT_SSH_VARIANT` and `ssh.variant` as the
operator's choice: it says so in a `note` line and writes nothing. It closes the closing review's H1
(finding id 3) and M1 (finding id 9), which share one root cause.

## 2. Scope (IN)

- **S1 — the operator-choice guard.** In `check_ssh_keepalive`, on the path where an ssh-shaped
  remote exists and no config scope sets `core.sshCommand`, and BEFORE that path splits into its set
  branch (`--fix`, `--session`) and its `UNWIRED` branch (`--check`), the arm asks three questions in
  this order and stops at the first that answers yes:
  1. `${GIT_SSH:-}` is non-empty;
  2. `${GIT_SSH_VARIANT:-}` is non-empty;
  3. `git config --get ssh.variant` exits 0, which reads every scope.

  A yes prints `note     ssh       — <name> is the operator's choice of SSH program; NOT setting
  core.sshCommand, which would override it`, where `<name>` is `GIT_SSH`, `GIT_SSH_VARIANT` or
  `ssh.variant`. It writes no config, appends no health event and counts nothing, under every mode.
  Observed by AC1, AC2, AC3, AC4.
- **S2 — a failed read is not an absence.** The `ssh.variant` read distinguishes its exit codes:
  0 is set (S1 step 3), 1 is unset, and any other status prints `note     ssh       — cannot read
  ssh.variant (git config exit <n>); NOT setting core.sshCommand` and writes nothing. This is the
  class the closing review's M4 names for the sibling `core.sshCommand` read, which
  `TOOL-aLevelledCopy-8` fixes; this unit does not reintroduce it in the read it adds. Observed by
  AC5.
- **S3 — `--check` gives no wrong advice.** Under any S1 or S2 trigger, `--check` prints the `note`
  line and no `UNWIRED  ssh` line, so it carries no `Fix: git config core.sshCommand …` and the ssh
  arm adds nothing to the exit status. Observed by AC4.
- **S4 — the header says it.** The ssh paragraph of the header comment names the three triggers and
  why: `core.sshCommand` outranks `GIT_SSH`, so setting it would replace the operator's program. Its
  does-not-check list keeps `GIT_SSH_COMMAND` and adds that a `core.sshCommand` already present beside
  a `GIT_SSH` is graded by the existing `ok` and `note` cases, because the arm cannot tell who wrote
  it. Observed by AC7.
- **S5 — the suite's existing ssh arms are hermetic to an operator's environment.** The suite's
  `seed_ssh_fixture` unsets `GIT_SSH` and `GIT_SSH_VARIANT`, so the LC2 arms written by
  `TOOL-aLevelledCopy-2` keep passing on a node that exports either. Without this, S1 makes those arms
  red on exactly the plink node this unit protects: the fixture-inherits-ambient-machine-state class.
  Observed by AC6.
- **S6 — the triggers are gated.** New LC2 arms in the kit's own self-test, one per trigger and one
  for S2, each observed RED against the checker as it stands before this unit. Observed by AC8.

## 3. Non-goals (OUT)

- **The precedence of an existing `core.sshCommand`.** When a scope already sets it, git uses it and
  `GIT_SSH` is moot, so the arm's `ok` and `note` cases stand unchanged. A value an earlier SessionStart
  wrote over a `GIT_SSH` cannot be told from an operator's own; no adopter holds one, because the arm
  has not landed on `main` (its build commit c82936e23 is not an ancestor of `origin/main`, read with
  `git merge-base --is-ancestor` on 2026-10-09).
- **`GIT_SSH_COMMAND`.** It outranks `core.sshCommand`, so a value written here never overrides it.
  The header already says the arm does not check it.
- **Amending `TOOL-aLevelledCopy-2`'s spec.** It is CLOSED and stays closed. This spec carries the
  change to the arm that unit built (§8 F1 says why that is prose here and not an edge).
- **The runbook.** `WIRE-INTO-PROJECT.md` is a governance carrier (M3 veto 2); its wiring-health
  paragraph is already the subject of an open ask in this build's `BACKLOG.md`.
- **The arm's other failure states.** A failed `core.sshCommand` write, a failed `--show-scope` read,
  push-main version skew, the sed-only derivation and the URL classifier's untested branches are
  `TOOL-aLevelledCopy-8`'s batch.

### Edges

- **hands-off** `TOOL-aLevelledCopy-8` — that unit rebuilds the arm's `core.sshCommand` set-or-unset
  read (review M4) after this one lands; it must keep this guard on the unset path, ahead of both the
  set branch and the `UNWIRED` branch, and its new fixtures must stay hermetic to `GIT_SSH` as S5 makes
  the existing ones.

## 4. Design

### Where the guard sits

The arm today resolves `push-main.sh`, derives `want`, scans remotes for an ssh-shaped push URL, reads
`core.sshCommand` at every scope, and on an empty read branches on `DO_FIX`. The guard is placed after
the remote scan and the config read, on the empty-read path, before the `DO_FIX` split. Placing it
earlier would change the `skip` lines gov's own HTTPS tree prints for no gain; placing it inside one
branch would leave the other wrong. It is phrased by position on the unset path rather than by line,
because `TOOL-aLevelledCopy-8` rewrites how "unset" is decided.

### Why these three triggers

`GIT_SSH` names a program git runs instead of `ssh` when no `core.sshCommand` exists. `GIT_SSH_VARIANT`
and `ssh.variant` tell git which argument dialect that program speaks; a `plink` variant beside a
written `ssh -o …` would hand OpenSSH plink's flags. Any non-empty value is treated as a choice,
including `ssh` and `auto`: the arm cannot know why an operator set it, and standing back costs only
the keepalive, which the `note` line names.

### The read and its failure

```bash
v=$(git config --get ssh.variant 2>/dev/null); rc=$?
# 0 = set (a trigger) · 1 = unset (continue) · anything else = note, write nothing
```

### Inventory

No new function, variable or event token. The arm gains two `note` line shapes, both under the
existing `ssh` label. The suite gains arms, not helpers; `seed_ssh_fixture` gains one `unset` line.

### Files touched (estimate)

- `tools/check-wiring.sh`
- `tools/check-wiring.test.sh`

### Rollout

The check-wiring kit ships with a normal `govkit update`. The one kit-version bump per touched kit
happens once, after the last unit of this build. `TOOL-aLevelledCopy-8` writes the same two files at
`order 4`, after this unit.

### Alternatives rejected

- **Only `GIT_SSH`, the review's minimum fix.** Rejected: the variant triggers carry the same
  override with a worse failure, wrong flags rather than a wrong program, and each costs one test.
- **Unsetting `core.sshCommand` when a `GIT_SSH` appears later.** Rejected: the arm cannot tell its own
  earlier write from an operator's, and it never overwrites or removes an operator value.
- **Setting `GIT_SSH_COMMAND` in a hook instead.** Rejected: a different mechanism, outside this
  arm, and it would outrank `GIT_SSH` for every git call in the hook's process.

## 5. Production-readiness checklist

- security — narrows a write: the arm now writes in strictly fewer states than before, and reads two
  environment variables and one config key it never executes or echoes beyond the variable's name.
- perf / scale — one extra `git config --get` spawn, about 0.75 s on node a (PINNED, measured
  2026-10-02), only on the unset path with an ssh remote and no environment trigger.
- error / empty / loading states — a failed `ssh.variant` read is a `note` that writes nothing (S2);
  an empty variable is not a trigger.
- observability — the `note` line names which of the three triggers fired.
- risks — a node exporting `GIT_SSH` for an unrelated purpose loses the keepalive; the `note` says so
  on every run, and the operator can set `core.sshCommand` themselves.
- testing — S6's arms, each failing case observed against the pre-unit checker.
- migration — none; the arm has not landed on `main`.
- user docs — the header comment (S4); the runbook is the open ask named in §3.

## 6. Acceptance criteria

Every fixture is the one `TOOL-aLevelledCopy-2`'s arms use: a git repository under a short `%TEMP%`
directory, `GIT_CONFIG_GLOBAL` at a file of the fixture's own, `GIT_CONFIG_NOSYSTEM=1`, copies of
`tools/check-wiring.sh` and `tools/push-main.sh` at the same prefix, and an `origin` of
`git@example.invalid:o/r.git`. No network is touched and nothing pushes. Each criterion is observed
by its arm run alone, as AC8 states.

- **AC1** — When `GIT_SSH=/bin/false` is exported, `core.sshCommand` is unset at every scope and
  `bash tools/check-wiring.sh --session` runs, the run prints a `note     ssh` line naming `GIT_SSH`,
  `git config core.sshCommand` prints nothing afterwards, no `FIXED    ssh` line prints, and the
  common dir's `health.log` holds no `sshcommand-set` line. Red when: the key is set, which is the
  checker's behaviour at this build's pre-unit HEAD.
- **AC2** — When only `GIT_SSH_VARIANT=ssh` is exported and `--session` runs on the same fixture, the
  `note     ssh` line names `GIT_SSH_VARIANT` and `git config core.sshCommand` prints nothing.
  Red when: the key is set.
- **AC3** — When `ssh.variant=plink` is written to the fixture's global config file, nothing is
  exported, and `--session` runs, the `note     ssh` line names `ssh.variant` and `git config
  core.sshCommand` prints nothing. Red when: the key is set.
- **AC4** — When `bash tools/check-wiring.sh --check` runs under each of AC1, AC2 and AC3's triggers
  on an otherwise wired fixture, it exits 0, prints the matching `note     ssh` line, and prints no
  `UNWIRED  ssh` line and no `Fix: git config core.sshCommand`. Red when: it exits 1 or advises the
  operator to set the key.
- **AC5** — When the run's `git` is a shim script first on its `PATH` that exits 3 for `config
  --get ssh.variant` and execs the real binary otherwise, and `--session` runs with no
  environment trigger, the run prints a `note     ssh` line containing `cannot read ssh.variant` and
  `git config core.sshCommand` prints nothing. Red when: the failed read is taken as unset and the
  key is written.
- **AC6** — When the LC2 arms written by `TOOL-aLevelledCopy-2` are run alone in a slice with
  `GIT_SSH=/bin/false` and `GIT_SSH_VARIANT=plink` exported by the caller, every one prints `ok`.
  Red when: LC2 AC1, AC2 or AC7 fails because the fixture inherited the caller's variable.
- **AC7** — When `grep -nw GIT_SSH tools/check-wiring.sh` runs, it hits the header's ssh paragraph
  and the arm, and `grep -c ssh.variant tools/check-wiring.sh` prints at least 2. Red when: the
  header still names only `GIT_SSH_COMMAND`.
- **AC8** — When each new arm is run ALONE, as the suite's prologue plus the one block in a sliced
  copy inside the kit directory, under `bash <slice>`, it prints `ok` against the built checker and
  `FAIL` against a scratch copy of the checker taken with `git show` from the commit before this
  unit's build commit. Red when: an arm prints `ok` against that copy, which means it cannot see the
  defect.
  cost: about 20 s a slice on node a; the whole suite is not run in this pass.

## 7. Gates

`check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `memory hygiene`

The close runs these once, in the bar. `tools/check-wiring.sh` trips the two arms legs; every other
guard on the two files is broad, as `check-spec-tokens.py --legs-for` prints, and the remaining legs
are named by judgment from `TOOL-aLevelledCopy-2`'s set.

New arm: tools/check-wiring.test.sh · covers AC1 AC2 AC3 AC4 AC5 · each arm run against the pre-unit checker per AC8 · none
New arm: tools/check-wiring.test.sh · covers AC6 · the caller exports GIT_SSH and GIT_SSH_VARIANT before the LC2 block, with the unset line removed from seed_ssh_fixture · none

## 8. Open questions

- **F1 — how does this spec record that it builds on `TOOL-aLevelledCopy-2`?** The brief asks for a
  §3 Edges `consumes-from` naming that unit. Options: (a) that edge, which hygiene check 12's
  reciprocity join reds unless the CLOSED spec gains a matching `hands-off` line, an edit the same
  brief rules out; (b) state the dependency in §1, §3 and §4 prose and declare no edge to it. (a)
  fails a gate already written (M3 veto 1): the join in `tools/memory-tree/check-memory-hygiene.sh`
  registers every Tier-2 spec past the edges cutoff whatever its status, so a CLOSED target still
  demands the mirror line. RESOLVED (agent, 2026-10-09, delegated): (b). The code that unit built is
  in the tree, and the edge mechanism exists for criteria resting on work not yet built.
- **F2 — which values count as the operator's choice?** Options: (a) a non-empty `GIT_SSH` only, the
  review's minimum; (b) that plus a non-empty `GIT_SSH_VARIANT` and any set `ssh.variant`, as the
  review's M1 and the brief list. (b) closes the wrong-flags case (a) leaves open, at one config read,
  and trips no veto. RESOLVED (agent, 2026-10-09, delegated): (b), with any non-empty value a trigger.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the closing review's H1 and M1 and the promotion brief.
- rev-2 · 2026-10-09 · AC5's failing `git` is a `PATH` shim, not an `export -f` function: the lexicon
  leg tokenizes code inside `$(…)` and grades a function named `git` as a definition whose name leads
  with no declared verb. S5's gate is also made unconditional: the suite exports `GIT_SSH` and
  `GIT_SSH_VARIANT` before the LC2 block, so dropping the seed's `unset` reds LC2 AC1 and AC7 on every
  node, not only on one that exports them. Status CLOSED, built.

## 10. Reuse audit

The seam is `check_ssh_keepalive` in `tools/check-wiring.sh` itself, which this unit extends, and its
own `note` vocabulary for a deliberate operator value. `python tools/codebase-map/reuse_lookup.py
"detect an operator-chosen ssh program before writing git config"` ranked only generic `git` and
`write` name stems and no ssh seam. `git grep -nw -e GIT_SSH -e GIT_SSH_VARIANT -e ssh.variant --
tools/` hit nothing on 2026-10-09, so no existing reader of these values exists to reuse. The recall
probe returned this build's brief, the closing review's H1 and the open push-main precedence ask (`TOOL-aLevelledCopy-4`), none of which holds an implementation. The fixture conventions are `seed_ssh_fixture` and the
suite's `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_NOSYSTEM` idiom, both reused unchanged.

Recall terms used: core.sshCommand GIT_SSH GIT_SSH_COMMAND ssh.variant plink operator check-wiring session overwrite keepalive push-main
