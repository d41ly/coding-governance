# TOOL-aCollapsedScan-13 — checks 23 and 21 stop shelling out to read data they already hold

**Status:** CLOSED · rev-3 · 2026-08-26 · node a · Tier-2 · base 3c37a1fb · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-build-TOOL-aCollapsedScan-13-equivalence-harness.sh](../build/2026-08-26-build-TOOL-aCollapsedScan-13-equivalence-harness.sh) | journal | — |
| [2026-08-27-build-TOOL-aCollapsedScan-13-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aCollapsedScan-13-acceptance-ledger.md) | journal | — |
| [2026-08-26-review-TOOL-aCollapsedScan-13-closing-diff.md](../reviews/2026-08-26-review-TOOL-aCollapsedScan-13-closing-diff.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

Take the process-creation cost out of `check-memory-hygiene.sh`, the leg that gates every commit in
this repo, without changing what any check covers or reports. Two checks are 93% of it, and both
spend their time running external commands to inspect strings already held in shell variables.

## 2. Scope (IN)

- **S1** — Check 23's per-spec filter stops forking to decide scope: `${sp##*/}` for the basename, a
  substring expansion for the date, a shell string compare for the cutoff, and one read of the
  spec's head for the status header instead of `sed` piped into `grep`.
- **S2** — Check 23's per-criterion lookup stops running `printf` into `grep -m1 -E` per (unit,
  label) pair. `$alledger` is already in memory; it is loaded once into a `declare -A` keyed
  `"<uid> <lab>"` and read by subscript.
- **S3** — Check 21's branch 4 stops running four processes per record. The `grep -oE` over the
  filename stem becomes a `case` pattern with parameter expansion, and the `printf | tr | grep -qxF`
  membership test becomes `case " $ids " in *" $claimed "*)`.
- **S4** — An equivalence proof over the real corpus: the checker's stdout and exit status are
  byte-identical before and after, on a clean tree AND on a staged break per touched check.

## 3. Non-goals (OUT)

- Changing what any check COVERS. Every spec still walked, every record still projected, every pair
  still graded. S4 is what holds this unit to that, and it outranks the speed criterion if the two
  ever conflict.
- Scoping check 23 to changed specs. It asserts a PAIRING between a spec and a journal record, and
  that pairing breaks without the spec changing. Walking terminal specs is correct and stays.
- Checks 10 and 11. Measured at 0.3 s and 0.0 s — check 11's loop iterates zero times because
  `TOMBSTONE_ROOTS=""`. An earlier revision of this spec proposed fixing both; §4 records why.
- `gen_build_index.py --print-bindings`, measured at 2.5 s, which is 0.6% of the check that calls
  it. The Python parse is not the problem in either check.
- Declaring a wall-clock ceiling for this leg. `tools/gate-legs.json` has no field for one; that is
  `TOOL-aCollapsedScan-5`.

## 4. Design

### The measurement, and the three wrong answers before it

The figures below come from a scratch copy of the checker with an `EPOCHREALTIME` stamp printed at
each check banner, so every figure is the gap between one check's own two timestamps.

| region | seconds | share |
|---|---|---|
| check 23 | 1035.9 | 81% |
| check 21 | 149.6 | 12% |
| banner 20 to check 23 | 47.8 | 4% |
| check 12 | 25.8 | 2% |
| check 10 | 0.3 | — |
| check 11 | 0.0 | — |

**Three earlier attributions were wrong, and how is worth more than the table.**

1. A `bash -x` profile keyed on `LINENO` put check 23 at 69% and checks 10 and 11 at 22%. The 10/11
   figures were artifacts: `set -x` reports `LINENO` for the enclosing construct, so time from
   elsewhere lands on a construct's first line. Check 11 was credited with 831 hits over a loop that
   iterates ZERO times, check 10 with 842 over a population of 3 files.
2. A first checkpoint probe put check 21 at 80%. That probe's `END` stamp sat after the script's
   `exit` and never fired, so the region containing check 23 went unmeasured and a truncated span
   was read as the whole. Check 21 is real, at 12% rather than 80%.
3. The 2.19 s per record measured for check 21's loop over 20 iterations extrapolates to ~606 s
   against the probe's 149.6 s. The extrapolation ran under a concurrent full bar and the probe did
   not; neither figure is wrong, and only the ratio is safe to carry.

**The test that separates a measurement from an artifact is whether its counts can be true.** Check
23's reconcile against the corpus — 320 tracked specs, 1323 acceptance-criterion pairs across 57
in-scope specs — and check 11's did not, against a loop that cannot run.

### Why these two checks are slow

Neither is compute-bound. Both hold their data in shell variables and shell out to look at it.

