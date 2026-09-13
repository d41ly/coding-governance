# TOOL-aReplayedCard-2 — SessionStart matchers, two card fragments, a rematching merge, a wiring arm

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-2 · base c4f02308 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

Wire the card verb into the harness: write it at `startup` and `clear`, replay it at `resume` and
`compact`, and stop the two existing SessionStart entries from running on every compaction. Ship
the wiring as fragments `settings-merge.py` applies, teach that merger to re-match an entry it
already owns, and add the `check-wiring.sh` arm that reds when a matcher is missing or misspelled,
because a SessionStart matcher that never fires looks exactly like one that is wired.

## 2. Scope (IN)

- **S1** Two fragment files beside the engine, in the shape `settings-merge.py` reads: one with
  event `SessionStart`, matcher `startup|clear`, command `bash <hook_path> --card --registry
  <registry>`; one with matcher `resume|compact` and `--card --replay`. `hook_path` carries the
  `{kit}` token the sibling fragments carry. Observed by AC1.
- **S2** `tools/settings-merge.py` REMATCHES: when an entry carrying the fragment's marker sits in a
  group whose matcher differs from the fragment's, the entry moves to the fragment's group and the
  emptied group is dropped. Today the merger finds a group by exact matcher and would append a
  second entry while the old, matcher-less one kept firing. Observed by AC2.
- **S3** The two existing SessionStart entries in `.claude/settings.json` — `check-wiring.sh
  --session` and `procmon-hook.js` — gain matcher `startup|resume|clear`, so neither runs at
  `compact`. The check-wiring entry gains a fragment so S2 can re-match it; the procmon entry is
  re-matched through its kit's fragment gaining a SessionStart sibling. Observed by AC3.
- **S4** A `card` arm in `tools/check-wiring.sh` on the recall arm's pattern: fragment absent →
  `skip`; fragment present and either SessionStart entry absent or carrying a different matcher →
  `UNWIRED` naming the entry and the matcher it expected; both present → `ok`. Observed by AC4.
- **S5** `WIRE-INTO-PROJECT.md` gains one step: apply the two fragments with `settings-merge.py
  --fragment`, run `check-wiring.sh --check`, and read the deny's ceiling from the hooks README.
  NOT OBSERVED by a criterion: runbook prose.
- **S6** The `--registry` value in this repository's settings is `AGENTS.md`, the file holding the
  node registry table; an adopter names its own. NOT OBSERVED: a settings value; AC1 observes the
  fragment carries the token and the hook README states it.
- **S7** The session-kickoff dossier claims the two fragment keys the codebase-map inventory will
  enumerate, in the same commit. Observed by AC5.

## 3. Non-goals (OUT)

- No `UserPromptSubmit` and no `PreCompact` hook; the design record's harness area rejects both.
- No change to the hooks' commands beyond the matcher; `check-wiring --session` keeps its
  report-never-rewrite rule (`TOOL-aBatchedTribunal-1f`).
- No `SubagentStop` hook; stage 2.
- No CI wiring.

### Edges

- **consumes-from** `KICK-aReplayedCard-1` — the verb the two entries call; without it both
  SessionStart entries run a bash script that refuses.
- **consumes-from** external — the harness's SessionStart matcher vocabulary `startup`, `resume`,
  `clear`, `compact`, confirmed from the hooks documentation in the design record's appendix
  (verdicts 3 and 16).

## 4. Design

### Data model

The fragment schema is the sibling's: `{name, event, matcher, marker, hook_path}`, one event per
file. The card needs two matchers on one event, so two files. The re-match in S2 keys on the
`marker`, which is what "this is our hook" already means to the merger.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `orientation-card.fragment.json` | fragment | `skills/session-kickoff/` | kebab like the siblings |
| `orientation-replay.fragment.json` | fragment | `skills/session-kickoff/` | kebab |
| `check-wiring.fragment.json` | fragment | `tools/` | kebab; the SessionStart entry it wires |
| `procmon-session.fragment.json` | fragment | `tools/process-monitor/` | kebab; the SessionStart sibling |
| `rematch` | verb inside `merge()` | `settings-merge.py` | a step, not a new function unless the body demands one; if extracted it leads with `set` |

### Migration

An installed tree runs `python tools/settings-merge.py --fragment <each>` once; the re-match moves
the two existing entries under their matchers without duplicating them. `check-wiring.sh --check`
reports UNWIRED until then, which is the migration's own signal.

### Rollout

Live at the commit. The first SessionStart after it writes the card; the first compaction replays.

### Files touched (estimate)

