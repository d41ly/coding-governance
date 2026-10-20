# Research — the Plan stage: how work enters, is prioritised and assigned today, and the contract it should have

**Serves:** research PLAY-dClosedLoop-1

Returned by `gov-researcher` at its role's effort on handoff
`prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md`, session `1799cb98`, 2026-10-14:
109.1k subagent tokens, 46 tool uses, 318 s. Recorded verbatim below the rule. The main loop's
reading of it lives in the gap register, not here.

---

## 1. Inventory

- **`backlog.py`**: the grammar for asks and dispositions, severity labels (`SEVERITIES` BLOCKER/HIGH/MED/LOW), the status fold, and the READY grader with rules R1–R6. Evidence: `tools/memory-tree/backlog.py:81-84`, `:903`, `:1377-1451`.
- **Per-build `BACKLOG.md`**: where asks are filed (`## Asks`, `## Dispositions`), one writer per file. Evidence: `memory/builds/*/BACKLOG.md`, and `BACKLOG_MODE="builds"` at `.memory-tree.conf:729`.
- **Family views**: generated read-only views of live asks, one per family. Evidence: `memory/backlog/{DEPL,KICK,PLAY,TOOL}.md`; dossier `memory/map/features/memory-tree-backlog.md`.
- **`gen_build_index.py --asks`**: the query, `--ready`, `--probe` and `--json` surface. Evidence: `gen_build_index.py:2737`.
- **`--new-build <slug> --asks <ids>`**: scaffolds a README that the owner lands, with the asks as its mandate. Evidence: `gen_build_index.py:3588-3635`.
- **`check_slug_claimed`**: refuses a slug already used, checking local history only. Evidence: `gen_build_index.py:3478-3503`.
- **Build status**: taken from the specs' headers by precedence, or the typed `status:` front-matter key when no spec exists yet. Evidence: `gen_build_index.py:738-757`.
- **`memory/LIVE.md`**: a generated table of non-terminal builds with dormancy, landed-unclosed and open BLOCKER asks. Evidence: `gen_build_index.py:1766-1807`.
- **`memory/ledger/<YYYY-MM>.md`**: the generated list of builds opened each month. Evidence: `memory/ledger/2026-10.md:1-5`.
- **`memory/DECISIONS.md`**: an append-only index, one line per decision. Evidence: `memory/DECISIONS.md:5-6`.
- **Run claims**: one ref per slug at `refs/gov/runs/<slug>`, written by compare-and-swap. They cover unattended runs only. Evidence: `tools/unattended/unattended.sh:2070-2086`, verdicts at `:2177-2185`.
- **Node registry**: `fleet.toml` plus `--claim-node`. Evidence: `tools/playbook/fleet.toml:1-12`.
- **`/session-kickoff` Step 3**: derives a closed task scope and asks the owner only for gaps. Evidence: `skills/session-kickoff/SKILL.md:126-164`.
- **`manifest-check.sh`**: `--task-skeleton` (eight fields), `--brief-skeleton`, `--card --append` (checks citations and the route). Evidence: dossier `memory/map/features/session-kickoff.md`.
- **Brief record**: the owner's prompt quoted verbatim, plus `## Owner confirmation`. Evidence: `memory/builds/*/prompts/*-brief.md` (472 files).
- **`scratch-guard.js`**: refuses a product write that no routed, buildable unit owns. Evidence: `tools/hooks/scratch-guard.js:74-99`.
- **`UNATTENDED-ASKS.md`**: routes, the mandate properties P5 and P6, the per-ask outcomes (planned, stale, duplicate, not ready), owner-call parking. Evidence: `memory/guides/UNATTENDED-ASKS.md:17-103`.
- **`check-brief-recorded.sh`**: a gate leg, but it covers only units built while a run was live. Evidence: `tools/unattended/check-brief-recorded.sh:10-13`.
- **Memory-hygiene check 9**: the build index must equal a fresh render, and the backlog verdicts V10 (retroactive) and V12 (severity required, forward-only) are enforced through it. Evidence: `tools/memory-tree/check-memory-hygiene.sh:1253`; `backlog.py:1125`; `ASK_CUTOFF=2026-10-01`.
- **drift-audit signals**: `backlog_asks_unlabelled`, `live_builds_without_activity`, `backlog_asks_contested`. Evidence: `tools/drift-audit/drift_report.py:2029`, `:3476`.
- **`workflows.toml`**: stage order starts at `orient` (stage 1). No workflow comes before it. Evidence: `tools/roles/workflows.toml:14-20`.
- **`gov-orienter` role**: the only role that serves this stage. Evidence: `tools/roles/agents/gov-orienter.agent.md`.
- **One-off aged-ask deferral**: TOOL-aMendedFleet-14 and -106 deferred every aged unlabelled ask onto one owner-triage ask. Evidence: `memory/builds/aMendedFleet/BACKLOG.md:7`.

