**Serves:** research TOOL-dBoundRoles-1

# dBoundRoles — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns for the re-ground brief
[`2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground`](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground.md),
each copied from its agent transcript. The cross-check record they answer is
[`2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck`](2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md).

## Group A, items, actors and composition (specs 1, 2, 12, 14, 20)

All five Group A specs are revised. No row was refused, and every spec stays under the 49152-byte cap.

**Checks:**
- **Quoted sentences:** a `grep -n` for each sentence the record quotes from br1, br2, br12, br14 and br20 prints nothing.
- **Hygiene gate:** I ran it over an index copy with only these five specs staged. Only check 9 fires, which `python tools/memory-tree/gen_build_index.py --write` cures. That render belongs to you. Its drift also lists the dBoundRoles, dKeptSession and dTotalRecall READMEs.
- **Cleanup:** the index copy is deleted, and nothing is staged in the real index. My edit scripts are still in `.../scratchpad/br-wA/`.

| Spec | Rev | Rows | Bytes |
|---|---|---|---|
| 1 | rev-3 | 3, 8 | 32616 |
| 2 | rev-3 | 11 | 26438 |
| 12 | rev-3 | 25 | 21614 |
| 14 | rev-4 | 27 | 30260 |
| 20 | rev-3 | 33, 34, 35 | 36390 |

**Spec 1**
- **Moved:** S7 · §3 · §4 The registration · §4 The item arm · AC6 · §8 F6.
- **Row 3:** the item arm now grades every composed item, repository rows included and skipping none, citing dl24 S3 and layer-roles `[matrix]` FA-4. AC6 adds a repository item `item.build.adopter.ship` whose actor is `gov-deployer`.
- **Row 8:** `check_layer_roles` reads each role's slot and `layer` from `.claude/roles.json` as JSON data. That is the generated file option, read directly rather than through a subprocess; the playbook kit imports nothing from the roles kit.
- **New F6:** `RESOLVED (agent, 2026-10-26, delegated)`, choosing (a), the index.

**Spec 2**
- **Moved:** §8 F4 only.
- **F4 re-resolved:** `RESOLVED (agent, 2026-10-26, delegated)`. The tester's template becomes `outcome:code-miss|spec-wrong|answered, evidence:text, answer:text?`. The two-word judgment set stays, and `answered` covers the `test.reason` act.

**Spec 12**
- **Moved:** S2 · S3 · §3 · §4 Where the binding lives / Inventory / Files touched · §5 · AC1 · §7 · §8 F4.
- **Change:** `place` now runs a new roles-kit verb, `handoff.py check-return-file --role <slot> --file <file>`, as a subprocess. That verb runs `validate_return` and S3's marker-role check.
- **The name:** the brief suggested `validate-return`, but the naming lexicon refuses `validate` (the declared verb is `check`). `check-return` is already unit 5's verb for hook payloads.
- **New F4:** `RESOLVED (agent, 2026-10-26, delegated)`, choosing (a), the verb.

**Spec 14**
- **Moved:** S2 · S3 · §4 The extractors / Inventory / Files touched / Alternatives rejected · §5 · AC1 · §8 F5.
- **Change:** both extractors run a new `check_roles.py --print-tag-rows role|stage` as a subprocess, with the blob's text on stdin.
- **AC1:** now also greps `tag_index.py` for a roles-library import.
- **br14:233 re-checked:** the rejection of importing `roles_lib` still holds, and now also cites the sibling-kit rule.
- **New F5:** `RESOLVED (agent, 2026-10-26, delegated)`, choosing (a), the verb.

**Spec 20**
- **Moved:** S2 · S3 · S6 · §3 · §4 The actor patch / Inventory / Files touched · §5 · AC6 · §8 F3, F6, F7.
- **Row 35:** S2 now says the kind rows are dl6 S1's and names their `binds`, `population`, `factory` and `gate`. The `roles catalogue` leg's `enforces` comes from dl6 S9. This unit adds only `schema`, so `enforces` does not change.
- **Row 33:** S3 composes through the playbook kit's `compose` verb as a subprocess. With the playbook kit absent, it returns gov's rows and prints a note.
- **Row 34:** S6 is now a roles-kit verb, `check_roles.py --check-actor-patch <file>`, that `loop_items.py` runs as a subprocess.
- **F3 re-resolved:** `RESOLVED (agent, 2026-10-26, delegated)`.
- **New F6, left open for you:** recommends (a), so it follows dl26 F5. The ask is dl26 F5's `compose` verb, with `kind.role` and `kind.workflow` named among its callers.
- **New F7, left open for you:** recommends (a). The ask is "TOOL-dDeclaredLoop-24 S4: `check_item_composition` runs `check_roles.py --check-actor-patch` as a subprocess for each item whose composed actor is a repository role, a refusal naming the item".

