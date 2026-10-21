# TOOL-dTrueNorth-20 — the round-2 spec audit's 38 minors: declared keys, honest exits, bounded reads, one reader each, and the records that name them

**Status:** OPEN · rev-3 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 7

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-prompt-TOOL-dTrueNorth-20-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-20-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md`)
exited CONVERGED with 41 confirmed findings over units 8 to 16. Its 3 highs are units 17 to 19. This
unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW, each by its report
id and each its own scope item, where the report merged ids into one item too. The minors land on
units 8 to 16, so this unit repairs none in particular and builds after every unit (order 7). An item
whose defect would bite an earlier pass reaches that pass through the hands-off bullet the unit's own
§3 carries to this one; the rest are amended and observed at this pass.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 11, 26 | S1, S2 |
| M2 | MEDIUM | 4, 30 | S3, S4 |
| M3 | MEDIUM | 2, 42 | S5, S6 |
| M4 | MEDIUM | 5 | S7 |
| M5 | MEDIUM | 12 | S8 |
| M6 | MEDIUM | 13 | S9 |
| M7 | MEDIUM | 24 | S10 |
| M8 | MEDIUM | 25 | S11 |
| M9 | MEDIUM | 27 | S12 |
| M10 | MEDIUM | 28 | S13 |
| M11 | MEDIUM | 29 | S14 |
| M12 | MEDIUM | 33 | S15 |
| M13 | MEDIUM | 36 | S16 |
| M14 | MEDIUM | 37 | S17 |
| M15 | MEDIUM | 39 | S18 |
| M16 | MEDIUM | 40 | S19 |
| M17 | MEDIUM | 41 | S20 |
| M18 | MEDIUM | 43 | S21 |
| L1 | LOW | 7, 16 | S22, S23 |
| L2 | LOW | 23, 32 | S24, S25 |
| L3 | LOW | 3 | S26 |
| L4 | LOW | 6 | S27 |
| L5 | LOW | 9 | S28 |
| L6 | LOW | 10 | S29 |
| L7 | LOW | 14 | S30 |
| L8 | LOW | 15 | S31 |
| L9 | LOW | 18 | S32 |
| L10 | LOW | 19 | S33 |
| L11 | LOW | 20 | S34 |
| L12 | LOW | 31 | S35 |
| L13 | LOW | 35 | S36 |
| L14 | LOW | 45 | S37 |
| L15 | LOW | 46 | S38 |

That is 21 MEDIUM and 17 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 11. `tools/memory-tree/kit.toml`'s `conditional_keys` gains `DESIGN_RECORD`,
  `DESIGN_BASELINE`, `DESIGN_VIEW` and `DESIGN_NODES`, gov-only keys where blank or absent is off.
  Govkit check 7 is the list's one reader (`tools/govkit/govkit.py:2487-2505`) and it adds nothing to
  the example conf, so `TOOL-dTrueNorth-16` S37's "absent from the example conf" stands. Observed by AC1.
- **S2** — id 26. The red that S1 cures is observed before it: `TOOL-dTrueNorth-12` S5's row alone
  fails check 7's predicate once per key. Observed by AC1.
- **S3** — id 4. `--check-coverage`'s off line is spelled `build-index: coverage off — SPEC_CARRIES_CUTOFF
  is blank`, the line `TOOL-dTrueNorth-3` S5 prints and `TOOL-dTrueNorth-15` S1 keeps, so
  `TOOL-dTrueNorth-16` S29's `(?m)^build-index: coverage` matches it in an adopter. Observed by AC2.
- **S4** — id 30. `--check-asbuilt` prints `build-index: as-built clean · <n> deviation records` when
  armed and clean, and `build-index: as-built <k> finding(s)` above its `as-built VERDICT` block, so
  S29's expect matches every state; the three clauses are run in an adopter tree and in gov.
  Observed by AC3.
- **S5** — id 2. `TOOL-dTrueNorth-16` S2's refusal guards later builds only: every consumes-from edge
  inside this build dispatches at orders 1 to 4, before it lands. Its "the orders this build's units
  carry stand; the refusal is what makes …" and its §3 reason not to renumber are superseded: this
  build's same-order consumers rely on BUILD-METHOD M6's condition (2), each dispatched only after
  its producer is CLOSED, and step 3 builds `TOOL-dTrueNorth-4` before `TOOL-dTrueNorth-6`.
  Observed by AC4.
- **S6** — id 42. `--dispatch` in `tools/unattended/unattended.sh` refuses with code 49 a consumes-from
  cycle among the build's units, a self-edge included, naming the cycle, found by
  `scan_consumes_cycles` beside `read_consumes_from` in `tools/unattended/lib-unattended.sh`; and a
  spec whose `### Edges` block holds a `**consumes-from**` line from which `read_consumes_from` reads
  no id, naming the spec. Settled at rung 5 (§8 F4), so this pass writes deviation-6 from §4.
  Observed by AC5 and AC35.
