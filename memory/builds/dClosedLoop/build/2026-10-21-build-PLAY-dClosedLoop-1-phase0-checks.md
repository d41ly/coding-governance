# Phase 0 checks: P0.7's checks and red tests on the committed opening, and AC8 on the real packet

**Serves:** research PLAY-dClosedLoop-1

P0.7 of `build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`, run by dClosedLoop's session on node d on
2026-10-21 over the opening as committed: `b50573ef4` opened the 22 builds, `738dca981` renamed each packet so its
name claims the id its Serves line lists (hygiene check 21), and `8b51c299e` reworded P0.8's rows so check 27 finds no
near match. The opening commit's parent is `8d19dd714`. Exit codes are taken unpiped.

## [checks]

| Check | Exit | The line that proves it |
|---|---|---|
| `open.py --check` | 0 | `65 files byte-compared · roster arm over 509 clauses · summary arm over 22 rows, 0 disagreements · findings 0` |
| `packet.py --check <slug>`, all 22 | 0 × 22 | no build red |
| `gen_build_index.py --check` | 0 | |
| `gen_build_index.py --check-format` | 0 | `slot contract clean (193 build README(s); heading canon BOUND on 124)`; 22 advisories that a Build-level rules slot passes its 823 B high-water under its 1800 B ceiling |
| `bash tools/memory-tree/check-memory-hygiene.sh`, whole tree | 0 | after the two fixes above; at `b50573ef4` it was 1 on check 21 (22 packets), then on check 27 (5 rows) |
| `bare-ids.py` (plain) at the opening's parent `8d19dd714` | 0 | 0 lines |
| `bare-ids.py --opened` at the tip | 0 | 0 lines |
| `gap-join.py --readmes` over the 22 opened READMEs | 0 | `owned but not in the register: none`, `builds owning nothing: none`; the v2 mode also 0 |
| `open.py --driver-builds` | 0 | nine builds, the seven of the opening plus dFurnishedOrders and dLinkedLibrary |
| `open.py --carriers --check` | 0 | |
| `carries.py` | 2 | `no spec measured, so the join reads nothing and is never green`, as expected |
| `deviations.py` | 0 | `members 0 (0 unjoined), records 0 · refused 0 · policy report`: 0 members, not merely exit 0 |
| `asbuilt.py --check` | 0 | `findings 0 · view at 59ff8f2ac` |
| `python tools/memory-tree/gotchas.py --check` | 0 | |
| `python tools/lexicon/lexicon.py` | 0 | `offenders=1211`, the pin lowered from 1219 with its row in `.lexicon.conf` |

The plain predicate at the tip prints the ids the opening minted, as the revised P0.7 expects, which is why it runs at
the parent and `--opened` runs at the tip.

## [red-tests]

Each planted in a `git clone --shared` of the branch, then restored; the script is `[instrument]` below. Its output, with
red test 5's planted id marked `missing:`, as P0.6 marks verbatim copies, so it joins no build:

````text
clone at f579121fe
parent 8d19dd714: bare-ids plain rc=0 lines=0
== 1. one-byte README edit reds open.py --check
  before rc=0
  after rc=1 :: open: check of the opening of 2026-10-21 · 65 files byte-compared · roster arm over 509 clauses · summary arm over 22 rows, 0 disagreements · findings 1
== 2. a roster missing one clause reds the every-clause-in-one-row arm
  rc=1 :: open: check of the opening of 2026-10-21 · 65 files byte-compared · roster arm over 509 clauses · summary arm over 22 rows, 2 disagreements · findings 6
== 3. a parents: typo raises
parents: dTrueNorht
  gen_build_index --check rc=1 :: build-index: memory/builds/dGroundRules/README.md: parents: names 'dTrueNorht', which is not a build folder under memory/builds/ — an edge to nothing is a typo, not a relation
== 4. a removed contract row reds --check-format
  rc=1 :: build-index: memory/project/readme-contract.txt names neither a bound nor an exempt row for `memory/builds/dGroundRules/README.md`, so a new build would escape the contract by existing
== 5. a bare chain id of an opened build planted in a record makes --opened print one line
  before rc=0 lines=0
  after rc=1 lines=1 :: memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-nodes.md:71: missing:TOOL-dGroundRules-99
== 6. a gap removed from one README's problem slot reds the gap join's README mode
  before rc=0
