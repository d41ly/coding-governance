**Serves:** journal TOOL-dBoundRoles-54

# TOOL-dBoundRoles-54 — the first builder's return, a divergence

Run `wf_6da83969-b78`, started at `46e317547` on rev-5 in parallel with TOOL-dBoundRoles-16. It changed no file and
committed nothing; `diverged: true`.

## The divergence, as returned

S3, AC3 and the §4 Files touched entry "the spec of TOOL-dBoundRoles-49, a rev bump (S3)" cannot be built as written.
(1) S3 has this pass rev-bump TOOL-dBoundRoles-49's spec, restating its S3, its "Why two checks" paragraph and its
AC2 for the roster set. That spec is `CLOSED` at rev-5, closed by `fa3e705e1`, and the build method's M4 freezes a
CLOSED spec: its correction is a new unit on top. A repair unit corrects only an unbuilt sibling's spec, and unit 49
was unbuilt when this unit was specced but is built now. So AC3, which reads that spec's AC2 for the roster, cannot be
met by any edit this pass may make. (2) The path is outside the pass's declared write set.

The builder named two routes: (a) S3 and AC3 drop the edit to unit 49's spec. This spec's own §6 carries the restated
criterion, and unit 49's frozen AC2 gets a recorded deviation record in `build/` instead of a rev bump, with §4 Files
touched and the write set naming that record. (b) The main loop admits a CLOSED spec's rev bump and widens the write set.

Everything else held at `46e317547`: `tools/govkit/selftest.py#derive_roles_expected` holds the roles load S1 lifts,
`#derive_seed_expected` and unit 49's S3 overlay check exist, `tools/roles/roles_lib.py#load_roles`,
`tools/govkit/govkit.py#rule_sources` and `#resolve_rule_pool` exist, `gov-session` sets `agent: false` and has its
house overlay, and the lexicon accepts `derive_overlay_expected` as a `py.function`. The roster and the overlays now
number thirteen each (DERIVED, the builder's probe at `46e317547`), which AC1 already reads as derived.

## The decision

Route (a), by M3 as a delegated agent resolution: (b) edits a frozen spec, which M4 forbids. widens: none · relaxes:
none.
