# KICK-dKeptSession-67 — acceptance ledger

**Serves:** journal KICK-dKeptSession-67

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria AC1 to AC4 were observed on win32 at the pass's base
`07acb816`. AC1 to AC3 ran over a scratch fixture repository built by a probe script in the session
scratchpad, the way the suite's fixture section builds it: the conf, the fixture kit's descriptor,
`render.sh` and `rev.sh` read as data from the suite's quoted heredoc bodies, `in-0.txt` in the base
and the base commit amended with `rev.sh`'s render, the run branch with its records commit `<C>`,
and each pass cut at `main` and reset to `<C>`. The tool's own CLI, `pass-tree.sh --merge`, ran
there. The unit adds no function: `python tools/lexicon/lexicon.py` exited 0 over the change.

Owed to the close: every leg the spec's section 7 names, the pass-tree suite whole, and the `New arm:`
line's RED-first observation, the `K67` block's two merges and `T4`'s symbolic-ref arm staged red
against `pass-tree.sh` at ce776cccc. AC5 is the main loop's act after this unit's pass merges.

**Evidences:** KICK-dKeptSession-67
- AC1 — pass 13 added `in-13.txt` in one commit and carried `rev.sh`'s re-render in a second. Its
  `--merge` exited 0 (DERIVED, that run) and printed one sha, equal to `git rev-parse HEAD`. Its
  stderr carried no REFUSING line: the count was 0 (DERIVED, that run), and its one line was the
  regeneration's summary. The merge's first parent was the pre-merge HEAD and its second pass 13's
  tip; `git show HEAD:fx-rev.txt` equalled pass 13's render captured before the merge; `rev.sh
  --check` from the fixture's top exited 0 (DERIVED, that run); `git symbolic-ref HEAD` printed
  `refs/heads/run`.
- AC2 — pass 14 added `in-14.txt` and carried the base's `fx-rev.txt`. Its `--merge`, after AC1's,
  exited 0 (DERIVED, that run) and printed one sha, equal to HEAD; the regeneration reported stage 2
  as written with `fx-rev.txt` moved. `git show HEAD:fx-rev.txt` differed from pass 14's bytes; the
  criterion's `grep -c` for `in-14.txt` at its blob in the merge printed 1 (DERIVED, that run), and
  `rev.sh --check` exited 0 (DERIVED, that run).
- AC3 — `FX_RENDER_FAIL=1` over pass 7, as `T4` runs it, exited 1 (DERIVED, that run) with `the
  regeneration failed` on stderr; HEAD was the pre-merge sha, `git symbolic-ref -q HEAD` printed
  `refs/heads/run`, `git status --porcelain` printed nothing, and `git rev-parse -q --verify
  MERGE_HEAD` exited 1 (DERIVED, that run).
- The fixture generator's refusal, probed directly in the same fixture: with an input staged that
  HEAD lacks, `rev.sh --check` and `rev.sh` each exited 2 (DERIVED, that probe) naming that input;
  with a tracked input edited in the work tree, `--check` exited 2 naming it; restored, `--check`
  exited 0 (DERIVED, that probe). This is the condition AC1's red case reads at ce776cccc.
- AC4 — in the unattended kit, `grep -c "over the merge as it will be committed" README.md` printed
  1 and `grep -c "provisional commit of the merge" pass-tree.sh` printed 1 (DERIVED, that run); the
  criterion's `grep -c "tools/"` over the three files counted 0 in each of `pass-tree.sh`,
  `README.md` and `pass-tree.test.sh` (PINNED by the spec at ce776cccc, DERIVED again that run).
- AC5 — not observed, as the spec states: the re-run of KICK-dKeptSession-16's `--merge` is the main
  loop's act once this unit's pass has merged.
