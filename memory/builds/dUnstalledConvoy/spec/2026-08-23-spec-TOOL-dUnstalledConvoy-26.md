# TOOL-dUnstalledConvoy-26 — a gate leg declares whose subject it is, and a kit's own self-tests become owner-adjustable

**Status:** CLOSED · rev-3 · 2026-08-24 · node d · Tier-2 · base b164a296 · streams tooling

## 1. Goal

A kit's self-tests read THE KIT: they stage a break into a copy of a checker and assert the checker
still catches it. They have a job when the kit's source changes and none at all in a repo that
copy-installs the kit and never edits it. Today they are ordinary bar legs, so every adopter runs them
on every full gate.

`f5f4732a` fixed this for one kit by DELETING seven legs, and its commit message drew the distinction
this unit generalises: the RECORD AND WIRING checks read the REPOSITORY and go stale with nobody
editing the kit, while the SELF-TESTS read the kit. rev-1 tried to name the second group by counting
`.test.sh` legs and got the population wrong twice over. This revision makes the distinction DECLARED.

## 2. Scope (IN)

- **S1 — every `[[gate_leg]]` declares `subject`, one of `kit` or `repo`.** A `kit`-subject leg tests
  the kit's own source; a `repo`-subject leg reads the repository it is installed in. Only `kit`
  legs become on-demand. This is the membership criterion rev-1 never stated, and it is the owner's
  own vocabulary from `f5f4732a` rather than a new one.
- **S1b — the population is DERIVED the way govkit derives it**, through `read_descriptors`, which
  loads `tools/*/kit.toml` AND `tools/govkit/entries/*.kit.toml`. rev-1 globbed the first only and
  missed ten legs; that is `two-answers-to-one-question` with the consumer as the other answer. No
  count of this population appears anywhere in this spec, because a number in prose beside a derived
  set is wrong on the next commit.
- **S2 — `run-gates` skips a `kit`-subject leg unless asked**, and `GATE_FULL=1` does NOT ask.
  `changed()` returns 0 the moment `GATE_FULL` is set, so the `guard = ["{kit}/"]` these legs carry is
  bypassed at exactly the push boundary an adopter feels.
- **S3 — the ask is `GATE_SELFTESTS=1`** and nothing else unlocks them.
- **S4 — the skip has its OWN verb and its OWN counter.** NOT `skips`, and not the `GATE skip …
  (unchanged vs <branch>)` line: that tail would be a lie — the leg is not unchanged, it is out of
  subject — and `skips` is load-bearing elsewhere (S5). The verb is new, and `profile_bar.py`'s closed
  verb set learns it, or the row is silently dropped from the profile summary.
- **S5 — the `gate-full-green` stamp keeps its meaning.** `[ "$skips" = 0 ]` is one of its five
  preconditions, so an on-demand skip counted as a skip means the stamp is never written again — and
  `.githooks/pre-push` then forces `GATE_FULL=1` on every push forever, with the lag bound
  permanently unreachable. Counting it separately is what keeps the stamp writable; **and the stamp
  RECORDS the switch state**, so a record named `gate-full-green` can never certify a partial run
  without saying it was partial.
- **S6 — the wire format gains the field, and `chunk` moves with it.** `chunk` is the LAST field of
  the reader's `\x1e`-separated row, so a sixth field appended after it is parsed as chunk. rev-1's
  §3 claimed `chunk` was untouched; it is touched by construction.
- **S7 — the decision sits in the GUARD PRE-PASS, not the dispatch loop.** A skip inside the dispatch
  loop with no result sentinel reds the bar with a "(no result)" row per skipped leg, because the
  reporting pass reads a result the loop never wrote.
- **S8 — `gate-legs.json` carries `subject` on every leg**, and govkit's both-directions cross-check
  learns the field so a descriptor and the manifest cannot disagree about it. The eight legs the
  descriptors EXEMPT are reachable by the exemption path only, so the check must read them there or
  it silently covers less than it claims.
- **S9 — govkit EMITS `subject` into a target's manifest.** Nothing in rev-1's scope did this, and
  `govkit.py`'s emission drops every field but name, argv and guard — so without this item the flag
  never reaches an adopter and the whole unit stops at this repo's edge.
- **S10 — the adopter is told how to run them**, once at adoption and on demand after, in govkit's
  install summary.
- **S11 — every change lands with its arm, and every arm that can fail is observed failing first.**

## 3. Non-goals (OUT)

- **Deleting or restoring any self-test.** The unattended kit's seven stay deleted; that was an owner
  ruling on that kit.
