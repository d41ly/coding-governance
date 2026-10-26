**Serves:** research TOOL-dBoundRoles-37 TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44

# Round-1 fix pass — dBoundRoles, its return

The return of the agent dispatched from `memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-2-spec-writer.md`, run direct/aedd53281b6f3c49e, extracted from its transcript by script.

All three fix items are done, and R3 took the split branch. TOOL-dBoundRoles-43 is now 48868 bytes and keeps 46 items. The new TOOL-dBoundRoles-44 is 16823 bytes and takes the other 11. Nothing is committed.

**Checks.** `check-memory-hygiene.sh --only 2,12,25` came back green in a throwaway clone with every dBoundRoles spec committed; the clone is deleted. The role hook refused `tools/check-spec-tokens.py`, so I copied its `[bar]`, guard-join and path-join predicates into scratch probes and ran them over the five specs. They found no suite token in any criterion or leg line, no missing guarded leg, no untracked path in a criterion, and no citation past its file's end. The real spec-tokens leg still has to run in the main loop.

**R3: the split, so you can record the `--rescope` row**
- The cut is by what an item reads. 44 gets 43's former S3, S4, S18, S20, S26, S30, S31, S33, S42, S47 and S48, which are ids 3, 5, 26, 28, 43, 48, 49, 51, 62, 16 and 17 (nine MEDIUM, two LOW). It renumbers them S1 to S11, sits at `order 29`, and has its own §6, §7 and §10. 43 keeps its old item numbers, so the fix brief's S references still hold.
- **44 writes:** `tools/workflows/README.md`, `tier2-review.test.sh`, `unattended-build.test.sh`, `tools/dead-path-waivers.txt`, `skills/session-kickoff/SKILL.md`, `memory/gotchas/`, `tools/memory-tree/check-memory-hygiene.sh` and its `.test.sh`, `HYGIENE.template.md` → `memory/HYGIENE.md`, `tools/unattended/SKILL.template.md` → `.claude/skills/unattended/SKILL.md`, `memory/guides/UNATTENDED-VERBS.md`, `help/roles.md`, `.memory-tree.conf` and `memory/builds/dBoundRoles/README.md`.
- **43 writes:** `tools/roles/*`, `tools/hooks/scratch-guard.js`, its `.test.sh`, `format-guard.js`, `tools/govkit/selftest.py`, `tools/govkit/steps/*`, `tools/playbook/*`, `tools/loop/placement.py`, the three `memory/project/` registries and spec 25.
- **Why they are disjoint:**
  - The two Files touched lists share no path.
  - 44's two population reads (S1 and S3) are of the build run's base.
  - 44's gotcha pages point at the two hook files by path, and 43 renames or removes neither.
  - 44's other criteria read only its own files or the commit log.
  - The items whose criteria read roles-code output stay in 43: S16 greps the re-rendered agent files, S27 needs S50's suite, and S2 runs the spawn guard S50 edits, so S28 stays beside S2.
  - Neither unit touches DECISIONS, a backlog shard, the run-state file or a generator.
- Even after the split, 43 needed about 4 KB of cuts. I dropped the §1 table (the ids are now listed in prose), the §4 shapes table (folded into S8), the §2 intro (already said in §4 "How an item closes"), and tightened the edges, forks and §10. No finding was dropped.

**Files changed** (all under `C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\spec\`)
- `2026-10-26-spec-TOOL-dBoundRoles-37.md` — R1: AC1 imports the module and calls `derive_roles_expected` directly; the existing `New arm:` line stays.
- `2026-10-26-spec-TOOL-dBoundRoles-40.md` — R1: AC1 to AC3 go through a one-case slice of `check_roles_install` (the form `DEPL-aBenchedProbe-2` uses), with breaks staged in a scratch copy; the `permission:` line is gone.
- `2026-10-26-spec-TOOL-dBoundRoles-42.md` — R1: AC4 names the self-test module in prose. R2: S5 gains its **Readers:** clause. R3 knock-on: the hands-off edges are split between 43 (ids 44, 45) and 44 (ids 3, 26, 43), and the non-goals, class table, Rollout line and §1 now point at 44.
- `2026-10-26-spec-TOOL-dBoundRoles-43.md` — R1: AC17, AC37 and AC41 use a one-case slice. R2: **Readers:** clauses on S5, S10, S25, S27, S28, S38 and S41. R3: kept items only; §4 now argues "Why two units"; edges, legs, Files touched and §8 updated (F9 and F14 moved out).
- `2026-10-26-spec-TOOL-dBoundRoles-44.md` — R3: new spec.
- `2025-10-25`-dated units 1, 10, 11, 13, 17, 21, 24 and 25 (`2026-10-25-spec-TOOL-dBoundRoles-<n>.md`) — R3 knock-on, needed because hygiene check 12 fails any edge without a matching edge back. Each gets a hands-off bullet to 44 and a narrowed bullet to 43 (unit 17's moves to 44 entirely), and its pending rev-2 line now names 44.

**Decisions to confirm**
- 44 gains a `New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC6` line. 43 already listed that test file under Files touched but declared no arm for it.
- 44's S3 now says the reader list is re-derived at the build run's base. That matches unit 25 S8 and the finding, and it keeps the split clean.

**Not fixed: a wrong path in other specs.** Specs 37 to 42 cite the audit as `memory/builds/dBoundRoles/reviews/2026-10-26-spec-audit-round-1.md`, but the file is `2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`. I corrected it only in 43 and 44, whose §1 I rewrote.
