# TOOL-aHeardState-2 — runlog prose: a transcript measure of narration, interjections and pair emission

**Status:** INPROGRESS · rev-2 · 2026-10-13 · node a · Tier-2 · base 2f01150c · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md) | research | TOOL-aHeardState-1 |
| [2026-10-13-review-TOOL-aHeardState-1-2-closing-diff-review-round1.md](../reviews/2026-10-13-review-TOOL-aHeardState-1-2-closing-diff-review-round1.md) | diff-review | TOOL-aHeardState-1 |

<!-- /gen:spec-records -->

## 1. Goal

A gate at the turn end sees one message at a time and only in a routed session. The old charter named
a chat-prose audit and shipped none ("none yet"), with two alarm thresholds. This unit ships it as a
read-only `runlog.py` subcommand, so any session's transcript, routed or not, before or after the
hook existed, can be measured for prose discipline and pair emission after the fact.

## 2. Scope (IN)

- **S1** — `python tools/runlog/runlog.py prose --session <sid>` resolves the session's main
  transcript through `resolve_session_tree` and reads it through `read_records`; `--transcript <path>`
  reads one named file instead. Sub-agent files and records marked `isSidechain` are out. A
  transcript that does not resolve exits 2 naming what was looked for. AC1, AC5.
- **S2** — turns. A turn opens at any main-file user record whose typed text `_read_text` returns,
  whatever its origin — an owner prompt, an idle-wake tick the harness marks `isMeta`, a task
  notification, a hook's feedback; a `tool_result` record never opens one, and an opener that follows
  another with nothing from the assistant between them joins its turn. In a turn, the FINAL MESSAGE is the assistant text after the turn's last `tool_use` block, and each other
  assistant message carrying text, counted once per `message.id`, is one INTERJECTION. AC2.
- **S3** — the figures, one line each: narration share, the interjection characters over all
  assistant prose characters, marked `ALARM` above 40%; interjections per final message as mean, max
  and the count of turns above 3, marked `ALARM` when the mean exceeds 3; and pair emission, the final
  messages carrying the adjacent bare `BUILD`/`SPEC` pair over all final messages. AC2, AC3.
