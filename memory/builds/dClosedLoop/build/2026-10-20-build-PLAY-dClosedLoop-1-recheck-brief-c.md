# Second-look brief: run C

**Serves:** research PLAY-dClosedLoop-1

**Your task is to judge each finding below: confirm it or refute it.** This brief is your instructions, not the
subject of your review: do not review it, the audit's seal or its instruments. A defect you see in them goes in one
line at the end of your return, and nowhere else.

Each finding below was returned by a walker reading the sealed copy of the design at
`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Grade a confirmed one by the copy's round record's
`[rubric]` (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`).

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index, and **Stage 0's leads,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`,
   which some findings cite.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/recheck-c/`.

Read nothing else: not the working tree's other records, not the walkers' returns or the reports, not the session's
scratchpad or temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it
alone, since the working tree may differ from it.

## Findings to judge

### C1-F4 — The join factory moves to `tools/lib`, which no adopter receives
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0049
- **Class:** K10, c2
- **Severity:** high
- **Evidence:**
  - cl-0049: "`compute_coverage` moved to `tools/lib` as the join factory … while `map_lib` re-exports the moved names … the template re-copied into adopters through govkit's update".
  - The charter's Kinds fact: "tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead".
  - Probe: `grep -rn 'inline\|gov-internal' tools/lib/*.sh` printed `resolve-python.test.sh:160: <prefix>/lib/ is gov-internal and ships nothing, so a copy-installed kit cannot source a shared library and must carry the function inline`.
  - No clause or record says the moved functions are carried inline.
- **Consequence:** After an update, an adopter's copy-installed codebase-map re-exports from a module that was never installed, so its imports fail. The tags-pack joins that use the factory cannot run in any adopter.
- **Fix:** Make cl-0049 carry the factory inline in every shipped kit that imports it, with a parity leg as for `resolve-python.sh`, or declare `tools/lib` a shipped kit with an install row. Prove it with a copy-install fixture run.

### C1-F17 — The render gate's legacy list is hard-wired shrink-only, so strict's `instructions.legacy: refuse` has no arm
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0050
- **Class:** K9
- **Severity:** low
- **Evidence:** Catalogue: "`instructions.legacy` | shrink-only, refuse | … IW-1 arms the render gate at dOrderedCharter". The strict preset sets `refuse`. cl-0050 says "the render gate armed with a shrink-only legacy list (IW-1)".
- **Consequence:** Under strict, a legacy document is still admitted.
- **Fix:** In cl-0050, read the gate's mode from `instructions.legacy`, with each value planted.

### C2-F5 — Items declare a `map` slot before any ancestor registers it
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0124`
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - 0124: "the items' declarations of the `map` slot and their unfolds", on dPlacedRequest.
  - ownership:100: "the unfolds render in the work order's map slot, dBoundRoles's; the project-map system is dTotalRecall's".
  - dBoundRoles and dTotalRecall both come after dPlacedRequest.
  - Stage 0 K4: "`memory.map-unfold`: read by no chain clause and no item (guard-bearing)".
- **Consequence:** dPlacedRequest's spec cites a work-order slot and a map that do not exist when it lands, and no stand-in is declared, unlike 0125's probe parts.
- **Fix:** Either move 0124 to dBoundRoles, or add "an empty slot rendered as not installed until dBoundRoles and dTotalRecall land, seen on the core-only install".

### C2-F14 — The commit kind's position-engine reader has no writer until the commit queue lands
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0108`
- **Class:** K3
- **Severity:** medium
- **Evidence:**
  - 0108: "… and the position engine reading them".
  - Stage 0 K3: "commit: no writer item … written by the commit queue". memory-plan:157 names the writer as "the commit queue from the act binding", which is dWellOiledMachine's.
  - gap-spine-08: "0 of 6,084" commits carry the item, act or session that made them.
- **Consequence:** Between dDeclaredLoop and dWellOiledMachine, the engine reads `Gov-*` trailers that no commit carries. Position then falls back to subject parsing with no rule saying so.
- **Fix:** State 0108's interim: until the commit queue writes the trailers, the engine reads the subject view, seen on today's commits. Name the writer by tag.

### C3-F19 — The resolve check can go green on an empty population
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0241
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** layer-memory [annotations] says: "Its first green proves nothing … the population is empty. Three planted red cases are owed … a dangling `refs=` id, a dangling `refs=` path, and a `gov:feature` tag with no entry … The check asserts a non-empty population once the first annotation lands". Clause 0241 says: "the generated annotation index and its resolve check (`annotations.grammar`), the shipped-evidence signal re-checked first".
- **Consequence:** A gate never seen red, over an empty population, is read as coverage, against the charter's [gate] rule.
- **Fix:** Carry the three planted reds and the non-empty assertion in 0241.

### C3-F21 — The touched-block comment budget is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0244
- **Class:** K8
- **Severity:** medium
- **Evidence:** systems [design-annotations] says: "Budget. A block a commit touches is at most 12 lines, and a head line at most 160 B". The annotations leg's checks include "the touched-block budget; history inside a note's body; one anchor per feature tag". gap-mem-18 says: "Comment load is unbudgeted". Clause 0244 says only: "the `annotations` leg, the marker query … and the read hook". 0248 covers only the untouched blocks.
- **Consequence:** New long comment blocks pass, and gap-mem-18 stays open.
- **Fix:** List the leg's checks in 0244, the touched-block cap among them, each seen red on a planted case.

### C3-F30 — The lexicon declaration kind has no declared writer or reader in any clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0269
- **Class:** K3
- **Severity:** low
- **Evidence:** layer-memory [contract] says: "lexicon declaration | dMindYourWords | … dMindYourWords builds the declaration and its packs; writer item not named". Stage 0's K3 lists it as both "no writer item" and "no reader". Clause 0269 says: "declared by the owner, custom packs included (`lexicon.packs`)".
- **Consequence:** The kind's registry row has no door, and the one-door check cannot grade it.
- **Fix:** Name the declaration as a registered kind in 0269, its door `instructions.edit` and its reader the lexicon's pack loader.

### C4-F7 — Lease expiry by "tip unchanged" cannot fire while the fenced pushes keep moving the tip
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0324 (with cl-dClosedLoop-0284 and cl-dClosedLoop-0293)
- **Class:** K10 (a race across nodes)
- **Severity:** medium
- **Evidence:**
  - 0324's red case is "a planted holder that loops while active, its lease lost after `leases.expiry-hours`". The `renewal` fixture plants a holder "whose acts write commits".
  - The catalogue's `leases.expiry-hours` row says "an observer seeing the tip unchanged this long".
  - cloud-and-scale `[design]` 2 says "Every effect push, a pass push … carries the holder's new lease beat".
  - `build.push` defaults to every-pass (0318).
  - 0284 says "its liveness its build lease's beat".
- **Consequence:** a looping holder that commits pushes a new lease beat at every pass, so the observer never sees the tip unchanged. The lease never expires, and the P39 arm cannot go red as specified.
- **Fix:** in 0324 (and 0293), state that expiry reads the last progress-renewal stamp carried in the lease record, never the tip's movement. Add an arm in which a committing, witness-free holder loses its lease.

### C5-F4 — The playbook gate lives in the kit that convergence deletes, and no clause moves it out first
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0486 (and cl-dClosedLoop-0392)
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - cl-0392 makes "`check-playbook` as Design's pack".
  - cl-0486 retires the unattended kit, with "the gate legs that reference the kit … each re-pointed or retired with it".
  - In `tools/gate-legs.json`, the leg "playbook validity gate" has argv `['bash', '{prefix}/unattended/check-playbook.sh']`. The probe was a python scan of the legs for `unattended/`.
  - The script itself is `tools/unattended/check-playbook.sh`. `--record-piece` and `--record-set` live in `tools/unattended/unattended.sh:29-30`.
  - The fates row reads: "playbook mode (`--record-piece`, `--record-set`, `check-playbook`) … RESHAPED … Design's pack (dIndexedDesign)".
- **Consequence:** Under cl-0486's "re-pointed or retired", a builder may retire the playbook gate as a leg of the retired kit. The script then disappears with `tools/unattended/`, and gap-flow-17's recipe half is lost.
- **Fix:**
  - cl-0392 moves `check-playbook.sh` and the piece and set recorders to the loop kit's home in its own unit, with their readers re-pointed.
  - cl-0486 names that leg as re-pointed, never retired, and runs it on the scratch clone with `tools/unattended/` removed.

### C5-F6 — Caps, the rework budget and deadlines are "re-derived" with no route through the owner, though raising a loop bound is a loosening
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0461, cl-dClosedLoop-0473 and cl-dClosedLoop-0474
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - cl-0461: "caps re-derived from evidence and review cost". cl-0473: "the rework budget, the deadlines and the thresholds re-derived from that evidence once 30 builds have run".
  - P9: "A cap's value is the owner's".
  - v2 `flow.rework-budget`: "raising it is a loosening, the owner's alone".
  - stall-and-loop item 11: "Observability trends, never decides". Item 8: "raising any loop bound … is a loosening: under `flow.adapt` it waits for the owner".
  - layer-expansions `loop.propose` "re-derives the caps", and `loop.file` routes to "the owner's breakpoint, as `review.loop.retire` says".
  - Contrast cl-0463: "through the guarded policy command, the owner's own setting for a role winning".
- **Consequence:** A builder can apply re-derived values directly. That loosens a loop bound unattended, or overwrites an owner's cap. dDeclaredLoop's static check would then refuse the Loop Review's own write.
- **Fix:** Each of these clauses files its re-derived value as a `loop.file` proposal through the guarded policy command, the owner's setting winning and a raise waiting for the owner. Plant a re-derivation that writes the policy directly and see it red.

### C5-F15 — The deviation and coverage gaps are owned by the bootstrap build, not the build whose gate closes them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0412 (and cl-dClosedLoop-0398)
- **Class:** K8
- **Severity:** low
- **Evidence:**
  - gap-build-07: "A deviation is recorded but never gated", owned by dTrueNorth (final-questions [gaps]). gap-design-13 is likewise dTrueNorth's.
  - The gap register's rule (the folds' closing review, 2026-10-19): "owned by the one whose landing completes the closure, which descends from the other".
  - The gate is cl-0412 (dScopedBuild) and the Design exit read is cl-0398 (dIndexedDesign). Both descend from dTrueNorth.
- **Consequence:** The gap join reads "never gated" as closed when dTrueNorth lands, before any gate exists.
- **Fix:** Move gap-build-07 to dScopedBuild and gap-design-13 to dIndexedDesign, or split each gap into the instrument key and the gate key.

### C5-F17 — The reuse check's re-entries omit the rework budget and the non-converging end that flow-steps settled
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0410
- **Class:** K2
- **Severity:** medium
- **Evidence:**
  - cl-0410: "re-entries bounded by `flow.route-backs`".
  - flow-steps [build] `build.reuse-check`: "re-entries past `flow.route-backs` → that item's loop ends non-converging and its open rows go to asks, each re-entry drawing on `flow.rework-budget` (revised 2026-10-19 by the owner's SL-1 and SL-2)".
- **Consequence:** A reuse-check loop built from the clause neither draws on the build's budget nor files its open rows as asks, which breaks P39's single budget per build.
- **Fix:** Append to cl-0410: "each re-entry drawing on `flow.rework-budget`, and past `flow.route-backs` ending non-converging with its open rows filed as asks". Seen on a planted fourth re-entry.

### C5-F23 — `design.streams` names both an item and a key, and the planner item's Needs loops onto itself
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0397
- **Class:** K1
- **Severity:** low
- **Evidence:**
  - Stage 0's leads K1: "design.streams: a cycle among Needs: design.streams > design.streams".
  - flow-steps' Needs cell: "`design.overlaps`, where `design.streams` holds".
  - The precedent: layer-expansions renamed "the key `maintain.record` to `maintain.record-when` … so the item `maintain.record` keeps its name".
- **Consequence:** The needs graph and the tag index cannot tell the item from the key.
- **Fix:** Rename the key, for example `design.streams-when`, in v2 [policies], flow-steps and cl-0397.

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/recheck-c/` only. Your effort is the one the owner's
role definition sets.
