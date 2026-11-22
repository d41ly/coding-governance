**Serves:** journal TOOL-dWitnessedBar-63

# TOOL-dWitnessedBar-63 — builder return 1 (run `wf_da412000-42b`), committed 6932f9604

## Why

TOOL-dWitnessedBar-63 is built from spec rev-4 and committed as one pass commit with a `Pass: TOOL-dWitnessedBar-63` trailer. The spec status is now CLOSED, dated 2026-11-21. The spec's claims about current code all held when probed, so there is no divergence. Two gov-canary arms in this unit's own write set were already red at the base and are repaired; deviation record 632 covers them.

## Summary

Built commit 6932f9604 on base a07a2203. No gate, suite or bar ran. I checked my changes with probes of the code over scratch fixtures, plus the greps the acceptance criteria spell. Every criterion is either observed or marked OWED in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-63-1-acceptance-ledger.md.

What changed:
- **Seed (all three legacy_ledger.py copies):** the no-HEAD path now writes `legacy_ledger: <population>: <reason>; nothing written` to stderr (S6). Only an exit 1 with nothing printed counts as an unborn HEAD (S8). The unborn line goes to stderr (S32).
- **Section 2o of resolve-python.test.sh:** new cases for no HEAD, exit 128, cross-drive, the unborn stream split and `--sha HEAD`.
- **lib-unattended.sh (S9, S22):** each generated row is read whole, `\` is folded to `/`, a colon anywhere is refused, and the `when` is checked before the generator.
- **Containment rule:** govkit selfcheck uses `derive_contained_rel` (S10); regen's `check_when` applies the same rule inline (S11).
- **No-TAB lines:** the runner's `read_record_keys` reads whole lines and treats a no-TAB line as no key (S17, S19); the hook's `read_bar_file` does the same.
- **Signer temps (S20):** `remove_stale_signer_temps` and `PEER_SIGNERS_GRACE_S` (86400 s) sweep `gov-signers-` files left by killed reads. There is also a new `key-no-tab` plant. (DERIVED from the builder's probe)
- **Gov canary scrub arm (S3):** it prints the four list counts and PM_SCRUB's first and last names, and gains a copy with the assignment taken out.
- **New selftest arms:** AC5 (five Windows path forms), AC13 (the lone-CR conf) and AC14 (a row with no generator).
- **Docs and comments:** S25, S28, S29 and S31.
- **Floors:** gov canary 38→41, evidence suite 312→314.
- **Records and housekeeping:** shell-role widen 6, which also covers 14 lines units 51 and 56 had already added to run-gates.sh past its row. Kickoff manifest re-stamped. Codebase map and build index regenerated. Four extra paths declared through `--dispatch`. (DERIVED from the builder's probe)

Checks that ran, and the gate each stands in for:
- **python resolver (section 2o):** the seed routes through `run_seed_cli` over a commitless, then committed, fixture under %TEMP%/u63ll. AC4, AC6 (including a real Z: drive on this host) and AC23 held.
- **govkit selftest:** `resolve_generated_indexes` over scratch trees under %TEMP%/u63lu (AC5 forms, AC14, and the AC14 split probe); `regen.check_when` and the `_check_exists_refused` expression over each form; the step's `derive_reads` and `up` over the lone-CR conf (AC13).
- **run-gates evidence, pre-push self-test and run-gates gov canary:** `read_record_keys`, `read_bar_file`, `read_green_file` and `check_bar_scrub_parity`, each cut out with awk and run alone over scratch records and staged copies (AC1, AC2, AC11, AC16).
- **The verdict-backends plant loop in run-gates gov canary:** `verdict_backends.py --fixture --plant key-no-tab`, `no-pair` and `peer-no-ssh-keygen` all held (AC11, AC12).
- Also run: `bash -n` and `ast.parse` over every touched file, and the naming lexicon on both new function names.

Owed to the close:
- **Suites:** `run-gates gov canary`, `govkit selftest`, `python resolver (behaviour + inline parity + idiom ban)`, `run-gates evidence`, `pre-push self-test`, plus every §7 leg.
- **The RED-first observation for each `New arm:` line:**
  - the gov arm reds on a one-line PM_SCRUB cut;
  - the selftest arm reds without the backslash fold and with a text-mode conf read;
  - section 2o reds when exit 128 stamps the null SHA and when the unborn line goes to stdout;
  - verdict_backends reds when a no-TAB key is taken as its value and when the sweep is deleted;
  - the evidence arm reds when the `IFS=$'\t'` split is restored;
  - the hook suite reds when a no-TAB key is taken as its value.
- **Close-only criteria:** AC3, AC7, AC8's `cmp`, AC9, AC18's unit 62 AC7 ledger line, and AC24.

Bug-class checklist: `gotchas.py --for-diff HEAD~1..HEAD` exited 0. I checked the classes it selected against the commit: line claims are tested per line, no new local collides with an existing one, the assertions cannot pass over an empty fixture, and the Windows CR and drive cases are handled.

Decisions and residuals:
- **Deviation 632:** at the base, the gov arm's GATE_SELECTION copy was always empty because the sed script and file name were fused into one word. Separately, the plant loop expected `peer-no-ssh-keygen` to exit 1, but since unit 62 the plant returns 0. Both are fixed: the sed takes its file as a separate word, and the loop now expects 0.
- **AC13 arm:** it stubs only the containment walk for its `derive_reads` call, because Windows refuses a filename containing a CR.
- **`exists:.` disagreement:** regen and govkit now refuse a bare `exists:.`, but the shell reader still keeps it. S9 does not name it, and no fixture plants it.
- **Untested branch:** the `--home` no-HEAD stderr line has no suite arm.
- **Commit trailer:** it uses `Claude Opus 5`, following AGENTS.md.
