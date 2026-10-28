**Serves:** research TOOL-dRankedPlan-1

# dRankedPlan — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns of the re-ground brief [`2026-10-28-prompt-TOOL-dRankedPlan-1-parents-reground`](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-reground.md), each copied from its agent transcript by script; only the headings are the main loop's, each returned heading demoted two levels. Group A's writer was resumed once: its first pass spelled the typed kinds' writer cell with a `new` verb no parent claims.

## Group A, specs 1, 2, 3, 4, 9, 15, 16 and 24

All eight Group A specs are revised for the record rows they answer. No row was refused. All eight stay `DEFERRED` and are dated 2026-10-28, and each has one new §9 line naming the record and its rows. No spec is above 35,443 bytes, well under the 49,152 cap.

The hygiene gate ran over a copy of the index with only these eight specs staged. The only red was check 9, the build-index render owed (`gen_build_index.py --write`), which is yours to run. Its other lines name these specs only as check 25 notes ("did not grade … READER NOT IN TREE covers it"), not findings. I deleted the index copy. The quoted sentences for every row are gone, or only the corrected sentence remains.

##### Per spec

| Spec | Rev | Sections moved | Rows | Bytes |
|---|---|---|---|---|
| rp1 | rev-3 | S6 · §3 · §4 · §10 | 3 | 24,871 |
| rp2 | rev-3 | S1 · S3 · AC1 · §3 · §4 · §10 | 6, 7, 8 | 31,590 |
| rp3 | rev-3 | S5 · S6 · S7 · §3 · §10 | 12, 15, plus your S6 note | 35,443 |
| rp4 | rev-5 | S3 | 18 | 21,416 |
| rp9 | rev-4 | S1 · S4 · S5 · §3 · §4 · §8 · §10 | 21, 22 | 25,349 |
| rp15 | rev-4 | S2 · S5 · S6 · AC10 · §3 · §4 · §5 · §8 · §10 | 34, 38 | 30,105 |
| rp16 | rev-5 | S1 | 39 | 31,649 |
| rp24 | rev-3 | S1 · S4 · §3 · §4 · §5 · §10 | 48, 49 | 14,206 |

What changed, per spec:
- **rp1:** `plan.unplaced` is now read through the memory-tree adapter `read_policy_value` (tr8 S10). A refusal or a missing policy kit reads `warn` and prints the refusal once. The `read_slot_mode` precedent is gone from S6, Evidence and §10.
- **rp2:**
  - The planner's limits leave the body. They become three `never` entries, one per `plan.authority` value, each `— gen_build_index.py --ratified-order`, shown in a fenced block in §4.
  - The body keeps only the job.
  - AC1 now greps the rendered `## Never` section and requires `check_roles.py` to name no R5 or R13 line.
  - `plan.authority` is read through `read_policy_value`.
  - `item.plan.research` reads the `S` rows of `gen_build_index.py --print-bindings` by subprocess (verified at `gen_build_index.py:690`, `:770`).
- **rp3:**
  - The `triage` and `dupes` writers are now `build_records.py new <kind> --build --unit --field`. `gov_record.py new <kind>` stays the door call.
  - `plan_items.py` runs that door by subprocess.
  - The `Rows` key is memory-tree's own `derive_content_key` (tr2 S5).
  - Your note 1: S6 now runs `ratify.py <home>` as a subprocess argv list found through `backlog.resolve_kit_dir`, matching rp22 S1. The §9 line marks it "(writer-found, not a record row)".
- **rp4 and rp24, the life-item choice:** I picked the second option. rp24 S1 keeps the `check_disposition_record` filter only for an item whose `read_outcome_set` answers a set. Records for an item with no `[[item]]` row pass with no value filter. rp4 S3 then grades them by `DISPOSAL_MOVES`, and S4's `derive_move` refusal holds the rest.
  - Why: dl16:59-61 makes the check admit nothing, "never green", for an item the loop definition does not declare. dl13:234-235 says `item.life.request` and `item.life.close` have no row.
  - The other option would put a second value check, against the move tables, inside a reader whose admission rule dl16 S5 owns. rp4 already holds the three moves and the `derive_move` refusal.
  - Both specs say this, and rp24 §4 records the rejected option.
