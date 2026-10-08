# TOOL-dLadderedRemote-1 — the remote ladder has one canonical per language, and one truth table holds both

**Status:** INPROGRESS · rev-1 · 2026-10-08 · node d · Tier-2 · base 40a8b8c3 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md](../build/2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md) | journal | TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 |
| [2026-10-08-review-TOOL-dLadderedRemote-2-closing-diff-round1.md](../reviews/2026-10-08-review-TOOL-dLadderedRemote-2-closing-diff-round1.md) | diff-review | TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 |

<!-- /gen:spec-records -->

## 1. Goal

The question "which remote does landed mean, and what is its default branch" gets one answer,
written once per language in the lib dir and inlined byte-identical everywhere. The answer is the
lander's ladder from `TOOL-aRepatriatedFork-8` S1, so a node whose remote is not named `origin`
resolves instead of refusing.

## 2. Scope (IN)

- **S1** — `tools/lib/resolve_remote.py`, the Python canonical: a module docstring and one marked
  block defining `resolve_remote(root)`, which returns `(remote, branch, observed, refusal)`.
  Observed by AC1, AC2, AC3, AC4.
- **S2** — `tools/lib/resolve-remote.sh`, the shell canonical: one marked block defining
  `resolve_remote_sh`, which sets `RR_REMOTE`, `RR_BRANCH`, `RR_OBSERVED` and `RR_WHY` and returns 1
  on a refusal. Its git command is `${RR_GIT:-git}`, so a caller holding a pinned wrapper passes it.
  Observed by AC1, AC2, AC3, AC4.
- **S3** — two rows in the parity table of `tools/lib/resolve-python.test.sh`, `resolve_remote` and
  `resolve_remote_sh`, each with its canonical file and excluded prefix. Observed by AC5.
- **S4** — a behaviour arm, `§2d`, in the same file: eight git fixtures, both canonicals run over
  each, and both must print the table's expected `remote|branch|observed|refusal` row. Observed by
  AC1, AC2, AC3, AC4.
- **S5** — `tools/push-main.sh` replaces its own remote and branch selection with an inline copy of
  the shell block. It keeps its exit codes and its two existing messages' remedies. Observed by AC6.

## 3. Non-goals (OUT)

- Any other consumer. They are unit 2.
- Fetching. The ladder reads configuration and local refs only, as every site does today.
- A rung that guesses among several remotes, such as `checkout.defaultRemote` or "the one remote
  carrying a HEAD symref". The handoff names `GOV_REMOTE` as the one new knob.
- The unattended authorization anchor. Its check 24 one-remote rule and `observe_remote` are untouched.

### Edges

- **hands-off** `TOOL-dLadderedRemote-2` — the inline copies at every other site, which turn the
  parity rows' populations from one file into thirteen
- **hands-off** `TOOL-dLadderedRemote-3` — the ban that stops a literal from coming back

## 4. Design

### The ladder

| Rung | Value | Answer |
|---|---|---|
| remote 1 | `GOV_REMOTE`, when non-empty | that name |
| remote 2 | `branch.<current>.remote`, when HEAD is on a branch and the value is not `.` | that name |
| remote 3 | `git remote` lists exactly one | that one |
| refusal A | `git remote` lists two or more and no rung above chose | refusal naming `GOV_REMOTE` |
| refusal B | the chosen name is not in `git remote` | refusal naming the rung that chose it, and `GOV_REMOTE` |
| no remote | `git remote` lists none and nothing was chosen | remote empty, NO refusal |
| observed | `refs/remotes/<remote>/HEAD`'s target, `<remote>/` stripped | that branch, or empty |
| branch | `GOV_DEFAULT_BRANCH` when non-empty, else observed | that branch, or empty |

A refusal empties remote, branch and observed, so no caller can pick a remote the ladder refused.
No remote is not a refusal: drift-audit's local fallback, render's local `main`/`master` and
run-gates' fail-safe "run" all live beneath that answer, and unit 2 keeps each of them.
`GOV_DEFAULT_BRANCH` is read verbatim, so a caller that only CROSS-CHECKS it compares it with
`observed`, and a caller that lets it select reads `branch`.

### The refusal text, one spelling in both languages

```
cannot choose a remote: GOV_REMOTE is unset, <where> has no configured remote, and this repository has <n> remotes (<names>). Name it: export GOV_REMOTE=<remote>.
<how> names <remote>, which is no remote of this repository (<names|none>). Name one that is: export GOV_REMOTE=<remote>.
```

`<where>` is `branch <name>` or `a detached HEAD`. `<names>` is the remote list joined by single
spaces. `<how>` is `GOV_REMOTE` or `branch.<name>.remote`. Neither block carries a single quote,
so either can sit inside a single-quoted program a caller embeds.

### The behaviour arm's table

