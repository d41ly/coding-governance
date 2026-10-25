# TOOL-dWitnessedBar-88 — the round-1 audit of units 79 to 84, 19 minors batched: quoted reasons answered, one return contract and pass-commit lookup, a derived owner on one line, a measure-keyed probe, arm spellings matched, hook directory guarded

**Status:** OPEN · rev-4 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 45 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-88-round10-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-88-round10-fix-return.md) | research | — |
| [2026-10-25-build-TOOL-dWitnessedBar-88-round10-h1-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-88-round10-h1-return.md) | research | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-88-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-88-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-88-2-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-88-2-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-88-round10-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-88-round10-fix-brief.md) | research | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-88-round10-h1-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-88-round10-h1-brief.md) | research | — |
| [2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 79 to 84
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md`)
exited CONVERGED with 22 confirmed findings: no BLOCKER; three HIGH, ids 1, 17 and 7, which
`TOOL-dWitnessedBar-85`, `-86` and `-87` take; and 19 minors. BUILD-METHOD M4 batches every MEDIUM
and LOW into one unit, or two only where they split into disjoint write sets by M6's clauses so that
both build concurrently. §4 "Why one unit" says why these stay one. Each finding is named by report id
and is its own scope item, including where the report merged ids into one item. The minors land on
units 76 to 84, so this unit repairs no single unit and builds above every unit in the build
(order 45).

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M1 | MEDIUM | 2 | unit 80 S3; units 74 and 76 S3, AC2, §7 | S1 |
| M1 | MEDIUM | 12 | unit 79 S3; unit 76 S3, AC3 | S2 |
| M2 | MEDIUM | 3 | unit 84 S13, AC13; unit 76 S2 | S3 |
| M3 | MEDIUM | 4 | unit 84 S6, S7, S10, AC6, AC7, AC10 | S4 |
| M4 | MEDIUM | 9 | unit 82 AC1; unit 83 S3; unit 84 AC3, AC17 | S5 |
| M5 | MEDIUM | 10 | unit 83 S1, AC1, §10 | S6 |
| M6 | MEDIUM | 11 | unit 82 S1; unit 83 AC1; unit 84 S14, AC17 | S7 |
| M7 | MEDIUM | 14 | unit 82 S1, §7; unit 83 S1; unit 84 S14, §7 | S8 |
| M8 | MEDIUM | 18 | unit 84 S2, S4, AC2 | S9 |
| M9 | MEDIUM | 19 | unit 84 S6, AC6, §8 F3 | S10 |
| M10 | MEDIUM | 21 | unit 84 S9, §4 | S11 |
| L1 | LOW | 6 | unit 83 §4, AC1 | S12 |
| L1 | LOW | 16 | unit 82 §4; unit 83 §4, AC1 | S13 |
| L2 | LOW | 5 | unit 84 AC10 | S14 |
| L3 | LOW | 13 | unit 80 S1, §3; unit 76 AC1; unit 77 S2; unit 84 S5 | S15 |
| L4 | LOW | 15 | unit 84 S7, §4 | S16 |
| L5 | LOW | 20 | unit 79 S2, S3 | S17 |
| L6 | LOW | 22 | unit 83 AC1; units 82 S1, 83 S1, 84 S14 | S18 |
| L7 | LOW | 23 | unit 81 S1, AC2, AC3 | S19 |

That is 11 MEDIUM and 8 LOW findings by raw id. Ids 2 and 12 share item M1, which is the medium grade
of the defect `TOOL-dWitnessedBar-87` takes as id 7. Ids 6 and 16 share item L1. Item M6 (id 11) and
item L6 (id 22) are one defect at two grades, and M7 (id 14) shares its placement rule.

## 2. Scope (IN)

- **S1** — id 2. Every reader of the reason unit 80 S3 stands in place of is answered. Unit 80's
  acceptance ledger beside AC2 carries one line quoting `it passed a value that lost its CR` and naming
  each spec that spells it with its answer: unit 74 S3, AC2 and New-arm line, answered by
  `TOOL-dWitnessedBar-81` S3; unit 76 S3, AC2 and New-arm line, answered by `TOOL-dWitnessedBar-87`
  S2; and the absent-variable case of both S3s, covered by each variant's own reason in
  `TOOL-dWitnessedBar-79` S3 and unit 80 S3. It names this unit. Observed by AC1.
- **S2** — id 12. The other-variable reason, per variant. The tail variant keeps unit 76 S3's
  `it named <other> whose CR arrived`, unchanged; the length variant prints S17's reason. At the close
  the main loop stages 76 AC3's break, a `check_canary_keys` that prints `rec_sha` whenever it prints
  `rec_fp`, in a scratch clone of the built tree. Unit 76's ledger beside AC3 records the two `rec_fp`
  lines it printed and names this unit. Observed by AC2.
- **S3** — id 3. One return contract for `check_canary_keys`. It returns 0 when it printed nothing; 1
  when it printed at least one variable and no call of `check_cr_reached` returned 2; and 2 when any
  call returned 2. The liveness loop requires, on each variant's mutant, return 1 and output exactly
  `<var>`, and on a 2 prints `TOOL-dWitnessedBar-84` S13's `could not be sourced or read (rc 2)`
  reason. Observed by AC3.
- **S4** — id 4. Unit 84's ledger obligations observed. The lines 84 S6, S7 and S10 require are each
  graded by this unit's AC4: unit 74's ledger beside AC3 names `TOOL-dWitnessedBar-84` S6; the ledgers
  of units 74 and 76 beside AC1 name `check_cr_reached` or `check_canary_keys` and
  `TOOL-dWitnessedBar-84`; unit 78's ledger beside AC8 names `_derive_case_keys`. Observed by AC4.
- **S5** — id 9. One pass-commit lookup. Every observation this build makes at a unit's pass commit,
  82 AC1, 83 S3 and AC3, 84 AC3 and AC17, and those of S7, S11 and S16 here, locates the commit with
  `build_commit` over `cdfbd1cf..HEAD`, the build folder `memory/builds/dWitnessedBar` and the conf's
  `GENERATED_INDEXES` and `SHARED_RECORDS`, with `tools/unattended/lib-unattended.sh` sourced, as
  `TOOL-dWitnessedBar-62` S16 rules. The `git log | grep` spelling of 82 AC1 and 84 AC3 is not used.
  Each ledger line answering those criteria carries the sha and the word `build_commit`. Observed by
  AC5.
- **S6** — id 10. The floor's owner, derived by the shipped readers. The owner is the last unit of
  the build README's `gen:build-units` region, the unit set and order `--plan` reads and
  `gen_build_index.py` sorts with unordered units last, whose spec's Gates section, as
  `extract_gates` cuts it, holds a column-0 line opening
  `New arm: tools/run-gates/run-gates.gov.test.sh`, the rule `scan_arm_covers` reads. The command is
  §4's owner derivation. Unit 83's ledger beside AC1 records the owner it names beside the one 83
  AC1's pipeline names. Observed by AC6.
- **S7** — id 11. The owner line's side, and the last restatement. This unit adds a gov-canary arm
  (S17), so S6 names it as the owner at the close. Its builder restates `FLOOR_ASSERTIONS` absolutely,
  at the count the suite executes on a passing run at this pass, by `TOOL-dWitnessedBar-82` S1's rule.
  The comment naming `TOOL-dWitnessedBar-88` is the one line directly above `FLOOR_ASSERTIONS=<n>`, and
  no earlier owner sits on that line. The ledgers of unit 82 beside AC1, unit 84 beside AC17 and unit
  85 beside AC2 each record the line `grep -B1` read above the constant at their pass commits.
  Observed by AC7.
- **S8** — id 14. The assignment line is bare. `FLOOR_ASSERTIONS=<n>` carries nothing after the
  number, which `tools/check-testsuite-counts.sh:94` reads with `^FLOOR_ASSERTIONS=[0-9]+$`. This unit's
  §7 names `testsuite counts (every bar self-test prints one)`, the leg §7 of units 82 and 84 omit, and
  the ledgers of unit 82 beside AC1 and unit 84 beside AC17 name that leg. Observed by AC8.
- **S9** — id 18. The single-copy probe keyed on the measure. §4's measure probe prints every line of
  the suite outside `check_cr_reached`'s body that holds a byte measure, `wc -c`, `tail -c`, `od`,
  `cut -c`, a `${#` expansion or a `: -1}` slice, together with a `rec_` name, an indirect `${!`
  expansion or a variable `CANARY_KEYS` names, the names derived from the `CANARY_KEYS` line. Unit
  84's ledger beside AC2 names this probe as the whole-suite single-copy observation. Observed by AC9.
- **S10** — id 19. The `<key>)` edit admits every spelling bash reads the same. The liveness loop's
  match is `\(<key>)[[:space:]]*<var>=\)"\{0,1\}\${\{0,1\}_rg_v}\{0,1\}"\{0,1\}`, with an unescaped `{`
  after `\$`, so `$_rg_v`, `"$_rg_v"`, `${_rg_v}`, `"${_rg_v}"` and an aligned arm are each edited in
  one line with their spacing kept. The replacement is written unquoted. Unit 84's ledger beside AC6
  names this match as the one the loop uses. Observed by AC10.
- **S11** — id 21. The canary's guard covers its reads under `.githooks/`. The `run-gates gov canary`
  row's `guard` in `tools/gate-legs.json` gains `.githooks/`, after its existing entries, because the
  reverse shard-contract block opens every `.sh` argv of the manifest under `$ROOT` and four of them
  sit there. Nine legs carry that entry today, so it is broad over `BROAD_LEG_FLOOR` and the spec-tokens
  join owes the canary on no spec for it. The two other such reads,
  `skills/session-kickoff/manifest-check.sh` and `skills/session-kickoff/manifest-check.test.sh`, take
  one ask row in `memory/builds/dWitnessedBar/BACKLOG.md` under the family's next free id, naming
  `DEPL-aScoutedSeam-1`, `KICK-aScoutedSeam-1` and `TOOL-dWitnessedBar-27`, the live specs listing
  them under Files touched, with a `SEV` disposition line. Unit 78 AC5 and unit 84 AC16 stage a
  manifest lacking the hook entry, which the built guard's `.githooks/` still trips, so each is
  observed at its own unit's pass commit by S5's lookup and recorded there. Observed by AC11.
- **S12** — id 6. The New-arm list's length, recorded. Unit 83's ledger beside AC1 records the
  length 83 AC1's pipeline prints at the close, beside the 20 that 83 §4 and its AC1 figure line
  state and the 24 it printed at `162f4ec8c`, naming units 79, 80, 82 and 84 as the specs that 20
  missed. Observed by AC12.
- **S13** — id 16. The figure, restated where this round measured it. §4 Evidence of this spec pins
  the list's length at the commit that adds this spec, with the pipeline that re-derives it, and
  names units 79, 80, 82, 84, 85 and this unit as the additions since unit 82 §4's 20. Observed by
  AC13.
- **S14** — id 5. Callers counted by their prefix argument. 84 AC10's caller count is read as
  `grep -cE '^[^#]*_derive_case_keys [^ ]+ (rec_|bg_)'`, which counts a call whatever the quoting of
  its first argument and skips a comment line. Unit 84's ledger beside AC10 records it printing 2.
  Observed by AC14.
- **S15** — id 13. The tail variant's text recorded where the earlier text is named. Unit 76's
  ledger beside AC1 records that `TOOL-dWitnessedBar-80` S1 writes `${_rg_v%?}x` where 76 S3 wrote
  `${_rg_v%?}`, and names 79 AC1 and 80 AC1 as the observation of the current length and tail
  variants on the `fingerprint` arm. Unit 72's ledger beside AC1, where 77 S2 and 84 S5 record the
  staged `fingerprint` variant, names that variant as `${_rg_v%?}x`. Observed by AC15.
- **S16** — id 15. The render's whole output named. Unit 84's ledger beside AC7 names every file under
  `memory/map/generated/` that unit 84's pass commit changed, as
  `git show --stat --format= <sha> -- memory/map/generated/` lists them, since
  `tools/codebase-map/gen_map.py --write` renders the whole directory and 84's Files touched names
  `symbols.json` alone. Observed by AC16.
- **S17** — id 20. The length variant's other-variable reason. When the length variant's mutant
  output holds `<var>` and another name, the arm prints `TOOL-dWitnessedBar-74` S3's line for `<var>`
  with the reason `the length variant named <other> whose CR arrived`, sets `fail=1`, leaves unit 66
  S2's assertion uncounted as 79 S3's other reasons do, and the variant adds nothing to `a` under
  `TOOL-dWitnessedBar-85` S1. Observed by AC17.
- **S18** — id 22. The owner read from one line. 83 AC1's comment is read as
  `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1`, and that line names
  the owner S6 derives and no other unit id. Unit 83's ledger beside AC1 records the line. Observed by
  AC18.
- **S19** — id 23. One platform rule for unit 81's records. Unit 81's two breaks are owed on a
  Windows node, the rule 81 S1 and AC2 state, and the records 81 AC3 grades take the same rule: unit
  76's ledger lines that 81 S4 writes carry a `uname -s` beginning `MINGW` or `MSYS`. A close on any
  other node records each break beside 81 AC2's and AC3's ledger lines as owed, with the `uname -s`
  it ran under, and files one ask row in `memory/builds/dWitnessedBar/BACKLOG.md` naming the Windows
  re-run. Observed by AC19.

## 3. Non-goals (OUT)

- Rewording the spec text of units 76 to 84. Each item is closed by what this pass builds or
  observes, and a claim or criterion it answers is answered in that unit's acceptance ledger by name,
  as `TOOL-dWitnessedBar-78` §3 does for units 68 to 73.
- The canary's guard entries for `skills/session-kickoff/manifest-check.sh` and its test. S11 files
  the ask that carries them, because an exact entry would owe the canary on three live specs, two of
  them in a build with no `BACKLOG.md`; §8 F3.
- The left-shift gates the report names: the checklist entries, a hygiene check that re-runs a DERIVED
  figure's pipeline, a spec-tokens check that reds a `git log | grep` pass-commit lookup, a spec-tokens
  check for a ledger obligation no criterion greps, and a gate leg deriving a held suite's `$ROOT`
  reads. No clause of this build names them. S3's contract, S9's probe, S10's match and S11's guard
  are the regressions this batch builds.
- The per-variant count, the coverage records and 76 AC2's own break, which are
  `TOOL-dWitnessedBar-85`'s, `-86`'s and `-87`'s.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-76` — S2's `check_canary_keys`, S3's other-variable reason and the ledger lines for AC1 and AC3, which S2, S3 and S15 extend or answer (ids 3, 12 and 13)
- **consumes-from** `TOOL-dWitnessedBar-77` — S2's staged `fingerprint` variant, which S15 names by its current text (id 13)
- **consumes-from** `TOOL-dWitnessedBar-78` — AC5's manifest lacking the hook entry and the ledger line for AC8, which S4 and S11 observe at its pass commit or grade (ids 4 and 21)
- **consumes-from** `TOOL-dWitnessedBar-79` — the length variant and S3's reasons, which S2 and S17 extend with the other-variable case (ids 12 and 20)
- **consumes-from** `TOOL-dWitnessedBar-80` — S3's tail reason and S1's replacement text, whose readers S1 and S15 answer (ids 2 and 13)
- **consumes-from** `TOOL-dWitnessedBar-81` — S1, AC2, AC3 and S4's records, which S19 holds to one platform rule (id 23)
- **consumes-from** `TOOL-dWitnessedBar-82` — S1's restatement rule, AC1 and its §4 figure, which S5, S7, S8 and S13 locate, place or restate (ids 9, 11, 14 and 16)
- **consumes-from** `TOOL-dWitnessedBar-83` — S1's owner, AC1's pipeline and comment read, and S3's pass-commit record, which S5, S6, S12 and S18 derive, record or read (ids 6, 9, 10 and 22)
- **consumes-from** `TOOL-dWitnessedBar-84` — S2's probe, S6's match, S7's render, S9's guard, S13's return codes, S14's restatement and AC3, AC10, AC16 and AC17, which S3 to S5, S7 to S11, S14 and S16 widen, count or answer (ids 3, 4, 5, 9, 11, 14, 15, 18, 19 and 21)
- **consumes-from** `TOOL-dWitnessedBar-85` — S1's per-variant count and S2's restated floor, which S17's reason leaves uncounted and S7 restates after (ids 11, 14, 20 and 22)
- **consumes-from** `TOOL-dWitnessedBar-87` — the answer to 76 AC2's own break, which S1 names as the answer for unit 76's readers (id 2)
- **hands-off** `TOOL-dWitnessedBar-89` — S3's contract, S6's derivation, S7's restatement, S10's match, S11's and S19's ask rows, AC13 and AC19, which unit 89 completes (ids 1, 3, 4, 7, 8, 10, 12 and 14 of the round-1 spec audit of units 85 to 88)
- **hands-off** `TOOL-dWitnessedBar-90` — S6's owner rule, which names unit 90 the floor's owner, and the owner derivation S6, AC6 and AC18 run, which unit 90 makes name each failure (ids 13 and 21 of the round-1 spec audit of unit 89)
- **hands-off** `TOOL-dWitnessedBar-92` — AC6's and AC18's close-time runs of the owner derivation and their ledger answers, which unit 92 records with the resolved interpreter and whose derivation it replaces with one naming every exit (ids 4 and 14 of the round-1 spec audit of unit 90)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The suite half, S3, S7, S8,
S10 and S17, writes `tools/run-gates/run-gates.gov.test.sh`. S11 writes `tools/gate-legs.json`, which
the suite reads as its manifest, M6 clause 2. The ledger items record the arm runs and pass commits
the suite half and S11 produce, so each reads the other half's output as an acceptance input, clause
2 again, and S11 and S19 both write `memory/builds/dWitnessedBar/BACKLOG.md`, a shared record under
clause 3. No split leaves two disjoint write sets, and dispatch is strictly sequential, a shared order
included (`tools/workflows/unattended-build.js:76`), so a split would buy no concurrency. One unit
holds all 19 findings, as `TOOL-dWitnessedBar-84` §4 held its 16.

### Evidence

- `tools/run-gates/run-gates.gov.test.sh:91-95`, read on 2026-10-25: `a=0`, two comment lines naming
  `TOOL-aShardedFloor-2`, `FLOOR_ASSERTIONS=16`, then `# Raised 15 -> 16 by TOOL-dDerivedDocket-23`
  below the constant. `:441-457` hold the reverse shard-contract block, which opens each manifest `.sh`
  argv under `root`.
- `tools/check-testsuite-counts.sh:94` requires `^FLOOR_ASSERTIONS=[0-9]+$`, and the leg that runs it,
  `testsuite counts (every bar self-test prints one)`, has no guard (`tools/gate-legs.json`).
- `tools/gate-legs.json:1184-1196`: the gov canary's guard is `{prefix}/run-gates/` and
  `{prefix}/gate-legs.json`. A walk of the manifest on 2026-10-25 found six `.sh` argv outside the
  tool root: `.githooks/pre-commit.test.sh`, `.githooks/pre-push.runlog.test.sh`,
  `.githooks/pre-push.test.sh`, `.githooks/straggler-guard.test.sh`,
  `skills/session-kickoff/manifest-check.sh` and `skills/session-kickoff/manifest-check.test.sh`; and
  nine legs whose guard carries `.githooks/`.
- `tools/check-spec-tokens.py:331` sets `BROAD_LEG_FLOOR = 5`. `derive_tripped_legs` (`:625-634`)
  returns one guard per leg, the first that trips in manifest order, so `.githooks/` placed after the
  exact `.githooks/pre-push` entry leaves `--legs-for .githooks/pre-push` printing that entry.
- Live specs naming `skills/session-kickoff/manifest-check.sh` and its test under Files touched, read
  on 2026-10-25: `DEPL-aScoutedSeam-1` and `KICK-aScoutedSeam-1` (SPECCED) and `TOOL-dWitnessedBar-27`
  (OPEN). `memory/builds/aScoutedSeam/` holds no `BACKLOG.md`.
- `build_commit` (`tools/unattended/lib-unattended.sh:1186`) matches the id as a whole token through
  `read_attribution_tokens` (`:1149`), which reads a `Pass: none` trailer as naming no unit, and skips
  a commit touching only the build folder, the generated indexes or the shared records.
- `tools/workflows/unattended-build.js:607-612` sorts by `order`, an unordered unit at `1e9`, then by
  id string. `tools/memory-tree/gen_build_index.py:1553` sorts the `gen:build-units` region by
  `(order is None, order, id)`, the same order, and `verb_plan` in `tools/unattended/unattended.sh`
  takes its unit set and order from that region. `extract_gates` (`tools/check-spec-tokens.py:495`)
  cuts §7 by heading text, and `scan_arm_covers` (`:1322`) reads a `New arm:` line only at column 0
  inside it.
- Probed on this node on 2026-10-25 (GNU sed 4.9, GNU bash 5.3.9 `x86_64-pc-cygwin`): S10's match with
  the replacement `${_rg_v:1}`, and again with `${_rg_v%?}x`, rewrote `sha) rec_sha=$_rg_v`,
  `"$_rg_v"`, `${_rg_v}`, `"${_rg_v}"` and `sha)   rec_sha=$_rg_v` in one line each, keeping the
  alignment, and left the `fingerprint)` arm alone. The canary's `sed 's/%[$].[\]r.}/}/'` changed no
  line of the tail-edited result.
