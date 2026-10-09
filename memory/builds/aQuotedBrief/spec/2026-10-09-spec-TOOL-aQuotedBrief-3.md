# TOOL-aQuotedBrief-3 — every brief item carries its disposition, and `build-complete` grades each one

**Status:** CLOSED · rev-2 · 2026-10-09 · node a · Tier-2 · base fa68a767 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aQuotedBrief-3-6-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aQuotedBrief-3-6-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aQuotedBrief-3-5-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aQuotedBrief-3-5-build-brief.md) | journal | — |
| [2026-10-09-review-TOOL-aQuotedBrief-3-closing-diff-round1.md](../reviews/2026-10-09-review-TOOL-aQuotedBrief-3-closing-diff-round1.md) | diff-review | TOOL-aQuotedBrief-1 TOOL-aQuotedBrief-2 |

<!-- /gen:spec-records -->

## 1. Goal

`build-complete` grades the roster a prompt-mode run wrote for itself, so an item the owner asked for
that orientation merged away, dropped or left unspecced still closes green. This unit makes every
brief item declare its disposition at the pinned BASE, joins those dispositions to the roster at
preflight, and adds a seventh `build-complete` term that refuses the close while any item is neither
built by a CLOSED unit nor parked where the wrap-up surfaces it.

## 2. Scope (IN)

- **S1** — Each `### Items` line of the brief (`TOOL-aQuotedBrief-1` §4 "The record") is one physical
  line ending in exactly one bracketed disposition, §4 "The item grammar". The prompt path in
  `tools/unattended/VERBS.template.md` decides every item's disposition at step 1, where the
  orientation probes already run, and writes it at step 3. Observed by AC1 and AC6.
- **S2** — `--preflight` refuses a prompt-mode run past `PROMPT_BRIEF_CUTOFF` when the record at BASE
  fails §4 "The preflight join": an item with no disposition or two, a `planned` id that is not a unit
  of the README's authored roster at BASE, a roster unit no `planned` item names, or a `duplicate`
  that does not name a `planned` item. It is a new numbered check after unit 1's. Observed by AC1,
  AC2 and AC3.
- **S3** — `build-complete` gains term 7, evaluated after term 6 for a run whose recorded mode is
  `prompt` past the cutoff, §4 "Term 7". Every other run meets the term and says nothing, so no
  existing close changes verdict. Observed by AC4, AC5 and AC7.
- **S4** — The `build-complete` row of `tools/unattended/PROTOCOL.template.md` §4 names the seventh
  term in one sentence, and its render `memory/guides/UNATTENDED-PROTOCOL.md` follows. NOT OBSERVED
  by a criterion: the protocol parity and size legs grade the render.

## 3. Non-goals (OUT)

- A new core Definition-of-Done item. Adding one moves `CORE_FLOOR` in every adopter, because the
  leg refuses a floor below the core count; a term on `build-complete` is the kit's precedent for
  avoiding that (the `specs-audited` arm's comment in `tools/unattended/unattended.sh`).
- Filing items as asks. incms and nicocares run `BACKLOG_MODE` `shards`, where a tracked
  `memory/builds/*/BACKLOG.md` is a generator verdict, and neither declares `ASKS_CMD`; and
  `asks-disposed` grades a self-filed ask as disposed, not closed, so a bare `KEEP` row passes.
- Re-dispositioning an item after BASE. The dispositions are part of the authorization; a later
  change of mind is a parked entry, which term 7 accepts and the wrap-up surfaces.
- Grading whether a `stale` or `duplicate` disposition is true. It is decided at BASE, written in
  the record the owner can read, and confirmed by the owner whenever the brief drew on the session.

### Edges

- **consumes-from** `TOOL-aQuotedBrief-1` — the `### Items` sub-section and `PROMPT_BRIEF_CUTOFF`;
  without them there is no item to dispose of and no switch for the join.

## 4. Design

### Evidence

Read at `fa68a767` on 2026-10-09.

- `build-complete` is the `dod_met` arm at `tools/unattended/unattended.sh:10472`. Its comment says
  "SIX terms, ALL required", evaluated in order, each returning early with its own `DOD_OUT`.
  `unit_rows` and `nonterminal_units` read the generated units region; term 5 carries a DEFERRED unit
  forward through `check_carry_forward`.
- `--rescope --act supersede` requires `--successor` (`:12156`) and writes
  `rescope · item supersede <id> -> <successor>` into the run-state file.
- `park()` (`:11373`) appends one parked line of the shape `<kind> · item <item> · reason <reason>`
  and refuses a newline or ` · ` inside the item, so an item text opening `brief item <n>:` is one
  parseable field.
- Preflight records the mode as the run-state fact `mode` (`write_preflight_record`, `:6788`), so
  term 7 reads it at close without re-reading the README. The join of S2 sits in `verb_preflight`
  beside `TOOL-aQuotedBrief-1`'s check, after the authorization read and before the write gate.
- The leg refuses `CORE_FLOOR` below the kit's core count (`tools/unattended/check-unattended.sh`
  fail 3 and its slack arm), and both adopters declare `CORE_FLOOR="13:13"`.

### The item grammar

```
<n>. <the item, one line> [planned <unit-id>[ <unit-id>]...]
<n>. <the item, one line> [stale <evidence>]
<n>. <the item, one line> [duplicate <m>]
<n>. <the item, one line> [parked <reason>]
```

The disposition is the LAST bracketed group on the line, ASCII only, so a bracket inside the item
text does not move it. `stale` carries the probe that shows the item is already true, `parked` the
reason the run cannot decide it. Numbers start at 1 and rise by one.

