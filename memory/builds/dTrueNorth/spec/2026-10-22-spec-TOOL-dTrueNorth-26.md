# TOOL-dTrueNorth-26 — the closing diff review's minors: one scrubbed runner, one spec predicate, tracked records, one clause grammar, honest edges, and the comments that name them

**Status:** CLOSED · rev-2 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 10

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-26-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-26-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-26-deviation-25.md](../build/2026-10-22-build-TOOL-dTrueNorth-26-deviation-25.md) | deviation | — |
| [2026-10-22-build-TOOL-dTrueNorth-26-deviation-26.md](../build/2026-10-22-build-TOOL-dTrueNorth-26-deviation-26.md) | deviation | — |
| [2026-10-22-build-TOOL-dTrueNorth-26-deviation-27.md](../build/2026-10-22-build-TOOL-dTrueNorth-26-deviation-27.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-26-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-26-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-26-1-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-26-1-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-26-2-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-26-2-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-26-divergence-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-26-divergence-brief.md) | research | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-26-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-26-spec-brief.md) | research | — |
| [2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md) | diff-review | TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-27 TOOL-dTrueNorth-29 TOOL-dTrueNorth-30 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of dTrueNorth, round 1
(`memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`),
exited CLEAN WITH FIXES and CONVERGED with 22 confirmed findings. Its three highs are units 23 to 25.
This unit is the batch BUILD-METHOD M4 makes of the rest, every confirmed MEDIUM and LOW, one scope
item per raw finding id, where the review merged ids into one item too. It builds after the highs
(order 10), because three of them write the files several items amend. Every line cited below was
read at the review range's tip, `6f5f4ddec`.

| Review item | Severity | Finding ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 1 | S1 |
| M2 | MEDIUM | 5 | S2 |
| M3 | MEDIUM | 6, 19 | S3, S4 |
| M4 | MEDIUM | 7 | S5 |
| M5 | MEDIUM | 13 | S6 |
| M6 | MEDIUM | 14 | S7 |
| M7 | MEDIUM | 20 | none: handed to `TOOL-dTrueNorth-25`, which closes it with H3 |
| M8 | MEDIUM | 21 | S8 |
| M9 | MEDIUM | 23 | S9 |
| L1 | LOW | 8 | S10 |
| L2 | LOW | 9 | S11 |
| L3 | LOW | 10, 15, 24 | S12, S13, S14 |
| L4 | LOW | 16 | S15 |
| L5 | LOW | 17 | S16 |
| L6 | LOW | 18 | S17 |
| L7 | LOW | 22 | S18 |

That is 10 MEDIUM and 9 LOW findings by raw id, 18 of them scope items here. Findings 14, 18, 21 and
22 are built from the skeptic's corrected fix, which the review states in place of the finder's.

## 2. Scope (IN)

- **S1** — finding 1. `design_lib.run_git` (`tools/memory-tree/design_lib.py:147-151`) builds its env
  as `build_git_env()` less `tree_lib.GIT_ENV_LEAKS`, the expression `tree_lib.read_git_output` uses
  (`tools/memory-tree/tree_lib.py:270`), so `asbuilt_view.build_view_fixture`'s `git init`
  (`tools/memory-tree/asbuilt_view.py:327`), `read_retired_ids`, `read_owned_nodes` and
  `read_design_keys` read the repository they name; the review's `read_design_record` is no function
  of the module. `routed_commits.run_git` strips `tree_lib.GIT_ENV_LEAKS` too, and its own
  tuple, which lacks `GIT_NAMESPACE`, is retired.
  **Readers:** by name: `run_git`, the one reader spelling the tuple (`tools/memory-tree/routed_commits.py:81`,
  `:95`); no suite spells it.
  by value: NO VALUE READERS, since the tuple feeds one env strip and nothing counts or compares it.
  Observed by AC1 and AC2.
- **S2** — finding 5. The carries join's `parts` arm (`tools/check-spec-tokens.py:975-979`) collects
  the set of `n` its clause's part carriers state; more than one `n` is a `parts` finding naming every
  total, and one `n` keeps today's compare of the sorted `k` values with `range(1, n+1)`. Observed by
  AC3.
- **S3** — finding 6. The "tier2-review self-test" leg of `tools/gate-legs.json` (`:737-748`) adds
  `{prefix}/memory-tree/gen_build_index.py` to its `guard`, so a scoped run that moves only that file
  runs `TOOL-dTrueNorth-20` AC13's arm, which reads `AUDIT_WRITER_MARK` out of it
  (`tools/workflows/tier2-review.test.sh:244-262`). Observed by AC4.
- **S4** — finding 19, the same guard from the verification lens. The guard's reader is the one
  `run-gates.sh`'s `changed()` and the spec-token checker's `--legs-for` share, so this pass observes
  the leg listed for the file through `--legs-for`, the review's own probe, and lists the leg on this
  spec's §7 line, which its own Files touched now owes. Observed by AC4.
