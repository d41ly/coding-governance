# DEPL-dCarriedReceipt-12 — write preconditions and a lock, on both writing verbs

**Status:** CLOSED · rev-7 · 2026-08-26 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-DEPL-dCarriedReceipt-1-adopter-measurements.md](../build/2026-08-24-build-DEPL-dCarriedReceipt-1-adopter-measurements.md) | research | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 |
| [2026-08-25-build-DEPL-dCarriedReceipt-12-acceptance-ledger.md](../build/2026-08-25-build-DEPL-dCarriedReceipt-12-acceptance-ledger.md) | journal | — |
| [2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |

<!-- /gen:spec-records -->

## 1. Goal

`cmd_update` has no in-progress-operation guard of any kind, and `cmd_apply`'s guard is dead in the
worktree layout adopters are told to use. `update --write` against a path carrying a live `UU`
collapses three index stages to zero through its own `git add` (`:3103`), and both sides of the
operator's merge become unrecoverable. Nothing else in this build may gain a write path until a
write refuses to run on a tree that is mid-operation.

The same hole has a second half, and nobody owned that one either: the preamble validates that
`--to` resolves (`:2940-2944`) and that the receipt's `gov_commit` resolves (`:2946-2955`), and then
never compares them to each other or to any ref. So `update --to <older sha>` raw-writes every clean
row BACKWARDS and rewinds `receipt["gov_commit"]` at `:3126`, and `update --to <feature-branch-tip>`
lands bytes from a branch no adopter was ever offered. A precondition that checks the tree but not
the vintage is half a guard, so both halves land here.

## 2. Scope (IN)

- **S1** — replace the `target/.git/<marker>` path stat at `:2334` with `git rev-parse --git-path
  <marker>`, the form already used at `:2019`, so the probe resolves in a linked worktree where
  `.git` is a file.
- **S2** — apply that probe **unconditionally** in both `cmd_apply` and `cmd_update`. Today it sits
  inside `if pins:`, so a target declaring no `lf_pin` is unguarded even where the path form works.
- **S3** — refuse on `git ls-files -u` returning any row (an unresolved merge in the index).
- **S4** — refuse when any path the receipt claims is dirty, naming the paths. A dirty file outside
  the receipt's population does not block.

  **DIRTY IS DEFINED HERE, once, because three acceptance criteria in two other units depend on the
  answer and two of them need it in opposite directions.** A claimed path is dirty when it differs
  index-versus-HEAD or worktree-versus-index — `git diff --cached` and `git diff` over that path, and
  deliberately NOT `git status --porcelain`, which also flags `??`. Two carve-outs, the second of
  them bought by a criterion elsewhere:
  - A claimed path absent from both the index and the worktree is dirty when HEAD still carries it:
    a STAGED deletion is an operator decision and the run refuses, naming the path. It is NOT dirty
    when HEAD does not carry it either, which is the committed deletion `-9` S11 restores and `-9`
    AC9 requires; that is the only state this carve-out covers, and the reason is that there is
    nothing left to diff.
  - An untracked file SHADOWING a claimed path that is absent from the index is **not dirty** here.
    That state is `-7` S4's refusal, which names the path and the risk; two units refusing the same
    state gives the operator two different messages for one tree.
  - **A THIRD CARVE-OUT, added at rev-7 by owner ruling 2026-08-26: gov's OWN staging.** A path whose
    only difference is index-versus-HEAD, and whose index blob is the exact `oid` the receipt
    recorded landing there, was staged by this tool and by nothing else. This unit shipped without
    it and PARKED the consequence: `apply` STAGES everything it lands, so a completed apply made
    every receipt-claimed path dirty by the definition above. A second `apply` refused, `update
    --write` straight after `apply` refused, and `apply --resume` refused STRUCTURALLY -- it needs a
    receipt, a receipt needs a completed apply, and a completed apply leaves the target dirty, so
    that path was unreachable without an unrelated commit in between. THE OID COMPARISON IS WHY THIS
    IS NOT A WEAKENING: an operator's staged edit to a gov-owned path produces a DIFFERENT index
    blob and stays dirty, which is the case S4 exists for, and an unstaged worktree edit is
    untouched. Armed as a PAIR -- the post-apply run proceeds, the operator's staged edit still
    refuses -- because either arm alone is indistinguishable from deleting the guard.
- **S5** — an `O_EXCL` lock at `.governance/outbox/.update.lock`, taken by both writing verbs,
  released on every exit path including refusal, and carrying the pid and start time so a stale lock
  is diagnosable rather than mysterious.
- **S6** — every refusal names the condition, the marker or path that tripped it, and what to do.
- **S7** — `update` refuses when `--to` is not a DESCENDANT of the receipt's `gov_commit`, measured
  with `git -C <gov> merge-base --is-ancestor <base_commit> <to_commit>`. The refusal names BOTH
  shas and says a downgrade is not an update. Equal commits pass — `--is-ancestor` holds reflexively,
  so a re-run at the same vintage stays legal — and a receipt carrying no `gov_commit` skips the
  check, matching the existing `if base_commit:` guard at `:2946`.
- **S8** — `update` refuses when `--to` is reachable from no ref, measured with `git -C <gov>
  for-each-ref --contains <to_commit> --count=1` returning nothing. `rev-parse --verify` at `:2940`
  accepts any object that EXISTS — a dangling commit, a fetched-but-unmerged tip — which is how a
  branch nobody shipped becomes an adopter's new baseline. It is the same class `-13` S3 refuses on
  the read side by declining `git log --all`; refusing it on the write side too keeps one answer to
  the question of what vintage an adopter may be moved to.

## 3. Non-goals (OUT)

- **Not** auto-resolving, stashing, or aborting anything in the target. A deployer that tidies the
  operator's tree is a deployer that loses work; refuse and say why.
- **Not** a `--force` escape. Deliberate: the whole point is that the muscle-memory invocation must
  not be the destructive one, and a flag reachable in a hurry is not a guard.
- **Not** journal/resume for a crash mid-write; that is parked on the build's cut list and reuses
  `apply --resume`'s existing mechanism when it lands.

## 4. Design

### The precondition order, stated once for the whole build

This unit owns the FIRST gate a write passes, and FIVE other units add their own further in. No spec
composed them, so the order is declared here and the others cross-reference it rather than restating
it. A `--write` run passes in this sequence and stops at the first refusal. The table runs from the
preamble to the write. `-14`'s post-write verification is step 12 and is the only entry AFTER bytes
land; its snapshot and baseline are steps 10 and 11, whose relative order is free.

| # | owner | what it decides | on failure |
|---|---|---|---|
| 1 | this unit, S1–S3 | is the target mid-operation? | refuse, whole run |
| 2 | this unit, S4–S5 | is any receipt-claimed path dirty, and can the lock be taken? | refuse, whole run |
| 3 | this unit, S7–S8 | is `--to` a descendant of the receipt's `gov_commit`, and reachable from a ref? | refuse, whole run |
| 4 | `-7` S9 | for a row carrying BOTH `commit` and `gov_oid`, do they agree? | refuse, whole run |
| 5 | `-7` S4 | is a claimed path present in the worktree and absent from the index? | refuse, whole run |
| 6 | `-13` S7 | does this ROW carry `evidence: "unattributed"` AND resolve to the `table` disposition? | print, count, skip the ROW, after `how` resolves and before `classify_row` |
| 7 | `-9` S1/S5 | which `carry` rung, if any, proves itself over the whole file? | no failure mode; it classifies |
| 8 | `-11` S2 | did gov rename this row's source between the two vintages? | verdict `renamed`; `-11`'s own two refusals |
| 9 | `-9` S6 | apply the proven rung to `base` and `theirs` before `three_way` | no failure mode; it feeds the merge |
| 10 | `-14` S2–S3 | snapshot every touched row's paths and its six identity fields | none; it is the rollback's only input |
| 11 | `-14` S4 | run each touched kit's `[check].argv` as a BASELINE | none; it decides whether step 12 may roll back |
| 12 | `-14` S4–S5 | re-run each touched kit's `[check].argv` AFTER the write | roll back from the recorded OIDs; `r.fail` |

Two things in that table are load-bearing rather than arbitrary, and the first is easy to get
backwards. **Steps 4 and 5 are in the PREAMBLE and step 6 is inside the classification loop**, so the
integrity check runs BEFORE the unattributed skip and cannot lean on it. That is precisely why `-7`
S9 is scoped by FIELD PRESENCE rather than by `evidence`: an unattributed row carries neither
field, so S9 has nothing to assert about it and passes over it silently, and the row is skipped by
name two steps later. Scope S9 by `evidence` instead and it would have to know a classification
that has not happened yet — `evidence` is `-13`'s field and is exactly what step 6 keys on. `role`
is different: it is on every row `apply` and `adopt` write and is read at `:2973` before the
dispatch resolves at `:2974`, which is why S9's one exemption by ROLE (`-7` §8 F4) needs no later
precondition and does not re-open this ordering. Scope it by nothing and it refuses on all 41 of
inCMS's unattributable rows and no adopter ever updates. Second, **steps 1–5 precede everything
per-row**, because a refusal that depends on which rows a receipt happens to hold is a refusal an
operator cannot predict.

### Data model

No receipt change. The lock is a file, not a field.

### Migration

None. Both verbs gain refusals only; a clean target behaves exactly as today. S7 and S8 are
`update`-only and read `receipt["gov_commit"]`, a field that already exists and whose shape they do
not change.

### Alternatives rejected

- *Keep the path stat and special-case a worktree.* A second way to answer "where is the git dir"
  is a second answer that drifts. `--git-path` already exists in this file and is correct for every
  layout, including submodules — which matters, because NicoCares is one.
- *Guard only `update`.* `apply` writes `.gitattributes` and lands bytes; it has the same exposure
  and already ships a guard that merely does not work.
- *Advisory warning instead of refusal.* A warning printed above a successful-looking write is what
  the operator will not read.
- *Accept any `--to` that resolves and let the three-way sort out a bad vintage.* Measured false: a
  row whose identities agree never reaches `three_way` at all — it takes the raw arm at `:3069-3071`
  — so "the merge will catch it" is exactly wrong for the clean rows a backwards `--to` would
  silently rewind. A vintage has to be refused before the dispatch, not survived after it.

### Files touched (estimate)

`tools/govkit/govkit.py` (~60 lines), `tools/govkit/selftest.py` (8 arms), one fixture that builds
a linked worktree and one scratch gov carrying a two-branch history.

## 5. Production-readiness checklist

- security — the dirty-path refusal closes a real exposure: a write onto an unstaged local edit is
  indistinguishable afterwards from an edit the operator made. S7 and S8 close the supply-side twin:
  without them the vintage an adopter is moved to is whatever the invoking operator typed, backwards
  shas and unpublished branch tips included.
- perf / scale — one `rev-parse` and one `ls-files -u` per run; negligible against the blob reads
  already performed.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a stale lock prints its recorded pid and age and the command to
  clear it, rather than an unexplained refusal.
- observability — every refusal names its condition; the lock file records who holds it.
- risks — the residual risk is a target mutated by another process between the precondition check
  and the write. The lock covers govkit-vs-govkit; it does not cover govkit-vs-human, and this spec
  does not claim otherwise.
- testing + left-shift gates — eight arms, each observed RED before the fix. The linked-worktree arm
  is the one that matters and is the one no existing fixture covers, which is why the defect shipped.
  The two vintage arms gate the CLASS — any `--to` outside the forward, published range — rather than
  the single older-sha instance that surfaced them.
- migration / rollback — none; revertible as a pure addition of refusals.
- user docs — `WIRE-INTO-PROJECT.md` gains the precondition list beside the update step.

## 6. Acceptance criteria

- **AC1** — With `MERGE_HEAD` present in a **linked worktree** target, both `govkit.py apply` and
  `govkit.py update --write` refuse by name. Observe RED first: at `9ddcc5c9` both proceed, because
  `.git` is a file there and the path stat cannot fire.
- **AC2** — With `MERGE_HEAD` present in a normal (non-linked) target that declares **no** `lf_pin`,
  `apply` refuses. Observe RED first: today the probe sits inside `if pins:`.
- **AC3** — With an unresolved path in the index (`git ls-files -u` non-empty), `update --write`
  refuses and the index still shows three stages afterwards (`git ls-files -u | wc -l` unchanged).
- **AC4** — With one receipt-claimed path dirty, `update --write` refuses and names that path; with
  a dirty path **outside** the receipt population, it proceeds.
- **AC5** — Two concurrent `update --write` runs against one target: the second refuses on the lock
  and the first completes; after both, `.governance/outbox/.update.lock` is absent.
- **AC6** — A refusal path also releases the lock: after AC3's refusal, `.update.lock` is absent.
- **AC7** — With a receipt recording `gov_commit` at a NEWER sha, `update --to <older sha> --write`
  refuses by name, prints both shas, writes zero bytes, and leaves `receipt["gov_commit"]` at the
  newer value. Observe RED first: at `9ddcc5c9` the run proceeds, takes the raw arm on every clean
  row and rewinds the field at `:3126`. A `--to` that IS a descendant, and a `--to` equal to
  `gov_commit`, both still proceed.
- **AC8** — `update --to <sha reachable from no ref> --write` refuses by name; that same sha, once a
  ref contains it, proceeds. Observe RED first: `rev-parse --verify` at `:2940` accepts a dangling
  or branch-only object today and nothing else looks.
- **AC9** — A claimed path deleted with `git rm` and NOT committed refuses by name; the same path
  once committed proceeds to the `missing` cell. Both arms run against S4's definition and neither
  is reachable from AC4's dirty-path arm, which edits a path that still exists.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` leg, plus
`tools/govkit/refusal_join.py` — this unit adds eight refusal branches, S7's and S8's included, and
every one needs an arm asserting it, which is the join's declared contract.

## 8. Open questions

- **F1 — should the dirty-path refusal cover the whole target or only receipt-claimed paths?**
  Receipt-claimed only. A deployer refusing over an unrelated edit in a repo it does not own is a
  deployer people learn to work around.
  RESOLVED (agent, 2026-08-24, delegated): receipt-claimed only, under the full-scope approval.
- **F2 — lock scope: per target, or per (target, verb)?** Per target. `apply` and `update` both
  write the receipt, so letting them interleave is the case the lock exists for.
  RESOLVED (agent, 2026-08-24, delegated): per target.

## 9. Revision log

- rev-7 · 2026-08-26 · node a · owner ruling: S4 takes a THIRD carve-out for gov's own staging,
  keyed on the recorded `oid` rather than on the fact of being staged. Closes the operator burden
  this unit parked at build time, and the `apply --resume` path it made structurally unreachable.
  The `settle()` helper and the seven fixture sites that call it STAY -- committing between writing
  verbs is still the modelled flow, and those arms assert what they always did.

- rev-6 · 2026-08-25 · round-6 fold: H1 — §4's ordering prose still argued that `-7` S9 CANNOT
  be scoped by `role`, which is exactly what S9's fourth arm now does. The round-5 narrowing
  landed in `-7` and not here, and `-12` is README step 2 while `-7` is step 3, so a builder met
  an emphatic impossibility argument before meeting the ruling. The paragraph now contrasts
  `role` against `evidence` alone: `role` is stored on every row `apply` and `adopt` write and is
  read at `:2973` one line before the dispatch resolves at `:2974`, so the exemption (`-7` §8 F4)
  needs no classification to have happened. The "scope it by nothing" clause and the 41-row
  measurement are untouched — both are correct and neither is about `role`.
- rev-5 · 2026-08-25 · round-4 fold: H5 restates S4's first carve-out — a STAGED deletion is dirty
  and refuses, a COMMITTED one is not — and deletes the false claim that the carve-out is what buys
  `-9` AC9 and AC10, with AC9 added over both states. M1 renumbers §4's ordering table 1..12 with no
  letter suffixes, moves `-7` S4 above the per-row skip, adds `-14`'s snapshot and baseline as steps
  10 and 11, and amends the two orderings named below it. H1 rewrites step 6's decision and failure
  cells: the skip is scoped to rows resolving to the `table` disposition and runs after `how`
  resolves, before `classify_row`. The declared arm count moves 7 to 8 for AC9; the refusal-branch
  count is unmoved, because a staged deletion refuses through S4's existing dirty branch.
- rev-4 · 2026-08-25 · round-5 fold: `dirty` is DEFINED in S4, with the two carve-outs three
  acceptance criteria in two other units depend on. §4's table is corrected and completed — step
  6's owner was wrong, `-7` S4, `-11` and `-9` S6 were missing, `-14`'s post-write rollback is now
  step 9, and "three other units" was five.
- rev-3 · 2026-08-24 · round-4 fold: §4 gains the build-wide PRECONDITION ORDER, which no spec
  composed. Six steps across four units, with the two load-bearing orderings named — `-7` S9 is in
  the PREAMBLE and `-13` S7's skip is in the LOOP, which is exactly why S9 is scoped by field
  presence and passes silently over a row carrying neither field.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold); the dead-guard
  mechanism verified in source against `9ddcc5c9` and reproduced in a live linked worktree.
- rev-2 · 2026-08-24 · folded the pre-code review: adopted R4's two unowned `--to` preconditions as
  S7 (descendant of the receipt's `gov_commit`) and S8 (reachable from some ref), each with its own
  AC and `refusal_join.py` arm, and raised the declared branch count from six to eight. Both git
  predicates were run at `9ddcc5c9` before being written down: `merge-base --is-ancestor` holds
  reflexively on an equal sha and fails on a backwards one, and `for-each-ref --contains` answers
  non-empty for a commit some ref reaches.

## 10. Reuse audit

Reuses the `git rev-parse --git-path` form already present at `govkit.py:2019` rather than adding a
second git-dir resolver — the duplicate-answer defect this file's own comments name elsewhere. The
refusal shape reuses the existing `Refusal` class and its message discipline, and the new branches
are counted by the existing `refusal_join.py` contract rather than a new counter. No new seam: both
verbs already have a preamble where preconditions belong, and `cmd_apply` already demands
cleanliness in one place — this unit generalises that call site instead of adding one. S7 and S8 sit
in that same preamble, beside the two resolve-checks they complete, and both ask git directly rather
than building a second model of the commit graph inside govkit.