### The preflight join

Read once, at BASE, from the prompt record and the README's authored roster pair:

1. Every item line carries exactly one disposition from the four.
2. Every `planned` id is a unit row of the authored roster.
3. Every roster unit is named by at least one `planned` item, so the authorization holds no scope the
   brief did not ask for. A unit the run adds later goes through `--rescope --act add`, as today.
4. Every `duplicate <m>` names an item `m` whose own disposition is `planned`.

### Term 7

For each item, by disposition:

- `planned` — met when every named unit is CLOSED in the generated region at HEAD. A unit superseded
  by a `rescope · item supersede` row is replaced by its successor, followed to the end of the chain.
  Otherwise met only when a parked line's item opens `brief item <n>:`.
- `parked` — met when a parked line's item opens `brief item <n>:`.
- `stale` and `duplicate` — met at BASE.

The unmet message names each item number, its disposition and the unit or park it lacks. A DEFERRED
unit that term 5 carried forward leaves its item unmet until the run parks the item, so the carry
reaches the wrap-up as an item the owner asked for and did not get.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_brief_items` | function | `sh.function`; `python tools/lexicon/lexicon.py --suggest read_brief_items --as sh.function` answered OK |
| `check_brief_items` | function | `sh.function`; `python tools/lexicon/lexicon.py --suggest check_brief_items --as sh.function` answered OK at build time |

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `tools/unattended/VERBS.template.md` · `tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-VERBS.md` · `memory/guides/UNATTENDED-PROTOCOL.md` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **A new verb recording each disposition after BASE.** It lets a run decide late what the owner
  confirmed early, and it adds a record kind for what one bracket on the authorized line carries.
- **Joining items to asks.** See §3: not available in either adopter, and graded as disposed rather
  than closed.
- **Reading the verbatim prompt's bullets.** A mid-session prompt may hold no bullets at all ("yes,
  spec it as a build"); the brief is where the run states the items it was asked for.

## 5. Production-readiness checklist

- security — no new write path; one more refusal at preflight and one more term at close.
- perf / scale — one `git show` of the record at BASE, already read by unit 1's check, and one read
  of the run-state file at close.
- error / empty / loading states — a brief with no items is refused by unit 1's rule 2, so term 7
  never grades an empty population.
- observability — every unmet item is named with its number and what it lacks.
- risks — a run can mark an item `stale` to skip it. The disposition is in the authorized record, and
  a session-derived brief is confirmed by the owner before the push.
- testing — arms in `tools/unattended/unattended.test.sh` over the `readme`, `scope published`,
  `run --preflight` and `run --close` fixtures, run once at VERIFYING.
- migration — none: the cutoff grades by README `opened:` date.
- user docs — the verbs file's prompt path and the protocol's DoD row.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs over a prompt-mode record whose item 2 carries no bracketed
  disposition, it refuses at the new check naming item 2 and join rule 1.
  Red when: the item is admitted, or the refusal names no item.
- **AC2** — When item 1 is `[planned TOOL-tBr-9]` and the authored roster holds no `TOOL-tBr-9`,
  `--preflight` refuses naming join rule 2; when the roster holds a unit no item names, it refuses
  naming join rule 3.
  Red when: either a dangling plan or unrequested scope passes.
- **AC3** — When item 2 is `[duplicate 3]` and item 3 is `[stale ...]`, `--preflight` refuses
  naming join rule 4.
  Red when: a duplicate of an item nothing builds is admitted.
- **AC4** — When `--close` runs over a fixture whose item 1 plans a unit ended WONTDO, with no park
  naming `brief item 1:`, the `build-complete` message names item 1 and the unit.
  Red when: a planned item whose unit was abandoned closes green.
- **AC5** — When the same unit was superseded through `--rescope --act supersede --successor` and
  the successor is CLOSED, term 7 is met; with the successor WONTDO, it is not.
  Red when: the chain is not followed, or a WONTDO successor passes.
- **AC6** — When `grep -n "\[planned" memory/guides/UNATTENDED-VERBS.md` runs, the prompt path shows
  the four dispositions and says step 1 decides them.
  Red when: the render lacks the grammar.
- **AC7** — When `--close` runs over a slug-mode build, and over a prompt-mode build whose README
  predates the cutoff, `build-complete` verdicts and messages are those at BASE.
  Red when: term 7 grades a run it does not cover.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC7 · the HEAD driver, which admits a brief with no dispositions and closes it green · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §4 · build: the four join rules share check 115, each naming its rule and,
  for an item, the item number last; `check_brief_items` is term 7 and `read_brief_items` the item
  parser both use; term 7 also runs on term 6's `SPEC_THIN_CUTOFF`-blank exit, where term 6 is off.

## 10. Reuse audit

`reuse_lookup.py "record a self-contained brief of an unattended prompt-mode run, quoting session
context, and refuse unrelated commits on the run branch"` returned no seam for item grading. The
extended seams are the `build-complete` arm of `dod_met` and its readers `unit_rows`,
`nonterminal_units` and `check_carry_forward` in `tools/unattended/unattended.sh`; the rescope and
park lines are read in the shapes their writers already emit. The asks route was probed and rejected
in §3.

Recall terms used: `prompt record verbatim authorized-by prompt published anchor branch tip
self-authorization orientation AskUserQuestion owner turn build folder roster` — the same query as
`TOOL-aQuotedBrief-1`, which surfaced `TOOL-aPromptedMandate-5` and `TOOL-dNarrowedAnchor-1`.
