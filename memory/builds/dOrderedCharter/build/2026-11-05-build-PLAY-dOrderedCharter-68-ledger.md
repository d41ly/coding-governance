# PLAY-dOrderedCharter-68 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-68

Each line is a probe this pass ran at rev-1 of the spec, from the worktree root with the pass applied. The
plants ran through `gov_tag.py --fixture --plant` by hand and never through `adopt-playbook.sh` or any
`--selftest`, which a role does not run. AC5, the suite arm and its RED-first observation, the legs section 7
names and the merge bar are the main loop's at the close. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-68
- AC1 — `[(1, 'intro')] [2]` — the spec's `fence_probe` printed it, then `[(1, 'a'), (2, 'b'), (6, 'c')]`; at the parent commit its first line raised `TypeError`, the function taking one argument.
- AC2 — `True` — the spec's `cached_probe` printed it; at the parent commit it printed `False`.
- AC3 — `· unclosed fence ·` — `gov_tag.py --fixture --plant unclosed-fence` with the two `--set` flags exited 1 printing `tags: memory/guides/ALPHA.md:11 · unclosed fence · it opens here and never closes, so every later line goes unread` and no `unresolved`.
- AC4 — `tags: unclosed fence, frozen record, printed` — `--plant unclosed-record` with the same flags exited 0 printing `tags: unclosed fence, frozen record, printed · memory/builds/x/README.md:2` and `tags: green · 0 red`.
- AC5 — owed — `gov_tag.py check --base HEAD` over the whole tree is refused to a role agent by its own permission line, so the main loop observes it at the close. A probe of the shared walker over the frozen record printed its sentinel at `717`.
- AC6 — `3` and `1` — `grep -c "unclosed fence" help/tags.md` printed `3`; `grep -c "tree_lib.unfenced_lines"` over the bug-class record printed `1`.
