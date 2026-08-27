# Acceptance ledger — DEPL-dCarriedReceipt-1, `{relpath}` in the seam that writes

**Serves:** journal DEPL-dCarriedReceipt-1

**Evidences:** DEPL-dCarriedReceipt-1
- AC1 — `python tools/govkit/govkit.py apply --target <scratch> --kits push-main` — the RED was
  observed on a live target BEFORE the fix and is recorded in this build's merged-row reproduction:
  the receipt carried `pre-push` and `pre-push.test.sh` at the target ROOT while the rule's own
  `claims` spell `.githooks/pre-push`. After the fix the same command lands
  `.githooks/pre-push` and `.githooks/pre-push.test.sh`, and the receipt names them.
- AC2 — `tools/govkit/selftest.py` — the arm `[-1] a source under `home` still resolves to its
  basename` asserts `push-main.sh` resolves to `tools/push-main.sh` through the same seam. It stays
  GREEN with the defect staged back in, which is what makes it a regression guard rather than a
  restatement of AC1.
- AC3 — `python tools/govkit/govkit.py apply --target <scratch> --kits push-main` — five files
  landed and six receipt rows written, the same counts as before the change; only the two hook
  destinations moved. The NicoCares reading AC3 names was NOT taken: that target is not present in
  this tree, and the scratch target is the substitute. Stated rather than implied.
- AC4 — `python tools/govkit/govkit.py selfcheck` — green across the shipped registry, and RED with
  the defect staged, naming `push-main` and both destinations by name. The first draft of this arm
  did NOT red: it asked `rule_destinations`, which routes through `destinations_for` — the resolver
  that was already correct — so it graded the healthy path and could not fail on the writer's bug.
  Re-aimed at `resolve_dests`, the seam `plan`, the write loop and the wildcard exclusion all call,
  and re-observed RED.

## What S2's grep established

`grep -rn "{relpath}" tools/ --include=*.py` returns three sites, and the spec required each to be
routed or recorded as deliberately not routed:

- `destinations_for` — ALREADY routed through `rule_relpath`. This was half the defect: two
  resolvers, one right and one wrong, for one token.
- the membership test `"{relpath}" not in d` — deliberately NOT routed. It asks whether a template
  still carries the token, which is a question about the template rather than about a source, and
  there is nothing for `rule_relpath` to resolve.
- `resolve_dests` — the defect, and the one this unit fixes.

## What this ledger does not claim

The `selfcheck` arm is scoped to rules declaring BOTH `to` and `claims`, and skips any destination
still carrying an unresolved `{...}` token. Those are answer keys a target supplies and `claims` are
written without them, so comparing the two spellings would red every templated rule in the registry.
A rule declaring no `claims` states no second opinion and is therefore ungraded by this arm — the
gate is only as wide as the second opinion it compares against, and that bound is stated rather than
discovered later.

The default branch of `resolve_dests` — the one taken when a rule declares no `to` — still computes
its own home-relative path inline rather than calling `rule_relpath`. It carries no `{relpath}`
token, so S2's grep does not reach it and S1 does not name it. It is a duplicated computation of the
same idea and a candidate for the same treatment; it is recorded here rather than changed, because
`rule_relpath` returns the whole source for a `root_relative` rule and that would move the
destination of any future `root_relative` rule declaring no `to`.
