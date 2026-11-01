**Serves:** research TOOL-dWellOiledMachine-1

# dWellOiledMachine — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns of the re-ground brief [`2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground`](../prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md), each copied from its agent transcript by script; only the headings are the main loop's, each returned heading demoted two levels. Four writers were resumed after their first return: three to fix in-process calls they reported outside their rows, and one to give each asked verb one owning fork across the five groups.

## Group A, specs 1 to 9

I've revised all nine Group A specs (1 to 9) for every row the record names. Each is under 49152 bytes and keeps status `DEFERRED`. I refused no rows: each one checked out against the parent text.

**Checks:** the memory hygiene gate, run over a copy of the index with only my nine specs staged, flags none of them. Its one failure is check 9, which wants `python tools/memory-tree/gen_build_index.py --write` re-run (`memory/LIVE.md` and the `dKeptSession`, `dOrderedCharter` and `dWellOiledMachine` READMEs are stale). That render is the main loop's job, so I left it. The index copy is deleted, and I didn't run the naming lexicon. A grep of all nine finds no remaining `through `resolve``, `resolve(key` or `readPolicy` read and no hand-written `tools/gate-legs.json` leg row.

**Per spec** (all §9 lines are dated 2026-10-28 and cite the cross-check record with their row numbers):

| Spec | Rev | Rows | Sections moved | Forks | Bytes |
|---|---|---|---|---|---|
| wm1 | rev-3 | 1, 2, 3 | §2 S3, S7 · §4 The launch, Inventory, Files touched · §6 AC10 · §8 F1, F4 · §10 | F1 re-resolved `RESOLVED (agent, 2026-10-28, delegated)`, rung 1, naming PLAY-dOrderedCharter-7. The policy kit now runs a new verb, `launch.py argv`, instead of loading the factory. F4 added, open for the owner: which principle the `runtime selftest` leg enforces, since no v2 `[enforcement]` row names cl-0279. Recommends `principle.p36`. | 38605 |
| wm2 | rev-3 | 4, 5 | §1 · §2 S1, S6, S8 · §3 Edges · §4 Inventory, Files touched · §7 · §8 F4 · §10 | F4 added, open: how to reach the shrink-list factory. Recommends asking dKeptSession for a verb over a named kit's list. The leg's `enforces` is `principle.p15`, because v2:1837 names cl-0280. | 29654 |
| wm3 | rev-2 | 9 | §2 S4, S8 | none | 31268 |
| wm4 | rev-3 | 12, 13 | §2 S1, S6 · §3 Edges · §4 The hook · §6 AC1, AC6 · §8 F3 · §10 | F3 added, open: how the prompt reaches `request.py key`. Recommends asking dPlacedRequest for a stdin form (`key -`), because a temp file would put the unredacted prompt on disk. | 26163 |
| wm5 | rev-2 | 15, 16 | §2 S2, S3, S4, S5 · §3 Edges · §4 The witness rule, Inventory · §6 AC5 · §8 F3 · §10 | F3 added, open: where S3 gets the disposition record's commit. Recommends asking dDeclaredLoop for `loop_lib.py disposition --hold` to print the record's path. Also mints the verb `ratify.py disposition` for `placement.py` to call. | 25920 |
| wm6 | rev-3 | 19, 20 | §2 S5, S6, S7 · §3 Edges · §8 F4 | F4 added, open: how to read a lease's epoch. Recommends asking dPlacedRequest to add `epoch` to the holder verb that tr2 F6 already asks for. | 36605 |
| wm7 | rev-3 | 21, 24 | §2 S1, S6, S7 · §3 non-goals, Edges · §7 · §8 F3, F4, F5 · §10 | F3 re-resolved `RESOLVED (agent, 2026-10-28, delegated)`, rung 1, naming TOOL-dBoundRoles-3 and layer-runtime. F4 added, open: how to read stage rows, run agents and the session tree. Recommends a dBoundRoles stage-row verb, the existing `handoff.py agents --run`, and a runlog verb this build adds. F5 added, open: where `script` and `allow` come from. Recommends asking dBoundRoles. | 30787 |
| wm8 | rev-3 | 27, 29, 30 | §2 S4, S8, S9 · §4 Files touched · §6 AC7 | none. The leg's `enforces` is `principle.p26`, because v2:1848 names cl-0286. | 30761 |
| wm9 | rev-3 | 31, 33 | §1 · §2 S2, S5 · §3 Edges · §6 AC5, AC6 · §8 F2 · §10 | F2 re-resolved `RESOLVED (agent, 2026-10-28, delegated)`, rung 1, naming TOOL-dBoundRoles-22 and -3. The reservation size is now the stage row's `cap` rather than its `fan`. It cites wm7 F4 instead of opening a second fork. | 24912 |

**Changes that go beyond swapping one call for another:**
- **wm9 now reserves `cap`, not `fan`.** br22:108-109 defines `fan` as the most agents a stage spawns in one call and `cap` as the most in flight at once, and the slot ledger counts agents in flight. So F2's earlier pick was wrong on the parent's own terms, and AC5 and AC6 changed with it.
- **New verbs in this build's own runtime kit:** wm1 adds `launch.py argv` and wm5 adds `ratify.py disposition`. In wm5 the loop kit's `breakpoints.py` and `placement.py` now run `ratify.py` as subprocesses.
- **Policy refusals:**
  - wm3: a refused read refuses the pause or the override write.
  - wm5: a refused harness read refuses the fallback.
  - wm6: a refused read relaunches nothing and journals the refusal.
  - wm8 and wm9: a refused read falls back to the catalogue default.

**In-process sibling calls the record doesn't list** (I left these unedited because they aren't my rows):
- wm6 S1 and its F3 call the loop kit's `derive_position` in process.
- wm3 S3 calls the loop kit's `write_transition` by name.
- wm1 S2 and §3 still say dBoundRoles' renderer fills `fan` (and S2 also has `script`), but br3:48-61 renders neither.

