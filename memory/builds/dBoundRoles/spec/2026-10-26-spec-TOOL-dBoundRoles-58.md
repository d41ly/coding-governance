# TOOL-dBoundRoles-58 — the round-1 audit of units 45 to 51, its 35 minors: criteria that can pass on a correct build, one typed set and one block reader at spawn, one extents record at render, the H1 parity's consumers, and AMENDED answers that name a revision

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 32 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 |
| [2026-10-26-build-TOOL-dBoundRoles-52-round3-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-52-round3-fix-return.md) | research | TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-55 |
| [2026-10-26-prompt-TOOL-dBoundRoles-52-round3-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-52-round3-fix-brief.md) | research | TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-55 |
| [2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the seven promoted specs 45 to 51
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`) confirmed
six HIGH findings, promoted as `TOOL-dBoundRoles-52` to `-57`, and 24 MEDIUM and 11 LOW. BUILD-METHOD M4
batches the minors into one unit: they do not split into two disjoint write sets by M6 (§4 "Why one
unit"). This unit takes all 35, report ids 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 19, 21, 22, 23, 24, 25,
26, 27, 28, 31, 32, 33, 34, 35, 37, 38, 39, 42, 45, 46, 47, 48, 49 and 50, each its own scope item even
where the report merged several into one item.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M1 | 2, 39 | unit 47 S1, AC1, AC2 | S1, S2 |
| M2 | 3 | unit 50 S8, AC8 | S3 |
| M3 | 4, 37, 46 | unit 45 AC1 | S4, S5, S6 |
| M4 | 5 | unit 48 AC2, §7 | S7 |
| M5 | 8, 15, 32 | unit 46 S1, AC3, §8 F2 | S8, S9, S10 |
| M6 | 21, 33 | unit 48 S3 | S11, S12 |
| M7 | 11 | unit 51 S1, AC1 | S13 |
| M8 | 17 | unit 50 S3, AC3 | S14 |
| M9 | 34 | unit 50 S9, unit 56 | S15 |
| M10 | 22 | units 46 S2 and 48 S3 | S16 |
| M11 | 23 | units 48 S1, S2 and 41 S1, S2 | S17 |
| M12 | 24 | units 46 AC1, 48 AC3, 50 AC7 | S18 |
| M13 | 25 | unit 50 S21, unit 43 S56 | S19 |
| M14 | 31 | unit 50 AC12 | S20 |
| M15 | 42 | unit 45 S2 | S21 |
| M16 | 45 | unit 45 S2, §4 | S22 |
| M17 | 47 | units 50 AC4, AC20, AC22 and 51 AC2, AC5, AC7 | S23 |
| M18 | 48 | units 50 and 51 §3, and 38, 41, 42, 44, 25 | S24 |
| L1 | 9 | unit 46 S2, AC1 | S25 |
| L2 | 10 | unit 48 S3 | S26 |
| L3 | 12, 38 | unit 45 §5 | S27, S28 |
| L4 | 19 | unit 46 §4 | S29 |
| L5 | 26 | unit 48 S1 | S30 |
| L6 | 27 | unit 49 S1 | S31 |
| L7 | 28 | unit 51 S1, S6, §5 | S32 |
| L8 | 35 | units 45, 46 and 48 §5 | S33 |
| L9 | 49 | unit 51 S8, AC8 | S34 |
| L10 | 50 | unit 47 S1 | S35 |

## 2. Scope (IN)

- **S1** — id 2. A second render, on a typed `diff`. Unit 47's case adds a `--role gov-skeptic` render
  whose `--input diff=` is one line carrying `record:TOOL-tFix-9@000000000000` and whose `--input spec=`
  names the scratch spec quoting it. `gov-skeptic` reads `input:diff?, input:spec?`
  (`tools/roles/agents/gov-skeptic.agent.md:7`) and keeps its slot after unit 1. The render refuses
  naming the span once; with a plain-words diff it renders. Observed by AC1.
- **S2** — id 39. The case's role reads both keys, by statement and by check. Every render of 47's case
  calls `TOOL-dBoundRoles-53`'s `assert_role_reads` for its role and keys, S1's included, and its
  refusal half requires no `does not read` in stderr. Where 47's S1 does not yet say its role must read
  every key it passes, the pass adds that sentence. Observed by AC2.
- **S3** — id 3. Unit 50 S8 names its role. Its two renders at unit 41's pass commit and its parent run
  `--role gov-skeptic` with `--input diff=<one line>` and `--input spec=<a spec with no grammar span>`;
  S8 and AC8 say so. Observed by AC3.
- **S4** — id 4. Unit 45 AC1's control render runs on a role that reads `input:spec` with no required
  brief key: the case renders `--role gov-builder --input spec=<scratch spec>` and sees the spec's bytes
  inside a fence. Observed by AC4.
- **S5** — id 37. The control role reads no `task:` key, so its render resolves no kickoff checker
  (`tools/roles/handoff.py:340-346`) and needs no card. Observed by AC5.
- **S6** — id 46. Unit 45 AC1 and its fixture line restated: the control render names `gov-builder`, and
  the fixture is the scratch adopter with no brief record and no card. Observed by AC6.
- **S7** — id 5. Unit 48 AC2 is a balanced flip in the render path. Its staged copy appends one unfenced
  block that opens a three-backtick fence before the handed block and one after it that closes the
  handed fence's last state with a longer run, §4's attack, so the walk ends balanced. The render refuses
  naming the handed block, and with `check_block_fences` reduced to the end of the walk it renders, so
  48's staged break turns this case red. Observed by AC7.
- **S8** — id 8. The spawn guard's file runs as a program only. `tools/roles/spawn-guard.js`, which
  unit 25 moves `tools/hooks/agent-cap.js` into, ends with `if (require.main === module) main()`, and its
  `module.exports` holds `TYPED_INPUTS`. Observed by AC8.
- **S9** — id 15. Unit 46 AC3 holds through a require: `node -e` requiring the file prints the set and
  exits without reading stdin. 46's §8 F2 names that guard as the precedent it follows. Observed by AC9.
- **S10** — id 32. The entry change has a case and an inventory line. A spawn-guard suite case pipes a
  rule-6 payload to the file and sees it deny and admit as before; the export list unit 25's inventory
  keeps names `TYPED_INPUTS`. Observed by AC10.
- **S11** — id 21. One typed set at spawn. 48 S3's typed-block exemption in `checkHandoffSpawn` reads
  `TYPED_INPUTS`. Observed by AC11.
- **S12** — id 33. The exemption follows the set. A case adds a third name to `TYPED_INPUTS` in a scratch
  copy of the file and sees a block headed by it exempt from the fence-shape half. Observed by AC12.
- **S13** — id 11. Unit 51 AC1 matches whole ids. It reads the pass subjects with the shape
  `^build\(dBoundRoles\): TOOL-dBoundRoles-<n> —`, for 3, 38, 39 and 40, so unit 37's commit no
  longer answers for unit 3. Observed by AC13.
- **S14** — id 17. Unit 50 AC3 reads stale rows where they are computed: the default mode of
  `tools/check-dead-paths.sh` exits 0 and prints no `stale waiver(s)` or `UNRESOLVED` line, and
  `--list` is read only for its `HIT` lines. Observed by AC14.
- **S15** — id 34. The H1 readers' consumers, observed. Over unit 56's five fixtures, the index
  generator's `spec_ids` resolution and the memory-recall extractor's record anchor each name the id
  `parse_spec_h1` returns. The ledger names each consumer with its leg: `build-index selftest`,
  `memory-recall kit selftest`, `routed-commits selftest`, and `deviation_join.py`, which has no leg of
  its own. Observed by AC15.
- **S16** — id 22. One block reader at spawn. `readTaskBlocks(section)` in the spawn guard's file, built
  on `readUnfencedLines`, yields each unfenced `### ` block's heading, fact line and line range. 46 S2's
  typed-block check and 48 S3's fence check both read it, and no other splitter of the task section is
  left in the file. Observed by AC16.
- **S17** — id 23. One extents record at render. `render_handoff` builds each block's extent once, with
  its key, line range, fence lines and a `handed` flag classified by `TOOL-dBoundRoles-45` §4 "The one
  answer"; `check_block_fences` and unit 41's graded text both read it, and no second classifier is
  left. Observed by AC17.
- **S18** — id 24. The moved hash is the one called. No criterion of a live spec and no case under
  `tools/` calls `handoff.derive_section_sha`; 46 AC1, 48 AC3 and 50 AC7 cite
  `roles_lib.derive_section_sha`, where unit 6 S4 moves it. Observed by AC18.
- **S19** — id 25. One transcript resolver. Unit 43 S56's `resolve_agent_transcript` takes an optional run
  id and spells the `subagents` and `workflows` layout once; 50 S21's `resolve_subagent_dir` is folded
  into it and deleted, its callers re-pointed. Observed by AC19.
  **Readers:** by name: `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-50.md`, whose
  S21 mints the helper and points its two readers at it, its AC21 greps for it and its inventory lists
  it; and `tools/roles/handoff.py`, whose `agents` verb (lines 847, 854 and 885) spells the layout
  inline at this unit's base and calls the helper from unit 50's pass. READER NOT IN TREE for unit 39's
  route test: it is built in the check-return verb at unit 39's pass, and its own spec never spells the
  helper's name, so spec 50's S21 is the one file that assigns it. by value: NO VALUE READERS — a path
  helper, compared by nobody.
- **S20** — id 31. Unit 50 AC12 runs the leg's own argv: the `shell hygiene (a fork spent on builtin
  work)` row's of `tools/gate-legs.json`. Observed by AC20.
- **S21** — id 42. `check_authored_lines` splits a typed value on `\n` only and deletes every `\r` from
  each line before matching, as `extract_prompt_marker` (`tools/roles/roles_lib.py:252`) and
  `extractHandoffMarker` do. Observed by AC21.
  **Readers:** by name: `tools/roles/roles_lib.py:252` and `tools/hooks/agent-cap.js:2051`, the two
  readers that already delete each carriage return and whose split S21 copies, and
  `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-45.md`, whose S2 states the rule
  whose line split S21 fixes; no name leaves the tree. by value: NO VALUE READERS — the carriage return
  is deleted only from the copy of a line the check matches, and the handed value and the rendered bytes
  keep it.
- **S22** — id 45. The graded line shapes follow their readers. `^### `, `FACT_RE`, `MARKER_RE` and
  `^Framed by:` are graded on every line of a typed value; `^#{1,2} ` only on the lines
  `read_unfenced_lines` yields. Observed by AC22.
