# KICK-dKeptSession-15 — a compaction's summary read as a lead, never a source

**Status:** DEFERRED · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 11 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0153@9a9b7d43 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-26 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

After a compaction a session knows where it is from the harness's summary, a model's paraphrase that
nothing checks, and the replay hook gives it only the stored card and a `now —` line
(`skills/session-kickoff/manifest-check.sh:719-725`). The design's test after each compaction is
"position re-derived from witnesses; a summary is a lead, never a source"
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:300`; the design
overview's compaction rule; gap-orient-14). This unit prints, in the replay, the build's position as
TOOL-dDeclaredLoop-7's engine re-derives it from witnesses, and after a compaction one notice that
the summary is a lead to check against it, never a source.

## 2. Scope (IN)

- **S1** — The position line. `render_position_line <slug>` in
  `skills/session-kickoff/manifest-check.sh` runs `python <loop kit>/position.py <slug> --json`
  (TOOL-dDeclaredLoop-7 S7) under `CARD_POSITION_BOUND = 10` seconds and prints `position — <answer>
  · next <item tag>`, `<answer>` the JSON's `answer` and `<item tag>` its `next.item`, or `none` when
  the answer is not `act`. The slug is the session card's `## route` `- build:` value, the one
  TOOL-dPlacedRequest-2 S7's lookup reads. Observed by AC1, AC2.
- **S2** — The skips. No route naming a build prints `position — skipped: the card routes no build`;
  no loop kit resolvable as an optional sibling prints `position — skipped: no loop kit`; a call past
  its bound prints `position — skipped: position.py did not answer within 10s`; exit 2 prints
  `position — invalid-input · next none`. Observed by AC3.
- **S3** — The lead notice. When the replay's hook payload names `"source": "compact"`, read from the
  payload TOOL-dPlacedRequest-2 S7 already captures for `transcript_path`, the replay prints, directly
  after the position line, `lead — the compaction summary is a lead, never a source: check it against
  the position above and the card's pointers`. A `resume` source prints no notice. Observed by AC4.
- **S4** — Witnesses over the card. The position line is always the engine's answer, never the card's
  stored `item —` pointer (KICK-dKeptSession-13): where the two disagree the line prints the
  engine's, and the pointer stays as written until the next item boundary rewrites it. Observed by
  AC2.
- **S5** — The slots. Both lines print at the place KICK-dKeptSession-12 S5's replay order gives
  them, after `partial —` and before `context —`. Observed by AC5.
- **S6** — The plants `position-act`, `position-awaiting`, `position-disagrees`, `position-skips`,
  `lead-compact` and `lead-resume` in `skills/session-kickoff/card-store.fixture.sh`, the loop kit a
  stub answering the planted JSON. Observed by AC1 to AC5.
- **S7** — `help/orientation-card.md` gains the two lines and what a session does with them. Observed
  by AC6.

## 3. Non-goals (OUT)

- The position itself, its witnesses and its answers: TOOL-dDeclaredLoop-7's engine, called here.
- A check that the summary agrees with the position: the session reads both; nothing here parses a
  summary.
- What the harness keeps across a compaction, and a pre-compaction flush: compaction CX-3's owed
  checks, outside this clause.
- The `next` command and its executor: dWellOiledMachine's; the replay prints the engine's answer
  and acts on nothing.

### Edges

- **consumes-from** `KICK-dKeptSession-12` — `print_replay`, with I10's replay order, which places the `position —` and `lead —` lines after `partial —`; without it the lines have no fixed slot
- **consumes-from** `KICK-dKeptSession-13` — `## pointers`, the section the lead notice points a compacted session at beside its position, and whose `item —` pointer S4 never lets stand in for the engine's answer
- **consumes-from** external — dDeclaredLoop's position engine, `position.py <slug> --json` (TOOL-dDeclaredLoop-7 S1, S5, S7), which reads witnesses only

## 4. Design

### Evidence

- `print_replay` at base: the stored card, then one `now —` line, and nothing re-derived but HEAD
  (`manifest-check.sh:719-725`).
- The replay hook fires on `resume` and `compact` (`skills/session-kickoff/orientation-replay.fragment.json`,
  matcher `resume|compact`), so its payload's `source` tells the two apart.
- The engine reads only commits and their trailers, the transition record, the loop definition, the
  run-state file's parked entries and the remote-tracking refs (TOOL-dDeclaredLoop-7 S1): a witness
  reading, which is what the clause asks the position to be.
- The night pass's row cites "dDeclaredLoop unit 29" as the owner; v2's dKeptSession row moved the
  clause here (v2:1771), so that pointer is stale (scout C).

### The lines

