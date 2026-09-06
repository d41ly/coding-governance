# The turnstile reaps a live holder, and that is where the six- and nine-hour stalls came from

**Serves:** research TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-8

Measured on node `a`, 2026-09-06, at base `faaea5f5`, while probing
`TOOL-aQuenchedHarness-2` §8 F1 — "what band does the ledger support". The probe answered its own
question with a NEGATIVE and then answered a bigger one nobody had asked.

## 1. What the probe was, and what it returned

F1's stated probe: for every leg with more than one recorded reading, the ratio between its slowest
and fastest recorded seconds is the load spread this bar actually shows. Its liveness assertion: a
ledger with fewer than two readings per leg produces NO band, and the probe says so.

**A single `gate-ledger.tsv` holds exactly one row per leg.** 96 lines, 96 distinct names, zero
duplicates. So against one ledger the probe returns the negative its liveness assertion anticipated,
and the band is underivable. That is a real answer and it is recorded rather than retried with
softer words.

**Twelve ledgers exist**, one per worktree plus the primary, and they are twelve independent readings
of the same legs on the same node under different load. Joining them gives the spread F1 wanted:

| statistic | value |
|---|---|
| legs with two or more readings | 93 of 101 |
| spread, median | 5.5x |
| spread, p75 | 9.0x |
| spread, p90 | 11.9x |
| spread, max | 47.1x (`pass-order history`, 37.9 s to 1788.7 s) |
| legs whose spread exceeds 10x | 18 |

`unattended kit gate` alone ranges 190.4 s to 3837.2 s across twelve readings — a 20.2x dilation of
one leg, on one node, from contention.

## 2. What that does to unit 2's premise, stated because it weakens it

The declared ceilings sit at roughly 10x the recorded seconds, and this repo's backlog has twice
described that as slack. **It is not slack.** 10x is between the p75 and the p90 of the observed
load spread, so a band much tighter than the current values would red healthy legs under exactly the
conditions this repo runs in — which is `TOOL-dRetiredFork-40`'s warning, now with a number under it.

Unit 2 remains worth building, because a ceiling with no measurement behind it is still unarguable
and an unbacked one is still invisible. But it is no longer the fix for the stall, and the spec must
stop implying that it is. That is a fold owed to `TOOL-aQuenchedHarness-2`.

## 3. The mechanism the spread pointed at

A 20x to 47x dilation needs concurrent bars. The turnstile exists to prevent exactly that, so either
it is being defeated or the dilation has another source. It is being defeated, and from source rather
than from inference:

- `ts_hb` is DEFINED at `tools/run-gates/run-gates.sh:444` and CALLED at exactly one site, `:1150`.
  The runner's own comment names that site: a leg COMPLETING.
- `TS_TTL` is `PROF_TIMEOUT * 3` when the selected profile row declares a per-leg timeout, else the
  fallback `1800`. Every shipped row in `tools/run-gates/gate-profiles.txt` declares `timeout=0`, so
  every real run uses `1800`.
- The reaper at `:472` deletes the beacon of a holder whose heartbeat is older than `TS_TTL`, calling
  it "a stalled holder".
- `unattended kit gate` is recorded at 3837.2 s. It is one leg. It exceeds 1800 s by more than a
  factor of two.

So on any bar that runs that leg, the holder goes more than `TS_TTL` without a leg completing, its
beacon is reaped as stalled, and the next bar acquires and runs UNQUEUED alongside it. The dilation
then lengthens every leg, which makes the next reap more likely, which is why the effect compounds
rather than averaging out.

**The runner already knows.** A `ponytail:` comment sits in the derivation block: *a single leg
longer than TS_TTL with no per-leg deadline configured is reaped mid-run.* It names the remedy as
setting `timeout=` on the profile row. That remedy has never been applied to any shipped row, and
the arithmetic says not to: the per-leg timeout would have to exceed the longest leg, which puts
`TS_TTL` at three times that and `TS_MAXWAIT` — a declared `TS_TTL * 4` — near thirteen hours.

## 4. The arithmetic of a nine-hour stall

None of it requires anything to hang.

1. A bar holds the beacon and enters a leg longer than 1800 s.
2. Its heartbeat goes stale. A second bar reaps it and runs concurrently.
3. Under that contention legs dilate by the measured 5.5x median and up to 47x.
4. A third bar queues, finds a live-looking holder, and waits out `TS_MAXWAIT` — `1800 * 4`, two
   hours — before failing open and running UNQUEUED as well.
5. Every leg is bounded, but at roughly 10x its recorded seconds, so nothing reds until hours in.

Two hours of queue plus a contended bar whose worst legs have dilated an order of magnitude reaches
six to nine hours without a single wedged process.

## 5. What this changes in the build

- **A unit was ADDED**, `TOOL-aQuenchedHarness-8`, by `--rescope --act add`. It makes the heartbeat a
  timer rather than a side effect of finishing work, which is what the reaper's bound was always
  asking about.
- It takes `order 1`. Everything else in this build lowers the cost of the bar; this one stops the
  bar from multiplying itself, and the cost work is worth less while that is happening.
- **Unit 2 owes a fold**: its §1 and §8 F1 both read as though tightening ceilings were the remedy
  for the stall, and §2 of this record refutes that.

## 6. Liveness of this measurement, said plainly

The spread figures come from twelve files this session did not write, under load this session did not
control, so they are evidence about a busy node and not a controlled experiment. The MECHANISM in §3
does not depend on them: it is read from source and from one recorded leg duration, and it would hold
if every spread figure here were wrong. The spread is what made anyone look.

What is NOT observed: a live capture of two bars holding the beacon at once. The before/after fixture
`TOOL-aQuenchedHarness-8` §2 S6 requires is that observation, and it is owed by the unit rather than
claimed here.
