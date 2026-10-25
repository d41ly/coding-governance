# TOOL-dWitnessedBar-92 — the round-1 audit of unit 90, 13 minors batched: a call site isolated from the floor, ledger notes labelled and placed under their answer, criteria that can red, a narrower write grant and a derivation that names every exit

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 48 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 |
| [2026-10-25-build-TOOL-dWitnessedBar-91-round13-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-91-round13-fix-return.md) | research | TOOL-dWitnessedBar-91 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-91-round13-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-91-round13-fix-brief.md) | research | TOOL-dWitnessedBar-91 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of unit 90
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-90-spec-audit-round1.md`)
exited CONVERGED with 14 confirmed findings: one at HIGH, which `TOOL-dWitnessedBar-91` takes, and 13
minors. BUILD-METHOD M4 batches every MEDIUM and LOW into one unit, or two only where they split into
disjoint write sets by M6's clauses. §4 "Why one unit" says why these stay one. Each finding is named
by report id and is its own scope item, including where the report merged two ids into one item.
Every minor lands on `TOOL-dWitnessedBar-90`, so this unit repairs unit 90 and builds one step after
it (order 48).

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M1 | MEDIUM | 6 | unit 90 S2, AC2 | S1 |
| M2 | MEDIUM | 2 | unit 90 AC1, §7 New arm | S2 |
| M3 | MEDIUM | 3 | unit 90 ledger clauses of AC1 to AC4, AC6, AC7 and AC9 to AC15 | S3 |
| M4 | MEDIUM | 4 | unit 90 S3, S15, AC3, AC15 | S4 |
| M5 | MEDIUM | 9 | unit 90 S12, S13, §4 Evidence, §10, AC12, AC13 | S5 |
| M6 | MEDIUM | 11 | unit 90 AC10, ledger notes of S1 to S15 | S6 |
| M7 | MEDIUM | 13 | unit 90 S13, AC13 | S7 |
| L1 | LOW | 7 | unit 90 §4 Evidence | S8 |
| L1 | LOW | 12 | unit 90 S11, AC11 | S9 |
| L2 | LOW | 5 | unit 90 §4 Rollout, S10 | S10 |
| L3 | LOW | 8 | unit 90 S12, §4 Evidence | S11 |
| L4 | LOW | 14 | unit 90 §4 owner derivation, S15, §5, AC15 | S12 |
| L5 | LOW | 16 | unit 90 ledger notes of S1 to S15 | S13 |

That is 7 MEDIUM and 6 LOW findings by raw id. Ids 7 and 12 share item L1. Id 6 is the defect id 1
names, found at a medium grade: the two items share one fix, which unit 91 makes, and S1 adds the
half only id 6's fix names.

## 2. Scope (IN)

- **S1** — id 6. The anchored count's baseline. On the built tree,
  `grep -c 'sha)[[:space:]]*rec_sha="' .githooks/pre-push` prints 0, because unit 69's built arm is
  `sha) rec_sha=$_rg_v`, unquoted. Beside unit 91 S1's 1 in each quoted clone of 90 AC2, that 0 shows
  the count tells a quoted arm from the built one, so the 1 is the clone's edit. Unit 90's ledger
  records the 0 in the note row `92|S1` of §4's note table. Observed by AC1.
- **S2** — id 2. 90 AC1's clones isolated from the floor. Each of 90 AC1's two scratch clones also
  carries one line directly after the canary's top-level call site of `check_canary_keys`, in the
  parent shell. The line adds to `a` the increments the call site's `0)` arm adds, read from the
  built call site. A skipped visited increment then leaves `a` at the floor, so only the call site's
  verdict can fail the arm. 90 AC1's exit clause is superseded: each clone exits non-zero and prints
  no line holding `PASS (` and none holding `below the pinned floor`, beside 90 AC1's other clauses.
  90 §7's staged red is corrected: a third clone with the same added line and a call site handling
  0, 1 and 2 alone ends `PASS (<n> assertions)`, and the main loop records that last line before
  it pins anything. The added line never sits inside `check_canary_keys`, which runs in a
  command-substitution subshell, and S2 adds no line to the built suite and no marker to
  `check_canary_keys`. Unit 90's ledger records the third clone's last line in note row `92|S2`.
  Observed by AC2.
- **S3** — id 3. Each note keyed on the item that writes it. Every note unit 90 writes in another
  unit's ledger opens with the label `TOOL-dWitnessedBar-90 S<k>`, where `<k>` is the item writing it.
  Each of 90's ledger clauses is read through §4's note check over that item's rows of §4's note
  table, in place of a `grep -n 'AC<n>'` that only has to find a line naming `TOOL-dWitnessedBar-90`.
  One item writes each label, so no item's clause can pass on another item's line. Observed by AC3.
- **S4** — id 4. Two criteria that can red. First, 90 AC3's `grep -c 'sha)'` over the probe's own
  scratch files is struck. The probe's diff counts read 89 S6's fixed text, which no build act
  changes, so they stand PINNED by 90 §4 Evidence (2026-10-25) and are not run by the build. 90 S2's
  clones, 89 AC6's clone and 88 AC10's clones grade the built loop. Second, 90 AC15's
  `sed ... | grep -cE 'python3? -c'` clause over 90's own text is struck. In its place, each
  close-time run of the owner derivation that 88 AC6 and AC18 and 89 AC9 and AC12 make is recorded in
  a note under that criterion's answer. The note quotes `resolve_python: <the path it printed>` and the
  derivation's exit. These are note rows `92|S4`, with one more in unit 90's ledger under AC3 that
  marks the probe `PINNED`. Observed by AC4.
- **S5** — id 9. The write grant left narrow. 90 S13's declaration of `memory/builds/dWitnessedBar/spec/`
  in `--writes` is withdrawn, for this unit's pass and for every pass 90 S13 or 89 S13 binds. The
  `gen:spec-records` regions that `gen_build_index.py --write` moves are committed under the seam
  `--check-commit` already has. It admits a path a kit `[[generated]]` row or `GENERATED_INDEXES`
  covers, through `resolve_generated_indexes`, and a path whose change sits inside gen regions alone,
  through `check_gen_region_only`. 90 S12's statement names all three `[[generated]]` rows
  `gen_build_index.py` owns: `{memory_root}/LIVE.md`, `{memory_root}/ledger` and
  `{memory_root}/backlog`. With the declaration withdrawn, S12's "this build adds no rule beside it"
  holds. `spec/` stays in 90's Files touched and in 90 AC13's porcelain read, which observe a commit
  and grant nothing. Units 89 and 90 dispatch before this unit, so a declaration either made is
  answered after the fact: each of their pass commits changed no other unit's spec outside its gen
  regions. Note rows `90|S13` and `92|S5` record it. Observed by AC5.
- **S6** — id 11. Notes under the answer, never beside it. Every note units 90 and 92 write in an
  acceptance ledger is a continuation line under the `- AC<n>` answer its note-table row names: two
  spaces in, never a line opening `- `. It is written once that answer exists. 90 AC10's
  `grep -cE "^- AC${n} "` count, which reads at least 1, is superseded: it reads exactly 1 for each
  of 89's thirteen criteria, so it counts 89's own answers alone. The same exact count holds for each
  answer a note of this build sits under, in the ledgers of units 87, 88 and 90. A ledger with 90's
  notes and no 89 answer beside AC4 then reds. Observed by AC6.
- **S7** — id 13. 90 AC13 reads the regeneration's exit. 90 AC13's regeneration runs as
  `. tools/lib/resolve-python.sh; py=$(resolve_python) || exit 5`, then
  `"$py" tools/memory-tree/gen_build_index.py --write`. It must exit 0 before
  `git status --porcelain --untracked-files=no -- memory/` is read, in place of 90 AC13's bare
  `python` with no exit read. Unit 90's ledger records the exit in note row `92|S7`.
  Observed by AC7.
- **S8** — id 7. The floor-comment inventory, stated as the command prints it. Over base `cdfbd1cf`,
  `grep -n -i floor tools/run-gates/run-gates.gov.test.sh` prints lines 20, 91, 92, 94, 262, 377, 378,
  396, 408 and 459. It does not print `:93` or `:95`, which are a continuation line and the
  `TOOL-dDerivedDocket-23` line. This corrects 90 §4 Evidence's first bullet, and this spec's §4
  Evidence carries it. NOT OBSERVED by the build: the inventory reads a base blob that no build act
  changes, and S9 observes on the built tree the keep list it decides.
- **S9** — id 12. 90 S11's keep list, made whole. Beside the comments 90 S11 keeps, the floor comments
  outside the assertion floor stay untouched: `:20` (`test_recall_floor.py from the payload`) and
  `:262` (`1565 s floor`). So does `:396`, the section header
  `# ---- THE SHARD CONTRACT, both directions (TOOL-aShardedFloor-2) ----`, though it carries the unit
  id 90 S11 drops from the owner line. This unit's pass reads all three on the built tree. Where unit
  90's pass removed one, this pass restores it, byte for byte, from base `cdfbd1cf`. Unit 90's ledger
  records the reading in note row `92|S9`. Observed by AC8.
- **S10** — id 5. Each act at its phase. 90 §4 Rollout is superseded. S11, S14 and S15's probes run at
  the pass, and S3's probe is PINNED (S4). S1, S2 and S9's clones run at the close. AC13's
  regeneration runs after the pass commit, and every ledger note is written at the close. 90 S10's
  reading of unit 89's schedule is superseded too. 89 AC4, AC6, AC7, AC10 and AC12 have a half at the
  pass, and 89 AC1 is wholly at the close. 89 AC2, AC3, AC5, AC8, AC9 and AC11 are graded at the
  close, and 89 AC13's porcelain read runs after its pass commit. 90 S10's note, row `90|S10`, quotes
  `AC4 AC6 AC7 AC10 AC12` as the criteria with a pass half. Unit 90's ledger records the Rollout in
  note row `92|S10`. Observed by AC9.
- **S11** — id 8. The pre-commit trigger, stated by its filter. 90 S12's sentence is restated as
  follows. `.githooks/pre-commit` runs hygiene with `--staged`, and so check 9, on a commit that
  adds, copies, modifies or renames a path under `memory/` (`--diff-filter=ACMR`). A deletion-only
  commit under `memory/` runs no staged hygiene, and `regen.py --check` before the bar's first leg is
  its backstop. 90 S12's note, rows `90|S12`, carries `--diff-filter=ACMR` beside
  `regen.py --check` and `check 9`. Observed by AC10.
- **S12** — id 14. The owner derivation names every exit. §4's owner derivation takes the place of 90
  §4's, which took the place of 89 §4's. It keeps exits 3 to 6. It adds `TOKEN READER NOT FOUND`
  (exit 7) for a `tools/check-spec-tokens.py` that is missing or fails to load, `SPEC UNREADABLE <path>`
  (exit 8) for an index row naming a spec it cannot read, and `TOKEN READER FAILED <path>` (exit 9)
  for an `extract_gates` that raises. Every close-time run of the owner derivation runs this script:
  88 S6, AC6 and AC18, 89 S9, AC9 and AC12, and 90 AC15. Unit 90's ledger records the staged exits in
  note row `92|S12`. Observed by AC11.
- **S13** — id 16. A note's grepped tokens on one physical line. Every note units 90 and 92 write
  carries its label and every token its note-table row names on one physical line, and wraps only
  prose after it, as `memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md` rules. §4's
  note check reads the label and the token on one line, so a wrapped token reads as no note.
  Observed by AC12.

## 3. Non-goals (OUT)

- Rewording the spec text of unit 90. Each item is closed by what this pass builds or observes, and a
  criterion it supersedes is answered in unit 90's ledger by name, as `TOOL-dWitnessedBar-90` §3 does
  for units 87 and 89.
- Unit 91's anchored count and only-arm check. S1 adds the baseline beside them and restates neither.
- Notes written by units other than 90 and 92. Unit 91 S2 states its own note's spelling, which is
  the spelling S6 and S13 give.
- The left-shift gates the report names: spec-lint rules for an exact `grep -c` count, a staged-red
  clone's Red-when, a shared ledger selector, a criterion fed only its own text, a `--writes`
  directory, a bare launcher, a Rollout phase, a quoted command's output and a script's exit codes,
  and the hygiene check 23 tightenings. No clause of this build names them.
- New assertions in the suite, and a `New arm:` line. S9 only restores comments unit 90's pass may
  have removed. So `TOOL-dWitnessedBar-88` S6's derivation still names unit 90 the floor's owner.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-90` — AC1's clones and §7's staged red, S3's probe, S10's schedule, S11's keep list, S12's freshness claim, S13's write set, §4's owner derivation, Rollout and Evidence, and the ledger clauses of AC1 to AC4, AC6, AC7 and AC9 to AC15, which S1 to S13 supersede or complete (ids 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14 and 16)
- **consumes-from** `TOOL-dWitnessedBar-91` — S1's anchored count `sha)[[:space:]]*rec_sha="`, whose baseline over the built hook S1 observes (id 6, the medium-graded half of H1)
- **consumes-from** `TOOL-dWitnessedBar-69` — S1's unquoted `sha) rec_sha=$_rg_v` arm, on which S1's baseline reads 0 (id 6)
- **consumes-from** `TOOL-dWitnessedBar-89` — its ledger's `- AC<n>` answers, under which S3, S4 and S6 place notes and which S6 counts, and its §5 schedule, which S10 restates in unit 90's note (ids 3, 4, 5 and 11)
- **consumes-from** `TOOL-dWitnessedBar-88` — AC6's and AC18's close-time runs of the owner derivation, which S4 records and S12's derivation replaces, and their ledger answers (ids 4 and 14)
- **consumes-from** `TOOL-dWitnessedBar-87` — its ledger's `- AC2` answer, under which unit 90 S6's note sits by S3 and S6 (ids 3 and 11)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The one item that may write
code is S9, which can restore a comment in `tools/run-gates/run-gates.gov.test.sh`. S2's clones run
that suite, so the rest of the batch reads S9's output as an acceptance input, which M6 clause 2
forbids. Every other item writes notes into the ledgers of units 87, 88, 89 and 90, and S6 counts
the answers those notes sit under, so a split would share those records. Dispatch is strictly
sequential, a shared order included (`tools/workflows/unattended-build.js:76`), so a split would buy
no concurrency.

