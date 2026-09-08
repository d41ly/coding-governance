# Brief — TOOL-aReapedSpinner-5, the session seam

**Serves:** journal TOOL-aReapedSpinner-5

What this pass was handed: the unit's spec at rev-4, D23 (the hook destination belongs to the unit
that ships the file), and `tools/hooks/scratch-guard.js` as the sibling hook to copy in shape.

What it builds: `tools/process-monitor/procmon-hook.js`, its two `.claude/settings.json` entries,
its `[[files]]` row, and eight arms.

The four things that are not obvious:

- **Three states, kept apart.** Clean is SILENT, flagged is a short list, broken is ONE named line.
  Collapsing the first and third is how "nothing to report" becomes indistinguishable from "the
  probe could not run".
- **The stamp is written AFTER the work.** Stamped first, a crashing hook throttles itself out of
  ever running again and the silence reads as a clean tree.
- **The stamp lives in the git COMMON dir**, for the reason `.unattended.conf` records about its
  lander marker: in a linked worktree `.git` is a FILE.
- **It fails OPEN, always.** A monitoring fault may not block a tool call, so every path exits 0.
