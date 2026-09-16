# TOOL-dLoggedFlight-20 — the committed record carries no time a journal or transcript produced

**Status:** SPECCED · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-review-TOOL-dLoggedFlight-20-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-20-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 |

<!-- /gen:spec-records -->

## 1. Goal

Five review rounds found an owner turn's clock time recoverable from the committed record through a
new derived path each time: an idle gap's end, a stale extract, a killed verb's END, a killed bar's
`NONE` line, a compaction row, the commitment's last line time. Each fold closed the path it was shown,
and the next round found one the rule did not enumerate. The owner ruled on 2026-09-16 that the
committed record carries no time a journal or a transcript produced. Every time it keeps comes from a
source that is already public in git: a commit, or a row of the committed run-state file. Every other
time stays in the machine-local model and the runlog Skill's answers. That closes the class by
construction, and it supersedes `TOOL-dLoggedFlight-15`, `-17`, `-18` and `-19`.

## 2. Scope (IN)

- **S1** Declared sources. `RECORD_SCHEMA` in `tools/runlog/record.py` gives every `utc` and `duration`
  slot a declared source, and the only sources a time may have are `git` and `run-state`. Observed by
  AC1 and AC5.
- **S2** The timeline. The Timeline table renders only rows whose source is `git` or `run-state`:
  commits, merges, phase moves read from the run-state file's history, and its dispatch, brief and
  review rows. Rows from the driver, gates and pushes journals and from transcripts are not rendered.
  A Timeline fact renders their count per kind instead. The elided line's times come from the rows
  kept. Observed by AC2.
- **S3** The Summary. The window renders as the committer times of its first and last commits in the
  run's era, and the duration as the difference between them. A window bound that came from a journal
  line never renders. The commitment renders its digest and line count, never a line's time. Observed
  by AC3.
- **S4** Anomalies and coverage. The Anomalies table and the Coverage table carry no time column. An
  anomaly renders its kind, sub-class and count. A journal's epoch stays in the local model. Observed
  by AC4.
- **S5** The refusal retires. `scan_owner_times` and the render's owner-time refusal are removed, since
  no rendered time now comes from a source an owner act can set without the time already being public.
  Idle gaps render as a count only. Observed by AC6.
- **S6** The population check. A self-test arm renders a fixture model whose every journal and transcript
  event carries a sentinel second. It reads EVERY `utc` token of the rendered markdown and the Data twin.
  Each must equal a commit time or a run-state row time from the fixture, and none may equal a sentinel.
  The population is the rendered text, never a named list, which is the narrowing three rounds found.
  Observed by AC1.
- **S7** The schema leg. `check-records` refuses a committed record whose Timeline row has a source
  other than `git` or `run-state`, or whose layout carries a time column S4 removed, naming the record,
  the line and the rule. Observed by AC5.
- **S8** The Skill. `tools/runlog/SKILL.template.md` says the committed record carries no event times,
  and routes a question about when something happened to the local `model` answer. Observed by AC7.

## 3. Non-goals (OUT)

- The local model. It keeps every time it has, for the Skill's answers on this machine.
- Count correctness. `TOOL-dLoggedFlight-14` and `TOOL-dLoggedFlight-16` own which sources the counts
  rest on.
- Coarsening times into buckets. A bucket is still a clock time, and the ruling withholds the source,
  not the precision.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — the model's timeline, window and anomaly set, with each
  event's source.
- **consumes-from** `TOOL-dLoggedFlight-9` — the renderer, `RECORD_SCHEMA` and the refusal this unit
  retires.
- **consumes-from** `TOOL-dLoggedFlight-10` — the schema leg this unit gives the source rule.
- **consumes-from** `TOOL-dLoggedFlight-14` — the counts the record keeps in place of the times.

## 4. Design

The defect class was enumeration: each withholding rule ran over a narrower population than the leak.
This unit changes what is withheld from values to sources. A source either is already public or is not,
and that is decidable per slot, so there is no population to enumerate beyond the schema's own slots.
S6 then checks the rendered text itself, so a slot that escapes the declaration still fails.