### Evidence

- `tools/run-gates/run-gates.gov.test.sh`, unchanged from base `cdfbd1cf` to `d42cdf8b`:
  `grep -n -i floor` prints 20, 91, 92, 94, 262, 377, 378, 396, 408 and 459. `:93` and `:95` hold no
  `floor`. Each of `THE SHARD CONTRACT, both directions (TOOL-aShardedFloor-2)`,
  `test_recall_floor.py from the payload` and `1565 s floor` is counted once by `grep -c`. `:459`
  prints `below the pinned floor`, and `:460-465` print `PASS ($a assertions)` only when `fail` is 0.
- `.githooks/pre-push:1350` and `:1352` hold the two `rec_sha=""` resets, and
  `grep -c 'sha)[[:space:]]*rec_sha="'` prints 0 on today's hook. Spec-69 line 74 spells the built
  arm `sha) rec_sha=$_rg_v`.
- `TOOL-dWitnessedBar-89` S7 (spec-89 lines 92-96) puts the canary's visited increment at its single
  top-level call site and none in the body of `check_canary_keys`. 89 S4 (lines 69-77) returns 3 on a
  visited failure. Neither is built yet.
- `tools/unattended/unattended.sh:13552-13559` is `--check-commit`'s admission loop. It admits a
  path a declaration covers, then one `GENERATED_INDEXES` covers, then one where
  `check_gen_region_only "HEAD:$p" ":$p"` holds, and refuses the rest with fail 49 at `:13565` and
  `:13577`, `stages paths outside the set it declared`. `GENERATED_INDEXES` is resolved at `:750`
  through `resolve_generated_indexes` (`tools/unattended/lib-unattended.sh:838`).
  `check_gen_region_only` (`tools/unattended/lib-unattended.sh:1137`) compares two blobs through
  `GEN_REGION_AWK` (`:1136`). `covers` (`:745-749`) admits every path under a declared directory.
