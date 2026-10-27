# TOOL-dWellOiledMachine-104 — spec 96's ordering check is observed red: a fixture where unit 93's own pass touches spec 93 and no amendment precedes it

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 68 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-104-deviation-1041.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-104-deviation-1041.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`),
finding 30, item H1, at HIGH. Item H1 also carries findings 1, 11, 19, 29, 12, 20, 13, 21 and 31,
closed by TOOL-dWellOiledMachine-98 to -103 and -105 to -107. Finding 30 is the failure envelope of
96 AC5: its probe can never print the amendment, so it cannot tell whether the parse reached spec 93
before unit 93 built. Spec 93's history has its own trap for any replacement: unit 93's pass flips
spec 93's status, so the first commit touching spec 93 after the floor may be the pass itself. This
unit adds to spec 96 a criterion that runs TOOL-dWellOiledMachine-98's predicate on a scratch fixture
holding that trap, a prefix-matching id and both orders, so each red case is observed.

## 2. Scope (IN)

- **S1** — 96 gains its fixture. Spec 96 takes a rev bump, its §9 line naming this unit and finding
  30, whose §4 gains a `### Fixture` sub-head holding §4's script below, verbatim. Observed by AC1.
- **S2** — 96 gains AC8. The same rev bump adds to spec 96's §6: "**AC8** — When §4's fixture script
  runs from the repository root, it prints `pass-only 1`, `prefix 1`, `before 0` and `after 1`.
  fixture: a git repository under `%TEMP%/abb96`, that exists only while the script runs. Red when: unit 93's
  own pass commit, or a commit naming `TOOL-dWellOiledMachine-960`, is read as the amendment, or an
  amendment after the pass reads as ordered." Observed by AC1, AC2.
- **S3** — 96 §5's testing line reads "AC1 to AC8, and the arm S3 adds to spec 93's §7". Observed by
  AC1.
- **S4** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 96 and whose subject names this unit and not
  TOOL-dWellOiledMachine-93. At this unit's own pass, at order 68, nothing is written: the pass runs
  AC1 to AC3 and records them. Observed by AC3.

## 3. Non-goals (OUT)

- The predicate: finding 1, TOOL-dWellOiledMachine-98. 96 AC5's text: finding 20,
  TOOL-dWellOiledMachine-103. 96 S4's join naming AC8: finding 12, TOOL-dWellOiledMachine-102.
- No suite arm: the fixture is a probe the criterion runs, not a merge-bar suite.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-96` — §4, §5's testing line and §6, which gain the fixture and AC8 before unit 96's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate the fixture loads from spec 95 and runs
- **hands-off** `TOOL-dWellOiledMachine-102` — AC8, which 96 S4's rewritten join names as an observer
- **hands-off** `TOOL-dWellOiledMachine-115` — §3 Edges, §4's fixture, §5, §10 and the S2 and AC2 fixture texts, which gain the edge to unit 103, a per-run directory and `build_fixture` (round-5 promotions audit, findings 1, 18 and 31)

## 4. Design

### The fixture

The script below is what S1 places in spec 96's §4.

```bash
eval "$(sed -n '/^check_amended_before_built() {/,/^}/p' memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md)"
export LIB="$PWD/tools/unattended/lib-unattended.sh"
fx=$(cygpath -u "$TEMP")/abb96; rm -rf "$fx"; git init -q "$fx"; cd "$fx" || exit 1
git config user.email fx@fx; git config user.name fx
s=memory/builds/dWellOiledMachine/spec; mkdir -p "$s"
c() { git add -A; git commit -qm "$1"; }
echo 1 > "$s/x-TOOL-dWellOiledMachine-93.md"; c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-93"
echo 1 > "$s/x-TOOL-dWellOiledMachine-96.md"; c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-96"; git tag floor
ps() { mkdir -p tools; echo "p$1" >> tools/x.py; echo "INPROGRESS $1" >> "$s/x-TOOL-dWellOiledMachine-93.md"; c "build(dWellOiledMachine): TOOL-dWellOiledMachine-93 built"; }
am() { echo "a$1" >> "$s/x-TOOL-dWellOiledMachine-93.md"; c "spec(dWellOiledMachine): $2 amends spec 93"; }
git checkout -q -B pass-only floor; ps 1; check_amended_before_built 93 96 93; echo "pass-only $?"
git checkout -q -B prefix floor; am 2 TOOL-dWellOiledMachine-960; ps 2; check_amended_before_built 93 96 93; echo "prefix $?"
git checkout -q -B before floor; am 3 TOOL-dWellOiledMachine-96; ps 3; check_amended_before_built 93 96 93; echo "before $?"
git checkout -q -B after floor; ps 4; am 4 TOOL-dWellOiledMachine-96; check_amended_before_built 93 96 93; echo "after $?"
cd - >/dev/null; rm -rf "$fx"
```

In `pass-only` the pass commit is the first commit after the floor touching spec 93, as unit 93's
status flip would be; a predicate reading "first commit touching the spec" would call it the
amendment. In `prefix` the only earlier commit touching spec 93 names a longer id.

### Evidence

- 96 AC5's probe printed e446e9582 over 0689e7fa..HEAD (finding 30's appendix row), and
  `grep -c derive_arm_suite_path` over spec 93 printed 0 there, which makes a content anchor work for
  this spec alone (finding 31 shows it fails for spec 91).
- These four cases, run 2026-10-27 with TOOL-dWellOiledMachine-98's function loaded from a scratch
  file, printed 1, 1, 0 and 1 in that order.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-96.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 96's rev cell moves)

### Alternatives rejected

- **Spec 95's fixture reused.** Its cases do not hold a pass commit that touches the amended spec
  with no amendment before it, the trap specific to spec 93.
- **A staged break in the live repository.** It writes commits into the run's own history.

## 5. Production-readiness checklist

- security — N/A — a scratch repository under `%TEMP%`, removed by the script.
- perf / scale — ten commits and four predicate calls.
- error / empty / loading states — `pass-only` is the empty amendment population.
- observability — the four printed lines.
- risks — `cygpath` is Git Bash's; the repository runs there.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `grep -c "^### Fixture"`, `grep -c "^- \*\*AC8\*\*"` and `grep -c "testing — AC1 to AC8"`
  run over `<spec 96>`, each prints 1.
  Red when: spec 96 carries no red case for its ordering criterion.
- **AC2** — When the script under spec 96's `### Fixture` runs, it prints `pass-only 1`, `prefix 1`,
  `before 0` and `after 1`.
  fixture: a git repository under `%TEMP%/abb96`, that exists only while the script runs.
  Red when: a pass commit or a prefix-matching id is read as the amendment, or the late case exits 0.
- **AC3** — When `check_amended_before_built 96 104 93` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 96 lands after unit 93's build commit.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: the fixture is a probe that 96 AC8 and this unit's AC2 run.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  30 (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-5
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-115.

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate, loaded from spec 95 exactly as the live
criteria load it. The probe `python tools/codebase-map/reuse_lookup.py "check that a spec amendment
commit landed before the unit's build commit"` ranked `build_fixture` as the house fixture builder; it
builds selftest trees for code suites, not a history in four orders, so no existing seam fits the
fixture, and the script stays a probe. The recall query below ranked the round-4 report's "stage the
red case once" line first.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
