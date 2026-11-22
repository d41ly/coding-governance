**Serves:** journal TOOL-dWitnessedBar-75

# TOOL-dWitnessedBar-75 — builder return 1 (run `wf_c4b11e71-5df`), committed 5b7349498

## Why

I built TOOL-dWitnessedBar-75 as its spec, rev-3, states, and committed it as one pass commit carrying the `Pass: TOOL-dWitnessedBar-75` trailer. The spec's claims about the code held at base: the && chain, the one emission site, unit 74's rgf_why chain and the shell-role row at 735. There was no divergence to report.

## Summary

The pass commit is 5b7349498 and the base is dcb2854c4. The canary's failure line now says which check failed first: `count <n>`, then `rec_sha`, then `rec_fp`. Probes over scratch copies of the hook show each break prints its own distinct line. Three things are still owed to you at the close: AC2's scratch-clone runs, AC3's two ledger records, and the New-arm RED-first observation.

**What changed.** In C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh, the canary's single && chain is now an if/elif chain that sets `rgf_what`, the same shape as unit 74's `rgf_why`:
- `count $rgf_n` when the mutant changed anything other than one line.
- `rec_sha` when `check_cr_reached` returns non-zero on the mutant.
- `rec_fp` when the `rgf_mr` measure is not `41 cr`.

A later check never runs once an earlier one has failed. `rgf_ok` is set to 1 only when `rgf_what` is empty, and it is still the flag both compares' counts read. The one failure statement keeps unit 70's prefix and now ends `on $(uname -s) for $rgf_what; the CR-strip assertion is not counted`. I dropped the old chain's `[ -n "$rgf_fn" ]` test: an empty cut changes no line, so the count test already reports it as `count 0`, as S1 says. The commit records this as a `Decided:` trailer.

**Shell-role row.** I ran `ratchet.py widen shell-role`, which wrote memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-75-widen-16.md. The tool only adds 1 to the row, so it wrote 736. The `sh_hygiene.py --shell-role --measure` seed measures the suite at 738, so I set the row to 738 by hand, following unit 51's precedent. That is the second `Decided:` trailer.

**Other files in the commit.** The acceptance ledger memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-75-1-acceptance-ledger.md, and the spec status moved to CLOSED with nothing else in it hand-edited. Also RUN.md and what `gen_build_index.py --write` rewrote: LIVE.md, backlog/TOOL.md, the build README and the spec's records table. No function was added, so I did not regenerate the codebase map. I left help/reference/drive.md and help/reference/units.md unstaged and untouched; they are not this unit's.

**Checks that ran (all probes, standing in for `run-gates gov canary` until you run it at the close):**
- AC1: the criterion's `grep -n` prints one line, and it holds ` for $rgf_what;`. `bash -n` passed on the suite.
- Probe 1 used a hand-built record laid out as the AC12 arm's, with the suite's own `check_cr_reached` and canary lines cut from it. Over HEAD's hook, the no-strip hook, the `sha` variant, the `fingerprint` variant and a file with no `read_green_file`, it gave empty, `count 0`, `rec_sha`, `rec_fp` (measure 40) and `count 0`, matching the spec's Evidence table.
- Probe 2 ran the arm's own lines from `check_cr_reached()` to `rm -rf "$rgf_t"` with `ROOT` at scratch trees and the record built by `run_local_plant`, using `TMPDIR` at `%TEMP%/w75`. HEAD's hook printed no canary line, with fail 0 and a 4. Each break printed only its own ` for <what>;` line, and the liveness lines were `mutant changed 0 lines`, `variant changed 0 lines` and none.
- The bug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`) ran over the commit. I checked the guard-above-a-fold, fixture-finds-nothing, attested-count, ledger-token and synthetic-value classes against the diff, and none needed a change.

**Refused by the hook.** One command was blocked by the scratch-guard because it was the `portability (shell lines only shrink)` leg (`sh_hygiene.py --shell-role <ledger>`), which a builder may not run. It is owed to you at the close.

**Owed to you at the close:**
- The legs of §7: `run-gates gov canary` (with GATE_SELFTESTS), `portability (shell lines only shrink)` against the 738 row, `recall floor`, `recall floor arms` and `memory hygiene`.
- AC2's runs in scratch clones under `%TEMP%`.
- AC3's two red records beside AC2 in unit 70's acceptance ledger, one quoting `for count 0` and one `for rec_sha`, each with its `uname -s`.
- The New arm in tools/run-gates/run-gates.gov.test.sh, covering AC1 and AC2: its RED-first observation needs three staged breaks, a hook with no strip line (reaching `for count 0`), the `sha) rec_sha=${_rg_v%?} ;;` variant (reaching `for rec_sha`) and the same edit on the `fingerprint` case (reaching `for rec_fp`).
