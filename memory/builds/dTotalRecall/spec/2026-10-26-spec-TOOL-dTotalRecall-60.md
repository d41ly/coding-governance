# TOOL-dTotalRecall-60 — the round-1 spec audit of units 44 to 53: its 35 minors, batched

**Status:** CLOSED · rev-3 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 31 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-60-deviation-601.md](../build/2026-10-26-build-TOOL-dTotalRecall-60-deviation-601.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-60-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-60-1-acceptance-ledger.md) | log | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-60-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-60-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-60-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-60-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-60-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-60-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-54 TOOL-dTotalRecall-59 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
exited CONVERGED with 41 confirmed findings. Its six highs, ids 1, 4, 13, 15, 24 and 37, are units 54
to 59. This unit is the batch BUILD-METHOD M4 makes of the rest: the 26 MEDIUM findings, ids 2, 3, 5,
6, 7, 8, 12, 14, 16, 17, 18, 19, 20, 21, 25, 26, 27, 29, 30, 32, 33, 38, 39, 40, 42 and 44 (items M1 to
M21), and the 9 LOW findings, ids 9, 10, 11, 22, 23, 31, 34, 35 and 36 (items L1 to L8). Each keeps its
report id and its own scope item. The minors land on units 44 to 53, so this unit repairs none in
particular and builds after every unit: order 31, above the 30 that units 55 to 58 hold. The review
record holds each item's text.

Seven minors report at a lower grade a defect a high unit already closes: ids 6 and 12 (unit 59 cuts
`absorbs`), ids 18 and 19 (unit 54 builds the parser on the real family read), id 2 (unit 54 lands the
parser before step 9), and ids 25 and 44 (unit 55 gives the build-folder scripts reasons of their own).
Each item for them re-observes that unit's fix at this tip, or adds what the finding asks beyond it.
The report's refuted ids 28, 41, 43, 45 and 46 are not in the disposal population.

Re-grounded at `12d219431`. S13, S19, S20 with S11, S24, S26, S30 and S31 build. S23 is cut to what
HEAD can observe, and its block rides owner ask TOOL-dTotalRecall-109 with the held
`TOOL-dTotalRecall-37` (§8 F4). Every other item holds at HEAD or is a ledger line the pass writes, and
keeps its criterion as a check.

## 2. Scope (IN)

Each item states its change to the unit it lands on, as that unit was built; a landed spec is frozen
and is not edited.

- **S1** — id 3 (M1). Holds at HEAD. `TOOL-dTotalRecall-53` AC5's empty-diff demand is replaced by
  render parity, as its rev-5 took in: at the tip `asbuilt_view.py --check` and the instrument's own
  `--check` both exit 0 over the view `DESIGN_VIEW` names, which re-renders whenever a deviation record
  is added. Observed by AC1.
  **Readers:** by name: `2026-10-26-spec-TOOL-dTotalRecall-53.md`, whose S5 and AC5 carry the demand
  as amended; a git grep for the range 462d20f3..HEAD finds no reader outside the memory root.
  by value: NO VALUE READERS — the demand is an observation a pass makes once, and no tool, gate or
  record compares, counts or derives from its result.
- **S2** — id 14 (M1). Holds at HEAD: the same view carries no hand edit. Hygiene check 9's byte-drift
  arm is green at the tip, and the view holds no `Caused-by` header line. Its one line spelling the
  token is the clause row of cl-dClosedLoop-0230, which quotes it. Observed by AC2.
- **S3** — id 5 (M2). Holds at HEAD: `id_grammar.py#scan_readers`, which `--readers` and `--flip-probe`
  call, honours only `# census: kept slug-grammar <reason>` (`id_grammar.py#read_kept_reason`, unit 53
  S34) for split and regex hits alike. Unit 53's two family-index reads are outside the census by shape
  and carry no marker. The census arm's fixture gains a line in each spelling. Observed by AC3.
- **S4** — id 27 (M2). Holds at HEAD: unit 53 re-marked unit 43's `# slug-grammar: kept` lines, so the
  old spelling is gone from `tools`. Observed by AC4.
- **S5** — id 6 (M3). Holds at HEAD: no live carrier of `legacy-records` stays under `tools`,
  `.memory-tree.conf` or `memory/project`. Unit 52 rev-7 AC3's two spared files, a generated
  measurement record and a ledger home whose rows key derived anchors, are spared here. Observed by AC5.
- **S6** — id 12 (M3). Holds at HEAD: no `[[ledger]]` table with `population = "legacy-records"` is in
  `tools/govkit/registry.toml`, where unit 52 put the one registration, or in
  `tools/memory-tree/kit.toml`, read by `tomllib` rather than grep. Observed by AC6.
- **S7** — id 16 (M4). Holds at HEAD by unit 45 S2: `gen_build_index.py#render_spec_skeleton` takes a
  keyword-only `slug`, its header reads the node from `slug[0]`, and `gen_build_index.py#cmd_new_spec`
  and the seven self-test calls (DERIVED 2026-11-24, `grep -n "render_spec_skeleton("`) pass it.
  Observed by AC7.
