# TOOL-dWitnessedBar-78 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-78

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21 (`uname -s` `MINGW64_NT-10.0-22621`, GNU bash 5.3.9 `x86_64-pc-cygwin`), through probes of the
code this pass changed: the hook's cut `read_bar_file`, `read_inherited_green` and `read_green_file`,
sourced by `eval` over records written under the scratchpad; the gov suite's new lines, cut from
`rbf_fn=$(awk` to the line-rule failure line, run with `ROOT` at the built hook and at three scratch
copies of it; the suite's canary lines, cut from `check_cr_reached() (` to the `rec_fp` compare, run over
the `clean` plant's record under `%TEMP%/p78g` and `%TEMP%/p78t`; a scratch fixture repository under
`%TEMP%/p78fx` for the guard probes; and the `clean` plant under `%TEMP%/p78vc` for the record read. The
hook passed `bash -n`. The shell-role rows are set to the measured code lines, the hook's 1743 and the
gov suite's 820 (`tools/gate-lint/sh_hygiene.py#measure_code_lines`), widened under
`2026-11-21-build-TOOL-dWitnessedBar-78-widen-21` and `-widen-22`; the hook's base blob already measured
1731 against its row's 1720. The §7 legs and the `New arm:` line's RED-first observation are the main (DERIVED from the builder's probe)
loop's at the close. (DERIVED from the builder's probe)

