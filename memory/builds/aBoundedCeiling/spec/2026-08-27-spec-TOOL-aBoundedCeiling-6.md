# TOOL-aBoundedCeiling-6 — the close's gate run cannot outlive a declared bound

**Status:** OPEN · rev-3 · 2026-08-27 · node a · Tier-2 · base 1d83cc94 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md](../build/2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md) | research | TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 |
| [2026-08-27-prompt-TOOL-aBoundedCeiling-1.md](../prompts/2026-08-27-prompt-TOOL-aBoundedCeiling-1.md) | research | TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 |
| [2026-08-27-review-TOOL-aBoundedCeiling-1-diff-review-round1.md](../reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-diff-review-round1.md) | diff-review | TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 |
| [2026-08-27-review-TOOL-aBoundedCeiling-1-diff-review-round2.md](../reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-diff-review-round2.md) | diff-review | TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 |
| [2026-08-27-review-TOOL-aBoundedCeiling-1-round1.md](../reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-round1.md) | spec-audit | TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 |
| [2026-08-27-review-TOOL-aBoundedCeiling-1-round2.md](../reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-round2.md) | spec-audit | TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 |

<!-- /gen:spec-records -->

## 1. Goal

Put a wall-clock bound on every project-declared command `tools/unattended/unattended.sh` runs, so
an unattended run can no longer wait forever on one that will never return. Two seams qualify today
and both are unbounded: `$GATE_CMD` in the `gates-green` Definition-of-Done item, which is where a
`--close` waits, and `$WIRING_CHECK` in `check_wiring`, which is where a `--preflight` waits. This is the only unit of this build that protects an adopter whose gate
command is not `tools/run-gates/run-gates.sh`, and it is the one that would have ended the hang
recorded in
[the live observation](../build/2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md).

## 2. Scope (IN)

- **S1** — `.unattended.conf` gains `GATE_BOUND`, seconds: the wall-clock bound on ANY
  project-declared command this driver runs, which today is `$GATE_CMD` in the `gates-green` DoD arm
  and `$WIRING_CHECK` in `check_wiring`. One key for both, because they are the same question — how
  long may a command this project named be allowed to not return — and a second number would be a
  second thing to set and forget.
- **S2** — ONE bounded-run helper in `unattended.sh`, applied at BOTH unbounded command seams in
  that file: the `gates-green` arm of `dod_met` running `$GATE_CMD`, and `check_wiring` running
  `$WIRING_CHECK`. Each runs under `timeout -k`, capturing to a FILE and never through a command
  substitution. One function, two call sites — which is the lazier diff AND the one that does not
  reproduce the class the target line's own comment records: *"Sibling of the seam check_wiring
  already uses for $WIRING_CHECK -- TOOL-aBranchedMandate-2 fixed that call site and did not grep for
  this one."* Bounding one of two siblings for a second time would be that defect, third instance.
  It also closes `TOOL-aPromptedMandate-9`, which measured `check-wiring.sh --check` at 1m22s and
  concluded that nothing in the driver's precondition chain has a timeout.
- **S3** — a breach makes the item UNMET and says so, naming the bound and the elapsed time. It is
  never a pass, and it is never silently indistinguishable from a red bar.
- **S4** — an announced default when the project declares nothing, so an adopter who has never heard
  of the key is still bounded, and is told which number bounded them.
- **S5** — a liveness line when `timeout` will not run on the host, exactly as the driver already
  emits for its bounded remote observation.

## 3. Non-goals (OUT)

- **N1** — `.githooks/pre-push` is not bounded here. It runs the bar at the push boundary and is a
  different kit with a different owner. Every unbounded seam INSIDE `unattended.sh` is in scope, which
  is S2's widening: rev-1 scoped only `$GATE_CMD` and left `$WIRING_CHECK` unbounded one function
  away, which is the fix-one-call-site class this repo has already recorded twice.
- **N2** — nothing kills a process this driver did not start. An orphan whose parent is already gone
  is outside this unit and outside this run's mandate.
