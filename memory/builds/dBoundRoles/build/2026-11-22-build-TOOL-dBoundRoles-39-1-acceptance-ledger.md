**Serves:** journal TOOL-dBoundRoles-39

# TOOL-dBoundRoles-39 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `a71ff0520`: a `python` probe in the session scratchpad that ran
`tools/roles/handoff.py check-return` as a subprocess over a git fixture made under `%TEMP%` with `git init` and one
empty commit, each payload's transcript written under the fixture's `session/subagents/`, `roles.retries` at its
catalogue default of 3. The same probe over the base blob of `tools/roles/handoff.py`, exec'd with this kit on its path,
printed a `block` for the harness, unmarked, no-path and unreadable-transcript payloads alike. No gate, suite or bar ran
in the pass: the `New arm:` arm section 7 declares, its RED-first observation, and the legs section 7 lists are owed to
the main loop at the close.

**Evidences:** TOOL-dBoundRoles-39
- AC1 — `harness-typed-stop` — a payload with `agent_type` `gov-builder`, a transcript under `subagents/workflows/wf_fx-1/` and a plain-text `last_assistant_message` exited 0 with empty stdout and stderr, and the fixture's `.git/return-check/` folder stayed absent; so did the same transcript with its separators turned to `\`, and a heading-first computed task with no marker. The step is the route test in `tools/roles/handoff.py#run_return_check`. OWED: the arm 22 plant `harness-typed-stop` in `tools/roles/render_agents.py#check_return_arm`, RED first against a `check-return` with the route test removed, and the `roles render selftest` leg at the close.
- AC2 — `unmarked-stop` — a transcript under `subagents/` whose first record reads `Build it.` exited 0, printed nothing and left no record; a payload with no `agent_transcript_path` and one naming a missing file did the same. OWED: the `unmarked-stop` plant, RED first at the close.
- AC3 — `stop-retry` — the marked direct spawn printed `decision` `block` naming `outcome` on stops one to three, the record reading `attempts` 1, 2 and 3 with `valid` false, then passed with a stderr witness at 3 of 3. OWED: arm 22's `stop-retry` rows, now carrying a marked transcript (deviation 392), at the close.
- AC4 — `direct spawn` — `grep -n "direct spawn" tools/roles/README.md` printed the "The return check" section's lines saying `check-return` grades a direct spawn's return only, that a direct spawn's `agent_transcript_path` holds no `/subagents/workflows/` pair, and that a direct spawn's first `user` record opens with a marker line `roles_lib.extract_prompt_marker` parses; the next line says a harness stage's return is graded by its stage schema. OWED: nothing beyond the legs section 7 lists at the close.
- seen-red — `roles render selftest` — red `da8a257f` — green `da8a257f` — the route test of `check-return` taken out, arm 22 red
