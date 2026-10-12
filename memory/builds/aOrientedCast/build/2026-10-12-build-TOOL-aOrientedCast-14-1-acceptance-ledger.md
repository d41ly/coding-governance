# TOOL-aOrientedCast-14 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-14

Direct checks only: under the owner's rule for this run no gate, suite, slice or self-test ran in
this pass. What ran: a scratch probe that built a git repository holding a role index with `gates`
and a manifest, a second checkout holding no index, and two directories under no checkout, then
piped hand-built `Bash` payloads into `node tools/hooks/scratch-guard.js` and `Agent` payloads into
`node tools/hooks/agent-cap.js`, with `CLAUDE_PROJECT_DIR` removed from the child's environment and
set only where a row names one. Each payload ran twice: against this pass's hooks and against the
parent's (`git show HEAD:tools/hooks/…` into one scratch directory) as the RED. The parent admitted
eight of AC1's nine payloads and every AC3 and AC4 refusal, and printed no witness; this pass refuses
or witnesses each as the criterion states. AC1's `node -r <preload.js>` payload is refused by the
parent too, since its `--selftest` refuses whichever word heads, so that row pins the reading and is
not a RED. Owed to the main loop at the close (M8): the three `New arm:` lines of §7, each RED on its
staged break and GREEN restored, the `FLOOR_ASSERTIONS` raise to 309, and every leg §7 lists.

**Evidences:** TOOL-aOrientedCast-14
- AC1 — `gov-builder` — `bash -o pipefail <runner>`, `bash -O extglob <runner>`, `bash -e -c '<runner>'`, `env -u FOO bash <runner>`, `exec bash <runner>` and `nice -n 10 bash <runner>` exited 2 naming G2; `bash -e -x <suite>`, `python -X utf8 <selftest.py>` and `node -r <preload.js> <script> --selftest` exited 2 naming G3; the parent's hook exited 0 on all but the last.
- AC2 — `gov-builder` — `bash -n <suite>`, `bash -e -n <suite>`, `command -v <runner>`, `python -c "print(1)" <selftest.py>` and `node -e "1" <script> --selftest` each exited 0 with empty stderr; the parent's hook refused the `node -e` payload as G3.
- AC3 — `role-gate unarmed` — with the cwd under no checkout, `bash <runner>` exited 2 naming G2 when `CLAUDE_PROJECT_DIR` named the scratch repository, 0 with empty stderr when it was unset, and 0 with one stderr line carrying `role-gate unarmed` when it named a second directory under no checkout; a cwd in the index-less checkout with `CLAUDE_PROJECT_DIR` naming the repository exited 0 with empty stderr. The parent's hook exited 0 silent on all four.
- AC4 — `rule 6 unarmed` — an `Agent` payload of `subagent_type` `Explore` with its cwd under no checkout and `CLAUDE_PROJECT_DIR` naming the armed scratch repository exited 2 naming the type refusal; with the cwd in the index-less checkout it exited 0 with empty stderr; with both under no checkout it exited 0 with one stderr line carrying `rule 6 unarmed`. The parent's hook exited 0 silent on all three.
- AC5 — `grep -c 'unset CLAUDE_PROJECT_DIR' tools/hooks/agent-cap.test.sh` — printed 1, against 0 at the parent; `grep -c 'env -u CLAUDE_PROJECT_DIR' tools/hooks/scratch-guard.test.sh` printed 4, against 2 at the parent.
