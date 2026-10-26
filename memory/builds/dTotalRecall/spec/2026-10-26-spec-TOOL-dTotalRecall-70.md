# TOOL-dTotalRecall-70 — the round-5 minors: each criterion that observed nothing is observed at the tip, and each gap it hid in units 61 to 66 is closed

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 33 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
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

## 2. Scope (IN)

Every item states its change to the unit it lands on, as that unit was built. A landed spec is
frozen and is not edited. An item whose unit's criterion observed nothing therefore makes the
observation at the tip. Where that observation is red, the item repairs the code, or writes a
deviation record when the departure is in a spec. "The registry" is
`memory/project/census-kept-paths.txt`, a ledger home after `TOOL-dTotalRecall-68`. "pass(N)" is the
first line of `git log --reverse --format=%H --grep='^Pass: TOOL-dTotalRecall-N$' 462d20f3..HEAD`.
"The probe" is the joined-text count of `TOOL-dTotalRecall-67` §4.

- **S1** — id 2 (M1). Unit 62's AC3 grep, `git grep -n absorbs -- tools/memory-tree/kit.toml`,
  certified nothing, because the field existed at no step. This unit's ledger records that grep as
  void. The absence it claimed is held by unit 66's AC5. Unit 59's own pass is read for the stale
  text's consequence, a cut of a field that does not exist: pass(59)'s diff carries no minus line
  spelling `absorbs`. Observed by AC1.
- **S2** — id 9 (M1). The §9 halves of units 62, 63 and 64's AC1 are re-read in the amendment's own
  form, which no edge-fold line matches. The text read is each target spec as it stood at its own
  unit's pass, `git show pass(T)^:<spec path>`. The forms are `amended by TOOL-dTotalRecall-62` in
  units 52 and 59, `added by TOOL-dTotalRecall-63` in unit 46 and `amended by TOOL-dTotalRecall-64`
  in unit 46. Observed by AC1.
- **S3** — id 31 (M1). The content halves are re-read the same way, by the strings of §4's table, for
  units 46, 52, 55, 56, 57 and 59. A target that built from text without its amendment gets a
  deviation record of that unit, and the code the amendment governs is read by the criterion the
  amendment carried. Observed by AC1.
- **S4** — id 4 (M2). The registry's row grammar is the factory's: TAB-separated, one field per
  column, never a whitespace split. The plant `kept-row-multiword` holds a reason of several words,
  `outside the write set`, on a plain keep and on a pinned writer's row. `--check` prints it whole for
  both. Observed by AC2.
- **S5** — id 13 (M2). A row is told apart by its named fields, never by its field count. A row
  whose field count is not the registration's seven is a red finding naming its line. That is the
  plant `kept-row-arity`, one row of four fields and one of six. Observed by AC2.
- **S6** — id 17 (M2). The reader is the factory's `read_rows`, never a hand parser of
  `transition_audit.read_registry`'s shape. Unit 68's AC3 probe is re-read at the tip. Observed by
  AC2.
- **S7** — id 28 (M2). Unit 65's error state "fewer than three fields" gives way to S5's rule, and a
  reason of several words survives both the plain-keep read and the pinned-writer read. Observed by
  AC2.
- **S8** — id 3 (M3). Unit 57's domain refusal and unit 58's remedy name the registry, never the
  constant. Each reads "keep it by a row of `<MEMORY_ROOT>/project/census-kept-paths.txt`", with the
  conf's memory root. The domain loop reads the registry's rows. Observed by AC3.
  **Readers:** by name: READER NOT IN TREE — `CENSUS_KEPT_PATHS` is minted by `TOOL-dTotalRecall-55`
  in this build and is absent at base `462d20f3` · by value: `read_kept_path`'s domain loop and its
  refusal message, unit 57's, and the marker reader's remedy message that `check_cause_writers` and
  `check_alias_compares` print, unit 58's, each of which this item points at the registry.
- **S9** — id 22 (M3). The plants `kept-row-editable`, `kept-row-drained` and `unkept-build-alias`
  write a fixture registry home, never a table row, and each stages its own red. Observed by AC3.
