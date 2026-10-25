# TOOL-dPlacedRequest-57 — the version oracle's base is the observing run's own pinned BASE, never a sha a spec pins

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 29 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-57-deviation-571.md](../build/2026-10-25-build-TOOL-dPlacedRequest-57-deviation-571.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-57-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-57-promoted-fix-return.md) | research | TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-57-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-57-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 |
| [2026-10-25-review-TOOL-dPlacedRequest-57-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-57-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-5 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md`)
confirmed **finding 1 at HIGH**, its item **H1**. The same defect is reported by findings 8 and 21,
item **M1**, which `TOOL-dPlacedRequest-59` carries at MEDIUM. `TOOL-dPlacedRequest-54` S3 and AC1
pin the oracle's base to the literal `c63aabbb`, which is this spec run's pinned BASE (the `base:`
fact of `memory/builds/dPlacedRequest/RUN.md`). The README's first build-level rule makes this a spec
run that closes by carry-forward, landing as `merge: dPlacedRequest — land onto …`
(`tools/push-main.sh:880`), and the build run that builds unit 54 forks after that landing. There,
before `--prepare`, fact 1 finds the spec run's landing; its subject matches, it is not an ancestor
of `c63aabbb`, so the oracle walks the spec run's commits and exits 0. 54 AC1 expects exit 2, so it is
red on a correct build, and the own-merge test's protection against an earlier landing is inert.
Measured 2026-10-25 in this worktree: fact 1 returns `c63aabbb` itself, so 54 AC1 is green today only
because the merge found is the base. This unit repairs `TOOL-dPlacedRequest-54`, at order 28, so it
sits at order 29: every close-time read passes the base of the run doing the reading.

## 2. Scope (IN)

- **S1** — The base is read, never typed. A criterion that runs the oracle on this repo's history
  passes the observing run's pinned BASE, read from its run-state file's `## Run facts` section, the
  scope `fact` reads (`tools/unattended/unattended.sh:1359-1375`):
  `b=$(awk '/^## /{s=/^## Run facts/} s&&/^base: /{print $2; exit}' memory/builds/dPlacedRequest/RUN.md)`.
  An empty `b` reaches the oracle's own `base does not resolve` refusal. 54 S1 and S3 are restated to
  this read in place. Observed by AC1 and AC2.
- **S2** — One place names it. `TOOL-dPlacedRequest-44` AC1 carries S1's read as its base argument.
  `TOOL-dPlacedRequest-34` AC59, as unit 54 cuts it to one line pointing at 44 AC1, names no base of
  its own. Observed by AC2.
- **S3** — The criteria restated. 54 AC1 runs in the building run's worktree before `--prepare` with
  S1's base, expecting `version oracle: no prepared merge on HEAD` and exit 2; its scratch copy
  without the own-merge test prints a header naming the merge fact 1 finds, derived at observation.
  54 AC3 reads 34 AC59 for `TOOL-dPlacedRequest-44` and the prepared merge and no sha. 54, 44 and 34
  each take a rev bump with a §9 line naming this unit. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- No change to the own-merge test, the refusals or the walk: units 54 and 55.
- No default base inside the oracle: a defaulted base hides a missing argument and weakens the
  ancestor test (the review's M2).
- No new fixture row: 54 S2's fifth row stages an earlier own landing, and its read under an older
  base is finding 21's item of `TOOL-dPlacedRequest-59`; 54 §4's prose claim is finding 8's item there.
- No verb printing the base, and no new bug-class record: the closing review's left-shift decides one
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-54` — S1, S3, AC1 and AC3, which this unit restates to the observing run's base; without them there is no base argument to correct
- **consumes-from** `TOOL-dPlacedRequest-44` — AC1 as unit 54 leaves it, which this unit gives S1's base read
- **consumes-from** `TOOL-dPlacedRequest-34` — AC59 as unit 54 cuts it, from which this unit drops the base
- **hands-off** `TOOL-dPlacedRequest-56` — 34 AC59 without its base, after which that unit's item for finding 19 measures unit 34, so this pass runs first at their shared order
- **hands-off** `TOOL-dPlacedRequest-59` — S1's base read, which that unit's items for findings 2, 9 and 16 pass to every other oracle-running criterion, and for findings 8 and 21 state in 54's §4 prose and AC2
- **hands-off** `TOOL-dPlacedRequest-60` — AC2, whose read of 34 AC59 that unit bounds at the end of the bullet
- **hands-off** `TOOL-dPlacedRequest-61` — §1, S1, §4, §5, §10, AC1, AC2, the hands-off edge to 56 and the Files touched sentence on 44, which that unit's items for findings 3, 6, 7, 13, 14 and 21 amend

## 4. Design

### The read, at the close

```bash
b=$(awk '/^## /{s=/^## Run facts/} s&&/^base: /{print $2; exit}' memory/builds/dPlacedRequest/RUN.md)
git rev-parse -q --verify "$b^{commit}"     # the oracle's own first guard, unit 54 S1
# then the oracle as 44 §4 states it, with "$b" as its one argument
```

In the build run, every first-parent merge on HEAD before `--prepare` is an ancestor of that run's
BASE, the spec run's landing included, so the oracle refuses; after `--prepare` the prepared merge is
not, so it is walked. The read is the working file's, which at the close is the committed one.

### Evidence

- `memory/builds/dPlacedRequest/RUN.md` `## Run facts` reads `base:
  c63aabbb4a73d44315dd5dd1219ff1dac5055cf8` on 2026-10-25, written by `--preflight`; the build run's
  preflight writes its own.
- Measured 2026-10-25 on node a: `git rev-list --first-parent --min-parents=2 --max-count=1 HEAD`
  printed `c63aabbb4a73d44315dd5dd1219ff1dac5055cf8`, the base itself, and the awk read above printed
  the same sha. PINNED at that date.
- `tools/push-main.sh:880` writes the landing subject `merge: $SLUG — land onto $remote/$def at …`,
  the subject the own-merge test matches.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md`: S1, S3, AC1, AC3 and
  its §9 line
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md`: AC1 and its §9 line.
  `TOOL-dPlacedRequest-56` writes this file at the same order, so the two passes run in sequence,
  this one first, since 56's item for finding 19 measures unit 34 after this edit.
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md`: AC59 and its §9 line

### Alternatives rejected

- **The merge-base with `origin/main`.** It reads a tracking ref, the freshness 44 F1 rejected, and a
  fixture has no remote.
- **`read_pinned_base`** (`tools/unattended/unattended.sh:8110`). It is internal to the driver and
  reads committed blobs for a landing decision; a criterion at the close needs the same fact, which
  the working file already holds.
- **A base literal per run, rewritten at each preflight.** It is a fact typed beside the file that
  owns it.

## 5. Production-readiness checklist

- security — none: a read of local history and of the run-state file.
- perf / scale — one `awk` over a file of under a hundred lines, once at the close.
- error / empty / loading states — an absent file or `base:` line gives an empty `b`, which the
  oracle refuses with exit 2 and `base does not resolve`.
- observability — the oracle's refusal names what was missing.
- risks — a run-state file rewritten by hand with another base moves the read; the driver's own
  checks own that file.
- testing — the probes of §6.
- migration — none: criterion text.
- user docs — none: criterion text.

## 6. Acceptance criteria

- **AC1** — When, in the building run's worktree before `--prepare`, `b` is read by S1's `awk` and
  the oracle as 44 §4 states it runs with `"$b"`, `b` resolves by `git rev-parse --verify`, the
  oracle prints `version oracle: no prepared merge on HEAD` and exits 2, and a scratch copy without
  the own-merge test prints a header naming the merge `git rev-list --first-parent --min-parents=2
  --max-count=1 HEAD` returns.
  Red when: the base is a sha an earlier run pinned, and that run's landing merge is walked as this
  build's prepared merge.
  figure: `b` and the merge DERIVED at observation.
- **AC2** — When `sed -n '/^## 2\./,/^## 3\./p;/^## 6\./,/^## 7\./p' 2026-10-25-spec-TOOL-dPlacedRequest-54.md | grep -c c63aabbb`
  runs it prints 0; 44's AC1 bullet, extracted by `awk '/^- \*\*AC1\*\*/{f=1} f&&/^- \*\*AC2\*\*/{exit} f'`,
  names `RUN.md` and `## Run facts`; 34's AC59 bullet, extracted the same way, names
  `TOOL-dPlacedRequest-44` and holds no match for `grep -E '[0-9a-f]{8}'`; and 54, 44 and 34 each
  carry a §9 line naming `TOOL-dPlacedRequest-57`.
  Red when: a criterion that runs in a later run pins a sha observed in this one.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: the oracle is a criterion's command, observed once at the close.

## 8. Open questions

- **F1 — Where does a close-time criterion take the oracle's base from (S1)?** (a) The observing
  run's `base:` fact in its run-state file; (b) the merge-base of HEAD and `origin/main`; (c)
  `read_pinned_base` inside the driver; (d) a literal rewritten per run. (b) rests on a tracking
  ref's freshness; (c) is no verb a criterion can call; (d) is a typed copy of (a). RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the skeptic's corrected fix for finding 1. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-5 promotions, finding
  1 (HIGH, item H1, whose defect findings 8 and 21 of item M1 also report).
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edges to `TOOL-dPlacedRequest-60` and `TOOL-dPlacedRequest-61`, mirroring their consumes-from.

## 10. Reuse audit

The seam extended is the run-state file's `## Run facts` section and the scope its reader `fact`
gives it (`tools/unattended/unattended.sh:1359-1375`); the awk read copies that scope and adds no
reader to the driver. `python tools/codebase-map/reuse_lookup.py "read the running build's pinned
base from its run-state file"` ranked `read`, `read_text` and `run`, name stems only, none a base
reader a criterion can call: no existing seam fits beyond the run-state file itself. `python
tools/memory-recall/query.py "which base does a close-time criterion pass when it runs in a later run
than the one that wrote it"` returned TOOL-aUnmannedHelm-5 (an unresolved merge-base is a refusal,
which S1's empty read keeps), this audit's H1, `read_pinned_base` through TOOL-dSweptBranches-22, and
round 4's H2; none disagrees with source.

Recall terms used: pinned base run-state fact oracle own-merge ancestor landing spec run build run carry-forward
