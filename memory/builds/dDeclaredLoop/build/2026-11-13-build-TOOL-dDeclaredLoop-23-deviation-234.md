# TOOL-dDeclaredLoop-23 deviation 234 — the reader's helper names beside the spec's inventory, and the routed reader's refusal

**Serves:** deviation TOOL-dDeclaredLoop-23

- **Departs from:** `TOOL-dDeclaredLoop-23@rev-3` [§4 "### Inventory"]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-23`'s spec at rev-3 mints `SHA_RE`, `VIEWS`, `read_commits`, `derive_attribution`, `read_message_ids`, the CLI verbs and the two flags in `commit_trailers.py`, and has `read_routed_commits` call `read_commits` with its own runner.
- **After:** the block also defines `run_git`, the default runner; `read_key_table`, the lookup of the registered keys; `derive_tokens`, the one token rule; and `build_fixture`, which the `--fixture` flag and the AC2 and AC3 probes build the planted repository with. `read_routed_commits` and `read_newest_unit` raise the module's `Refusal` where the reader raises `LookupError` or `ValueError`. `routed_commits.py#extract_unit_ids` stays defined and is no longer called there.
- **Cause:** builder discovery
- **Reason:** the three functions of §4 need a runner, a table read and a tokeniser, and a probe needs the fixture as a repository it can read; the lexicon answered OK for each name on 2026-11-13. The routed-commit leg exits 2 on a `Refusal` and would print a traceback on any other exception. Other builds' specs name `extract_unit_ids` as a seam, so removing it is not this unit's to do.
- **Evidence:** `tools/lib/commit_trailers.py#read_key_table`, `tools/lib/commit_trailers.py#build_fixture` and `tools/memory-tree/routed_commits.py#read_routed_commits` at the pass commit of `TOOL-dDeclaredLoop-23`.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-23
