**Serves:** research KICK-dKeptSession-1

# dKeptSession — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns for the re-ground brief
[`2026-10-26-prompt-KICK-dKeptSession-1-parents-reground`](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md),
each copied from its agent transcript. The cross-check record they answer is
[`2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck`](2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md).

## Group A, sibling kits and the driver (specs 1, 8, 20, 36, 44, 56)

I revised all six Group A specs (1, 8, 20, 36, 44, 56). Each now reads rev-3, dated 2026-10-26, still DEFERRED. Each is under 49152 bytes and has a new §9 line naming the sections moved, the cross-check record and its rows. I refused no rows: each parent line the record cites says what the record says it does. I ran the memory hygiene gate over an index copy with only these six specs staged. Its one failure was check 9, which wants the main loop to run `gen_build_index.py --write` for `memory/builds/dKeptSession/README.md`, so I left it. I deleted the copy afterwards, and nothing is staged in the real index. I did not run the naming lexicon.

| Spec | Rev | Bytes | Rows | Sections moved |
|---|---|---|---|---|
| 1 | rev-3 | 32956 | 3 | S4 · §3 Edges · §5 · AC6 · §8 F4 · §10 |
| 8 | rev-3 | 23418 | 33 | S5 · S8 · §3 Edges · §4 Alternatives rejected · §5 · §10 |
| 20 | rev-3 | 22918 | 73, 74 | S2 · S4 · AC4 · §3 Edges · §4 read order, Inventory, Files touched · §5 · §8 F3 · §10 |
| 36 | rev-3 | 12615 | 100 | S2 · S3 · AC3 · AC4 · §4 Evidence |
| 44 | rev-3 | 34724 | 105 | S9 · §10 |
| 56 | rev-3 | 33755 | 108 | S3 · AC3 |

**Spec 1.**
- `presets.py` now finds `guard.py` through the policy kit's one inline `resolve_kit_dir` block (`tools/policy/policy.py:1132-1169`) and runs it as one subprocess per load, not one per key. If the loop kit is not found, the load exits 2 naming it.
- **New fork F4, open for the owner.**
  - (a) Ask dDeclaredLoop for a `guard.py --expansion` verb. It reads `<key>=<value>` lines on stdin, judges each with `check_expansion_value`, and exits 2 on any refusal.
  - (b) Add a `requires_if` row naming `loop` to `tools/policy/kit.toml`.
  - Recommendation (a). The ask the build run would file targets TOOL-dDeclaredLoop-2 S8.

**Spec 8.**
- The hook now spawns the policy kit's existing reader command, `node <policy kit>/policy-mirror.js get actions.free --repo <repo>` (TOOL-dGroundRules-5 §4). It no longer loads that module into the hook.
- I added no fork, because the choice follows from what exists. That command is already there, so no parent change is needed. The `requires_if` route is something the rule allows only as a declared exception, and §4 now lists it as a rejected alternative.

**Spec 20.**
- **S2:** `check_scenario_policy` reaches the policy kit through `loop_lib.py`'s inline `resolve_kit_dir` and two subprocess calls:
  - a new `presets.py slot` verb, which this unit adds to unit 1's module and which checks the `never` list and `check_value`;
  - then `presets.py pairs`, as spec 44 S41 already says.
- **S4:** `read_scenario_value` reads a `scenarios.py slots --build <slug>` verb by subprocess. AC4 now says its fixture holds the policy kit.
- **New fork F3, open for the owner.**
  - (a) Ask dDeclaredLoop for the `slots` verb.
  - (b) Add a `requires_if` row naming `loop` to `tools/policy/kit.toml`.
  - (c) This unit adds the verb to `tools/loop/scenario.py` itself.
  - **Recommendation (c), which differs from the brief's (a)-or-(b) framing.** The verb exists to print this unit's own slot fields, and S2 already puts this unit's code in that file. The owner may still pick (a).

**Spec 36.**
- `<driver>` is `resolve_kit_dir("unattended", "unattended.sh", here)` from `loop_lib.py`'s inline block.
- "Absent driver" now means that block's `LookupError`. The `isfile` test applies only to the path it resolved.
- AC4's plant removes the kit from all three places the block searches.

