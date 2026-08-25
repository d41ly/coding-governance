**Serves:** journal TOOL-dFramedEntrypoint-1

# Owner dispositions of this build's parked decisions

*Node d, 2026-08-25, after the build landed at `60ba1d60`. Five decisions were parked during the run
and a sixth entry corrected one of them. Four were put to the owner and ruled; the fifth is still
open. Recorded here rather than in the build README, because a decision log is not entrypoint
content — which is the rule this build shipped.*

## Ruled

### 1. The bound population grows ORGANICALLY

**Ruling: each build's owner conforms their own README when they next touch it.** The contract binds
one file today and grows only with unrelated traffic; the 49 terminal builds never bind at all.

What this declines, stated because it was the recommendation: making the two judgement slots
`empty_ok` for pre-existing builds, which would have let live builds bind on shape alone without
anyone inventing a benefit their owner never claimed. The owner chose the slower path over the wider
one. **No follow-up work.** The registry's exempt rows already carry "drains when its build's owner
conforms it", which is now the literal policy rather than a placeholder.

### 2. The authored `roster:units` pair becomes MANDATORY and gated

**Ruling: gate its presence.** `build-complete` term 3 stops passing vacuously on 51 of 62 builds
and
becomes a real check, and `TOOL-aPacedTurnstile-14` closes.

**This is follow-up work and it is not small.** 51 build READMEs gain a pair; the gate needs a
presence assertion with its arm; the term's semantics change from "nothing to compare" to "compare,
and a planned unit with no spec is a finding". The pair also becomes a sixth authored region in a
README whose authored half this build just closed to five slots — so the canon and the pair have to
be reconciled, and unit 1's `scan_canon` already reserves a position for the pair without requiring
it. That reservation is what makes this ruling cheap to honour rather than a canon change.

### 3. `BUILD-METHOD.md`'s budget rises to 350 lines

**Ruling: raise it to 350.** Not one of the three options offered — the owner picked the raise and
set a different figure, which is the owner exercising exactly the authority M3's veto 2 reserves.

M1 declares the pair and no gate enforces it, which is why the file sat 2 lines over unnoticed. The
raise makes the current content legal with room; whether the pair ever gets a gate is now a separate
question nobody has been asked. Recorded plainly: this ruling fixes the breach and not the
blindness.

### 4. `dead-path-waivers.txt` keys on the surrounding line's TEXT

**Ruling: key on text, not on `<path>:<line>`.** Survives the failure that actually happens — an
insertion above the hit — and breaks only on rewording, which is rare and loud. Keeps per-hit
precision where a file carries several waived mentions, which the path-only alternative loses.

Evidence it earned: the line keying broke twice inside one build, and on the second occasion the
re-key was first done by PROXIMITY and scrambled three rows onto the wrong reasons.

## Still open

**`--plan` and `--status` disagree about which unit is next.** `--status` reads the generated units
region, which now sorts by build order, and `--plan` sorts tracked specs by id. Neither is wrong
about STATUS; they disagree about which unit each volunteers first. The fix lives in
`tools/unattended/`, a different kit with its own contract, and no ruling has been taken.

## Not a decision

The sixth parked entry is a CORRECTION, not a question: this run parked the lexicon naming leg as
red
at BASE and therefore not its to fix, and that was wrong. Measured with `git stash` on a tree whose
work was already committed, so stash dropped nothing and the reading was of HEAD. Re-measured in an
isolated worktree, BASE is green; the whole overage was this build's own functions, and it was fixed
by renaming twelve of them onto declared verbs with no pin raised.

## An id collision this record has to own

The four rows above were first filed as `TOOL-dFramedEntrypoint-2` through `-5`, which are the ids
of four CLOSED specs in this same build. Section 2's rule is that `<seq>` is the numeric max of your
own ids in that family plus one, and the max was 9; I took the next four unused-looking numbers
instead of deriving them. Renumbered to 10 through 13 before anything cited them. The hygiene gate
did not catch it, and it would not: a backlog row CITING an id is not a second DEFINITION of it, so
checks 13 and 14 both read this as legal. The collision is semantic and the only reader who would
have noticed is a person following the id to the wrong document.
