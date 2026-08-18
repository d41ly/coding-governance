# TOOL-aPacedTurnstile-7 — the push boundary scopes to the diff, and "every leg" becomes a bounded obligation

**Status:** OPEN · rev-5 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

`.githooks/pre-push` exports `GATE_FULL=1`, so every landing runs all 70 legs and pays a measured
873 s — a records-only landing included, at 14x the 62 s its own guards would have cost. Scope the
push boundary to the diff, and replace the property that forcing bought with a bounded, recorded
obligation instead of deleting it.

## 2. Scope (IN)

- **S1** — `.githooks/pre-push` stops exporting `GATE_FULL=1` unconditionally; it decides.
- **S2** — the hook forces a full run when the run record's last full green is absent, is not an
  ancestor of the pushed tip, or is more than `GATE_FULL_MAX_LAG` commits behind it.
- **S2b** — the hook forces a full run when the record's TREE fingerprint does not equal a fresh
  fingerprint of the pushed tip (predicate 0), when the lag value is not a decimal integer
  (predicate 6), and on any `push-main` retry after the first, whose reconcile merge commit no
  recorded green describes (predicate 7). It computes that fingerprint by CALLING
  `TOOL-aPacedTurnstile-5`'s shipped helper, never by reimplementing the digest — two implementations
  of one digest disagree silently and then force full forever, which reads as caution rather than as
  the defect it is.
- **S3** — the hook forces a full run when the pushed diff touches `tools/gate-legs.json`, the file
  in which a guard can be narrowed.
- **S4** — the hook forces a full run when the recorded leg-manifest fingerprint differs from
  `git hash-object tools/gate-legs.json` at the pushed tip.
- **S5** — the decision and its reason are printed on one line, and passed to the runner in the
  environment so it lands in the record's header as a declared key. The first draft said "written to
  the run record" with no mechanism, which contradicted this unit's own non-goal of not owning the
  record format and would have been cleared by the record's start-of-run reset in any case.
- **S6** — `GATE_FULL_MAX_LAG` is a SOURCE CONSTANT in `.githooks/pre-push` with its justification in
  a comment beside it. No sibling creates a runtime conf the hook could read: the kit descriptor is
  TOML a bash hook cannot parse, and the profile table's header forbids a coverage knob by rule. It
  is deliberately NOT the `GOV_DEFAULT_BRANCH` shape, which the spec audit showed does not exist as
  described and would be fail-OPEN here — an environment value that widens the lag leaves no diff
  behind, which is the defeatable class `TOOL-aStandingWrit-4` recorded in this very hook. If an
  environment value is honoured at all it is CLAMPED and validated, and anything non-integer forces
  full rather than being ignored.
- **S7** — the hook exports the no-halt flag `TOOL-aPacedTurnstile-3` defines, unconditionally and
  independently of its own scoped-or-full decision, so a landing always gets a complete verdict list
  instead of stopping at the first red chunk.
- **S8** — `.githooks/pre-push.test.sh` gains one arm per forcing predicate, one arm proving the
  scoped path actually scopes, and one proving the no-halt export.
- **S9** — the safety property is rewritten wherever it is stated: `AGENTS.md`, the playbook
  template's diff-scope line, AND `tools/run-gates/run-gates.sh`'s own header comment, which states
  the same claim and which `TOOL-aPacedTurnstile-1` ships into the kit and therefore to adopters.
- **S10** — close the one guard hole that is verified still open, named in
  `memory/builds/cKeyedLaunchpad/README.md` park 2 and in `cBriefedPilot-15`: the kit/dogfood parity
  leg's guard omits `memory/guides/`, which is a file pair it actually validates.

## 3. Non-goals (OUT)

- Changing what any leg asserts. Widening guards in general stays out: S10 closes the ONE hole that
  is verified open and recorded twice, and does not open a survey of the other 41.
- The run record's format, location and writer. That is `TOOL-aPacedTurnstile-5`; this unit is a
  consumer and states only what it reads.
- Removing `GATE_FULL`. It stays as the manual escape and as the mechanism this unit sets.
- Making the bar faster. Scoping changes which legs run, never how fast a leg is.
- Proving guard completeness. Named as the follow-up that would retire this unit's residual risk.

## 4. Design

### The property, before and after

