**Serves:** research TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91

# The round-6 promoted-fix pass's return — dLinkedLibrary

The spec writer's final return, extracted from its transcript by script, never retyped.

I fixed all six findings by editing the drafts in place, with no rev bump and no §9 line. After the edits, `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25` exits 0 and names none of the specs for units 87 to 91. I did not run `check-spec-tokens.py`, because my role admits only the hygiene gate and the lexicon, so finding 6 is not yet confirmed by that checker. I checked it against the checker's `BAR` regex instead (`tools/check-spec-tokens.py:390-395`), and the §6 of `TOOL-dLinkedLibrary-91` no longer holds a backticked token it matches.

For findings 1 to 4, none of the four items actually retires anything, so I took the brief's "reword" route rather than writing `**Readers:**` clauses. Check 25 fires on a retirement word anywhere in an item next to a code-shaped backticked token (`test_retirement`, `check-memory-hygiene.sh:1979-1998`). Here those words described scratch copies or decoding, not removals.

**`2026-10-27-spec-TOOL-dLinkedLibrary-87.md`**
- **Finding 1 (S3):** "with 82's template branch removed from a scratch copy" now reads "over a scratch copy that lacks 82's template branch".
- **Finding 2 (S4):** "one whose scalar branch is dropped" now reads "one lacking the scalar branch". "one with both 81 S3's fallback and 82's branch dropped" now reads "one lacking both 81 S3's fallback and 82's branch".

**`2026-10-27-spec-TOOL-dLinkedLibrary-90.md`**
- **Finding 3 (S1):** "`utf-8-sig`, which drops one leading U+FEFF" now reads "which reads past one leading U+FEFF". The title and §1 still say "drops", but check 25 reads only §2.

**`2026-10-27-spec-TOOL-dLinkedLibrary-91.md`**
- **Finding 4 (S22):** "a `"$VAR"` concatenated before it replaced by that variable's heredoc" now reads "…before it read as that variable's heredoc in the same file".
- **Finding 5 (AC13):** the criterion now names its witness: "When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, no tree's output holds a census row named `default`, `variables`, `workflow`, `image`, `services`, `cache`, `before_script` or `after_script`, the eight blocks S13 lists." The "Red when" line is unchanged.
- **Finding 6 (§6):** AC23's "a scratch copy of `run-gates.sh`" now reads "a scratch copy of the gate runner, the file holding S22's first two hosts", and I reflowed the lines. AC20's `tools/run-gates/regen.py` does not match the `BAR` regex and was not among the findings, so it stays.

Units 88 and 89 needed nothing. Nothing is committed, the index is not regenerated, and every spec is still under 49152 bytes (`TOOL-dLinkedLibrary-91` is at about 31.3 KB).

Files changed:
- C:\projects\coding-governance\.claude\worktrees\unattended-dlinkedlibrary-4f9fd9\memory\builds\dLinkedLibrary\spec\2026-10-27-spec-TOOL-dLinkedLibrary-87.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dlinkedlibrary-4f9fd9\memory\builds\dLinkedLibrary\spec\2026-10-27-spec-TOOL-dLinkedLibrary-90.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dlinkedlibrary-4f9fd9\memory\builds\dLinkedLibrary\spec\2026-10-27-spec-TOOL-dLinkedLibrary-91.md
