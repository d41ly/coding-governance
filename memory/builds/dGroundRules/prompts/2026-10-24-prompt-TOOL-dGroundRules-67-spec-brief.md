**Serves:** research TOOL-dGroundRules-67

# Spec brief — TOOL-dGroundRules-67, the close sweep

## The prompt

> Every roster unit of dGroundRules is terminal. Three repairs found at the close need product writes and so a routed unit: deviation-78's guard sweep, hygiene check 15 on the review-protocol template, and the lexicon verb pin.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-24-spec-TOOL-dGroundRules-67.md`, a Tier-1 micro-spec at order 21 (after every other unit), in the shape `memory/TEMPLATE-SPEC.md` gives and `2026-10-24-spec-TOOL-dGroundRules-66.md` follows, with its status cell `DEFERRED`. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. S1, the deviation-78 sweep: the `policy fixtures` row of `tools/gate-legs.json` gains, as a minimal in-place edit (never a re-dump of the file), the twelve paths the full `python tools/policy/check_policy.py --fixture` run at df4912bda reported as `guard-trace · WRONG … not under the policy fixtures guard`: `AGENTS.md` and, spelled `{prefix}/…`, `branch-reconcile/kit.toml`, `drift-audit/kit.toml`, `gate-lint/kit.toml`, `lexicon/kit.toml`, `memory-tree/build-readme-slot-limits.txt`, `process-monitor/kit.toml`, `pytest-parallel-guardrails/kit.toml`, `roles/agents/gov-builder.agent.md`, `template-size-limits.txt`, `unattended/kit.toml` and `workflows/kit.toml`. That run printed 769 assertions and 12 wrong, every wrong one of these. Cite `TOOL-dGroundRules-33`'s deviation-78 record as the owed step.
2. S1's measured `[guards]` hit set is one: `aScoutedSeam` TOOL-aScoutedSeam-1 §4 names `tools/workflows/kit.toml`. Waive it as TOOL-dGroundRules-23 and -25 did under ER:388: a row in `memory/project/spec-token-waivers.txt`, ask TOOL-dGroundRules-110's accept clause and severity row updated, and a deviation record in this build's `build/` folder (Risk: loosening; **Surface:** the waiver). Name exact spellings by reading those precedents.
3. S2, hygiene check 15: `tools/workflows/REVIEW-PROTOCOL.template.md` cites `.claude/settings.local.json` (rendered to `memory/guides/REVIEW-PROTOCOL.md`); respell that sentence so it names no untracked file and states the layers rule 7 reads since TOOL-dGroundRules-61 (the local settings file, the project's `.claude/settings.json`, and the file `GOV_SETTINGS_JSON` declares), and re-render the guide through the kit's renderer, naming the command.
4. S3, the verb pin: `.lexicon.conf` `VERB_OFFENDER_PIN` moves 1204 → 1212 with a RE-MEASURED comment in the house form (see the two above it), naming the eight arrivals since TOOL-dGroundRules-10 (2ebafd441), measured by diffing `lexicon.py --offenders` verb keys: `pathlike` and `spec` in `tools/memory-tree/gen_build_index.py`; `bad`, `mkrepo`, `ok` and `want` in `tools/policy/adopt-policy.test.sh`; `ask` and `grade_check` in `tools/policy/check_policy.py`; none left.
5. Acceptance criteria each name a command run from the repository root and a `Red when:`: AC1 the full `--fixture` run prints 0 wrong and no `guard-trace · WRONG` line (Red when: a path the trace reads stays out of the guard; staged break: drop one added line in a scratch copy); AC2 `python tools/check-spec-tokens.py --legs-for AGENTS.md` names `policy fixtures`; AC3 hygiene prints no check 15 line naming the review protocol; AC4 `lexicon.py --check` exits 0 on the verb pin (Red when: a ninth offender arrives). §7 names the legs the close runs (`policy fixtures`, `spec tokens`, `memory hygiene`, `lexicon naming predicates`, `workflows` render parity if one exists) and declares no `New arm:` (no suite arm is added).
6. §3 edges: none needed beyond naming TOOL-dGroundRules-33 (CLOSED) and TOOL-dGroundRules-61 (CLOSED) in prose; check hygiene check 12 stays clean.
7. Keep every acceptance code span on one line; no acceptance line starts at column 0 with `AC<n>`; no retirement word in §2; no code span holds a path glued to a quote; an untracked path sits in a fenced block.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other spec; product code; any repair beyond the three named.

### Limitations
The full fixture run and the guard pre-measure were taken by the main loop at df4912bda; re-measure if HEAD moved.

### Reuse
TOOL-dGroundRules-23 and -25's ask-110 waiver rows and deviation records; the RE-MEASURED comments in `.lexicon.conf`.
