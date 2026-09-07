**Serves:** diff-review TOOL-aPooledSweep-1 TOOL-aPooledSweep-2 TOOL-aPooledSweep-3

# Tier-2 diff review — the closing fold of the pooled sweep mode

*Node `a` · 2026-09-07 · reviewed at the integration boundary (the cumulative diff landing on `main`),
per charter §8. Adversarial lens fan → skeptic refutation → this synthesis.*

Reviewed range: `2d2dcf10...HEAD` · ROUND 2

## Verdict: BLOCKED

One blocker. The fold repaired the wall's *rendering* path and, in the same edit, removed the only
thing that ever *stopped* the run at the wall — so `--sweep` now advertises a bound it does not
enforce. Everything else can land behind it. Every finding below was reproduced against the shipped
script, and I re-verified the blocker and the two mediums myself before writing this; none of it is
inferred from reading.

## Review shape

| | |
|---|---|
| Range | `2d2dcf10...HEAD` (1 commit, `16def840`) |
| Round | 2 |
| Raw findings | 16 |
| Confirmed | 15 |
| Refuted | 1 |
| Unverified | 0 |
| Precision | 0.94 |
| Distinct defects after merge | 8 |

## Run integrity

- Lenses: 4/4 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified; 0 spurious verdicts discarded; 0 duplicates
  removed by the harness.

Every counter is zero, so this run is complete: the finding set is not truncated by a dead lens, and
a zero elsewhere in this report is evidence rather than an absence of evidence.

One thing the harness's zero-duplicate count does not capture, and it matters for reading the table
below. The 15 confirmed findings are 8 distinct defects: three lenses each independently reproduced
the wall-launch regression, three each reproduced the wall-derivation arithmetic, three each caught
the stale stamp comment, and two caught the leading-zero refusal gap. I merged them at adjudication
time. The convergence is a signal, not noise — three lenses built three different fixtures for the
blocker and all three got the same overrun — so the co-reporting counts are kept in the table.

## Findings

Severity is the one I adjudicated here, which is not always the lens's. Two promotions and one
demotion are argued in place.

| # | Sev | Where | Defect |
|---|-----|-------|--------|
| D1 | BLOCKER | `tools/run-gates/run-selftests.sh:530` | The wall fires, kills the in-flight workers, and the pool keeps launching every remaining suite. |
| D2 | HIGH | `tools/run-gates/run-selftests.sh:492` | `$(( $(date +%s%N) / … ))` kills every worker on a host with BSD `date`, turning `--sweep` into a total false RED. |
| D3 | MEDIUM | `tools/run-gates/run-selftests.sh:412` | The derived wall is 2x–15x the run's own maximum possible duration, so it can never fire on the shipped population. |
| D4 | MEDIUM | `tools/run-gates/run-selftests.test.sh:335` | Neither the wall derivation nor the post-breach launch behaviour is asserted by any arm. |
| D5 | LOW | `tools/run-gates/run-selftests.sh:263` | The new `SELFTEST_OUTER_WIDTH` refusal misses every leading-zero spelling. |
| D6 | LOW | `tools/run-gates/run-selftests.sh:609` | The comment justifying the strict `>` says the stamps are whole seconds; the same commit made them milliseconds. |
| D7 | LOW | `tools/run-gates/run-selftests.sh:32` | `SELF` keeps whatever path the invoker typed, so the two remedy lines are not repo-root-relative after a relative invocation. |
| D8 | LOW | `…/build/2026-09-07-build-TOOL-aPooledSweep-1-acceptance-ledger-and-the-measured-ab.md:74` | AC9's arithmetic half states a wall figure the same commit superseded. |

---

### D1 — BLOCKER — the run wall no longer bounds the run

`tools/run-gates/run-selftests.sh:530` (the dispatch loop), against the watchdog at `:519-524`.

Co-reported by three lenses (raw ids 3, 8, 13), each with its own fixture, each reaching the same
result.

