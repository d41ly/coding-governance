# TOOL-dGroundRules-43 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-43

No merge bar, no gate leg and no self-test suite ran in this pass. The read criteria ran in this
worktree from the repository root. The staged criteria ran on a `git clone` of the branch under
`%TEMP%/gr43c` carrying the changed `check_policy.py`, each staging applied by a scratch script to
the clone's copy and the copy reset from the worktree before the next; fixture repositories sat under
`%TEMP%/gr43x` and `%TEMP%/gr43a`. Each code item was also seen RED before the change, against the
HEAD `check_policy.py` loaded from a scratch directory: the snapshot of `EXCLUDES_REPO` listed
`secret.local`, an audit-hooked `os.open(O_CREAT|O_WRONLY)` was kept as a read, and `resolve_govkit`
of a tree with no deployer raised `no deployer to install with: looked at ...`. Owed at the close: the
`policy fixtures` leg over the built tree and the new arm's red-first observation (AC8, AC9, AC11,
AC12, AC15).

**Evidences:** TOOL-dGroundRules-43
- AC1 — `PAIRS_PY` then `PAIRS_SH` on the built tree — printed `True`, `False`, then `0`, `1`.
- AC2 — `FIX census-window-edge` printed one `RED as planted` line, no `WRONG`, `57 assertion(s) executed · 0 wrong`; `python tools/policy/check_policy.py --repo <t>` over `TREE_AMBIG` under `%TEMP%/gr43a` printed the one `arm_cap_census` finding `tools/govkit/registry.toml, vendor/gov/govkit/registry.toml: 2 govkit/registry.toml candidates, so the tool root is not guessed and no row is graded`, beside the framework's `population: zero` line.
- AC3 — `EVIDENCE` — printed `165:<!-- gen:build-order -->` and `179:<!-- /gen:build-order -->`.
- AC4 — `MOVE_MARKER` in the clone's build README, then `ORDER_ROWS | wc -l` printed `18` and `ORDERS` printed `19`.
- AC5 — `ORDER_ROWS | wc -l` and `ORDERS` on the built tree — each printed `19`.
- AC6 — `ORDER_SHIFT`, `TOOL-dGroundRules-11`'s `· order 1` changed to `· order 99` in the clone — `ORDERS` printed `20`, `ORDER_ROWS | wc -l` printed `19`.
- AC7 — `grep -c "KIT_AGENT_CAP_VERSION" tools/workflows/check-protocol-parity.test.sh` on the built tree printed `0`; after `OLD_ARM` in the clone the same grep printed `2`.
- AC8 — `FIX adopter-fresh-target` in this worktree printed no `WRONG`, exit 0; after `RAW_GOV`, `FIX adopter-fresh-target` in the clone printed `WRONG: the receipt's gov_source is 'C:\\Users\\daily-agent\\AppData\\Local\\Temp\\pol-vsiio4sb', not the snapshot C:/Users/DAILY-~1/AppData/Local/Temp/pol-vsiio4sb`, exit 1.
- AC9 — `PLANT_WRITES`, then `FIX adopter-fresh-target` in the clone — printed `guard-trace · 10 source read(s)`, `guard-trace · 2 absent read(s) set aside`, no `guard-trace` line naming `probe_w.lock` or `probe_absent.txt`, no `WRONG`, exit 0; `probe_w.lock` existed afterwards, so its exclusion is the event filter's.
- AC10 — `SNAP_PROBE` over `EXCLUDES_REPO` under `%TEMP%/gr43x` — `git -C <s> ls-tree -r --name-only HEAD` listed `a.txt` and `kept.txt`, not `secret.local`; the HEAD code listed `secret.local` and the excludes file too.
- AC11 — `PLANT_UNTRACKED`, then `FIX adopter-fresh-target` in the clone — `guard-trace · 10 source read(s)`, no `WRONG`, exit 0; after `KEEP_SUFFIX` too, `guard-trace · WRONG tools/govkit/entries/probe_new.toml · not under the policy fixtures guard`, exit 1.
- AC12 — `FAR_CWD` with the repository root printed the same four `guard-trace` lines as `FIX adopter-fresh-target` (`9 source read(s)`, `1 absent read(s) set aside`, `0 ignored read(s) set aside`, `52 guard line(s) checked`), exit 0; after `NO_CWD`, `FAR_CWD` with the clone printed `guard-trace · WRONG: check-spec-tokens.py --legs-for exited 2: spec-tokens: not a git repo`, exit 1.
- AC13 — `git ls-files .claude` piped to the `grep -cE` of §4 Evidence — printed `0`.
- AC14 — `PREFIX_PARITY` — printed `../x refused refused`, `a/../../b refused refused`, `/x refused refused`, `\\srv\s refused refused`, `C:x refused refused`, `C:/x refused refused`, `tools admitted admitted`, `a/.. refused admitted`, `x/../y refused admitted`.
- AC15 — `NO_GOVKIT`, then `FIX budgets-ships-join` in the clone — printed `the deployer is located · WRONG: no govkit kit holding govkit.py in this install: looked in .../gr43c/.governance/install.json, .../gr43c/tools/policy/govkit and .../gr43c/tools/govkit`, exit 1.