- **rp24, row 49:** records are found with `gov_record.py find --kind disposition --build <slug>` and read with `show` (tr9 S3, S5), by subprocess. A non-zero exit, or `find`'s 40-row total line, raises. §5 marks as UNVERIFIED whether `find`'s index sees a newly committed record.
- **rp9:** `plan.ratification` is read by a new `read_policy_value` in `ratify.py`, built to the oc7 §4 contract (bounded `policy.py get` subprocess, `PolicyRefused` on exit 2). The coverage question is answered from `READER_SHAPES` (`check_policy.py:423-427`): a call with the key literal first counts, an argv list does not. S4 reads records through `find` and `show`, and S5 reaches the plan record through the verb F6 settles.
- **rp15:**
  - The leg `loop plan revision` is declared once as a `[[gate_leg]]` in `tools/loop/kit.toml`, with every manifest key including `enforces`, and rendered with `leg_factory.py`.
  - `tools/run-gates/leg_factory.py` is not in the tree, so the spec says the pass hand-writes the declaration and manifest row as a stand-in.
  - Files touched lists `tools/gate-legs.json` as rendered, not edited. New AC10 reads `leg_factory.py --check` and the declaration through `tomllib`.
  - The plan record is reached through rp9 F6's verb. The `from` comparison now compares lines above `## Revisions` with no `FIELD` parse.
- **rp16:** the S1 writer is now `"build_records.py new plan --build --unit --field"`. S3's `gov_record.py new plan` stays.

##### Forks added (none re-resolved)
- **rp9 F6, open for the owner:** which memory-tree verb `ratify.py` uses to find the plan record. Options:
  - (a) ask TOOL-dRankedPlan-16 for `plan_record.py path <slug>`;
  - (b) use `gov_record.py find --kind plan`;
  - (c) declare a `requires_if` row.
  I recommend (a). rp15 cites this fork rather than opening a second.
- **rp15 F8, open for the owner:** which `enforces` tag the leg carries. Clause `cl-dClosedLoop-0497` has no `[enforcement]` row. Options are `principle.p20`, `p2` or `p35`. I recommend `principle.p20`, as dl3 F7 does.
- **Your note 2:** the leg declaration is rp15 S6 and its `enforces` fork is F8, so rp29 S26's pointer is right as written.

##### Possible parent or cross-group issues
- **dl3 S4** reads `transitions.record` through an in-process `resolve(...)` from the loop kit. That is the same in-process read oc7:202-205 rules out.
- **rp3 S2** reads `plan.triage` by spelling `policy.py get plan.triage` inside Python. That shape is invisible to the reader-coverage row for `.py` files, and it bypasses memory-tree's `read_policy_value`. Row 16 marked it AGREES, so I left it alone. rp29 S6 to S8 also edit that read.
- **rp1 S3** still names `find_plan_record` in memory-tree. That is the same kit, so it is fine as written.

