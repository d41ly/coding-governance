# TOOL-dRetiredFork-20 — a spec lint resolves a spec's own machine-facing tokens

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 0 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

PROMOTED from spec-audit round 2, blocker 4, and it is the gate the review names under seven
separate findings. `TOOL-dRetiredFork-14` AC3 ends "Observed via `bash .claude/hooks/agent-cap.test.sh`"
while AC5, three lines below, names the tracked `bash tools/hooks/agent-cap.test.sh`. Round 1's B4
fold corrected AC5 and left the byte-identical string in AC3. **That is `AGENTS.md` §7's "gate the
CLASS, not the instance", broken inside the fold that enforces it** — and worse than a stale path,
because `TOOL-dRetiredFork-14` S2 withdraws that entire destination, so the witness will exist less
after the unit lands than before it.

Verified at HEAD: `git ls-files .claude/hooks/` returns `agent-cap.js`, `recall-opened.js` and
`scratch-guard.js`, and no test file exists there on disk either. AC3 is the only criterion observing
S3's self-arming parity arm, so the unit's highest-risk behaviour is graded by a command nobody can
run.

Three sessions of this build have now hand-verified spec tokens that a lint should verify. This unit
stops that.

## 2. Scope (IN)

- **S1** — Correct `TOOL-dRetiredFork-14` AC3's observation to `bash tools/hooks/agent-cap.test.sh`,
  and correct its rev-2 log line, which currently says B4 touched AC5 and overstates the fold.
- **S2** — Sweep the CLASS, not the instance: every §6 criterion in every spec under
  `memory/builds/*/spec/`, not only the one the review named.
- **S3** — The lint, over a spec's own machine-facing tokens, in three joins the tree already owns:
  a §7 gate name against `tools/gate-legs.json`; a backticked path-shaped token in a §6 criterion
  against `git ls-files`; a `path:line` citation anywhere in the spec against that file's line count.
- **S4** — A declared, shrink-only exception registry for paths a unit is deliberately about to
  create, with a reason per row. Without it every unit that adds a file reds itself, which is how a
  lint stops being run.
- **S5** — Observe the RED before wiring: stage AC3's original untracked path, confirm the lint reds
  naming file, section and token, unstage.
- **S6** — Run the candidate predicate over every tracked spec BEFORE wiring, printing hits AND
  near-misses, and disposition each. This build's own set is 30 specs and the corpus is larger; a
  lint landing over an undrained population is the state `TOOL-dRetiredFork-17` §4 warns against.
- **S7** — The leg declares a wall-clock ceiling in `tools/gate-legs.json` and carries its
  `memory/project/testsuite-count-waivers.txt` row if its suite prints no assertion count.

## 3. Non-goals (OUT)

- Resolving a pinned argv's FLAGS against the program's refusal paths. Round 2 proposes it for
  blocker 2 and it is far deeper than a tree join; `DEPL-dRetiredFork-9` records it as a documented
  manual check instead.
- Grading whether a cited line SAYS what the spec claims. The lint resolves existence and range
  only, and its header must say so — a structural check that reads as a semantic one is the class
  `AGENTS.md` §7 names first.
- Kit-descriptor placeholder checks. Those are `TOOL-dRetiredFork-19`; the split is by subject, this
  one's being specs.

## 4. Design

### Data model

Three predicates, one population. A token is machine-facing when it is backticked AND matches a path
shape, a `path:line` shape, or sits inside a §7 gate list. Everything else in a spec is prose and is
not this lint's business.

### Migration

The exception registry ships EMPTY and the S6 run decides its first rows. A registry seeded at the
size of the problem is a ratchet with a worse name, which is `TOOL-dRetiredFork-17` F2's argument
one level over.

### Alternatives rejected

Grading only the specs in this build. The defect class is the corpus's, not this build's, and
`AGENTS.md` §7 says fixing one file and scanning only that file certifies coverage you do not have.

A pre-commit-only check. The specs move in records commits that a busy tree routes through a
worktree; the bar is where this binds.

## 5. Production-readiness checklist

- security — reads tracked files, runs nothing they name. The `path:line` join must not open a path
  a spec supplies without confirming `git ls-files` names it first.
- perf / scale — three greps and two joins over the tracked spec corpus; the declared ceiling is
  what makes the cost a verdict rather than an annoyance.
