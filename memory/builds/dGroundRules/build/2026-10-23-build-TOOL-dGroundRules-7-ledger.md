# TOOL-dGroundRules-7 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-7

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed before the
commit, with this unit's edit in the worktree: the list through the kit's own `lists` verbs on the
built tree, the greps over the generated list, and the planted cases through the kit's own fixture
CLI, run for the one case `legacy-homes`, its seven repositories under the system temp directory,
short-named and removed by the case. The New arm's RED-first observation is the close's.

**Evidences:** TOOL-dGroundRules-7
- AC1 — `python policy.py lists --check` — run from the repository root as `python tools/policy/policy.py lists --check` after `lists --write`, exit 0: "policy lists: legacy-homes.txt · 115 row(s) derived from the legacy homes", "legacy homes: no landed list at ed497191, so this one seeds the baseline", "policy lists: green · 0 finding(s)". 115 rows is the spec's measured figure: 102 kit conf rows (`.codebase-map.conf` 6, `.lexicon.conf` 2, `.memory-tree.conf` 35, `.process-monitor.conf` 6, `.unattended.conf` 53), 11 gate rows, 2 house rows, with 45 kit conf keys left off as retrofit conversions.
- AC2 — `python check_policy.py --fixture legacy-homes` — run as `python tools/policy/check_policy.py --fixture legacy-homes`, exit 0, 11 assertions, 0 wrong: case `planted-row` printed "case planted-row: red · lists --check · exit 1 · 1 report(s) · typed row .unattended.conf PLANTED_KEY owner-policy", the one report §4 item 1b gives; case `today` printed "case today: green · lists --check · exit 0 · 0 report(s)".
- AC3 — `grep "^.githooks/gate-env.sh " legacy-homes.txt` — run in the kit directory, it printed eleven rows: `GATE_DOC_PATHS`, `GATE_POST_MERGE`, `GATE_WSL_PARITY_RUNS`, `INHERITED_RED`, `INHERITED_RED_MAX_AGE` owner-policy and `GATE_SELFTESTS`, `GATE_WSL_MIRROR_DEFAULT`, `GOV_BRANCH_GATE_CMD`, `GOV_GATE_CMD`, `GOV_KITROOT`, `GOV_PYTHON` mechanic, the mark table's keys and no other; `GATE_POLICY_FILE` is absent. A probe of `scan_gate_readers` printed the reader calls' keys, `GATE_POLICY_FILE` and `HELD_CI_WORKFLOW` among them, both kit conf rows of `.unattended.conf`.
- AC4 — `grep -c " REVIEW_ROUNDS owner-policy" legacy-homes.txt` — printed 1, and `grep -cE "_(CUTOFF|PIN) " legacy-homes.txt` printed 0.
- AC5 — `grep "^<tool-root>/roles/house/policy.toml " legacy-homes.txt` — printed exactly `<tool-root>/roles/house/policy.toml [effort] owner-policy` and `<tool-root>/roles/house/policy.toml [gates] owner-policy`.
- AC6 — `python check_policy.py --fixture legacy-homes` — case `growth` (`PLANTED_NEW` assigned in the fixture's `.unattended.conf`, its row typed into the list) printed "case growth: red · lists --check · exit 1 · 1 report(s) · .unattended.conf PLANTED_NEW is a new legacy home and the list is shrink-only; carry it as a key in <the derived catalogue path> instead", and its sub-step "case growth: lists --write · exit 1 · ... · the list unchanged".
- AC7 — `python check_policy.py --fixture legacy-homes` — case `shrink` (`KEPT_KEY` removed from the fixture's `.unattended.conf`, its pair in the landed list) printed "case shrink: red · lists --check · exit 1 · 1 report(s) · stale list at .unattended.conf KEPT_KEY owner-policy, re-run lists --write", then "case shrink: lists --write · exit 0", then "case shrink, after lists --write: green · lists --check · exit 0 · 0 report(s) · the row gone"; no typed-row report.
- AC8 — `python check_policy.py --fixture legacy-homes` — case `retrofit` (`PLANTED_CUTOFF="2026-11-01"` and `PLANTED_PIN="3"` added) printed "case retrofit: green · lists --check · exit 0 · 0 report(s)" and, after `lists --write`, "0 PLANTED_ row(s) listed".
- AC9 — `python check_policy.py --fixture legacy-homes` — case `unmarked` (`GATE_PLANTED=1` in the fixture's gate file before the seed, so its landed list holds the pair) printed "case unmarked: red · lists --check · exit 1 · 1 report(s) · GATE_PLANTED in .githooks/gate-env.sh has no mark in GATE_ENV_MARKS"; the list row reads `unmarked`, never a default mark.
- AC10 — `python check_policy.py --fixture legacy-homes` — case `absent-homes` (no gate file, no house file) printed "case absent-homes: green · lists --check · exit 0 · 0 report(s) · announced: .githooks/gate-env.sh, <tool-root>/roles/house/policy.toml", one announce line for each absent home.

Owed at the close, observed by no command in this pass:

- The New arm line of §7, `tools/policy/check_policy.py`'s `--fixture legacy-homes`: RED on a staged break of `check_legacy_homes` and GREEN restored.
- The §7 legs over the built tree, and the `policy check` and `policy fixtures` legs. `adopter-fresh-target` reds on `arm_legacy_homes` in the fresh adopter until TOOL-dGroundRules-17, as the README's "Each arm in an adopter" row says. A probe of `run_arm(arm_legacy_homes, ".", KIT)` on gov's own tree found no finding: "115 row(s) derived from the legacy homes · no landed list at ed497191, so this one seeds the baseline".
