# TOOL-dUnstuckLanding-25 — restore the two dMendedRecall units a merge resolution dropped

**Status:** INPROGRESS · rev-1 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The merge `01c22e15` ("origin/main (dMendedRecall) into the aRepatriatedFork run branch") resolved
its conflicts in `tools/unattended/unattended.sh` and `tools/unattended/VERBS.template.md` to the run
branch's side. That dropped two shipped units:

- **`TOOL-dMendedRecall-2`'s `write_ask_views`:** 108 of its 129 added lines are absent at HEAD.
- **`TOOL-dMendedRecall-3`'s `--status` verb entry:** all 29 of its lines are absent.

Both records read CLOSED, and their code is gone from `origin/main`. Their arms in
`unattended.test.sh` fail at HEAD, and this build's close runs that suite (ruling
`TOOL-dUnstuckLanding-24`). Restore both, adapted to the code units 13 to 16 have since changed.
Adopted under protocol section 11. Found by unit 16's builder, and measured by the orchestrator: a
re-run `git merge-tree` of the two parents shows the conflict, and the committed resolution drops the
lines.

## 2. Scope (IN)

- **S1** — `write_ask_views` and its header comment come back into `tools/unattended/unattended.sh`,
  taken from its last landed form, `ef1dcdb6:tools/unattended/unattended.sh:6812-6990` and the call at
  `:7117`. Restore it with the same name, the same contract and the same call site in
  `write_inherited_asks`, and reconcile it with unit 16's changes to `write_inherited_asks` and
  `read_ask_back` (SEV-aware reuse, BLOCKER filing). Any numbered `fail` branch it carried returns
  with the same number when that number is free, and otherwise takes the next free one, armed.
  Observed by AC1, AC2.
- **S2** — The `--status` entry of `tools/unattended/VERBS.template.md` regains the field-by-field
  account `TOOL-dMendedRecall-3` gave it, from `ef1dcdb6:tools/unattended/VERBS.template.md`. It is
  extended by the fields units 13 to 16 added to `verb_status`'s line since, such as the derived
  `LANDED (attended)` phase, so that the entry describes the line HEAD actually prints. The render is
  re-copied. Observed by AC3, AC4.
- **S3** — The rest of the merge is audited: every line `01c22e15^2` added over the merge-base, in
  every file the merge touched, is either present at HEAD, superseded with its successor named, or
  restored. The result is written into this unit's acceptance ledger. Observed by AC5.

## 3. Non-goals (OUT)

- **A gate that catches a merge dropping one side's hunks.** That is a separate mechanism, filed as
  an ask in this build's `BACKLOG.md`.
- **The two dMendedRecall records.** They stay CLOSED, because their units were built and landed. A
  later merge reverted the code, and this unit restores it.

### Edges

- **consumes-from** external — `write_inherited_asks` and `read_ask_back` as the CLOSED unit
  `TOOL-dUnstuckLanding-16` committed them. The restored call site must sit inside that version.

## 4. Design

Restore from the last landed blob, then reconcile it by hand against HEAD. Do not cherry-pick
`9cba3c3f`: three later dMendedRecall revisions (rev-3 to rev-5) and units 13 to 16 sit between that
commit and HEAD.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

## 5. Production-readiness checklist

- security — N/A: this restores code that was reviewed and landed, and it adds no new write path.
  The function stages only its own render delta, as it did before.
- perf / scale — one generator render for each close that files an ask, as before.
- error / empty / loading states — the named-miss lines of the original carry over.
- observability — the original's miss lines carry over.
- risks — the restored code may disagree with unit 16's SEV-aware filing. AC2's probe is what shows
  it does not.
- testing — the existing dMendedRecall-2 arms; no new arm.
- migration — none.
- user docs — the VERBS `--status` entry.

## 6. Acceptance criteria

- **AC1** — When `grep -c write_ask_views tools/unattended/unattended.sh` runs, it prints at least 3:
  the header comment, the definition and the call. Red when: it prints 0, the state at HEAD.
- **AC2** — When a hermetic probe copies the driver suite's prologue and its `TOOL-dMendedRecall-2`
  arms (the AC9 "generated views were not re-rendered" pair and the F4 `f4-views-double: 1 filed`
  pair) into the scratchpad and runs them against a fixture repository, all four pass.
  Red when: any of them fails, as all four do at HEAD.
- **AC3** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it reports the render of
  `VERBS.template.md` in sync. Red when: the render differs from its template.
- **AC4** — When the `--status` entry of `VERBS.template.md` is compared field by field with the
  `printf` and suffix strings `verb_status` appends at HEAD, every field is named in the order printed.
  Red when: a field `verb_status` prints is unnamed, the defect `TOOL-dMendedRecall-3` closed.
- **AC5** — When this unit's acceptance ledger is read, it lists `01c22e15`'s other conflicted files
  with a disposition for each: present, superseded (successor named) or restored.
  Red when: a file `git merge-tree` reports as conflicted has no disposition.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `kit version markers` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

New arm: none. The `TOOL-dMendedRecall-2` arms already exist in `tools/unattended/unattended.test.sh`, and this unit makes them pass again.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; adopted under protocol section 11 from unit 16's finding.

## 10. Reuse audit

No existing seam fits beyond the function this unit restores. `python tools/codebase-map/reuse_lookup.py
"re-render and stage generated views after filing ask rows"` returns only Python name-stem matches,
such as `render_family_view` in `tools/memory-tree/backlog.py`, and the map leaves the `.sh` layer
unscanned. None of them renders the views from the shell close. The seam is `write_ask_views` itself, at its last landed blob
`ef1dcdb6:tools/unattended/unattended.sh`. The recall probe returns `TOOL-dMendedRecall-2` and
`TOOL-dAlignedCarrier-9` as the binding records.

Recall terms used: write_ask_views inherited red ask views stale render stage close records commit refusal 69