- `tools/memory-tree/kit.toml:473-478`, `:481-486` and `:489-495` are the three `[[generated]]` rows
  whose generator is `gen_build_index.py`: `{memory_root}/LIVE.md`, `{memory_root}/ledger` and
  `{memory_root}/backlog`. `.unattended.conf:418` names none of them.
- `.githooks/pre-commit:180` gates the staged hygiene leg on
  `git diff --cached --name-only --diff-filter=ACMR -- 'memory/**'`. `tools/run-gates/run-gates.sh:1449`
  runs `regen.py --check`.
- `tools/memory-tree/check-memory-hygiene.sh:3146` opens a ledger answer on `^- *(\*\*)?AC[0-9]+`, and
  `:3158` adds the backticked tokens of every later non-blank line to that answer, so a continuation
  note joins the answer it sits under. `memory/HYGIENE.md` "Acceptance ledger" (`:686`) gives one
  answer line per criterion, inside an `**Evidences:**` block.
- `tools/check-spec-tokens.py:495` defines `extract_gates`. §4's owner derivation was probed on
  2026-10-25 against a scratch copy of the five paths it reads. Over the live README it printed 28 and
  `spec/2026-10-25-spec-TOOL-dWitnessedBar-90.md`, exit 0. It printed `SPEC UNREADABLE <path>`, exit
  8, with a README row repointed to a spec that does not exist. It printed `TOKEN READER NOT FOUND`,
  exit 7, with `check-spec-tokens.py` removed, and again with no `extract_gates` in it. It printed
  `TOKEN READER FAILED <path>`, exit 9, with an `extract_gates` that raises. It printed
  `MALFORMED REGION` exit 3, `REGION READER NOT FOUND` exit 4 and `REGION READ FAILED (rc 2)` exit 6
  on 90 AC15's three stagings. PINNED on 2026-10-25. Units 91 and 92 declare no `New arm:`, so a
  re-render that lists them leaves the length at 28 and the owner at unit 90.
