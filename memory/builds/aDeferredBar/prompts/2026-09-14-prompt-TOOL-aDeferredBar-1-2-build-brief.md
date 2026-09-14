# Build brief — TOOL-aDeferredBar-1

**Serves:** journal TOOL-aDeferredBar-1

The pass this brief is handed to builds unit 1 of `aDeferredBar` at rev-3. The spec is
`memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-1.md` and it is authoritative;
this brief adds only what the spec cannot carry — what two audit rounds settled, so the pass does
not re-litigate them, and the rules the pass itself is bound by.

## What the pass builds

The instruction, at every carrier a build agent reads, changed at each carrier's SOURCE and
re-rendered: the child prompt (S1), the harness `GROUND` and its spec-writer prompt (S2), the
build method's M6 through its template (S3), the unattended Skill's "While it runs" bullet through
its template (S4), and the kickoff manifest's line-263 trap, re-stamped (S5). The spec's §4 files
table is the write set; declare it with `--dispatch` BEFORE the first edit, and re-declare WIDER
before the commit if a stamp carrier turns up that the table did not name.

## What the audits already decided, so the pass does not reopen it

- The M6 sentence is REPLACED, not appended to; the byte budget of M1 is not raised. `wc -c` and
  `wc -l` on the render are the observations (AC6), under 27648 bytes and 350 lines.
- Both manifest stamps move, `last-audit` and `last-body-change`, and the commit message carries a
  `manifest-audit: delta …` line (AC13). Half a stamp is the recorded gotcha; do both.
- The version pair on line 44 of `unattended-unit.js` and line 3 of `unattended-build.js` moves in
  BOTH tokens of the line; AC8 greps the whole line, so a half-moved marker reds.
- `GATE_(FULL|SELFTESTS)= prefix` and the other pinned forms in AC1 are grep ARGUMENTS with `grep`
  at command position; that is not a deny shape and unit 2's regex does not match them (AC16 probes
  it). Spell the child-prompt literal exactly as §4 pins it.
- The `memory hygiene` and `method carriers` legs are hand-run by their own scripts (AC15); nothing
  in this unit runs the bar.

## The rules this pass is bound by

- **No merge bar, no self-test suite, no `GATE_*=` prefix, no `run-selftests.sh`, no
  `run-unattended-gates.sh` in this pass.** Every criterion in §6 names a direct command; run those.
  Where a suite verdict is owed — none is, for this unit — it returns to the parent in `summary`.
- A watched kit file owes `last-audit` AND `last-body-change` AND the kit version in every carrier
  that spells it; the gate remedies name three of five. `bash tools/check-kit-versions.sh` and
  `bash tools/memory-tree/check-verdict-epoch.sh` are direct and cheap. If a stamp carrier reds that the files
  table does not name, re-declare the write set wider, then fix it.
- Author with Write/Edit, never a heredoc into a file: a backslash escape dies one layer in and the
  symptom never looks like quoting (six recorded instances).
- Commit ONCE at the end of the pass with the unit id in the subject; flip the spec's status header
  to CLOSED in that same commit; write the acceptance ledger under `build/` per `memory/HYGIENE.md`
  "Acceptance ledger" with one line per AC and `**Serves:** journal TOOL-aDeferredBar-1`.
- Then run `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names
  before returning.

## What the pass must not do

- No edit to `tools/unattended/PROTOCOL.template.md` or its render — unit 3 owns the protocol's
  next change and it sits near its cap.
- No edit to `tools/check-spec-tokens.py`, `.memory-tree.conf` or `SPEC-TEMPLATE.template.md` —
  unit 2 owns them, sequenced after this unit.
- No edit to `memory/DECISIONS.md` or `memory/backlog/*.md` — shared records, main-loop only.
- No widening of scope: a beneficial discovery goes in `summary` for the main loop to `--rescope`.
