**Serves:** spec-audit TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 TOOL-aUnblockedFleet-6

# Design review — aUnblockedFleet round 2: unit 6 read cold, five rev-2 folds re-read

*Tier-2 adversarial pass over the spec set only. No code was changed. Every source claim below was
re-verified against the working tree at base `117de044` before this report was written, by opening
the cited lines rather than by trusting a finder's quotation. Round 1's three blockers and seven
highs are not re-litigated here: they were folded, and this pass grades the folds plus the unit the
fold created.*

**Reviewed subjects, each pinned at the blob it was read at:**

- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-1.md@735341ebcecdc3a37014737e3a972ee24698bd64`
- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-2.md@2af21eb6f9ea4770dbc22b56201e49aed30e206f`
- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-3.md@eb1a2edb292d864c1e63f5ee619ab35c6e01c646`
- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-4.md@f57fd76fe61ec2070fb812e38af167cedd56d062`
- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-5.md@87223bd7adf436bd0a080585d48516e739f67fce`
- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-6.md@a0db53270f08fdd70e1ac61bd9eb368d4fc91085`

**ROUND: 2.**

## Verdict: BLOCKED

Three blockers, five highs, four mediums, one low — thirteen distinct defects after dedupe, from
twenty-five confirmed raw findings. All three blockers and three of the five highs are in
`TOOL-aUnblockedFleet-6`, the unit round 1 created and nobody has reviewed until now. The five folded
units are in much better shape than they were: every round-1 blocker is genuinely closed, and the
ownership hazard the fold removed from units 1 and 2 stayed removed. What blocks the set is that the
new unit re-created that hazard, and that its own observability half is dead twice over.

The headline is one sentence. **Unit 6's thesis is right and its two mechanisms are both wrong in the
same direction: the queue evidence it reads is at a path production never writes, and the fix that
makes the fail-open reachable is the same edit that destroys the evidence.** `run-gates.sh:686`
writes `gate-queue-status` to `$gd` — `git rev-parse --git-dir`, the *per-worktree* dir — while S5,
AC5 and §10 all name `<git-common-dir>`. Every unattended run in this fleet lives in a sibling
worktree, where those two resolve differently. And `:692` deletes that file the instant the wait loop
ends, which after S3 is always ~900 s, long before the 3600 s kill S5 exists to explain. Both arms go
green anyway, because AC5 *plants* the file at the reader's own path. That is the fixture-satisfied
gate the charter §7 names, twice, in one scope item.

The third blocker is not about observability at all. `TS_MAXWAIT` has a second consumer that unit 6
never mentions: `ts_sweep_queue` derives its stale-ticket cutoff from it, and the sweep's entire
safety argument is that a ticket older than `TS_MAXWAIT` cannot belong to a live waiter. Make the
bound per-invocation and that is false — an unattended bar at 900 s sweeps the live tickets of
ordinary bars entitled to 7200 s, and a swept waiter can never match its own acquire predicate again.
Unit 6 would then re-create the exact wedge the sweep was written to remove, on a bystander.

## Review shape

- **raw 44 · confirmed 25 · refuted 19 · unverified 0 · precision 0.57.**
- The 25 confirmed collapse to **13 distinct defects: 3 BLOCKER · 5 HIGH · 4 MEDIUM · 1 LOW.** Each
  section names the raw ids that reached it. Four independent lenses found the `gate-queue-status`
  path defect and four found the test-file ownership collision, which is the expected shape when a
  fresh unit is read by several lenses at once.
- Precision 0.57 is above the ~0.5 floor charter §8 names and up from round 1's 0.43. Read the rise
  as the target changing rather than the fan improving: an unreviewed Tier-2 unit with real source
  claims in it is a richer surface than five folded prose specs.
- **Severities here are this report's adjudication, not the raw finders'.** Two raw highs were
  promoted to blocker (the S3/S5 contradiction, the sweep consumer) because a build that follows the
  spec literally ships a dead feature behind a green arm. One raw high (`lengthens nothing`) was
  *not* promoted, because on the arithmetic it converts a tail failure into a median slowdown rather
  than a new failure — real, mis-stated in the spec, not unbuildable.