- **S7** — id 5. `derive_audit_writers(root, rels, resolve=None)` takes an injected resolver, the
  shape `read_landed_unclosed` takes (`tools/memory-tree/gen_build_index.py:1678`); the generator's
  self-test passes one returning its fixture harness, and a live read whose workflows kit does not
  resolve prints one `build-index: SKIP audit-writer test` line naming why beside the `-` field
  `TOOL-dTrueNorth-14` S2 gives. Observed by AC6.
- **S8** — id 12. The harness path becomes repo-relative POSIX before the `<sha>:<path>` request, so
  a Windows resolver's absolute backslash path cannot read as `missing`. The missing-blob half of the
  finding is `TOOL-dTrueNorth-19` S3's. Observed by AC7.
- **S9** — id 13. `read_bindings` folds a record's `ids` to first-seen order after `_expand_ids`,
  which keeps its base return. **Readers:** by name: `read_bindings`. by value: the `S` and `B` rows
  of `cmd_print_bindings` (`gen_build_index.py:728-733`) and the record tables built from
  `binds_all` (`:2353-2366`), each now seeing an id once. `TOOL-dTrueNorth-9` AC3's three ids then
  hold as written. Observed by AC8.
- **S10** — id 24. No waiver row: the hit `routed-commits selftest <- tools/unattended/lib-unattended.sh`
  against `TOOL-dTrueNorth-7` stands only while that spec is live, orders 4 to 6, when no bar runs
  (BUILD-METHOD M6), and unit 7's CLOSED flip ends it; a row would read stale at the close. This
  pass observes the end state. Observed by AC9.
- **S11** — id 25. The hits `TOOL-dTrueNorth-11`'s guard makes on dPinnedHandoff's live specs, derived
  tree-wide before the cure: `build-index selftest <- tools/check-spec-tokens.py` on its `-2` and `-3`,
  and `memory-hygiene self-test <- tools/check-spec-tokens.py` on its `-2`. Their cure is §8 F3,
  open. Observed by AC10.
