# KICK-dKeptSession-4 — the preset asked once at govkit intake and written into the scaffolded policy file

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 5 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0142@816ff525 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-16 KICK-dKeptSession-19 KICK-dKeptSession-20 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

A repository's posture is one choice, its `preset`, and v2 makes choosing it a policy change,
"guarded and recorded like any other" (v2:1412). Today the policy kit's scaffold writes only
dGroundRules' literal defaults, so a new adopter starts with no preset named and nobody was asked.
This unit puts the policy at govkit intake: the deployer asks for the preset once, records the
answer in the target's `deploy.toml`, and the scaffold writes it as the policy file's top-level
`preset`, through the answer route intake already derives from a kit's argv.

## 2. Scope (IN)

- **S1** — The token (shared interface I6). The policy kit's `[adopt] argv` in
  `tools/policy/kit.toml` becomes `["bash", "{kit}/adopt-policy.sh", "--scaffold", "--preset",
  "{preset}"]`, so `needed_answers` (`tools/govkit/govkit.py:13089`) derives `preset` as an answer the
  selection needs and `cmd_intake` records it under `[answers]` as `preset`, never under deploy.toml's
  `[policy]` table, which the deployer owns (`govkit.py:13223-13229`). The `[[regenerate]]` argv is
  unchanged: it re-runs `--scaffold` over a kept file, which the answer never rewrites. Observed by
  AC1 and AC2.
- **S2** — The scaffold. `adopt-policy.sh --scaffold --preset <name>` passes the name to `python
  policy.py scaffold --preset <name>`, and `render_scaffold(rows, preset)` writes `preset = "<name>"`
  as the file's first key, above dGroundRules' tables. A name that is not a shipped preset of
  KICK-dKeptSession-1's store is refused, exit 2, naming the name and the four shipped ones, and no
  file is written. Observed by AC3 and AC4.
- **S3** — A kept file. Where `.governance/policy.toml` exists, the scaffold keeps it as it does today
  and, when the file's `preset` differs from the answer, prints one line naming both, never writing:
  the file is the repository's own and changing it is a guarded policy change. Observed by AC5.
- **S4** — Fixture answers. Every answer set a gov fixture installs the policy kit with gains
  `preset = "standard"`: `DEPLOY_FULL`'s `[answers]` in `tools/govkit/selftest.py`, which the policy
  kit's `adopter-fresh-target` case reads through `read_deploy_answers`. Observed by AC6.
- **S5** — The page `help/policy.md` says intake asks for the preset, names the four shipped values,
  and gives the upgrade step for a target whose `deploy.toml` predates the answer. Observed by AC7.

## 3. Non-goals (OUT)

- A default answer: intake asks, and refuses with none, as for every other answer (§8 F1).
- A repository-declared preset at intake: one is declared in the policy file a repository already
  has, after intake (KICK-dKeptSession-1 S3).
- Switching a preset after install: a policy change through the policy guard, not the deployer.
- Any change to `needed_answers`, `cmd_intake` or `resolve_tokens`: the token is the whole hook.

### Edges

- **consumes-from** `KICK-dKeptSession-1` — `presets.toml`, whose shipped table names are the answers the scaffold admits
- **consumes-from** external — govkit's `needed_answers`, `cmd_intake` and `resolve_tokens` (`tools/govkit/govkit.py:13089,13122,1233`); dGroundRules' `render_scaffold`, `adopt-policy.sh --scaffold` and the `adopter-fresh-target` case (TOOL-dGroundRules-1, -16, -21 S1)
- **hands-off** `KICK-dKeptSession-32` — `render_scaffold`'s preset argument, whose written rows that unit narrows to the keys the preset leaves unassigned (id 1)
- **hands-off** `KICK-dKeptSession-44` — `adopt-policy.sh --scaffold`'s refusal path, which the batch's S13 passes through (id 20)

## 4. Design

### The route

```
kit.toml [adopt] argv  ... "--preset", "{preset}"
  -> needed_answers: {preset}                          (derived, never listed)
  -> govkit intake --answer preset=strict
  -> deploy.toml  [answers]  preset = "strict"
  -> apply: adopt-policy.sh --scaffold --preset strict
  -> policy.py scaffold --preset strict
  -> .governance/policy.toml:  preset = "strict"   then dGroundRules' tables
```

The scaffold's bytes stay the blob git stores (TOOL-dGroundRules-21 S1): the line is written LF-only
through the same `sys.stdout.buffer` path, before `SCAFFOLD_HEADER`'s tables and after the header
comment.

### Migration

A target whose `deploy.toml` was written before this unit carries no `preset` answer, so a `plan` or
an unattended `apply` that resolves the `[adopt] argv` refuses naming `preset`, `resolve_tokens`'
missing-answer path (`govkit.py:1233-1249`). The upgrade step is one line under `[answers]`,
`preset = "<name>"`; `help/policy.md` states it. No adopter of the policy kit exists at this spec's
base, since dGroundRules has not landed.

### Inventory

| Identifier | Kind | Home |
|---|---|---|
| `{preset}` | install token | `tools/policy/kit.toml` |
| `--preset` | flag | `tools/policy/adopt-policy.sh`, `tools/policy/policy.py scaffold` |
| `preset` | `[answers]` key | a target's `.governance/deploy.toml` |

### Files touched (estimate)

