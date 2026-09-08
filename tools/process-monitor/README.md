# process-monitor — find, report and kill the processes an agent session forgot

<!-- gov:kit process-monitor@0.1 -->

Every deadline a repo like this owns bounds a command a CHECKER launched. Nothing bounds a process
an AGENT launched — a `Bash run_in_background` job, a `Monitor` pipeline, a suite invoked by hand —
and those are the majority of the processes an agent fleet creates.

One sweep on the machine this kit was built on found, live at once: two `until grep -q …; do :; done`
spin loops 11.4 hours old holding 46221 CPU-seconds between them, waiting on a file no writer was
left to make; nine copies of a test script where one was started; five `tail -f` processes 52 to 61
hours old whose parents were long dead, still holding pipes; and a gate runner still running 7.5
hours after it was stopped, with its children.

## What it does

**Census → fence → classify → reap.** Four stages, each its own module, each usable alone.

| stage | question | file |
|---|---|---|
| census | what is running, with what parents, age and CPU | `census.py` |
| fence | which of those are OURS | `scope.py` |
| classify | which of ours are dead weight, and why | `classify.py` |
| reap | kill a tree and PROVE each member died | `reap.py` |

Attribution is a property of the TREE, not of a row: a process is yours because its ancestry starts
at a path you declared, which is what makes a `sleep 900` with a bare argv reapable and an unrelated
editor invisible.

## Adopting it

```bash
cp -r <this kit> <your repo>/tools/process-monitor
cp tools/process-monitor/process-monitor.conf.template .process-monitor.conf   # then EDIT it
bash tools/process-monitor/adopt-process-monitor.sh
bash tools/process-monitor/adopt-process-monitor.sh --check
```

You declare `PROCMON_ROOTS` and nothing else is required. The conf carries the reason for every key
beside it.

## What this kit does NOT check

Stated because a structural check reads as a semantic one to everybody who did not write it, and
because a monitor that seems to cover more than it does is worse than one that covers less.

- **It does not know what a process is DOING.** It knows how old it is, how much CPU it has used,
  and whether its parent is gone. A process past its deadline doing useful work looks exactly like
  one that is stuck; only the declared ceiling separates them, and choosing that ceiling is yours.
- **It cannot attribute a process whose command line names no declared root AND whose ancestry is
  dead.** That population is real — on the build machine a 7.5-hour `sleep 27200` and three
  `tail -f /tmp/…` were unattributable — and the report NAMES the count rather than passing over
  it. Declare more roots, or accept that those are invisible.
- **It does not see a third of the process table's command lines.** On Windows, 199 of 314 rows
  reported a `CommandLine` at all; the rest are protected or system processes. Those cannot be
  roots. They can still be descendants of one.
- **"Parentless" is not "abandoned".** On Windows a parent exiting neither reparents its children
  nor clears the field, so `explorer.exe`, `csrss.exe` and every long-lived desktop process reads
  parentless. The SCOPE FENCE is the only thing separating those from a genuine orphan — which is
  why the fence runs before the classifier and why an over-broad `PROCMON_ROOTS` is the one
  misconfiguration that matters.
- **It does not verify that your declared roots are correct**, only that they are not obviously
  dangerous — not a filesystem root, not the system temp directory. A root naming somebody else's
  project is accepted.
- **The adopter's `--check` grades the DECLARATION, not the result.** Whether your roots actually
  admit your own work is a separate arm, because answering it needs a census and a closure.
- **It never restarts, reschedules or cleans up after anything it killed.**
- **The POSIX backend is unexercised on the machine this was built on.** MSYS `ps` rejects `-o`
  entirely, so that path is graded by captured fixtures only, and its arms say so.

## Why it is not simpler than it looks

Three things were measured on Windows and each one killed an obvious design:

- `kill -9 <top>` leaves the descendants alive. `taskkill /T` prints `SUCCESS` and killed one
  process of four, because it walks the WINDOWS process tree and MSYS parent edges are a different
  graph. A leaves-first walk of the right graph killed 5 of 5.
- A process the MSYS shell did not spawn cannot be signalled by MSYS `kill` at all — it answers
  `No such process` — and dies only to `taskkill /PID`. The predicate is not "native", it is "not
  an MSYS child", which is every orphan worth reaping.
- Every descendant of a test tree shared the CALLER's own process group, so a group kill reaps the
  session running the sweep.

The kit therefore keys on the Windows pid, carries both parent graphs, and chooses its signal per
row. None of that is defensive programming; each replaced something that measured false.
