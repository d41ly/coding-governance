**Serves:** research PLAY-dClosedLoop-1

# Phase 0, dispatch 234: every command run for a plant or a red test, in order

The builder's evidence for its brief (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-deviations.md`), each
command with its exit code and the line that proves it, before and after each fix. `build/` is
`memory/builds/dClosedLoop/build/`, and a file there is named by its suffix. Every id this record quotes from a
command's output is written in the `missing:` form, so the build index joins nothing; the outputs held each one bare.
Every command ran from a tree's root, with `python -B`.

## [p0-6] The bare-id predicate and the marks

The predicate is `build/…-bare-ids.py`. The fix is commit `60d041ba5`, on `4bfca2c74`.

**1. The predicate on the unfixed tree** (`4bfca2c74`): `python -B build/…-bare-ids.py`, exit 1, 25 lines, one per
citation, on 22 lines in 7 files, the plan's count. No later record added one.

| File | Lines | Citations |
|---|---|---|
| `build/…-deviations.py` | 178, 180, 181, 183, 184, 185, 189, 191, 193, 197 | 12 |
| `build/…-asbuilt.py` | 106, 107 | 2 |
| `build/…-research-exec-instruments.md` | 7, 776, 789 | 4 |
| `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md` | 24483 | 1 |
| `build/…-execution-plan-reviews-compared.md` | 170 | 1 |
| `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-plan-a.md` | 275, 277, 312 | 3 |
| `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-plan-b.md` | 202, 235 | 2 |

Its first line: `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md:24483: missing:PLAY-dTrueNorth-2`.

**2. The red test before the fix**, in a scratch clone at `4bfca2c74`: a minimal `memory/builds/dTrueNorth/README.md`
(front matter with `ids:` empty, the five slot headings), staged, then `python -B tools/memory-tree/gen_build_index.py
--write`: exit 0, `build-index: wrote 1540 artifact(s)`. The README's line 7 became `ids: missing:PLAY-dTrueNorth-1
missing:PLAY-dTrueNorth-2 missing:PLAY-dTrueNorth-3 missing:PLAY-dTrueNorth-4 missing:PLAY-dTrueNorth-5
missing:PLAY-dTrueNorth-6 missing:PLAY-dTrueNorth-7 missing:TOOL-dTrueNorth-1`: the generator joined eight ids.

**3. Each instrument mode before the fix**, on `4bfca2c74`, and **4. after it**, on `60d041ba5`:

| Command | Exit before | Exit after | Summary line, the same before and after |
|---|---|---|---|
| `build/…-deviations.py` | 0 | 0 | `baseline read, chain-build specs 0, members 0, records 0 · findings 0` |
| `build/…-deviations.py --fixture` | 0 | 0 | `chain-build specs 2, members 3, records 3 · findings 0 · fixture` |
| `… --fixture --plant clause` | 1 | 1 | `members 3, records 2 · findings 1 · fixture · plant clause` |
| `… --fixture --plant pass-revision` | 1 | 1 | `chain-build specs 3, members 4, records 3 · findings 1` |
| `… --fixture --plant amended` | 1 | 1 | `members 4, records 3 · findings 1 · fixture · plant amended` |
| `… --fixture --plant pin` | 1 | 1 | `members 3, records 3 · findings 1 · fixture · plant pin` |
| `… --fixture --plant approver` | 1 | 1 | `members 3, records 3 · findings 1 · fixture · plant approver` |
| `… --fixture --plant status` | 0 | 0 | `chain-build specs 3, members 3, records 3 · findings 0` |
| `build/…-asbuilt.py --check` | 0 | 0 | `asbuilt: findings 0` |
| `build/…-asbuilt.py --fixture` | 0 | 0 | `asbuilt: findings 0 · fixture` |
| `… --fixture --plant hand-edit` | 1 | 1 | `asbuilt: findings 1 · fixture · plant hand-edit` |
| `… --fixture --plant no-row` | 1 | 1 | `asbuilt: findings 1 · fixture · plant no-row` |
| `… --fixture --plant no-citation` | 1 | 1 | `asbuilt: findings 2 · fixture · plant no-citation` |

Every exit code and summary line is unchanged. A diff of the two full outputs differs in three finding lines only,
each naming its id in the `missing:` form after the fix: the `pass-revision`, `amended` and `pin` plants, whose ids are
fixture strings.

**5. The predicate after the fix**, on `60d041ba5`: exit 0, nothing printed.

**6. The red test after the fix**, in the same scratch clone reset onto `60d041ba5`, the same README staged, then
`gen_build_index.py --write`: exit 0, `wrote 1540 artifact(s)`. The README's line 7 stayed `ids:`, and its
build-index region carries no `ids` line: the generator joined none. The predicate there: exit 0, nothing printed.

**7. The predicate's plants**, in that clone, each line appended to the tracked
`build/2026-10-20-build-PLAY-dClosedLoop-1-recheck-brief-a.md` and the file restored after each run:

| Plant | Exit | Output |
|---|---|---|
| a bare id, the id missing:TOOL-dTrueNorth-1 written bare | 1 | one line, `…-recheck-brief-a.md:112: missing:TOOL-dTrueNorth-1` |
| the same id behind `x:` | 1 | one line, `…-recheck-brief-a.md:112: missing:TOOL-dTrueNorth-1` |
| control: the same id in the `missing:` form | 0 | nothing |

## P0.1 and P0.2

Dispatch 241's evidence for its brief (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-deviations-2.md`): the
revision record's `[builder]` section (`build/…-phase0-revision.md`), in its order, read with the owner's three answers
(ER `[phase0-answers]`), which the execution plan's `[phase-0]` now carries at `1d6a7e8fe`. Built in a `--shared` clone
of the main loop's branch at `1d6a7e8fe`, committed on `p0-deviations-2`. The old code is the three instruments'
blobs there: `deviations.py` `fea6291c4`, `asbuilt.py` `9b9542e92`, `bare-ids.py` `2e0956aa9`.