- **S12** — id 27. An ask row and its `SEV` row in `memory/builds/dClosedLoop/BACKLOG.md` (§4 "The
  ask") asks the owner to re-render the chain packets with `packet.py --write`, pins kept, once this
  build lands, since every view re-render and every ask naming a chain build moves their bytes.
  Observed by AC11.
- **S13** — id 28. `TOOL-dTrueNorth-16` closes at order 5 and the size join measures live specs only
  (`tools/check-spec-tokens.py:916-925`), so no high-water row is owed at this pass; were it live
  here, this pass records its row by the class row's `--bump` route
  (`tools/template-size-limits.txt:162-166`). Observed by AC12.
- **S14** — id 29. A `requires_if` row in `tools/memory-tree/kit.toml` names `workflows` when
  `SPEC_AUDIT_PIN_CUTOFF`, which `TOOL-dTrueNorth-5` lists in `optional_keys`, is set; and the
  literal is pinned from the producer: `AUDIT_WRITER_MARK` in `gen_build_index.py` is the reader's
  one spelling, and an arm in the workflows kit's tier2-review suite reads that constant and asserts
  the harness defines a function of that name. Observed by AC13.
- **S15** — id 33. `.gitattributes` gains the view's path with `merge=ours` beside `memory/LIVE.md`
  (`:84`), its comment naming push-main's `regen.py --write` as the re-render through the generator's
  existing `[[generated]]` row. No `kit.toml` row. Observed by AC14.
- **S16** — id 36. `read_gen_region_awk` treats a resolved kit whose `lib-unattended.sh` holds no
  single-line `GEN_REGION_AWK='…'`, an empty value, or no `awk` on `PATH` as the unresolved kit of
  `TOOL-dTrueNorth-12` S2: `LookupError` naming the file and the variable, exit 2 live, the named
  SKIP under `--fixture`. Observed by AC15.
- **S17** — id 37. `read_reviewed_paths` reads `Reviewed: ` from every unfenced line before the
  record's first `## ` heading, not the first twelve, superseding `TOOL-dTrueNorth-13` S4's window.
  Observed by AC16.
- **S18** — id 39. `read_spec_revisions` makes one log over
  `':(glob)<MEMORY_ROOT>/builds/*/spec/**/*-spec-*.md'` and filters it to `paths` in Python; a failed
  spawn is a named refusal, exit 2. Observed by AC17.
- **S19** — id 40. `read_conf_key` in `tools/check-spec-tokens.py` parses each line through
  `tree_lib.parse_conf_line` (`tools/memory-tree/tree_lib.py:63`), last declaration wins and `export`
  stripped, loaded by path from the kit as `TOOL-dTrueNorth-16` S11 loads the generator. Observed by AC18.
- **S20** — id 41. `--check-asbuilt --staged` runs when any staged path satisfies `check_index_input`
  (`gen_build_index.py:831-857`), plus `DESIGN_RECORD` and `DESIGN_VIEW` where they fall outside it,
  the trigger `TOOL-dTrueNorth-16` S21 gives check 29; this supersedes S17's hand list. Observed by AC19.
- **S21** — id 43. An ask id this build files is `PLAY-dClosedLoop-<n>` above every id the tree spells
  at its commit, and a prepared merge that `merge-rows.py`'s `no_new_duplicates` refuses on it is
  reconciled by renumbering this run's row, its `SEV` row and their renders, never the landed one.
  Observed by AC20.
- **S22** — id 7. `TOOL-dTrueNorth-16` AC31 is observed by identity, in-process, and by an `ast` scan
  of `asbuilt_view.py` for a regex call on a string-literal pattern. Observed by AC21.
- **S23** — id 16. `TOOL-dTrueNorth-16` AC32 is observed by grepping the compiled pattern itself.
  Observed by AC22.
- **S24** — id 23. The comment above `GENERATED_INDEXES` in `.unattended.conf` (`:402-404`) says the
  view's pairs are declared there because its path is gov's own dClosedLoop file, which a
  `[[generated]]` row cannot spell (`TOOL-dTrueNorth-6` §4 "Alternatives rejected"), in place of
  "Blank: this project adds no generator of its own". Observed by AC23.
- **S25** — id 32. The same comment, as `TOOL-dTrueNorth-16` S18's other half: its AC18 is observed
  with the old sentence gone. Observed by AC23.
- **S26** — id 3. `TOOL-dTrueNorth-16` AC17 is observed with `--write` run after the plant.
  Observed by AC24.
- **S27** — id 6. `TOOL-dTrueNorth-16` AC12 is observed over a floor: a chain spec with three
  revisions, one from a merged branch. Observed by AC25.
- **S28** — id 9. `TOOL-dTrueNorth-16` S35's pin-aware ask supersedes `TOOL-dTrueNorth-5` §3's "filed
  as an ask at this build's close" (`:78`), so the close files nothing for it. Observed by AC26.
- **S29** — id 10. `TOOL-dTrueNorth-12` S5's row names all four `DESIGN_*` keys, and
  `TOOL-dTrueNorth-16` S19's move is stated complete: `design_lib.write_design_fixture` is the one
  fixture builder its callers reach, and no module under `tools/` spells the builder's old name.
  Observed by AC27.
- **S30** — id 14. `TOOL-dTrueNorth-15` §4 Evidence's second bullet is superseded by
  `git grep -lF '**Status:** INPROGRESS' -- 'memory/builds/*/spec/*.md'`, which prints at base.
  Observed by AC28.
- **S31** — id 15. `TOOL-dTrueNorth-12` AC5 is observed by a TOML read of the one row. Observed by AC27.
- **S32** — id 18. `read_adding_commits(root, pathspec, wanted)` in `tools/memory-tree/tree_lib.py`,
  the oldest add under `--reverse --no-renames --diff-filter=A` over one glob pathspec, is the one
  adding-commit reader: `derive_audit_writers` (`TOOL-dTrueNorth-19` S1) and the deviation join's
  ported `read_adding_commit` both call it. Observed by AC29.
- **S33** — id 19. `read_blobs_at(root, requests)` in `tree_lib.py` maps `(rev, path)` pairs to text or
  None in one bytes-mode `cat-file --batch`, UTF-8 with CRLF folded; `read_blobs_at_rev`,
  `read_spec_revisions` and `derive_audit_writers` call it. Observed by AC30.
- **S34** — id 20. `TOOL-dTrueNorth-11` AC2 is observed through `check-spec-tokens.py --legs-for`.
  Observed by AC31.
- **S35** — id 31. An ask commit runs `gen_build_index.py --write` and stages what it moves:
  dClosedLoop's README `ids:`, `memory/backlog/PLAY.md` and `memory/LIVE.md`; units 15 and 16 did so
  under check 9, and this pass's own ask commit does so by this item. Observed by AC32.
- **S36** — id 35. Where a repeated id folds is S9's `read_bindings`, never `_expand_ids`, and
  `TOOL-dTrueNorth-9` S4's arm gains the duplicate case. Observed by AC8.
- **S37** — id 45. The "Deviation records" paragraph of `tools/memory-tree/HYGIENE.template.md`
  gains the decline route for an approval carried for the owner's walk: a decline is filed as an
  ask naming the record, and its follow-up is a new record naming the declined one in
  `**Supersedes:**` (`TOOL-dTrueNorth-18` S1), the view re-rendered in that commit; `memory/HYGIENE.md`
  is re-rendered. Observed by AC33.
- **S38** — id 46. The rule's trigger, in the homes `TOOL-dTrueNorth-8` S1 and `TOOL-dTrueNorth-17` S1
  write, reads "a commit that changes any view input: a record matching the glob added, edited, moved
  or taken out, a `DESIGN_*` key changed, or the render's code changed"; unit 8 S3's arm gains the
  case of a record taken out. Observed by AC34.

## 3. Non-goals (OUT)

- The three highs, units 17 to 19. Where a minor shares a defect with one, ids 12 and 46, the high's
  unit owns the mechanism it names and this item owns only what §2 states.
- Editing the frozen specs of units 1 to 16. A criterion restated here is superseded here and
  observed at this pass.
- Editing dPinnedHandoff's specs, which README rule 7 keeps outside this build's writes.
- Renumbering any unit, and a cycle refusal for ask holds, which `backlog._scan_cycles` already makes.
- The left-shift gates the report suggests per item; each is a separate gate and so a separate unit
  by M2, and the close left-shifts the confirmed classes.

### Edges

- **consumes-from** `TOOL-dTrueNorth-7` — its CLOSED status at order 6, which ends S10's hit
- **consumes-from** `TOOL-dTrueNorth-8` — S1's rule and S3's arm, which S38 rewords and extends
- **consumes-from** `TOOL-dTrueNorth-9` — `read_bindings`' `ids` and S4's arm, which S9 and S36 fold and extend
- **consumes-from** `TOOL-dTrueNorth-10` — deviation-3's approval, whose decline route S37 states
- **consumes-from** `TOOL-dTrueNorth-11` — the checker guard behind S11's hits, and AC2, which S34 re-observes
- **consumes-from** `TOOL-dTrueNorth-12` — `read_gen_region_awk` and the `requires_if` row, which S1, S16, S29 and S31 harden
- **consumes-from** `TOOL-dTrueNorth-13` — `read_reviewed_paths`, whose window S17 widens
- **consumes-from** `TOOL-dTrueNorth-14` — `derive_audit_writers`, which S7, S8, S14, S32 and S33 extend
- **consumes-from** `TOOL-dTrueNorth-15` — the coverage off line and its ask, which S3, S21, S30 and S35 spell and file
- **consumes-from** `TOOL-dTrueNorth-16` — the revision reader, the conf read, `--check-asbuilt`, its contract clauses, its asks and its refusal, which S3 to S6, S13, S18 to S20, S22 to S28 and S35 amend or observe
- **consumes-from** `TOOL-dTrueNorth-17` — the extended rule S38 rewords
- **consumes-from** `TOOL-dTrueNorth-18` — the `**Supersedes:**` field S37's decline route names
- **consumes-from** `TOOL-dTrueNorth-19` — the bounded reader S8, S32 and S33 extend

## 4. Design

### Why one unit and not two

The tree-library items (S32, S33) feed the generator's and the design library's readers (S7, S8,
S18), the checker items (S19, S22, S23) read `design_lib.py` and `tree_lib.py`, and the kit
descriptor items (S1, S14, S29, S31) are the contract govkit grades for the generator's own rows. Any
split puts a file one half writes among the other half's contracts, which M6's clause 2 refuses.

### Deviation-6

`memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-20-deviation-6.md`, written in this
pass's commit with the view re-rendered:

```markdown
# TOOL-dTrueNorth-20 deviation 6 — the dispatch refuses a consumes-from cycle and an unreadable edge, a carrier change no clause names

**Serves:** deviation TOOL-dTrueNorth-20

- **Departs from:** `dTrueNorth` [grant]
- **Hand-off:** design-to-spec
- **Before:** the chain's grant PLAY-dClosedLoop-3 lifts veto 2 only for the governance-carrier changes dTrueNorth's own `[chain]` clauses name, and none of `cl-dClosedLoop-0001` to `cl-dClosedLoop-0006` names the dispatch verb of `tools/unattended/unattended.sh`
- **After:** TOOL-dTrueNorth-20 adds two code-49 refusals to `--dispatch`: a consumes-from cycle among a build's units, a self-edge included, and a spec whose Edges block holds a consumes-from line from which no unit id is read, taken under the owner's standing ruling for a fork whose only options trip veto 2 outside the grant
- **Cause:** review finding
- **Reason:** The round-2 spec audit's id 42 found that a malformed Edges block reads as fewer edges, which blocks nothing, and that a cycle wedges the run at --dispatch with no named stop. Every mechanism that refuses either at the act is a governance-carrier change no dTrueNorth clause names, so the fork was settled at rung 5 by the most capable option.
- **Evidence:** `memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md`, item M3 (id 42); the standing ruling ER:388 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`); the decision row `PLAY-dClosedLoop-6`; TOOL-dTrueNorth-20 §8 F4
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, citing `PLAY-dClosedLoop-6` (ER:388), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-20
- **Caused-by:** 2026-10-21-review-TOOL-dTrueNorth-8-spec-audit
- **Surface:** the `--dispatch` verb of `tools/unattended/unattended.sh`, two code-49 refusals: a consumes-from cycle, and an Edges block whose consumes-from line yields no id
```

### The ask (S12)

Its id follows S21; its date is the pass's. The row goes under `## Asks`, the `SEV` row under
`## Dispositions`.

