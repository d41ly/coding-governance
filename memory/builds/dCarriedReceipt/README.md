---
slug: dCarriedReceipt
node: d
opened: 2026-08-24
streams: deployer
roster: DEPL
ids: DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 DEPL-dCarriedReceipt-16 TOOL-dCarriedReceipt-1 TOOL-dCarriedReceipt-2 TOOL-dCarriedReceipt-3 TOOL-dCarriedReceipt-4
---

# dCarriedReceipt — a receipt that carries provenance, and an update that can be trusted with it

Node `d` · opened 2026-08-24 · streams deployer · base `9ddcc5c9`.

Closes the standing asks **DEPL-aFerriedDossier-1** (bootstrap a receipt, grow one),
**DEPL-aFerriedDossier-2** (widen the S5 fixture family with a non-default-prefix entry and an
adopt-existing variant) and **DEPL-aFerriedDossier-3** (the 13 defects inCMS measured here with line
numbers). Those three were filed 2026-08-16 as an inbound dossier and no unit ever owned them.

## Why now, and what changed since the dossier

An adopter-side audit on 2026-08-24 measured both live targets against gov `9ddcc5c9` by blob OID and
found **zero rows auto-syncable in either repo** — `cmd_update` refuses without
`.governance/install.json`, and neither target has one. It also found two defects in the shipped
update engine that the dossier could not have seen, because they only appear on the *second* run:

- **A merge result is stamped into the receipt as if gov wrote it.** The stamp is `govkit.py:3098`,
  sitting between the merge write at `:3097` and the commit advance at `:3099`. So on the next commit
  that touches the file, `classify_row`'s ours-vs-receipt comparison at `:2889` reads
  `("equal","differs")`, the grid at `:2845` calls that `stale`, and `:3071` raw-overwrites the file.
  Every hand-edit the three-way preserves is destroyed one update later and reported as a clean write
  with zero conflicts. This is **DEPL-dCarriedReceipt-8**.
- **The refuse-during-merge guard cannot fire in a linked worktree.** `:2334` stats
  `target/.git/MERGE_HEAD` as a path; in a linked worktree `.git` is an 80-byte file. `cmd_update`
  has no such guard at all. This is **DEPL-dCarriedReceipt-12**.

Both were verified in source. They are why the safety chain lands before either onboarding unit.

## The architecture in one paragraph

A receipt row stops carrying one overloaded hash of worktree bytes and carries **two identities** —
`gov_oid` (the blob gov shipped at the row's `commit`) and `oid` (the blob the target holds, read
from its index) — with the difference between them explained by a per-row `carry` rung (`verbatim` /
`eol` / `relocate`) that is **recomputed by proof on every run and never trusted from the receipt**.
Identities agree → the file is gov's and takes an automatic raw write. Identities differ by a PROVEN
rung → automatic RECONCILIATION to the *carried* bytes, through the three-way rather than by a raw
write: the rung is applied to `base` and to `theirs`, so it cancels in the base→theirs diff and
`git merge-file` sees only gov's semantic change. That is what reaches an adopter at a non-default
prefix, with no operator turn and no write-time transform. Identities differ by anything else →
there is a local delta, the raw-write arm is closed to that row permanently, and only the three-way
applies. Role `forked` is a claim the DESCRIPTOR RULE makes about a file's provenance, re-read from
that rule on every run and never inferred from what the attribution walk found; a forked row is
report-only and written in neither direction. A destination that attributes to no gov vintage is a
SEPARATE state, `evidence: "unattributed"` — no `commit`, no `gov_oid`, its role still whatever its
rule declared — printed, counted and skipped once its role resolves to the one disposition that
writes, before the verdict table, because that disposition needs a base and such a row has none.
`oid != gov_oid` **is** the local-delta predicate, so no stored flag can go stale behind it. One
row class sits outside that model by construction. Where gov owns a BLOCK inside a file the target
owns — role `merged` — there is no whole-file gov blob to hash, so the row carries neither
identity, the delta predicate has no operands, and its drift is the block hash's business. It is
exempt from the integrity preamble by ROLE, which is the one place that preamble is not scoped by
field presence (`-7` §8 F4). A new read-only verb `govkit adopt` writes that receipt for an
already-installed tree by measuring it against gov history. Partial *adoption* is measured
separately and earlier by `plan --coverage`, which needs only `deploy.toml`.

