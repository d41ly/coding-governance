# TOOL-aWokenSentinel-15 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-15

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite, and `unattended-build.test.sh` was not run whole. The pass verified with the direct checks
the spec's section 6 names: each new arm run ALONE through the suite's own `run_wf` runner, in a
scratchpad script carrying only the suite's preamble (the three assertion helpers, `run_wf`, the
`UNITS`, `SPEC_OK` and `DISPOSE_OK` fixtures, `review_out`, `rec`, `NOSUBJ`, `B40` and `T40`) and
the arms under observation, pointed by its third argument first at `git show
12513c25:tools/workflows/unattended-build.js` saved under the scratchpad and then at the render at
the tip; the greps of AC3 and AC4 over the tip and over the files at `12513c25`; the parity
checker's `--check`; and `check-workflow-syntax.js`. Those stand in for the `review-protocol
parity (kit vs dogfood)`, `workflow script syntax`, `verifier fan-out`, `memory hygiene`, `spec
tokens` and `install-prefix (shipped surface)` legs, which run once at the close. The template and
its render land in this one commit, rendered by `check-protocol-parity.test.sh --render`. No spec
fold was owed: the code is section 4's block verbatim inside the resolver branch, the schema pins
both fields at forty hex, and the header paragraph carries the limit sentence; the spec's rev stays
at 2. One dispatch note: the first `--dispatch` was refused on `memory/LIVE.md` as already declared
by unit 16's dispatch in this group, the same refusal every sibling pass since unit 8 met, so the
declaration was re-made without the two generated indexes, which this commit does not touch.

**Evidences:** TOOL-aWokenSentinel-15
- AC1 — `run_wf "$NOSUBJ"` with the stubbed resolver returning `[{path: "s3", blob: "$B40", tree: "$T40"}]` (two different 40-hex literals) over the render at `12513c25` printed `RESULT` and traced one `^workflow:` line, so the four arms read `FAIL ... output lacked 'THROW'`, `lacked 's3 HEAD 0123… tree fedc…'`, `lacked 'Commit the fold'` and `got '1' want '0'` — RED first; over the tip it printed `THROW unattended-build: 1 subject(s) differ between HEAD and the working tree ... s3 HEAD 0123456789abcdef0123456789abcdef01234567 tree fedcba9876543210fedcba9876543210fedcba98. Commit the fold, then re-invoke with the same arguments; an audit is pinned at bytes history holds.` and `grep -c '^workflow:'` printed `0`. OBSERVED.
- AC2 — the same invocation with `tree` equal to `blob` over the tip traced `^workflow:` once and its `wargs:` line carried `"subjects":[{"path":"s3","blob":"0123456789abcdef0123456789abcdef01234567"}]` with `grep -c '"tree"'` over that line printing `0`; over the render at `12513c25` the `wargs:` line carried the `tree` field through to the callee (`got '1' want '0'`) — RED first. OBSERVED.
- AC3 — `grep -c 'hash-object'` printed `3` over `tools/workflows/unattended-build.template.js` and `3` over `tools/workflows/unattended-build.js` at the tip (the schema comment, the header paragraph and the prompt sentence) and `0` over each at `12513c25`; `grep -c 'after the check passes'` printed `1` over each at the tip and `0` at base; `bash tools/workflows/check-protocol-parity.test.sh --check` exited 0 printing `in parity — 2 rendered pair(s) match their templates`. OBSERVED; the parity leg itself is observed at --close.
- AC4 — `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js` exited 0 printing `1 workflow script(s) parsed clean`; `grep -c 'Commit the fold' tools/workflows/unattended-build.test.sh` printed `2` and `grep -c '"tree"'` over the same file printed `5` at the tip, and `0` and `0` over the file at `12513c25`; `run_wf "$UNITS"` (supplied subjects, 7-hex blobs, no `tree`) over the tip traced `^workflow:` once, `^agent:audit:subjects` zero times, and its output carried neither `THROW` nor `Commit the fold`. The two pre-existing `NOSUBJ` arms (`B round 2 ...` and `R2-E ...`), widened to a 40-hex `blob` with an equal `tree`, read `ok` over the tip through the same runner. OBSERVED.
- AC5 — `run_wf "$NOSUBJ"` with the stubbed resolver returning `[{path: "s3", blob: "$B40"}]` and no `tree` over the tip printed `THROW unattended-build: resolved subject 0 does not carry a 40-hex blob and a 40-hex tree: {"path":"s3","blob":"0123…"}. The resolver returns both full object names or the pre-flight cannot compare them.` and did not carry `Commit the fold`; over the render at `12513c25` it printed `RESULT` and proceeded to the sub-workflow (`output lacked '40-hex tree'`) — RED first. OBSERVED.
- checkers — the three files were edited in place under their CRLF working-copy encoding and `git diff --stat` reports line-scoped hunks only (55, 55 and 34 lines), so no whole-file line-ending rewrite is staged. OBSERVED; the legs are observed at --close.
