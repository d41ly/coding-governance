---
slug: aPacedTurnstile
node: a
opened: 2026-08-18
streams: tooling
roster: TOOL
ids: TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 TOOL-aPacedTurnstile-8 TOOL-aPacedTurnstile-9 TOOL-aPacedTurnstile-10 TOOL-aPacedTurnstile-11 TOOL-aPacedTurnstile-12 TOOL-aPacedTurnstile-13 TOOL-aPacedTurnstile-14 TOOL-aPacedTurnstile-15 TOOL-aPacedTurnstile-16
---

# aPacedTurnstile — the merge bar gets an execution discipline

Node `a` · opened 2026-08-18 · streams tooling.

`tools/run-gates.sh` runs every leg it is given, at a width it picks from core count alone, in one
undifferentiated batch, with no knowledge of any other bar running on the same machine and no memory
of what the last run proved. That was survivable at 47 legs. At 70 it is not.

## The measurement this build starts from

Node `a` (16 cores / 32 GB), commit `6517579`, three runs of the existing runner:

| run | wall | legs | sum of leg durations |
|---|---:|---|---:|
| full bar, `GATE_FULL=1` — what `.githooks/pre-push` runs | **873 s** | 70 ran, 0 skipped | 4018 s |
| guard-scoped, typical mixed diff | **283 s** | 47 ran, 23 skipped | 1676 s |
| pure-records, every guard skips | **62 s** | 28 ran, 42 skipped | 262 s |

### Re-measured 2026-08-20 at `43a6c13`, and the shape changed

The table above is the 2026-08-18 ground. It is superseded. `TOOL-aMeteredTurnstile-1` shipped
`tools/run-gates/profile_bar.py` — an instrument that records a run as a RUN and names its regime —
and the re-scope ran it on a QUIET node `a`:

| | `6517579`, 2026-08-18 | `43a6c13`, 2026-08-20 |
|---|---:|---:|
| legs | 70 | **86** (50 guarded, 36 unguarded) |
| wall observed | 873 s | **1033.2 s** |
| total leg work | 4018 s | **4614.6 s** |
| floor — the longest leg | 659.9 s | **836.5 s**, 81 % of wall |
| throughput bound, work / width 8 | 502 s | **576.8 s** |
| regime | floor | **floor**, packing 1.24x |

The instrument states the consequence itself, and it is arithmetic about any bounded-pool bar rather
than an opinion about this one: *"Widening the pool and trimming small legs both buy ZERO. Only
making that leg cheaper, sharding it, or removing it from the critical path moves this number."*

**Do not cite `<git-dir>/gate-timings.tsv` as a measurement.** It is last-write-wins across runs and
never evicts a renamed leg. Measured on this node while four concurrent bars were running, it held
the floor leg at 1252 s and a total of 7625 s — inflated by 1.5x to 2x against the quiet-machine
truth above. Cite the `profile_bar` record, which carries its own envelope, or re-run the instrument.

Four facts follow, and the whole build is shaped by them.

**The bar is floor-bound by one leg.** `unattended driver selftest` costs 659.9 s, which is 75.6 % of
the 873 s wall clock. Perfect packing of the other 69 legs gives `max(660, 4018/8) = 660 s`. Every
scheduling improvement in this build competes for the remaining 213 s. Sharding that leg is worth
more than everything specced here, and it is deliberately NOT specced here — it is a separate build.

> **Still true at `43a6c13`, and more so: `max(836.5, 4614.6/8) = 836.5 s`, so the same leg is now
> 81 % of the wall and scheduling competes for 197 s of a longer run.** This fact was recorded as
> context in the design pass. The re-scope promotes it to the thing that decides the build, because
> it is the reason `-3`'s dispatch half buys nothing measurable and `-6` and `-7` buy everything.