- a11y — N/A.
- i18n — read bytes with `newline=""` on both sides. A text-mode read rewrites lone CRs and would
  move a citation's line number, which is this repo's recorded `text-mode-read-eats-embedded-CR`
  class landing directly on a line-number check.
- error / empty / loading states — an empty spec population REFUSES; a spec with no machine-facing
  token is legal and silent.
- observability — the run names how many specs it graded, how many tokens it resolved and how many
  exception rows are live, so a growing exception list is visible without opening it.
- risks — a false red blocks every records commit repo-wide. S6's pre-wiring run is the mitigation
  and the near-miss list is the evidence it worked.
- testing + left-shift gates — S5's observed RED, plus arms for each of the three joins and for the
  exception registry's staleness.
- migration / rollback — additive leg; reverting is removing its manifest row.
- user docs — `memory/TEMPLATE-SPEC.md` gains one sentence naming the lint and its exception
  registry, so an author learns the rule before a red bar teaches it.

## 6. Acceptance criteria

- **AC1** — When a §6 criterion names a backticked path `git ls-files` does not track, the lint
  exits non-zero naming the spec, the section and the token; the RED is observed against
  `TOOL-dRetiredFork-14` AC3's original text before the lint is wired.
- **AC2** — When a §7 gate name is not a row in `tools/gate-legs.json`, the lint exits non-zero
  naming it. Round 1 found 18 such names across this build's set by hand.
- **AC3** — When a `path:line` citation names a line beyond that file's length, the lint exits
  non-zero. Round 2 found two false citations this arm would have caught.
- **AC4** — When the offending path carries a row in the exception registry with a reason, the lint
  exits `0` and prints the live exception count.
- **AC5** — When an exception row names a path `git ls-files` now tracks, or that no spec names any
  more, the lint exits non-zero — a stale exception cannot hide a real hit.
- **AC6** — When `memory/builds/*/spec/*.md` matches nothing, the lint REFUSES rather than passing.
- **AC7** — The S6 run over every tracked spec is recorded with hits and near-misses, and
  `TOOL-dRetiredFork-14` AC3 is corrected in the same landing.
- **AC8** — `bash tools/check-testsuite-counts.sh` exits `0` and the leg declares a ceiling.

## 7. Gates

`memory hygiene` · `build README slot contract` · `build-index selftest` ·
`testsuite counts (every bar self-test prints one)` · `install-prefix (shipped surface)`.

## 8. Open questions

- **F1 — does the lint ship as a memory-tree kit leg, or as a gov-only checker?** Every adopter
  keeps specs under the same grammar, so the class is theirs too; but the three joins read
  `tools/gate-legs.json`, whose path is prefix-dependent, and an adopter's gate manifest lives
  elsewhere. Recommendation: ship it in the memory-tree kit with the manifest path resolved rather
  than spelled, which is `TOOL-dRetiredFork-10`'s rule applied to a new file rather than an old one.
- **F2 — what counts as a path shape?** Too loose and every prose mention of a directory reds; too
  tight and `scripts/` cases slip through. Recommendation: require a slash AND an extension, or an
  exact match against a tracked path, and record the near-misses S6 produces as the calibration
  evidence rather than guessing twice.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. PROMOTED from spec-audit round 2 blocker 4 under BUILD-METHOD
  M4's disposition rule. `git ls-files .claude/hooks/` was run at `b0108f13`; the surviving AC3
  string was read in the file rather than taken from the review.

## 10. Reuse audit

No existing seam fits, and the near miss is worth naming: `python tools/codebase-map/reuse_lookup.py
"resolve a document's backticked tokens against the tree that owns them"` reports `resolve` at
fan-in 25 in `tools/memory-recall/recall_conf.py` and `owners_of` at fan-in 3 in
`tools/codebase-map/map_lib.py`, but both resolve CONFIG and MAP keys rather than document tokens,
and neither reads `git ls-files`. The closest live pattern is `tools/check-dead-paths.sh`, which
resolves carrier text against deletion history — the same shape against a different tree fact — and
its shrink-only waiver registry is the model S4 copies.

Recall terms used: `spec lint`, `gate-legs`, `git ls-files`, `citation`, `path:line`, `waiver`,
`shrink-only`, `near-miss`, `staged RED`, `token`, `acceptance criterion`, `class not instance`.
