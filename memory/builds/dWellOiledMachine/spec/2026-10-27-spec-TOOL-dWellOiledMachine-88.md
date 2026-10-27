# TOOL-dWellOiledMachine-88 — runlog verify's `pruned` test names its population and reads each file's first parseable line as its head

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 4 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-88-deviation-881.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-88-deviation-881.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-90 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`),
finding 61, item H7, at HIGH, the skeptic's corrected fix; item H7 also carries finding 41, which
TOOL-dWellOiledMachine-86 closes. TOOL-dWellOiledMachine-72 S1 requires every producer file "the run's
commitment draws on" to begin with a line whose `t` is later than the run's start. Nothing records
which producers a commitment drew on: the commitment holds only a sha256 and a count
(`tools/runlog/record.py:1301-1303`), and the model is rebuilt from the journal now. Retention
(TOOL-dWellOiledMachine-16 S5) keeps every unparseable line, so a retained file's first line can carry
no `t`. Either way the predicate is undefined or false on a pruned journal, which yields the false
`mismatch` 72 exists to remove. This unit names the population and the head.

## 2. Scope (IN)

- **S1** — The population. 72 S1's test runs over every producer of `mdl.JOURNALS`
  (`tools/runlog/model.py:147`) whose file `rl.PRODUCER_FILES[<producer>]` is present under the
  journal root: the producers `measure_commitment` hashes from (`tools/runlog/record.py:1217-1221`).
  No "recorded prune" and no record of the commitment's producers is consulted, since no unit writes
  one. Observed by AC1.
- **S2** — The head. A file's head is its first line that `rl.parse_line` accepts with a numeric `t`;
  lines before it that do not parse, or carry no `t`, are skipped, as `measure_commitment` skips
  them. A file with no such line is treated as TOOL-dWellOiledMachine-86 treats an empty one.
  Observed by AC2.
- **S3** — 72's S1 sentence corrected. Spec 72 takes a rev bump at this unit's pass whose S1 names
  S1's population and S2's head in place of "every producer file the run's commitment draws on", its
  §9 line naming this unit and finding 61. Observed by AC3.

## 3. Non-goals (OUT)

- An empty or absent producer file is finding 41's, closed by TOOL-dWellOiledMachine-86.
- No change to the prune or to which lines it keeps: 16 S5 stands.
- No change to how a commitment is computed.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-72` — S1's `pruned` predicate, whose population and head this unit defines
- **hands-off** `TOOL-dWellOiledMachine-90` — the population and head, combined with unit 86's empty-file reading in one case (finding 20)
- **hands-off** `TOOL-dWellOiledMachine-94` — §5's security line, which reads an unparseable line as deleted (finding 16)

## 4. Design

### Evidence

- `measure_commitment` iterates `mdl.JOURNALS`, reads `rl.PRODUCER_FILES[producer]` under the journal
  root, and skips a line that does not decode or whose `t` does not parse
  (`tools/runlog/record.py:1217-1230`); `mdl.JOURNALS` is `("driver", "gates", "pushes")`
  (`tools/runlog/model.py:147`).
- `check_commitment` compares only `sha256` and `lines` (`tools/runlog/record.py:1301-1305`).
- 16 S5 keeps unparseable lines through the prune (`spec-16.md:64-66`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `unparseable-head`, `foreign-producer` | `tools/runlog/selftest.py` cases | none |

### Files touched (estimate)

- `tools/runlog/record.py`: S1, S2
- `tools/runlog/selftest.py`: the two cases
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-72.md` (S3's rev bump)

### Alternatives rejected

- **Recording the commitment's producers in the record.** The finder's fix the skeptic rejected: it
  changes the committed record's grammar and still leaves every record rendered before it without
  the list.

## 5. Production-readiness checklist

- security — an edit among the remaining parseable lines stays `mismatch`.
- perf / scale — one forward read per producer file until its first parseable line.
- error / empty / loading states — S2 sends a file with no parseable line to 86's empty-file reading.
- observability — the `pruned` line's `<why>` names the head instant S2 found.
- risks — none beyond 72 S3's stated limit.
- testing — AC1 to AC3 and the arm in §7.
- migration — none.
- user docs — none beyond 72's README section.

## 6. Acceptance criteria

- **AC1** — When the `foreign-producer` fixture case, on its §7 `New arm:` line, adds a `runtime.log` holding
  only old lines beside a pruned `driver.log`, `runlog.py verify <record>` prints `pruned` and exits 0.
  Red when: a producer outside `mdl.JOURNALS` decides the verdict.
- **AC2** — When the `unparseable-head` case puts a line with no `t` at the head of a pruned
  `driver.log`, `verify` prints `pruned —` naming the instant of the first parseable line and exits 0.
  Red when: the unparseable head makes the record read `mismatch`.
- **AC3** — When `grep -n "draws on" 2026-10-27-spec-TOOL-dWellOiledMachine-72.md` runs over spec 72
  after this unit, it prints nothing, and its §9 names this unit.
  Red when: S1 still names an undefined population.

## 7. Gates

`runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/runlog/selftest.py · covers AC1 AC2 · the two cases staged against 72 S1's predicate reading the first line as the head over every producer file · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  61 (H7).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-94.

## 10. Reuse audit

The seam extended is 72 S1's predicate inside `check_commitment`, given the population and the line
skip `measure_commitment` already uses (`tools/runlog/record.py:1217-1230`), so the two readers of
one journal agree. The probe `python tools/codebase-map/reuse_lookup.py "first parseable line time of
a journal file"` ranked `read_journal`, `check_line` and `render_line` (`tools/runlog/runlog_lib.py`);
`rl.parse_line` is the parser S2 reuses.

Recall terms used: `python tools/memory-recall/query.py "what does runlog verify say for a pruned
journal" --terms "runlog verify commitment pruned retention empty producer file head parseable t
JOURNALS PRODUCER_FILES"`
