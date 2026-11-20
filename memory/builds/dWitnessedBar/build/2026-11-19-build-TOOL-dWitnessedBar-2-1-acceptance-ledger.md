# TOOL-dWitnessedBar-2 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-2

This pass ran no merge bar, no gate leg and no self-test suite. Every criterion below was checked on node
d on 2026-11-20 by probing the unit's own code: `verdict_backends.py off-node` on gov's registry and
`--fixture --plant lander-refused` and `lander-peer`, whose planted repositories sit under `%TEMP%`;
scratch fixtures under `%TEMP%` that drive a real `git push` through a copy of the pre-push hook, run a
copy of the lander through a hook that leaves no allow record, and run a copy of `check-pass-order.sh`
over a planted history; `commit_trailers.py unchecked` and `message` on gov's tree; `policy.py get` and
`lists --write`; `render_playbook.py --reference`; and the greps the criteria name. The close owes
every leg of section 7 and the RED-first observation of its four `New arm:` lines; the new arms are
`BYP AC2`, `BYP S2` and `44` in `tools/push-main.test.sh`, the `BP` arms in `.githooks/pre-push.test.sh`,
`BYP` in `.githooks/pre-push.runlog.test.sh` beside its exit-table row, and the `unwitnessed` and `no
anchor` arms in `tools/unattended/check-pass-order.test.sh`.

**Evidences:** TOOL-dWitnessedBar-2
- AC1 — `policy.py get hooks.bypass` — `grep -cE 'policy\.py"? get hooks\.bypass'` counted 1 in each of
  `tools/push-main.sh`, `.githooks/pre-push` and `tools/unattended/check-pass-order.sh`, and the
  reader-coverage pattern of `check_policy.py`, applied in process to their non-comment lines, finds
  the key in all three. `python policy.py get hooks.bypass --explain` in `tools/policy/` printed
  `allowed` with `policy: hooks.bypass · default · not set in .governance/policy.toml at e52614f4,
  origin/main, the landed revision; the catalogue default`.
- AC2 — `bypass=ungated-landing` — a copy of the lander pushed through a hook that vets its bar and
  leaves no allow record: it printed `landed UNGATED`, exited 4, printed `bypass: ungated-landing ·
  88e6319d · hooks.bypass allowed · tree verdict none`, and `.git/runlog/pushes.log` gained
  `decision=bypass bypass=ungated-landing sha=88e6319d… policy=allowed tree_verdict=none`. With the
  run-gates kit beside the lander and a full GREEN per-tree verdict planted for the pushed tree, the
  same line read `tree_verdict=GREEN`.
- AC3 — `Commit-Checked:` — a fixture push under `allowed` carrying one pass commit with no trailer and
  one with `Commit-Checked: unattended@1.0` exited 0, printed `bypass: unwitnessed-commit · 9da3acde`,
  and the journal gained one `bypass=unwitnessed-commit` line naming the first and none naming the
  control. `git interpret-trailers --in-place --if-exists replace` over a message carrying `Pass:`
  appended `Commit-Checked: unattended@1.129` into its trailer block above the comment lines, and
  `commit_trailers.py message` still read `PASSTRAILER TOOL-a-1`; this pass commit is itself made
  through `check_commit_message`, so the close reads its trailer, and `commit_trailers.py unchecked
  HEAD~1..HEAD` omitting it, at the commit.
- AC4 — `decision=refuse-bypass` — the same push under `hooks.bypass = "refused"` with `verdict =
  "peer-node"` exited 1 naming `1c17c4fb`, `pre-push-refusal` read `bypass-refused`, the journal kept
  its `bypass=unwitnessed-commit … policy=refused` line, and the push's END line read `rc=1
  exit=clean decision=refuse-bypass`.
- AC5 — `peer-node` — `python verdict_backends.py off-node --backend local-hook` in `tools/run-gates/`
  exited 1 printing `verdict-backends: off-node · local-hook · false · off-node backends: peer-node,
  remote-ci`; `--plant lander-refused` held 3 of 3: the fixture lander under `hooks.bypass =
  "refused"` and `verdict = "local-hook"` exited 1 printing `hooks.bypass is refused and verdict
  local-hook is no off-node backend … peer-node, remote-ci`, and the remote's refs were unchanged. The
  hook under the same pair refused with `bypass-refused` naming the same two names. `--plant
  lander-peer` still held 2 of 2.
- AC6 — `--preview` — over a planted history whose base adds the driver, so it is the anchor, a copy of
  `check-pass-order.sh` exited 1 under `refused` naming the unwitnessed commit and not its witnessed
  control, exited 0 under `allowed` with `pass-order: note — hooks.bypass is allowed at HEAD`, and
  `--preview` listed it under either and exited 0; a history whose driver never carried the trailer
  printed `no Commit-Checked anchor in HEAD's history` on the summary line and exited 0.
- AC7 — `## ` — `grep -n 'hooks.bypass' help/reference/policy.md` printed `35:## \`hooks.bypass\``,
  the row drained from `unsummarised-keys.txt` by `policy.py lists --write`; `grep -n
  'Commit-Checked' help/tags.md` printed lines 259, 260 and 264; `grep -n 'decision=bypass'
  tools/runlog/README.md` printed line 49.

**Beyond the spec's words:** the `lander-refused` plant of `verdict_backends.py`, the fixture the
`tools/push-main.test.sh` arm for AC5 runs as arm 43 runs `lander-peer`, inside the file §4 names; and
the `bypass-refused` refusal's `hook-bypass walk did not run` clause under `refused`, deny by default
where the trailer reader does not resolve. Neither moves a design clause.