- **S5** — finding 7. One predicate says what a spec file is. `build_spec_file_re(memory_root)` in
  `design_lib.py` compiles the `-spec-` filename shape `read_spec_revisions` holds as its local
  `inside` (`:484-489`); `read_spec_revisions` refuses a path it does not match, as today, and
  `scan_chain_specs` (`:392-423`) applies it after the cutoff test, counting a spec-folder `.md` it
  does not match under a new `unnamed` reason. The deviation join (`deviation_join.py:500`, `:544`)
  therefore never hands the revision reader a file it refuses. `--chain-specs` prints the new count
  beside the three it prints (`design_lib.py:637`). Observed by AC5 and AC6.
- **S6** — finding 13. `read_consumes_from` (`tools/unattended/lib-unattended.sh:335-357`) reads a
  payload of `none`, bare or backticked, as it reads `external`: well formed, naming no unit, printing
  nothing in either mode, so `scan_consumes_cycles` no longer names the two CLOSED specs that hold it.
  Every other payload from which no id is read stays unreadable. Settled at rung 5 (§8 F4), so this
  pass writes deviation-26 from §4. Observed by AC7, AC8 and AC22.
- **S7** — finding 14, the skeptic's fix. The as-built view's record population and the deviation
  join's spec and record list are TRACKED paths, as `plan()` reads them
  (`tools/memory-tree/gen_build_index.py:2822-2823`): `read_tracked_builds(root, memory_root)` in
  `design_lib.py`, one `ls-files` over `<memory_root>/builds` through `design_lib.run_git`, the call
  `--chain-specs` makes at `:628`, which that verb then calls too. `read_records`
  (`deviation_join.py:238-244`) keeps the tracked paths matching its glob, and `read_population`'s
  `found` (`:497-499`) keeps the tracked `.md` under each chain build. In the same change
  `Fixture.write_tree` (`:900-906`) runs `git read-tree` on its branch after the import, so a
  fixture's records and specs are tracked. A failed `ls-files` is a `DesignRefusal` naming it, which
  each caller maps as it maps the design's other refusals. Observed by AC9 and AC10.
- **S8** — finding 21, the skeptic's fix. `asbuilt_view.py` (`:122`) and `deviation_join.py` (`:145`)
  import `_CL` from `design_lib`. In the same change, `design_lib.py`'s `VIEW_ROW` (`:120`), which
  spells the clause grammar literally in its clause cell today, is rebuilt from `_CL` as `CARRY`
  (`:112`) is, so the clause-id grammar is spelled once (`design_lib.py:107`) and AC11's one-line
  git grep can hold. `TOOL-dTrueNorth-20` AC21's scan
  (`tools/check-spec-tokens.test.sh:1523-1531`) walks each `re.compile`, `re.match`, `re.search` and
  `re.fullmatch` call's pattern argument and flags any call whose subtree holds a str Constant leaf;
  the assignments to `ROW_FOLLOW` and `ROW_DEPARTS` (`asbuilt_view.py:123-124`) are the allowed
  targets, and the liveness half becomes "the walk flagged exactly the allowed targets before the
  allow-list was applied". Observed by AC11 and AC12.
- **S9** — finding 23. `TOOL-dTrueNorth-16` S2's edge refusal at `--dispatch` (`tools/unattended/unattended.sh:13731-13737`)
  builds its producer set as the union of `unit_ids_of` (`:4658`) and `roster_ids` (`:4600`), the
  authored pair with this folder's `unit` asks, the reader that already carries a planned unit with
  no spec; `roster_ids`' exit 3 on a malformed pair refuses with code 49 naming the pair. A
  same-build producer with no `SPEC_PATH` blocks, as `(no spec)`, where today it continues. Settled
  at rung 5 (§8 F5), so this pass writes deviation-27 from §4. Observed by AC13 and AC22.
- **S10** — finding 8. `read_design_view` (`design_lib.py:178-179`) reads the view as
  `read_bytes().decode("utf-8")` with CRLF folded, as `check_view`'s caller (`asbuilt_view.py:551`)
  and `read_chain_clauses` (`design_lib.py:247`) read it, so a bare CR in a row stays in its text
  cell for every reader. A file that is not UTF-8 is the refusal it is today. Observed by AC14.
- **S11** — finding 9. `load_kit_module` (`tools/check-spec-tokens.py:802-824`) returns the module
  it loaded from the kit's path, registering it under `name` only when that slot is free; a
  namesake already in `sys.modules` stays where it is. The docstring says a namesake slot reloads the
  kit's file on each call. Observed by AC15.
- **S12** — finding 10. The header line of `tools/memory-tree/check-memory-hygiene.sh` (`:22`)
  stating TOOL-dTrueNorth-3 S5's superseded trigger, "Check 29 is held unless the commit stages a
  path under a build's spec/ folder or the conf", is rewritten as `TOOL-dTrueNorth-16` S21's rule:
  checks 29 and 30 pass `--staged` through and their verbs decide on the render's trigger,
  `check_index_input`, plus the carries checker for 29 and `DESIGN_RECORD` and `DESIGN_VIEW` for 30.
  Observed by AC16.
