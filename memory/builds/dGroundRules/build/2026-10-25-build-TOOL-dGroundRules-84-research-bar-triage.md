# Research — the close's bar pre-check at cae57b1d8: ten red legs triaged into three fix units

**Serves:** research TOOL-dGroundRules-84
**Commissions:** TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86

A gov-researcher triaged the ten legs the bar pre-check at `cae57b1d8` failed, each green at the
run's base `3c2b69be4`, from the recorded per-leg output (the run's scratchpad
`bar-reds-cae57b1d8.txt`). Introducing commits come from `git blame` and `git log -S` against the
base; where a later commit restyled a line, blame names the last toucher. The researcher ran eleven
read-only leg commands in the worktree before the scratch guard stopped it; its role allows none, the
tree status was identical before and after, and the outputs matched the recorded log.

## The ten legs

1. **kickoff-manifest ratchet.** `memory/guides/SESSION-KICKOFF.md` audit block, `last-body-change:
   f221e1135`: 20 watched commits since, the tenth `f6674a6a2` (-21). Fix: re-audit §B against the
   tree and advance `last-body-change`. One stale claim found: §B lines 171-172 call raising the
   template ceiling "an owner decision, not an edit", while since `69aa76517` (-9) the ceiling is read
   through the policy kit's `budgets.<cap>`. Precedent `d85890512` (TOOL-dTrueNorth-27).
2. **memory hygiene.**
   - Check 25: `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md` S30
     **Readers:** names `loadDeclaredCap`, which `2ebafd441` (-10) removed from
     `tools/hooks/agent-cap.js`. Fix: a rev of that spec pointing the Readers clause at
     `read_legacy_fanout` in `tools/policy/policy.py` (spells `FANOUT_CAP`) and `LEGACY_FANOUT`.
   - Check 23: `memory/builds/dGroundRules/build/2026-10-23-build-TOOL-dGroundRules-34-ledger.md`
     line 51 (AC32), from `75b1ffe59` (-34); check 23 is skipped under `--staged`, so no per-commit
     run saw it. Fix: carry the backticked token `gen:build-order` in the AC32 answer.
3. **shell hygiene, location probe.** `tools/check-template-size.sh:92,93`, two bare
   `git -C "$_dir" rev-parse --show-*`, from `69aa76517` (-9). Fix: open both with
   `(unset GIT_DIR GIT_WORK_TREE; …`, the lint's own remedy.
4. **shell hygiene, fork spent on builtin work** (12 findings).
   - `.githooks/pre-commit:204` (-6, `4c1f59ccd`): `pg_names=${pg_hit//$'\n'/ }`.
   - `tools/check-line-length.sh:165` (-9): a first-line parameter expansion for the `printf` to
     `head -n 1` substitution.
   - `tools/check-template-size.sh:90` (-9): the `dirname` fallback rewritten in the
     `adopt-branch-reconcile.sh:25` form; the var-pipe row lowered to 2.
   - `tools/check-spec-tokens.test.sh` (-46, moved by -56): two printf substitutions become
     `printf -v`.
   - `tools/hooks/agent-cap.test.sh`: the stale pure-fn-subst row 117 of
     `memory/project/spawn-idiom-sites.txt` is deleted (-10 drained its sites).
   - `tools/policy/adopt-policy.sh:28` (-1): the `adopt-branch-reconcile.sh:25` form.
   - `tools/policy/policy-shim.sh:38,39,57` (-5): the byte-identical inline copy of
     `tools/lib/resolve-remote.sh`; a registry row whose reason follows the `run-held-wsl.sh` row
     (converts only with its canonical copy), not a conversion.
   - `tools/push-main.test.sh` (-25, the arm-33 block near lines 1086-1112): var-pipe 15 to 19 and
     one pure-fn-subst, converted to parameter expansion or `[[ =~ ]]`.
   - `tools/workflows/check-protocol-parity.test.sh:553,604` (-10, -30): the indent pipe through
     `sed` becomes a `printf '  %s\n'` over a parameter expansion.
   - `tools/workflows/unattended-build.test.sh` (-74): cat-file 1 to 4, converted to `$(<f)`, the
     redirected-read site guarded by a file test instead.
