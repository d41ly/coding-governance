# TOOL-dTotalRecall-124 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-124
**Caused-by:** TOOL-dTotalRecall-124

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-1 over base
`6fa6785f8bb05a095ab86ce503999f034ab63064`, 2026-11-26, in one commit. §7's legs, `code_record.py --selftest`, and
the RED-first observation of the `New arm:` line are owed to the close. Every observation below is a scratch probe
that replays the arm's fixture and its three assertions over a kit copy, outside the suite (DERIVED 2026-11-26).

**Evidences:** TOOL-dTotalRecall-124
- AC1 — `code-record ctags list input` — the probe over the built kit read the stub's input as `./-fZ.go` alone and the line-break code path skipped as `a path no cell holds`; over a copy with the `./` cut the stub read `-fZ.go`, and over a copy with the printable test cut the derivation raised OSError 22 copying the line-break path, which the arm reads as no skip row, so each prints `FAIL` (DERIVED 2026-11-26, the probes). The suite's `ok` row and `PASS — the code record's arms` are owed to the close.
- AC2 — `tree_lib.read_blobs_at` — over the probe's repository, the requests for the line-break `kit.toml`, `z9/kit.toml` and `ok.py` with a CR answered each `kit.toml`'s own text and None; at the base and over a copy with the route cut, every request sent to the batch, they answered None, None and `z9/kit.toml`'s text (DERIVED 2026-11-26, the probes).
- AC3 — `python tools/memory-tree/gotchas.py --check` — named no finding of the class, its advisory count unmoved at 55; `grep -c 'path-list-input-read-as-options.md' memory/map/features/playbook.md` printed 1; `python tools/codebase-map/gen_map.py --check` exited 0; `python tools/memory-tree/row_grammar.py --check-relations 33706662` over the staged class printed `1 near match(es), 1 satisfied` and no `check 27:` line, the near match `read-allowlist-admits-a-writing-option` answered with `coexists-with` (DERIVED 2026-11-26). The after-commit read is in the pass's return.
