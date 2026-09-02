# DEPL-dRetiredFork-7 — the undeclared-fork census, and the ledger contract

**Status:** OPEN · rev-3 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams deployer · order 2 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

Every number in this build rests on two adopter registers, and both undercount. Indexed against
gov's complete object history — 23,384 unique blobs from `git rev-list --objects --all` — ELEVEN
files inCMS declares `engine` are in no gov commit ever, including `scripts/gotchas.py`,
`scripts/check-arms.py` and `scripts/recall/extract.py`. NicoCares has two registers counting
different populations and nothing reconciles them: `.githooks/pre-commit` and `scripts/check-wiring.sh`
appear in NEITHER. And the migration's success state REDS NicoCares' bar, because its census arm
fails when it finds zero carve-outs. A retirement programme that cannot count its subjects and
cannot reach zero is not a programme.

## 2. Scope (IN)

- **S1** — The census, run once per adopter and recorded: every file each tree holds that maps to a
  gov path, blob-tested against gov's full object history, classified as byte-identical to HEAD,
  identical to some vintage (drift), or in no gov commit ever (undeclared fork).
- **S2** — The same census for `C:/projects/swydee`, which has no `.governance/` at all. Measured
  already and it inverts the priority: of 35 differing kit files, 32 are byte-identical to some gov
  vintage and only three diverge, one of which is a 70-line ancestor of gov's 1480-line runner.
- **S3** — The ledger contract. NicoCares' `nc carve-out N/M` tag encodes its own denominator, so
  retiring one requires editing every other tag; and its census arm at `scripts/check-wiring.sh`
  is an anti-vacuity guard that FAILS at zero — correctly written, and it has caught two real
  population-reach defects. The contract: stable ids with no denominator, the population in a
  tracked registry, and the guard asserting the registry is READABLE rather than non-empty.
- **S4** — The reverse-direction contradiction, recorded rather than resolved: gov declares
  `extract.py`, `query.py` and `recall-opened.js` as `role = "forked"`, `direction = "gov-from-target"`,
  report-only in both directions; inCMS declares two of the same files `engine`, meaning "gov's
  bytes, assert the OID". Two registers, opposite roles, one set of files.
- **S5** — File the defects this census exposes that are not this build's to fix, each with its
  measurement: the `--add-kits` flag `update` names at `govkit.py:5870` and the parser does not
  have, whose absence a selftest arm at `selftest.py:746` cannot detect because it grades the
  STRING. The `--kits` dispatch defect rev-1 also filed here is NOT filed: `DEPL-dRetiredFork-2`
  S5b fixes it, and filing a row at order 2 that another unit closes at order 6 ships a backlog row
  that is already false.
- **S6** — RECORD inCMS's `gen_build_index.py` row as contract-adopted in the census output, and
  hand the reclassification to that adopter as a named recommendation. rev-1 said "Reclassify",
  which §3 forbids and AC7 asserts against — the row lives in inCMS's own `kits.json` and gov
  owns none of it. Recording it carves the item cleanly out of §3's non-goal.
  gov's file is 2519 lines with 59 top-level defs, inCMS's is 518 with 14, and they share three
  symbol names. There is no upstream file to converge on, and its 2764-line diff inflates every
  metric computed over that registry.

## 3. Non-goals (OUT)

- Fixing the eleven undeclared inCMS files or the two NicoCares ones. This unit MEASURES and
  DECLARES; whether each converges, is absorbed or is accepted as project-owned is a per-file
  decision needing the adopter's own record.
- Onboarding swydee. Its census lands here; giving it a receipt is a follow-up build.
- Editing either adopter's tree. gov owns none of it; the deliverable is the measurement and the
  contract, handed over.

## 4. Design

### Inventory

| register | population it counts | what it misses |
|---|---|---|
| nc `carve-out N/20` tags | files nc deliberately edited | a gov engine edited without a tag |
| nc `install.json` | rows whose on-disk oid differs from `gov_oid` | files in no receipt row at all |
| inCMS `kits.json` `divergence` | 24 declared repaths and forks | 11 `engine` rows gov never shipped |

### Rollout

This unit runs FIRST among the sweeps — order 2, before any literal or absorption sweep touches an
adopter — because a sweep that retires a fork nobody counted cannot be verified, and because S3's
ledger fix is what makes any retirement possible at NicoCares at all.

### Alternatives rejected

Trusting the registers. They are the only inventories that exist and they are both wrong in the same
direction, which is the direction that makes the build look smaller than it is.

## 5. Production-readiness checklist