**How each plant was seen on the old code first.** Every `deviations.py` plant runs in a temporary git repository the
instrument builds (finding 10): its `.memory-tree.conf` declares the one family `FIX`, so fixture ids such as
`FIX-dTrueNorth-10` parse as spec H1s there while the tree's grammar joins none of them. The repository holds v2's
`[chain]` verbatim, a fixture `DECISIONS.md`, the base history and the plant, and ends on a prepared merge onto its
`origin/main`. The before-probe, `d241/before.py` in this session's scratch folder, builds the same repository with the
new builder and runs the old `deviations.py` in it, so the old code reads the very history the new code reads. Each
plant has its own unit, clause or row, so `--fixture` with no plant builds every population plant at once.

**Plant names.** Every name the `[builder]` section proposed is kept. Added: the report plants `kind-spec`,
`kind-build`, `kind-whole`, `kind-norun`, `stub-widens`, `stub-relaxes`, `stub-grants`, `stub-drop`, `omit-grant`,
`record-no-tier`, `record-no-reason`, `record-no-surface`, `trailer-relaxes-only`, `trailer-widens-only`,
`trailer-388-none`, `trailer-240-none`, `trailer-rung6`, `outside-packet`, `outside-product`, `range`, `record-late`,
`hand-edit` and `instrument-byte`, with the controls `--control no-arm` and `--control base-range`; and `asbuilt.py`'s
plant `baseline`. Retired, since the history plants replace them: the in-memory plants `pass-revision`, `pin` and
`status`. The fixture's base history joins every member it holds, so each green control below also proves the base.

Every command ran from a tree's root with `python -B`, the fixture's temporary folders under the session's scratch
folder. A fixture repository's shas move with the bytes of the instruments it copies, so the shas below are the final
code's.

**1. The fixture repository** (finding 10). `build/…-deviations.py --fixture`: exit 0,
`deviations: baseline 2c1af5030 read, chain-build specs 16, members 25 (10 unjoined), records 15 · refused 6 · policy
report · fixture`; each of its 16 specs parsed to its `FIX-dTrueNorth-<n>` unit through `tree_lib.parse_spec_h1`, the
members naming them. `build/…-bare-ids.py` on the final tree: exit 0, nothing printed.

