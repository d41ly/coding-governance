# TOOL-dWitnessedBar-46 — what an adopter receives of the ratchet pack: the scalar-pin leg over its own seeded pins, and the rest kept gov's

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 10 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 34 at HIGH**, its item **H7**, alone in that item. `TOOL-dWitnessedBar-14` S2
declares the nine ratchet legs as `[[gate_leg]]` rows of the shipped memory-tree descriptor. Its
`ratchet (keys, not a scalar)` leg reds every `*_PIN=` assignment no population holds, and that
population's home is gov's `memory/project/conf-scalar-pins.txt`; the example conf an adopter's conf is
made from assigns `ROW_DUPLICATE_PIN="0"` (`tools/memory-tree/.memory-tree.conf.example:283`). The other
legs read gov's registered populations and the base remote. An adopter whose conf came from the example
reds on its first update, and the spec never says what an adopter receives. This unit takes the report's
fix. It repairs `TOOL-dWitnessedBar-14`.

## 2. Scope (IN)

- **S1** — The adopter-receives table. §4 "What an adopter receives" states, per leg of unit 14's pack,
  whether it ships, by one rule: a leg ships when every input it reads at an adopter either ships with
  the kit or is seeded at the adopter by `test.seed`. Observed by AC1.
- **S2** — The scalar-pin leg ships over the adopter's own pins. `conf-scalar-pins`' registration gets
  the seed `["python3", "{kit}/ratchet.py", "keys-not-scalar", "--measure"]`, printing one row per
  `*_PIN=` assignment of a scalar count in the tree's tracked root confs, keyed by conf and key. The
  memory-tree adopter runs `legacy_ledger.py seed --population conf-scalar-pins` after it scaffolds the
  memory tree, absent-only, so a conf made from the example seeds its `ROW_DUPLICATE_PIN` row and the leg
  is green. Observed by AC2.
- **S3** — An unarmed population is never green. `keys-not-scalar` over an absent or unarmed
  `conf-scalar-pins` exits 1 printing `unarmed conf-scalar-pins` and the seed command, so a failed seed
  is visible rather than silent. Observed by AC3.
- **S4** — The home is admitted. `conf-scalar-pins.txt` joins check 3's named list of kit-shipped
  registries in `tools/memory-tree/check-memory-hygiene.sh`, as `substitution-fed-loops.txt` does, so the
  seeded home passes at an adopter. Observed by AC2.
- **S5** — The other live legs stay gov's. `ratchet (never gains)`, `ratchet (both ways)`,
  `ratchet (unarmed)`, `ratchet (populated)`, `ratchet (seed laundering)`, `ratchet (rename)` and
  `ratchet (key shape)` move from `[[gate_leg]]` rows of `tools/memory-tree/kit.toml` to `[[exempt_leg]]`
  rows of `tools/govkit/registry.toml`, each carrying its whole row and a `why` naming the gov-only input
  it reads. `ratchet selftest` ships, since its fixtures build their own repositories. gov's manifest is
  unchanged as a set. Observed by AC1.

## 3. Non-goals (OUT)

- The pack's verbs, the widen route and the population itself: `TOOL-dWitnessedBar-14`'s.
- `test.seed` and its home rule: `TOOL-dWitnessedBar-15`'s and `TOOL-dWitnessedBar-47`'s.
- Shipping the seven gov-only legs to adopters: a later build, once each has an adopter seed and a base
  every adopter holds. The exit code of a live leg with no base is the minors batch's id 58 item
  (`TOOL-dWitnessedBar-51`).
- A template check that a spec adding a shipped `[[gate_leg]]` carries an adopter-receives line, the
  report's left-shift: no clause of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-14` — the `ratchet` pack's legs, `ratchet.py keys-not-scalar` and the `conf-scalar-pins` registration, whose shipping this unit decides