- **S13** — finding 15. The same header names check 30 among the checks whose `--staged` reading is
  the verb's, which it omits today. Observed by AC16.
- **S14** — finding 24. The same header points at the two block comments (`:1675-1680`, `:1694-1706`)
  as the rule's statement, so the header no longer states a second one. The instance is added to the
  bug-class checklist under `amendment-leaves-its-other-half-standing`. Observed by AC16.
- **S15** — finding 16. The `SPEC_CARRIES_CUTOFF` comment of `.memory-tree.conf` (`:1001-1007`) names
  its readers: `design_lib.read_design_conf` with `check_cutoff_value` in the carries join
  (`tools/check-spec-tokens.py:1018-1020`), and the generator's own parse of the same file through
  `CARRIES_KEY` (`gen_build_index.py:131`); the sentences naming `read_cutoff_key` and "Nothing reads
  it until TOOL-dTrueNorth-2's join lands" go. Observed by AC17.
- **S16** — finding 17. The as-built view's verdicts gain one: armed, `DESIGN_VIEW` must answer
  `merge: ours` to `git check-attr merge`, read by `check_view_merge` in `asbuilt_view.py` beside
  `check_baseline` and returned among `read_view_inputs`' findings, so `--check-asbuilt` and hygiene
  check 30 name a view whose `.gitattributes` line (`.gitattributes:91`) no longer guards it. The
  comments in `.gitattributes` (`:87-90`), `.memory-tree.conf` (`:984-986`) and `.unattended.conf`
  (`:402-411`) each name all three homes of the path. Settled at rung 3 (§8 F3). Observed by AC18 and
  AC19.
- **S17** — finding 18, the skeptic's fix. `deviation_join.read_blobs` (`:258-277`) routes through
  `tree_lib.read_blobs_at` (`tree_lib.py:308`), keyed on `(rev, path)` pairs at its three call sites
  (`:439`, `:483`, `:599`), so the kit holds one `cat-file --batch` parser: None stays None, a blob
  that is not UTF-8 reads as None, and only `OSError` maps to `Unmeasured`. Its other two parts are
  S1's. Observed by AC1 and AC20.
- **S18** — finding 22, the skeptic's fix. In `run_plant_arms` (`deviation_join.py:1351-1365`) the
  report-mode arm of a plant `derive_plant_needle` maps to None asserts the report render's own
  findings count is 0, the value `render_lines` returns whatever the policy (`:715-747`), and every
  plant with a needle keeps `check_needle`, which no longer takes a None needle. Observed by AC21.

## 3. Non-goals (OUT)

- The three highs, units 23 to 25, and M7 (finding 20), which `TOOL-dTrueNorth-25` closes with H3:
  `deviation_join.py` in `DELEGATES` and an `AC34` that can fail. This unit adds nothing to either.
- The left-shift gates the review suggests per item: the import-closure check, the scrubbed-builder
  scan, the second-batch-reader scan, the suite-reads-outside-its-guard meta check and the
  constant-arm meta assertion. Each is a separate gate and so a separate unit by M2; the close
  left-shifts the confirmed classes.
- `transition_audit.py`'s own `run_git` (`:82-84`) and `read_blobs` (`:392`), the further instances
  of S1's and S17's classes no finding names, and `deviation_join.py:667`'s inline departs pattern,
  which `ROW_DEPARTS` repeats; the class gates above are where they are found.
- `GENERATED_INDEXES` tied to `DESIGN_VIEW` by a check: the memory-tree kit reads no `.unattended.conf`,
  so S16 names it in comments only.
- Editing the frozen specs of units 1 to 20, and dPinnedHandoff's or any other build's specs.

The code this unit amends was built by units 1 to 20, all CLOSED and frozen: `design_lib.py` by
`TOOL-dTrueNorth-1` and `TOOL-dTrueNorth-16`, the carries join and `load_kit_module` by
`TOOL-dTrueNorth-2` and `TOOL-dTrueNorth-16`, the hygiene header by `TOOL-dTrueNorth-3`, the
deviation join by `TOOL-dTrueNorth-4` and `TOOL-dTrueNorth-12`, the view by `TOOL-dTrueNorth-6`, the
dispatch refusals by `TOOL-dTrueNorth-16` and `TOOL-dTrueNorth-20`, and the guard, the AC21 scan,
`read_blobs_at` and the view's `merge=ours` line by `TOOL-dTrueNorth-20`. They are named here and not
as edges: a frozen spec cannot write the mirroring hands-off line check 12's reciprocity arm asks for.

### Edges

- **consumes-from** `TOOL-dTrueNorth-23` — `tree_lib.GIT_ENV_LEAKS` and `read_git_output` as H1 leaves them, which S1 and S17 strip by, and `read_spec_revisions`' pathspec and filename shape, which S5 lifts into one predicate
- **consumes-from** `TOOL-dTrueNorth-24` — `read_population`'s rescope arm and its `read_row_commit` call, beside which S7 moves `found` to tracked paths and S17 re-keys the blob read
- **consumes-from** `TOOL-dTrueNorth-25` — `DELEGATES` and the kit README's render's-code list, which discharge M7, and the README's check-30 sentence S16 extends