**Spec 44.** S9 now matches spec 56 S23: `readCard` and `extractRouteUnits` are copied inline into `mail-notice.js` and never loaded from the hooks kit. `tools/unattended/gate-guard.js:173-177` is the existing example of that pattern.

**Spec 56.**
- `run_driver` finds `<driver>` once per process through the inline block.
- It re-raises the block's `LookupError` unchanged, as the one "unarmed" signal each caller handles in its own way. `resolve_bash`'s `LoopError` still means "driver present, no usable shell".
- AC3 records `argv[1]` as the resolved path and adds a case where the kit is absent and nothing is spawned.

No resolved fork was re-resolved, and no other fork was reopened.

**Parent specs that look wrong:**
- **TOOL-dGroundRules-10 S5, as built.** `tools/hooks/agent-cap.js:465-469` loads the policy kit's `policy-mirror.js` in process. `tools/hooks/kit.toml` declares no `requires_if` for it, so this is the same rule breach as row 33, in the parent's own code. Spec 8 leaves that line alone.
- **TOOL-dDeclaredLoop-3:54-55** still says `resolve(...)`, as the record notes. It is not in this group.
- **Possibly the same class in spec 1, not on the record.** S5's `arm_presets` compares the loads "both ways" with `[[selects]]` rows of `tools/loop/loop.toml`, reading another kit's data file directly. I left it unchanged because no row covers it.

Files:
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-8.md
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-20.md
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-36.md
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-56.md

## Group B, loop-kit reads and records (specs 5, 7, 9, 10, 11, 13)

All six Group B specs are revised and every row assigned to them is answered. I refused none. The hygiene gate names none of the six. Its one failure is check 9, which needs the main loop to re-render the build index. The naming lexicon exits 0.

