**Serves:** research PLAY-dOrderedCharter-37

# Brief: spec 37 — fold the pre-check's findings before its builder runs

## The prompt

> why are the specs being reviews (and 11 times at that) instead of building?

— owner, 2026-11-09. A read-only pre-check of spec 37 against HEAD found what its builder would have handed back. This folds them while
unit 31 builds.

## The brief

### Goal

Revise spec 37 so a builder can build it as written over this tree, folding every finding below.

### Items

1. **Where you write.** A unit is building, so edit only this scratch copy and write nothing under the repository:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold37/2026-10-23-spec-PLAY-dOrderedCharter-37.md`
2. **H1, the units page's empty population.** No tracked overlay holds a unit row and the unit reader returns none, so S3 refuses the units
   page and AC1 cannot exit 0. Move the units reference row and its page into F8's later commit, after PLAY-dOrderedCharter-40's rows are
   tracked; AC1 and AC10 split the same way.
3. **H2, the unit-tag check.** No `unit.` tag resolves until unit 40, so a check over the pages' unit lines reds the docs leg or grades an
   empty population. Name the check in S4, land it and the unit lines with unit 40's rows (or have it print a non-verdict over an empty
   namespace), and make AC8 require a population of at least one.
4. **H3, the run arm over today's pages.** Seven existing help pages hold fenced commands that run gov-tree paths or carry placeholders a
   shell reads as redirects, and the scratch adopter holds only a README. List those pages in Files touched with a `run: no` marker or a
   rewrite per block, and narrow the non-goal on rewriting today's pages to their run markers.
5. **H4, a usage shape for drive, kind and unit rows.** The docs leg's shapes have no fit, and a page-shaped anchor carrying a fingerprint
   reads stale. Resolve the shape under the fork rule, and reconcile the non-goals' "one row source" with S5's "no row source here".
6. **M1, wire the new checks.** No leg runs `--reference --check` or `--run`. Add them to a leg in `tools/gate-legs.json`, put it in
   Files touched and name them in the leg line.
7. **M2, the drive plant.** The start stage's main role holds several rows, so removing one vanishes no member. Make the plant remove a
   whole single-row group, and reword the risks line to "a stage and role that vanishes".
8. **M3, AC5's red.** A renderer copying the fingerprint function produces identical lines. Give AC5 a staged break that can fail, or a
   static assertion that the renderer holds no hashing.
9. **M4, the run arm's bash.** Call the govkit kit's inlined `resolve_bash` rather than a bare `bash -c`.
10. **L1 to L3.** Say the rendered usage resolves `{prefix}` and to what; name the three reader adapters the registries need; correct the
    stale citations by moving to `path#symbol` and the drifted counts by pinning them; make AC3, AC5, AC6 and AC8 runnable from the
    repository root; and give `--reference` a root or target override if AC1 and AC9 plant into a scratch copy.
11. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

Resolve each choice under the fork rule and record it in section 8.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte unless an item above corrects it, and new text cites code as `path#symbol`,
  outside the acceptance bullets, which spell plain tracked paths and never a file not yet tracked. New text names a section in words,
  and a check by what it checks. A sha written in section 2 stays out of backticks, and a Readers clause names readers only, never the
  command that found them. Every new fact is pinned, keyed or marked PINNED or DERIVED; name a unit by its id. Every function name it
  mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- Any retirement word in section 2 owes its Readers clause.

### Acceptance

- Spec 37 builds as written over HEAD, every edge it gains is mirrored in your return for the main loop, and each change has a history
  line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### Gates

None run: this is a scratch edit. The main loop sweeps the spec before its dispatch.

### Non-goals

- No code. No edit outside the scratch copy.