- The same day, §4's measure probe printed the planted `${!v}` line, the planted `$rec_fp` line and a
  `${#rec_sha}` line from a scratch file, skipped a measure inside `check_cr_reached`'s body and a
  `$bg_x` measure, and printed nothing over the suite as it stands.
- `tools/codebase-map/gen_map.py:143-151` renders `inventories.json`, `MAP.md`, `CARDS.md` and
  `symbols.json` under `memory/map/generated/`.
- New-arm list: 83 AC1's pipeline printed 24 specs at `162f4ec8c`, from unit 12 at order 5 to unit 84
  at order 44. With units 85 and 88, which carry a gov-canary New-arm line, it prints 26 at the commit
  that adds this spec, the last line naming this spec at order 45. PINNED at that commit; S13's AC
  re-derives it there.
- §4's owner derivation, run on 2026-10-25 over the README region rendered at `162f4ec8c`, printed 24
  and `spec/2026-10-25-spec-TOOL-dWitnessedBar-84.md`, agreeing with 83 AC1's pipeline there; the
  region names units 85 to 88 once the index is re-rendered.

### The owner derivation

Run from the repository root; it prints the list's length, then the owner's spec path.

```bash
python -c "import importlib.util as u, re; s = u.spec_from_file_location('cst', 'tools/check-spec-tokens.py'); m = u.module_from_spec(s); s.loader.exec_module(m); b = 'memory/builds/dWitnessedBar/'; r = open(b + 'README.md', encoding='utf-8').read().split('<!-- gen:build-units -->')[1].split('<!-- /gen:build-units -->')[0]; o = [p for p in re.findall(r'\]\((spec/[^)]+)\)', r) if any(l.startswith('New arm: tools/run-gates/run-gates.gov.test.sh') for l in (m.extract_gates(open(b + p, encoding='utf-8').read()) or '').splitlines())]; print(len(o)); print(o[-1] if o else 'NO OWNER')"
```

