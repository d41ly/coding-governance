# The candidate predicate, run over this node's REAL process table — hits and near-misses

**Serves:** research TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3

Node `a`, 2026-09-08. The charter's §7 rule: *run a candidate gate predicate over the real tree
before wiring it, and print hits AND near-misses.* Two probes, both throwaway and in the scratchpad.
Four corrections came out of it, and three of them invalidate something a rev-1 spec asserts.

## The headline: it finds the owner's own reported orphans

```
pid 2315342  ppid 2315334  age 53.07h  cpu 67.9s  rate 0.00  ORPHAN  tail.exe -f .../tasks/bs9du47g1.output
pid 2335513  ppid 2335503  age 52.99h  cpu 99.9s  rate 0.00  ORPHAN  tail.exe -f .../tasks/bwgmo8y0j.output
```

Those are the sweep's *"five Monitor greps from 52–61 hours ago — parents long dead, still holding
pipes"*, still running, found by the candidate predicate with no hand-tuning. Their parents
(2315334, 2335503) are absent from the table.

## Correction 1 — `ps -W`'s COMMAND is the EXECUTABLE, not the command line

Probe 1 scoped on it and matched **zero of 315 rows**, in a tree that demonstrably holds agent
processes. `ps -W` prints `/usr/bin/sleep`, never `sleep 900`. Scope attribution must read CIM's
`CommandLine`, which carries the full string.

**Spec impact:** unit 1 §4 says `ps -W` supplies the identity and CIM supplies "cpu_s and the
precise creation time". CIM must also supply `command`. Unit 2 reads `command` and would have been
handed the executable path.

## Correction 2 — the ORPHAN label alone must never authorize a kill

Probe 1's unscoped run flagged **297 of 315 rows as over-ceiling AND ORPHAN**, including
`Windows Defender` (rate 0.79, 85.8 h), `lsass.exe`, `csrss.exe`, `svchost.exe`, Docker and
uTorrent. `ps -W` reports every non-MSYS Windows process with `ppid 0`, which the naive orphan
predicate reads as "parent is dead".

Worse in the other direction: this session's OWN freshly-spawned Bash-tool shells appear with
`ppid 0` or `ppid 1` at age 0.00 h, so a live, wanted process is ORPHAN-labelled the instant it
starts. **The age ceiling is the only thing separating those two populations**, which is exactly
unit 3's "age DECIDES, rate LABELS" — the design survives the measurement, but only because the
fence and the ceiling both run BEFORE the label is acted on. A `reap-orphans` mode reading the label
alone would have reaped `lsass.exe`.

**Spec impact:** unit 3 §4 says a `ppid` of 1 is treated as dead. It must say 0 OR 1, and it must
say that the label is meaningless outside the fenced, over-ceiling population.

## Correction 3 — PowerShell stdout is NOT UTF-8

`subprocess.run(..., text=True)` crashed on `0xe7` at byte 66732 of the CIM output — a CP1252 `ç`
in some process's command line — and the failure is not a caught exception, it is a
`UnicodeDecodeError` on a reader THREAD, after which `o.stdout` is `None`. Read bytes, decode with
`errors="replace"`.

**Spec impact:** unit 1 has no criterion for it. It is a real, reproducible, total failure of the
census on an ordinary desktop, and it needs its own arm.

## Correction 4 — 199 of 314 CIM rows carry a CommandLine; the rest are null

Protected and system processes return nothing. A row with no command line **cannot be attributed**,
so unit 2's F1 (refuse and COUNT) is right — and the count is not a nicety here, it is 115 of 314
rows on this node. A silent drop of a third of the table is the green-by-absence class.

## The near-misses, and the honest limit they expose

Unscoped MSYS rows the predicate did NOT catch:

```
pid 1991531  sleep.exe 27200          (7.5 h — almost certainly agent garbage)
pid  257797  tail.exe -f /tmp/revert-harness.txt
pid  263836  tail.exe -f /tmp/revert-harness.txt
pid  278495  tail.exe -f /tmp/revert-harness.txt
```

None names a declared root: `sleep 27200` names no path at all, and the `tail`s name `/tmp`. Their
parents are gone, so ANCESTRY attribution cannot reach them either — measured, ancestry added
exactly **one** row on this table (a `head` child of the probe itself).

**This is a real limit and it is stated rather than designed around: a process whose command line
names no declared root and whose ancestry is dead is UNATTRIBUTABLE.** Two dispositions, and the
build takes both: an adopter may declare additional roots (`/tmp` here would catch three of the
four), and the report must NAME the unattributable-MSYS-row count so the gap is visible instead of
being reported as a clean tree.

## What the numbers were

| Measurement | Value |
|---|---|
| `ps -W` rows | 313 |
| CIM rows | 314 |
| CIM rows carrying a CommandLine | 199 |
| MSYS rows (`ppid != 0`) | 10 |
| scoped by DIRECT command match | 7 |
| scoped once ANCESTRY is added | 8 |
| scoped AND over 1 h | 2 — both the 53 h `tail`s |

Every figure is from one run and will differ on the next; they are recorded as evidence that the
probe ran and what it saw, not as pins. The probe refused twice before producing any of them —
once when the CIM read returned nothing and once on the decode — which is the liveness assertion
working before it was ever specified.