## 4. Design

### Why one unit and not two

S6 and S9 write only the unattended kit, a write set disjoint from the rest, which BUILD-METHOD M4
permits as a second batch. §8 F2 keeps one: the dispatcher's rescope row names one unit, and
nothing else at order 10 builds beside it, so a split buys no concurrency.

### What each item reads, and what it does not check

- S1 and S17: the strip covers the location variables the list holds after unit 23; whether any
  other git env variable leaks is the scrubbed-builder scan's question, outside this unit.
- S5: a free-named spec-folder file is passed over and counted, never graded; hygiene check 5 is
  what bans one (TEMPLATE-SPEC, "Multi-spec builds").
- S7: a record staged and not committed is in the index, so it is read; a draft never staged is not.
  A fixture that plants a record in the work tree alone sees it vanish from the view.
- S9: a unit added by a rescope row alone, named in neither the roster pair nor an ask, is still
  invisible to the producer set; the run's practice adds each such unit to the roster table.
- S16: the finding reads the attribute git resolves for the path, so a `.gitattributes` pattern that
  covers the view passes as the literal line does. Each armed fixture that asserts check 30 clean
  writes the attribute: `asbuilt_view.build_view_fixture`, the generator selftest's design fixtures
  (`gen_build_index.py:4995-5010`), and the hygiene suite's check 29 and 30 fixture
  (`tools/memory-tree/check-memory-hygiene.test.sh:4175`).
- S18: it moves no arm count of the routed-commits selftest, and S5's `spec-notes` plant adds its
  own refuse and report arms; twelve report arms stop being constant. The figure is DERIVED at
  writing: `derive_plant_needle` returns None for eleven plants at `190c1eea`, each exiting 0 and
  none in `RISK_PLANTS`, and the twelfth is `spec-notes`, which enters `PLANTS` with exit 0 in
  `PLANT_EXITS` and no needle. The plant table can honour no needle for it: the plant's claim is
  that a notes file adds no finding, and the join's report render prints no line naming the file,
  so a needle would need a render line this unit has no use for. Its report arm is therefore the
  findings-count-0 arm S18 makes.

### Deviation-26 (S6)

`memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-26-deviation-26.md`, written in this
pass's commit with the view re-rendered:

```markdown
# TOOL-dTrueNorth-26 deviation 26 — the dispatch reads a consumes-from none as no edge, a carrier change no clause names

**Serves:** deviation TOOL-dTrueNorth-26

- **Departs from:** `dTrueNorth` [grant]
- **Hand-off:** design-to-spec
- **Before:** the chain's grant PLAY-dClosedLoop-3 lifts veto 2 only for the governance-carrier changes dTrueNorth's own `[chain]` clauses name, and none of `cl-dClosedLoop-0001` to `cl-dClosedLoop-0006` names the edge reader `--dispatch` refuses on
- **After:** TOOL-dTrueNorth-26 makes `read_consumes_from` read a consumes-from payload of `none`, bare or backticked, as it reads `external`, so `--dispatch` no longer refuses a build whose spec declares no producer that way, taken under the owner's standing ruling for a fork whose only options trip veto 2 outside the grant
- **Cause:** review finding
- **Reason:** The closing diff review's finding 13 found two CLOSED specs whose `none` payload reads as unreadable, so every later --dispatch of their builds is refused with a remedy that rewrites a frozen spec, while the hygiene engine admits the same form. Every mechanism that clears it is a governance-carrier change no dTrueNorth clause names, so the fork was settled at rung 5 by the most capable option.
- **Evidence:** `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`, item M5 (finding 13); the standing ruling ER:388 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`); the decision row `PLAY-dClosedLoop-6`; TOOL-dTrueNorth-26 §8 F4
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, citing `PLAY-dClosedLoop-6` (ER:388), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-26
- **Caused-by:** 2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1
- **Surface:** the `--dispatch` verb of `tools/unattended/unattended.sh`, through `read_consumes_from`: a consumes-from payload of none reads as no edge
```

### Deviation-27 (S9)

`memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-26-deviation-27.md`, the same commit:

```markdown
# TOOL-dTrueNorth-26 deviation 27 — the dispatch refuses a consumer whose producer has no spec, a carrier change no clause names

**Serves:** deviation TOOL-dTrueNorth-26

