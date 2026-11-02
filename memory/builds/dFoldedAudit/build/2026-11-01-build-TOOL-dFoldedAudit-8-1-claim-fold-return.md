# dFoldedAudit — the check 13 fold's return

**Serves:** journal TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-8

TOOL-dFoldedAudit-8 is authored. Both fix-brief items are applied, and the working-tree run of `check-memory-hygiene.sh --only 13` now prints no check 13 line at all. Before the edit it named three ids against dFoldedAudit.

**Changes**
- **TOOL-dFoldedAudit-8, rev-1 to rev-2:** the §4 headings now read `### The revision of `TOOL-dDeclaredLoop-32``, `...-20` and `TOOL-dFairHearing-17`. The revision log has a rev-2 line. A grep of the build folder found nothing citing these headings by name or anchor, so no cross-reference needed changing.
- **TOOL-dFoldedAudit-1, rev-3 to rev-4:** the §4 bytes paragraph now reads "The unbuilt S9 of TOOL-dDeclaredLoop-20 will need about 60 more of those bytes...". The revision log has a rev-4 line, and the byte figures do not move.
- Both specs are still OPEN, so no `spec-revised` record is owed.

**Finding on item 2:** the old line 158 in unit 1 was never a claim. Running it through `resolve_anchor` returned `None`, because `anchor_at` only matches `##`-style headings, bullets and table rows. Check 13's `TOOL-dDeclaredLoop-20` hit came from unit 8's heading alone, as unit 1's rev-4 line records. I reworded it anyway, as the brief asked.

**Verification**
- **Anchor predicate:** the old heading text returned the id, and all three new headings returned `None`.
- **Revision logging:** a direct grep confirms each header rev has its revision-log line, rev-4 in unit 1 and rev-2 in unit 8.
- **Check 12:** the `--only 12` run had not finished when I returned, and it is still running in the background. Its output is in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-build-m4-spec-audit-694e7b\728ed75b-dc6d-443b-b1e2-72cabd3e91a1\tasks\blevgerfm.output`.
- **Your bar:** `tools/check-spec-tokens.py` and check 13 after staging are yours to run. Check 13 reads the tracked files from the working tree, so staging should not change this result.

Nothing is committed, and no index was regenerated.

Files:
- `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-8.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-1.md`
