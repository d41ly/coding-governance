# Revision — aPiecewiseGrade: TOOL-aPiecewiseGrade-7 diverged at its builder

**Serves:** research TOOL-aPiecewiseGrade-7

## The brief

### Goal
DIVERGENCE: section 5, AC2 cannot hold as written. AC2 runs `sed -n '/# AC13: /,/each hold the lock/p' tools/unattended/unattended.test.sh` and requires that the output's last line end `foreign:1:w-x"`. At HEAD ad94c0603 the file has two lines that match `# AC13: `. The first is 8060 (`  # AC13: four live plants are held.`). The second is 16139 (`# AC13: each of S7's three conditions held false ALONE, ...`). sed closes the first range at the `same` line 8075, then reopens it at 16139. No later line holds `each hold the lock`, so the second range runs to the end of the file. Probed at HEAD, the command printed 4158 lines (DERIVED, wc -l at ad94c0603) and its last line was `exit "$st"`. Building the arm exactly as sections 2 and 4 say still leaves AC2 red. The only ways to make it pass both break the spec. One is to reword or move the line-16139 comment, which belongs to another unit's block and is outside the design. The other is to drop the `# AC13: ` opening from the line-8060 comment, which S2 forbids. What section 5 needs to say: AC2 has to name a range that closes, either by anchoring its start on text unique to the line-8060 comment (for example `/# AC13: .*live plants/`) or by adding `q` after the end match (`sed -n '/# AC13: /,/each hold the lock/{p;/each hold the lock/q}'`). Its "last line ends" clause then holds once the arm is built. I checked every other claim in the spec against HEAD and found no other divergence. The cited lines all hold: unattended.sh 2563 and 2573; unattended.test.sh 7545, 7774, 7976-7979, 8024-8027, 8060, 8063, 8075, 18117 and 20198 (`FLOOR_SHARD_3=451`, PINNED at ad94c0603). No other line in the file opens `foreign)`. The AC3 base 3300b594c is in history.

### Items
1. In `memory/builds/aPiecewiseGrade/spec/2026-11-16-spec-TOOL-aPiecewiseGrade-7.md`, rewrite AC2 so its `sed` range closes at the AC13 loop's own end, by one of the two forms the Goal names, and say which; verify the revised command against HEAD prints the loop alone. Nothing else in the spec moves unless the change makes a sentence false.
2. Bump its rev and add a revision-log line naming this record by its file stem.
3. Stage the spec and clear `python tools/check-spec-tokens.py --spec` over it. Do not commit. Return its path and status line, AC2's new text, and the checker's final line.

### Acceptance
- A lock whose recorded owner is a dead pid from another runtime reads as held, and the arm saying so reds when the runtime clause is deleted.

### Gates
`check-spec-tokens.py --spec` over the spec.

### Non-goals
- Any change to `tools/unattended/unattended.sh` or any other product file: the arm only.
- `tools/check-spec-tokens.py` and its suite, which TOOL-aPiecewiseGrade-8 writes.
- Any edit to a CLOSED spec.
- Building anything.
