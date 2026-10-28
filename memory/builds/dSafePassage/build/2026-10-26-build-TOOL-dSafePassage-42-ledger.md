**Serves:** journal TOOL-dSafePassage-42

# TOOL-dSafePassage-42 — acceptance ledger

The unit as built, at spec rev-7. `tools/govkit/upgrade_steps.py`: `STEP_REFUSED_KEYS` gains
`imap.tunnel` and `instaweb.httpd` (any value) and `sendemail.smtpServer` under the new value rule
`an absolute path` (`/`, `\` or a drive letter) (S7); `read_target_repositories` takes the config
reader `read_target_local_config` hands it and calls it on each repository before any index read
there, a repository it grades refused never having its index read, the gitlink read keeping
`-c core.fsmonitor=false` (S8); a `modules/` row's `reached_by` is the path the worktree's
`.gitmodules` maps the name to, read by `git config -z -f .gitmodules --get-regexp
'^submodule\..*\.path$'`, or the name and `, by name` (S22). The `isolation` family gains
`submodule-fsmonitor` and `submodule-name-differs`. `tools/govkit/selftest.py` gains the `[dSP-42]`
arm and the widened class arm. `tools/push-main.sh`'s `remove_new_untracked` writes its current set
with `write_untracked_snapshot` (S18). `tools/push-main.test.sh` arm 37 counts over check-arms'
`scan_shell_lines` from the `if ! run_gov_first` call (S12, S13), and grades a blanked lander copy.
`tools/run-gates/selftest-budgets.txt` re-prices `push-main self-test` (S27). `help/upgrade-steps.md`
names the three keys (S7) and keeps TOOL-dSafePassage-24's literals (S21).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows, Git Bash) by a probe of the changed code: the fixture CLI, a `python -c` or script
probe, a direct `--prepare` landing over a scratch clone, or the criterion's own command.

Owed at the close: the two `New arm:` lines' RED-first observations — the `[dSP-42]` arm of
`tools/govkit/selftest.py` (red on the index-first walk copy and on a table copy missing
`imap.tunnel`; both reds were observed by probe here, not under the suite) and arm 37's blanked count
in `tools/push-main.test.sh` (red on a counter that reads raw lines) — the §7 legs, and AC6's
`memory/DECISIONS.md` row half.

**Evidences:** TOOL-dSafePassage-42
- AC2 — a scratch clone of HEAD carrying this pass's lander, `feat` with a committed `regen.py` that exits 1: `bash tools/push-main.sh --prepare --slug fx` exited 1, `git status --porcelain` empty; with `regen.py` reverted the retry exited 0, its stderr held no "uncommitted changes or untracked files" line, and HEAD^2 existed. Red, observed: a lander copy that re-takes `gfsnap` after the walk left `?? .governance/install.json` after the refusal, and the retry exited 1 printing the dirty-tree refusal naming `.governance/install.json` — the leftover this fixture's walk makes; no `.governance/steps` or `.governance/outbox` path was left, because no step of this fixture writes one.
- AC3 — `git show "3708a705:tools/push-main.sh" | sed -n '918p;920p'` printed `rm -f "$rgsnap"` and `git add -A`.
- AC4 — a script probe importing `tools/govkit/upgrade_steps.py` by path: over `git help --config` the predicate kept 49 keys, none matching neither table; with the `imap.tunnel` row taken out, `['imap.tunnel']`; `check_target_local_config` over a scratch repository named `imap.tunnel`, `instaweb.httpd` and `sendemail.smtpserver` with `smtpServer = /usr/bin/x` (and `C:/x.exe`), and only the first two with `smtp.example.com`. Red, observed: the same probe over HEAD's module printed `neither ['imap.tunnel', 'instaweb.httpd', 'sendemail.smtpServer']` and refused none of them.
- AC5 — `python tools/govkit/upgrade_steps.py fixture isolation --plant submodule-fsmonitor` exited 1, refusing `core.fsmonitor in .git/modules/sub/config (submodule sub)`, `fsmonitor canary: absent`. Red, observed: a copy whose walk runs `git ls-files -s` before grading printed `fsmonitor canary: present · fsmonitor` and `isolation: FAILED`.
- AC6 — `python tools/drift-audit/drift_report.py --json` read `cutoff_keys_armed` value 37 of 37, tolerance 37; `git grep -n -e "TOOL-dSafePassage-34" -- tools/drift-audit/drift_signals.py` printed line 352, the raise comment. The `memory/DECISIONS.md` row is the main loop's, at the close.
- AC7 — a probe calling `take_write_lock` with `read_boot_clock` stubbed to 12345.5 and `read_pid_namespace` to `pid:[4026532221]` wrote `boot_id, host, pid, pid_ns, platform, started, started_boot, started_utc, verb`; `git grep -n "started_utc" -- tools/govkit` printed one record writer, `govkit.py:7240`, beside a reader (`:7217`) and two fixture plants.
- AC8 — a `bash -c` probe over `git grep -l "^# >>> resolve_python" -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md` less `tools/lib/resolve-python.sh`, every block by ordinal, CR stripped: `files=75 differ=0 memory=0` (DERIVED; 69 at `bb9a4871`).
- AC9 — arm 37's `count37`, run by direct probe with `HERE=tools`, printed 6 for `tools/push-main.sh`, the rows of `PREPARE_REFUSALS`, and 6 for a lander copy carrying `# return 1` and `echo "return 1"` after the call and a comment naming `run_gov_first` above the mint block. Red, observed: the retired `awk | sed | grep -c` counter printed 6 and 10 over the same two files.
- AC10 — an `ast` probe: `upgrade_steps.py` defines `demand_safe_token`, `resolve_shell_argv`, `resolve_bash`, `resolve_tokens`, `target_context`, the eight constants and `Refusal`; govkit redefines none, and `upgrade_steps.py` reaches none of them back off govkit.
- AC11 — the criterion's `git grep … | grep -v` printed one code line, `tools/push-main.sh:938`, inside `write_untracked_snapshot`; `git grep -n "write_untracked_snapshot"` printed the definition and four calls, `:949` inside `remove_new_untracked`. A scratch repository probe of the two functions removed the new untracked files and kept the pre-existing one.
- AC12 — the criterion's `git grep` printed lines 64, 68, 70 and 88 of `help/upgrade-steps.md`, inside "What a step can reach".
- AC13 — `--plant submodule-name-differs` exited 1, refusing `filter.canary.clean in .git/modules/nm/config (submodule lib/p)`, and with the mapping unset `(submodule nm, by name)`, canary absent. The `submodule-filter`, `-stub`, `nested`, `unpopulated`, `unpopulated-worktree`, `main-only`, `local-fsmonitor`, `local-include` and `submodule-url-userinfo` plants and the bare case ran as before.
- AC14 — `grep -n "^BRANCH_PIN" tools/govkit/refusal_join.py` printed line 41; `git show "3708a705:tools/govkit/govkit.py" | sed -n '4684p;5061p'` printed the `not row["missing"]` line and a `kind == "write"` line with no `missing`.
- AC15 — `wsl.exe -d claude-u26 -- python3 -c "…sys.path.insert(0, '/mnt/c/…/tools/govkit'); import upgrade_steps; print(upgrade_steps.read_boot_clock())"` printed `449867.233514815`, and `read_pid_namespace()` printed `pid:[4026532398]`. Red, observed: the path passed as its own argument printed `ModuleNotFoundError: No module named 'upgrade_steps'`. This node has no `Ubuntu` distribution; `wsl.exe -l -q` lists `claude-u26`, run in its place, as TOOL-dSafePassage-31 did.
- AC16 — the criterion's `git grep` printed the `SPEC_DATE` binding (`:884`, from `design_lib.SPEC_FILE_DATE`) and `SPEC_DATE.search("/" + f)` lines, the `ac-order` join's at `:1684`; the file's one other date regex (`:759`) grades a key's value, not a filename.
- AC17 — `grep -n "^push-main self-test" tools/run-gates/selftest-budgets.txt` printed the row at 1032 s: 209 s plus 6 landings (TOOL-dSafePassage-27's 2, TOOL-dSafePassage-28's 4) at 79.8 s, the one `--prepare` fixture landing timed by direct CLI (fixture 14.7 s, landing 65.0 s), x1.5.
