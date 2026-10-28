# TOOL-dIndexedDesign-46 — the round-1 audit of units 31 to 38: its 27 minors batched, one writer and one allocator per typed name, one predicate per question, and every vacuous criterion made to observe

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 19 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 |
| [2026-10-28-build-TOOL-dIndexedDesign-41-promoted-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-41-promoted-fix-return.md) | research | TOOL-dIndexedDesign-41 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-41-promoted-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-41-promoted-fix-brief.md) | research | TOOL-dIndexedDesign-41 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-46-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-46-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 31 to 38
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`)
exited CONVERGED with 34 confirmed findings. BUILD-METHOD M4 promotes every MEDIUM and LOW into one batch
unit, or two only where they split into disjoint write sets by M6. They do not split:
`tools/memory-tree/design_lib.py` is written by the overlap writer (S2, S4), the diff number (S6 to S8),
the meet predicate (S10) and the fork join's closed sets (S19), which span every candidate half. This is
that one unit. Each finding is named by report id and is its own scope item, including where the report
merged ids into one item. The minors land on eight units, so this unit repairs no one unit and takes
order 19, above every unit of the build.

| Item | Sev | Id | Lands on | S |
|---|---|---|---|---|
| M1 | MED | 4 | unit 38 S2, AC2 | S1 |
| M2 | MED | 5 | unit 38 S10 | S2 |
| M2 | MED | 15 | unit 38 S10 | S3 |
| M2 | MED | 23 | unit 38 S10 | S4 |
| M3 | MED | 6 | unit 38 S36, AC27 | S5 |
| M4 | MED | 14 | unit 34 S2 | S6 |
| M4 | MED | 35 | unit 34 S2, AC3 | S7 |
| M5 | MED | 34 | unit 34 S2, AC3 | S8 |
| M6 | MED | 18 | unit 38 AC24 | S9 |
| M7 | MED | 21 | unit 37 S1, §10 | S10 |
| M8 | MED | 22 | unit 38 S3 | S11 |
| M9 | MED | 24 | unit 38 S4, AC4 | S12 |
| M10 | MED | 28 | unit 38 S18 | S13 |
| M11 | MED | 33 | unit 35 §5, S4 | S14 |
| M12 | MED | 38 | unit 38 S27, AC21 | S15 |
| M13 | MED | 39 | unit 31 S1, AC3 | S16 |
| L1 | LOW | 7 | unit 35 S5, AC1 | S17 |
| L1 | LOW | 20 | unit 35 S5, §7 | S18 |
| L2 | LOW | 8 | unit 38 S29, unit 32 S1 | S19 |
| L3 | LOW | 9 | unit 38 S22, S26 | S20 |
| L4 | LOW | 10 | unit 38 S38, AC15 | S21 |
| L5 | LOW | 16 | unit 38 S25 | S22 |
| L6 | LOW | 19 | unit 38 §1, §4 | S23 |
| L7 | LOW | 25 | unit 38 S42 | S24 |
| L8 | LOW | 29 | unit 35 §3, unit 38 S14 | S25 |
| L9 | LOW | 30 | units 35 and 38 §4, §7 | S26 |
| L10 | LOW | 40 | unit 36 AC1, AC2 | S27 |

That is 16 MEDIUM and 11 LOW findings by raw id. Ids 5, 15 and 23 share item M2, ids 14 and 35 share
M4, and ids 7 and 20 share L1. Id 33 is the lens-yield part of id 26, whose bookkeeping
`TOOL-dIndexedDesign-44` lands, and ids 14 and 35 are the `diff` side of id 12, whose `fork` side
`TOOL-dIndexedDesign-42` lands.

## 2. Scope (IN)

Every item builds at this unit's pass, on the code its unit built, unless it names an earlier act. A
"ledger note" is §4's rule.

- **S1** — id 4. One population. At this pass, before the close, the main loop runs `tier2-review.js`
  with `coverage: 'only'` over every roster spec that no `coverage-lens` reading pins at its header
  revision, CLOSED included, and commits the record. Unit 38 S2 and AC2 then name one population, every
  roster unit. Ledger note under unit 38 AC2. Observed by AC1.
- **S2** — id 5. One writer of the overlap name. `design_lib.py --overlaps --record` derives no `<n>` of
  its own. It takes the record's file name and `<n>` from `build_records.py`, through S8's allocator.
  Observed by AC2.
- **S3** — id 15. The overlap record's keyed fields. Unit 38 S10's per-kind row for `overlap` requires
  `Policy`, the `design.overlap` value read, and `Read at`, the commit it read. The per-pair rows stay
  unkeyed bullets that the factory's `FIELD` regex does not read, and S10's "the fields unit 2 §4's
  grammar spells" is superseded. Ledger note under unit 38 AC7. Observed by AC3.
- **S4** — id 23. One call for both typed writers. The overlap writer and `--reentry --write` both name
  their file through the same factory call, and `design_lib.py` holds no `-<kind>-<n>.md` name pattern
  of its own. Observed by AC2.
- **S5** — id 6. The step-9 order, bound where `--dispatch` reads it. This is an act ahead of this
  unit's order, at the build run's M2 cross-read before its first code pass. Unit 20's §3 Edges gains
  `consumes-from TOOL-dIndexedDesign-13`, and unit 13's gains the mirrored hands-off, each a rev bump
  whose §9 line names this unit and report id 6. `--dispatch` then refuses unit 20 while unit 13 is not
  CLOSED (`tools/unattended/unattended.sh:13737-13745`), and unit 38 AC27 becomes a check rather than a
  record. Observed by AC4.
- **S6** — id 14. The diff number's scope. A diff record's `<n>` is the next number free within the
  build, the factory's collision scope. That supersedes unit 20 S4's "the next number free for that
  unit" and unit 34 S2's sentence equating the two. Ledger notes under unit 20 AC5 and unit 34 AC3.
  Observed by AC5.
- **S7** — id 35. A fixture that tells the two scopes apart. Take a build holding
  `TOOL-tFix-1-diff-1.md`. A `--reentry --write` for a feature whose first unit is `TOOL-tFix-2` writes
  `-diff-2.md`, and neither record reads malformed. Unit 34 AC3's import grep is dropped, as a ledger
  note under it.
  **Readers:** by name: `grep -n "build_records" design_lib.py`, unit 34 AC3's observation;
  READER NOT IN TREE, because `git grep` finds it spelled only at
  `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-34.md:135`, a record, and no
  tool, gate or guide runs it · by value: NO VALUE READERS — its output is read only by the pass that
  observes unit 34 AC3, and AC5's two-scope fixture observes unit 34 S2 in its place. Observed by AC5.
- **S8** — id 34. The allocator. `derive_next_record_path(root, slug, unit, kind)` in
  `build_records.py` takes `<n>` as one more than the highest `-<kind>-<n>.md` number in the build's
  `build/` folder, over tracked AND on-disk files. It creates the file with exclusive create,
  `open(path, "x")`. On a clash it re-reads and retries once, and a second clash refuses naming the
  path. Observed by AC6.
- **S9** — id 18. Unit 38 AC24's `extract_section_ref` half is observed by behaviour. Unit 7's
  instrument's M1 runs over a scratch Tier-1 spec whose `## 5. Acceptance criteria` maps to
  `section.acceptance` through `extract_section_ref`, while a Tier-2 ordinal map would give
  `section.readiness`. M1 must print the first. Ledger note under unit 38 AC24. Observed by AC7.