## Units

| id | was | delivers | tier | deps |
|---|---|---|---|---|
| DEPL-dCarriedReceipt-1 | U1 | `{relpath}` resolves through `rule_relpath` in `resolve_dests` | 2 | — |
| DEPL-dCarriedReceipt-2 | U2 | `refuse` → `report`; `attributes` gets a `pins` arm | 1 | — |
| DEPL-dCarriedReceipt-3 | U3 | `intake` honours `--answer prefix=` | 1 | — |
| DEPL-dCarriedReceipt-4 | U4 | `coverage_rows()` + `plan --coverage` | 1 | 1 |
| DEPL-dCarriedReceipt-5 | U5 | `[[decline]]` contract + three staleness arms | 1 | 4 |
| DEPL-dCarriedReceipt-6 | U6 | the silenced-gate-leg bar, and the gov defect it finds | 2 | 1 |
| DEPL-dCarriedReceipt-7 | U7 | two identities, read index-side | 2 | 2 |
| DEPL-dCarriedReceipt-8 | U8 | a merge result never overwrites `gov_oid` | 2 | 7 |
| DEPL-dCarriedReceipt-9 | U9 | `carry` rungs, recomputed, over a derived needle map | 2 | 7, 8 |
| DEPL-dCarriedReceipt-10 | U10 | role `forked`, report-only | 2 | 2 |
| DEPL-dCarriedReceipt-11 | U11 | rename detection; `withdrawn` stops deleting silently | 2 | 7 |
| DEPL-dCarriedReceipt-12 | U12 | write preconditions + lock | 2 | — |
| DEPL-dCarriedReceipt-13 | U13 | `govkit adopt` — the receipt bootstrap | 2 | 1, 2, 7, 9, 10, 12 |
| DEPL-dCarriedReceipt-14 | U14 | post-write verification with index rollback | 2 | 7, 11 |
| DEPL-dCarriedReceipt-15 | U17 | gov stops shipping literal prefixes in kit bodies | 2 | — |

The adopter-side units land in `d41ly/incms` under slug `dPinnedVintage` (was U15, U16, U18) and are
not this build's to carry.

## Landing order

Dependency-ordered. A unit leaves both trees green once the units in its `deps` column are beneath
it — "landable alone" is NOT a property this build has, and two units withdrew the claim after their
round-1 folds. `-7` now lands behind `-2` (its AC5 cannot read `"schema": 3` until `-2` teaches
`update` to move an `attributes` row), and `-14` ratified a hard order behind `-11` as well as `-7`
in its §8 F3. `-8`, `-9` and `-11` each state their own dependency in §3. Each unit's §3 land-alone
line is the authority; the `deps` column above mirrors it.

1. **`-2`, `-3`** — Tier-1, no deps, ~12 lines together. `-2` is a precondition for every later run
   re-stamping its receipt at all.
2. **`-1`, `-12`** — the resolver fix and the write preconditions. `-12` lands before anything gains
   a `--write` path it does not already have.
3. **`-7` → `-8`** — two identities, then the integrity fix that rests on them. `-8` is the unit the
   owner's "sync only where nothing was hand-edited" requirement actually reduces to.
4. **`-9`, `-10`, `-11`, `-14`** — the remaining safety and reach units, and the one step whose
   internal order is not free: `-14` lands after `-11`, whose `renamed` disposition its snapshot and
   its touched-kit predicate both read. `-9` and `-11` intersect on a renamed row carrying a rung
   (`-11` S11), but that item is inert until both are landed and neither blocks the other.
