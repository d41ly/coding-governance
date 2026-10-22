**Serves:** research TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7

# Spec brief — dTrueNorth, the seven units and the interfaces they share

You author specs and write no product code. Read, in this order, before your first line:

1. The packet, `memory/builds/dTrueNorth/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its
   Items section quotes each clause verbatim with its id, its hash and its tokens; its Acceptance, Gates, Non-goals,
   Pins, Gaps and Later builds sections bind every unit.
2. The build README, `memory/builds/dTrueNorth/README.md`: its build-level rules bind every spec, rule 6 (fork marks)
   and rule 8 (the unattended kit's self-test suites are waived for this landing) above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit here is Tier 2: each is a
   new or changed kit contract (`memory/guides/SESSION-KICKOFF.md`, Tier rule).
4. Your unit's own section below, and the "Shared interfaces" section, which every writer reads.

The bootstrap instruments are the semantics and the plant suites your product replaces. Read the one your unit
succeeds whole; it is under `memory/builds/dClosedLoop/build/`, and every `B/` below is that folder:
- `B/2026-10-19-build-PLAY-dClosedLoop-1-carries.py`: units 1, 2, 3;
- `B/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py`: units 4, 5;
- `B/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py`: unit 6;
- `B/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-1]` (its lines 721-862) and `[deviations]`
  (its lines 1208-1295): unit 7 whole, and the deviation records below;
- `B/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md` `[coverage]`, `[deviation]` and `[bootstrap]`: the
  owner's FQ-2, FQ-3 and FQ-5 the clauses quote.
You never edit an instrument, v2, the as-built file or the packet: the packet's Non-goals.

## Every spec, whatever its unit

- Path `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-<n>.md`; H1 `# TOOL-dTrueNorth-<n> — <title>`,
  an EM DASH, never a colon (the index and `--plan` read nothing else).
- Status header `DRAFT`, the `order` verb your roster names, `streams tooling`.
- Its binding lines, each at column 0 on a line of its own, in the shape `carries.py`'s `CARRY` and `DERIVED`
  regexes parse: `**Carries:** <the Items id>@<hash8> whole` for units 1 to 6; unit 4 also
  `**Carries:** node:record-kind.deviation`; unit 7 `**Derived:** PLAY-dClosedLoop-2`.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks (the token
  arm reads them; `cl-dClosedLoop-0002` has none).
- Each clause's own "seen red on" cases are acceptance criteria, each observed RED on its planted case and green
  without it, by a probe or fixture of the unit's own code a pass can run. No criterion names the merge bar, a
  `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a `New arm:` line in
  section 7 and the main loop observes it at the close. A criterion an unattended self-test suite would observe is
  amended citing README rule 8.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
- §8 forks: settle each by the README rule 6 rungs, in the §8 mark shape TEMPLATE-SPEC states. A choice on rung 5
  or 6 cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and carries `widens:` and `relaxes:`, each a value or
  `none`. Never leave an open question: a FACT-QUESTION names its probe and you run the probe now.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set.

## Shared interfaces — one spelling for every writer

These are fixed so seven specs written by four writers agree on the interface axis (M2). A writer who finds one
wrong says so in its §8 as a fork and settles it there; it never silently respells one.

- **S1 · the cutoff.** One key, `SPEC_CARRIES_CUTOFF="2026-10-21"` in `.memory-tree.conf`, the opening landing's
  date (`271aa59de`), read through `tools/check-spec-tokens.py`'s `read_cutoff_key`, blank meaning off, as
  `SPEC_HANDOFF_CUTOFF` is. Unit 1 declares it; units 2 and 3 read it and declare nothing.
- **S2 · the design source.** Three keys in `.memory-tree.conf`, declared by unit 1: `DESIGN_RECORD` (v2's path),
  `DESIGN_BASELINE` (the pin, `59ff8f2ac04a967751eae00de6856afbea66c033`) and `DESIGN_VIEW` (the as-built view's
  path, today `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, which `asbuilt.py`
  renders). Clauses are read from `DESIGN_VIEW`'s table, so a deviation's `amends` row moves a clause's hash for
  every reader at once; retired ids from `DESIGN_RECORD`'s `[clause-ids]` at `DESIGN_BASELINE`. The chain builds
  are the view's Build column, and no build list is typed anywhere.
- **S3 · one parser.** `tools/memory-tree/design_lib.py`, owned by unit 1: the view reader (build, clause id, text,
  hash8, since), `clause_hash` exactly as `carries.py` takes it, the retired-id reader, and the binding-line parser
  for `**Carries:**`, `**Derived:**`, `**Moved:**`, `**Retired:**` and `**Deferred:**`, refusing a malformed line
  by name. Units 2, 3, 4 and 6 import it and parse none of these themselves (one fact in one place).
- **S4 · the join.** Unit 2's join is a further join inside `tools/check-spec-tokens.py`, beside the handoff
  join, exposed as one function unit 3 calls for the coverage report. Its acceptance is `carries.py --fixture`'s
  thirteen plants, each red on its plant and green without it (D3, stricter than the clause: deviation record 3).
- **S5 · the coverage region.** `<!-- gen:build-coverage -->` / `<!-- /gen:build-coverage -->`, rendered by
  `tools/memory-tree/gen_build_index.py --write` into each chain build's README beside its unit ids, its body what
  `carries.py --report <slug>` prints today, field for field.