- **S23** — id 47. Ledger criteria read their own block. 51 AC2, AC5 and AC7 and 50 AC4, AC20 and AC22
  scope each grep to the unit's own `**Evidences:**` block, from its line to the next `**Evidences:**` or
  heading. Observed by AC23.
- **S24** — id 48. AMENDED answers name a revision. For every criterion units 50 and 51 answer AMENDED,
  the pass bumps the answered spec, 38, 41, 42, 44 or 25, with the amended criterion and a §9 line
  naming 50 or 51; 50's and 51's §3 non-goal on rewording specs 1 to 49 gains that one exception; and
  each answer reads `amended rev-<n>`, naming that revision. Observed by AC24.
- **S25** — id 9. The typed-block check runs before the marker count in `checkHandoffSpawn`, so a forged
  marker in `input:question` is denied naming the block and the line. Observed by AC25.
- **S26** — id 10. No literal list of typed input names is left in the spawn guard's file outside
  `TYPED_INPUTS`. Observed by AC26.
- **S27** — id 12. Unit 45 §5's risk line names the case the CLI admits: a one-line `--input diff` that
  is a lone fence run refuses as an open fence, and such content is handed as `input:spec`. Observed by
  AC27.
- **S28** — id 38. The risk line also names `input:question` quoting one line of a fence pair, with its
  remedy, close the fence or hand the text as a file; the pass renders that case and sees it refused.
  Observed by AC28.
