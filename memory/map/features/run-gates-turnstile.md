# run-gates-turnstile — how many gate bars a host admits, and what two concurrent bars share

```toml
feature = "run-gates-turnstile"
title = "The host turnstile: the slots that admit gate bars, the docs key beside them, and the files two concurrent bars share"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aFrugalTurnstile-5", "TOOL-aPairedSlots-1", "TOOL-aPairedSlots-2",
  "TOOL-aPairedSlots-3", "TOOL-aPairedSlots-4", "TOOL-aPairedSlots-5", "TOOL-aPairedSlots-6",
  "TOOL-aPairedSlots-7", "TOOL-aPairedSlots-9", "TOOL-dDerivedDocket-64"]

[claims]
gate-legs = ["run-gates turnstile"]
kits = []
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["record-file-read-by-line-position.md", "overlap-judged-from-the-invocation-interval.md",
  "predicate-bounded-by-its-own-count.md", "invariant-held-on-one-admission-path.md",
  "floor-left-below-the-arms-it-guards.md", "allocation-knob-without-a-ceiling.md",
  "beacon-published-before-it-is-complete.md"]
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/run-gates/run-gates.sh",
  "tools/run-gates/gate-profiles.txt",
  "tools/run-gates/run-gates.turnstile.test.sh",
]
```

The turnstile lives inside `tools/run-gates/run-gates.sh`, which the run-gates dossier owns. Its rules
are kept here, so that neither dossier outgrows its cap.

## Constraints & why

**A host admits `slots` non-doc bars at once, and one by default.** The turnstile is a counting
semaphore. Slot 1 is `gate-bar-beacon` under the host's turnstile directory and slot k is
`gate-bar-beacon.<k>`, each with its own pid, nonce, heartbeat and repo file. The stale reap and the
nonce-guarded release act per slot, so neither can free another holder's beacon. The queue stays one
FIFO, and only its head claims, taking the lowest free slot. The count is the profile row's
`slots=<n>`, 1 to 64, overridden by `GATE_TURNSTILE_SLOTS`. With one slot the runner prints exactly the lines it
printed before the semaphore existed. `TOOL-aPairedSlots-1`, `TOOL-aPairedSlots-2`.

**The kit ships one slot.** The two-bar measurement behind the `capable` row found no arm where two
concurrent bars finished as soon as two sequential ones, so that row carries no `slots` key. The
numbers, and how to re-measure before turning two slots on, are `TOOL-aPairedSlots-9`'s results
record.

**A second holder's width is decided once, at dispatch.** When more than one slot is held as a bar
dispatches, `TS_SHARE_RULE` (`full` or `half`) sets its pool width, an explicit `GATE_JOBS` wins, and a
`gate profile: width` line says which applied. Memory pressure needs no second rule: `mempause` reads
host memory, so concurrent bars already share its pause. `TOOL-aPairedSlots-3`.

**A docs-only bar never queues.** Under `GATE_DOCS_BASE` a bar takes its own key,
`gate-docs-beacon/<run id>`, unbounded by the owner's ruling, and its run record reads
`queued_from docs`. Nesting reads every slot beacon and every docs beacon, so a bar started inside
any holder passes through. It waits only for a holder in its own worktree, never another's.
`TOOL-aPairedSlots-4`, `TOOL-aPairedSlots-15`.

**A worktree holds one bar at a time.** A bar does not claim while any holder present names its own
top level, a slot at any count or a docs beacon, so everything under one worktree's git dir stays one
bar's: its ledger, run records, gate logs and green stamps. Only the common dir is shared.
`TOOL-aPairedSlots-5`, whose audit record lists every path two bars of one repository write.

**The common dir takes a second writer.** The run-log line is appended through `cat`, one write per
line, because the `printf` builtin's own redirection tears a long line under MSYS. The shared full
green is staged under a per-process name, and the last writer wins. Drift-audit's history header is
written only by the writer whose exclusive create made the file. `TOOL-aPairedSlots-7`.

**A waiting bar beats.** On every tick it waits, the turnstile rewrites `gate-queue-heartbeat` under
its own worktree's git dir, beside `gate-logs/`, and never removes it, so an out-of-process liveness
reader sees a queued bar move before its first leg lands; the unattended driver's clock reads its
mtime. `TOOL-dDerivedDocket-64`.

## Shared seams

**The profile row.** `slots` is a knob in `gate-profiles.txt` beside `width` and `mempause`, read by
the runner's one profile parser. `--print-profile` prints it, and the unattended driver's backstop
reads that output rather than parsing the table again (`TOOL-aPairedSlots-6`).

## Reuse affordance

seam: `GATE_TURNSTILE_DIR` — reuse whenever a harness must run real bars against a private turnstile;
extend by pointing it at a fixture directory, never by adding a second lock.

## Gaps

- Two slots have not been measured on a host with a healthy kernel pool: the `capable` row's verdict
  rests on one repetition per arm.
- The health log's trim can drop a line a concurrent bar appends, filed as `TOOL-aPairedSlots-10`.
