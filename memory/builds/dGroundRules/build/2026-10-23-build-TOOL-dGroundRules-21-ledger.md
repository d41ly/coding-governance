# TOOL-dGroundRules-21 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-21

No merge bar, no gate leg and no self-test suite ran in this pass, the lexicon's `--suggest`
excepted; a hook refused the one direct run of the spec-token checker, which `--dispatch` ran
instead. Criteria a fixture observes were observed green by the kit's fixture CLI on the built tree,
one named case per run; criteria a grep observes, by that grep; the rest by in-process probes of the
changed code or by scratch repositories under the system temp directory. Each `New arm:` line's
red-first observation, and every leg §7 names, are owed to the close. Three were observed red here
on HEAD's code as well: the scaffold's CR bytes (AC1), the hook's silent missing guard (AC21) and
the fresh target's twelve findings before this unit, nine after it.

Two observations depend on units after this one. `budgets-switch-refuse`, `budgets-pinned-warn`
and every `budgets-cap-` case's `warn` half read `refuse` once S12 refuses the derived default of
an unset `budgets.<cap>` and S31 reads that refusal as a refused reader; TOOL-dGroundRules-62 types
that one refusal and reads it as "no file value", as its §1 states. And `adopter-fresh-target`
keeps nine findings on this host, whose `git init` names its branch `master`: `arm_mirror_landed`
and the reader-coverage arm meet a landed revision that does not resolve, and `arm_mirror_parity`
an absent mirror under a HEAD carrying the policy file, which TOOL-dGroundRules-25 S7 and S26 close.

