# TOOL-dWitnessedBar-6 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-6

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-20, by running the unit's own CLIs: each plant of `verdict_backends.py --fixture` in
`tools/run-gates/`, which builds its scratch repositories, bare remotes and canned API answers in the
system temp dir and drives `read`, a copy of the lander and `remote_verdict.py --responses`; the loop
guard's new plant `pin-owner-only`; `remote_verdict.py pin` over a scratch repository; a probe of the
driver's `write_held_asks` and `write_pin_ask` sourced from `unattended.sh`; `verify-peer` over a scratch
remote with a stub bar; and the greps the criteria name. The three new arms section 7 declares
(`run-gates.gov.test.sh`'s plant loop, `push-main.test.sh` case 43, the re-pointed h9 arm of
`unattended.test.sh`) were written and not run: their runs and RED-first observations are owed to the
main loop at the close, with the legs section 7 names.

**Evidences:** TOOL-dWitnessedBar-6
- AC1 — `registry` — the plant exited 2: over the tree it printed `local-hook off_node=false`,
  `peer-node off_node=true` and `remote-ci off_node=true`, each with `tools/run-gates/kit.toml`; with a
  second descriptor declaring `local-hook`, `read_backends` refused `verdict backend local-hook is declared
  twice: in tools/other/kit.toml and in tools/run-gates/kit.toml`; 2 of 2 held.
- AC2 — `unregistered` — `read` exited 2 and the fixture lander 1, each passing on the policy reader's
  refusal `verdict: "ci-cloud" is not one of ["local-hook", "peer-node", "remote-ci"]`, and the bare
  remote's refs were unchanged; under `undeclared` both refused `verdict = remote-ci names no declared
  verdict backend; the descriptors declare local-hook, peer-node`, the lander exiting 1, no ref moved.
- AC3 — `local-green` — `read --backend local-hook` printed `GREEN` (exit 0) over a full slot reading
  GREEN, `RED` over one reading RED, `NONE` with no file and `NONE` with only `<tree>.scoped` reading GREEN.
- AC4 — `peer` — a tag pushed by `write_peer_tag` as node `b` read `GREEN` under `GOV_NODE=a`; the same
  tag from node `a` read `NONE` (`this node's own, so it is not off-node`), and one whose `tree` line
  named another tree read `NONE`; `verify-peer` under `GOV_NODE=b` over a scratch remote with a stub bar
  published `refs/gov/verdict/<sha>`, skipped it on a second run, and node `a` read it `GREEN`.
- AC5 — `remote-green` — `remote_verdict.py read --responses <dir> --sha <sha>` printed `GREEN`; over
  `other-path` and `step-skipped`, `NONE`; over `api-404`, `DEAD PROBE` (`GET ... answered HTTP 404`).
- AC6 — `swapped-workflow` — under the default trust it printed `HELD` naming
  `.github/workflows/remote-ci.yml`; with `verdict.remote.trust = "app-only"` at the landed revision,
  `GREEN · <sha8> · witness claimed`.
- AC7 — `read_held_reds()` — `git grep -n 'read_held_reds()' tools/unattended` printed nothing; the `held`
  plant printed two `held` rows and `held reader: run 77 at aaaaaaaa · 2 held job(s) read · 1 red`; the
  sourced `write_held_asks` called the kit's `remote_verdict.py held https://github.com/o/r.git
  remote-ci.yml` and printed the same ask rows as before, and with no kit resolving printed one `held
  reader: DEAD PROBE` line and called nothing; `check-arms.py --emit-floors` names
  `tools/unattended/unattended.sh:343:339`, its ceiling 343 unmoved.
- AC8 — `dispatch-closure` — `remote_verdict.py pin` over a scratch repository whose policy sets that
  scope printed four `<path> <blob>` lines, each blob equal to `git rev-parse HEAD:<path>`, and a
  `verdict.remote.pin` id equal to `git hash-object --stdin` over them, the tree left clean; the guard
  plant `pin-owner-only` (`agents-with-reason`, the change record and the decision row staged, off a live
  run's branch) exited 1 naming `verdict.remote.pin: owner-only`, the value's rule admitting the rest.
- AC9 — `lander-peer` — the plant's lander under `verdict = "peer-node"` printed `verdict: peer-node · NONE`,
  published `refs/gov/candidate/<sha>` on the bare remote and exited 1 with `reads NONE ... so nothing is
  pushed to main`; the remote's main was unmoved.
- AC10 — `verdict-backends` — `grep -n 'verdict-backends' help/README.md` names line 20;
  `grep -c 'verdict_backend' tools/run-gates/README.md` printed 6; `grep -c '^verdict'
  tools/policy/unsummarised-keys.txt` printed 0; `help/reference/policy.md` line 200 is
  ``## `verdict.remote.pin` ``.
