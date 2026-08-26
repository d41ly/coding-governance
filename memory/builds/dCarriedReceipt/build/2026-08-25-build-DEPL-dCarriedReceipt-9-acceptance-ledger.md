# Acceptance ledger — DEPL-dCarriedReceipt-9, `carry` rungs over a derived needle map

**Serves:** journal DEPL-dCarriedReceipt-9

**Evidences:** DEPL-dCarriedReceipt-9
- AC1 — `tools/govkit/selftest.py` — RED observed on a real target with the pre-unit engine:
  `classify_row` returned a dict with NO `carry` key on all ten rows. GREEN: the ladder returns, per
  row, the rung the fixture was AUTHORED to prove, measured at 4 verbatim / 1 eol / 2 relocate / 3
  with no rung. **SUPERSEDED at rev-10:** S13's inCMS fixture is now built and AC1 is measured over
  the real 52-row population at 21 verbatim / 6 eol / 5 relocate / 20 no rung — the spec's figures,
  reproduced. The synthetic fixture and its arm both stay: they grade the ladder over a population
  authored to trigger every rung, which the real one does not guarantee.
- AC2 — amended rev-9, RESTATED rev-10 — the spec's `13` pairs now ARE asserted, over the 86-row
  population they were measured on, together with both dropped names. Its `26` needles is asserted
  as 25 and as a RELATION rather than a literal; see the S13 section. The arms assert the whole pair set,
  the ambiguous gov directory dropped BY NAME with both destinations, and the derived relationship
  `needles = 2*pairs - (slashless pairs)`, reporting 3 pairs / 5 needles and 2 pairs / 3 needles as
  measured.
- AC3 — `tools/govkit/selftest.py` — the fixture is asserted to trigger the hazard FIRST: the
  substituter really would rewrite `bash tools/land.sh` in gov's bytes, so a write-time transform
  would corrupt it. GREEN: the row proves no rung, keeps `patched`, and its bytes are byte-identical
  after `update --write`.
- AC4 — `tools/govkit/selftest.py` — the `~` form reaches a destination no `/`-form needle could
  produce. RED with only the `/` form emitted, and again with shortest-first ordering.
- AC5 — `tools/govkit/selftest.py` — asserted on CONTENT: the merged index blob is exactly gov's
  B-vintage bytes carrying the target's `scripts/` spelling. RED with the rung not applied to base
  and theirs: the merge conflicts.
- AC6 — `tools/govkit/selftest.py` — a non-UTF-8 blob returns byte-identical. The precondition
  asserts the SAME needle fires on the decodable form, so the arm grades the decode guard rather
  than an empty map.
- AC7 — `tools/govkit/selftest.py` — a hand-planted `"carry": "relocate"` on a row that provably
  matches no rung is DROPPED rather than believed. RED when the loop is made to trust it.
- AC8 — amended rev-9 — the spec's predicted red describes `9ddcc5c9` and is unreachable on `-8`'s
  tip, which is the same correction `-8`'s own ledger recorded. The REACHABLE red was observed: the
  three-way took an un-carried base, every line naming a path read as an operator edit, the merge
  CONFLICTED and the run exited 1. GREEN: rc 0, and the index blob spells `scripts/` and spells
  `tools/` nowhere.
- AC9 — `tools/govkit/selftest.py` — RED observed exactly as predicted: the deleted row restored as
  `gone refers to tools/demo/gone.txt`, gov's prefix into a target that does not use it. GREEN:
  restored carrying the target's spelling.
- AC10 — `tools/govkit/selftest.py` — RED observed: no `carry` key and `oid == gov_oid` over bytes
  gov never shipped. GREEN: the row reads `relocate`, the identities DIFFER, and the next update
  re-proves the rung from the blobs rather than reverting.

## The break sweep is the part worth trusting

Twenty-two staged breaks across twenty-two full selftest invocations, each patching one LINE and
never `git checkout --`, each restore verified by sha256 of both files. **All 71 new arms were
observed RED under at least one break — 71 of 71, none left over.**

It also caught TWO DEFECTIVE ARMS OF ITS OWN. One ran its `git diff HEAD` check after a `settle()`
that commits, so it was clean whether the run wrote the row or not — a check that could not fail.
The other's thunk RAISED, which took the harness down at that line and left 30 later arms
unreported rather than failing one. Both are fixed and commented at the site.

## S13 IS BUILT at rev-10, and AC2's `26` was derivably wrong — confirmed by measurement

Reopened on node `a` by owner ruling 2026-08-26, where inCMS and its pinned revision `2cff5855`
both resolve. `tools/govkit/fixtures/make_incms_receipt.py` reconstructs the receipt from inCMS's
own generated `.governance/install.index`, and `incms-2cff5855.receipt.json` (52 rows, 30 KiB) is
committed beside it.

**AC1 REPRODUCES EXACTLY: 21 verbatim, 6 eol, 5 relocate, 20 no rung, over all 52 rows.** The
spec's figures, measured for the first time against the population they were written about. The
offline derivation was cross-checked row-by-row against inCMS's real object store at build time:
zero disagreements on 52 of 52. The arms run with neither live repository present.

**AC2 did NOT reproduce, and was restated rather than fitted** — which is what AC2's own text
instructed. Two populations answer two questions: AC1 grades the 52 rows whose recorded COMMIT
resolves, because a rung is proved against gov's bytes at that commit; the needle map needs no
commit and its population is the 86 rows whose SOURCE resolves. Over the 86: **13 pairs, 25
needles**, dropping `tools/memory-recall` and `tools/workflows` by name — the spec's pair count
and both drop-names, and one needle short of its `26`. Over the 52 it is 14 pairs / 27 needles /
nothing dropped.

**The `26` was wrong by exactly one, for exactly the reason this build derived before it could
measure it.** `tools` is the single surviving gov directory carrying no slash, so its `/` and `~`
forms coincide and it contributes one needle rather than two: `2×13 − 1 = 25`. The arm asserts
that RELATION, not the literal. `-13`'s AC12 was warned to re-derive rather than inherit, and did.

**How the fixture proves `eol` without vendoring bytes.** `verbatim` and `relocate` compare the
target's recorded `oid` against a transformation of gov's bytes, so an oid IS the comparison. `eol`
normalises BOTH sides and an oid cannot be un-hashed, so each row carries `lf_oid` — one
measurement of the target taken where inCMS was reachable, which the arm reproduces from gov's
side. Same function, opposite inputs. That is what keeps the fixture at 30 KiB instead of a 540 KiB
pack of another project's source vendored into this repo, and it stores an independent measurement
rather than the answer.

### The original rev-9 note, kept because the deferral was real


S13 asks for a committed receipt of the 52 rows at inCMS `2cff5855`. That repository is not
reachable from this tree, so no run here can generate it. It is marked DEFERRED in place at rev-9.

Separately and worth more: building DERIVED that `26` is wrong even over the 86-row population it
was measured on. The `/` and `~` forms of a gov directory carrying no slash are the SAME string, so
such a pair contributes ONE needle, not two — and §4's own Inventory says `tools` survives as a
single pair. Thirteen pairs cannot yield twenty-six distinct needles. Nothing asserts either figure
now, so nothing is red, but `-13` S4a reads this same derivation and must re-derive rather than
inherit. Both are parked for the owner.

## One correction to §5

"No new subprocess" is wrong. `verbatim` is settled from the two oids and costs nothing, but `eol`
is a question about BYTES, so every row whose index blob is not gov's own now pays one
`git cat-file`. The docstring that previously claimed the opposite now records it.
