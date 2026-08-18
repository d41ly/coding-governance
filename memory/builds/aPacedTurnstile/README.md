---
slug: aPacedTurnstile
node: a
opened: 2026-08-18
streams: tooling
roster: TOOL
ids: TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-7
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

| id | unit | classification |
|---|---|---|
| TOOL-aPacedTurnstile-1 | `run-gates` promoted from gov-internal script to a deployable kit | MISSING |
| TOOL-aPacedTurnstile-2 | hardware profiles — a declared table, auto-selected | MISSING |
| TOOL-aPacedTurnstile-3 | ordered chunks, each reported before the next starts | MISSING |
| TOOL-aPacedTurnstile-4 | the beacon and the queue — one bar per repo at a time | MISSING |
| TOOL-aPacedTurnstile-5 | the run record — the durable status emitter | MISSING |
| TOOL-aPacedTurnstile-6 | resume from a failed leg, diff-only re-runs, worktree scoping | MISSING |
| TOOL-aPacedTurnstile-7 | the push boundary becomes diff-scoped | MISSING |

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

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node a · opened 2026-08-18 · streams tooling
ids TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-7

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aPacedTurnstile-7 — the push boundary scopes to the diff, and "every leg" becomes a bounded obligation](spec/2026-08-18-spec-TOOL-aPacedTurnstile-7.md) | OPEN | rev-1 | 2026-08-18 |

Records live under `spec/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-18-spec-TOOL-aPacedTurnstile-7.md](spec/2026-08-18-spec-TOOL-aPacedTurnstile-7.md)
<!-- /gen:build-docs -->
