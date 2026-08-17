# The playbook audit — the commissioning input for aSiftedPlaybook

*Read-only audit of the three shipped `parallel-coding-governance*.md` files at template **v2.7**,
run 2026-08-16 against BASE `91ef1b05`. Every finding below was reproduced against source before
inclusion; a suspected defect that could not be reproduced was dropped, and the ones that were
actively disproved are enumerated rather than discarded. Committed per round-2 audit finding H12 —
before this file existed, completeness against the commissioning input was unfalsifiable, and a
later session could not tell a dropped defect from one that never existed.*

## Method

Three defect classes were hunted, each requiring a reproduction rather than an assertion:

- **stale** — a claim the tooling has moved past.
- **missing wire** — a kit, gate, guide or companion §-stub that exists but nothing in the trio
  points at, or a pointer whose target is gone.
- **non-agnostic** — a rule true only for this repo's layout, node registry, install prefix or
  situational history, and therefore wrong in an adopter's tree.

Cross-file convergence was checked in all three directions: template §-stub ↔ companion §-heading ↔
customize placeholder and conditional-section lists.

## The eleven confirmed defects

| # | Sev | Class | Where | Defect |
|---|---|---|---|---|
| A1 | high | stale | `template.md:150` | The `agent-cap.js` hook is described as `(matcher \`Workflow\`)`. The wired value is `Workflow\|Agent` (`.claude/settings.json:5`), and `REVIEW-PROTOCOL.md:58-60` records that `check-wiring.sh` asserts the VALUE precisely because a group left at `Workflow` alone still contains the string and used to report ok. An adopter wiring per this parenthetical gets a hook blind to the whole `Agent` modality. |
| A2 | high | non-agnostic | `template.md`, 17 sites | The default branch is spelled as the literal `main` seventeen times with no placeholder, while `.githooks/pre-commit:16`, `tools/push-main.sh:20` and the kickoff engine all resolve it dynamically. Two of the seventeen sit inside §16 micro-formats the template declares MANDATORY and byte-stable, so a project on `master` must either violate a mandatory format or emit a false one. |
| A3 | high | stale | `customize.md:20-21` | "36 in total, and the two groups are **disjoint** — no placeholder appears in both files, so each one is filled in exactly one place." Measured: 23 + 14 = 37 while the union is 36, because `{{MEMORY_ROOT}}` appears in both files. The prose argues against running the both-files verification grep that would catch the resulting unfilled placeholder. |
| A4 | med | stale | `template.md:150` | `agent-cap.js` implements four rules; the template describes two. Missing: RULE 3 (`:346`, the hook resolves the bound wherever it is written) and RULE 4 (`:549`, direct `Agent` spawns counted at runtime, five per prompt) — the latter being the only enforcement that reaches a fan-out made outside a `Workflow` script. |
| A5 | med | stale | `template.md:107` | "a **19-check** hygiene gate". The true count is 20. Notably the count is NOT derivable from the engine — `check-memory-hygiene.sh`'s own `fail` numbers stop at 12, with 13-16, 17-19 and 20 delegated — so its authority is `tools/gate-legs.json:3` and `tools/memory-tree/README.md:18`. |
| A6 | med | missing wire | all three | The `drift-audit` kit is named nowhere in the trio, while `WIRE-INTO-PROJECT.md §3d` installs it as "optional, recommended". The adopter's instantiated ruleset never mentions records-vs-reality auditing, and the deletion checklist cannot tell them what to strip if they decline it. |
| A7 | med | stale | `template.md:51` · `customize.md:61` | "a committed build **plan**". `UNATTENDED-PROTOCOL.md` says "build folder" five times and "build plan" zero; `AGENTS.md:182` and `domain-rules.md:25` agree. The template is what an agent reads at landing time and it names an artifact the protocol does not define. |
| A8 | low-med | missing wire | all three | `pytest-parallel-guardrails` is never named, although `domain-rules.md:87-88` already encodes in full the two bug classes it exists to fix. The reader is told to solve a problem a shipped kit already solves. |
| A9 | low-med | missing wire | `customize.md:12-13` | `agent-instructions` is never named, while the file instructs the deploying agent to write the filled template into "`AGENTS.md` / `CLAUDE.md`". An adopter who writes only `AGENTS.md` ships a repo Claude Code cannot read, which is the entire reason that kit exists. |
| A10 | low | stale | `template.md:51` | The landing rule cites "(companion §1, §8)", but v2.7 turned §8 into a pointer back at §1 (`:159`: "landing is §1's rule, not restated here"). The edit changed one direction only, leaving a circular reference. |
| A11 | low | stale | `domain-rules.md:10-12` | "Four are droppable-per-project (§4, §9, §11 and §13) and §1's unattended block is a fifth, **line-scoped** one" — asserting by contrast that the four are whole-section drops. `customize.md:69-71` drops only §9's outbound-call lines and only §4's harness lines. Two of the four are line-scoped too. |

**Which scope item fixes each of these is BUILD STATE, not audit state**, so it lives in the build
README's coverage table and deliberately not here. This file records what was found on 2026-08-16
and does not move when the plan does.

## Four more, found after the audit closed

Recorded separately because they are NOT part of the eleven and must not inflate that count:

