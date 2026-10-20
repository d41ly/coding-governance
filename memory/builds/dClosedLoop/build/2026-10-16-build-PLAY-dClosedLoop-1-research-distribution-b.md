# Research: the distribution expansion, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 56's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-21-researcher.md`, which dispatch 55 ran
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`.

---

I verified everything below by reading code and running read-only probes. Two caveats on the probes. My one `govkit epoch` run is itself a bar leg ("kit epoch"): it is read-only and wrote nothing, but I'm disclosing it. When I then tried `check-receipt.py`, scratch-guard refused it as a gate leg, so the receipt-absent behaviour is read from the code (check-receipt.py:430).

## 1. Verdict

Distribution is the layer that moves bytes and versions across a repository boundary. Its parts are the kit descriptor, govkit's install and update, the receipt, the release tags with their notes, the currency probe, the fleet register, and the install of each harness adapter's render targets.

Core is everything that runs on bytes already in the tree: the render, `--check`, the bar, and the lander. The descriptor-driven seam already exists (govkit, 29 descriptors, a receipt that carries a per-kit `version`).

The pick extends that seam (candidate A):
- releases become annotated product tags;
- currency is computed in the adopter from gov's remote tag list plus its own receipt, so no gov checkout is needed;
- the wiring and version judges collapse to one verdict each.

With no distribution installed, the core already takes announced fallbacks.

## 2. Today

| Part | What it does | Measured use | Where |
|---|---|---|---|
| Kit descriptors | Declare files, roles, adopt, check, legs, holes, version source | 29: 17 `tools/*/kit.toml` plus 12 `tools/govkit/entries/*.kit.toml`, 2,754 lines. **No descriptor declares layers, extension points, record kinds or policies** (0 hits) | e.g. tools/branch-reconcile/kit.toml:4-65 |
| Version minting | The lander runs `govkit mint` into the prepared merge | `epoch`: 20 versioned, 9 `skip · no declared version` (push-main, agent-instructions, gate-lint, 6 check-* entries) | push-main.sh:799-810; govkit.py:13110-13173 |
| Version carriers | `gov:kit <id>@<n>` markers rewritten by `write_version_carriers` | 682 markers in 368 files | govkit.py:798 |
| Releases and notes | — | 0 release tags (only `archive/*`, 3 on the remote); 0 changelog files; 4 `mint:` commits in 5,997 on main, 0 in the last 300 | below |
| govkit verbs | selfcheck, shipped, epoch, mint, contribute, plan, check, apply, intake, update, adopt | 11 verbs; `contribute` is dispatched (:13713) but missing from USAGE (:13212); no `fleet` verb, although the scout planned one (governance-deployer-research.md:66) | govkit.py:13672-13745 |
| Conformance | `govkit selfcheck` | 10 numbered arms, 42 sub-arm markers | govkit.py:1772-3686 |
| Adopt scripts | Per-kit configure and `--check` | 13 non-test `adopt-*.sh`; none writes the receipt | tools/*/adopt-*.sh |
| Receipt | `install.json` (schema 3) plus `install.sums`; each row carries `kit`, `version`, `sha256`, `gov_oid` | Gov itself has **none**: `.governance/` holds only `deploy.toml` | govkit.py:8019-8029, :7608-7609 |
| Receipt readers in the core | Kit-dir resolution reads the receipt first, then probes | 31 non-govkit files read `install.json` | resolve_kit_dir.py:16-22 |
| Overlay | `deploy.toml` `[answers]` and `[charter] adopter_rules` → charter section 2 | Gov selects 22 of 29 entries and omits `run-gates`, `branch-reconcile` and 5 check-* entries. Its comment says "EVERY kit this repo carries" (deploy.toml:11): **the record and the code disagree** | deploy.toml:18-26, :59-70; render_playbook.py:28 |
| Harness render targets | `CLAUDE.md` = `@AGENTS.md`; aliases claude, gemini, copilot, cursor, windsurf; Codex reads `AGENTS.md` natively (`CODEX_MAX` 32 KiB) | The gov leg wires `--aliases claude` only. 24 `rendered` rows, 7 of them hard-coded to `.claude/skills/*/SKILL.md`, plus 1 `merged` row into `.claude/settings.json` | adopt-agent-instructions.sh:30-58; kit table below |
| Currency | `resolve_measurer_currency` checks only that gov's own clone matches its remote (identity via `ls-remote`, "never distance") | No adopter-currency code. `census.py` needs the adopter's tree (`--adopter` required) | govkit.py:609-626; census.py:309 |
| Fleet register | `adopters.toml` | 3 rows, a brand-name ban only | adopters.toml:1-25 |
| Inline lib copies | Hand-kept blocks, parity-gated | 254 `# >>>` markers across 16 primitives: resolve_python 77, resolve_kit_dir 71, derive_self_rel 49 and others. 72 non-lib files define `resolve_python() {`, plus the canonical = 73, which matches the register | `git grep "# >>> "` |
| Runbook | The `cp -r` install path | 162,896 bytes. The descriptor's `project-owned` withholding is ignored by `cp -r` | WIRE-INTO-PROJECT.md; codebase-map/kit.toml:44-46 |

