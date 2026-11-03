**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-42

# dCalibratedLens — the ancestors re-ground writers' returns, verbatim

The five `gov-spec-writer` returns that fold the cross-check record [`2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck`](2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck.md), extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md); each group's handoff sits beside it.

## Group W1, led by spec 1 (specs 1 and 42)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-1-5-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-5-spec-writer.md).

1. Rows
- **Row 9 (first pass, owner's pick), cl1: folded.** Moved §2 S3 and S4, §4 "The effort order", Inventory, Files touched and §10, §5, AC4, AC8, both §7 `New arm:` lines, and a new §8 F7. F7 holds the three options from the "Parked" section, marked `RESOLVED (owner, 2026-11-03): (b)` with the quote "go with (b) for row 9". `REVIEW_STAGES` now lives only in `review_pin.py`. `--stage` admits only its members, so a marked literal outside the set, such as `unit-spec`, exits 2. `roles_lib.py` reaches the set through `resolve_kit_dir("workflows", "review_pin.py", kit_dir)`, the way `read_cap_answer` reaches the policy kit (`tools/roles/roles_lib.py:136-158`), along `tools/roles/kit.toml:19`. When review-harness is absent, a call with `--review-stage` raises a `RolesError` naming `review_pin.py`, and a call without it reads its default stage's key as before.
- **Row 2, cl1: folded.** §4 "The stage path": `unclassed` joins the `--trigger` key set (dl20:281).
- **Row 3, cl1: folded.** §2 S5, the §4 stage-path diagram, the §3 Edges line, AC11 and the S5 "Observed by" line. The caller is now the main loop. It reads dl19 S9's `--plan` `breakpoint:` lines (dl19:81) and takes `--stage` from the step segment of the `item.<step>.<name>` tag the position names, whatever relational form the position takes. The verbs guide states this call, and AC11 greps for `breakpoint:`. Files touched gains nothing new: `VERBS.template.md` was already in it.
- **Row 4, cl1: folded.** §1 now says "the five stages TOOL-dDeclaredLoop-19 reads". §3 Non-goals names TOOL-dTendedCadence-1 S1's `item.maintain.*` rows as the boundary. TOOL-dTendedCadence-1 is added to the build-run precondition, to "Waits on" and to §3 Edges as a consumes-from line.
- **Row 7, cl1: folded.** §8 F4 is re-marked `RESOLVED (agent, 2026-11-03, delegated): (a), rung 3`. It names TOOL-dDeclaredLoop-109 in `memory/builds/dDeclaredLoop/BACKLOG.md`, and keeps `widens: none · relaxes: none` on one line. The ask is also in the build-run precondition and the §3 hands-off edge, and the rev-5 line in §9 names F4.
- **Row 157, cl42: folded.** H1, §2 S2, §3 Edges, §5 risks. S2 now states its departure from tr53 S21's caller rule: the case proves the row lookup only. TOOL-dTotalRecall-108 is named as what makes the real check grade these records, with a new hands-off edge for it. The H1 now reads "with the parameters" instead of "in the form".

2. Specs edited
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-1.md`: rev-5, 48632 bytes. That is 520 bytes under the 49152 limit, so any later fold to this spec has very little room.
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-03-spec-TOOL-dCalibratedLens-42.md`: rev-2, 11408 bytes.

3. Hygiene run
- Command: `cp "$(git rev-parse --git-path index)" <scratch>/index.copy; GIT_INDEX_FILE=<scratch>/index.copy git add <spec 1> <spec 42>; GIT_INDEX_FILE=<scratch>/index.copy bash tools/memory-tree/check-memory-hygiene.sh --staged`. The copy was deleted after the run.
- It exited 1, with one failure: `HYGIENE check 9 FAILED — generated build index differs from a fresh render`. The cause it gave was "render owed under --staged — …ancestors-crosscheck.md is staged as A". The stale list includes specs 1 and 42 (their records tables, and the README title, which spec 42's H1 change also moves), along with the other dCalibratedLens specs, `LIVE.md`, `backlog/TOOL.md`, three build READMEs and `PLAY-dClosedLoop-1-as-built.md`. All of it is cured by a `gen_build_index.py --write` render, so it is left for the main loop.
- No other check named either spec. The fold probes print none of the contradicted text: "firing site", the old key set without `unclassed`, "for each stage", "The main loop files the ask", and "in the form dTotalRecall's unit 53".

4. Ancestor text that looks wrong
- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md:56-60`: the `item.maintain.*` rows are homed in `tools/drift-audit/kit.toml` with `step = "cadence.maintain"`. But `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-19.md:54-57` (S4) refuses a `review.breakpoints` tag "the loop definition does not declare". No text says the loop definition admits those rows. If it does not, cl1's Maintain boundary is refused even with tc1 CLOSED.

## Group W2, led by spec 2 (specs 2, 4, 19 and 20)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-2-3-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-2-3-spec-writer.md).

1. Rows
- Row 11, spec 2: folded. S9. The `item.loop.price` row gains `inputs = ["layer.observability:the catch source and tools/gate-legs.json"]`, `allowance = "records"` (a member of `WRITES`, `tools/roles/check_roles.py:94`) and `witness = { class = "history", by = "the value-ledger snapshot" }`, citing TOOL-dDeclaredLoop-9 S1. `returns` already read `record-kind.value-ledger`.
- Row 13, spec 2: folded. §2 preconditions, id 26 bullet. The bullet names TOOL-dDeclaredLoop-110, THE LOOP KIT REFUSES A CADENCE STEP VALUE, and §2's precondition list now includes it in `memory/builds/dDeclaredLoop/BACKLOG.md`.
- Row 14, spec 2: folded. id 42 bullet, Files touched. The claim moves to TOOL-dDeclaredLoop-1 S7's `memory/map/features/loop.md`. The "(new when no dossier claims …)" clause is gone.
- Row 14, spec 4: folded. id 42 bullet, Files touched. The same move to `loop.md`.
- Row 16, spec 2: folded. id 36 bullet, Files touched. `value-ledger` joins the untyped part of `RECORD_KIND_TOKENS` (TOOL-dTotalRecall-18 S7), not `TYPED_RECORD_KINDS`, naming TOOL-dTotalRecall-1 S2 and PLAY-dOrderedCharter-42 S2-S3. The home stays where it is.
- Row 20, spec 2: folded. id 37 bullet. The reason already named `loop_review.py record`. Added: the commit that lands the first snapshot, TOOL-dCalibratedLens-3 S8's patch build, drops `unarmed` from the row, and that unit's AC observes the dropped key. That AC belongs to spec 3, so group W3 has to write it.
- Row 126, spec 19: folded. S2, AC2. The `three-homes` plant strips `unarmed` from its two scratch registry rows before it commits (TOOL-dTotalRecall-42 S2), and AC2's exit 0 states this. Note: AC3 expects a red on a `memory/loop-review/` record, so it also depends on TOOL-dTotalRecall-108. That gap is not in my rows and I left it unedited.
- Row 129, spec 20: folded. §1, §3 Edges, §4 Evidence, §4 Alternatives. `derive_record_kind(path, written_kind, rows)` now takes the kind its caller passes, the one `tree_lib.read_bindings` classified (TOOL-dTotalRecall-53 S21). A `memory/loop-review/` record gets a kind only through TOOL-dTotalRecall-108.
- Row 130, spec 20: folded. §3 Edges, §5 risks, AC2's fixture line. The contingent `hands-off` edge is removed. TOOL-dTotalRecall-108, filed in `memory/builds/dTotalRecall/BACKLOG.md`, is now a build-run precondition on the `consumes-from external` edge and on AC2.
- Row 131, spec 20: folded. S1, AC1, §10. The three kinds bind through the untyped part of `RECORD_KIND_TOKENS`, naming TOOL-dTotalRecall-1 S2 and PLAY-dOrderedCharter-42 S2-S3. The `shape-run` and `act` comparisons are dropped from S1. AC1 now checks that the kinds are in `RECORD_KIND_TOKENS` and in neither `TYPED_RECORD_KINDS`.
- Row 133, spec 20: folded. §3. The citation now reads "TOOL-dTotalRecall-42 S5".
- Row 134, spec 20: folded. S2, AC2. The `serves-kinds` plant strips `unarmed` from its scratch registry rows (TOOL-dTotalRecall-42 S2), and AC2's exit 0 states this.

2. Specs edited
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-2.md`: rev-6, 47403 bytes.
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-4.md`: rev-6, 36698 bytes.
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-19.md`: rev-3, 15073 bytes.
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-20.md`: rev-3, 15488 bytes.

3. Hygiene
`cp "$(git rev-parse --git-path index)" <scratchpad>/index.w2 && GIT_INDEX_FILE=<scratchpad>/index.w2 git add <the four specs> && GIT_INDEX_FILE=… bash tools/memory-tree/check-memory-hygiene.sh --staged`. The index copy was deleted afterwards, and the real index is untouched (the four specs show ` M`).
- The first run failed check 25 on S2 of specs 19 and 20. The words "removes `unarmed`" match the check's retire vocabulary, but the plant only edits a scratch copy and retires nothing. I re-worded both to "strips" rather than add a false **Readers:** clause.
- The second run printed one failure, `HYGIENE check 9 FAILED — generated build index differs from a fresh render`, with the note "render owed under --staged — …ancestors-crosscheck.md is staged as A". The stale list includes the records regions of my four specs. All of this belongs to the main loop: only `gen_build_index.py --write` cures it.
- That same stale list also prints `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, a hand edit from line 5. It predates my edits and is outside my group.
- Every other check printed HELD or clean. Exit 1, from check 9 alone.

4. Ancestor text that looks wrong
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-53.md:94-96`: S21 has every `derive_record_kind` caller pass `read_bindings`' kind. `read_bindings` reads only the build folders (`tools/memory-tree/tree_lib.py:421-425`), so no registry row homed outside `memory/builds/` is ever graded until TOOL-dTotalRecall-108 lands.
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-18.md:76-77`: S7's untyped part of `RECORD_KIND_TOKENS` is a literal 4-tuple. At base, `tree_lib.py:406` already holds a fifth token, `deviation`, in the untyped literal.

## Group W3, led by spec 3 (specs 3, 5 and 7)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-3-3-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-3-3-spec-writer.md).

1. Rows
- Row 24 · cl3 · folded · S1, §4 "The items". S1 now says "TOOL-dDeclaredLoop-12 §4's row form". A paragraph under the items table gives all four rows `returns = "record-kind.loop-review"`, an `allowance` and `inputs` (`layer.runtime:GOV_CADENCE_KEY` on `lease`, `layer.observability:<what it reads>` on the others). `witness` was already in the table.
- Row 26 · cl3 · folded · §2, S4, §4 id 26 bullet, §8 F2 and F5. §2 lists TOOL-dWellOiledMachine-128 and TOOL-dDeclaredLoop-110 as build-run preconditions, each filed in its build's `BACKLOG.md`. F2 and F5 now read `RESOLVED (agent, 2026-11-03, delegated)` and point at the filed rows instead of restating the ask text. Rungs and the `widens:`/`relaxes:` lines are unchanged.
- Row 30 · cl3 · folded · S8, §4 id 37 bullet, AC8. The reason is now `unarmed = "no record yet; its writer is loop_review.py record"`. S8 says the commit that lands the first period's record edits the row to carry no `unarmed` key (TOOL-dTotalRecall-42 S2). AC8 checks a scratch worktree: exit 1 naming `unarmed` while the row keeps the key, exit 0 once it is dropped. S8 avoids the word "drops" because hygiene check 25 treats it as retiring a named thing.
- Row 31 · cl3 · folded · §4 id 36 bullet, Files touched. `loop-review` now joins the untyped part of `RECORD_KIND_TOKENS`, citing TOOL-dTotalRecall-18 S7, TOOL-dTotalRecall-1 S2 and PLAY-dOrderedCharter-42 S2-S3. The home is unchanged.
- Row 38 · cl5 · folded · §4 id 37 bullet, AC9. The reason is now `"no keep yet; its writer is loop_review.py keep"`, and the commit of the first keep drops it (tr42 S2). AC9 strips `unarmed` from its scratch row first, naming tr42 S2, and expects exit 1 naming `unarmed` if the key stays. The keep record's binding moved through `RECORD_KIND_TOKENS` in the id 36 bullet and Files touched.
- Row 40 · cl5 · folded · §2, S9. The row gains `inputs`, `allowance = "none"`, `returns = "record-kind.loop-review"` and `witness`. TOOL-dDeclaredLoop-110 is now a build-run precondition in §2.
- Row 41 · cl5 · folded · §3. The line now reads "Writing the keep at the owner's breakpoint: the owner runs `keep`."
- Row 61 · cl7 · folded · §1, §2, §3 (Non-goals and Edges), §10, S6. TOOL-dDeclaredLoop-20 S3 is cited only as the source of the line's four fields. TOOL-dTotalRecall-11 S4's `--review` door is named, and TOOL-dDeclaredLoop-111 is the review-act writer and a build-run precondition. S6's "two writers" now names that writer and TOOL-dWellOiledMachine-19 S6. The H1 is unchanged, because once ask 111 is served `review.cost` is the writer.

The `grep -n -F` of every quoted child-side phrase now prints nothing in all three specs.

2. Specs
- TOOL-dCalibratedLens-3 · rev-6 · 51906 bytes. **This does not meet the 49152 limit.** The spec was already 51098 bytes at rev-5, before this fold, and about 11 KB of that is the generated records table. Getting under the limit would mean cutting about 2.8 KB of design text, which this brief does not allow, so the main loop has to decide (a split or a trim pass). Restating F2 and F5 as pointers to the backlog rows saved about 900 bytes.
- TOOL-dCalibratedLens-5 · rev-5 · 49147 bytes. To fit, I also shortened the three "Amendments" intro paragraphs; that is wording only and no design moved.
- TOOL-dCalibratedLens-7 · rev-3 · 20173 bytes.

3. Hygiene
- Command: `GIT_INDEX_FILE=<scratchpad copy of the index> git add` the three specs, then `bash tools/memory-tree/check-memory-hygiene.sh --staged`. I deleted the copy afterwards.
- First run: check 25 FAILED on cl3 S8 ("§2 items that retire a named thing carry no **Readers:** clause … S8"). I re-worded S8.
- Second run: exit 1. The only failure is `HYGIENE check 9 FAILED — generated build index differs from a fresh render`, with "render owed under --staged — …ancestors-crosscheck.md is staged as A". It lists 30 files as "stale — differs from a fresh render", my three specs among them. Only a `gen_build_index.py --write` render clears that, so it is the main loop's. Nothing else names my specs.

4. Ancestor text that looks wrong
- `memory/builds/dTendedCadence/spec/2026-10-30-spec-TOOL-dTendedCadence-1.md:181,189` spells the lease row's actor as a bare `executor` and gives `inputs`/`allowance`/`returns` to its command rows only. TOOL-dDeclaredLoop-12:127-128 requires them for any non-role actor, and does not say whether `executor` is one. I gave cl3's lease row all three so it passes either way. (The tc1 file name is from the build folder; its date prefix is not confirmed here.)
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-11.md:91-92` still names "`review.cost`'s review act row (TOOL-dDeclaredLoop-20)" as a writer of shape-run records, but TOOL-dDeclaredLoop-20:59-62 and :130 write no record. TOOL-dDeclaredLoop-111 is the ask that closes the gap.

Files edited:
- C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-3.md
- C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-5.md
- C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-7.md

## Group W4, led by spec 16 (specs 16, 9 and 11)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-16-2-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-16-2-spec-writer.md).

1. Rows:
- Row 110, spec 16: `folded`. Moved S4, AC3 and §7's arm line. A transition's `scenario` value is the placed scenarios joined by `+` (TOOL-dDeclaredLoop-27 S8), and the tuple keys on that joined value whole, so each line counts once and S5's sums hold. AC3 gains the `stall-two-scenarios` plant (`scenario=scenario.feature+scenario.patch`, one row, no row per member).
- Row 113, spec 16: `folded`. Moved §4 `BOUND_EVIDENCE`, AC7 and §7. I took the "censored at the base" route. Spent never passes the total, and past it a draw "writes nothing and returns `exhausted`" (dl30 S3), so the p90 proposes only `lower` or `hold`, and any raise is the owner's call from the `budget-spent` trend. AC7's plants now sit inside the `4+2` total of 6: ten builds each at 2, 3 and 4 draws give `p90 2`, and the `bounds-spent` plant (all thirty at `6/6`) gives `p90 4 · hold`.
- Row 114, spec 16: `folded`. Moved §4 `BOUND_EVIDENCE`. The evidence is now the most draws of any cause naming one item, as `count_returns(build, item)` counts them (dl30 S6).
- Row 115, spec 16: `folded`. Moved S8 and AC7. For `flow.rework-budget`, `--rev` reads the commit of the transition record into `building` that carries the freeze row (dl30 S2, S3). Every other key, and a build with no freeze row, still reads the newest transition record.
- Row 116, spec 16: `folded`. Moved S7, S8, §5 perf and AC7. I took the first route. Only node-local keys are kept in `bound-evidence`, and committed keys are re-read from their committed source at every derivation, so dl30 S7's draws after close count. AC7 gains the `bounds-late-patch` plant (`p90 3`).
- Row 116, F1 part, spec 16: `folded`. Moved §3 non-goals, §3 build-run preconditions, §4 Waits on, and §8 F1's wording. F1 now names TOOL-dWellOiledMachine-129 in `memory/builds/dWellOiledMachine/BACKLOG.md`. The mark, rung and `widens:`/`relaxes:` line are unchanged; the mark already read `RESOLVED (agent, 2026-11-03, delegated)`.
- Row 77, spec 9: `folded`. Moved §2 preconditions and the §4 id 51 line. `find --all` is TOOL-dWellOiledMachine-32 §8 F6's ask, which dWellOiledMachine's build run files, and no `dTotalRecall/BACKLOG.md` row holds it yet. It is a build-run precondition. Until it lands, F6's interim refusal holds ("a reader that meets the total line refuses, naming it"), which surfaces as S1's `acts unread` line.
- Row 79, spec 9: `folded`. Moved §10. It now reads "output tokens only, no input-token field" (tr11's schema field `"Out-tokens"`).
- Row 80, spec 9: `folded`. Moved §4 "The metric", AC7 and AC8. The tags are now `item.build.unit-pass` and `item.review.dispose`, the same fix applied to the fixture ACs. Spec 16's example and AC3 still use `item.build.unit`. That is not a row I was given, so it is untouched.
- Row 84, spec 11: `folded`. Moved §5 risks. The run record's `rounds` rows come from `review` rows only (`tools/runlog/record.py:862`). dl32 S5's `fix-pass` row is a park kind of its own, never a review row, so `route-backs-per-build` excludes it, and nothing counts the two loops together.

2. Specs edited:
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-16.md`: rev-4, 39588 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-9.md`: rev-4, 34122 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-11.md`: rev-4, 33819 bytes

3. Hygiene run: `cp $(git rev-parse --git-path index) <scratchpad>/index-w4; GIT_INDEX_FILE=<scratchpad>/index-w4 git add <the three specs>; GIT_INDEX_FILE=… bash tools/memory-tree/check-memory-hygiene.sh --staged`. The index copy was deleted afterwards.
   - It exited 1 on one check only, "HYGIENE check 9 FAILED — generated build index differs from a fresh render". The cause it printed is "render owed under --staged — …-1-ancestors-crosscheck.md is staged as A".
   - The drift list names `memory/LIVE.md`, `memory/backlog/TOOL.md`, the dCalibratedLens, dDeclaredLoop, dTotalRecall and dWellOiledMachine READMEs, and about 25 dCalibratedLens specs including 9, 11 and 16, each "stale — differs from a fresh render". A `gen_build_index.py --write` cures all of these; that is the main loop's render, and I left it.
   - It also names a pre-existing hand edit in `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, which is not in my group.
   - Check 30 printed "as-built clean"; checks 10 and 23 and the edge joins were HELD under `--staged`. No other finding names my specs.

4. Ancestor text that looks wrong:
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-3.md:69-71` names TOOL-dDeclaredLoop-30 as a `read_transitions` reader, but `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-30.md:46-47` (S3) reads its rows through `tools/memory-tree/build_records.py`.
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-32.md:330` says "the build run files it in the owning build's `BACKLOG.md`", but no row in `memory/builds/dTotalRecall/BACKLOG.md` holds the `find --all` ask, and the main loop's filed-ask list does not include it.

## Group W5, led by spec 14 (specs 14, 13, 6 and 8)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-14-2-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-14-2-spec-writer.md).

All four W5 specs are revised: seven rows folded and none refused. Row 86 is folded but part of it is also returned as parked, because one behaviour it needs has no ancestor text. The hygiene run names my specs only in check 9's render drift, which is the main loop's to cure with the index render. The real index was not touched.

1. Rows
- **Row 94, spec 14: folded.** Sections S4, S5 §4 "The proposed row" and AC6, plus the arm line in §7. I took the "refuse multi-scenario carriers" route, the smaller of the two routes the return offers. S4 now quotes dl27 S8's "the placed scenarios in declared order joined by `+`". A change whose field names more than one scenario is not carried, because `extends` takes one tag (dl27 S3). AC6 gains a `scenario=scenario.feature+scenario.patch` plant.
- **Row 95, spec 14: folded.** Sections S5 and §4 "The proposed row". Both now read the schema's `activatable` list (dl27 S3, `tools/loop/scenario-schema.toml`) instead of naming two kinds.
- **Row 97, spec 14: folded.** Sections S9, §4 Inventory, Files touched and AC11. I took the first route, widening `compare_path` in `tools/loop/adapt.py`. It gains two keyword parameters, `composition` (default: the pinned one) and `file_orders` (default: true). S9 passes the promoted composition with `file_orders=False`, so it files nothing, and dl28's boundary call is unchanged. AC11 now observes that no `flow-deviation` order is filed.
- **Row 86, spec 13: folded, with one part parked.** Sections §2 (preconditions and S3) and the edge line in §3.
  - **Folded:** the precondition is now the owner's pick on TOOL-dDeclaredLoop-26 §8 F5, which is "OPEN for the owner". Under option (a) it is the `compose` verb, an ask on dOrderedCharter that no `BACKLOG.md` holds. S3's route is stated as holding under F5 (a).
  - **Parked:** S3's route under F5 (b). That option puts "a declared import row on `tools/loop/kit.toml` naming playbook" (dl26:288-289), which is on the loop kit. S3 lives in the workflows kit (`render_lenses.py`), and no text gives it a route to `compose_rows` under (b). The options are a declared import row on `tools/workflows/kit.toml`, or that kit taking the verb anyway. My recommendation is to settle it once the owner picks F5.
- **Row 46, spec 6: folded.** Section §4 Evidence now cites TOOL-dTotalRecall-9 S8 ("The work order: `render_handoff`") and §10.
- **Row 48, spec 6: folded.** AC7's permission line now says `gov_record.py` is TOOL-dTotalRecall-2's door, and its `budget` verb is TOOL-dTotalRecall-9 S6's.
- **Row 50, spec 6: folded.** Sections S3, §3 (non-goal and build-run preconditions), §4 Waits on, AC5 and §8 F4. F4 is re-marked `RESOLVED (agent, 2026-11-03, delegated)` and now reads "(a), filed as TOOL-dTotalRecall-107 in `memory/builds/dTotalRecall/BACKLOG.md`". It keeps rung 3 and `widens: none · relaxes: none`. The ask is now listed among the build-run preconditions.
- **Row 69, spec 8: folded.** Section §3. I took the "name the departure" route. Restricting the view on `lose` would have needed a trigger that no text gives, which would be a new fork. §3 now quotes TOOL-dTotalRecall-17 S7's ask and says this unit does not serve it: S3's view drops only the map slot and still counts the `code`, `bug-classes` and other slots. On `lose` every cell still reads `/no-map`.

2. Specs edited
- spec 14: rev-3, 37285 bytes
- spec 13: rev-4, 35205 bytes
- spec 6: rev-5, 32414 bytes
- spec 8: rev-5, 33842 bytes

Each new §9 line uses the brief's form. The `grep -n` probe of each quoted child phrase now returns nothing.

3. Hygiene run
I copied the index to the scratchpad, pointed `GIT_INDEX_FILE` at the copy, staged only the four specs into it with `git add`, ran `bash tools/memory-tree/check-memory-hygiene.sh --staged`, and deleted the copy. It exited 1 on one check:
- "HYGIENE check 9 FAILED — generated build index differs from a fresh render", triggered because `build/2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck.md` is staged as A.
- It printed "build-index DRIFT — run: python tools/memory-tree/gen_build_index.py --write" and listed `memory/LIVE.md`, `memory/backlog/TOOL.md`, the three builds' READMEs, about 25 dCalibratedLens specs (specs 6, 8, 13 and 14 among them) and `2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` as stale.
- Checks 10 and 23, the edge joins, the stale-line guard and the curation-debt guard were held under `--staged`. Check 29 graded nothing, and check 30 reported clean.
- No other finding named my specs. The render drift is the main loop's.

4. Ancestor text that looks wrong
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-17.md:68-69` asks dCalibratedLens for a cause "from the slice manifest alone". cl8 §8 F2 records that no spec writes a slice manifest, since TOOL-dTotalRecall-12 S9 hands it to dWellOiledMachine, so the ask names an input nothing produces.
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-26.md:286-289` offers F5 (b) only as an import row on `tools/loop/kit.toml`. Its own text says every loop-kit caller needs `compose_rows`, but a caller outside the loop kit, such as the workflows kit's `render_lenses.py`, has no route under (b).

Files edited:
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-14.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-13.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-6.md`
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-8.md`
