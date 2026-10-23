# TOOL-dSafePassage-49 — the spec audit of units 43 to 46, the step module's 20 minors: one step-row predicate, TOOL-4 after TOOL-43, a second walk refusal, identity forms held by the arm, declared exits, and the readings that cite them

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 13 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-49-deviation-95.md](../build/2026-10-23-build-TOOL-dSafePassage-49-deviation-95.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-49-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-49-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-49-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-49-hygiene-fix.md) | research | — |

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
- **S4** — id 19. TOOL-dSafePassage-4 builds strictly after TOOL-dSafePassage-43. The build driver
  sorts the roster by `order` and breaks a tie by id string (`tools/workflows/unattended-build.js:608-613`),
  `TOOL-dSafePassage-4` sorts before `TOOL-dSafePassage-43`, and dispatch is strictly sequential
  (`:76-82`). So the order field is the only carrier. TOOL-dSafePassage-4 takes order 3, and its two
  consumers now at order 3, TOOL-dSafePassage-18 and TOOL-dSafePassage-19, take order 4, as §4
  "The order move" derives. The field is read when the roster is handed out, before any pass, so no
  pass of this unit can write it: §8 F1. Observed by AC2.

### The step row's one rule (D-5, D-9, D-17, D-21)

- **S5** — id 2. TOOL-dSafePassage-4 S4 move 1 lets a `rolled-back` row whose witness holds go on. Its
  move 3 then records that row `applied` with the `down interrupted:` failure, as TOOL-dSafePassage-39
  S3 does for an unrecorded row, and never `rolled-back` with a failure. Its `via` follows
  TOOL-dSafePassage-39 S3's rule, because no up is on record since the last down completed.
  TOOL-dSafePassage-4 §4's row "`rolled-back`, or none · witness holds · as an `applied` row" is read
  with that state. The `rollback` family gains `rolled-back-witness-holds`. TOOL-dSafePassage-4's and
  TOOL-dSafePassage-43's §3 hands-off bullets to this unit name the reading. Observed by AC3.
- **S9** — id 29, the skeptic's corrected fix. A row's `failure` is absent, `null` (read as absent) or
  a non-empty `str`. Any other type, and the empty string, is refused naming the step, in every state.
  TOOL-dSafePassage-43 §4's table is read with that row first. Observed by AC4.
- **S16** — id 15. The row rule is one predicate, `test_step_row(step_id, state, failure)` in
  `tools/govkit/upgrade_steps.py`, beside `set_step_state`, in TOOL-dSafePassage-16's shape for
  `test_steps_recordable`. It raises `Refusal` naming the step and the text on every refused row of
  §4 "The row rule", and returns `None` on an admitted one. `set_step_state` and `read_step_states`
  both call it and restate none of it, so TOOL-dSafePassage-43 S3's "the reader inherits it" is read
  as that call. Observed by AC4 and AC5.
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
  an f-string, and fixture code compares through the constant too. Observed by AC6.

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
  `protocol.ext.allow`. Observed by AC12.

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
  `http.https://<redacted>@h/.sslkey` for both. The `isolation` family gains
  `subsection-password-space`, `[http "https://u:se cret@h/"] sslKey = x`, which TOOL-dSafePassage-45
  AC6's no-substring assertion covers. Observed by AC14.

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
- The other same-order `consumes-from` edges the driver's id tie-break builds consumer first:
  TOOL-dSafePassage-2 on TOOL-dSafePassage-7, TOOL-dSafePassage-11 on TOOL-dSafePassage-15 and
  TOOL-dSafePassage-12 on TOOL-dSafePassage-8. No finding of this audit names them. S4 also moves
  TOOL-dSafePassage-4 past TOOL-dSafePassage-7, and the rest are a follow-up for the owner.

### Edges

