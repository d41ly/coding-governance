# TOOL-dEasedEffort-2 — acceptance ledger

**Serves:** journal TOOL-dEasedEffort-2

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran, from the worktree
root: the two `git diff` commands AC1 and AC2 name, before either ledger line was written, then every
command section 5 names over the edited working tree. The red side ran over copies of the unedited
ledger and class read from `HEAD`, and printed what AC1 to AC4 name for today. No criterion here
diffs to `HEAD`, so each prints the same before and after the pass commit. Owed to the main loop at
the close: the four legs section 6 lists, with the full bar. The spec declares no `New arm:`, so no
RED-first observation is owed.

**Evidences:** TOOL-dEasedEffort-2
- AC1 — `git diff --name-only 2a6f3975 e74ef35e8 -- .claude` — it printed the four agent-type paths, the `grep -c` for that form on the AC3 line printed `1`, the `diff` of the paths that line names against that output printed nothing, exit 0, and the `grep -c` for the old `HEAD` form printed `0` over the ledger. That last `grep -c` printed `1` on the unedited copy.
- AC2 — `git diff --numstat 2a6f3975 e74ef35e8 -- tools/roles/house/policy.toml` — it printed 4 added and 4 deleted, and over the AC1 line the three `grep -c` printed `1` and the `wc -l` printed `2`. The first and last greps printed `0` on the unedited copy.
- AC3 — `grep -c "Seven ways, and a spec set" "$G"` — it printed `1`, `grep -c "Six ways" "$G"` printed `0`, and over the Symptom range the bullet count printed `7` and the two bullet greps printed `1` each. The bullet count printed `6` on the unedited copy.
- AC4 — `grep -c "items L1 and L2"` — it printed `1` over the Where it bit range, and so did the `TOOL-dEasedEffort-1` grep. Both printed `0` on the unedited copy.
- AC5 — `git diff --numstat e74ef35e8 -- "$L"` — it printed 2 added and 2 deleted, and the `grep -cP` over the AC lines printed `5`.
- AC6 — `git diff e74ef35e8 -- "$G" | grep -c '^-[^-]'` — it printed `1`, the count-word line, and the anchor probe printed `3`, the count `memory/gotchas/INDEX.md` holds for this class.
