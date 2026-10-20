# Research: flow and roles adoption, today's product measured

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 123's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-5-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md`.

---

**Research: how an adopter adds to or changes gov's flow and roles today, and what the next update does to each change**

**The answer in brief.** Today an adopter can add flow items in only a few places, and can change gov's flow almost nowhere without editing gov's own files.
- **Adding beside gov's works** in three places:
  - **Gate legs:** rows the adopter adds to the shared gate-leg manifest.
  - **Unattended run:** the `*_EXTRA` vocabulary keys in `.unattended.conf`.
  - **Roles:** a role file the adopter drops next to gov's (`tools/roles/agents/*.agent.md`) and its house overlay. These survive an update and render.
- **Two things are measured below for the first time:**
  - **Adopter roles and workflows:** nothing registers or checks one. The checker's tables of role ceilings and workflow names are typed into gov's code, so registering a role means editing gov's files. On my fixture that edit conflicted and the whole roles kit was held back.
  - **Overrides of gov's gate legs:** only a leg's `ceiling` override survives. An edited argument list stopped every gate leg from being written. A deleted gov leg came back, and no output line said so.

**How I measured.** I cloned gov at `320c79646` under the session scratchpad (system temp root) and installed into an empty target with `intake --all` and `apply --all`. To get the four failed adopters through I ran them by hand, after supplying the asked answers, `ci_file` and `.unattended.conf`. Gov's later changes were synthetic commits made in the clone:
- **v2 `6cfb0448e`:** a `workflows.toml` trigger, a `tier2-review.template.js` line, the `policy.toml` seed, a `gate-profiles.txt` row, a `check_roles.py` ceiling, two leg ceilings and one new leg.
- **v3 `d4e862b37`:** the roles README.
- **v4:** the stop-guard fragment.

I then ran `govkit update` (read-only) and `update --write`. The fixture is deleted, and `git status` shows no file of mine.

**One limit:** the scratch-guard refuses gate legs to my role, as it did for the sibling pass. Every leg verdict below is therefore read from the code, and marked "read".

## 1. Population, and the command that derived it

```
python3 tools/govkit/govkit.py plan --target <fixture> --all
  | grep -E "<- (roles|review-harness|unattended|run-gates|agent-cap|kickoff-manifest|playbook|playbook-render|settings-merge)$"
  | grep -v -E "\[(attributes|project-owned)" | grep -v -E "README|\.test\.|fixture|selftest"
```
Plan total: `252 write(s), 129 order(s), 19 side-effect(s), 2 covered, 3 blocked, 0 forked`.

`plan` prints no row for `[[generated]]`, `[config]` or `[gate_runner_seed]`. I added those with a `tomllib` walk over each flow kit's `kit.toml` and `tools/govkit/entries/*.toml`, which printed `rendered`, `seed`, `generated`, `config`, `runner` and `gate_legs` counts per kit.

| Area | Members (installed path, role) |
|---|---|
| Role definitions | `tools/roles/agents/gov-*.agent.md` ×10 (engine); `tools/roles/house/gov-*.md` ×10 and `policy.toml` (seed); `tools/roles/workflows.toml` (engine); `check_roles.py`, `roles_lib.py`, `render_agents.py`, `handoff.py` (engine); `.claude/agents/*.md` and `.claude/roles.json` (generated); `.claude/skills/build/SKILL.md` (rendered) |
| Review harnesses | `tools/review-harness/{tier2-review,unattended-build,drift-audit-code,drift-audit-state}.template.js` (engine) → `.js` (rendered); `unattended-unit.js`, `orient.agent.md` (engine); `memory/guides/REVIEW-PROTOCOL.md` (rendered) |
| Unattended run (ladder, verbs, stops) | `unattended.sh` (holds `PHASES_CORE` and `DOD_CORE`), `check-unattended.sh`, `gate-guard.js`, `stop-guard.js`, `stall-recorder.js` (engine); `UNATTENDED-{PROTOCOL,VERBS,STOPS,ASKS}.md`, `PLAYBOOK-TEMPLATE.md` and the unattended skill (rendered); `.unattended.conf` (config, owned by the adopter) |
| Build method | `memory/guides/BUILD-METHOD.md` (rendered from `BUILD-METHOD.template.md`); `.memory-tree.conf` (config) |
| Kickoff | `memory/guides/SESSION-KICKOFF.md` (seed); `{user_skills}/session-kickoff` (machine junction) |
| Gate legs and the merge bar | `tools/gate-legs.json` (runner, written by `write_gate_legs`, not a file row); `run-gates.sh`, `gate-profiles.txt` (engine); `windows-only-legs.txt`, `selftest-budgets.txt` (project-owned, withheld); `.githooks/pre-push` (push-main engine), which sources `.githooks/gate-env.sh` (no kit ships it) |
| Autonomy and enforcement hooks | `tools/hooks/{agent-cap,scratch-guard,format-guard}.js` and fragments; `.claude/settings.json` (merged); `.agent-cap.conf` `FANOUT_CAP`; `.memory-tree.conf` `ROUTED_PATHS` |

