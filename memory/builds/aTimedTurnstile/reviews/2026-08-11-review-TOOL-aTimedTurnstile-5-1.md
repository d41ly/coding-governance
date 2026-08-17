# Review aTimedTurnstile-1 — Tier-2 on TOOL-aTimedTurnstile-5, the merge bar's bounded worker pool

**Serves:** spec-audit TOOL-aTimedTurnstile-5

**Date:** 2026-08-11 · **Tier:** 2 · **Streams:** tooling · **Base:** `f638d8b` → `b1baf71`
**Targets:** `tools/run-gates.sh` (+142/−27) · `tools/run-gates.test.sh` (+110)
**Question asked:** does the bar still report exactly what it checks, now that 47 legs run through a
pool instead of a loop?
**Threat model (narrow, as commissioned):** this is a local pre-push gate runner, not a service. The
only threat that matters is a change that makes the bar say GREEN while checking less — a dropped
leg, a lost failure, a verdict that disagrees with the printed lines, or a knob that weakens the bar.

## 1. Verdict

**The concurrency itself held. Every confirmed defect is on the periphery — the width knob, the
timing cache, and the canary's own arms — and none of them can make a leg's failure disappear.**

Six lenses attacked the core invariants (result-file tearing, index misalignment between the manifest
and the dispatch ORDER line, the `(no result)` race, the drop-sentinel, a swallowed `mv`/`wait`, a
tally that disagrees with the printed lines) and **none of those attacks survived**. The write-then-
rename ordering is correct, reporting is driven off the manifest cursor while dispatch is driven off
the advisory order array so the two indices never have to agree, and the `(no result)` branch's
three-condition guard (dispatch exhausted + full `wait` + re-check) is the right shape for the race
it was built to close. `GATE_JOBS=1` byte-identity to the pre-change runner is the strongest single
piece of evidence in the unit and it is real.

What the review actually found is a **one-sided suite**: the canary was extended with seven arms and
**the single mechanism this diff restructured most — the guard/skip decision — is exercised by zero
of them** (F1). The guard decision moved out of the deleted `leg_if_changed` into a serial pre-pass
that materialises the literal string `skip` into `$WORK/<i>.rc`, and that same file is then overloaded
as the dispatch "already decided" marker and as the `GATE skip` selector. Three consumers, one
producer, **no arm**: neither the 4-leg fixture nor the 30-leg fixture declares a `guard` on any leg,
so a regression that writes the sentinel for a leg that IS in the diff would print `GATE skip`, exit
GREEN, and keep all seven arms green. That is precisely the green-while-checking-less shape the file's
own header (lines 11-14) says it exists to forbid, and it is the one finding I escalated above the
lens severity.

Second and third are the two arms that are **graded against the wrong thing**: arm 3c pins an absolute
5000 ms wall clock while the canary is now itself one of eight concurrently-running legs (F3 — three
independent lenses measured it, one observed an outright 7286 ms trip), and arm 3g asserts only the
ABSENCE of `(no result)`, so a broken fixture passes it silently (F4). Fourth is the width knob: an
all-digit `GATE_JOBS` above int64 escapes a `test -lt` clamp and the runner **spins forever having
executed zero legs and printed no verdict** (F2 — reproduced independently in this write-up: exit 124
under `timeout`, 0 stdout lines, 115 stderr lines). Narrow trigger, but it directly contradicts the
invariant its own comment at `run-gates.sh:30` asserts.

Net: **land it.** The pool is sound and the wall-clock win (335s → 90s) is real. F1 should land with
it — it is a fixture edit plus two asserts, and it is the arm that makes every future edit to the skip
path honest.

## 2. Review shape

| raw | confirmed | refuted | unverified | precision | lenses |
|-----|-----------|---------|------------|-----------|--------|
| 16  | 11        | 5       | 0          | **0.69**  | 5/5 live |

Precision 0.69 sits comfortably above the ~0.5 floor named in `parallel-coding-governance.template.md`
§8. The 11 confirmed findings collapse to **6 distinct defects** — three clusters had two or three
lenses land independently on the same line, which is worth recording as signal rather than noise: the
`GATE_JOBS` clamp (2 lenses), the arm-3c timing pin (3 lenses), and the guard-path coverage hole
(2 lenses, one by construction and one by mutation). Convergence is why F1 and F3 are ranked where
they are.

