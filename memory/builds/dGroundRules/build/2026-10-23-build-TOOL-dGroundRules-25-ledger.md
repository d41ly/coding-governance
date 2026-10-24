# TOOL-dGroundRules-25 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-25

No merge bar, no gate leg and no self-test suite ran in this pass. The policy kit's criteria were
observed by its fixture CLI on the built tree; the lander suite's arm, the two no-launcher arms, the
build-index selftest arms and the parity cut by reading and by probes of the code they exercise; the
documents by `grep`. The spec-token checker ran in `--dispatch` mode over the live tree, exit 0. Every
`New arm:` line's red-first observation, the §7 legs, and each criterion this ledger names as owed are
the close's. `adopter-fresh-target` is red on this unit's commit, as S7 accepts until
TOOL-dGroundRules-31: the installed policy adopter's `mirror --write` refuses `uncommitted changes` on
install day, so `govkit.py apply` exits 1 and the case grades nothing after it.

**Evidences:** TOOL-dGroundRules-25
- AC1 — `last-valid` — `python tools/policy/check_policy.py --fixture mirror-commit-rewrite` printed each of the four reason kinds `mirror fresh` at the carrying commit and at its commit-tree rewrite, the `last-valid` kind last, `18 assertion(s) executed · 0 wrong`; the red half, its builder staged to format the sha8, is owed at the close.
- AC2 — `regen.py --check` — arm 33 of `tools/push-main.test.sh` runs the real `--prepare` over a policy-file change and reads `regen.py --check` and `mirror --check` at the prepared HEAD; written and syntax-checked with `bash -n`, its run owed at the close.
- AC3 — `push-main: prepared` — the same arm asserts the lander's captured output holds `push-main: prepared` and `HEAD^2` resolves before either check is read; owed at the close.
- AC4 — `bad` — the arm prints `bad` naming `--prepare`'s exit status and reads neither check when the lander refuses; the stub-staged observation is owed at the close.
- AC5 — `legacy-homes.txt` — `--fixture adopter-fresh-target` now asserts no `legacy-homes.txt` installed and the `not graded · the list is gov's own` line on every `--check`; it reads red on this commit at `govkit.py apply ... exited 1` (`uncommitted changes`), so this is owed at the close, after TOOL-dGroundRules-31.
- AC6 — `requires` — the case selects `policy`, `run-gates` and the closure of `requires` read as registry ids, its apply line naming `--kits policy,run-gates,memory-tree`; the staged `agent-cap` observation is owed at the close, after TOOL-dGroundRules-31.
- AC7 — `regen.py --check` — the case re-runs the installed memory-tree adopter and the policy adopter's `--scaffold` after the first commit, commits the mirror and runs the installed `regen.py --check`; owed at the close, after TOOL-dGroundRules-31, as S7 states.
- AC8 — `empty` — the case joins each README row's last column to its `ARMS` entry's `empty`; owed at the close, after TOOL-dGroundRules-31.
- AC9 — `ORDER [project-owned]` — `--fixture legacy-homes-withheld-install` printed `ORDER [project-owned] tools/policy/legacy-homes.txt` as the plan's one row for the list and `none held` in the applied target, `2 assertion(s) executed · 0 wrong`.
- AC10 — `legacy-homes` — `grep -n "ORDER" README.md` under the kit prints the `legacy-homes` row saying the plan's `ORDER [project-owned]` row is informational and the list is not the adopter's to author.
- AC11 — `legacy-homes.txt` — the adopter-list phase of `adopter-fresh-target` writes `legacy-homes.txt` beside the installed kit and asserts the announce line with no finding; its run is owed at the close, after TOOL-dGroundRules-31.
- AC12 — `kit check-line-length not installed` — `--fixture census-default-adopter` printed `cap census: line-length · kit check-line-length not installed`, `manifest-bytes graded at tools/manifest-check.sh`, `no finding`, `2 assertion(s) executed · 0 wrong`.
- AC13 — `--fixture budgets-ships-join` — it printed `35 assertion(s) executed · 0 wrong` and `--fixture fixtures-guard-census` `33 assertion(s) executed · 0 wrong` on the built tree, each locating the registry and `gate-legs.json` from the kit's resolved tool root; the foreign-prefix copy is owed at the close.
- AC14 — `memory/guides/REVIEW-PROTOCOL.md` — `grep -c "gov:fixed-writers" tools/workflows/REVIEW-PROTOCOL.template.md` printed `1`, and the dogfood copy holds the same receiver line.
- AC15 — `### The predicate` — `grep -n "gov:fixed-writers" memory/guides/REVIEW-PROTOCOL.md` printed line 86, after `### The predicate` and before the line opening `Everything else is denied`.
- AC16 — `grep -c "cannot resolve to an integer ≤" tools/hooks/README.md` — printed `1`; S16 held at HEAD.
- AC17 — `MAX_VERIFIERS` — the AC17 `grep -nE` over `memory/map/features/agent-cap.md` printed nothing, and the card names `MAX_VERIFIERS` and `runtime.agents-in-flight`; S17 held at HEAD.
- AC18 — `KIT_AGENT_CAP_VERSION` — the render reads the resolved hook's `KIT_AGENT_CAP_VERSION` against the floor 1.40; the compare printed 1 (fallback) for `1.39`, `0.99` and an empty version and 0 for `1.40`, `1.41` and `2.0`, and the substitution rewrote the template's split to `Math.min(SPEC_WRITERS, 5))) // gov:fixed-verifiers`. Probed further: both the hook at HEAD and the pre-writer hook of main deny that fallback (`a cap which this file does not show to be bounded`), which TOOL-dGroundRules-30 S3 judges; the scratch-copy render is owed at the close.
- AC19 — `.agent-cap.conf` — `--fixture guard-mirror-beside-conf` printed `guard.py --staged · exit 1` naming `its input .agent-cap.conf is staged changed`, `3 assertion(s) executed · 0 wrong`.
- AC20 — `uncommitted changes` — with an uncommitted `.agent-cap.conf` in a scratch worktree, `python tools/policy/policy.py mirror --write` exited 2 printing `policy: refused · .agent-cap.conf:0 · uncommitted changes; the mirror renders a revision, commit first`.
- AC21 — `--fixture guard-mirror-inputs-join` — it printed the guard refusing `.zz-recorded.conf`, the extra recorded input, by name, `3 assertion(s) executed · 0 wrong`.
- AC22 — `\r` — `python tools/policy/policy.py mirror --print` captured as bytes held 44626 bytes and 0 `\r`.
- AC23 — `policy fixtures` — `python tools/check-spec-tokens.py --legs-for tools/gate-legs.json` named `policy fixtures`.
- AC24 — `backlog.py` — `fixtures-guard-census` walks the census enforcers' imports and sourced files and the guard now carries `{prefix}/memory-tree/backlog.py` among fourteen modules; the staged-out observation is owed at the close.
- AC25 — `check-spec-tokens.py` — the case pipes its paths to `check-spec-tokens.py --legs-for -` and reads an unreachable checker as `WRONG`; the staged-absent observation is owed at the close.
- AC26 — `--fixture arms-empty-declared` — it printed every `ARMS` entry's `empty` and why, `12 assertion(s) executed · 0 wrong`; the staged-off red and the fresh-target half are owed at the close, the latter after TOOL-dGroundRules-31.
- AC27 — `arm_schema` — `--fixture arms-empty-target` printed the three arms `not graded` over the empty target and `arm_schema · 0 finding(s) · 4 key(s)` over the scaffolded one, `4 assertion(s) executed · 0 wrong`.
- AC28 — `resolve_bash_py` — the awk cut of the `resolve_bash_py` block from `check_policy.py` and from `resolve_bash.py` under `tools/lib/` compared identical; the one-byte red is owed at the close.
- AC29 — `--fixture adopter-suite` — the case prints `WRONG` unless the suite exits 0 and names its arm count, and on a bash `resolve_bash` cannot find; it reads red with arm 4 until TOOL-dGroundRules-31, so both staged observations are owed at the close.
- AC30 — `file` — `--fixture on-invalid-bom` printed `stdout 'refuse'` with `policy: budgets.enforce · file · set in .governance/policy.toml`, `1 assertion(s) executed · 0 wrong`.
- AC31 — `is-shallow-repository true` — `--fixture on-invalid-shallow` printed `is-shallow-repository true` before its verdict and `history is shallow at 17907ad1; fetch more history`, `3 assertion(s) executed · 0 wrong`.
- AC32 — `.claude/settings.json` — `--fixture limit-settings-env-stale` printed `regen: STALE · stage 1 · policy · .claude/settings.json` (exit 1) and `GOV_SETTINGS_JSON names it, and it is not a file` (exit 2), `2 assertion(s) executed · 0 wrong`.
- AC33 — `--fixture limit-settings-elsewhere` — it printed the hard link keeping the old bytes, the target a new inode and no temporary file left beside it, `6 assertion(s) executed · 0 wrong`.
- AC34 — `grep -c "boundedParallel" tools/check-playbook-parity.test.sh` — printed `0`, and the valid fixture writes the re-pointed rule-2 sentence.
- AC35 — `fail 5` — `tools/check-template-size.sh` under a PATH whose three launchers exit 9009 exited 5 printing `TEMPLATE-SIZE check 5 FAILED — ... no python launcher resolved`, the refusal A24 asserts; `python tools/memory-tree/check-arms.py --report` printing it `ARMED` is owed at the close. The hygiene checker under the same PATH exited 2 printing `HYGIENE — no usable python`, the line its new arm asserts.
- AC36 — `grep -c "derive_lowered_limit" memory/map/generated/symbols.json` — printed `1` after `gen_map.py --write` in this unit's first commit, which the pre-commit codebase-map gate passed; `derive_census_tree` sits there too.
- AC37 — `build-index selftest` — `derive_parallel_step` answered `no` for one unit's path under the other's directory token and `yes` for disjoint paths, in process; the selftest arms are owed at the close.
- AC38 — `no` — `derive_parallel_step` answered `no` for a unit consuming from its step's other unit, in process; the selftest arm is owed at the close.
- AC39 — `| no |` — the build-order rows of steps 4, 6 and 7 in `memory/builds/dGroundRules/README.md` (lines 251, 253, 254) end `| no |`; the criterion's `grep -nE` also prints three design-clause rows of the same numbers (lines 62, 64, 65), which carry no Parallel column.

Owed at the close, observed by no command in this pass: each `New arm:` line of §7 red on its staged break and green restored, and `adopter-fresh-target`, `limit-fresh-target-spawn` and `adopter-suite`, red until TOOL-dGroundRules-31.
