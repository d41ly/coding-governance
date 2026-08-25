**Serves:** journal TOOL-dFramedEntrypoint-1

# Owner rulings, 2026-08-24

*Four forks put to the owner after the research fan and its adversarial verification, and ruled the
same day. Recorded here rather than in the build README because this build's whole subject is that a
decision log is not entrypoint content. The rulings bind every spec in this build.*

## Fork 1 — which population the contract binds

**Ruling: a declared registry, seeded from the conforming subset.**

The registry takes the shape this repo already ships at `memory/project/method-carriers.txt` with
`tools/memory-tree/check-method-carriers.sh`: asserted in BOTH directions, so an undeclared build
README reds and a row naming a path that no longer exists reds too.

Why the three alternatives lost. A date-keyed cutoff was refused on measurement: every date key
exempts all 61 tracked build READMEs on the day it is set, and the population guard is blind to date
vacuity because it counts the population before the date filter, so a cutoff governing zero files
reports green. Ceilings at the measured p90 would land green but sit loose enough to permit most of
what the owner objected to. Tight ceilings over the whole corpus would open the largest waiver
registry this repo has ever had, at roughly thirty rows.

## Fork 2 — what the authored slot set contains

**Ruling: the owner's four slots, plus a parked-decisions slot and the build's goal bound.**

The four are the immutable description, expected improvements, detriments if not built, and
build-level rules. The two additions exist because the build method mandates authored README content
that the owner's four cannot hold: parked decisions are written by one method section, read by a
resuming session in another, and rolled up for the owner in a third.

Parks are NOT derived from a spec's open-questions section. That was tested and refuted three ways,
and the builds that carry parks today mark those sections `none` and point at the README, so a
derivation would render an empty park list for every build that has one.

Parks are authored prose for the irreducible triple — the question, the options seen, and the reason
it was not decided — and carry ZERO authored counts and zero authored status summaries. The one
measured park corpus in this tree rotted on both of its hand-counted numbers, and the charter already
forbids writing a count of a derived population in prose.

## Fork 3 — what leaves the build README

**Ruling: delete both generated regions, and render each record inside the spec it serves.**

The document inventory region is near-pure duplication and has no executable reader outside the
generator. The records table is a separate decision with a real cost: it carries every over-cap
generated line in the corpus, and it holds the only spec-to-record coverage signal this repo has,
because the hygiene check that grades bindings grades the other direction. Both coverage joins must
therefore be re-emitted rather than deleted with the table.

The inverse rendering was measured feasible before the ruling: a generated marker pair placed between
a spec's status header and its first numbered section passes the spec-format check on a scratch
clone, needs no new section, and needs no canon cutoff.

## Fork 4 — how the budgets fail, and what happens to immutability

**Ruling: a hard declared ceiling plus an advisory high-water; immutability is documented, not gated.**

The shape is the one `tools/check-template-size.sh` already implements, and both halves are copied:
a hard per-subject ceiling that exits non-zero, and a high-water ratchet that never touches the exit
code.

Immutability of the description is a claim about history, and no mechanism for it has a green
starting state: 26 of the 61 description blocks in the corpus already carry more than one commit, so
a history-based gate reds 43% of the tree at HEAD. Nothing in this repo enforces the append-only rule
on its own decision log either, and that is the precedent the ruling follows.

## What was NOT ruled, and is parked

The authored roster marker pair is live on ten builds and is the only structure in the kit that can
express a planned unit with no spec yet. Its single reader feeds the planning verb's missing-unit
report and one Definition-of-Done term, and that term is overridable and passes vacuously on 51 of 61
builds. Whether to make the pair mandatory and turn the term into a real check, or to delete the
reader, the report and the term together, is an owner decision this build does not take. It is
carried as this build's park.
