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

**State.** SPECCED at rev-1, unreviewed at the time of writing. One Tier-2 spec covers the whole
change, because it is one contract revision rather than a kit built from nothing.

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

**What this build does NOT do.** It defines the seam the instruction layer plugs into and stops
there. How to write a sub-spec, how to run an adversarial review, what "built" means for a given
unit — all of that belongs to the parallel session, and a second author here would collide with it.

**Read before reviewing:** `memory/guides/UNATTENDED-PROTOCOL.md` (binding, and this build amends
it) and `memory/builds/aUnmannedHelm/reviews/2026-08-10-review-aUnmannedHelm-2.md`, whose three
reproduced blockers are the reason the current authorization is shaped the way it is. A review of
this build that does not re-derive those three attacks against the NEW surface has not reviewed it.

**Live constraints, measured 2026-08-11:**

- The playbook template has **190 bytes free** (`bash tools/check-template-size.sh`). This build
  amends existing clauses rather than adding a section, so it should spend none — verify, don't
  assume.
- `ARMS_FLOORS` pins `tools/unattended/unattended.sh` at 31 branches and
  `tools/unattended/check-unattended.sh` at 33, both one-sided upward. Deleting the mandate branches
  lowers a floor, which reds. The floors move down only in a commit that says why.
- `ORPHAN_ID_PIN` is 5 and shrink-only. Minting unit ids ahead of their specs would create orphans,
  which is why the plan region names units by TITLE and never by id.

## The units

One spec, scope items `S1`–`S7`. The rows below are the reading order, not a decomposition into
sub-specs.

| Area | What changes |
|---|---|
| **S1** | authorization reads the build README at BASE; the mandate block and its marker pair retire |
| **S2** | `RUN.md` becomes wholly generated — `--preflight` creates it, the authored facts drop to four |
| **S3** | the merge-base-equals-HEAD refusal is scoped to the verbs that can honestly assert it |
| **S4** | `--plan`, deriving the gap list from specs and review records rather than from prose |
| **S5** | the authored plan region, and the build-README template that documents it |
| **S6** | the phase vocabulary gains the members `--plan` needs to name a position |
| **S7** | the amendment set — protocol, charter, playbook companion, manifest, skill render, hand-back |

## Owner decision menu

Four forks are open and live in the spec's §8. They are summarised here; the spec carries the
tradeoffs.

**F1** — does the plan region's byte-equality across BASE become a hard precondition, or stay an
opt-in that lights up only when the region exists? Recommendation: opt-in, because a hard
precondition reintroduces the per-build authoring this build exists to remove.

**F2** — when a legitimate mid-run reconciliation moves the merge-base forward, does the recorded
BASE assertion relax from equality to ancestry? Recommendation: yes, with the plan-region comparison
carrying the integrity the equality used to carry.

**F3** — does `--plan` read tracked files only, matching every other gate here, or also the working
tree? Recommendation: tracked only, so an uncommitted spec is invisible until the run commits it.

**F4** — is the widening the owner ratified recorded as a decision row, given it converts a
per-build grant into a class grant? Recommendation: yes, and named as such.

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

None yet. The spec is unreviewed at rev-1.

Records live under `spec/`, `build/` and `reviews/`. The table below is
GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** SPECCED · 1 unit(s) · node a · opened 2026-08-11 · streams tooling+playbook+kickoff · ids TOOL-aStandingWrit-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aStandingWrit-1 — the run authorizes on a plan it did not write](spec/2026-08-11-spec-aStandingWrit-1.md) | SPECCED | rev-1 | 2026-08-11 |
<!-- /gen:build-index -->