### The measure probe

```bash
F=tools/run-gates/run-gates.gov.test.sh
awk -v keys="$(sed -n 's/^CANARY_KEYS=//p' "$F" | grep -oE ':[A-Za-z_][A-Za-z0-9_]*' | tr -d : | tr '\n' ' ')" \
  'BEGIN{n=split(keys,k," ")} /^check_cr_reached\(\)/,/^}/{next} {m=($0 ~ /wc -c|tail -c|od |cut -c|[$][{]#|: -1[}]/); v=($0 ~ /[$][{]!|rec_[a-z_]+/); for(i=1;i<=n;i++) if(index($0,k[i])) v=1; if(m && v) print FNR": "$0}' "$F"
```

### Inventory

Minted: `check_canary_keys`'s return codes 0 and 1 beside 84 S13's 2; S17's reason
`the length variant named <other> whose CR arrived`; S10's match; the `.githooks/` guard entry; S11's
ask row and, on a close off Windows, S19's; the restated `FLOOR_ASSERTIONS` and its owner line. No
function, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes. S11 widens when one leg runs and narrows nothing.

### Rollout

Live at landing, at order 45, after every other unit of the build, the last of them
`TOOL-dWitnessedBar-84`, `-85` and `-86` at order 44. S1, S2, S4, S5, S7, S8, S11, S12, S14 to S16, S18
and S19 are answered in other units' ledgers at the close.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `tools/gate-legs.json`
- `memory/builds/dWitnessedBar/BACKLOG.md`
- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **Two batches, suite half and the rest.** §4 "Why one unit".
- **Read the owner with `grep -A1` below the constant, the finder's suggestion for id 11.** The fixes
  for ids 14 and 22 both put the comment on its own line directly above, and only the line above
  serves all three.
