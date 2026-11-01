**Serves:** research KICK-dKeptSession-65

# The round-6 promoted-fix pass's return — dKeptSession

The writer's final return, extracted from its transcript by script, never retyped.

I fixed the one finding in place in `KICK-dKeptSession-65`. Nothing else changed and nothing is committed.

**The change:** `C:\projects\coding-governance\.claude\worktrees\unattended-dkeptsession-dd0ede\memory\builds\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-65.md`, in §6, AC5's first sentence (line 300).
- Before: the guards were `{prefix}/policy/` and `{prefix}/memory-tree/gen_build_index.py`.
- After: the guards are `{prefix}/policy/` and `tools/memory-tree/gen_build_index.py` in its `{prefix}` spelling.

I used the repository path rather than the basename because that is what the criterion means. The same AC prints the hit `policy fixtures <- tools/memory-tree/gen_build_index.py`, which is that path with the prefix filled in, and the file is tracked. The checker flagged the old token because it treats a token as a path when its last segment holds a dot (`tools/check-spec-tokens.py:1139`), and it does not fill in `{prefix}`. `{prefix}/policy/` on the same line ends in `/`, so the checker skips it (`:1137`).

The header, its rev-1, the `**Derived:**` line, the §3 edges and the §8 marks are all unchanged. Lines 59, 103 and 175 still say `{prefix}/memory-tree/gen_build_index.py`, but in §2 and §4 they describe what is in the manifest. The brief reported a hit only in §6, so I left them alone.

**Hygiene check:** `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` ran checks 2, 12 and 25 and exited 0. It printed nothing about unit 65. The dKeptSession lines it did print are check 25's "did not grade … READER NOT IN TREE covers it" notes on units 1, 2, 3 and 64; they are notes about what it skipped, not findings. I did not run `check-spec-tokens.py`; the main loop re-runs it.
