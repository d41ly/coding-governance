**Serves:** journal TOOL-dBoundRoles-93

# Resume brief — the close of the dBoundRoles build run, after the closing review

Every unit of the roster is CLOSED, the closing review is CONVERGED, and the run stands at VERIFYING on
`branch/unattended-dboundroles-62c3df`. The two earlier briefs, `2026-11-23-prompt-TOOL-dBoundRoles-51-resume-node-a.md` and
`2026-11-24-prompt-TOOL-dBoundRoles-69-close-resume.md`, still hold the close's steps; this one replaces their state.

## What stops the run: three owner decisions

1. **The nine `Red-fix:` commits the push boundary refuses.** `routed_commits.py` grades each against the lane's limits in
   the pushed range, where no waiver is read, and these are in this branch's pushed history, made before the limit was
   known to the run: `dbc7bb6a`, `3fa017d5`, `918ffb5b`, `69a05280`, `b9a6d520`, `0b026d5c`, `e6196f84` and `f40a0e58`
   break L3, each by one generated record row the index regeneration wrote inside a spec, and `be10c468` breaks L2 by
   moving the render `.claude/agents/gov-skeptic.md`. The landing cannot pass that leg as the history stands. The
   choices seen: the owner rewrites or squashes the branch; the owner changes the limit, by its source, so a change
   inside a generated region is no spec edit, and says what happens to `be10c468`; or the owner lands it another way.
   The run refused each: a pushed history is never rewritten, and a run never moves the grader its own commits break.
2. **The reconcile merge.** `push-main.sh --prepare` at `origin/main` `3d6c1702a` refused on conflicts and names
   `git merge origin/main` on this branch as the next step, as the verbs do. The owner's rule says never to merge main
   into this branch by hand, so the run asked and did not.
3. **The flagged bar.** The notice owes `GATE_FULL=1 GATE_SELFTESTS=1` on the one `--close`. The owner decides it.

## What this session did

- Round 1 of the closing review (run `wf_e7033108-b0d`) was BLOCKED, one blocker and nine highs by finding. Its items are
  TOOL-dBoundRoles-86 to TOOL-dBoundRoles-92, specced, built and CLOSED; 92 also holds the atomic step key unit 43 owed
  and four stale expectations of the govkit self-test that were this build's. Round 2 over that fold (run
  `wf_1dced697-790`) was CONVERGED with no blocker and no high; its mediums are TOOL-dBoundRoles-93, CLOSED.
  TOOL-dBoundRoles-94 is an ask, HIGH and kept for the owner: the shell-write scan pairs quotes before it blanks
  comments, so a write after one apostrophe in a comment is admitted; the round refuted it as older than round 1's tip.
- The new arms were seen red on staged breaks in scratch trees, and the ledgers carry the seen-red lines. Not observed by
  the main loop: the arms of TOOL-dBoundRoles-18, 23, 37, 39, 40, 49, 53 to 55, 59 to 61, 64 and 89, beyond what their builders
  probed. One staged break gave no red: a role's own effort key read as absent leaves arm 29 of the roles adopter suite
  green, so that half of TOOL-dBoundRoles-21's arm is unproved.
- Suites read at VERIFYING, each beside its reading at the run BASE on the same node. Green: `spawn-guard self-test`,
  `scratch-guard self-test`, `tier2-review self-test`, `marker contracts`, `roles render selftest`, `loop factories fixtures`,
  `loop placement fixtures`, `loop position fixtures`, `unattended gate-guard selftest`. Red with the same failing set as at BASE:
  `govkit selftest`, `memory-hygiene self-test`, `check-wiring self-test`, `manifest-check self-test`, `unattended-build self-test` (its
  `DISPOSAL_SCHEMA` arm), `roles adopter self-test` (arm 8). `loop item kind` reds on `record-kind.flake` at both, the new
  `role-core` case with it. The unattended driver shards were cut short at the hold, unread.
- The held lines of the agent ledger are written.

## The bar's reds at the tip, against BASE

