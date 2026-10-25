# TOOL-dWitnessedBar-50 — the wrong-shell population is a stated predicate, the commit hook among its members

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 3 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 50 at HIGH**, its item **H11**, alone in that item. `.githooks/pre-commit` sources
`resolve-python.sh` dynamically (`. "./$r"`) and calls `resolve_python` (`.githooks/pre-commit:239`), but
`TOOL-dWitnessedBar-27`'s 75-entry population omits it. Unit 27 pins five files naming
`resolve-python.sh` beyond the inline carriers where there are ten, three of which (`govkit.py`,
`registry.toml`, `corpus_ids.py`) cannot carry a bash call; its arm's "sources" predicate is never
stated, and AC5 greps only `^# >>> resolve_python`. Built to the list, the hook a WSL user meets on
`git commit` in a `/mnt/c` checkout gets no refusal while AC5 stays green. This unit takes the skeptic's
corrected fix. It repairs `TOOL-dWitnessedBar-27`.

## 2. Scope (IN)

- **S1** — The predicate, stated. The population is every tracked shell file under `tools/`, `skills/`
  and `.githooks/`, a shell file being one named `*.sh` or whose first line is a `bash` or `sh` shebang,
  that carries a `# >>> resolve_python` block or calls `resolve_python` at command position (`$(resolve_python`
  or a line beginning `resolve_python`) outside such a block. The canonical `tools/lib/resolve-python.sh`
  is outside it. Observed by AC1.
- **S2** — The named exclusion. `tools/unattended/lib-unattended.sh` is outside the population: it is
  sourced by `tools/unattended/unattended.sh`, which refuses first, and its one call is guarded by
  `declare -F resolve_python` (`:190`). The arm prints the exclusion and its reason on every run, and
  refuses a second exclusion added without one. Observed by AC1.
- **S3** — The members unit 27 did not list. `.githooks/pre-commit` carries the `refuse_wrong_shell`
  block inline and calls `refuse_wrong_shell || exit 2` before any work; `tools/check-line-length.sh` and
  `tools/playbook/adopt-playbook.sh`, which define an unmarked `resolve_python` of their own and call it,
  do the same. Observed by AC2.
- **S4** — The arm derives, never lists. `bash tools/lib/refuse-wrong-shell.sh --coverage` derives the
  population from S1, prints its count and the named exclusion, and exits 1 naming each member that
  neither carries the refusal block nor sources `refuse-wrong-shell.sh`, or that never calls
  `refuse_wrong_shell || exit 2`; unit 27's coverage arm in `tools/lib/resolve-python.test.sh` runs it. Files naming
  `resolve-python.sh` that the predicate leaves out, `tools/govkit/govkit.py`,
  `tools/govkit/registry.toml`, `tools/memory-tree/corpus_ids.py` and `.githooks/pre-commit.test.sh`,
  are outside by the predicate, never by a list. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- The predicate `wrong_shell_at`, its block, its twins and the edits to the inline carriers unit 27
  already lists: `TOOL-dWitnessedBar-27`'s.
- The order of the refusal against each member's first `resolve_python` call: the minors batch's id 51
  (`TOOL-dWitnessedBar-51`), which asserts it over this unit's population.
- Records under `memory/builds/*/build/*.sh`: outside `tools/`, `skills/` and `.githooks/`.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-27` — `refuse-wrong-shell.sh`, its block and the coverage arm in `tools/lib/resolve-python.test.sh`, whose population this unit states as a predicate
- **hands-off** `TOOL-dWitnessedBar-51` — the derived population of S1, over which the minors batch's id 51 item asserts the refusal precedes the first `resolve_python` call
- **hands-off** `TOOL-dWitnessedBar-57` — the derived population and `--coverage`, whose call predicate, pin, stub case and dropped canonical the resolver and ledger minors batch states (ids 5, 6, 19, 51)

## 4. Design

### Evidence

- `.githooks/pre-commit:234-239`: `r=$(git ls-files -- '*resolve-python.sh' | head -n 1)`, then
  `. "./$r"` and `py=$(resolve_python)`.
- The ten files outside `tools/lib/resolve-python.sh` that name `resolve-python.sh` and carry no block,
  by `git grep -l` at `cdfbd1cf`: `.githooks/commit-msg`, `.githooks/pre-commit`,
  `.githooks/pre-commit.test.sh`, `.githooks/straggler-guard.test.sh`, `tools/govkit/govkit.py`,
  `tools/govkit/registry.toml`, `tools/lib/pyrun.sh`, `tools/lib/resolve-python.test.sh`,
  `tools/memory-tree/corpus_ids.py` and `tools/memory-tree/transition-audit.test.sh` (PINNED,
  measured 2026-10-25).
- S1's predicate over the tree at `cdfbd1cf` yields 78 members: 69 shell files carrying the block, and
  nine calling `resolve_python` without one, `.githooks/commit-msg`, `.githooks/pre-commit`,
  `.githooks/straggler-guard.test.sh`, `tools/check-line-length.sh`, `tools/lib/pyrun.sh`,
  `tools/lib/resolve-python.test.sh`, `tools/memory-tree/transition-audit.test.sh`,
  `tools/playbook/adopt-playbook.sh` and `tools/unattended/lib-unattended.sh` (PINNED, measured
  2026-10-25 with a shell probe of S1; the arm re-derives it at every run). S2 takes the last out, so 77.

### Inventory

Minted: the `--coverage` mode of `refuse-wrong-shell.sh`, the predicate's statement and the one named
exclusion. Naming cells: the flag is asked of `python tools/lexicon/lexicon.py --suggest coverage --as
cli.flag` at the pass.

### Migration

None.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-27`.