- **Changing what any self-test asserts.** This moves WHEN they run.
- **A per-kit or per-leg opt-out matrix.** One switch, repo-wide. A matrix is a surface nobody audits
  and its failure mode is a kit silently exempt from its own tests.
- **Making `GATE_FULL` unlock them.** `GATE_FULL` means "ignore every guard"; conflating it with
  "run the kit's own tests" leaves no way to ask for a complete bar without them.
- **Re-subjecting the repo-subject legs.** `kit/dogfood doc parity`, `review-protocol parity`,
  `marker contracts` and `run-gates canary` read the REPOSITORY — the canary holds the manifest
  key-set pin and the guard-liveness refusal — and they stay on the bar under `subject = "repo"`.
  CORRECTED by `TOOL-dUnstalledConvoy-30` (2026-08-24): that list read as exhaustive and was not.
  Four more legs are `repo` — `pre-push self-test`, `branch-guard self-test`, `push-main self-test`
  and `run-gates gov canary` — because a failure of any of them means this repository has a broken
  push or commit boundary, which cannot wait for somebody to remember a variable. This spec's §4
  criterion asked what a leg TESTS, and against `push-main.kit.toml` that wording puts all four on
  the held side; `-30` replaces it with what a leg FAILURE MEANS.

## 4. Design

The whole unit turns on S1. rev-1 tried to name a population by pattern and was wrong twice: it
globbed one of two descriptor roots, and it would have swept in four legs whose subject is the
repository. A declared field is checkable in both directions, survives a rename, and says which
answer is meant at the point where somebody has to choose.

S5 is the finding rev-1 missed entirely and it is the reason `§5 — security: none` was backwards. The
stamp is a five-way conjunction including `skips = 0`; a new skip that lands in that counter does not
weaken the bar quietly, it silences the stamp and pins `pre-push` into forcing a full run forever.
Both readings are bad and they are bad in opposite directions, which is why the switch state goes INTO
the stamp: a green that means "everything except the kit's own tests" has to say so where the push
boundary reads it.

S7 and S4 are one lesson twice. The dispatch loop writes a result per index and the reporting pass
reads one; skipping inside the loop leaves a hole the reporter reports. And the existing skip verb
carries a REASON in its text — `unchanged vs main` — which is false for this skip and would be read by
a human as a guard outcome.

What this does NOT buy: it does not verify a kit's self-tests still pass in an adopter's repo. It
moves them off the automatic bar; running them is the owner's choice and reading the result is the
owner's job. A green adopter bar after this says nothing about the kit's own health, and S10's text
says so where an adopter sees it.

## 5. Production-readiness checklist

- **security** — this changes the push boundary's behaviour, which is the opposite of rev-1's claim.
  S5 is the whole of the answer: the stamp stays writable and records what it covered.
- **perf/scale** — an adopter's full gate loses the kit-subject legs. This repo's own bar is unchanged
  when the switch is set and loses them when it is not.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — a manifest whose every leg is `kit`-subject, with the switch off,
  must refuse rather than report green. The observable is a RUN OUTCOME, so the arm drives the runner
  over such a manifest rather than asserting a predicate over the manifest alone.
- **observability** — S4's verb and S5's stamp field are the observability, and both are in scope.
- **testing/gates** — `run-gates`' own self-tests, govkit's selftest and matrix, plus the full bar
  invoked as `GATE_FULL=1 GATE_SELFTESTS=1`, which is what the Definition of Done needs. rev-1 named
  `GATE_FULL=1` alone while also specifying that it does not unlock these legs, so its own DoD
  invocation skipped every leg its acceptance criteria are observed by.
- **migration/rollback** — an adopter wanting today's behaviour sets `GATE_SELFTESTS=1`. No code
  change, no re-deploy. **`govkit apply` refuses an upgrade re-apply across the green→skipped
  transition**, so the migration path for an already-installed target is named in S10 rather than
  discovered.
- **help/ docs** — govkit's install summary, `tools/run-gates/README.md`, and `AGENTS.md`'s merge-bar
  section, which describes guards without saying `GATE_FULL` overrides them.

## 6. Acceptance criteria

- **AC1** — a `kit`-subject leg does not run on a default bar AND does not run under `GATE_FULL=1`,
  observed in `tools/run-gates/run-gates.test.sh`.
- **AC2** — the same leg RUNS under `GATE_SELFTESTS=1`, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC3** — a skipped `kit` leg is reported with the NEW verb, its own counter, and NOT the
  `unchanged vs` text, observed in `tools/run-gates/run-gates.test.sh`.
