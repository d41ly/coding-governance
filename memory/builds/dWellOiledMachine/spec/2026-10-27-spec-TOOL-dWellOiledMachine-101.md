# TOOL-dWellOiledMachine-101 — spec 95's ordering check is observed red: a fixture where an older spec-set commit names unit 90 and the amendment lands late

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 67 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-101-deviation-1011.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-101-deviation-1011.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`),
finding 29, item H1, at HIGH. Item H1 also carries findings 1, 11, 19, 12, 20, 30, 13, 21 and 31,
closed by TOOL-dWellOiledMachine-98 to -100 and -102 to -107. Finding 29 is the failure envelope of
95 AC2: "read literally, AC2 is always red; read loosely, always green", because the commit the probe
reached was an older spec-set commit naming unit 90. A replacement probe nobody has seen go red is no
better. This unit adds to spec 95 a criterion that runs TOOL-dWellOiledMachine-98's predicate on a
scratch fixture repository holding that same older commit, in three orders, so the red case is
observed and not argued.

## 2. Scope (IN)

- **S1** — 95 gains its fixture. Spec 95 takes a rev bump, its §9 line naming this unit and finding
  29, whose §4 gains a `### Fixture` sub-head holding §4's script below, verbatim. Observed by AC1.
- **S2** — 95 gains AC6. The same rev bump adds to spec 95's §6: "**AC6** — When §4's fixture script
  runs from the repository root, it prints `before 0`, `after 1` and `unbuilt 1`, and its last line is
  the subject of the fixture's first commit, which names `TOOL-dWellOiledMachine-90`. fixture: a git
  repository under `%TEMP%/abb95`, that exists only while the script runs. Red when: an amendment that follows
  unit 90's build commit, or one with no build commit after it, reads as ordered, or the older commit
  naming unit 90 is read as the amendment." Observed by AC1, AC2.
- **S3** — 95 §5's testing line reads "AC1 to AC6". Observed by AC1.
- **S4** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 95 and whose subject names this unit and neither
  TOOL-dWellOiledMachine-90 nor TOOL-dWellOiledMachine-93. At this unit's own pass, at order 67,
  nothing is written: the pass runs AC1 to AC3 and records them. Observed by AC3.

## 3. Non-goals (OUT)

- The predicate: finding 1, TOOL-dWellOiledMachine-98. 95 AC2's text: finding 19,
  TOOL-dWellOiledMachine-100. 95 S3's join naming AC6: finding 11, TOOL-dWellOiledMachine-99.
- No suite arm: the fixture is a probe the criterion runs, not a merge-bar suite.
- No fixture for specs 96 and 97: their own failure modes are findings 30 and 31.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-95` — §4, §5's testing line and §6, which gain the fixture and AC6 before unit 95's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate the fixture runs
- **hands-off** `TOOL-dWellOiledMachine-99` — AC6, which 95 S3's rewritten join names as an observer

## 4. Design

### The fixture

The script below is what S1 places in spec 95's §4. It loads the predicate from spec 95, points `LIB`
at the checkout's library, builds the fixture, runs three cases from one floor and removes it.

```bash
eval "$(sed -n '/^check_amended_before_built() {/,/^}/p' memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md)"
export LIB="$PWD/tools/unattended/lib-unattended.sh"
fx=$(cygpath -u "$TEMP")/abb95; rm -rf "$fx"; git init -q "$fx"; cd "$fx" || exit 1
git config user.email fx@fx; git config user.name fx
s=memory/builds/dWellOiledMachine/spec; mkdir -p "$s"
c() { git add -A; git commit -qm "$1"; }
echo 1 > "$s/x-TOOL-dWellOiledMachine-90.md"
c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-90"
echo 1 > "$s/x-TOOL-dWellOiledMachine-95.md"; echo 2 >> "$s/x-TOOL-dWellOiledMachine-90.md"
c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-95"; git tag floor
am() { echo "a$1" >> "$s/x-TOOL-dWellOiledMachine-90.md"; c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-95 amends spec 90"; }
ps() { mkdir -p tools; echo "p$1" >> tools/x.py; echo "s$1" >> "$s/x-TOOL-dWellOiledMachine-90.md"; c "build(dWellOiledMachine): TOOL-dWellOiledMachine-90 built"; }
git checkout -q -B before floor; am 1; ps 1; check_amended_before_built 90 95 90; echo "before $?"
git checkout -q -B after floor; ps 2; am 2; check_amended_before_built 90 95 90; echo "after $?"
git checkout -q -B unbuilt floor; am 3; check_amended_before_built 90 95 90; echo "unbuilt $?"
git log --reverse --format=%s | grep -E "TOOL-dWellOiledMachine-(90|95)([^0-9]|$)" | head -1
cd - >/dev/null; rm -rf "$fx"
```

The first commit stands in for 089c397aa: it names unit 90 and touches spec 90 before the floor. The
last line is what the old subject-order probe printed on that history, kept so the criterion shows the
defect beside its fix. The pass commit also touches spec 90, as a real pass flips its status.

### Evidence

- 95 AC2's probe printed 089c397aa over 0689e7fa..HEAD, a commit naming TOOL-dWellOiledMachine-90
  that predates any amendment (finding 29's appendix row).
- This script, run 2026-10-27 with TOOL-dWellOiledMachine-98's function loaded from a scratch file,
  printed `before 0`, `after 1`, `unbuilt 1`, then
  `spec(dWellOiledMachine): TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-90`.
- `/tmp` in this repository's Git Bash is `%TEMP%` (`cygpath -w /tmp`), and the fixture rule puts a
  repository there under a short name.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 95's rev cell moves)

### Alternatives rejected

- **A staged break in the live repository.** It writes commits into the run's own history, which
  every later history check then reads.
- **One fixture for all three specs.** Each spec's red case is a different failure mode (findings 30
  and 31), and one fixture would observe only one of them.

## 5. Production-readiness checklist

- security — N/A — a scratch repository under `%TEMP%`, removed by the script.
- perf / scale — seven commits and three predicate calls.
- error / empty / loading states — the `unbuilt` case is the empty build population.
- observability — the four printed lines.
- risks — `cygpath` is Git Bash's; the repository runs there.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `grep -c "^### Fixture"`, `grep -c "^- \*\*AC6\*\*"` and `grep -c "testing — AC1 to AC6"`
  run over `<spec 95>`, each prints 1.
  Red when: spec 95 carries no red case for its ordering criterion.
- **AC2** — When the script under spec 95's `### Fixture` runs, it prints `before 0`, `after 1`,
  `unbuilt 1` and a last line naming `TOOL-dWellOiledMachine-90`.
  fixture: a git repository under `%TEMP%/abb95`, that exists only while the script runs.
  Red when: the late or unbuilt case exits 0, or the in-order case exits 1.
- **AC3** — When `check_amended_before_built 95 101 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 95 lands after unit 90's build commit.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: the fixture is a probe that 95 AC6 and this unit's AC2 run.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  29 (H1).

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate, loaded from spec 95 exactly as the live
criteria load it, so the fixture exercises the text that ships rather than a copy. The probe
`python tools/codebase-map/reuse_lookup.py "check that a spec amendment commit landed before the
unit's build commit"` ranked `build_fixture` (shared by `tools/lib/lib-selftest.sh` and the
memory-tree joins) as the house fixture builder; it builds selftest trees for code suites, not a
history in three orders, so no existing seam fits the fixture, and the script stays a probe. The
recall query below ranked the round-4 report's "stage the red case once" line first.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
