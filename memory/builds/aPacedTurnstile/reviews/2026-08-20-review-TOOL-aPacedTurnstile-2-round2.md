# Tier-2 re-review — TOOL-aPacedTurnstile-2, the fold of the closing review

**Range reviewed:** `d37c8a4049acbeb93d1f97f2f94565e95be91354...HEAD` (one commit, `2977316`).

**Serves:** diff-review TOOL-aPacedTurnstile-2

**Build:** aPacedTurnstile · **Date:** 2026-08-20 · **Tier:** 2 · **Streams:** tooling
**Judged against:** `memory/builds/aPacedTurnstile/reviews/2026-08-20-review-TOOL-aPacedTurnstile-2.md`
(B1, M1–M5, L1–L3) and the contract
`memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-2.md`, AC1–AC13.
**Governing invariant graded:** no knob may ever turn a leg into a PASS or a SKIP; a knob may cost
speed, and the timeout may convert an unbounded hang into a bounded RED naming its leg.

**Review shape:** raw 20 · confirmed 17 · refuted 3 · unverified 0 · precision 0.85. The 17 confirmed
reports collapse to **10 distinct defects** — four named the same cgroup-over-seam inversion, four the
same unescaped backtick, two the same elapsed-assertion noise floor, two the same `-k` probe gap.
Counts below are the distinct set: **2 blockers · 2 highs · 3 medium · 3 low**.

## Verdict: the fixes work; two of the new gates do not

Every folded finding closes on its own terms. B1's mechanism is genuinely repaired — I measured the
timed run's `sleeper` leg at 4-5 s against a 20 s fixture where the whole-bar wall clock used to be
identical with the knob on and off. M1's formula is gone from both shipping files, M3 warns and tags,
M4 refuses both halves, L2's indented comment is a comment. The invariant survived every attack again:
no path here produces a PASS or a SKIP, and every defect below costs a false RED or a wrong width.

What did not survive is the *new* machinery. Two of the arms this fold added to protect the merge bar
are themselves merge-bar defects — one reds a correct runner roughly one run in three, and one detects
a scratch-path collision and then performs every destructive write it just refused. Separately, M5's
cgroup source is applied on top of the `GATE_RAM_MB` seam, which hands the box the deciding vote back
in exactly the arms written so the box would not decide.

## Blockers

### R1 — arm 4h's elapsed assertion has a noise floor larger than its signal

`tools/run-gates/run-gates.test.sh:661` (merges raw 5, 17) · severity **high**, graded **BLOCKER**
because it reds a correct runner on a shipped merge-bar leg.

The assertion subtracts two WHOLE-RUN wall clocks:

```sh
t0=$(date +%s); o=$(runp GATE_PROFILES=fx/tbl-tight.txt); t_timed=$(( $(date +%s) - t0 ))
...
t0=$(date +%s); runp GATE_PROFILES=fx/tbl-loose.txt >/dev/null 2>&1; t_ctl=$(( $(date +%s) - t0 ))
[ "$(( t_ctl - t_timed ))" -ge 10 ]
```

Both terms carry the runner's entire fixed startup and reporting cost, so the fixture's ~17 s signal
rides a large, noisy constant with only 7 s of headroom. Measured on node `a` in this worktree:

| what | measurement |
|---|---|
| two instantly-exiting legs through the same runner | 19 s, 19 s — the constant |
| three timed/control pairs of arm 4h's own fixture | timed 28 / 20 / 12 s, control 40 / 31 / 32 s |
| resulting difference against the `-ge 10` threshold | 12 s, 11 s, 20 s — two pairs inside 2 s of RED |

The timed run alone swung 12 s to 28 s on identical input. That spread is the same order as the signal
the threshold is trying to see. Two independent reproductions in this round measured differences of
6, 8, 10 and -3 s under bar-shaped concurrent load, i.e. actual REDs — and this canary runs as one of
eight concurrent legs, which is the loaded case. The arm's own comment, "Load inflates both runs, so
the DIFFERENCE survives it", is false for sequential samples: only the overhead MEAN cancels, never
its jitter.

The timeout fired correctly in every run I made (`timed out after 3s` present each time), so the
failure message accuses the runner of the exact blocker this commit fixed.

**Fix.** Grade the LEG's clock, not the process tree's, using a number the runner already writes.
`$P/.git/gate-timings.tsv` holds a `sleeper` row per run — I measured 4.577 s timed against 21.703 s
untimed on the same fixture. Read that row after the timed run, run the control, read it again, and
assert the timed reading is far below the control's. That keeps the control design the by-design note
requires, excludes startup entirely, and adds no process. Read the file BETWEEN the runs; the control
overwrites the entry.

