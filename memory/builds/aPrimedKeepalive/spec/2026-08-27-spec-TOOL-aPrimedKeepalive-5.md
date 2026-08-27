# TOOL-aPrimedKeepalive-5 — `dCarriedReceipt`'s record gains the `landed-anchor` its own verb failed to write

**Status:** OPEN · rev-1 · 2026-08-27 · node a · Tier-1 · base b4e1d5be · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md) | journal | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 |
| [2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md](../prompts/2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md) | research | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/builds/dCarriedReceipt/RUN.md` says `phase: LANDED` and carries no `landed-anchor`, so
hygiene's sibling leg check 15 has been red at `main` since 2026-08-25. No verb can repair it —
`--landed` already wrote the terminal phase before it refused, and check 26 then refuses every other
verb on a finished record. Hand-complete the missing fact, on evidence verified independently.

## 2. Scope (IN)

- **S1** — `memory/builds/dCarriedReceipt/RUN.md` gains `landed-anchor: remote`, in the exact fact
  grammar `set_fact` writes and in the position its siblings occupy.
- **S2** — the claim is VERIFIED before it is written, not assumed: the record's witness must be an
  ancestor of the tip `origin` advertises for its default branch, shown by `git merge-base
  --is-ancestor`, and the command and its result are recorded in the unit's journal.
- **S3** — `unpushed-at-landing` is written only if the record lacks it AND the value can be
  measured; if it cannot, it is left absent rather than defaulted, because a zero meaning "could not
  measure" is this repo's named green-by-absence class.
- **S4** — the backlog row this discharges, `TOOL-dScaffoldedMirror-22`, is updated with this third
  instance, since the row's own text is the evidence that the trap fires on every no-ff landing.

## 3. Non-goals (OUT)

- Fixing the defect that caused it. `TOOL-dScaffoldedMirror-22` states the fix — compute and
  validate, then write both facts together, so a refusal leaves the record untouched — and it is a
  change to `verb_landed`'s ordering that this build does not take on. The row stays OPEN.
- Any other field of that record. Its phase, witness, keepalive id and parked entries are exactly as
  its own run left them.
- Any other record in the tree. `dTieredTribunal` is `TOOL-aPrimedKeepalive-4`'s subject and is
  NOT hand-edited: that one is repaired by changing what the leg concludes, not by writing a fact.

## 4. Design

### Why a hand-completion is the right act here, and only here

The kit's own rule is that a run's facts are written by verbs, never by hand. This record is the
documented exception the backlog row already names: the verb wrote `phase: LANDED` at `:1890` and
then refused at check 34 before reaching the `set_fact` for the anchor, and check 26 refuses `--park`
and `--phase` on a finished record. So no verb can reach it, by construction. The row records the
same remedy applied twice already, on `dScaffoldedMirror` and `dPromptedSeam`, both times with the
ancestry verified from git rather than assumed.

`remote` is the correct value and not the convenient one. The alternative, `local`, asserts the work
reached the local default branch and not the remote; the witness `04c7da24` is an ancestor of
`origin/main`, which is the strictly stronger claim and the one the record's own run was making.

### Files touched (estimate)

`memory/builds/dCarriedReceipt/RUN.md` — one line. `memory/backlog/TOOL.md` — one row's text.

### Alternatives rejected

**Leave it and override `gates-green` at close.** The bar is the merge bar; an override on a red leg
whose cause is a one-line true fact is spending the bar's credibility to avoid a one-line edit.

**Fix `verb_landed`'s ordering in this build.** That is the real fix and it is a Tier-2 unit in the
driver's landing path. Out of scope by §3; the row stays open and says so.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the journal record carries the verification command and its output, so a later
  reader can re-run it.
- risks — writing a false terminal fact. S2's independent verification is the whole mitigation, and
  the value written is the one git confirms rather than the one that clears the check fastest.
- testing + left-shift gates — check 15 is the gate and it currently reds; green after is the
  observation. The left-shift for the CLASS is `TOOL-dScaffoldedMirror-22`, which stays open.
- migration / rollback — one line; revert is the rollback.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `git merge-base --is-ancestor 04c7da244361950b38a611671d341ac3400e32cb origin/main`
  runs, it exits 0, and that command and result are in the unit's journal record.
- **AC2** — When `memory/builds/dCarriedReceipt/RUN.md` is read, it carries `landed-anchor: remote`
  in the same fact grammar as its neighbours.
- **AC3** — When `bash tools/unattended/check-unattended.sh` runs, check 15 no longer names
  `memory/builds/dCarriedReceipt/RUN.md`.
- **AC4** — When `memory/backlog/TOOL.md` is read, `TOOL-dScaffoldedMirror-22` records this as the
  third instance and remains `OPEN`.

## 7. Gates

`unattended kit gate` · `memory tree hygiene`, and `bash tools/run-gates/run-gates.sh` at the push
boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft. Adopted into this build by owner ruling on 2026-08-27.

## 10. Reuse audit

No mechanism is built, so there is no seam to extend — the reuse is of a RECORDED REMEDY rather than
of code. `memory/backlog/TOOL.md`'s `TOOL-dScaffoldedMirror-22` states the act, the value, and the
verification, and names the two prior applications on `dScaffoldedMirror` and `dPromptedSeam`. This
unit follows it rather than inventing a third way to repair the same record shape.

Recall terms used: `landed-anchor absent record repair verb refused check 15 cutoff witness ancestor
hand-completed unrepairable finished`. The query returned `TOOL-dScaffoldedMirror-22` and
`TOOL-dUnstalledConvoy-38`, which together explain both why the record is broken and why no verb can
reach it.