The pid fix is correct as far as it goes: `echo $$` in a backgrounded subshell wrote the *runner's*
pid into every pid file, so the watchdog SIGTERMed `run-selftests.sh` itself. That did stop the run —
destructively, with no verdicts — and it was the only stopping mechanism the wall had. Redirecting
the kill to the `timeout` children removed it and added nothing in its place.

The watchdog is a single pass over the pid files that exist at the breach instant, then it exits. The
dispatch loop never reads `$SWEEP_ROOT/wall-breached`. So after the wall fires, the pool goes on
launching.

Reproduced three times independently. The tightest run: a 3-row fixture at `SELFTEST_OUTER_WIDTH=1`
with `SELFTEST_WALL=10` killed row two at 10s, then launched and completed row three, exiting at 16s
against its own advertised 10s wall — and rendered `ok` for a suite that started after the breach.
A second lens got 17s, a third 23s, all on the same shape.

On the shipped 59-row population at the resolved width 8, a breach in wave 1 signals at most the
eight workers holding a pid file and leaves seven waves to run — hours past the bound, while the
summary prints `the Ns run wall killed: <one name>` as though the run had stopped.

The sibling runner in the same directory already carries the guard, `run-gates.sh:1533`, with the
incident that motivated it recorded immediately above at `:1508`: a third leg started 57s after the
breach and ran to completion, 149s against an 8s bound. That is this defect, already measured once in
this repo, on the other runner.

**Fix.** One line, mirroring the sibling: `[ -e "$SWEEP_ROOT/wall-breached" ] && break` as the first
statement of the `while [ "$i" -le "$SW_N" ]` body. Rows with no verdict file then fall into the
existing `WALL_BREACHED` missing-verdict branch at `:563-565`, which finally has a reason to exist;
reword it to distinguish "never started" from "killed mid-flight".

**Left-shift gate.** Extend the wall arm's fixture to three suites so one exists *after* the walled
one, and assert that row did not run. The current arm cannot see this defect and never could: its
fixture holds exactly two suites and the walled one is the last, so there is nothing left to
dispatch. Charter §7 — a new gate is not landed until its failing case has been observed — is unpaid
here, and this is the specific arm that did not pay it.

*Why blocker rather than high.* The commit's own comment at `:492` claims this fold made the WALL
rendering path reachable. It did, and in the same edit it made the wall non-binding, which is the
larger of the two properties. A backstop that prints a bound it does not enforce is worse than an
absent one, and the fix is a single line already written elsewhere in the same directory.

### D2 — HIGH — `date +%N` inside arithmetic kills every worker on a BSD host

`tools/run-gates/run-selftests.sh:492`, and identically at `:504`.

`s=$(( $(date +%s%N) / 1000000 ))` assumes GNU `date`. A BSD/macOS `date` prints the literal `N` for
the unsupported directive, so the expansion becomes `$(( 1788791142N / 1000000 ))`. I confirmed the
abort semantics directly: the arithmetic error aborts the enclosing shell, the statement after it
never runs, exit 1. Applied here, the backgrounded `_rs_sweep_one` subshell dies at line 492, before
`$d/v` is written.

Every row then renders `FAIL … (no verdict was written, so this suite could not start)`. That is a
total false RED whose message blames each suite for the runner's own arithmetic — a wrong verdict
that looks like a real one, which is worse than a hang.

Reachability is asserted by the script itself, not by me. Lines `355-362` resolve `gtimeout` over
`timeout` precisely because coreutils ships prefixed on Homebrew and macOS — the one platform family
where `date` is BSD. The block advertises support for the host it cannot run on. Nothing in the repo
pins GNU coreutils; §11 pins `bash` and `python3` only. This is a kit copied into adopter repos.

Partial mitigation, and only on novelty: `run-gates.sh:1283` and `:1311` already call `date +%s%N`,
but as bare assignments rather than inside `$(( ))`, so they degrade rather than abort. The new code
is what makes the assumption lethal.

