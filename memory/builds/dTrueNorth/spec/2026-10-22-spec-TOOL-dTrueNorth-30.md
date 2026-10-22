# TOOL-dTrueNorth-30 — the check 21 writer arm declares the undated-artifact exemption its fixture's neighbours declare

**Status:** CLOSED · rev-1 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 13

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-30-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-30-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-30-deviation-32.md](../build/2026-10-22-build-TOOL-dTrueNorth-30-deviation-32.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-30-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-30-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-30-1-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-30-1-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-30-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-30-spec-brief.md) | research | — |
| [2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md) | diff-review | TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-26 TOOL-dTrueNorth-27 TOOL-dTrueNorth-29 |

<!-- /gen:spec-records -->

## 1. Goal

The second writer-test arm of TOOL-dTrueNorth-14
(`tools/memory-tree/check-memory-hygiene.test.sh:3409-3414`), whose failure message reads
`check 21: a record an older harness wrote, merged after the pinning harness landed, fails check 21`,
has never been green. Check 21 fails in its fixture on
`memory/builds/tOne/build/result.json — no Serves line`, an undated artifact the
TOOL-aRepatriatedFork-10 block plants (`:3184`) and leaves in the shared fixture. This unit makes the arm grade the record it is about, and no assertion changes.
Every line cited below was read at `a75750ce5`.

## 2. Scope (IN)

- **S1** — The writer-test arm's conf (`:3403`), today
  `write_pk_conf $'RECORD_UNBOUND_PIN="0"\nSPEC_AUDIT_PIN_CUTOFF="2026-09-01"'`, gains a third line,
  `RECORD_UNDATED_ARTIFACTS="exempt"`. One comment line in the block's header (`:3378-3387`) says why,
  naming this unit. Observed by AC1.
- **S2** — Neither arm of the block changes what it asserts. The first still requires the graded line
  carrying the Q row's exempt count (`:3406`), and the second still reds on `HYGIENE check 21 FAILED`
  (`:3411`). No assertion floor moves. Observed by AC2, and the arm's pass by AC3.
- **S3** — deviation-32, the record of this unit's addition to the roster, is written in this spec
  pass and reads with no malformed field. Observed by AC4.

## 3. Non-goals (OUT)

- Any other arm of the suite, the TOOL-aRepatriatedFork-10 block's planted files included.
- The check 26 `cache hits` half of the partition arm, red at the base and inherited.
- A change to check 21 or to the generator.
- Running any suite or the bar. They are the close's.

### Edges

- **consumes-from** external — the CLOSED units whose fixture this edits: TOOL-dTrueNorth-14 (the
  block and its two arms) and TOOL-dTrueNorth-29 (the record's move into the build's `reviews/`
  folder, S6 there); a frozen spec cannot write the mirroring hands-off line, so they are named here
  in prose

## 4. Design

The fixture tree `_b1` is shared by every block from `:3040` to `:3667`. The rf10 block plants
`result.json` under the build folder and grades it three ways, blank, `exempt` and `grade`
(`:3200-3241`), and nothing takes it out. Every later block whose conf leaves
`RECORD_UNDATED_ARTIFACTS` blank therefore runs check 21 with that file in its missing-Serves
population.

The rf10 header states the fixture's convention for this: `RECORD_UNBOUND_PIN` is declared on every
run so that check 21's pin branch "is never the red these arms read" (`:3178-3179`). The four
TOOL-aRepatriatedFork-32 confs apply it to the artifact too, with `RECORD_UNDATED_ARTIFACTS="exempt"`
(`:3261`, `:3267`, `:3285`, `:3294`). The TOOL-dTrueNorth-5 confs (`:3330`, `:3352`, `:3366`) do not
declare it and need not, because none of their arms reads `HYGIENE check 21 FAILED`. The writer
test's second arm does read it, so its conf takes the same line.

With the key at `exempt`, check 21 sets aside every row whose basename has no leading ISO date and no
`.md` suffix and prints the count (`tools/memory-tree/check-memory-hygiene.sh:1422-1433`). The audit-pin
arm's Q row and its graded line (`:1451-1461`) do not read the key. In the fixture at `:3403` the other
records under `build/` and `reviews/` are legacy-listed (`:3218`, restored at `:3374`) or carry a
Serves line (`:3396`), so `result.json` is the one missing-Serves row, as the brief's debug run showed.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-30-deviation-32.md` (new, this spec pass)

### Alternatives rejected

- **The rf10 block takes `result.json` out after its last arm.** It fixes the cause one block earlier,
  but it changes the tree the TOOL-aRepatriatedFork-32 and TOOL-dTrueNorth-5 arms run over, and it
  leaves the four TOOL-aRepatriatedFork-32 confs declaring an exemption over nothing. Both are other
  arms, which this unit leaves alone.
