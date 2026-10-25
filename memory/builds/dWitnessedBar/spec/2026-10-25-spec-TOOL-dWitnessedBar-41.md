# TOOL-dWitnessedBar-41 — the selection a bar ran under travels on the per-tree verdict, and the hook re-derives it before adopting

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 22 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 59 at HIGH**, its item **H2**, alone in that item. `TOOL-dWitnessedBar-5` S7 has
the hook re-derive a selection only for "a verdict whose run record holds a `selection`". Run records
sit in the per-worktree `<git-dir>/gate-run/<run id>/` (`tools/run-gates/run-gates.sh:2601`) and are
swept past `GATE_RUN_KEEP` (`:5692-5695`). The verdict the hook adopts is `TOOL-dWitnessedBar-4`'s
per-tree record in the shared `<common-dir>/gate-verdict/`, which names no selection. A bar run in
worktree A under a `GATE_SELECTION` holding legs writes a GREEN per-tree verdict; a push of the same tree
from worktree B, or after A's run dir is swept, finds no run record and adopts the GREEN without
re-deriving. This unit takes the report's fix. It repairs `TOOL-dWitnessedBar-5`.

## 2. Scope (IN)

- **S1** — The selection on the per-tree record. Unit 4's per-tree record gains `selection`, the
  `git hash-object` of the canonical selection text (§4 "The canonical text"), or `none` when the run
  read no `GATE_SELECTION`, and one `selection.<n>` key per `held` row the runner read, `<n>` an index
  from 1, its value `<leg name> · <source> · <note>`. Observed by AC1.
- **S2** — The hook re-derives from the record. Before it adopts a per-tree record, the hook reads its
  `selection`: `none` adopts as the other predicates say; a hash rebuilds the canonical text from the
  `selection.<n>` keys, refuses when its hash differs from `selection`, and otherwise runs
  `python tools/run-gates/verdict_flow.py select --check --selection <file> --rev <R>` over the rebuilt
  text, adopting only on exit 0. Observed by AC2 and AC3.
- **S3** — Absent means refused. A per-tree record carrying no `selection` key is not adopted, because it
  cannot say whether its bar held legs. Observed by AC3.
- **S4** — `select --check` reads a file. `verdict_flow.py select --check` gains `--selection <path>`
  beside unit 5's `--run <run dir>`, comparing the file's `held` rows with a fresh derivation at R as the
  `--run` form compares the run record's copy. Observed by AC2.

## 3. Non-goals (OUT)

- The selection record, `select`, `SELECT_SOURCES` and the hold predicate: `TOOL-dWitnessedBar-5`'s.
- The per-tree record's other keys and its write rule: `TOOL-dWitnessedBar-4`'s and
  `TOOL-dWitnessedBar-40`'s.
- Retaining run records across worktrees: the per-tree record now carries what the hook reads, so no
  run record is needed at the push.
- A spec-set lint that every key the hook's adoption predicate reads appears in unit 4's key table, the
  report's left-shift: no clause of this build names it, and AC3 is the arm for this key.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-5` — `verdict_flow.py select --check` and the selection record's row grammar, which the hook runs over the rebuilt selection
- **consumes-from** `TOOL-dWitnessedBar-4` — the runner's per-tree record and the hook's adoption of it, which gain the `selection` keys and the re-derivation
- **hands-off** `TOOL-dWitnessedBar-56` — the `selection` keys, their canonical text and the hook's rebuild, which the verdict-boundary minors batch makes lossless over the accepted rows (ids 2, 3, 16, 33, 47)

## 4. Design

### Evidence

- Run records: `RUNROOT="$gd/gate-run"` (`run-gates.sh:2601`), `$gd` the worktree's own git dir, and
  the sweep keeps the newest `GATE_RUN_KEEP` (`:5692-5695`).
- The per-tree record lives under the common dir, resolved as the `.shared` stamp resolves it
  (`RG_COMMON_RAW`, `run-gates.sh:113-117`), so every worktree reads one directory
  (`TOOL-dWitnessedBar-4` §4 "The record").
- Unit 5's selection rows are `held<TAB><leg name><TAB><source><TAB><note>` under a `#` header naming
  the values read (`TOOL-dWitnessedBar-5` §4 "The selection record"), and its separator ` · ` is refused
  in a leg name.

### The canonical text

The `held` rows of the file `GATE_SELECTION` named, in file order, each `held<TAB><leg><TAB><source><TAB><note>`
and LF-terminated, the header and any other line dropped. The runner hashes it with
`git hash-object --stdin`; the hook rebuilds it from `selection.1` onward, each ` · ` turned back into a
TAB, and hashes it the same way. A mismatch means a key was edited or lost, and the record is refused.