**Left-shift gate.** The rule this arm broke is already in §7 and needs no new gate, only applying:
a gate whose measurement includes a term it does not control is grading the node. State the margin in
the arm's comment as a ratio of signal to measured constant, so the next author who tightens the
fixture can see when the headroom has gone.

### R2 — the section-4 scratch guard prints REFUSING and then performs every write it refused

`tools/run-gates/run-gates.test.sh:497-500` (raw 2) · severity **high**, graded **BLOCKER** because
its damage lands in the repo under test.

```sh
if [ "$( cd "$P" && git rev-parse --show-toplevel ... )" = "$( cd "$ROOT" && git rev-parse ... )" ]; then
  echo "canary: REFUSING — the section-4 scratch $P resolves to the repo under test, ..."
  fail=1
fi
cp "$SCRATCH/tools/run-gates/run-gates.sh" "$P/tools/run-gates/run-gates.sh"
```

There is no `exit` between the guard and the writes, and the file runs under `set -u` alone (line 4) —
no `set -e`, and neither `echo` nor an assignment aborts. On the exact condition the guard detects,
these all still execute against the tree it just identified as the real repo: the two-leg fixture
`$P/tools/gate-legs.json` heredoc (:507), `git config user.email t@e && git config user.name t`
(:513), and later `rm -f "$P/shim/timeout"` (:760) and `rm -rf "$P/cg"` (:831). The guard's own comment
states the condition has been observed once with the cause unidentified, so the next occurrence is
annotated rather than prevented: the bar's real leg manifest is overwritten with a two-leg fixture and
the repo's local commit identity is rewritten to `t <t@e>`, which then attributes whatever is committed
next. `fail=1` reds the bar after the fact.

A guard that detects the corruption and then performs it is the §7 class this repo has already
left-shifted once.

**Fix.** Make the refusal a refusal: `exit 2` in place of `fail=1` (the message already explains why),
and move the guard above the `mkdir -p "$P/tools/run-gates" "$P/fx" "$P/shim"` at :489 so no directory
is created inside the real tree either.

**Left-shift gate.** A gov-only arm asserting the guard's own failing case: point `P` at `$ROOT` in a
subshell copy of the guard and assert it exits non-zero WITHOUT the fixture manifest appearing. Per §7
a new gate is not landed until its failing case has been observed, and this guard's has not been.

## High

### R3 — the cgroup cap is applied on top of the `GATE_RAM_MB` seam, so ambient container state overrides the operator

`tools/run-gates/run-gates.sh:206-211` (merges raw 1, 7, 9, 16).

`det_ram` returns early with `RAM_SRC="seam"` when `GATE_RAM_MB` is set (:183) precisely to signal a
bypass; `det_ram_capped` then MINs the cgroup limit into it anyway. Reproduced against the real runner
with the canary's own three-row fixture table:

```
GATE_CORES=16 GATE_RAM_MB=32000, no cgroup file
  gate profile: big    (cores 16 via seam, ram 32000 MB via seam; width 8, timeout off; detected)
GATE_CORES=16 GATE_RAM_MB=32000, GATE_CGROUP_ROOT holding a 2 GB memory.max
  gate profile: small  (cores 16 via seam, ram 2048 MB via seam,cgroup; width 4, timeout off; detected)
GATE_CORES=0 GATE_RAM_MB=0, same cgroup root
  gate profile: any    (cores ? via seam, ram 2048 MB via seam,cgroup; width 2, ...; detection failed)
```

Three consequences, in order of cost.

- Shipped canary arm 4a (:529) is byte-for-byte that first invocation and asserts `big`; arm 4b (:536)
  is its sibling at 8000 MB. Neither sets `GATE_CGROUP_ROOT`, so both read the real `/sys/fs/cgroup`.
  Inside any memory-capped container under the fixture's 24000 MB threshold the SHIPPED canary reds,
  with a message blaming row selection — in the environment M5 was written for and the one AGENTS.md
  records the bar as scheduled to move to. `README.md:32` promises "every assertion here is true in
  any tree". Latent on all four registered nodes, which are Windows.
- `README.md:31`, added by this same commit, says `GATE_CORES` / `GATE_RAM_MB` "override the readings".
  That is now false for RAM, and the canary's own comment at :712 says the same thing ("the
  GATE_CORES/GATE_RAM_MB seams BYPASS detection"). Three carriers, one of them the code's own early
  return, now state something the runner does not do — and the operator's only escape hatch when the
  cgroup reading is wrong is disabled, since a seam can no longer raise a number.
