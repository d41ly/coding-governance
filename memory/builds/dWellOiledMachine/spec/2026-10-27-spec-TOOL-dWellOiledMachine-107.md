# TOOL-dWellOiledMachine-107 — spec 97's ordering check is observed red: a fixture where spec 91 already holds the amendment's string and one of four amendments lands late

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 69 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-107-deviation-1071.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-107-deviation-1071.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`),
finding 31, item H1, at HIGH, the skeptic's corrected fix. Item H1 also carries findings 1, 11, 19,
29, 12, 20, 30, 13 and 21, closed by TOOL-dWellOiledMachine-98 to -106. Finding 31 is the failure
envelope of 97 AC15, and its skeptic judged the finder's fix unsound: anchoring the amendment on a
content string with `git log -S` fails for spec 91, because `fixture-session` is in spec 91 since
e446e9582 and the anchor finds that commit whatever the order. 97 also covers four amended units at
once, so a check can pass three and miss the fourth. This unit adds to spec 97 a criterion that runs
TOOL-dWellOiledMachine-98's predicate, in AC15's loop, on a scratch fixture holding both traps.

## 2. Scope (IN)

- **S1** — 97 gains its fixture. Spec 97 takes a rev bump, its §9 line naming this unit and finding
  31, whose §4 gains a `### Fixture` sub-head holding §4's script below, verbatim. Observed by AC1.
- **S2** — 97 gains AC16. The same rev bump adds to spec 97's §6: "**AC16** — When §4's fixture script
  runs from the repository root, it prints `ordered []`, `late [94]` and `unamended [91 92 93 94]`,
  and its last line, the subject `git log -S fixture-session` finds for the fixture's spec 91, names
  `TOOL-dWellOiledMachine-91`. fixture: a git repository under `%TEMP%/abb97`, that exists only while
  the script runs. Red when: a content string present before this spec's own commit, or three of four
  amendments in order, reads as ordered." Observed by AC1, AC2.
- **S3** — 97 §5's testing line reads "AC1 to AC16". Observed by AC1.
- **S4** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 97 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-91 to -94. At this unit's own pass, at order 69, nothing is written: the pass
  runs AC1 to AC3 and records them. Observed by AC3.

## 3. Non-goals (OUT)

- The predicate: finding 1, TOOL-dWellOiledMachine-98. 97 AC15's text: finding 21,
  TOOL-dWellOiledMachine-106. 97 S24's join naming AC16: finding 13, TOOL-dWellOiledMachine-105.
- No suite arm: the fixture is a probe the criterion runs, not a merge-bar suite.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-97` — §4, §5's testing line and §6, which gain the fixture and AC16 before unit 97's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate the fixture loads from spec 95 and runs
- **hands-off** `TOOL-dWellOiledMachine-105` — AC16, which 97 S24's rewritten join names as an observer

## 4. Design

### The fixture

The script below is what S1 places in spec 97's §4.

```bash
eval "$(sed -n '/^check_amended_before_built() {/,/^}/p' memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md)"
export LIB="$PWD/tools/unattended/lib-unattended.sh"
fx=$(cygpath -u "$TEMP")/abb97; rm -rf "$fx"; git init -q "$fx"; cd "$fx" || exit 1
git config user.email fx@fx; git config user.name fx
s=memory/builds/dWellOiledMachine/spec; mkdir -p "$s"
c() { git add -A; git commit -qm "$1"; }
for n in 91 92 93 94; do echo "session_id: 'fixture-session'" > "$s/x-TOOL-dWellOiledMachine-$n.md"; done
c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94"
echo 1 > "$s/x-TOOL-dWellOiledMachine-97.md"; c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-97"; git tag floor
am() { for n in "$@"; do echo a >> "$s/x-TOOL-dWellOiledMachine-$n.md"; done; c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-97 amends specs $*"; }
ps() { mkdir -p tools; echo p >> "tools/x$1.py"; c "build(dWellOiledMachine): TOOL-dWellOiledMachine-$1 built"; }
loop() { r=""; for n in 91 92 93 94; do check_amended_before_built $n 97 $n || r="$r $n"; done; echo "[${r# }]"; }
git checkout -q -B ordered floor; am 91 92 93 94; for n in 92 91 93 94; do ps $n; done; echo "ordered $(loop)"
git checkout -q -B late floor; am 91 92 93; for n in 92 91 93 94; do ps $n; done; am 94; echo "late $(loop)"
git checkout -q -B unamended floor; for n in 92 91 93 94; do ps $n; done; echo "unamended $(loop)"
git log -S fixture-session --format=%s -- "$s/x-TOOL-dWellOiledMachine-91.md"
cd - >/dev/null; rm -rf "$fx"
```

The first commit stands in for e446e9582: it authors specs 91 to 94 and puts `fixture-session` in
spec 91 before the floor. The passes run in build order, unit 92 first, as orders 31, 56, 66 and 67
put them. The last line is what the content anchor the skeptic rejected finds on the `unamended`
history, kept so the criterion shows the defect beside its fix.

### Evidence

- `fixture-session` is in spec 91 at lines 51, 137 and 158, and `git log -S fixture-session` over
  0689e7fa..HEAD for spec 91 prints e446e9582 (finding 31's appendix row).
- This script's cases, run 2026-10-27 with TOOL-dWellOiledMachine-98's function loaded from a scratch
  file, gave no unit for the ordered case, 94 for the late one and all four for the unamended one,
  and the content anchor printed the first commit's subject.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-97.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 97's rev cell moves)

### Alternatives rejected

- **The finder's `-S` anchor, with `read_spec_gates` for spec 93.** Valid for that spec alone; the
  skeptic showed the scheme fails for spec 91.
- **A staged break in the live repository.** It writes commits into the run's own history.

## 5. Production-readiness checklist

- security — N/A — a scratch repository under `%TEMP%`, removed by the script.
- perf / scale — sixteen commits and twelve predicate calls.
- error / empty / loading states — `unamended` is the empty amendment population for all four.
- observability — the three bracketed lists name each unit out of order.
- risks — `cygpath` is Git Bash's; the repository runs there.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `grep -c "^### Fixture"`, `grep -c "^- \*\*AC16\*\*"` and `grep -c "testing — AC1 to AC16"`
  run over `<spec 97>`, each prints 1.
  Red when: spec 97 carries no red case for its ordering criterion.
- **AC2** — When the script under spec 97's `### Fixture` runs, it prints `ordered []`, `late [94]`,
  `unamended [91 92 93 94]` and a last line naming `TOOL-dWellOiledMachine-91`.
  fixture: a git repository under `%TEMP%/abb97`, that exists only while the script runs.
  Red when: the pre-floor string, or three amendments of four, reads as ordered.
- **AC3** — When `check_amended_before_built 97 107 94` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 97 lands after unit 94's build commit.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: the fixture is a probe that 97 AC16 and this unit's AC2 run.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  31 (H1).

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate, loaded from spec 95 exactly as the live
criteria load it, inside AC15's own loop. The probe `python tools/codebase-map/reuse_lookup.py "check
that a spec amendment commit landed before the unit's build commit"` ranked `build_fixture` as the
house fixture builder; it builds selftest trees for code suites, not a four-unit history, so no
existing seam fits the fixture, and the script stays a probe. The recall query below ranked the
round-4 report's "do not anchor A on content strings" line first.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