- **S29** — id 19. Unit 46 §4 Inventory says `.lexicon.conf` arms `js.function` and no JS constant or
  file cell. Observed by AC29.
- **S30** — id 26. `check_block_fences` drops its end-of-walk clause; `TOOL-dBoundRoles-38` S5 stays the
  one owner of that refusal, as 48 §3 says. Observed by AC30.
  **Readers:** by name: `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-48.md:40-41`,
  S1's "a walk that ends inside one", the one place the clause is spelled; the function is minted at
  unit 48's pass, so no product file spells it at this unit's base. by value: `tools/roles/handoff.py`,
  whose `render_handoff` joins every refusal line into `refusals` and so the clause's line with it, and
  which still receives 38 S5's line for the same open walk.
- **S31** — id 27. One seed predicate. A function in `tools/govkit/govkit.py` filters `planned_writes`
  rows to seed writes, the condition `cmd_plan` inlines today (`:5050-5051`); `cmd_plan` and unit 49's
  `derive_seed_expected` both call it. Observed by AC31.
- **S32** — id 28. Unit 51's inversions have a disposition. An order inversion S1 or S6 finds is parked
  with `bash tools/unattended/unattended.sh --park dBoundRoles`, naming both units, and 51 AC1 checks
  that row exists when it finds one. Observed by AC32.
