# PLAY-dOrderedCharter-11 — load sets derived per reader and item, budgeted, and refused when a required unit is missing

**Status:** CLOSED · rev-9 · 2026-11-08 · node d · Tier-2 · base ce13efbe · streams playbook · order 21 · closes PLAY-dOrderedCharter-57 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0041@29cae3c8 whole
**Carries:** node:policy-key.instructions.checks

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-27 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-build-PLAY-dOrderedCharter-11-deviation-111.md](../build/2026-10-24-build-PLAY-dOrderedCharter-11-deviation-111.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-11-deviation-112.md](../build/2026-10-24-build-PLAY-dOrderedCharter-11-deviation-112.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 |
| [2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-25-build-PLAY-dOrderedCharter-11-deviation-113.md](../build/2026-10-25-build-PLAY-dOrderedCharter-11-deviation-113.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-11-deviation-114.md](../build/2026-10-25-build-PLAY-dOrderedCharter-11-deviation-114.md) | deviation | — |
| [2026-11-02-build-PLAY-dOrderedCharter-11-ledger.md](../build/2026-11-02-build-PLAY-dOrderedCharter-11-ledger.md) | journal | — |
| [2026-11-08-build-PLAY-dOrderedCharter-11-1-builder-return.md](../build/2026-11-08-build-PLAY-dOrderedCharter-11-1-builder-return.md) | journal | — |
| [2026-11-08-build-PLAY-dOrderedCharter-11-deviation-115.md](../build/2026-11-08-build-PLAY-dOrderedCharter-11-deviation-115.md) | deviation | — |
| [2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md](../build/2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-11-1-spec-writer.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-11-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md](../prompts/2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-46 |
| [2026-11-02-prompt-PLAY-dOrderedCharter-11-build-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-11-build-brief.md) | journal | — |
| [2026-11-02-prompt-PLAY-dOrderedCharter-17-ask-fold-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-17-ask-fold-brief.md) | research | PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-42 |
| [2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md) | research | PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-11-04-prompt-PLAY-dOrderedCharter-52-drift-sweep-brief.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-52-drift-sweep-brief.md) | research | PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 |
| [2026-11-08-prompt-PLAY-dOrderedCharter-3-drift-fold-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-3-drift-fold-brief.md) | research | PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

No load set is computed per reader, six load points carry budgets and the rest none, and no injected
load point is measured (gap-found-10); and the one switch that held the missing-unit refusal also held
the size budget, so loosening one loosened the other (gap-found-34). This unit derives each reader's
load set from the instruction-unit rows, refuses a set missing a unit its `required-by` names as
`instructions.checks` says, still refused under `budgets.enforce`'s `warn`, measures each rendered load
point against its cap under `budgets.*` and its harness's limit, and measures the injected load points
at session start (layer-instruction R-C, v2:973-981 P27, v2:1242, the owner's NT-22, the whole-design
audit's C1-F1 and C1-F14).

## 2. Scope (IN)

- **S1** — The load set. `derive_load_set(units, reader, item=None, features=())` in a new module
  `tools/playbook/load_sets.py` returns, from S10's rows read through `tools/playbook/instruction_units.py`,
  the units whose `scope` selects every reader (`reader.every`), the reader's role, and its item. The
  role selects by a practice tag its `rules:` value cites, and by its `role.<name>` selector once
  `tools/playbook/namespaces.toml` holds a `role` row whose `role` is `selects`; at `c7269a97` it holds
  none (its rows are `doc`, `unit`, `reader`, `practice`, `level`, `layer`, `principle`, `kind`, `kit`
  and `repo`), so the role-selector part selects nothing and is reported `unarmed — role.*: no role
  namespace is registered`, never empty and green, until a unit registers one (the fork record's F5).
  The item and step selectors are
  dDeclaredLoop's namespaces: until it registers them the item part is reported `unarmed`, never empty
  and green. `features` holds the work order's `feature.*` tags, by which `TOOL-dFurnishedOrders-18`
  selects its units: a unit whose `scope` carries a tag in `features` joins the set once
  `tools/playbook/namespaces.toml` (PLAY-dOrderedCharter-19 S2), read through `read_namespaces`
  (`tools/playbook/tag_index.py#read_namespaces`), holds a
  `feature` row whose `role` is `selects` (TOOL-dLinkedLibrary-20 S1); while it holds none, the feature
  part selects nothing and is reported `unarmed — feature.*: no feature namespace is registered`, never
  empty and green. Observed by AC1 and AC7.
- **S2** — The missing-unit refusal. `check_required(load_set, units, reader, item, mode)` names every
  unit whose `required-by` names the reader's role or its item and which the set lacks. `mode` is
  `instructions.checks`: `refuse` (default) leaves the render undone and exits 1 naming each unit;
  `warn` renders the whole set and puts a `Missing required unit: <tag>` line where the reader sees it;
  `record` renders and writes the gap into the prompt record's `**Load gaps:**` line only. No value
  skips the check (foundations C6, LR-1). `budgets.enforce` is never read here, so `warn` there leaves
  the refusal standing. A unit required by a role whose selector part is `unarmed` is absent from the
  set and so missing, the fail-closed side. The key is read with `policy.py get instructions.checks`
  through unit 19's `read_policy_value` (`tools/playbook/policy_value.py#read_policy_value`), the
  playbook kit's one subprocess caller of that verb, called with the key literal first,
  `read_policy_value("instructions.checks", root)`, the call shape dGroundRules' reader-coverage arm
  counts (TOOL-dGroundRules-8, its Readers table). It reads the target's committed policy at its landed
  revision, and an unset key answers the catalogue default `refuse` with its reason
  (TOOL-dGroundRules-2 S7, TOOL-dGroundRules-3 S2); on `PolicyRefused`, which the reader raises on its
  exit 2 and with no policy kit found, the check runs as `refuse` and prints the exception's `line`
  once (the fork record's F4). The key's catalogue row
  lands with dGroundRules with no `summary` or `usage`, named on the shrink-only
  `tools/policy/unsummarised-keys.txt` (TOOL-dGroundRules-1 S3, S6): this unit adds no row; it fills that
  row's `summary` and its `usage`, a line the row admits (`instructions.checks = "warn"`), and drains the
  name with `python <prefix>/policy/policy.py lists --write` in the same commit. Observed by AC2, AC3
  and AC6.
- **S3** — The budgets. `check_budget(load_point, size, mode)` measures a rendered load point's bytes,
  CR stripped, of the committed blob, against its cap under `budgets.*`, which `budgets.py` answers
  from the cap's home in the census, for the charter its `AGENTS.md` row of
  `tools/template-size-limits.txt` read at the landed revision, a `budgets."<key>"` value in
  `.governance/policy.toml` taking a row's place. Each cap is named as the census `tools/policy/caps.toml` names it
  (TOOL-dGroundRules-9 S1): a load point's cap is the census row whose `name` is its repo-relative path,
  `AGENTS.md` for the charter and the path of each Skill that has one, read from the census with
  `tomllib` and never typed here; a role block's is `role-body`, a family cap whose value stays
  `BODY_CEILINGS` (`tools/roles/check_roles.py:85-89`, now `tools/roles/check_roles.py#BODY_CEILINGS`)
  and whose mode alone is asked. One
  `python <prefix>/policy/budgets.py resolve <cap> …` subprocess per run, the policy kit found through
  the inlined `resolve_kit_dir`, answers each cap's value and its mode, `refuse` under
  `budgets.enforce = "refuse"` or a `budgets.pinned` name and `warn` otherwise (TOOL-dGroundRules-9 S2);
  over its cap a load point warns or refuses as that mode says. Per harness, a load point a harness
  reads whole carries that harness's limit as a second cap, today the charter under Codex's `CODEX_MAX`
  (32768), read with `python <prefix>/policy/budgets.py home codex-instructions`, the verb unit 6 adds
  to the policy kit, which prints the census row's `constant:` home and the constant's value, so the
  move unit 31 makes re-points the row and this read with it, and this unit never parses that row. A set over it is refused whatever the mode
  (R-C). A load point with no census row prints `no cap declared`, never a pass; on `budgets.py`'s
  exit 2 the render refuses printing the reader's line, and with no policy kit found the budget check
  prints `unarmed` naming it (§8 F4). The subprocess keeps the script and its verb as separate list
  elements, and no line of the module outside a comment spells the budgets script's name followed by a
  space and its verb: the policy check's cap census reads that sequence as a request and every word after
  it as a cap, which is how unit 73 found 30 English words requested in `tools/run-gates/owed_rows.py`.
  Observed by AC4.
- **S4** — The render calls. `render_handoff` (`tools/roles/handoff.py:312`, now
  `tools/roles/handoff.py#render_handoff`) and `render_agent_file`
  (`tools/roles/render_agents.py:144`) derive the role's load set and run S2 and S3 before writing;
  `render()` (`tools/playbook/render_playbook.py:979`, now `tools/playbook/render_playbook.py#render`)
  runs S3 over the charter. The roles kit finds
  `load_sets.py` through `resolve_kit_dir` and runs its `check` verb as a subprocess, as
  `derive_role_roster` finds and runs the roles kit's `roster` verb (`render_playbook.py:470-500`, now
  `tools/playbook/render_playbook.py#derive_role_roster`),
  since a kit may not import a sibling kit (TOOL-dGroundRules-1 §4 Evidence); with the playbook kit
  absent the check prints `unarmed` and the render proceeds. Observed by AC2.
- **S5** — The injected load points, measured. `python tools/playbook/load_sets.py injected` prints one
  line per injected load point the harness places from this repository, with its bytes and its cap or
  `no cap declared`, and a breach line when over: the agent list (each `description:` of
  `.claude/agents/*.md`), the Skill list (each `description:` of `.claude/skills/*/SKILL.md` and
  `skills/*/SKILL.md`) and the session-start hook's output (the card). The session-start card writer,
  `write_card` (`skills/session-kickoff/manifest-check.sh:706`), runs it and appends its breach lines,
  none when nothing is over. Observed by AC5.

## 3. Non-goals (OUT)

- The `budgets.*` keys, `budgets.enforce`, `budgets.pinned` and the policy reader: dGroundRules
  (v2:1346-1348). No cap value is set or moved here.
- The `code` slot in a role's load set: `PLAY-dOrderedCharter-27`.
- Each practice's reach for the step in a work order: `PLAY-dOrderedCharter-21`.
- The auto-memory index as an injected load point, and directives found in it:
  `PLAY-dOrderedCharter-14`.
- A composition over a harness's limit at update, and the project block's count:
  `PLAY-dOrderedCharter-34`.
- The item, step and policy selectors' joins: dDeclaredLoop. Registering a `role` namespace: no unit
  yet (the fork record's F5).
- The `derive` verb's `--feature` flag and the work order's feature units: `TOOL-dFurnishedOrders-18`. The work order's packet budget:
  dBoundRoles.
- Field loads measured from the roles' runs (R-C): no run measurement exists to read.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-9` — S10's unit rows and their `required-by` and `scope` fields
- **consumes-from** `PLAY-dOrderedCharter-1` — the practice tags a role's `rules:` value cites
- **consumes-from** `PLAY-dOrderedCharter-6` — the `budgets.py home` verb through which `CODEX_MAX` is read
- **consumes-from** `PLAY-dOrderedCharter-19` — `read_policy_value` and `PolicyRefused` in `tools/playbook/policy_value.py`, through which S2 reads `instructions.checks`, and `read_namespaces` in `tools/playbook/tag_index.py`, through which S1 reads the `role` and `feature` rows
- **hands-off** `PLAY-dOrderedCharter-27` — the `code` slot added to the load set and its budget
- **hands-off** `PLAY-dOrderedCharter-21` — the step's practice reach added to the load set
- **hands-off** `PLAY-dOrderedCharter-34` — the composition's count against each budget, reusing the budget check
- **consumes-from** external — dGroundRules, landed before the build run: `policy.py get` at the landed revision (TOOL-dGroundRules-2 S7) with an unset key's default and reason (TOOL-dGroundRules-3 S2), the `instructions.checks` row and the shrink-only list this unit drains (TOOL-dGroundRules-1 S3, S6), `budgets.py resolve` and the cap census (TOOL-dGroundRules-9 S1, S2), `budgets.enforce` in gov's policy file at `warn` (TOOL-dGroundRules-1 S1), and the reader-coverage arm's call shapes (TOOL-dGroundRules-8)
- **consumes-from** external — `tools/template-size-limits.txt`, in the tree: the `AGENTS.md` row `budgets.py resolve` answers as the charter's `limits:` home; dSafePassage's step that would move it under `budgets.*` is DEFERRED at TOOL-dSafePassage-61 and is not waited for
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 12 and 40, which that batch unit corrects after this unit lands, each by the item its report id names

## 4. Design

### Data model

The unit row fields this unit reads are S10's: `scope` (a list of selector tags), `required-by` (a list
of `role.<name>` or `item.<tag>`), `budget` (its class). The load set is a list of unit tags, in the
unit registry's order. A refusal line: `load-set — refused · <reader> · missing <tag>[, <tag>] ·
instructions.checks=refuse`.

### Inventory

Minted: `tools/playbook/load_sets.py`; `derive_load_set`, `check_required`, `check_budget`; the CLI
verbs `derive`, `check` and `injected`; the prompt record line `**Load gaps:**`; the reader-visible
line `Missing required unit: <tag>`; the printed states `unarmed` and `no cap declared`; the plants
`required-away`, `role-unregistered`, `role-registered`, `feature-unregistered`, `feature-registered`,
`charter-over` and `role-block-over` of `load_sets.py --fixture --plant`. The policy key
`instructions.checks` and its three values are v2's.

### Migration

None. The gate legs that measure a cap at the bar, `charter size` and the roles kit's body ceilings,
keep the mode `budgets.py` answers them (TOOL-dGroundRules-9 S5); this unit adds the render-time
measurement beside them.

### Rollout

Live at landing. On gov's tree the roles carry no `required-by` row naming them until units are
registered with one, so the refusal is first exercised by the fixture; the derive verb prints each
role's set and its required count, a zero printed as a count and never as a pass.

Two commits. The first lands the unit with the row's fill and the list's drain. The second stages only
`.governance/policy.json` as `policy.py mirror --write` regenerates it, because the mirror records the
catalogue's blob id and the fill stales it (TOOL-dGroundRules-5 S1), and the guard admits a mirror
commit only when the policy file and the catalogue equal HEAD (TOOL-dGroundRules-19 S1).

The plants' rows in `tools/playbook/adopt-playbook.sh` close with their own tally, a fourth refusal
site after a plant loop beside the layer check's, the tag resolver's and the edge grammar's. The
check that every fail branch is armed or pinned reads each such site as unarmed, and no sibling suite
stages a failing row, so the main loop writes its row in `memory/project/unarmed-branches.txt` in the
second row shape, with the reason the three rows unit 73 named give. The module and its plants spell no
kit path, deriving each from the module's own location as `tools/playbook/instruction_units.py#derive_tool_rel`
does, because the shipped-surface ban reds a literal one since unit 72.

### Files touched (estimate)

- `tools/playbook/load_sets.py`
- `tools/playbook/adopt-playbook.sh` (the plants' `run_plant_rows` rows)
- `tools/playbook/instruction_units.py`
- `tools/playbook/render_playbook.py`
- `tools/roles/handoff.py`
- `tools/roles/render_agents.py`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `help/roles.md`
- `tools/policy/catalogue.toml` (the `instructions.checks` row's `summary` and `usage`)
- `tools/policy/unsummarised-keys.txt` (drained by `lists --write`)
- `.governance/policy.json` (the second commit, regenerated by `mirror --write`)

### Alternatives rejected

- **One switch for both refusals**, as `instructions.checks` held before the night pass two: the owner
  split them (NT-22), and gap-found-34 is that coupling.
- **The load-set code inside the roles kit.** The charter and Skills are load points too, and the
  playbook kit already holds S10's reader.
- **A third SessionStart hook for the injected measure.** The card writer already runs at session
  start, and a third entry is what `check_card` (`tools/check-wiring.sh:1044`, now
  `tools/check-wiring.sh#check_card`) refuses.

## 5. Production-readiness checklist

- security: no write path beyond the prompt record's gap line, written by the renderer that writes the
  record.
- perf / scale: one registry read per render; the injected measure reads about 20 small files.
- error / empty / loading states: an unreadable unit registry refuses the render naming it; an empty
  population prints its count.
- observability: every refusal and breach is one line naming the reader, the load point and the value.
- risks: a role's set refused at a spawn stops that pass, by design; `warn` is the owner's lever.
- testing: §6 and the `New arm:` lines of §7.
- migration: none.
- user docs: `help/roles.md` gains what a refused handoff says and the three `instructions.checks`
  values.

## 6. Acceptance criteria

- **AC1** — When `python load_sets.py derive --reader role.gov-builder --units <fixture>`
  runs over a fixture registry with units scoped `reader.every`, `role.gov-builder` and `role.gov-skeptic`,
  in a scratch tree whose `tools/playbook/namespaces.toml` holds no `role` row, it prints the first
  alone, the role part `unarmed — role.*` and the item part `unarmed`; with a `role` row whose `role` is
  `selects` planted, carrying every field AC7 names, it prints the first two and not the third.
  Red when: a unit scoped to another role loads, or an unarmed part reads as empty.
- **AC2** — When `python load_sets.py check --reader role.gov-builder --units <fixture>`
  runs over a planted registry whose unit `required-by = ["role.gov-builder"]` is scoped only to
  `role.gov-skeptic`, in a scratch tree holding AC1's planted `role` row, it exits 1 naming the unit
  under `--checks refuse`; and `handoff.py render` for the builder over that fixture writes no prompt
  file.
  Red when: the set missing the required unit renders.
- **AC3** — When the AC2 fixture runs under `--checks warn` and `--checks record`, both exit 0: `warn`
  puts `Missing required unit:` in the rendered text, `record` writes `**Load gaps:**` in the prompt
  record and nothing in the text; under `--checks refuse --budgets-enforce warn` it still exits 1.
  Red when: either value skips the check or `budgets.enforce` softens the refusal.
- **AC4** — When `check_budget` runs through `load_sets.py check --load-point AGENTS.md` over a scratch
  charter of 40000 bytes with a scratch cap of 50000, it exits 1 naming `CODEX_MAX` under
  `--budgets-enforce warn`; over a scratch role block 10 bytes past its body ceiling it prints a warning
  and exits 0 under `warn`, and exits 1 under `refuse`.
  Red when: a harness-limit breach passes under `warn`, or a cap breach refuses under `warn`.
- **AC5** — When `python load_sets.py injected` runs in gov, it prints a line for the
  agent list, the Skill list and the card, each with its bytes; with a scratch cap below the agent
  list's bytes it prints a breach line naming the agent list.
  Red when: a load point is missing or a breach prints nothing.
  figure: the bytes are DERIVED on each run.
- **AC6** — When `python "tools/policy/policy.py" lists --check` runs after the first commit, it exits 0;
  `git grep -n -x -F "instructions.checks" -- "tools/policy/unsummarised-keys.txt"` finds no line; and
  `git grep -n -F '("instructions.checks"' -- tools/playbook/` finds one line, in the new module.
  Red when: the row keeps no summary or usage, the name stays on the shrink-only list, or the key is
  read in a shape the reader-coverage arm does not count.
- **AC7** — When `python -c` calls `load_sets.derive_load_set` with `features=("feature.roles",)` over a
  fixture registry holding a unit scoped `feature.roles`, in a scratch tree whose
  `tools/playbook/namespaces.toml` holds no `feature` row, the unit is not selected and the report
  carries `unarmed — feature.*`; with a `feature` row whose `role` is `selects` planted, carrying every
  field of `REGISTRY_FIELDS` (in `tools/playbook/tag_index.py`: `ns`, `owner`, `layer`,
  `source`, `extractor`, `role`, `purpose-source` and `join-armed-by`) so `read_namespaces` raises no
  `TagError`, it is selected.
  Red when: an unregistered feature selector reads as an empty set, so "no feature units" passes green.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `roles render wiring` · `roles render selftest` · `govkit acceptance matrix` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `policy fixtures`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 AC4 AC7 · the `playbook render selftest` leg's `run_plant_rows` rows, each running `load_sets.py --fixture --plant <case>`: a required unit scoped away from its role, a unit scoped `role.gov-builder` with and without a `role` row registered, a unit scoped `feature.roles` with and without a `feature` row, and the oversized charter and role block, each failing case staged by its plant · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC5 · a fixture card write with a scratch cap below the agent list's bytes · none

## 8. Open questions

- **F1 — Where `record` writes a gap.** R-C says "the gap is recorded" and names no record. Options: (a)
  a `**Load gaps:**` line in the prompt record the render writes; (b) a journal line; (c) an ask.
  RESOLVED (agent, 2026-10-23, delegated): (a), rung 3; the prompt record is the one record every
  rendered work order already has, (b) has no journal for a main-loop render, and (c) is what R-C gives
  the caller on a refusal, not on `record`. widens: none · relaxes: none
- **F2 — Which budget mode applies at render.** Options: (a) `budgets.enforce`'s catalogue default
  `warn`, read with no reader; (b) `refuse`; (c) no render-time budget; (d) the mode `budgets.py resolve`
  answers per cap. The first pick was (a), on the premise that the key did not exist yet, which the
  parents' landed specs remove: `budgets.enforce` sits in gov's policy file at `warn`
  (TOOL-dGroundRules-1 S1), and `budgets.py` answers each cap's mode from it and `budgets.pinned`
  (TOOL-dGroundRules-9 S2). RESOLVED (agent, 2026-10-24, delegated): (d), rung 1, the parents' landed
  specs; (a) would ignore a pin, and (b) and (c) set aside the owner's switch. widens: none · relaxes:
  none
- **F3 — Which harness limit applies per load point.** R-K gives harness limits to dWellOiledMachine's
  adapters. Options: (a) Codex's `CODEX_MAX` for the charter alone, read from
  `tools/agent-instructions/adopt-agent-instructions.sh:31`, now
  `tools/agent-instructions/adopt-agent-instructions.sh#CODEX_MAX`; (b) wait for the adapters. RESOLVED (agent,
  2026-10-23, delegated): (a), rung 3; it is the one harness limit the tree measures today (C1-F14's
  fix plants it), and the adapters add theirs as they land. widens: none · relaxes: none
- **F4 — What the checks do when a policy reader cannot answer.** `policy.py get` and `budgets.py
  resolve` exit 2 on a refusal (TOOL-dGroundRules-2 S7, TOOL-dGroundRules-9 S2), and an adopter may hold
  the playbook kit without the policy kit. Options: (a) the missing-unit check runs as `refuse` and
  prints the reader's line once; the budget check refuses the render on `budgets.py`'s exit 2 and prints
  `unarmed` naming the policy kit when the kit is absent; (b) every such case refuses the render; (c)
  every such case reads the catalogue default. (c) reads a value no reader resolved, and (b) reds every
  render of an adopter that has not installed a kit nothing else requires; TOOL-dGroundRules-9 §8 F4
  rules out both for its own enforcers. RESOLVED (agent, 2026-10-24, delegated): (a), rung 1, that
  fork's (a): a missing reader never loosens a refusal, and says so once. widens: none · relaxes: none
  Re-read at `550ea807a`: whether `tools/playbook/kit.toml` requires the policy kit is
  `PLAY-dOrderedCharter-73`'s F1, parked with the owner. This mark holds while nothing requires it; a
  ruling that does leaves the `unarmed` branch reached by no valid install, and is not this unit's.
- **F5 — How the role part selects while no `role` namespace is registered.** S1 and AC1 to AC3 select
  by `role.<name>`, and a `required-by` names `role.gov-builder`; at `c7269a97`
  `tools/playbook/namespaces.toml` registers no `role` row, `tools/playbook/readers.toml` holds only
  `reader.every`, `reader.driver` and `reader.subagent`, and no spec of this build registers one.
  Options: (a) the role-selector part reported `unarmed — role.*` until a unit registers a `role` row
  whose `role` is `selects`, as S1 reports the unregistered `feature` part, the practice-tag part still
  selecting; (b) this unit registers a `role` row in `tools/playbook/namespaces.toml`; (c) select by
  `role.<name>` with no row registered. (b) is a second mechanism in this unit, a namespace row
  carrying every `REGISTRY_FIELDS` field, its owner, extractor and join undesigned by any unit; (c)
  grades a selector against no registry, the shape the tag resolver's `bad-ns` plant reds as
  "namespace … is not registered". RESOLVED (agent, 2026-11-04, delegated): (a), rung 1, the tree at
  `c7269a97` and the main loop's sweep decision in
  `2026-11-04-prompt-PLAY-dOrderedCharter-52-drift-fold-brief.md`; an unregistered selector never reads
  as an empty set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · S2 S3 S4 · §3 Edges · §4 Migration, Rollout, Files touched · AC6 · §8 F2 F4 · §10 ·
  re-grounded on the parents' landed specs by `2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck.md`
  row 33 and U1 to U4: caps are read with `budgets.py resolve`, named as the census names them, and
  `CODEX_MAX` through its census row; `instructions.checks` is read with `policy.py get` in a shape the
  reader-coverage arm counts, its landed row filled and drained, the mirror in a second commit; F2
  re-resolved on rung 1 and F4 added; the roles kit runs `load_sets.py` as a subprocess.
- rev-4 · 2026-10-25 · S3 · §3 Edges · item 6 of `2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md`,
  the parent audit's P1: `CODEX_MAX` is read with `budgets.py home codex-instructions`, the one reader of
  a cap's home, which unit 6 adds at order 19 (its §8 F5) since that unit's check calls it first.
- rev-5 · 2026-11-02 · S1 · §3 · AC7 · §7 · closes PLAY-dOrderedCharter-57 by
  `2026-11-02-prompt-PLAY-dOrderedCharter-17-ask-fold-brief`: `derive_load_set` carries the `features`
  argument `TOOL-dFurnishedOrders-18` selects by, its feature part `unarmed` while no `feature` row is
  registered as a selector, seen by AC7 on a fixture with none registered.
- rev-6 · 2026-11-03 · §7 · from `2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md` Item 2: the leg line names `policy fixtures`, whose guard a §4 Files touched path trips, the guards hit the spec-token check reads with DEFERRED as live.
- rev-7 · 2026-11-04 · S1 S2 S3 S4 · section 3 Edges · section 4 Inventory, Files touched,
  Alternatives rejected · AC1 AC2 AC7 · section 7 · the fork record's F5 · section 10 · from
  `2026-11-04-prompt-PLAY-dOrderedCharter-52-drift-fold-brief.md` findings 11-1 to 11-6 and the
  cross-cutting finding: S2 reads `instructions.checks` through unit 19's `read_policy_value`, and the
  Edges gain unit 19; the role-selector part is `unarmed` while no `role` namespace is registered
  (F5), AC1 and AC2 plant one; AC7's planted row carries every registry field; the selftest rides
  `run_plant_rows`; anchors written as symbols beside each listed citation; S3, the Edges and the
  reuse audit re-ground on `tools/template-size-limits.txt`, still tracked.
- rev-8 · 2026-11-04 · AC7 · from `2026-11-04-prompt-PLAY-dOrderedCharter-20-3-sweep-fix-brief.md` item 3: AC7 names `REGISTRY_FIELDS` beside the plain path.
- rev-9 · 2026-11-08 · S3 S4 · section 4 Rollout · AC6 · section 8 F3 F4 · section 10 · from
  `2026-11-08-prompt-PLAY-dOrderedCharter-3-drift-fold-brief.md`: re-read at `550ea807a`. AC6's grep
  reads the kit directory, the new module not being tracked yet; S3 keeps the budgets script and its
  verb apart, as unit 73 found the cap census requires; the Rollout names the plant tally's pinned row
  and the shipped-surface ban unit 72 left; moved anchors in S4, F3 and the reuse audit gain their
  symbols; F4 notes, mark unchanged, that unit 73's parked F1 decides whether the policy kit is
  required. Re-checked unchanged: no `role` or `feature` namespace row, `instructions.checks` still on the
  shrink-only list, and `PolicyRefused` raised on the reader's exit 2 and with no policy kit found.

## 10. Reuse audit

The seams extended: `render_handoff`'s `reads` walk (`tools/roles/handoff.py:337-396`, now inside
`tools/roles/handoff.py#render_handoff`), where a
handoff's blocks are assembled and where the load set joins; `BODY_CEILINGS`
(`tools/roles/check_roles.py:85-89`, now `tools/roles/check_roles.py#BODY_CEILINGS`), the role
block's one carrier, read and not copied; the policy kit's one cap reader, `budgets.py resolve`
(TOOL-dGroundRules-9 S2), with each cap named from the census `tools/policy/caps.toml` (its S1), which
reads the limits file `tools/template-size-limits.txt` as a cap's `limits:` home, never this unit;
`read_policy_value` (`tools/playbook/policy_value.py#read_policy_value`) and `read_namespaces`
(`tools/playbook/tag_index.py#read_namespaces`), unit 19's readers; `run_plant_rows`
(`tools/playbook/adopt-playbook.sh#run_plant_rows`), the plant loop the selftest rides; `resolve_kit_dir`, the sibling resolver (`render_playbook.py:79`,
`roles_lib.py:97`); and `write_card` (`skills/session-kickoff/manifest-check.sh:706`) as the one
session-start writer. `python tools/codebase-map/reuse_lookup.py "budget the bytes a role's handoff
loads"` ranked `load`, `load_conf`, `load_workflows`, `load_text`, `load_policy` and
`derive_budget_cut` (`tools/codebase-map/reuse_lookup.py`), name-stem matches on "load" and "budget";
none derives a load set, and `derive_budget_cut` cuts a shortlist, not a load point, so the map and
the source disagree on fit.

Recall terms used: `python tools/memory-recall/query.py "how are load sets budgeted per role and refused when a required unit is missing" --terms "load set budget required-by instructions.checks budgets.enforce BODY_CEILINGS role render refuse warn"`
