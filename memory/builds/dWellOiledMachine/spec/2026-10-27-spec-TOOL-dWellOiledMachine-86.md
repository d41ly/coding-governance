# TOOL-dWellOiledMachine-86 — runlog verify reads an emptied or absent producer file as consistent with `pruned`

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 4 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-86-deviation-861.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-86-deviation-861.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-90 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`),
finding 41, item H7, at HIGH; item H7 also carries finding 61, which TOOL-dWellOiledMachine-88 closes.
TOOL-dWellOiledMachine-72 S1 returns `pruned` only when every producer file begins with a line newer
than the run's start, and its §5 grades an empty producer file `mismatch`, never `pruned`. Retention
(TOOL-dWellOiledMachine-16 S5) keeps only the lines at or after its cutoff, through `os.replace`, so a
producer idle longer than the window is left present and EMPTY. On a node where `pushes.log` (say)
went idle past the window, every committed record older than the window verifies `mismatch` and exits
1: the false tamper verdict 72 exists to remove. This unit reads an empty or absent producer file as
consistent with `pruned`.

## 2. Scope (IN)

- **S1** — An empty or absent file is consistent with `pruned`. In 72 S1's predicate, a producer file
  that is absent, or present with no line, imposes no condition: it is what retention leaves of a
  producer whose every line was older than the cutoff. Every file that holds a line must still
  satisfy 72 S1's head test, so an emptied file never masks an edit in another. A journal whose every
  producer file is empty reads `pruned`: retention emptied all of them. Observed by AC1, AC2.
- **S2** — The why names the empty files. The `pruned` line's `<why>` gains
  `; <producer> empty` for each empty or absent producer file it passed over, so the verdict shows
  which producers retention emptied. Observed by AC1.
- **S3** — 72's §5 line corrected. The error-state line of spec 72's §5, "an empty producer file …
  is `mismatch`, never `pruned`", is replaced at this unit's pass by S1's reading, its §9 line naming
  this unit and finding 41. Observed by AC3.

## 3. Non-goals (OUT)

- Which producer files the predicate reads, and which line is a file's head, are finding 61's,
  closed by TOOL-dWellOiledMachine-88.
- No change to the prune: 16 S5 stands.
- A journal with no producer file at all keeps `check_commitment`'s existing refusal
  (`tools/runlog/record.py:1296-1299`).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-72` — S1's `pruned` predicate and its §5 empty-file reading, which this unit corrects
- **hands-off** `TOOL-dWellOiledMachine-90` — the empty-file reading, combined with unit 88's head in one case (finding 20)
- **hands-off** `TOOL-dWellOiledMachine-94` — §5's security line, which reads an unparseable line as deleted (finding 16)

## 4. Design

### Evidence

- 72 §5 reads "an empty producer file reads as having no head, which is `mismatch`, never `pruned`"
  (`spec-72.md:86-87`).
- 16 S5 applies the cutoff to each `PRODUCER_FILES` file and keeps the lines at or after it
  (`spec-16.md:63-70`), so an idle producer's file stays present and empty.
- `check_commitment` refuses only when no producer file of `mdl.JOURNALS` exists at all
  (`tools/runlog/record.py:1296-1299`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `idle-producer`, `all-empty` | `tools/runlog/selftest.py` cases | none |

### Files touched (estimate)

- `tools/runlog/record.py`: S1, S2
- `tools/runlog/selftest.py`: the two cases
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-72.md` (S3's rev bump)

### Alternatives rejected

- **Keeping a sentinel line in every pruned file.** It changes 16 S5's retention output for every
  reader of the journal to answer one verifier's question.

## 5. Production-readiness checklist

- security — an edit among remaining lines stays `mismatch`; an emptied file is the case 72 S3
  already states `verify` cannot tell from a deletion.
- perf / scale — one size check per producer file on a differing commitment.
- error / empty / loading states — S1 is the empty state.
- observability — S2 names each emptied producer.
- risks — a deleted producer file reads as retention; 72 S3's stated limit covers it.
- testing — AC1 to AC3 and the arm in §7.
- migration — none.
- user docs — none beyond 72's README section, which states the limit.

## 6. Acceptance criteria

- **AC1** — When the `idle-producer` fixture case, on its §7 `New arm:` line, renders a run record over a
  journal with `driver.log` and `pushes.log` lines, then cuts `pushes.log` to empty and `driver.log`
  to lines newer than the run's start, `runlog.py verify <record>` prints `pruned —` ending
  `pushes empty` and exits 0.
  Red when: the emptied file makes the record verify `mismatch`.
- **AC2** — When the `all-empty` case cuts every producer file to empty, `verify` prints `pruned` and
  exits 0; when the `idle-producer` case instead keeps `driver.log` whole, holding the run's lines,
  and edits one byte of a hashed line, `verify` prints `mismatch` and exits 1.
  Red when: an emptied file masks an edit in another producer, or a fully pruned journal reads
  `mismatch`.
- **AC3** — When `grep -n "never .pruned." 2026-10-27-spec-TOOL-dWellOiledMachine-72.md` runs over
  spec 72 after this unit, it prints nothing, and its §9 names this unit.
  Red when: §5 still grades an empty file `mismatch`.

## 7. Gates

`runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/runlog/selftest.py · covers AC1 AC2 · the idle-producer case staged against 72 S1's predicate grading an empty file `mismatch` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  41 (H7).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-94.

## 10. Reuse audit

The seam extended is 72 S1's `pruned` predicate inside `check_commitment`
(`tools/runlog/record.py:1260-1307`), the one verifier of a commitment. The probe `python
tools/codebase-map/reuse_lookup.py "verify a journal commitment after retention emptied a producer
file"` ranked `build_commit`, `read_journal`, `resolve_journal_root` and `Journal`; `read_journal`
reads lines and none judges an empty file, so the predicate is extended in place.

Recall terms used: `python tools/memory-recall/query.py "what does runlog verify say for a pruned
journal" --terms "runlog verify commitment pruned retention empty producer file head parseable t
JOURNALS PRODUCER_FILES"`
