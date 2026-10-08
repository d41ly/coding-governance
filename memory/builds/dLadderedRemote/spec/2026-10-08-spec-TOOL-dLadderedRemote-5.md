# TOOL-dLadderedRemote-5 — the closing review's minors: a tighter ban, an unambiguous ladder, and prose that names the ladder

**Status:** INPROGRESS · rev-1 · 2026-10-08 · node d · Tier-2 · base 40a8b8c3 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every MEDIUM and LOW item of the round-1 closing review, built as the one batch unit the build
method's M4 prescribes. The record is
`memory/builds/dLadderedRemote/reviews/2026-10-08-review-TOOL-dLadderedRemote-2-closing-diff-round1.md`.
Its items 3 to 19 are this unit's scope.

## 2. Scope (IN)

- **S1** — items 7, 8 and 9, in both canonicals and all thirteen inline copies. The current branch is
  read from the full `symbolic-ref --quiet HEAD` with `refs/heads/` stripped. The observed branch is
  read from the full target of `refs/remotes/<remote>/HEAD` with `refs/remotes/<remote>/` stripped.
  The shell canonical treats a remote name containing whitespace as no configured remote, as the
  Python one already does. The §2d table gains four rows: a detached HEAD with two remotes, a
  `branch.<b>.remote` naming no remote, a tag sharing the branch's name, and a local branch named
  `<remote>/main`. Observed by AC1.
- **S2** — items 3, 4, 5, 10 and 11, in `tools/check-remote-literals.sh` and its self-test. The
  comment filter reads `#` everywhere and `//`, `/*` and `*` in `*.js` only. Shape 2 matches the name
  then a slash, preceded by anything but a name character, a dot, a slash or `$`. The default shape
  adds `??`, `${x-name}`, `${x:=name}` and a quoted second call argument. A new shape catches an
  unquoted assignment. The remedy shape adds `push`, `pull` and `remote.<name>.`. The `||` default
  requires a quote. The population excludes only `*selftest*.py`, `test_*.py` by basename and
  `fixtures/` directories, and it includes `skills/*.js`. Every newly caught spelling and every newly
  admitted path gets an arm. Observed by AC2, AC3.
- **S3** — item 12: the python-resolver leg's guard gains `.githooks/`. Observed by AC4.
- **S4** — items 13 and 14. On a refusal `derive_liveness` reads `unresolved`. `run-gates.sh` and
  `map_lib.resolve_compare_base` read the OBSERVED branch, never `GOV_DEFAULT_BRANCH`, as they did at
  BASE. Observed by AC5.
- **S5** — items 15, 16 and 17. `read_refs`'s docstring states that `GIT_CALLS` does not count the
  ladder's own git calls. `base_from` reads `ladder-refused` on a refusal. The govkit currency check
  resolves without `GOV_REMOTE`, because that knob names the TARGET repository's remote and never the
  gov checkout's. Observed by AC5.
- **S6** — items 6 and 18. The prose names the ladder and `GOV_REMOTE`: `tools/drift-audit/README.md`,
  `WIRE-INTO-PROJECT.md`, `skills/session-kickoff/SKILL.md`, both `test_codebase_map` files,
  `tools/codebase-map/INVENTORY-DERIVATION.md` and `tools/run-gates/README.md`. Observed by AC6.
- **S7** — item 19. Spec 3 gets a rev-2 naming the `declarations` chunk, and the budget row's figure
  is re-derived to the 60-second floor. NOT OBSERVED: record and declaration text only.

## 3. Non-goals (OUT)

- A repo-subject parity leg. The held parity rows are the existing system property item 12 names,
  and the guard widening is the in-scope part of it.
- Counting the ladder's git calls inside `GIT_CALLS`. That would change a reader's cost figure, so
  the docstring states the gap instead.
- Ban shapes beyond the ones listed in S2. The header lists what stays invisible.

### Edges

