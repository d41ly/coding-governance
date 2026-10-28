# TOOL-dIndexedDesign-2 — the design index: overlaps between live designs, as `design.overlap` says

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 6 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0384@372bd58d whole
**Carries:** node:item.design.overlaps
**Carries:** node:policy-key.design.overlap
**Carries:** node:record-kind.overlap

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-16 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |

<!-- /gen:spec-records -->

## 1. Goal

Two live designs in different builds that declare the same path are invisible to each other today
(gap-design-02): the one cross-run probe reads unmerged remote refs only and never refuses. This unit
joins every live spec's write set across builds on the default branch, lets a spec acknowledge an
overlap in its §3 Edges, and acts on an unacknowledged one as the policy key `design.overlap` says:
`warn` at spec-write and kickoff, `refuse` until acknowledged, or `index-only`, shown in the index
view alone.

## 2. Scope (IN)

- **S1** — The join, `derive_design_overlaps(root, files, subjects=None)` in
  `tools/memory-tree/design_lib.py`: over every tracked spec whose status is not CLOSED or WONTDO,
  DEFERRED included (I7), one row per pair of units in different builds whose write sets meet by
  `check_writes_intersect` over `read_spec_writes`, per shared path, each row
  `(unit a, unit b, path, acknowledged)`. A write-set token is a path when it carries a `/` or an
  extension; a one-segment directory such as `tools/` declares nothing, the reading
  `check_dir_shaped` gives the guard join. With `subjects`, only pairs with a side among those spec
  paths. Observed by AC1.
- **S2** — The acknowledgement: a §3 `### Edges` bullet `**overlaps**` whose backticked payload is the
  other unit's id, which acknowledges that pair, or a path, which acknowledges every pair on that path;
  either side's bullet acknowledges the pair. Read through `read_spec_edges(text, "overlaps")`. Check 12
  admits the verb, takes a unit id of any build or a path as its payload, and holds it out of the
  mirror and order joins, because one side's word is the acknowledgement. Observed by AC2, AC7.
- **S3** — The spec-write arm, an `overlap` arm in `tools/check-spec-tokens.py`: it reads
  `read_design_policy("design.overlap", root)` (I3) and runs S1 with the LIVE specs it already grades
  as subjects. Under `warn` it prints one `spec-tokens: overlap ·` line per subject spec with an
  unacknowledged pair, naming its count, its first three paths and the other builds, and leaves the exit
  status alone; under `refuse` the same lines exit 1; under `index-only` it prints one line saying the
  arm reads nothing at spec-write. Observed by AC3.
- **S4** — The kickoff point: `print_overlaps` in `tools/unattended/unattended.sh` appends a design-index
  block after its unmerged-ref probe. It reads `design.overlap` through I3's shell form, spelled
  `"$_ovpy" "$_ovpol/policy.py" get design.overlap`, and runs `design_lib.py --overlaps` over the specs
  its own diff changed, the rule `check_cross_run_overlap ""` uses for its own paths, or, with none,
  prints the LIVE population's unacknowledged count and points at `memory/LIVE.md`. Under
  `index-only` it prints one line naming that value. The card's `overlaps —` cell prints the driver's
  output as it does today (`skills/session-kickoff/manifest-check.sh:555-589`), so the card is unchanged.
  Observed by AC4.
- **S5** — The index view: `render_live` (`tools/memory-tree/gen_build_index.py:2079`) gains a
  `## Design overlaps` section in `memory/LIVE.md`, one line per build holding an unacknowledged pair:
  `- <build> · <n> unacknowledged unit pair(s) · with <build>, … · paths: <first three>`, or the single
  line `none`, rendered under every value of `design.overlap`. Observed by AC5.
- **S6** — The overlap record, kind `overlap`, written by `design_lib.py --overlaps --record <slug>`
  for the build's roster: `memory/builds/<slug>/build/<date>-build-<first unit id>-overlap-<n>.md`, its
  Serves line naming each unit of the build with a row, one row per pair
  `- <unit id> · <unit id> · <path> · acknowledged|unacknowledged`, the value of `design.overlap` and
  the commit it read; `<n>` the next free sequence. Observed by AC6.
