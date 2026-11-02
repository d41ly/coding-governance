# dFoldedAudit — unit 17's spec-writer return

**Serves:** journal TOOL-dFoldedAudit-17

Run direct/ab76a3b82a0f1dc0a, verbatim from its task notification.

I wrote the Tier-1 spec for TOOL-dFoldedAudit-17: status OPEN, rev-1, `order 170`, base `8a5328a9`. It is the only file written, and nothing is committed or regenerated.

**Units**
- `TOOL-dFoldedAudit-17` — authored: `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-02-spec-TOOL-dFoldedAudit-17.md`

**Checked against the tree.** A trial merge of `951f44e4` with `8a5328a9` conflicts on exactly the brief's eight paths. Another 22 paths that both sides changed merge cleanly. I simulated the six hand resolutions in scratch: both Python files compile, and the pin probe prints `37 39 True`. Counted with the drift signal's own parser, each side arms 37 cutoff keys and the merged tree arms 38. The pin therefore reads `ok (pin 39, drain it)` until the close arms `SPEC_FOLD_CUTOFF`.

**Where the spec goes past the brief**, each worked out from code or earlier merges:
1. **The clone's `origin`.** A clone of the local repo calls that repo `origin`, so its `origin/main` would be local `main` (`2a6f3975`), not GitHub's tip. The clone must point `origin` at the run repo's GitHub URL before `git fetch origin`. It also sets `core.hooksPath .githooks`, since a fresh clone otherwise runs no hooks.
2. **Two re-stamps of `last-audit`, not one.** The manifest checker's pre-commit check refuses a merge commit whose stamp is unchanged. Its full check cannot see a stamp change inside a merge commit. So the merge commit stamps the branch tip, and a follow-up commit stamps the merge commit's sha. The dSafePassage merge `37b3bf32` and its follow-up `f25d719e` did exactly this.
3. **The policy mirror must wait for the follow-up commit.** The policy guard admits `.governance/policy.json` in a merge only as one parent's blob. The mirror also records the catalogue's blob, and the merged catalogue is a new one. So the merge commit takes `--ours`, and the follow-up runs `policy.py mirror --write`.
4. **`SPEC_SUPERSEDE_CUTOFF` really stays unchanged.** The check that dates a cutoff searches history with `git log -S`, which never lists merge commits. On `origin/main` it lists only `56aef62a` for `SPEC_AC_ORDER_CUTOFF`, even though landing merges carried that line.
5. **The tip may have moved by the time the builder fetches.** The spec gives the rule rather than fixed numbers: the floor is main's floor plus 12, and the pin is main's pin plus 2. The brief's stop condition still applies to a conflict on any other path.

**Still to run.** I ran the memory hygiene gate in a throwaway clone with the spec committed; no shape check names it. Check 9 is red only because the new spec changes `memory/LIVE.md` and this build's README, which you regenerate. Check 23 is red on unit 16's criteria having no journal record, unrelated to this spec. The naming lexicon exits 0. The main loop still needs to run `tools/check-spec-tokens.py` over the spec. Criteria AC8, AC9 and AC12 run the exact command of a gate leg. Each says that if scratch-guard refuses it to the builder, the main loop observes it at the close.

Open questions: none.
