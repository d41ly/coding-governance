---
slug: aDeclaredBound
node: a
opened: 2026-08-18
streams: tooling
roster: TOOL
ids: TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5
---

# aDeclaredBound — four hardcoded thresholds become declarations, and one of them gets a guard rail

Node `a` · opened 2026-08-18 · streams tooling.

`TOOL-aLoosenedCeiling` made the read-path budget adjustable and then surveyed what else is not.
The owner picked four from that survey. This build specs them.

| threshold | today | where |
|---|---|---|
| check 7's entry budget | `300`, and `350` for a build README | `check-memory-hygiene.sh` awk, and a third copy inside the failure message |
| `SPEC10_CUTOFF` | `2026-08-04`, env-overridable | a shell default in the same engine, while its THREE siblings are conf keys |
| `_RATCHET_LOOKBACK` | `14` | `drift_report.py` module constant |
| agent-cap's `CAP` / `MAX_VERIFIERS` / `MAX_LENSES` | `5` each | `agent-cap.js` file constants, deliberately not overridable |

## The fourth is not like the other three

The first three are ordinary: a number that should have been a declaration and is not. The fourth
is a number that is a constant **on purpose**, and its own source says why:

> A BARE LITERAL, never an environment read. An env-settable ceiling is the defeatable class this
> guard exists to remove, and it leaves no diff behind when someone raises it.

The owner's ask is that it become adjustable *by the owner*, with agents not touching it absent an
explicit request. Those two halves are not in tension with the recorded decision — the objection is
to the ENVIRONMENT as a channel, not to adjustability. An env read leaves no trace; a committed
declaration leaves a diff, a blame line and a reviewable justification. This build keeps the env
refusal exactly as it is and adds a declaration channel that cannot be used quietly.

**What no in-repo mechanism can do is PREVENT an agent from raising it.** An agent with shell access
can edit any file, including the gate that would catch it. `memory/guides/UNATTENDED-PROTOCOL.md` §9
already says this about checks running under a run's own uid, and this build says it again rather
than implying a guarantee it cannot deliver. What the design buys is: lowering is free, raising is
loud, and an unattributed raise reds the bar.

## Units

| id | mechanism | tier |
|---|---|---|
| `TOOL-aDeclaredBound-1` | check 7's two entry budgets become conf keys | 2 |
| `TOOL-aDeclaredBound-2` | `SPEC10_CUTOFF` joins its three sibling cutoffs in the conf | 2 |
| `TOOL-aDeclaredBound-3` | `_RATCHET_LOOKBACK` moves to drift-audit's PROJECT LAYER, not a conf | 2 |
| `TOOL-aDeclaredBound-4` | agent-cap reads a declaration; lowering is free, raising is attributed | 2 |
| `TOOL-aDeclaredBound-5` | the agent-cap number is single-sourced — prose points, never restates | 2 |

**Why five units for four thresholds.** Unit 5 is not extra scope; it is what makes unit 4 honest.
The number `5` is restated in at least eight live carriers — the charter, the README, the BINDING
review protocol, the byte-gated playbook template, a map dossier and the shipped kickoff skill among
them. The moment the value is adjustable, every one of those becomes a second answer to a question
that now has a declared first answer. This repo already ruled on that shape for the kit version:
*"a version written in prose rots between bumps, and this one rotted twice in a day."* Unit 4 without
unit 5 ships a knob whose documentation is wrong for anyone who turns it.

## Order

Units 1, 2 and 3 are independent of each other and of 4/5 — three different files, three different
kits. Unit 5 lands BEFORE unit 4: strip the restatements while the number is still fixed at 5 and
every carrier is still true, then make it adjustable. The reverse order has a window in which the
declaration and the prose can disagree, which is the defect unit 5 exists to prevent.

Units 1 and 2 touch the same engine and therefore share its kit-version bump and its self-test.
They sequence; the bump rides the later of the two, because the verdict-epoch leg is topological.

<!-- gen:build-index -->
**Build status:** OPEN · 5 unit(s) · node a · opened 2026-08-18 · streams tooling
ids TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aDeclaredBound-1 — check 7's entry budget becomes a declaration](spec/2026-08-18-spec-TOOL-aDeclaredBound-1.md) | OPEN | rev-1 | 2026-08-18 |
| [TOOL-aDeclaredBound-2 — SPEC10_CUTOFF joins its three sibling cutoffs in the conf](spec/2026-08-18-spec-TOOL-aDeclaredBound-2.md) | OPEN | rev-1 | 2026-08-18 |
| [TOOL-aDeclaredBound-3 — the ratchet lookback becomes a project-layer declaration](spec/2026-08-18-spec-TOOL-aDeclaredBound-3.md) | OPEN | rev-1 | 2026-08-18 |
| [TOOL-aDeclaredBound-4 — agent-cap reads a declaration: lowering is free, raising is attributed](spec/2026-08-18-spec-TOOL-aDeclaredBound-4.md) | OPEN | rev-1 | 2026-08-18 |
| [TOOL-aDeclaredBound-5 — the agent-cap number is single-sourced before it becomes adjustable](spec/2026-08-18-spec-TOOL-aDeclaredBound-5.md) | OPEN | rev-1 | 2026-08-18 |

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
  - [2026-08-18-spec-TOOL-aDeclaredBound-1.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-1.md)
  - [2026-08-18-spec-TOOL-aDeclaredBound-2.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-2.md)
  - [2026-08-18-spec-TOOL-aDeclaredBound-3.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-3.md)
  - [2026-08-18-spec-TOOL-aDeclaredBound-4.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-4.md)
  - [2026-08-18-spec-TOOL-aDeclaredBound-5.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-5.md)
<!-- /gen:build-docs -->
