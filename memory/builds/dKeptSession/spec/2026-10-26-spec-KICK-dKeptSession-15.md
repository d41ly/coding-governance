# KICK-dKeptSession-15 — a compaction's summary read as a lead, never a source

**Status:** CLOSED · rev-4 · 2026-11-22 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 11 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0153@9a9b7d43 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-26 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-build-KICK-dKeptSession-15-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-15-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-KICK-dKeptSession-16-reground-orders-7-13-returns.md](../build/2026-11-21-build-KICK-dKeptSession-16-reground-orders-7-13-returns.md) | research | KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 |
| [2026-11-22-build-KICK-dKeptSession-15-red-fix-14.md](../build/2026-11-22-build-KICK-dKeptSession-15-red-fix-14.md) | red-fix | — |
| [2026-11-22-build-KICK-dKeptSession-15-red-fix-15.md](../build/2026-11-22-build-KICK-dKeptSession-15-red-fix-15.md) | red-fix | — |
| [2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md](../build/2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 KICK-dKeptSession-79 KICK-dKeptSession-80 KICK-dKeptSession-89 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md) | research | KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-26 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 |
| [2026-11-21-prompt-KICK-dKeptSession-15-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-15-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-15-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-15-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-15-orders-11-12-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-15-orders-11-12-reground-brief.md) | research | KICK-dKeptSession-14 |
| [2026-11-21-prompt-KICK-dKeptSession-26-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-26-precheck-brief.md) | research | KICK-dKeptSession-26 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

After a compaction a session knows where it is from the harness's summary, a model's paraphrase that
nothing checks. The replay hook gives it the stored card, the build card's `card —` line, the
`route —`, `resume —` and `partial —` lines TOOL-dPlacedRequest-2 S7 landed, and a `now —` line
(`skills/session-kickoff/manifest-check.sh#print_replay`, `#derive_resume_lines`); none of them says
where the build stands. The design's test after each compaction is "position re-derived from
witnesses; a summary is a lead, never a source"
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md@4f5e5809f696:300`;
the design overview's rule,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-design-overview.md@c705dfd0c158:162`;
gap-orient-14). This unit prints, in the replay, the build's position as TOOL-dDeclaredLoop-7's
landed engine re-derives it from witnesses, and after a compaction one notice that the summary is a
lead to check against it, never a source.

## 2. Scope (IN)

- **S1** — The position line. `render_position_line <slug>` in
  `skills/session-kickoff/manifest-check.sh` finds the engine as `resolve_kit_file loop position.py`
  (`#resolve_kit_file`, the resolver `print_rekeyed_card` uses for `claims.py`) and runs `python
  <loop kit>/position.py <slug> --json` (`tools/loop/position.py#main`) in the session's own tree,
  `CARD_TREE`, entered by a `cd` in the call's subshell: `main` takes no root and derives the
  toplevel of its working directory, while the engine itself runs in `$ROOT`. It runs under
  `CARD_POSITION_BOUND`, which KICK-dKeptSession-13 mints at order 9 with its
  fixture-only env override for the same engine read and this unit reuses, stdin closed and its
  output into a scratch file, the way `derive_map_block` bounds the map (`#derive_map_block`). It
  prints `position — <answer> · next <item tag>`: `<answer>` the JSON's `answer`, held to a member of
  `tools/loop/position.py#ANSWERS`, and `<item tag>` its `next.item`, held to `[A-Za-z0-9._-]+`, or
  `none` when the answer is not `act`. Both fields are read by a bash `[[ =~ ]]` match over the
  output, as `read_session_id` reads the payload's fields, so no second process parses it. The
  engine prints with `json.dumps`' default separators, so the match reads `"answer": "<word>"` and
  `"next": {"item": "<tag>"`, anchored on `next` since `frontier` and `refusals` rows also carry
  an `item` field. The slug
  is the one `read_card_build` takes from the session card's `## route` (`#read_card_build`), which
  `print_replay` already holds. Observed by AC1, AC2.
