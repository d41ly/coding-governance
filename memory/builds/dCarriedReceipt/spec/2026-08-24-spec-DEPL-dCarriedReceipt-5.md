# DEPL-dCarriedReceipt-5 — the `[[decline]]` contract, and three arms that keep it honest

**Status:** CLOSED · rev-5 · 2026-08-26 · node d · Tier-1 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-build-DEPL-dCarriedReceipt-5-acceptance-ledger.md](../build/2026-08-26-build-DEPL-dCarriedReceipt-5-acceptance-ledger.md) | journal | — |
| [2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round6.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round6.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |

<!-- /gen:spec-records -->

## 1. Goal

A coverage report with no way to say "we deliberately did not take that" is a report an operator
reads once. inCMS's 54-row gap (55 before `-1` lands) contains 11 rows the adopter took under
another name or folded into
another file, so a run that keeps naming them is crying wolf, and the only way to quiet it is to
stop running it. The design problem this unit solves is distinguishing **deliberately not taken**
from **missed** — and it must solve it without creating the thing it is preventing, because an
exclusion list nobody grades is a fork with a friendlier name. The answer is a declaration that
carries machine-gradable evidence and that self-destructs when the world moves underneath it.

## 2. Scope (IN)

- **S1** — `[[decline]]` blocks in the target's `.governance/deploy.toml`, read by `load_deploy`
  (`:553`). That file's own header says it carries every owner decision, and a decline is one.
  Required keys: `kit`, `dest`, `why`.
- **S2** — at most ONE evidence field per row, from a closed set of three: `taken_as`,
  `consumed_into`, `discharge`. Two on one row reds. A row asserting two different things about one
  destination is two rows, and a reader that has to pick between them picks wrong eventually.
- **S3** — `taken_as = "<path>"` is HASH-GRADED. The gov blob comes from `blob_at` (`:2148`) at the
  revision the run measures; the target's bytes come from its INDEX at `taken_as`; both are compared
  CR-stripped, using the same normalisation `cmd_check` already applies to a merged block at
  `:1581` with the `CR` constant at `:1695`. Equal means the row is covered. NOT equal
  **reclassifies the row to `diverged`** and reports it as such; it does not fail. A mismatch says
  the adopter holds the file with local edits, which is a three-way's input (`three_way`, `:2897`)
  once a receipt exists — never a reason to red a coverage report.
- **S4** — `consumed_into = "<path>"` asserts only that the named path is tracked in the target.
  Deliberately weak: gov cannot know what "folded into" means byte-wise, and a predicate that
  pretended to would pass on everything, which is the could-not-fail shape.
- **S5** — `discharge = { command = [...] }` reuses the `[[hole]].discharge` shape verbatim and runs
  through the path `cmd_check` already runs a hole probe on (`:1657-1679`): `resolve_tokens` per
  argv element, refuse naming the key when one is unresolved (`:1669-1672`), `resolve_shell_argv`,
  then `subprocess.run(..., cwd=target)`. Exit 0 is discharged; anything else is reported.
- **S6** — `decline_findings()`, ONE predicate with three staleness arms, mirroring the exemption
  hygiene `selfcheck` already runs at `:1203-1223`. An empty `why` reds, in the words that arm
  already uses at `:1208-1210`. A decline whose `dest` is now PRESENT in the target reds. A decline
  whose `dest` no claimed kit ships at the revision the run measures reds — the arm that makes the
  list self-cleaning when gov withdraws a file.
- **S7** — two call sites for that one predicate: `cmd_check`, and `plan --coverage` from `-4`. A
  decline may only hide a gap row in a run that also grades it.

## 3. Non-goals (OUT)

- **Not** a free-form rewrite rule, and **not** line-level partial application of a residual file.
  Both are on this build's ratified OUT list; `consumed_into` records that a fold happened and
  claims nothing about which lines.
- **Not** automatic rename detection. `taken_as` is a DECLARATION an owner writes; inferring it is
  on the OUT list, and the whole point of this unit is that the inference is the owner's to make.
- **Not** a write path. `taken_as` does not make the relocated file an `update` destination. That
  needs the two identities (`-7`) and the receipt `adopt` writes (`-13`).
- **Not** converting `:1581`'s text-side CR-stripped hash to the new bytes helper. It computes a
  value stored in receipts, and re-spelling it is a different unit's risk for no gain here.
- **Not** a decline for a whole kit. That case is expressed by omission from `deploy.toml`'s `kits`
  list, and `cmd_update` already reports it at `:3027`.
- **Land-alone:** this unit must land AFTER `-4`, because `plan --coverage` is the reader that
  consumes a decline. It leaves both trees green on its own: a target with no `[[decline]]` block
  behaves byte-identically to today.

## 4. Design

"Deliberately not taken" is not a property of the file; it is a property of the DECISION, and a
decision is only distinguishable from an oversight by the evidence attached to it. So the row asks
for two different things at once. `why` is for the human who reads the report next year and is
graded only for existence, because grading prose is how a gate starts lying. The evidence field is
for the machine and is graded for truth. A row may carry `why` alone — that is the honest "we chose
not to take it" — and it is precisely that row the three staleness arms exist for: with no evidence
field, the only thing keeping it from becoming permanent fiction is that it reds the day the file
appears, and reds the day gov stops shipping it.

`taken_as` mismatching is deliberately NOT a failure, and that is the load-bearing choice in this
unit. The alternative reds the honest adopter who relocated a file and then edited it, whose only
route back to green is deleting the decline — the exclusion list eating the evidence that made it
trustworthy. Reclassifying to `diverged` keeps the row, keeps the reason, and puts the file into the
state `VERDICT_GRID` (`:2843`) already names for exactly this.

### Data model

One TOML array-of-tables in the target descriptor. Every field is owner-authored.

| field | required | asserts | graded by |
|---|---|---|---|
| `kit` | yes | which kit's row this excuses | the kit is in `deploy.toml`'s `kits` |
| `dest` | yes | the planned destination not held | arms 2 and 3 of S6 |
| `why` | yes | the human reason | arm 1: empty reds |
| `taken_as` | no | gov's bytes live here instead | CR-stripped hash vs `blob_at` |
| `consumed_into` | no | folded into this tracked file | the path is tracked |
| `discharge` | no | this command proves it is handled | exit 0 |

### Alternatives rejected

- *A boolean `declined = true` on some row.* No reason, no evidence, no expiry — the shape that
  makes an exclusion list a fork.
- *A separate `.governance/declines.toml`.* A second owner-decision file is a second place to look
  and a second thing to keep in sync, and `deploy.toml`'s own header already claims the job.
- *Grading `why` for content — length, a record id, a pattern.* Every such predicate is satisfiable
  by typing something, so it buys nothing over existence and costs a false sense of enforcement.

### Files touched (estimate)

`tools/govkit/govkit.py` (~85 lines across `decline_findings`, one bytes-side hash helper, and two
call sites), `tools/govkit/selftest.py` (8 arms), `WIRE-INTO-PROJECT.md` (the decline section),
`tools/govkit/refusal_join.py` (`BRANCH_PIN`, re-derived).

## 5. Production-readiness checklist

- security — `discharge` runs an argv from the TARGET's own descriptor. That is not new exposure:
  `[[hole]].discharge` already does exactly this through the same runner, in the same verb, against
  the same file, and this unit adds no second execution path.
- perf / scale — one `blob_at` and one index read per `taken_as` row. Bounded by the number of
  declines an owner typed, which is bounded by the coverage gap.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a target with no `[[decline]]` block takes no new code path. A
  decline naming a `kit` absent from `kits` reds by name rather than being silently skipped, which
  is the same silence class the third arm exists to close.
- observability — every declined row prints as declined with its `why`, never as absent and never
  omitted. A gap that disappears from a report without saying why is the failure mode of every
  exclusion list.
- risks — the residual risk is an owner who declines a row they should have taken. Nothing detects
  that, and this spec does not claim otherwise; what it guarantees is that the decline names a
  reason, is re-graded on every run, and dies when the file arrives or gov withdraws it.
- testing + left-shift gates — AC2 through AC4 are the left-shift, one arm per staleness class, and
  each is the same class the exemption hygiene at `:1203-1223` already gates one level up.
- migration / rollback — none. `[[decline]]` is additive TOML; a descriptor written before this unit
  parses identically after, and a revert makes the blocks inert rather than invalid.
- user docs — `WIRE-INTO-PROJECT.md` gains a decline section: the three fields, the three arms, and
  the sentence that a decline is a decision rather than a mute button.

## 6. Acceptance criteria

- **AC1** — At `9ddcc5c9`, a `[[decline]]` block in a target's `.governance/deploy.toml` is parsed
  by `load_deploy` and read by nothing: `grep -n "decline" tools/govkit/govkit.py` returns no hits.
  Observe this first — an owner decision the tool cannot see is the defect.
- **AC2** — A decline with `why = ""` reds, naming the `kit` and `dest`, in `check` and in
  `plan --coverage` alike.
- **AC3** — A decline whose `dest` IS tracked in the target reds as stale, and the message says the
  file arrived rather than saying the decline is malformed.
- **AC4** — A decline whose `dest` is shipped by no claimed kit at the measured revision reds as
  stale. Built by removing the source rule from a fixture descriptor, which is the withdrawal case.
- **AC5** — With `taken_as` naming a path whose index blob equals the gov blob after CR-stripping,
  the row reports `declined` and drops out of the gap count; with one byte changed, the same row
  reports `diverged` and the run's exit code is unchanged.
- **AC6** — `taken_as` differing from the gov blob ONLY in line endings still reports `declined`.
  This is the arm that fails against a plain `_sha` comparison, and it is why the helper strips `CR`.
- **AC7** — `consumed_into` naming a tracked path passes; naming an untracked one reds.
- **AC8** — `discharge = { command = [...] }` exiting 0 reports discharged; exiting 1 reports
  undischarged; carrying an unresolved `{token}` refuses and names the key, matching `:1669-1672`.
- **AC9** — A row carrying both `taken_as` and `consumed_into` reds on the one-evidence-field rule
  before either is evaluated.
- **AC10** — Under `python tools/govkit/govkit.py plan --coverage`, declining N gap rows moves
  exactly N out of the gap count into the declined count, and the WRITE-ROW TOTAL does not move. A decline that shrank the denominator would be hiding
  gov's own population rather than excusing a row, which is what this asserts against.

  **AMENDED at rev-5.** The criterion used to name a frozen fixture seeded with a specific gap
  count at the base sha, and specific declared and residual counts. Those are three measurements of
  one adopter at one gov vintage, and gov has shipped files since — a fixture reproducing them
  would have to be manufactured rather than measured, which is the staged-break class: an arm that
  proves a mechanism against a value invented for it proves it for the invented value. The
  arithmetic above IS the property of this code, it is gateable on any fixture, and it is gated.
  The live reading against the adopter the criterion named goes in the acceptance ledger, taken
  from that repository's OWN declared kit map and never from an invented one.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically `govkit selftest`, `govkit selfcheck` and
`govkit refusal join`. That last one is a real obligation rather than a mention: this unit adds
roughly seven refusal branches, and `BRANCH_PIN` in `tools/govkit/refusal_join.py:41` is a
shrink-only FLOOR, so it is re-derived at landing rather than pinned to a literal here, and it is
moved in the SAME commit with both values named beside it, per that file's own convention. Every
new branch also needs an arm asserting it, which is the join's declared contract and is why the arm
count in §4 tracks the branch count.

## 8. Open questions

- **F1 — do the three arms live in `check` only, or in `check` and `plan --coverage`?** Both, as one
  predicate with two call sites. `check` refuses without a receipt (`:1480-1485`), so a check-only
  placement would leave the arms unreachable at every target this build is trying to reach, and
  `plan --coverage` is the run that ACTS on a decline by hiding a row. A list that is applied in one
  verb and graded in another is graded nowhere the day someone runs only the first.
  RESOLVED (agent, 2026-08-24, delegated): one predicate, both call sites.
- **F2 — is a decline with `why` and no evidence field legal?** Yes. Requiring evidence would make
  the common honest case — "we looked at it and chose not to take it" — inexpressible, and an
  inexpressible decision gets expressed by deleting the kit from `kits` instead, which loses far
  more. The three staleness arms are what make the bare form safe.
  RESOLVED (agent, 2026-08-24, delegated): legal, graded by the staleness arms.

## 9. Revision log

- rev-5 · 2026-08-26 · BUILT and CLOSED on node `a`, session `aResumedRelay`. ONE criterion
  AMENDED: AC10 pinned a frozen fixture at a gap count measured on one adopter at the base sha,
  plus the declared and residual counts that follow from it. Reproducing those today would mean
  manufacturing the fixture rather than measuring it — the staged-break class, where an arm proves
  a mechanism against a value invented for the arm. What AC10 now asserts is the ARITHMETIC, which
  is a property of this code and is gateable on any fixture: N declines move N rows, and the
  write-row total does not move. The live reading is in the acceptance ledger. §7's other
  obligation was met as written rather than amended: `BRANCH_PIN` was RE-DERIVED at landing —
  eleven new branches, not the seven the spec estimated — moved in the same commit with both
  values named beside it, and every one of the eleven is armed.

- rev-4 · 2026-08-25 · round-4 fold: L4 — §7's `BRANCH_PIN` sentence rendered an English clause as
  an inline code identifier and cited `tools/govkit/refusal_join.py:40`, where the constant is at
  `:41` and `:39-40` is the comment above it. It now carries `-9` §7's repaired shape, identifier
  inside the backticks and property in prose beside it, with the duplicated shrink-only clause
  dropped.
- rev-3 · 2026-08-25 · round-5 fold: §1's coverage figure carried the pre-`-1` vintage flat, which
  `-4` rev-2 arms as a regression alarm. It now reads 54 with 55 labelled as the pre-`-1`
  measurement, and AC10's fixture is labelled frozen rather than live.
- rev-2 · 2026-08-24 · round-3 fold: the literal `BRANCH_PIN` value is withdrawn — it is a
  shrink-only FLOOR and the build's own landing order falsifies any number pinned here before this
  unit lands.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass. Every cited site was read at
  `9ddcc5c9` and three brief citations are corrected here rather than repeated. The hole-discharge
  runner the `discharge` field reuses is at `:1657-1679`, not the `[check].argv` runner at
  `:1629-1653`; the brief's `:1632-1652` spans the second, which is the wrong one of the two
  probe runners in that function. `three_way` is at `:2897`. And `Refusal` is at `:78` while
  `Report` is at `:565`, so the brief's single `:566` names neither class statement. The
  reclassify-rather-than-fail rule for `taken_as` is recorded in §4 as the unit's load-bearing
  choice, because it is the one an eager reviewer will try to tighten.

## 10. Reuse audit

Every field in this contract wires through a seam that already exists, which is what keeps a
declaration file from becoming a second engine. `load_deploy` (`:553`) is the reader; `blob_at`
(`:2148`) is the one provenance source and is never replaced by a working-tree read; `tracked`
(`:111`) answers presence for `consumed_into` exactly as it does for coverage; `discharge` reuses
the `[[hole]]` shape and the runner at `:1657-1679` rather than defining a second command form; the
three arms are the exemption hygiene at `:1203-1223` re-aimed at a different declaration; `Report`
(`:565`) carries every finding. One genuinely new thing is added and is named rather than hidden: a
bytes-side CR-stripped sha helper beside `_sha` (`:2870`), because the only existing normalisation
is text-side at `:1581` and `blob_at` returns bytes. It is one helper with the same computation, not
a second normalisation policy, and §3 records why `:1581` is deliberately left calling its own.