## 2. Flow

**Inputs.** Work enters in one of two ways:
- **An owner prompt (the dominant path).** It becomes a brief and a build README with `authorized-by: prompt`. That covers 62 READMEs; 165 of 167 builds carry no `asks:` line.
- **An ask** filed into some build's `BACKLOG.md` by a run's discovery filing (`UNATTENDED-ASKS.md:105-118`). Only 2 READMEs carry `asks:`.

**Mechanism.**
1. The fold derives each ask's status from sets of rows. ENFORCED: hygiene check 9 requires the index to match a fresh render.
2. Severity labels come from `SEV` rows. ENFORCED only for asks filed on or after 2026-10-01 (V12). Older asks may stay unlabelled.
3. READY grades whether an ask can be run. It is ENFORCED only at `--new-build` and at unattended preflight (`gen_build_index.py:3632`). Otherwise it is advisory.
4. Kickoff Step 3 derives the task fields. The field set is ENFORCED by `check_card_task` at `--card --append`. The fields' content and the scope are STATED only.
5. The route on the card gates product writes. ENFORCED by `scratch-guard.js`.
6. Claims refuse a second unattended driver for the same slug. ENFORCED only when `RUN_CLAIMS=on`, which this repo sets in `.unattended.conf` (the shipped default is off). Attended sessions write no claim.
7. Dormancy and landed-unclosed are rendered for display only. drift-audit reports `live_builds_without_activity` with "report only, no pin".

**Outputs.** A build README with its roster, a brief, the card's `## task` and `## route`, and the ask-to-spec links (`closes` / `advances` in spec headers).

**Hand-offs.**
- In, from Maintain/Review: drift findings and asks filed by runs.
- Out, to Design: the README roster and brief go to spec-write (stage 3 in `workflows.toml`), with the spec audit asked once at kickoff (`SKILL.md:151-158`).
- Out, to Build: the route and the run claim.

**Priority and order.** Nothing produces either. A search for "priorit|roadmap|next build" across `memory/guides/`, `HYGIENE.md`, `README.md`, the template and `AGENTS.md` returned no hits. `--asks` sorts by home and then id.

## 3. The implicit contract today

**Entry criteria.**
- For a build: an owner prompt in chat, or an owner-landed README carrying `asks:` where at least one ask grades better than `no` at READY.
- The slug must be unused in local history. Nothing checks the remote's unmerged branches.

**Exit criteria (Plan to Design).**
- A card whose `## task` has all eight skeleton fields.
- The owner's "go", quoted in the brief.
- A README with a roster, or (unattended) a pinned `asks:` set with each ask ending as planned, stale, duplicate or parked.

**Artifacts.** README front matter (`slug node opened streams roster ids status authorized-by spec-audit`), the brief under `prompts/`, the card in the git common dir, `BACKLOG.md` rows, `DECISIONS.md` lines.

**Who does the work.**
- The owner: intent, the go, triage requests, landing the mandate.
- The main loop or `gov-orienter`: orientation and scope.
- Runs: discovery filing.
- No role triages, ranks or plans across builds.

**Review at this stage.**
- Nothing reviews a plan, a backlog or a priority order.
- Spec-review (stage 4) reviews specs, which belongs to Design.
- drift-audit grades whether records are true, not whether the plan is sound.
- Triage happens only when the owner asks for it (TOOL-aMendedFleet-106).

## 4. Gaps

**HIGH**
- **No priority or order record.** Nothing ranks asks or builds, and nothing records dependencies between builds. Evidence: absent, searched "priorit|roadmap|order:|rank:|after:|depends" in guides, charter and README front matter (0 keys). TOOL-aBoundedVerdict-7 ("nothing records inter-unit dependencies") is DEFERRED.
- **Triage is never drained.** 435 of 521 live asks carry no severity (drift `backlog_asks_unlabelled`), including 133 of 218 OPEN asks. 297 asks are DEFERRED onto TOOL-aMendedFleet-106, which has been open since 2026-10-05. No role or workflow owns triage (`workflows.toml` has none before `orient`).
- **The ask pipeline is not the real intake.** 165 of 167 build READMEs carry no `asks:` line; 62 are `authorized-by: prompt`. A prompt yields a single-build brief, never a cross-build plan.
- **Nothing reviews a plan.** Evidence: absent, searched `REVIEW-PROTOCOL.md` and `workflows.toml` triggers for backlog, plan and priority. The closest, drift-audit, grades whether records are true.
- **Dormant work is never disposed of.** 21 of 25 live builds are dormant (drift, "report only, no pin"); `render_live` only labels them (`gen_build_index.py:1797`).