**The 14x saving already exists and is switched off where it matters.** 873 s against 62 s is the
full bar against a pure-records run. The mechanism is the per-leg `guard`, and `.githooks/pre-push`
sets `GATE_FULL=1`, which bypasses every guard. So a docs-only landing pays 14 m 33 s to prove
nothing about docs.

**The operator is blind for most of a run.** Legs dispatch longest-first from the timing cache and
report in manifest order, so stdout is head-of-line blocked. Measured: 63 of 70 legs complete while
9 lines had printed; on the 283 s scoped run the first line appeared at roughly 240 s.

**Nothing coordinates two bars.** There is no runtime lock anywhere in this repo, and `git worktree
list` shows eleven live worktrees on this node.

> **Observed, not predicted, on 2026-08-20.** `git worktree list` now returns 26. Four concurrent
> full bars from different sessions stretched one leg of this build's own closing run from about 11
> minutes to 99, and red the run-gates canary's timing arms — which announced honestly that the arm
> AND its width-1 control had both expired, so the clamp was unproven either way, rather than
> passing green. A sibling measured the same machine at width 24 running 26 % SLOWER than width 8:
> the contended resource does not parallelise, so serializing bars is the right shape here. `-4` was
> the sixth unit of seven; the re-scope makes it the second.

## Units

All seven were MISSING at kickoff, were authored in this build's design pass, and were then audited
by `reviews/2026-08-18-review-TOOL-aPacedTurnstile-1.md`, which returned **BLOCKED** on five
blockers. All five are folded in, each as a rev bump with its §9 line. The forks every spec's
§8 still carried were then swept and RESOLVED in place under the standing mandate, which is what
moved the set from FORKED to READY; before that sweep this table's classification column and the
driver's own computation disagreed. **The live rev of each spec is in the generated table below,
not here** — restating it in this column is what let that column go stale once already.

A SECOND audit then ran, because M4 keys on rev movement and every rev had moved since the only
recorded verdict — which was round 1's BLOCKED. It returned BLOCKED again on 29 confirmed findings
of 37 raised, recorded in `reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md`, and all 29
are folded. It was worth running twice: nine of round 1's fixes had landed half, inverted, or in the
wrong unit, and three of the sweep's own ratified answers turned out to be options written BEFORE
the round-1 fold-in — including `-5`'s, which credited blocker F2's closure to a mechanism the
fold-in had replaced and would have re-licensed the branch F2 named.

A THIRD pass then re-reviewed that fold, which is what M8 asks for. It returned BLOCKED on 23
confirmed of 25 raised (`reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md`), and all 23
are folded. **The recurring defect of this build is not in any one document: it is that a fix naming
more than one carrier lands in one of them.** Round 1's F2 landed in the scope items and not in §4
or the criteria; round 2 found nine of the same shape; round 3 found the round-2 fix had landed in
the consumer and not in the owner. Every remaining multi-carrier obligation in this set is therefore
written as a MEASUREMENT or as a rule rather than as an enumeration.

| id | unit | classification | audit |
|---|---|---|---|
| TOOL-aPacedTurnstile-1 | `run-gates` promoted from gov-internal script to a deployable kit | **BUILT** | F1 blocker folded |
| TOOL-aPacedTurnstile-2 | hardware profiles — a declared table, auto-selected | **BUILT** | — |
| TOOL-aPacedTurnstile-3 | chunked REPORTING; the dispatch half cut | RE-SCOPED | — |
| TOOL-aPacedTurnstile-4 | the beacon and the queue — one bar per repo at a time | RE-SCOPED | — |
| TOOL-aPacedTurnstile-5 | the run record — the durable status emitter | RE-SCOPED | F2/F3/F5 and T1 folded |
| TOOL-aPacedTurnstile-6 | reuse a proven green; the base rule repaired | RE-SCOPED | F4 folded |
| TOOL-aPacedTurnstile-7 | the push boundary becomes diff-scoped | RE-SCOPED | F5, R1 and T1 folded |

