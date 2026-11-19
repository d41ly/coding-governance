**Serves:** research TOOL-dTrackedAtlas-2

# Spec brief — TOOL-dTrackedAtlas-2: the Atlas renders the actual state

You author ONE spec and write no product code. Read first, whole: the build README
`memory/builds/dTrackedAtlas/README.md`, the prompt record
`memory/builds/dTrackedAtlas/prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md`, the committed spec of
TOOL-dTrackedAtlas-1 under `memory/builds/dTrackedAtlas/spec/` (its interface section is your contract: consume
the derivation through it, never re-derive a build's state), `memory/TEMPLATE-SPEC.md`, and
`memory/guides/BUILD-METHOD.md` at `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`,
`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`, `doc.build-method#m5-recall-and-reuse` and
`doc.build-method#m12-research-test-choose-when-the-solution-is-not-given`.

## The mechanism

The generator `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py` and its template
`…-atlas.html` render the actual state: a view per chain build (spec run, build run, landing merge, unit counts by
status, open forks, revisions, deviation records, claim, can-start), and per comparison area (`AREAS`) the landed
builds whose stages change that area's "today" since the 2026-10-14 baseline, with the as-built view
(`build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`) in place of v2's `[chain]` where the two differ. The
2026-10-14 measurements stay, labelled as the baseline and never presented as today.

## Facts and constraints

- Today the generator reads only dClosedLoop's records (`SOURCES`, `LAYER_RECORDS`, `AREAS`), skips every
  `-brief`, `-return-` and `-as-built` file by name, and regenerates byte-identical at `9e21ac760`. The as-built
  renderer's docstring (`…-asbuilt.py`) already says the atlas renders should read the view in place of the design
  record. The procedure and probes are `build/2026-10-16-build-PLAY-dClosedLoop-1-atlas-instruments.md`.
- `build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-atlas.md` states what an as-built atlas should show:
  read it, and say in §10 which of its points this unit takes and which it leaves.
- Unit 3 (specced beside you) adds a generation stamp and a staleness `--check` to the same generator; do not
  spec either. Name in §3 the generator functions you change, so unit 3 can avoid them.
- Keep every existing refusal (a row, section or event it cannot place still refuses) and every existing `--plant`
  case. The template keeps its own doctype, charset, viewport and body margin.
- No new file under `memory/builds/dClosedLoop/build/`; nothing under `tools/`. Never commit or publish the page.
- Acceptance: at `9e21ac760`, the page (written to a scratch path, never committed) names the six landed build
  runs with their merges and the two startable runs; an area whose stage a landed build covers shows that build;
  the baseline section reads as the baseline; a new `--check --plant <case>` that removes a landed build's state
  from the derived data reds, observed red before green. No gate, suite or bar in a criterion.
