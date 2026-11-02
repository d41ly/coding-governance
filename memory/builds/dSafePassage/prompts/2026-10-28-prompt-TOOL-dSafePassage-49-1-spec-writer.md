**Serves:** research TOOL-dSafePassage-49

# Brief: TOOL-dSafePassage-49's AC14 grades the named entry, and AC2's order sweep is moot on CLOSED units

## The prompt

No owner prompt. The build run's builder handed TOOL-dSafePassage-49 back as a DIVERGENCE (`wf_65aeefbf-dd6`, HEAD `9e91439d0`), and the run revises the spec under M2.

## The brief

### Goal

Every criterion of TOOL-dSafePassage-49 can go green against HEAD's code plus this unit's own writes.

**What the builder measured.**
1. **AC14 is red by construction.** It asserts that `--plant subsection-password-space` prints no substring of `se cret` longer than 2 characters. Every refused step prints TOOL-dSafePassage-24's fixed refusal from `run_step_isolated` (`tools/govkit/upgrade_steps.py`): "...declares what git runs as a program or sends as a credential, <entries>, so nothing was spawned". ` credential` contains `cre` and ` cr`, both pieces of `se cret`, so the assertion is red even when the redaction is correct. That lead text is pinned by the `[dSP-24]` needles in `tools/govkit/selftest.py`. The TOOL-45 and TOOL-38 plants escaped this only by luck.
2. **AC2 / S4 / §8 F1(a).** F1(a) RESOLVED that the build run's sweep moves TOOL-dSafePassage-4 to order 3 and -18/-19 to order 4 before the roster is handed out. That never happened. TOOL-4, -7, -18, -19 and -43 are now CLOSED. The run built them in consumes-from topological order, which is recorded in RUN.md's dispatch rows. Their headers still read 4 at order 2 and 18/19 at order 3, so AC2 ("TOOL-4's order is greater than TOOL-43's and TOOL-7's") is red, and a CLOSED spec's header is not this unit's to edit.
3. **For the rebuild (not divergences):**
   - AC12: `not refused` and `ssh://` sit on adjacent lines 71 and 72 of `help/upgrade-steps.md`, so one sentence needs reflowing.
   - AC5: "exactly one `startswith(DOWN_STOP_PREFIXES)` call" also needs the rollback fixture's own check at `upgrade_steps.py:4405` to compare through `test_step_row`.
   - AC3: the `rolled-back-witness-holds` plant cannot reach the walk through `derive_reverse_steps`, which drops `rolled-back` rows. The plant must record s2 `rolled-back` after the rows are derived, for example in the reverse child before `run_reverse_walk`.
   - S6/AC7 and AC8's data already hold.

**The main loop's recommendations.**
- **(1)** Make AC14 grade only the refusal's named entries, the text after TOOL-dSafePassage-24's fixed lead, for any 3-character piece of the password. Also grade the whole output for the full password and for each space-separated half. This is the class fix: any future password is graded the same way. Name the trap in AC14's Red-when.
- **(2)** Strike F1(a)'s sweep and AC2. The order relation it protected was dispatch order, and the run already honoured it by consumes-from. Record that in §8 F1 as re-resolved, citing RUN.md's dispatch sequence. S4 shrinks to whatever residual remains, or is struck.
- **(3)** Fold the rebuild notes into the criteria they touch.

Take each recommendation unless the code shows it breaks a written criterion. Record a rejected one in §8 with its reason.

### Items

1. **Revise TOOL-dSafePassage-49** as a rev bump dated 2026-10-28, still `DEFERRED`, with one §9 line naming this brief.
2. **Cross-read** TOOL-dSafePassage-45 (its AC6 no-substring assertion has the same latent class; it is CLOSED, so report it) and every DEFERRED spec that cites F1(a)'s sweep or TOOL-49's AC2. CLOSED specs are read-only.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- AC14 names the graded span and the fixed-lead trap. AC2 and the sweep are struck or re-resolved, citing RUN.md.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code.
- No edit to a CLOSED spec.
- No commit, and no stage into the real index.
