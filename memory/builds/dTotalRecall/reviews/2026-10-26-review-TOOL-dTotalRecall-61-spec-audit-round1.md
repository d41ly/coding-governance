**Serves:** spec-audit TOOL-dTotalRecall-63@rev-1 TOOL-dTotalRecall-64@rev-1 TOOL-dTotalRecall-61@rev-1 TOOL-dTotalRecall-62@rev-1 TOOL-dTotalRecall-65@rev-1 TOOL-dTotalRecall-66@rev-1

# Tier-2 review: the round-1 spec audit of dTotalRecall's six round-4 promotions (TOOL-dTotalRecall-61 to -66)

Provenance: a Tier-2 spec audit at full intensity, run on 2026-10-26 over dTotalRecall's round-4 promotion commit `c235c2e05` (packet re-rendered at `653bed738`). Five lenses ran first (finders gov-spec-reviewer). Five skeptic batches followed (gov-skeptic), then synthesis (gov-synthesizer). 52 spec documents were supplied as sibling context.

Reviewed: memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-63.md@075a47273f2ffe110c90a9ed57af0b0c3bce03ac, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-64.md@d44e97d57d1c03c056a92b014c8aa63840f595f6, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-61.md@ebfb13577587d67978a0925589096ce1bc3399a6, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-62.md@9c6c968a24f23b1947bd19349875da6e2709f76e, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md@c2a9995bc82d97c8a0d0fef81a040d47f27dc817, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-66.md@801dda34f78ef3b60b690b9db57185cd50a0bb59

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker survived. Three high, 17 medium and 2 low items stand. Each has a fix that amends spec text before the affected unit builds.

By raw confirmed finding, the tally is 3 high, 23 medium and 2 low.

The highs share two themes:
- The amending AC1 of unit 61 cannot go red when the amendments to units 55, 56 and 57 are missing, because the hands-off fold already put a §9 line naming unit 61 into each of them (H1).
- Unit 65's new keep registry sits outside the machinery the build already relies on. It is not registered as a `[[ledger]]` population (H2), and its `.memory-tree.conf` edit lands after the last `last-audit` re-stamp, which reds the bar until the close (H3).

Unit 65 also carries most of the mediums: its row grammar contradicts itself (M2), its retirement inventory misses readers (M3), it repairs unit 55 after unit 55 builds (M4), and it leaves adopter-facing gaps (M6).

Where one defect was found at two binding grades, it appears once per grade, and the lower item names the item it shares the defect with.

## Review shape

The review ran at intensity full: raw 33, confirmed 28, refuted 5, unverified 0 (0 uncertain), precision 0.85.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 8 | 7 | 1 | 0 | 0 | 0.88 |
| grounding | yes | 7 | 6 | 1 | 0 | 0 | 0.86 |
| reuse | yes | 5 | 3 | 2 | 0 | 0 | 0.60 |
| blast-radius | yes | 7 | 6 | 1 | 0 | 0 | 0.86 |
| failure-envelope | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |

Adjudicated tally: by item, 0 blocker, 3 high, 17 medium, 2 low (22 items). By raw confirmed finding, 0 blocker, 3 high, 23 medium, 2 low (28 findings).

The five refuted findings are:
- id 7: AC3 and AC24 of unit 66 are the observations S5 and S32 ask for.
- id 15: 462d20f3 is still this run's merge-base.
- id 19: the map_lib.py:1502 citation is correct and the parent dependency is declared.
- id 20: a Python fixture idiom is a precedent, not a seam to reuse.
- id 23: a duplicate of id 28.

### Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdict hygiene: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 23 judged sound, 5 judged unsound, 0 none proposed, 0 not judged.
- Severity: 0 ungraded by the skeptic (bound at the finder's grade), 2 re-graded by the skeptic (ids 3 and 28, high to medium).
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 52 spec documents supplied as `specs`, as sibling context.
- Checklist: 44 items, each assigned to exactly one of 5 lenses (coherence 9, grounding 9, reuse 9, blast-radius 9, failure-envelope 8).
- By design: none supplied, no caller byDesign and a block of 0.
- Move check: no checked subject moved.

Every integrity count is zero where it should be, so this run is complete.

## High

### H1. Unit 61's AC1 is green before the pass, so the amendments to units 55, 56 and 57 are unobserved (id 1)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-61.md` §6 AC1 (:158-162), against its §2 S2 and S3.
- **What is wrong:** AC1 has two halves. Its §9 half counts lines naming TOOL-dTotalRecall-61 in each amended spec. The disposal pass already wrote a rev line into the §9 of units 53, 55, 56 and 57 naming unit 61: the edge-mirror line "the Edges block gains the mirror of TOOL-dTotalRecall-61 ...". So that half is green today. Its only text probe greps unit 53 for "stays in its constant at this pass". The Red-when "a spec §4 names is unamended" can therefore fire only for unit 53.
- **Consequence:** A unit-61 pass that amends only unit 53's S34 passes AC1. Unit 55 then never ends `CAUSE_WRITER_KEPT`, unit 56 never ends `ALIAS_COMPARE_KEPT`, and unit 57 gets no consumes-from edge to unit 56. The failure first shows at unit 57's AC3, after units 55 and 56 have already built from unamended text. The skeptic kept this at high rather than blocker because AC3 still catches it downstream.
- **Fix (skeptic: sound):** Have AC1 grep for each amendment's own text:
  - unit 55: its `git grep -n CAUSE_WRITER_KEPT -- tools` criterion;
  - unit 56: its `git grep -n ALIAS_COMPARE_KEPT -- tools` criterion;
  - unit 57: its `**consumes-from** \`TOOL-dTotalRecall-56\`` edge and its "follows units 55 and 56" line.

  Alternatively, count §9 lines carrying this unit's amendment form ("amended by TOOL-dTotalRecall-61 (id 1, item H1)"), which no spec carries today.
- **Related:** M1 is the same defect found at medium, extended to units 62, 63 and 64.
- **Gate suggestion:** a spec-lint rule: every AC that claims to observe a spec amendment must name a string that prints 0 at HEAD before the pass. A hands-off fold line naming the unit never counts as that string.

### H2. Unit 65's keep registry is a `memory/project/*.txt` file with no `[[ledger]]` registration and its own hand parser (id 16)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-65.md` §2 S1-S2, §4 "The registry", §10.
- **What is wrong:** Unit 65 adds `memory/project/census-kept-paths.txt` and names `transition_audit.read_registry` (transition_audit.py:759-774, a hand parser) as its seam. It names no `[[ledger]]` registration. The parent build dWitnessedBar (declared in README `parents:`) points every `memory/project/*.txt` at the ledger factory:
  - TOOL-dWitnessedBar-16 S1 derives that population;
  - its S4 says "no reader keeps a parser of the old grammar";
  - its §4 converts `read_registry` itself;
  - its AC1 is red when "a registry the rule finds has no registration".

  This build already registers its project homes that way (unit 19 S7, and unit 52 through `legacy_ledger.py`).
- **Consequence:** The keep list is graded by no engine, so a keep row added later to quiet the cause or alias census meets no shrink-only ratchet. The repo gains a second parser of a grammar the parent retires, and its cited seam is one the parent rewrites. That misleads the next change.
- **Fix (skeptic: the finder's proposal was rejected; this is the skeptic's corrected fix):**
  - Register `census-kept-paths` as a `[[ledger]]` population in `tools/memory-tree/kit.toml`, direction shrink-only. Its key fields are census, path and reason, and unit 66 S36's record glob and ask id are optional fields.
  - `read_kept_path` reads rows through `legacy_ledger.read_rows`.
  - Amend unit 66 S36 to tell a plain keep from a pinned writer by its named fields, not by field count.
  - Point §10 at `tools/lib/legacy_ledger.py` (TOOL-dWitnessedBar-13).
  - Add a criterion: `python legacy_ledger.py read census-kept-paths` prints every row with its reason, and a planted extra row is named `gained` against a fixture base.
- **Related:** This fix also settles the row-grammar defect (M2), and it should land in the same amendments that M4's fix makes to units 55 to 57.
- **Gate suggestion:** dWitnessedBar-16's own rule, run at spec time: a spec that adds a `memory/project/*.txt` file must name its `[[ledger]]` registration.

### H3. Unit 65 edits a watched file after the last `last-audit` re-stamp, so the bar is red until the close (id 21)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-65.md` §2 S1, §4 Files touched, §7, §8.
- **What is wrong:** The `watch:` list in `memory/guides/SESSION-KICKOFF.md` (:6) includes `.memory-tree.conf`. Unit 60 (order 31) S22 re-stamps `last-audit` over unit 52's conf edit, under its §8 F2 grant. Unit 65 is sequenced after unit 60 and adds `census-kept-paths.txt` to `PROJECT_REGISTRY_EXTRA` in that conf. It names no re-stamp, no `kickoff-manifest ratchet` leg and no grant. Unit 66 touches neither file.
- **Consequence:** manifest-check C5 (manifest-check.sh:1462-1473, "watched files changed since last-audit with no re-stamp") calls `fail 5`. The `kickoff-manifest ratchet` row in `tools/gate-legs.json` has no guard, so the bar is red on every run from unit 65's pass to the close.
- **Fix (skeptic: sound):**
  - Add `memory/guides/SESSION-KICKOFF.md` (the `last-audit` re-stamp, bundled with the conf edit) to §4 Files touched.
  - Add an S-item and a criterion: `bash skills/session-kickoff/manifest-check.sh` exits 0 at the pass tip.
  - Name `kickoff-manifest ratchet` in §7.
  - Add a §8 fork that cites the README `may:` grant, as unit 60 F2 does.

  Alternatively, move unit 60's re-stamp to after unit 65.
- **Gate suggestion:** a spec-lint rule: a spec whose Files touched names a path on the kickoff manifest's `watch:` list must also name `SESSION-KICKOFF.md` and the `kickoff-manifest ratchet` leg.

## Medium

### M1. AC1's §9 half is pre-green across units 61 to 64, so the amendments to units 55, 56, 57 and 59 are unobserved (ids 2, 9, 31)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-61.md` §6 AC1; `2026-10-26-spec-TOOL-dTotalRecall-62.md` §6 AC1 and AC3 (against its §2 S3); the same shape in AC1 of units 63 and 64.
- **What is wrong:** The round-4 hands-off fold (`c235c2e05`) already wrote a rev-2 or rev-3 §9 line naming the promoting unit into every spec it amends:
  - units 53, 55, 56 and 57 name unit 61;
  - units 52 and 59 name unit 62;
  - unit 46 names units 63 and 64.

  Every "§9 prints at least 1" half is therefore green at HEAD. The content halves check only unit 53 (for unit 61) and only unit 52 (for unit 62). Nothing checks unit 59's S3 amendment either. Spec 59 S2 still reads "`absorbs` is cut" (:39), and its New arm still "replaces unit 52's absorbed-population arm" (:139). Unit 62's AC3 grep (`git grep -n absorbs -- tools/memory-tree/kit.toml`) also prints nothing today, so it decides nothing.
- **Consequence:** A pass that amends only unit 53, or only unit 52, meets AC1, and its Red-when cannot fire. Units 55, 56 and 57 build from their old text, and nothing catches it until unit 57's AC3 at step 30. A unit-59 builder follows stale text and goes to cut a field that does not exist.
- **Fix (skeptic: sound for all three ids; merged):**
  - Key each §9 half on the amendment form, for example `grep -c "amended by TOOL-dTotalRecall-6N"`. The edge-fold lines ("gains the mirror of") do not match it.
  - Add one content grep per amended spec, each confirmed to print 0 at HEAD before the pass:
    - unit 55: "whose last rows they are after unit 53" or "so the constant ends at this pass";
    - unit 56: its `ALIAS_COMPARE_KEPT -- tools` criterion;
    - unit 57: a consumes-from line naming `TOOL-dTotalRecall-56`;
    - unit 59: its S2 "`absorbs` is absent", and the absence of `tools/memory-tree/kit.toml` from its Files touched.
  - For unit 62's AC3, run the `absorbs` check against a planted re-add of the field (described for the build, not run here), or drop the claim that it observes anything.
- **Related:** H1 is the unit-61 half of this defect at its binding high grade.
- **Gate suggestion:** the pre-green check named under H1.

### M2. Unit 65's registry has two row grammars: tab-separated, and `read_registry`'s whitespace split (ids 4, 13, 17, 28)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-65.md` §2 S1 (:35-36), §4 "The registry" (:82-84), §5 error states (:124), §10. Against `2026-10-26-spec-TOOL-dTotalRecall-66.md` §4 "The registry row after S36" (:192).
- **What is wrong:** S1 declares rows as `<census>\t<path>\t<reason>`. §4 says the grammar "follows read_registry there (:763-774): strip, skip # and blank, split". That reader does `bits = line.split()`, which splits on any whitespace. Every reason in the registry contains spaces ("pinned instrument", "outside the write set"). §5 handles only "fewer than three fields". Unit 66 tells a plain keep (3 fields) from a pinned writer (5 fields) by counting fields.
- **Consequence:** A builder who follows the cited reader cuts each reason to one word. A "pinned instrument" row becomes 4 tokens, which is neither 3 nor 5, so it is refused or misread. An "outside the write set" row becomes 6 tokens, so a plain keep can be read as a pinned writer whose record glob is `write` and whose ask is `set`. Rows with 4 or 6+ fields are undefined, and the malformed check never fires. Spec 65's AC2 expects `kept pinned instrument` printed whole, so the defect would likely red at the pass, which is why the skeptic graded id 28 medium rather than high.
- **Fix (skeptic: sound for all four ids; merged):**
  - In S1 and §4, state the split as `line.split("\t")`, tab only, with no whitespace collapse. Drop the claim that the grammar follows `read_registry`, or say plainly that it departs from it. `tools/gate-lint/sh_hygiene.py:402` `read_registry` is a valid tab-separated precedent.
  - Make exactly 3 or exactly 5 fields the only legal arities, and any other count a red finding naming its line. This amends §5's "fewer than three".
  - Add a plant whose reason has several words (for example `outside the write set`), read back whole through both the 3-field and the 5-field paths, and assert that `--check` prints the whole reason.
- **Related:** If H2's fix lands, the ledger factory's named fields replace the field count, and this item reduces to stating the factory's row grammar.
- **Gate suggestion:** a bug-class checklist entry (two-answers-to-one-question): a spec that cites a reader as "the grammar to follow" must quote that reader's split, and every sample row in the spec must parse under it.

### M3. Unit 65's retirement of `CENSUS_KEPT_PATHS` misses the readers and messages units 56, 57 and 58 put under `tools/` (ids 3, 22)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-65.md` §2 S3 Readers line (:47-49), §4 Files touched, §6 AC1.
- **What is wrong:** S3 names `read_kept_path` as the constant's only reader. These other carriers are unlisted:
  - spec 57:66-68 builds the loop `for c, p, reason in CENSUS_KEPT_PATHS:` and the error `raise ValueError(f"CENSUS_KEPT_PATHS row {p}: ...")`;
  - spec 58:37 ships the remedy "keep it by a CENSUS_KEPT_PATHS row; its bytes are not this build's";
  - unit 57's plant `kept-row-editable` builds "a fixture whose table holds a row";
  - unit 56's `unkept-build-alias` stages by "skipping the table read";
  - unit 55 plants `kept-row-drained`.

  Unit 66 re-words none of these.
- **Consequence:** AC1 (`git grep -n CENSUS_KEPT_PATHS -- tools` prints nothing) is red at unit 65's own pass unless the builder edits text the spec never names. If the builder only strips the name, the adopter-facing remedy no longer says where a keep goes, and the plants stop staging anything. AC1 does catch any leftover string, so the skeptic graded id 3 medium rather than high.
- **Fix (skeptic: sound for both ids; merged):**
  - Name every carrier in S3's Readers line and in S2: the domain loop moves to the registry rows, and unit 57's refusal and unit 58's remedy both name the registry, for example "keep it by a row of `<MEMORY_ROOT>/project/census-kept-paths.txt`".
  - The plants `kept-row-editable`, `kept-row-drained` and `unkept-build-alias` write a fixture registry file instead of a table row.
  - Add unit 58 to §3 Edges (consumes-from, with the mirror in 58), and add the module that holds unit 58's marker reader to Files touched.
  - Add a criterion that greps the remedy for the registry path.
- **Gate suggestion:** a bug-class checklist entry (retirement-inventory-misses-readers-by-value): a spec that retires a name must list the result of `git grep <name>` over the build's specs and `tools/`, one line per hit.

### M4. Unit 65 repairs unit 55 one step after unit 55 builds, so two units design one table and one accessor (id 18)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-65.md` §1 ("It repairs TOOL-dTotalRecall-55, at the step after it"), §4 Alternatives rejected.
- **What is wrong:** Spec 55 is `OPEN · rev-2 · order 30`, and its rev-2 log reads "nothing else moved". Its S1 still designs `CENSUS_KEPT_PATHS` in `tree_lib.py` and `read_kept_path(census, path)` (:101 mints both). Unit 65 (order 31) then removes the table and rebuilds the accessor with a root argument. Spec 64 rejects this pattern by name ("An edge-fold on unit 46 alone ..."), and units 61, 62 and 64 avoid it by amending their target before its pass.
- **Consequence:** The run builds a table, its accessor and unit 55's criteria in `tree_lib.py`, then rewrites them at order 31. Unit 57's criterion that probes `tree_lib.CENSUS_KEPT_PATHS` (spec 57:115) goes red after unit 65.
- **Fix (skeptic: the finder's proposal was rejected; this is the skeptic's corrected fix):** Amend units 55, 56 and 57 together before their order-30 passes, each a rev bump naming TOOL-dTotalRecall-65:
  - unit 55 builds `read_kept_path(census, path, root)` over `memory/project/census-kept-paths.txt`, with no `CENSUS_KEPT_PATHS`;
  - unit 56 adds its alias row to the registry file;
  - unit 57's domain rule and its criterion read the registry's rows, not `tree_lib.CENSUS_KEPT_PATHS`.

  Unit 65 then writes spec text only, or is folded.
- **Related:** With this fix, the carriers M3 lists are written registry-first, and H2's ledger registration belongs in unit 55's amendment.
- **Gate suggestion:** the round-3 order check: a unit whose spec names another unit it repairs must be ordered at or before that unit, or must bump that unit's spec.

### M5. The registry's census column has no domain and its (census, path) key has no uniqueness rule (id 29)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-65.md` §2 S1/S2 (:35-38), §5 error states (:124).
- **What is wrong:** Nothing restricts the census value to `check_cause_writers` or `check_alias_compares`, and nothing rejects a repeated (census, path) key. Unit 66 S1 and S3 drain only rows of those two census names. Unit 66 S36 adds five-field rows with no domain or uniqueness rule either.
- **Consequence:** A row with a typo in its census name is read and drained by nothing, and stays forever as a keep that keeps nothing. With a duplicate key, `read_kept_path` returns whichever row the reader happens to pick, so a stale reason can win silently.
- **Fix (skeptic: sound):** S1 states the domain: the census column is one of the census function names, and any other value is a red finding naming the line. A repeated (census, path) key is also red. Add the plants `kept-row-unknown-census` and `kept-row-duplicate` to §7's arm, and an AC that observes each one red.
- **Gate suggestion:** a bug-class checklist entry (C35 append-without-an-idempotence-key): every registry a spec adds states its key, its uniqueness rule and the value domain of each enumerated column.

### M6. An adopter told to "write its own registry" gets an unexplained red hygiene check 3 (id 24)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-65.md` §4 "Why the project layer" (:91-92), §4 Files touched (:106-111), §5 user docs (:131).
- **What is wrong:** The shipped engine reads `<M>/project/census-kept-paths.txt` at its default path, and §4 tells an adopter it "writes its own registry". `memory/project/` is a closed name set: check 3 in `check-memory-hygiene.sh` (:736-753) whitelists by name the registries a kit reads at their default path (`pass-order-waiver.txt`, `role-stand-in-waiver.txt`). Any other file falls to the bare "unexpected entries (structure)" refusal (:762-777). The spec neither adds the name to that whitelist nor documents the `PROJECT_REGISTRY_EXTRA` step, as `tools/memory-tree/README.md:562` does for `refusal-retirements.txt`. §5 says user docs are "none".
- **Consequence:** An adopter who creates the file as told gets a red `memory hygiene` check 3, and nothing they receive tells them why.
- **Fix (skeptic: sound):** Choose one route, list its files, and add a criterion for it:
  - (a) Add `F:census-kept-paths.txt` to check 3's whitelist in `tools/memory-tree/check-memory-hygiene.sh`. This is a watched file and changes the adopter contract, so it needs its own re-stamp and note.
  - (b) Document the EXTRA declaration in `tools/memory-tree/README.md` and in the registry lists of `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`, as `refusal-retirements.txt` is documented.
- **Gate suggestion:** a bug-class checklist entry (shipped-checker-edit-is-an-adopter-contract-change): a spec that makes a shipped engine read a new default path must name either the whitelist change or the adopter doc that declares it.

### M7. No criterion guards the engine's other modules against a build-folder path literal (id 30)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-65.md` §6 AC1 (:135-138); `2026-10-26-spec-TOOL-dTotalRecall-66.md` §6 AC28 (:320).
- **What is wrong:** The goal says "the engine ships no path of this repository". AC1 greps `memory/builds/[A-Za-z]+/` over `tree_lib.py` only, while Files touched also names `record_causes.py` and `record_kinds.py`. `CAUSE_WRITER_PINNED`, minted by unit 50 in `record_causes.py`, holds the dClosedLoop `deviations.py` literal. Unit 66 AC28 greps only for the constant's name.
- **Consequence:** A build-folder literal left in, or inlined into, `record_causes.py` or `record_kinds.py` when S36 dissolves the constant ships to every adopter through `include = "**"`, and no criterion reds. That is the H4 defect unit 65 was promoted to close.
- **Fix (skeptic: the finder's proposal was rejected; this is the skeptic's corrected fix):** Leave unit 65 AC1 on `tree_lib.py`. Widen unit 66 AC28 instead. At the tip, for every slug S in `git ls-files 'memory/builds/*/build/*.py' | cut -d/ -f3 | sort -u`, the command `git grep -nF "memory/builds/$S/build/" -- tools/memory-tree ':!*selftest*' ':!*.test.*'` prints nothing.
- **Gate suggestion:** the round-3 lint over engine-role kit files that reds a literal path under `memory/builds/` in shipped code.

### M8. Unit 64 edits unit 38's spec after unit 38 has built, with no deviation record (id 5)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-64.md` §4 "The amendment to unit 38"; §6 AC1.
- **What is wrong:** Unit 38 builds at order 8 and unit 64 at order 9 (spec status lines and the README build table). Unit 64 rev-bumps unit 38's spec, and AC1 requires `grep -c TOOL-dTotalRecall-64` over 38's §9 to print at least 1. The packet prompt (:52) makes every departure from a spec after its first pass a deviation record, and spec 66:33-34 says "a landed spec is frozen and is not edited". Unit 64 names no deviation record.
- **Consequence:** The pass either breaks the frozen-spec rule with no deviation record, so the departures report misses it, or cannot meet AC1. The amendment also changes the hand-off of a unit that has already landed.
- **Fix (skeptic: sound):** Drop the unit-38 amendment and the unit-38 halves of AC1, and let unit 38's stale hand-off line stand as history. Alternatively, record the change as a deviation of unit 38 (author-recorded), as the packet's departure rule requires, and say so in §4 and §5.
- **Gate suggestion:** an order check in the build index: a spec may amend another unit's spec only if that unit's order is greater, or it names a deviation record.

### M9. Unit 64's AC1 edge alternative can never match, because the phrase wraps across two lines (id 10)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-64.md` §6 AC1, and §1 (the claim that the edge "still reads 'whose body this unit rebuilds'").
- **What is wrong:** Unit 46's consumes-from line wraps "whose body this unit" / "rebuilds under its name and signature" across lines 55-56. AC1's line-wise `grep -cE "...|whose body this unit rebuilds"` hits only lines 73, 75 and 81, so the edge alternative is vacuous.
- **Consequence:** If the pass leaves unit 46's edge unamended (S3), AC1 still counts 0 for it. The edge keeps promising that unit 46 rebuilds the body, which is H3's two-designers defect, and AC1 certifies a check it never makes.
- **Fix (skeptic: sound):** Match a phrase that does not wrap, for example `grep -c 'rebuilds under its name and signature'`. Or join paragraphs first (`tr '\n' ' '` or `awk RS=''`), then grep. Confirm the grep prints 1 at HEAD before the pass, so the criterion can go red.
- **Gate suggestion:** a bug-class checklist entry (ledger-token-wrapped-across-a-line-joins-nothing): every grep an AC names must print a positive count at HEAD before the pass when it is meant to count down to 0.

### M10. Unit 64 amends unit 46's sections but not §1, whose Goal still says "rebuilds the parser" (id 14)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-64.md` §2 S1-S3, §4 "The amendments to unit 46" (the list of sections amended).
- **What is wrong:** The amendment list and §9 template cover "S1 S2 S3 §4 §5 §7 §10 §3" and leave out §1. Spec 46 §1 (:26-27) still ends "This unit rebuilds the parser on that regex", which contradicts the amended S1 ("builds no body"). AC1 does not grep for that phrase.
- **Consequence:** Unit 46's builder reads a Goal telling them to rebuild `parse_id_parts` on `build_id_token_re`, the overwrite that H3 and this unit exist to prevent. It is the "amendment that leaves its other half standing" that the spec's own Alternatives section names.
- **Fix (skeptic: sound):** Add §1 to the amendment list, rewriting the last sentence as, for example, "This unit observes the parser unit 54 builds on that regex." Add "rebuilds the parser on that regex" to AC1's must-print-0 grep.
- **Gate suggestion:** the round-3 checklist entry (amendment-leaves-its-other-half-standing), extended so that a superseding amendment greps every section of the target for the superseded verb.

### M11. Unit 64's AC2 compares only `parse_id_parts`, so a rebinding of `SUFFIX_RE` goes unobserved (id 32)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-64.md` §6 AC2 and AC1.
- **What is wrong:** Unit 54's body is two names: `parse_id_parts` and the module-level `SUFFIX_RE` it reads (spec 54 :89-93, :113). AC2 compares only the `parse_id_parts` segment. Unit 46 still defines `SUFFIX_RE` (:70) and says "Minted: `SUFFIX_RE`" (:88). Unit 64 §4 amends that Inventory, but AC1's pattern does not match line 88.
- **Consequence:** A unit-46 pass that re-mints or rebinds `SUFFIX_RE` in `id_grammar.py` (the second module-level assignment wins) changes suffix stripping for every id reader. The compared function segment stays byte-equal, so AC2 stays green.
- **Fix (skeptic: sound):** AC2 compares both segments, `parse_id_parts` and the `SUFFIX_RE` assignment, against unit 54's pass commit, and asserts that `grep -c "^SUFFIX_RE *=" id_grammar.py` prints 1. AC1 adds `Minted: \`SUFFIX_RE\`` to its zero-count pattern for unit 46's spec.
- **Gate suggestion:** a spec-lint rule: a byte-equality AC over a function must list every module-level name the function reads.

### M12. `git show` probes in units 64 and 66 break on this checkout's CRLF working tree and on a bare relative path (id 11)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-64.md` §6 AC2; the same path form in `2026-10-26-spec-TOOL-dTotalRecall-66.md` AC14 (:289) and AC22 (:308).
- **What is wrong:** AC2 compares `ast.get_source_segment` of `parse_id_parts` in the `git show` blob (LF) with the working file. Here `tools/memory-tree/*.py` are CRLF in the working tree (`core.autocrlf=true`, `* text=auto`), so a bytes comparison is never equal. Also, `git show <commit>:id_grammar.py` run from `tools/memory-tree/` fails ("exists, but not 'tree_lib.py'"), because git needs `:./id_grammar.py` or the full path.
- **Consequence:** A bytes-read probe reds unit 46's pass when the body is untouched, and the builder chases a phantom rewrite or weakens the probe. A probe that follows the spec's path form exits fatal.
- **Fix (skeptic: sound):** Read both sides as text with universal newlines: the working file via `open(..., encoding='utf-8')`, and the blob decoded and `.replace('\r\n','\n')`. Spell the revision as `git show <sha>:./id_grammar.py`, and likewise `<seed>:./legacy-records.txt` and `462d20f3:./tree_lib.py` in unit 66 AC14 and AC22.
- **Gate suggestion:** a spec-lint rule: a `git show <rev>:<path>` in an AC must use a repo-root path or `./`, and a byte comparison against the working tree must state its newline handling.

### M13. Three ordering checks read `git log` newest-first output as if it were oldest-first (id 12)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-63.md` §6 AC2 (:118); `2026-10-26-spec-TOOL-dTotalRecall-61.md` AC3 (:172); `2026-10-26-spec-TOOL-dTotalRecall-66.md` AC23 (:310).
- **What is wrong:** Each says plain `git log --format=%s` "lists" or "precedes" unit X's pass commit before unit Y's. `git log` prints newest first, so a correctly ordered X appears after Y.
- **Consequence:** Read literally, each check is red on the correct sequence (54 then 46, 56 then 57, 54 then 45) and green on the wrong one, the opposite of its Red-when.
- **Fix (skeptic: sound):** Spell each check so it does not depend on output order: `git log --reverse --format=%s` lists X before Y, or `git merge-base --is-ancestor <X's pass commit> <Y's pass commit>` exits 0.
- **Gate suggestion:** a spec-lint rule that reds an AC naming `git log` with "before"/"precedes" and without `--reverse` or `--is-ancestor`.

### M14. Unit 66's AC26 is green today and does not observe S34's `TemporaryDirectory` requirement (id 6)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-66.md` §6 AC26, against §2 S34.
- **What is wrong:** S34 asks for the fixtures of unit 59 AC3, unit 60 AC14 and unit 60 AC23 to be made in `tempfile.TemporaryDirectory()`. AC26 greps for `%TEMP%` in `tools/lib/resolve-python.test.sh` and `tools/govkit/selftest.py`, which prints nothing today. Unit 59 AC3's arm lives in `tools/lib/legacy_ledger.py` (spec 59:139), which AC26 does not grep. Unit 60 AC14's fixture is "the scratch clone under `%TEMP%/<short>`" (spec 60:282), with no arm in either file. Only unit 60 AC23 is covered, and only negatively.
- **Consequence:** A unit-66 build that leaves the fixtures where they are passes AC26. S34 is effectively unobserved.
- **Fix (skeptic: the finder's proposal was rejected; this is the skeptic's corrected fix):** Grep for `tempfile.TemporaryDirectory` in each named arm, scoped to its fixture function: `tools/lib/legacy_ledger.py` (unit 59 AC3) and `tools/govkit/selftest.py` (unit 60 AC23). Unit 60 AC14 has no arm, so the ledger line recording that criterion names the `TemporaryDirectory` path it ran in. Make the criterion red on a planted literal scratch path, a probe described for the build.
- **Gate suggestion:** a bug-class checklist entry (fixture-passes-by-finding-nothing): an AC phrased as "prints nothing" must also name a plant that makes it print something.

### M15. S18's list of govkit `.gitattributes` readers misses the rollback, the `check` drift loop and the role tables (id 25)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-66.md` §2 S18 (:88-91), §4 Files touched.
- **What is wrong:** S18 says "every govkit site that reads gov's `.gitattributes` block reads both" and lists five sites (:7703, :7380, :9917, :10459, :12965). These sites also assume one attributes row:
  - the rollback snapshot `_pins_row = pins_write[0] if pins_write is not None else pins_drop` (:10345-10349), taken only when the lf-pin block is written or dropped, and its restore (:11718, :11862);
  - the `check` drift loop (:5596-5645);
  - the dispatch `UPDATE_ROLE['attributes']: 'pins'` (:8489) and `known_roles` (:2733).

  Neither S18 nor unit 60 says which role the new row carries. The skeptic notes that the drift loop handles several rows by `block_id`, so that site alone does not misgrade.
- **Consequence:** An update that changes only the `govkit:generated` block gets no snapshot, so a rollback restores neither its bytes nor its receipt row. Update can dispatch the generated block through the lf-pin recompute. The runbook line WIRE-INTO-PROJECT.md:1407 ("a rollback restores the pre-run index entry") would go stale.
- **Fix (skeptic: sound):** Extend S18's list with the rollback snapshot and restore (:10336-10350, :11718, :11850-11870), the `check` drift loop (:5596-5645) and the `UPDATE_ROLE` / `known_roles` entries (:2733, :8489). State per site whether it keys on `block_id`. Add an AC12 case: a rollback after `update` restores both blocks.
- **Gate suggestion:** a spec-lint rule: a scope item claiming "every site that reads X" must cite the `git grep` that enumerates the sites, with one disposition per hit.

### M16. S36 retires `CAUSE_WRITER_PINNED` but names only two of its readers (id 26)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-66.md` §2 S36 Readers (:137-139), §6 AC28.
- **What is wrong:** S36 moves the constant into a five-field registry row and names only `check_cause_writers` and S26's ask read. Other readers are unlisted:
  - unit 50's plants `pinned-writer-drained` and `departures-pinned` (spec 50:97-98, AC2/AC3), built on the constant's row;
  - unit 53 S35's `--cause-writers` disposition table (53:133), which unit 50 hands the constant to;
  - unit 55's census-keyed drain, which after S36 also grades the moved row. Spec 55:43 deliberately gave the pinned writer no row.

  The skeptic notes that unit 50's ask rule and S1's drain overlap rather than conflict.
- **Consequence:** At unit 66's pass, each of these readers either reds or silently stops grading. AC28 greps only the name and checks `--check`, so it observes none of them.
- **Fix (skeptic: the finder's proposal was rejected; this is the skeptic's corrected fix):** Extend S36's Readers with unit 50's plants `pinned-writer-drained` and `departures-pinned`, which now stage a five-field fixture registry row, and with unit 53 S35's `--cause-writers` disposition. State that S1's census-keyed drain also applies to five-field rows, beside unit 50 S2's ask rule. Add a criterion that `--cause-writers` prints `deviations.py` with its pinned disposition, read from the registry row.
- **Gate suggestion:** the retirement-inventory checklist entry named under M3.

### M17. Unit 66's AC22 grep already matches the spec texts, so it cannot fail on a missing ledger line (id 27)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-66.md` §6 AC22.
- **What is wrong:** `git grep -n "tree_lib.py:410-412" -- memory/builds/dTotalRecall` prints 8 hits at HEAD: specs 60 and 66 and two review records. None is an acceptance-ledger line.
- **Consequence:** AC22 is met before any ledger line exists. It cannot go red on a missing or wrong ledger citation for unit 60's S32.
- **Fix (skeptic: sound):** Scope the grep to the acceptance-ledger record only, by its path or glob under `memory/builds/dTotalRecall/build/`. Require a line carrying both `tree_lib.py:410-412` and `:421`, and state the red as "the ledger file prints no such line".
- **Gate suggestion:** the pre-green check named under H1: an AC grep must print 0 at HEAD when it is meant to observe a line the pass writes.

## Low

### L1. The alias-census half of unit 65's AC2 (and unit 61's AC2) names no command (id 8)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-65.md` §6 AC2 (:139-141); the same shape in `2026-10-26-spec-TOOL-dTotalRecall-61.md` §6 AC2 (:163-165).
- **What is wrong:** The clause hangs the `check_alias_compares` observation on `python record_causes.py --check`. `check_alias_compares` lives in `record_kinds.py` (spec 40:40, :92) and runs under `record_kinds.py --check`.
- **Consequence:** A verifier who reads the clause as part of `record_causes.py`'s output sees no `deviations.py:380` line and reports red. One who greps the whole output for `deviations.py` can match the cause-census row instead. Behaviour does not change.
- **Fix (skeptic: sound):** Spell the second command: "`python record_kinds.py --check` run from `tools/memory-tree/` prints a line naming `deviations.py:380` and `kept pinned instrument`". Match both substrings on one line.
- **Gate suggestion:** a bug-class checklist entry (line-claim-matched-over-the-whole-output): every observed line in an AC names the command that prints it and the substrings that must share the line.

### L2. Unit 63's cited-family fixture conf is under-specified, so a fixture built to the letter raises `ConfError` (id 33)

- **Where:** `2026-10-26-spec-TOOL-dTotalRecall-63.md` §4 "The amendment to unit 46" (:62-64) and §6 AC2 fixture (:115-121).
- **What is wrong:** The fixture is specified only as a `.memory-tree.conf` that declares `RECALL_CITED_FAMILIES` with `ZED`. `recall_conf.resolve`, which `grammar_for(root)` calls, raises `ConfError` with no `MEMORY_ROOT` (:294) or no usable `FAMILIES` (:303), and when a cited family is already in `FAMILIES` (:322-323).
- **Consequence:** A literal fixture raises against both bodies, so the case cannot tell them apart. It is a loud red, never a false green, and unit 54 already built such a fixture.
- **Fix (skeptic: sound):** Spell out the fixture conf in §4 and AC2: `MEMORY_ROOT=memory`, `FAMILIES="tooling:TOOL"` (no ZED), and `RECALL_CITED_FAMILIES="ZED"`. Add a guard to the Red-when: a `ConfError` from the fixture is a fixture fault, not a pass.
- **Gate suggestion:** none beyond the fix. This is a spec-clarity item, and a checklist entry "a fixture conf names every key its resolver requires" covers it.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=33 confirmed=28 refuted=5 unverified=0 blocker=0 high=3 medium=23 low=2 agents=11 out-tokens=195086

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-61.md:section 6 AC1 (against section 2 S2, S3) | high | high | confirmed | I read spec-61:158-162. AC1's only text probe is the grep of 'stays in its constant at this pass' over spec-53. I ran awk over §9 of each spec and grepped for TOOL-dTotalRecall-61. It found a line in 53 (rev-3), 55, 56 and 57 (rev-2). Each is the edge-mirror line ('the Edges block gains the mirror of TOOL-dTotalRecall-61 ...'), so AC1's §9 half is already green today. A unit-61 pass that amends only unit 53 therefore passes AC1, even though its Red-when says 'a spec §4 names is unamended'. Units 55 and 56 would then build without ending their constants. Nothing catches this until unit 57's AC3, which runs after both units have built. I grade it high rather than blocker because AC3 does still catch it downstream. | sound | fixture-passes-by-finding-nothing |
| 2 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-62.md:section 6 AC1 and AC3 (against section 2 S3) | medium | medium | confirmed | spec-62 AC1 checks unit 52's text ('absorbs = ', 'first seed record-kinds-legacy'). For unit 59 it only counts TOOL-dTotalRecall-62 in §9. The awk count over spec-59's §9 found the rev-2 mirror line, so that half is already green. `git grep -n absorbs -- tools/memory-tree/kit.toml` printed nothing (rc=1), and the field can only appear if unit 52 builds it, which AC1/AC2 already police. So no criterion observes S3: spec-59 S2 still reads '`absorbs` is cut' (line 39), and its New arm still says it 'replaces unit 52's absorbed-population arm' (line 139). The effect is contained: a unit-59 builder would follow stale cut text for a field that does not exist. | sound | fixture-passes-by-finding-nothing |
| 3 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 2 S3 Readers line; section 4 Files touched; section 6 AC1 | high | medium | confirmed | spec-57:66-68 designs `for c, p, reason in CENSUS_KEPT_PATHS:` and the message `raise ValueError(f"CENSUS_KEPT_PATHS row {p}: ...`. spec-58:37 gives the remedy 'keep it by a CENSUS_KEPT_PATHS row; its bytes are not this build's', and 58's Files touched are under tools/memory-tree. spec-65:47-49 lists only `read_kept_path` as the by-value reader, and AC1 requires `git grep -n CENSUS_KEPT_PATHS -- tools` to print nothing. The by-name iteration in 57 and the two message strings are unlisted readers. A grep of spec-66 for CENSUS_KEPT_PATHS found nothing, so the batch does not re-word them either. AC1 would red, or a builder would improvise the wording without design text. AC1 does still catch any leftover string, so this is medium. | sound | - |
| 4 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 2 S1 against section 4 'The registry' | medium | medium | confirmed | spec-65:35-36 gives the row as `<census>\t<path>\t<reason>`. Lines 83-84 say the row grammar follows `read_registry` (strip, skip, split). `sed -n 757,776p tools/memory-tree/transition_audit.py` shows `bits = line.split()`, a whitespace split. The reasons contain spaces ('pinned instrument', spec-65:77-78). spec-66:192 classifies rows by field count: 3 fields is a plain keep, 5 a pinned writer. Under a whitespace split, a 'pinned instrument' row has 4 tokens, so it would be refused or misread. The spec's two grammars contradict each other. | sound | two-answers-to-one-question |
| 5 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-64.md:section 4 'The amendment to unit 38'; section 6 AC1 | medium | medium | confirmed | spec-38:3 says order 8 and spec-64:3 says order 9; the README build table puts 38 at step 8 and 64 at step 9. spec-64 §4 'The amendment to unit 38' rev-bumps 38's spec with a §9 line, and AC1 requires `grep -c TOOL-dTotalRecall-64` over 38's §9 to print at least 1. So the edit lands after unit 38's pass. Packet prompt line 52 says 'Every departure ... from a spec after its first pass, is a deviation record'. spec-66:33-34 states 'a landed spec is frozen and is not edited'. spec-64 names no deviation record for the change. The effect is contained: a departures report misses one hand-off-line change. | sound | - |
| 6 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-66.md:section 6 AC26 (against section 2 S34) | medium | medium | confirmed | `git grep -n "%TEMP%" -- tools/lib/resolve-python.test.sh tools/govkit/selftest.py` printed nothing (rc=1), so AC26 is already green. S34 names fixtures for unit 59 AC3, unit 60 AC14 and unit 60 AC23. spec-59:139 puts 59 AC3's arm in tools/lib/legacy_ledger.py, which AC26 does not grep. spec-60:282 says 60 AC14's fixture is 'the scratch clone under `%TEMP%/<short>`; the pass makes it', with no arm in either grepped file. Only 60 AC23 (govkit/selftest.py, spec-60:339) is covered, and only negatively. AC26 does not observe S34's TemporaryDirectory requirement. | unsound | fixture-passes-by-finding-nothing |
| 7 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-66.md:section 6 AC3 and AC24 (against section 2 S5 and S32) | low | - | refuted | Both criteria do print their passing values today: `git hash-object` on deviations.py gave 30a1f15b..., equal to packet.md:74, and `grep -c "census: kept"` printed 0. But each IS the observation its scope item asks for. S5 says unit 56's AC3 is read against the pin the packet records at the tip. 66 AC3 (spec-66:253-255) compares hash-object with the Pins line 'names at HEAD', so it follows an owner's --repin, which is exactly S5's re-reading. S32 says unit 56's AC1 is observed with grep -c, which prints 0. AC24 is that grep -c printing `0`. Unit 56 AC1 (spec-56:103) used `git grep -c`, which prints nothing on no match. Neither S5 nor S32 asks for a ledger line, so the cited sections already make the observation. Both are hold criteria that go red if the instrument moves without a repin or gains a marker. No graded defect remains. | unsound | fixture-passes-by-finding-nothing |
| 8 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 6 AC2; also spec-61 section 6 AC2 | low | low | confirmed | spec-65.md:139-141 reads 'When `python record_causes.py --check` runs ... it lists the eight build-folder files ..., and `check_alias_compares` lists `deviations.py:380` kept `pinned instrument`'. spec-61.md:163-165 has the same shape. spec-40.md:40 and :92 place check_alias_compares in record_kinds.py, and spec-53 AC22 runs it on its own. So the clause names no command for the alias census, and a reader can take it as part of record_causes.py's output. The intent is recoverable from the siblings and nothing in behaviour changes, so the effect is limited to a verifier misreading the check. | sound | line-claim-matched-over-the-whole-output |
| 9 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-61.md:section 6 AC1 (same defect in TOOL-dTotalRecall-62 AC1, -63 AC1 and -64 AC1) | medium | medium | confirmed | Re-probed. Running awk over §9 and grepping for TOOL-dTotalRecall-6x found a rev-2 or rev-3 '§3 · the Edges block gains the mirror of TOOL-dTotalRecall-61...' line already present in units 53, 55, 56 and 57. Units 52 and 59 already carry 62, and unit 46 carries 63 and 64. So every '§9 prints at least 1' half is green at HEAD. The other halves of AC1 check only unit 53 for unit 61 ('stays in its constant at this pass' prints 0 now) and only unit 52 for unit 62 ('first seed record-kinds-legacy' prints 0). Nothing that can fail checks the amendment text for units 55, 56, 57 (spec-61.md:108-116) or for unit 59 (spec-62.md:110). The finder's proposed strings print 0 at HEAD in 55, 56, 57 and 59. | sound | - |
| 10 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-64.md:section 6 AC1, and section 1 (the claim that the edge 'still reads "whose body this unit rebuilds"') | medium | medium | confirmed | Re-ran `grep -nE "read_root_conf\|_id_alternation\(conf\)\|whose body this unit rebuilds"` on spec-46. It hit only lines 73, 75 and 81. `grep -n rebuild` showed line 55 ending 'whose body this unit' and line 56 starting 'rebuilds under its name and signature', so the third alternative can never match. spec-64 §1 names this edge as part of the defect, but AC1 cannot go red if the edge (S3) is left unamended. | sound | ledger-token-wrapped-across-a-line-joins-nothing |
| 11 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-64.md:section 6 AC2 (path form also in TOOL-dTotalRecall-66 AC14 and AC22) | medium | medium | confirmed | In this checkout, `git ls-files --eol tools/memory-tree/*.py` reports 14 w/crlf, core.autocrlf is true and .gitattributes sets `* text=auto`. From tools/memory-tree, `git show HEAD:tree_lib.py` printed "fatal: path 'tools/memory-tree/tree_lib.py' exists, but not 'tree_lib.py'", and `HEAD:./tree_lib.py` works. A Python probe found blob bytes == working-file bytes False, while a text-mode read of the working file equals the decoded blob (True). spec-64 AC2 says 'git show <unit 54's pass commit> of id_grammar.py, run from tools/memory-tree/' and does not fix the path form or newline handling. spec-66.md:289 and :308 use the same 'git show ... of' form. The trap is real but only bites a bytes read or a bare relative rev:path, so its effect is contained. | sound | - |
| 12 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-63.md:section 6 AC2 (same in TOOL-dTotalRecall-61 AC3 and TOOL-dTotalRecall-66 AC23) | medium | medium | confirmed | spec-63 AC2 (line 118), spec-61 AC3 (line 172) and spec-66 AC23 (line 310) each say plain `git log --format=%s` 'lists' or 'precedes' unit X's pass commit before unit Y's. git log prints newest first, which the HEAD log confirms (653bed738 above c235c2e05). Read literally, the check is green when Y was committed first, the opposite of each Red-when ('unit 57 builds before unit 56'). | sound | - |
| 13 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 4 'The registry' (the row grammar), with TOOL-dTotalRecall-66 section 4 'The registry row after S36' | medium | medium | confirmed | In transition_audit.py:763-774, read_registry does `bits = line.split()` (any whitespace) and keeps bits[0] and bits[1]. spec-65.md:84 says the row grammar 'follows read_registry there (:763-774): strip, skip # and blank, split'. Its own rows (lines 77-78) end in the reason 'pinned instrument', which holds a space. spec-66.md:192 tells a plain keep from a pinned writer by field count (three or five). Neither spec 55, 56 nor 65 states a tab-only split. A builder who follows the cited seam would split a 3-field row into 4 fields, so the reason is lost and the 3-or-5 rule misreads it. | sound | - |
| 14 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-64.md:section 2 S1-S3 and section 4 'The amendments to unit 46' (the list of sections amended) | medium | medium | confirmed | spec-46 §1 (lines 26-27) still ends 'This unit rebuilds the parser on that regex.' spec-64 §4's amendment list and its §9 template cover 'S1 S2 S3 §4 §5 §7 §10 §3' and leave out §1. spec-64's AC1 grep does not search for that phrase. After the amendment, unit 46's Goal would contradict its amended S1 ('builds no body'). That is the second-designer prompt H3 exists to remove, though the amended S1, §4 and Files touched each say no body is built. | sound | - |
| 15 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-62.md:section 4 'The amendments to unit 52' (§1 text) and section 10 | low | - | refuted | The premise is false on re-probe. RUN.md pins this run's base, `base: 462d20f3510072a1dddb5b948370937cfd3bbe0e`, with anchor-sha the same value, and the build passes run on this same run branch. `git merge-base HEAD origin/main` still prints 462d20f3, even with origin/main 189 commits ahead (c53e4eb30). Main moving does not change the run's merge-base, so 'this run's compare base 462d20f3' names the base the build run is judged at. The units also carry `base 462d20f3` in their status lines. | sound | - |
| 16 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 2 S1-S2, section 4 'The registry', section 10 | high | high | confirmed | Confirmed on read. Spec 65 §4 and §10 make transition_audit.read_registry (transition_audit.py:759-774, a hand parser) the seam for a new memory/project/census-kept-paths.txt, and the spec names no [[ledger]] registration. The parent build dWitnessedBar is declared in README `parents:`. Its unit dWitnessedBar-16 derives its population as `memory/project/*.txt` (S1). Its S4 says 'no reader keeps a parser of the old grammar', its §4 table converts `transition_audit.read_registry (:763)` itself, and its AC1 is red when 'a registry the rule finds has no registration'. This build already registers project homes as [[ledger]] populations (unit 19 S7 legacy-records, unit 52 via legacy_ledger.py). So the new keep list is unratcheted, and its cited seam is one the parent rewrites. | unsound | - |
| 17 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 4 'The registry' (row grammar sentence) | medium | medium | confirmed | Confirmed. `sed -n 763,774p tools/memory-tree/transition_audit.py` shows `bits = line.split()`, which splits on any whitespace and keeps only bits[0] and bits[1]. Spec 65 S1 makes the row `<census>\t<path>\t<reason>`, and its §4 sample reason is 'pinned instrument', which contains a space. §4 says the grammar 'follows read_registry there (:763-774): strip, skip # and blank, split'. Unit 66 §4 tells a plain keep from a pinned writer by field count ('three fields ... five'). A builder who follows the cited reader cuts the reason and miscounts the fields. AC2 would catch this at the pass, so the effect is contained. tools/gate-lint/sh_hygiene.py:402 read_registry documents a TAB-separated row grammar, so it is a valid precedent. | sound | - |
| 18 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 1 ("It repairs TOOL-dTotalRecall-55, at the step after it"), section 4 Alternatives rejected | medium | medium | confirmed | Confirmed. Spec 55 is `OPEN · rev-2 · order 30`. Its rev-2 log reads 'the Edges block gains the mirror of ... TOOL-dTotalRecall-65 ...; nothing else moved'. S1 still designs `CENSUS_KEPT_PATHS` in tree_lib.py and `read_kept_path(census, path)`, and :101 mints both. Spec 65 (order 31) then removes the table, and its AC1 requires `git grep CENSUS_KEPT_PATHS -- tools` to print nothing. Spec 64 rejects this pattern by name ('An edge-fold on unit 46 alone. It is what left S1 and §4 standing'), and spec 61 calls two units designing one body H3's defect. Unit 57 (order 30) has a criterion that probes `tree_lib.CENSUS_KEPT_PATHS` (spec 57:115), and that criterion goes red after unit 65. | unsound | - |
| 19 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-62.md:section 10 Reuse audit | medium | - | refuted | The premise is false on re-probe. Spec 62 §10 reads '`compare_to_base` at `resolve_compare_base` (`tools/codebase-map/map_lib.py:1502`)'. The parenthetical is attached to resolve_compare_base, and `git grep` shows that function at exactly map_lib.py:1502. dWitnessedBar-13 uses the same phrasing ('the rows at resolve_compare_base(root)'s SHA'). Spec 62 §4 AC2 names `compare_to_base` from `legacy_ledger.py` run from `tools/lib/`, and its §3 cites TOOL-dWitnessedBar-51 S30. dWitnessedBar is declared a parent build in the README (`parents: dDeclaredLoop dWitnessedBar dPlacedRequest`), so the dependency on the parent's file is declared. | sound | - |
| 20 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-66.md:section 2 S22 and S34 (with S8 and the section 7 New arm over tools/lib/resolve-python.test.sh) | medium | - | refuted | The premise is false on re-probe. Unit 59 §4 Inventory mints the plant `merged-home-gained` in `legacy_ledger.py`'s self-test, and its AC3 is a python probe run in a fixture. The fixture builder is Python, so a Python environment scrub and TemporaryDirectory are the matching idiom, not a sibling kit's code read at runtime. S22 and S34 cite branch-reconcile and codebase-map with 'as ... does', which is a precedent, not an import. Section 2d's scrub (resolve-python.test.sh:330/332) is an inline per-command `env -u`, not a shared seam to extend. The finding names a preference, not a graded defect. | unsound | - |
| 21 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 2 S1; section 4 Files touched; section 7; section 8 | high | high | confirmed | Confirmed. SESSION-KICKOFF.md:6 `watch:` lists `.memory-tree.conf`. manifest-check.sh:1462-1473 runs `git rev-list -1 "$LA_SHA..HEAD" -- "${WATCH[@]}"` and calls `fail 5` when no re-stamp sits at or after the change. In tools/gate-legs.json the `kickoff-manifest ratchet` row has no guard key, so it runs on every bar. Spec 60 S22 re-stamps over unit 52's conf edit under its §8 F2 grant. Spec 65 S1 then edits `.memory-tree.conf` (PROJECT_REGISTRY_EXTRA), and its §4 says M6 sequences that pass after unit 60's. Spec 65's Files touched, §7 and §8 name no re-stamp, no manifest leg and no grant. Spec 66's Files touched lists neither the conf nor SESSION-KICKOFF.md. The bar is therefore red from unit 65's pass to the close. | sound | - |
| 22 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 2 S3 Readers; section 6 AC1 | medium | medium | confirmed | Re-ran `git grep -n CENSUS_KEPT_PATHS -- memory/builds/dTotalRecall/spec`. Spec 57:66-68 builds the loop `for c, p, reason in CENSUS_KEPT_PATHS:` with the error text `CENSUS_KEPT_PATHS row {p}: ...`. Spec 58:37 has the shipped remedy `keep it by a CENSUS_KEPT_PATHS row; its bytes are not this build's`. Spec 57 AC1 builds 'a fixture whose table holds a row'. Spec 56:118 stages `unkept-build-alias` by 'skipping the table read', and spec 55 plants `kept-row-drained`. Spec 65:47-49 calls `read_kept_path` 'its one reader' and names none of the other carriers. AC1 (`git grep CENSUS_KEPT_PATHS -- tools` prints nothing) therefore goes red until the builder edits text the spec never names, and the spec gives no wording for the adopter-facing remedy. The effect is contained because AC1 forces the edit, so medium. | sound | retirement-inventory-misses-readers-by-value |
| 23 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 4 The registry (row grammar); section 5 error states | medium | - | refuted | duplicate of id=28. It is the same defect. Spec 65:84 says the rows follow `read_registry` ('strip, skip # and blank, split'), and at transition_audit.py:771 that reader does `bits = line.split()`, a whitespace split. That breaks the multi-word reasons in the tab-separated `<census>\t<path>\t<reason>` rows, leaves §5's 'fewer than three fields' rule unreachable, and makes unit 66's arity test (3 against 5) misread rows. I confirmed it under id=28. | sound | - |
| 24 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 4 Why the project layer; section 5 user docs; section 4 Files touched | medium | medium | confirmed | In check-memory-hygiene.sh:736-753, check 3's closed `memory/project/` whitelist admits `pass-order-waiver.txt` and `role-stand-in-waiver.txt` by name because a kit reads them at their DEFAULT path. It also says PROJECT_REGISTRY_EXTRA is the escape for a registry a project adds. Anything else falls through to the bare refusal 'unexpected entries (structure)' (:762-777), which gives no remedy. tools/memory-tree/README.md:562 documents the EXTRA step for `refusal-retirements.txt`. Spec 65 has the shipped engine read `<M>/project/census-kept-paths.txt` at its default path, and :91-92 tells an adopter it 'writes its own registry'. Its files-touched list (:106-111) has no whitelist change and no README or HYGIENE doc change, and :131 says user docs are 'none'. An adopter who creates the file as told gets an unexplained red check 3. The non-goal 'a kit-shipped registry' withholds shipping the file, not declaring or documenting its name, so it does not cover this. | sound | shipped-checker-edit-is-an-adopter-contract-change |
| 25 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-66.md:section 2 S18; section 4 Files touched | medium | medium | confirmed | S18 (spec 66:88-91) claims 'every govkit site that reads gov's .gitattributes block reads both' and lists five sites. `git grep -n '"attributes"' tools/govkit/govkit.py` reproduces the finder's 13 lines. At :10345-10349 the rollback snapshot is `_pins_row = pins_write[0] if pins_write is not None else pins_drop`, taken only when the lf-pin block is written or dropped. An update that changes only the `govkit:generated` block (unit 60 S23 gives it its own writer and receipt row) therefore gets no snapshot, so the rollback (:11718, :11862) restores neither its bytes nor its row. The `check` drift loop (:5604-5647) and the dispatch `UPDATE_ROLE['attributes']: 'pins'` (:8489) both act by role, and neither S18 nor unit 60 says which role the new row carries. One correction to the finder: the drift loop handles several attributes rows by block_id, so that site alone does not misgrade. The list is still incomplete, and the rollback gap can be reached. | sound | - |
| 26 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-66.md:section 2 S36 Readers; section 6 AC28 | medium | medium | confirmed | S36's Readers (spec 66:137-139) names only `check_cause_writers` and the S26 ask read. Other readers exist. Spec 50:97-98 and AC2/AC3 build the fixture plants `pinned-writer-drained` and `departures-pinned` on the constant's row. Spec 50:68 hands `CAUSE_WRITER_PINNED` to unit 53, whose S35 `--cause-writers` (53:133) prints the census table with dispositions. Spec 50 AC1 lists deviations.py 'under CAUSE_WRITER_PINNED'. Spec 55:43 gives the pinned writer no row. AC28 only greps the name and checks `--check`, so it observes none of these. One part of the claim is overstated. Unit 50 S2 reds a pinned row whose instrument spells Caused-by, and S1's cause-line arm does the same, so the two drains overlap rather than conflict. | unsound | retirement-inventory-misses-readers-by-value |
| 27 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-66.md:section 6 AC22 | medium | medium | confirmed | I re-ran `git grep -n "tree_lib.py:410-412" -- memory/builds/dTotalRecall` at HEAD. It printed 8 hits: two review records (44 round-1 :289 and :291, 54 round-1 :267 and :399), spec 60:99 and :135, and spec 66:118 and :307. None is an acceptance-ledger line. Because the grep's population includes the spec texts themselves, AC22's grep half is already met before any ledger line exists. The criterion's prose names 'the ledger line', but the mechanical check cannot red on a missing or wrong ledger citation. Contained to one L1 citation item, so medium. | sound | - |
| 28 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 2 S1 and section 4 'The registry' (row grammar), with section 5 error states | high | medium | confirmed | Spec 65:35-36 declares rows as `<census>\t<path>\t<reason>`. Then :82-84 says the grammar 'follows `read_registry` there (`:763-774`): strip, skip `#` and blank, split'. `sed -n 750,780p tools/memory-tree/transition_audit.py` shows that reader does `bits = line.split()`, splitting on any whitespace. Spec 55:44-46 gives the reasons `pinned instrument` and `outside the write set`, so a builder who follows the cited reader cuts the reason down. §5 (:124) handles only 'fewer than three fields', so rows with 4 or 6+ fields go undefined. Unit 66:192 tells a plain row from a pinned writer by arity (3 against 5). Graded medium rather than high: spec 65's AC2 expects `kept pinned instrument` printed whole, so a whitespace-split build would likely red at the pass, which contains the effect. | sound | - |
| 29 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 2 S1/S2 and section 5 error states | medium | medium | confirmed | Unit 65 S1 (lines 35-38) defines the row as `<census>\t<path>\t<reason>`. §5 line 124 refuses only a malformed row with fewer than three fields. Neither restricts the census value or rejects a repeated (census, path) key. Unit 66 S1 and S3 (lines 36-44) drain only `check_cause_writers` and `check_alias_compares` rows. Unit 66 S36 adds five-field rows but sets no census domain and no uniqueness rule either. A grep of units 55-57, 65 and 66 for duplicate/repeat/unknown-census wording found nothing that does this. So a row with a typo in its census name is drained by nothing, and a duplicate key resolves to whichever row the builder's reader happens to pick. The effect is contained to stale keeps, so medium. | sound | - |
| 30 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md:section 6 AC1 | medium | medium | confirmed | Unit 65 AC1 (lines 135-138) runs `git grep -nE "memory/builds/[A-Za-z]+/"` over `tree_lib.py` only, while Files touched also names `record_causes.py` and `record_kinds.py`. Unit 50 §4 (lines 88-91) mints `CAUSE_WRITER_PINNED` in `record_causes.py` holding the dClosedLoop deviations.py literal. Unit 66 AC28 (line 320) greps only the constant's name. So a literal inlined when S36 dissolves the constant is caught by no criterion. The unit-65 non-goal defers only a lint gate, not the pass criterion. At base, `git grep` of the build slugs in tools/memory-tree (excluding selftest and test files) prints nothing, so the check is satisfiable at the end. | unsound | - |
| 31 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-61.md:section 6 AC1 (and the same shape in unit 62 AC1, unit 63 AC1, unit 64 AC1) | medium | medium | confirmed | I re-ran the awk/grep over each §9. Units 53, 55, 56 and 57 each already carry a rev line naming TOOL-dTotalRecall-61 ('the Edges block gains the mirror of TOOL-dTotalRecall-61, ...'). Units 52 and 59 carry -62, and unit 46 carries -63 and -64. All of these are present before any pass, so AC1's §9 half is already green. Unit 61 AC1's content half checks only unit 53, with `stays in its constant at this pass`, which currently counts 0. Unit 62 AC1 checks only unit 52. So nothing at the amending pass observes the amendments to units 55, 56, 57 (S2, S3) or to unit 59. Unit 61 AC3 catches only part of this, and only later, at unit 57's tip. | sound | - |
| 32 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-64.md:section 6 AC2 and section 6 AC1 | medium | medium | confirmed | Unit 46 line 70 defines `SUFFIX_RE` in its §4 code block, and line 88 reads 'Minted: `SUFFIX_RE` in tools/memory-tree/id_grammar.py'. Unit 64 §4 amends that Inventory to 'Minted: nothing.' However, unit 64 AC1's pattern `read_root_conf\|_id_alternation\(conf\)\|whose body this unit rebuilds` does not match line 88; it counts 3 today, all from the code block. Unit 64 AC2 compares only the `parse_id_parts` segment. Unit 54 §4 (lines 89-93, 113) mints both `parse_id_parts` and `SUFFIX_RE`. So the Inventory amendment goes unobserved, and so does a rebinding of `SUFFIX_RE` in id_grammar.py. Either one leaves the compared function segment byte-equal. | sound | - |
| 33 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-63.md:section 4 'The amendment to unit 46' and section 6 AC2 fixture | low | low | confirmed | Unit 63 §4 (lines 62-64) and AC2 (lines 115-121) specify the fixture only as a conf declaring `RECALL_CITED_FAMILIES` with ZED. `recall_conf.resolve` (lines 277-323) raises ConfError for no MEMORY_ROOT (line 294) and for no usable FAMILIES (line 303). It also raises ConfError for a cited family already in FAMILIES (lines 322-323). `extract.grammar_for` calls `recall_conf.resolve(pathlib.Path(root))`. A fixture built to the letter therefore fails loudly against both bodies, a red and never a false green. Unit 54 already built such a fixture, so the builder will likely fill the gap. The defect is spec clarity only, so low. | sound | - |
