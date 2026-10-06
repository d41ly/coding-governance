# TOOL-aMendedFleet-70 — runlog's extractor reports what a session spends in tokens and minutes before it reaches READY

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 70

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

The report's context-diet items are argued from one figure: a session spends a median of about
66.7K tokens and 6.7 minutes before its kickoff reaches READY, over 23 sessions. That figure was
computed once by hand and nothing in the tree can compute it again, so no diet unit can show it
moved it. runlog's extractor already streams every
session's transcripts into timed `usage` events. This unit adds one report-only mode over it that
finds each session's READY point and prints what the session spent to reach it, per session and as
quartiles, so the baseline is a command instead of a sentence.

## 2. Scope (IN)

- **S1** — `derive_ready_point(tree)` in `tools/runlog/extract.py` returns the time and the witness
  of a session's first READY with the time of the main file's first timed record, which S2's
  minutes start from, or `None`, reading the MAIN file only, a sidechain record excluded.
  Two witnesses are read, in memory, and nothing of either text is kept:
  - `card` — a shell tool call whose command carries both `--card` and `--append` as words, which
    is how the kickoff engine's Step 5 appends the READY card;
  - `text` — an assistant text block with a line matching `^(?:- )?READY — (?!none yet)\S+ · node `,
    the charter's READY micro-format with or without its list marker.
  The earlier of the two wins. Observed by AC1, AC2 and AC3.
- **S2** — `measure_ready_tree(root)` streams every session under a projects root by the same glob
  `measure_tree` uses, runs `extract_session` and S1 on each, and returns, per session reaching
  READY: its id, the minutes from its first timed record to READY, the requests and the summed
  `in`, `out`, `cache_read` and `cache_write` tokens of every `usage` event at or before READY
  across all sources, and the main thread's context, `in` plus both cache fields, at its first
  request and at its last request before READY. It also returns the sessions scanned and the count
  per witness. Observed by AC1 and AC5.
- **S3** — `runlog.py extract --ready DIR` is a fourth exclusive mode beside `--measure`. It prints
  one summary line `runlog: ready (report-only, grades nothing) sessions=<n> ready=<m> card=<a>
  text=<b>`, one quartile line each for spent tokens, context growth and minutes, and one row per
  READY session. It writes nothing and exits 0; a root holding no session prints
  `runlog: ready DEAD PROBE — no session under <DIR>` and exits 2. Observed by AC1, AC4 and AC5.
- **S4** — `tools/runlog/README.md`'s extractor section gains the command line and one paragraph
  stating what the mode reads, that it keeps times and counts only, and what it cannot see: a
  session that reached READY without either witness, and a text witness quoted inside a longer
  message. Observed by AC7.
- **S5** — The runlog dossier's prose names the mode in one sentence, and the dossier stays under
  its byte cap. Observed by AC8.
- **S6** — A self-test arm drives S1 and S2 over a `ready` scenario added to
  `tools/runlog/fixtures/transcripts.json`. NOT OBSERVED by a criterion here: the suite runs once
  at the close, and the arm is declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- A new extract event kind, tool class or schema field. The mode reads what `extract_session`
  already returns plus S1's scan, so every existing consumer of an extract is untouched, which AC6
  observes.
- First-turn tokens of workflow or sub-agent sidechains. `TOOL-aMendedFleet-93`, split from unit
  67, measures a judge's first turn from its sidechain transcript directly, and neither reads nor
  extends this mode.
- A drift signal, a pin or a gate over the figure. It is a baseline to read, and nothing yet
  decides what value is wrong.
- Disposing of `TOOL-aReplayedCard-9`, which unit 14 already decides.
- Reading narration. The `narration` verb prints text; this mode prints none.
- The runlog kit version bump, owed once at the close after the build's last move of the kit.

### Edges

- **hands-off** external — the runlog kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04 at `efc4b0c9`, whose `tools/` bytes equal base.

- `extract_session` emits one `usage` event per request, keyed by request id, carrying `t`, `src`,
  `in`, `out`, `cache_read` and `cache_write`; `build_usage` already sums them per source.
  `measure_tree` streams every `*/*.jsonl` under a projects root through it and is the shape S2
  copies.
- `derive_tool_class` reads a shell command in memory and keeps only a class, flags, a verb and a
  slug; `manifest-check.sh --card --append` classifies as `other` today, so no event marks READY.
  S1 therefore scans the main file itself rather than widening the closed `CLASSES` list.
- The kickoff engine's Step 5 pipes the READY card into `--card --append --session <sid>`, and the
  card the SessionStart hook injects ends `READY — none yet`. That injection is not an assistant
  record, and the negative lookahead keeps an echoed copy of it from counting.
- `TOOL-cMendedVintage-16` ruled that the card reader accepts an optional leading `- `, so S1's text
  pattern does too.
- This node's projects root is 4.9 GB, PINNED by `du -sh` on 2026-10-04; the extractor's rate is
  what `extract --measure` prints, so AC5's cost is DERIVED from it.

### Inventory

- `derive_ready_point` and `measure_ready_tree`, Python functions in the extractor, and
  `print_ready` in the CLI, each leading with a verb its file already uses.
- The flag `--ready` on `runlog.py extract`.

### Files touched (estimate)

- `tools/runlog/extract.py`
- `tools/runlog/runlog.py`
- `tools/runlog/README.md`
- `tools/runlog/selftest.py`
- `tools/runlog/fixtures/transcripts.json`
- `memory/map/features/runlog.md`
- `memory/map/generated/symbols.json`

### Rollout

Additive and inert until called. An adopter receives it with the kit's next version.

### Alternatives rejected

- **A `ready` tool class in `CLASSES`.** It changes the closed list every extract consumer and the
  self-test's fixture parity are held to, for a fact only this mode reads.