## 2. One row per artifact

The last column is measured on the fixture unless marked "read". Sentinels were checked with `grep -c` after `update --write`.

| Artifact | Source | Seams today | Direct edit at the next update |
|---|---|---|---|
| `tools/roles/workflows.toml` | engine | None. `check_roles.py:90` closes `WORKFLOW_NAMES` at 10 (R6) and `:93` closes `DRIVERS`. | Change only one line gov didn't touch: the row reads `diverged`, both `ADOPTER-WF-TRIGGER` and `GOV-V2-RESEARCH` are present, and it is merged. Change the line gov also changed (t2): `diverged and the three-way conflicts — left untouched, order written`, then `kit 'roles' was HELD BACK … ROLLED BACK · tools/roles/kit.toml`, so the roles legs stayed at 120/300 and gov's new leg did not land. |
| `tools/roles/house/policy.toml` | seed | `[effort]` by role and stage; `[gates]` validated against the manifest (R12) | Retune kept (`gov-builder = "low"`, and the rendered `effort: low`). The row reads `reseed-available`, and gov's v2 change to the same file (`GOV-V2-SEED`, `max`) does not arrive: 0 hits. |
| `tools/roles/house/<role>.md` | seed | Appended under `## House rules` | Survives and renders (`ADOPTER-HOUSE-SPECWRITER` is in `.claude/agents/gov-spec-writer.md`), reported `patched [seed]`. |
| `tools/roles/agents/<adopter>.agent.md` | none: `load_roles` globs `agents/*.agent.md` (`roles_lib.py:328`) | Drop in a file | `adopt-roles.sh --scaffold` rendered `.claude/agents/acme-auditor.md` with its house rules. No update line named it across four runs, and it survived. The catalogue leg reds it (read): R5 `slot 'acme-auditor' has no ceiling row in BODY_CEILINGS` (`check_roles.py:220-221`), R7/R8 (`:315-337`), R11 (README region). |
| `check_roles.py` (to register that role) | engine | None | Adding the ceiling row on the line gov's v2 changed conflicted (t2). The roles kit was held back, same as the row above. |
| `.claude/roles.json` | generated by `render_agents.py` | None (derived from `policy.toml` and `workflows.toml`) | Overwritten: the added gate and harness were gone (`git diff` shows both removed). The update printed only `ran roles: … --scaffold -> exit 0 (adopted)`. |
| `tools/review-harness/tier2-review.template.js` | engine | Per-call args only: `lensNotes`, `checklist`, `intensity`, `roles`, `efforts`. `KINDS` is closed at 2 (`:183`), `ROLE_KEYS` at 4 (`:229`); `DIFF_LENSES` and `SPEC_LENSES` are typed (`:705`, `:741`). | Added lens `acme-privacy` merged with `GOV-V2-RESUME` and flowed into the rendered `tier2-review.js`. A conflicting edit holds the kit back (sibling pass, same mechanism). |
| `tools/review-harness/tier2-review.js` | rendered | None | Overwritten (`ADOPTER-RENDERED-HARNESS` 0), labelled `re-rendered`. |
| `tools/gate-legs.json`: the adopter's own row | adopter | Append a row | Survives (`acme own leg`). No update line names it. |
| `tools/gate-legs.json`: edited gov argv | gov-owned by receipt | None | `leg 'roles catalogue' in the target differs from what the receipt recorded`, then `gate legs: WITHHELD … the 60 leg(s) this step built are NOT written`, rc 1. Gov's new leg did not land (0). |
| `tools/gate-legs.json`: deleted gov leg | gov-owned | None | Re-appended at the next emission (`review-join ban` 1). No output line names it. |
| `tools/gate-legs.json`: changed gov ceiling | gov-owned | Keep rule (`govkit.py:4249-4253`) | Kept: `kept the target's ceiling 999 (gov's is 310)`. |
| `tools/run-gates/gate-profiles.txt` | engine | None | Merged (`width=3` and `width=7` both present). |
| `.unattended.conf` | config, owned by the adopter | `PHASES_EXTRA`, `DOD_EXTRA`, `DIRECTIVES_EXTRA`(+`_TABLE`), `HALT_CODES_EXTRA`, `HOLD_CODES_EXTRA`; bounds; `REVIEW_ROUNDS`, `LANDING_NODES`, `SPEC_AUDIT_DEFAULT`, `RUN_CLAIMS` | Never touched (`ACMEQA` 1, `acme-signoff` 1). Read: an extra phase is vocabulary only (`verb_phase` `unattended.sh:6003`). An extra DoD item is satisfied only by an attested fact (`*)` arm `:12225-12226`). The core cannot shrink (`*_FLOOR`). |
| Unattended guides, the `/unattended` skill, `BUILD-METHOD.md`, `REVIEW-PROTOCOL.md` | rendered | Conf keys | Overwritten (sibling pass; not re-measured) |
| `.claude/settings.json` hooks | merged | Add entries | Adopter hook survived. The removed `stop-guard` hook was re-wired when its fragment moved (`hooks: tools/unattended/stop-guard.fragment.json wired`). Read: `check-wiring` auto-wires at SessionStart. |
| `.githooks/gate-env.sh` | adopter-only (no kit ships it) | Gate policy env, sourced by `pre-push:652` | No receipt row; gov never writes it (read). |
| `memory/gotchas/*`, `memory/project/*` registries, build README keys (`spec-audit:`, `authorized-by:`) | adopter data | Items the review checklist and the legs read | No receipt row in the fixture; gov never writes them (read). |