- **consumes-from** `TOOL-dSafePassage-4` — move 3, the down table, AC4 and the `order` verb, which S2, S4 and S5 read and move
- **consumes-from** `TOOL-dSafePassage-29` — the class arm and `STEP_UNREFUSED_KEYS`, which S8 widens to identity forms; without the arm there is nothing to widen
- **consumes-from** `TOOL-dSafePassage-43` — `DOWN_STOP_PREFIXES`, the writer rule, its table, AC3 and its arm line, which S1, S3, S5, S9, S13, S16 and S20 amend and read
- **consumes-from** `TOOL-dSafePassage-44` — AC1, AC2 and AC3 and the `ssh-scheme-bare-user` plant, which S6, S11 and S17 read
- **consumes-from** `TOOL-dSafePassage-45` — S8's tested subsection, S9's redactor, S13's read, AC2, AC12, S11's pin and the PINNED figure, which S10, S14, S15, S17, S18 and S19 amend and read
- **consumes-from** `TOOL-dSafePassage-47` — the candidate shape and the config-read refusal, beside which S7 adds the `rev-parse --git-dir` refusal
- **consumes-from** `TOOL-dSafePassage-48` — the send-email rows in both forms and the `sendemail.sendmailCmd` row, which S8's arm holds to a derivation

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

### The order move

S4's move, derived from every spec's §3 `consumes-from` bullets and `order` verbs at 2828457d. A
unit moves only when a unit it consumes from reaches its order, and only these three do:

| Unit | Order now | Order after S4 | Consumes from, with orders after S4 |
|---|---|---|---|
| `TOOL-dSafePassage-43` | 2 | 2 | TOOL-dSafePassage-3 (1) |
| `TOOL-dSafePassage-4` | 2 | 3 | TOOL-dSafePassage-1, -3 (1); -2, -7, -43 (2) |
| `TOOL-dSafePassage-18` | 3 | 4 | TOOL-dSafePassage-16 (2); -4 (3) |
| `TOOL-dSafePassage-19` | 3 | 4 | TOOL-dSafePassage-2, -16 (2); -4 (3); -18 (4, built first by id) |

No unit consuming from TOOL-dSafePassage-18 or TOOL-dSafePassage-19 sits below order 5.

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
not meet `TOOL-dSafePassage-50`'s, and the two run at different orders anyway. S4's header move is not
in this write set: §8 F1 places it before the roster is handed out.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Moving TOOL-dSafePassage-43 to order 1 (S4).** It relies on the id tie-break within order 1,
  leaves a same-order `consumes-from`, and leaves TOOL-dSafePassage-4 before TOOL-dSafePassage-7, which
  it consumes; AC2 refuses it.
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
- risks: S4 moves three build orders before the roster is handed out, which §8 F1 places; S7
  refuses a submodule of a newer repository format than the installed git knows.
- testing: the probes and plants of §6, through §7's arm.
- migration: none.
- user docs: `help/upgrade-steps.md`, the section S17 scopes, which names S7's and S18's refusals.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant down-fails` and
  `--plant witness-stays` run, and a `python -c` probe reads `DOWN_STOP_PREFIXES`, each stop text the
  two plants leave opens with one of its entries, and neither run prints a `Refusal` traceback.
  Red when: a stop text opens with no entry, or the writer refuses the reverse walk's own stop.
- **AC2** — When a `python -c` probe reads the `order <n>` verb of each spec under
  `memory/builds/dSafePassage/spec/`, TOOL-dSafePassage-43's order is greater than
  TOOL-dSafePassage-3's, TOOL-dSafePassage-4's is greater than TOOL-dSafePassage-43's and
  TOOL-dSafePassage-7's, and TOOL-dSafePassage-18's and TOOL-dSafePassage-19's are greater than
  TOOL-dSafePassage-4's.
  Red when: TOOL-dSafePassage-4 shares an order with a unit it consumes from.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant rolled-back-witness-holds`
  runs, `s2` is downed, ends `rolled-back` with no `failure`, no `Refusal` is printed, and the run
  exits 0.
  Red when: move 3 writes `rolled-back` with a failure and the writer stops the rollback.
- **AC4** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `test_step_row`, `set_step_state` and a `read_step_states` over a one-row receipt for each row of
  §4 "The row rule", the three agree on every row. `failure` valued `5` or `""` is refused in each
  state, with a `Refusal` and no `AttributeError`.
  Red when: the writer and the reader disagree on a row, or a wrong-typed `failure` raises anything but
  `Refusal`.
