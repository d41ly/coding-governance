**Serves:** research TOOL-dQuietDisk-1

# Owner instruction — the arm observations and the flagged bar run before this landing

## The prompt

> Run both

— owner, 2026-11-22, relayed by the session that started this run, answering its question: whether the owner opts in to
(a) the owed RED-then-GREEN observations of the build's `New arm:` lines over its kit suites and (b) the flagged bar
(`GATE_FULL=1 GATE_SELFTESTS=1`) before landing, or the run lands on the plain bar with both recorded as owed.

## How the run applies it

- Both run before the landing, on the lander's prepared merge, since `origin/main` moved past this branch's last merge.
- The flagged bar is the close's own bar: `--close` runs with `GATE_FULL=1 GATE_SELFTESTS=1` exported, so the kit
  Definition-of-Done item that owes it is met rather than overridden.
- Each `New arm:` line of a built unit is observed RED on its staged break and GREEN restored, in a scratch clone,
  and recorded as a seen-red line in a `Pass: none` commit. The lines in unattended-kit suites
  (`tools/unattended/check-pass-order.test.sh` of TOOL-dQuietDisk-2, `tools/unattended/check-brief-recorded.test.sh`
  of TOOL-dQuietDisk-3) stay unrun under the owner's standing rule of 2026-08-23, and are listed in the wrap-up as
  owed. WONTDO and DEFERRED units (6, 15, 17) owe none.
- The opt-in is for this landing only, never standing.
- The relayed message repeats the earlier condition: dQuietDisk lands only after dWitnessedBar's landing, which this
  branch carries, and on the remote's current tip, which the lander's prepare merges.