- **S10** — id 18 (M4). One keep home and one accessor stand at the tip. Unit 57's criterion that
  probed `tree_lib.CENSUS_KEPT_PATHS` is re-read over the registry's rows: every row's path matches
  `build_kept_path_re(memory_root)` (`TOOL-dTotalRecall-66` §4). Observed by AC3.
- **S11** — id 29 (M5). The census column's domain is `check_cause_writers` or
  `check_alias_compares`, and any other value is a red finding naming its line. A `(census, path)`
  pair held by two rows is red too, even when their reasons differ, which the factory's whole-key
  uniqueness does not catch. These are the plants `kept-row-unknown-census` and `kept-row-duplicate`.
  Observed by AC4.
- **S12** — id 24 (M6). Hygiene check 3 admits `census-kept-paths.txt` by name, as it admits
  `pass-order-waiver.txt`, because the engine reads it at its default path. The kit README says
  where a keep row goes. That edit moves a watched file, so `last-audit` is re-stamped after it under
  §8 F2. Observed by AC5.
- **S13** — id 30 (M7). The engine ships no build-folder path of this repository in any module.
  For every slug with a tracked build-folder `.py` file, `tools/memory-tree` spells none of its
  build-folder paths outside the self-tests. A literal found there moves to the registry. Observed
  by AC6.
- **S14** — id 5 (M8). Unit 64 changed unit 38's spec after unit 38's pass. That change is a
  departure, so this unit writes the deviation record of unit 38, its approver `author-recorded`,
  naming unit 64's commit and the hand-off line it changed. Observed by AC7.
- **S15** — id 10 (M9). Unit 64's AC1 edge alternative is re-read over joined text:
  `whose body this unit rebuilds` in unit 46's spec at pass(46)^. Observed by AC8.
- **S16** — id 14 (M10). Unit 46's Goal, "This unit rebuilds the parser on that regex", is read at
  pass(46)^. Whatever it reads, the body unit 46 left is compared with unit 54's by S17's probe. A
  rebuilt body is repaired back to unit 54's. Observed by AC8.
- **S17** — id 32 (M11). The body compare covers both names unit 54 mints: the `parse_id_parts`
  segment and the module-level `SUFFIX_RE` assignment, each equal to pass(54)'s. `id_grammar.py`
  assigns `SUFFIX_RE` once. Observed by AC8.
- **S18** — id 11 (M12). Every compare against a blob reads both sides as text with universal
  newlines. Each revision is spelled `<sha>:./<file>` from the file's directory, or by its
  repository-root path. That covers S17's probe, and unit 66's AC14 and AC22 as re-read here.
  Observed by AC8 and AC9.
