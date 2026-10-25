# TOOL-dWitnessedBar-61 — the seed stamps the null SHA when HEAD is unborn, so a before-first-commit seed writes rows the ledger reads

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 5 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 |
| [2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 52 to 57
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md`)
confirmed finding **id 35 at HIGH**, its item **H4**. The same defect is id 2 at MEDIUM, item **M2**,
which the minors batch `TOOL-dWitnessedBar-62` takes. `TOOL-dWitnessedBar-15` S1 defaults the seed's
`--sha` to HEAD and stamps it on every row and on the unarmed line; `TOOL-dWitnessedBar-13`'s row grammar
needs an SHA of 8 to 40 hex. The fixtures that prove the before-first-commit path, unit 53's arm and unit
52's AC1, seed in a fresh `git init` where HEAD is unborn and `git rev-parse HEAD` exits 128. No spec says
what the seed writes then, so it either fails, leaving the population unarmed, or writes a row the reader
refuses. The report asks for the rule in unit 52 or as a hands-off to unit 15; the rule belongs to the
seed verb, so this unit states it there, one step after unit 15 and before every unit that seeds on an
uncommitted tree. It repairs `TOOL-dWitnessedBar-15`.

## 2. Scope (IN)

- **S1** — The unborn rule. `seed` takes its SHA from `--sha` when given; otherwise from
  `git rev-parse --verify --quiet HEAD`; and when that exits non-zero with nothing printed, from the null
  SHA, forty `0` characters, which unit 13's grammar admits. Every row and every `# unarmed` line that run
  writes carries it, and the run prints `seed: HEAD is unborn, rows carry the null SHA` once. A git
  failure other than an unborn HEAD, such as no repository, is unit 15's unarmed path with its reason.
  Observed by AC1.
- **S2** — Never re-dated. A present armed home whose rows carry the null SHA is left byte-identical by
  a later `seed` after the first commit, as unit 15's absent-only rule leaves every present home; the
  null SHA records that the row was seeded before any commit. A `--widen` run appends its new keys at
  the new HEAD. Observed by AC2.
- **S3** — The reader admits the row. `read_rows` parses a row whose SHA is the null SHA, and the
  unarmed-line reader parses an unarmed line carrying it. Observed by AC1.

## 3. Non-goals (OUT)

- The seed verb, its state table and its absent-only rule: `TOOL-dWitnessedBar-15`'s.
- The row grammar: `TOOL-dWitnessedBar-13`'s. The null SHA needs no change to it.
- Unit 53's arm compare and its statement that the re-seed stamps the new commit: the minors batch's id 2
  item (`TOOL-dWitnessedBar-62`).
- An `unborn` token in the SHA column (the report's other example): unit 13's reader would need a second
  shape for one column.
- The report's left-shift text, a bug-class checklist entry "a tool defaults to HEAD with no unborn-repo
  rule": a gate no clause of this build names. S1's arm and unit 53's arm run the seed in a commitless
  `git init`.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-15` — `seed_population`, its `--sha` default and its unarmed line, whose SHA in an unborn repository S1 defines
- **hands-off** `TOOL-dWitnessedBar-47` — the unborn rule, under which a fresh `git init` target's seed writes rows before anything is committed
- **hands-off** `TOOL-dWitnessedBar-52` — the unborn rule, under which AC1's scaffold seed in a commitless `git init` writes a row the leg reads
- **hands-off** `TOOL-dWitnessedBar-53` — the unborn rule, under which the arm's first `seed --all` before the commit arms each population it lists
- **hands-off** `TOOL-dWitnessedBar-62` — the null SHA on the rows seeded before the commit, which the minors batch's id 2 item asserts beside the re-seed's HEAD
- **hands-off** `TOOL-dWitnessedBar-63` — the other-failure row routed to unit 15's refused-home branch, the unborn predicate on exit code, stdout and stderr together, the unborn line on stderr, a validated `--sha`, and the sequence before unit 47 observed at the close (ids 2, 5, 13, 24, 31, 32)

## 4. Design

### Evidence

- In a scratch `git init` with nothing committed, `git rev-parse --verify -q HEAD` exits 1 printing
  nothing and `git rev-parse HEAD` exits 128 (the report's id 35 reproduction).
- The repository's existing unborn rule: `read_worktree_head` runs
  `git rev-parse --verify --quiet HEAD` and returns `None` on an unborn HEAD rather than raising
  (`tools/memory-recall/query.py:258-271`); the runner suite asserts "an unborn HEAD reads empty, never
  the word HEAD" (`tools/run-gates/run-gates.evidence.test.sh:2256`).
- The null SHA is already the suites' spelling of "no commit"
  (`.githooks/pre-push.test.sh:238`, `.githooks/pre-push.runlog.test.sh:209`).
- Unit 14 S9 compares a surviving row's SHA with the base's, so a null SHA unchanged since the base is
  not a re-dating; no reader dereferences the row SHA as a commit.

### The rule

| `--sha` | `rev-parse --verify -q HEAD` | SHA stamped |
|---|---|---|
| given | not run | the given value |
| absent | exits 0, prints `<sha>` | `<sha>` |
| absent | exits 1, prints nothing (unborn) | `0000000000000000000000000000000000000000` |
| absent | any other failure | none: unarmed, reason `no HEAD: <stderr line>` |

### Inventory

Minted: the line `seed: HEAD is unborn, rows carry the null SHA`; the reason `no HEAD`. Nothing else.

### Migration

None: no population has been seeded under the factory yet.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-15`. It shares order 5 with
`TOOL-dWitnessedBar-47`, whose fresh `git init` targets read this rule and which writes the same
`legacy_ledger.py`, so the main loop sequences this unit first within the step (BUILD-METHOD M6,
clauses 1 and 2).

### Files touched (estimate)

- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`
- `tools/lib/resolve-python.test.sh`

### Alternatives rejected

- **The scaffold fixture commits once before copying the kit.** It models an existing project only, and
  leaves a real first adoption into an empty repository with no defined seed.
- **Refuse to seed on an unborn HEAD.** The population would start unarmed on exactly the path units 47,
  52 and 53 exist to arm.

## 5. Production-readiness checklist

- security — no new write path; the same homes, written through `write_rows`.
- perf / scale — one `rev-parse` per seed run, as before.
- error / empty / loading states — an unborn HEAD seeds with the null SHA; any other git failure is
  unarmed with its reason, never a partial file.
- observability — S1's one line names the unborn case on the run that met it.
- risks — a row seeded before the first commit carries no commit to blame; the line says so.
- testing — AC1 and AC2 by fixture; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`; the module docstring states the rule.

## 6. Acceptance criteria

- **AC1** — When `python legacy_ledger.py seed --population p` runs in a fixture `git init` with nothing
  committed, it prints `armed p 2` and `HEAD is unborn`, each row's fourth field is forty `0`
  characters, and `read_rows` over the home returns two rows; with the seed made to exit 1, the
  `# unarmed` line carries the same SHA and the unarmed reader parses it.
  Red when: the seed dies on `rev-parse HEAD`, leaves the home unarmed, or writes the word `HEAD`.
  fixture: a scratch `git init` under `%TEMP%/<short-name>`, built by section `2l` of the suite.
- **AC2** — When that fixture is committed and `seed --population p` runs again, it prints `present p`
  and the home is byte-identical; with `--widen R1` and a third key, the new row carries the new HEAD and
  the first two keep the null SHA.
  Red when: a later seed re-dates the null-SHA rows.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest` · `memory hygiene`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 · section `2l` gains a commitless `git init` seed and its first-commit re-run, staged red by restoring the bare HEAD default · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-15`'s clause, splitting a clause the
  roster unit carries whole. (b) reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — What does the seed stamp on an unborn HEAD?** Options: (a) the null SHA, which unit 13's grammar
  admits; (b) a token such as `unborn`, with unit 13's reader widened; (c) refuse, unarmed; (d) leave it
  to the fixtures, which commit first. (c) unarms the populations units 47, 52 and 53 exist to arm, and
  (d) leaves a real empty repository undefined; veto 1 discards both against unit 52's AC1 and unit 53's
  AC1. (b) changes a grammar a sibling owns for one column. RESOLVED (agent, 2026-10-25, delegated): (a),
  rung 3, the most criteria met with no grammar change, tie-broken by reuse of the suites' null-SHA
  spelling. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 52 to 57, id 35
  (HIGH, item H4; the same defect is id 2, item M2, in `TOOL-dWitnessedBar-62`).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-63's
  consumes-from edge, promoted by the round-1 spec audit of units 58 to 62; nothing else moved.

## 10. Reuse audit

The seam is `read_worktree_head`'s unborn rule (`tools/memory-recall/query.py:258-271`), the one place
this repository already reads HEAD without raising on an unborn branch, applied to unit 15's `--sha`
default; the null SHA is the suites' existing spelling. `python tools/codebase-map/reuse_lookup.py "seed
stamps a sha when HEAD is unborn"` ranked `seed` (test helpers), `stamp` (`.githooks/pre-push.test.sh`),
`seed_affordances` and `derive_short_sha`; none resolves an unborn HEAD, so no existing seam fits beyond
the reader named. `git grep -n -i unborn -- tools .githooks` found that reader and the runner suite's
assertion.

Recall terms used: `python tools/memory-recall/query.py "what does a tool stamp when HEAD is unborn in a fresh repository" --terms "unborn HEAD rev-parse verify quiet null sha seed legacy_ledger first commit git init scaffold"`