Two of the update's outputs above are worth noting, both measured:
- The fixture's update exits 1 on every run because of two unrelated hole legs (`codebase-map`, `agent-cap restatement`). An adopter cannot tell a lost edit from that by the exit code.
- No update line ever named an adopter's role, overlay, leg, or the restored gov leg.

### A defect found on the way (measured, outside the question)
In a default adopter install, the spawn guard refuses gov's own review harness.
- `workflows.toml` names `{prefix}/workflows/tier2-review.js`. Gov installs the kit at `tools/review-harness/`, and the receipt row's source is the template, so `resolve_kit_dir` finds no row and falls back to `tools/workflows`.
- The rendered `.claude/roles.json` lists `['tools/review-harness/unattended-unit.js', 'tools/workflows/tier2-review.js', 'tools/workflows/unattended-build.js']`, and `render_agents` printed `tools/workflows/unattended-build.js … absent here; its kit is not installed` although it is installed.
- Piping a `Workflow` payload into `node tools/hooks/agent-cap.js` in the fixture returned rc 2: `scriptPath tools/review-harness/tier2-review.js … is not a declared harness`. `unattended-unit.js` was admitted (rc 0).

### Where a record and the code disagree
- **Roles descriptor comment.** `tools/roles/kit.toml` says engine files, `workflows.toml` included, are "overwritten on every update". The code three-way merges them, and a non-conflicting edit survived.
- **Product rule.** `.claude/rules/product.md` places the harnesses in `workflows/`, which is true in gov but not in an adopter.

## 3. What an adopter can add beside gov's today, per kind

| Kind | Exists beside gov's? | Registered by | Checked by | Rendered |
|---|---|---|---|---|
| Gate leg | Yes: a row in the shared manifest | Nothing on the adopter's side; gov's own 73 non-kit legs are registered by `[[exempt_leg]]` in `tools/govkit/registry.toml`, which is gov-side only | Runner only; no adopter-side registration check | The manifest is the render |
| Role | The file survives and renders | Glob plus a typed `BODY_CEILINGS` row plus a `workflows.toml` listing | Catalogue leg reds without the two engine edits (read) | `.claude/agents/<role>.md` and `roles.json` (measured) |
| Workflow shape | No: `WORKFLOW_NAMES` is closed at 10 | — | R6 | `roles.json` harnesses derive only from `workflows.toml` workflow-driver entries, so the spawn guard refuses any other harness |
| Harness script | The file can exist (inCMS ran 13 under `.claude/workflows/`) | Population is found by `meta` marker (`check-workflow-syntax.js`, TOOL-aRepatriatedFork-4) | Syntax, fan-out and join legs | Not admitted by agent-cap unless listed in `workflows.toml` (read, `agent-cap.js:2173`) |
| Lens | No: typed arrays in the harness template | — | — | `lensNotes` per call only, with no persisted home |
| Review item | Yes: `memory/gotchas/` classes become the `checklist` | Record grammar | `gotchas.py --check` | Per-diff stdout |
| Run phase, DoD item, directive, halt or hold code | Yes: conf `*_EXTRA` | Conf key | `check-unattended.sh` against shrink-only floors | `DIRECTIVES_EXTRA_TABLE` rows reach the skill; phases and DoD reach no render |
| Hook | Yes: own settings entry | — | — | Merged |