| Path | Change |
|---|---|
| `skills/session-kickoff/orientation-card.fragment.json` | new |
| `skills/session-kickoff/orientation-replay.fragment.json` | new |
| `tools/check-wiring.fragment.json` | new |
| `tools/process-monitor/procmon-session.fragment.json` | new |
| `tools/settings-merge.py` | the re-match branch and its self-test arm |
| `tools/check-wiring.sh` | the `card` arm |
| `tools/check-wiring.test.sh` | arms for S4 |
| `.claude/settings.json` | four matchers, two new entries |
| `WIRE-INTO-PROJECT.md` | one step |
| `memory/map/features/session-kickoff.md` | the fragment keys |
| `tools/hooks/README.md` | the `--registry` note beside the deny section |

### Alternatives rejected

**Editing `.claude/settings.json` by hand and shipping no fragment.** An adopter then has no
merge path and the wiring arm has nothing to compare against.

**One fragment carrying a matcher list.** The merger's schema is one matcher per fragment; widening
the schema for one consumer is a second grammar.

**Leaving the existing entries matcher-less.** Measured 35–81 s per compaction for the wiring
check; the design record's improvement 3.

## 5. Production-readiness checklist

- security — N/A. Settings edits through the existing merger.
- perf / scale — two fewer hook runs per compaction; the card run replaces neither.
- error / empty / loading states — a fragment missing a field is refused by the merger and
  reported UNWIRED by the arm, as today for scratch-guard.
- observability — the `card` arm line on every SessionStart.
- risks — a misspelled matcher never fires; the arm compares the literal.
- testing — `settings-merge.py` self-test arm for the re-match; `check-wiring.test.sh` arms.
- migration — one merger run per installed tree.
- user docs — `WIRE-INTO-PROJECT.md`.

## 6. Acceptance criteria

- **AC1** — When `python tools/settings-merge.py --fragment` is run on a scratch settings file with
  `orientation-card.fragment.json` and then `orientation-replay.fragment.json`, the result holds
  two SessionStart groups with matchers `startup|clear` and `resume|compact`, each carrying one
  entry whose command names the resolved checker path and the verb.
  Red when: the two fragments collapse into one group or the `{kit}` token survives unresolved.
- **AC2** — When the merger's self-test seeds a settings file holding the marker under a
  matcher-less SessionStart group and applies a fragment naming matcher `startup|resume|clear`,
  the result holds exactly one entry with that marker, under the new matcher, and no empty group.
  Red when: a second entry is appended and the old group survives.
- **AC3** — When `.claude/settings.json` at the landing commit is read, every SessionStart group
  carries a `matcher`, and none carries `compact` except the replay group.
  Red when: the wiring check or procmon still fires on compaction.
- **AC4** — When `bash tools/check-wiring.sh --check` runs at the landing commit it prints an `ok
  card` line; when the self-test stages a settings file whose replay entry carries matcher
  `resume` alone, the arm prints `UNWIRED card` naming `compact`.
  Red when: a narrowed matcher passes as wired.
- **AC5** — When `python tools/codebase-map/check_gate_coverage.py` and the map coverage leg run at
  the landing commit, the two fragment keys are claimed by the session-kickoff dossier.
  Red when: a new inventory key is unclaimed.
- **AC6** — When one compaction is forced in a session on this branch after landing, the transcript
  shows the card's bytes re-injected after the compaction boundary, verbatim, followed by one
  `now —` line, and no `check-wiring` output.
  Red when: the replay entry never fires or fires the writer instead.
  fixture: one live session; recorded in the acceptance ledger with the session id.
  cost: one manual compaction, minutes.

## 7. Gates

`settings-merge selftest` · `check-wiring self-test` · `hook destinations (every declared hook path ships)` · `process-monitor wiring` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `memory hygiene`

New arm: `tools/settings-merge.py` self-test · the marker under a matcher-less group · none, the self-test asserts inline
New arm: `tools/check-wiring.test.sh` · a replay entry whose matcher lacks `compact` · its own count line

The full bar is owed with `GATE_SELFTESTS=1`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seams are `tools/settings-merge.py`'s `merge()` at lines 199–232, whose marker-and-path
compare is the two-question shape the re-match extends with a third question, and the recall arm
of `tools/check-wiring.sh` at lines 434–488, the one arm that already distinguishes `skip` from
`UNWIRED` on fragment presence. `python tools/codebase-map/reuse_lookup.py` run for this build returned `agent-cap.topLevelArgs`
and `registry.toml` as seams; the fragment schema was read from `tools/hooks/scratch-guard.fragment.json`
and `tools/process-monitor/procmon-hook.fragment.json`.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