**Parent specs that look wrong or incomplete:**
- TOOL-dDeclaredLoop-56 S47 (dl56:236-238) says `loop_lib.py disposition --hold` is the only reader of a disposition record but never says what it prints.
- KICK-dKeptSession-19 S1 (ks19:30-36) puts the shrink-list factory in `policy.py` with no verb another kit can call; `policy.py lists` only covers the policy kit's own two lists.
- TOOL-dPlacedRequest-19 S1 (pr19:36): `request.py key` only reads a file, so a caller holding unredacted text has nowhere safe to pass it.
- wm5 cited TOOL-dDeclaredLoop-16 S4 for `check_owner_disposition`; it actually lives in TOOL-dDeclaredLoop-31 S6. I corrected the cite.

Wherever a leg row is involved, Files touched records that a hand edit of the manifest row stands in until TOOL-dWitnessedBar-11 lands `leg_factory.py`, which isn't in the tree yet.

The spec files are in `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/`, named `2026-10-26-spec-TOOL-dWellOiledMachine-1.md` through `-9.md`.

## Group B, specs 10, 11, 12, 15, 16, 17, 19, 20, 23 and 24

Group B is done: all 10 specs are revised for the 17 rows the record names for them. No row was refused, and nothing is staged in the real index.

**Checks**
- **Size:** every spec is under 49152 bytes.
- **Status and §9:** each Status line reads `rev-N+1 · 2026-10-28`, still `DEFERRED`, and §9 holds one new 2026-10-28 line naming the sections moved and the record rows.
- **Old sentences:** grepping for every quoted old sentence prints nothing.
- **Hygiene:** `check-memory-hygiene.sh --staged`, run over an index copy with only these ten specs staged, exits 1 on check 9 alone. That says a build-index render is owed: `LIVE.md` and the READMEs of dWellOiledMachine, dKeptSession and dOrderedCharter differ from a fresh render. Only `gen_build_index.py --write` cures that, so it is the main loop's. The copy is deleted.
- **Lexicon:** not run, because no new name was minted.

**Per spec** (path `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-<n>.md`)

| Spec | Rev | Rows | Sections moved | Forks | Bytes |
|---|---|---|---|---|---|
| wm10 | rev-4 | 35 | S5, S6, S8, §5, §10 | none | 42382 |
| wm11 | rev-3 | 37, 38, 40 | S1, S2, S10, Inventory, Files touched, AC8 (new), §10 | F4 open, F5 open | 31923 |
| wm12 | rev-4 | 41 | S11, Inventory, Files touched, AC10 (new) | F5 open | 34848 |
| wm15 | rev-2 | 43, 44 | S3, S5 | none | 23675 |
| wm16 | rev-3 | 47 | S5, §4 The prune, §10 | none | 26533 |
| wm17 | rev-3 | 49 | S3, S4 | none | 29295 |
| wm19 | rev-2 | 53, 55, 56 | S4, S5, S6, §3 non-goal and Edges, §10 | cites wm30 F3, none minted | 25726 |
| wm20 | rev-3 | 57 | S4, Inventory, Files touched, AC7 (new) | F2 open | 26941 |
| wm23 | rev-4 | 59 | S9, Inventory, Files touched, AC8 (new) | F4 open | 26158 |
| wm24 | rev-3 | 60 | S2, §10 | none | 24328 |

**How the main rows were answered**
- **Policy reads:**
  - The Python readers now run `policy.py get <key>` as a bounded subprocess, and each spec states what a refused read does.
  - wm10's `dispatch.js` and wm19's `act-binding.js` spawn `policy-mirror.js get` instead. A failed read takes the fail-closed default: `closed` for wm10, `refuse` for wm19.
  - Both JS files find `policy-mirror.js` by their own path join. The cross-check's Change for row 35 suggested taking `resolvePolicyHelper` from `scratch-guard.js`, but that would import the hooks kit, so I did not follow it.
- **Legs (wm11, wm12, wm20, wm23):** each leg is now one `[[gate_leg]]` row of `tools/runtime/kit.toml` holding `enforces`, made by `leg_factory.py new`. Each spec records that a hand edit of the manifest stands in until `leg_factory.py` lands.
- **The `enforces` forks:** the clauses these specs carry (0289, 0290, 0298, 0301) appear in no v2 `[enforcement]` row, so each leg has an open fork:
  - wm11 F5 recommends `principle.p5`.
  - wm12 F5 recommends `principle.p22`.
  - wm20 F2 recommends `principle.p16`.
  - wm23 F4 recommends `principle.p27`.
- **Worktree root (wm11 F4, row 38):** the cross-check's fix doesn't work as written. `render_playbook.py --target . --answers worktree_root` prints `{"worktree_root": null}` today, because the key is no placeholder and the per-node override isn't read there.
  - F4 is open and recommends an ask to the playbook kit's owner: make `--answers worktree_root` answer this node's override, else the derived root.
  - The other options are a `requires_if` row or an inline copy of the derivation.
- **Agent transcripts (wm19, row 56):** wm30's F3, already open from Group C, asks dBoundRoles for `handoff.py agents --json` and names spec 19 as one of its readers. wm19 cites that fork and minted none.
- **Roles (wm24, row 60):** I did not need a new verb. The roles kit already renders each role's `writes` into `.claude/roles.json`, and br1 F6's `check_layer_roles` reads that file the same way. wm24 now reads it as JSON data.
- **Claims column (wm15, row 44):** `clock-offset` is now `CLAIM_ROWS` field 19, after `last-fetch`, and `--claims` still prints fields 1 to 5.
- **Author/verifier (wm19, row 53):** the non-goal no longer names TOOL-dBoundRoles-25. No dBoundRoles spec names an owner for that separation.

**Things that look wrong elsewhere** (none of these files were edited)
- **wm42** (Group D): its S1 list of by-value readers of `.claude/roles.json` should now include wm24's `map_reads.py`.
- **wm19 S3, not flagged by the record:** `check_role_harness_rows` in the runtime kit's `shape.py` compares against the stage rows' default `fan`. The only reader of those rows is `load_workflows` in the roles kit, so this check is an unflagged sibling-kit read. It needs the same stage-rows verb fork that Group D is writing for wm43 and wm45.
- **br1 F6:** I checked its text and it agrees; it is noted only as the precedent wm24 now follows.
- **No parent spec is wrong.** The cross-check's Change lines for rows 35 and 38 are inaccurate, for the reasons above.