- The deliberate zero — `GATE_RAM_MB=0`, the UNKNOWN state arm 4c grades — is REPLACED rather than
  min'd, because :210 takes the limit whenever `DET_RAM` is 0. Arm 4c survives only because its
  `GATE_CORES=0` half still forces the `detection failed` tag.

The block's own justification does not cover this: it argues the MIN because "Every source above
reports HOST physical memory". A seam is not a host source, and `det_cores` has no analogous cap, so
the two seams behave differently.

**Fix.** One line, after the `det_ram` call in `det_ram_capped`:
`[ "$RAM_SRC" = seam ] && return 0`. The container guard still covers every genuinely detected reading.
(Pinning `GATE_CGROUP_ROOT` to a nonexistent path inside `runp` would hide the canary symptom and leave
the override silently re-decided by the host.)

**Left-shift gate.** A fourth 4q fixture setting `GATE_RAM_MB` and `GATE_CGROUP_ROOT` together and
asserting the visibility line reports the seam value with no `cgroup` in `RAM_SRC` — plus the same
assertion for `GATE_RAM_MB=0` staying UNKNOWN. That gates the precedence rule itself rather than the
one arm that trips over it.

### R4 — the INERT probe does not exercise the option the timed invocation uses

`tools/run-gates/run-gates.sh:299` and `tools/run-gates/run-gates.test.sh:600` (merges raw 6, 19).
Raised from the finders' medium: I reproduced a whole-bar RED produced by a knob, which is the same
false-RED class as R3 and the direct inversion of the contract stated three lines above the probe.

The probe runs `timeout 1 true`; B1's fix changed the leg invocation to `timeout -k 5s "$PROF_TIMEOUT"`
(:398). A `timeout` that runs but does not accept `-k` therefore passes the probe, is never declared
INERT, and fails every timed leg on argument parsing. Reproduced with a PATH shim that accepts
`timeout 1 true` and rejects `-k`:

```
gate profile: tight  (cores 16 via nproc, ram 32692 MB via getconf; width 2, timeout 3s; detected)
GATE FAIL  one  (exit 125)
    timeout: invalid option -- k
gates RED — 1/1 legs failed
```

That is "a knob the operator set and the host cannot honour is worse than no knob" — the sentence at
:297-298 — inverted into a bar that reds. Arm 4m cannot catch it: its shim exits 127 for every
invocation, so it drives total absence and not partial support. The canary's `HAVE_TIMEOUT` probe at
:600 has the identical gap, so such a host takes the asserting branch of 4g/4h and blames the runner.
Latent for adopters while every shipped row sets `timeout=0`, but the shipped canary itself sets
`timeout=3` (:629) — exactly the latency B1 had. Host class is narrow but real: BusyBox `timeout`
before 1.30 has no `-k`.

**Fix.** Probe the invocation actually used, in both files: `timeout -k 1s 1 true`.

**Left-shift gate.** Extend arm 4m with a second shim that accepts a bare `timeout N cmd` and rejects
`-k`, asserting the runner announces INERT and completes GREEN. That is the arm that grades the
degradation contract for the option set the runner really passes.

## Medium

### R5 — `-k` exits 137, and only 124 gets the timeout tail

`tools/run-gates/run-gates.sh:436` (raw 10).

Measured on node `a`, GNU coreutils 8.32: `timeout -k 1s 1 bash -c 'trap "" TERM; sleep 6'` returns
137, while a TERM-dying child returns 124. `report_one`'s predicate is
`{ [ "$rc" = 124 ] && [ "$PROF_TIMEOUT" -gt 0 ]; }`, so the one case `-k` was added for — its own
comment at :397 says "`-k` follows for the child that ignores SIGTERM" — reports as

```
GATE FAIL  stubborn  (exit 137)
gates RED — 1/1 legs failed
```

with no mention of a timeout at all. 137 reads as an OOM kill everywhere, so the operator is pointed
at memory instead of at the budget they set. The verdict stays RED and the invariant holds, but the
tail contract AC8 and arm 4h grade does not cover the new branch — and nothing drives it: arm 4h's
sleeper fixture (:506) dies on TERM, so `-k` never fires in any arm.

