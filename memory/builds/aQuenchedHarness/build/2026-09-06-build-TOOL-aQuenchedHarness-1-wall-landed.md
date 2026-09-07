# The whole-run wall — built, reviewed, six blockers folded, and one measurement retracted

**Serves:** journal TOOL-aQuenchedHarness-1

Node `a`, 2026-09-06. Evidence for `TOOL-aQuenchedHarness-1` §6 at rev-5. The first cut of this
record described a design that no longer exists; it was replaced rather than appended to, because
half of what it claimed was false.

## 1. The retraction, first, because it was reported to the owner as fact

This build told the owner the wall cost **+44 s per bar, a 6.4x regression**, from an interleaved
three-round A/B. **That number does not exist.** The A/B copied the NEW `gate-profiles.txt` into the
fixture and then swapped only `run-gates.sh` between HEAD and the working tree. HEAD does not carry
the `wall` knob, so its arm hit `prof_die` and **exited 2 in ~8 s having run zero legs** — and 8 s
read as a fast bar. Three rounds of a config refusal timed against three rounds of a real bar.

Re-measured with each arm carrying its OWN table, and every arm refused unless it printed
`gates GREEN`:

| round | old (HEAD) | new, wall on | new, wall off |
|---|---|---|---|
| 1 | 25679 ms | 22520 ms | 21952 ms |
| 2 | 25867 ms | 23026 ms | 26789 ms |
| 3 | 27082 ms | 29312 ms | 28347 ms |

No measurable difference. **The check that was owed is one `grep -q '^gates GREEN'` per arm**, and it
is now the first thing `ab-wall.sh` does.

An adversarial review put the real per-bar cost of the first implementation at +4.7 s quiet and
+12–16 s loaded. All of it was the startup probe, which §3 removes.

## 2. What the change is now

`tools/run-gates/run-gates.sh`: a `wall` profile knob with a `GATE_WALL` override; a watcher armed at
the FIRST DISPATCH, detached from job control; `scan_descendants` / `remove_descendants` walking one
`ps` snapshot; `arm_wall` / `remove_wall_watcher`; a per-leg `$WORK/<i>.pid` written by `runleg`; a
breach check at the reader-loop head; a breach verdict above every other exit path; and a sixth
precondition on the full-green stamp. `gate-profiles.txt` declares `wall=10800 / 14400 / 21600` with
its derivation. `KIT_RUN_GATES_VERSION` 1.4 → 1.5. Six arms in the canary, floor 132 → 139.

## 3. The six blockers, each measured rather than reasoned

**The startup liveness probe graded nothing, on every host.** It built its subject as
`( ( sleep 90 & ) ; sleep 90 ) &`, and bash exec-replaces a subshell's last command — so `$!` WAS the
sleep and had no children, and the intended grandchild was reparented to PID 1 before the snapshot.
The walk returned a one-element set every time, the survivor check saw only the pid it had just
SIGKILLed, `WALL_LIVE` was pinned at 1, and the INERT branch was unreachable. Reproduced 14/14 by
four independent reviewers. It also leaked one orphaned `sleep 90` per bar. **Deleted**, and the
assertion moved to the breach path, where a real tree exists: `remove_descendants` now reports by pid
what it could not reach.

**The wall bounded nothing once it had fired.** The breach check sat only at the outer loop head, and
the marker was written AFTER the kill loop — which runs one descendant walk per stuck leg, seconds to
tens of seconds wide. Measured: an 8 s wall, two wedged legs, and a third leg **started 57 s after the
breach** and ran to completion; 149 s against an 8 s bound. **The marker is now written before the
first kill.**

**The wall was not a clock.** It counted `sleep 1` iterations, and `sleep` is external: 20 nominal
seconds measured 32.9 s, 30 measured 58.0 s — 1.65x to 1.93x drift, entirely spawn cost. `wall=10800`
would have fired between 4h56m and 5h48m while the profile line printed 3 h. **Now an `EPOCHSECONDS`
deadline**, polled at a tenth of the wall, floored at 1 s and capped at 30 s: about ten spawns per run
whatever the wall is, and the overshoot stays proportional. A flat 30 s poll was tried first and made
an 8 s fixture wall fire at 30 s.