## 4. Gov as its own adopter, and what the records say happened

### Gov's own customizations
- **Gate legs:** 140 in `tools/gate-legs.json`, of which 73 come from no descriptor. All 73 are `[[exempt_leg]]` rows with a reason. I measured this with a `tomllib` diff of the manifest against every descriptor.
- **Roles:** gov edits `workflows.toml` and `house/policy.toml` in place. Those files are also the shipped source and seed, so a retune is also every new adopter's default; for example `175f86981` sets spec writers at high and builders at xhigh. All ten house overlays are 0 bytes.
- **`.unattended.conf`:** `RUN_CLAIMS="on"`, `LANDER_MODE="in-place"`, `KICKOFF_ENGINE`, `GATE_WALL`, `REVIEW_ROUNDS="1"`, and every `*_EXTRA` blank.
- **`.githooks/gate-env.sh`:** `INHERITED_RED=land`, `GATE_DOC_PATHS`, and others.
- **Run-gates declarations:** `windows-only-legs.txt` and `selftest-budgets.txt`.
- **Data:** 148 gotcha classes plus `INDEX.md`, and 31 files under `memory/project/`.
- Gov has no receipt, so it never runs the update path on any of this.

### Records' incidents
I found no record of an adopter customizing roles, `workflows.toml` or `policy.toml`; the grep hit only gov's own specs.
- **TOOL-aRepatriatedFork-4:** at inCMS, gov's harness gates, which only searched gov's install prefix, "print a clean verdict over a set that excludes all 13 live harnesses", and "both adopters carry a hand-kept population fork". It was fixed by discovering harnesses by marker.
- **DEPL-aRepatriatedFork-17 S8:** the gate-leg step refused nc's `agent-instructions wiring` row, which had gov's argv but no receipt record. This produced the claim rule.
- **DEPL-cMendedVintage-22:** a hand-edit of a gov-owned row "is never detected" and was overwritten. A gov argv change "reds an adopter whose manifest is byte-identical". It was fixed to compare the target against the receipt.
- **DEPL-aBenchedProbe-2:** the ceiling keep rule. Its N3 says a deleted key is not preserved.
- **aBoundedCeiling round-2 review:** "An adopter's manifest is a merge, not a rewrite". Target-authored rows with no ceiling sat beside kit rows that had one, and the runner refuses.
- **TOOL-aRepatriatedFork-49:** refused to clear interpreter variables because doing so "changes the environment every adopter's own legs receive".
- **TOOL-aRepatriatedFork-7:** nc's lower `FANOUT_CAP`.
- **Backlog TOOL-cSettledDocket-8 (DEFERRED):** `DIRECTIVES_EXTRA_TABLE` has one reader.
- **nc's landing nodes:** these lived in its `CLAUDE.md` prose and became `LANDING_NODES` (sibling pass).

### Self-tests
- `selftest.py:15790` has a fixture for a target's own leg. `:2664` and `:2679` cover the kept ceiling, `:6175`, `:13855` and `:13897` the row-drift message, and `:15763` the claimed leg.
- `check-unattended.test.sh:2901` and following arm `DIRECTIVES_EXTRA`, and `unattended.test.sh:6637` and `:9802` arm the halt and hold extras.
- No arm covers an adopter role file, an adopter workflow or an edited `roles.json`.

## 5. Candidates: the existing seams a design for custom flow and roles could extend

