# Research — the Design stage: how a scoped unit becomes a reviewed design today, and the contract it should have

**Serves:** research PLAY-dClosedLoop-1

Returned by `gov-researcher` at its role's effort on handoff
`prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md`, session `1799cb98`, 2026-10-14:
123.2k subagent tokens, 40 tool uses, 325 s. Recorded verbatim below the rule. The main loop's
reading of it lives in the gap register, not here.

---

## 1. Inventory

- **Spec format** (`memory/TEMPLATE-SPEC.md`). Defines the two tiers, the ten Tier-2 and eight Tier-1 sections, the F-item forks in §8 and the two facts §10 must state. Evidence: :134-162, :290-322, :348-372.
- **Build method M2-M5 and M12** (`memory/guides/BUILD-METHOD.md`). Splits work into units, classifies each MISSING, THIN, FORKED or READY, sets the fork rule and vetoes, the opt-in audit, the probes and research. Evidence: :32-178, :335-363.
- **Workflow table** (`tools/roles/workflows.toml`). Design is three stages: `reuse` 2, `spec-write` 3, `spec-review` 4, plus `research` at 0. Evidence: :22-48, :77-84.
- **`/build` router** (`tools/roles/SKILL.template.md:38-55`). Stage 2 spawns no scout. Stage 4 is the audit the harness runs.
- **Roles.** `gov-spec-writer` writes `spec`. `gov-spec-reviewer`, `gov-skeptic` and `gov-synthesizer` run inside the harness. `gov-researcher` and `gov-reuse-scout` write nothing. Evidence: `tools/roles/agents/*.agent.md`.
- **Build harness** (`tools/workflows/unattended-build.js`). Runs SPEC, then AUDIT and DISPOSAL. Evidence: BUILD-METHOD.md:221-229.
- **Spec lenses** (`tools/workflows/tier2-review.js:741`). Five: coherence, grounding, reuse, blast-radius, failure-envelope.
- **Audit opt-in guard** (`tools/hooks/agent-cap.js:30-33`, rule 0). Refuses an undeclared spec-audit `Workflow` call.
- **Hygiene check 12** (`tools/memory-tree/check-memory-hygiene.sh`, "memory hygiene" leg). Checks spec shape, §10 evidence and the §8 mark at terminal status. Check 21 checks the `**Serves:**` binding.
- **Spec-token joins** (`tools/check-spec-tokens.py`). Seven joins: legs, paths, citations, bar, guards, claims, handoff. They check that names exist and lines are in range, not what they mean (dossier `memory/map/features/spec-tokens.md`).
- **Probes** named in BUILD-METHOD.md:155-170: `reuse_lookup.py`, `memory-recall/query.py`, `gotchas.py --for-paths` and `gen_build_index.py --asks --path`. Also `tools/lexicon/lexicon.py` (the "lexicon naming predicates" leg).
- **Planning verb** (`tools/unattended/unattended.sh:4411-4565`, `plan_state`). Computes MISSING, THIN, FORKED or READY. `--dispatch` refuses MISSING and THIN only (BUILD-METHOD.md:227).
- **Overlap probe** (`unattended.sh:3409`, `check_cross_run_overlap`, `--overlaps`). Advisory; compares against unmerged remote refs.
- **Write gate** (`tools/hooks/scratch-guard.js:796, :870-912`). `checkBuildable` admits product writes only for a routed unit that is Tier-2 at INPROGRESS, or Tier-1 at INPROGRESS or graded SPECCED. A role arm limits writes under `spec/` to roles declaring `writes = spec`.
- **Commit-side legs.** `routed_commits.py` checks that a product commit names a unit whose spec existed. The "pass-order history" leg refuses spec-after-code on CLOSED units.
- **Records.**
  - Spec files: 1,322.
  - Review records with `Serves: spec-audit`: 254.
  - The `research` record kind (HYGIENE.md:575): 7 on disk.
  - Also build README Units tables and `memory/DECISIONS.md`.
- **Codebase map** (`memory/map/features/*.md`, `FOUNDATION.md`). An inventory of 31 dossiers holding 318 claimed keys, with 36 more still unclaimed in `baseline.toml`.

## 2. Flow

**In from Plan.** A READY card, a brief under `prompts/`, the owner's go and the tier kickoff assigns (SKILL.template.md:14-19). ENFORCED: the role arm and agent-cap rule 6 refuse an agent spawn whose prompt is not a rendered handoff.

**Reuse.** The scout runs only if kickoff opted in. Otherwise the writer reads the card's `**Reuse:**` field. STATED only: `enforced-by = "none"` (workflows.toml:27).