The blockers, because they are the record of what the design got wrong before a line of code. Five
from round 1, one from round 2, one from round 3 — and the round-4 pass found none, which is where
the design closed:

| # | unit | the defect |
|---|---|---|
| F1 | `-1` | the descriptor declared five gate-leg rows when only four legs exist at its landing, which reds the deployer's selfcheck on the unit's own commit |
| F2 | `-5` | moving the per-leg completion file to a FIXED path turns a leftover into a false GREEN — that file is the dispatch suppressor, not a log, and two sibling units add exactly the writers that outlive a run |
| F3 | `-5` | `gate-full-green`'s "failed nothing" precondition was the only one of its preconditions with no negative control, so an implementation that forgot it passed every arm |
| F4 | `-6` | the unit had no position in the build order while changing the base every guard diffs against, leaving it undecidable which base the authoritative boundary would use |
| F5 | `-7` | a full green earned on a DIRTY tree reset the lag counter, making the replacement property false while the record made it look measured |
| R1 | `-7` | the fix for F5 overshot. Predicate 0 joined the recorded digest against a fresh fingerprint of the PUSHED TIP, and `-5` defines that digest over the committed tree object, so it fired on every push whose tree had moved — exactly the population predicates 3 and 4 admit. Both arms were fixture-built, so nothing on the bar noticed |
| T1 | `-5`, `-7` | the fix for R1 landed in the CONSUMER, not the owner. `-7` said predicate 0 computes at the recorded sha by CALLING `-5`'s helper, while `-5` declared one digest over the live working tree with no sha argument. R19 gave that helper a NAME and nobody gave it a SIGNATURE |

## What the first unit changed for the six that follow

`TOOL-aPacedTurnstile-1` is BUILT and landed, full bar green at 73/73. Four of its effects are
inputs to units specced before it existed, so they are named here rather than left to be
rediscovered:

- **The canary SPLIT.** `run-gates.test.sh` ships and asserts only what is true in any tree;
  `tools/run-gates/run-gates.gov.test.sh` holds the arms keyed on gov's corpus, is withheld from the
  payload by a `project-owned` rule, and REFUSES with exit 2 rather than passing on a foreign
  manifest. `-3` AC6, `-6` AC12 and `-7` AC9 now have a named home that did not exist when they were
  written.
- **The manifest is DERIVED, not spelled** — the kit dir's sibling, computed identically in the
  runner and both harnesses, with the gov canary asserting that identity as SOURCE parity. `-3`'s
  reorder must preserve it.
- **The report tail is a two-space contract.** Every report verb `-2`, `-3` and `-6` add conforms:
  two spaces before any parenthesised tail.
- **The leg count moved 70 → 73**, and then to 86 by 2026-08-20. It has now moved three times inside
  this build's lifetime, which is why no spec here states it any more.

Three defects the unit's own arms caught while it was built, each a class this repo already names,
each fixed rather than waived: a prefix strip comparing a git-spelled path against a pwd-spelled one
(two spellings, one directory); a gate arm that RECOMPUTED the answer it was checking and disagreed
with itself on first run; and a mutation arm whose mutation silently never happened, so it passed by
finding the string it was meant to remove.

## The re-scope — 2026-08-20, `TOOL-aPacedTurnstile-16`

The owner answered the scope decision `-1` parked with option (c): re-scope the remaining five units
against what `-1` and `-2` actually landed. Every one of the five was regrounded against the tree.
None was dropped and none was already built by somebody else — `GATE_REUSE`, `impure`, the chunk
key, the beacon, the ledger and `gate-fingerprint.sh` are all still absent. What HAD moved was every
number in every spec, and one thing bigger than a number.

**The thesis.** This build was designed around SCHEDULING — chunk the legs, dispatch them better,
pick a width. The bar is floor-bound, so scheduling cannot move it. The wall-clock value sits
entirely in the two units that make the bar RUN LESS, and none of it in the unit that reorders work.

