---
slug: aStandingWrit
node: a
opened: 2026-08-11
streams: tooling+playbook+kickoff
roster: TOOL
ids: TOOL-aStandingWrit-1
---

# aStandingWrit — the run authorizes on a plan it did not write

Node `a` · opened 2026-08-11 · streams tooling+playbook+kickoff.

The unattended-run kit shipped with an authorization the owner has to hand-author once per run: a
mandate block, fenced by a marker pair, inside the run-state file the driver then writes into. It
works and it is un-forgeable, and it is not the feature the owner asked for. The owner's act is
supposed to be `/unattended <slug>` and nothing else.

This build moves the authorization off the owner's keyboard without moving it inside the run's reach.
The surface it moves to is the build folder the owner already creates when they shape a build.

This README is the **master overview and the owner decision menu**, per `memory/TEMPLATE-SPEC.md`.

## Start here

**State.** SPECCED at rev-3. The Tier-2 review returned **do not build** on rev-1; rev-2 folded it and
rev-3 carries all eight owner forks RESOLVED. S0 is the next thing built, per F8, and its mechanism is
being settled by a dedicated design panel before a line is written.

**Read this first.** The review reproduced, end to end and with a live control, an authorization
bypass in the unattended kit **as it is merged and gated on `main` today**. The pinned BASE anchors
on a remote-tracking ref, and `unattended.sh:119-120` claims moving it "requires a push". It does
not: `git update-ref refs/remotes/origin/main <sha>` does it offline. A run can author its own
mandate, forge the anchor, and pass `--preflight`, the gate leg and `--close`, then land. It is
recorded as its own backlog row because it is a defect in landed code and does not depend on this
build. **F8 asks whether the repair lands ahead of everything else. It should.**

**The problem in one line.** `unattended.sh` refuses a run whose build has no owner-authored
`RUN.md` (`fail 15`), and the surrounding checks make that refusal correct — so the kit is working
as designed and the design is wrong.

**The three defects this build fixes**, all of which sit on the execution path and none of which is
an instruction-layer question:

1. The authorization artifact is owner-authored, per run.
2. `trusted_base()` refuses when the merge-base equals HEAD — which is the state at preflight on a
   fresh branch, i.e. every run this feature exists to enable.
3. The driver has no notion of the work. `RUNNING` covers spec-writing, reviewing and building
   undifferentiated, so `--status` after a compaction cannot say where the run is and `--resume`
   cannot say what to pick up.

**What this build does NOT do.** It decides exactly three things the instruction layer must honour —
that a unit's position is READ from its spec's status header and declared pointers rather than
inferred, that `INPROGRESS` means built-but-not-landed, and that `BLOCKED`, `DEFERRED` and `WONTDO`
are never a `next:` target — and stops. How to write a sub-spec, how to run the adversarial review,
and what evidence makes a unit built belong to the parallel session. That session is unlocatable from
this tree, so the dependency is a backlog row rather than an assumption.

**Read before reviewing:** `memory/guides/UNATTENDED-PROTOCOL.md` (binding, and this build amends
it) and `memory/builds/aUnmannedHelm/reviews/2026-08-10-review-aUnmannedHelm-2.md`, whose three
reproduced blockers are the reason the current authorization is shaped the way it is. A review of
this build that does not re-derive those three attacks against the NEW surface has not reviewed it.

**Live constraints, measured 2026-08-11 by running the gates, not by copying a note:**

- The playbook template has **148 bytes free** (`bash tools/check-template-size.sh` reports
  32620/32768). Rev-1 said 190; that figure was copied from a manifest note stale since before the
  last merge, and the note itself says to read the number from the gate.
- `ARMS_FLOORS` pins `tools/unattended/unattended.sh` at 31 branches and
  `tools/unattended/check-unattended.sh` at 33, with **zero slack** on both. The floor is a per-gate
  NET count, so this build's additions can mask its deletions and six guards can vanish in silence.
  Re-measure and re-pin in the same commit; the spec's AC13 asserts the number.
