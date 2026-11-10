# PLAY-dOrderedCharter-31 — this build's own upgrade steps: the agent-instructions wiring to the one renderer, adopter rules into the overlay, the seeded template's succession row, the census's change records and the `map_lib` deprecation

**Status:** DEFERRED · rev-12 · 2026-11-09 · node d · Tier-2 · base ce13efbe · streams playbook · order 36 · advances PLAY-dOrderedCharter-38 · ratified 2026-10-25

**Carries:** cl-dClosedLoop-0061@bf1a53b5 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-c.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-c.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-build-PLAY-dOrderedCharter-31-deviation-311.md](../build/2026-10-24-build-PLAY-dOrderedCharter-31-deviation-311.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-31-deviation-312.md](../build/2026-10-24-build-PLAY-dOrderedCharter-31-deviation-312.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-31-deviation-313.md](../build/2026-10-24-build-PLAY-dOrderedCharter-31-deviation-313.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 |
| [2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-25-build-PLAY-dOrderedCharter-31-deviation-314.md](../build/2026-10-25-build-PLAY-dOrderedCharter-31-deviation-314.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-31-deviation-315.md](../build/2026-10-25-build-PLAY-dOrderedCharter-31-deviation-315.md) | deviation | — |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-31-1-spec-writer.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-31-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md](../prompts/2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-46 |
| [2026-11-02-prompt-PLAY-dOrderedCharter-31-build-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-31-build-brief.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md) | research | PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-11-08-prompt-PLAY-dOrderedCharter-46-drift-fold-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-46-drift-fold-brief.md) | research | PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-37 |
| [2026-11-09-prompt-PLAY-dOrderedCharter-31-1-spec-writer.md](../prompts/2026-11-09-prompt-PLAY-dOrderedCharter-31-1-spec-writer.md) | journal | — |
| [2026-11-09-prompt-PLAY-dOrderedCharter-31-2-spec-writer.md](../prompts/2026-11-09-prompt-PLAY-dOrderedCharter-31-2-spec-writer.md) | journal | — |
| [2026-11-09-prompt-PLAY-dOrderedCharter-31-3-spec-writer.md](../prompts/2026-11-09-prompt-PLAY-dOrderedCharter-31-3-spec-writer.md) | journal | — |
| [2026-11-09-prompt-PLAY-dOrderedCharter-31-park-record-brief.md](../prompts/2026-11-09-prompt-PLAY-dOrderedCharter-31-park-record-brief.md) | research | — |
| [2026-11-09-prompt-PLAY-dOrderedCharter-31-repair-2-brief.md](../prompts/2026-11-09-prompt-PLAY-dOrderedCharter-31-repair-2-brief.md) | research | — |
| [2026-11-09-prompt-PLAY-dOrderedCharter-31-repair-brief.md](../prompts/2026-11-09-prompt-PLAY-dOrderedCharter-31-repair-brief.md) | research | — |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

