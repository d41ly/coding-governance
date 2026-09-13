# TOOL-aReplayedCard-4 — path-bearing manifest trap bullets become `memory/gotchas/` records

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-1 · base c4f02308 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-5 |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

The manifest's environment-traps section is 12973 of its 25595 bytes at base, measured with `awk`
over the section and `wc -c`, and every one of its bullets is global: a session reads all of them
whether or not it touches the file a bullet is about. The manifest itself says a recurring bug class
belongs in `memory/gotchas/`, where `gotchas.py --for-paths` puts it on the checklist for the areas a
unit touches. Move the bullets that carry a path anchor there, and re-stamp the manifest.

## 2. Scope (IN)

- **S1** Every bullet in the manifest's `### Environment traps` section whose body carries a token
  `gotchas.py`'s `ANCHOR_RE` recognises becomes one record under `memory/gotchas/`, in the
  catalogue's shape: front matter `name`, `description`, `kind: class`; sections `## Symptom`,
  `## Where it bit`, `## The fix`; a sentence that names its gate or says `no machine gate`. The
  population is DERIVED by the pass with that regex over the section at base and recorded in the
  acceptance ledger; the design record's reader counted 22 and this run's probe agreed, but the
  number is not pinned here. Observed by AC1 and AC2.
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
  entrypoint they asked for. Observed by AC5.

## 3. Non-goals (OUT)

- No change to the dated-corrections section.
- No new universal record; `UNIVERSAL_BUDGET` is 5 and the point of the eviction is path-keyed
  selection.
- No rewrite of a bullet's meaning; the fix and the symptom are moved, not re-litigated.
- No touch to any other unit's file; this unit runs alone at order 1 because it writes a backlog
  shard, a shared mutable record.

### Edges

- **hands-off** `KICK-aReplayedCard-3` — a lighter manifest for Step 2 to read once.
- **consumes-from** external — `gotchas.py`'s `ANCHOR_RE` and checks 17 to 19, which decide
  whether a record is reachable.

## 4. Design

One record per bullet, named by its kebab-cased subject, body in the catalogue's three sections,
the bullet's own path tokens preserved as the anchors. A record needs `git add` before
`gotchas.py --check` or the hygiene leg can see it.

### Files touched (estimate)

| Path | Change |
|---|---|
| `memory/gotchas/<one per bullet>.md` | new |
| `memory/gotchas/INDEX.md` | regenerated |
| `memory/guides/SESSION-KICKOFF.md` | bullets removed; stamps |
| `memory/map/features/*.md` | `gotcha-classes` claims |
| `memory/backlog/TOOL.md` | two rows closed |

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the manifest shrinks by roughly half; measured by `wc -c` before and after and
  recorded in the ledger.
- error / empty / loading states — N/A.
- observability — `gotchas.py --for-paths` output.
- risks — a record with inert anchors; check 19 is the arm.
- testing — the hygiene leg and `gotchas.py --check`.
- migration — none.
- user docs — the manifest's evicted-to-the-catalogue sentence.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-paths <the anchors of every new record>`
  runs at the landing commit, every new record is selected.
  Red when: a record's anchors reach nothing and it never appears on a checklist.
  figure: DERIVED — the record count is measured by the pass and written to the ledger.
- **AC2** — When `python tools/memory-tree/gotchas.py --check` runs, checks 17, 18 and 19 pass over
  the new records.
  Red when: a record names no gate, or its only anchors are append-only paths.
- **AC3** — When `bash skills/session-kickoff/manifest-check.sh` runs at the landing commit, the
  ratchet is green and `wc -c` of `memory/guides/SESSION-KICKOFF.md` is below the base figure by at
  least the bytes of the evicted bullets.
  Red when: the stamps did not move with the body.
- **AC4** — When the `codebase-map coverage + freshness` leg runs, every new record's key is
  claimed.
  Red when: a record lands unclaimed.
- **AC5** — When `memory/backlog/TOOL.md` is read, rows `TOOL-aWeighedCompass-14` and
  `TOOL-aWeighedCompass-15` read CLOSED with a note naming this unit.
  Red when: a row still reads OPEN over a fix the manifest carries.

## 7. Gates

`memory hygiene` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `drift-audit records`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is `tools/memory-tree/gotchas.py` — its `ANCHOR_RE`, its `--write` and its `--for-paths`
verb — and the manifest's own instruction that bug classes belong in the catalogue. The reuse probe
returned `SESSION-KICKOFF.md` as the seam; the record shape was read from
`memory/gotchas/two-answers-to-one-question.md`.

Recall terms used: `manifest traps environment gotchas catalogue anchor for-paths eviction INDEX universal budget check 19 kickoff manifest byte cap`