- **Derive the owner from the spec headers with `sed` and `sort`, as 83 AC1 does.** It sorts an
  unordered unit first where the dispatcher sorts it last, and it reads a `New arm:` line anywhere in a
  spec; that is the second copy of the build order 83's own alternatives reject.

## 5. Production-readiness checklist

- security — no new write path. S11 and S19 write only ask rows in this build's `BACKLOG.md`.
- perf / scale — S11 runs the gov canary on a change under `.githooks/` once GATE_SELFTESTS is set;
  S3 adds no call; the close's clones run once.
- error / empty / loading states — S3 names a read failure apart from a failed check; S17 names an
  over-reporting check; the owner derivation prints `NO OWNER` on an empty list.
- observability — S17's reason names the variant and the other variable; the owner line names its
  unit and is read from one line.
- risks — S9's probe can print a legitimate measure of a key's value outside the function; its
  Red-when is a planted copy, and a builder who finds such a line routes it through
  `check_cr_reached`. S10's match also admits an unbalanced quote or brace, which bash would refuse
  before the loop runs.
- testing — AC2, AC3, AC5, AC6, AC9 to AC11, AC13, AC14 and AC17 by probe, fixture or scratch clone;
  the rest by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'lost its CR' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-80*acceptance-ledger*`
  runs at the close, it prints one line naming `TOOL-dWitnessedBar-74`, `TOOL-dWitnessedBar-76`,
  `TOOL-dWitnessedBar-81`, `TOOL-dWitnessedBar-87` and `TOOL-dWitnessedBar-88`.
  Red when: a spec still quotes the reason unit 80 stands in place of with no answer recorded for it.
  permission: the ledger is written at the close.
- **AC2** — In a scratch clone of the built tree whose suite copy has `check_canary_keys` print
  `rec_sha` whenever it prints `rec_fp`, the arm prints a `rec_fp` line holding
  `(the length variant named rec_sha whose CR arrived)` and one holding
  `(it named rec_sha whose CR arrived)`. When
  `grep -n 'AC3' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-76*acceptance-ledger*` runs, it
  prints both lines, each with `TOOL-dWitnessedBar-88`.
  Red when: 76 AC3's break reaches a variant for which no reason is defined.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When a probe cuts `check_cr_reached`, `check_canary_keys` and the `CANARY_KEYS` definition
  out of the suite file with `awk '/^check_canary_keys\(\)/,/^}/' tools/run-gates/run-gates.gov.test.sh`
  and its like for the other two, sources them, and calls
  `check_canary_keys` on the length variant's `sha` mutant, built as 79 AC1 builds it, over the AC12
  record, it returns 1 and prints exactly `rec_sha`. On the unedited cut it returns 0 and prints
  nothing, and with a `<file>` that does not exist it returns 2.
  Red when: the loop accepts a 0 with output, or a 1 from a direct `check_cr_reached` call that never
  tests which key was named.
  fixture: the AC12 record, which `TOOL-dWitnessedBar-68` S1 and `TOOL-dWitnessedBar-67` S2 build.
- **AC4** — When `grep -n 'AC3' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-74*acceptance-ledger*`
  runs at the close, a printed line names `TOOL-dWitnessedBar-84` S6; when
  `grep -n 'AC1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-7[46]*acceptance-ledger*` runs,
  each ledger prints a line naming `check_cr_reached` or `check_canary_keys` with
  `TOOL-dWitnessedBar-84`; and `grep -n 'AC8' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-78*acceptance-ledger*`
  prints a line naming `_derive_case_keys`.
  Red when: unit 74 AC3 stands red beside 84 AC6 with no ledger line reconciling them.
  permission: the ledgers are written at the close.
