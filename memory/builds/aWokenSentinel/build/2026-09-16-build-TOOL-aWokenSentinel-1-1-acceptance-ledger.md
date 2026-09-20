# TOOL-aWokenSentinel-1 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-1

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite, per the build README's rule three. The one check the pass verified with is the unit's own
arm block, sourced beside the suite's prologue into a scratch runner and run ALONE — 34 executed
assertions, green against the built driver, and RED against seven frozen kit copies each missing
one graded line: the `session` write, the `pid` write, the NOTE, the moved `keepalive` write, the
`$KID` pass-through at the dispatch arm, the `refuse_if_terminal` call, and the `stage_or_fail`
call. Each break was caught by the assertion that grades that line and no other break was caught
by nothing. That block stands in for `tools/unattended/unattended.test.sh` whole, which sits on no
bar leg.

**Evidences:** TOOL-aWokenSentinel-1
- AC1 — `CLAUDE_CODE_SESSION_ID=abc CLAUDE_PID=4242 bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1` over the reset fixture, then `grep -c` for `^session: abc$`, `^pid: 4242$` and `^keepalive: k1$` — each printed `1`, exit 0, and the merged output carried no `NOTE - this harness exposes no`; RED with the `session` line removed (`expected [1], got [0]`), RED with the `pid` line removed, RED with the moved `keepalive` line removed
- AC2 — `env -u CLAUDE_CODE_SESSION_ID -u CLAUDE_PID bash "$SCRIPT" --preflight tRun --keepalive-id k1 2>&1` over a reset fixture — `^session: absent$` and `^pid: absent$` each printed `1`, the NOTE naming `session id or pid` counted `1`, exit 0; then `CLAUDE_CODE_SESSION_ID=abc env -u CLAUDE_PID …` over a reset fixture — `exposes no pid, so` counted `1`, `^session: abc$` printed `1`, `^pid: absent$` printed `1`; RED with the NOTE line removed (`AC2 one NOTE naming both: expected [1], got [0]`)
- AC3 — on AC1's record, `CLAUDE_CODE_SESSION_ID=def CLAUDE_PID=9 bash "$SCRIPT" --resume tRun --keepalive-id zzz 2>&1` — output carried `resume at phase RUNNING` and `lease replaced · keepalive k1 -> zzz · session abc -> def · pid 4242 -> 9`, the three greps with the new values each printed `1`, `git diff --cached --name-only` listed the run-state file and `git diff --cached -- memory/builds/tRun/RUN.md | grep -c '^+keepalive: zzz$'` printed `1`, exit 0; then `run --resume tRun` carried no `lease replaced` and the three values were unchanged; RED with the `$KID` pass-through removed from the dispatch arm (12 assertions), RED with the `stage_or_fail` call removed — caught ONLY by the staged-blob grep, which is why that assertion exists beside the spec's name-only one
- AC4 — `mutate` the phase to `LANDED`, then `run --resume tRun --keepalive-id yyy` — output carried `UNATTENDED check 26 FAILED` and `LANDED via --resume`, no `lease replaced`, exit 1, `^keepalive: yyy$` counted `0` and `^keepalive: zzz$` still `1`; then `run --resume tRun` carried `nothing to resume — phase LANDED is terminal` at exit 0; RED with the `refuse_if_terminal` call removed (`AC4 a terminal-record replacement exits 1: expected [1], got [0]`). amended rev-4: the spec sent `zzz` and asked for a `0` count on a record AC3 had just written `zzz` to
- AC5 — `grep -c 'write_lease' tools/unattended/unattended.sh` printed `3` at the tip and `0` at base; `grep -cE 'set_fact "\$rel" (session|pid) ' tools/unattended/unattended.sh` printed `2`, both inside `write_lease`
- AC6 — `grep -c 'carries twelve facts' tools/unattended/unattended.sh` printed `0` at the tip and `1` at base; `grep -c 'the session and pid holding the run' tools/unattended/unattended.sh` printed `1`; `grep -cE '^1[45]\. \*\*The (session id|pid)\*\*'` printed `2` over `tools/unattended/PROTOCOL.template.md` and `2` over `memory/guides/UNATTENDED-PROTOCOL.md`; the render came from `bash tools/unattended/adopt-unattended.sh` and `cmp` reported the pair identical. Leg half, `bash tools/unattended/check-unattended.sh` check 10 — observed at --close
- AC7 — `grep -c 'unattended.sh --resume <slug> \[--keepalive-id <id>\]' tools/unattended/unattended.sh` printed `1` at the tip and `0` at base; `grep -c 'REPLACES the lease'` printed `1` over `tools/unattended/VERBS.template.md` and `1` over `memory/guides/UNATTENDED-VERBS.md`; `bash tools/unattended/unattended.sh --version` printed `unattended 1.24`; the derived usage line reads `unattended.sh --resume <slug> [--keepalive-id <id>]`. Leg half, check 26's header join — observed at --close
- AC8 — `git diff --cached --name-only` before the commit listed none of the ten paths on the `watch` line of `memory/guides/SESSION-KICKOFF.md`, read from the line; `git grep -lE '^\*\*Status:\*\* CLOSED' -- memory/builds/aWokenSentinel/spec/` lists this spec after staging. Leg half, `git show --name-only --format= HEAD` on the pass commit — observed at --close
- AC9 — `grep -c '^export CLAUDE_CODE_SESSION_ID=fixture-session$' tools/unattended/unattended.test.sh` and `grep -c '^export CLAUDE_PID=999999999$' tools/unattended/unattended.test.sh` each printed `1` at the tip and `0` at base; `grep -c -- '--keepalive-id zzz' tools/unattended/unattended.test.sh` printed `1` at the tip and `0` at base

## What this ledger does not evidence

No kit gate, harness-arms leg, hygiene leg, spec-token leg, lexicon leg, install-prefix leg or
codebase-map leg ran inside this pass; every one is `--close`'s and each row above says so. The
suite's `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rose by the 34 the block executed; the suite whole
was not run, so the sharded totals are the prior measurement plus that count and not a fresh one.
The build README's authored roster row for this unit moved `PLANNED` to `CLOSED` beside the spec
header.
