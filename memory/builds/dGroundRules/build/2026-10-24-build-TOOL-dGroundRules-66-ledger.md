# TOOL-dGroundRules-66 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-66

No merge bar, gate leg or self-test suite ran in this pass. AC4 to AC7 ran from the worktree root with
this unit's edit in place. AC1 to AC3 each ran in a fresh `--branch` clone of the run branch at
`ef04a7f00` under `%TEMP%`, made as section 6 makes `D`, with `RUN_CLAIMS="off"` and a blank
`SPEC_TOKENS_CLI` appended to its conf, BEFORE the base driver `3c2b69be:tools/unattended/unattended.sh`
and AFTER this pass's driver, and removed after. AC8 ran in such a clone holding this pass's changed
files committed as the pass commit with a `Pass: TOOL-dGroundRules-66` trailer, before the real pass
commit, because its ledger line rides in that commit. The New arm's red-first observation, and the
suite run that executes it, are the close's.

**Evidences:** TOOL-dGroundRules-66
- AC1 — `.governance/policy.json with tools/policy/policy.py` — BEFORE, `--dispatch dGroundRules --pass TOOL-dGroundRules-66 --writes tools/policy/policy.py` exited 1 with check 49's condition-3 line ending `.governance/policy.json with tools/policy/policy.py`. AFTER, in a fresh clone, it exited 0 printing `d88f7ddd TOOL-dGroundRules-19 left out as terminal (CLOSED)` (and the same for `729e5128`) then `dispatch declared — ef04a7f0 TOOL-dGroundRules-66 · tools/policy/policy.py`.
- AC2 — `left out as terminal (WONTDO)` — AFTER, with unit 19's spec header set to `INPROGRESS` by the criterion's `sed`, AC1's command exited 1 printing `.governance/policy.json with tools/policy/policy.py`; in another fresh clone with `WONTDO` in its place it exited 0, printing `left out as terminal (WONTDO)` for both of unit 19's keys and `dispatch declared`.
- AC3 — `reserves nothing against a sibling` — AFTER, `--dispatch dGroundRules --pass TOOL-dGroundRules-24 --writes help/README.md` exited 0 printing `unattended: dispatch — TOOL-dGroundRules-24 is CLOSED, so this declaration reserves nothing against a sibling; set its spec back to INPROGRESS for it to`; BEFORE it exited 0 with `dispatch declared` and no such line.
- AC4 — `left out as terminal (CLOSED)` — `read_open_passes memory/builds/dGroundRules/RUN.md` after `load_spec_facts` over the build's tracked specs printed exactly two `left out as terminal (CLOSED)` lines, naming `729e5128` and `d88f7ddd`, and no row carrying `TOOL-dGroundRules-19 · reason`; with `current` added it printed no line naming `TOOL-dGroundRules-19`. The one row it printed was this pass's own open key.
- AC5 — `verb_dispatch 1` — the criterion's `type` loop printed `verb_dispatch 1`, `print_audit 1` and `check_commit_message 0`.
- AC6 — `ROUTED_PATHS` — over `print_audit`'s range, `grep -c "right answer for .--dispatch"` printed 0 and `grep -c ROUTED_PATHS` printed 2; over `check_commit_message`'s range, `grep -c "check_pass_open alone"` printed 1.
- AC7 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` — exited 0, and `grep -c "whose spec is CLOSED or WONTDO is not a sibling"` printed 1 for each file.
- AC8 — `TOOL-dGroundRules-7 · tools/policy/policy.py` — unit 7's command in the replica clone exited 1 with BEFORE, printing `.governance/policy.json with tools/policy/policy.py`, and 0 with AFTER, printing `dispatch declared — 343e8136 TOOL-dGroundRules-7 · tools/policy/policy.py tools/policy/legacy-homes.txt tools/policy/check_policy.py tools/policy/README.md tools/policy/kit.toml help/policy.md` after the two `left out as terminal (CLOSED)` lines and "no sibling pass is open", so this pass's own key read closed at its commit.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: tools/unattended/unattended.test.sh --shard 4/8 with tools/unattended/unattended.sh at cfdee9fd0^: `FAIL missing: dispatch declared`, `FAIL missing: ARCH-tRun-1 left out as terminal (CLOSED), so its declared paths reserve nothing: work/idx.md`, `FAIL missing: ARCH-tRun-1 is CLOSED, so this declaration reserves nothing against a sibling`. Same shard with the terminal test staged to also take INPROGRESS: `FAIL missing: --dispatch declares a generated index together with its generator`, `FAIL unexpected: left out as terminal`. GREEN at fce5603f8 after TOOL-dGroundRules-70: `PASS (596 assertions)`.