Specs are in `C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\`:
- 2026-10-26-spec-TOOL-dRankedPlan-1.md
- 2026-10-26-spec-TOOL-dRankedPlan-2.md
- 2026-10-26-spec-TOOL-dRankedPlan-3.md
- 2026-10-26-spec-TOOL-dRankedPlan-4.md
- 2026-10-26-spec-TOOL-dRankedPlan-9.md
- 2026-10-26-spec-TOOL-dRankedPlan-15.md
- 2026-10-26-spec-TOOL-dRankedPlan-16.md
- 2026-10-26-spec-TOOL-dRankedPlan-24.md

## Group B, specs 13, 21, 22, 29, 31, 37 and 45

I revised all seven Group B specs for the rows the record names, and refused none. Each is under 49152 bytes and still DEFERRED, with a new §9 line naming the record and its rows.

The hygiene gate, run over an index copy with only these seven specs staged, has one red: check 9, the generated build index differs from a fresh render. A `gen_build_index.py --write` render cures that, so it is yours. I deleted the index copy and the `rp-wB/` scratch folder. For every row, the `grep` for the old sentence prints nothing or only the corrected sentence. I did not run the naming lexicon, since no new names were minted.

`tools/run-gates/leg_factory.py` is not in the tree. Every leg spec says the pass hand-writes the manifest row as a stand-in and its deviation record names it. Each new acceptance criterion carries a `fixture:` line saying what it reads until TOOL-dWitnessedBar-11 lands.

| Spec | Rev | Rows | Sections moved | Bytes |
|---|---|---|---|---|
| TOOL-dRankedPlan-13 | rev-4 | 31 | §2 S10 · §3 Edges · §4 Files touched · §6 AC11 (new) · §9 | 29858 |
| TOOL-dRankedPlan-21 | rev-3 | 45 | §2 S1, S3, S4 · §3 Edges · §4 Evidence, Alternatives rejected · §5 · §6 AC1, AC3 · §8 F3 · §9 · §10 | 17451 |
| TOOL-dRankedPlan-22 | rev-3 | 47 | §2 S1, S2, S3 · §4 Evidence · §6 AC1 · §9 | 14374 |
| TOOL-dRankedPlan-29 | rev-3 | 54, 55 | §2 S25, S26 · §4 Files touched · §6 AC20 · §9 | 42273 |
| TOOL-dRankedPlan-31 | rev-3 | 57 | §2 S1, S2 · §4 Evidence, Files touched · §6 AC1 · §8 F1 · §9 · §10 | 13673 |
| TOOL-dRankedPlan-37 | rev-4 | 60, 61 | §2 S1, S13, S17 · §4 Evidence, Files touched · §6 AC11 · §9 | 34725 |
| TOOL-dRankedPlan-45 | rev-3 | 63 | §2 S6, S7, S18 · §4 Evidence, Files touched · §6 AC5, AC13 · §9 | 35161 |

What each now says:
- **rp13:** the `plan-fields selftest` leg is declared once in `tools/memory-tree/kit.toml` with `enforces = ["principle.p32"]`, and the manifest is rendered from it. AC11 greps the declaration and runs `leg_factory.py --check`.
- **rp29:** S25 puts `chunk` and `ceiling` on that declaration. S26 points at rp15 S6's declaration and its §8 F8 tag, as rp15 now reads. AC20 reads both descriptors.
- **rp31:** the leg's `chunk`, `ceiling` and `enforces` are all on its `[[gate_leg]]` row, and there is no separately written manifest row.
- **rp45:** S6 and S18 edit only the declarations. S7 adds `gate-leg conformance` and `core meta-check`. AC5 now checks the new leg's `enforces`.
- **rp37 S13:** guards widen only in each leg's declaration, using `[gate_leg.gov]` where gov differs, and S4's plant "runs" `ratify.py` rather than importing it.
- **rp21:** the generator runs `ratify.py <slug> --exited` as a subprocess with a timeout and imports nothing from the loop kit.
  - What a failed run does: exit 2 (unknown slug) reads as not crossed. Any other failure exits the check 2, naming the build, so a broken reader never makes a row unratified.
  - `read_slot_mode` is no longer cited as the route.
  - AC3 adds a grep that the generator imports no loop-kit module.
- **rp37 S1 and S17:** the generator's plant runs `ratify.py --fixture --seed` and `loop_transition.py record`. S17's ratified set is read through the verdict on `--exited`'s line.
- **rp22:** `triage.py` asks by running `ratify.py <home>` as a subprocess. S2 counts that argv-list form as a caller, and the plant shows it admitted in `triage.py` and refused in `gen_build_index.py`.

**Forks:**
- **rp21 F3, added, `RESOLVED (agent, 2026-10-28, delegated)`, rung 1.** The generator can't import `RATIFYING_EXITS`, so `--exited`'s line now ends with a verdict, `ratifying` or `not ratifying`. The alternatives were a copy of the set in memory-tree, which breaks `[one-fact]`, or a `requires_if` import, which oc7 §4 rules out because the verb exists. rp37 S17 relies on this verdict.
- **rp31 F1, added, open for the owner.** It asks which principle the `session-predicate callers` leg enforces: `principle.p2`, `p22` or `p23`. I recommend `principle.p2`: the ban refuses an answer taken from session state after the act. No other spec of this build had a fork on this leg.

**Problems I found but did not edit:**
- **rp3 S6** (Group A, `rp3:81`) still says `triage.py ratify` "calls `read_plan_ratification(<home>)`". That is memory-tree calling the loop kit in process, and no record row covers it. rp22 S1 now says `triage.py` runs `ratify.py <home>` as a subprocess, so rp3 S6 needs the same re-spelling, by Group A or as a follow-up.
- **rp32 `RATIFY_MODE_FLAGS`** already includes `--exited` (`rp32:65`), so rp21's new subprocess call is not counted as a caller. That fits the design; I note it only because the two depend on each other.
- **No parent spec looks wrong.** wb11 S1 to S4, oc7 S3, S11 and §4, and dl3 S5 bear out every row as quoted.

The seven files are in `C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\`:
- 2026-10-26-spec-TOOL-dRankedPlan-13.md
- 2026-10-26-spec-TOOL-dRankedPlan-21.md
- 2026-10-26-spec-TOOL-dRankedPlan-22.md
- 2026-10-26-spec-TOOL-dRankedPlan-29.md
- 2026-10-27-spec-TOOL-dRankedPlan-31.md
- 2026-10-27-spec-TOOL-dRankedPlan-37.md
- 2026-10-27-spec-TOOL-dRankedPlan-45.md

## Group A, resumed: the factory writer cell re-spelled in rp3 and rp16

The three writer cells in rp3 and rp16 now use tr1:167's form, and no `build_records.py new` is left in any of my eight specs.

**Lines changed**
- **rp3:73 (S5):** the writer is now `build_records.py --build <slug> --unit <id> <triage's field flags>`, "in the form of the `deviation` row's writer (TOOL-dTotalRecall-1 §4)".
- **rp3:94-95 (S7):** the writer is now `build_records.py --build <slug> --unit <id> <dupes's field flags>`, "as S5's".
- **rp16:35-36 (S1):** the flag is now `--writer "build_records.py --build <slug> --unit <id> <plan's field flags>"`.
- **rp3 §9, the same rev-3 line extended:** "S5 and S7 spell the writer cell in the `deviation` row's form, with no `new`, since no parent claims a generic `new` verb on the factory (TOOL-dTotalRecall-1 §4)."
- **rp16 §9, the same rev-5 line extended:** "…the cell spelled in the `deviation` row's form with no `new`, since no parent claims a generic `new` verb on the factory (TOOL-dTotalRecall-1 §4)…"

I kept each kind's flags as a named placeholder, like tr1:167's `<deviation's field flags>`, rather than writing every flag out. I also reworded both §9 lines so they don't quote the old string; otherwise the check for `build_records.py new` would have matched them.

**Byte counts and revs**
- rp3: 35,703 bytes, still rev-3.
- rp16: 31,817 bytes, still rev-5.

**Hygiene check:** I re-ran it over an index copy with only rp3 and rp16 staged. The only failure is check 9, the build-index render that `gen_build_index.py --write` fixes, which is yours to run. The other lines naming these specs are check 25 notes ("did not grade … READER NOT IN TREE covers it"), not findings. I deleted the index copy.

rp3:95 now runs past the ~100-column wrap, and rp16:36 already did before this change; neither affects the gate.

Files:
- C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-3.md
- C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-16.md
