**Serves:** research TOOL-dFurnishedOrders-1

# dFurnishedOrders' specs against dBoundRoles' re-grounded specs: a read-only cross-check

Node d, 2026-10-28, base `1a61f21a2` (origin/main). dFurnishedOrders' spec run began at `1a3ce03dd`,
the parent of its first spec commit `4d726ef27`. That base holds the second wave's re-grounds but none
of the third wave's: dBoundRoles' (`ac8ab8d5f`, landed as `fffe4aadf`), dTotalRecall's (`794a0f5fb`,
landed as `2bd5e10d4`) or dKeptSession's (`ff44fb2a2`, landed as `0689e7fa1`). Their deviation records
confirm what each revised: dBoundRoles units 1, 2, 3, 5, 6, 11, 12, 14, 20, 21, 22, 23, 25, 43 and 60;
dTotalRecall units 1, 2, 4, 8, 9, 11, 15, 18, 19, 20, 22, 25, 26, 43 and 76; dKeptSession units 1, 5, 7
to 13, 18, 20, 25, 36, 44 and 56. This record compares each assumption the exposed specs make about a
parent with what the parents' DEFERRED specs say now. It is not an audit: no spec was edited, no review
harness ran, and the mismatches feed the re-ground brief
[`2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground`](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md).

**Counts:** 127 assumptions · 83 AGREES · 37 MISMATCH · 7 UNKNOWN UNTIL BUILT, over 39 specs (the 30
citation specs and the 9 rule-wide hits the readers found bound; the other 12 hits are not bound). 22
specs hold at least one MISMATCH: 2, 3, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 20, 29, 37, 42,
46, 48, 50 and 58. By rule: 14 citation, 7 R1, 15 R3 and 1 R8. 3 mismatches sit outside the citation
population, found only by rule scoping: rows 124 (fo48), 126 (fo50) and 127 (fo58), all R1, all hand
edits of the `govkit selftest` row. 12 mismatches come from a re-ground: rows 6, 19, 35, 63, 77 and 98
(br21's `with_default`, which br43 makes the catalogue-default read), 73 and 120 (br43's "imports the
policy kit" clause), 99 (br43 AC21's predicate), 71 (br3 naming the `declaration --item` verb), 60 (br2
F4's `answered` outcome) and 50 (br1's roster moved nine lines). The other 25 were already mismatches
at `1a3ce03dd`; rows 32, 46 and 51 gain the `with_default` form from the re-ground on top.

## Method

- **Population by citation.** `grep -oE` over `spec/*.md` for the units the three re-grounds revised,
  both `<FAMILY>-<build>-<n>` and the bare `<build>-<n>`. That gives 30 specs: 25 cite a dBoundRoles
  unit, 11, 17, 41 and 45 a dTotalRecall unit, and 42 and 46 dKeptSession's unit 44.
- **Population by rule.** The brief restates R1 to R8 from the parents' cross-check records and the
  third wave's own seams, and a text probe for each over the other 30 specs named 21 candidates. The
  reader found 9 of them bound (fo13, fo25, fo26, fo33, fo34, fo39, fo48, fo50, fo58), of which fo48,
  fo50 and fo58 hold a mismatch; the rest are scratch-clone fixtures, reads of a parsed manifest, the
  roles kit calling its own library, or CPU contention rather than dl33's budget.
- **Readers.** Three `gov-spec-reviewer` agents, read-only, one per group of the brief
  [`2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck`](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck.md),
  their handoffs beside it. Groups A1 and A2 are the citation population and applied R1 to R8 to their
  own specs; group B verified the rule-wide hits. Their returns, with every MISMATCH's both sides
  quoted, its `Change:` and its `Cause:`, are
  [`2026-10-28-build-TOOL-dFurnishedOrders-1-crosscheck-returns`](2026-10-28-build-TOOL-dFurnishedOrders-1-crosscheck-returns.md).
- **The main loop** assembled the table from the returns' tables by script, sorted by spec, and
  derived the counts from it. It changed no verdict. Two readers' prose counts disagree with their own
  tables (A1 says 39, 21 and 3, its table 45, 17 and 1; A2 says 52 rows, its table 54); the tables win.
  A1's prose names two UNKNOWN lines with no table row (fo2's `read_agent_limit` with no policy kit,
  and fo4 and fo9 waiting on br3 F5's verb); they are kept under UNKNOWN UNTIL BUILT below.
- **Aliases:** `foN:L` is line L of `spec/2026-10-2?-spec-TOOL-dFurnishedOrders-N.md`; `brN:L`,
  `trN:L`, `ksN:L`, `ocN:L`, `dlN:L`, `wbN:L` and `prN:L` of the parents' spec N under
  `../../<build>/spec/`; all at `1a61f21a2`.
- **What it does not check:** anything a parent's build run decides; dSafePassage and dGroundRules
  surfaces dFurnishedOrders names directly; specs neither population reached (fo21, fo35, fo36, fo38,
  fo40, fo43, fo44, fo47, fo51 and fo57, whose probe hits were only the word `witness` or `budget`).
  The rule-wide probe is a text heuristic. No skeptic re-ran the verdicts. Instead each re-ground
  writer re-reads both sides before it edits, and returns a row it cannot bear out as refused.