- **N3** — the bound is not a per-leg ceiling and does not replace one. `TOOL-aBoundedCeiling-1`
  bounds each leg of gov's runner; this bounds the whole invocation of whatever command a project
  declares, gate runner or wiring check alike. A project can have both, one, or neither.

## 4. Design

### The defect, in the four lines that hold it

`unattended.sh`'s `gates-green` arm reads:

```sh
DOD_OUT=""
[ -n "$GATE_CMD" ] || return 1
DOD_OUT=$($GATE_CMD 2>&1) && { DOD_OUT=""; return 0; }
return 1
```

There is no bound of any kind. Whatever the project declares runs until it returns, and if it never
returns, `--close` never returns. The observation record measures that at three hours and nineteen
minutes with the launching session already dead, in a tree whose `GATE_CMD` is `scripts/gate.sh` —
a runner gov does not ship and cannot reach.

### The trap this unit must not walk into

Wrapping that line in `timeout` and leaving the `$( )` would reproduce
`memory/gotchas/bounded-through-a-pipe-is-unbounded.md` exactly, at the third site. The substitution
reads until EOF, EOF arrives when the last inherited write end closes, and a surviving grandchild
holds it — so `timeout` reports 124 on schedule while the caller blocks for the entire hang. That
gotcha records the identical mistake being made twice in this repo days apart, once in
`run-gates.sh` and once in this very driver.

The fix is the one that file already uses for its bounded remote observation: redirect to a file,
let `timeout` return, then read the file, with `-k` for the child that ignores `SIGTERM`.

### Why the default is a number and not "unbounded"

`.unattended.conf` has precedent in both directions. `HALT_FLOOR` refuses when undeclared, because
"a pin that quietly defaults is a pin nobody set". `LANDER_MARKER` treats empty as "the observation
is simply not asked for", so an adopter is not wedged by a key they have never heard of.

Neither is right here, and the reason is that this pin measures something different from both. A
FLOOR exists to detect shrinkage, and a silent default defeats it. A wall-clock bound exists to stop
an unbounded wait, and **any finite default is strictly better than infinity** — including for the
adopter who never edits their conf, which is the population that produced the observed hang.

So: a declared default, applied when the project says nothing, and ANNOUNCED on stderr whenever it
is the default rather than a project's own value. Defaulted, never silent. Making the key REQUIRED
was rejected because `--preflight` refuses on a missing required key, so a required `GATE_BOUND`
would refuse every adopter's next run over a field their conf cannot have.

### Choosing the default

The bound must clear the slowest legitimate bar by a wide margin, because a bound that fires on a
healthy run is a bound that gets removed. Gov's own full bar with self-tests is roughly 9700 seconds
of leg-sum with a 1320-second longest leg, which is about 26 minutes of wall clock at width 8 and
was measured at 4926 seconds of leg-sum before the self-tests moved off. A default of one hour sits
above every recorded gov bar and far below the three hours and nineteen minutes actually observed.

That number is a declaration and not a law: a project whose bar legitimately runs longer raises it
in its own conf, with the reason beside it, which is the same discipline every other pin in that
file carries.

The same hour covers the preflight's wiring check, and sizing it against the bar is what makes that
safe rather than sloppy: `TOOL-aPromptedMandate-9` measured `check-wiring.sh --check` at 1m22s under
load, which is two orders of magnitude inside a bound sized for a full merge bar. A check that needs
more than an hour to answer whether a hook is wired has failed in a way a tighter number would only
have hidden.

### Inventory

| site | change |
|---|---|
| `.unattended.conf` | `GATE_BOUND`, with its derivation in the comment |
| `tools/unattended/.unattended.conf.example` | the same key with its default — check 22 reds without it |
| `tools/unattended/PROTOCOL.template.md` | the key joins the declared-key table |
| `memory/guides/UNATTENDED-PROTOCOL.md` | RE-RENDER in the same commit — check 10 byte-diffs the pair |
| `unattended.sh` conf defaults (~:212) | `GATE_BOUND` beside `GATE_CMD` |
| `unattended.sh` the new bounded-run helper | `timeout -k`, file capture, elapsed, breach message |
| `unattended.sh` `dod_met` `gates-green` (~:2695) | call site one |
| `unattended.sh` `check_wiring` (~:988) | call site two, closing `TOOL-aPromptedMandate-9` |
| `unattended.sh` liveness (~:143) | the existing `timeout` probe covers this bound too |
| `tools/unattended/SKILL.template.md` | the close section's sentence about the bound |
| `.claude/skills/unattended/SKILL.md` | RE-RENDER in the same commit, `bash tools/unattended/adopt-unattended.sh` |

