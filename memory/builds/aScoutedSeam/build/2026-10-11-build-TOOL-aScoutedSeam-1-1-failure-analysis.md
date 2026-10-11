**Serves:** research TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 TOOL-aScoutedSeam-3 KICK-aScoutedSeam-1 DEPL-aScoutedSeam-1

# Why build sessions reinvent seams that already exist — gov, inCMS and NicoCares

Measured 2026-10-11 on node `a` by this session and five read-only research agents, against gov at
`de383a31` and frozen clones of inCMS at `81800a0f9` and NicoCares at `ad71abd4`. Nothing was written
to either adopter. The ground-truth cases these findings rest on are
`2026-10-11-build-TOOL-aScoutedSeam-1-3-cases.json`; the arms that were measured on them are the
companion record `2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md`.

## The failure, in the three repositories

**inCMS, the media picker.** A modal media gallery landed in build aLucidVitrine on 2026-07-01: a
field factory `imageField` in `packages/blocks/src/fields/imageField.tsx`, a field
`MediaPickerField`, a bridge `useMediaPickerBridge` that lets `packages/blocks` reach the modal, and
the modal itself in `apps/web`. Between 07-03 and 07-20 five later builds gave an image property a
bare text box instead: the per-section decor texture, the DSL `designData` inspector, the hero
accents, the ProductCard block and the email image block. All five are still at inCMS HEAD. One
carries a code comment saying blocks cannot reach the picker, which was false at its parent: the
bridge existed for exactly that. Two controls from the same weeks were legitimately different (a
visitor file upload to a plugin upstream, and a text box that names an entry field).

**NicoCares, the design vocabulary.** The package carries a 101-token `--nc-*` layer in
`package/nicocares-v3/site-css/site.css`, about 132 `data-part` names, a shared product-card
generator `scripts/gen_product_card.py`, and the `quiz-intake` stage. inCMS core carries the DSL
vocabulary (`Eyebrow.bare`, `Button.variant`, `Section.width`, `Card{media,badge}`) and the theme
variables. Six traced builds re-expressed instead of reusing: three passes over the medical intake,
the account area, the plan cards and the API product carousel. Each was later consolidated after the
owner complained one to three times; the plan cards and the carousel had been told by a dossier that
"a third product surface adds a call, not a third copy", and forked anyway.

**gov itself.** Twelve verified reinventions across Python, shell, JavaScript and TOML: a second
process-table reader, a case normaliser duplicating `subtokens`, a second repo-root walk in
`agent-cap.js`, a private conf parser beside four others, a hand-kept terminal-phase set, and seven
more. Seven of the twelve missed seams are shell. Half were written below spec granularity, inside a
helper during a build or a fold, after §10 had already named an adjacent seam.

## What the existing tools do, and why they did not prevent it

| Tool | Mechanism | Why it did not catch these |
|---|---|---|
| `tools/codebase-map/reuse_lookup.py` | stem intersection between the query and symbol, inventory and dossier names, ordered by fan-in | a seam whose name shares no stem with the phrase cannot be seeded; precision was measured at about 0.05 (TOOL-aWeighedCompass-1) and a constant control beat it at every K (TOOL-dTracedLattice-1) |
| the codebase map inventories | public symbols plus declared key populations | CSS custom properties, unexported components, class methods, DSL vocabulary and product markdown are not inventoried; NicoCares declares no symbol tier at all |
| `tools/memory-recall/query.py` | BM25 over decision records with caller-written terms | it indexes records, never code; its live §10 probes hit 25 of 99 at @10 |
| spec §10 reuse audit, check 12 | the section names a probe citation or "no existing seam fits", plus a terms line | it grades shape; "a citation naming the wrong seam satisfies it" (`memory/TEMPLATE-SPEC.md`) |
| kickoff Step 4 | dossier read, gotchas, one recall query | it has never named `reuse_lookup`, and the card has no seam section |
| the builder | reads the brief and the spec | nothing compares the diff with the seam §10 named |

## Ten failure classes, each with its evidence

1. **The probe is not run.** inCMS's lookup log holds one row ever against 789 recall rows; NicoCares
   holds nine. All five inCMS reinventions predate the lookup, and from 2026-09-09 to 10-02 it
   refused to run on inCMS's own conf.
2. **Lexical retrieval cannot cross a vocabulary gap.** The inCMS sessions framed an image property
   as a URL sink (`safeImgSrc`, `sink:"url"`); the picker never appears in sink vocabulary. A goal
   phrase misses `subtokens` and `gitCommonDir`; a mechanism phrase finds them.
3. **Whole layers are not inventoried.** Design tokens, part vocabularies and DSL nodes are values
   inside two files, and the map keys files and slugs.
4. **The seam lives in another repository.** A NicoCares page's vocabulary is half in inCMS core, and
   NicoCares' lookup reads only NicoCares' map.
5. **When a seam surfaces it is buried.** Shortlists run 128 to 611 candidates; inCMS's `PricingPanel`
   ranked about 433 and was cut by the output budget.
6. **Found, then forked.** The plan cards and the carousel both had the generator surfaced and named
   in a dossier, and both forked. The decor spec asked for a `MediaRef` and the build copied the
   nearest text-URL sibling.
7. **The nearest precedent is copied, not the canonical one.** The hero accents copied the decor
   field's text box; gov's conf parsers copied each other four times.
8. **A false belief is recorded as rationale.** "packages/blocks can't import them" stood in a
   comment five days after the bridge landed to make it true.
9. **A gate sanctions the shortcut.** inCMS's `incms/focal-coverage` rule offers "a bare-URL image, no
   mediaId" as an opt-out reason, and the ProductCard spec pre-planned that disable.
10. **The reuse result stops at the spec.** §10 is graded on shape, regrounding re-runs only the
    recall half, the card carries no seams, and the diff is never compared with them.

## What follows for a design

- The search must READ code, not match names: every recorded reuse save so far came from reading
  code, a recall-reached dossier, or a Tier-2 review (TOOL-aWeighedCompass-1 finding 9d).
- It must run as a fixed step the owner opted into, not as a probe a session may skip.
- It must cover the design layer and the host repository a package installs into.
- Its output must be short, verified and binding, and must name the canonical seam over a stale copy.
- It must ride to the spec, the brief and the builder, and a diff-time check must catch what a
  pre-spec pass cannot see.

Recall terms used: reuse lookup seam affordance reinvention dossier recall shortlist fan-in kickoff
orientation convergence
