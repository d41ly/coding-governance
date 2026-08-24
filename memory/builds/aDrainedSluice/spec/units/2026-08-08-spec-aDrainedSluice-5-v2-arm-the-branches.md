# TOOL-aDrainedSluice-5 — V2: arm every pinned branch, or say why not

**Status:** CLOSED · rev-4 · 2026-08-08 · node a · Tier-2 · base 76fcd09b · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-08-review-TOOL-aBatchedTribunal-1-3.md](../../reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md) | diff-review | TOOL-aDrainedSluice-1 TOOL-aDrainedSluice-2 TOOL-aDrainedSluice-3 TOOL-aDrainedSluice-4 TOOL-aDrainedSluice-6 TOOL-aDrainedSluice-7 TOOL-aDrainedSluice-8 TOOL-aDrainedSluice-9 TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-8 |
| [2026-08-08-review-TOOL-aDrainedSluice-5-2.md](../../reviews/2026-08-08-review-TOOL-aDrainedSluice-5-2.md) | spec-audit | TOOL-aDrainedSluice-6 TOOL-aDrainedSluice-7 TOOL-aDrainedSluice-8 TOOL-aDrainedSluice-9 |

<!-- /gen:spec-records -->

## 1. Goal

The pin exists so an unarmed branch is visible, not so it can stay unarmed. Nine hygiene branches are
pinned before V1; V1 widens the population to the manifest-check gate and the pin becomes **25** rows
(16 + 9), which is the number this unit drains. Drive the pin to empty, or to rows that carry a
reason a reader accepts.

## 2. Scope (IN)

- **S1** — every branch in the pin gets a FIXTURE that actually trips it and an assertion naming that
  branch's OWN failure text. A fixture that does not trip the branch produces an arm that passes by
  finding nothing, which is the class this repo already catalogues.
- **S2** — the fixtures are BATCHED where batching works, which is the hygiene harness: `fail()` sets
  a status flag and never aborts AND nothing downstream of it short-circuits, so one scratch tree
  trips many branches in one invocation. Measured on THIS tree, not inherited: the gate is 3.5 s on
  the real repo and the whole self-test — seven gate invocations plus the git setup — is 25 s, so
  nine extra scratch-tree runs would roughly double a leg that runs on every commit. (The drafted
  "~8.8 s per invocation, ~95 s for eleven" was an upstream figure for an upstream tree, and both
  halves were wrong here: the invocation is cheaper and the population is 25, not eleven.)
- **S2b** — batching does NOT work for the manifest-check harness, and the draft assumed it did.
  `fail()` does not abort, but its CALLERS short-circuit: `BLOCK_OK` skips four whole checks once any
  check-2 branch fires, and check 3 is a three-way `if`/`elif` chain whose arms are mutually
  exclusive by construction. That harness gets several small fixtures instead, and the reason is
  recorded here so the next person does not helpfully merge them back together. Measured further:
  `SKIP_RANGE` makes a check-3 branch and check 5's full-mode branch mutually exclusive, and check
  5's two branches live in opposite invocation MODES (full vs `--staged`) — so the minimum for 16
  branches is ten invocations, not one. The harness is also not a scratch tree: it copies a template
  repo per scenario, ~0.95 s each over 40 scenarios (37.7 s measured), so five new scenarios cost
  ~5 s rather than the ~95 s the drafted argument feared.
- **S3** — arming happens after V1 and V3, because those two change the branch set: V1 widens the
  population to a second gate, and V3 touches check 5's message. V4 does NOT change it — review 1
  measured that `check-arms` keys on shell `fail` call sites while V4's finding is an awk `print`
  inside an already-armed branch — so the draft's ordering premise was wrong about one of its three
  dependencies and is corrected here rather than left as folklore.
- **S4** — a branch that genuinely cannot be armed from a fixture STAYS pinned and its row gains the
  reason, in a comment above it. The pin file's format gains nothing; comments are already ignored by
  its parser.
