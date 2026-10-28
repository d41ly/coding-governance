# TOOL-dIndexedDesign-7 — the spec measured, recommendations emitted, and the spec redesigned as a structured, tagged contract

**Status:** OPEN · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 5 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0389@158d7ac4 whole
**Carries:** node:record-kind.spec
**Carries:** node:item.design.unit-spec

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-c.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-c.md) | research | TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

Measure the spec format before changing it, emit recommendations from the measurement, and give the
spec the structured fields the owner's D3 answer names (definitions, design, boundaries, interfaces
and acceptance) as fields a check reads, on the tagged sections of TOOL-dIndexedDesign-9. The fields
are opt-in until a trial on real units shows they win, because the owner asked for the new format to
be trialled against the old before it becomes the default (walkthrough:445-469).

## 2. Scope (IN)

- **S1** — The measurement instrument, a research file under this build's folder and never product:
  `memory/builds/dIndexedDesign/build/<date>-build-TOOL-dIndexedDesign-7-spec-measure.py`, its verbs
  `measure`, `trial` and `--fixture <case>`. `measure` reads the tracked corpus at one named commit and
  computes the four measurements of §4 "The measurements", M1 to M4, every section named by its I1 tag.
  Observed by AC1, AC2.
- **S2** — The recommendations: `measure` emits one line per section tag by §4's rule, `structure`,
  `trim` or `keep`, with the shares that decided it. Observed by AC3.
- **S3** — The research record the pass writes from S1 and S2,
  `memory/builds/dIndexedDesign/build/<date>-build-TOOL-dIndexedDesign-7-spec-measure.md`, serving
  `research TOOL-dIndexedDesign-7`, naming the commit it measured, the corpus counts, the four tables,
  the recommendations and the S7 verdict; each `structure` or `trim` line S4 does not answer becomes an
  ask in this build's `BACKLOG.md`. Observed by AC4.
- **S4** — The structured fields, stated once in `tools/memory-tree/SPEC-TEMPLATE.template.md` and its
  render `memory/TEMPLATE-SPEC.md`: a rules section naming the five parts and where each lives, and the
  Tier-2 skeleton gaining three sub-heads, `### Definitions` and `### Interfaces` inside the Design
  section and `### Invariants` inside the Non-goals section beside `### Edges`, each with the grammar of
  §4 "The fields". Observed by AC10.
- **S5** — The field check, a `fields` arm in `tools/check-spec-tokens.py` over the LIVE specs it
  already grades: a spec carrying any of the three sub-heads is graded on all three, and a Tier-2 spec
  dated on or after a set `SPEC_TAGS_CUTOFF` must carry them; it reads each section through
  `read_spec_section` and reds the findings §4 "The check" lists. It prints one
  `spec-tokens: fields ·` summary line on every run, and an announce line when it graded nothing.
  Observed by AC5, AC6, AC7.
- **S6** — The switch: the `fields` arm reads `SPEC_TAGS_CUTOFF`, TOOL-dIndexedDesign-9's key, through
  the checker's `read_cutoff_key`, so one date makes the tagged canon and the fields the default
  together; this unit adds no key and leaves the key as unit 9 declares it, blank. Observed by AC7.
- **S7** — The trial: the instrument's `trial` verb partitions the CLOSED Tier-2 specs dated on or
  after this unit's landing into the field form and the old form and prints `PENDING`, `WIN` or `LOSE`
  by §4 "The trial". The pass runs it once into S3's record, and files an ask in this build's
  `BACKLOG.md` to set `SPEC_TAGS_CUTOFF` when the verdict reads `WIN`, the arming unit 9 hands to this
  unit. Observed by AC9.
- **S8** — The skeleton writer: `gen_build_index.py --new-spec` gains `--fields`, and writes the three
  sub-heads with fill markers when it is passed or when the new spec's date is on or after a set
  `SPEC_TAGS_CUTOFF`, through `render_spec_skeleton` (`tools/memory-tree/gen_build_index.py:8617`).
  Observed by AC8.
- **S9** — The docs: `tools/memory-tree/README.md` names the `fields` arm, the cutoff and the trial;
  `KIT_MEMORY_TREE_VERSION` moves. NOT OBSERVED by a criterion: prose, graded by `kit/dogfood doc parity`.

## 3. Non-goals (OUT)

- The section tags, their reader `read_spec_section` and the declaration of `SPEC_TAGS_CUTOFF`:
  TOOL-dIndexedDesign-9 owns I1. This unit reads sections through it and adds no section to the canon
  (§8 F1).
