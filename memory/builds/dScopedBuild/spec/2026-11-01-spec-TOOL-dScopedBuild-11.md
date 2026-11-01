# TOOL-dScopedBuild-11 — a playbook's pieces built as units, each piece record joined to its unit's build commit by hash, and a proposal to amend the playbook filed as an ask

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 11 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0409@5b78cbe2 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-10-reuse-scout-d.md](../build/2026-11-01-build-TOOL-dScopedBuild-10-reuse-scout-d.md) | research | TOOL-dScopedBuild-10 TOOL-dScopedBuild-12 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-6 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

A run following a playbook records each piece it produced (`record_piece`,
`tools/unattended/unattended.sh:13115`), and no piece record names the roster unit that built it, so
"a playbook's pieces built as units" (the night pass, point 1) has nothing to join. A run that would
amend its playbook parks a `proposal` row in its `RUN.md` (`verb_propose`, `:12940`), a file that
rotates with the run, and the owner's queue never sees it. This unit gives every piece record a
`unit:` field, joins it by hash to that unit's build commit at the recipe close, and files each
proposal as an ask in the run's own `BACKLOG.md` through the kit's one ask filer.

## 2. Scope (IN)

Build-run precondition: TOOL-dIndexedDesign-11 has landed, so `tools/unattended/check-playbook.sh`
sources `lib-unattended.sh` (its S2) and `derive_set_identity` exists (its S1). dIndexedDesign is a
parent.

- **S1** — The field. `record_piece` takes a seventh argument, the unit id, refused by the composite
  field guards (`:13131-13137`) exactly as the six others are, and refused unless it is id-shaped by
  the driver's `_ids_of`. The first write puts `unit: <id>` between the `run:` and `playbook-sha:`
  header lines (`:13151`, `:13152`). A later write sets it with `set_field` (`:13096`), as `hash:` is set
  at `:13158`, or inserts it after `run:` when the record has no `unit:` line. `--record-piece`
  requires `--unit <id>`: the verb's row in `VERB_REQUIRES` (`:823`) names it, `check_verb_flag`
  reads it in `verb_record_piece` (`:13254`), and both of that verb's calls pass the `--unit` value
  the parser already holds in `BR_UNIT` (`:14440`). The synopsis line (`:29`) names the flag.
  Observed by AC1, AC2.
- **S2** — The join. Under `check-playbook.sh --counts <playbook> <run> <at>`, the census loop
  (`:595-650`) grades a record that passed its stale test as `unjoined` when it carries no `unit:`
  line, when `build_commit "<at>..HEAD" <unit> <the run's build folder> "$GENERATED_INDEXES"
  "$SHARED_RECORDS" "" ""` (`tools/unattended/lib-unattended.sh:1186`, the newest-first window) leaves
  `_BC_OUT` empty, or when `git rev-parse <that commit>:<piece>` differs from the record's `hash:`.
  An `unjoined` piece is counted in no other state. The machine line gains a seventh field,
  `unjoined=<n>`, after `unchecked=`. The merge-bar mode has no base and grades no join; its census
  note gains `unjoined not graded: no base`. Observed by AC3, AC4, AC5.
- **S3** — The close. The `pieces-complete` arm of `--close` (`unattended.sh:11499-11525`) reads
  `unjoined=` as it reads the other fields, and a new term after TERM 2b refuses a non-zero count:
  `a piece this run produced names no unit, or its unit's build commit does not hold the bytes its
  record hashes, so it was not built as a unit: <n> unjoined`. NOT OBSERVED by a criterion: the
  term is reached only through `--close`, which runs the bar, so a pass cannot reach it; the
  `unattended.test.sh` arm of §7 observes it at the close over the suite's stub bar, and AC4 observes
  the count it reads.
- **S4** — The set. A set's identity is `derive_set_identity` (TOOL-dIndexedDesign-11 S1), which reads
  `hash:` lines only, so the `unit:` field moves no set record and no set check. Observed by AC6.