- **AC5** — When `govkit.py check --target <t>` reads a receipt whose `applied` row carries
  `"failure": 5`, and then `"failure": ""`, each run counts one problem naming the row and prints no
  traceback; and an `ast` walk of `tools/govkit/upgrade_steps.py` finds exactly one call whose
  argument is `DOWN_STOP_PREFIXES` with the method `startswith`, inside `test_step_row`.
  Red when: the reader restates the rule, or a wrong type escapes as a traceback.
- **AC6** — When a `python -c` probe walks `tools/govkit/upgrade_steps.py` with `ast`, every string
  constant opening with an entry of `DOWN_STOP_PREFIXES`, f-string parts included, sits inside the
  `DOWN_STOP_PREFIXES` assignment.
  Red when: a stop text, TOOL-dSafePassage-33's included, is a retyped literal.
- **AC7** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant ssh-scheme-bare-user`
  runs, it exits 0 with its step spawned; and a `python -c` probe finds no `STEP_REFUSED_KEYS` row whose
  pattern is `remote.<x>.url` or `remote.<x>.pushurl`.
  Red when: a table row refuses the ssh-scheme remote that the predicate keeps.
- **AC8** — When a `python -c` probe runs TOOL-dSafePassage-44's AC2 with S11's floor over
  `tools/runlog/redaction.tsv`, it holds and names `ssh://git@github.com/o/r.git` among its tokens; over a
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
- **AC12** — When §4 "The section probe" runs over `help/upgrade-steps.md`, its output holds a line with
  both `ssh://` and `not refused`, and a line holding `protocol.ext.allow`.
  Red when: either claim sits outside the section, or the ssh line says the URL is refused.
- **AC13** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant gitmodules-unreadable`
  runs, the step is refused naming the `.gitmodules` path, and the run exits 1.
  Red when: the directory is read as a missing file and every name is marked `by name`.
- **AC14** — When a probe calls `render_redacted_config("http.https://u:se cret@h/.sslkey")` and
  `render_redacted_config("http.https://u:se/cret@h/.sslkey")`, each returns
  `http.https://<redacted>@h/.sslkey`; and `--plant subsection-password-space` prints no substring of
  `se cret` longer than 2 characters.
  Red when: a password holding a space or `/` prints.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC3 AC4 AC9 AC10 AC13 AC14 · the self-test runs the step-row agreement over §4's table and the four plants, and the widened class arm; its failing cases are staged by a writer copy admitting any `failure` on an `applied` row, a reader copy restating the rule, a walk copy without the `rev-parse` refusal, a table copy without `sendemail.<x>.ccCmd`, a `.gitmodules` read with no file test and a redactor copy stopping at a space · none

What the check does not cover: a stop text whose opening is right and whose rest is wrong, a key git's
scripts read that neither its listing nor `UNLISTED_EXECUTOR_KEYS` names, and an order inversion
between units no `consumes-from` bullet joins.

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

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 43 to 46's 9 MEDIUM and 11
  LOW findings of the step module, one scope item per raw id.

## 10. Reuse audit

The seams extended are named per item: TOOL-dSafePassage-3's `set_step_state` and `read_step_states`
in TOOL-dSafePassage-16's predicate shape, TOOL-dSafePassage-43's `DOWN_STOP_PREFIXES`,
TOOL-dSafePassage-4's reverse walk and plants, TOOL-dSafePassage-29's class arm,
TOOL-dSafePassage-38's redactor, TOOL-dSafePassage-45's `.gitmodules` read and TOOL-dSafePassage-47's
walk, all specced and unbuilt at the base. `python tools/codebase-map/reuse_lookup.py "classify a directory as a git repository by its layout"`
and `"refuse a config key under a send-email identity"` ranked `git`, `run_git`, `classify`, `key`
and `read_conf_key`, name-token matches, so no existing seam fits beyond those specs. The order move
was derived from every spec's §3 bullets and `order` verbs, and the driver's sort was read at
`tools/workflows/unattended-build.js:608-613`, not taken from a record.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit finding on a submodule walk or a refused executor key is promoted and its reading carried to the faulted unit" --terms "spec audit promoted reading hands-off submodule walk repository shape refused executor sendemail identity"`
