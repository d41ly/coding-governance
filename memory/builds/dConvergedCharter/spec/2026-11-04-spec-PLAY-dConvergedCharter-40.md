# PLAY-dConvergedCharter-40 — `guide_move.py apply`'s amend route: an entry whose target tag a kit manifest already holds gains its `help` and edge on that row under an `edit` change record, never a second row

**Status:** DEFERRED · rev-3 · 2026-11-05 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 15 · advances PLAY-dConvergedCharter-24

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-41 |
| [2026-11-04-build-PLAY-dConvergedCharter-40-deviation-401.md](../build/2026-11-04-build-PLAY-dConvergedCharter-40-deviation-401.md) | deviation | — |
| [2026-11-04-prompt-PLAY-dConvergedCharter-7-r4-fold-brief.md](../prompts/2026-11-04-prompt-PLAY-dConvergedCharter-7-r4-fold-brief.md) | research | PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 |
| [2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-41 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 |
| [2026-11-05-review-PLAY-dConvergedCharter-11-chain-spec-audit-round2.md](../reviews/2026-11-05-review-PLAY-dConvergedCharter-11-chain-spec-audit-round2.md) | spec-audit | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-41 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's 11 revised and promoted specs
(`memory/builds/dConvergedCharter/reviews/2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md`)
confirmed finding **id 27 at MEDIUM**, report item **M13**. PLAY-dConvergedCharter-7 S7 says a retired
guide section whose directive text is already a unit, one of PLAY-dConvergedCharter-1's residue rows,
gains its rationale as that unit's `help` and its `explains=` edge on that unit, written through
PLAY-dConvergedCharter-13's `apply`. That `apply` composes every row with `core.py new unit` (unit 13
S3) and appends it with a change record `Action add` (S4): it has no route that changes an existing row.
Built as written, a builder either appends a second row for the tag, which the schema and one-fact
checks refuse, or hand-edits the manifest outside the guarded route, with no change record and no
refuse-unless-`check` guard, an unreviewed write path into kit manifests in the commonest case of S7.
Closing the finding adds a write path no unit's scope names, an amend of an existing row, so it is its
own unit. It is the batch of this round's NEW-MECHANISM minors, and the batch holds one finding. It lands
at order 15, the step after unit 13 (order 14), whose `apply` it extends, and before unit 7 (order 17),
which writes through it.

## 2. Scope (IN)

Build-run preconditions: PLAY-dConvergedCharter-13 has landed `tools/playbook/guide_move.py` with
`plan`, `apply`, `--fixture` and S4's write route; and its parents have landed the unit rows and
`read_units` (PLAY-dOrderedCharter-9 S1, S2), `instructions_edit.py check` and the change record whose
`Action` is one of `WRITE_VERBS = ("add", "edit", "remove", "rename", "split")` with `Before` and
`After` as `<tag>@<hash8>` (PLAY-dOrderedCharter-15 S6, S7, its §4 Data model), and `core.py new unit`
(PLAY-dOrderedCharter-20 S9).

- **S1** — id 27, the amend entry. A plan entry may carry `target = "<unit tag>"`. Before composing a
  row, `apply` reads the manifest of the entry's `kit` through `read_units`. Where an active row there
  holds `target`, the entry is an AMEND: `core.py new unit` is never called, and the row keeps its tag,
  `type`, `level`, `text` and `scope`, so its directive text is untouched; it gains the entry's `help`,
  and the entry's edge (`explains=doc.<name>#<seg>` on unit 7's route) is appended to its `edges` unless
  the row already carries it. An amend entry's `type`, `level` and `text` may be blank, the refusal of a
  blank `text` (unit 13 S3) applying to an add entry only. Three refusals, each exit 2 writing nothing
  for the whole plan and naming the entry's section and the tag: a `target` no active row holds, so an
  amend never creates a row; a row whose `help` is already non-empty and differs from the entry's, so an
  amend never overwrites rationale another pass wrote; and two entries of the plan sharing one `target`,
  naming both sections (§8 F1). Each refusal reads the manifest on disk, which, with one entry per
  target, is the row its amend changes. An entry with no `target` takes unit 13's add route unchanged.
  Observed by AC1 and AC2.
