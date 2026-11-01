# TOOL-dScopedBuild-43 — the round-1 audit of units 40 and 41, its 11 minors batched: 7 MEDIUM and 4 LOW findings, each its own scope item

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 20 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 |
| [2026-11-01-prompt-TOOL-dScopedBuild-42-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-42-promoted-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 40 and 41
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-40-spec-audit-round1.md`)
exited CONVERGED with 12 confirmed findings. One is at HIGH, and `TOOL-dScopedBuild-42` takes it. The
other 11 are minors. BUILD-METHOD M4 batches every MEDIUM and LOW into one unit, and §4 "Why one
unit" says why these stay one. Each finding is named by report id and is its own scope item. That
includes the ids the report merged into one item (M1, L1), each of which takes that item's severity.
The minors land on units 40 and 41, so this unit repairs no one unit and builds after every unit of
the build (order 20).

| Report item | Severity | Report id | Lands on | Scope item | Built by |
|---|---|---|---|---|---|
| M6 | MEDIUM | 1 | unit 40 S4 | S1 | unit 38's ledger |
| M1 | MEDIUM | 8 | unit 40 S2, AC2 | S2 | observed only |
| M1 | MEDIUM | 15 | unit 40 S1, §4 | S3 | observed only |
| M5 | MEDIUM | 3 | unit 41 §1 | S4 | text only |
| L1 | LOW | 4 | unit 41 S1, §4, §10 | S5 | text only |
| L1 | LOW | 9 | unit 41 S19 | S6 | text only |
| L3 | LOW | 5 | unit 41 §4 Rollout | S7 | text only |
| M4 | MEDIUM | 7 | unit 41 AC14 | S8 | observed only |
| M3 | MEDIUM | 10 | unit 41 S22, §8 F3, §10 | S9 | this unit |
| M2 | MEDIUM | 11 | unit 41 S11, AC9 | S10 | this unit |
| L2 | LOW | 13 | unit 41 §4, §5 | S11 | this unit |

That is 7 MEDIUM and 4 LOW findings by raw id. Each item supersedes or completes a clause of the
unit it lands on by name, and that unit's §3 names this unit. Only S1 rules a ledger note; every
other item is observed by its own criterion or is marked NOT OBSERVED.

## 2. Scope (IN)

- **S1** — id 1. Unit 40 S4's "Observed by AC2" is superseded. Unit 38's acceptance ledger answers
  its AC2 with a note naming `TOOL-dScopedBuild-40 S2`, as unit 40 S4 rules, and AC1 here reads it.
  Observed by AC1.
- **S2** — id 8. Unit 40 S2's class, restated. Over a population of paths and its entries, no result
  `r` that differs from its path and ends `/` has an entry equal to `r` or starting with `r`. A
  result equal to its own path is out of the class. Unit 40 AC2's assertion is scoped the same way.
  This supersedes unit 40 S2's "a population of paths" wording; its other clauses stand.
  Observed by AC2.
- **S3** — id 15. Unit 40 S1's directory case, stated. A declared path ending `/` whose result is
  the path itself is the declaration's own grant and stands. `design_lib.check_guard_trips`
  (`tools/memory-tree/design_lib.py:589-598`) trips a guard under a declared directory, so the grant
  covers what lies under it. With entries `["src/lib/core/"]`, `src/lib/` reduces to `src/lib/`. With
  `["pkg/sub/core/"]`, `pkg/sub/` reduces to `pkg/sub/`. A directory with no entry under it keeps
  unit 38's reduction: with `["tools/"]`, `docs/guide/` reduces to `docs/`. Unit 40's rule is built
  as its §4 states it, and §4 "The directory rows" adds the rows its table lacks. Observed by AC2.
- **S4** — id 3. Unit 41 §1's closing sentence is superseded. Only S3 to S5, through unit 30's note
  naming `TOOL-dScopedBuild-39 S27`, S14 and S19 rule a ledger note. Every other item of unit 41 is
  observed by its own criterion or is marked NOT OBSERVED. NOT OBSERVED: a summary sentence has no
  behaviour, and unit 41 AC3 reads the three notes that exist.
- **S5** — id 4. Unit 41's `build_fixture` cites are respelled as `routed_commits.py:387`, and its §4
  Evidence range as `:387-417`, matching unit 36 S1. NOT OBSERVED: a corrected citation has no
  behaviour, and §4 Evidence pins the line.
- **S6** — id 9. Unit 41 S19's cite is respelled as `regen.py:273-274`: line 273 tests `run[0]` and
  line 274 assigns `sys.executable`. NOT OBSERVED: a corrected citation has no behaviour, and §4
  Evidence pins the lines.
- **S7** — id 5. Unit 41 §4 Rollout's earlier-builder list gains S2 beside S1, so every scope item
  sits in one bucket. NOT OBSERVED: a partition of scope items has no behaviour, and unit 41's §1
  table already names S2's builders.
- **S8** — id 7. Unit 41 AC14 is superseded by AC3. It is observed at the commit that ships, `T`,
  after the last reconcile merge, and names `T` and the origin tip `R` that merge reconciled onto.
  Its population is `git log --no-merges --format=%H f4597719..T ^R -- tools/policy/check_policy.py`,
  so another build's commits and the merge commit stay out of it. Observed by AC3.
- **S9** — id 10. The scrub-list class arm. `tools/run-gates/run-gates.gov.test.sh` gains one arm.
  It reads `BAR_SCRUBBED_KNOBS` off `.githooks/pre-push` by the driver suite's cut
  (`tools/unattended/unattended.test.sh:4337`). It reads `PM_SCRUB` off
  `tools/run-gates/post-merge.sh` from its `PM_SCRUB="` line to the first line ending `"`. It fails
  when either list reads empty, and it fails naming every hook name `PM_SCRUB` lacks. Unit 41 S22, §8
  F3 and §10 cite `TOOL-dWitnessedBar-60`, the DEFERRED record that designs this fix. Its S2's
  `GATE_REGEN_CHECK` word is unit 41 S22, and the `PM_SCRUB` half of its S4 arm is this item. §8 F2.
  Observed by AC4.
- **S10** — id 11. The driver suite's parity arm fails on an empty cut. In the
  TOOL-aFrugalTurnstile-12 AC3 arm (`tools/unattended/unattended.test.sh:4333-4348`), a hook file
  that exists and whose `BAR_SCRUBBED_KNOBS` cut reads empty prints a `FAIL` line naming the hook path
  and sets the suite red. The `SKIP` line stays only for a hook file that is absent, the case of an
  install without the push-main kit (`tools/unattended/kit.toml:42-50` ships the suite as `engine`).
  This completes unit 41 S11 and AC9. Observed by AC5.
- **S11** — id 13. The docs that describe the scrub. In `tools/run-gates/README.md`, the paragraph
  ending at `:252` names `post-merge.sh` as a second bar that scrubs `GATE_REGEN_CHECK`. The section
  "The post-merge bar" names `GATE_REGEN_CHECK` in its sentence at `:555-557` listing what post-merge
  does not honour. The comment at `tools/run-gates/run-gates.sh:1434` names post-merge beside the
  pre-push hook. Unit 41 §4 Files touched gains these two files, and its §5 user-docs bullet is
  superseded: no page under `help/` describes the scrub, and the kit README's section does.
  Observed by AC6.

## 3. Non-goals (OUT)

- The report's left-shift gates: spec-lint, spec-audit checklist and bug-class entries, one per
  item. No clause of this build names them.
- The HIGH finding, which `TOOL-dScopedBuild-42` takes.
- The rest of `TOOL-dWitnessedBar-60`: its six other knobs, its driver half and its other hook list.
  S9 lands only what this build's drift needs.
- Rewording units 38, 40 and 41 in this pass. Each item supersedes a clause by name.
- Moving any unit's order. The disposal adds this unit at order 20 and renumbers nothing.

### Edges

- **consumes-from** `TOOL-dScopedBuild-38` — AC2's acceptance-ledger answer, whose note naming `TOOL-dScopedBuild-40 S2` AC1 reads (id 1)
- **consumes-from** `TOOL-dScopedBuild-40` — S1's directory case, S2's class and S4's ledger clause, which S1 to S3 complete (ids 1, 8, 15)
- **consumes-from** `TOOL-dScopedBuild-41` — §1, §4, §5, §10, S1, S11, S19, S22, F3, AC9 and AC14, which S4 to S11 complete, and S22's `PM_SCRUB` word, which S9's arm holds (ids 3, 4, 9, 5, 7, 10, 11, 13)
- **hands-off** external — `TOOL-dWitnessedBar-60`, DEFERRED in another build: its builder extends S9's arm with its other lists rather than adding a second arm, and re-pins its S2 list and its §4 table of `PM_SCRUB`, which S9 and unit 41 S22 leave stale

## 4. Design

### Why one unit

M4 admits a second unit only where the minors split into two disjoint write sets by M6. The items
on unit 40 (S1 to S3) write nothing in this pass: unit 38's builder writes S1's note, and S2 and S3
state behaviour unit 40's rule already has. Every write is S9 to S11's, on unit 41. One write set
cannot split, so the minors are one unit.

### Evidence

- `routed_commits.py:387` holds `def build_fixture`, and `regen.py:273-274` hold the `run[0]` test
  and the `sys.executable` assignment, at `e4847a14` (S5, S6).
- `post-merge.sh:35-38`: `PM_SCRUB` spans four lines. The cut of S9 reads 23 words at `e4847a14`, and
  the one hook name it lacks is `GATE_REGEN_CHECK`. A copy whose line opens `export ` reads empty.
  PINNED on 2026-11-01 (S9).
- `git grep PM_SCRUB -- tools .githooks` matches only `post-merge.sh`, so no arm holds the list (S9).
- `unattended.test.sh:4338-4339`: an empty `$fk_hk` prints `SKIP` and sets nothing red (S10).
- `tools/run-gates/README.md:252` and `run-gates.sh:1434` credit only the pre-push hook with the
  scrub, and the section at `tools/run-gates/README.md:543` names no `GATE_REGEN_CHECK`. Each grep of
  AC6 prints 0 at `e4847a14` (S11).
- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-60.md`: Status DEFERRED,
  rev-2. Its S2 adds `GATE_REGEN_CHECK` to `PM_SCRUB`, and its S4 designs the arm in
  `run-gates.gov.test.sh` (S9).

### The directory rows

| Entries | Path | Unit 38 | After unit 40 |
|---|---|---|---|
| `src/lib/core/` | `src/lib/` | `src/` | `src/lib/` |
| `pkg/sub/core/` | `pkg/sub/` | `pkg/` | `pkg/sub/` |
| `tools/` | `docs/guide/` | `docs/` | `docs/` |

### Inventory

Minted: nothing. Two suite arms and three prose edits. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 20, after every unit, as the disposal rule places a batch that lands on several
units. Unit 41 S22 adds the knob at order 18, so S9's arm is green when it lands. `TOOL-dScopedBuild-42`
at order 19 also writes `tools/unattended/unattended.test.sh`, so BUILD-METHOD M6 sequences the two.
S1 to S3 and S8 are observed at the close; S4 to S7 correct text.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`: S9's arm
- `tools/unattended/unattended.test.sh`: S10's empty-cut branch
- `tools/run-gates/README.md`: S11's two sentences
- `tools/run-gates/run-gates.sh`: S11's comment

### Alternatives rejected

- **Fail on an absent hook too (S10).** The suite ships to adopters as `engine`, and one without the
  push-main kit has no hook, so the arm would red there on arrival.
- **Correct the citations of S4 to S7 in the specs they land on.** That is a fold, and M4 admits none.
- **One unit per minor.** M4 forbids it.

## 5. Production-readiness checklist

- security — S9 holds the landed-sha bar's scrub to the hook's, so a knob the hook denies cannot be
  inherited there again unseen.
- perf / scale — two `sed` cuts per suite run.
- error / empty / loading states — S9 and S10 turn an empty cut into a failure. AC3 reports an empty
  population as no commit editing the file, never as a pass.
- observability — S9 and S10 name the file whose cut read empty and each missing knob.
- risks — S9's cut depends on `PM_SCRUB`'s closing quote ending a line; AC4 stages the empty read.
- testing — AC1 to AC3 and AC6 by probe, AC4 and AC5 by probe and by suite arm at the close.
- migration — none.
- user docs — none under `help/`; S11 corrects the run-gates kit README.

## 6. Acceptance criteria

- **AC1** — When unit 41 AC3's `awk` read of each `**Evidences:**` block runs over
  `memory/builds/dScopedBuild/build/*.md`, piped to `grep -c`, with unit `TOOL-dScopedBuild-38` and
  note `TOOL-dScopedBuild-40 S2`, it prints at least 1.
  Red when: unit 38's ledger answers AC2 without the note. A planted journal holding the note under
  `**Evidences:** TOOL-dScopedBuild-36` prints 0.
  figure: DERIVED at observation; it prints 0 at `e4847a14`.
  permission: observed at the close, after unit 38 is built.
- **AC2** — When `python -c` calls `design_lib.derive_kit_dir` on `src/lib/` with
  `["src/lib/core/"]`, on `pkg/sub/` with `["pkg/sub/core/"]` and on `docs/guide/` with
  `["tools/"]`, it returns `src/lib/`, `pkg/sub/` and `docs/`. Over every path `git ls-files` prints,
  with `routed_commits.check_conf`'s entries, and over unit 40 AC1's pairs and these three, no result
  `r` that differs from its path and ends `/` has an entry equal to `r` or starting with `r`.
  Red when: a declared directory is narrowed, so `src/lib/` returns `src/`, or every directory
  reduces to itself, so `docs/guide/` returns `docs/guide/`.
  permission: observed at the close, after unit 40 is built.
- **AC3** — When, at the commit `T` that ships, after the last reconcile merge onto origin tip `R`,
  `git log --no-merges --format=%H f4597719..T ^R -- tools/policy/check_policy.py` runs, each sha's
  subject names a unit whose `design_lib.read_spec_writes` lists `tools/policy/check_policy.py` and
  whose §7 leg line holds `policy fixtures`. No commit whose subject names `TOOL-dScopedBuild-26`
  edits the file, by `git diff-tree --no-commit-id --name-only -r <sha>`.
  Red when: a commit edits the file under a subject naming no such unit. In a scratch clone, a merged
  branch carrying a `TOOL-xOther-1` commit that edits the file puts neither that commit nor the
  merge commit in the population.
  figure: DERIVED at the close. The population is empty at `e4847a14`, and an empty population is
  reported as no commit editing the file, never as the first half passing.
  permission: observed at the close, at the tip that ships.
- **AC4** — When `sed -n 's/^BAR_SCRUBBED_KNOBS="\([^"]*\)"$/\1/p' .githooks/pre-push` prints
  `$hk` and `sed -n '/^PM_SCRUB="/,/"$/{s/^PM_SCRUB="//;s/"$//;p;}' tools/run-gates/post-merge.sh`
  prints `$pm`, both are non-empty and every word of `$hk` is a word of `$pm`.
  Red when: `PM_SCRUB` lacks a hook knob, or its line opens `export `, so `$pm` reads empty.
  figure: DERIVED at observation; at `e4847a14` the one miss is `GATE_REGEN_CHECK`.
  permission: the arm itself is §7's first `New arm:` line, observed RED then GREEN at the close,
  after unit 41 is built.
- **AC5** — When `sed -n '/TOOL-aFrugalTurnstile-12 AC3: THE CLOSE/,/^fi$/p' tools/unattended/unattended.test.sh`
  runs, its output holds a `FAIL TOOL-aFrugalTurnstile-12 AC3` line beside `st=1` on the
  empty-cut branch, and its one `SKIP` line sits under a test that the hook file is absent. On a
  staged break, a scratch copy written by `sed 's/^BAR_SCRUBBED_KNOBS=/export &/' .githooks/pre-push`,
  the file exists and the arm's cut over it prints empty, the case that branch takes.
  Red when: an empty cut over a present hook prints `SKIP` and sets nothing red. A hook whose line
  opens `export BAR_SCRUBBED_KNOBS=` fails the arm.
  figure: DERIVED at observation; the arm holds no `FAIL` line for an empty cut at `e4847a14`.
  permission: the arm's run is §7's second `New arm:` line, observed RED then GREEN at the close.
- **AC6** — Each of three reads prints at least 1. `grep -B3 -A3 'scrubs the knob from the bar'`
  over `tools/run-gates/README.md`, piped to `grep -c post-merge`, is the first.
  `awk '/^## The post-merge bar/{f=1;next} /^## /{f=0} f'` over the same file, piped to
  `grep -c GATE_REGEN_CHECK`, is the second.
  `sed -n '/WHAT THIS DOES NOT CHECK: anything a leg/,/TOOL-aPrimedIndex-7/p' tools/run-gates/run-gates.sh`,
  a read of the comment that runs nothing, piped to `grep -c post-merge`, is the third.
  Red when: a carrier still credits only the pre-push hook with the scrub.
  figure: DERIVED at observation; each prints 0 at `e4847a14`.

## 7. Gates

`run-gates gov canary` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC4 · `PM_SCRUB` held to the hook's `BAR_SCRUBBED_KNOBS`, staged by cutting `GATE_REGEN_CHECK` out of `PM_SCRUB` and by opening its line with `export ` · `FLOOR_ASSERTIONS` raised by the arm's assertion count

New arm: tools/unattended/unattended.test.sh · covers AC5 · the parity arm's empty cut over a present hook, staged by opening the hook's line with `export ` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause.
  It lands on two units. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the precedent
  `TOOL-dWitnessedBar-91` §8 F1 set. widens: none · relaxes: none
- **F2 — Gate the scrub-list class here, or leave it to `TOOL-dWitnessedBar-60` (id 10)?** Options:
  (a) S9's arm, holding `PM_SCRUB` to the hook's `BAR_SCRUBBED_KNOBS` in `run-gates.gov.test.sh`,
  where that record designs it; (b) the same arm reading `_gknobs` too, as that record's S4 does; (c)
  keep unit 41 S22's one word and hand the class gate to that record by a `hands-off external` line.
  (c) leaves the drift class ungated while the record stays DEFERRED. (b) copies the driver suite's
  parity arm, a second place for one fact. (a) trips no veto: the suite is gov-only and is not a
  governance carrier. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the most feature-rich
  survivor after (b) loses to the one-fact rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 40 and 41, its 11
  minors: MEDIUM ids 1 3 7 8 10 11 15 and LOW ids 4 5 9 13.

## 10. Reuse audit

Each item extends the seam of the unit it lands on: unit 40's `derive_kit_dir` guard for S2 and S3,
unit 41 AC3's ledger read for S1, unit 41 AC14's population for S8, and the driver suite's
TOOL-aFrugalTurnstile-12 AC3 arm (`tools/unattended/unattended.test.sh:4333`) for S10, whose hook
cut S9 reuses. `python tools/codebase-map/reuse_lookup.py "hold every knob a caller bar scrubs to the
hook's scrubbed knob list"` ranked `read_id_list`, `declared_list`, `write_bar_green` and
`check_list`. None holds one knob list to another, so no existing seam fits beyond the arms named.

Recall terms used: `python tools/memory-recall/query.py "which arm holds post-merge's scrub list to the pre-push hook's scrubbed knobs" --terms "PM_SCRUB BAR_SCRUBBED_KNOBS parity arm post-merge pre-push scrub empty cut SKIP class gate"`