- **S19** — id 12 (M13). Every build-order check reads ancestry, never `git log` output order. The
  pairs are pass(56) before pass(57) (unit 61's AC3), pass(54) before pass(46) (unit 63's AC2) and
  pass(54) before pass(45) (unit 66's AC23). Observed by AC10.
- **S20** — id 6 (M14). S34 of unit 66 is observed where its fixtures live. Two fixture functions
  open `tempfile.TemporaryDirectory`: the one building unit 59's plant `merged-home-gained` in
  `tools/lib/legacy_ledger.py`, and the one building unit 60's AC23 adopter in
  `tools/govkit/selftest.py`. Unit 60's AC14 has no arm, so its ledger line names the
  `TemporaryDirectory` path it ran in. Observed by AC11.
- **S21** — id 25 (M15). Every govkit site that assumes one `.gitattributes` row also reads the
  `govkit:generated` row. The rollback snapshot (`tools/govkit/govkit.py:10343-10349`) is taken when
  either block is written or withdrawn, and its two restores (`:11716-11719`, `:11860-11863`) put
  back both blocks' bytes and receipt rows. The new row's role is stated beside `UPDATE_ROLE`
  (`:8487-8489`) and `known_roles` (`:2733`). The `check` drift loop (`:5596`) keys on `block_id`
  and is left as it is. `WIRE-INTO-PROJECT.md:1405-1409` describes both blocks' restore. Observed
  by AC12.
- **S22** — id 26 (M16). The readers of the pinned writer's row are re-pointed onto the registry.
  Unit 50's plants `pinned-writer-drained` and `departures-pinned` stage a registry row whose
  `records` field is a glob and whose disposition is `keep:<ask>`. Unit 53's `--cause-writers`
  prints `deviations.py` with its pinned disposition, read from that row. Unit 66 S1's drain covers
  that row beside unit 50 S2's ask rule. Observed by AC13.
  **Readers:** by name: READER NOT IN TREE — `CAUSE_WRITER_PINNED` is minted by
  `TOOL-dTotalRecall-50` in this build and is absent at base `462d20f3` · by value: unit 50's two
  plants, unit 53's `--cause-writers` disposition table and unit 66 S1's drain, each pointed at the
  registry row by this item.
- **S23** — id 27 (M17). Unit 66's AC22 is read where a ledger line can be. The grep runs over
  `memory/builds/dTotalRecall/build/` only, and needs one line carrying both `tree_lib.py:410-412`
  and `:421`. Observed by AC9.
- **S24** — id 8 (L1). The alias census is observed by its own command. `record_kinds.py --check`
  prints one line naming both `deviations.py:380` and `kept pinned instrument`. That is the reading
  unit 65's AC2 and unit 61's AC2 meant. Observed by AC14.
- **S25** — id 33 (L2). Unit 63's cited-family case is re-run at the tip with its conf spelled
  whole: `MEMORY_ROOT=memory`, `FAMILIES="tooling:TOOL"` and `RECALL_CITED_FAMILIES="ZED"`. A
  `ConfError` from that tree is a fixture fault, never a pass. Observed by AC15.

## 3. Non-goals (OUT)

- The three highs: units 67, 68 and 69.
- Editing a landed spec's text, frozen once its unit builds, as §2's opening states.
- The spec lints and checklist entries the report suggests as gates. The close's left-shift step
  (BUILD-METHOD M8) takes them.
- `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`, for S12 (§4, "Alternatives
  rejected").

### Edges

- **consumes-from** `TOOL-dTotalRecall-61` — its AC2 and AC3 as built, re-read by their own commands and by ancestry (ids 8, 12)
- **consumes-from** `TOOL-dTotalRecall-62` — its amendments to units 52 and 59 and its AC3, re-read at the tip (ids 2, 9, 31)
- **consumes-from** `TOOL-dTotalRecall-63` — its amendment to unit 46 and its AC2, re-read with the conf spelled whole and by ancestry (ids 9, 12, 31, 33)
- **consumes-from** `TOOL-dTotalRecall-64` — its amendments to units 46 and 38 and its AC1 and AC2, re-read over joined text and both segments (ids 5, 9, 10, 11, 14, 31, 32)
- **consumes-from** `TOOL-dTotalRecall-65` — the registry, `read_kept_path` and its by-value carriers, the engine's literals and check 3's admission (ids 3, 4, 8, 13, 17, 18, 22, 24, 28, 29, 30)
- **consumes-from** `TOOL-dTotalRecall-66` — S18's attributes sites, S34's fixtures, S36's pinned row and AC14, AC22, AC23 and AC28 (ids 6, 11, 12, 25, 26, 27, 30)
- **consumes-from** `TOOL-dTotalRecall-67` — the strings of its §4 table, re-read at the tip against the text units 55, 56 and 57 built from (id 31)
- **consumes-from** `TOOL-dTotalRecall-68` — the factory row grammar of the registry and its `records` and `keep:` fields (ids 4, 13, 17, 26, 28, 29)
- **hands-off** `TOOL-dTotalRecall-74` — its pass and its AC1 and AC8 ledger lines, whose backticked strings that unit re-reads by a probe no shell quotes at step 34 (the round-1 audit of units 67 to 70, id 11)
- **hands-off** `TOOL-dTotalRecall-76` — its §4 table and AC8 readings, its AC7 and S14 record, its messages, its fixture sweep, its check-3 admission and its S12 re-stamp, re-read or repaired by that batch (the round-1 audit of units 67 to 70, ids 2, 3, 4, 15, 18, 25, 30)
- **hands-off** `TOOL-dTotalRecall-88` — its four kept-row plants, its S8 message and its check-3 case, rebuilt on that batch's fixture base, read at step 33 and named as the one second spelling (the round-1 audit of units 71 to 76, ids 3, 25, 26, 27, 43)

## 4. Design

### How the batch builds

One pass, after every other unit is terminal. The items share `tree_lib.py`, `record_causes.py` and
`record_kinds.py`, and every half would regenerate `memory/map/generated/` with its generator. So
BUILD-METHOD M6 keeps them one unit. Inside the pass the order is:

1. The read-only items: S1 to S3, S10, S15 to S19, S23 and S25. Each red they find decides a repair
   below.
2. The registry items: S4 to S9, S11 and S22.
3. The engine items: S13 and S20, then S21.
4. S12 and its re-stamp, last, so that the stamp follows every watched edit of the pass.
5. S14's deviation record and the ledger lines.

### The amendment strings of S2 and S3

Each string is read with the probe over `git show pass(T)^:memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-T.md`.
A string marked "1" must print at least 1. A string marked "0" must print 0.

| T | Amending unit | String | Wanted |
|---|---|---|---|
| 52 | 62 | `first seed record-kinds-legacy` | 1 |
| 59 | 62 | ``` `absorbs` is absent ``` | 1 |
| 59 | 62 | `it replaces unit 52's absorbed-population arm` | 0 |
| 46 | 63 | `ZED-aFoo-2` | 1 |
| 46 | 64 | `This unit's pass builds no body and observes that one` | 1 |
| 46 | 64 | `whose body unit 54 builds and this unit's criteria observe` | 1 |
| 46 | 64 | `whose body this unit rebuilds` | 0 |
| 55 | 61 | `whose last rows they are after unit 53` | 1 |
| 56 | 61 | `whose last row it is after unit 53` | 1 |
| 57 | 61 | `this one follows units 55 and 56` | 1 |

PINNED, measured 2026-10-26 at `653bed738`: every "1" string prints 0 over its target spec and at
least 1 over its amending spec. Every "0" string prints 1 over its target spec. So each row can
read either value. `rebuilds the parser on that regex` (S16) and ``Minted: `SUFFIX_RE` `` (S17)
print 1 over unit 46's spec at the same commit, and unit 64 amends neither. S16 and S17 therefore
judge the code, not the text.

### The body compare of S16 to S18

```bash
# run from tools/memory-tree/
python -c "import ast,subprocess,sys
def segs(src):
    t = ast.parse(src); out = {}
    for n in t.body:
        if isinstance(n, ast.FunctionDef) and n.name == 'parse_id_parts': out['parse_id_parts'] = ast.get_source_segment(src, n)
        if isinstance(n, ast.Assign) and any(getattr(x, 'id', '') == 'SUFFIX_RE' for x in n.targets): out.setdefault('SUFFIX_RE', []).append(ast.get_source_segment(src, n))
    return out
old = subprocess.run(['git', 'show', sys.argv[1] + ':./id_grammar.py'], capture_output=True, check=True).stdout.decode('utf-8').replace('\r\n', '\n')
new = open('id_grammar.py', encoding='utf-8').read()
a, b = segs(old), segs(new)
print(a == b, len(b.get('SUFFIX_RE', [])))" <pass(54)>
```

It prints `True 1` when unit 46 left unit 54's body and one `SUFFIX_RE` assignment.

### The registry rules of S4, S5, S7 and S11

`read_kept_path` takes the factory's rows. Before it answers, it refuses the following, each as a
red finding naming the line:

- a malformed row, which the factory returns;
- a census value outside `check_cause_writers` and `check_alias_compares`;
- a second row for one `(census, path)` pair.

`record_causes.py --check` and `record_kinds.py --check` both print those findings.

### S12's admission

In check 3 of `tools/memory-tree/check-memory-hygiene.sh`, a case `F:census-kept-paths.txt) ;;`
sits beside `F:role-stand-in-waiver.txt` (`:745`), above the `PROJECT_REGISTRY_EXTRA` case. Its
comment names the reason those two give: a kit reads the file at its default path. The sentence at
`tools/memory-tree/README.md:716` names this registry beside `pass-order-waiver.txt`. A new
paragraph says that an adopter keeps a census hit in a file of its own build folders by a row
there. The decisions `TOOL-bQuiltedLantern-3` and `TOOL-aRepatriatedFork-10` S4 rule this route.
Gov's own `PROJECT_REGISTRY_EXTRA` entry for the name stays as unit 65 wrote it, and the test
fixture of §7 proves admission with no such entry.

### Inventory

Minted: the fixture plants `kept-row-multiword`, `kept-row-arity`, `kept-row-unknown-census` and
`kept-row-duplicate` in `record_causes.py --fixture`; the check-3 case `F:census-kept-paths.txt`;
a deviation record of `TOOL-dTotalRecall-38`. Naming cell: none, no function minted.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/record_causes.py`, `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`, `tools/memory-tree/README.md`
- `memory/guides/SESSION-KICKOFF.md`
- `tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `WIRE-INTO-PROJECT.md`
- `tools/lib/legacy_ledger.py`, `tools/memory-tree/legacy_ledger.py`, `tools/gate-lint/legacy_ledger.py` (only where S20 moves a fixture, the three edited in one commit under `PARITY_ROWS`)
- `tools/memory-tree/id_grammar.py` (only where S16 finds a rebuilt body)
- `memory/builds/dTotalRecall/build/` (S14's deviation record and this unit's ledger lines)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **S12 by documentation alone**, declaring the name in each adopter's `PROJECT_REGISTRY_EXTRA`.
  An adopter who writes the file as told is red until it finds the note. The decision
  `TOOL-bQuiltedLantern-3` places a registry a kit relies on in the kit's whitelist instead.
- **A bullet in `memory/HYGIENE.md` and its template beside `pass-order-waiver.txt`.** That file is
  a governance carrier, and the README's grant reaches only the stamp precedent `TOOL-dTotalRecall-60`
  §8 F2 set. The kit README is the document an engine adopter reads, and its by-name sentence
  already stands at `:716`.
- **Two batches.** S8, S9, S11 and S22 write `record_causes.py`, and so do S4 to S7. No split leaves
  two disjoint write sets under M6's clauses.

## 5. Production-readiness checklist

- security — no new write surface. Check 3 admits one more name under `<MEMORY_ROOT>/project/`, a
  file the engine already reads (unit 65).
- perf / scale — reads and plants only. The body compare reads one blob.
- error / empty / loading states — each registry refusal is a red finding naming its line. A
  `ConfError` from S25's tree is a fixture fault.
- observability — each re-read writes its count or verdict into this unit's ledger line. A void
  criterion is recorded as void.
- risks — S12 changes an adopter's check 3. It admits a name and refuses nothing it admitted before.
- testing — AC1 to AC15 by the pass; the arms of §7 at the close.
- migration — none. S22's plants change their fixtures only.
- user docs — none under `help/`; S12's text is in the kit README.

## 6. Acceptance criteria

- **AC1** — When the probe runs over `git show pass(T)^:<spec path>` for each row of §4's table, each
  prints the wanted count. The §9 forms of S2 print at least 1 in their targets.
  `git show pass(59) -- tools | grep -c "^-.*absorbs"` prints 0.
  Red when: a unit built from text its amending unit had not written, and no deviation record names
  it.
  figure: the counts at writing are PINNED in §4; the tip counts are DERIVED by the pass.
- **AC2** — When `python record_causes.py --fixture --plant kept-row-multiword` runs from
  `tools/memory-tree/`, `--check` prints `kept outside the write set` whole, on the plain keep's line
  and on the pinned row's line. `--plant kept-row-arity` prints a red naming each malformed row's
  line. At the tip,
  `python -c "import inspect, tree_lib; s = inspect.getsource(tree_lib.read_kept_path); print('read_rows' in s, '.split(' in s)"`
  prints `True False`.
  Red when: a reason is cut at a space, or a row of the wrong arity is read.
- **AC3** — When `git grep -n "census-kept-paths.txt" -- record_causes.py record_kinds.py tree_lib.py`
  runs from `tools/memory-tree/` at the tip, it prints the domain refusal's line and the marker
  remedy's line. `git grep -n CENSUS_KEPT_PATHS -- tools`, run from the repository root, prints
  nothing. Each plant of S9 prints its own red
  finding from its fixture home. A `python -c` probe over the registry's rows finds every path
  matching `tree_lib.build_kept_path_re` for the conf's memory root.
  Red when: a message names a table no tree holds, a plant stages nothing, or a row names an editable
  file.
- **AC4** — When `python record_causes.py --fixture --plant kept-row-unknown-census` and
  `--plant kept-row-duplicate` run from `tools/memory-tree/`, each `--check` prints a red finding
  naming the planted row's line.
  Red when: a mistyped census or a second row for one pair is read silently.
- **AC5** — When `check-memory-hygiene.sh` runs over a scratch tree holding
  `census-kept-paths.txt` under `memory/project/` and no `PROJECT_REGISTRY_EXTRA`, check 3 names no such path.
  With the file renamed `census-kept-pathz.txt`, it names that one. `grep -c census-kept-paths.txt
  tools/memory-tree/README.md` prints at least 1. `bash skills/session-kickoff/manifest-check.sh`
  exits 0 at the tip.
  Red when: an adopter's registry reds check 3, or the watched edit has no re-stamp after it.
- **AC6** — When, for each slug S that `git ls-files 'memory/builds/*/build/*.py' | cut -d/ -f3 | sort -u`
  prints, `git grep -nF "memory/builds/$S/build/" -- tools/memory-tree ':!*selftest*' ':!*.test.*'`
  runs at the tip, it prints nothing.
  Red when: an engine module ships a build-folder path of this repository.
- **AC7** — When `git log --format=%H pass(38)..HEAD -- memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-38.md`
  prints a commit, `git grep -l "deviation TOOL-dTotalRecall-38" -- memory/builds/dTotalRecall/build`
  prints a record whose evidence names that commit.
  Red when: unit 38's spec moved after its pass and no deviation record names the move.
- **AC8** — When §4's body compare runs from `tools/memory-tree/` with pass(54), it prints `True 1`.
  The probe over unit 46's spec at pass(46)^ prints 0 for `whose body this unit rebuilds`, and the
  ledger records the count of `rebuilds the parser on that regex` there.
  Red when: unit 46's pass rebuilt either name, or bound `SUFFIX_RE` twice.
- **AC9** — When `git grep -n -e "tree_lib.py:410-412" --and -e ":421" -- memory/builds/dTotalRecall/build`
  runs at the tip, it prints at least one line. `git show 462d20f3` of `tree_lib.py`, run from
  `tools/memory-tree/` and read as text, holds `BIND_RE` and `def record_paths` at those lines. Unit
  66's AC14 compare, re-run from `memory/project/` with `git show` of `legacy-records.txt` at unit 19's seed commit,
  prints no key the seed lacked.
  Red when: the ledger file prints no such line, or a compare reads a path git cannot resolve.
- **AC10** — When `git merge-base --is-ancestor` runs at the tip on the pairs pass(56) and pass(57),
  pass(54) and pass(46), and pass(54) and pass(45), each exits 0.
  Red when: a unit built before the unit it reads.
- **AC11** — When a `python -c` probe prints, for each fixture function S20 names, whether its source
  holds `tempfile.TemporaryDirectory`, it prints `True` for each. The ledger line for unit 60's AC14
  names the path it ran in. In a scratch copy with one such call spelled as a literal scratch path,
  the probe prints `False`.
  Red when: a fixture is made at a fixed path.
- **AC12** — When `python tools/govkit/govkit.py update` changes only the `govkit:generated` block of
  a scratch adopter and is made to fail its verify step, the rollback leaves `.gitattributes` and both
  blocks' receipt rows equal to their pre-run values.
  `grep -c "both blocks" WIRE-INTO-PROJECT.md` prints at least 1.
  Red when: the generated block or its row stays at the failed run's value.
- **AC13** — When `python record_causes.py --cause-writers` runs from `tools/memory-tree/` at the
  tip, it prints `deviations.py` with its pinned disposition and the ask of its row.
  `--fixture --plant pinned-writer-drained` and `--plant departures-pinned` each print their red from
  a registry row.
  Red when: a reader of the pinned row reads no row, or stages nothing.
- **AC14** — When `python record_kinds.py --check` runs from `tools/memory-tree/` at the tip, one
  line of its output carries both `deviations.py:380` and `kept pinned instrument`.
  Red when: the alias census keeps the compare by no row, or prints the reason cut.
- **AC15** — When a `python -c` probe calls `parse_id_parts("ZED-aFoo-2", tree)`, in a
  `tempfile.TemporaryDirectory()` tree whose `.memory-tree.conf` is S25's three keys, it prints
  `('ZED', 'aFoo', 2)`.
  Red when: the call raises `ValueError`. A `ConfError` is a fixture fault and is fixed, never
  passed.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kickoff-manifest ratchet` · `kit/dogfood doc parity` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC2 AC3 AC4 AC13 · the plants `kept-row-multiword`, `kept-row-arity`, `kept-row-unknown-census`, `kept-row-duplicate` and S22's two re-staged plants, staged by skipping each refusal · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 · `census-kept-paths.txt` planted with no `PROJECT_REGISTRY_EXTRA`, staged by deleting the check-3 case · none
New arm: tools/govkit/selftest.py · covers AC12 · a failed update that wrote only the generated block, staged by snapshotting the lf-pin row alone · none

## 8. Open questions

- **F1 — How does an adopter's census registry pass hygiene check 3 (id 24)?** Options: (a) check 3
  admits `census-kept-paths.txt` by name, and the kit README says where a keep row goes; (b) the kit
  README and the hygiene docs tell an adopter to declare the name in `PROJECT_REGISTRY_EXTRA`. (b)
  leaves an adopter red until it reads the note, and it edits `memory/HYGIENE.md`, a governance
  carrier. (a) is the route `TOOL-bQuiltedLantern-3` and `TOOL-aRepatriatedFork-10` S4 ruled for a
  registry a kit reads at its default path. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  the most feature-rich option and the ruled precedent. widens: none · relaxes: none
- **F2 — May S12 re-stamp `memory/guides/SESSION-KICKOFF.md`, a governance carrier?** Options: (a)
  yes, under the build's grant, the stamp following this pass's edit of
  `tools/memory-tree/check-memory-hygiene.sh`, a watched file; (b) no, leaving the
  `kickoff-manifest ratchet` leg red from this pass to the close. (b) fails AC5. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 5, the README's `may:` grant, as `TOOL-dTotalRecall-60` §8 F2 and
  `TOOL-dTotalRecall-69` §8 F1 use it. grants: PLAY-dClosedLoop-3 SESSION-KICKOFF.md's last-audit
  stamp follows the check-3 edit · widens: none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 61 to 66, its 25
  confirmed minors: 23 MEDIUM, ids 2 3 4 5 6 9 10 11 12 13 14 17 18 22 24 25 26 27 28 29 30 31 32
  (items M1 to M17), and 2 LOW, ids 8 33 (items L1 and L2).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-74, TOOL-dTotalRecall-76, each the other end of an edge a unit the round-1 spec audit of units 67 to 70 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.

## 10. Reuse audit

The seams are those the minors already name:

- the joined-text probe of `TOOL-dTotalRecall-67` §4;
- the ledger factory's `read_rows` and the registration of `TOOL-dTotalRecall-68`;
- check 3's by-name case for a kit-read registry (`tools/memory-tree/check-memory-hygiene.sh:742-745`);
- govkit's rollback snapshot (`tools/govkit/govkit.py:10343-10349`);
- the scratch-directory idiom of `tools/codebase-map/selftest.py:1815`;
- `tree_lib.build_kept_path_re` (`TOOL-dTotalRecall-66` §4).

No mechanism is minted beyond four plants and one case.
`python tools/codebase-map/reuse_lookup.py "a shrink-only ledger registration for a project path list read by the census"`
ranked name-stem neighbours and not the factory, which is absent at base `462d20f3`. The recall
query below found the factory and the decision `TOOL-bQuiltedLantern-3`, which settles S12's route.

Recall terms used: `python tools/memory-recall/query.py "how is a memory/project registry registered as a ledger population and ratcheted" --terms "ledger registration shrink-only legacy_ledger read_rows project registry PROJECT_REGISTRY_EXTRA census keep gained"`
