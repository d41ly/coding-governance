# Walk return: run B, walker 4, a review of its brief

**Serves:** research PLAY-dClosedLoop-1

Dispatch 168's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-9-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I found five defects in the B4 walk brief. All five weaken the audit's recall measurement; none are errors in what the brief asks the walker to walk. Its slice matches the whole-audit's `[slicing]` row B4, and the item counts are right: 8 `review.*`, 7 `probe.*` and 6 `life.*` rows in the copy's flow-steps. Every record it names exists in the copy. The code it points to has not changed since the copy's base (`git diff --stat 747a2af22..HEAD -- tools skills .githooks` printed nothing). I wrote nothing to the repository, and this return quotes no planted text.

Spec under review: `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-walk-brief-b4.md`

---

### F1 — The copy the brief tells walkers to read freely contains its own catalogue of the planted escapes
- **Section:** brief "Where you read", second bullet ("Every design record from the sealed copy only: `.../build/` ... The copy is the design under audit").
- **Severity:** high, c3 (the recall score would credit detection it never measured).
- **Evidence:**
  - `seed.py` builds the copy with `git archive ... BASE`, the whole tree. It cuts sentences from only three records: final-questions, research-final-audit and whole-audit (`grep -n 'cut' k7q2/seed.py`, lines 95–103).
  - The copy's past reviews and their comparisons therefore survive in the copy:
    - `grep -n -i -E 'declined.{0,80}retir' seed-dcl/tree/memory/builds/dClosedLoop/{reviews,build}/*` printed `reviews/2026-10-18-review-...-shape-audit-b.md:776:### M31. A declined retirement leaves convergence unable to exit`, with its fix at line 784.
    - It also printed `build/2026-10-18-build-...-shape-reviews-compared.md:104:| \`declined-retirement\` | ... | fold |`. Line 132 of that file lists `supervisor-restart` too.
  - Both are plant labels in `seed.py` ("P05 declined-retirement", "P03 supervisor-restart").
  - The plants are by definition "escapes ... each fixed by a fold since" (copy's whole-audit `[recall]`). Their reviews and fold records are in the folder the brief calls "the design under audit".
- **Consequence:** A walker can find plants by reading old findings and checking whether each fix is present, without walking anything. Run B's recall against the bar of 8 of 12 (10 of 12 across both runs) is then inflated and can't be separated from real detection. Run A had the same exposure.
- **Fix:**
  - `seed.py` should strip from the copy `memory/builds/dClosedLoop/reviews/`, every `*-reviews-compared*.md`, and the fold and answers records that list findings. The design map should then be re-rendered.
  - Failing that, the brief should forbid those paths by name.
  - For runs already dispatched: each return gets a "records read outside the allowed set" line, and the scorer reviews by hand every hit whose plant appears in those records.
  - Check that it holds: `grep -rl -iE 'declined-retirement|supervisor-restart' <copy>` prints nothing.

### F2 — The sealed key, the seeding script and run A's returns can be read from where walkers work, and the brief's pinned hash identifies the key
- **Section:** brief, opening paragraph ("you will not see its findings") and the key paragraph ("its SHA-256, fixed before launch, is `505c5243...`").
- **Severity:** high, c3.
- **Evidence:**
  - `ls -la C:/Users/d41ly/AppData/Local/Temp/claude/k7q2` printed `key.json`, `seed.py` and `returns/`.
  - `sha256sum k7q2/key.json` printed `505c52433040...b7b7`, exactly the brief's hash.
  - `returns/` holds `...-walk-return-a1.md` to `-a5.md`, timestamped 00:41–00:48.
  - `k7q2` sits next to `seed-dcl/` in the same temp root that the brief sends walkers into.
  - The brief's reading rules forbid only `memory/` in the working tree and design records outside the copy. Neither the key, the script nor the returns is a design record.
- **Consequence:**
  - Listing the temp root exposes all twelve plants, and the published hash lets a walker confirm which file is the key.
  - The brief's promise that this run "will not see" run A's findings is not enforced, so the two runs are not independent. That breaks Chapman's two-run estimate and the union's recall.
- **Fix:**
  - Move `key.json`, `seed.py` and `returns/` outside any path a walker's Bash can reach, or encrypt them until scoring.
  - Add to the brief an allow-list: the copy, `design-map.txt`, `stage0-leads.md`, the working tree's `tools/`, `skills/` and `.githooks/`, and the walker's own scratch folder. Everything else in the temp root is forbidden.
  - Have the return declare "read outside the allow-list: none".

### F3 — The walker's scratch folder sits next to Stage 0's run on the copy, which lists both mechanical plants
- **Section:** brief, "What you return", last paragraph (probes write under `.../scratchpad/walk-b4/`).
- **Severity:** medium.
- **Evidence:**
  - `diff audit-run/stage0-tree-k3k5.out audit-run/stage0-copy.out` in the same scratchpad printed the copy-only reds:
    - `K3 dupes: no writer item: ...`
    - `K5 P23: names \`cl-dClosedLoop-0093\`, which no clause carries`
  - The same scratchpad also holds `walkkit/briefs/` (run A's briefs), `seal_run_b.py` (whose text quotes the cut sentence naming both mechanical plants' kinds), and run A's scratch folders `walk-a2` to `walk-a5`.
  - The brief restricts reading to the copy only for design records. Nothing forbids reading sibling scratch folders.
- **Consequence:** The two mechanical plants can be read off a neighbouring file. This is the same kind of leak as run A walker 5's breach, which run B's sealing was meant to close.
- **Fix:** Give run B's walkers a scratch root with nothing else in it, for example `.../scratchpad/walk-run-b/<walker>/` created empty. Move `audit-run/`, `walkkit/` and `walk-a*` out. Add the scratchpad's other contents to the brief's forbidden set.

### F4 — The copy's whole-audit still names the mechanical plants' classes, and the brief makes walkers read it
- **Section:** brief, opening paragraph ("whose `[scenarios]`, `[walk-table]` and `[rubric]` you follow") and the seal it assumes.
- **Severity:** medium.
- **Evidence:**
  - The copy's whole-audit `[recall]` reads: "Two are mechanical, and Stage 0 must catch both on the copy itself (`stage0.py --root <copy> --arms K3,K5`)".
  - Its `[rubric]` defines K3 as "a record kind with no writer or no reader" and K5 as "a principle no clause enforces".
  - The cut sentence (per `seal_run_b.py`) was "a kind's writer dropped and a principle's enforcing clause dropped". The `--arms` list plus the rubric restores the same information.
  - The copy also ships `stage0.py`. Its leads file says Stage 0 was "never on the copy", but nothing in the brief stops a walker running it there.
- **Consequence:** The "sealed tighter" claim for run B (commit `abbc8c76d`) does not hold. Any walker who reads `[recall]`, or runs one bounded command, gets the two mechanical plants.
- **Fix:** Either cut the `--arms K3,K5` parenthesis from the copy's `[recall]` and leave the two mechanical plants out of walker recall (Stage 0 is scored on them by design), or say so in the brief. Don't count them as walker hits.

### F5 — The brief's FMEA and STRIDE steps can't fail: nothing in the records to read, nowhere in the return to put them, and no check on them
- **Section:** brief, "How you walk", steps 3 and 4.
- **Severity:** medium.
- **Evidence:**
  - Step 3 says "read its failure mode, its effect and how it is detected (the FMEA columns)".
  - The copy's flow-steps item tables have the header `| Item | Actor | Needs | Does | Proven by | Then | Owner |` in all four sections checked. `grep -i 'fmea\|failure mode'` on flow-steps printed nothing.
  - research-final-audit `[5]` line 207 defines FMEA as a lens the walker *produces*: "FMEA columns per item: failure mode, effect, detection, route".
  - The return's walk-table has columns only for actor, needs, witness, route and verdict. It has no slot for failure mode, effect or detection, and none for STRIDE.
  - `grep -n -i 'fmea\|stride' build/...-walk.py` hits only the brief template at line 222. `walk.py check` reds rows, cells, verdicts and ids, never a missing FMEA or STRIDE reading.
- **Consequence:**
  - A walker that skips both lenses passes the return check. Per the gate rule, a lens that can't go red is not coverage.
  - The trust-boundary readings on S2 and S4 (spoofing, tampering and so on) are where the critical K10 cases sit, and they are unverifiable.
- **Fix:**
  - Reword step 3 to "write, for each item a failure reaches: failure mode, effect, detection, route".
  - Add `FailureMode | Effect | Detection` cells to rows whose scenario injects a failure, and a `STRIDE` block per S2 and S4 data flow, to the return shape.
  - Extend `walk.py check` to red their absence. See it red on a return with one cell dropped.

---

**What I checked:** the brief; its siblings b1–b5 and a1 (by diff); the copy's whole-audit `[scenarios]`, `[slicing]`, `[walk-table]`, `[rubric]`, `[briefs]` and `[recall]`; research-final-audit `[5]`; the three step sections of flow-steps; `stage0-leads.md`; and `seed.py`, reading its plant labels and file targets only.

**What I did not run:** `walk.py check`, `stage0.py` and `score.py` (gates and instruments).

**Probe locations:** commands above are relative to `C:/Users/d41ly/AppData/Local/Temp/claude/` (temp root) and `.../1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/` (scratchpad).