`tools/unattended/check-unattended.sh` takes NO edit. It is absent from the table on purpose: its
check 22 joins the kit's example conf against the rendered protocol and its check 10 byte-diffs the
template against that render, so the files it reads are edited above. rev-1 listed it as an edit
site, which would have led a builder to the required-key loop — exactly the "make it required" move
§4 rejects.

**Three template-and-render PAIRS are in that table and each is its own bar leg.** The protocol pair,
the conf example against the protocol, and the Skill pair. Edit either half of any pair without the
other and a leg reds on every bar, because all three legs are `subject: repo` and unguarded. The
Skill pair is the one an earlier revision walked past while promising the sentence in §5.

### Alternatives rejected

**Bound it in the project's `GATE_CMD` string** — declare `GATE_CMD="timeout 3600 bash ..."`. It
puts the fix in every adopter's hands separately, none of them will do it, and the driver expands
`$GATE_CMD` unquoted so the wrapper's own failure modes become the project's to debug. It also
cannot capture to a file, so it lands squarely in the gotcha above.

**Bound the whole `--close` verb.** Too coarse. `--close` also writes records and stages them, and a
bound that kills it mid-write leaves a run-state file nobody can resume.

## 5. Production-readiness checklist

- **security** — no new trust boundary. `$GATE_CMD` is already expanded by this driver; this only
  limits how long the same command may run.
- **perf/scale** — one `timeout` process per close. Immaterial against a bar measured in minutes.
- **observability** — a breach names the bound and the elapsed time: in the DoD output the close
  already prints for `$GATE_CMD`, and in the preflight refusal for `$WIRING_CHECK`. The defaulted case
  announces itself on stderr.
- **risks** — a bound set below a project's real bar blocks its landings. Priced by a one-hour
  default derived above, and by the key being a project declaration.
- **testing + left-shift gates** — AC1 through AC5 in `tools/unattended/unattended.test.sh`, with
  AC1 and AC5 measuring ELAPSED time, because the message was always the correct half of this defect.
- **migration / rollback** — removing `GATE_BOUND` from a conf restores the announced default;
  removing the wrapper restores today's unbounded behaviour.
- **user docs** — the rendered Skill's close section gains one sentence, and the protocol's declared
  key table gains the row.

## 6. Acceptance criteria

- **AC1** — When `GATE_BOUND=2` and `GATE_CMD` is a script that sleeps 30, `--close` reports
  `gates-green` UNMET naming the bound, and the VERB returns in seconds — asserted as elapsed time
  in `unattended.test.sh`, never as a message.
- **AC2** — When that same `GATE_CMD` backgrounds a grandchild that outlives it, AC1's elapsed
  assertion still holds, which is the arm that distinguishes a real bound from
  `bounded-through-a-pipe-is-unbounded`.
- **AC3** — When a conf declares no `GATE_BOUND`, `--close` still bounds the run at the announced
  default and prints which number it used, observed on stderr.
- **AC4** — When `timeout` will not run on the host, `--close` prints that the bound is INERT and
  the gate still runs, with the item's verdict unchanged against a control.
- **AC5** — When `$WIRING_CHECK` is a script that sleeps past the bound, `--preflight` refuses in
  seconds naming the bound, asserted as elapsed time. Without this the helper has one exercised call
  site and one asserted only by inspection, which is how the sibling seam went unbounded the first
  time.

## 7. Gates

