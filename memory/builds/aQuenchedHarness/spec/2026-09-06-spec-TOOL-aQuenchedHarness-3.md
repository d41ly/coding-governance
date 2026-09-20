# TOOL-aQuenchedHarness-3 — a self-test never reaches an adopter, as a leg or as a file

**Status:** CLOSED · rev-6 · 2026-09-07 · node a · Tier-2 · base faaea5f5 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-07-build-TOOL-aQuenchedHarness-3-acceptance-ledger-adopter-withholding.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-3-acceptance-ledger-adopter-withholding.md) | journal | — |
| [2026-09-06-prompt-TOOL-aQuenchedHarness-1.md](../prompts/2026-09-06-prompt-TOOL-aQuenchedHarness-1.md) | research | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-5 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 |
| [2026-09-07-review-TOOL-aQuenchedHarness-7-closing-diff-review.md](../reviews/2026-09-07-review-TOOL-aQuenchedHarness-7-closing-diff-review.md) | diff-review | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 |

<!-- /gen:spec-records -->

## 1. Goal

Stop shipping this repo's kit self-tests into adopter repositories, as bar legs or as files. The leg
half is far smaller than every prior revision of this spec claimed, and the file half is untouched by
anything: `tools/run-gates/kit.toml` and its siblings claim `include = "**"`, so every `*.test.sh`,
`test_*.py` and `selftest.py` lands in an adopter tree on install.

## 2. Scope (IN)

- **S1** — each kit descriptor gains a `[[files]]` rule claiming its own self-test paths with
  `role = "project-owned"`, so the deployer withholds them. `tools/run-gates/kit.toml` already does
  exactly this for `run-gates.gov.test.sh`, with its reason beside it; this extends that rule to the
  rest and gives each one a reason of its own.
- **S2** — THE LEG DECLARATION MOVES OUT OF THE DESCRIPTOR. Each withheld suite's `[[gate_leg]]`
  block leaves its `kit.toml` and becomes an `[[exempt_leg]]` row in `tools/govkit/registry.toml`
  with its reason. 21 rows move; the leg stays on GOV's bar and is held there exactly as before.
  Rev-4 said the leg half "needs no code" because `silenced_legs` would drop it. Measured: it does
  drop it — and it reports each drop with `r.fail`, because that function exists for gov's own
  DEFECT (a descriptor naming a file gov forgot to ship). Every adopter apply then exited 1 with one
  problem per withheld suite. The precedent for the right shape was already written beside
  `run-gates.gov.test.sh` in `tools/run-gates/kit.toml`: "a descriptor row naming a leg the target's
  manifest cannot carry is what reds the deployer's selfcheck."
- **S2b** — `silenced_legs` stays exactly as it is. It is the backstop for the accidental case and
  this unit must not weaken it into accepting a deliberate one; the fix is to stop creating the
  condition, not to stop reporting it.
- **S3** — a gate leg asserting the property over a freshly emitted fixture target, in BOTH
  directions: no emitted leg's argv names a self-test path, AND the emitted leg count is strictly
  less than the descriptor row count, so a rule that withholds nothing cannot report clean.
- **S4** — `tools/run-gates/run-gates.sh` is NOT touched, and neither is `tools/govkit/govkit.py`.
  The local hold predicate, the set of legs the bar holds, and `GATE_SELFTESTS` are exactly as today.
- **S5** — arms staging: a descriptor whose self-test file is claimed `project-owned`, asserting the
  file is absent from the target and its leg is absent from the emitted manifest and NAMED in the
  report; and a descriptor where the claim is removed, asserting both come back.

## 3. Non-goals (OUT)

- Not adding `chunk` to the descriptor schema, and no longer needing to. `TOOL-aScouredKit-27` scopes
  that as a five-declaration act; S2 removes the reason to attempt it.
- Not withholding the three `subject = repo` test files whose legs an adopter SHOULD run —
  `kit-dogfood-parity.test.sh`, `marker-contract.test.sh` and `check-protocol-parity.test.sh`. Their
  legs are `subject = repo, chunk = declarations`, they are graded on the ADOPTER's tree, and S1's
  rules must not claim them. This is the disposition, decided by enumeration.
- Not changing which legs run in THIS repo. S4 states it and AC5 measures it as an EQUALITY.
- Not removing an adopter's ability to obtain the withheld suites. They are in the public repository
  and each `project-owned` rule records that.
- Not the on-demand runner, which is `TOOL-aQuenchedHarness-4`.

## 4. Design

### What is actually true at HEAD, enumerated

Every prior revision of this spec described this population and got it wrong. Measured:

| fact | count |
|---|---|
| `[[gate_leg]]` rows across `tools/*/kit.toml` | 52 |
| of those, held in gov by `subject == kit OR chunk == selftests` | 27 |
| held via `subject == kit`, which the apply DOES emit, so an adopter's runner holds them too | 26 |
| held via `chunk == selftests` alone, so the hold does NOT travel | 1 |