- **AC4** — `profile_bar.py` renders that verb rather than dropping the row, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC5** — a full green run with the switch OFF still writes `gate-full-green`, and the stamp records
  the switch state; with the switch ON the stamp records that too, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC6** — `.githooks/pre-push` does not force a full run on the strength of a stamp written with the
  switch off, observed in `tools/run-gates/run-gates.test.sh`.
- **AC7** — every leg in `tools/gate-legs.json` carries `subject`, and every descriptor leg does too,
  with the population read through govkit's own descriptor loader rather than a glob, observed in
  `tools/govkit/selftest.py`.
- **AC8** — a descriptor and the manifest disagreeing about `subject` is a refusal in both directions,
  and the check reaches the EXEMPTED legs, observed in `tools/govkit/selftest.py`.
- **AC9** — a target installed by govkit receives `subject` on its emitted legs, observed in
  `tools/govkit/matrix.py`.
- **AC10** — a manifest of only `kit` legs with the switch off REFUSES when the runner is driven over
  it, observed in `tools/run-gates/run-gates.test.sh`.
- **AC11** — govkit's install summary names how to run them once and on demand, observed in
  `tools/govkit/selftest.py`.
- **AC12** — every arm that can fail was observed failing against the pre-fix code, observed in
  `2026-08-24-build-TOOL-dUnstalledConvoy-26-1-red-first.md`.
- **AC13** — the full bar is green under `GATE_FULL=1 GATE_SELFTESTS=1`, observed by
  `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. Both variables, because
`GATE_FULL` alone skips every leg this unit's acceptance criteria are observed by.

## 8. Open questions

- **F1 — one repo-wide switch, or per-kit?** RESOLVED (agent, 2026-08-24): one. A matrix is a surface
  nobody audits and its failure mode is a kit silently exempt from its own tests.
- **F2 — should `GATE_FULL` unlock them?** RESOLVED (agent, 2026-08-24, delegated): no. rev-2 argued
  this was safe because the stamp records the switch — and round 2 established the stamp's field is
  INERT, since `.githooks/pre-push` parses only sha, fingerprint and manifest_blob. The safety
  argument therefore belongs to `TOOL-dUnstalledConvoy-27`, which makes the hook read it. Until that
  lands, this resolution has no support and this unit must not be closed ahead of it.
- **F3 — which legs are `kit` and which are `repo`?** RESOLVED (agent, 2026-08-24, delegated): by S1's
  criterion rather than a list. Round 2 showed the criterion read literally puts gov's push- and
  commit-boundary self-tests on the on-demand side, which is wrong; that assignment is
  `TOOL-dUnstalledConvoy-30`.
- **F4 — where does THIS repo set the switch?** RESOLVED (agent, 2026-08-24, delegated): NOT in
  `.githooks/pre-push`, which rev-2 chose and which govkit ships verbatim as engine payload to every
  push-main adopter — turning the switch on for exactly the adopters this unit exists to spare. Where
  it goes instead is `TOOL-dUnstalledConvoy-28`.

## 9. Revision log

- rev-3 · 2026-08-24 · round 2 returned BLOCKED at six blockers against round 1's three, so the
  loop was NON-CONVERGENT and the standing blockers were promoted to units. Three of this
  spec's own resolutions were falsified by that audit and now DELEGATE to the units that
  carry them: F2 to -27, F3 to -30, F4 to -28. The marks also take the house form the
  classifier reads, which rev-2's did not — it read FORKED on a spec whose forks were all
  answered.
- rev-2 · 2026-08-24 · spec audit returned BLOCKED with three blockers, all reproduced at base before
  folding. The `gate-full-green` stamp conjoins `skips = 0`, so rev-1's skip would have silenced it
  and pinned pre-push into forcing a full run forever — unmentioned in rev-1 and the reason its
  "security — none" was backwards. The population was derived from one of govkit's two descriptor
  roots and missed ten legs. And rev-1's own DoD invocation, `GATE_FULL=1`, skips every leg its ACs
  are observed by. The membership criterion is now a declared `subject` field rather than a pattern,
  which also keeps four repo-subject legs on the bar that rev-1 would have swept off.
- rev-1 · 2026-08-23 · initial draft. Written against the runner's wire format and `changed()` guard,
  but with the population globbed rather than read the way its consumer reads it.

## 10. Reuse audit

The runner's per-leg wire format already carries optional fields and this adds one in the same shape.
`[[gate_leg]]` already carries `guard` and `red_after_land`. The descriptor↔manifest cross-check
already runs in both directions and already refuses a stale exemption; S8 extends it. `subject` reuses
the vocabulary `f5f4732a` established rather than coining a second one. No new file, no new kit, no
new script.