Every adopter-visible surface this build takes away ships with the row that carries an adopter across
it, through dSafePassage's step kind (`cl-dClosedLoop-0018`), so `update` walks an adopter from today's
install to this build's and dSafePassage's step gate stays green only because each row exists. Five
surfaces move: the agent-instructions kit, whose wiring the one renderer absorbs (unit 20); the
repository's `[charter] adopter_rules`, which become level-0 `repo.` units of its overlay (unit 32); the
seeded charter template (unit 34 stops reading it); the practices the census moves out of the shipped
set (unit 34); and the names `map_lib` re-exports after unit 19 moves them. P38: "a build that changes
what an adopter can see ships its successor with an upgrade step that runs up and down".
Re-read at c0800e284, two of the five take no member away: PLAY-dOrderedCharter-34's project block
still reads `[charter] adopter_rules`, so the conversion step moves an adopter's rules and leaves the key a live
input (section 8, F8), and the census moves no practice (PLAY-dOrderedCharter-34's census record).

## 2. Scope (IN)

- **S1** — The agent-instructions kit carried to its successor. Its registry entry
  (`tools/govkit/registry.toml:106-107`) and its `[[exempt_leg]]` row (`:523`) leave the registry, its
  directory `tools/agent-instructions/` leaves the tree, its two legs leave `tools/gate-legs.json`
  (`:293`, `:382`) with their rows in `tools/govkit/subject-pins.tsv`,
  `tools/run-gates/ceiling-evidence.txt` and `tools/run-gates/selftest-budgets.txt`, and a
  `[[retired]]` row names it: `id = "agent-instructions"`, `successor = "playbook-render"`, `surfaces`
  the members `step_gate.py --list` prints for the entry at the base. `CODEX_MAX` moves into the module
  unit 20 absorbed the wiring into, and unit 6's check and unit 34's render read it there. The same
  commit re-points `tools/policy/caps.toml`'s `codex-instructions` row, its `enforcer` to that module
  and its `home` to `constant:<that module>:CODEX_MAX`, and the census's
  `budgets-cap-codex-instructions` case in `tools/policy/check_policy.py` to that enforcer, so
  `arm_cap_census`'s join both ways holds (TOOL-dGroundRules-9 S1, S7, `:175`).
  Re-read at c0800e284, that module is `tools/playbook/render_playbook.py`, whose
  `tools/playbook/render_playbook.py#run_entry_files` holds the absorbed wiring. The row's `kit` and `installed` keys name the
  agent-instructions kit and its adopter as well, so they move in the same commit: `kit` to
  `playbook-render` and `installed` to the renderer's `{prefix}` path, as the `one-line-rule` row
  spells both. The case's plant, the `codex-instructions` branch of
  `tools/policy/check_policy.py#derive_outside_probe_plant`, runs the adopter under `bash` over an
  `AGENTS.md` past CODEX_MAX. With the renderer as the enforcer it renders a template past
  CODEX_MAX instead and expects the render's harness-limit refusal naming CODEX_MAX under both
  `warn` and `refuse`, the same answer an outside row gives under each. That plant's scaffold is the
  one `tools/policy/check_policy.py#derive_one_line_rule_plant` builds: the engine copy, the policy
  kit, the modules the render imports, and the template beside the engine. At this second instance
  the scaffold becomes a factory, `derive_render_plant`, which both plants call. The composition
  fixture's over-Codex arm, `tools/playbook/fixtures/composition.py#arm_over_codex`, prints the
  refusal line the case reads. At the build run's
  base §4's first query also hits that row and its case, and the policy file, whose `AGENTS.md`
  comment block names "the agent-instructions kit's CODEX_MAX" once TOOL-dSafePassage-1 S7 carries it
  there: argued history in a guarded file, kept.
  Re-read at 05fd1b7f7, the query also hits rows that red a leg once the directory is gone, each
  written in the same commit. The `policy fixtures` leg's guard in `tools/gate-legs.json` names the
  adopter and the kit's descriptor, two entries that go with the directory. The docs leg reports
  `memory/project/docs-undocumented.txt`'s `entry:agent-instructions` row as an orphan once the
  entry leaves the registry, so the row goes. The arms check reds `.memory-tree.conf`'s
  `ARMS_FLOORS` entry for the adopter once that gate leaves its population, so the entry goes; that
  takes the citation out of `.memory-tree.conf`, and `memory/project/positional-refs.txt`'s row for
  it goes stale, so the pass runs `python tools/playbook/positional.py shrink`. `core.py meta-check`
  reds a `leg` row of `tools/playbook/core-pending.txt` naming no leg, so each departing leg's row
  goes with it. `tools/playbook/instruction_units.py#arm_no_renderer`, the fixture's `no-renderer`
  plant, copies the adopter and asserts its refusal, and reds with the adopter gone, so the plant
  and its row in that module's `PLANTS` go, and the `why` of `instruction units selftest`'s
  `[[exempt_leg]]` row in `tools/govkit/registry.toml` stops naming the plant and this kit. The rows
  of the lint and arms waiver lists that name the deleted files are the owed-rows probe's "path
  deleted" population (unit 50's edge). `.governance/install.json` is gov's receipt, rewritten by
  the update that carries the claim, never by hand. Kept as history:
  `tools/govkit/fixtures/release-0/deploy.toml`, the release-0 adopter AC3's scratch adopter
  installs with this kit claimed; `tools/template-size-limits.txt`'s comment; and the record rows of
  `memory/project/positional-refs.txt`, whose citing records do not change. `CODEX_MAX` is still
  assigned in the adopter at 05fd1b7f7. At c0800e284 `tools/check-template-size.sh` names the kit
  nowhere and CODEX_MAX only as the shell variable it fills from
  `budgets.py home codex-instructions`, and `tools/check-template-size.test.sh` copies the file the
  census row's `home` names: PLAY-dOrderedCharter-6's check and its test follow the census row, so re-pointing the
  row moves both readers too.
  **Readers:** by name: `tools/govkit/registry.toml`, `tools/gate-legs.json`,
  `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt`,
  `tools/run-gates/selftest-budgets.txt`, `tools/govkit/selftest.py`, `tools/govkit/govkit.py`,
  `README.md`, `WIRE-INTO-PROJECT.md`, `AGENTS.md`, `.governance/deploy.toml`,
  `.claude/rules/product.md`, `.lexicon.conf`, `.memory-tree.conf`, `memory/map/baseline.toml` and
  `memory/map/features/roles.md`, each a hit of §4's first query at the base, and at 05fd1b7f7
  also `.governance/install.json`, `help/size-caps.md`, `memory/project/docs-undocumented.txt`,
  `memory/project/positional-refs.txt`, `memory/project/spawn-idiom-sites.txt`,
  `memory/project/testsuite-count-waivers.txt`, `memory/project/unarmed-branches.txt`,
  `tools/govkit/fixtures/release-0/deploy.toml`, `tools/playbook/README.md`,
  `tools/playbook/core-pending.txt`, `tools/playbook/instruction_units.py`,
  `tools/playbook/render_playbook.py`, `tools/policy/caps.toml`, `tools/policy/check_policy.py` and
  `tools/template-size-limits.txt`, and at c0800e284 also `help/charter.md`,
  `help/composition.md`, `tools/check-template-size.sh`, `tools/check-template-size.test.sh`,
  `tools/playbook/adopt-playbook.sh`, `tools/playbook/fixtures/composition.py` and
  `tools/playbook/load_sets.py`, each spelling CODEX_MAX, whose name the move keeps; the
  `no-renderer` plant's name is spelled by
  `tools/playbook/instruction_units.py` and `tools/govkit/registry.toml` alone · by value: unit 6's
  check, which holds the harness limit through `CODEX_MAX`, and `print_size_note`'s announce, which
  the render's harness-limit refusal replaces (unit 34), and the `instruction units selftest` leg,
  whose verdict counts the `no-renderer` plant. Observed by AC1, AC2, AC3 and AC13.
- **S2** — The by-value inventory, derived by §4's queries over the tree at the pass and never copied
  into a file; root `README.md`'s line 17 is among its hits. Each hit is re-pointed to the renderer,
  re-worded where it states where the wiring lives, or kept where it narrates history, and the pass
  commit's `Decided:` trailer names each kept hit. Observed by AC2.
- **S3** — The `map_lib` re-export declared as a deprecation. A `[[class]]` row `module-export` joins
  dSafePassage's class registry `tools/govkit/surface-classes.toml`: its reader returns each name
  `tools/codebase-map/map_lib.py` re-exports from the join factory unit 19 moves to `tools/lib/`, and its
  plant stages one re-export taken away, so the names leave only with a row naming them. The names
  are held for `install.deprecation-window` releases, which dConvergedCharter counts from this row's
  landing commit on the default branch (§8 F6, the owner's pick); no `[[shim]]` row holds them. The same commit writes the
  class's `[[class]]` row in `tools/govkit/usage.toml`, usage shape `none` with a `why`, since a
  docs leg finding is a registered class with no row there (TOOL-dSafePassage-13 S1, S8) and an
  import name fits none of its S2 shapes. Re-read at 05fd1b7f7, the names are the four
  `tools/codebase-map/map_lib.py` imports from the memory-tree kit's `coverage_join.py`, the inline
  copy whose canonical source is `tools/lib/coverage_join.py`: `Coverage`, `compute_coverage`,
  `drop_touched_exemptions` and `resolve_compare_base`, so the class's population is not empty.
  Observed by AC4 and AC14.
- **S4** — The adopter rules into the overlay, by a step whose down restores them. An `[[upgrade]]` row
  `playbook/adopter-rules-to-overlay` in `tools/govkit/entries/playbook.kit.toml`, its program
  `tools/govkit/steps/adopter_rules_to_overlay.py`: its up turns each `- ` line of
  `[charter] adopter_rules` in `.governance/deploy.toml` into one level-0 `repo.` unit of
  `.governance/instructions.toml` and takes the key out of the descriptor; its down restores both files
  byte-identical from the before-image; its witness holds when the key is absent and every line it held
  is a unit's text. The row's `surfaces` is `[]`, the declared absence the step grammar admits
  (`tools/govkit/upgrade_steps.py#check_surfaces`): the step moves an adopter's rules and takes no
  member of gov's product away, so no class row is written for it (section 8, F8). The
  `ADOPTER_RULES` placeholder row (`tools/govkit/entries/playbook.kit.toml:273-277`) stays as
  PLAY-dOrderedCharter-34 landed it. Re-read at c0800e284, three readers need it:
  `tools/playbook/render_playbook.py#render` refuses a template token no row declares, and the
  template carries `{{ADOPTER_RULES}}`; `tools/playbook/render_playbook.py#build_project_block`
  takes the row's key and its default bullet, the one route a level-0 unit renders through; and
  `tools/playbook/render_playbook.py#read_charter_table` refuses a `[charter]` key no row declares,
  which an adopter that has not yet run the step still answers. The block renders the key's lines
  and then the units, so the step's up leaves the rendered rules and their order as they were. That
  holds through two properties of the rows the step writes. The block renders the level-0 units
  `tools/playbook/instruction_units.py#derive_unit_selection` keeps under its every-reader selector,
  which keeps a unit only when its `scope` holds the selector or `reader.every`, so each converted
  row carries `scope = ["reader.every"]`. It renders them in overlay row order, and
  `tools/playbook/overlay.py#derive_overlay_text`, which `write_overlay_units` calls, places each new
  row by level then tag. So each converted row's tag carries an ordinal segment that sorts in rule
  order, `repo.rule-<NN>-<seg>`, whose grammar section 4 "The adopter-rules step" states. The
  key keeps every reader it has. **Readers:** by name: `tools/playbook/render_playbook.py`,
  `tools/playbook/fixtures/composition.py`, `tools/playbook/README.md`, `help/composition.md`,
  `tools/govkit/entries/playbook.kit.toml`, `WIRE-INTO-PROJECT.md`, `.claude/rules/product.md` and
  `.governance/deploy.toml` · by value: `read_charter_table`
  (`tools/playbook/render_playbook.py:809`) and the project block, which render the key's lines
  ahead of the overlay's level-0 units; `tools/playbook/instruction_units.py#derive_unit_selection`,
  which keeps a converted row by its `scope`; and `tools/playbook/overlay.py#derive_overlay_text`,
  which orders the converted rows by their tags. Observed by AC5, AC6 and AC7.
- **S5** — The seeded charter template's succession row. A `[[retired]]` row in
  `tools/govkit/registry.toml`, `id = "playbook/seeded-template"`, `successor = "none"`, `surfaces` the
  members the step gate lists for the seed rule at the base, and the seed's `[[files]]` rule
  (`tools/govkit/entries/playbook.kit.toml:23-26`) and its hole leave the playbook descriptor. An
  adopter's seeded copy that it edited becomes `retired-edited`, kept and ordered as
  `install.retired-edits` says (TOOL-dSafePassage-9), never deleted; one it never edited reads
  `withdrawn`: TOOL-dSafePassage-9's 2026-10-25 revision routes a retired seed row through its
  `retired-edited` arm (§8 F7, the owner's pick). Its readers are inventoried by path and by value by §4's
  second query. Re-read at c0800e284, those two verdicts do not hold: TOOL-dSafePassage-9 reads a
  seed row as retired only where gov holds no blob at the row's `source`, and the renderer kit
  ships the same root template beside its engine (section 8, F9).
  The seed rule's leaving moves three more rows, each in the same commit, found by reading the code
  at c0800e284. First, the `playbook` entry then lands no file while its `version_from` names the
  template. The version-constant arm of `tools/govkit/govkit.py#selfcheck` fails an entry whose
  `[[files]]` rules do not land the file its `version_from` names, and
  `tools/govkit/govkit.py#resolve_entry` over the descriptor with its `[[files]]` emptied returns
  no write (PINNED, probed at c0800e284; the probe ran the resolver, never the selfcheck leg). So
  `version_from` becomes `{ none = "<reason>" }`, the declared absence that arm and the marker arm
  both pass over, as fifteen tracked files under `tools/` spell it (PINNED, counted at
  c0800e284). The scope arm derives `repo` from an entry with no rule, the value the entry
  declares, and no arm grades an entry that lands no file. The `[adopt]` and `[check]` texts that
  call installation a copy to an owner-chosen path are re-worded.
  Second, the hole `playbook-placeholders` probes the seeded copy at `{playbook_path}`, so it leaves
  the descriptor with the rule, and the two arms of
  `tools/govkit/selftest.py#check_playbook_hole_modes` that assert its verdicts go with it. The same
  function's `[charter]` arm needs a key a selected kit's argv or destination names, and with
  `kits = ["playbook"]` none is left, so it selects `kickoff-manifest` and answers its
  `manifest_path`, which `tools/govkit/govkit.py#needed_answers` returns at c0800e284. Third, the
  `micro-format definitions` leg of `tools/govkit/entries/check-microformats.kit.toml` passes
  `{playbook_path}` as its subject, a file a new adopter no longer holds, and its own comment records
  that a leg naming a path no adopter has exits 2 on install day. Its subject becomes the template
  the renderer kit lands beside its engine, `{prefix}/playbook/coding-governance-agents.template.md`
  (PLAY-dOrderedCharter-34, S5), the file `tools/check-microformats.sh` grades when gov runs it with
  no argument, and its `requires` becomes `playbook-render`, the entry that lands that file.
  `tools/playbook/instruction_units.py` and `tools/policy/check_policy.py` spell `playbook_path` no
  more at c0800e284, PLAY-dOrderedCharter-34's F7 having moved their fixtures' templates.
  **Readers:** by name: `tools/govkit/entries/playbook.kit.toml`, `tools/govkit/govkit.py`,
  `tools/govkit/matrix.py`, `tools/govkit/selftest.py`, `tools/check-placeholders.sh`,
  `tools/govkit/entries/check-microformats.kit.toml`, `tools/playbook/README.md`,
  `WIRE-INTO-PROJECT.md`, `tools/govkit/fixtures/release-0/deploy.toml`, the release-0 adopter's
  answer, kept, `tools/playbook/render_playbook.py`, `tools/playbook/kit.toml`,
  `tools/playbook/fixtures/composition.py`, `help/charter.md` and `help/roles.md`, each spelling
  `playbook_path` at c0800e284; and for the hole's id, `tools/govkit/entries/playbook.kit.toml`,
  `tools/govkit/selftest.py`, `tools/govkit/govkit.py`, `tools/check-placeholders.sh`,
  `tools/playbook/README.md` and `memory/map/features/lexicon.md` · by value: the seed row's
  `reseed-available` grade (`tools/govkit/govkit.py:9989-9990`), which at c0800e284 sits in
  `tools/govkit/govkit.py#_cmd_update` and still grades an adopter's seed row while gov holds a blob
  at its source; the `micro-format definitions` leg, which grades the file at `{playbook_path}`; and
  the `[charter]` argv-token finding of `tools/govkit/govkit.py#cmd_check`, which reads the tokens
  the seed rule's destination needed. Observed by AC8, AC9 and AC15.
- **S6** — A change record for every unit the census moves out of the shipped set (unit 34, S8), in
  the change record kind unit 15 writes (S12, S13), each `mark = semantic` and `successor = none`.
  Re-read at c0800e284, that population is empty, and this unit says so rather than read it as
  coverage. PLAY-dOrderedCharter-34's census record, and `tools/playbook/practice_census.py` run at
  c0800e284, rule one row `gov-only` with the disposition `stays` and move none (PINNED: the
  summary line reads `moves 0 · moves, row kept 0`). So the pass writes no change record. The step
  gate registers no `unit` class either: PLAY-dOrderedCharter-33's F5 lands that class row in a later
  commit of its own, once PLAY-dOrderedCharter-40 tracks the first gov unit row, and that unit's AC7
  sees a gov unit tag taken away with no change record go red. This unit observes only that the
  census moves nothing at its pass; a census that moves a row there is a hand-back, since no class
  could see its record. Observed by AC10.
- **S7** — Gov first. Every step of S1, S4 and S5 runs on gov's own tree before any adopter meets it,
  as `cl-dClosedLoop-0025` runs every step in the lander's prepared merge, and gov's source-mode
  receipt lists each step id. Observed by AC11.
- **S8** — The page: `help/upgrade-steps.md` (TOOL-dSafePassage-1's) gains one section naming this
  build's steps and what each does to an adopter's tree. Observed by AC12.

## 3. Non-goals (OUT)

- The step kind, its reader, the walk, the before-image helpers, the step gate and its nine classes,
  `retired-edited` and the order writer: dSafePassage's (TOOL-dSafePassage-1, -2, -9, -10). This unit
  writes rows in their grammar and one class row through their extension point.
- Absorbing the wiring into the renderer and the render gate: unit 20's. Composing the project block
  and dropping the seeded template as the render's input: unit 34's. The census's rulings: unit 34's.
- The `map_lib` re-export itself: unit 19's. Counting its window: dConvergedCharter (§8 F6).
- Taking a re-export away when its window closes, and the `module-export` row with the last one:
  dConvergedCharter.
- A legacy block for an adopter's own instruction files: dLinkedLibrary.
- Taking `[charter] adopter_rules` out of the render's inputs, and the project block's reading of the
  `ADOPTER_RULES` row: CLOSED PLAY-dOrderedCharter-34's mechanism, which a new unit would change
  (section 8, F8).
- Changing how `govkit update` grades a seed row gov still holds a source for: dSafePassage's
  TOOL-dSafePassage-9 arm (section 8, F9).

### Edges

- **consumes-from** external — TOOL-dSafePassage-9's 2026-10-25 revision (`2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md`, Item 5): a retired seed row routed through its `retired-edited` arm, an edited copy reading `retired-edited` with one order and an unedited one `withdrawn`, which AC9 expects; without it the seed override grades the edited copy `patched`
- **consumes-from** `PLAY-dOrderedCharter-20` — the renderer that absorbed the agent-instructions wiring, which the kit's successor ships
- **consumes-from** `PLAY-dOrderedCharter-32` — the overlay file and the level-0 `repo.` unit grammar the adopter-rules step writes, through `write_overlay_units`
- **consumes-from** `PLAY-dOrderedCharter-34` — the seeded template no longer read and the census's moved units, none at c0800e284; the template the renderer kit ships beside its engine, which the render reads once S5 takes the seed rule out and the micro-format leg grades; the project block, which reads the `ADOPTER_RULES` row S4 keeps; and the render's harness-limit refusal, which the re-pointed census case observes
- **consumes-from** `PLAY-dOrderedCharter-15` — the change record kind S6 would write, for no unit while the census moves none
- **consumes-from** `PLAY-dOrderedCharter-33` — the step gate's gov unit-tag class, witnessed by the change record; its class row lands in that unit's later commit, and its AC7 observes the red S6 owes no record for
- **consumes-from** `PLAY-dOrderedCharter-19` — the join factory's move and `map_lib`'s re-export
- **consumes-from** `PLAY-dOrderedCharter-6` — the check that reads `CODEX_MAX`, re-pointed with the constant
- **consumes-from** external — dSafePassage's step kind, step gate, class registry, `retired-edited` and the `upgrade-walk` leg (TOOL-dSafePassage-1, -5, -9, -10), built before this build's build run; dGroundRules' minimal guard (`cl-dClosedLoop-0012`), which the lander's prepared merge never fires (TOOL-dGroundRules-6, `:105-107`); and its cap census `tools/policy/caps.toml` with `arm_cap_census` (TOOL-dGroundRules-9)
- **hands-off** `PLAY-dOrderedCharter-39` — S1's leg removal and moving list: the agent-instructions wiring leg keeps its name on the renderer, and the card import moves by name beside CODEX_MAX (finding 1)
- **consumes-from** `PLAY-dOrderedCharter-46` — the candidate read, which S4's step re-renders through over the overlay it has just written (finding 80)
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 10, 21 and 71, which that batch unit corrects after this unit lands, each by the item its report id names
- **consumes-from** `PLAY-dOrderedCharter-50` — the owed-rows probe: this pass runs `python tools/run-gates/owed_rows.py --base HEAD` before its commit and writes every row it names in that commit (round-2 id 23), every registry row naming the deleted directory and every row of a retired leg among them
- **hands-off** `PLAY-dOrderedCharter-55` — AC12's pathspec, which unit 49 S24 corrects, is observed at `PLAY-dOrderedCharter-49`'s pass and recorded from that observation; this pass changes no code to satisfy it (round-2 id 2); and unit 39's option probe reads the adopter at this pass's parent (round-2 id 1)

## 4. Design

### The rows

```toml
# tools/govkit/registry.toml
[[retired]]
id = "agent-instructions"
successor = "playbook-render"
surfaces = ["entry:agent-instructions"]          # plus every member `step_gate.py --list` prints for it

[[retired]]
id = "playbook/seeded-template"
successor = "none"
surfaces = []                                     # every member the gate lists for the seed rule at BASE

# tools/govkit/entries/playbook.kit.toml
[[upgrade]]
id = "playbook/adopter-rules-to-overlay"
up = ["python", "{gov}/govkit/steps/adopter_rules_to_overlay.py", "up", "{target}"]
down = ["python", "{gov}/govkit/steps/adopter_rules_to_overlay.py", "down", "{target}"]
witness = ["python", "{gov}/govkit/steps/adopter_rules_to_overlay.py", "witness", "{target}"]
surfaces = []                                     # the key stays a live input of the render (S4, F8)
needs-target = false

# tools/govkit/surface-classes.toml
[[class]]
id = "module-export"
reader = "{prefix}/codebase-map/map_lib.py:read_module_export_members"
plant = "{prefix}/codebase-map/map_lib.py:write_module_export_plant"
summary = "each name map_lib re-exports from the join factory, held for install.deprecation-window"

# tools/govkit/usage.toml
[[class]]
class = "module-export"
usage = "none"
why = "an import name a module keeps for older callers has no verb, key, hook, leg or page"

# tools/policy/caps.toml, the codex-instructions row's four moved keys (S1)
enforcer = "{prefix}/playbook/render_playbook.py"
home = "constant:{prefix}/playbook/render_playbook.py:CODEX_MAX"
kit = "playbook-render"
installed = "{prefix}/playbook/render_playbook.py"

# tools/govkit/entries/playbook.kit.toml, with the seed rule and its hole gone (S5)
version_from = { none = "<why the entry carries no constant once it lands no file>" }

# tools/govkit/entries/check-microformats.kit.toml (S5)
requires = ["playbook-render"]
argv = ["bash", "{prefix}/check-microformats.sh", "{prefix}/playbook/coding-governance-agents.template.md"]
```

Re-read at `05fd1b7f7`, the landed rows set the shape. Every `surface-classes.toml` row spells its
functions `{prefix}/<kit>/<file>:<function>`, and the step gate's own pairs are named
`read_<class>_members` and `write_<class>_plant`, so the new pair takes those names. A `none` row
of `usage.toml` carries no `rows` key: `file` and `installable` carry none, and the file's header
says a `page` or `none` class carries none.

The `surfaces` lists are written from `python tools/govkit/step_gate.py --list` run at the base, so
every member is spelled as the gate spells it and none is typed from memory. A class reader lives
beside the parent's nine class readers (TOOL-dSafePassage-10, `:99-100`) or in the module whose names
it reads, never in a step program: `step-rows-frozen` freezes every byte of a program a landed argv
names (TOOL-dSafePassage-1 S9), so a later edit to the reader there would red it. At `05fd1b7f7` the
registry holds the nine class rows, and an `[[upgrade]]` row already ships in this shape:
`agent-cap/fanout-cap-to-agents-in-flight` in `tools/hooks/kit.toml`, its program under
`tools/govkit/steps/`, which S4's row follows.

### The adopter-rules step

The up reads `.governance/deploy.toml` with `tomllib`. No `[charter]` table or no `adopter_rules` key:
exit 0. Otherwise it writes the before-image of both files (TOOL-dSafePassage-1's helpers in
`tools/govkit/upgrade_steps.py`, imported by its own file's path), then, per `- ` line in order, one
overlay row:

```toml
[[unit]]
tag = "repo.rule-<NN>-<seg>"   # NN: the line's ordinal in the key; seg: the line's text folded; both below
level = 0
type = "directive"
scope = ["reader.every"]       # the block renders only what the every-reader selector keeps
text = "<the line, its leading '- ' cut>"
```

in S10's row grammar, validated by unit 32's overlay reader before it is written, and it then takes the
`adopter_rules` key out of `deploy.toml` by a line edit that leaves every other byte in place. A line
over the one-line cap or failing the reader refuses with exit 1 and writes nothing.

The tag's grammar. `<NN>` is the line's 1-based ordinal among the key's lines, zero-padded to two
digits; a key holding 100 lines or more pads every ordinal to its line count's digit count. One up (DERIVED from the tag grammar)
converts the whole key, so every tag one run writes has one width, and the tags' byte order is the
rules' order, which is the order `tools/playbook/overlay.py#derive_overlay_text` places them in.
`<seg>` is the rule's text folded by `tools/playbook/tag_index.py#derive_heading_seg`, cut at 40
bytes, its trailing `-` trimmed; a rule whose fold is empty takes the tag `repo.rule-<NN>`. The
longest tag is 51 bytes plus the ordinal's width, under `tools/playbook/tag_index.py#TAG_MAX_BYTES` (DERIVED from the tag grammar)
(64) for any width up to 13 digits. The ordinal makes each tag unique within the key, so no
collision suffix is minted. A tag the overlay already holds is the writer's own refusal, exit 2, and
the step has then changed neither file. Gov's own key holds nine rules, so its tags run
`repo.rule-01-` to `repo.rule-09-`, the longest 53 bytes and each matching the tag grammar (PINNED,
derived at bb432ee2f by folding gov's key under this grammar).

The up refuses, exit 1 and nothing written, on two more inputs whose conversion would change the
block. The first is a key line that is not a `- ` line, since the block renders a unit only as
`- <text>`. The second is an overlay already holding a level-0 unit whose tag sorts below the last
converted tag: the block rendered that unit after the key's lines, and the writer would place it
among or ahead of them. Gov's own key holds only `- ` lines, and gov holds no overlay at
bb432ee2f (PINNED, read then).

The down restores both files from the before-image under its refusal rule: a file whose bytes are
neither the image's before nor its after is named and left.

**Who writes.** The step writes the overlay and `deploy.toml` as `update` runs it, which is the write
the clause names ("by a step whose down restores it"), not an agent's edit through unit 15's command.
The minimal guard refuses agent writes to both files (`cl-dClosedLoop-0012`, TOOL-dGroundRules-6
S1); a step run by `update` in the lander's prepared merge is not one, and the lander never fires
pre-commit (TOOL-dGroundRules-6, `:105-107`), so the step's write meets no guard and owes no
admission ask.

### The inventory queries

Run at the pass, before the first edit and after the last:

```bash
git grep -n -F -e "agent-instructions" -e "adopt-agent-instructions" -e "CODEX_MAX" -- . \
  ':!memory/builds' ':!memory/ledger' ':!memory/map/generated' ':!tools/agent-instructions/'
git grep -n -F -e "playbook_path" -e "coding-governance-agents.template.md" -e "reseed-available" -- . \
  ':!memory/builds' ':!memory/ledger' ':!memory/map/generated'
```

The first is the agent-instructions kit's population, by path and by value; at `ce13efbe` it returns
the files S1's Readers line lists, `README.md:17` among them. The second is the seed's; its hits that
read the gov-root template unit 20 keeps are kept, and the ones that read a seeded copy are re-pointed
or re-worded. The generated map is re-rendered by `python tools/codebase-map/gen_map.py --write`, never
edited. Both counts are DERIVED by the query at the pass. Run at `05fd1b7f7`, the first returns 31
files, the second 41 (PINNED, counted then): the first's further hits are the ones S1 names with
what each owes, and the second's most numerous are the gov-root template's name in kit code, checks
and guides, kept; its `playbook_path` hits are the ones S5's Readers line lists. Run at c0800e284,
the first returns 37 files and the second 46 (PINNED, counted then); the first's new hits name
CODEX_MAX, whose name the move keeps, and S1's Readers line lists them.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| the `[[retired]]` ids `agent-instructions` and `playbook/seeded-template` | `tools/govkit/registry.toml` | none |
| the step id `playbook/adopter-rules-to-overlay` | `tools/govkit/entries/playbook.kit.toml` | none |
| `tools/govkit/steps/adopter_rules_to_overlay.py` (step program) | govkit kit | the lexicon's naming predicates |
| `read_module_export_members`, `write_module_export_plant` | `tools/codebase-map/map_lib.py` | the lexicon's naming predicates |
| the class id `module-export` | `tools/govkit/surface-classes.toml` | none |
| `derive_render_plant`, the render plant's factory (S1) | `tools/policy/check_policy.py` | the lexicon's naming predicates |

### Files touched (estimate)

- `tools/govkit/registry.toml`
- `tools/govkit/entries/playbook.kit.toml`
- `tools/govkit/surface-classes.toml`
- `tools/govkit/usage.toml` (the `module-export` class's `[[class]]` row)
- `tools/govkit/steps/adopter_rules_to_overlay.py` (new)
- `tools/codebase-map/map_lib.py` (the `module-export` class's reader and plant)
- `tools/policy/caps.toml`, `tools/policy/check_policy.py` (the `codex-instructions` row and its case)
- `tools/playbook/render_playbook.py` (CODEX_MAX's new home)
- `tools/govkit/entries/check-microformats.kit.toml` (the micro-format leg's subject and `requires`)
- `tools/govkit/selftest.py`, `tools/check-placeholders.sh`, `memory/map/features/lexicon.md` (the
  hole's arms, the `[charter]` arm's key, and the hole's name re-worded where it is named)
- `tools/gate-legs.json`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/run-gates/selftest-budgets.txt`
- `tools/agent-instructions/` (leaves the tree)
- `memory/project/docs-undocumented.txt`, `memory/project/positional-refs.txt` (the orphan row, and the stale row `shrink` drops)
- `memory/project/spawn-idiom-sites.txt`, `memory/project/testsuite-count-waivers.txt`, `memory/project/unarmed-branches.txt` (the owed-rows probe's rows)
- `tools/playbook/core-pending.txt` (each departing leg's row)
- `tools/playbook/instruction_units.py` (the `no-renderer` plant and its `PLANTS` row)
- `tools/playbook/README.md`, `help/size-caps.md` (re-worded where they say the adopter wires or announces)
- `.governance/deploy.toml` and `.governance/instructions.toml` (gov first, written by the step)
- `README.md`, `WIRE-INTO-PROJECT.md`, `.claude/rules/product.md`, `.lexicon.conf`, `.memory-tree.conf`
- `coding-governance-agents.template.md` (source; `AGENTS.md` is its render)
- `memory/map/baseline.toml`, `memory/map/features/roles.md`
- `help/upgrade-steps.md`

### Alternatives rejected

- **A `[[shim]]` row of kind `module` for `map_lib`** (TOOL-dSafePassage-6 S1): its forwarder replaces
  the file at `from`, and `map_lib.py` stays with every other name it defines (§8 F2).
- **Deleting an adopter's seeded template**: refused by the clause ("never deleted") and by the owner's
  FK-1-4 with FK-3-1, which dropped `delete` from `install.retired-edits`.
- **One step per adopter rule**: the rules are one key, read and written together, and one before-image
  restores them together.

## 5. Production-readiness checklist

- security: the step writes only the two `.governance/` files of the target it runs on, under the walk's
  containment, and validates every row through unit 32's reader before writing; nothing it writes runs.
- perf / scale: one TOML read and two file writes per adopter; the queries are two `git grep` runs.
- error / empty / loading states: no `adopter_rules` key, the step is a no-op with exit 0; a line the
  reader refuses fails the up with nothing written, as do a key line that is not a `- ` line and an
  overlay level-0 unit whose tag sorts below the converted rules'; a down over a later edit names the
  file and leaves it.
- observability: the walk prints each step's id and outcome; the step gate prints each member and the
  row that witnesses it.
- risks: an adopter whose `CLAUDE.md` holds more than the import line keeps it, and the render's
  `--check` names it (unit 34, S4); the `playbook/seeded-template` id is a step-shaped id no step
  declares, on which the parent's grammar states no rule (§8 F1); and a registered class whose
  population is empty exits 2 (TOOL-dSafePassage-10 S5), so the commit that takes away the last
  `map_lib` re-export also removes the `module-export` row and its `usage.toml` row. Two open
  questions bound the build: the conversion step has no member for the step gate to see (section 8, F8), and
  an adopter's seeded copy is graded as a seed row gov still ships, since gov keeps the template's
  source (section 8, F9).
- testing: AC1 to AC15, each observing the step gate, the step program, the renderer, the census or a
  descriptor directly on a scratch clone or the tree.
- migration: this unit is the migration; §4.
- user docs: `help/upgrade-steps.md` (S8).

## 6. Acceptance criteria

- **AC1** — When `python step_gate.py --base ce13efbe` runs on a scratch clone of the
  pass's tip with the `agent-instructions` `[[retired]]` row taken out, it exits 1 naming
  `entry:agent-instructions`; with the row back it exits 0 for that member.
  Red when: the kit leaves with no succession row and the gate stays green.
  fixture: a clone under `%TEMP%`; dSafePassage's step gate landed.
- **AC2** — When the first query of §4 "### The inventory queries" runs after the pass, every hit is a
  kept hit the pass commit's `Decided:` trailer names, and `README.md`'s kit line names the renderer.
  Red when: a reader still names `tools/agent-instructions/` as where the wiring lives.
  figure: the count is DERIVED by the query at the pass.
- **AC3** — When `python tools/govkit/govkit.py check --target <scratch adopter>` runs on a scratch
  adopter installed at `ce13efbe` with `agent-instructions` claimed, it prints
  `agent-instructions: retired, successor playbook-render` and counts no problem for it, the line
  TOOL-dSafePassage-1's AC9 states; and `python tools/govkit/govkit.py update --target <scratch adopter>`
  carries the claim to `playbook-render` and its `CLAUDE.md` import line is unchanged.
  Red when: the update refuses the whole run on the retired kit, or rewrites a working import.
- **AC4** — When `python step_gate.py --fixture --plant module-export` runs, it exits 1
  naming the re-exported name the plant took away; with `--with-row` it exits 0.
  Red when: a re-exported name leaves `map_lib` with no row naming it.
- **AC5** — When `python adopter_rules_to_overlay.py up <scratch>` runs on a target
  whose `deploy.toml` holds three rules, the overlay holds three level-0 `repo.` units with the rules'
  text, the key is gone, and `witness` exits 0; `down` restores both files byte-identical, and `up`
  again reproduces the first result byte for byte.
  Red when: the down leaves a byte different, or a rule is lost or doubled.
- **AC6** — When the same program's `up` runs on a target with no `adopter_rules` key, it exits 0 and
  writes nothing; on a target whose rule exceeds the one-line cap it exits 1 and writes nothing, and
  so it does on a target whose key holds a line that is not a `- ` line, and on one whose overlay
  already holds a level-0 unit tagged `repo.a`.
  Red when: a refused rule leaves a half-written overlay, or the up converts a key whose lines or
  order the block would not render as they were.
- **AC7** — When `python tools/playbook/render_playbook.py --target <scratch>` has written the charter
  of a scratch clone of the pass's tip whose `deploy.toml` holds three rules, written so their texts
  sort in the reverse of their order (`- Zeta`, `- Mid`, `- Alpha`), and the step's `up` has
  run there and been committed, `python tools/playbook/render_playbook.py --target <scratch> --check`
  exits 0, the project block holding the same lines in the same order, each overlay row the up wrote
  holding `scope = ["reader.every"]` and a tag from `repo.rule-01-` to `repo.rule-03-`; and
  `python tools/govkit/upgrade_steps.py list` prints the step's row.
  Red when: the up loses, doubles or reorders a rule in the rendered charter, or the render refuses
  a token or a `[charter]` key once the step has run.
  fixture: two plants on the same clone, each committed, under which the same `--check` exits 1:
  the scope plant takes `scope` out of the three rows, so the block drops them; the reorder plant
  writes the three rows into an empty overlay through the overlay writer with tags folded from their
  text alone (`repo.zeta`, `repo.mid`, `repo.alpha`), so the writer places them `Alpha`, `Mid`, `Zeta`.
- **AC8** — When `python step_gate.py --base ce13efbe` runs on a scratch clone with the
  `playbook/seeded-template` row taken out, it exits 1 naming each seed member; with it, 0.
  Red when: the seed rule leaves with no succession row and the gate stays green.
- **AC9** — When `python tools/govkit/govkit.py update --target <scratch adopter>` runs on an adopter
  installed at `ce13efbe` whose seeded template it edited, the row reads `retired-edited`, one order is
  written and the file's bytes are unchanged; on one it never edited, the row reads `withdrawn`.
  These are TOOL-dSafePassage-9's verdicts for a retired seed row at its 2026-10-25 revision (§8 F7).
  Red when: an edited seeded copy is deleted or graded `patched` with no order.
  fixture: at c0800e284 this criterion is red as written, since gov still holds a blob at the seed
  row's source; it waits on section 8's F9.
- **AC10** — When `python tools/playbook/practice_census.py` runs at the pass's tip, its summary line
  reads `moves 0 · moves, row kept 0`, so S6 owes no change record.
  Red when: the census moves a row out of the shipped set and the pass writes no change record, a
  hand-back while the step gate registers no `unit` class.
  figure: the zero counts are PINNED at c0800e284 and re-derived by the census at the pass.
- **AC11** — When `python upgrade_steps.py list` and gov's source-mode receipt are read
  after the lander's prepared merge, the receipt's `steps` holds `playbook/adopter-rules-to-overlay`
  and its witness exits 0 on gov's tree.
  Red when: an adopter meets a step gov never ran on itself.
- **AC12** — When `git grep -n -e "adopter-rules-to-overlay" -- upgrade-steps.md` runs, it finds
  the section.
  Red when: the steps ship with no page under `help/`.
- **AC13** — When `python -c "import tomllib; print([(r['enforcer'], r['home']) for r in tomllib.load(open( 'tools/policy/caps.toml' , 'rb'))['cap'] if r['name'] == 'codex-instructions'])"`
  runs after the pass, it prints the module `CODEX_MAX` moved into and `constant:<that module>:CODEX_MAX`,
  and `python "tools/policy/check_policy.py"` reports `arm_cap_census` green. The same row's `kit`
  reads `playbook-render` and its `installed` the renderer's path, and
  `python tools/policy/check_policy.py --fixture budgets-cap-codex-instructions` exits 0, the render
  refusing a template past CODEX_MAX with the same line under `warn` and under `refuse`.
  Red when: the row still names `tools/agent-instructions/adopt-agent-instructions.sh`, through its `{prefix}` spelling, which the pass deletes; or the case still runs the adopter.
- **AC14** — When `git grep -n -A1 -e 'class = "module-export"' -- tools/govkit/usage.toml`
  runs after the pass, it prints the row, followed by `usage = "none"`.
  Red when: a class registered in `tools/govkit/surface-classes.toml` has no `[[class]]` row in
  `tools/govkit/usage.toml`, which the docs leg reports as a finding.
- **AC15** — When `python -c "import tomllib; d = tomllib.load(open('tools/govkit/entries/playbook.kit.toml', 'rb')); m = tomllib.load(open('tools/govkit/entries/check-microformats.kit.toml', 'rb')); print(d['version_from'], d.get('files'), d.get('hole'), m['requires'], [g['argv'] for g in m['gate_leg']])"`
  runs after the pass, it prints a `version_from` holding `none`, no `files` and no `hole` for the
  `playbook` entry, and `['playbook-render']` with the micro-format leg's subject the template beside
  the engine.
  Red when: `version_from` still names a file the entry no longer lands, which the selfcheck's
  version-constant arm refuses, or the micro-format leg still grades `{playbook_path}`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `recall floor` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `agent-instructions self-test` · `lexicon naming predicates` · `straggler-guard arms` · `kit/dogfood doc parity` · `transition-audit arms` · `check-wiring self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy fixtures` · `playbook render selftest` · `step-gate` · `step-rows-frozen` · `upgrade-walk` · `docs` · `policy check` · `core meta-check` · `instruction units selftest` · `tags (the resolver's checks)` · `harness arms (fail branches armed or pinned)` · `placeholder-catalogue self-test`

The `step-gate`, `step-rows-frozen`, `upgrade-walk` and `docs` legs dSafePassage lands keep green
over this unit's rows, and dGroundRules' `policy check` and `policy fixtures` legs run `arm_cap_census` and the
census case over the re-pointed row; they are named here in prose because the manifest at `ce13efbe`
holds none of them. At `05fd1b7f7` the manifest holds all six, so the leg line names them, with
`playbook render selftest`, whose guard the playbook kit's files this pass edits trip, and the four
unguarded legs S1's rows feed: the core meta-check over the pending list, the instruction-unit
fixtures holding the `no-renderer` plant, the tag resolver's positional arm over the positional
list, and the arms check over `ARMS_FLOORS` and the unarmed list. The `govkit acceptance matrix` leg
is red there for the renderer's dependency unit 73 parked for the owner (its fork record's F1); this
pass does not repair it. Re-read at c0800e284, `placeholder-catalogue self-test` joins the line,
its guard tripped by `tools/check-placeholders.sh`, whose comment names the hole; `govkit selfcheck`
grades the `playbook` entry's `version_from`, and `govkit selftest` runs the hole's arms and the
`[charter]` arm S5 moves.

New arm: tools/govkit/surface-classes.toml · covers AC4 · the step gate's own fixture runs the new class row's plant with and without `--with-row` · none
New arm: tools/govkit/selftest.py · covers none · the `[charter]` arm of `check_playbook_hole_modes` answers `kickoff-manifest`'s `manifest_path`, a token a selected kit's argv or destination names · none
New arm: tools/policy/check_policy.py · covers AC13 · the `budgets-cap-codex-instructions` case renders a template past CODEX_MAX through the renderer under `warn` and under `refuse` · none

## 8. Open questions

- **FACT-QUESTION · F1 — Whether a `[[retired]]` row can name the seeded template.** Scout C's
  interface 10: a `[[retired]]` row's `id` is an entry id or a step id, and the seed is a file inside
  the `playbook` entry. Probe: TOOL-dSafePassage-1 §4 "### Data model", read at `ce13efbe` and again
  at its rev-9 (`:201-204`), which still states no rule either way. Observation:
  the grammar refuses a retired id that is still a live entry or declared step and a successor that is
  not live, and states no rule that a retired step id was once declared; `surfaces` takes any
  `<class>:<name>`. Liveness: the same reader refuses `id = "playbook"`, a live entry, so the probe can
  read a refusal.
  RESOLVED (agent, 2026-10-23, delegated): a `[[retired]]` row with the step-shaped id `playbook/seeded-template`, `successor = "none"` and the seed's members in `surfaces`, rung 2; the build run re-grounds against the landed reader, and if it refuses the id, the row becomes an `[[upgrade]]` row whose `surfaces` names the same members, recorded as a deviation. widens: none · relaxes: none
- **FACT-QUESTION · F2 — Whether the `map_lib` deprecation fits a `[[shim]]` row.** Probe:
  TOOL-dSafePassage-6 S1 and S3, read at `ce13efbe`. Observation: a `module` row's forwarder is written
  at its `from` path and "stands in for itself in `sys.modules`", so a row whose `from` is
  `codebase-map/map_lib.py` would replace a module that keeps every name it does not re-export.
  Liveness: a row whose `from` is a moved whole module would fit, so the probe can read a fit.
  RESOLVED (agent, 2026-10-23, delegated): no fit; the deprecation is declared by S3's `module-export`
  class row, the parent's own extension point ("a later build's class joins by adding its own row"),
  rung 2. widens: none · relaxes: none
- **F3 — How the step gate sees the adopter rules leave.** None of the parent's nine classes reads a
  playbook placeholder or a `[charter]` key. Options: (a) a `charter-key` class row; (b) no class, so
  the clause's "seen red at the step gate" has no member; (c) folding the key into the `conf` class.
  (b) fails the clause, and (c) changes the parent's class reader. RESOLVED (agent, 2026-10-23,
  delegated): (a), rung 3, through the parent's extension point. widens: none · relaxes: none
  Its premise, that the key and its row leave, does not hold at c0800e284: PLAY-dOrderedCharter-34's
  project block keeps both, so no class row is written and F8 carries the question.
- **F4 — Who writes gov's overlay and `deploy.toml` when the step runs on gov.** The minimal guard
  refuses agent writes to both until dDeclaredLoop, and unit 15's command refuses every write until
  then. Options: (a) the step, run by `update` in the lander's prepared merge (`cl-dClosedLoop-0025`);
  (b) unit 15's command; (c) the owner by hand. (b) refuses by its own clause, and (c) is no step.
  RESOLVED (agent, 2026-10-23, delegated): (a), rung 1, the clause naming the step as the converter;
  the lander never fires pre-commit (TOOL-dGroundRules-6, `:105-107`), so the step's write meets no
  guard and owes no ask. widens: none · relaxes: none
- **F5 — The agent-instructions kit's successor.** Options: (a) `playbook-render`, the renderer that
  absorbed the wiring; (b) `none`, the files withdrawn; (c) `playbook`. (b) leaves an adopter's alias
  files with no owner, and (c) is the seed entry whose template this build stops reading. RESOLVED
  (agent, 2026-10-23, delegated): (a), rung 1, v2's "agent-instructions' wiring moved to the one
  renderer". widens: none · relaxes: none
- **F6 — What counts the `map_lib` re-export's window.** S3's `module-export` row reds a re-exported
  name's leaving at the step gate, but TOOL-dSafePassage-6 counts `install.deprecation-window` per
  `[[shim]]` row only (its S5, `:63-68`), its §3 named this re-export a first shim row (`:89-91`), and
  F2 found no shim kind that fits. Options: (a) the `module-export` class row stays, and
  dConvergedCharter, which takes a re-export away (§3), counts the window from that row's landing
  commit on the default branch, with an ask to dSafePassage to drop its unit 6's mention of this
  re-export as a first shim row (`:89-91`); (b) an ask to dSafePassage for a shim kind that forwards
  named re-exports, counted per row. (b) adds a forwarder kind to the parent for one partial module
  whose other names stay (F2), and (a) reuses the population the class row already declares, its
  landing commit derived from history as the parent derives a shim row's. Recommendation (a).
  RESOLVED (owner, 2026-10-25): (a). No ask is filed: TOOL-dSafePassage-6's 2026-10-25 revision
  (`2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md`, Item 4) drops its §3 naming of this re-export as a first shim row.
- **F7 — What an edited seeded copy reads once gov stops shipping the seed.** S5 and AC9 expect
  `retired-edited` with one order. TOOL-dSafePassage-9 sends the grid cell (`differs`, `absent`) to
  `retired-edited`, and its arm takes "both a first-time engine row and a row already carrying the
  role" (`:127-128`), naming no seed row, and at `cbf44887` the seed override
  (`tools/govkit/govkit.py:9988-10000`) grades an edited copy `patched` with no order, AC9's red, and
  an unedited one `current`. Options: (a) an ask to dSafePassage
  to route a retired seed row through its unit 9's `retired-edited` arm, so the edited copy reads
  `retired-edited` and the unedited one `withdrawn`; (b) this unit extends that arm itself; (c) AC9
  states the verdict the parent gives. (b) gives the parent's arm a second owner, and (c) states the
  clause's own red as the expected result. Recommendation (a).
  RESOLVED (owner, 2026-10-25): (a). No ask is filed: TOOL-dSafePassage-9's 2026-10-25 revision
  (`2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md`, Item 5) routes a retired seed row through its `retired-edited` arm, an edited copy reading
  `retired-edited` with one order and an unedited one `withdrawn`.
- **F8 — What the step gate sees when the adopter rules move.** The carried clause asks the
  conversion to be seen red at the step gate without its row. At c0800e284 the conversion takes no
  member of gov's product away: `tools/playbook/render_playbook.py#build_project_block` still renders
  `[charter] adopter_rules`, `tools/playbook/render_playbook.py#read_charter_table` still admits the
  key while the `ADOPTER_RULES` row declares it, and that row must stay, since the template carries
  its token and the block takes its default from it (S4). Options: (a) the step's `surfaces` is `[]`
  and the key stays a live input, so the clause's red half has no member for this conversion; (b) a
  class over the `[charter]` keys gov's own `.governance/deploy.toml` answers, whose member leaves
  when gov's own step runs; (c) a new unit on top of PLAY-dOrderedCharter-34 takes the key out of the
  render's inputs, and its own row witnesses that member. (b) reads the file the step it would
  witness writes, a guard sharing state with what it guards, which the charter's `[class]` practice
  refuses, and its member is gov's own answer, which no adopter receives; the first veto discards it.
  (c) takes away an input every adopter's render reads today, a public surface change, and adds a
  unit to the build; the second veto makes it an owner turn. (a) is what this unit builds under any
  pick, the step's row frozen once it lands, but it leaves a half of the carried clause with no
  observation, and narrowing a carried clause is the owner's (the build method's bound on delegated
  scope). Recommendation (a): the key renders the same rules it always did, so retiring it buys a red
  and nothing an adopter can use; the owner states the clause's red half as owed only by a
  conversion that takes a member away. OPEN for the owner: every survivor trips the second veto or the
  delegation's bound.
- **FACT-QUESTION · F9 — What an adopter's seeded copy reads once the seed rule leaves.** S5 and AC9
  expect `retired-edited` with one order for an edited copy and `withdrawn` for an unedited one,
  from F7's pick. Probe, read at c0800e284: `tools/govkit/govkit.py#classify_row` gives `absent` on
  gov's side only where gov holds no blob at the row's `source`, and the seed override in
  `tools/govkit/govkit.py#_cmd_update` passes `retired-edited` and `withdrawn` through only then
  (`SEED_KEPT_VERDICTS`), the rule TOOL-dSafePassage-9 states ("a `seed` row whose source gov no
  longer ships"). The seed row's `source` is the root `coding-governance-agents.template.md`, which
  gov keeps and the renderer kit lands beside its engine (`tools/playbook/kit.toml`, the
  PLAY-dOrderedCharter-34 S5 rule), and with no rule claiming the row's destination the role
  re-resolution leaves it `seed`. Observation: an unedited copy reads `current`, an edited one
  `patched`, either `reseed-available` once the template moves, and no order is written, AC9's red.
  Liveness: TOOL-dSafePassage-9's own fixture, `tools/govkit/fixtures/retired_edits.py`, removes the
  seed's source and reads `retired-edited`, so the probe can read the verdict AC9 wants. Options:
  (a) an ask to dSafePassage to read a seed row whose kit's rules no longer land its destination as
  retired; (b) this unit makes that one change in `tools/govkit/govkit.py#_cmd_update`, where the
  role re-resolution finds no rule for the row; (c) AC9 states the verdicts HEAD gives. (c) leaves
  an edited copy with no order, the clause's red, so the first veto discards it. (a) waits on an
  unbuilt change in another build, a new external dependency, and (b) is the option F7 discarded and
  the owner did not pick, so each is an owner turn. Recommendation (b): one predicate at the one site
  the update already re-resolves a row's role, and F7's premise, that the seed's source leaves gov,
  stopped holding when PLAY-dOrderedCharter-34 shipped the template from the same root path. OPEN
  for the owner; AC9 waits on it, and every other criterion builds without it.
- **F10 — The agent-instructions entry leaves while gov's own deploy still selects it.** Found by the
  third hand-back (`memory/builds/dOrderedCharter/RUN.md`, the `decision` line of
  2026-11-09T18:39:19Z) and read at f988ae3a1. S1 takes the kit's `[[entry]]` out of
  `tools/govkit/registry.toml`, and gov's `.governance/deploy.toml` names `agent-instructions` in
  its `kits`. `tools/govkit/govkit.py#resolve_selection` refuses a target's `kits` naming an id that
  is not a registry entry and reads no `[[retired]]` row. Gov's own selection reaches it through
  `tools/govkit/govkit.py#read_plan_destinations`, which `tools/govkit/govkit.py#_cmd_update`'s
  source mode calls before it walks a step and `tools/govkit/step_gate.py#read_file_members` calls
  for the `file` class, so `update` on gov and AC1's step gate both refuse at the pass's tip. Only
  `tools/govkit/govkit.py#cmd_check` routes an id that left through
  `tools/govkit/upgrade_steps.py#resolve_claim`, and it reads the receipt's claims, not `kits`.
  `.governance/deploy.toml` is a line of `tools/policy/guarded-paths.txt`, so
  `tools/policy/guard.py` refuses an agent commit that changes it. F4 does not answer this: it rules
  that `update` in the lander's prepared merge writes gov's `deploy.toml` when the adopter-rules step
  runs, but that step edits only the `[charter]` key, never `kits`, and the refusal comes before the
  walk. The same refusal meets any adopter whose `kits` names the id at `plan`, `apply` and `adopt`
  (DERIVED from `tools/govkit/govkit.py#resolve_selection`), as the release-0 fixture's `kits` does
  (`tools/govkit/fixtures/release-0/deploy.toml`). Options: (a) the owner drops `agent-instructions`
  from gov's deploy kits before or with the pass; (b) the selection resolver reads a retired id
  through its `[[retired]]` row, a new mechanism; (c) the entry leaves only at the landing. (a)
  answers gov alone and leaves an adopter that selects the id refused. (b) widens the scope of this
  unit into the resolver, and it is the one option that answers every target the class holds,
  reusing the claim resolver `cmd_check` already calls. (c) leaves S1 unbuilt at the pass's tip,
  where AC1 observes it. Recommendation (b). OPEN for the owner: (a) is an owner edit to a guarded
  file, and (b) and (c) change the unit's scope.
- **F11 — `check-microformats` requires `playbook-render`, which the default selection lacks.** Found
  by the same hand-back and read at f988ae3a1. At HEAD
  `tools/govkit/entries/check-microformats.kit.toml` declares `requires = ["playbook"]`, and S5 moves
  it to `playbook-render`, the entry that lands the template the leg then grades. The registry's
  `[selection] default` (`tools/govkit/registry.toml`) holds `check-microformats` and `playbook` and
  not `playbook-render`, and `tools/govkit/govkit.py#_cmd_apply` refuses a selection with a
  requirement neither selected nor claimed (`tools/govkit/govkit.py#derive_unsatisfied_requires`),
  never widening it, so every default install refuses once S5 lands. Options: (a) add
  `playbook-render` to the default selection; (b) drop `check-microformats` from it; (c) change the
  leg's subject. Each changes what every adopter installs by default. (b) ships the default charter
  with its micro-format grammar unchecked. (c) needs a subject a default install holds without
  `playbook-render`, and S5 takes away the seeded copy at `{playbook_path}`, the only charter file
  the `playbook` entry lands. Recommendation (a): the default install keeps its gate and gains the
  kit that lands what the gate grades. OPEN for the owner. The builder's finished step program and
  its partial patch are kept outside the tree, in the run's scratch u31 folder (the same RUN.md
  line), for the pass that resumes once F10 and F11 are answered.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-39, PLAY-dOrderedCharter-46, PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-50, PLAY-dOrderedCharter-55.
- rev-4 · 2026-10-24 · S1 S3 S4 S5 S7 · §3 · §4 · §5 · AC3 AC9 AC13 AC14 · §7 · §8 F1 F4 F6 F7 · §10 ·
  re-grounded on the parents' landed specs by `2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck.md`,
  rows 3, 6, 10, 12 and 16 and U1, U2, U7 and U9: S1's readers drop `tools/template-size-limits.txt`,
  which leaves gov in TOOL-dSafePassage-1's commit, and re-point the `codex-instructions` census row
  with `CODEX_MAX`; the `charter-key` reader and plant move to `step_gate.py`; AC3 reads succession
  through `check`; the leg is `upgrade-walk`; F4 owes no admission ask; F6 and F7 open for the owner.
  On the coordinator's follow-up, S3, S4, §4 and AC14 add each class's `tools/govkit/usage.toml`
  `[[class]]` row (TOOL-dSafePassage-13 S1, S8), and the consumes-from edge to
  `PLAY-dOrderedCharter-30` and S7's sentence on its comment leave, that comment being the owner's.
- rev-5 · 2026-10-25 · S3 S5 · §3 · AC9 · §8 F6 F7 · the owner picks (a) on F6 and F7, from
  `2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md` Items 3 and 4: dConvergedCharter counts the
  re-export's window from the `module-export` row's landing commit, and AC9 expects
  TOOL-dSafePassage-9's retired-seed verdicts, with a consumes-from edge on that revision; no ask is
  filed, since dSafePassage's units 6 and 9 are revised in the same commit.
- rev-6 · 2026-11-03 · §7 · from `2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md` Item 2: the leg line names `policy fixtures`, whose guard a §4 Files touched path trips, the guards hit the spec-token check reads with DEFERRED as live.
- rev-7 · 2026-11-04 · AC13 · from `2026-11-04-prompt-PLAY-dOrderedCharter-20-3-sweep-fix-brief.md` item 4: AC13 names the adopter by its full tracked path.
- rev-8 · 2026-11-08 · S1 S3 S5 · section 4 The rows, The inventory queries, Inventory, Files
  touched · section 7 · section 10 · from
  `2026-11-08-prompt-PLAY-dOrderedCharter-46-drift-fold-brief.md`: re-read at `05fd1b7f7`. S1's
  first query now hits 31 files, and its Readers line gains the fifteen the base did not hold, with
  what each owes: the `policy fixtures` guard's two entries, the docs leg's orphan row, the
  `ARMS_FLOORS` entry and the positional row its edit stales, the pending `leg` rows, the
  `no-renderer` plant that copies the adopter, the owed-rows probe's waiver rows, gov's receipt, and
  the kept history. `tools/check-template-size.sh` leaves Files touched, since unit 6's check reads
  `CODEX_MAX` through the census row. S3 names the four re-exported names. S5's Readers line gains
  the release-0 fixture and the three fixture modules that answer `playbook_path`. The class rows
  spell `{prefix}/`, their reader and plant names follow the step gate's own pairs, and the `none`
  usage rows carry no `rows` key, as the landed rows show. The leg line gains the six dSafePassage
  and dGroundRules legs now in the manifest, `playbook render selftest` and the four unguarded legs
  S1's rows feed; the reuse audit records the landed seams.
- rev-9 · 2026-11-09 · S5 · section 3 · from
  `2026-11-09-prompt-PLAY-dOrderedCharter-34-repair-2-brief.md` Item 1: PLAY-dOrderedCharter-34 now
  ships the template beside the renderer's engine and reads it there, so the consumes-from edge to it
  names that template, which the render reads once S5 takes the seed rule out, and S5's Readers line
  says its F7 moves its fixtures' templates to their tree's renderer-kit directory rather than to
  `gov_root`.
- rev-10 · 2026-11-09 · section 1 · S1 S4 S5 S6 · section 3 · section 4 The rows, The inventory
  queries, Inventory, Files touched · section 5 · AC7 AC9 AC10 AC13 AC14 AC15 · section 7 · section 8
  F8 F9 · section 10 · from `2026-11-09-prompt-PLAY-dOrderedCharter-31-repair-brief.md`, re-read at
  c0800e284: the `ADOPTER_RULES` row stays, the conversion step declares `surfaces = []` and the
  `charter-key` class leaves this spec, AC7 observing the rendered rules unchanged, with F8 open for
  the owner; S6's population is empty, so AC10 observes the census moving nothing and the unit-tag
  red stays PLAY-dOrderedCharter-33's AC7; the codex cap row's `kit` and `installed` move with its
  enforcer to the renderer and its case renders through a `derive_render_plant` factory; the
  `playbook` entry's `version_from` becomes a declared `none`, its hole's selftest arms go with the
  hole, the `[charter]` arm answers `manifest_path`, and the micro-format leg grades the template
  beside the engine (AC15); AC9 waits on F9, gov keeping the seed's source; S1's and S5's Readers
  lines are re-grepped.
- rev-11 · 2026-11-09 · S4 · section 4 The adopter-rules step · section 5 · AC6 AC7 · section 10 ·
  from `2026-11-09-prompt-PLAY-dOrderedCharter-31-repair-2-brief.md`, re-read at bb432ee2f: each
  converted row carries `scope = ["reader.every"]`, since the project block renders only what the
  every-reader selector keeps (Item 1), and its tag is `repo.rule-<NN>-<seg>`, a zero-padded ordinal
  two digits wide, wider only past 99 lines, its seg the `doc` namespace's fold and its collision (DERIVED from the tag grammar)
  suffix dropped, so the overlay writer's level-then-tag placement keeps
  rule order (Item 2, the main loop's ruling); the up also refuses a key line that is not a `- `
  line and an overlay level-0 unit sorting below the converted tags, each of which would change the
  block; AC7 gains the scope and reorder plants, AC6 the two refusals. Item 3's five confirmations
  stand as written, and S4's Readers line gains the selector and the writer; F8 and F9 stay parked.
- rev-12 · 2026-11-09 · section 8 F10 F11 · from
  `2026-11-09-prompt-PLAY-dOrderedCharter-31-park-record-brief.md`, read at f988ae3a1: the third
  hand-back's two blockers, the agent-instructions entry leaving while gov's own deploy selects it
  and `check-microformats` requiring `playbook-render` outside the default selection, are recorded
  as forks OPEN for the owner; no design text moved, and the unit stays DEFERRED.

## 10. Reuse audit

No seam in the tree takes these rows yet: `grep -rn '\[\[upgrade\]\]' tools` returns nothing at
`ce13efbe`, as scout C found (`memory/builds/dOrderedCharter/build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-c.md:14`);
the step kind, the class registry, `retired-edited` and the step gate are dSafePassage's specs,
deferred to its build run, and this unit writes rows in their grammar. The built seams it reads, each
verified at source: `[charter] adopter_rules` (`.governance/deploy.toml:59-70`) and `read_charter_table`
(`tools/playbook/render_playbook.py:809`); the `ADOPTER_RULES` placeholder
(`tools/govkit/entries/playbook.kit.toml:273-277`); the seed rule (`:23-26`) and its
`reseed-available` grade (`tools/govkit/govkit.py:9989-9990`); the kit's registry entry
(`tools/govkit/registry.toml:106-107`) and `CODEX_MAX` (`tools/agent-instructions/adopt-agent-instructions.sh:31`).
`reuse_lookup.py "retire a shipped file with a successor at update"` ranked name-token hits only
(`corpus_files`, `parse_file`, `hash_file`); none carries a file to a successor. The reader-inventory
query follows unit 18's stated-query form (its §4 "### The inventory query"), never a typed list. Where
a record and the source disagree: the scout cites the seed row at `entries/playbook.kit.toml:23-26`, which
matches, and `README.md:17` as the kit's by-value reader, which spells its path and is a by-path hit
too. The recall probe found the clause, TOOL-dSafePassage-1 and -5, and TOOL-dGroundRules-13
(`memory/builds/dGroundRules/BACKLOG.md:6`), the guard-admission ask a step run on gov's own tree was
thought to need; F4 no longer follows it, since the lander never fires pre-commit
(TOOL-dGroundRules-6, `:105-107`). The class readers' seam is the parent's own: its nine readers and
plants sit in `tools/govkit/step_gate.py` (TOOL-dSafePassage-10, `:99-100`), the shape the `module-export`
pair follows; the census row re-pointed is TOOL-dGroundRules-9's (`:175`). Re-read at `05fd1b7f7`, the
parents have landed: the step kind and its before-image helpers in `tools/govkit/upgrade_steps.py`,
the gate and its readers in `tools/govkit/step_gate.py`, the class registry
`tools/govkit/surface-classes.toml`, and the census row in `tools/policy/caps.toml`. The same grep
for `[[upgrade]]` finds one row, `tools/hooks/kit.toml`'s, whose program sits in
`tools/govkit/steps/`, the precedent S4's row follows. The seams cited by line have moved:
`tools/playbook/render_playbook.py#read_charter_table`, `tools/govkit/govkit.py#_cmd_update` for the
`reseed-available` grade, and the `ADOPTER_RULES` placeholder a line lower in its descriptor.
Re-read at c0800e284 for rev-10, each seam the revision adds is extended, never copied: the codex
case's render plant extracts `tools/policy/check_policy.py#derive_one_line_rule_plant`'s scaffold
into one factory at its second instance; the `playbook` entry's `version_from` takes the declared
`none` form fifteen tracked files already spell; the `[charter]` arm reads its key from
`tools/govkit/govkit.py#needed_answers`; the micro-format leg grades the template the renderer kit
already lands; and the conversion step's `surfaces = []` is the step grammar's own declared absence
(`tools/govkit/upgrade_steps.py#check_surfaces`), so no class is minted for it.
Re-read at bb432ee2f for rev-11, the converted tag's fold is the `doc` namespace's own,
`tools/playbook/tag_index.py#derive_heading_seg`, which `tools/playbook/writing_practice.py` already
calls, so no second fold is written; the rows go in through
`tools/playbook/overlay.py#write_overlay_units`, unit 32's one writer, whose level-then-tag placement
the ordinal segment meets rather than a writer of the step's own.

Recall terms used: `python tools/memory-recall/query.py "how does gov ship its own upgrade step that retires the seeded charter template" --terms "upgrade step retired row seeded template adopter_rules overlay down restores successor change record"`
