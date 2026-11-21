# TOOL-dWitnessedBar-67 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-67

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21 (GNU bash 5.3.9 `x86_64-pc-cygwin`, git 2.54.0.windows.1, Python 3.15.2), through scratch
probes that `eval` each new arm's own lines, cut from its suite by the arm's header: the gov suite from the
clean plant's record arm to the bar-scrub arm's closing `rm -rf`, with `$KITDIR` set to `tools/run-gates`;
the evidence suite from the unit-63 AC16 header to the closing `echo`; the resolver suite from the
corrupt-HEAD header to the no-HEAD header, its fixtures under `%TEMP%/r67` and an outer
`GIT_CONFIG_GLOBAL` setting `init.defaultBranch=main` and `init.defaultRefFormat=reftable`. Every staged
break below ran over a scratch copy, `diff` counting the changed lines named. Each suite passed `bash -n`.
The shell-role seed measures the resolver suite at 1371 past 1314, the gov suite at 706 past 636 and the
evidence suite at 2452 past 2447, widened under `2026-11-21-build-TOOL-dWitnessedBar-67-widen-11`. The §7
legs and the three `New arm:` lines' RED-first observations are the main loop's at the close.
(DERIVED from the builder's probes)

**Evidences:** TOOL-dWitnessedBar-67
- AC1 — `rec_verdict` — `grep -n 'rec_verdict' .githooks/pre-push` printed nothing, and `grep -nE 'rec_[a-z_]+.*GREEN'` over `tools/run-gates/run-gates.gov.test.sh` printed nothing.
- AC2 — `rec_fp` — the arm's sourced `read_green_file` over its record set `rec_fp` to forty `c`, the arm's assertion held and the cut counted 19 assertions with `fail` at 0. Against a scratch hook with `    _rg_v=${_rg_v%$'\r'}` deleted (`diff` counted 1 line), the arm printed `set rec_fp to 'cccccccccccccccccccccccccccccccccccccccc\r'` and set `fail` to 1; this node's read loop hands the CR on, so the red stood on Windows.
- AC3 — `gov-signers-d` — the sweep probe printed `case unlink held`, `case stat held` and `case glob held`: unlink returned `[]` with one stderr line naming `gov-signers-b`; stat returned `['gov-signers-b']` with stderr empty; glob returned `[]` with one line naming the directory; no unlink reached `gov-signers-d`, which stayed. Without the `OSError` catch around the unlink (`diff` 4 lines) the unlink case printed `raised PermissionError`; with `p.exists()` for the regular-file test (`diff` 2 lines) the unlink and stat cases printed `gov-signers-d` among the unlinked entries. `grep -n 'gov-signers-d'` names the arm.
- AC4 — `GIT_DIR` — over `post-merge.sh` and the `pm-comment` copy, the assignment's five lines, bash's evaluated words equalled the reader's, first `GIT_DIR`, last `GATE_REUSE_DAY` as bash read it. With the reader's `exit` dropped (`diff` 1 line), both compares failed naming the words read past bash's, opening `GATE_REUSE_PUSH GATE_REUSE_DIGEST_ENV GATE_REUSE_SAMPLE GATE_REUSE_DAY"`.
- AC5 — `--ref-format=files` — under the hostile outer config, each of the five corrupt-HEAD fixtures and the child fixture read `files` from `git rev-parse --show-ref-format` and HEAD `ref: refs/heads/master`, the four broken ones still read no HEAD, and `GIT_CONFIG_GLOBAL` read unset after the block. `grep -n -- '--ref-format=files' tools/lib/resolve-python.test.sh` names the fixture builders. The red with `--ref-format=files` dropped where the hostile config reaches git is unit 71's.
- AC6 — `timeout=60` — the recorder printed `git calls 5 timeouts ['60']` for the seed with `--sha` in the child fixture and for the seed in the `missing` fixture. With `timeout=60` dropped (`diff` 1 line) both printed `timeouts ['None']` and the arm failed.
- AC7 — `65 AC7` — `seed --all` over p and x1 in the `garbage` fixture exited 1 with two lines, `unarmed p no HEAD: fatal: No such ref: HEAD` and the same for x1, one reason, and no home. `grep -n '65 AC7'` names unit 65's two stand-ins, which replace only the call holding `--verify`.
- AC8 — `--sha` — in the child fixture, two commits and branches `deadbeef` and `cafe1234` at HEAD~1, each `seed --sha` exited 2 naming `--sha`, stderr `resolves through a ref to <HEAD~1's sha>, a commit it does not abbreviate`, and wrote no home. HEAD~1's first ten hex characters in upper case still armed p at its full lowercase sha. With the prefix test removed (`diff` 1 line) both exited 0.
- AC9 — `head<TAB>z` — the cut `read_record_keys` read a record ending `head<TAB>z` with no LF as `head=[z]`, and the arm printed `ok`. With the `|| [ -n "$_rk_l" ]` guard dropped from a scratch runner (`diff` 1 line), it read `[unset]` and the arm printed `FAIL`.
- AC10 — `fatal: No such ref: HEAD` — in the loop fixture `git symbolic-ref -q HEAD` exited 128 and the seed printed `unarmed p no HEAD: fatal: No such ref: HEAD`. `grep -n 'refs/heads/other'` names the loop line writing both files.
- AC11 — `armed p 2` — the one-file `chain` fixture's seed exited 0 printing `armed p 2`, both rows carry forty `0`, and no `refs/heads/other` was created.
- AC12 — `grep -H` — OWED to the close: unit 65's AC4 ledger line, which reads `sed -n 3p` today, is the main loop's to rewrite naming this unit's S14 and the per-file `grep -H '^\*\*Status:\*\*'` reading.
- AC13 — `gen_build_index` — `grep -n 'gen_build_index' tools/govkit/govkit.py` prints one line, in the comment beside `_check_exists_refused`, which names `1:x` on the same line.
- AC14 — `order 36` — `grep -H '^\*\*Status:\*\*'` read unit 64 at `order 36` and unit 65 at `order 37`, and the build README's build-order rows 36 and 37 each name one unit.
- AC15 — `PM_SCRUB` — the `grep -cE` over the unmodified `post-merge.sh` printed 1. Over a copy with `PM_SCRUB="${PM_SCRUB/GATE_SELECTION/}"` after the assignment (`diff` 1 line), the arm printed `PM_SCRUB has 2 assignment statements` and set `fail` to 1.
- AC16 — `git for-each-ref listed` — after `git branch a/b` and `git symbolic-ref HEAD refs/heads/a` in the child fixture, the seed printed `unarmed p no HEAD: git for-each-ref listed <sha> commit<TAB>refs/heads/a/b`. With the listed reason replaced by the `exited` one (`diff` 1 line), it printed `git for-each-ref exited 0` and the arm failed.
- AC17 — `?:\*` — `grep -c '?:\*' tools/unattended/lib-unattended.sh` printed 0, and `grep -n '":" in rel'` named `tools/govkit/upgrade_steps.py#derive_contained_rel` and `tools/run-gates/regen.py#check_when`.
