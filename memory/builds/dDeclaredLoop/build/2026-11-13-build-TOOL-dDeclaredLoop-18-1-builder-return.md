**Serves:** journal TOOL-dDeclaredLoop-18

# Builder return — TOOL-dDeclaredLoop-18, dispatch 1: a divergence, nothing built

Run wf_951bfccb-377. The builder stopped before its code and handed the spec back.

## Why

DIVERGENCE: the spec (rev-3, base ed497191) was written before dOrderedCharter's seams were built, and six of its claims do not hold against the code at cb34ba603. Nothing was written, `--dispatch` and `--brief` were not run, and the worktree is clean.

1. §4 "The four rows" (S1), `purpose-source`. The `step` row spells `purpose-source = "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md#design-tags"`. That file is tracked, and `check_namespace_purpose` (tools/playbook/tag_index.py@46bfe37d:1266-1271) reds any `<path>#<field>` whose path is not `.toml` or `.py`. The row as written turns the `tags` leg red at landing; the existing `bad-purpose-source` plant shows the same rule. §4 must give a `purpose-source` the arm accepts for each of the four rows; it spells only the `step` row's.

2. §4 "The extractors" and Inventory, the row contract. The spec says an extractor takes path and text and yields `(tag, "member"|"family", line)`. The code calls `fn(ctx, path, None)` to ask whether a path is read, then `fn(ctx, path, text)` for rows `(tag, kind, line, end_line, text)`. A defining row is kind `tag` (`DEFINE_KINDS = ("doc","section","tag")`). No reader reads a kind `member` or `family`: not `check_tag_shape`, `derive_namespace_state`, `check_namespace_joins` nor `read_defined`. A `member` row would leave all four namespaces unarmed and ungraded, so AC1 to AC4 could not go red. §4 must say members are kind `tag`, and name which readers gain the minted `family` kind.

3. §3 Non-goals against AC6. `check_resolves` (tools/playbook/tag_index.py@46bfe37d:955-966) reds every graded citation into an armed namespace that is not a defined row. Once `policy` is armed, `policy.review.build` reads "unresolved · names no row". The Non-goal excludes "a family resolver inside PLAY-dOrderedCharter-19 S7's `resolves` check", so AC6's "exits 1 naming `policy.reviews.build` alone" cannot hold. Either the Non-goal goes and S5 covers `check_resolves`, or AC6 changes.

4. §4 "The catalogue in the `policy` namespace" (S5, AC6, §8 F5), the family read. The spec says `read_policy_value(key, root, rev="HEAD")` returns for any key a catalogue row matches. Probed: `python tools/policy/policy.py get review.build --explain --rev HEAD` exits 2 with "the row review.<stage> carries a derived default no reader computes yet, so review.build has no value to read until the file sets it". `review.build.effort`, `roles.effort.builder` and `budgets.x` do the same; `reviews.build` exits 2 with "not a catalogue key". So `PolicyRefused` is raised for a matched, unset placeholder key, and S5's rule "a `PolicyRefused` reads the citation as undeclared" makes every family citation undeclared unless the policy file sets that key. The spec must name another signal for "a row matches" (F5's option (c), or telling the two refusals apart), or have the `policy-family` plant set the key and say that "declared" means set.

5. §4 Migration ("no tag in these namespaces exists in a source at base") and "the catalogue is green". memory/map/features/policy.md:83 and :87 carry the backticked spans `policy.resolve` and `policy.validate`, which are Python seams in a map dossier outside `memory/builds/`. With `policy` armed, both `check_namespace_joins` and `check_resolves` red them, so the real `tags` leg goes red at landing. The spec must say how these are handled, and widen the write set if the dossier or its generator changes. The catalogue itself is clean: 272 rows, 264 literal names, 6 family prefixes as pinned, none colliding with a namespace word or the segment shape, and `lexicon.py --tags` refuses none of the 270.

6. §5 observability, AC2, AC1 and AC3, the printed text. `gov_tag.py check` prints no per-namespace member or family count (`run_check`, tools/playbook/gov_tag.py@20c41e24:276-285), so AC2's observable does not exist and S6 lists only plants for that file. The shape reasons are spelled `first segment 'step' is a namespace word` and `segment 'Plan' is outside [a-z0-9][a-z0-9-]*` (`derive_tag_fault`, tools/playbook/tag_index.py@46bfe37d:1076-1083), not AC1's `first segment is a namespace word` or AC3's `segment outside seg`. An arm matching the ACs' literals would never pass. §2 or §4 must place the count line, and AC1 and AC3 must quote the real reasons.

Smaller, for the same revision. The `policy-family` plant's "copies of the playbook and policy kits" only reaches the copied `policy_value.py` if the plant runs the copied `gov_tag.py` as a subprocess, because `run_fixture` runs in-process on the real kit's modules. That copy also needs the memory-tree kit (`load_memory_tree`), and a catalogue that still answers `tags.bare-refs`, `tags.retired-cites` and `tags.slice`, since `--set` is honoured only under `--fixture`. The §7 `New arm:` line names tools/playbook/adopt-playbook.sh, which "Files touched" omits.

## Summary

TOOL-dDeclaredLoop-18 was not built: returned as a DIVERGENCE with six spec claims that fail against current code, listed in `why`. No commit, no write under the repository, spec status left INPROGRESS.

Not run: `--dispatch`, `--brief`, `gen_build_index.py --write`, `gotchas.py --for-diff` (no commit to run it over), and no gate, suite or bar.

Checks that ran, all read-only probes and none standing in for a gate verdict:
- Read tools/playbook/tag_index.py, gov_tag.py, policy_value.py and namespaces.toml whole against the spec.
- `python tools/policy/policy.py get <key> --explain --rev HEAD` over `review.build`, `reviews.build`, `review.build.effort`, `roles.effort.builder`, `budgets.x` (all exit 2) and `tags.slice` (exit 0).
- A `python` parse of tools/policy/catalogue.toml: 272 rows (PINNED), 264 literal names, 6 family prefixes, no shape or namespace-word fault.
- `python tools/lexicon/lexicon.py --tags` over the 270 would-be `policy` tags and four sample tags: 0 refused.
- `git grep` for backticked or bracketed `step.`/`item.`/`policy.`/`command.` spans in Markdown outside `memory/builds/`: the two live hits are memory/map/features/policy.md:83 and :87.

AC7 was not observable: its red needs the `item` row registered, which was not written.

Owed at the close once the spec is revised and the unit rebuilt: the §7 `New arm:` on tools/playbook/adopt-playbook.sh (RED on the `policy-ns-word` and `loop-bad-seg` plants, then GREEN), and the `tags` leg over the real tree.

One scratch file was written, outside the repository: C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/policy-tags.txt

The session's orientation card still reads this unit as "Tier-2 at DEFERRED"; the spec header is INPROGRESS, so the card is stale.

Files for the spec writer:
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/playbook/tag_index.py
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/playbook/gov_tag.py
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/playbook/policy_value.py
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/policy/catalogue.toml
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/map/features/policy.md
