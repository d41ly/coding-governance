# TOOL-dWellOiledMachine-112 — spec 108's ordering check is observed red: a fixture where the amendment of spec 97 lands after unit 92 builds and before unit 94

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 71 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-112-deviation-1121.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-112-deviation-1121.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-115 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-5 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md`),
finding 29, item H2, at HIGH. Item H2 also carries finding 5, closed by TOOL-dWellOiledMachine-111.

Finding 29 is the failure envelope of 108 AC21: the path its own "Red when" names, a spec-97 bump
that lands after unit 92's build commit and before unit 94's, exits 0, so on that path the criterion
certifies what it does not check. TOOL-dWellOiledMachine-111 rewrites the clause as a loop over
units 90 to 94. This unit adds to spec 108 a criterion that runs that loop, read from 108 AC21
itself, on a scratch history holding exactly that path, beside the old single call, so the defect
and its fix are observed together.

## 2. Scope (IN)

- **S1** — 108 gains its fixture. Spec 108 takes a rev bump, its §9 line naming this unit and finding
  29, whose §4 gains a `### Fixture` sub-head holding §4's script below, verbatim. Observed by AC1.
- **S2** — 108 gains AC23. The same rev bump adds to spec 108's §6: "**AC23** — When
  `sed -n '/^### Fixture/,/^### /p' <spec 108> | sed -n '/^eval/,/run unamended$/p;/run unamended$/q' | bash` runs
  from the repository root, it prints `ordered [] old 0`, `late [92] old 0` and
  `unamended [90 91 92 93 94] old 1`. fixture: a git repository in a fresh
  `abb108.XXXXXX` under `%TEMP%` directory, removed when the script exits. Red when: AC21's loop reads a
  bump landed after unit 92's build commit as ordered." Observed by AC1, AC2.
  **Readers:** by name: `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md`, the spec the criterion is added to. by value: NO VALUE READERS — spec prose no program reads.
- **S3** — 108 §5's testing line reads "AC1 to AC23", and 108 S23's "the pass runs AC1 to AC21"
  reads "the pass runs AC1 to AC23", counting TOOL-dWellOiledMachine-110's AC22. Observed by AC1.
- **S4** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 108 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. At this unit's own pass, at order 71, nothing is written: the
  pass runs AC1 to AC3 and records them. Observed by AC3.

## 3. Non-goals (OUT)