**Fix.** Probe once beside the existing `timeout` probe and fall back:

```sh
if [ "$(date +%N)" = N ]; then _rs_now_ms(){ echo $(( $(date +%s) * 1000 )); }
else _rs_now_ms(){ echo $(( $(date +%s%N) / 1000000 )); }; fi
```

The fallback costs only sub-second resolution on the peak figure, which the half-open `>` at `:613`
already tolerates.

**Left-shift gate.** An arm that shims a BSD-style `date` onto `PATH` in front of the fixture and
asserts the sweep still renders verdicts — the same shape as the existing `git-nostatus.sh` shim arm
at `:315`, which is already the pattern for "a tool that answers differently than assumed".

### D3 — MEDIUM — the derived wall cannot fire on the real population

`tools/run-gates/run-selftests.sh:412`. Co-reported by three lenses (raw ids 4, 9, 14).

Arithmetic re-checked against the shipped declaration, by me: `selftest-budgets.txt` holds 59 rows
summing to 55280 with a largest budget of 13600, `sweep-ceiling-factor: 2`, and
`run-gates.sh --print-profile` resolves width 8 on this node. So the largest per-suite bound is
27200s and the sum of every bound is 110560s.

Every suite is individually bounded by `timeout -k 5`, so the pool's makespan cannot exceed
sum-of-bounds — about 41000s at width 8, 110560s at outer 1. The derived wall is
`SWEEP_LARGEST * SWEEP_WAVES` = 217600s at width 8 and 1604800s (18.6 days) at the
`SELFTEST_OUTER_WIDTH=1` setting the new comment itself cites. Both are above the ceiling the
per-suite bounds already impose, so the wall is unreachable.

Worse than incidental: at `OUTER=1` the formula reduces to largest x N, which is greater than or
equal to sum-of-bounds for *any* declaration. The wall is unreachable by construction in that mode,
not merely by these numbers.

Round 1's D4 prescribed `max(SWEEP_LARGEST, ceil(SUM_BOUNDS / OUTER))`. The landed code took neither
that form nor an equivalent — it over-corrected from a wall that was too small into one that never
binds. The mechanism-that-cannot-fire class this repo gates for elsewhere.

The knock-on is why this is not merely cosmetic: the WALL rendering path D1's pid fix just repaired
is now reachable *only* through a manual `SELFTEST_WALL`, which is exactly what the new arm has to
pass.

**Fix.** Accumulate `SWEEP_SUM` in the loop at `:387-394` that already computes `SWEEP_LARGEST`, then

```sh
SWEEP_WALL=$(( (SWEEP_SUM + OUTER - 1) / OUTER + SWEEP_LARGEST ))
```

That is the standard list-scheduling makespan bound — correct at every width, 5x to 12x tighter, and
it keeps the existing `SWEEP_WALL -lt SWEEP_LARGEST` refusal valid. Also correct the paragraph title
at `:399`, `THE RUN WALL IS THE LARGEST PER-SUITE BOUND`, which the paragraph appended below it at
`:404` now contradicts.

*Why medium rather than high.* The per-suite `timeout` bounds still cap every suite, so nothing runs
unbounded. The defect is an inert backstop and a header line that states a bound it cannot enforce,
not a hang.

### D4 — MEDIUM — no arm asserts the wall derivation or the post-breach launch

`tools/run-gates/run-selftests.test.sh:335`.

The new WALL arm passes `SELFTEST_WALL=10` explicitly, so it exercises the override branch, never the
derivation. I checked every arm in the file: the refusal arm at `:221` passes `SELFTEST_WALL=5`
against `SWEEP_LARGEST=120` and would still refuse with the derivation reverted; no arm greps `wave`;
none reads the `run wall <n>s` value printed at `:472`. The fixture's two rows carry budget 60 → a
120s bound while its suites sleep at most 5s, so `SWEEP_WALL=$SWEEP_LARGEST` (120s) and
`SWEEP_LARGEST * SWEEP_WAVES` (240s) are indistinguishable to every unset-wall arm.