- §4's note check was probed on 2026-10-25 over a fixture ledger. It printed `NOTES OK 4` for four
  placed rows. It printed `MISPLACED` for a row naming the wrong answer, and `NO NOTE` for a label no
  line carries and for a token not on the label's line. `S1([^0-9]|$)` did not match an `S11` note.
- `memory/builds/dWitnessedBar/RUN.md` records a dispatch as
  `dispatch · item <sha8> <unit> · reason <declared paths>`, as `memory/builds/aBatchedArm/RUN.md:59`
  shows.

### The note table

One row per note, `<unit>|<item>|<ledger unit>|<answer>|<token>`. The note carries the label
`TOOL-dWitnessedBar-<unit> <item>` and the token on one physical line. It sits under the `- <answer>`
line of the acceptance ledger of `TOOL-dWitnessedBar-<ledger unit>`. An empty token asks for the label
alone.

```text
90|S1|89|AC4|
90|S2|89|AC6|rec_sha="${_rg_v}"
90|S3|89|AC6|sha)
90|S4|89|AC11|
90|S6|87|AC2|
90|S7|89|AC3|struck
90|S9|89|AC1|lost its CR
90|S9|89|AC4|for unread
90|S10|89|AC12|AC4 AC6 AC7 AC10 AC12
90|S11|89|AC10|build_commit
90|S12|89|AC13|--diff-filter=ACMR
90|S12|89|AC13|regen.py --check
90|S12|89|AC13|check 9
90|S12|89|AC13|{memory_root}/ledger
90|S13|89|AC13|check_gen_region_only
90|S14|89|AC7|
90|S15|89|AC12|resolve_python
92|S1|90|AC2|sha)[[:space:]]*rec_sha="
92|S2|90|AC1|PASS (
92|S4|90|AC3|PINNED
92|S4|88|AC6|resolve_python:
92|S4|88|AC18|resolve_python:
92|S4|89|AC9|resolve_python:
92|S4|89|AC12|resolve_python:
92|S5|90|AC13|--writes
92|S7|90|AC13|gen_build_index.py --write
92|S9|90|AC11|THE SHARD CONTRACT
92|S10|90|AC1|at the close
92|S12|90|AC15|TOKEN READER NOT FOUND
```