gap-rt-34. Closing every one is this build's goal bound.
  after rc=1 :: unowned: ['gap-tool-24']
restored: 0 dirty paths
````

A first run planted red test 1 as a byte appended at the end of the README. That byte lands after the last generated
marker, in the half `open.py` leaves to the index generator, and it stayed green under both `open.py --check` and
`gen_build_index.py --check`. The test above plants the byte in the authored half, the H1, and reds. **Not checked:** a
trailing byte after a README's last generated marker; no check reads it.

## [ac8]

In a scratch clone at `8b51c299e`: `handoff.py render --role gov-spec-writer --build dTrueNorth --unit
TOOL-dTrueNorth-1 --input prompt=<dTrueNorth's packet> --input spec=<the packet>` exits 0 and writes
`prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-1-spec-writer.md`, carrying `brief:goal`, `brief:items`,
`brief:acceptance`, `brief:gates` and `brief:non-goals`; `handoff.py check` on it exits 0. The render was made in the
clone because `--out` admits only the build's own `prompts/`, and the opening writes no handoff.

## [answers-2]

The owner's opening-read answers (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md` `[phase0-answers-2]`) re-rendered
the opening at `bcc221781`: nine driver-changing builds, `PLAY-dClosedLoop-18` and `-19` minted for dFurnishedOrders and
dLinkedLibrary after `-11` to `-17`, and the gap join's README mode, answer 5, which red test 6 above sees red on a
planted orphan. Every check of `[checks]` was re-run at `f579121fe` with the results it states. One finding on the
way: the instruments refused the open instruments record while its new section was titled "The owner's opening-read
answers", because the atlas parser they share reads a decision-shaped title in an instruments record as misfiled;
hygiene did not catch it. The section was retitled at `f579121fe`.

## [summary]

`open.py --summary` at `f579121fe`, after the owner's opening-read answers re-rendered the opening, for the owner's read of
the other 21 builds:

````text
open: summary of the 22 chain builds, read from the files the opening wrote, opened 2026-10-21
| Build | Stage | `parents:` | Units | Family · `streams:` | Carry-forward ask | Packet | `may:` line | `spec-audit:` | Rule 8 · clean-reading ask | Contract row |
|---|---|---|---|---|---|---|---|---|---|---|
| dTrueNorth | Fidelity | dClosedLoop | 7 | TOOL · tooling | none: whole run | 19407 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 PLAY-dClosedLoop-2 | 2026-10-21 | yes · PLAY-dClosedLoop-11 | present, bound |
| dGroundRules | Policy | dTrueNorth | 11 | TOOL · tooling | TOOL-dGroundRules-12 | 31599 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dSafePassage | Supersession | dGroundRules | 13 | TOOL · tooling | TOOL-dSafePassage-14 | 31648 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dOrderedCharter | Foundation | dSafePassage | 37 | PLAY · playbook | PLAY-dOrderedCharter-38 | 68382 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | yes · PLAY-dClosedLoop-12 | present, bound |
| dFairHearing | Review harness | dSafePassage | 18 | TOOL · tooling | TOOL-dFairHearing-19 | 30347 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dDeclaredLoop | Spine | dOrderedCharter dFairHearing | 34 | TOOL · tooling | TOOL-dDeclaredLoop-35 | 58727 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | yes · PLAY-dClosedLoop-13 | present, bound |
| dPlacedRequest | Entry | dDeclaredLoop | 21 | TOOL · tooling | TOOL-dPlacedRequest-22 | 43562 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | yes · PLAY-dClosedLoop-14 | present, bound |
| dKeptSession | Session | dDeclaredLoop dPlacedRequest | 28 | KICK · kickoff | KICK-dKeptSession-29 | 37153 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dBoundRoles | Roles | dDeclaredLoop dWitnessedBar dPlacedRequest | 26 | TOOL · tooling | TOOL-dBoundRoles-27 | 44575 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dFurnishedOrders | Orders | dBoundRoles | 20 | TOOL · tooling | TOOL-dFurnishedOrders-21 | 33433 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | yes · PLAY-dClosedLoop-18 | present, bound |
| dTotalRecall | Memory | dDeclaredLoop dWitnessedBar dPlacedRequest | 26 | TOOL · tooling | TOOL-dTotalRecall-27 | 46936 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dLinkedLibrary | Library | dTotalRecall | 25 | TOOL · tooling | TOOL-dLinkedLibrary-26 | 40272 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | yes · PLAY-dClosedLoop-19 | present, bound |
| dMindYourWords | Lexicon | dWellOiledMachine dWitnessedBar dLinkedLibrary dFurnishedOrders | 17 | TOOL · tooling | TOOL-dMindYourWords-18 | 28255 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dWellOiledMachine | Runtime | dBoundRoles dTotalRecall dKeptSession | 61 | TOOL · tooling | TOOL-dWellOiledMachine-62 | 111449 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | yes · PLAY-dClosedLoop-15 | present, bound |
| dWitnessedBar | Test | dDeclaredLoop | 30 | TOOL · tooling | TOOL-dWitnessedBar-31 | 44417 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | yes · PLAY-dClosedLoop-16 | present, bound |
| dRankedPlan | Plan | dDeclaredLoop dTotalRecall dBoundRoles | 16 | TOOL · tooling | TOOL-dRankedPlan-17 | 25324 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dIndexedDesign | Design | dDeclaredLoop dTotalRecall dKeptSession dBoundRoles dLinkedLibrary | 16 | TOOL · tooling | TOOL-dIndexedDesign-17 | 30262 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dScopedBuild | Build | dIndexedDesign dWitnessedBar dWellOiledMachine dFurnishedOrders | 15 | TOOL · tooling | TOOL-dScopedBuild-16 | 26871 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dShippedRelease | Deploy | dWitnessedBar dTotalRecall dBoundRoles dWellOiledMachine dLinkedLibrary dFurnishedOrders | 31 | DEPL · deployer | DEPL-dShippedRelease-32 | 52209 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dTendedCadence | Maintain | dWitnessedBar dRankedPlan dWellOiledMachine dIndexedDesign dFurnishedOrders | 18 | TOOL · tooling | TOOL-dTendedCadence-19 | 32108 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dCalibratedLens | Review | dTendedCadence dFairHearing | 17 | TOOL · tooling | TOOL-dCalibratedLens-18 | 27898 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | no | present, bound |
| dConvergedCharter | Convergence | dScopedBuild dShippedRelease dCalibratedLens dMindYourWords | 23 | PLAY · playbook | PLAY-dConvergedCharter-24 | 35203 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-21 | yes · PLAY-dClosedLoop-17 | present, bound |
````

