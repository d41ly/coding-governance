# Acceptance ledger — TOOL-dHomedResolver-1

**Serves:** journal TOOL-dHomedResolver-1

Built on `ada7047d`. Every new arm was run against a `git archive` of base `5a836bf0` first, in the
session scratchpad, through a probe holding the suite's `cblock` helper and the arm block verbatim.
At base the two namesake arms and the home-naming arm failed with the message inCMS core saw,
`stem 'DECISIONS' resolves to 2 live index(es)`, and the positive control passed. On this code all
four pass. The Python namesake arm failed at base with `resolves to 2 live index(es), so the
exclusivity half was NOT graded` and passes here. The cross-reader arm was mutation-checked: with
the Python home alone changed to `memory/<stem>.md` it printed `DISAGREE on the home of ARCH`.

Before wiring, the candidate predicate ran read-only over gov, inCMS core at `incms/main` and nc:
every tracked rotated archive resolves to the same file under both rules, and no innocent file reds.
Core at `ca8b51512^` held two build-folder `DECISIONS.md` ledgers beside its root index.

**Evidences:** TOOL-dHomedResolver-1
- AC1 — `check-memory-hygiene.sh` — over the `homed` fixture check 10 names nothing for the DECISIONS archive beside a build-folder `DECISIONS.md`; red at 5a836bf0
- AC2 — `BACKLOG_MODE` — under the default `shards`, the same fixture's ARCH archive beside a build-folder `ARCH.md` is not named; red at 5a836bf0
- AC3 — `check-memory-hygiene.sh` — the DEPL archive is named with `declares its live index at memory/backlog/DEPL.md, which is not tracked`
- AC4 — `check-memory-hygiene.sh` — the `rotarchive` block's seven assertions and the `bmode` block's 26, deferral count included, pass on this code
- AC5 — `row_grammar.py --selftest` — the namesake arm prints `does not partition the family: ARCH-tBoth-2`; red at 5a836bf0
- AC6 — `row_grammar.py --selftest` — the cross-reader arm prints `JOIN-OK` with both readers' homes for DECISIONS and every declared family
- AC7 — `git grep -n 'by BASENAME'` — prints nothing over the HYGIENE catalogue, its kit template and the hygiene dossier
