# Build brief — TOOL-dRetiredFork-11

**Serves:** journal TOOL-dRetiredFork-11

**Recorded AFTER the pass, not before it.** The two units before this one took their brief first;
this one did not, and saying so is cheaper than a record that implies an order it did not have.

## What the unit is

`.githooks/pre-push` hardcodes `tools/` at five functional sites and ships VERBATIM to every
push-main adopter, so the defect ships with it. At any other prefix the fingerprint helper and the
leg-manifest diff resolve to nothing and the bar command names a script that does not exist. Forcing
predicates 6 and 7 then match NOTHING and never fire, so a manifest-wide change lands there scoped
against a green earned on a different leg set — green-by-absence, in the hook that decides whether
the authoritative bar is owed at all.

## What the first cut got wrong, measured

The probe was keyed on a `run-gates/` DIRECTORY, following NicoCares. gov's own pre-push fixtures
write a `gate-legs.json` and never create that directory, so the probe fell through to `scripts`,
the refusal fired, and twenty arms broke at once. **Keyed on the leg manifest instead** — the thing
predicates 6 and 7 actually read.

The refusal was also too wide. A tree with NO manifest anywhere is a legitimate case: a fresh
adopter, a project not running the bar, this hook's own fixtures. The refusal now fires only where a
manifest IS tracked but not at the resolved root, which is the actual silent failure.

## Placement, which NicoCares paid for

`GOV_KITROOT` is assigned immediately after the work tree is entered, above every use. NicoCares'
copy assigned it 57 lines below its first use and, under `set -u`, the raw-push refusal printed
`GOV_KITROOT: unbound variable` and nothing else — the one path whose job is to name the lander
destroyed its own remedy, and `bash -n` cannot see it.

## The control that matters

S4 asks for the failing case observed first. The strongest form available here is running the
PRE-CHANGE hook against the same fixture: it must NOT force where the new one does. That control
initially skipped in silence, because `git show HEAD:.githooks/pre-push` ran inside the scratch repo
rather than gov's and wrote an empty file. A control that quietly does not run is worse than none.
