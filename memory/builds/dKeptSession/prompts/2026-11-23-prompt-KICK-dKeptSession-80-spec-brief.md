**Serves:** research KICK-dKeptSession-80

# Brief — dKeptSession: the run branch reconciled with origin/main at 525f3ab97

## The prompt

> /unattended dKeptSession

## The brief

### Goal

Every unit of this build is built, the closing review is recorded, and the run is at VERIFYING (witness
`0a39514a6`). The lander's `bash tools/push-main.sh --prepare --slug dKeptSession` refused and changed
nothing. Merging the run branch onto `origin/main` at `525f3ab97` conflicts.

`origin/main` is 193 commits (DERIVED, `git rev-list --count 8b8b1374..origin/main`) past `8b8b1374`, the
tip KICK-dKeptSession-69 reconciled with. The dQuietDisk and aFlattenedSeed landings are among them.

The refusal names the remedy: reconcile on the branch first (`git merge origin/main`, resolve, commit), then
run `--prepare` again.

KICK-dKeptSession-69 holds the first reconcile and is frozen at 8b8b1374, and its spec sits near the size
cap. So this second reconcile is a unit of its own, `KICK-dKeptSession-80`, added by
`--rescope --act add`.

Write its Tier-2 spec. Copy KICK-dKeptSession-69's reconcile procedure (its S1 to S4 and §4) and re-key it
to `525f3ab97`. Reuse that procedure; don't re-derive it.

### Items

0. The conflicts, from a trial `git merge --no-commit --no-ff origin/main`, aborted (33 files, DERIVED: `git diff --name-only --diff-filter=U` in that trial):
   - **Generated outputs, each re-rendered by its own generator and never hand-merged:**
     - `.governance/policy.json`
     - `help/reference/policy.md`
     - `memory/map/generated/MAP.md`
     - `memory/map/generated/symbols.json`
     - `tools/gate-legs.json`, rendered by `tools/run-gates/leg_factory.py --write` from the kit
       descriptors and govkit's registry
   - **The 22 chain packets** `memory/builds/<slug>/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, one
     per dClosedLoop build:
     - dBoundRoles, dCalibratedLens, dConvergedCharter, dDeclaredLoop, dFairHearing, dFurnishedOrders,
       dGroundRules, dIndexedDesign, dKeptSession, dLinkedLibrary, dMindYourWords, dOrderedCharter,
       dPlacedRequest, dRankedPlan, dSafePassage, dScopedBuild, dShippedRelease, dTendedCadence, dTotalRecall,
       dTrueNorth, dWellOiledMachine, dWitnessedBar.
     - This run carried the owner's repin of the dClosedLoop schedule instrument across all 22 (`91d470117`).
       Say how each packet resolves: re-rendered by `tools/chain-packet.py --write <slug>`, or which side's
       bytes are kept. A packet's `rendered at` pin must still read fresh to `check-spec-tokens.py`'s packet
       join after the merge.
   - **Product and configuration hunks, counted from the trial (DERIVED, `grep -c '^<<<<<<<'`):**
     - `.memory-tree.conf`: 2 hunks
     - `tools/govkit/registry.toml`: 3 hunks
     - `tools/lib/resolve-python.test.sh`: 2 hunks
     - `tools/policy/catalogue.toml`: 1 hunk
     - `tools/policy/check_policy.py`: 1 hunk
     - Each is resolved by keeping both sides' content: rows unioned, code joined. Name the rule per file in
       §4, as KICK-dKeptSession-69 §4 "The thirteen files" did.
   - **The kickoff manifest stamp** `memory/guides/SESSION-KICKOFF.md`: one stamp written over the merge, as
     KICK-dKeptSession-69 S4 does. Its body keeps both sides' dated corrections.
1. S1, the reconcile commit:
   - The main loop runs `git merge --no-ff --no-commit origin/main` in the run worktree.
   - The builder resolves every conflict by the rules above, regenerates as KICK-dKeptSession-69 S4 does
     (`regen.py --write` over a provisional merge commit), and commits nothing.
   - The main loop commits the merge with the trailer `Pass: KICK-dKeptSession-80`, hooks running.
2. Out of scope, stated in §3: the full bar's own reds. The close's full bar at `0a39514a6` read RED on 16
   of 119 legs (DERIVED, the close-bar-attribution record), against the run's own pre-merge tree. Most are graded against registries and code main
   changed, so they can only be read on the merged tree. The main loop re-runs the bar after this commit,
   attributes each red against `origin/main`, and clears the run's own reds through the red-fix lane, one
   record each.
3. Criteria, each observable at the merge commit:
   - no unmerged path;
   - `regen.py --check` exits 0;
   - `HEAD^2` is `525f3ab97`;
   - each product hunk's both sides are present by a grep;
   - the packets read fresh;
   - `manifest-check.sh` exits 0.
   The legs the merge moves go in §7.
4. Header:
   - Tier-2, `order 38` (after KICK-dKeptSession-79's 37), streams tooling, advancing
     KICK-dKeptSession-29.
   - `**Derived:** PLAY-dClosedLoop-2` on line 5, as the sibling promotions carry it.
   - No `New arm:` line unless a resolution adds code.
   - Cite code by `path#symbol`, and pin every figure with DERIVED or PINNED on its own line.
   - Keep within the live-spec size cap, and leave no fork open.
5. Files touched: the 33 files (DERIVED, item 0), plus what the regeneration rewrites, the merge's own records and this
   unit's acceptance ledger. Leave out `memory/DECISIONS.md`, a shared record a pass may not declare.

### Acceptance

These all report nothing for the new spec:
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`
- a plain `bash tools/memory-tree/check-memory-hygiene.sh --only 2`
- `python tools/check-spec-tokens.py --spec <path>`
- a PLAIN `python tools/check-spec-tokens.py`
- a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
- `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-80`

### Gates

Only those checks.

### Non-goals

- No product code, no commit, no merge and no index render.
- No spec other than KICK-dKeptSession-80's. Read the others; edit only the new spec, in the run worktree.
