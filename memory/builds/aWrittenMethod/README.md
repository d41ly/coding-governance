---
slug: aWrittenMethod
node: a
opened: 2026-08-11
streams: tooling+playbook+kickoff
roster: TOOL
ids: TOOL-aWrittenMethod-1
---

# aWrittenMethod — the instruction layer: the build method, written down

Node `a` · opened 2026-08-11 · streams tooling+playbook+kickoff.

The unattended-run kit supervises a build but does not instruct one. `--preflight` asserts a mandate,
pins a BASE, sets phase RUNNING and returns. Between RUNNING and `--close` the driver does nothing:
no loop, no dispatch, no prompt. The build method — how to spec, how to review, how to build — is
supplied by the owner pasting prose into chat on every run, which is exactly the state
`aUnmannedHelm` found the mandate in before it became a kit.

This build turns that prose into a durable instruction layer.

This README is the **master overview and the owner decision menu**, per `memory/TEMPLATE-SPEC.md`.

## Start here

**State.** Unit 1 CLOSED and landed at `7f614a1`. Five further units are OPEN — the declines unit 1
recorded, now taken up. All five were DECLARED at BASE as backlog rows before this run named them, so
per the method's M2 they are MISSING (no spec carries the id), not un-declared.

## Units

The roster. This table is the roster, not the `ids:` key — M2 says so and this build is why.

| Unit | Tier | Mechanism | State |
|---|---|---|---|
| `TOOL-aWrittenMethod-1` | 2 | the build method, rendered and delivered | CLOSED, landed `7f614a1` |
| `TOOL-aWrittenMethod-2` | 2 | the mandate BASE the run cannot steer | OPEN |
| `TOOL-aWrittenMethod-3` | 1 | the method's displacement, at 247 of 250 lines | OPEN |
| `TOOL-aWrittenMethod-4` | 2 | a gate for the sixth carrier | OPEN |
| `TOOL-aWrittenMethod-5` | 1 | the method in the manifest's watch set | OPEN |
| `TOOL-aWrittenMethod-6` | 2 | escaping conf values before substitution | OPEN |

**Unit 2 is the blocker and leads.** It is the unapplied half of `D3` from
`../aUnmannedHelm/reviews/2026-08-10-review-aUnmannedHelm-2.md`: fixes 1 and 2 landed with that
build, fixes 3 and 4 did not, and the hole they leave was reproduced end to end during unit 1.

## State of this pass

| Unit | State |
|---|---|
| `TOOL-aWrittenMethod-2` | **BUILT** on branch, unmerged (`5d1faf9`). rev-3, INPROGRESS |
| `-6` `-3` `-4` `-5` | SPECCED rev-2, forks resolved, NOT built |

Landing order `2 → 6 → 3 → 4 → 5` — not parallel-safe. Unit 2 is done, and its two build-time
defects are recorded in its §9: a global set inside `$( )` never reached the caller because command
substitution runs in a subshell, and one refusal branch was unreachable because an earlier call
already returns on the same failure. The first broke every preflight until it was found; the second
was deleted rather than left as decoration.

**PARKED — units 6, 3, 4, 5.** *The question:* build the remaining four, then the closing diff
review, the bar, and landing. *The options seen:* push on with what context remains; park after the
blocker. *The reason:* unit 2 alone consumed the pass — two build-time defects, a fixture repair the
audit had predicted, six new armed branches and an arms-floor ratchet. Unit 6 rewrites six
substitution sites under a hostile-value fixture and unit 4 adds two gate legs; neither is a thing to
start on the budget left. Unit 2 is independently valuable and self-contained: it is the blocker, its
write set is disjoint from the other four, and nothing pending depends on it.

**Next action:** build unit 6 per its rev-2 spec, then 3, 4, 5. Keepalive NOT reaped.

## The two passes, and why there are two

The first pass was aimed at the wrong target and is kept as a record rather than deleted, because its
method was sound and three of its findings are independently real.

