# TOOL-dWitnessedBar-71 — AC5's hostile git config reaches the fixture `git init` as command-scope environment config, which S6's isolation cannot mask, and the arm proves it is in effect before grading

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 40 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 |
| [2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 66 and 67
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md`)
confirmed finding **id 11 at HIGH**, report item **H2**. No other id shares that item. Report item
M1 describes the same defect at MEDIUM under ids 3, 18 and 21, which `TOOL-dWitnessedBar-73` takes.

`TOOL-dWitnessedBar-67` S6 runs every git call of section `2l` with `GIT_CONFIG_NOSYSTEM=1` and an
empty `GIT_CONFIG_GLOBAL`. AC5 plants its hostile config, `init.defaultBranch=main` and
`init.defaultRefFormat=reftable`, by exporting `GIT_CONFIG_GLOBAL` to a file. S6's isolation replaces
that file before the fixture `git init` runs, so git's built-in defaults apply, and the staged break
"dropping `--ref-format=files`" cannot turn AC5 red. The spec never says which mechanism AC5 grades.

This unit keeps S6's isolation for what it is for, shielding the fixtures from the machine's own
config, and plants the hostile config at a scope the isolation does not touch. The arm then proves
the plant is in effect before it grades a fixture. It repairs `TOOL-dWitnessedBar-67` and builds one
step after it (order 40).

## 2. Scope (IN)

- **S1** — The plant. Around section `2l`'s fixture build in `tools/lib/resolve-python.test.sh`, the
  suite exports `GIT_CONFIG_COUNT=2`, `GIT_CONFIG_KEY_0=init.defaultRefFormat`,
  `GIT_CONFIG_VALUE_0=reftable`, `GIT_CONFIG_KEY_1=init.defaultBranch` and `GIT_CONFIG_VALUE_1=main`
  inside a subshell that builds the fixtures, so the suite's own environment after section `2l`,
  including any `GIT_CONFIG_COUNT` its caller set, is untouched. Unit 67 S6's `GIT_CONFIG_NOSYSTEM=1`
  and empty `GIT_CONFIG_GLOBAL` stay in force inside it. This replaces AC5's exported hostile
  `GIT_CONFIG_GLOBAL`. Observed by AC1 and AC3.
- **S2** — The plant is proven in effect before any fixture is graded. Under S1's environment, the arm
  runs a plain `git init -q` in a scratch directory and asserts that `git rev-parse --show-ref-format`
  prints `reftable` and `git symbolic-ref HEAD` prints `refs/heads/main`. Otherwise it fails with
  `resolve-python: the hostile git config is not in effect` and grades no fixture of AC5. Observed by
  AC1 and AC2.
- **S3** — AC5 is graded under S1, and its staged break reaches the fixture. Each fixture built by
  `git -c init.defaultBranch=master init -q --ref-format=files` prints `files` and
  `refs/heads/master`. In a scratch copy whose fixture builder lacks `--ref-format=files`, the arm
  fails naming the fixture and `reftable`. Observed by AC3.

## 3. Non-goals (OUT)

- Unit 67 S6's isolation. It stays, and it still covers every git call of section `2l`.
- The two branch defences' own staged reds, the `-c init.defaultBranch=master` flag and the branch
  file read from `git symbolic-ref HEAD`. They are `TOOL-dWitnessedBar-73` S1 and S2, for ids 3 and 18.
- The report's left-shift text, a staged-red record that refuses an entry with no captured failing
  output. No clause of this build names that gate. S2's in-effect proof is the regression this unit
  builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-67` — S6's isolation of section `2l` and AC5's config-proof fixtures, whose hostile plant this unit moves to a scope the isolation cannot mask (id 11)
- **hands-off** `TOOL-dWitnessedBar-73` — the branch defences' staged reds and the AC5 ledger line naming which config scope wins, under S1's plant (ids 3, 18, 21, report item M1)
- **hands-off** `TOOL-dWitnessedBar-78` — one `refs/heads/master` assertion per fixture in section `2l`, and the ledger lines for AC1 and AC3 (ids 7 and 14 of the round-1 spec audit of units 68 to 73)

## 4. Design

### Evidence

Probed on git 2.54.0.windows.1, in fixture repositories under `%TEMP%/gcx`, with
`GIT_CONFIG_NOSYSTEM=1` and `GIT_CONFIG_GLOBAL` naming an empty file exported:

| environment beside the isolation | `git init` form | `--show-ref-format` | `symbolic-ref HEAD` |
|---|---|---|---|
| S1's five variables | plain `git init -q` | `reftable` | `refs/heads/main` |
| S1's five variables | `-c init.defaultBranch=master init -q --ref-format=files` | `files` | `refs/heads/master` |
| S1's five variables | `-c init.defaultBranch=master init -q` | `reftable` | `refs/heads/master` |
| S1's five variables | `init -q --ref-format=files` | `files` | `refs/heads/main` |

So the `GIT_CONFIG_COUNT` plant reaches an isolated `git init`, a `-c` flag outranks it, and dropping
either fixture flag changes what the fixture holds. The round's report reproduced the masking: an
inner `GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=<empty> git init` gave `files` and `refs/heads/master`
with the hostile file exported outside.

- Unit 67 S6's third bullet cites `tools/check-wiring.test.sh:1819`, which exports
  `GIT_CONFIG_GLOBAL="$D/.git/fixture-global" GIT_CONFIG_NOSYSTEM=1`.
- `init.defaultRefFormat`, `--ref-format` and `--show-ref-format` need git 2.45 or later. A git without
  them fails S2's assertion loudly rather than passing AC5.

### Inventory

Minted: the failure line of S2. No function, constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 40, after `TOOL-dWitnessedBar-67` (39). Order 40 is shared with
`TOOL-dWitnessedBar-72`. Their write sets do not meet, since this unit writes
`tools/lib/resolve-python.test.sh` and unit 72 writes `tools/run-gates/run-gates.gov.test.sh`, and
neither reads the other's file.

### Files touched (estimate)

- `tools/lib/resolve-python.test.sh`

### Alternatives rejected

- **Drop S6's third bullet so AC5's exported `GIT_CONFIG_GLOBAL` reaches the fixtures.** The fixtures
  then read the developer's own global config wherever AC5 does not export one, which is the leak the
  isolation exists to stop.
- **Say in S6 that the fixture `git init` inherits the caller's `GIT_CONFIG_GLOBAL`.** It splits one
  section's git calls into two config regimes that a later edit can cross silently.
- **Plant the hostile defaults in a repository's own `.git/config`.** `init.*` defaults are read before
  `git init` creates that file, so they never apply.

## 5. Production-readiness checklist

- security — no new write path. The plant lives only in the subshell that builds the fixtures.
- perf / scale — one extra `git init` per run, for S2.
- error / empty / loading states — S2 turns a git too old for `reftable`, or a plant that no longer
  reaches `git init`, into a named failure rather than a vacuous pass.
- observability — S2's line names the cause before any fixture assertion runs.
- risks — git's command-scope environment config is documented and stable since git 2.31.
- testing — AC1 and AC2 by probe, AC3 by scratch copy. The arm under §7 at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe exports S1's five variables beside `GIT_CONFIG_NOSYSTEM=1` and an empty
  `GIT_CONFIG_GLOBAL`, a plain `git init -q` gives `git rev-parse --show-ref-format` as `reftable` and
  `git symbolic-ref HEAD` as `refs/heads/main`. `grep -n 'GIT_CONFIG_COUNT=2' tools/lib/resolve-python.test.sh`
  names section `2l`.
  Red when: the hostile config is planted through `GIT_CONFIG_GLOBAL`, which the isolation masks.
  fixture: a scratch repository under `%TEMP%/<short-name>`.
  figure: the two values are PINNED, measured on git 2.54.0.windows.1 on 2026-10-25.
- **AC2** — When section `2l` runs from a scratch copy with S1's exports deleted, it prints `resolve-python: the hostile git config is not in effect` and grades no
  fixture of AC5.
  Red when: the arm grades the fixtures with no hostile config in effect.
- **AC3** — When section `2l` builds unit 64's fixtures under S1, each prints `files` for
  `git rev-parse --show-ref-format`. Against a scratch copy with `--ref-format=files` deleted from the
  fixture builder, the arm fails naming the fixture and `reftable`.
  Red when: the staged break leaves AC5 green, so the flag is certified with nothing observing it.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene`

The resolver leg runs `tools/lib/resolve-python.test.sh`. It is held unless the main loop sets
GATE_SELFTESTS at the close (`tools/run-gates/run-gates.sh:3129-3131`), which
`SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf:40`).

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 · section `2l`'s command-scope hostile plant and its in-effect proof, staged red by deleting S1's exports (reaches S2's line) and by deleting `--ref-format=files` (reaches the fixture's ref store) · none

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

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 66 and 67, id 11
  (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-78, promoted by the round-1 spec audit of units 68 to 73; nothing else
  moved.

## 10. Reuse audit

The seam is section `2l` of `tools/lib/resolve-python.test.sh` as units 64 and 67 build it, the
isolation `tools/check-wiring.test.sh:1819` already writes, kept unchanged, and the command-scope
form `tools/check-wiring.test.sh:38` already uses to pin `core.autocrlf`
(`export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false`), which S1 extends
to two keys. `git grep -n GIT_CONFIG_COUNT -- tools` also names `tools/drift-audit/selftest.py:4488`
and `tools/lexicon/selftest.py:46`, the same form in Python.
`python tools/codebase-map/reuse_lookup.py "plant a git config default that an isolated fixture git init still reads"`
ranked `read`, `git`, `read_text` and `fixture`, name-stem neighbours only; the map does not index
environment-variable idioms, so the grep found the seam the map missed.

Recall terms used: `python tools/memory-recall/query.py "how does a fixture stay files-backed when the machine's git config says reftable" --terms "GIT_CONFIG_GLOBAL GIT_CONFIG_NOSYSTEM GIT_CONFIG_COUNT reftable defaultRefFormat defaultBranch fixture isolation section 2l"`
