# Brief — aPairedSlots: two non-doc gate bars at once, doc-only bars on their own key

**Serves:** research TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6

Handed to `/unattended` as the `--prompt` value on 2026-10-11, node `a`. The value carried whitespace
and named no readable file, so by the Skill's routing table it is the prompt itself, taken verbatim
below. It names no tracked id of this repo as a mandate: `TOOL-aFrugalTurnstile-5` is cited as the
turnstile to build on, not as an ask to close.

## The prompt

```text
Let two NON-DOC gate bars run at once on one repository, instead of strictly one. DOC-ONLY bars should be freely admitted with their own key. Repo: C:/projects/coding-governance (gov), node a. Owner-requested on 2026-10-11.

Why. The run-gates turnstile admits ONE bar per repository; every other bar queues behind it. On 2026-10-11 a docs-only scoped landing bar (aBenchedProbe follow-up) sat at queue position 1 for over 30 minutes behind an unrelated full bar from another worktree, with a third bar queued behind it. With several unattended runs landing per day, the queue, not the legs, is now the dominant cost of a landing. The owner wants two bars admitted concurrently.

The concurrent run aFrugalTurnstile (branch origin/branch/awesome-cannon-44b2b1, 37 commits ahead of origin/main d22cca6c at 7f3940a0d) rewrites the turnstile in its unit TOOL-aFrugalTurnstile-5: the turnstile becomes HOST-WIDE, names its holder, lets nested bars through, and --hold admits a foreign bar. Build on that turnstile, never on the one it replaces. If aFrugalTurnstile has landed when this run starts, start from origin/main. If it has not, coordinate with its session and/or build from its worktree.
The measured objection this run must answer first. The turnstile header in tools/run-gates/run-gates.sh records why it serializes: three full bars at once measured CPU at 39 %, both queues empty, and width 24 ran 26 % SLOWER than width 8 — "the contended resource does not parallelise, so two concurrent bars are worse than two sequential ones". Do not argue with that; re-measure it. Before any code (build method M12, researched and solution-tested):
The metric is the one the owner named: when two non-doc bars start together, the time until BOTH are green (makespan), and each bar's own wall. Compare (A) today: two bars serialized, each at the profile's full width, against (B) two bars concurrent, each at half the width. Also try (C) two concurrent at full width each, since the earlier measurement was three bars, not two.
Run each arm at least twice on node a, on frozen clones under a short %TEMP% root (memory notes run-long-suites-on-a-frozen-clone, clone-into-scratchpad-hits-max-path), with no other bar running, and record the host's other load. Each arm must prove it ran its legs (ab-arm-must-prove-it-ran): assert a leg count per bar, not just an exit code. Never wrap a bar or the lander in timeout (never-wrap-the-lander-in-timeout); wait on pids with a monitor.
Commit the instrument and the result rows under this build's build/ folder.

The decision rule, so nobody has to be asked. Ship the capability either way, as a declared knob: a per-row slots=<n> in tools/run-gates/gate-profiles.txt (kit default 1), overridable by GATE_TURNSTILE_SLOTS. Set node a's row to 2 only if arm B's or arm C's makespan is no worse than arm A's in both repetitions; record which arm and its width rule. Otherwise land at 1 (dark), and record the numbers and the reason in the build README, so an owner can flip it.

What must change, and what must not:

* The turnstile becomes a counting semaphore of slots holders: one beacon directory per slot, each with its own pid, nonce and heartbeat, the stale-holder reap and the nonce-guarded release per slot, the queue order unchanged. With slots=1 the observable behaviour, stdout lines included, is byte-identical to today.
* Width: when more than one slot is held, a bar's pool width follows the decision rule above (half width for arm B), resolved once at dispatch and printed on the profile line. mempause already reads host memory, so two bars share its pause; confirm it, do not add a second one.
* Audit every path two concurrent bars on ONE repository both write, and make each safe or per-bar: the common dir's gate-ledger.tsv, runlog/gates.log, health.log, drift-history.tsv, gate-full-green.shared (one slot, last writer wins), gate-queue-heartbeat, the gate-work.* TMPDIR sweep and its owner record, the process-monitor reap (a bar must never reap its sibling's legs), and any leg fixture that uses a fixed name under %TEMP% or the common dir. Run predicates over the real tree and print hits and near-misses before trusting the list.
* --print-profile gains slots; the unattended driver's backstop (queue term TS_MAXWAIT plus the wall) must stay correct with two holders.
* Do not touch the scoped/full staleness rules, the lineage reuse, post-merge.sh or the push boundary; those are aFrugalTurnstile's.


Acceptance, each observed RED before GREEN on a staged break:

* tools/run-gates/run-gates.turnstile.test.sh: with slots=2 two bars hold at once and a third queues; a stalled slot is reaped while the other holder keeps running; a release cannot free another slot's beacon; with slots=1 the arms that exist today pass unchanged.
* Two real concurrent bars on two worktrees of one repo produce the same leg verdicts as the same two bars run serially, and neither's ledger row, run-log line or run record is lost or interleaved.
* The A/B numbers are committed, and node a's slots value follows the decision rule.


Gates: bash tools/run-gates/run-gates.sh at the close, the run-gates canary and turnstile suites sliced in passes, kit version markers, govkit epoch. Bump run-gates once, after the last move, and re-stamp the kickoff manifest because run-gates.sh and gate-profiles.txt are watched. Run python tools/codebase-map/gen_map.py --write after any new function, and refresh memory/map/features/run-gates.md before the close (it is near its 20480-byte cap; split it if needed rather than overflow it).
When the build LANDS or stops, say so in the wrap-up with the gov head sha, the node a slots value it landed with, and the A/B makespans behind it.
```

