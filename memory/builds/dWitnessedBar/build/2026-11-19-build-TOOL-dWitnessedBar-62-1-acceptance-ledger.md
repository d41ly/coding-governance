# TOOL-dWitnessedBar-62 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-62

This pass ran no merge bar, no gate leg and no self-test suite. Every criterion marked observed was
checked on node d on 2026-11-20 by probing the unit's own code: the `grep` and `awk` lines each
criterion spells, run over the built tree; `regen.check_when` and `resolve_generated_indexes` over a
scratch tree under `%TEMP%/w62b` holding every `when` form; selfcheck's `_check_exists_refused`, cut from
`tools/govkit/govkit.py#selfcheck` and run over each form; the plants `ratchet.py --fixture --plant
deleted-conf` and `untracked-conf` and `verdict_backends.py --fixture --plant peer-no-ssh-keygen` and
`clean`; `refuse-wrong-shell.sh --coverage` over the built tree and over the five-spelling fixture built
as the suite builds it under `%TEMP%/w62r`; `legacy_ledger.py seed --home` inside a `git worktree add`
fixture under `%TEMP%/w62l`; and the one-scaffold seed-across fixture, its registration and its save,
commit, clear, re-seed and compare, run by hand under `%TEMP%/w62e`. Criteria only a suite or a leg can
observe are OWED to the close, with each `New arm:` line's RED-first observation: `govkit selftest`,
`memory-hygiene self-test`, `run-gates evidence`, `pre-push self-test`, `pre-push bar self-test`,
`python resolver (behaviour + inline parity + idiom ban)`, `drift-audit selftest`, `run-gates gov canary`,
`memory hygiene` and `recall floor`.