- **S5** — after arming, `ARMS_ARMED_FLOOR` is re-measured UP to the new armed count. A floor left at
  its old value would let every arm this unit writes be deleted again silently.
- **S6** — each new arm is checked against the harness BEFORE it is trusted: the fixture is run, the
  gate's real output is read, and the assertion is written against the text that actually appeared.
  Writing the assertion from the source and hoping is how six upstream probes reported success while
  exercising nothing.
- **S7** — the manifest-check harness gains whatever fixtures its own branches need, in its own file,
  in its own shape. It is a shipped kit file, so its test grows the same way the hygiene test does.
- **S8** — most of the manifest work is an ASSERTION-TEXT swap, not a fixture. Measured by
  instrumenting `fail()` and running the untouched suite: 11 of the 16 branches already fire in an
  existing scenario and assert only `check N FAILED`, which names the CHECK and not the BRANCH —
  precisely the distinction this meta-gate exists to make. Exactly five branches (check 2, ordinals
  2, 3, 4, 5 and 7) have no scenario at all, and three of those five co-fire on one fixture.
- **S9** — the one piece of mechanism this unit does add is named rather than smuggled: `run` takes a
  single pattern, and check 2's three missing-key branches are independent `||` statements that all
  fire on one invocation. A `runm` that asserts many signatures over ONE run is what keeps that from
  becoming three identical repo builds. Nothing else is added, and the `grep -q` in `run` becomes
  `grep -qF` because every signature in this gate carries braces, quotes, parentheses or an em-dash.

## 3. Non-goals (OUT)

- Changing any branch's message to make it easier to assert. If a message is hard to assert on, that
  is a signal about the message; V4 already reworded one for exactly that reason and did it as a
  visible edit, not as a convenience.
- Lowering a floor. Both floors are one-sided upward; this unit only raises the armed floor.
- Arming a branch by asserting a substring that another branch also emits. The signature is the
  branch's own longest literal run, and `check-arms` is the judge of whether an arm counts.

## 4. Design

### Data model

Unchanged from V1: a branch is `(gate, check, ordinal, line, signature)` and an arm is a positive,
non-comment assertion naming that signature. This unit adds fixtures and assertions; it adds no
mechanism.

### Inventory

The population is measured at the start of the unit, after V1/V3/V4. For each branch:

| Column | Meaning |
|---|---|
| gate · check · ordinal | the key |
| covering scenario | the EXISTING fixture that already trips it, where there is one |
| fixture | the tree state that trips it, where there is not |
| assertion | the text asserted, copied from the gate's real output |
| outcome | ARMED, or PINNED with a written reason |

Measured after V1/V3/V8, and this is the whole population:

| Gate | Branches | Already fired by a scenario | Needed a new fixture |
|---|---|---|---|
| `manifest-check.sh` | 16 | 11 (assertion-text swap only) | 5 — check 2 ordinals 2, 3, 4, 5, 7 |
| `check-memory-hygiene.sh` | 14 | 5 (armed before this unit) | 9 — checks 1, 2, 6, 8, 9, 10, 11 + two stale-line guards |

### Migration

The pin shrinks. Every row that leaves is a row whose branch gained an arm in the same commit.

### Rollout

