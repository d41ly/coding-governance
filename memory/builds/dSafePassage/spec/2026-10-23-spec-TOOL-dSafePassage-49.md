# TOOL-dSafePassage-49 — the spec audit of units 43 to 46, the step module's 20 minors: one step-row predicate, TOOL-4 after TOOL-43, a second walk refusal, identity forms held by the arm, declared exits, and the readings that cite them

**Status:** CLOSED · rev-6 · 2026-10-28 · node d · Tier-2 · base 3708a705 · streams tooling · order 13 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-49-deviation-135.md](../build/2026-10-23-build-TOOL-dSafePassage-49-deviation-135.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-49-deviation-95.md](../build/2026-10-23-build-TOOL-dSafePassage-49-deviation-95.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-build-TOOL-dSafePassage-49-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-49-ledger.md) | journal | — |
| [2026-10-28-build-TOOL-dSafePassage-49-deviation-181.md](../build/2026-10-28-build-TOOL-dSafePassage-49-deviation-181.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-49-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-49-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-49-2-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-49-2-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-49-fork-resolution.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-49-fork-resolution.md) | research | — |
| [2026-10-23-prompt-TOOL-dSafePassage-49-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-49-hygiene-fix.md) | research | — |
| [2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md) | research | TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-49-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-49-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-49-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-49-1-spec-writer.md) | research | — |
| [2026-10-28-prompt-TOOL-dSafePassage-49-2-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-49-2-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-50 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 43 to 46
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md`)
exited CONVERGED with 27 confirmed findings. Its 2 HIGH are promoted as `TOOL-dSafePassage-47` and
`TOOL-dSafePassage-48`. BUILD-METHOD M4 batches its 25 minors, and they split into two disjoint write
sets by M6's clauses, so they are two units.

This unit is the half whose writes are the step module, its self-test and its help page: 9 MEDIUM and
11 LOW findings. Each is named by its report id and is its own scope item, including where the report
merged ids into one item. The other half, the lander's arm and the spec template, is
`TOOL-dSafePassage-50`. These minors land on units 4, 43, 44 and 45, so this unit repairs none in
particular and builds after every unit, at order 13.

Where a minor would bite an earlier pass, the faulted unit's own §3 hands-off bullet to this unit
names it, so that pass may build it. Where a finding's defect is the text of a spec built before this
one, the item states the superseding reading. A criterion here observes it where anything can.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| D-3 | MEDIUM | 1, 11, 18 | S1, S2, S3 |
| D-4 | MEDIUM | 19 | S4 |
| D-5 | MEDIUM | 2 | S5 |
| D-6 | MEDIUM | 3 | S6 |
| D-7 | MEDIUM | 26 | S7 |
| D-8 | MEDIUM | 27 | S8 |
| D-9 | MEDIUM | 29 | S9 |
| D-11 | LOW | 4 | S10 |
| D-13 | LOW | 6 | S11 |
| D-14 | LOW | 7, 20 | S12, S13 |
| D-15 | LOW | 25 | S14 |
| D-16 | LOW | 12 | S15 |
| D-17 | LOW | 15 | S16 |
| D-18 | LOW | 16 | S17 |
| D-19 | LOW | 31 | S18 |
| D-20 | LOW | 32 | S19 |
| D-21 | LOW | 33 | S20 |

That is 9 MEDIUM and 11 LOW findings by raw id. The report refuted six, ids 14, 21, 22, 23, 24 and 28,
and left none unverified. D-15's other ids, 8, 13 and 17, cite TOOL-dSafePassage-46 alone and are
`TOOL-dSafePassage-50`'s. The skeptic re-graded id 1 from high to medium and ids 4 and 20 from medium to
low. It REJECTED the finders' fixes of ids 11, 25, 26 and 29, so S2, S14, S7 and S9 are built from the
skeptic's corrected fixes. Ids 26 and 27 are the defects of the highs 9 and 10, found at a second grade.
Their items here add what the second finding found beyond the high's edit.

## 2. Scope (IN)

### Which pass observes the reverse walk's stop rows (D-3, D-4)

- **S1** — id 1. TOOL-dSafePassage-43's AC3 is read as observed at TOOL-dSafePassage-4's pass, never at
  TOOL-dSafePassage-43's. Its two plants, `down-fails` and `witness-stays`, are minted by
  TOOL-dSafePassage-4's §4 Inventory, and that unit builds after TOOL-dSafePassage-43 (S4).
  TOOL-dSafePassage-43 keeps AC1, the writer probe, and AC2, the reader. TOOL-dSafePassage-43's §3
  hands-off bullet to this unit names the reading. NOT OBSERVED: a reading of which pass observes
  another unit's criterion; S2 carries the observation into TOOL-dSafePassage-4's AC4.
- **S2** — id 11, the skeptic's corrected fix. TOOL-dSafePassage-4's AC4 is read with one more clause:
  each failure text the `down-fails` and `witness-stays` plants leave opens with an entry of
  `DOWN_STOP_PREFIXES` (TOOL-dSafePassage-43 S1). TOOL-dSafePassage-4's §3 hands-off bullet to this
  unit carries the reading to that pass. Observed by AC1, a regression guard here.
- **S3** — id 18. TOOL-dSafePassage-43's §7 `New arm:` line is read as covering AC1 only: the writer
  probe over the rows of its §4 table. Its rollback-plant half is TOOL-dSafePassage-4's arm in
  `tools/govkit/selftest.py`, which already runs every `rollback` plant. So TOOL-dSafePassage-43's arm
  needs only TOOL-dSafePassage-3's `set_step_state` and can be staged red at its own pass. NOT
  OBSERVED: a reading of another unit's arm line; the main loop observes both arms at the close.
- **S4** — id 19. TOOL-dSafePassage-4 builds strictly after TOOL-dSafePassage-43. Struck at rev-6
  as a header move, because the relation already held and no header can now carry it (§8 F1). The
  premise that the `order` field is the only carrier was wrong. `--dispatch`'s edge refusal,
  TOOL-dTrueNorth-16 S2 in `tools/unattended/unattended.sh:13857-13926`, refuses a unit while a
  same-build unit it consumes from is neither CLOSED nor WONTDO. The build run dispatched
  TOOL-dSafePassage-43, -7 and -2 before TOOL-dSafePassage-4, and TOOL-dSafePassage-4 before -18 and
  -19, by `memory/builds/dSafePassage/RUN.md`'s dispatch rows. All six specs are CLOSED, so no pass
  writes their headers. NOT OBSERVED: a finished dispatch sequence, which no write of this unit
  moves; TOOL-dSafePassage-51 AC1 reads it from the `Pass:` trailers.

### The step row's one rule (D-5, D-9, D-17, D-21)

- **S5** — id 2. TOOL-dSafePassage-4 S4 move 1 lets a `rolled-back` row whose witness holds go on. Its
  move 3 then records that row `applied` with the `down interrupted:` failure, as TOOL-dSafePassage-39
  S3 does for an unrecorded row, and never `rolled-back` with a failure. Its `via` follows
  TOOL-dSafePassage-39 S3's rule, because no up is on record since the last down completed.
  TOOL-dSafePassage-4 §4's row "`rolled-back`, or none · witness holds · as an `applied` row" is read
  with that state. The `rollback` family gains `rolled-back-witness-holds`. `derive_reverse_steps`
  skips a row the receipt records `rolled-back` (`tools/govkit/upgrade_steps.py:1957` at
  `9e91439d0`), so the plant records s2 `rolled-back` after the rows are derived and before
  `run_reverse_walk` reads the receipt, for example in the reverse child the fixture spawns. A plant
  that records it before the derivation never reaches move 1. TOOL-dSafePassage-4's and
  TOOL-dSafePassage-43's §3 hands-off bullets to this unit name the reading. Observed by AC3.
- **S9** — id 29, the skeptic's corrected fix. A row's `failure` is absent, `null` (read as absent) or
  a non-empty `str`. Any other type, and the empty string, is refused naming the step, in every state.
  TOOL-dSafePassage-43 §4's table is read with that row first. Observed by AC4.
- **S16** — id 15. The row rule is one predicate, `test_step_row(step_id, state, failure)` in
  `tools/govkit/upgrade_steps.py`, beside `set_step_state`, in TOOL-dSafePassage-16's shape for
  `test_steps_recordable`. It raises `Refusal` naming the step and the text on every refused row of
  §4 "The row rule", and returns `None` on an admitted one. `set_step_state` and `read_step_states`
  both call it and restate none of it, so TOOL-dSafePassage-43 S3's "the reader inherits it" is read
  as that call. The rollback fixture's own stop check, `s.startswith(DOWN_STOP_PREFIXES)` at
  `tools/govkit/upgrade_steps.py:4405` at `9e91439d0`, compares through `test_step_row` too, so the
  module holds one such call. Observed by AC4 and AC5.
- **S20** — id 33. The step-row arm stages a second failing case: a writer copy that admits any
  `failure` on an `applied` row, under which the `interrupted: started …` and `exit 1: x` rows go red.
  It is declared on this unit's `New arm:` line beside S16's agreement rows. Observed by AC4, whose
  arm's second staged break this is.

### The stop texts' one source (D-14)

- **S12** — id 7. The edge pair TOOL-dSafePassage-43 **hands-off** TOOL-dSafePassage-33 and
  TOOL-dSafePassage-33 **consumes-from** TOOL-dSafePassage-43 is written by this disposal. So
  TOOL-dSafePassage-33's pass builds S3's `witness still holds after down; before-image <path> absent`
  from `DOWN_STOP_PREFIXES`. Observed by AC6.
- **S13** — id 20. "Built from the constant" (TOOL-dSafePassage-43 S1) is observed: in
  `tools/govkit/upgrade_steps.py`, every string constant that opens with an entry of
  `DOWN_STOP_PREFIXES` lies inside that constant's own assignment. This includes each literal part of
  an f-string, and fixture code compares through the constant too. At `9e91439d0` the rollback
  fixture's `down exit 1: fx: s3 down fails by its plant` and its s2 twin (`:4401-4402`) are retyped
  literals, so the pass builds both from `DOWN_STOP_PREFIXES`. Observed by AC6.

### The ssh remote at TOOL-44's pass (D-6, D-13)

- **S6** — id 3. TOOL-dSafePassage-44's pass removes TOOL-dSafePassage-35 S8's `remote.<x>.url` and
  `remote.<x>.pushurl` rows of `STEP_REFUSED_KEYS`. It takes that half of TOOL-dSafePassage-45 S19
  forward, because `test_credential_bearing` refuses every URL those rows refused (TOOL-dSafePassage-38
  S1), and the ssh exemption lives there alone. The rest of S19 stays TOOL-dSafePassage-45's.
  TOOL-dSafePassage-44's AC1 is read with one more clause: `STEP_REFUSED_KEYS` holds no
  `remote.<x>.url` or `remote.<x>.pushurl` row. The edge pair TOOL-dSafePassage-44 **consumes-from**
  TOOL-dSafePassage-35 and its mirror are written by this disposal, and TOOL-dSafePassage-44's
  hands-off bullet to this unit names the reading.
  **Readers:** by name: READER NOT IN TREE, because the two rows, their table `STEP_REFUSED_KEYS`
  and its matcher `check_target_local_config` are minted in `tools/govkit/upgrade_steps.py` by
  TOOL-dSafePassage-29 and TOOL-dSafePassage-35, unbuilt at the base, so no tracked file spells them
  yet; at their landing the readers are `check_target_local_config` and TOOL-dSafePassage-29 S3's
  class arm in `tools/govkit/selftest.py`, whose kept keys end in `command` or `cmd` and so never
  match either row · by value: `test_credential_bearing` (TOOL-dSafePassage-38 S1), which refuses
  every URL the two rows refused and keeps the ssh-scheme bare user. Observed by AC7.
- **S11** — id 6. TOOL-dSafePassage-44's AC2 is read with a floor. The probe fails when
  `tools/runlog/redaction.tsv` has no `url-userinfo` row, and asserts that at least one token of its
  `negative` cell holds `://` and that `ssh://git@github.com/o/r.git` is among them. Observed by AC8.

### The walk's second refusal (D-7)

- **S7** — id 26, the skeptic's corrected fix, beside TOOL-dSafePassage-47's walk. Each candidate that
  TOOL-dSafePassage-47 S1 classifies also runs `git --git-dir=<c> rev-parse --git-dir`. A non-zero exit
  is a refusal naming the candidate, whatever its stderr says. This unit's probe on node d, git
  2.54.0.windows.1, 2026-10-23, set `core.repositoryformatversion` to 99 in a submodule's git
  directory. `rev-parse --git-dir` exited 128 with `fatal: Expected git repo version <= 1, found 99`,
  while `config --list` exited 0 with a warning. So TOOL-dSafePassage-47's read alone lists a
  repository git will not open and grades keys no step can reach through git. The `isolation` family
  gains `submodule-format-unknown`. Observed by AC9.

### The send-email identity forms, held by the arm (D-8)

- **S8** — id 27. TOOL-dSafePassage-29 S3's class arm widens each key it keeps, `<section>.<name>`, to
  `<section>.dsp49.<name>` wherever `git help --config` lists a line of the shape
  `<section>.<placeholder>.*`. It asserts that the widened key matches a row of `STEP_REFUSED_KEYS` or
  `STEP_UNREFUSED_KEYS` as well. The arm also keeps every key of `UNLISTED_EXECUTOR_KEYS`, which holds
  `sendemail.sendmailCmd`, the key TOOL-dSafePassage-48 S2 refuses though git's listing omits it. So
  the arm goes red on a table that lacks an identity form or the `sendmailCmd` row. Where a widened key
  matches no row, the pass adds the row the arm demands. Observed by AC10.

### Criteria read against their claims (D-11, D-18)

- **S10** — id 4. TOOL-dSafePassage-45's AC12 and S20 are read case-sensitively. The refusal line
  holds the exact bytes `gc.recentobjectshook` that `git config --list` prints, and does not hold
  `gc.recentObjectsHook`. TOOL-dSafePassage-45's hands-off bullet to this unit names the reading.
  Observed by AC11.
- **S17** — id 16. TOOL-dSafePassage-44's AC3 and TOOL-dSafePassage-45's AC2 second half are read
  over the "What a step can reach" section alone, extracted by §4 "The section probe". TOOL-44's AC3
  asserts a line holding both `ssh://` and `not refused`. TOOL-45's AC2 asserts a line holding
  `protocol.ext.allow`. At `9e91439d0` the two ssh tokens sit on adjacent lines,
  `help/upgrade-steps.md:104-105`, so the pass reflows that sentence until one line carries both.
  Observed by AC12.

### The `.gitmodules` read and the redactor (D-19, D-20)

- **S18** — id 31. Before TOOL-dSafePassage-45 S13's read, a `<worktree>/.gitmodules` that exists and
  is not a regular file that opens for reading is a refusal naming it. Exit 1 of the read then means
  only "missing, or maps none". The audit's probe found that git exits 1 with only a warning on a
  directory named `.gitmodules`. The `isolation` family gains `gitmodules-unreadable`, a directory
  named `.gitmodules`. Observed by AC13.
- **S19** — id 32. `render_redacted_config` (TOOL-dSafePassage-38 S2) redacts a key's tested
  subsection, `key[first "." + 1 : last "."]` (TOOL-dSafePassage-45 S8), from `<scheme>://` to the
  subsection's last `@`, whatever lies between. TOOL-dSafePassage-45 S9's pattern stays for every
  other text. This unit ran S9's pattern on node d, 2026-10-23: `http.https://u:se/cret@h/.sslkey` and
  `http.https://u:se cret@h/.sslkey` came back unchanged, and the subsection rule returns
  `"http.https://<redacted>@h/.sslkey"` for both. The `isolation` family gains
  `subsection-password-space`, `[http "https://u:se cret@h/"] sslKey = x`. Its output is graded over
  the refusal's named entries, the text between TOOL-dSafePassage-24's fixed lead and tail, and not
  over the whole output as TOOL-dSafePassage-45 AC6 reads its own plants: the lead's ` credential`
  holds `cre` and ` cr`, two pieces of `se cret` (§8 F2). Observed by AC14.

### Readings of pins and figures (D-15, D-16)

- **S14** — id 25, the skeptic's corrected fix. The spec-to-spec line pins of TOOL-dSafePassage-43 §1,
  TOOL-dSafePassage-44 §1 and TOOL-dSafePassage-45 S11 are read by section and item, which an Edges
  bullet added later cannot shift:
  - TOOL-dSafePassage-38 §4 "Data model", the userinfo pattern;
  - TOOL-dSafePassage-26 S33, the lock record;
  - TOOL-dSafePassage-39 AC1;
  - TOOL-dSafePassage-4 §4 "Data model", the four `applied` or `failed` rows.

  NOT OBSERVED: a reading of citations, which no code carries.
- **S15** — id 12. TOOL-dSafePassage-45's PINNED figure is read as "17 of 1004 keys, a key being a
  line of `git help --config` that holds a `.`". On node d, 2026-10-23, 1004 lines held a `.` and two
  did not, the blank line and the footer `'git help config' for more information`. NOT OBSERVED: a
  pinned figure no code reads; TOOL-dSafePassage-45 AC7's kept count is DERIVED.

## 3. Non-goals (OUT)

- Both highs: `TOOL-dSafePassage-47` and `TOOL-dSafePassage-48`.
- The lander's arm and the spec template: `TOOL-dSafePassage-50`.
- Rewriting a built spec. An item that corrects a built spec's text states the reading here. The two
  edge pairs S6 and S12 name are the exception, because their findings ask the disposal to write them.
- The report's left-shift gates and checklist entries.
- The other same-order `consumes-from` edges the driver's id tie-break would build consumer first:
  TOOL-dSafePassage-2 on TOOL-dSafePassage-7, TOOL-dSafePassage-11 on TOOL-dSafePassage-15 and
  TOOL-dSafePassage-12 on TOOL-dSafePassage-8. The same edge refusal held each one, producer first,
  by `memory/builds/dSafePassage/RUN.md`'s dispatch rows `:75` before `:79`, `:85` before `:113` and
  `:117` before `:123`, so no follow-up is owed.

### Edges

- **consumes-from** `TOOL-dSafePassage-4` — move 3, the down table and AC4, which S2 and S5 read; S4's move of its `order` verb is struck at rev-6 (§8 F1)
- **consumes-from** `TOOL-dSafePassage-29` — the class arm and `STEP_UNREFUSED_KEYS`, which S8 widens to identity forms; without the arm there is nothing to widen
- **consumes-from** `TOOL-dSafePassage-43` — `DOWN_STOP_PREFIXES`, the writer rule, its table, AC3 and its arm line, which S1, S3, S5, S9, S13, S16 and S20 amend and read
- **consumes-from** `TOOL-dSafePassage-44` — AC1, AC2 and AC3 and the `ssh-scheme-bare-user` plant, which S6, S11 and S17 read
- **consumes-from** `TOOL-dSafePassage-45` — S8's tested subsection, S9's redactor, S13's read, AC2, AC12, S11's pin and the PINNED figure, which S10, S14, S15, S17, S18 and S19 amend and read
- **consumes-from** `TOOL-dSafePassage-47` — the candidate shape and the config-read refusal, beside which S7 adds the `rev-parse --git-dir` refusal
- **consumes-from** `TOOL-dSafePassage-48` — the send-email rows in both forms, each kept `sendemail.<key>` and its identity form, and the `sendemail.sendmailCmd` row, which S8's arm holds to a derivation
- **hands-off** `TOOL-dSafePassage-51` — F1(a)'s sweep ending on AC2's header probe and amending the Rollouts of TOOL-dSafePassage-2, -7 and -43, both struck at rev-6 with F1(a) and AC2 (§8 F1); S7's `rev-parse` run only after a config read that exited 0; no `UNLISTED_EXECUTOR_KEYS` in the module, the expected key a literal in `tools/govkit/selftest.py`; a staged move-3 copy for AC3; fixture code comparing through `test_step_row`; S18's `stat` before any open, with the `gitmodules-fifo` plant; S6's Readers reason; §4's section probe; and §10's lookups, findings 1, 10, 19, 2, 9, 14, 4, 3, 24, 13, 8 and 18 of the spec audit of units 47 to 50
- **hands-off** `TOOL-dSafePassage-55` — F1(a)'s sweep ending on AC2 run as that unit's one order probe, all four relations, finding 1 of the spec audit of units 51 and 52; struck at rev-6 with F1(a) and AC2 (§8 F1), so this unit leaves that unit nothing, and the edge stays only as the end its mirror reads

## 4. Design

### The row rule

`test_step_row(step_id, state, failure)`, called by `set_step_state` and by `read_step_states`:

| State | `failure` | Outcome |
|---|---|---|
| any | not absent, not `null`, and not a non-empty `str`, such as `5` or `""` | `Refusal` naming the step |
| `applied` | none | admitted |
| `applied` | opens with an entry of `DOWN_STOP_PREFIXES` | admitted |
| `applied` | any other text | `Refusal` naming the step and the text |
| `failed` | a non-empty text | admitted |
| `failed` | none | `Refusal` naming the step |
| `rolled-back` | none | admitted |
| `rolled-back` | a text | `Refusal` naming the step and the text |

### The arm's widening

```
placeholder lines = git help --config lines matching ^([a-z]+)\.<[a-z]+>\.\*$
kept              = TOOL-dSafePassage-29 S3's kept keys  +  UNLISTED_EXECUTOR_KEYS
widened           = { s + ".dsp49." + rest  for  s.rest in kept  if  s names a placeholder line }
assert every key of kept and widened matches a row of STEP_REFUSED_KEYS or STEP_UNREFUSED_KEYS
```

On node d, git 2.54.0.windows.1, 2026-10-23, the placeholder lines were `bundle.<id>.*`,
`credential.<url>.*`, `http.<url>.*` and `sendemail.<identity>.*`. The kept keys they widen were
`credential.helper`, `http.extraHeader`, `sendemail.ccCmd`, `sendemail.headerCmd`,
`sendemail.smtpServer` and `sendemail.toCmd`, six in all. These figures are DERIVED, re-read by the arm
on every run.

### The section probe

```
awk '/^#+ What a step can reach/{f=1;next} /^#+ /{f=0} f' help/upgrade-steps.md
```

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the function `test_step_row` (cell `py.function`, OK by
`python3 tools/lexicon/lexicon.py --suggest test_step_row --as py.function`, 2026-10-23), the constant
`UNLISTED_EXECUTOR_KEYS`, the `rollback` plant `rolled-back-witness-holds`, and the `isolation` plants
`submodule-format-unknown`, `gitmodules-unreadable` and `subsection-password-space`. No conf key, gate
leg or policy key. The row rule's `raise Refusal` sites move from `set_step_state` into
`test_step_row`, and §7's arm reaches each one. `tools/govkit/refusal_join.py`'s `BRANCH_PIN` is a
floor and is not lowered. The refusals of S7 and S18 are TOOL-dSafePassage-24's one `raise Refusal`
site.

### Migration

None: no landed step row, receipt step or rollback record exists before this build lands.

### Rollout

Live at landing. It builds at order 13, after every unit of the build. Its write set is
`tools/govkit/upgrade_steps.py`, `tools/govkit/selftest.py` and `help/upgrade-steps.md`. That set does
not meet `TOOL-dSafePassage-50`'s, and the two run at different orders anyway. No header move is
owed (§8 F1).

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Any header move (S4).** Every unit it would move is CLOSED and was dispatched after the units it
  consumes from, so a moved verb would describe no dispatch still to come (§8 F1).
- **Moving TOOL-dSafePassage-4's AC4 stop rows into TOOL-dSafePassage-43's pass (S1, S2).** The finder's
  fix of id 11, rejected by the skeptic: the plants are TOOL-dSafePassage-4's, and the criterion
  belongs with the walk that writes the rows.
- **Reading git-send-email's option table at run time (S8).** The script is absent where git's email
  package is not installed, so the arm would grade nothing there; `UNLISTED_EXECUTOR_KEYS` names the
  one key found, with its source.
- **Redacting a subsection only when it parses as a URL (S19).** A password holding a space or a `/`
  is exactly the text that does not parse.
- **Folding each minor into its unit's spec.** The disposal promotes, never folds (BUILD-METHOD M4).

## 5. Production-readiness checklist

- security: S7 refuses a submodule git will not open; S8 holds every send-email identity form to an
  arm; S18 refuses an unreadable `.gitmodules`; S19 stops a password holding a space or `/` from
  printing.
- perf / scale: one `rev-parse` per candidate (S7), and one predicate call per row write and read
  (S16).
- error / empty / loading states: a wrong-typed or empty `failure` is a counted problem, never a
  traceback (S9); an unreadable `.gitmodules` is a refusal naming it (S18).
- observability: each refusal names its file or step; S19's redaction prints the scheme and host.
- risks: S7 refuses a submodule of a newer repository format than the installed git knows.
- testing: the probes and plants of §6, through §7's arm.
- migration: none.
- user docs: `help/upgrade-steps.md`, the section S17 scopes, which names S7's and S18's refusals.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant down-fails` and
  `--plant witness-stays` run, and a `python -c` probe reads `DOWN_STOP_PREFIXES`, each stop text the
  two plants leave opens with one of its entries, and neither run prints a `Refusal` traceback.
  Red when: a stop text opens with no entry, or the writer refuses the reverse walk's own stop.
- **AC2** — STRUCK at rev-6, number retained so no cross-reference dangles. It read the `order <n>`
  verbs under `memory/builds/dSafePassage/spec/`, and S4's move was never made. The relation it
  guarded is dispatch order, which `--dispatch`'s edge refusal held: the dispatch rows of
  `memory/builds/dSafePassage/RUN.md` show it (§8 F1). The pass's ledger answers this label in the
  AMENDED form, naming rev-6.
  Red when: never in this unit; no write of this unit's pass can move a header of a CLOSED spec.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant rolled-back-witness-holds`
  runs, its rows line shows `s2` recorded `rolled-back` after `derive_reverse_steps` derived the rows
  and before the walk reached s2 (S5). Then `s2` is downed and ends `rolled-back` with no `failure`,
  no `Refusal` is printed, and the run exits 0.
  Red when: move 3 writes `rolled-back` with a failure and the writer stops the rollback, or the plant
  records s2 before the derivation and s2 never reaches move 1.
- **AC4** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `test_step_row`, `set_step_state` and a `read_step_states` over a one-row receipt for each row of
  §4 "The row rule", the three agree on every row. `failure` valued `5` or `""` is refused in each
  state, with a `Refusal` and no `AttributeError`.
  Red when: the writer and the reader disagree on a row, or a wrong-typed `failure` raises anything but
  `Refusal`.
- **AC5** — When `govkit.py check --target <t>` reads a receipt whose `applied` row carries
  `"failure": 5`, and then `"failure": ""`, each run counts one problem naming the row and prints no
  traceback; and an `ast` walk of `tools/govkit/upgrade_steps.py` finds exactly one call whose
  argument is `DOWN_STOP_PREFIXES` with the method `startswith`, inside `test_step_row`. The walk
  covers the whole module, the rollback fixture included.
  Red when: the reader restates the rule, the fixture's stop check keeps its own `startswith` call,
  or a wrong type escapes as a traceback.
- **AC6** — When a `python -c` probe walks `tools/govkit/upgrade_steps.py` with `ast`, every string
  constant opening with an entry of `DOWN_STOP_PREFIXES`, f-string parts included, sits inside the
  `DOWN_STOP_PREFIXES` assignment. The walk covers the rollback fixture.
  Red when: a stop text, TOOL-dSafePassage-33's or a fixture's `down exit 1:` text included, is a
  retyped literal.
- **AC7** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant ssh-scheme-bare-user`
  runs, it exits 0 with its step spawned; and a `python -c` probe finds no `STEP_REFUSED_KEYS` row whose
  pattern is `remote.<x>.url` or `remote.<x>.pushurl`.
  Red when: a table row refuses the ssh-scheme remote that the predicate keeps.
- **AC8** — When a `python -c` probe runs TOOL-dSafePassage-44's AC2 with S11's floor over
  `tools/runlog/redaction.tsv`, it holds and names `"ssh://git@github.com/o/r.git"` among its tokens; over a
  scratch copy of the table without the `url-userinfo` row, it fails naming the row.
  Red when: the probe passes with zero tokens tested.
- **AC9** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-format-unknown`
  runs, the step is refused before any spawn, naming the submodule's git directory under
  `.git/modules/`, and the run exits 1.
  Red when: the repository is listed and graded although git will not open it.
- **AC10** — When `git help --config` runs on node d and a `python -c` probe applies §4 "The arm's
  widening", every kept and widened key matches a row; over a copy of `STEP_REFUSED_KEYS` without the
  `sendemail.<x>.ccCmd` form the probe names `sendemail.dsp49.cccmd`; and over a copy without the
  `sendemail.sendmailCmd` row it names that key.
  Red when: an identity form or the unlisted key can be dropped and the probe stays green.
  figure: the widened count is DERIVED; six were read on node d on 2026-10-23.
- **AC11** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant local-recent-objects-hook`
  runs, its refusal line holds the exact bytes `gc.recentobjectshook` and `.git/config`, and does not
  hold `gc.recentObjectsHook`.
  Red when: the refusal re-cases the key git printed.
- **AC12** — When §4 "The section probe" runs over `help/upgrade-steps.md`, its output holds one line
  with both `ssh://` and `not refused`, and a line holding `protocol.ext.allow`.
  Red when: either claim sits outside the section, the ssh sentence still wraps its two tokens onto
  two lines, or the ssh line says the URL is refused.
- **AC13** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant gitmodules-unreadable`
  runs, the step is refused naming the `.gitmodules` path, and the run exits 1.
  Red when: the directory is read as a missing file and every name is marked `by name`.
- **AC14** — When a probe calls `render_redacted_config` on `"http.https://u:se\x20cret@h/.sslkey"`,
  `\x20` the space, and on `"http.https://u:se/cret@h/.sslkey"`, each returns
  `"http.https://<redacted>@h/.sslkey"`. And when
  `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant subsection-password-space` runs,
  it exits 1, and a probe grades its output in two spans:
  - the refusal's named entries, the text after `sends as a credential, ` and before
    `, so nothing was spawned` on the refusal line, the fixed lead and tail of TOOL-dSafePassage-24's
    `Refusal` in `run_step_isolated` (`tools/govkit/upgrade_steps.py:1609-1611` at `9e91439d0`). It
    holds `"http.https://<redacted>@h/.sslkey in .git/config"` and no 3-character piece of the planted
    password `se cret`;
  - the whole output, which holds neither the password nor any of its space-separated halves of 3 or
    more characters, here `cret`.
  Red when: a password holding a space or `/` prints, or the entries span is absent or names no
  entry. The trap this grading avoids: every 3-character piece graded over the whole output is red
  by construction, because the fixed lead's ` credential` holds `cre` and ` cr`. The 2-character
  half `se` sits in the lead's `sends` for the same reason (§8 F2).
  figure: the 3-character floor is TOOL-dSafePassage-45 AC6's "longer than 2 characters", kept.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC3 AC4 AC9 AC10 AC13 AC14 · the self-test runs the step-row agreement over §4's table and the four plants, and the widened class arm; its failing cases are staged by a writer copy admitting any `failure` on an `applied` row, a reader copy restating the rule, a walk copy without the `rev-parse` refusal, a table copy without `sendemail.<x>.ccCmd`, a `.gitmodules` read with no file test and a redactor copy stopping at a space, AC14's plant graded over the refusal's named entries and never over its fixed lead · none

What the check does not cover: a stop text whose opening is right and whose rest is wrong, a key git's
scripts read that neither its listing nor `UNLISTED_EXECUTOR_KEYS` names, and a password piece that
the refusal's fixed text happens to spell, which AC14 grades only inside the named entries.

## 8. Open questions

- **F1 — Who writes S4's order move, and when?** `tools/workflows/unattended-build.js` reads the
  `order` verb when it sorts the roster (`:608-613`), before any pass runs. So this unit's own pass at
  order 13 cannot move TOOL-dSafePassage-4 ahead of its order-2 dispatch, and the disposal that
  promoted this unit writes only its specs and their edges.
  - (a) The M3 sweep of the run that next hands out the roster applies S4 before the hand-out. It
    makes a rev bump of TOOL-dSafePassage-4, TOOL-dSafePassage-18 and TOOL-dSafePassage-19, each §9
    line naming this unit's S4, and amends each one's §4 Rollout sentence naming its order. The build
    order region is then re-rendered. AC2 reads the result.
  - (b) The same sweep moves TOOL-dSafePassage-43 to order 1 instead, one header, relying on the id
    tie-break that sorts TOOL-dSafePassage-3 first. It fails AC2 and leaves TOOL-dSafePassage-4
    before TOOL-dSafePassage-7.
  - (c) The driver's tie-break follows `consumes-from` edges within an order. That is a change to
    `tools/workflows/unattended-build.js`, outside this build's goal, and it too lands after this
    run's roster is sorted.
  - Recommendation: (a), the skeptic's judged-sound fix and the only option AC2 admits.
  - RESOLVED (agent, 2026-10-23, delegated): (a), on rung 3 of the execution plan's fork rule
    (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:901-948`):
    the mandate delegates the fork, and M3 takes the most feature-rich option that survives the vetoes.
    (a) is the only option AC2 admits. (b) fails AC2, which is veto 1. (c) changes
    `tools/workflows/unattended-build.js`, outside this build's goal, which is veto 2, and no grant names
    it. The run that applies (a) is this build's build run, before it hands out the roster.
  - (d), added at rev-6: no header move. The relation the order verbs stood for is dispatch order,
    and `--dispatch`'s edge refusal (`tools/unattended/unattended.sh:13857-13926`) holds it for every
    `consumes-from` edge, whatever the headers read.
  - Re-opened at rev-6, because (a) was never applied and cannot be now. TOOL-dSafePassage-4, -7,
    -18, -19 and -43 are CLOSED with their headers at orders 2, 2, 3, 3 and 2, and a CLOSED spec's
    header is no pass's to write. The build run dispatched them by `consumes-from` instead, as the
    build brief's order states
    (`memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-49-build-brief.md:10`)
    and the dispatch rows of `memory/builds/dSafePassage/RUN.md` record:
    TOOL-dSafePassage-3 at `:55`, -43 at `:71`, -7 at `:75`, -2 at `:79`, -4 at `:81`, -18 at `:91`
    and -19 at `:95`. Every relation AC2 named holds in that sequence. RESOLVED (agent, 2026-10-28,
    delegated): (d), on the main loop's recommendation in
    `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-49-1-spec-writer.md`.
    (a) is struck, AC2 is struck and S4 is NOT OBSERVED. (b) and (c) are moot for the same reason:
    no dispatch they could order is still to come.
