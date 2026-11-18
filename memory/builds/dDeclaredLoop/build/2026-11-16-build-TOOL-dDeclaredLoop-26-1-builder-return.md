**Serves:** journal TOOL-dDeclaredLoop-26

# Builder return — TOOL-dDeclaredLoop-26, dispatch 1: rev-5's files touched, position's read, the tag resolver's root and the plants' pin do not hold over the tree as built

## Why

DIVERGENCE: TOOL-dDeclaredLoop-26 rev-5 cannot be built as written. I checked it against HEAD 830567b20 and four places fail. No product edit was made, so there is no patch to save, and the tree is clean.

(1) §4 Files touched, and §5 "registry and pins", leave out paths the change needs.
- `memory/map/features/loop.md` is missing. Its `[claims] gate-legs` list must gain `loop composition fixtures`. The codebase map's inventories read every name in tools/gate-legs.json (memory/map/generated/inventories.json lists each loop leg), so the coverage gate reds a new leg no dossier claims. Unit 29's spec listed this file for its own leg.
- The generated map files are not named: `memory/map/generated/symbols.json`, `MAP.md`, `CARDS.md` and `inventories.json`. §5 says "the map's generated files are regenerated", and symbols.json indexes Python functions (it holds 9 entries for upstream.py), so eight new functions stale it.
- `tools/loop/README.md` is not named either. Every loop module has a section there, and unit 29 listed it.

(2) §1 and S3 cite a read that no longer holds. They say `position.py#derive_position_into` reads through `loop_items.py#read_composition`. Since unit 29 it reads through `loop_items.read_composed_items(repo)`, in derive_position_into and in print_check_refusal. That function turns exit 2 into gov's own rows and exit 1 into a ValueError. S3 makes `read_composition_at` answer `read_composition`'s triple, so position needs that mapping at a pin. There are two ways to get it:
- (a) `read_composed_items` gains a revision argument routed through `read_composition_at`. That edits tools/loop/loop_items.py, which Files touched does not list.
- (b) position.py copies the mapping, which breaks the [reuse] rule.
The spec has to choose one, and list loop_items.py if it takes (a).

(3) S4 and §4 "The carry" say `gov_tag.py show <tag> --json` runs "with the repository as its working directory", found by `resolve_kit_dir`. But gov_tag.py's `resolve_repo_root` reads `rev-parse --show-toplevel` from its own folder and ignores the working directory. So a resolver found beside composition.py (`resolve_kit_dir(..., KIT)`) reads this tree's tag index, never the scratch's, and AC2 and AC4 cannot hold. I probed a build_scratch_tree scratch with a rename change record written by write_change:
- The scratch's own copy of the resolver, found by `resolve_kit_dir("playbook", "gov_tag.py", <root>/<the loop kit's tree-relative folder>)`, answered exit 0 with a `retired` row whose text is `**Successor:** item.design.regroup`.
- The same scratch first refused the policy read: `refs/heads/main names no commit ... GOV_DEFAULT_BRANCH is unset`. build_scratch_tree's branch is not `main`.
S4 has to say the resolver is found under the repository being read, and §4 "The plants" has to say the base names `main` or sets GOV_DEFAULT_BRANCH.

(4) In §4 "The plants", C1 is ill-defined against AC1. Both moves are recorded "at commit C1", but write_transition commits each move. The second move is recorded at the first move's commit, so its pin, and the `composition@<sha8>` AC1 expects, is that commit, not C1. The plant has to name which commit AC1's pin is.

Confirmed as written: the claims of S1, S2 and S8 I probed (read_overlay, read_kind_source, derive_kind_composition, TRANSITION_FIELDS, resolve_commit, read_clean_env, read_policy_kit, run_selftest_cases, build_scratch_tree), the `principle principle.p8 dOrderedCharter` pending row, VERB_OFFENDER_PIN 1209, and §5's claim that compose does not answer 0 in a scratch with no kinds register (exit 2, unarmed). A compose in a scratch whose definition re-tags `item.design.decompose` answered 0, holding `item.design.regroup` and not `item.design.decompose`.

## Summary

Not built and nothing committed: the spec has to be revised first. The base is 830567b20732add8bbda1d34ef885e9b0fe97d18 and the working tree is clean.

I did not run `--dispatch` or `--brief`, because both write `memory/builds/dDeclaredLoop/RUN.md` and this pass makes no write. I ran no gate, suite or bar, not even the naming lexicon. That means no gate's verdict is replaced by anything here.

The only checks were read-only probes:
- **Reading the code:** position.py, loop_transition.py, loop_items.py, gov_tag.py, overlay_rows.py, build_records.py and the four registry files, checked against what the spec says about them.
- **One scratch-repository probe:** C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/probe26.py. It builds a build_scratch_tree scratch, re-tags `item.design.decompose`, writes a rename change record and commits. Then it runs compose (exit 0, holding `item.design.regroup`) and the scratch's own `gov_tag.py show --json`, which answered exit 0 with a `retired` row once the branch was named `main`.
- **One compose in an empty repository:** exit 2, unarmed. This confirms §5's claim about the transition plants.

The `why` field lists the four findings in one divergence:
1. Files touched omits the loop dossier's claim for the new leg, the generated map files and tools/loop/README.md.
2. Position now reads through `read_composed_items`, so the spec must choose between editing loop_items.py and copying the mapping.
3. The tag resolver must be found under the repository it reads, and the scratch must name `main`.
4. The plants' C1 does not match AC1's pin.

Owed when the unit is built: every leg in §7, the new leg `loop composition fixtures`, and the RED-first observation of both `New arm:` lines.
