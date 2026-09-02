# DEPL-dRetiredFork-1 — the carry map stops dropping a gov directory that fans into two destinations

**Status:** OPEN · rev-4 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams deployer · order 6 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

govkit already reconciles a pure repath with no operator turn. `derive_carry_rung` at
`tools/govkit/govkit.py:5135` proves a `relocate` rung when `ours == derive_carried(base, needles)`,
and `derive_carried_by_rung` applies that transform to BOTH base and theirs so the repath cancels in
the diff and `git merge-file` sees only gov's semantic change. It absorbs ZERO of NicoCares'
nineteen forks. Every row returns `rung=None`, and one measured reason is that
`derive_carry_map` DROPS any gov directory fanning into more than one target directory — seven of
them on that adopter, printed on every run. A dropped directory contributes no needle, so the rows
under it cannot prove the rung that would have reconciled them.

## 2. Scope (IN)

- **S1** — A gov directory that fans into several target directories yields needles PER ROW rather
  than being dropped. The per-row overlay `resolve_row_needles` already exists and is already
  applied; this unit makes it the resolution for the fanned case instead of the drop.
- **S2** — The drop message is retained for the case that genuinely cannot resolve, and it names
  which rows lost a needle rather than only which directory was dropped — a report naming a
  directory does not tell an operator which files are frozen.
- **S3** — A liveness assertion on the needle map: a run whose needle map is EMPTY refuses rather
  than reporting every row as unattributed, because those two states are indistinguishable today.
- **S4** — Measure the effect on both adopters read-only and record it: how many of NicoCares' 19
  and inCMS's rows move from `rung=None` to `relocate`. The number is the unit's whole value and it
  is currently unknown.
- **S3b** — GRADE every derived needle and REFUSE a degenerate one. §5's security row states
  this obligation and rev-1 built nothing for it: a needle is a path fragment used in a byte
  substitution over file content, so an empty or single-character fragment matches far more than
  the path it names, on the build's highest-severity path.
- **S5** — Arms in `tools/govkit/selftest.py` for a fanned directory whose rows resolve, a genuinely
  ambiguous row that still drops, and an empty needle map that refuses.

- **S6** — Record each adopter's `evidence: "unattributed"` row count BEFORE and AFTER. Nothing in
  the 25-unit set drives that population down, and `_cmd_update` withholds the `gov_commit`
  re-stamp while any such row exists (`tools/govkit/govkit.py:6566-6573`), naming
  `adopt --re-adopt --write` and `--allow-ungraded` as the only escapes. Measured today: 32 rows at
  NicoCares, 30 at inCMS. The build's done-condition requires that stamp, so this unit either moves
  the count or states that it cannot.
- **S7** — MOVE it: drive the NicoCares `evidence: "unattributed"` population to ZERO, which is the
  branch S6 names and `DEPL-dRetiredFork-9` ratified. S6 only MEASURES; without this item AC6 would
  be an acceptance criterion with no scope behind it, which is the shape this build keeps finding.
  The 32 rows measured today are the before-count. inCMS is out of scope here and its half of the
  done-condition stays deferred.
## 3. Non-goals (OUT)

- **The residual-byte problem.** Whole-file equality decides a rung — one residual byte and it does
  not match, which the function's own docstring states and names `adopt-unattended.test.sh` as an
  example of. Every `nc carve-out N/20` comment is such a byte. This unit widens the needle map; it
  does not make a commented repath reconcile, and `DEPL-dRetiredFork-7` is where that is confronted.
- Composing the rungs into a lattice. The ladder is a ratified `§8 F2` decision and its cost — a
  CRLF checkout at a non-default prefix falling to three-way — is stated rather than hidden.
- Any change to the three-way merge itself.

## 4. Design

### Data model

The needle map is `{gov_path_fragment: target_path_fragment}`. Today it is keyed by DIRECTORY PAIR
and a fan-out makes the key ambiguous. After this unit, a fanned gov directory contributes no
map-level needle and each row under it resolves its own, which is the mechanism the existing drop
message already describes as the fallback — "Rows under it now resolve against their own destination
instead" — but which produces no needle for the rung proof.

### Migration

Read-only first, on both adopters, before any write. `update` is read-only by default and its
failure mode is silent data loss in a repository gov does not own, so the measurement in S4 is
mandatory and precedes `--write` on any real tree.

### Alternatives rejected

Requiring adopters to install every kit at one destination. That is a demand on trees gov does not
own, and it is contradicted by the descriptors themselves: seven gov directories legitimately fan,
because a kit ships a rendered SKILL.md beside its engine files.

## 5. Production-readiness checklist

- security — a needle is a path fragment used in a byte substitution over file content. A needle
  derived from a target-supplied path must not be able to match more than the path it names; grade
  the derived fragments and refuse a degenerate one, such as an empty string.
- perf / scale — the map is derived once per run over the receipt's own rows.
- a11y — N/A.
- i18n — the substitution decodes UTF-8 and returns the raw bytes on failure, which is existing
  behaviour and must be preserved.
