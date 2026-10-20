# Research: fully oriented handoffs, for the chain's execution

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 216's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-53-researcher.md`.

---

**Fully oriented handoffs: what orients a session today, how work moves between sessions and nodes, and the handoff the owner's plan needs**

I wrote nothing in the repository. My probes ran read-only from the worktree root, with bytecode writing off, and their scripts sit in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/exec/d216/` (`packet_probe.py`, `packet_probe2.py`, `sched_probe.py`, `foreign_carry.py`). While I worked, `git status` showed `session-log.md`, `README.md` and a staged `...-execution.md` change. Those are the parent session's writes, not mine.

## 1. Facts the answer rests on

**What orients a session today**
- **The card.** A SessionStart hook runs `manifest-check.sh --card --write` (`skills/session-kickoff/orientation-card.fragment.json:3-8`). The card lives at `<git-common-dir>/orientation/<sid>.md` and is keyed by session id (`skills/session-kickoff/manifest-check.sh:32`, `:311-316`). It is never pushed. This session's card holds the cells for node, tree, base, worktrees, drift, overlaps, live builds, claims and recent commits (`.git/orientation/1799cb98-….md:1-30`).
- **Kickoff.**
  - Step 1 consumes the card but never its branch or BASE (`skills/session-kickoff/SKILL.md:54-56`).
  - Step 3 fills the eight sealed task fields from `--task-skeleton` (`SKILL.md:134-142`; `manifest-check.sh:82-94`). A product-code task also gets a brief (`SKILL.md:164`).
  - Step 5 appends the READY card through `--card --append` and stops for "go" (`SKILL.md:195-210`). The READY shape is `READY — <slug> · node <tag> · <branch> · base <sha> · Tier-<n> · gates <list>` (`AGENTS.md:62`).
  - Step 5b continues without halting only inside a live run-state file (`SKILL.md:212-227`).
- **The closed scope is the route.** `## route` names the build, each unit with its spec, and the brief, and every one must resolve (`manifest-check.sh:162-166`, `:994-1059`).
  - Each spec must be tracked under `<build>/spec/` with the unit id as its H1 (`:1034-1045`), so no route can exist before a spec does.
  - The write gate refuses product writes when no route exists (`tools/hooks/scratch-guard.js:74-80`). This session's SubagentStart context said exactly that.
- **`gov-session`.** It is `agent: false` and reads `input:question, brief:goal?, task:todo?, card:route?` (`tools/roles/agents/gov-session.agent.md:5,11`). Its body tells the receiver to run its own kickoff and re-verify the sender's records (`:14-23`). The workflow is `handoff`, enforced by "none" (`tools/roles/workflows.toml:91-96`).
- **`handoff.py render`.**
  - It writes `<date>-prompt-<unit>-<n>-<role>.md` under the build's `prompts/` (`tools/roles/handoff.py:297-304`, `:417-418`). `--out` is refused outside that folder (`:1029-1033`).
  - The marker carries role-sha and task-sha, and `check` only re-hashes the file's own bytes (`:29-31`, `:426-450`). It does not check content truth or role currency (`:71-73`).
  - Free inputs are limited to `spec, diff, question, prompt` (`:98`, `:970-972`).
  - `brief:*` keys come from the one `prompts/` file holding both `## The prompt` and `## The brief`. Two such files refuse unless `--input prompt=` names one (`:283-294`).
  - It refuses when the build folder is absent (`:317-319`).
- **The build method.**
  - The roster is the README's authored Units table; `ids:` is derived (`memory/guides/BUILD-METHOD.md:39-42`).
  - Never build a MISSING or THIN unit (`:61`). There are exactly five pass kinds (`:182-183`).
  - Parallel passes need recorded disjoint write sets (`:209-216`). The harness buys order, not enforcement (`:221-229`).
  - The reground reads `--status`, RUN.md, the method, and the current spec (`:240-245`).