**Evidences:** TOOL-dWitnessedBar-62
- AC1 — `not compared` — OWED to the close (`govkit selftest`): `check_when_forms_agree` reads the admissible tree through `build_items` together and prints the row lacking `write`, `check` and `stage` as `not compared tools/run-gates/kit.toml {kit}/w54-bare.out`. Observed by probe: `regen.check_when` holds conf-true and present and not conf-false or absent, and `resolve_generated_indexes` printed the conf-true and present pairs alone.
- AC2 — `Refusal` — observed by probe: `check_when` raised `Refusal` for the unknown-token, empty-path, no-colon, absolute (`/run-gates/regen.py`, `C:/x`) and `..` forms; lib-unattended named `tools/run-gates/kit.toml` and each `when` on stderr and kept the conf-true pair; `_check_exists_refused` read True for the absolute, drive and `..` paths and False for `{prefix}/govkit/govkit.py`. The arm's selfcheck runs and its RED with lib-unattended's containment case removed are OWED to the close.
- AC3 — `cp "$_sk/.memory-tree.conf.example"` — `grep -c` printed 1 (2 at base). Observed by hand over the fixture: the scaffold armed `conf-scalar-pins 1`, the listing run armed `row-duplicates 0`, `date-cutoffs 26` and `seed-across-fixture 1` and printed `present` for the rest, and the compare printed `compared` and `shas … null-then-head` for all four. The suite's run is OWED (`memory-hygiene self-test`), FLOOR_ASSERTIONS 796 to 797.
- AC4 — `git ls-files` — observed by hand: `seed-across-fixture` was armed by the listing run and compared after the commit, one row `.memory-tree.conf`. Its RED with the seed reading `git ls-files` tracked-only is OWED to the close.
- AC5 — `run-gates gov canary` — OWED to the close: the main loop runs that leg and writes unit 43's AC1, AC2 and AC4 lines and unit 56's AC15 line naming it.
- AC6 — `FLOOR_ASSERTIONS` — observed: `grep -n 'RAISED .* by TOOL-dWitnessedBar-'` names 40, 41, 42, 51, 56 and 60 in the evidence suite, now 62 (311 to 312); 43, 56 and 60 in the gov suite; 45 and 56 in the adopter suite; 46, 51, 53 and 56 in the hygiene suite, now 62 (796 to 797). No arm of this unit lands in the gov or adopter suite, so those floors are unchanged; each floor against the executed count is OWED to the close.
- AC7 — `FAIL executed` — OWED to the close: one listed unit's arm deleted from each suite in a scratch copy.
- AC8 — `selection.1` — OWED to the close (`run-gates evidence`, `pre-push bar self-test`): the evidence suite's empty-note runner arm and the hook suite's `empty` case in both selection loops are built; read: the runner writes `selection.1` from the row's text past `held<TAB>` and hashes the row's text.
- AC9 — `no gate-verdict written` — observed: the three-term loop in `tools/run-gates/` printed nothing and the count printed 2.
- AC10 — `build_commit` — OWED to the close: the call over `cdfbd1cf..HEAD` for `TOOL-dWitnessedBar-24`.
- AC11 — `selection_row` — observed: `grep -n '^selection_row|'` names line 441 of `tools/lib/resolve-python.test.sh`, and the `# >>> selection_row` cuts of `verdict_flow.py` and `drift_report.py` diffed empty; `read_selection_holds` over a scratch selection held a, b and e and not the `bogus` mode or source rows. The one-byte break is OWED to the close.
- AC12 — `--selection` — observed: `drift_report.py --gate-health --fixture differs --selection <empty>` exited 0 printing `gate-health fixture differs ok`, and the `-A1` grep shows `--selection` in each README call. The ledger lines of unit 1's AC1 to AC4 and unit 51's AC17 are OWED to the close.
- AC13 — `derived from 96 files` — observed: the §4 probe printed `86 10 96` and `--coverage` printed `93 members, derived from 96 files`, with the widened reader.
- AC14 — `exists:` — observed: the grep names the README's `when` paragraph and lib-unattended's header comment, each naming the absolute and `..` refusal and the absent-path silent skip.
- AC15 — `not in the work tree` — observed: `python ratchet.py --fixture --plant deleted-conf` printed two PASS lines and `1 cases, 2 checks, 0 failed`.
- AC16 — `GREEN` — observed: `python verdict_backends.py --fixture --plant clean` held both scenarios, the second reading `local-hook · GREEN`. The hook suite's parity arm is OWED (`pre-push bar self-test`).
- AC17 — `--coverage` — observed: over the fixture `--coverage` printed `never calls refuse_wrong_shell` for `elif.sh`, `while.sh`, `dollar.sh`, `backtick.sh` and `group.sh` and nothing for `hashed.sh`; the built tree stays `derived from 96 files`. The suite's arm is OWED.
- AC18 — `outside the tree` — observed: inside the linked worktree `--home .git` and `--home nested/.git` printed `unarmed … outside the tree` with exit 1 and the gitlink byte-identical, and `wtdir/rel.txt` and the absolute `wtdir/abs.txt` printed `armed`. The suite's arm is OWED.
- AC19 — `govkit.py selfcheck` — OWED to the close: unit 57's AC18 line names unit 54's AC2 line.
- AC20 — `FOO_PIN` — observed: `python ratchet.py --fixture --plant untracked-conf` held both checks, the leg exiting 1 naming `.x.conf FOO_PIN` as an undeclared site.
- AC21 — `memory/LIVE.md` — OWED to the close: unit 54's AC1 call in the S33 clone.
- AC22 — `tracked root` — observed: the grep over the two memory-tree docs and `memory/HYGIENE.md` printed nothing.
- AC23 — `tail.AbCd1234` — OWED to the close (`run-gates evidence`): present at HEAD, this pass writes none.
- AC24 — `awk '/^read_policy_key` — observed: the `grep -c` printed 1; the cut `eval "$(awk …)"` under bash read the sentinel `K=plain` as `plain` and `land` then `park` as `park`. The arm's twelve graded rows are OWED (`govkit selftest`).
- AC25 — `witness` — observed: `python -I inherited_red.py witness` over a gate file holding `#   INHERITED_RED=park|land`, `INHERITED_RED_MAX_AGE=10` and `export INHERITED_RED=park` named line 3 alone, and a spaced indented assignment line too.
- AC26 — `--plant peer-no-ssh-keygen` — observed: the plant held both scenarios, the second printing `signer temps left: 0`.
