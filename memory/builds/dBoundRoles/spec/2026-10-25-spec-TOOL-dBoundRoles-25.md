# TOOL-dBoundRoles-25 — the spawn guard and harness admission moved into the roles pack, admission held to the landed blob, `tools/hooks/agent-cap.js` retired with an upgrade step

**Status:** DEFERRED · rev-5 · 2026-10-26 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 26 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0190@03bbbf1e whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-c.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-16 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-24 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-25-deviation-251.md](../build/2026-10-26-build-TOOL-dBoundRoles-25-deviation-251.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-25-deviation-252.md](../build/2026-10-26-build-TOOL-dBoundRoles-25-deviation-252.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-25-deviation-253.md](../build/2026-10-26-build-TOOL-dBoundRoles-25-deviation-253.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-25-deviation-254.md](../build/2026-10-26-build-TOOL-dBoundRoles-25-deviation-254.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-26 |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-69 |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-43 TOOL-dBoundRoles-60 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

By NT-27's table, agent-cap's handoff spawn guard and its harness admission belong to the roles pack,
with admission comparing a harness with its landed blob (the night pass two, point 7). At HEAD,
admission matches a harness by path alone, so a harness edited and not yet landed runs at call time
before the merge bar has read it (gap-roles-30). In a default adopter install the guard also refuses
gov's own `tier2-review.js` (gap-roles-25). This unit moves every rule `tools/hooks/agent-cap.js` still
runs at the build run's base into `tools/roles/spawn-guard.js` (brief I24, D4). It holds a harness to its
landed blob and gives each helper the file exports a home. Then it retires `tools/hooks/agent-cap.js`
with an upgrade step, its readers inventoried by name and by value, the charter's agent-cap line among
them.

## 2. Scope (IN)

- **S1** — The inventory, taken at the build run's base and never from this spec's list (brief D4).
  Every rule `main()` of `tools/hooks/agent-cap.js` runs, found by its `RULE <n>` comment and its call
  in `main()`, and every name its `module.exports` carries, each with its importers by
  `git grep -n -F 'agent-cap.js' -- tools skills`. The pass writes the inventory into its acceptance
  ledger before moving anything. A rule or export the disposition table of §4 does not place stops
  the unit (§8 F6). Observed by AC9.
- **S2** — The pack. `tools/roles/spawn-guard.js` is a `PreToolUse` hook on `Workflow|Agent` holding
  every rule S1 finds, in `main()`'s order. That is rule 6 as TOOL-dBoundRoles-4, -6, -10, -16, -17 and -20
  leave it (the handoff spawn guard and `checkHarnessCall`), rule 7 (TOOL-dGroundRules-10 S5's settings
  check) and any call-time check a parent added beside them. Each deny keeps its bytes after the prefix
  `BLOCKED by spawn-guard:`. Its fragment `tools/roles/spawn-guard.fragment.json` names the event, the
  matcher `Workflow|Agent`, the marker `spawn-guard.js` and the hook path, laid out like
  TOOL-dFairHearing-16 S4's `spec-audit-optin.fragment.json`. Observed by AC1, AC2, AC3, AC7 and AC8.
- **S3** — Admission held to the landed blob. A `Workflow` call whose `scriptPath` is a declared
  harness is admitted only when the harness file's working-tree blob id equals its blob id at the
  landed revision (§4 "Admission"). A harness absent at that revision is refused as not landed.
  Observed by AC4, AC5 and AC6.
- **S4** — The helpers' homes (§4 "Disposition", §8 F3). A helper read by one kit moves into that
  kit. A helper read by two kits moves into `tools/hooks/scratch-guard.js`'s `module.exports`, which
  the pack already reads for rule 6's index readers. A kit imports no sibling kit (TOOL-dGroundRules-1
  §4), so `tools/roles/kit.toml`'s `requires_if` gains a row naming `agent-cap` whose `why` names
  `spawn-guard.js`'s require of `scratch-guard.js` and the pack's refusal where it does not resolve.
  Observed by AC9.
- **S5** — The suite. `tools/roles/spawn-guard.test.sh` holds every arm of
  `tools/hooks/agent-cap.test.sh` over a moved rule, retargeted, plus the arms of AC4 to AC6. The
  roles kit withholds the suite as `project-owned`. A new leg, `spawn-guard self-test`, runs it,
  declared once as an `[[exempt_leg]]` row of `tools/govkit/registry.toml` by `leg_factory.py new
  --exempt` (TOOL-dWitnessedBar-11 S1, S3), its `enforces` that of `agent-cap self-test` as that
  unit's S6 wrote it; `tools/gate-legs.json` is re-rendered by `--write`, never edited. That leg still
  on PLAY-dOrderedCharter-7's pending list stops the unit, as that list only shrinks. Under
  `core.bypass = never` the meta-check reds this guarded leg (PLAY-dOrderedCharter-7 S10) while
  TOOL-dWitnessedBar-11 §8 F5 is open; the leg keeps its guard and takes F5's outcome. Observed by AC8.
- **S6** — The wiring. Gov's `.claude/settings.json` wires the pack and no `agent-cap.js` command.
  `tools/settings-merge.py`'s default fragment is the roles kit's `spawn-guard.fragment.json`, read
  from its file and never typed (§8 F4). `tools/check-wiring.sh` grades the pack's fragment through
  the one per-fragment function TOOL-dFairHearing-16 S6 makes. The roles kit's `requires` gains the
  hooks entry `agent-cap` and the policy kit. Observed by AC10 and AC11.
  **Readers:** by name: `tools/settings-merge.py`, `tools/govkit/entries/settings-merge.kit.toml`
  · by value: `tools/govkit/entries/settings-merge.kit.toml`, whose merged-region `block_id` matches
  the wired command and whose code-2 `[[outcome]]` probe names the hook it could not resolve;
  `tools/govkit/matrix.py`, whose settings-merge exit-2 rows derive the hook's landed path.
  Retired with it: the built-in `AGENT_CAP` fragment, `HOOK_MARKER`, `NO_HOOKS_KIT`,
  `_resolve_agent_cap_dir` and `_resolve_agent_cap_hook_path` in `tools/settings-merge.py`.