### Files touched (estimate)

- `tools/lib/refuse-wrong-shell.sh`
- `tools/lib/resolve-python.test.sh`
- `.githooks/pre-commit`
- `tools/check-line-length.sh`
- `tools/playbook/adopt-playbook.sh`

### Alternatives rejected

- **A literal `resolve-python.sh` grep.** It reds forever on the three non-shell files that only name it.
- **A typed list of members.** The defect this unit closes is a list that missed one.

## 5. Production-readiness checklist

- security — the commit hook, the first gov script a WSL user meets, now refuses the wrong shell.
- perf / scale — the refusal is builtins only, no fork.
- error / empty / loading states — an empty derived population reds the arm, never passes it.
- observability — the arm prints the population count, the exclusion and its reason.
- risks — a new sourced library calling `resolve_python` reds until it carries the refusal or is named
  with a reason.
- testing — AC1 to AC3 by probe and a scratch-clone plant; the arm of §7 at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `bash refuse-wrong-shell.sh --coverage` runs in `tools/lib/` on the built tree, it prints the
  derived population count, names `tools/unattended/lib-unattended.sh` excluded with its reason, and
  exits 0; `grep -c 'refuse_wrong_shell || exit 2' .githooks/pre-commit` prints 1.
  Red when: the population is a typed list, so `.githooks/pre-commit` is not a member.
- **AC2** — When `wsl.exe -e bash .githooks/pre-commit` runs with its working directory at this
  worktree's root on node d, it exits 2 with the `refuse_wrong_shell:` lines before any other output.
  Red when: the commit hook resolves python under WSL over `/mnt/` with no refusal.
  fixture: a Windows node with WSL; node d has one.
- **AC3** — When `bash refuse-wrong-shell.sh --coverage` runs from `tools/lib/` in a scratch clone with
  `.githooks/pre-commit`'s refusal call cut, it exits 1 naming that file; with a new shell file under
  tools/ calling `$(resolve_python)` and carrying no block, it names that file too.
  Red when: a dynamic-source caller with no inline block escapes the arm.
  fixture: a scratch clone under `%TEMP%/<short-name>`.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `line-length gate selftest` · `playbook render wiring` · `playbook render selftest` · `memory hygiene` · `govkit acceptance matrix`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC3 · the coverage arm running `refuse-wrong-shell.sh --coverage` over S1's derived population, staged red by cutting `.githooks/pre-commit`'s call and by a planted caller with no block · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-27`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Is a sourced library that calls `resolve_python` a member?** Options: (a) outside, named with
  its reason, since its sourcer refuses first; (b) a member, carrying the refusal itself. (b) puts an
  `exit 2` into a file whose sourcer already refused, which can only fire where the sourcer's did.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one exclusion printed on every run.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 50 (HIGH, item H11).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seams are unit 27's `refuse-wrong-shell.sh`, which gains the `--coverage` mode beside its `--probe`,
and its coverage arm in `tools/lib/resolve-python.test.sh`, whose population this unit derives from a
predicate in place of a list. `python tools/codebase-map/reuse_lookup.py "derive the entry
points that must refuse a wrong shell"` ranked `CensusRefused`, `ScopeRefused`,
`derive_baseline_additions` and other `derive_*` stems, none a shell-entry census; no existing seam fits
beyond the arm.

Recall terms used: `python tools/memory-recall/query.py "which shell entry points must refuse WSL bash on a windows checkout" --terms "refuse_wrong_shell pre-commit resolve_python population coverage arm entry point WSL mnt predicate"`