## What the mismatches have in common

- **A catalogue default typed in the roles kit (fo2, fo5, fo8, fo16, fo17, fo18, fo29).** Citation,
  from the re-ground. br21 rev-3 gives `read_policy_setting` a `with_default` argument, and br43 S21
  makes it the form a catalogue-default read takes; each spec still reads None as the default and
  types the default's value in the roles kit. None then means only that no policy kit was found.
- **A sibling kit reached in process (fo3, fo6, fo7, fo10, fo11, fo12, fo14, fo17, fo29, fo37, fo42,
  fo46).** R3. Policy keys read through the policy kit's `resolve` (fo3, fo7, fo11, fo12, fo17); runlog's
  `extract.py`, memory-tree's `backlog.py` and `legacy_ledger.py`, the playbook kit's `gov_tag.py` and
  the policy kit's `budgets.py` loaded by file (fo3, fo7, fo10, fo11, fo14, fo29, fo42); a hook
  `require`s `readPolicy` (fo6); the lexicon kit called in process (fo46); and fo37's sibling-import
  check, which greps only `import` lines and so blesses the by-file loads. br43 now says no file under
  `tools/roles/` imports the policy kit (rows 73 and 120 from the re-ground); the rest pre-existing.
- **A leg edited by hand (fo6, fo29, fo37, fo46, fo48, fo50, fo58).** R1. The `answered-calls
  self-test` leg is written into `tools/gate-legs.json` with no `enforces` (fo6) and re-guarded there
  (fo29 S19, fo37 S24); the `govkit selftest` leg, an `[[exempt_leg]]` row at
  `tools/govkit/registry.toml:439`, is re-guarded in the manifest by four specs (fo46, fo48, fo50,
  fo58). wb11 makes the manifest a render of the declarations. Pre-existing.
