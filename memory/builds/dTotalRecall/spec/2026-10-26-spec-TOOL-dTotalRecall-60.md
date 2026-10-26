# TOOL-dTotalRecall-60 — the round-1 spec audit of units 44 to 53: its 35 minors, batched

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 31 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 |

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

## 2. Scope (IN)

Each item states its change to the unit it lands on, as that unit was built; a landed spec is frozen
and is not edited.

- **S1** — id 3 (M1). `TOOL-dTotalRecall-53` AC5's empty-diff demand is replaced by render parity:
  at the tip `asbuilt_view.py --check` and the instrument's own `--check` both exit 0 over the view
  `DESIGN_VIEW` names, which re-renders whenever a deviation record is added. Observed by AC1.
  **Readers:** by name: `2026-10-26-spec-TOOL-dTotalRecall-53.md`, whose S5 and AC5 are the one
  carrier spelling the empty-diff demand over the view; a git grep for the range 462d20f3..HEAD finds
  it there and in the round-1 review record that reports it, and nowhere outside the memory root.
  by value: NO VALUE READERS — the demand is an observation a pass makes once, and no tool, gate or
  record compares, counts or derives from its result.
- **S2** — id 14 (M1). The same view carries no hand edit: hygiene check 9's byte-drift arm is green at
  the tip, and the view holds no `Caused-by` line. Observed by AC2.
