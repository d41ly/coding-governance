# KICK-aReplayedCard-3 — the engine consumes the card at Step 1 and appends at Step 5

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-2 · base c4f02308 · streams kickoff · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Make the kickoff engine read the orientation card a SessionStart hook already put in context instead
of re-running the Step 1 batch, and make its READY card land on disk through `--card --append`, so a
kickoff's outcome survives compaction and the deny can read it. The engine's own rule since
cKeyedLaunchpad, "consume, don't recompute", gets its first live source.

## 2. Scope (IN)

- **S1** Step 1 states that a card opening `orientation —` already in context satisfies the
  orientation batch; the engine runs only the fast-forward the card reports as not yet made, and
  the map-diff when the ff moved. No card → the batch as today. Observed by AC1.
- **S2** Step 5 pipes the READY micro-format, the manifest-audit delta line, the gotcha class
  names, the record ids the recall probe returned and were judged binding, and the open items, to
  `bash <check-script> --card --append --session <sid>`, taking `<sid>` from the card header in
  context. Then it stops exactly as today. Observed by AC2.
- **S3** Step 5b appends the same body plus the build slug and the run-state path, then continues
  without halting, as today. Observed by AC2.
- **S4** The engine's file stays under the `kickoff engine size <=18KiB` gate. The headroom at base
  is 207 B (`wc -c` 18225 against 18432); the two clauses fit by trimming the Step 1 batch prose
  the card now makes redundant. If they do not fit, the fallback is the design record's split of
  Steps 0–2b into a second file with its own size leg, and that is a rev bump with a §9 line, not a
  silent overrun. Observed by AC3.
- **S5** The manifest is re-stamped: `skills/session-kickoff/SKILL.md` is in `watch:`, so this unit
  owes `last-audit` with a delta line in the commit message. Observed by AC4.
- **S6** The session-kickoff dossier claims nothing new here and is refreshed on touch.
  NOT OBSERVED: prose; the coverage leg grades keys, and this unit mints none.

## 3. Non-goals (OUT)

- No subagent, no `.claude/agents/orient.md`, no Step 0 spawn clause. Owner decision 1.
- No change to the manifest body, to Steps 2 through 4, or to the READY card's fields.
- No re-render of the memory-recall Skill line about kickoff probes; that is stage 2.
- No consumption of the card by the unattended driver; `TOOL-aReplayedCard-3` is the resume seam.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the card and its header line; without it Step 1 has
  nothing to consume and runs the batch.
- **consumes-from** `KICK-aReplayedCard-2` — the append verb; without it Step 5 has no way to land
  the READY line and the deny never opens.
- **hands-off** `TOOL-aReplayedCard-3` — the Step 5b path a resumed run reaches.

## 4. Design

### Data model

None new. The body piped at Step 5 is the shape `KICK-aReplayedCard-2` §4 declares.

### Inventory

No identifier is minted; the change is engine prose.

### Migration

An adopter's installed engine is a junction to the tracked copy on this node and a copy elsewhere;
`tools/check-wiring.sh --session` already reports a tracked-versus-installed mismatch, so a stale
copy is visible at the next start.

### Rollout

Live at the commit that lands it. A session without a card sees no change.

### Files touched (estimate)

| Path | Change |
|---|---|
| `skills/session-kickoff/SKILL.md` | Step 1 consume clause; Step 5 and 5b append clause; batch prose trimmed |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp with the delta line |
| `memory/map/features/session-kickoff.md` | refreshed on touch |

### Alternatives rejected

**Restating the card's fields in the engine.** Two answers to one question; the verb's output is
the shape, and the engine points at the verb.

**A UserPromptSubmit hook injecting the card every turn.** Nothing is evicted between turns, per
the design record's harness area; the per-turn cost buys nothing.

## 5. Production-readiness checklist

- security — N/A. Prose in a skill file.
- perf / scale — one fewer git batch per kickoff when the card is present.
- error / empty / loading states — no card → today's Step 1; append refused → the engine reports
  the refusal on the READY card and still stops.
- observability — the READY line on disk.
- risks — the size gate; S4 names the fallback.
- testing — AC3 is the size gate; AC1 and AC2 are observed on one real kickoff after wiring.
- migration — none.
- user docs — the engine is its own document.

## 6. Acceptance criteria

- **AC1** — When `/session-kickoff` runs in a session whose context holds a card, the transcript
  shows no second `git worktree list` or `status --short` batch at Step 1, and the READY card's
  BASE equals the card's.
  Red when: the engine re-derives what the card carried.
  fixture: a session started after `TOOL-aReplayedCard-2` wires the hook; observed once, recorded
  in the acceptance ledger with the session id.
- **AC2** — When that kickoff reaches Step 5, the card on disk ends with the READY line the
  transcript printed, and `bash skills/session-kickoff/manifest-check.sh --card --check` over it
  exits 0.
  Red when: the READY line is printed and never appended, so the next commit is denied.
- **AC3** — When `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` runs at the
  landing commit, it exits 0 and the file is at or under 18432 bytes.
  Red when: the two clauses push the file past the ceiling and the gate reds.
  figure: DERIVED by the gate at observation; 207 B of headroom is the base measurement.
- **AC4** — When `bash skills/session-kickoff/manifest-check.sh` runs at the landing commit, the
  ratchet is green and the commit touching `SKILL.md` carries a `manifest-audit:` delta line.
  Red when: a watched file moved and the stamp did not.

## 7. Gates

`kickoff engine size <=18KiB` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is the engine's own hedge at `skills/session-kickoff/SKILL.md` lines 26–28, "a
SessionStart hook may already have reported worktree/branch state. Consume, don't recompute", which
has had no live source until the card. The probe `python tools/codebase-map/reuse_lookup.py` run for
this build returned `SESSION-KICKOFF.md` and `manifest-check.sh` as the kickoff seams; the engine
line was found by reading the engine.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
