# TOOL-dRetiredFork-4 — reconcile inCMS's agent-cap fail-open claim against HEAD

**Status:** CLOSED · rev-4 · 2026-09-03 · node d · Tier-1 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-build-TOOL-dRetiredFork-4-1-d1-reconciliation.md](../build/2026-09-03-build-TOOL-dRetiredFork-4-1-d1-reconciliation.md) | journal | — |
| [2026-09-03-prompt-TOOL-dRetiredFork-4-1-build-brief.md](../prompts/2026-09-03-prompt-TOOL-dRetiredFork-4-1-build-brief.md) | journal | — |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md](../reviews/2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md) | diff-review | DEPL-dRetiredFork-1 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

**This unit's rev-1 premise was measured FALSE, and the unit is rescoped rather than rewritten
around.** rev-1 claimed, from inCMS's `KIT_AGENT_CAP_DELTA` D1 row, that a marked sequential-agent
loop nested inside another loop exits `0` where the unnested form exits `2` — a fail-open. Reproduced
at `b0108f13` through the live hook: the nested case exits **2** and the unnested exits **0**, the
exact opposite. The machinery rev-1 said was missing is present and named:
`tools/hooks/agent-cap.js:949` reads "NESTED LOOPS FAIL CLOSED WITH NO EXTRA CLAUSE",
`tools/hooks/README.md:48` already owns the clause, and `tools/hooks/agent-cap.test.sh:357` already
ships the fixture as `seq fold: a marked loop inside an UNMARKED loop -> deny`, expecting exit 2.

So there is no fail-open of that shape to close. What remains is real and unfinished: an adopter
carries a divergence row asserting a defect gov's own suite contradicts, and nobody has disposed of
it. This unit disposes of it, and absorbs nothing until it has.

## 2. Scope (IN)

- **S1** — Obtain inCMS's actual reproduction for D1: the fixture, the invocation and the observed
  exit code, from `ARCH-aFerriedToolkit-3` or from that adopter's own suite. rev-1 paraphrased the
  registry's `what` field and ran nothing, which is how the direction inverted.
- **S2** — Run that exact fixture against gov `b0108f13` and record both exit codes verbatim.
- **S3** — Dispose on the evidence, in exactly one of three ways, and record which. **(a)** The
  fixture reproduces a real gov defect of a DIFFERENT shape than rev-1 described — most plausibly an
  outer iteration count multiplying an admitted inner bound, which the `:949` comment does not cover
  — and this unit is superseded by a new spec describing THAT defect. **(b)** It does not reproduce
  at HEAD, the row is stale, and `DEPL-dRetiredFork-7` strikes it from inCMS's register. **(c)** It
  reproduces only under an adopter-local modification, so it is inCMS's and not gov's.
- **S3b** — Reconcile against gov's OWN open row, which rev-1 and rev-2 both missed:
  `TOOL-aNumeralWarden-2` (`memory/backlog/TOOL.md:79`) records that agent-cap's enclosing-opener
  walk is defeated by two nested wrappers or by 59 lines of distance between the `.map` and the
  `agent(` call, that it needs a STATEMENT-LEVEL walk rather than an opener count, and that the
  58/59 boundary is unfixtured. That row decided the remedy AGAINST the depth-stack shape rev-1
  proposed — a depth stack is an opener count one level smarter, over the same 60-line window the
  live code walks. Any disposition (a) successor must be that row, not a new id.
- **S4** — Whatever the disposition, record the reconciliation between inCMS's row and
  `agent-cap.js:949` in `memory/DECISIONS.md`. The next session reading that registry row will
  otherwise repeat rev-1's error.

## 3. Non-goals (OUT)

- Editing `tools/hooks/agent-cap.js`. No defect is established, and rev-1's S1 would have added a
  depth stack the file already carries.
- Modelling regex literals in the literal-blanker. Unchanged from rev-1: inCMS declined it, and
  matching raw text is fail-closed in the wrong direction, because the hook's own remedy string
  contains `parallel(` and so does every correct `boundedParallel` helper.
- Changing the fan-out bound. Parked at build level as an owner turn.

## 6. Acceptance criteria

- **AC1** — inCMS's D1 fixture is recorded verbatim in this build's folder with the invocation that
  runs it, and `bash tools/hooks/agent-cap.test.sh` still passes unchanged at `b0108f13`.
- **AC2** — Running that fixture against gov HEAD produces a recorded exit code, and the record
  states whether it agrees with inCMS's claim or with `tools/hooks/agent-cap.js:949`.
- **AC3** — Exactly one disposition from S3 is recorded, naming its evidence. Disposition (a) names
  the successor spec id; (b) names the register row `DEPL-dRetiredFork-7` will strike.
- **AC4** — `memory/DECISIONS.md` carries the reconciliation, and `bash
  tools/memory-tree/check-memory-hygiene.sh` exits `0` afterwards.

## 7. Gates

`agent-cap self-test` · `memory hygiene` · `workflow script syntax` ·
`verifier fan-out`.

## 8. Open questions

none - rev-1's premise was measured FALSE and the unit was rescoped on that
measurement, which settles the question rather than opening one. This section is present
because a section 8 with neither an item nor a `none` form is a refusal, not a pass, and both
this spec's readers grade it that way.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from the inCMS `KIT_AGENT_CAP_DELTA` D1 row and
  `ABL-aFerriedToolkit-3`.
- rev-2 · 2026-09-02 · folded spec-audit round 1, findings B4 and B5. B5 measured the rev-1 premise
  INVERTED at HEAD — the nested case denies, the unnested admits — so the unit is rescoped from an
  absorption to a reconciliation, dropped from Tier-2 to Tier-1, and its goal, scope and acceptance
  are replaced rather than edited. B4 found every rev-1 acceptance criterion anchored on
  `.claude/hooks/agent-cap.test.sh`, which is not tracked; the suite is `tools/hooks/agent-cap.test.sh`,
  and rev-2 names no untracked path. The README's "nine fixes" count drops to eight.
- rev-3 · 2026-09-02 · folded spec-audit round 1, findings H15 and M6. H15: gov holds an OPEN row for this exact defect,
  `TOOL-aNumeralWarden-2`, which decided the remedy AGAINST the shape rev-1 absorbed; S3b binds the
  disposition to it. rev-2's §10 probe missed the one gov record that binds the change. M6: §7 named
  `agent-cap restatement`, which grades the charter's five machine-compared values and is unrelated
  to this unit; removed.
- rev-4 . 2026-09-02 . added the section 8 `none` declaration both readers require;
  no design content changed.