- **Departs from:** `dTrueNorth` [grant]
- **Hand-off:** design-to-spec
- **Before:** the chain's grant PLAY-dClosedLoop-3 lifts veto 2 only for the governance-carrier changes dTrueNorth's own `[chain]` clauses name, and none of `cl-dClosedLoop-0001` to `cl-dClosedLoop-0006` names the dispatch edge refusal of `tools/unattended/unattended.sh`
- **After:** TOOL-dTrueNorth-26 reads the edge refusal's producers from the authored roster and the generated units region together, and a same-build producer with no spec blocks its consumer with code 49, taken under the owner's standing ruling for a fork whose only options trip veto 2 outside the grant
- **Cause:** review finding
- **Reason:** The closing diff review's finding 23 found that the refusal reads only specced units, so a consumer whose producer is planned and unspecced dispatches against code that does not exist, the case TOOL-dTrueNorth-16 S2 exists to stop. Every mechanism that refuses it is a governance-carrier change no dTrueNorth clause names, so the fork was settled at rung 5 by the most capable option.
- **Evidence:** `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`, item M9 (finding 23); the standing ruling ER:388 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`); the decision row `PLAY-dClosedLoop-6`; TOOL-dTrueNorth-26 §8 F5
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, citing `PLAY-dClosedLoop-6` (ER:388), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-26
- **Caused-by:** 2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1
- **Surface:** the `--dispatch` verb of `tools/unattended/unattended.sh`, a code-49 refusal of a consumer whose same-build producer has no spec
```

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `build_spec_file_re` | function, `design_lib.py` | `py.function`, OK |
| `read_tracked_builds` | function, `design_lib.py` | `py.function`, OK |
| `check_view_merge` | function, `asbuilt_view.py` | `py.function`, OK |
| `unnamed` | `scan_chain_specs` skip reason | none |
| `spec-notes` | deviation fixture plant, `PLANTS`, exit 0 in `PLANT_EXITS`, no needle (§4, S18) | none |

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md` (re-rendered from the template, never edited)
- `tools/memory-tree/README.md`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/gate-legs.json`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `.memory-tree.conf`
- `.gitattributes`
- `.unattended.conf`
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (re-rendered by `--write`, never edited)
- `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-26-deviation-26.md` (new)
- `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-26-deviation-27.md` (new)
- the bug-class checklist's `amendment-leaves-its-other-half-standing` entry (S14)

### Alternatives rejected

- **S5: widen the revision pathspec and `inside` to every `.md` under spec/.** It grades files the
  corpus's naming rule says are not specs, and it rewrites the pathspec unit 23 owns.
- **S7: leave the fixture's index empty and read the work tree there.** A fixture would then read
  the population the live tree no longer reads.
- **S8: move `ROW_FOLLOW` and `ROW_DEPARTS` into `deviation_join.py`.** The scan would then meet no
  call it can flag in `asbuilt_view.py`, so its liveness half would read the empty population again.
- **S9: `read_roster_at HEAD <README>`.** It reads a committed blob and no `unit` ask, where
  `roster_ids` is the driver's own reader of planned units and reads the tree `SPEC_PATH` maps.
- **S11: load under a unique `memory_tree.<name>`.** A caller's own `import design_lib` would then
  catch a different `DesignRefusal` class than the one the join raises.

## 5. Production-readiness checklist

- security — S1 and S17 keep every kit git call on the scrubbed environment; S9 refuses rather
  than admits; S7 reads what a commit holds. No new input crosses a trust boundary.
- perf / scale — S7 is one `ls-files` per read, the spawn `--chain-specs` already pays; S17 keeps
  one batch per caller.
- error / empty / loading states — a failed `ls-files`, a malformed roster pair and a missing
  attribute are each a named refusal or finding; none reads as green over nothing.
- observability — S2 names every total, S5 counts `unnamed`, S9 names both units, S16 names the
  path and the attribute.
- risks — S6 lets a build dispatch that is refused today; S7 drops an unstaged draft from the view;
  S16 reds every armed fixture lacking the attribute until it writes one.
- testing — AC1 to AC22 as probes and fixtures; the arms under §7.
- migration — additive: the tree's only armed view already carries the line; `unnamed` is a new
  count beside the old three.
- user docs — `memory/HYGIENE.md` and the kit README for check 30; no page under `help/` covers these
  engines.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch clone or fixture repository sits under a
short `%TEMP%` path with no hook installed.

- **AC1** — When a probe sets every name of `tree_lib.GIT_ENV_LEAKS` in `os.environ`, stubs
  `subprocess.run` to capture its `env`, and calls `design_lib.run_git` and `routed_commits.run_git`,
  neither captured env holds any of them, and `routed_commits` has no `GIT_LOCATION_VARS` attribute.
  Red when: either runner passes `GIT_NAMESPACE` or `GIT_DIR` through.
- **AC2** — When a probe makes scratch repositories A and B, exports `GIT_DIR` naming A's, and calls
  `design_lib.run_git(B, "rev-parse", "HEAD")`, it prints B's HEAD; and
  `python tools/memory-tree/asbuilt_view.py --fixture` run with the same export leaves A's HEAD as it
  was and exits 0.
  Red when: the answer is A's, or the fixture's `git init` re-initialises A.