```
selection	<blob id of the canonical text>      or      selection	none
selection.1	unit-heavy suite · level · e2e outside tests.landing-levels
selection.2	flaky leg · quarantine · TOOL-x-7
```

### Inventory

Minted: the per-tree keys `selection` and `selection.<n>`; the flag `--selection` of
`verdict_flow.py select --check`. Naming cells: the flag is asked of `python tools/lexicon/lexicon.py
--suggest selection --as cli.flag` at the pass.

### Migration

A per-tree record written before this pass carries no `selection` and is not adopted (S3); the first
push of such a tree runs its bar.

### Rollout

Live at landing; the runner, the hook and `verdict_flow.py` change in one commit.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/verdict_flow.py`
- `tools/run-gates/run-gates.evidence.test.sh`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`

### Alternatives rejected

- **Key the selection by hash under the common dir.** A second directory needs its own retention rule,
  and a record whose selection file was swept is refused anyway; the record carrying its own rows has
  nothing to sweep.
- **Retain run records across worktrees for the hook.** It keeps every worktree's run dirs alive for
  the one key the per-tree record can carry itself.

## 5. Production-readiness checklist

- security — closes a fail-open path: a loosening made in one worktree is re-derived at R before any
  worktree adopts its GREEN, and a record that cannot say whether it held legs is refused.
- perf / scale — a few keys per record; `select --check` runs only for a record whose `selection` is a
  hash.
- error / empty / loading states — absent key: refused; hash mismatch: refused naming it; `--check` exit
  1: refused naming the row R does not derive.
- observability — the hook's line names which of the three refused the record.
- risks — a push of a tree whose bar held a quarantined leg now pays one `select --check` run.
- testing — AC1 to AC3 by fixture; the arms of §7 at the close.
- migration — §4.
- user docs — `tools/run-gates/README.md`'s verdict section names the keys at the pass; no page under
  `help/` covers the boundary.

## 6. Acceptance criteria

- **AC1** — When the runner makes a full run over a fixture manifest in a clean scratch clone with
  `GATE_SELECTION` naming a file holding one `quarantine` row, the per-tree record holds
  `selection.1` naming that leg and a `selection` equal to `git hash-object` of the canonical text; with
  no `GATE_SELECTION` it holds `selection none`.
  Red when: the per-tree record omits the selection, so another worktree cannot see it.
  fixture: a scratch clone under `%TEMP%/<short-name>`; the tree holds none.
- **AC2** — When `.githooks/pre-push` runs from a second worktree of that clone, with the first worktree's
  run dir removed, over a GREEN record whose selection holds a row R does not derive, it runs the bar
  and names the row; with a row R does derive it adopts the record; and
  `python verdict_flow.py select --check --selection <file> --rev <R>` exits 1 and 0 on the same two files.
  Red when: the hook adopts a GREEN made under a selection nothing re-derived.
- **AC3** — When the per-tree record's `selection.1` is edited after the run, or its `selection` key is
  deleted, the hook runs the bar and names the reason.
  Red when: an edited or keyless record is adopted.

## 7. Gates

`measure-legs selftest` · `pre-push self-test` · `pre-push bar self-test` · `run-gates canary` · `run-gates evidence` · `memory hygiene`

New arm: .githooks/pre-push.test.sh · covers AC2 AC3 · a push from a second worktree with the first's run dir removed over a record whose selection R does not derive, then an edited and a keyless record, staged red by skipping the re-derivation · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 · a full run under a one-row selection on a scratch clone, staged red by dropping the `selection` keys from the writer · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-5`'s clause, which would split a
  clause that unit carries whole. (b) reds the parts join; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none ·
  relaxes: none
- **F2 — Where do the selection's rows live for the hook?** Options: (a) as `selection.<n>` keys on the
  per-tree record itself, with a hash for integrity; (b) a content-addressed file under
  `<common-dir>/gate-selection/`; (c) the run record, retained across worktrees. (b) needs a retention
  rule of its own; (c) keeps every run dir alive for one key. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3, the record's own additive-key grammar. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 59 (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-56, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seams extended are unit 4's per-tree record and its additive `<key>TAB<value>` grammar, and unit 5's
`select --check`, given a file form. `python tools/codebase-map/reuse_lookup.py "carry a held-leg
selection with the verdict another worktree adopts"` ranked `legs`, `leg`, `adopt`,
`add_scratch_worktree` and `parse_verdicts`, none of which carries a record across worktrees; no
existing seam fits beyond the two named.

Recall terms used: `python tools/memory-recall/query.py "how does a held-leg selection travel with a verdict adopted from another worktree" --terms "GATE_SELECTION selection record held leg select check common-dir gate-verdict worktree adopt witness"`