- **S3** — id 5 (M2). The slug census reads one marker: `id_grammar.py --readers` and `--flip-probe`
  honour only `# census: kept slug-grammar <reason>` (unit 53 S34's grammar) for split and regex hits
  alike, and unit 53 S2's two family-index lines carry that spelling. Observed by AC3.
- **S4** — id 27 (M2). Unit 43's `# slug-grammar: kept` lines are re-marked in S34's grammar, so the old
  spelling is gone from `tools`; unit 53 S16 is a re-observation of unit 43 S14, not a second reader.
  Observed by AC4.
- **S5** — id 6 (M3). `TOOL-dTotalRecall-52` AC3 holds once unit 59 has cut `absorbs`: no carrier of
  `legacy-records` stays under `tools`, `.memory-tree.conf` or `memory/project`. Observed by AC5.
- **S6** — id 12 (M3). No `[[ledger]]` table with `population = "legacy-records"` remains in
  `tools/memory-tree/kit.toml`, read by `tomllib` rather than grep. Observed by AC6.
- **S7** — id 16 (M4). `render_spec_skeleton` (`tools/memory-tree/gen_build_index.py:8521`) gains a
  keyword-only `slug`, and its header reads the node from `slug[0]`, never from `spec_id`. Its eight
  callers pass it: `cmd_new_spec` at `:8623` the slug it already parsed (`:8594`), and the self-test
  sites at `:8248`, `:8249`, `:8266`, `:8281`, `:8282`, `:8293` and `:8297` their fixture slug.
  Observed by AC7.
- **S8** — id 29 (M4). An id the tree's grammar refuses is refused by `cmd_new_spec` as a `Problem`
  naming the id, before `render_spec_skeleton` is reached. Observed by AC8.
- **S9** — id 42 (M4). The self-test's fixture id `ARCH-aFix-3` stays valid with no conf of its own:
  its calls pass `slug="aFix"`, so no root grammar is consulted for a family this repo does not
  declare. Observed by AC9.
- **S10** — id 2 (M5). Unit 45's three readers run on unit 54's parser: unit 45 consumes it by a §3
  edge, and unit 54's pass commit (step 8) precedes unit 45's (step 9). Observed by AC10.
- **S11** — id 7 (M6). Over `TOOL-dTotalRecall-47`'s fixture, after S20, `record_causes.py --check`
  names exactly one causeless record, the one whose Serves line names no id, and no other.
  Observed by AC11.
- **S12** — id 8 (M7). Unit 47 AC2's named-provenance clause is replaced by its derived form: every
  record unit 47's pass commit backfilled was added after unit 36's pass commit. Observed by AC12.
- **S13** — id 38 (M8). `record_causes.py --backfill --build <slug>` writes only under
  `memory/builds/<slug>/` and lists any other causeless record unwritten, so a re-run at the prepared
  merge cannot rewrite another build's record. Observed by AC13.
- **S14** — id 17 (M9). Unit 45 AC2's flipped-clone command is spelled with its tier,
  `--new-spec TOOL-d2026-10-26ClosedLoop-3 --tier 2`, in a clone that tracks
  `memory/builds/d2026-10-26ClosedLoop/README.md` (`:8600-8601`). Where `cmd_new_spec`'s own id match
  (`:8590`, `[a-z][A-Za-z0-9]*` for the slug) still refuses a hyphenated slug at this tip, that match is
  re-pointed to `parse_id_parts`. Observed by AC14.
- **S15** — id 18 (M10). `parse_id_parts` reads the family set `grammar_for(root)` reads, declared and
  cited, as unit 54 built it; no second conf read exists. Observed by AC15.
- **S16** — id 19 (M11). The era refusal is shown with declared families: `TOOL-001` and `TOOL-d119`
  each raise `ValueError`. Observed by AC16.
- **S17** — id 20 (M12). Unit 44 AC2's thirteen sites are matched by file and line text, the text
  `git show 462d20f3:<file>` prints at each cited line, recorded in this unit's acceptance ledger
  before the probe runs. Observed by AC17.
- **S18** — id 21 (M13). Unit 53 S30's figure is observed: the acceptance ledger holds the tip's
  `journal` count with its counting command, and the guard grep matches a figure with or without a
  thousands comma. Observed by AC18.
- **S19** — id 25 (M14). `CAUSE_WRITER_PINNED`'s ask is resolved through `backlog.check_hold_live`
  (`tools/memory-tree/backlog.py:878`): the row is red when that answers `None` or `False`.
  Observed by AC19.
- **S20** — id 26 (M15). `write_missing_causes` (unit 47) writes a prefixed cause line for a record
  whose Serves line carries a comment prefix, `<prefix>**Caused-by:** <first Serves id>`, the prefix
  being the one `tree_lib.BIND_RE` captures (`tools/memory-tree/tree_lib.py:410-412`). Only an
  extension with no line-comment syntax stays `not backfilled`. Observed by AC20.
- **S21** — id 30 (M16). Unit 36's AC4 arm in `tools/runlog/selftest.py` is rewritten to unit 48's
  rule: a head with its cause line cut returns no finding, and a cause naming an unserved id returns
  one. Observed by AC21.
- **S22** — id 32 (M17). `memory/guides/SESSION-KICKOFF.md`'s `last-audit` stands re-stamped at the tip
  over unit 52's change to `.memory-tree.conf`, a watched file, under §8 F2's grant. Observed by AC22.
- **S23** — id 33 (M18). govkit writes the `linguist-generated` lines of unit 53 S20 in a block of
  their own, `govkit:generated`, with its own writer beside `lf_pin_block`
  (`tools/govkit/govkit.py:5845`), its own `update` arm and its own receipt row, so the `govkit:lf-pins`
  span `update` compares (`:9917-9926`) is untouched. Observed by AC23.
- **S24** — id 39 (M19). The split census exempts only shapes proven safe: `[0]` on any split,
  `.split("-", 1)` indexed `[0]` or `[1]`, and `.rsplit("-", 1)` indexed `[1]` or `[-1]`. Every other
  maxsplit and every other `rsplit` is listed, the plants `x.split("-", 2)[1]` and `x.rsplit("-")[1]`
  join the fixture, and each new base hit is re-pointed or marked. Observed by AC24.
- **S25** — id 40 (M20). `check_cause_line` (unit 48) takes the served set as the Serves tokens with
  each `N..M` run expanded, parsed as `check_serves_line` parses them (`tools/runlog/record.py:1461-1478`).
  Observed by AC25.
- **S26** — id 44 (M21). Unit 49's reason is admitted for `tools/memory-tree/asbuilt_view.py` alone, the
  one file whose output is `DESIGN_VIEW`; a keep carrying it on any other file is red. Unit 55's rows
  carry reasons of their own. Observed by AC26.
- **S27** — id 9 (L1). Unit 53 S2's marker is observed doing work: with unit 44's `[0]` exclusion staged
  off in a scratch copy, `--readers` leaves the two marked lines unlisted and lists an unmarked index-0
  plant. Observed by AC27.
- **S28** — id 10 (L2). S7's re-point is observed through the parse: a probe passing `slug="xFoo"` with
  `spec_id="TOOL-dFoo-3"` renders `node x`. Observed by AC28.
- **S29** — id 11 (L3). Unit 53's minors that re-report a high unit's defect number nine, ids 13, 23, 2,
  42, 15, 4, 43, 51 and 12, under five high units; the acceptance ledger states that count.
  Observed by AC29.
- **S30** — id 22 (L4). `tools/runlog/README.md` says, under "The committed record" (`:366-370`) and at
  the schema-leg paragraph (`:513-516`), that the head's optional fourth line is a cause line graded
  for shape only. Observed by AC30.
- **S31** — id 36 (L4). `RECORD_SCHEMA` (`tools/runlog/record.py:176-181`) declares the cause line's
  pattern as `cause_line` beside `title`, `serves_kind` and `intro`, so the schema leg compiles it from
  data. Observed by AC31.
- **S32** — id 23 (L5). Unit 51's citations are corrected where a reader looks: the acceptance ledger
  cites `tools/memory-tree/tree_lib.py:410-412` for `BIND_RE` and `:421` for `record_paths`.
  Observed by AC32.
- **S33** — id 31 (L6). `memory/map/generated/` is current at the tip for unit 47's
  `write_missing_causes` and for unit 59's edit of `tools/lib/legacy_ledger.py`. Observed by AC33.
- **S34** — id 34 (L7). Unit 53 S27's line reaches every build README with an order table: the
  `gen:build-order` regions are re-rendered by `gen_build_index.py --write`, and the line is written
  only under a table. Observed by AC34.
- **S35** — id 35 (L8). The asks units 50 and 53 filed move `memory/backlog/PLAY.md`, which stands
  re-rendered, and an ask naming a chain build leaves this run's packet current. Observed by AC35.

## 3. Non-goals (OUT)

- The six highs: units 54 to 59.
- Editing any landed spec's text, frozen at CLOSED, as §2's opening states.
- The spec lints the report suggests as gates over the set; the close's left-shift step
  (BUILD-METHOD M8) takes them.
- Re-pointing a fourth id reader beyond S14's conditional one.

### Edges

- **consumes-from** `TOOL-dTotalRecall-36` — the runlog self-test arm of its AC4, which S21 rewrites
- **consumes-from** `TOOL-dTotalRecall-43` — the `# slug-grammar: kept` lines S4 re-marks
- **consumes-from** `TOOL-dTotalRecall-44` — the shape-keyed split census and its AC2 sites (ids 20, 39)
- **consumes-from** `TOOL-dTotalRecall-45` — the three re-pointed readers and `render_spec_skeleton`'s
  re-point (ids 2, 10, 16, 17, 29, 42)
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
- **consumes-from** `TOOL-dTotalRecall-53` — the view's parity, the census marker, S20's govkit lines,
  S27's order line, S30's figure and its asks (ids 3, 5, 9, 11, 14, 21, 27, 33, 34, 35)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` and its refusals (ids 2, 18, 19)
- **consumes-from** `TOOL-dTotalRecall-55` — `CENSUS_KEPT_PATHS` and its reasons (ids 25, 44)
- **consumes-from** `TOOL-dTotalRecall-59` — the registration with `absorbs` cut (ids 6, 12)

## 4. Design

### How the batch builds

One pass, after every unit is terminal. The items share `record_causes.py`, `id_grammar.py`,
`gen_build_index.py` and the runlog kit, so their write sets intersect and BUILD-METHOD M6 keeps them
one unit. Within the pass the order is: the marker items S3 and S4 first, since S24 and S27 read the
marker; S20 before S11, since S11 counts what S20 leaves; then the code items in unit order; then the
prose and ledger items S29, S30, S32, S34 and S35.

### The govkit block of S23

```text
# govkit:generated begin
<one `<path> linguist-generated` line per `rendered` code row of an installed kit>
# govkit:generated end
```

`update` reads this span and the `govkit:lf-pins` span separately, each reporting `current` or its own
moved state, so an adopter applied at base reads `current` for its lf pins after upgrading.

### Inventory

Minted: `--build` on `record_causes.py --backfill`; the keyword `slug` of `render_spec_skeleton`; the
govkit block `govkit:generated`, its writer, update arm and receipt row; the `RECORD_SCHEMA` key
`cause_line`; the plants `cut-cause-line`, `range-served`, `other-build-causeless`, `reason-on-other-file`,
`split-maxsplit-two` and `rsplit-bare`. Naming cells: the govkit writer is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass, and a flagged name
takes the suggestion; flags, keys and plants have no cell.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`, `tools/memory-tree/gen_build_index.py`, `tools/memory-tree/record_causes.py`
- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/backlog.py`, `tools/memory-tree/row_grammar.py`
- `tools/branch-reconcile/branch_reconcile.py`
- `tools/runlog/record.py`, `tools/runlog/selftest.py`, `tools/runlog/README.md`
- `tools/govkit/govkit.py`, `tools/govkit/selftest.py`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/backlog/PLAY.md` (regenerated by `python tools/memory-tree/gen_build_index.py --write`)
- `memory/builds/*/README.md` (the `gen:build-order` region, regenerated by the same command)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Fold each minor into its unit's spec.** M4 refuses folding at the exit.
- **Split into two batches.** Both halves would regenerate `memory/map/generated/` with its generator,
  which M6 clause 3 forbids two concurrent passes to share, and the marker items are read by census
  items on both sides.
- **Write S23's lines inside the `govkit:lf-pins` block.** Every existing adopter would read
  `pins-moved` on unchanged pins (§8 F1).

## 5. Production-readiness checklist

- security — S13 narrows a write to one build's folder; S23 adds a block govkit already has the
  machinery to write; no other surface.
- perf / scale — S25 expands ranges a record already carries; S24 adds two shapes to one regex.
- error / empty / loading states — S8 refuses by `Problem`; S13 lists what it will not write; S19 reds a
  closed ask.
- observability — S13 prints the unwritten records; S23's receipt row names the block's state.
- risks — S24 lists new base hits, each re-pointed or marked in the pass; S14's re-point is
  conditional on the tip and recorded either way in the pass commit's `Decided:` trailer.
- testing — AC1 to AC35 by the pass; the arms of §7 at the close.
- migration — S23 adds a block on the adopter's next `govkit update`, and the lf-pins block is not
  rewritten; S31's schema key is additive.
- user docs — none under `help/`: S30's README is the runlog kit's own reference, not a help page.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/asbuilt_view.py --check` and the dClosedLoop `asbuilt.py
  --check` run at the tip, both exit 0. Red when: the view's bytes differ from its render.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 9` runs at the tip it exits 0,
  and `grep -c "Caused-by"` over the view prints `0`. Red when: a hand edit lands in the view.
- **AC3** — When `python id_grammar.py --readers` runs from `tools/memory-tree/` at the tip over a
  fixture holding one line marked `# census: kept slug-grammar x` and one marked
  `# slug-grammar: kept x`, it lists the second and not the first. Red when: the old spelling still
  exempts.
- **AC4** — When `git grep -n "# slug-grammar: kept" -- tools` runs at the tip, it prints nothing.
  Red when: a line keeps the old spelling.
- **AC5** — When `git grep -n "legacy-records" -- tools .memory-tree.conf memory/project` runs at the tip,
  it prints nothing. Red when: a carrier of the old name stays.
- **AC6** — When a `tomllib` probe reads `tools/memory-tree/kit.toml` at the tip, no `ledger` table has
  `population` `legacy-records`. Red when: the old registration survives.
- **AC7** — When `grep -n "def render_spec_skeleton"` and the eight call sites of S7 are read at the tip,
  the signature takes `slug` and every call passes it. Red when: a caller omits it, or the header
  splits `spec_id`.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --new-spec TOOL-x --tier 2` runs at the
  tip, it exits non-zero with a message naming `TOOL-x`. Red when: it raises a traceback or writes a file.
- **AC9** — When `python tools/memory-tree/gen_build_index.py --selftest` runs at the tip, its
  `render_spec_skeleton` cases pass with `ARCH-aFix-3`. Red when: a fixture call raises on the
  undeclared family.
- **AC10** — When `git log --format=%s` lists the pass commits at the tip, unit 54's precedes unit 45's,
  and `grep -c "TOOL-dTotalRecall-54"` over unit 45's §3 prints at least 1. Red when: unit 45 ran
  before the parser landed.
- **AC11** — When `python record_causes.py --fixture` runs from `tools/memory-tree/` and builds unit
  47's fixture and `--backfill` then `--check` run, `--check` names exactly the no-id record.
  Red when: it names the `.sh` record or none.
- **AC12** — When `git log --diff-filter=A` is read for each record unit 47's pass commit changed, each
  was added after unit 36's pass commit. Red when: a backfilled record predates unit 36's pass.
- **AC13** — When `record_causes.py --fixture --plant other-build-causeless` builds a fixture and
  `--backfill --build fixtureBuild` runs, the other build's record is listed and unchanged.
  Red when: the verb writes outside the named build.
- **AC14** — When the command of S14 runs in the flipped clone `TOOL-dTotalRecall-5` §4 makes, the spec
  it writes carries `node d` in its status header. Red when: it exits with the usage or id refusal.
  fixture: the scratch clone under `%TEMP%/<short>`; the pass makes it.
- **AC15** — When a `python -c` probe compares `parse_id_parts`' accepted families with
  `grammar_for(root).families` in a scratch tree declaring `RECALL_CITED_FAMILIES`, they are equal.
  Red when: a cited family is refused.
- **AC16** — When the probe calls `parse_id_parts("TOOL-001", ".")` and `parse_id_parts("TOOL-d119", ".")`,
  each raises `ValueError`. Red when: either returns a tuple.
- **AC17** — When the tip's `id_grammar.py --readers` runs in the scratch worktree of unit 44 AC2, each of
  the thirteen ledgered site texts is listed with its file. Red when: a site text is missing.
- **AC18** — When the counting command the ledger names for S18 runs at the tip, it prints the ledgered
  figure, and `git grep -nE "[0-9][0-9,]*[0-9] .?journal" -- tools memory/guides memory/HYGIENE.md`
  prints no hit without its command beside it. Red when: a figure ships with no command.
- **AC19** — When `record_causes.py --fixture --plant pinned-ask-closed` builds a fixture whose pinned
  row's ask is `WONTDO`, `--check` exits 1 naming the row. Red when: a closed ask keeps the row.
- **AC20** — When `--backfill` runs twice over a fixture `.sh` record, the record holds one
  `# **Caused-by:**` line and `bash -n` exits 0 on it. Red when: the line is bare, doubled or absent.
- **AC21** — When a `python -c` probe calls `check_cause_line` from `tools/runlog/record.py` on the plant
  `cut-cause-line`, it returns no finding; on a cause naming an unserved id it returns one.
  Red when: absence reds, or the old arm stands.
- **AC22** — When `bash skills/session-kickoff/manifest-check.sh` runs at the tip, it exits 0.
  Red when: the stamp is older than the last change to a watched file.
- **AC23** — When `python tools/govkit/govkit.py update` runs on a scratch adopter applied at base, the
  lf pins read `current` and `.gitattributes` gains the `govkit:generated` block naming the four
  renders. Red when: the lf pins read `pins-moved`.
  fixture: the scratch adopter under `%TEMP%/<short>`; the pass makes it.
- **AC24** — When `--readers` runs over the fixture with `split-maxsplit-two` and `rsplit-bare`, it lists
  both, and still not `x.rsplit("-", 1)[1]`. Red when: a maxsplit or rsplit reader is unlisted.
- **AC25** — When the probe calls `check_cause_line` on the plant `range-served`, serving `TOOL-x-1..3`,
  a cause of `TOOL-x-2` passes and `TOOL-x-4` returns one finding. Red when: the range is not expanded.
- **AC26** — When `record_causes.py --fixture --plant reason-on-other-file` builds a fixture keeping a
  second file with unit 49's reason, `--check` exits 1 naming it. Red when: the reason keeps it.
- **AC27** — When `--readers` runs over a scratch copy with the `[0]` exclusion removed, the two marked
  lines are unlisted and an unmarked index-0 plant is listed. Red when: the marker changes nothing.
- **AC28** — When a `python -c` probe calls `render_spec_skeleton` with `spec_id="TOOL-dFoo-3"` and
  `slug="xFoo"`, the header reads `node x`. Red when: it reads `node d`.
- **AC29** — When `grep -c "nine"` runs over this unit's acceptance ledger entry for S29, it prints at
  least 1. Red when: the count is not stated.
- **AC30** — When `grep -n "Caused-by" tools/runlog/README.md` runs at the tip, both paragraphs of S30
  print a line. Red when: either paragraph still describes the fixed head alone.
- **AC31** — When a probe reads `RECORD_SCHEMA["cause_line"]` from `tools/runlog/record.py`, it returns
  the cause-line pattern. Red when: the key is absent.
- **AC32** — When `git show` prints the memory-tree kit's `tree_lib.py` at revision `462d20f3` and
  `sed -n 410,412p` reads that output, it prints `BIND_RE`, the line the ledger cites. Red when: the cited lines hold something else.
- **AC33** — When `python tools/codebase-map/gen_map.py --check` runs at the tip, it exits 0.
  Red when: the symbols tier is stale.
- **AC34** — When `python tools/memory-tree/gen_build_index.py --check` runs at the tip it exits 0, and
  every README holding a `| Step | Units | Parallel |` table carries S27's line under it.
  Red when: a region is stale or the line is missing.
- **AC35** — When `gen_build_index.py --check` and the packet's `--check dTotalRecall` run at the tip,
  both exit 0. Red when: `memory/backlog/PLAY.md` or the packet is stale.

## 7. Gates

`memory hygiene` · `build-index selftest` · `tier2-review self-test` · `branch-reconcile selftest` · `runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC13 AC19 AC20 AC26 · the plants `other-build-causeless`, `pinned-ask-closed`, `reason-on-other-file` and a `.sh` record, staged by skipping each new test · none
New arm: tools/memory-tree/id_grammar.py · covers AC3 AC24 · the plants `split-maxsplit-two`, `rsplit-bare` and an old-spelling marker, staged by restoring the old shapes · none
New arm: tools/runlog/selftest.py · covers AC21 AC25 · unit 36's AC4 arm, moved to the narrowed rule, and the `range-served` plant, staged by a token compare · none
New arm: tools/govkit/selftest.py · covers AC23 · the apply-at-base, update-at-tip adopter, staged by writing the lines inside the lf-pins block · none

## 8. Open questions

- **F1 — Where do S23's `linguist-generated` lines go?** Options: (a) a block of their own,
  `govkit:generated`, with its writer, update arm and receipt row; (b) inside `govkit:lf-pins`, with
  the update comparison widened and an adopter migration stated. (b) flips every existing adopter to
  `pins-moved` on unchanged pins until the migration runs, which AC23 forbids; veto 1 discards it.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the only option surviving the vetoes.
  widens: none · relaxes: none
- **F2 — May S22 re-stamp `memory/guides/SESSION-KICKOFF.md`, a governance carrier?** Options: (a) yes,
  under the build's grant, the stamp following unit 52's edit of a watched file; (b) no, leaving the
  `kickoff-manifest ratchet` leg red from unit 52's pass to the close. (b) fails AC22. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 5, the README's `may:` grant, as `TOOL-dTotalRecall-43` §8 F3 used
  it. grants: PLAY-dClosedLoop-3 SESSION-KICKOFF.md's last-audit stamp follows unit 52's
  `.memory-tree.conf` edit · widens: none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of one unit's clause, which would split a clause that unit carries whole. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, its 35
  minors batched (26 MEDIUM, 9 LOW).

## 10. Reuse audit

Each item extends the seam its finding names, cited in the item: unit 44's `--readers` predicate,
unit 47's `write_missing_causes` with `tree_lib.BIND_RE`'s captured prefix (`tools/memory-tree/tree_lib.py:410`),
`backlog.check_hold_live` (`tools/memory-tree/backlog.py:878`), `check_serves_line`'s range expansion
(`tools/runlog/record.py:1461`), govkit's `lf_pin_block` (`tools/govkit/govkit.py:5845`) as the shape of
S23's sibling block, and `cmd_new_spec`'s parsed slug (`gen_build_index.py:8594`). S23's block is the
one new mechanism. `python tools/codebase-map/reuse_lookup.py "write a cause line into a record head after its binding line"`
ranked name-stem neighbours and no seam these items bypass.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
