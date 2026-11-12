**Serves:** research PLAY-dOrderedCharter-35

# Brief: spec 35 — the builder's hand-back on the composer's names and four gaps

## The prompt

> Resume the build, it's no longer paused

— owner, 2026-11-08. Unit 35's builder handed back a divergence before writing any code, and the dispatch order gate holds every later
order behind it, so the spec is revised in place before its builder runs again.

## The brief

### Goal

Revise spec 35 so a builder can build it as written over this tree, and every spec of this build that names its composer agrees.

### Items

1. **The composer's names fail the naming lexicon.** `lexicon.py --suggest` refuses `compose_rows` (`compose` is not a declared verb) and
   answers `apply_row_patch` with `set_row_patch`. The main loop's ruling for this build: rename them `derive_row_composition` and
   `set_row_patch`, which both pass, in spec 35 and in every spec of this build that names them (33, 36 and 49 do), with a history line
   in each. Specs of other builds that name `compose_rows` (dDeclaredLoop, dBoundRoles, dWitnessedBar, dShippedRelease) are not edited:
   spec 35 states the rename once, in a line those builds' own regrounding reads.
2. **The overlay reader.** S1 says `read_overlay_rows` reads through unit 32's reader and parses no TOML itself, but
   `tools/playbook/overlay.py#read_overlay` returns only the unit and policy rows. Say which field the overlay record gains for its other
   tables, and add `tools/playbook/overlay.py` to Files touched.
3. **The schema field grammar.** S10 and section 3 leave field declarations to unit 36, yet S3 and the data model must tell set fields from
   scalars now to refuse an `add` or `remove` naming a scalar or an undeclared field. State the minimal field grammar this unit reads, and
   hand the rest to 36 by an edge 36 mirrors.
4. **The schema path.** Say what the kinds register's `schema` path is relative to.
5. **The shared schema reader.** `check_owned` and the composer both need each kind's owner seat: put one shared reader in the inventory,
   reusing `tools/playbook/pins.py#read_row_kinds` where it fits, its name passing the lexicon.
6. **No extractor for overlay rows.** The owned clause keys on a definition sourced from the overlay, but no namespace extractor indexes
   the overlay's row tables. Say who supplies that extractor for a real kind, or narrow the clause to what this unit observes.
7. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

Resolve each choice under the fork rule and record it in section 8.

In each spec you change:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks. A sha
  written in section 2 stays out of backticks. Every new fact a record states is pinned, keyed or marked PINNED or DERIVED; a number
  beside a unit or spec number reads as a fact, so name a unit by its id.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Spec 35 builds as written over HEAD, every edge it gains is mirrored, the renamed names agree across this build's specs, and each change
  has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### Gates

Memory hygiene, as your role runs it.

### Non-goals

- No code. No edit to a spec outside this build, and within it none but 33, 35, 36 and 49.
