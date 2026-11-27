# TOOL-aPrunedIndex-4 — acceptance ledger

**Serves:** journal TOOL-aPrunedIndex-4
**Caused-by:** TOOL-aPrunedIndex-4

No merge bar, no self-test suite and no gate leg ran in this pass, and nothing here opened either live index
file. Every reading is node a's, 2026-11-26, from base `f777b966e`, by the `gc-predates` plant in its own
scratch repository and by one read-only probe of `read_live_versions` over this repository's worktrees. The
new arm's five staged reds, the legs of section 7, and AC8 are owed at the close. The staged reds were observed afterwards at `57c8f95e6`, as the seen-red lines below record.

**Evidences:** TOOL-aPrunedIndex-4
- AC1 — `python tools/playbook/gov_tag.py --fixture --plant gc-predates` — exit 0; step 4 printed one `tag-index — skipped:` line naming `wt3`, left 0 rows of its version and the live dump unchanged; 46 s. (PINNED, 2026-11-26)
- AC2 — `gc-predates` step 2 — refused naming `wt4`, its registry unreadable on disk, with 10 dead rows of 10 unmoved. (PINNED, 2026-11-26)
- AC3 — `gc-predates` step 3 — exit 0, no skipped line, 0 dead rows, and 10 rows of `wt3`'s version of 10 kept. (PINNED, 2026-11-26)
- AC4 — `gc-predates` step 5 — refused with `no worktree holds tools/nokit/namespaces.toml`, 12 rows of `root`'s version unmoved. (PINNED, 2026-11-26)
- AC5 — a `python -c` probe calling `read_live_versions(<this repo>, "tools/playbook")` — 104 worktrees, four skipped (`blissful-khayyam-69a7df`, `deterministic-attended-workflows-943570`, `deterministic-reuse-workflows-f70c33`, `full-repo-bar-tests-2591de`), equal to the list a separate disk and `git ls-tree` walk of the porcelain listing derives; none refused; 83 s, no index opened. (PINNED, 2026-11-26)
- AC6 — `grep -n "predates" tools/playbook/README.md help/tags.md tools/playbook/gov_tag.py` — each file prints the sentence on what `--gc` skips.
- AC7 — `gc-predates` step 6 — 3 of 3 conf breaks (deleted, a directory, bytes that do not decode) refused naming `wt4`, the 16 rows of its conf key unmoved after each and after the restored collection. (PINNED, 2026-11-26)
- AC8 — `python tools/playbook/tag_bundle.py --selftest`, run alone by the main loop at `d5288a92d` — exit 0, `PASS — the tag plants, 14 rows`, 106 s wall, under the leg's 300 s `ceiling`; the budget row in `tools/run-gates/selftest-budgets.txt` reads 159, and `derive-ceilings.py --write --observed` wrote the evidence row (PINNED, 2026-11-26)
- AC9 — a probe of `tag_bundle.SELFTEST_ROWS` printed `gc-predates|0|refused on wt4, wt3 read and then skipped by name, refused on none, refused on a conf`.
- seen-red — `tags bundle selftest` — red `57c8f95e6` — green `57c8f95e6` — `gc-predates`: today's code with no skip, the skip on absence from disk alone, on absence from HEAD alone, no refusal on an empty live set, and no refusal on an absent or non-file conf (step 6, 1 of 3 refused, 0 of 16 rows left) each exit 1 (PINNED, 2026-11-26)
