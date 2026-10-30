**Serves:** research DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24

# Reuse scout E — dShippedRelease

The scout's final return, extracted from its transcript by script, never retyped.

# Reuse scout E: DEPL-dShippedRelease-9, -10, -21, -23, -24

All `path:line` citations were read at HEAD `f4597719e` and are relative to the worktree root, `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d`. The main files are listed with absolute paths at the end. I wrote nothing in the repository.

`scratch-guard` refused my run of `tools/govkit/check_runbook_parity.py` because a role agent runs no gate. The parity leg is therefore unrun, and its figures below come from reading its source and counting anchors.

Neither the `reuse_lookup.py` shortlists nor my searches found a conformance gate, a renderer-of-record table or a layer contract at HEAD. The parent surfaces cited below are specs, not built code.

## (1) One row per unit

### DEPL-9, derived runbook (`cl-0419`, gap-deploy-08)
- **Seam:** `render` in `tools/playbook/render_playbook.py:1024` — reuse for one renderer; extend via a new scope on PLAY-dOrderedCharter-20's S5 `--render-scope` / `--check-render` (not built).
- **Exists today:**
  - The runbook is 164,498 bytes of hand-written prose.
  - `tools/govkit/check_runbook_parity.py:42` anchors sections with `<!-- govkit:entry <id> -->`. 12 of 30 entries are anchored, and `PROBLEM_PIN = 18` (`:60`).
  - Its docstring (`:14`) says it does not grade prose.
  - The order source already exists: `derive_install_order` at `tools/govkit/govkit.py:911`.
- **Closest parent shapes (not built):**
  - PLAY-dOrderedCharter-37 S1 and S2: a `references.toml` reader that returns rows, a `--check` that compares bytes, and the rendered header line.
  - TOOL-dLinkedLibrary-18: the region parser, for a rendered section inside a hand-written document.
- **Design lines:** v2:1782; layer-expansions:435 and :440; research-distribution-a:108; fates:180; gap-register:398; layer-expansions:125 ("in part").
- **Owned nodes:** none.
- **Policy keys:** none.
- **Paths:** `WIRE-INTO-PROJECT.md`, `tools/playbook/render_playbook.py`, `tools/playbook/renderers.toml` (OC-20), `tools/playbook/instruction_units.py` (`INSTRUCTION_PATHSPECS`), `tools/govkit/check_runbook_parity.py`, `tools/govkit/registry.toml` if `runbook_exempt` rows are needed.

### DEPL-10, kit factory and conformance gate (`cl-0420`, gap-tool-07, gap-tool-02, item `kits.version`)
- **Seam:** `kinds.toml` row `kind.kit` plus `core.py new <kind>` (PLAY-dOrderedCharter-7 S4 to S6, not built) — reuse for factory and gate registration; extend via the row's `factory`, `gate` and `population`.
- **Pattern to copy:** TOOL-dWitnessedBar-11 (`new`, `--conform`, kind row), TOOL-dWitnessedBar-45 (`--conform` runs with no govkit), and `leg-schema.toml` (WB-28 §4) with `role-schema.toml` (TOOL-dBoundRoles-2). A kit schema would be the third such file, so the rule is to extract its factory, not copy.
- **Exists today:**
  - Selfcheck arms start at `tools/govkit/govkit.py:1858`, with version at `:2119` and 5c at `:2222`.
  - `read_descriptors` is at `:13238`, and `regen.read_descriptors` at `tools/run-gates/regen.py:108`.
  - There is no top-level known-key set. The only key sets I found are `FORK_RULE_KEYS`, `OUTCOME_PROBE_KEYS`, `OBSERVED_KEYS` and `POLICY_KEYS`.
  - The 30 descriptors use 27 top-level keys.
  - No `new kit` verb exists.