**Spec-write.** The harness spawns `gov-spec-writer`. It runs the M5 probes, writes §10 and puts each fork in §8. ENFORCED:
- §10 shape (check 12);
- token joins (spec-tokens leg);
- only spec-role writers may touch `spec/` (scratch-guard role arm).

STATED only:
- one mechanism per spec;
- the four-axis agreement check between sub-specs (M2:66-71). Only the §3 Edges join is checked;
- the M12 candidate search and its recorded losses. No checker reads `Alternatives rejected` (grep over `tools/` finds none);
- that §10 is true (TEMPLATE-SPEC.md:320-322).

**Forks.** The owner decides through `AskUserQuestion`. Under a mandate the agent decides, marked delegated. ENFORCED: §8 is checked only at a terminal status (check 12); `--plan` prints FORKED but refuses nothing.

**Design Review.** Runs only where `spec-audit:` or `SPEC_AUDIT_DEFAULT` is declared. ENFORCED: agent-cap rule 0 refuses an undeclared audit. STATED only:
- folding fixes with a rev bump;
- disposing findings by severity through promotion (M4:141-148).

**Out to Build.** The main loop flips the spec to INPROGRESS itself (SKILL.template.md:59-60) and appends a `## route`. ENFORCED: scratch-guard reads only status and tier (scratch-guard.js:896-903), `--dispatch` refuses MISSING and THIN, and `routed_commits` checks commits. Fork state and review state are read by nothing at this hand-off.

## 3. The implicit contract today

- **Entry:** a READY card, a brief, the owner's go and a unit on the roster.
- **Exit:** a spec that passes check 12 and the token joins, at SPECCED. The owner approves, and the main loop flips it to INPROGRESS. §8 resolution is owed only before CLOSED or WONTDO. Review is owed only where declared.
- **Artifacts:**
  - one spec per unit, with §10 seam and terms, and §8 resolution marks;
  - optional review records under `reviews/` with a `## Verdict` line and a `Serves` line;
  - `DECISIONS.md` rows;
  - rarely, a `research` record.
- **Who:** `gov-spec-writer` writes, inside a harness. The main loop handles forks and the status flip. The owner approves scope and owns the audit opt-in (TOOL-aWardedAudit-4). The scout and researcher are optional.
- **Review:** `tier2-review.js` runs in spec mode, nested in `unattended-build.js`:
  - 3-5 lenses and `REVIEW_ROUNDS` rounds;
  - the verdict is CLEAN, CLEAN WITH FIXES or BLOCKED;
  - fixes fold back as a rev bump plus a §9 line;
  - confirmed findings left at the exit are promoted to new units, not parked.

## 4. Gaps

1. **HIGH: no record holds an architecture above one unit.**
   - The map is an inventory of claims; FOUNDATION.md:29-31 limits itself to shared substrate.
   - 0 of 31 dossiers carry a stage or contract field.
   - Absent: `git grep -il architecture` under `memory/`, excluding `builds/` and `ledger/`, finds only HYGIENE.md, a stream tag in FOUNDATION.md and archive files.
2. **HIGH: design conflicts between builds are invisible.**
   - Measured by probe over the live specs' `### Files touched` paths: 41 pairs of live specs from different builds share a path, across 22 build pairs.
   - 25 of those pairs share a path that is not a shared registry; 21 have an INPROGRESS side.
   - `--overlaps` reads only unmerged remote refs and prints "this run is NOT blocked" (unattended.sh:3409).
   - The coherence lens reads only the specs under review (tier2-review.js:743).
3. **HIGH: Design Review is off by default.**
   - 3 of 173 build READMEs declare `spec-audit:`, and `.unattended.conf:326` has `SPEC_AUDIT_DEFAULT=""`.
   - 503 of 989 Tier-2 specs have no spec-audit record, and neither do 19 of 30 live specs.
   - Of the 254 past audits, 0 were CLEAN: 170 BLOCKED, 58 CLEAN WITH FIXES.
4. **HIGH: the hand-off to Build ignores the design's state.**
   - `checkBuildable` reads only status and tier (scratch-guard.js:896-903).
   - `--plan dNarrowedAnchor` shows TOOL-dNarrowedAnchor-1 at **INPROGRESS and FORKED**, so a route to it would be admitted.
   - INPROGRESS is a value the agent writes itself (scratch-guard.js:89-90).