The whole new derivation path can be reverted and all 41 arms stay green. Round 1's D4 explicitly
prescribed the missing gate: the same fixture at `SELFTEST_OUTER_WIDTH=1` and at the resolved width
must print a strictly larger run wall for the narrower pool.

**Fix / left-shift gate — the same thing here.** Two arms:

1. Run the fixture at `SELFTEST_OUTER_WIDTH=1` and at the resolved width with no `SELFTEST_WALL`, and
   assert the narrower pool prints a strictly larger `run wall`; capture with the
   `sed -n 's/.*run wall \([0-9]*\)s.*/\1/p'` shape the round-trip helper already uses.
2. The three-suite post-breach arm from D1.

*Why medium rather than the low it was reported at.* This is not one missing arm among many — it is
the arm whose absence let D1 land, and it is the left-shift for D1 and D3 both. §7's "a gate you have
only ever seen pass is an assertion about nothing" applies to the fold's own new arm.

### D5 — LOW — the width refusal misses every leading-zero spelling

`tools/run-gates/run-selftests.sh:263`. Co-reported by two lenses (raw ids 2, 6).

The refusal arm is `*[!0-9]*|0`, which matches the literal `0` only. I reproduced the case statement
directly: `00`, `007` and `08` all fall through to `*)`, and the clamp accepts them because
`[ 08 -le 8 ]` evaluates numerically true.

What the operator gets instead of the declared exit-2 refusal:

- `00` — `line 273: W / OUTER : division by 0`, the same at `:411`, then
  `line 673: SELFTEST_INNER_WIDTH: unbound variable`, exit 1. No message names the knob.
- `08`, `09` — bash reads a leading zero as octal in `$(( ))`, so the run dies with
  `value too great for base`, exit 1. Confirmed in isolation.
- `007` — silently becomes 7, and the run prints `outer 007`.

That last one is the interesting one: it is the exact "a knob you asked for was silently discarded"
shape this block was written to prevent, one input class over. The arm the fold shipped covers `abc`
and nothing else.

**Fix.** Validate numerically rather than by pattern — keep `*[!0-9]*)` for the non-numeric case and
add `[ "$SELFTEST_OUTER_WIDTH" -ge 1 ] || <refuse>` in the accepting arm, which catches `0`, `00` and
`000` alike. Strip a leading zero before the arithmetic, or refuse it, so `08` cannot reach `$(( ))`.

**Left-shift gate.** A second want-rc-2 arm with `SELFTEST_OUTER_WIDTH=00` beside the `abc` one, and
a third with `08`. Same for `SELFTEST_WALL`, whose `*[!0-9]*)` arm has the same shape.

### D6 — LOW — the stamp comment was falsified by its own commit

`tools/run-gates/run-selftests.sh:609`. Co-reported by three lenses (raw ids 7, 11, 15).

The awk rationale reads "Stamps are whole seconds, so with `>=` a suite ENDING at second T and its
replacement STARTING at T both count at T". Verified by archaeology, not just by reading:
`git show 16def840` contains both that added comment and the switch of `s` and `e` to
`$(( $(date +%s%N) / 1000000 ))`. The preceding commit `2d2dcf10` contains neither. The rationale was
false the moment it was written, and the build ledger appended in the same commit states the correct
unit — so the code and the record disagree about the file they both describe.

Its supporting measurement is stale too: it cites a strictly serial fixture reporting peak 2, which
under the current millisecond stamps reports peak 1.

No runtime effect — the strict `>` is correct half-open semantics at any resolution. The damage is
that the next reader either mis-reasons about `took=$(( (e - s) / 1000 ))` two blocks up, or reverts
the `>` for having lost its stated premise, reinstating the handoff double-count the new peak-1 arm
exists to pin.

**Fix.** Re-state the reason against the current stamps: the interval is half-open because a suite
ending at instant T and its replacement starting at T are a handoff and not an overlap — true at any
resolution — and note that millisecond stamps make an exact-tie handoff rare rather than certain.

