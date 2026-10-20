# Walk return: run B, walker 5, a review of its brief

**Serves:** research PLAY-dClosedLoop-1

Dispatch 169's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-10-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I found three defects in the run B, walker 5 brief, and one of them is serious enough to fix before this walker reads anything. Each was established with a read-only probe. I wrote nothing to the repository and ran no gate.

The spec is `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-walk-brief-b5.md`. It is rendered from the `TEMPLATE` and `EXTRA` blocks in `.../build/2026-10-19-build-PLAY-dClosedLoop-1-walk.py`, so every fix below goes in `walk.py` and then the five run B briefs are rendered again.

### F1 (blocker) — The sealed key, the seeding script and run A's returns can be read from where the walker is sent
- **Address:** walk-brief-b5, "Where you read" and "What you return" (`walk.py` TEMPLATE). The parent record is `whole-audit` [recall] and [walk].
- **Evidence:**
  - The brief sends the walker to `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/`. The folder next to `seed-dcl/` in that temp root holds the key, the seeding script and run A's returns:
    - `find .../Temp/claude -maxdepth 4 -iname '*key*' -o -iname '*seed*' -o -iname '*return*'` printed `.../Temp/claude/k7q2/key.json`, `.../k7q2/seed.py` and `.../k7q2/returns/...-walk-return-a1.md` through `-a5.md`.
    - `sha256sum .../k7q2/key.json` printed `505c52433040b18b95d5da9021b5ad0feada756b88290857a1b9eee9c4b837b7`. That is exactly the hash the brief pins, so the walker can confirm the file is the key.
  - The brief's scratch folder `.../scratchpad/walk-b5/` sits in the same scratchpad as `walk-a2` to `walk-a5`, which are run A's walkers' scratch (for example `walk-a2/dBoundRoles.row` and `walk-a5/clauses.txt`). It also sits beside the walk kit (`walkkit/briefs/` holds all ten briefs) and earlier plant files (`v2-planted*.md`, `plant/`).
  - The only read rule the brief adds is "Nothing under `memory/` in the working tree but this brief". Nothing in it fences off the temp root or the scratchpad's other folders.
  - The brief tells the walker "you will not see its findings". [walk] says run A's returns are kept "outside the scratchpad", but they are in a folder one directory listing away from the copy.
- **Consequence:**
  - A walker that lists the copy's parent folder can read every plant and every one of run A's findings. Run B's recall, and the joined recall that gates the audit, would then measure that, not what the walk found.
  - This would be the second breach of the same kind: run A's walker 5 already read the working tree's record.
  - The rubric calls this c3: the recall gate certifies something it does not check.
- **Fix:**
  - Before run B launches, move `k7q2/` (key, `seed.py`, `returns/`) out of the temp root and out of the scratchpad, to somewhere no read rule sends a walker.
  - Give run B walkers a scratch root that does not contain `walk-a*`, `walkkit/` or any plant files.
  - Add a rule to the brief: read nothing outside the copy, the working tree's `tools/`, `skills/` and `.githooks/`, and your own scratch folder.
  - Check before dispatch: `find <temp root> <scratch root> -name 'key.json' -o -name 'walk-return-*'` must print nothing.

### F2 (medium) — The brief never names the 26 expansion items it requires a row for
- **Address:** walk-brief-b5, "Your slice" (`Steps: ... expansions (26 items)`) and the reading list (`EXTRA["S4"]`).
- **Evidence:**
  - Deriving the items on the copy, the way `walk.py derive_items` does, gives 26 tags, from `maintain.lease` … `loop.price` … `release.route` … `kits.offer`, `kits.install` and `kits.update`.
  - Checking where four of them appear: `kits.offer`, `release.route`, `loop.price` and `maintain.direct` each occur 0 times in the copy's `design-map.txt` and 0 times in `flow-steps`. They appear only in `layer-expansions` (2, 6, 3 and 2 times).
  - The level-0 map has `step.*` rows for the ten flow steps but none for expansions, because items are folded at level 0. The flow-steps `[expansions]` section names only families such as `maintain.*` and `loop.*`.
  - The brief says "Read `flow-steps` whole". It lists `layer-expansions` only as extra reading "For S4", and nowhere says the expansion items are that record's items.
- **Consequence:** The walker can only guess the 26 tags. `walk.py check` rejects a return that misses a row ("a missing row"), so any guessed or partial list fails the return. Items the walker misses go unwalked in all seven scenarios.
- **Fix:** Have `brief()` list each step's item tags, at least the expansions' tags, which it already has from `derive_items`. Name `layer-expansions` as the home of the expansion items, separately from the S4 reading list.

### F3 (medium) — Walker 5 has the heaviest load in either run at the same medium effort
- **Address:** walk-brief-b5, "Your slice" and "What you return" item 3. The cause is `whole-audit` [slicing], row B 5.
- **Evidence:**
  - B5 owes 31 items × 7 scenarios = 217 rows. The others owe: B1 17×7 = 119, B2 24×7 = 168, B3 23×7 = 161, B4 21×7 = 147, and each run A walker 116.
  - B5 also reads seven extra records (three for S2, four for S4), on top of `flow-steps` and v2.
  - The brief ends "Your effort is the owner's medium."
- **Consequence:** An incomplete table fails `walk.py check`. A complete but shallow one lowers recall on the adopt and expansions items, which no other run B walker covers. This adds noise to run B's recall bar of 8 of 12.
- **Fix:** Re-slice [slicing] so B5's rows come down toward the other walkers' (around 150), for example by moving `adopt` to B4. Alternatively, give B5 an explicit higher effort, recorded in [walk].

### Checked and sound
- The adopt and expansions item counts (5 and 26) match the copy.
- All five builds are in the copy's `[chain]`, and it runs from dTrueNorth to dConvergedCharter.
- All nine principles are among the copy's 42.
- Every record the brief names exists in the copy, including `fates`, `cloud-and-scale`, `stall-and-loop` and the whole-audit record's `[scenarios]`, `[walk-table]` and `[rubric]`.
- `git diff --stat 747a2af22 HEAD -- tools skills .githooks` printed nothing, so the code the walker reads in the working tree matches the commit the copy was made from.
