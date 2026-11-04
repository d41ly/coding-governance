# Spec brief — TOOL-dFairHearing-43: the closing diff review's eight minors

**Serves:** research TOOL-dFairHearing-43

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Write the spec for `TOOL-dFairHearing-43` at `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-43.md`. This is the one unit that the closing diff review's exit promotes: `memory/builds/dFairHearing/reviews/2026-11-04-review-TOOL-dFairHearing-1-40-diff-review.md`, round 1, CLEAN WITH FIXES and CONVERGED, with 0 blockers, 0 highs and 8 confirmed minors. The build method's severity rule batches every MEDIUM and LOW into one unit. The run's amendment row adding the unit is in `memory/builds/dFairHearing/RUN.md`. Commit nothing; the main loop commits.

### Items
1. Carry every one of the review's eight items, in its `## Items` order, as scope items whose fix the review's ledger judged sound:
   - the checklist agent's command line pastes unchecked `base` and `head` (id 1);
   - checkDisposition and renderCell disagree on a `none` reason cell (id 2);
   - unattended-build's audit forward drops `twin` and `unclassed` (id 3);
   - spec-audit-optin.js finds the hooks kit at a hard-coded sibling path (id 4);
   - the AC19 quoting arm drives only the diff preset (id 7);
   - check_ungated has no caller outside its selftest (id 5);
   - kit.toml names `legManifest` (id 6);
   - a check_policy.py comment claims a check its case does not run (id 8).
   Read each finding's claim, reason and fix in the record's appendix, and re-ground each cited line against today's tree (`23e1a54d4`).
2. Left-shift each finding. Where an existing gate or arm can red on the class, name that arm. For the four findings whose disposition reads `new:<class>` (ids 1, 5, 6 and 8), the unit adds a catalogue class record under `memory/gotchas/` and regenerates `memory/gotchas/INDEX.md`, as unit 39 did. A render a template change moves is regenerated in the same unit.
3. One `New arm:` line per gate the unit adds, each naming a break that reds on today's code.
4. Write the unit's departure record, the way unit 39's deviation record `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-39-deviation-391.md` was written: cause `review finding`, evidence the review record and the RUN.md amendment row.
5. Header: order 29, after unit 40. Unit 40's header already `closes TOOL-dFairHearing-19`, and the build derives CLOSED. Choose the header's ask clause so that this unit's state never re-opens ask 19. Derive it from `memory/TEMPLATE-SPEC.md`, the build's BACKLOG.md and the README's rules, and say how in the spec. If the template needs an ask and none fits, record the fork in the open-questions section, resolved `RESOLVED (agent, 2026-11-04, delegated)` in README rule 5's shape.
6. Every criterion must be one a correct build can pass on today's tree. Check every backticked word of the acceptance section against `tools/check-spec-tokens.py`'s `BAR` pattern (lines 419 to 424). Do not cite in the acceptance section a file the unit will create; spell such a path in prose. Every change-log line names a section, a scope id or an acceptance id.
7. New tracked text must not cite a check, section or method rule by a bare number, such as "check 12" or an M-number. Name each by what it checks.

### Acceptance
A spec that conforms to `memory/TEMPLATE-SPEC.md` and carries all eight findings, each with a criterion that reds on today's code and greens on a correct build. Its departure record is written beside it.

### Gates
None you run.

### Non-goals
No code, and no other spec. Not the lexicon offender count, the replay scorer's stated-count reader or the playbook-parity leg guard: those are separate adopted units.
