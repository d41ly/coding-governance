# Brief review: run B, walker 4, second dispatch

**Serves:** research PLAY-dClosedLoop-1

Dispatch 172's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-13-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I found six defects in the brief, all new. **F1 is high:** the read rules let a walker read the design's review history, so the score could measure that reading instead of the walk. F2 to F5 are medium and F6 is low. I ran no gate and wrote nothing to the repository. My one probe script is in the session scratchpad.

Paths used below:
- **Spec under review:** `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-walk-brief-b4.md`
- **Round record:** `.../build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`
- **Walk kit:** `.../build/2026-10-19-build-PLAY-dClosedLoop-1-walk.py`
- **Scorer:** `.../build/2026-10-19-build-PLAY-dClosedLoop-1-score.py`
- **Sealed copy:** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/`

### F1 — The read rules let a walker read review history (high, c3)
- **Address:** walk-brief-b4, "What you may read", item 1 (line 15). The same text is in walk.py's `TEMPLATE`.
- **Evidence:**
  - The brief says the walk "reads the design, never its review history". But it only shuts out `*-compared.md`, `*-instruments.md`, session-log, `reviews/` and `prompts/`.
  - Records that pass that rule but are review history:
    - `audit-fold.md`: sections `[fold] Each item, folded` and `[review-fold] The fold's closing review, folded`.
    - `final-reviews.md`: "The folds' closing review…".
    - `walk.md`, `night-pass.md`, `night-pass-two.md`, `away-pass.md`, `ownership-skeptic.md`, `ownership-verify.md`.
  - The brief tells the walker to read `flow-steps` whole. That record carries `## [revised] Revised 2026-10-16: the two Tier-2 rounds, folded` (line 755).
  - v2's lines 4 to 677 are untagged revision notes that narrate folds.
  - The read audit's two new classes are the scratchpad and the temp root outside `seed-dcl/`. Neither flags any of these files.
- **Consequence:** every plant is a past defect "fixed by a fold since". A walker that reads the fold notes can find a plant by matching the note, not by walking to it. The recall would then certify a walk that never happened. This only fails to bite if the seeding cut every such sentence, and nothing checks that the cut covered fold records.
- **Fix:**
  - Replace the exclusion patterns with a named list of the design records the slice needs.
  - Exclude the history parts of required records by section: `[revised]` and v2's preamble.
  - Add a read-audit class for any path in the copy outside that list.

### F2 — The copy's round record names the mechanical plants' arms, and other tools can be run on the copy (medium)
- **Address:** walk-brief-b4, "What you may read" (line 25), together with the copy's whole-audit `[recall]`.
- **Evidence:**
  - `grep -n "K3\|K5"` on the copy's whole-audit printed line 195: "Two are mechanical, and Stage 0 must catch both on the copy itself (`stage0.py --root <copy> --arms K3,K5`)". The brief sends the walker to that record.
  - The working tree's `[walk]` says the sentence naming the plants' kinds had been cut from the copy. This parenthetical survived.
  - The brief forbids only "instrument from the copy against the copy". Running the working tree's `stage0.py --root <copy>` is not forbidden.
  - The brief says "a planted one is scored like any other finding". `score.py` (lines 101–103) counts hits over all twelve plants, mechanical ones included.
- **Consequence:** run B's walkers can score the two mechanical plants for free, which pushes the run toward the 8 of 12 bar.
- **Fix:**
  - Cut `--arms K3,K5` from the copy's round record.
  - Change the rule to "run no instrument against the copy".
  - Score run B on the ten judgement plants, as run A was, and say so in the brief.