5. **`-13`** — `adopt`, which needs `-1`, `-7`, `-9`, `-10`, `-12` and `-2` beneath it; `-12`'s
   S7 vintage guard is what its AC11 observes, and step 2 already puts `-12` below this one.
   `-2`'s `pins` disposition is what AC13 and AC14 observe, and step 1 already puts it below this
   one.
6. **`-4`, `-5`, `-6`** — coverage. `-4` is independently useful once step 2 is beneath it — it
   needs `-1`, whose reading AC3 asserts — and may be pulled forward to step 3; it is the only unit
   that runs against a real adopter today.
7. **`-15`** — the durable prefix fix. Deferrable without blocking anything.

## Owner decisions on the record

- **2026-08-24 — full scope approved.** All eighteen units, gov and adopter side. The owner was
  shown the per-unit cut consequences and cut nothing.
- **Not in scope, carried from the aFerriedDossier §4 cut-line and re-affirmed by this design:** a
  reverse transform or any upstream/contribute verb; a free-form rewrite rule; line-level partial
  application; automatic rename detection for *coverage*; tokenizing gov's engine files; auto-resolving
  a base for rows matching no gov vintage; deleting the adopter's own commit-time brake.
- **Strict mode over merge, from the dossier's §4:** inCMS's policy is that vendored kits carry zero
  local edits, so a `diverged` row is a policy violation rather than a merge. `-8` makes that
  expressible; the strict flag itself is keyed on the target descriptor, not an operator flag.

## Evidence