**A breach could write GREEN into the durable record, or exit 2 as a configuration refusal.** A killed
leg writes no `.rc`, so whether `fails` moves at all is a race — both outcomes were reproduced. The
run record now reads the MARKER, and the breach verdict is hoisted above the empty-population refusal
that was reporting a hang as operator error.

**A chunk the wall emptied reported `green`.** A killed leg increments none of the five chunk
counters. Observed: `---- chunk product: green (0 ran, 0 failed, 0 skipped, 0 reused, 0 held)` over a
chunk whose every leg had just been SIGKILLed. Now `killed`. This is `TOOL-dUnstalledConvoy-32`'s rule
reaching a newer kind of did-not-run.

**The kit version had not moved.** A runner below the bump reading a walled table hits `prof_die` and
exits 2 having run zero legs — every bar, not some. The precedent sits four lines below the constant
(`TOOL-dUnstalledConvoy-26`). 1.4 → 1.5, with the asymmetry written beside it.

## 4. Two more, smaller

The `ps` walk fed field 2 of an unvalidated text stream to `kill -9`; cygwin prints argv raw, and
snapshots on this box already carry about ten malformed continuation rows per capture from other
sessions' multi-line `bash -c`. Numeric guards added on both the ppid match and the pid.

The tracked arm was **red 3/3 on this box** for a property of the box: it bounded the control at 45 s
and compared raw wall clock, while a loaded bar spends 90–100 s in startup and teardown alone. Both
runs are now bounded at 300 s and the assertion is a 30 s MARGIN against a 112 s designed gap, so the
overhead cancels. That is the class `TOOL-aProvenReuse-6` and `TOOL-aScannedThrottle-7` both record.

## 5. Naming

A first cut named the four functions `wall_*` and moved `VERB_OFFENDER_PIN` by four. They are now
`scan_descendants`, `remove_descendants`, `arm_wall` and `remove_wall_watcher`, each leading with a
verb `.lexicon.conf` declares, checked with `--suggest` before being written. **The pin did not move.**
That is the §12 remedy — rename, not a new row — and unlike the `ts_*` pair earlier in this build
there was no existing family to stay consistent with, so the bump had no justification.

## 6. What is verified, and what is NOT

**Verified.** The wall fires and names the leg: `rc=1`, `gates RED — the 8s wall fired`,
`still running at the wall: slow leg`, with the runner alive to print it, and an unwalled control on
the same fixture running 155 s against the walled run's 30 s. `kit-versions`, `lexicon`,
`govkit selfcheck`, `memory hygiene --staged` and the charter size gate are all green.

**NOT verified, and this is the honest half.** `run-gates.test.sh` — the canary that carries the six
new arms — **has not been run since these fixes.** The last attempt ran 103 minutes against a 22-minute
recorded cost and was killed. A forensic review apportioned that: contention from up to sixteen
concurrent bars on this box was ~82% of it, the suite's own hard-capped clamp arms ~12%, and this
change **11 to 32 seconds** — because only 2 of the canary's 69 nested bars had reached the wall
before the kill, and 62 of the 69 run with the wall OFF anyway, since the suite copies only
`run-gates.sh` into most fixtures and not the profile table.

So the wall's tracked coverage is **7 of 69 bars**, not the whole suite, and saying so is the point:
the gate advertises more than it grades. Running the canary is owed, on a quiet box, and starting it
on a loaded one is the mistake that produced the 103 minutes.

## 7. What the wall is actually worth

Rev-1 through rev-4 of the spec said a wedged run's worst case is "the sum of every ceiling it can
reach" — 42.06 h across the 94 declared ceilings. **That overstates it by 4.6x.** At width 8 the
list-scheduling worst case is 9.16 h. The wall tightens 9.2 h to 3 h. Still worth having, and a
smaller claim than the spec was making.