### The note check

Run as a script with `bash` from the repository root, the note-table rows it grades on stdin. It
prints `NOTES OK <rows>` and exits 0 when every row's note is present and placed. Otherwise it prints
`NO SINGLE LEDGER <unit>`, `NO NOTE <unit> <item> <token>` or `MISPLACED <unit> <item> <token>` for
each failing row and exits 1.

```bash
b=memory/builds/dWitnessedBar/build
bad=0; n=0
while IFS='|' read -r u s l a t; do
  [ -n "$u" ] || continue
  f=$(ls $b/*TOOL-dWitnessedBar-${l}-*acceptance-ledger* 2>/dev/null)
  [ "$(printf '%s' "$f" | grep -c .)" = 1 ] || { echo "NO SINGLE LEDGER $l"; bad=1; continue; }
  o=$(awk -v k="TOOL-dWitnessedBar-$u $s([^0-9]|\$)" -v t="$t" '/^\*\*Evidences:\*\*|^#/{o=""} /^- /{o=$0} $0 ~ k && (t == "" || index($0, t)) {print o}' "$f")
  [ -n "$o" ] || { echo "NO NOTE $u $s ${t:-}"; bad=1; continue; }
  printf '%s\n' "$o" | grep -qvE "^- (\*\*)?$a[^0-9]" && { echo "MISPLACED $u $s ${t:-}"; bad=1; continue; }
  n=$((n+1))
done
[ "$bad" = 0 ] && echo "NOTES OK $n"
[ "$bad" = 0 ]
```

A note spelled as its own `- AC<n>` line passes the placement test, because it is its own opener.
S6's exact count is what refuses it.

### The owner derivation

Run as a script with `bash` from the repository root. It prints the New-arm list's length, then the
owner's spec path. Its failures are `MALFORMED REGION` (exit 3), `REGION READER NOT FOUND` (exit 4),
`resolve_python`'s own refusal (exit 5), `REGION READ FAILED (rc <n>)` (exit 6),
`TOKEN READER NOT FOUND` (exit 7), `SPEC UNREADABLE <path>` (exit 8) and `TOKEN READER FAILED <path>`
(exit 9). The region is decoded with replacement, so no byte in it raises. An exit 1 is left only to
an interpreter that cannot start the fixed program, which the probe above did not see.

