# TOOL-dLoggedFlight-17 — the owner-time refusal re-reads every session the model read, and holds an idle row to the model's own guard

**Status:** WONTDO · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 16 · superseded by TOOL-dLoggedFlight-20 (owner, 2026-09-16: the committed record carries no journal or transcript time)

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-14` at rev-1 gave the owner-time refusal an independent read of owner turns, so
the renderer would stop grading the model with the model's own turns. Two gaps left it unable to refuse
the leak it was written for. It re-read only sessions the journal names, and on the shipped
`RUNLOG_SESSION_VARS=""` default the journal names none (H5). It kept `scan_owner_times`' second and
next-second comparison for an idle row, while the measured leak ends up to two minutes after the turn
(H4). The spec audit of units 14 and 15, round 1, confirmed both as HIGH, and the loop promoted them
here. Re-read owner turns from every session the model read, named or discovered. Refuse an idle row
with any known turn inside it or within `IDLE_OWNER_GUARD_S` of either end, which is the model's own
guard, so the refusal fires only where the renderer's turns and the model's disagree.

Every code line cited here was read at `a6f9d52e` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The sessions read. `build_run_model` records `coverage["transcripts"]["read"]`, the sorted
  ids of every session whose source `resolve_run_sessions` read, named or discovered, after
  `TOOL-dLoggedFlight-14` S4 kept it. The model already exposes only journal-named ids, as
  `sessions=sids` (`tools/runlog/model.py:1711`). The field lives in the local model. The renderer reads
  no key of it: the Coverage `sessions` fact renders counts, and a committed record carries no session
  id (`TOOL-dLoggedFlight-9` S4). Observed by AC4 and AC5.
- **S2** The independent read. `read_owner_seconds(model, projects)` in `tools/runlog/record.py`
  resolves each id in `transcripts.read` through `resolve_session_tree` and reads its turns through
  `scan_owner_turns` (`tools/runlog/extract.py:935`), keeping the integer second of every `owner`
  event. A session whose transcript is not local, or whose tree cannot be resolved, contributes
  nothing. It returns the seconds and the number of sessions it read. `write_record` takes `projects`
  and calls it, and `cmd_record` in `tools/runlog/runlog.py` passes the `projects` it already resolves
  on both its write path and its stdout path. `render_record` takes the seconds as `owner_seconds` and
  hands them to `scan_owner_times` beside the model's turns, so it stays a pure function with no file
  read. Observed by AC1, AC2 and AC4.
- **S3** The liveness line. `cmd_record` prints one report-only line to stdout, beside its existing
  wall line, naming the independent owner-turn read with `sessions=<n>` and `turns=<n>`. A refusal
  that read nothing then shows `sessions=0` rather than passing as one that found nothing. Observed by
  AC4.
- **S4** The idle-row comparison. `scan_owner_times` refuses an idle row when any owner second it holds,
  the model's or the independent read's, lies at or after the row's start second minus
  `IDLE_OWNER_GUARD_S`, and at or before its start second plus its duration plus one plus
  `IDLE_OWNER_GUARD_S`. That is `derive_idle_gaps`' own hold condition (`model.py:817`), widened by
  the two truncations the rendered start and duration carry. It names the row and never the time.
  Every UTC token keeps the same-second comparison, now against both sets of turns.
  `TOOL-dLoggedFlight-15` S4's band for held kinds is that unit's. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- Which source the model reads, and whether a store extract covers the window.
  `TOOL-dLoggedFlight-14` and `TOOL-dLoggedFlight-16` own those.
- A band around every rendered time. It refuses ordinary records whose rows answered a turn within
  seconds, which closing review round 2 recorded as O2.
- The held kinds' band, which `TOOL-dLoggedFlight-15` S4 owns.
- A committed count of independently read turns. The closed schema gains no fact, and S3's line is
  report-only.
- A render where no session read has a local transcript. The independent read is then empty, and the
  refusal grades with the model's turns alone. Wherever the model's own source fell short of the
  window, `TOOL-dLoggedFlight-16`'s `stale` has already withheld idle judgement.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-6` — `resolve_session_tree` and `scan_owner_turns`, the
  independent reader.
- **consumes-from** `TOOL-dLoggedFlight-8` — `resolve_run_sessions` and the transcripts coverage block,
  which gains `read`, and `derive_idle_gaps`' guard, which S4 mirrors.
- **consumes-from** `TOOL-dLoggedFlight-9` — `scan_owner_times`, `render_record` and `write_record`,
  which gain the independent seconds.
- **consumes-from** `TOOL-dLoggedFlight-14` — the source order and the discovered path's reach test,
  which fix which sessions are read.
- **hands-off** `TOOL-dLoggedFlight-15` — the owner turns the held-kind band compares against.
- **hands-off** `TOOL-dLoggedFlight-19` — the idle row's class and the guard that holds it.

## 4. Design

