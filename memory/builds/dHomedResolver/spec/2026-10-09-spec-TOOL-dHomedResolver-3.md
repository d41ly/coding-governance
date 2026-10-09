# TOOL-dHomedResolver-3 — two gotcha records for the classes units 1 and 2 close

**Status:** SPECCED · rev-1 · 2026-10-09 · node d · Tier-1 · base 5a836bf0 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-prompt-TOOL-dHomedResolver-1-0-run-mandate.md](../prompts/2026-10-09-prompt-TOOL-dHomedResolver-1-0-run-mandate.md) | journal | TOOL-dHomedResolver-1 TOOL-dHomedResolver-2 |

<!-- /gen:spec-records -->

## 1. Goal

Units 1 and 2 gate two instances. The classes behind them recur wherever a checker resolves by name
or derives from git's index, and the catalogue holds neither, so a reviewer of the next such checker
is handed no question to ask. Write one record per class.

## 2. Scope (IN)

- **S1** — `memory/gotchas/name-search-resolves-a-namesake.md`: a resolver that searches by name,
  where the location is declared, admits every file sharing the name, and its finding blames the
  subject for a collision it did not cause. Observed by AC1.
- **S2** — `memory/gotchas/index-derivation-reads-a-half-staged-move-as-a-deletion.md`: a
  derivation over `git ls-files` reads a move whose destination is unstaged as a deletion, and a
  writer then renders that deletion into every file citing what moved. Observed by AC1.
- **S3** — Each record anchors on the paths its instance lives in, so `gotchas.py --for-paths`
  selects it for a change there, and `memory/gotchas/INDEX.md` is re-rendered. Observed by AC2.

## 3. Non-goals (OUT)

- Any gate: units 1 and 2 carry the arms. These records are the reviewer's question for the next
  instance, which no arm here can reach.

### Edges

- **consumes-from** `TOOL-dHomedResolver-1` — the instance and the fix the first record cites.
- **consumes-from** `TOOL-dHomedResolver-2` — the instance and the fix the second record cites.

## 4. Design

### Files touched (estimate)

- `memory/gotchas/name-search-resolves-a-namesake.md`
- `memory/gotchas/index-derivation-reads-a-half-staged-move-as-a-deletion.md`
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- **One record for both.** Rejected: one is about WHERE a reader looks and the other about WHEN its
  population is complete. A reviewer asks different questions of each.
- **Extend `vacuous-selector-empty-population`.** Rejected: that class prints nothing; both of these
  print a confident, wrong finding or a confident, wrong render.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --check` runs, both new records parse and the
  catalogue is clean.
  Red when: a record's front matter or section shape is refused.
- **AC2** — When `python tools/memory-tree/gotchas.py --for-paths tools/memory-tree/gen_build_index.py tools/memory-tree/check-memory-hygiene.sh`
  runs, it lists both new classes.
  Red when: a record carries no anchor that selects its instance's file.

## 7. Gates

`gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The seam is the catalogue's own record shape: front matter, Symptom, Where it bit, The fix, What
this does NOT say, as `join-key-widened-by-a-shared-location.md` carries them. A search of the 104
records for the classes found neither: `vacuous-selector-empty-population` and
`two-answers-to-one-question` are the nearest, and both describe a different failure.

Recall terms used: check 10 rotation note live index basename archive stem backlog shard resolves preamble TOOL-cTracedPromise-6 TOOL-cSpliceWarden-2