| # | Fixture | Env | Expected `remote|branch|observed|refusal` |
|---|---|---|---|
| 1 | one remote `incms`, `incms/HEAD` names `incms/main` | none | `incms|main|main|` |
| 2 | remotes `incms` and `origin`, a branch with no upstream | none | `|||cannot choose a remote: …` |
| 3 | fixture 2 | `GOV_REMOTE=incms` | `incms|main|main|` |
| 4 | fixture 2, the branch's remote set to `origin`, `origin/HEAD` names `origin/trunk` | none | `origin|trunk|trunk|` |
| 5 | fixture 1 | `GOV_REMOTE=nosuch` | `|||GOV_REMOTE names nosuch, …` |
| 6 | no remote | `GOV_DEFAULT_BRANCH=dev` | `|dev||` |
| 7 | one remote `r`, no HEAD symref | `GOV_DEFAULT_BRANCH=main` | `r|main||` |
| 8 | fixture 1, the branch's remote set to `.` | none | `incms|main|main|` |

The refusal column compares the whole text, so the two canonicals cannot drift in wording.

### Inventory

New identifiers: `resolve_remote` in cell `py.function` and `resolve_remote_sh` in cell
`sh.function`, both answered OK by `tools/lexicon/lexicon.py --suggest`. New globals `RR_REMOTE`,
`RR_BRANCH`, `RR_OBSERVED`, `RR_WHY` and the caller knob `RR_GIT`. New marker stems
`resolve_remote` and `resolve_remote_sh`.

### Files touched (estimate)

- `tools/lib/resolve_remote.py`
- `tools/lib/resolve-remote.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`

### Alternatives rejected

- One shared module imported at run time. Kits may not import a sibling kit and the lib dir ships
  nothing, as the `resolve_compare_base` docstring in `tools/codebase-map/map_lib.py` records.
- A shell canonical only, with Python callers shelling out to it. Seven Python consumers would each
  spawn bash, and an adopter's Windows node may resolve a different shell.

## 5. Production-readiness checklist

- security: the ladder reads two environment values. `GOV_REMOTE` can steer a probe to another
  configured remote's tracking ref, which is the same reach `GOV_DEFAULT_BRANCH` already has. No
  authorization path reads the ladder; unit 2's unattended edits stay off it.
- perf / scale: at most four git calls per resolution.
- error / empty / loading states: refusal, no remote and no branch are three distinct answers.
- observability: the refusal text names the knob that fixes it.
- risks: a clone with two remotes and a branch without an upstream used to read `origin` silently
  and now refuses. Gov's four registered nodes have one remote each.
- testing: the behaviour arm plus the parity rows; push-main's own suite for S5.
- migration: none; an adopter receives the inline copies through `govkit update`.
- user docs: N/A — no user-facing surface; the knob is documented beside push-main's existing text.

## 6. Acceptance criteria

- **AC1** — When `resolve_remote` and `resolve_remote_sh` run over the §2d table's fixture 1, both
  print `incms|main|main|`. Red when: either prints an empty remote or reads `origin`.
- **AC2** — When it runs fixture 2, both print the `cannot choose a remote` refusal naming
  `GOV_REMOTE`, with remote, branch and observed empty. Red when: either picks a remote.
- **AC3** — When it runs fixture 3, both resolve `incms` although `origin` exists. Red when: either
  answers `origin` or refuses.
- **AC4** — When it runs fixtures 4 to 8, every row matches the table. Red when: a staged break that
  drops rung 2 from `resolve_remote` makes row 4 differ.
- **AC5** — When one byte of the inline copy in `tools/push-main.sh` is changed, the parity loop
  names that file for `resolve_remote_sh`. Red when: the loop stays silent.
- **AC6** — When `tools/push-main.sh` runs with two remotes and none configured, it still refuses
  with exit 2 naming `GOV_REMOTE`. Red when: the message or the exit code moved.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 AC4 · a staged break dropping rung 2 from one canonical · none
New arm: tools/lib/resolve-python.test.sh · covers AC5 · a one-byte edit to the push-main copy · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft.

## 10. Reuse audit

The seam extended is the lander's inline ladder at `tools/push-main.sh` lines 102 to 125, promoted
to the lib dir by the `resolve_kit_dir` precedent of `TOOL-aRepatriatedFork-2` S3 and the two-canonical
health log of `TOOL-aGraftedHelix-8`, both in the parity table of `tools/lib/resolve-python.test.sh`.
`python tools/codebase-map/reuse_lookup.py "choose the remote and its default branch for a landed ref"`
returned no seam that fits: its candidates were landing-fact readers, not a remote resolver.
Recall terms used: remote origin GOV_REMOTE GOV_DEFAULT_BRANCH set-head default branch ladder push-main resolve_base tracking ref stale local
