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

**Units matter here and the spec audit caught them mixed.** `check-template-size.sh` enforces BYTES;
the fold projection and the section inventories below were measured in CHARACTERS, and the two differ
by about one per cent over this corpus because of the non-ASCII glyphs. Every row states its unit.

| Quantity | Value | Unit |
|---|---|---|
| template · companion · customize, on disk | 36 828 · 23 482 · 8 999 | bytes |
| naive merge against the 49 152 gate | over by ~10 KB | bytes |
| converged projection, after the four cuts below | ~44 400 | bytes |
| the same projection as first measured | 43 998 | characters |
| `AGENTS.md` total | 33 146 chars / 33 413 | both |
| `AGENTS.md` gate-suite section alone | 26 222 chars — 79 per cent of the file | characters |
| lines over 450 — `AGENTS.md` · template · companion | 8 · 4 · 8 | characters |
| longest line — `AGENTS.md` · template | 1 047 · 1 474 | characters |
| recorded size high-water for the template | 37 381 | bytes |

Two corrections the audit forced, both kept rather than smoothed over. The ruleset has **four** lines
over 450 characters, not five — one line measures 462 bytes and 449 characters and is already
compliant. And the converged projection is ~44 400 BYTES, not 43 998, so the headroom against 49 152
is roughly 4.7 KB rather than 5.2 KB.

The converged file still fits the EXISTING ceiling on the projection, but **the projection is not a
measurement**: it depends on prose `PLAY-aFusedCharter-1` S6, S7 and S10 have not written yet. The
build measures the real file and, if it does not fit, raises a fork rather than editing the constant.

The high-water record is a separate obligation the audit surfaced: the converged file lands ~7 KB
above the recorded 37 381, so `check-template-size.sh` would print its advisory growth WARN on every
run thereafter until somebody re-records it. `TOOL-aFusedCharter-3` owns the `--bump`, because it is
the last unit to touch the file.

## The four cuts, and the test each failed

The admission test is the owner's: does this instruction shape an OVERALL session, regardless of
project? Content that fails it leaves the ruleset. Sizes below are CHARACTERS, like every other
section inventory in this build — the size ceiling is in BYTES and the two differ by about one per
cent over this corpus.

| Cut | Characters | Why it fails the test |
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

**The charter-completeness signal is retired by unit 2, not unit 5, and that is a blocker the spec
audit found.** `handkept_inventories_disagreeing_with_source` measures `0 of 70` against a pin of 0
and is gateable: it reds the moment any leg's argv script path is absent from `AGENTS.md`'s
gate-suite section. Units 4, 6 and 7 each ADD a leg, and the charter bullets that would name them
only arrive at unit 5 — so on the stated order, three units red `drift-audit records` with no unit
owning the fix. Retiring the signal in unit 2 costs nothing, because between unit 2 and unit 5 the
charter still names every pre-existing leg and unit 5 deletes the section it grades anyway.

## Build-level rules

- **The version marker moves once, at the integration boundary.** Today two files carry
  `<!-- governance-template: vN.N -->` and `check-placeholders.sh` asserts they agree. After unit 1
  there is one carrier, which changes that gate's population from a comparison to a presence check —
  unit 2 owns the amendment, and unit 2 owns the single marker bump.
- **Every unit that touches the converged file re-measures with `bash tools/check-template-size.sh`.**
  Read from the gate, never carried between specs as a remembered number.
- **No spec id in this build may be cited from product source while its status is non-terminal.**
  The drift signal `non_terminal_specs_cited_by_product_source` reads `2 of 60 ok (pin 2)`, and BOTH
  slots are already spent by `TOOL-aBatchedLintel-1` and `TOOL-aGuardedTally-1`. It is not a
  zero-tolerance pin — an earlier version of this line said so — but the predicate is `value > pin`,
  so any citation from this build reds it just the same, and if either of those two units closes
  mid-build the rule silently loosens instead. Its `PRODUCT_GLOBS` cover the playbook files,
  `WIRE-INTO-PROJECT.md`, `tools/`, `skills/`, `.claude/` and `memory/guides/SESSION-KICKOFF.md` —
  which are the files these units edit.
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

### The second round — RESOLVED 2026-08-18

Three forks the spec audit left open or created, put to the owner together and answered. Each is
marked in place in its own spec's `§8`.

| Fork | Resolution |
|---|---|
| `TOOL-1` F2 — where the parity gate's two value-parity rows take their stated side from | KEEP them in the playbook. The gate's subject is the playbook's own claims, and moving the stated side into a file the playbook does not ship changes what the gate is for. No scope change; `PLAY-1` S7 was already written against this answer. |
| `PLAY-3` F1 — a byte ceiling for the charter, and over what | YES, over the WHOLE file, seeded at the landed measurement plus headroom. The rejected option priced the authored half alone, which needs a region-aware measurement mode the size gate lacks. This flips a Non-goal into new scope. |
| `DEPL-1` F4 — where the target descriptor lives | KEEP `.governance/deploy.toml`. The four root confs are tuning knobs; this is a committed authorization artifact that `intake` writes once and every deployer verb reads there. No scope change. |

