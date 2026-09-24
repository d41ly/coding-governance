# TOOL-aRepatriatedFork-5 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-5

One unit pass under the mandate. It ran no merge bar and no self-test suite: the gate guard refuses
the new `.githooks/pre_push_bar_selftest.py` by name while the run is BUILDING, so neither it nor the
three edited `*.test.sh` suites were executed here. Every criterion below was observed by a scratch
fixture driving real `git push` calls, or by a direct checker. No adopter tree was written; the one
NicoCares read was `git cat-file` at nc `14b9fb7a`.

## The fixtures

- **Push fixture**: a scratch repo and bare remote under `%TEMP%/pb5`, the hook under test installed
  through `core.hooksPath`, the default bar at `scripts/run-gates/run-gates.sh` printing
  `DEFAULT BAR RAN - RED` and exiting 1, a tracked GREEN `scripts/unattended-bar.sh`, an untracked
  stub outside the repo, and a `gatepayload` PATH command. One push per case, recording rc, whether
  the remote moved, the decision line and the last run-log END line.
- **Hooks driven**: the a7c78ad2 bytes (`git show a7c78ad2:.githooks/pre-push`), this unit's hook, and
  a copy of this unit's hook with the harness's NEUTER line spliced after its `    set +f` anchor.
- **Lander fixture**: a scratch repo under `%TEMP%/pb6` declaring `LANDER_MARKER=unattended-landed`,
  driven through the HEAD and the new `tools/push-main.sh` with the new hook.
- **Adopter-shaped clone**: a fresh `git init` under `%TEMP%/pb8`, which carries no gov history, with
  the red-first control block sliced out of `.githooks/pre-push.test.sh` and run against it.

**Evidences:** TOOL-aRepatriatedFork-5
- AC1 — `GOV_GATE_CMD=true` — the new hook exited 1 with `names no script at all` and the remote did not move; the a7c78ad2 hook exited 0 and the remote moved under `FULL gate … no recorded full green`
- AC2 — `.githooks/pre-push` — the new hook refused all four hostile values, untracked, PATH payload, `-c` payload and rewritten working copy, before `UNTRACKED STUB RAN`, `PAYLOAD RAN` or `DIRTY WORKING COPY RAN` printed; the a7c78ad2 hook landed all four at rc 0
- AC3 — `bar: bash` — with `bash scripts/unattended-bar.sh` tracked and unmodified, it landed at rc 0 under a decision line ending `bar: bash scripts/unattended-bar.sh`
- AC4 — `GOV_GATE_CMD_TEST=1` — the untracked stub landed at rc 0 under a decision line carrying `bar: STUB bash`
- AC5 — `pushes.log` — the last END line read `bar=default` with no override, `bar=tracked` for the vetted bar and `bar=stub` under the escape; every refusal read `decision=refuse-bar` with no `bar` key
- AC6 — `tools/push-main.sh` — under `GOV_GATE_CMD_TEST=1` it landed at rc 0, printed `NOT writing the lander marker`, and no marker file existed; the HEAD bytes wrote `landed main at <sha> by push-main`; with a tracked bar and no escape the new bytes wrote the marker naming the pushed commit
- AC7 — `grep -L 'GOV_GATE_CMD_TEST' .githooks/pre-push.test.sh .githooks/pre-push.runlog.test.sh tools/push-main.test.sh` — over the three harnesses it printed nothing
- AC8 — `05455c45` — `AC1 red-first control NOT RUN` was printed by the sliced control in the clone without `05455c45`, which recorded no failure; the HEAD slice called `bad` there, and in gov's tree the new slice resolved the commit and printed no SKIP
- AC9 — `git grep -n 'overrides the gate for testing\|or by overriding the gate command' -- AGENTS.md tools/unattended` — no line, exit 1
- AC10 — `.githooks/pre-push` — with the harness's NEUTER line spliced after the anchor in a copy, the PATH payload, the `-c` payload and the rewritten working copy each landed at rc 0 with their own text printed; the unmutated hook refused all three