- **br3's `--item` render (fo17, fo20, fo29).** br3 S1 runs `loop_lib.py declaration --item <tag>
  --json` in a subprocess and refuses with exit 1 when no loop kit is found, so fo17's and fo20's
  `not-installed` branches are dead and the stubs in fo17 AC2 and fo29 AC8 answer the wrong verb.
- **Single defects:** fo12 F1's probe pinned to lines br1's roster left (re-ground); fo15's tester
  template missing br2 F4's `answered` outcome (re-ground); fo17's `neighbourhood` reader, which tr8
  does not land (open asks TOOL-dTotalRecall-102 and -103); fo20's `read_claims`, which pr1 now fetches
  over two namespaces.

## Summary table

| # | Spec | Group | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | fo1 | A1 | The scout's placement return and the driver's record of it belong to br12, and the scout still returns the card | cite | AGREES | fo1:105, :89; br12:37-41 ("beside the card body the role already returns"), :43-49 |
| 2 | fo1 | A1 | The card's recall check runs `map_diff.py` as a subprocess found by `resolve_kit_file` | R3 | AGREES | fo1:67-75 |
| 3 | fo1 | A1 | `render_handoff` runs the codebase-map verb, found by `resolve_kit_dir` (fo29 S23) | R3 | AGREES | fo1:81-83; fo29:138 |
| 4 | fo2 | A1 | The `return` grammar has a `list` type that can carry `tasks` | cite | AGREES | fo2:49-53, :250; br2 "The return template" (`type := … "list"`) |
| 5 | fo2 | A1 | `validate_return` checks the shape, and the batch join is added on top | cite | AGREES | fo2:82-83; br5:35-48 |
| 6 | fo2 | A1 | `read_policy_setting("prompts.batch", root)`: None means the catalogue default `per-batch`; no policy kit means `per-task` | cite | MISMATCH | fo2:63-67; br21:41-50; br43:105-110 |
| 7 | fo2 | A1 | `read_agent_limit(root)` bounds the batch | cite | AGREES | fo2:46-47; br22:53-57 |
| 8 | fo2 | A1 | Stage rows (`fan`) exist only on `workflow`-driver entries | cite | AGREES | fo2:78, :157-159; br22:34-37 |
| 9 | fo2 | A1 | The matrix is read through `loop_items.py matrix` as a subprocess | R3 | AGREES | fo2:43-45 |
| 10 | fo3 | A1 | br5 S3's return-check record is not where notices persist | cite | AGREES | fo3:80-81; br5:56-63 |
| 11 | fo3 | A1 | runlog's `extract.py` reads `notices.record` through an in-process `resolve` | R3 | MISMATCH | fo3:42-46; oc7:202-205, :379-380 |
| 12 | fo3 | A1 | `handoff.py` loads runlog's `extract.py` by file | R3 | MISMATCH | fo3:54-56, :163-164, :241; oc7:202-205 |
| 13 | fo4 | A1 | Work orders are br3's and gain a block | cite | AGREES | fo4:131; br3:S2 |
| 14 | fo4 | A1 | `### bug-classes` sits in br23's `boundaries` slot | cite | AGREES | fo4:55, :341-344; br23:43-44, :123 |
| 15 | fo4 | A1 | br23's rule for an empty slot never applies to a slot block | cite | AGREES | fo4:40-41; br23:131 |
| 16 | fo4 | A1 | The lookup runs `gotchas.py --for-names` as a subprocess via `resolve_kit_dir` | R3 | AGREES | fo4:57-59 |
| 17 | fo5 | A1 | `role-schema.toml` `[[field]]` rows, `shape = "list"`, `required = "every"` | cite | AGREES | fo5:33-35; br2 "The schema" table |
| 18 | fo5 | A1 | `## Trust` is appended after br2 S6's `## Return` | cite | AGREES | fo5:41-44; br2 S6 |
| 19 | fo5 | A1 | `read_policy_setting`: None (default or no kit) renders `keyed`/`cold` typed in the roles kit | cite | MISMATCH | fo5:45-48; br21:41-50; br43:105-110 |
| 20 | fo5 | A1 | The roster includes br1's new roles, among them `gov-reviewer` and `gov-tester` | cite | AGREES | fo5:93-100, :106-107; br1:131-143 |
| 21 | fo5 | A1 | The tester's packet is its br3 work order | cite | AGREES | fo5:76-77; br3 S2 |
| 22 | fo5 | A1 | br20's composition requires every structured field on a repository role | cite | AGREES | fo5:176-178; br20 S3 ("carries every structured field gov's carry") |
| 23 | fo5 | A1 | The verifier context is read by `policy.py get … --rev HEAD` at render time | R6 | AGREES | fo5:56-58 |
| 24 | fo6 | A1 | The fragment layout follows br25 S2 | cite | AGREES | fo6:80-81; br25:50-53 |
| 25 | fo6 | A1 | Wiring follows br5 S5 (`--scaffold` merge, roles arm of `check-wiring.sh`) | cite | AGREES | fo6:81-82; br5 S5 |
| 26 | fo6 | A1 | New leg `answered-calls self-test` hand-written into `tools/gate-legs.json` with no `enforces` | R1 | MISMATCH | fo6:82-86, :203; wb11:36-50; oc7:58-63 |
| 27 | fo6 | A1 | `answered-calls.js` `require`s the policy kit's `readPolicy` | R3 | MISMATCH | fo6:57-58, :124, :345; ks8:62-66 |
| 28 | fo6 | A1 | `answered-calls.js` requires `scratch-guard.js` exports (the helper home br25 S4 gives) | R3 | AGREES | fo6:21-22, :26-30; br25:58-63; fo29:131-133 (S20 `requires_if`) |
| 29 | fo7 | A1 | `role-schema.toml` gains `[return.repair]` | cite | AGREES | fo7:30-36; br2 S1 |
| 30 | fo7 | A1 | `validate_return` refuses a malformed `contradicted` return | cite | AGREES | fo7:36-38; br5:35-48 |
| 31 | fo7 | A1 | br11's reader answers kind `refusal` (added by br26) | cite | AGREES | fo7:131-133; br11:60-70; br26:55 |
| 32 | fo7 | A1 | `roles.on-contradiction` is read through an in-process `resolve` | R3 | MISMATCH | fo7:53-54; oc7:379-380; br43:105-110 |
| 33 | fo7 | A1 | `handoff.py` calls memory-tree's `render_ask_row`/`render_sev_row`/`render_status_row` in process | R3 | MISMATCH | fo7:60-63; oc7:202-205 |
| 34 | fo8 | A1 | `slices` field row: `shape = "list"`, `required = "optional"` | cite | AGREES | fo8:32-34; br2 "The schema" table |
| 35 | fo8 | A1 | `instructions.slices`: None renders the catalogue default `handed` | cite | MISMATCH | fo8:50-52; br21:41-50; br43:105-110 |
| 36 | fo8 | A1 | Thirteen role files once br1 adds its roles and the reviewers merge | cite | AGREES | fo8:132-135; br1:129-147 (gov's own merge is br1 S3, not br18, but the count holds) |
| 37 | fo8 | A1 | Slices are resolved through `gov_tag.py where` as a subprocess | R3 | AGREES | fo8:39-41 |
| 38 | fo9 | A1 | The role index carries `layer` and `acts-as` (br1 S6) | cite | AGREES | fo9:35-36; br1 S6 |
| 39 | fo9 | A1 | Arm 3 (br1 S7) grades the composed loop, repository rows included | cite | AGREES | fo9:62-63, :94-96; br1 S7 (rev-3) |
| 40 | fo9 | A1 | Other kits reach the `matrix` verb by subprocess, as br3 S1 reaches the loop kit | cite | AGREES | fo9:57-58; br3 S1 |
| 41 | fo9 | A1 | br20 S7 reads arm 2 over the composition | cite | AGREES | fo9:73-74; br20 S7 |
| 42 | fo10 | A1 | Retries are br5's, and are not counted here | cite | AGREES | fo10:83-84; br5 S3 |
| 43 | fo10 | A1 | The roles kit loads runlog's `extract.py` by file; `derive_role_matrix` is looked up from the roles kit | R3 | MISMATCH | fo10:54-58, :67-70, :266-275; oc7:202-205 |
| 44 | fo11 | A1 | `record_find.py` sits in memory-tree, found by `resolve_kit_dir` (tr9 S5) | cite | AGREES | fo11:37-39; tr9:104-107 |
| 45 | fo11 | A1 | The slot body is tr9 S8's `reads:` list; the budget is `gov_record.py budget` on `memory.item-budget`/`over-budget` | cite | AGREES | fo11:39-42; tr9:108-125 |
| 46 | fo11 | A1 | `retrofit.slot-bytes` and `roles.orientation.house-index` are read through an in-process `resolve` | R3 | MISMATCH | fo11:67-71; oc7:379-380 |
| 47 | fo11 | A1 | memory-tree's `legacy_ledger.py` is loaded by file | R3 | MISMATCH | fo11:136, :143-144; oc7:202-205 |
| 48 | fo12 | A1 | `every-role` comes from the index's `acts-as` (br1 S6) | cite | AGREES | fo12:35-36; br1 S6 |
| 49 | fo12 | A1 | The item's `map` comes from the declaration br3 S1 reads at render | cite | UNKNOWN UNTIL BUILT | fo12:83; br3 S1, :266-278 (F5) |
| 50 | fo12 | A1 | F1's probe `sed -n 120,134p` over br1 finds 12 `layer.roles` rows and 1 `layer.runtime` row | cite | MISMATCH | fo12:218-225; br1:131-143 |
| 51 | fo12 | A1 | `memory.project-map` and `memory.map-unfold` are read through an in-process `resolve` | R3 | MISMATCH | fo12:60-63; oc7:379-380 |
| 52 | fo13 | B | The kickoff engine only checks that memory-tree's `gov_map.py` exists, through `resolve_kit_file`, and imports nothing; the scout runs it as a command line | R3 | AGREES | fo13:36-38, :53-55; oc7:202-205 |
| 53 | fo14 | A1 | Work order input blocks are br3's | cite | AGREES | fo14:84; br3 S2 |
| 54 | fo14 | A1 | A helper two kits read lives in `scratch-guard.js` exports (br25 S4) | cite | AGREES | fo14:41-48, :96; br25:58-63; fo29:131-133 |
| 55 | fo14 | A1 | `roles_lib` calls memory-tree's `backlog.py` `parse_file`/`derive_statuses` in process | R3 | MISMATCH | fo14:66-69, :324-325; oc7:202-205 |
| 56 | fo15 | A1 | br43 S13's refusal-arm composition in `render_role` is what the factory generalises | cite | AGREES | fo15:34-37; br43:86-89 |
| 57 | fo15 | A1 | `validate_return` refuses a malformed `probe` return | cite | AGREES | fo15:50-52; br5:35-48 |
| 58 | fo15 | A1 | `gov-tester` already carries `layer`/`acts-as` from br1 | cite | AGREES | fo15:86-87; br1 S2 |
| 59 | fo15 | A1 | `never` entries follow br2's `<limit> — <enforcer>` grammar | cite | AGREES | fo15:141-143; br2 S2 |
| 60 | fo15 | A1 | The tester's `return` is `outcome:code-miss\|spec-wrong\|designed\|judged, evidence, method?, losing?`, with `test.reason` returning `code-miss`/`spec-wrong` | cite | MISMATCH | fo15:129, :133-137; br2:324-338 |
| 61 | fo16 | A1 | br11 S5's door `owner-question --kind [--attended]` and `resolve_owner_question(kind, attended, repo, rev)` | cite | AGREES | fo16:49-58; br11:60-70 |
| 62 | fo16 | A1 | br11 S6's FORKED case answers resolve/park-item/park-build/stop-run | cite | AGREES | fo16:64-67, :147; br11 S6 |
| 63 | fo16 | A1 | `read_policy_setting("attendance", root)`: None reads `unattended` | cite | MISMATCH | fo16:35-36; br21:41-50; br43:105-110 |
| 64 | fo16 | A1 | `breakpoints.py list` and `runlog.py turns` are reached as subprocesses | R3 | AGREES | fo16:35-45 |
| 65 | fo17 | A2 | `code_record.py` lands in the memory-tree kit, found with `resolve_kit_dir("memory-tree", "code_record.py", …)` | cite | AGREES | fo17:43-45 · tr8:48-51, :204 |
| 66 | fo17 | A2 | A kit sibling is a file-level relation with no range (tr8 S6 kit membership) | cite | AGREES | fo17:99-101, :229-233 · tr8:66-68 |
| 67 | fo17 | A2 | The record holds what the row grammar needs: kind, qualified name, `line`, `end_line`, call edges and test edges | cite | AGREES | fo17:90-96 · tr8:50-51, :66-67, :69-71, :155-158 |
| 68 | fo17 | A2 | tr8 "lands a `neighbourhood` reader printing §4's rows" (the hands-off edge) | cite | MISMATCH | fo17:83, :43-44 · tr8:117, :136. `grep -c neighbourhood` over tr8 prints 0. `memory/builds/dTotalRecall/BACKLOG.md:15-16` (asks TOOL-dTotalRecall-102 and -103) are still open |
| 69 | fo17 | A2 | `code_record.py` answers the unknown verb `neighbourhood` with exit 2 | cite | UNKNOWN UNTIL BUILT | fo17:46-47 · tr8:43-47, :74-75, :255-310 (flags only: `--time`, `--check`, `--dump`, `--fixture`, `--ceiling`) |
| 70 | fo17 | A2 | A `degraded` record is the reader's problem, not the slot's | cite | UNKNOWN UNTIL BUILT | fo17:70 · tr8:79-80, :175 |
| 71 | fo17 | A2 | A `--item` render with a stub `loop_lib.py` that prints only the seed's `unarmed` line reaches the `code` block (AC2) | cite (br3 S1 reads br17's `--item`) | MISMATCH | fo17:184-187 · br3:39-47, :266-280 |
| 72 | fo17 | A2 | A missing loop kit renders `not-installed` | cite | MISMATCH | fo17:40-41 · br3:46-47 |
| 73 | fo17 | A2 | `memory.code-budget` and `memory.code-roles` are read through "J1's policy read" (J1 allows an in-process `resolve`), and the AC1 fixture is justified by `resolve` | R3 | MISMATCH | fo17:50-51, :183 · brief J1 (`prompts/…-spec-brief.md:175`) · br21:41-48 · br43:105-110 · oc7:202-205 |
| 74 | fo17 | A2 | Seed and record reader are both reached by subprocess | R3 | AGREES | fo17:38-40, :43-45 · oc7:202-205 |
| 75 | fo18 | A2 | A work order cut with `--item` exists, and AC3 renders one in a scratch adopter | cite | UNKNOWN UNTIL BUILT | fo18:41-42, :210-215 · br3:41, :266-280 |
| 76 | fo18 | A2 | `read_policy_setting(key, root)` runs `get` and returns None on a default | cite | AGREES | fo18:47-48 · br21:41-48 |
| 77 | fo18 | A2 | `annotations.delivery`: on None the code substitutes the literal `work-order` | cite | MISMATCH | fo18:69-71 · br21:46-47 · br43:105-109 |
| 78 | fo18 | A2 | `### instructions` sits in br23's `boundaries` slot beside the charter rule blocks | cite | AGREES | fo18:132-133 · br23:42-43, :123 |
| 79 | fo18 | A2 | `load_sets.py derive` and `gov_tag.py bundle` are reached by subprocess | R3 | AGREES | fo18:42-43, :61-62 · oc7:202-205 |
| 80 | fo19 | A2 | `validate_return(role, text, root, work_order)` and its template read | cite | AGREES | fo19:44-47, :58-63 · br5:37-49 |
| 81 | fo19 | A2 | `check-return` blocks and re-asks while attempts are fewer than `roles.retries` | cite | AGREES | fo19:66-68, :251-255 · br5:55-69 |
| 82 | fo19 | A2 | br5 S6's `spawnWithRetries` re-runs a null return | cite | AGREES | fo19:78-79 · br5:76-82 |
| 83 | fo19 | A2 | br5 leaves the per-order schema out | cite | AGREES | fo19:32-33 · br5:100-101 |
| 84 | fo19 | A2 | Template types are `text`, `path`, `sha`, `list`, `int` and a closed set | cite | AGREES | fo19:117-124 · br2:115, :162 |
| 85 | fo20 | A2 | A `--item` render reaches `### problems` (AC4, AC6) | cite | UNKNOWN UNTIL BUILT | fo20:57-58, :238-252 · br3:41, :266-280 |
| 86 | fo20 | A2 | "no loop kit" renders `not-installed` | cite | MISMATCH | fo20:63-66 · br3:46-47 |
| 87 | fo20 | A2 | The block sits in br23's `material` slot after the `reads` blocks | cite | AGREES | fo20:159 · br23:122 |
| 88 | fo20 | A2 | `read_claims` calls the one-namespace `read_gov_namespace` with `refs/gov/runs` only, its rows unchanged | R8 | MISMATCH | fo20:30-36, :255 · pr1:76-80 |
| 89 | fo20 | A2 | Seed and driver are reached by subprocess | R3 | AGREES | fo20:57-66 · oc7:202-205 |
| 90 | fo22 | A2 | br2 S1's `[[field]]` grammar (`key`, `owner`, `shape`, `required`) and the `list` shape | cite | AGREES | fo22:41-44 · br2:33-38, :115 |
| 91 | fo22 | A2 | br1 S3 merges the reviewers into `gov-reviewer` | cite | AGREES | fo22:93 · br1:68-70, :158-159 |
| 92 | fo24 | A2 | br5 S1 keeps the unknown-field check | cite | AGREES | fo24:97-98 · br5:43-44 |
| 93 | fo25 | B | The step reads `MEMORY_ROOT` without loading memory-tree's `tree_lib.parse_conf` in process (S4's load, retired by fo37 S34) | R3 | AGREES (as amended by fo37) | fo25:47-50 loads `tree_lib` by path; fo37:208-211 replaces it with govkit's own `parse_conf_assignment`; tr20:38-42, :299-305 |
| 94 | fo26 | B | `derive_attended` reads runlog's owner turns through the `runlog.py turns` subprocess, not by importing `extract.py` | R3 | AGREES | fo26:63 ("the `turns` verb it reads"); fo16:43, :231; fo37:105 |
| 95 | fo27 | A2 | br11 S6 adds a FORKED case to `verb_dispatch` | cite | AGREES | fo27:28, :168 · br11:71-76 |
| 96 | fo27 | A2 | The driver reaches `handoff.py owner-question` by subprocess | R3 | AGREES | fo27:37-38 · br11:66 |
| 97 | fo28 | A2 | `run.on-owner-question` answers the away case | cite | AGREES | fo28:83-85 · br11:67-69 |
| 98 | fo29 | A2 | S9: "a None reading the catalogue default" and "no `resolve_kit_dir("policy", "policy.py", ...)` import is left in `tools/roles/`" | cite | MISMATCH | fo29:92-95 · br21:43, :46-47 · br43:105-109 |
| 99 | fo29 | A2 | AC7's predicate `import policy\|[^.]\bresolve\(` catches a second policy reader | cite | MISMATCH | fo29:306-309 · br21:41-43 · br43:427-429. `git grep -n -E "import policy\|[^.]\bresolve\(" -- tools/roles/` prints only `roles_lib.py:110` (a comment) |
| 100 | fo29 | A2 | S16: None from any cause, with a note naming a missing kit | cite | AGREES | fo29:118-119 · br21:48 |
| 101 | fo29 | A2 | S8: the fixture commits the policy file so the read sees the landed revision | cite | AGREES | fo29:89-91 · br21:44 (`get` reads the landed revision; only the word `resolve` is stale) |
| 102 | fo29 | A2 | S12: template fields stay br5 S1's | cite | AGREES | fo29:102-105 · br5:37-49 |
| 103 | fo29 | A2 | S25: `check_roles` can read `instructions.exclude` (br20 S7) | cite | UNKNOWN UNTIL BUILT | fo29:148-150 · br20:58-64, :96-100 |
| 104 | fo29 | A2 | AC8: a stub `loop_lib.py` gains one call per `--item` render | cite | MISMATCH | fo29:96-98, :310-311 · br3:39-42 |
| 105 | fo29 | A2 | S6 and S11: `load_kit_module` loads runlog's `extract.py` and the playbook kit's `gov_tag.py` in process through `importlib` | R3 | MISMATCH | fo29:81-86, :99-101 · oc7:202-205. `tools/roles/kit.toml:19` has a `requires_if` only for review-harness, and S20 adds one only for hooks (fo29:132-133) |
| 106 | fo29 | A2 | S20: `answered-calls.js` reaches `scratch-guard.js` under a declared `requires_if` row | R3 | AGREES | fo29:130-133 |
| 107 | fo29 | A2 | S19 re-guards the `answered-calls self-test` row by editing `tools/gate-legs.json` | R1 | MISMATCH | fo29:127-129, :248, :335 · wb11:36-47 · fo6:82-85 (the leg is an `[[exempt_leg]]` row) |
| 108 | fo32 | A2 | br1 S3's merged `gov-reviewer` replaces the two reviewers | cite | AGREES | fo32:83-85 · br1:68-70 |
| 109 | fo32 | A2 | `gov-reviewer`'s `reads` holds `input:spec` and `input:diff` | cite | UNKNOWN UNTIL BUILT | fo32:83 · br1:63-66 (no `reads` line stated) |
| 110 | fo33 | B | The posture read finds the loop kit with `resolve_kit_dir("loop", "breakpoints.py", KIT_DIR)` and runs it as a subprocess | R3 | AGREES | fo33:44-45; fo34:42, :69-71; oc7:202-205 |
| 111 | fo34 | B | The policy key is read through `read_policy_setting`, which runs `policy.py get` as a subprocess and raises on exit 2; `breakpoints.py list` is a bounded subprocess | R3 | AGREES | fo34:36-41, :69-71; br21:41-44, :47-48; br43:105-109 |
| 112 | fo37 | A2 | S11 and S33: `validate_return` and the refusal arm's checks are br5 S1's and br26 S2's, DEFERRED | cite | AGREES | fo37:113-115, :205-208 · br5:37 |
| 113 | fo37 | A2 | S2: the sibling-import check greps only bare `import`/`from` statements | R3 | MISMATCH | fo37:73-76 · oc7:202-205 |
| 114 | fo37 | A2 | S24 adds a guard to the `answered-calls self-test` row of `tools/gate-legs.json` | R1 | MISMATCH | fo37:172-176, :331, :446-448 · wb11:36-47 |
| 115 | fo39 | B | The bounded runner is an inline copy of one canonical `tools/lib/` block; no sibling kit's `regen.py` is imported | R3 | AGREES | fo39:31-41, :145-146; oc7:202-205 |
| 116 | fo41 | A2 | The govkit step uses govkit's own functions, no sibling kit | R3 | AGREES | fo41:94-100 |
| 117 | fo42 | A2 | S8: `validate_return` and the arm checks are br5 S1's and br26 S2's | cite | AGREES | fo42:84-89 · br5:37 |
| 118 | fo42 | A2 | S12: the template line is composed by br43 S13 | cite | AGREES | fo42:104-109 · br43:86-89 |
| 119 | fo42 | A2 | S10: `gov-skeptic` exists before and after the merge | cite | AGREES | fo42:93-96 · br1:141, :158-159 |
| 120 | fo42 | A2 | S7: `read_cap_answer` loads the policy kit's `budgets.py` in process and keeps a `sys.path` insert of the policy kit's directory | R3 | MISMATCH | fo42:77-83 · br43:105-110 · oc7:202-205 · `tools/roles/roles_lib.py:148-151` |
| 121 | fo45 | A2 | The step carries the `git_env_leaks_py` block inline | R3 | AGREES | fo45:62-66 |
| 122 | fo46 | A2 | S8 adds guard files to the `govkit selftest` row of `tools/gate-legs.json` | R1 | MISMATCH | fo46:89-96 · wb11:36-47 · `tools/govkit/registry.toml:439-440` |
| 123 | fo46 | A2 | S5: the roles adopter suite calls the lexicon kit's `check_self_containment` | R3 | MISMATCH | fo46:74-79 · oc7:202-205 · `tools/roles/kit.toml:19`, :46-48 · `tools/lexicon/lexicon.py:2359` (no CLI takes a kit dir) |
| 124 | fo48 | B | The `govkit selftest` guard is widened by editing that leg's row in `tools/gate-legs.json` by hand (S14, S17, S18) | R1 | MISMATCH | fo48:127-130, :141-147, :299; wb11:36-38, :43-45, :154 |
| 125 | fo48 | B | The step `retired_dispatch_args.py` imports govkit itself (`derive_tool_root`, `git()`), and reaches no sibling kit in process | R3 | AGREES | fo48:92-93, :242; tr20:38-39 ("a step program reaches it by importing `govkit`") |
| 126 | fo50 | B | The narrowed home rows are written straight into the `govkit selftest` row of `tools/gate-legs.json` | R1 | MISMATCH | fo50:51-52, :175, :184; wb11:36-38, :43-45, :154 |
| 127 | fo58 | B | The `govkit selftest` row in `tools/gate-legs.json` gains `{prefix}/check-spec-tokens.py`, landing in one commit with its reach | R1 | MISMATCH | fo58:136-140, :179-182, :271, :377-379; wb11:43-45, :154 |