- **S7** — The upgrade step `agent-cap/spawn-guard-to-roles-pack` (brief I21), an `[[upgrade]]` row
  in `tools/hooks/kit.toml` whose program is `tools/govkit/steps/spawn_guard_pack.py` (§4 "The step").
  Its up wires the pack before it unwires agent-cap, and its down restores the settings file
  byte-identical. Observed by AC12 and AC13.
- **S8** — The retirement. `tools/hooks/agent-cap.js` and `tools/hooks/agent-cap.test.sh` are deleted,
  and the leg `agent-cap self-test` retires with its `[[exempt_leg]]` declaration (S5). The hooks kit keeps its
  registry id `agent-cap` (§8 F5), and its `version_from` moves to a `KIT_AGENT_CAP_VERSION` constant
  in `tools/hooks/scratch-guard.js` that continues the kit's version sequence. Every reader is
  disposed in the pass's commit (§4 "Readers disposed"). The by-name readers below are what
  `git grep -l -F 'agent-cap.js'` printed at base `4ed9e567`, re-derived by the same command at the
  build run's base, and the leg's readers what `git grep -l -F 'agent-cap self-test'` printed.
  Observed by AC14 and AC16.
  **Readers:** by name: `tools/hooks/agent-cap.test.sh`, the retired suite, deleted with the file, its
  arms over moved rules carried into S5's suite (AC8); `.claude/rules/product.md`,
  `.claude/settings.json`, `.lexicon.conf`,
  `README.md`, `WIRE-INTO-PROJECT.md`, `tools/check-agent-cap-restatement.sh`,
  `tools/check-agent-cap-restatement.test.sh`, `tools/check-hook-destinations.test.sh`,
  `tools/check-kit-versions.sh`, `tools/check-playbook-parity.sh`, `tools/check-playbook-parity.test.sh`,
  `tools/check-wiring.sh`, `tools/check-wiring.test.sh`, `tools/codebase-map/map_lib.py`,
  `tools/drift-audit/README.md`, `tools/govkit/entries/settings-merge.kit.toml`, `tools/govkit/govkit.py`,
  `tools/govkit/matrix.py`, `tools/govkit/selftest.py`, `tools/hooks/README.md`,
  `tools/hooks/format-guard.js`, `tools/hooks/kit.toml`, `tools/hooks/scratch-guard.js`,
  `tools/roles/README.md`, `tools/roles/adopt-roles.test.sh`, `tools/roles/workflows.toml`,
  `tools/settings-merge.py`, `tools/workflows/README.md`, `tools/workflows/REVIEW-PROTOCOL.template.md`,
  `tools/workflows/check-protocol-parity.test.sh`, `tools/workflows/check-review-join.sh`,
  `tools/workflows/check-review-join.test.sh`, `tools/workflows/check-verifier-fanout.sh`,
  `tools/workflows/check-verifier-fanout.test.sh`, `tools/workflows/drift-audit-code.template.js`,
  `tools/workflows/drift-audit-state.template.js`, `tools/workflows/orient-counterfactual.js`,
  `tools/workflows/tier2-review.template.js`, `tools/workflows/unattended-build.template.js`,
  `tools/workflows/unattended-build.test.sh`, `memory/guides/MERGE-BAR.md`,
  `memory/guides/REVIEW-PROTOCOL.md`, `memory/map/features/agent-cap.md`,
  `memory/map/features/review-harnesses.md`, `memory/map/features/unattended.md`; the leg's:
  `tools/gate-legs.json`, `tools/govkit/registry.toml`, `tools/govkit/subject-pins.tsv`,
  `tools/run-gates/ceiling-evidence.txt`, `tools/run-gates/run-selftests.sh`,
  `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/windows-only-legs.txt`; and the charter's
  agent-cap line in `coding-governance-agents.template.md`, rendered into `AGENTS.md`
  · by value: `.claude/settings.json`'s wired `Workflow|Agent` command, which runs the file;
  `tools/hooks/kit.toml`'s `version_from`, from which the kit version is read; `tools/check-kit-versions.sh`,
  which compares `KIT_AGENT_CAP_VERSION` with every `gov:kit agent-cap@` marker;
  `tools/check-playbook-parity.sh`'s rows extracting `MAX_LENSES` and `MAX_VERIFIERS` from the file;
  every `resolve_kit_dir` call anchoring the hooks kit on `agent-cap.js` (`tools/check-playbook-parity.sh`,
  `tools/check-kit-versions.sh`, `tools/govkit/selftest.py`'s `KIT_DIRS`, `tools/check-wiring.sh`'s
  `KIT_FILE_PAIRS`); `tools/govkit/matrix.py`'s settings-merge exit-2 rows; `tools/check-wiring.sh`'s
  agent-cap arm; the review kit's modules importing the file's exports (TOOL-dFairHearing-16 S1); the
  `resolveKitDir` slice `tools/lib/resolve-python.test.sh` cuts from the file (TOOL-dFairHearing-32
  S26); and the charter line, which names the hook as a rule an agent obeys.