## [bar]

The full bar, `bash tools/run-gates/run-gates.sh`, on the quiescent tree at `5a891e8d8`, 2026-10-21: exit 1, one leg
red. The leg is spec tokens' size arm: the unit spec's H1 took the form a unit's H1 takes in rev-2, so the build index
binds every record that serves it into the spec's `gen:spec-records` region, and the spec passes the 49152-byte
ceiling. The escape is a row in `tools/template-size-highwater.txt`, a routed product path Phase 0 does not write, so
it is raised with the owner. The four skips are leg guards, unchanged against main. The bar's summary lines:

````text
---- chunk records: green  (4 ran, 0 failed, 0 skipped, 0 reused, 0 held)
---- chunk product: green  (19 ran, 0 failed, 0 skipped, 0 reused, 0 held)
---- chunk selftests: skipped  (0 ran, 0 failed, 0 skipped, 0 reused, 68 held)
GATE skip  kit/dogfood doc parity  (unchanged vs main)
GATE skip  codebase-map gate coverage  (unchanged vs main)
GATE skip  transition-audit arms  (unchanged vs main)
GATE skip  govkit refusal join  (unchanged vs main)
GATE FAIL  spec tokens (a spec's own names resolve)  (exit 1)
---- chunk declarations: RED  (33 ran, 1 failed, 4 skipped, 0 reused, 0 held)
---- chunk wiring: green  (11 ran, 0 failed, 0 skipped, 0 reused, 1 held)
---- chunk e2e: skipped  (0 ran, 0 failed, 0 skipped, 0 reused, 2 held)
gates RED — 1/67 legs failed (4 skipped) (71 held: subject kit or chunk selftests, GATE_SELFTESTS=1 runs them)
spec-tokens: memory/builds/dClosedLoop/spec/2026-10-20-spec-PLAY-dClosedLoop-1.md [size] `size <- memory/builds/dClosedLoop/spec/2026-10-20-spec-PLAY-dClosedLoop-1.md` — 117455 bytes, 68303 over the spec ceiling 49152; split the spec or move history out of it
````

## [instrument]

`redtests.sh <worktree> <scratch dir> <opening's parent>`, verbatim:

````bash
#!/usr/bin/env bash
# P0.7's red tests on the committed opening, each planted in a scratch clone, then restored.
# usage: redtests.sh <worktree> <scratch dir>
set -u
W=$1; S=$2
D=memory/builds/dClosedLoop/build
OPEN=$D/2026-10-20-build-PLAY-dClosedLoop-1-open.py
BARE=$D/2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py
rm -rf "$S/clone" && git clone -q --shared "$W" "$S/clone" && cd "$S/clone" || exit 9
echo "clone at $(git rev-parse --short=9 HEAD)"
# the plain predicate at the opening commit's parent
git checkout -q "${3:-HEAD^}" && { python "$BARE" > "$S/parent.txt" 2>&1; echo "parent $(git rev-parse --short=9 HEAD): bare-ids plain rc=$? lines=$(grep -c . "$S/parent.txt")"; }
git checkout -q -
step() { echo "== $1"; }
restore() { git checkout -q -- . ; git clean -qfd memory/ >/dev/null; }
R=memory/builds/dGroundRules/README.md

step "1. one-byte README edit reds open.py --check"
python "$OPEN" --check >/dev/null 2>&1; echo "  before rc=$?"
sed -i "0,/^# dGroundRules/s//# dGroundRulez/" "$R"; python "$OPEN" --check > "$S/r1.txt" 2>&1; echo "  after rc=$? :: $(grep -m1 -i 'differ\|red\|FAIL\|stale' "$S/r1.txt")"; restore

step "2. a roster missing one clause reds the every-clause-in-one-row arm"
ln=$(grep -n '^| .*cl-dClosedLoop-' "$R" | head -1 | cut -d: -f1)
sed -i "${ln}d" "$R"; python "$OPEN" --check > "$S/r2.txt" 2>&1; echo "  rc=$? :: $(grep -m1 -i 'clause' "$S/r2.txt")"; restore

step "3. a parents: typo raises"
sed -i 's/^parents: dTrueNorth/parents: dTrueNorht/' "$R"; grep -m1 '^parents:' "$R"
python tools/memory-tree/gen_build_index.py --check > "$S/r3.txt" 2>&1; echo "  gen_build_index --check rc=$? :: $(grep -m1 -i 'parent' "$S/r3.txt")"; restore

step "4. a removed contract row reds --check-format"
C=memory/project/readme-contract.txt
row=$(grep -n 'dGroundRules' "$C" | head -1 | cut -d: -f1); sed -i "${row}d" "$C"
python tools/memory-tree/gen_build_index.py --check-format > "$S/r4.txt" 2>&1; echo "  rc=$? :: $(grep -m1 -i 'dGroundRules' "$S/r4.txt")"; restore

step "5. a bare chain id of an opened build planted in a record makes --opened print one line"
python "$BARE" --opened > "$S/r5a.txt" 2>&1; echo "  before rc=$? lines=$(grep -c . "$S/r5a.txt")"
P=$D/2026-10-20-build-PLAY-dClosedLoop-1-phase0-nodes.md
PLANT="TOOL-dGround""Rules-99"   # composed, so this script's own source joins no build
printf '\nA planted citation: %s.\n' "$PLANT" >> "$P"; git add "$P"
python "$BARE" --opened > "$S/r5.txt" 2>&1; echo "  after rc=$? lines=$(grep -c . "$S/r5.txt") :: $(head -1 "$S/r5.txt")"
git reset -q; restore

step "6. a gap removed from one README's problem slot reds the gap join's README mode"
GJ=$D/2026-10-19-build-PLAY-dClosedLoop-1-gap-join.py
REG=$D/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md
V2=$D/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
python "$GJ" --readmes "$REG" "$V2" memory/builds > "$S/r6a.txt" 2>&1; echo "  before rc=$?"
sed -i 's/^gap-tool-24, gap-rt-34\./gap-rt-34./' "$R"; grep -m1 '^gap-rt-34' "$R"
python "$GJ" --readmes "$REG" "$V2" memory/builds > "$S/r6.txt" 2>&1; echo "  after rc=$? :: $(grep -m1 -i 'gap-tool-24\|orphan\|not owned' "$S/r6.txt")"; restore
echo "restored: $(git status --short | wc -l) dirty paths"
````
