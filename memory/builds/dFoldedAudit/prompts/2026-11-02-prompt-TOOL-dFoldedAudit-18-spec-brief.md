# Spec brief — TOOL-dFoldedAudit-18: the help page for the spec-audit switches and the chain verbs

**Serves:** research TOOL-dFoldedAudit-18

## The brief

### Goal
Write TOOL-dFoldedAudit-18's spec at Tier-1. The docs leg, which reached this branch through the landing merge, must anchor five members this build added and no page under `help/` documents. Read `build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md` first; its tags bind. Header `order 180`, status OPEN. Commit nothing.

### Items
1. The close's `docs` leg printed `UNDOCUMENTED` for five members:
   - `policy:review.spec-audit.chain-ceiling` (default 4, a round count, min 1)
   - `policy:review.spec-audit.chain-stop` (default `own-work`, values `own-work` and `clean-only`)
   - `policy:review.spec-audit.disposal` (default `by-nature`, values `by-nature` and `promote-all`)
   - `verb:unattended.sh:--chain-verdict`
   - `verb:unattended.sh:--record-round` (flags `--audited`, `--blockers=`, `--finding=`, `--highs=`, `--sibling=`, `--subject=`)

   `memory/project/docs-undocumented.txt` only shrinks, so these must be documented, not listed.
2. Write one new page, `help/spec-audit.md`, in the shape `help/docs-leg.md` and `help/policy.md` use: what it is, how to use it, and what each value does. Take every fact from this build's M4 text in `memory/guides/BUILD-METHOD.md`, the policy catalogue rows, and the verbs' entries in `memory/guides/UNATTENDED-VERBS.md`. Each member gets its anchor, `<!-- usage: <id> <fingerprint> -->`, once and only on this page. The fingerprint is the one the leg prints. A first anchor carrying a placeholder fingerprint reads STALE and prints the right one.
3. Link the page from `help/README.md` if that index lists the pages.
4. Commits follow the charter's trailer, `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. The worktree sits on top of the prepared landing merge `30396a42`, so the pass commit is one more single-parent commit there. A second merge is refused at the landing.

### Acceptance
- `python tools/govkit/docs_leg.py` exits 0 and prints no `UNDOCUMENTED`, `STALE`, `COMMAND`, `LINK` or `TWICE` line.
- `python tools/govkit/docs_leg.py --undocumented` names none of the five ids.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass. §7 names the `docs` leg, by its exact name in `tools/gate-legs.json`.

### Non-goals
No change to any member's behaviour, no row added to the undocumented list, and no write outside `help/` beyond the spec.
