---
slug: aUnmannedHelm
node: a
opened: 2026-08-10
streams: tooling+kickoff+playbook+deployer
roster: TOOL
ids: TOOL-aUnmannedHelm-1
---

# aUnmannedHelm — the unattended-run kit: a mandate on disk, not a block of chat

Node `a` · opened 2026-08-10 · streams tooling+kickoff+playbook+deployer.

The owner's unattended sessions are launched today by retyping a protocol block into chat. It has
already drifted between runs, and nothing in the product records it. This build turns it into a kit:
a run-state file that survives compaction and process death, a protocol document, a driver script,
and a merge-bar leg — plus the kickoff hand-back, and an adopter path so other repos get the same
affordance.

This README is the **master overview and the owner decision menu**, per `memory/TEMPLATE-SPEC.md`.
Each unit below becomes its own conforming sub-spec under `spec/`. Unit 1 is specced;
units 2 through 7 are not yet written.

**`TOOL-aNumeralWarden-1` owns every agent-cap edit** after the F2 fold, so no unit here may claim
one — not `tools/hooks/agent-cap.js`, its test, its wired copy, nor `memory/guides/REVIEW-PROTOCOL.md`.
That spec is at rev-4 with four open forks.

It is **not** a blocking dependency, and the earlier claim that it was is withdrawn. The scoped
Tier-2 on the folded scope item found that the fold had created a dependency CYCLE: it keyed its
refusal on this build's run-state file, which this build's unit 1 defines. Resolving it to an atomic
count that reads no run-state file dissolved the cycle in both directions. Neither build blocks the
other now, and this build's own AC13 already required the arity guarantee not to depend on the
hook's schedule.

## Start here

**State.** Unit 1 is SPECCED and has cleared a Tier-2. Units 2 through 7 have no sub-spec yet.
Nothing here is built.

**Next action, either of:** write unit 2's sub-spec (the protocol document, which the other units
consume), or build unit 1 from `spec/2026-08-10-spec-aUnmannedHelm-1.md`, which stands alone.

**Read before writing any sub-spec:** `reviews/2026-08-10-review-aUnmannedHelm-1.md`. The
obligations column below is a one-line summary of what that review pinned on each unit, not a
replacement for it.

**Live constraints, measured 2026-08-10 and re-measurable:**

- The playbook template has **80 bytes free** at v2.5, not the 685 this build was designed against.
  A `aCandidStub` landing spent the headroom. Unit 2's playbook rules must be sized against 80, or
  fund themselves by moving prose into the companion.
- `non_terminal_specs_cited_by_product_source` sits AT its pin with zero headroom. No file under
  `tools/`, `skills/`, `.claude/`, the template, its companions or `WIRE-INTO-PROJECT.md` may cite
  this build's ids while the owning sub-spec is non-terminal. Records under `memory/` may.
- `TOOL-aNumeralWarden-1` is NOT a blocking dependency. It owns every agent-cap edit; it does not
  gate any unit here.

## The units

| Unit | Subject | Obligations the Tier-2 review pinned |
|---|---|---|
| **Unit 1** | the run-state file `RUN.md` | Joins the check-4 whitelist and `index_set`, with a check-7 exemption; NOT check 8. Moves four doc sites, not two. Carries the run BASE as an authored fact. Specced — see `spec/2026-08-10-spec-aUnmannedHelm-1.md` |
| **Unit 2** | the protocol document + domain-rules §15 | Owns keepalive schedule AND reap as agent obligations naming the tool calls. Names `bash tools/push-main.sh` as the landing step, never `--no-verify`. Ships a kit-owned CORE DoD set the project layer may only extend |
| **Unit 3** | the driver `tools/unattended/` | `--preflight` ASSERTS the mandate, never writes it; RECORDS a keepalive id the agent hands it; delegates to `check-wiring.sh --check`, not `--fix`. Per-verb acceptance for `--resume` and `--status` |
| **Unit 4** | the gate leg | Budget THREE `gate-legs.json` entries, not one. Witness PRESENCE is its own `fail` branch. Asserts at most one run-state file is in a non-terminal phase. Two-granularity population guard |
| **Unit 5** | the rendered skill | `.gitattributes` pin only — `check-wiring.sh`'s eol population is derived, so the script itself needs no edit. Drift and CRLF each need an acceptance criterion |
| **Unit 6** | the `/session-kickoff` hand-back | Enumerate all six interactive exits by line, not five. Needs the acceptance criterion it currently lacks: mandate present hands back, mandate absent still stops |
| **Unit 7** | the adopter path | Refuses a foreign repo and an unsupported prefix; ADOPTS correctly through a junction. Bumps the `governance-template` marker to v2.6 with a v2.5 archive snapshot — v2.5 was taken by aCandidStub on 2026-08-10 |

## Ratified decisions

Five forks were put to the owner on 2026-08-10 and all five resolved. Four more were raised by the
Tier-2 review and resolved the same day.

**F1** — the charter's explicit-ask rule for merge and push is amended narrowly to accept a
committed standing mandate naming the build and both actions. The review found the rule is written
in **four** live places, not the two the spec named, so the amendment set is `AGENTS.md`, the
playbook's §1 and §8, and `.claude/SESSION-KICKOFF.md`.

**F2** — FOLD, against the recommendation. The agent-cap work moved to `TOOL-aNumeralWarden-1`.

**F3** — the full protocol travels to adopters, with the phase vocabulary and the DoD assertion set
as project-owned declarations. The review added a floor: a kit-owned core set the project may only
extend, or deleting an item becomes a silent override that defeats F4.

**F4** — `--close` blocks, with a named and recorded override. The keepalive item is
agent-attested rather than machine-checked, so it does not spend the override budget.

**F5** — one build, one sub-spec per unit. Seven units.

**B1** (review) — `RUN.md` joins the check-4 whitelist and `index_set` with a check-7 exemption, and
does NOT join check 8. The unattended leg owns phase-vocabulary validation.

**B2** (review) — the run's BASE sha is an authored fact, the fifth. `gen_build_index.py` does not
derive it, so the generated region cannot carry it.

**B3** (review) — the keepalive splits by actor. The protocol owns scheduling and reaping; the
driver only records the id and asserts a recorded reap.

**B4** (review) — the master scope and this decision menu live here, not in the spec.

## Review record

`reviews/2026-08-10-review-aUnmannedHelm-1.md` — Tier-2 on the rev-2 spec. Five spec lenses over 57
raw findings, five batched default-refute skeptics, 50 confirmed at precision 0.88, no lens dead.
Eight blocker-severity findings collapsing to five distinct defects, all folded at rev-3.

Records live under `spec/`, `build/` and `reviews/`. The table below is
GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 2 unit(s) · node a · opened 2026-08-10 · streams tooling+kickoff+playbook+deployer · ids TOOL-aUnmannedHelm-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aUnmannedHelm-1 — the run-state file, and the hygiene contract that admits it](spec/2026-08-10-spec-aUnmannedHelm-1.md) | INPROGRESS | rev-4 | 2026-08-10 |
| [TOOL-aUnmannedHelm-4 — the protocol document, and the authorization it rests on](spec/2026-08-10-spec-aUnmannedHelm-4-u2-protocol.md) | INPROGRESS | rev-2 | 2026-08-10 |
<!-- /gen:build-index -->