- **consumes-from** `TOOL-dLadderedRemote-3` — the ban this unit tightens
- **consumes-from** `TOOL-dLadderedRemote-2` — the consumer sites S4 and S5 amend

## 4. Design

The canonical edits are re-inlined by one script, which replaces each marked block with the
canonical's bytes. The parity rows then grade every copy. The widened ban runs over the real tree
before it is wired, and every new hit is drained in this unit or named as a by-design exclusion in
the header.

### Files touched (estimate)

- `tools/lib/resolve_remote.py`
- `tools/lib/resolve-remote.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/check-remote-literals.sh`
- `tools/check-remote-literals.test.sh`
- `tools/gate-legs.json`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/selftest-budgets.txt`
- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/selftest.py`
- `tools/unattended/unattended.sh`
- `tools/runlog/model.py`
- `tools/govkit/govkit.py`
- `tools/drift-audit/README.md`
- `WIRE-INTO-PROJECT.md`
- `skills/session-kickoff/SKILL.md`

## 5. Production-readiness checklist

- security: S5's currency change narrows what the environment can steer.
- perf / scale: unchanged; two `symbolic-ref` calls read full refs instead of short ones.
- error / empty / loading states: S1 makes two refusal texts graded; S5 names a refused base.
- observability: `base_from` distinguishes a refusal from no remote.
- risks: the widened ban may hit current code; it is run over the tree before it is wired.
- testing: four new table rows, new ban arms, a map selftest arm for the environment.
- migration: none.
- user docs: S6 is the docs item.

## 6. Acceptance criteria

- **AC1** — When `resolve_remote` and `resolve_remote_sh` run over the §2d table's twelve rows, both
  print each row's expected answer. Red when: a staged break restoring `--short` in either canonical
  makes the tag row differ.
- **AC2** — When the ban's self-test plants a `*)` case arm, `${x#origin/}`, `removeprefix("origin/")`,
  a defaulted `.get`, `${R:=origin}`, an unquoted assignment, `git push origin`, a `skills/*.js` file
  and a product file named `latest_probe.py`, `check-remote-literals.sh` names each. Red when: one
  stays unnamed.
- **AC3** — When it plants a variable named `origin` used as `$origin/HEAD` or `x || origin.kind`,
  `check-remote-literals.sh` stays clean, and over the real tree it exits 0. Red when: either names a
  line.
- **AC4** — When `tools/gate-legs.json` is read, the python-resolver leg's guard lists `.githooks/`.
  Red when: it does not.
- **AC5** — When `GOV_DEFAULT_BRANCH` names a branch other than the observed one,
  `resolve_compare_base` still returns the observed branch's base. Red when: the environment moves it.
- **AC6** — When `git grep` runs over the S6 files for `set-head origin` and `origin/HEAD`, it finds no
  remedy line, and `WIRE-INTO-PROJECT.md` names `GOV_REMOTE`. Red when: a stale line remains.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `remote literals (kit code names no remote)` · `remote literals self-test` · `codebase-map kit selftest` · `run-gates canary` · `runlog selftest` · `govkit selftest` · `drift-audit selftest` · `every held leg is budgeted, every budget row resolves` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `pre-push run-log line` · `run-gates run-log line` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor arms` · `run-gates gov canary` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/lib/resolve-python.test.sh · covers AC1 · `--short` restored in one canonical · none
New arm: tools/check-remote-literals.test.sh · covers AC2 AC3 · one pattern removed at a time · FLOOR_ASSERTIONS
New arm: tools/codebase-map/selftest.py · covers AC5 · GOV_DEFAULT_BRANCH naming another branch · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft, from the round-1 closing review.

## 10. Reuse audit

Every item amends a seam this build already added: the canonicals, the ban, and the consumer sites
of unit 2. `python tools/codebase-map/reuse_lookup.py "choose the remote and its default branch for a landed ref"`
found nothing beyond them.
Recall terms used: remote origin GOV_REMOTE GOV_DEFAULT_BRANCH set-head default branch ladder push-main resolve_base tracking ref stale local
