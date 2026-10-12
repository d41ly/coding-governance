# TOOL-aBriskPreflight-19 — acceptance ledger

**Serves:** journal TOOL-aBriskPreflight-19

No merge bar and no self-test suite ran in this pass. Every criterion was observed directly on node
`a`, 2026-10-12, at spec rev-1, by the leg's own checker run from the worktree before the commit.
Each leg was first observed RED on the unchanged tree, which is the staged break: the three
spellings, 1067 offenders and the unarmed `post-merge.sh` site. The legs of spec §7 are owed to the
close.

**Evidences:** TOOL-aBriskPreflight-19
- AC1 — `bash check-install-prefix.sh` — exited 0 printing `install-prefix: clean`, 0 kit-path
  spellings on 0 lines. Before the change it exited 1 naming the three sites. The two pre-push
  suite sites now spell the manifest through `KIT_REL`. The unattended suite's foreign bar is
  resolved through the suite's own `resolve_kit_dir`, as it resolves every other sibling kit. A
  slice of the suite's resolver printed the resolved answer text byte-identical to the old literal.
- AC2 — `lexicon.py --check` — exited 0 with `offenders=1063`, against 1067 before.
  `adopt-lexicon.sh --check` exited 0. The four renames are `decide_on` to `run_push_selftests`,
  `pfx_fixture` to `build_pfx_fixture`, `pfx_stamp` to `write_pfx_stamp`, and `pfx_decide` to
  `run_pfx_push`. `bash -n` passed on both suites, and a `grep -w` of the four old names over
  `.githooks` and `tools` printed nothing.
- AC3 — `check-arms.py --check` — exited 0, printing a `waived` line for the `post-merge.sh` site
  with its reason. No arm can assert the site's whole text where the checker reads arms: it reads
  only the `post-merge.test.sh` sibling suite, which does not exist. The arm that drives it is in
  `run-gates.evidence.test.sh`, so S3's pin branch was taken.
