**Serves:** research PLAY-dOrderedCharter-40

# Brief: spec 40 — the tags leg reds 42 declared selectors once gov's first unit rows are tracked

## The prompt

> I see that a lot of units are being refused this build and that's wasting tokens

— owner, 2026-11-10. Unit 40 built at c91c26904, but its builder's role may not run `gov_tag.py check`, and the main loop's run after
the pass reds 42: every declared `practice.*` tag and the three `reader.*` tags print "is declared and selects no unit".

## The brief

### Goal

Revise spec 40 so a repair pass leaves the tags leg green with unit 40's four rows tracked, without resting on parked
PLAY-dOrderedCharter-31.

### Items

1. **Where you write.** A unit is building, so edit only this scratch copy and write nothing under the repository:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold40b/2026-10-24-spec-PLAY-dOrderedCharter-40.md`
2. **The cause.** `tools/playbook/tag_index.py`'s join over `selects` namespaces (the block that appends "is declared and selects no
   unit") arms once ANY unit row exists. Before c91c26904 no unit row was tracked, so the `practice` and `reader` joins printed
   "unarmed: no unit row". Unit 40's four rows carry no `scope` (spec 40 F2), so they select nothing, and every declared selector reds.
   Gov's practices and readers are selected only by unit rows the parked unit 31 and later units would write. Confirm this against
   HEAD with `python tools/playbook/gov_tag.py check` and a read of that block.
3. **Resolve it as a fork under the fork rule.** Candidate options: (a) the selects join arms per namespace only once some unit selects
   a member of it, printing the unarmed line otherwise; (b) unit 40's rows carry a `scope` that selects every declared reader, and the
   practice join is handled by (a) or by a pending row; (c) a pending or waiver row per declared selector until the units that select
   them land. Weigh each against the gate rule that an empty population never reads as coverage, and against `[class]`. Record the pick
   in section 8, and say what the join does not check after it.
4. **Make the leg observable.** Add an acceptance criterion that the tags leg's check exits 0 over the tree with the four rows tracked,
   observed by the main loop (the builder role may not run it), and a plant that reds the old behaviour if the pick changes code.
5. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

Resolve each choice under the fork rule and record it in section 8.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-10, with one history line naming this brief. Leave the status as it reads.
- New text cites code as `path#symbol`, outside the acceptance bullets, which spell plain tracked paths. New text names a section in
  words and a check by what it checks. Every new fact is pinned, keyed or marked PINNED or DERIVED; name a unit by its id. Every function
  name it mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Acceptance

- Spec 40 says how its repair pass leaves the tags leg green with the four rows tracked, with the fork resolved in section 8.

### Gates

None run: this is a scratch edit. The main loop sweeps the spec before its commit.

### Non-goals

- No code. No edit outside the scratch copy.