The five refutations were not carried into this write-up (only their count was passed to it), so §6
records the classes that were attacked and cleared rather than the individual ids. A later reader
re-raising a core-invariant hypothesis should read §6 first.

**Independently re-verified while writing this report** (not taken on the lenses' word): the clamp
overflow and its non-termination, `GATE_JOBS=""` resolving to width 8, the 47-legs-vs-46-timing-rows
arithmetic, and the total absence of `guard` from the canary.

## 3. Findings, severity-ranked

Severity legend: **B** blocker · **H** high · **M** medium · **L** low.
"Gate" = the left-shift check that would have caught the class mechanically.
**Blockers: 0. Highs: 1.**

### Axis A — the canary's arms (the bar's own self-check)

#### F1 · **H** · `tools/run-gates.test.sh:61` (and `:141-145`) — the guard/skip path is exercised by zero arms

*Consolidates ids 6 and 10. Escalated from the lenses' medium; reasoning below.*

This diff moved the run-or-skip decision out of the deleted `leg_if_changed` into a serial pre-pass at
`run-gates.sh:81-86`, which materialises the decision as the literal string `skip` in `$WORK/<i>.rc`.
That one file now has **three** consumers:

- `run-gates.sh:127` — `[ -f "$WORK/$k.rc" ] && continue`, i.e. suppress dispatch entirely;
- `run-gates.sh:108` — the `GATE skip  %s (unchanged vs %s)` branch of `report_one`;
- `run-gates.sh:153,157-158` — the `skips` tally, the `($skips skipped)` note, and the
  `$((n-skips))/$((n-skips))` GREEN arithmetic.

It has **no producer in any arm**. `grep -n 'guard\|skip' tools/run-gates.test.sh` returns exactly one
line, and it is a comment about the unrelated drop-sentinel. Neither the 4-leg fixture (`:61-68`) nor
the generated 30-leg fixture (`:141-145`) declares a `guard` key, so the pre-pass loop `continue`s on
every leg at `run-gates.sh:83` and none of the five code paths above ever executes at any width. No
other gate leg drives `run-gates.sh` at all (`tools/lib/pyrun.sh` and
`tools/memory-tree/check-verdict-epoch.test.sh` merely name it), so this is total, not partial.

**Why H and not M.** A mutation of `run-gates.sh:85` from `changed "${gp[@]}" || printf 'skip' > …` to
an unconditional `printf 'skip' > …` — every guarded leg skipped regardless of the diff, the canonical
green-while-checking-less regression — leaves the whole suite green, and it does so *by construction*,
not by luck: with zero guarded legs in either fixture the mutated line is unreachable from the canary.
The repo's own charter calls this out twice (`AGENTS.md`: "a check that cannot fail is not a check";
this file's header: green-by-absence "is what this canary exists to forbid"), and the exposure grows on
a schedule that is already written down — `memory/backlog/TOOL.md` (TOOL-aTimedTurnstile-2) proposes
guarding the 29 self-test legs that hold 96.7% of the bar's wall, at which point this uncovered path
decides most of the bar. Today only 1 of 47 legs is guarded, which is why it is H and not B.

**Fix.** Add a fifth leg to the arm-3 scratch manifest with `"guard": ["never/touched.txt"]`, commit
the fixture and point `origin/HEAD` at it so `BASE` resolves:

```
git -C "$SCRATCH" add -A && git -C "$SCRATCH" commit -qm fx
git -C "$SCRATCH" update-ref refs/remotes/origin/main HEAD
git -C "$SCRATCH" symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
```

then assert at **both** widths that the output carries the skip line at its manifest position and that
the tally agrees: `GATE skip  <name> (unchanged vs main)` and
`gates GREEN — 4/4 legs passed (1 skipped)`. Both lenses independently ran this fixture against the
current runner and it is green on day one, so the arm reds only on a regression.

**Gate A1 — branch-coverage assert on the reporter.** Have the canary assert its own fixtures exercise
every branch of `report_one`: at least one `GATE ok`, one `GATE FAIL (exit …)`, one `GATE skip`, and
(via the 30-leg arm) the `(no result)` guard. Cheapest honest form is a structural pre-assert on the
fixture manifest — "at least one leg carries a `guard`" — which reds the day someone simplifies the
fixture back. Same shape as the existing check-1 well-formedness assert, ~4 lines.

**Gate A2 — bring the canary inside the harness meta-gate.** `tools/memory-tree/check-arms.py` is the
repo's answer to exactly this class ("a POSITIVE assertion naming the branch's OWN failure text… an
ABSENCE assertion and a COMMENT all fail to arm"), and it cannot see this file: its population is a
tracked `*.sh` that **defines** a `fail() {` helper, and it **excludes `*.test.sh` outright**.
`run-gates.sh` uses a bare `fails=` counter and no helper, so the runner and its canary sit entirely
outside the meta-gate. That exclusion is well-reasoned for its original population (a fixture heredoc
would create phantom gates), but it is why F1, F4 and F5 all shipped in the same file on the same day.
Either widen the predicate to admit a gate whose failure path is a counter rather than a helper, or
add a narrow sibling rule: **in a `*.test.sh`, an arm whose only assertion is a negative (`case … in
*"…"*)`, `! grep`, `grep -v`) must be paired with a positive liveness assertion in the same loop
body.** That single rule catches F4 and F5 mechanically and generalises past this diff.

#### F3 · **M** · `tools/run-gates.test.sh:97` — arm 3c's absolute 5000 ms bound is graded against load it does not control

*Consolidates ids 4, 9 and 14 — three lenses, three independent measurement campaigns.*

The arm times a 4-sleeping-leg scratch run at `GATE_JOBS=4` and requires `par_ms < 5000`. The floor is
**incompressible** — the `sleep 2` leg — so the entire margin lives in the ~0.7-1.8 s of process
overhead (`resolve-python.sh` RUNS candidate interpreters, one python manifest parse, three
`git rev-parse`, four `bash` workers, plus a fork per `$(live)` evaluation), and process overhead is
exactly what dilates under contention. Meanwhile `tools/gate-legs.json:331` makes this file leg 47 of
47, and `run-gates.sh:33` now dispatches at `min(8, nproc)` — **the arm times itself while competing
with seven siblings it did not exist alongside before this diff.**

Measured, across three lenses on this 16-core node:

| condition | `run_scratch 4` wall |
|---|---|
| idle | 2666-3577 ms (53-71% of budget) |
| alongside 6-7 real heavy legs | 3349-3996 ms |
| under sustained CPU contention | 4123-9759 ms; one lens measured **7286 ms** and another **all four reps over budget** |
| sampled 28× *while the real full bar ran* | ~3249 ms typical, worst **4824 ms** — 96.5% of budget |

Corroborating in-repo evidence, independent of any lens: the bar's own timing cache records the
`run-gates canary` leg at **65.4 s** against a ~16.5 s sleep floor (≈4× dilation), and this build's own
spec §Design measures **1.66× per-leg dilation at width 8**. 3.3 s idle × 1.66 = 5.5 s, over the bar.

A trip reds the canary leg, which reds the bar, which blocks `.githooks/pre-push` — whose failure text
is literally `fix, or 'git push --no-verify' to override deliberately`. A bar that reds for a reason
unrelated to any leg's assertion trains operators straight at the one switch that turns the gate off.
Nodes `b` and `c` are separate, unmeasured machines, and `pin-copied-from-another-corpus` is a
catalogued class in this repo.

**Fix.** Assert the property, not a deadline. Arm 3a already produces the width-1 run; time it too and
compare on the same machine in the same conditions:

```
t0=$(date +%s%N); run_scratch 1 >/dev/null; t1=$(date +%s%N); ser_ms=$(( (t1-t0)/1000000 ))
t0=$(date +%s%N); run_scratch 4 >/dev/null; t1=$(date +%s%N); par_ms=$(( (t1-t0)/1000000 ))
[ $((par_ms*2)) -lt "$ser_ms" ] || { echo "canary: width-4 (${par_ms}ms) did not beat half of width-1 (${ser_ms}ms) — the pool is not overlapping"; fail=1; }
```

A pool degraded to serial still fails it (`par_ms ≈ ser_ms`), which is the arm's stated purpose, but
uniform load and cold start cancel. Raising 5000 to a bigger number only moves the cliff.

**Gate A3 — ban absolute wall-clock pins in gate legs.** A one-line grep leg: no `*.test.sh` under
`tools/` may compare a `_ms`/`_sec` variable against a hardcoded literal without a same-run baseline
variable on the other side. Every timing assertion on the bar must be a ratio or a self-calibrated
budget, because every leg on the bar now runs under a load it does not control. This is a new class
created by this diff and it will recur the next time someone times something.

#### F4 · **M** · `tools/run-gates.test.sh:149` — arm 3g asserts only ABSENCE, so a broken fixture passes it

Arm 3g is the **only** regression guard on the `(no result)` race — a race this diff already had to fix
once, and whose fixture the arm's own comment (`:133-136`) documents as carefully tuned ("reproduced at
1-in-40, and let the pre-fix reader pass. Do not 'simplify' this back to the shared fixture"). Its
entire assertion is `case "$o" in *"(no result)"*)`. Nothing checks that the run happened.

Two independent fixture breakages were reproduced and **both left `fail=0` and the arm reporting
success**: omitting the `git init` in `$SCRATCH/many`, and a missing manifest. The first degrades worse
than "no run" — with no `git init`, `git rev-parse --show-toplevel` walks **up** to the parent
`$SCRATCH` repo, so the runner executes the parent's 4-leg manifest at width 1. The arm silently
becomes the exact configuration its own comment forbids, and reports green. The healthy control does
emit 30 `GATE` lines, so the fixture is fine today — the gap is the missing positive assertion.

Arm 3f, twelve lines above, asserts `gates GREEN — 4/4 legs passed`. 3g is the outlier against the
file's own standard.

**Fix.** One line inside the rep loop, before the `case`:

```
printf '%s\n' "$o" | grep -q '^gates GREEN — 30/30 legs passed$' \
  || { echo "canary: the 30-leg width-1 fixture did not run — arm 3g proves nothing"; fail=1; break; }
```

**Gate:** covered by **Gate A2** above (negative-only arm must carry a positive liveness assertion).

#### F5 · **L** · `tools/run-gates.test.sh:123` + `tools/run-gates.sh:34` — one third of the clamp arm is vacuous, and the `''` case alternative is dead

*Consolidates ids 3 and 12.*

`run-gates.sh:33` is `JOBS=${GATE_JOBS:-$(( … ))}`. `:-` substitutes the default for **null as well as
unset**, and the default is an arithmetic expansion that is never empty, so `JOBS` is never the empty
string and the `''` alternative at `:34` is **unreachable**. Deleting `''|` outright leaves
`bash tools/run-gates.test.sh` exiting 0 — verified by mutation, tree restored.

Correspondingly, arm 3f loops `for w in 0 "" nonsense` under a comment asserting the knob "clamps to 1"
and that "these three runs are serial by construction". Measured on this 16-core node:

| `GATE_JOBS` | resolved `JOBS` | reaches the clamp? |
|---|---|---|
| `0` | 1 | yes |
| `nonsense` | 1 | yes |
| `""` | **8** | **no — takes the `min(8,nproc)` default** |

The `""` iteration runs at default width, is not serial, and executes no clamp code; it would still
pass with lines 34-35 deleted entirely. The comment misdescribes the behaviour and one third of the
clamp arm asserts nothing about clamping — which is how F2 shipped.

**Fix.** Drop the unreachable `''` alternative (or switch to `${GATE_JOBS-…}` if an explicitly-empty
knob is meant to clamp), correct the comment, and replace the `""` iteration with inputs that actually
reach the clamp: `for w in 0 -3 nonsense 99999999999999999999`.

**Gate:** the out-of-range value belongs in **Gate B1** below; the vacuous-arm shape is **Gate A2**.

### Axis B — the width knob

#### F2 · **M** · `tools/run-gates.sh:35` — an out-of-range `GATE_JOBS` bypasses the clamp and the runner spins forever having executed zero legs

*Consolidates ids 1 and 5. Independently reproduced while writing this report.*

`case "$JOBS" in ''|*[!0-9]*) JOBS=1 ;; esac` at `:34` rejects only non-digits, so an all-digit value
above int64 reaches `:35`, where `[ "$JOBS" -lt 1 ]` **errors** (bash `strtoimax` overflow, exit 2,
`[: 99999999999999999999: integer expected`) instead of comparing. The clamp never fires. Then:

- `:125` — `[ "$(live)" -lt "$JOBS" ]` errors identically, so the inner dispatch loop never fires and
  `di` stays 0;
- `:137` — `[ "$di" -lt "$ndisp" ] && continue` sends the outer loop straight back to a dispatch pass
  that again does nothing.

Reproduced here on a 2-leg scratch repo built from the real `run-gates.sh` + `resolve-python.sh`:
control run prints two `GATE ok` lines and `gates GREEN — 2/2 legs passed`, exit 0;
`GATE_JOBS=99999999999999999999 timeout 8 bash tools/run-gates.sh` gives **exit 124, 0 stdout lines,
115 stderr lines**, no `----` rule, no verdict, at full CPU (two forks per iteration for `$(live)`).
A second lens measured the same on a 4-leg fixture to a 15 s timeout, 221 stderr lines.

This contradicts the invariant the code's own comment at `:30` asserts — "clamped to 1 rather than
refused — this knob only schedules work, **it can never skip a leg**" — and spec §5's "clamped to at
least 1; it cannot skip a leg or change a verdict". Every leg is skipped and **no verdict is produced
at all**. Wired into `.githooks/pre-push:55` this hangs the push indefinitely rather than failing
closed. Trigger requires a deliberate 20-digit operator value, which is why this is M and not H — but
the failure mode on a merge bar is a silent hang, not a red, and the hang is the part that matters.

**Fix — two halves, both cheap.**

1. **Make the clamp total.** Arithmetic evaluation saturates where `test` errors:
   `JOBS=$(( JOBS < 1 ? 1 : (JOBS > 64 ? 64 : JOBS) ))` after the digit check. (Equivalently, add a
   length alternative to the case: `''|*[!0-9]*|???????????*)`.)
2. **Give the outer loop a real liveness guarantee.** Track whether the preceding dispatch pass
   actually started a worker and only `continue` at `:137` when it did, so a dispatch loop that *can
   never* fire falls through to the `wait` + report path instead of spinning. Half 1 fixes the known
   input; half 2 makes the class non-fatal — the runner would report `(no result)` per leg and exit
   RED, which is the correct fail-closed behaviour for any future way of reaching that state.

**Gate B1 — width fuzz with a timeout, and the timeout is the point.** Extend arm 3f to
`for w in 0 -3 nonsense 99999999999999999999 999999999999999999999999999999`, and wrap each run in
`timeout 30`. The current arm shape would **hang forever** on this input rather than red, so adding the
value without the timeout converts a silent hang in production into a silent hang on the bar. Assert
both that the run terminates and that it prints the full `gates GREEN — 4/4 legs passed` line.

**Gate B2 — no `test`-based numeric comparison on operator input.** A grep leg over `tools/**/*.sh`:
any `[ "$VAR" -lt/-gt/-le/-ge` where `VAR` derives from an environment variable must be preceded by an
arithmetic clamp. Narrower and more durable than fuzzing one knob — the next env knob someone adds
inherits the guarantee. This is the same left-shift shape as `check-install-prefix.sh`: forbid the
spelling, not the instance.

### Axis C — the timing cache

#### F6 · **L** · `tools/run-gates.sh:148` — the cache rewrite deletes every guard-skipped leg's row

`:145-150` rewrites `<git-dir>/gate-timings.tsv` **whole**, and `:148` emits a row only
`[ -f "$WORK/$i.sec" ]`. `.sec` is written exclusively inside `runleg()` (`:96`), which a guard-skipped
leg never enters because `:127` suppresses its dispatch. So every rewrite silently discards the
previously-cached duration of every skipped leg.

Confirmed on this repo, independently: `tools/gate-legs.json` holds **47** legs, the worktree's
`gate-timings.tsv` holds **46** rows, and the one absent name is exactly `manifest-check self-test` —
the repo's single guarded leg — while that same run's `gate-last-summary.txt` reads
`gates GREEN — 46/46 legs passed (1 skipped)`.

The cost is on S3, the dispatch hint: `:63`'s `durs.get(data[i]["name"], 0.0)` scores an unknown leg 0.0
and sorts it **last** in longest-first dispatch. The diff-scoped DoR/post-merge runs are exactly the
runs where guards fire, so they are exactly the runs that strip the hint the next full push-boundary
run needs. Correctly low: the cache is advisory and can never move a verdict (`:44`, `:144` both say
so, and arm 3e proves a corrupt cache is survivable). It worsens under TOOL-aTimedTurnstile-2's
proposed 29 extra guards, at which point a diff-scoped run would blank most of the cache.

**Fix.** Merge on absent instead of truncating: read the existing TSV into a name→seconds map, overwrite
only the entries for legs that produced a `.sec` this run, emit the union. Legs dropped from
`gate-legs.json` fall out naturally because the python side keys on the manifest's names.

**Gate C1 — cache-survival arm.** With the guarded leg from **F1**'s fixture in place: run once at full
scope so every leg times, then run again with the guard firing, and assert the skipped leg's row is
still in `gate-timings.tsv`. Three lines on top of a fixture F1 already builds, and it pins the
"advisory data survives a scoped run" property the next cache edit would otherwise break silently.

## 4. Left-shift gates, ranked by value

| # | Gate | Catches | Cost |
|---|------|---------|------|
| **A2** | negative-only arms must carry a positive liveness assertion (`check-arms.py` sibling rule, or widen its population past the `fail() {` + non-`*.test.sh` predicate) | F1, F4, F5, and the whole class | one rule, ~20 lines python |
| **A1** | reporter branch coverage: the fixtures must exercise `ok`, `FAIL`, `skip`, `(no result)` | F1 permanently | ~4 lines, rides F1's fixture |
| **B2** | no `test`-based numeric comparison on env-derived input | F2 and every future knob | one grep leg |
| **A3** | no absolute wall-clock literal in a gate leg without a same-run baseline | F3 and every future timing pin | one grep leg |
| **B1** | width fuzz **under `timeout`** | F2's specific input; the timeout also converts any future hang into a red | 5 lines in arm 3f |
| **C1** | advisory-cache survival across a scoped run | F6 | 3 lines |

A2 is the highest-value item in the report and the one with reach past this diff: the repo already owns
a meta-gate whose entire thesis is "an ABSENCE assertion is not an arm", and the file that just gained
seven new arms is structurally invisible to it.

## 5. What held up (recorded so it is not re-attacked)

Five hypotheses were refuted, and they cluster on the core concurrency invariants. A later reader should
not re-raise these without new evidence:

- **Result-file tearing.** `runleg()` (`:88-97`) writes `.out`, then `.sec`, then `mv -f`s a temp into
  `.rc`. `.rc` is the completion signal and it appears last, atomically. The reader never gates on
  `.out`, so a partially-written `.out` cannot be read as a result.
- **Manifest / dispatch-order / report-cursor misalignment.** The two indices are deliberately
  independent: `disp`/`di` walk the advisory ORDER line, `next` walks the manifest, and both address the
  same `names[]`/`argvs[]` arrays built 1:1 with the manifest at `:71-76`. Reporting can therefore never
  inherit a scheduling reorder — which is what makes the byte-identity result (`GATE_JOBS=1` vs the
  pre-change runner, and width 1 vs width 8) meaningful rather than coincidental.
- **The `(no result)` race.** The three-condition guard at `:130-140` (dispatch exhausted **and** a full
  `wait` **and** a re-check) is the correct closure for the `jobs -rp`-only-counts-RUNNING hole, and arm
  3g's fixture is tuned to the condition that actually reproduces it (30 instant legs at width 1, 6-in-8
  against the pre-fix reader) rather than a plausible-looking one. The arm's *assertion* is weak (F4);
  its *fixture* is not.
