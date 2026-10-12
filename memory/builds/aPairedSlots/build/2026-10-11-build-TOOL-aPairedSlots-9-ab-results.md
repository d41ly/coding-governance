# The two-bar A/B — three arm-runs, and the slot count node a lands with

**Serves:** journal TOOL-aPairedSlots-9

Run on node a from 2026-10-11T06:26Z to 2026-10-11T23:14Z by
`2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh`, over two frozen clones of origin/main
`d19938f3` under `%TEMP%/pab`. Every bar is the default full bar with self-tests held: 65 legs it
must report. Each arm-run took the host turnstile with `--hold` first, so no other session's bar
started inside it, and both its bars nested under that hold. The rows, the host samples and the
arm-run log sit beside this record as `2026-10-11-build-TOOL-aPairedSlots-9-ab-results.tsv`,
`-ab-samples.tsv` and `-ab-plan.txt`. On A1's two bar rows the run record's verdict carried its end
time as a second field, so every column from `ok` on sits one place right: read them as 55 ok,
10 FAIL, 65 expected, proof `yes`.

## The makespans

| Arm-run | Bars | Start (UTC) | Makespan | Legs reported | How it ended |
|---|---|---|---|---|---|
| A1 | one after the other, width 8 each | 06:26:30 | **8440 s** (4202 + 4238) | 65 and 65 | Complete. Both bars RED on the same 10 legs, which fail at the frozen base. |
| B1 | at once, width 4 each | 16:35:43 | **more than 11162 s** | not proven | Stopped by hand at 19:41Z, past A1's makespan, by the owner's one-repetition ruling. |
| C1 | at once, width 8 each | 20:43:53 | **more than 8945 s** | not proven | Stopped by hand at 23:12:56Z, past A1's makespan. |

An earlier B1 launch is void and decides nothing: its hold waited out the two-hour queue bound
behind another session's bar and failed open without a holder nonce, so its two bars did not nest
and ran one after the other. Its rows carry rc 143.

B1's stop note records why it was slow: the unattended kit's gate leg ran for more than three hours
in both bars, against 2857 s and 2719 s in A1's two bars. C1 had a watcher meant to stop it at
A1's makespan. It passed that bound at 8492 s, but its process match found no pid, and it logged
the stop anyway. The bars were found running and stopped by hand 453 s later. Both bars' exits
were recorded at 9004 s and 9010 s.

## Host load, graded per arm-run

`foreign` is the number of `run-gates.sh` processes outside the A/B root at each sample, which
counts processes rather than bars, since one bar runs several. An arm-run is graded **clean** when
every sample in its window reads zero foreign processes, and **contaminated** otherwise.

| Arm-run | Samples | Foreign, mean / max | Bash processes, mean | Load, mean | CPU %, mean | Grade |
|---|---|---|---|---|---|---|
| A1 | 110 | 2.8 / 17 | 40 | 7.6 | 46.9 | contaminated |
| B1 | 58 | 12.1 / 26 | 84 | 3.7 | 27.9 | contaminated |
| C1 | 63 | 12.8 / 24 | 66 | 4.0 | 24.9 | contaminated |

All three are contaminated, and B1 and C1 ran beside four to five times A1's foreign load. That
weights the comparison against the concurrent arms. It does not reverse it: both concurrent
arm-runs averaged less CPU than A1, so they were not starved of CPU.

**The host was degraded throughout.** The kernel pools read 20178 MB paged and 6177 MB nonpaged at
2026-10-11T22:55Z, after 7.3 days of uptime with no reboot since 2026-10-04, and `/usr/bin/true`
cost 408 ms a spawn. The same leak measured 24.8 GB on 2026-10-11T00:49Z, before A1 began. With
CPU under half used, the contended resource was process creation, which a second bar cannot speed
up. A host with a healthy pool could answer differently.

## The decision

The rule is TOOL-aPairedSlots-9 §4's, at one repetition. A1 is proven at 8440 s.
`2026-10-11-build-TOOL-aPairedSlots-9-rule-check.py` recomputes both values from the rows file and
compares them with the tree.

- **F1, `slots`.** B1 is more than 11162 s and C1 more than 8945 s. Neither is at or below 8440 s,
  and finishing either could only raise it. The `capable` row carries no `slots` key, so node a
  lands at **1**, the turnstile serial as before.
- **F2, `TS_SHARE_RULE`.** Neither `B_1 < C_1` nor its opposite is shown, since both are lower
  bounds. The rule's other branch gives **`full`**, which the tree already carries. At one slot the
  runner never reads it.

To turn two slots on, add `slots=2` to the `capable` row of `tools/run-gates/gate-profiles.txt`, or
set `GATE_TURNSTILE_SLOTS=2` for one host or one bar. Re-measure on a freshly booted host first:
`init <root> <source-repo> <sha>`, then `plan <root> "A1 B1 C1"`, with the instrument above.