Today the hook's own comment states it. `GATE_FULL` marks "THE run that must be total: the self-test
legs are diff-scoped on earlier runs, and if that scoping reached here no run would ever execute
every leg against the tree that actually lands." That is accurate, and two records already lean on
it. `memory/builds/cBriefedPilot/spec/2026-08-14-spec-cBriefedPilot-15.md` names a leg whose guard
omits `memory/guides/BUILD-METHOD.md` and is caught only at the push boundary.
`memory/builds/cKeyedLaunchpad/README.md` refused to widen a guard because `GATE_FULL=1` covers it.

The replacement property, as it will be written into `AGENTS.md`: every leg runs against a tree that
lands at least once every `GATE_FULL_MAX_LAG` commits, and always when the leg set or its guards
move. That is strictly weaker. It is also, unlike today's property, MEASURABLE — the record makes
"when did every leg last run, and on what sha" answerable, which nothing answers today.

### Data model

The hook reads four fields from the run record and nothing else: the sha of the most recent run in
which every leg ran and passed, that run's leg-manifest fingerprint, its TREE fingerprint, and a
schema version it can refuse. The tree fingerprint is what predicate 0 joins against a fresh
fingerprint of the pushed tip; without that join a green earned on a dirty working tree resets the
lag counter, and the replacement property written into `AGENTS.md` becomes false while the record
makes it look measured. Field names are owned by `TOOL-aPacedTurnstile-5`.

### The decision

Evaluated in order; the first hit forces and stops.

| # | predicate | reason string |
|---|---|---|
| 0 | the record's tree fingerprint does not equal a fresh fingerprint of the pushed tip | `the record describes a different tree` |
| 1 | no run record, or it does not parse, or its schema version is unknown | `no usable run record` |
| 2 | recorded manifest fingerprint differs from `git hash-object tools/gate-legs.json` | `the leg manifest changed` |
| 3 | `git merge-base --is-ancestor` of recorded sha against the tip is non-zero | `the last full green is not an ancestor` |
| 4 | `git rev-list --count` over recorded sha to tip exceeds `GATE_FULL_MAX_LAG` | `N commits since the last full bar` |
| 5 | the pushed diff touches `tools/gate-legs.json` | `the leg manifest is in this diff` |
| 6 | `GATE_FULL_MAX_LAG` is set to anything that is not a decimal integer | `unusable lag` |
| 7 | this is a `push-main` retry attempt after the first | `a reconcile merge is not covered by the record` |

**Every predicate fails toward FULL.** An absent, unreadable, unparseable or ambiguous record yields
a full run, never a scoped one. This is the entire safety argument, and it is why each read is
written as a failure that sets the reason rather than as an assignment that might leave a variable
empty. `TOOL-aStandingWrit-4` recorded that exact class in this same hook, where an unmatched
`GOV_DEFAULT_BRANCH` sent it down its own "nothing to gate" exit 0 and skipped every leg on the bar.

Predicates 2 and 5 overlap without being the same check. Predicate 5 catches a manifest edit inside
the pushed range even where the fingerprint round-trips. Predicate 2 catches a manifest that differs
from the recorded one for any other reason, including a record written on another node.

### Rollout

One commit. The rollback is restoring the unconditional `export GATE_FULL=1`, one line, no revert of
anything else. The first push after this lands finds no record and forces full, which is the correct
cold start rather than a special case.

### Files touched (estimate)

| file | change |
|---|---|
| `.githooks/pre-push` | the decision block, the lag default with its comment, the no-halt export |
| `.githooks/pre-push.test.sh` | one arm per predicate, the scoped-path arm, the no-halt arm |
| `AGENTS.md` | the gate-suite paragraph's safety-property sentence |
| `parallel-coding-governance.template.md` | its diff-scope and full-bar sentence |
| `tools/run-gates/run-gates.sh` | the header comment stating the same retired claim |
| `tools/gate-legs.json` | S10's one guard row |

### Alternatives rejected

- **Scope with no backstop at all.** Rejected: two live records depend on the backstop, and the
  residual risk is a wrong merge verdict rather than a late signal.
- **Keep forcing full on every push.** Rejected by owner decision on 2026-08-18, with the 873 s
  against 62 s measurement in hand.
- **Prove each guard complete, then scope freely.** The sound answer, and far larger than this
  build. Recorded as the follow-up that retires the residual risk.
- **Reuse a previous green keyed on the tree sha instead of scoping.** Sound where legs are pure,
  and `git rev-parse HEAD^{tree}` makes it a one-command key. But `tools/unattended/check-unattended.sh`
  calls `git ls-remote`, so its verdict is a function of the remote as well as of the tree. Reuse
  therefore belongs to `TOOL-aPacedTurnstile-5` behind a per-leg purity declaration, not here.