- The spec-site `**Edges:**` line and its `implements=` and `decides=` edges: TOOL-dIndexedDesign-12.
- The feature level and its interface record: TOOL-dIndexedDesign-8 reads S4's `### Interfaces`.
- Applying a `trim` recommendation to the template: each is an ask S3 files, decided on its own.
- Setting `SPEC_TAGS_CUTOFF` in this pass: S7's ask arms it once the trial reads `WIN`.
- The `sections` column of the `spec` row in `record-kinds.toml`: TOOL-dTotalRecall-9 S2 writes it and
  TOOL-dIndexedDesign-9 files its ask; the fields sit inside sections and need no column.
- Ask PLAY-dClosedLoop-22, the binding-line grammar's template home (§8 F5).
- The spec-audit lenses of `tier2-review.js`, which the measurement reads and never changes.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-9` — `read_spec_section`, the I1 reader the instrument and the `fields` arm read every section through, with its tag table and `SPEC_TAGS_CUTOFF`, the switch S6 reads and S7's ask arms; without it M1 cannot name a Tier-1 section
- **hands-off** `TOOL-dIndexedDesign-8` — `record-kind.spec`, the structured spec whose `### Interfaces` field the feature level reads as each unit's half of a feature's interfaces
- **consumes-from** external — TOOL-dTotalRecall-1 §4's `spec` row of `record-kinds.toml`, the registry row of `record-kind.spec`, DEFERRED at base and built before this build run
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 4, 17, 27 and 50, each a scope item of that batch unit

## 4. Design

### Evidence

Read at `4bf0f400d`; no product file differs from base `57bc3b91`.

- The canon is ten `##` sections for Tier-2 and eight for Tier-1 (`memory/TEMPLATE-SPEC.md:134-145`),
  held by check 12's `SPEC_CANON` (`tools/memory-tree/check-memory-hygiene.sh:1901-1919`).
- Fields already read by a machine: `S<n>` and `AC<n>` joins, `Red when:`, `### Edges`,
  `### Files touched (estimate)`, the F-item, `New arm:`. None states definitions, invariants or the
  interfaces a unit takes and produces.
- `review_replay.py` SPEC MODE maps a spec-audit finding to a section by `extract_section_ref`
  (`tools/workflows/review_replay.py:100`) and by item kind through `ITEM_SECTIONS = {"S": 2, "AC": 6,
  "F": 8}` (`:70`), the Tier-2 numbering, which misreads a Tier-1 spec; TOOL-dIndexedDesign-9 moves it to
  the tag reader. `parse_record_findings` is at `:185`.
- `read_spec_revisions` (`tools/memory-tree/design_lib.py:608`) gives every revision of a spec with its
  text before and after.
- The prior measurement, `memory/builds/aWeighedCanon/build/2026-09-04-build-TOOL-aWeighedCanon-1-spec-format-measurements.md`,
  counted revisions and sizes over 479 specs at `6c670b02` and mapped no finding to a section.

### The measurements

The population is every tracked spec at the measured commit, and every spec-audit record, a record
whose first binding opens `**Serves:** spec-audit`.

| Id | Measures | How |
|---|---|---|
| M1 | where findings land | each record's findings by `parse_record_findings(text, mode="spec-audit")`; a finding's ordinal resolves to the title the audited spec carries at that ordinal, then to its I1 tag through `read_spec_section`'s mapping, so Tier-1 §5 is `section.acceptance`; an `S`, `AC` or `F` item resolves by its label's defining section |
| M2 | where builders diverge | for each CLOSED unit, each revision after its first build commit, the oldest commit whose `Pass:` trailer, else subject, names the unit and that changes a path outside the memory root; each such revision's §9 entry's scope tokens resolve to tags; a revision with no entry counts as `untagged` |
| M3 | rework after the spec | the share of CLOSED units with at least one M2 revision; the count of WONTDO units whose tail names a successor |
| M4 | cost | bytes per tag; revisions before the first build commit; spec-audit records per spec |

### The recommendations

For each tag, `f` is its share of M1 findings, `v` its share of M2 revisions and `b` its share of M4
bytes. `structure` when `f + v > 2b`, because the section draws findings and rework beyond its size;
`trim` when `f = 0`, `v = 0` and `b >= 0.05`; `keep` otherwise. A line reads
`- <tag> · <recommendation> · f <f> · v <v> · b <b>`, shares to three places. The rule's thresholds
are this spec's own, the weakest tier of bound (the execution plan's rung 6), and S3's record states
them beside the result.

### The fields

