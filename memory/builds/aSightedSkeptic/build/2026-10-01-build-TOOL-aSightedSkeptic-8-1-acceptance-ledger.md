# TOOL-aSightedSkeptic-8 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-8

Every finding now keeps the key of the lens that dispatched it. Every return carries a findings
`ledger`, the `confirmedFindings` set in the shape of the next round's `priorFindings`, and an
`appendix` the harness renders and the synthesis copies. The arm readings come from the main loop's
one VERIFYING run of the tier2-review self-test at 149e89d6 (165 passed, 0 failed) and from the same
test file run against the BASE render at 9fdd0c18 in a frozen clone (56 passed, 109 failed). The
greps and the direct checks were re-run on the build's tip, whose `tools/` is byte-identical to
149e89d6. The round-1 fold (828a5ffa, rev-2) amended AC4 and AC5 and added their arms; those two
lines were re-read from the self-test at fe3c29fc (180 passed, 0 failed) and from the same test file
against the BASE render (56 passed, 124 failed).

**Evidences:** TOOL-aSightedSkeptic-8
- AC1 — `ledger: every finding carries its dispatching lens` — its three halves printed `ok`: "a
  complete run, five entries in id order", "an echo of bogus still yields seams" and "every lens
  file reused yields the same lenses". All three printed `FAIL` against the BASE render.
- AC2 — `ledger: the skeptic and synthesis lines name the lens` — its three halves printed `ok`:
  "every verify: finding line", "every CONFIRMED synth line, id pattern intact" and "the deferred
  path's log lines". All three printed `FAIL` against the BASE render.
- AC3 — `ledger: every verdict state reaches the ledger` — both halves printed `ok`, the first
  reading "refuted uncertain unverified unverified confirmed" and the second "the absent fields read
  null, a missing reason reads empty". Against the BASE render both printed `FAIL`, the first with no
  verdict list at all.
- AC4 — `ledger: confirmedFindings feeds the next round` — its three halves printed `ok`: "one entry
  per confirmed finding", "a rejected fix is replaced by the skeptic's note, at the binding grade"
  and "a round-2 run given it carries every ref and claim in every find: prompt". All three printed
  `FAIL` against the BASE render. The rev-2 pair, "an unsound fix with an empty note keeps the
  finder's fix, marked unsound" and the same with "a blank note", printed `ok` at fe3c29fc and
  `FAIL` against the BASE render; 828a5ffa's message records them RED under a staged break of the
  fixed render, since the code was already right.
- AC5 — `ledger: the appendix is rendered by the harness` — the arm is split in three, all `ok` at
  VERIFYING: "heading, eight columns, one row per finding, the refuted one included", "a pipe and a
  line break in a cell leave the row count unchanged", and "ledger: the appendix is handed to the
  synthesis verbatim". All three printed `FAIL` against the BASE render. The rev-2 arm "a U+2028 in
  a reason cell leaves the row count unchanged", whose reason also carries U+2029, NEL, VT, FF, 0x1C
  and 0x1E and which compares the `str.splitlines` split with the `\n` split, the cell reading
  `p q r s t u v w`,
  printed `ok` at fe3c29fc and `FAIL` against the BASE render, and 828a5ffa's message records it
  RED against the unfixed render.
- AC6 — `ledger: every exit path carries the ledger` — all six paths printed `ok`: every lens dead,
  no finding raised, every finding refuted, one skeptic batch dead, the synthesis dead, and complete.
  All six printed `FAIL` against the BASE render.
- AC7 — `python tools/lexicon/lexicon.py --suggest renderAppendix --as js.function` — printed a line
  opening `OK — renderAppendix leads with render`, and the same for `renderCell` printed
  `OK — renderCell leads with render`. `check-review-join.sh`, `check-verifier-fanout.sh` and
  `check-workflow-syntax.js` each exited 0, and the `sed` render of the cap 5 piped into `diff`
  against the render printed 0 lines.
- AC8 — `grep -c 'confirmedFindings' tools/workflows/README.md` — printed 1, and over the BASE file 0.