| # | Sev | Where | Defect | Found |
|---|---|---|---|---|
| B1 | high | `template.md:150` | "an array LITERAL of **≤6** elements (the lens fan) passes unmarked". `agent-cap.js:119` sets `MAX_LENSES = 5`, with a comment recording that 6 was a trailing-comma miscount the owner ratified away. The template prescribes a fan the hook DENIES. | while writing `PLAY-1` §2 |
| B2 | med | `template.md:157` | "the ≤5 cap is enforced at the `Workflow` tool-call … never inside the script where no hook reaches" — the pre-`agent-cap`-1.3 description; RULE 4 enforces at the `Agent` call too. | discovery `wf_4e13d9e7-550` |
| B3 | low | `template.md:24` | §0 says "Never run more than 5 agents **concurrently**", naming the weaker of the two rules as if it were the rule. `REVIEW-PROTOCOL.md:12-13` states plainly that concurrency is not a budget. | while writing `PLAY-1` §2 |
| B4 | med | all three | `gate-lint` is a **fourth** shipped kit absent from the trio — and absent from `AGENTS.md` and `README.md` entirely, so the charter does not know it ships. | discovery `wf_4e13d9e7-550` |

## Refuted — eight disproved, one withdrawn

Recorded so a later audit does not re-spend the tokens, and because a refuted finding is evidence
about the files' quality just as a confirmed one is.

| # | Suspicion | Disproof |
|---|---|---|
| R1 | `customize.md`'s "four codebase-map lines" is wrong | Exactly four: template `:40`, `:46`, `:108`, `:137`. |
| R2 | "13 of the 36 … unfilled in the companion" is wrong | **REFUTATION WITHDRAWN 2026-08-16** (round-3 H10). 13 is the companion-EXCLUSIVE count; the companion CARRIES 14, and after a template-only fill all 14 are unfilled. The suspicion was correct and this row is a confirmed defect, fixed by `PLAY-aSiftedPlaybook-4` S4. The tracked OPEN row `PLAY-aSealedCaravan-1` had already recorded it. |
| R3 | The template header's "nine domain checklists" is wrong | Exact: §1, §4, §7-§13. |
| R4 | The companion header's "nine activity-scoped domain sections" is wrong | Exact, same nine. |
| R5 | Template §10's "25 generic classes" is wrong | Exactly 25 bullets in `domain-rules.md` §10. |
| R6 | "install per WIRE §5" points at the wrong section | Correct — the `tier2-review.js` install is at `WIRE-INTO-PROJECT.md:469-472`, inside §5, even though §5's title advertises only worktree tooling. |
| R7 | `tools/workflows/tier2-review.js` in the template is an install-prefix violation | It is not. `tools/<kit>/` is the kit's declared one-segment install prefix, which is why the path carries no waiver. |
| R8 | `adopt-memory-tree.sh --scaffold` does not exist as documented | It exists. |
| R9 | `gate-lint`'s absence from the map is an undetected coverage gap | Its key is baselined at `memory/map/baseline.toml:43` — a tracked unclaimed key, not an undetected gap, and not a playbook defect. (Its absence from `AGENTS.md` IS real and is recorded above as B4.) |

**Nine listed, EIGHT actually refuted.** The build README originally said "eight", counting the
three separate count-claims R3/R4/R5 as one bullet; enumerating them forced the true figure to nine.
Round 3 then withdrew R2, so eight stand. Both corrections came from writing the list out rather than
summarising it — twice over, this file has caught a number that a summary sentence could not.

## What this audit did not cover

Stated so the gap is deliberate rather than assumed:

- **The kits themselves**, except as reference targets. Defects found in passing while using them
  as sources of truth are recorded as follow-ups, not fixed here. **The `agent-cap` "TWO rules"
  item is WITHDRAWN 2026-08-16** (`PLAY-aDeclaredCeiling-1`): this report filed
  `WIRE-INTO-PROJECT.md` as calling `agent-cap` "the review protocol's TWO rules" against four, and
  the sentence is CORRECT. It reads "the mechanical enforcement of the review protocol's TWO rules:
  route fan-out through the cap-5 helpers, AND a review's verify stage spawns at most 5 agents
  TOTAL", and `memory/guides/REVIEW-PROTOCOL.md` binds exactly two rules — its `## The hard cap`
  and `## Concurrency` sections. The "four" is `tools/hooks/agent-cap.js`'s four numbered
  IMPLEMENTATION rules, which are how the hook enforces those two, not a second count of them. This
  audit compared a sentence about the PROTOCOL to a population in the HOOK. The remaining follow-up
  is real: `tools/memory-tree/README.md:6` still said "19-check" when this was written, and was
  corrected at the closing review. **Root `README.md:33` was PULLED INTO SCOPE and is no longer a follow-up**
  — `TOOL-aSiftedPlaybook-1` S4 receives it with a §4 inventory row and AC13 observing it, because
  that unit already edits the file and the front door is adopter-facing. Three documents gave three
  answers on this carrier across two review rounds; this is the one that records where it landed.
- **`WIRE-INTO-PROJECT.md`'s structure**, beyond the one dead `§2a` reference `PLAY-3` S6 corrects.
- **`skills/session-kickoff/SKILL.md`'s spec-canon count — TRUE AT BASE, FIXED ON MAIN, no longer a
  follow-up.** At BASE `91ef1b05` the engine read "status header + nine canonical sections" against a
  ten-section canon. Commit `5fd7c7e` ("build(KICK-cKeyedLaunchpad-4): the sealed task region, and
  the duplication it removes"), one of the 102 this branch was behind, replaced it with the
  right pattern: "the template states its own section count and the gate that enforces it; do not
  restate that number here, because it has already gone stale in three other carriers." Round 3 read
  it at HEAD, could not see BASE, and called the bullet fabricated. It was not — it was accurate when
  written and went stale underneath this build. Recorded in full because a report about falsifiable
  completeness should show its own corrections, including the ones where the reviewer was wrong.
- **Whether each of the eleven is worth fixing.** That was the owner's call and was given.