- **`kits.version` seam:** `cmd_mint` at `tools/govkit/govkit.py:13497`, reached through `run_minter` at `tools/push-main.sh:802` (`:902` prepare path, `:1084` attended path). The announced skips are at `:805` and `:810`. The behaviour is already built; what is missing is the `[[item]]` row and the slot in `item.test.merge`. No parent spec names `kits.version`.
- **Design lines:** foundations C3 and C4 (:290, :294); v2:965-971 (P16); layer-expansions:118, :441, :446, :448, :456; research-distribution-b:111-116; fates:107, :177, :178, :185, :186.
- **Owned nodes:** `item.kits.version`, proposed owner DEPL-10, carried by a `**Carries:** node:` line because no clause carries it.
- **Policy keys:** none.
- **Paths:** `tools/playbook/kinds.toml`, `tools/playbook/core.py`, `tools/playbook/core-pending.txt`, a new schema and checker, `tools/govkit/govkit.py`, `tools/govkit/registry.toml`, `tools/check-kit-versions.sh`, `tools/gate-legs.json`, the `[[item]]` home `tools/loop/loop.toml`. The 10 `version_from = {none}` entries are also touched if `none` is refused.

### DEPL-21, purpose field and descriptors for govkit and lib (`cl-0431`, gap-tool-04)
- **Seams:**
  - `purpose`: the `kit` row of `tools/playbook/namespaces.toml`, which PLAY-dOrderedCharter-22 §4 points at `tools/govkit/registry.toml`, "until dShippedRelease's `purpose` in `kit.toml`". TOOL-dTotalRecall-16 S3 and S4 (`--purpose-review --write`) is the writer for "today's kits reviewed".
  - not-installable: `selectable` (`tools/govkit/govkit.py:908`, `:2514`, `:2525`).
  - inline generation: `regen.py` plus `PARITY_ROWS` (`tools/lib/resolve-python.test.sh:168`).
- **Exists today:** 30 descriptors, none carrying `purpose`. `tools/lib` and `tools/govkit` are `[[exempt]]` paths (`tools/govkit/registry.toml:197`, `:299`).
- **Consumer treatment at HEAD, read from source and not executed:**

| Consumer | What it reads | Effect of a new descriptor |
|---|---|---|
| `regen.py:110` | tracked `*/kit.toml` | parsed; no rows means no items; a malformed row exits 2, and `run-gates.sh` turns that into a bar-wide refusal |
| `check-kit-placeholders.py:83`, `:159`, `:222` | filesystem glob | joins the `silent` list; printed in the count line |
| `run-gates.sh:1441` | filesystem glob, existence only | could flip `_rg_any`, so regen runs on a tree holding only lib's descriptor |
| `check-hook-destinations.sh:112`, `:138` | registry, not the glob | sees nothing unless an `[[entry]]` exists |
| `render_playbook.py:806-810` | `*/entries/playbook.kit.toml` plus the registry | sees nothing unless an `[[entry]]` exists; `:590` and `:973` then admit `lib` as a fence or `kits` member |
| `read_descriptors`, `govkit.py:13238` | registry | sees nothing unless an `[[entry]]` exists; `all_kits:908` would then put lib in `--all` |

- **Design lines:** audit-fold:66 (M16), :423 (FM10); project-map:653, :721; fates:181, :182; research-distribution-a:123; layer-expansions:124, :441.
- **Owned nodes:** none.
- **Policy keys:** none.
- **Paths:** `tools/lib/kit.toml`, `tools/govkit/kit.toml` (new), `tools/govkit/registry.toml`, the six named consumers, `tools/unattended/lib-unattended.sh`, each `tools/*/kit.toml` and `tools/govkit/entries/*.kit.toml` for `purpose`, `tools/playbook/namespaces.toml`, their test suites.

### DEPL-23, deployer definition (`cl-0433`, the owed line at v2:1970)
- **Seam:** `tools/roles/agents/*.agent.md` through `roles_lib.load_roles` — reuse for one role definition; extend via the role-landing recipe in TOOL-dWitnessedBar-23 §4.
- **Files that recipe touches:**
  - `tools/roles/agents/gov-deployer.agent.md`
  - `tools/roles/house/gov-deployer.md`
  - the seed list in `tools/roles/kit.toml:36-38`
  - `tools/roles/workflows.toml`
  - `BODY_CEILINGS` at `tools/roles/check_roles.py:87`
  - the roster in `tools/roles/README.md`
  - `.claude/agents/gov-deployer.md`
  - `.claude/roles.json`
  - `tools/govkit/selftest.py`
