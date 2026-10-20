# Research — the Deploy stage in its three senses: landing, distributing gov, releasing an adopter's product

**Serves:** research PLAY-dClosedLoop-1

Returned by `gov-researcher` at its role's effort on handoff
`prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-5-researcher.md`, session `1799cb98`, 2026-10-14:
82.9k subagent tokens, 36 tool uses, 249 s. Recorded verbatim below the rule. The main loop's
reading of it lives in the gap register, not here.

---

## 1. Inventory

- **`tools/push-main.sh`**: the lander. It has an attended mode and `--prepare/--land/--carry` modes. It mints kit versions, regenerates outputs and starts the post-merge bar (push-main.sh:14-47, :427). It writes the lander marker only when the hook leaves an allow record (:342-354).
- **`.githooks/pre-push`**: the bar at the push boundary. It refuses a raw default-branch push (:1219-1222) and decides full, scoped or covered. It reads `GATE_POST_MERGE` at R (:1621) and lets `refs/gov/bar-red` force a full bar (:1908-2057).
- **`.githooks/gate-env.sh`**: repository policy read at R, such as the branch bar `GOV_BRANCH_GATE_CMD` (gate-env.sh:66).
- **`tools/run-gates/post-merge.sh`**: a detached full bar after a landing. It publishes `refs/gov/bar-red`.
- **`tools/run-gates/run-gates.sh` and `tools/gate-legs.json`**: the merge bar. Its legs include the epoch, receipt-sync, govkit and push-main self-tests.
- **`.github/workflows/remote-ci.yml`**: gov-only CI. It runs the full bar on every push to main and states that it "blocks nothing" (:10-12). It has `permissions: contents: read`.
- **Charter practices** (template:28-31): `[small]`, `[isolate]`, `[land]`, `[post-merge]`, plus `[bar]` and `[contract]`. The micro-formats `merged`, `pushed` and `up` are at template:55-64.
- **`tools/unattended/`**: `unattended.sh --landed` accepts only a lander marker. The definition of done includes `closing-review-recorded` (PROTOCOL.template.md:352).
- **`tools/govkit/govkit.py`**: the deployer. Its verbs are selfcheck, intake, plan, apply, check, update, adopt, epoch, mint and contribute (USAGE at :13212, dispatch at :13713).
- **Kit population**: `tools/govkit/registry.toml`, 12 entry descriptors in `tools/govkit/entries/*.kit.toml`, and 17 `tools/*/kit.toml`.
- **13 `tools/*/adopt-*.sh` scripts**: each kit's configure step, which `apply` runs.
- **Receipts**: `.governance/install.json` at schema 3 plus `install.sums`. They are graded in an adopter by `tools/run-gates/check-receipt.py`, which checks integrity only (:1-20).
- **`skills/deploy-governance/SKILL.md`**: the operator order. It runs selfcheck, then intake, plan, apply, check and update, and it does not commit or push.
- **Charter rendering**: `tools/playbook/render_playbook.py` and `adopt-playbook.sh` render the charter from `.governance/deploy.toml`.
- **`tools/agent-instructions/`**: makes `AGENTS.md` canonical and adds the per-tool shims (README.md:1-5).
- **`WIRE-INTO-PROJECT.md`** (162,896 bytes): a narrative runbook covering §5b adopt, §5c contribute and Maintenance/outbox (:1376). `check_runbook_parity.py` only checks that sections exist.
- **`tools/govkit/census.py` and `adopters.toml`**: gov-internal. The first is the fork census; the second is a brand-name ban, not a fleet register.
- **`memory/builds/aDeployScout/spec/governance-deployer-research.md`**: the design origin. Its "governance-check riding target CI" was never built.
- **Roles**: `tools/roles/workflows.toml` has 10 workflows and none of them is a lander, release or deploy role.

## 2. Flow

**Hand-off in from Test.** A unit branch arrives with a green bar record.

**Landing (sense a).**
1. Either the owner asks, or the unattended protocol authorizes the landing. **STATED** only (`[land]`).
2. `push-main.sh --prepare` merges onto the tip the remote advertises, then runs `govkit mint` and `regen.py --write`.
3. `--land` pushes, and pre-push runs the bar.
   - **ENFORCED:** a raw push is refused (pre-push:1222).
   - **ENFORCED:** a red bar is refused through `write_refusal gate-red` (pre-push:2378).
   - **ENFORCED:** a commit from another build is refused through `--carry`.
   - **ENFORCED:** a push without an allow record exits 4 as UNGATED (push-main.sh:350).