**Decision for you:** in specs 1, 12 and 14 I marked the new forks resolved rather than open. The verbs live in the roles kit, which this build owns, so none needs a change from a parent. Re-open them if you want them in front of the owner.

**Parent specs that look wrong:**
- **dl6 S1:** the `kind.role` population is `tools/roles/agents/*.agent.md` alone. dl24 S1 includes the overlay's rows in its item population, so repository roles are missing from oc7 S5's "whole population both ways" read. dl6's data model also never states `kind.workflow`'s `binds`.

**Coordination notes:**
- **Group B, br22 F2:** spec 20 does not add `kind.role` or `kind.workflow` to dl27's `activatable` list.
- **Group B, br43:** it builds on spec 12's `place`, so its transcript verb on `handoff.py` should sit beside `check-return-file`.
- **Unchanged in spec 2 (not a record row):** wb23's `returns` line says one judgment per red, but the template's single `outcome` cannot hold several reds in one return.

Files:
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-1.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-2.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-12.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-14.md
- C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-20.md

## Group B, policy reads and the placement return (specs 5, 11, 21, 22, 43)

All five Group B specs are revised, and no record row was refused. The hygiene gate, run over an index copy with only these five specs staged, named none of them for anything except check 9. That is the build-index render that `python tools/memory-tree/gen_build_index.py --write` cures (it also names the stale `dBoundRoles`, `dKeptSession` and `dTotalRecall` READMEs), so I left it for you. The index copy is deleted and the real index was never touched. In the lexicon, `read_policy_setting` and `read_agent_limit` pass. `with_default` is a parameter and `agent-return` is a CLI verb, and the lexicon grades neither kind of name. Every grep for a sentence a row quotes now prints nothing, except row 51's. That sentence stays because it is still true, and it now goes on to name the subprocess route.

### TOOL-dBoundRoles-21 (row 36)
- **Rev:** rev-3, 2026-10-26, still DEFERRED. 27532 bytes.
- **Sections moved:** S1, §3, §4 Alternatives rejected, §5, AC7, §8 F2, §9, §10.
- **S1:** `read_policy_setting` now runs `policy.py get <key> --json` as a subprocess. I checked that `cmd_get` at `tools/policy/policy.py:1332` exists with `--rev`, `--explain` and `--json`, and that `--json` prints value, source and reason.
- **New keyword, `with_default`:** this is the one design consequence beyond the row. Spec 43 makes `read_policy_setting` the only caller of `get`. Spec 22's agent limit, unit 5's retries and unit 11's key all need the catalogue default, so the function needs a way to return it.
- **AC7:** gains `git grep -nwE '(from|import) policy' -- tools/roles`, which prints nothing on today's tree.
- **F2:** re-resolved to (a), the subprocess per key: `RESOLVED (agent, 2026-10-26, delegated)`, rung 1, citing TOOL-dDeclaredLoop-18 §4 and PLAY-dOrderedCharter-7 §4 "The policy reads". Pinning one `--rev` per run is rejected because no `policy.py` verb prints the landed revision whole; `get`'s reason gives only a sha8, in prose. So it would need a second remote ladder.

### TOOL-dBoundRoles-5 (row 14)
- **Rev:** rev-3. 25572 bytes. Sections moved: S4, AC5, §9.
- **Change:** `roles.retries` is read with `policy.py get` as a subprocess through `roles_lib.resolve_kit_dir(..., KIT_DIR)`, the way br15 S6 reads its key. `KIT_DIR` exists at `tools/roles/handoff.py:90`. No fork added.

### TOOL-dBoundRoles-11 (row 18)
- **Rev:** rev-3. 26711 bytes. Sections moved: S5, §3 Edges, §4 The reader, §9.
- **Change:** the key is read with `policy.py get run.on-owner-question --rev <rev>` as a subprocess.
- **New refusal:** a `get` exit 2, or no policy kit found, now refuses and names the key or the kit. No fork added.

