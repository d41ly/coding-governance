**Serves:** diff-review TOOL-aRepatriatedFork-31 TOOL-aRepatriatedFork-32 TOOL-aRepatriatedFork-35 TOOL-aRepatriatedFork-36 TOOL-aRepatriatedFork-37 TOOL-aRepatriatedFork-38

# aRepatriatedFork: Tier-2 closing diff review of units 31 to 38, round 1

*Node `a`, 2026-09-26. This reviews the six units landed on the build branch after round 2 of the
first closing review: the adopter-name ban and its drain (31, 35), check 21's cutoff rework (32), the
recall kit's convergence (36), the repair pointer the unattended suite derives (37) and the conf
readers that now drop a trailing comment the way bash does (38). Three primed finder lenses ran
(security and write paths, correctness and gate liveness, integration seams at the two adopters),
then one skeptic asked to refute each finding. Every reproduction ran in a scratch repo or a scratch
clone of an adopter under `$TEMP`; no adopter tree was written.*

**Range reviewed: `3cf05f29...b511423b`** (branch `branch/arepatriated-fork-build-e42158`, before
the history rewrite that put each unit's spec ahead of its code; the rewritten tip `176e1060` has the
same tree as `b511423b`).

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No finding survived the skeptic at BLOCKER or HIGH. S1, the one HIGH a finder raised, reproduced, but
its sink predates the range and reaching it needs commit rights that already run code, so it grades
LOW. What remains is one design fault seen from three sides (two receipt readers, a parity gate that
cannot see them, and a wiring join that ignores both), a hook that stopped being opt-in, and a set of
LOW reader and fixture gaps. Every finding is a MEDIUM or LOW and is FOLDED into its unit's spec as a
rev-3 bump, per the build method's severity rule.

## Review shape and run integrity

- **Raw findings:** 15. Confirmed 12, partial 3, refuted 0. One row of S3's table was refuted
  (`../evil.js` is refused by both readers) and the rest of S3 stands. **Precision 1.00** (15/15).
- **By final severity:** MEDIUM 4 (S4, S5, I1, I2), LOW 11.
- **Run integrity:** lenses 3/3 returned, the skeptic returned, 0 died, 0 duplicates at the verdict
  stage. The skeptic merged three clusters: {S3, S5, I1}, {S1, S2} and {I4 with the ship rule}.

## Findings, verdicts and dispositions

| id | finder severity | skeptic verdict | final | unit | disposition |
|---|---|---|---|---|---|
| S1 | HIGH | confirmed, severity down | LOW | 36 | FIXED — an owned receipt path is graded with govkit's `[[own]].path` rule and refused; a `$(...)` row is refused by both CLIs |
| S2 | MEDIUM | confirmed, severity down | LOW | 36 | FIXED — the same grade refuses `\` and any climb before containment |
| S3 | MEDIUM | partial | LOW | 36 | FIXED — one reader: check-wiring calls `settings-merge.py --resolve-hook`, and its awk parser is gone |
| S4 | MEDIUM | confirmed | MEDIUM | 36 | FIXED — an owned file named differently from the hook is refused, so a merge exits 2 and writes nothing |
| S5 | MEDIUM | confirmed | MEDIUM | 36 | FIXED — the parity claim is withdrawn from both headers and the hook-destinations gate; crafted-receipt arms grade the one reader |
| C1 | MEDIUM | partial | LOW | 32 | FIXED — check 21 prints graded, total and exempt counts every run and reds a pin above the graded count |
| C2 | LOW | confirmed | LOW | 32 | FIXED — the generator contract pins the `U` rows too |
| C3 | LOW | confirmed | LOW | 38 | FIXED — `read_conf_scalar` peels single quotes like bash |
| C4 | LOW | confirmed | LOW | 38 | FIXED — `K=#x` reads `#x` in every reader that split on a leading `#` |
| C5 | LOW | confirmed | LOW | 38 | FIXED — the lexicon arm asserts its fixture edit landed |
| I1 | MEDIUM | confirmed | MEDIUM | 36 | FIXED — `wired` joins on the hook's resolved path in the command; an entry running another copy is UNWIRED, named |
| I2 | MEDIUM | confirmed | MEDIUM | 36 | FIXED — the hand-off states inCMS's real route: copy gov's bytes, declare, then `adopt --re-adopt --write` |
| I3 | MEDIUM | confirmed, severity down | LOW | 36 | FIXED — nc named in the hand-off and filed as DEPL-aRepatriatedFork-23 |
| I4 | LOW | partial, wider than claimed | LOW | 36 | FIXED — the hook takes an `opt_in` rule and lands only where `with_hook = "yes"` is declared |
| I5 | LOW | confirmed | LOW | 32, 35 | HANDED OFF — no gov code change; the new nc update conflicts and the undated-legacy trap are in DEPL-aRepatriatedFork-23 |

## Owner rulings for this fold (2026-09-26)

- **The owned-hook seam is HARDENED, not removed**, against the skeptic's recommendation to delete
  it. One resolver, in `settings-merge.py`, which `check-wiring.sh` calls. It grades the owned path
  exactly as govkit grades an `[[own]].path` and refuses an owned file named differently from the
  hook. `wired` compares the command's path against the resolved one.
- **The recall hook stays OPT-IN.** It lands only at an adopter that asked for it, the three "lands
  dark" documents stay true, and an adopter that declined keeps a green wiring check.

## The design judgement, and why it was not taken

The skeptic judged the seam not worth five fixes, since neither adopter's copy needs to differ from
gov's. The owner ruled otherwise, and the fold implements the skeptic's own "minimum acceptable
version": one resolver, govkit's grade, and the name refusal. It keeps the skeptic's advice not to
re-read `deploy.toml` at an adopter, because govkit never travels there.

## Bar reds carried into the fold

These are not review findings; the bar reported them against the same range.

- **verdict epoch** — the memory-tree version was last bumped before a later memory-tree engine
  change. The fold bumps it at the tip, after its last engine change, in every carrier.
- **govkit selftest** — the `a6-unshipped` scratch gov, and three sibling builders, lacked
  `adopters.toml`, which arm 10 refuses. Folded into TOOL-aRepatriatedFork-36 S4.
- **run-gates evidence** — one arm failed once under heavy contention. The fold runs that leg alone
  and records whether it reproduces.