| unit | re-scope | why |
|---|---|---|
| `-3` | **SPLIT, dispatch half CUT** | keeps the chunk key, chunk-ordered reporting and the early first signal — `aMeteredTurnstile` measured 9.3 minutes of silence before the first leg reported. Loses S2's reorder and S4's chunk-major dispatch: both buy zero on a floor-bound bar |
| `-4` | **KEEP, promoted to second** | its value was never wall clock. It is the only thing in the tree that coordinates two bars, and the contention it prevents is now observed rather than argued |
| `-5` | **KEEP, absorbs three carriers** | `profile_bar.py` reads `gate-timings.tsv` and REFUSES when the file's mtime does not move, so S6 cannot simply replace it; the header key set extends to the profile row `-2` created |
| `-6` | **KEEP, S8 CUT, base rule repaired** | the network predicate matched six legs on its first run over the real manifest, every one hermetic, and `impure` cannot travel. S5's refusal could not tell a degenerate merge-base from a fresh branch |
| `-7` | **KEEP, carriers re-derived** | the mechanism is intact and the guard hole S10 closes is verified still open in both carriers. Two of the seven files S9 named no longer exist — `aFusedCharter` collapsed the template family — so AC7 is restated as a SEARCH's output rather than a list, which is the half that rotted |

Two sibling records were closed as part of this, and it is a records fix rather than product work:
`TOOL-aTimedTurnstile-2` and `-5` were both INPROGRESS at revs dated 2026-08-11 while describing a
tree that already exists. Leaving them open made a non-terminal spec the second owner of a seam
three units here rewrite, and of the very push-boundary property `-7` retires. `-7` now SUPERSEDES
`aTimedTurnstile-2` S3 — superseded, never rewritten.

## Build order, and the dependency that forces each edge

Derived by the design pass's reconciliation, then RE-derived by the re-scope against the measurement.

```
-1  →  -2  →  -5  →  -4  →  -6  →  -7  →  -3
```

*Superseded, kept visible because the edges it names are still the reasoning the table below edits:*
`-1 → -2 → -5 → -6 → -3 (runner) → -4 → -7 → -3 (manifest reorder)`. Two edges of that chain existed
only to protect the reorder commit, and they dissolve with it; `-7`'s wait on `-3` dissolves with the
halt.

| edge | what forces it |
|---|---|
| `-1` first | it moves the runner and both harnesses, so every other unit's paths, gate commands and waiver rows are wrong until it lands; it also fixes the report-tail contract the other three extend |
| `-1` → `-2` | the profile knob is inserted directly above a clamp block that must not move, and it must sit in the moved file |
| `-2` → `-5` | the record writer gains the profile line; sequencing the record first means re-editing it |
| `-5` → `-6` | `-6` reads the ledger and the input key `-5` writes, and cannot be built against a record that does not exist |
| `-5` → `-4` | `-4` widens the EXIT trap `-5` narrows, so the trap's final shape is settled before a second unit edits it |
| `-4` second | RE-SCOPED forward from sixth. Its value is contention, not wall clock, and it is independent of the base and boundary changes — so landing it early de-risks everything after it, and it is the unit that would have paid for itself twice already on this node |
| `-4` → `-6` | `-6` changes the base every guard diffs against; settling coordination before base semantics keeps the two failure surfaces apart |
| `-6` → `-7` | `-7` reads the full-green record `-5` writes and inherits the base `-6` sets; it is the only unit that changes what the authoritative run covers, so it lands after everything it grades |
| `-7` → `-3` | nothing forces this edge. `-3` is last because it is reporting-only and has no dependents once the halt is cut — not because anything waits on it |
| ~~everything → `-3` manifest~~ | CUT with S2. The reorder rewrote every row of a file that `cKeyedLaunchpad-7`, `aWalkedCorpus-2` and `aGuardedTally-1` are all queued to add rows to, and the row-keyed merge driver does not cover JSON |