## Group C, specs 25, 26, 30, 32, 33, 34, 36, 37 and 39

I revised all nine Group C specs for the 16 rows the record names: 25, 26, 30, 32, 33, 34, 36, 37 and 39. No row was refused.

Every spec is under 49152 bytes and is LF-only. Each Status line now reads `DEFERRED · rev-N+1 · 2026-10-28`, and each §9 has one new line naming the sections moved, the cross-check record and its rows. Nothing is staged in the real index.

On the hygiene gate (index copy, with only these nine specs staged): the only failure was check 9. It is the `gen_build_index.py --write` render the main loop owes, and it names spec 25 only as an index input. It also lists `memory/LIVE.md` and the dKeptSession, dOrderedCharter and dWellOiledMachine READMEs as stale. I left all of that and deleted the index copy afterwards. I did not run the naming lexicon. The new names are `render_wall` in `act.py`, the `session_glob_py` block, and the asked verbs `loop_lib.py declaration` and `handoff.py shape-line`.

| Spec | Rev | Bytes | Rows | Sections moved |
|---|---|---|---|---|
| wm25 | rev-2 | 28937 | 61 | S4 |
| wm26 | rev-2 | 26749 | 62 | S2, S3, S4, §3 Edges, §6 fixture, §8, §10 |
| wm30 | rev-2 | 22426 | 68 | S4, §8, §10 |
| wm32 | rev-4 | 33753 | 69, 70, 71, 74, 75, 76 | S7, S8, S10, §4 Inventory and Files touched, AC5, AC9 (added), §8, §10 |
| wm33 | rev-5 | 34330 | 77 | S8, §4 Inventory and Files touched, AC4, §7, §8 |
| wm34 | rev-4 | 30090 | 80, 82 | S2, S4, Files touched, AC5, second `New arm:` line, §8, §10 |
| wm36 | rev-4 | 30218 | 89 | S5 |
| wm37 | rev-3 | 28679 | 90 | S5 |
| wm39 | rev-3 | 32222 | 94, 95 | S10, §4 Inventory and Files touched, AC10 (added), §8 |

**What each fix says:**
- **wm25, wm36, wm37:** each key is read by a bounded `policy.py get` subprocess. On a refusal:
  - wm25 answers `session`.
  - wm36 takes the default with a `binary — NOTE` line.
  - wm37 refuses the launch with `launch — refused · act-auth`, since S6's `last` arm makes `get` exit 2 on a bad list.
- **wm26:** runs `position.py <slug> --json` and `breakpoints.py list --build <slug>` as subprocesses. Its `attendance —` line carries the value and its `adds`.
- **wm32:** the `act` record becomes a typed kind:
  - Its registry row has `tag = "record.act"`, `layer = "layer.runtime"`, `lifecycle = "frozen"`, `readers = []` with a `readers-none` reason, and `id-rule = "<date>-build-<unit id>-act-<n>.md"`.
  - It joins `TYPED_RECORD_KINDS`, the factory's table and HYGIENE's list in one pass.
  - The writer passes `--unit <anchor> --caused-by <anchor>`.
  - `render_wall` is carried in the runtime kit.
  - The `Acts` table uses `find --kind act --build`, reads fields through `show`, keeps acts whose record was added inside the run's `window` (`tools/runlog/record.py:227`), and refuses to render past the cap.
- **wm33, wm39:** each leg is one `[[gate_leg]]` row of the runtime kit's descriptor carrying `enforces`, rendered by `leg_factory.py --write`. An AC greps the row and runs `leg_factory.py --check`. The spec records that a hand edit stands in until `leg_factory.py` exists.
- **wm34:** `find` is read within its cap and prints `trace — record find capped · <total> rows match` instead of claiming the population is whole. Transcripts are found through an inline `session_glob_py` block under a `PARITY_ROWS` row.

**Forks:**
- wm26 F4: ask dDeclaredLoop for `loop_lib.py declaration <item> --json`. Open for the owner, recommends (a).
- wm26 F5: ask dBoundRoles for `handoff.py shape-line`. Open for the owner, recommends (a).
- wm30 F3: ask dBoundRoles for `handoff.py agents --json`, because the existing `agent —` line falls back to the role file's effort (`handoff.py:902-906`). Open for the owner, recommends (b). It names wm7, wm19 and wm43 as readers of the same functions.
- wm32 F4: the act id goes in the `Act` field, not the file name. `RESOLVED (agent, 2026-10-28, delegated)`, rung 1, on tr2's minting rules and oc42's typed-kind naming.
- wm32 F5: `--caused-by` takes the anchor unit id. `RESOLVED (agent, 2026-10-28, delegated)`, rung 1 on tr19 S5.
- wm32 F6: ask dTotalRecall for an uncapped `record find` mode. Open for the owner, recommends (b). It is the one cap fork, and it names wm34, wm44, wm51 and wm53. wm34 cites it.
- wm33 F4: the `enforces` tag. Open for the owner, recommends `principle.p35`; cl-0311 has no `[enforcement]` row.
- wm34 F4: the inline `session_glob_py` block. `RESOLVED (agent, 2026-10-28, delegated)`, rung 1. It follows the spec's own F1, which rules out the runtime kit depending on runlog.
- wm39 F4: re-resolved `RESOLVED (agent, 2026-10-28, delegated)`, rung 1 on tr19 S8. The ask is restated against `check_causes`' records: a record whose `Made-by` names an act that `bindings.py --read` finds `not-local` is red.
- wm39 F6: the `enforces` tag. Open for the owner, recommends `principle.p35`; cl-0317 has no row.

**Decisions for you:**
- **wm39 F4:** I re-resolved it as the brief says for a resolved fork. Under the brief's "An ask" rule it could instead be left open for the owner; that is your call.
- **Cross-group asks:** wm30 F3 and wm32 F6 are asks that other groups' specs share. Other groups' writers may open forks of their own for the same verbs, so a dedupe is owed.

**Same-class gaps the record did not row, left unedited:**
- wm25 S5 calls the loop kit's `derive_position(repo, slug)` in process.
- wm32 S9 still says "read through `resolve` (I31), run as `policy.py get`".
- wm32 S6 resolves the transcript through runlog's `resolve_session_tree`; wm34 F4's block could serve it.

