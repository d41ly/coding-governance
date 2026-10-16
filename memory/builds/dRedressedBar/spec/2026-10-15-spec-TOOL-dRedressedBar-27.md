# TOOL-dRedressedBar-27 — hygiene check 23 green by evidence: this build's eight missing acceptance ledgers written, and the base's 37 foreign ledger lines put in a legal form

**Status:** CLOSED · rev-2 · 2026-10-16 · node d · Tier-1 · base ebce889c · streams tooling · order 21 · ratified 2026-10-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-16-build-TOOL-dRedressedBar-27-1-set-aside-work.md](../build/2026-10-16-build-TOOL-dRedressedBar-27-1-set-aside-work.md) | research | — |
| [2026-10-16-build-TOOL-dRedressedBar-27-2-acceptance-ledger.md](../build/2026-10-16-build-TOOL-dRedressedBar-27-2-acceptance-ledger.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-27-1-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-27-1-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-27-brief.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-27-brief.md) | research | — |
| [2026-10-16-prompt-TOOL-dRedressedBar-27-2-revision.md](../prompts/2026-10-16-prompt-TOOL-dRedressedBar-27-2-revision.md) | research | TOOL-dRedressedBar-18 |
| [2026-10-16-prompt-TOOL-dRedressedBar-27-3-spec-writer.md](../prompts/2026-10-16-prompt-TOOL-dRedressedBar-27-3-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A full `bash tools/memory-tree/check-memory-hygiene.sh` at the build tip reds check 23 in three
arms. Units 2, 4, 5, 7, 9, 11, 18 and 20 closed with no acceptance ledger. Eight lines in
aSparedSpawn's ledgers are in neither legal form. Thirty answers, one in aOrientedCast and 29 in
aSparedSpawn, share no backticked token with their criterion. The owner ruled on 2026-10-15 to fix
them here (`prompts/2026-10-15-prompt-TOOL-dRedressedBar-27-brief.md`). This unit writes the eight
ledgers from what each builder recorded and rewrites each foreign line from its own evidence, so
check 23 passes with no waiver and no reading anyone did not make. Its spec-writer pass `<w27>`
first writes the five revision entries the unobserved lines cite, because a build pass may not write
a spec.

## 2. Scope (IN)

- **S1** — Arm 1. One acceptance ledger per listed unit under `memory/builds/dRedressedBar/build/`,
  answering every criterion its spec numbers, each line in the class §4 assigns it. Observed by AC1.
- **S2** — Arm 2. The eight foreign lines check 23 reads in neither form take a legal form, their
  words kept. Observed by AC2 and AC4.
- **S3** — Arm 3. The thirty foreign answers share a token with their criterion. Each added token
  names something the recorded observation ran, read or printed, and the pass cites where. Observed
  by AC3, AC4 and AC5.
- **S4** — The six criteria no record observed are written AMENDED, as F1 resolved: five foreign
  lines and unit 18's AC15. Each owning spec first gains one revision-log entry recording that the
  criterion was never observed, written by this unit's spec-writer pass `<w27>` before the build
  pass. The build pass then writes each line opening `amended rev-<n>` naming that entry. Observed by
  AC5 and AC4, and by AC1, AC2 and AC3 for their arms.
- **S5** — The agent-returns record is re-collected so it holds unit 18's rev-4 builder return,
  which arm 1 reads. Observed by AC7.
- **S6** — This unit's own ledger, listing every foreign line before and after. Observed by AC8.

## 3. Non-goals (OUT)

- No product code. No change under `tools/`, to `.memory-tree.conf`, to `memory/HYGIENE.md` or to
  any registry under `memory/project/`. No key, cutoff, grandfather row or waiver row moves to make
  check 23 pass. AC6 observes this.
- No edit to builds aSparedSpawn or aOrientedCast beyond the 37 target bullets and, in each of four
  specs (`TOOL-aSparedSpawn-11`, `-13` and `-32`, and `TOOL-aOrientedCast-22`), exactly three things:
  one appended revision-log entry (F1, resolved by the owner), the status header's rev and date moved
  to match it, and that spec's one generated row in its build README, re-rendered by
  `gen_build_index.py --write` and never by hand. All three land at `<w27>`. The status token, every
  other header field, every other section and every other README line stay as they are.
- No spec text in the build pass. It moves only the status and date cells of this spec, and the
  generated `gen:spec-records` rows its new ledgers add, which `gen_build_index.py --write` renders.
- No new reading of a foreign criterion. A foreign line keeps what its unit observed, and nothing is
  re-run for it.
- No re-observation of this build's criteria at the tip. Four later units moved
  `tools/run-gates/measure_legs.py`, so a reading there answers a different object (see Alternatives
  rejected).
- No line outside the 102 keys of §4 "Today's red". Lines check 23 already passes stay as they are,
  even where they read like these: `TOOL-aOrientedCast-20`'s AC7 is one.
- The probe of §4 is never committed. A tracked `.py` under `memory/builds/` is graded by the
  python-resolver ban and counted by the naming lexicon's corpus.
- No merge to local main and no push without the owner's ask.

## 4. Design

Records only. Every figure and line number below was read at the branch tip `b7f19d442` on
2026-10-15, and rev-2's corrections at `3f052d89e` on 2026-10-16. The unit lands in two passes.

| Name | Commit |
|---|---|
| `<w27>` | This unit's spec-writer pass: this spec at rev-2, the five revision entries and header moves of "The six revision entries", and the three build READMEs' generated rows, committed together by the main loop |
| `<red>` | `3f052d89e`, the commit the first build pass started from, before any record of this unit's work was tracked. The red halves are read here (see "The set-aside work") |
| `<parent>` | The commit the build pass starts from, at or after `<w27>` |
| `<p27>` | The build pass's commit |

Only `gov-spec-writer` writes a spec, and scratch-guard admits a builder's spec edit only where it
moves the status and date cells of the spec its card routes (`tools/hooks/scratch-guard.js:94-99`).
The first build pass was refused all five spec writes for that reason and returned DIVERGENCE, so
they are `<w27>`, as `<w21>`, `<w22>` and `<w25>` were before it. A build pass that finds any of the
five entries missing at `<parent>` returns that to the main loop before any write.

### Today's red

Measured with `bash tools/memory-tree/check-memory-hygiene.sh --only 23` at `b7f19d442` (PINNED).

- **Arm 1**, "a CLOSED unit numbers an acceptance criterion that no journal record evidences": every
  label of eight specs, 64 keys. They are `TOOL-dRedressedBar-2` AC1-AC4, `-4` AC1-AC4, `-5`
  AC1-AC10, `-7` AC1-AC7, `-9` AC1-AC7, `-11` AC1-AC7, `-18` AC1-AC17 and `-20` AC1-AC8.
- **Arm 2**, "an acceptance-ledger line is in neither legal form": `TOOL-aSparedSpawn-10/AC9`,
  `-11/AC10`, `-13/AC11`, `-6/AC6`, `-6/AC8`, `-8/AC10`, `-8/AC6` and `-32/AC12`.
- **Arm 3**, "a ledger answer shares no backticked token with the criterion": `TOOL-aOrientedCast-22/AC7`,
  and `TOOL-aSparedSpawn-1/AC5`, `-11/AC10`, `-11/AC2`, `-11/AC3`, `-11/AC6`, `-11/AC7`, `-12/AC5`,
  `-12/AC6`, `-13/AC3`, `-13/AC5`, `-14/AC3`, `-14/AC4`, `-14/AC7`, `-2/AC2`, `-2/AC6`, `-3/AC3`,
  `-3/AC4`, `-3/AC7`, `-4/AC10`, `-4/AC12`, `-4/AC6`, `-4/AC8`, `-8/AC11`, `-8/AC12`, `-16/AC11`,
  `-16/AC12`, `-16/AC18`, `-32/AC1` and `-34/AC1`.

That is 8 units and 38 foreign entries. `TOOL-aSparedSpawn-11/AC10` sits in arms 2 and 3, so the
foreign entries are 37 distinct lines. Arms 2 and 3 are byte-identical at the base `ebce889c7`
(`prompts/2026-10-15-prompt-TOOL-dRedressedBar-1-4-researcher.md`).

### What check 23 grades

Read from `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf` at `b7f19d442`.

| Rule | Where |
|---|---|
| The population is a CLOSED, Tier-2 spec dated on or after `ACCEPTANCE_LEDGER_CUTOFF`, 2026-08-20, whose id is not in `ACCEPTANCE_LEDGER_GRANDFATHER` | `.memory-tree.conf:828`, `:846`; checker `:3088-3092` |
| The label and token arms bind from `LEDGER_LABEL_CUTOFF` and `LEDGER_TOKEN_CUTOFF`, 2026-09-08, by the spec's filename date. All 23 specs here are later, so every arm binds | `.memory-tree.conf:259`, `:264`; checker `:3095-3096` |
| An answer is a `- ACn` or `- **ACn**` bullet inside an `**Evidences:** <id>` block of a record whose `**Serves:**` kind is `journal`. A block ends at the next `**Evidences:**` line or at any line opening `#` | checker `:3005-3010` |
| The form is read on the bullet's FIRST LINE only. A complete backticked pair is OBSERVED, else `amended rev-<n>` is AMENDED, else it is `bad` | `:3013` |
| Tokens are extracted per line, so a backticked span broken by a line break is a token on neither line | `altoks`, `:3029` |
| The token list is bullet-scoped: every non-blank line up to the next bullet, `**Evidences:**` line or heading. A paragraph trailing the last bullet belongs to it | `:3022` |
| The spec side is each label under `## N. Acceptance criteria`, with its bullet's per-line tokens | `:3075-3085` |
| An answer passes the join when any spec token and any answer token contain one another, case-folded. It is silent when either side has no token | `:3155-3166` |
| The first answer per unit and label wins, in `git ls-files` order | `:3120` |

`memory/HYGIENE.md` "Acceptance ledger" gives the meaning. OBSERVED carries a token naming what made
the observation. AMENDED names the revision that changed the criterion and the section 9 line that
logs it. There is no third form.

### Classes, and the rule each line follows

Every line this unit writes or rewrites is in one class.

- **O, observed.** The record holds a reading of the criterion as it stands. The line is OBSERVED.
  Its first line carries a complete backticked token. Every token on the line names what the
  recorded observation ran, read or printed, and at least one is contained in, or contains, one of
  the criterion's tokens. A printed line that instantiates a criterion's template, such as
  `skipped — unbuildable · …` for `skipped — <id> · <why>`, earns the template token. So does a
  source line that instantiates the criterion's own spelling, such as `NR==FNR` for `NR == FNR` or
  `age.${heldkeys[$i]}` for `age.*`.
- **A, amended.** A real section 9 entry of the owning spec changed the criterion after the reading,
  or moved it out of the unit. The line opens `amended rev-<n>`, names that entry, and carries the
  reading if one exists. No backtick sits on its first line. A token in its wrap either names what
  the reading touched or quotes the criterion's own text the entry changed. Where the entry itself
  says the build's reading still answers the reworded criterion, as spec 7's rev-5 does for AC4,
  the line is O instead.
- **U, unobserved.** The record holds no reading, and no section 9 entry changed the criterion.
  Before writing one, the pass greps the owning build's records for a later observation. If one
  exists, the line is O and cites it. Otherwise the pass appends the entry "The six revision
  entries" lists to the owning spec, and the line is written AMENDED: it opens `amended rev-<n>`
  naming that entry, its reading then opens `NOT OBSERVED` and says what was owed and when, in the
  record's own words, and its wrap quotes the criterion's own token as what was never observed.

Two rules bind every class. A foreign line keeps every word it had, in order; the pass adds words
and moves line breaks, and removes none. And a token is added to an O line only where the cited
evidence carries it, or an instance of it, at the commit the before-and-after entry names. A token
spelled as the criterion spells it is found in the owning spec, and the entry names both that spec
line and the evidence's instance. Where the evidence carries neither, that line is U for the half
the evidence does not show.

### Arm 1 — the eight ledgers

Each ledger takes the shape of this build's own, such as
`2026-10-14-build-TOOL-dRedressedBar-16-1-acceptance-ledger.md`: an H1, the line
`**Serves:** journal <unit id>`, a preamble, then one `**Evidences:** <unit id>` block with one
bullet per label in label order. The preamble names the spec rev built against, the build commits,
the return's heading in the agent-returns record, and that no gate ran in the build pass.

| Unit | Built at | Commits | Return | Criteria and class |
|---|---|---|---|---|
| 2 | rev-3, current | `c7a9213d1` | `:4655` | AC1-AC4 O |
| 4 | rev-2; rev-3 moved §3, §5, §7 | `305ea9c20` | `:4707` | AC1-AC4 O |
| 5 | rev-5; rev-6 names AC1 and AC2 and says "no criterion text moves" | `ecdca277e` | `:4882` | AC1-AC10 O |
| 7 | rev-4; rev-5 rewords AC4 and says "this unit's ledger still answers it" | `671f25c71` | `:5035` | AC1-AC7 O |
| 9 | rev-4; rev-5 to rev-7 move no criterion | `59f11096a` | `:4681` | AC1-AC7 O |
| 11 | rev-3; rev-4 to rev-6 move no criterion | `b65688cde` | `:5180` | AC1-AC7 O |
| 18 | rev-4 | `6783992aa`, `997fc294f` | `wf_0e7a57a1-02c`, collected by S5; AC8's reading is the first build's at `:5496` | 13 O, 3 A, 1 U, below |
| 20 | rev-2, current | `404d45c8c`, `21c2d1531`, `566c6d831` | `:5022` | AC1-AC8 O |

Return lines are in `build/2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md` at
`b7f19d442`. The commit bodies and their `Decided:` trailers are read beside each return.

Two readings are written as the builder gave them, never tidied into a pass.

- Unit 7's AC5. The builder reported it "partly met": `git grep -nF "gov:kit <kit>@<old>"` printed
  two lines, both prose quotes in `memory/builds/aOrientedCast/` records, and nothing outside
  `memory/builds/`. No revision moved AC5, so the line is O and states those two lines.
- Unit 9's AC5. The builder observed the green half and wrote that the red half "was observed when
  the spec was written". The line says so.

Unit 18, read from its rev-4 builder's return and its commits:

- **O:** AC3, AC4, AC6, AC7, AC9, AC10, AC11, AC12, AC13, AC14, AC16 and AC17, from the return's
  table. AC8 is O from the first build's reading at `:5496`, because the rev-4 return says that code
  is unchanged and was not re-run, and `6783992aa` restored it verbatim. AC17's line names its half on
  AC15's run as owed.
- **A:** AC1, AC2 and AC5. Spec 18's rev-7 entry (spec `:1134`) rewrote them after the build and says
  "Unit 18 built against its criteria as written". Each line opens `amended rev-7` and carries the
  rev-4 reading.
- **U:** AC15. The rev-4 return says the turnstile arm runs the real runner's hold verb and was not
  run. Its line opens `amended rev-9`, the entry "The six revision entries" lists.

Ledger names: `2026-10-15-build-TOOL-dRedressedBar-<n>-1-acceptance-ledger.md` for units 2, 4, 5, 7,
9, 11 and 20, and `2026-10-15-build-TOOL-dRedressedBar-18-2-acceptance-ledger.md` for unit 18, whose
`-1-` is the set-aside record. The names keep the 2026-10-15 date the saved files carry.

### The set-aside work

The first build pass wrote the eight ledgers, the re-collected returns record and the 37 foreign
bullets, could not commit them, and saved them verbatim in
`build/2026-10-16-build-TOOL-dRedressedBar-27-1-set-aside-work.md`. The build pass restores each
from that record and changes it only where this revision requires. That record's `HANDOFF.txt`
holds the five entries `<w27>` writes, and its builder's return names seven spec facts rev-2 corrects.

That record opens `**Serves:** research`, but check 23 resets its journal flag at every
`**Serves:**` line (`tools/memory-tree/check-memory-hygiene.sh:3005`). From its line 561 the record
embeds the eight ledgers whole, each with a column-0 `**Serves:** journal` line and an
`**Evidences:**` block. So once it is tracked, check 23 reads it as a journal record answering units
2, 4, 5, 7, 9, 11, 18 and 20. Two things follow.

- The red halves are read at `<red>`, `3f052d89e`, where that record is untracked. At `<parent>`
  the saved copies may already answer arm 1.
- At `<p27>` each unit's own ledger must win check 23's first-wins map. `git ls-files` lists every
  `2026-10-15-` ledger name above before the `2026-10-16-` set-aside record, so it does. AC1 names
  the answering file, so a renamed ledger that sorted after the record would read red.

### Unit 18's source, re-collected

The brief names unit 18's return in the agent-returns record as its source. That record was last
collected after the first build diverged (its header says so), so it holds only the diverged rev-3
return at `:5496`. The rev-4 builder's return is in the session journal
`C:/Users/d41ly/.claude/projects/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/subagents/workflows/wf_0e7a57a1-02c/journal.jsonl`.
Read on 2026-10-15, it carries a criterion table for AC1 to AC17.

The record declares its own scope, "every agent of session 8d2976c7", and embeds its own collector.
The pass cuts that collector from the record's fenced block into the session scratchpad, runs it with
`-I` over that session's `subagents` directory, and replaces the record's `## Returns` body with the
output. The header sentence moves to "last regenerated" at this unit. `1f45ba9a9` is the precedent.
The collector sorts by timestamp, so new returns are inserted and an earlier one keeps its bytes
unless its transcript moved. AC7 grades that none moved.

`git ls-files` lists that record before every new ledger, and it is a `journal` record. A
column-0 `**Evidences:**` line inside any collected return would win check 23's first-wins map for
that unit. It holds none today, and AC7 grades that the re-collection keeps none.

### Arms 2 and 3 — the 37 foreign lines

Paths are `memory/builds/aSparedSpawn/build/<date>-build-TOOL-aSparedSpawn-<n>-acceptance-ledger.md`,
dated 2026-10-11 for units 1 to 14, 2026-10-12 for 16 and 32, and 2026-10-13 for 34. The
aOrientedCast line is in
`memory/builds/aOrientedCast/build/2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md`.
An instrument written `-<n>-direct-checks.sh` is that unit's dated
`*-build-TOOL-aSparedSpawn-<n>-direct-checks.sh` record in the same folder.

Lines are at `b7f19d442`, and a reflow above a target moves it. "Verified" means the spec writer
found the evidence at `b7f19d442`. "Confirm" means the pass reads it at the unit's pass commit,
found by its `Pass:` trailer, and applies the fallback rule above if it is not there.

Arm 2:

| Key | Line | Class | Remedy | Evidence |
|---|---|---|---|---|
| aSparedSpawn-10/AC9 | 50 | O | The check field's command wraps after `--only`; join it onto line 1 | Its own token; the spec side has none, so the join is silent |
| aSparedSpawn-11/AC10 | 53 | U | AMENDED, `amended rev-4`. Quote `check-pass-order.sh` and `check-brief-recorded.sh` as what was never timed | The line: "OWED at VERIFYING; no figure exists yet" |
| aSparedSpawn-13/AC11 | 63 | U | AMENDED, `amended rev-6`; the wrap's existing `a` already shares with the criterion | The line: "not run"; the criterion's own `cost:` line |
| aSparedSpawn-6/AC6 | 36 | A | Open the answer `amended rev-2`; the wrap's two tokens already share | Spec 6 rev-2 names AC6 and makes the run the owner's equivalence run. Verified |
| aSparedSpawn-6/AC8 | 44 | O | The bullet's own `exit 3` becomes its check field on line 1 | Its own token, which contains the criterion's `exit` |
| aSparedSpawn-8/AC10 | 60 | O | Join the wrapped check-field command onto line 1 | Its own token |
| aSparedSpawn-8/AC6 | 41 | O | Join the wrapped check-field command onto line 1 | Its own token |
| aSparedSpawn-32/AC12 | 79 | O | Reflow so `lineage` ends line 1 | Its own token |

Arm 3, apart from `-11/AC10` above:

| Key | Line | Class | Token, and the words it names | Evidence |
|---|---|---|---|---|
| aOrientedCast-22/AC7 | 35 | U | AMENDED, `amended rev-2`; quote `AskUserQuestion` as the refusal never seen live | The line: owed to the live session. No later record observes it |
| aSparedSpawn-1/AC5 | 23 | O | `REUSE_SCHEMA`, for "the schema line" | `tools/run-gates/run-gates.evidence.test.sh:1145-1153`. Verified |
| aSparedSpawn-11/AC2 | 22 | O | `process.exit`, for "the exit stub" | Instrument `-11-direct-checks.sh:88` stages it in the runner cut from `agent-cap.test.sh`. Confirm the stub is `process.exit` |
| aSparedSpawn-11/AC3 | 26 | O | `gov:sequential-agents`, for "the marker strip" | Instrument `:93`. Verified |
| aSparedSpawn-11/AC6 | 38 | U | AMENDED, `amended rev-4`; quote `git archive` as the run that was owed | The line: "OWED at VERIFYING"; its reading is of the diff only |
| aSparedSpawn-11/AC7 | 41 | O | `build_commit`, for "two declared calls" | Instrument `:60-70`. Verified |
| aSparedSpawn-12/AC5 | 46 | O | `TREE_CLEAN`, for "a tracked file dirtied" | Instrument `-12-direct-checks.sh:123`; the runner sets `TREE_CLEAN=no` on any dirt, `run-gates.sh:2692-2693` today. Confirm |
| aSparedSpawn-12/AC6 | 49 | O | `guard`, for the held and selected legs | The instrument's fixture legs. Confirm |
| aSparedSpawn-13/AC3 | 40 | O | `clock`, for "`clk` executed" | Instrument `-13-direct-checks.sh` declares it once. Confirm it is `clk`'s |
| aSparedSpawn-13/AC5 | 44 | O | `TREE_CLEAN`, for "an untracked guarded file" | Instrument `:137`, and the runner as for `-12/AC5`. Confirm |
| aSparedSpawn-14/AC3 | 40 | O | `REFUSAL_CEILINGS` or `--check`, for "above its ceiling" | `tools/memory-tree/check-arms.py`'s selftest. Confirm it grades through `--check`'s walk |
| aSparedSpawn-14/AC4 | 43 | O | `memory/DECISIONS.md`, for "the fixture decision log" | The same selftest's fixture. Confirm |
| aSparedSpawn-14/AC7 | 55 | O | `--check`, for the planted gate's refusal | The same selftest. Confirm |
| aSparedSpawn-2/AC2 | 17 | O | `GATE_CALIBRATION_RATES`, for "the seam's rates" | `tools/run-gates/run-gates.test.sh:3711-3715`, arm 12a. Verified |
| aSparedSpawn-2/AC6 | 21 | O | `spawnpause`, for the row arm 12e declares | The same suite at `:3794`. Confirm |
| aSparedSpawn-3/AC3 | 23 | O | `GATE_WALL`, for "a 50 s wall" | Instrument `-3-direct-checks.sh`, two hits. Verified |
| aSparedSpawn-3/AC4 | 28 | O | The double-quoted FAIL text, backticked; it carries `again on its serial retry` | The line's own printed output |
| aSparedSpawn-3/AC7 | 38 | O | `NR == FNR`, for the "before" run's ledger merge | The criterion's spelling, spec 3 `:163`. The "before" runner is `286b839a`, the unit's ledger `:9`, and carries `NR==FNR` at `286b839a:tools/run-gates/run-gates.sh:4036`. Verified at rev-2 |
| aSparedSpawn-4/AC10 | 56 | O | `PROCMON_WHY`, for "the `run-gates: process-monitor:` line" | That line prints it, `run-gates.sh:2903` today. Confirm |
| aSparedSpawn-4/AC12 | 64 | O | `"$(cat <<'RKD'`, for "its wrapper reverted" | The wrapper the revert restores, `989e9234b:tools/hooks/agent-cap.test.sh:72`. The instrument `-4-direct-checks.sh` composes the idiom at run time (`:280`) and does not carry the literal. Verified at rev-2 |
| aSparedSpawn-4/AC6 | 35 | O | `input_key`, for "all six ledger keys" | The column `input_key` writes, `run-gates.sh:3177` today. Confirm |
| aSparedSpawn-4/AC8 | 47 | O | `PS4`, for "its trace descriptor" | Instrument, four hits. Verified |
| aSparedSpawn-8/AC11 | 67 | O | `skipped — <id> · <why>`, the template of the printed line | The line's own printed instance; spec 8 spells the template at `:352`. Verified at rev-2 |
| aSparedSpawn-8/AC12 | 71 | O | `tools/unattended/unattended.sh`, beside `unattended-status` | `memory/project/fork-ceilings.txt:15`, that row's command. Verified |
| aSparedSpawn-16/AC11 | 19 | A | Open `amended rev-3`; `--dispatch` moves into the wrap; add `TOOL-aSparedSpawn-25` | Spec 16 rev-3 moved S10 with AC11 to the exit (spec `:355`); rev-4 names its ask (`:364`). Verified |
| aSparedSpawn-16/AC12 | 20 | O | `age.*`, for the base runner's count | The criterion's spelling, spec 16 `:110`. The instrument's base is `f53211e6c`, the unit's ledger `:8`, whose runner spells the file `age.${heldkeys[$i]}` at `f53211e6c:tools/run-gates/run-gates.sh:3097` and `:3115`. Verified at rev-2 |
| aSparedSpawn-16/AC18 | 26 | O | `GATE ok    <leg>  (sampled against a cached ok)`, the template of the printed line | The line's own printed instance |
| aSparedSpawn-32/AC1 | 21 | U | AMENDED, `amended rev-5`; quote `git diff 69e0ff0f5 37200355d -- F` as the range not read | The pass read origin's moved tip `6e8f8b1da`, spec 32 §4 (f) and rev-4 (spec `:212`, `:374`); rev-4 names §4 only |
| aSparedSpawn-34/AC1 | 45 | O | `git diff 6e8f8b1da main -- F`, beside the `-U0` form the pass ran | `-U0` changes no added line. Verified |

`-11/AC10` carries a "Checked as well" paragraph that check 23 reads into its bullet. The criterion
tokens its U line quotes make the join pass, so the paragraph does not move.

### The six revision entries

F1 resolved (a). Each U line cites one entry in the revision log of the spec that owns it, numbered
one above that log's highest entry at `<red>`. The five entries are `<w27>`, written by this unit's
spec-writer pass in the text the set-aside record's `HANDOFF.txt` saved, dated 2026-10-16. The build
pass reads them and writes none:

| Spec | Entry | Label | What it records |
|---|---|---|---|
| `memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-11.md` | rev-4 | AC6, AC10 | AC6's suite run and AC10's timings were owed at VERIFYING, and no record observes either |
| `memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-13.md` | rev-6 | AC11 | The two whole bars were never run, and no record observes them |
| `memory/builds/aSparedSpawn/spec/2026-10-12-spec-TOOL-aSparedSpawn-32.md` | rev-5 | AC1 | The range was read at origin's moved tip `6e8f8b1da`, where rev-4's §4 (f) moved the merge, and never at `37200355d` |
| `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-22.md` | rev-2 | AC7 | The live refusal was owed to the main loop's session at the close, and no record observes it |
| `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md` | rev-9 | AC15 | The turnstile arm runs the real runner's hold verb inside `--selftest`, which no pass ran, and no record observes it |

Each entry takes the shape `- rev-<n> · 2026-10-16 · <ACn …> · records, TOOL-dRedressedBar-27: <what
it records>. The criterion does not move, and the status stays CLOSED.` The AC tokens satisfy
`REV_SCOPE_CUTOFF`. The entry is the line's evidence: it says the criterion was never observed. It
never claims the criterion was reworded.

Each of the five specs' status header moves its rev to the new entry's number and its date to
2026-10-16, so header and log stay one fact, as the format's rev rule asks
(`memory/TEMPLATE-SPEC.md:66-69`). The status stays CLOSED and no other header field moves. The
gate alone would not demand it: check 12 reds only a header rev above the log's highest entry
(`tools/memory-tree/check-memory-hygiene.sh:2052`). The header move changes each spec's row in its
build README's generated units table. So at `<w27>` the main loop re-renders
`memory/builds/aSparedSpawn/README.md`, `memory/builds/aOrientedCast/README.md` and
`memory/builds/dRedressedBar/README.md` with `python tools/memory-tree/gen_build_index.py --write`,
never by hand. For the two foreign READMEs, the diff is that one row each. The dRedressedBar README
also moves this spec's row to rev-2.

### The probe

A Python program in the session scratchpad, run with `-I`. It takes a ref and a list of keys. It
reads the tree through `git ls-tree -r --name-only <ref>` and `git show <ref>:<path>`, so one program
reads `<red>`, `<parent>` and `<p27>`. It applies the rules of the table "What check 23 grades", and prints one
line per key: `ok obs`, `ok amd`, `GAP`, `BAD` or `TOKBAD`, with the answering file and line. It also
prints `ORPH` for an answer whose label the spec does not number.

Its liveness half runs first: at `<red>` it must print exactly the 102 keys of "Today's red" in
their arms. A probe that cannot reproduce that list is wrong and is fixed before it grades anything.
It re-derives check 23 and is not check 23. The close's `memory hygiene` leg is the verdict.

The word check is the probe's second mode. For each of the 37 targets it reads the bullet at
`<parent>` and at `<p27>`, takes each side's word sequence with backticks and quote marks stripped,
and prints `LOST <key> <word>` for a word the first side has and the second lacks.

### The record

`2026-10-16-build-TOOL-dRedressedBar-27-2-acceptance-ledger.md` carries
`**Serves:** journal TOOL-dRedressedBar-27`. Its `-2-` follows the set-aside record's `-1-`, as unit
18's ledger does. A `## Foreign lines, before and after` section precedes
its `**Evidences:**` block. It gives each of the 37 targets a `###` sub-head with its key, class and
evidence, and two fenced blocks holding the bullet's bytes at `<parent>` and at `<p27>`. The section
sits under a heading and above the block, because check 23 reads raw lines and a fenced `- ACn` line
inside an `**Evidences:**` block would be read as an answer. The block answers AC1 to AC8 with the
probe's output lines.

### Files touched (estimate)

At `<w27>`, by this unit's spec-writer pass and the main loop:

- this spec, at rev-2
- the status header's rev and date and the revision log alone of
  `memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-11.md`,
  `memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-13.md`,
  `memory/builds/aSparedSpawn/spec/2026-10-12-spec-TOOL-aSparedSpawn-32.md`,
  `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-22.md` and
  `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md`
- one generated row each in `memory/builds/aSparedSpawn/README.md` and
  `memory/builds/aOrientedCast/README.md`, the rows of specs 18 and 27 in
  `memory/builds/dRedressedBar/README.md`, and the build's row in `memory/LIVE.md`, all by
  `gen_build_index.py --write`

At `<p27>`, by the build pass:

- `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-2-1-acceptance-ledger.md`
- `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-4-1-acceptance-ledger.md`
- `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-5-1-acceptance-ledger.md`
- `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-7-1-acceptance-ledger.md`
- `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-9-1-acceptance-ledger.md`
- `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-11-1-acceptance-ledger.md`
- `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-18-2-acceptance-ledger.md`
- `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-20-1-acceptance-ledger.md`
- `memory/builds/dRedressedBar/build/2026-10-16-build-TOOL-dRedressedBar-27-2-acceptance-ledger.md`
- `memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`
- the fourteen aSparedSpawn ledgers of units 1, 2, 3, 4, 6, 8, 10, 11, 12, 13, 14, 16, 32 and 34
- `memory/builds/aOrientedCast/build/2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md`
- this spec's status and date cells, and the build README's and `memory/LIVE.md`'s generated rows
- the generated `gen:spec-records` region of each of
  `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-<n>.md` for n of 2, 4, 5, 7,
  9, 11, 18 and 20, one row for its new ledger, by `gen_build_index.py --write`

### Alternatives rejected

- **A grandfather row or a later cutoff.** The brief and the owner's ruling forbid it, and it would
  hide 102 real answers rather than give them.
- **Unit 18's ledger from the record as it stands.** Eight criteria its rev-4 builder did observe
  would read unobserved, which is false. Quoting the journal's return inside unit 18's ledger
  instead puts a second copy of the return beside the record whose job is to hold it.
- **Re-observing this build's unobserved criteria at the tip.** `TOOL-aBriskPreflight-12` did this
  for a seconds-long `grep`. Here the only such criterion is unit 18's AC15. It runs the real
  runner's hold verb inside `--selftest`, which a builder may not run, against a profiler four later
  units changed.
- **Moving a foreign line's trailing paragraph above its `**Evidences:**` line.** It changes no word,
  but no target needs it once its own token earns the join.

## 5. Acceptance criteria

- **AC1** — When the §4 probe runs at `<p27>` over the 64 keys of units 2, 4, 5, 7, 9, 11, 18 and 20,
  each prints `ok obs` or `ok amd` with that unit's own ledger as §4 names it, and no `ORPH` line
  names those units.
  Red when: at `<red>` each of the 64 prints `GAP`, the arm-1 list `check-memory-hygiene.sh`
  printed at `b7f19d442`; or a key answers from the set-aside record.
  figure: 64 is DERIVED by the probe from the eight specs' labels; the list is PINNED at `b7f19d442`.
  permission: check 23's own verdict is the `memory hygiene` leg, which the close runs. A builder
  runs no gate.
- **AC2** — When the probe runs at `<p27>` over the eight arm-2 keys, each prints `ok obs` or
  `ok amd`.
  Red when: at `<red>` all eight print `BAD`, check 23's arm-2 list at `b7f19d442`.
- **AC3** — When the probe runs at `<p27>` over the 30 arm-3 keys, none prints `TOKBAD`.
  Red when: at `<red>` all 30 print `TOKBAD`, check 23's arm-3 list at `b7f19d442`.
- **AC4** — When the probe's word check compares the 37 target bullets at `<parent>` and `<p27>`, it
  prints no `LOST` line, and `git diff <parent> <p27>` over the fifteen foreign ledger files shows no
  hunk outside those bullets. Over the five specs of "The six revision entries",
  `git diff <w27>~1 <w27>` adds exactly one entry each inside the `## 9. Revision log` section, and
  changes only the `**Status:**` line's rev and date, to that entry's number and 2026-10-16, and the
  generated `gen:spec-records` region. Over `memory/builds/aSparedSpawn/README.md` and
  `memory/builds/aOrientedCast/README.md` it changes one generated row each, the row of that spec,
  and `gen_build_index.py --check` reads clean at `<w27>`. `git diff <parent> <p27>` over the five
  specs changes nothing outside a `gen:spec-records` region.
  Red when: a word of a foreign reading is dropped, a hunk lands on a line no target owns, a spec's
  header rev differs from its new entry or any other header field, section or README line moves, a
  README row differs from what `gen_build_index.py --write` renders, or the build pass writes spec
  text.
- **AC5** — When each token the pass added to a foreign O line is searched with `git grep -F` at the
  commit and path its before-and-after entry names, each is found. A token spelled as the criterion
  spells it, such as `age.*`, `NR == FNR`, the two templates and `git diff 6e8f8b1da main -- F`, is
  found in its owning spec, and the entry names the evidence's instance beside it. When each AMENDED
  line's `amended rev-<n>` is looked up in its spec's revision log at `<w27>`, that entry names the
  line's AC label.
  Each of the six U lines opens `amended rev-<n>` with the entry "The six revision entries" lists
  for it, carries no backtick on its first line, and its reading opens `NOT OBSERVED`.
  Red when: an added token's search prints nothing, a cited entry does not name the label, or a U
  line is in the OBSERVED form.
- **AC6** — When `git diff <parent> <p27> -- .memory-tree.conf tools/ memory/HYGIENE.md memory/project/`
  runs, it prints nothing.
  Red when: a cutoff, a grandfather row, a waiver row or a checker line moves.
- **AC7** — When the re-collected `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md` is read
  at `<p27>`, it holds the `wf_0e7a57a1-02c` return labelled `TOOL-dRedressedBar-18 · build`,
  `grep -c '^\*\*Evidences:\*\* '` over it prints `0`, and `git diff <parent> <p27>` over it removes
  no line under `## Returns`.
  Red when: that return is absent, an earlier return's bytes moved, or a line opens `**Evidences:**`.
- **AC8** — When `2026-10-16-build-TOOL-dRedressedBar-27-2-acceptance-ledger.md` is read, it carries
  `**Serves:** journal TOOL-dRedressedBar-27`, one before-and-after entry for each of the 37 foreign
  targets, and an `**Evidences:** TOOL-dRedressedBar-27` block answering AC1 to AC8.
  Red when: a target has no entry, or an entry's before bytes differ from the bullet at `<parent>`.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`memory hygiene` is check 23's verdict over this unit, run once at the close. The two recall legs
are owed because every touched path sits under their `memory/` guard. The unit adds no arm.

## 7. Open questions

- **F1 — How is a criterion no record observed written, when check 23 admits only a backticked first
  line or `amended rev-<n>`?** Six lines are in class U: `TOOL-aSparedSpawn-11` AC6 and AC10,
  `TOOL-aSparedSpawn-13/AC11`, `TOOL-aSparedSpawn-32/AC1`, `TOOL-aOrientedCast-22/AC7` and
  `TOOL-dRedressedBar-18/AC15`. No section 9 entry changed any of them. The brief asks for "the honest
  legal form check 23 accepts for an unobserved criterion, not given a token it did not earn", and
  forbids any edit to those builds beyond the listed lines. `memory/HYGIENE.md` says AMENDED is where
  divergence belongs, and that writing the observed form for a criterion nobody observed is the
  failure it exists to prevent. AMENDED needs a section 9 entry. So the two constraints cannot both
  hold for the five foreign lines.
  - (a) AMENDED, everywhere. Each owning spec gains one revision entry naming the label: what was owed,
    that no record observed it, and that the criterion does not move and the status stays CLOSED.
    That is `TOOL-aSparedSpawn-11` rev-4, `-13` rev-6, `-32` rev-5, `TOOL-aOrientedCast-22` rev-2 and
    `TOOL-dRedressedBar-18` rev-9, with each header rev and the generated rows they move. The line
    opens `amended rev-<n>` and quotes the criterion's own token in its wrap. `TOOL-aBatchedArm-3`'s
    rev-8 is the precedent. The owner widens the second non-goal by one entry per foreign spec.
  - (b) An OBSERVED-shaped owed line. The criterion's own token sits on line 1 and the reading opens
    `NOT OBSERVED`. Only ledger lines move. `TOOL-aOrientedCast-20/AC7` is in this shape today, and
    check 23 passes it. It writes the observed form for an unobserved criterion, which the grammar
    names as the failure, and it is what the brief calls a token not earned.
  - (c) (a) for this build's spec 18, which later units here already revise as records fixes while it
    stays CLOSED, and (b) for the five foreign lines, keeping the non-goal as written.
  Recommendation: (a). It is the only form that is both legal and true under the grammar, and it
  costs five revision entries. If the owner keeps the second non-goal as written, (c).
  RESOLVED (owner, 2026-10-15): (a) — relayed by the coordinator. The second non-goal widens, for
  each of the four foreign specs, to the appended entry, the header's rev and date, and the one
  generated README row; §4 "The six revision entries" holds what `<w27>` writes. At rev-1 the build
  pass held those writes, and rev-2 moved them to `<w27>`.

## 8. Revision log

- rev-1 · 2026-10-15 · initial draft from the unit-27 brief. Every key, line and rev was read at
  `b7f19d442`. Today's red was measured with `--only 23`. Unit 18's rev-4 return was found
  uncollected in the session journal. F1 resolved by the owner on 2026-10-15 as (a) and folded
  before the first commit: S4, the second non-goal, §4's classes, tables, files and new section
  "The six revision entries", AC4 and AC5. The four foreign specs' header rev and date move with their
  new entry, and their build READMEs' one generated row each is re-rendered by
  `gen_build_index.py --write`: the coordinator's call, to keep header and log one fact.
- rev-2 · 2026-10-16 · S4 · §1 · §3 · §4 · §7 · AC1 AC2 AC3 AC4 AC5 AC8 · the first build pass's
  DIVERGENCE (`prompts/2026-10-16-prompt-TOOL-dRedressedBar-27-2-revision.md`). Scratch-guard refused
  it all five spec writes, so the five revision entries and header moves are this unit's spec-writer
  pass `<w27>`, written in this same pass in the text the set-aside record's `HANDOFF.txt` saved,
  dated 2026-10-16. The main loop commits them with this revision and re-renders the three build
  READMEs' rows. The build pass writes only the eight ledgers, the returns record, the 37 foreign
  bullets and its own ledger, restored from
  `build/2026-10-16-build-TOOL-dRedressedBar-27-1-set-aside-work.md`. §4 gains the commit table and
  "The set-aside work": that record embeds the eight ledgers as journal text check 23 reads, so the
  red halves move to `<red>`, `3f052d89e`, and AC1 names the answering ledger. Seven spec facts the
  builder found are corrected: `-8/AC11`'s template is `skipped — <id> · <why>`; `-4/AC12`'s literal
  is the wrapper at `989e9234b:tools/hooks/agent-cap.test.sh:72`; `-3/AC7`'s before-runner is
  `286b839a`; `-16/AC12`'s instrument base is `f53211e6c`, spelling the file `age.${heldkeys[$i]}`;
  AC5 finds criterion-spelled tokens in the owning spec; Files touched adds the generated records
  rows the eight ledgers add to specs 2, 4, 5, 7, 9, 11, 18 and 20; and AC4's date is 2026-10-16.
  This unit's own ledger becomes `-27-2-`, since the set-aside record holds `-27-1-`.

## 9. Reuse audit

`python tools/codebase-map/reuse_lookup.py "evidence each acceptance criterion of a closed unit in a
ledger line joined to its criterion by a shared token"` returned name-stem neighbours only. Examples
are `units` in `tools/unattended/unattended.test.sh`, `check_line` in `tools/runlog/runlog_lib.py`
and `resolve_prefix_token`; none reads or writes a ledger. No code is written, so no existing seam
fits a new mechanism. The seams this unit extends are records. They are the ledger grammar of
`memory/HYGIENE.md` "Acceptance ledger", the agent-returns record's embedded collector, and this
build's own ledger shape. Recall surfaced three precedents followed here. `TOOL-aBriskPreflight-12`
back-filled two ledgers from build commits, wrote AMENDED for a sibling's later revision and refused
the observed form untruly. `TOOL-aHoistedPass-39` filed this first-line class and named its remedy,
a token already in the criterion's paragraph hoisted onto line 1. `memory/builds/aSweptBar/` is a
records-only unit that handed this check 23 debt on. Rev-2's `<w27>` follows this build's own
spec-writer passes `<w21>`, `<w22>` and `<w25>`, each a records fix to another CLOSED spec, written
before its unit's build pass (spec 18's rev-6 to rev-8).

Recall terms used: `python tools/memory-recall/query.py "how is an acceptance criterion nobody
observed written in a ledger, and how are another build's ledger lines back-filled" --terms
"acceptance ledger AMENDED OBSERVED owed VERIFYING back-fill grandfather check 23 token join Evidences
journal"`