- **The tally.** `n` increments only inside `report_one`, once per printed line; `skips` and `fails`
  increment on the same branches that print. The GREEN line's `$((n-skips))/$((n-skips))` and the RED
  line's `$fails/$n` are therefore derived from the printed lines, not from a parallel count.
- **The drop-sentinel.** An empty name holds its index and is skipped at both `:124` (report) and `:127`
  (dispatch), and is never counted. Worth noting for the record: canary check 1 (`:24-27`) **rejects an
  empty name in `gate-legs.json` outright**, so the sentinel path is unreachable from any valid manifest
  and is defensive depth rather than live behaviour. Not a finding — but it is the second uncovered
  branch in `report_one`'s neighbourhood, and Gate A1 should note it rather than demand an arm for it.

## 6. Recommended landing order

1. **F1** (guarded leg in the fixture + the two asserts) — lands with the diff. It is the arm that makes
   every future edit to the skip path honest, and TOOL-aTimedTurnstile-2 is queued directly behind it.
2. **F2 half 1** (arithmetic clamp) + **B1** (fuzz under `timeout`) — one line each, removes a silent
   hang on the push boundary.
3. **F3** (ratio instead of 5000 ms) — before the next node runs the bar. `b` and `c` are unmeasured
   machines and this is the arm most likely to red one of them for nothing.
4. **F4** (one-line liveness assert in 3g) — trivial, and it protects the only guard on a race that has
   already bitten once.
5. **F5**, **F6**, and gates **A2/A3/B2** — a follow-up unit. A2 in particular deserves its own spec:
   widening `check-arms.py`'s population is a change to a gate that grades other gates, and its header
   documents at length why the current predicate is shaped the way it is.