- **consumes-from** `TOOL-dWitnessedBar-15` — `legacy_ledger.py seed`, which the memory-tree adopter runs for `conf-scalar-pins`
- **consumes-from** `TOOL-dWitnessedBar-47` — the directory admission rule, without which the adopter's seed into its uncommitted `memory/project/` is refused
- **hands-off** `TOOL-dWitnessedBar-52` — `keys-not-scalar --measure` and the adopter's seed of `conf-scalar-pins`, whose conf read unit 52 widens to the working tree (id 1)
- **hands-off** `TOOL-dWitnessedBar-53` — the adopter's seed of `conf-scalar-pins`, which unit 53's arm runs across the scaffold's first commit (id 13)
- **hands-off** `TOOL-dWitnessedBar-56` — its hygiene-suite arm and the adopter-receives table, whose floor and README sentence the verdict-boundary minors batch lands (ids 37, 41)
- **hands-off** `TOOL-dWitnessedBar-57` — `keys-not-scalar` over the seeded population, which the resolver and ledger minors batch makes name an empty seed (id 44)
- **hands-off** `TOOL-dWitnessedBar-62` — the hygiene suite's scaffold arm and the adopter-receives table, which the minors batch extends with unit 53's arm and restates over the working-tree conf set (ids 5, 11, 25)

## 4. Design

### Evidence

- The example conf: `ROW_DUPLICATE_PIN="0"` (`tools/memory-tree/.memory-tree.conf.example:283`); the
  other `*_PIN=` lines there are blank (`:191`, `:194`, `:293`, `:294`), which assign no count.
- `adopt-memory-tree.sh` copies the example when no conf exists (`:97-98`) and creates `$M/project`
  (`:515`).
- Check 3 admits a kit-shipped registry only by name, and calls the `PROJECT_REGISTRY_EXTRA` route for
  one "the defect" (`tools/memory-tree/check-memory-hygiene.sh:733-738`).
- `check-memory-hygiene.test.sh` scaffolds a tree with `adopt-memory-tree.sh --scaffold` (`:2425`).

### What an adopter receives

| Leg | Reads at an adopter | Ships |
|---|---|---|
| `ratchet (keys, not a scalar)` | the adopter's root confs and its seeded `conf-scalar-pins` | yes |
| `ratchet selftest` | its own scratch repositories | yes, held as a kit self-test |
| `ratchet (never gains)` | every registered population and the base remote; `retrofit.widen` through `tools/policy/policy.py` | no, `[[exempt_leg]]` |
| `ratchet (both ways)` | every registration's seed run at HEAD | no |
| `ratchet (unarmed)` | every registered home | no |
| `ratchet (populated)` | every population and the seen-red records | no |
| `ratchet (seed laundering)` | every population at the base | no |
| `ratchet (rename)` | the base range | no |
| `ratchet (key shape)` | every population | no |

### Inventory

Minted: the verb flag `keys-not-scalar --measure`; the check-3 name `conf-scalar-pins.txt`; seven
`[[exempt_leg]]` rows. Naming cells: the flag is asked of `python tools/lexicon/lexicon.py --suggest
measure --as cli.flag` at the pass.

### Migration

gov's manifest rows are unchanged as a set: the seven legs render from `[[exempt_leg]]` rows with the
same keys. An adopter's next update receives two ratchet legs and seeds its pins.

### Rollout

Live at landing. The pass runs `python tools/run-gates/owed_rows.py --base HEAD` before its commit
(PLAY-dOrderedCharter-50 S6).

### Files touched (estimate)

- `tools/memory-tree/ratchet.py`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/adopt-memory-tree.sh`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/govkit/registry.toml`
- `tools/gate-legs.json`

### Alternatives rejected

- **Ship all nine legs with adopter rules per leg.** Seven read gov's registered populations, the base
  remote or a policy reader no adopter install carries at this build, so each would need a seed and a
  base this unit cannot derive; shipping them unproven is the defect this unit closes.
- **Exempt all nine.** The example conf an adopter starts from carries a scalar pin, and the one leg
  that sees it would never run where it matters.

## 5. Production-readiness checklist