- **Not covered, stated so a green row is not misread:** the full bar was NOT run for this review, no
  staged two-worktree race was constructed, and no arm was executed. The path claim in B1 was checked
  by resolving both git dirs in this worktree; everything else is source reading. The five folded
  units were re-read only for new contradictions introduced by their folds, not audited afresh.

---

# BLOCKERS

## B1 — The queue breadcrumb is at the per-worktree git dir, and the spec names the common dir in all three places

*(raw ids 2, 11, 22, 33)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §2 S5, §6 AC5, §10 "The second
seam"**

S5 says the driver reads `<git-common-dir>/gate-queue-status`, "which `run-gates.sh:686` already
writes". It does not. `run-gates.sh:686` writes `"$gd/gate-queue-status"`; `gd="$GD"` at `:157`; and
`GD="$(git rev-parse --git-dir 2>/dev/null)"` at `:95`. That is the **per-worktree** git dir. The
common dir is a different variable entirely — `TS_COMMON=$(git rev-parse --git-common-dir …)` at
`:421` — and the turnstile block's own header states the split deliberately: *"The runner's
per-worktree `$gd` resolutions above are deliberate and are left exactly as they are: evidence is
per-worktree, contention is per-repository."*

In this very worktree the two resolve to `…/.git/worktrees/<name>` and `…/.git`. Charter §3 puts
every feature run in a sibling worktree, so the deployment unit 6 exists for is exactly the
deployment where the driver would stat a path nothing writes. The reason the wrong path reads
plausibly is that the driver already resolves the common dir at `unattended.sh:2214` for the lander
marker — a genuinely repo-wide fact — and this one is not.

AC5 hides it. It plants the status file and then asserts the message names the queue, so the arm
grades the reader against a fixture the reader itself defines. The existing suite cannot catch it
either: `run-gates.turnstile.test.sh:248` uses `$R8/.git/gate-queue-status` in a plain scratch repo,
where `--git-dir` and `--git-common-dir` coincide.

**Fix.** S5, AC5 and §10 name `git rev-parse --git-dir`, spelled as the expression rather than as a
literal path, and the driver resolves it with that same command. Add one arm that runs the killed
case from a **linked worktree** rather than a plain clone, and one that lets a real queued bar write
the file and reads it back, so writer and reader are joined by something other than a planted
fixture.

**Left-shift gate.** `run-gates.turnstile.test.sh` gets a worktree fixture — `git worktree add` in
the scratch repo, run the queued bar from it, assert the file appears under `--git-dir` and NOT under
`--git-common-dir`. That one arm pins the distinction the source comment already asserts and would
red on any future edit that moves the writer. It is also the arm that makes every other
`gate-queue-status` assertion in the suite mean something, since today they all run where the two
paths are the same directory.

## B2 — `TS_MAXWAIT` has a second consumer unit 6 never names, and making it per-run falsifies the sweep's safety property

*(raw ids 20, 34)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §2 S1, its absence from §3 and §5 `risks`,
and §10's verification list**

S1 turns `TS_MAXWAIT` into an env-settable per-invocation value. `TS_MAXWAIT` is not only the wait
bound: `ts_sweep_queue` derives its stale-ticket cutoff from it at `run-gates.sh:515`
(`cutoff=$(date -u -d "@$(( $(ts_now) - TS_MAXWAIT ))" …)`), and the age branch at `:536` sweeps on
the stamp **alone** — the dead-pid branch at `:531` `continue`s only when the pid is *dead*, so a
live waiter's ticket falls straight through to the age test.

The source states the invariant that makes this safe, at `:494-496`: *"a live waiter FAILS OPEN at
`TS_MAXWAIT` and drops its own ticket, so a ticket past that bound cannot belong to one. DERIVED from
the fail-open rule below rather than chosen."* And `:488-490` prices the failure: sweeping a live
waiter's ticket "leaves that waiter unable to ever match the acquire predicate … Strictly worse."

