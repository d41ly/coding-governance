# TOOL-aReplayedCard-4 — path-bearing manifest trap bullets become `memory/gotchas/` records

**Status:** CLOSED · rev-3 · 2026-09-14 · node a · Tier-1 · base c4f02308 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-5 |
| [2026-09-14-build-TOOL-aReplayedCard-4-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aReplayedCard-4-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-5 |
| [2026-09-14-prompt-TOOL-aReplayedCard-4-brief.md](../prompts/2026-09-14-prompt-TOOL-aReplayedCard-4-brief.md) | journal | — |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md) | diff-review | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

The manifest's environment-traps section is 12973 of its 25595 bytes at base, measured with `awk`
over the section and `wc -c`, and every one of its bullets is global: a session reads all of them
whether or not it touches the file a bullet is about. The manifest itself says a recurring bug class
belongs in `memory/gotchas/`, where `gotchas.py --for-paths` puts it on the checklist for the areas a
unit touches. Move the bullets that carry a path anchor there, and re-stamp the manifest.

## 2. Scope (IN)

- **S1** Every bullet in the manifest's `### Environment traps` section whose body carries a token
  `gotchas.py`'s `ANCHOR_RE` recognises lands in a record under `memory/gotchas/`, in the
  catalogue's shape: front matter `name`, `description`, `kind: class`; sections `## Symptom`,
  `## Where it bit`, `## The fix`; a sentence that names its gate or says `no machine gate`. The
  catalogue's own rule is ONE RECORD PER CLASS, so the join is by class and not by bullet: two
  bullets of one class share a record; a bullet whose class an existing record already carries is
  FOLDED into that record as a new section, its anchors added to the record's; a bullet whose fact
  an existing record already states is deleted with no record written. The ledger maps every bullet
  to the record it landed in. The population is DERIVED by the pass with that regex over the section
  at base and recorded in the acceptance ledger; the design record's reader counted 22 and this
  run's probe agreed, but the number is not pinned here. Observed by AC1 and AC2.
- **S2** A bullet whose anchors resolve to no tracked path is rewritten to name the tracked file it
  is about, so the record is reachable; a bullet that is genuinely about no file stays in the
  manifest and the ledger says which and why. Observed by AC2.
- **S3** The evicted bullets are deleted from the manifest; the section keeps its heading and its
  "evicted to the catalogue" sentence, which gains the new names. `last-audit` and
  `last-body-change` are re-stamped with the delta line in the commit message. Observed by AC3.
- **S4** `python tools/memory-tree/gotchas.py --write` re-renders `INDEX.md`, and each new record is
  claimed under a dossier's `gotcha-classes` key, in the same commit, after `git add`, because the
  coverage inventory reads tracked files. Observed by AC4.
- **S5** Backlog rows `TOOL-aWeighedCompass-14` and `TOOL-aWeighedCompass-15` flip to CLOSED in
  place with the closing note, because the manifest already names the recall kit and the tooling
  entrypoint they asked for. NOT THIS PASS'S WRITE: `memory/backlog` is a `SHARED_RECORDS` member
  in `.unattended.conf`, and `unattended.sh --dispatch` refuses any pass declaration overlapping
  one, so the flip is the orchestrator's, in a records commit of its own after this unit lands,
  the way `TOOL-aLeakedHandle-5` was closed. AC5 is AMENDED to say so.

## 3. Non-goals (OUT)

- No change to the dated-corrections section.
- No new universal record; `UNIVERSAL_BUDGET` is 5 and the point of the eviction is path-keyed
  selection.
- No rewrite of a bullet's meaning; the fix and the symptom are moved, not re-litigated.
- No touch to any other unit's file; this unit runs alone at order 1 because it rewrites the
  manifest every later unit reads, and its declared write set carries no shared mutable record.

### Edges

- **hands-off** `KICK-aReplayedCard-3` — a lighter manifest for Step 2 to read once.
- **consumes-from** external — `gotchas.py`'s `ANCHOR_RE` and checks 17 to 19, which decide
  whether a record is reachable.

## 4. Design

