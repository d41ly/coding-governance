**Serves:** research TOOL-dTotalRecall-37

# TOOL-dTotalRecall-37 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-37-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-37-reground-spec-writer.md), in substance.

- Re-grounded at rev-3, base `8b8b1374`; `check-spec-tokens.py --spec`, `unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-37` and hygiene check 12 exit 0.
- Moved by the landed code: the workflows kit tracks more `.js` files than the spec typed (DERIVED, `git ls-files tools/workflows/*.js`), the new hand-written ones `check-review-join.js`, `check-verifier-fanout.js` and `spec-audit-optin.js`; AC1 checks the whole kit through `git ls-files | git check-attr --stdin` rather than a typed list.
- Unit 8's record is `tools/playbook/code_record.py`; AC4 reads the index file `tag_index.py#derive_index_path` names.
- The render set resolves through govkit's `rule_sources` and `resolve_dests`; probed over every rendered row, exactly the four `.js` renders survive.
- Two extractions so no second copy lands (`[reuse]`): `derive_home_ctx` (the ctx `derive_regenerate_argvs` builds) and `read_attr_population(target, attr)` (from `eol_population`), behaviour-neutral for current callers (S3, AC5).
- `policy fixtures` added to the leg line (its guard names `tools/govkit/govkit.py`); bare cites rewritten by symbol.
- F3 RESOLVED (agent, delegated): a rendered `to` that does not end `.md` counts as code, the complement of the spec's Markdown non-goal. Parked: none.