**Evidences:** TOOL-dGroundRules-21
- AC1 — `od -c` — `python policy.py scaffold | od -c | grep -cF '\r'` printed `0`, and `cmp` of its bytes against `git show HEAD:.governance/policy.toml` was equal; HEAD's `policy.py scaffold` piped the same way printed `8`.
- AC2 — `git check-attr eol` — over the policy file, `catalogue.toml`, `caps.toml`, `legacy-homes.txt` and `unsummarised-keys.txt` under the kit, each printed `eol: lf`.
- AC3 — `KIT_POLICY_VERSION` — `grep -c "gov:kit policy@" README.md` printed `1`, and `grep -n "version_from" kit.toml` printed line 9 naming `KIT_POLICY_VERSION`.
- AC4 — `python tools/memory-tree/check-arms.py --report` — it printed `adopt-policy.sh -> adopt-policy.test.sh` with the three `exit` sites ARMED and none waived, and `--emit-floors` printed the row `tools/policy/adopt-policy.sh:3:3` now in `ARMS_FLOORS`; `--fixture adopter-suite` ran the suite, whose `--check` arm over `runtime.agents-in-flight = 0` exited 1: `==== 8 passed, 0 failed ====`.
- AC5 — `--fixture adopter-fresh-target` — both `--check` runs printed `arm_schema` grading the scaffold's 4 keys and `arm_mirror_readers` the memory-tree kit's staged code files with no finding, and the planted `Arm` printed one finding under `finding` and `not graded` under `announce`; the reader-coverage arm printed `not graded · 0 of 267 catalogue key(s) graded for a reader, no owner build landed` in an in-process probe over this repository, whose landed revision resolves, and in the case a finding for the unresolvable landed revision named above.
- AC6 — `grep -cE "(pre-push|push-main.sh|post-merge.sh|unattended.sh):[0-9]" README.md` — it printed `0`, and the `-e "read_policy_key()"` grep printed lines 202 to 205, the four copies by symbol.
- AC7 — `compare_base_py` — the awk cut of the block from `map_lib.py`, `policy.py` and `compare_base.py` was identical; a scratch copy of `policy.py` with one byte changed in the block still carried the marker on line 416 and its cut differed.
- AC8 — `# >>> remote_ladder_py` — `grep -c '^def resolve_remote' policy.py` printed `1`, and the awk skipping that range piped to the grep printed nothing.
- AC9 — `git_env_leaks_py` — the cuts from `policy.py` and `git_env_leaks.py` were identical, and `tree_lib.GIT_ENV_LEAKS == policy.GIT_ENV_LEAKS` printed `True`.
- AC10 — `--fixture on-invalid-utf16` — `get budgets.enforce --rev HEAD --explain` printed `refuse` with source `last-valid` and a reason holding `not UTF-8: 'utf-8' codec can't decode byte 0xff`; 1 assertion, 0 wrong.
- AC11 — `read_policy_text` — `grep -n "read_blob_at(" policy.py budgets.py` printed the definition, the call in `read_policy_text` and the limits read in `budgets.py`.
- AC12 — `--fixture resolution-derived-default` — `get zz.derived` exited 2 naming the row and `a derived default no reader computes yet`, and `mirror --print` there rendered 254 keys, none `zz.derived`; 2 assertions, 0 wrong.
- AC13 — `--fixture on-invalid-shallow` — the `--depth 1` clone refused `history is shallow at <sha8>; fetch more history`, and the full clone read V from `last-valid`; 2 assertions, 0 wrong.
- AC14 — `--fixture mirror-landed-parity` — with a `bash.bat` exiting 127 first on `PATH`, where `shutil.which` found it, the case named `C:/Program Files/Git/bin/bash.exe` as the shim's bash and passed: 4 assertions, 0 wrong.
- AC15 — `--fixture mirror-absent-adopter` — over a HEAD carrying neither file and over no commit, `arm_mirror_parity` and `arm_on_invalid` each printed `not graded` and no finding; 4 assertions, 0 wrong.
- AC16 — `--fixture mirror-shim-exit-one` — `node policy-mirror.js get budgets.enforce` exited 2 with a `PolicyRefusal` naming `status 1` for the shim exiting 1, and `status 2304` for the one killed by `kill -9 $$`, which this host's bash reports as an exit; 3 assertions, 0 wrong.
- AC17 — `--fixture mirror-stale-legacy` — a landing changing `.agent-cap.conf` alone was read through the shim, `2`, its reason opening `mirror stale at`; 2 assertions, 0 wrong.
- AC18 — `--fixture mirror-direct-reader` — RED as planted, and green unplanted with the consumer's only mention of `policy.json` in its `//` comment line.
- AC19 — `git check-attr eol` — over `.governance/policy.json` it printed `eol: lf`, the pin at HEAD unchanged.
- AC20 — `grep -c "def arm_single_reader" check_policy.py` — it printed `1`, and the `def arm_(mirror|limits)_readers` grep printed nothing.
- AC21 — `policy guard` — a scratch repository whose `core.hooksPath` held a copy of `.githooks/pre-commit`, its list at HEAD and no `guard.py`, committing the staged policy file from this shell exited 1 printing `pre-commit: policy guard REFUSING`; HEAD's hook in the same repository exited 0 and printed no such line.
- AC22 — `--fixture guard-admits-raise` — it admitted `budgets.".claude/skills/x/SKILL.md" 100 -> 120`; `guard-lowered` refused it as a lowering and `guard-class-row` refused `budgets."memory/builds/*/spec/"` as no measured-file cap, each 0 wrong.
- AC23 — `grep -c "resolve_compare_base(" policy.py` — it printed `2`, the definition and the one call in `cmd_lists`.
- AC24 — `--fixture legacy-homes-main-dropped` — the branch's `lists --check` exited 0 with no report and no `new legacy home`; 1 assertion, 0 wrong.
- AC25 — `--fixture reader-coverage-relocated` — at `vendor/gov/policy/` the arm graded the landed owner, `1 finding(s) · 1 of 1`, and with `tree_lib.py` gone it refused, both never `not graded`; 2 assertions, 0 wrong.
- AC26 — `memory-tree` — `grep -n "requires" kit.toml` printed `requires = ["memory-tree"]`, and the relocated case's second scenario printed `requires memory-tree, which does not resolve: no memory-tree kit holding tree_lib.py in this install: looked in` three paths.
- AC27 — `--fixture reader-quoted-pattern` — `resolve(f'budgets."{cap}"')` and the joined form each graded `budgets.*` with no finding, and with neither it red; `grep -c 'parse_key("policy-file.on-invalid")' policy.py` printed `2`.
- AC28 — `--fixture budgets-zero-cap` — `"index-lines" = 0`: `policy.py check` exited 0, `is valid`, and the hygiene enforcer under `refuse` exited 0 over an index past every other value; 2 assertions, 0 wrong.
- AC29 — `arm_limits_readers` — an in-process probe over this repository printed `0 finding(s)` over 176 tracked code files, naming neither file.
- AC30 — `--fixture limits-reader-docstring` — a docstring and a comment with a read shape stayed green and a line opening the file red; 2 assertions, 0 wrong. The live arm over this repository is the probe of AC29; `python check_policy.py` as a leg is owed to the close.
- AC31 — `--fixture budgets-reader-refused` — two remotes and no `GOV_REMOTE` under `warn`: `check-template-size.sh` exited 1, check 2, saying `Name it: export GOV_REMOTE=<remote>.` once and no `BUDGET WARN`; with stub launchers first on `PATH` it exited 5 saying `no python launcher resolved`; 2 assertions, 0 wrong.
- AC32 — `AGENT_CAP` — `grep -n "AGENT_CAP" memory/map/features/agent-cap.md` printed nothing; the line now states rule 7, `runtime.agents-in-flight` and the writer and verifier bounds.
- AC33 — `grep -c "AGENT_CAP=7" tools/workflows/check-review-join.test.sh` — it printed `0` at HEAD and now, the stub predicate already planted; the D7 arm's text `is its own refusal and not a join` is in the file once, and its run is owed to the close.
- AC34 — `--fixture limit-settings-elsewhere` — `settings --write` under `GOV_SETTINGS_JSON` wrote that file and not `.claude/settings.json`, rule 7 admitted at 2, refused unset naming `.claude/settings.json`, and refused at 3 naming the named path; 5 assertions, 0 wrong.
- AC35 — `grep -c "bounded-helper width" tools/check-playbook-parity.sh` — it printed `0`; the hooks README grep printed line 76, the remedy's example, and line 118, the surviving verifier bound, neither a denial of the raw primitive or the clamp.
- AC36 — `agent-cap@` — the `git grep -hoE` over `tools/hooks/*.js` printed two rows, `KIT_AGENT_CAP_VERSION = '1.40'` and three `agent-cap@1.40`, no bump made.
- AC37 — `--fixture limit-fresh-target-spawn` — `adopt-policy.sh --scaffold` over a committed target wrote the settings at 6, and the first `Agent` payload exited 0; 2 assertions, 0 wrong.
- AC38 — `--fixture limit-hook-settings-malformed` — a `{` settings file exited 2 naming `.claude/settings.json` and a cwd in no checkout exited 2 naming it; `limit-hook-reader-throws` exited 2 naming `reading the landed limit` and the planted throw; 3 assertions, 0 wrong.
- AC39 — `grep -cE "git show [0-9a-f]{7,40}:" tools/hooks/agent-cap.test.sh` — it printed `0`.
- AC40 — `grep -n "os.replace" policy.py` — it printed the settings write at line 940, and `grep -n "UNVERIFIED" agent-limit.md` printed line 37, the restart claim; the two-halves probe needs live sessions and is owed to the close.
- AC41 — `python tools/codebase-map/gen_map.py --check` — `gen_map.py --write` rewrote `symbols.json` for this unit's functions; the `--check` leg is owed to the close.