That derivation holds only while every bar in the repository shares one `TS_MAXWAIT`. After S1 an
unattended close runs with 900 while an ordinary developer bar runs with 7200, and the close's sweep
deletes the ticket of a live waiter aged 900-7200 s. The victim still holds `TS_TICKET`, but its
acquire predicate is `ls -1 "$TS_Q" | sort | head -1` matched against its own basename (`:606`),
which a deleted file can never satisfy — so it spins to its full 7200 s bound and then runs unqueued.
Unit 6 would inflict, on a bystander, the wedge class its own §4 cites the turnstile records for
removing.

§10's "Verified against source at writing time" list stops at `:686` and never reaches `:495-536`,
which is precisely why this is a spec defect rather than an implementation risk: the reuse audit
looked at the knob's *definition* and not at its readers.

**Fix.** Sever the two uses in scope, not in code review. Add an S-item stating that the override
applies to the **fail-open comparison only** (`:665-668`) and that `ts_sweep_queue` keeps its cutoff
on the derived `TS_TTL * 4`. That direction is safe because a waiter that drops its ticket *earlier*
than the cutoff still satisfies "older than the cutoff implies dead"; the reverse is not. The
alternative — writing each waiter's own bound into its ticket name so a sweeper judges by the owner's
declaration — is strictly bigger and buys nothing this build needs.

**Left-shift gate.** An arm in `run-gates.turnstile.test.sh`: plant a ticket for a **live** pid with
a stamp older than a short override, run a bar with `GATE_TURNSTILE_MAXWAIT` set below that age, and
assert the ticket survives and no "sweeping a queue ticket past the bounded wait" line is printed.
That arm fails today for the right reason and is the smallest thing that pins the invariant to the
knob.

## B3 — S3 deletes the state S5 exists to report; the two scope items answer one question incompatibly

*(raw id 12)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §2 S3 against §2 S5, and §5 `observability`**

S5's reported state is "the bar was killed by `GATE_BOUND` while still queued". `run-gates.sh:692`
removes `gate-queue-status` immediately after the wait loop, and that line is reached on **both**
exits — the acquire break and the fail-open break at `:669`. S3 pins the loop's exit at
`GATE_BOUND / 4`, i.e. at 25 % of the bound, by construction and for any `GATE_BOUND`. So after S3
the process is never simultaneously alive and queued at the kill: it fails open at ~900 s, the file
is deleted, legs run, and the kill at 3600 s lands with the file already gone.

The only surviving path to S5's hit state is S2's ignore path, where a malformed override restores
the 7200 s derivation — the misconfiguration case. §5 promises that after this unit a bound kill
"says whether the bar ever started"; on the path S3 creates it always says the same thing, and AC6's
`miss` arm is describing the normal case rather than the control it claims to be. AC5 passes anyway,
for B1's reason: it plants the file.

There is one genuine survivor worth pointing S5 at instead. The queued-phase signal traps at
`:579-581` run `ts_drop_ticket; exit <n>` and do **not** remove `gate-queue-status`, so a bar TERM'd
*while still queued* does leave the file behind — but that is the pre-S3 world, and after S3 it is
only reachable inside the first 900 s.

**Fix.** Re-point S5 at evidence the fix does not destroy: the `turnstile WAIT EXPIRED after Ns
(bound Ns)` line at `:668`, which `run_bounded` already captures into `RB_OUT` and which the driver
therefore already has in hand at `unattended.sh:2852`, or the run-record queue fields resolved after
the block at `:700`. Restate AC5 as *a bar that failed open reports the wait it burned*, and require
the arm to reach that state by running against a held beacon rather than by planting a file. Then S5
reports something that happens on the normal path instead of only in the misconfiguration case.

**Left-shift gate.** The arm that closes this is a `hit` on the queue clause reached by an
*end-to-end* fail-open: hold the beacon, run `--close` with a short override, assert the DoD text
names the wait. If the assertion can be satisfied without a beacon ever being held, it is grading a
fixture again. Pair it with a `miss` over an uncontended run, which is the real control.

---

# HIGHS

## H1 — S3's export has no precondition, and `GATE_BOUND` has a declared INERT state