- **S2** — id 27, the amend's write and record. An amend rewrites the one row in place in the kit's
  `instructions.toml` as the pass's own kit edit, by the same route and guard as unit 13 S4: the whole
  plan, adds and amends together, is written only when `instructions_edit.py check` passes over the
  would-be tree, and refused otherwise with both the manifest and the guide byte-identical. Each amend
  writes one change record through `python tools/memory-tree/build_records.py new change` with `Action
  edit`, `Before` and `After` the row's `<tag>@<hash8>` before and after the amend under
  PLAY-dOrderedCharter-15 S7's normaliser, `Mark` as that normaliser reads the two, `Proof` `none —
  agent pass`, and `Promoted-from` the section tag: the field set S7 gives an `edit`, with no
  `Successor`. Each amend's record is written BEFORE the manifest is rewritten, the one order in which
  `Before` is still on disk. Idempotence follows unit 13 S1 part by part: the row part is skipped where
  the row already carries the entry's `help` and edge, the record part where a change record with
  `Action edit`, `Promoted-from` the section tag and `After` the amended row's `<tag>@<hash8>` exists, so
  a re-run writes only the missing part and, with both standing, prints `skipped <section>: already at
  <tag>`. THE ORPHAN. An interrupted amend leaves an `edit` record whose `After` names a row never on
  disk: `apply` exits non-zero there naming that record, so the pass, whose check is red, commits
  nothing past it (BUILD-METHOD M6). A re-run, its plan unchanged or with the entry's `help` corrected
  so its `After` differs, finds the orphan as a record with `Action edit`, `Promoted-from` the section
  tag and `Before` the row's current `<tag>@<hash8>` whose `After` no row on disk carries; where the
  orphan is not in `HEAD` (the file `apply` itself wrote), the re-run unlinks it before writing the
  amend's record, so the trail holds one `edit` per change; where it is committed, history the pass
  cannot rewrite, `apply` exits 2 naming it and writes nothing. Observed by AC1 and AC3.
- **S3** — id 27, the plants. `guide_move.py --fixture --plant <case>` gains `amend-existing` (a kit
  manifest holding a unit whose `help` is empty, an entry targeting it), `amend-missing` (a `target` no
  row holds), `amend-conflict` (a target row whose `help` already differs), `amend-two-sections` (two
  entries targeting one row), `amend-twice` (the `amend-existing` apply run a second time) and
  `amend-interrupted` (the manifest write raises after the amend's record is written),
  `amend-interrupted-then-edited` (that interruption, then the entry's `help` corrected before the
  re-run) and `amend-orphan-committed` (the orphan record committed before the re-run), each run by
  `guide_move.py --selftest` under `adopt-playbook.sh --selftest`, as unit 13 S6's plants are. Observed by AC1 to AC3.
- **S4** — id 27, the docs. `tools/playbook/README.md`'s mover section names the `target` field and the
  amend route beside the add route. NOT OBSERVED by a criterion: prose, graded by the `docs` leg at the
  close.

## 3. Non-goals (OUT)

- Which entries carry a `target`: the route that writes the plan decides it. PLAY-dConvergedCharter-7's
  `--rationale` route sets it to the unit whose `promoted-from=doc.<name>#<seg>` edge names the section
  (unit 1's residue rows carry that edge with an empty `help`, PLAY-dConvergedCharter-1 S3).
- Amending a row's directive text, type, level or scope: an `edit` of the directive is the owner's
  through `instructions_edit.py edit`; this route adds rationale and an edge only.
- Unit 13's add route, its factory `prose_move.py` and its idempotence rule: unchanged, extended here.
- Writing through `instructions.edit`'s door, which under `owner-command-agents-propose` prints a
  proposal for an agent and writes nothing (unit 13 §8 F2).

### Edges

- **consumes-from** `PLAY-dConvergedCharter-13` — `guide_move.py apply` and its S4 write route, which S1 and S2 extend with the amend; without it there is no `apply` to extend
- **hands-off** `PLAY-dConvergedCharter-7` — `guide_move.py apply`'s amend route, through which that unit's S7 gives a section whose directive text is already a unit its `help` and `explains=` edge on that row
- **consumes-from** external — PLAY-dOrderedCharter-9, -15 and -20, the unit rows, the check, the change record and `core.py new unit`, each landed before this build run

## 4. Design

### Evidence

Read at `45022c64a`; no product file differs from base `0d1c1dda`.

- `tools/playbook/guide_move.py` does not exist at base; PLAY-dConvergedCharter-13 S3 and S4 (rev-4)
  specify `apply` composing each row with `core.py new unit` and appending it with `Action add`, and
  name no amend.
- PLAY-dOrderedCharter-15's `WRITE_VERBS` is `("add", "edit", "remove", "rename", "split")`
  (`memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md:180`), and its change
  record carries `Unit`, `Action`, `Before`, `After`, `Mark`, `Successor` (on every action but `add`
  and `edit`), `Proof` and `Promoted-from` (`:97-104`), so an amend's record is an `edit` with both
  hashes and no `Successor`; there is no `amend` action.
- PLAY-dOrderedCharter-20's one-fact check reds two active units sharing one text (`instruction_units.py
  one-fact`, its S2), so a second row carrying the rationale beside unit 1's directive row is refused,
  not merely redundant.
- PLAY-dConvergedCharter-1 S3 writes each residue row with an empty `help` and the edge
  `promoted-from=doc.<name>#<seg>` through unit 13's route, so the row unit 7 amends exists and its
  `help` is blank when unit 7 runs.

### The plan entry, amended

```toml
[[move]]
source  = "tools/memory-tree/BUILD-METHOD.template.md"
section = "doc.build-method#m5-recall-and-reuse"
kit     = "memory-tree"
target  = "unit.reuse-first"   # an active row's tag: amend it; absent: add a row
help    = """<the section's rationale, verbatim>"""
edge    = "explains=doc.build-method#m5-recall-and-reuse"
type    = ""                   # blank is admitted on an amend
level   = ""
text    = ""
```

### Inventory

Minted: the plan field `target`; the plant cases `amend-existing`, `amend-missing`, `amend-conflict`,
`amend-two-sections`, `amend-twice` and `amend-interrupted` of `guide_move.py --fixture`. No function name is minted: the amend is a branch of
unit 13's `apply`, and any helper the builder names is asked of `python tools/lexicon/lexicon.py
--suggest <name> --as py.function` at the pass.

### Rollout

Gov's tree, one pass at order 15, after PLAY-dConvergedCharter-13 and before PLAY-dConvergedCharter-7
writes its rationale rows. `guide_move.py` ships with the playbook kit; an adopter runs nothing.

### Files touched (estimate)

- `tools/playbook/guide_move.py`: S1 to S3
- `tools/playbook/README.md`: S4

### Alternatives rejected

- **A new `help`-only unit with its own tag for the section.** Its `text` would restate unit 1's
  directive text, which the one-fact check reds, or carry a typed stand-in text, a second fact beside
  the first; the skeptic's alternative fix, rejected by the one-fact check's rule (§4 Evidence).
- **A hand edit of the existing row in unit 7's pass.** It skips the change record and the
  refuse-unless-`check` guard, the unreviewed second write path the finding names.
- **Calling `instructions_edit.py edit`.** Under the default `owner-command-agents-propose` an agent's
  call prints a proposal and writes nothing (unit 13 §8 F2), so the rationale would never land.
- **An `Action amend` change record.** `WRITE_VERBS` holds no `amend`; an `edit` with both hashes is the
  record the parent already defines for a changed row.

## 5. Production-readiness checklist

- security — no new write surface beyond unit 13's: the amend writes only the kit manifests a plan
  names, under the same refuse-unless-`check` guard, and refuses to overwrite a non-empty `help` or to
  create a row from a `target`.
- perf / scale — one `read_units` per kit the plan names; one extra record per amend.
- error / empty / loading states — a missing target, a conflicting `help` and two entries on one target
  each refuse the whole plan, exit 2, naming the section and the tag; a re-run writes only an amend's
  missing part and skips a done one with a printed line.
- observability — `apply` prints each amend as `amend <section> -> <tag>` and each skip with its reason.
- risks — a `target` naming a retired row is refused as missing, since only an active row is amended.
- testing — the plants of S3 and the arm of §7.
- migration — none: the route is used by PLAY-dConvergedCharter-7's pass.
- user docs — `tools/playbook/README.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python guide_move.py --fixture --plant amend-existing` runs, `apply` leaves the kit
  manifest holding the target tag on exactly one row, that row's `type`, `level`, `text` and `scope`
  byte-equal to before, its `help` equal to the entry's and its `edges` holding the entry's edge, and
  `build_records.py` lists one change record for it with `Action edit` and two different hashes, its
  field set the one PLAY-dOrderedCharter-15 S7 gives an `edit`, `Proof` set and no `Successor`; with
  `instructions_edit.py check` made to fail over the would-be tree, the manifest and the guide are
  byte-identical after the run.
  Red when: a second row is appended for an existing tag, the directive text changes, the record reads
  `add` or departs from the parent's `edit` shape, or a row is written past a failing check.
- **AC2** — When `python guide_move.py --fixture --plant amend-missing` runs, `apply` exits 2 naming the
  section and the missing tag and writes nothing; under `amend-conflict` it exits 2 naming the tag whose
  `help` differs, and the row's `help` is unchanged; under `amend-two-sections` it exits 2 naming both
  sections and the tag, the manifest unchanged.
  Red when: an amend creates a row, overwrites a `help` another pass wrote, or one plan amends one row
  twice.
- **AC3** — When `python guide_move.py --fixture --plant amend-twice` runs, the second `apply` writes no
  byte and no record and prints `skipped <section>: already at <tag>`; under `amend-interrupted` the
  first `apply` exits non-zero naming the record it left, and the re-run amends the row and writes no
  second record; under `amend-interrupted-then-edited` the re-run leaves exactly one `edit` record for
  the section, its `After` the row's hash on disk; under `amend-orphan-committed` the re-run exits 2
  naming the committed orphan and writes nothing.
  Red when: a re-run appends the edge twice, writes a second change record, skips a row whose record
  alone stands, leaves a record whose `After` no row on disk carries, or rewrites a committed record.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`guide_move.py --selftest` runs under `adopt-playbook.sh --selftest`, the arm PLAY-dConvergedCharter-13
declares; this unit's plants join it. The parent legs `instruction render (one renderer of record)` and
`writing practice (records and units)` read the amended rows once they land; neither is in the manifest
at base.

New arm: tools/playbook/guide_move.py · covers AC1 AC2 AC3 · the plants `amend-existing`, `amend-missing`, `amend-conflict`, `amend-two-sections`, `amend-twice`, `amend-interrupted`, `amend-interrupted-then-edited` and `amend-orphan-committed`, staged red with the amend branch removed so the existing tag gains a second row, with the `help` conflict check skipped, with the row part skipped on its record alone, and with the orphan search skipped so a corrected re-run writes a second `edit` record · none

## 8. Open questions

- **F1 — Two entries of one plan on one `target`.** Options: (a) refuse the plan, exit 2, naming both
  sections and the tag; (b) apply the entries in plan order, each reading the row the earlier left, so
  the second meets the first's `help` and the conflict refusal fires; (c) merge them, the helps joined and
  each edge appended. (b) refuses the same plans as (a) naming one section only; (c) adds a merge grammar
  and a record whose `Promoted-from` names two sections where PLAY-dOrderedCharter-15 S7 gives one.
  RESOLVED (agent, 2026-11-04, delegated): (a), rung 3, the narrowest: a plan
  PLAY-dConvergedCharter-7's pass writes that meets it fails at that pass naming both sections, and a
  merge is specced only when one does. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-04 · initial draft, promoted by the disposal of
  `2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1` for finding 27 (MEDIUM, item M13),
  repairing PLAY-dConvergedCharter-13, whose `apply` it extends; PLAY-dConvergedCharter-7's S7, §3, §10 and
  AC12 rewritten as this unit's sibling edit (its rev-4), and PLAY-dConvergedCharter-13's §3 given the
  hands-off edge (its rev-4).
- rev-2 · 2026-11-04 · S1 S2 S3 §4 §5 §8 AC1 AC2 AC3 §7 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1` findings 16 (the amend's record
  drops `Successor` and sets `Proof`, AC1 holding it to the parent's `edit` shape), 37, the skeptic's
  corrected fix closed with the record written before the row (each part skipped on its own test, the
  plant `amend-interrupted`), and 38 (a plan with two entries on one `target` refused, the refusals
  reading the manifest on disk, §8 F1, the plant `amend-two-sections`).
- rev-3 · 2026-11-05 · S2 S3 AC3 §7 · folded
  `2026-11-05-review-PLAY-dConvergedCharter-11-chain-spec-audit-round2` finding 37 (M19: the orphan
  record an interrupted amend leaves is named: `apply` exits non-zero on it, a re-run with the plan
  changed or not removes an uncommitted orphan before writing its record and refuses a committed one,
  the plants `amend-interrupted-then-edited` and `amend-orphan-committed`, AC3 and the arm).

## 10. Reuse audit

The seam extended is PLAY-dConvergedCharter-13's `guide_move.py apply` and its S4 write route, the one
route an agent pass writes kit rows by, with PLAY-dOrderedCharter-15 S7's change record (`Action edit`
from its `WRITE_VERBS`) and PLAY-dOrderedCharter-9 S2's `read_units` to find the row. `python
tools/codebase-map/reuse_lookup.py "amend an existing instruction unit's help field and edges through
the guarded kit manifest write route"` ranks name-stem hits only at base, since neither `guide_move.py`
nor `instructions.toml` exists yet (unit 13 §4 Evidence: `git ls-files` prints neither at
`d8a12f046`); no existing callable amends a manifest row, so no existing seam fits beyond the deferred
`apply`, and this unit adds a branch to it rather than a second mover or writer. The probe, run at
`45022c64a`, ranked name stems only (`write`, `resolve_kit_dir`, `write_text`, `manifest`, `field`,
`units`), none a manifest-row writer. The recall probe's hits past this spec were scout A's row on the
`help` fields unit 7 renders, unit 7's AC12 (the append-only rationale route this unit amends), and
TOOL-dLinkedLibrary-27's ask on `instructions_edit.py add --manifest`; none amends an existing row, which
agrees with unit 13 §8 F2's ruling that an agent pass writes kit rows as its own kit edit under a change
record, the rule S2 keeps to.

Recall terms used: `python tools/memory-recall/query.py "how does an agent pass add rationale to an
existing instruction unit without a second row" --terms "instruction unit help field amend edit change
record guide_move apply kit manifest one-fact explains edge"`
