# TOOL-dTotalRecall-70 — the round-5 minors: each criterion that observed nothing is observed at the tip, and each gap it hid in units 61 to 66 is closed

**Status:** CLOSED · rev-4 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 33 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-70-deviation-701.md](../build/2026-10-26-build-TOOL-dTotalRecall-70-deviation-701.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-70-deviation-702.md](../build/2026-10-26-build-TOOL-dTotalRecall-70-deviation-702.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-70-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-70-1-acceptance-ledger.md) | log | — |
| [2026-11-05-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-11 TOOL-dTotalRecall-19 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-43 TOOL-dTotalRecall-50 TOOL-dTotalRecall-61 TOOL-dTotalRecall-89 |
| [2026-11-24-prompt-TOOL-dTotalRecall-70-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-70-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-70-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-70-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-70-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-70-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 61 to 66
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md`)
exited CONVERGED with 28 confirmed findings. Its three highs are units 67 to 69: id 1 is
`TOOL-dTotalRecall-67`, id 16 is `TOOL-dTotalRecall-68` and id 21 is `TOOL-dTotalRecall-69`. This
unit is the batch BUILD-METHOD M4 makes of the rest:

- the 23 MEDIUM findings, ids 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 17, 18, 22, 24, 25, 26, 27, 28,
  29, 30, 31 and 32 (items M1 to M17);
- the 2 LOW findings, ids 8 and 33 (items L1 and L2).

Each keeps its report id and its own scope item. The minors land on units 61 to 66, so this unit
repairs none in particular and builds after every unit: order 33, above the 32 that units 66, 68
and 69 hold. The review record holds each item's text.

Several ids share an item, and so a defect. Ids 2, 9 and 31 are M1. Ids 4, 13, 17 and 28 are M2.
Ids 3 and 22 are M3. M1 is H1's defect at MEDIUM, extended to units 62, 63 and 64. Unit 67 closes
H1's half, and S3 here re-reads it at the tip. M2's row grammar is settled by unit 68's factory
grammar, so its items state that grammar and plant what it must refuse.

Re-grounded at `c0a707782`, over `TOOL-dTotalRecall-68` rev-3 and `TOOL-dTotalRecall-66` rev-5, whose passes precede
this one. Built here: the plants of S4, S5 and S11, S8's marker remedy, S11's two refusals, S12 and S14's record.
S21 is cut with its reason. Every other item holds, is a ledger line, and keeps its criterion as a check.

## 2. Scope (IN)

Every item states its change to the unit it lands on, as that unit was built. A landed spec is
frozen and is not edited. An item whose unit's criterion observed nothing therefore makes the
observation at the tip. Where that observation is red, the item repairs the code, or writes a
deviation record when the departure is in a spec. "The registry" is
`memory/project/census-kept-paths.txt`, a ledger home in the factory grammar after `TOOL-dTotalRecall-68`, and "the
reader" is `tree_lib.py#read_kept_rows(census, root)`, its rows read by named field. "pass(N)" is the
first line of `git log --reverse --format=%H --grep='^Pass: TOOL-dTotalRecall-N$' 462d20f3..HEAD`.
"The probe" is §4's blob probe.

- **S1** — id 2 (M1). Unit 62's AC3 grep for `absorbs` certified nothing, over `tools/memory-tree/kit.toml`
  as audited and over `tools/govkit/registry.toml` as its rev-3 spells it, because the field existed at no step.
  This unit's ledger records that grep as void. The absence it claimed is held by unit 66's AC5. Unit
  59's own pass is read for the stale text's consequence, a cut of a field that does not exist: pass(59)'s
  diff carries no minus line spelling `absorbs`. Holds. Observed by AC1.
- **S2** — id 9 (M1). The §9 halves of units 62, 63 and 64's AC1 are re-read in the amendment's own
  form, which no edge-fold line matches. The text read is each target spec as it stood at its own
  unit's pass, `git show pass(T)^:<spec path>`. The forms are `amended by TOOL-dTotalRecall-62` in
  units 52 and 59, `added by TOOL-dTotalRecall-63` in unit 46 and `amended by TOOL-dTotalRecall-64`
  in unit 46. Holds. Observed by AC1.
- **S3** — id 31 (M1). The content halves are re-read the same way, by the strings of §4's table, for
  units 46, 52, 55, 56, 57 and 59. A target that built from text without its amendment gets a
  deviation record of that unit, and the code the amendment governs is read by the criterion the
  amendment carried. Each row reads its wanted count, so no such record is owed. Observed by AC1.
- **S4** — id 4 (M2). The registry's row grammar is the factory's: TAB-separated, one field per
  column, never a whitespace split. The plant `kept-row-multiword` holds a reason of several words,
  `outside the write set`, on a plain keep, and one of several words on a pinned writer's row. `--check` prints
  the first whole on the keep's line, and the reader answers the second whole in the row's `reason` field, the
  pinned row's lines naming its ask (§8 F4). Observed by AC2.
- **S5** — id 13 (M2). A row is told apart by its named fields, never by its field count. A row
  whose field count is not the registration's seven is a red finding naming its line, the factory's
  refusal as unit 68's reader raises it. The plant `kept-row-arity` arms it, one row of four fields and one of
  six. Observed by AC2.
- **S6** — id 17 (M2). The reader is the factory's `read_rows`, never a hand parser of
  `transition_audit.py#read_registry`'s shape. Unit 68's AC3 source probe is re-read at the tip. Observed by
  AC2.
- **S7** — id 28 (M2). Unit 65's error state "fewer than three fields" gives way to S5's rule, unit 68's,
  and a reason of several words survives both the plain-keep read and the pinned-writer read. Observed by
  AC2.
- **S8** — id 3 (M3). The two messages name the registry, never the constant. Unit 57's domain refusal does since
  unit 65. Unit 58's marker remedy, `id_grammar.py#check_marker_domain`, still reads "kept by its path-keyed
  row", and this pass makes it read "kept by a row of `<memory root>/project/census-kept-paths.txt`" (§4). The
  domain loop reads the registry's rows, as unit 65 left it. Observed by AC3.
  **Readers:** by name: READER NOT IN TREE — `CENSUS_KEPT_PATHS` is absent from `tools` since
  `TOOL-dTotalRecall-65` · by value: the reader's domain refusal, and the marker remedy that
  `check_cause_writers` and `check_alias_compares` print through `check_marker_domain`, which this item points at
  the registry.
- **S9** — id 22 (M3). Done by units 65 and 68 for `kept-row-editable` and `kept-row-drained`, whose rows the
  factory writes into the fixture's registry. `unkept-build-alias` holds a hit under no row and its fixture no registry, so it
  reads no table either. Each stages its own red. Observed by AC3.
- **S10** — id 18 (M4). One keep home and one accessor stand at the tip. Unit 57's criterion that
  probed the engine's table is re-read over the registry's rows: every row's path matches
  `build_kept_path_re(memory_root)` (`TOOL-dTotalRecall-66` §4). Observed by AC3.
- **S11** — id 29 (M5). The census column's domain is `check_cause_writers` or
  `check_alias_compares`, and any other value is a red finding naming its line. A `(census, path)`
  pair held by two rows is red too, even when their reasons differ, which the factory's whole-key
  uniqueness does not catch. These are the plants `kept-row-unknown-census` and `kept-row-duplicate`.
  Observed by AC4.
- **S12** — id 24 (M6). Hygiene check 3 admits `census-kept-paths.txt` by name, as it admits
  `pass-order-waiver.txt`, because the engine reads it at its default path. The kit README says
  where a keep row goes. The engine file is watched, so this pass's commit re-stamps `last-audit` under
  §8 F2. Observed by AC5.
- **S13** — id 30 (M7). The engine ships no build-folder path of this repository in any module.
  For every slug with a tracked build-folder `.py` file, no code file of `tools/memory-tree` spells one of its
  build-folder paths outside the self-tests (§8 F6). A literal found there moves to the registry. At this re-ground
  one code line does, `record_causes.py#CLOSED_LOOP`, which unit 66 S36 takes out. Observed by AC6.
- **S14** — id 5 (M8). Unit 64 rev-3 left unit 38's CLOSED spec frozen (its §8 F2), so unit 38's
  hands-off to unit 46, "whose body that unit rebuilds on `tree_lib.build_id_token_re`", stands against a tree where
  unit 54 built that body and unit 46 observed it. That is the departure. This unit writes
  its deviation record, of unit 38, through `gov_record.py new deviation`, its approver `author-recorded`, its
  cause the review finding, naming pass(64), the commit that settled it, and the hand-off line. Observed by AC7.
- **S15** — id 10 (M9). Unit 64's AC1 edge alternative is re-read over joined text:
  `whose body this unit rebuilds` in unit 46's spec at pass(46)^. Holds. Observed by AC8.
- **S16** — id 14 (M10). Unit 46's Goal, "This unit rebuilds the parser on that regex", is read at
  pass(46)^, and the body unit 46 left is compared with unit 54's by S17's probe. Both hold, so no repair is
  owed. The compare reads pass(46), never the tip, where unit 66 S35 has changed the function by design.
  Observed by AC8.
- **S17** — id 32 (M11). The body compare covers both names unit 54 mints: the `parse_id_parts`
  segment and the module-level `SUFFIX_RE` assignment, each equal to pass(54)'s at pass(46). `id_grammar.py`
  assigns `SUFFIX_RE` once there and at the tip. Observed by AC8.
- **S18** — id 11 (M12). Every compare against a blob reads both sides as text with universal
  newlines. Each revision is spelled `<sha>:./<file>` from the file's directory, or by its
  repository-root path. That covers S17's probe, and unit 66 rev-5's AC14 and AC22, which spell both.
  Observed by AC8 and AC9.
- **S19** — id 12 (M13). Every build-order check reads ancestry, never `git log` output order. The
  pairs are pass(56) before pass(57) (unit 61's AC3), pass(54) before pass(46) (unit 63's AC2) and
  pass(54) before pass(45) (unit 66's AC23). Holds. Observed by AC10.
- **S20** — id 6 (M14). S34 of unit 66 is observed where its fixtures live. Unit 59's plant
  `merged-home-gained` sits in section `2o` of `tools/lib/resolve-python.test.sh`, whose directory is the suite's own
  `mktemp -d`. Unit 60's AC14 ran in a clone under the system temp directory, as its ledger says, and its AC23 has
  no fixture. No Python fixture function is left to read. Observed by AC11.
- **S21** — id 25 (M15). Cut: the tree holds no `govkit:generated` block, since unit 60 rev-3 F4 cut it to ride owner ask
  TOOL-dTotalRecall-109 with the held `TOOL-dTotalRecall-37`, and unit 66 F4 cut its sites after it. The rollback
  snapshot, its two restores, the role tables and the runbook text ride that ask (§8 F5). Observed by AC12.
- **S22** — id 26 (M16). Done by unit 66 S36 and S1: the plants `pinned-writer-drained` and `departures-pinned`
  stage a registry row whose `records` field is a glob and whose disposition is `keep:<ask>`,
  `--cause-writers` prints `deviations.py` with its pinned disposition from that row, and the census-keyed
  drain covers it beside unit 50 S2's ask rule. Observed by AC13.
  **Readers:** by name: READER NOT IN TREE — `CAUSE_WRITER_PINNED` leaves `tools` with
  `TOOL-dTotalRecall-66`, before this pass · by value: unit 50's two
  plants, the `--cause-writers` disposition lines and unit 66 S1's drain, each read here from the
  registry row.
- **S23** — id 27 (M17). Unit 66's AC22 is read where a ledger line can be. The grep runs over
  unit 60's acceptance ledger alone, and needs one line carrying both
  `tools/memory-tree/tree_lib.py@462d20f3:410-412` and `:421`. Holds. Observed by AC9.
- **S24** — id 8 (L1). The alias census is observed by its own function. `record_kinds.py#check_alias_compares`
  lists one line naming both `deviations.py` at its line 380 and `kept pinned instrument`. That is the reading
  unit 65's AC2 and unit 61's AC2 meant. Observed by AC14.
- **S25** — id 33 (L2). Unit 63's cited-family case is re-run at the tip with its conf spelled
  whole: `MEMORY_ROOT=memory`, `FAMILIES="tooling:TOOL"` and `RECALL_CITED_FAMILIES="ZED"`. A
  `ConfError` from that tree is a fixture fault, never a pass. Observed by AC15.

## 3. Non-goals (OUT)

- The three highs: units 67, 68 and 69.
- Editing a landed spec's text, frozen once its unit builds, as §2's opening states.
- The registry's registration, its base compare and the reader's path against its home: units 68 and 73.
- `last-body-change`, which the manifest check's age arm reads: `TOOL-dTotalRecall-75`'s.
- The `PROJECT_REGISTRY_EXTRA` entry unit 65 wrote, which S12 leaves: `TOOL-dTotalRecall-76`'s.
- The spec lints and checklist entries the report suggests as gates. The close's left-shift step
  (BUILD-METHOD M8) takes them.
- `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`, for S12 (§4, "Alternatives
  rejected").

### Edges

- **consumes-from** `TOOL-dTotalRecall-61` — its AC2 and AC3 as built, re-read by their own commands and by ancestry (ids 8, 12)
- **consumes-from** `TOOL-dTotalRecall-62` — its amendments to units 52 and 59 and its AC3, re-read at the tip (ids 2, 9, 31)
- **consumes-from** `TOOL-dTotalRecall-63` — its amendment to unit 46 and its AC2, re-read with the conf spelled whole and by ancestry (ids 9, 12, 31, 33)
- **consumes-from** `TOOL-dTotalRecall-64` — its amendment to unit 46, unit 38's frozen line, and its AC1 and AC2, re-read over joined text and both segments (ids 5, 9, 10, 11, 14, 31, 32)
- **consumes-from** `TOOL-dTotalRecall-65` — the registry, its by-value carriers, the engine's literals and check 3's admission (ids 3, 4, 8, 13, 17, 18, 22, 24, 28, 29, 30)
- **consumes-from** `TOOL-dTotalRecall-66` — S18's attributes sites, cut there, S34's fixtures, S36's pinned row, `build_kept_path_re` and AC14, AC22, AC23 and AC28 (ids 6, 11, 12, 18, 25, 26, 27, 30)
- **consumes-from** `TOOL-dTotalRecall-67` — the strings of its §4 table, re-read at the tip against the text units 55, 56 and 57 built from (id 31)
- **consumes-from** `TOOL-dTotalRecall-68` — the factory row grammar of the registry, `read_kept_rows` over `read_rows`, and its `records` and `keep:` fields (ids 4, 13, 17, 26, 28, 29)
- **hands-off** `TOOL-dTotalRecall-74` — its pass and its AC1 and AC8 ledger lines, whose backticked strings that unit re-reads by a probe no shell quotes at step 34 (the round-1 audit of units 67 to 70, id 11)
- **hands-off** `TOOL-dTotalRecall-76` — its §4 table and AC8 readings, its AC7 and S14 record, its messages, its fixture sweep, its check-3 admission and its S12 re-stamp, re-read or repaired by that batch (the round-1 audit of units 67 to 70, ids 2, 3, 4, 15, 18, 25, 30)
- **hands-off** `TOOL-dTotalRecall-88` — its four kept-row plants, its S8 message and its check-3 case, rebuilt on that batch's fixture base, read at step 33 and named as the one second spelling (the round-1 audit of units 71 to 76, ids 3, 25, 26, 27, 43)

## 4. Design

### How the batch builds

One pass, after units 66, 68 and 69. The items share `tree_lib.py` and `record_causes.py`, and every half would
regenerate `memory/map/generated/` with its generator. So BUILD-METHOD M6 keeps them one unit.
`TOOL-dTotalRecall-73` writes those two modules and `TOOL-dTotalRecall-75` writes
`memory/guides/SESSION-KICKOFF.md` at this step, so the three passes run in sequence, in any order. Inside the pass
the order is:

1. The read-only items: S1 to S3, S6, S7, S9, S10, S13, S15 to S25. Each red they find decides a repair below.
2. S11, then the plants of S4, S5 and S11.
3. S8's message.
4. S12 and its re-stamp, in the same commit as the pass.
5. S14's deviation record and the ledger lines.

### The blob probe

It runs from `memory/builds/dTotalRecall/spec/`. The heredoc's delimiter is quoted, so no shell expands a backtick in a
string. `check=True` makes a failed `git show` a red, never a 0. The text is joined, so a wrapped phrase counts.

```bash
REV=<revision> N=<unit number> python - <<'PROBE'
import os, re, subprocess
STRINGS = ["<string>", "<string>"]
raw = subprocess.run(["git", "show", os.environ["REV"] + ":./2026-10-26-spec-TOOL-dTotalRecall-%s.md" % os.environ["N"]],
                     capture_output=True, check=True).stdout.decode("utf-8")
text = re.sub(r"\s+", " ", raw)
for s in STRINGS:
    print(text.count(s), s)
PROBE
```

The passes it reads, DERIVED 2026-11-24 by §2's command: pass(38) `2f59e5acb`, pass(45) `c6fcf603b`,
pass(46) `63f283ddd`, pass(52) `926526b1c`, pass(54) `74af3faa4`, pass(55) `5b5895a49`, pass(56) `798f98fc1`,
pass(57) `5ff76c2e2`, pass(59) `47afc8937` and pass(64) `86360f071`.

### The amendment strings of S2 and S3

Each string is counted over T's spec at pass(T)^. A string marked "1" must print at least 1. A string marked "0" must
print 0.

| T | Amending unit | String | Wanted |
|---|---|---|---|
| 52 | 62 | `no base re-key is built` | 1 |
| 59 | 62 | ``` `absorbs` is absent ``` | 1 |
| 59 | 62 | `it replaces unit 52's absorbed-population arm` | 0 |
| 46 | 63 | `ZED-aFoo-2` | 1 |
| 46 | 64 | `This unit's pass builds no body and observes that one` | 1 |
| 46 | 64 | `whose body unit 54 builds and this unit's criteria observe` | 1 |
| 46 | 64 | `whose body this unit rebuilds` | 0 |
| 55 | 61 | ``` The eight rows move out of `CAUSE_WRITER_KEPT` ``` | 1 |
| 56 | 61 | ``` The row moves out of `ALIAS_COMPARE_KEPT` ``` | 1 |
| 57 | 61 | `this one follows units 55 and 56` | 1 |

PINNED 2026-11-24 at `c0a707782`, by this probe: each "1" string prints 0 over its target at `653bed738` and at least 1 over
its amending spec, and each "0" string prints 1 over its target at `653bed738`, so each row can read
either value. At pass(T)^ each row prints its wanted count, and each §9 form of S2 prints 1. Three strings rev-3
pinned are replaced: unit 62 rev-3 spells no `first seed record-kinds-legacy`, and the re-grounds of units 55 and 56
re-worded unit 61's sentence and kept what it says. `rebuilds the parser on that regex` (S16) and
``Minted: `SUFFIX_RE` `` (S17) print 1 over unit 46's spec at `653bed738` and 0 at pass(46)^.

### The body compare of S16 to S18

```bash
# run from tools/memory-tree/
python -c "import ast,subprocess,sys
def segs(rev):
    src = subprocess.run(['git', 'show', rev + ':./id_grammar.py'], capture_output=True, check=True).stdout.decode('utf-8').replace('\r\n', '\n')
    t = ast.parse(src); out = {}
    for n in t.body:
        if isinstance(n, ast.FunctionDef) and n.name == 'parse_id_parts': out['parse_id_parts'] = ast.get_source_segment(src, n)
        if isinstance(n, ast.Assign) and any(getattr(x, 'id', '') == 'SUFFIX_RE' for x in n.targets): out.setdefault('SUFFIX_RE', []).append(ast.get_source_segment(src, n))
    return out
a, b = segs(sys.argv[1]), segs(sys.argv[2])
print(a == b, len(b.get('SUFFIX_RE', [])))" <pass(54)> <pass(46)>
```

It prints `True 1` when unit 46 left unit 54's body and one `SUFFIX_RE` assignment, as at this re-ground (DERIVED
2026-11-24). Both sides are blobs, so no checkout's line endings enter it.

### The registry rules of S5 and S11

The factory returns a malformed row, and unit 68's reader refuses it by line. After that refusal, and whatever census
was asked, the reader refuses the two S11 names, each finding carrying the row's line, which `read_rows` gives beside
its values:

```python
KEPT_CENSUSES = ("check_cause_writers", "check_alias_compares")   # beside KEPT_FIELDS
...
    first, bad = {}, []
    for key, (_n, _tail, line, _row) in rows.items():
        census_, path = key[:2]
        if census_ not in KEPT_CENSUSES:
            bad.append(f"line {line}: census {census_!r} is none of {', '.join(KEPT_CENSUSES)}")
        at = first.setdefault((census_, path), line)
        if at != line:
            bad.append(f"line {line}: a second row for {census_} {path}, the first at line {at}")
    if bad:
        raise ValueError(f"{CENSUS_KEPT_REGISTRY}: " + "; ".join(bad))
```

Each census appends that one `ValueError` to its reds and reads every hit unkept, unit 57's catch unchanged, so
`record_causes.py --check` and `record_kinds.py --check` both print it. `run_fixture`'s `adopter-no-registry` arm
reads `KEPT_CENSUSES` in place of its own tuple of the two names.

### The plants

Each is a case of `record_causes.py --fixture`, writes the fixture's registry, and prints `--check`'s lines.

- `kept-row-multiword` joins `PINNED_PLANTS`, so it has a pinned writer's row as unit 66 leaves it, with a reason of
  several words, beside `KEPT_SCRIPT` spelling its hit under a plain keep. It passes, exit 0, when `--check` exits 0, its
  keep line ends `kept outside the write set`, and `read_kept_path` answers the pinned row's `reason` whole.
- `kept-row-arity` appends two raw rows to the header the factory writes, one of four TAB fields and one of six, both naming
  `KEPT_SCRIPT`, which spells no Serves literal. It exits 1 with one red naming the registry, `line 2` and `line 3`.
- `kept-row-unknown-census` writes one row of census `check_cause_writer` for that same script. It exits 1 with one red
  naming the registry and `line 2`.
- `kept-row-duplicate` writes two rows of one `(census, path)` pair and different reasons for `KEPT_SCRIPT` spelling its
  hit. It exits 1 with two reds, the registry's naming both lines, and the hit read unkept.

With its refusal staged off, each of the last three exits 0.

### S8's message

`check_marker_domain(path, text, census)` keeps its signature. Its finding ends "a build folder's script is kept by a row of
`<memory root>/project/<registry>`, since its bytes are not this build's". The memory root is what stands before
`path`'s last four segments, `builds/<slug>/build/<file>`, the one shape both walks' globs match
(`record_kinds.py#read_tracked`: `*` crosses no `/`). The file name is `tree_lib.CENSUS_KEPT_REGISTRY`, reached by
`id_grammar.py#load_sibling`, so no message site spells it.

### S12's admission

In check 3 of `tools/memory-tree/check-memory-hygiene.sh`, a case `F:census-kept-paths.txt) ;;`
sits beside `F:role-stand-in-waiver.txt`, above the `PROJECT_REGISTRY_EXTRA` case. Its
comment names the reason those two give: a kit reads the file at its default path. The README's
sentence "A registry a KIT ships, such as `pass-order-waiver.txt`, is admitted by name." names this registry beside it. A
new paragraph there says that an adopter keeps a census hit in a file of its own build folders by a row
of that file, in the factory's seven-field grammar. The decisions `TOOL-bQuiltedLantern-3` and
`TOOL-aRepatriatedFork-10` S4 rule this route. The manifest's `watch:` line lists the engine file and not the README.
The pre-commit hook's staged arm refuses the engine edit without a changed `last-audit`, so both are in one commit,
after a re-read of the claims the manifest draws from that file. The kit version's bump is the lander's.

### Inventory

Minted: the constant `KEPT_CENSUSES` in `tree_lib.py`; the fixture plants `kept-row-multiword`, `kept-row-arity`,
`kept-row-unknown-census` and `kept-row-duplicate`; the check-3 case `F:census-kept-paths.txt`;
a deviation record of `TOOL-dTotalRecall-38`. Naming cell: none, no function minted.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/record_kinds.py` (the docstrings that state what the registry's refusal covers)
- `tools/memory-tree/id_grammar.py` (S8)
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`, `tools/memory-tree/README.md`
- `memory/guides/SESSION-KICKOFF.md` (the `last-audit` re-stamp)
- `memory/builds/dTotalRecall/build/` (S14's deviation record and this unit's ledger lines)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **S12 by documentation alone**, declaring the name in each adopter's `PROJECT_REGISTRY_EXTRA`.
  An adopter who writes the file as told is red until it finds the note. The decision
  `TOOL-bQuiltedLantern-3` places a registry a kit relies on in the kit's whitelist instead.
- **A bullet in `memory/HYGIENE.md` and its template beside `pass-order-waiver.txt`.** That file is
  a governance carrier, and the README's grant reaches only the stamp precedent `TOOL-dTotalRecall-60`
  §8 F2 set. The kit README is the document an engine adopter reads, and its by-name sentence
  already stands.
- **Two batches.** S4, S5 and S11 write `record_causes.py` and S11 writes `tree_lib.py` with them. No split
  leaves two disjoint write sets under M6's clauses.
- **Hand `check_marker_domain` the registry's path.** A fourth argument at both callers carries what `path` already says.

## 5. Production-readiness checklist

- security — no new write surface. Check 3 admits one more name under `<MEMORY_ROOT>/project/`, a
  file the engine already reads (unit 65).
- perf / scale — reads and plants only. The body compare reads two blobs.
- error / empty / loading states — each registry refusal is a red finding naming its line, and the walk reads every
  hit unkept. A `ConfError` from S25's tree is a fixture fault.
- observability — each re-read writes its count or verdict into this unit's ledger line. A void
  criterion is recorded as void.
- risks — S12 changes an adopter's check 3. It admits a name and refuses nothing it admitted before. S11 refuses rows
  an adopter's registry could hold; no adopter holds one, the registry having never left this run branch.
- testing — AC1 to AC15 by the pass; the arms of §7 at the close.
- migration — none: gov's rows name the two censuses and each pair once.
- user docs — none under `help/`; S12's text is in the kit README.

## 6. Acceptance criteria

Where a criterion reads "as at HEAD", the pass observes it and builds nothing for it. Fixture commands run from
`tools/memory-tree/`.

- **AC1** — When §4's probe runs at pass(T)^ for each row of §4's table, each
  prints the wanted count, and the §9 forms of S2 print at least 1 in their targets, as at HEAD.
  `git show pass(59) -- tools | grep -c "^-.*absorbs"` prints 0, as at HEAD.
  Red when: a unit built from text its amending unit had not written, and no deviation record names
  it.
  figure: the counts are PINNED in §4; the pass's own counts are DERIVED by it.
- **AC2** — When `python record_causes.py --fixture --plant kept-row-multiword` runs, it prints its `PASS` line and
  exits 0, its keep line ending `kept outside the write set`. `--plant kept-row-arity` exits 1 with one
  `record causes: RED ` line naming `census-kept-paths.txt`, `line 2` and `line 3`. At the tip,
  `python -c "import inspect, tree_lib; s = inspect.getsource(tree_lib.read_kept_rows); print('read_rows' in s, '.split(' in s)"`
  prints `True False`.
  Red when: a reason is cut at a space, or a row of the wrong arity is read.
- **AC3** — When a `python -c` probe calls `id_grammar.check_marker_domain` from `tools/memory-tree/` at the tip, its path a
  script of one build folder under the memory root `docs/memory`, its text a line carrying the `cause-writer` marker and
  its census `cause-writer`, the finding names the registry's file under
  `docs/memory/project/`, and `python -c "import inspect, id_grammar; s = inspect.getsource(id_grammar.check_marker_domain); print('CENSUS_KEPT_REGISTRY' in s, 'census-kept' in s)"`
  prints `True False`. `python record_kinds.py --fixture --plant marker-in-kept-script` prints `PASS` and a `RED` line naming
  the registry's file under `memory/project/`. `git grep -n CENSUS_KEPT_PATHS -- tools`, run from the repository root,
  prints nothing, as at HEAD. `python record_causes.py --fixture --plant kept-row-editable` and
  `--plant kept-row-drained` each exit 1 with one red naming the registry, and
  `python record_kinds.py --fixture --plant unkept-build-alias` exits 1 with one, as at HEAD.
  `python -c "import tree_lib; r = tree_lib.build_kept_path_re('memory'); print([bool(r.fullmatch(p)) for c in tree_lib.KEPT_CENSUSES for p in tree_lib.read_kept_rows(c, '../..')])"`
  prints no `False` and is not empty.
  Red when: a message names a table no tree holds, a plant stages nothing, or a row names an editable
  file.
- **AC4** — When `python record_causes.py --fixture --plant kept-row-unknown-census` runs, it exits 1 with one
  `record causes: RED ` line naming `census-kept-paths.txt` and `line 2`. `--plant kept-row-duplicate` exits 1
  with two, one naming `census-kept-paths.txt`, `line 3` and `line 2`.
  Red when: a mistyped census or a second row for one pair is read silently.
- **AC5** — When a scratch script runs the lines of `tools/memory-tree/check-memory-hygiene.sh` from `bp=$(` to the first
  `esac; done)`, with `M=memory`, an empty `PROJECT_REGISTRY_EXTRA` and `p1` holding
  `F:census-kept-paths.txt` and `F:census-kept-pathz.txt`, it prints the second name alone; at HEAD it prints both
  (DERIVED 2026-11-24). `grep -c census-kept-paths.txt README.md` run from `tools/memory-tree/` prints at least 1. At
  the tip `git merge-base --is-ancestor <W> <S>` exits 0, W being
  `git rev-list -1 HEAD -- <each path of the watch: line>` and S
  `git log -1 --format=%H -G"^last-audit:" -- memory/guides/SESSION-KICKOFF.md`.
  Red when: an adopter's registry reds check 3, or the watched edit has no re-stamp with or after it.
  fixture: the script under the run's scratch directory; the pass makes it.
- **AC6** — When, for each slug S that `git ls-files 'memory/builds/*/build/*.py' | cut -d/ -f3 | sort -u`
  prints, `git grep -nF "memory/builds/$S/build/" -- 'tools/memory-tree/*.py' 'tools/memory-tree/*.sh' 'tools/memory-tree/*.js' ':!*selftest*' ':!*.test.*'`
  runs at the tip, it prints nothing.
  Red when: an engine module ships a build-folder path of this repository.
  figure: one line at `c0a707782`, `record_causes.py#CLOSED_LOOP`'s, over 15 slugs (DERIVED 2026-11-24, that command).
- **AC7** — When `git diff -U0 pass(38) HEAD -- memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-38.md`
  runs, every line it adds or drops is a row of the `gen:spec-records` region, as at HEAD, and
  `git show --stat pass(64)` lists no such path. `git grep -l "86360f071" -- 'memory/builds/dTotalRecall/build/*TOOL-dTotalRecall-38-deviation-*.md'`
  prints the record this pass writes, whose Evidence names pass(64) and whose Departs from names
  unit 38's hands-off to unit 46.
  Red when: unit 38's spec moved after its pass outside its records region, or no deviation record names the hand-off
  that unit 46 did not take.
- **AC8** — When §4's body compare runs with pass(54) and pass(46), it prints `True 1`, as at HEAD, and
  `grep -c "^SUFFIX_RE = " id_grammar.py` run from `tools/memory-tree/` at the tip prints `1`.
  The probe over unit 46's spec at pass(46)^ prints 0 for `whose body this unit rebuilds`, and the
  ledger records the counts of `rebuilds the parser on that regex` and ``Minted: `SUFFIX_RE` `` there.
  Red when: unit 46's pass rebuilt either name, or `SUFFIX_RE` is bound twice.
- **AC9** — When `git grep -n -e "tree_lib.py@462d20f3:410-412" --and -e ":421" -- 2026-11-24-build-TOOL-dTotalRecall-60-1-acceptance-ledger.md`
  runs from `memory/builds/dTotalRecall/build/`, it prints one line, as at HEAD, and `git show 462d20f3` of `tree_lib.py`, the
  revision spelled with `:./`, run from
  `tools/memory-tree/` and read as text, holds `BIND_RE` and `def record_paths` at those lines. Unit
  66's AC14 compare, re-run from `memory/project/` against `legacy-records.txt` at unit 51's pass `30d1901d6`,
  prints no key that revision lacked.
  Red when: the ledger file prints no such line, or a compare reads a path git cannot resolve.
- **AC10** — When `git merge-base --is-ancestor` runs at the tip on the pairs pass(56) and pass(57),
  pass(54) and pass(46), and pass(54) and pass(45), each exits 0, as at HEAD.
  Red when: a unit built before the unit it reads.
- **AC11** — When a `python -c` probe reads the file S20 names and prints whether it holds
  `TMP=$(mktemp -d)` and `LL="$TMP/ll"` and, after them, `2o merged-home-gained`, it prints `True`, as at HEAD; over a
  scratch copy whose `LL=` line is a literal scratch path it prints `False`.
  `grep -c "built under the system temp directory" 2026-11-24-build-TOOL-dTotalRecall-60-1-acceptance-ledger.md`, run from
  `memory/builds/dTotalRecall/build/`, prints at least 1.
  Red when: a fixture is made at a fixed path.
  fixture: the copy under the run's scratch directory; the pass makes it.
- **AC12** — When `git grep -n "govkit:generated" -- tools .gitattributes WIRE-INTO-PROJECT.md` runs at the tip it prints
  nothing, and `grep -c 'GA_BLOCK_ID = ' govkit.py` run from `tools/govkit/` prints `1`, as at HEAD.
  Red when: a second block lands with a rollback that restores one.
- **AC13** — When `python record_causes.py --cause-writers` runs from `tools/memory-tree/` at the
  tip, it prints `deviations.py` with its pinned disposition and the ask of its row.
  `--fixture --plant pinned-writer-drained` and `--plant departures-pinned` each print `PASS` over
  a registry row, and `git grep -n CAUSE_WRITER_PINNED -- tools` prints nothing.
  Red when: a reader of the pinned row reads no row, or stages nothing.
- **AC14** — When `python -c "import record_kinds as k; print(*k.check_alias_compares('../..', 'tools')[0], sep='\n')"`
  runs from `tools/memory-tree/` at the tip, one line carries both the departures instrument's path with its line 380
  and `kept pinned instrument`, as at HEAD.
  Red when: the alias census keeps the compare by no row, or prints the reason cut.
- **AC15** — When a `python -c` probe calls `parse_id_parts("ZED-aFoo-2", tree)`, in a
  `tempfile.TemporaryDirectory()` tree whose `.memory-tree.conf` is S25's three keys, it prints
  `('ZED', 'aFoo', 2)`, as at HEAD.
  Red when: the call raises `ValueError`. A `ConfError` is a fixture fault and is fixed, never
  passed.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `record-kinds` · `record causes (causes and orphans over the legacy population)` · `memory-recall kit selftest` · `kickoff-manifest ratchet` · `branch-guard self-test` · `kit/dogfood doc parity` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC4 · the plants `kept-row-multiword`, `kept-row-arity`, `kept-row-unknown-census` and `kept-row-duplicate`, staged by splitting the reason at a space and by skipping each refusal · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC3 · a hit on the remedy's registry path in the `marker-in-build-script` arm, staged by the old remedy text · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 · `census-kept-paths.txt` planted with no `PROJECT_REGISTRY_EXTRA` beside `pass-order-waiver.txt`, staged by deleting the check-3 case · none

## 8. Open questions

- **F1 — How does an adopter's census registry pass hygiene check 3 (id 24)?** Options: (a) check 3
  admits `census-kept-paths.txt` by name, and the kit README says where a keep row goes; (b) the kit
  README and the hygiene docs tell an adopter to declare the name in `PROJECT_REGISTRY_EXTRA`. (b)
  leaves an adopter red until it reads the note, and it edits `memory/HYGIENE.md`, a governance
  carrier. (a) is the route `TOOL-bQuiltedLantern-3` and `TOOL-aRepatriatedFork-10` S4 ruled for a
  registry a kit reads at its default path. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  the most feature-rich option and the ruled precedent. widens: none · relaxes: none
- **F2 — May S12 re-stamp `memory/guides/SESSION-KICKOFF.md`, a governance carrier?** Options: (a)
  yes, under the build's grant, the stamp in this pass's commit beside its edit of
  `tools/memory-tree/check-memory-hygiene.sh`, a watched file; (b) no, which the pre-commit hook's staged arm
  refuses. (b) fails AC5. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 5, the README's `may:` grant, as `TOOL-dTotalRecall-60` §8 F2 and
  `TOOL-dTotalRecall-69` §8 F1 use it. grants: PLAY-dClosedLoop-3 SESSION-KICKOFF.md's last-audit
  stamp follows the check-3 edit · widens: none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F4 — Where is the pinned row's reason observed whole (S4)?** Its lines print its ask and its records and no
  reason, at HEAD and after unit 66. Options: (a) the plant reads it through `read_kept_path`, by its named
  field; (b) widen unit 66's `read_pinned_rows` and its lines to print it. (b) changes three consumers for a value
  no one reads off that line. RESOLVED (agent, 2026-11-24, delegated): (a), rung 3, the read the finding's defect
  lived in. widens: none · relaxes: none
- **F5 — What does S21 build with no `govkit:generated` block in the tree?** Options: (a) the observation that none
  stands, the sites riding owner ask TOOL-dTotalRecall-109; (b) the second block's sites now, with no row to write.
  (b) is scaffolding for a held unit. RESOLVED (agent, 2026-11-24, delegated): (a), rung 3, as `TOOL-dTotalRecall-66`
  §8 F4 ruled for its S18. widens: none · relaxes: none
- **F6 — Does S13's grep read `tools/memory-tree/record-kinds.toml`?** Its `purpose.source` cells cite the layer spec by
  build-folder path, the citation `TOOL-dTotalRecall-18` S1's cell grammar requires. Options: (a) the kit's code files
  alone, the modules id 30 names; (b) every file, the cells re-sourced to `owner`. (b) drops each cell's citation.
  RESOLVED (agent, 2026-11-24, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 61 to 66, its 25
  confirmed minors: 23 MEDIUM, ids 2 3 4 5 6 9 10 11 12 13 14 17 18 22 24 25 26 27 28 29 30 31 32
  (items M1 to M17), and 2 LOW, ids 8 33 (items L1 and L2).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-74, TOOL-dTotalRecall-76, each the other end of an edge a unit the round-1 spec audit of units 67 to 70 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.
- rev-4 · 2026-11-24 · §1 S1 to S25 §3 §4 §5 AC1 to AC15 §7 §8 §10 · re-grounded at HEAD `c0a707782` per
  `2026-11-24-prompt-TOOL-dTotalRecall-70-reground-brief`, over unit 68 rev-3 and unit 66 rev-5: the blob probe is
  spelled and §4's table re-keyed on what units 52, 55 and 56 built from, each row reading its wanted count; the body
  compare reads pass(46), since unit 66 S35 changes the tip; S14's departure is unit 38's untaken hand-off, its
  evidence pass(64); S8 keeps the marker remedy alone; S9, S20, S22, S23 and S24 hold and are re-observed; S21 is cut
  (F5); S4's pinned half (F4) and S13's population (F6) are decided; AC5, AC7, AC9, AC11, AC12 and AC14 are probes; the
  registry's reader is `read_kept_rows`; the govkit, runbook, factory and `legacy_ledger.py` files leave Files touched.

## 10. Reuse audit

The seams are those the minors already name, re-read at `c0a707782`:

- the joined-text probe of `TOOL-dTotalRecall-67` §4, read from a blob;
- the ledger factory's `legacy_ledger.py#read_rows`, whose line numbers S11's findings carry, and unit 68's reader over it;
- check 3's by-name case for a kit-read registry, `pass-order-waiver.txt`'s;
- `id_grammar.py#check_marker_domain` and `id_grammar.py#load_sibling`;
- `record_causes.py#run_fixture`'s plants and the fixture registry's factory writer unit 68 S6 leaves;
- `tree_lib.build_kept_path_re` (`TOOL-dTotalRecall-66` §4);
- `gov_record.py new deviation`, the one write door.

No mechanism is minted beyond four plants, one constant and one case.
`python tools/codebase-map/reuse_lookup.py "a shrink-only ledger registration for a project path list read by the census"`
ranks the factory's `read_rows` fifth among name-stem neighbours (DERIVED 2026-11-24, that command). The recall
query below found the factory and the decision `TOOL-bQuiltedLantern-3`, which settles S12's route.

Recall terms used: `python tools/memory-recall/query.py "how is a memory/project registry registered as a ledger population and ratcheted" --terms "ledger registration shrink-only legacy_ledger read_rows project registry PROJECT_REGISTRY_EXTRA census keep gained"`