The five parts and where each lives:

| Part | Field | Grammar |
|---|---|---|
| definitions | `### Definitions`, Design section | `- **<term>** — <definition>`, one per term, or the single word `none` |
| design | the Design section's body | as today |
| boundaries | `### Files touched (estimate)` for what the unit may touch; `### Invariants`, Non-goals section, for what must hold; the Non-goals body for what it must not change | `- **V<n>** — <invariant>. Held by AC<n>.` or `NOT OBSERVED` and the reason, or `none` |
| interfaces | `### Interfaces`, Design section | a table `Interface`, `Direction`, `Spelling`, `Counterpart`; direction `takes` or `produces`; spelling in backticks; counterpart a unit id or `external` |
| acceptance | the Acceptance section | as today: a label, a backticked command, `Red when:` |

Prose explains a field and never stands in for it.

### The check

The `fields` arm reds, per graded spec: a field sub-head absent where S5 requires it; a bullet or row
off its grammar; a term defined twice; a defined term the rest of the spec never uses; an invariant
naming an `AC<n>` the Acceptance section does not define; and an Interfaces row whose counterpart is
a unit of the same build with no §3 `### Edges` bullet of the matching verb (`takes` to
**consumes-from**, `produces` to **hands-off**) naming that unit and carrying the row's spelling.
Each finding prints `spec-tokens: fields · <path> · <field> · <finding>`. An unparseable section is a
finding, never a skip.

### The trial

`trial` reads the CLOSED Tier-2 specs dated on or after the landing commit's date that carry a
spec-audit record. Field form carries all three sub-heads; old form carries none; a spec with some is
listed apart and counted in neither.

- `PENDING` while either form holds fewer than 8 such specs.
- `LOSE` when the field form's mean M1 findings per spec is not below the old form's, or its mean M2
  revisions per spec is not below, or its median bytes exceed 1.25 times the old form's.
- `WIN` otherwise.

The observation that makes the redesign lose is the first two lines: fields that do not lower
findings or rework are cost without a return. Expected at the pass: `PENDING`, since no field-form spec
exists before this unit lands.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `…-TOOL-dIndexedDesign-7-spec-measure.py` and `.md` | research instrument and record | none |
| `measure`, `trial` | verbs of the instrument | none |
| `structure`, `trim`, `keep`; `PENDING`, `WIN`, `LOSE` | recommendation and verdict words | none |
| `### Definitions`, `### Invariants`, `### Interfaces` | spec sub-heads | none |
| `V<n>` | invariant label | none |
| `fields` | arm of `check-spec-tokens.py` | none |
| `--fields` | flag of `--new-spec` | none |

### Migration

None: no landed spec gains a field, and the arm grades only a spec that opts in or is dated past a
set cutoff.

### Rollout

Live at landing as an opt-in; `SPEC_TAGS_CUTOFF` stays blank, as TOOL-dIndexedDesign-9 declares it,
until S7's ask is answered.

### Files touched (estimate)