## The mismatches, both sides quoted

Each reader wrote the bullets for its own specs, with both sides quoted, the `Change:` and the
`Cause:`. They are kept once, in section 2 of each group's return in
[`2026-10-28-build-TOOL-dFurnishedOrders-1-crosscheck-returns`](2026-10-28-build-TOOL-dFurnishedOrders-1-crosscheck-returns.md):
Group A1 (fo2, fo3, fo5, fo6, fo7, fo8, fo10, fo11, fo12, fo14, fo15, fo16), Group A2 (fo17, fo18,
fo20, fo29, fo37, fo42, fo46) and Group B (fo48, fo50, fo58).

## UNKNOWN UNTIL BUILT

- **Rows 49, 75 and 85, with fo4 S4 and fo9 S4:** an item's `map`, a work order cut with `--item`, and
  the `--item` renders of fo18 AC3 and fo20 AC4 and AC6 need `loop_lib.py declaration --item <tag>
  --json`, which br3 F5 leaves open for the owner and dDeclaredLoop must build.
- **Rows 69 and 70 (fo17):** whether `code_record.py` exits 2 on an unknown verb is tr8's CLI as built;
  what the slot renders over a `degraded` record is decided by whoever builds the reader under ask
  TOOL-dTotalRecall-103.
- **Row 103 (fo29 S25):** how `check_roles` sees `instructions.exclude` is decided by br20's build of the
  playbook kit's `compose` verb (br20 F6).