```bash
eval "$(sed -n '/^region() {/,/^}/p' tools/unattended/unattended.sh)"
declare -F region >/dev/null || { echo 'REGION READER NOT FOUND'; exit 4; }
. tools/lib/resolve-python.sh
py=$(resolve_python) || exit 5
b=memory/builds/dWitnessedBar/
r=$(region "${b}README.md" '<!-- gen:build-units -->' '<!-- /gen:build-units -->'); rc=$?
[ "$rc" = 3 ] && { echo 'MALFORMED REGION'; exit 3; }
[ "$rc" = 0 ] || { echo "REGION READ FAILED (rc $rc)"; exit 6; }
prog=$(cat <<'PY'
import sys, re, importlib.util as u
b = 'memory/builds/dWitnessedBar/'
try:
    s = u.spec_from_file_location('cst', 'tools/check-spec-tokens.py'); m = u.module_from_spec(s); s.loader.exec_module(m); x = m.extract_gates
except Exception:
    print('TOKEN READER NOT FOUND'); sys.exit(7)
o = []
for p in re.findall(r'\]\((spec/[^)]+)\)', sys.stdin.buffer.read().decode('utf-8', 'replace')):
    try:
        t = open(b + p, encoding='utf-8').read()
    except (OSError, UnicodeDecodeError):
        print('SPEC UNREADABLE ' + p); sys.exit(8)
    try:
        g = x(t) or ''
    except Exception:
        print('TOKEN READER FAILED ' + p); sys.exit(9)
    if any(l.startswith('New arm: tools/run-gates/run-gates.gov.test.sh') for l in g.splitlines()):
        o.append(p)
print(len(o)); print(o[-1] if o else 'NO OWNER')
PY
)
printf '%s\n' "$r" | "$py" -c "$prog"
```

### Inventory

Minted: the derivation's `TOKEN READER NOT FOUND`, `SPEC UNREADABLE <path>` and
`TOKEN READER FAILED <path>` lines with exits 7, 8 and 9; the note check's `NOTES OK <rows>`,
`NO SINGLE LEDGER`, `NO NOTE` and `MISPLACED` lines; the note labels `TOOL-dWitnessedBar-92 S<k>`.
No function, constant, plant, flag or file in the product. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 48, one above unit 90's 47 and beside `TOOL-dWitnessedBar-91`. S9's
reading and any restore run at the pass. S5's dispatch reading and pass-commit reading, and S7's
regeneration, run after the pass commit. S1, S2, S5's scratch-clone probe and S12's stagings run at
the close, with every note.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **Two batches, the suite half and the ledger half.** §4 "Why one unit".
- **Key each selector on a token only its item writes, the report's first way for id 3.** The
  tokens are chosen one by one, and the next item that quotes another's token reopens the defect. A
  label written by one item is unique by construction.
- **Filter unit 90's lines out with `grep -v 'TOOL-dWitnessedBar-90'`, for id 11.** 89's own answers
  legitimately name unit 90, as its AC12 answer and AC9's derivation output do, so a correct build
  would red.
- **Put the floor compensation inside `check_canary_keys`, the finder's first way for id 2.** The
  canary calls it in a command substitution, so an increment there never reaches the parent shell.
- **A marker line S1 of unit 90 prints on 3, the finder's second way for id 2.** It contradicts 90
  S1's "prints nothing beyond the visited line" and mints a probe-only marker, which 90 §8 F3 refuses.
- **Narrow 90 §4 Evidence's command to `grep -n FLOOR`, a way id 12's fix offered.** It prints only
  `:94` and `:459`, so the bullet would still not list what the command prints.

## 5. Production-readiness checklist

- security — the write grant narrows: no pass of this build declares the spec directory. The scratch
  clones sit under `%TEMP%`.
- perf / scale — one note-check run over 29 rows, the derivation's stagings and four clones, once.
- error / empty / loading states — the note check names a missing ledger, a missing note and a
  misplaced one apart. The derivation names seven failures, each with its own exit.
- observability — every note carries its writer's label, so a ledger line traces to its item.
- risks — a writer who spells a note as its own `- AC<n>` line passes the placement test; S6's exact
  count refuses it. A row whose token two notes carry passes on either; the label confines it to one
  item.
- testing — S9 at the pass; AC5's dispatch and commit reads and AC7 after the pass commit; AC1, AC2,
  AC5's scratch clone and AC11 by fixture at the close; the note checks at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — On the built tree, `grep -c 'sha)[[:space:]]*rec_sha="' .githooks/pre-push` prints 0.
  When §4's note check is fed the note-table rows opening `92|S1|`, it prints `NOTES OK 1`.
  Red when: the built arm is quoted, so the anchored count reads 1 with no clone edit and cannot tell
  a quoted arm from the built one.
  permission: the ledger is written at the close.
- **AC2** — In each of 90 AC1's two scratch clones, carrying the line S2 adds after the top-level call
  site, the arm exits non-zero and prints no line holding `PASS (` and none holding
  `below the pinned floor`. In a third clone with the same line and a call site handling 0, 1 and 2
  alone, the last line the arm prints holds `PASS (`. When §4's note check is fed the rows opening
  `92|S2|`, it prints `NOTES OK 1`.
  Red when: a call site that handles 0, 1 and 2 alone fails the isolated clone through the floor.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  figure: the increment count is DERIVED at observation time from the built call site's `0)` arm.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When §4's note check is fed every note-table row opening `90|`, it prints
  `NOTES OK 17` and exits 0. In a scratch copy of the ledgers where the note holding `for unread` is
  relabelled `TOOL-dWitnessedBar-90 S1`, it prints `NO NOTE 90 S9 for unread` and exits 1.
  Red when: an item's ledger clause passes on another item's line.
  fixture: a scratch copy of the build's ledgers under the run's scratch directory.
  figure: 17 is PINNED, the rows of §4's note table opening `90|` at rev-1.
  permission: the ledgers are written at the close.
