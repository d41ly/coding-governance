---
slug: aFusedCharter
node: a
opened: 2026-08-18
streams: playbook+tooling+deployer
roster: PLAY+TOOL+DEPL
ids: DEPL-aFusedCharter-1 PLAY-aFusedCharter-1 PLAY-aFusedCharter-2 PLAY-aFusedCharter-3 TOOL-aFusedCharter-1 TOOL-aFusedCharter-2 TOOL-aFusedCharter-3
---

# aFusedCharter — the playbook converges into one deployable charter, and the deploy path becomes mechanical

Node `a` · opened 2026-08-18 · streams playbook+tooling+deployer.

The product this repo ships is three root files. `parallel-coding-governance.template.md` is the
operating ruleset, `.domain-rules.md` holds nine activity-scoped sections the template reaches by
`§`-stub, and `.customize.md` is prose telling a human agent how to fill 38 placeholders by hand.
The owner's finding is that the split leaks: the companion falls out of the deploy path, and this
repo's own `AGENTS.md` — which the template is supposed to BECOME — has diverged from it with
nothing joining the two.

This build converges the product to a single file, deletes the sections that do not shape a session
regardless of project, makes the deploy path a program rather than a prose instruction, and joins
`AGENTS.md` to its source with a marker region a gate re-renders.

## Measured at BASE `497d25d0`

Every figure below was measured, not estimated, and each unit re-measures rather than carrying a
number out of this file.

| Quantity | Value |
|---|---|
| template · companion · customize | 36 828 · 23 482 · 8 999 bytes |
| naive merge against the 49 152 gate | over by ~10 KB |
| converged, after the four cuts below | 43 998 bytes — 5 154 under the ceiling |
| `AGENTS.md` total | 33 146 bytes |
| `AGENTS.md` gate-suite section alone | 26 222 bytes — 79 per cent of the file |
| lines over 450 chars — `AGENTS.md` · template · companion | 8 · 5 · 8 |

The converged file fits the EXISTING ceiling. No ceiling raise is specced, and a unit that finds
otherwise raises it as a fork rather than editing the constant.

## The four cuts, and the test each failed

The admission test is the owner's: does this instruction shape an OVERALL session, regardless of
project? Content that fails it leaves the ruleset.

| Cut | Bytes | Why it fails the test |
|---|---|---|
| `§4` Runtime isolation and the verification harness | 1 950 | Port offsets, seeded databases and a UI harness recipe. It governs standing up a local stack, which most repos do not have. |
| `§10`'s 25 recurring bug classes | 7 752 | A hand-kept generic list, half of it web and database specific. The mechanism that actually works is per-project and diff-scoped, and this repo already ships it. |
| `§13` Visual consistency | 2 359 | A design system governs UI work only. |
| `§17` User-facing file references | folded | One rule about output; it belongs inside `§16`, not beside it. |

Two further trims are content, not sections: the kit-advertisement prose in `§5`, `§6` and `§7`
moves to `WIRE-INTO-PROJECT.md`, which is where a reader deciding what to install actually looks;
and `§8`'s 1 499-character bullet spelling the `agent-cap` hook's marker grammar moves to that
hook's own README, leaving the two caps and the fact that a hook enforces them.

## Units — the authored roster (M2)

One mechanism per unit. Each cell is a label; the unit's `§1` Goal owns the statement.

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `PLAY-aFusedCharter-1` | 2 | the converged document |
| 2 | `TOOL-aFusedCharter-1` | 2 | the file-surface migration and every consumer of it |
| 3 | `PLAY-aFusedCharter-2` | 2 | the session-slug micro-format block |
| 4 | `DEPL-aFusedCharter-1` | 2 | the playbook renderer — the deploy path becomes a program |
| 5 | `PLAY-aFusedCharter-3` | 2 | `AGENTS.md` — the rendered region, and the admission cut that pays for it |
| 6 | `TOOL-aFusedCharter-2` | 2 | the micro-format definition gate |
| 7 | `TOOL-aFusedCharter-3` | 2 | the line-length gate |

## The order is TOTAL

**Units 1 and 2 land in ONE pass.** Unit 1 deletes `parallel-coding-governance.domain-rules.md`, and
three legs name that file by path — `check-placeholders.sh` refuses when either marker carrier is
absent, `check-playbook-parity.sh` stats all three files before it starts, and `govkit selfcheck`
asserts the tracked surface against `registry.toml`. Landing unit 1 without unit 2 is a red bar, and
a pass whose gate is red is not followed by another. The two specs stay separate because the
document and its consumer surface are different mechanisms with different failure modes, but they
share a landing.