The audit that grounds every number here, with its method and its own instrument defect stated:
`memory/builds/dCarriedReceipt/build/` (to be carried in from the adopter side, matching how
`aFerriedDossier` carried its dossier).

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `DEPL-dCarriedReceipt-1` | 2 | `{relpath}` resolves through `rule_relpath` in the seam that writes |
| 2 | `DEPL-dCarriedReceipt-10` | 2 | role `forked`, report-only |
| 3 | `DEPL-dCarriedReceipt-11` | 2 | rename detection, and `withdrawn` stops deleting silently |
| 4 | `DEPL-dCarriedReceipt-12` | 2 | write preconditions and a lock, on both writing verbs |
| 5 | `DEPL-dCarriedReceipt-13` | 2 | `govkit adopt`, the receipt bootstrap |
| 6 | `DEPL-dCarriedReceipt-14` | 2 | post-write verification, with index rollback |
| 7 | `DEPL-dCarriedReceipt-15` | 2 | gov stops shipping its own prefix inside kit bodies |
| 8 | `DEPL-dCarriedReceipt-2` | 1 | `refuse` becomes `report`, and `attributes` gets a pins arm |
| 9 | `DEPL-dCarriedReceipt-3` | 1 | `intake` honours `--answer prefix=` |
| 10 | `DEPL-dCarriedReceipt-4` | 1 | `coverage_rows()` and `plan --coverage` |
| 11 | `DEPL-dCarriedReceipt-5` | 1 | the `[[decline]]` contract, and three arms that keep it honest |
| 12 | `DEPL-dCarriedReceipt-6` | 2 | the silenced-gate-leg bar, and the gov defect it finds |
| 13 | `DEPL-dCarriedReceipt-7` | 2 | two identities, read index-side |
| 14 | `DEPL-dCarriedReceipt-8` | 2 | a merge result never overwrites `gov_oid` |
| 15 | `DEPL-dCarriedReceipt-9` | 2 | `carry` rungs, recomputed, over a derived needle map |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 15 unit(s) · node d · opened 2026-08-24 · streams deployer
ids DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12
ids DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 DEPL-dCarriedReceipt-16 TOOL-dCarriedReceipt-1 TOOL-dCarriedReceipt-2 TOOL-dCarriedReceipt-3 TOOL-dCarriedReceipt-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-dCarriedReceipt-1 — `{relpath}` resolves through `rule_relpath` in the seam that writes](spec/2026-08-24-spec-DEPL-dCarriedReceipt-1.md) | — | 2 | CLOSED | rev-1 | 2026-08-24 |
| [DEPL-dCarriedReceipt-10 — role `forked`, report-only](spec/2026-08-24-spec-DEPL-dCarriedReceipt-10.md) | — | 2 | CLOSED | rev-7 | 2026-08-25 |
| [DEPL-dCarriedReceipt-11 — rename detection, and `withdrawn` stops deleting silently](spec/2026-08-24-spec-DEPL-dCarriedReceipt-11.md) | — | 2 | CLOSED | rev-7 | 2026-08-25 |
| [DEPL-dCarriedReceipt-12 — write preconditions and a lock, on both writing verbs](spec/2026-08-24-spec-DEPL-dCarriedReceipt-12.md) | — | 2 | CLOSED | rev-7 | 2026-08-26 |
| [DEPL-dCarriedReceipt-13 — `govkit adopt`, the receipt bootstrap](spec/2026-08-24-spec-DEPL-dCarriedReceipt-13.md) | — | 2 | CLOSED | rev-8 | 2026-08-26 |
| [DEPL-dCarriedReceipt-14 — post-write verification, with index rollback](spec/2026-08-24-spec-DEPL-dCarriedReceipt-14.md) | — | 2 | CLOSED | rev-7 | 2026-08-25 |
| [DEPL-dCarriedReceipt-15 — gov stops shipping its own prefix inside kit bodies](spec/2026-08-24-spec-DEPL-dCarriedReceipt-15.md) | — | 2 | CLOSED | rev-5 | 2026-08-26 |
| [DEPL-dCarriedReceipt-2 — `refuse` becomes `report`, and `attributes` gets a pins arm](spec/2026-08-24-spec-DEPL-dCarriedReceipt-2.md) | — | 1 | CLOSED | rev-3 | 2026-08-25 |
| [DEPL-dCarriedReceipt-3 — `intake` honours `--answer prefix=`](spec/2026-08-24-spec-DEPL-dCarriedReceipt-3.md) | — | 1 | CLOSED | rev-2 | 2026-08-25 |
| [DEPL-dCarriedReceipt-4 — `coverage_rows()` and `plan --coverage`](spec/2026-08-24-spec-DEPL-dCarriedReceipt-4.md) | — | 1 | CLOSED | rev-6 | 2026-08-26 |
| [DEPL-dCarriedReceipt-5 — the `[[decline]]` contract, and three arms that keep it honest](spec/2026-08-24-spec-DEPL-dCarriedReceipt-5.md) | — | 1 | CLOSED | rev-6 | 2026-08-26 |
| [DEPL-dCarriedReceipt-6 — the silenced-gate-leg bar, and the gov defect it finds](spec/2026-08-24-spec-DEPL-dCarriedReceipt-6.md) | — | 2 | CLOSED | rev-6 | 2026-08-26 |
| [DEPL-dCarriedReceipt-7 — two identities, read index-side](spec/2026-08-24-spec-DEPL-dCarriedReceipt-7.md) | — | 2 | CLOSED | rev-8 | 2026-08-26 |
| [DEPL-dCarriedReceipt-8 — a merge result never overwrites `gov_oid`](spec/2026-08-24-spec-DEPL-dCarriedReceipt-8.md) | — | 2 | CLOSED | rev-5 | 2026-08-25 |
| [DEPL-dCarriedReceipt-9 — `carry` rungs, recomputed, over a derived needle map](spec/2026-08-24-spec-DEPL-dCarriedReceipt-9.md) | — | 2 | CLOSED | rev-10 | 2026-08-26 |
<!-- /gen:build-units -->

Records: 27 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->