- **F2 — Which halves of the planted password does AC14 grade over the whole output?** The main
  loop recommended each space-separated half.
  - (a) Every half. `se cret`'s half `se` sits in the fixed lead's `sends`, so AC14 would be red by
    construction, the trap the revision exists to close.
  - (b) Each half of 3 or more characters, the floor the entries span already uses, so every future
    password is graded by one rule.
  - (c) A plant password whose halves are each 3 characters or longer. It moves S19's measured texts
    and AC14's redactor inputs for no gain over (b).
  - Recommendation: (b).
  - RESOLVED (agent, 2026-10-28, delegated): (b). The recommendation is taken except for halves
    shorter than 3 characters, which the code shows would break AC14 as written.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 43 to 46's 9 MEDIUM and 11
  LOW findings of the step module, one scope item per raw id.
- rev-2 · 2026-10-23 · §8 · F1 RESOLVED (agent, delegated) to (a) on rung 3: this build's build run
  applies S4's order move before it hands out the roster.
- rev-3 · 2026-10-23 · §3 · the Edges gain the end this unit owes the promotion `TOOL-dSafePassage-51` of the spec audit of units 47 to 50, written by the disposal stage; no other section moved.
- rev-4 · 2026-10-23 · §3 · the Edges gain the end this unit owes the promotion `TOOL-dSafePassage-55` of the spec audit of units 51 and 52, written by the disposal stage; no other section moved.
- rev-5 · 2026-10-26 · §3 Edges · AC8 · AC14 · §7 · the TOOL-dSafePassage-48 consumes-from bullet names
  `sendemail.<key>`; AC8's URL and AC14's redactor texts are string literals, the space spelled `\x20`; the
  §7 leg line gains `policy fixtures`, whose guard a §4 Files touched path trips, per the spec-tokens
  repair handoff
  `memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-31-1-spec-writer.md`; no
  criterion's meaning moved.