- **S10** — id 21. One write-set path predicate. Unit 37's `check_meet_path(tok, files=None)` takes an
  optional tracked-file set. Given one, it answers as `check_path_shaped(tok, files) or check_dir_shaped(tok)`
  answers today (`tools/check-spec-tokens.py:1104-1121`). Given none, it keeps unit 37 S1's shape rule,
  which keeps planned root files. `extract_files_touched` (`:564-583`) calls it with `git ls-files`, so
  one function answers both joins. Observed by AC8.
- **S11** — id 22. The opt-in read once, the driver's way. `check_spec_audit_declared` applies the dated
  rule `check_authorization` applies (`unattended.sh:928-931`, `:3975-3980`, `:4033`): a dated README
  `spec-audit:` key, else a dated `SPEC_AUDIT_DEFAULT` on the default branch, else `review.design` as
  unit 3 reads it. An undated value reads absent. Observed by AC9.
- **S12** — id 24. An act ahead of this unit's order, at unit 38's pass: unit 38 S4's four
  `[[stand-in]]` rows stay in `tools/loop/loop.toml` until ask TOOL-dIndexedDesign-23's reader shape
  lands, the ruling unit 1 §8 F5 made for `item.design.exit`. Unit 38's pass deletes none of them.
  Ledger note under unit 38 AC4 citing F5 and the ask.
  **Readers:** by name: `tools/loop/loop.toml` and its `[[stand-in]]` rows; READER NOT IN TREE, because
  `tools/loop/` is not tracked at HEAD, the loop kit being TOOL-dDeclaredLoop-13's and unbuilt, and
  `git grep` finds `loop.toml` and `[[stand-in]]` spelled only in records under `memory/builds/`
  · by value: NO VALUE READERS — this item deletes no row, so no reader loses one, and the loop kit's
  stand-in reader, TOOL-dDeclaredLoop-13 S8's, is unbuilt at base. Observed by AC10.
