# TOOL-cBriefedPilot-8 — `closing-review-recorded`, joined to the base the run pinned once

**Status:** OPEN · rev-2 · 2026-08-14 · node c · Tier-2 · base 37c05e1b · streams tooling · ratified 2026-08-15

## 1. Goal

Give D7's "review the closing diff" a checker at `--close`: a tracked review record under this build
must name the run's pinned BASE. The join to a value pinned once is what stops a review written
before the run from satisfying it, and the harness that writes the review writes the value, so an
honest run passes with no authoring step.

## 2. Scope (IN)

- **S1** — `closing-review-recorded:machine` appended to `DOD_CORE` in
  `tools/unattended/unattended.sh`, making the kit-owned core eight items.
- **S2** — a `dod_met` case arm for it, in the SAME commit as S1, or the item falls to the `*)`
  default and becomes satisfiable by one line the run writes into its own record.
- **S3** — the arm reads the recorded BASE, refuses a value shorter than eight characters, and selects
  a tracked review record under this build that contains its first eight characters:

  ```sh
  rb=$(fact "$rel" base); [ ${#rb} -ge 8 ] \
    && GIT grep --cached -qF -- "${rb:0:8}" -- "$M/builds/$slug/reviews/*.md"
  ```

- **S4** — one clause appended to the synth agent's write instruction in
  `tools/workflows/tier2-review.js`: open the report with a line naming the reviewed range
  `<base>...<head>`.
- **S5** — `CORE_FLOOR` in `.unattended.conf` moves `10:7` to `10:8`. Unit 7 makes the first half of
  the move; this unit makes the second, so each commit's floor matches its own core set.
- **S6** — arms in `unattended.test.sh` for the empty-`reviews/` case, the matching record, the
  untracked record, a record naming a different sha, and an absent `base:` line.

## 3. Non-goals (OUT)

- **Any heading or verdict grammar.** Measured over this corpus's 46 tracked review records:
  `^## Verdict: CLEAN` matches zero files, `^## Verdict:` matches six with the values `BLOCKED` five
  times and `CHANGES REQUESTED` once, and nine more carry a bare `^## Verdict` with no colon. An
  anchor on the verdict value would make the item unsatisfiable against every record this repo has
  written. The rejection is recorded in the build README as risk 2, and this unit does not reopen it.
- **A review-record authoring step in M8.** The design pass folded it out: M4 already mandates the
  `## Verdict: CLEAN` opening line, and a second opening-line rule in M8 would be two answers to one
  question inside the file whose M1 forbids exactly that. The run's only obligation stays the rename
  M8 already requires.
- **A filename or sequence join between a spec and a review.** Measured wrong on 7 of 7 multi-unit
  builds in this corpus and recorded in the driver's own comment.
- **Judging what the review said.** The item measures that a record exists and names the pinned BASE.
  Everything else is §5's risk row, stated rather than implied away by the label.
- **A new `fail` branch.** The item reports through `verb_close`'s existing `fail 13`. `ARMS_FLOORS`
  is untouched by this unit.

## 4. Design

### Data model

The recorded BASE is a run fact, read with the existing `fact()`. Its first eight characters are the
needle, because a sha spelled in prose is spelled abbreviated: measured, 15 of the 46 tracked review
records contain an eight-hex-shaped token and none contains a full forty-character one.

The length guard is not defensive decoration. `grep -F ""` matches every line of every file, so an
absent or truncated `base:` line would make the selection match the first review record in the build
and the item would pass by finding anything. That is the same degeneration an empty base once caused
in `check_authorization`, where it turned a provenance test into a read of the git index.

`GIT grep --cached` is one command answering the exact question. `--cached` reads the INDEX, which is
the leg's own stated per-run population and the reason `--preflight` stages the run-state file, so an
untracked review is excluded by construction rather than by a filter. It runs through the driver's
`GIT()` wrapper because it turns index entries into bytes, and the wrapper is what makes an
object-substitution lever inert for this kit's reads.

### What the harness contributes, and its measured limit

`tools/workflows/tier2-review.js` already holds the range: `const base = a.base || 'origin/main'` at
line 65 and `const head = a.head || 'HEAD'` at line 66, and it already instructs the synth agent to
write a markdown report. S4 appends one clause to that instruction, so the value the check joins on
reaches the record without anyone remembering to type it.

**The limit, stated because the clause looks like it guarantees more than it does.** That default is a
REF, not a sha. A caller who lets it stand produces a report opening `origin/main...HEAD`, which
carries no sha and satisfies nothing. What makes the clause work under a mandate is M8, which spells
the invocation with `base: '<BASE sha>'` and says in the same paragraph that the base is an immutable
sha and never a moving ref. The harness is not changed to enforce that; see §8.

### Why the join is to a value pinned once

Unit 5 makes `--preflight` write `base:` only when the record carries none. Without it a re-preflight
— which is mandatory before every `--close`, and is also the documented post-compaction recovery —
re-derives the base, and a review record written against the earlier value stops matching. The item
would then be unmet for a run that did everything right, at the verb that has nobody to read the
refusal. That is the whole of this unit's dependency on unit 5.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | `DOD_CORE` plus one `dod_met` case arm |
| `.unattended.conf` | `CORE_FLOOR` `10:7` to `10:8` |
| `tools/workflows/tier2-review.js` | one clause in the synth write instruction |
| `tools/unattended/unattended.test.sh` | five arms |

### Alternatives rejected

- **Requiring a forty-character sha in the record.** Zero records in this corpus carry one, so the
  item's steady state would be the routine override the design listed as a risk — and a routinely
  overridden item is a check that has been turned off with extra steps.
