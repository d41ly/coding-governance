---
slug: cKeyedLaunchpad
node: c
opened: 2026-08-13
streams: kickoff+tooling
roster: KICK+TOOL
ids: KICK-cKeyedLaunchpad-1 KICK-cKeyedLaunchpad-2 KICK-cKeyedLaunchpad-3 KICK-cKeyedLaunchpad-4 KICK-cKeyedLaunchpad-6 KICK-cKeyedLaunchpad-7 TOOL-cKeyedLaunchpad-5
---

# cKeyedLaunchpad — the kickoff kit re-grounded, and the manifest it reads put under gates

Node `c` · opened 2026-08-13 · streams kickoff+tooling.

The session-kickoff kit is the one part of this repo that every session runs and no gate grades. An
adversarial review at BASE `f006691` found the engine executing on this node is a copy from
2026-07-15, fifty-one lines shorter than the tracked one. It is missing Step 5b entirely. The
manifest search order is spelled in five files with no authority among them. The ratchet gate checks
six structural signals and has no opinion on size, so an adopter manifest of 77,056 bytes carrying a
single 16,266-character line passes it clean.

This build closes those. It re-grounds the engine on the tooling the repo actually ships, moves the
manifest to a home the memory tree governs, and extends the ratchet with the three checks that would
have caught the drift the review found by hand.

This README is the **master overview and the owner decision menu**, per `memory/TEMPLATE-SPEC.md`.
Each unit below becomes its own conforming sub-spec under `spec/`.

## Start here

**State.** Design pass complete and REVIEWED TWICE. The M4 audit returned BLOCKED with 18 confirmed
defects; the fix-verify pass over the fold returned BLOCKED again with 19 more, including the same U6
arithmetic a second time. Both folds are in. Units 2, 3, 5, 6 and 7 are at rev-3; units 1 and 4 at
rev-2.

**Next action:** owner scope approval, then build in dependency order. `BUILD-METHOD.md` M4 says to
STOP once a synthesis calls the design clean and its fixes are folded — further passes land in the
prose about the design rather than in the design, and building is both cheaper and stricter.

**Build order**, corrected by the fix-verify pass: `-1` (independent) then `-2`, `-3`, `-4`, `-5`,
`-6`, `-7`. U5 is no longer front-loadable — taking the `--for-paths` call site gave it an edge to U2.
Authoring was
SEQUENCED, not parallel: U3 reads U2's location interface and U6 reads U3's ceiling, so
`BUILD-METHOD.md` M6's disjoint-write-set test fails on the contract axis even though the six files
do not collide. Grounding research was fanned out; authoring is not.

**BASE** is `f006691f7cd2231dcb95152972f1998dfe8358e4`, on `branch/session-kickoff-skill-review-0c76ec`.

## The findings this build answers

Each row is a defect the review reproduced against source at BASE. The unit column is where it is
fixed.

| # | Finding | Evidence | Unit |
|---|---|---|---|
| F1 | The installed engine is a stale copy, not the junction `AGENTS.md` claims | `LinkType` empty on `~/.claude/skills/session-kickoff`; 183 lines against the tracked 234 | U1 |
| F2 | The manifest search order is spelled in five files, none authoritative | `SKILL.md:70`, `manifest-check.sh:54`, `manifest-check.sh:58`, `WIRE-INTO-PROJECT.md:330`, `SKILL.md:224` | U2 |
| F3 | The ratchet gates structure only, never size or prose | The NicoCares manifest is 77,056 B with a 16,266-char line and exits 0 | U3 |
| F4 | §A carries no binding and is fully hand-authorable | Deleting §A leaves every check green | U4 |
| F5 | The traps section is 69% of this repo's manifest and duplicates `memory/gotchas/` | 14,665 of 21,170 B; 27 bullets against 13 class records | U5, U6 |
| F6 | Scaffolding writes `docs/` and `scripts/`, contradicting the runbook | `SKILL.md:224` against `WIRE-INTO-PROJECT.md:353`, which itself still emits `scripts/` at line 366 | U2 |
| F7 | The engine has no size gate, in a repo that byte-gates its playbook at 32 KiB | `SKILL.md` is 15,604 B and ungated | U7 |

## Units

Classification is `BUILD-METHOD.md` M2, first match wins. A unit is MISSING until a conforming spec
carries its id.

| Unit | Id | Mechanism | Tier | Class | Depends on |
|---|---|---|---|---|---|
| U1 | `KICK-cKeyedLaunchpad-1` | skill-install freshness reported by `check-wiring.sh` | 1 | rev-2, reviewed | none |
| U2 | `KICK-cKeyedLaunchpad-2` | the manifest location list, single-sourced and re-ordered | 2 | rev-3, reviewed | none |
| U3 | `KICK-cKeyedLaunchpad-3` | ratchet checks C7 size, C8 line length, C9 stamp age | 2 | rev-3, reviewed | U2 |
| U4 | `KICK-cKeyedLaunchpad-4` | the sealed task region and its byte-compare | 2 | rev-2, reviewed | U3 |
| U5 | `TOOL-cKeyedLaunchpad-5` | `gotchas.py --for-paths`, the anchor selector without a diff | 1 | rev-3, reviewed | U2 |
| U6 | `KICK-cKeyedLaunchpad-6` | traps evicted from the manifest, and a ceiling so they cannot return | 2 | rev-3, reviewed | U3, U5 |
| U7 | `KICK-cKeyedLaunchpad-7` | the engine's prose pass and its size gate | 1 | rev-3, reviewed | U2, U4, U5, U6 |