- **S33** — id 35. `help/roles.md` documents the three refusals: step 3's list gains the authored-line
  refusal of a typed input, and "What the hooks refuse" gains the typed-block denial and the block-fence
  denial. 45's, 46's and 48's §5 user-docs lines name the page. Observed by AC33.
- **S34** — id 49. Unit 51 AC8 derives its population with
  `git ls-files '*SKILL.md' '*SKILL.template.md'`, which holds `skills/deploy-governance/SKILL.md`.
  Observed by AC34.
- **S35** — id 50. 47's case covers the typed set. Its typed renders are derived from `INPUT_NAMES` less
  `PATH_INPUTS`, each name mapped to the role that reads it, `question` to `gov-orienter` and `diff` to
  `gov-skeptic`; a typed name with no mapped role fails the case naming it. Observed by AC35.

## 3. Non-goals (OUT)

- The six HIGH findings, `TOOL-dBoundRoles-52` to `-57`.
- Rewording specs 1 to 57 beyond what an item changes. Where an item changes a criterion or scope item of
  another unit, §4 "How an item closes" is the one route.
- The report's left-shift gates: the render-argument probe, the derived-expectation checklist entry, the
  fence parity bar test, the vanished-literal probe, the hooks-kit export lint, the typed-name lint, the
  bare-id token check, the ledger-block extractor, the gate-lint argv check and the help-page rule. No
  clause of this build names them; the items' own cases are the regressions.

### Edges