**Parent spec that looks wrong:** tr11's own `shape-run` registry row (tr11:173-182) has `layer = "memory"`, which is not a layer tag. Its `readers` are file names and its `lifecycle` is prose, against tr18 S1 and its column table (tr18:45-49, :130-133).

The nine revised specs are in `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/`:
- 2026-10-26-spec-TOOL-dWellOiledMachine-25.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-26.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-30.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-32.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-33.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-34.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-36.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-37.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-39.md

## Group D, specs 41 to 48

All eight Group D specs are revised, one per spec, for the rows the cross-check record names. Every row was borne out by the parent text, so I refused none. All eight specs stay `DEFERRED`, are under 49152 bytes, and have one new §9 line naming the cross-check record and its rows. Grepping each row's quoted sentence now finds nothing, or only the corrected sentence.

I ran `check-memory-hygiene.sh --staged` over an index copy with only these eight specs staged. Its one finding is check 9: the build-index render is owed, which only `gen_build_index.py --write` cures. That one is the main loop's, and I left it. The index copy is deleted and the real index is untouched.

| Spec | Rev | Rows | Sections moved | Bytes |
|---|---|---|---|---|
| TOOL-dWellOiledMachine-41 | rev-3 | 99 | S2, §5, §10 | 24355 |
| TOOL-dWellOiledMachine-42 | rev-2 | 101 | S1 | 23703 |
| TOOL-dWellOiledMachine-43 | rev-3 | 103, 104, 106 | §1, S2, S5, S7, S8, §3 Edges, §4 table, §5, AC5, §8, §10 | 33497 |
| TOOL-dWellOiledMachine-44 | rev-3 | 109, 110, 111 | S2, S6, S8 | 29215 |
| TOOL-dWellOiledMachine-45 | rev-3 | 112, 113 | §1, S1, S3, S5, §3 Edges, §4 pseudo-code, AC2, AC3, AC5 | 29064 |
| TOOL-dWellOiledMachine-46 | rev-2 | 116, 117 | S3, S7, §3 Edges, §10 | 28273 |
| TOOL-dWellOiledMachine-47 | rev-4 | 118 | S1 | 29227 |
| TOOL-dWellOiledMachine-48 | rev-2 | 122, 123 | S2, S3, S4, S8, §4 Evidence, AC4, §8, §10 | 34133 |

**What changed:**
- **wm41:** the driver check now reads the lease holder through the verb that TOOL-dTotalRecall-2 §8 F6 asks dPlacedRequest for, and waits on F6's pick. It files no second ask.
- **wm42:** `check_layer_roles` joins the readers of `.claude/roles.json`. Its item check is unchanged, because no item names `gov-session`, which acts as `cycle`.
- **wm43:** a Workflow call now reserves the largest stage `cap`, not `fan`. The stage rows, run journal, task notifications and process chain are read through verbs by subprocess.
- **wm44:** mirror rows now count inside `record find`'s 40-row cap, with the total line kept last. `record_find.py` runs `mirror.py get|scan` by subprocess, and `memory.mirror` is read by `policy.py get`. A refused read counts as `none`.
- **wm45:** a Workflow call reserves `cap`, read through wm43's F3 verb. The limit is read by `policy.py get`; a refusal takes the catalogue default, as wm9 S2 does.
- **wm46:** the key is read by `policy.py get`. The route runs `loop_transition.py record` and `budget.py draw --cause re-dispatch` by subprocess.
- **wm47:** `runtime.hold-ceiling` is read by `policy.py get`.
- **wm48:** a refused `owner-question` makes `ask` raise nothing and exit 2, and AC4 gains that case. The run keys are read by `policy.py get`.

**Forks added.** Each is open for the owner with a recommendation; none was re-resolved:
- **wm43 F3, stage `cap` read:** recommend asking dBoundRoles for `handoff.py stage-caps <harness>`. I found no existing fork on this verb. wm45 cites this fork rather than opening its own.
- **wm43 F4, run journal and task notifications:** recommend asking dBoundRoles for `handoff.py run-state --session <file> [--run <id>] [--from <byte>]`.
- **wm43 F5, the process chain:** recommend this unit adding `scope.py --self-chain` to process-monitor, which no parent build owns.
- **wm48 F4, a catalogue row's `direction`:** recommend this unit adding `--row` to `policy.py get`, as wm43 S9 already edits that file. The alternative ask would go to dGroundRules, which is CLOSED.

**Things that look wrong or need a decision:**
- **The brief is wrong about `--explain`.** It says `--explain` serves where a spec needs the catalogue row. In fact `get --explain` prints only `policy: <key> · <source> · <reason>` (`tools/policy/policy.py:1333-1336`, `:1358-1359`), and no verb prints `direction`. That is why wm48 needed F4.
- **br1 (TOOL-dBoundRoles-1), possibly:** it puts `gov-session` in `layer.runtime` (br1:143), but none of its registration rows names that role. If `layer.runtime` is not a core row, `check_layer_roles`' fourth check would flag it red until wm42 retires the role. I did not check whether `layer.runtime` is core.
- **Group A must cite F3, not open a second fork.** wm7, wm9 and wm19 (Groups A and B) read the same stage rows and should cite wm43 §8 F3.
- **Left unedited, outside my rows:**
  - wm42 §4 Evidence still cites br1 `:98`, which is now `:107` (row 100, which agrees).
  - wm43 S9 and F1 lean on wm1 S7's in-process load (row 3, Group A).
  - wm45 AC6's "fan-two act" is wm9's reservation (row 31, Group A).
  - wm41 S3's holder test runs inside wm58's door, which waits on TOOL-dTotalRecall-2 §8 F6 (row 153, Group E).

