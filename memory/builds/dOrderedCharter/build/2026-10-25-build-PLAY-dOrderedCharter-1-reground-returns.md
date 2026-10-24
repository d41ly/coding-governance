**Serves:** research PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55

# The re-ground's spec writers: their returns

Five gov-spec-writer agents, one per group of the brief `memory/builds/dOrderedCharter/prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md`, each given follow-ups by the main loop. Each section below is that agent's end-of-turn text, in order, extracted from its subagent transcript by script, never retyped. Headings inside a return are demoted so this record keeps its own outline.

## Group A, caps, led by unit 11

### Return 1

I revised all five Group A specs (2, 3, 6, 11, 34). Each stays `DEFERRED`, dated 2026-10-24, with one new §9 line that cites the cross-check record. The hygiene gate, run over an index copy with only these five staged, names my specs for one thing only: check 9, the build-index render owed for `memory/builds/dOrderedCharter/README.md`. Only `python tools/memory-tree/gen_build_index.py --write` cures that, so it's yours. I deleted the index copy afterwards and staged nothing into the real index.

Per spec:

- **PLAY-dOrderedCharter-11** — rev-3 · 26903 bytes.
  - **Sections moved:** S2, S3, S4, §3 Edges, §4 Migration, Rollout and Files touched, AC6 (new), §8 F2 and F4, §10.
  - **Changes:** caps are read with `budgets.py resolve`, each named by its census row in `tools/policy/caps.toml`. The role block reads only `role-body`'s mode. `CODEX_MAX` is read through the `codex-instructions` census row. `instructions.checks` is read with `policy.py get`, in the call shape the reader-coverage arm counts. Its existing catalogue row is filled and drained, and the regenerated mirror goes in a second commit. The roles kit now runs `load_sets.py` as a subprocess, because a kit may not import a sibling kit.
  - **Forks:** F2 re-resolved to (d), `RESOLVED (agent, 2026-10-24, delegated)`. F4 added, covering what happens when a reader exits 2 or the policy kit is absent: (a), `RESOLVED (agent, 2026-10-24, delegated)`.
- **PLAY-dOrderedCharter-2** — rev-4 · 32115 bytes.
  - **Sections moved:** S2, S9, §3 Edges, §4 Rollout and Files touched, §5, AC2, AC7, AC8 (new).
  - **Changes:** `charter.override` is read with `policy.py get`, and its row is filled and drained. AC2's invalid value now refuses because the scratch target has no valid revision to fall back to. `AGENTS.md` is measured with `budgets.py resolve`, and a crossing is raised on `budgets."AGENTS.md"` in the guard's one admitted shape. `.governance/policy.toml` and `memory/DECISIONS.md` replace the limits file in Files touched.
  - **Forks:** none.
- **PLAY-dOrderedCharter-3** — rev-4 · 27492 bytes.
  - **Sections moved:** S7, §3 Edges, §4 Files touched, §5, AC7.
  - **Changes:** the guard admits exactly one changed leaf per commit, so the two raises (`UNATTENDED-PROTOCOL.md` and the kickoff `SKILL.md`) land in two commits, each with its document's envelope. A document with no census row has no cap, and this unit adds none, because a new cap is the owner's. I added external consumes-from edges for dSafePassage unit 1 and dGroundRules units 9 and 6.
  - **Forks:** none.