- **consumes-from** `TOOL-dBoundRoles-45` — `check_authored_lines`, AC1 and §5, which S4 to S6, S21, S22, S27, S28 and S33 complete (ids 4, 12, 35, 37, 38, 42, 45, 46)
- **consumes-from** `TOOL-dBoundRoles-46` — `TYPED_INPUTS`, S2's typed-block check, AC1, AC3 and §4, which S8 to S10, S16, S18, S25, S29 and S33 complete (ids 8, 9, 15, 19, 22, 24, 32, 35)
- **consumes-from** `TOOL-dBoundRoles-47` — the cross-unit case, which S1, S2 and S35 widen (ids 2, 39, 50)
- **consumes-from** `TOOL-dBoundRoles-48` — `check_block_fences`, S3's fence check, AC2 and AC3, which S7, S11, S12, S16 to S18, S26, S30 and S33 complete (ids 5, 10, 21, 22, 23, 24, 26, 33, 35)
- **consumes-from** `TOOL-dBoundRoles-49` — `derive_seed_expected`, whose filter S31 shares with `cmd_plan` (id 27)
- **consumes-from** `TOOL-dBoundRoles-50` — S8, AC3, AC4, AC7, AC12, AC20, AC22, S21 and §3, which S3, S14, S18 to S20, S23 and S24 restate (ids 3, 17, 24, 25, 31, 47, 48)
- **consumes-from** `TOOL-dBoundRoles-51` — S1, AC1, AC2, AC5, AC7, AC8 and §3, which S13, S23, S24, S32 and S34 restate (ids 11, 28, 47, 48, 49)
- **consumes-from** `TOOL-dBoundRoles-53` — `assert_role_reads` and its exit check, which S2 applies to every render of the case (id 39)
- **consumes-from** `TOOL-dBoundRoles-56` — the five fence-edge fixtures and the shared H1 rule, over which S15 observes each consumer (id 34)
- **consumes-from** `TOOL-dBoundRoles-25` — the spawn guard moved into `tools/roles/spawn-guard.js` and its export inventory, where S8 to S12, S16, S25 and S26 land, and AC14, which S24 bumps (ids 8, 9, 10, 15, 21, 22, 32, 33, 48)
- **consumes-from** `TOOL-dBoundRoles-41` — the graded text, which S17 builds from one extents record, and AC3, which S24 bumps (ids 23, 48)
- **consumes-from** `TOOL-dBoundRoles-43` — S56's `resolve_agent_transcript`, into which S19 folds the second resolver (id 25)
- **consumes-from** `TOOL-dBoundRoles-6` — `derive_section_sha` in `roles_lib.py`, which S18's criteria cite (id 24)
- **consumes-from** `TOOL-dBoundRoles-38` — AC4, which S24 bumps for unit 50's AMENDED answer (id 48)
- **consumes-from** `TOOL-dBoundRoles-42` — AC2 and AC4, which S24 bumps for units 50's and 51's AMENDED answers (id 48)
- **consumes-from** `TOOL-dBoundRoles-44` — AC8 and AC9, which S24 bumps for unit 51's AMENDED answers (id 48)
- **consumes-from** `TOOL-dBoundRoles-59` — `assert_role_reads` folded through unit 14's read-key parser, which S2 calls on every render of 47's case (id 21 of the round-1 audit of units 52 to 58)
- **hands-off** `TOOL-dBoundRoles-60` — S5, S9, S18, S21, AC5, AC6, AC18, AC21, AC30, §4 and §7, which unit 60 restates: criteria that can pass and can fail, the session-free control render, the AMENDED answer for 46 AC3, the write set and the floor moves (ids 1, 3, 9, 12, 15, 19, 22, 24, 29, 32, 37 and 38 of the round-1 audit of units 52 to 58)

## 4. Design

### Why one unit

M4 admits two units only when the minors split into two disjoint write sets by M6. They do not. Items
S4 to S6, S21, S22, S27, S28 and S33 bump spec 45; S18 bumps 46, 48 and 50 together; S23 and S24 bump 50
and 51 together; S33 writes `help/roles.md` for 45, 46 and 48; and S1, S2, S4, S7, S21, S22 and S35
write one suite. Every spec but 49 is joined to another through a shared item, and S31, the one item on
49, is one minor, which M4 does not make a unit of its own.

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a landed
unit already left it. Where an item changes what another unit's criterion or scope item says, the pass
bumps that unit's spec FIRST with the changed text and a §9 line naming this unit (BUILD-METHOD M2,
READY), and that unit's ledger answers the criterion `amended rev-<n>`, naming the revision. That is
S24's rule, applied here to this unit's own amendments, so no answer names a revision that does not
exist.

### Where each item lands at order 32

