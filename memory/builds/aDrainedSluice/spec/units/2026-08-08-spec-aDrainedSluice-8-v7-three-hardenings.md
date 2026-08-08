# TOOL-aDrainedSluice-8 — V7: three gates that could not see what they judge

**Status:** INPROGRESS · rev-2 · 2026-08-08 · node a · Tier-2 · base 76fcd09b · streams tooling

## 1. Goal

Three backlog rows share one shape: a gate whose INPUT is narrower than its claim. The JavaScript
gates cannot see an untracked file, `check-wiring.sh` cannot see a line-ending problem it is
otherwise perfectly placed to fix, and `hygiene-parity.test.sh` cannot tell a valid baseline from one
that predates the change it is comparing across.

## 2. Scope (IN)

- **S1** — `tools/workflows/check-review-join.sh` and `tools/workflows/check-workflow-syntax.js`
  select from `git ls-files --cached --others --exclude-standard`, so a NEW workflow script is judged
  the moment it exists rather than the moment it is staged. Ignored files stay ignored.
- **S2** — the widened population keeps both gates' empty-population failure: a discovery run that
  finds nothing still fails.
- **S3** — `tools/check-wiring.sh` gains a line-ending check over the paths `.gitattributes` pins
  `eol=lf` that are RENDERED and byte-compared. It reports CRLF in `--check`/`--session` and repairs
  it in `--fix`, by rewriting the file's bytes rather than by `git checkout` — the index normalises,
  so `git status` is clean and a checkout is a no-op.
- **S4** — the repair is bounded to paths that are tracked, carry an `eol=lf` attribute, AND are
  RENDERED by a gate that byte-compares them. Measured: the attribute alone covers 43 files, which is
  far wider than the data model's description and wider than any repair should reach on a
  `--fix`. The rendered set is derived from the kits that declare a render target, so the bound is a
  fact about the tree rather than a sentence in a spec.
- **S5** — `tools/memory-tree/hygiene-parity.test.sh` REFUSES a baseline older than the kit version
  whose behaviour it is comparing. It asserts byte-identity, and the 1.5 flatten deliberately changed
  the verdicts, so a pre-flatten baseline reports every difference as a failure — true and useless.
  The refusal names the reason and the earliest usable revision.
- **S6** — the earliest usable revision is DERIVED, not written down: the first commit in which
  `KIT_MEMORY_TREE_VERSION` reached the current major/minor. A hardcoded sha rots at the next bump.
- **S7** — each item gets an arm that exercises the DISCOVERY path, not the explicit-file path. Both
  JavaScript gates bypass git entirely when handed explicit paths, and every existing arm in their
  harness is explicit-file — so an arm written the usual way would test the code this unit does not
  change.
- **S7b** — the landing boundary is checked, not assumed. `.githooks/pre-push` requires the validated
  tree to BE the pushed tip and `tools/push-main.sh` gates on `git status --porcelain -uno`, which
  deliberately PERMITS untracked files at that boundary. Widening the JavaScript gates to untracked
  files therefore changes what a landing sees; the unit measures that before it lands, and if an
  untracked scratch file would red a legitimate push, the widening is scoped to `--check` runs rather
  than to the hook path.
- **S7c** — the parity floor's EMPTY case is defined. Measured, `git log -S` for the current version
  constant returns exactly one commit, and it is the flatten itself; when it returns none — a fresh
  clone with a shallow history, or a squashed import — the harness refuses with that as the reason
  rather than treating "no floor found" as "any baseline is fine".

## 3. Non-goals (OUT)

- Widening the memory-tree hygiene gate's population to untracked files. It judges the tracked
  corpus by design — a scratch file in `memory/` is not a memory record until it is staged, and the
  `--staged` leg already covers the commit boundary.
- Auto-repairing line endings anywhere outside the pinned-and-rendered set.
- Making `hygiene-parity.test.sh` a gate leg. It needs a baseline argument and is deliberately not
  wired; the refusal makes a wrong argument loud, which is the whole change.

## 4. Design

### Data model

```
JS gate population : git ls-files --cached --others --exclude-standard, filtered to tools/**/*.js
CRLF population    : tracked paths whose git attribute `eol` is `lf`, intersected with the files
                     a gate renders and byte-compares
parity floor       : first commit where KIT_MEMORY_TREE_VERSION == the current value
```

### Inventory

The backlog id leads the PROSE, never the table cell. A table row whose first cell is an id is an
ANCHOR — it DEFINES that id — so listing the three rows that way made this spec claim three ids that
belong to another build, and hygiene check 13 said so on the first run.

