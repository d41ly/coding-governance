# DEPL-dShippedRelease-14 — the landing review, blocking the build's close and never the push

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 11 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0424@2fe22720 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-13 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-14-deviation-141.md](../build/2026-10-30-build-DEPL-dShippedRelease-14-deviation-141.md) | deviation | — |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing reviews a landing (`gap-deploy-06`'s review half). This unit runs the `landing review`
breakpoint TOOL-dDeclaredLoop-19 places, over the landed range, with the lenses `review.pin` passes
from dFairHearing's catalogue until dCalibratedLens's Deploy lenses land, and makes it block
`deploy.close` and never the push. A landing with no review placed says so in words of its own, so
"blocks the close" cannot read as a green nobody earned.

This unit owns no node. It reads `item.deploy.close`, `item.deploy.notify`, `item.review.pin`,
`item.review.dispose`, `policy-key.review.<stage>` and `record-kind.landing`.

## 2. Scope (IN)

- **S1** — The placement read, `unattended.sh --deploy review <slug> <sha>` over `run_deploy_review(slug,
  sha, root)` in `tools/loop/deploy_items.py` (pin C1). It asks `derive_breakpoints`
  (`tools/loop/breakpoints.py`, TOOL-dDeclaredLoop-19 S1) for a `landing review` row. No row sets the
  landing record's `review` field to `not-placed · review.deploy=<value>` through `set_landing_field`,
  prints that line and exits 0. A row fires it through `--trigger <slug> --subject landing:<sha> --cause
  <cause>` (TOOL-dDeclaredLoop-20 S2), `<cause>` the row's, sets `review` to `pending`, prints the pin
  of S3 and exits 3, so the walk of DEPL-dShippedRelease-4 holds at the breakpoint, before
  `deploy.notify`. Observed by AC1, AC2, AC3.
- **S2** — The close term, `check_landing_review(slug, sha, root)` in `deploy_items.py`, a fourth term of
  `deploy.close` beside `check_unleased`, `check_released` and `check_core_settled`
  (DEPL-dShippedRelease-4 S11), reading the record's `review` field through `read_landing`. `pending`
  fails, the close printing `held · check_landing_review · pending`. `not-placed · …` passes and
  prints `landing review — <sha8> · not placed · <value>`, a line that is never `clean`, `green` or
  `passed`. `disposed · …` passes. Any other value fails, so a forged or absent field is held and not
  read as reviewed. Observed by AC1, AC2.
- **S3** — The pin, `read_landing_pin(sha, root)` in `tools/workflows/review_pin.py`, reached as `python
  review_pin.py --landing <sha>` beside its `--subject` form (TOOL-dFairHearing-3 S8). It prints one
  JSON line of harness arguments: `kind` `diff-review`, `base` the landed merge's first parent (§8
  F1), `head` `<sha>`, and `reviewDir`. It passes no `preset`, because `preset` is refused on
  `diff-review` (TOOL-dFairHearing-2 AC1), and it prints `lenses` beside them: `diff defaults · no
  Deploy lens` while no row of `tools/workflows/lenses.toml` names the literal `landing` in `presets`,
  `Deploy` once one does. Observed by AC4.
- **S4** — The disposal: the `landing record` route `review.dispose` declares and leaves unarmed
  (TOOL-dDeclaredLoop-20 §3). `python deploy_items.py dispose-landing <sha> <report>` reads the review
  record's confirmed findings and files each through `write_review_patches(slug, sha, findings)`,
  `python intake.py file --origin landing --build <slug> --sha <sha>` with the canonical text
  `landing-review <sha> <finding id>`, the post-close row DEPL-dShippedRelease-13 §4 states. It then
  sets `review` to `disposed · <n> finding(s) · <report path>`. A second run files nothing. A report
  whose `## Verdict` line is absent is refused, exit 2, and `review` stays `pending`. Observed by AC5, AC6.
- **S5** — The record reaches the tree: the review record under `memory/builds/<slug>/reviews/` joins
  the paths `run_records_landing` stages (DEPL-dShippedRelease-4 S7), so it rides the records landing
  `run_unlease` drives. Observed by AC6.
- **S6** — The walk's order. A breakpoint is no `[[item]]` row, so `run_deploy_items`
  (DEPL-dShippedRelease-4 S1) gains one step: before the item a `derive_breakpoints` row's `position`
  names, it runs the row's verb, which for `landing review` is this unit's `--deploy review`. That is
  the one place flow-steps:494 puts it, between `item.deploy.recommend` and `item.deploy.notify`.
  Observed by AC3.
