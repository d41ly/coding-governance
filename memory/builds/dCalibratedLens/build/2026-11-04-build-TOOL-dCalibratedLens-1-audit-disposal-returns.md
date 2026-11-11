**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-24

# dCalibratedLens — the cross-check audit's disposal writers' returns, verbatim

The six `gov-spec-writer` returns that fold the spec-audit record [`2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit`](../reviews/2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit.md), extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-04-prompt-TOOL-dCalibratedLens-1-crosscheck-audit-disposal`](../prompts/2026-11-04-prompt-TOOL-dCalibratedLens-1-crosscheck-audit-disposal.md); each group's handoff sits beside it.

## Group D1, led by spec 1 (specs 1 and 24)

Handoff: [`2026-11-04-prompt-TOOL-dCalibratedLens-1-1-spec-writer`](../prompts/2026-11-04-prompt-TOOL-dCalibratedLens-1-1-spec-writer.md).

1. Items, one per bullet:
   - M7 on cl1: folded. Moved S5 (the main loop runs `--trigger` only for a review breakpoint, `--cause` comes from the line's `cause` field, and a step outside `REVIEW_STAGES` gets no `--stage`), S7, the §4 stage path, AC11 (the `--plan` fixture with an owner-gate line and an `item.review.dispose` placement) and the §7 unattended arm.
     - Review breakpoint means a line named one of TOOL-dDeclaredLoop-19 §4's review names (`breakpoint`, `spec audit`, `closing review`, `gate review`, `landing review`) or with cause `placement`. Owner gates, owner items and the ratification stand-in take no `--trigger`.
     - A step outside `REVIEW_STAGES` uses §4's "absent" row: the call maps its subject and reads `spec-review`'s default stage. I picked this over refusing at placement because refusing would change dDeclaredLoop's `derive_breakpoints`, a parent primitive.
   - M8 on cl1: folded. S4: a `REVIEW_STAGES` member with no literal read raises a `RolesError` naming the stage. AC4's red text no longer claims to observe a single home. AC8 and the adopt-roles arm gain a `"release"` member case. §5 updated. No parity gate added.
   - M10 on cl1: folded. S5: `--trigger` finds `handoff.py` through the inline `resolve_kit_dir "$py" roles handoff.py <here>` (`tools/unattended/lib-unattended.sh:133`). With the roles kit absent it prints a stderr `note` naming `handoff.py`, omits `efforts`, and exits as it would with roles present. AC9 gains a no-roles fixture, and §5 and the §7 unattended arm are updated. No kit edge added.
   - M11 on cl1: folded. S4 now parses the `^REVIEW_STAGES = ` line as text with `ast.literal_eval` and never imports `review_pin.py`. Three failures each raise a named `RolesError`: review-harness absent, no `REVIEW_STAGES` line, and a right side that is not a tuple of strings. AC8 gains fixtures for the stale and malformed cases, red against a traceback, run in a scratch install. §5 and the adopt-roles arm updated.
   - L9 on cl1: folded. AC11's `grep -c 'breakpoint:'` clause is replaced by three greps over the rendered guide (`--trigger.*--cause.*--stage`, `owner item. line.*takes no .--trigger`, `REVIEW_STAGES.*takes no .--stage`). S7 has the guide state each of those three sentences on one line. The staged break deletes them.
   - L1 on cl24: folded. AC1 now uses the anchored `grep -n '^- \*\*AC3\*\*.*check-verifier-fanout.js --hook'` and requires exactly one line. A re-run over cl1 prints only :409.

2. Specs edited:
   - `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-1.md`: rev-6, 56601 bytes (from 48632).
   - `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-24.md`: rev-4, 14621 bytes.

3. Hygiene: I copied the index, staged only the two specs into the copy, ran `GIT_INDEX_FILE=<copy> bash tools/memory-tree/check-memory-hygiene.sh --staged`, then deleted the copy. It exited 1. The only failure was "HYGIENE check 9 FAILED — generated build index differs from a fresh render", listing LIVE.md, the build README and every re-revised dCalibratedLens spec (cl1 and cl24 among them) as stale. That is a `gen_build_index.py --write` cure, so it is left for the main loop. Nothing else names my specs; the remaining lines are checks held under `--staged`. The copied index also already held `memory/builds/dCalibratedLens/build/2026-11-02-build-TOOL-dCalibratedLens-2-chain-rounds.md` as staged. That file is not mine and is not in the starting git status, so another writer may have staged it into the real index.

4. Parent text that looks wrong:
   - `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-19.md:135`: a `review.breakpoints` placement takes the name `breakpoint`, the same name §4's table gives the Plan review at :142. A `breakpoint:` line is therefore told apart only by its `cause`, and S1's name list at :42 does not say this.

## Group D2, led by spec 3 (specs 3, 2, 5 and 19)

Handoff: [`2026-11-04-prompt-TOOL-dCalibratedLens-3-1-spec-writer`](../prompts/2026-11-04-prompt-TOOL-dCalibratedLens-3-1-spec-writer.md).

1. Items

- **M1 on cl3: folded.** Moved §4 "The items" (the paragraph after the table) and AC7.
  - `file` and `record` now carry `allowance = "records"`, and `lease` and `gather` keep `"none"`. Each is cited to `WRITES` at `tools/roles/check_roles.py:96`.
  - Each of the four rows now carries `witness = { class, by = <the table's Witness cell> }`, in cl2 S9's form.
  - The class is `history` on `lease`, `gather` and `record`. On `file` it is `hook-record`, derived rather than picked. The intake is node-local and never committed (TOOL-dWellOiledMachine-4 S1), so it is not a `history` fact. It is written through the hook's one writer, `write_intake` (TOOL-dWellOiledMachine-27 S1).
  - AC7 now requires `python loop_lib.py --check` to exit 0 refusing none of the four rows, with a permission line naming dDeclaredLoop's unit 12 and ask TOOL-dDeclaredLoop-110.
- **M5 on cl3 and cl2: folded.** One wording in both: the commit landing the first record and its snapshot strips `unarmed` from both the `loop-review` and the `value-ledger` rows.
  - On cl3 it moved S8, §4 Amendments id 37 and AC8. AC8's scratch worktree now commits one record and one snapshot. It requires exit 1 naming `unarmed` while either row keeps the key, and exit 0 only once both have lost it.
  - On cl2 it moved §4 Amendments id 37, which now names TOOL-dCalibratedLens-3 AC8 as what observes both drops.
  - In S8 I kept the old phrasing, the rows edited "to carry no `unarmed` key". My first draft said "drops", and check 25 then read S8 as retiring a named thing.
- **M6 on cl5: folded.** Moved the §2 preconditions, the §3 Edges and AC9's fixture line.
  - Names TOOL-dTotalRecall-108, the dTotalRecall BACKLOG row filed 2026-11-03, with its title.
  - Names TOOL-dCalibratedLens-20's `**Serves:**` line on the keep.
  - The grading is now stated as TOOL-dTotalRecall-42 S5 read with -53 S21 and -108.
  - Edges gain -108 on the external consumes-from line and a new consumes-from on `TOOL-dCalibratedLens-20`.
- **M6 on cl19: folded.** Moved §2 (a new build-run preconditions paragraph, since there was no "Waits on" line), S2, AC3 and §3 Edges.
  - S2 now reads "the per-record grading of TOOL-dTotalRecall-42 S5 read with TOOL-dTotalRecall-53 S21 and ask TOOL-dTotalRecall-108, over TOOL-dCalibratedLens-20's Serves line", as cl20 §4 Evidence and cl42 S2 state it.
  - AC3 gains a fixture line: the build run waits for the ask rather than editing the plant.
  - Edges gain consumes-from lines for `TOOL-dCalibratedLens-20` and for the external TOOL-dTotalRecall-1, -42 S5, -53 S21 and -108.
- **L4 on cl2: folded.** Moved §4 "The row". The `id` cell now says it in words: "a pipe in it escaped as backslash-pipe".

Every quoted defect phrase now greps to nothing. `grep -c dTotalRecall-108` prints 4 for cl5 and 5 for cl19.

2. Specs edited

- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-3.md`: rev-7, 56235 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-2.md`: rev-7, 50457 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-5.md`: rev-6, 52993 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-19.md`: rev-4, 19558 bytes

3. Hygiene run

Command: `GIT_INDEX_FILE=<scratchpad>/d2.index` (a copy of the worktree index, with only specs 2, 3, 5 and 19 staged) `bash tools/memory-tree/check-memory-hygiene.sh --staged`. The copy was deleted afterwards, and the real index holds none of the four.

- Printed `HYGIENE check 9 FAILED — generated build index differs from a fresh render`, with `build-index DRIFT — run: python tools/memory-tree/gen_build_index.py --write`. The stale list covers `memory/LIVE.md`, the build README and the generated records regions of the dCalibratedLens specs. This is render-owed and the main loop's to cure.
- Every other check was clean or HELD: checks 10 and 23, the §3 edge joins and the stale guards. Check 29 graded 0 specs, and check 30 printed "as-built clean".
- An earlier run also failed check 25 on cl3 S8, caused by my word "drops". The S8 rewording above cured it, and the final run names none of my specs.

4. Parent text that looks wrong

- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-9.md:45` places `WRITES` at `tools/roles/check_roles.py:94`, but the tuple is at `:96`.
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-5.md:102` gives no class to a node-local, never-committed record written by a command's own call, as the intake is. I read it as `hook-record`, but the table does not settle it, and a reviewer may read it otherwise.

## Group D3, led by spec 16 (specs 16, 12 and 17)

Handoff: [`2026-11-04-prompt-TOOL-dCalibratedLens-16-1-spec-writer`](../prompts/2026-11-04-prompt-TOOL-dCalibratedLens-16-1-spec-writer.md).

1. Items
- **M3 on cl16:** folded. Sections moved: S2, §6 AC2, §7 `New arm:` line. S2 now gives each refusal its own `<why>`: `not in the journal tuple`, `a stall-and-loop class left out` and `owner items unread`. AC2's `stall-left-out` now plants `no-progress`, which is in the planted tuple, and asserts exactly one line, `stall trend — refused · no-progress · a stall-and-loop class left out`. A separate `stall-cycle-unread` case refuses `cycle` with `owner items unread`. AC2 now requires the build to remove the clause-six check and see `stall-left-out` go red, and the `New arm:` line names that broken version.
- **M12 on cl16:** folded. Sections moved: S8, §6 AC7, §7 `New arm:` line. S8 now says which commit `<commit>` is. For the freeze row it is the commit that added the row, the first line of `git log --reverse --format=%H -S '<the freeze row>' -- <path>`. For every other key it is the commit that added the newest transition record, `git log --diff-filter=A --format=%H -- <path>`. A later commit touching the file never counts. AC7 gains the plant `bounds-value-then-patch`: the value changes to `"6+2"`, then a late patch draw lands on five builds closed under the old value, and the line must read `builds 0 · refused: 0 of 30 rows`. Its Red-when case is a build moving into the new value's population. The `New arm:` line names the broken version: a `--rev` read at a record's latest commit.
- **L2 on cl16:** folded. Sections moved: §4 example, §6 AC3. Every `item.build.unit` became `item.build.unit-pass` at the example line and AC3's three rows.
- **L2 alignment on cl12:** folded. Sections moved: §4 "The rows" (:89, :100, :101), §6 AC1 and AC2. `item.build.unit` became `item.build.unit-pass` and `item.review.synth` became `item.review.dispose`.
- **L2 alignment on cl17:** folded. Sections moved: §4 "The lines" (:135, :136), §6 AC1, AC2 and AC7. `item.build.unit` became `item.build.unit-pass`.

2. Specs edited
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-16.md`: rev-5, 44694 bytes.
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-12.md`: rev-3, 18622 bytes.
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-17.md`: rev-3, 29906 bytes.

3. Hygiene run
- **Command:** `cp "$(git rev-parse --git-path index)" <scratchpad>/idx-d3 && GIT_INDEX_FILE=<scratchpad>/idx-d3 git add memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-{12,16,17}.md && GIT_INDEX_FILE=<scratchpad>/idx-d3 bash tools/memory-tree/check-memory-hygiene.sh --staged`, with the index copy deleted afterwards.
- **What it printed:** exit 1. The only failure is `HYGIENE check 9 FAILED — generated build index differs from a fresh render` (`build-index DRIFT — run: python tools/memory-tree/gen_build_index.py --write`).
  - It lists `memory/LIVE.md`, `memory/builds/dCalibratedLens/README.md` and 26 dCalibratedLens specs as stale, among them cl12, cl16 and cl17.
  - It also says `render owed under --staged — memory/builds/dCalibratedLens/build/2026-11-02-build-TOOL-dCalibratedLens-2-chain-rounds.md is a build-index input or output`.
  - Only a render cures this, so it is left to the main loop.
  - Checks 10, 23, 29, the edge joins and the stale guards are held under `--staged`. Check 30 printed `as-built clean · 1896 deviation records`.
  - Nothing else names these specs.
- **Acceptance greps:** `grep -n` over the three specs for `plants \`cycle\``, `the commit of the`, `commit of its newest`, a bare `item.build.unit` and `item.review.synth` returns nothing (exit 1).

4. Parent text that looks wrong
- None found. One related thing outside L2's stated fix, left unedited: two other example tags that dDeclaredLoop never declares. They are `item.review.verify` at `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-16.md:186` and `item.review.audit` at `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-17.md:135`. L2's proposed gate would catch both.

## Group D4, led by spec 14 (specs 14, 10, 15 and 8)

Handoff: [`2026-11-04-prompt-TOOL-dCalibratedLens-14-1-spec-writer`](../prompts/2026-11-04-prompt-TOOL-dCalibratedLens-14-1-spec-writer.md).

1. Items
- **M2, cl14: folded.** Moved S9, §4 "Waits on", §8 F8 and a new §8 F9, which is the PRIMITIVE GAP "compare_path takes no composition and always files". F9 lists options (a) widen in this build, (b) file an ask on dDeclaredLoop, (c) a local comparison function. It is marked `RESOLVED (agent, 2026-11-04, delegated): (a), the in-build widening, rung 3`, and its reason cites the owner's standing rule as row 83 of `2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck` words it. F8's `grants:` now also covers `tools/loop/adapt.py`'s `compare_path` widening. "Waits on" now says the unit specs none of its parents' primitives "but one". The default-call AC arm the item asks for is AC15, shared with L8.
- **L8, cl14: folded.** Moved §7 prose (it now names `loop adapt fixtures`, TOOL-dDeclaredLoop-28 S8), a new `New arm: tools/loop/adapt.py` line, a new AC15, §4 Inventory (the `unrecorded-skip-unfiled` plant), Files touched, and §5 testing (now AC1 to AC15). The S9 sentence "dl28's boundary call is unchanged" is replaced by a claim that AC15 observes: the default call still files one `flow-deviation` order, and `file_orders=False` files none. The red is staged by flipping the default.
- **M9, cl10: folded, option (b).** Moved S4, which now uses the two-case form decided by `test -f tools/run-gates/leg_factory.py` with a `Decided:` trailer, as units 46 and 47 do. In the hand case the leg's row goes in `tools/gate-legs.json`, plus a `[[exempt_leg]]` row with `name` and `why` only, in the shape of `tools/govkit/registry.toml:666-668`. `check_evals.py` reads the guard from the `gate-legs.json` row, which holds it in either case. Also moved: a §3 consumes-from edge on TOOL-dWitnessedBar-11 (its absence selects the hand case), a §4 "Waits on" sentence saying the unit does not wait on that unit, Files touched, and AC5, which now reads the declaration for whichever case was taken.
- **L3, cl10: folded.** §4 Inventory: the joined row is split into two rows.
- **L6, cl15: folded.** §8 F2 is re-titled "What counts a document's reads?". It names TOOL-dTendedCadence-9 S1's `reads` verb and `measure_path_reads` (its §8 F5 (a)) as the producer S3 extends. "has no producer" and "PRIMITIVE GAP" are dropped, and the resolution stays (a).
- **L7, cl8: folded.** Moved §8 F3 and the §4 "Alternatives rejected" cause-verb bullet. Both now home the parser in `tools/workflows/replay_scorer.py` after TOOL-dFairHearing-12 S2's move, and `review_replay.py` remains only as base-line cites (`:10-23`, `:151`).

2. Specs edited
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-14.md`: rev-4, 43427 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-10.md`: rev-6, 44617 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-15.md`: rev-4, 38199 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-8.md`: rev-6, 36851 bytes

3. Hygiene run
- **Command:** `cp "$(git rev-parse --git-path index)" <scratchpad>/d4-index; GIT_INDEX_FILE=<scratchpad>/d4-index git add <the four specs>; GIT_INDEX_FILE=<scratchpad>/d4-index bash tools/memory-tree/check-memory-hygiene.sh --staged`. The index copy was deleted afterwards, and the real index is untouched.
- **Result:** it exited 1 with one failure, `HYGIENE check 9 FAILED — generated build index differs from a fresh render`. That is `build-index DRIFT — run: python tools/memory-tree/gen_build_index.py --write`, plus "stale — differs from a fresh render" lines on the `gen:spec-records` blocks of most dCalibratedLens specs, mine included.
- **Why it is the main loop's:** only the `--write` render cures these, so I left them. Nothing else named my specs. Checks 10 and 23, the edge joins and the stale guards are HELD under `--staged`, check 29 graded nothing, and check 30 printed "as-built clean".

4. Parent text that looks wrong
- None found.

## Group D5, led by spec 9 (specs 9 and 7)

Handoff: [`2026-11-04-prompt-TOOL-dCalibratedLens-9-1-spec-writer`](../prompts/2026-11-04-prompt-TOOL-dCalibratedLens-9-1-spec-writer.md).

1. Items
- M4 on cl9: folded. Sections moved: §4 id 51, S1, §5 perf, AC1. The parent text gives no batch read. The door's `show` takes one key (`gov_record.py show <id>[#<tag>][@<blob>]`, `dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-9.md:104`), and `read_act_records` runs one `show` per row (`dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-53.md:76-77`). So, as the brief directs for that case, I re-derived the bound for one `show` per act and the spec says why. 500 acts at about 80 ms per Python start is about 40 s before the door does any work, so S1's bound is now 180 s (360 ms per `show`). AC1 gains a `--since` case and a one-time timing over 500 planted act records under 180 s, which the build records. That timing is not an arm case. One thing outside my group: cl17 S4 runs the all-time `ledgers.py acts`-side `estimate` read under a 60 s bound at `2026-11-02-spec-TOOL-dCalibratedLens-17.md:65`, so it carries the same one-`show`-per-act risk.
- L5 on cl9: folded. Section moved: §4 id 50, plus the §5 perf line. Probe records are now listed by `gov_record.py find --kind probe --all` and each read through `show`. Each `probe-trigger` record is read through `show` of the key in its probe's `Trigger`. Until `--all` lands, §2's interim refusal holds. "never `gov_record.py find`" is gone.
- L5 on cl7: folded. Sections moved: §2, S1, §5 security. S1 now lists shape-run records with `gov_record.py find --kind shape-run --all` and reads each through `show <key>`, with `read_record_fields` parsing that text. The `git ls-files` listing is gone. §2 names the door's `find`, `show` and `find --all`, with F6's interim refusal, as a build-run precondition.

2. Specs edited
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-9.md`: rev-5, 38085 bytes.
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-7.md`: rev-4, 23918 bytes.

3. Hygiene run
- Command: `cp "$(git rev-parse --git-path index)" <scratchpad>/index-d5 && GIT_INDEX_FILE=<scratchpad>/index-d5 git add <cl9> <cl7> && GIT_INDEX_FILE=<scratchpad>/index-d5 bash tools/memory-tree/check-memory-hygiene.sh --staged`. I deleted the copy afterwards.
- Output: exit 1. The only failure is `HYGIENE check 9 FAILED — generated build index differs from a fresh render`. It names `memory/LIVE.md`, `memory/builds/dCalibratedLens/README.md` and the `gen:spec-records` blocks of 28 dCalibratedLens specs, including cl7 and cl9, as "stale — differs from a fresh render".
  - That is a `gen_build_index.py --write` cure, so I left it to the main loop.
  - Check 13 named nothing, and nothing else in the output names cl7 or cl9.
  - Checks 10, 23, the edge joins and the debt guards were HELD under `--staged`. Check 29 graded 0 specs, and check 30 printed as-built clean.

4. Parent text that looks wrong
- None found.

## Group D6, led by spec 20 (spec 20, the edge join check 12 asked for)

Handoff: [`2026-11-04-prompt-TOOL-dCalibratedLens-20-1-spec-writer`](../prompts/2026-11-04-prompt-TOOL-dCalibratedLens-20-1-spec-writer.md).

1. The two lines added, verbatim:

```
- **hands-off** `TOOL-dCalibratedLens-5` — the keep's `**Serves:** keep TOOL-dCalibratedLens-5` line, the kind AC9's grading reads
- **hands-off** `TOOL-dCalibratedLens-19` — the `**Serves:**` line on the snapshot and the record, the kind AC3's grading reads
```

They follow the external `consumes-from` edge in §3 Edges of `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-20.md`. Each takes its wording from the matching consuming line: unit 5's spec at line 174 and unit 19's spec at line 104.

2. The new rev is rev-4, dated 2026-11-04. The spec is now 19047 bytes; it was 18586. The §9 line has been added in the spec's existing form.

3. The command was `cp "$(git rev-parse --git-path index)" <scratchpad>/index-u20; GIT_INDEX_FILE=<scratchpad>/index-u20 git add memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-20.md; GIT_INDEX_FILE=<scratchpad>/index-u20 bash tools/memory-tree/check-memory-hygiene.sh`. I deleted the index copy and its output file afterwards.
   - **Check 12:** it printed nothing. The output has no `check 12` line, so neither unit 5's nor unit 19's `consumes-from` `TOOL-dCalibratedLens-20` is named.
   - **Seen red first:** a run before the edit printed `HYGIENE check 12 FAILED — a §3 edge names a sibling that declares no matching edge back`. It named `2026-11-02-spec-TOOL-dCalibratedLens-19.md` and `2026-11-02-spec-TOOL-dCalibratedLens-5.md`, each with "§3 declares **consumes-from** `TOOL-dCalibratedLens-20` and that unit declares no matching **hands-off** ... back".
   - **Still failing:** the run exits 1. The only failure is check 9: the build index is out of date for `memory/builds/dCalibratedLens/README.md` and unit 20's spec. That clears when the main loop renders the index.