## 5. Production-readiness checklist

- security — the record is read from the git dir, already trusted by every other hook path; a
  hostile record can only force MORE work, because every parse failure forces full.
- perf / scale — five git commands, each O(1) or O(commits in range), all measured well under a
  second on this repo.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English strings in a shell hook, as everywhere else here.
- error / empty / loading states — the absent-record and unparseable-record paths ARE the empty
  states, both force full, and both carry arms.
- observability — S5 is the observability: the reason string is printed and recorded.
- risks (concurrency, data-loss, rollback hazards) — the residual risk is a too-narrow guard landing
  a wrong verdict inside the lag window. Rollback is one line.
- testing + left-shift gates — S8's arms, one per forcing predicate. The class left-shifts as the
  forcing table itself.
- migration / rollback — no migration. Cold start forces full, which is correct.
- user docs — S9, across all three carriers of the retired claim.

## 6. Acceptance criteria

- **AC1** — When a records-only commit is pushed to the default branch with a fresh full-green
  record present, `.githooks/pre-push` runs its gate without `GATE_FULL` set.
- **AC2** — When no run record exists, `bash .githooks/pre-push.test.sh` observes the hook invoking
  its gate with `GATE_FULL=1` and printing `no usable run record`.
- **AC3** — When the pushed diff touches `tools/gate-legs.json`, `bash .githooks/pre-push.test.sh`
  observes `GATE_FULL=1` and the reason `the leg manifest is in this diff`.
- **AC4** — When the recorded full-green sha is not an ancestor of the pushed tip,
  `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` AND the reason
  `the last full green is not an ancestor`. The reason string is part of the criterion because
  predicate 1 also yields `GATE_FULL=1`, so the flag alone cannot tell the arms apart, and each
  fixture's record is asserted to PARSE before the predicate under test is triggered.
- **AC5** — When more commits than `GATE_FULL_MAX_LAG` separate the recorded green from the tip,
  `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` AND the reason naming the commit count.
- **AC6** — When the record's manifest fingerprint disagrees with `git hash-object tools/gate-legs.json`,
  `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` AND the reason `the leg manifest changed`.
- **AC6b** — When the recorded tree fingerprint does not match a fresh fingerprint of the pushed tip,
  `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` and the reason
  `the record describes a different tree` — predicate 0, the join without which a green earned on a
  dirty tree silently resets the lag.
- **AC6c** — When `tools/push-main.sh` retries after reconciling with origin,
  `bash tools/push-main.test.sh` observes the retry gate running with `GATE_FULL=1`.
- **AC7** — When the retired claim is searched for after this lands, a WHITESPACE-INSENSITIVE search
  (the carriers hard-wrap the sentence across lines, so a line-anchored `grep` matches nothing today
  and would pass unchanged) finds it in none of the three carriers — `AGENTS.md`,
  `tools/run-gates/run-gates.sh` and `parallel-coding-governance.template.md` — AND a positive search
  finds the replacement sentence naming `GATE_FULL_MAX_LAG` in each. The negative alone is satisfied
  by any rewording, including one still false, and by a grep that never could have matched.
- **AC8** — When the hook runs, it exports the no-halt flag regardless of which branch its forcing
  table took, asserted in `.githooks/pre-push.test.sh` on both the scoped and the forced path — so a
  landing never stops reporting at the first red chunk.
- **AC9** — When `bash tools/run-gates/run-gates.test.sh` runs, the kit/dogfood parity leg's guard
  names `memory/guides/`, and a fixture touching only `memory/guides/BUILD-METHOD.md` causes that leg
  to RUN rather than skip — the hole `cKeyedLaunchpad` park 2 recorded, closed and armed.
- **AC10** — When `bash tools/check-testsuite-counts.sh` runs, `.githooks/pre-push.test.sh` reports
  an executed assertion count no lower than its recorded floor.

## 7. Gates

`bash .githooks/pre-push.test.sh` · `bash tools/push-main.test.sh` ·
`bash tools/run-gates/run-gates.test.sh` (the post-move path — this unit lands seventh) ·
`bash tools/check-testsuite-counts.sh` · `bash tools/check-playbook-parity.sh` ·
`bash tools/memory-tree/check-memory-hygiene.sh` · `python tools/memory-tree/check-arms.py --check` ·
and the full bar, `GATE_FULL=1 bash tools/run-gates.sh`.