- **Row 109 (fo32):** `gov-reviewer`'s `reads` line is decided when br1 writes the agent file.
- **fo2 S2, no table row:** what `read_agent_limit` returns with no policy kit is settled when br22 is
  built (br22:56-57).

## Rule-wide hits the rules do not bind

Of the 21 candidates, 12 are not bound, each with its reason in section 4 of Group B's return: fo23,
fo30, fo31, fo49, fo52, fo53, fo54, fo55, fo56, fo59, fo60 and fo61. Row 93 (fo25) is AGREES only as
fo37 S34 amends it: fo25 S4 still loads `tree_lib` in process, and if fo37 is dropped or reordered,
fo25 breaks tr20:38-42, a rule dTotalRecall's re-ground wrote.

## For the re-ground

Every spec below is revised by one writer of the re-ground brief, for the rows named. The other
mismatch-free specs stay as they are.

By spec: fo2: row 6; fo3: rows 11 and 12; fo5: row 19; fo6: rows 26 and 27; fo7: rows 32 and 33; fo8:
row 35; fo10: row 43; fo11: rows 46 and 47; fo12: rows 50 and 51; fo14: row 55; fo15: row 60; fo16:
row 63; fo17: rows 68, 71, 72 and 73; fo18: row 77; fo20: rows 86 and 88; fo29: rows 98, 99, 104, 105
and 107; fo37: rows 113 and 114; fo42: row 120; fo46: rows 122 and 123; fo48: row 124; fo50: row 126;
fo58: row 127.