**Fix.** Widen the mapping, keeping the `PROF_TIMEOUT` guard so a leg that chooses 137 itself is
unaffected: `{ { [ "$rc" = 124 ] || [ "$rc" = 137 ]; } && [ "$PROF_TIMEOUT" -gt 0 ]; } && ftail="(timed out after ${PROF_TIMEOUT}s, killed)"`.

**Left-shift gate.** A second fixture leg in arm 4h that installs `trap "" TERM` before its sleep and
asserts the timeout tail. It is the only thing that would exercise `-k` at all.

### R6 — arm 4q never reads the cgroup v1 path, and drives v1's sentinel through the v2 filename

`tools/run-gates/run-gates.test.sh:814, 821, 826` (raw 14).

`cgroup_ram_mb` walks two sources (:168): `$CGROUP_ROOT/memory.max` and
`$CGROUP_ROOT/memory/memory.limit_in_bytes`. All three 4q fixtures write only `$P/cg/memory.max` —
including the one commented "v1's sentinel" — so the v1 element is only ever reached by its `[ -r ]`
guard failing. I confirmed the v1 branch does work today (a `memory/memory.limit_in_bytes` fixture
returns 2048), so this is a coverage gap and not a live bug: a typo in that filename, or a v1-only
reading failing for an unrelated reason, is invisible to the canary. v1 is the branch that matters on
the older CI images this source was added for, and the sentinel assertion proves `num_ok`'s bound, not
that the file it belongs to is ever opened. This is fixture-passes-by-finding-nothing, one arm over
from where the fold just closed it.

**Fix.** Add a fourth 4q fixture writing a small value to `$P/cg/memory/memory.limit_in_bytes` with no
`memory.max` present, asserting the visibility line names `cgroup`; and move the
`9223372036854771712` sentinel fixture to that same v1 file, where it actually occurs.

**Left-shift gate.** The fixture above IS the gate. Assert both sources in the same loop shape the
function uses, so a source added later without an arm is visibly the odd one out.

### R7 — AC8 still grades the message, and still names a timeout the arm no longer sets

`memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-2.md:205` (raw 15). Raised
from low: this is the criterion that let the blocker land, and the fold revved the spec without
repairing it.

AC8 reads "When a fixture row sets a one-second timeout and a fixture leg sleeps past it, the runner
reports that leg FAILED with a timeout tail and the overall verdict is RED". The arm now writes
`tight\t0\t0\twidth=2,timeout=3` (:629) and adds the elapsed-vs-control assertion. Meanwhile the
spec's own rev-6 entry (:296) states the blocker was the timeout "bounding the verdict and not the
clock, which the acceptance criteria could not see because AC8 graded the message" — the fold named
the AC as the blind spot and then repaired only the code. As written, a future builder can delete the
elapsed assertion and AC8 stays green: the same could-not-fail shape the blocker had. This spec sets
its own counter-precedent — rev-4/AC11b was added because a defect had been RELOCATED by its fix, so
the criterion was repaired rather than left to the code.

**Fix.** Rev AC8 to the property the arm now grades: a fixture leg that outlives the row's timeout is
reported FAILED with a timeout tail, the verdict is RED, AND the run's leg time is materially shorter
than an untimed control over the same fixture. Drop the one-second literal or match it to the fixture.
Fold R1's measurement change into the same rev.

**Left-shift gate.** Documented check, no gate: when a fix changes what an arm asserts, the AC it
serves is part of the same commit. The build already has the sweep habit from round 4 of unit 1 —
extend it from literals to acceptance criteria.

## Low

### R8 — arm 4h's SKIP message runs `timeout` instead of naming it

`tools/run-gates/run-gates.test.sh:664` (merges raw 4, 8, 12, 18).

`cat -A` confirms bare backticks around `timeout` inside a double-quoted `echo`, so the shell runs a
command substitution. The sibling skip at :613 escapes them correctly (`\`timeout\``) — one commit,
one sentence, two spellings. The branch fires only when `timeout 1 true` already failed, which is
exactly where the substitution misfires: the line renders as "no working  on this host", with either
`timeout: command not found` or a usage dump landing in the canary's output. The loud counted skip is
the entire compensating control the fold added for M2, and it deletes its own subject at the moment it
fires, against §7's rule that a skip must announce what went unexercised.

**Fix.** Escape both backticks as :613 does, or drop them.

**Left-shift gate.** None worth building for one character. If a class gate is ever wanted, it belongs
with the repo's shell-hygiene scans (the PowerShell scan's sibling), not in this kit.

### R9 — a dead `local` in `det_ram`

`tools/run-gates/run-gates.sh:181`.