- **AC5** — In a fixture repository under `%TEMP%/<short-name>` holding a commit that touches the
  path the `git log` below names, with a subject naming `TOOL-tFix-1` and the trailer
  `Pass: none`, then a second such commit with no trailer, `build_commit <base>..HEAD TOOL-tFix-1 memory/builds/tFix "" ""`
  prints the second commit's sha, while the first line of
  `git log --reverse --format='%H %s' -- tools/run-gates/run-gates.gov.test.sh | grep 'TOOL-tFix-1'`
  names the first. At the close,
  `grep -n 'build_commit' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-8[234]*acceptance-ledger*`
  prints a line holding a forty-hex sha in each of the three ledgers.
  Red when: a records or fold commit naming the id is graded as the unit's pass.
  fixture: a fixture repository under `%TEMP%/<short-name>`.
- **AC6** — When §4's owner derivation runs at the close, it prints a non-zero length and an owner
  path, and `grep -n 'AC1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-83*acceptance-ledger*`
  prints a line holding that owner's id and `TOOL-dWitnessedBar-88`. In a scratch clone holding a
  planted spec with no `order` verb whose §7 carries a gov-canary `New arm:` line, after
  `python tools/memory-tree/gen_build_index.py --write` there, the derivation names the planted spec
  while 83 AC1's pipeline names another; a planted spec whose `New arm:` line sits in §4 is not listed.
  Red when: the owner differs from the unit the dispatcher builds last among those adding an arm.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
