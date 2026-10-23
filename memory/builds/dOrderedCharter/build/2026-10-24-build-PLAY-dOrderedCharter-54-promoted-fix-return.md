**Serves:** research PLAY-dOrderedCharter-54

# Promoted-fix pass, round 2 follow-up — the spec writer's return

Both follow-ups are done. Spec 49 is now **47958 B** for the whole file, records rows included, and spec 54's AC2 and AC4 now probe the unit's own script instead of naming the test suite. I can't run `check-spec-tokens.py`, so the `[bar]` fix rests on a probe that reuses its `BAR` regex (below).

**Spec 49.** "48000 B of your text" can't mean the text without the records rows. That text was already 47643 B, and with the 1711 B rows block it came to 49354 B. So I trimmed the whole file to at most 48000 B, which leaves about 1.2 KB for the next records rows.
- **What changed:** only prose, almost all in §2, plus four lines in §4 and §5.
- **What a check against the staged rev-2 shows is unchanged:** all 73 scope items with their report ids and their AC pairings; §6, §7 and §8 byte-for-byte (every criterion, gate, New arm line and fork); the §3 Edges block byte-for-byte; and the §1 list of report items and ids.
- **One wording I had to put back:** my first rewrite of S62 said unit 34's relay "drops" two states. Check 25 reads that as a retirement and asks for a Readers clause, so it now says "filters them out", close to the original.

**Spec 54, new AC2:**
> - **AC2** — When `bash skills/session-kickoff/manifest-check.sh --card --write < payload-s2.json`, session `s2`'s SessionStart payload, runs in a fixture worktree whose `orientation-card.md` is owned by session `s1`, its transcript touched now, `grep -c "card-owner — s1" orientation-card.md` still prints 1 and the output carries unit 49's `card-file — skipped:` line.
>   Red when: a live owner's card is overwritten.

**Spec 54, new AC4:**
> - **AC4** — When `bash skills/session-kickoff/manifest-check.sh --card --write < payload-s1.json`, session `s1`'s SessionStart payload, runs in a fixture worktree whose `orientation-card.md` `s1` owns, the file is rewritten, its `orientation —` line's `written` stamp moved, and the output carries neither `card-file — skipped:` nor `card-file — took over:`.
>   Red when: a session is refused its own card.

- **Where the payload and card come from:** `--card --write` with the session's JSON on stdin is the existing interface (`manifest-check.sh:19`, `:284-300`). The card file `.claude/orientation-card.md` is unit 8's. I cite it by basename because it is git-ignored, so a full path would be an untracked-path hit.
- **The suite arm:** §7 already carries `New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC4`, so I left it as is.

**Checks:**
- A probe reusing check-spec-tokens' own `BAR` regex finds no bar match and no untracked path among spec 54's §6 tokens.
- `--only 12` and `--only 25` both exit 0 with no failure line for a dOrderedCharter spec. Each prints the same four "check 25 did not grade … READER NOT IN TREE covers it" notes as before, on specs 19 S7, 30 S5, 34 S8 and 43 S3.

Files changed, in `C:\projects\coding-governance\.claude\worktrees\unattended-dorderedcharter-10a315\memory\builds\dOrderedCharter\spec\`:
- 2026-10-24-spec-PLAY-dOrderedCharter-49.md (47958 B)
- 2026-10-24-spec-PLAY-dOrderedCharter-54.md
