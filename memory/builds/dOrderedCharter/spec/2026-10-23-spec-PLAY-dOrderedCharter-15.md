# PLAY-dOrderedCharter-15 — the instruction manifest and its guarded write command, each change recorded, and the pack catalogue

**Status:** CLOSED · rev-10 · 2026-11-04 · node d · Tier-2 · base ce13efbe · streams playbook · order 16 · advances PLAY-dOrderedCharter-38 · ratified 2026-10-25

**Carries:** cl-dClosedLoop-0045@f345dc78 whole

**Carries:** node:policy-key.instructions.edit

**Carries:** node:policy-key.instructions.proof

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-27 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-build-PLAY-dOrderedCharter-15-deviation-151.md](../build/2026-10-24-build-PLAY-dOrderedCharter-15-deviation-151.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-15-deviation-152.md](../build/2026-10-24-build-PLAY-dOrderedCharter-15-deviation-152.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 PLAY-dOrderedCharter-84 PLAY-dOrderedCharter-85 PLAY-dOrderedCharter-86 PLAY-dOrderedCharter-87 |
| [2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-25-build-PLAY-dOrderedCharter-15-deviation-153.md](../build/2026-10-25-build-PLAY-dOrderedCharter-15-deviation-153.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-15-deviation-154.md](../build/2026-10-25-build-PLAY-dOrderedCharter-15-deviation-154.md) | deviation | — |
| [2026-11-02-build-PLAY-dOrderedCharter-15-ledger.md](../build/2026-11-02-build-PLAY-dOrderedCharter-15-ledger.md) | journal | — |
| [2026-11-04-build-PLAY-dOrderedCharter-15-1-builder-return.md](../build/2026-11-04-build-PLAY-dOrderedCharter-15-1-builder-return.md) | journal | — |
| [2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md](../build/2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md](../prompts/2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-46 |
| [2026-11-02-prompt-PLAY-dOrderedCharter-15-build-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-15-build-brief.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md) | research | PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-11-03-prompt-PLAY-dOrderedCharter-9-drift-sweep-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-9-drift-sweep-brief.md) | research | PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-50 |
| [2026-11-04-prompt-PLAY-dOrderedCharter-15-1-spec-writer.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-15-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-PLAY-dOrderedCharter-15-3-spec-writer.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-15-3-spec-writer.md) | journal | — |
| [2026-11-04-prompt-PLAY-dOrderedCharter-15-divergence-brief.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-15-divergence-brief.md) | research | — |
| [2026-11-04-prompt-PLAY-dOrderedCharter-15-edge-mirror-brief.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-15-edge-mirror-brief.md) | research | — |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |
| [2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md](../reviews/2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md) | diff-review | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 |

<!-- /gen:spec-records -->

## 1. Goal

There is no write path for instructions (gap-found-15): the owner changes one only by editing a source or the
template by hand, with no manifest, no validating command, no recorded change and no pack beyond the
practice catalogue. R-I gives each kit a manifest and the repository an overlay, merged as row stores, and one
command that adds, edits, removes, lists, renders and checks units, proving its caller is the owner by
`instructions.proof` so an agent only proposes. This unit lands that command under `instructions.edit`, each
value with its arm, witness and planted red; `flow-only` refused at load until dDeclaredLoop lands (L3);
every write refused until dDeclaredLoop's guard lands (M11); the change record (S12, S13) each write
leaves; the command's checks as a leg over the tree; the manifests' row merge; and instruction packs
extending `charter.practices` into a pack catalogue, apart from the policy presets (C1-F19).

## 2. Scope (IN)

- **S1** — The manifest. The instruction manifests are each kit's `instructions.toml` (unit 9) and the
  repository's overlay `.governance/instructions.toml` (unit 32), listed by `read_manifests(root)` in
  `tools/playbook/instructions_edit.py`, the one list the one-door check and the write path read. Across
  nodes they are row stores: `tools/memory-tree/merge-rows.py` gains a TOML-table class keyed by each
  `[[unit]]` table's `tag`, with the driver's postconditions (no tag lost, none duplicated), and
  `.gitattributes` routes `**/instructions.toml` and `.governance/instructions.toml` to `merge=rows`.
  Observed by AC1.
- **S2** — The command, `python tools/playbook/instructions_edit.py <verb>`: the five write verbs of
  `WRITE_VERBS` (§4 Data model), each taking `--manifest <kit id>|overlay`, and the read verbs `list`,
  `render`, `check` and `propose`. A write validates the would-be tree with S6's checks, writes the row,
  writes its change record (S7) for the same commit, re-renders the targets unit 20's renderer assigns,
  and prints the paths it wrote. `propose` writes nothing and prints the row diff and the command that
  would apply it. `list` prints each row's `<tag>@<hash8>`. The record's inputs are flags, as
  `tools/memory-tree/build_records.py#main` takes `new exception`'s: `--build <slug>`, the recording
  build; `--unit <id>`, the unit the record is filed under and the `Caused-by` value, as
  `tools/memory-tree/build_records.py#write_exception` writes it; and `--mark editorial|semantic`.
  `rename` and `split` also take `--successor <tag[,tag]>`, each of a `split`'s successors a row the
  manifest already holds, and `add` takes `--promoted-from <source>`. The parser requires none of them:
  a write tests them after its guard, flow and proof branches, in the Data model's order, and exits 2
  naming each absent flag, so AC6's command, which passes none, stops at the guard. A proposal prints
  the flags it was given and a placeholder for each absent one. Observed by AC2 and AC9.
- **S3** — `instructions.edit`, each value with its arm, witness and planted red:

  | Value | Arm | Witness | Planted red |
  |---|---|---|---|
  | `owner-command-agents-propose` (default) | a write with `instructions.proof`'s proof writes; one without prints the proposal and writes nothing | the change record's `Proof` field | a non-terminal write call that writes a row |
  | `command-for-all` | any caller's write writes | the change record's `Proof: none — command-for-all` | a write whose would-be tree fails S6, admitted |
  | `flow-only` | the command writes nothing; writes come from the flow's item | the load refusal naming the absent flow component | the value loading while the flow component is absent |

  `flow-only` is refused at load, exit 2, as selecting an absent component, until the layer register
  (unit 16) holds a core row declaring the point `point.instruction.flow`, which dDeclaredLoop's flow
  declares when it lands (L3). Observed by AC3, AC4 and AC5.
- **S4** — Every write refused until dDeclaredLoop's guard lands (M11). Whatever the value, a write verb
  exits 1 naming the guard and the stand-in route while no core row of the layer register declares
  `point.instruction.guard`, the point dDeclaredLoop's guard declares; the refusal prints the row diff as
  `propose` would. dGroundRules' minimal guard (`cl-dClosedLoop-0012`) refuses agent writes to the
  overlay meanwhile. Observed by AC6.
- **S5** — `instructions.proof`. `tty-cli`, the default, is the owner's presence shown as standard error
  being an interactive terminal, the one stream dGroundRules' minimal guard tests for `policy-file.proof`
  (`[ -t 2 ]`, written inline in `.githooks/pre-commit`, TOOL-dGroundRules-6 S4 and its §8 F3). That
  test is shell with no callable, so the command tests `sys.stderr.isatty()` itself, stated as a second
  implementation of the guard's signal (§8 F4, the owner's pick). `signed` and `both` are refused at load as selecting an absent component, the layered
  proof v2 places in `[planned]`, until a core row declares `point.instruction.signed-proof`. Both keys
  are read with `policy_reader("instructions.edit")` and `policy_reader("instructions.proof")`,
  PLAY-dOrderedCharter-9's callable over unit 19's `read_policy_value(key, root)`
  (`tools/playbook/policy_value.py:72`), which finds the policy kit through its own inline
  `resolve_kit_dir` (`:23-60`, called at `:75`), since a kit never imports a sibling (TOOL-dGroundRules-1
  §4), runs `policy.py get <key> --explain`, and returns the value's stdout lines and the explain line:
  an unset key reads its catalogue default with its reason (TOOL-dGroundRules-3 S2), and each call is a
  shape the reader-coverage arm counts (TOOL-dGroundRules-8, the Readers table). A refused read, the
  `PolicyRefused(key, line)` it raises (`:63-69`), refuses every verb at load, exit 2, naming the key
  and carrying the reader's line. Observed by AC3, AC7 and AC12.