- **S5** — The proposal as an ask (I20). `verb_propose`, after its guards and before `park()`, files
  one ask in `<MEMORY_ROOT>/builds/<slug>/BACKLOG.md`: the family is `read_roster_family`'s, the id
  `<family>-<slug>-<derive_ask_seq>` (`:9780`), the rows the three of §4 "The ask", written through
  `write_ask_rows` (`:9984`) at `LOW`, then `write_ask_views 1` (`:9854`). The reason joins the refused
  shapes: a reason spelling ` · ` is refused with fail 48, as the item and step already are (`:12954`),
  because the ask row's clause grammar splits on it. The run-state row is written as before with its
  reason field `filed as <id>`, so the ask holds the reason once and the row points at it, and
  `--status`'s noted count reads one row per proposal as it does today. Observed by AC7, AC8.
- **S6** — Reuse first and the dark path. An OPEN ask in that `BACKLOG.md` whose text carries
  `playbook amendment: <item> at step <step>,` is reused, printing `proposal already filed as <id>`
  and writing nothing, the reuse `write_inherited_asks` makes (`:10030-10041`). With `ASKS_CMD` blank
  the verb files no ask, parks the row with its reason as today, and prints
  `propose: ASKS_CMD is blank, so the proposal is parked in the run-state file and filed as no ask`.
  Observed by AC8, AC9.
- **S7** — The filer's voice (I20). `write_ask_rows` prints its two outcome lines under the prefix
  `gates-green:`. An optional tenth argument names the caller's prefix, `gates-green` when absent, so
  the two gates-green callers (`:10078`, `:10272`) print byte for byte what they print at base; with a
  prefix other than `gates-green` the filed line reads `<prefix>: filed ask <id> for <subject>, <SEV>,
  staged in <path>`, carrying no `red at` clause. Observed by AC7.
- **S8** — The carrier. `tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`, says in its `--propose` bullet (`:694-697`) that a proposal is
  filed as an ask in the run's `BACKLOG.md` and its run-state row names that ask, and in its
  `--record-piece` synopsis that `--unit` names the unit that built the piece. Observed by AC10.

## 3. Non-goals (OUT)

- The playbook kind, its resolver and its set check: TOOL-dIndexedDesign-10 and -11. This unit adds
  a field and a census state; the set identity is S1 of TOOL-dIndexedDesign-11, unchanged.
- Deriving a build's roster from a playbook's pieces: a playbook entering Design as a `repeat` build
  is dPlacedRequest's and dIndexedDesign's; a unit here is whatever id the roster already holds.
- Grading the join on the merge bar: it has no base (§8 F1).
- Amending the playbook from the ask: the ask is the owner's queue, and a separate authoring run
  answers it.
- A shared filing factory over the three callers: `write_ask_rows` is already the kit's one copy of
  the write, read-back and rollback (`:9972-9974`); what each caller adds is the row text it composes
  (§8 F4).

### Edges

- **hands-off** `TOOL-dScopedBuild-12` — `write_ask_rows`, as S5 makes `--propose` its third caller and S7 gives it the caller's prefix, the filer unit 12's open rows past `flow.route-backs` go through
- **consumes-from** external — TOOL-dIndexedDesign-11 S1 and S2, `derive_set_identity` and the library `check-playbook.sh` sources, DEFERRED at base and a parent's
- **hands-off** external — dIndexedDesign's set check reads the piece records this unit extends, and their `hash:` lines are unchanged
- **hands-off** `TOOL-dScopedBuild-35` — S1's `--unit` in the unattended Skill and the attended form, S14; S6's reuse keyed on the whole text, S31; S7's prefix passed by `write_gate_asks`, S34; and its new functions in `symbols.json`, S17 (ids 29, 49, 8, 33)

## 4. Design

### Evidence at base

