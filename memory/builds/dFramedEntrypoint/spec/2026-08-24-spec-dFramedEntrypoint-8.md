# TOOL-dFramedEntrypoint-8 — the superseding decision, and the three records that assert what is not true

**Status:** CLOSED · rev-5 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams tooling · ratified 2026-08-24

## 1. Goal

This build writes a prose template for build READMEs, and a ratified record in this tree says not to.
That refusal is reversible and the owner has reversed it, but a reversal that leaves no record is
indistinguishable from an oversight. This unit lands the superseding decision with the re-measurement
that makes the reversal true, and repairs three separate records that currently assert things the tree
contradicts — two of which sent this build's own research to the wrong conclusion.

## 2. Scope (IN)

- **S1** — a superseding row in `memory/DECISIONS.md` under the tooling section. It names the census
  conclusion and the non-goal it reverses, says the reversal is knowing and owner-approved, carries the
  re-measurement, and states the shape that answers the original objection: the template binds a
  declared population rather than redding a third of the corpus on landing.
- **S2** — the re-measurement itself, recorded with its command. The refusal rested on a ratio — a
  template that most of the corpus violates on day one is decorative — and that ratio has moved from 17
  of 25 to 20 of 61 while the corpus grew 2.4 times.
- **S3** — the map dossier for the build README surface is corrected in three places. Separately and
  NOT as part of the same claim, `gen_build_index.py`'s own comment above the plan-pair constants
  carries a stale RATIONALE rather than a stale rule: the rule it states is still correct, and only
  the reason given for it expired when the frozen authorization scope moved. It is corrected here
  because a true rule resting on a dead reason is how the next reader deletes the rule. It states that the
  authored roster pair is being retired and that its readers were removed; one reader is live and
  deliberate, and the spec it cites was itself corrected to admit that. It also states a carrier count
  that is wrong.
- **S4** — `memory/project/curation-debt.txt` is corrected. Its header justifies four of its seven rows
  with a precedent sentence that appears nowhere in the record it cites, and that record says the
  opposite: the READMEs in question were edited by the generator, and its acceptance criterion gates
  against the hand-edit alternative.
- **S4b** — `.memory-tree.conf`'s `READ_PATH_CEILING` is raised in the SAME commit as S1, or a member
  of the read path is trimmed by at least the row's width. `memory/DECISIONS.md` is one of six capped
  members and the margin measures in the low tens of bytes on the staged tree, while a row in that file
  measures 263 to 295. Without this the append cannot land green, and AC7 asserts it does. The raise
  follows the minimal-raise precedent the conf's own comments record, not the measure-plus-headroom
  jump the tool prints, and it carries its reason.
- **S5** — a backlog row for the fan-out guard's documentation defect: two files state that an array
  literal of five or fewer elements passes the guard unmarked, positioned directly under the bullet
  banning the raw primitive. The exemption applies only to the receiver of a spawn call, not to the
  primitive, and the raw primitive is refused regardless of its argument.
- **S6** — the CENSUS RECORD ITSELF IS NOT EDITED. A ratified record is superseded by a new id, never
  rewritten.

## 3. Non-goals (OUT)

- No repair of the seven curation-debt ROWS. Only the header's false justification is corrected; whether
  each row still earns its place is that row's own drain condition.
- No change to the authored roster pair, its reader, or the Definition-of-Done term it feeds. The
  dossier is corrected to describe what is there; changing what is there is this build's park.
- No fix for the fan-out guard's documentation. S5 records it; the repair belongs to whoever owns that
  kit's docs, and bundling it here would put a hooks change inside a memory-tree build.
- No new gate for any of this. Three of the four defects are prose asserting a fact about code, and the
  general remedy for that class is the drift audit, which already exists and already reports this
  family of signal.

## 4. Design

### Data model

None. This unit writes records.

### Migration

The decision row lands FIRST in the build order, because it is the authorisation for units 1 through 7
and a template landing ahead of its superseding decision is the silent reversal the unit exists to
prevent.

### Alternatives rejected

**Editing the census record to soften its conclusion.** Refused by this tree's append-only rule for
ratified records, and it would destroy the measurement that makes the reversal legible — the reversal
is only meaningful against the original ratio.

**Treating the dossier and registry errors as this build's incidental cleanup, uncatalogued.** Rejected
because both errors demonstrably propagate: the dossier told two independent research lenses that a live
reader had been removed, and the registry header's false citation is the stated reason for four waiver
rows.

### Files touched (estimate)

`memory/DECISIONS.md` · `.memory-tree.conf` for the S4b ceiling raise ·
`memory/map/features/build-readme-surface.md` · `memory/project/curation-debt.txt` ·
`memory/backlog/TOOL.md`.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A. No mechanism ships.
- observability — the decision row is the observability: it is what makes the reversal findable by the
  next session that reads the census and wonders why the template exists.