**Evidences:** TOOL-dWitnessedBar-78
- AC1 — `for count 0` — with `ROOT` at a copy of the built hook whose `read_green_file` has its `_rg_v=${_rg_v%$'\r'}` line deleted, the canary lines printed `gov-canary: the planted CR never reached read_green_file on MINGW64_NT-10.0-22621 for count 0; the CR-strip assertion is not counted`, then the compare's line naming `rec_sha` with `'b…b\r'` and the compare's line naming `rec_fp` with `'c…c\r'`, `a` 0, `fail` 1. Over the built hook they printed nothing, `rgf_seen` ` rec_sha rec_fp`, `a` 2. The arm's own run is OWED at the close.
- AC2 — `for count 0` — unit 70's and unit 72's ledger lines for AC3 now quote that line and the compare's own line, naming `rec_sha` and `rec_fp` respectively, and name `TOOL-dWitnessedBar-78`; the close's grep is OWED.
- AC3 — `diff count` — the canary's `sed` over each liveness variant, `${_rg_v%?}x` and `${_rg_v:1}` for both `sha` and `fingerprint`, changed one line, and each variant differs from the cut in one line; unit 70's ledger line for AC2 names `TOOL-dWitnessedBar-74` AC2 and unit 72's for AC1 names `TOOL-dWitnessedBar-76` AC2, each reading diff count 1.
- AC4 — `git diff --quiet HEAD~1 --` — the criterion's `python -c` printed `tools/ tools/run-gates/ tools/gate-legs.json .githooks/pre-push`; in the fixture repository, after a commit touching `.githooks/pre-push` alone, the command over those pathspecs exited 1.
- AC5 — `{prefix}/.githooks/pre-push` — over a scratch manifest whose gov canary guard drops `.githooks/pre-push` the probe printed `tools/ tools/run-gates/ tools/gate-legs.json`, and over one spelling it `{prefix}/.githooks/pre-push` (with `{prefix}/` dropped too) it printed `tools/run-gates/ tools/gate-legs.json tools/.githooks/pre-push`; on the hook-only commit each exited 0.
- AC6 — `AC7` — unit 73's ledger line for AC7 names `TOOL-dWitnessedBar-78` AC4 and AC5 as the observation of 73 S7; the close's grep is OWED.
- AC7 — `tools/hooks/kit.toml` — the printed pathspecs hold `tools/` and no `*`, `?` or `[`; after a commit touching `tools/hooks/kit.toml` alone the command exited 1, and over the guard without `tools/` it exited 0.
- AC8 — `max_age` — the derivation over the built cut read sixteen pairs, `max_age bg_age`, `blocks bg_blocks` and `base bg_base` among them; over the third record every derived variable read `new`, `fail` 0. With `ROOT` at a copy holding `1ab2e0605`'s `read_bar_file` (`IFS=$'\t' read -r k v`), the arm printed `missing: base max_age blocks` and `these did not read exactly new: bg_fp bg_reused bg_sha bg_st`, `fail` 1.
- AC9 — `read_inherited_green` — the block's awk range piped to `grep -c 'awk'` printed 0 and to `grep -c 'read_inherited_green'` printed 1; over a record holding `sha<TAB>` forty `b` CR-LF and `max_age<TAB>7` CR-LF, `ig_sha` read 40 bytes, `ig_age` read `7`, and a `bg_sha` set to `keepme` before the call still read `keepme`. (DERIVED from the builder's probe)
- AC10 — `run-gates gov canary <- .githooks/pre-push` — the criterion's grep printed one ask row in each `BACKLOG.md`: `PLAY-dConvergedCharter-42` naming `PLAY-dConvergedCharter-41`, `TOOL-dPlacedRequest-74` naming `TOOL-dPlacedRequest-11`, and `TOOL-dWellOiledMachine-130` naming `TOOL-dWellOiledMachine-10` and `TOOL-dWellOiledMachine-17`, each with a `SEV` row. The derivation re-run at this pass printed the same four specs as §4 Evidence, no difference; unit 73's ledger line for AC6 names them and the `--spec` runs.
- AC11 — `Traceback` — over the `clean` plant's record with a `0xff` byte in a value, `read --backend local-hook` printed `verdict: local-hook · GREEN · a69cba9a · …` and exited 0; with the record path a directory it printed `verdict: local-hook · NONE · a69cba9a · no full per-tree verdict at gate-verdict/2fba3d25`; neither stderr held `Traceback`.
- AC12 — `encoding="utf-8", errors="replace", newline=""` — the criterion's `python -c` printed `[]`, and the grep named the record's open in `tools/run-gates/verdict_backends.py#read_local_verdict`.
- AC13 — `pre-push bar self-test` — unit 69's ledger line for AC3 names `TOOL-dWitnessedBar-78` §7 and its three suites; the close's grep is OWED.
- AC14 — `rec_man` — over the fourth record both cuts read the manifest as `x  \t` under `od -c`, `rec_fp` and `bg_fp` empty, and `rec_st` and `bg_st` `on`. Against a copy whose `read_green_file` splits with `IFS=$'\t' read -r _rg_k _rg_v` the arm printed `rec_man`; against one whose loop lacks `|| [ -n "$_rg_l" ]` it printed `rec_st`; each `fail` 1.
- AC15 — `BINMODE` — unit 69's ledger line for AC2 states that `-v BINMODE=3` keeps the CR and the environment form does not, and names `TOOL-dWitnessedBar-78`; the close's grep is OWED.
- AC16 — `Minted` — unit 72's ledger line for AC1 quotes the canary's failure line whole with `for <what>` and names `TOOL-dWitnessedBar-75` as where the `rec_fp` value is minted; the close's grep is OWED.
- AC17 — `one strip serve every key` — unit 72's ledger line for AC3 states S3's reason as that sentence; the close's grep is OWED.
- AC18 — `= refs/heads/master \]` — the criterion's grep printed two assertions, the corrupt-HEAD loop's and `child`'s, each followed by a `73 AC1:` failure line, and `grep -c '71 S3\|71 AC3'` printed 0; unit 71's ledger line for AC3 names `TOOL-dWitnessedBar-73` AC1.
- AC19 — `check-verdict-epoch.test.sh@` — unit 71's ledger line for AC1 names `tools/memory-tree/check-verdict-epoch.test.sh@c9500821b:31-32` and states 35 lines, which `git grep -n GIT_CONFIG_COUNT -- tools` printed again at `1ab2e0605`; the close's grep is OWED. (DERIVED from the builder's probe)
- AC20 — `V.run_local_plant("clean"` — the ban grep printed nothing, and each `grep -c` printed 1.
