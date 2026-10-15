# Kit review: the lexicon

**Serves:** research PLAY-dClosedLoop-1

The owner asked for a full review of the lexicon kit under the new architecture, with an upgrade and
its own codebase integration. The review follows the memory round
(`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`), which set `lexicon.pin` to
`shrink-only` and recorded `gap-mem-10` against dTotalRecall.

Three researchers measure the kit in parallel: dispatches 27 to 29. Their returns are saved verbatim
beside this record, and the design is written here once they return.

## [words] The owner's words, 2026-10-15

> Lexicon needs a full review under the new architecture and an upgrade and codebase integration of
> its own: currently, agentic sessions keep raising its offender pin as a default mechanism for verbs
> that are not actually 'debt' - they are built-in verbs from the 3rd party kits and changing them is
> innately impossible. The kit has to account for that by default and provide agents a clear
> mechanism with how to exclude these verbs from debt and perhaps pre-built tables of verbs per
> popular kits. Additionally, the mechanism of enforcing naming conventions should be reviewed and
> improved where possible. The goal of the Lexicon kit is to ensure that conventions and names are
> consistent and don't drift.

## [settled] What the design already fixes

- **Layers.** The lexicon belongs to the Knowledge expansion (layers round one). The core never depends
  on it (P28).
- **The pin** (memory round, F4-8):
  - `lexicon.pin` defaults to `shrink-only`.
  - `absorb` is allowed, and `velocity` uses it.
  - `no-gate` is allowed.
- **dTotalRecall owns the lexicon's work**, with `gap-mem-10`: the gate absorbs debt, its pin rising
  from 412 to 1,087 with one real drain in 60 days.
- **Point-of-use delivery** (P29). A builder's work order hands it what its item needs, keyed. The
  memory round names `--suggest` as the answer handed for new names.
- **The codebase map** reads definitions with the lexicon kit's own tokenizers
  (`map_extractors.py:306`), and the map is planned to grow callers and complete Python definitions.
- **The annotation grammar** (F4-2):
  - `gov:note` is voluntary.
  - `gov:feature` anchors are required wherever a reuse entry points.
  - The `gov:` marker family is already read by four gates.
- **What dispatch 25 measured:**
  - `.lexicon.conf` is 46,577 B. It holds 23 verb rows, 4 cells, 1 pin, the banned suffixes and the
    languages.
  - Two waiver files exist, of 8 lines each.
  - Agents ran the kit 1,305 times bare and 542 times with `--suggest` in 60 days.
  - The drift audit read `lexicon_marginal_offense_rate` at 584 of 4,948.

## [history] The builds that made the kit

- **dClosedLexicon** opened on 2026-08-16. Its README gives the kit's founding idea: a closed verb
  table, because "a verb you cannot pick is a responsibility you have not scoped". Three design
  choices followed:
  - a scaffold seed derived from the adopter's own corpus and then frozen;
  - vacuity armed twice;
  - the predicates shipped behind one opt-in kit.
- **aSurfacedLexicon** extended the kit. Two of its asks bear on this review:
  - `TOOL-aSurfacedLexicon-23` is the path-scoped selector. Two cells are un-armed for lack of it,
    because they graded `memory/builds/**` records.
  - `TOOL-aSurfacedLexicon-15` is the rename unit the pin was meant to fall with.

Neither build is live. Both are evidence; no chain build counts on them.

## [research] Dispatched, 2026-10-15

| # | Part | Handoff |
|---|---|---|
| 27 | the kit as built and as enforced: mechanics, enforcement points, exceptions, how the vocabulary changes | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-8-researcher.md` |
| 28 | the offender population and the pin's history: what is forced, what is debt, who raised the pin and why, naming drift | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-9-researcher.md` |
| 29 | prior art and the forced-name mechanism: how naming checkers treat names nobody can change, generated vocabulary tables per kit, override detection prototyped on this tree | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-10-researcher.md` |