**Left-shift gate.** None fits; comment-vs-code contradiction is not gateable here. This is a §10
checklist entry: *a diff that changes a unit must re-read the prose that states that unit.* The
existing peak-1 arm already covers the behaviour.

### D7 — LOW — `SELF` is not repo-relative after a relative invocation

`tools/run-gates/run-selftests.sh:32`.

`SELF=${0#"$ROOT"/}; SELF=${SELF#./}` strips a prefix that a relative `$0` never has. Invoked as
`bash ./run-selftests.sh` from `tools/run-gates`, `$0` is `./run-selftests.sh`, the `ROOT` strip is a
no-op, and `SELF` ends as the bare filename — while the script has already `cd`'d to the repo root.
The two remedy lines at `:656` and `:668` then print `bash run-selftests.sh`, which is copied out of a
gate log or a landing report and pasted at the repo root, where it resolves to nothing.

The non-empty guard at `:33` cannot catch it: the derivation is not empty, just relative to a
directory the script no longer stands in. The header comment claims the value is "THIS SCRIPT'S OWN
REPO-RELATIVE PATH, DERIVED", which it is not for any relative invocation.

**Fix.** Derive from the already-resolved absolute dir instead of `$0`:
`SELF="${HERE#"$ROOT"/}/$(basename -- "$0")"`, keeping the existing refusal. `HERE` is absolute and
under `ROOT` for every invocation form, so the strip always lands.

**Left-shift gate.** One arm invoking the runner by a relative path from inside `tools/run-gates` and
asserting the printed remedy line contains a `/`. Cheap, and it also pins the install-prefix property
the derivation exists for.

### D8 — LOW — the acceptance ledger gives two answers for the wall

`memory/builds/aPooledSweep/build/2026-09-07-build-TOOL-aPooledSweep-1-acceptance-ledger-and-the-measured-ab.md:74`.

AC9's arithmetic half states "over the real population the largest budget is 13600 s and the derived
wall is 27200 s". The D4 paragraph appended to the same file in the same commit says the wall is
"`largest bound x waves` now" — 217600s at width 8. Both lines are in the file; 27200s was correct
under the pre-fold derivation.

AC9's surviving conclusion (the wall is above the largest per-suite bound by construction) still
holds, so this is a stale figure rather than a wrong verdict. But the acceptance record is what a
later session reads to learn what was verified, and re-deriving the wall is exactly the reading the
record exists to avoid.

**Fix.** Amend the AC9 line to the new derivation, or restate it as the value the wall had when AC9
was observed with an explicit note that D4 superseded it — a record of what was true then, not a
claim about the code as it stands. If D3 above is taken, this line is rewritten a second time; do it
once, after.

**Left-shift gate.** None. This is the "one fact in one place" rule (§6) applied to a record, and the
documented check is that a fold amending a derivation greps the build folder for the old figure
before committing.

---

## Refuted

One finding was refuted by the skeptic pass and is recorded here so it is not re-raised: it did not
survive verification and no action is owed.

## What is not covered by this review

The merge-bar legs themselves were not re-run for this report — this is a diff review, not a gate
run. Round 1 blocked partly on `tools/check-install-prefix.sh` being red on this worktree; the fold's
D3 paragraph claims it now exits 0, and I did not independently re-run it. Confirm that at the push
boundary before landing.

The nine-suite A/B measurement recorded in the acceptance ledger was read, not reproduced. Its
conclusion is not disturbed by anything above.

## Landing

Fix D1 before this lands. It is one line and it has a working reference implementation in the
adjacent file. D2 and D3 should ride with it — D2 because an adopter on macOS gets a fabricated RED
and no way to tell, D3 because leaving it means the wall D1 repairs still cannot fire without a
manual knob. D4's two arms are what stop the pair coming back. The four lows can land in the same
fold or the next one; none of them changes a verdict.