- **S2** — The skips and the refusal. A card whose route names no build prints `position — skipped:
  the card routes no build`; no `position.py` resolving prints `position — skipped: no loop kit`; no
  Python, or no working `timeout -k`, prints the skip `derive_map_block` prints for the same cause
  with the `position —` prefix; a call past its bound prints `position — skipped: position.py did not
  answer within <bound>s`; an exit other than 0 or 2, or output S1's match does not read, prints
  `position — skipped: position.py printed no answer this replay reads`. The engine exits 2 after
  printing its JSON on `invalid-input`, and argparse exits 2 too on a refused command line, printing
  only a usage line (`tools/loop/position.py#main`). So an exit 2 is read by S1's match as exit 0
  is: an answer of `invalid-input` prints `position — invalid-input · next none`, and any other
  output prints the unreadable skip above, never `invalid-input`. Observed by AC1, AC3.
- **S3** — The lead notice. `render_lead_notice` prints, directly after the position line, `lead —
  the compaction summary is a lead, never a source: check it against the position above and the
  card's pointers` when `CARD_SOURCE` reads `compact`. `read_session_id` already keeps the payload's
  `source` in `CARD_SOURCE` (`#read_session_id`, PLAY-dOrderedCharter-54 S1), so nothing here reads
  stdin again. That reader reads the payload only when no `--session` is given and stdin is not a
  terminal, so a replay run with `--session`, or with stdin closed, has an empty `CARD_SOURCE` and
  prints no notice. Any other source, `resume` among them, prints no notice. Observed by AC4.
- **S4** — Witnesses over the card. The position line is always the engine's answer, never the card's
  stored `item —` pointer (KICK-dKeptSession-13 S2): where the two disagree the line prints the
  engine's, and the pointer stays as written until the next item boundary rewrites it. Observed by
  AC2.
- **S5** — The slots. Both lines print at the place KICK-dKeptSession-12 S5's replay order, I10, gives
  them: after `partial —`, before KICK-dKeptSession-14's `context —`, and before the `now —` line,
  which stays last as `print_replay` prints it. Observed by AC5.
- **S6** — The plants `position-act`, `position-awaiting`, `position-disagrees`, `position-skips`,
  `lead-compact` and `lead-resume` in `skills/session-kickoff/card-store.fixture.sh`, appended to its
  `PLANTS`, which the manifest-check suite's card-store block runs by `--list`. Each plant writes its
  `<slug> --json` answer, a JSON, an exit code and a delay, into the plant file outside the
  repository that KICK-dKeptSession-13 S9's stub loop kit answers from; this unit adds no second
  stub. Each replays as the fixture's `replay` plant does, its payload piped on stdin with no
  `--session`, never through `run_card_engine`, which closes stdin. The suite's
  `FLOOR_ASSERTIONS` rises by one per new plant
  (`skills/session-kickoff/manifest-check.test.sh@b771dadeb50a:2489`). Observed by AC1 to AC5.
- **S7** — `help/orientation-card.md`'s section "When a session resumes" gains the two lines and what a
  session does with them. Observed by AC6.

## 3. Non-goals (OUT)

- The position itself, its witnesses and its answers: TOOL-dDeclaredLoop-7's engine, called here.
- A check that the summary agrees with the position: the session reads both; nothing here parses a
  summary.
- What the harness keeps across a compaction, and a pre-compaction flush: compaction CX-3's owed
  checks, outside this clause.
- The `next` command and its executor: dWellOiledMachine's; the replay prints the engine's answer
  and acts on nothing.
- The payload's `source` capture: `read_session_id` landed it.

### Edges