**Only U1 is fully independent.** U5 gained an edge to U2 when it took the `--for-paths` call site
(its Step 4 edit must follow U2's engine restructure), and U7 gained edges to U4 and U5 because both
now write `SKILL.md` and U7's size limit is measured AFTER every other edit to that file. The M4
fix-verify pass found all three edges missing, which is how a build order stays plausible while being
wrong.

## Owner decisions — where the manifest lives

All three were resolved by the owner at kickoff, before any spec was authored. Each unit's §8 carries
the mark in place.

| Decision | Pick | Consequence |
|---|---|---|
| Where the primary manifest lives | `memory/guides/SESSION-KICKOFF.md` | Probed clean against hygiene and method-carriers. Strands the `.claude/` row in `memory/project/method-carriers.txt`, which U2 must move. |
| Whether the manifest stays on drift-audit's product surface | Add the explicit path to `PRODUCT_GLOBS` | U2 becomes a three-kit change and moves a drift-audit pin. |
| The third manifest location | The skill base directory, as a machine-global fallback | It sits outside every repo, so no project gate can reach it. U2 must make the engine skip Step 2b for it and say so in the READY card. |

## Owner decisions — what the new gates do

All three were put to the owner at kickoff and resolved before any unit spec was authored. Each
unit's §8 carries the mark in place, naming the owner as resolver.

1. **The C7 size ceiling is a hard red from day one.** RESOLVED (owner, 2026-08-13). The WARN-then-red
   option was declined. The consequence is accepted and named here so it is not rediscovered: the
   NicoCares manifest at 77,056 B reds the moment that repo pulls the kit update, and its cleanup is a
   follow-up that repo owns. This build does not retrofit it, per the OUT list.
2. **C9 reuses the `aRatchetForge` maintenance-stall thresholds.** RESOLVED (owner, 2026-08-13):
   ten watch-pathspec commits, or three months, with zero manifest body growth. Verified at source in
   `memory/builds/aRatchetForge/spec/manifest-ratchet-spec.md` §10.9. That spec deliberately left the
   rule to an owner-read review rather than a gate, because the delta lines it would have read live in
   commit messages and READY cards that squash merges do not preserve.
3. **U6 evicts the bug-class traps and caps the remainder.** RESOLVED (owner, 2026-08-13). Traps that
   are recurring bug classes become `memory/gotchas/` records reachable through U5's `--for-paths`
   selector. Traps that are genuinely machine-local stay in the manifest under a hard bullet cap.
4. **C9 reads a recorded baseline, not git history.** RESOLVED (owner, 2026-08-13), after the M4 audit
   reproduced the blocker: a path-scoped `git log --name-status` reports a `git mv` as an ADD, so the
   history walk would have read unit 2's own move as the manifest's birth and reported a stalled
   manifest as freshly maintained. The audit block gains a `last-body-change` sha instead. This also
   settles what CLEARS a C9 red, which the walk design had no answer for — advancing that key.
5. **U6 rewrites the surviving over-cap trap bullets.** RESOLVED (owner, 2026-08-13), after the audit
   measured that deletion alone could not reach the target: 19 of 27 bullets exceed 400 bytes, and
   three the eviction KEEPS are over the cap the same unit introduces.

## How the build phase is authorized

The unattended kit's preflight REFUSED this run, correctly, and the refusal is recorded rather than
worked around:

```
UNATTENDED check 6 FAILED — no build README at the pinned BASE, so nothing committed
before this run branched authorizes it, and a build folder the run created on its own
branch authorizes nothing
```

This session created `memory/builds/cKeyedLaunchpad/` on its own branch, so the folder cannot be its
own mandate. Nothing was back-dated and no spec was pushed early to make the check pass; the mandate
mechanism is simply unused here.

The build phase runs instead on the OTHER authorization the charter grants — the owner's explicit ask,
given in chat naming both the merge and the push, and scoped to "when the entire build is fully done".
`AGENTS.md` states the two as alternatives: an explicit ask, **or** a committed build folder the run
did not create. This run has the first and not the second.

The practical difference, so a later reader is not misled: there is no `RUN.md`, no phase field and no
machine-checkable Definition-of-Done for this run. The discipline is `BUILD-METHOD.md`'s and the
record is this README plus the commit log.

## The invariant the audit earned

Three of the eighteen confirmed defects (H6, H7, M4) were one failure wearing three faces: **a §3
non-goal handed an obligation to a named sibling that never accepted it, and no gate detects the
orphan.** `READ_PATH_CEILING` was raised by unit 2 and lowered by nobody. The `--for-paths` verb was
built by unit 5, its only call site delegated to unit 7, which never mentioned it — so unit 6 would
have deleted eight manifest bullets in favour of a path nothing in the build opens. Step 3's
Risk-tier bullet was edited by units 4 and 7 in opposite directions.

The cheap invariant, adopted for this build and worth carrying to the method: **every §3 bullet that
names a sibling unit must be matched by an S-item in that sibling.** It is checkable by reading two
sections, and it would have caught all three at authoring time.

Left-shifting it into a gate is not free — §3 prose is not machine-parseable — so it is a reading
rule here, and a candidate `BUILD-METHOD.md` M2 clause if it earns its keep on a second build.

## Parked

Written per `BUILD-METHOD.md` M6: the question, the options seen, and the reason it was refused. A
bare "parked" is indistinguishable from "forgotten".

1. **`AGENTS.md` is gated by nothing.** Grounding for U2 found that the charter can cite a file that
   does not exist and the full bar stays green. Hygiene check 15's dead-path population is `memory/`
   only, and `check-install-prefix.sh`'s population is `tools/*`, `skills/*`, `.githooks/*`, the
   template families and `WIRE-INTO-PROJECT.md`. Neither reaches `AGENTS.md`. Options seen: widen
   check 15's population to the charter, add a charter-scoped path check, or accept it. Refused here
   because it is a new gate over a file outside this build's scope, and U2 already carries three
   kits. It matters because `AGENTS.md:54` is one of the paths U2 rewrites, so the interval where it
   could be wrong is real.
2. **The kit/dogfood parity leg's guard does not cover its own live half.** The leg guards on
   `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `tools/lib/` and `tools/memory-tree/`, but the
   pair it validates includes `memory/guides/BUILD-METHOD.md`. A diff-scoped run touching only the
   live copy skips the leg; only `GATE_FULL=1` catches it. Options seen: add the guide paths to the
   guard, or rely on the pre-push full bar. Refused here because changing a leg guard is a merge-bar
   change with its own blast radius. U2 works around it by requiring a `GATE_FULL=1` run.

## Unit index

Records live under `spec/`, `build/` and `reviews/`. The table below is GENERATED from the status
header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** OPEN · 7 unit(s) · node c · opened 2026-08-13 · streams kickoff+tooling · ids KICK-cKeyedLaunchpad-1 KICK-cKeyedLaunchpad-2 KICK-cKeyedLaunchpad-3 KICK-cKeyedLaunchpad-4 KICK-cKeyedLaunchpad-6 KICK-cKeyedLaunchpad-7 TOOL-cKeyedLaunchpad-5

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [KICK-cKeyedLaunchpad-1 — the installed engine, and why link-ness is the wrong thing to check](spec/2026-08-13-spec-cKeyedLaunchpad-1.md) | OPEN | rev-2 | 2026-08-13 |
| [KICK-cKeyedLaunchpad-2 — one location list, and the three kits the move drags in](spec/2026-08-13-spec-cKeyedLaunchpad-2.md) | OPEN | rev-3 | 2026-08-13 |
| [KICK-cKeyedLaunchpad-3 — three checks the ratchet never had, and the stall it can actually measure](spec/2026-08-13-spec-cKeyedLaunchpad-3.md) | OPEN | rev-3 | 2026-08-13 |
| [KICK-cKeyedLaunchpad-4 — the sealed task region, and the duplication it must remove rather than ratify](spec/2026-08-13-spec-cKeyedLaunchpad-4.md) | OPEN | rev-2 | 2026-08-13 |
| [TOOL-cKeyedLaunchpad-5 — the anchor selector without a diff, and the latent split it exposes](spec/2026-08-13-spec-cKeyedLaunchpad-5.md) | OPEN | rev-3 | 2026-08-13 |
| [KICK-cKeyedLaunchpad-6 — evicting the traps that pay, and restoring the cap the kit already shipped](spec/2026-08-13-spec-cKeyedLaunchpad-6.md) | OPEN | rev-3 | 2026-08-13 |
| [KICK-cKeyedLaunchpad-7 — the engine's prose pass, and the three strings it must not touch](spec/2026-08-13-spec-cKeyedLaunchpad-7.md) | OPEN | rev-3 | 2026-08-13 |
<!-- /gen:build-index -->

## Method

`memory/guides/BUILD-METHOD.md`, multi-pass. The M5 reuse probes were run at kickoff and their
results belong in each spec's §10.

```bash
python tools/codebase-map/reuse_lookup.py "gate a document's size and line length"
python tools/memory-recall/query.py "why does the kickoff manifest live where it does and what gates its prose" --terms "kickoff manifest ratchet last-audit watch verify-paths SESSION-KICKOFF discovery order traps accretion size gate prose"
```

The size-gate probe returned `tools/check-template-size.sh` as the nearest seam. It is the wrong one
to extend: it is a gov-only gate leg over a single file, and these checks must ride
`manifest-check.sh` so that adopters inherit them when they re-pull the kit. That is a recorded miss,
not a skipped audit.
