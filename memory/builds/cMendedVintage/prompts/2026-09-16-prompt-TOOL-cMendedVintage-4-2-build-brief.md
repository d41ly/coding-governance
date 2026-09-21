# Build brief — TOOL-cMendedVintage-4

**Serves:** journal TOOL-cMendedVintage-4

Three shipped files tell an operator to run a merger at a path that exists at no prefix but gov's
own. Read the spec whole first.

*Standing note: briefs in this build have carried six claims measurement disproved, and the units
that distrusted one found real pre-existing bugs. Anything below I have not run is marked
UNVERIFIED.*

## Your precondition landed one unit ago, and it changes what you will see

`TOOL-cMendedVintage-3` fixed the `.git` boundary walk, so `${KIT_REL:+…}` now yields the empty
prefix at a root install instead of a path assembled from directories above the tree. Its builder
reported one consequence directly relevant to you: **a root install now REACHES the agent-cap remedy
line at all**, which it previously never got to, and that line still reads `python3
tools/settings-merge.py`. Your unit is what makes it correct there.

So the ordering is real, not bookkeeping: spelling `${KIT_REL:+$KIT_REL/}` before that fix would have
replaced a dead literal with a wrong path.

## The three carriers, and the one that already gets it right

`tools/check-wiring.sh:353` resolves the merger at `tools/` or the repo root only, and eight emission
sites then carry a `:-tools/settings-merge.py` tail. `adopt-process-monitor.sh` hardcodes
`$ROOT/tools/settings-merge.py` two lines below fragment paths the same file derives correctly.
`adopt-memory-recall.sh` carries the same two-rung loop plus a hardcoded fallback, under a comment
describing a resolution the code no longer performs.

`tools/unattended/adopt-unattended.sh` is the exemplar — it derives `TOOL_ROOT` and spells the remedy
through it. Copy that shape rather than inventing a fourth.

## The ratchet is the trap here

Deleting literals makes counts FALL, and a fall is SLACK, which reds `--check` until the ratchet is
rewritten. So `bash tools/check-install-prefix.sh --write-ratchet` runs in the SAME commit and
`tools/install-prefix-carried.txt` is committed with it. Land the deletions without it and you ship a
red bar.

UNVERIFIED by me and worth checking rather than assuming: the spec's migration table predicts
`check-wiring.sh` 3 → 2 and `adopt-memory-recall.sh` 8 → 6, and predicts
`adopt-process-monitor.sh` stays at 5 because its `:219` literal is `/`-preceded and the predicate
never counted it. Measure the actual counts; if they differ, the table is wrong and says so in §9.

## Bounds

Do not touch `adopt-process-monitor.sh:16` — that is a usage line a human reads, its ratchet row's
fourth column already records the reason, and deriving it would hand the operator a variable to
expand. Do not widen the carried predicate; that is `TOOL-cMendedVintage-5`, sequenced after you for
the reason its own edge states — eight of the ten occurrences it would newly catch are the tails you
are deleting, so it must run after you or its one-shot rebaseline blesses them.

## Required of every unit now

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-TOOL-cMendedVintage-4-acceptance-ledger.md`, shape
per the "Acceptance ledger" section of `memory/HYGIENE.md`. Record a criterion you could not observe
as OWED rather than claiming it. **Keep every backticked span whole on its own line** — check 23
harvests tokens per line, so a span wrapping a line break joins nothing, and that has already been
found twice in this build's ledgers.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`. Re-declare with `--dispatch` if your
write set grows. The machine is heavily loaded: bound every command at 900s or more and treat a
timeout as contention to report, not a failing check.
