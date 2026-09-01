# DEPL-dGaugedVintage-7 — a ratchet that counts lines cannot see a swapped literal

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-install-prefix.sh` ratchets root-prefix spellings with `grep -c`, which counts matching
LINES. A second literal added to a line that already carries one keeps the count, and one kit's path
swapped for another's keeps it too, so the shrink-only ledger can stay level while the surface it
describes changes.

## 2. Scope (IN)

- **S1** — Count LITERALS rather than lines: the ratchet's per-file number becomes the number of
  root-prefix occurrences, so a second occurrence on one line raises it.
- **S2** — Re-measure `tools/install-prefix-carried.txt` against the new counting in the same change,
  because every existing row was written under line counting and most will move.
- **S3** — An identity arm: the ledger records WHICH kit each occurrence names, so swapping one kit's
  path for another's at equal count reds.
- **S4** — A fixture for each of the two blind spots, both observed RED before the fix.

## 3. Non-goals (OUT)

- The population's exclusions. `*.test.sh`, `selftest.py` and `*.conf.example` stay excluded for the
  reasons the script's header gives, and whether those exclusions are too wide is its own question.
- The waiver registry's contents. `tools/install-prefix-waivers.txt` rows are unaffected; only the
  counting changes.
- Making the checker prefix-parametric. That is `DEPL-dCarriedReceipt-15` and it is a larger unit
  this one must not absorb.
- Reducing the carried count. This unit measures honestly; draining is separate work.

## 4. Design

### Inventory

| Site | Today | After |
|---|---|---|
| `check-install-prefix.sh` counting | `xargs -0 -r grep -cHE "$re_ship"` — hit lines | occurrences |
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

- **AC1** — When two root-prefix literals sit on one line of a shipped file,
  `bash tools/check-install-prefix.sh` counts two, observed on a fixture where today it counts one.
- **AC2** — When one kit's path is swapped for another's at equal count,
  `bash tools/check-install-prefix.sh` exits non-zero and names the file, observed on a fixture.
- **AC3** — When the tree is unchanged, `bash tools/check-install-prefix.sh` exits 0 against the
  re-measured ledger.
- **AC4** — Both blind spots are observed RED before the fix: stage each fixture, run
  `bash tools/check-install-prefix.sh` at current `HEAD`, and confirm it exits 0 where it should not.
- **AC5** — `bash tools/check-install-prefix.sh --write-ratchet` reproduces the committed ledger
  byte-for-byte, so the file cannot drift from the counting that produced it.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the install-prefix leg, and `testsuite counts` because S4 adds
arms.

## 8. Open questions

- **F1 — the ledger's row shape under S3.** Recording the kit identity per occurrence makes the row
  wider than `<path>\t<count>`. Options: a third tab-separated field holding a sorted kit list, or a
  separate identity ledger. Recommendation: the third field, because a separate file is the second
  answer §4 rejected. Unresolved.
- **F2 — whether the header must state the counting.** A number whose meaning changed silently is
  the class this unit exists to close, one level up. Recommendation: yes, and the migration line in
  §5 says so. Unresolved only in wording.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.

## 10. Reuse audit

- No existing seam fits: `python tools/codebase-map/reuse_lookup.py "count root prefix literals in
  shipped files"` returns `repo_root`, `map_root`, `require_adopted_root` and `tracked_files`, none
  of which counts anything. The counting lives inline in `tools/check-install-prefix.sh` and this
  unit changes it in place, which is correct for a gate that is one predicate over one population.
- Recall terms used: `check-install-prefix carried ratchet grep count literal carry map relocate
  needle rung prefix adopter`