The one is `run-gates canary`. `subject` already travels — `_cmd_apply` emits it under
`check_target_reads_subject`, with a comment naming this exact defect as the reason — so 26 of the 27
are already held on an adopter's bar today.

**`TOOL-aScouredKit-27` is therefore STALE and this unit says so rather than inheriting it.** That row
names three legs reaching an adopter unheld: `push-main self-test`, `pre-push self-test` and
`run-gates canary`. The first two are `subject = repo, chunk = selftests` in gov but appear in NO
descriptor `[[gate_leg]]` row, so they reach no adopter manifest at all. Only the third is live.

### The mechanism, which is a declaration and not code

`silenced_legs` asks of every leg's argv whether the target holds the path it names, and
`_cmd_apply` drops and REPORTS the ones it does not. So withholding a file withholds its leg, and the
single leaking leg closes as a side effect of the file rule rather than through a predicate anybody
has to keep in step with `run-gates.sh`. One mechanism, already tested, already documented.

### Inventory

- One `[[files]]` rule per kit that ships self-tests, `role = "project-owned"`, each carrying its own
  reason line.
- 21 `[[exempt_leg]]` rows in `tools/govkit/registry.toml`, one per withheld suite, each naming the
  file its kit withholds and why.
- `no self-test reaches an adopter` — the new gate leg's name in `tools/gate-legs.json`.

### Files touched (estimate)

Every `tools/*/kit.toml` that ships a self-test (a `project-owned` files rule added, its
`[[gate_leg]]` rows removed) · `tools/govkit/registry.toml` (21 `[[exempt_leg]]` rows) ·
`tools/govkit/selftest.py` · `WIRE-INTO-PROJECT.md`. **No change to `tools/govkit/govkit.py`.**

### Alternatives rejected

**A filename-derived predicate** (rev-1) — measured to select 53 of 94 legs and hold four repository
checks off every bar, one of them the codebase-map coverage gate the charter forbids exempting.

**Reusing `selfcheck`'s manifest maps from the apply path** (rev-2) — they are locals of another verb
and the apply path never opens the manifest.

**A new shared manifest reader in the apply path** (rev-3) — correct as an implementation and
UNNECESSARY as a design: S2's existing machinery closes the same gap with no new code, and the
smaller change is the one that cannot drift from `run-gates.sh`.

## 5. Production-readiness checklist

- security — an adopter receiving fewer executable files and fewer legs is a narrowing. No new path
  executes anything new, and no deployer code changes.
- perf / scale — none: a `[[files]]` rule is read where the others already are.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a withheld leg is REPORTED by the existing `_silenced_found` path,
  named rather than silently absent; a rule claiming a path no kit holds is a descriptor defect
  `govkit selfcheck` already grades.
- observability — the apply's existing silenced-leg report, which now names the withheld self-tests.
- risks — OVER-REACH is the hazard: a rule that claims one of §3's three `subject = repo` test files
  would silence a leg an adopter needs. AC4 asserts those three files are still present in a fixture
  target, which is the direction that catches it.
- testing + left-shift gates — S5's arms, each observed RED before landing, plus S3's both-direction
  leg.
- migration / rollback — removing a `[[files]]` rule restores today's install. Files already on an
  adopter's disk are not deleted by an apply.
- user docs — `WIRE-INTO-PROJECT.md` gains one sentence on what adopters no longer receive and where
  the withheld suites live.

## 6. Acceptance criteria

- **AC1** — When `govkit` applies to a fixture target, no `*.test.sh`, `test_*.py` or `selftest.py`
  claimed `project-owned` is present in the target.
- **AC2** — When that same `govkit apply` runs, the emitted manifest carries no leg whose argv names
  one of those withheld paths, and each such leg is NAMED in the `silenced_legs` report rather than
  silently absent.
- **AC3** — When the emitted leg count is compared with the `[[gate_leg]]` row count across
  `tools/*/kit.toml`, it is strictly smaller, so a set of rules that withholds nothing cannot report
  clean.
- **AC4** — When a fixture target is inspected, `kit-dogfood-parity.test.sh`,
  `marker-contract.test.sh` and `check-protocol-parity.test.sh` ARE present and their legs ARE
  emitted — the over-reach direction.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs without `GATE_SELFTESTS`, the set of legs it
  holds is EQUAL to today's set, compared name-for-name against a set captured before the change.
- **AC6** — When a `project-owned` rule is removed from one descriptor, that kit's self-test file and
  its leg both return to the fixture target — the guard's own failing case, observed before landing.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the new `no self-test reaches an adopter` leg ·
`govkit selfcheck`, which carries no guard and runs on every bar · `govkit acceptance matrix` and
`govkit refusal join`, which run when their `tools/govkit/` guard fires · `kit version markers` and
the descriptor-shape legs, which grade every `kit.toml` this unit edits ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for `govkit selftest` at the Definition of Done.

## 8. Open questions

