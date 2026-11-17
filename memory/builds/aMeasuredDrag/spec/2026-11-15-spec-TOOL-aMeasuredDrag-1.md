# TOOL-aMeasuredDrag-1 — `--check-commit` reads its `Pass:` trailer before it walks any pass, and walks only the units the message names

**Status:** CLOSED · rev-2 · 2026-11-15 · node a · Tier-1 · base aebbb4a7 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aMeasuredDrag-1-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-evidence.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-evidence.md) | research | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-findings-adopters.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-findings-adopters.md) | research | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-findings-gate.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-findings-gate.md) | research | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-findings-hooks.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-findings-hooks.md) | research | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-findings-pipeline.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-findings-pipeline.md) | research | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-findings-process.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-findings-process.md) | research | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-findings-records.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-findings-records.md) | research | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-review-brief.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-review-brief.md) | research | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-runlog-6d98c39c.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-runlog-6d98c39c.md) | journal | TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 TOOL-aMeasuredDrag-12 |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-synthesis-brief.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-synthesis-brief.md) | research | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-1-verdicts.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-1-verdicts.md) | research | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-1-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-1-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-10-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-10-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-11-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-11-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-12-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-12-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-13-skeptic.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-13-skeptic.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-14-skeptic.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-14-skeptic.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-15-skeptic.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-15-skeptic.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-16-skeptic.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-16-skeptic.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-17-skeptic.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-17-skeptic.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-18-synthesizer.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-18-synthesizer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-19-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-19-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-2-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-2-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-20-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-20-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-3-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-3-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-4-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-4-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-5-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-5-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-6-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-6-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-7-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-7-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-8-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-8-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-9-researcher.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-9-researcher.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief.md) | research | TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 |
| [2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md](../reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md) | diff-review | TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-review-TOOL-aMeasuredDrag-1-performance.md](../reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-performance.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Brief item 1, findings pipeline-1 and pipeline-3 of the 2026-11-15 performance review. The
`commit-msg` hook's `--check-commit` asks `check_pass_open` of every current key of the run before it
reads the `Pass: none` that ends most checks, so a records commit pays one `pass_commit` walk per
dispatched unit for an answer it discards. This unit reads the trailer first and asks openness only
of the units the message names, with every exit status and printed line unchanged. The brief's
second half, the status test ahead of openness in `read_open_passes`, cannot keep its stderr lines
unchanged. F1 resolved it as option A: that reorder is parked for the owner with its price, and this
unit does not build it.

## 2. Scope (IN)

- **S1** — In `tools/unattended/unattended.sh#check_commit_message`, the `none` test
  (`tools/unattended/unattended.sh@eb567029d1:14311`) sits above the `head=` read (`:14301`) and
  the rows walk (`:14302-14310`). A message whose trailer carries the token `none` returns 0 and
  asks no pass. Observed by AC1 and AC2.
- **S2** — The rows walk keeps a key only when the message names its unit. With a non-empty
  trailer, the unit is one of its tokens, the same token test `for u in $trl` makes at `:14334`.
  With an empty trailer, the unit is a whole token of the subject through `id_in`, the test the
  refusal loop makes at `:14318`. `check_pass_open` and the `O` amend test run for kept keys only.
  Observed by AC1 and AC2.
- **S3** — The comment above `rows=` (`:14285-14300`) states the new order and that a key the
  message does not name is never asked. NOT OBSERVED: comment text, read by the focused
  self-review.
- **S4** — The unit's acceptance ledger records the before and after of AC3 beside its spawn
  baseline. Observed by AC3.

## 3. Non-goals (OUT)

- `read_open_passes` (`:14192-14211`) is not edited: F1 resolved as option A, and the status-first
  reorder is parked for the owner with the price F1 states. Its order is the stated design of
  TOOL-dGroundRules-66: openness is asked first so that "a closed key of a terminal unit prints
  nothing" (its spec, lines 127-128).
- `pass_commit` in `tools/unattended/lib-unattended.sh` is not edited. One `git log` walk shared by
  every key is the finding's second fix, and a cache of it is the review's section 5 work.
- `--dispatch`, `--audit` and the check 23 leg are not edited.
- What moves, stated rather than hidden: `pass_commit` prints a scratch-file refusal on stderr when
  `mktemp` fails (`lib-unattended.sh@a3e03db6b9:1059`). For a key whose unit the message does not
  name, that line is no longer printed, because that pass is no longer asked. Its answer was
  already unused. No other byte of stdout, stderr or exit status moves.

## 4. Design

The trailer `trl` and the subject `subj` are already parsed before the walk (`:14279`, `:14284`),
so the change is a move and a filter:

```bash
  case " $trl " in *" none "*) return 0 ;; esac     # moved up from :14311
  head=$(GIT rev-parse -q --verify HEAD 2>/dev/null)
  rows=$(read_pass_declarations "$rel" current | while IFS= read -r r; do
      [ -n "$r" ] || continue
      d=${r#* dispatch · item }; d=${d%% · reason *}
      # only a unit this message names is ever graded below
      if [ -n "${trl// /}" ]; then case " $trl " in *" ${d#* } "*) ;; *) continue ;; esac
      else id_in "$subj" "${d#* }" || continue; fi
      ...the o / O tests, unchanged...
    done)
```

Why it is exact. Past the walk, the rows are read in two places only. The empty-trailer loop
(`:14314-14322`) reads an `o` row only when `id_in "$subj"` holds for its unit. The trailer loop
(`:14334-14376`) reads rows only where `$2 == u` for a `u` in `$trl`, which is `decl`, `graded`
and the amend test. The filter keeps exactly those rows, in their order, so the first refusal
of the empty-trailer loop is the same row. `trl` holds only `[A-Za-z0-9-]` runs joined by spaces
(`:14280`), and a unit id holds the same characters, so the `case` token test is the `$2 == u`
equality.

### Files touched (estimate)

- `tools/unattended/unattended.sh`

## 5. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --check-commit <msg>` runs in this worktree
  over this run's record, once before the edit and once after, for four messages, the stdout,
  stderr and exit status of each pair are byte-identical (`cmp`). The four messages are: one
  ending `Pass: none`; a subject naming no unit with no trailer; a subject naming
  `TOOL-aMeasuredDrag-1` with no trailer, which refuses with code 49 while its pass is open; and
  one ending `Pass: TOOL-aMeasuredDrag-11`, which refuses with code 49 while that unit has no open
  pass.
  Red when: the filter drops a row a loop reads, and the refusal for the named open pass reads
  as a pass.
  fixture: the run-state file `memory/builds/aMeasuredDrag/RUN.md` holds the dispatch row of this
  unit from its `--dispatch` on. A dispatch row landing between the two captures voids the pair,
  and both are taken again.
- **AC2** — When `bash -x tools/unattended/unattended.sh --check-commit <msg>` runs after the edit,
  `grep -cE '^\++ pass_commit '` over its trace prints 0 for the `Pass: none` message and for the
  subject naming no unit, and at least 1 for the subject naming `TOOL-aMeasuredDrag-1`. Before the
  edit, the first two print at least 1.
  Red when: the `none` test sits below the walk again, or the walk asks a unit the message does
  not name.
  figure: every count is DERIVED from the trace at observation time.
- **AC3** — When the `Pass: none` message of AC1 is timed before and after the edit with `time`,
  each timing beside `time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)` taken in the
  same shell, the after is under the before, and the ledger records the three wall times.
  Red when: the after is not under the before, which means the walk still runs.
  figure: all three times are DERIVED at observation time and recorded with their commit sha.

## 6. Gates

`unattended kit gate` · `lexicon naming predicates` · `scratch-guard self-test` · `tier2-review self-test`

What the close runs, and no pass does: the merge bar once, which runs the `--check-commit` arms of
`tools/unattended/unattended.test.sh` (TOOL-aWindowedPass-3 and its closing review rounds, the `O`
amend case of TOOL-aWindowedPass-6 among them) through its selftest shards. No arm is added or moved.

## 7. Open questions

- **F1 — Does `read_open_passes` test status before openness, given that this moves stderr lines?**
  RESOLVED (agent, 2026-11-15, delegated): A — B moves stderr lines against the README's
  printed-line rule (M3 veto 1); the reorder is parked for the owner with its price.
  The brief orders the status test (`:14200-14208`) ahead of `check_pass_open` (`:14199`) and also
  orders that the stderr naming of keys a status skip releases is kept (`:14186`). Today only an
  OPEN key of a terminal or deferred unit is named, and deciding which keys are open is the walk
  the reorder exists to skip. On the review's measured case, dOrderedCharter, the walk was 71 s PINNED 2026-11-15
  PINNED (skeptic verdict, 2026-11-15) over 89 closed keys of terminal units.
  - Option A — leave `read_open_passes` as it is, build S1 to S4 only, and park the reorder in
    this run's record with this question, for the owner. Every byte is unchanged, and the
    `--dispatch` and `--audit` hours of pipeline-1 stay unrecovered.
  - Option B — status first, and every key of a terminal or deferred unit is named on stderr with
    no walk, open or closed. Stdout and every verdict and refusal are unchanged, and the suite's
    hit and miss arms at `tools/unattended/unattended.test.sh@ba1ce4cbde:9474-9516` still hold.
    Stderr gains one line per CLOSED key of such a unit, 89 PINNED (review, 2026-11-15) per
    `--dispatch` on that build, and the design sentence of TOOL-dGroundRules-66 is reversed.
    Taking B rewrites this spec: a scope item for the reorder, a criterion over the trace count
    of `check_pass_open` for a CLOSED unit's keys, and a rev-2 line.
  - Option C — status first, with terminal and deferred keys left out silently. The brief's own
    text refuses it.
  - Recommendation: A. Under doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority, B fails the first veto, because it moves printed
    lines against this build's non-goal and README rule "a unit whose spec finds it must move a
    verdict, refusal or printed line parks that change". A is the one survivor, and the park
    puts B in front of the owner with its price.

## 8. Revision log

- rev-1 · 2026-11-15 · initial draft from brief item 1 of the aMeasuredDrag brief.
- rev-2 · 2026-11-15 · §1 · §3 · §7 · F1 resolved as option A under the run's delegation
  (`2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief`): the `read_open_passes` reorder is parked
  for the owner, and no scope item or criterion grades it. S1 to S4 and AC1 to AC3 are unchanged.

## 9. Reuse audit

The seam is `check_commit_message` itself, edited in place, with the token rules it already uses:
`id_in` (`tools/unattended/lib-unattended.sh@a3e03db6b9:712`) and the trailer token split at `:14280`.
`python tools/codebase-map/reuse_lookup.py "skip a terminal unit before asking whether its
dispatched pass is open"` ranked name stems only (`before`, `units`, `skip`) and named no seam for
this behaviour, so the seam is named here from source. Recall returned TOOL-dGroundRules-66, whose
spec states why `read_open_passes` asks openness first (F1), and TOOL-aSwiftRefusal-3, which added
the deferred skip and its stderr line.

Recall terms used: `python tools/memory-recall/query.py "why does read_open_passes ask openness
before the terminal status skip" --terms "read_open_passes check_pass_open pass_commit terminal
deferred status skip released stderr dispatch audit check-commit trailer"`