- **S13** — id 28. The roles carriers. `python tools/roles/check_roles.py --write` re-renders the
  `gen:roles-catalogue` region of `tools/roles/README.md` after unit 38 S18's `plan` change.
  `tools/roles/README.md:283` and `tools/roles/kit.toml:14` and `:19` say "the harnesses
  `workflows.toml` names", never a count. Observed by AC11.
- **S14** — id 33. The lens-yield row. `deriveLensYield` and `renderStageShape` take the coverage stage
  as an extra row when it dispatched. The row credits its confirmed findings, so a run's confirmed total
  equals the sum of its rows. Observed by AC12.
- **S15** — id 38. Unit 13's definition shapes, listed per extension. For py: `def <s>`, `class <s>`
  or `<s> =` at line start. For sh: `<s>()` or `function <s>`. For js: `function <s>`,
  `(const|let|var) <s> =` or `class <s>`. `<symbol>` is `re.escape`d before it is spliced. Observed by
  AC13.
- **S16** — id 39. Unit 31's required keys are typed. `prompt`, `repo` and `sha_before` must each be
  present and hold a non-empty string, else `--blind` exits 2 naming the case id and the key. Observed
  by AC14.
- **S17** — id 7. Unit 35 S5's agent-cap arm is deleted. It repeats the `verifier fan-out` leg, which
  already feeds every committed harness to the hook. Observed by AC15.
- **S18** — id 20. The leg's own self-test gains the denied half.
  `tools/workflows/check-verifier-fanout.test.sh` gains a fixture harness whose `SPEC_LENSES` holds a
  sixth entry, and the script refuses it. Observed by AC15.
- **S19** — id 8. One home per closed set. Unit 8's fork join (unit 38 S29) reads `Class`, `Level` and
  `Resolver` from `build_records.py`'s per-kind table, and so does any `diff` `Level` test in
  `design_lib.py`. Neither spells the values. Observed by AC16.
- **S20** — id 9. The verbs guide lists unit 38's two refusals: S22's refusal of a `--design-exit` exit
  other than 0 or 1, and S26's `blocked` under `ready-plus-audit`. They go in
  `tools/unattended/VERBS.template.md` and its render. Observed by AC17.
- **S21** — id 10. Unit 38 AC15's `COVERAGE_BRIEF` clause is superseded, being green before order 17.
  S38 is observed by unit 16's ledger note naming the edge, as a ledger note under unit 38 AC15.
  Observed by AC10.
- **S22** — id 16. `PROBE_TIMEOUT_SECONDS = 30` moves from `gen_build_index.py:3679` to `design_lib.py`.
  `gen_build_index.py` reads `design_lib.PROBE_TIMEOUT_SECONDS`, since it imports `design_lib` already
  (`:310`), so no dependency reverses and the bundle wrapper needs no second literal. Observed by AC18.
- **S23** — id 19. The write-set claim corrected. S5 to S7 write `tools/unattended/unattended.sh` and
  only read `REFUSAL_CEILINGS`, and S15 to S17 write `.memory-tree.conf`. Recorded as a ledger note under
  unit 38 AC5, since unit 38 is CLOSED and its §1 and §4 are frozen. Observed by AC10.
- **S24** — id 25. One slug guard. `check_build_slug(slug)` in `tools/memory-tree/backlog.py`, beside
  `SLUG_RE` (`:129`), holds the two-part test now inline at `gen_build_index.py:4141`. `--new-build`,
  `design_lib.py --overlaps --record` and `plan_streams.py write` call it. Observed by AC19.
