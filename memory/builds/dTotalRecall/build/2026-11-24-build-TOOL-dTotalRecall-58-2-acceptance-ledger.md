# TOOL-dTotalRecall-58 — acceptance ledger, build pass 2

**Serves:** log TOOL-dTotalRecall-58
**Caused-by:** TOOL-dTotalRecall-58

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-4 over base
`12d219431` and ran each probe below on node a, 2026-11-24, from `tools/memory-tree/` unless named: the
greps, the log and the packet check from the root, each plant's fixture built under the system temp
directory and removed. §7's legs and the `New arm:` RED-first observations of the plants
`marker-in-build-script` (`record_causes.py#PINNED_PLANTS`) and `marker-in-kept-script`
(`record_kinds.py#run_selftest`'s `shows`) are owed to the close.

**Evidences:** TOOL-dTotalRecall-58
- AC1 — `marker-in-build-script` — `python record_causes.py --fixture --plant marker-in-build-script` printed PASS and exited 0: its `--check` under `FIXTURE_PINNED` exited 1 with exactly one `RED` line, `RED cause-writer` naming the pinned instrument at its line 13, `tree_lib.py#BIND_HEAD_LINES` plus one, its pinned row still printed and its count line `1 pinned · 0 red` (DERIVED 2026-11-24, this probe). With `id_grammar.py#check_marker_domain` replaced by one returning no finding in a probe script calling `run_fixture`, the plant printed FAIL, its check exiting 0, and exited 1, the staged break the `New arm:` names (DERIVED 2026-11-24, this probe).
- AC2 — `462d20f3..HEAD` — the spelled `git log` at base `12d219431`, piped through `grep -c dTotalRecall`, printed `0`, and the pass commit stages no code file under a build folder (DERIVED 2026-11-24, this probe). The second half, `packet.py --check dTotalRecall`, runs past ten minutes on this node (DERIVED 2026-11-24, the pass 1 return) and was observed through `python tools/chain-packet.py --check dTotalRecall`, the instrument's own `main` and bytes (TOOL-aBatchedPacket-1): exit 0, `byte compare green`, `pin arm 7 instruments, 0 findings` (DERIVED 2026-11-24, this probe).
- AC3 — `marker-in-kept-script` — `python record_kinds.py --fixture --plant marker-in-kept-script` printed PASS and exited 0: its check exited 1 with exactly one `RED` line, `RED alias-compare` naming the script at the path `tree_lib.py#CENSUS_KEPT_PATHS` keeps for `check_alias_compares`, line 14, `tree_lib.py#BIND_HEAD_LINES` plus two, the hit still listed `kept pinned instrument` (DERIVED 2026-11-24, this probe). Under the same staged break the plant printed FAIL, its check exiting 0, and exited 1 (DERIVED 2026-11-24, this probe).
- AC4 — `census: kept` — the spelled `git grep -c` over the build folders' code files printed nothing and exited 1, and the spelled `read_kept_reason(` grep over `tools` listed the definition, `id_grammar.py#scan_readers`, `record_causes.py#read_open_literals`, `record_kinds.py#check_alias_compares` and `id_grammar.py#check_marker_domain`, nothing else (DERIVED 2026-11-24, this probe). Over the real tree neither census listed a red: `104 code files under memory/builds/*/build · 9 census file(s) · 8 kept · 1 pinned · 0 red` and `54 script(s) under memory/builds/*/build · 1 hits · 1 kept · 0 red` (DERIVED 2026-11-24, this probe).