- **Reading the stored orientation cards.** They live in a per-machine store that keeps no record
  of sessions predating the card, while the transcripts do.
- **Text witness only.** An unattended run speaks only in files, so its kickoff may never echo the
  card as text; the append call is the witness it cannot skip.

## 5. Production-readiness checklist

- security — the mode keeps no text: the two witnesses are matched in memory and only a time
  survives, which is the extractor's existing rule.
- perf / scale — one extra pass over each main file beside `extract_session`; AC5 states the cost.
- error / empty / loading states — an empty root is a named DEAD PROBE exit 2; a torn or unknown
  record lands in the extractor's existing coverage block.
- observability — the summary line prints the scanned and witness counts, so a zero READY count
  is distinguishable from a root that matched nothing.
- risks — a text witness can be a quoted READY line; the card witness usually precedes it, and the
  README states the gap.
- testing — AC1 to AC8 directly; the arm in S6.
- migration — N/A — no stored state.
- user docs — S4.

## 6. Acceptance criteria

- **AC1** — When a scratch projects root under a short `%TEMP%` path holds one session written from
  the `ready` scenario of `tools/runlog/fixtures/transcripts.json`, in which the third request's
  turn calls `--card --append`, and `python tools/runlog/runlog.py extract --ready <that root>`
  runs, it prints `sessions=1 ready=1 card=1`, and the session's row names three requests and the
  token sums the scenario's first three `usage` blocks add to.
  Red when: READY is missed, or a request after READY is counted.
  fixture: the scenario is written by this unit; the tree holds none today.
- **AC2** — When that scenario's card call is replaced by an assistant text line
  `- READY — fixture · node a · …` and the mode re-runs, it prints `ready=1` with `text=1`.
  Red when: the text witness is not read.
- **AC3** — When the scenario's only READY line is `READY — none yet` and no card call exists, the
  mode prints `sessions=1 ready=0`.
  Red when: the injected placeholder line counts as READY.
- **AC4** — When `python tools/runlog/runlog.py extract --ready <an empty scratch dir>` runs, it
  prints `DEAD PROBE` and exits 2.
  Red when: an empty root reports a clean zero.
- **AC5** — When `python tools/runlog/runlog.py extract --ready` runs with node a's projects root as
  its argument, it exits 0 with `sessions` and `ready` both above 0, and prints three quartile lines.
  Red when: the real tree yields no READY session, which on this node is a dead witness.
  cost: minutes; the root's size divided by the rate `extract --measure` prints.
  figure: every count is DERIVED at observation time.
- **AC6** — When `python -c` imports `tools/runlog/extract.py` and prints `SCHEMA`, `KINDS` and
  `CLASSES` at base and at the tip, the two outputs are identical.
  Red when: the mode widened the extract contract.
- **AC7** — When `grep -n -- "--ready" tools/runlog/README.md` runs, it hits the extractor's command
  block and the paragraph naming what the mode cannot see.
  Red when: the mode ships undocumented.
- **AC8** — When `wc -c memory/map/features/runlog.md` runs it prints at most 20480, and
  `grep -c -- "--ready" memory/map/features/runlog.md` prints at least 1.
  Red when: the refresh is skipped or breaks the dossier cap.

## 7. Gates

`runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/runlog/selftest.py` · the `ready` scenario with its witness removed, which must report `ready=0` · none

## 8. Open questions

- **F1 — Which witness marks READY?**
  Options: the card append call; the READY text line; the earlier of both. An unattended kickoff
  may never echo the card, and a session predating the card has only the text.
  RESOLVED (agent, 2026-10-04, delegated): the earlier of both, each counted, per S1.
- **F2 — Which tokens are "tokens to READY"?**
  Options: the sum of every request's tokens; the growth of the main context; both. The report's
  "+66.7K" reads as growth, while cost is the sum.
  RESOLVED (agent, 2026-10-04, delegated): both, printed side by side, per S2 and S3.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the extractor and CLI at base and the kickoff engine's
  Step 5.
- rev-2 · 2026-10-04 · §1 · §3 · M2 cross-read: this spec said the A/B unit reads and may extend
  this mode; `TOOL-aMendedFleet-93` reads judge transcripts directly and puts extending the mode
  out of its scope, so the goal, the sidechain non-goal and the hands-off edge now agree with it.
- rev-3 · 2026-10-05 · §2 S1 · build pass: S2's minutes start at the first timed record, which no
  extract event carries, so S1's one scan of the main file returns that time beside READY's rather
  than S2 paying a second pass over the file.

## 10. Reuse audit

The seam extended is `tools/runlog/extract.py`: `measure_tree` is the projects-root walk and
`extract_session` the per-session `usage` source, so S2 adds a walk beside one and reads the other.
`python tools/codebase-map/reuse_lookup.py "sum token usage from session transcripts up to the point
a session reaches READY"` returned `extract_session`, `resolve_session_tree`, `build_usage` and
`build_run_usage` as the nearest seams; `build_usage` sums per source over a whole session and has
no cut point, so S2 sums with a time bound rather than calling it. Recall returned
`TOOL-cMendedVintage-16` on the optional list marker, which S1's pattern follows; `KICK-aReplayedCard-3`
on Step 5 committing after `--card --append`, which makes the append the witness; and unit 14's F3,
which already disposes of `TOOL-aReplayedCard-9`. Where the report and the tree disagree: the
report cites the baseline but the tree holds no instrument that computed it.

Recall terms used: `python tools/memory-recall/query.py "how many tokens and minutes does a session
spend before it reaches READY at kickoff" --terms "tokens-to-READY orientation kickoff READY card
first-turn tokens session transcript usage runlog extract baseline"`
