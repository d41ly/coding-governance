**Serves:** research TOOL-dTotalRecall-58
**Caused-by:** TOOL-dTotalRecall-58

# TOOL-dTotalRecall-58 divergence fold — the spec writer's return

The gov-spec-writer return for [2026-11-24-prompt-TOOL-dTotalRecall-58-divergence-fold-spec-writer](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-58-divergence-fold-spec-writer.md), in substance.

- Folded to rev-4 (INPROGRESS); `--check-specs`, `check-spec-tokens.py --spec` and hygiene check 12 exit 0.
- S4 keeps the three pre-pass callers and adds `id_grammar.py#check_marker_domain`; AC4 lists it. The docstring of `read_kept_reason`, which names its callers, is admitted for that one edit.
- S1 and S3 keep by `tree_lib.py#CENSUS_KEPT_PATHS` through `read_kept_path`; neither retired name is left.
- Section 4: `check_marker_domain` returns `(line number, finding)` pairs, and marker reds stay outside each build-folder count line.
- AC2's `packet.py --check` was not run by the writer.