```markdown
- PLAY-dClosedLoop-<n> · filed <date> · THE CHAIN PACKETS GO STALE WHEN dTrueNorth LANDS. Each chain build's packet pins the as-built view's HEAD blob and lists the open dClosedLoop asks naming a chain build, and dTrueNorth re-renders the view and files such asks, so packet.py --check fails its byte compare for every other chain build, dGroundRules included. · accept every chain packet re-rendered with packet.py --write, its instrument pins kept, and packet.py --check green for each chain build
- SEV · PLAY-dClosedLoop-<n> · MEDIUM · a chain build cannot start its first pass until its packet is re-rendered
```

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `scan_consumes_cycles` | function, `lib-unattended.sh` | `sh.function`, OK |
| `read_adding_commits` | function, `tree_lib.py` | `py.function`, OK |
| `read_blobs_at` | function, `tree_lib.py` | `py.function`, OK |
| `AUDIT_WRITER_MARK` | constant, `gen_build_index.py` | none |

### Files touched (estimate)

- `tools/memory-tree/kit.toml`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `tools/memory-tree/README.md`
- `tools/check-spec-tokens.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/workflows/tier2-review.test.sh`
- `.gitattributes`
- `.unattended.conf`
- `memory/builds/dClosedLoop/BACKLOG.md`
- `memory/builds/dClosedLoop/README.md`, `memory/backlog/PLAY.md`, `memory/LIVE.md` (re-rendered by `--write`, never edited)
- `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-20-deviation-6.md` (new)
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (re-rendered by `--write`, never edited)
- `memory/project/spec-token-waivers.txt` (only if §8 F3 resolves to a waiver)

