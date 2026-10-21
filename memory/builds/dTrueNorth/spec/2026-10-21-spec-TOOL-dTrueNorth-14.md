# TOOL-dTrueNorth-14 — the audit-pin arm grades a record by the harness that wrote it, so a run in flight is not refused at its merge

**Status:** OPEN · rev-1 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 3

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
confirmed finding **id 40 at HIGH**, its item **H7**: the audit-pin cutoff refuses records written by
runs already in flight. `TOOL-dTrueNorth-5` S6 sets `SPEC_AUDIT_PIN_CUTOFF` by the relation
`SPEC_DIRECT_CUTOFF` uses, the day after the newest filename date on any ref. That holds for specs,
dated once, and fails for review records: a run whose base predates the landing keeps running its own
harness and writes unpinned `spec-audit` records dated after the cutoff. When it merges main it brings
in the arm, and check 21 fails records whose bytes are fixed, leaving a hand edit or a legacy entry as
the only exits. Spec-audit records are written every day and many worktrees run at once. This unit
grades a record by the harness that wrote it: a record whose adding commit's review harness lacks
`renderAuditBinding` owes no pin. It repairs `TOOL-dTrueNorth-5`.

## 2. Scope (IN)

- **S1** — `derive_audit_writers(root, rels)` in `tools/memory-tree/gen_build_index.py` takes the
  `spec-audit` records `TOOL-dTrueNorth-5` S3 grades and returns those written by an older harness.
  One `git log --no-renames --diff-filter=A --format=%x00%H --name-only -- <rels>` finds each
  record's adding commit; one `git cat-file --batch`, read as bytes, reads the review harness at each
  distinct adding commit; a record whose harness text lacks `renderAuditBinding` is in the set. The
  harness's path is the workflows kit's `tier2-review.js`, located by
  `backlog.resolve_kit_dir("workflows", "tier2-review.js", <this kit's directory>)`. With no graded
  record it makes no git call. Observed by AC1 and AC2.
- **S2** — `cmd_print_bindings` prints no `P` row for a record in that set, and its `Q` row gains a
  fourth field, the count exempted: `Q<TAB><graded><TAB><cutoff, or off><TAB><exempt>`. A record with
  no adding commit, staged and not yet committed, is graded, since the tree's own harness is writing
  it. A workflows kit that does not resolve exempts nothing and prints the fourth field as `-`.
  Observed by AC1, AC2 and AC3.
- **S3** — Check 21's audit-pin branch (`TOOL-dTrueNorth-5` S4) reads the `Q` row by its `^Q\t`
  prefix and names the exempt count in its stderr line: `the audit-pin arm graded <k> spec-audit
  record(s) from SPEC_AUDIT_PIN_CUTOFF=<v>, <e> written by a harness before renderAuditBinding`.
  Observed by AC4.
- **S4** — The comment above `SPEC_AUDIT_PIN_CUTOFF` in `.memory-tree.conf` says why a record written
  after the landing by an older harness is safe, the writer test of S1, in place of the filename
  relation alone, which `TOOL-dTrueNorth-5` S6 relied on. Observed by AC5.

## 3. Non-goals (OUT)

- Design-document subjects: `TOOL-dTrueNorth-13`. A record that test exempts and a record this one
  exempts both print no `P` row, and neither reads the other's input.
- Re-pinning or rewriting any record already tracked.
- A report-only arm until every live run's base holds this unit, the finding's second option: no
  reader in the kit can enumerate every live run's base, so it could not be derived.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-5` — `cmd_print_bindings`' `P` and `Q` rows, `SPEC_AUDIT_PIN_CUTOFF`, `renderAuditBinding` and check 21's audit-pin branch; without them there is no arm to exempt a record from
- **hands-off** `TOOL-dTrueNorth-16` — the `Q` row's four-field shape, which its contract clause for `--print-bindings` and its docs sentence for `memory/HYGIENE.md` must spell

## 4. Design

### Evidence

- `.memory-tree.conf` justifies `SPEC_DIRECT_CUTOFF`'s relation by spec filename dates
  (`.memory-tree.conf:295-305`).
- The class is recorded in `memory/gotchas/a-merged-in-check-can-refuse-a-pinned-record.md`: a merge
  brings in a check the running record cannot satisfy because its bytes are fixed.
- Remote CI checks out full history (`.github/workflows/remote-ci.yml:61`, `fetch-depth: 0`), so an
  adding commit resolves there as it does locally; a shallow clone would read every file as added at
  its boundary, whose harness carries the function, and would grade rather than exempt.
- `TOOL-dTrueNorth-5` lands `renderAuditBinding` and both writers in one commit (its §4 Rollout), so
  a harness carrying the function is a harness that writes pinned lines.
