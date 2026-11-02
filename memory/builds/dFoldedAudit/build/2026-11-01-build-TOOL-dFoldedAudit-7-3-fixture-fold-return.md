# dFoldedAudit — unit 7's fixture fold return

**Serves:** journal TOOL-dFoldedAudit-7

TOOL-dFoldedAudit-7 is revised to rev-4. The status cell stays INPROGRESS, §9 has the rev-4 line, nothing is committed and no other file changed. One part of brief item 3 does not match the precedent, so check that before you dispatch.

**Brief item 3 misdescribes the precedent:**
- `d7e8a027a` touches only `.governance/policy.json` and `RUN.md`; it does have its own dispatch row (anchor `f6674a6a`) and its own `Pass:` trailer.
- The CLOSED flip and the README re-render sit in the first commit, `f6674a6a2`.
- I kept the brief's placement, because it holds on its own merits. The ledger gate asks a line for every criterion of a closed spec (`memory/HYGIENE.md:713`), and AC9 has nothing to observe until the mirror is written.
- §4 credits `d7e8a027a` only with the row and trailer, records the flip's place as this unit's own choice, and lists the first-commit flip under Alternatives rejected.
- If you meant to follow the precedent exactly, that §4 table and AC9's new wording are what change. §8 stays `none`, because the brief made this choice.

**Items:**
1. **Fixture K:** it now holds `tools/policy/budgets.py`. A scratch fixture confirmed the traceback without it. With it, `policy.py get` gives AC2's three values and AC3's `policy: refused` line, with no `caps.toml`. That probed `get` only, because the reader doesn't exist yet.
2. **New criterion:** AC10 and its `New arm:` line cover the closed-set and bad-argument rows, and S2 now names AC10. The closed-set row is only reachable through a widened catalogue, and `get` does answer `fold-all` with exit 0 there. The catalogue half of the arm is counted either way, on the `_da_home` shape.
3. **Two-commit shape:** it is now a table in §4's Rollout, and S5 no longer says "a commit of its own".

**Beyond the brief's wording, both needed by item 3:**
- AC9 now reads after `mirror --write` rather than after the second commit, because that commit carries the ledger answering it. `mirror --check` compares the tree file with the render at HEAD (`tools/policy/policy.py:1404`, `:1411-1416`), so the second commit changes neither side.
- §4 says "that same commit" in the harness prompt (`tools/workflows/unattended-unit.js:314`) means the second commit for this unit. A builder following that prompt alone would flip in the first commit.

**Checks:**
- **Memory hygiene:** `tools/memory-tree/check-memory-hygiene.sh` exited 1. Check 9 is the README roster cell still reading `rev-3`, which clears when you re-render.
- **Check 13:** four hits on ids claimed by two build folders. For `TOOL-dDeclaredLoop-20`, the HEAD files holding the id are units 1 and 8 and a build record. None of the four ids is in this spec, but I didn't trace the other three to their files. Check 13 may also hold the exit at 1.
- **Spec tokens:** `tools/check-spec-tokens.py` was not run; it's yours after this pass.

**Could not verify:** I found no meaning for the builder's "the mirror commit reads as `O`", so the spec doesn't rely on it.

**Scratch fixtures:** a safety check refused an `rm -rf` in my first probe, so I built fresh directories instead. They remain under the session scratchpad at `fx`, and nothing was deleted.

Files:
- C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-7.md
- C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-build-m4-spec-audit-694e7b\728ed75b-dc6d-443b-b1e2-72cabd3e91a1\scratchpad\fx