### F3 — Build verdicts do not match the items the walker walks (medium, K10)
- **Address:** walk-brief-b4, "Your slice", the builds line (line 37). The cause is whole-audit `[slicing]` row B 4.
- **Evidence:** I parsed the Owner column of the copy's flow-steps against run B's slices. It printed:
  - `B1 dPlacedRequest owns: {'entry': 5, 'probe': 7} | outside walker's steps: {'probe': 7}`
  - `B4 dDeclaredLoop owns: {'plan': 2, 'design': 2, 'build': 1, 'test': 2, 'deploy': 1, 'breakpoint': 4} | outside…: {'plan': 2, 'design': 2, 'build': 1, 'test': 2, 'deploy': 1}`
  - `B4 dWellOiledMachine … outside: {'entry': 1}`
  - `B4 dCalibratedLens owns: {}`. Its items are the `loop.*` expansion items, which walker 5 walks.
- **Consequence:**
  - Walker 4 walks all seven `probe.*` items but gives dPlacedRequest no verdict. Walker 1 gives that verdict without walking them.
  - Walker 4's verdicts on dDeclaredLoop and dCalibratedLens rest on half, or none, of the items those builds own.
  - `walk.py check --report` passes regardless, because it only counts that each build has one verdict.
- **Fix:** render each build's owned items outside the walker's steps into the brief as required rows, or re-cut `[slicing]` so the walker who gives a build's verdict walks its items.

### F4 — The table format the brief asks for makes the last finding swallow the table in the skeptic split (medium)
- **Address:** walk-brief-b4, "What you return", item 3, and walk.py `findings_of`.
- **Evidence:**
  - The brief's format is the lowercase `| item | S<n> | …` with no section heading. `findings_of` ends a finding only at `^### `, `^\| Item ` or `^## `.
  - My probe (`scratchpad/probe_fo.py`) built a return in the brief's shape and ran `findings_of` on it. It printed: `B4-F2 'architecture-v2 [chain]' lines: 12 | table swallowed: True | verdicts swallowed: True`.
- **Consequence:**
  - The skeptic who gets the last finding also gets the walker's whole table of about 147 rows, its verdicts and its read-outside line.
  - That skeptic sees the walker's verdicts on the clean cells it is meant to attack independently.
- **Fix:** have the brief require the exact header `| Item | Scenario | Actor | Needs | Witness | Route | Verdict |`, or `## ` headings before parts 3 to 6. Alternatively, make `findings_of` stop at any table row.

### F5 — Other walkers' notes are readable, and the read audit does not catch it (medium)
- **Address:** walk-brief-b4, "What you may read", item 4 (line 22).
- **Evidence:**
  - `find scratch -maxdepth 2` under `seed-dcl/` shows the other walkers' live notes next to this one's: `walk-b1/dPlacedRequest.txt`, `walk-b3/cl.py`, `walk-b5/policies.txt` and more.
  - The read audit's temp-root class exempts everything under `seed-dcl/`.
- **Consequence:** a walker can read another walker's notes in the same run without being caught. The brief forbids it, but nothing checks that.
- **Fix:** give each walker a scratch folder outside a shared parent, or add a read-audit class for any path under `seed-dcl/scratch/` other than the walker's own.

### F6 — The brief blocks a protocol file the charter tells the walker to read (low)
- **Address:** walk-brief-b4, "What you may read", item 3 (line 21).
- **Evidence:**
  - The charter's protocol list sends "Any record, index or id under `memory/`" to `memory/HYGIENE.md`, and "Writing a spec" to `memory/TEMPLATE-SPEC.md`.
  - `ls memory` shows both files sit outside `memory/guides/`, which is the only part of the working tree's `memory/` the brief allows.
- **Consequence:** a walker reading clause ids has to break either the charter or the brief. Either way it creates an unexplained out-of-list read.
- **Fix:** name `memory/HYGIENE.md` in item 3, or say that the charter's protocol pointers are out of scope for the walk.

The brief also has no slot in the return for the failure-mode (FMEA) and STRIDE readings, and flow-steps has no FMEA columns for "the FMEA columns" to point to. I left this out because the round record's `[walk-run-b]` already records it.