- `tools/check-spec-tokens.py`: S5, S6's read
- `tools/check-spec-tokens.test.sh`: S5's arm cases
- `tools/memory-tree/gen_build_index.py`: S8 and its selftest arm
- `tools/memory-tree/SPEC-TEMPLATE.template.md` and its render `memory/TEMPLATE-SPEC.md`: S4
- `tools/memory-tree/README.md`: S9
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION` only

### Alternatives rejected

- **Measure by re-running the spec-audit lenses over today's specs.** Lost to cost: 254 past audits
  already hold the findings, and re-running them measures today's lenses, not the format's record.
- **Map a finding's ordinal through a fixed Tier-2 table**, as `ITEM_SECTIONS` does today. Lost to
  the Tier-1 misread scout C measured (`review_replay.py:67`, `:70`): Tier-1 §5 is Acceptance.
- **Fields as structured front matter** (a TOML block per spec). Lost to the house grammar: every
  field the checks read today is a markdown sub-head or bullet, and a second syntax doubles the readers.

## 5. Production-readiness checklist

- security — N/A — the arm and the instrument read tracked text and write one record; no new write
  path into product.
- perf / scale — `measure` reads each spec once and every revision through one
  `read_spec_revisions` batch; the arm adds a section read per opted-in LIVE spec.
- error / empty / loading states — an empty population prints its zero and refuses to recommend; a
  record the finding parser cannot read is counted unread and named, never dropped.
- observability — the arm's summary line on every run; S3's record lists every count with its sha.
- risks — the thresholds of §4 are the writer's: S3 prints them beside every share, so a reader can
  re-judge them; the trial can stay `PENDING` while authors decline the opt-in, which S7's ask names.
- testing — the instrument's `--fixture` cases, and the arms of §7.
- migration — none.
- user docs — `memory/TEMPLATE-SPEC.md` through its kit template; the memory-tree README.

## 6. Acceptance criteria

- **AC1** — When `python …-spec-measure.py --fixture findings` runs over a Tier-2 spec, a Tier-1 spec
  and a spec-audit record whose findings cite `§6` and `AC2` on the first and `§5` on the second, M1
  attributes all three to `section.acceptance`.
  Red when: the Tier-1 `§5` lands on the readiness section, the ordinal misread.
- **AC2** — When `--fixture divergence` runs over a CLOSED unit with a build commit, a rev-2 after it
  whose §9 entry names `§4 · AC3`, and a rev-1 before it, M2 counts one revision against
  `section.design` and one against `section.acceptance`, and M4 counts the rev-1.
  Red when: a revision before the first build commit counts as divergence.
- **AC3** — When `--fixture recommend` runs over planted shares, a tag at `f 0.30 · v 0.20 · b 0.10`
  reads `structure`, a tag at `f 0 · v 0 · b 0.08` reads `trim` and a tag at `f 0.10 · v 0.10 · b 0.10`
  reads `keep`.
  Red when: a line's recommendation differs from §4's rule.
- **AC4** — When the pass runs `measure` at its base, the record `…-spec-measure.md` names that commit,
  the four tables, a recommendation line per I1 tag and the `trial` verdict, and each `structure` or
  `trim` line S4 does not answer has an ask row in this build's `BACKLOG.md`.
  Red when: a tag lacks a line, or a recommendation lacks its ask.
  figure: every count DERIVED at the pass's base.
- **AC5** — When `python tools/check-spec-tokens.py` runs in a fixture repository over a LIVE spec whose
  `### Interfaces` row takes `read_x` from a sibling unit and whose §3 carries no
  **consumes-from** bullet naming that unit, it exits 1 printing a `spec-tokens: fields` line naming the
  row; with the bullet carrying `read_x`, it exits 0.
  Red when: a declared interface with no matching edge passes.
  fixture: the suite builds the repository, `SPEC_TAGS_CUTOFF` blank, the spec opting in by shape.
- **AC6** — When the same run grades a spec whose `### Invariants` names `AC9` that its acceptance
  section never defines, whose `### Definitions` defines one term twice, and defines a second term
  used nowhere else, it prints three `spec-tokens: fields` findings and exits 1.
  Red when: any of the three passes.
  fixture: as AC5.
- **AC7** — When the fixture conf sets `SPEC_TAGS_CUTOFF` on or before a tagged Tier-2 spec's filename date
  and that spec carries no `### Interfaces`, `python tools/check-spec-tokens.py` exits 1 naming the
  absent field; with the key blank the same spec is not graded and the summary line counts it ungraded.
  Red when: a required field is absent and the run passes, or a blank key grades a spec that did not opt in.
  fixture: the conf arms `SPEC_TAGS_CUTOFF` alone, so check 12's tagged canon holds the spec too.
- **AC8** — When `python gen_build_index.py --new-spec TOOL-tFix-1 --tier 2 --fields` runs in a fixture
  repository, the written skeleton carries `### Definitions`, `### Interfaces` and `### Invariants`,
  each with a fill marker; without `--fields` and with the cutoff blank it carries none of them.
  Red when: `--fields` writes no field, or a blank cutoff writes one unasked.
- **AC9** — When `--fixture trial` runs its three plants, seven field-form audited specs read
  `PENDING`; eight of each form with the field form's mean findings equal to the old form's read `LOSE`;
  eight of each with fewer findings, fewer revisions and median bytes at 1.1 times read `WIN`.
  Red when: an equal-findings trial reads `WIN`, or a short population reads anything but `PENDING`.
- **AC10** — When `grep -n "### Interfaces" memory/TEMPLATE-SPEC.md` runs, it prints the skeleton's
  sub-head and the rules section's line, and `tools/memory-tree/SPEC-TEMPLATE.template.md` carries the
  same lines.
  Red when: the render and its template differ, or a part of the five is unnamed.

## 7. Gates

`build-index selftest` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `memory hygiene` · `policy fixtures` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: tools/check-spec-tokens.test.sh · covers AC5 AC6 AC7 · fixture specs opting in by shape and one past a set cutoff, its failing case an Interfaces row with no matching edge · none