*(raw ids 4, 27, 36)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §2 S3 and S4, §5 `error / empty /
loading states`, §6 AC4**

`run_bounded` applies `timeout -k 5s` only when `[ "$GATE_BOUND_LIVE" = 1 ] && [ "${GATE_BOUND:-0}"
-gt 0 ]` (`unattended.sh:188`), and `:218` announces the other case in as many words: *"this node has
no working 'timeout -k', so the `GATE_BOUND` wall-clock bound on `GATE_CMD` and `WIRING_CHECK` is
INERT; both run unbounded this session."* That state is not hypothetical — `TOOL-aBoundedCeiling-6`
armed it deliberately, and the same guard appears at three sites in the file (`:188`, `:1092`,
`:2851`).

S3 exports the derived value unconditionally. On such a node the close cuts its queue wait from
7200 s to 900 s to fit inside a deadline that cannot fire, then fails open and runs contended beside
the holder — pure cost, no benefit, on exactly the host class the kit already probes for and
announces. §4's whole argument ("the fail-open threshold sits OUTSIDE the deadline that kills the
process first") presumes a live deadline; §5's error-states line reaches S2 and S5 and never reaches
this one. AC4 asserts only that the child carries the value, never under which conditions it should
carry one at all.

One half of the raw finding is refuted and worth recording: `GATE_BOUND` cannot be absent or zero
here, because `unattended.sh:304-308` defaults an absent key and refuses a non-positive integer. The
derivation always runs over a validated positive integer. It is liveness, not validity, that S3 skips.

**Fix.** State the precondition in S3 with the same predicate `run_bounded` uses —
`[ "$GATE_BOUND_LIVE" = 1 ] && [ "${GATE_BOUND:-0}" -gt 0 ]` — and add an AC asserting the stub
`GATE_CMD` sees **no** `GATE_TURNSTILE_MAXWAIT` when the bound is inert. That is the control that
stops AC4 being unconditional, and it is the same shape as `TOOL-aBoundedCeiling-6`'s own AC4.

**Left-shift gate.** `unattended.test.sh` already has the fixture: force `GATE_BOUND_LIVE=0`, run the
close over a stub `GATE_CMD` that echoes its environment, and `miss` on the variable name. One arm,
and it also pins the INERT notice, which currently has one reader and no assertion tying it to
behaviour.

## H2 — `waited` is written once, at ~0, in exactly the scenario the unit exists for

*(raw ids 3, 23)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §2 S5, §6 AC5**

The status write at `:686` sits inside the announce guard at `:674`: `if [ "$pos" != "$ts_lastpos" ]
|| [ "$ts_announced" = 0 ]`, followed by `ts_lastpos=$pos; ts_announced=1`. With one holder and one
waiter — §4's own two-run case — the waiter's position is stable at 1, so the guard fires once and
never again. `TS_WAITED` at that first announce is the elapsed time of one failed acquire: zero or
one second.

So S5's promise to report "the waited seconds" hands the operator `waited 0` after a fifteen-minute
queue. That is worse than no number: it reads as "the queue was not the problem", which sends the
operator hunting a failing leg — the precise outcome S5 claims to prevent. AC5 requires the file to
"record a non-zero wait" and then plants it, so no criterion can observe that the shipped writer
cannot produce one.

The honest discriminator in today's code is the file's **presence**, not its `waited` field. Note
that this interacts with B3: after S3 the presence signal is gone too, so S5 currently keys on the
one field that does not move, in a state that no longer occurs.

**Fix.** Either add a scope item making the write unconditional per tick (refresh `waited` outside
the announce guard, keeping the position announcement itself guarded so the stderr line does not
become a spinner), or reword S5 and AC5 to report `waited` explicitly as a lower bound. Whichever is
chosen, AC5 must assert the reported seconds against a real wall-clock wait over a held beacon rather
than over a planted number.

**Left-shift gate.** An arm that holds position constant across several ticks and asserts the number
**grew** between two reads. It is three lines against a beacon the suite already knows how to hold,
and it is the only assertion that distinguishes a refreshed field from a frozen one.

