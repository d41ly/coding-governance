---
slug: aRoutedQuill
node: a
opened: 2026-10-09
streams: tooling+kickoff+playbook+deployer
roster: TOOL+KICK+PLAY
ids: KICK-aRoutedQuill-1 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-6
---

# aRoutedQuill — every code build is routed through orientation, a brief and a specced unit

## The problem this build exists to solve

Orientation, the brief and the spec run only when someone invokes them. Nothing stops an agent from
writing product code straight from a raw prompt. The commit deny accepts any READY line and never
sees Edit, Write or a subagent, and the spec-before-code checks grade only units a run already
declared. A default adopter wires none of these hooks. So a build request reaches gov's workflow
only when the person typing it already knows to ask for it. The one quality trial on record measured
clear briefs, never the vague prompt where routing should pay.

## Expected improvements

- Product code is written only under a unit whose spec exists, in a session, a subagent or a run.
- Every build starts from a committed brief the owner confirmed, never from the raw prompt.
- An adopter gets the routing by installing gov, with nothing left to wire.
- A trial says whether routing improves the code, and at what cost.

## Detriments if this is not built

- Agents keep building from raw prompts whenever nobody types /session-kickoff.
- Code no spec owns keeps landing, so a review cannot trace it to a decision.
- Gov keeps claiming a workflow benefit it has never measured.

## Build-level rules

Eight units, one mechanism each. Owner decisions, 2026-10-09: every product-code write needs a
specced unit, and a Tier-1 unit takes a micro-spec that still follows the spec template. A Tier-1
unit admits writes at a conforming SPECCED spec, a Tier-2 unit only at INPROGRESS. The gate has no
bypass and enforces from landing, with no warn phase. Its kit joins govkit's defaults and is wired
at install. No spec audit is declared. The write gate routes and the push leg guarantees: a Bash
write or a hook-less run passes the first and not the second. The gate reads a status the agent
writes, so approval is recorded, not proven. There is no prompt classifier and no UserPromptSubmit
gate, which aReplayedCard rejected on harness grounds. Three shared names have one owner each:
`ROUTED_PATHS` belongs to unit 2, the card's `## route` section to the kickoff unit, and the unit id
a commit names to unit 3. Kit versions bump once per kit, after the last unit touching it. The
kickoff unit runs after unit 1, not beside it, because both re-stamp the kickoff manifest. At the
rev-2 cross-read every unit is FORKED: its open questions go to the owner before any code.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aRoutedQuill-1` | SPECCED | a Tier-1 spec carries what and how, done, out of scope and how to verify, and check 12 grades it |
| 2 | `KICK-aRoutedQuill-1` | SPECCED | kickoff writes the rewritten prompt as a brief the owner confirms, and the card names the routed unit |
| 3 | `TOOL-aRoutedQuill-2` | SPECCED | a PreToolUse gate refuses a product-path write unless the card routes a buildable unit |
| 4 | `TOOL-aRoutedQuill-3` | SPECCED | a push-time leg reds a product change whose commit names no unit specced before it |
| 5 | `TOOL-aRoutedQuill-4` | SPECCED | a SubagentStart hook hands every subagent the routed unit, its spec and its brief |
| 6 | `TOOL-aRoutedQuill-5` | SPECCED | the gate's kit and the card writer are adopter defaults, wired at install |
| 7 | `PLAY-aRoutedQuill-1` | SPECCED | the charter's Definition of Ready requires a spec for every product-code unit |
| 8 | `TOOL-aRoutedQuill-6` | SPECCED | a routed-vs-raw trial on frozen clones of real repos |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 8 unit(s) · node a · opened 2026-10-09 · streams tooling+kickoff+playbook+deployer
ids KICK-aRoutedQuill-1 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aRoutedQuill-1 — a Tier-1 spec is a micro-spec, and check 12 grades its sections by heading text](spec/2026-10-09-spec-TOOL-aRoutedQuill-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-10-09 |
| [KICK-aRoutedQuill-1 — the kickoff writes a brief the owner confirms, and the card routes the session to its units](spec/2026-10-09-spec-KICK-aRoutedQuill-1.md) | 2 | 2 | SPECCED | rev-2 | 2026-10-09 |
| [TOOL-aRoutedQuill-2 — scratch-guard refuses a product write no buildable unit on the card owns](spec/2026-10-09-spec-TOOL-aRoutedQuill-2.md) | 3 | 2 | SPECCED | rev-2 | 2026-10-09 |
| [TOOL-aRoutedQuill-3 — every pushed commit that touches a product path names a unit specced before it](spec/2026-10-09-spec-TOOL-aRoutedQuill-3.md) | 4 | 2 | SPECCED | rev-2 | 2026-10-09 |
| [TOOL-aRoutedQuill-4 — every subagent starts holding the card's route, stated as facts](spec/2026-10-09-spec-TOOL-aRoutedQuill-4.md) | 4 | 2 | SPECCED | rev-2 | 2026-10-09 |
| [PLAY-aRoutedQuill-1 — the charter's Definition of Ready: every product-code unit carries a spec before code](spec/2026-10-09-spec-PLAY-aRoutedQuill-1.md) | 5 | 2 | SPECCED | rev-2 | 2026-10-09 |
| [TOOL-aRoutedQuill-5 — a default govkit install ships the write gate wired and its product paths armed](spec/2026-10-09-spec-TOOL-aRoutedQuill-5.md) | 5 | 2 | SPECCED | rev-2 | 2026-10-09 |
| [TOOL-aRoutedQuill-6 — routed against raw: a paired trial on frozen clones of real repositories](spec/2026-10-09-spec-TOOL-aRoutedQuill-6.md) | 6 | 1 | SPECCED | rev-2 | 2026-10-09 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: KICK-aRoutedQuill-1 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-6.

Ids no `spec-audit` record has ever named: KICK-aRoutedQuill-1 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aRoutedQuill-1` | no |
| 2 | `KICK-aRoutedQuill-1` | no |
| 3 | `TOOL-aRoutedQuill-2` | no |
| 4 | `TOOL-aRoutedQuill-3`, `TOOL-aRoutedQuill-4` | yes |
| 5 | `PLAY-aRoutedQuill-1`, `TOOL-aRoutedQuill-5` | yes |
| 6 | `TOOL-aRoutedQuill-6` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