- `tools/policy/kit.toml`: the `[adopt] argv`
- `tools/policy/adopt-policy.sh`: `--preset`, the kept-file line
- `tools/policy/policy.py`: `render_scaffold(rows, preset)`, `scaffold --preset`
- `tools/policy/check_policy.py`: the `intake-preset` case
- `tools/govkit/selftest.py`: `DEPLOY_FULL`'s answer
- `help/policy.md`

### Alternatives rejected

- **The answer in deploy.toml's `[policy]` table.** That table is the deployer's own two switches
  (`on_baseline_red`, `on_hook_block`); a preset there would give one table two owners.
- **A probe deriving the preset.** Nothing in a target's tree says which posture its owner wants; a
  derived answer would be a guessed one.

## 5. Production-readiness checklist

- security — deny by default: no answer is invented, an unknown name writes nothing, and a kept file
  is never rewritten by the deployer.
- perf / scale — one more argv token; no new process.
- error / empty / loading states — a missing answer is intake's existing refusal naming `preset`; an
  unknown name exits 2 naming the shipped four.
- observability — the kept-file line names the file's preset and the answer.
- risks — a target that answers `strict` or `guarded` refuses hook bypass from its first commit
  (v2:1467-1469); `help/policy.md` says so beside the four values.
- testing — the case of §6 and the arm in §7.
- migration — §4.
- user docs — `help/policy.md`, S5.

## 6. Acceptance criteria

The case is `intake-preset` in the policy kit's fixture: a fresh `git init` target under `%TEMP%`
with a short name, installed by the deployer from a scratch snapshot, as `adopter-fresh-target` does.

- **AC1** — When `python govkit.py intake --target <dir> --kits <ids>` runs, `<ids>` the policy kit
  and the closure of its `requires`, with every answer but `preset`, it exits non-zero naming
  `preset` and writes no `deploy.toml`.
  Red when: intake writes a descriptor with no preset, or invents one.
- **AC2** — When it runs with `--answer preset=strict`, the written `deploy.toml` carries `preset =
  "strict"` under `[answers]` and its `[policy]` table holds only `on_baseline_red` and
  `on_hook_block`.
  Red when: the answer lands outside `[answers]`.
- **AC3** — When `apply` then runs, the target's policy file opens, after its header comment, with
  `preset = "strict"`, and `python policy.py get hooks.bypass --explain` there prints `refused` with
  source `preset`.
  Red when: the scaffold drops the answer, so the target reads `allowed`.
- **AC4** — When `bash adopt-policy.sh --scaffold --preset lax --target <dir>` runs on a target with
  no policy file, it exits 2 naming `lax` and the four shipped presets, and no file exists after.
  Red when: an unknown preset is written.
- **AC5** — When the target already holds a policy file naming `standard` and the scaffold runs with
  `--preset strict`, the file's bytes are unchanged and one line names `standard` and `strict`.
  Red when: the deployer rewrites a kept file, or keeps it silently.
- **AC6** — When `python check_policy.py --fixture adopter-fresh-target` runs after S4, it installs
  with the `preset` answer and grades as before.
  Red when: the fixture's answer set lacks `preset` and its install refuses.
- **AC7** — When `grep -n "intake" policy.md` runs in the help directory, it prints the paragraph
  naming the answer, the four values and the upgrade line.
  Red when: the page omits the intake answer.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 AC2 AC3 AC4 AC5 · the `intake-preset` case, staged by an install with no answer, an unknown name and a kept file · none

## 8. Open questions

- **F1 — With no answer, does intake default to `standard` or refuse?** (a) Refuse, as `cmd_intake`
  does for every answer (`govkit.py:13144-13151`: "an answer this tool guesses is one the operator
  never made and cannot audit"); (b) default `standard`, the `preset` key's catalogue default,
  through a new optional-answer form in `needed_answers`. v2:1412 makes choosing a preset a policy
  change, guarded and recorded, which a guessed answer is not, and (b) changes the deployer's
  deny-by-default rule for one token. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2:1412
  and the deployer's own stated rule; an operator who wants the default answers `standard`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-32`, `KICK-dKeptSession-44`
  mirrored, the other ends of the edges the round-1 spec audit's promoted units declare; no other
  section moved.

## 10. Reuse audit

The seam extended is govkit's derived-answer route: `needed_answers` (`tools/govkit/govkit.py:13089`)
collects every `{token}` (`TOKEN_RX`, `:1138`) from a selected kit's `adopt`, `check` and `gate_leg`
argv, `cmd_intake` (`:13122`) records each under `[answers]` (`:13165-13166`) and refuses a missing
one (`:13144-13151`), all verified at HEAD; the scaffold is dGroundRules' `render_scaffold` (GR
`policy.py:1313`) called by `adopt-policy.sh --scaffold` (GR `adopt-policy.sh:91-104`), and its
`[adopt] argv` is GR `kit.toml:32-33`. `python tools/codebase-map/reuse_lookup.py "intake answer
token recorded in deploy descriptor and scaffold"` ranked `records`, `resolve_prefix_token`,
`read_descriptors` and `render_record`: `resolve_prefix_token` is the `prefix` answer's own
spelling, not a second route. `python tools/memory-recall/query.py "how does govkit intake ask for
the policy preset and write the scaffold"` returned scout A's row 4 and this build's brief.
Disagreement: none; scout A's line numbers match HEAD and the branch.

Recall terms used: govkit intake needed_answers cmd_intake answers token scaffold render_scaffold preset deploy.toml
