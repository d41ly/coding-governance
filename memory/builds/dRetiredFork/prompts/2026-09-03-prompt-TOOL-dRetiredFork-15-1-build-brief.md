# Build brief — TOOL-dRetiredFork-15

**Serves:** journal TOOL-dRetiredFork-15

## What this is

Four NicoCares carve-outs exist because a value a PROJECT owns is a literal in gov's checker, and a
fifth because check 4 does not consult the grandfather registry check 5 already reads. All five sit
in one file, which already presets thirty values in one block and validates them in one loop. The
mechanism is present; these five were never added to it.

## The sites, located

- check 4's `vre = "^[A-Za-z][A-Za-z0-9-]*$"` — the slug, hardcoded inside the awk
- check 3's `F:legacy-files.txt|F:curation-debt.txt)` case — the `memory/project/` whitelist
- check 21 branch A's `miss21` rows — the records with no `Serves` line
- check 5's `in_legacy()` — already reading `LEGACY_SET`, which check 4 does not consult
- check 7's `awk -v ecc=...` — where `length()` decides chars-or-bytes by locale, not by declaration

## AC0 is the criterion that matters, and it is why this is Tier-2

Two of these keys NARROW WHAT IS GRADED. `BUILD_SLUG_RE` is a predicate and `RECORD_SERVES_CUTOFF`
is a population date filter, so a bad value does not red — **it silently grades nothing and reports
green**. A regex matching the empty string admits every folder name; a cutoff dated in the future
excludes every record.

Both guards are owed BEFORE the keys are wired, and both REDs must be observed. That is the whole
difference between a declared key and a hole with a name.

`PROJECT_REGISTRY_EXTRA` only ADDS to a whitelist and is bounded by the tree's own contents, so it
carries no such risk. No key here sets a threshold on a violation count; §3 draws that line and this
unit stays on its side of it.

## Blank means gov's behaviour, for all five

An adopter who never edits `.memory-tree.conf` must see an identical run. That is AC1, and it is
checked byte-for-byte against a baseline captured before the first edit — gov's green output is two
lines, so the comparison is exact rather than approximate.

## F1's answer, folded

gov's own check-7 comment says it deliberately sets no locale, because pinning one "would silently
re-decide the cap on any adopter whose awk counts characters today". A DECLARED key with a blank
default re-decides nothing — that is the difference, and the comment gets quoted in the conf example
so the next reader sees why the default is blank rather than `chars`.

F2: a cutoff, not a 549-row grandfather list, matching the five cutoffs already in the conf.