- **consumes-from** `KICK-dKeptSession-12` — `print_replay`, with I10's replay order, which places the `position —` and `lead —` lines after `partial —` and before `now —`; without it the lines have no fixed slot
- **consumes-from** `KICK-dKeptSession-13` — `## pointers`, the section the lead notice points a compacted session at beside its position, whose `item —` pointer S4 never lets stand in for the engine's answer; `CARD_POSITION_BOUND`, the bound S1 reuses; and the stub loop kit of its S9, whose plant file S6 writes
- **hands-off** `KICK-dKeptSession-14` — `print_replay`'s `position —` line, the slot the `context —` line follows
- **consumes-from** external — dDeclaredLoop's landed position engine, `position.py <slug> --json` (TOOL-dDeclaredLoop-7 S1, S5, S7), which reads witnesses only

## 4. Design

### Evidence

- `print_replay` (`skills/session-kickoff/manifest-check.sh#print_replay`) prints the stored card,
  re-keyed, then for a routed card `resolve_build_card`'s `card —` line and `derive_resume_lines`'
  `route —`, `resume —` and `partial —` lines, then `now —` last; nothing in it reads the loop kit's
  position.
- The replay hook fires on `resume` and `compact`
  (`skills/session-kickoff/orientation-replay.fragment.json`, matcher `resume|compact`), and
  `read_session_id` keeps the payload's `source`, so the two are told apart with no new read.
- The engine reads only witnesses: commits and their trailers, the recorded moves, the composed items,
  the acceptance records, the run-state file and the remote-tracking tip; no status header decides a
  step (`tools/loop/position.py#derive_position`). `--json` prints the position as one object whose
  `next` is `{"item": …, "unit": …, "actor": …, "key": …}` or `null`, exit 2 only on
  `invalid-input` (`tools/loop/position.py#main`).
- One `position.py dKeptSession --json` run on this tree took 7.3 s (PINNED 2026-11-21, node a),
  answering `act` at `item.build.base` at base c2a407b0: the engine runs the driver's `--plan`
  when no hand-over is set, so a large build costs most of the bound. Three runs at `79144f3f`,
  under the unattended run's own load, took 15.7 s, 9.6 s and 29.4 s (PINNED 2026-11-21, node a),
  two of three past the 10 s `CARD_POSITION_BOUND` (PINNED by KICK-dKeptSession-13).
- The `--json` object's keys run `slug`, `state`, `build_step`, `units`, `next`, `frontier`, and on;
  `next` was `{"item": "item.build.base", "unit": …, "actor": …, "key": …}` in the same run
  (`tools/loop/position.py#main`).
- The night pass's row cites "dDeclaredLoop unit 29" as the owner; v2's dKeptSession row moved the
  clause here
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1771`),
  so that pointer is stale (scout C).

### The lines

```
partial — 0 uncommitted path(s) · resume.partial: continue-item · kept, the item continues, its witness still owed
position — act · next item.build.unit-pass
lead — the compaction summary is a lead, never a source: check it against the position above and the card's pointers
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `render_position_line`, `render_lead_notice` | shell functions, `manifest-check.sh` | `sh.function`, OK by `lexicon.py --suggest` |
| `position —`, `lead —` | replay lines | none |
| the six plants of S6 | fixture cases | none |

### Migration

None: two lines added to the replay's output.

### Rollout

Live at landing. Where the loop kit does not resolve the line reads `position — skipped: no loop kit`.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`: S1 to S5
- `memory/guides/SESSION-KICKOFF.md`: the kickoff manifest, `last-audit` re-stamped, as `watch:`
  names `manifest-check.sh`
- `skills/session-kickoff/card-store.fixture.sh`: S6's plants, written into unit 13's stub plant file
- `skills/session-kickoff/manifest-check.test.sh`: `FLOOR_ASSERTIONS` raised by the six plants
- `help/orientation-card.md`: S7
- `memory/map/generated/symbols.json`: `render_position_line` and `render_lead_notice`, regenerated
  by `gen_map.py --write`, which the bar's codebase-map leg grades

The kit version constants are the lander's to mint (`tools/push-main.sh@78f40c3c2475:27`).

### Alternatives rejected

- **The engine's own `position —` line copied into the replay.** It starts `position — <slug> · state
  …` (`tools/loop/position.py#render_position_lines`), so the replay would carry two spellings of one
  prefix; the JSON's two fields render I10's.
