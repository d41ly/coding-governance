---
slug: aProvenReuse
node: a
opened: 2026-08-31
streams: tooling
status: INPROGRESS
roster: TOOL
ids: TOOL-aProvenReuse-1 TOOL-aProvenReuse-2
authorized-by: prompt
---

# aProvenReuse — the reuse-first rule gets a machine half

## The problem this build exists to solve

`reuse-first` is a DIRECTIVE of every unattended run and it is enforced by nothing. `grep -n reuse`
over `tools/unattended/unattended.sh` returns exactly one hit — the handle's own name inside
`DIRECTIVES_CORE` — and over `tools/unattended/check-unattended.sh` it returns a comment about an
unrelated check. The kit's own Skill states the hole in as many words: *"Waiving it is SILENT: the
bar stays green over a build that skipped the reuse probes, because nothing machine-checks a spec's
reuse section for content."*

That is not a theoretical hole and this build did not have to guess at its size. Over the 346
post-`SPEC10_CUTOFF` specs in this tree that carry a §10 Reuse audit:

- **188 (54%) record no recall terms at all.** `memory/guides/BUILD-METHOD.md` M5 requires them by
  name, and M7's regrounding step 5 — *"Re-run the recall probe with the terms recorded in that
  spec's §10"* — therefore resolves to nothing for the majority of the corpus. A method step that
  cannot execute is a step nobody notices is missing.
- **176 (51%) name neither probe.** Not `reuse_lookup.py`, not `query.py`, not an explicit
  "no existing seam fits".
- **93 (27%) satisfy both halves of what M5 actually asks for.**

Hygiene check 12 already parses every one of those §10 sections. It grades them on three things —
the heading is present, the body is non-empty, no skeleton placeholder survives — and on nothing
else, so `N/A — none` is a passing reuse audit. The owner's prose is the mandate and is recorded
verbatim under [prompts/](prompts/2026-08-31-prompt-TOOL-aProvenReuse-1.md).

## Expected improvements

- A spec dated at or after a declared cutoff cannot land claiming a reuse audit it did not record.
  The 253 specs that would fail the predicate today are grandfathered, exactly as `SPEC10_CUTOFF`,
  `STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF` and `FORK_MARK_CUTOFF` already grandfather their own.
- M7 regrounding step 5 becomes executable for every spec written from here on.
- An unattended run that never ran a recall probe cannot reach `--close` silently. It can still
  override, but the override is recorded and reaches the wrap-up, which is the difference between a
  skipped check and an invisible one.
- Waiving `reuse-first` stops being silent. The waived run's `reuse-probed` line names the waiver
  and its reason instead of passing without comment.

## Detriments if this is not built

- Every future build keeps paying to rediscover seams the tree already has, which is the specific
  harm the owner's prompt names.
- The directive table keeps carrying a handle whose waiver changes nothing observable, so the
  waiver mechanism reports coverage it does not have.
- `reuse-first` remains the one directive in a 16-handle set whose satisfaction leaves no trace on
  disk, and a set with one unobservable member cannot be audited as a set.

## Build-level rules

- **Classification (M2), written before acting**: both units were MISSING at open — no conforming
  spec carried either id — and are authored by this run at Tier 1. Neither adds a write path, a
  migration, an auth surface or a shared contract; both extend an existing checker in place.
- **Two mechanisms, two units, and the split is the tracked/local boundary.** Unit 1's evidence is
  a tracked file, so it belongs on the merge bar and works in any clone. Unit 2's evidence is a
  node-local log in the git common dir, so it belongs to the driver and could never be a bar leg.
  Putting both in one spec would make the closing diff unable to say which half a finding lands on.
- **The third gap found is deliberately NOT built, and the reason is M3 veto 2.**
  `tools/codebase-map/reuse_lookup.py` writes no log, while `tools/memory-recall/query.py` writes
  one — so of M5's two probes only one has liveness evidence available. Closing that asymmetry means
  either a cross-kit dependency (codebase-map reading a memory-recall convention) or a third
  telemetry format and a third kit version bump. It is not strictly beneficial, so protocol §11
  makes it a backlog row rather than an adoption.
- **Neither unit may red a landed spec.** A predicate that reds 253 tracked files is not a gate, it
  is a migration nobody asked for. The cutoff idiom is the whole reason this is landable.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aProvenReuse-1` | OPEN | hygiene check 12 grades §10's CONTENT, behind a declared cutoff |
| 2 | `TOOL-aProvenReuse-2` | OPEN | a `reuse-probed` DoD item joins the run to the recall query log |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 0 unit(s) · node a · opened 2026-08-31 · streams tooling
ids TOOL-aProvenReuse-1 TOOL-aProvenReuse-2

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