- security — reading two repositories gov does not own, read-only, no writes.
- perf / scale — a full-history blob index over 23,384 objects, once per adopter; cacheable by sha
  because a commit's tree is immutable.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a census that maps zero files REFUSES; that is the vacuity class
  the NicoCares guard already exists to catch, one level up.
- observability — the census output is the record; it names every file in each of the three classes
  rather than reporting counts.
- risks — the census is the input to every other unit's sizing. If it is wrong, the build is
  mis-scoped. Mitigated by testing against gov's full object history rather than HEAD, which is what
  distinguishes drift from divergence.
- testing + left-shift gates — the census script is gov-internal and gets its own arms; it is not a
  bar leg, because gov has no adopter registry and nothing on the bar reaches outside the repository.
- migration / rollback — a measurement; nothing to roll back.
- user docs — the census output lands in this build's folder; the ledger contract lands in
  `WIRE-INTO-PROJECT.md`.

## 6. Acceptance criteria

- **AC1** — When the census runs against `C:/projects/incms/main`, it names all eleven `engine`-declared
  files that appear in no gov commit, and its total maps every tracked kit-derived file to exactly
  one of the three classes.
- **AC2** — When it runs against `C:/projects/nicocares/main`, it names `.githooks/pre-commit` and
  `scripts/check-wiring.sh` as present in neither register.
- **AC3** — When it runs against `C:/projects/swydee`, it reports 32 of 35 differing files as
  identical to some gov vintage and names the three that diverge.
- **AC4** — When the census maps zero files, it REFUSES rather than reporting a clean tree. The index is built from `git rev-list --objects --all`, so an empty map is detectable.
- **AC4b** — The census output NAMES the `gen_build_index.py` row, its recorded class and the
  two symbol counts that justify it — 2519 lines with 59 defs against 518 with 14, sharing three
  names — and the recommendation handed to inCMS is quoted in this build's record. This is S6,
  which rev-1 left unobserved by every criterion.
- **AC5** — The ledger contract is written, and a worked example shows a NicoCares carve-out being
  retired without editing any other tag and without the census arm failing at zero. The contract and the worked example land in `WIRE-INTO-PROJECT.md`.
- **AC6** — Each defect in S5 has a row in `memory/backlog/DEPL.md` carrying its file, line and
  measurement.
- **AC7** — The reverse-direction contradiction in S4 is recorded in `memory/DECISIONS.md` with both
  registers quoted, and neither register is edited by this unit.

## 7. Gates

`memory hygiene` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`.

## 8. Open questions

- **F1 — who owns the census script?** It reads two foreign trees, so it cannot be a kit and cannot
  be a bar leg. Recommendation: gov-internal under `tools/govkit/`, registry-exempt with a stated
  reason, alongside `fixtures/make_incms_receipt.py`, which is the existing precedent for
  adopter-shaped gov-internal tooling.
- **F2 — does an undeclared fork become a declared one, or a defect?** Eleven files is not a
  bookkeeping slip. Recommendation: each gets a row and a disposition, and the ones that turn out to
  be adopter-authored programs are reclassified as project-owned rather than pretended into
  convergence — which is exactly what S6 does for `gen_build_index.py`.
- **F3 — is swydee in this build's scope after all?** Its census says it is the CHEAPEST consumer to
  converge, not the hardest, which is the opposite of what every design assumed. Recommendation:
  keep it parked, and put this measurement in front of the owner, because the ordering argument may
  now favour doing it first.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. The 23,384-blob index, the eleven inCMS files, the two
  NicoCares files and the swydee 32-of-35 split are measurements from this build's classification
  pass, not estimates.
- rev-2 · 2026-09-02 · folded spec-audit round 1, finding H8. rev-1 filed the `--kits` dispatch defect that
  `DEPL-dRetiredFork-2` F2 recommended fixing; M2 requires one owner, and DEPL-2 takes it.
- rev-3 · 2026-09-02 · folded spec-audit round 2, finding 9. S6 was imperative, §3 forbade it and no criterion
  observed it, so the unit could pass its DoD with the row untouched while the README believed
  it reclassified. S6 RECORDS and recommends now, which §3 permits, and AC4b observes it.

## 10. Reuse audit

No existing seam fits. `reuse_lookup.py` reports `tools/govkit/fixtures/make_incms_receipt.py` as the
only gov-internal tool that reads an adopter tree, and it constructs a fixture rather than measuring
one; nothing in the corpus indexes gov's full object history. The census is new, gov-internal, and
deliberately not a kit.

Recall terms used: `census`, `undeclared fork`, `divergence`, `kits.json`, `install.json`,
`carve-out`, `denominator`, `anti-vacuity`, `blob`, `vintage`, `swydee`, `forked`, `gov-from-target`.
