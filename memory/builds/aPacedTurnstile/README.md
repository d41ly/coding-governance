---
slug: aPacedTurnstile
node: a
opened: 2026-08-18
streams: tooling
roster: TOOL
ids: TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 TOOL-aPacedTurnstile-8 TOOL-aPacedTurnstile-9 TOOL-aPacedTurnstile-10 TOOL-aPacedTurnstile-11 TOOL-aPacedTurnstile-12 TOOL-aPacedTurnstile-13 TOOL-aPacedTurnstile-14 TOOL-aPacedTurnstile-15
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

Four facts follow, and the whole build is shaped by them.

**The bar is floor-bound by one leg.** `unattended driver selftest` costs 659.9 s, which is 75.6 % of
the 873 s wall clock. Perfect packing of the other 69 legs gives `max(660, 4018/8) = 660 s`. Every
scheduling improvement in this build competes for the remaining 213 s. Sharding that leg is worth
more than everything specced here, and it is deliberately NOT specced here — it is a separate build.

**The 14x saving already exists and is switched off where it matters.** 873 s against 62 s is the
full bar against a pure-records run. The mechanism is the per-leg `guard`, and `.githooks/pre-push`
sets `GATE_FULL=1`, which bypasses every guard. So a docs-only landing pays 14 m 33 s to prove
nothing about docs.

**The operator is blind for most of a run.** Legs dispatch longest-first from the timing cache and
report in manifest order, so stdout is head-of-line blocked. Measured: 63 of 70 legs complete while
9 lines had printed; on the 283 s scoped run the first line appeared at roughly 240 s.

**Nothing coordinates two bars.** There is no runtime lock anywhere in this repo, and `git worktree
list` shows eleven live worktrees on this node.

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

A THIRD pass then re-reviewed that fold, which is what M8 asks for and which this build has now
twice been repaid for. It returned BLOCKED on 23 confirmed of 25 raised
(`reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md`), and all 23 are folded. **The
recurring defect of this build is not in any one document: it is that a fix naming more than one
carrier lands in one of them.** Round 1's F2 landed in the scope items and not in §4 or the
criteria. Round 2 found nine of the same shape. Round 3 found the round-2 blocker fix had landed in
`-7`, the consumer, and not in `-5`, which owns the interface it now calls — R19 gave the
fingerprint helper a NAME and nobody gave it a SIGNATURE — plus two fixes that created fresh
defects inside their own commit. Every remaining multi-carrier obligation in this set is therefore
written as a MEASUREMENT or as a rule rather than as an enumeration, and where that was not possible
the figure says in place that it is derived and has already moved.

| id | unit | classification | audit |
|---|---|---|---|
| TOOL-aPacedTurnstile-1 | `run-gates` promoted from gov-internal script to a deployable kit | **BUILT** | F1 blocker folded |
| TOOL-aPacedTurnstile-2 | hardware profiles — a declared table, auto-selected | READY | — |
| TOOL-aPacedTurnstile-3 | ordered chunks, each reported before the next starts | READY | — |
| TOOL-aPacedTurnstile-4 | the beacon and the queue — one bar per repo at a time | READY | — |
| TOOL-aPacedTurnstile-5 | the run record — the durable status emitter | READY | F2/F3/F5 and T1 blockers folded |
| TOOL-aPacedTurnstile-6 | resume from a failed leg, diff-only re-runs, worktree scoping | READY | F4 blocker folded |
| TOOL-aPacedTurnstile-7 | the push boundary becomes diff-scoped | READY | F5, R1 and T1 blockers folded |

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
- **The leg count moved 70 → 73**, which is the figure `-3`'s chunk arithmetic reads and which that
  spec already records as DERIVED and already-moved-once.

Three defects the unit's own arms caught while it was built, each a class this repo already names,
each fixed rather than waived: a prefix strip comparing a git-spelled path against a pwd-spelled one
(two spellings, one directory); a gate arm that RECOMPUTED the answer it was checking and disagreed
with itself on first run; and a mutation arm whose mutation silently never happened, so it passed by
finding the string it was meant to remove.

## Build order, and the dependency that forces each edge

Derived by the design pass's reconciliation, not chosen for convenience.

```
-1  →  -2  →  -5  →  -6  →  -3 (runner)  →  -4  →  -7  →  -3 (manifest reorder)
```

