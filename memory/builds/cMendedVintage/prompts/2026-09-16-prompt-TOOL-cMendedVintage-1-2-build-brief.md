# Build brief — TOOL-cMendedVintage-1

**Serves:** journal TOOL-cMendedVintage-1

memory-tree gets the `--render` mode it is the only rendered-row kit without. Read the spec whole
first.

*A note on this brief's standing. Two earlier briefs in this build asserted a mechanism I had not
measured, and both were wrong — a claim about which bytes a failed `checkout-index` leaves on disk,
and a claim that `classify_outcome` matched on one term when it already required all of them. Both
cost a builder time to disprove. So: everything below that I have not run is marked UNVERIFIED, and
where it matters you measure before you act on it.*

## Why this unit exists at all

`update`'s re-render step can only run a `[[regenerate]]` argv, and a kit can only declare one if
its adopter has an entrypoint that actually re-renders. Three kits had one and got their declaration
in `DEPL-cMendedVintage-5`. memory-tree did not: its adopter accepts only `--scaffold`, and on an
adopted tree that branch prints "already scaffolded — nothing to do" and exits 0. So its four
rendered rows — `HYGIENE.md`, `TEMPLATE-SPEC.md`, `guides/BUILD-METHOD.md`,
`guides/ANNOTATION-STYLE.md` — go one vintage stale on every update with nothing able to refresh
them.

This is also the unit `DEPL-cMendedVintage-8` waits on: that unit's gate reds this repo until a
descriptor shipping rendered rows declares a regenerate, and memory-tree is the last one that
cannot.

## The trap S2 names, and it is the whole risk here

The scaffold path has a create-from-nothing fallback: when `HYGIENE.template.md` is absent it writes
a one-line stub. Carrying that into `--render` unchanged would mean a render run on a tree whose
template is missing silently REPLACES an adopter's committed `HYGIENE.md` with a stub. That is
destroying a file the target owns, from the verb whose whole job is refreshing it.

S2 makes it a refusal under `--render` and keeps it under `--scaffold` alone. Extract the shared
render set, but do not let the fallback ride along with it.

## Bounds

Four rendered rows, one function, both modes calling it — the point of the extraction is that the
set cannot diverge between the two modes, so do not leave a fifth render reachable from only one.

Do not touch the `.memory-tree.conf` or `READINESS_ROWS` refusals that run before either mode; S3
puts `--render` after them deliberately.

## Traps this build has measured, carried forward

If you add a function, lead it with a declared verb from `.lexicon.conf`. The offender pin is a
two-sided equality and one non-conforming name reds an unguarded merge-bar leg — that happened here
once from a fixture helper.

Do not spell a `tools/<kit>/…` path in any file this kit ships, including prose in a README. The
carried-prefix arm is a BAN: a count may fall and never rise, so `--write-ratchet` is not a remedy.
That also happened here once, in a README sentence, one unit ago.

A fixture can stage a condition the tool does not actually refuse — confirm a RED is the red you
meant. A first cut can be vacuously green when the artifact it inspects is absent.