Units 25 (order 26), 43 (28), 50 and 51 (30) and 56 and 57 (31) have built. The spawn guard's code is in
`tools/roles/spawn-guard.js` and its suite in `tools/roles/spawn-guard.test.sh`; `agent-cap.js` is
retired. S8 to S12, S16, S25 and S26 land there. The roster is unit 1's: `gov-spec-reviewer` is merged
into `gov-reviewer`, which is why S4 renders `gov-builder`.

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/roles/agents/gov-builder.agent.md:7` and `gov-skeptic.agent.md:7` hold the reads S1 and S4
  rely on; `tools/roles/handoff.py:340-346` resolves a kickoff checker only for a `task:` key.
- `tools/hooks/agent-cap.js` ends with a bare `main()` and has no `module.exports`; `:2101-2103` denies
  on the marker count before any block is read; `:2050-2051` strips every `\r` before matching.
- `tools/check-dead-paths.sh` `--list` exits 0 before `stale_rows` is computed.
- `tools/govkit/govkit.py:5050-5051` inlines the seed-write condition in `cmd_plan`.
- `help/roles.md:20-24` lists the renderer's refusals and `:103` heads "What the hooks refuse".
- `memory/HYGIENE.md` "Acceptance ledger" gives the AMENDED form as `amended rev-<n>`, naming the
  revision and its §9 line.

### Inventory

Minted: `readTaskBlocks` (`js.function`), the extents record of S17, the seed predicate of S31
(`py.function`), and the cases of S1, S7, S10, S12, S21, S22, S28 and S35. Each name is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as <cell>` at the pass.

### Migration

None: no stored data changes. S24 rewrites ledger answer lines this build's own passes wrote.

### Rollout

Live at landing, at order 32, after every unit it repairs and every HIGH promotion of the same audit.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`
- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/spawn-guard.js`
- `tools/roles/spawn-guard.test.sh`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `help/roles.md`
- the specs of units 25, 38, 41, 42, 44, 45, 46, 47, 48, 49, 50 and 51, rev bumps, and the ledgers
  S24 corrects, named here for the dispatch write set

### Alternatives rejected

- **Two units.** No cut leaves two disjoint write sets with more than one minor on each side.
- **AMENDED answers naming this unit, as rounds 1 and 2 did.** That is id 48's defect; §4 "How an item
  closes" is its correction.
- **Keep two task-section splitters at spawn (S16) or two extents records at render (S17).** Each pair
  grades one defect two ways.

## 5. Production-readiness checklist

- security — S16, S21, S22 and S25 close a split-view and a CR-split forgery path and a preempted
  denial; S11 keeps the typed exemption from going stale. No new write path.
- perf / scale — renders, payloads, greps and one walk per block reader.
- error / empty / loading states — S35 fails a typed name with no role; S32 parks an inversion.
- observability — the ledger records S15, S24 and S10's inventory line.
- risks — S24's bumps touch five converged specs; each moves only the answered criterion.
- testing — AC1 to AC35 by render, payload, probe and grep; the arms of §7 at the close.
- migration — none.
- user docs — `help/roles.md` by S33.

## 6. Acceptance criteria

The ledgers below are read block-scoped, as S23 states: from the unit's `**Evidences:**` line to the next
`**Evidences:**` line or heading.

- **AC1** — When the roles adopter fixture renders `--role gov-skeptic` with `--input diff=` carrying
  `record:TOOL-tFix-9@000000000000` and `--input spec=` quoting it, it exits 1 naming the span once; a
  plain-words diff renders. Red when: the typed diff's span passes.
- **AC2** — When a scratch copy of 47's case drops `input:spec` from S1's role, the case fails at
  `assert_role_reads` naming the key. Red when: a render of the case reaches a verdict with an unread key.
- **AC3** — When `grep -n 'gov-skeptic' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-50.md`
  runs, it prints S8 and AC8. Red when: 50's renders still name no role that reads both inputs.
- **AC4** — When the fixture renders `--role gov-builder --input spec=<scratch spec>` with no brief record,
  it exits 0 and the spec's bytes sit inside a fence. Red when: the control render refuses for a missing
  brief.
- **AC5** — When `python -c` reads the `reads` of 45 AC1's control role through `roles_lib.load_roles`, it
  holds no `task:` key and no required `brief:` key. Red when: the control role needs a card or a brief.
- **AC6** — When `grep -n 'gov-builder' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-45.md`
  runs, it prints AC1, and the spec's §9 names `TOOL-dBoundRoles-58`. Red when: AC1 still renders a role
  the fixture cannot satisfy.