- AC21's text: finding 5, TOOL-dWellOiledMachine-111.
- No suite arm: the fixture is a probe the criterion runs, not a merge-bar suite.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-108` — §4, §5's testing line and §6, which gain the fixture and AC23 before unit 108's pass
- **consumes-from** `TOOL-dWellOiledMachine-111` — the loop in 108 AC21 that the fixture extracts and runs
- **consumes-from** `TOOL-dWellOiledMachine-98` — the predicate the fixture loads from spec 95 and runs
- **consumes-from** `TOOL-dWellOiledMachine-110` — AC22, which the AC1 to AC23 range S3 writes counts

## 4. Design

### The fixture

The script below is what S1 places in spec 108's §4. Its first line opens with `eval` and its last
ends `run unamended`, which is how AC23 cuts it out of the spec.

```bash
eval "$(sed -n '/^check_amended_before_built() {/,/^}/p' memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md)"
export LIB="$PWD/tools/unattended/lib-unattended.sh"
l=$(awk '/^- \*\*AC21\*\*/{p=1} /^- \*\*AC22\*\*/{p=0} /^## 7\./{p=0} p' memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md | tr -s '\n ' ' ' | grep -o 'for n in [^`]*done')
[ -n "$l" ] || { echo "no loop in AC21"; exit 1; }
fx=$(mktemp -d "$(cygpath -u "$TEMP")/abb108.XXXXXX"); trap 'cd /; rm -rf "$fx"' EXIT
git init -q "$fx"; cd "$fx" || exit 1
git config user.email fx@fx; git config user.name fx; git config core.autocrlf false
s=memory/builds/dWellOiledMachine/spec; mkdir -p "$s"
c() { git add -A; git commit -qm "$1"; }
echo 1 > "$s/x-TOOL-dWellOiledMachine-97.md"; c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-97"
echo 1 > "$s/x-TOOL-dWellOiledMachine-108.md"; c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-108"; git tag floor
am() { echo a >> "$s/x-TOOL-dWellOiledMachine-97.md"; c "spec(dWellOiledMachine): TOOL-dWellOiledMachine-108 amends spec 97"; }
ps() { mkdir -p tools; echo p >> "tools/x$1.py"; c "build(dWellOiledMachine): TOOL-dWellOiledMachine-$1 built"; }
run() { r=$(eval "$l" | tr '\n' ' '); check_amended_before_built 97 108 94; echo "$1 [${r% }] old $?"; }
git checkout -q -B ordered floor; am; for n in 92 91 90 93 94; do ps $n; done; run ordered
git checkout -q -B late floor; ps 92; am; for n in 91 90 93 94; do ps $n; done; run late
git checkout -q -B unamended floor; for n in 92 91 90 93 94; do ps $n; done; run unamended
```

The passes run in build order, unit 92 first, as orders 31, 56, 65, 66 and 67 put them. The loop is
read from 108 AC21 and never re-typed, so a wrong unit list or argument order there turns AC23 red.
`old` is the exit status of the single call AC21 made before TOOL-dWellOiledMachine-111: 0 on the
`late` history is the defect, printed beside the loop that catches it.

### What it does not check

- That the loop's unit list is complete: it observes the five units AC21 names, not the set of units
  spec 97 reaches. Finding 5's §4 Evidence in TOOL-dWellOiledMachine-111 derives that set.
- AC21's clauses for specs 95 and 96, which the `grep -o` leaves out.

### Evidence

- This script, run 2026-10-27 against a scratch copy of AC21 holding the loop and with the predicate
  loaded from a scratch file, printed `ordered [] old 0`, `late [92] old 0` and
  `unamended [90 91 92 93 94] old 1`, and removed its directory.
- `mktemp -d` gives each run its own directory, so two runs on one machine do not share a repository
  (finding 31's class, in TOOL-dWellOiledMachine-115).

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 108's rev cell moves)

### Alternatives rejected

- **A staged break in the live repository.** It writes commits into the run's own history.
- **A fixture that re-types the loop.** Finding 19 shows a re-typed loop cannot see a wrong list in
  the criterion it claims to test.

## 5. Production-readiness checklist

- security — N/A — a scratch repository under `%TEMP%`, removed by the script's exit trap.
- perf / scale — 19 commits and 18 predicate calls; 33 to 64 seconds on this machine,
  measured 2026-10-27.
- error / empty / loading states — `unamended` is the empty amendment population; an AC21 with no
  loop prints `no loop in AC21` and exits 1.
- observability — the bracketed lists name each unit out of order, and `old` shows the single call.
- risks — `cygpath` is Git Bash's; the repository runs there.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `grep -c "^### Fixture"`, `grep -c "^- \*\*AC23\*\*"`,
  `grep -c "testing — AC1 to AC23"` and `grep -c "the pass runs AC1 to AC23"` run over `<spec 108>`,
  each prints 1.
  Red when: spec 108 carries no red case for its ordering criterion.
- **AC2** — When `sed -n '/^### Fixture/,/^### /p' <spec 108> | sed -n '/^eval/,/run unamended$/p;/run unamended$/q' | bash`
  runs, it prints `ordered [] old 0`, `late [92] old 0` and `unamended [90 91 92 93 94] old 1`.
  fixture: a git repository in a fresh `abb108.XXXXXX` under `%TEMP%` directory, removed when the script
  exits.
  cost: about a minute.
  Red when: a bump landed after unit 92's build commit reads as ordered.
- **AC3** — When `check_amended_before_built 108 112 92` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 108 lands after unit 92's build commit.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: the fixture is a probe that 108 AC23 and this unit's AC2 run.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-5 promotions, finding
  29 (H2).

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`), loaded from spec 95, and the fixture shape of
TOOL-dWellOiledMachine-107. `build_fixture` (`tools/memory-tree/routed_commits.py:387`) builds a
scratch repository from an ordered commit list in one `git fast-import`, but it is Python inside a
kit self-test, and this fixture must run the bash predicate between commits on three branches, so it
is not used. The probe `python tools/codebase-map/reuse_lookup.py "build a scratch git repository
fixture from an ordered list of commits"` ranked name-stem hits (`git`, `build`, `scratch`,
`fixture`), none a history builder.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`