```
$ python3 tools/govkit/govkit.py epoch     → 29 lines; 20 "clean · <ver>", 9 "skip · no declared version"; exit 0
$ git log origin/main --grep='^mint: kit versions' --oneline | wc -l → 4
$ git ls-remote --tags origin               → refs/tags/archive/{aGatheredDeclaration,aMendedWarden,aPairedLexer}
```

## 3. Attach points

| Attach point | Declared in | Core behaviour without distribution |
|---|---|---|
| Deploy's "versions and release notes" | flow-steps:358-359, as a prose bullet | The lander's announced skip: "kit versions were NOT minted — no govkit deployer beside this lander" (push-main.sh:806-808), exit 0 |
| Harness adapters' load points (R-K) | layer-runtime:743; layer-instruction:594-604 | The instruction command renders `AGENTS.md` and its aliases in place, which is core (agent-instructions, layer-instruction:227) |
| Command adapters (`govkit`, `release`, `currency`) | layer-runtime:739 | Unregistered: the item's slot renders "not installed" |
| Journal readers (fleet watch) | layer-runtime:746 | None |
| Kit-dir resolution reads the receipt | **No layer declares it.** 31 core files read it | Falls back to a probe beside the kit, then a named refusal (resolve_kit_dir.py:19-21) |
| Maintain's release cut | observability, unreviewed (flow-steps:476-483) | Without observability, no cadence runs, so no release is cut |

Attach points the layer needs that no core layer declares:
1. **Install targets per harness adapter.** `[harness]` (layer-runtime:710-732) lists capabilities but has no field for "where a rendered Skill, rule or hook lands". The 8 `.claude/` paths are typed into descriptors.
2. **The receipt as a record kind** owned by distribution and read by the core. P30 says one declaration; there is none.
3. **Deploy's version slot as a registered point.** Today it is a bullet.

## 4. Candidates

| | Mechanism | Smallest losing test | Result |
|---|---|---|---|
| **A. Extend govkit, with adopter-side currency** (pick) | Descriptors gain the P28 fields. Releases are annotated product tags. The receipt records per-kit `version` and the installed tag. The adopter's currency probe compares its receipt with `git ls-remote --tags <gov_source>`: identity only, no objects (the `resolve_measurer_currency` seam) | (1) The receipt must give per-kit versions without a gov checkout. (2) `ls-remote` must answer from a tree with no gov objects | (1) Passes: rows carry `"version": vers` (govkit.py:7608). (2) Passes: `ls-remote --tags origin` returned 3 refs. **Owed:** 0 release tags exist, so the probe today can only say "no release published" |
| **B. Gov-side fleet pull** | A `fleet` verb reads each adopter's receipt from its clone (the census shape), and gov owns the currency verdict | The witness must be available to the adopter's own Deploy, which the contract hands it, without a checkout of the other repo | **Loses as the primary mechanism.** `census.py:309` requires `--adopter <tree>`, and check-receipt.py:7-14 says provenance "resolve[s] only against a gov checkout". It is kept as the fleet register's reader under `pull-and-watch` |
| **C. Git-native vendoring** (submodule or subtree at a tag) | The kit tree is pinned by a git link, and currency is the pinned SHA | Every shipped file must land inside the vendored directory | **Loses.** 28 of 92 file rows land outside the kit or prefix: 24 `rendered` (`.claude/skills/*`, `{memory_root}/guides/*`), 3 `merged` (`.githooks/pre-commit`, `.claude/settings.json`, `pyproject.toml`) and seeds. An installer is needed anyway, and gov cannot vendor itself (P8) |
| **D. Per-kit adopt scripts plus `cp -r`** (no central deployer) | The runbook path | The delivery must honour withholding and record what it installed | **Loses.** 31 `project-owned` rows are ignored by `cp -r` (codebase-map/kit.toml:44-46), and none of the 13 adopt scripts writes a receipt (grep: 0 writes) |

```
$ python3 - (tomllib over 29 descriptors)
file roles {'engine': 45, 'generated': 1, 'seed': 10, 'project-owned': 31, 'merged': 3, 'rendered': 24}
destinations outside the kit/prefix: 28
[check] argv present: 11 ; identical to one of its own gate_leg argv: 11
```

