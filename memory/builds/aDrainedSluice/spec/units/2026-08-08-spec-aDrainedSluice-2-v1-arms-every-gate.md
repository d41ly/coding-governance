# TOOL-aDrainedSluice-2 — V1: the harness meta-gate discovers its gates

**Status:** CLOSED · rev-2 · 2026-08-20 · node a · Tier-2 · base 76fcd09b · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-08-review-TOOL-aBatchedTribunal-1-3.md](../../reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md) | diff-review | TOOL-aDrainedSluice-1 TOOL-aDrainedSluice-3 TOOL-aDrainedSluice-4 TOOL-aDrainedSluice-5 TOOL-aDrainedSluice-6 TOOL-aDrainedSluice-7 TOOL-aDrainedSluice-8 TOOL-aDrainedSluice-9 TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-8 |
| [2026-08-08-review-TOOL-aDrainedSluice-2-1.md](../../reviews/2026-08-08-review-TOOL-aDrainedSluice-2-1.md) | spec-audit | TOOL-aDrainedSluice-3 TOOL-aDrainedSluice-4 |

<!-- /gen:spec-records -->

## 1. Goal

`check-arms.py` names one gate and one test file. Every other gate with `fail` branches is silently
uncovered, and there is one: `skills/session-kickoff/manifest-check.sh` carries 16 `fail` calls
behind six numbers and no arm requirement at all. Discover the pairs instead of naming one.

## 2. Scope (IN)

- **S1** — the gate/test population is DISCOVERED: a tracked shell script that DEFINES the helper
  (`fail() {`) AND has `fail <n> "` call sites is a gate, and its test is the sibling named
  `<gate-stem>.test.sh`. Both come from `git ls-files`, so a new gate is covered the day it lands.
  The helper-definition clause is load-bearing: with a call-site predicate alone, any `*.test.sh`
  that quotes a fail line becomes a "gate" demanding a `<stem>.test.test.sh` that will never exist,
  and the whole suite goes permanently red. `*.test.sh` is excluded from the gate population outright
  as well — belt and braces, because the fixture shape is one shell-written heredoc away and
  `check-arms.py`'s own selftest already builds one.
- **S1b** — the population is `*.sh`, and the two EXTENSIONLESS shell gates in `.githooks/` are
  outside it. Neither carries a `fail` helper today, so nothing is missed; the hole is recorded as a
  named follow-up rather than left implicit in a glob.
- **S2** — a gate with `fail` branches and NO sibling test is a NAMED failure, not a skip. That state
  is exactly "fourteen unarmed branches and nothing to arm them with", and it must be loud.
- **S3** — the branch key gains the gate: `(gate, check number, ordinal)`. The reason is the PIN,
  not the arm scan. Each gate is paired with its OWN sibling test and the scan reads only that file,
  so one gate's arm can never reach another's branch with either key — the original justification was
  untestable. The pin's keys, by contrast, are global: simulated over the widened population, four
  manifest-check branches collide with hygiene's existing pin rows and produce false stale-signature
  reds, and a signature that happened to match would produce a false EXEMPTION instead.
- **S4** — the pin file gains the same field, and every existing row is migrated to it in this unit.
  A pin row whose gate no longer exists reds, exactly as a row whose branch no longer exists does.
- **S4b** — the captured message TERMINATES at the closing quote of the shell string. `FAIL_RE`
  captures to end of line, which is safe only where every `fail` is the last statement on its line.
  `manifest-check.sh` writes five branches inline as `{ fail 2 "…"; BLOCK_OK=0; }`, so five of its
  sixteen signatures would end in shell source — text no assertion can ever emit, making those rows
  PERMANENTLY unarmable inside a shrink-only pin.
- **S5** — the floors become PER-GATE, not aggregate, and are re-measured. An aggregate total lets
  one gate's DELETED guard be masked by another gate's added one, and it goes slack by a whole gate's
  branch count the day a third gate lands — a guard that gets quieter as the population grows. The
  measured targets: the pin goes 9 rows to about 25, the branch floor 14 to 30, and the armed floor
  stays 5, because every arm in this repo currently lives in the hygiene suite.
- **S6** — `check-arms.py` is outside the population by EXTENSION, and that is stated as a fact
  rather than defended as a guard. The earlier rationale was wrong twice: the matcher does not match
  its own matcher line, and what would match is the selftest's own fixture strings. A `.py` file is
  not a `*.sh`, so the exclusion clause was unreachable and the criterion that "proved" it was green
  on an empty population.
- **S6b** — a gate that raises a NAMED error does not abort the walk. The error becomes a finding
  line naming that gate and the scan continues, so one bad gate cannot hide every other gate's
  unarmed branches, every stale pin row and both floors behind a single red line.
- **S7** — `--report` groups by gate, `--emit-pin` emits the four-field rows, and the self-test gains
  arms for the multi-gate key, the missing-test failure, and the self-exclusion.

## 3. Non-goals (OUT)

- Extensionless shell gates. `.githooks/pre-commit` and `.githooks/pre-push` are shell gates with
  their own self-tests, and a `*.sh` glob does not see them. Measured: neither carries a `fail`
  helper, so the population is complete today. Recorded here as a named follow-up so the next person
  to add a `fail` branch to a hook finds this sentence instead of a silent hole.
- Arming the newly discovered branches. That is V2; this unit makes them VISIBLE, which is the
  prerequisite and the whole point of a pin.
- Discovering gates written in Python. `corpus_ids.py`, `gotchas.py` and `gen_build_index.py` report
  findings through a list and a return code rather than a `fail` helper, and inventing a second
  branch grammar to cover them is the catalogue-drift class. Recorded as a follow-up if one appears.