- security — no new surface; the seed reads tracked confs and writes one registered home.
- perf / scale — one grep over the root confs per seed and per run.
- error / empty / loading states — an absent or unarmed population exits 1 naming the seed command.
- observability — the leg prints the population's rows and each unheld pin by conf and key.
- risks — a failed adopter seed reds the leg until re-run; S3 makes that red say what to run.
- testing — AC1 to AC3 by probe and fixture; the arm of §7 at the close.
- migration — §4.
- user docs — `tools/memory-tree/README.md`'s pack section gains the adopter-receives table at the pass;
  no page under `help/` documents the ledger.

## 6. Acceptance criteria

- **AC1** — When `python -c "import json,sys; print(sorted(l['name'] for l in json.load(open(sys.argv[1], encoding='utf-8')) if l.get('pack') == 'ratchet'))" tools/gate-legs.json`
  runs, it prints the nine legs as before, and `grep -c '^\[\[gate_leg\]\]' tools/memory-tree/kit.toml`
  falls by seven against the pass's parent while `tools/govkit/registry.toml` gains seven
  `[[exempt_leg]]` rows naming them.
  Red when: a leg reading a gov-only input stays a shipped `[[gate_leg]]`.
- **AC2** — When `adopt-memory-tree.sh --scaffold` builds a scratch tree from the example conf,
  `python ratchet.py keys-not-scalar` there exits 0
  naming one row, `.memory-tree.conf` and `ROW_DUPLICATE_PIN`, and check 3 passes with
  `conf-scalar-pins.txt` present.
  Red when: the adopter's pin is not seeded, or check 3 refuses its home.
  fixture: a scratch `git init` target under `%TEMP%/<short-name>`; the tree holds none.
- **AC3** — When `keys-not-scalar` runs in that scratch tree with `conf-scalar-pins.txt` removed, it
  exits 1 printing `unarmed conf-scalar-pins` and `legacy_ledger.py seed --population conf-scalar-pins`.
  Red when: an absent population reads green.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `govkit selftest` · `govkit acceptance matrix` · `run-gates canary` · `measure-legs selftest` · `recall floor arms` · `govkit refusal join` · `run-gates gov canary`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC3 · the scaffold arm runs `keys-not-scalar` over the example-made tree and then with its home removed, staged red by dropping the adopter's seed call · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-14`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Which ratchet legs does an adopter receive?** Options: (a) all nine, with an adopter rule per
  leg; (b) the scalar-pin leg over the adopter's own seeded pins and the self-test, the seven legs over
  gov's populations kept gov's; (c) none. (a) needs a seed and a base per leg that no adopter install
  carries at this build, which veto 1 discards against unit 14's own criteria at an adopter; (c) leaves
  the example conf's pin unseen where it ships. RESOLVED (agent, 2026-10-25, delegated): (b), rung 3,
  the most criteria met that can be observed at an adopter today. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 34 (HIGH, item H7).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-52, TOOL-dWitnessedBar-53, TOOL-dWitnessedBar-56,
  TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-62's
  consumes-from edge, promoted by the round-1 spec audit of units 52 to 57; nothing else moved.

## 10. Reuse audit

The seams are unit 15's `seed` verb, check 3's named list of kit-shipped registries
(`tools/memory-tree/check-memory-hygiene.sh:716-743`) and the `[[exempt_leg]]` row unit 11 gives a whole
leg row. `python tools/codebase-map/reuse_lookup.py "seed an adopter's scalar pin population at update"`
ranked `seed` (test helpers), `adopt`, `population` (`tools/govkit/refusal_join.py`),
`require_adopted_root`, `declared_scalar` and `seed_affordances`; none seeds a ledger at an adopter, so
the adopter calls the one verb that does.

Recall terms used: `python tools/memory-recall/query.py "what does an adopter receive of a ratchet leg pack" --terms "ratchet keys-not-scalar conf-scalar-pins ROW_DUPLICATE_PIN adopter test.seed check 3 project registry exempt_leg"`