- **AC4** — When §4's note check is fed the rows opening `92|S4|`, it prints `NOTES OK 5`. In a scratch
  copy of 88's ledger whose note under `- AC6` has lost its `resolve_python:` path, it prints
  `NO NOTE 92 S4 resolve_python:` and exits 1.
  Red when: a close that runs a derivation through a bare launcher records no resolved interpreter
  and passes.
  fixture: a scratch copy of the build's ledgers under the run's scratch directory.
  permission: the ledgers are written at the close.
- **AC5** — After this unit's pass commit,
  `grep -E ' dispatch · item [0-9a-f]+ TOOL-dWitnessedBar-92 ' memory/builds/dWitnessedBar/RUN.md`
  prints at least one line, and piped to `grep -cE ' memory/builds/dWitnessedBar/spec/?( |$)'` prints
  0. For each commit `git log --format=%H -E --grep='^Pass: TOOL-dWitnessedBar-(89|90)$' cdfbd1cf..HEAD`
  prints, each path under `memory/builds/dWitnessedBar/spec/` its diff names, other than that unit's
  own spec, reads the same through `GEN_REGION_AWK` from `tools/unattended/lib-unattended.sh` before
  and after. The number of paths read is recorded beside the verdict. `grep '^GENERATED_INDEXES='
  .unattended.conf` holds none of `memory/LIVE.md`, `memory/ledger` and `memory/backlog`. In a scratch
  clone with this unit's pass dispatched with `--writes memory/builds/dWitnessedBar/build/`, an edit
  to spec 89's `gen:spec-records` region alone is admitted by
  `bash tools/unattended/unattended.sh --check-commit <message file>`. An edit to its §6 body is
  refused with `stages paths outside the set it declared`. With
  `memory/builds/dWitnessedBar/spec/` added to `--writes`, the same body edit is admitted. When §4's
  note check is fed the rows opening `92|S5|` and `90|S13|`, it prints `NOTES OK 2`.
  Red when: a pass declares the spec directory, or a pass of unit 89 or 90 edits another unit's spec
  outside its gen regions.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  cost: a clone and three staged commits, at the close.
  permission: the ledger is written at the close.
- **AC6** — At the close, for each `n` from 1 to 13,
  `grep -cE "^- AC${n} " memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-89-*acceptance-ledger*`
  prints exactly 1. The same count prints exactly 1 for `AC2` in unit 87's ledger, for `AC6` and
  `AC18` in unit 88's, and for each `n` from 1 to 15 in unit 90's. In a scratch copy of 89's ledger
  with its `- AC4` answer removed and 90's notes kept, the count for 4 prints 0. In one where 90 S1's
  note is spelled `- AC4 — TOOL-dWitnessedBar-90 S1`, it prints 2.
  Red when: a unit-90 line opening `- AC<n>` stands in for 89's own answer.
  fixture: a scratch copy of the build's ledgers under the run's scratch directory.
  permission: the ledgers are written at the close.
- **AC7** — After this unit's pass commit, with `py` set by `resolve_python`,
  `"$py" tools/memory-tree/gen_build_index.py --write; echo "rc=$?"` prints `rc=0`, and
  `git status --porcelain --untracked-files=no -- memory/` then prints nothing. The same procedure
  with `py=false` prints `rc=1`, and the criterion reds. When §4's note check is fed the rows opening
  `92|S7|`, it prints `NOTES OK 1`.
  Red when: a launcher that never ran the generator leaves the porcelain empty and passes.
  permission: the ledger is written at the close.
- **AC8** — On the built tree, each of these three probes of the suite's text prints 1, and none runs
  the suite:
  `grep -c 'THE SHARD CONTRACT, both directions (TOOL-aShardedFloor-2)' tools/run-gates/run-gates.gov.test.sh`,
  `grep -c 'test_recall_floor.py from the payload' tools/run-gates/run-gates.gov.test.sh` and
  `grep -c '1565 s floor' tools/run-gates/run-gates.gov.test.sh`. When §4's note check is fed the rows
  opening `92|S9|`, it prints `NOTES OK 1`.
  Red when: a sweep by `grep -i floor` deletes a comment outside the assertion floor.
  figure: each count is PINNED at 1 over base `cdfbd1cf`.