- **AC7** — When the render case of S7 runs against `render_handoff` with `check_block_fences` reduced to
  the end of the walk, the case reads red; restored, it refuses naming the handed block. Red when: the
  staged break leaves the render case green.
- **AC8** — When `grep -n 'require.main === module' spawn-guard.js` runs in `tools/roles/`, it prints the
  entry line. Red when: requiring the file runs the hook.
- **AC9** — When `node -e` requires the spawn guard's file with stdin closed and prints `TYPED_INPUTS`, it
  prints `question` and `diff` and exits 0 at once. Red when: the require hangs on stdin or exits first.
- **AC10** — When the spawn-guard suite pipes a rule-6 payload and a forged one to `node spawn-guard.js`,
  the first exits 0 and the second 2. Red when: the entry change alters what the hook decides.
- **AC11** — When `grep -n 'TYPED_INPUTS' spawn-guard.js` runs in `tools/roles/`, it names the
  exemption's line. Red when: the exemption spells its own names.
- **AC12** — When a scratch copy adds `extra` to `TYPED_INPUTS` and pipes a payload whose
  `### input:extra` block holds an unfenced line, the fence-shape half admits it. Red when: a new typed
  input is denied as a handed block.
- **AC13** — When `git log --reverse --format=%s <BASE>..HEAD | grep -nE '^build\(dBoundRoles\): TOOL-dBoundRoles-3 '`
  runs, it prints unit 3's pass and not unit 37's. Red when: a prefix id answers for another.
- **AC14** — When `bash tools/check-dead-paths.sh` runs on the built tree, it exits 0 with no
  `stale waiver(s)` line. Red when: a stale row is read from a mode that never computes it.
- **AC15** — When a `python -c` probe runs `gen_build_index.spec_ids` and the extractor's anchor over unit
  56's fixtures, each names `parse_spec_h1`'s id. Red when: a consumer resolves a spec another way.
- **AC16** — When `grep -n "startsWith('### ')" spawn-guard.js` runs in `tools/roles/`, it prints only
  `readTaskBlocks`' line, and a fenced `### input:question` line in a handed block opens no typed block.
  Red when: two splitters read one section two ways.
- **AC17** — When `grep -n 'handed' tools/roles/handoff.py` runs, the flag is set in one place, and a
  probe shows `check_block_fences` and the graded text read the same records. Red when: two classifiers
  grade different blocks as handed.
- **AC18** — When `git grep -n 'handoff.derive_section_sha' -- tools memory/builds/dBoundRoles/spec`
  runs, it prints nothing. Red when: a criterion calls a function unit 6 moved.
- **AC19** — When `grep -c '"subagents"' tools/roles/handoff.py` runs it prints 1, and `grep -n
  'resolve_subagent_dir' tools/roles/handoff.py` prints nothing. Red when: the session layout is spelled
  twice.
- **AC20** — When `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`
  runs on the built tree, it exits 0, and 50 AC12 spells that argv. Red when: the criterion scans paths
  the leg excludes.
- **AC21** — When the fixture renders `--input question=` holding `\r` followed by a whole `gov:handoff`
  marker line, it exits 1 naming the line. Red when: a CR-split marker passes the render.
- **AC22** — When the fixture renders a question holding a closed three-backtick fence around
  `# install deps`, it exits 0, and the same line unfenced refuses. Red when: a comment inside a closed
  fence is refused, or a heading outside one passes.
- **AC23** — When `grep -nE '<unit .* acceptance ledger>' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-51.md`
  runs, every match is scoped to its unit's block. Red when: a criterion greps a whole ledger.
- **AC24** — When a `python -c` probe reads every `amended rev-<n>` answer in this build's ledgers, each
  names a revision whose spec carries that §9 line, and no answer reads `AMENDED, naming`. Red when: an
  answer names a revision nobody wrote.
- **AC25** — When the spawn-guard suite pipes a payload whose `### input:question` holds a whole
  `gov:handoff` marker line, it exits 2 naming `input:question`. Red when: the count denial preempts it.
