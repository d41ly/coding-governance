# TOOL-dRankedPlan-8 — the full kickoff only where `kickoff.runs` says: a `kickoff —` line beside the card

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 15 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0376@f1c33063 whole
**Carries:** node:policy-key.kickoff.runs

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-7 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

Every session is told to run the full kickoff and re-derives what its card printed, a median 6
calls. The owner's OR-2 answer: "Full kickoff should be run in a session that doesn't have a card
READY … When a build/flow step is resumed, a card should be looked up first and used to reorient"
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md:259-263`), and
v2 makes that the default of a key with four values (v2:1172). TOOL-dPlacedRequest-3 S5 ships the
default's stand-in as kickoff prose and leaves the key to this build. This unit lands `kickoff.runs`:
one computed `kickoff —` line printed beside the session's card, naming the key's value and whether
this session runs the full kickoff, re-orients from its card, or hands its request to Plan, and the
stand-in's paragraph reading that line instead of its fixed predicate.

## 2. Scope (IN)

- **S1** — The verdict, `derive_kickoff_line` in `skills/session-kickoff/manifest-check.sh`. It reads
  `kickoff.runs` once through `read_card_policy kickoff.runs` (TOOL-dPlacedRequest-2 S11) and the
  session's stored card, and prints `kickoff — <value> · <verdict>`, the verdict by §4's table: the
  card is ORIENTED when its last line matching `CARD_READY_RE`
  (`skills/session-kickoff/manifest-check.sh:995`) is not `READY — none yet`, the predicate R6
  already reads (:1054), and ROUTED when it carries a `## route` heading. Observed by AC1 to AC4.
- **S2** — The skipped form. A refused read, or no policy reader resolved, prints
  `kickoff — skipped: <why> · no-ready-card · <verdict>`, the verdict the catalogue default gives,
  so a session always has a line to follow. Observed by AC5.
- **S3** — Where the line is printed. It is computed and never stored, as the replay's `now —` line
  is: `write_card` (:706) prints it after the card it writes; `print_replay` (:721) prints the stored
  card without any `kickoff —` line and then a fresh one, before `now —`, after
  TOOL-dPlacedRequest-2 S7's lookup has re-keyed the card; and TOOL-dPlacedRequest-2 S6's
  `--card --lookup` prints it after its `card —` line. A session therefore reads a verdict computed
  over the card it holds at that moment. Observed by AC6.
- **S4** — The stand-in armed. TOOL-dPlacedRequest-3 S5's paragraph in
  `skills/session-kickoff/SKILL.md`, before Step 2, takes its test from the `kickoff —` line: `full`
  runs Steps 2 to 4, `re-orient` re-orients from the card and goes to Step 5's hand-back, and `plan`
  takes the request to Plan without Steps 2 to 4. The line's verdict word is the one place the
  value is applied, so the paragraph spells neither the READY predicate nor the key's values, and
  the file stays within its size row, 18432 bytes (`tools/template-size-limits.txt:63`). Observed by
  AC7.
- **S5** — The plants `kickoff-no-ready-card`, `kickoff-opening-a-build`, `kickoff-every-session`,
  `kickoff-plan-absorbs` and `kickoff-refused` in TOOL-dPlacedRequest-2 S12's
  `skills/session-kickoff/card-store.fixture.sh`, each planting one value through S12's stub policy
  kit and a fresh, an oriented and a routed card; and the arm in
  `skills/session-kickoff/manifest-check.test.sh`. Observed by AC1 to AC6, through the `New arm:`
  line.
