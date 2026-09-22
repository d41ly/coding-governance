**Serves:** diff-review DEPL-dRetiredFork-1 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21

# Closing diff review — dRetiredFork

Tier-2 · node d · 2026-09-03 · subject: the cumulative diff `5e7f41d3...HEAD`, 95 code files,
+6320/−3781 (the 101 files under `memory/` are records and were excluded)

## Verdict: CLEAN WITH FIXES

Fourteen of the thirty confirmed findings were fixed in this pass, including every one that
made a live check vacuous, inverted a verdict, or blocked a push. The remaining sixteen are
filed with the reviewer's own evidence. Nothing confirmed is unaccounted for.

## Shape and cost

Five primed finder lenses, then adversarial verification batched into five skeptics — the batch
grows, the agent count does not. Ten agents, 2.02M subagent tokens, 643 tool calls, 33 minutes
wall.

| | |
|---|---|
| lenses returning | 5 / 5 |
| raw findings | 35 |
| after dedup | 35 |
| verifiers | 5 (the cap) |
| **confirmed** | **30** |
| refuted | 5 |
| precision | 0.86 |

Precision of 0.86 is far above the ~0.5 floor §8 sets for tightening scope before adding agents.
The lenses were primed with this project's own recurring defect classes rather than a generic list,
and with an explicit by-design exclusion list, which is what kept refuted noise to five.

## What the two mechanisms found independently

The full 93-leg bar ran concurrently and went RED at 8 legs. **Four defects were found by both, from
opposite directions** — the bar by execution, the review by reading:

- `$KIT_REL` inside quoted heredocs (`merge-rows.test.sh`, `check-pass-order.test.sh`)
- six bare `python` calls in `census.test.sh` against the repo-wide launcher ban
- ceilings authored in milliseconds against a field the runner reads as seconds

That overlap is the argument for running both. Neither is redundant: the bar found the
`adopt-memory-tree.sh` scaffolding regression the review missed, and the review found the two
vacuous `git_pathspec` checks and the inverted `check` verdict, which every leg on the bar reported
as green.

## The five that mattered most

1. **`git ls-files` and `git diff` reject `--pathspec-from-file`** — exit 129, EMPTY stdout, and the
   helper captures output with `check=False`. The LF-index verification read `""` and printed
   `0 not LF in the index` unconditionally; the pre-renormalize cleanliness guard could no longer
   fire. Two live checks turned vacuous *by the unit whose subject was vacuous checks*.
2. **`run_kit_check`'s outcome block inverted its own verdict.** `classify_outcome` returns a block
   only when its probe is satisfied, so re-asking `ok` failed five shipped descriptors that declare
   `code = 0` with no `ok` key. A correct install reported `landed-but-inert`; exit-0-by-absence
   still reported `adopted`. The two arms swapped, inside the fix written to unswap them.
3. **The BAN arms re-implemented the gate instead of invoking it.** Proven by staging the break the
   suite was written to catch: replacing the whole refusal with `if false; then` left every arm
   green and the suite closing PASS. This build's capstone, graded by a transcription of itself.
4. **The pre-push kit-root refusal preceded the default-branch classification**, so an adopter at a
   third prefix had *every* push refused — feature branches included — by a hook whose own header
   says other pushes do nothing, with no environment escape hatch.
5. **`check-wiring`'s agent-cap probe was the only one in the file without the `${KIT_REL:+…}`
   guard**, so a root install built an absolute `/hooks/agent-cap.js`, matched nothing, and printed
   `skip — not adopted` over a present, correctly wired hook. The one arm in that file where a false
   skip has a security shape.

## Disposition

Fourteen findings were fixed in this pass and are described in the commit that carries them.
Sixteen were promoted to backlog rows carrying the reviewer's own evidence verbatim rather than my
paraphrase — `TOOL-dRetiredFork-32` through `-40`, plus `-31`. Every confirmed finding is either
fixed or filed; the generator that produced the rows reported zero ungrouped leftovers, which is
how that claim is checked rather than asserted.

**Five refuted**, and one deserves recording because it was a SPLIT verdict rather than a miss: the
claim that the re-render decline path is unreachable was refuted on its first half (flag-gated
silence is documented intended behaviour, and the decline was measured firing) and confirmed on its
second (no descriptor declares `[[regenerate]]`, so the argv loop has never executed) — which was
already filed as `TOOL-dRetiredFork-29` before the review ran.

## What this says about the build's own method

Two of the five headline defects were introduced by units whose stated subject was that exact
defect class. That is not irony, it is the measurement: **a fold is unreviewed surface**, and a
change written to close a class is written by someone holding that class in mind and therefore
least likely to see it in their own diff. The closing review is the only pass that reads the fold.
