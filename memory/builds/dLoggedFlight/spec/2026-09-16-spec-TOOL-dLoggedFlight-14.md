# TOOL-dLoggedFlight-14 — a session's transcript is read fresh, and a stale store extract never reads as covering the window

**Status:** SPECCED · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 14

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The run model reads a session's store extract before its live transcript, and never asks whether the
extract reaches the window's end. A stale extract therefore reads `present`. Idle gaps are then judged
without the owner turns and tool calls that came after it, and the owner-time refusal checks the same
stale turns, so it cannot see the turn it exists to protect. Closing review round 2 measured this as
R2-B1, round 1's B1 reproduced, and the loop promoted it here. Make every transcript-derived fact rest on
a source that covers the window, and make the refusal read its owner turns from a source the model did
not compute.

## 2. Scope (IN)

- **S1** Source order. `resolve_run_sessions` in `tools/runlog/model.py` reads a session's LIVE
  transcript whenever `resolve_session_tree` finds one, by extracting it in memory. A store extract
  stands in only where no transcript is local. Observed by AC1.
- **S2** Freshness. Every extract `tools/runlog/extract.py` writes carries `extracted_at`, the epoch
  second its extraction ran. A store extract that stands in for a session covers the window only when
  its `extracted_at` is at or after the window's end. An extract without the field, written before this
  unit, never covers a window. A session whose only source falls short reads `partial`. Observed by AC2
  and AC4.
- **S3** What coverage gates. Idle gaps are judged, and the owner-turn, usage and attributed-call facts
  render values, only when every named session's source covers the window's end. Otherwise idle gaps
  read not judged and those facts render `-`, as the M6 fold renders them for `not-local`. Observed by
  AC2.
- **S4** The discovered path. `--discover` attributes sessions heuristically when no journal names one,
  and its sessions take the same S1 order and S2 test. Observed by AC3.
- **S5** An independent refusal. When a named session's transcript is local, `record` re-reads that
  transcript's owner-turn seconds itself, through the extractor, and hands them to `scan_owner_times`
  beside the model's. The refusal then does not grade the model with the model's own turns. When no
  transcript is local, S3 has already withheld every value the refusal guards. Observed by AC5.
- **S6** The class, recorded. `memory/gotchas/withheld-value-recovered-from-a-derived-one.md` gains this
  instance: a cache preferred over its source, with its freshness key never read. Observed by AC6.

## 3. Non-goals (OUT)

- Refreshing or deleting store extracts. A stale extract is a fact about the store, and the model reads
  around it rather than rewriting it.
- The rows an owner act causes. `TOOL-dLoggedFlight-15` holds those, and this unit only fixes which
  owner turns the model and the refusal know.
- Byte-comparing an extract with a transcript. `tree_bytes` cannot be compared when no transcript is
  local, which is the only case an extract is read at all under S1.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-6` — the extract format this unit adds `extracted_at` to.
- **consumes-from** `TOOL-dLoggedFlight-8` — the session resolution and coverage block this unit changes.
- **consumes-from** `TOOL-dLoggedFlight-9` — the owner-time refusal this unit gives an independent read.
- **hands-off** `TOOL-dLoggedFlight-15` — the owner turns its held rows are measured against.

## 4. Design

The defect is a guard sharing a variable with the thing it guards, which charter section 7 names. The
idle-gap guard and the refusal both read owner turns from the extract whose staleness hides the turns.
S1 removes the cache from the common case: a local transcript is always the source, so a stale extract
can only matter where no transcript is local. S2 gives that remaining case a freshness key it can
actually read. S5 makes the backstop read a second source, so a future regression in the model's
turns is caught at render.

Extraction in memory costs a read of the session's transcript files per render. A render reads only
the run's named sessions, so the cost is bounded by those sessions' size, not by the store, and
`extract --measure` prints the rate report-only.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `extracted_at` | extract field | extract schema |
| `check_extract_covers` | function | `py.function`, led by `check` |
| `read_owner_seconds` | function | `py.function`, led by `read` |

### Files touched (estimate)

`tools/runlog/{model.py,extract.py,record.py,runlog.py,selftest.py,README.md}`,
`memory/gotchas/withheld-value-recovered-from-a-derived-one.md`, `memory/map/features/runlog.md`,
and fixtures named in `tools/runlog/kit.toml`.

### Alternatives rejected

- Keep the extract first and compare `tree_bytes` with the transcript's size: rejected, since it still
  reads the cache in the common case and a size match does not prove the content matches.
- Refresh a stale extract before a render: rejected by §3, since it writes the store from a read path.
- Widen the refusal's band around every owner turn instead: rejected, since it refuses ordinary
  records whose rows answered a turn within seconds, trading a leak for evidence loss (round 2, O2).

## 5. Production-readiness checklist

- security — the change removes a path by which an owner turn's time reaches a public record.
- perf / scale — a render extracts only its run's named sessions, in memory; the git-call count of
  `TOOL-dLoggedFlight-8` S12 does not change.
- error / empty / loading states — an extract without `extracted_at`, or one short of the window,
  reads `partial` and withholds; an unreadable transcript falls back per S1.
- observability — the coverage block names each session's source and whether it covers the window.
- risks — a render made mid-run on a long session reads more bytes than before.
- testing — each AC staged RED on its fixture; fixtures built by the real extractor over synthetic
  transcripts.
- migration — extracts written before this unit read `partial` until re-extracted.
- user docs — the kit README's model and extractor sections.

## 6. Acceptance criteria

- **AC1** — When `build_run_model` reads a fixture run whose session has a local transcript
  holding an in-window owner turn beside a twenty-minute driver silence, and a store extract cut before
  that turn, the model reads the transcript: no idle row lies within `IDLE_OWNER_GUARD_S` of the turn,
  and the in-window owner count is the transcript's.
  Red when: the store extract is read first, or an idle row ends beside the turn.
- **AC2** — When the same fixture has no local transcript and the extract's `extracted_at` falls before
  the window's end, the session reads `partial`, idle gaps read not judged, and the owner-turn, usage and
  attributed-call facts render `-`.
  Red when: a short extract reads `present`, or any of those facts renders a number.
- **AC3** — When `build_run_model` resolves a run through the discovered path with a stale store extract
  and a local transcript, it takes the transcript, and with no transcript it reads `partial`.
  Red when: the discovered path keeps the extract-first order.
- **AC4** — When `extract` writes a session, the object carries an integer `extracted_at`, and a store
  extract without the field never covers a window.
  Red when: the field is absent, or a field-less extract reads `present`.
- **AC5** — When `render_record` is handed a model whose owner turns are stale, and the rendered text
  carries an idle row ending beside a turn the local transcript holds, `record` refuses, naming the row
  and not the time.
  Red when: the refusal reads only the model's turns.
- **AC6** — When `python tools/memory-tree/gotchas.py --for-paths tools/runlog/model.py` runs, it selects
  `withheld-value-recovered-from-a-derived-one`, whose record names this instance.
  Red when: the class record does not name the stale-cache instance.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each AC staged RED on its fixture · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from closing review round 2's R2-B1 at the loop's
  NON-CONVERGENT exit.

## 10. Reuse audit

The seams are `resolve_run_sessions` and `resolve_session_tree` in `tools/runlog/model.py` and
`tools/runlog/extract.py`, and `scan_owner_times` in `tools/runlog/record.py`, all this build's. No
other kit reads a transcript. `tools/codebase-map/reuse_lookup.py "read a transcript fresh instead of a
cached extract"` returned name-stem candidates only; the relevant ones are this build's
`extract_session` and `read_session_ids`, and no candidate tests a cache's freshness.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