Then `3` (the block is content inside the document unit 1 produced) → `4` (the renderer reads the
conditional markers unit 1 adds) → `5` (`AGENTS.md` receives what unit 4 renders, which is also what
makes unit 4's `--check` leg non-vacuous) → `6` (the gate grades the block unit 3 wrote) → `7` last,
because it reds on any carrier not yet wrapped and every earlier unit rewrites one.

**There is no separate render-parity unit.** An earlier draft carried one; `DEPL-aFusedCharter-1` F3
resolved that re-render-and-compare is `adopt-playbook.sh --check`, which is this repo's established
wiring-leg idiom and already how three other kits prove the same property.

## Build-level rules

- **The version marker moves once, at the integration boundary.** Today two files carry
  `<!-- governance-template: vN.N -->` and `check-placeholders.sh` asserts they agree. After unit 1
  there is one carrier, which changes that gate's population from a comparison to a presence check —
  unit 2 owns the amendment, and unit 2 owns the single marker bump.
- **Every unit that touches the converged file re-measures with `bash tools/check-template-size.sh`.**
  Read from the gate, never carried between specs as a remembered number.
- **No spec id in this build may be cited from product source while its status is non-terminal.**
  The drift signal `non_terminal_specs_cited_by_product_source` sits at a zero-tolerance pin, and
  its `PRODUCT_GLOBS` cover the playbook files, `WIRE-INTO-PROJECT.md`, `tools/`, `skills/`,
  `.claude/` and `memory/guides/SESSION-KICKOFF.md`. Those are the files these units edit.
- **`AGENTS.md` is `.memory-tree.conf`'s `CHARTER`.** Unit 5 restructures it, so the hygiene checks
  keyed on the charter are that unit's gates, not an afterthought.
- **Adding a gate leg trips a growing set of meta-gates.** Units 6 and 7 each add one, so each runs
  the full bar rather than a list remembered from here — measured on 2026-08-18, the set included
  map freshness, the kickoff ratchet, `govkit selfcheck` and its selftest.

## Owner decisions — RESOLVED 2026-08-18

Put to the owner at kickoff and answered before any spec was written.

| Fork | Resolution |
|---|---|
| How `AGENTS.md` joins the template | A `gov:playbook` marker region holding the render, project content in authored slots outside it, a gate re-rendering and byte-comparing — paired with an admission cut over the gate-suite section. |
| Where `§10`'s 25 bug classes go | Deleted outright. The template keeps one rule pointing at the project's own checklist. |
| How binding the micro-format is | Doc-binding plus a gate over the DEFINITIONS. Emission stays a documented pre-send check. |
| Which further trims | The kit-advertisement prose, `§8`'s agent-cap hook grammar, and `§17` folded into `§16`. |

The owner's correction that produced the first row is recorded because it refutes a design this
session proposed: `AGENTS.md` cannot import a second playbook file, because `@`-imports are Claude
Code syntax and `AGENTS.md` exists precisely so that Codex, Cursor, Copilot and Windsurf read it
NATIVELY — those tools would render the import line as literal text.

<!-- gen:build-index -->
**Build status:** OPEN · 7 unit(s) · node a · opened 2026-08-18 · streams playbook+tooling+deployer
ids DEPL-aFusedCharter-1 PLAY-aFusedCharter-1 PLAY-aFusedCharter-2 PLAY-aFusedCharter-3 TOOL-aFusedCharter-1 TOOL-aFusedCharter-2 TOOL-aFusedCharter-3

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [DEPL-aFusedCharter-1 — the deploy path becomes a program, and the customize companion retires](spec/2026-08-18-spec-DEPL-aFusedCharter-1.md) | OPEN | rev-1 | 2026-08-18 |
| [PLAY-aFusedCharter-1 — the playbook converges into one file, and loses what does not govern a session](spec/2026-08-18-spec-PLAY-aFusedCharter-1.md) | OPEN | rev-1 | 2026-08-18 |
| [PLAY-aFusedCharter-2 — every session emits a shaped overview of its own state, and the shapes get one grammar](spec/2026-08-18-spec-PLAY-aFusedCharter-2.md) | OPEN | rev-1 | 2026-08-18 |
| [PLAY-aFusedCharter-3 — AGENTS.md becomes a rendered region plus authored slots, and stops re-narrating its own gate manifest](spec/2026-08-18-spec-PLAY-aFusedCharter-3.md) | OPEN | rev-1 | 2026-08-18 |
| [TOOL-aFusedCharter-1 — the product becomes one tracked path, and every consumer of the old three is repointed](spec/2026-08-18-spec-TOOL-aFusedCharter-1.md) | OPEN | rev-1 | 2026-08-18 |
| [TOOL-aFusedCharter-2 — the micro-format definitions become machine-gradeable against their own grammar](spec/2026-08-18-spec-TOOL-aFusedCharter-2.md) | OPEN | rev-1 | 2026-08-18 |
| [TOOL-aFusedCharter-3 — an instruction file's lines get a declared maximum, defaulting to 450 characters](spec/2026-08-18-spec-TOOL-aFusedCharter-3.md) | OPEN | rev-1 | 2026-08-18 |

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
  - [2026-08-18-spec-DEPL-aFusedCharter-1.md](spec/2026-08-18-spec-DEPL-aFusedCharter-1.md)
  - [2026-08-18-spec-PLAY-aFusedCharter-1.md](spec/2026-08-18-spec-PLAY-aFusedCharter-1.md)
  - [2026-08-18-spec-PLAY-aFusedCharter-2.md](spec/2026-08-18-spec-PLAY-aFusedCharter-2.md)
  - [2026-08-18-spec-PLAY-aFusedCharter-3.md](spec/2026-08-18-spec-PLAY-aFusedCharter-3.md)
  - [2026-08-18-spec-TOOL-aFusedCharter-1.md](spec/2026-08-18-spec-TOOL-aFusedCharter-1.md)
  - [2026-08-18-spec-TOOL-aFusedCharter-2.md](spec/2026-08-18-spec-TOOL-aFusedCharter-2.md)
  - [2026-08-18-spec-TOOL-aFusedCharter-3.md](spec/2026-08-18-spec-TOOL-aFusedCharter-3.md)
<!-- /gen:build-docs -->