- The record header is written once (`unattended.sh:13142-13153`): `piece:`, `hash:`, `run:`,
  `playbook-sha:`; `hash:` is re-stamped on every later write (`:13156-13159`). Its readers take each
  field by `sed -n 's/^<key>: //p'` (`check-playbook.sh:251`, `:617`, `:619`), so an added line moves
  none of them.
- `build_commit`'s seventh argument, passed empty, walks newest-first (`lib-unattended.sh:1189-1191`),
  and the answer is left in `_BC_OUT` for a caller in its own shell.
- No tracked run-state file records `mode: recipe` (`git grep` over `memory/builds/*/RUN*.md` at
  `5f0b11f12` finds none), so requiring the field breaks no recorded run. The tracked fixture records
  under `tools/unattended/fixture-records/` are read by the merge-bar mode only, which grades no join.
- The ask grammar: `- <id> · filed <date> · <text> · seen <locator> · accept <value>`
  (`tools/memory-tree/backlog.py:23-30`); a locator is `` `<path>`@<sha7+> ``.

### The join

```
for each piece record of run <run> under the playbook's records root, past the stale test:
  unit  := the record's `unit:` value                     -> none: unjoined
  c     := build_commit "<at>..HEAD" unit <build dir> GENERATED_INDEXES SHARED_RECORDS "" ""
                                                          -> empty: unjoined
  blob  := git rev-parse c:<piece>                        -> != hash: unjoined
  else  -> on to the failed / unchecked / verified tests, unchanged
```

The newest build commit is the piece as its unit last built it. A fix pass that edits the piece moves
the newest commit and the record's re-stamped `hash:` together; a later commit of another unit that
edits the piece leaves the record stale first, a state `pieces-complete` already refuses.

### The ask

```
- <id> · filed <date> · playbook amendment: <item> at step <step>, proposed by run <slug>: <reason> · seen `<playbook path>`@<base sha8> · accept the playbook amends step <step> as proposed, or the owner rules the proposal declined
- SEV · <id> · LOW · a playbook step a run following it proposed to amend
- KEEP · <id> · filed by a recipe run for the playbook's author; outside this build's goal
```

The playbook path and base are the run's `playbook` and `base` facts, the reading `verb_record_piece`
makes (`:13274`). The subject handed to `write_ask_rows` is `proposal <item> at step <step>`.

### Inventory

Minted: the record field `unit:`; the census state and machine field `unjoined`; the `--record-piece`
requirement `--unit`; `write_ask_rows`' optional tenth argument; the ask text `playbook amendment:`.
No function is minted.

### Migration

Additive for the bar. A recipe run started before this lands records pieces without `--unit` and its
`--close` refuses on `unjoined`; it re-records each piece with `--unit`, which inserts the field.

### Rollout

Live at landing. The unattended kit's version moves (`KIT_UNATTENDED_VERSION`, `unattended.sh`).

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/check-playbook.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-playbook.test.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **Joining against the unit's first build commit**, `build_commit`'s default `--reverse` window.
  Tested by reading `record_piece`: the `hash:` is re-stamped on every write, so a fix pass that edits
  the piece makes the record disagree with the first commit and an honest piece reads `unjoined`.
- **Joining on the merge bar.** The bar has no run and no base (`check-playbook.sh:514-516`), so the
  range `build_commit` walks does not exist there.
- **Keeping the proposal's reason in both the run-state row and the ask.** Two copies of one fact,
  which the charter's one-fact rule refuses.

## 5. Production-readiness checklist

- security — every new field passes the composite guards already on the writer, and the reason now
  also refuses the separator the ask row parses on; the ask is written only through `write_ask_rows`,
  whose read-back rolls a row back that the generator cannot read.
- perf / scale — one `build_commit` walk and one `rev-parse` per recorded piece at `--counts`; the
  walk is bounded by the run's range.
- error / empty / loading states — a record with no `unit:` is a named state, never a silent pass;
  a blank `ASKS_CMD` is announced and keeps today's row.
