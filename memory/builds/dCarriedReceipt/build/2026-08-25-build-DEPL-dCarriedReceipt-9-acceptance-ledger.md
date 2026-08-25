# Acceptance ledger — DEPL-dCarriedReceipt-9, `carry` rungs over a derived needle map

**Serves:** journal DEPL-dCarriedReceipt-9

**Evidences:** DEPL-dCarriedReceipt-9
- AC1 — `tools/govkit/selftest.py` — RED observed on a real target with the pre-unit engine:
  `classify_row` returned a dict with NO `carry` key on all ten rows. GREEN: the ladder returns, per
  row, the rung the fixture was AUTHORED to prove, measured at 4 verbatim / 1 eol / 2 relocate / 3
  with no rung. NOT over inCMS — see the S13 note below; the spec's 21/6/5 are reproduced nowhere.
- AC2 — amended rev-9 — the spec's `13` pairs and `26` needles were NOT asserted anywhere, because
  the spec already disclaims them over its own stated population. The arms assert the whole pair set,
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

## S13 was not built, and AC2's `26` is derivably wrong

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
