# TOOL-aScouredKit-14 — three prose defects in the load-bearing documents

**Status:** CLOSED · rev-1 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams playbook

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-15 |
| [2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md) | spec-audit | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-15 TOOL-aScouredKit-30 TOOL-aScouredKit-31 TOOL-aScouredKit-32 |

<!-- /gen:spec-records -->

## 1. Goal

Take the only prose cuts the wave-2 audit could justify — two, both provably rule-preserving — and
fix the one count in the corpus that the charter explicitly delegates to a single carrier and that
now contradicts its own breakdown.

## 2. Scope (IN)

- S1. `AGENTS.md` Conventions — the third statement of the unattended-authorization rule collapses
  to its first clause plus the pointer. Both surviving carriers are in the SAME file and are named
  in §4.
- S2. `AGENTS.md` merge-bar section — the cold/warm timing pair, which the sentence after it
  certifies as describing a bar that no longer exists, is deleted.
- S3. `tools/memory-tree/README.md` — the check-count cell's parenthetical is corrected to the
  derived split, and the stale "21-check" phrase in the same file's opening is removed rather than
  re-numbered.

## 3. Non-goals (OUT)

- Every other cut the prose lens considered and declined. Its refusals are recorded in its own
  writeup with reasons, and re-litigating them here would lose the reasons.
- `memory/HYGIENE.md`'s catalog stopping at check 22. That needs a new catalog item in two
  byte-compared files and is a unit, not a fold; it is reported as a backlog row.
- Declaring ceilings for `WIRE-INTO-PROJECT.md` and the rendered unattended Skill. A row alone is
  inert without a matching leg, so that is its own unit and is backlogged with the measurement.
- Any reflow, tightening or merge whose justification is style.

## 4. Design

S1 and S2 are the only two cuts that survived a default-refute skeptic, and both clear the bar the
lens set for itself: name the rule the removed bytes carried, and name where it still lives.

For S1 the rule survives twice in `AGENTS.md` itself — in the §1 Landing bullet and in the merge-bar
section's unattended paragraph. The copy being cut is measurably the LEAST precise of the three: the
surviving §1 copy carries "must be reachable from a BASE observed on the remote rather than read
from a local ref", and the surviving merge-bar copy carries "OBSERVED from the remote's own HEAD
advertisement, never read from a local ref and never named by the environment" — a property the cut
copy did not state. The charter's own §1 unattended block forbids exactly this shape.

For S2 the figures survive in `memory/builds/aShardedFloor/README.md` and in
`TOOL-aScannedThrottle-8`, and the live pointer to `<git-dir>/gate-ledger.tsv` two lines above the
cut survives it.

S3 is not a cut. Charter §5 delegates the hygiene check count to the kit README and says it is
"deliberately not restated" there, so that cell is the ONLY carrier — and it said "23 checks" while
enumerating 22, with the same file's opening paragraph still saying "21-check". The derived split
was taken from the `fail <n>` sites in `check-memory-hygiene.sh`: the shell owns 1-12, 21, 22 and
23; 13-16 go to `corpus_ids.py`, 17-19 to `gotchas.py`, 20 to `row_grammar.py`. The opening phrase
loses its number rather than gaining a corrected one, because a count typed beside a population it
does not derive is the class this repo names and it has now been wrong twice in one file.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — N/A.
- observability — the recovered `AGENTS.md` margin is measurable by the size gate.
- risks — a prose cut that loses a rule is a regression no gate catches. Mitigated structurally: each
  cut names its surviving carrier and both are in the same file, so the survival is checkable by
  grep rather than by belief.
- testing + left-shift gates — `bash tools/check-template-size.sh AGENTS.md` ·
  `bash tools/check-wiring.sh` · `bash tools/check-playbook-parity.sh`.
- migration / rollback — N/A.
- user docs — the README cell IS the user doc, and S3 is its correction.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-template-size.sh AGENTS.md` runs, it reports at least 400 bytes
  of headroom, against the 41 measured at the base sha.
- **AC2** — When `grep -c "observed on the remote"` and `grep -c "HEAD advertisement"` run over
  `AGENTS.md`, each returns at least 1 — the rule S1 cut still stands in both named carriers.
- **AC3** — When `tools/memory-tree/README.md` is read, its check-count cell enumerates every
  bucket the shell's `fail <n>` sites hold, and no line in that file states a different total.
- **AC4** — When `bash tools/run-gates/run-gates.sh` runs, it is green.

## 7. Gates

`charter size` · `playbook parity` · `kit/dogfood doc parity` · `memory hygiene` · the full bar at
the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

No code seam: this unit edits three prose sites. The reuse question it does answer is which document
OWNS each fact, which is what makes the cuts safe — the two `AGENTS.md` carriers named in §4 and the
`fail <n>` sites in `tools/memory-tree/check-memory-hygiene.sh` for the count. The build's reuse
probe is recorded in `TOOL-aScouredKit-1` §10 and is not re-composed.