One record per CLASS, named by its kebab-cased subject, body in the catalogue's three sections,
the bullet's own path tokens preserved as the anchors and the tracked file the trap is about added
where the bullet's own tokens reach nothing. Resolution is `gotchas.py`'s `selectable` — substring
either way or basename equality — because that is the predicate check 19 and `--for-paths` apply;
a stricter exact-path reading counts fewer and the ledger records both figures. A bullet whose
subject is the one path `selectable` excludes by construction (`memory/gotchas/` itself), or whose
trigger is a path NO anchor can express (a file outside the tree's tool root), stays in the manifest
under S2. A record needs `git add` before `gotchas.py --check` or the hygiene leg can see it.

### Files touched (estimate)

| Path | Change |
|---|---|
| `memory/gotchas/<one per class>.md` | new |
| `memory/gotchas/<existing>.md` | a section folded in, where the class already has a record |
| `memory/gotchas/INDEX.md` | regenerated |
| `memory/guides/SESSION-KICKOFF.md` | bullets removed; stamps |
| `memory/map/features/*.md` | `gotcha-classes` claims |
| `memory/map/generated/*` | re-rendered from the claims |

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the manifest shrinks by the evicted bullets' bytes net of the names the evicted
  sentence gains; measured by `wc -c` before and after and recorded in the ledger.
- error / empty / loading states — N/A.
- observability — `gotchas.py --for-paths` output.
- risks — a record with inert anchors; check 19 is the arm.
- testing — the hygiene leg and `gotchas.py --check`.
- migration — none.
- user docs — the manifest's evicted-to-the-catalogue sentence.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-paths <the anchors of every record a
  bullet landed in>` runs at the landing commit, every such record — new, or existing and extended —
  is selected.
  Red when: a record's anchors reach nothing and it never appears on a checklist.
  figure: DERIVED — the record count is measured by the pass and written to the ledger.
- **AC2** — When `python tools/memory-tree/gotchas.py --check` runs, checks 17, 18 and 19 pass over
  the new records.
  Red when: a record names no gate, or its only anchors are append-only paths.
- **AC3** — When `bash skills/session-kickoff/manifest-check.sh` runs at the landing commit, the
  ratchet is green and `wc -c` of `memory/guides/SESSION-KICKOFF.md` is below the base figure by
  the bytes of the evicted bullets LESS the bytes the evicted-to-the-catalogue sentence gained
  naming them, both figures in the ledger. AMENDED at rev-2: rev-1 said "at least the bytes of the
  evicted bullets", which S3's own "gains the new names" clause makes unreachable by construction.
  Red when: the stamps did not move with the body.
- **AC4** — When the `codebase-map coverage + freshness` leg runs, every new record's key is
  claimed.
  Red when: a record lands unclaimed.
- **AC5** — When `memory/backlog/TOOL.md` is read after the orchestrator's records commit, rows
  `TOOL-aWeighedCompass-14` and `TOOL-aWeighedCompass-15` read CLOSED with a note naming this unit.
  Red when: a row still reads OPEN over a fix the manifest carries. AMENDED at rev-2: the flip is
  outside this pass's declarable write set (S5), so this unit's ledger carries the AMENDED form and
  the observation belongs to the commit that makes it.

## 7. Gates

`memory hygiene` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `drift-audit records`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-14 · S1 · S2 · S5 · §3 · §4 · AC1 · AC3 · AC5 · the join is by CLASS, not by
  bullet: the catalogue's own rule is one record per class, and building found four bullets whose
  class an existing record carries (folded into three records), three pairs of one class (one record
  each), one bullet the catalogue already states (deleted), two with no reachable anchor (kept in the
  manifest, S2). The backlog flip leaves this pass: `--dispatch` refuses a declaration overlapping
  `memory/backlog` (`SHARED_RECORDS`), so S5 is the orchestrator's and AC5 is AMENDED. AC3's byte
  bound is net of the sentence S3 grows. Resolution named as `selectable`, with the two figures the
  ledger carries. Built and CLOSED by the pass that made these changes.
- rev-3 · 2026-09-14 · §5 · the perf row said "roughly half", a figure that belonged to evicting the
  whole section and not to the anchored subset; rewritten to the AC3 measurement. Found by the
  post-commit bug-class checklist (`amendment-leaves-its-other-half-standing`), records only.

## 10. Reuse audit

The seam is `tools/memory-tree/gotchas.py` — its `ANCHOR_RE`, its `--write` and its `--for-paths`
verb — and the manifest's own instruction that bug classes belong in the catalogue. The reuse probe
returned `SESSION-KICKOFF.md` as the seam; the record shape was read from
`memory/gotchas/two-answers-to-one-question.md`.

Recall terms used: `manifest traps environment gotchas catalogue anchor for-paths eviction INDEX universal budget check 19 kickoff manifest byte cap`
