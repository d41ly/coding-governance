# TOOL-aRepatriatedFork-4 — review-harness gates find harnesses where adopters keep them

**Status:** CLOSED · rev-2 · 2026-09-23 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-23-build-TOOL-aRepatriatedFork-4-1-acceptance-ledger.md](../build/2026-09-23-build-TOOL-aRepatriatedFork-4-1-acceptance-ledger.md) | journal | — |
| [2026-09-24-build-DEPL-aRepatriatedFork-1-runlog-0e284ca8.md](../build/2026-09-24-build-DEPL-aRepatriatedFork-1-runlog-0e284ca8.md) | journal | DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 TOOL-aRepatriatedFork-21 |
| [2026-09-23-prompt-TOOL-aRepatriatedFork-4-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-4-build-brief.md) | journal | — |
| [2026-09-24-review-TOOL-aRepatriatedFork-2-closing-diff-round1.md](../reviews/2026-09-24-review-TOOL-aRepatriatedFork-2-closing-diff-round1.md) | diff-review | DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

Make `tools/workflows/check-verifier-fanout.sh` and `tools/workflows/check-review-join.sh` judge the
review harnesses both adopters actually run, which live under `.claude/workflows/`. Today both gates
scope their population to their own install prefix, so at inCMS they print a clean verdict over a set
that excludes all 13 live harnesses, and both adopters carry a hand-kept population fork to compensate.

## 2. Scope (IN)

- **S1** — `check-verifier-fanout.sh` applies no path filter to its discovery population. The
  `export const meta` marker it already applies at `tools/workflows/check-verifier-fanout.sh:86` is
  the whole selector, which is the rule `check-workflow-syntax.js` already follows. Observed by AC1,
  AC2 and AC3.
- **S2** — `check-review-join.sh` keeps its derived prefix and ADDS the harness convention directory,
  so its population is the kit prefix united with `.claude/workflows/`. It applies no marker filter,
  so the prefix cannot simply go. Observed by AC4, AC5 and AC6.
- **S3** — Both gates name the population they resolved in their empty-population refusal, and
  review-join also in `--explain` and its clean line, so a reader can see that `.claude/workflows/`
  was consulted. Verifier-fanout has no `--explain`; its refusal alone names the population.
  Observed by AC4 and AC7.
- **S4** — Correct the three places that state the old split: the comment at
  `tools/workflows/check-workflow-syntax.js:38-42`, the paragraph at `tools/workflows/README.md:80-83`
  and the population section above it. Each says the other two gates apply no marker filter, which
  has been false for `check-verifier-fanout.sh` since `3c794dcd` (2026-08-08). Observed by AC8.
- **S5** — One regression arm per gate, staged red first against the a7c78ad2 bytes, and a review-harness
  version bump because shipped bytes move. Observed by AC2, AC5 and AC9.

## 3. Non-goals (OUT)

- A conf key or a harness-home list. Rejected in §4 Alternatives.
- The agent-cap predicate itself, including the cap value the verifier-fanout message prints. That
  is `TOOL-aRepatriatedFork-7`, which renders the declared cap into messages.
- Shipping the new arms to adopters. Both suites are `project-owned` in `tools/workflows/kit.toml:33-34`,
  so the arms bind gov's bar only; carrying a gov suite to an adopter is `TOOL-aRepatriatedFork-18`.
- inCMS's `KIT_CHECK_REVIEW_JOIN_TEST_DELTA` fork of `check-review-join.test.sh`. Its delta is a
  verdict-conflict arm, not a population, and it stays with inCMS.
- nc's `.claude/worktrees/` exclusion, which nc already declined to re-apply. Measured again here:
  in gov's primary tree, with three nested worktrees present and `.claude/worktrees/` not ignored,
  `git ls-files --cached --others --exclude-standard -- '*.js'` lists no file under a nested worktree,
  because git does not descend into a directory holding a `.git` file.

### Edges

none

## 4. Design

### Data model

No data. Two population expressions change.

| gate | today (a7c78ad2) | after |
|---|---|---|
| `check-verifier-fanout.sh` | `POP_RE="^$KIT_PREFIX/.*\.js$"` at `:43`, then the marker filter at `:86` | every `*.js` git lists, then the marker filter at `:86` |
| `check-review-join.sh` | `POP_RE="^$KIT_PREFIX/.*\.js$"` at `:64`, no marker filter | the prefix OR `.claude/workflows/`, still no marker filter |

The review-join expression, written out because a table cell cannot hold its alternation:

```sh
if [ -n "$KIT_PREFIX" ]; then POP_RE="^($KIT_PREFIX|\.claude/workflows)/.*\.js$"; else POP_RE='\.js$'; fi
```

The empty-prefix branch of review-join is unchanged: a root install already sees every `*.js`.

