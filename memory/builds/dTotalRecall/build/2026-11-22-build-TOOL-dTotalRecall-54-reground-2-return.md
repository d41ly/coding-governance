**Serves:** research TOOL-dTotalRecall-54

# TOOL-dTotalRecall-54 second re-ground over unit 5 as built — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-54-reground-2-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-54-reground-2-spec-writer.md), in substance.

- Folded to rev-5 at HEAD `e514feb71`; `check-spec-tokens.py --spec`, `--check-specs dTotalRecall TOOL-dTotalRecall-54`, hygiene check 12 and `writing_practice.py check pinned-facts` exit 0; the lexicon accepts `parse_id_parts` and `load_sibling`.
- The parser passes `root` to `tree_lib.py#build_id_token_re`, whose slug class unit 5 bound per root; the one-argument call accepts an id a scratch tree's grammar refuses, so AC1 gains that case and the `New arm:` line names it.
- §3's literal slug-class caveat is gone: unit 5 is CLOSED and landed the binding at `202a354a4` through `tree_lib.py#read_slug_class`.
- Unit 5 added two more inline copies of the sibling import (`id_grammar.py#read_slug_policy`, `#read_recorded_grammars`); F3 RESOLVED (agent, delegated) as (a): `load_sibling` replaces all three, AC5 counts one `sys.path.append` left in `id_grammar.py`, and §4 states that only AC5's import-alone half is the red case now.
- Every other claim held at HEAD. No sibling spec needed a bullet; unit 39's spec spells `load_sibling` with another signature and its own §4 defers to what lands.

## The `alt` follow-up

The same writer folded [2026-11-22-prompt-TOOL-dTotalRecall-54-alt-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-54-alt-brief.md) into rev-5: S1 spells `parse_id_parts(ident, root, *, alt=None)`, the sketch reads the tree's families only when `alt` is `None`, new AC6 observes one id refused without `alt` and parsed with it and a positional `alt` refused, the `New arm:` line covers it, §3 orders step 8 as 54, 38, 4, and the hands-off to unit 38 names both parameters. The three checks read green. Unit 38 rev-6 defines `backlog.ANY_FAMILY` itself (its §4 and Files touched), which the writer asked the main loop to confirm.