5. **MED:** Nothing checks that §10 is true (TEMPLATE-SPEC.md:320-322). 142 of 978 Tier-2 §10 sections dated since 2026-08-04 cite neither `reuse_lookup` nor "no existing seam fits".
6. **MED:** M12's rejected candidates are not checked. 95 of 978 Tier-2 specs lack `### Alternatives rejected`, and no checker reads that sub-head.
7. **MED:** The reuse stage is neither enforced nor recorded (workflows.toml:27). `gov-reuse-scout.agent.md` adds nothing of its own.
8. **MED:** Research has no harness and no binding (workflows.toml, `research` workflow has harness "none"). There are 7 research records across 173 builds.
9. **MED:** The four-axis sub-spec agreement check is prose only (BUILD-METHOD.md:66-71).
10. **LOW:** A spec not yet pushed from another node is invisible to the inventory (TEMPLATE-SPEC.md:90).
11. **LOW:** Design is split across workflow stages 2-4 with no single contract (workflows.toml).
12. **LOW:** Nothing checks that the tier assigned matches the change. The tier rules are prose only (TEMPLATE-SPEC.md:380-384).

## 5. Candidates

**C1: refuse the hand-off at Build entry.**
- *Mechanism.* Widen `checkBuildable` and `--dispatch` so a route is admitted only when `plan_state` is READY. For Tier-2, also require a spec-audit record naming the spec at its current rev, unless the build declares the audit not owed.
- *Seam.* `tools/hooks/scratch-guard.js:870`, `tools/unattended/unattended.sh:4411` (`plan_state`).
- *Losing test.* Run the predicate over today's INPROGRESS units. C1 loses if the audit arm selects nothing, or if what the guard reads is written by the agent it guards.
- *Result.*
  - The FORKED arm is live: it catches 1 unit, dNarrowedAnchor-1.
  - The audit arm is vacuous: 0 of 10 INPROGRESS units sit in a build that declares an audit.
  - The guard shares its writer: INPROGRESS is set by the agent, and a review record is hand-writable markdown (handoff.py:78 says the same of the ledger).
  - So the FORKED arm survives and the audit arm loses unless the opt-in default changes.

**C2: a design index across builds plus an architecture record.**
- *Mechanism.*
  - A generated index joins every live spec's `### Files touched` paths with its build and stage, across all builds on the default branch.
  - Spec-write reads it, and a leg reds an overlap that neither spec acknowledges in its §3 Edges.
  - An authored architecture record states each stage's contract, and every dossier declares the stage it serves.
- *Seam.* `read_files_touched` and `check_cross_run_overlap` (`unattended.sh:3389`, `:3409`), `gen_build_index.py --asks --path`, the dossier TOML (`memory/map/features/*.md`).
- *Losing test.* (a) The signal on merged live specs is empty or only shared-registry noise. (b) The map cannot host it because most of the tree is unowned.
- *Result.* (a) 41 pairs, of which 25 are on paths that are not registries; today's probe sees none of them. (b) 318 keys claimed against 36 unclaimed, so about 90% covered. Survives.

**C3: review-side, audit owed by default plus a cross-build lens.**
- *Mechanism.* Make the audit owed unless waived, and add a sixth spec lens that reads other builds' live specs.
- *Seam.* `tools/workflows/tier2-review.js:741`, agent-cap rule 0 (`agent-cap.js:1848`), `.unattended.conf:326`.
- *Losing test.* (a) Past audits are mostly CLEAN, which would make the audit a rehearsal. (b) The lens would re-derive a join a deterministic checker can compute.
- *Result.*
  - (a) does not reject it: 0 of 254 audits were CLEAN.
  - (b) rejects the lens: C2 computes the overlap deterministically, and the spec-tokens dossier names "paying a reviewer to do what a checker does" as the defect.
  - What survives is the default-on flip. It costs about 9 agents and 0.81 M tokens per spec (REVIEW-PROTOCOL.md:23-28), and it changes a governance carrier, so it is an owner decision (M3 veto 2; TOOL-aWardedAudit-4).

## 6. Pick

C2. Gaps 1 and 2 are the two that exist because development here is concurrent and multi-node, and only C2 makes them visible. It does so with a deterministic join over records that already exist, extending a probe the kickoff card already calls. C1's FORKED arm survived its test, catches a live unit today and is a one-predicate addition, so the Build stage's entry contract should adopt it (a hand-off to the Build researcher). The audit-default flip in C3 also survived its test (0 of 254 audits clean), but it changes a governance carrier and belongs to the owner. C1's audit arm and C3's cross-build lens each lost their tests and should not be built.