```
partial — 0 uncommitted path(s) · resume.partial: continue-item · kept, the item continues
position — act · next item.build.pass
lead — the compaction summary is a lead, never a source: check it against the position above and the card's pointers
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `render_position_line`, `render_lead_notice` | shell functions, `manifest-check.sh` | `sh.function`, asked at the pass |
| `CARD_POSITION_BOUND` | constant | none declared |
| `position —`, `lead —` | replay lines | none |
| the six plants of S6 | fixture cases | none |

### Migration

None: two lines added to the replay's output.

### Rollout

Live at landing. Until the loop kit is built the line reads `position — skipped: no loop kit`.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`: S1 to S5; `KIT_MANIFEST_VERSION` moved
- `skills/session-kickoff/manifest-check.test.sh`: the arm the §7 line declares
- `skills/session-kickoff/card-store.fixture.sh`: S6's plants
- `help/orientation-card.md`: S7

### Alternatives rejected

- **The engine's own `position —` line copied into the replay.** It starts `position — <slug> ·
  state …`, so the replay would carry two spellings of one prefix; the JSON's two fields render I10's.
- **The lead notice on every replay.** A resume carries no summary, and a notice on every start
  stops being read.
- **The position read from the card's pointers.** A pointer is a stored reading, which is exactly what
  the clause says a session must not take as a source.

## 5. Production-readiness checklist

- security — the replay prints two fields of the engine's JSON, each held to one line of printable
  text; the slug is the route's, already held to `[A-Za-z0-9]+`.
- perf / scale — one bounded engine call per replay, only on a routed card.
- error / empty / loading states — every failure is a `skipped` line naming why, and the replay still
  prints the card.
- observability — the two lines themselves.
- risks — a slow engine adds up to ten seconds to a resume; the bound caps it.
- testing — S6's plants, red and green.
- migration — none.
- user docs — `help/orientation-card.md`, S7.

## 6. Acceptance criteria

- **AC1** — When `bash card-store.fixture.sh --plant position-act` replays a card routed to `tFix`
  with a stub engine answering `act` at item `item.build.pass`, the output carries `position — act ·
  next item.build.pass`; the plant `position-awaiting` prints `position — awaiting · next none`.
  Red when: the line is absent, or a non-`act` answer names an item.
- **AC2** — When the plant `position-disagrees` replays a card whose `item —` pointer names
  `item.design.spec` while the stub engine answers `item.build.pass`, the line names
  `item.build.pass`.
  Red when: the replay takes the stored pointer over the engine's answer.
- **AC3** — When the plant `position-skips` replays an unrouted card, then a routed one with no loop
  kit, then one whose stub sleeps past `CARD_POSITION_BOUND`, the line reads `skipped: the card
  routes no build`, `skipped: no loop kit` and `did not answer within 10s`.
  Red when: a failure prints nothing, or blocks the replay past its bound.
- **AC4** — When the plant `lead-compact` replays with a payload naming `"source": "compact"`, the
  `lead —` notice follows the position line; with `lead-resume`, `"source": "resume"`, no `lead —`
  line prints.
  Red when: a compaction's replay carries no notice, or a resume's carries one.
- **AC5** — When the plant `lead-compact` replays a routed card, `grep -n` over its output puts
  `partial —`, `position —` and `lead —` at increasing line numbers.
  Red when: either line prints outside I10's slot.
- **AC6** — When `grep -n "lead —" orientation-card.md` runs over the help page, it finds S7's
  section naming `position —`.
  Red when: the page does not say what the notice asks.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC2 AC4 · the position and lead lines over a stub engine, the failing case a replay that prints the card's stored `item —` as the position · none

## 8. Open questions

- **F1 — Does the lead notice print after a resume too?** Options: (a) after a compaction only; (b)
  after every replay. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the clause's "a
  compaction's summary": a resume restores the transcript and carries no summary.
  widens: none · relaxes: none
- **F2 — Which output of the engine does the replay render?** Options: (a) `position.py --json`'s
  `answer` and `next.item`; (b) the engine's `position —` line copied. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3: it renders I10's spelling, which KICK-dKeptSession-12 fixes, and keeps
  one spelling per prefix in one output. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 15, the night pass's compaction row, the
  design overview's compaction rule, TOOL-dDeclaredLoop-7 S1 and S7, and scout C's row for this unit.

## 10. Reuse audit

The seams extended are `print_replay` (`skills/session-kickoff/manifest-check.sh:721`), with
KICK-dKeptSession-12's order of its lines, and TOOL-dDeclaredLoop-7's engine through its `--json` CLI;
the payload's `source` is read from the capture TOOL-dPlacedRequest-2 S7 makes for `transcript_path`,
never a second read of stdin, since `read_session_id` (:293) consumes it. `python
tools/codebase-map/reuse_lookup.py "print the re-derived position after a compaction replay"` ranked
name stems only (`build_spec_path_re`, `derive_baseline_additions`, `derive_clause_hash`,
`derive_scope`); none re-derives a position, and the engine is not on this tree's map at base, so no
existing seam fits the line beyond the replay itself. Scout C's row agrees with source on the replay
at base and on the stale "dDeclaredLoop unit 29" pointer. The recall query returned scout C's row and
the brief's line for this unit.

Recall terms used: `python tools/memory-recall/query.py "how does a session re-derive its position after compaction instead of trusting the summary" --terms "compaction summary lead never a source position engine witnesses print_replay orientation-replay gap-orient-14"`
