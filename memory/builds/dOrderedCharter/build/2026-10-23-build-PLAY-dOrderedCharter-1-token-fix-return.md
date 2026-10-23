**Serves:** research PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37

# Token-fix pass — the spec writer's return

I applied the token-fix brief to 36 of the 37 specs, editing them in place: nothing staged, nothing committed, no deviation record touched. Spec 5 had no hits and is unchanged. I could not run `check-spec-tokens.py` myself: scratch-guard blocks that leg for this role. So I can't report its exit code or the true hit count. That run is still owed in the main session, along with the carries arm, which my probe doesn't reproduce.

What stands in for it: a probe I wrote that copies the checker's path and hands-off logic. Before my edits it found the same 196 path and hands-off hits as the brief's list (188 path, 8 hands-off). After them it finds 0.

**What I changed**
- **Path hits (188):** in the Acceptance bullets only, each path the build will create is now cited by its basename (for example `python gov_tag.py ...`), the form earlier builds used. Full paths stay in §2, §4 and Files touched. A few needed rewording instead:
  - **Specs 19, 20, 28:** the `json.load(open('tools/gate-legs.json', ...))` commands now take the file as an argument (`sys.argv[1]` with `tools/gate-legs.json` after the script). They still run as written.
  - **Spec 19 AC10:** the `diff` now `cd`s into `tools/lib` and `tools/memory-tree` before the `sed`, because both files are named `coverage_join.py`.
  - **Spec 3:** AC3 now says "the same opener naming `.claude/agents/gov-builder.md` at `Level 5`", and AC6's planted file is now "`NEW.md` in its guides folder".
  - **Spec 4:** AC1 points at "the envelope's closer line (§4's form)".
  - **Spec 8:** AC5 says "the card's import line S4 spells" and "the new Gemini `settings.json`".
  - **Spec 14:** AC3 says "`outside.md` one directory above the memory directory".
  - **Spec 36:** AC1 says "the `fixed-by` entry §4 declares, the `parser=` source `row_kind.py#read_witness`".
- **Hands-off hits (8):** each token is now named in the sibling spec, in the line where that sibling reads it:
  - **Spec 8:** `LEVELS[1]`.
  - **Spec 1:** `resolve_practices`, added to its Non-goals line about packs.
  - **Spec 32:** `--manifest overlay`.
  - **Spec 33:** `Mark`, `Successor` and `Proof`, which also fixes it spelling the fields in lowercase.
  - **Spec 3:** `INSTRUCTION_PATHSPECS`, added to its Non-goals line about the one renderer.
  - **Spec 31:** `write_overlay_units`.
  - **Spec 34:** `read_overlay`.
- **Carries, clause 0046:** spec 16's first Non-goals bullet now names the moved names and their importers in backticks, as the brief asked. All 14 of the clause's tokens now appear in spec 16.
- **Carries, stale pin:** the brief's bullets didn't cover this hit, so this was my call. Deviation 341 changed clause 0064's text, and spec 34's own §8 F4 says its pin takes the new hash once the as-built view takes the record, which it now has. I re-pinned spec 34 to `cl-dClosedLoop-0064@42692e4c` and confirmed that hash by recomputing it from the record's new text.
- **Hygiene check 2 (spec 14):** the `the title-and-file link text` text is no longer link-shaped. The check flags it even inside backticks.
- **Hygiene check 25 (spec 1, S6):** added a **Readers:** clause. By name: `render_playbook.py`, `playbook.kit.toml`, `WIRE-INTO-PROJECT.md` and `tools/roles/README.md`. By value: the two role agent files whose `rules:` lists take `cross-os?` as optional. Each reader came from `git grep` over the tree.

**Hygiene re-run:** `check-memory-hygiene.sh --only 2,25` exits 1, but checks 2 and 25 print no failure. The exit 1 comes from check 12, which runs in the same block as 25. All my specs are under the 49152-byte ceiling.

**Still open, outside the brief:**
- **Check 12 is red.** 26 hand-offs have no matching reverse edge in the sibling spec (for example, spec 15 hands off to spec 1 and spec 1 has no matching consumes-from back). Separately, spec 30 hands off to spec 21, which is ordered before it. None of my edits added an edge or changed an edge's type or target.
- **Spec 33 AC6** still plants `successor = "<new tag>"`, while spec 15 names the change-record field `Successor`. I left it because the brief said to change nothing else.

Files are in `C:\projects\coding-governance\.claude\worktrees\unattended-dorderedcharter-10a315\memory\builds\dOrderedCharter\spec\`:
- `2026-10-23-spec-PLAY-dOrderedCharter-1.md` through `-37.md` (every number except 5)