- **Registration:** TOOL-dBoundRoles-1 S5 already puts `gov-deployer` on `layer.distribution` and `layer.integrations`, and S1 requires `layer` and `acts-as`. BR-2 requires `never` and `return`. None of this is built.
- **Exists today:** 10 role files and no deployer file.
- **Design lines:** v2:1970, v2:419, v2:683, v2:1772; layer-roles:480, :484; flow-roles:106, :107, :119; layer-expansions:326; research-integrations-b:151; BR-1 §8 F3.
- **Owned nodes:** none. The role half of gap-deploy-06 lands here, but that gap is outside this group.
- **Policy keys:** none owned. It reads `deploy.on-verify-fail`, whose row is at `tools/policy/catalogue.toml:1028` and which another group owns.

### DEPL-24, `install.guards` (`cl-0434`, gap-deploy-14)
- **Seam:** `run` at `tools/settings-merge.py:510`, whose first argument is already `settings_file`, plus `GOV_SETTINGS_JSON` at `tools/check-wiring.sh:102` and `tools/govkit/govkit.py:6132`, `:6187` — reuse for the target settings file; extend via one resolver reading the key. A receipt-row precedent for a destination outside the repo is `scope = "machine"` at `tools/govkit/entries/kickoff-manifest.kit.toml:47`.
- **Exists today:**
  - Project-settings wiring through `run_fragment_merges` (`tools/govkit/govkit.py:6109`).
  - `check-wiring.sh` arms for each hook.
  - Nothing handles managed settings.
  - The "not under the tree" branch of `render_settings_path` already reports rather than reds.
- **Design lines:** v2:1310, v2:1434, v2:1441; night-pass:380, :540, :670, :753; gap-register:404.
- **Owned nodes:** `policy-key.install.guards`, proposed owner DEPL-24.
- **Policy keys:** `install.guards`.
  - The row exists at `tools/policy/catalogue.toml:1058` with owner dShippedRelease and no `summary` or `usage`.
  - The name is on `tools/policy/unsummarised-keys.txt:77`, so the spec fills the row and drains it with `policy.py lists --write`.
- **Paths:** `tools/settings-merge.py`, `tools/check-wiring.sh`, `tools/govkit/govkit.py`, the catalogue and list above, `.governance/policy.json` (mirror), `WIRE-INTO-PROJECT.md` or its rendered section.

### Gap placement
- **gap-tool-02:** DEPL-10.
- **gap-tool-07:** DEPL-10.
- **gap-tool-04:** DEPL-21.
- **gap-deploy-08:** DEPL-9, one half only (see item 9 in section 2).

## (2) Where records and source disagree

1. **Two named consumers do not read `*/kit.toml`.** `check-hook-destinations.sh` reads the registry (`:112`, `:138`), and `render_playbook.py` reads `*/entries/playbook.kit.toml` and the registry (`:806-810`). Only `regen.py:110`, `check-kit-placeholders.py:83` and `run-gates.sh:1441` glob descriptors.
2. **The clause's consumer list is short.** It misses `lib-unattended.sh:857`, `render_agents.py:171-195` and `map_extractors.py:85`, whose docstring calls lib a kit while `registry.toml:199` says "Not a kit". Unbuilt consumers are also missing: `check_layers.py` (OC-16 §4), `leg_factory.py` (WB-11 S2), the `kit` namespace extractor (OC-10:115) and `[[command]]` rows (DL-18:47).
3. **The clause marks only lib not installable.** `registry.toml:301` says the same of govkit ("never installed into a target"), yet `tools/playbook/kit.toml:31` and `:37` ship two govkit files.
4. **`registry.toml:199`, `:680` and `:684` go stale.** The two later rows say "no descriptor can claim a leg over it", which stops being true once lib has a descriptor.
5. **OC-16 has the wrong population.**
   - S2 and AC8 say 29 descriptors; HEAD has 30 and its file list omits `tools/policy/kit.toml`. DEPL-21 makes 32.
   - S1 uses `homes` and `shared` for directories with no descriptor.
   - Its `no-layer` plant reds any descriptor without a layer, but `shared` says lib holds no layer.
   - OC-10:115 and :193 also say 29.