- **S9** — The charter line. The `<!-- kit:agent-cap -->` block of `coding-governance-agents.template.md`
  (`:135-138`) loses its agent-cap hook line. The `<!-- kit:roles -->` block gains one line naming the
  spawn guard and the landed-blob rule, and `AGENTS.md` is re-rendered. Observed by AC15.
- **S10** — The records. `help/roles.md`'s "What the hooks refuse" names the landed-blob refusal and
  the pack, and `tools/roles/README.md` and `tools/hooks/README.md` say where each moved rule lives.
  Observed by AC17.

## 3. Non-goals (OUT)

- Changing what a moved rule refuses. Each rule moves with its predicate and its deny text, the prefix
  aside. TOOL-dBoundRoles-6's `role-sha` compare and absent-index refusal, -4's `checkFraming`,
  -10's `resolvePromptsAuthor`, -16's shape reading, -17's `item=` group and -20's composition
  reading move as those units leave them.
- The agent limit, the slot ledger, rules 1, 3 and 4 and the clamp: TOOL-dGroundRules-10's. Rules 0, 2
  and 5 and their homes: TOOL-dFairHearing-16's.
- Act binding of a Workflow call's roles, efforts and fan: dWellOiledMachine's.
- Renaming the hooks kit's registry entry `agent-cap` (§8 F5).
- Typed refusal records for hook denies. TOOL-dBoundRoles-26 types role returns. A deny here names its
  remedy's actor in prose.
- Withdrawing an adopter's installed `{prefix}/hooks/agent-cap.js`: govkit's existing withdrawn arm
  does that under `--write-withdrawals`, once the step has moved the wired command.

### Edges

