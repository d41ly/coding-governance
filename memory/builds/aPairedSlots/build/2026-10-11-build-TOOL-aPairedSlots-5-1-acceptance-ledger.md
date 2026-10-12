# Acceptance ledger — one slot per worktree, and the shared-path audit

**Serves:** journal TOOL-aPairedSlots-5

Observed on node a on 2026-10-11. The turnstile suite's new arm 43 was sliced and run over the
changed runner: 3 assertions, PASS. The claim was then staged to ignore the slot's `repo` file and
the arm run again: RED. The first slice of the arm read its two-worktree half red for a fixture
reason: the second worktree was checked out with CRLF under the host's global `core.autocrlf`, and
its runner refused the table; the arm now turns that off in the fixture before the checkout.

**Evidences:** TOOL-aPairedSlots-5
- AC1 — `GATE_TURNSTILE_SLOTS=2` — two fixture bars in one worktree never held at once (peak 1) and
  the second's queue line read `held, one by this worktree` naming the first's pid; two worktrees of
  one fixture repository held at once (peak 2). With the claim ignoring `repo` the one-worktree pair
  held at once (peak 2) and the line named no holder.
- AC2 — `2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md` — carries a row for every path the
  prompt names, each with its disposition and the measurement or code line behind it, and names
  TOOL-aPairedSlots-7 or -8 against every collision.