`-6` was absent from this chain in the first draft, which the spec audit raised as a blocker: the
unit changes the base `changed()` diffs against, `-7` consumes `changed()` and declares it unchanged,
and with no sequenced position it was undecidable from the record which base the authoritative
boundary would run on.

## Owner decisions already taken

Taken at kickoff on 2026-08-18, before any spec was authored, and not to be re-litigated inside the
build:

| question | decision |
|---|---|
| how far to carry the discipline to adopters | promote `run-gates.sh` to a real, deployable kit |
| sequencing against the 660 s floor | mechanism first; sharding the heavy legs is its own build |
| GPU acceleration | CUT — there is no float math anywhere on this bar |
| hardware profiles despite a ~0 win on 8+ cores | KEEP — build the table now for the 4-core case |
| the push boundary | make it diff-scoped |

## The risk this build carries

Diff-scoping the push boundary inverts the safety property the current design rests on. `AGENTS.md`
states it plainly today: a guard "can only ever scope a NON-authoritative run, which is what makes a
too-narrow guard cost an early signal rather than a wrong merge verdict". Two records already lean on
that backstop — `memory/builds/cBriefedPilot/spec/2026-08-14-spec-cBriefedPilot-15.md` and a park in
`memory/builds/cKeyedLaunchpad/README.md`, which refused to widen a guard precisely because
`GATE_FULL=1` would catch it. TOOL-aPacedTurnstile-7 owns that inversion and must replace the
backstop rather than delete it.

The design pass sharpened this into the build's single largest risk: **`-7` removes the only
mechanism that has ever caught a too-narrow guard, in the same build in which three units widen
the guard surface — and one such hole was verified still open.** `kit/dogfood doc parity` validated
three pairs and guarded on two, so a change to only `memory/guides/BUILD-METHOD.md` skipped the leg
that checks it. Round 2 found the hole had TWO carriers: `tools/memory-tree/kit.toml` declares the
same leg for DEPLOYMENT, and govkit copies a descriptor's guard verbatim into a target, so fixing
gov's manifest alone would have EXPORTED it.

**CLOSED, in `-7`'s own commit and in both carriers** — not filed as an accepted residual, which
is what the risk being real rather than theoretical bought.

Two things the design pass recommended that this build does NOT take, recorded because a refused
recommendation is worth more on the record than off it:

- It recommended shipping `GATE_FULL_MAX_LAG` at `1` — behaviourally today's bar — and lowering it
  only once the record shows how often a scoped verdict differed from the full run it replaced. The
  argument is that `-7`'s value is measurability, and taking the saving before the measurement exists
  spends the property that was supposed to justify spending it. This build ships `10` instead,
  because the owner's stated goal is to stop paying 873 s per landing and a default of `1` defers
  essentially all of that. The knob is one line, the record makes the comparison observable, and
  lowering it later needs no code.
- It recommended keeping `-5` and `-6` as one spec. Refused in `-6` §8, with the reason recorded
  there: the split isolates the half a reviewer must be hostile toward.