| File | Change | Drains |
|---|---|---|
| `check-review-join.sh`, `check-workflow-syntax.js` | population widens to untracked-not-ignored | the untracked-population row |
| `tools/check-wiring.sh` (+ its test) | CRLF detection and repair on pinned rendered files | the CRLF-self-heal row |
| `tools/memory-tree/hygiene-parity.test.sh` | refuses a baseline below the kit-version floor | the parity-baseline row |

### Migration

None.

### Rollout

One commit. The three items share a shape and no ordering constraint, and splitting them would
triple the bookkeeping for no revert granularity anyone wants.

### Files touched (estimate)

Four scripts, two tests.

### Alternatives rejected

- **Leave the JS gates tracked-only and document it.** Rejected: the row already documents it, and a
  documented blind spot in a gate is the thing this repo keeps a catalogue record about.
- **Repair CRLF with `git checkout -- <path>`.** Rejected: it is a NO-OP here. The index normalises
  on commit, so git believes the file is unchanged and refuses to rewrite it; the bytes must be
  rewritten directly. This was measured during the previous build, where `rm` plus `git checkout`
  was needed precisely because the plain checkout did nothing.
- **Pin the parity floor to a sha.** Rejected by S6: it rots at the next version bump, and the thing
  that actually defines the floor is the version constant.

## 5. Production-readiness checklist

- security — N/A across all three.
- perf / scale — one extra `git ls-files` flag, one `git check-attr` batch, one `git log -S`.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — the widened populations keep their empty-is-a-failure rule; a repo
  with no `eol=lf` pins reports nothing and is clean; a parity run with no baseline argument keeps its
  existing usage message.
- observability — the CRLF report names each file; the parity refusal names the floor and why.
- risks — S3 REWRITES file bytes. Bounded by S4 to tracked, attribute-pinned paths, and only under
  `--fix`; `--check` and `--session` report without touching anything.
- testing + left-shift gates — three arms, each asserting its own message.
- migration / rollback — one commit.
- user docs — the kit READMEs and `AGENTS.md`'s wiring bullet.

## 6. Acceptance criteria

- **AC1** — When an untracked, unignored `.js` under `tools/` reintroduces the banned join, the ban
  fails naming it — before it is staged.
- **AC2** — When a file is git-ignored, neither JavaScript gate looks at it.
- **AC3** — When a tracked `eol=lf`-pinned rendered file holds CRLF, `check-wiring.sh --check` reports
  it and `--fix` rewrites it to LF; a file without the attribute is untouched.
- **AC4** — When `check-wiring.sh --session` runs on a clean tree, it reports nothing new.
- **AC5** — When `hygiene-parity.test.sh` is given a baseline older than the kit-version floor, it
  refuses with a message naming the floor and the reason; a baseline at or after it runs normally.
- **AC6** — When the kit version is bumped, the floor moves with it and no sha is edited.
- **AC7** — When each item's arm runs, it asserts that item's own message and the harness prints its
  pass line last.

## 7. Gates

`bash tools/run-gates.sh`; the `review-join`, `workflow script syntax` and `check-wiring self-test`
legs carry this unit.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — should the CRLF repair be automatic in `--session`?** Options: repair on every session
  start, or report there and repair only under `--fix`. RESOLVED (owner, 2026-08-08): report in
  `--session`, repair in `--fix`. `--session` already auto-sets an UNSET `core.hooksPath` and never
  clobbers a set one; rewriting file bytes is a bigger act than setting an unset config, and the same
  restraint applies.
- **Fork B — how the parity floor is expressed.** Options: a sha, a date, or the version constant.
  RESOLVED (owner, 2026-08-08): the version constant, resolved to its first commit. It is the thing
  that actually defines when the verdicts changed, and it cannot go stale silently.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 2, four highs: N13 narrows the CRLF repair to the rendered set
  (the attribute alone is 43 files); N14 makes the arms exercise the discovery path, since both gates
  bypass git for explicit paths; N15 checks the widening against the landing boundary, which permits
  untracked files on purpose; N16 defines the parity floor's empty case.

## 10. Reuse audit

S1 changes one git invocation in each of two existing gates and leaves their structure alone. S3
extends `check-wiring.sh`, which already owns the three-state detect/report/repair shape for
`core.hooksPath`, the agent-cap hook and the recall opt-in — this is a fourth case in that existing
machinery, not a new tool, and it reuses `git check-attr` rather than re-deriving what
`.gitattributes` says. S5 adds a guard to a harness that already refuses a baseline identical to the
current file, which is the same class of refusal one step further out. No new file, no new leg.
