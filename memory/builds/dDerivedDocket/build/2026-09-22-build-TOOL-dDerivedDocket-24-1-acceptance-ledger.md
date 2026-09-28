# TOOL-dDerivedDocket-24 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-24

The inherited-red policy is built at all three readers. The runner ages and owns each INHERITED leg
under `GATE_INHERITED_RED_MAX_AGE`, writes the three columns before the reason, and writes
`gate-inherited-green` under an exported `land`. The pre-push hook parses the two keys out of its
policy file at the remote sha, reads that stamp whenever FULL would be forced, and lands an
inherited-only red on an unmoved tree. The driver reads `GATE_POLICY_FILE` and the policy at the
advertised tip, pins the run id, applies the decision table, files one ask per INHERITED leg once
`ASKS_CMD` is declared, and refuses the two escape routes unless that record backs them. The leg's
check 23 reads the absorb subject, and govkit's predicate compiles from `POLICY_KEYS`. The spec
moved to rev-7 for the `gates-run` fact's timing and row four's reading, and its section 9 line
says so.

No merge bar, no gate leg and no `*.test.sh` suite ran in this pass. Four replicas ran by hand, from
the scratch root, each assembled from the suite's own text and run over its own fixture. The
runner's and the driver's replicas used a short directory under the system temp root instead,
because `git worktree add` refuses the scratch root's length with `'$GIT_DIR' too big`: the MAX_PATH
case TOOL-aProbedUnit-11 records.

- The leg suite's prologue and the three ABSORB arms: 9 assertions, all green.
- The hook suite's inherited-red block: 13 of its 14 arms ok. The fourteenth is AC11's, which read
  `park` because HEAD did not yet carry gov's `land`, and it is owed to the run after this commit.
- The canary's age block over the real runner: 6 assertions green. `age 8 · owner <sha8>` and the id
  its subject carries came back for a red that arrived at landing 4 of 12, `aged at R~10` for one that
  arrived at landing 1, and a stamp that names R, the bound and the leg.
- The driver suite's inherited-red block over the real driver: 66 assertions, every one green
  except AC11's, the same pre-commit case. AC19's real-runner arm first read `aged`, because the
  fixture's leg was red on every earlier commit of its first-parent line and the probe at R~10 found
  it; the leg is now red only from AC19's own commit, and the arm read MET.

The predicate govkit compiles was lifted from `govkit.py`'s own text and run over eight policy
lines, four invocations and the tracked tree: every policy line caught with its key named, no
invocation caught, and `.githooks/gate-env.sh`, which no kit ships, the one policy file in the tree.

Every criterion observed through a suite, or through `bash tools/unattended/check-unattended.sh`
over the real tree, carries a `permission:` line deferring it to VERIFYING, so none of them gets a
line here: AC1 to AC7, AC9, AC11 to AC19, and AC21 to AC23. The same goes for AC10's leg half.

**Evidences:** TOOL-dDerivedDocket-24
- AC2 — `pre-push self-test` — at 364278a8 the leg exited 0, `pre-push.test: all cases ok`, with
  `IR AC2 an inherited-only red within its age lands under land`, whose arm matches exit 0 and
  `red on inherited legs only — landing under INHERITED_RED=land: x` naming leg `x`;
  `IR AC2 the runner is handed land, the bound 10 and R`; and
  `IR AC2 a MIXED leg is blocked under land`, whose arm matches exit 1.
- AC3 — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — at 364278a8 its
  `run-gates canary` leg exited 0 with `PASS (266 assertions)` and no SKIP line. Its age arms, over
  a twelve-landing fixture under `GATE_INHERITED_RED_MAX_AGE=10`, assert a red arriving at landing
  4 reads `INHERITED` at `age 8` naming that landing's owner sha and id, in the record's columns
  too, and a red already present at landing 1 reads `aged at R~10` and writes no
  `gate-inherited-green`.
- AC4 — `gate-inherited-green` — at 364278a8 `run-gates canary` (exit 0, `PASS (266 assertions)`)
  asserts an inherited-only bar under `land` writes `gate-inherited-green` naming R, the bound 10
  and the leg, and writes no `gate-full-green` into a git dir that held none. `pre-push self-test`
  (exit 0, all cases ok) logged `IR AC4 an inherited green at the remote sha scopes the gate` and
  `IR AC4 a moved remote sha forces FULL past the inherited green`.
- AC8 — `ABSORB` — over the leg suite's fixture: a pass that declared `work/one.txt` and an
  `absorb(tRun): memory hygiene inherited at 0123abcd` commit writing `fix/leg.txt` printed
  `check 23 ABSORB` naming that path, with no FAILED and no dodged-join line. The same commit moving
  a declared path while no commit named the pass was an ABSORB too. The same paths under a subject
  that also named the unit id printed no ABSORB and reded the ceiling as an undeclared write.
- AC10 — `hold ·` — the skill-wiring half. `adopt-unattended.sh --check` reads `in sync`, and the
  rendered Skill's Close section names the hold for an inherited red under `park` once. Its steps run
  commit, push, reap, then `--hold`, and the rendered stops guide states ABSORB's four conditions and
  the absorb subject. The leg half over the rendered tree is owed at VERIFYING.
- AC14 — `pre-push self-test` — at 364278a8 the leg exited 0, `pre-push.test: all cases ok`, with
  `IR AC14 a stamp's wider window is not trusted`, whose arm matches `FULL gate on main push` and
  a reason naming the stamp's `max_age 50` and the bound 10 at the remote sha.
- AC16 — `pre-push self-test` — at 364278a8 the leg exited 0, `pre-push.test: all cases ok`, with
  `IR AC16 a stale full green still reaches the inherited green`, whose arm matches
  `scoped gate on main push` naming the inherited green, over a full green that
  `is not an ancestor of the pushed tip`.
- AC20 — `memory/DECISIONS.md` — the TOOL heading carries one `TOOL-dDerivedDocket-24` row naming
  D12-i4, the charter's 'blocks a red one' and 'green at the push boundary', and the protocol's
  `gates-green`, at 287 bytes against the 300 budget.
- AC22 — `govkit selftest` — at 364278a8 the leg exited 0, `govkit-selftest: all arms held`, with
  `AC22: a bare INHERITED_RED assignment inside a kit's payload REDS, naming the file` and the same
  arm for `INHERITED_RED_MAX_AGE` both `ok`. Each runs `govkit.py selfcheck` over a scratch kit
  whose `tools/demo/policy.sh` carries `INHERITED_RED=land`, then
  `export INHERITED_RED_MAX_AGE=10  # gov only`, and matches exit 1 naming that file.
- AC24 — `wc -c < memory/guides/UNATTENDED-PROTOCOL.md` — 64744 bytes and 706 lines at the parent,
  64719 and 704 here, the `GATE_POLICY_FILE` row being one line of 170 bytes against the 195-byte
  paragraph it replaced. `grep -c 'contend on the bar' tools/unattended/README.md` prints 1.