### Alternatives rejected

- **A waiver row for S10's hit.** Unit 7 closes before this pass, so the row would read stale.
- **Moving the `Reviewed:` line in both writers (S17).** It fixes future records only, edits six
  workflow files, and leaves the three tracked records whose line sits at 15 or 16 graded.
- **Restating `TOOL-dTrueNorth-9` AC3 to expect the duplicate (S9).** A repeated id would then render
  twice in every records table and double-count in the ids joins.

## 5. Production-readiness checklist

- security — S6 adds refusals and no write; S16 and S18 refuse rather than read nothing; S8 keeps a
  missing harness graded. No new input crosses a trust boundary.
- perf / scale — S18 and S32 make each history read one spawn whatever the population; S33 one
  batch read per caller.
- error / empty / loading states — every unresolved or failed read is a named refusal or a named SKIP
  (S7, S16, S18); none reads as green over nothing.
- observability — the refusals name the cycle, the spec, the file and the variable; the SKIP lines
  name what they held back.
- risks — S6 refuses a dispatch the order gate admits; S15 takes this side of the view in a merge and
  relies on push-main's re-render; S21's renumbering touches only this run's own rows.
- testing — AC1 to AC35 as probes of the units' code, fixtures and records; the arms under §7.
- migration — additive: S9 changes `ids` only for a record that repeats one.
- user docs — `memory/HYGIENE.md`, the kit README; no page under `help/` covers these engines.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch clone or fixture repository is under a short
`%TEMP%` path, with no hook installed.

- **AC1** — When a probe loads `tools/memory-tree/kit.toml` with `tomllib` and checks every
  `requires_if` row's `when_any_key_set` against the four config lists, as check 7 does, no key is
  undeclared; with S1's keys taken out, each `DESIGN_*` key is named.
  Red when: a condition key of the unattended row appears in no config list.
- **AC2** — When `python3 tools/memory-tree/gen_build_index.py --check-coverage` runs in a scratch
  adopter tree whose conf lacks `SPEC_CARRIES_CUTOFF`, its stdout matches `(?m)^build-index: coverage`.
  Red when: the off line opens with any other words.
- **AC3** — When a probe runs the three `memory-tree/gen-build-index` contract clauses' commands of
  `tools/memory-tree/kit.toml` in that adopter tree and in gov, each stdout matches its `expect`.
  Red when: one state of `--check-asbuilt` prints a line no alternative matches.
- **AC4** — When a probe reads each `dispatch` row of `memory/builds/dTrueNorth/RUN.md` against
  `git log --format='%H %s'`, every unit consuming from a same-build unit is dispatched after the
  commit setting its producer's header `CLOSED`, and `TOOL-dTrueNorth-4` before `TOOL-dTrueNorth-6`.
  Red when: a consumer's row precedes its producer's close.
- **AC5** — When a scratch preflight fixture holds a build whose two units consume from each other,
  `unattended.sh --dispatch` exits 49 naming the cycle; with one spec's edge bullet written so
  `read_consumes_from` reads no id, it exits 49 naming that spec; well formed and acyclic, it proceeds.
  Red when: either shape dispatches.
  cost: minutes, for a preflight fixture built as `TOOL-dTrueNorth-16` AC2's is.
- **AC6** — When a probe calls `derive_audit_writers` with a stub resolver returning a fixture harness
  that lacks `renderAuditBinding`, the record is exempt; with a stub raising `LookupError`, it exempts
  nothing and `--print-bindings` prints the `build-index: SKIP audit-writer test` line.
  Red when: the function reads the machine's workflows kit whatever the caller injects.
- **AC7** — When the stub returns an absolute path with backslashes, the record is still exempt.
  Red when: the request spells the path as given and `cat-file` answers `missing`.