- **AC3** — When a probe runs `scan_carries` over a one-clause design and two specs carrying it as
  `part 1/2` and `part 2/3`, one `parts` finding names the totals 2 and 3; `part 1/2` with `part 2/2`
  gives none.
  Red when: the first carrier's total is read alone.
- **AC4** — When `python tools/check-spec-tokens.py --legs-for tools/memory-tree/gen_build_index.py`
  runs, it lists `tier2-review self-test`, and a `json.load` of `tools/gate-legs.json` shows that
  leg's guard holding `"{prefix}/memory-tree/gen_build_index.py"`.
  Red when: a scoped run moving only the generator skips the AC13 arm.
- **AC5** — When a probe calls `scan_chain_specs` with a blank cutoff over a chain build's spec path
  and a notes file beside it whose name holds no `-spec-`, the notes file is counted under `unnamed`
  and `read_spec_revisions` over the kept paths returns without `DesignRefusal`.
  Red when: the selector keeps a path the revision reader refuses.
- **AC6** — When `python tools/memory-tree/deviation_join.py --fixture --plant spec-notes` runs, a
  chain build holding an H1-bearing notes file in its spec folder is measured, exit 0.
  Red when: the join prints `nothing measured` naming the notes file.
- **AC7** — When `bash -c '. "tools/unattended/lib-unattended.sh" && read_consumes_from --scan $(git ls-files "memory/builds/*/spec/*.md")'`
  runs, no line has an empty id field, and a scratch spec whose payload is the backticked words
  foo bar still prints one.
  Red when: `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md` prints as unreadable.
  figure: the count was 2 at `6f5f4ddec`, DERIVED by the same command.
- **AC8** — When a scratch preflight fixture holds a build whose CLOSED sibling declares
  `**consumes-from** none` backticked, `unattended.sh --dispatch` of its other unit is not refused
  with code 49.
  Red when: the dispatch names the sibling as unreadable.
  cost: minutes, for a preflight fixture built as `TOOL-dTrueNorth-16` AC2's is.
- **AC9** — When a probe writes an untracked `*-deviation-*.md` into a tracked fixture tree's build
  folder, `deviation_join.read_records` and `asbuilt_view.read_view_inputs` return the same records
  as before; after `git add` of the file, both include it.
  Red when: the untracked draft moves the view's count or rows.
- **AC10** — When a probe builds a `deviation_join.Fixture` and calls `write_tree`, `git ls-files` in
  its root lists every path of the branch's tree.
  Red when: the fixture's index is empty, so its records read as untracked.
- **AC11** — When a probe imports the three modules, `asbuilt_view._CL is design_lib._CL` and
  `deviation_join._CL is design_lib._CL`; and `git grep -n -F 'cl-d[A-Z]\w+-\d{4}' -- tools/memory-tree/`
  prints one line, in `design_lib.py`.
  Red when: a module spells the clause grammar again.
- **AC12** — When the AC21 scan walks `asbuilt_view.py`, it flags exactly `ROW_FOLLOW` and
  `ROW_DEPARTS` before the allow-list and nothing after; walking a scratch copy holding an added
  `re.compile(r"^\| " + _CL)`, it flags that line.
  Red when: a BinOp pattern with a literal leaf passes the scan.
- **AC13** — When a scratch preflight fixture's consumer declares `**consumes-from**` a unit on the
  authored `roster:units` pair with no spec, `unattended.sh --dispatch` of the consumer exits 49
  naming both units and `(no spec)`; with the producer's spec CLOSED, it proceeds.
  Red when: the producer's absence from `gen:build-units` lets the consumer through.
  cost: minutes, the preflight fixture of AC8.
- **AC14** — When a probe writes a scratch view whose row text holds a bare CR and calls
  `read_design_view`, the row is returned with the CR in its text cell.
  Red when: it raises `DesignRefusal` naming a line that is no row of the view's grammar.
- **AC15** — When a probe puts a namesake `tree_lib` from a scratch directory in `sys.modules`, loads
  the checker by path and calls `load_kit_module("tree_lib")`, the module returned has the kit's
  `tools/memory-tree/tree_lib.py` as its file, and `sys.modules["tree_lib"]` is still the namesake.
  Red when: the namesake is returned.
- **AC16** — When `grep -c "Check 29 is held unless the commit stages a path" tools/memory-tree/check-memory-hygiene.sh`
  runs it prints 0, and `sed -n 1,40p tools/memory-tree/check-memory-hygiene.sh` names check 30,
  `check_index_input` and the block comments.
  Red when: the header states a trigger the body does not run.
- **AC17** — When `grep -n -B9 '^SPEC_CARRIES_CUTOFF=' .memory-tree.conf` runs, it names
  `read_design_conf` and `check_cutoff_value` and neither `read_cutoff_key` nor "Nothing reads it".
  Red when: the comment names a reader whose docstring excludes the key.
- **AC18** — When a scratch clone of the tree takes the view's line out of `.gitattributes`,
  `python tools/memory-tree/gen_build_index.py --check-asbuilt` exits 1 naming `DESIGN_VIEW` and
  `merge=ours`; restored, it exits 0 with its clean count line.
  Red when: the view loses its attribute and check 30 stays clean.