### TOOL-dBoundRoles-22 (rows 40, 41, 42)
- **Rev:** rev-3. 24076 bytes. Sections moved: S5, §3, §4 The row and The cap, §5, AC4, §8 F2 and F5, §9.
- **F2, re-opened as the brief asks:** OPEN for the owner, recommendation (a): unit 20 adds `kind.role` and `kind.workflow` to dl27's `activatable` list, against (c): the scenario half recorded unowned. The claim about unit 20 is dated to `c8d46e188`, since Group A is revising spec 20 now.
- **F5, new:** OPEN for the owner, recommendation (a): an ask of dDeclaredLoop for `upstream.py kinds`. dl29's only verbs are `rows`, `join --write` and `--fixture`, so nothing prints S3's set of row kinds. AC4's third R9 line waits on that ask; until it lands, the `seg`-shape fallback runs with its note.

### TOOL-dBoundRoles-43 (rows 49, 50, 51)
- **Rev:** rev-5. 48756 bytes, leaving 396 bytes for the generated records region to grow.
- **Sections moved:** S10, S21, S23, S43, S56, §3, §4, AC21, AC23, AC43, AC56, §8, §9.
- **S43 and S56:** placement now runs a new roles-kit verb, `handoff.py agent-return --agent <id> [--session <file>]`, as a subprocess. It finds the session through `resolve_session_file`, as the `agents` verb does.
- **S21 and AC21:** `read_policy_setting` is the only caller of `get` in the roles kit, and AC21 reds an import.
- **S23 and S10:** both now reach `write_overlay_units` through a playbook verb run as a subprocess.
- **F17, new:** OPEN for the owner, recommendation (a): an ask of dOrderedCharter for an `overlay.py` write verb. I rejected two alternatives:
  - This unit adding the verb itself would put a write surface on another build's module without that build.
  - oc15's `instructions_edit.py rename` writes nothing under the default `instructions.edit`.
- **Trims to get under the cap, no design moved:**
  - I cut the 44 one-line titles of the §2 items; each item's text still states what it does.
  - I cut `widens: none · relaxes: none` from the rung-3 forks; the build README asks it only of rung 5 and 6 choices, and no tool reads it.
  - I tightened §4 "Why two units" and one non-goal.

### Parent specs that look wrong
- **oc31 S4 and oc49 S11:** their govkit step programs, `tools/govkit/steps/adopter_rules_to_overlay.py` and `census_to_overlay.py`, write through `write_overlay_units` but name no route. wb28:63-64 (rev-3) bars a govkit module from importing a playbook module, and oc32 gives `overlay.py` only `check` and `--fixture`. It is the same gap as br43 F17, so the ask there would serve all three steps.

Files:
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-5.md
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-11.md
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-22.md
- C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-43.md

## Group C, the guard and the legs (specs 3, 6, 23, 25, 60)

All five Group C specs are revised. No record row was refused: re-reading both sides bore out rows 12, 15, 43, 44, 45 and 53. The staged hygiene run over an index copy holding only these five reports one failure, check 9 (a build-index render is owed). It names no defect in any of the five; the main loop's `gen_build_index.py --write` clears it. Check 25 flagged spec 25 S5 once because of the word "retired"; I reworded it and the re-run was clean. I deleted the index copy and the `br-wC` folder afterwards, and nothing was staged into the real index.

| Spec | Now reads | Bytes | Rows |
|---|---|---|---|
| 3 | rev-3 | 24393 | 12 |
| 6 | rev-3 | 27560 | 15 |
| 23 | rev-4 | 27437 | 43 |
| 25 | rev-5 | 48406 (under the 49152 cap) | 44, 45 |
| 60 | rev-6 | 33674 | 53 |