5. **shell hygiene, fixed-name temp.** `tools/policy/adopt-policy.sh:99` writes `"$FILE.tmp"` (-1,
   restyled by -21). Fix: `mktemp -u "$FILE.XXXXXXXX"` then `mv`.
6. **spawn budget.** memory-hygiene 240 against 189 at `check-memory-hygiene.sh:527,534` (20 forks
   each plus a per-key `grep -qE` loop); manifest-check 105 against 90 at `manifest-check.sh:1337`
   (`read_budget_field` three times, plus the new `resolve_python`, `resolve_kit_file` and a python
   start), all from `69aa76517` (-9)'s per-cap readers. Fix: parse the budgets answer once in-shell.
   Risk: that recovers about 50 forks for memory-hygiene but about 6 of manifest-check's 15; the rest
   is -9's python start, and `fork-ceilings.txt` ceilings only shrink.
7. **install-prefix** (34 spellings). Test fixtures in `agent-cap.test.sh`, `govkit/selftest.py`
   and `check_policy.py`; prose and docstrings in `tools/policy/README.md` and `check_policy.py`;
   code in `check_policy.py`, `policy.py`, `.githooks/pre-commit` and `check-spec-tokens.test.sh`.
   Fix: derive each path from the suite's own names or `resolve_kit_dir`, spell prose as
   `<tool-root>/…`, and rename the fixture's `hooks/consumer.*` directory to a non-kit name. One is a
   checker false positive: `tools/policy/caps.toml:87` `limits:.claude/skills/unattended/SKILL.md`
   passes on line 83 without the `limits:` prefix, so `check-install-prefix.sh`'s rule-3 operand
   split should also split on `:`.
8. **method carriers.** `tools/policy/caps.toml:63,67` and `tools/policy/check_policy.py:3488,3757`
   (-9). Fix: two rows in `memory/project/method-carriers.txt` in the
   `tools/template-size-limits.txt` row's shape (a size-cap subject, never a restatement).
9. **harness arms.** `tools/check-template-size.sh:76` check 7 branch 1; its arm A15 at
   `check-template-size.test.sh:141` stops at `(given`. Fix: extend the expected text to the whole
   signature, `(given 9999 )`.
10. **govkit runbook parity** (19 problems against a pin of 18). The registry entry `policy` has no
    `<!-- govkit:entry policy -->` section in `WIRE-INTO-PROJECT.md` (-1). Fix: a non-empty anchored
    section spelling kit paths only as `<tool-root>/…`.

The working tree also reds hygiene check 9 from the staged rescope; the commit that lands it runs
`gen_build_index.py --write`.

## Unit-plan candidates

- **A, one unit for all ten** (the TOOL-dTrueNorth-27 shape). Loses on: any fix needing a ruling or a
  write outside this folder stalls all ten; three do (2a, 6, 7's checker change).
- **B, one unit per fix class, disjoint write sets.** Holds once the prefix fixes in `pre-commit` and
  `check-spec-tokens.test.sh` join the shell unit and the records unit only adds registry rows.
  **Adopted.**
- **C, one unit per leg.** Rejected: eight files are shared across legs.

## The plan adopted

- **TOOL-dGroundRules-84, shell sources and kit-path spellings:** legs 3, 4, 5, 7 and 9, the
  `check-install-prefix.sh` split with a new arm, and the `spawn-idiom-sites.txt` rows.
- **TOOL-dGroundRules-85, fork budget:** leg 6, in `check-memory-hygiene.sh` and
  `manifest-check.sh`; it loses if either stays over its ceiling.
- **TOOL-dGroundRules-86, records and docs:** legs 1, 2, 8 and 10, built last so the manifest
  re-audit reads the tree -84 and -85 leave.