**2. The pin** (row 5; finding 13; finding 7 as the owner's "List it first"). `deviations.py` holds
`BASELINE = "59ff8f2ac04a967751eae00de6856afbea66c033"`; `asbuilt.py` reads `deviations.BASELINE`.

| Command | Old code | New code |
|---|---|---|
| `--fixture --plant baseline` | exit 0, `members 1, records 6 · findings 0`: the re-pointed line moves the reference, so the loosening is no member | `--policy refuse` exit 1; `report` exit 0, first line `v2's Baseline moved from 2c1af5030 to 114153034, at v2's Baseline: line (design-revised): recorded by nobody`, then `cl-dClosedLoop-0119 moved from a9b53abc to e71a7e58 since the baseline … recorded by nobody` |
| a scratch worktree at `1d6a7e8fe`, `cl-dClosedLoop-0119` loosened (`993a73c50`) and v2's `Baseline:` re-pointed to it (`e955e8163`); `deviations.py` | exit 0, `members 0, records 0 · findings 0` | `report` exit 0 and `refuse` exit 1, each first `v2's Baseline moved from 59ff8f2ac to 993a73c50 … recorded by nobody`, then `cl-dClosedLoop-0119 moved from a9b53abc to e71a7e58 since the baseline` |
| the same worktree; `asbuilt.py --check` | exit 1, `the file differs from its render from line 5 (a hand edit): Generated by … at`: the view rendered from the re-pointed sha | exit 1, `asbuilt: findings 1 · view at 59ff8f2ac`, `v2's Baseline moved from 59ff8f2ac to 993a73c50` |
| `asbuilt.py --fixture --plant baseline` | exit 1, `asbuilt: no plant baseline` | exit 1, `asbuilt: findings 1 · view at 59ff8f2ac · fixture · plant baseline`, `v2's Baseline moved from 59ff8f2ac to 1d6a7e8fe` |

`asbuilt.py --fixture` and its plants `hand-edit`, `no-row` and `no-citation` keep their exits (0, 1, 1, 1) and finding
lines on the new code; the summary now ends `· view at <sha9>`.

**3. The pass reader** (row 3; finding 1). Under `--policy refuse`:

| Plant | Old code | New code |
|---|---|---|
| `subject-pass` | exit 0, `members 2 … findings 0` | exit 1, `FIX-dTrueNorth-10's spec changed at 6b992e074, not an ancestor of its first pass 12112e7c8, at FIX-dTrueNorth-10@rev-1 (spec-revised): recorded by nobody` |
| `pass-none` | exit 0 | exit 0, `members 6 (0 unjoined)`: the base's six, none for its unit |
| `status-flip` | exit 0 | exit 0, `members 6 (0 unjoined)` |

The probe `d241/anchor.py` imports the reader and runs it over dRenderedAnchor's seven specs: first passes
`40d657e2e`, `54344d9a7`, `a8d836483`, `6d560aed2`, `b4b79004d`, `b31803aab` and `b23697d80`, each the trailer-only
reading's; `dRenderedAnchor: 7 specs, 9 after-pass revisions that are not Status-only, 0 of them members under the
Status-and-generated exception`. The tenth after-pass revision, `9506f2d33` of unit 3, is Status-only, as dispatch
238's count also set it aside.

**4. Not an ancestor of the pass** (row 4). `--plant two-branch`: old exit 0, `members 2 … findings 0`; new `refuse`
exit 1, `FIX-dTrueNorth-13's spec changed at d2c0d25fb, not an ancestor of its first pass cce651641, at
FIX-dTrueNorth-13@rev-1 (spec-revised): recorded by nobody`.

**5. Header revisions** (row 8). `--plant header-rev`: old exit 1, `FIX-dTrueNorth-14's spec revision rev-3, after its
first pass: joins no deviation record departing from FIX-dTrueNorth-14@rev-2`; new exit 0 under both policies,
`FIX-dTrueNorth-14's spec changed at c25d652b2 … at FIX-dTrueNorth-14@rev-1 (spec-revised): joins
2026-10-21-build-FIX-dTrueNorth-14-deviation-7`.

**6. The Status-and-generated exception** (finding 2).

| Plant | Old code | New code, `refuse` |
|---|---|---|
| `gen` | exit 1, `FIX-dTrueNorth-15's spec revision rev-2, after its first pass: joins no deviation record departing from FIX-dTrueNorth-15@rev-1` | exit 0, `members 6 (0 unjoined)` |
| `status-gen` | exit 1, the same line for `FIX-dTrueNorth-16` | exit 0, `members 6 (0 unjoined)` |
| `gen-text` | exit 1, the same line for `FIX-dTrueNorth-17` | exit 1, `FIX-dTrueNorth-17's spec changed at 9333903ec, not an ancestor of its first pass 923c46271, at FIX-dTrueNorth-17@rev-1 (spec-revised): recorded by nobody` |

Over dRenderedAnchor, item 3's probe prints 0 of the 9 as members. `grep -n GEN_REGION_AWK build/…-deviations.py`:
lines 41 and 224 (docstrings), 226 `found = re.findall(r"^GEN_REGION_AWK='([^']*)'$", Path(LIB).read_text(…` and 229
(its refusal): the program is read from `tools/unattended/lib-unattended.sh` and run with awk, never copied.

**7. The ledger arm** (row 7; finding 4).

| Plant | Old code | New code |
|---|---|---|
| `quote` | exit 1, `an AMENDED acceptance line in FIX-dTrueNorth-18's spec: joins no deviation record (it names 'none')` | exit 0 under both, `members 6 (0 unjoined)` |
| `amended` | exit 0, `members 2 … findings 0` | `refuse` exit 1, `FIX-dTrueNorth-19's ledger line AC1 amended rev-3, in …-acceptance-ledger.md:6, at FIX-dTrueNorth-19@rev-2 (spec-revised): recorded by nobody` |
| `amended-joined` | exit 0 | exit 0, the same line for `FIX-dTrueNorth-20` ending `joins 2026-10-21-build-FIX-dTrueNorth-20-deviation-8` |

Every ledger line names its address as `<unit>@rev-<N-1>`. In the base, one record departing from
`FIX-dTrueNorth-1@rev-1` joins three members: the revision after the pass, the ledger line `amended rev-2` and the
hand-back.

**8. The approver arm** (row 6; findings 8 and 9 as the owner's "Rows name the ids"). Each plant moves one clause and
adds the record departing from it; the fixture `DECISIONS.md` at the fixture's `origin/main` holds rows 1, 2, 3, 5 and
6 under the fixture ids `FIX-dClosedLoop-2`, `-3`, `-4`, `-6` and `-7`. The base's control: an owner citing
`FIX-dClosedLoop-4`, whose row names `cl-dClosedLoop-0004`, passes, and so does one citing `FIX-dClosedLoop-2` for the
extra unit `FIX-dTrueNorth-99` that row names.

| Plant | Old code | New code, `refuse`; each exits 0 under `report` with the member listed |
|---|---|---|
| `approver-none` | exit 1, `… is approver '' or risk 'stricter' outside the grammar` | exit 1, `refused: …-deviation-7: it records no approver` |
| `owner-bare` | exit 0, `findings 0` | exit 1, `refused: …: its approver 'owner' names the owner and cites no decision id` |
| `owner-er` | exit 0, `findings 0` | exit 1, `refused: …: its approver 'owner, quoted at ER:189' names the owner and cites no decision id` |
| `owner-row5` | exit 0, `findings 0` | exit 1, `refused: …: its approver cites FIX-dClosedLoop-6, whose row does not name cl-dClosedLoop-0003` |
| `owner-row1-added` | exit 0, `findings 0`, the add row unread | exit 1, `refused: 2026-10-21-build-FIX-dTrueNorth-21-deviation-7: its approver cites FIX-dClosedLoop-2, whose row does not name FIX-dTrueNorth-21` |
| `owner-unknown-id` | exit 0, `findings 0` | exit 1, `refused: …: its approver cites FIX-dClosedLoop-99, which no row of memory/DECISIONS.md at origin/main holds` |
| `approver`, the green control | exit 1, `… is approved by the author, and a stricter change needs the spec writer` | exit 0, `cl-dClosedLoop-0007 moved … joins …-deviation-7`, `refused 0` |

`grep -n "PLAY-dClosedLoop" build/…-deviations.py` prints seven lines, the `**Serves:**` line and six instrument paths,
each the unit id `PLAY-dClosedLoop-1`; no fixture line matches, since the fixture's ids are `FIX-`. `grep -nE
"PLAY-dClosedLoop-([2-9]|10)\b|missing:" build/…-deviations.py`: exit 1, nothing. The instrument holds no decision id.

**9. The further arms** (findings 3 and 5; the rescope addresses).

| Plant | Old code | New code |
|---|---|---|
| `add` | exit 0, `findings 0` | `refuse` exit 1, `the rescope add of FIX-dTrueNorth-22, in memory/builds/dTrueNorth/RUN.md, at new unit FIX-dTrueNorth-22 (design-to-spec): recorded by nobody` |
| `handback` | exit 0 | `refuse` exit 1, `FIX-dTrueNorth-23's divergence hand-back in …-prompt-FIX-dTrueNorth-23-1-revision.md, at FIX-dTrueNorth-23@rev-1 (spec-to-code): recorded by nobody` |
| `audit-pin` | exit 0 | `refuse` exit 1, `FIX-dTrueNorth-24's spec changed at feddb9d58, past its audited revision rev-1 (237292ade), at FIX-dTrueNorth-24@rev-1 (spec-revised): recorded by nobody` |
| `defer` | exit 0 | exit 0, `members 6 (0 unjoined)` |
| `fix-record` | exit 0 | exit 0, `members 6 (0 unjoined)` |
| `audit-nopin` | exit 0 | exit 0, `members 6 (0 unjoined)`, `no audit pin: FIX-dTrueNorth-1, FIX-dTrueNorth-2, FIX-dTrueNorth-27` |

The base's supersede row reads `FIX-dTrueNorth-2@rev-1`, the item's header revision at the row's commit, and joins its
record.

**10. The policy** (finding 7). Every plant of items 2 to 9 ran under `--policy refuse` and again under `report`: the
red plants (`baseline`, `clause`, `subject-pass`, `two-branch`, `gen-text`, `amended`, the six approver plants, `add`,
`handback`, `audit-pin`) exit 1 under `refuse` and 0 under `report`, each listing its member; the green ones
(`pass-none`, `status-flip`, `header-rev`, `gen`, `status-gen`, `quote`, `amended-joined`, `approver`, `defer`,
`fix-record`, `audit-nopin`) exit 0 under both. `--plant clause`: `report` exit 0 and `refuse` exit 1, `cl-dClosedLoop-0008
moved from 6598846f to 6c553936 since the baseline … recorded by nobody`; the old code exited 1. `--fixture --policy
refuse`, every plant at once: exit 1, `members 25 (10 unjoined) … refused 6`; under `report`, exit 0. The old code on
the same repository: exit 1, `members 13, records 15 · findings 8`, and neither the moved baseline nor any further arm
among them.

**11. Row 9's placement.** `grep -n -- "--prepare" build/…-deviations.py`: line 7, the docstring's "Placement (P0.1
row 9): the instruments run on the prepared merge, after `push-main.sh --prepare`, so two specs written".

**12. The departures report** (P0.2; findings 6 and 12). Each run builds the fixture, renders the report, writes it
under the fixture's `memory/builds/dTrueNorth/build/` and commits it on the prepared merge, renders it again, and
runs the byte compare and the validating arm.

- `--report dTrueNorth --fixture`, every population plant: exit 0, `build run ·
  2026-10-21-build-FIX-dTrueNorth-80-departures-build.md · entries 34 · byte compare green · validating arm green`.
  Entries 1 to 3 are the marked choices (`widens`, `relaxes`, `grants`); entry 4 is the moved baseline; entries 5 to
  25 are every member of items 2 to 9, joined or `recorded by nobody`, a refused approver named on its line; then the
  three forks (a `Decided:` trailer, a §8 RESOLVED mark, a park row), the carried and added units, and two outside
  paths.
- Its head names `carries.py` `9657a5e86…`, `deviations.py` `93e7a492a…`, `asbuilt.py` `97c8f8fbf…` and `packet.py`
  `986dd43f0…`; each equals `git hash-object` of the file committed here, so `git rev-parse HEAD:<path>` at this
  commit agrees.
- Run kind: `--plant kind-spec` exit 0, `spec run · …-departures-spec.md`; `kind-build` exit 0, `build run ·
  …-departures-build.md`; `kind-whole` exit 0, `build run · …-departures-build.md`; `kind-norun` exit 2, `nothing
  measured: memory/builds/dTrueNorth/RUN.md is absent, so no live run names a base: and the report has no run kind`.

The red tests, each planted into the sources or a renderer stub:

| Plant | Exit | The line that proves it |
|---|---|---|
| `stub-widens` | 1 | `entry 4, a marked choice, comes after entry 3, a member` |
| `stub-widens --control no-arm` | 0 | `byte compare green · validating arm removed` |
| `stub-relaxes` | 1 | `entry 4, a marked choice, comes after entry 3, a member` |
| `stub-relaxes --control no-arm` | 0 | `byte compare green · validating arm removed` |
| `stub-grants` | 1 | `entry 4, a marked choice, comes after entry 3, a member` |
| `stub-grants --control no-arm` | 0 | `byte compare green · validating arm removed` |
| `stub-drop` | 1 | `the Decided: trailer of a8a4e53e8 does not appear: kept the slower path — …` |
| `record-no-tier` | 1 | `entry 2's relaxes: [the 200 ms render bound] joins …-deviation-6, which carries no **Tier:**` |
| `record-no-reason` | 1 | the same, `which carries no **Reason:**` |
| `record-no-surface` | 1 | `entry 1's widens: [the help renderer's public flags] joins no record` |
| `trailer-relaxes-only` | 1 | `the trailer of 527bbbb12 cites ER:240 and carries no widens:` |
| `trailer-widens-only` | 1 | `the trailer of 5cc6628f8 cites ER:388 and carries no relaxes:` |
| `trailer-388-none` | 1 | `the trailer of c7f1a491b cites ER:388 and its widens: is none` |
| `trailer-240-none` | 0 | `validating arm green`, the trailer listed as a fork |
| `trailer-rung6` | 0 | `validating arm green`; `entry 4 · choice · widens [none] · relaxes [the 50-line cap] joins …-deviation-7`, among the first four |
| `omit-grant` | 1 | `the Decided: trailer of 6117498c9 does not appear: took the policy table change — …` |
| `outside-packet` | 0 | `entry 15 · outside · memory/builds/dGroundRules/prompts/2026-10-21-prompt-FIX-dGroundRules-1-packet.md`; the base's `memory/LIVE.md` re-render is not listed |
| `outside-product` | 0 | `entry 15 · outside · tools/fix-unrecorded.txt`; every pass's own `--writes` path is not listed |
| `range` | 0 | the run's own packet write listed (`entry 15`); dSafePassage's path and its `Decided:` trailer, landed on `origin/main` between the base and the prepare, neither listed nor required |
| `range --control base-range` | 0 | red in what it lists: `entry 11 · fork · … Decided: their own choice — another build's fork`, required by the arm, and `entry 17 · outside · memory/builds/dSafePassage/build/2026-10-21-build-FIX-dSafePassage-1-note.md` |
| `record-late` | 1 | `the written report differs from its render from line 28: - entry 9 · member · new unit FIX-dTrueNorth-28 …` |
| `hand-edit` | 1 | `the written report differs from its render from line 18: ## Entries, reviewed` |
| `instrument-byte` | 1 | `the written report differs from its render from line 12`, the head line naming `carries.py`'s blob |

The old instrument had no report mode (`deviations.py --report dTrueNorth` at `1d6a7e8fe` prints the plain summary and
ignores the flag), so no red test of item 12 has a before.

**13. The bare-id predicate's opened mode** (finding 11). In a scratch worktree at `1d6a7e8fe` with the new
instruments, `d241/opened.py` wrote dGroundRules' README and `BACKLOG.md` with the opening script's own
`render_readme` and `render_backlog` (roster units 1 to 11, ask 12), and dTrueNorth's README, since dGroundRules'
`parents:` names it; both staged, then `gen_build_index.py --write`: exit 0, `build-index: wrote 1541 artifact(s)`.

| Command | Exit | Output |
|---|---|---|
| `bare-ids.py`, the plain mode | 1 | two lines, `memory/builds/dGroundRules/BACKLOG.md:5: missing:TOOL-dGroundRules-12` and `:9:`, the ask the opening minted: finding 11's red |
| `bare-ids.py --opened` | 0 | nothing |
| `--opened`, a bare missing:TOOL-dGroundRules-40 appended to `…-recheck-brief-a.md` | 1 | one line, `…-recheck-brief-a.md:112: missing:TOOL-dGroundRules-40` |
| `--opened`, control: roster unit missing:TOOL-dGroundRules-3 cited there | 0 | nothing |
| `--opened`, the same citation, its row removed from `roster:units` | 1 | one line, `…-recheck-brief-a.md:112: missing:TOOL-dGroundRules-3` |
| `--opened`, both files restored | 0 | nothing |

The plain mode keeps P0.6's verdicts on the new code, in this tree: a bare missing:TOOL-dTrueNorth-1 appended to
`…-recheck-brief-a.md`, exit 1 and one line; the same behind `x:`, exit 1 and one line; in its `missing:` form, exit 0
and nothing.

**14. Today's tree**, at this commit: `deviations.py` exit 0, `deviations: baseline 59ff8f2ac read, chain-build specs
0, members 0 (0 unjoined), records 0 · refused 0 · policy report`, and the same under `--policy refuse`, exit 0;
`asbuilt.py --check` exit 0, `asbuilt: findings 0 · view at 59ff8f2ac`; `bare-ids.py` exit 0 and `bare-ids.py
--opened` exit 0, nothing printed; `carries.py` exit 2; `deviations.py --report dTrueNorth` exit 2, no live RUN.md.

**15. What these runs do not show.** A moved baseline is listed first among the members; in the report the marked
choices come before it, since the validating arm requires every marked choice before every other entry. The report
lists a moved baseline in every build's report. The `range` control's red is in what it lists, since the arm checks
only that every trailer of its range appears. A hand-back whose record lands in the commit that revises the spec reads
the revised header. In a fixture, the report's `carries.py --report` and `asbuilt.py --check` blocks are the
worktree's, since the fixture holds none of their inputs.

**After the commit, the M6 checklist.** `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` over
`472249174`: exit 0, 16 classes. Four were checked by a probe:
- **A fixture that passes by finding nothing.** `d241/controls.py` builds each green control's repository and reads
  what it planted. For `pass-none`, the commit `build FIX-dTrueNorth-11, attributed to no pass` writes a product path
  and carries the trailer `none`, so the first pass is `None`. For `status-flip`, the trailer-less commit naming the
  unit writes no product path. For `header-rev`, two revisions follow the pass, one excepted and one material. For
  `gen` and `status-gen`, one revision follows the pass and is not material. For `quote`, the spec holds `AMENDED`
  twice. For `defer`, `RESCOPE` reads the `defer` row. For `fix-record`, the record is read, Goal not `DIVERGENCE:`.
  For `audit-nopin`, the audit is read with no pin.
- **A synthetic value standing in.** `check_approver` was run with the tree's own conf: it reads 195 rows of
  `memory/DECISIONS.md` at `origin/main`. An owner citing missing:PLAY-dClosedLoop-4 is refused while that row is
  absent, passes once a row naming `cl-dClosedLoop-0004` is added in memory, and is refused when it cites a row
  naming neither the clause nor the unit.
- **Readers of what changed.** packet.py reads `asbuilt.baseline_clauses`, which `asbuilt.py` keeps as an alias of
  `deviations.read_chain_clauses`. `packet.py --fixture` gives the same line at `1d6a7e8fe` and at `472249174`:
  exit 0, `byte compare green · completeness 0 findings … · pin arm 6 instruments, 0 findings`. The retired plants'
  names now appear only in frozen records of earlier runs.
- **A key that occurs twice.** Each of the nine clause ids the fixture edits occurs once in v2's `[chain]`, so the
  edit lands on the clause's own id.