The asymmetry is deliberate and is the same one `TOOL-dRetiredFork-10` recorded. `TOOL-dRetiredFork-10`
§3 refused deleting the review-join prefix because the widened population admitted
`.claude/hooks/agent-cap.js`, whose ban table trips the predicate. That still holds for review-join.
It never held for verifier-fanout: that spec's S2 said verifier-fanout applied no marker filter, and
the marker at `:86` had existed since `3c794dcd`. Deleting its prefix admits no unmarked file.

`.claude/workflows/` joins the review-join population as a literal for the reason the hook's third
probe rung is one (`tools/workflows/check-review-join.sh:73-75`, F1 ratified): it is the harness's
own convention, not an install prefix an adopter picks. Hooks under `.claude/hooks/` stay out,
which is the narrowing inCMS's fork chose (`scripts/workflows/check-review-join.sh:114-117` at inCMS)
and the reason nc's `\.claude` wholesale form (`scripts/workflows/check-review-join.sh:71` at nc) is
not taken.

### Inventory

Measured 2026-09-23 by running the post-change expression from a scratch copy of each gate against
each tree. PINNED; AC2 and AC5 re-derive them.

| tree | verifier-fanout today | verifier-fanout after | review-join judged after |
|---|---|---|---|
| gov | 7 | 7 | 3, clean |
| inCMS | 7 (gov bytes) or 13 (its fork) | 20, clean | 15, clean |
| nc | 7 (gov bytes) | 31, clean | 26, clean |

Nothing is minted. No identifier is added, so no naming cell is graded.

### Migration

What each adopter then does, once `govkit update` delivers these bytes.

| adopter | record | disposition |
|---|---|---|
| inCMS | `.governance/kits.json` divergence row `scripts/workflows/check-review-join.sh` (`INCMS REPATH`, `:387-391`) | deleted with the fork; the file takes gov bytes and its role in `kits.json:202` becomes `engine` |
| inCMS | divergence row `scripts/workflows/check-verifier-fanout.sh` (`INCMS REPATH`, `:397-401`) | deleted the same way, `kits.json:204` becomes `engine` |
| inCMS | role `diverged` for `scripts/workflows/check-workflow-syntax.js` (`kits.json:206`) | becomes `engine`: the file is already byte-identical to gov a7c78ad2 (measured 2026-09-23), so the role is stale bookkeeping and no byte moves |
| nc | `nc carve-out 10/24` in `scripts/workflows/check-verifier-fanout.sh:43-54`, `:86-89` | deleted; gov bytes |
| nc | `nc carve-out 11/24` in `scripts/workflows/check-review-join.sh:64-72`, `:109-119` | deleted; gov bytes |
| nc | the census denominator in `scripts/check-nc-wiring.sh:260-269` | falls by two, which arm 4 of that script requires in the same commit |

inCMS gains two capabilities it lacks by taking gov bytes: the predicate delegation through
`node "$HOOK" --only=join` (gov `:139`, where inCMS still carries three inline awk bans at
`scripts/workflows/check-review-join.sh:217-219`), and the refusal when agent-dispatching files
exist but arm 2 judged none (gov `:346-352`).

inCMS's divergence check `scripts/check_divergence.py` pairs each row with its marker in both
directions, so the row and the `INCMS REPATH` comment leave in one commit.

### Rollout

One gov commit with the version bump. Adopters converge on their next `govkit update`.

### Files touched (estimate)

- `tools/workflows/check-verifier-fanout.sh`
- `tools/workflows/check-review-join.sh`
- `tools/workflows/check-workflow-syntax.js` (comment only)
- `tools/workflows/check-verifier-fanout.test.sh`
- `tools/workflows/check-review-join.test.sh`
- `tools/workflows/README.md`
- `tools/workflows/tier2-review.js` (the two `review-harness` and `tier2-review` markers)

### Alternatives rejected

- **A declared population key.** audit-B §6 proposed one. Rejected for the reason
  `TOOL-dRetiredFork-10` gave for the prefix: an adopter cannot read a key its installed kit predates,
  and the marker already identifies a harness wherever it lives.
- **Receipt-driven kit homes.** Resolving homes from `.governance/install.json` answers where GOV's
  files went, and the files this gate misses are the adopter's own harnesses, which have no receipt row.
- **Deleting review-join's prefix.** Measured and refused by `TOOL-dRetiredFork-10` §3; nothing moved.

## 5. Production-readiness checklist

- security — N/A: both gates read tracked and untracked-unignored `*.js` and pipe them to an
  existing node predicate; no new input reaches a shell.
- perf / scale — verifier-fanout now runs `grep` over every listed `*.js` once. At nc that is 31
  marker hits out of the repo's `*.js`; the predicate still runs only on marked files.
- error / empty / loading states — both empty-population refusals stay, and now name the population
  they resolved instead of `$KIT_SAYS/` alone.
- observability — `--explain` on review-join lists `.claude/workflows/` beside the prefix.
- risks — a verifier-fanout red at an adopter on a harness it never judged before. That is the point,
  and it was measured clean at both adopters on 2026-09-23.