- **Group A, catalogue defaults, led by spec 2:** specs 2, 5, 8, 16 and 18.
- **Group B, policy reads and the loop render, led by spec 17:** specs 7, 11, 12, 17 and 20.
- **Group C, the roles kit's cross-kit loads and the `answered-calls` leg, led by spec 29:** specs 3,
  6, 10, 14, 29, 37 and 42.
- **Group D, the `govkit selftest` leg and the tester template, led by spec 46:** specs 15, 46, 48, 50
  and 58.

## After the re-ground

The four writers' returns are
[`2026-10-28-build-TOOL-dFurnishedOrders-1-reground-returns`](2026-10-28-build-TOOL-dFurnishedOrders-1-reground-returns.md).
No writer refused a row; each re-read both sides and found the parent line the record cites. Every
revised spec stays `DEFERRED`, each with one spec-revised deviation record. What they found beyond the
rows:

- **Edits beyond the listed rows, kept consistent:** fo16 AC1 gains a policy-kit-removed case for the
  branch S1 moved; fo18 S2 follows fo8's revised read; fo29 S16 and AC12 follow fo2's revised S5 (no
  policy kit gives `per-task` and the note, an unset key `per-batch`); fo10 S4 follows fo3's new S4;
  fo17's non-goal names ask TOOL-dTotalRecall-103 as the Edges bullet does; fo11's mirror bullet reads
  fo29's "ledger read", after Group B's writer was resumed for it.