- **AC19** — When `grep -c 'GENERATED_INDEXES' .gitattributes`, `grep -c 'gitattributes' .unattended.conf`
  and `grep -c 'gitattributes' .memory-tree.conf` run, each prints at least 1.
  Red when: a home of the path is named in none of the other two.
  figure: each printed 0 at `6f5f4ddec`, PINNED then.
- **AC20** — When a probe calls `deviation_join.read_blobs` over a scratch repository holding a blob
  that is not UTF-8, its answer is None; with `tree_lib.read_git_output` stubbed to raise `OSError`, it
  raises `Unmeasured`; and an `ast` walk of `read_blobs` finds a call of `read_blobs_at` and no
  `--batch` string.
  Red when: the blob decodes with replacement characters, or a short stream raises `ValueError`.
- **AC21** — When a probe wraps `deviation_join.render_lines` so the report policy adds one finding,
  then calls `run_plant_arms`, the report arm of every plant `derive_plant_needle` maps to None
  fails; unwrapped, all hold.
  Red when: a needle-less report arm holds over a planted finding.
  cost: minutes, one fixture per plant.
  figure: twelve such plants after this pass, the eleven at `190c1eea` and `spec-notes`, DERIVED by
  the probe from `derive_plant_needle`.
- **AC22** — When `python tools/memory-tree/deviation_join.py --approval author-recorded` runs after
  this pass, under the chain's value (`PLAY-dClosedLoop-4`), the one the routed-commits host runs
  (`HOST_APPROVAL`, `deviation_join.py:136`), no `refused:` or malformed line names
  `2026-10-22-build-TOOL-dTrueNorth-26-deviation-26`, `2026-10-22-build-TOOL-dTrueNorth-26-deviation-27`
  or `2026-10-22-build-TOOL-dTrueNorth-26-deviation-25`. A run of
  `python tools/memory-tree/deviation_join.py --approval by-risk` does refuse
  deviation-26, whose loosening risk asks an owner where §4 records a spec writer (`LEAST`,
  `:146-147`), as it refuses deviation-20 and deviation-21 at HEAD. Its departures report, under the
  default `report` policy, lists deviation-26 on a `refused:` line beside those two and exits 0.
  Deviation-27, stricter, is not refused there.
  Red when: a dispatch change is recorded nowhere, a record falls outside the grammar, or the
  author-recorded run refuses the spec writer's approval.
  figure: the by-risk header's refused count was 2 at `190c1eea`, DERIVED by the same command; this
  pass adds one.

## 7. Gates

`memory hygiene` · `build-index selftest` · `memory-hygiene self-test` · `routed-commits selftest` · `spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `tier2-review self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `lexicon naming predicates`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC3 AC11 AC12 AC14 AC15 · an env carrying every leak name, a 1/2 and 2/3 carry, a second clause grammar, a BinOp literal pattern, a bare CR row and a namesake module · none
New arm: tools/memory-tree/deviation_join.py (its selftest, run by the routed-commits selftest) · covers AC6 AC9 AC10 AC20 AC21 · a notes file in a spec folder, an untracked record, an empty fixture index, a non-UTF-8 blob and a planted report finding · none
New arm: tools/memory-tree/asbuilt_view.py (its selftest) · covers AC18 · a fixture view with no merge=ours attribute · none
New arm: tools/unattended/unattended.test.sh · covers AC8 AC13 · a CLOSED sibling declaring none, and a producer on the roster with no spec · none

README rule 8 waives the unattended suites' verdict at this landing, so AC8's and AC13's
red-then-green readings at the close are their targeted probes, as `TOOL-dTrueNorth-20` §7 states
for its own. `KIT_MEMORY_TREE_VERSION` is minted by the lander for the delegates this unit moves.

## 8. Open questions

- **F1 — Which binding line does a unit the closing review promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry. (b) reds `unbound` and (c) reds `parts`; veto 1 discards both.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-22, delegated): (a).
  widens: none · relaxes: none
- **F2 — One batch unit or two?** BUILD-METHOD M4 permits a second batch for a disjoint write set,
  and S6 with S9 is one. (a) One unit. (b) Two, the second needing its own rescope add, record and
  spec. Both close every finding; the tie-break is fewer open questions, and (b) opens a unit the
  dispatcher's rescope row does not name for no concurrency at order 10. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-22, delegated): (a). widens: none · relaxes: none
- **F3 — Which mechanism closes finding 17?** (a) A check-30 finding, `check_view_merge`, that
  `DESIGN_VIEW` resolves `merge=ours`, with the three comments naming each other. (b) The comments
  alone, the review's minimum. (c) A check reading `.gitattributes` and `.unattended.conf` from the
  memory-tree kit, a read of another kit's conf the kit does not make today (veto 2, outside the
  grant). (a) meets AC18 and AC19, (b) AC19 alone. Recommendation (a), rung 3, the grant covering
  the view's gate. RESOLVED (agent, 2026-10-22, delegated): (a). grants: PLAY-dClosedLoop-3 check 30's
  merge=ours finding on DESIGN_VIEW for cl-dClosedLoop-0006 · widens: none · relaxes: none