- **AC8** — When a probe runs `read_bindings` over a record reading
  `**Serves:** spec-audit TOOL-tPin-1@rev-2 TOOL-tPin-1@rev-3 TOOL-tPin-2..3`, its `ids` are
  `["TOOL-tPin-1", "TOOL-tPin-2", "TOOL-tPin-3"]` and `_expand_ids` on the same text returns four.
  Red when: the fold moves into `_expand_ids`, or `ids` keeps the duplicate.
- **AC9** — When `python3 tools/check-spec-tokens.py --list` runs after this pass, no line pairs
  `routed-commits selftest <- tools/unattended/lib-unattended.sh` with `TOOL-dTrueNorth-7`.
  Red when: unit 7 is still live, so its Files touched is graded.
- **AC10** — When `python3 tools/check-spec-tokens.py --list` runs in a scratch clone holding
  `TOOL-dTrueNorth-11`'s manifest, it lists the three S11 hits on dPinnedHandoff's specs, and after
  §8 F3's cure none stands unwaived and unanswered.
  Red when: a hit the guard makes is found only by the bar.
- **AC11** — When `grep -n 'THE CHAIN PACKETS GO STALE' memory/builds/dClosedLoop/BACKLOG.md` runs, it
  prints the ask row, and its id has a `SEV` row.
  Red when: the packets' staleness is recorded nowhere.
- **AC12** — When `python3 tools/check-spec-tokens.py --list` runs after this pass, no `size <-` line
  names `TOOL-dTrueNorth-16`.
  Red when: unit 16 is live and over 49152 bytes with no row holding it.
- **AC13** — When a probe reads `kit.toml`'s `requires_if` with `tomllib`, one row names `workflows`
  under `SPEC_AUDIT_PIN_CUTOFF`; and the tier2-review suite's new arm, run over a scratch copy of the
  harness with the function renamed, fails naming `AUDIT_WRITER_MARK`.
  Red when: a rename of the producer's function passes its own suite.
- **AC14** — When a scratch repository with `merge.ours.driver` set merges two branches that each add
  a record and re-render the view, the merge does not conflict, and the run-gates kit's
  `regen.py --write` then writes a view whose head counts both records.
  Red when: the view's head line conflicts and the merge stops.
- **AC15** — When a probe points `read_gen_region_awk` at a scratch kit whose `lib-unattended.sh`
  lacks the line, it raises `LookupError` naming the file and `GEN_REGION_AWK`; with an empty value,
  the same.
  Red when: an empty strip is returned, so every revision reads as status-only.
- **AC16** — When a probe grades a scratch `spec-audit` record whose ten-line provenance paragraph
  precedes its `Reviewed:` line, the design-document id prints no `P` row.
  Red when: the line is read only within the first twelve unfenced lines.
- **AC17** — When a probe calls `read_spec_revisions` over a fixture repository holding 601 spec
  paths of at least 98 bytes, it returns without `OSError`; with `git` a stub exiting 128 it raises
  the named refusal.
  Red when: the paths go on argv or a failed spawn reads as no revisions.
- **AC18** — When a scratch conf declares `SPEC_GUARD_LEGS_CUTOFF` twice, and separately as
  `export SPEC_GUARD_LEGS_CUTOFF=…`, `read_conf_key` returns the last value in each case.
  Red when: the first declaration wins, or `export` reads as absent.
- **AC19** — When a scratch clone stages only an `asbuilt_view.py` edit,
  `python3 tools/memory-tree/gen_build_index.py --check-asbuilt --staged` runs its verdict rather than
  printing the held line.
  Red when: a staged edit of the verdict's own code is held.
- **AC20** — When two branches of a scratch repository each file `PLAY-dFix-20` in one `BACKLOG.md`,
  the second merge is refused by `merge-rows.py`; with that side's row renumbered by S21, the merge
  succeeds and the ids are distinct.
  Red when: the reconcile edits the landed row.
- **AC21** — When a probe imports the modules, `asbuilt_view.VIEW_ROW is design_lib.VIEW_ROW` and the
  checker's `SPEC_DATE is design_lib.SPEC_FILE_DATE`, and an `ast` walk of `asbuilt_view.py` finds no
  `re.compile`, `re.match`, `re.search` or `re.fullmatch` call on a string literal.
  Red when: a second row grammar or date pattern compiles.
- **AC22** — When `git grep -n -F '[0-9]{2})-spec-' -- tools/check-spec-tokens.py "tools/memory-tree/design_lib.py"`
  runs, it prints one line, in `design_lib.py`.
  Red when: the pattern is spelled in both files.
- **AC23** — When `grep -c 'Blank: this project adds no generator of its own' .unattended.conf` runs it
  prints 0, and `grep -n -B4 '^GENERATED_INDEXES=' .unattended.conf` names the dClosedLoop path reason.
  Red when: the comment contradicts the value below it.
- **AC24** — When a scratch clone plants a record departing through `gap gap-mem-47` and runs
  `python3 tools/memory-tree/gen_build_index.py --write`, then `--check` exits 0 with no
  `as-built VERDICT` line and `--check-asbuilt` exits 1 naming the record.
  Red when: `--check` reports drift because the plant was never re-rendered.
