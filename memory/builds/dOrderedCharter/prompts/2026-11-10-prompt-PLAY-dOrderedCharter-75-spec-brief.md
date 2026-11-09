**Serves:** research PLAY-dOrderedCharter-75

# Brief: spec 75 — the selects join arms per namespace, so gov's first unit rows leave the tags leg green

## The prompt

> I see that a lot of units are being refused this build and that's wasting tokens

— owner, 2026-11-10. PLAY-dOrderedCharter-40 built at c91c26904 and the tags leg then redded 42 declared selectors, every `practice.*`
and `reader.*` tag "declared and selects no unit". Spec 40 is CLOSED, and the build method freezes a CLOSED spec: its correction is a
new unit on top. A spec writer already designed the correction as spec 40 rev-6 in a scratch copy, before that rule was applied.

## The brief

### Goal

Write spec 75, a new Tier-2 unit that lands the correction, from the design in the scratch copy, and leave spec 40 untouched.

### Items

1. **Source design.** Read the scratch copy, which holds the correction as S5, F6, AC5, AC6, a `New arm:` line, a section 5 note and
   a section 4 evidence paragraph:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold40b/2026-10-24-spec-PLAY-dOrderedCharter-40.md`
   Carry that design whole into spec 75: the selects join in `tools/playbook/tag_index.py#check_namespace_joins` is graded per
   namespace only once some unit's `scope` names a tag in it, and prints the unarmed line until then; the docstring, `help/tags.md` and
   `tools/playbook/README.md` change with it; the `unscoped-unit` plant; the tags leg's check exits 0 over the tree.
2. **Where you write.** A unit is building, so write only this scratch file and nothing under the repository:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold75/2026-11-10-spec-PLAY-dOrderedCharter-75.md`
3. **Header.** `**Status:** DEFERRED · rev-1 · 2026-11-10 · node a · Tier-2 · base <HEAD's short sha> · streams playbook · order 37 ·
   advances PLAY-dOrderedCharter-38`, in the shape every spec of this build carries, the template at `memory/TEMPLATE-SPEC.md`.
   Order 37 sorts it after PLAY-dOrderedCharter-40 inside that group, by its edge.
4. **Edges.** `consumes-from` PLAY-dOrderedCharter-40 (its four unit rows, which arm the join) and PLAY-dOrderedCharter-10 (the join
   it changes), each with what it consumes. Record F6's `relaxes:` line for PLAY-dOrderedCharter-10 S4's selecting direction; add no
   edge into a CLOSED spec's text.
5. **The fork.** Carry F6 resolved as the scratch copy has it, with its options and vetoes.

In the spec: new text cites code as `path#symbol`, outside the acceptance bullets, which spell plain tracked paths; a section is named
in words and a check by what it checks; every new fact is pinned, keyed or marked PINNED or DERIVED; a unit is named by its id; every
function name it mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Acceptance

- Spec 75 builds as written over HEAD with unit 40 landed, carries the scratch design whole, and its tags-leg criterion is one the main
  loop can observe.

### Gates

None run: the main loop sweeps the spec before its commit.

### Non-goals

- No code. No edit to spec 40 or any file under the repository.
