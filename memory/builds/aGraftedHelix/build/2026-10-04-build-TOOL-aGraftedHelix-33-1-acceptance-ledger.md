# Acceptance ledger — TOOL-aGraftedHelix-33

**Serves:** journal TOOL-aGraftedHelix-33

Node `a`, 2026-10-06. The build commit is `4b21bbd7`, over the pass's parent `843d5c0b`, the spec's
rev-2 commit, which restated AC1's red after the staged break printed something other than the
pre-S3 tree's output. No merge bar and no self-test suite ran in this pass. AC1 to AC6 ran as a slice
generated into the session scratchpad, `gh33-slice.sh`: the build-harness suite's prologue with its
kit dir pinned, the `N_UNITS` fixture line, and the GH33 block, 41 assertions, green at `4b21bbd7`.
Each staged break was a scratch copy of the render beside the slice, read through the slice's
`GH33_F` override, so the shipped render was never edited. Two more slices covered the arms whose
doubles this unit changed: the sliced spec fan block with the attended AC14 arms and the engine pin
(33, green), and the GH15 spec commit block (157, green). The whole suite, and the bar, are the main
loop's, at VERIFYING.

**Evidences:** TOOL-aGraftedHelix-33
- AC1 — `agent:commit:specs:tB` — the slice counted one commit stage, whose prompt carried `spec(tB): A-tB-1 A-tB-2 A-tB-3 A-tB-4`, the log `committed 4 spec(s)`, three `resolved by path` lines and no empty `specPath`; with the merge's resolver call bypassed in a render copy, 32 assertions failed, the commit line naming the raw paths beside `A-tB-1` and the run throwing `named no committed spec`, as rev-2 states.
- AC2 — `THROW` — the five-spelling run printed no `THROW` line and its commit line named `A-tB-1` to `A-tB-5`; each of four render copies failed two to four assertions, the backslash fold removed refusing group 0's entry, the drive fold removed refusing group 1's, the second arm removed refusing `A-tB-5`'s caller path, and the third arm narrowed to `-spec-<id>.md` refusing groups 2 and 3 in one throw.
- AC3 — `names no roster unit by id and no unit's spec by path` — all seven entries, from `A-tB-9` to the basename routing to both `A-tB-1` and `B-tB-1`, ended in a `THROW` carrying the phrase and the entry as JSON with no `agent:commit:` line; with the throw deleted in a render copy 14 assertions failed and the `A-tB-9` run reached `RESULT` after `no commit — the writers authored no unit of this roster`.
- AC4 — `the spec whose H1 defines` — the run threw naming `A-tB-2`, the entry, both paths and the commit sha beside `Refusing before any audit or hand-out reads a spec`, and printed no `"roster"`; with the H1 agreement test deleted in a render copy it reached `RESULT` with `2026-10-05-spec-A-tB-2-other.md` on the roster row of `A-tB-2`.
- AC5 — `the caller's path differs` — the absolute pair printed no `THROW`, the roster row of `A-tB-1` carried the repo-relative `specPath`, and no log line carried the phrase; the commit return read unfolded threw `named a path outside`, and the fill comparing raw strings logged the phrase.
- AC6 — `by its unit id` — the attended `planState` `MISSING` fixture with pinned `subjects`, its writer returning the caller `specPath` in `authored`, reached `RESULT`, logged `A-tB-1` as left to the caller to commit, and its one `prompt:spec:tB:` line carried the sentence; with the resolution moved to `authoredIds` the plan-state refusal named `A-tB-1`, and with the sentence deleted the two prompt counts read 0.
- AC7 — `git status --porcelain tools/workflows/` — printed nothing at `4b21bbd7` after `--render`; `node tools/workflows/check-workflow-syntax.js` printed `6 workflow script(s) parsed clean`; `grep -c "items: SPEC_ENTRY" tools/workflows/unattended-build.js` printed `3`; the `const SPEC_ENTRY` line carries `enum:`; the `"authored":["x"]` count in the suite is 0; and the kit README carries the refusal phrase once.
- AC8 — `bash tools/check-kit-versions.sh` — printed `kit-versions: clean — 16 declared carrier(s) under tools/`; `python tools/govkit/govkit.py epoch --base <the pass's parent sha>`, run as `--base 843d5c0b3`, printed `epoch: review-harness · clean · 1.39`; line 3 of `tools/workflows/unattended-build.js` moved from `1.9` at `843d5c0b` to `1.10`.