**MED**
- **Held claims never age.** The `held` verdict ignores age (`unattended.sh:2182`). 8 of 17 claims on the remote are held, the oldest last beat 2026-10-07.
- **Claim `node` is a user name, not the fleet tag.** It is written from `USERNAME` (`unattended.sh:2410`); 17 of 17 claim records carry `daily-agent` or `d41ly`, not `a` or `d`.
- **Attended sessions claim nothing.** Claims exist only for unattended runs (`unattended.sh:2071-2075`). Two nodes can open builds against one ask; READY R2 treats `live_builds=None` as "all builds live" (`backlog.py:1292-1294`).
- **Most OPEN asks are not ready.** 94 of 218 grade `no` and 74 `legacy`; 132 lack an acceptance (R5).
- **The brief is only gated for run-built units.** Attended briefs are STATED only (`check-brief-recorded.sh:29`).

**LOW**
- **Slug uniqueness is checked locally.** `check_slug_claimed` reads local history, not the remote's unmerged branches (`gen_build_index.py:3490-3500`).
- **Collisions are rare but real.** 8 of 859 asks are answered by specs in more than one build; 0 of 859 are contested (drift).

## 5. Candidates

**A. Derive a queue inside the fold.**
- **Mechanism:** order live asks by severity, READY grade, age and holds, and render a "Next" section into `LIVE.md` and `--asks --next`. The owner steers only through `SEV` rows.
- **Seam:** `backlog.derive_statuses` / `derive_ready`, plus `render_live` (`gen_build_index.py:1766`).
- **Losing test:** if more than half the OPEN set ties on the leading key, or if most work never passes through asks, the order is arbitrary or blind.
- **Result:** 133 of 218 OPEN asks (61%) tie on `unlabelled`, and 165 of 167 builds came from prompts, which the queue cannot see. **LOSES** as the Plan contract. It stays useful as an input.

**B. An owner-landed plan record plus a Plan workflow and its Review.**
- **Mechanism:**
  - A dated, owner-committed plan record: an ordered list of builds and asks, each with its entry condition and dependencies.
  - A planner/triager role drafts it from the prompt's brief and the fold's signals.
  - A Plan-Review lens (skeptic) checks the order.
  - A hygiene predicate reds when a non-terminal build, or an OPEN BLOCKER or HIGH ask, is neither placed in the plan nor dispositioned.
- **Seams:** `tools/roles/workflows.toml` (a new workflow before `orient`), `--new-build`'s owner-landed mandate (`gen_build_index.py:3588`), the brief record, and hygiene check 9.
- **Losing test:** the predicate must move on the real tree, not pass trivially and not be unbounded.
- **Result:** 25 live builds plus 40 OPEN BLOCKER/HIGH asks gives 65 items, all unplaced today. The predicate would red on 65 bounded items, so it moves; this is not a rehearsal.
- **Second losing test:** an owner-landed record shape goes unused.
- **Result:** `asks:` is used in 2 of 167 READMEs, which is a warning. But briefs (472) and `authorized-by: prompt` (62) show that the prompt-to-brief path is used. So B survives only if the plan is written from the prompt or brief, not from an ask list.

**C. Generalise claims into a pull queue.**
- **Mechanism:** every kickoff route writes `refs/gov/claims/<slug|ask>` with a heartbeat and expiry. Planning becomes "a node takes the next unclaimed READY ask".
- **Seam:** the compare-and-swap claim in `unattended.sh:2070-2186`.
- **Losing test:** observed contention must justify making claims the Plan mechanism, and existing claims must expire.
- **Result:** 0 of 859 asks contested, and 8 of 859 are multi-build. `held` never expires (8 of 17 held). `node` does not join `fleet.toml` (17 of 17). **LOSES** as the Plan contract: it coordinates who builds but does not prioritise. Its defects go to the Build/Deploy hand-off.

## 6. Pick

I recommend B. It is the only candidate whose losing test moved on the real tree (65 unplaced items), and it closes the four HIGH gaps that are about missing records: priority, triage ownership, prompt intake and Plan Review. It extends existing seams (`workflows.toml`, the owner-landed `--new-build` mandate, the brief, hygiene check 9) rather than adding a parallel store. A's derived signals (severity, READY grade, dormancy) become the planner's inputs and the Plan-Review lens's checklist, not the order itself, because 61% of OPEN asks tie. C's fixes (held claims that never expire, the user name versus fleet tag in `node`, claims for attended sessions) belong to the Build-stage hand-off, not to Plan.