- observability — `unjoined=<n>` on the machine line, and the close names the count; the filed ask is
  printed with its id and path.
- risks — a recipe run in flight at landing is refused at its close until it re-records with
  `--unit` (§4 "Migration").
- testing — AC1 to AC10 by a pass in a scratch clone; the arms of §7 at the close.
- migration — §4.
- user docs — `memory/guides/UNATTENDED-VERBS.md` (S8); no `help/` page covers recipe mode
  (`help/README.md`).

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --record-piece tX --path tools/unattended/fixture-pieces/one/piece.md`
  runs in a scratch clone with `--leg L --verdict PASS --unit TOOL-tX-1 --records-root <dir>`, the
  record written holds `unit: TOOL-tX-1` on the line after `run:`; without `--unit` the verb exits
  non-zero naming `--unit` (check 112).
  Red when: a piece record is written naming no unit.
  fixture: a scratch clone under `%TEMP%`, written by the pass.
- **AC2** — When the same `--record-piece` runs again on a record whose `unit:` line was deleted by
  hand, the record holds one `unit:` line after `run:`; a `--unit` value spelling ` · ` exits non-zero
  with fail 47.
  Red when: a re-write leaves an older record unjoinable, or a forged field reaches the record.
- **AC3** — When `bash tools/unattended/check-playbook.sh --counts <playbook> tX <at>` runs in the
  clone after a commit naming `TOOL-tX-1` wrote both fixture pieces and each was recorded with that
  unit, its machine line ends `unjoined=0`.
  Red when: a piece its unit built reads as unjoined.
- **AC4** — When the clone's second record names `TOOL-tX-2`, which no commit names, `--counts` prints
  `unjoined=1` and `verified=1`; with the `unit:` line deleted from that record it prints
  `unjoined=1` again.
  Red when: a planted piece whose hash matches no unit's build commit is counted verified.
- **AC5** — When the clone's first record keeps its unit and its `hash:` is set to the blob of the
  piece's previous version, while the working file matches it, `--counts` counts that piece
  `unjoined=1` and not `verified`.
  Red when: a record whose hash names bytes its unit's build commit does not hold is verified.
- **AC6** — When `bash -c '. tools/unattended/lib-unattended.sh ; derive_set_identity tools/unattended/fixture-records dScriptedRepeat'`
  runs in the clone before and after a `unit:` line is added to both fixture records, it prints the
  same identity both times.
  Red when: the field enters the set identity, so every recorded set reads superseded.
- **AC7** — When `bash tools/unattended/unattended.sh --propose tRun --item "name the register once" --step F4 --reason "two pieces read it two ways"`
  runs in a clone holding the suite's run-state `tRun`, the `BACKLOG.md` of `tRun`'s build folder in
  the clone holds one ask whose text carries `playbook amendment: name the register once at step F4,`,
  a `SEV · <id> · LOW` row and a `KEEP` row; the run-state row ends `reason filed as <id>`; and the verb prints
  `propose: filed ask`.
  Red when: a proposal is parked in the run-state file and reaches no ask.
- **AC8** — When AC7's command runs a second time, the `BACKLOG.md` still holds one such ask and the
  verb prints `proposal already filed as`; a `--reason` spelling ` · ` exits non-zero with fail 48.
  Red when: a repeated proposal mints a second id, or a reason breaks the ask row's grammar.
- **AC9** — When AC7's command runs with `ASKS_CMD=` declared blank in the clone's `.unattended.conf`,
  no `BACKLOG.md` row is written, the run-state row keeps the reason, and the verb prints
  `filed as no ask`.
  Red when: the dark path writes an ask it cannot read back, or parks nothing.
- **AC10** — When `grep -c 'filed as an ask' memory/guides/UNATTENDED-VERBS.md` runs at the pass tip it
  prints at least 1, and `grep -c -- '--record-piece --path --leg --verdict --unit' tools/unattended/unattended.sh`
  prints 1.
  Red when: the carrier still says a proposal is only a run-state row, or the flag is not required.

## 7. Gates

`unattended kit gate` · `playbook validity gate` · `pass-order history` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC7 AC8 AC9 · the record-piece, propose and recipe close cases, the close's `unjoined` term (S3) among them, over the suite's `tRun`, staged red by writing the record without `unit:`, by skipping the `unjoined` term and by parking before filing · none
New arm: tools/unattended/check-playbook.test.sh · covers AC3 AC4 AC5 AC6 · the `--counts` cases over a committed fixture unit, staged red by reading the record's hash where the census reads the blob at the build commit · none

## 8. Open questions

- **F1 — Where is the join graded?** Options: (a) under `--counts`, the census the recipe close reads;
  (b) also on the merge bar; (c) in the `pieces-complete` arm alone, outside the census. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3: the census is "the sole evidence for `pieces-complete`" (`check-playbook.sh:230-231`) and holds the base the join's range needs; (b) has no base on the bar; (c) is a second census beside the first. widens: none · relaxes: none
- **F2 — Is `unit:` required on every piece record?** Options: (a) required, at write and in the
  census; (b) optional, joined when present; (c) required only for a build whose README carries a
  roster table. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the most feature-rich survivor: the clause has every piece built as a unit, (b) lets a piece no unit built pass the close, and (c) adds a condition no record asks for; no tracked recipe run exists to break (§4 "Evidence at base"). widens: none · relaxes: none
- **F3 — Does `--propose` keep its run-state row?** Options: (a) file the ask and write no row;
  (b) file the ask and write the row with its reason field `filed as <id>`; (c) the row alone.
  RESOLVED (agent, 2026-11-01, delegated): (b), rung 3: it files the ask the clause asks for and keeps `--status`'s noted count and the `proposal` kind every reader of `PARK_KINDS` (`unattended.sh:875`) already handles, with the reason held once; (a) needs the kind's readers re-pointed for no gain the clause names; (c) fails the clause. widens: none · relaxes: none
- **F4 — Is a filing factory extracted over the three callers?** Options: (a) `verb_propose` calls
  `derive_ask_seq` and `write_ask_rows` as the two gates-green filers do; (b) a new factory
  re-pointing those two. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3: I20 spells the route as those two functions and "no new ask writer", and `write_ask_rows` is already the one copy of the write, read-back and rollback; the rest each caller composes differently. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 11, scout D's row 11 and its piece-unit
  join interface, shared interface I20, and the sources read at `5f0b11f12`.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are the piece writer `record_piece` and its verb `verb_record_piece`
(`tools/unattended/unattended.sh:13115`, `:13254`); the census of `check-playbook.sh --counts`, the
one reader `pieces-complete` trusts; `build_commit` (`tools/unattended/lib-unattended.sh:1186`), the
kit's one build-commit predicate, called with its newest-first window; and the ask filer
`derive_ask_seq` and `write_ask_rows` (`:9780`, `:9984`), whose comment calls them "one copy for every
auto-filer". `python tools/codebase-map/reuse_lookup.py "join a playbook piece record to the unit
build commit that built it by blob hash"` ranked `build_commit` (fan-in 7, a SEAM) beside name stems
that read no piece record (`records`, `units`, `read_blobs_at`): the seam S2 calls. Scout D's lines held
at `5f0b11f12` (`record_piece` :13115, `verb_propose` :12940, `park` :12537, `PARK_KINDS` :875,
`write_inherited_asks` :10020); its proposed field position, between `run:` and `playbook-sha:`, is
kept; its note that the join reads `build_commit` is narrowed here to the newest-first window, for the
re-stamp reason in §4.

Recall terms used: `python tools/memory-recall/query.py "how is a recipe run's piece record joined to a unit and a playbook proposal filed" --terms "record_piece piece record hash build_commit verb_propose proposal ask write_ask_rows derive_ask_seq pieces-complete recipe"`
