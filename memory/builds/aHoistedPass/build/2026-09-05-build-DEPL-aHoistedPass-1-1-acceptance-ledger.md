**Serves:** journal DEPL-aHoistedPass-1

# Acceptance ledger — DEPL-aHoistedPass-1

Tier-2 · node a · 2026-09-05 · landed at `867b14a9`

`requires` bought install ORDER and nothing else, so a kit descriptor could name a dependency no verb
checked and no gate redded. Both places it can mean something now do: a registry-name arm in
`selfcheck` check 7, and an installed-set refusal in `_cmd_apply`, with a printed row in `cmd_plan`
that moves no exit code.

## Acceptance criteria

**Evidences:** DEPL-aHoistedPass-1

- AC1 — MET — `python tools/govkit/govkit.py selfcheck` exits 0 on the untouched tree and again after
  arm A lands.
- AC2 — MET — arm A's FAILING CASE, observed before landing. `kit.toml:7` staged as
  `requires = ["memory-tree", "reviewharness"]` makes `selfcheck` exit 1 printing
  `entry 'unattended' requires 'reviewharness', which is not a registry entry`. Unstaged after, and
  the same command exits 0.
- AC3 — MET — `apply --target <virgin> --kits unattended` exits 2 naming BOTH `memory-tree` and
  `review-harness` in one refusal. Both, which is what an arm expecting one name cannot tell from a
  half-built check.
- AC4 — MET — `apply --kits memory-tree,settings-merge,agent-cap,review-harness,unattended` passes
  the new check: zero occurrences of the refusal in its output. That run exits 1 further down, in the
  render step, for a reason belonging to a bare scratch target and not to this unit; the criterion is
  about the new check and the new check did not fire.
- AC5 — MET — a target whose receipt already claims `review-harness` and `memory-tree`, given
  `apply --kits unattended`, passes the check (zero occurrences) and proceeds into the install. The
  receipt carve-out is exercised rather than assumed.
- AC6 — MET — `plan --target <virgin> --kits unattended` prints two `UNMET` rows AND exits 0.
- AC7 — MET — `plan --kits review-harness,unattended` prints
  `selection: review-harness, unattended`, which is the only thing the edge itself buys.
- AC8 — MET, and it REFUTED the spec — `python tools/govkit/selftest.py` run BY HAND ends
  `govkit-selftest: all arms held`, exit 0. The first run exited 1 with three arms failing, and they
  were the arms section 4 said could not fail: plan-versus-apply SET EQUALITIES, which a larger apply
  selection is exactly what moves. The repair is eleven call sites rather than nine, because each
  paired `plan` moves with its `apply`. Nothing on any bar would have reported it, which is why AC8
  is a by-hand run and not a claim.
- AC9 — MET — `python tools/govkit/refusal_join.py` exits 0 reporting `246 branch(es) across 4
  module(s)`, exactly two higher than the 244 measured at the spec's base, with `BRANCH_PIN` unmoved
  at 217.
- AC10 — MET AS AMENDED at rev-5 — `bash tools/check-kit-versions.sh` exits 0 with
  `KIT_GOVKIT_VERSION` at `1.10`. **The eight `unattended` carriers stay at `1.17` deliberately**:
  rev-5 withdrew rev-3's resolution of F1 and parked the bump, because the move edits
  `SKILL.template.md`'s marker and ruling D1 puts that on the M3 veto-2 list the mandate's delegation
  does not reach. The criterion says in its own words that the checker's green is NOT evidence the
  version is right — it grades agreement, never movement.
- AC11 — MET — `bash tools/check-install-prefix.sh` exits 0 and `tools/install-prefix-carried.txt` is
  byte-unchanged: both new strings name kit ids and no `tools/` path.
- AC12 — MET — the `derive_install_order` docstring's `--kits drift-audit` sentence now carries the
  clause naming the apply-time check, landed in the same commit as arm B, and stays literally true
  about the function it documents.
- AC13 — MET — arm B's refusal names the remedy: add the missing id to `--kits`, or install it first
  and re-run, and says govkit does not widen a selection on the operator's behalf.
- AC14 — MET AS AMENDED — all three rows S9 names are present in `memory/backlog/DEPL.md` BY ID. The
  mis-spelled-`require`-key row is `DEPL-aHoistedPass-5`, filed at `order 1` by
  `TOOL-aHoistedPass-1` S3 from the same design bullet and NOT re-minted here; this unit minted
  `DEPL-aHoistedPass-9` for the stale `BRANCH_PIN`/`FILE_PIN` and `DEPL-aHoistedPass-10` for the
  ungraded ninth `unattended` carrier. Graded by id and never by a count, because a count cannot tell
  a row that already existed from one nobody filed.

## What the spec could not have known

**Three selftest arms compare a `plan` to an `apply` and were never given the same selection.** They
only ever passed because the two verbs happened to name the same kits, and the moment arm B forced a
wider apply the equality broke with the whole of `memory-tree` in `applied-only`. An arm whose
subject is plan/apply agreement must give both verbs one selection; the fix is the paired call site,
never the assertion.

## What is parked to the owner

The `unattended` 1.17-to-1.18 bump, with its full carrier list: eight graded by
`check-kit-versions.sh`, five rendered by `adopt-unattended.sh` and byte-compared by the unguarded
`unattended skill wiring` leg, and a ninth outside both populations. Three sibling units stood down
from that move on the strength of this unit taking it, and order 2 now performs nothing — their
assertions stay true, because the checker grades agreement rather than movement, and the build closes
with the `unattended` payload changed and its version unmoved.