| edge | what forces it |
|---|---|
| `-1` first | it moves the runner and both harnesses, so every other unit's paths, gate commands and waiver rows are wrong until it lands; it also fixes the report-tail contract the other three extend |
| `-1` → `-2` | the profile knob is inserted directly above a clamp block that must not move, and it must sit in the moved file |
| `-2` → `-5` | the record writer gains the profile line; sequencing the record first means re-editing it |
| `-5` → `-6` | `-6` reads the ledger and the input key `-5` writes, and cannot be built against a record that does not exist |
| `-6` → `-3` | `-6` changes the base every guard diffs against, and `-3`'s chunk-skip reporting is graded against that base |
| `-3` → `-4` | the halt kills live workers, and beacon release must be proven on that path |
| `-4` → `-7` | `-7` reads the full-green record `-5` writes and inherits the base `-6` sets; it is the only unit that changes what the authoritative run covers, so it lands after everything it grades |
| everything → `-3` manifest | the reorder rewrites every row of a file four units add rows to, and the row-keyed merge driver does not cover JSON |

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

The design pass sharpened this into the build's single largest risk, and it is sharper than the
kickoff framing: **`-7` removes the only mechanism that has ever caught a too-narrow guard, in the
same build in which three units widen the guard surface — and one such hole is verified still open.**
The `kit/dogfood doc parity` leg guards on four paths but validates a pair that includes
`memory/guides/BUILD-METHOD.md`, which is in none of them. Today that costs a late signal; after `-7`
it costs a wrong merge verdict. `-7` S10 therefore closes that hole inside this build rather than
recording it as an accepted residual, and `-7` AC9 arms it.

Round 2 found that hole has TWO carriers and S10 was closing one. `tools/memory-tree/kit.toml`
declares the same leg for DEPLOYMENT with an even narrower guard, and govkit's emit verb copies a
descriptor's declared guard verbatim into a target — so fixing gov's manifest row alone would leave
the half that SHIPS open, and `-1` promotes the runner to a deployable kit precisely so adopters run
this bar. The hole would have been exported rather than fixed, and nothing catches the divergence:
govkit's selfcheck joins descriptor gate legs to the manifest by NAME only. S10 now names both
carriers and AC9b arms the shipping one.

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
**Build status:** OPEN · 8 unit(s) · node a · opened 2026-08-18 · streams tooling
ids TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 TOOL-aPacedTurnstile-8 TOOL-aPacedTurnstile-9 TOOL-aPacedTurnstile-10 TOOL-aPacedTurnstile-11 TOOL-aPacedTurnstile-12
ids TOOL-aPacedTurnstile-13 TOOL-aPacedTurnstile-14 TOOL-aPacedTurnstile-15

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aPacedTurnstile-1 — the gate runner becomes a deployable kit](spec/2026-08-18-spec-TOOL-aPacedTurnstile-1.md) | CLOSED | rev-7 | 2026-08-18 |
| [TOOL-aPacedTurnstile-2 — the runner's knobs become a declared hardware profile table](spec/2026-08-18-spec-TOOL-aPacedTurnstile-2.md) | CLOSED | rev-8 | 2026-08-20 |
| [TOOL-aPacedTurnstile-3 — ordered chunks, and a verdict the operator sees before the run ends](spec/2026-08-18-spec-TOOL-aPacedTurnstile-3.md) | OPEN | rev-8 | 2026-08-20 |
| [TOOL-aPacedTurnstile-4 — the turnstile: one bar per repo, and a queue for the rest](spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md) | OPEN | rev-4 | 2026-08-18 |
| [TOOL-aPacedTurnstile-5 — the run record: a durable, machine-readable status emitter](spec/2026-08-18-spec-TOOL-aPacedTurnstile-5.md) | OPEN | rev-7 | 2026-08-18 |
| [TOOL-aPacedTurnstile-6 — reuse a proven green, and scope a worktree to its own branch point](spec/2026-08-18-spec-TOOL-aPacedTurnstile-6.md) | OPEN | rev-4 | 2026-08-18 |
| [TOOL-aPacedTurnstile-7 — the push boundary scopes to the diff, and "every leg" becomes a bounded obligation](spec/2026-08-18-spec-TOOL-aPacedTurnstile-7.md) | OPEN | rev-8 | 2026-08-18 |
| [TOOL-aPacedTurnstile-14 — the authored roster is read with its refusal intact](spec/2026-08-20-spec-TOOL-aPacedTurnstile-14.md) | SPECCED | rev-2 | 2026-08-20 |
<!-- /gen:build-units -->

Records live under `spec/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md) | diff-review | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
| [2026-08-20-review-TOOL-aPacedTurnstile-2-round2.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-2-round2.md) | diff-review | TOOL-aPacedTurnstile-2 |
| [2026-08-20-review-TOOL-aPacedTurnstile-2.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-2.md) | diff-review | TOOL-aPacedTurnstile-2 |

Ids no record names: TOOL-aPacedTurnstile-14.

Ids no `spec-audit` record has ever named: TOOL-aPacedTurnstile-14.
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
  - [2026-08-20-review-TOOL-aPacedTurnstile-2-round2.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-2-round2.md)
  - [2026-08-20-review-TOOL-aPacedTurnstile-2.md](reviews/2026-08-20-review-TOOL-aPacedTurnstile-2.md)
<!-- /gen:build-docs -->