- **consumes-from** `TOOL-dBoundRoles-6` — the per-role `role-sha` in the index and its compare at spawn, which this unit moves into the pack; without it the moved guard compares nothing and AC2 has no case
- **consumes-from** `TOOL-dBoundRoles-16` — the per-role `shapes` and the stage map the harness-call check reads, moved with it; without them AC3 has no case
- **consumes-from** `TOOL-dBoundRoles-20` — `harnesses`, the role index's list of held harnesses the composition renders, which the moved `checkHarnessCall` matches a `scriptPath` against before S3's landed-blob compare
- **consumes-from** `TOOL-dBoundRoles-38` — the fence-aware marker and fact readers in `checkHandoffSpawn` and `readUnfencedLines` in `scratch-guard.js`'s exports, which the move carries as it finds them (id 52 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-42` — the deletion, S8's readers and AC14, whose `memory/` readers unit 42 classes and whose live-carrier population it restates (id 42 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-43` — the pack, the retirement and its step, whose AC3, hook policy reads, registries and rule-7 refusal unit 43 completes (ids 2, 19, 27, 44, 45 and 61 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-44` — the retirement, S8's readers and the close, whose memory half, frozen receipt, gotcha pages and harness swap unit 44 completes (ids 3, 26, 43 and 62 of the round-1 spec audit)
- **consumes-from** `TOOL-dBoundRoles-46` — `TYPED_INPUTS` and the typed-block check in `checkHandoffSpawn`, which the move carries as it finds them (id 1 of the round-1 audit of units 37 to 44)
- **consumes-from** `TOOL-dBoundRoles-48` — the block-fence check in `checkHandoffSpawn`, which the move carries as it finds it (id 34 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-50` — the leg rename, which this pass also makes on the §7 leg line of every non-terminal spec of this build naming `agent-cap self-test`, units 43 and 50, each a rev bump with its §9 line; and the deleted suite's spawn-idiom registry rows, which unit 50 answers (ids 4, 27, 29 and 33 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-58` — the moved guard in `tools/roles/spawn-guard.js` and its export inventory, where unit 58 lands its spawn-side items, and AC14, which unit 58 bumps for unit 51's amended answer (ids 8, 9, 10, 15, 21, 22, 32, 33 and 48 of the round-1 audit of units 45 to 51)

## 4. Design

### Evidence at base `4ed9e567`

- Rule 6 is `checkHandoffSpawn` (`tools/hooks/agent-cap.js:2089-2149`) and `checkHarnessCall`
  (:2157-2188) over `HANDOFF_MARK_RE` (:2044). `main()` runs it at :2269-2295, importing
  `loadRoleIndex`, `resolveRoleRoot` and `buildComparablePath` from `tools/hooks/scratch-guard.js`
  (:952, :1396, :166, exported at :1615).
- Admission matches the path only: `checkHarnessCall` resolves `scriptPath` to a root-relative path
  and compares it with the index's `harnesses` list (:2166-2175). Nothing reads the file's bytes.
- `main()` is called unguarded at :2427. scratch-guard runs `main()` only as the entry point (:1614).
- The hooks kit's descriptor is registry entry `agent-cap` (`tools/hooks/kit.toml:3`). Its version is
  `agent-cap.js`'s constant (:6), and the file ships as engine (:21-24).
- settings-merge wires agent-cap as its built-in default: `HOOK_MARKER` (`tools/settings-merge.py:117`),
  `AGENT_CAP` (:231-242). Its descriptor's merged region is
  `hooks.PreToolUse[matcher]/hooks[command~agent-cap.js]`
  (`tools/govkit/entries/settings-merge.kit.toml:22`). The hooks kit's adopter runs it (`[adopt] via =
  "settings-merge"`, `tools/hooks/kit.toml:102-116`).
- Gov's wiring: `.claude/settings.json:4-12`.
- Parents change the file before this unit runs. TOOL-dGroundRules-10 S4 retires rules 1, 3 and 4 and
  adds rule 7. TOOL-dFairHearing-16 S1 to S4 move rules 0, 2 and 5 and export shared helpers.
  TOOL-dFairHearing-32 S25 adds `resolveKitDir` and `checkOptinPackPresent`. All are DEFERRED at
  `4ed9e567`, which is why S1 inventories at the build run's base.

### Disposition

| What S1 finds | Its home |
|---|---|
| rule 6, the spawn guard and harness admission, with `HANDOFF_MARK_RE`, the JS copy of `MARKER_RE` (brief I5), whose home TOOL-dBoundRoles-17 leaves to this unit | `tools/roles/spawn-guard.js` |
| rule 7, the settings in force | `tools/roles/spawn-guard.js` (brief D4) |
| any other check `main()` runs on the call, `checkOptinPackPresent` among them | `tools/roles/spawn-guard.js`, unchanged, in `main()`'s order |
| `resolveKitDir` and `resolveHarnessName` | `tools/roles/spawn-guard.js`, between the same `// >>> resolveKitDir` markers, so `tools/lib/resolve-python.test.sh` re-points its slice and its truth table runs unchanged |
| an export only review-kit modules import (the script views, `boundedK`, `intConsts`, `joinCall`, `topLevelArgs`, `MAX_VERIFIERS`, `MAX_LENSES`) | `tools/workflows/script-views.js`, a new review-kit module; `check-verifier-fanout.js` and `check-review-join.js` import it from beside themselves |
| an export imported by the pack and by a review-kit module (`extractWorkflowArgs`, `extractBuildSlug`) | `tools/hooks/scratch-guard.js`'s `module.exports`, over S4's declared edge |
| an export no file imports | deleted |

The pack and `spec-audit-optin.js` already probe the hooks kit beside their own kit for
scratch-guard's readers, so the S4 rule adds no new probe. A pack that cannot load scratch-guard's
readers refuses every `Workflow` and `Agent` call, naming the hooks kit and the owner as the remedy's
actor. A guard that cannot read does not admit.

### Admission

For a `Workflow` call whose `scriptPath` already matched a declared harness at `rel`:

1. `L` is the landed revision, `readLandedRevision` from `tools/policy/policy-mirror.js`
   (TOOL-dGroundRules-5 S5), found in the policy kit beside the roles kit the way rule 7 finds the
   mirror. That is the one JS reader held equal to `derive_landed_revision` by that unit's
   `mirror-landed-parity` case. No policy kit, or a refusal from it, refuses the call naming the owner.
2. `landed` is `git -C <root> rev-parse --verify --quiet <L>:<rel>`. An empty answer refuses:
   `harness <rel> is not landed at <L8>; land it before running it`. The remedy's actor is the driver.
3. `worktree` is `git -C <root> hash-object -- <rel>`, which applies the repository's clean filters,
   so a CRLF checkout of an LF blob compares equal.
4. `landed != worktree` refuses: `harness <rel> differs from its blob at the landed revision <L8>; an
   edited harness runs only after it lands, so the bar has read it`. The remedy's actor is the driver.

The check runs after the declared-harness match and before the `args.roles` checks, so a call
refused for its path pays no git call. Two `git` subprocesses per admitted call is the cost. An
uncommitted edit and a committed but unlanded edit are refused alike: the design accepts that an
in-build harness edit waits for landing (`research-stall-refusals.md` row V17, §8 F2).

### The step

```toml
# tools/hooks/kit.toml
[[upgrade]]
id = "agent-cap/spawn-guard-to-roles-pack"
up = ["python", "{gov}/govkit/steps/spawn_guard_pack.py", "up", "{target}", "{prefix}"]
down = ["python", "{gov}/govkit/steps/spawn_guard_pack.py", "down", "{target}", "{prefix}"]
witness = ["python", "{gov}/govkit/steps/spawn_guard_pack.py", "witness", "{target}", "{prefix}"]
surfaces = ["installable:{prefix}/hooks/agent-cap.js", "file:{prefix}/hooks/agent-cap.js"]
needs-target = true
```

**up.** With no command naming `agent-cap.js` in the target's `.claude/settings.json` it exits 0.
Otherwise it writes the before-image of that file through TOOL-dSafePassage-1's helper. Where the
target installs the roles kit, it runs the target's `settings-merge.py --fragment
<roles kit>/spawn-guard.fragment.json` first. Then it runs `settings-merge.py --fragment <tmp> --unwire`,
where `<tmp>` is a fragment for agent-cap's entry written under `tempfile.mkdtemp`, carrying the
marker `agent-cap.js` and the hook path the target's receipt records. Wiring first means a killed up
leaves both hooks wired, never neither. The order is the one `tools/hooks/kit.toml:18-20` records
for a moved security guard. A target without the roles kit loses the guard, which matches what it
had: rule 6 is armed only by a role index.

**witness.** It exits 0 when no command naming `agent-cap.js` is wired, and, where the roles kit is
installed, the `Workflow|Agent` group carries the `spawn-guard.js` marker.

**down.** It restores `.claude/settings.json` from the before-image under TOOL-dSafePassage-1's rule.

### Readers disposed

The pass re-derives S8's readers at the build run's base. Each is disposed in the commit, by class:

| Class | Disposition |
|---|---|
| the wiring: `.claude/settings.json`, settings-merge and its descriptor | re-pointed to the pack (S6); gov's tree runs S7's up first (P38) |
| a hooks-kit anchor (`resolve_kit_dir ... hooks agent-cap.js`, `KIT_FILE_PAIRS`, `KIT_DIRS`) | anchored on `scratch-guard.js` |
| the version: `version_from`, `tools/check-kit-versions.sh`, the `gov:kit agent-cap@` markers | the constant in `scratch-guard.js`; the checker reads that file |
| a constant extracted from the file (`tools/check-playbook-parity.sh`) | extracted from the file S4 moved it to |
| a fixture copying the file (`tools/govkit/selftest.py`, `tools/check-hook-destinations.test.sh`, `tools/check-wiring.test.sh`) | copies `scratch-guard.js`, or the pack where the case is about the spawn guard |
| the leg and its rows | renamed `spawn-guard self-test` in its declaration and re-rendered (S5), run from the roles kit; its budget, evidence and pin rows re-keyed, its ceiling and budget re-measured at the pass |
| prose and comments | name the pack, `scratch-guard.js` or the moved rule's new home |
| a harness template's comment | re-rendered with its template, which moves that harness's blob (§5 risks) |
| the dossiers | `memory/map/features/agent-cap.md` drops the file; `memory/map/features/roles.md` claims the pack, re-rendered by `python tools/codebase-map/gen_map.py --write` |

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `checkHarnessLanded`, `readHarnessBlobs` | `tools/roles/spawn-guard.js` | `js.function` camel, asked of `python tools/lexicon/lexicon.py --suggest <name> --as js.function` at the pass |
| the module `tools/workflows/script-views.js` | the review kit | — |
| `cmd_up`, `cmd_down`, `cmd_witness`, `main` | `tools/govkit/steps/spawn_guard_pack.py` | `py.function` snake |
| step id `agent-cap/spawn-guard-to-roles-pack` | the S7 row | — |
| leg `spawn-guard self-test` | an `[[exempt_leg]]` row of `tools/govkit/registry.toml`, rendered into `tools/gate-legs.json`: chunk `selftests`, subject `kit`, `enforces` the retired leg's, guard the pack's three files and `{prefix}/hooks/scratch-guard.js` | — |
| `KIT_AGENT_CAP_VERSION` re-homed | `tools/hooks/scratch-guard.js` | — |

### Rollout

The pack is live at the landing, wired in gov's tree in the same commit that deletes the hook, so the
spawn guard is never unenforced here. A session started before the edit reads the new hook once the
settings watcher catches it (`memory/gotchas/settings-edit-takes-effect-mid-session.md`).

**This build's own close.** Once this unit's pass is committed, a harness that any unit of this build
edited differs from its landed blob and is refused until landing. That holds for
`tools/workflows/tier2-review.js`, which the closing review runs. The main loop therefore runs the
closing review, and any promoted unit's harness, with each such harness at its landed bytes. It
writes `git show <L>:<rel>` over the working-tree file for the call and restores it with
`git checkout -- <rel>` after. The landed harness has passed the bar, so the rule holds for the
build's own close. The pass records in its acceptance ledger which harnesses this applies to, from
`git diff --name-only <BASE> HEAD` over the index's `harnesses`.

### Files touched (estimate)

- `tools/roles/spawn-guard.js` (new), `tools/roles/spawn-guard.fragment.json` (new),
  `tools/roles/spawn-guard.test.sh` (new)
- `tools/roles/kit.toml`, `tools/roles/README.md`, `tools/roles/workflows.toml`,
  `tools/roles/adopt-roles.test.sh`
- `tools/hooks/agent-cap.js` (removed), `tools/hooks/agent-cap.test.sh` (removed)
- `tools/hooks/scratch-guard.js`, `tools/hooks/scratch-guard.test.sh`, `tools/hooks/format-guard.js`,
  `tools/hooks/kit.toml`, `tools/hooks/README.md`
- `tools/workflows/script-views.js` (new), `tools/workflows/check-verifier-fanout.js`,
  `tools/workflows/check-review-join.js`, `tools/workflows/spec-audit-optin.js`
- `tools/workflows/check-verifier-fanout.sh`, `tools/workflows/check-verifier-fanout.test.sh`,
  `tools/workflows/check-review-join.sh`, `tools/workflows/check-review-join.test.sh`,
  `tools/workflows/check-protocol-parity.test.sh`, `tools/workflows/unattended-build.test.sh`
- `tools/workflows/kit.toml`, `tools/workflows/README.md`
- `tools/workflows/REVIEW-PROTOCOL.template.md`, with `memory/guides/REVIEW-PROTOCOL.md` its render
- `tools/workflows/tier2-review.template.js`, `tools/workflows/unattended-build.template.js`,
  `tools/workflows/drift-audit-code.template.js`, `tools/workflows/drift-audit-state.template.js`,
  with `tools/workflows/tier2-review.js`, `tools/workflows/unattended-build.js`,
  `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js` their renders;
  `tools/workflows/orient-counterfactual.js`
- `tools/govkit/steps/spawn_guard_pack.py` (new), `tools/govkit/selftest.py`,
  `tools/govkit/registry.toml`, `tools/govkit/govkit.py`, `tools/govkit/matrix.py`,
  `tools/govkit/subject-pins.tsv`, `tools/govkit/entries/settings-merge.kit.toml`
- `tools/settings-merge.py`
- `tools/check-wiring.sh`, `tools/check-wiring.test.sh`, `tools/check-kit-versions.sh`,
  `tools/check-playbook-parity.sh`, `tools/check-playbook-parity.test.sh`,
  `tools/check-hook-destinations.test.sh`, `tools/check-agent-cap-restatement.sh`,
  `tools/check-agent-cap-restatement.test.sh`, `tools/lib/resolve-python.test.sh`
- `tools/gate-legs.json` (rendered), `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/ceiling-evidence.txt`,
  `tools/run-gates/windows-only-legs.txt`, `tools/run-gates/run-selftests.sh`
- `tools/codebase-map/map_lib.py`, `tools/lexicon/lexicon.py`, `tools/drift-audit/README.md`,
  `.lexicon.conf`
- `.claude/settings.json`, `.claude/rules/product.md`
- `coding-governance-agents.template.md`, with `AGENTS.md` its render
- `README.md`, `WIRE-INTO-PROJECT.md`, `help/roles.md`
- `memory/guides/MERGE-BAR.md`, `memory/map/features/agent-cap.md`, `memory/map/features/roles.md`,
  `memory/map/features/review-harnesses.md`, `memory/map/features/unattended.md`

### Alternatives rejected

- **Admission against HEAD's blob.** It closes the uncommitted edit the gap names. It still runs a
  committed edit the bar has not read, which is the run the clause refuses (§8 F2).
- **Rule 7 into a policy-kit pack.** That is a third hook pack on `Workflow|Agent` the clause does not
  name. Brief D4 placed it with the guard (§8 F1).
- **The script views copied into each review-kit gate.** That would be two scanners of one script, the
  drift TOOL-dFairHearing-16 §4 rejected (§8 F3).

## 5. Production-readiness checklist

- security — deny by default holds. A pack that cannot load its readers, cannot resolve the landed
  revision or cannot hash a harness refuses the call. The landed compare closes the window in which an
  edited harness ran unscanned (gap-roles-30). No rule is weakened in the move: S5 carries each moved
  arm. Wiring before unwiring keeps the guard present through a killed up.
- perf / scale — two `git` subprocesses per admitted `Workflow` call; an `Agent` call pays none.
- error / empty / loading states — no index, broken index, no policy kit, a harness absent at `L`, or
  a harness differing from `L`: each refuses with its reason and its remedy's actor.
- observability — each deny names the harness, `L`'s first eight hex digits and the remedy.
  `check-wiring.sh` prints the pack wired or UNWIRED.
- risks — a harness edited in a build cannot run until it lands, including this build's own harnesses.
  §4 Rollout gives the close's route. An adopter whose roles kit is absent loses rule 7 with rule 6.
  The renamed leg's ceiling is re-measured at the pass.
- testing — `tools/roles/spawn-guard.test.sh` and the step's selftest cases, each observed by a pass
  running the pack against fixture payloads; every new arm is observed RED then GREEN by the main loop
  at the close.
- migration — S7's step, gov's tree first.
- user docs — `help/roles.md`, S10.

## 6. Acceptance criteria

- **AC1** — When `node spawn-guard.js` reads an `Agent` payload whose prompt carries no `gov:handoff`
  marker, in a fixture tree with a role index, it exits 2 with stderr opening `BLOCKED by spawn-guard:`.
  A rendered handoff's payload exits 0.
  Red when: the pack admits the freeform prompt, or the rule never moved.
- **AC2** — When the payload's marker carries a `role-sha` other than the index's for that role, the
  pack exits 2 naming both values.
  Red when: the moved rule drops TOOL-dBoundRoles-6's compare.
  fixture: needs TOOL-dBoundRoles-6 at the build run's base.
- **AC3** — When a `Workflow` payload's `args.roles` names a role whose index `shapes` lacks the
  harness entry's `kind`, the pack exits 2.
  Red when: the moved check stops reading TOOL-dBoundRoles-16's `shapes`.
  fixture: needs TOOL-dBoundRoles-16 at the build run's base.
- **AC4** — When a fixture repository with a bare remote whose `main` holds a declared harness has
  that harness edited in the working tree, the pack exits 2 on a `Workflow` call naming it, and stderr
  names the path and `L`'s sha8. Committing the edit without pushing still exits 2. Restoring the
  landed bytes exits 0.
  Red when: admission compares against HEAD, or by path alone, so the committed edit is admitted.
- **AC5** — When the declared harness exists in the working tree and not at `L`, the pack exits 2 with
  `is not landed`.
  Red when: a missing landed blob is read as equal.
- **AC6** — When a fixture adopter installs the kits at prefix `scripts`, its index naming the review
  harness `tier2-review.js` under that prefix, and that file is landed, a `Workflow` call whose
  `scriptPath` names it exits 0 (gap-roles-25). A CRLF checkout of the same LF blob also exits 0.
  Red when: the pack refuses gov's own harness in an adopter install, or compares raw bytes.
- **AC7** — When rule 7's planted settings set `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` above the landed
  `runtime.agents-in-flight`, the pack exits 2 naming the file and both numbers.
  Red when: rule 7 was left behind or dropped.
  fixture: needs TOOL-dGroundRules-10 at the build run's base.
- **AC8** — When the pass's ledger lists every arm the retired hook's suite held over a moved rule at
  the build run's base, each with its payload and its exit, each listed payload piped to
  `node spawn-guard.js` in the fixture tree exits as the ledger records, a deny's stderr opening
  `BLOCKED by spawn-guard:`. The suite that carries the arms is §7's New arm.
  Red when: an arm over a moved rule was not carried, so its payload exits otherwise in the pack.
- **AC9** — When `node -e` requires `tools/hooks/scratch-guard.js` and the new `script-views.js`, the
  first exports `extractWorkflowArgs` and `extractBuildSlug` as functions and the second exports the
  script views. `node check-verifier-fanout.js` and `node check-review-join.js` over the shipped
  harnesses exit 0 with `agent-cap.js` absent. Every row of S1's ledger inventory names its home.
  Red when: a review-kit module still requires the deleted file and exits 2.
- **AC10** — When `python -c` reads gov's `.claude/settings.json`, the `Workflow|Agent` group carries
  a command naming `spawn-guard.js` and none naming `agent-cap.js`. `bash tools/check-wiring.sh` prints
  the pack wired. With that entry removed from a scratch copy, it prints `UNWIRED` naming the pack.
  Red when: the pack's fragment is graded by no arm.
- **AC11** — When `python settings-merge.py` runs with no `--fragment` in a scratch target holding the
  roles kit, it wires the command `spawn-guard.fragment.json` declares. In a target without the roles
  kit, it exits 2.
  Red when: settings-merge still carries a built-in fragment, so the default wires a deleted hook.
- **AC12** — When a scratch target whose settings wire `agent-cap.js` runs the step's `up` argv, its
  settings wire `spawn-guard.js` and no `agent-cap.js` command, and the `witness` argv exits 0 where it
  exited 1 before. An up killed after its wire call leaves both commands wired.
  Red when: the up unwires before it wires, so a killed up leaves no guard.
- **AC13** — When the `down` argv runs after the up, `.claude/settings.json` is byte-identical to the
  before state, compared with `cmp`. When that file was edited after the up, the down exits 1 naming
  it.
  Red when: a byte differs, or the edit is overwritten.
- **AC14** — When the pass is committed, `git ls-files tools/hooks/agent-cap.js tools/hooks/agent-cap.test.sh`
  prints nothing. `git grep -l -F 'agent-cap.js' -- ':!memory/builds' ':!memory/ledger' ':!.governance/steps'`
  prints only `tools/hooks/kit.toml`, govkit's self-test module, whose step cases (§7's New arm)
  spell the old file, the step program and files under `tools/govkit/fixtures`. `grep -c 'KIT_AGENT_CAP_VERSION = ' tools/hooks/scratch-guard.js` prints 1.
  Red when: a live reader still names the deleted file, or `version_from` names a file that is gone.
- **AC15** — When `grep -n -A3 'kit:roles' coding-governance-agents.template.md` runs, the roles block
  holds the spawn-guard line. `grep -c 'agent-cap hook' AGENTS.md` prints 0.
  Red when: the charter still tells an agent about a hook that no longer exists.
- **AC16** — When `python step_gate.py --base <the pass's parent sha>` runs on the committed tree, no
  `RED` line names `agent-cap.js`.
  Red when: the S7 row's `surfaces` omits a member.
  fixture: needs TOOL-dSafePassage-10's gate at the build run's base.
- **AC17** — When `grep -n 'landed' help/roles.md` runs, it prints the line naming the landed-blob
  refusal under "What the hooks refuse".
  Red when: the page still lists only a path match.
- **AC18** — When `python tools/run-gates/leg_factory.py --list` runs on the committed tree, it prints
  `spawn-guard self-test` declared in `tools/govkit/registry.toml` and no `agent-cap self-test`; `--check`
  exits 0, and the leg's manifest row carries a non-empty `enforces`.
  Red when: the leg is a hand-written manifest row, or carries no `enforces`.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `hook destinations self-test` · `check-wiring self-test` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `verifier fan-out self-test` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `playbook parity selftest` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `codebase-map kit selftest` · `drift-audit selftest` · `lexicon naming predicates` · `lexicon selftest` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `run-selftests self-test` · `straggler-guard arms` · `transition-audit arms` · `recall floor` · `recall floor arms` · `roles catalogue` · `roles render wiring` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass's files trip the guard of `agent-cap self-test` at the base, so the leg is named, and the
pass retires it into `spawn-guard self-test`.

New arm: tools/roles/spawn-guard.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · each moved arm's planted payload, plus a fixture remote whose landed harness the working tree edits, a harness absent at the landed revision, and an adopter layout at prefix `scripts` · `tools/run-gates/selftest-budgets.txt`, the renamed leg's row re-measured
New arm: tools/govkit/selftest.py · covers AC11 AC12 AC13 · a scratch target wiring `agent-cap.js`, an up killed after its wire call, an edit after the up · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by the measured count of new refusal sites
New arm: tools/check-wiring.test.sh · covers AC10 · a scratch settings file with the pack's entry removed · none

## 8. Open questions

- **F1 — Where does rule 7, the settings in force, go?** No record names its home (brief D4; scout C,
  note on rule 7). Options: (a) the roles pack, beside the guard, both judging the same
  `Workflow|Agent` call; (b) a policy-kit pack of its own; (c) stay in agent-cap, which then never
  retires. (c) fails the clause's "once its last rule has moved". (b) adds a hook pack and its wiring,
  a public surface no clause of this build names (veto 2). RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3, as brief D4 settles. widens: none · relaxes: none
- **F2 — Which revision does admission compare a harness with?** Options: (a) the landed revision, so
  an uncommitted edit and a committed but unlanded edit are both refused; (b) HEAD, which refuses only
  an uncommitted edit; (c) the landed revision, with an edited harness admitted after the bar's harness
  checks pass on it at call time. The clause says "its landed blob so an edited harness never runs
  before the bar has read it". The design accepts that an in-build harness edit waits for landing
  (`research-stall-refusals.md` V17). (b) and (c) are looser mechanisms and would each be a departure.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 1. This build's own close runs edited harnesses at
  their landed bytes, as §4 Rollout gives. widens: none · relaxes: none
- **F3 — Where do the helpers agent-cap exports go once it is deleted?** TOOL-dFairHearing-16 §3 hands
  their "last home" to this build. Options: (a) by importer: one kit's helpers into that kit, two
  kits' into `scratch-guard.js`'s exports; (b) all into the pack; (c) all into `scratch-guard.js`;
  (d) the two kits' helpers as a `tools/lib/` canonical block inlined into each under a parity row.
  (b) makes the review kit import the roles kit for a script lexer it alone reads. (c) loads a lexer
  of about a thousand lines into a hook that runs on every Bash and Edit call. The rev-1 pick, (a),
  left the pack's require of `scratch-guard.js` undeclared, which PLAY-dOrderedCharter-7 §4 rules out
  ("A kit may not import a sibling kit"). (d) moves two exports but not rule 6's index readers, which
  the pack reads from the same file, and the parity loop greps `#` markers in `.sh` and `.py` only
  (`tools/lib/resolve-python.test.sh:226`). RESOLVED (agent, 2026-10-26, delegated): (a), rung 1,
  naming PLAY-dOrderedCharter-7, the pack's one in-process edge declared as S4's `requires_if` row,
  the declaration the rule admits (`tools/memory-tree/kit.toml:8`). widens: none · relaxes: none
- **F4 — What does settings-merge wire with no `--fragment` once agent-cap is gone?** Options: (a) the
  roles kit's `spawn-guard.fragment.json`, read from its file; (b) nothing, `--fragment` required;
  (c) a built-in copy of the pack's fragment. (b) breaks the hooks kit's `[adopt] via =
  "settings-merge"` and settings-merge's own adopter argv, and changes its descriptor's outcome
  contract. (c) states the fragment twice. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. The
  hooks kit's `[adopt]` is unchanged, and the descriptor's `block_id` and code-2 outcome name
  `spawn-guard.js`. widens: none · relaxes: none
- **F5 — Does the hooks kit's registry id `agent-cap` retire with the file?** Options: (a) keep the id,
  with its version moved to `scratch-guard.js`; (b) retire it to a successor entry through a
  `[[retired]]` row. (b) changes every adopter's receipt, `.governance/deploy.toml`'s `kits`, the
  charter's `kit:agent-cap` block and the matrix rows, which is a public surface the clause does not
  name. The clause retires the file. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. A rename
  is a later build's to propose. widens: none · relaxes: none
- **FACT-QUESTION · F6 — Are the parent sections this unit calls present?** Probe: at the build run's
  base, `grep -n 'RULE [0-9]' tools/hooks/agent-cap.js`, `grep -n 'module.exports'` over it, and
  `git ls-files tools/policy/policy-mirror.js tools/govkit/upgrade_steps.py tools/govkit/step_gate.py
  tools/workflows/spec-audit-optin.js`. Observation at `4ed9e567`: the file runs rules 0 to 6, exports
  nothing, and none of the four files exists. Liveness: TOOL-dGroundRules-10, TOOL-dFairHearing-16,
  TOOL-dGroundRules-5 and TOOL-dSafePassage-1 each name these changes in their Files touched, so the
  probe moves when they land. RESOLVED (agent, 2026-10-25, delegated): the build run re-grounds on each.
  It stops this unit if a rule S1 finds has no row in §4's disposition table, if rules 1, 3, 4, 0, 2
  or 5 are still in the file, or if TOOL-dSafePassage-1 S1-S3 or TOOL-dGroundRules-5 S5 is absent.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 25, the brief's I4, I5, I21, I24 and D4,
  scout C's row for cl-0190, the night pass two's point 7, and TOOL-dGroundRules-10, TOOL-dFairHearing-16
  and -32 and TOOL-dSafePassage-1 and -10 at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **consumes-from** and **hands-off** bullets mirroring the edges of TOOL-dBoundRoles-38, TOOL-dBoundRoles-42, TOOL-dBoundRoles-43, TOOL-dBoundRoles-44, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-46, -48 and -50, promotions of the round-1 audit of units 37 to 44; the -50 bullet hands this pass the leg rename on two live §7 lines. Nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-58, the minors batch of the round-1 audit of units 45 to 51; nothing else moved.
- rev-5 · 2026-10-26 · S4 · S5 · S8 · §4 Disposition, Readers disposed, Inventory, Files touched · AC18 ·
  §8 F3 · re-grounded by `build/2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md` rows 44
  and 45: the renamed leg is declared once through TOOL-dWitnessedBar-11's factory with `enforces`,
  the manifest rendered; the pack's require of `scratch-guard.js` is a declared `requires_if` edge, F3
  re-resolved.

## 10. Reuse audit

The seams extended are four. The first is TOOL-dFairHearing-16 S4's hook-pack layout: a `.js` hook
plus its `.fragment.json`, wired by `tools/settings-merge.py --fragment` and graded by
`tools/check-wiring.sh`. The second is `tools/hooks/scratch-guard.js`'s export surface (`:1615`), which
rule 6 already imports. The third is TOOL-dSafePassage-1's upgrade-step kind with its S6 step on the
same descriptor as precedent. The fourth is TOOL-dGroundRules-5's `readLandedRevision`, the one JS
reader of the landed revision. Every parent seam is specced and DEFERRED at `4ed9e567`.
`python tools/codebase-map/reuse_lookup.py "move a PreToolUse guard rule into another kit's hook pack
and retire the old hook file"` ranked `resolve_kit_dir` (72 installs), the kit-anchor seam the
readers table re-points, and the three `PreToolUse` hooks of the harness inventory. No ranked name
compares a harness with a landed blob, so no seam fits that compare beyond `readLandedRevision` plus
git's own blob id. `blob_oid` (`tools/govkit/govkit.py:6725`, scout C) is Python. The pack is JS and
`git hash-object` applies the clean filters, which a raw hash would not. The recall probe returned
scout C's row, the night pass two's NT-27 table and `research-agent-cap.md` §5. Scout C read 63 files
naming `agent-cap`. That count includes the separate `check-agent-cap-restatement` kit and the
registry id. The file name `agent-cap.js` is spelled by the narrower set S8 lists.

Recall terms used: `python tools/memory-recall/query.py "where does agent-cap's handoff spawn guard and harness admission go when the hook retires" --terms "agent-cap rule 6 spawn guard harness admission landed blob roles pack fragment retire hook upgrade step readers"`
