---
slug: aGradedMandate
node: a
opened: 2026-08-31
streams: tooling
roster: TOOL
ids: TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9
authorized-by: prompt
---

# aGradedMandate — the unattended kit reads the answers it already records

## The problem this build exists to solve
An unattended run replaces the owner's read of the diff with machine checks. A five-lens adversarial
review of every layer of the kit asked one question — what lets such a run produce WORSE WORK than
an attended one and land it green — and returned twelve confirmed findings whose theme is one
sentence: **the kit records the answer and never reads it.** The closing review's blocker count, the
spec-audit coverage line rendered into every build README, the held-leg guard arrays, the retirement
rows: all four are computed, committed, and opened by nothing at the one checkpoint that exists.
Two runs in this tree reached `LANDED` with their closing review loop stopped at `BLOCKED`, blockers
standing, on a Definition-of-Done item that was MET. The report is
`build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`.

## Expected improvements
- A closing review must END, and `--close` reads whether it did.
- A spec audit stops being unobservable: a CLOSED unit no audit ever named blocks the close.
- A run that edits a held checker runs that checker's own arms before it lands.
- Dropping declared scope reaches the owner's one turn instead of the history class.

## Detriments if this is not built
- Candour stays charged and silence stays free: recording a second review round buys the whole
  promotion bill, recording nothing buys nothing, exactly when the work is worst.
- Every later green means less than it reads, here and in every adopter that copies the kit.

## Build-level rules
- **The lens is narrow.** Not "is this kit correct" — that has had many rounds. Only: what lets a run
  do worse work and land it green. A finding about bookkeeping is out of scope.
- **The prompt authorizes the kit's own carriers.** "Changes to any layer of the kit" reaches
  `PROTOCOL.template.md`, `SKILL.template.md` and `.unattended.conf`. It does NOT reach carriers
  outside the kit — the charter, the build method, `memory/HYGIENE.md`. Those are M3 veto 2 and are
  parked or backlogged, never edited here.
- **A leg-side ratchet that reds a landed record is unlandable, and that decided two units.** The
  closing-loop fix is DRIVER-side only, and the promotion fix tightens the id-status half alone,
  because the blocker-sum half reds `aPrimedKeepalive` on main today.
- **Every new predicate is observed RED against a staged break before it is called built**, and its
  own header states what it does NOT check.
- **This build is the dogfood.** It must itself satisfy every item it adds: a converged closing loop,
  a spec audit naming every unit, and an escalated bar.

## Parked decisions
Entries live in `RUN.md`. The two standing at authoring time: the unattended kit's own five suites
remain reachable by no bar and no value of any flag, because closing that needs either a raised
`GATE_BOUND` or a new record surface, and both are owner turns; and the landing itself, since
`tools/push-main.sh` refuses off the default branch and this session may not leave its worktree —
the same wall `aScouredKit` met and parked on 2026-08-30.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aGradedMandate-1` | 2 | `closing-review-recorded` requires the closing loop to have ENDED |
| 2 | `TOOL-aGradedMandate-2` | 2 | `specs-audited`, an eleventh core Definition-of-Done item |
| 3 | `TOOL-aGradedMandate-3` | 2 | `gates-green` escalates onto held self-test legs by the run's own diff |
| 4 | `TOOL-aGradedMandate-4` | 2 | `build-complete` refuses a CLOSED unit whose spec grades THIN |
| 5 | `TOOL-aGradedMandate-5` | 2 | a retirement becomes a `surfaced`-class parked act |
| 6 | `TOOL-aGradedMandate-6` | 2 | check 24's RETIRE arm keys its baseline to the run's pinned BASE |
| 7 | `TOOL-aGradedMandate-7` | 2 | the promotion clause counts only ids that are non-WONTDO at HEAD |
| 8 | `TOOL-aGradedMandate-8` | 1 | the agent-facing carriers corrected, in one render |
| 9 | `TOOL-aGradedMandate-9` | 2 | the leg's two-way Skill join extended to `DOD_NO_OVERRIDE` |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 9 unit(s) · node a · opened 2026-08-31 · streams tooling
ids TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aGradedMandate-1 — `closing-review-recorded` requires the closing loop to have ENDED](spec/2026-08-31-spec-TOOL-aGradedMandate-1.md) | 1 | 2 | SPECCED | rev-2 | 2026-08-31 |
| [TOOL-aGradedMandate-2 — `specs-audited`, an eleventh core Definition-of-Done item](spec/2026-08-31-spec-TOOL-aGradedMandate-2.md) | 2 | 2 | SPECCED | rev-2 | 2026-08-31 |
| [TOOL-aGradedMandate-3 — `gates-green` escalates onto held self-test legs by the run's own diff](spec/2026-08-31-spec-TOOL-aGradedMandate-3.md) | 3 | 2 | WONTDO | rev-2 | 2026-08-31 |
| [TOOL-aGradedMandate-4 — `build-complete` refuses a CLOSED unit whose spec grades THIN](spec/2026-08-31-spec-TOOL-aGradedMandate-4.md) | 4 | 2 | SPECCED | rev-2 | 2026-08-31 |
| [TOOL-aGradedMandate-5 — a retirement becomes a `surfaced`-class parked act](spec/2026-08-31-spec-TOOL-aGradedMandate-5.md) | 5 | 2 | SPECCED | rev-2 | 2026-08-31 |
| [TOOL-aGradedMandate-6 — check 24's RETIRE arm keys its baseline to the run's pinned BASE](spec/2026-08-31-spec-TOOL-aGradedMandate-6.md) | 6 | 2 | SPECCED | rev-2 | 2026-08-31 |
| [TOOL-aGradedMandate-7 — the promotion clause counts only ids that are non-WONTDO at HEAD](spec/2026-08-31-spec-TOOL-aGradedMandate-7.md) | 7 | 2 | SPECCED | rev-1 | 2026-08-31 |
| [TOOL-aGradedMandate-8 — the agent-facing carriers corrected, in one render](spec/2026-08-31-spec-TOOL-aGradedMandate-8.md) | 8 | 1 | SPECCED | rev-1 | 2026-08-31 |
| [TOOL-aGradedMandate-9 — the leg's two-way Skill join extended to `DOD_NO_OVERRIDE`](spec/2026-08-31-spec-TOOL-aGradedMandate-9.md) | 9 | 2 | SPECCED | rev-1 | 2026-08-31 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aGradedMandate-1` | no |
| 2 | `TOOL-aGradedMandate-2` | no |
| 3 | `TOOL-aGradedMandate-3` | no |
| 4 | `TOOL-aGradedMandate-4` | no |
| 5 | `TOOL-aGradedMandate-5` | no |
| 6 | `TOOL-aGradedMandate-6` | no |
| 7 | `TOOL-aGradedMandate-7` | no |
| 8 | `TOOL-aGradedMandate-8` | no |
| 9 | `TOOL-aGradedMandate-9` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