- **F1 — the owner's own either/or.** RESOLVED (agent, 2026-09-06, delegated): take the FIRST clause,
  and note that the SECOND is very nearly true already. 26 of the 27 held legs are held on an
  adopter's bar today because `subject` travels; withholding the files closes the twenty-seventh and
  satisfies the first clause at the same time, with one mechanism.
- **F2 — how is a file withheld?** RESOLVED (agent, 2026-09-06, delegated): `role = "project-owned"`
  on a `[[files]]` rule, the marker `tools/run-gates/kit.toml` already uses for
  `run-gates.gov.test.sh`.
- **F3 — do the three shipping `subject = repo` test files stay?** RESOLVED (agent, 2026-09-06,
  delegated): yes, enumerated in §3. Their legs are graded on the adopter's own tree.
- **F4 — is `TOOL-aScouredKit-27` closed by this unit?** RESOLVED (agent, 2026-09-06, delegated):
  partly, and the wrap-up says which part. One of its three named legs is live and this unit closes
  it; the other two reach no adopter manifest, so that half of the row is stale and is corrected in
  place rather than silently inherited.

## 9. Revision log

- rev-6 · 2026-09-07 · CLOSED. Every kit descriptor withholds its own self-tests with a `project-owned` rule and each withheld leg carries an `[[exempt_leg]]` row, so `govkit selfcheck` is green and an adopter apply no longer exits 1 with one silenced-leg problem per suite. Ten arms green. The two suites this build added later, `run-selftests.test.sh` and `extract-arms.test.sh`, were declared the same way on arrival, which is the ratchet working rather than a follow-up.

- rev-1 · 2026-09-06 · initial draft.
- rev-2 · 2026-09-06 · folded spec-audit round 1: the filename predicate removed, the shared-reader
  claim withdrawn, the files stopped shipping, §7's guard claim corrected.
- rev-3 · 2026-09-06 · folded spec-audit round 2: the apply path shown never to open the manifest, the
  `project-owned` marker adopted, the two halves joined, the population stated as 52/27.
- rev-6 · 2026-09-07 · VERIFIED. All 10 arms pass in `tools/govkit/selftest.py`, measured on a FROZEN
  CLONE of this branch: 1124 ok, 2 failed — the identical 2 that fail at the pre-session baseline
  `274aa39b`, filed as `TOOL-aQuenchedHarness-9`. This unit adds ten arms and no failures.
  The first run of that suite reported 28 failures and none of them was real: it ran against the live
  worktree while this session committed four times, and the suite pins gov's vintage at module import
  while `_cmd_apply` stamps each fixture receipt from live HEAD. Recorded as
  `memory/gotchas/suite-invalidated-by-a-commit-under-it.md`, because it cost two wrong attributions
  before anyone read the refusal message.
- rev-5 · 2026-09-06 · BUILT, and building it found what enumeration had not. Withholding the FILE
  does silence the LEG — `silenced_legs` drops it exactly as rev-4 said — but that function reports
  each drop with `r.fail`, because it exists for gov's own defect and not for a deliberate act. Every
  adopter apply exited 1 with one problem per withheld suite. S2 now moves the 21 declarations to
  `[[exempt_leg]]` rows, which is the shape `tools/run-gates/kit.toml` already documents beside
  `run-gates.gov.test.sh`, and S2b records that `silenced_legs` itself must NOT be weakened to accept
  the deliberate case. Observed armed / broken / restored: with the rule the test file and its leg
  are absent and the apply exits 0; with the rule removed the file comes back. `run-gates canary`,
  the one leg §4 measured as actually leaking, is among the 21.
- rev-4 · 2026-09-06 · ENUMERATED before coding, per M2's "to diverge, change the spec first", and the
  unit collapsed. Of the 27 held descriptor rows, 26 are held via `subject`, which the apply already
  emits — so exactly ONE leg leaks, `run-gates canary`. And `silenced_legs` already drops a leg whose
  argv names a path the target lacks, so withholding the FILES withholds the legs with no deployer
  code at all. Rev-3's shared manifest helper is correct and unnecessary; it is now a rejected
  alternative. `TOOL-aScouredKit-27` is recorded as two-thirds stale rather than inherited.

## 10. Reuse audit

The seam is the `[[files]]` role vocabulary the tree already uses — `role = "project-owned"` in
`tools/run-gates/kit.toml`, withholding `run-gates.gov.test.sh` today with its reason beside it — and
`silenced_legs` in `tools/govkit/govkit.py`, whose docstring states that it exists to stop gov handing
an adopter a leg naming a file gov never ships. Those two together are the whole unit; the code was
already written by `DEPL-dCarriedReceipt-6` and this unit supplies the declarations that make it fire.
`tools/codebase-map/reuse_lookup.py` returned `registry.toml` [govkit] as the affordance seam. The
prior record `TOOL-aScouredKit-27` was read in full and is corrected in §4 rather than cited as
current.

Recall terms used: `govkit apply emit descriptor gate_leg files role project-owned adopter manifest
subject chunk hold withhold`