<!-- gen:build-index -->
**Build status:** SPECCED · 8 unit(s) · node a · opened 2026-08-18 · streams tooling
ids TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 TOOL-aPacedTurnstile-8 TOOL-aPacedTurnstile-9 TOOL-aPacedTurnstile-10 TOOL-aPacedTurnstile-11 TOOL-aPacedTurnstile-12
ids TOOL-aPacedTurnstile-13 TOOL-aPacedTurnstile-14 TOOL-aPacedTurnstile-15 TOOL-aPacedTurnstile-16

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aPacedTurnstile-1 — the gate runner becomes a deployable kit](spec/2026-08-18-spec-TOOL-aPacedTurnstile-1.md) | CLOSED | rev-7 | 2026-08-18 |
| [TOOL-aPacedTurnstile-2 — the runner's knobs become a declared hardware profile table](spec/2026-08-18-spec-TOOL-aPacedTurnstile-2.md) | CLOSED | rev-8 | 2026-08-20 |
| [TOOL-aPacedTurnstile-3 — ordered chunks, and a verdict the operator sees before the run ends](spec/2026-08-18-spec-TOOL-aPacedTurnstile-3.md) | CLOSED | rev-10 | 2026-08-20 |
| [TOOL-aPacedTurnstile-4 — the turnstile: one bar per repo, and a queue for the rest](spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md) | CLOSED | rev-7 | 2026-08-20 |
| [TOOL-aPacedTurnstile-5 — the run record: a durable, machine-readable status emitter](spec/2026-08-18-spec-TOOL-aPacedTurnstile-5.md) | CLOSED | rev-9 | 2026-08-20 |
| [TOOL-aPacedTurnstile-6 — reuse a proven green, and scope a worktree to its own branch point](spec/2026-08-18-spec-TOOL-aPacedTurnstile-6.md) | CLOSED | rev-6 | 2026-08-20 |
| [TOOL-aPacedTurnstile-7 — the push boundary scopes to the diff, and "every leg" becomes a bounded obligation](spec/2026-08-18-spec-TOOL-aPacedTurnstile-7.md) | CLOSED | rev-10 | 2026-08-20 |
| [TOOL-aPacedTurnstile-14 — the authored roster is read with its refusal intact](spec/2026-08-20-spec-TOOL-aPacedTurnstile-14.md) | SPECCED | rev-3 | 2026-08-20 |
<!-- /gen:build-units -->

Records live under `spec/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md) | diff-review | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-20-review-TOOL-aPacedTurnstile-14.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-14.md) | spec-audit | TOOL-aPacedTurnstile-14 |
| [2026-08-20-review-TOOL-aPacedTurnstile-2-round2.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-2-round2.md) | diff-review | TOOL-aPacedTurnstile-2 |
| [2026-08-20-review-TOOL-aPacedTurnstile-2.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-2.md) | diff-review | TOOL-aPacedTurnstile-2 |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-18-spec-TOOL-aPacedTurnstile-1.md](spec/2026-08-18-spec-TOOL-aPacedTurnstile-1.md)
  - [2026-08-18-spec-TOOL-aPacedTurnstile-2.md](spec/2026-08-18-spec-TOOL-aPacedTurnstile-2.md)
  - [2026-08-18-spec-TOOL-aPacedTurnstile-3.md](spec/2026-08-18-spec-TOOL-aPacedTurnstile-3.md)
  - [2026-08-18-spec-TOOL-aPacedTurnstile-4.md](spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md)
  - [2026-08-18-spec-TOOL-aPacedTurnstile-5.md](spec/2026-08-18-spec-TOOL-aPacedTurnstile-5.md)
  - [2026-08-18-spec-TOOL-aPacedTurnstile-6.md](spec/2026-08-18-spec-TOOL-aPacedTurnstile-6.md)
  - [2026-08-18-spec-TOOL-aPacedTurnstile-7.md](spec/2026-08-18-spec-TOOL-aPacedTurnstile-7.md)
  - [2026-08-20-spec-TOOL-aPacedTurnstile-14.md](spec/2026-08-20-spec-TOOL-aPacedTurnstile-14.md)
- **`reviews/`**
  - [2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md)
  - [2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md)
  - [2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md)
  - [2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md)
  - [2026-08-18-review-TOOL-aPacedTurnstile-1.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1.md)
  - [2026-08-20-review-TOOL-aPacedTurnstile-14.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-14.md)
  - [2026-08-20-review-TOOL-aPacedTurnstile-2-round2.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-2-round2.md)
  - [2026-08-20-review-TOOL-aPacedTurnstile-2.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-2.md)
<!-- /gen:build-docs -->