| Pass | Aimed at | Verdict |
|---|---|---|
| 1 — `build/2026-08-11-build-aWrittenMethod-1-enforcement-pass.md` | proving a run did not tamper with its own instructions | REJECTED for scope. It designed an enforcement layer and labelled it an instruction layer |
| 2 | the method itself: how to spec, how to review, how to build, and how that text reaches the agent | converged into the spec below |

The scope error in pass 1 was introduced by its own briefing, not discovered in its output. The
briefing named "a run that writes its own SPEC is the analogue of a run that writes its own MANDATE"
as the central tension and scored candidates on checkability and self-authorization safety. Every
candidate and both judges optimized that faithfully. The output graded the owner's sixteen rules as
six machine-checked, six witnessed, three agent-attested and three unenforceable — a grading rubric,
where a procedure had been asked for.

The distinction the two passes separate, and which the kit currently conflates:

| Layer | Scope | Answers |
|---|---|---|
| Mandate | per-run | may this run merge and push |
| Specs | per-build | what to build |
| **Method** | **generic, stable across builds** | **how to spec, review, build, recall, parallelize, reground, land** |

The method is mostly generic. That is why it does not need per-run provenance, and it is the reason
pass 1's apparatus was answering a question nobody asked.

## What survives pass 1

Three findings, each verified against source rather than inherited from the pass:

- **The pinned BASE is forgeable.** `default_branch()` returns `$GOV_DEFAULT_BRANCH` verbatim, and
  `git update-ref refs/remotes/origin/<name> <sha>` writes a remote-tracking ref with no push and no
  network. Reproduced end to end in a scratch repo: BASE resolves to a commit the run authored while
  staying unequal to HEAD, so the degenerate guard does not fire, and `check_mandate` compares
  run-authored bytes against run-authored bytes. The driver's own comment asserts the opposite
  defense. This was already filed as D3/BLOCKER in
  `../aUnmannedHelm/reviews/2026-08-10-review-aUnmannedHelm-2.md` and no backlog row tracked it.
  Now `TOOL-aWrittenMethod-2`, and it is **not** in this build's scope.
- **Four project declarations are delivery, not enforcement**, and carry into pass 2: the recall
  entrypoint, the reuse entrypoint, the review harness, and the keepalive interval.
- **Measured corpus facts** that constrain any design here: `## Verdict` appears in 8 of 32 review
  records and no verdict field exists anywhere; the build README `ids:` key is written as ranges and
  unions across all 25 builds, so it is not a machine-readable unit roster; and the mandatory-key
  mechanism in `.unattended.conf` is the required-key loop in the gate leg, not the
  surviving-placeholder grep, because an empty value substitutes silently.

## Ratified decisions

None yet. The forks are in the spec's §8.

Records live under `spec/` and `build/`. The table below is GENERATED from the status header of every
spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 6 unit(s) · node a · opened 2026-08-11 · streams tooling+playbook+kickoff · ids TOOL-aWrittenMethod-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aWrittenMethod-1 — the build method, rendered and delivered](spec/2026-08-11-spec-aWrittenMethod-1.md) | CLOSED | rev-4 | 2026-08-11 |
| [TOOL-aWrittenMethod-2 — the mandate BASE the run cannot steer](spec/2026-08-11-spec-aWrittenMethod-2.md) | INPROGRESS | rev-3 | 2026-08-11 |
| [TOOL-aWrittenMethod-3 — the method's displacement, at 247 of 250 lines](spec/2026-08-11-spec-aWrittenMethod-3.md) | SPECCED | rev-2 | 2026-08-11 |
| [TOOL-aWrittenMethod-4 — a gate for the sixth carrier](spec/2026-08-11-spec-aWrittenMethod-4.md) | SPECCED | rev-2 | 2026-08-11 |
| [TOOL-aWrittenMethod-5 — the method in the manifest's watch set](spec/2026-08-11-spec-aWrittenMethod-5.md) | SPECCED | rev-2 | 2026-08-11 |
| [TOOL-aWrittenMethod-6 — escaping conf values before substitution](spec/2026-08-11-spec-aWrittenMethod-6.md) | SPECCED | rev-2 | 2026-08-11 |
<!-- /gen:build-index -->