**Check 23**, per spec: `basename` twice, `cut`, `printf` into `sort -C`, `sed` into `grep` — about
seven processes to decide whether a spec is in scope at all, and 263 of 320 are not. Then, per
acceptance criterion, `printf` into `grep -m1 -E` to search `$alledger`, which is already a
variable: 1323 pairs, two processes each. About 4,900 spawns.

**Check 21 branch 4**, per record: `grep -oE` to pull the claimed id out of the filename stem, then
`printf | tr | grep -qxF` to ask whether that id appears in `$ids`, also already a variable. Four
processes over 277 records, about 1,100 spawns.

The 4.4:1 ratio those spawn counts predict is the same order as the 6.9:1 the probe measured, which
is the third independent thing that has to agree before this design is trusted.

### Alternatives rejected

- **Scoping either walk.** §3 states why for check 23; check 21's population is every record and its
  assertion is about the record's own name, so there is nothing to scope by.
- **Moving either check into Python.** It would remove the spawns by moving the work, at the cost of
  a second reader of a grammar `HYGIENE.md` documents once — and `gen_build_index.py` already does
  the parse both checks consume.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` only, plus the memory-tree kit version marker.

## 5. Production-readiness checklist

- security — N/A. No new input, write path or network call.
- perf / scale — the subject. Measured before and after per AC3.
- a11y / i18n — N/A.
- error / empty / loading states — the empty-`$labs` arm in check 23 and branch 4's two
  name-carries-no-id arms in check 21 keep their behaviour; AC1's byte comparison proves it.
- observability — refusal text unchanged by construction, since AC1 compares bytes.
- risks — THE risk is silently weakening a merge-bar gate: a refactor that makes a check stop
  finding things looks exactly like a faster check. AC2 is the answer and it outranks AC3.
- testing + left-shift gates — AC2's staged breaks, plus the memory-tree kit's own suites.
- migration / rollback — a single-file revert.
- user docs — none owed.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs on the clean tree before and
  after, its stdout and exit status are byte-identical, proven by `diff` of the two captures.
- **AC2** — When a break is staged for check 23 and for check 21 and
  `bash tools/memory-tree/check-memory-hygiene.sh` runs, each is reported with a message
  byte-identical to the pre-change checker's, and both exit 1. A check whose break cannot be staged
  is named unproven rather than assumed.
- **AC3** — When the leg is timed with `bash tools/memory-tree/check-memory-hygiene.sh` before and
  after under the same machine load, taken back to back, the after figure is at most half the
  before. The ratio is the claim; the absolute seconds are recorded with the load state named.
- **AC4** — When the checkpoint probe is re-run with `EPOCHREALTIME`, neither check 23 nor check 21
  is the largest region.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs, the bar is green.

## 7. Gates

`memory hygiene` — which is the subject, so its own green is necessary and not sufficient; AC2 is
what makes it meaningful. Plus the memory-tree kit's self-tests and the full bar.

## 8. Open questions

- **F1 — refactor in shell, or move the hot checks into Python?** RESOLVED (agent, 2026-08-26,
  delegated): shell. §4 records the reason.
- **F2 — is a `declare -A` acceptable here?** RESOLVED (agent, 2026-08-26, delegated): yes, this
  file already uses three.
- **F3 — should the leg gain a declared ceiling so the cost cannot silently return?** RESOLVED
  (agent, 2026-08-26, delegated): not here — no leg in `tools/gate-legs.json` can carry one, which
  is `TOOL-aCollapsedScan-5`. AC4's re-profile is this unit's own guard.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft, against a `bash -x` line profile.
- rev-2 · 2026-08-26 · AC3 rewritten before any code: as drafted it demanded an idle box and this one
  was not idle, and a criterion known to be unmeetable is not a criterion.
- rev-3 · 2026-08-26 · rewritten against a checkpoint probe after the line profile was found to carry
  artifacts. Checks 10 and 11 leave the scope entirely (0.3 s and 0.0 s, against 186 s and 118 s in
  the discarded profile); check 21 branch 4 enters it at 12%; check 23 is confirmed at 81% and keeps
  its two scope items. §4 records all three wrong answers and the test that separates a measurement
  from an artifact, because that is the reusable part.

## 10. Reuse audit

The seam is `check-memory-hygiene.sh` itself; this unit changes how two of its checks reach data
they already hold and adds no new reader. The prior art it copies is `TOOL-aCollapsedScan-1` in this
same build — one pass into a map, then lookups — and `TOOL-dNarrowedAnchor-1`, which cut the same
class from the unattended gate self-test. No reuse probe was needed to find the seam: the checkpoint
profile names the checks, and the four-processes-per-record pattern is visible in the source.