## H3 — "It shortens a pathological wait and lengthens nothing" is false, and it is the sentence that prices the whole design

*(raw id 25)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §5 `perf / scale`, against §3's rejection of
`GATE_TURNSTILE=0`**

§4 measures run A's bar at ~1560 s. With `GATE_BOUND=3600`, S3's derivation gives a 900 s queue
bound. 900 < 1560, so run B **always** reaches the fail-open at `:665-668` while A is still running,
and proceeds "UNQUEUED alongside whatever holds the beacon" for A's remaining ~660 s. That is
contention on the normal path of every concurrent close — the same measured contention (width 24
running 26 % slower than width 8) that §3 gives as its reason for rejecting `GATE_TURNSTILE=0`. The
accepted design reintroduces a bounded slice of the rejected alternative and the spec asserts its
absence instead of pricing it.

§4's own arithmetic sharpens the point: today B needs 1560 + 1560 = 3120 s, inside 3600. So in the
median case B survives *without* this unit, and what the unit buys is the tail. After the change the
median case pays ~660 s of two-bar contention every time, which also lengthens A — and A is itself
under `GATE_BOUND`. This is not a new failure mode (the arithmetic still lands inside the bound on
both sides), which is why it is a high and not a blocker. It is a false justification on the one
sentence that decides whether `÷ 4` is the right ratio.

**This is the answer to "does deriving it as `GATE_BOUND / 4` hold".** It does not hold as argued.
The property that actually has to hold is `GATE_BOUND − maxwait > a CONTENDED full bar`, not
`> the uncontended 1560 s floor` — because a bar that fails open is by construction a contended bar.
At 3600 s and a 26 %-slower contended bar that is roughly 3600 − 900 = 2700 s of headroom against
~1970 s of work, which passes, but nothing in the spec says so and nothing re-derives it if either
number moves.

**Fix.** Replace the "lengthens nothing" line with the accepted outcome stated plainly: **bounded
concurrency, not serialization.** Quantify the overlap it admits (bar wall clock minus the queue
bound) and record the property that must hold, with the contended bar as the term. If `÷ 4` survives
that arithmetic, keep it and show the working; if the intent is that the queued bar usually *does*
acquire, the ratio has to be sized above the measured bar and the bound raised, which §3 has already
rejected — in which case say that the unit trades serialization for a deadline and stop claiming both.

**Left-shift gate.** Not gateable as a wall-clock property, and it should not be faked with a timing
arm — this repo has two open rows about load-sensitive turnstile arms already. The left-shift is a
checklist line in unit 6 §5 stating the residual explicitly, plus the `.unattended.conf` comment M1
below already owes, so the next reader sizing `GATE_BOUND` sees both bounds at once.

## H4 — Two units own `unattended.test.sh` again, and unit 6 needs the arms three orders before they land

*(raw ids 5, 14, 24, 37)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §4 Files touched and §6 AC5/AC6,
against `spec/…-TOOL-aUnblockedFleet-4.md` §2 S4c**

Unit 6's files table claims `tools/unattended/unattended.test.sh` ("an arm for the queue clause on a
bound kill") and its AC5/AC6 name that file explicitly. Unit 4's S4c, a Scope (IN) item, claims the
same two arms: "the driver arms cover `TOOL-aUnblockedFleet-6`'s two states as well". Unit 6 is
order 3; unit 4 is order 6.

This is the defect round 1 folded out of units 1 and 2 — unit 2's rev-2 log records dropping its
claim on `check-unattended.test.sh` and its files table now explicitly disclaims the file — and the
unit the fold created re-introduced it, in the direction that also inverts the order. Three
corroborating facts, each checked: unit 4's own files table for that file lists only "check-5 arm
rewritten; silence arm added", so not even unit 4's §4 carries S4c's arms; unit 4's AC1-AC7 contain
no criterion for S4c at all; and unit 1 §2 S5 states the build-wide absolute that unit 4 "owns every
test edit in this build", which unit 4's own carve-out for `run-gates.turnstile.test.sh` already
contradicts.

