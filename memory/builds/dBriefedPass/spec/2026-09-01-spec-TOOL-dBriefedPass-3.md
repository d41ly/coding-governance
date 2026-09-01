# TOOL-dBriefedPass-3 — a build pass on an unspecced, THIN or out-of-order unit is REFUSED

**Status:** SPECCED · rev-1 · 2026-09-01 · node d · Tier-2 · base 269dacae · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-prompt-TOOL-dBriefedPass-1.md](../prompts/2026-09-01-prompt-TOOL-dBriefedPass-1.md) | research | TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |

<!-- /gen:spec-records -->

## 1. Goal

Move the M2 hard floor from a rule an agent remembers to a refusal a machine makes. A build pass
declared for a unit that is MISSING, THIN or out of its declared order is refused at the moment of
the act, and a unit whose build commit predates a conforming spec reds the merge bar afterwards.

## 2. Scope (IN)

- **S1** — `--dispatch` REFUSES when its `--pass <unit-id>` names a unit whose `plan_state` is
  `MISSING` or `THIN`. The message names the id, the state and the section that is empty.
- **S2** — `--dispatch` REFUSES when the unit's declared `order` step has an earlier step holding a
  unit that is neither terminal nor itself dispatched. Units sharing an order value are the parallel
  group and do not block each other; a unit with NO order verb is unordered and is not blocked.
- **S3** — a new merge-bar check in `tools/unattended/check-unattended.sh`: for every unit the build
  README's generated region carries as CLOSED, the commit that BUILT it must have a conforming,
  non-THIN spec for that id at its FIRST PARENT. The build commit is the earliest commit in
  `BASE..HEAD` carrying the unit id in its subject and touching a file outside `spec/` and outside
  `reviews/`.
- **S4** — S3 is DATE-GATED by a new `.unattended.conf` declaration `PASS_ORDER_CUTOFF`, on the
  build README's `opened:` date, for the reason every other cutoff in this conf exists: every build
  that landed before this check cannot be rewritten, and a term that reds them is unlandable by any
  run. BLANK or absent turns the term OFF and the check ANNOUNCES that it did.
- **S5** — S3 reports a LIVENESS assertion on every run: the number of builds graded and the number
  skipped by the cutoff. A check that grades nothing must say so rather than printing a clean bill.
- **S6** — the check is registered in `tools/gate-legs.json` with a declared ceiling.
- **S7** — arms in `tools/unattended/unattended.test.sh` and
  `tools/unattended/check-unattended.test.sh` for every refusal, each observed RED before the guard
  exists, and each observed GREEN on the legitimate shape it must not refuse.

## 3. Non-goals (OUT)

- The check does not require a build pass to have been dispatched. `--dispatch` is owed by
  CONCURRENT passes; making it mandatory for every pass is `TOOL-dBriefedPass-5`'s carrier edit, and
  stating the requirement in two places would be two answers to one question.
- The check does not grade whether the spec was GOOD, reviewed, or followed. `specs-audited` already
  measures that a pre-code audit left evidence, and this is a strictly different question.
- No existing gate leg is scoped, relaxed or exempted to make room for this one.
- Retro-grading landed builds is explicitly out, by S4.

## 4. Design

### Data model

S3's join, stated as the predicate rather than as prose, for each CLOSED unit id `U` under build
`B`:

1. `C` is the earliest commit in `BASE..HEAD` whose subject contains `U` as a WHOLE TOKEN and whose
   diff touches at least one path outside `memory/builds/<B>/spec/` and `memory/builds/<B>/reviews/`.
2. If no such commit exists, the unit contributes NOTHING and is counted as `unbuilt-in-range`. A
   run whose units were built before its own BASE is the ordinary shape for a resumed build.
3. Otherwise, at the first parent of `C`, a tracked file under `memory/builds/<B>/spec/` must carry
   `U` in a conforming status header, and `plan_state` over that blob must not return `MISSING` or
   `THIN`.

The whole-token match is mandatory and its class is `memory/gotchas/id-matched-as-a-substring`:
every id ending in a 1-up sequence is a prefix of nine others, so an unanchored `TOOL-x-1` would
match `TOOL-x-19`'s commit and grade the wrong unit.