The plain bar ran once on `c2378668b` plus the dead-path rows. Reds BASE holds too, word for word: `lexicon wiring`,
`policy check`, `remote literals (kit code names no remote)`, `layer dependencies (the core never depends on an expansion)`,
`memory hygiene (the pass checks)`. `tags (the resolver's checks)` timed out on a loaded host. The lexicon naming leg is red at BASE and
green at `origin/main` by a raised pin, and this build adds four offenders, so it owes a pin row after the merge:
`compose_roles` and `compose_workflows`, and the canonical `refuse_wrong_shell` and `wrong_shell_at` in
`tools/roles/return-check.sh`. The rest are this build's own, each to fix after the merge, the merge first:

| Leg | What it names |
|---|---|
| `routed commits name a specced unit` | the nine commits above |
| `step-gate` | the reviewers row of `tools/roles/kit.toml` lacks, in `surfaces`, the two `drive:`, two `file:` agent, two `file:` house, two `installable:` house and two `role:` members that vanished; the row freezes at the landing |
| `loop stage coverage` | the hook `SubagentStop tools/roles/return-check.sh` has no claim row in `tools/loop/loop.toml` |
| `govkit acceptance matrix` | the outcome `no-spawn-guard-to-wire` of `tools/hooks/kit.toml` names no file that must exist, and the aged install holds no receipt |
| `encoding posture (JavaScript text IO names its encoding)` | one `readFileSync` in `tools/roles/spawn-guard.js#checkFactKeys` |
| `spawn budget (forks per hot entrypoint)` | `unattended-plan-handover` one fork over its ceiling |
| `instruction render (one renderer of record)`, `ratchet (never gains)`, `ratchet (seed laundering)`, `ratchet (rename)` | the rows of `memory/project/instructions-legacy.txt` for the agents that came, went and were renamed, and `shell-role.txt` |
| `ratchet (both ways)` | `FORK_RECORD_CUTOFF` in `date-cutoffs`, and three new steps in `landed-steps` |
| `drift-audit records` | one more armed cutoff than `drift-pins.txt`, and `PLAY-dClosedLoop-1` cited by a `purpose-source` of `tools/playbook/namespaces.toml` |
| `python reads (a name never bound, an import outside its guard)` | five unread parameters |
| `shell hygiene (a fork spent on builtin work)`, `shell hygiene (a backslashed path handed to bash)`, `portability (shell lines only shrink)` | rows of `spawn-idiom-sites.txt`, `quoting-sites.txt` and `shell-role.txt` |
| `memory hygiene` | check 15 rows for the moved hook, and check 25 over three live specs of dConvergedCharter, dTotalRecall and dWellOiledMachine that list its old path |
| `spec tokens (a spec's own names resolve)` | live specs of aOrientedCast and aScoutedSeam whose legs now include the two suites whose guards TOOL-dBoundRoles-93 widened |

The earlier briefs call the dead-path and lexicon reds inherited. They are not: `origin/main` is clean on both. The
dead-path names are widened in this session's records.

## What the resuming session does

1. Take over with `--resume dBoundRoles`, the keepalive first, in a session launched from the run worktree.
2. On the owner's answers: the reconcile, `--authorization`, then the plain bar, then the table above, each product fix in
   the red-fix lane with the index regeneration left to the next commit.
3. Re-price the budget rows this build scaled as proxies from quiet readings; today's are from a loaded node. Then
   `--prepare`, the deviation report steps of the build README, `--authorization`, `--close`, `--land`, `--landed`.

## Disclosures for the wrap-up

- Unit 92's first pass handed its work back as patches, over a missing `help/loop.md` in its declared set; its second pass
  committed them. That builder wrote one suite edit through a Python heredoc, which its role's rule on suite edits
  forbids; the diff was read. The merge of its tree was made by hand, since `pass-tree.sh --merge` renders the policy
  mirror from a committed catalogue only; the mirror is the next commit.
- Suites ran in detached scratch trees at the main loop, some while a builder worked, never inside a pass.
- One Workflow call was sent with an invented head sha and no roles; the spawn guard refused it and nothing ran.
- The earlier session's disclosures, from the brief it handed over, stand.