- **The brief rows and the run-state file.**
  - `--brief` records the unit and a tracked brief file's hash as a history row in RUN.md (`memory/guides/UNATTENDED-VERBS.md:47-48`, `:697-699`; row shape at `tools/unattended/lib-unattended.sh:838`). An example: `brief · item TOOL-aBatchedArm-4 · reason b56f676efee7 <path>` in `memory/builds/aBatchedArm/RUN.md`.
  - RUN.md holds the phase, lease, BASE, host, session and parked entries, BRIEF and HANDOFF among them (`memory/guides/UNATTENDED-PROTOCOL.md:141`, `:174-182`, `:206-235`).
  - The build harness takes a per-unit `briefPath` and `specBriefPath` (`tools/workflows/unattended-build.js:169-178`).
- **Between nodes.**
  - Only git carries anything. Run claims live at `refs/gov/runs/<slug>` (`memory/guides/UNATTENDED-STOPS.md:187-199`), and `RUN_CLAIMS="on"` (`.unattended.conf:162`).
  - A foreign live claim refuses a second driver with check 107 (`tools/unattended/unattended.sh:2294`). The resume tick skips leases held on other hosts (`tools/unattended/resume-tick.sh:281-285`).
  - `ANCHOR_SCOPE="local"` (`.unattended.conf:267`) lets a README committed at HEAD authorize a run, and refuses `spec-audit:` in a `slug` or `recipe` README (`UNATTENDED-PROTOCOL.md:87-91`).
- **The chain and its pins.**
  - v2 `[chain]` holds the 22 rows (`architecture-v2.md:1760-1785`).
  - The hash rule is in `[clause-ids]`, and the baseline is `59ff8f2ac` (`:1794-1811`).
  - Some checks owed to specific builds sit outside `[chain]`, in `[owed]` (`:1955-2037`).
  - The bootstrap list is in `final-questions.md:274-303`.
  - `parents:` is authored README front matter, and children are derived from it (`tools/memory-tree/gen_build_index.py:1570-1588`, `:2335-2345`).
  - The existing cross-spec `hands-off` join works only inside one build (`tools/check-spec-tokens.py:101-104`).
  - No file under `tools/`, `skills/` or `.githooks/` reads a `cl-` id or `**Carries:**` line (grep returned nothing).

**Gap rows this facet touches**
- gap-orient-11: cards are keyed by session and absent from the remote (`gap-register.md:142`).
- gap-orient-07: briefs carry pointers, not facts (`:138`).
- gap-roles-11: work orders hand references, not content (`:163`).
- gap-roles-23: most handoffs carry no typed marker (`:175`).
- gap-roles-27: commitments do not cross an edge as rows the receiver must answer (`:179`).
- gap-conc-16: no node can find work it does not hold (`:337`).

**Disagreements between records and code**
- `handoff.py` strips a leading `(…)` qualifier from a task value (`handoff.py:198-204`). That drops the `(1)` of a numbered To-do: the card reads `(1) research…` (card line 32), and the render reads `research…`.
- `carries.py` checks only that a carried id exists. It never checks that the clause belongs to the spec's own build (`carries.py:198-204`).

## 2. Candidates, their losing tests and the results

**A. A hand-typed brief record for each chain build.** This is today's design-build pattern: `*-handoff-brief.md` rendered through `handoff.py render --input prompt=`.
- It loses if nothing can check its completeness.
- Result: **it loses as the carrier of clauses and hashes.**
  - `check` hashes only the file's own bytes (`handoff.py:71-73`), and no product tool reads `cl-` ids.
  - A dropped clause or a stale hash would pass every check.
  - It survives only as the carrier of the owner's prose (the prompt and the non-goals).

**B. A packet generated for each chain build.** A script derives it from v2 at the baseline, the as-built view, the gap register, `map.py`, and v2's `[policies]` and `[owed]` sections. It is written as a brief-shaped record in the chain build's `prompts/` and checked by re-rendering it and comparing bytes, as `asbuilt.py --check` does.
- It loses if any field cannot be derived for some build.
- Results:
  - **Clauses:** all 509 derive, and baseline equals HEAD for every hash.
  - **Gaps:** 386 of 386 resolve, including ranges such as "gap-review-04 to gap-review-10". Each is owned exactly once, and none is unowned.
  - **Parents, children and owned nodes:** all derive.
  - **Policy keys:** 267 carry a chain-build owner.
  - **Stand-ins only partly derive.** Of 74 mentions of a later build, 42 match a stand-in pattern. The other 32 are interface hooks such as "once dKeptSession adds presets" (`cl-0009`), so this field must list each mention verbatim rather than classify it.
  - **Lines outside `[chain]` are needed.** A packet built from clauses alone misses `[owed]` items: dTotalRecall is named 11 times there and dOrderedCharter 3 times, so those lines must be excerpted too.
  - The largest clause body is dWellOiledMachine's at 36 KB, which is acceptable in a prompt.