- **AC25** — When the probe of `TOOL-dTrueNorth-16` AC12 runs over a fixture whose chain spec has three
  revisions, one merged from a branch, both arms' lists have length 3 and agree.
  Red when: a fixture with no chain spec passes on two empty lists.
- **AC26** — When `grep -c 'NOT PIN-AWARE' memory/builds/dClosedLoop/BACKLOG.md` runs after the close,
  it prints 1.
  Red when: the close files unit 5's follow-up a second time.
- **AC27** — When a probe reads `kit.toml` with `tomllib` and keeps the `requires_if` rows whose `kit`
  is `unattended`, exactly one returns, naming all four `DESIGN_*` keys; and
  `git grep -n build_design_fixture -- tools/` prints nothing.
  Red when: the row lacks `DESIGN_NODES`, or a caller still spells the old builder.
- **AC28** — When `git grep -lF '**Status:** INPROGRESS' -- 'memory/builds/*/spec/*.md'` runs, it prints
  at least one path.
  Red when: the pathspec matches no file, so the evidence reads as an absence.
  figure: the count is DERIVED at observation.
- **AC29** — When a fixture record is deleted and re-added on a branch, `derive_audit_writers` and the
  deviation join's pin-anchor read report the same adding commit, the oldest.
  Red when: either caller runs its own `git log`.
- **AC30** — When an `ast` walk of `read_blobs_at_rev`, `read_spec_revisions` and
  `derive_audit_writers` runs, none spells `cat-file`; each calls `tree_lib.read_blobs_at`.
  Red when: a function keeps its own batch parser.
- **AC31** — When `python3 tools/check-spec-tokens.py --legs-for tools/check-spec-tokens.py` runs, it
  lists `build-index selftest` and `memory-hygiene self-test`, and in a scratch clone holding the
  manifest at `271aa59d` it lists neither.
  Red when: the probe re-implements the trip rule.
- **AC32** — When `python3 tools/memory-tree/gen_build_index.py --check` runs after this pass's ask
  commit, it exits 0.
  Red when: the ask commit staged `BACKLOG.md` alone.
- **AC33** — When `git grep -n 'decline' -- tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md`
  runs, both name the ask and the superseding record.
  Red when: a declined approval has no route.
- **AC34** — When `git grep -n 'moved or taken out' -- tools/memory-tree/README.md "tools/memory-tree/asbuilt_view.py"`
  prints both homes, and a scratch clone staging `git rm` of a record makes
  `python3 tools/memory-tree/gen_build_index.py --check --staged` exit 1 until `--write`.
  Red when: the rule names only adds and edits.
- **AC35** — When `python3 "tools/memory-tree/deviation_join.py" --approval by-risk` runs after this pass,
  no `refused:` or malformed line names `2026-10-21-build-TOOL-dTrueNorth-20-deviation-6`.
  Red when: S6's widening is recorded nowhere, or its record falls outside the grammar.

## 7. Gates