One commit per harness — the hygiene test and the manifest-check test — so a revert is per-harness.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.test.sh`,
`skills/session-kickoff/manifest-check.test.sh`, `memory/project/unarmed-branches.txt`,
`.memory-tree.conf`.

### Alternatives rejected

- **Assert the exit code instead of the message.** Rejected: the scratch trees deliberately red many
  checks at once, so an exit code says nothing about WHICH branch fired. Upstream shipped six probes
  of exactly this shape that reported success while exercising nothing.
- **Delete the pin and let the floors carry it.** Rejected: a floor says how many, never which. The
  pin is what makes a specific gap nameable and drainable.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — S2's batching is the whole perf story; the arms add assertions, not invocations.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a fixture that fails to trip its branch shows up as a red arm,
  which is the correct and loud outcome.
- observability — every arm names its branch's own text, so a failing arm says which branch broke.
- risks — a fixture that trips a DIFFERENT branch than intended would arm the wrong one. S6's
  read-the-real-output rule is the guard, and `check-arms --report` shows exactly which branches
  moved from pinned to armed.
- testing + left-shift gates — this unit IS test work; its own verification is the report delta.
- migration / rollback — one commit per harness.
- user docs — none needed; the pin file's own header explains itself.

## 6. Acceptance criteria

- **AC1** — When the unit lands, `check-arms.py --report` shows every branch either ARMED or pinned
  with a written reason, and no pinned row lacks one.
- **AC2** — When each new fixture is added, running its harness shows the gate emitting that branch's
  own message, and the assertion quotes that message.
- **AC3** — When any new arm is deleted, its harness fails — proving the arm is load-bearing rather
  than decorative.
- **AC4** — When `ARMS_ARMED_FLOOR` is read, it equals the new armed count and the measurement is
  recorded.
- **AC5** — When the hygiene and manifest-check harnesses run, each prints its pass line last and
  each names its assertion count.
- **AC6** — When the full bar runs, it is green.
- **AC7** — When a green half exists for a branch, it is asserted too: a selector that matches
  nothing is silent for the wrong reason, and a red-only arm cannot tell the two apart.

## 7. Gates

`bash tools/run-gates.sh`; the `memory hygiene`, `memory-hygiene self-test`, `manifest-check
self-test`, `harness arms` and `check-arms selftest` legs all carry this unit.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — arm every branch, or accept a residue.** RESOLVED (owner, 2026-08-08): arm every branch
  that a fixture can reach, and leave a REASONED residue for any that a fixture cannot. The
  distinction is the point: "not yet written" and "cannot be written from here" look identical in a
  pin without a reason, and only one of them is acceptable.
- **Fork B — one commit or one per harness.** RESOLVED (owner, 2026-08-08): one per harness. They are
  different kits with different owners on a multi-node repo, and a revert should not span both.

## 9. Revision log

- rev-4 · 2026-08-08 · CLOSED. Landed: 30/30 branches armed, the pin emptied, `ARMS_FLOORS` raised to
  `16:16` and `14:14`. Folded the wave-2 verification's remaining two findings: S2's perf figures and
  population count were upstream numbers (re-measured here — 3.5 s gate, 25 s hygiene self-test,
  37.7 s manifest suite, 25 pinned rows), and §10's "no mechanism at all" was false once the
  manifest harness needed a multi-assert helper, so `runm` is declared in S9 instead of denied.
- rev-1 · 2026-08-08 · initial draft.
- rev-3 · 2026-08-08 · folded review 2's N17: the batching premise is false for the manifest-check
  harness, whose callers short-circuit. Its blocker N-equivalent — five signatures carrying shell
  source — was already fixed in V1, which is why it does not appear here.
- rev-2 · 2026-08-08 · folded review 1's M6 into S3: V4 does NOT change the branch set, because
  `check-arms` keys on shell `fail` call sites and V4's finding is an awk `print` inside a branch
  that is already armed. The ordering premise kept its V1 and V3 dependencies, which are real.

## 10. Reuse audit

This unit writes almost no mechanism, and the exception is declared rather than hidden. The hygiene
fixtures go into the scratch tree that harness already builds, in its existing batched shape, and use
its existing `hit`/`hitl`/`c5block` helpers — `cblock`/`chit`/`cnot` are `c5block` generalised to any
check number, because five checks print bare paths and an unattributed assertion is satisfied by the
wrong one. The manifest fixtures use the harness's existing `mkrepo`/`write_manifest`/`run` shape;
`runm` is the one addition (S9), and it exists because `run` asserts a single pattern while three
branches fire on one invocation. The judge is `check-arms.py`, unchanged from V1; the pin and the
floors are the existing ones. Everything else added is coverage, which is what the backlog row asked
for.