- **S7** — The docs: `help/deploy.md` states when a landing review runs and what `not-placed` means;
  `tools/workflows/README.md` states `--landing`; `tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`, states `--deploy review` and `dispose-landing`. NOT OBSERVED by
  a criterion: prose, read by the memory hygiene leg at the close.

**Build-run preconditions**: `derive_breakpoints` (TOOL-dDeclaredLoop-19), `--trigger` and
`review.dispose` (TOOL-dDeclaredLoop-20), `review_pin.py` (TOOL-dFairHearing-3), `lenses.toml`
(TOOL-dFairHearing-13), `intake.py` with the `landing` origin (TOOL-dWellOiledMachine-27, the ask of
DEPL-dShippedRelease-13 §8 F3), `read_landing` and `set_landing_field` (DEPL-dShippedRelease-1), the
close and `run_unlease` (DEPL-dShippedRelease-4).

## 3. Non-goals (OUT)

- The Deploy lenses themselves, a `landing` literal in `PRESETS` or a landing record as a harness
  subject kind: dCalibratedLens's and dFairHearing's.
- A per-build opt-in for `review.deploy`. TOOL-dDeclaredLoop-19:148-150 says none exists for this
  stage; `review.deploy = "owed"` or a `review.breakpoints` row naming `item.deploy.notify` places it.
- Blocking the push. `--close`'s `closing-review-recorded` (`tools/unattended/unattended.sh:11767`) is
  the pre-push review and is unchanged; it maps to `item.build.ratify`, not to this breakpoint.
- Holding the `landed` notice: it rode the push (TOOL-dWellOiledMachine-60 S2), so dependents hear of a
  landing before its review ends, and a finding enters as a patch build.
- A `[[stand-in]]` row for the lenses, §8 F4.

### Edges

- **consumes-from** `DEPL-dShippedRelease-1` — `read_landing` and `set_landing_field`, the subject of the review and its `review` field
- **consumes-from** `DEPL-dShippedRelease-4` — `run_unlease`, whose records landing carries the review record, and the close terms beside which `check_landing_review` runs
- **consumes-from** external — TOOL-dDeclaredLoop-19's breakpoint, -20's trigger and disposal, TOOL-dFairHearing-3's `review_pin.py` and -13's `lenses.toml`, TOOL-dWellOiledMachine-27's `landing` origin
- **hands-off** external — dCalibratedLens's Deploy lenses, which end this unit's stand-in when a `lenses.toml` row names `landing`
- **hands-off** `DEPL-dShippedRelease-51` — `read_landing_pin`, whose `base` that unit reads from `landing_prior_tip` (review id 29)
- **hands-off** `DEPL-dShippedRelease-52` — `read_landing_pin`, whose second-node reading that unit derives (review id 71)
- **hands-off** `DEPL-dShippedRelease-60` — `run_deploy_review`, which that unit gives its first step (review id 4)
- **hands-off** `DEPL-dShippedRelease-73` — `check_landing_review`, whose pass that unit re-derives (review id 82)
- **hands-off** `DEPL-dShippedRelease-78` — the re-walk, which the minors batch repairs (review ids 83)

## 4. Design

### Evidence

Read at `5d1c82ac`; no product file differs from base `f4597719`.

- `KINDS` is `['diff-review', 'spec-audit']` and a value outside it is refused
  (`tools/workflows/tier2-review.template.js:190`). A landing is neither a spec nor a design document,
  and a non-spec `spec-audit` subject reads as a design document (`:428`).
- `review.<stage>` allows `off`, `opt-in`, `owed` and `owed-above-tier`, with `opt-in` for every stage
  but Build (`tools/policy/catalogue.toml:1206-1209`).
- From TOOL-dDeclaredLoop-19:148-150: "for the other stages no per-build opt-in exists in this tree, so
  `opt-in` there places nothing".
- The role row of a `diff-review` run is `closing-review` (`tools/roles/workflows.toml:62`).

### The field

```
review: pending
review: not-placed · review.deploy=opt-in
review: disposed · 2 finding(s) · memory/builds/<slug>/reviews/<record>.md
```

| Field value | `check_landing_review` | `deploy.close` prints |
|---|---|---|
| `not-placed · <value>` | passes | `landing review — <sha8> · not placed · <value>` |
| `pending` | fails | `close — <slug> · held · check_landing_review · pending` |
| `disposed · …` | passes | nothing beyond the disposal line |
| anything else | fails | `… · check_landing_review · unreadable field` |

### The range