- **S7** — The kind registered through `record_kinds.py new overlap --tag record.overlap`
  (TOOL-dTotalRecall-1 S9), node `record-kind.overlap`. Observed by AC9.
- **S8** — The catalogue row of `design.overlap` (`tools/policy/catalogue.toml:925-929`) gains its
  `summary` and `usage`, and `python tools/policy/policy.py lists --write` drains its name from
  `tools/policy/unsummarised-keys.txt`; the values `warn`, `refuse`, `index-only` and the default
  `warn` stay as written. S3's and S4's calls are its literal readers. Observed by AC8.
- **S9** — The docs: the §3 section of `tools/memory-tree/SPEC-TEMPLATE.template.md` and its render
  `memory/TEMPLATE-SPEC.md` state the third verb and its payloads; the `--overlaps` entry of
  `tools/unattended/VERBS.template.md`, copied to `memory/guides/UNATTENDED-VERBS.md`, names the
  design-index block; `help/policy.md` names the key's consumers; `tools/memory-tree/README.md` names
  the join, the arm and the record; `KIT_MEMORY_TREE_VERSION` and `KIT_UNATTENDED_VERSION` move.
  Observed by AC10.

## 3. Non-goals (OUT)

- Overlaps inside one build: `derive_parallel_step` (`gen_build_index.py:1724`) and `--dispatch`'s
  disjointness rule already sequence them.
- Overlaps with unmerged remote refs: `check_cross_run_overlap` keeps that probe unchanged.
- The stream plan that reads the overlap record: TOOL-dIndexedDesign-15. The agreement axes and the
  unpushed-spec read that announce pairs in its row grammar: TOOL-dIndexedDesign-6.
- Routing an unacknowledged overlap back to `design.decompose` as an item move: the loop engine's
  transition, dDeclaredLoop's; this unit's refusal is the checker's exit at spec-write and at
  `--dispatch`, which runs the same checker.