`memory hygiene` · `build-index selftest` · `memory-hygiene self-test` · `routed-commits selftest` · `spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `govkit selfcheck` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC6 AC7 AC8 AC16 AC19 AC24 AC29 AC30 AC34 · a stubbed resolver, a backslash harness path, a doubled id, a late Reviewed line, a staged verdict edit, a planted gap record, a re-added record and a deleted one · none
New arm: tools/memory-tree/routed_commits.py (its selftest) · covers AC15 AC17 · a kit without the awk line and 601 spec paths · none
New arm: tools/check-spec-tokens.test.sh · covers AC18 AC21 AC22 · a doubled and an exported cutoff, and a second date pattern · none
New arm: tools/workflows/tier2-review.test.sh · covers AC13 · the harness function renamed against AUDIT_WRITER_MARK · that suite's assertion floor, raised by the arm
New arm: tools/unattended/unattended.test.sh · covers AC5 · a consumes-from cycle and an unreadable edge bullet · none

README rule 8 waives the unattended suites' verdict at this landing, so AC5's red-then-green reading
at the close is its targeted probe, as `TOOL-dTrueNorth-16` §7 states for its own.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry. (b) reds `unbound` and (c) reds `parts`; veto 1 discards both.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none ·
  relaxes: none
- **F2 — One batch unit or two?** §4 "Why one unit and not two" shows every split shares a contract.
  Recommendation one. Rung 3. RESOLVED (agent, 2026-10-21, delegated): one. widens: none ·
  relaxes: none
- **F3 — How do S11's three hits on dPinnedHandoff's live specs clear before the close?** (a) Three
  rows in `memory/project/spec-token-waivers.txt`, each naming the spec and why, beside an ask row
  asking dPinnedHandoff to name both legs on its §7 lines; the file declares itself SHRINK-ONLY, so
  its count would rise from 23 to 26, a declared ceiling M3 gives the owner. (b) Raise
  `SPEC_GUARD_LEGS_CUTOFF` past 2026-09-22, a root conf outside the grant (veto 2), grandfathering
  every spec of that date. (c) Leave the hits to dPinnedHandoff's own run, so this build's close meets
  a red `spec tokens` leg, failing README rule 1's whole-run landing (veto 1). Recommendation (a),
  the narrowest; whether ER:388's standing ruling reaches a declared ceiling is not derivable from
  the records, so the resolver is the main loop under the chain's rungs, or the owner. Rung 5 (veto 2 only, outside the grant): RESOLVED (agent, 2026-10-21, delegated): (a), citing
  ER:388 (`PLAY-dClosedLoop-6`), applied by the main loop before TOOL-dTrueNorth-15's dispatch, which the
  hits refused: two token rows (the three hits share two tokens), count 23 to 25, and ask `TOOL-dTrueNorth-21`
  in this build's `BACKLOG.md`, naming dPinnedHandoff. widens: memory/project/spec-token-waivers.txt rises 23 to 25 · relaxes: none
- **F4 — Which mechanism closes id 42?** (a) Two code-49 refusals at `--dispatch`. (b) A hygiene
  arm reporting a cycle at the bar. (c) The statement alone. (c) leaves the wedge, failing the
  finding (veto 1); (a) and (b) each change a governance carrier no dTrueNorth clause names, so veto 2
  holds outside the grant. Rung 5 takes the most capable: (a) refuses at the act and reuses
  `read_consumes_from`. RESOLVED (agent, 2026-10-21, delegated): (a), citing ER:388
  (`PLAY-dClosedLoop-6`), recorded as deviation-6. widens: the --dispatch verb of
  tools/unattended/unattended.sh gains code-49 refusals of a consumes-from cycle and an unreadable
  edge · relaxes: none
- **F5 — For ids 13 and 35, fold in `read_bindings` or restate AC3?** §4's rejected alternative says
  why restating loses. Recommendation fold. Rung 3. RESOLVED (agent, 2026-10-21, delegated): fold in
  `read_bindings`. widens: none · relaxes: none
- **F6 — For id 37, widen the reader or move the line?** §4's rejected alternative says why moving
  loses. Recommendation widen. Rung 3. RESOLVED (agent, 2026-10-21, delegated): widen.
  widens: none · relaxes: none
- **F7 — Does the build's grant lift veto 2 for every other carrier edit here?** Each is a change a
  dTrueNorth clause names: S16 to S19, S22, S23, S32 and S33 are `cl-dClosedLoop-0001`'s and
  `cl-dClosedLoop-0002`'s readers; S3 and S20 `cl-dClosedLoop-0003`'s; S37
  `cl-dClosedLoop-0004`'s record; S7, S8, S9, S14 and S17 `cl-dClosedLoop-0005`'s pin; S1, S4, S15,
  S24, S29 and S38 `cl-dClosedLoop-0006`'s view and gate. RESOLVED (agent, 2026-10-21, delegated):
  lifted by `PLAY-dClosedLoop-3`, rung 3, for all but S6, which F4 settles. grants:
  PLAY-dClosedLoop-3 the memory-tree kit, checker, tier2-review suite, .gitattributes and
  .unattended.conf edits S1 to S38 make for cl-dClosedLoop-0001 to cl-dClosedLoop-0006 ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, batching the round-2 spec audit's 21 MEDIUM and 17 LOW findings.
- rev-2 · 2026-10-21 · §6 · the acceptance criteria name the modules this build creates (`deviation_join.py`, `asbuilt_view.py`, `design_lib.py`) quoted or bare, and a `git show`/`json.load` argument quoted, so the spec-tokens paths join, which reads the live tree at every `--dispatch`, stops refusing every unit before those modules exist. No criterion's observation moves.
- rev-3 · 2026-10-21 · §8 · F3 resolved by rung 5 and applied before unit 15's dispatch: two waiver rows and ask `TOOL-dTrueNorth-21`.

## 10. Reuse audit

Every item extends a seam units 8 to 19 build, read in their specs and verified at base where it
exists: `read_landed_unclosed`'s injectable resolver (`tools/memory-tree/gen_build_index.py:1678`),
`check_index_input` (`:831-857`), `read_blobs_at_rev` (`:2934`), `tree_lib.parse_conf_line`
(`tools/memory-tree/tree_lib.py:63`), `migrate_backlog.scan_spec_adds` (`:408`),
`read_consumes_from` (`tools/unattended/lib-unattended.sh:327`), govkit check 7, and the
`merge=ours` lines of `.gitattributes`. `python tools/codebase-map/reuse_lookup.py "refuse a
dependency cycle among units at dispatch"` ranked `units`, `CensusRefused`, `ScopeRefused` and
`baseline_units` by name stem and missed `backlog._scan_cycles`, the ask-hold cycle scan found by
reading `tools/memory-tree/backlog.py:1262`; it is Python in the memory-tree kit, which the unattended kit installs without, so S6 walks
the edges in the shell library beside their reader, as `read_consumes_from` re-parses them.

Recall terms used: `python tools/memory-recall/query.py "how does a spec audit's promoted repair unit
close a defect a pass before it would hit" --terms "spec-audit promoted unit repairs order transition
re-render as-built view argv pathspec supersedes amends"`