- Renaming any check or renumbering any branch.

## 4. Design

### Data model

```
gate     : a tracked *.sh whose body has a `fail <n> "` call site, excluding this module's own file
test     : <gate-stem>.test.sh beside it — absent is a NAMED failure, never a skip
branch   : (gate, check number, ordinal within that number, source line, signature)
pin row  : gate<TAB>check<TAB>ordinal<TAB>signature
floors   : ARMS_BRANCH_FLOOR · ARMS_ARMED_FLOOR, re-measured over both gates
```

### Inventory

| Before | After |
|---|---|
| `HYGIENE` and its test named as constants | both discovered from `git ls-files` |
| pin rows `check<TAB>ordinal<TAB>signature` | `gate<TAB>check<TAB>ordinal<TAB>signature` |
| one gate's branches | every gate's, grouped in the report |

### Migration

The nine existing pin rows gain a leading gate field naming
`tools/memory-tree/check-memory-hygiene.sh`. `--emit-pin` regenerates the file, and the result is
compared against the old rows so the migration is a widening rather than a rewrite.

### Rollout

One commit: the module, the migrated pin, the re-measured floors, the self-test arms.

### Files touched (estimate)

`tools/memory-tree/check-arms.py`, `memory/project/unarmed-branches.txt`, `.memory-tree.conf`.

### Alternatives rejected

- **List the pairs in the conf.** Rejected: a list is a second copy of what the tree already says,
  and the row this unit drains exists because a named list went stale the moment a gate was added.
- **Treat a missing sibling test as "no arms required".** Rejected: it is the loudest possible state
  and would be the quietest possible output.

## 5. Production-readiness checklist

- security — N/A. Reads tracked shell sources.
- perf / scale — one `git ls-files` plus one read per gate and per test.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a tree with no gate at all fails: this module exists because
  branches need arms, and finding no branches on a repo that has gates is the vacuity it guards.
- observability — `--report` groups by gate and prints each branch's line, signature and state.
- risks — widening the key changes the pin format; the migration is in the same commit.
- testing + left-shift gates — self-test arms for the multi-gate key, the missing test, the
  self-exclusion, and the re-measured floors.
- migration / rollback — one commit.
- user docs — `HYGIENE.template.md` and the kit README.

## 6. Acceptance criteria

- **AC1** — When gate A's `(check 1, ordinal 1)` is PINNED, gate B's `(check 1, ordinal 1)` is still
  reported as unarmed-and-unpinned, no stale-signature line mentions gate B, and no "IS armed now"
  line is raised against gate A. The criterion is about the PIN, because the arm scan is per-pair and
  an arm-worded criterion is green with or without the gate field.
- **AC2** — When a gate has `fail` branches and no sibling `.test.sh`, `--check` fails naming the
  gate.
- **AC3** — When the population is discovered, `check-arms.py` is absent from it because it is not a
  `*.sh`, and a `*.test.sh` that quotes a `fail <n> "` line is absent because it does not define the
  helper. Both are asserted; neither is assumed.
- **AC3b** — When a captured message is followed by more shell on the same line, the signature ends
  at the closing quote and contains no shell source — asserted with an inline-form fixture whose
  green side is a test file containing only the real message.
- **AC4** — When a pin row names a gate that no longer exists, `--check` fails naming the row.
- **AC5** — When `--report` runs on this repo, it lists branches from both
  `check-memory-hygiene.sh` and `manifest-check.sh`.
- **AC6** — When the floors are read, they are PER-GATE and equal the freshly measured counts, and
  the measurement is recorded in the build journal. When gate A loses a branch and gate B gains one,
  leaving the total unchanged, the per-gate floor still reds.
- **AC6b** — When one gate raises a named error, every other gate's branches, the pin-liveness rules
  and the floors are still evaluated in the same run.
- **AC7** — When `--selftest` runs, every arm above has a red and a green side and the pass line
  prints last.

## 7. Gates

`bash tools/run-gates.sh` in full; the `harness arms` and `check-arms selftest` legs carry this unit.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — how a gate's test is found.** Options: a naming convention, or a declaration in the
  conf. RESOLVED (owner, 2026-08-08): the convention. Every test in this kit is already
  `<stem>.test.sh` beside its subject, and a declaration is the stale-list shape this unit drains.
- **Fork B — Python gates.** Options: widen the branch grammar, or scope to shell. RESOLVED
  (owner, 2026-08-08): scope to shell, said out loud in §3. The Python gates report through a list
  and a return code; a second branch grammar to cover them is the catalogue-drift class, and each of
  those modules already ships its own selftest with per-rule arms.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 1: M3 terminates the capture at the closing quote (five
  manifest-check signatures would otherwise have been permanently unarmable); M4 restates S3/AC1 in
  terms of the pin, whose keys really do collide; M5 replaces an unreachable self-exclusion and its
  wrong rationale with an extension-scope fact; M7 makes the floors per-gate; M8 requires the helper
  definition and excludes `*.test.sh`; M14 stops one gate's error aborting the walk; M15 records the
  extensionless-hook hole. The corrected target numbers (pin ~25, branch floor 30, armed floor 5)
  replace the draft's guesses.

## 10. Reuse audit

The discovery rule is the one `gen_build_index.py` already uses for builds and `gotchas.py` already
uses for records: derive the population from the tree, never from a list. The `<stem>.test.sh`
convention is the kit's existing one, unchanged. The pin keeps the shape of the kit's other
grandfather lists and gains one field. The floors follow the measured-pin convention. Nothing new is
scaffolded; one constant pair becomes a walk.
