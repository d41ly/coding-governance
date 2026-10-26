# KICK-dKeptSession-38 — the card-fixture verdict passes only while the tested binary is both PATH's and the session's, and an unknown version is red

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 9 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 |
| [2026-10-26-build-KICK-dKeptSession-38-deviation-381.md](../build/2026-10-26-build-KICK-dKeptSession-38-deviation-381.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 58 at HIGH**, report item **H5**. Id 26 is the same defect, found by the
grounding lens, and shares the item; it is promoted as `KICK-dKeptSession-37`. Unit 37 records the
launched binary's version, and this unit is the reader that compares it.

`KICK-dKeptSession-12` S2 passes the verdict when its recorded version equals the version `AI_AGENT`
names now. A pass earned by PATH's binary then switches the always-resume override off for a session
harness that was never tested, a PATH upgrade never makes the pass stale, and with `AI_AGENT` unset
both sides read `unknown` and compare equal. This unit compares the recorded version with both
binaries and reads an unknown one as red. It repairs `KICK-dKeptSession-12` and builds one step after
it (order 9).

## 2. Scope (IN)

- **S1** — id 58. Two comparisons. `read_card_fixture_verdict` answers `pass` only when, beside
  `KICK-dKeptSession-12` S2's verdict and blob tests, the recorded `cli` equals `read_claude_version`
  now (`KICK-dKeptSession-37` S1) and equals the version `AI_AGENT` names now. Otherwise it answers
  `red: recorded under cli <old>, PATH now <new>` or `red: fixture ran cli <x>, this session runs
  <y>`. Observed by AC1 and AC2.
- **S2** — id 58. Unknown is red. A recorded `cli unknown`, an unreadable PATH version or an
  `AI_AGENT` naming no version answers `red: cli version unknown · <which>`, never an equality.
  Observed by AC3.
- **S3** — id 58. The plants `fixture-cli-path-differs`, the recorded version equal to the session's
  and PATH's stub different, and `fixture-cli-unknown`, in
  `skills/session-kickoff/card-store.fixture.sh`. Observed by AC1 to AC3.
- **S4** — id 58. `help/orientation-card.md`'s verdict paragraph (`KICK-dKeptSession-12` S7) says a
  pass holds only while the tested version is PATH's and the session's. `KICK-dKeptSession-12` S2's
  one comparison is superseded by name here and answered in that unit's acceptance ledger. Observed
  by AC4.

## 3. Non-goals (OUT)

- What the verdict records: `KICK-dKeptSession-37`, the id 26 half.
- The `resume —` override's text beyond its reason: `KICK-dKeptSession-12` S3's.
- Running the fixture: `--fixture-run` only, never from a hook.

### Edges

- **consumes-from** `KICK-dKeptSession-12` — `read_card_fixture_verdict`, whose single comparison with `AI_AGENT` this unit replaces with two and an unknown rule (id 58)
- **consumes-from** `KICK-dKeptSession-37` — `read_claude_version` and the recorded `cli` field, the launched binary's version this reader compares

## 4. Design

### Evidence

- `KICK-dKeptSession-12` S2: pass "only when … its version equals the version `AI_AGENT` names now"
  (spec-12 lines 42-46).
- On this node `AI_AGENT` names 2.1.308 and PATH's claude 2.1.292 (the audit's probe, 2026-10-26).
- `derive_cli_line` already compares the two for the `cli —` cell and treats neither as known when
  `AI_AGENT` names no version (`skills/session-kickoff/manifest-check.sh:414-415`).

### The answers

| Recorded | PATH now | `AI_AGENT` now | Answer |
|---|---|---|---|
| 2.1.292 | 2.1.292 | 2.1.292 | `pass` |
| 2.1.308 | 2.1.292 | 2.1.308 | `red: recorded under cli 2.1.308, PATH now 2.1.292` |
| 2.1.292 | 2.1.292 | 2.1.308 | `red: fixture ran cli 2.1.292, this session runs 2.1.308` |
| unknown | any | any | `red: cli version unknown · recorded` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `fixture-cli-path-differs`, `fixture-cli-unknown` | fixture plants | none |

### Migration

None: no verdict file exists before `KICK-dKeptSession-12`.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`: S1 and S2; `KIT_MANIFEST_VERSION` moved
- `skills/session-kickoff/card-store.fixture.sh`: S3's plants
- `skills/session-kickoff/manifest-check.test.sh`: the arm in §7
- `help/orientation-card.md`: S4

### Alternatives rejected

- **Comparing with PATH only.** A session started from an IDE runs a harness PATH does not hold,
  which a pass on PATH's binary says nothing about.

## 5. Production-readiness checklist

- security — none: one more bounded version read.
- perf / scale — one `claude --version` spawn per replay, under `CARD_CLI_BOUND`.
- error / empty / loading states — every unreadable side answers red, so the override fails towards
  a fresh session.
- observability — the reason names the two versions that differ.
- risks — a node whose session harness and PATH binary always differ never passes; the reason says
  so on every replay, and running the fixture with PATH pointed at the session's binary clears it.
- testing — the plants of §6 and the arm in §7.
- migration — none.
- user docs — `help/orientation-card.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `bash card-store.fixture.sh --plant fixture-cli-path-differs` replays with a recorded
  `pass` at `cli 9.9.2`, `AI_AGENT=claude-code_9-9-2_agent` and a PATH stub answering `9.9.1`, the
  `resume —` line's override reason reads `recorded under cli 9.9.2, PATH now 9.9.1`.
  Red when: the reader compares with `AI_AGENT` alone and answers `pass`.
- **AC2** — When the plant's PATH stub answers `9.9.2` and `AI_AGENT` names `9.9.3`, the reason reads
  `fixture ran cli 9.9.2, this session runs 9.9.3`; with all three `9.9.2`, the reader answers
  `pass`.
  Red when: a mismatch passes, or a full match reads red.
- **AC3** — When `--plant fixture-cli-unknown` replays with `AI_AGENT` unset and a recorded `cli
  unknown`, the reason reads `cli version unknown`.
  Red when: `unknown` equals `unknown` and the reader answers `pass`.
- **AC4** — When `grep -n "PATH" orientation-card.md` runs in `help/`, the verdict paragraph names
  both comparisons.
  Red when: the page describes one comparison.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 · the two plants over stub PATH binaries and planted `AI_AGENT` values, staged red by a copy comparing with `AI_AGENT` alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H5 (id 58).

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-12`'s `read_card_fixture_verdict`, with
`KICK-dKeptSession-37`'s `read_claude_version` for PATH and `derive_cli_line`'s `AI_AGENT` parse
(`skills/session-kickoff/manifest-check.sh:414-415`) for the session. `python
tools/codebase-map/reuse_lookup.py "record the version of the binary a fixture launched"` ranked name
stems only, so no other seam compares versions; `derive_cli_line` is the comparison this reader
reuses.

Recall terms used: `python tools/memory-recall/query.py "when is a card-fixture pass stale" --terms
"card-fixture verdict stale cli version AI_AGENT PATH unknown read_card_fixture_verdict always-resume
fresh-when-idle"`
