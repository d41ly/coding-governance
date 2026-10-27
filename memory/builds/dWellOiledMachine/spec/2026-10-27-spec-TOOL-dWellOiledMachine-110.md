# TOOL-dWellOiledMachine-110 — spec 108 gains AC22, which reads the S12 and S13 edits in spec 97 that no criterion observed

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 71 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-110-deviation-1101.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-110-deviation-1101.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-115 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-5 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md`),
finding 4, item H1, at HIGH. Item H1 carries finding 4 alone. Its bare-name half is finding 27's
defect, closed by TOOL-dWellOiledMachine-109.

Finding 4's own half is what AC12 never reads. 108 S12 rewrites 97 AC1's third clause, and 108 S13
adds a clause to 97 AC1 and a line to 97 §4 Evidence. AC12 reads only spec 90, so the edits to spec
97 could be skipped and AC12 would still certify them. This unit adds a criterion to spec 108 that
reads those edits in spec 97, and gives S13's §4 line an exact spelling so that criterion can find
it.

## 2. Scope (IN)

- **S1** — 108 S13 spells its line. Spec 108 takes a rev bump, its §9 line naming this unit and
  finding 4, whose S13 has 97's §4 Evidence gain the sentence "The flattened AC20 slice of spec 90,
  piped to `grep -c 'tools/memory-tree/door_fixture.py'`, printed 0 on spec 90 as committed at
  05ab0d1f8, before 97 S1's rewrite." Observed by AC1, AC2.
- **S2** — 108 gains AC22. The same rev bump adds to spec 108's §6, after AC21: "**AC22** — When
  `<AC1 of spec 97>` is piped to `grep -c "AC20"` and to
  `grep -c "grep -c 'tools/memory-tree/door_fixture.py'"`, each prints 1, and
  `awk '/^## 4\./{p=1;next} /^## 5\./{p=0} p' <spec 97> | grep -c "printed 0 on spec 90 as committed at 05ab0d1f8"`
  prints 1. Red when: S12's slice or S13's base line is missing from spec 97." Observed by AC1, AC2.
- **S3** — The joins. The same rev bump has 108 S12 read "Observed by AC12, AC22" and 108 S13 read
  "Observed by AC12, AC22". Observed by AC1.
- **S4** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 108 and whose subject names this unit and not
  TOOL-dWellOiledMachine-92. It lands before the amendments spec 108 makes are applied, so S1's
  sentence is what reaches spec 97. At this unit's own pass, at order 71, nothing is written: the
  pass runs AC1 to AC3 and records them. Observed by AC3.

## 3. Non-goals (OUT)

- AC12's bare-name greps over spec 90: finding 27, TOOL-dWellOiledMachine-109.
- S11's edits to spec 93 and their criterion: finding 32, TOOL-dWellOiledMachine-115.
- No "Observed by" parity check over every S-item. That is the report's left-shift line, a separate
  mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-108` — S12, S13 and §6, which gain the joins, the exact §4 line and AC22 before unit 108's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls
- **hands-off** `TOOL-dWellOiledMachine-112` — AC22, which 112 counts when it sets 108's criterion range to AC1 to AC23
- **hands-off** `TOOL-dWellOiledMachine-121` — S2's AC22 text and §4 Evidence, whose first count keys on `tr '\n' ' '` and whose §4 clause is flattened before its count (round-6 promotions audit, findings 5 and 20)

## 4. Design

### Evidence

- Re-run 2026-10-27 at HEAD 05ab0d1f8, 97's AC1 bullet, flattened, piped to `grep -c` prints 0 for
  `AC20`, 0 for `tools/runtime/supervise.py`, 0 for `tools/memory-tree/door_fixture.py` and 0 for
  `error-unmatch`. 97's §4 holds one line naming `door_fixture.py` and none reading "printed 0".
- 108 AC12 pipes only `<spec 90>`, and 108 S13 says "Observed by AC12" (finding 4's appendix row).
- After 108 S8, 97 AC1 spells both full paths in its `git ls-files --error-unmatch` clause as well,
  so a full-path count over 97 AC1 cannot tell S12's clause from S8's. `AC20` and the quoted
  `grep -c 'tools/memory-tree/door_fixture.py'` occur in 97 AC1 only through S12.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 108's rev cell moves)

### Alternatives rejected

- **Widen AC12 to read spec 97 too.** AC12 then observes two specs, and TOOL-dWellOiledMachine-109
  rewrites the same bullet at the same cross-read.
- **Grep 97 §4 for `door_fixture.py`.** It already counts 1 at base.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — three greps.
- error / empty / loading states — an absent §4 line or AC1 clause prints 0 and reads red.
- observability — AC22 names the two places it reads.
- risks — none beyond 108's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<X of N>` is the bullet labelled X of spec N, from its label to the next column-0 `- **` label or
heading, flattened with `tr -s '\n ' ' '`. Each command runs from the repository root; the predicate
is loaded as TOOL-dWellOiledMachine-98 §6 states.

- **AC1** — When `<AC22 of 108>` is piped to `grep -c "AC1 of spec 97"` and to
  `grep -c "printed 0 on spec 90 as committed at 05ab0d1f8"`, each prints 1; `<S13 of 108>` piped to
  the second pattern prints 1; and `<S12 of 108>` and `<S13 of 108>` piped to `grep -c "AC22"` each
  print 1.
  Red when: spec 108 has no criterion reading spec 97, or S13's line has no exact spelling.
- **AC2** — When AC22's three counts run over `git show 05ab0d1f8:<spec 97>`, they print 0, 0 and 0;
  and when they run over `<spec 97>` at this unit's pass, after spec 108's amendments of spec 97 have
  landed, they print 1, 1 and 1.
  Red when: AC22 reads green on spec 97 before S12 and S13 were applied.
- **AC3** — When `check_amended_before_built 108 110 92` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 108 lands after unit 92's build commit, the earliest build
  that spec 108's corrections reach (through 97 S20).

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-5 promotions, finding
  4 (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-6
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-121.

## 10. Reuse audit

The seams reused are spec 108's own `<X of spec N>` slice and its §6 numbering, extended by one
criterion, and TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`), loaded from spec 95 rather than copied. No new probe is
minted. The recall query below ranked this finding's own report and TOOL-aHonedRuleset-12, the open
ask for criteria greps run at base, among its first hits.

Probe: `python tools/codebase-map/reuse_lookup.py "slice one section of a spec and count a token in it"` returned
lexical neighbours only (`counts` and `slice` in two suites, `read_spec_revisions` in `design_lib.py`);
none slices a spec section for a criterion, so no existing seam fits beyond the idiom named above.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec criterion that is
green before its build made red at base" --terms "criterion green at base bare name full path grep
count flattened slice red case rewrite"`
