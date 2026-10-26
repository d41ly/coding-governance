# KICK-dKeptSession-37 — the card-fixture verdict records the version of the claude binary the fixture launched, never the session's environment

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 9 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-37-deviation-371.md](../build/2026-10-26-build-KICK-dKeptSession-37-deviation-371.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 26 at HIGH**, report item **H5**. Id 58 is the same defect, found by the
failure-envelope lens, and shares the item; it is promoted as `KICK-dKeptSession-38`. This unit is the
item's writer half, what the verdict records, and unit 38 is its reader half, what the verdict is
compared with.

`KICK-dKeptSession-12` S1 stamps the verdict with the version `derive_cli_line` reads from
`AI_AGENT`, the session harness, 2.1.308 on this node, while the fixture runs `claude -p` from PATH,
2.1.292. A pass earned by the PATH binary is therefore recorded against a harness that was never
tested, and a PATH upgrade never makes it stale. This unit records the version of the binary the
fixture launched. It repairs `KICK-dKeptSession-12` and builds one step after it (order 9).

## 2. Scope (IN)

- **S1** — id 26. The one PATH read. `read_claude_version <scratch file>` in
  `skills/session-kickoff/manifest-check.sh` is extracted from `derive_cli_line`'s PATH half
  (`skills/session-kickoff/manifest-check.sh:416-428`): `command -v claude`, then `claude --version`
  under `timeout -k 2 "$CARD_CLI_BOUND"` into a scratch file, never a `$( )` capture, and the first
  token of two to four integers. It prints the version or `unknown` with its why on stderr, and
  `derive_cli_line` calls it, so the read lives once. Observed by AC1 and AC3.
- **S2** — id 26. The recorded field. `record_card_fixture_verdict` (`KICK-dKeptSession-12` S1) writes
  `cli <version>` from `read_claude_version`, run immediately before the fixture, the binary the
  fixture's `claude -p` resolves; `cli unknown` when the read fails. It never reads `AI_AGENT`.
  Observed by AC2.
- **S3** — id 26. `KICK-dKeptSession-12` S1's "the harness version `derive_cli_line` reads from
  `AI_AGENT`" is superseded by name here and answered in that unit's acceptance ledger with AC2's
  output. Observed by AC2.

## 3. Non-goals (OUT)

- Comparing the recorded version with today's binaries, and reading `unknown` as red:
  `KICK-dKeptSession-38`, the id 58 half.
- The fixture and which binary it launches: PLAY-dOrderedCharter-8's.
- The report's left-shift checklist entry, that a recorded verdict is keyed to the artefact under
  test. No clause of this build names that checklist.

### Edges

- **consumes-from** `KICK-dKeptSession-12` — `record_card_fixture_verdict` and its `cli` field, which this unit keys to the launched binary instead of `AI_AGENT` (id 26)
- **hands-off** `KICK-dKeptSession-38` — `read_claude_version` and the recorded `cli` field, which the verdict's reader compares with PATH's binary and the session's harness
- **hands-off** `KICK-dKeptSession-56` — `read_claude_version`, `derive_cli_line` and AC1, and §7's legs, the batch's S18, S35, S36 and S26 (ids 24, 12, 55, 35)

## 4. Design

### Evidence

- On this node `AI_AGENT` reads `claude-code_2-1-308_agent`, and PATH's
  `/c/Users/daily-agent/.local/bin/claude --version` prints `2.1.292 (Claude Code)` (the audit's
  probe, 2026-10-26).
- PLAY-dOrderedCharter-8's fixture starts session A with `claude -p`
  (`memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md:170`).
- `derive_cli_line` reads `AI_AGENT` for the session's version (`manifest-check.sh:413-414`) and
  PATH's `claude --version` under `CARD_CLI_BOUND` into a scratch file (`:416-428`).

### The verdict line

```
card-fixture — pass · fixture 3f9c2a71 · cli 2.1.292 · 2026-10-27T09:14:02+0000
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_claude_version` | shell function, `manifest-check.sh` | `sh.function`, `read`, OK |

### Migration

None: no verdict file exists before `KICK-dKeptSession-12`.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`: S1 and S2; `KIT_MANIFEST_VERSION` moved
- `skills/session-kickoff/card-store.fixture.sh`: the plant `fixture-run-cli`
- `skills/session-kickoff/manifest-check.test.sh`: the arm in §7

### Alternatives rejected

- **`AI_AGENT` as the recorded version.** It names the session harness, which the fixture does not
  launch.
- **A second PATH read beside `derive_cli_line`'s.** The two would disagree on a bound or a parse.

## 5. Production-readiness checklist

- security — one bounded `claude --version`, its output parsed as a version token and nothing else.
- perf / scale — one spawn per `--fixture-run`, which already launches two sessions.
- error / empty / loading states — an unreadable version records `cli unknown`, which unit 38 reads
  as red.
- observability — the verdict line names the version tested.
- risks — PATH changing between the version read and the launch is a window of seconds inside one
  verb.
- testing — the plant of §6 and the arm in §7.
- migration — none.
- user docs — `help/orientation-card.md`'s verdict paragraph, `KICK-dKeptSession-38` S4.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'claude --version </dev/null' skills/session-kickoff/manifest-check.sh`
  runs, it prints `1`, the line inside `read_claude_version`, and `derive_cli_line` calls that
  function.
  Red when: the PATH read is written twice.
- **AC2** — When `bash card-store.fixture.sh --plant fixture-run-cli` runs `--card --fixture-run` with
  a stub `claude` on PATH answering `9.9.1 (Claude Code)` and `AI_AGENT=claude-code_9-9-2_agent`, the
  verdict file's line carries `cli 9.9.1`.
  Red when: the line carries `cli 9.9.2`, the session's version.
- **AC3** — When the plant's stub `claude` exits 1, the line carries `cli unknown`.
  Red when: a failed read records the session's version or nothing.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC2 AC3 · the `fixture-run-cli` plant with a stub PATH binary and a different `AI_AGENT`, staged red by a copy recording `AI_AGENT`'s version · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H5 (id 26).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is `derive_cli_line`'s PATH read (`skills/session-kickoff/manifest-check.sh:416-428`),
extracted as `read_claude_version` and called by both it and the verdict writer. `python
tools/codebase-map/reuse_lookup.py "record the version of the binary a fixture launched"` ranked
`records`, `fixture`, `build_fixture` and `write_record` by name stem only; none reads a binary's
version, so `derive_cli_line` is the one seam.

Recall terms used: `python tools/memory-recall/query.py "which claude binary does the card fixture
test" --terms "card-fixture verdict cli version AI_AGENT PATH claude --version derive_cli_line
fixture-run always-resume"`