- **S6 · the deviation record.** Kind `deviation`, joined to hygiene check 21's kinds; file
  `memory/builds/<build>/build/<date>-build-<unit>-deviation-<n>.md`, `<n>` per build; fields as
  `deviations.py`'s header names them, in its bold-key form. Unit 4 owns the grammar, the population and the join;
  unit 6 reads its `**Follow-through:**` line.
- **S7 · the audit pin.** `**Serves:** spec-audit <unit>@rev-<N> …`, a revision named per id. Unit 5 owns the
  grammar and the writer of it; unit 4's population reads it.
- **S8 · the as-built view.** Unit 6's generator renders `DESIGN_VIEW` byte for byte what `asbuilt.py --write`
  renders on the same records (the retirement table, execution plan line 855).

## Deviation records each spec's writer writes

Write each beside your spec, under `memory/builds/dTrueNorth/build/`, in S6's grammar. Do not commit it: the main
loop commits it with your unit's next spec commit.
- **deviation-1**, by unit 4's writer: `2026-10-21-build-TOOL-dTrueNorth-4-deviation-1.md`. The stand-in join reads
  the chain's values, `report` and any recorded approver, until dDeclaredLoop's and dScopedBuild's keys land; departs
  from `cl-dClosedLoop-0004@c374ccd0`; cause owner ruling; risk loosening; approver owner, citing `PLAY-dClosedLoop-4`
  (P0.8 row 3, the row recording ER:189). Execution plan line 1278.
- **deviation-2**, by unit 7's writer: `2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md`. The extra unit; departs
  from dTrueNorth's v2 row, which plans six units; hand-off design-to-spec; follow-through `new unit
  TOOL-dTrueNorth-7`; approver owner, citing ER:232, ER:320 and `PLAY-dClosedLoop-2`. Execution plan line 1279.
- **deviation-3**, by unit 2's writer: `2026-10-21-build-TOOL-dTrueNorth-2-deviation-3.md`. The product join takes
  the instruments' plant suite as its acceptance (D3), stricter than `cl-dClosedLoop-0002@6acd9ea9`; risk stricter;
  approver the spec writer, under `author-recorded`. Execution plan lines 1289-1294.
- **deviation-4**, by unit 4's writer: `2026-10-21-build-TOOL-dTrueNorth-4-deviation-4.md`. The same D3 departure
  from `cl-dClosedLoop-0004@c374ccd0`, naming P0.1 row 8a's exception (a revision that changes only its
  `**Status:**` line and generated regions) beside the stricter plants, so the product inherits it openly.

## The units

**Writer groups.** Units 1, 2 and 3 are one writer's (order 1), unit 5 one (order 2), units 4 and 6 one (order 3),
unit 7 one (order 4). That is also the build order: 1, 2, 3, 5, 4, 6, 7.

- **TOOL-dTrueNorth-1** — Items 1. The parser S3 and the conf keys S1, S2. Seen red on a planted malformed
  `**Carries:**` line; the chain builds' specs alone read, behind the cutoff.
- **TOOL-dTrueNorth-2** — Items 2. The join S4: a ghost id, an unbound spec, a stale pin, two whole carriers or two
  pins, a revision that stops carrying a clause with no decision, a token missing from its carriers each red, and a
  run that measured no spec never green, each on its planted case over a fixture spec set. Also deviation-3.
- **TOOL-dTrueNorth-3** — Items 3. The region S5, every field Items 3 lists, an explicit `none`; and memory hygiene
  refusing a chain build's spec at `INPROGRESS` while its build's coverage is red, seen red on a planted uncarried
  clause.
- **TOOL-dTrueNorth-5** — Items 5. The pin S7: every audit of a spec record pins the revision it read as `@rev-N`
  on its Serves line, written by `tools/workflows/tier2-review.js`'s spec-audit record and graded by check 21; a
  revision past its pin reads as unaudited; and the builder's, spec reviewer's and diff reviewer's rule lines
  (`tools/roles/`, rendered into `.claude/agents/`) carry the charter's `[docs]` rule.
- **TOOL-dTrueNorth-4** — Items 4, and the owned node `record-kind.deviation`. The record S6; its population from
  history (each revision after its unit's first attributed pass commit or past its pinned audited revision, each
  AMENDED acceptance line, each divergence hand-back, each rescope row, each clause-hash move); the join at the
  commit through the routed-commit attribution (`tools/memory-tree/routed_commits.py`) and at the close; the
  approver against the risk class by the `[deviation]` by-risk table, under the stand-in deviation-1 records. Seen
  red on a planted revision after a pass with no record, an AMENDED line with no record, a mismatched pin and an
  approver below the risk, and green on a status-only edit. Also deviation-1 and deviation-4.
- **TOOL-dTrueNorth-6** — Items 6. The generator S8 and its gate: red on a hand edit, on a deviation with no row and
  on a changed clause with no citation; the coverage join and the later renders reading it, through S2's
  `DESIGN_VIEW`.
- **TOOL-dTrueNorth-7** — `**Derived:** PLAY-dClosedLoop-2`, the execution plan's `[phase-1]` "The extra unit",
  lines 732-803, whole: the spec-run test read at the run's baseline commit, the `DEFERRED` carry of an added unit
  once with its witness in a rotated `RUN.<phase>.<blob8>.md`, the `baseline_units` fallback to the authored
  `roster:units` pair (`tools/unattended/lib-unattended.sh`) taken by all three callers, STOPS §15's second term and
  the verbs' close rule 9 re-rendered from their templates, and the thirteen red cases, each its own criterion. It
  edits `tools/unattended/`, so it is a driver-changing unit and builds last. Also deviation-2.