- **B survives.**

**C. Handoffs per pass only.** Today's `--brief` rows and harness briefs, plus `gov-session` prompts, with no build-level packet.
- It loses if a cold session cannot be oriented to a chain build through it.
- Results:
  - `handoff.py render --role gov-session --build dTrueNorth` exits 1 because the build folder does not exist.
  - Rendered under dClosedLoop instead, the task block carries dClosedLoop's `brief:goal` and `task:todo`, taken from the sender's brief and card. The receiver is handed the wrong scope.
  - `--input clauses=` is refused, because inputs are closed to four names.
- **C loses as the orientation carrier. It survives as the work order for each pass.** Passes are needed anyway: in a 3-node build-level schedule, only one build is available for the first 30 units and again from 48 to 101, and 14 of 21 events have fewer than 3 builds available. So passes of one build must move between nodes.

**D. One handoff per node.**
- It loses if no reader keys by node, or if a node's packet sits empty.
- Results:
  - Claims, run state, the as-built view and the coverage report are keyed by slug. Cards are keyed by session.
  - The same schedule leaves two nodes with nothing for most of the first 131 units.
- **D is rejected.** Node assignment is a claim, which is the coordination researcher's question.

## 3. Recommendation: one packet per chain build, plus a brief per pass that cites it

**The build packet** is generated, never typed. It is written as `memory/builds/<slug>/prompts/<date>-prompt-<first id>-packet.md`, using the brief skeleton's headings so `handoff.py --input prompt=` can read `brief:*` from it. It is committed and pushed together with the README in the commit that opens the build. It holds:
1. **Pins:** the baseline sha, the paths and blobs of v2 and the as-built view, the HEAD it was rendered at, and the generator's version.
2. **Clauses:** each `id@hash8` at the baseline, its as-built hash now and the deviation record behind any change, the full text, its tokens, and a flag on clauses the token arm cannot see.
3. **Owned nodes.**
4. **Parents:** each parent's status and landed sha, the parent clauses this build's clauses name, and any deviation records on parent clauses since the baseline.
5. **Children:** the builds that wait on this one.
6. **Gaps:** each key with its severity, summary and register line.
7. **Policies:** the keys it owns, and the keys it reads that a later build owns.
8. **Later builds named:** each mention with its clause id and excerpt, stand-in matches flagged.
9. **Obligations outside `[chain]`:** the `[owed]`, `[open]`, `[enforcement]` and `[policies]` lines naming the build.
10. **Must not touch:** every other build's clauses (carrying one needs a `**Moved:**` decision), the frozen v2 (a change is a deviation record), and anything outside its routed units.
11. **The coverage report:** the output of `carries.py --report <slug>`.
12. **The reading order** for a cold session: README and Units table, the packet, the method, the current spec.

**Checked complete** by:
- a `--check` that re-renders the packet and compares bytes, with completeness arms (every clause and hash, every gap, every parent) each seen red on a planted omission;
- `handoff.py check` on each rendered prompt.

**Kept current:**
- Each pass brief cites `packet@blob`.
- At every M7 reground the session runs `--check`.
- The packet goes stale when a deviation record lands in the build's or an ancestor's `build/` folder, when a parent's status or landed sha moves, or when the gap register changes. It is then re-rendered and committed before the next pass.

**The pass brief** is today's mechanism: `handoff.py render --build <chain build> --unit <id> --input prompt=<packet>`, recorded with `--brief`. It adds the unit's carried clauses and its write set.

**Moving work to another node** means pushing the folder (README, roster, packet). The receiving node then starts `/unattended <slug>`, or runs an attended kickoff with a `gov-session` prompt rendered under the chain build, never under dClosedLoop.

## 4. Worked example: dTrueNorth's packet

