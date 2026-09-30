# TOOL-aRepatriatedFork-51 — brief-recorded takes a declared waiver registry, as pass-order does

**Status:** SPECCED · rev-1 · 2026-10-01 · node a · Tier-1 · base 6e7cb0df · streams tooling · order 22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-prompt-TOOL-aRepatriatedFork-51-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aRepatriatedFork-51-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The full bar at `6e7cb0df` redded the `brief-recorded` leg on two closed units of this build.
`TOOL-aRepatriatedFork-44` was built with no recorded brief, which history cannot fix.
`TOOL-aRepatriatedFork-46` is misread: the shared build-commit pick takes its adoption records commit
`09dae486`, which named it and moved `.memory-tree.conf` pins. The sibling `pass-order` leg met the same
misread and carries a declared waiver registry for it. This leg has none, so its only honest outcomes
were a fabricated row or a run that can never land. This unit gives it the sibling's registry.

## 2. Scope (IN)

- **S1** — `check-brief-recorded.sh` reads `memory/project/brief-recorded-waiver.txt` from HEAD, one
  `<unit-id><TAB><reason>` row per waived unit. A violation of a waived unit is counted and not
  reported. An absent file waives nothing. Observed by AC1 and AC3.
- **S2** — A row naming a unit the leg no longer reports reds the leg by name. Observed by AC2.
- **S3** — The liveness output gains one line naming the waived count and units. Observed by AC1.

## 3. Non-goals (OUT)

- Fixing the build-commit misread. `TOOL-aRepatriatedFork-48` files it for both legs.
- A declarable registry path. `pass-order`'s `PASS_ORDER_WAIVER` exists for an adopter with no
  `project/` directory, and none has asked for this leg's.
- The waiver rows themselves. They are records, written after this unit and parked for the owner.

### Edges

none

## 4. Design

### Mechanism

The block is `check-pass-order.sh`'s registry read, ported with its two properties. Every violation
site calls one function, `add_violation`, which counts a waived id or appends the message. After the
walk, each registry id that no violation named is stale.

### Inventory

This unit mints one shell function in `tools/unattended/check-brief-recorded.sh`, `add_violation`. It
leads with the declared verb `add` and is `snake`, the `sh.function` cell, per `lexicon.py --suggest`.

### Files touched (estimate)

- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/check-brief-recorded.test.sh`

### Alternatives rejected

- A retroactive brief row for `TOOL-aRepatriatedFork-44`. It would record a brief nobody handed.
- Moving `BRIEF_RECORDED_CUTOFF`. It would exempt every unit of every build opened in the window.

## 5. Production-readiness checklist

- security — the registry is a bypass the graded run can commit, exactly as `pass-order`'s is and as
  the leg's conf already is. A stale row reds, so a waiver cannot outlive its violation.
- perf / scale — one `git show` per run.
- error / empty / loading states — an absent registry waives nothing.
- observability — S3's line names every waived unit on every run.
- risks — a waiver hides a real violation. Each row is parked for the owner when written.
- testing — AC1 to AC3.
- migration — none. The unattended kit's version is already moved on this branch.
- user docs — none. No `help/` page describes the leg.

## 6. Acceptance criteria

- **AC1** — When `check-brief-recorded.sh` runs over a fixture with no brief row and a committed
  `brief-recorded-waiver.txt` naming `ARCH-tBrief-1`, it exits 0 and prints `1 violation(s) waived`.
  Red when: the `6e7cb0df` leg exits 1 on the same fixture.
- **AC2** — When the same registry is committed over a conforming fixture, the leg exits 1 naming
  `ARCH-tBrief-1` as a stale exemption.
  Red when: the `6e7cb0df` leg exits 0.
- **AC3** — When the registry exists only in the working tree, the leg exits 1 and prints
  `0 violation(s) waived`.
  Red when: an uncommitted row waives the violation.

## 7. Gates

`brief-recorded` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: `tools/unattended/check-brief-recorded.test.sh` · a committed, a stale and an uncommitted one-row registry · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, promoted by the VERIFYING repair pass R1 from the full bar's
  `brief-recorded` red at `6e7cb0df`.

## 10. Reuse audit

The seam is `check-pass-order.sh`'s waiver registry, found by reading. `reuse_lookup.py` reports `.sh`
as an unscanned layer, so it cannot see it. The read is ported rather than shared because each leg
installs standalone and this kit's library holds no registry reader today.

Recall terms used: `brief-recorded waiver registry pass-order stale row exemption build_commit misread adoption records commit`.
