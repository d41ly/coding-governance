# Owner mandate — aGradedDialect

**Serves:** none — this is the owner's verbatim prompt, the authorization this run asserts. It
precedes every spec in the build, so it names no spec id.

## Provenance

Handed to `/unattended` as the `--prompt` value on 2026-09-10, node `a`. The value carried
whitespace and named no readable file, so it is the prompt ITSELF and is recorded verbatim below
rather than by reference. No path of origin exists to record.

## The prompt, verbatim

> The lexicon kit ships without TypeScript support at all. Research and design a thorough, flexible
> solution, build it per the protocol.

## What the run read into it, and what it did not

The build README states the scope in its own words; this section records only the two readings that
were not obvious from the sentence, so a later reader can tell a derivation from an invention.

- **"ships without TypeScript support at all" is accurate as written, and it is not an oversight.**
  `tools/lexicon/lexicon.py` ships `PATTERN_SETS` with exactly one entry, `js-regex`, and
  `KNOWN_EXTS` maps only `py`, `js` and `sh`. An adopter with `.ts`/`.tsx` gets `ts::dark tsx::dark`
  written into their own `.lexicon.conf` by `scaffold_lexicon.py` on the first run. That absence is
  a RATIFIED DECISION, `TOOL-dScaffoldedMirror-13`, with its evidence and its consequence recorded
  in `memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-13.md`.
- **The prompt is therefore read as the owner LIFTING that deferral, not as a bug report.** The
  deferral named its own revisit test — "revisit after `-8`, with fixtures extracted from real
  adopter files rather than authored" — and both halves now hold: `TOOL-dScaffoldedMirror-8` is
  CLOSED as of 2026-08-25, and the adopter corpus it was measured against is present on this node at
  `C:/projects/incms/main`, carrying 1257 tracked `.ts`/`.tsx` files. The run does not treat itself
  as overriding a decision; it treats itself as the session the decision asked for.

## What the run refused to read into it

- **No adoption of the kit on that adopter.** `-13` §3 says deciding what the kit says about `.ts`
  is a different act from installing it there, and the prompt does not ask for the second.
- **No new predicate.** "TypeScript support" is read as extraction and declaration, so the existing
  P1 and P2 predicates and the convention check reach a language they could not reach before. A
  fourth predicate would be a different build.