- **S25** — id 29. The catalogue sentences. BUILD-METHOD M4's "The catalogue is `SPEC_LENSES`"
  (template and render, `:133`) and `tools/memory-tree/README.md:699` name `COVERAGE_BRIEF` beside
  `SPEC_LENSES`, adding at most 40 bytes to the render under M1's 30720. Observed by AC20.
- **S26** — id 30. The render step named. This unit's own template edits name
  `check-protocol-parity.test.sh --render` beside each render line, and §7 lists the parity leg. Units 35
  and 38 get a ledger note under AC2 and AC15 respectively, naming that render command as the step their
  passes used. Observed by AC10.
- **S27** — id 40. Unit 36 AC1 and AC2 are re-observed over the joined paragraph, by `tr '\n' ' '`,
  never one physical line. Ledger note under unit 36 AC1. Observed by AC10.

## 3. Non-goals (OUT)

- Any HIGH of the audit: `TOOL-dIndexedDesign-39` to `-45`.
- Raising `MAX_LENSES`, `REFUSAL_CEILINGS`, `cutoff_keys_armed` or BUILD-METHOD's budget: owner turns.
- Rewriting a CLOSED spec's text. Each repaired unit is answered in its ledger, except S5's edge, which
  lands before any code.
- The report's left-shift gates and checklist entries, beyond S18's arm. No clause of this build names
  them.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-31` — S16: `derive_scouted_seam_input`'s required keys
- **consumes-from** `TOOL-dIndexedDesign-32` — S19: the `fork` row's closed sets in the per-kind table
- **consumes-from** `TOOL-dIndexedDesign-34` — S6 to S8: the `diff` writer and its typed row
- **consumes-from** `TOOL-dIndexedDesign-35` — S14, S17, S25, S26: the coverage stage, its S5 arm and its renders
- **consumes-from** `TOOL-dIndexedDesign-36` — S27: its AC1 and AC2
- **consumes-from** `TOOL-dIndexedDesign-37` — S10: `check_meet_path`
- **consumes-from** `TOOL-dIndexedDesign-38` — S1 to S5, S9, S11 to S13, S15, S19 to S24, S26: its items, criteria and ledger
- **consumes-from** `TOOL-dIndexedDesign-44` — S14: the coverage stage's finder bookkeeping, beside which the yield row is counted

## 4. Design

### Evidence

- `tools/memory-tree/deviation_join.py:160` captures the build slug and `<n>`, and `:283-292` key the
  collision on (build, n), so the factory's number is per build. `:268-293` read TRACKED paths only, and
  nothing in it allocates a number.
- `tools/check-spec-tokens.py:1104-1121`, `check_path_shaped`, keeps a slash-free token only when
  tracked. `:564-583`, `extract_files_touched`, classifies Files touched tokens through it and
  `check_dir_shaped`. The file loads `design_lib.py` by path (`:425-428`).
- `tools/unattended/unattended.sh:13737-13745` refuses a `--dispatch` whose `consumes-from` producer of
  this build is not CLOSED or WONTDO.
- `tools/roles/README.md:283`, `tools/roles/kit.toml:14` and `:19` say "three harnesses", read 2026-10-28.
- `gen_build_index.py:3679` holds `PROBE_TIMEOUT_SECONDS = 30`, and `:310` imports `design_lib`.
  `backlog.py:129` holds `SLUG_RE`, and `gen_build_index.py:4141` tests the lowercase initial inline.
- `memory/guides/BUILD-METHOD.md:133` and `tools/memory-tree/README.md:699` name `SPEC_LENSES` as the
  catalogue's one source.

### Ledger notes

Where an item supersedes a criterion or a sentence of a CLOSED unit, that unit's acceptance ledger
carries, at this pass, a continuation line under the named criterion's answer, two spaces in. It holds
the label `TOOL-dIndexedDesign-46 S<n>` and, on that one physical line, a backticked token of the item.
A note is never its own `- AC` line.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_next_record_path` | Python function, `build_records.py` | `py.function`, answered OK by `lexicon.py --suggest` |
| `check_build_slug` | Python function, `backlog.py` | `py.function`, answered OK by `lexicon.py --suggest` |
| `Policy`, `Read at` | `overlap` record fields | none |

### Migration

No record is rewritten. `PROBE_TIMEOUT_SECONDS` moves module and keeps its value. Unit 35's S5 arm is
deleted.

