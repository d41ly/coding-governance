---
slug: aRoutedQuill
node: a
opened: 2026-10-09
streams: tooling+kickoff+playbook+deployer
roster: TOOL+KICK+PLAY
ids: KICK-aRoutedQuill-1 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7
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

Nine units, one mechanism each. Owner decisions, 2026-10-09: every product-code write needs a
specced unit, and a Tier-1 unit takes a micro-spec that still follows the spec template. A Tier-2
unit admits writes at INPROGRESS; a Tier-1 unit at INPROGRESS, or at SPECCED once the micro-spec
check has graded it. The gate has no bypass, refuses on a missing card or an unarmed conf, and
enforces from landing with no warn phase. Its kit joins govkit's defaults, is wired at install and
reaches existing adopters through `govkit update`. No spec audit is declared. The write gate routes
and the push leg guarantees: a Bash write or a hook-less run passes the first and not the second.
The gate reads a status the agent writes, so approval is recorded, not proven. There is no prompt
classifier and no UserPromptSubmit gate. `ROUTED_PATHS` belongs to the gate unit, the card's
`## route` and the brief shape to the kickoff unit, and a commit's unit id to the push leg unit.
The brief shape moves into the kickoff kit after TOOL-aQuotedBrief-1 lands as specced, as agreed
with that build's session, and the repoint unit points its check at it. Kit versions bump once per
kit, after its last unit. The kickoff unit runs after the micro-spec unit, because both re-stamp the
kickoff manifest. Every judgement fork is resolved; one probe settles the two subagent questions
before the gate and hand-off units build.

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
| 9 | `TOOL-aRoutedQuill-7` | SPECCED | the unattended prompt-brief check reads its sub-heads from the kickoff kit's skeleton |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 9 unit(s) · node a · opened 2026-10-09 · streams tooling+kickoff+playbook+deployer
ids KICK-aRoutedQuill-1 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aRoutedQuill-1 — a Tier-1 spec is a micro-spec, and check 12 grades its sections by heading text](spec/2026-10-09-spec-TOOL-aRoutedQuill-1.md) | 1 | 2 | SPECCED | rev-2 | 2026-10-09 |
| [KICK-aRoutedQuill-1 — the kickoff writes a brief the owner confirms, and the card routes the session to its units](spec/2026-10-09-spec-KICK-aRoutedQuill-1.md) | 2 | 2 | SPECCED | rev-3 | 2026-10-09 |
| [TOOL-aRoutedQuill-2 — scratch-guard refuses a product write no buildable unit on the card owns](spec/2026-10-09-spec-TOOL-aRoutedQuill-2.md) | 3 | 2 | SPECCED | rev-3 | 2026-10-09 |
| [TOOL-aRoutedQuill-3 — every pushed commit that touches a product path names a unit specced before it](spec/2026-10-09-spec-TOOL-aRoutedQuill-3.md) | 4 | 2 | SPECCED | rev-3 | 2026-10-09 |
| [TOOL-aRoutedQuill-4 — every subagent starts holding the card's route, stated as facts](spec/2026-10-09-spec-TOOL-aRoutedQuill-4.md) | 4 | 2 | SPECCED | rev-2 | 2026-10-09 |
| [PLAY-aRoutedQuill-1 — the charter's Definition of Ready: every product-code unit carries a spec before code](spec/2026-10-09-spec-PLAY-aRoutedQuill-1.md) | 5 | 2 | SPECCED | rev-3 | 2026-10-09 |
| [TOOL-aRoutedQuill-5 — a default govkit install ships the write gate wired and its product paths armed](spec/2026-10-09-spec-TOOL-aRoutedQuill-5.md) | 5 | 2 | SPECCED | rev-3 | 2026-10-09 |
| [TOOL-aRoutedQuill-6 — routed against raw: a paired trial on frozen clones of real repositories](spec/2026-10-09-spec-TOOL-aRoutedQuill-6.md) | 6 | 1 | SPECCED | rev-4 | 2026-10-09 |
| [TOOL-aRoutedQuill-7 — the unattended prompt-brief check reads its sub-head list from the kickoff kit's `--brief-skeleton`](spec/2026-10-09-spec-TOOL-aRoutedQuill-7.md) | 6 | 2 | SPECCED | rev-2 | 2026-10-09 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: KICK-aRoutedQuill-1 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7.

Ids no `spec-audit` record has ever named: KICK-aRoutedQuill-1 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aRoutedQuill-1` | no |
| 2 | `KICK-aRoutedQuill-1` | no |
| 3 | `TOOL-aRoutedQuill-2` | no |
| 4 | `TOOL-aRoutedQuill-3`, `TOOL-aRoutedQuill-4` | yes |
| 5 | `PLAY-aRoutedQuill-1`, `TOOL-aRoutedQuill-5` | yes |
| 6 | `TOOL-aRoutedQuill-6`, `TOOL-aRoutedQuill-7` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