6. **`cl-0433` says "dBoundRoles's layer contract".** The contract is PLAY-dOrderedCharter-16 S3. BR-1 S5 only adds `roles`, `lenses` and `check_layer_roles`. Both are unbuilt.
7. **BR-1 S7 and AC6 conflict with the flow design.** They refuse any composed item whose actor is `role:gov-deployer`, and §4 says every row is an item of the core loop. flow-roles:106, :107 and :119 name the deployer as an item actor. Layer-roles:480 calls it an "item role".
8. **"Render parity" is defined nowhere.** It appears only in chain rows v2:1782 and v2:1785. OC-20's gate is `--check-render`, its scopes exclude a runbook, and `INSTRUCTION_PATHSPECS` (S4) excludes `WIRE-INTO-PROJECT.md`.
9. **gap-deploy-08 has an uncarried half.** The packet's goal closes every gap, but layer-expansions:125 closes it "in part". The `[isolate]` ports and the `up —` line have no clause, and my v2 grep for both found nothing.
10. **Three gaps have only a chain-row cell.** gap-tool-02, gap-tool-04 and gap-tool-07 appear in v2 only in row 1782's gap cell, and no parent spec cites them. Clauses 0419, 0420 and 0433 are token-blind, so `carries.py` cannot confirm their carriers.
11. **Stale figures.**

| Record claim | At HEAD |
|---|---|
| arm 5c at `govkit.py:2162` | `:2222` |
| 11 `[check]` argvs | 12; 11 duplicate their own leg, `policy` does not |
| 11 `adopt-*.sh --check` legs | still 11 |
| 73 files with `resolve_python` | 74 |
| 261 markers over 17 names | 270 lines over 18 stems by my regex, including tests, `tools/lib` and one `helper` stem |
| 163 KB runbook | 164,498 bytes |
| 0 of 29 descriptors carry `layers` | 0 of 30 |
| 10 of 29 unversioned | 10 of 30 |

12. **Field names drifted.** Layer-expansions:448 lists `layers`, `declares`, `uses`, `records`, `policies` and `units`. OC-16 S2 and F2 use a singular `layer` and put `declares` and `uses` on `layers.toml` rows. OC-9 puts units in per-kit `instructions.toml`.
13. **Version rule versus code.** Layer-expansions:449 refuses `none` unless a kit ships no bytes. Selfcheck arm 5 accepts `none`, and `cmd_mint` skips it. Ten entries are affected.
14. **The conformance gate has no settled owner.** Layer-expansions:118 defers to "the chain re-cut", and the re-cut record has no matching line. Layer-expansions:446 says core, v2:1782 gives it to this build, and OC-16's rejected alternatives refuse a core contract inside govkit.
15. **"Core guards" has no list.** v2:1310 and night-pass:380 and :540 name no members. `settings-merge.py` (docstring, about `:50`) says the `${CLAUDE_PROJECT_DIR}` spelling varies "for nobody".
16. **Stale citations.**
    - OC-20 §10 and OC-37 cite `render()` at `:979`; HEAD is `:1024`.
    - BR-1 cites `WORKFLOW_NAMES` at `:90`; HEAD is `:92`.
    - research-tool-fates:138 cites v2:1197, and ownership-skeptic:73 cites v2:1122, for a row now at v2:1782.
    - The distribution research still says `deploy.version`, renamed at layer-expansions:670.
17. **Outside this group, but it will hit the first spec commit.** `memory/builds/dShippedRelease/README.md:8` carries `status: OPEN`, and PLAY-dClosedLoop-31 says the generator refuses that key once a spec exists.

## (3) Shared interfaces, proposed names

