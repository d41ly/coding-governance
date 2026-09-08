# process monitor — the only deadline in this repo that is not a checker's own

```toml
feature = "process-monitor"
title = "identify, report and kill the processes an agent session launched and forgot"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aReapedSpinner-8", "TOOL-aReapedSpinner-9", "TOOL-aReapedSpinner-10"]

[claims]
gate-legs = [
  "process-monitor wiring",
  "process-monitor census selftest",
  "process-monitor adopter selftest",
]
kits = ["process-monitor"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/process-monitor/**",
  ".process-monitor.conf",
]
```

## Constraints & why

Every other bound in this repo wraps a command a CHECKER launched — `run-gates` its legs,
`unattended` its `GATE_BOUND` commands, `run-selftests` its suites. Nothing bounded a process an
AGENT launched, and those are the majority a fleet creates: a `Bash run_in_background` job, a
`Monitor` pipeline, a suite invoked by hand. One sweep on node `a` found two spin loops 11.4 hours
old holding 46221 CPU-seconds, five `tail -f` at 52–61 hours with dead parents, and a gate runner
alive 7.5 hours after it was stopped.

**Four stages, four modules, one direction.** `census.py` reads the table; `scope.py` decides which
rows are ours; `classify.py` decides which of ours are dead weight; `reap.py` kills and proves it.
Each is usable alone, and the split is what lets the fence be gated separately from the kill.

**The census is keyed on `winpid` and carries BOTH parent graphs.** MSYS rows measured 19 of 337 on
this host, and the gate runner dispatches its legs as NATIVE processes, so a census keyed on the
MSYS id describes a twentieth of the population and structurally excludes what the kit exists to
reap. `kind` is decided by the `0x400000` bit `ps -W` sets on a PID for a process MSYS did not
spawn; without that discriminator every row grades `msys`, because `ps -W` reports a PID for all of
them.

**Attribution is a TREE CLOSURE, not a per-row predicate.** A `sleep 900` names nothing, a leg shell
carries a relative script path, and `pre-push` invokes the runner relatively — per-row attribution
refused every real tree. A row is ours because its ancestry starts at a declared root.

**Age DECIDES and the CPU rate only LABELS.** One CPU sample cannot separate a spin loop from honest
work; a declared deadline separates either from abandonment. Every failure in the opening sweep was
hours past any defensible ceiling.

## Shared seams

The signal is chosen per row and the choice is OPERATIONAL: whichever liveness probe answers decides.
Measured — a native process the shell did NOT spawn answers `No such process` to both the bash
builtin `kill` and `/usr/bin/kill`, and dies only to `taskkill /PID`; the same binary spawned BY the
shell dies to `kill`. The predicate is not nativeness, it is whether MSYS can address the row.

`taskkill`'s SINGLE-PID form is used and its `/T` form is banned. `/T` walks the WINDOWS tree, which
is a different graph from MSYS's, and it printed `SUCCESS` while killing one process of four. The kit
supplies its own walk, so it uses the form that measured correct.

`tools/run-gates/run-gates.sh` delegates its teardown reap here when the monitor is installed and
falls back to its own depth-8 walk when it is not, announcing which at profile time. That
conditional is what keeps the runner installable alone.

## Gaps

- **A process whose command line names no declared root AND whose ancestry is dead is
  UNATTRIBUTABLE.** Measured live: a 7.5-hour `sleep 27200` and three `tail -f /tmp/…`. The report
  names the count rather than passing over it, and an adopter may declare more roots, but the kit
  cannot reach them.
- **A large minority of rows report no command line at all** — protected and system processes. They
  cannot be roots; they can still be descendants of one. The share is a property of the machine and
  is derived at report time, never written down.
- **The POSIX backend is UNEXERCISED.** MSYS `ps` rejects `-o` outright, so that path is graded by
  captured fixtures only and its arms say so rather than implying coverage.
- **"Parentless" is not "abandoned" on Windows.** A parent exiting neither reparents its children nor
  clears the field, so `explorer.exe`, `csrss.exe` and every long-lived desktop process reads
  parentless — 24 of 337 rows, 18 of them over an hour old. Only the SCOPE FENCE separates those from
  a real orphan, which is why the fence runs before the classifier and why that ordering is a safety
  requirement rather than tidiness.
- **The kit's self-tests are withheld from adopters** (`project-owned` in `kit.toml`, `subject = kit`
  on their legs), per the 2026-08-23 owner ruling. An adopter who never edits the checkers has no job
  for them.

## Reuse affordance

seam: `scope.py derive_scope` — reuse the shape whenever a safety property is computed in one module
and consumed in another. It returns a MAPPING carrying a per-row `killable` flag, and `run_kill`
refuses a bare set outright rather than accepting the keys. That refusal exists because the flag WAS
silently discarded at both call sites once: the fence computed the answer correctly and the boundary
threw it away, making the caller's own session an acceptable kill target. Four of that build's
closing findings were the same shape — a property computed correctly and lost at a seam — so the
durable lesson is to make the boundary carry the property, and to refuse the flattened type at the
door rather than trusting each new caller to remember.