- **Selecting with `git ls-files` piped through `xargs grep`.** Same answer, three processes and an
  `xargs -r` portability assumption, against one `git grep --cached`. Process spawn is what this
  kit's own comments record as dominating on Windows.
- **Reading the worktree rather than the index.** It would let an unsaved, unstaged, uncommitted
  report satisfy a Definition-of-Done item, which is the property the whole staging discipline exists
  to deny.

## 5. Production-readiness checklist

- security — N/A. The needle is a sha prefix; nothing is executed and nothing is written.
- perf / scale — one `git grep` over one build's `reviews/` directory at close.
- a11y · i18n — N/A.
- error / empty / loading states — the absent-base and no-records cases are distinct and both armed.
- observability — one unmet item at `--close`, naming itself.
- risks — three, all real and none removable inside this unit. It cannot tell an adversarial review
  from any other: an M4 per-spec review written this run that cites the base satisfies it. A BLOCKED
  review satisfies it, and the landed-with-a-blocker path is covered by `build-complete` instead,
  which rests on M8's "a blocker unfixable inside the mandate's scope is a park, and its unit does not
  close" being honoured. And both sides of the join are written under the run's own uid, which is
  protocol §9's boundary and is unchanged by this unit.
- testing + left-shift gates — the five arms in S6, plus the harness clause exercised by the existing
  workflow-script legs.
- migration / rollback — the `CORE_FLOOR` raise and the `DOD_CORE` addition land together. A run with
  no review record does not silently pass; it blocks, which is the intended new behaviour.
- user docs — protocol §4's table row is unit 18. M8 needs no edit, and that is deliberate.

## 6. Acceptance criteria

- **AC1** — When the build's `reviews/` directory holds no tracked record, `--close` blocks naming
  `closing-review-recorded`.
- **AC2** — When a tracked review record contains the recorded BASE's first eight characters,
  `--close` proceeds past the item.
- **AC3** — When that same record exists but is UNTRACKED, `--close` blocks.
- **AC4** — When the only tracked record names a different sha, `--close` blocks.
- **AC5** — When the run-state file carries no `base:` line, `--close` blocks on this item rather than
  matching the first record in the directory.
- **AC6** — When `tier2-review.js` runs with `base` set to a sha, the report it names opens with a
  line carrying that sha and the head.
- **AC7** — With `CORE_FLOOR` at `10:8` and the item removed from `DOD_CORE`, the `unattended kit
  gate` reds on the shrunk core set; with both present it is green.

## 7. Gates

`unattended driver selftest` (`tools/unattended/unattended.test.sh`) · `unattended kit gate`
(`tools/unattended/check-unattended.sh`, for the `CORE_FLOOR` pin) · `workflow script syntax`
(`tools/workflows/check-workflow-syntax.js`) · `review-join ban (no ref-keyed join)`
(`tools/workflows/check-review-join.sh`) · `review-join self-test` · `verifier fan-out self-test` ·
the full bar at the push boundary.

## 8. Open questions

none — the fork below is RESOLVED (agent, 2026-08-15, delegated): option A — `tier2-review.js` keeps accepting a ref, and M8's spelling carries the rule.

  Option B was ruled infeasible by the finding's own evidence: the harness has no filesystem and no
  repo access, so it cannot see whether a mandate is in force, and the flag would have to come from
  the caller already passing the base wrongly. The failure surfaces as an unmet DoD item naming the
  run's own record, which is where the fix belongs. §8 named the agent as resolver.

**Should `tier2-review.js` refuse a non-sha `base`, or is M8's spelling enough?** The default
`'origin/main'` is a moving ref, and a caller who lets it stand writes a range line that satisfies
nothing while looking like compliance.

- **Option A: leave it.** M8 spells the mandated invocation with the pinned sha and states the rule in
  the same paragraph. The harness has attended callers too, for whom a ref is the normal and correct
  argument, and refusing one would break them for a rule that is not theirs.
- **Option B: refuse a non-sha `base` under a mandate.** The harness cannot see whether a mandate is
  in force — it has no filesystem and no repo access, which is recorded in its own honest-limit
  comment — so the flag would have to be passed by the caller who is already passing the base wrongly.

Recommendation: **A**, and let the failure surface as an unmet item rather than as a harness refusal;
the unmet item names the run's own record, which is where the fix is. Resolver: agent, if the owner
does not take it.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds FG-1, FG-8, FG-13, C5 and C12's
  claim without C12's fix. The corpus measurements in §3 and §4 were re-run against this tree at
  authoring; the harness's `base` default was read at `tier2-review.js:65` and is the source of §8.

- rev-2 · 2026-08-15 · §8 resolved under the standing mandate for `cBriefedPilot`; the pick and the reasoning are in §8. Header gains the ratified pointer.

## 10. Reuse audit

- **`dod_met` in `tools/unattended/unattended.sh`** — the seam, extended by one `case` arm exactly as
  unit 7 extends it. The reporting, the override budget and the machine-versus-agent labelling come
  with it.
- **`fact()`** — the recorded-BASE reader, already used by `trusted_base`, `verb_status` and the leg's
  own `fact_of`. No second parser.
- **`GIT()`** — the dereference pin. The new read goes through it for the reason the wrapper exists,
  rather than being spelled as a plain `git` because it happens to read the index.
- **`tools/workflows/tier2-review.js`'s synth write instruction** — an existing instruction string
  gains a clause. No new agent, no new phase, no change to the fan-out the review protocol caps.

Probes run at authoring for the cluster. `python tools/codebase-map/reuse_lookup.py "unattended run
definition of done item checked at close"` returned no seam that joins a run fact to a review record;
the nearest hits are generic `check` and `run` name stems, recorded as a miss rather than retried.
Recall terms used: unattended close DoD override roster README region generated units plan spec
status terminal review base.