- **AC26** — When `grep -nE "'question'.*'diff'|\"question\".*\"diff\"" spawn-guard.js` runs in
  `tools/roles/`, it prints only `TYPED_INPUTS`' line. Red when: a second typed list exists.
- **AC27** — When `grep -n 'lone fence run' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-45.md`
  runs, it prints §5's risk line. Red when: the risk names hunk context the CLI refuses.
- **AC28** — When the fixture renders `--input question=` holding one line of a three-backtick fence, it
  exits 1 naming the open line. Red when: the risk's case cannot be reached.
- **AC29** — When `grep -n 'js.file' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-46.md`
  runs, it prints no claim that the cell is declared. Red when: the inventory miscites the conf.
- **AC30** — When `grep -n 'ends inside' tools/roles/roles_lib.py` runs, it prints 38 S5's refusal only.
  Red when: two functions refuse one open walk.
- **AC31** — When govkit's self-test module is imported by a `python -c` slice and `derive_seed_expected`
  and `cmd_plan` are read, both call S31's predicate. Red when: the seed condition is spelled twice.
- **AC32** — When `grep -n 'unattended.sh --park' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-51.md`
  runs, it prints S1. Red when: an inversion has no record the main loop reads.
- **AC33** — When `grep -n 'typed input' help/roles.md` runs, it prints the step 3 refusal and the two
  hook bullets. Red when: an operator meets a refusal the page omits.
- **AC34** — When `git ls-files '*SKILL.md' '*SKILL.template.md' | xargs grep -nwE 'Grep|Glob'` runs on
  the built tree, it prints nothing. Red when: a Skill outside the typed glob names a refused tool.
- **AC35** — When a scratch copy of `tools/roles/handoff.py` adds a typed name to `INPUT_NAMES`, 47's case
  fails naming it. Red when: a typed input escapes the cross-unit case.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `roles render selftest` · `agent-cap self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `build-index selftest` · `memory-recall kit selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`agent-cap self-test` stands for the spawn guard's suite; unit 25's pass renames it on every live §7
line when it renames the leg.

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 AC4 AC7 AC21 AC22 AC28 AC35 · the diff render, the read check, the control render, the balanced flip, the CR and comment cases and the typed-set loop, staged by a fenced typed value, an end-only fence check and an unmapped typed name · none
New arm: tools/roles/spawn-guard.test.sh · covers AC10 AC12 AC16 AC25 · the entry guard, the derived exemption, the one block reader and the check order, staged by a literal exemption and a marker count moved first · none
New arm: tools/govkit/selftest.py · covers AC31 · the shared seed predicate, staged by an inlined copy in `cmd_plan` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause; veto 1 discards
  (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1
  set. widens: none · relaxes: none
- **F2 — Where does an inversion found by unit 51 go (id 28)?** Options: (a) a parked row through
  `--park`; (b) an ask in this build's `BACKLOG.md`. The main loop reads verdicts, rosters and parked
  rows, never asks mid-run (`memory/gotchas/orchestrator-hand-off-owed-a-disposition.md`). RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the record the reader reads. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the 24 MEDIUM and 11 LOW findings of the round-1 audit of units 45
  to 51, each id its own item, in one unit.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-59 and TOOL-dBoundRoles-60, the HIGH promotion and the minors batch of the round-1 audit of units 52 to 58; nothing else moved.

## 10. Reuse audit

The seams are the units' own: 53's `assert_role_reads`, 38's walkers, 46's `TYPED_INPUTS`, 43 S56's
`resolve_agent_transcript`, 56's fixtures, `planned_writes` in `tools/govkit/govkit.py`, and the AMENDED
grammar of `memory/HYGIENE.md`, each extended rather than copied.
`python tools/codebase-map/reuse_lookup.py "close many small spec audit findings in one batch"` ranked
`audit`, `read_spec_revisions`, `parse_spec_h1` and `build_spec_path_re`, none a batch mechanism, so no
existing seam fits beyond those named.

Recall terms used: `python tools/memory-recall/query.py "how is handed content kept from forging machine-read lines in a work order" --terms "fence walker marker reader typed input block extents spawn guard amended revision ledger"`