- **F4 — Which mechanism closes finding 13?** (a) `read_consumes_from` reads a `none` payload as
  `external`. (b) The unreadable half of `scan_consumes_cycles` reads non-terminal specs only.
  (c) No change, failing AC7 (veto 1). (a) and (b) each change the `--dispatch` verb, a governance
  carrier no dTrueNorth clause names, so veto 2 holds outside the grant. Rung 5 takes the most
  capable: (a) meets AC7 and AC8 at every status, where (b) still refuses a live spec's `none` that
  the hygiene engine admits. RESOLVED (agent, 2026-10-22, delegated): (a), citing ER:388
  (`PLAY-dClosedLoop-6`), recorded as deviation-26. widens: the --dispatch verb of
  tools/unattended/unattended.sh reads a consumes-from payload of none as no edge · relaxes: none
- **F5 — Which mechanism closes finding 23?** (a) The producer set is `unit_ids_of` with
  `roster_ids`, and a same-build producer with no spec blocks. (b) No change, failing AC13 (veto 1).
  (a) changes the `--dispatch` verb, so veto 2 holds outside the grant and rung 5 takes it, the one
  surviving option. RESOLVED (agent, 2026-10-22, delegated): (a), citing ER:388
  (`PLAY-dClosedLoop-6`), recorded as deviation-27. widens: the --dispatch verb of
  tools/unattended/unattended.sh refuses a consumer whose same-build producer has no spec ·
  relaxes: none
- **F6 — Does the build's grant lift veto 2 for every other carrier edit here?** Each is a change a
  dTrueNorth clause names: S1, S5, S10 and S11 are `cl-dClosedLoop-0001`'s and
  `cl-dClosedLoop-0002`'s readers; S2 and S15 `cl-dClosedLoop-0002`'s join; S12 to S14
  `cl-dClosedLoop-0003`'s check; S7, S17 and S18 `cl-dClosedLoop-0004`'s join; S3 and S4
  `cl-dClosedLoop-0005`'s pin reader; S8 and S16 `cl-dClosedLoop-0006`'s view and gate. RESOLVED
  (agent, 2026-10-22, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3, for all but S6 and S9,
  which F4 and F5 settle. grants: PLAY-dClosedLoop-3 the memory-tree kit, checker, gate-legs guard
  and conf comment edits S1 to S5, S7, S8 and S10 to S18 make for cl-dClosedLoop-0001 to
  cl-dClosedLoop-0006 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft, batching the closing diff review's 10 MEDIUM and 9 LOW findings, M7 handed to TOOL-dTrueNorth-25.
- rev-2 · 2026-10-22 · AC22 · AC21 · S8 · S18 · §4 · the builder's DIVERGENCE: AC22 ran
  `--approval by-risk`, which refuses §4's verbatim deviation-26, a loosening with a spec-writer
  approver. Ruling (a) of the run: AC22 runs `--approval author-recorded`, the chain's value and the
  host's, and states the by-risk refusal and its report listing. `spec-notes` takes no needle, so
  AC21's figure is twelve; S8 states that `VIEW_ROW` is rebuilt from `_CL`. §4's deviation text is
  unchanged.

## 10. Reuse audit

Every item extends a seam the build already has, read at `6f5f4ddec`: `tree_lib.GIT_ENV_LEAKS` and
`read_git_output`'s strip (`tools/memory-tree/tree_lib.py:251-270`), `tree_lib.read_blobs_at`
(`:308`), `read_spec_revisions`' filename shape (`tools/memory-tree/design_lib.py:484-489`),
`--chain-specs`' tracked read (`:628`), `check_baseline` beside which S16's finding sits,
`roster_ids` (`tools/unattended/unattended.sh:4600`), the `external` arm of `read_consumes_from`
(`tools/unattended/lib-unattended.sh:350`), and check-wiring's `merge=ours` read through
`git check-attr` (`tools/check-wiring.sh:1443-1448`). `python tools/codebase-map/reuse_lookup.py
"strip the hook-exported git location variables from a git subprocess environment"` ranked `run_git`
across nine files, `build_git_env` and `read_git_output`, the seam S1 routes to; `python
tools/codebase-map/reuse_lookup.py "read the tracked files under the build folders instead of
globbing the working tree"` ranked `read_text`, `tracked` and `read_conf_key` by name stem and missed
the `ls-files` call `--chain-specs` makes, found by reading `design_lib.py:628`, which S7 lifts into
`read_tracked_builds`.

Recall terms used: `python tools/memory-recall/query.py "how does a closing diff review's minors
batch close each finding against the code the build landed" --terms "closing diff review minors batch
git env leak scrub tracked records cat-file reader clause grammar roster dispatch"`