The eight specs are in `C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dWellOiledMachine\spec\`, named `2026-10-26-spec-TOOL-dWellOiledMachine-41.md` through `-48.md`.

## Group E, specs 50, 51, 52, 53, 54, 56, 58, 59, 79 and 90

I revised all ten Group E specs and refused none of their 21 rows. Each spec keeps `DEFERRED`, has one new §9 line naming the sections moved and the cross-check rows, and is under 49152 bytes.

I ran the memory hygiene gate over a copy of the index with only these ten specs staged. The only red is check 9: the build index must be re-rendered (`gen_build_index.py --write`), which is the main loop's job. None of my specs is named in a failure. The check 25 "did not grade" lines are notes about the existing "READER NOT IN TREE" entries in specs 79 and 90. Under `--staged` the gate holds back the §3 edge-join check, so I couldn't confirm the edges I touched (51↔53, 54↔56) pair up; they are written as matching pairs. I deleted the index copy and the real index is untouched. A grep for each row's quoted sentence now finds nothing, or only the corrected sentence.

Specs live in `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/`.

| Spec | Rev | Bytes | Rows | Sections moved |
|---|---|---|---|---|
| 50 | rev-2 | 23034 | 126, 127 | §2 S2, S5, S7; §3 Edges |
| 51 | rev-2 | 21232 | 131 | §2 S2; §3 Edges; §5; §10 |
| 52 | rev-2 | 23941 | 135 | §2 S5; §8 F3 |
| 53 | rev-2 | 28438 | 136, 137 | §2 S4, S5; §3 Edges; §4 Inventory; §5 |
| 54 | rev-2 | 28204 | 140, 142, 143 | §2 S1, S2, S6; §3 Edges; §4 Evidence, Inventory; §8 F5; §10 |
| 56 | rev-3 | 24889 | 148, 149 | §2 S1, S2, S4; §3 Non-goals, Edges; §4 Inventory, Files touched; §5 |
| 58 | rev-4 | 37123 | 153, 154 | §2 S4, S5, S7, S8, S9; §3 Edges; §4 Files touched; §8 F5 |
| 59 | rev-2 | 27185 | 156, 157, 158 | §2 S3, S4, S5; §3 Edges; §4 Inventory, Files touched; §5; §6 AC7; §7 New arm; §10 |
| 79 | rev-4 | 46951 | 163 | §1; §2 S13, S29, S40; §3 Edges; §4 Files touched, Alternatives; §6 AC40 |
| 90 | rev-4 | 47533 | 165 | §1; §2 S3, S35, S37; §4 Files touched, Alternatives; §6 AC35, AC37 |

**What changed, per spec:**
- **50:** A parent's state is now the `state` field of the loop kit's existing `position.py <parent> --json` (TOOL-dDeclaredLoop-7 S7), so no new verb was needed. The release is recorded by running `loop_transition.py record` as a subprocess.
- **53:** Mints `read_act_records(repo, build=None)` in `ledgers.py`; the naming lexicon printed OK for it.
  - It runs `record find --kind act`. While a query's last line is the 40-row cap's total line, it re-queries with a `--paths` glob that adds one more hex digit of the act id. The act id is 12 hex digits (wm32 S1), so the split always ends.
  - Each row's fields are read with `record show`, and the `Item` filter is applied in `ledgers.py`.
  - Both policy keys are read through a `policy.py get` subprocess. Exit 2 admits nothing, as a refused ledger read already does.
- **51:** Reuses wm53's `read_act_records` rather than copying the narrowing. wm53 (order 38) lands before wm51 (order 54). I added the edge pair: 51 consumes-from 53, and 53 hands-off to 51.
- **52:** `members` takes the fleet tag and verdict from `--claims` fields 2 and 5. The `node-` keys come through the verb F3 asks for.
- **54:**
  - `--claims` is read as its five fields; `offer` comes through wm52 F3.
  - The workflow rows come through the dBoundRoles verb that wm7 §8 F4 already asks for, so this spec files no second ask.
  - Harnesses come from wm56's `act` verb. This unit adds `model --equivalent` and `hardware` to its own `roles_lib.py` CLI.
  - S6 now reads `roles.model.<role>.<harness>` from the assignment being checked. It asks the roles kit only for the adapter equivalent, because `get` reads the landed revision.
- **56:** The two `runtime.*` keys are read with `with_default=True`; the typed defaults are deleted and a `None` raises `RolesError`. The per-role keys are still read without it, so `own` keeps its source. `launch_act` reaches S1 to S3 through two new `roles_lib.py` verbs, `act` and `credential-check`, run as subprocesses.
- **58:**
  - The door's holder test, in S4 (c) and S5, waits on TOOL-dTotalRecall-2 §8 F6.
  - The `--quiesce` and `--unlease` verbs read the `lease` mode's `mine` class inside the unattended kit itself.
  - `quiesce` is now a typed kind: it joins `TYPED_RECORD_KINDS`, the factory table and HYGIENE's kind list, and its registry row is spelled with the cells tr1 and tr18 require. `Caused-by` is the build's anchor unit, the form wm32 uses for `act`.
- **59:**
  - Policy keys are read through a `policy.py get` subprocess, and the ending through `endings.py derive`.
  - S4 adds a `budget.py state --key` verb over its own `derive_period_budget`. I opened no fork for it: S4 already edits `budget.py`, and the returns' `Change:` line asks for exactly this.
  - Contention draws nothing: a refused take or an unanswering remote writes no record. New AC7 checks this and is added to the New arm line.
- **79:** S13 and S29 now edit the `[[gate_leg]]` declarations and re-render. S40 has each leg's own spec declare it with `enforces`, and records the hand-edit stand-in until `leg_factory.py` lands. AC40 now runs `leg_factory.py --conform`. No new leg, so no `enforces` fork was needed.
- **90:** S3 and S37 edit the runtime kit's `[[gate_leg]]` row. S35 edits the `manifest-check self-test` `[[exempt_leg]]` row at `tools/govkit/registry.toml:445`. AC35 and AC37 read those declarations, and the hand-edit stand-in is recorded.

**Forks:**
- **wm52 F3, open for the owner, new.** It asks dPlacedRequest to have `read_claims` keep the `node-` keys as `CLAIM_ROWS` columns after field 18, plus a read-only verb that prints named fields past the fifth. Recommendation (a). wm54 S1 reads `offer` through the same verb.
- **wm54 F5, open for the owner, new.** It covers how `discover.py` reaches the build index's units. The options are (a) this unit adds a `gen_build_index.py --units` read mode, (b) a `requires_if` row, or (c) parsing the rendered index region. Recommendation (a).
- **wm58 F5, open for the owner through TOOL-dTotalRecall-2 F6.** It is not a new ask; it records that the door waits on F6.
- I re-resolved no fork. None of the ten specs had a resolved fork that a parent now rules out.

**Rows partly refuted:** Row 142 says `--claims` lacks `status`, but `status` is field 3 of `--claims` (`tools/unattended/unattended.sh:2204`; pr1:206-208). I corrected only the `offer` part.

**Parent specs that look wrong:** One gap, no error found.
- TOOL-dTotalRecall-18's `home` column (tr18:130) reds any `fields` kind whose tracked glob matches no tracked file. So a newly registered kind such as `quiesce` (wm58) or `act` (wm32) would red `record-kinds` until its first record is committed. tr18 gives no exemption for a new kind; tr25 avoided it only because `stream-plan` is a `fence` kind.

**For the main loop:**
- Re-render the build index: check 9 (render owed).
- `leg_factory.py` is not in the tree yet, so specs 79 and 90 record a hand edit standing in for it until wb11 lands.

## Group A, resumed: the three in-process calls it found in wm1, wm3 and wm6

I've fixed all three in-process calls. None of the revs moved again; each spec's existing §9 line for this pass now ends with the sections moved and "writer-found, not a record row". No new fork was opened.

- **wm1** (rev-3, 39249 bytes). Sections moved: §2 S2 · §3 non-goals, Edges.
  - S2 now says dBoundRoles' work order renders only five blocks, with no `fan` and no `script` (br3:48-61).
  - The act's `fan` comes from its stage row, read as wm7 §8 F4 picks, the same way wm9 S5 reads `cap`. `script` comes from wm7 §8 F5.
  - The non-goal and the Edges line now credit dBoundRoles' renderer with only `role`, `schema` and `text`.
- **wm3** (rev-2, 31780 bytes). Sections moved: §2 S3, S5 · §3 Edges · §8 F4 wording.
  - B19, T11 and T12 are now recorded by running `python loop_transition.py record --build … --from … --item … --outcome … --witness …` as a subprocess (dl3:60-61), with the loop kit found through `resolve_kit_dir`.
  - In F4 I changed only the reference to `write_transition` into "the transition writer"; the fork stays resolved as it was.
- **wm6** (rev-3, 37210 bytes). Sections moved: §2 S1 · §3 Edges · §8 F3.
  - S1 reads the position engine by running `python position.py <slug> --json` as a subprocess (dl7 S7).
  - F3 is re-resolved, marked `RESOLVED (agent, 2026-10-28, delegated)`, rung 1, naming PLAY-dOrderedCharter-7. It keeps option (a), the engine read directly, but now through its own verb rather than an in-process call.

**Hygiene:** I reran it over an index copy with only my nine specs staged, and it names none of them. The one failure is check 9 again, the build-index render (`gen_build_index.py --write`), which is the main loop's to run. The index copy is deleted.

The specs are in `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/`:
- `2026-10-26-spec-TOOL-dWellOiledMachine-1.md`
- `2026-10-26-spec-TOOL-dWellOiledMachine-3.md`
- `2026-10-26-spec-TOOL-dWellOiledMachine-6.md`

## Group C, resumed: the three gaps it found in wm25 and wm32

I fixed all three gaps. Both specs keep this pass's rev (wm25 rev-2, wm32 rev-4), and each has its §9 line extended with the sections moved and "writer-found, not a record row".

The hygiene rerun (an index copy with only the nine specs staged) failed on check 9 alone, the same as before. That is the build-index render the main loop owes, and it names spec 25 only as an index input. No other finding names any of the nine specs. I deleted the copy afterwards. The real index has nothing staged, and all nine files are still LF-only.

1. **wm25 S5:** `run.py --host-act` now runs `python <loop kit>/position.py <slug> --json` as a bounded subprocess, found through the inline `resolve_kit_dir` block. On its exit 2, or with no loop kit found, it refuses with exit 2 and writes no act. §3 Edges and §6's fixture stub now name `position.py` instead of `derive_position`.
2. **wm32 S9:** the sentence now says only that both keys are read by a bounded `policy.py get <key>` subprocess, the policy kit found through the inline `resolve_kit_dir` block. The "through `resolve` (I31)" wording is gone.
3. **wm32 S6:** the transcript pointer now resolves through wm34's inline `session_glob_py` block, citing TOOL-dWellOiledMachine-34 S2 and §8 F4, instead of runlog's `resolve_session_tree`. I also changed the matching seam in §10 to the block. `resolve_session_tree` still appears at line 65, where S6 says where the block's glob comes from, and in §4 Evidence (line 151), which states a true fact about current code.

| Spec | Rev | Bytes | Sections moved by this fix |
|---|---|---|---|
| wm25 | rev-2 | 29447 | S5, §3 Edges, §6 fixture, §9 line |
| wm26 | rev-2 | 26749 | none |
| wm30 | rev-2 | 22426 | none |
| wm32 | rev-4 | 34378 | S6, S9, §10, §9 line |
| wm33 | rev-5 | 34330 | none |
| wm34 | rev-4 | 30090 | none |
| wm36 | rev-4 | 30218 | none |
| wm37 | rev-3 | 28679 | none |
| wm39 | rev-3 | 32222 | none |

Both edited specs are in `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/`:
- 2026-10-26-spec-TOOL-dWellOiledMachine-25.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-32.md

## Group D, resumed: wm42's readers after Group B's wm24

I made both wm42 edits inside the same rev-2. The Status line is unchanged at `rev-2 · 2026-10-28`, and the spec is now 24208 bytes.

**Sections moved this pass:** S1 and §4 Evidence.

- **S1:** wm24's `check_map_in_slice` (`tools/runtime/map_reads.py`) joins the readers of `.claude/roles.json`. The check you asked for: dropping `gov-session`'s row changes nothing it reads. It looks up `writes` for the role of a spawned agent, and `gov-session` is `agent: false` (`.claude/roles.json:43-48`), so no agent ever runs as it.
- **§4 Evidence:** the TOOL-dBoundRoles-1 cite now reads `:107` instead of `:98`; I confirmed line 107 is the retirement line. That is row 100 of the cross-check record.
- **§9:** the rev-2 line now lists `S1 · §4 Evidence` and names wm24 rev-3 S2's reader and the cite fix (row 100).

**Hygiene check**, run over an index copy with only wm42 staged: the one finding is check 9, the build-index render owed (`gen_build_index.py --write`). That is the main loop's to cure, and I left it. Nothing else names wm42. The index copy is deleted and the real index has nothing staged.

The spec is `C:\projects\coding-governance\.claude\worktrees\elastic-lalande-a8b091\memory\builds\dWellOiledMachine\spec\2026-10-26-spec-TOOL-dWellOiledMachine-42.md`. Everything else in my earlier return still stands; only wm42's sections and byte count changed (it was 23703 bytes).

## Group A, resumed: the fork dedupe across groups

Each verb now has one owning fork, and no spec outside wm7 still cites wm7 §8 F4.

**Hygiene:** I reran it over an index copy holding the seven specs this pass touched plus wm3 and wm6, which I touched earlier. It names none of them. The only failure is check 9, which needs `gen_build_index.py --write` re-run; that render is the main loop's. The index copy is deleted.

**Specs touched** (no rev bumped; each spec's existing 2026-10-28 §9 line now lists the sections moved and says "fork dedupe"):

| Spec | Sections moved | Bytes |
|---|---|---|
| wm7 | §2 S1, S6, S7 · §3 Edges · §8 F4 · §10 | 31497 |
| wm43 | §2 S5 · §8 F3, F4 | 34149 |
| wm30 | §8 F3 | 22619 |
| wm1 | §2 S2 · §3 non-goals | 39456 |
| wm9 | §2 S5 · §3 Edges | 25036 |
| wm54 | §2 S2 · §3 Edges | 28324 |
| wm19 | §2 S3 · §10, writer-found, not a record row | 26297 |

**What changed:**
- **wm43 F3** now owns the stage-row read for the whole build:
  - I renamed its asked verb from `stage-caps` to `handoff.py stage-rows <harness>`, because it now prints `{workflow: {key: {role, fan, cap}}}` (br22:34-45, :108-109).
  - I keyed the output by workflow so that wm7 S1 can get its `workflow` field from it.
  - `inflight.py` still reserves the largest `cap`.
  - Its text lists every reader: wm1 S2, wm7 S1 and S6, wm9 S5, wm19 S3, wm45 S3 and wm54 S2.
- **wm43 F4** is narrowed to a session's Workflow runs, their notifications and the byte offset. Its S5 reads each run's started agents through wm30 F3's verb. I kept it separate from wm30 F3 rather than merging, because it is a different verb: session-level runs, not one run's agents.
- **wm30 F3** owns the run-agents ask. I added `type` to the asked `--json` fields, because wm7 S7 needs each agent's type.
- **wm7:**
  - S7 finds the transcript through the inline `session_glob_py` block, as wm32 S6 does, and reads each run's agents and types through wm30 F3's verb.
  - F4 is re-resolved `RESOLVED (agent, 2026-10-28, delegated)` on rung 1, naming oc7 and the three canonical forks; it asks for nothing of its own.
  - F5 is unchanged.
- **wm19 S3:** `check_role_harness_rows` now reads the stage rows through wm43 F3's verb instead of calling `load_workflows` in process. S1's in-process read stays, because it runs in the roles kit's own `handoff.py`.
- **wm1, wm9, wm54:** their stage-row cites now point at wm43 F3. In wm1, `script` still cites wm7 F5.

No new fork was opened.

**Final open forks for these verbs:**
- Stage rows: wm43 §8 F3, open (asks dBoundRoles for `handoff.py stage-rows`).
- A run's started agents: wm30 §8 F3, open (asks dBoundRoles for `handoff.py agents --json`).
- A session's runs and notifications: wm43 §8 F4, open (narrowed `handoff.py run-state`).
- Transcript tree: wm34 §8 F4, already resolved; no open fork.

**Decision for you:** wm54 S2 needs the workflow entries' `roles` filtered by `driver` and `stage`. The verb asked in wm43 F3 works per harness and prints stage roles only, so it does not fully serve wm54. Either the wm43 F3 ask gains each entry's `driver` and `stage`, or wm54 needs a narrower read. I left the cite as instructed.

## The owner's picks, 2026-10-29: Group A, specs 1, 2, 4, 5, 6, 7, 11, 12, 20 and 23

All 10 Group A specs are revised, and the 13 forks the brief names for this group are marked `RESOLVED (owner, 2026-10-29)` in place. Each Status line still reads `DEFERRED`, dated 2026-10-29, and each spec has one new §9 line naming its forks, the brief `prompts/2026-10-29-prompt-TOOL-dWellOiledMachine-1-owner-forks.md`, and the sections moved.

**Checks:**
- **Size:** every file is under the 49152-byte cap (byte counts are in the table).
- **Open marks:** `grep -c "Open for the owner"` finds none in any of the ten specs.
- **Hygiene:** I ran `bash tools/memory-tree/check-memory-hygiene.sh --staged` over an index copy with only these ten specs staged. It exits 1 on a single finding, check 9: the build index is out of date, and a `gen_build_index.py --write` render clears it (`memory/LIVE.md` and the dRankedPlan and dWellOiledMachine `README.md` files). The brief leaves that to the main loop. No other finding names any of these specs.
- **Naming lexicon:** not run, since no new names were added.

| Spec | Rev now | Fork and pick | Sections moved | Bytes |
|---|---|---|---|---|
| wm1 | rev-4 | F4 (a) `principle.p36` | §4 Inventory, Files touched · §8 F4 | 44262 |
| wm2 | rev-4 | F4 (a) ask dKeptSession for a verb over a named kit's list | §2 S6 · §3 Edges · §8 F4 · §10 | 33960 |
| wm4 | rev-4 | F3 (b) ask dPlacedRequest for `request.py key -` (prompt on stdin) | §2 S1 · §3 Edges · §4 The hook · §8 F3 | 30318 |
| wm5 | rev-3 | F3 (a) ask dDeclaredLoop for the verb to print the found record's path | §2 S3 · §8 F3 | 30055 |
| wm6 | rev-4 | F4 (a) ask dPlacedRequest for a read-only epoch verb over `read_claims` | §2 S6, S7 · §8 F4 | 41326 |
| wm7 | rev-4 | F5 (a) ask dBoundRoles for `script` and `allow` on the work order | §2 S1 · §8 F3, F4, F5 | 35733 |
| wm11 | rev-4 | F4 (a) ask the playbook kit's owner for `--answers worktree_root`; F5 (a) `principle.p5` | §2 S2, S10 · §6 AC8 · §8 F4, F5 | 36176 |
| wm12 | rev-5 | F5 (a) `principle.p22` | §2 S11 · §6 AC10 · §8 F5 | 38803 |
| wm20 | rev-4 | F2 (a) `principle.p16` | §2 S4 · §6 AC7 · §8 F2 | 30893 |
| wm23 | rev-5 | F4 (a) `principle.p27` | §2 S9 · §6 AC8 · §8 F4 | 30110 |

**How the specs now read:**
- **Tag forks:** each tag is written into the leg's `[[gate_leg]]` row as `enforces = ["principle.pN"]`, in the list form PLAY-dOrderedCharter-7 S2 gives. The criterion that checks `enforces` now names the tag literally (AC8, AC10, AC7 and AC8 in specs 11, 12, 20 and 23). Spec 1 has no such criterion.
- **Ask forks:** every sentence that said "as §8 Fn picks" or "before the pick" now states the asked route. No backlog row was filed.

**Edits outside the named forks:**
- **wm7 F3** (agent-resolved earlier) used to say the list's carrier is "not the work order". Option (a) of F5 now makes the work order the carrier, so the sentence now says the carrier is the field asked of dBoundRoles' work order, not the work order as br3 renders it today.
- **wm7 F4** said "the open picks are theirs", pointing at wm43 F3 and wm30 F3. Group B resolves both under this same brief, so it now says those forks' asks were each resolved by the owner on 2026-10-29. Neither fork was re-resolved.

I did not add the template's `ratified <date>` header pointer: the corpus only adds it when a spec closes, and these stay `DEFERRED`. The revision lines written before rev-4 still say "(F4, open)" and similar, because they record history.

The index copy and the edit script are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-elastic-lalande-a8b091/bd0d7692-8d65-44a9-bf88-d3f42e06b8de/scratchpad/wm-fA/`. Nothing was committed or staged into the real index.