- **S6** — `help/orientation-card.md` (TOOL-dPlacedRequest-9's page) gains a paragraph on the
  `kickoff —` line: its four values, its three verdicts and when it is printed. Observed by AC8.

## 3. Non-goals (OUT)

- The card, its stores, lookup and replay: TOOL-dPlacedRequest-2's, called here.
- The `entry.orient` row and its body: TOOL-dPlacedRequest-3's; S4 changes the test its stand-in
  paragraph applies and nothing else in it.
- The `plan —` line and `plan.kickoff`: unit 7's.
- What Plan does with a request under `plan-absorbs`: Plan's items, units 2 and 16 among them.
- The catalogue row: `tools/policy/catalogue.toml:204` already holds `kickoff.runs` with its four
  values and default, and no unit writes a catalogue row.
- The reader-coverage arm's view of a `read_card_policy` read: §8 F6 asks dPlacedRequest for it.

### Edges

- **hands-off** `TOOL-dRankedPlan-7` — `render_card`, the card whose cell list this unit leaves as it is, so unit 7's `plan —` cell joins it beside `live —`, while the computed `kickoff —` line follows the card it describes
- **consumes-from** external — dPlacedRequest, built before this build run: `read_card_policy`, the lookup, the replay's re-key and `card-store.fixture.sh` with its stub policy kit (TOOL-dPlacedRequest-2 S6, S7, S11, S12), and the stand-in paragraph S4 arms (TOOL-dPlacedRequest-3 S5)
- **hands-off** external — dPlacedRequest: `read_card_policy <key>` reads counted by `check_policy.py`'s reader coverage, the ask of §8 F6
- **hands-off** `TOOL-dRankedPlan-29` — the computed `kickoff —` line and §8 F6, which that unit's S9 and S23 align with TOOL-dRankedPlan-7 (round-1 spec audit, ids 10, 26)

## 4. Design

### Evidence

- The session card is written at `startup` and `clear` by `--card --write` and replayed at `resume`
  and `compact` by `--card --replay` (`.claude/settings.json:32-49`).
- `render_card` (`skills/session-kickoff/manifest-check.sh:517`) ends every fresh card with
  `READY — none yet` (:544); a kickoff's `--card --append` lands the READY line that orients it, and
  R6 refuses a route on a card that still reads `READY — none yet` (:1054), so a routed card is
  always an oriented one.
- `print_replay` (:721) already prints one line computed at replay and never stored, `now —`.
- `skills/session-kickoff/SKILL.md` is 18310 bytes at base against its 18432-byte row, and
  TOOL-dPlacedRequest-3 S5 and S6 spend prose there.
- `check_policy.py`'s reader coverage counts a `.sh` read only in the shape `policy.py get <key>`
  (`tools/policy/check_policy.py:423-434`).

### The verdict

| `kickoff.runs` | ORIENTED | ROUTED | Verdict |
|---|---|---|---|
| `no-ready-card` (default) | yes | any | `re-orient` |
| `no-ready-card` | no | no | `full` |
| `opening-a-build` | any | yes | `re-orient` |
| `opening-a-build` | any | no | `full` |
| `every-session` | any | any | `full` |
| `plan-absorbs` | yes | any | `re-orient` |
| `plan-absorbs` | no | no | `plan` |

`opening-a-build` runs the full kickoff wherever the card routes no build, since a session with no
routed build is the one that opens one; a READY card with no route, such as an answer-only kickoff,
re-orients under `no-ready-card` and runs the full kickoff here. `plan-absorbs` is OR-2's "Never:
Plan absorbs it": no session runs the full kickoff, and an unoriented one takes its request to Plan.

```
kickoff — no-ready-card · re-orient
kickoff — plan-absorbs · plan
kickoff — skipped: kickoff.runs refused · no-ready-card · full
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_kickoff_line` | shell function, `manifest-check.sh` | `sh.function`, asked at the pass |
| `kickoff —` | computed card line | none |
| `full`, `re-orient`, `plan` | verdict words | none |
| the five `kickoff-*` plants | fixture cases | none |

### Migration

None. A stored card holds no `kickoff —` line, so no card written before this unit needs a rewrite.

### Rollout

Live at landing for every session. Under the default the verdicts equal TOOL-dPlacedRequest-3 S5's
stand-in, so a repository that sets no value sees no change in what its sessions do.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`: S1 to S3, and `KIT_MANIFEST_VERSION` moved
- `skills/session-kickoff/manifest-check.test.sh`: the arm the §7 line declares
- `skills/session-kickoff/card-store.fixture.sh`: S5's plants
- `skills/session-kickoff/SKILL.md`: S4
- `help/orientation-card.md`: S6

### Alternatives rejected

- **The verdict as `SKILL.md` prose.** The file has about 120 bytes left before the parents spend
  theirs, and four values with their predicates do not fit (§8 F1).
- **A cell stored in the card by `render_card`.** A stored verdict goes stale the moment a kickoff
  appends its READY line, and the replay would print the startup verdict to a resumed session that
  is oriented (§8 F3).
- **A `--card --kickoff` verb the session runs.** One more call per session, the cost OR-2 set out
  to remove.

## 5. Production-readiness checklist

- security — no new write path: the line is printed, never stored, and reads one policy value
  through the reader TOOL-dPlacedRequest-2 bounds.
- perf / scale — one bounded policy read and two greps of the card per verb.
- error / empty / loading states — S2's skipped form names the cause and still gives a verdict; a
  missing card reads as neither ORIENTED nor ROUTED.
- observability — the line itself, on every card the hooks print.
- risks — `kickoff.runs` reds `check_policy.py`'s reader coverage once dRankedPlan lands if
  `read_card_policy kickoff.runs` is not counted as a read (§8 F6); `every-session` costs every
  session the full kickoff, which is what the value asks.
- testing — S5's plants and arm, red and green.
- migration — none.
- user docs — `help/orientation-card.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `bash card-store.fixture.sh --plant kickoff-no-ready-card` runs `--card --write`
  for a fresh session, the output ends the card with `kickoff — no-ready-card · full`; after a
  kickoff body with a READY line is appended, `--card --replay` prints
  `kickoff — no-ready-card · re-orient` once, before `now —`.
  Red when: an oriented card reads `full`, or the replay prints the line twice.
- **AC2** — When the plant `kickoff-opening-a-build` replays a READY card with no `## route`, it
  prints `kickoff — opening-a-build · full`, and a READY card routing a build prints
  `kickoff — opening-a-build · re-orient`.
  Red when: an unrouted card re-orients under `opening-a-build`.
- **AC3** — When the plant `kickoff-every-session` replays a routed, oriented card, it prints
  `kickoff — every-session · full`.
  Red when: `every-session` re-orients any session.
- **AC4** — When the plant `kickoff-plan-absorbs` writes a fresh card, it prints
  `kickoff — plan-absorbs · plan`, and an oriented card prints `kickoff — plan-absorbs · re-orient`.
  Red when: `plan-absorbs` prints `full` for any card.
- **AC5** — When the plant `kickoff-refused` has the stub policy kit refuse `kickoff.runs`, the line
  reads `kickoff — skipped: kickoff.runs refused · no-ready-card · full` for a fresh card and the
  card is still written.
  Red when: a refused read prints no verdict, or blocks the card.
- **AC6** — When `grep -c "^kickoff — "` runs over the stored card file after AC1's write, append and
  replay, it counts 0, and `bash skills/session-kickoff/manifest-check.sh --card --check --session
  <sid>` exits 0 on that card.
  Red when: the line is stored, or its presence in output breaks the card's check.
- **AC7** — When `grep -c "kickoff —" SKILL.md` and `wc -c < SKILL.md` run over the kickoff engine,
  the first is at least 1 and the second is at most 18432.
  Red when: the stand-in paragraph still applies its fixed predicate, or the file outgrows its row.
- **AC8** — When `grep -n "kickoff.runs" orientation-card.md` runs over the help page, it finds S6's
  paragraph naming the four values and the three verdicts.
  Red when: the page does not describe the line.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `policy fixtures` · `kickoff engine size <=18KiB`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the five `kickoff-*` plants over S12's stub policy kit, the failing case an oriented card printed `full` under `no-ready-card` · none

## 8. Open questions

- **FACT-QUESTION · F1 — Does the verdict fit as kickoff prose, or must it be a card line?** Probe:
  `wc -c skills/session-kickoff/SKILL.md` against its row at `tools/template-size-limits.txt:63`.
  Observation, 2026-10-26 at `911a7039`: 18310 of 18432 bytes, 122 left before TOOL-dPlacedRequest-3
  S5 and S6 add their prose. Liveness: a file well under its row would admit the prose. RESOLVED
  (agent, 2026-10-26, delegated): a computed line from `manifest-check.sh`, and S4's paragraph names
  only the line. widens: none · relaxes: none
- **F2 — What do `opening-a-build` and `plan-absorbs` test?** OR-2 gives the option text only:
  "Only when opening a build" and "Never: Plan absorbs it". Options for `opening-a-build`: (a) the
  card routes no build; (b) the request's placement disposition is `new`, known only after
  `entry.place`. (b) cannot be printed at session start, which is where OR-2 wants the saving.
  RESOLVED (agent, 2026-10-26, delegated): (a) for `opening-a-build`, and for `plan-absorbs` no full
  kickoff ever, an unoriented session's request going to Plan, rung 3. widens: none · relaxes: none
- **F3 — Stored in the card, or computed beside it?** Options: (a) a cell `render_card` stores; (b)
  a line computed at write, replay and lookup and never stored. (a) reads `full` on every resumed
  card, since the cell was written before the kickoff appended its READY line. RESOLVED (agent,
  2026-10-26, delegated): (b), rung 3, on the replay's `now —` precedent. This moves I15's proposed
  `kickoff —` cell out of `render_card`'s cell list while keeping its line form; the main loop is
  told. widens: none · relaxes: none
- **F4 — The verdict words.** I15 proposes `· full` and `· re-orient`. `plan-absorbs` with no READY
  card is neither: no full kickoff runs, and there is no card to re-orient from. RESOLVED (agent,
  2026-10-26, delegated): a third word, `plan`, rung 3, returned to the main loop as a refinement of
  I15. widens: none · relaxes: none
- **F5 — What does a refused read print?** RESOLVED (agent, 2026-10-26, delegated): the
  `skipped:` form of S2 with the catalogue default's verdict, rung 1: TOOL-dPlacedRequest-2 S11
  reads v2's default until a reader answers, and a session with no verdict would fall back to
  today's every-session kickoff silently. widens: none · relaxes: none
- **FACT-QUESTION · F6 — Is `read_card_policy kickoff.runs` a read the reader-coverage arm counts?**
  Probe: `READER_SHAPES` at `tools/policy/check_policy.py:423-434`. Observation, 2026-10-26: its
  `.sh` row matches only `policy.py get <key>`, so a wrapper call passing the key reads as no reader,
  for this key and for TOOL-dPlacedRequest-2's five. Liveness: a `.sh` line spelling
  `policy.py get kickoff.runs` matches. RESOLVED (agent, 2026-10-26, delegated): the reader stays
  `read_card_policy`, the one card reader, and the main loop is asked to file an ask: target
  dPlacedRequest, "`read_card_policy <key>` reads are invisible to `check_policy.py`'s reader
  coverage", accept: the arm counts `read_card_policy <key>` in a `.sh` file as a read of `<key>`,
  seen red on a planted script whose one read is that call. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 8, OR-2
  (orientation.md:259-263), v2:1172, TOOL-dPlacedRequest-2 S6, S7, S11 and S12,
  TOOL-dPlacedRequest-3 S5, and scout A's row for this unit.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are `skills/session-kickoff/manifest-check.sh`'s card verbs at base,
`write_card` (:706), `print_replay` (:721) with its computed `now —` line, and the READY predicate R6
reads (:1054) through `CARD_READY_RE` (:995); and TOOL-dPlacedRequest-2's `read_card_policy`,
lookup and fixture. `python tools/codebase-map/reuse_lookup.py "card cell saying whether a session
runs the full kickoff or re-orients from its card"` ranked name stems (`run`, `run_git`,
`render_cards_md`, `parse_cell_key`); `render_cards_md` is the codebase map's renderer and none
decides a kickoff, so no existing seam fits the verdict and S1 adds it beside the card verbs. Scout
A named `policy-shim.sh get kickoff.runs` as the read; the card's own reader, `read_card_policy`, is
the one TOOL-dPlacedRequest-2 S11 gives the card, so S1 uses it. The recall query returned the
clause, v2's catalogue row, scout A's row and the fold-brief finding that `entry.orient` had
hard-coded `no-ready-card`, which S4 answers.

Recall terms used: `python tools/memory-recall/query.py "when does a session run the full kickoff instead of re-orienting from its READY card" --terms "kickoff.runs no-ready-card opening-a-build every-session plan-absorbs orientation card READY re-orient OR-2 stand-in"`
