# TOOL-dWitnessedBar-71 — AC5's hostile git config reaches the fixture `git init` as command-scope environment config, which S6's isolation cannot mask, and the arm proves it is in effect before grading

**Status:** INPROGRESS · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 40 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-build-TOOL-dWitnessedBar-71-deviation-711.md](../build/2026-10-25-build-TOOL-dWitnessedBar-71-deviation-711.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-71-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-71-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-71-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-71-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-71-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-71-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 66 and 67
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md`)
confirmed finding **id 11 at HIGH**, report item **H2**. No other id shares that item. Report item
M1 describes the same defect at MEDIUM under ids 3, 18 and 21, which `TOOL-dWitnessedBar-73` takes.

`TOOL-dWitnessedBar-67` S6 landed in `e1d569fc9`. Its block of section `2o` runs every git call with
`GIT_CONFIG_NOSYSTEM=1` and `GIT_CONFIG_GLOBAL` naming an empty scratch file, exported at
`tools/lib/resolve-python.test.sh@d31bef20:1537` and unset at `tools/lib/resolve-python.test.sh@d31bef20:1628`.
Unit 67 AC5 names a hostile config, `init.defaultBranch=main` and `init.defaultRefFormat=reftable`,
exported as `GIT_CONFIG_GLOBAL`. The suite plants none. Unit 67's builder exported that file around a
cut of the block (`memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-67-1-acceptance-ledger.md`,
beside AC5), and S6's export replaces it before the fixture `git init` runs. So git's built-in
defaults apply, and the staged break "dropping `--ref-format=files`" cannot turn AC5 red. That
builder left the red to this unit.

This unit keeps S6's isolation for what it is for, shielding the fixtures from the machine's own
config, and plants the hostile config at a scope the isolation does not touch. The arm then proves
the plant is in effect before it grades a fixture. It repairs `TOOL-dWitnessedBar-67`, CLOSED, and
builds one step after it (order 40).

## 2. Scope (IN)

- **S1** — The plant. Section `2o` of `tools/lib/resolve-python.test.sh` gains one function,
  `run_planted_git`, defined once inside S6's block above the corrupt-HEAD loop. It runs one `git`
  call with five command-prefix assignments: `GIT_CONFIG_COUNT=2`,
  `GIT_CONFIG_KEY_0=init.defaultRefFormat`, `GIT_CONFIG_VALUE_0=reftable`,
  `GIT_CONFIG_KEY_1=init.defaultBranch` and `GIT_CONFIG_VALUE_1=main` (§8 F3). S2's proof and S3's
  two fixture builders run their `git init` through it, and no other call does. A prefix assignment
  lives for its one command, so the suite's environment after each call, including any
  `GIT_CONFIG_COUNT` its caller set, is untouched. Unit 67 S6's export stays in force around it.
  In the same edit the corrupt-HEAD block's unit-64 header, which reads "Four fresh `git init`s ...
  each seed exits 1" above a loop building five fixtures (`TOOL-dWitnessedBar-67` S13 added `chain`),
  is corrected to open "Five fresh `git init`s" and to say the four broken ones exit 1 and `chain`
  arms. Observed by AC1, AC3 and AC4.
- **S2** — The plant is proven in effect before any fixture is graded. Inside S6's block and before
  the corrupt-HEAD loop, the arm runs `run_planted_git init -q` in a scratch directory under `$LL`
  and asserts that `git rev-parse --show-ref-format` prints `reftable` and `git symbolic-ref HEAD`
  prints `refs/heads/main`. Otherwise it fails with
  `resolve-python: the hostile git config is not in effect`, and S3's ref-format assertions do not
  run, so no fixture of AC5 is graded with no plant in effect. The arm's comment states what it does
  not check: a config scope other than command scope, and a git without `--show-ref-format`, which
  fails the proof rather than passing. Observed by AC1 and AC2.
- **S3** — AC5 is graded under S1, and its staged break reaches the fixture. Section `2o` has two
  config-proof builders, the corrupt-HEAD loop's (five fixtures) and the `child` fixture's
  (DERIVED by `grep -n -- '--ref-format=files "\$LL' tools/lib/resolve-python.test.sh`, two lines,
  PINNED 2026-11-21). Each runs as `run_planted_git -c init.defaultBranch=master init -q --ref-format=files`,
  and each fixture prints `files` and `refs/heads/master`. The loop's `67 AC5` assertion grades the
  five, and the `child` fixture gains the same `--show-ref-format` assertion naming `child`. In a
  scratch copy whose builder lacks `--ref-format=files`, the arm fails naming the fixture and
  `reftable`. Observed by AC3.

## 3. Non-goals (OUT)

- Unit 67 S6's isolation. It stays, and it still covers every git call of its block.
- The two branch defences' own staged reds, the `-c init.defaultBranch=master` flag and the branch
  file read from `git symbolic-ref HEAD`. They are `TOOL-dWitnessedBar-73` S1 and S2, for ids 3 and 18.
- The report's left-shift text, a staged-red record that refuses an entry with no captured failing
  output. No clause of this build names that gate. S2's in-effect proof is the regression this unit
  builds.
- The plain `git init -q` fixtures of section `2o` outside S6's block, unit 61's unborn fixture and
  the fixtures of units 63 and 65. No config-proof builder makes them, so they are outside S3's
  population.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-67` — S6's isolation of section `2l` and AC5's config-proof fixtures, whose hostile plant this unit moves to a scope the isolation cannot mask (id 11)
- **hands-off** `TOOL-dWitnessedBar-73` — the branch defences' staged reds and the AC5 ledger line naming which config scope wins, under S1's plant (ids 3, 18, 21, report item M1)
- **hands-off** `TOOL-dWitnessedBar-78` — one `refs/heads/master` assertion per fixture in section `2l`, and the ledger lines for AC1 and AC3 (ids 7 and 14 of the round-1 spec audit of units 68 to 73)

The three bullets above are carried byte-identical, so their `2l` names section `2o` as the
resolver suite numbers it at HEAD.

## 4. Design

### Evidence

Probed on git 2.54.0.windows.1 on 2026-11-21 (PINNED), in fixture repositories under the
session's scratch directory, with `GIT_CONFIG_NOSYSTEM=1` and `GIT_CONFIG_GLOBAL` naming an empty
file exported:

| environment beside the isolation | `git init` form | `--show-ref-format` | `symbolic-ref HEAD` |
|---|---|---|---|
| S1's five variables | plain `git init -q` | `reftable` | `refs/heads/main` |
| S1's five variables | `-c init.defaultBranch=master init -q --ref-format=files` | `files` | `refs/heads/master` |
| S1's five variables | `-c init.defaultBranch=master init -q` | `reftable` | `refs/heads/master` |
| S1's five variables | `init -q --ref-format=files` | `files` | `refs/heads/main` |

So the `GIT_CONFIG_COUNT` plant reaches an isolated `git init`, a `-c` flag outranks it, and dropping
either fixture flag changes what the fixture holds. The masking reproduces: with the hostile file
exported as `GIT_CONFIG_GLOBAL`, an inner `GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=<empty> git init`
gave `files` and `refs/heads/master`.

- A function holding the five assignments as a prefix of its `git` call planted `reftable` and
  `refs/heads/main`, and `GIT_CONFIG_COUNT` read unset in the calling shell after it. Called under a
  caller's `GIT_CONFIG_COUNT=1` naming `core.autocrlf`, the caller's count and key read back unchanged.
- `bad` and `ok` (`tools/lib/resolve-python.test.sh#bad`) set `st` and `n` in the shell that calls
  them. The corrupt-HEAD loop builds and grades each fixture in one pass, so a subshell holding its
  build would lose the grading's failures (§8 F3).
- Unit 67 S6's third bullet cites `tools/check-wiring.test.sh@248c8263:1987`, which exports
  `GIT_CONFIG_GLOBAL="$D/.git/fixture-global" GIT_CONFIG_NOSYSTEM=1`, the line
  `tools/check-wiring.test.sh@d31bef20:1987` still holds.
- `init.defaultRefFormat`, `--ref-format` and `--show-ref-format` need git 2.45 or later. A git without
  them fails S2's assertion loudly rather than passing AC5.

### Inventory

Minted: the function `run_planted_git` (cell `sh.function`, which
`python tools/lexicon/lexicon.py --suggest run_planted_git --as sh.function` grades OK under the
declared verb `run`) and the failure line of S2. No constant, flag or file.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 40, after `TOOL-dWitnessedBar-67` (39, CLOSED) and `TOOL-dWitnessedBar-70`
(39). Order 40 is shared with `TOOL-dWitnessedBar-72`, `TOOL-dWitnessedBar-74` and
`TOOL-dWitnessedBar-75`, each writing `tools/run-gates/run-gates.gov.test.sh`, which this unit
neither writes nor reads. A sibling that grows its suite widens its own row of
`memory/project/shell-role.txt`, a different line from this unit's. `TOOL-dWitnessedBar-73` (41)
grades the branch defences under S1's plant.

### Files touched (estimate)

The resolver suite grows past its `memory/project/shell-role.txt` row, so the pass widens it as
`TOOL-dWitnessedBar-51` S1 states, its widen record declared through `--dispatch`, as unit 67 did.

- `tools/lib/resolve-python.test.sh`
- `memory/project/shell-role.txt`

### Alternatives rejected

- **Drop S6's third bullet so AC5's exported `GIT_CONFIG_GLOBAL` reaches the fixtures.** The fixtures
  then read the developer's own global config wherever AC5 does not export one, which is the leak the
  isolation exists to stop.
- **Say in S6 that the fixture `git init` inherits the caller's `GIT_CONFIG_GLOBAL`.** It splits one
  block's git calls into two config regimes that a later edit can cross silently.
- **Plant the hostile defaults in a repository's own `.git/config`.** `init.*` defaults are read before
  `git init` creates that file, so they never apply.

## 5. Production-readiness checklist

- security — no new write path. The plant lives only in the one `git` call `run_planted_git` makes.
- perf / scale — one extra `git init` per run for S2, and one `--show-ref-format` read for `child`.
- error / empty / loading states — S2 turns a git too old for `reftable`, or a plant that no longer
  reaches `git init`, into a named failure rather than a vacuous pass.
- observability — S2's line names the cause before any fixture assertion runs.
- risks — git's command-scope environment config is documented and stable since git 2.31.
- testing — AC1 and AC2 by probe, AC3 by scratch copy, AC4 by grep. The arm under §7 at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe runs `run_planted_git init -q` beside `GIT_CONFIG_NOSYSTEM=1` and an empty
  `GIT_CONFIG_GLOBAL`, `git rev-parse --show-ref-format` prints `reftable` and
  `git symbolic-ref HEAD` prints `refs/heads/main`. `grep -n 'GIT_CONFIG_COUNT=2' tools/lib/resolve-python.test.sh`
  prints one line, `run_planted_git`'s definition, inside section `2o`.
  Red when: the hostile config is planted through `GIT_CONFIG_GLOBAL`, which the isolation masks.
  fixture: a scratch repository under `%TEMP%/<short-name>`.
  figure: the two values are PINNED, measured on git 2.54.0.windows.1 on 2026-11-21.
- **AC2** — When section `2o` runs from a scratch copy with the five assignments deleted from
  `run_planted_git`, it prints `resolve-python: the hostile git config is not in effect` and grades no
  fixture of AC5.
  Red when: the arm grades the fixtures with no hostile config in effect.
- **AC3** — When section `2o` builds its config-proof fixtures under S1, the corrupt-HEAD loop's five
  and `child` each print `files` for `git rev-parse --show-ref-format`. Against a scratch copy with
  `--ref-format=files` deleted from either builder, the arm fails naming the fixture and `reftable`.
  Red when: the staged break leaves AC5 green, so the flag is certified with nothing observing it.
- **AC4** — When `grep -n 'Four fresh' tools/lib/resolve-python.test.sh` runs, it prints nothing, and
  `grep -n 'Five fresh' tools/lib/resolve-python.test.sh` prints the corrupt-HEAD block's header line.
  Red when: the header counts four fixtures above a loop of five, one of which arms.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `memory hygiene`

The resolver leg runs `tools/lib/resolve-python.test.sh`. Its subject is `kit` in
`tools/gate-legs.json`, so it is held (`tools/run-gates/run-gates.sh@d31bef20:3120`) unless the main
loop sets GATE_SELFTESTS at the close, which `SELFTESTS_OWED_PATHS="tools/"`
(`.unattended.conf@d31bef20:40`) makes it do. `portability (shell lines only shrink)` and the two
recall legs read the widened `memory/project/shell-role.txt` row. The other legs guarding `tools/lib/`
are not named: the spec-tokens guards join excludes that path as broad.

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 · section `2o`'s command-scope hostile plant through `run_planted_git` and its in-effect proof, staged red by deleting `run_planted_git`'s five assignments (reaches S2's line) and by deleting `--ref-format=files` from either config-proof builder (reaches the fixture's ref store) · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 67 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which layer does AC5 grade (id 11)?** Options: (a) the fixture `git init` under a
  command-scope plant the isolation cannot mask, with the isolation kept; (b) drop S6's third bullet;
  (c) narrow S6's isolation to the seed's probe calls. (b) lets the developer's global config reach
  the fixtures, which unit 67 AC5's Red-when, a fixture that inherits outer config, names as the
  failure; veto 1 discards it. (c) leaves the fixture `git init` reading `GIT_CONFIG_GLOBAL`, so the
  same leak returns wherever AC5 exports nothing; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the one survivor and the report's corrected fix for ids 18 and 21.
  widens: none · relaxes: none
- **F3 — Which shell scope carries S1's plant over the landed loop (forced by the re-ground)?** Rev-2
  exported the five variables in a subshell that builds the fixtures. Unit 67 landed a loop that
  builds and grades each fixture in one pass, and a child block that does the same, through `bad`
  and `ok`, which set `st` and `n` in the calling shell. Options: (a) one function,
  `run_planted_git`, prefixing the five assignments to each config-proof `git init` and S2's;
  (b) split each block into a subshell that builds every fixture and a parent pass that grades them;
  (c) export the five for the block and unset them after, as S6 does. (c) drops a caller's
  `GIT_CONFIG_COUNT` and its pairs, which S1 keeps untouched; veto 1 discards it. (a) and (b) each
  meet AC1 to AC3. RESOLVED (agent, 2026-11-21, delegated): (a), on the tie-break. (b) leaves open
  how a build failure inside the subshell reaches `st`, and (a) reuses the per-command prefix form of
  `tools/unattended/unattended.test.sh@d31bef20:1457` and the shape of the suite's own
  `run_down_git` wrapper (`tools/lib/resolve-python.test.sh#run_down_git`).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 66 and 67, id 11
  (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-78, promoted by the round-1 spec audit of units 68 to 73; nothing else
  moved.
- rev-3 · 2026-11-21 · §1 to §10 · S1 to S3 · AC1 to AC4 · re-grounded over unit 67 as landed
  (`e1d569fc9`), per 2026-11-19-prompt-TOOL-dWitnessedBar-71-reground-brief: section `2l` reads `2o`
  outside the carried Edges bullets; the suite plants no hostile config, so S1 adds one; S1's
  subshell becomes `run_planted_git` (§8 F3); S3 names the `child` builder beside the loop's; S1
  corrects the unit-64 header and AC4 observes it; Files touched and the leg line gain
  `memory/project/shell-role.txt` and its readers; citations move to `path#symbol` or blob-pinned lines.

## 10. Reuse audit

The seam is section `2o` of `tools/lib/resolve-python.test.sh` as units 64 and 67 built it. S6's
isolation (`tools/lib/resolve-python.test.sh@d31bef20:1537`) stays unchanged, in the form
`tools/check-wiring.test.sh@d31bef20:1987` already writes. S1 extends the command-scope form
`tools/check-wiring.test.sh@d31bef20:38` uses to pin `core.autocrlf`
(`export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false`) to two keys,
the bash two-key form `tools/memory-tree/check-verdict-epoch.test.sh@d31bef20:31` already exports.
It takes the per-command prefix of `tools/unattended/unattended.test.sh@d31bef20:1457`, so the plant
lives for one command. `git grep -n GIT_CONFIG_COUNT -- tools` prints 34 lines in 20 files (PINNED
2026-11-21), the Python form among them at `tools/drift-audit/selftest.py@d31bef20:4658` and
`tools/lexicon/selftest.py@d31bef20:46`.
`python tools/codebase-map/reuse_lookup.py "plant a git config default that an isolated fixture git init still reads"`
ranked `read_text`, `read`, `git` and `read_bytes` first, name-stem neighbours only. Its
`run_fixture_git` (`tools/run-gates/verdict_backends.py#run_fixture_git`) is a Python wrapper over one
fixed environment, which a bash suite cannot call. The map does not index environment-variable
idioms, so the grep found the seam the map missed.

Recall terms used: `python tools/memory-recall/query.py "how does a fixture stay files-backed when the machine's git config says reftable" --terms "GIT_CONFIG_GLOBAL GIT_CONFIG_NOSYSTEM GIT_CONFIG_COUNT reftable defaultRefFormat defaultBranch fixture isolation section 2o"`