## The brief

### Goal
Admit two non-doc gate bars at once where a measurement on node a shows it pays, and admit doc-only
bars freely on a key of their own, on top of aFrugalTurnstile's host-wide turnstile.

### Items
1. Re-measure the serialization claim before any code: arms A (two serial bars at full width), B (two concurrent at half width) and C (two concurrent at full width), each at least twice on frozen clones on a quiet node a, each bar asserted to have run its legs, the instrument and rows committed under `build/`. [planned TOOL-aPairedSlots-1]
2. A declared `slots=<n>` key on each `gate-profiles.txt` row, kit default 1, overridable by `GATE_TURNSTILE_SLOTS`, printed by `--print-profile`, and node a's row set to 2 only when arm B or C is no worse than arm A in both repetitions. [planned TOOL-aPairedSlots-1]
3. The turnstile becomes a counting semaphore of `slots` holders, one beacon directory per slot with its own pid, nonce and heartbeat, reaped and released per slot, queue order unchanged, and byte-identical at `slots=1`. [planned TOOL-aPairedSlots-2]
4. A bar dispatched while more than one slot is held takes the width the A/B chose, resolved once and printed on the profile line; mempause is confirmed shared, not duplicated. [planned TOOL-aPairedSlots-3]
5. Doc-only bars take their own turnstile key and are admitted without a cap. [planned TOOL-aPairedSlots-4]
6. Every path two concurrent bars on one repository both write is audited by a predicate over the real tree and made safe or per-bar. [planned TOOL-aPairedSlots-5]
7. The unattended driver's backstop, the queue term plus the wall, stays correct with two holders. [planned TOOL-aPairedSlots-6]

### Acceptance
- `run-gates.turnstile.test.sh`, sliced: at `slots=2` two bars hold at once and a third queues; a stalled slot is reaped while the other holder runs; a release cannot free another slot's beacon; at `slots=1` today's arms pass unchanged. Each arm observed RED on a staged break first.
- Two real concurrent bars on two worktrees of one repository give the same leg verdicts as the same two bars run serially, and neither's ledger row, run-log line or run record is lost or interleaved.
- The A/B rows are committed, and node a's `slots` value follows the decision rule.

### Gates
`bash tools/run-gates/run-gates.sh` at the close; the run-gates canary and turnstile suites sliced in passes; kit version markers; govkit epoch; the codebase-map freshness leg after `gen_map.py --write`.

### Non-goals
The scoped and full staleness rules, lineage reuse, `post-merge.sh` and the push boundary, all aFrugalTurnstile's. A second memory pause. A cap on doc-only bars.

### Limitations
Build on TOOL-aFrugalTurnstile-5's turnstile, never the one it replaced. Never wrap a bar or the lander in `timeout`; wait on pids. No merge bar or self-test suite inside a pass. Frozen clones under a short `%TEMP%` root. Bump run-gates once after the last move, re-stamp the kickoff manifest, refresh the run-gates dossier under its 20480-byte cap, splitting it if needed.

### Reuse
The seam is aFrugalTurnstile's turnstile in `tools/run-gates/run-gates.sh`, its `ts_*` functions, `--hold` and the beacon fields, plus the profile-row parse, `--print-profile` and the unattended kit's `parse_gate_profile`. `reuse_lookup.py` found no counting-semaphore seam. Recall qid 921 returned TOOL-aReapedTicket-4, the two-waiter reap race that a per-slot reap must not widen, and the three-bar measurement in TOOL-aMeteredTurnstile-6 and TOOL-aUnblockedFleet-6 that this build re-measures.

## Drawn from the session

> Own key, unbounded (Recommended)
— owner, 2026-10-11 ~04:30 +0300, answering how many doc-only bars may hold their key at once

> Hold per arm-run (Recommended)
— owner, 2026-10-11 ~04:30 +0300, answering whether the A/B may hold the host turnstile per arm-run

## Owner confirmation

Asked: A doc-only bar (one the pre-push hook runs with GATE_DOCS_BASE set) gets its own turnstile key, so it never waits behind a non-doc bar. How many doc-only bars may hold that key at once?
Answer: Own key, unbounded (Recommended)

Asked: Each A/B arm needs a quiet host, and the owner prompt asks for 'no other bar running'. To get that, the instrument waits for any foreign bar to finish, then holds the host turnstile (aFrugalTurnstile's --hold) for the arm. That's 6 arm-runs of roughly 1–2.5 h each, about 9 h in total. Other sessions' bars queue during each arm, and fail open after the 2 h queue bound. Is that acceptable?
Answer: Hold per arm-run (Recommended)

The one owner turn carried these two gap questions and not the brief text itself; the brief above
quotes both answers verbatim and paraphrases nothing else from the session.