### Rollout

The pass lands every item at order 19 except S5 and S12. S5 is the build run's M2 cross-read, before its
first code pass, and S12 is unit 38's pass. Unit 38's Edges block names S12, and its builder reads it
there. S1's reading runs last, before the close.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S2, S4, S9, S10, S19, S22
- `tools/memory-tree/build_records.py`: S3, S8
- `tools/memory-tree/gen_build_index.py`: S11, S22, S24
- `tools/memory-tree/backlog.py`, `tools/memory-tree/plan_streams.py`: S24
- `tools/check-spec-tokens.py`: S10
- `tools/workflows/tier2-review.template.js`, its render `tools/workflows/tier2-review.js` by
  `check-protocol-parity.test.sh --render`, and `tools/workflows/tier2-review.test.sh`: S14
- `tools/workflows/replay_scorer.py`: S16
- `tools/workflows/check-verifier-fanout.test.sh`: S18
- `tools/hooks/agent-cap.test.sh`: S17
- `tools/roles/README.md`, `tools/roles/kit.toml`: S13
- `tools/unattended/VERBS.template.md`, and `memory/guides/UNATTENDED-VERBS.md` its render: S20
- `tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md` its render, and
  `tools/memory-tree/README.md`: S25
- `memory/builds/dIndexedDesign/spec/`: S5's two edges, at the M2 cross-read
- `memory/builds/dIndexedDesign/build/`: the ledger notes and unit 7's instrument fixture (S9)
- `memory/builds/dIndexedDesign/reviews/`: S1's record

### Alternatives rejected

- **Two batches.** Lost to M6 clause 1: `design_lib.py` sits in every candidate split.
- **Fold each fix into its unit's spec.** Lost to the owner's 2026-10-05 ruling M4 records: none is
  folded.
- **Distinct orders for units 13 and 20 (S5).** Lost to the edge: an order change re-sequences the whole
  step, while the edge binds only the pair that needs it.

## 5. Production-readiness checklist

