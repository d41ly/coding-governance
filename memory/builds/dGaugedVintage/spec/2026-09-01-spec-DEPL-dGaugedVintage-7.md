# DEPL-dGaugedVintage-7 — a ratchet that counts lines cannot see a swapped literal

**Status:** CLOSED · rev-3 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 6 · ratified 2026-09-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-DEPL-dGaugedVintage-7-acceptance-ledger.md](../build/2026-09-01-build-DEPL-dGaugedVintage-7-acceptance-ledger.md) | journal | — |
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-install-prefix.sh` has TWO arms with two regexes, and this unit changes the second.
Arm 1's `RE` (`:63`) matches the bare `<kit>/<file>` root spelling and is waived per `<path>:<line>`.
Arm 2's `re_ship` (`:201`) binds a literal `tools/` prefix and feeds the shrink-only ratchet with
`grep -cHE`, which counts matching LINES. So a second SHIPPING-prefix literal on a line that already
carries one keeps the count, and one kit's path swapped for another's keeps it too: the ledger stays
level while the surface it describes changes.

## 2. Scope (IN)

- **S1** — Count LITERALS rather than lines in ARM 2 only: the ratchet's per-file number becomes the
  number of `tools/<kit>/<file>` occurrences matched by `re_ship` (`:201`), so a second occurrence on
  one line raises it.
- **S2** — Re-measure `tools/install-prefix-carried.txt` against the new counting in the same change,
  because every existing row was written under line counting and most will move.
- **S3** — NOT BUILT, and recorded rather than dropped. The identity arm needs a THIRD field in
  `tools/install-prefix-carried.txt` and a second comparison inside the ratchet's awk, on a gate that
  is on the merge bar — a unit-sized change of its own, and one whose failure mode is a subtly wrong
  awk program grading the shipped surface. The swap blind spot therefore SURVIVES this unit: one
  kit's path exchanged for another's at equal occurrence count still passes. Filed as the follow-up
  in §8 F1 rather than left implied.
- **S4** — A fixture for each of the two blind spots, both observed RED before the fix.

## 3. Non-goals (OUT)

- The population's exclusions. `*.test.sh`, `selftest.py` and `*.conf.example` stay excluded for the
  reasons the script's header gives, and whether those exclusions are too wide is its own question.
- The waiver registry's contents. `tools/install-prefix-waivers.txt` rows are unaffected; only the
  counting changes.
- Making the checker prefix-parametric. That is `DEPL-dCarriedReceipt-15` and it is a larger unit
  this one must not absorb.
- Reducing the carried count. This unit measures honestly; draining is separate work.
- **Arm 1's identical blind spot.** `RE` at `:63` is waived per `<path>:<line>`, so two literals on
  one line collapse there too. Deferred deliberately: arm 1's waiver granularity is line-keyed and
  changing it rewrites `tools/install-prefix-waivers.txt`, which is a second migration. It wants its
  own unit.

## 4. Design

### Inventory

| Site | Today | After |
|---|---|---|
| arm 2 counting (`:201`, `re_ship`, shipping prefix) | `xargs -0 -r grep -cHE` — hit lines | occurrences |
| arm 1 (`:63`, `RE`, bare root spelling) | `grep -HnE`, waived per `<path>:<line>` | unchanged — see §3 |
| `install-prefix-carried.txt` | `<path>\t<count>` under line counting | re-measured under occurrence counting |
| identity of the named kit | not recorded | recorded per S3 |

The script's own comment already says the count is hit LINES, so this is a known property rather than
a misreading of the code; what is new is that the property is a hole and not merely a choice.

### Migration

S2 rewrites the ledger's numbers. That is a large mechanical diff and it must land in the same commit
as S1, or the ratchet reds for every session in between.

### Alternatives rejected

Adding a second, occurrence-counted ledger beside the line-counted one was rejected: two ledgers over
one population is a second answer to one question, and the older one would rot.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — `grep -o | wc -l` over the same population; the population is the cost and it is
  unchanged.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the population must be asserted non-empty, as it is today, so a
  mis-scoped selector fails loudly rather than reporting a clean zero.
- observability — the run prints the total occurrence count so a drain is visible.
- risks — S2's re-measure could hide a real increase inside a large mechanical diff. Mitigated by
  landing S1 and S2 together with the before and after totals stated in the commit message.
- testing + left-shift gates — S4, and both arms are observed RED first.
- migration / rollback — the ledger's numbers change meaning. The file's header must say which
  counting produced them, or a future reader compares incomparable numbers.
- user docs — none; the script's header is the doc.

## 6. Acceptance criteria

- **AC1** — When two SHIPPING-prefix literals — `tools/<kit>/<file>.<ext>`, the form `re_ship`
  matches — sit on one line of a shipped file, `bash tools/check-install-prefix.sh` counts two,
  observed on a fixture where today it counts one.
- **AC2** — AMENDED at build time: NOT MET, because S3 was not built. A kit path swapped for
  another's at equal occurrence count still passes `bash tools/check-install-prefix.sh`. Stated as an
  open hole rather than quietly dropped — the unit closes the line-counting blind spot and leaves the
  identity one.
- **AC3** — When the tree is unchanged, `bash tools/check-install-prefix.sh` exits 0 against the
  re-measured ledger.
- **AC4** — AMENDED to the one blind spot this unit closes. RED OBSERVED for the line-counting
  case: appending a single line carrying TWO shipping-prefix literals moved
  `bash tools/check-install-prefix.sh`'s count for that file 3 -> 4 under the old counting, where two
  occurrences require 3 -> 5. The swap case was not staged, because S3 that would catch it was not
  built.
- **AC5** — `bash tools/check-install-prefix.sh --write-ratchet` reproduces the committed ledger
  byte-for-byte, so the file cannot drift from the counting that produced it.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the install-prefix leg, and `testsuite counts` because S4 adds
arms.

## 8. Open questions

- **F1 — the ledger's row shape under S3, now the follow-up this unit files.** The ratchet's awk
  reads `pin[$1]=$2` and `now[$1]=$2`, so a third field is inert until a second comparison is added
  beside it — which is the work, not the field. Recommendation stands: a third tab-separated field
  holding a sorted kit list, never a separate ledger. `prior:` no prior ruling found. Unresolved, and
  deliberately so: it is the next unit.
- **F2 — whether the header must state the counting.** RESOLVED (agent, 2026-09-01, delegated): yes,
  and it does. The emitter's own comment now says OCCURRENCES per path, quotes the measured 3 -> 4
  versus 3 -> 5, and names the id — so a future reader comparing an old number to a new one is told
  the unit changed. `prior:` no prior ruling found.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit H6. AC1's fixture used the bare root spelling, which
  the arm this unit changes cannot match: `re_ship` at `:201` binds a literal `tools/` prefix. §1, §2
  and §4 now name the two arms separately, AC1's fixture is a shipping-prefix pair, and §3 defers
  arm 1's identical blind spot with the reason.

- rev-3 · 2026-09-01 · BUILT and CLOSED, PARTIALLY. Arm 2 counts occurrences (`grep -oHE` plus an
  awk tally) instead of hit lines, and the ledger was re-measured in the same change: 12 of 108
  rows moved. S3's identity arm was NOT built and AC2 is not met — the swap blind spot survives,
  and §8 F1 is now the follow-up that closes it. F2 resolved.
  Acceptance ledger at `build/2026-09-01-build-DEPL-dGaugedVintage-7-acceptance-ledger.md`.
## 10. Reuse audit

- No existing seam fits: `python tools/codebase-map/reuse_lookup.py "count root prefix literals in
  shipped files"` returns `repo_root`, `map_root`, `require_adopted_root` and `tracked_files`, none
  of which counts anything. The counting lives inline in `tools/check-install-prefix.sh` and this
  unit changes it in place, which is correct for a gate that is one predicate over one population.
- Recall terms used: `check-install-prefix carried ratchet grep count literal carry map relocate
  needle rung prefix adopter`