- **S6** — The checks, run before every write and as a leg over the tree,
  `python tools/playbook/instructions_edit.py check`: unit 20's schema and one-fact checks, unit 12's
  grammar, unit 19's tag checks, and two of this unit's own: **conflicts at one level**, two active
  directives at one level whose texts differ only in an opposite modal (`MUST` against `NEVER`); and
  **references**, a pointer unit or an `edges` target naming a `unit.*` tag that resolves to no active unit
  and no change record's successor. The budgets join when unit 11 lands them. Observed by AC8.
- **S7** — The change record (S12, S13), the `change` kind of unit 7's factory
  (`tools/memory-tree/build_records.py`): `<date>-build-<unit id>-change-<n>.md` in the recording build's
  `build/` folder, `**Serves:** change <unit id>`, with the fields `Unit` (the tag), `Action` (one of
  `WRITE_VERBS`), `Before` and `After` (each `<tag>@<hash8>`, the hash unit 24's one pin normaliser
  `design_lib.derive_pin_hash` gives, `tools/memory-tree/design_lib.py:173`, over the row's `text`, or
  its `source` on a row with no `text`, or `none`; on a `split`, `After` is a comma list, one
  `<tag>@<hash8>` per successor in `Successor`'s order, and `Before` stays one), `Mark`
  (`editorial` or `semantic`), `Successor` (a tag, a comma list for a split, or `none`, on every action
  but `add` and `edit`), `Proof` (`tty-cli` or `none — <value>`), `Promoted-from` (optional, the source a
  promotion names, written as the `promoted-from` edge) and `Caused-by`. Each field is the factory's
  bullet, `- **<Field>:** <value>`, the one shape `tools/memory-tree/build_records.py#write_record`
  writes and its `read` verb reads, read on the playbook side by `read_change_fields(text)` in `instruction_units.py`, a
  change record being a path `CHANGE_RECORD_RE` matches, the file name above under
  `<memory_root>/builds/*/build/`. The edge check reads `Promoted-from` through a change-record adapter,
  `read_change_edges(text, path)` in `tools/playbook/edge_grammar.py`, which `read_tree_edges`
  (`:560-600`) calls for such a path and which tags the edge `site = "instructions.edit"`.
  `promoted-from`'s row names that site as its one writer (`tools/playbook/edges.toml:237-244`), and the
  writer arm reds the type at any other site (`edge_grammar.py:415-417`), while no adapter assigns this
  site today (`:254-386`; `read_header_edges` reads `Caused-by` and `Made-by` alone, `HEADER_RE` `:83`).
  Unit 20 derives each unit's `status` from these, and this unit takes the body of unit 20's
  `read_change_records`, which it replaces when it lands the `change` kind (S14); unit 33 grades `Mark`. The factory's `new change` verb, its flags S14's, is the stand-in door
  a build's builder records a kit manifest change through while the command refuses writes. Observed by
  AC9.
- **S8** — The pack catalogue, `tools/playbook/packs.toml`: one `[[pack]]` row per instruction pack, with
  `name`, `kind` (`methodology`, `governance` or `language`), `practices` (practice tags of S15's
  catalogue, or the one selector `all`) and `description`, read by `read_packs`. `resolve_practices(value)`
  resolves a `charter.practices` value naming packs and practices into practice tags, for unit 1's key
  reader. One row ships, `foundation`, `kind = "governance"`, `practices = "all"`, the governance
  foundation set v2 names as the key's default. The check reds a pack naming a practice the catalogue
  lacks (`unarmed` until unit 1 writes the catalogue) and a pack whose name equals a practice's. The pack
  catalogue is no policy preset: no preset row sets `charter.practices`. Observed by AC10.
- **S9** — Retired rows from change records, which unit 19 hands to this unit. The `unit` namespace's one
  extractor, `instruction_units:extract_unit` (unit 9 S3; `tools/playbook/namespaces.toml:28`), also
  claims each change record and returns, for a record whose `Action` ends a tag (`remove`, `rename`,
  `split`), one `retired` row: the record's `Unit` tag, at its `- **Unit:**` line, its text the record's
  `- **Successor:**` line with its `- ` cut, `**Successor:** <value>`. Unit 19's `check_retired`
  (`tools/playbook/tag_index.py:879`) reads it, so `gov_tag.py check` reds new text citing the tag. The
  redirect lives in that text: one tag for a rename, the list for a split, which redirects to no single
  successor, and `none` for a removal. `show` alone reads it back: the `show` branch of
  `tools/playbook/gov_tag.py#run_kit_verb` (`tools/playbook/gov_tag.py:82-84`) takes its rows from
  `tools/playbook/tag_index.py#resolve_address`, which reads `DEFINE_KINDS` alone, so a retired tag
  yields none today. When that returns no row, the branch falls back to the `retired` rows of the
  exact tag, its alias resolved, through `read_retired_rows(con, tag)` beside
  `tools/playbook/gov_tag.py#read_refs`, and prints them through its own lines, kind `retired` and then
  the row's text, or as `--json` rows. A row found exits 0, as the branch's `0 if rows else 1` does, the
  kind saying it is no live tag; no retired row either prints the no-row line and exits 1. The subtree
  slice does not apply: under `tags.slice = "subtree"` the fallback still reads the one tag, since a
  retired row is a name and no prefix. `resolve_address`, `where`, `bundle` and both resolvers,
  `tools/playbook/edge_grammar.py#read_tag_rows` and `tools/playbook/instruction_units.py#load_resolver`,
  stay on `DEFINE_KINDS`, so a retired tag resolves as live nowhere. The read lands in
  `tools/playbook/gov_tag.py` and not `tools/playbook/tag_index.py`, whose module hash versions each
  extractor it holds (`tools/playbook/tag_index.py#derive_extractor_versions`). No table or
  column is added to the index schema (`tag_index.py:72-85`), and the `unit` row's `source` names
  change records (§8 F5). The extractor reads the fields through `read_change_fields` beside it, so its
  version, its module's hash, covers the read (unit 9 §8 F6). Observed by AC11.
  **Readers:** by name: READER NOT IN TREE — this item retires no name; it writes the rows of tags that
  change records will retire, and the extractor that writes them is unit 9's · by value: `check_retired`
  (`tools/playbook/tag_index.py:879`) reads each row's tag, the join reads the `retired` kind at
  `tag_index.py:830` and `:988`, and the `show` fallback in `tools/playbook/gov_tag.py#run_kit_verb`
  (`tools/playbook/gov_tag.py:82-84`) prints each row's text where `resolve_address` finds no row.
- **S10** — The legs and plants, two legs in `tools/gate-legs.json` (F6). `instruction edits (manifest checks)`
  runs S6 over the tree and S8's check, carrying `"enforces": ["principle.p11", "principle.p13"]`,
  `"subject": "repo"` and `"chunk": "declarations"`. `instruction edits selftest` runs
  `python {prefix}/playbook/instructions_edit.py fixture`, which walks every case of the module's
  `PLANTS`, so a later unit's case joins the leg by joining that table; its row is
  `instruction units selftest`'s shape, `"enforces": ["principle.p16"]`, `"subject": "kit"`,
  `"chunk": "selftests"` and `"ceiling": 300`.
  `python tools/playbook/instructions_edit.py fixture --plant <case>` builds a throwaway repository in the
  system temp directory, with its own layer register and a committed `.governance/policy.toml`, since the
  reader reads revisions only (TOOL-dGroundRules-2 S2), and runs the case. Each leg's rows land in this
  pass, as unit 26 writes its leg's: an `[[exempt_leg]]` row in `tools/govkit/registry.toml` after the
  `edges` row (`:715`), the first since the leg runs unit 19's tag checks and unit 20's over gov's own
  manifests and change records, the reason the `tags` row gives (`:712`), the second since its cases
  reach the `policy` and `memory-tree` kits, which a `playbook-render` target may not hold, the reason
  `instruction units selftest`'s row gives; its `tools/govkit/subject-pins.tsv`
  row, by `python tools/govkit/govkit.py selfcheck --write` (`tools/govkit/govkit.py:2736-2742`); and
  its name in the `gate-legs` claim of `memory/map/features/playbook.md` (`:11`), with the files
  `python tools/codebase-map/gen_map.py --write` rewrites under `memory/map/generated/`. `tools/gate-legs.json`
  is on the `watch:` list of `memory/guides/SESSION-KICKOFF.md`, so that file takes a new `last-audit`
  stamp, as unit 20's pass did. Observed by AC1 to AC11 and AC13.
- **S11** — The two catalogue rows. `instructions.edit` and `instructions.proof` land with dGroundRules as
  `[[key]]` rows of `tools/policy/catalogue.toml`, owner dOrderedCharter (v2:1243-1244), with no
  `summary` or `usage` and their names on the shrink-only `tools/policy/unsummarised-keys.txt`
  (TOOL-dGroundRules-1 S3, S6). This unit adds no row: it fills each row's `summary` and `usage`, a line
  its row admits (`instructions.edit = "command-for-all"`, `instructions.proof = "tty-cli"`), and drains
  both names in the same commit with `python <prefix>/policy/policy.py lists --write`. Observed by AC12.
- **S14** — The `change` kind landed, as unit 20's fork F7 hands it here; numbered past S12 and S13,
  which name the design's record clauses in this spec. In `tools/memory-tree/build_records.py`, the
  `change` row of `KINDS` gains `required` (`Unit`, `Action`, `Before`, `After`, `Mark`, `Proof`,
  `Caused-by`) and `closed` (`Mark`, and `Action`, the one list `WRITE_VERBS` reads). `check_change_fields`
  grades the pin shapes, `Proof`, and `Successor` on an ending action. `read_change(path, text)` and
  `read_changes(root, conf=None)` sit beside `read_exception` and `read_exceptions`, the second sorted by
  date, build and `<n>` as a number, since `derive_status` takes the last record; two builds' same-day
  records of one tag order by slug, the read's known ceiling. `main`'s `read` verb branches to
  `read_change`. `write_change` is the one writer, over `write_record`, validating through
  `check_change_fields`; the command and the door both call it. `DOORS` gains `change`, and `new` takes
  one sub-parser per door, `new exception`'s flags unchanged, so that
  `tools/memory-tree/build_records.py#run_fixture`'s door branch takes each door's argv from a table
  keyed by kind. The door's flags are
  `new change --build <slug> --unit <id> --tag <unit tag> --action <verb> --mark <mark> --before <pin> --after <pin>`,
  with `--successor <tag[,tag]>` on an ending action, `--promoted-from <source>` and `--root <dir>` optional. `--tag` fills `Unit`; `--unit`
  names the file and fills `Caused-by`; a pin is `none` or what `instructions_edit.py list` prints.
  `Proof` reads `none — stand-in door` and takes no flag, so no caller claims a proof. In
  `tools/playbook/instruction_units.py`, the body of `read_change_records(root)` returns
  `build_records.read_changes(root)` as the mappings `derive_status` reads, and raises `UnitRowError`
  naming each malformed record. `derive_status_note` would read None for good, so this unit deletes it,
  with the head line of `tools/playbook/instruction_units.py#run_one_fact` and the note lines of
  `tools/playbook/render_playbook.py#run_check_render`, whose `UnitRowError` arm stands and reds a
  malformed record. `arm_status` loses its two pins, the `status: unarmed` line and the read that
  raises, and gains their successors: a committed record retires its unit at render, a malformed one
  raises and reds the gate, and no `status: unarmed` line prints. Observed by AC9 and AC14.
  **Readers:** by name: `tools/playbook/instruction_units.py` and `tools/playbook/render_playbook.py`,
  each spelling the deleted function · by value: `arm_status` in `tools/playbook/instruction_units.py`
  compares the `status: unarmed` line, and `tools/playbook/README.md` describes it, so its status-arm
  sentence is rewritten.

## 3. Non-goals (OUT)

- The guard itself and the flow's item that writes under `flow-only`: dDeclaredLoop's. This unit names
  the points each declares and refuses until they are declared.
- The layered, signed proof: v2 `[planned]`.
- The overlay's file, home and `repo.` units: unit 32; the overlay's row mechanism over every kind: unit 35.
- The `editorial` and `semantic` mark's admission rules, pins and drift: unit 33.
- Instruction-effectiveness records (R-J) and the Loop Review's pruning: later builds.
- The policy presets and their catalogue: dKeptSession's; packs never enter them.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-9` — `read_units`, the rows every verb reads, and `extract_unit` beside its reader, whose claim S9 extends to change records
- **consumes-from** `PLAY-dOrderedCharter-20` — the schema and one-fact checks, the renderer a write re-renders through, `derive_status`, and the body of `read_change_records`, which it replaces when it lands the `change` kind
- **consumes-from** `PLAY-dOrderedCharter-12` — the grammar check S6 runs
- **consumes-from** `PLAY-dOrderedCharter-7` — the record factory and its stand-in door, which S7's kind joins, and `principle` in `tools/playbook/edges.toml`'s `enforces` row's `to`, which S10's `enforces` values need
- **consumes-from** `PLAY-dOrderedCharter-16` — the layer register whose declared points S3, S4 and S5 read
- **consumes-from** `PLAY-dOrderedCharter-19` — the tag checks S6 runs, the index whose `retired` rows S9 writes, and `read_policy_value` in `tools/playbook/policy_value.py`, which S5's reader wraps
- **consumes-from** `PLAY-dOrderedCharter-24` — its S7 normaliser, `design_lib.derive_pin_hash`, for `Before` and `After`
- **consumes-from** external — dGroundRules, built before this build run: `policy.py get` at the landed revision (TOOL-dGroundRules-2 S1, S7), the two catalogue rows and the shrink-only list S11 fills and drains (TOOL-dGroundRules-1 S3, S6), the mirror's `mirror --write` (TOOL-dGroundRules-5 S2), and the stderr signal its minimal guard's hook tests (TOOL-dGroundRules-6 S4, `cl-dClosedLoop-0012`)
- **hands-off** `PLAY-dOrderedCharter-1` — `resolve_practices`, which the `charter.practices` reader calls
- **hands-off** `PLAY-dOrderedCharter-14` — the command a promotion goes through, and the `Promoted-from` field
- **hands-off** `PLAY-dOrderedCharter-32` — the overlay as the command's `--manifest overlay` target
- **hands-off** `PLAY-dOrderedCharter-33` — the `Mark`, `Successor` and `Proof` fields its checks read
- **hands-off** `PLAY-dOrderedCharter-35` — the command that writes and re-pins an overlay row
- **hands-off** `PLAY-dOrderedCharter-31` — the change record kind its census records are written in
- **consumes-from** `PLAY-dOrderedCharter-28` — the `promoted-from` edge type and the one site it admits, this command's change record
- **hands-off** external — dDeclaredLoop declares `point.instruction.guard` and `point.instruction.flow`, which arm writes and `flow-only`
- **consumes-from** `PLAY-dOrderedCharter-42` — the change kind's token in the bindings reader, without which S7's record reads malformed (finding 31)
- **hands-off** `PLAY-dOrderedCharter-40` — the change records of gov's first four unit rows, written through S7's stand-in door (finding 2)
- **hands-off** `PLAY-dOrderedCharter-45` — S1's table class given its whole conflict envelope and a parse postcondition (finding 79)
- **hands-off** `PLAY-dOrderedCharter-46` — S2's re-render pointed at the overlay the write verb has just written, through the candidate read (finding 80)
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 5, 14, 67 and 85, which that batch unit corrects after this unit lands, each by the item its report id names
- **consumes-from** `PLAY-dOrderedCharter-50` — the owed-rows probe: this pass runs `python tools/run-gates/owed_rows.py --base HEAD` before its commit and writes every row it names in that commit (round-2 id 23)
- **hands-off** `PLAY-dOrderedCharter-52` — the `instructions_edit.py fixture --plant` entry that unit's S6 three cases join

## 4. Design

### Data model

```toml
# tools/playbook/packs.toml
[[pack]]
name = "foundation"
kind = "governance"
practices = "all"
description = "The governance foundation set, every catalogue practice until the census narrows it."
```

```
WRITE_VERBS = ("add", "edit", "remove", "rename", "split")

write(verb, row, manifest):
  value  = policy("instructions.edit")      # refused at load if it selects an absent component
  proof  = policy("instructions.proof")     # likewise
  if not declared("point.instruction.guard"):  refuse: guard absent, print the proposal
  if value == "flow-only":                       refuse: writes come from the flow's item
  if value == "owner-command-agents-propose" and not proven(proof):  print the proposal, write nothing
  if a record flag is absent:                    refuse, exit 2, naming each flag
  if check(would_be_tree) is red:                refuse, naming each red
  write row; write change record; re-render; print paths
```

### Inventory

Minted: the module `tools/playbook/instructions_edit.py` with `read_manifests`, `WRITE_VERBS`, the verbs of S2 and the
fixture cases; the points `point.instruction.guard`, `point.instruction.flow` and
`point.instruction.signed-proof`; the record kind `change` and its fields; the file
`tools/playbook/packs.toml` with `read_packs` and `resolve_practices`; `read_change_fields` and
`CHANGE_RECORD_RE` in `tools/playbook/instruction_units.py`; `read_change_edges` in
`tools/playbook/edge_grammar.py`; `read_retired_rows` in `tools/playbook/gov_tag.py`; `check_change_fields`,
`read_change`, `read_changes` and `write_change` in `tools/memory-tree/build_records.py`; merge-rows'
TOML-table class; the legs `instruction edits (manifest checks)` and `instruction edits selftest`.

### Migration

None: no manifest exists before unit 9's rows; the `.gitattributes` lines take effect on the next merge.

### Rollout

Live at landing, at order 16, refusing every write until dDeclaredLoop's guard declares its point; `list`,
`render`, `check` and `propose` run from landing. S11 lands as two commits: the first fills the two rows
and drains the list; the second stages only `.governance/policy.json` as `policy.py mirror --write`
regenerates it, because a catalogue edit stales the mirror and the guard admits a mirror commit only
when the policy file and the catalogue equal HEAD (TOOL-dGroundRules-5 S1, TOOL-dGroundRules-19 S1).

### Files touched (estimate)

- `tools/playbook/instructions_edit.py`
- `tools/playbook/packs.toml`
- `tools/playbook/instruction_units.py`, `extract_unit`'s change-record claim, the body of
  `read_change_records`, the status note's deletion and `arm_status`
- `tools/playbook/render_playbook.py`, the note lines of `run_check_render`
- `tools/playbook/gov_tag.py`, `show`'s `retired` fallback
- `tools/playbook/README.md`, the status-arm sentence
- `help/tags.md`, `show` on a retired tag
- `tools/playbook/edge_grammar.py`, `read_change_edges`
- `tools/playbook/namespaces.toml`, the `unit` row's `source`
- `tools/memory-tree/build_records.py`, the kind's row, its reader and writer, `new change`, `read` and
  `run_fixture`
- `tools/memory-tree/merge-rows.py`
- `.gitattributes`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`, the `last-audit` stamp
- `tools/govkit/registry.toml`, the `[[exempt_leg]]` rows
- `tools/govkit/subject-pins.tsv`, by `govkit.py selfcheck --write`
- `memory/map/features/playbook.md`, the legs' claim
- `memory/map/generated/`, the map's generated outputs
- `tools/policy/catalogue.toml`, the two existing rows filled
- `tools/policy/unsummarised-keys.txt`, drained by `lists --write`
- `.governance/policy.json`, the second commit

### Alternatives rejected

- **The command as a verb of `govkit`.** govkit is the distribution layer, an expansion (scout B), and the
  write path is the instruction layer's.
- **Packs as policy presets.** The presets never touch `charter.practices` (v2's `[presets]`), and C1-F19
  names a pack catalogue apart from them.
- **A command that writes now and lets dDeclaredLoop's guard tighten it later.** M11 refuses every write
  until the guard lands; a write path with no guard is the surface the clause closes.

## 5. Production-readiness checklist

- security: deny by default: every write refused until the guard declares its point, and a refused policy
  read refuses every verb; the proof tests the one stream the minimal guard's hook tests, stderr (§8 F4);
  `tty-cli` proves owner presence against a cooperative agent only, the
  threat the owner accepted (v2 `[witnesses]`, SA-1).
- perf / scale: one read of every manifest per call; the merge class parses two TOML files per conflict.
- error / empty / loading states: a refused write prints the proposal so the change is never lost; an
  absent component exits 2 at load naming it; the pack check reads `unarmed` until the catalogue exists.
- observability: every refusal names the value, the missing point or the failing check, and the remedy.
- risks: a builder who edits a kit manifest by hand without a change record is caught by unit 20's status
  derivation and unit 33's step gate, not by this command.
- testing: S10's plants both ways.
- migration: none.
- user docs: `help/tags.md` says what `show` prints for a retired tag; unit 37 renders the command's
  reference page from its rows.

## 6. Acceptance criteria

- **AC1** — When `python instructions_edit.py fixture --plant merge` merges two branches
  that each add a `[[unit]]` table to one `instructions.toml`, the merged file holds both tags once, and a
  branch pair adding one tag with different bytes is a conflict the driver names.
  Red when: a tag is lost or duplicated by the merge.
- **AC2** — When `python instructions_edit.py fixture --plant propose` runs, `propose`
  prints the row diff and the command that applies it, and `git status --porcelain` in the fixture prints
  nothing.
  Red when: `propose` writes a file.
- **AC3** — When `python instructions_edit.py fixture --plant owner-propose` runs with the
  guard's point declared, a write from a terminal writes the row and a change record whose `Proof` reads
  `tty-cli`, and the same write with standard error not a terminal prints the proposal and writes nothing.
  Red when: a non-terminal call writes a row.
- **AC4** — When `python instructions_edit.py fixture --plant command-for-all` runs, a
  non-terminal write writes the row and a change record whose `Proof` reads `none — command-for-all`, and a
  write whose would-be tree fails `schema` is refused.
  Red when: a failing write is admitted, or the record's proof is blank.
- **AC5** — When `python instructions_edit.py fixture --plant flow-only` sets
  `instructions.edit` to `flow-only` with no `point.instruction.flow` declared, every verb exits 2 naming
  the absent flow component; with the point declared, a write verb exits 1 naming the flow as the writer.
  Red when: `flow-only` loads while the flow is absent, or the command writes under it.
- **AC6** — When `python tools/playbook/instructions_edit.py add --manifest playbook-render --tag unit.demo --type
  directive --level 3 --text "MUST demo."` runs on the tree at landing, it exits 1 naming
  `point.instruction.guard` and dDeclaredLoop, prints the proposal, and the manifest is unchanged.
  Red when: any write lands before the guard declares its point.
- **AC7** — When `python instructions_edit.py fixture --plant proof-values` sets
  `instructions.proof` to `signed`, then `both`, each load exits 2 naming the absent signed proof, and
  `tty-cli` loads.
  Red when: an unbuilt proof is accepted.
- **AC8** — When `python instructions_edit.py fixture --plant checks` runs, two level-3
  directives `MUST push after each pass.` and `NEVER push after each pass.` red the conflict arm, and a
  pointer to `unit.gone` with no successor reds the references arm; renaming `unit.gone` with a change
  record naming its successor clears it.
  Red when: a contradiction at one level or a stranded reference passes.
- **AC9** — When `python instructions_edit.py fixture --plant record` runs a rename and a split, the
  rename's change record names `Unit`, `Action: rename`, both pins, `Mark`, `Successor` and `Proof`, the
  split's `After` holds one pin per successor, `build_records.py read` grades each clean,
  `read_change_fields` returns the fields that verb prints, a record missing `Successor` on a rename is
  red, and the rename with no `--mark` exits 2 naming the flag and writes nothing.
  Red when: a write leaves no record, a record omits its successor, or a write runs with a record input
  absent.
- **AC10** — When `python instructions_edit.py fixture --plant packs` runs,
  `resolve_practices(["foundation"])` returns every catalogue practice tag, a pack naming `practice.nosuch`
  reds the check, and with no catalogue the check prints `unarmed`.
  Red when: a pack names an unknown practice, or an absent catalogue reads green.
- **AC11** — When `python instructions_edit.py fixture --plant retired-rows` records a rename
  of `unit.old` to `unit.new` and a split of `unit.both`, `python gov_tag.py show unit.old`
  exits 0 and prints its row of kind `retired` with the text `**Successor:** unit.new`, under `tags.slice`'s
  `leaf` and `subtree` alike, `python gov_tag.py where unit.old` exits 1, `unit.both`'s row text lists both
  successors, and new text citing `unit.old` reds `gov_tag.py check` under `tags.retired-cites`'
  default; and the case's `read_change_edges` returns the record's `Promoted-from` as a `promoted-from`
  edge at site `instructions.edit`, which `check_edges` grades clean, while the same edge read from a
  section `**Edges:**` line reds as written outside `instructions.edit`.
  Red when: a retired tag resolves as live, `show` finds no retired row, a split redirects to one
  successor, or a change record's `promoted-from` edge reds at its one writer's site.
- **AC12** — When `python -c "import tomllib; k = ('instructions.edit', 'instructions.proof'); print([(r['name'], r['owner'], bool(r.get('summary')), bool(r.get('usage'))) for r in tomllib.load(open( 'tools/policy/catalogue.toml' , 'rb'))['key'] if r['name'] in k])"`
  runs after the pass, it prints exactly two tuples, each owned by `dOrderedCharter` with both flags
  `True`; `python "tools/policy/policy.py" lists --check` exits 0; `grep -c -e instructions.edit -e instructions.proof "tools/policy/unsummarised-keys.txt"`
  prints `0`; and `git grep -n -e 'policy_reader("instructions.edit"' -e 'policy_reader("instructions.proof"' -- tools/playbook/instructions_edit.py`
  prints both lines.
  Red when: a key keeps no summary or usage, stays on the list, gains a second row, or is read in a shape
  the reader-coverage arm does not count.
- **AC13** — When
  `git grep -n -F -e "instruction edits (manifest checks)" -e "instruction edits selftest" -- tools/govkit/subject-pins.tsv tools/govkit/registry.toml memory/map/features/playbook.md memory/map/generated/MAP.md`
  runs after the pass, it prints both names in each of the four files, the registry's each a `name =`
  line of an `[[exempt_leg]]` row, and `git grep -n -F -A4 "instruction edits selftest" -- tools/gate-legs.json`
  prints the leg's `fixture` argv.
  Red when: a leg lands unpinned, unclaimed, missing from the dossier, or claimed with the map not
  regenerated, or no leg runs the plants.
- **AC14** — When `python tools/memory-tree/build_records.py --fixture --plant typed-kinds` runs, it
  exits 0 with `change` read `bound`; `python tools/memory-tree/build_records.py new change --help`
  lists `--tag` and no `--principle`; `python tools/playbook/instruction_units.py fixture --plant status`
  exits 0, a committed change record retiring its unit at render and a malformed one redding
  `--check-render`; and `git grep -n -e derive_status_note -e "status: unarmed" -- tools/playbook`
  prints nothing.
  Red when: `unarmed` outlives the pending row, a malformed record reads green, or a door takes
  another door's flags.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `spec tokens (a spec's own names resolve)` · `policy fixtures` · `govkit selftest` · `govkit refusal join` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness`

New arm: tools/playbook/instructions_edit.py · covers AC1 AC2 AC3 AC4 AC5 AC7 AC8 AC9 AC10 AC11 · the `instruction edits selftest` leg running every `fixture` case, each failing case staged by its plant · none

New arm: tools/gate-legs.json · covers AC6 · the `instruction edits (manifest checks)` leg over the tree, its failing case a write admitted while the guard's point is undeclared · none

New arm: tools/memory-tree/build_records.py · covers AC14 · the `typed-kinds` plant's `change` door, its failing case a door handed another door's flags · none

New arm: tools/playbook/instruction_units.py · covers AC14 · the rewritten `status` case under `instruction units selftest`, its failing case a malformed change record · none

## 8. Open questions

- **F1** — How does the command know dDeclaredLoop's guard and flow have landed, given neither exists and
  no S-interface names them?
  RESOLVED (agent, 2026-10-23, delegated): rung 3, the most feature-rich survivor: a point a core row of
  the layer register declares (S3, S4), read through unit 16's register, which P28 makes the one place a
  component attaches; dDeclaredLoop declares `point.instruction.guard` and `point.instruction.flow` when
  it lands, and a fixture repository declares them in its own register to stage each arm, so no test
  switch ships.
- **F2** — `instructions.proof` allows `signed` and `both`, and v2 places the layered proof in `[planned]`.
  Options: build a signed proof here; refuse both at load as an absent component.
  RESOLVED (agent, 2026-10-23, delegated): rung 1, v2 `[witnesses]` answers it: the owner keeps `tty-cli`
  and the layered proof waits in `[planned]`. Both refused at load (S5), the mechanism L3 gives
  `flow-only`.
- **F3** — With every write refused until the guard lands, how does a build's builder record a kit
  manifest change?
  RESOLVED (agent, 2026-10-23, delegated): rung 1, memory-plan `[doors]` answers it: `instructions.edit`
  writes change records, and a stand-in door serves until the record door adopts it; the S12 factory's
  `new change` verb is that door (S7), and the command uses the same kind once it writes.
- **F4 — How does the command prove `tty-cli`, when the guard's test is inline shell?** dGroundRules'
  minimal guard tests `[ -t 2 ]` inside `.githooks/pre-commit` (TOOL-dGroundRules-6 S4, its §8 F3) and
  lands no callable a Python command can run, so rev-3's "called through that guard's one
  implementation" has nothing to call, and rev-3 named the other stream, standard input. Options:
  (a) this unit's own proof, `sys.stderr.isatty()`, testing stderr as the hook does, stated in S5 and on
  the command's page as the second implementation of one signal; (b) an ask to dGroundRules to move
  the hook's test into a callable in `tools/policy/` that the hook and this command both run; (c) wait
  for dDeclaredLoop's TTY CLI and refuse every write until then. (b) is the one-implementation shape,
  but it moves a landed parent's hook seam for one consumer; (c) leaves `tty-cli` with no
  implementation, so AC3's owner arm has nothing to observe even with the guard's point declared.
  Recommendation (a): one stream, stderr, named once, and the second spelling is one call.
  RESOLVED (owner, 2026-10-25): (a). PLAY-dOrderedCharter-7's `core.exceptions: owner-only-expiring`
  proof is this check.
- **F5** — How does the change-record extractor register, and where does a retired tag's redirect live?
  A namespace row holds one `extractor` (`tag_index.py:133`, read by `read_namespaces` `:118-140` and
  `load_extractors` `:179`); `unit`'s claims only manifests; the index schema holds no successor
  (`:72-85`); `show` prints tag, path, kind and text (`gov_tag.py:77-86`) of the rows
  `tools/playbook/tag_index.py#resolve_address` returns, none of them `retired`. Options: (a) `extract_unit`
  also claims change records, its `retired` row's text the `Successor` line; (b) a new namespace row for
  change records; (c) a successor table in the index.
  RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. (b) lost on `read_namespaces`: a row's `ns` is a
  word tags open with, and a change record mints no tag of its own, only retired `unit.*` tags, so the
  row would register a word nothing opens with and owe unit 22's `purpose-source` for members that do
  not exist. (a) and (c) both need a `show` change, S9's fallback, so that change decides nothing. (c)
  lost on the schema: a table needs an `INDEX_SCHEMA` bump (`tag_index.py:88`), which rebuilds every
  node's index, while the `text` column already carries the line. widens: none · relaxes: none
- **F6** — Section 7's first `New arm:` line says a leg runs every `fixture --plant` case, S10 lands one
  leg running the check, and no bar leg runs the plants. Options: (a) a second leg,
  `instruction edits selftest`, with its own rows; (b) the one leg also running the fixture; (c) the
  plants joining unit 20's `instruction units selftest` through
  `tools/playbook/instruction_units.py#PLANTS`.
  RESOLVED (agent, 2026-11-04, delegated): (a), the most feature-rich survivor. It satisfies every
  criterion, a later unit's case joins by joining this module's table, as units 45 and 52 do, and it
  repeats unit 20's split of a tree leg from a selftest leg, at the cost of one more row in each of
  three files. (b) lost on the row: one leg holds one `chunk` and one `subject`, so the plants would
  sit in `declarations` as `repo`, and a plant's red would read as the tree's. (c) lost on the
  direction: `instructions_edit.py` imports `instruction_units.py`, so a delegating row would make the
  lower module's fixture reach its consumer, and every case of this module would count as one
  expectation there. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the spec run's carrier of `cl-dClosedLoop-0045`.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-40, PLAY-dOrderedCharter-42, PLAY-dOrderedCharter-45, PLAY-dOrderedCharter-46, PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-50.
- rev-4 · 2026-10-24 · §2 S5, S10, S11 (new) · §3 Edges · §4 Rollout, Files touched · §5 security · AC3, AC12 (new) · §8 F4 (new, open for the owner) · §10 · re-grounded on the parents' landed specs by `2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck` row 40, U3 and U4: the proof tests stderr, the guard's stream, and how it is run is F4's; both keys are read through `policy_reader`, and a refused read refuses; the two landed rows are filled and drained, never added.
- rev-5 · 2026-10-25 · Status (ratified) · §2 S5 · §8 F4 · §10 · the owner's answer to F4, item 1 of `2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks`: (a), the command's own check that stderr is a terminal, stated directly where S5 and the reuse audit pointed at the open fork.
- rev-6 · 2026-11-03 · §7 · from `2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md` Item 2: the leg line names `policy fixtures`, whose guard a §4 Files touched path trips, the guards hit the spec-token check reads with DEFERRED as live.
- rev-7 · 2026-11-03 · S3 S4 S5 S7 S9 S10 · §3 Edges · §4 · AC6 AC11 AC12 AC13 (new) · §7 · §8 F5 (new) ·
  §10 · from `2026-11-03-prompt-PLAY-dOrderedCharter-9-drift-fold-brief.md` items 15-1 to 15-8: the unit
  extractor claims change records and the redirect is the retired row's text (F5); a change-record
  adapter tags `promoted-from` at its writer's site; the leg's exempt, pin and dossier rows land in this
  pass with the legs they trip; the manifest id is `playbook-render`; the points are `point.instruction.*`;
  the reader is unit 19's `read_policy_value` and the normaliser `design_lib.derive_pin_hash`; and §10's
  lines and AC12's note are re-read.
- rev-7 · 2026-11-03 · S9 · from `2026-11-03-prompt-PLAY-dOrderedCharter-9-readers-brief.md`: S9's
  `**Readers:**` clause escapes the by-name half, the item retiring no name, and names the retired rows'
  value readers.
- 2026-11-04 · section 3 Edges · from `2026-11-04-prompt-PLAY-dOrderedCharter-15-edge-mirror-brief.md`: the hands-off mirror of the consumes-from edge unit 52 declares against this unit; a mirror-only edit, so the status line keeps its rev.
- rev-8 · 2026-11-04 · S7 · section 3 · from `2026-11-04-prompt-PLAY-dOrderedCharter-20-divergence-brief.md`: S7 and the consumes-from line for unit 20 take the body of `read_change_records`, which this unit replaces when it lands the `change` kind.
- rev-9 · 2026-11-04 · section 4 Files touched · from `2026-11-04-prompt-PLAY-dOrderedCharter-20-3-sweep-fix-brief.md` item 1: the line names the map's generated outputs and not the generator, which the pass runs and never writes, so the three legs guarding the map kit stay untripped; no S or AC id moved.
- rev-10 · 2026-11-04 · S2 S7 S9 S10 S14 (new) · section 4 · section 5 · AC1 AC9 AC11 AC13 AC14 (new) · section 7 · F5 F6 (new) · section 10 · from `2026-11-04-prompt-PLAY-dOrderedCharter-15-divergence-brief.md`: `show` alone falls back to `retired` rows; each field is the factory's bullet; a second leg runs the plants (F6); the `change` kind's landing is stated whole, the status note deleted; the write verbs' inputs are flags tested after the guard, and `After` on a split is a list of pins; AC1's pair has different bytes; the kickoff manifest takes its stamp.

## 10. Reuse audit

The seams extended are `tools/memory-tree/merge-rows.py`, the row-keyed driver R-I and the research's
pick name for manifest merges (its `key` at line 232 anchors a markdown row; S1 adds a TOML-table class
beside its three), the `.gitattributes` `merge=rows` lines (77, 78 and 84, under the comment at 67),
`extract_unit` and `check_retired` for the retired rows, the `show` branch of
`tools/playbook/gov_tag.py#run_kit_verb` for the redirect, `read_tree_edges`' adapters for the change
record's edge, unit 7's record factory for the
`change` kind, and the stream dGroundRules' minimal guard tests for the TTY proof. No TTY proof exists
in the tree today (scout A: no `isatty` under `tools`), and the guard's lands as `[ -t 2 ]` inline in
`.githooks/pre-commit` (TOOL-dGroundRules-6 S4), no callable, so this unit writes a second test of the
same stream (§8 F4, the owner's pick).
`python tools/codebase-map/reuse_lookup.py "an owner-only command that adds edits and removes instruction rows
and records each change"` ranked name-token matches (`rows`, `records`, `changed`), none a guarded write
path, so no existing seam fits the command itself.

Recall terms used: `python tools/memory-recall/query.py "how does the owner change an instruction and how is an agent kept to proposing" --terms "instructions.edit instructions.proof tty-cli owner command propose change record manifest guard flow-only pack"`