- security — S8 never overwrites a record; S24 validates a slug at two write boundaries.
- perf / scale — S1 is one review over the specs no reading pins.
- error / empty / loading states — S16 and S8 turn a silent miss into a named refusal.
- observability — S14 makes the yield table sum to the confirmed total.
- risks — S5 and S12 act before this unit's order. AC4 and AC10 read the history that shows they did.
- testing — AC1 to AC20 by probe, fixture or ledger grep; the arms §7 declares.
- migration — §4 Migration.
- user docs — none under `help/`; the guides are S20's and S25's.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --design-exit dIndexedDesign` runs after
  S1's record is committed, it prints no `· none` lens line.
  Red when: a roster unit has no reading at its header revision.
  cost: one coverage-only review, minutes of agent time. permission: the main loop's act, before the close.
- **AC2** — When `design_lib.py --overlaps --record tFix` runs twice over a scratch build that already
  tracks another unit's `-overlap-1.md`, it writes `-overlap-2.md` and then `-overlap-3.md`.
  `grep -nE "overlap-\\{|-overlap-%" design_lib.py` prints nothing.
  Red when: the writer derives its own number, or reuses one.
- **AC3** — When `build_records.py`'s reader reads a scratch `-overlap-1.md` with `Policy`, `Read at` and
  two pair rows, it reads `bound`. Without `Read at`, it refuses naming the field.
  Red when: the pair rows are refused, or a missing keyed field passes.
- **AC4** — When `read_consumes_from` from `tools/unattended/lib-unattended.sh` reads unit 20's spec at
  the commit before unit 13's pass, it prints `TOOL-dIndexedDesign-13`. When `git log --format=%s` lists
  the pass commits at the close, unit 13's precedes unit 20's.
  Red when: the edge is absent before step 9, or the order is reversed.
- **AC5** — When `design_lib.py --reentry tFix --base <rev> --write` runs over a scratch build tracking
  `2026-10-28-build-TOOL-tFix-1-diff-1.md`, for a feature whose first unit is `TOOL-tFix-2`, it writes
  `2026-10-28-build-TOOL-tFix-2-diff-2.md`, and both read `bound`.
  Red when: it writes `-diff-1.md`, the per-unit number.
- **AC6** — When an untracked `-diff-1.md` sits in the scratch build's `build/` folder and `--write`
  runs, it writes `-diff-2.md`, and `sha256sum` of the first file is unchanged.
  Red when: the untracked record is overwritten.
- **AC7** — When unit 7's instrument runs M1 over the S9 fixture, it prints `section.acceptance` for the
  Tier-1 heading. With `extract_section_ref` stubbed to return `section.SENTINEL`, it prints the sentinel.
  Red when: M1 maps the ordinal itself.
- **AC8** — When a `python -c` calls `check_meet_path` with the `git ls-files` set over `.memory-tree.conf`,
  `README.md`, `.gitattributes`, `design.forks`, `Makefile`, `tools/x/`, `tools/` and `NEWFILE.md`, it
  returns True, True, True, False, False, True, False and False, the verdicts of base
  `check_path_shaped or check_dir_shaped`. With no set it returns unit 37 S1's verdicts, `design.forks`
  and `NEWFILE.md` True. `grep -c "check_path_shaped(word, files) or"` over `check-spec-tokens.py` prints 0.
  Red when: the spec-token join's verdicts move, or a second rule classifies Files touched.
- **AC9** — When `--design-exit` runs under `with-spec-audit` over a fixture opted in only by a dated
  `SPEC_AUDIT_DEFAULT`, it prints a lens line. Over one whose README carries `spec-audit: yes`, it prints none.
  Red when: the default is ignored, or an undated key reads as declared.
- **AC10** — When `grep -n "TOOL-dIndexedDesign-46 S"` runs over the acceptance ledgers of units 20, 34,
  35, 36 and 38 at this pass, it prints the notes of S1, S3, S6, S7, S9, S12, S21, S23, S26 and S27, each
  under its criterion. A `tomllib` read of `loop.toml` still lists the four `[[stand-in]]` rows
  while ask TOOL-dIndexedDesign-23 is open in `BACKLOG.md`.
  Red when: a note is missing or is its own `- AC` line, or a stand-in row was deleted.
- **AC11** — When `python tools/roles/check_roles.py` runs, it exits 0. When `grep -c "three harnesses"`
  runs over `tools/roles/README.md` and `tools/roles/kit.toml`, it prints 0 for each.
  Red when: the catalogue region is stale, or a count survives.
- **AC12** — When a `node -e` stub run of `tier2-review.js` with `coverage: 'with'` confirms one coverage
  finding, its `lensYield` holds a `coverage` row crediting it, and the rows' confirmed counts sum to the
  run's total. Under `'only'` it holds one row.
  Red when: the coverage finding falls into no row.
- **AC13** — When unit 13's grader reads MUSTs naming a class, a module constant, a shell function and a
  JS `const`, each defined on a non-comment line, each exits 0. A MUST whose symbol holds `(` matches
  only its literal text.
  Red when: a valid definition shape is refused, or a symbol is spliced unescaped.
- **AC14** — When `python replay_scorer.py --blind` reads three planted cases with
  `"prompt": ""`, `"repo": null` and no `sha_before`, it exits 2 for each, naming the case id and the key.
  Red when: an empty or non-string value is dispatched.
- **AC15** — When `git diff <p>^ HEAD -- tools/hooks/agent-cap.test.sh` runs, `<p>` being unit 35's pass
  commit, it prints nothing. When `bash tools/workflows/check-verifier-fanout.sh` runs on S18's fixture,
  it exits 1 naming `SPEC_LENSES`.
  Red when: the redundant arm survives, or the six-entry fixture is admitted.
- **AC16** — When `grep -nE "\"(preference|goal)\"" design_lib.py` runs in the memory-tree kit, it prints
  no line of the fork join. When a scratch copy of the per-kind table gains a `Class` value, the join
  admits a record using it.
  Red when: the join keeps its own copy of the set.
- **AC17** — When `grep -n "blocked"` and `grep -n "design-exit"` run over
  `memory/guides/UNATTENDED-VERBS.md`, each names its refusal, and the render matches its template.
  Red when: either refusal is unlisted.
- **AC18** — When `grep -rn "PROBE_TIMEOUT_SECONDS = "` runs over `tools/memory-tree/`, it prints one line,
  in `design_lib.py`.
  Red when: a second literal exists, or `design_lib.py` imports `gen_build_index`.
- **AC19** — When `grep -c "check_build_slug("` runs over `gen_build_index.py`, `design_lib.py` and
  `plan_streams.py`, each counts its call. When `design_lib.py --overlaps --record ../x` runs, it exits 2
  writing nothing.
  Red when: a writer keeps an inline copy of the test.
- **AC20** — When `grep -c "COVERAGE_BRIEF"` runs over `memory/guides/BUILD-METHOD.md` and
  `tools/memory-tree/README.md`, each prints at least 1. When `wc -c memory/guides/BUILD-METHOD.md` runs,
  it prints at most 30720.
  Red when: a carrier omits the brief, or the budget breaks.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `verifier fan-out` · `review-join self-test` · `agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `review-protocol parity (kit vs dogfood)` · `policy fixtures` · `memory-hygiene self-test` · `build-index selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `roles catalogue` · `roles render selftest` · `roles adopter self-test` · `unattended kit gate` · `kit/dogfood doc parity` · `build-method size` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

New arm: tools/workflows/check-verifier-fanout.test.sh · covers AC15 · a fixture harness with a sixth `SPEC_LENSES` entry, staged by the fixture itself, which the hook must deny · none
New arm: tools/workflows/tier2-review.test.sh · covers AC12 · the `coverage` row of `lensYield` under `with` and `only`, staged by mapping `runningLensKeys` alone · none
New arm: tools/memory-tree/build_records.py · covers AC3 AC6 · the `typed-kinds` plant's overlap record with two pair rows, and an untracked record before a write, staged by a tracked-only allocator · none

## 8. Open questions

- **F1 — The opt-in's reader (id 22): consume the driver's pinned value, or apply its dated rule?**
  Options: (a) `--design-exit` takes the run's pinned `spec-audit:` fact; (b) `check_spec_audit_declared`
  applies the same three-source dated rule. (a) leaves a standalone `--design-exit`, run outside an
  unattended run, with no value to read. RESOLVED (agent, 2026-10-28, delegated): (b), rung 3, the most
  feature-rich survivor; AC9 holds it to the driver's verdicts. widens: none · relaxes: none
- **F2 — The stand-in rows (id 24): keep, gate on the ask, or reconcile?** Options: (a) keep the four
  rows until ask TOOL-dIndexedDesign-23's reader shape lands; (b) make their deletion a build-run
  precondition on that ask; (c) record why they differ from `item.design.exit`. (c) has no ground,
  since unit 38 S4 itself records the loop kit's reader as not in tree. (b) leaves unit 38 unable to close
  while the ask is open. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the one survivor,
  matching unit 1 §8 F5. widens: none · relaxes: none
- **F3 — BUILD-METHOD and the verbs guide are governance carriers (S20, S25).** Options: (a) edit them
  under the README's `may: PLAY-dClosedLoop-3` grant, the sentences naming the refusals and the coverage
  stage the build's own clauses add; (b) leave them stale. (b) fails AC17 and AC20. RESOLVED (agent,
  2026-10-28, delegated): (a), rung 3 with veto 2 lifted by the grant. grants: PLAY-dClosedLoop-3
  BUILD-METHOD M4's catalogue sentence and the verbs guide's two refusals. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, the minors batch of the round-1 spec audit of units 31 to 38: 16
  MEDIUM and 11 LOW findings by raw id, each its own scope item.

## 10. Reuse audit

Each item extends the seam its finding names. S2, S4 and S8 extend `build_records.py`'s name grammar and
collision. S10 extends unit 37's `check_meet_path` with `check_path_shaped`'s rule
(`tools/check-spec-tokens.py:1104`). S11 follows `check_authorization`'s dated rule. S19 reads the
per-kind table. S22 moves `PROBE_TIMEOUT_SECONDS` to a module both readers import. S24 lifts the slug
test beside `backlog.SLUG_RE`. S18 extends the `verifier fan-out` leg's own self-test. The probe
`python tools/codebase-map/reuse_lookup.py "allocate the next free record number from the working tree with exclusive create"`
ranked `tree`, `records`, `load_map_tree`, `extract_records` and `read_records`. Only `read_records`
(`tools/memory-tree/deviation_join.py:268`) reads typed records, and it checks collisions rather than
allocating, so S8's allocator is new beside it. No other item builds a seam that exists.

Recall terms used: `python tools/memory-recall/query.py "how were minor spec audit findings batched into one unit" --terms "minors batch MEDIUM LOW promoted one unit disjoint write sets ledger note spec audit round"`
