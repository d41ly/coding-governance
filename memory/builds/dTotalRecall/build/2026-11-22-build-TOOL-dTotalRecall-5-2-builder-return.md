**Serves:** research TOOL-dTotalRecall-5

# TOOL-dTotalRecall-5 build pass 2 — the builder's return (DIVERGENCE)

The gov-builder return of `unattended-unit.js` run `wf_08ce3d04-bfb`, at base `a8748ffaa`, saved in substance. Nothing was written or committed.

## why

DIVERGENCE: rev-9 contains two statements that cannot both hold. Its §7 gates cannot go green on the grammar §4 "The policy reads" designs. Nothing was written.

(1) The design. §4 "The policy reads" says a ValueError from `tree_lib.py#read_policy_value` refuses the caller. S4 has `build_grammar` call `derive_slug_grammar(conf.root)`, and S13 has `build_id_token_re` / `_expand_ids` / `read_bindings` do the same. S6 says a failed module run makes check 4 exit 2. Together, every id parse and every check-4 run now depends on `policy.py get` working in its root. But `policy.py get` refuses (exit 2) in any repository where it cannot resolve a landed revision, meaning no remote and no commit on `main`. Measured 2026-11-22: a scratch repo from `git init --template=` with one commit lands on `master` (this node's `init.defaultBranch` is `master`). There `policy.py get builds.slug-words` exits 2 with `refs/heads/main names no commit in this repository ... GOV_DEFAULT_BRANCH is unset`, and `read_policy_value` raises `ValueError builds.slug-words did not read: ...`. After `git branch -m main` the same repo prints `1-3`.

(2) The gates this breaks (§7 lists both):
- `memory-hygiene self-test`: `tools/memory-tree/check-memory-hygiene.test.sh` pins every fixture to master on purpose with `GIT_CONFIG_KEY_1=init.defaultBranch GIT_CONFIG_VALUE_1=master`. Its comment (the block above that export) says it does this so that "no fixture has a landed revision". It runs about 35 fixture inits, and every check-4 run in them would exit 2 under S6. (DERIVED, the builder's own run)
- `corpus-ids selftest`: `tools/memory-tree/corpus_ids.py#_scratch` runs a plain `git init` and commits on the node default, then reaches `grammar_for(tmp)`, which would raise.

Other callers that would hit the same refusal on such a tree: `merge-rows.py` (the merge driver), `transition_audit.py`, `drift_report.py`, and an adopter repo with no remote whose branch is not `main`.

The precedent in the same kit points the other way. Checks 6 and 7 read their policy switch and treat the read's refusal as "refuses as before", the default behaviour (same comment block in check-memory-hygiene.test.sh). S6 and §4, by contrast, refuse.

What §4 "The policy reads" (and S6's module-failure sentence) would have to say. Pick one:
(a) A ValueError whose cause is that no landed revision resolves applies `SLUG_DEFAULTS`, as LookupError does, with one stderr line per process naming the key and the reader's reason. A ValueError for a value the reader refuses still refuses. Check 4's exit 2 stays only for a module crash or a malformed recorded grammar.
(b) Keep the refusal, and add to Files touched and Scope every suite fixture that needs a landed `main`: at least check-memory-hygiene.test.sh's master pin and `corpus_ids.py#_scratch`, plus a census of the rest. This conflicts with the hygiene suite's deliberate master pin for checks 6 and 7.
(c) Read the three keys only where `.governance/policy.toml` is tracked in `root`, and apply the defaults otherwise.

(3) Minor, for the same revision, so it does not come back as a second divergence. S13 rebinds only `build_id_token_re`'s slug group. `_expand_ids`'s range form `rng` keeps `[A-Za-z0-9]+`, so `TOOL-dX-1..3` would still expand to `TOOL-dX-2` while the single token `TOOL-dX-2` is refused. That is the F10 inconsistency again, in the range form. The spec should say whether `rng` splices `slug_class` too.

Every other claim I checked held against HEAD a8748ffaa:
- the census command prints 71 lines in 35 files; (DERIVED, the builder's own run)
- the cited symbols in tree_lib.py, gen_build_index.py and id_grammar.py;
- check-memory-hygiene.sh's `BUILD_SLUG_RE` default, refusals, declared-key loop and check-4 `slugre` binding;
- the `memory-tree/hygiene-print-modes` contract;
- the workflows kit's `[[files]]` placeholders and `[[regenerate]]` row;
- the renderer's MEMORY_TREE_DIR probe and FANOUT_CAP read;
- `PARITY_ROWS` and its marker-derived population;
- the canonical `resolve_kit_dir` block, and run-gates' embedded copy;
- `requires_if` support in govkit;
- the three catalogue rows, the `unsummarised-keys.txt` and `docs-undocumented.txt` rows, and the HYGIENE.template.md slug rule at line 191.

## summary

I built nothing and committed nothing. The spec's design makes its own §7 gates go red, so I am returning a divergence (details in `why`). This pass started at a8748ffaad84826239b594de5c22792b8194ead2 and wrote no repository path. The only uncommitted change is the main loop's own staged `memory/builds/dTotalRecall/RUN.md`, which I left untouched.

- **Not done:**
  - I did not run the `--brief` record verb, because it writes a RUN.md row that the divergence rule would make me undo (pass 1 did the same).
  - I did not run the `gotchas.py --for-diff` checklist, because there is no commit for it to read.
  - I made no draft, so there is no patch to save.
  - Nothing was skipped for running past its time bound.
- **What I checked:**
  - Read-only `git grep` and `sed` over HEAD.
  - The census command of §4 "The readers" at HEAD: 71 lines in 35 files, as pinned. Output saved at C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/census2-HEAD.txt. (DERIVED, the builder's own run)
  - A probe of `tools/policy/policy.py get` and of `tree_lib.read_policy_value` in a one-commit scratch repo on `master` (exit 2 / ValueError), then the same repo renamed to `main` (prints `1-3`). The scratch repos are under C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/ (pg1, pg2, pg3).
  - Reads of the master pin in `tools/memory-tree/check-memory-hygiene.test.sh` and of `tools/memory-tree/corpus_ids.py#_scratch`.
- **Gates:** these checks stand in for no gate, and none ran. Every AC1 to AC12 observation and the three `New arm:` RED-first observations (resolve-python.test.sh, check-memory-hygiene.test.sh, gen_build_index.py `--selftest`) are still owed once the unit is rebuilt from a revised spec.
- **Card mismatch:** the parent's orientation card still says this unit is DEFERRED, but its spec header reads INPROGRESS. The card is stale.