- **New verbs this build mints for itself,** with no ask: `runlog.py notices --transcript <path>
  --json` (fo3 S4) and `runlog.py orientation --transcript <path> --json` (fo10 S2), as fo16 S2 already
  mints `runlog.py turns`; fo42 S7 reads the cap through the existing `budgets.py resolve --explain`.
- **The no-policy-kit fallbacks are the writers' reading.** Where a spec keeps a typed value only for
  the no-kit None (fo5, fo7, fo8, fo11, fo12, fo17, fo18), the writers took the brief's rule and fo29
  S9; fo8 keeps rendering `handed` with no policy kit because its AC9 already does. The owner may want
  one rule for that case.
- **fo6's leg `enforces` is `["principle.p29"]`,** from v2's P29 row naming cl-dClosedLoop-0197, which
  fo6 carries. `tools/run-gates/leg_factory.py` is not in the tree, so fo6 S9, fo29 S19, fo37 S24 and
  fo46, fo48, fo50 and fo58 each record a hand edit standing in for it until wb11's migration lands.
- **fo37 S2's widened predicate prints nothing over the real tree,** with `budgets` left off its list
  until fo42 removes `roles_lib.py:150`'s import at order 25.
- **Parent text that looks wrong (not edited):** br43 S19 and AC19 accept a `readPolicy` import line
  in `scratch-guard.js`, against ks8 S5's "a hook never `require`s the policy kit's module"; ks8 S5
  leaves `agent-cap.js:469`'s in-process `require` of `policy-mirror.js` in place; wb11 S1 says each
  `[[exempt_leg]]` row carries the whole leg row, but `govkit selftest`'s holds only `name` and `why`
  and carries no `enforces`; wb13 S10 puts `legacy_ledger.py`'s verbs on the canonical file only, so an
  adopter's copy may not run as a command; tr8:117 and :136 still give the `code` slot to dBoundRoles
  (ask TOOL-dTotalRecall-102 open).