- `backlog.resolve_kit_dir` is at `tools/memory-tree/backlog.py:1749`.

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `derive_audit_writers` | function, `tools/memory-tree/gen_build_index.py` | `py.function`, OK |
| the `Q` row's fourth field | `--print-bindings` output | none |

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `.memory-tree.conf` (the comment above `SPEC_AUDIT_PIN_CUTOFF` only)

### Alternatives rejected

- **A later cutoff.** Any fixed date reds a run that starts before the landing and merges after the
  date, so no value is safe.
- **Exempting every record dated within N days of the landing.** It guesses a run's length, and a
  run held over a weekend outlives it.

## 5. Production-readiness checklist

- security — no new write path; two read-only git calls.
- perf / scale — at the landing the arm grades zero records and makes no call; afterwards one log
  over the graded records' paths and one batch read per run of `--print-bindings`.
- error / empty / loading states — an unresolved workflows kit exempts nothing and says `-`; a record
  with no adding commit is graded.
- observability — the `Q` row and check 21's stderr line both carry the exempt count.
- risks — a hand-written unpinned record committed on a branch based before the landing is exempt;
  its harness could not have pinned it either.
- testing — AC1 to AC3 and AC5 as probes; AC4 through the hygiene suite's arm at the close.
- migration — none.
- user docs — the conf comment; the `memory/HYGIENE.md` sentence on the `Q` row is
  `TOOL-dTrueNorth-16`'s item for id 17.

## 6. Acceptance criteria

- **AC1** — When a probe builds a fixture git repository under `%TEMP%` whose commit A holds a fixture
  `tools/workflows/tier2-review.js` without `renderAuditBinding` and a conf setting
  `SPEC_AUDIT_PIN_CUTOFF="2026-01-01"`, branches `run` from A and commits there an unpinned
  `spec-audit` record dated 2026-02-02, lands on `main` a commit L adding `renderAuditBinding` to the
  fixture harness, merges `run` into `main`, and calls `cmd_print_bindings` in-process, it prints no
  `P` row for that record and a `Q` row whose fourth field is 1.
  Red when: the merged record prints a `P` row, which is check 21 failing a run in flight.
  fixture: a fixture repository under a short `%TEMP%` path; the tree holds none.
- **AC2** — When the same fixture then commits on `main` an unpinned record dated 2026-02-03, the call
  prints one `P` row for it.
  Red when: the writer test exempts a record the pinning harness wrote.
- **AC3** — When an unpinned record is staged and not committed in that fixture, the call prints a
  `P` row for it.
  Red when: a record with no adding commit is exempt.
- **AC4** — When the hygiene engine runs over AC1's fixture, check 21 passes and its stderr line names
  `1 written by a harness before renderAuditBinding`.
  Red when: the branch reads the old three-field `Q` row and fails it.
  permission: the hygiene engine is a gate leg no role agent may run; the main loop observes it
  through the hygiene suite's `New arm:` line in §7.
- **AC5** — When `grep -n -B3 '^SPEC_AUDIT_PIN_CUTOFF=' .memory-tree.conf` runs, the comment above the
  key names `renderAuditBinding` and the writer test.
  Red when: the comment still rests the key's safety on the filename relation alone.

## 7. Gates

`build-index selftest` · `memory-hygiene self-test` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `transition-audit arms` · `straggler-guard arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC1 AC2 AC3 · a branch-written unpinned record merged after the pinning harness lands, a main-written one and a staged one, against the base predicate that grades by filename date alone · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC4 · check 21 over a fixture holding an exempt record and a four-field Q row · that suite's assertion floor, raised by the arms added

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts` against the repaired unit's whole carrier; veto 1 discards both. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F2 — How is the exempt count reported?** (a) A fourth field on the `Q` row. (b) One `E` row per
  exempt record. (b) adds a row kind check 21 must learn to ignore, and a red there would be a
  stranded reader; (a) changes one row the same unit's branch already parses. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F3 — Does the build's grant lift veto 2 for the generator, engine and conf edits?** All three are
  governance carriers by `PLAY-dClosedLoop-10`'s list, and `cl-dClosedLoop-0005` names the pin and
  its grading. RESOLVED (agent, 2026-10-21, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3.
  grants: PLAY-dClosedLoop-3 the audit-pin arm's writer test, its Q row and check 21's line for the
  pin cl-dClosedLoop-0005 names · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-1 spec audit's id 40 (HIGH, item H7).

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "exempt a record written by an older harness from
a dated check"` ranked `check`, `records` and `load_affordance_exempt` by name stem, none a writer
test, so no existing seam fits the exemption; the evidence is that every dated cutoff in the kit
grades by filename date. The reads reuse two seams: `read_blobs_at_rev`'s bytes discipline for the
batch read (`tools/memory-tree/gen_build_index.py:2934`) and `backlog.resolve_kit_dir` for the
harness's path. The recall probe surfaced the gotcha this class is recorded in; it agrees with
source.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`