- rev-6 · 2026-10-28 · S4 · S5 · S13 · S16 · S17 · S19 · §3 · §4 · §5 · AC2 · AC3 · AC5 · AC6 · AC12 ·
  AC14 · §7 · §8 · the builder's divergence, folded per
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-49-1-spec-writer.md`:
  AC14 grades the refusal's named entries for 3-character pieces and the whole output for the
  password and its halves of 3 or more characters, F2 recording the rejected 2-character half; F1
  re-resolved to (d), so F1(a)'s sweep, S4's move, §4 "The order move" and AC2 are struck, citing
  RUN.md's dispatch rows; the rebuild notes folded into AC3, AC5, AC6 and AC12.

## 10. Reuse audit

The seams extended are named per item: TOOL-dSafePassage-3's `set_step_state` and `read_step_states`
in TOOL-dSafePassage-16's predicate shape, TOOL-dSafePassage-43's `DOWN_STOP_PREFIXES`,
TOOL-dSafePassage-4's reverse walk and plants, TOOL-dSafePassage-29's class arm,
TOOL-dSafePassage-38's redactor, TOOL-dSafePassage-45's `.gitmodules` read and TOOL-dSafePassage-47's
walk, all specced and unbuilt at the base. `python tools/codebase-map/reuse_lookup.py "classify a directory as a git repository by its layout"`
and `"refuse a config key under a send-email identity"` ranked `git`, `run_git`, `classify`, `key`
and `read_conf_key`, name-token matches, so no existing seam fits beyond those specs. Rev-6 adds no
seam. AC14's span is bounded by two fixed pieces of TOOL-dSafePassage-24's `Refusal` in
`run_step_isolated`, whose `a credential, ` and `, so nothing was spawned` the `[dSP-24]` needles in
`tools/govkit/selftest.py` already pin. F1's re-resolution reads the existing edge refusal in
`tools/unattended/unattended.sh:13857-13926`, which already guards what S4's move was for.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit finding on a submodule walk or a refused executor key is promoted and its reading carried to the faulted unit" --terms "spec audit promoted reading hands-off submodule walk repository shape refused executor sendemail identity"`