`bash tools/run-gates/run-gates.sh` for two legs this unit's edits reach directly and that run on
every bar: `unattended kit gate`, whose checks 22 and 10 read the conf example and the rendered
protocol, and `unattended skill wiring`, which re-renders the Skill template and diffs it against the
tracked render. Plus `bash tools/unattended/run-unattended-gates.sh --selftests`, which is where
`unattended.test.sh` lives and is the only thing that runs it, since that suite is deliberately not a
bar leg.

## 8. Open questions

- **F1 — the default's value.** One hour, against thirty minutes which is nearer gov's own worst
  measured bar. RESOLVED (agent, 2026-08-27, delegated): one hour. Thirty minutes is inside the
  spread of a single gov bar under the ambient load this node demonstrably has, and
  `memory/gotchas/process-creation-is-the-suite-cost.md` states the consequence — a ceiling that
  reds on someone else's scan gets ignored, which is worse than not having one.
- **F2 — whether a breach should ABORT the run rather than leave the item unmet.** RESOLVED (agent,
  2026-08-27, delegated): unmet. An unmet DoD item is already terminal for a close and leaves a
  record an owner can read and an operator can override deliberately; an abort would discard the
  distinction between a gate that failed and a gate that never answered, which is the whole
  information this unit adds.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft, forced by a live three-hour `--close` hang observed on node
  `a` while the other two units of this build were being specced.
- rev-3 · 2026-08-27 · folded the round-2 spec audit. Widened S1, N3 and §1 to the definition S2
  had already outgrown — the key bounds any project-declared command this driver runs, not just the
  gate one — since the narrow wording was routed straight into the conf comment and the protocol's
  declared-key table and would have shipped to every adopter. Added the Skill template-and-render
  pair to the Inventory and `unattended skill wiring` to §7, without which §5's own user-docs promise
  reds a leg on every bar. Re-routed §5 to cover AC5.
- rev-2 · 2026-08-27 · folded the round-1 spec audit. Widened S2 from one call site to a helper at
  both unbounded seams in the file, which closes `TOOL-aPromptedMandate-9` and avoids repeating the
  fix-one-sibling class the target line's own comment records. Added the conf EXAMPLE and the
  protocol RE-RENDER to the Inventory, without which this unit reds its own gate twice, and removed
  `check-unattended.sh` as an edit site. Added AC5 so the second call site is exercised.

## 10. Reuse audit

**The seam is in the same file and this unit is its second instance.** `unattended.sh` already
bounds its remote observation with exactly the shape this needs: a declared `REMOTE_BOUND`, a
`REMOTE_BOUND_LIVE` probe that RUNS `timeout -k 1s 1 true` rather than testing for the binary, a
stderr line when the bound is inert, and a capture through a file rather than a substitution. Its own
header records why the file capture is there — a command substitution around `timeout` waits on the
last inherited write end while `timeout` reports success on schedule.

So this unit adds no mechanism. It applies an existing, argued, in-file mechanism to the one caller
that was left out of it, which is the caller the owner's prompt names.

`python tools/codebase-map/reuse_lookup.py "a wall-clock ceiling per gate leg, enforced by the
runner, that turns a hang into a red verdict"` returned `.unattended.conf` [unattended] as its
top affordance seam, which is the declaration site this unit extends.

Recall terms used: `leg ceiling timeout deadline hang wedge selftest guard bar budget verdict spawn
profile runner`. The decisive return was
`memory/gotchas/bounded-through-a-pipe-is-unbounded.md`, which names this driver as one of the two
places the class has bitten and states that its remote-observation fix was caught before shipping by
the recall probe the build method requires — the same probe, on the same file, one caller over.

**The sibling seam, which rev-1 missed and the audit named.** `unattended.sh:988` is
`wout=$($WIRING_CHECK 2>&1) && return 0` — the same unbounded substitution over the same kind of
project-declared command, one function away from the line this unit was written about, and already
measured OPEN as `TOOL-aPromptedMandate-9`. The target line's own comment predicted this exact miss.
S2 now covers both, which is why this unit gets smaller rather than larger by fixing the class.

**Where a hit was STALE.** None. Every claim about `dod_met`, `REMOTE_BOUND` and the conf key set was
read from `tools/unattended/unattended.sh` at writing time rather than taken from a record.
