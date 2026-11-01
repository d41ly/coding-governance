# TOOL-dScopedBuild-4 — the closing review recorded as `review.build.when` says: per build, per unit or per landing, in both modes

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 14 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0402@19e9688b whole
**Carries:** node:policy-key.review.build.when
**Carries:** node:item.build.ratify

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-2-reuse-scout-c.md](../build/2026-11-01-build-TOOL-dScopedBuild-2-reuse-scout-c.md) | research | TOOL-dScopedBuild-2 TOOL-dScopedBuild-13 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |

<!-- /gen:spec-records -->

## 1. Goal

The attended closing review is unenforced: 29 of 59 attended builds with a CLOSED unit carry one,
against 86 of 89 unattended (gap-build-02,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:363`). Only the
unattended `--close` grades it, in the `closing-review-recorded` arm
(`tools/unattended/unattended.sh:11767-11893`), and only once per build, because `verb_review` reads
every subject other than the slug as a spec audit (`:12694-12698`). This unit lifts that arm into one
predicate, `check_closing_review_recorded <slug> <when>`, that both modes' exit runs, and grades it as
`review.build.when` says: once per build, per unit or per landing, each value seen on its planted
case. It places `build.ratify` after the review's disposal.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: the both-mode exit `unattended.sh
--build-exit <slug>`, its attended runner `run_build_exit` and its contract `check_build_exit`, which
sets `BX_BASE`, and the history-derived base `routed_commits.py --build-base <slug>`
(TOOL-dScopedBuild-1 S2, S4, S5; I1 and I2); the owner gate's disposition reader `check_owner_disposition`
(TOOL-dDeclaredLoop-19 S6) and the loop definition `tools/loop/loop.toml` (TOOL-dDeclaredLoop-12 S2),
both of dDeclaredLoop, a parent of dIndexedDesign and dWitnessedBar.

- **S1** — The predicate. `check_closing_review_recorded <slug> <when>` in `tools/unattended/unattended.sh`,
  the body of the `closing-review-recorded` arm moved into a function and the arm reduced to one call,
  and `check_build_exit` calling it as one of its arms (TOOL-dScopedBuild-1 S4), never a verb body, so
  `--close` and `--build-exit` run one predicate (I13). The function is read-only, so under `--close`
  the arm and the exit cannot disagree; and the exit's arm prints its waived line and does not refuse
  where `is_overridden closing-review-recorded` (`:10440`) holds, its `OV_ITEMS` filled by
  `verb_close` from `--override` and empty under `--build-exit`, so an override still waives the one
  item it names. Per owed subject it keeps the arm's two
  terms: a tracked record bound `diff-review` naming a commit inside that subject's range, by ancestry
  both ways (`:11826-11838`); and the last `--review` round on that subject carrying a terminal token,
  read by `review_last_reason` (`:12630`) (`:11872-11890`). Its refusal names the subject and the
  term. Observed by AC1.
- **S2** — `per-build`. One subject, `<slug>`; its range the build's base to HEAD, the base being
  `BX_BASE` where `check_build_exit` has set it, else the answer of `routed_commits.py --build-base
  <slug>` (I1), falling back to the tip on its exit 1 as `check_build_exit` does; any diff-review
  record of the build. Observed by AC1.
- **S3** — `per-unit`. One subject per roster unit with an attributed commit in the per-build range,
  `<slug>:<unit id>`; its commits those `read_attribution_tokens` (`tools/unattended/lib-unattended.sh:1149`)
  attributes to the unit; its record a diff-review record whose `**Serves:**` line names the unit id
  and which names one of those commits. Observed by AC2.
- **S4** — `per-landing`. One subject, `<slug>@<landing base sha7>`, the landing base being the
  run's pinned `base:` fact under a run-state file and, attended, the merge-base of HEAD with the
  default branch `resolve_remote_sh` (`unattended.sh:2510`) names; its range that base to HEAD.
  The landing commit does not exist when its review runs, so the subject is keyed by the base the
  landing sits on. Observed by AC3.
- **S5** — The two modes. With a run-state file (`runmd_of`, `:1347`) both terms are graded. With none,
  the attended mode, the record term is graded over the same ranges and the loop-end term prints
  `loop end: not graded — no run-state file, so no --review round exists to read`, because the
  attended Skill records no rounds; the exit is met on the record term alone. Observed by AC4.
- **S6** — The subject kinds. `derive_closing_subject <slug>` in `tools/unattended/lib-unattended.sh`
  prints the one extended pattern a closing subject matches, `^<slug>(:<unit id>|@<sha7>)?$`, the unit
  id `<FAMILY>-<slug>-<n>`. `verb_review` reads a subject matching it as the closing review, its kind
  sentence and its bound `RUNAWAY_CEILING` (`:12694`, `:12773`), and every other subject as a spec
  audit as today; check 2 in `tools/unattended/check-unattended.sh` passes the pattern to its awk in
  place of its `it != slug` test (`:850`), so a per-unit closing round is never graded as a spec
  row. The reuse-check guard TOOL-dScopedBuild-12 S10 places on a slug-subject round reads the same
  pattern. Observed by AC5.
- **S7** — The key read. `resolve_policy_cli` in `lib-unattended.sh` finds `policy.py` through
  `resolve_kit_dir` (`:132`), as `resolve_index_generator` (`:188`) finds the memory-tree generator,
  and the value is read as `"$py" "$ROOT/$cli" get review.build.when` (I4), a string literal at the
  call. Where the policy kit is not installed, the predicate grades `per-build`, the catalogue default,
  and prints `review.build.when: per-build — the policy kit is not installed`. Observed by AC6 and AC9.
- **S8** — `build.ratify`. `check_build_ratified <slug>` in `unattended.sh`, run inside
  `check_build_exit` after the closing-review predicate is met and never before it, waived with it by
  S1's `is_overridden` test, so `--build-exit` and `--close` both run it and the owner rules on what
  the review's disposal leaves. It reads `decisions.major` through S7's reader. Under
  `author-owner-ratifies` it refuses while a spec of the build carries a fork marked `RESOLVED (agent,
  <date>, delegated)` and `check_owner_disposition <slug> ratification` finds no owner disposition
  record, every delegated fork read as major as TOOL-dDeclaredLoop-19 S5 reads it until a fork record
  carries a class; under `author-rubric` and `owner-only` it prints `ratify: not owed under
  decisions.major <value>`. `item.build.ratify`'s row is declared in `tools/loop/loop.toml`, its needs
  `item.build.recommend` and `item.review.dispose`, so TOOL-dDeclaredLoop-19 S5's stand-in gate is not
  placed beside it and one hold stands. Observed by AC7.
- **S9** — The catalogue row. `review.build.when` at `tools/policy/catalogue.toml:1224` gains `summary`
  and `usage`, its allowed values `per-build`, `per-unit`, `per-landing` and default `per-build`
  unchanged; `policy.py lists --write` re-renders `tools/policy/unsummarised-keys.txt` without it.
  Observed by AC8.
- **S10** — The docs. `tools/unattended/VERBS.template.md`'s `--review` sentence (`:779-780`), rendered
  to `memory/guides/UNATTENDED-VERBS.md`, names the three closing subjects; the attended Skill's
  Stage 6 (`tools/roles/SKILL.template.md:74`, rendered to `.claude/skills/build/SKILL.md`) says a
  closing review is recorded per `review.build.when`, each per-unit record bound `**Serves:**
  diff-review <unit id>`; `help/roles.md` names the key. Observed by AC10.

## 3. Non-goals (OUT)

- No exit contract: `--build-exit` and the base are TOOL-dScopedBuild-1's; this unit's predicate runs
  inside them.
- No change to how a review's findings are disposed: `review.findings` (TOOL-dDeclaredLoop-20 S4) and
  TOOL-dScopedBuild-2's disposal half.
- No loop-end grading in attended mode: the attended Skill records no `--review` rows, and inventing
  an attended run-state record is a write surface this clause does not name (§8 F2).
- No fork class: every delegated fork is major until a later build's fork record carries one
  (TOOL-dDeclaredLoop-19 §3).
- No rows handed to the review: TOOL-dScopedBuild-13 extends the same predicate with the rows' record.

### Edges

- **consumes-from** `TOOL-dScopedBuild-1` — `--build-exit` and `check_build_exit`, the both-mode exit the predicate and the ratification run inside, with `BX_BASE` and `routed_commits.py --build-base`, the range it grades; without them an attended build has no exit to refuse
- **hands-off** `TOOL-dScopedBuild-13` — `check_closing_review_recorded`, which unit 13 extends with the term that the closing review's handed rows are recorded
- **consumes-from** external — TOOL-dDeclaredLoop-19 S5, S6 (`check_owner_disposition` and the stand-in this unit's row stops) and TOOL-dDeclaredLoop-12 S2 (`tools/loop/loop.toml`), specced and DEFERRED at base

## 4. Design

### The owed subjects

| `review.build.when` | Subjects | Range of each | Record it needs |
|---|---|---|---|
| `per-build` | `<slug>` | I1's base..HEAD | a diff-review naming a commit in range |
| `per-unit` | `<slug>:<unit id>` for each roster unit with an attributed commit in I1's range | that unit's attributed commits | a diff-review whose Serves names the unit and that names one of them |
| `per-landing` | `<slug>@<landing base sha7>` | the landing base..HEAD | a diff-review naming a commit in range |

The subject spellings are I13's, with `<landing sha7>` refined to the landing's base (S4). A
`--review` round is recorded on each subject as today: `--review <slug> --subject <subject>`.

### The function

```
check_closing_review_recorded <slug> <when>     # -> 0 met, 1 refused; DOD_OUT holds the reason
  rel = runmd_of slug; mode = attended when no run-state file
  for each owed subject (table above):
    record term   -> the arm's existing ancestry join over that subject's range and record filter
    loop-end term -> review_last_reason rel subject, terminal token, CONVERGED implies zero;
                     attended: the not-graded line
  the first refusal names its subject; a met run prints one line per subject
```

Its body is the arm's code with the range and record filter parameterised; every comment the arm
carries moves with it. `--close`'s arm and `check_build_exit`'s arm call it with the value S7 read;
the two DoD items stay apart, `build-complete` holding the red term and `closing-review-recorded` this
predicate, so an override names the one it waives.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_closing_review_recorded` | function, `unattended.sh` | `sh.function`, `--suggest` OK |
| `check_build_ratified` | function, `unattended.sh` | `sh.function`, `--suggest` OK |
| `derive_closing_subject` | function, `lib-unattended.sh` | `sh.function`, `--suggest` OK |
| `resolve_policy_cli` | function, `lib-unattended.sh` | `sh.function`, `--suggest` OK |
| `<slug>:<unit id>`, `<slug>@<sha7>` | `--review` subject forms | none |
| `item.build.ratify` | `[[item]]` row, `tools/loop/loop.toml` | none |

### Migration

None. At the default `per-build` the owed subject is the slug, as today; the range starts at I1's base,
which for a build of one run is the parent of its first pass and so holds every commit the pinned
base's range held.

### Rollout

Live at landing. A run under `per-unit` or `per-landing` owes those subjects from its first exit after
the policy file names the value.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `tools/policy/catalogue.toml`, and `tools/policy/unsummarised-keys.txt` by `lists --write`
- `tools/loop/loop.toml`: the `item.build.ratify` row
- `tools/roles/SKILL.template.md`, rendered to `.claude/skills/build/SKILL.md`
- `help/roles.md`

### Alternatives rejected

- **A conf key naming the policy CLI, in `RECALL_CLI`'s register.** Rejected by reading
  `tools/policy/legacy-homes.txt`: it is generated and shrink-only, and a conf key the list at the
  compare base lacks reds `lists --check` ("A new key goes in the catalogue instead"). The sibling-kit
  resolver needs no key.
- **The landing commit's sha in the per-landing subject.** At the close the landing commit is the
  prepared merge the review cannot name before it exists; the base it sits on is stable and already a
  run-state fact.
- **Keeping the pinned base for `per-build`.** It grades a carried-forward build's second run alone,
  so a build landing in two runs closes on a review of half its range; I1's base is the build's.
- **A Python home for the predicate.** The arm, `review_last_reason` and the run-state reads are the
  unattended kit's bash, and the kit ships without the memory-tree parser (`:11829-11831`).

## 5. Production-readiness checklist

- security: the predicate reads tracked records and run-state rows only; the subject forms are matched
  by one anchored pattern, so a subject carrying ` · ` or a newline is still refused by `verb_review`
  before any row is written (`:12745-12751`).
- perf / scale: per-unit runs one ancestry walk per unit; `read_attribution_tokens` is one `git log`
  over the range.
- error / empty / loading states: no record, an untracked record, a spec audit standing in, no round,
  and an open loop each keep the arm's distinct sentence, now naming the subject.
- observability: every met subject prints one line; attended prints the not-graded line.
- risks: the per-build range starts earlier than the pinned base for a carried-forward build, so a
  record of an earlier run's commit satisfies it, which is the build-level reading `per-build` means.
- testing: the slices and fixture runs of §6, in `tools/unattended/unattended.test.sh` and
  `tools/unattended/check-unattended.test.sh`.
- migration: none (§4).
- user docs: the verbs guide, the Skill and `help/roles.md` (S10).

## 6. Acceptance criteria

- **AC1** — When `bash unattended.sh --close tRun` runs in a preflighted fixture with no policy file
  and no diff-review record, `closing-review-recorded` is unmet naming the subject `tRun`; with a
  tracked diff-review naming a commit inside `routed_commits.py --build-base tRun`..HEAD and a
  `CONVERGED` round on subject `tRun`, it is met.
  Red when: the arm and the function disagree, or a record outside the range satisfies it.
  fixture: the driver suite's preflighted slug fixture, two units with a pass each.
- **AC2** — When the fixture commits `.governance/policy.toml` setting `review.build.when` to
  `per-unit` and holds one diff-review record serving `TOOL-tRun-1` alone, `--close` is unmet naming
  `tRun:TOOL-tRun-2`; with a second record serving `TOOL-tRun-2` that names that unit's commit, and a
  terminal round on each per-unit subject, it is met.
  Red when: one record over the build satisfies `per-unit`, which is the clause's planted case.
- **AC3** — When the committed policy value is `per-landing` and the only diff-review names a commit
  before the run's pinned base, `--close` is unmet naming `tRun@<the base's sha7>`; with a record
  naming a commit after the base and a terminal round on that subject, it is met.
  Red when: a previous landing's review satisfies this landing.
- **AC4** — When `bash unattended.sh --build-exit tAtt` runs in a fixture build with no run-state file
  and a tracked diff-review naming a commit in its range, it meets the closing-review term and prints
  `loop end: not graded`; with no record it refuses naming `tAtt`.
  Red when: an attended build with no review passes the exit, the gap this clause closes.
  fixture: a scratch repository under `%TEMP%` built by the arm, one CLOSED unit, no `RUN.md`.
- **AC5** — When `bash unattended.sh --review tRun --subject tRun:TOOL-tRun-1 --verdict CLEAN
  --blockers 0` runs twice past `REVIEW_ROUNDS`, the third round is still accepted under
  `RUNAWAY_CEILING` and its refusals say "the closing diff review"; a subject `tRun-specs` is still
  bounded by `REVIEW_ROUNDS`; and `check-unattended.sh` over that run-state file grades no
  `tRun:TOOL-tRun-1` row as a spec row.
  Red when: a per-unit closing subject is bounded or graded as a spec audit.
- **AC6** — When `derive_closing_subject tRun` is sliced from `lib-unattended.sh`, its pattern matches
  `tRun`, `tRun:TOOL-tRun-12` and `tRun@1a2b3c4`, and matches neither `tRun-specs` nor
  `tRunX:TOOL-tRun-1`.
  Red when: a spec-audit subject matches.
- **AC7** — When the fixture commits `decisions.major` as `author-owner-ratifies` and a spec of the
  build carries a fork marked `RESOLVED (agent, 2026-11-01, delegated)`, `--build-exit tRun` with the
  closing review met refuses naming `ratification`; after an owner disposition record naming the gate,
  it is met; under `author-rubric` it prints `ratify: not owed`; with the closing review unmet it
  refuses on that term first.
  Red when: the ratification is graded before the review, or a delegated fork exits unratified.
- **AC8** — When `python tools/policy/policy.py get review.build.when` runs with no policy file, it
  prints `per-build`; after `policy.py lists --write`, `grep -c review.build.when
  tools/policy/unsummarised-keys.txt` prints 0; `git grep -c 'get review.build.when' --
  tools/unattended/unattended.sh` prints at least 1.
  Red when: the row lacks `summary` or `usage`, or no literal reader exists.
- **AC9** — When `resolve_policy_cli` is sliced and run in a fixture with no policy kit beside the
  unattended kit, it returns 1, and `--close` grades `per-build` printing `the policy kit is not
  installed`.
  Red when: a missing kit refuses the exit or grades nothing.
- **AC10** — When `grep -n "tRun:\|<slug>:<unit id>" memory/guides/UNATTENDED-VERBS.md` and `grep -n
  review.build.when .claude/skills/build/SKILL.md help/roles.md` run, each prints the sentence S10
  names, and `tools/unattended/VERBS.template.md` carries the guide's bytes.
  Red when: the guide and its template differ, or a subject form is unnamed.

## 7. Gates

`unattended kit gate` · `check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `policy check` · `recall floor` · `recall floor arms` · `routed-commits selftest` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC9 · the fixture runs under each committed `review.build.when` value and the attended fixture, its failing case one build-wide record under `per-unit` · none

New arm: tools/unattended/check-unattended.test.sh · covers AC5 · a run-state file holding a terminal per-unit closing row with no counts, staged by restoring the `it != slug` test · none

## 8. Open questions

- **F1 — Which base does `per-build` grade from?** Options: (a) I1's history-derived base, in both
  modes; (b) the run's pinned base, as the arm does today, unattended only. (b) has no attended value
  and grades one run of a carried-forward build. RESOLVED (agent, 2026-11-01, delegated): (a), rung 1,
  the clause's "for attended builds as for unattended" read with cl-dClosedLoop-0399's one exit
  contract, whose base is I1's (TOOL-dScopedBuild-1). widens: none · relaxes: none
- **F2 — How is the loop's end read for an attended build?** Options: (a) not graded, said on a
  printed line, the record term alone gating; (b) an attended `--review` record written into a new
  run-state file; (c) the newest record's `## Verdict:` line read as the loop's end. (b) adds a write
  surface the clause does not name (veto 3); (c) reds an honest landing whose round-1 record reads
  BLOCKED and is never rewritten, the reason the arm reads rows rather than verdicts
  (`unattended.sh:11784-11791`). RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the survivor;
  the gap's measured defect is a missing record, which (a) closes. widens: none · relaxes: none
- **F3 — What keys the per-landing subject?** Options: (a) the landing's base, the run's pinned
  `base:` or the attended merge-base; (b) the landing commit; (c) a landing counter. (b) does not exist
  when the review runs; (c) is a second count beside the landed log. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, a refinement of I13's proposed `<landing sha7>` this unit owns.
  widens: none · relaxes: none
- **F4 — How does `build.ratify` hold the build?** Options: (a) `check_build_ratified` after the
  closing-review term, through `check_owner_disposition`, with `item.build.ratify`'s row declared so
  the stand-in stops; (b) leave TOOL-dDeclaredLoop-19's stand-in in place and carry the node by name
  only; (c) a new owner-signed header pointer. (b) builds nothing the node names; (c) is a second owner
  record beside the disposition record. RESOLVED (agent, 2026-11-01, delegated): (a), rung 1,
  `flow-steps.md:296`'s row, "the owner's disposition record for each major fork", read through the one
  reader the grandparent ships. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 4, v2:1337 and :1659, flow-steps:296,
  walkthrough:498-536 (walk B3), research-build:97-99 and :147, gap-register:363, scout C's row 4 and
  interfaces 5 and 6, and the spec brief's I2, I4 and I13.

## 10. Reuse audit

The seam extended is the `closing-review-recorded` arm (`tools/unattended/unattended.sh:11767-11893`),
moved into a function its two callers share, with `review_last_reason` (`:12630`), `verb_review`'s
subject test (`:12694`, `:12773`), check 2's awk (`tools/unattended/check-unattended.sh:850`),
`read_attribution_tokens` (`tools/unattended/lib-unattended.sh:1149`), `resolve_kit_dir` (`:132`) in
`resolve_index_generator`'s pattern (`:188`), and `resolve_remote_sh` (`unattended.sh:2510`).
`python tools/codebase-map/reuse_lookup.py "require a closing review record per unit or per landing
before the build exits"` scanned every layer and ranked name-token helpers (`build`, `records`,
`units`, `build_commit`); none grades a review record, so the arm is the seam, found by reading the
DoD. The recall probe returned TOOL-aBoundedVerdict-16 and TOOL-cBriefedPilot-8, the specs that built
the arm's two terms, and walk B3's ruling; scout C's lines hold at `5f0b11f12`.

Recall terms used: `python tools/memory-recall/query.py "when is the closing review owed and how is it recorded for attended and unattended builds" --terms "closing-review-recorded diff-review review.build.when per-unit per-landing subject verb_review attended BASE"`