## 8. Open questions

none — the forks below are RESOLVED. Every pick is the M3 ratification of the fork's own
recommendation; the reason each survived the veto order is recorded with it.

- **The shipped default for `GATE_FULL_MAX_LAG`.** Options are `1` (full on nearly every push, so
  almost no saving), `10`, `25`, or a time bound rather than a commit bound. Recommendation: `10`.
  This repo took 13 commits between `origin/main` and the current tip inside a single build, so `10`
  forces roughly one full bar per build rather than one per push, which is the granularity at which
  both parked records would still have been caught.
  RESOLVED (agent, 2026-08-18, delegated): `10`. This is the disposition the build README already
  records, together with the design pass's refused recommendation of `1` and the reason for
  refusing it: the owner's stated goal is to stop paying the full bar per landing, and `1` defers
  essentially all of that saving. The knob is one line and lowering it later needs no code.
- **Whether `tools/push-main.sh` should force full on a retry.** RESOLVED (agent, 2026-08-18,
  delegated): YES, and the first draft's answer was wrong. The lander retries by reconciling with
  origin, which produces a MERGE commit whose content no recorded green describes — the recorded
  green was earned on the pre-merge tip. Under the first draft's answer the retry re-ran the same
  decision, found a fresh ancestor green, and scoped: the merge commit that actually reaches the
  remote would have been the one commit never fully graded. Predicate 7 closes it.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-4 · 2026-08-18 · folded the blocker re-review: §2 described none of predicates 0, 6 or 7, so
  the scope under-described its own decision table; and predicate 0 is now stated as CALLING
  `TOOL-aPacedTurnstile-5`'s shipped fingerprint helper rather than computing its own digest, which
  would have failed toward FULL permanently and looked like caution.
- rev-3 · 2026-08-18 · folded the spec audit. Predicate 0 joins the record's tree fingerprint to the
  pushed tip, without which a full green earned on a dirty tree reset the lag counter (BLOCKER F5,
  F30). Predicate 7 forces full on a push-main retry, whose reconcile merge commit no recorded green
  describes — the first draft's §8 answer was wrong and is rewritten (F29). The lag becomes a source
  constant rather than the cited `GOV_DEFAULT_BRANCH` shape, which does not exist as described and
  would be fail-OPEN (F26). AC4 through AC6 gain their reason strings, because the flag alone cannot
  tell the predicates apart (F28). AC7 becomes whitespace-insensitive and covers all three carriers,
  having been a line-anchored grep that could never have matched a hard-wrapped sentence (F27, F42).
  S5's durable half gains a mechanism (F25); the gate list is repointed past `-1`'s move (F43).
- rev-2 · 2026-08-18 · folded the design-set reconciliation. The lag default moves into the hook
  because no sibling creates a conf a bash hook can read; the no-halt export is added, because
  `TOOL-aPacedTurnstile-3`'s halt fires when the full-run flag is unset and this unit makes the
  landing run frequently unset, which would have made a landing fail-fast; the retired safety claim
  is chased into the runner's own header comment, which ships to adopters; the one verified-open
  guard hole is closed here rather than left as a recorded residual; and AC7 gains its positive
  half, having been satisfiable by any rewording.
- rev-5 · 2026-08-18 · swept section 8 under the standing mandate: every fork RESOLVED in
  place per M3, and the section's first non-blank line made machine-legal so the classifier
  reads this unit as READY instead of FORKED.

## 10. Reuse audit

The seam this extends is `.githooks/pre-push`'s existing `GOV_GATE_CMD` indirection together with its
`export GATE_FULL=1` line, both already exercised by `.githooks/pre-push.test.sh` — the hook's test
already stubs the gate, so the forcing arms need no new harness. `tools/run-gates.sh`'s `changed()`
and its `GATE_FULL` bypass are consumed unchanged; this unit adds no scoping mechanism of its own.
The record it reads is `TOOL-aPacedTurnstile-5`'s, cited there rather than duplicated here.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL. The probe returned `TOOL-aTimedTurnstile-2` (the owner call this
unit executes), `cBriefedPilot-15` and the `cKeyedLaunchpad` park (both dependents on the property
this unit weakens), and `TOOL-aStandingWrit-4` (the fail-OPEN class the decision table's
fail-toward-FULL direction is written against).
