**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46

# dCalibratedLens — the parents re-ground writers' returns, verbatim

The five `gov-spec-writer` returns that fold the cross-check record [`2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck`](2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md), extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md); each group's handoff sits beside it.

## Group W1, led by spec 1 (specs 1, 13, 24 and 30)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-1-3-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-3-spec-writer.md).

1. Rows

- **Row 4, cl1: folded.** §2 S1 (`PRESETS` now also holds `whole-design`, by TOOL-dFairHearing-18 S1), the §2 build-run precondition, §3 Edges, §4 "Waits on", §4 Evidence, §4 id 16, §5 risks and AC3. The receiver now has eight literals. TOOL-dFairHearing-16, -18 and -23 are added to the preconditions and to "Waits on".
- **Row 6, cl1: folded.** §2 S2 (new rows are appended after the catalogue's last row) and §4 "The rows". The slots are renumbered to file order: drawn rows first, in fh2's order (`coherence`, `grounding`, `failure-envelope`), then the new rows. AC1's "in slot order" holds again.
- **Row 9, cl1: parked.** Not edited. The deciding line is `tools/workflows/kit.toml:10`, `requires = ["agent-cap", "policy"]`. `REVIEW_STAGES` lives in `roles_lib.py`, in the roles kit, and the review-harness kit does not require roles. `tools/roles/kit.toml:19` already makes roles `requires_if` review-harness. So for `review_pin.py` to admit only `REVIEW_STAGES` members, a kit edge or a second home has to be chosen. That is a new fork. Options:
  - (a) `review_pin.py` imports `REVIEW_STAGES` from `roles_lib.py`, and review-harness's `requires` gains `roles`, so the two kits name each other.
  - (b) `REVIEW_STAGES` moves to `review_pin.py` as its one home. `roles_lib.py` reaches it through the inline `resolve_kit_dir`, along the existing roles → review-harness edge.
  - (c) `review_pin.py` keeps its own copy of the stage set, with a parity arm against `REVIEW_STAGES`.

  Recommendation: (b), because it follows the edge that already exists.
- **Row 10, cl1: folded.** §2 S3 and §3 Edges. `read_lens_literals` now runs `render_lenses.py --markers` (TOOL-dFairHearing-23 S35) and reads the literal name from each `gov:lens-slots <literal>` line that command numbers.
- **Row 13, cl1: folded.** §4 id 43. Only rp6 AC1's arm flips. rp6 AC3's arm passes `preset: unit-spec` itself, so it is untouched unless it is rewired. rp6 AC4 is a probe, not an arm, and reads red once the Plan literal lands.
- **Row 16, cl1: folded.** §2 S4 and AC6. Step 1a is now one `read_policy_setting` call per stage, each with its key spelled as a literal (TOOL-dIndexedDesign-3 S5), so id3 AC7's first grep still prints 1. AC6 adds `grep -cE 'read_policy_setting\("review\.[a-z]+\.effort"' tools/roles/roles_lib.py` → 6.
- **Row 17, cl1: folded.** §4 Evidence, §4 id 16, §4 r2 id 15, the §3 hands-off to cl24, and AC3. AC3 now runs `node tools/workflows/check-verifier-fanout.js --hook tools/hooks/agent-cap.js tools/workflows/tier2-review.js` and expects exit 0 (fh16 S2, AC2).
- **Row 115, cl13: folded.** The §2 preconditions, S4, §3 Edges, §4 "The schema" and its prose. `LENS_SLOTS` is now cited at `tools/workflows/check-verifier-fanout.js#LENS_SLOTS` (TOOL-dFairHearing-23 S42), and -23 is a precondition.
- **Row 116, cl13: folded.** §2 S1, S2 and S6, AC1 and AC7.
  - A tag now addresses every row of its key, and `members` prints each tag once.
  - S6's plant now picks a row whose key no other row holds; otherwise no tag vanishes and AC6 cannot go red.
  - AC1 and AC7 now count distinct keys.
- **Row 156, cl24: folded.** Title, §1, §2 S1 to S3, §3, §4 Evidence and "The observation", §5, AC1 to AC3, §7's `New arm:` line and §10.
  - The observation and the red twin now run through `check-verifier-fanout.js --hook`, and the looped copy expects exit 1.
  - fh16 S2 and S5 are named as the reason the base deny at `agent-cap.js:1940-1943` / `agent-cap.test.sh:2325` does not survive.
  - AC1's grep now looks for `AC3.*check-verifier-fanout.js --hook` in cl1.
  - AC3's witness is now `boundedParallel(PLAN_LENSES.map((f) => () => agent(f)), 5)`. Hygiene check 12 needs a backticked witness, and the checker's exact deny text is not known until it is built.
- **Row 162, cl30: folded.** §2 S25 now names the one rp6 arm that flips (its AC1's), beside its AC3 arm, which is untouched, and its AC4 probe, which reads red. Row 13's fold made the "three arms" wording false, so cl30 could not stay as it was.

2. Specs

- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-1.md`: rev-4, 40028 bytes
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-13.md`: rev-3, 30741 bytes
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-24.md`: rev-3, 10391 bytes
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-30.md`: rev-3, 27263 bytes

3. Hygiene

The command, run over a copy of the index (deleted after):
`cp "$(git rev-parse --git-path index)" "$IDX" && GIT_INDEX_FILE="$IDX" git add <specs 1, 13, 24, 30> && GIT_INDEX_FILE="$IDX" bash tools/memory-tree/check-memory-hygiene.sh --staged`

- **First run:** check 12 named cl24 AC3 ("acceptance bullets naming no backticked witness"). I fixed it.
- **Final run: exit 1.** The only remaining failure is check 9, "generated build index differs from a fresh render … `memory/builds/dCalibratedLens/README.md` (stale)". That one is cured by `gen_build_index.py --write` and belongs to the main loop. cl24's title change is part of what that render will pick up.
- **Held checks:** 10, 23, the edge joins and the stale-line guards were held under `--staged`.
- **Specs named:** none of the four.

4. Parent text that looks wrong

- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md:204`: calls `LENS_SLOTS=5` in `check-verifier-fanout.sh` "its one home", while `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md:174-175` gives that home to `check-verifier-fanout.js`.
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md:207` vs `:294-295`: they disagree on whether the `slots` line names the marked literals.
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-2.md:92-95`: records an `agent-cap.js --only=scripts` measurement with no payload named. A bare run exits 0 without reading any harness.
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md:153-156` (S35): `--markers` prints line numbers only, so every caller that needs literal names has to re-read the lines it numbers.
- `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-3.md:295`: says the reader-coverage shapes "cannot see" a key built from a variable. But `tools/policy/check_policy.py:428-429` admits an `f`-prefixed literal, so `f"review.{stage}.effort"` would be matched.
- `memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-6.md:213`: declares no suite arm for AC4 (`:199-204`), yet AC4's "Red when" reads like an arm's.
- `tools/hooks/agent-cap.test.sh:2325` (a base file, not a spec): this arm asserting rule 2's deny under `--only=scripts` sits under rule 6's S11. fh16 S5 (`2026-10-23-spec-TOOL-dFairHearing-16.md:64-67`) moves only "the arms … over rules 0, 2 and 5", so it is not clear which unit moves or flips this one.

## Group W2, led by spec 10 (specs 10, 23 and 36)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-10-2-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-10-2-spec-writer.md).

All 13 rows in Group W2 are folded; none refused or parked. The three specs are edited, and every row's probe of the quoted child-side text now comes back clean. The hygiene run fails only on check 9, the build-index render, which belongs to the main loop.

1. Rows
- **Row 91, spec 10:** folded. §2 S1, §4 Inventory, §7 `New arm:`. The instance's plants are arms of `replay_scorer.run_selftest`, reached through `review-replay selftest` (fh12 F3). The `New arm:` line's last field now reads "that runner's `ARMS_DECLARED`, raised by the five arms added". Of the return's two routes I took the first, which is also the smaller: `--fixture` and `--plant <name>` are minted in the Inventory, and `--plant` runs one named arm. So the AC commands and spec 36's hands-off text stay as they were.
- **Row 92, spec 10:** folded. §2 preconditions, S1, §3 external edge, §4 Waits on. `case_evidence(case)` (TOOL-dFairHearing-14 S2) is the case's `**Subject:**` at `**Base:**` plus its known rows' addresses, and a case missing either is refused by id.
- **Row 94, spec 10:** folded. S6, S7, §4 "The case" example, §4 "A case from a finding", AC7. I took the first route, scoping cases to tagged refs. A finding whose `ref` carries no `[tag]` is refused, citing fh12 S3 and fh1 S3. S7 proposes only findings with a tagged ref. The example address is now `:[recall-probe]`, and AC7 adds a refusal for "finding 10".
- **Row 95, spec 10:** folded. S2. `n` is now defined as the rows whose `escaped` is `no` (the `**Population:**` line's `reviewed` figure), with `k` counted among them, as fh1 S3 prints `reviewed <k>/59`. I chose 59 over 65 because it is the smaller change and matches fh25's figures. The `0/59` literal stays because it now agrees, so a `grep` for `0/59` still finds it; what has gone is the undefined `n`.
- **Row 96, spec 10:** folded. S5. The seed takes the lower of the two runs, `fhr1` on a tie, and that run's report is the `<candidate src>`. The reason: fh25 S5 flips the switch only "when both runs meet spec 1's bar", and spec 10's `fell` rule would red on run-to-run noise if the baseline were the higher run. This is my derivation, not something the parent says outright, so the reviewer should check it; the other choice would be one seed per run. The existing sentence citing "the reviewed score TOOL-dFairHearing-25's verdict record states" stays, because the new sentence after it says which run.
- **Row 97, spec 10:** folded. S5. `**Replayed:**` carries the orchestrating commit (TOOL-dFairHearing-32 S14). `**Base:**` is `6cfd21619e9cbe6084dd9d38982194750aa908b2`, with the placement commit made by the README step (fh32 S18).
- **Row 98, spec 10:** folded. S8. The replay procedure now points to the README's "Replaying a review blind" section (fh23 S17, fh32 S17 and S18) instead of fh1 S5.
- **Row 102, spec 10:** folded. S4, §4 Evidence, Files touched. The leg is one whole `[[exempt_leg]]` row under wb11 S1, as tc7 S4 declares its leg. It is appended by `leg_factory.py new --exempt <why>` (wb11 S3), and `gate-legs.json` is its render through `leg_factory.py --write`. The "form `tier2-review self-test`'s takes" wording is gone.
- **Row 152, spec 23:** folded. S1, AC2 fixture line. The seed's score is the lower run's `reviewed <k>/59` at the orchestrating commit. §10's "taken from TOOL-dFairHearing-25's verdict record" stays true and is not edited.
- **Row 153, spec 23:** folded. S2, §4 Evidence. The replayed sha is the orchestrating commit. A new bullet lists the parent edits to `tier2-review.template.js` after fh25: fh27 (21, :227), fh30 (21, :117), fh35 (22, :144), fh32 (23, :258), fh37 (24, :186) and fh40 (26, :316). A scan found no parent unit after order 20 that names another of the seed's loads.
- **Row 154, spec 23:** folded. S3, §7 `New arm:`. `close-bar` is an arm of `replay_scorer.run_selftest`, raising `ARMS_DECLARED` by one.
- **Row 164, spec 36:** folded. §1, S1, §4 Evidence. The replayed sha is the orchestrating commit (fh32 S14), and S1 and §4 now count the parent template edits after fh25.
- **Row 165, spec 36:** folded. S2, §7 `New arm:`. `seed-loads` is an arm of `replay_scorer.run_selftest`, raising `ARMS_DECLARED` by one.

2. Specs edited
- spec 10: rev-5, 37670 bytes
- spec 23: rev-4, 14426 bytes
- spec 36: rev-3, 13078 bytes

3. Hygiene run
I copied the index to the scratchpad, pointed `GIT_INDEX_FILE` at the copy, ran `git add` on specs 10, 23 and 36, then ran `bash tools/memory-tree/check-memory-hygiene.sh --staged`. It exited 1 and printed:
```
HYGIENE check 9 FAILED — generated build index differs from a fresh render:
build-index: render owed under --staged — memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-10.md is a build-index input or output
build-index DRIFT — run: python tools/memory-tree/gen_build_index.py --write
    memory/builds/dCalibratedLens/README.md (stale — differs from a fresh render)
    memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-16.md (stale — differs from a fresh render)
```
Everything else was HELD under `--staged` or clean (check 30 as-built clean). The only finding is the build-index render, which only `gen_build_index.py --write` cures, so it is left for the main loop. The index copy is deleted.

4. Parent text that looks wrong
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md:136-139` still gives `git clone --branch fh-base "$TEMP/fhb/h.bundle"` as the isolation recipe. fh25:26-27 says this step exits 128, and only fh23 S17 and fh25 correct it.
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md:63-66` (S6) still names "the commit the runs started from". fh32:82-90 (S14) supersedes this from outside.
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-14.md:43-44` (S2) still gives review-replay's `case_evidence` as "the known item's ref and the record it came from". fh32:69-72 (S11) supersedes this.

Files:
- C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-10.md
- C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-23.md
- C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-36.md

## Group W3, led by spec 3 (specs 3, 8 and 11)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-3-2-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-3-2-spec-writer.md).

1. Rows (group W3)
- **Row 41 · cl3 · folded.** §10 and S2 moved. I took the second route. The walk is no longer called TOOL-dTendedCadence-1 S2's. S2 now says it keeps no re-run journal, the one TOOL-dTendedCadence-48 S28 gives Maintain's walk. A second `seen` receipt is harmless because the record is checked before the first filing (TOOL-dCalibratedLens-27 S1). So a re-run after a filing only follows a failed final write, and adds one `seen` receipt to the intake already open, never a second intake. In §10 the walk now reads "a walk over TOOL-dDeclaredLoop-12's `order_by_needs`, as Maintain's is, without TOOL-dTendedCadence-48 S28's re-run journal". `grep -n "TendedCadence-1 S2's walk\|walk TOOL-dTendedCadence-1 S2"` prints nothing.
- **Row 46 · cl3 · folded.** §5, §6, §7, §10 and S8 moved. I took the cap route to keep the fold short.
  - "as TOOL-dTendedCadence-1 S6 lands a maintenance record" is gone. The pre-render builds the JSON with every route `pending`, the longest route word. It exits 1 with `loop — refused: record text <n> bytes over INTAKE_CAP_BYTES` (65536, TOOL-dWellOiledMachine-4 S2) and files nothing.
  - A redacted span lands as its placeholder. No digest covers the text: TOOL-dTendedCadence-49 rejects the JSON because of its digest, and cl3 has none. `record` exits 2 on stdin that is not JSON.
  - New AC10: the `over-cap` plant, a snapshot over 64 KiB. Under a counting stub filer it exits 1 with a filer count of 0. AC10 joins the existing `New arm:` line's covers.
  - §10 now says Maintain's record lands through TOOL-dTendedCadence-49.
  - `grep -n "as TOOL-dTendedCadence-1 S6 lands\|-1 S6 use it"` prints nothing.
- **Row 76 · cl8 · folded.** S3 and §5 moved. I took the second route because the computation already scans each order's whole bytes (cl8 §4 "The computation"). So it was the smaller change and keeps the design. S3 now says the order renders a block for each of its `ORDER_SLOTS` points, nine in all with `map` and `code` among them. The view is every path the order spells, the `bug-classes` slot's class paths included. §5's risk now says that over-read widens `in-view`, citing TOOL-dFurnishedOrders-4 S3. `grep -n "the slices, the \`map\` slot and the \`code\` slot it hands"` prints nothing.
- **Row 80 · cl8 · folded.** S1, the §2 preconditions, the §4 header-name line, the id 33 amendment, Files touched and §10 moved.
  - TOOL-dFairHearing-12 S2 joins the preconditions.
  - S1 quotes "into the factory unedited" and names `replay_scorer.py`. The cited `review_replay.py` lines are now stated as base lines of the moved names.
  - id 33 now factors `read_appendix_table` in `replay_scorer.py`. Files touched lists `replay_scorer.py`, and `review_cause.py` imports it.
  - `grep -n "factored in \`tools/workflows/review_replay.py\`\|imports \`review_replay.py\`"` prints nothing.
- **Row 107 · cl11 · folded.** §5 moved. I took the first route. `--paths` now names all four refusals and quotes rp13 S2: "an absolute path, a drive letter, a `..` segment or an empty entry". `grep -n "refused when absolute or carrying"` prints nothing.

2. Specs edited
- cl3: rev-5, 46753 bytes.
- cl8: rev-4, 29374 bytes.
- cl11: rev-3, 29432 bytes.

3. Hygiene run
I copied the index to the scratchpad, staged the three specs into the copy through `GIT_INDEX_FILE`, and ran `bash tools/memory-tree/check-memory-hygiene.sh --staged`. It exited 1 on one finding only: "HYGIENE check 9 FAILED — generated build index differs from a fresh render … memory/builds/dCalibratedLens/README.md (stale — differs from a fresh render)". Only `gen_build_index.py --write` cures that, so it is the main loop's. Nothing else names these specs. The copy is deleted.

4. Parent text that looks wrong
- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md:100-104` still describes the readings-JSON landing, which `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-71.md:36-40` replaces only once that unit builds.
- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-48.md:123-125`: the S28 journal records only completed items, and the parent's own audit found holes in it (`memory/builds/dTendedCadence/reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md:204`): a partial filing, `--dry-run` appends and a torn line. So S28's "files no second receipt" does not hold as written.

Files:
- C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-3.md
- C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-8.md
- C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-11.md

## Group W4, led by spec 9 (specs 9 and 16)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-9-2-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-9-2-spec-writer.md).

1. Rows (all five folded: the parent text bore each one out)
- Row 83 · `TOOL-dCalibratedLens-9` and `TOOL-dCalibratedLens-16` · folded. In spec 9, S1 now says it widens TOOL-dWellOiledMachine-53 S4's `read_act_records`, which reads `Item`, `Wall`, `Tokens-In` and `Tokens-Out` through `show`, so that it also reads `Act`. AC1 now checks `act`, and a missing or `null` `Act` turns it red. Files touched and §10 changed with it. In spec 16, the id 50 amendment now says its `act` field comes from that widening. Probe: `grep -n 'calls \`read_act_records(repo, build)\` once'` on spec 9 prints nothing.
- Row 84 · `TOOL-dCalibratedLens-9` (id 51) · folded. The §4 id 51 amendment drops the `git ls-files` / `git cat-file --batch` route and reads through `read_act_records` over `gov_record.py find --all`, the owner's pick at TOOL-dWellOiledMachine-32 §8 F6 (b). `--since` keeps "before any record is read" through a `since` argument that S1's widening adds, applied to `find`'s rows before any `show`. The §2 preconditions now name `find --all`. Probe: `grep -n 'one \`git cat-file --batch\`'` prints nothing.
- Row 87 · `TOOL-dCalibratedLens-9` · folded, §8 F4. F4 is re-worded to quote TOOL-dWellOiledMachine-12 S8's fallback ("else the item TOOL-dDeclaredLoop-7's `position.py <slug> --json` names for the binding's build, else `none`"). Only a line reading `item=none` counts as `unattributed`. The mark is now `RESOLVED (agent, 2026-11-03, delegated)`, still rung 1, with `widens: none · relaxes: none` on one line, and §9 names it. Probe: `grep -n 'act-less session counts as'` prints nothing.
- Row 136 · `TOOL-dCalibratedLens-16` · folded, S2, §3 preconditions and Waits on.
  - `NOT_TRENDED` gains `act-launch`, `act-adopt`, `act-killed` and `act-exit`, citing TOOL-dWellOiledMachine-6 S12.
  - `relaunch` stays trended, as a retry loop that `RESUME_ATTEMPTS` caps (wm6 S5).
  - `limit-hold` stays trended, as a hold on a session limit (wm6 S9).
  - TOOL-dWellOiledMachine-6 is added as a build-run precondition.
  - Probe: `` grep -n '`hook-failure` and' `` prints nothing.
- Row 142 · `TOOL-dCalibratedLens-16` · folded.
  - Sections moved: §3 non-goals, preconditions and Waits on; S2; S3; S4; §4 Evidence and Inventory; §5 perf; AC2; a new AC12; the §7 arm's covers; F1; §10.
  - It takes the return's first route.
  - S3 adds `read_cycle_items(repo, since)`, which reads `question` rows from `unattended.sh --mail read project` whose `subject` opens `owner item cycle`, citing wm48 S1, wm50 S4 and KICK-dKeptSession-5 S6. Lexicon `--suggest` answered OK for the name.
  - The trended set now includes `cycle`.
  - AC2 no longer journals a `cycle` line.
  - F1 is re-picked to `RESOLVED (agent, 2026-11-03, delegated)`: (b) for `cycle` alone and (a) for the other two. It is still rung 3, with `widens: none · relaxes: none`, and §9 names it. Its ask is narrowed to "TWO STALL AND LOOP CLASSES HAVE NO WRITER"; that ask is not yet filed in any BACKLOG.
  - The deciding line is wm50:86-87.
  - Probes: `grep -n -e '-49 and -50 produce the lines' -e 'raises a cycle owner item, each line'` prints nothing.

2. Specs edited
- `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-9.md`: rev-3, 28625 bytes.
- `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-16.md`: rev-3, 32715 bytes.

3. Hygiene run
- The command was `cp "$(git rev-parse --git-path index)" <scratchpad>/w4.index; GIT_INDEX_FILE=<scratchpad>/w4.index git add <spec 9> <spec 16>; GIT_INDEX_FILE=<scratchpad>/w4.index bash tools/memory-tree/check-memory-hygiene.sh --staged`. It exited 1, and the copy was deleted afterwards.
- The only failure was `HYGIENE check 9 FAILED — generated build index differs from a fresh render: build-index: render owed under --staged — memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-16.md is a build-index input or output ... build-index DRIFT — run: python tools/memory-tree/gen_build_index.py --write  memory/builds/dCalibratedLens/README.md (stale)`. Only a `gen_build_index.py --write` render cures that, so it is left for the main loop.
- Checks 10 and 23, the §3 edge joins and the debt guards were HELD under `--staged`. Check 30 printed "as-built clean". Nothing else was named, and none of it names my specs.

4. Parent text that looks wrong
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-53.md:70-77`: S4 still reads through the capped `find` with a `--paths` glob split, not the owner's `find --all` (wm32:325-329), and it reads no `Act`.
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-53.md:73-76`: the glob splits on act-id hex digits, but wm32:306-312 (F4) keeps the id out of the file name.
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-16.md:56-60`: S3 still lists `budget-spent`, `deadline-passed`, `cycle` and `secret-hit`, which wm79:93-95 drops.

## Group W5, led by spec 2 (specs 2, 4, 15, 41 and 46)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-2-2-spec-writer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-2-2-spec-writer.md).

1. Rows
- **Row 25, spec 2: folded.** Moved S5, §3, AC1, AC2, AC3 and AC5. `--key` is now admitted only with `--dry-run`, and with no key `price` exits 2 printing `price — refused: no key; run under cadence.py run loop-review`. AC5 now writes under `GOV_CADENCE_KEY=2026-W45` and adds two red cases: `--key` without `--dry-run`, and no key at all. AC1 to AC3 now pass `--key 2026-W45` to their dry runs, because a keyless dry run would exit 2. In the parent this rule is S3, not S2 as the brief says: tc1:68-70 reads "`--key <key>` is admitted only with `--dry-run` … no key at all exits 2", and AC3 at tc1:251-253. So the spec cites "TOOL-dTendedCadence-1 S3".
- **Row 26, spec 2: folded.** Moved §4 "The snapshot". The write-boundary grammar is unchanged. The text now says only the weekly form has a source (`derive_period` gives `weekly` and `daily` only, TOOL-dWellOiledMachine-13 S5). The monthly and `n<k>.<sha12>` forms come only from unit 3 §8 F2's ask, THE PERIOD KEY HAS NO MONTH AND NO LANDING COUNT. Until that ask lands, `GOV_CADENCE_KEY` carries the weekly form alone.
- **Row 59, spec 4: folded.** Moved §4 Evidence: `derive_estimate_hours` is now cited as TOOL-dWellOiledMachine-53 S4. Parent lines: wm53:54 is S3 `read_node_ledgers`, and wm53:61-66 is S4, which holds `derive_estimate_hours`.
- **Row 131, spec 15: folded, first route.** Moved §2, S3, §4 "Reads" and its Minted list, AC4 and §10.
  - S3 now extends TOOL-dTendedCadence-9 S1's `reads` verb with `--since`, `--entry` and subject arguments, and `measure_path_reads` with an `entry` keyword. It no longer adds a new verb or `measure_subject_reads`.
  - TOOL-dTendedCadence-9 S1 is added to §2's build-run preconditions.
  - AC4's `--transcripts` becomes `--projects-root`, tc9's own flag.
  - §10 drops "no seam counts a document's reads" and cites tc9 §8 F5.
  - Two results of using tc9's counter: the count rule now matches only `Read`, so `NotebookRead` is gone, and a `Read` is counted when it lies inside the tree. Entry injections still use the repository-key rule, so AC5 is unchanged.
  - The second route (rename the verb) was not taken. It would keep a second reader of the session records, which tc9:344-348 F5 rejects.
- **Row 167, spec 41: folded.** Moved §4 Evidence and S27. Evidence now gives the two base entries plus the third, `{prefix}/unattended/unattended.sh`, that TOOL-dFairHearing-17 S5 adds. S27 adds `agent-cap.js` beside whatever entries the guard holds at the pass, re-read then and never rewritten from the base list.
- **Row 168, spec 46: folded.** Moved §4 Evidence, S5 and AC2.
  - Evidence names TOOL-dFairHearing-17 S5, citing fh17:183.
  - S5 keeps `{prefix}/unattended/unattended.sh` beside the three new entries: in the `[[exempt_leg]]` row in the factory case, and in the manifest row in the hand case. The guard is re-read at the pass and never rewritten from the base list.
  - AC2 gains a red case: the pass dropping any entry the guard held before it.

2. Specs edited
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-2.md`: rev-5, 41882 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-4.md`: rev-5, 32588 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-15.md`: rev-3, 33033 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-41.md`: rev-3, 16136 bytes
- `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-03-spec-TOOL-dCalibratedLens-46.md`: rev-2, 11703 bytes

3. Hygiene run
- Command: `GIT_INDEX_FILE=<scratchpad>/w5-index` (a copy of the real index), `git add` of the five specs above, then `bash tools/memory-tree/check-memory-hygiene.sh --staged`. It exited 1, and the copy was deleted afterwards.
- It printed one finding, check 9: "build-index: render owed under --staged — memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-15.md is a build-index input or output … build-index DRIFT — run: python tools/memory-tree/gen_build_index.py --write · memory/builds/dCalibratedLens/README.md (stale — differs from a fresh render)". Only a `--write` render cures it, so it is left for the main loop.
- Every other check passed or was held under `--staged`. Nothing else named these specs.

4. Parent text that looks wrong
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md:46-47`: S5 hand-edits the `tier2-review self-test` guard in `tools/gate-legs.json`, which TOOL-dWitnessedBar-11 S1 to S3 make a render. fh17 says nothing about which declaration the entry goes in.
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md:183`: the same hand edit, repeated in its design section.
