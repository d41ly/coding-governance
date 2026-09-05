---
slug: aHoistedPass
node: a
opened: 2026-09-04
streams: tooling+deployer
roster: TOOL+DEPL
parents: dBriefedPass dRatifiedSeam
ids: DEPL-aHoistedPass-1 TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9
---

# aHoistedPass — the harnessed build pass, actually reachable, actually per-unit, and a ratchet that keeps it reachable

## The problem this build exists to solve

`dBriefedPass` built the harness that makes a build's pass order a property of a program rather than
of an agent's recollection. `dRatifiedSeam` fixed its AUDIT stage, which until then asked a sidechain
agent for a tool a sidechain does not hold, so BUILD was structurally unreachable through it. Both
landed. Runs since have used none of it, and three independent defects explain why.

**No route.** `passes-harnessed:M6` is declared in `DIRECTIVES_CORE` and shown to every run in the
Skill's directive table, and the section it points at states no harness rule. `grep -c
unattended-build memory/guides/BUILD-METHOD.md` is 0 and **0 of 17 core handles appear in that file at
all**. The gate grading the pointer, check 16 arm B, asserts only that the cited section EXISTS. A run
that resolves the handle reads M6, finds nothing, and builds inline. This was found as finding M9 of
`dBriefedPass`'s own closing diff review and never landed.

**Wrong shape.** The harness's BUILD stage is ONE `agent()` handed the whole roster, so orientation is
a request inside a prompt rather than a property of the program. Over 85 builds the median roster is 4
and the maximum is 30.

**No witness.** The harness writes nothing to disk. `dRetiredFork` ran without it and produced `brief`
rows byte-identical to what a harnessed run writes, so those rows witness nothing about the harness.

## Expected improvements

- A run reading its bound directives finds the rule where the directive says it is.
- Each build unit is built by an agent holding that unit's spec and brief, not the roster.
- Every per-unit dispatch is a main-loop tool call, so the fan-out guard sees it at all.
- The pointer gate stops being satisfiable by a section that says nothing.
- A budget declared in prose and read by nobody becomes a budget a gate reads.
- An adopter without the harness is told so, at install and on every bar, instead of silently
  carrying a core directive naming a file that is not there.

## Detriments if this is not built

- The directive keeps binding every run to a route no run can find, and the gate keeps passing it.
- The one-agent BUILD stage keeps handing 30 units to a single context.
- The next carrier edit reintroduces the same mispointer, because nothing reads a section's body.

## Build-level rules

- **The ratchet and the route land in ONE unit and one commit.** Measured this pass: the anchor term
  reds **17 of 17** core handles against `memory/guides/BUILD-METHOD.md` as it stands. A ratchet
  landing before its anchors reds the bar; anchors landing before the ratchet are unguarded prose.
  `TOOL-aHoistedPass-2` carries both or neither.

- **The budget raise precedes the anchors.** The anchor floor is 289 bytes and
  `tools/memory-tree/BUILD-METHOD.template.md` has 12 bytes of headroom on a KiB reading. The raise is
  `TOOL-aHoistedPass-3` at `order 2`; the anchors are `order 3`.

- **The comment-strip is the whole point of the ratchet term, and it was wrong once.** A predicate
  dropping lines that MATCH `<!--` drops only a comment's first line, so a multi-line comment carrying
  the anchor satisfies it while the section states no rule. Measured on four fixtures against the real
  file: the naive form PASSES the multi-line evasion and the block-stripping form REDS it, with the
  honest sentence green in both. The term strips whole `<!-- … -->` blocks across lines.

- **The hoist is the shape, and its headline was false.** BUILD dispatch leaves the harness for the
  main loop, one `Workflow` call per unit. The re-read this buys does NOT protect the child's content:
  measured, a child rewritten with a second `agent()`, a nested `workflow()` or a stripped `meta` all
  admit at exit 0. What the hoist actually buys is that each dispatch moves from ZERO hook checks —
  a `workflow()` from inside a sidechain fires no hook — to four rule blocks, three burst-class and one
  a ref-keyed-join rule, plus the deletion of a whole clause set, a unit and two rulings.

- **`--dispatch` does not backstop the loop, and no spec may claim it does.** It refuses a MISSING and
  a THIN unit, and refuses an out-of-order one only when BOTH units carry an `order` verb — which 38 of
  61 multi-unit builds cannot offer. A declaration row alone satisfies "dispatched", and the Skill
  orders the declaration before the pass. Loop completeness rests on `build-complete` at `--close`
  alone, whose escape is a recorded `--override`.

- **`pass-order history` grades spec-before-code for CLOSED units. It grades neither the build's
  declared unit order nor completeness**, and its own header says so. No spec cites it as a catcher for
  either.

- **The termination oracle only advances on a spec status flip.** A unit leaves `next` candidacy only
  when its spec header reaches `CLOSED` or `WONTDO`, and no carrier on the harness path instructs that
  act. The child performs it in the same commit as the code.

- **Recipe mode is MEASURED, not decided.** `TOOL-aHoistedPass-8` is a probe, not a fix. Until it
  reports, this build ships with a known live disagreement between a carrier and a registry —
  `UNATTENDED-PROTOCOL.md` says recipe mode does not take the route while the directive's scope is
  `all` — and no unit takes a side.

- **Three units carry an owner-gated carrier.** Ruling D1 (2026-09-04) put
  `tools/unattended/SKILL.template.md` on the veto-2 list, so every unit touching it is an owner turn,
  including a pure re-render — and `check-kit-versions.sh` requires a `gov:kit` marker in every tracked
  `tools/unattended/*.template.md`, which means every unattended kit-version bump edits it.

- **The design of record is `build/2026-09-04-build-TOOL-aHoistedPass-1-design-pass.md`.** Eight
  revisions, three adversarial rounds and two over-claim audits sit behind it; every unit below derives
  from it rather than restating it.

## Parked decisions

- **The slot byte ceilings are not met.** This README's problem, improvements and build-rules slots
  each sit over their declared ceiling, so `memory/project/readme-contract.txt` carries it as EXEMPT
  rather than BOUND. Trimming that prose is this build's owner's call; the row drains when they do.
  The structural faults that bind every build README regardless of that split were repaired by the
  `aKeyedAnnotation` session, which is what let the bar bind again.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aHoistedPass-1` | OPEN | the record catches up with the verdicts that superseded it |
| 2 | `TOOL-aHoistedPass-2` | OPEN | the route a run can find, and the ratchet that keeps it findable |
| 3 | `TOOL-aHoistedPass-3` | OPEN | the build-method budget becomes a number a gate reads |
| 4 | `TOOL-aHoistedPass-4` | OPEN | the loop ban learns the two spellings that walk past it |
| 5 | `TOOL-aHoistedPass-5` | OPEN | the child that builds one unit and holds nothing else |
| 6 | `TOOL-aHoistedPass-6` | OPEN | the harness hands out a roster and stops driving the build |
| 7 | `TOOL-aHoistedPass-7` | OPEN | a brief on disk before the code that cites it |
| 8 | `TOOL-aHoistedPass-8` | OPEN | the recipe-mode question, measured instead of argued |
| 9 | `TOOL-aHoistedPass-9` | OPEN | the adopter without the harness is told, on every bar |
| 10 | `DEPL-aHoistedPass-1` | OPEN | a declared kit dependency that is actually checked |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 10 unit(s) · node a · opened 2026-09-04 · streams tooling+deployer
ids DEPL-aHoistedPass-1 TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aHoistedPass-1 — the record catches up with the verdicts that superseded it](spec/2026-09-04-spec-TOOL-aHoistedPass-1.md) | 1 | 1 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aHoistedPass-4 — the loop ban learns the two spellings that walk past it](spec/2026-09-04-spec-TOOL-aHoistedPass-4.md) | 1 | 1 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aHoistedPass-8 — the recipe-mode question, measured instead of argued](spec/2026-09-04-spec-TOOL-aHoistedPass-8.md) | 1 | 1 | SPECCED | rev-1 | 2026-09-04 |
| [DEPL-aHoistedPass-1 — a declared kit dependency that is actually checked](spec/2026-09-04-spec-DEPL-aHoistedPass-1.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aHoistedPass-3 — the build-method budget becomes a number a gate reads](spec/2026-09-04-spec-TOOL-aHoistedPass-3.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aHoistedPass-2 — the route a run can find, and the ratchet that keeps it findable](spec/2026-09-04-spec-TOOL-aHoistedPass-2.md) | 3 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aHoistedPass-5 — the child that builds one unit and holds nothing else](spec/2026-09-04-spec-TOOL-aHoistedPass-5.md) | 4 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aHoistedPass-6 — the harness hands out a roster and stops driving the build](spec/2026-09-04-spec-TOOL-aHoistedPass-6.md) | 5 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aHoistedPass-9 — the adopter without the harness is told, on every bar](spec/2026-09-04-spec-TOOL-aHoistedPass-9.md) | 6 | 2 | SPECCED | rev-1 | 2026-09-04 |
| [TOOL-aHoistedPass-7 — a brief on disk before the code that cites it](spec/2026-09-04-spec-TOOL-aHoistedPass-7.md) | 7 | 2 | SPECCED | rev-1 | 2026-09-04 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-aHoistedPass-1 TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aHoistedPass-1`, `TOOL-aHoistedPass-4`, `TOOL-aHoistedPass-8` | yes |
| 2 | `DEPL-aHoistedPass-1`, `TOOL-aHoistedPass-3` | yes |
| 3 | `TOOL-aHoistedPass-2` | no |
| 4 | `TOOL-aHoistedPass-5` | no |
| 5 | `TOOL-aHoistedPass-6` | no |
| 6 | `TOOL-aHoistedPass-9` | no |
| 7 | `TOOL-aHoistedPass-7` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBriefedPass](../dBriefedPass/README.md), [dRatifiedSeam](../dRatifiedSeam/README.md)
<!-- /gen:build-edges -->