- **A Python reader of the JSON.** A second process per replay for two fields the bash match reads,
  each held to a closed set or a token grammar.
- **The lead notice on every replay.** A resume carries no summary, and a notice on every start
  stops being read.
- **The position read from the card's pointers.** A pointer is a stored reading, which is exactly what
  the clause says a session must not take as a source.

## 5. Production-readiness checklist

- security — the replay prints two fields of the engine's output, the answer held to `ANSWERS` and the
  tag to `[A-Za-z0-9._-]+`; the slug is the route's, already held to `[A-Za-z0-9]+` by
  `read_card_build`.
- perf / scale — one bounded engine call per replay, only on a routed card; the measured cost above
  is most of the bound on this build, which a skip line names when it is passed.
- error / empty / loading states — every failure is a `skipped` line naming why, and the replay still
  prints the card.
- observability — the two lines themselves.
- risks — a slow engine adds up to the bound to a resume, and a build whose engine call exceeds it
  reads `skipped` until the call speeds up; on this build under a run's load that was two calls in
  three (§4 Evidence). The bound is KICK-dKeptSession-13's, read here and not moved.
- testing — S6's plants, red and green.
- migration — none.
- user docs — `help/orientation-card.md`, S7.

## 6. Acceptance criteria

- **AC1** — When `bash card-store.fixture.sh --plant position-act` replays a card routed to `tFix`
  with the stub engine answering `act` at item `item.build.unit-pass`, the output carries `position —
  act · next item.build.unit-pass`; the plant `position-awaiting` prints `position — awaiting · next
  none`, then with the stub printing a JSON whose answer is `invalid-input` and exiting 2 prints
  `position — invalid-input · next none`.
  Red when: the line is absent, or a non-`act` answer names an item.
- **AC2** — When the plant `position-disagrees` replays a card whose `item —` pointer names
  `item.design.unit-spec` while the stub engine answers `item.build.unit-pass`, the line names
  `item.build.unit-pass`.
  Red when: the replay takes the stored pointer over the engine's answer.
- **AC3** — When the plant `position-skips` replays an unrouted card, then a routed one whose loop kit
  holds no `position.py`, then one whose stub sleeps past a `CARD_POSITION_BOUND` the plant lowers,
  the lines read `skipped: the card routes no build`, `skipped: no loop kit` and `did not answer
  within`, and each replay still prints the card; then with the stub printing only a usage line
  and exiting 2, the line reads `skipped: position.py printed no answer this replay reads`.
  Red when: a failure prints nothing, blocks the replay past its bound, or an argparse exit 2 reads
  as `invalid-input`.
- **AC4** — When the plant `lead-compact` replays with a payload naming `"source": "compact"`, piped
  on stdin with no `--session`, the `lead —` notice follows the position line; with `lead-resume`,
  `"source": "resume"`, no `lead —` line prints.
  Red when: a compaction's replay carries no notice, or a resume's carries one.
- **AC5** — When the plant `lead-compact` replays a routed card, `grep -n` over its output puts
  `partial —`, `position —`, `lead —` and `now —` at increasing line numbers.
  Red when: either line prints outside I10's slot.