- **Match the second arm on a narrower failure line.** That loosens what the arm asserts, which the
  goal forbids: a check 21 red from any branch must still red it.

## 5. Production-readiness checklist

- security — N/A — a fixture conf line in a self-test; no write path and no surface.
- perf / scale — N/A — no run is added; the arm's one gate run is unchanged.
- error / empty / loading states — the exemption prints its count on every run (`:1432`), so the
  narrowing is never silent.
- observability — no printed line of the suite changes.
- risks — the exemption could hide an undated artifact the writer test should grade. It cannot: the
  arm's subject is a dated `.md` record, which the filter keeps.
- testing — AC1 to AC4 as probes; the arm under §7, observed RED and then GREEN at the close.
- migration — N/A — no adopter conf or data changes.
- user docs — N/A — no page under `help/` covers the hygiene suite's fixtures.

## 6. Acceptance criteria

Every command runs from the repository root under bash.

- **AC1** — When `awk '/TOOL-dTrueNorth-14 AC4/,/-m tn14-out/' tools/memory-tree/check-memory-hygiene.test.sh | grep -c 'write_pk_conf.*RECORD_UNDATED_ARTIFACTS="exempt"'`
  runs, it prints 1, and the matched line also carries `SPEC_AUDIT_PIN_CUTOFF="2026-09-01"`.
  Red when: the block's conf carries the two keys alone, where the same command prints 0.
- **AC2** — When `git diff -U0 a75750ce5 -- tools/memory-tree/check-memory-hygiene.test.sh` runs,
  its one `-` line is the old conf line, and its `+` lines are the new conf line and one `#` comment
  line; no changed line carries `echo` or a `case` pattern.
  Red when: an arm's pattern or message moves, or a line outside the block changes.
- **AC3** — When a probe replays the fixture into a scratch repository and runs this tree's
  `tools/memory-tree/check-memory-hygiene.sh` once with that repository as its working directory,
  the output carries
  `1 written by a harness before renderAuditBinding` and
  `check 21: 1 undated non-markdown artifact(s) not graded`, and no `HYGIENE check 21 FAILED`.
  The replay is the base tree (`:3044-3069`), the rf10 plants (`:3182-3189`) with the legacy list
  of `:3218`, and the block's commits (`:3392-3401`) with `WF_KIT` set to `tools/workflows`. The conf
  is the base lines of `write_pk_conf` plus the three keys of S1.
  Red when: the same probe with the conf `:3403` writes today prints `HYGIENE check 21 FAILED` naming
  `result.json — no Serves line`.
  fixture: none in the tree; the probe builds it from the suite's own lines.
- **AC4** — When `python tools/memory-tree/deviation_join.py --approval author-recorded` runs after
  deviation-32 is committed, no `malformed:` or `refused:` line names
  `2026-10-22-build-TOOL-dTrueNorth-30-deviation-32`, and the rescope add member for
  `TOOL-dTrueNorth-30` joins it.
  Red when: the record falls outside the grammar, or the add member is recorded by nobody.

## 7. Gates

`memory-hygiene self-test` · `memory hygiene` · `recall floor` · `recall floor arms`

The suite's leg carries the arm. The other three are owed by deviation-32 under `memory/`: the
hygiene gate grades its Serves line, and the two recall legs guard the tree it lands in.

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC3 · check 21's second writer-test arm, red at a75750ce5 on the rf10 block's undated result.json · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft, the writer-test arm's conf declaring the undated-artifact exemption its fixture's neighbours declare, with deviation-32.

## 10. Reuse audit

The unit extends the suite's own fixture-conf seam, the `write_pk_conf` helper
(`tools/memory-tree/check-memory-hygiene.test.sh:3044-3049`), with the key the TOOL-aRepatriatedFork-32
confs already pass it, read at source. `python tools/codebase-map/reuse_lookup.py "declare a conf key
in a shared hygiene fixture so another check 21 branch is never the red an arm reads"` ranked
name-stem neighbours, `read`, `read_text`, `key`, `check` and `load_conf`, none of them a fixture
helper, so the seam is the one the suite's rf10 header names. No helper is minted.

Recall terms used: `python tools/memory-recall/query.py "a shared fixture's leftover artifact reds a
later arm; declare the undated artifact exemption in the arm's conf" --terms "shared fixture leftover
artifact result.json RECORD_UNDATED_ARTIFACTS exempt check 21 write_pk_conf writer test audit-pin
older harness"`