| # | Mechanism (existing instance) | Smallest test that would make it lose | Result |
|---|---|---|---|
| A | **Shared declaration file with ownership per entry, recorded in the receipt.** Instances: `gate-legs.json` via `write_gate_legs`; `.claude/settings.json` hook merge. | (1) the adopter's addition survives while gov's additions still land; (2) an adopter override of one gov entry survives without stopping the rest; (3) a gov entry the adopter removes stays removed, and is reported | (1) **passed** (`acme own leg` and `roles v2 new leg` both present). (2) **passed for `ceiling`, lost for `argv`**: the whole manifest was withheld, rc 1. (3) **lost**: re-appended with no output line; the stop-guard hook was re-wired. |
| B | **Kit-owned core plus extension keys in conf, with a shrink-only floor.** Instances: `PHASES_EXTRA`, `DOD_EXTRA`, `DIRECTIVES_EXTRA`, `HALT/HOLD_CODES_EXTRA`, `FANOUT_CAP` | (1) survives the update; (2) an added item carries behaviour (a position, a machine check); (3) can remove or retune a core item | (1) **passed**. (2) **lost** (read): a phase is vocabulary, a DoD item an attested fact. (3) **lost by design**: the floor refuses. |
| C | **Seed overlay composed by the renderer.** Instances: `house/<role>.md`, `policy.toml` | (1) survives and renders; (2) gov's later change to the same file still arrives | (1) **passed**. (2) **lost**: `reseed-available`, `GOV-V2-SEED` 0. |
| D | **Discovery by glob or marker.** Instances: `agents/*.agent.md`; the harness `meta` marker | (1) the adopter's file survives and renders; (2) it is accepted by the checker and the spawn guard without an edit to gov's files | (1) **passed**. (2) **lost**: R5/R7/R8 (read), agent-cap rule 6 (measured on gov's own harness), and the registration edit conflicted, holding the kit back. |
| E | **Edit gov's source and three-way merge** | An adopter edit to a line gov later changes | **Lost**: `HELD BACK … ROLLED BACK`, which also froze the kit's gate legs. |
| F | **Adopter data or per-call args read at run time.** Instances: `memory/gotchas/`, `memory/project/*`, build README keys, `lensNotes` | (1) persists and reaches every run unrestated; (2) can change gov's step or lens set | (1) **passed** for gotchas and registries; **lost** for `lensNotes`, which is per call with no home. (2) **lost**. |

Editing a generated output directly is no seam: `roles.json`, `.claude/agents` and rendered harnesses lost the edit silently (measured). Settings-hook merge is a second instance of A, not a separate mechanism. Another candidate would differ only in which file holds the entry.

## 6. Pick, and what it leaves uncovered

**Pick: A, ownership per entry in a shared, merged declaration recorded in the receipt, extracted into one factory.** It has two instances today (`write_gate_legs` and the settings-hook merge), which is the charter's `[reuse]` trigger.
- **Why A:** it is the only measured mechanism where all three hold at once: the adopter's addition survives, gov's new entries still land in the same update, and an override of a gov entry is detected by name (`ownership of the NAME is not ownership of the ROW`).
- **Its keep rule** already shows the override shape working for one field (`ceiling`).
- **B and C** are good for value retunes and vocabularies, but neither can carry new behaviour or deliver gov's later changes.
- **D and E** both lost by holding the kit back. D's typed tables are the reason.

**What the pick leaves uncovered, each with a test the design must add:**
- **Override by field.** Today any field but `ceiling` withholds the whole manifest, rc 1. Test: an override of one gov entry's argv stands, and every other entry still lands.
- **Removing or skipping a gov entry.** Deletion is silently undone, for legs and hooks alike. Test: a declared, reported disable entry survives an update.
- **Registration on the adopter's side.** Gov checks its own legs through `[[exempt_leg]]`, but nothing does this for an adopter. Test: an adopter row with no registration reds.
- **The closed tables** (`BODY_CEILINGS`, `WORKFLOW_NAMES`, `DRIVERS`, `KINDS`, `ROLE_KEYS`, `DIFF_LENSES`/`SPEC_LENSES`, `PHASES_CORE`/`DOD_CORE`) must become entries of the merged declaration. Until then an adopter role or workflow needs engine edits. Test: an adopter role passes the catalogue leg and the spawn guard with no byte of gov's changed.
- **Behaviour of added items.** An extra phase has no position, and an extra DoD item has no machine checker.
- **Rendered prose.** The build method's steps, the unattended verbs and stops, and the kickoff's machine-scope skill have no entry form; a step there is prose in a whole-file render.
- **Reporting.** No update line names an adopter's added or overridden entry, and the fixture's update exits 1 on every run for unrelated holes.
- **The harness-path defect.** It must be fixed before A can carry workflows, or adopters' `roles.json` will keep listing harness paths that do not exist.

**Needed from the main session:** run the `roles catalogue` and `roles render wiring` legs on a fixture holding an adopter role. That would confirm the R5, R7, R8 and R11 verdicts above, which I read from the code because the scratch-guard refuses me as a role agent.