- **S8** — id 29 (M4). Holds at HEAD: `cmd_new_spec`'s own match, bound to the slug grammar's class, and
  `backlog.SLUG_RE` refuse an id as a `Problem` naming it, before `render_spec_skeleton` is reached.
  Observed by AC8.
- **S9** — id 42 (M4). Holds at HEAD: the self-test's fixture id `ARCH-aFix-3` renders with
  `slug="aFix"`, no root grammar consulted for a family this repo does not declare. Observed by AC9.
- **S10** — id 2 (M5). Holds at HEAD: unit 45's readers run on unit 54's parser, unit 45 consumes it by
  a §3 edge, and unit 54's pass commit `74af3faa4` is an ancestor of unit 45's `c6fcf603b`.
  Observed by AC10.
- **S11** — id 7 (M6). Over the plant `backfill-selection`, after S20, `record_causes.py --check` names
  exactly one causeless record, the one whose Serves line names no id, and no other. Observed by AC11.
- **S12** — id 8 (M7). Replaces unit 47 AC2's named-provenance clause, whose premise moved: unit 47's
  pass ran the verb at its tip and it wrote no record, so its pass commit `a5f016658` modified none.
  Observed by AC12.
- **S13** — id 38 (M8). `record_causes.py --backfill --build <slug>` writes only under
  `<memory root>/builds/<slug>/`. It lists any other record the verb selects as `not backfilled` with the
  reason `another build's record`, and leaves it byte-identical, so a re-run at the prepared merge cannot
  rewrite another build's record. `--backfill` alone reads the whole tree as today. Observed by AC13.
- **S14** — id 17 (M9). Holds at HEAD: in a clone that tracks
  `memory/builds/d2026-10-26ClosedLoop/README.md`, the command, spelled with its tier, writes the spec.
  `cmd_new_spec`'s id match admits the hyphenated slug through the slug grammar's class, so it is not
  re-pointed to `parse_id_parts`. Observed by AC14.
- **S15** — id 18 (M10). Holds at HEAD: `id_grammar.py#parse_id_parts` reads the family set
  `grammar_for(root).families`, declared and cited, and makes no second conf read. Observed by AC15.
- **S16** — id 19 (M11). Holds at HEAD: the era refusal, shown with declared families. `TOOL-001` and
  `TOOL-d119` each raise `ValueError`. Observed by AC16.
- **S17** — id 20 (M12). Unit 44 AC2's thirteen sites, the ten of unit 38's §1 and the three of unit
  44's `TOOL-dTotalRecall-45` row, are matched by file and line text. The text is the split line each
  named function holds at `7047890d5`, the same text at `462d20f3` (DERIVED 2026-11-24, a probe of both
  revisions), recorded in this unit's acceptance ledger before the probe runs.
  `check_policy.py#derive_run_kind`, which no line of that base holds, is listed apart. Observed by AC17.
- **S18** — id 21 (M13). Unit 53 S30's figure is observed: the acceptance ledger holds the tip's
  `journal` count with its counting command, and the guard grep matches a figure with or without a
  thousands comma. Observed by AC18.
- **S19** — id 25 (M14). `CAUSE_WRITER_PINNED`'s ask is live, not only filed. After
  `record_causes.py#check_ask_filed` answers filed, `check_cause_writers` asks
  `backlog.py#check_hold_live`, through `check_ask_live` (§4), and the row is red when that answers
  `None` or `False`. Observed by AC19.
- **S20** — id 26 (M15). `record_causes.py#write_missing_causes` writes the cause line behind the lead
  its record's first Serves line wears, the text before that line's `**Serves:**`, whatever the
  record's extension: `# **Caused-by:** <first Serves id>` under a `# **Serves:**` line. The refusal
  reason `not markdown` is dropped, since the graded set holds no non-Markdown record whose Serves line
  wears no comment prefix (`record_causes.py#read_grading`). Observed by AC20.
  **Readers:** by name: `tools/memory-tree/record_causes.py`, whose `BACKFILL_EXPECTED` and docstring
  spell the reason; `tools/memory-tree/check-memory-hygiene.test.sh`, which asserts it · by value:
  `check_backfill_plant`, which compares each refusal's reason with `BACKFILL_EXPECTED`.
- **S21** — id 30 (M16). Built by unit 48 rev-3 (its F2):
  `tools/runlog/selftest.py#test_record_cause_line` holds unit 36's AC4 arm to the narrowed rule, a head
  with its cause line cut returning no finding and a cause naming an unserved id returning one.
  Observed by AC21.
- **S22** — id 32 (M17). Holds at HEAD: `memory/guides/SESSION-KICKOFF.md`'s `last-audit` stands
  re-stamped over unit 52's change to `.memory-tree.conf`, a watched file. The newest commit to touch a
  watched path, unit 53's `6db81d070`, re-stamps it itself. This pass edits no watched path, so it
  stamps nothing. Observed by AC22.