| Name | Producer | Consumers |
|---|---|---|
| `tools/playbook/kit-schema.toml` (`[kind]`, `[[field]]`, WB-28's shape) | DEPL-10 | DEPL-21, DEPL-26 (interpreter floor), `check_layers.py` |
| `kind.kit` row, `core.py new kit`, leg `kit conformance` | DEPL-10 | OC-7's `core.py kinds` |
| `purpose` descriptor key | DEPL-21, on DEPL-10's schema | OC-22 `namespaces.toml`, TR-16, DEPL-9 |
| `installable = false`, `why_not_installable` | DEPL-21 | every row of the consumer table, `check_layers.py`, `leg_factory.py` |
| `[[inline]]` rows on lib's descriptor (research-distribution-a:123) | DEPL-21 | `regen.py`; TOOL-dLinkedLibrary's parity rows |
| `read_kit_rows()`: ordered rows, install order from `derive_install_order` | DEPL-10 | DEPL-9, DEPL-17 |
| render scope `runbook`, `[[target]]` for `WIRE-INTO-PROJECT.md` | DEPL-9 | OC-20's `--check-render` |
| `gov-deployer`, `layer = "layer.distribution"`, `acts-as = "item"` | DEPL-23 | release-notes and verify units (DEPL-3, DEPL-15) |
| `guard = true` on a hook fragment, `derive_settings_target(root)` | DEPL-24 | `settings-merge.py`, `check-wiring.sh`, `run_fragment_merges`, DEPL-17, DEPL-25 receipt |
| `item.kits.version` row with `slot = test.merge` | DEPL-10 | TOOL-dWitnessedBar-4 S5, DL-12 |

## (4) Order constraints

- **Within the group:** DEPL-10, then DEPL-21, then DEPL-9, because the runbook renders fields the schema defines. DEPL-23 and DEPL-24 are independent of those three.
- **Across groups:** DEPL-24's receipt field, if any, lands with or after DEPL-25. DEPL-17 shares `read_kit_rows()`, so it follows DEPL-10.

| Unit | Parent surfaces needed (none built) |
|---|---|
| DEPL-9 | OC-20 S4, S5, S8; OC-37 S1, S2; LL-18 |
| DEPL-10 | OC-7 S4 to S6; OC-16 S2 and S3; WB-11, WB-45; WB-4 S5; DL-24 S3 |
| DEPL-21 | OC-16 S1; OC-22 §4; TR-16 S3 and S4; WB-11; LL-18 and the `PARITY_ROWS` growth from LL-54, -56, -61, -64, -74 |
| DEPL-23 | OC-16; BR-1 S1, S5, S7; BR-2; BR-6; WB-23 as the recipe |
| DEPL-24 | `read_policy_value` (OC-7 §4); dSafePassage-5, which leaves this out of scope (§3, `:102`) |

## (5) Forks

**Could not be settled from source:**
- **F1.** Do lib and govkit become `[[entry]]` rows, or stay `[[exempt]]` with an unregistered descriptor? An entry makes every registry consumer see them, but needs `all_kits`, `--all` and arm 7b changed. Staying exempt means the hook and renderer consumers never see them, so the clause's "each consumer's leg" is empty for those two.
- **F2.** Is not-installable a new value of `selectable`, or a new key? Reusing `selectable` is smaller, but `:908` tests `!= "conditional"`, so a new value silently means selectable.
- **F3.** Where does the conformance gate live? Source favours a core home in `tools/playbook`, by OC-16's rejected alternative and WB-45's no-govkit rule. Yet selfcheck already holds most of the arms, and research-distribution-b:101 wanted to extend them.
- **F4.** How does a core renderer reach `derive_install_order`, which sits in an expansion kit? The options are an `optional` row under OC-16, or moving the order into core.
- **F5.** Does the runbook render whole, or region by region? "A rendered section" in the clause implies regions.
- **F6.** Does `render parity` mean OC-20's gate with a new scope, or a stronger `govkit runbook parity` that keeps the leg's name? OC-20 F2 says a leg keeps its name either way.
- **F7.** How do expansion items with a deployer actor pass BR-1 S7? This needs a deviation or a ruling, because AC6 pins the refusal.
- **F8.** Which workflow does the deployer join? WB-23 kept `WORKFLOW_NAMES` closed, and BR-1 S4 added two names.
- **F9.** Which P28 fields stay on descriptors, given item 12 in section 2, and does `version_from = {none}` become red for the 10 entries now?
- **F10.** What does "one seen red on a planted lib descriptor" plant, and in which leg?
- **F11.** Does the one version check retire `check-verdict-epoch.sh`? OC-16 AC1 pins that script's stdout as byte-identical.
- **F12.** Which hooks are the core guards, and how does a committed policy file express a per-machine setting? Managed settings paths and command spelling are harness facts I could not confirm from this repository.
- **F13.** Who carries the `[isolate]` and `up —` half of gap-deploy-08? It needs a clause, a `**Moved:**` line, or a recorded departure.

**Files**
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\govkit\govkit.py`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\govkit\registry.toml`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\govkit\check_runbook_parity.py`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\run-gates\regen.py`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\playbook\render_playbook.py`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\settings-merge.py`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\check-wiring.sh`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\policy\catalogue.toml`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-16.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-20.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-1.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-11.md`