4. After the push, `run_post_merge` starts the post-merge bar only if R declares `GATE_POST_MERGE`.
5. A red there publishes `refs/gov/bar-red`, which forces a full bar on the next push. **ENFORCED only where declared.**
6. Remote CI re-runs the bar after the landing. Its result is **informational**: it cannot write a ref and blocks nothing.
7. Unattended runs end at `--landed`, which reads the lander marker. **ENFORCED.**

**Kit distribution (sense b).**
1. Gov lands a kit change, and the lander mints the version. **ENFORCED** by the epoch leg.
2. An operator runs `govkit` against a target: intake, then plan, then apply. Apply stages the files, writes the receipt and runs the adopters.
3. The operator commits and lands it in that target with the target's own lander. **STATED** (SKILL.md: "your job").
4. `update` is pull-only and read-only by default. Withdrawals and rollbacks become orders under `.governance/outbox/`.
5. The adopter's bar runs the receipt-sync leg, which checks integrity but not currency.

**Product release (sense c).** Nothing in gov handles it. The `up —` line and "own ports and databases" under `[isolate]` are prose.

**Hand-offs out to Maintain:** outbox orders, the post-merge red, receipt drift, and `contribute` patches coming back to gov.

## 3. The implicit contract today

- **Entry criteria:**
  - a green branch bar;
  - for unattended runs, a built and reviewed unit;
  - an explicit owner ask or the unattended mandate;
  - a clean tree and the default branch's prepared merge.
- **Exit criteria:**
  - a pushed `--no-ff` merge whose pushed SHA the pre-push allow record names;
  - a lander marker;
  - `pushed`/`merged` micro-format lines;
  - where declared, a post-merge bar started. Nothing waits for it to finish (push-main.sh:46-47).
- **Exit for sense b:** a staged install, a receipt, and a `check` with every hole discharged. Committing it in the target is the operator's job.
- **Exit for sense c:** none.
- **Artifacts:**
  - landing: the lander marker, the pre-push verdict files, `pushes.log`, mint and regen commits, `refs/gov/runs/*`, and the CI run record;
  - deployment: `deploy.toml`, `install.json`, `install.sums` and `outbox/*.md`.
- **Who does the work:** the owner or the unattended session runs the lander. An agent or the owner runs govkit through the skill. No role agent owns landing or releasing.
- **Review at this stage:**
  - The bar is the only gate on an attended landing.
  - An unattended landing additionally needs `closing-review-recorded`, which is machine-checked for existence, not content.
  - A kit release is minted automatically. There is no changelog (0 tracked files) and no release review. The last 300 commits on main include 4 mint commits.
  - An adopter's update is reviewed only by `update`'s self-check, which rolls back a touched kit whose `[check]` goes red, plus whoever reads the staged diff.

## 4. Gaps

