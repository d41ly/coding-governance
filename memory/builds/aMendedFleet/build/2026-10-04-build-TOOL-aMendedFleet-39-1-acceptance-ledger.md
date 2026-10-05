# TOOL-aMendedFleet-39 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-39

**Evidences:** TOOL-aMendedFleet-39
- AC1 — `gen_map.py --check` — exited 0 after `--write`, and the `git-hooks` array in `inventories.json` read `['commit-msg', 'pre-commit', 'pre-push', 'pre-rebase']`. Red first: at base the extractor's evidence listed seven keys, three of them the helpers `gate-env.sh`, `straggler-guard.sh` and `pre_push_bar_selftest.py`
- AC2 — `harness-hooks: 10` — the grep over `MAP.md` printed that line; the extractor run directly listed ten keys, with `manifest-check.sh` once on `SessionStart` though two matchers wire it, and `procmon-hook.js` once per event
- AC3 — `harness-hooks: Stop` — in a scratch clone under the TEMP root with the working diff applied, the `Stop` command rewritten to `node -e 1` made `gen_map.py --check` exit 1 ending `harness-hooks: Stop: command names 0 ${CLAUDE_PROJECT_DIR}/ scripts, expected one: node -e 1`; rewritten instead to name `tools/unattended/no-such-guard.js`, it exited 1 naming that path as not a file in the tree. The unbroken clone exited 0
- AC4 — `pre-comit` — an empty `.githooks/pre-comit` in the same clone made `--check` exit 1 with `git-hooks: .githooks/pre-comit is not a hook name git runs (githooks(5))`; an empty `.githooks/helper.sh` instead left `--check` at 0 and the extractor at the same four keys
- AC5 — `test_codebase_map.py` — exited 0, every test `ok`; the `git grep` for a `git-hooks` claim on the three helpers printed nothing (exit 1). Red first: in the clone, emptying `FOUNDATION.md`'s `harness-hooks` claim made it exit 1 with `FAIL test_every_inventory_key_is_claimed_or_baselined` naming `SessionStart tools/check-wiring.sh` as UNCLAIMED
- AC6 — `PreToolUse` — the grep over `baseline.toml` printed nothing (exit 1)
- AC7 — `DOSSIER_CAP_BYTES` — a `python -c` reader took the cap, 20480, from `.memory-tree.conf` and sized the 28 touched dossier files: none over, the largest 20454 (`agent-cap`; `unattended` 20439). Red first: with the claim lines added and no cut, `agent-cap` measured 20578 and `unattended` 20629

## The cuts

`agent-cap` drops the measured figures of three passages, citing the record that keeps each:
`TOOL-aNumeralWarden-1` (the four-call burst), `TOOL-aReplayedCard-1`'s spec (the node spawn
timing) and `TOOL-cRefutedPremise-1` (a sidechain runs hooks). `unattended` drops two, citing
`TOOL-aBoundedVerdict-13` (the capture timing) and `TOOL-aBoundedVerdict-10` (the hung bar, whose
date and 240 s figure the backlog row keeps). The cap did not move.

## Owed at the close

- `codebase-map coverage + freshness`, `codebase-map gate coverage`, `codebase-map kit selftest`,
  `codebase-map adopter e2e`, `recall floor`, `recall floor arms`, `lexicon naming predicates`,
  `memory hygiene` and `spec tokens`. None ran here. `lexicon.py --suggest` answered OK for
  `_derive_harness_hooks`, and `encoding_posture.py` exited 0.
- `map_extractors.py` is the project-owned file in the codebase-map kit directory; whether the kit
  epoch owes a bump for it is the close's, per the brief.
