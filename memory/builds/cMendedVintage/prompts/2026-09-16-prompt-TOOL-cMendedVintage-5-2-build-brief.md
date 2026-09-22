# Build brief — TOOL-cMendedVintage-5

**Serves:** journal TOOL-cMendedVintage-5

The carried-prefix ban is blind to the commonest spelling of the defect it exists to catch. Read the
spec whole first.

*Standing note: briefs in this build have carried six claims measurement disproved. Anything below I
have not run is marked UNVERIFIED.*

## Why this unit is sequenced HERE and not earlier

`re_ship` excludes `-` from the class of characters that may precede a carried `tools/…` literal, so
the entire `${VAR:-tools/path}` family is invisible: a variable that resolves at one prefix with a
hardcoded fallback that resolves only at gov's.

`TOOL-cMendedVintage-4` just deleted eight of those tails from `check-wiring.sh`. Its own §3 edge
states the constraint you inherit: **your rebaseline is one-shot and blesses whatever is in the tree
when it runs.** Had you gone first, it would have blessed the eight tails that unit removed, and the
class would have gone invisible again behind a ratchet that now called them normal.

So the deletions land first and the widened predicate second. That ordering is the unit.

## The measurement that decides the shape, and it is already taken

I ran the candidate predicates over the real tree before this build began, and the spec carries the
result: dropping `-` adds **11** occurrences and every one is the real defect shape — `${smerge:-…}`,
`${1:-tools/agent-cap-restatement-waivers.txt}`, `${DECL:-tools/line-length-limits.txt}`.

Dropping `/` as well adds roughly **240**, dominated by CORRECT `<gov>/tools/…` spellings that name
gov's own checkout, where `tools/` is the true path. **Do not drop `/`.** A rebaseline that blessed
those 240 would permanently bless them and then red every future legitimate `<gov>/tools/…` line.

Re-measure both before you edit — the tree has moved fifteen units since I took those numbers, and
if they differ the spec's §4 is wrong and says so in §9.

## The trap the previous unit found in its own new bytes

A COMMENT quoting a dead spelling is itself a carried literal: a backtick is not in the predicate's
excluded lead class. `TOOL-cMendedVintage-4` wrote two comments explaining what it had removed and
held its own file's count at 3 until it reworded them. Your unit is entirely about this predicate, so
anything you write explaining it is the likeliest thing in the build to trip it. Check your own diff
against the widened predicate before committing.

Its test arm hit the mirror image: a negative assertion spelling a full filename would have RAISED
that suite's row, which `--write-ratchet` cannot absorb. Stop a pattern before the extension.

## The rebaseline is one-shot — order within your own commit matters

Widen the predicate, bump `PREDICATE_EPOCH`, THEN rebaseline, then stage a break and confirm RED.
Rebaselining before the bump records the old epoch's population under the new epoch's name.

## Required of every unit now

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-TOOL-cMendedVintage-5-acceptance-ledger.md` per the
"Acceptance ledger" section of `memory/HYGIENE.md`. Record any criterion you could not observe as
OWED. Keep every backticked span whole on its own line — check 23 harvests per line and a wrapped
span joins nothing, found twice in this build already.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`. Re-declare with `--dispatch` if your
write set grows. The machine is heavily loaded: bound every command at 900s or more.
