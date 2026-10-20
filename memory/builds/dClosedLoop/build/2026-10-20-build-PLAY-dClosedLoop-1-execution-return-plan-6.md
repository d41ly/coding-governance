# Return: the execution plan's writer, resumed to fold the owner's walk

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 230's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-56-spec-writer.md`.

---

The walk's four changes are folded into the plan; the schedule script didn't need to change, and nothing is committed. Re-run at HEAD `a93477abc` it exits 0 and matches the pasted `[schedule]` block. One question is left for the owner: whether the self-test waiver should reach builds that touch `tools/` but don't change the driver (under "Left open" below).

## The four changes, as applied

**1. Unit family by stream** ("Family by stream", ER:438).
- **How it's derived:** `open.py` matches the owner's own words against two cells in each build's v2 row: its Stage and the noun at the end of its slug. `charter` or `playbook` gives PLAY, `session` or `kickoff` gives KICK, `deploy` gives DEPL, anything else TOOL. `open.py --families` prints the table, and the per-build summary carries each family.
- **What I tried first and dropped:** counting how many of a build's clauses name each stream. It put dOrderedCharter (12 of 37 clauses) below any natural cut and made dSafePassage, which talks about adopters, a deploy build.
- **Result** (pasted into P0.5 from my run of the same rule):

| Family | Builds | Matched on |
|---|---|---|
| PLAY | dOrderedCharter, dConvergedCharter | slug noun "Charter" |
| KICK | dKeptSession | stage "Session" |
| DEPL | dShippedRelease | stage "Deploy" |
| TOOL | the other 18 | nothing matched |

- **Also updated:** P0.5's family row (now also sets `roster:` and `streams:`), P0.6 minting rules 1 and 2 (mint in the build's derived family), and new P0.8 row 8. The plan had no example chain ids to fix.

**2. The opening read** ("Rows + dTrueNorth (Recommended)", ER:446).
- **Summary:** P0.5 defines `open.py --summary`, one row per build with: slug, stage, parents, unit count, family and `streams:`, ask id (or "none: whole run"), packet size and check result, the `may:` line verbatim, `spec-audit:` date, whether it is driver-changing, and whether its contract row is present. `open.py --check` fails a summary row that disagrees with the files, with a planted red.
- **Owner's read:** P0.7 and the [owner] row now say the owner reads the nine decision rows (the grant row among them) and dTrueNorth's README and packet in full, plus `--check` output and the summary for the other 21.

**3. Self-test waivers** ("Waive in each README", ER:476).
- **Waiver form:** reused from dAlignedCarrier's README (`memory/builds/dAlignedCarrier/README.md:28-30`) as new README rule 8. The waiver line in the README, the close exporting `GATE_FULL=1` but not `GATE_SELFTESTS=1`, and each acceptance ledger noting which suite run went unobserved, as dAlignedCarrier's ledger did. It cites the 2026-08-23 instruction (`MERGE-BAR.md:39-41`, `SESSION-KICKOFF.md:136-138`).
- **Driver-changing set:** derived by a predicate over v2's clauses: any clause naming `unattended.sh`, `check-unattended.sh`, `tools/unattended/`, `/unattended`, "the unattended kit", the verbs `--plan`/`--status`, or run claims. "The driver" alone is excluded because in v2 it means the loop's driver role. dTrueNorth joins through its extra unit. That gives seven:

| Build | Clauses that touch the kit |
|---|---|
| dTrueNorth | extra unit |
| dOrderedCharter | 0047, 0048 |
| dDeclaredLoop | 0106 |
| dPlacedRequest | 0120, 0134 |
| dWitnessedBar | 0344 |
| dWellOiledMachine | 0280, 0281, 0306 |
| dConvergedCharter | 0485, 0486, 0494, 0496 |

- **Also updated:**
  - Phase 1's close step no longer exports `GATE_SELFTESTS=1`. The red-case fixture stays in the kit's suite but runs as a targeted probe.
  - The seven driver rows in [sync-points] carry the waiver.
  - [constraints] now records the standing instruction.
  - The waiver is added to P0.8 row 6.

**4. Governance carrier defined** ("Define it in Phase 0 (Recommended)", ER:525). New P0.8 row 9: a carrier is a tracked path on the list `open.py --carriers` derives from the tree at the opening commit. The selectors, with where the records or the tree bound each:
- the routed product paths (`.memory-tree.conf:9`): 17 kits under `tools/` with a `kit.toml`, plus `tools/govkit`, `tools/lib`, the 40 root-level files under `tools/` (gate scripts and their lists), and `skills/session-kickoff` and `skills/deploy-governance`;
- the 11 files under `.githooks/`;
- `.claude/`: 9 agent files, `roles.json`, 7 skills, `settings.json`, `rules/product.md`;
- the charter template with `AGENTS.md` and `CLAUDE.md`, which `DECISIONS.md:204` calls "the governance carrier";
- the ten guides under `memory/guides/`, bound in earlier build READMEs (aRatifiedRulings, aEvidencedLens, aPrimedKeepalive, aSightedSkeptic);
- seven root confs, including `.unattended.conf`, whose key table `tools/unattended/README.md:336` calls a carrier.

The grant text in P0.5 and row 2 now reads against this list. `--carriers --check` fails on an unlisted path, with a planted red. The [cannot] "defined nowhere" row is now designed around.

Every walk answer, including "Hold" (ER:461) and the hand-off answer (ER:533), is quoted under "Decided by the owner" in [defaults]. The [owner] table now marks the review pair and the walk as done, with "start phase 0 in a new session" as the current step.

## Sweep
I grepped the whole plan for the old wording of each changed rule:
- "TOOL for every unit" and "TOOL for all" survive only inside the quoted answer.
- "every README … every packet" as the owner's read is gone.
- `GATE_FULL=1 GATE_SELFTESTS=1` is gone.
- "driver's test leg" and "defined nowhere … Cannot" are gone.
- "seven decision rows" is gone, and the leftover approval rows are updated to the walk's outcome.

I found two lines past the wrap width and rewrapped them. The only one left is a file path that can't wrap. The bare-id population is still 25 citations in 7 files, none in the plan, and the plan still has one H1.

One thing I checked and judged not to be a conflict: D1 (land through your own new code) names three builds as answered, while README rule 8 covers the derived seven. They are different rules.

## Left open
- **Self-tests outside the seven driver builds.** Every close whose range touches `tools/` is still told by the verbs to export `GATE_SELFTESTS=1`, which runs every kit's self-tests. The waiver as answered covers only the seven driver-changing builds. It's recorded as a question in [defaults] → "Left open by the walk", with my recommendation to put rule 8 in every build that writes under `tools/`.
- **Tables pasted from my scratch probes.** The family, driver-build and carrier results come from probes in the writer's scratch folder; `open.py` doesn't exist yet. Phase 0 must re-derive them with `open.py` and compare.