**Forks left open for the owner** (each names the ask the build run would file):

- fo7 F9: `backlog.py render --json` from the build owning `tools/memory-tree/backlog.py` at the pass,
  dTotalRecall today (recommended), over a `requires_if` row or `gov_record.py new ask`.
- fo11 F5: `legacy_ledger.py registrations --json` and S10's command-line verbs on the memory-tree copy,
  asked of TOOL-dWitnessedBar-13 (recommended), over a `requires_if` row or a second reader.
- fo14 F8: `gen_build_index.py --asks --json` rows gain the `data` clause (recommended).
- fo29 F6: PLAY-dOrderedCharter-19's `gov_tag.py` gains `namespaces --json` (recommended).
- fo46 F7: a lexicon `--self-containment <kit-dir>` mode from the build owning `tools/lexicon/` at the
  pass (recommended), over a `requires_if` row or unit 42's copy of the walk.

Re-resolved by the writers, `RESOLVED (agent, 2026-10-28, delegated)` on rung 1: fo3 F3 and fo10 F3
(runlog verbs by subprocess, oc7 §4) and fo42 F2 (`budgets.py resolve` by subprocess, br43 S21). fo12
F1's probe was re-pinned to a content-anchored grep and still reads 12 and 1, so its resolved mark
stays.