Commit times and run-state row times can sit near an owner turn, because an agent often commits right
after the owner answers. They add nothing a reader cannot already get from `git log` on the public
remote, and that is why they are the kept sources.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `TIME_SOURCES` | constant | none |
| `check_time_sources` | function | `py.function`, led by `check` |

### Files touched (estimate)

`tools/runlog/{record.py,model.py,runlog.py,selftest.py,README.md,SKILL.template.md}`,
`.claude/skills/runlog/SKILL.md`, `memory/map/features/runlog.md` and the regenerated map.

### Alternatives rejected

- Continue the per-path holds of `TOOL-dLoggedFlight-15` to `-19`: rejected by the owner's ruling,
  after five rounds in which each audit widened the surface.
- Coarsen every rendered time to a bucket: rejected by §3.
- Drop the Timeline section: rejected, since commits and run-state rows are public and give the record
  its sequence.

## 5. Production-readiness checklist

- security — closes the owner-time class by source, not by path.
- perf / scale — the render does less; no git call is added.
- error / empty / loading states — a run with no commits in its era renders its window as `-`.
- observability — the per-kind counts replace the removed rows, so the record still says what happened.
- risks — a reader of the committed record loses the order of journal events; the local model keeps it.
- testing — each AC staged RED on its fixture, with S6's sentinel arm over the whole rendered text.
- migration — records committed before this unit are re-rendered by their next placement.
- user docs — the kit README's record section and the runlog Skill.

## 6. Acceptance criteria

- **AC1** — When `render_record` renders a fixture model whose every journal and transcript event carries
  a sentinel second, every `utc` token in the markdown and the Data twin equals a fixture commit time or
  run-state row time, and none equals a sentinel.
  Red when: any rendered time equals a sentinel, or a time slot has a source other than `git` or
  `run-state`.
- **AC2** — When `render_record` renders the same fixture, the Timeline holds only rows whose source is
  `git` or `run-state`, and its fact counts the withheld rows per kind.
  Red when: a verb, gate, push, compaction, limit, idle or workflow row renders.
- **AC3** — When `render_record` renders a run whose window ends at a journal line, the Summary window
  reads the committer times of the era's first and last commits, and the commitment reads its digest and
  line count only.
  Red when: the window or the commitment carries a journal time.
- **AC4** — When `render_record` renders anomalies and coverage, neither table has a time column.
  Red when: either table carries a `utc` column.
- **AC5** — When `check-records` reads a fixture record carrying a verb row with a time, it exits 1 naming
  the record, the line and the source rule.
  Red when: the record is accepted.
- **AC6** — When `grep -n scan_owner_times tools/runlog/record.py` runs, it finds nothing, and a render
  whose commit lands in the same second as an owner turn is not refused.
  Red when: the refusal remains or fires on a public commit time.
- **AC7** — When `grep -n 'no event times' .claude/skills/runlog/SKILL.md` runs, it finds the sentence
  that routes a time question to the local model.
  Red when: the Skill still tells a reader the committed record answers when something happened.

## 7. Gates

`runlog selftest` · `runlog record schema` · `runlog skill wiring` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each AC staged RED on its fixture, S6's sentinel arm over the whole render · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, from the owner's ruling of 2026-09-16; supersedes
  `TOOL-dLoggedFlight-15`, `-17`, `-18` and `-19`.

## 10. Reuse audit

The seams are `RECORD_SCHEMA`, `render_record` and `scan_owner_times` in `tools/runlog/record.py`, and
the schema leg `check-records` in `tools/runlog/runlog.py`, all this build's.
`tools/codebase-map/reuse_lookup.py "declare a source for every rendered time"` returned name-stem
candidates only. Outside this kit they are codebase-map's `derive_source_paths`, memory-recall's
`extract_declarations` and lexicon's `parse_ts_source`, unrelated name matches, and none declares a
source per rendered time.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