- The lease granularity `leases.overlap` (dPlacedRequest's key), §4 "Alternatives rejected".
- The policy reader itself: TOOL-dIndexedDesign-16 owns I3.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-16` — `read_design_policy`, I3, which S3 calls with `design.overlap` and whose shell form S4 spells `policy.py get design.overlap`
- **hands-off** `TOOL-dIndexedDesign-6` — `record.overlap`, the row grammar and the `**overlaps**` acknowledgement its unpushed-spec read announces pairs in, through S1's join
- **hands-off** `TOOL-dIndexedDesign-15` — `record.overlap`, the overlap record the stream planner reads beside the order and the write sets
- **consumes-from** external — TOOL-dTotalRecall-1 S9's `record_kinds.py new` and TOOL-dDeclaredLoop-12 S2's `[[item]]` row for `item.design.overlaps`, each DEFERRED at base and built before this build run

## 4. Design

### Evidence

Read at `4bf0f400d`; no product file differs from base `57bc3b91`.

- `check_writes_intersect` and `check_guard_trips` (`tools/memory-tree/design_lib.py:589-605`) are the
  one containment rule the build-order render and `--dispatch` share; `read_spec_writes` is at `:528`
  and `read_spec_edges` at `:543`, which reads any `**<verb>**` bullet under `### Edges`.
- Check 12's edge pass refuses any head but `consumes-from` and `hands-off`
  (`tools/memory-tree/check-memory-hygiene.sh:2569`) and demands each edge's mirror from a sibling of
  the same build (`:2809-2811`).
- `check-spec-tokens.py` grades the LIVE specs, `OPEN|SPECCED|INPROGRESS|BLOCKED` (`:331`), and
  `--dispatch` runs it before admitting a pass (`unattended.sh:13670-13680`).
- `print_overlaps` (`unattended.sh:3523-3540`) calls `check_cross_run_overlap ""`, which reads only
  unmerged remote refs and prints "this run is NOT blocked" (`:3514`).
- Measured over the 816 tracked non-terminal specs at `4bf0f400d` (PINNED; a probe of S1's rule,
  re-derived by S1 at the pass):

| Population | Cross-build unit pairs |
|---|---|
| every non-terminal spec, one-segment roots read as paths | 38,375 |
| the same, roots declaring nothing | 36,098 |
| the same, a LIVE side on at least one end | 3,386, over 194 build pairs |
| neither side DEFERRED | 133 |

  The most-paired LIVE spec carries 331 pairs; `tools/unattended/unattended.sh` is declared by 118
  non-terminal specs in 13 builds, and `tools/gate-legs.json` alone joins 5,275 pairs.

### The policy table

| Value | Spec-write (S3) | Kickoff (S4) | Index view (S5) | Overlap record (S6) |
|---|---|---|---|---|
| `warn`, the default | lines, exit unchanged | lines | rendered | written on demand |
| `refuse` | lines, exit 1 | lines | rendered | written on demand |
| `index-only` | one announce line | one announce line | rendered | written on demand |

Under `refuse` the exit reaches the commit that runs the checker and every `--dispatch`, so a unit
with an unacknowledged overlap is not built until a bullet acknowledges it. A refused policy read is a
refusal in S3 and an `UNAVAILABLE` line in S4, never a guessed value.

### The acknowledgement

```markdown
### Edges

- **overlaps** `TOOL-dOtherBuild-4` — both write the probe's table; this unit appends a row only
- **overlaps** `tools/unattended/unattended.sh` — every live design touching the driver, sequenced by build order
```

The payload is the first backticked token, as `read_spec_edges` reads it. A token matching the house
id shape is a unit; any other is a path, acknowledging each pair whose shared path it trips by
`check_guard_trips`. Check 12 grades the bullet's shape and a non-empty payload, and nothing else: an
acknowledgement names another build's unit, which the mirror join cannot see, and its prose is the
author's reason.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_design_overlaps` | function, `design_lib.py` | `py.function`, asked at the pass |
| `--overlaps`, `--record` | CLI verb and flag of `design_lib.py` | none |
| `overlaps` | §3 edge verb | none |
| `overlap` | arm of `check-spec-tokens.py` | none |
| `## Design overlaps` | section of `memory/LIVE.md` | none |
| `overlap`, `record.overlap` | record kind and tag, node `record-kind.overlap` | none |
| `…-overlap-<n>.md` | record filename grammar | none |

### Migration

None: no spec gains a bullet. The first render of `memory/LIVE.md` shows the population §4 measures;
each build acknowledges its own pairs as its specs are next written.

### Rollout

Live at landing under the catalogue default `warn`, the owner's D2 answer (walkthrough:441-443).
`refuse` is a committed policy value; with 3,386 LIVE-side pairs at `4bf0f400d` it reds every LIVE
spec until each acknowledges its paths, which §5 names.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S1, S6, the `--overlaps` CLI
- `tools/check-spec-tokens.py`: S3
- `tools/check-spec-tokens.test.sh`: S3's arm cases
- `tools/memory-tree/gen_build_index.py`: S5 and its selftest arm; `memory/LIVE.md` re-rendered
- `tools/memory-tree/check-memory-hygiene.sh`: S2's verb, `KIT_MEMORY_TREE_VERSION`
- `tools/memory-tree/check-memory-hygiene.test.sh`: S2's arm cases
- `tools/memory-tree/SPEC-TEMPLATE.template.md` and its render `memory/TEMPLATE-SPEC.md`: S9
- `tools/unattended/unattended.sh`: S4, `KIT_UNATTENDED_VERSION`
- `tools/unattended/unattended.test.sh`: S4's arm cases
- `tools/unattended/VERBS.template.md` and its copy `memory/guides/UNATTENDED-VERBS.md`: S9
- `tools/memory-tree/record-kinds.toml`: S7's row, through its factory
- `tools/policy/catalogue.toml` and `tools/policy/unsummarised-keys.txt`: S8
- `help/policy.md` and `tools/memory-tree/README.md`: S9

### Alternatives rejected

- **The granularity `leases.overlap` names, `kit-dirs` by default** (walkthrough:415-418). Lost to
  measurement: S1's file rule already yields 36,098 pairs, and a kit-directory rule joins every pair of
  specs under one kit; the key is dPlacedRequest's, no ancestor of this build.
- **The shell `read_files_touched` and `overlaps` as the join.** Lost to I16: the Python join is the
  one the checker, the generator and the record share, and a fourth reader is what I16 forbids.
- **Build ancestry as an acknowledgement.** Lost to measurement: of the 3,386 LIVE-side pairs, none sits
  between a build and its ancestor at `4bf0f400d`, so `parents:` acknowledges nothing where it matters.

## 5. Production-readiness checklist

- security — N/A for a new surface: the join reads tracked specs and the record writer writes one file
  under the named build's folder; the policy file is read at the landed revision.
- perf / scale — S1 with subjects is linear in the population times the subjects; the full join for
  S5 is quadratic over about 800 specs, measured in seconds by the probe of §4.
- error / empty / loading states — no subject spec prints the population count; a spec with no Files
  touched joins nothing and is counted; a refused policy read refuses in S3.
- observability — every line names the unit, the count, the paths and the other builds; S5 renders on
  every `--write`.
- risks — `refuse` at today's population reds every LIVE spec with an overlap until it acknowledges;
  `warn` prints one line per such LIVE spec, 36 at most at `4bf0f400d`.
- testing — the arms of §7 over a two-build fixture with planted overlaps and acknowledgements.
- migration — none.
- user docs — `memory/TEMPLATE-SPEC.md`, `memory/guides/UNATTENDED-VERBS.md` and `help/policy.md`.

## 6. Acceptance criteria

- **AC1** — When `python design_lib.py --overlaps` runs in a fixture repository of builds tA and tB,
  where `TOOL-tA-1` and a DEFERRED `TOOL-tB-1` write `<root>/<path-a>`, `TOOL-tB-2` writes the root `<root>/`,
  `TOOL-tB-3` writes `<root>/<dir>/` beside `TOOL-tA-1`'s `<root>/<dir>/<path-b>`, a CLOSED `TOOL-tB-4` writes `<root>/<path-a>`
  and a DEFERRED `TOOL-tA-2` writes `<root>/<path-a>` too, it prints exactly the rows `TOOL-tA-1 · TOOL-tB-1 · <root>/<path-a>`,
  `TOOL-tA-2 · TOOL-tB-1 · <root>/<path-a>` and `TOOL-tA-1 · TOOL-tB-3 · <root>/<dir>/<path-b>`, each `unacknowledged`.
  Red when: a DEFERRED side is dropped, the root joins, a CLOSED side joins, or a same-build pair prints.
  fixture: the suite builds the repository; none exists in the tree. `<root>` is a one-segment
  directory, `<path-a>` a file directly under it and `<dir>/<path-b>` a file one level down, each a
  name the suite picks.
- **AC2** — When `TOOL-tA-1`'s §3 gains `**overlaps**` naming `TOOL-tB-1`, that row reads
  `acknowledged` and the other two do not; when `TOOL-tB-1` instead names the path `<root>/<path-a>`, both
  `<root>/<path-a>` rows read `acknowledged`.
  Red when: either side's bullet fails to acknowledge, or a path bullet acknowledges a pair on another
  path.
  fixture: as AC1.
- **AC3** — When `python tools/check-spec-tokens.py` runs in the AC1 repository with an OPEN `TOOL-tA-1`
  and no policy file, it prints one `spec-tokens: overlap` line naming `TOOL-tA-1`, its two
  unacknowledged pairs and build tB, and the overlap arm leaves the exit status alone; with a committed
  `.governance/policy.toml` setting `design.overlap` to `refuse`, the same run exits 1; once
  `TOOL-tA-1`'s §3 acknowledges the paths `<root>/<path-a>` and `<root>/<dir>/<path-b>` it exits 0; under `index-only` it
  prints the one announce line and no pair.
  Red when: the planted unacknowledged overlap under `refuse` exits 0, which is the clause's planted case.
  fixture: as AC1; the policy file is committed because `get` reads the landed revision.
- **AC4** — When `bash unattended.sh --overlaps` runs in a clone of the AC1 repository whose own diff
  changed `TOOL-tA-1`'s spec, its output's design-index block names `TOOL-tA-1` and `TOOL-tB-1` under
  `warn` and under `refuse`, and prints only the `index-only` line under `index-only`; with no spec in
  the diff it prints the LIVE population's count and names `memory/LIVE.md`.
  Red when: kickoff shows nothing for an unacknowledged overlap under `warn`.
  fixture: the driver suite's clone with one remote and a set `refs/remotes/<remote>/HEAD`.
- **AC5** — When `python gen_build_index.py --write` runs in the AC1 repository, `memory/LIVE.md` carries
  `## Design overlaps` with one line for tA naming 3 unacknowledged unit pairs with tB, and one for tB;
  after `TOOL-tB-1` acknowledges the path `<root>/<path-a>` the tA line reads 1; with every pair acknowledged the section reads
  `none`.
  Red when: an unacknowledged pair is missing from the view, or the view varies with `design.overlap`.
  fixture: as AC1.
- **AC6** — When `python design_lib.py --overlaps --record tA` runs twice in the AC1 repository, it
  writes `…-TOOL-tA-1-overlap-1.md` and then `…-overlap-2.md`, each holding the three rows of AC1 in
  the S6 grammar, the value of `design.overlap` and the commit read, its Serves line naming
  `TOOL-tA-1` and `TOOL-tA-2`.
  Red when: a row is missing or the second run overwrites the first.
  fixture: as AC1.
- **AC7** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 12` runs over a fixture spec
  whose §3 carries `**overlaps**` naming a unit of another build, check 12 passes it and demands no
  mirror; a bullet headed `**overlap**` and an `**overlaps**` bullet with no payload each red.
  Red when: the verb reds, demands a mirror, or a misspelled head passes.
  fixture: the hygiene suite's spec fixture, `SPEC_EDGES_CUTOFF` and `SPEC_FORMAT_CUTOFF` set.
- **AC8** — When `python tools/policy/policy.py get design.overlap` runs with no policy file it prints
  `warn`; after `policy.py lists --write`, `grep -c design.overlap tools/policy/unsummarised-keys.txt`
  prints 0; `git grep -c 'read_design_policy("design.overlap"' -- tools/check-spec-tokens.py` and
  `git grep -c 'policy.py" get design.overlap' -- tools/unattended/unattended.sh` each print at least 1.
  Red when: the row lacks `summary` or `usage`, or either literal reader is missing.
- **AC9** — When `python record_kinds.py --check` runs at this unit's tip, it passes with the `overlap`
  row present, tagged `record.overlap`.
  Red when: the row is missing or its tag differs.
  fixture: the registry is TOOL-dTotalRecall-1's, absent at base until it lands.
- **AC10** — When `grep -n "overlaps" memory/TEMPLATE-SPEC.md` runs, it prints the §3 section's
  sentence naming the third verb and its two payloads, and `tools/memory-tree/SPEC-TEMPLATE.template.md`
  carries the same bytes; `grep -n "design.overlap" memory/guides/UNATTENDED-VERBS.md` prints the
  `--overlaps` entry's sentence.
  Red when: a render differs from its template, or a payload form is unnamed.

## 7. Gates

`build-index selftest` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `memory hygiene` · `policy check` · `policy fixtures` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `unattended kit gate` · `manifest-check self-test` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 AC3 · the two-build fixture under each committed value of `design.overlap`, its failing case the unacknowledged overlap under `refuse` exiting 0 · none

New arm: tools/memory-tree/gen_build_index.py · covers AC5 · the `--selftest` arm rendering the LIVE section before and after an acknowledgement, its failing case an unacknowledged pair absent from the view · none

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC7 · a spec carrying `**overlaps**` to another build, a misspelled head and an empty payload, its failing case the verb demanding a mirror · none

New arm: tools/unattended/unattended.test.sh · covers AC4 · `--overlaps` in a clone whose diff changed a spec with an unacknowledged overlap, under each value, its failing case no design-index line under `warn` · none

## 8. Open questions

- **F1 — Which specs are live designs?** Options: (a) every non-terminal spec, DEFERRED included, as I7
  states, each signal scoped to its subjects: the LIVE specs at spec-write, the session's own specs at
  kickoff, and every build in the index view; (b) the LIVE set alone. Measured at `4bf0f400d`: (b)
  yields 133 pairs and is blind to every harness-run build, whose unit specs sit DEFERRED until their
  build commit closes them, so the index would miss the chain builds that overlap most. RESOLVED (agent,
  2026-10-28, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What does an acknowledgement name?** Options: (a) the other unit's id or a shared path, the
  path acknowledging every pair on it; (b) the other unit's id only, as I7 proposed. (b) asks the
  most-paired LIVE spec for 331 bullets, and a new unit writing the driver for up to 117. RESOLVED
  (agent, 2026-10-28, delegated): (a), rung 3, the most feature-rich survivor; this unit owns I7 and
  refines it here. widens: none · relaxes: none
- **F3 — Where does the index view render?** Options: (a) a `## Design overlaps` section of
  `memory/LIVE.md`, one line per build; (b) a `GEN_REGIONS` region in every build README; (c) a new
  generated file at the memory root. (b) writes each pair into two READMEs and re-renders every README
  at landing; (c) is a new root file hygiene check 3 must admit, for a population `memory/LIVE.md`
  already lists. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, every criterion met and the
  `render_live` seam reused. widens: none · relaxes: none
- **F4 — Does a one-segment directory token join?** Options: (a) no, as `check_dir_shaped` reads a root
  for the guard join (`design_lib.py:579-586`); (b) yes, as everything under it. (b) joins 1,169 pairs on
  `tools/` alone at `4bf0f400d`, every one a root named in prose. RESOLVED (agent, 2026-10-28,
  delegated): (a), rung 3, one reading of a write set across both joins. widens: none · relaxes: none
- **F5 — Are shared registries left out of the join?** Options: (a) no: every path joins, and a registry
  is acknowledged once per unit by a path bullet; (b) leave out the unattended conf's `SHARED_RECORDS`
  and generated indexes, as the remote-ref probe does (`unattended.sh:3432-3435`). (b) has the
  memory-tree kit read the unattended kit's conf, an edge `tools/memory-tree/kit.toml` does not declare,
  and I7 states the pair rule "and nothing else". RESOLVED (agent, 2026-10-28, delegated): (a), rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 2, v2:1288 and :1605, flow-steps:241,
  walkthrough D2 and candidate 2, research-design:84-86, scout A's row 2 and interfaces 6 to 9, and the
  spec brief's I3, I7 and I16.

## 10. Reuse audit

The seams extended are `check_writes_intersect` and `read_spec_writes`
(`tools/memory-tree/design_lib.py:601`, `:528`) for the pair rule, `check_dir_shaped` (`:579`) for the
root reading, `read_spec_edges` (`:543`) for the acknowledgement, check 12's edge pass
(`check-memory-hygiene.sh:2555-2600`) for the verb, the checker's LIVE population
(`tools/check-spec-tokens.py:331`), `print_overlaps` (`tools/unattended/unattended.sh:3523`), whose
output the card already prints, and `render_live` (`tools/memory-tree/gen_build_index.py:2079`).
`python tools/codebase-map/reuse_lookup.py "join the files touched write sets of live specs across
builds and report overlapping paths"` ranked `write`, `live` and `build` helpers by name tokens and
then `read_spec_revisions`; none joins write sets across builds, and `derive_parallel_step`
(`gen_build_index.py:1724`) pairs units within one build only, so no existing seam fits the
cross-build join, which S1 composes from the readers above. Scout A's row 2 holds against source; its
interface 9 left the population open, and §8 F1 settles it on the measurement of §4.

Recall terms used: `python tools/memory-recall/query.py "which live specs of different builds declare the same files touched path" --terms "design index overlap files touched write set check_writes_intersect cross-build live spec acknowledge edges overlaps"`