- **AC6** — When `grep -n "lead —" help/orientation-card.md` runs, it finds S7's paragraph naming
  `position —`.
  Red when: the page does not say what the notice asks.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `policy fixtures` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the position and lead plants of `card-store.fixture.sh` over unit 13's stub engine, run by the suite's card-store block, the failing case a replay that prints the card's stored `item —` as the position, or a notice after a resume · `FLOOR_ASSERTIONS`, raised by one per new plant

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
- rev-2 · 2026-11-21 · §1 · S1 · S2 · S3 · S5 · S6 · S7 · §3 · §4 · §5 · AC1 · AC2 · AC3 · AC6 · §7 ·
  §10 · re-grounded on the landed dDeclaredLoop and dPlacedRequest at base c2a407b0 by
  2026-11-21-prompt-KICK-dKeptSession-15-orders-11-12-reground-brief: every line citation re-cited by
  symbol or blob pin; S3 narrowed to reading `CARD_SOURCE`, which `read_session_id` already keeps, so
  no payload capture is built; S1 bound to the landed `--json` shape, the `ANSWERS` set, the session's
  tree and `derive_map_block`'s bounding, with the env override the fixture lowers; S2 gains the
  no-Python, no-timeout and unreadable-output skips; S6 narrowed to the fixture alone, since the
  suite's card-store block runs every listed plant, so the manifest-check test file leaves Files
  touched, and its stub extends unit 13's; S5 and AC5 place both lines before `now —`, which stays
  last (unit 12 rev-4 S5); the item tags made real ones; the measured engine cost
  pinned; the hands-off edge to unit 14 added for its `consumes-from`; `policy fixtures` named for
  `manifest-check.sh`. No fork moved.
- rev-3 · 2026-11-21 · S1 · S6 · §3 · §4 · fold of KICK-dKeptSession-13 rev-4 under
  2026-11-21-prompt-KICK-dKeptSession-15-orders-11-12-reground-brief: S1 reuses the
  `CARD_POSITION_BOUND` unit 13 now mints, so it leaves the Inventory; S6 writes its answers into
  unit 13's stub plant file and adds no second stub; the edge to unit 13 names both. The replay's
  lines are not boundary lines, so unit 13's detached verb moves nothing here.
- rev-4 · 2026-11-21 · S1 · S2 · S3 · S6 · §4 · §5 · AC1 · AC3 · AC4 · §7 · checked for behaviour
  under `2026-11-21-prompt-KICK-dKeptSession-26-precheck-brief`: an exit 2 reads `invalid-input`
  only where the JSON says so, since argparse's refusals exit 2 too, and AC3 stages one; S1 enters
  `CARD_TREE` by `cd`, as `position.py` takes no root, and anchors its match on `next`; the payload
  reaches `CARD_SOURCE` only with no `--session`, so the plants pipe it as the `replay` plant does;
  the engine re-timed under the run's load; the kickoff manifest's re-stamp, the floor raise and
  `symbols.json` added, the version bump dropped to the lander, and the arm homed in the suite.

## 10. Reuse audit

The seams extended are `print_replay` (`skills/session-kickoff/manifest-check.sh#print_replay`), with
KICK-dKeptSession-12's order of its lines; `resolve_kit_file`, `read_card_build` and
`derive_map_block`'s bounded sibling call for finding, keying and bounding the engine; the
`CARD_SOURCE` that `read_session_id` keeps; KICK-dKeptSession-13's `CARD_POSITION_BOUND` and its
stub loop kit's plant file in the card-store fixture
(`skills/session-kickoff/card-store.fixture.sh#write_card_fixture`); and TOOL-dDeclaredLoop-7's
landed engine through its `--json` CLI (`tools/loop/position.py#main`). `python
tools/codebase-map/reuse_lookup.py "print the re-derived position after a compaction replay"` ranked
name stems only (`derive_kit_prefix`, `derive_tool_root`, `derive_kit_file`), none of which derives a
position; `python tools/codebase-map/reuse_lookup.py "position engine json answer next item"` ranked
`derive_position` in `tools/loop/position.py`, the engine this unit calls and never copies, so no
existing seam fits the line beyond the replay itself. Scout C's row agrees with source on the stale
"dDeclaredLoop unit 29" pointer; its replay row predates TOOL-dPlacedRequest-2 S7's landed resume
lines, re-read above. The recall query returned scout C's row, this spec and the brief's line for
this unit.

Recall terms used: `python tools/memory-recall/query.py "how does a session re-derive its position after compaction instead of trusting the summary" --terms "compaction summary lead never a source position engine witnesses print_replay orientation-replay gap-orient-14"`