- **HIGH** — Sense c, an adopter's own release, environments, rollout, rollback and post-deploy verification, is not addressed.
  - Absent: rollback|rollout|staging|canary|smoke in the template, tools, skills and `.githooks` (only govkit's own update rollback matches).
  - Adopter "ic" built `release.yml`, `sign-release.yml`, `restore-drill.yml` and `infra/deploy.sh` entirely outside gov.
- **HIGH** — The post-landing verdict is inert.
  - `GATE_POST_MERGE` is declared in 0 of 3 trees (gov, ic, nc).
  - `refs/gov/bar-red` is absent on gov's remote.
  - Remote CI cannot publish a verdict (remote-ci.yml:10-12, `contents: read`).
- **HIGH** — No CI job is emitted into adopters.
  - The govkit dossier says "nothing writes a CI job into a target", and only `github-actions` is accepted (govkit.py:5746).
  - Ic's 6 workflows contain 0 references to run-gates.
- **HIGH** — Nobody watches whether adopters are current.
  - The most common gov commit in the ic and nc receipts is `c83ef509`, which is 990 commits behind origin/main after 6 days.
  - nc's receipt spans 75 distinct gov commits.
  - `update` is pull-only, and `adopters.toml` is a brand ban, not a fleet register.
- **MED** — Outbox orders are not graded by anything. nc holds 16, including 5 `update-rollback-*` orders.
- **MED** — The Deploy stage has no review.
  - No landing or release role exists (workflows.toml lists 10 workflows).
  - There is no kit release note or changelog.
  - An attended landing has no review gate.
- **MED** — On Git for Windows, a KILL or TerminateProcess of the hook still lands an ungated push. The lander only reports it afterwards (push-main dossier Gaps; push-main.sh:350).
- **MED** — Hooks-path drift is only reported as a note (pre-push:19-20; check-wiring check H).
- **MED** — The push-main kit has no version (`push-main.kit.toml:7`) and `requires = []` (:8), yet `run_post_merge` needs the run-gates kit's `post-merge.sh` (push-main.sh:445).
- **MED** — The research's failure-policy keys (`on_diverged_remote`, `on_preexisting_red`) are absent. They have 0 hits in govkit.py.
- **LOW** — The runbook is 162,896 bytes of narrative, and its parity gate checks only that sections exist.
- **LOW** — The record and the code disagree on `contribute`: it is dispatched (govkit.py:13713) but missing from USAGE (:13212-13223).
- **LOW** — `[isolate]` ports and databases and the `up —` line have no allocator and no checker. It is stated only.

## 5. Candidates

**A. A post-landing chain the lander runs.**
- **Mechanism:** generalize `run_post_merge` into a chain the gate-env file declares at R: post-merge bar, then the adopter's deploy command, then its verify command. Each step publishes a per-SHA `refs/gov/<step>-red`, and pre-push already binds that ref to the next landing.
- **Seam it extends:** `tools/push-main.sh:427`, `.githooks/pre-push:1621` and `:1908`, `tools/run-gates/post-merge.sh`.
- **Test that would make it lose:** the seam must be live in at least one real tree, and its finish must have a witness that does not depend on the landing node.
- **Result: LOSES.** 0 of 3 trees declare `GATE_POST_MERGE`, and `refs/gov/bar-red` is absent on gov's remote. The lander says it "does NOT check whether that bar ever finished" (push-main.sh:46-47). The chain is a detached process on one node that may sleep. Both adopters do carry push-main and run-gates, so the code is shipped but has never run outside fixtures.

**B. A Deploy stage owned by CI, with the jobs emitted by govkit.**
- **Mechanism:**
  1. Build the `[gate_runner.ci]` emitter. Each adopter then receives a gov-owned job: the full bar on a default-branch push, plus a scheduled job for receipt sync and a currency probe against `gov_source`.
  2. Add a descriptor slot through which an adopter declares its own release, deploy and verify workflows as rows.
  3. CI publishes a per-SHA verdict that pre-push's existing `read_post_merge_red` binds.
- **Seam it extends:** the validator at `tools/govkit/govkit.py:5746`, the `write_gate_legs` emitter, `.github/workflows/remote-ci.yml` as gov's own instance, and pre-push's post-merge red read.
- **Tests that would make it lose:**
  1. A receipted adopter uses a CI system gov cannot emit.
  2. The CI job cannot publish a verdict that the push decision reads.
  3. Adopters already run gov's bar in CI, so B would only duplicate it.
- **Results:**
  1. Passes: 2 of 2 receipted adopters use `.github/workflows` (ic has 6, nc has 1).
  2. **Fails as wired today**: `permissions: contents: read`, and remote-ci.yml:10-12 says it blocks nothing. It is closable by an owner-granted `contents: write` scoped to `refs/gov/*`, or by having pre-push read a commit status instead.
  3. Passes: ic has 0 run-gates references in 6 workflows.

**C. A record-driven contract.**
- **Mechanism:** add `released —` and `deployed — <env> · <sha> · verify <…>` micro-formats, and a deploy record under `memory/builds/` that memory hygiene grades.
- **Seam it extends:** the micro-format block (template:55-68), `tools/check-microformats.sh`, and the memory-tree hygiene engine.
- **Test that would make it lose:** a gate must re-derive the record's claim from a witness other than the agent's own text.
- **Result: LOSES.** `check-microformats.sh:18-20` grades the definitions only. No non-markdown file under tools, skills or `.githooks` checks an emitted `up —` line (the grep hits are em-dash prose). The record would assert, and the guard would share state with what it guards (`[class]`).

## 6. Pick

I recommend B, reusing A's binding (`refs/gov/*-red` read by pre-push) as the reader, so a CI verdict forces a full bar on the next landing. B is the only candidate whose witness runs off the landing node and that every receipted adopter can host today; A and C each failed their losing test outright. It closes all four HIGH gaps through one emitter that govkit already validates. The adopter keeps its own release workflows, and gov grades only that they are declared and that their verify step reported per SHA. B still fails part of its own test until you choose between a scoped `contents: write` grant and a commit-status read in pre-push, so that decision belongs in the chain build's first unit.
