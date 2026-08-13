---
slug: cKeyedLaunchpad
node: c
opened: 2026-08-13
status: OPEN
streams: kickoff+tooling
roster: KICK+TOOL
ids: KICK-cKeyedLaunchpad-1..-4 KICK-cKeyedLaunchpad-6..-7 TOOL-cKeyedLaunchpad-5
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

**State.** Design pass. Seven units decomposed and classified; all seven are MISSING. No code is
written and none may be until each unit's spec is authored and reviewed, per `BUILD-METHOD.md` M2's
hard floor.

**Next action:** author the seven unit specs, then run the M4 spec audit over the set.

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

Classification is `BUILD-METHOD.md` M2, first match wins. All seven are MISSING because no
conforming spec carries their id yet.

| Unit | Id | Mechanism | Tier | Class | Depends on |
|---|---|---|---|---|---|
| U1 | `KICK-cKeyedLaunchpad-1` | skill-install freshness reported by `check-wiring.sh` | 1 | MISSING | none |
| U2 | `KICK-cKeyedLaunchpad-2` | the manifest location list, single-sourced and re-ordered | 2 | MISSING | none |
| U3 | `KICK-cKeyedLaunchpad-3` | ratchet checks C7 size, C8 line length, C9 stamp age | 2 | MISSING | U2 |
| U4 | `KICK-cKeyedLaunchpad-4` | the sealed §A region and its byte-compare | 2 | MISSING | U3 |
| U5 | `TOOL-cKeyedLaunchpad-5` | `gotchas.py --for-paths`, the anchor selector without a diff | 1 | MISSING | none |
| U6 | `KICK-cKeyedLaunchpad-6` | traps evicted from the manifest, and a ceiling so they cannot return | 2 | MISSING | U3, U5 |
| U7 | `KICK-cKeyedLaunchpad-7` | the engine's prose pass and its size gate | 1 | MISSING | U2, U6 |

U1 and U5 depend on nothing and are Tier 1. They can be specced and built while the Tier-2 units are
still in review.

## Owner decisions already taken

Both were resolved by the owner at kickoff, before any spec was authored. Each unit's §8 carries the
mark in place.

| Decision | Pick | Consequence |
|---|---|---|
| Where the primary manifest lives | `memory/guides/SESSION-KICKOFF.md` | Probed clean against hygiene and method-carriers. Strands the `.claude/` row in `memory/project/method-carriers.txt`, which U2 must move. |
| Whether the manifest stays on drift-audit's product surface | Add the explicit path to `PRODUCT_GLOBS` | U2 becomes a three-kit change and moves a drift-audit pin. |
| The third manifest location | The skill base directory, as a machine-global fallback | It sits outside every repo, so no project gate can reach it. U2 must make the engine skip Step 2b for it and say so in the READY card. |

## Open forks for the owner

These are scope questions, which M3 does not delegate. None blocks spec authoring; each blocks its
own unit's build.

1. **The C7 size ceiling applies to which manifests?** A 25 KiB cap reds the NicoCares manifest at
   77,056 B the moment that repo pulls the kit update. Options are a hard red, a WARN that becomes a
   red at a declared date, or a per-repo declared ceiling with 25 KiB as the default. Recommendation
   is the dated WARN, because the kit ships to repos this build does not control.
2. **What C9 measures as staleness.** C5 already reds on watch drift, so C9 is about a manifest
   nothing has touched. The `aRatchetForge` build specced a maintenance-stall review at ten watch
   commits or three months with zero body growth. Recommendation is to reuse that threshold rather
   than mint a new one.
3. **Whether U6 evicts traps or caps them.** Eviction moves each trap to `memory/gotchas/` as a
   class record, which costs a dossier claim and an index render per record. A cap alone leaves the
   traps in place but bounded. Recommendation is eviction for the bug-class traps and a cap for the
   machine-local remainder, which is the split the review found.

## Unit index

Records live under `spec/`, `build/` and `reviews/`. The table below is GENERATED from the status
header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node c · opened 2026-08-13 · streams kickoff+tooling · ids KICK-cKeyedLaunchpad-1..-4 KICK-cKeyedLaunchpad-6..-7 TOOL-cKeyedLaunchpad-5

*No spec under this build carries a status header; the status above is declared in the front matter.*
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
