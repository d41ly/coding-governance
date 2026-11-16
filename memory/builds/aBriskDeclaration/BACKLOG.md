# aBriskDeclaration — asks

## Asks

- TOOL-aBriskDeclaration-2 · filed 2026-11-14 · THE RESOLVER REFUSAL'S PIN OUTLIVED ITS REASON. Arm A5 of `TOOL-aBriskDeclaration-1` now drives `--dispatch`'s no-usable-python refusal from the suite's fixture by overriding `resolve_python` in a subshell, the method the sidecar pin row `unattended.sh 49 15` says cannot be used. A5 quotes the refusal without its `--dispatch: ` prefix, so `check-arms.py` neither arms the branch nor reports the arm as stranded, and the pin stays in force with a false reason. The closing review's M1, `memory/builds/aBriskDeclaration/reviews/2026-11-14-review-TOOL-aBriskDeclaration-1-closing-diff-round1.md`. · seen `tools/unattended/unarmed-branches.txt` matching `inline resolver found no usable python` run `python tools/memory-tree/check-arms.py --check` · accept A5 asserts the refusal's whole signature, `check-arms.py --check` grades the branch ARMED, and the pin row is removed in the same commit
- TOOL-aBriskDeclaration-3 · filed 2026-11-14 · THE OLD ORDER STILL STATED ONE SENTENCE UP. The verbs guide's `--dispatch` paragraph, in both copies, still opens "After every cheap refusal and before the claim read it runs the DECLARED spec-token checker", two lines above the sentence `TOOL-aBriskDeclaration-1` added saying the checker is started before the open-pass reader, and the arm header above the aSwiftRefusal-1 group still says the checker runs after every cheap refusal. The closing review's L1. · seen `memory/guides/UNATTENDED-VERBS.md` matching `After every cheap refusal and before the claim read it runs` run `grep -c` · accept that sentence reads the new order in `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, byte-equal past line 1, and the suite's arm header says the same
- TOOL-aBriskDeclaration-4 · filed 2026-11-14 · NO PLANT FOR AN UNTERMINATED LAST LINE. `order_verb_of`'s read loop sees a final line with no newline only through its `|| [ -n "$line" ]` clause, and none of arm A1's ten plants ends without a newline, so deleting the clause leaves the suite green. The closing review's L2. · seen `tools/unattended/unattended.test.sh` matching `brisk A1: the order verb is read with no process` run `bash tools/unattended/unattended.test.sh --shard 3/8` · accept A1 carries an eleventh plant whose header is the file's last line with no newline, and the arm reds with the clause deleted

## Dispositions

- SEV · TOOL-aBriskDeclaration-2 · MED · a misleading registry row and an unlinked arm; no verdict changes
- SEV · TOOL-aBriskDeclaration-3 · LOW · prose only; the code and the sentence added below it state the new order
- SEV · TOOL-aBriskDeclaration-4 · LOW · a missing test; a real spec carries its header near the top with body text after it
- KEEP · TOOL-aBriskDeclaration-2 · build method M8 fixes blockers only, and the review found none
- KEEP · TOOL-aBriskDeclaration-3 · build method M8 fixes blockers only, and the review found none
- KEEP · TOOL-aBriskDeclaration-4 · build method M8 fixes blockers only, and the review found none
