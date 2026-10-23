**Serves:** research PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49

# Promoted-fix pass — the spec writer's return

All three jobs are done on the eleven promoted specs, 39 to 49. Spec 49 is now **48970 B**, under the 49152 B ceiling. Edits were in place with no rev bump. Nothing was staged or committed, no index was rendered, and no spec numbered 1 to 37 or deviation record was touched. I can't run check-spec-tokens, so the path result rests on a probe that copies its §6 rule (below).

**1. Review citation:** in all eleven specs, every citation of `2026-10-23-review-PLAY-dOrderedCharter-spec-round1.md` now points at `memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`. That is one line per spec, and that record exists.

**2. The 36 `[path]` hits:** each file the build run will create is now cited in §6 by its basename. Where a basename alone would change what a `git grep`, `git log` or `git check-attr` command matches, the command runs from the file's directory with `git -C <dir>` instead. Full paths stay in §2, §4 and Files touched. The less obvious fixes:
- **Spec 41 AC1:** the `tomllib` one-liner now takes the tracked `tools/govkit/entries/playbook.kit.toml` as a separate argument (`sys.argv[1]`) instead of embedding it in the code.
- **Spec 41 AC4:** the grep pathspec is now `help/` instead of `help/charter.md`, and the criterion names `render_playbook.py` and the page `charter.md`.
- **Spec 43 AC1:** says "S1's card import line" instead of repeating `@.claude/orientation-card.md`, which S1 already spells.
- **Spec 47 AC3:** the fixture's record moves to `notes.md` under the fixture's `tools` directory.
- **Spec 49:**
  - AC17 runs `git ls-files` over "S24's six paths" instead of listing them.
  - AC32 uses `git ls-files -- '*edge_checks.py'`.
  - AC48 names unit 22's `chain.toml`.
  - AC24, AC29, AC46, AC57 and AC59 use the `git -C <dir>` form.

**3. Spec 49 trim (53135 → 48970 B), prose only:**
- **§1:** the 64-row table became a compact list of report items and their ids (M1 to M45, L1 to L19), plus the rule that S1 to S73 take the ids in order. M<n>'s criterion is AC<n> and L<n>'s is AC<45+n>.
- **§4 Evidence** now covers only the four citations §2 doesn't already make.
- **§3 Edges:** the bullets keep each verb and target and name the S items in brackets instead of "which … correct".
- **Elsewhere:** shorter §1 opening, §4 Order, Rollout and Alternatives, §5 risks, §10, and S3, S5, S11, S13, S27, S31, S35 and S40.

**Checks I ran:**
- **Nothing lost in the trim:** a script confirmed S1 to S73, AC1 to AC64 and F1 to F9 are all present. It also confirmed the item-to-id list matches the original staged table exactly, and that every scope item's "Observed by" criterion matches what the table gave it.
- **No path hits left:** a re-implementation of the tool's §6 path rule over specs 39 to 49 finds no untracked path-shaped token and no `spec-round1` citation.
- **Edges still pass:** hygiene check 12 (`--only 12`) exits 0 with no line naming specs 39 to 49.

Files changed, all in `C:\projects\coding-governance\.claude\worktrees\unattended-dorderedcharter-10a315\memory\builds\dOrderedCharter\spec\`:
- 2026-10-24-spec-PLAY-dOrderedCharter-39.md (citation only)
- 2026-10-24-spec-PLAY-dOrderedCharter-40.md
- 2026-10-24-spec-PLAY-dOrderedCharter-41.md
- 2026-10-24-spec-PLAY-dOrderedCharter-42.md
- 2026-10-24-spec-PLAY-dOrderedCharter-43.md
- 2026-10-24-spec-PLAY-dOrderedCharter-44.md
- 2026-10-24-spec-PLAY-dOrderedCharter-45.md
- 2026-10-24-spec-PLAY-dOrderedCharter-46.md
- 2026-10-24-spec-PLAY-dOrderedCharter-47.md
- 2026-10-24-spec-PLAY-dOrderedCharter-48.md
- 2026-10-24-spec-PLAY-dOrderedCharter-49.md (48970 B)