- risks — the read-path budget, and it is not hypothetical here: the margin is in the low tens of bytes
  on the staged tree and one decision row is an order of magnitude wider. S4b is the mitigation and it
  is in scope rather than noted. Only the DECISION APPEND is on that path — the dossier edit is not a
  member — so the raise is sized against one file's growth. The margin is read from the corpus tool,
  never from the ceiling alone.
- testing + left-shift gates — none new; the hygiene gate already grades the row grammar and the
  dossier claims.
- migration / rollback — records only, trivially revertible.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `memory/DECISIONS.md` is read at HEAD, it carries a row naming the census conclusion
  and the non-goal being reversed, the words that mark the reversal knowing, and the re-measurement.
- **AC2** — When the re-measurement is taken, the `git ls-files` command that produced both ratios is recorded beside
  them in this build's acceptance ledger.
- **AC3** — When `memory/map/features/build-readme-surface.md` is read at HEAD, no sentence claims the
  authored roster pair is retired or that its readers were removed, and its carrier count matches a
  `git grep -lF` over the tracked build READMEs.
- **AC4** — When `memory/project/curation-debt.txt` is read at HEAD, its header carries no claim about
  a precedent that a build's own folder owns its own prose.
- **AC5** — When `memory/backlog/TOOL.md` is read at HEAD, it carries a row describing the fan-out
  guard's documentation defect, naming both files that state it.
- **AC6** — When the census record is diffed against its state at this build's base, `git diff` reports it unchanged.
- **AC7** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs after the append and the S4b
  raise, it is green including the read-path check, and both the pre-append margin and the post-append
  margin are recorded with the command that produced them.
- **AC8** — When `python tools/drift-audit/drift_report.py` runs after this unit, its README mechanism
  signal is re-derived and its value recorded, because this unit changes the authored prose it scans.

## 7. Gates

`memory hygiene` · the codebase-map coverage and freshness legs, since a dossier claim moves · the
row-grammar merge driver over the backlog shard.

## 8. Open questions

- **F1 — does the decision row supersede one id or two?** The census conclusion and the generated-prose
  record's non-goal are separate statements in separate records, and both refuse a build-README prose
  template. Naming only one leaves the other standing. RESOLVED (agent, 2026-08-24, delegated): name both in
  one row. One decision reverses one policy however many records stated it.
- **F2 — is the drift audit's README mechanism pin re-baselined in this unit or after unit 7?** The
  signal scans exactly the authored region this build shrinks, so its value will move twice.
  RESOLVED (agent, 2026-08-24, delegated): record the value here and re-baseline after unit 7, so the pin
  is set against the corpus the contract produced rather than against an intermediate state.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft. All four defects were surfaced by this build's research fan and
  confirmed by its adversarial verification; the fan-out guard's documentation defect was observed
  directly when a bounded fan was refused for following the documented affordance.
- rev-2 · 2026-08-24 · folded spec-audit round 1. The read-path ceiling enters scope.
  `memory/DECISIONS.md` is a capped member with a margin in the low tens of bytes and a row in it is
  an order of magnitude wider, so the append this unit exists to make could not have landed green as
  specced.
- rev-3 · 2026-08-24 · folded the factual corrections from round 1's LOW tier. The read-path claim
  is narrowed to the decision append; the dossier is not a member of that path. The generator's
  stale plan-pair comment is named as a stale RATIONALE under a rule that still holds, rather than
  folded into the dossier's factual errors.
- rev-4 · 2026-08-24 · every open fork in section 8 resolved under the standing mandate's delegated resolver authority, by M3's rule: the most feature-rich survivor after the three vetoes. No option was taken that needed a new dependency, install location or public surface. The one question this build refuses is not a spec fork and is parked on the run-state file instead.
- rev-5 · 2026-08-24 · BUILT and CLOSED. Four records corrected, the superseding decision landed, the read-path ceiling raised minimally with its reason. Two things changed during the build: the decision row was rewritten from 482 to 274 characters to fit check 7's entry cap, and the curation-debt correction was reworded so AC4's own grep could tell a claim from its denial. Ledger: `build/2026-08-24-build-TOOL-dFramedEntrypoint-8-acceptance.md`.

## 10. Reuse audit

The existing seam is `memory/DECISIONS.md`'s own reversal precedent: two rows in that file already carry
the reverses-knowingly shape, each pairing the reversed id with the measurement that changed. This unit
copies that shape rather than inventing a supersession convention, which is the whole reuse finding —
the tree already knows how to reverse itself, and the failure mode being avoided is a reversal that
does not look like one.
