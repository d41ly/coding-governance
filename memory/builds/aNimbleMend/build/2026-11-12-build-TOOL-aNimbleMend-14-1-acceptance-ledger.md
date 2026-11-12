# Acceptance ledger — TOOL-aNimbleMend-14

**Serves:** journal TOOL-aNimbleMend-14

Built against spec rev-1 in one pass commit. Each line is a probe of the changed code the builder made in the pass: the criterion's own command, run from the worktree's toplevel, over the primary checkout's ledger read-only or over the fixture of the spec's section 4 built under `%TEMP%`. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section, and the RED-first then GREEN observation of its new arm, the arm class "a carried-forward ledger row never opens the lane" of `tools/hooks/scratch-guard.test.sh`, which was written and never run; the rebuilt lane block of that suite and its raised `FLOOR_ASSERTIONS` are a static count the close confirms.

**Evidences:** TOOL-aNimbleMend-14
- AC1 — `[]` — `readOpenReds` over the primary checkout's git directory and toplevel printed the empty list, with the ledger there still holding 9 red rows. (PINNED, 2026-11-12)
- AC2 — `BLOCKED by scratch-guard` — the hook run against the primary checkout exited 2, its stderr opened with that refusal, and no line held the lane's witness.
- AC3 — `["at-head","held-at-head","unlanded"]` — the reader printed that list over the fixture with `GOV_DEFAULT_BRANCH=main`.
- AC4 — `["at-head","held-at-head"]` — printed under `GOV_DEFAULT_BRANCH=no-such-branch`; with the `LEG_MANIFEST` line taken out of the fixture's conf the reader printed the empty list.
- AC5 — `at-head, held-at-head, unlanded` — the hook exited 0 over the fixture with one stderr line holding those names and no landed leg; with the three open rows taken out of the ledger it exited 2 and printed no witness.
- AC6 — `function` — the criterion's `node -p` over `tools/policy/policy-mirror.js` printed it.
- AC7 — `LEG_MANIFEST` — the four greps printed 0, 1, 0 and 1 in the criterion's order.