- **AC9** — When §4's note check is fed the rows opening `92|S10|` and `90|S10|`, it prints
  `NOTES OK 2`, so 90 S10's note quotes `AC4 AC6 AC7 AC10 AC12` as the criteria with a pass half.
  Red when: 90 S10's note records 90 S10's own list, which gives 89 AC1 a pass half and 89 AC7 none.
  permission: the ledgers are written at the close.
- **AC10** — When §4's note check is fed the rows opening `90|S12|`, it prints `NOTES OK 4`, and no
  line carrying `TOOL-dWitnessedBar-90 S12` holds `on any commit touching`.
  Red when: the note states check 9's trigger by its effect and omits the deletion-only gap.
  permission: the ledger is written at the close.
- **AC11** — When §4's owner derivation runs on the built tree, it prints a non-zero length and a spec
  path and exits 0. In a scratch copy holding `tools/unattended/unattended.sh`,
  `tools/lib/resolve-python.sh`, `tools/check-spec-tokens.py` and `memory/builds/dWitnessedBar/`, it
  prints `TOKEN READER NOT FOUND` and exits 7 with `tools/check-spec-tokens.py` removed. It prints
  `SPEC UNREADABLE` and exits 8 with a README row repointed to a spec that does not exist. It prints
  `TOKEN READER FAILED` and exits 9 with an `extract_gates` that raises. It keeps 90 AC15's exits 3, 4
  and 6 on their stagings. When §4's note check is fed the rows opening `92|S12|`, it prints
  `NOTES OK 1`.
  Red when: a missing spec or token reader exits 1 with a traceback and no named line.
  fixture: a scratch copy under the run's scratch directory.
- **AC12** — When §4's note check is fed every row of §4's note table, it prints `NOTES OK 29` and
  exits 0. In a scratch copy of 89's ledger where 90 S2's note wraps `rec_sha="${_rg_v}"` onto the
  next line, it prints `NO NOTE 90 S2 rec_sha="${_rg_v}"` and exits 1.
  Red when: a note wrapped at the house width splits a token from its label and the record still
  reads as present.
  fixture: a scratch copy of the build's ledgers under the run's scratch directory.
  figure: 29 is PINNED, the rows of §4's note table at rev-1.
  permission: the ledgers are written at the close.

## 7. Gates

`run-gates gov canary` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms` · `memory hygiene`

`run-gates gov canary` and `testsuite counts (every bar self-test prints one)` are owed for the suite
S9 may restore a comment in; `run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS
at the close, which `SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf:40`). `recall floor` and
`recall floor arms` are owed for the ledgers under `memory/`. This unit adds no arm and moves none,
so it declares no new-arm line.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 90 is itself
  derived and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-90` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How are the ledger selectors made unique (id 3)?** Options: (a) a label per item,
  `TOOL-dWitnessedBar-90 S<k>`, read with the answer it sits under; (b) a token per item chosen from
  what that item writes, the report's first way. (b) holds only while no item quotes another's
  token, and 90 S3's line already quotes S2's. (a) is unique by construction and joins id 11's
  continuation-line spelling. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most
  feature-rich survivor.
  widens: none · relaxes: none
- **F3 — What answers the spec-directory declaration units 89 and 90 make before this unit
  builds (id 9)?** Options: (a) withdraw it going forward and read each of their pass commits for an
  edit outside a gen region; (b) withdraw it going forward only. Under (b), the widened grant those
  two passes may have held goes unread. (a) reads its one consequence. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the most feature-rich survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of unit 90: 7 MEDIUM and
  6 LOW findings, batched.

## 10. Reuse audit

Each item extends the seam its finding names. S2 reuses 90 AC1's clones and 89 S7's placement. S3,
S6 and S13 use the acceptance ledger of `memory/HYGIENE.md` "Acceptance ledger", whose continuation
lines `tools/memory-tree/check-memory-hygiene.sh:3158` already joins to the answer above. S5 names
the admission seam `--check-commit` already has, `check_gen_region_only`
(`tools/unattended/lib-unattended.sh:1137`) and `resolve_generated_indexes` (`:838`), and grants
nothing beside it. S7 and S12 adopt `resolve_python` (`tools/lib/resolve-python.sh`), the one
interpreter resolver, and S12 keeps `region` (`tools/unattended/unattended.sh:1310`).
`python tools/codebase-map/reuse_lookup.py "join a ledger note to the acceptance answer it sits under"`
ranked `note`, `join_aliases`, `read_join_state` and `resolve_answers`, none a reader that places a
line under the answer above it, so no existing seam fits beyond the ledger grammar and the seams
named above.

Recall terms used: `python tools/memory-recall/query.py "how does a later unit record a note beside another unit's acceptance answer without opening a second answer line" --terms "acceptance ledger continuation line answer label selector note superseded criterion check 23 wrapped token"`