H4 is a check that cannot fail on the shape it exists for. Round 2 measured R2-B1's gaps ending within
two minutes after a real owner turn that the stale source did not hold, so the leak's precision is the
reply latency, and a same-second comparison sees none of it. The model already holds any gap with a
turn it knows inside it or within `IDLE_OWNER_GUARD_S`, 900 s, of either end (`model.py:92`, `:98`).
The renderer comparing at that same guard can therefore fire only where its turns and the model's
differ. It never refuses an ordinary record, which was O2's objection to a band on every time.

H5 is a population narrower than the leak. The shipped kit blanks `RUNLOG_SESSION_VARS`
(`tools/unattended/unattended.sh:343`), so no driver line carries a `sess.*` field and the journal
names no session. The model's discovered branch keys its extracts internally and exposes none of
their ids. S1 exposes every id read, so S2's read has the model's whole population.

The rendered start and duration are each truncated to the second, so the rendered row can sit up to
two seconds nearer a turn than the model measured. A turn lying within two seconds outside the guard
therefore refuses. That costs one record and never publishes a time.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `read_owner_seconds` | function | `py.function`, led by `read` |
| `read` | model coverage key | `coverage["transcripts"]` |
| `owner_seconds` | parameter | `render_record` and `scan_owner_times` |

### Files touched (estimate)

`tools/runlog/{model.py,record.py,runlog.py,selftest.py,README.md}` and
`memory/map/features/runlog.md`.

### Alternatives rejected

- Re-read only the sessions the journal names: rejected by H5, since the shipped default names none.
- Keep the same-second comparison for idle rows: rejected by H4, since the measured leak is minutes
  wide.
- Compare the model's exact idle floats rather than the rendered row: rejected, since the refusal's
  premise is grading the text it would publish, and the model is what a regression corrupts.
- Read the transcripts inside `render_record`: rejected, since the function's contract is no file
  read, and a pure render is what lets the record's arms run without a transcript tree.

## 5. Production-readiness checklist

- security — closes the shipped-default and the minutes-wide paths by which an idle row places an owner
  turn the model missed.
- perf / scale — one main-file extraction per session read with a local transcript, per render; the
  set is bounded by `TOOL-dLoggedFlight-14` S4, and the git-call count does not change.
- error / empty / loading states — an unresolvable tree contributes nothing, and S3's line counts only
  the sessions read.
- observability — S3's report-only line.
- risks — a turn lying within two seconds outside the guard refuses an ordinary record, per §4.
- testing — each AC staged RED against the rev-1 `scan_owner_times`; AC3 is the near miss that proves
  the control can pass.
- migration — none.
- user docs — the kit README's record section.

## 6. Acceptance criteria

- **AC1** — When `render_record` renders a model built from a store extract that omits an in-window
  owner turn, with `owner_seconds` from `read_owner_seconds` over the local transcript that holds it,
  and the text carries an idle row ending 30 s after that turn, it refuses, naming an idle row and no
  time.
  Red when: it renders, or the refusal message carries a UTC token; staged RED against the rev-1
  `scan_owner_times`, which compares the row's end second and the next.
  fixture: the model is built with `projects` withheld, so the store extract is its only source.
- **AC2** — When the same fixture's idle row ends 600 s after the turn, and in a variant starts 600 s
  after it, `render_record` refuses both.
  Red when: either renders.
- **AC3** — When the model reads the live transcript, so its turns equal the independent read's, and
  its one idle gap lies exactly `IDLE_OWNER_GUARD_S` plus two seconds from the nearest turn,
  `render_record` refuses nothing.
  Red when: it refuses.
  figure: DERIVED — the gap's placement is computed from `IDLE_OWNER_GUARD_S` read from the module.
- **AC4** — When a run's journal names no session and the discovered path reads one whose transcript
  is local, `read_owner_seconds` returns a non-empty set holding that session's turns, the arm asserts
  that before asserting AC1's refusal on it, and `runlog.py record` prints `sessions=1`.
  Red when: the set is empty, the line reads `sessions=0`, or the refusal fires with the set empty.
- **AC5** — When `build_run_model` reads the named fixture and the discovered fixture,
  `coverage["transcripts"]["read"]` holds exactly the ids of the sessions read, and no id appears in
  the record `render_record` writes, markdown or Data twin.
  Red when: a read id is missing, an unread id is present, or a rendered record carries an id.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each AC staged RED on its fixture · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from H4 and H5 of the spec audit of units 14 and 15,
  round 1, at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-14`'s S5 and AC5.

## 10. Reuse audit

The seams are `scan_owner_turns` and `resolve_session_tree` in `tools/runlog/extract.py`, and
`scan_owner_times` and `write_record` in `tools/runlog/record.py`, all this build's.
`tools/codebase-map/reuse_lookup.py "read a session's owner turns from its transcript"` returned
`extract_session` and `resolve_session_tree` as seams at fan-in 3; `scan_owner_turns` already reads a
main file's owner events and is extended rather than copied. No candidate compares an idle row with a
guard. The recall query returned only this build's own records.

Recall terms used: owner turn idle gap held near_owner refusal commitment verify window end stale extract coverage transcripts