`<sha>^1` is the advertised tip the merge was prepared on, so `<sha>^1..<sha>` is the landing's
own diff (`check_prepared_merge`, `tools/push-main.sh:958`, and the prepare's parents, `:947`). A
second node reads it from the graph, the same first parent `read_landing_outcome` derives there
(DEPL-dShippedRelease-12 S8).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `run_deploy_review`, `check_landing_review`, `write_review_patches` | functions, `deploy_items.py` | `py.function`, each OK by `--suggest` at `5d1c82ac` |
| `read_landing_pin` | function, `review_pin.py` | `py.function`, OK |
| `--deploy review`, `dispose-landing`, `--landing` | verb and flags | none |

### Migration

None. A record written before this unit reads `pending`, and DEPL-dShippedRelease-1's records carry it
from their first write, so `--deploy review` is the first thing to move it.

### Rollout

At the default `review.deploy`, `opt-in`, this is one printed line per landing and no review.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S4, S6
- `tools/loop/deploy_fixture.py`: the cases of §6
- `tools/workflows/review_pin.py`: S3
- `tools/workflows/README.md`: S7
- `tools/unattended/unattended.sh`: the verb, S5's path, `KIT_UNATTENDED_VERSION`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`: S7
- `help/deploy.md`: S7

### Alternatives rejected

- **A new harness kind, `landing`.** Rejected: it changes `KINDS`, the record-kind vocabulary and the
  review key for a subject a diff already expresses, and it is dFairHearing's surface. Test:
  `tier2-review.template.js:190`, whose refusal any third kind must pass.
- **`spec-audit` with the landing record as a design subject.** Rejected: its `SPEC_LENSES` read a
  document for design coherence and nothing here is one. Test: `:428`.
- **Blocking `deploy.notify` as the breakpoint's position reads.** Rejected as a guarantee: the notice
  has already gone, and the position stays only because the items after it wait. Test:
  TOOL-dWellOiledMachine-60 S2, S3.
- **Reading `not-placed` as a pass with no line.** Rejected by `[gate]`: an empty population read as
  coverage. Test: AC1.

## 5. Production-readiness checklist

- security — `read_landing` treats the field as a claim, and a value outside the table fails. Findings
  reach `intake.py` as text with its own redaction (TOOL-dWellOiledMachine-4).
- perf / scale — one policy read per landing unless a review is placed; a placed review is the harness's
  cost, on the same fan-out ceilings.
- error / empty / loading states — not placed, pending and disposed are three distinct lines; a report
  with no verdict is refused.
- observability — `review` on the landing record, printed by `read-landing`.
- risks — a build under `owed` whose review never runs holds its lease and its close: the walk's exit 3
  says so at each beat, and the lease ages to `stale` as any live one does.
- testing — `deploy_fixture.py` cases and one `review_pin.py` case over a catalogue with no Deploy lens.
- migration — none.
- user docs — `help/deploy.md`, `tools/workflows/README.md`.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-not-placed` runs `--deploy review` at the default
  `review.deploy`, `read-landing` prints `review<TAB>not-placed · review.deploy=opt-in`, the close prints
  `not placed` and passes the term, and neither output holds the word `clean`.
  Red when: "blocks the close" reads as a green with no review placed.
- **AC2** — When `python deploy_fixture.py --case review-owed` plants `.governance/policy.toml` with
  `review.deploy = "owed"`, the landing stands on the remote, `--deploy review` exits 3, `--deploy close`
  exits 3 printing `held · check_landing_review · pending`; a planted disposed field lets it pass; a
  planted `review: lgtm` holds it.
  Red when: the review blocks the push, or a close passes with the review pending.
- **AC3** — When `python deploy_fixture.py --case review-values` plants each of `off`, `opt-in`, `owed` and
  `owed-above-tier` with a Tier-2 spec and with none, the two `owed` cases and only they fire
  `--trigger`, each with its cause, and a `review.breakpoints` row naming `item.deploy.notify` fires it
  under `off`; the walk reaches the verb after `deploy.recommend` and before `deploy.notify`.
  Red when: a value places a review `derive_breakpoints` did not.
- **AC4** — When `python review_pin.py --landing <sha>` runs in a fixture whose `lenses.toml` holds no row
  naming `landing`, it prints `diff-review`, a `base` equal to `git rev-parse <sha>^1`, no `preset` key
  and `diff defaults · no Deploy lens`, and exits 0; a planted `landing` row prints `Deploy`.
  Red when: a tree with no Deploy lens fails to pin, the clause's seen-on case, or `preset` is passed.
- **AC5** — When `python deploy_fixture.py --case review-disposed` plants a report with two confirmed
  findings, `python deploy_items.py dispose-landing <sha> <report>` files two intakes with two keys, and a
  second run files none; a report with no `## Verdict` line exits 2 and `review` stays `pending`.
  Red when: a finding files nothing, or a re-run files twice.
- **AC6** — When `python deploy_fixture.py --case review-clean` walks a build whose planted report reads
  `## Verdict: CLEAN`, `review` reads `disposed · 0 finding(s)`, the report is on the default branch in
  the records landing, and `deploy.close` records its transition.
  Red when: a clean review holds the close, or its record stays off the tree.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kit version markers` · `recall floor` · `recall floor arms`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC5 AC6 · the `review-` cases, the failing case `review-not-placed` staged against `check_landing_review` passing `pending` · none

New arm: tools/workflows/review_pin.py · covers AC4 · its fixture with no `landing` row, the failing case a planted `preset` key in the landing pin · none

## 8. Open questions

- **F1 — What is the review's subject?** `review.pin` "pins the artifact: ... or the landing record"
  (flow-steps:570). Options: (a) `diff-review` over `<sha>^1..<sha>`, the landing's diff, its record
  read beside it; (b) a new subject kind `landing`; (c) `spec-audit` with the record as a design
  subject. (b) changes dFairHearing's closed `KINDS` and (c) reads a landing for design. RESOLVED
  (agent, 2026-10-30, delegated): (a), rung 3, reuse of the harness as it stands. widens: none · relaxes: none
- **F2 — Which lenses, given `review.pin` passes no landing preset?** The clause says "the preset
  `review.pin` passes", and TOOL-dFairHearing-3 S8 maps spec and design subjects only, with `preset`
  refused on `diff-review` (scout A disagreement 12). Options: (a) pass no `preset`: the diff kind's
  default lenses are the catalogue's, drawn from `lenses.toml`; (b) add a `landing` literal to
  `PRESETS`, a parent's surface, with no lens to put in it. The clause's intent is "the catalogue's
  lenses until the Deploy ones land", which (a) holds. RESOLVED (agent, 2026-10-30, delegated): (a),
  rung 3, deviation 141. widens: none · relaxes: none
- **F3 — What does the default `review.deploy` block?** `opt-in` places nothing (scout A disagreement
  13). Options: (a) a distinct `not-placed` state that passes the term and prints; (b) raise the
  default to `owed`, a catalogue default this unit does not own; (c) pass silently. (b) is the
  owner's key and (c) is the vacuous green. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3,
  `[gate]`. widens: none · relaxes: none
- **F4 — Is the Deploy-lens stand-in a `[[stand-in]]` row?** The brief asks one where a clause names a
  stand-in, and TOOL-dDeclaredLoop-13 S8 reds a row naming no row item or another owner. No item of
  the five programs is dCalibratedLens's Deploy lens: `review.lens` is dFairHearing's and `deploy.recommend`
  dDeclaredLoop's. Options: (a) the catalogue's absence of a `landing` row is the stand-in, printed by
  S3; (b) an invented item. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1,
  TOOL-dDeclaredLoop-13 S8's red rule leaving no other. widens: none · relaxes: none
- **F5 — When does the review run, given the notice has gone?** Scout A disagreement 14. Options: (a)
  at the breakpoint's position, holding the items after it, with the notice already sent; (b) after
  `deploy.unlease`, holding only the close. (b) closes the mailbox and tombstones before the review, so
  its record would need a second records landing. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1,
  flow-steps:494. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 14, flow-steps:441-442, :494-495 and :574,
  `gap-deploy-06`'s review half, and scout A's row and disagreements 12, 13 and 14.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 51, 52, 60, 73, 78); no scope, design or criterion moved.

## 10. Reuse audit

The seams are `derive_breakpoints` and `--trigger` (TOOL-dDeclaredLoop-19, -20, unbuilt) for placing and
firing, `review_pin.py` (TOOL-dFairHearing-3, unbuilt) for the pin, the `review.dispose` landing route
TOOL-dDeclaredLoop-20 declares unarmed, and `tools/workflows/tier2-review.template.js` for the run. `python
tools/codebase-map/reuse_lookup.py "block a build close until a post-landing review is disposed"` returned
name-stem neighbours (`build`, `build_commit`, `build_fixture`), so no shipped seam fits and every seam
here is a parent spec. Scout A's row holds at `5d1c82ac`. The recall probe's hits were this build's records, and neither
disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "what review runs after landing and what does it block" --terms "landing review breakpoint review.deploy opt-in review.pin preset diff-review lenses deploy close"`
