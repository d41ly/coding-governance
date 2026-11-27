**Serves:** research TOOL-dTotalRecall-5

# TOOL-dTotalRecall-5 build pass 1 — the builder's return (DIVERGENCE)

The gov-builder return of `unattended-unit.js` run `wf_74b83e73-148`, at base `44c6800aa`, saved in substance. Nothing was written or committed.

## why

DIVERGENCE: the pre-build check of rev-8 found one contradiction inside the spec and two claims about the tree that do not hold. Nothing was written.

(1) §6 AC12, with its Red-when, and §8 F10 contradict §4 "The grammar" and S13. §4 defines a word as [A-Z][a-z0-9]* with the default words=1-3. That makes `dX` a legal one-word slug, so slug_class (the legacy shape OR the shape in force) admits it. A probe that spliced that class into build_id_token_re's slug group matched TOOL-dX-2 in full and refused TOOL-x-1. AC12 says TOOL-dX-2 must not match. F10 says the bound class refuses the fixture id TOOL-dX-2, but only the legacy shape does. The same word shape also widens grammar_for().ID_RE's session era (S4) to accept ids like ABL-dX-3, which today's [A-Za-z]{2,} refuses. §4 or S4 never states that widening. The spec has to pick one:
  (a) §4's word becomes [A-Z][a-z0-9]+ (at least one character after the capital). Measured at HEAD: all 229 build folders still fit that stricter shape, all six flip slugs still fit, and none of the 3062 distinct ids read_bindings reads at HEAD falls outside the class.
  (b) AC12, its Red-when and F10 drop the TOOL-dX-2 refusal, and S4 states the ID_RE widening.

(2) §4 "The readers" table says the runlog, branch-reconcile and run-gates readers go through "its resolve_kit_dir copy". run-gates has one: the embedded block in tools/run-gates/run-gates.sh#resolve_kit_dir. The other two do not:
  - tools/runlog/runlog_lib.py, the reader AC8 probes, has no copy. Runlog's only copies are in adopt-runlog.sh and selftest.py.
  - tools/branch-reconcile has none anywhere. The brief already says this pass adds it.
§4 or S8 would have to say that this pass adds the canonical resolve_kit_dir block to both runlog_lib.py and branch_reconcile.py. It would also have to say whether those copies join the resolve_kit_dir parity row of tools/lib/resolve-python.test.sh#PARITY_ROWS. S8 currently counts only "two rows" (slug_legacy_py and slug_legacy_sh).

(3) The census command in §4 "The readers", which §1's and AC7's PINNED figures stand on, does not reproduce as written. On this node (git 2.54.0.windows.1) the `(\\d|...)` arm inside single quotes matches no literal backslash-d spelling. The command prints 49 lines in 21 files at b4137f489, at 8b8b1374 and at HEAD, and 47 lines at fb872a37e. With that arm spelled `([\\]d|...)` it prints the PINNED 71 lines in 35 files at b4137f489 and at HEAD. The fb872a37e figure (62/29) was not re-measured with that spelling. The command should be spelled with the bracketed backslash so the figure it pins reproduces.

Every other cited symbol, path and pinned line checked out against b4137f489 and HEAD.

## summary

I built nothing and committed nothing: the spec contradicts itself and makes two claims about current code that do not hold (details in `why`). This pass started at 44c6800aa43c9caea8b5e5a2a479ab5b7b9de871 and wrote no repository path. The only uncommitted change is the main loop's own staged `memory/builds/dTotalRecall/RUN.md`, left untouched.

- **Not done:** I did not run the `--brief` record verb, because its row in RUN.md would have had to be undone under the divergence rule. Nothing was skipped for running past its time bound. The `gotchas.py --for-diff` checklist was not run, since there is no commit for it to read. I made no draft, so there is no patch to save.
- **What I checked:** I compared the spec's claims with the tree using `git grep`, `git show` at b4137f489 and short `python -c` probes against `tools/memory-tree/tree_lib.py`. Those probes covered `build_id_token_re` with the class from §4 spliced in, the slug shape against every folder under `memory/builds/`, and the ids `read_bindings` reads at HEAD. They stand in for no gate. No gate, suite, bar or `--selftest` ran, and every AC1 to AC12 observation and every `New arm:` red-first observation is still owed once the unit is rebuilt.
- **Scratch files:** the census outputs are `C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/census-b4137f489.txt` and `C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/census-HEAD.txt`.
- **Card mismatch:** the parent's orientation card still says this unit is DEFERRED, but the spec header reads INPROGRESS since commit 44c6800aa. The card is stale.