**Fix.** Pick one owner in one place. The cleaner split, given unit 6 is the Tier-2 unit whose
behaviour these grade: unit 6 keeps both suites' unit-6 arms, S4c is deleted from unit 4, and
`unattended.test.sh`'s unit-6 arms are named in unit 4's non-goals. Then amend unit 1 S5's "every
test edit" absolute to name the carve-out, so the build states its ownership rule once. The
alternative — move AC5/AC6 into unit 4 — requires re-ordering unit 4 ahead of unit 6, which drags the
whole landing order.

**Left-shift gate.** Mechanical and cheap: a records check that every file named in any spec's
Files-touched table is claimed by exactly one unit in the build, and that a file named by an AC is
claimed by that AC's own unit or by a unit at an earlier order. Both predicates are a few lines over
the spec set that `gen_build_index.py` already parses, and both would have red on this build twice
now.

## H5 — Unit 2's S7 and S6 got no acceptance criterion, so round 1's class fix is half applied

*(raw id 6)* · **`spec/…-TOOL-aUnblockedFleet-2.md` §2 S6 and S7, absent from §6**

Round 1's finding was that surviving in-code carriers of the removed singularity rule were invisible
to every unit's acceptance. Unit 3 folded its three carriers **with** a class-wide content grep
(AC6), written in its own words as "deliberately a CONTENT grep across the whole kit rather than a
line-numbered one". Unit 2 folded its one carrier **without** any criterion at all.

