# TOOL-dLoggedFlight-14 — a session's live transcript is read before its store extract, on the named and the discovered path

**Status:** CLOSED · rev-4 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-dLoggedFlight-14-1-acceptance-ledger.md](../build/2026-09-16-build-TOOL-dLoggedFlight-14-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 |
| [2026-09-16-review-TOOL-dLoggedFlight-14-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-14-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-15 |
| [2026-09-16-review-TOOL-dLoggedFlight-20-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-20-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 |

<!-- /gen:spec-records -->

## 1. Goal

The run model reads a session's store extract before its live transcript. A stale extract then hides
the owner turns and tool calls that came after it, and the idle-gap guard judges with the same stale
turns. Closing review round 2 measured this as R2-B1, round 1's B1 reproduced, and the loop promoted
it here. Make a local transcript the source of every session it belongs to, named or discovered, and
read on the discovered path only the sessions that reach the run's window.

The spec audit of this unit, round 1, moved two halves out. The freshness key, its test and what a
short source withholds are `TOOL-dLoggedFlight-16` (B1). The independent owner-time refusal went to
`TOOL-dLoggedFlight-17` (H4, H5), which the owner's ruling of 2026-09-16 superseded by
`TOOL-dLoggedFlight-20`: the record carries no journal or transcript time, so no owner time is left to
refuse. What this unit still owns is count correctness.

## 2. Scope (IN)

- **S1** Source order. `resolve_run_sessions` in `tools/runlog/model.py` reads a session's LIVE
  transcript whenever `resolve_session_tree` finds one, by extracting it in memory. A store extract
  stands in only where no transcript is local. Observed by AC1.
- **S2** Moved to `TOOL-dLoggedFlight-16` S1 to S3, which owns `extracted_at`,
  `check_extract_covers` and the `stale` state. NOT OBSERVED here: that unit's AC1 to AC4 observe it.
- **S3** Moved to `TOOL-dLoggedFlight-16` S3 and S4. A short source reads `stale`, which
  `COUNTED_STATES` does not hold, so `partial` keeps `TOOL-dLoggedFlight-9` S4's lower-bound
  rendering. NOT OBSERVED here: that unit's AC4 observes it.
- **S4** The discovered path. `--discover` attributes sessions by slug when no journal names one.
  Each discovered session takes S1's order. A session is read only when it reaches the run's window,
  decided before anything is extracted:
  - with its transcript local, the latest modification time among its session tree's files must lie
    at or after the window's start, else it is dropped unread; once extracted, it is kept only when an
    event lies inside the window;
  - with no transcript local, its store extract must hold an event inside the window, else it is
    dropped.

  The sessions S4 keeps are the sessions the model read, for every rule that counts or tests sessions:
  `TOOL-dLoggedFlight-16`'s freshness test and every transcript-derived count the record keeps. The
  Coverage `sessions` fact's extracted count is the number kept. Observed by AC3 and AC7.
- **S5** Retired. It moved to `TOOL-dLoggedFlight-17`, which `TOOL-dLoggedFlight-20` supersedes: the
  committed record no longer carries a time the refusal guarded. NOT OBSERVED here.
- **S6** The class, recorded. `memory/gotchas/withheld-value-recovered-from-a-derived-one.md` gains this
  instance: a cache preferred over its source, with its freshness key never read. Observed by AC6.

## 3. Non-goals (OUT)

- Whether a store extract covers the window, and what a short one withholds. `TOOL-dLoggedFlight-16`
  owns both.
- Any committed time. `TOOL-dLoggedFlight-20` keeps every journal and transcript time out of the
  record, which retired the owner-time refusal and the held rows.
- One residue of S4, stated because it cannot be read away. A session whose transcript has left this
  machine, and whose extract was made before it did anything inside the window, is indistinguishable
  from an earlier run's session, and it is dropped. With no other session kept, the transcripts read
  `not-local` and withhold. With another session kept, the counts are short by that session. The
  discovered path is heuristic, and the model's coverage note already says so.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-6` — the extractor this unit runs in memory on a live
  transcript, and the session tree it stats.
- **consumes-from** `TOOL-dLoggedFlight-8` — the session resolution and coverage block this unit
  changes.
- **consumes-from** `TOOL-dLoggedFlight-16` — the window `resolve_run_sessions` takes, and the `stale`
  state the discovered-path arm reads.
- **hands-off** `TOOL-dLoggedFlight-15` — superseded by `TOOL-dLoggedFlight-20`; the edge stays because
  that retired record declares it.
- **hands-off** `TOOL-dLoggedFlight-17` — superseded by `TOOL-dLoggedFlight-20`; the edge stays because
  that retired record declares it.
- **hands-off** `TOOL-dLoggedFlight-20` — the transcript-derived counts the record keeps once every
  journal and transcript time is withheld.

## 4. Design

The defect is a guard sharing a variable with the thing it guards, which charter section 7 names. The
idle-gap guard read owner turns from the extract whose staleness hid the turns. S1 removes the cache
from the common case: a local transcript is always the source, so a stale extract can only matter
where no transcript is local, and `TOOL-dLoggedFlight-16` grades that case.

Extraction in memory costs a read of the session's transcript files per render. On the discovered
path the store holds every past session of the build, and extracting each of them on every render
would read the build's whole history. S4 therefore decides reach before extraction. A local
transcript's file times cost one stat per file. A missing transcript leaves only the extract, which is
read already.

### Inventory

This unit mints no identifier. `resolve_run_sessions` takes the window that `TOOL-dLoggedFlight-16`
passes it.

### Files touched (estimate)

`tools/runlog/{model.py,selftest.py,README.md}`,
`memory/gotchas/withheld-value-recovered-from-a-derived-one.md` and `memory/map/features/runlog.md`.

### Alternatives rejected

- Keep the extract first and compare `tree_bytes` with the transcript's size: rejected, since it still
  reads the cache in the common case and a size match does not prove the content matches.
- Filter discovered sessions only by the store extract's events, as the audit's M4 fix first put it:
  rejected for a local transcript, since a stale extract cut before the window would drop the session
  that ran it.
- Keep every discovered session and let the freshness test grade it: rejected by M4, since an earlier
  run's extract whose transcript was purged can never be refreshed and would read `stale` forever.

## 5. Production-readiness checklist

- security — the model's owner turns and idle judgement come from the transcript wherever one is local.
- perf / scale — a render extracts only the sessions S4 keeps; a past session with a local transcript
  costs a stat per file, and the git-call count of `TOOL-dLoggedFlight-8` S12 does not change.
- error / empty / loading states — an unreadable transcript falls back per S1; a session tree whose
  files cannot be stat'ed is extracted, the safe direction.
- observability — the Coverage `sessions` fact counts the extracts read, so a render that read a
  build's history shows it.
- risks — a render made mid-run on a long session reads more bytes than before; S4's residue in §3.
- testing — each AC staged RED on its fixture; fixtures built by the real extractor over synthetic
  transcripts.
- migration — none; a store extract is read as before wherever no transcript is local.
- user docs — the kit README's model and extractor sections.

## 6. Acceptance criteria

- **AC1** — When `build_run_model` reads a fixture run whose session has a local transcript
  holding an in-window owner turn beside a twenty-minute driver silence, and a store extract cut before
  that turn, the model reads the transcript: no idle row lies within `IDLE_OWNER_GUARD_S` of the turn,
  and the in-window owner count is the transcript's.
  Red when: the store extract is read first, or an idle row ends beside the turn.
- **AC3** — When `build_run_model` resolves a run through the discovered path with a stale store
  extract and a local transcript, it takes the transcript. With no transcript local and that extract
  holding an in-window event, the transcripts read `stale`, the Coverage `idle gaps` fact reads
  `judged no`, and the owner-turn, usage and attributed-call facts render `-`.
  Red when: the discovered path keeps the extract-first order, or a stale discovered extract leaves
  idle gaps judged or a count rendered; staged RED by applying the freshness test to named sessions
  only.
- **AC6** — When `python tools/memory-tree/gotchas.py --for-paths tools/runlog/model.py` runs, it selects
  `withheld-value-recovered-from-a-derived-one`, whose record names this instance.
  Red when: the class record does not name the stale-cache instance.
- **AC7** — When the `--discover` fixture's store also holds an extract of the same slug from an
  earlier session, whose every event and whose `extracted_at` precede the window's start, with no
  local transcript, that session is not read: the Coverage `sessions` fact's extracted count excludes
  it, and the state is the one the run's own session gives. With that session's transcript local and
  its files last modified before the window's start, the arm's count of `extract_session` calls shows
  it was not extracted. With that session's transcript local, its files last modified at or after the
  window's start and every event before it, the count shows it extracted once, and the Coverage
  `sessions` fact's extracted count excludes it.
  Red when: the earlier session is read, turns the state `stale`, or is extracted while its files
  precede the window, or the session with later-touched files and no in-window event is counted.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each AC staged RED on its fixture · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from closing review round 2's R2-B1 at the loop's
  NON-CONVERGENT exit.
- rev-2 · 2026-09-16 · §1 · §3 · §4 · S2 S3 S4 S5 · AC2 AC3 AC4 AC5 AC7 · folded the spec audit of
  units 14 and 15, round 1. M3: S4 names the discovered sessions as sessions the model read for every
  rule over sessions, and AC3 asserts a stale discovered extract withholds. M4: S4 drops a discovered
  session that does not reach the window before extracting it, and AC7 pins an earlier session of the
  same slug. The promotions: B1 went to `TOOL-dLoggedFlight-16`, which takes S2, S3, AC2 and AC4. H4
  and H5 went to `TOOL-dLoggedFlight-17`, which takes S5 and AC5. The order moves from 14 to 15 so unit
  16 lands first, the title drops the half that moved, and the edge to `TOOL-dLoggedFlight-9` left with
  S5.
- rev-3 · 2026-09-16 · §1 · S4 · S5 · §3 · the owner's ruling of 2026-09-16 (no journal or
  transcript time is committed) supersedes `TOOL-dLoggedFlight-15` and `-17` by `TOOL-dLoggedFlight-20`:
  S5 retires, and this unit keeps count correctness.
- rev-4 · 2026-09-16 · AC7 · folded M3 of the spec audit of units 14, 16 and 20, round 1. S4's local
  transcript rule has two clauses, and AC7 reached only the first. AC7 gains an arm for the second: a
  session whose files were touched at or after the window's start and whose every event precedes it is
  extracted and not counted.

## 10. Reuse audit

The seams are `resolve_run_sessions` in `tools/runlog/model.py`, and `resolve_session_tree` and
`extract_session` in `tools/runlog/extract.py`, all this build's. No other kit reads a transcript.
`tools/codebase-map/reuse_lookup.py "read a transcript fresh instead of a cached extract"` returned
name-stem candidates only; the relevant ones are this build's `extract_session` and
`read_session_ids`, and no candidate tests a cache's freshness. The rev-2 probe,
`reuse_lookup.py "read a session's owner turns from its transcript"`, returned `extract_session` and
`resolve_session_tree` as seams at fan-in 3, which S1 and S4 extend.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
