# Acceptance ledger — DEPL-dCarriedReceipt-10, role `forked`, report-only

**Serves:** journal DEPL-dCarriedReceipt-10

**Evidences:** DEPL-dCarriedReceipt-10
- AC1 — `python tools/govkit/govkit.py update` — RED observed on the REAL trees, not a reduction. A
  copy of inCMS's own `scripts/recall/` was asserted to import cleanly first, then gov's
  `tools/memory-recall/extract.py` was copied over it, which is exactly what an `engine` update
  performs. Result: `ModuleNotFoundError: No module named 'recall_conf'`, and `import query` dies at
  the same line. inCMS's `install.index` declares that path role `engine` today. GREEN: the role now
  exists, so a descriptor can say `forked` instead.
- AC2 — `tools/govkit/selftest.py` — `update --write` prints exactly one `report` line naming
  `direction gov-from-target`, leaves the target's bytes byte-identical, leaves GOV's copy untouched,
  and re-stamps `gov_commit`. LIVENESS in the same run: the engine row DID move, so nothing passed by
  doing nothing.
- AC3 — `python tools/govkit/govkit.py selfcheck` — the S6 arm. GREEN over the shipped registry.
  RED observed by undeclaring `extract.py` from S7's rule: selfcheck exits 1 naming the path, the
  claiming entry and the role it was claimed with.
- AC4 — `tools/govkit/selftest.py` — RED observed FIRST at the pre-unit state: a descriptor saying
  `forked` failed with `role 'forked' is not in ROLE_KINDS`, the WRONG reason. GREEN: three separate
  refusals — absent `direction`, absent `record`, and a `direction` outside the closed set — each
  with its own arm and each seen RED.
- AC5 — `tools/govkit/selftest.py` — RED observed by reverting `cmd_plan`'s summary to hand-naming
  five kinds: the row was still MARKED `FORK` while the summary omitted the count entirely, which is
  the defect S2 names. GREEN: the summary is DERIVED from `KIND_MARKS` and reads `... 0 blocked,
  3 forked`, measured on gov's own tree.
- AC6 — `python tools/govkit/govkit.py selfcheck` — exit 0 with `forked` in both `UNLANDED_REASON`
  and `UPDATE_ROLE`. RED under dropping the `UNLANDED_REASON` line.
- AC7 — `tools/govkit/selftest.py` — RED observed by using `row["direction"]` instead of `.get`: the
  run raises `KeyError` and prints a traceback, turning the one disposition that exists to avoid
  acting into a crash. GREEN: a row with no direction prints with no direction clause and none
  invented.

## S6 and S7 landed here, not in the unit's own build

The builder's permitted file set was `tools/govkit/` only — a restriction of mine, not the spec's —
so it could reach neither `tools/memory-recall/kit.toml` (S7) nor the doc. It refused to write S6 as
dormant machinery, on the correct grounds that an arm wired over a population that cannot contain a
hit is the green-by-absence shape this repo forbids. Both landed in this same commit, which is what
S7 requires in as many words.

## S6's first draft could not fail

Keyed on `rule_sources`, exactly as the spec's Inventory describes the population. That arm graded
only rules with LITERAL includes — and the rule that swallows an undeclared fork is precisely the
`**` one, whose `rule_sources` is empty. Observed: undeclaring `extract.py` left selfcheck GREEN.
Re-aimed at `resolve_rule_pool`, the expanded pool, and re-observed RED. This is the third arm in
this build to fail this way, and the third caught by insisting on the failing case.

The Inventory's own reasoning is unchanged and still correct: keyed repo-wide the predicate matches
FOUR files, and the fourth is gov's own `.claude/hooks/recall-opened.js`, which no descriptor claims.
Only the enumerator moved, not the population.

## §5's user-docs item names a table that does not exist

It asks for the role to join a role table in `WIRE-INTO-PROJECT.md`. That file has no role table.
The sentence landed in `skills/deploy-governance/SKILL.md` beside the other plan marks, which is
where marks are already documented for an operator. Recorded at rev-7.

## The branch pin moved

`refusal_join.py`'s `BRANCH_PIN` is re-derived 161 -> 180 in this commit, covering `-7`'s, `-8`'s and
`-10`'s new refusal branches, with both values named beside it per that file's own convention. §7 of
this spec asks for exactly that at landing.
