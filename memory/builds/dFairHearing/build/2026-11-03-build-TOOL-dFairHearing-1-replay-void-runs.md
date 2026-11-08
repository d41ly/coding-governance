# TOOL-dFairHearing-1 — the first replay 3 and 4 runs, voided

**Serves:** research TOOL-dFairHearing-1

The main loop spawned replays 3 and 4 on 2026-11-03 with each agent reading its whole staged input file. Each of those files carries its `## The bar` section above `## The prompt, verbatim`, so an agent reading the file reads the expected answer. The #23 skeptic said so in its return ("I read the brief's bar section before I knew I wasn't supposed to"). All four runs are void: the two skeptics' returns are kept below as raw data, and the two synthesizers were stopped before they returned. The re-runs read a copy holding only the prompt and the schema sections.

## The control skeptic (void)

The agent's final message, verbatim. Agent `gov-skeptic` at medium effort, spawned by the main loop on 2026-11-03 with the handoff `prompts/2026-11-03-prompt-TOOL-dFairHearing-1-7-skeptic.md`, over the staged input `2026-11-03-build-TOOL-dFairHearing-1-replay-4-skeptic-control.md`. 8 tool uses, 49.9 s, 29.0k tokens.

```json
{"path":"","verdicts":[{"id":1,"verdict":"refuted","reason":"The diff did not introduce this defect, and at the head it no longer exists. At base 0ac2418c0, build_rows set each worktree's action from derive_action alone and never checked containment, so the defect was already there unchanged (PRE-EXISTING per SCOPE). The diff removes it. At f0e00195e, build_rows (branch_reconcile.py:1015-1028) first gives every worktree row its base action. It then builds `held` from every worktree row whose action is not `remove worktree`. Any `remove worktree` row with a held path under it (check_under) is demoted to `keep (contains kept worktree <path>)`. Only after that does it build `kept` from the final worktree actions and derive the local-branch actions, so X's branch also stays. Write mode reads r[\"action\"] (line 954) and does not recompute it. read_dirt's drop (now at lines 267-269) is unchanged. Its `others` list comes from the same `git worktree list` that fills wt_rows (read_worktrees, lines 311-319), so every worktree it hides is a row that `held` can see. The new selftest arm_keeps builds the cited fixture: outer linked worktree on x-br, inner at outer/.claude/worktrees/inner holding precious.txt, run from a linked worktree. It asserts the outer row reads `keep (contains kept worktree`, and that --write leaves outer, precious.txt and x-br in place. That arm is source I read, not a run.","fixVerdict":"sound","fixNote":""}]}
```

## The #23 skeptic (void)

Agent `gov-skeptic`, handoff `prompts/2026-11-03-prompt-TOOL-dFairHearing-1-6-skeptic.md`, 10 tool uses, 98.2 s. Its JSON, verbatim:

```json
{"path":"","verdicts":[{"id":1,"verdict":"refuted","reason":"PRE-EXISTING at the base, and this diff cures it rather than introducing it. At ff0b3dc32, `git show ff0b3dc32:.memory-tree.conf` line 18 has ROUTED_COMMIT_WAIVED listing only 61c3a3aa47a0 d608d04954ef a481c2a751d9 61ad831fb7f0 79126924852f. 3d05f1ead, 4e49aeb53 and d31d7bc96 are all ancestors of the base (`merge-base --is-ancestor`), and they came in through 8dea35478 (merge of origin/main 76b9c451). Their committer dates (%cI, which routed_commits.py compares against the cutoff) are 2026-10-09, each touches tools/, and each has an empty Pass trailer and no unit id in its subject. So at the base, check_routed_commits in WHOLE mode would list them as `names no unit`, and the defect is real there. Under SCOPE, though, a defect that is present at the base and that the diff did not introduce or make reachable is out of scope. The diff's one fix commit, 5b4f964d5, adds exactly these three 12-hex prefixes, so at head the cited instance is cured.","fixVerdict":"instance","fixNote":"Waive by class, not by sha. Either grade only commits whose first parent already tracks tools/memory-tree/routed_commits.py, since a commit made in a history without the leg could never have met it, or regenerate ROUTED_COMMIT_WAIVED from every current WHOLE violation not reachable from the leg's landing commit dfc9fe185. Then add d6aae9d18, 22efab659 and 670436cd5, which reached this branch through 8f493d467.","severity":"blocker"}]}
```

It added, after the JSON: "I read the brief's bar section before I knew I wasn't supposed to; the verdicts above come only from the code and git history."
