**Serves:** research KICK-dKeptSession-57 KICK-dKeptSession-62

# The round-3 promoted-fix pass's return — dKeptSession

The writer's final return, extracted from its transcript by script, never retyped.

All three findings are fixed in place. `check-memory-hygiene.sh --only 2,12,25` exits 0 and reports no finding on any dKeptSession spec. The only dKeptSession lines it prints are the existing "READER NOT IN TREE covers it" notices for specs 1, 2 and 3, which are informational. I did not run `check-spec-tokens.py`, which you will re-run.

1. **Spec 57, `[path]`:** AC2 now reads "When `python policy.py mirror --check` runs in the policy kit at `<this pass>`, …", citing the file by basename. The full path `tools/policy/policy.py` is still in S2. §4 and Files touched did not contain the path before this change and I left them as they were.

2. **Spec 62, `[bar]`:** AC18 now reads "When the inline-parity arm runs over a scratch tree whose `mail-notice.js` copy of `readCard` is staged to differ by one byte, it reds naming `read_card_js`." It now describes a staged break and no longer names the suite, the same shape as AC20. The suite stays on its existing §7 line, `New arm: tools/lib/resolve-python.test.sh · covers AC18 AC20 · …`, so no new arm line was needed.

3. **Spec 62, hygiene check 25:** I reworded S27 rather than adding a `**Readers:**` clause, because S27 retires nothing. "with its docstring removed" meant the docstring is left out of the text the AC2 grep reads, not deleted from `extract.py`. The check fired on the word "removed" sitting next to `derive_context_window`. A Readers clause would have claimed a retirement that does not happen. S27 now reads "…from its `def` to the next top-level `def`, read with its docstring's lines left out of the grepped text, matches neither `expanduser` nor `\.claude`." AC25 still says "its docstring removed". It is in §6, which check 25 does not grade, and changing it was outside this brief.

Each spec's `**Derived:**` line, §3 edges, §8 marks and rev number are unchanged. Nothing was committed.

Files:
- C:\projects\coding-governance\.claude\worktrees\unattended-dkeptsession-dd0ede\memory\builds\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-57.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dkeptsession-dd0ede\memory\builds\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-62.md
