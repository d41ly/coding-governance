# TOOL-aHomedAnchor-1 — the driver's third anchor: `ANCHOR_SCOPE="local"` authorizes from local history

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-2 · base 11224126 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aHomedAnchor-1-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aHomedAnchor-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-build-TOOL-aHomedAnchor-1-runlog-5ac5d61b.md](../build/2026-10-09-build-TOOL-aHomedAnchor-1-runlog-5ac5d61b.md) | journal | TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 |
| [2026-10-09-prompt-TOOL-aHomedAnchor-1-0-run-mandate.md](../prompts/2026-10-09-prompt-TOOL-aHomedAnchor-1-0-run-mandate.md) | journal | TOOL-aHomedAnchor-2 |
| [2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md](../reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md) | diff-review | TOOL-aHomedAnchor-2 |

<!-- /gen:spec-records -->

## 1. Goal

Let an owner start `/unattended <slug>` from the worktree branch or the local `main` that committed
the build folder, with no push to origin, by adding a third `ANCHOR_SCOPE` value, `local`, that the
driver resolves from local history. Landing is unchanged: it still pushes `main`.

## 2. Scope (IN)

- S1. `resolve_base` in `tools/unattended/unattended.sh`, under `ANCHOR_SCOPE="local"`, when the
  build README does not resolve at the first anchor's merge-base, sets `ANCHOR_KIND=local` and
  returns the degenerate code with HEAD as the derived base, provided the README resolves at HEAD.
  It never observes the run branch's advertised tip. Observed by AC1.
- S2. `trusted_base`, when `ANCHOR_KIND=local`, takes the RECORDED `base:` as the base. Absent, it
  is HEAD at `--preflight` (`allow-degenerate`) and fail 16 anywhere else. Present, it must resolve
  and be an ancestor of HEAD, else fail 18, and at `--close` it must differ from HEAD, else fail 16.
  Observed by AC3 and AC4.
- S3. The fail 18 widening `trusted_base` already carries for `published` gains the same clause for
  `local`, so a local-anchored run whose README later reaches the default branch is not wedged.
  NOT OBSERVED: reaching it needs the folder landed on origin mid-run; the clause is one alternative
  beside the published one and is read in review.
- S4. Check 50 stays keyed on `ANCHOR_KIND=run-branch`, so the local anchor admits `slug`,
  `prompt` and `recipe` alike. Observed by AC1 and AC5.
- S5. A `may:` grant (fail 78) and a README `spec-audit:` line (fail 89) are refused on the local
  anchor in every mode, as on the second anchor; the prompt-mode quoted-ask admission is unchanged.
  `SPEC_AUDIT_DEFAULT` is read at the default-branch side of BASE on the local anchor, as on the
  second. Observed by AC5.
- S6. `tools/unattended/adopt-unattended.sh` renders `{{ANCHOR_SCOPE}}` as `local` for a conf
  declaring `local`. Observed by AC6.
- S7. The carriers say what `local` is and what it spends: protocol §1 and §8, the verbs file's slug
  and prompt paths, the Skill's prompt path, STOPS' published-tip rule, the conf example and the kit
  README. Template and rendered copy move together. NOT OBSERVED: prose, graded by the parity legs.
- S8. This repository's `.unattended.conf` declares `ANCHOR_SCOPE="local"`. NOT OBSERVED: a
  one-line declaration; its effect is AC1's.

## 3. Non-goals (OUT)

- The landing push: `push-main.sh` still pushes `main`, by the owner's ruling.
- `RUN_CLAIMS`: a claim is a lease on the remote, not an authorization, and it is untouched.
- An offline run: the first anchor is still observed, so a remote that does not answer still
  refuses `--preflight` as today.
- The `published` value: its behaviour, and `TOOL-dNarrowedAnchor-1`'s refusal of `slug` on it, do
  not move.
- The bar leg: `TOOL-aHomedAnchor-2`.

### Edges

- **hands-off** `TOOL-aHomedAnchor-2` — the leg's checks 9 and 29 admitting a local-anchored BASE

## 4. Design

`local` is the third value of `ANCHOR_SCOPE`. The first anchor fires first, unchanged: a README at
the remote merge-base is a default-branch run whatever the scope says. Only when it misses does
`local` widen, and it widens to local history, not to the advertised branch tip.

What the local anchor can and cannot assert:

| Property | default-branch | run-branch (`published`) | local |
|---|---|---|---|
| the folder predates the run | yes | no | no |
| the BASE is observed off this node | yes | yes | no |
| the roster cannot shrink | yes | no | no |
| `slug` admitted | yes | no | yes |
| a branch push to start or hold | no | yes | no |

On the local anchor nothing outside this node pins the BASE, so the recorded `base:` is the only
input there is, and `trusted_base` says so instead of deriving a value it would then compare against
itself. It still refuses a base off HEAD's history and a run that built nothing. The record names
the anchor as `anchor-kind: local`, which preflight already writes from `ANCHOR_KIND`.

`may:` and `spec-audit:` are owner-only by rulings D12-j and `TOOL-aWardedAudit-4`. A local README
is one the run could have written, so both are refused there in every mode. Honouring them would
widen the self-grant surface beyond this unit's tier, which is M3's third veto.

`--hold` and `--scheduled` already require the published tip only under `published`; under `local`
they take the default-branch path and print the existing skip line.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/adopt-unattended.sh`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/SKILL.template.md`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/README.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `.claude/skills/unattended/SKILL.md`
- `.unattended.conf`

## 5. Production-readiness checklist

- security — the local anchor authorizes from bytes this node wrote. The owner accepted it; the
  record names the anchor, and `may:` and `spec-audit:` stay refused there.
- perf / scale — N/A — one `git show` and one `merge-base --is-ancestor` per call.
- error / empty / loading states — an absent recorded base outside preflight is fail 16.
- observability — `anchor-kind: local` in the run-state file.
- risks — an adopter on `published` is unaffected; a misspelt value keeps the strict anchor.
- testing — AC1 to AC6, arms in the driver suite, observed by a slice, never the suite.
- migration — N/A — an opt-in value; no record changes.
- user docs — the carriers in S7.

## 6. Acceptance criteria

- **AC1** — When `unattended.sh --preflight tBr` runs under `ANCHOR_SCOPE="local"` with a `slug`
  README committed on an unpushed branch, it prints `preflight OK` and the run-state file carries
  `anchor-kind: local`. Red when: `resolve_base` keeps the strict anchor and refuses with fail 16.
- **AC2** — When the same fixture runs under `ANCHOR_SCOPE="published"`, `--preflight` refuses with
  `the remote advertises no tip for the branch this run is on`. Red when: `local` leaked into
  `published`.
- **AC3** — When `--authorization` runs on a local-anchored record whose `base:` is rewritten to a
  commit off HEAD's history, it prints fail 18's `is not an ancestor of HEAD`. Red when: the recorded
  base is taken unchecked.
- **AC4** — When `--authorization` runs on a local-anchored record whose `base:` equals HEAD, it
  prints fail 16's `built nothing`. Red when: a run that built nothing is authorized to land.
- **AC5** — When the local fixture's README carries `may:` or `spec-audit:`, `--preflight` refuses
  with fail 78 or fail 89 naming the local anchor, and a `recipe` README passes check 50. Red when:
  a local README's grant is honoured, or the local anchor refuses a mode.
- **AC6** — When `adopt-unattended.sh` renders the Skill for a conf declaring `local`, the rendered
  text reads `authorizes at this project's anchor, `local``. Red when: the renderer maps `local` to
  `default-branch`.

## 7. Gates

`unattended kit gate` · `unattended protocol size` · `unattended skill size` · `unattended skill wiring` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 · a local-scope fixture on an unpushed branch, then a forged and a degenerate base · none

## 8. Open questions

- **F1 — may a `slug` README's `may:` and `spec-audit:` count on the local anchor?**
  Honour them, as the default-branch anchor does, or refuse them, as the second anchor does.
  RESOLVED (agent, 2026-10-09, delegated): refuse. Honouring widens the self-grant surface past
  this unit's tier, M3 veto 3, so no surviving option honours them.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`reuse_lookup.py "authorize an unattended run from a local commit without a published branch
tip"` names no seam for the anchor; the seam extended is `resolve_base` and `trusted_base` in
`tools/unattended/unattended.sh`, the two functions `ANCHOR_SCOPE="published"` already widens, and
`TOOL-dNarrowedAnchor-1`'s check 50, reused unchanged.

Recall terms used: `--terms "ANCHOR_SCOPE published second anchor SECOND_ANCHOR_MODES slug mode
branch tip authorization reachable BASE merge-base dNarrowedAnchor"`, which returned
`TOOL-dNarrowedAnchor-1`, `TOOL-aPromptedMandate-1` and `TOOL-aWardedAudit-1`.