The carrier is real and still in the tree: `check-unattended.sh:716-717` reads *"Check 7 is `nlive <=
1`, which fires at TWO"*, which unit 2's S1 falsifies. Unit 2's AC1-AC6 cover exit 0, the report
text, the silent case, `EXCLUDED`, `UNAVAILABLE` and the full bar — none reads that block, and a
stale comment reds no gate. Unit 3's AC6 greps three alternates ("the bar reds on the second one",
"At most one run-state file may be non-terminal", "returns the run to check_single_live"); none of
them matches this block's text, and unit 3's S7 deliberately routes this fourth carrier to unit 2.
So the class-coverage instrument the build added in response to round 1 has a known member routed out
of it and into a unit with no observing criterion. S6's "states what it does NOT check" header
rewrite is unobserved for the same reason.

The file this lands in is the one unit 2's own §3 says becomes *more* load-bearing after the change.

**Fix.** Extend unit 3's AC6 grep to include a string from that block (`nlive <= 1` is the
distinctive one), or add an AC to unit 2 asserting the check-4 header no longer names check 7 as a
live refusal. One criterion covers both S6 and S7 if it greps for the stale claim rather than for the
new prose.

**Left-shift gate.** The grep itself is the gate — it belongs in the kit's own check as a content
assertion over `tools/unattended/`, not only in an AC that runs once. A rule that is removed from
behaviour and left in a comment is this build's most-repeated defect (four carriers across two units
in round 1, a fifth here), which makes it a class, not an instance.

---

# MEDIUMS

## M1 — S6 edits the one `GATE_BOUND` carrier an adopter never reads, and the copy they do read now gives wrong advice

*(raw ids 26, 38)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §2 S6 and §4 Files touched**

S6's stated rationale is that "an adopter reading that key must be able to see that it now sets a
second bound", and it then names `.unattended.conf` — this repository's own file, which no adopter
reads. `tools/unattended/.unattended.conf.example:27-33` is the adopter-facing copy, and its comment
says the bound applies to "GATE_CMD and WIRING_CHECK" and closes with: *"Set it ABOVE your slowest
legitimate bar. A bound that fires on a healthy run gets deleted."*

After this unit only three quarters of `GATE_BOUND` is available to the bar. An adopter following the
shipped sentence to the letter — bound just above the slowest bar — gets a queue bound at 25 % of it
and a run that fails open on every concurrent close, which is the outcome that sentence exists to
warn against. No unit's scope, files table or AC owns that file. Check 22 cannot help: its own header
says it grades "presence of the key name in the table region, nothing more", explicitly not that a
row describes its key correctly.

The raw finding's fourth-carrier claim is partly refuted and recorded as such: unit 3 does own the
protocol template row and its S4 re-render covers the render, so two of the four carriers are
handled. The example file is the one nobody owns.

**Fix.** Extend S6 and unit 6's files table to `tools/unattended/.unattended.conf.example`, and
rewrite its sizing sentence to state the residual rather than merely appending "a second bound now
exists" — an adopter needs the ratio, not the fact.

**Left-shift gate.** One AC greping the derivation text in both `.unattended.conf.example` and the
rendered `memory/guides/UNATTENDED-PROTOCOL.md`. Longer term, check 22 could grade that a key's
carriers agree on their *consumer list*, which is a diff between two comment blocks and is the only
thing that catches this class without a human reading both files.

## M2 — The protocol sentence is owned by no scope item and is cited to a scope item about a different file

*(raw ids 16, 31)* · **`spec/…-TOOL-aUnblockedFleet-3.md` §4 Files touched row 1, against §2, §6, and
unit 6 §5**

Unit 3's files table adds "the turnstile bound gains one sentence (unit 6 S6)" to
`tools/unattended/PROTOCOL.template.md`. Unit 3 §2 has no scope item for that edit (S1/S2 are the
singularity paragraph, S3/S7 the Skill, S4-S6 the renders and markers), §6's AC1-AC6 are greps for
**removed** strings plus parity and version checks, and unit 6's S6 is about `.unattended.conf`'s
comment, not the protocol. Meanwhile unit 6 §5's user-docs line defers to "unit 3's protocol edit".
Both specs point at the other for one content edit to a governance carrier.

Unit 3 declines a new arm on the grounds that check 10 covers the file. Check 10 byte-compares
template against render; it cannot see whether the sentence exists or whether it is right.

**Fix.** Give unit 3 its own S-item for the protocol sentence, cite unit 6 S3 (the derivation) rather
than S6 for the mechanism, and add an AC greping the derivation in both
`tools/unattended/PROTOCOL.template.md` and its render.

**Left-shift gate.** Same instrument as M1's, one file over: a positive content grep in an AC. This
build has now produced three edits whose only existence is a Files-touched table row, which suggests
the tables themselves want a records check — every row either maps to an S-item or is marked as a
mechanical consequence of one.

## M3 — The README still states the pre-fold verb census

*(raw id 18)* · **`memory/builds/aUnblockedFleet/README.md:19`, against
`spec/…-TOOL-aUnblockedFleet-1.md` §4**

The README's problem statement reads "All fourteen driver verbs take a `<slug>`" under the heading
"Measured before this folder was written". Unit 1's rev-2 §4 records the corrected census: the
dispatch `case` at `:4248-4261` lists fourteen, the population is seventeen (`VERBS_SLUG` fourteen at
`:86` plus `VERBS_INLINE` three at `:89`), of which sixteen take a slug and the seventeenth is
`--version`. That same paragraph names the README's sentence as the defect it was correcting.

Round 1's M1 was folded into one carrier and left in the other, so the build's front page — the first
document a resuming or reviewing session reads — states the wrong number for the measurement the
whole build rests on. The correction's own argument was that an assertion between two derived values
must not be typed twice; typing it twice is what survived.

**Fix.** Point the README paragraph at unit 1 §4 rather than restating the count. Unit 5 already owns
the README, so it lands as an S-item there.

**Left-shift gate.** None worth building for one number; the gate is the rule the charter already
states, and pointing instead of restating removes the carrier rather than checking it.

## M4 — `gate-queue-status` has no freshness rule, and the traps that matter leave it behind

*(raw id 40)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §2 S5, §6 AC5/AC6**

S5 reads the file with no assertion that it belongs to this invocation. The only removal is `:692`,
on the normal path out of the wait loop; the queued-phase signal traps at `:579-581` run
`ts_drop_ticket` and exit **without** touching it. So a bar TERM'd while queued — S5's own target
case — leaves the file in its worktree's git dir, where the next run in that same worktree will read
it. A later bound-kill that happened mid-legs then reports "the bar never STARTED": a confident wrong
diagnosis, which is worse than the "the bar never returned" wording S5 replaces. AC5 covers present
and AC6 covers absent; nothing covers stale.

One half of the raw finding is refuted and matters for the fix: the file is **not** repo-wide. It is
per-worktree (that is B1), so the cross-run contamination is between sequential runs in one worktree,
not between two concurrent closes in different ones.

**Fix.** S5 requires the driver to accept the file only when its mtime is at or after the
`run_bounded` invocation's start time, and to say the queue state was unreadable otherwise. Add a
stale arm: plant a status file older than the invocation and assert the message keeps its existing
wording. Note that B3's re-pointing may retire this finding entirely — evidence taken from `RB_OUT`
is this invocation's by construction, which is a second reason to prefer it.

**Left-shift gate.** If the file survives as the seam, `run-gates.sh` should remove it in the
queued-phase traps as well, and the suite should assert that a TERM'd queued bar leaves no
`gate-queue-status` behind. That converts a freshness rule the reader must remember into a lifecycle
the writer guarantees.

---

# LOW

## L1 — AC1 pins a 120-second wall-clock literal into a binding bar leg

*(raw id 41)* · **`spec/…-TOOL-aUnblockedFleet-6.md` §6 AC1, against §7**

AC1 sets `GATE_TURNSTILE_MAXWAIT=120` and grades "within ~120s", in
`run-gates.turnstile.test.sh`, which §7 names binding. The arm must actually burn the bound to
observe the expiry, so it adds two minutes of wall clock to a leg on every bar for an assertion a
four-second bound would give identically. Charter §7 prices cost as a verdict.

It is also the exact class two OPEN rows already record against this suite: `TOOL-aScannedThrottle-7`
("a fixed wall-clock bound on a box whose process creation moves 25x") and `TOOL-dSpentCeiling-8`
(run 1 redded `run-gates turnstile`, with the recorded candidate fix being "a declared timing budget
the arm REFUSES against"). The suite's own comment at `:282` states the house idiom for this
assertion: scale it through the same knob rather than pinning a second number.

**Fix.** Use a single-digit override in the arm and assert the **ordering** against a same-run
control — the expired notice arrives before the derived `TS_TTL * 4` could have elapsed — rather than
against a 120 s literal.

**Left-shift gate.** The `TOOL-dSpentCeiling-8` candidate fix, applied here: the arm declares its
timing budget and **refuses** rather than fails when the host is too loaded to distinguish the two
thresholds. A refusal that announces itself is a skip that cannot be misread as coverage.

---

# What was refuted, and what stands

Nineteen candidates did not survive. The recurring refuted shapes: objections to unit 6's §5 `N/A`
rows on a scheduling change (correct as written); several readings of the rejected alternatives in §4
as under-argued, which did not survive contact with the copy-install argument; claims that
`GATE_BOUND` could be absent or zero at the derivation (refuted at `unattended.sh:304-308`, which
defaults an absent key and refuses a non-positive one); and a claim that unit 6 §4 quotes the
per-worktree source comment (it does not — the comment is in `run-gates.sh`, and the spec's silence
about it is the defect, not a misquote).

**Three things stand and should not be lost in a re-spec.**

The unit's thesis is correct and round 1 was right to promote it. The turnstile really does serialize
concurrent closes, the queue wait really is charged inside `GATE_BOUND`, and `run-gates.sh` really
does hold a deliberate, tested fail-open path that the deadline makes unreachable. Making an existing
escape hatch reachable is a smaller and better fix than a retry, a handoff or a second scheduler, and
§4 argues that well.

The fail-open does exactly what §4 claims. `:665-668` drops the ticket, prints the reason with both
numbers, proceeds unqueued, and contributes nothing to the exit code. That half of the design needed
no repair, and B2's fix is deliberately scoped to leave it alone.

And the folds worked. Round 1's three blockers are closed, unit 3's AC6 is a genuinely better
instrument than the line-anchored greps it replaced, unit 4's S4b arms the one-competitor threshold
the build actually moves, and unit 2's files table now disclaims a file rather than quietly sharing
it. The defect that repeated — two units owning one file — repeated in the *new* unit, which is what
H4's left-shift gate exists to stop happening a third time.