**Version identity inside A** is a detail fork (§8.1), not a fifth mechanism.

**Wiring consolidation inside A.** There are two shapes:
- (i) one in-tree verdict that reads the shipped descriptors' `[check]` argvs plus receipt integrity, emitted as one bar leg;
- (ii) govkit `check` alone.

(ii) loses on the same test as B: `check` needs a gov checkout (check-receipt.py:7-8), so an adopter's bar cannot run it. I pick (i).

## 5. The contract, filled

| Field | Distribution |
|---|---|
| Tag and definition | `distribution`: delivery of kits across repositories (install, update, release, currency, overlay), and the install of each harness adapter's render targets |
| Instruction units | The deploy-governance Skill (skills/deploy-governance/SKILL.md, 171 lines) reduced to the operator order; release-note and currency views; the runbook shrunk to a pointer at the descriptors (gap-deploy-08) |
| Engine kits | govkit, with check-wiring's install arms and check-placeholders folded in; the adopt scripts (configure only, `--check` moved into the one verdict); the lib-block generator; `adopters.toml` grown into the fleet register |
| Record kinds | `receipt` (`.governance/install.json`, writer govkit apply/update, readers core resolvers and the verdict); `release` (annotated tag plus notes, writer `govkit release`); `currency` (per-SHA probe record, writer the probe); `fleet-row` (gov-internal); `outbox order` (existing) |
| Extension points | **Declares:** kit layer packs (the descriptor's `layers`, `extends` and `records` rows that a conformance gate grades). **Uses:** Deploy's version slot; harness adapters (reading a new `install_targets` field); command adapters; journal readers |
| Policies and gates | Keys in §6. Gates: **one wiring verdict** replaces the 12 wiring judges; **one version check** replaces the 8 version legs plus `check-verdict-epoch`; the kit-factory conformance gate (selfcheck arms plus a P28 arm) |

**Descriptor fields P28 needs:**
- `layers = ["memory"]`;
- `extends = [{point="hook packs", name="recall-opened"}]`;
- `declares = [...]`;
- `records = ["landing", ...]`, each a join to the memory contract;
- `policies = ["release.cadence"]`, a join to the catalogue;
- gates are the existing `[[gate_leg]]` rows.

**The conformance gate (the kit factory's)** checks five things:
1. every field is present;
2. every name resolves in its registry (layer tags, Runtime's nine points, record kinds, the key catalogue);
3. every versioned file has `version_from`, with no `none` permitted unless the kit ships no bytes;
4. every `rendered` destination is either adapter-relative or explicitly harness-agnostic;
5. `requires` covers every sibling the code resolves. That fixes the push-main to run-gates miss (`requires = []` against push-main.sh's `post-merge.sh`), which is gap-deploy-07.

## 6. Items and policies

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `deploy.version` (fills Deploy's slot, inside the lander's prepare) | command `govkit mint` | Bumps every entry whose shipped bytes moved | The `epoch` verdict at the push boundary, from history (govkit.py:13034-13062) | clean or minted → land; refused → Test; govkit absent → announced skip, the push bar's epoch leg grades |
| `maintain.release` | command `govkit release`, run by Maintain when `release.cadence` is due | Cuts annotated tag `gov/v<date>.<n>` with notes generated from the landing records and mint lines since the previous tag | The tag on the remote (`ls-remote`) and the notes blob at the tag | nothing moved → skip; cut → `maintain.fleet`; remote refuses → owner item |
| `maintain.currency` (in every adopter) | command | Joins receipt rows to the remote tag list → releases behind, per kit | Currency record keyed by HEAD SHA, from receipt plus advertisement; `unverified` when unreachable, announced and never green | ≤ `currency.max-behind` → done; over → an owner item proposing `update` |
| `maintain.fleet` (gov only) | command | Reads each register row's remote receipt (shallow fetch of `.governance/install.json`) | Fleet record per release | `pull-and-watch` → report; `push-branches` → opens an update branch per adopter |
| `distribution.install` and `distribution.update` | owner or command | apply, adopt, update | Receipt plus the one wiring verdict | Existing rollback and outbox |
| `instruction.install-targets` | command | Writes each render to the paths `runtime.harnesses`' adapters declare | Wiring verdict re-render compare | Adapter declares no target → slot "not installed", core render kept |

| Key | Allowed | Default | Why |
|---|---|---|---|
| `release.cadence` (existing) | every-landing, daily, weekly, owner-cut | weekly | Handed |
| `deploy.currency` (existing) | pull-and-watch, push-branches, pull-only | pull-and-watch | Handed. `pull-only` = `maintain.currency` on demand; `pull-and-watch` adds Maintain plus `maintain.fleet`; `push-branches` adds gov-opened branches, which need adopter write access |
| `currency.max-behind` | 0, 1, 2, 4 releases | 2 | Turns a measurement into an owner item. The 990-commits case went unseen because nothing set a bar |
| `install.from` | release-tag, any-commit | release-tag | The receipt then names one release, so "releases behind" is defined. A mixed install (75 distinct commits in nc's receipt, per the deploy research §4) breaks it |

## 7. Gaps

**Closed by the pick:**
- **gap-deploy-04:** the adopter-side probe, the fleet register and the three modes.
- **gap-deploy-06:** release tags and generated notes. The release *review* still needs a role, which is a roles-layer fill.
- **gap-tool-02:** one verdict and one check.
- **gap-tool-04:** generation.
- **gap-deploy-08:** partly: the runbook shrinks to descriptors once `cp -r` (D) retires.
- **gap-deploy-07:** only its version half: push-main gets `version_from` and `requires`. The hook-kill half stays with Runtime.

**New gaps exposed:**

| Proposed gap | Evidence |
|---|---|
| Harness install targets are hard-coded | 7 `rendered` rows to `.claude/skills/*` plus 1 `merged` row to `.claude/settings.json`; no `[harness]` field for targets (layer-runtime:710-732) |
| The receipt is undeclared core input | 31 non-govkit files read `install.json`; no layer contract declares it |
| The inline-copy class is wider than `gap-tool-04` | 254 markers across 16 primitives, versus 73 `resolve_python` files |
| The wiring judgment is declared twice | All 11 `[check]` argvs are identical to their own `[[gate_leg]]` argv; `check-wiring.sh` (1,988 lines, 16 `check_*` arms) is a third judge, run at SessionStart (.claude/settings.json:56) |
| Gov's overlay contradicts itself | deploy.toml:11 says "EVERY kit" but omits 7 entries, `run-gates` among them |
| No release has ever been cut | 0 release tags, 0 changelogs; 9 of 29 entries unversioned |
| USAGE is stale | `contribute` is missing (govkit.py:13212 against :13713) |

## 8. Forks

| # | Decision | Options | Recommendation |
|---|---|---|---|
| 1 | Release identity | (a) one product tag `gov/v<date>.<n>`, with kit versions in the notes; (b) per-kit tags `kit/<id>/v<ver>` (20 per release) | **(a).** FL-DP2 measures currency in releases behind, and tag names alone order it via `ls-remote`. Per-kit detail is read on `update` |
| 2 | Does gov carry a self-receipt (P8)? | (a) `govkit apply --target .` on gov; (b) gov stays receipt-less and is graded on the absent path | **(b).** A self-receipt hashes the source against itself and proves nothing. Gov's receipt-less tree is the standing fixture for "core without distribution". P8's overlay half is met by `deploy.toml`, once fixed to select every entry |
| 3 | Where inline lib blocks are generated | (a) at install by `apply`; (b) in-tree by a regen stage, tracked and drift-gated | **(b).** The `cp -r` path and gov's own tree both need the bytes present, and only (b) serves both |
| 4 | The `cp -r` install path | Keep it, or retire it | **Retire it.** It loses test D, and its runbook is the bulk of gap-deploy-08 |
| 5 | The fleet register's home | (a) grow `adopters.toml` with remote and cadence; (b) adopters self-register | **(a).** It is already gov-internal and unshipped (adopters.toml:1-3), and self-registration needs a write path into gov |

**Absent (question 6).** In a tree with no distribution, gov's own included:
- the lander mints nothing, announces it and lands (push-main.sh:806-808);
- `check-receipt` prints `SKIP no receipt` (check-receipt.py:430);
- kit resolution probes beside the kit (resolve_kit_dir.py:20);
- the currency slot renders "not installed — no receipt; currency unmeasured";
- `policy.on-missing-expansion=refuse` refuses only a preset that names `release.cadence` or `deploy.currency`.

The core render and `--check` of `AGENTS.md` and its aliases still run, because they are core instruction.

**Build-time tests the pick owes (not built here):**
- a fixture adopter with a receipt at tag N−3 and a stub remote advertising N, where the probe must report 3 behind with no gov objects present;
- a descriptor missing `layers` must red the conformance gate;
- a Codex-only adapter must receive no `.claude/` writes.

Files most relevant:
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\govkit\govkit.py
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\govkit\registry.toml
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\govkit\adopters.toml
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\push-main.sh
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\lib\resolve_kit_dir.py
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\run-gates\check-receipt.py
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\agent-instructions\adopt-agent-instructions.sh
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\.governance\deploy.toml
