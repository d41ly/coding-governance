# TOOL-dGroundRules-61 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-61

No merge bar, gate leg or self-test suite ran in this pass. Each criterion's command ran verbatim from
this worktree's root over `25c869a36` with this pass's files in the working tree. The staged breaks
were copies of `tools/hooks/agent-cap.js` written over the working file for one run each and restored
byte-identical after (`cmp` silent): HEAD's file, the precedence pick that grades only the first layer
setting a variable, and the reader that never appends the declared layer. The three hook-suite arms
of §7 ran outside the suite, as a scratch script replaying their lines over a fixture repository under
`%TEMP%/r61p`, removed after: green on this pass's hook, and each red on its own staged break. Owed at
the close: the `policy fixtures`, `agent-cap self-test`, `gotchas selftest` and `memory hygiene` legs
over the built tree, and the RED-first observation of both `New arm:` lines of §7.

**Evidences:** TOOL-dGroundRules-61
- AC1 — `CASE limit-settings-elsewhere-project-over`, run as `python tools/policy/check_policy.py --fixture limit-settings-elsewhere-project-over` through `tools/hooks/agent-cap.js` printed `declared at 2, project CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS at 3 · a Workflow call · exit 2` with stderr `.claude/settings.json: env.CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS is 3, above runtime.agents-in-flight 2.`, its control at 2 exit 0, and `64 assertion(s) executed · 0 wrong`; on HEAD's hook the same case printed `WRONG: exit 0 · stderr '(none)'` and `1 wrong`.
- AC2 — `CASE limit-settings-elsewhere`, run as `python tools/policy/check_policy.py --fixture limit-settings-elsewhere` printed, for its `GOV_SETTINGS_JSON at 2` check, `GOV_SETTINGS_JSON at 2 · a Workflow call · exit 0` and `68 assertion(s) executed · 0 wrong`; on the reader omitting the declared layer it printed `GOV_SETTINGS_JSON at 2 · a Workflow call · WRONG: exit 2` and `2 wrong`.
- AC3 — `CASE limit-settings-elsewhere`, run as `python tools/policy/check_policy.py --fixture limit-settings-elsewhere`, with `.claude/settings.json` planted at `2` before its `GOV_SETTINGS_JSON at 3` check, printed `GOV_SETTINGS_JSON at 3 · a Workflow call · exit 2` with stderr naming the declared file and `above runtime.agents-in-flight 2`; on the precedence pick (§8 F1 (a)) it printed `GOV_SETTINGS_JSON at 3 · a Workflow call · WRONG: exit 0` and `1 wrong`.
- AC4 — `CASE limit-settings-declared-absent`, run as `python tools/policy/check_policy.py --fixture limit-settings-declared-absent` printed `GOV_SETTINGS_JSON names no file, project at 2 · a Workflow call · exit 2` with stderr `GOV_SETTINGS_JSON names <path>, which is not a file`, so `not a file`, and `63 assertion(s) executed · 0 wrong`; on HEAD's hook it printed `WRONG: exit 2` with stderr naming the path as a layer whose `env` is absent, never `not a file`, and `1 wrong`.
- AC5 — `DOC_LAYERS`, run as `grep -nE "GOV_SETTINGS_JSON|--settings|managed" help/agent-limit.md` printed lines 34, 43, 44, 53, 58, 73 and 74: line 53 names `GOV_SETTINGS_JSON` among the three layers rule 7 reads, lines 43 and 44 name the `--settings` flag layer and the managed-policy layer as layers rule 7 never reads, and lines 73 and 74 name them again among the layers it does not read; at HEAD the page carried no line matching `--settings` or `managed`.
- AC6 — `python tools/memory-tree/gotchas.py --for-paths tools/hooks/agent-cap.js tools/check-wiring.sh` listed `check-grades-one-layer-of-a-layered-config`, and `python tools/memory-tree/gotchas.py --check` exited 0 after `--write` regenerated `memory/gotchas/INDEX.md`.