- error / empty / loading states — S3. An empty map REFUSES.
- observability — the run reports rung counts by kind, so `relocate` moving from zero is visible.
- risks — a WIDER needle map means more rows take the automatic raw-write path. A wrong needle
  therefore writes gov's bytes over a target's real edit. This is the highest-severity risk in the
  build; the mitigation is that the rung is proved by whole-file equality before any write, so a row
  whose bytes are not exactly the carried form still falls to three-way.
- testing + left-shift gates — S5's three arms plus the acceptance-matrix harness.
- migration / rollback — no receipt schema change; reverting restores the drop.
- user docs — `WIRE-INTO-PROJECT.md` section 5b, which describes the rungs to operators.

## 6. Acceptance criteria

- **AC1** — When a receipt puts one gov directory at two destinations, `python
  tools/govkit/govkit.py update --target <fixture>` produces needles for those rows and reports at
  least one `relocate` rung; the pre-change run reported the directory DROPPED and no rung.
- **AC2** — When a row's destination is genuinely ambiguous, it still drops and the report names the
  ROW, not only the directory. Observed via `python tools/govkit/govkit.py update --target <fixture>`.
- **AC3** — When the needle map is empty, the run REFUSES rather than reporting every row
  unattributed. Observed via `python tools/govkit/govkit.py update --target <fixture>`.
- **AC4** — A read-only `update` against `C:/projects/nicocares/main` reports a `relocate` count
  strictly greater than zero, and that number is recorded in the acceptance ledger.
- **AC5** — `python tools/govkit/selftest.py` passes with its arm count increased by S5's three.
- **AC6** — The `evidence: "unattributed"` row count at NicoCares after this unit is ZERO, with
  the before-count recorded beside it per S6.
  At NicoCares the done-condition depends on NO escape: `DEPL-dRetiredFork-1` S7 drives the
  `evidence: "unattributed"` count to ZERO, so `tools/govkit/govkit.py:6566-6573` does not withhold
  the `gov_commit` re-stamp and the pinned argv carries neither `--allow-ungraded` nor a preceding
  `govkit adopt --re-adopt --write`. inCMS's half is DEFERRED, and when it is attempted it is
  attempted with `--allow-ungraded`, which is a stated weakening and not a quiet one.
- **AC7** — When a receipt row yields an empty or single-character needle fragment, the run
  REFUSES naming the row, observed via `python tools/govkit/govkit.py update --target <fixture>`,
  and the RED is staged before the grading is wired.
- **AC8** — `python tools/govkit/govkit.py selfcheck` exits `0`.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join`.

## 8. Open questions

- **F1 — how many of the nineteen actually move?** UNRESOLVED, and it is the unit's central fact.
  This is a `FACT-QUESTION` decided by S4's read-only run against both adopters. Liveness: the run
  must be able to report ZERO, which is a real possible answer if the residual-byte problem dominates
  — and if it does, this unit's value collapses onto `DEPL-dRetiredFork-7` and the owner should see
  that before it is built.
- **F2 — does a per-row needle change the recorded `carry` field's meaning?** The field records the
  rung, not the map. Recommendation: no schema change, and assert that in the selftest.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. `derive_carry_rung` and the DROP message were read at
  `b0108f13` and quoted rather than recalled.
- rev-2 · 2026-09-02 · folded spec-audit round 1, finding H3. The README's done-condition requires a `gov_commit`
  re-stamp, `update` withholds it while any row is unattributed, and no unit drove that population
  down — S3 here and DEPL-2 S5 only reported it. S6 measures it; AC6 requires the count to fall or
  the impossibility to be recorded.
- rev-3 · 2026-09-02 · folded spec-audit round 2, finding 22. §5's security row stated a grading obligation
  on the needle map that no scope item built and no criterion observed — on the path where a
  wrong needle writes gov's bytes over a target's real edit. S3b builds it; AC7 observes it.
- rev-4 · 2026-09-02 · `DEPL-dRetiredFork-9` resolves the done-condition fork against this spec:
  AC6 now requires ZERO at NicoCares rather than merely below-before, and S7 adds the scope item
  that drives it — the branch S6 already named. The AC6 sentence is shared verbatim with
  `DEPL-dRetiredFork-3` AC10.

## 10. Reuse audit

The seam is `derive_carry_map` / `derive_carried` / `derive_carry_rung` / `derive_carried_by_rung` in
`tools/govkit/govkit.py`, which `reuse_lookup.py` reports as a four-function family already carrying
this exact concern; this unit changes one branch inside it and adds no new function. `resolve_row_needles`
is the existing per-row overlay being promoted from fallback to resolution.

Recall terms used: `carve-out`, `install-prefix`, `KIT_REL`, `carried`, `relocate`, `rung`,
`adopter`, `divergence`, `repath`, `govkit`, `receipt`, `unattributed`, `derive`, `prefix`.