- **PLAY-dOrderedCharter-6** — rev-4 · 26122 bytes.
  - **Sections moved:** S6, S7, §3 Edges, §4 Rollout and Files touched, AC6, AC7, §7 (New arm line), §8 F4, §10.
  - **Changes:** S6 reads both caps through `budgets.py resolve`, the rows having been moved by dSafePassage's step. `CODEX_MAX` is read through its census row. S7's sentence moves to `help/charter.md`. AC6's scratch cap now sits in a committed policy file, because the `LIMITS` override is retired.
  - **Forks:** F4 added (where S7's sentence goes): (a), `RESOLVED (agent, 2026-10-24, delegated)`.
  - **Grep:** one `template-size-limits` hit remains, in the §10 recall query, which is history.
- **PLAY-dOrderedCharter-34** — rev-4 · 33714 bytes.
  - **Sections moved:** S3, §3 Edges, §4 Budgets and harness limits, §8 F6, §10.
  - **Changes:** the cap is now `budgets."AGENTS.md"`, read through `budgets.py resolve`, and the harness limit comes from `CODEX_MAX`'s census row.
  - **Forks:** F6 re-resolved, `RESOLVED (agent, 2026-10-24, delegated)`.

No fork in my group is left open for you. I did not re-open specs 3 and 6's F3: their chosen options still stand, though their reasons cite the old file's four conditions.

Things that look wrong or missing:

1. **dGroundRules unit 9 has no reader for a consumer cap's home.** `budgets.py resolve` only gives back a `constant:` value the caller passes in. So specs 6 (shell) and 11 (Python, which spec 34 uses) each parse the `codex-instructions` row themselves. That is two readers of one census row. A `budgets.py` verb that prints a row's home would make it one, and that would be an ask to dGroundRules.
2. **The census home forms don't match.** dGroundRules unit 9's data model lists four `home` forms, but dSafePassage unit 1 S8 moves the seven `limits:` rows to a `policy` form that unit 9 never defines.
3. **Specs 2 and 11 depend on spec 9's naming.** Both read their key through unit 9's `policy_reader`. Spec 2 has no §3 edge to unit 9, and adding one needs the matching edge in spec 9, which is Group B's file, so I named the dependency in S2's text only. Both also assume Group B keeps the name `policy_reader`.

The edit scripts are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-thermostat-power-issue-370c51/784b9d4d-3d6b-441c-87c6-b603e2cf2649/scratchpad/dA/`.

Files are in `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/`:
- `2026-10-23-spec-PLAY-dOrderedCharter-2.md`
- `2026-10-23-spec-PLAY-dOrderedCharter-3.md`
- `2026-10-23-spec-PLAY-dOrderedCharter-6.md`
- `2026-10-23-spec-PLAY-dOrderedCharter-11.md`
- `2026-10-23-spec-PLAY-dOrderedCharter-34.md`

### Return 2

I restored the token in spec 6, but I couldn't confirm the fix with `python tools/check-spec-tokens.py`. The scratch-guard hook blocks this role from running it (my allowlist is only "memory hygiene" and "lexicon naming predicates"), so you'll need to run it in the main session.

**What I checked instead:** the literal `tools/template-size-limits.txt` now appears in spec 6 S6 at line 77 (and in the §9 rev-4 line at 275). Spec 6's header still reads `**Carries:** cl-dClosedLoop-0036@3667f2f3 whole`. That should clear the `carries <- token:cl-dClosedLoop-0036` finding, but the gate is the real test.

The line changed, in S6 (`2026-10-23-spec-PLAY-dOrderedCharter-6.md`):
- Before: ``former limits file into `.governance/policy.toml` (TOOL-dSafePassage-1 S7, S8), and both caps are``
- After, the sentence now reads: ``…the `AGENTS.md` and template rows `tools/template-size-limits.txt` held until dSafePassage's step moved them under `budgets.*` in `.governance/policy.toml` and removed the file (TOOL-dSafePassage-1 S7, S8), and both caps are held.``

As you asked, there is no rev bump: the existing §9 rev-4 line gains one clause, "S6 names `tools/template-size-limits.txt` as the rows' former home, keeping `cl-dClosedLoop-0036`'s token in its carrier."

The spec is now 27251 bytes, under the 49152 cap.

I staged and committed nothing. `git diff --cached` does show `memory/LIVE.md` and `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` in the real index. I didn't stage those, so another session must have.

File: `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-6.md`

### Return 3

I dropped " and removed the file" from spec 6 S6, and the hygiene gate now passes: exit 0, with no check 25 finding and nothing failed.

- **Sentence now:** "…the `AGENTS.md` and template rows `tools/template-size-limits.txt` held until dSafePassage's step moved them under `budgets.*` in `.governance/policy.toml` (TOOL-dSafePassage-1 S7, S8), and both caps are held." The `tools/template-size-limits.txt` token is still there.
- **How I ran the gate:** I copied the index and reset the copy to HEAD with `git read-tree HEAD`, then staged only spec 6 into it. The real index held other sessions' staged files, so a plain copy would have graded those too. I deleted the copy afterwards.
- **Byte count:** 27230, under the 49152 cap.

No rev bump, nothing staged in the real index, no commit.

File: `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-6.md`

### Return 4

I put the `budgets.py home <cap>` verb in spec 6, not spec 11 as you and the brief said. Spec 6's check is the verb's first caller and lands at order 19, before spec 11 at order 21. The hygiene gate's edge arm reds a **consumes-from** edge whose target lands later, so spec 6 can't wait for spec 11. Specs 11 and 34 now call the verb, and neither spec 6 nor 34 parses `caps.toml`. If you'd rather spec 11 own it, the order has to change first. I recorded the choice as spec 6's §8 F5, `RESOLVED (agent, 2026-10-25, delegated)`.

Hygiene, run over an index copy reset with `git read-tree HEAD` and only these three specs staged, has one finding: check 9, the build-index render for `memory/builds/dOrderedCharter/README.md`. Only `gen_build_index.py --write` cures it. The new pair of edges (spec 6 hands off to spec 11, spec 11 consumes from spec 6) runs in landing order. The gate holds edge joins under `--staged`, so the full join gets checked at the push run. I deleted the copy, staged nothing in the real index, and made no commit.

The lexicon has no CLI-verb cell: `--as cli.verb` comes back MALFORMED. Asked as `py.function`, `home` gets "not in the declared table", which the lexicon calls a scoping question rather than a spelling one. The function behind the verb, `read_cap_home`, answers OK as `py.function`.

**Spec 6 — rev-5, 2026-10-25, DEFERRED, 33136 bytes**
- **S9 (new):**
  - **Output:** the verb prints `<cap>\t<home>\t<value>`. For a `constant:` home, the value is the integer on the line that the built `derive_home_line` (and its `SHELL_KEY` pattern) finds; for any other home it prints `-`.
  - **Refusals:** it exits 2 for a cap with no census row, or a home with no matching line.
  - **Comes with it:** a `budgets-home` case in `CASES`, a line on `help/size-caps.md`, and the policy kit's version marker moves.
- **S6:** reads `CODEX_MAX` with `budgets.py home codex-instructions`.
- **Also moved:**
  - §3: a hands-off edge to spec 11, and the dGroundRules external edge now names `budgets.py`, `derive_home_line`, `CASES` and the version marker.
  - §4 Inventory and Files touched; §5 user docs.
  - AC8, new: fixture plants and a probe that `codex-instructions` prints 32768.
  - §7: `policy check`, `policy fixtures` and `kit version markers` added, plus a new `check_policy.py --fixture` arm.
  - §8 F5 (new); §9.

**Spec 11 — rev-4, 2026-10-25, DEFERRED, 30625 bytes**
- **S3:** `CODEX_MAX` is read with `python <prefix>/policy/budgets.py home codex-instructions`.
- **Also moved:** a §3 consumes-from edge to spec 6, and §9. It still reads load-point cap names from the census with `tomllib`; item 6 only covers the home.

**Spec 34 — rev-5, 2026-10-25, DEFERRED, 37227 bytes**
- **Moved:** S3, §4 Budgets and harness limits, §8 F6 (wording only, same resolution), §10 and §9. Each now reads `CODEX_MAX` with `budgets.py home codex-instructions`.

Most of the growth in specs 11 and 34 is records rows the main loop rendered in between. All three are under 47000 bytes.

`grep -n 'budgets.py home'` prints the verb in spec 6 and the calls in specs 6, 11 and 34. That differs from the brief's acceptance line, which expects the verb in spec 11.

Files are in `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/`:
- `2026-10-23-spec-PLAY-dOrderedCharter-6.md`
- `2026-10-23-spec-PLAY-dOrderedCharter-11.md`
- `2026-10-23-spec-PLAY-dOrderedCharter-34.md`

## Group B, keys, led by unit 1

### Return 1

All seven Group B specs are revised: 1, 4, 7, 9, 14, 20 and 27. Each Status line is bumped with the status kept `DEFERRED`, and each has a new §9 line naming the sections moved and the cross-check record.

**Acceptance checks**
- **Stale wording:** `grep -e 'until it lands' -e 'template-size-limits'` finds nothing in any of the seven. The other "until then" hits are about non-parent topics (the IW-1 legacy list, `playbook parity`, `memory.code-roles`).
- **Size:** all seven are under 49152 bytes.
- **Hygiene:** I ran the hygiene gate over an index copy with only these seven staged, then deleted the copy. None of my specs is named as failing. The only failure is check 9, the build-index render: it names `memory/builds/dOrderedCharter/README.md` and spec 25 as stale, and spec 1 as an input the render owes. A `gen_build_index.py --write` render cures that, so I left it for you.
- **Naming lexicon:** the two new names pass, `read_policy_value` as `py.function` and `PolicyRefused` as `py.type`.

**One design addition: a single policy-reading helper.** The reader-coverage arm only counts a call whose first argument is the key as a string literal. A plain `subprocess.run([...,"get","key"])` doesn't match. So spec 7's §4 has a new section, "The policy reads", that defines the contract for `read_policy_value(key, root, rev=None)` and `PolicyRefused` in `tools/playbook/policy_value.py`. The helper runs `policy.py get <key> --explain` as a subprocess, finding the policy kit through its own inline `resolve_kit_dir`. Whichever playbook-kit pass reads a key first defines the module, following dSafePassage unit 9's rule for govkit's helper. Specs 1, 9, 14, 20 and 27 call it, and the matching edges are written on both sides within the group.

**Per spec**

| Spec | Rev | Bytes | Sections moved | Forks |
|---|---|---|---|---|
| 1 | rev-4 | 31332 | S4, new S8 · §3 Non-goals, Edges · §4 Rollout, Files touched · §5 · AC8, AC9 · §7 New arm · §8 · §10 | F4 added, open |
| 4 | rev-3 | 24615 | S2 · §3 Non-goals · §4 The verb, The preset line · AC1 · §8 F3 evidence | F3's evidence replaced; its mark is unchanged |
| 7 | rev-4 | 35898 | S9, S10, S11, new S12 · §3 Edges · §4 The policy reads (new), Inventory, Rollout, Files touched · §5 · AC9, AC10, AC11 · §7 · §10 | none |
| 9 | rev-4 | 23924 | S4 · §3 Edges · §5 · AC5 | none |
| 14 | rev-3 | 26702 | §3 Edges · §4 Measuring and detecting, Inventory · §5 · AC2 · §8 F1 | F1 re-resolved |
| 20 | rev-4 | 32293 | S8 · §3 Edges · §4 Rollout, Files touched · §5 · AC8, AC10 | none |
| 27 | rev-3 | 15280 | S2 · §3 Non-goals, Edges · §5 · AC1 · §7 New arm | none |

- **Spec 1:** on the derived-default refusal alone, the render takes the catalogue's `foundation` set and prints a line saying so; any other exit 2 refuses the render. F4 is marked FACT-QUESTION, recommending option (a): probe the landed row's `allowed`, and file an ask to dGroundRules if it refuses a practice tag. The `charter.practices` row is filled and drained in one commit, with the mirror in a second commit.
- **Spec 4:** the preset line now reads `preset — none: presets join the policy reader at dKeptSession; a key's source: policy.py get <key> --explain`.
- **Spec 7:** `owner-only-expiring` now points at spec 15's §8 owner-proof fork, and admits no record until a pass lands that proof. A refused read reds the gate. Both rows are filled and drained. The "python resolver" leg is added to §7 because the new module carries an inline `resolve_kit_dir` copy.
- **Spec 9:** `policy_reader` wraps `read_policy_value`. A list renders one member per line, and an exit 2 refuses the render naming the key. The spec now says a `policy:<key>` unit is no reader for coverage.
- **Spec 14:** F1 is `RESOLVED (agent, 2026-10-24, delegated)` on rung 1: the systems record's `:570`, beside the `memory.load-budget` row at `:569`, defines a k as 1,000 bytes. `LOAD_BUDGET_DEFAULT` is gone, the default moves from 8192 to 8000 bytes (§9 says so), and a refused read prints a `memory — skipped:` line.
- **Spec 20:** a refused read reds the gate, and `instructions.legacy` is filled and drained.
- **Spec 27:** the wait for the catalogue row is gone and a refused read refuses. The row's summary and usage are left to dFurnishedOrders, its owner.

**Things that need you or another group**
1. **Helper coordination across groups.** Group D's specs 19, 26 and 25 (orders 4, 9 and 10) read keys under `tools/playbook/` before spec 7 (order 11). The specs in groups A and C that read keys under `tools/playbook/` should also call or define this same helper, or the kit ends up with a second one. Code under `tools/roles/` cannot import the playbook kit and needs its own reader.
2. **A gap in spec 7, not from the re-ground.** Its exception record carries no `Proof` field, so "written through the door's owner path" leaves the register nothing to check. Spec 15's change record does carry `Proof`.
3. **Possible parent problem.** dGroundRules unit 1, `:69-71`, says the value check refuses a member v2 admits only as "repo-declared". `charter.practices`'s Allowed cell (v2:1143) is "catalogue or repo-declared practices". So the landed row may refuse every practice tag, which would also make spec 1's S8 `usage` line refused. That is spec 1's F4.
4. **Minor.** The cross-check record's rows 47–48 call the `16k` and `8k` values "pattern strings". v2:1369 gives `memory.load-budget` a closed list of values (`4k, 8k, 16k`).

The spec files are in `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/`, named `2026-10-23-spec-PLAY-dOrderedCharter-<n>.md`. My edit scripts and the hygiene output are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-thermostat-power-issue-370c51/784b9d4d-3d6b-441c-87c6-b603e2cf2649/scratchpad/dB/`.

### Return 2

I applied the owner's picks to specs 1 and 7. Both stay `DEFERRED`, and each has a §9 line naming the brief `2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks`. Nothing is staged in the real index and nothing is committed.

**Spec 1: rev-5, 2026-10-25, 35623 bytes**
- **Status line:** the rev is bumped and `ratified 2026-10-25` is added at the end.
- **§8 F4:** marked `RESOLVED (owner, 2026-10-25): (a).`, with the `FACT-QUESTION` label and the probe kept. I added the evidence, read with `git show` from `origin/branch/unattended-dgroundrules-e47ae1` at `df4912bd`, with no checkout:
  - `tools/policy/catalogue.toml:22-26` holds the row as `{ type = "set", item = "[A-Za-z0-9][A-Za-z0-9_.-]*", registry = "catalogue or repo-declared practices" }`, with `empty = "never"` and a derived default.
  - `check_value` (`tools/policy/policy.py:142`, set branch at `:159-171`) admits any member the `item` pattern matches. So `practice.yagni` passes and the probe should read source `file`. It still decides at the build run.
- **§9:** the rev-5 line follows rev-4 (item 5).

**Spec 7: rev-5, 2026-10-25, 39410 bytes**
- **S9:** `owner-only-expiring` now names the settled proof, stderr being a terminal, tested through spec 15's check (its §8 F4, which the owner resolved), never one of spec 7's own. It still admits no record until that check lands, since spec 15 builds at order 16 and spec 7 at order 11.
- **§3:** the hands-off edge to spec 15 and the §5 security line now say the same thing; neither points at an open fork any more.
- **§9:** the rev-5 line follows rev-4 (item 2).

**Hygiene:** I ran it over an index copy reset with `git read-tree HEAD`, with only these two specs staged, then deleted the copy. The only failure is check 9, the build-index render. It says spec 1 owes a render and that `memory/builds/dOrderedCharter/README.md` is stale. A `gen_build_index.py --write` render cures both, so I left them for you.

The edit script and hygiene output are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-thermostat-power-issue-370c51/784b9d4d-3d6b-441c-87c6-b603e2cf2649/scratchpad/dB/` (`f17.py`, `hyg2.out`).

## Group C, overlay and update, led by unit 32

### Return 1

I revised all six Group C specs. Each is still `DEFERRED`, carries a new §9 line naming the sections moved and the cross-check record, and stays well under the 49152-byte cap. The three acceptance checks pass:

- **Grep:** `until it lands` and `template-size-limits` now appear only in history lines.
- **Hygiene gate:** run over an index copy with only my six specs staged, it names none of them. Its one failure is check 9: the build-index render is owed, and `memory/builds/dOrderedCharter/README.md` and spec 25 (Group D's) differ from a fresh render. That is yours to fix with `gen_build_index.py --write`. The index copy is deleted.
- **Naming lexicon:** passes on the two Python names involved, `read_overlay_policies` and `run_unit_drift`.

### Per spec

**PLAY-dOrderedCharter-15**: rev-4, 34104 bytes
- **Moved:** §2 S5, S10 and a new S11 · §3 Edges · §4 Rollout and Files touched · §5 security · AC3 and a new AC12 · §8 F4 (new) · §10.
- **Changes:** `tty-cli` now tests standard error, the same stream as the guard's hook (`[ -t 2 ]`). The spec says this once, and AC3 now says standard error. Both keys are read with `policy_reader("instructions.edit")` and `policy_reader("instructions.proof")`, and an exit 2 from the reader refuses every verb at load. S11 fills both landed rows and drains the list, with the mirror in a second commit.
- **Fork:** F4, how the command proves `tty-cli`, is open for the owner. Options (a), (b) and (c) are as you specified; it recommends (a). Spec 7 should point at "spec 15 §8 F4".

**PLAY-dOrderedCharter-32**: rev-3, 33893 bytes
- **Moved:** §2 S7 · §3 non-goals and Edges · §4 The policy keys, Inventory and Files touched · §5 risks · AC8 · §8 F4 and F5 · §10.
- **Changes:** S7's read now lives inside the policy kit as `read_overlay_policies(repo, sha)` in `tools/policy/policy.py`. It reads the overlay's blob through `read_blob_at`, and its rows are seen by the key-to-row matcher, `validate`, `arm_schema` and the mirror. A `[[policy]]` key outside `adopter.` is refused, so the overlay cannot redeclare a catalogue key. Spec 32 still owns the row grammar; the policy kit parses only the `[[policy]]` tables, and `read_overlay` reads only each row's `key`, for its tag.
- **AC8 rewritten:** under dGroundRules unit 4, an out-of-set value makes the whole file fall back to its last valid revision rather than refusing. AC8 now observes the refusal (exit 2) only where the bad file is the only revision.
- **Forks:** F5 re-resolved on rung 1, naming dGroundRules units 1, 2 and 4, marked `RESOLVED (agent, 2026-10-24, delegated)`. In F4 I replaced only the false "files the admission ask" clause; its choice and original mark stand.

**PLAY-dOrderedCharter-33**: rev-3, 31537 bytes
- **Moved:** §2 S3, S7 and a new S8 · §3 Edges · §4 The walk and the modes, Inventory, Rollout and Files touched · §5 risks · AC4, AC9 and a new AC10 · §8 F4 · §10.
- **Changes:** the drift is now a `drift` verb of `pins.py`. `cmd_update` runs it as a subprocess before its write loop and writes the orders it returns with `write_row_order(outbox, "unit", row, to_commit, body)`, where `row['path']` is `.governance/instructions.toml#<repository tag>`. The mode is read with `govkit.read_policy_value("instructions.stale", target)` and passed to the verb as `--stale`. S8 fills and drains the `instructions.stale` row.
- **Fork:** F4 re-resolved on rung 1, naming both parents, marked `RESOLVED (agent, 2026-10-24, delegated)`.

**PLAY-dOrderedCharter-35**: rev-4, 34137 bytes
- **Moved:** §2 S5 · §3 Edges (adds consumes-from 46) · §4 The composer, Rollout and Files touched · AC12 · §8 F4.
- **Changes:** S5 fills and drains the landed `instructions.exclude` row and reads the key through `policy_reader` with `--rev HEAD`. AC12's red is now `policy.py lists --check`, not a schema refusal. Orders go through spec 33's handler, keyed on a `path`.
- **Fork:** F4 re-resolved on rung 1, naming dGroundRules unit 1's S3 and S6, marked `RESOLVED (agent, 2026-10-24, delegated)`.

**PLAY-dOrderedCharter-36**: rev-4, 27808 bytes
- **Moved:** §2 S4 · §3 Edges (adds consumes-from 46) · §4 The exclusion walk and a first-probe paragraph · §5 perf · §8 F4.
- **Changes:** the check reads the landed row's `allowed`. The first probe commits `[instructions] exclude = ["<tag>"]` as the policy file's only revision in a scratch repository and runs `policy.py check --rev HEAD`. If that exits 2, the build run files an ask to dGroundRules.
- **Fork:** F4 re-resolved on rung 1, marked `RESOLVED (agent, 2026-10-24, delegated)`. dGroundRules' catalogue has no "tag" value type, so a key now counts as tag-valued when its `allowed` type is `set`, `list` or `name`. This reads more keys than strictly needed rather than missing one.

**PLAY-dOrderedCharter-46**: rev-3, 17154 bytes
- **Moved:** §2 S1, S5 and a new S6 · §3 Edges (adds dGroundRules, and hands-off to 35 and 36) · §4 Evidence, Why HEAD and not the index, and Inventory · §5 testing · a new AC5 · §7 New arm (now covers AC5) · §8 F2 · §10.
- **Changes:** the overlay keeps reading `HEAD`. S6 makes every `policy.py get` the composition makes pass `--rev HEAD`; with no commit yet (unborn HEAD), no read is made. The stale "dGroundRules has no spec yet" evidence is replaced by its landed specs.
- **Fork:** F2 re-resolved on rung 1, citing dGroundRules unit 2 S1 and S7 and unit 4 S7, marked `RESOLVED (agent, 2026-10-24, delegated)`.

### For the other groups
Specs 15, 32, 35 and 36 call Group B's spec 9 callable by the name `policy_reader`, so spec 9 must keep that name. Specs 35 and 36 cite "PLAY-dOrderedCharter-46 S6".

### Parent specs that look wrong or incomplete
1. **dSafePassage unit 9 (`:154-158`):** `read_policy_value(key, root)` takes no revision, so it always reads the target's landed ref. Spec 46's rule that the overlay and policy values share one revision therefore cannot hold for `instructions.stale` at update. Spec 33 §5 states this as a risk; it may warrant an ask for a `rev` argument.
2. **dGroundRules units 2, 4, 5 and 19:** spec 32's extension needs changes inside the policy kit that its specs don't anticipate.
   - `validate(text)` and `load_catalogue(kit)` take no revision or extra rows.
   - The mirror records the blob ids of the policy file and the catalogue only, so an overlay `[[policy]]` edit is not part of its staleness key.
   - The guard's mirror shape compares only the policy file and the catalogue with HEAD.
3. **dGroundRules unit 1 (`:69-71`):** a value given as a "registered" member is refused by the value check. If `instructions.exclude`'s "set of gov tags" is encoded with `registry`, no value except `none` can be set. Spec 36's probe catches this, but the parent may need to settle it.

The spec files are in `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/`:
- 2026-10-23-spec-PLAY-dOrderedCharter-15.md
- 2026-10-23-spec-PLAY-dOrderedCharter-32.md
- 2026-10-23-spec-PLAY-dOrderedCharter-33.md
- 2026-10-23-spec-PLAY-dOrderedCharter-35.md
- 2026-10-23-spec-PLAY-dOrderedCharter-36.md
- 2026-10-24-spec-PLAY-dOrderedCharter-46.md

My edit scripts are still in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-thermostat-power-issue-370c51/784b9d4d-3d6b-441c-87c6-b603e2cf2649/scratchpad/dC/`.

### Return 2

I made the spec 32 correction. It stays at rev-3 and is now 35433 bytes. I extended the existing §9 rev-3 line rather than bumping the rev.

**What moved:**
- **§2 S9:** the `deploy.toml` comment is now the owner's edit, made at their terminal. The minimal guard's hook admits a guarded file staged there (dGroundRules unit 6, S1 and S4), and that is the only way a guarded file gets written outside a step. The pass leaves `.governance/deploy.toml` out of its commit, and its hand-back names the edit along with the comment's new text.
- **§4 The selection claim:** one added sentence saying the pass writes that text into its hand-back and the owner applies it.
- **§4 Files touched:** `.governance/deploy.toml` is off the list. A line below it says the file is not in the pass's commit.
- **AC11:** now in two halves.
  - On the pass's commit, `git show --name-only --format= HEAD -- .governance/deploy.toml` prints nothing, and the hand-back names the edit.
  - After the owner's edit, `git grep -n "EVERY kit" -- .governance/deploy.toml` finds nothing. A `permission:` line says this half observes the owner's edit, not the pass.
- **§8 F4:** split into two halves in one F-item.
  - The overlay half keeps its choice and its original 2026-10-23 mark. It now names spec 31's step as the writer of the overlay rows.
  - The `deploy.toml` half is re-resolved on rung 1 by dGroundRules unit 6 S4, marked `RESOLVED (agent, 2026-10-24, delegated)`: the owner edits the comment by hand.

**Checks:** the grep for `until it lands`, `template-size-limits` and `prepared merge` matches only one line, F4's options text. The hygiene gate, run over an index copy holding only spec 32, fails only check 9 (the build index needs a fresh render, which is yours). That index copy is deleted.

**Subprocess helper:** confirmed, none of my specs defines its own. Specs 15, 32 and 35 call spec 9's `policy_reader`, and spec 46 only passes `--rev HEAD` to it. Spec 36 uses `resolve_kit_dir` only to find the catalogue file it reads with `tomllib`. Spec 33 reads its policy value through govkit's `read_policy_value`.

The file is `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-32.md`.

### Return 3

I added the `usage.toml` row for the `unit` class to spec 33. It stays at rev-3 and is now 33152 bytes; I extended the existing §9 rev-3 line rather than bumping the rev.

**What moved:**
- **§2 S5:** the commit that registers the `unit` class also writes its `[[class]]` row in `tools/govkit/usage.toml`, because the docs leg treats a registered class with no row as a finding (dSafePassage unit 13 S1 and S8). The row's usage shape is `none`, with a `why`: a gov unit has no verb, key, hook, leg or page of its own, and units that do carry a `usage` field belong to spec 37's `unit-usage` class (its §8 F7). S5 is now observed by AC7 and AC11.
- **§4 The step gate class:** a second TOML block holds the row (`class = "unit"`, `usage = "none"`, `why`). A sentence after it covers the `rows` field (see below).
- **§4 Files touched:** adds `tools/govkit/usage.toml`.
- **AC11 (new):**
  - `git grep -n -A3 -F 'class = "unit"' -- tools/govkit/usage.toml` prints one `[[class]]` row with `usage = "none"` and a `why`.
  - `git grep -n -F 'id = "unit"' -- tools/govkit/surface-classes.toml` prints the registered class.
  - It is red when the class is registered with no usage row, or when the row declares a usage shape a unit doesn't have.

**One point unverified:** unit 13 S1 says every `[[class]]` row names where its rows come from, but its only example row is a `verb` class, so I couldn't tell whether a `none` class needs a `rows` field. The row omits it. The spec tells the builder that if unit 13's grammar requires `rows` on every class, they should spell it the way unit 13's `file` and `installable` rows (its other `none` classes) do.

**Checks:** the hygiene gate, run over an index copy holding only spec 33, fails only check 9 (the build-index render is owed, which is yours). The index copy is deleted.

The file is `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-33.md`.

### Return 4

I applied the owner's picks and the audit fixes to specs 15, 32, 35 and 36. Each is still `DEFERRED`, one rev higher, dated 2026-10-25, with a §9 line naming the owner-forks brief and its item.

**Checks:** the hygiene gate, run over an index copy reset with `git read-tree HEAD` and holding only these four specs, fails only check 9 (`memory/builds/dOrderedCharter/README.md` needs a fresh render, which is yours). The index copy is deleted. All four specs stay under 47000 bytes.

| Spec | Rev | Bytes |
|---|---|---|
| PLAY-dOrderedCharter-15 | rev-5 | 37441 |
| PLAY-dOrderedCharter-32 | rev-4 | 40621 |
| PLAY-dOrderedCharter-35 | rev-5 | 37637 |
| PLAY-dOrderedCharter-36 | rev-5 | 31792 |

These are larger than my earlier figures because the render had already added generated records rows before I started.

**Spec 15 (item 1).**
- **Moved:** the Status line now ends `ratified 2026-10-25`. S5 says directly that the command checks `sys.stderr.isatty()` itself, a second test of the signal the guard's hook tests. §10 reads the same way instead of pointing at an open fork.
- **Fork:** F4 now carries `RESOLVED (owner, 2026-10-25): (a).` and says that spec 7's `owner-only-expiring` proof is this check.

**Spec 32 (item 7, audit P4).**
- **Moved:** S7 now says the mirror renders `adopter.` keys and adds the overlay blob's id to its staleness key. It also says the guard's mirror shape requires `.governance/instructions.toml` to equal HEAD.
  - §4 Files touched adds `tools/policy/guard.py`.
  - §5 risks: any overlay edit, a `[[unit]]` row included, makes the mirror stale until the landing regenerates it.
  - AC8 adds two observations: `mirror --check` exits 1 after an overlay-only commit, and `guard.py --staged` refuses a staged mirror while the overlay differs from HEAD.
- **Fork:** a new F6, with option (a) (mirror and guard see the overlay) against (b) (the mirror omits `adopter.` keys). I resolved it as `RESOLVED (agent, 2026-10-25, delegated): (a)` on rung 1, because v2:1127 says every key in `.governance/policy.toml` is mirrored to JSON for the hooks.

**Spec 35 (item 8, audit P11).**
- **Moved:** S5 now says the key's values are the empty set `[]` (v2's `none`, and the default) or a set of gov tags. `get` prints the empty default as no line. S5 also cites the built row: `{ type = "set", item = ... }`, `empty = "allowed"`, `default = []`. AC12 now expects `[]` as the default.
- **Fork:** none.

**Spec 36 (items 5 and 8, audits P5 and P11).**
- **Moved:**
  - S4 gives the default as `[]`, which excludes nothing.
  - The first probe is now expected to exit 0. The built row's `item` pattern `[A-Za-z0-9][A-Za-z0-9_.-]*` admits a gov tag, and the built `check_value` admits any set member the pattern fully matches. The probe still decides at the build run.
  - I also fixed a gap in my rev-4 walk: `instructions.exclude` is itself a set-typed key, so the walk would have read it as a requirer of its own members and refused every exclusion. It is now never read as its own requirer.
- **Fork:** none.

**Two things you should know:**
- The dGroundRules branch tip has moved from `df4912bd` to `7e80dee4`. I checked that `catalogue.toml` and `policy.py` are unchanged between the two, and spec 36's evidence names both commits.
- Two of my Group C specs outside this round's list are now stale. I didn't edit them because you limited this round to four specs.
  - Spec 46 S6 (line 68) still says `instructions.exclude`'s default is `none`.
  - Spec 33's §5 risk line says the update reads `instructions.stale` at the landed ref, because `read_policy_value` took no revision. dSafePassage unit 9 now gives it `rev=None` (audit P3), so spec 33 could pass `rev="HEAD"` and drop that risk.

The files are in `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/`:
- 2026-10-23-spec-PLAY-dOrderedCharter-15.md
- 2026-10-23-spec-PLAY-dOrderedCharter-32.md
- 2026-10-23-spec-PLAY-dOrderedCharter-35.md
- 2026-10-23-spec-PLAY-dOrderedCharter-36.md

### Return 5

I fixed both. Each is still `DEFERRED` at rev-4, dated 2026-10-25, with a §9 line naming the owner-forks brief and the audit item.

| Spec | Rev | Bytes |
|---|---|---|
| PLAY-dOrderedCharter-33 | rev-4 | 36510 |
| PLAY-dOrderedCharter-46 | rev-4 | 20511 |

- **Spec 33 (P3):**
  - S3 now has `cmd_update` read the mode with `read_policy_value("instructions.stale", target, rev="HEAD")`. That is the target's `HEAD`, the revision spec 46 reads the overlay at; the `rev` reaches `policy.py get` as `--rev`.
  - §4 Inventory names the same call.
  - The §5 risk line about reading the mode at the landed ref is gone.
  - AC10's grep, `read_policy_value("instructions.stale"`, still matches the new call, so it needs no change.
- **Spec 46 (P11):** S6 now says that with no commit yet, `instructions.exclude` reads its catalogue default `[]` (v2's `none`), as dGroundRules' built row holds it. The spec's remaining "landed ref" mentions describe dGroundRules' own default revision, so they stay.

The hygiene gate, run over an index copy reset with `git read-tree HEAD` and holding only these two specs, fails only check 9 (`memory/builds/dOrderedCharter/README.md` needs a fresh render, which is yours). The index copy is deleted.

The files are in `C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/`:
- 2026-10-23-spec-PLAY-dOrderedCharter-33.md
- 2026-10-24-spec-PLAY-dOrderedCharter-46.md

## Group D, tags and steps, led by unit 31

### Return 1

I've revised all five Group D specs (19, 25, 26, 30, 31). Each is now at rev-4, dated 2026-10-24, still DEFERRED, with a §9 line naming the sections moved and the cross-check record.

**Checks:**
- **Wording grep:** across all five specs, the `until it lands` / `template-size-limits` grep finds one line, in spec 31's new §9 entry, which records the file's removal.
- **Size:** every spec is under 49152 bytes.
- **Hygiene:** I ran the memory hygiene gate on a copy of the index with only these five specs staged. The only finding left is check 9: the build index needs re-rendering (`memory/builds/dOrderedCharter/README.md` is stale). That's a `gen_build_index.py --write` job, so it's yours. I deleted the index copy and the scratch folder `dD` is empty. Nothing was staged into the real index and nothing was committed.

| Spec | Rev | Sections moved | Forks | Bytes |
|---|---|---|---|---|
| 19 | rev-4 | S8 S9 · §3 · §4 Migration, Files touched · §5 · AC15 (new) · §7 · §10 | none added | 38028 |
| 25 | rev-4 | S4 · S9 (new) · §3 · §4 Inventory, Files touched · §5 · AC9 (new) · §7 · §10 | none added | 22339 |
| 26 | rev-4 | S3 · S9 (new) · §3 · §4 Files touched · §5 · AC11 (new) · §7 · §10 | none added | 27650 |
| 30 | rev-4 | S5 · §3 · §4 Files touched · §8 | F4 added, `RESOLVED (agent, 2026-10-24, delegated)`: (a), rung 1, because TOOL-dGroundRules-6 S1 rules out the pass's own edit | 26399 |
| 31 | rev-4 | S1 S3 S5 S7 · §3 · §4 · §5 · AC3 AC9 AC13 (new) · §7 · §8 · §10 | F6 and F7 added, both left open for the owner, each recommending (a). F4's existing mark is kept; only its trailing clause changed to "owes no ask". F1's evidence now also cites dSafePassage unit 1 rev-9 `:201-204` | 40787 |

**What changed in each:**
- **Spec 19:** the three `tags.*` rows are filled and drained rather than added, and the mirror lands in a second commit. I added one helper, `run_policy_get(key, root)`, in `tools/playbook/render_playbook.py` next to its inlined `resolve_kit_dir`. It runs `policy.py get` as a subprocess and refuses with exit 2, naming the key, when the reader exits 2 or no policy kit is found. Specs 25 and 26 call it, and the hand-off edges now say so. S9's re-export no longer rides a dSafePassage shim; its hold is spec 31's open F6.
- **Specs 25 and 26:** each reads its keys through `run_policy_get`, and a new S9 fills and drains the landed rows (`tags.bundle` and `tags.bundle-rows` in 25, `tags.positional` in 26).
- **Spec 30:** under F4, the `.governance/deploy.toml:28` comment is rewritten in the lander's prepared merge for spec 31's landing. That adds a hands-off edge to spec 31, which carries the matching consumes-from edge.
- **Spec 31:**
  - **Leg name:** it is now `upgrade-walk`.
  - **AC3:** it now reads succession through `govkit.py check`, using the line dSafePassage unit 1's AC9 states.
  - **Moved reader:** the `charter-key` reader and plant moved out of the step program into `tools/govkit/step_gate.py`, so a later edit can't red `step-rows-frozen`.
  - **U1 and U2:** the limits file is gone from S1's readers. The commit that moves `CODEX_MAX` also re-points the `codex-instructions` census row and its `budgets-cap-codex-instructions` case; new AC13 observes it.
  - **U9:** §5 now says the commit that removes the last `map_lib` re-export also removes the `module-export` row.
  - **F7 evidence:** I checked this against the code: `tools/govkit/govkit.py:9988-10000` (with `UPDATE_ROLE` mapping `seed` to `report-reseed` at `:8480`) rewrites every seed row's verdict after the grid. An edited seeded copy that gov stops shipping comes out `patched` with no order, and an unedited one `current`. The cross-check record names a different path (`reseed-available`), but its conclusion holds, and AC9 now says its verdicts wait on F7.

**Parent specs that look wrong:**
- **dSafePassage unit 9 (`:126-128`):** its new arm doesn't cover seed rows, because the seed override above it rewrites the verdict first. This is what F7's option (a) would ask dSafePassage to fix.
- **dSafePassage unit 6 (`:89-91`):** it still lists the `map_lib` re-export among the first shim rows, which contradicts spec 31's F2. F6's option (a) asks to drop that mention.

**Issues outside my group:**
- **Spec 32 F4 (Group C), and so spec 30 F4:** I resolved spec 30's F4 to spec 32's route as you asked. But that route never says what actually writes a gov-only comment in the prepared merge: a step program runs on every adopter, and the edit isn't a step. Option (b), dropping the edit and keeping the comment, is a reasonable alternative, since `cross-os` still names the toolchain block that line describes. Group C may want to name the writer.
- **Spec 9 (Group B):** if its `policy_reader` lands as a second subprocess helper in `tools/playbook/`, it could call `run_policy_get` instead of adding a copy.
- **Spec 31 S1:** the "by value" half now names "unit 6's check" in neutral terms rather than `tools/check-template-size.sh`, so Group A's re-ground of spec 6 decides where the harness limit is read.

Files are in `C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dOrderedCharter\spec\`:
- 2026-10-23-spec-PLAY-dOrderedCharter-19.md
- 2026-10-23-spec-PLAY-dOrderedCharter-25.md
- 2026-10-23-spec-PLAY-dOrderedCharter-26.md
- 2026-10-23-spec-PLAY-dOrderedCharter-30.md
- 2026-10-23-spec-PLAY-dOrderedCharter-31.md

### Return 2

All three follow-ups are done, and no spec goes past 49152 bytes: the largest is spec 31 at 42238. The hygiene gate on an index copy with only my five specs staged still shows only check 9, the build-index re-render, which is yours. I deleted the copy, `dD` is empty, nothing is staged in the real index and nothing is committed. None of the specs was bumped again; each follow-up was added to its existing rev-4 entry in §9.

| Spec | What moved | Bytes |
|---|---|---|
| 19 | **S8:** this pass creates `tools/playbook/policy_value.py` with `read_policy_value(key, root, rev=None)` and `PolicyRefused`, to spec 7's §4 "The policy reads" contract. Its own reads are `read_policy_value("tags.slice", root)` and the two sibling keys, and a `PolicyRefused` exits 2 naming the key. **Other sections:** the readers clause, Inventory, Files touched, AC15's grep, §10 and the rev-4 entry now name `policy_value.py` instead of `render_playbook.py`. The hand-off edges to 25 and 26 name the module, and the edge to 7 now adds the module. **Parity:** the module's inline `resolve_kit_dir` copy needs no new row. The existing `resolve_kit_dir` row in `tools/lib/resolve-python.test.sh:172` picks it up through its marker grep at `:218`. | 39174 |
| 25 | S4, the consumes-from edge to 19, AC9's grep, §10 and the rev-4 entry call `read_policy_value` from unit 19's module. A `PolicyRefused` refuses the call. | 22679 |
| 26 | S3, the consumes-from edge to 19, AC11's grep, §10 and the rev-4 entry make the same change. | 27985 |
| 30 | **F4:** re-resolved on rung 1 by TOOL-dGroundRules-6 S4, marked `RESOLVED (agent, 2026-10-24, delegated)`. The pass leaves `.governance/deploy.toml` out of its commit, and its hand-back names the one-line comment edit (`cross-os` now drops only the toolchain section) for the owner to make at their terminal. F4 states why the prepared-merge route fails: no step writes a gov-only comment. **Other sections:** the hands-off edge to 31 is gone, and S5's readers line, Files touched and the rev-4 entry were updated to match. | 26558 |
| 31 | **Usage rows:** S3 and S4 now write each class's `[[class]]` row in `tools/govkit/usage.toml` in the same commit, shape `none` with a `why`. Neither class fits a TOOL-dSafePassage-13 S2 shape: a placeholder's usage lives in its own `[[placeholder]]` row's `default` and `why`, which no S2 source reads. **Other sections:** the class-rows code block now carries both rows, and Files touched lists `usage.toml`. The §5 risk adds that the last re-export's commit also removes the `usage.toml` row, §7's prose names the `docs` leg, and S4's observation line and the rev-4 scope list name the new AC14. **AC14:** a grep that both rows exist with `usage = "none"`. **Edge:** I removed the consumes-from edge to spec 30. | 42238 |

Decision for you: I also removed one sentence from spec 31's S7, beyond the edge you allowed. It was my own addition in this rev, and it said the prepared merge carries spec 30's comment rewrite; after the F4 change that is false. If you want it kept, restore it.

For the builder: in spec 31's `usage.toml` rows I spelled the `rows` field as `"none"`. TOOL-dSafePassage-13 shows `rows` only for a `verb` class, so the spec says the builder copies however unit 13's own `none` rows (`file`, `installable`) spell it when that unit builds.

Files are in `C:\projects\coding-governance\.claude\worktrees\thermostat-power-issue-370c51\memory\builds\dOrderedCharter\spec\`:
- 2026-10-23-spec-PLAY-dOrderedCharter-19.md
- 2026-10-23-spec-PLAY-dOrderedCharter-25.md
- 2026-10-23-spec-PLAY-dOrderedCharter-26.md
- 2026-10-23-spec-PLAY-dOrderedCharter-30.md
- 2026-10-23-spec-PLAY-dOrderedCharter-31.md

### Return 3

I've put the `install.deprecation-window` token back in spec 19's S9, now 40260 bytes, but I couldn't run `check-spec-tokens.py` to confirm the cl-dClosedLoop-0049 finding is gone. The scratch-guard hook blocks gov-spec-writer from that gate; only memory hygiene and the lexicon are allowed. Please run it from the main session.

What I checked instead:
- **Token probe:** spec 19 still has `**Carries:** cl-dClosedLoop-0049@a87d159d whole` at line 5, and `grep -n "install.deprecation-window"` on it now finds lines 116 and 433. Since the finding was that this clause's token appears in none of its carriers, I expect it to clear.
- **Hygiene gate:** run on a copy of the index, it fails on check 25 for spec 6 S6, which is Group A's. It reports nothing on my five specs, and check 9, the build-index render, no longer fails. The copy is deleted and the scratch folder `dD` is empty.

The changed S9 line (line 116 and the start of 117) now reads:

```
  (`tools/codebase-map/kit.toml:7`); `map_lib` re-exports them for `install.deprecation-window`
  releases, declared by PLAY-dOrderedCharter-31's `module-export` class row, the mechanism that counts
  that hold being that unit's open §8 F6; the template is
```

The rev-4 entry in §9 now ends: "…in place of a second helper; and S9 again names the `install.deprecation-window` hold `cl-dClosedLoop-0049` carries, its mechanism F6's." There was no rev bump.

The real index now holds 63 staged files, which I take to be yours: every group's specs, the prompts, and deviation records dated 2026-10-25. I didn't stage or unstage anything there. Your staged copy of spec 19 was staged before this edit, so re-stage it or the S9 fix won't be in your commit.

### Return 4

The owner's (a) picks for F6 and F7 are now in specs 31 and 19, each bumped one rev to 2026-10-25 and still DEFERRED. On an index copy reset with `git read-tree HEAD` (now `c63aabbb4`) holding only these two specs, the memory hygiene gate reports only check 9, the build-index render that `gen_build_index.py --write` fixes, which is yours. I deleted the copy, `dD` is empty, and nothing was staged or committed.

**Spec 31: rev-5, 46518 bytes**
- **Status:** now ends `ratified 2026-10-25`.
- **F6:** marked `RESOLVED (owner, 2026-10-25): (a).` Dropping the re-export from its first shim rows is credited to dSafePassage unit 6's 2026-10-25 revision (`2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md`, Item 4).
- **F7:** marked `RESOLVED (owner, 2026-10-25): (a).` Routing a retired seed row through the `retired-edited` arm is credited to dSafePassage unit 9's 2026-10-25 revision (same brief, Item 5): an edited copy reads `retired-edited` with one order, an unedited one `withdrawn`.
- **S3 and §3:** the names are held for `install.deprecation-window` releases. dConvergedCharter counts the window from the `module-export` row's landing commit, and no `[[shim]]` row holds them.
- **S5 and AC9:** both expect unit 9's new retired-seed verdicts.
- **Edge:** a new consumes-from external edge on that unit 9 revision.
- **§9:** a rev-5 line names `2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md`, Items 3 and 4.
- **Trims:** I shortened F6's and F7's evidence prose, because the brief says a spec over 47000 bytes must be trimmed to leave room for the records rows your render adds.
- **Check:** `grep -n 'RESOLVED (owner, 2026-10-25): (a)'` prints F6 at line 435 and F7 at line 447.
- **Unverified citation:** I cited the parent revisions as their "2026-10-25 revision" rather than by rev number. Their files in the working tree are still at rev-4 (unit 6) and rev-3 (unit 9) with the old text, because the other writer hasn't saved yet. Once those land, check the wording matches what they actually say.

**Spec 19: rev-5, 42820 bytes**
- **S9:** the `install.deprecation-window` hold is now spec 31's settled F6, counted by dConvergedCharter from that row's landing commit.
- **§3:** the external edge now calls it unit 31's settled re-export fork.
- **§9:** a rev-5 line names the owner-forks brief, Item 3.
- **Size:** I reported spec 19 at 40260 bytes last time. My edit here adds only about 400, so the file seems to have been changed in between, probably by your render.

## Group E, help and batches, led by unit 37

### Return 1

I revised all four Group E specs: 37, 49, 50 and 55. Each stays `DEFERRED` and is under the 49152-byte cap. The acceptance grep prints only history or removal lines, and the real index was never touched.

**Hygiene gate:** I ran it over a copy of the index with only these four specs staged, then deleted the copy and the `scratchpad/dE/` folder. Check 25 flagged spec 37's S2 for a missing **Readers:** clause, and I fixed it. The only finding left is check 9, the build index for spec 37, which only `gen_build_index.py --write` fixes, so it is yours. I ran the naming lexicon over the seven new function names and all passed.

### PLAY-dOrderedCharter-37: now rev-4, 34927 bytes
- **Sections moved:** §1, §2 (S1, S2, S4, S5), §3 (non-goals and the external edge), §4 (data model, examples, inventory, files), §5, §6 (AC5 changed, AC9 to AC11 added), §7 (one new arm), §8, §9, §10.
- **What changed:**
  - **Row 51:** the policy page's reader is `read_policy_reference_rows`. It finds the policy kit through `resolve_kit_dir` and parses `catalogue.toml` with `tomllib`; it never loads `policy.py`.
  - **Row 50:** the policy page renders rows that carry both `summary` and `usage`, and lists the rest under `## Not yet summarised (<n>)`. The other registries still refuse such a row.
  - **U8:**
    - `--fingerprints` now prints `<id>\t<fp8>\t<pages>`.
    - A key already anchored on another page (such as `help.enforce` on `help/docs-leg.md`) is linked, not anchored twice.
    - Anchoring a member deletes its row from `memory/project/docs-undocumented.txt`.
  - **Row 21:** the new classes register in `tools/govkit/surface-classes.toml`, each with a reader and a plant. Their `usage.toml` rows read usage from the registry itself, so `usage.toml` never restates it.
- **Forks:**
  - F5 (how drive and kinds join the docs leg) is new, `RESOLVED (agent, 2026-10-24, delegated)`, rung 1.
  - F6 (the policy page while rows lack a summary) is new, `RESOLVED (agent, 2026-10-24, delegated)`, rung 1.
  - F7 is new and was not in your brief, `RESOLVED (agent, 2026-10-24, delegated)`, rung 3. Unit 33's `unit` class holds every gov unit tag, but most units carry no `usage`, and the shrink-only list cannot take their rows. I chose a separate `unit-usage` class that uses unit 33's change records as its witness.
  - F1 to F4 are unchanged.

### PLAY-dOrderedCharter-49: now rev-3, 48971 bytes (181 bytes of headroom)
- **Sections moved:** §2 (S1, S11, S30, S31), §4 (inventory, files), §6 (AC1, AC7, AC23), §8, §9.
- **What changed:** S1 follows spec 37's policy-page rule. S30 and S31 measure against the `budgets.*` cap through `budgets.py resolve`.
- **Fork:** F3 is re-resolved, `RESOLVED (agent, 2026-10-24, delegated)`, rung 1, from (a) to a new (d). The census becomes a step of its own, `playbook/census-to-overlay`, with its own program file `tools/govkit/steps/census_to_overlay.py`. Two parent facts force this:
  - `step-rows-frozen` freezes unit 31's program once unit 31 lands (TOOL-dSafePassage-1 S9).
  - The prepared merge runs declared steps only (TOOL-dSafePassage-8 S1).

  On any tree whose receipt is not `"mode": "source"`, the step does nothing. It also absorbs spec 55's S9 re-render, because the program freezes when unit 49 lands.

### PLAY-dOrderedCharter-50: now rev-2, 17435 bytes
- **Sections moved:** §2 (the size row of S2, S3, S4), §3 (a new external edge), §4 (evidence), §9, §10.
- **What changed:** the probe reads caps from `tools/policy/caps.toml` and each value through `budgets.py resolve` as a subprocess. A crossed cap is answered by a trim, or by a raise in the guard's one admitted shape where the cap names a tracked file.
- **Forks:** none.

### PLAY-dOrderedCharter-55: now rev-2, 34050 bytes
- **Sections moved:** §2 (S9, S27), §3 (an edge reworded), §4 (order list, files), §6 (AC9, AC27), §9.
- **What changed:**
  - S27 and AC27 read the `budgets."memory/builds/*/spec/"` cap through `budgets.py resolve`.
  - S9 now names unit 49's census step. It is built at unit 49's pass and only observed here, which is spec 55's existing pattern for items that change an earlier pass. `adopter_rules_to_overlay.py` is gone from its files.
  - This S9 move goes beyond your brief's "U1 only" for spec 55. It follows from spec 49's U7 fix.
- **Forks:** none.

### Specs that look wrong
- **dOrderedCharter specs 31 and 33 (outside my group):** TOOL-dSafePassage-13 S8 makes any registered class without a `usage.toml` `[[class]]` row a finding. So spec 31's `charter-key` and `module-export` classes and spec 33's `unit` class each owe a `usage.toml` row (`usage = "none"` at least) at their own pass. Neither spec says so, and the cross-check record does not list it.
- **TOOL-dSafePassage-1 S9:** it freezes only files a landed argv names. A module that a step program imports stays editable, so a landed step's behaviour can still change. U7's fix for spec 31 relies on that gap.
- **TOOL-dSafePassage-13 S1, S2 and its hand-off to later builds:**
  - The `rows` sources are a closed list, so a later class whose registry states its own usage has no defined way in.
  - The hand-off asks later builds to add "its members' rows" to `usage.toml`, which conflicts with S2's no-restating rule.
  - Spec 37 now adds a row source to the leg to get around this.
- **TOOL-dGroundRules-6 S3:** an agent's raise is admitted only when the key's last segment is a tracked file. So the class cap `memory/builds/*/spec/` can never be raised by an agent. That may be intended, but no spec says so.

Files:
- C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-37.md
- C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md
- C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-50.md
- C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-55.md

### Return 2

Spec 49 now reads 47978 bytes CR-stripped (`wc -c` gives the same), down from 52060 with the current generated table in place. It stays at rev-3 and `DEFERRED`, and I committed nothing.

**Hygiene:** I ran the gate over an index copy reset with `git read-tree HEAD`, with only spec 49 staged. It exited 0 and names spec 49 for nothing, not even check 9, since your index render is now in place. One mid-trim run flagged check 12: shortening AC15 and AC50 had removed their backticked witnesses. I put a witness back in each before the clean run. I deleted the copy and all my scratch files.

**Real index:** I never touched it. It holds 65 staged files, none staged by me. Its spec 49 blob is an older 49891-byte version, so re-stage spec 49 from the working tree before you commit.

**What was trimmed**, with each fact still held somewhere:
- **§1:** the 64-entry id map is now one sentence giving the rule (MEDIUM M<n>'s criterion is AC<n>, LOW L<n>'s is AC<45+n>, merged ids share one). Each item already names its id and criterion. I also dropped the review-record path, which the generated table holds, and the "skeptic's corrected fix" list, since each of those items says so itself.
- **§3 edges:** the 35 consumes-from lines now give only their item references (for example `— S21, S42`); each item says what it consumes. The hands-off to spec 55 names that unit's items instead of a gloss.
- **§2:** I removed the ten subheadings; nothing in the tree cites them, and all 73 items stay numbered and in order. I also tightened the wording of S1, S3, S11, S12, S14, S35, S41, S48, S56 and S68.
- **§4:** the Order subsection is folded into its matching §3 non-goal. Rollout, Evidence and the "Two batches" alternative are condensed.
- **§6:** a few criteria now point at their item instead of repeating its paths: AC3, AC12, AC14, AC20, AC39, AC54, AC61 and AC63. AC1, AC13, AC26, AC45, AC50 and AC64 are reworded more tightly.
- **§7 and §8:** the first new-arm description is shorter, and F3, F5 and F8 have tighter option text with the same choices and resolutions.

All 73 items, 64 criteria and 9 forks remain, with their substance. I left every "Observed by ACn" phrase and every "Red when:" clause intact, because the hygiene gate and probably the acceptance matrix read them.

**§9:** the rev-3 line now lists sections §1 to §4 and §6 to §8, and ends with a clause naming the trim: "trimmed under its cap: §1's id map, the edge glosses, §2's subheadings and §4 Order go, each fact kept."

File: C:/projects/coding-governance/.claude/worktrees/thermostat-power-issue-370c51/memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md