**Spec 3**, `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-3.md`
- **Sections moved:** S1, §8 F5, §9.
- **S1** now names the verb it runs, `loop_lib.py declaration --item <tag> --json`. It states that TOOL-dDeclaredLoop-9 has only `--check` and `--fixture`.
- **New fork F5, open for the owner:** the ask to dDeclaredLoop for that verb. Recommended: (a) the ask. The alternatives are (b) parsing `--check`'s printed output and (c) a `requires_if` row on `tools/roles/kit.toml`.
- **F4 left as it was.** The brief said F4 should become this fork, but F4 is RESOLVED and still covers the other unbuilt parents (dl9 S2 and spec 2's `return` field). Converting it would re-open a fork, so I added F5 instead.

**Spec 6**, `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-6.md`
- **Sections moved:** S1, S2, §3 Edges, §4 "The guard's admitted shape" and Rollout, AC2, §8 F4 and F5, §10, §9.
- **S2** names `tools/loop/guard.py --staged` as the pre-commit verdict. Because dl2's guard-self step refuses any agent commit to `guarded-paths.txt`, the list's two new lines become the owner's terminal commit.
- **§4** gains a table of the admitted shape under each `policy-file.guard` value.
- **AC2** adds the same two exits through the loop kit's guard.
- **New fork F4, open for the owner:** whether the step 5a arm or dl2 S10's policy-path arm answers a write to the render paths. Recommended: (a) step 5a runs first and the policy-path arm passes over the render paths. The ask goes to dl2 S10.
- **New fork F5, open for the owner:** how a re-render is admitted under `agents-with-reason` and `agents-within-mandate`. Recommended: (a) an ask to dDeclaredLoop for a step in its verdict that answers the render paths under every value.

**Spec 23**, `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-23.md`
- **Sections moved:** S5, S6, §3 (non-goal and Edges), §4 "The floor" and "Alternatives rejected", AC5, AC6, §8 F3, §9.
- **S6** cites dl2's verdict and states the outcome under each guard value. AC5 adds a fixture for each of the two non-default values.
- **F3 re-resolved, marked `RESOLVED (agent, 2026-10-26, delegated)`, on rung 1 naming TOOL-dDeclaredLoop-2:** I picked (c). The floor admits a policy-file level below medium only while `policy-file.guard` is `owner-only`, read from the same file.
- **Flag for the owner:** (c) adds one key read to `check_effort_floor`. The other choice was to keep (a) and just state the limit. That would let an agent's recorded change set a level below medium under the two non-default values, which goes against the clause "only by the owner's explicit write". If the owner prefers that relaxation, F3 should be reconsidered.

**Spec 25**, `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md`
- **Sections moved:** S4, S5, S8, §4 Disposition, Readers disposed, Inventory and Files touched, new AC18, §8 F3, §9.
- **The renamed leg** is now an `[[exempt_leg]]` row in `tools/govkit/registry.toml`, written with `leg_factory.py new --exempt`. Its `enforces` is `agent-cap self-test`'s, as dWitnessedBar-11 S6 writes it, and the manifest is regenerated rather than edited.
- **Standing under `core.bypass = never`:** S5 states that the guarded leg reds under `never` while wb11 F5 is open.
- **Stop rule:** S5 stops the unit if `agent-cap self-test` is still on the pending list, since that list only shrinks.
- **The cross-kit require** of `scratch-guard.js` is declared as a `requires_if` row naming `agent-cap`.
- **F3 re-resolved, marked `RESOLVED (agent, 2026-10-26, delegated)`, on rung 1 naming PLAY-dOrderedCharter-7:** the pick stays (a), now with that declared edge. I added option (d), the `tools/lib/` inline block, and rejected it. It would move only the two exports, not rule 6's index readers. Also, the parity loop at `tools/lib/resolve-python.test.sh:226` only reads `#` markers in `.sh` and `.py` files.

**Spec 60**, `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md`
- **Sections moved:** §1 table, S20, §4 Evidence and Files touched, AC12, §8 F5, §9.
- **The guard** is widened in the leg's `[[exempt_leg]]` declaration, which keeps the `enforces` wb11 S6 wrote. The manifest is regenerated with `leg_factory.py --write`, and AC12 adds `--check`.
- **F5 re-resolved, marked `RESOLVED (agent, 2026-10-26, delegated)`, on rung 1 naming TOOL-dWitnessedBar-11.**

**Things that look wrong but are outside my rows (not edited):**
- **Spec 6 S2's directory line probably guards nothing.** It adds `.claude/agents/` as a directory line, but `guarded-paths.txt` holds one exact path per line. `tools/policy/guard.py:87` matches with `path in guarded`, and the `.githooks/pre-commit` block uses `grep -xF`. So agent files would go unguarded at commit unless the list format is taught a prefix. This was already the case before the re-ground.
- **dl2 S10** says "whose path is listed" without saying whether that means an exact or a prefix match, and F4 depends on the answer.
- **Same cross-kit pattern, not raised by the record:** `tools/hooks/agent-cap.js:465` loads the policy kit's `policy-mirror.js` in process, which is the interface dGroundRules-5 designed. Spec 25's pack inherits that through its plain `requires` on the policy kit. Separately, dFairHearing-16's `spec-audit-optin.js` reads `scratch-guard.js` from the hooks kit the same way.
