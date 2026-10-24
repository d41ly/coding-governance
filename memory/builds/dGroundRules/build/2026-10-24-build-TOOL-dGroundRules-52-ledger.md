# TOOL-dGroundRules-52 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-52

No merge bar, gate leg or self-test suite ran in this pass. The built-tree criteria ran verbatim from
this worktree's root over `a3a8b8685` with this pass's `tools/policy/check_policy.py` in the working
tree. The staged criteria ran in clones made as `CLONE_AT` makes them, under `%TEMP%/gr52` and
`%TEMP%/gr52<staging>`, each checked out at `a3a8b8685` with this pass's `check_policy.py` copied over
the clone's, byte-identical to the committed file, each staging applied by a scratch script and the
copy reset before the next; the fixture repositories sat under `%TEMP%/gr52ig` and `%TEMP%/gr52ex`.
Each "before this unit" observation ran against the clone's own HEAD `check_policy.py`. Owed at the
close: the `policy fixtures`, `memory hygiene`, `codebase-map coverage + freshness` and `lexicon
naming predicates` legs over the built tree, and the RED-first observation of §7's `New arm:` line,
which covers AC12, AC13 and AC21.

**Evidences:** TOOL-dGroundRules-52
- AC1 — `EVIDENCE` printed `165:<!-- gen:build-order -->` and `179:<!-- /gen:build-order -->`; the same grep over the build README at HEAD printed `242` and `265`.
- AC2 — `KEPT_PROBE` on the built tree printed `['tools/govkit/govkit.py']`; after `NO_MAP` in the copy it printed `['tools/govkit/__pycache__/govkit.cpython-314.opt-1.pyc', 'tools/govkit/__pycache__/govkit.cpython-314.pyc']`.
- AC3 — after `CLONE_AT` and `UNEXCLUDE`, `FIX adopter-fresh-target` in the copy printed `guard-trace · WRONG .git/info/exclude · not under the policy fixtures guard` and `guard-trace · WRONG .git/index · not under the policy fixtures guard`.
- AC4 — `RENDERED_STEPS` on the built tree printed rows 12, 13 and 14, each ending `| no |`; after `NO_STEP_RULE` and `gen_build_index.py --write` in the copy, the three rows ended `| yes |`.
- AC5 — `PAIRS_PY` and `PAIRS_SH` on the built tree printed `True`, `False`, then `0`, `1`; after `RAW_BOTH` in the copy they printed `True`, `True`, then `0`, `0`.
- AC6 — `GUARDABLE_PROBE` over `IGNORE_LOG` (`git config --get core.quotePath` exit 1, unset) printed `(['keep'], 2)` then `(['keep'], 1)`; the HEAD code printed `(['keep', 'ig\xf6'], 2)` then a `UnicodeEncodeError` for `'\udcff'`.
- AC7 — after `ORDER_SHIFT`, `TOOL-dGroundRules-11`'s `· order 1` changed to `· order 99` in the copy, `ORDERS` printed `20` and `ORDER_ROWS | wc -l` printed `19`.
- AC8 — after `CLONE_AT`, `git -C "$TEMP/gr52" rev-parse HEAD` printed `a3a8b8685e78169fcc355225e80214a9a85e55c0`, the sha checked out, and `FIX adopter-fresh-target` in the copy printed `9 source read(s)`, `1 absent read(s) set aside`, `0 ignored read(s) set aside`, `52 guard line(s) checked`, no `guard-trace` line naming .git/, exit 0; after `UNEXCLUDE`, AC3's lines.
- AC9 — `FIX budgets-ships-join` on the built tree printed `policy-fixture: guard-trace · 52 guard line(s) checked`; its only `WRONG` lines named the seven kit descriptors the close's deviation-78 sweep owns.
- AC10 — after `CLONE_AT` and `DEPTH3_LIVE`, `FIX census-window-edge` in the copy printed two `census-window-edge` `WRONG` lines (`WRONG: refused a/b/c/govkit/registry.toml, tools/govkit/registry.toml`) and no `WRONG` naming `rev-parse`, `check-ignore` or `policy fixtures`; with `TOPLEVEL` in its place, two `census-window-edge` `WRONG` lines (`WRONG: refused registry.toml, tools/govkit/registry.toml`) and none of the three.
- AC11 — `INSTALL_LINES` on the built tree printed `1` and `HELP_LEGS` printed `policy fixtures <- help/policy.md`; after `HELP_MOVED` in the copy, `INSTALL_LINES` printed `0`.
- AC12 — after `PLANT_NONASCII` (`tools/gövkit/__pycache__/x.pyc`), `FIX adopter-fresh-target` in the copy printed `guard-trace · unmapped cache read tools/gövkit/__pycache__/x.pyc`, `1 ignored read(s) set aside` and no `WRONG` naming x.pyc; the HEAD code printed `guard-trace · WRONG tools/gövkit/__pycache__/x.pyc · not under the policy fixtures guard`, exit 1.
- AC13 — `PREFIXED` printed `policy-fixture: guard-trace · WRONG sys.pycache_prefix is set`, exit 1, and ran no case; `$TEMP/gr52pfx` was never created.
- AC14 — `SNAP_PROBE` over `EXCLUDES_REL` under `%TEMP%/gr52ex` listed `excl.txt`, `kept.txt` and `one.txt`, not secret.local; after `NO_FORWARD` in the copy it listed secret.local too.
- AC15 — after `NO_GIT`, `FIX adopter-fresh-target` in the copy printed `guard-trace · WRONG: git rev-parse --git-dir --git-common-dir at <copy> did not answer both, so no case ran` and no `source read(s)` count line; after `DENY_OFF` (`UNEXCLUDE`'s `return ()`), it printed `11 source read(s)`.
- AC16 — after `BAD_JSON`, `FIX adopter-fresh-target` in the copy printed `guard-trace · WRONG: check-spec-tokens.py --legs-for exited 1: legs-for: REFUSING — gate-legs.json did not parse` and `guard-trace · WRONG: the manifest did not parse`.
- AC17 — `PYC_TEMP_PROBE` on the built tree printed `[]` and `['tools/govkit/__pycache__/govkit.cpython-314.pyc.123']`; the HEAD code raised `AttributeError: module 'check_policy' has no attribute 'UNMAPPED_READS'`. After `CLONE_AT` and `CUT_BACK` it printed `[]` and `['tools/govkit/govkit.py']`.
- AC18 — `LOCAL_COUNT` on the built tree printed `0`; after `TRACK_LOCAL` in the copy it printed `1`.
- AC19 — after `PLANT_BYTES`, `FIX adopter-fresh-target` in the copy printed `guard-trace · WRONG README.md · not under the policy fixtures guard`. after `STR_PATH` too, it printed `2 absent read(s) set aside` and no such line, exit 0.
- AC20 — after `EMPTY_GUARD`, `FIX adopter-fresh-target` in the copy printed a `guard-trace` `WRONG` for every traced read, among them `WRONG help/policy.md · not under the policy fixtures guard`.
- AC21 — after `PLANT_REFUSED` (`tools/govkit/__pycache__/x.pyc`), `FIX adopter-fresh-target` in the copy printed `guard-trace · unmapped cache read tools/govkit/__pycache__/x.pyc` and no `WRONG`.