- **S23** — id 33 (M18). Cut to what HEAD can observe. Unit 53 S20's `linguist-generated` lines ride
  with the held `TOOL-dTotalRecall-37` under owner ask TOOL-dTotalRecall-109. The four renders that unit
  names exist, and none carries the attribute, so a `govkit:generated` block would hold no line. The
  finding's defect, lines inside the `govkit:lf-pins` block, has no instance:
  `tools/govkit/govkit.py#lf_pin_block` writes `eol` pins alone. §8 F1's ruling, a block of its own with
  its writer, update arm and receipt row, rides that ask. Observed by AC23.
- **S24** — id 39 (M19). `id_grammar.py#_READER_SPLIT_SHAPE` exempts only shapes proven safe: `[0]` on a
  `.split("-")` of any maxsplit; `.split("-", 1)` indexed `[1]`; `.rsplit("-")` indexed `[0]`; and
  `.rsplit("-", 1)` indexed `[0]`, `[1]` or `[-1]`. Every other maxsplit, every other `rsplit` and
  every other unindexed split is listed. The plants `x.split("-", 2)[1]` and `x.rsplit("-")[1]` join the
  fixture. The hits it adds at HEAD read no unit id and are marked (DERIVED 2026-11-24, `scan_readers`
  run with §4's shape): `tools/policy/check_policy.py#derive_hygiene_plant`, splitting a cap's name, and
  `tools/process-monitor/census.py#parse_cpu_clock`, splitting a clock value. Observed by AC24.
- **S25** — id 40 (M20). Built by unit 48 rev-3 (its F2): `record.py#check_cause_line` takes the served
  set as the Serves tokens with each `N..M` run read through `UNIT_RANGE_RE`, as
  `record.py#check_serves_line` reads them. Observed by AC25.
- **S26** — id 44 (M21). Unit 49's reason, `record_causes.py#KEPT_INSTRUMENT`, is admitted for the file
  `KEPT_INSTRUMENT_KEY` names under the tool root alone, the one file whose output is `DESIGN_VIEW`. A
  marker or a `CENSUS_KEPT_PATHS` row carrying it on any other file is red naming the file, whatever
  `check_kept_instrument` answers. Unit 55's rows carry reasons of their own. Observed by AC26.
- **S27** — id 9 (L1). The marker is observed doing work over a marked line HEAD holds, since unit
  53's two family-index reads carry none: with the `[0]` exclusion staged off in a scratch copy,
  `--readers` lists those two reads and leaves a marked split unlisted. Observed by AC27.
- **S28** — id 10 (L2). Holds at HEAD: S7's re-point is observed through the parameter. A probe passing
  `slug="xFoo"` with `spec_id="TOOL-dFoo-3"` renders `node x`. Observed by AC28.
- **S29** — id 11 (L3). Unit 53's minors that re-report a high unit's defect number nine, ids 13, 23, 2,
  42, 15, 4, 43, 51 and 12, under five high units; the acceptance ledger states that count.
  Observed by AC29.
- **S30** — id 22 (L4). `tools/runlog/README.md` says, in its "The committed record" head paragraph and
  in "The schema leg"'s paragraph on the fixed head, that the head's optional fourth line is a cause
  line, `**Caused-by:** <target>`, graded for shape and never for absence. Observed by AC30.
- **S31** — id 36 (L4). `record.py#RECORD_SCHEMA` declares the cause line's pattern as `cause_line` beside
  `title`, `serves_kind` and `intro`, and `CAUSE_LINE_RE` compiles it from there, its one spelling.
  Observed by AC31.
- **S32** — id 23 (L5). Unit 51's citations are corrected where a reader looks: the acceptance ledger
  cites `BIND_RE` and `record_paths` at `462d20f3`, lines 410-412 and 421 of `tree_lib.py` there
  (DERIVED 2026-11-24, `git show` of that file at that revision), in the spelling unit 66 S28
  reads. Observed by AC32.
- **S33** — id 31 (L6). Holds at HEAD: `memory/map/generated/` is current for unit 47's
  `write_missing_causes`. Unit 59's tool edit was the section of `tools/lib/resolve-python.test.sh`
  (`47afc8937`), a suite that adds no map symbol. This pass re-renders the map for its own edits.
  Observed by AC33.
- **S34** — id 34 (L7). Holds at HEAD: unit 53 S27's line stands under the table of each build README
  with an order table, 141 READMEs (DERIVED 2026-11-24, `git grep -l` of the table head and of the
  line), and nowhere else. Observed by AC34.
- **S35** — id 35 (L8). Holds at HEAD: the asks units 50 and 53 filed, PLAY-dClosedLoop-1002 and
  PLAY-dClosedLoop-1003, are rendered in `memory/backlog/PLAY.md`, and neither spells a chain build's
  slug, so this run's packet stands. Observed by AC35.

## 3. Non-goals (OUT)

- The six highs: units 54 to 59.
- Editing any landed spec's text, frozen at CLOSED, as §2's opening states.
- The spec lints the report suggests as gates over the set; the close's left-shift step
  (BUILD-METHOD M8) takes them.
- The `govkit:generated` block, its writer, update arm and receipt row: owner ask
  TOOL-dTotalRecall-109, with `TOOL-dTotalRecall-37` (§8 F4).
- A value `--build` should refuse, and a spec id standing in for an ask: `TOOL-dTotalRecall-66`.

### Edges

- **consumes-from** `TOOL-dTotalRecall-36` — the runlog self-test arm of its AC4, which S21 re-observes
- **consumes-from** `TOOL-dTotalRecall-43` — the `# slug-grammar: kept` lines, re-marked, which S4
  re-observes
- **consumes-from** `TOOL-dTotalRecall-44` — the shape-keyed split census and its AC2 sites (ids 20, 39)
- **consumes-from** `TOOL-dTotalRecall-45` — the re-pointed readers and `render_spec_skeleton`'s
  `slug` (ids 2, 10, 16, 17, 29, 42)
- **consumes-from** `TOOL-dTotalRecall-46` — its criteria over the parser, re-observed (ids 18, 19)
- **consumes-from** `TOOL-dTotalRecall-47` — `--backfill`, `write_missing_causes` and its fixture
  (ids 7, 8, 26, 31, 38)
- **consumes-from** `TOOL-dTotalRecall-48` — `check_cause_line` and the run record's head (ids 22, 30,
  36, 40)