New arm: tools/memory-tree/gen_build_index.py · covers AC8 · the `--selftest` arm writing a skeleton with and without `--fields`, its failing case a `--fields` skeleton missing a sub-head · none

## 8. Open questions

- **F1 — Where do the fields live?** Options: (a) sub-heads inside the tagged sections, as `### Edges`
  sits inside Non-goals; (b) three new `##` sections, the canon growing to thirteen. (b) changes every
  reader of the canon, the 30 code sites and 4 prompt files scout C counted for TOOL-dIndexedDesign-9,
  check 12's `SPEC_CANON` and the I1 tag list, while (a) changes none. RESOLVED (agent, 2026-10-28,
  delegated): (a), rung 3, both meeting every criterion and (a) leaving fewer questions open and reusing
  the `### Edges` seam. widens: none · relaxes: none
- **F2 — Which switch makes the fields required?** Options: (a) `SPEC_TAGS_CUTOFF`, the brief's I8
  and TOOL-dIndexedDesign-9's §8 F1, blank until this unit's trial reads `WIN`, the fields graded on any
  spec that opts in by shape before then; (b) a key of the fields' own, so the tags could become the
  default apart from them. (b) puts two switches on one format and lets the tagged canon go live
  untrialled, against the owner's "trialled against the old on real units before it becomes the
  default" (walkthrough:465-466), which unit 9 reads as this unit arming its key. RESOLVED (agent,
  2026-10-28, delegated): (a), rung 3, one switch for one format. widens: none · relaxes: none
- **F3 — How is the new format trialled?** Options: (a) prospective, over CLOSED real units of each
  form, the verdict by §4 "The trial"; (b) retrospective, K landed specs re-expressed in the field form
  by an agent and both forms audited blind. (b) measures specs whose units are already built, so it is
  not a trial on real units, its re-expressing author reads the spec and confounds format with
  rewriting, and it costs 2K audits. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F4 — Which checker holds the field arm?** Options: (a) `check-spec-tokens.py`, which grades the LIVE
  specs and reads sections through `read_spec_section`; (b) check 12's awk in
  `check-memory-hygiene.sh`. (b) adds a fourth awk section walk beside the shell twin
  TOOL-dIndexedDesign-9 keeps in agreement by a case table, and grades frozen terminal specs.
  RESOLVED (agent, 2026-10-28, delegated): (a), rung 3. widens: none · relaxes: none
- **F5 — Does this unit take ask PLAY-dClosedLoop-22 into `closes`?** Options: (a) take it: S4's rules
  section gains the five binding keys' grammar, pointing at `design_lib.py`; (b) leave it open. The
  binding lines are TOOL-dTrueNorth-1's mechanism, parsed by `parse_binding_lines`
  (`tools/memory-tree/design_lib.py:348`), and M2 gives a second mechanism its own unit. RESOLVED (agent,
  2026-10-28, delegated): (b), rung 3: the ask stays open for a unit of its own. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 7, walkthrough D3 and its revision
  (:445-469), v2 P12 (:900-902), flow-steps' `design.unit-spec` row, scout C's row 7 and the spec
  brief's I1 and I8.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from edge of TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.

## 10. Reuse audit

The seams extended are `read_spec_section` (TOOL-dIndexedDesign-9, I1) for every section read;
`review_replay.py`'s `parse_record_findings` and `extract_section_ref`
(`tools/workflows/review_replay.py:185`, `:100`) for M1; `read_spec_revisions`
(`tools/memory-tree/design_lib.py:608`) for M2 and M4; the checker's `read_cutoff_key` and its LIVE
population (`tools/check-spec-tokens.py:732`, `:331`) for S5 and S6; `read_spec_edges`
(`design_lib.py:543`) for the Interfaces join; and `render_spec_skeleton` (`gen_build_index.py:8617`)
for S8. `python tools/codebase-map/reuse_lookup.py "measure which spec sections review findings land
in and how often a spec is revised after its first build pass"` ranked `build` helpers and then
`read_spec_revisions` (fan-in 5, a SEAM) and `parse_spec_h1`; nothing measures findings by section,
so no existing seam fits the instrument, which composes the readers above. The recall probe found the
prior measurement `TOOL-aWeighedCanon-1` (sizes and revisions, no section attribution), which S1
extends rather than repeats. Scout C's row 7 holds against source, its `ITEM_SECTIONS` misread at `review_replay.py:70`.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings mapped to spec sections and what did the spec format measurement find" --terms "spec format measure findings section review_replay spec-audit rework divergence structured contract tagged fields"`