- **AC7** — At this unit's pass commit, by S5's lookup, in a scratch clone,
  `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1` prints a comment naming
  `TOOL-dWitnessedBar-88` and no other unit id, and the arm prints `PASS (<n> assertions)` with `<n>`
  equal to the value. When `grep -n 'grep -B1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-8[245]*acceptance-ledger*`
  runs at the close, each of the three ledgers prints a line holding the comment it read.
  Red when: the last arm sits above the floor, or an owner comment sits where the read cannot see it.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  figure: both numbers are DERIVED at observation time.
  permission: the arm's run is the main loop's, at the close.
- **AC8** — When `grep -cE '^FLOOR_ASSERTIONS=[0-9]+$' tools/run-gates/run-gates.gov.test.sh` and
  `grep -c '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh` run on the built tree, each prints
  1, and `grep -n 'testsuite counts' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-8[24]*acceptance-ledger*`
  prints a line in each ledger naming `TOOL-dWitnessedBar-88`.
  Red when: a comment trails the number and the counts leg reds at the close with no spec naming it.
  permission: the ledgers are written at the close.
- **AC9** — When §4's measure probe runs on the built tree it prints nothing. Over a scratch copy
  holding `[ "$(printf %s "${!v}" | wc -c)" -eq 41 ]` inside the liveness loop it prints that line, and
  over one holding `[ "$(printf %s "$rec_fp" | wc -c)" -eq 41 ]` outside `check_cr_reached` it prints
  that line. `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-84*acceptance-ledger*`
  prints a line naming `TOOL-dWitnessedBar-88`.
  Red when: a second copy of the comparison in an indirect spelling stands with the probe silent.
  fixture: scratch copies under `%TEMP%/<short-name>`.