`local pages pgsz kb v lim` — `lim` is assigned and read only at :209-211 inside `det_ram_capped`,
which declares its own at :208. `det_ram`'s body never touches it, and since `det_ram_capped` calls
`det_ram` before its own declaration there is no dynamic-scoping interaction either way. Reader cost
and a future-edit hazard, not behaviour.

**Fix.** Drop `lim` from the list.

### R10 — the new knob is documented nowhere

`tools/run-gates/gate-profiles.txt:28` and `tools/run-gates/README.md:31`.

`GATE_CGROUP_ROOT` appears in exactly two tracked files, both of them code: the runner and the canary.
The OVERRIDES block in `gate-profiles.txt` still lists only `GATE_PROFILE` and `GATE_PROFILES` — the
prior review's M5 noted `GATE_CORES` / `GATE_RAM_MB` were missing from it too, and the fold added them
to the README only. So the file that owns the knobs documents two of five.

**Fix.** Add `GATE_CORES`, `GATE_RAM_MB` and `GATE_CGROUP_ROOT` to the OVERRIDES block, and
`GATE_CGROUP_ROOT` to the README's `gate-profiles.txt` row beside the seams. Fix R3 first — as it
stands the true sentence for RAM is not the one either file wants to carry.

**Left-shift gate.** An arm asserting every `GATE_*` name the runner reads appears in
`gate-profiles.txt`, derived by grepping the runner rather than from a typed list. That is the shape
this kit already uses for the pinned knob set, applied to the environment knobs.

## Did each folded finding close?

| folded | closes? | residual |
|---|---|---|
| **B1** — timeout bounds the clock | **yes** | leg time measured 4.577 s against a 20 s fixture; but its gate is R1, its AC is R7, its probe is R4, its `-k` tail is R5 |
| **M1** — stale `min(8, nproc)` | **yes** | `git grep 'min(8'` returns only the two gate predicates and the gov canary; arm 4l asserts both files and both halves |
| **M2** — arms assert on an INERT host | **partly** | `HAVE_TIMEOUT` gating and counted skips are right; arm 4m drives absence only (R4), and the skip line is broken (R8) |
| **M3** — dropped `GATE_PROFILE` | **yes** | warned on stderr and tagged on the visibility line; arm 4n asserts the tag and GREEN |
| **M4** — unbounded declared values | **yes** | arm 4o drives both halves, exit 2 with `file:line` |
| **M5** — cgroup blind | **partly** | the source works and is seamed; precedence over the seam is wrong (R3) and v1 is uncovered (R6) |
| **L2** — indented comment | **yes** | runner strips leading blanks; arm 4p covers the comment and the whitespace-only line |
| **L1 / L3** — records | **yes** | spec-2 rev-6 recuts the non-goal at content, spec-3's editor map is corrected, and the timeout claim is repaired in `gate-profiles.txt` and the map dossier |

The assertion floor moved 65 → 86 with the new arms, so the added arms cannot silently stop executing.

## The three hunted classes

- **fixture-passes-by-finding-nothing** — found twice, both in arms added by this fold. Arm 4q's v1
  source is never opened (R6), and arm 4m's shim cannot see the partial-support host its own subject
  has (R4). The class did not recur in the same place; it moved one arm over, which is what it did
  last round too.
- **two-answers-to-one-question** — found three times. `README.md:31` and the canary comment at :712
  against what `det_ram_capped` does (R3); AC8 against arm 4h (R7); `\`timeout\`` at :613 against
  `` `timeout` `` at :664 (R8).
- **heredoc-escape-reaches-the-regex** — found once, and it is R8: an escape that does not reach a
  regex but does reach the shell, in a message. The new fixture tables are still written with
  `printf` and single-quoted formats, and the leg-manifest heredocs use quoted delimiters, so nothing
  expands into a pattern. Reported as a clean scan of a small surface, not as coverage.

## Landing order

1. R1 and R2 before this lands anywhere — both are merge-bar defects in code this commit added.
2. R3 with them if the fold is going out to adopters; it is one line and it reds their canary.
3. R4, R5, R6, R7 as one follow-up; each is a line of code plus an arm, and R7 is the record.
4. R8, R9, R10 whenever the file is next open.

**What I did not verify.** I did not run the full canary end to end — measurements above are against
the real runner in a scratch fixture built the way section 4 builds its own. R3's container symptom is
reproduced through the `GATE_CGROUP_ROOT` seam, not inside an actual container; all four registered
nodes are Windows, so no node here can run that case natively.