Folder: `C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dKeptSession\spec\`

| Spec | Now reads | Bytes | Rows |
|---|---|---|---|
| `KICK-dKeptSession-5` | rev-8 | 36295 | 13, 16 |
| `KICK-dKeptSession-7` | rev-3 | 28490 | 23, 24, 26 |
| `KICK-dKeptSession-9` | rev-4 | 25939 | 36 |
| `KICK-dKeptSession-10` | rev-3 | 21520 | 39 |
| `KICK-dKeptSession-11` | rev-3 | 19185 | 43 |
| `KICK-dKeptSession-13` | rev-3 | 28452 | 49 |

Every status line is still `DEFERRED` and dated 2026-10-26. Each spec has one new §9 line that names the cross-check record and its rows.

**`KICK-dKeptSession-5`** — moved: §2 S10 and S12, §4 "The transition, in order", §6 AC6.
- **Row 13:** the disposal step works out `disposed=` at step 3a. A new step 5a writes the `mailbox-message` records after dDeclaredLoop-3's step 5 and before its step-6 commit, so the staged-index refusal at step 4 never sees them. No fork was needed, because this unit already inserts its own steps into that writer.
- **Row 16:** the record now serves as `mailbox-message`, never `journal`, with the tuple and HYGIENE list joins credited to spec 39.
- AC6 now checks that all three records land in the one transition commit.
- No forks added.

**`KICK-dKeptSession-7`** — moved: §2 S3, S4 and S6, §3 Non-goals and Edges, §5, §6 AC7, §8 F3 and F5.
- **Row 23:** the lease's `witness` is field 15 and `--claims` prints only fields 1 to 5 (I confirmed `cut -f1-5` at `tools/unattended/unattended.sh:2204`). Until a reader exists, the dependent holds as `awaiting confirmed`.
- **Row 24:** S4 takes the listing at the transition commit `write_transition` makes. When `micro-format` is the only channel, no commit is made, so it takes the listing at `HEAD`. AC7 now plants an older `--witness` to show the difference.
- **Row 26:** S6 reads both keys with `policy.py get`, run as a subprocess.
- **F3:** marked `RESOLVED (agent, 2026-10-26, delegated)` again, on rung 1, naming dPlacedRequest-1 S8 at rev-5.
- **F5 (new, open for the owner):** recommends option (a), asking dPlacedRequest for a verb that reads the witness. The ask the build run would file: "TOOL-dPlacedRequest-1: a verb `unattended.sh --lease show build <slug>` prints the lease's `witness` field from `CLAIM_ROWS`, or `-`".

**`KICK-dKeptSession-9`** — moved: §2 S3 and S6, §3 Edges, §5, §6 AC2, §8 F4 and F5.
- **Row 36:** S3 now reads the transition channel with `git`, as dPlacedRequest-1 F8 (a) does. AC2 also runs with only the `log` channel. S6 reaches `check_cap` through `budgets.py check`, run as a subprocess; that verb already exists at `tools/policy/budgets.py:370`.
- **F4:** marked `RESOLVED (agent, 2026-10-26, delegated)` again, on rung 1, naming dDeclaredLoop-12 S4 and dPlacedRequest-1 F8 (a). Reading by `git` gives the commit date directly, so the old ask for a time field is dropped.
- **F5 (new, open for the owner):** recommends option (a), because no loop-kit verb prints the steps. The ask: "TOOL-dDeclaredLoop-1: `loop_lib.py --steps` prints one `<step tag>` TAB `<state>` line per `[[step]]` row".

**`KICK-dKeptSession-10`** — moved: §2 S3, §3 Edges, §5. `mailbox.reads` is now read with `policy.py get` as a subprocess. No forks added.

**`KICK-dKeptSession-11`** — moved: §2 S3, §3 Edges. `notify.owner` is now read the same way. No forks added.

**`KICK-dKeptSession-13`** — moved: §2 S3, §5 risks, §8 F3.
- **Row 49:** S3 reads the extended token tuple.
- **F3:** its chosen option still stands, so I only replaced the false reason. The new bound: the parents' specs name 21 record kinds, and the longest `records —` line I measured on any build is 541 bytes for 5 kinds. A build using all 21 would reach about 2.6 KB against the 8192-byte card cap.
- One thing to know: some existing session cards are already 7.3 to 7.8 KB. A long `records —` line could therefore get a card refused whole (it is never cut short). I added this to §5 risks.

**Acceptance checks:**
- Each spec is under 49152 bytes.
- A `grep` for each quoted stale sentence prints nothing in any of the six.
- I staged the six specs into a copy of the index and ran hygiene `--staged` on it. It reported only check 9: `memory/builds/dKeptSession/README.md` is stale until `gen_build_index.py --write` runs, which is the main loop's job.
- I deleted the index copy, and the real index has nothing staged.

**Parent specs that look wrong:**
- dDeclaredLoop-3 S4 (around dl3:54-55) still reads `transitions.record` with an in-process `resolve(...)`. That conflicts with the sibling-kit rule in dDeclaredLoop-12 S4 (the cross-check record notes this too).
- dPlacedRequest-1 S8 says `leases.renewal` sets each write's `witness`, but never says what `witness` holds under `activity`, `fixed` or `none` (row 27, unknown until built). If it is `-`, spec 7's `confirmed-interfaces` holds until the parent lands.

**Things outside my group to note:**
- `KICK-dKeptSession-39` S4 still says it replaces spec 5's `journal` binding by name. Spec 5 no longer contains that sentence.
- `KICK-dKeptSession-10` §8 F3 still has the main loop file a row in dDeclaredLoop's `BACKLOG.md`, which this brief's ask rule forbids. I left it alone because the brief said not to re-open other forks.
- Spec 9's old F4 says its ask was "filed by the main loop". If that row exists in dDeclaredLoop's backlog, it is now stale.

## Group C, the card, the claim and the wait row (specs 12, 18, 25)

I've revised all three Group C specs: 12, 18 and 25. Every row I was given held up when I re-read both sides, so I refused none. Each spec stays `DEFERRED`, is under the 49152-byte cap, and has a new §9 line naming the cross-check record and its rows. I didn't touch any other file, and the real index has nothing staged.

On the hygiene check: I ran `check-memory-hygiene.sh --staged` over a copy of the index with only these three specs staged. It exits 1 on check 9 alone, which is the build-index render the main loop owes. It flags `dKeptSession/README.md` and spec 7 as stale and says spec 12 is an input to that render. It reports nothing else against any of the three specs. I deleted the index copy and my edit script afterwards.

| Spec | Rev | Bytes | Rows answered |
|---|---|---|---|
| 12 | rev-3 | 22118 | 45 |
| 18 | rev-3 | 17699 | 65 |
| 25 | rev-3 | 29096 | 82, 83, 87, 90 |

**Spec 12** (`2026-10-26-spec-KICK-dKeptSession-12.md`)
- **Sections moved:** §2 S4, §4 Evidence, §6 AC5, §9.
- **What changed:** S4 now takes the worktree path from the `tree —` cell of the stored build card that pr2 S6's lookup read: the ref's message, the cache or the snapshot. It reads that before the re-key, and never reads the re-keyed `<sid>.md`, whose cell names the replaying session's own tree.
- **No fork:** the stored text already keeps the cell its publisher or follower rendered. `render_tree_cell` is a startup cell called inside `render_card` at `manifest-check.sh:535`.
- **AC5:** now replays from a different tree, so reading the re-keyed cell makes it fail.
- The old sentence "as S6's lookup re-keys it" no longer appears.

**Spec 18** (`2026-10-26-spec-KICK-dKeptSession-18.md`)
- **Sections moved:** §10 and §9 only.
- **What changed:** §10 now says pr3 S3 declares `item.entry.claim` with the outcomes `claimed`, `slug-taken`, `awaiting` and `refused`, routes `claimed` to `transition`, and S4 removes its stand-in row.
- **S2 still owed:** dl13 S7's route join matches outcomes to rows but never checks the `disposition` those rows carry, so S2's join is still needed.
- **Forks:** none added.

**Spec 25** (`2026-10-26-spec-KICK-dKeptSession-25.md`)
- **Sections moved:** §2 S1 and S4; §3 Edges; §4 Evidence, The row, The wait in order, Rollout and Alternatives rejected; §6 AC4 and AC5; §8 F3, F4, F6 and F7; §9.
- **Row 82:** the Evidence bullet now names the witness source as the trailer or the `-transition-<n>.md` log record, notes that any other `--witness` exits 2, and covers the `micro-format`-only case.
- **Row 83:** S4 passes the question commit only after the landed witness check accepts it. Otherwise it passes the transition witness that pr1 §4 names, so the beat is never refused. The Rollout, AC4's fixture note and AC5 now say so.
- **Row 87:** `returns` stays prose, `"the answer's mail commit"`, pointing at F6, because the answer writes a mail commit and no record kind.
- **Row 90:** `on-deadline` is now `"stand-in:tools/unattended/unattended.sh"`, the `defaulted` route's target. F3's deferral is gone.

Forks in spec 25:
- **F3:** its mark is unchanged, `RESOLVED (agent, 2026-10-26, delegated)`. I only replaced the deferral sentence.
- **F4:** its mark is also unchanged. The ask now adds "even when it records no transition of the build on the channel `transitions.record` makes". I kept the existing clause about equalling the record's `witness`, because successive beats during one wait pass the same question commit.
- **F6 (new, open for the owner):** what `returns` names when no record kind exists. The options are:
  - (a) ask dDeclaredLoop to accept a prose `returns`;
  - (b) `record-kind.mailbox-message@1`, which would name a producer that never writes it;
  - (c) a new record kind, which records the same fact twice.

  I recommend (a). The ask the build run would file is: "TOOL-dDeclaredLoop-24: on a non-role row, a `returns` naming no record kind is prose and joins nothing".
- **F7 (new):** marked `RESOLVED (agent, 2026-10-26, delegated)`, rung 3. It settles how the beat knows the landed verb accepts a question commit. I chose a capability probe of the witness check `--lease renew` applies, with no write. A version gate was rejected because the lease verbs and the beat are in one driver, so it would compare the file with itself. Trying the renew and falling back was rejected because it costs a second fetch and treats every exit 2 as a refusal.

Parent specs that look wrong:
- **pr3 and dl24 disagree about prose `returns`.** pr3:160-165 says a `returns` naming no record kind "is prose and joins nothing … (TOOL-dDeclaredLoop-24 §4)". But dl24:144-145 only says that about inputs, and writes `returns` only as `record-kind.<name>@<n>`. Spec 25's F6 rests on the same gap.
- **pr1 names no function for its witness check.** pr1 §4 "The witness under `progress`" describes the check only in prose. F7 asks the build pass to name it as one function that both the renew and the beat call.
- **The record cites one line off.** It places the call to `render_tree_cell` at `manifest-check.sh:534`; at HEAD it is on :535.
