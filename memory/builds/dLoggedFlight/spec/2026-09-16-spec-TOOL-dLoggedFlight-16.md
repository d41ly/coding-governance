# TOOL-dLoggedFlight-16 — an extract short of the window reads `stale`, and `partial` keeps its lower-bound meaning

**Status:** CLOSED · rev-2 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-dLoggedFlight-16-1-acceptance-ledger.md](../build/2026-09-16-build-TOOL-dLoggedFlight-16-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 |
| [2026-09-16-review-TOOL-dLoggedFlight-20-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-20-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-20 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-14` at rev-1 withheld the owner-turn, usage and attributed-call facts under
`partial` whenever a session's source fell short of the window. `TOOL-dLoggedFlight-9` S4 renders
those facts under `partial` as a lower bound, and its AC10 arm asserts integers for a named session
with no source. The two criteria could not both pass. The spec audit of units 14 and 15, round 1,
confirmed this as B1, a BLOCKER, and the loop promoted it here. Give a source that falls short of the
window its own coverage state, `stale`, which `COUNTED_STATES` does not hold. A stale extract then
withholds what it cannot vouch for, and a session with no source keeps unit 9's rendering. The
freshness key and the test that reads it move here from unit 14 S2.

Every code line cited here was read at `a6f9d52e` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The field. Every object `extract_session` in `tools/runlog/extract.py:839` returns carries
  `extracted_at`, the integer epoch second at which that extraction ran. The store copy
  `write_session` writes and the in-memory copy the model makes therefore both carry it. The self-test
  helper `write_extract` in `tools/runlog/selftest.py:2102`, which types an extract by hand, gains the
  field too. Its default is a fixed value at or after every window the suite builds, so no existing
  arm changes its reading, and it takes an argument to backdate or omit the field. Observed by AC1.
- **S2** The test. `check_extract_covers(data, window)` in `tools/runlog/model.py` answers True only
  when `data["extracted_at"]` is an integer at or after `window["end"]`. An extract without the field,
  or with any other value in it, never covers. `resolve_run_sessions` (`model.py:692`) takes the run's
  window and applies the test to every session whose source is a store extract, whether the journal
  named it or the store's slug attribution discovered it. A session extracted in memory from its live
  transcript covers by construction, since it was extracted during the render. Observed by AC2 and
  AC3.
- **S3** The state. `COVERAGE_STATES` (`model.py:65`) gains `stale`, appended after `not-local`. The
  transcripts read `stale` when at least one session the model read has a source that does not cover
  the window. Otherwise the existing rule stands unchanged: `present`, `partial` or `not-local`.
  `stale` outranks `partial`, so a render holding one stale session and one session with no source
  reads `stale`. The coverage note counts the sessions that read short and names none of them.
  Observed by AC2 and AC4.
- **S4** What `stale` withholds, through predicates that already exist. `COUNTED_STATES` in
  `tools/runlog/record.py:109` stays `("present", "partial")`. Under `stale`, the renderer's `known`
  test (`record.py:632`) writes the owner-turn, usage and attributed-call facts as `-`, and the
  model's `tr_state == "present"` test (`model.py:1598`) leaves idle gaps not judged. No new branch
  is added to either file for this: one predicate decides every shape. Unit 9 S4's count rule, and the
  count assertions of its AC10 arm, `test_record_ac10_unknown_counts` (`selftest.py:4689`), stand
  unedited. That arm's `--close` Timeline `rc` loop is `TOOL-dLoggedFlight-22`'s to retire with the verb
  rows, and this unit pins nothing in it. Observed by AC4.
- **S5** The three-shape arm. One self-test arm renders, through `render_record`, three models side
  by side. The first has a named session whose only source is a store extract with `extracted_at` one
  second before the window's end. The second has one whose extract carries no `extracted_at`. The
  third has a fresh named session and a second named session with no source, AC10's shape. It asserts
  each shape's state, its three facts and its idle judgement against `COUNTED_STATES` read from the
  module, never against a typed list of states. Observed by AC4.
- **S6** The Skill. `tools/runlog/SKILL.template.md` gains a **Stale transcript** bullet beside its
  **No local transcript** bullet (`SKILL.template.md:73`). It says an extract that stops before the
  run's end reads `stale`, and that the record then writes those facts as `-` and judges no idle gap.
  `.claude/skills/runlog/SKILL.md` is re-rendered by `tools/runlog/adopt-runlog.sh --scaffold`.
  Observed by AC5.

## 3. Non-goals (OUT)

- Which source is read first. `TOOL-dLoggedFlight-14` makes a live transcript win over a store
  extract. Until it lands, an extract beside a local transcript is still read, and S2 grades it.
- Refreshing or deleting a stale extract. A stale extract is a fact about the store, and the model
  reads around it rather than rewriting it from a read path.
- Comparing an extract's `tree_bytes` with its transcript's size. The size is unreadable exactly when
  no transcript is local, and a size match does not prove the content matches.
- The discovered path's window filter, which `TOOL-dLoggedFlight-14` S4 adds.
- A judged marker for the tool-call anomalies, which closing review round 2 raised as R2-M2. Whatever
  carries it keys on `COUNTED_STATES`, the one predicate this unit leaves in place.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-6` — the extract object `extract_session` returns and
  `write_session` stores, which gains `extracted_at`.
- **consumes-from** `TOOL-dLoggedFlight-8` — `resolve_run_sessions` and `COVERAGE_STATES`, which gain
  the freshness test and the `stale` state.
- **consumes-from** `TOOL-dLoggedFlight-9` — the count rule `COUNTED_STATES` and its AC10 arm, which
  this unit relies on unchanged, and the S4 list of coverage states, which gains `stale`.
- **consumes-from** `TOOL-dLoggedFlight-12` — the Skill's paragraph on missing transcripts, which gains
  a `stale` bullet.
- **hands-off** `TOOL-dLoggedFlight-14` — the source order that decides when a store extract stands in
  at all, and the discovered-path arm that reads `stale`.
- **hands-off** `TOOL-dLoggedFlight-22` — the `--close` Timeline `rc` loop of the AC10 arm, which that
  unit retires with the verb rows; S4 and AC4 pin only the arm's count assertions.

## 4. Design

A stale extract and a missing session are both undercounts, and they differ in what a reader can see.
A missing session is named by the coverage note, so its counts read as the lower bound unit 9 says
they are. A stale extract was indistinguishable from a complete one, which is how R2-B1 published idle
gaps beside owner turns the extract never held. A state of its own makes the difference visible in
the Sources table, and it keeps the withholding decision in the one predicate unit 9 already owns.

The model already withholds everything B1 needs through two tests: the renderer's count test over
`COUNTED_STATES` and the model's idle test over `present`. So the whole mechanism is a field, a
comparison and a vocabulary word. The unit adds no renderer branch, and that absence is the design:
two tests deciding one withholding is the shape B1 was.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `extracted_at` | extract field | extract schema |
| `check_extract_covers` | function | `py.function`, led by `check` |
| `stale` | coverage state | `COVERAGE_STATES` vocabulary |

### Files touched (estimate)

`tools/runlog/{extract.py,model.py,selftest.py,README.md,SKILL.template.md}`,
`.claude/skills/runlog/SKILL.md` and `memory/map/features/runlog.md`.

### Alternatives rejected

The fork is F1 in §8. Each option was tested against the two criteria B1 found in conflict.

- Supersede unit 9 S4's `partial` clause and its AC10 near-miss arm: rejected by M3's first veto,
  since it fails AC10 as that closed unit wrote it.
- Keep the state `present` or `partial` and add a per-session covers-window flag the renderer reads
  beside `COUNTED_STATES`: rejected by the same veto, since unit 14 rev-1 AC4 is red when a field-less
  extract reads `present`. It would also make two tests decide one withholding and add a Coverage fact
  to the closed schema.

## 5. Production-readiness checklist

- security — a stale extract can no longer put idle gaps or clean-looking counts into a public record.
- perf / scale — one integer comparison per session read; no git call and no extra read.
- error / empty / loading states — a missing or malformed `extracted_at` never covers, so the render
  reads `stale` and withholds.
- observability — the Sources table's `transcripts` row reads `stale`, and the model's coverage note
  counts the short sessions.
- risks — a render made from an old extract loses its counts until the session is re-extracted, which
  is the intended trade.
- testing — each AC staged RED on its fixture; extracts made by the real extractor where the arm needs
  one, and by `write_extract` with the field backdated or omitted where it needs a short one.
- migration — every extract written before this unit reads `stale` until re-extracted. No run record
  is committed in this tree, and the `coverage-state` vocabulary only widens.
- user docs — the kit README's coverage section and the Skill's `stale` bullet.

## 6. Acceptance criteria

- **AC1** — When `extract_session` extracts a synthetic transcript and `write_session` stores the
  result, both objects carry an integer `extracted_at` at or after the epoch second read just before
  the call and at or before the one read just after it.
  Red when: the field is absent, is not an integer, or falls outside that bracket.
- **AC2** — When `build_run_model` reads a fixture run whose one named session has no local transcript
  and a store extract with `extracted_at` one second before the window's end, the transcripts read
  `stale`. With `extracted_at` equal to the window's end they read `present`.
  Red when: the short extract reads `present`, or the one at the end reads `stale`.
  figure: DERIVED — the window's end is read from a first build of the same fixture with no store,
  never typed.
- **AC3** — When the extract carries no `extracted_at`, or carries the string `"1"` in its place, the
  transcripts read `stale`.
  Red when: either extract reads `present`.
- **AC4** — When the S5 arm renders its three shapes through `render_record`, the stale and the
  field-less shapes read `stale`, render `-` for every owner-turn, usage and attributed-call count, and
  render the Coverage `idle gaps` fact as `judged no`. The shape with a session missing reads `partial`
  and renders those counts
  as integers. A fourth model holding one stale session and one missing session reads `stale`.
  Red when: a stale shape renders an integer or judges idle gaps, the missing-session shape renders
  `-`, the mixed model reads `partial`, or a count assertion of `test_record_ac10_unknown_counts` needs
  an edit to pass.
- **AC5** — When `bash tools/runlog/adopt-runlog.sh --check` runs after the template edit and the
  re-render, it passes, and the rendered Skill carries the word `stale` in its missing-source bullets.
  Red when: the check fails, or the rendered Skill does not name `stale`.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each AC staged RED on its fixture · floor raised by the arm count

## 8. Open questions

- **F1** Which outcome does a source short of the window get, when unit 9 renders counts under
  `partial`? Options: a new state the renderer withholds; superseding unit 9 S4's `partial` clause; or
  a covers-window flag beside the existing states. RESOLVED (agent, 2026-09-16, delegated): a new
  state, `stale`. It is the only option that fails neither unit 9's AC10 nor unit 14 rev-1's AC4, and
  it keeps one predicate deciding the withholding. §4 records why the other two lost.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from B1 of the spec audit of units 14 and 15, round 1,
  at the loop's BOUNDED exit. `extracted_at` and the freshness test move here from unit 14 S2.
- rev-2 · 2026-09-16 · S4 · AC4 · §3 · B2 of the spec audit of units 14, 16 and 20, round 1, promoted to
  `TOOL-dLoggedFlight-22`. S4 and AC4 said the AC10 arm stands unedited, and that unit retires the arm's
  verb-row loop, so the two could not both pass one bar run. "Unedited" now names the arm's count
  assertions only, and the edge to `-22` says who edits the rest.

## 10. Reuse audit

The seams are `extract_session` and `write_session` in `tools/runlog/extract.py`,
`resolve_run_sessions` and `COVERAGE_STATES` in `tools/runlog/model.py`, and `COUNTED_STATES` in
`tools/runlog/record.py`, all this build's. `tools/codebase-map/reuse_lookup.py "an extract's
extraction time decides whether it covers a window"` returned `extract_session` as a seam at fan-in 3
and `check_in_window`, and no candidate tests an extract's freshness, so the field and its test are
new. The recall query returned only this build's own records.

Recall terms used: owner turn idle gap held near_owner refusal commitment verify window end stale extract coverage transcripts
