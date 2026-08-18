---
slug: aPacedTurnstile
node: a
opened: 2026-08-18
streams: tooling
roster: TOOL
ids: TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 TOOL-aPacedTurnstile-8 TOOL-aPacedTurnstile-9 TOOL-aPacedTurnstile-10 TOOL-aPacedTurnstile-11
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
blockers. All five are folded in, each as a rev bump with its §9 line.

| id | unit | classification | audit |
|---|---|---|---|
| TOOL-aPacedTurnstile-1 | `run-gates` promoted from gov-internal script to a deployable kit | READY | rev-2, F1 blocker folded |
| TOOL-aPacedTurnstile-2 | hardware profiles — a declared table, auto-selected | READY | rev-2 |
| TOOL-aPacedTurnstile-3 | ordered chunks, each reported before the next starts | READY | rev-2 |
| TOOL-aPacedTurnstile-4 | the beacon and the queue — one bar per repo at a time | READY | rev-2 |
| TOOL-aPacedTurnstile-5 | the run record — the durable status emitter | READY | rev-2, F2/F3/F5 blockers folded |
| TOOL-aPacedTurnstile-6 | resume from a failed leg, diff-only re-runs, worktree scoping | READY | rev-2, F4 blocker folded |
| TOOL-aPacedTurnstile-7 | the push boundary becomes diff-scoped | READY | rev-3, F5 blocker folded |

The five blockers, because they are the record of what the design got wrong before a line of code:

| # | unit | the defect |
|---|---|---|
| F1 | `-1` | the descriptor declared five gate-leg rows when only four legs exist at its landing, which reds the deployer's selfcheck on the unit's own commit |
| F2 | `-5` | moving the per-leg completion file to a FIXED path turns a leftover into a false GREEN — that file is the dispatch suppressor, not a log, and two sibling units add exactly the writers that outlive a run |
| F3 | `-5` | `gate-full-green`'s "failed nothing" precondition was the only one of its preconditions with no negative control, so an implementation that forgot it passed every arm |
| F4 | `-6` | the unit had no position in the build order while changing the base every guard diffs against, leaving it undecidable which base the authoritative boundary would use |
| F5 | `-7` | a full green earned on a DIRTY tree reset the lag counter, making the replacement property false while the record made it look measured |

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
**Build status:** OPEN · 7 unit(s) · node a · opened 2026-08-18 · streams tooling
ids TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 TOOL-aPacedTurnstile-8 TOOL-aPacedTurnstile-9 TOOL-aPacedTurnstile-10 TOOL-aPacedTurnstile-11

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aPacedTurnstile-1 — the gate runner becomes a deployable kit](spec/2026-08-18-spec-TOOL-aPacedTurnstile-1.md) | OPEN | rev-3 | 2026-08-18 |
| [TOOL-aPacedTurnstile-2 — the runner's knobs become a declared hardware profile table](spec/2026-08-18-spec-TOOL-aPacedTurnstile-2.md) | OPEN | rev-3 | 2026-08-18 |
| [TOOL-aPacedTurnstile-3 — ordered chunks, and a verdict the operator sees before the run ends](spec/2026-08-18-spec-TOOL-aPacedTurnstile-3.md) | OPEN | rev-4 | 2026-08-18 |
| [TOOL-aPacedTurnstile-4 — the turnstile: one bar per repo, and a queue for the rest](spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md) | OPEN | rev-3 | 2026-08-18 |
| [TOOL-aPacedTurnstile-5 — the run record: a durable, machine-readable status emitter](spec/2026-08-18-spec-TOOL-aPacedTurnstile-5.md) | OPEN | rev-4 | 2026-08-18 |
| [TOOL-aPacedTurnstile-6 — reuse a proven green, and scope a worktree to its own branch point](spec/2026-08-18-spec-TOOL-aPacedTurnstile-6.md) | OPEN | rev-3 | 2026-08-18 |
| [TOOL-aPacedTurnstile-7 — the push boundary scopes to the diff, and "every leg" becomes a bounded obligation](spec/2026-08-18-spec-TOOL-aPacedTurnstile-7.md) | OPEN | rev-5 | 2026-08-18 |

Records live under `spec/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-18-review-TOOL-aPacedTurnstile-1.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7 |
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
- **`reviews/`**
  - [2026-08-18-review-TOOL-aPacedTurnstile-1.md](reviews/2026-08-18-review-TOOL-aPacedTurnstile-1.md)
<!-- /gen:build-docs -->