### Migration

`PASS_ORDER_CUTOFF` is seeded to the day this unit lands, so the population it grades starts empty
and grows. S5's liveness line is what stops that empty population reading as a pass.

### Alternatives rejected

- **Refuse at COMMIT time via a hook.** Rejected: the pre-commit hook runs a fast leg and a
  history-based join is not fast; and a hook is bypassable by the documented flag, which the
  protocol already names as a lever it cannot close. The merge bar is where this binds.
- **Assert the spec existed at BASE.** Rejected: the build method REQUIRES a run to author a missing
  spec, so a BASE-anchored test would refuse the shape the method mandates. The first parent of the
  BUILD commit is the correct anchor — it admits authoring, and refuses authoring AFTERWARDS.
- **Grade every unit, not only CLOSED ones.** Rejected: an OPEN unit legitimately has no build
  commit yet, so the term would red mid-build on every run including the one that must land it.

### Files touched (estimate)

`tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`, `tools/gate-legs.json`,
`.unattended.conf`, `tools/unattended/.unattended.conf.example`, and both test suites.

## 5. Production-readiness checklist

- **Security · data · write surface** — none new. The check reads git history and tracked blobs.
- **Performance** — one `git log` over the run's range per build plus one `plan_state` per graded
  unit. `TOOL-aCollapsedScan-4` records the `unattended kit gate` leg already over its declared
  120 s ceiling, so this check ships as its OWN leg with its own declared ceiling rather than
  widening that one. A leg arriving without a ceiling reds by that fact.
- **Error states** — S1's and S2's refusals each name the id, the state and the remedy.
- **Observability** — S5's liveness line on every run, graded and skipped counts both.
- **Testing** — S7, with the negative arms observed RED first.
- **Migration · rollback** — the cutoff. Reverting is deleting the leg row and the conf key.

## 6. Acceptance criteria

- **AC1** — a dispatch naming a unit with no tracked spec is REFUSED, naming the id and `MISSING`.
  Observed RED against the shipped driver, which accepts it today.
- **AC2** — a dispatch naming a unit whose spec has an empty acceptance section is REFUSED, naming
  `THIN` and the empty section.
- **AC3** — in `tools/unattended/unattended.test.sh`, a dispatch at order 3 while an order-2 unit is OPEN and undispatched is REFUSED naming
  the blocking unit; the same call with that unit CLOSED succeeds. Both arms, because a refusal with
  no observed passing case is a gate that cannot be satisfied.
- **AC4** — in `tools/unattended/unattended.test.sh`, two units sharing one order value dispatch concurrently without either refusing the
  other. This is the arm that proves S2 did not serialize the parallel group.
- **AC5** — in `tools/unattended/check-unattended.test.sh`, a staged fixture repo where a unit's build commit precedes its spec commit reds the new
  leg, and the message names the unit and both shas. Staged, confirmed RED, unstaged.
- **AC6** — in `tools/unattended/check-unattended.test.sh`, the same fixture with the spec commit FIRST is green. The passing case, observed.
- **AC7** — with `PASS_ORDER_CUTOFF` blank the leg prints its announced-OFF line and exits 0, and
  with it set the leg prints the graded and skipped counts. A run that grades zero builds says so.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended driver selftest` · `unattended kit gate` ·
the new leg itself · `gate manifest shape` · `memory hygiene`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · authored under the dBriefedPass mandate.

## 10. Reuse audit

No existing seam fits the history join in S3, and the evidence is that `plan_state` is called at
exactly two sites in the shipped driver — `tools/unattended/unattended.sh:2067` in `--plan`, which
only reports, and `:3271` in the `build-complete` term, which runs after every commit has landed.
Neither is a refusal at the moment of the act, which is the whole gap. What IS extended, cited by
path: `pass_commit` in `tools/unattended/lib-unattended.sh:98-109` already resolves the commit that
carries a unit id in its subject and touched a declared path, which is step 1 of S3's predicate, and
`TOOL-dCarriedReceipt-3` records its known limitation for FOLD passes spanning many units — read
that row before extending it.

Recall terms used: unattended mandate pass ordering workflow harness spec before code regrounding
compaction driver orchestration agent-cap fan-out build-method handoff prompt.