- **consumes-from** `TOOL-dTotalRecall-49` — the kept reason and its falsity test (id 44)
- **consumes-from** `TOOL-dTotalRecall-50` — `CAUSE_WRITER_PINNED` and its dClosedLoop ask (ids 25, 35)
- **consumes-from** `TOOL-dTotalRecall-51` — the comment-prefixed cause form and its citations (ids 23,
  26)
- **consumes-from** `TOOL-dTotalRecall-52` — the merged registration and its `.memory-tree.conf` edit
  (ids 6, 12, 32)
- **consumes-from** `TOOL-dTotalRecall-53` — the view's parity, the census marker, S27's order line,
  S30's figure and its ask (ids 3, 5, 9, 11, 14, 21, 27, 34, 35), and S20, held with
  `TOOL-dTotalRecall-37` (id 33)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` and its refusals (ids 2, 18, 19)
- **consumes-from** `TOOL-dTotalRecall-55` — `CENSUS_KEPT_PATHS` and its reasons (ids 25, 44)
- **consumes-from** `TOOL-dTotalRecall-59` — the registration with `absorbs` cut (ids 6, 12)
- **hands-off** `TOOL-dTotalRecall-65` — the reasons S26 grades, which that unit reads from its registry after this pass (the round-1 audit of units 54 to 60, id 27)
- **hands-off** `TOOL-dTotalRecall-66` — S8, S13, S19, S20, S23, S24 and AC10, AC18 and AC32, which that unit settles (the round-1 audit of units 54 to 60, ids 7, 9, 10, 16, 19, 20, 25, 33, 35, 44, 45, 46, 47, 48 and 50)

## 4. Design

### How the batch builds

One pass, after every unit of a lower order is terminal. The code items share `record_causes.py` and
`id_grammar.py`, which `TOOL-dTotalRecall-58` and `TOOL-dTotalRecall-65` also write, so BUILD-METHOD M6
sequences the passes: unit 58's first, then this one, then unit 65's, which consumes this unit. Within
the pass the order is S24; S20 before S11, since S11 counts what S20 leaves; S13, S19 and S26; S30 and
S31; then the ledger items S17, S18, S29 and S32, and the observations.

### The split shape of S24

```text
\.split\(\s*(["'])-\1\s*(?!,\s*1\s*\)\[1\])[^)]*\)(?!\[0\])
\.rsplit\(\s*(["'])-\2\s*(?!,\s*1\s*\)\[(?:0|1|-1)\])(?!\)\[0\])[^)]*\)
```

They replace the Python half of `_READER_SPLIT_SHAPE`, its shell half unchanged, and the comment above
it says so. A `.split` indexed `[0]` is the family at any maxsplit. `.rsplit("-", 1)` cuts at the last
hyphen, so both its ends survive a hyphen in the slug. A larger maxsplit on `rsplit` does not, and is
listed at `[0]` too. A call naming `sep=` first is not read, as today; one naming `maxsplit=`, or
closing on a later line, is listed or not read, never exempted as safe.

### The ask's liveness of S19

`check_ask_live(root, ask_id)` in `record_causes.py` reads the corpus and the finished fold once per
census run, through `gen_build_index.py#read_backlog_at_rev(root, "HEAD", conf)`, the reader
`--asks --ready` answers from, and returns why the ask is not live, or None. `None` from
`check_hold_live` reads `HEAD files neither an ask nor a spec of that id`; `False` names the ask's
terminal status. It is asked only of a row whose instrument stands and whose ask is filed, and a tree
with no pinned rows reads no corpus. A `gen_build_index.Problem` is a refused read, `--check`'s exit 2
naming it. The read costs 8.5 s here (DERIVED 2026-11-24, node a, one probe), inside the `record causes`
leg's 180 s ceiling (DERIVED, `tools/gate-legs.json`). The fixture's conf declares
`BACKLOG_MODE="builds"` for the `PINNED_PLANTS`, without which that reader holds no ask and a standing
row reads not live.

### The plants

- `other-build-causeless` joins `BACKFILL_PLANTS`: one causeless record under `fRoot` and one under
  `fClaim`, graded by `check_backfill_plant` with `--build fRoot`.
- `backfill-selection` keeps its records. `BACKFILL_EXPECTED` moves the `-probe.sh` record from the
  refusals to the paths written, and its grade asserts one prefixed cause line under that record's
  Serves line after the second run.
- `pinned-ask-closed` joins `PINNED_PLANTS`: the departures plant with a `WONTDO` row for `PINNED_ASK`,
  written by `backlog.py#render_status_row`. It passes when `--check` exits 1 naming the row not live.
- `reason-on-other-file` builds `kept-instrument-not-legacy`'s fixture with the view's `-` row kept, so
  the reason holds for `KEPT_INSTRUMENT_KEY`. It adds a tool-root writer whose marker carries the
  reason, and `KEPT_SCRIPT` spelling a Serves literal past its window under a `kept` row carrying it.
  `--check` exits 1 naming both, and not the renderer.
- `old-marker`, `new-marker`, `split-maxsplit-two` and `rsplit-bare` join `_SPLIT_PLANTS` in
  `tools/memory-recall/selftest.py`, `old-marker` spelled in parts so AC4's grep stays empty, and each
  line that the census reads there carries the marker its neighbours carry.

### Inventory

Minted: `--build` on `record_causes.py --backfill`; `check_ask_live` in the same module; the
`RECORD_SCHEMA` key `cause_line`; the plants above. Naming cells: `check_ask_live` satisfies cell
`py.function` (`python tools/lexicon/lexicon.py --suggest check_ask_live --as py.function`, 2026-11-24);
flags, keys and plants have no cell.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/check-memory-hygiene.test.sh` (the arms of S13, S19, S20 and S26)
- `tools/memory-recall/selftest.py` (the arm of S3 and S24)
- `tools/policy/check_policy.py` and `tools/process-monitor/census.py` (S24's two markers)
- `tools/runlog/record.py`
- `tools/runlog/README.md`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Fold each minor into its unit's spec.** M4 refuses folding at the exit.
- **Split into two batches.** Both halves would regenerate `memory/map/generated/` with its generator,
  which M6 clause 3 forbids two concurrent passes to share, and their plants sit in one fixture.
- **Write S23's lines inside the `govkit:lf-pins` block.** Every existing adopter would read
  `pins-moved` on unchanged pins (§8 F1).
- **Mint S23's block now, with no line to write.** An empty block is scaffolding for a held unit.

## 5. Production-readiness checklist

- security — S13 narrows a write to one build's folder; no other surface.
- perf / scale — S19 adds one corpus read per census run; S24 widens one regex.
- error / empty / loading states — S13 lists what it will not write; S19 reds a closed ask and refuses
  an unreadable corpus; S26 reds a reason on the wrong file.
- observability — S13 prints the unwritten records; S19's red names the ask and its answer.
- risks — S24's two added hits are marked in the pass; an id reader added later is listed by
  `--readers` and by the flip probe, and no leg runs `--readers` over the tree.
- testing — AC1 to AC35 by the pass; the arms of §7 at the close.
- migration — none: S31's schema key is additive, and no record is rewritten.
- user docs — none under `help/`: S30's README is the runlog kit's own reference, not a help page.

## 6. Acceptance criteria

Where a criterion reads "as at HEAD", the pass observes it and builds nothing for it.

- **AC1** — When `python tools/memory-tree/asbuilt_view.py --check` and
  `python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py --check` run at
  the tip, both exit 0, as at HEAD. Red when: the view's bytes differ from its render.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 9` runs at the tip it exits 0,
  and `grep -cE "^(- )?\*\*Caused-by:\*\*" 2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` run from
  `memory/builds/dClosedLoop/build/` prints `0`, as both do at HEAD.
  Red when: a hand edit lands in the view.
- **AC3** — When `python id_grammar.py --readers <fixture>` runs from `tools/memory-tree/` at the tip over
  a fixture holding a split line marked `# census: kept slug-grammar x` and one marked
  `# slug-grammar: kept x`, it lists the second and not the first. Red when: the old spelling still
  exempts.
  fixture: a throwaway git tree under the run's scratch directory; the pass makes it.
- **AC4** — When `git grep -n "slug-grammar: kept" -- tools` runs at the tip, it prints nothing, as at
  HEAD. Red when: a line keeps the old spelling.
- **AC5** — When `git grep -n "legacy-records" -- tools .memory-tree.conf memory/project ':!tools/run-gates/ceiling-evidence.txt' ':!memory/project/record-kinds-legacy.txt'`
  runs at the tip, it prints nothing, as at HEAD. Red when: a live carrier of the old name stays.
- **AC6** — When a `tomllib` probe reads `tools/govkit/registry.toml` and `tools/memory-tree/kit.toml` at
  the tip, no `ledger` table has `population` `legacy-records`, and one has `record-kinds-legacy`.
  Red when: the old registration survives, or the merged one is gone.
- **AC7** — When `grep -n "render_spec_skeleton(" gen_build_index.py` runs from `tools/memory-tree/` at the
  tip and each listed call is read to its closing parenthesis, the signature takes `slug` after a bare
  `*` and every call passes it. Red when: a caller omits it, or the header splits `spec_id`.
- **AC8** — When `python tools/memory-tree/gov_record.py new spec TOOL-x --tier 2` runs at the tip, it
  exits 2 with a message naming `TOOL-x`, as at HEAD. Red when: it raises a traceback or writes a file.
- **AC9** — When a `python -c` probe calls `render_spec_skeleton` over `memory/TEMPLATE-SPEC.md` with
  `spec_id="ARCH-aFix-3"` and `slug="aFix"`, the header reads `node a`, as at HEAD.
  Red when: the call raises on the undeclared family.
- **AC10** — When `git merge-base --is-ancestor 74af3faa4 c6fcf603b` runs, it exits 0, and
  `grep -c "consumes-from.*TOOL-dTotalRecall-54" 2026-10-26-spec-TOOL-dTotalRecall-45.md` run from the
  spec folder prints at least `1`. Red when: unit 45 ran before the parser landed.
- **AC11** — When `python record_causes.py --fixture --plant backfill-selection` runs from
  `tools/memory-tree/`, its `check` lines name the `-unbound.md` record under `causes` and no other, and
  the plant prints `PASS`. Red when: it names the `-probe.sh` record or none.
- **AC12** — When `git diff-tree --no-commit-id --name-status -r a5f016658 -- 'memory/builds/*/build/*' 'memory/builds/*/prompts/*' 'memory/builds/*/reviews/*'`
  runs, it prints unit 47's own ledger as added and no modified record, as at HEAD.
  Red when: that pass rewrote a record it did not add.
- **AC13** — When `python record_causes.py --fixture --plant other-build-causeless` runs from
  `tools/memory-tree/`, `--backfill --build fRoot` there writes the `fRoot` record and lists the `fClaim`
  one `not backfilled`, `git status --porcelain` names the first alone, and the plant prints `PASS`.
  Red when: the verb writes outside the named build.
- **AC14** — When `python tools/memory-tree/gov_record.py new spec TOOL-d2026-10-26ClosedLoop-3 --tier 2`
  runs in the flipped clone `TOOL-dTotalRecall-45` AC1 makes, the spec it writes carries `node d` in its
  status header. Red when: it exits with the usage or id refusal.
  fixture: the scratch clone under the run's scratch directory; the pass makes it.
- **AC15** — When a `python -c` probe in a scratch tree declaring `RECALL_CITED_FAMILIES="ZED"` calls
  `parse_id_parts` with one id of each of `grammar_for(root).families`, it returns each family, and for
  a family outside them it raises `ValueError`. Red when: a cited family is refused.
  fixture: the scratch tree under the run's scratch directory; the pass makes it.
- **AC16** — When the probe calls `parse_id_parts("TOOL-001", ".")` and `parse_id_parts("TOOL-d119", ".")`,
  each raises `ValueError`, as at HEAD. Red when: either returns a tuple.
- **AC17** — When the tip's `id_grammar.py --readers <worktree>` runs over a scratch worktree at
  `7047890d5`, each of the thirteen ledgered site texts is listed with its file, and `derive_run_kind`'s
  apart. Red when: a site text is missing.
  fixture: the scratch worktree under the run's scratch directory; the pass makes it.
- **AC18** — When the counting command the ledger names for S18, the `S` rows of
  `python tools/memory-tree/gen_build_index.py --print-bindings` whose third TAB field is `journal`, runs
  at the tip, it prints the ledgered figure, and
  `git grep -nE "[0-9][0-9,]*[0-9] .?journal" -- tools memory/guides memory/HYGIENE.md` prints no hit
  without its command beside it. Red when: a figure ships with no command.
  figure: DERIVED at the tip, by that command.
- **AC19** — When `python record_causes.py --fixture --plant pinned-ask-closed` runs from
  `tools/memory-tree/`, its `--check` exits 1 naming the row and its ask, and the plant prints `PASS`; at
  the tip `python record_causes.py --cause-writers` prints the PLAY-dClosedLoop-1002 row with no red.
  Red when: a closed ask keeps the row, or a live one reds it.
- **AC20** — When `python record_causes.py --fixture --plant backfill-selection` runs, the `-probe.sh`
  record holds one `# **Caused-by:** TOOL-fRoot-1` line, under its Serves line, after both backfills, and
  the second prints `0 backfilled`; `bash -n` over the same bytes exits 0.
  Red when: the line is bare, doubled or absent.
- **AC21** — When a `python -c` probe calls `check_cause_line(4, line, ["X-xFixtureRun-1"])` from
  `tools/runlog/record.py`, an empty line returns no finding and a cause naming `X-xFixtureRun-9` returns
  one, as at HEAD. Red when: absence reds, or the old arm stands.
- **AC22** — When `git log -1 --format=%H -G"^last-audit:" -- memory/guides/SESSION-KICKOFF.md` and
  `git log -1 --format=%H --` over the paths of that file's `watch:` line run at the tip, the first is the
  second or a descendant of it. Red when: the stamp is older than the last change to a watched file.
- **AC23** — When `git grep -n "linguist-generated\|govkit:generated" -- .gitattributes tools` runs at
  the tip it prints nothing, as at HEAD. Red when: the attribute or a block for it lands while unit 37 is
  held.
- **AC24** — When `python id_grammar.py --readers <fixture>` runs over the fixture with
  `split-maxsplit-two` and `rsplit-bare`, it lists both, and none of `x.rsplit("-", 1)[1]`,
  `x.rsplit("-", 1)[0]`, `x.split("-", 1)[1]` and `x.split("-", 2)[0]`; at the tip `--readers` lists no
  line of `check_policy.py` or `census.py`. Red when: a maxsplit or rsplit reader is unlisted, or a safe
  shape is listed.
  fixture: AC3's throwaway git tree, with these lines.
- **AC25** — When the probe calls `check_cause_line` with the served token `X-xFixtureRun-1..3`, a cause
  of `X-xFixtureRun-2` returns no finding and `X-xFixtureRun-4` returns one, as at HEAD.
  Red when: the range is not expanded.
- **AC26** — When `python record_causes.py --fixture --plant reason-on-other-file` runs from
  `tools/memory-tree/`, it exits 1 with one red per planted file and none naming the view's renderer.
  Red when: the reason keeps a file that is not that renderer.
- **AC27** — When `--readers` runs from a scratch copy of the tree whose `_READER_SPLIT_SHAPE` has lost
  its `[0]` exemption, it lists the index-0 reads of `gen_build_index.py#cmd_asks` and
  `backlog.py#render_family_view` and not the marked date split of `row_grammar.py#cmd_ages`.
  Red when: the marker changes nothing.
  fixture: the scratch copy under the run's scratch directory; the pass makes it.
- **AC28** — When a `python -c` probe calls `render_spec_skeleton` with `spec_id="TOOL-dFoo-3"` and
  `slug="xFoo"`, the header reads `node x`, as at HEAD. Red when: it reads `node d`.
- **AC29** — When `grep -c "nine"` runs over this unit's acceptance ledger entry for S29, it prints at
  least `1`. Red when: the count is not stated.
- **AC30** — When `grep -n "Caused-by" tools/runlog/README.md` runs at the tip, it prints a line in each
  of S30's paragraphs. Red when: either paragraph still describes the fixed head alone.
- **AC31** — When a `python -c` probe imports `tools/runlog/record.py`, `RECORD_SCHEMA["cause_line"]`
  equals `CAUSE_LINE_RE.pattern`, and the module's source spells that pattern once.
  Red when: the key is absent, or the regex has a second spelling.
- **AC32** — When `git show` prints the memory-tree kit's `tree_lib.py` at revision `462d20f3`, its
  lines 410 to 412 and 421 hold `BIND_RE` and `def record_paths`, and the ledger line for S32 spells `tools/memory-tree/tree_lib.py@462d20f3:410-412`
  and `:421` at that revision. Red when: the cited lines hold something else.
- **AC33** — When `python tools/codebase-map/gen_map.py --check` runs at the tip, it exits 0, and
  `grep -c '"write_missing_causes"' memory/map/generated/symbols.json` prints at least `1`.
  Red when: the symbols tier is stale.
- **AC34** — When a `python -c` probe reads every tracked build README, each holding a
  `| Step | Units | Parallel |` table carries S27's line under it and no other does, as at HEAD.
  Red when: a table lacks the line, or the line stands with no table.
- **AC35** — When `python tools/memory-tree/gen_build_index.py --check` runs at the tip it exits 0, and
  `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --check dTotalRecall`
  exits 0. Red when: `memory/backlog/PLAY.md` or the packet is stale.
  cost: the packet check ran past 13 minutes unfinished on node a (PINNED 2026-11-24), so it runs in the background.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory-recall kit selftest` · `drift-audit selftest` · `policy fixtures` · `playbook render selftest` · `kit/dogfood doc parity` · `runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `routed-commits selftest` · `scratch-guard self-test` · `process-monitor census selftest` · `measure-legs selftest` · `govkit selftest` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC11 AC13 AC19 AC20 AC26 · the plants `other-build-causeless`, `pinned-ask-closed`, `reason-on-other-file` and the moved `backfill-selection`, staged by skipping each new test and by restoring the `not markdown` refusal · none
New arm: tools/memory-recall/selftest.py · covers AC3 AC24 · the plants `old-marker`, `new-marker`, `split-maxsplit-two` and `rsplit-bare`, in the census arm it already runs, staged by restoring the old shape and by reading the old marker · none

## 8. Open questions

- **F1 — Where do S23's `linguist-generated` lines go?** Options: (a) a block of their own,
  `govkit:generated`, with its writer, update arm and receipt row; (b) inside `govkit:lf-pins`, with
  the update comparison widened and an adopter migration stated. (b) flips every existing adopter to
  `pins-moved` on unchanged pins until the migration runs, which is the finding's defect; veto 1
  discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the only option surviving the
  vetoes. widens: none · relaxes: none. F4 says when it is built.
- **F2 — May S22 re-stamp `memory/guides/SESSION-KICKOFF.md`, a governance carrier?** Options: (a) yes,
  under the build's grant, the stamp following unit 52's edit of a watched file; (b) no, leaving the
  `kickoff-manifest ratchet` leg red from unit 52's pass to the close. (b) fails AC22. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 5, the README's `may:` grant, as `TOOL-dTotalRecall-43` §8 F3 used
  it. grants: PLAY-dClosedLoop-3 SESSION-KICKOFF.md's last-audit stamp follows unit 52's
  `.memory-tree.conf` edit · widens: none · relaxes: none. Units 52 and 53 stamped it in their own
  passes, so this pass uses the grant for nothing.
- **F3 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of one unit's clause, which would split a clause that unit carries whole. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F4 — Does S23 build its block while `TOOL-dTotalRecall-37` is held unbuilt?** Unit 53 §8 F3 sent S20,
  the lines the block would hold, to owner ask TOOL-dTotalRecall-109 with unit 37. Options: (a) S23 keeps
  an observation of HEAD and its block rides that ask; (b) build the block, its update arm and its
  receipt row with no line to write; (c) hold this unit and its consumers until unit 37 builds. (b) is
  scaffolding no reader uses, which `[yagni]` refuses; (c) parks the other items for one. RESOLVED
  (agent, 2026-11-24, delegated): (a), M3, per
  `2026-11-24-prompt-TOOL-dTotalRecall-60-reground-brief` items 3 and 4. widens: none · relaxes: none
- **F5 — Which corpus does S19 ask liveness over?** Options: (a) `read_backlog_at_rev` at `HEAD`, the one
  existing reader that returns a corpus and its fold without rendering; (b) `gen_build_index.py#collect`,
  which reads every build and prints its own lines; (c) a worktree corpus assembled in
  `record_causes.py`. (c) is a second assembly of one read; (b) costs a whole index collection per
  census. (a) sees an uncommitted closing row one commit late, and a row naming an ask not yet
  committed reads not live until it is. RESOLVED (agent, 2026-11-24, delegated): (a), M3, the one that
  adds no reader. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, its 35
  minors batched (26 MEDIUM, 9 LOW).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-65, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-3 · 2026-11-24 · §1 · S1 to S35 · §3 · §4 · §5 · AC1 to AC35 · §7 · §8 F1, F2, F4, F5 · §10 ·
  re-grounded over `12d219431` per `2026-11-24-prompt-TOOL-dTotalRecall-60-reground-brief`: S1 to S10,
  S12, S14 to S16, S21, S22, S25, S28 and S33 to S35 hold at HEAD and keep their criteria as checks;
  S23 is cut and rides ask TOOL-dTotalRecall-109 (F4); S20 drops a refusal nothing can reach; S19 names
  its corpus (F5); S24 states the safe shapes whole and marks the two hits it adds; S26 grades the
  registry rows too; S27 reads a marked line HEAD holds; AC2 and AC5 spare the text HEAD quotes; AC9 and
  AC22 are probes, since a suite and a leg are no observation; arms move to the suites that hold them,
  and §7 takes the legs the guard join names; every citation is a symbol or a pinned revision.

## 10. Reuse audit

Each item extends the seam its finding names, cited in the item: unit 44's `--readers` predicate
`tools/memory-tree/id_grammar.py#_READER_SPLIT_SHAPE`, with `#read_kept_reason` as the one marker
reader; unit 47's `tools/memory-tree/record_causes.py#write_missing_causes`, with the lead
`tools/memory-tree/tree_lib.py#BIND_RE` matches; `#check_ask_filed` and
`tools/memory-tree/backlog.py#check_hold_live` over
`tools/memory-tree/gen_build_index.py#read_backlog_at_rev`; `#check_kept_instrument`; and
`tools/runlog/record.py#RECORD_SCHEMA`. No mechanism here is new.
`python tools/codebase-map/reuse_lookup.py "answer whether an ask is live from the backlog fold"`, run
2026-11-24, ranked name-stem neighbours (`live`, `ask`, `render_ask_row`) and no seam these items bypass.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