- testing — one foreign-layout arm per gate in the existing suites, reusing `mkfix` in
  `tools/workflows/check-verifier-fanout.test.sh:94-110`.
- migration — reverting restores the prefix filter; no adopter state changes.
- user docs — `tools/workflows/README.md` states the population rule once for all three gates.

## 6. Acceptance criteria

- **AC1** — When `bash tools/workflows/check-verifier-fanout.sh` runs in gov's tree, it reports
  `clean — 7 workflow script(s)`, the same count as at a7c78ad2.
  Red when: dropping the prefix admits a gov file the marker filter should have excluded.
  figure: PINNED at 7, measured 2026-09-23.
- **AC2** — When a fixture installs `tools/workflows/check-verifier-fanout.sh` under a `scripts/`
  prefix and carries its only harness, one with an unbounded verify stage, under `.claude/workflows/`,
  the gate exits `1` naming that harness; the a7c78ad2 bytes exit `1` with `the population is empty`.
  Red when: the population still stops at the kit prefix, and the fixture reads as empty.
- **AC3** — When the fixture of AC2 also carries a file under `.claude/workflows/` with no
  `export const meta`, the gate does not judge it.
  Red when: the marker filter was dropped along with the prefix.
- **AC4** — When `bash tools/workflows/check-review-join.sh --explain` runs in gov's tree, it names
  both `tools/` and `.claude/workflows/` as the population and still judges 3 files.
  Red when: the union was not built, or it changed gov's own verdict.
  figure: PINNED at 3, measured 2026-09-23.
- **AC5** — When a fixture installs `tools/workflows/check-review-join.sh` under a `scripts/` prefix
  and carries a ref-keyed join in a harness under `.claude/workflows/`, the gate exits `1` naming that
  harness; the a7c78ad2 bytes exit `1` with `no JavaScript under scripts/`.
  Red when: the harness directory is not in the population.
- **AC6** — When the same fixture carries a ref-keyed join in a file under `.claude/hooks/`,
  `tools/workflows/check-review-join.sh` does not name it.
  Red when: the union was widened to `.claude/` wholesale, which admits the hook ban tables.
- **AC7** — When a fixture holds no JavaScript under either the prefix or `.claude/workflows/`, the
  refusal printed by `tools/workflows/check-review-join.sh` names both directories.
  Red when: the message still names only the prefix.
- **AC8** — When `git grep -n 'apply no marker filter' -- tools/workflows` runs, it returns no line
  describing `check-verifier-fanout.sh`.
  Red when: a carrier of the old split survives.
- **AC9** — After the bump, `bash tools/check-kit-versions.sh` exits `0`, and with one bumped marker
  reverted it exits non-zero naming that carrier.
  Red when: a marker was missed, since the gate is already green before the unit starts.

## 7. Gates

`verifier fan-out` · `review-join ban (no ref-keyed join)` · `workflow script syntax` · `verifier fan-out self-test` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `kit version markers`

New arm: `tools/workflows/check-verifier-fanout.test.sh` · a `mkfix` fixture whose only harness sits under `.claude/workflows/`, run against the a7c78ad2 gate first to observe `population is empty` · none
New arm: `tools/workflows/check-review-join.test.sh` · a fixture with a ref-keyed join under `.claude/workflows/` and one under `.claude/hooks/`, run against the a7c78ad2 gate first · none

## 8. Open questions

- **F1 — does review-join take a marker filter too, so both gates share one population rule?** It
  would let the prefix go as it does for verifier-fanout. Against it: review-join's arm 2 judges files
  that dispatch agents, and a helper that dispatches without declaring `meta` would leave the arm.
  Recommendation: no, keep the union; the two gates answer different questions.
  RESOLVED (owner, 2026-09-23): no, keep the union, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, measured against gov a7c78ad2, inCMS 1bc57da27 and nc f69e2ffb.
- rev-2 · 2026-09-23 · built. S3 moved: verifier-fanout has no `--explain`, so it names its
  population in the refusal only, and review-join's clean line names the union too, since it
  otherwise claimed `tools/` alone over a wider population. Review-harness bumped 1.8 to 1.9 (S5).

## 10. Reuse audit

The seam is the population discovery `discovered()` in `tools/workflows/check-workflow-syntax.js:36-45`,
which already selects by the `meta` marker with no prefix; S1 makes verifier-fanout the same shape,
and S2 reuses the rung-3 literal convention at `tools/workflows/check-review-join.sh:76-79`.
`tools/codebase-map/reuse_lookup.py` was run and scans no `.sh`, so it ranked only unrelated Python
`derive_*` functions; no existing seam fits beyond the one named here.

Recall terms used: `population prefix KIT_PREFIX POP_RE claude/workflows harness marker meta review-join verifier-fanout carve-out green-by-absence`.