The whole-file answer to `PLAY-3` F1 accepts an apparent double-count deliberately: the region is
already priced by the ruleset's own ceiling, and pricing it again in the charter is the honest
reading rather than a flaw. If the ruleset grows five kilobytes, gov's charter really did become five
kilobytes more expensive to read every session, and a ceiling that hid that would price the wrong
thing.

The owner's correction that produced the first row is recorded because it refutes a design this
session proposed: `AGENTS.md` cannot import a second playbook file, because `@`-imports are Claude
Code syntax and `AGENTS.md` exists precisely so that Codex, Cursor, Copilot and Windsurf read it
NATIVELY — those tools would render the import line as literal text.

<!-- gen:build-index -->
**Build status:** OPEN · 7 unit(s) · node a · opened 2026-08-18 · streams playbook+tooling+deployer
ids DEPL-aFusedCharter-1 PLAY-aFusedCharter-1 PLAY-aFusedCharter-2 PLAY-aFusedCharter-3 TOOL-aFusedCharter-1 TOOL-aFusedCharter-2 TOOL-aFusedCharter-3

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [DEPL-aFusedCharter-1 — the deploy path becomes a program, and the customize companion retires](spec/2026-08-18-spec-DEPL-aFusedCharter-1.md) | OPEN | rev-5 | 2026-08-18 |
| [PLAY-aFusedCharter-1 — the playbook converges into one file, and loses what does not govern a session](spec/2026-08-18-spec-PLAY-aFusedCharter-1.md) | OPEN | rev-3 | 2026-08-18 |
| [PLAY-aFusedCharter-2 — every session emits a shaped overview of its own state, and the shapes get one grammar](spec/2026-08-18-spec-PLAY-aFusedCharter-2.md) | OPEN | rev-3 | 2026-08-18 |
| [PLAY-aFusedCharter-3 — AGENTS.md becomes a rendered region plus authored slots, and stops re-narrating its own gate manifest](spec/2026-08-18-spec-PLAY-aFusedCharter-3.md) | OPEN | rev-4 | 2026-08-18 |
| [TOOL-aFusedCharter-1 — the product becomes one tracked path, and every consumer of the old three is repointed](spec/2026-08-18-spec-TOOL-aFusedCharter-1.md) | OPEN | rev-5 | 2026-08-18 |
| [TOOL-aFusedCharter-2 — the micro-format definitions become machine-gradeable against their own grammar](spec/2026-08-18-spec-TOOL-aFusedCharter-2.md) | OPEN | rev-3 | 2026-08-18 |
| [TOOL-aFusedCharter-3 — an instruction file's lines get a declared maximum, defaulting to 450 characters](spec/2026-08-18-spec-TOOL-aFusedCharter-3.md) | OPEN | rev-3 | 2026-08-18 |

Records live under `spec/`, `build/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-18-build-PLAY-aFusedCharter-1-1-conditional-enumeration.md](build/2026-08-18-build-PLAY-aFusedCharter-1-1-conditional-enumeration.md) | journal | PLAY-aFusedCharter-1 DEPL-aFusedCharter-1 |
| [2026-08-18-review-PLAY-aFusedCharter-1-1.md](reviews/2026-08-18-review-PLAY-aFusedCharter-1-1.md) | spec-audit | PLAY-aFusedCharter-1 PLAY-aFusedCharter-2 PLAY-aFusedCharter-3 TOOL-aFusedCharter-1 TOOL-aFusedCharter-2 TOOL-aFusedCharter-3 DEPL-aFusedCharter-1 |
| [2026-08-18-review-PLAY-aFusedCharter-1-2.md](reviews/2026-08-18-review-PLAY-aFusedCharter-1-2.md) | spec-audit | PLAY-aFusedCharter-1 PLAY-aFusedCharter-2 PLAY-aFusedCharter-3 TOOL-aFusedCharter-1 TOOL-aFusedCharter-2 TOOL-aFusedCharter-3 DEPL-aFusedCharter-1 |
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
- **`build/`**
  - [2026-08-18-build-PLAY-aFusedCharter-1-1-conditional-enumeration.md](build/2026-08-18-build-PLAY-aFusedCharter-1-1-conditional-enumeration.md)
- **`reviews/`**
  - [2026-08-18-review-PLAY-aFusedCharter-1-1.md](reviews/2026-08-18-review-PLAY-aFusedCharter-1-1.md)
  - [2026-08-18-review-PLAY-aFusedCharter-1-2.md](reviews/2026-08-18-review-PLAY-aFusedCharter-1-2.md)
<!-- /gen:build-docs -->
