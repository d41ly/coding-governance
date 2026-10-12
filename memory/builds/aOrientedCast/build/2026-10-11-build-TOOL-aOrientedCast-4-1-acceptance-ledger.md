# TOOL-aOrientedCast-4 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-4

Direct checks only; no gate, suite or bar ran in the pass. AC1 to AC4 and AC7 ran from one slice
script in the pass's scratch: the suite's helper prologue and `run_wf`, extended by the `type:` and
`wfroles:` trace lines, and the new OC4 block, with nothing else of the suite. Over the worktree's
harnesses it printed 74 `ok` and no FAIL. Over the two harnesses written from `git show 646d4a73`
it printed 47 FAIL, every typed, refusal and hand-back arm among them; the 27 that held there are the
byte-identity and untyped-spawn invariants, which hold on both sides by design. AC5 and AC6 ran the
protocol-parity script directly in `--render` and `--check` mode, with each AC6 break staged in the
worktree, observed, and restored from a byte copy taken first. The close owes the
`unattended-build self-test` suite, whose executed count is checked against the raised floor of 612
only by a whole-suite run, and the rest of the spec's §7 list, `workflow script syntax` and the
`review-protocol parity` leg included, which this pass ran only as the direct checks below.

**Evidences:** TOOL-aOrientedCast-4
- AC1 — `promptjson:` — over the CONVERGED, no-`subjects` and NON-CONVERGENT runs with no `roles`, every `promptjson:` line equalled the base render's byte for byte, no `type:` line named a type, every `wfroles:` line read `-`, and seven `log:roles: … is untyped` lines printed; the child under `CHILD_ARGS` in both modes matched base the same way, its one `type:` line read `type:unit:A-tB-1:-` and it logged `builder is untyped`.
- AC2 — `dispatch.args.roles` — under `ROLES` the `spec:` agents read `gov-spec-writer`, `commit:specs:tB` read `gov-x` and `dispose:tB` read `gov-spec-writer`, while `audit:subjects:r1` and `audit:record:r1` read `-`; the spec and disposal prompts carried the stamp and lacked `stalls for hours`, `DO NOT WRITE PRODUCT CODE`, `real probe rather than a claim` and `the whole reason that join exists`, kept the rejoined `order` sentence, `Name every unit in` and the `edges` request; the audit's `wfroles:` read the three review roles beside `"workerType":"none"`; the RESULT carried `"roles":{"builder":"gov-builder"}`, no `roles` key with `ROLES` minus `builder`, and `wfroles:-` with the audit keys left out.
- AC3 — `unattended-build:` — `[]`, `"gov-x"`, `{"specwriter":"gov-x"}`, `{"disposal":"bad name"}`, `{"committer":"none"}` and `null` each threw a message opening `unattended-build:` and naming `roles` or the key, with no `agent:` line; the child threw one opening `unattended-unit:` on `{"specWriter":"gov-x"}` naming `specWriter`, on `{"builder":"x y"}` and on `{"builder":"none"}`, with no `agent:` line.
- AC4 — `DIVERGENCE:` — the typed child's one `type:` line read `type:unit:A-tB-1:gov-builder`, its prompt carried the stamp, `a why that opens DIVERGENCE:` and `changes nothing else in the spec`, and lacked `CHANGE THE SPEC FIRST` and `or to WONTDO with a reason`; a `unit:` double returning a `DIVERGENCE:` why gave `"diverged":true`, and one returning `tests red` gave `"diverged":false`.
- AC5 — `AGENT_TYPE_SHAPE` — after `--render`, `--check` exited 0, `node tools/workflows/check-workflow-syntax.js` exited 0 with 7 scripts parsed clean, and `grep -c AGENT_TYPE_SHAPE` read 2 over both the render and its template, with no `{{` on either line.
- AC6 — `unattended-unit.js` — `{0,63}` staged to `{0,64}` in its `AGENT_TYPE_SHAPE` exited 1 printing `agent-type shape DRIFT — tools/workflows/unattended-unit.js:146` beside the owner `tools/workflows/tier2-review.template.js`; the `a.workerType` test renamed to `w.workerType` in the template and its render alike exited 1 printing `DEAD PROBE — the owner tools/workflows/tier2-review.template.js yields no literal`; restored, it exited 0 printing `agent-type shape — 4 literal(s) in 4 file(s) agree with the owner`.
- AC7 — `dispatches every judge again` — under `ROLES` with the deferred double at `"durable":false` the RESULT's `exit` read `deferred-platform` and its `next` carried `dispatches every judge again` and lacked `reuses every lens`; at `"durable":true` with no `roles` the RESULT line equalled the base render's byte for byte. The double carried `"blockers":null` beside the spec's keys, as the review harness's every deferred return does: without it the harness's pre-existing returned-nothing refusal, unchanged since base, throws before the deferral is read.
