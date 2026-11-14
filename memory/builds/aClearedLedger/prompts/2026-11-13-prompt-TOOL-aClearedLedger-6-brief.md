# Brief — aClearedLedger: unit 6's spec, two helper names the naming lexicon refuses

**Serves:** research TOOL-aClearedLedger-6

## The prompt

> This is a new build with its own slug and build folder, not more units of aNimbleMend; follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

## The brief

### Goal
DIVERGENCE: spec section 4 (S1 and S2, "spelled exactly so"), with section 2's S1/S2, the probes P1/P2 and AC1/AC2 that read those names by pattern, mandates two new shell functions named `_hs_lines` and `_engreads_of`. Neither leads with a declared verb, so the naming lexicon grades both as P1 verb offenders, and `VERB_OFFENDER_PIN="1208"` in `.lexicon.conf` is a two-sided equality the tree sits exactly on. Building the spec as written moves the count to 1210 and reds the naming leg; the only cure inside this pass would be a pin raise in `.lexicon.conf`, a path the spec's Files touched does not declare, or a rename, which breaks AC1, AC2, P1 and P2. The spec has to say one of two things: (a) verb-led names throughout sections 2, 4, 5 and 6, or (b) keep the names, add `.lexicon.conf` to Files touched, and state the pin moving 1208 to 1210 with its RE-MEASURED comment line and why two debt names are owed. Nothing was written, so nothing needed restoring; the tree is clean at base. <!-- PINNED 2026-11-13 -->

### Items
1. The main loop takes (a): no pin is raised. Rename the two helpers to verb-led names the lexicon answers OK for under `sh.function`, asked with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`; the builder found `extract_hs_lines` or `render_hs_lines` for S1 and `derive_engreads` for S2 acceptable. Carry the rename through sections 2, 4, 5 and 6, the probes P1 and P2, and the counts AC1 and AC2 read by pattern. The header moves to the next rev with a revision-log line naming the builder's divergence.
2. Where S4's comments in the conf example point at the memory-recall kit's README, they name it in words: a file under `tools/` may not spell another kit's path.
3. `python tools/check-spec-tokens.py --spec` over the spec exits 0. Change nothing else, commit nothing, render no index.

### Acceptance
The spec names no helper the lexicon refuses, and every probe and criterion reads the new names.

### Gates
The naming lexicon's `--suggest` over the two names, and the spec-token checker over this one spec.

### Non-goals
Any change to `.lexicon.conf`, any other edit to the spec, any sibling spec, any commit, any index render.

### Limitations
The writer commits nothing and regenerates no index; the main loop commits the revision and dispatches the unit again.

### Reuse
The spec itself at `memory/builds/aClearedLedger/spec/2026-11-13-spec-TOOL-aClearedLedger-6.md`.