- **Pins:** baseline `59ff8f2ac04a967751eae00de6856afbea66c033`; deviation records: 0 (`asbuilt.py --check` reports findings 0, and `deviations.py` finds 0 members).
- **Clauses (hash8 at the baseline):**
  - `cl-0001@83b6b117`: clause ids and `**Carries:**` lines (522 B).
  - `cl-0002@6acd9ea9`: the carries join, which the token arm cannot see (451 B).
  - `cl-0003@d2811290`: the coverage report and the hygiene refusal (590 B).
  - `cl-0004@c374ccd0`: the deviation record and its join (1175 B).
  - `cl-0005@5417efbc`: audits pinning `@rev-N` (249 B).
  - `cl-0006@06ceb3cc`: the as-built view (527 B).
- **Owned node:** `record-kind.deviation`.
- **Parent:** dClosedLoop. It provides v2, the baseline, and the bootstrap instruments (`clause-ids.py`, `carries.py`, `deviations.py`, `asbuilt.py`) that this build turns into product (`final-questions.md:281-289`).
- **Child:** dGroundRules.
- **Gaps:**
  - gap-design-13, HIGH (`gap-register.md:361`)
  - gap-build-07, HIGH (`:368`)
  - gap-mem-47, MED (`:230`)
- **Policies:** it owns none. `.governance/policy.toml` is dGroundRules's (`cl-0007`), so dTrueNorth must use a conf cutoff, as `SPEC_HANDOFF_CUTOFF` does.
- **Later builds named, all stand-ins:**
  - `cl-0004`: a stand-in until dOrderedCharter's classifier and dDeclaredLoop's `deviation.approval` land.
  - `cl-0006`: a stand-in until dOrderedCharter's overlay grammar lands.
- **Seams to extend:**
  - `cl-0002`: the spec-tokens handoff join (`tools/check-spec-tokens.py:101-115`).
  - `cl-0004`: `tools/memory-tree/routed_commits.py`.
  - `cl-0003`: `tools/memory-tree/check-memory-hygiene.sh`, including check 21's kinds.
- **Coverage now:** all 6 clauses are uncarried, and the owned node is unnamed. That is expected before its specs exist.
- **Must not touch:** v2, the policy file, the classifier and overlay grammar (stand-ins only), and every clause from `cl-0007` onward.

## 5. What today's gov cannot do, and the smallest change for each

1. **The card is per node and never reaches the remote** (gap-orient-11). *Manual step:* the packet travels in git, committed and pushed with the README before any other node starts.
2. **No tool renders or checks the packet's content** (`handoff.py:71-73`, and no product tool reads `cl-` ids). *Smallest change:* a bootstrap instrument in dClosedLoop's `build/` folder, as `carries.py` is. It would be a record, not product code. A chain build absorbs it later, likely dFurnishedOrders, the build that owns work-order content.
3. **`handoff.py` refuses an unopened build, and a `gov-session` prompt rendered under dClosedLoop carries dClosedLoop's goal and to-do.** *Policy:* render only under the chain build once its folder has landed, with `--input prompt=<packet>`. Note that `gov-session` reads only `brief:goal`, so a cold attended pickup still reads the packet by path.
4. **A spec may carry another build's clause unrefused, and that clause then counts as carried for its owner** (`carries.py:198-204`; the `foreign_carry.py` plant produced no finding). *Smallest change:* an instrument fix in `carries.py` now, or a stricter arm on `cl-0002` recorded as a deviation (approved by the spec writer).
5. **A parent's promises to its children are joined only inside one build** (`check-spec-tokens.py:101-104`). *Manual step:* the packet lists each parent's promises, and the receiver verifies them at its own Design exit.
6. **No rule says when a branch reaches the remote**, and only one driver can hold a slug (`unattended.sh:2294`). *Policy:* push after every pass commit. A pass on another node of a slug a run holds is an attended session on its own branch (the coordination researcher's question).
7. **The local anchor refuses `spec-audit:` in a `slug` or `recipe` README** (`UNATTENDED-PROTOCOL.md:87-91`). *Policy:* a chain build that wants its audit opens with `authorized-by: prompt`, and its prompt record must quote the owner asking for the audit.
8. **`handoff.py` drops the `(1)` from a numbered To-do** (`handoff.py:198-204`). *Smallest change:* a fix in the roles kit, assigned to a chain build's unit.