- **AC10** — When a probe applies S10's match for `sha` with `${_rg_v:1}` to the function cut by
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` and to scratch copies of it whose `sha)` arm
  reads `rec_sha="$_rg_v"`, `rec_sha=${_rg_v}`, `rec_sha="${_rg_v}"` and `sha)   rec_sha=$_rg_v`, each
  `diff` counts one changed line. In scratch clones whose `.githooks/pre-push` spells the arm
  `rec_sha=${_rg_v}` and `sha)   rec_sha=$_rg_v`, the arm prints no line holding
  `variant changed 0 lines`. `grep -n 'AC6' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-84*acceptance-ledger*`
  prints a line naming `TOOL-dWitnessedBar-88`.
  Red when: a braced or aligned arm, which bash reads the same, stalls the liveness loop.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC11** — When `python tools/check-spec-tokens.py --legs-for .githooks/pre-push.test.sh` runs on the
  built tree it prints a line holding `run-gates gov canary <- .githooks/ [`, and
  `--legs-for .githooks/pre-push` prints a line holding `run-gates gov canary <- .githooks/pre-push`.
  `grep -n 'manifest-check' memory/builds/dWitnessedBar/BACKLOG.md` prints an ask row naming
  `DEPL-aScoutedSeam-1`, `KICK-aScoutedSeam-1` and `TOOL-dWitnessedBar-27`. When
  `grep -n 'AC5' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-78*acceptance-ledger*` and
  `grep -n 'AC16' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-84*acceptance-ledger*` run at
  the close, each prints a line holding `build_commit`.
  Red when: an edit adding `SHARD_ARITY=` to a suite under `.githooks/` leaves the gov canary
  unselected and its stale green reused.
  permission: the ledgers are written at the close.
- **AC12** — When `grep -n 'AC1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-83*acceptance-ledger*`
  runs at the close, a printed line holds the length derived at the close, `162f4ec8c` and
  `TOOL-dWitnessedBar-88`.
  Red when: the close compares the list against the stale 20 and reads the difference as drift.
  figure: the length is DERIVED at the close.
  permission: the ledger is written at the close.
- **AC13** — In a scratch clone checked out at the commit
  `git log --diff-filter=A --format=%H -1 -- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-88.md`
  names, 83 AC1's list pipeline prints as many lines as §4 Evidence states, the last naming this spec
  at order 45.
  Red when: the recorded figure disagrees with its own pipeline at the commit it is pinned to.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  figure: PINNED at that commit; 26 when this spec was written.
- **AC14** — When `grep -cE '^[^#]*_derive_case_keys [^ ]+ (rec_|bg_)' tools/run-gates/run-gates.gov.test.sh`
  runs on the built tree it prints 2, and it prints 2 again over a scratch copy holding an extra
  comment line `# _derive_case_keys "$cut" rec_` and over one whose calls pass the cut unquoted.
  `grep -n 'AC10' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-84*acceptance-ledger*` prints a
  line naming `TOOL-dWitnessedBar-88`.
  Red when: the count depends on how the first argument is quoted, or counts a comment.
  fixture: scratch copies under `%TEMP%/<short-name>`.
- **AC15** — When `grep -n '_rg_v%?}x' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-76*acceptance-ledger*`
  runs at the close it prints an AC1 line naming `TOOL-dWitnessedBar-79` AC1, `TOOL-dWitnessedBar-80`
  AC1 and `TOOL-dWitnessedBar-88`, and the same grep over unit 72's ledger prints an AC1 line naming
  `TOOL-dWitnessedBar-88`.
  Red when: a ledger names a variant text the suite no longer holds as the one staged.
  permission: the ledgers are written at the close.
- **AC16** — When `grep -n 'AC7' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-84*acceptance-ledger*`
  runs at the close, a printed line names each file
  `git show --stat --format= <sha> -- memory/map/generated/` lists for unit 84's pass commit, and
  `TOOL-dWitnessedBar-88`.
  Red when: the render rewrites a generated file no record names.
  permission: the ledger is written at the close.
- **AC17** — In a scratch clone of the built tree whose suite copy's `check_canary_keys` prints every
  `CANARY_KEYS` variable whenever any check fails, the arm prints
  `gov-canary: the rec_sha byte check was not seen red on its liveness variant (the length variant named rec_fp whose CR arrived)`
  and exits non-zero.
  Red when: an over-reporting check reaches the length variant with no reason defined.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC18** — When `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1 | grep -oE 'TOOL-[A-Za-z]+-[0-9]+' | sort -u`
  runs on the built tree, it prints exactly the id of the owner §4's derivation names, and
  `grep -n 'grep -B1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-83*acceptance-ledger*`
  prints a line holding that id.
  Red when: a stale owner sits in the window, or the owner line sits below the constant.
  permission: the ledger is written at the close.
- **AC19** — When `grep -n 'TOOL-dWitnessedBar-81' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-7[46]*acceptance-ledger*`
  runs at the close, every printed line holds a `uname -s` value beginning `MINGW` or `MSYS`, or the
  word `owed` with the id of an ask row in `memory/builds/dWitnessedBar/BACKLOG.md`.
  Red when: unit 76's ledger accepts a break from a node unit 74's would refuse.
  permission: the ledgers are written at the close.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selfcheck` · `spec tokens (a spec's own names resolve)` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms` · `memory hygiene`

`run-gates canary`, `run-gates gov canary` and `measure-legs selftest` are owed for
`tools/gate-legs.json`; `recall floor` and `recall floor arms` for the paths under `memory/`.
`govkit selfcheck` grades S11's entry's class, `spec tokens (a spec's own names resolve)` reads it in
its guards join, and `testsuite counts (every bar self-test prints one)` reads the assignment line S7
and S8 write. The held legs run only when the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC2 AC10 AC17 · the length variant's other-variable reason and the widened `<key>)` match, staged red by a scratch suite whose `check_canary_keys` prints every variable on any failure (reaches `the length variant named rec_fp whose CR arrived`) and by a match that admits one spelling (reaches `variant changed 0 lines` on a braced arm) · FLOOR_ASSERTIONS restated absolutely by S7, the last restatement, its owner the unit S6 derives

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. Units 76 to 85 are
  themselves derived and carry no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which reason does each variant print when another variable is named (ids 12 and 20)?**
  Options: (a) the length variant prints `the length variant named <other> whose CR arrived` and the
  tail variant keeps unit 76 S3's `it named <other> whose CR arrived`, id 20's corrected fix; (b) both
  keep 76 S3's reason, id 12's fix; (c) both print a variant-named reason. (b) prints one line twice for
  one key, so 76 AC3's red cannot say which variant over-reported, and fails AC2's distinct lines;
  veto 1 discards it. (c) changes the tail variant's line, so 76 AC3, which quotes
  `it named rec_sha whose CR arrived`, would need its own answer for a change nothing requires; it
  satisfies fewer criteria than (a). RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most
  feature-rich survivor.
  widens: none · relaxes: none
- **F3 — Which guard entries close the canary's reads outside the tool root (id 21)?** Options: (a)
  `.githooks/`, with the two `skills/session-kickoff/` reads carried by an ask row, the report's
  corrected fix; (b) the four exact `.sh` paths under `.githooks/`; (c) ask rows only. (b) is a typed
  copy of the manifest's argv list, which misses the next `.sh` a leg adds under `.githooks/`, the class
  the report names, so it fails AC11's Red-when for that suite; veto 1 discards it. (c) leaves the
  stale green the finding describes, failing AC11; veto 1 discards it. An exact entry for the
  `skills/session-kickoff/` reads is narrow, so the spec-tokens join would owe the canary on two
  SPECCED specs of a build with no `BACKLOG.md` and on audited `TOOL-dWitnessedBar-27`, which this run
  may not edit; that half takes the ask, as 84 §8 F2 did for the charter. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the one survivor; its follow-up is S11's ask row.
  widens: none · relaxes: none
- **F4 — Which platform rule do unit 81's two records take (id 23)?** Options: (a) a Windows node for
  both, with a close elsewhere recording the breaks as owed and filing an ask; (b) any `uname -s` for
  both. (b) accepts a record 81 AC2 refuses as written, since AC2 requires `MINGW` or `MSYS`; veto 1
  discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one survivor; its follow-up is
  S19's ask row, filed only off Windows.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 79 to 84: 11
  MEDIUM and 8 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-89, the minors batch of the round-1 spec audit of units 85 to 88;
  nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-90, the minors batch of the round-1 spec audit of unit 89; nothing else
  moved.
- rev-4 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-92, the minors batch of the round-1 spec audit of unit 90; nothing else
  moved.

## 10. Reuse audit

Each item extends the seam its finding names. S3 extends `check_canary_keys` and 84 S13's return codes.
S5 calls `build_commit` (`tools/unattended/lib-unattended.sh:1186`), which
`python tools/codebase-map/reuse_lookup.py "which commit built a unit"` ranked as a SEAM, as
`TOOL-dWitnessedBar-62` S16 rules. S6 reads the `gen:build-units` region `gen_build_index.py` renders
and `--plan` reads, with `extract_gates` and the column-0 rule of `scan_arm_covers`. S9 widens 84 S2's
probe; S10 widens the liveness loop's existing `<key>)` edit; S11 adds an entry to the existing guard
and files an ask row as `TOOL-dWitnessedBar-84` S9 does. The ledger items use the acceptance ledger of
`memory/HYGIENE.md` "Acceptance ledger". S7's restatement follows `TOOL-dWitnessedBar-82` S1's rule.
`python tools/codebase-map/reuse_lookup.py "derive build order and the last unit declaring an arm from spec headers"`
ranked `arm`, `build`, `units`, `armed` and `build_commit`, none a reader of build order beyond the
region and readers named above, so no existing seam fits beyond those.

Recall terms used: `python tools/memory-recall/query.py "how does a gate's assertion floor see a liveness variant that is no longer there" --terms "canary liveness variant counted FLOOR_ASSERTIONS restated floor owner deleted arm seen red increment"`