- **S4** — the pair predicate is the one `TOOL-aHeardState-1` defines, re-implemented once in Python:
  the definitions derived from the `<!-- microformats -->` fence of the charter (`--charter <path>`,
  default the toplevel's `AGENTS.md`), rule r1, adjacency, and the derived shapes. A charter with no
  fence prints the pair line as `unknown` naming the file, never as zero. A parity arm runs both
  implementations over one fixture set and requires equal verdicts. AC4, AC6.
- **S5** — report-only: exit 0 on any readable transcript, alarms included. It writes nothing and
  adds no gate leg. NOT OBSERVED — a negative property of the diff, which `git diff --stat` shows.
- **S6** — a fixture transcript under `tools/runlog/fixtures/`, named in `tools/runlog/kit.toml`'s
  withheld list, with arms in `tools/runlog/selftest.py`. AC2, AC3.

## 3. Non-goals (OUT)

- Any gate, leg or threshold that fails a run: the figures are a measure.
- Grading any micro-format but the pair, or any field VALUE.
- Knowing whether a turn ran under a routed build: the transcript does not say, so the pair line
  counts every final message.
- Sub-agent and Workflow transcripts.
- Redaction of message text: the subcommand prints counts only, never message bytes.

### Edges

- **consumes-from** `TOOL-aHeardState-1` — the pair predicate and its grammar derivation, which this
  unit re-implements under a parity arm; without that unit there is no definition to be equal to.

## 4. Design

### Data model

```
prose — <sid> · turns <n> · final messages <f>
narration — <x.x>% of <chars> assistant prose characters · <ok|ALARM> above 40%
interjections — mean <m.m> · max <k> · turns above 3 <t> · <ok|ALARM> above a mean of 3
pair — <p>/<f> final messages carry the BUILD/SPEC pair
```

The pair line reads `pair — unknown · no microformats fence in <path>` when the grammar cannot be
derived. A turn with no assistant text has no final message and counts in `turns` only.

The logic lives in a new module, `tools/runlog/prose.py`, beside `extract.py`, whose readers it
imports; `runlog.py` adds the subparser and prints. The shape compiler mirrors `format-guard.js`
step for step, and the parity arm lives in `tools/hooks/format-guard.test.sh`, the one suite that
can reach both kits, since both are gov-side.

### Files touched (estimate)

- `tools/runlog/prose.py`
- `tools/runlog/runlog.py`
- `tools/runlog/runlog_lib.py`
- `tools/runlog/selftest.py`
- `tools/runlog/kit.toml`
- `tools/runlog/README.md`
- `tools/hooks/format-guard.test.sh`

### Alternatives rejected

- **Shelling out to `node format-guard.js` per final message.** One spawn per message costs ~751 ms
  each on node a, and a session holds hundreds; it also makes the runlog kit require the hooks kit.
- **A third grammar spelling with no parity arm.** Two readers of one fact must be compared, or they
  drift (`two-answers-to-one-question`).
- **Counting interjections per text block.** The harness splits one message into blocks; a reader
  sees a message, so `message.id` is the unit.

## 5. Production-readiness checklist

- security — read-only over the user's own transcripts; prints counts, never text.
- perf / scale — one pass over the main transcript; a 1,162-entry session reads in seconds.
- error / empty / loading states — an unresolvable session exits 2; an empty one prints zeros with
  `turns 0`; a fence-less charter prints `unknown`.
- observability — the four lines are the output.
- risks — a turn-boundary misread skews interjections; the fixture pins the boundaries.
- testing — selftest arms over a fixture with known counts, and the cross-kit parity arm.
- migration — N/A — no stored data.
- user docs — the runlog kit README gains the subcommand; there is no `help/` tree.

## 6. Acceptance criteria

- **AC1** — When `python tools/runlog/runlog.py prose --session 86a064cd-3532-4202-93cd-dd26651975d3`
  runs on node a, it counts more than two turns, its `narration` line reads `ALARM`, and its `pair`
  line reads `<p>/<f>` with `<p>` below `<f>`. Red when: the session does not resolve, the owner-class
  turn rule's two turns come back, or every final message counts as carrying the pair.
  fixture: that session's transcript, present on node a only; it is still live, and has emitted pairs
  since the owner's zero-emission grep, so no count is pinned.
  figure: DERIVED at observation time.
- **AC2** — When `runlog.py prose --transcript` reads the fixture transcript, `turns`, `final
  messages`, the narration percentage, the interjection mean, max and turns-above-3 equal the values
  the selftest pins. Red when: any figure differs, a `tool_result` opens a turn, or blocks of one
  message count twice.
  figure: PINNED in the runlog selftest against the fixture.
- **AC3** — When the fixture's narration share exceeds 40% and its interjection mean exceeds 3, both
  lines read `ALARM`; on a second fixture turn set below both, both read `ok`. Red when: either mark
  ignores its threshold.
- **AC4** — When `--charter` names a file with no `<!-- microformats -->` fence, the pair line reads
  `unknown`. Red when: it reads `0/<f>`, which a missing grammar would fabricate.
- **AC5** — When `--session` names an id with no transcript, `runlog.py prose` exits 2 naming the
  projects root it searched. Red when: it exits 0 with zero figures.
- **AC6** — When the parity arm feeds the same fixture messages to `format-guard.js` and to
  `prose.py`, every pair verdict matches, and a fixture message carrying a correct pair moves the
  count off zero. Red when: the two implementations disagree on any message, or the count cannot move.

## 7. Gates

`runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test`

New arm: tools/runlog/selftest.py · covers AC2 AC3 AC4 AC5 · a fixture transcript with known turns, interjections and pairs; a fence-less charter; an unknown session id · none
New arm: tools/hooks/format-guard.test.sh · covers AC6 · the same fixture messages through both implementations · none

## 8. Open questions

- **F1 — Where does the parity arm live?** Options: `tools/runlog/selftest.py`, calling node; or
  `tools/hooks/format-guard.test.sh`, calling python. Both suites are withheld from adopters. The hook
  suite already builds fixture messages, so it carries the arm without a second fixture set.
  RESOLVED (agent, 2026-10-11, delegated): `tools/hooks/format-guard.test.sh`.
- **F2 — Which interjection statistic carries the alarm?** The old charter's threshold reads "more
  than 3 interjections per final message". The mean is the session-level figure; the max and the
  turns-above-3 count are printed beside it.
  RESOLVED (agent, 2026-10-11, delegated): the mean carries the mark.

## 9. Revision log

- rev-1 · 2026-10-11 · first draft, from the brief record and the kickoff's design defaults.
- rev-2 · 2026-10-13 · S2 · AC1 · §10 · a measurement of session 86a064cd with the draft found two turns,
  because `_derive_owner_class` drops idle-wake ticks and task notifications, which open real turns;
  any typed user record now opens one. The same session has emitted pairs since the owner's grep, so
  AC1 no longer pins a zero.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "transcript prose measure per session"` names `extract_session`
and `resolve_session_tree` in `tools/runlog/extract.py` as seams; this unit imports
`resolve_session_tree`, `build_session_tree`, `read_records` and `_read_text` from there rather than
reading the JSONL again. The thresholds come from the v1 template at 817ce189, which named the audit
`{{PROSE_AUDIT}}` and shipped none.

Recall terms used: micro-format emission final message BUILD SPEC pair state block stop hook chat-prose audit narration