- `non_terminal_specs_cited_by_product_source` sits AT its pin with zero headroom, and six of the
  seven amendment targets are inside its globs. One comment citing this spec's id while it is
  non-terminal reds the bar.

## The units

One spec, scope items `S0`–`S7`. The rows below are the reading order, not a decomposition into
sub-specs.

| Area | What changes |
|---|---|
| **S0** | close the anchor bypass — the pinned BASE becomes an observation of the remote, not of a local ref. Everything else depends on it |
| **S1** | authorization reads the build README at BASE; the mandate block and its marker pair retire |
| **S2** | `RUN.md` loses its authored mandate; `--preflight` creates it and commits it, so the leg can still see it |
| **S3** | the merge-base-equals-HEAD refusal is scoped by verb, with the BASE value for that state defined |
| **S4** | `--plan`, over DECLARED pointers only — the filename join and the title match are both deleted |
| **S5** | the authored plan region, its ordinal key, and the build-README template |
| **S6** | three new phase members, a meaning for `RUNNING`, and a verb that can actually write one |
| **S7** | the amendment set — seven files, not four |

## Owner decision menu — all eight RESOLVED 2026-08-11

Every fork resolved as recommended. The spec's §8 carries each one in place with its tradeoffs; this
is the summary.

**F8** — S0 lands as its own series, ahead of everything else. It repairs a live bypass in merged
code and depends on none of the design questions. Its mechanism is being settled by a dedicated
design panel rather than by this author's first instinct, because the first instinct is what shipped
the bypass.

**F5** — self-propagating authorization is refused. Any build created after this lands must carry a
plan region, which makes the integrity check non-vacuous for exactly the population that can
propagate. The 26 existing builds are grandfathered deliberately: they predate any run that could
have authored them.

**F6** — a build authorizes both actions, and the amended charter sentence says so. Replacing the
wording is a scope item, not a paraphrase.

**F7** — the instruction layer stays out of scope and the cut-line is narrowed instead, to the three
decisions the state table actually makes. The dependency is a backlog row, so if the parallel session
proves not to exist, the row is what surfaces it.

**F1** — the plan-region integrity check is opt-in, and the template ships the region commented out.

**F2** — the recorded-BASE assertion keeps equality. The hazard rev-1 cited cannot occur; the lander
refuses to run off the default branch.

**F3** — `--plan` reads tracked files only.

**F4** — the widening is recorded, naming all five losses.

## Ratified decisions

Two forks were put to the owner on 2026-08-11 at kickoff and both resolved.

**F0a** — the authorization surface. RESOLVED: **README existence alone, no conf key.** A committed
build folder with a `README.md` is the whole precondition; nothing is declared in `.unattended.conf`
and nothing is added to the README's front matter. The owner was shown that this converts a
per-build grant into a class grant over every build in the tree and chose it anyway.

**F0b** — the work loop. RESOLVED: **the driver derives the gap list.** A verb computes which
planned units have no spec, which specs have no review record, and which are non-terminal, from the
same source `gen_build_index.py` already reads. The instruction layer then says how to do each step;
this says which step remains.

## Review record

`reviews/2026-08-11-review-aStandingWrit-1.md` — Tier-2 over the rev-1 spec. Five lenses, five
cold-start agents, at the review protocol's cap of five total; no lens dead. Verdict: **do not
build**. Seven blockers, thirteen highs, seven verified factual errors, and one reproduced bypass in
landed code that outranks the spec entirely. Three findings were independently confirmed by two
lenses each. Folded at rev-2.

The review also returned two negative results worth keeping: no live branch or worktree collides
with this build's file list, and the rev-1 spec was machine-clean against the format contract.

Records live under `spec/`, `build/` and `reviews/`. The table below is
GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** SPECCED · 1 unit(s) · node a · opened 2026-08-11 · streams tooling+playbook+kickoff · ids TOOL-aStandingWrit-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aStandingWrit-1 — the run authorizes on a plan it did not write](spec/2026-08-11-spec-aStandingWrit-1.md) | SPECCED | rev-3 | 2026-08-11 |
<!-- /gen:build-index -->
