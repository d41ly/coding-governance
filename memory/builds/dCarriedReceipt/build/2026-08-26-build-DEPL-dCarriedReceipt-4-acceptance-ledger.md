# Acceptance ledger — DEPL-dCarriedReceipt-4, `coverage_rows()` and `plan --coverage`

**Serves:** journal DEPL-dCarriedReceipt-4

Built on node `a` under session slug `aResumedRelay`. Node `a` reaches BOTH live adopter checkouts,
which node `d` did not — that is why AC2 and AC3 were measurable here at all, and it is the one fact
about this build that a later reader most needs and could not derive.

**Evidences:** DEPL-dCarriedReceipt-4
- AC1 — `python tools/govkit/govkit.py plan --coverage` — RED is HISTORICAL: `parse_args` refused
  `--coverage` as an unknown argument before this unit, and cannot be made to refuse it again
  without removing the flag. What survives it is an arm asserting both flags are named in `USAGE`,
  which is the carrier §5 promises gains them.
- AC2 — amended rev-6 — the criterion's `181` plan rows, `143` write rows and `gap 0` were
  measurements at the base sha and are struck from the assertion; the rev-6 §9 line logs it. The
  reason is the value-in-prose-beside-the-source-that-owns-it class one layer out: a count of what
  gov ships is not a property of this join, and pinning one makes the criterion red on every
  unrelated landing. **The reading of the day**, taken against `C:/projects/nicocares/main` with the
  full fifteen-kit `--kits` list, gov at the merge commit that opened this session: **gap 4 of 144
  write rows**, exit 0, `lexicon 2, memory-tree 2`. What the criterion now asserts was checked row
  by row on both sides: each of the four names a file gov tracks today and NicoCares does not —
  `tools/lexicon/SKILL.template.md`, `tools/lexicon/canon.py`,
  `tools/memory-tree/build-readme-slot-highwater.txt`, `tools/memory-tree/build-readme-slot-limits.txt`,
  each `git ls-files` present in gov and absent at its `scripts/` destination in the target. Two of
  them were added to gov the day before this session. So the first live run of this join found four
  real gaps, which is the calibration working rather than failing.
- AC3 — amended rev-6 — the `54` over `135` figure is struck for the same reason and kept as
  history; the STRUCTURAL pair it was carrying is what the criterion now asserts, and it holds
  exactly. Observed: the one surviving `push-main` gap row is `.githooks/pre-push.test.sh`, printed
  under `.githooks/` and NOT at the target root, and `.githooks/pre-push` is absent from the gap set
  because inCMS tracks it — verified directly with `git -C <incms> ls-files -- '.githooks/*'`. That
  is `-1`'s resolver fix seen from the coverage side, and it is the regression alarm this criterion
  exists to be. **The reading of the day:** gap 76 of 136 write rows, exit 0, over the fourteen kits
  inCMS declares.
  **How the target was reached, because it matters and the criterion now requires saying so.**
  inCMS carries no `.governance/deploy.toml` — the adopter-side build writes it and has not landed —
  so the measurement was taken against an INDEX-ONLY MIRROR built in the session scratchpad:
  `git clone --local --shared --no-checkout` plus `read-tree HEAD`, which gives `git ls-files` the
  real answer with no object copy and no file checkout. The `deploy.toml` in that mirror was
  reconstructed from inCMS's OWN `.governance/kits.json` — its declared prefix and its fourteen kit
  ids, all fourteen of which still resolve to gov registry entries — and never invented. **Nothing
  was written into `C:/projects/incms`.**
- AC4 — `tools/govkit/selftest.py` — `--emit-declines` prints one `[[decline]]` block per gap row
  with an empty `why`, the count equals the gap count, `git status --porcelain
  .governance/deploy.toml` is empty afterwards, and a target with no gaps emits none. A fourth arm
  holds the design decision that keeps §7's `BRANCH_PIN` promise true: `--emit-declines` alone
  IMPLIES `--coverage` rather than refusing without it, so this unit adds no refusal branch.
- AC5 — `tools/govkit/selftest.py` — the false-positive arm. A fixture declaring a `project-owned`
  rule and a `merged` rule whose destinations the target does not hold reports `gap 0`. Left-shifted
  over the whole `ROLE_KINDS` table rather than over the one role that exposed it: two further arms
  assert `write` is the only kind in that table meaning gov puts bytes there, and that the join's
  predicate is spelled against the KIND rather than against a role list somebody would have to keep
  in step.
- AC6 — `tools/govkit/selftest.py` — a fixture missing exactly one planned write reports exactly
  that `dest` and exits 0; with the same file present in the WORKTREE but not `git add`-ed it is
  still reported; once tracked it stops being a gap. The index is the answer, asserted in all three
  directions.

Three arms beyond the criteria, each for a scope item the criteria do not reach: S3 (a destination
still carrying an unresolved token is not a coverage row — a brace is not a path), S4 (the tally
counts ROWS, so two rules colliding on one destination are two triage items, which is what a
destination-keyed join hid at the live target), and the clean-reading liveness arm, without which
every gap arm could pass because the join reports everything.

## What the live readings say, beyond passing

Both are real findings about real repositories and neither is this unit's defect:

- **NicoCares is four files behind gov**, all four added in the last few days. It was the
  zero-reading calibration target, and it is no longer at zero — which is the join doing its job on
  its first run.
- **inCMS's 76 gap rows are not 76 absent files.** Two whole kits account for eighteen of them —
  `review-harness` at eleven and `pytest-parallel-guardrails` at seven — and inCMS's own
  `kits.json` maps `review-harness` under `.claude/workflows/`, not under its `scripts/` prefix.
  That is a REPATH the gov descriptor does not know about, which reads as absence here by design:
  §3 puts rename detection for coverage on the ratified OUT list, and `-5`'s `[[decline]]` contract
  is the thing built to express it. So the number is triageable rather than alarming, and `-5` is
  the unit that will shrink it.
