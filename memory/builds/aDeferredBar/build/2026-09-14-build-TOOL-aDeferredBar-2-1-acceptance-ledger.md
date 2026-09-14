# The acceptance ledger — the bar join, its cutoff and its ten arms

**Serves:** journal TOOL-aDeferredBar-2

Every line is OBSERVED or AMENDED, and every observation is the direct command the criterion names,
run by the build pass at rev-4 of the spec. No merge bar and no self-test suite was run for any of
them: the ten fixtures were exercised by running `python tools/check-spec-tokens.py` and `--list` on
each staged fixture directly, once against the checker at `2ca014fd` and once against this one, so
every failing case was seen RED before its arm was written; the suite's own verdict is the main
loop's at `VERIFYING`. The relation refusal was observed on the fixture, and this tree's committed
form on a throwaway commit soft-reset before the build commit, because a commit cannot observe
itself.

**Evidences:** TOOL-aDeferredBar-2
- AC1 — `python tools/check-spec-tokens.py` — exit 1 on the DATED family's fixture; the hit line carries the spec path, `[bar]`, the token and the substitute text. The checker at `2ca014fd` exited 0 on the same fixture, `NOT_A_TOKEN` having dropped the `GATE_`-prefixed token.
- AC2 — `python tools/check-spec-tokens.py` — exit 1 with `[bar]` for the token on the §7 leg line; `2ca014fd` exited 0 with a clean leg join.
- AC3 — `python tools/check-spec-tokens.py --list` — the assert form exited 0 and the listing printed exactly two `NEAR` lines, both `outside the graded population`, one naming the §4 token and one the `New arm:` token, and no line naming `run-selftests.sh`; `2ca014fd` printed no `NEAR` line at all.
- AC4 — `python tools/check-spec-tokens.py` — exit 0 on the spec renamed to 2026-08-30, bar line `0 token(s) examined in 0 live spec(s) at/after SPEC_DIRECT_CUTOFF 2026-09-01 · 1 pre-cutoff live spec(s) carry one and are not graded`.
- AC5 — `python tools/check-spec-tokens.py` — exit 0 with the bar line `SPEC_DIRECT_CUTOFF blank (arm off) · 1 live spec(s) carry a bar token`; the line is absent at `2ca014fd`.
- AC6 — `python tools/check-spec-tokens.py` — exit 0 with `1 waiver(s)` on the WAIVER family's fixture; `2ca014fd` exited 1 there, the `[bar]` row reading as stale because it produced no bar hit.
- AC7 — `python tools/check-spec-tokens.py` — exit 1 with `STALE WAIVER` naming the row's token; a checker copy with the stale-row rule removed exited 0 and printed no such line, which is the observed RED.
- AC8 — `python tools/check-spec-tokens.py` — on the throwaway commit of this tree, exit 0 and the bar line `0 token(s) examined in 0 live spec(s) at/after SPEC_DIRECT_CUTOFF 2026-09-15 · 23 pre-cutoff live spec(s) carry one and are not graded` with no `relation unchecked` field; `grep ^SPEC_DIRECT_CUTOFF= .memory-tree.conf` prints `2026-09-15`, the two §4 Rollout commands return `2026-09-13` and `git log -1 --format=%cs` `2026-09-14`; `git diff --stat b2a330be -- memory/project/spec-token-waivers.txt` printed nothing. Before that commit the same run carried the announced `relation unchecked: value not yet committed` field.
- AC9 — `python tools/check-spec-tokens.py --list` — exit 0; 23 distinct specs on `predates SPEC_DIRECT_CUTOFF 2026-09-15` lines, equal to AC8's carrier count, and none of them unit 3's spec.
- AC10 — `grep -c SPEC_DIRECT_CUTOFF tools/memory-tree/SPEC-TEMPLATE.template.md` and `grep -c SPEC_DIRECT_CUTOFF memory/TEMPLATE-SPEC.md` — `1` and `1`; `head -1 memory/TEMPLATE-SPEC.md` carries `gov:kit memory-tree@2.76`, the value `KIT_MEMORY_TREE_VERSION` holds in `tools/memory-tree/check-memory-hygiene.sh`; the live copy is the canonical `render_doc` of the template, diffed empty.
- AC11 — `bash tools/check-kit-versions.sh` — exit 0; `git grep -l 'gov:kit memory-tree@2.75' -- tools memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides` printed nothing and the same over `2.76` printed nine paths.
- AC12 — `bash skills/session-kickoff/manifest-check.sh` — exit 0 with the record set staged; `last-audit` re-stamped at `c4f02308`, the `git merge-base origin/main HEAD` sha, with no body change and the delta line in the commit message saying so.
- AC13 — `python tools/codebase-map/gen_map.py --check` — exit 0 after `--write` re-rendered `symbols.json` for `extract_acceptance`; `grep -c "Four joins" memory/map/features/spec-tokens.md` prints `1`; `python3 tools/codebase-map/test_codebase_map.py` exited 0.
- AC14 — `grep -c "^SPEC_DIRECT_CUTOFF=\"\"" tools/memory-tree/.memory-tree.conf.example` — `1`.
- AC15 — `python tools/check-spec-tokens.py` — exit 1 with `[bar]` on the light-profile fixture; `2ca014fd` exited 0, the ordinal read having graded `## 6. Gates` as the bullet population.
- AC16 — `python tools/check-spec-tokens.py` — exit 0 and no `[bar]` on `GATE_FULL= cat tools/gate-legs.json`, bar line `2 token(s) examined in 1 live spec(s)`; exit 1 with `[bar]` once the value is restored. rev-1's flag branch, run over the empty assignment in isolation, matched it; rev-3's does not.
- AC17 — `python tools/check-spec-tokens.py` — exit 1 on the DATED family with `SPEC_DIRECT_CUTOFF="2026-09-02"` COMMITTED, stdout `REFUSING — SPEC_DIRECT_CUTOFF 2026-09-02 is not strictly past 2026-09-14, the day the value was committed`, and no `[bar]`, `graded` or `NEAR` line; `2ca014fd` graded the fixture clean at exit 0; the same value merely staged prints the `relation unchecked` field instead.
- AC18 — `grep -c 'a path built at runtime' tools/check-spec-tokens.py` and its four siblings — each `1`; all five printed `0` at `2ca014fd`.
- AC19 — `grep -c '^FLOOR_ASSERTIONS=32' tools/check-spec-tokens.test.sh` — `1`; the suite's `PASS (32 assertions)` line is the main loop's observation at `VERIFYING`, not this pass's.
