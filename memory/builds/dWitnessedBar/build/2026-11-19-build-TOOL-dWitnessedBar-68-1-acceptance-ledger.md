# TOOL-dWitnessedBar-68 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-68

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21 (GNU bash 5.3.9 `x86_64-pc-cygwin`, git 2.54.0.windows.1, Python 3.15.2), through a scratch
probe that `eval`s the AC12 arm's own lines, cut from `tools/run-gates/run-gates.gov.test.sh` by the arm's
header and its closing `rm -rf`, with `$KITDIR` set to `tools/run-gates`, and keeps the arm's `mktemp -d`
until it has read the record. The suite passed `bash -n`. Its shell-role count, measured by the gate-lint
kit's seed, is 636 past the 611 row, widened under `2026-11-21-build-TOOL-dWitnessedBar-68-widen-10`. The
§7 legs and the `New arm:` line's RED-first observation are the main loop's at the close. (DERIVED from the builder's probe)

**Evidences:** TOOL-dWitnessedBar-68
- AC1 — `od -c` — over the record the arm's call named, `<top>/work/.git/gate-verdict/2fba3d25...`, `od -c` showed `\r  \n` after `G R E E N`, after the forty `b` and after `reused_cache\t0`; `grep -c '^reused_cache'` printed 2 and `grep -c '^selection'` printed 2 (`selection`, `selection.1`); the path's last segment equalled `git rev-parse HEAD^{tree}` run in `<top>/work`.
- AC2 — `rec_sha` — the sourced `read_green_file` over that path set `rec_sha` to forty `b`, and `printf %s "$rec_sha" | wc -c` printed 40; `read_tag_lines` over the same path read `'GREEN'` and forty `b`.
- AC3 — `· GREEN ·` — the arm's local-hook read printed `verdict: local-hook · GREEN · <sha8> · witness witnessed: the full bar, run r1, on tree 2fba3d25`, and the arm counted three assertions with `fail` at 0. Over a scratch `tools/` under `%TEMP%/r68` holding copies of `run-gates/` and `policy/`, its `read_tag_lines` assignment changed to `out.setdefault(...)` (`diff` counted 1 line opening `>`), the same arm printed `· NONE ·` naming `reused 1 leg(s) from the cache` and set `fail` to 1. A call that exits non-zero printed the call's output under the arm's failure line.
- AC4 — `AC12` — `grep -n 'AC12'` over `2026-11-19-build-TOOL-dWitnessedBar-65-1-acceptance-ledger.md` prints line 32, which now names TOOL-dWitnessedBar-68 and its AC3 as the observation of AC12's local-hook half.