Files:
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-1.md`
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-2.md`
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-4.md`
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-5.md`
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-6.md`
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-7.md`
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-11.md`
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-12.md`
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-20.md`
- `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-23.md`

## The owner's picks, 2026-10-29: Group B, specs 26, 30, 32, 33, 39, 43, 48, 52 and 54

All nine Group B specs are revised and every named fork is resolved. Each spec is under the 49152-byte cap and dated 2026-10-29, still `DEFERRED`. None of them prints a named fork from `grep -n "Open for the owner"`.

I ran the hygiene gate over a copy of the index with only these nine specs staged. It exited 1, but its only failure is check 9: the build index is out of date, curable only by a `gen_build_index.py --write` render. The specs are named only in that render-owed line, which is yours to clear. The real index is untouched.

| Spec | Rev | Forks resolved (pick) | Sections moved | Bytes |
|---|---|---|---|---|
| 26 | rev-3 | F4 (a): ask dDeclaredLoop for the loop-kit read verb. F5 (a): ask dBoundRoles for `handoff.py shape-line` | S2, §8, §9 | 31215 |
| 30 | rev-3 | F3 (b): ask dBoundRoles for a `--json` mode of `handoff.py agents` | S4, §8, §9 | 26731 |
| 32 | rev-5 | F6 (b): ask dTotalRecall for an uncapped `record find --all` | S10, §8, §9 | 38501 |
| 33 | rev-6 | F4 (a): `principle.p35` on both legs' `[[gate_leg]]` rows | S8, AC4, §8, §9 | 38450 |
| 39 | rev-4 | F6 (a): `principle.p35` (F4 left alone) | S10, AC10, §8, §9 | 36292 |
| 43 | rev-4 | F3 (a), widened: ask for `handoff.py stage-rows`. F4 (a): ask for `handoff.py run-state`. F5 (a): this build adds `scope.py --self-chain` | S2, S7, S8, §4 Inventory and Files touched, §8, §9 | 39104 |
| 48 | rev-3 | F4 (a): this build adds `policy.py get --row` | S3, §4 Evidence, Inventory and Files touched, §8, §9 | 38448 |
| 52 | rev-3 | F3 (a): ask dPlacedRequest for the `node-` columns and a read-only `read_claims` verb | S5, §8, §9 | 28097 |
| 54 | rev-3 | F5 (a): this build adds `gen_build_index.py --units` | S1, S2, §4 Inventory and Files touched, §8, §9 | 32960 |

A few changes go slightly past the literal brief, so check them before you commit:

- **Spec 26, F4:** the verb's spelling now follows TOOL-dBoundRoles-3 §8 F5: `loop_lib.py declaration --item <tag> --json`, which exits 1 on an undeclared tag. Spec 26 had spelled it `declaration <item> --json` with exit 2. S2 still refuses on any non-zero exit, so its design is unchanged. The fork now says one ask, filed once, serves both, and this build files no second row.
- **Spec 43, F3:** to fit `driver` and `stage` in, the JSON shape changed to `{workflow: {"driver": d, "stage": s, "keys": {key: {"role", "fan", "cap"}}}}`. The fork names spec 54 S2 among its readers, filtering by those two fields. Spec 54 S2 now says its filter reads them from that same verb.
- **Specs 43, 48 and 54:** besides joining Files touched, each added verb also got a row in §4 Inventory (`--self-chain`, `--row`, `--units`).

The probe index copy and the gate's output are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-elastic-lalande-a8b091/bd0d7692-8d65-44a9-bf88-d3f42e06b8de/scratchpad/wm-fB/`. The full output is `hyg.txt` there.

Files are in `C:/projects/coding-governance/.claude/worktrees/elastic-lalande-a8b091/memory/builds/dWellOiledMachine/spec/`:
- 2026-10-26-spec-TOOL-dWellOiledMachine-26.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-30.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-32.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-33.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-39.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-43.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-48.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-52.md
- 2026-10-26-spec-TOOL-dWellOiledMachine-54.md
