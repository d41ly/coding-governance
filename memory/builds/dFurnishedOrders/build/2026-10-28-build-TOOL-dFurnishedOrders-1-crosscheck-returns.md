**Serves:** research TOOL-dFurnishedOrders-1

# dFurnishedOrders — the cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record
[`2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck`](2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck.md)
is assembled from, each copied from its agent transcript; only the headings are the main loop's. Group A1, citation read specs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15 and 16; Group A2, citation read specs 17, 18, 19, 20, 22, 24, 27, 28, 29, 32, 37, 41, 42, 45 and 46; Group B, rule-wide read specs 13, 23, 25, 26, 30, 31, 33, 34, 39, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60 and 61.

## Group A1, citation

I checked Group A1 (specs 1–12, 14, 15, 16) against origin/main at `1a61f21a2`. Result: 63 assumptions, 39 AGREES, 21 MISMATCH and 3 UNKNOWN UNTIL BUILT. 6 of the mismatches come from the re-grounds; the other 15 already read the same way at `1a3ce03dd`, and every one of those breaks rule R1 or R3.

#### 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | The scout's placement return and the driver's record of it belong to br12, and the scout still returns the card | cite | AGREES | fo1:105, :89; br12:37-41 ("beside the card body the role already returns"), :43-49 |
| 1 | The card's recall check runs `map_diff.py` as a subprocess found by `resolve_kit_file` | R3 | AGREES | fo1:67-75 |
| 1 | `render_handoff` runs the codebase-map verb, found by `resolve_kit_dir` (fo29 S23) | R3 | AGREES | fo1:81-83; fo29:138 |
| 2 | The `return` grammar has a `list` type that can carry `tasks` | cite | AGREES | fo2:49-53, :250; br2 "The return template" (`type := … "list"`) |
| 2 | `validate_return` checks the shape, and the batch join is added on top | cite | AGREES | fo2:82-83; br5:35-48 |
| 2 | `read_policy_setting("prompts.batch", root)`: None means the catalogue default `per-batch`; no policy kit means `per-task` | cite | MISMATCH | fo2:63-67; br21:41-50; br43:105-110 |
| 2 | `read_agent_limit(root)` bounds the batch | cite | AGREES | fo2:46-47; br22:53-57 |
| 2 | Stage rows (`fan`) exist only on `workflow`-driver entries | cite | AGREES | fo2:78, :157-159; br22:34-37 |
| 2 | The matrix is read through `loop_items.py matrix` as a subprocess | R3 | AGREES | fo2:43-45 |
| 3 | br5 S3's return-check record is not where notices persist | cite | AGREES | fo3:80-81; br5:56-63 |
| 3 | runlog's `extract.py` reads `notices.record` through an in-process `resolve` | R3 | MISMATCH | fo3:42-46; oc7:202-205, :379-380 |
| 3 | `handoff.py` loads runlog's `extract.py` by file | R3 | MISMATCH | fo3:54-56, :163-164, :241; oc7:202-205 |
| 4 | Work orders are br3's and gain a block | cite | AGREES | fo4:131; br3:S2 |
| 4 | `### bug-classes` sits in br23's `boundaries` slot | cite | AGREES | fo4:55, :341-344; br23:43-44, :123 |
| 4 | br23's rule for an empty slot never applies to a slot block | cite | AGREES | fo4:40-41; br23:131 |
| 4 | The lookup runs `gotchas.py --for-names` as a subprocess via `resolve_kit_dir` | R3 | AGREES | fo4:57-59 |
| 5 | `role-schema.toml` `[[field]]` rows, `shape = "list"`, `required = "every"` | cite | AGREES | fo5:33-35; br2 "The schema" table |
| 5 | `## Trust` is appended after br2 S6's `## Return` | cite | AGREES | fo5:41-44; br2 S6 |
| 5 | `read_policy_setting`: None (default or no kit) renders `keyed`/`cold` typed in the roles kit | cite | MISMATCH | fo5:45-48; br21:41-50; br43:105-110 |
| 5 | The roster includes br1's new roles, among them `gov-reviewer` and `gov-tester` | cite | AGREES | fo5:93-100, :106-107; br1:131-143 |
| 5 | The tester's packet is its br3 work order | cite | AGREES | fo5:76-77; br3 S2 |
| 5 | br20's composition requires every structured field on a repository role | cite | AGREES | fo5:176-178; br20 S3 ("carries every structured field gov's carry") |
| 5 | The verifier context is read by `policy.py get … --rev HEAD` at render time | R6 | AGREES | fo5:56-58 |
| 6 | The fragment layout follows br25 S2 | cite | AGREES | fo6:80-81; br25:50-53 |
| 6 | Wiring follows br5 S5 (`--scaffold` merge, roles arm of `check-wiring.sh`) | cite | AGREES | fo6:81-82; br5 S5 |
| 6 | New leg `answered-calls self-test` hand-written into `tools/gate-legs.json` with no `enforces` | R1 | MISMATCH | fo6:82-86, :203; wb11:36-50; oc7:58-63 |
| 6 | `answered-calls.js` `require`s the policy kit's `readPolicy` | R3 | MISMATCH | fo6:57-58, :124, :345; ks8:62-66 |
| 6 | `answered-calls.js` requires `scratch-guard.js` exports (the helper home br25 S4 gives) | R3 | AGREES | fo6:21-22, :26-30; br25:58-63; fo29:131-133 (S20 `requires_if`) |
| 7 | `role-schema.toml` gains `[return.repair]` | cite | AGREES | fo7:30-36; br2 S1 |
| 7 | `validate_return` refuses a malformed `contradicted` return | cite | AGREES | fo7:36-38; br5:35-48 |
| 7 | br11's reader answers kind `refusal` (added by br26) | cite | AGREES | fo7:131-133; br11:60-70; br26:55 |
| 7 | `roles.on-contradiction` is read through an in-process `resolve` | R3 | MISMATCH | fo7:53-54; oc7:379-380; br43:105-110 |
| 7 | `handoff.py` calls memory-tree's `render_ask_row`/`render_sev_row`/`render_status_row` in process | R3 | MISMATCH | fo7:60-63; oc7:202-205 |
| 8 | `slices` field row: `shape = "list"`, `required = "optional"` | cite | AGREES | fo8:32-34; br2 "The schema" table |
| 8 | `instructions.slices`: None renders the catalogue default `handed` | cite | MISMATCH | fo8:50-52; br21:41-50; br43:105-110 |
| 8 | Thirteen role files once br1 adds its roles and the reviewers merge | cite | AGREES | fo8:132-135; br1:129-147 (gov's own merge is br1 S3, not br18, but the count holds) |
| 8 | Slices are resolved through `gov_tag.py where` as a subprocess | R3 | AGREES | fo8:39-41 |
| 9 | The role index carries `layer` and `acts-as` (br1 S6) | cite | AGREES | fo9:35-36; br1 S6 |
| 9 | Arm 3 (br1 S7) grades the composed loop, repository rows included | cite | AGREES | fo9:62-63, :94-96; br1 S7 (rev-3) |
| 9 | Other kits reach the `matrix` verb by subprocess, as br3 S1 reaches the loop kit | cite | AGREES | fo9:57-58; br3 S1 |
| 9 | br20 S7 reads arm 2 over the composition | cite | AGREES | fo9:73-74; br20 S7 |
| 10 | Retries are br5's, and are not counted here | cite | AGREES | fo10:83-84; br5 S3 |
| 10 | The roles kit loads runlog's `extract.py` by file; `derive_role_matrix` is looked up from the roles kit | R3 | MISMATCH | fo10:54-58, :67-70, :266-275; oc7:202-205 |
| 11 | `record_find.py` sits in memory-tree, found by `resolve_kit_dir` (tr9 S5) | cite | AGREES | fo11:37-39; tr9:104-107 |
| 11 | The slot body is tr9 S8's `reads:` list; the budget is `gov_record.py budget` on `memory.item-budget`/`over-budget` | cite | AGREES | fo11:39-42; tr9:108-125 |
| 11 | `retrofit.slot-bytes` and `roles.orientation.house-index` are read through an in-process `resolve` | R3 | MISMATCH | fo11:67-71; oc7:379-380 |
| 11 | memory-tree's `legacy_ledger.py` is loaded by file | R3 | MISMATCH | fo11:136, :143-144; oc7:202-205 |
| 12 | `every-role` comes from the index's `acts-as` (br1 S6) | cite | AGREES | fo12:35-36; br1 S6 |
| 12 | The item's `map` comes from the declaration br3 S1 reads at render | cite | UNKNOWN UNTIL BUILT | fo12:83; br3 S1, :266-278 (F5) |
| 12 | F1's probe `sed -n 120,134p` over br1 finds 12 `layer.roles` rows and 1 `layer.runtime` row | cite | MISMATCH | fo12:218-225; br1:131-143 |
| 12 | `memory.project-map` and `memory.map-unfold` are read through an in-process `resolve` | R3 | MISMATCH | fo12:60-63; oc7:379-380 |
| 14 | Work order input blocks are br3's | cite | AGREES | fo14:84; br3 S2 |
| 14 | A helper two kits read lives in `scratch-guard.js` exports (br25 S4) | cite | AGREES | fo14:41-48, :96; br25:58-63; fo29:131-133 |
| 14 | `roles_lib` calls memory-tree's `backlog.py` `parse_file`/`derive_statuses` in process | R3 | MISMATCH | fo14:66-69, :324-325; oc7:202-205 |
| 15 | br43 S13's refusal-arm composition in `render_role` is what the factory generalises | cite | AGREES | fo15:34-37; br43:86-89 |
| 15 | `validate_return` refuses a malformed `probe` return | cite | AGREES | fo15:50-52; br5:35-48 |
| 15 | `gov-tester` already carries `layer`/`acts-as` from br1 | cite | AGREES | fo15:86-87; br1 S2 |
| 15 | `never` entries follow br2's `<limit> — <enforcer>` grammar | cite | AGREES | fo15:141-143; br2 S2 |
| 15 | The tester's `return` is `outcome:code-miss\|spec-wrong\|designed\|judged, evidence, method?, losing?`, with `test.reason` returning `code-miss`/`spec-wrong` | cite | MISMATCH | fo15:129, :133-137; br2:324-338 |
| 16 | br11 S5's door `owner-question --kind [--attended]` and `resolve_owner_question(kind, attended, repo, rev)` | cite | AGREES | fo16:49-58; br11:60-70 |
| 16 | br11 S6's FORKED case answers resolve/park-item/park-build/stop-run | cite | AGREES | fo16:64-67, :147; br11 S6 |
| 16 | `read_policy_setting("attendance", root)`: None reads `unattended` | cite | MISMATCH | fo16:35-36; br21:41-50; br43:105-110 |
| 16 | `breakpoints.py list` and `runlog.py turns` are reached as subprocesses | R3 | AGREES | fo16:35-45 |

#### 2. Mismatches

- **fo2 S5.** fo2:65-67 says "a None answer reads the catalogue default `per-batch`. With no policy kit resolved the render reads `per-task`". The parent says None comes back both for `source` default and for "no policy kit found" (br21:44-48). It adds `with_default` for "the form a read with a catalogue default takes" (br21:45-46), and br43:105-110 says callers use "`with_default` where they read the catalogue default".
  - Change: call `read_policy_setting("prompts.batch", root, with_default=True)`. Then None means only that no policy kit was found, which gives `per-task` and the note (F3 keeps its meaning). Drop the roles-kit copy of `per-batch`. fo29 S16 ("per-batch on a None from any cause") needs to be reconciled in the same pass.
  - Cause: re-ground (`with_default` and br43 S21's clause came in at `ac8ab8d5f`). Treating no-kit and default as the same None was already in br21 at `1a3ce03dd`.
- **fo3 S2.** fo3:42-46 says "reads `notices.record` through the policy kit's `resolve` (`tools/policy/policy.py:752`)". The parent says the module "runs `<sys.executable> <kit>/policy.py get <key>`… A kit may not import a sibling kit" (oc7:202-205), "the one seam a sibling kit may reach" (oc7:379-380).
  - Change: `read_notices_value` runs `policy.py get notices.record --json` as a subprocess, found by the inline `resolve_kit_dir`. The AC fixtures stay committed.
  - Cause: pre-existing.
- **fo3 S4.** fo3:54-56 says "`print_agent_lines` … loads runlog's `extract.py` by file through `resolve_kit_dir`". The parent rule is oc7:202-205, and the brief's R3 lists in-process module use or `sys.path`. fo29 S6 keeps `importlib.util.spec_from_file_location`, which is still in-process.
  - Change: add a runlog verb, for example `runlog.py notices --transcript <path> --json`, run as a subprocess. The other route is a `requires_if` row on `tools/roles/kit.toml` naming `runlog`, which tools/roles/kit.toml:19 does not hold today. Fix fo29 S6 to match.
  - Cause: pre-existing.
- **fo6 S9 (R1).** fo6:82-86 says the new leg comes "with the rows a new leg owes (`tools/gate-legs.json`, `tools/govkit/registry.toml`'s `[[exempt_leg]]`…)", and Files touched lists `tools/gate-legs.json` (fo6:203). No `enforces` is named anywhere. The parent says "Each leg is declared exactly once … `enforces`…" and "`--write` renders `tools/gate-legs.json`" (wb11:36-45). It also says "a leg carrying no `enforces` is red" (oc7:61), and br25:65-71 does the same for its sibling leg.
  - Change: declare `answered-calls self-test` once, with `leg_factory.py new --exempt <why>` and a named `enforces`, and re-render the manifest with `--write`. Files touched lists `gate-legs.json` as rendered. Add a `leg_factory.py --check` criterion. fo29 S19's guard edit has to move into the declaration too.
  - Cause: pre-existing.
- **fo6 S5 (R3).** fo6:57-58 says "`roles.answered-calls`, read through `readPolicy` (`tools/policy/policy-mirror.js:132`)". The parent says "by running dGroundRules' JS reader's own CLI as a subprocess, `node <policy kit>/policy-mirror.js get …` … the hook never `require`s the policy kit's module" (ks8:62-66).
  - Change: spawn `node <policy kit>/policy-mirror.js get roles.answered-calls --repo <repo>` under a bounded timeout, located through the exported `resolvePolicyHelper`. A failed spawn takes S7's `hook-failed` path.
  - Cause: pre-existing (the rule is TOOL-dGroundRules-1 §4). The ks8 wording that applies it came in at `ff44fb2a2`.
- **fo7 S4.** fo7:53-54 says "`roles.on-contradiction` is read through `resolve` (`tools/policy/policy.py:752`)". The parent: oc7:379-380, and br43:105-110 ("no file under `tools/roles/` runs `get` outside it or imports the policy kit").
  - Change: read it through `read_policy_setting(..., with_default=True)`, with no in-process `resolve`. fo29 S9 already moves the call; it should add `with_default`.
  - Cause: pre-existing (the in-process import). The `with_default` form is re-ground.
- **fo7 S6.** fo7:60-63 says rows are "rendered by `render_ask_row`, `render_sev_row` and `render_status_row` (`tools/memory-tree/backlog.py:1516-1540`), reached through `resolve_kit_dir`". The parent rule is oc7:202-205, and the roles kit has no `requires_if` row for memory-tree.
  - Change: render the rows through a memory-tree verb run as a subprocess, either one `backlog.py` already exposes or an ask on memory-tree. The other route is a declared `requires_if` row.
  - Cause: pre-existing.
- **fo8 S4.** fo8:50-52 says "`None` renders the catalogue's default, `handed`". The parent: br43:105-110 ("with `with_default` where they read the catalogue default") and br21:44-46.
  - Change: call with `with_default=True`, and drop the typed default `handed`. None then means no policy kit only, with its own fallback and note.
  - Cause: re-ground.
- **fo10 S2/S7.** fo10:54-58 says calls are "reached through the by-file load of runlog's `extract.py`". F3 (fo10:266-275) argues that the no-sibling rule "is about copies". The parent says "A kit may not import a sibling kit" (oc7:202-205), and br12's re-ground moved the same kind of reach to a subprocess verb (br12 S2).
  - Change: replace F3 (a) with (b): a runlog verb that classes one transcript, run by subprocess. S7 reads the matrix through `loop_items.py matrix --json` (fo9 S4), not a function call.
  - Cause: pre-existing.
- **fo11 S7.** fo11:67-71 says both keys are read "through the policy kit's `resolve(key, repo, rev)`". The parent: oc7:379-380 and br43:105-110.
  - Change: use `read_policy_setting(key, root, with_default=True)` for `retrofit.slot-bytes` and `roles.orientation.house-index`. This is fo29 S9's move, plus `with_default`.
  - Cause: pre-existing; `with_default` is re-ground.
- **fo11 S3.** fo11:143-144 says "The ledger module is loaded by file under its own name, the reach F3 of unit 10 records for a sibling kit's module". The parent: oc7:202-205.
  - Change: read the registrations through a memory-tree verb run as a subprocess (an ask on wb13's `legacy_ledger.py`), or declare a `requires_if` row.
  - Cause: pre-existing.
- **fo12 F1.** fo12:219-224 says "Probe: `sed -n 120,134p` over … TOOL-dBoundRoles-1.md … 12 rows carry `layer.roles` … 1 carries `layer.runtime` … Liveness: the second count is 1". Today the parent's roster sits at br1:131-143. The probe now prints 4 `layer.roles` rows and 0 `layer.runtime` rows, so the liveness assertion fails.
  - Change: re-pin the probe to `sed -n 129,143p` or, better, to a content-anchored grep over the roster table. The substance is unchanged (12 + 1).
  - Cause: re-ground (the spec-records table grew at `ac8ab8d5f` and pushed the roster down 9 lines).
- **fo12 S6.** fo12:60-63 says both keys are read "through the policy kit's `resolve(key, repo, rev)`". The parent: oc7:379-380 and br43:105-110.
  - Change: use `read_policy_setting(..., with_default=True)` for `memory.project-map` and `memory.map-unfold`, as fo29 S9 does, plus `with_default`.
  - Cause: pre-existing; `with_default` is re-ground.
- **fo14 S6.** fo14:66-69 says open asks are read "through `tools/memory-tree/backlog.py`'s `parse_file` and `derive_statuses` … reached by `resolve_kit_dir`". The parent: oc7:202-205. The spec's own reuse audit (fo14:328) states that a kit may not import across kits.
  - Change: read open repair asks through a memory-tree verb run as a subprocess that prints the open asks and their `data` clauses, or declare a `requires_if` row.
  - Cause: pre-existing.
- **fo15 S3.** fo15:129 gives `return: outcome:code-miss|spec-wrong|designed|judged, evidence:text, method:text?, losing:text?`, and fo15:136 has `test.reason` return `code-miss`/`spec-wrong` "with … the Test step's answer". The parent resolved the tester's template to "`outcome:code-miss|spec-wrong|answered, evidence:text, answer:text?` … (b) refuses every `test.reason` return, which carries no judgment" (br2:328-332).
  - Change: the re-founded template keeps `answered` and `answer:text?` beside `designed` and `judged`. The body returns `answered` for `test.reason`.
  - Cause: re-ground (br2 F4 at base gave only `code-miss|spec-wrong`).
- **fo16 S1.** fo16:35-36 says "`read_policy_setting("attendance", root)` (…; None reads `unattended`)". The parent: br43:105-110, br21:44-46, and catalogue.toml:61 `default = "unattended"`.
  - Change: call with `with_default=True`, so the catalogue answers `unattended`. A None (no policy kit) goes to S1's `unread: <why>` → attended path, not to a typed `unattended`.
  - Cause: re-ground.
- **fo5 S3.** fo5:45-48 says "A `None` answer, the catalogue default or no policy kit, renders the catalogue's default, `keyed` and `cold`". The parent: br43:105-110 and br21:44-46.
  - Change: read both keys with `with_default=True`. Keep the typed `keyed`/`cold` only as the no-policy-kit fallback, with a note.
  - Cause: re-ground.

#### 3. Unknown until built

- fo12 S2: whether the item's `map`/`unfolds` can be read at render depends on br3 F5's ask that dDeclaredLoop add `loop_lib.py declaration --item <tag> --json` (br3:266-278, open for the owner). dDeclaredLoop's answer decides it.
- fo2 S2: what `read_agent_limit` returns with no policy kit. br22 S5 says only "the cap arm prints `unarmed` once" (br22:56-57), so whether a batch is bounded or refused with no kit is settled when dBoundRoles 22 is built.
- fo4 S4 and fo9 S4 rely on br3's subprocess reach to the loop kit, which waits on the same F5 verb. The reach is agreed; the verb is not. dDeclaredLoop's answer to F5 decides it.

#### 4. Rule hits the rule does not bind

- fo2 S2 `roles_lib.resolve_kit_dir("loop", …)`: the roles kit is calling its own locator, and the loop kit is reached by subprocess.
- fo12 S3 reads the playbook kit's `namespaces.toml` as TOML data, not as a module. The same holds for fo9 S2's `layers.toml`, and br1 F6 sets the precedent of reading a sibling's data. fo29 S11's change to in-process `gov_tag.read_namespaces` would be bound, but that is fo29's.
- fo1:223 and :297 and fo8:313 mention a sibling import only as a rejected option.
- fo14:328 mentions a cross-kit import only as a rejected option.
- fo3:123 ("Neither reads `.governance/policy.toml`") is a statement that agrees with I8.

#### 5. Revised units cited but not depended on

- fo1: br12 — only a non-goal boundary.
- fo2: none.
- fo3: br5 — only a non-goal boundary (S3's record).
- fo4: none.
- fo5: br3 — only a non-goal boundary (the tester's work order).
- fo6: none.
- fo7: none.
- fo8: none.
- fo9: br20 — only a non-goal boundary (S7).
- fo10: br5 — only a non-goal boundary (the retry).
- fo11: none.
- fo12: br2 — named only in F2's rejected option (b).
- fo14: br3 — only a non-goal boundary (the input blocks).
- fo15: none.
- fo16: none.

Files: the A1 specs are `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dFurnishedOrders\spec\2026-10-26-spec-TOOL-dFurnishedOrders-<n>.md`. The parents I checked are `...\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-{1,2,3,5,11,20,21,22,23,25}.md`, `...\dBoundRoles\spec\2026-10-26-spec-TOOL-dBoundRoles-43.md`, `...\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-9.md`, `...\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-8.md`, `...\dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-7.md` and `...\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-11.md`.

## Group A2, citation

Group A2 checked: 15 specs, 52 assumptions. 33 AGREES, 14 MISMATCH and 5 UNKNOWN UNTIL BUILT. Nothing was written. I ran no gate. My only commands were `git show`, `git diff`, `git grep` and `grep`/`sed` over the specs and `tools/`.

#### 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 17 | `code_record.py` lands in the memory-tree kit, found with `resolve_kit_dir("memory-tree", "code_record.py", …)` | cite | AGREES | fo17:43-45 · tr8:48-51, :204 |
| 17 | A kit sibling is a file-level relation with no range (tr8 S6 kit membership) | cite | AGREES | fo17:99-101, :229-233 · tr8:66-68 |
| 17 | The record holds what the row grammar needs: kind, qualified name, `line`, `end_line`, call edges and test edges | cite | AGREES | fo17:90-96 · tr8:50-51, :66-67, :69-71, :155-158 |
| 17 | tr8 "lands a `neighbourhood` reader printing §4's rows" (the hands-off edge) | cite | MISMATCH | fo17:83, :43-44 · tr8:117, :136. `grep -c neighbourhood` over tr8 prints 0. `memory/builds/dTotalRecall/BACKLOG.md:15-16` (asks TOOL-dTotalRecall-102 and -103) are still open |
| 17 | `code_record.py` answers the unknown verb `neighbourhood` with exit 2 | cite | UNKNOWN UNTIL BUILT | fo17:46-47 · tr8:43-47, :74-75, :255-310 (flags only: `--time`, `--check`, `--dump`, `--fixture`, `--ceiling`) |
| 17 | A `degraded` record is the reader's problem, not the slot's | cite | UNKNOWN UNTIL BUILT | fo17:70 · tr8:79-80, :175 |
| 17 | A `--item` render with a stub `loop_lib.py` that prints only the seed's `unarmed` line reaches the `code` block (AC2) | cite (br3 S1 reads br17's `--item`) | MISMATCH | fo17:184-187 · br3:39-47, :266-280 |
| 17 | A missing loop kit renders `not-installed` | cite | MISMATCH | fo17:40-41 · br3:46-47 |
| 17 | `memory.code-budget` and `memory.code-roles` are read through "J1's policy read" (J1 allows an in-process `resolve`), and the AC1 fixture is justified by `resolve` | R3 | MISMATCH | fo17:50-51, :183 · brief J1 (`prompts/…-spec-brief.md:175`) · br21:41-48 · br43:105-110 · oc7:202-205 |
| 17 | Seed and record reader are both reached by subprocess | R3 | AGREES | fo17:38-40, :43-45 · oc7:202-205 |
| 18 | A work order cut with `--item` exists, and AC3 renders one in a scratch adopter | cite | UNKNOWN UNTIL BUILT | fo18:41-42, :210-215 · br3:41, :266-280 |
| 18 | `read_policy_setting(key, root)` runs `get` and returns None on a default | cite | AGREES | fo18:47-48 · br21:41-48 |
| 18 | `annotations.delivery`: on None the code substitutes the literal `work-order` | cite | MISMATCH | fo18:69-71 · br21:46-47 · br43:105-109 |
| 18 | `### instructions` sits in br23's `boundaries` slot beside the charter rule blocks | cite | AGREES | fo18:132-133 · br23:42-43, :123 |
| 18 | `load_sets.py derive` and `gov_tag.py bundle` are reached by subprocess | R3 | AGREES | fo18:42-43, :61-62 · oc7:202-205 |
| 19 | `validate_return(role, text, root, work_order)` and its template read | cite | AGREES | fo19:44-47, :58-63 · br5:37-49 |
| 19 | `check-return` blocks and re-asks while attempts are fewer than `roles.retries` | cite | AGREES | fo19:66-68, :251-255 · br5:55-69 |
| 19 | br5 S6's `spawnWithRetries` re-runs a null return | cite | AGREES | fo19:78-79 · br5:76-82 |
| 19 | br5 leaves the per-order schema out | cite | AGREES | fo19:32-33 · br5:100-101 |
| 19 | Template types are `text`, `path`, `sha`, `list`, `int` and a closed set | cite | AGREES | fo19:117-124 · br2:115, :162 |
| 20 | A `--item` render reaches `### problems` (AC4, AC6) | cite | UNKNOWN UNTIL BUILT | fo20:57-58, :238-252 · br3:41, :266-280 |
| 20 | "no loop kit" renders `not-installed` | cite | MISMATCH | fo20:63-66 · br3:46-47 |
| 20 | The block sits in br23's `material` slot after the `reads` blocks | cite | AGREES | fo20:159 · br23:122 |
| 20 | `read_claims` calls the one-namespace `read_gov_namespace` with `refs/gov/runs` only, its rows unchanged | R8 | MISMATCH | fo20:30-36, :255 · pr1:76-80 |
| 20 | Seed and driver are reached by subprocess | R3 | AGREES | fo20:57-66 · oc7:202-205 |
| 22 | br2 S1's `[[field]]` grammar (`key`, `owner`, `shape`, `required`) and the `list` shape | cite | AGREES | fo22:41-44 · br2:33-38, :115 |
| 22 | br1 S3 merges the reviewers into `gov-reviewer` | cite | AGREES | fo22:93 · br1:68-70, :158-159 |
| 24 | br5 S1 keeps the unknown-field check | cite | AGREES | fo24:97-98 · br5:43-44 |
| 27 | br11 S6 adds a FORKED case to `verb_dispatch` | cite | AGREES | fo27:28, :168 · br11:71-76 |
| 27 | The driver reaches `handoff.py owner-question` by subprocess | R3 | AGREES | fo27:37-38 · br11:66 |
| 28 | `run.on-owner-question` answers the away case | cite | AGREES | fo28:83-85 · br11:67-69 |
| 29 | S9: "a None reading the catalogue default" and "no `resolve_kit_dir("policy", "policy.py", ...)` import is left in `tools/roles/`" | cite | MISMATCH | fo29:92-95 · br21:43, :46-47 · br43:105-109 |
| 29 | AC7's predicate `import policy\|[^.]\bresolve\(` catches a second policy reader | cite | MISMATCH | fo29:306-309 · br21:41-43 · br43:427-429. `git grep -n -E "import policy\|[^.]\bresolve\(" -- tools/roles/` prints only `roles_lib.py:110` (a comment) |
| 29 | S16: None from any cause, with a note naming a missing kit | cite | AGREES | fo29:118-119 · br21:48 |
| 29 | S8: the fixture commits the policy file so the read sees the landed revision | cite | AGREES | fo29:89-91 · br21:44 (`get` reads the landed revision; only the word `resolve` is stale) |
| 29 | S12: template fields stay br5 S1's | cite | AGREES | fo29:102-105 · br5:37-49 |
| 29 | S25: `check_roles` can read `instructions.exclude` (br20 S7) | cite | UNKNOWN UNTIL BUILT | fo29:148-150 · br20:58-64, :96-100 |
| 29 | AC8: a stub `loop_lib.py` gains one call per `--item` render | cite | MISMATCH | fo29:96-98, :310-311 · br3:39-42 |
| 29 | S6 and S11: `load_kit_module` loads runlog's `extract.py` and the playbook kit's `gov_tag.py` in process through `importlib` | R3 | MISMATCH | fo29:81-86, :99-101 · oc7:202-205. `tools/roles/kit.toml:19` has a `requires_if` only for review-harness, and S20 adds one only for hooks (fo29:132-133) |
| 29 | S20: `answered-calls.js` reaches `scratch-guard.js` under a declared `requires_if` row | R3 | AGREES | fo29:130-133 |
| 29 | S19 re-guards the `answered-calls self-test` row by editing `tools/gate-legs.json` | R1 | MISMATCH | fo29:127-129, :248, :335 · wb11:36-47 · fo6:82-85 (the leg is an `[[exempt_leg]]` row) |
| 32 | br1 S3's merged `gov-reviewer` replaces the two reviewers | cite | AGREES | fo32:83-85 · br1:68-70 |
| 32 | `gov-reviewer`'s `reads` holds `input:spec` and `input:diff` | cite | UNKNOWN UNTIL BUILT | fo32:83 · br1:63-66 (no `reads` line stated) |
| 37 | S11 and S33: `validate_return` and the refusal arm's checks are br5 S1's and br26 S2's, DEFERRED | cite | AGREES | fo37:113-115, :205-208 · br5:37 |
| 37 | S2: the sibling-import check greps only bare `import`/`from` statements | R3 | MISMATCH | fo37:73-76 · oc7:202-205 |
| 37 | S24 adds a guard to the `answered-calls self-test` row of `tools/gate-legs.json` | R1 | MISMATCH | fo37:172-176, :331, :446-448 · wb11:36-47 |
| 41 | The govkit step uses govkit's own functions, no sibling kit | R3 | AGREES | fo41:94-100 |
| 42 | S8: `validate_return` and the arm checks are br5 S1's and br26 S2's | cite | AGREES | fo42:84-89 · br5:37 |
| 42 | S12: the template line is composed by br43 S13 | cite | AGREES | fo42:104-109 · br43:86-89 |
| 42 | S10: `gov-skeptic` exists before and after the merge | cite | AGREES | fo42:93-96 · br1:141, :158-159 |
| 42 | S7: `read_cap_answer` loads the policy kit's `budgets.py` in process and keeps a `sys.path` insert of the policy kit's directory | R3 | MISMATCH | fo42:77-83 · br43:105-110 · oc7:202-205 · `tools/roles/roles_lib.py:148-151` |
| 45 | The step carries the `git_env_leaks_py` block inline | R3 | AGREES | fo45:62-66 |
| 46 | S8 adds guard files to the `govkit selftest` row of `tools/gate-legs.json` | R1 | MISMATCH | fo46:89-96 · wb11:36-47 · `tools/govkit/registry.toml:439-440` |
| 46 | S5: the roles adopter suite calls the lexicon kit's `check_self_containment` | R3 | MISMATCH | fo46:74-79 · oc7:202-205 · `tools/roles/kit.toml:19`, :46-48 · `tools/lexicon/lexicon.py:2359` (no CLI takes a kit dir) |

#### 2. Mismatches

- **fo17, the `neighbourhood` reader.**
  - fo17:83: "TOOL-dTotalRecall-8's `code` record lands a `neighbourhood` reader printing §4's rows".
  - tr8:117 has "The `code` slot in each item's work order and `memory.code-budget`: dBoundRoles'", and tr8:136 has "dBoundRoles' `code` slot reads it". tr8 has no `neighbourhood` verb.
  - **Change:** have the Edges bullet name the open asks TOOL-dTotalRecall-103 (the reader) and -102 (the delivery) as what would make tr8 land the reader. As written, the bullet says tr8 already lands it. AC3 already covers the reader never landing.
  - **Cause:** pre-existing.
- **fo17, the AC2 stub.**
  - fo17:184-186: "a stub `loop_lib.py` prints `unarmed — write-set: no spec`".
  - br3:41: "`loop_lib.py declaration --item <tag> --json` in a subprocess". br3:46-47: a tag the loop does not declare "refuses with exit 1 and writes nothing".
  - **Change:** the stub must answer `declaration --item item.build.unit-pass --json` with a declaration whose actor is `role:gov-builder`, and give the seed's `unarmed` line only to `seed`. Otherwise the render exits 1 before `### code` is built.
  - **Cause:** re-ground (`ac8ab8d5f` named the verb).
- **fo17 and fo20, the "no loop kit" state.**
  - fo17:40-41: "a missing loop kit … renders `not-installed`". fo20:64: "no loop kit … renders `not-installed: <why>`".
  - br3:46-47: "or no loop kit found refuses with exit 1 and writes nothing".
  - **Change:** drop the no-loop-kit branch from the `--item` path, or state that br3 S1 refuses the render first. In both specs it is dead code.
  - **Cause:** pre-existing.
- **fo17, the policy read.**
  - fo17:51: "through J1's policy read". fo17:183: "since `resolve` reads the landed revision". J1 allows "`resolve(key, repo, rev)` (`policy.py`)".
  - br43:105-109: "`read_policy_setting` (unit 21 S1) is the one runner of `policy.py get` … no file under `tools/roles/` runs `get` outside it or imports the policy kit". br21:46-47: `with_default` is "the form a read with a catalogue default takes".
  - **Change:** read both keys with `read_policy_setting(..., with_default=True)` and reword the AC1 fixture line from `resolve` to `get`.
  - **Cause:** re-ground (br21 rev-3 and br43 rev-5).
- **fo18, the `annotations.delivery` default.**
  - fo18:70-71: "default `work-order`, as the default when the setting reads None".
  - br21:46-47 (`with_default`, quoted above). br43:107-109: "with `with_default` where they read the catalogue default".
  - **Change:** call `read_policy_setting("annotations.delivery", root, with_default=True)`. Keep the literal only for the no-policy-kit None.
  - **Cause:** re-ground.
- **fo20, `read_claims`.**
  - fo20:35-36: "`read_claims` calls it with `refs/gov/runs` and `refs/gov/remote/runs`, its rows … unchanged".
  - pr1:77-78: "`read_claims` fetches `refs/gov/leases/*` and the legacy `refs/gov/runs/*` in one bounded fetch".
  - **Change:** `read_gov_namespace` takes a list of namespaces fetched in one bounded fetch, and `read_claims` passes both `refs/gov/leases` and `refs/gov/runs`. F4's hedge does not cover this: pr1 lands no namespace reader. It widens `read_claims`' own fetch.
  - **Cause:** pre-existing.
- **fo29 S9, catalogue defaults.**
  - fo29:94-95: "a None reading the catalogue default; no `resolve_kit_dir("policy", "policy.py", ...)` import is left".
  - br21:43: "the policy kit found through `resolve_kit_dir("policy", "policy.py", here)`". br21:46-47: `with_default`.
  - **Change:** the five keys read with `with_default=True`. Restate the end state as "no `get` run or policy import outside `read_policy_setting`", because br21's own locator call stays.
  - **Cause:** re-ground.
- **fo29 AC7, the reader predicate.**
  - fo29:306: `git grep -n -E "import policy|[^.]\bresolve\(" -- tools/roles/`.
  - br43:427: `git grep -n -E "policy\.py.*get|from policy import|import policy" -- 'tools/roles/*.py'`.
  - Under br21's subprocess reader, fo29's grep matches nothing. A second `policy.py get` reader passes, so AC7 cannot fail.
  - **Change:** use br43 AC21's predicate.
  - **Cause:** re-ground.
- **fo29 AC8, the call count.**
  - fo29:310-311: "stub `loop_lib.py` appends one line per call … the counter gains one line per render".
  - br3:41: every `--item` render also runs `loop_lib.py declaration`.
  - **Change:** have the stub log its verb and count only `seed` lines, or expect two lines per render.
  - **Cause:** pre-existing (base br3:36-38 already ran the declaration as a `loop_lib.py` subprocess).
- **fo29 S6 and S11, in-process loads.**
  - fo29:82-85: "loads it with `importlib.util.spec_from_file_location` … Unit 3 S4 and unit 10 S2 load runlog's `extract.py`". fo29:100: "`gov_tag.py` … loaded by S6 as `gov_tag_reader`".
  - oc7:202: "A kit may not import a sibling kit".
  - **Change:** reach runlog's `derive_notices` and the playbook kit's `read_namespaces` through verbs run by subprocess, or declare `requires_if` rows for `runlog` and `playbook` on `tools/roles/kit.toml` with their why.
  - **Cause:** pre-existing.
- **fo29 S19 and fo37 S24, the `answered-calls self-test` guard.**
  - fo29:127: "The `answered-calls self-test` row of `tools/gate-legs.json` carries the guard". fo37:172-173: the same row "gains `{prefix}/hooks/agent-cap.js`".
  - wb11:36-38: "Each leg is declared exactly once: a `[[gate_leg]]` row … else an `[[exempt_leg]]` row in `tools/govkit/registry.toml`". wb11:43-44: "`--write` renders `tools/gate-legs.json`".
  - **Change:** put the guard on the leg's declaration (fo6 S9's `[[exempt_leg]]` row), render with `leg_factory.py --write`, and point both ACs at `leg_factory.py --list` or the rendered row. A hand edit fails `--check`.
  - **Cause:** pre-existing.
- **fo37 S2, the import grep.**
  - fo37:74-75: the grep is ``"^\s*(import|from) (extract|gov_tag|loop_lib|runlog_lib)\b"``, "which prints nothing once unit 29 S6 is built".
  - oc7:202: "A kit may not import a sibling kit".
  - The grep blesses fo29's `importlib` loads of the same modules.
  - **Change:** the check must also flag `load_kit_module`/`spec_from_file_location` loads of another kit's file not admitted by a `requires_if` row.
  - **Cause:** pre-existing.
- **fo42 S7, `read_cap_answer`.**
  - fo42:78-81: "loads the policy kit's `budgets.py` through `load_kit_module("policy", "budgets.py", "gov_policy_budgets")` … and keeps its `sys.path` insert of the policy kit's directory".
  - br43:108-109: "no file under `tools/roles/` runs `get` outside it or imports the policy kit".
  - **Change:** read the cap through a policy-kit verb by subprocess (the census verb `budgets.py` serves, or an ask for one), and drop the `sys.path` insert.
  - **Cause:** re-ground (base br43:105 said only "or imports `resolve` outside it").
- **fo46 S8, the `govkit selftest` guard.**
  - fo46:89-90: "The `govkit selftest` row of `tools/gate-legs.json` gains, as exact files: …".
  - wb11:36-44 (one declaration, rendered by `--write`). The leg is `tools/govkit/registry.toml:439-440` `[[exempt_leg]]`.
  - **Change:** add the guard to that `[[exempt_leg]]` row and render with `leg_factory.py --write`.
  - **Cause:** pre-existing.
- **fo46 S5, the lexicon call.**
  - fo46:76-78: "the unit 42 arm in the roles adopter suite calls it from gov's lexicon kit, which that suite can reach because the roles kit marks it `project-owned`".
  - oc7:202 (no sibling import). `project-owned` (`tools/roles/kit.toml:46-48`) withholds the file from adopters. It is not a `requires_if` row.
  - **Change:** run the check through a lexicon verb by subprocess (an ask: `lexicon.py` exposes no CLI for `check_self_containment(kit_dir)`), or declare the edge.
  - **Cause:** pre-existing.

#### 3. Unknown until built

- **fo17 exit 2:** whether `code_record.py` exits 2 on an unknown verb is decided by tr8's CLI as built. Today it has flags only and no stated parser.
- **fo17 `degraded`:** what the slot renders over a `degraded` record is decided by whoever builds the neighbourhood reader under ask TOOL-dTotalRecall-103.
- **fo18 AC3 and fo20 AC4/AC6:** these renders need `loop_lib.py declaration --item --json`. br3 §8 F5 leaves that verb open for the owner, and dDeclaredLoop must build it.
- **fo29 S25:** how `check_roles` sees `instructions.exclude` is decided by br20's build of the playbook kit's `compose` verb (br20 §8 F6). It is not stated whether that verb exposes exclusions.
- **fo32:** `gov-reviewer`'s `reads` line is decided when br1 writes `gov-reviewer.agent.md`.

#### 4. Rule-wide hits the rule does not bind

- **fo37 S3** (fo37:77-80): the 13 `sys.path.insert` lines of `str(KIT_DIR)` or `sys.argv[1]` load the roles kit's own modules, so R3 does not bind them.
- **fo42 S3** (fo42:63-67) and **fo45 §4** (fo45:104): each names `tools/gate-legs.json` only as a path another unit edits. Neither edits it, so R1 does not bind.
- **fo46 S13** (fo46:114-122): `census.py` carries the `run_bounded_py` block inline, a copy and not a sibling import, so R3 does not bind.

#### 5. Cited revised units that no assumption depends on

- fo17: none.
- fo18: none.
- fo19: br3 (fo19:95, a non-goal naming br3's work order).
- fo20: none.
- fo22: none.
- fo24: none.
- fo27: none.
- fo28: none.
- fo29: none (br21 at fo29:405 is the reuse audit, but :94 depends on it).
- fo32: none.
- fo37: none.
- fo41: tr20 (fo41:308-309, a recall-probe result only).
- fo42: ks44 (fo42:363, a recall-probe result only).
- fo45: tr20 (fo45:248, a recall-probe result only).
- fo46: ks44 (fo46:421, a recall-probe result only).

Specs reviewed: `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dFurnishedOrders\spec\` (units 17, 18, 19, 20, 22, 24, 27, 28, 29, 32, 37, 41, 42, 45 and 46).

## Group B, rule-wide

I checked all 21 Group B specs against R1 to R8 on the hits the brief named, reading the parents as they stand on origin/main at `1a61f21a2`. Three specs are MISMATCH, all under R1, and all three were already wrong at `1a3ce03dd`. Eight hits are AGREES, none is UNKNOWN UNTIL BUILT, and the remaining 15 hits are ones the rule does not bind.

**1. Assumptions**

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 48 | The `govkit selftest` guard is widened by editing that leg's row in `tools/gate-legs.json` by hand (S14, S17, S18) | R1 | MISMATCH | fo48:127-130, :141-147, :299; wb11:36-38, :43-45, :154 |
| 50 | The narrowed home rows are written straight into the `govkit selftest` row of `tools/gate-legs.json` | R1 | MISMATCH | fo50:51-52, :175, :184; wb11:36-38, :43-45, :154 |
| 58 | The `govkit selftest` row in `tools/gate-legs.json` gains `{prefix}/check-spec-tokens.py`, landing in one commit with its reach | R1 | MISMATCH | fo58:136-140, :179-182, :271, :377-379; wb11:43-45, :154 |
| 25 | The step reads `MEMORY_ROOT` without loading memory-tree's `tree_lib.parse_conf` in process (S4's load, retired by fo37 S34) | R3 | AGREES (as amended by fo37) | fo25:47-50 loads `tree_lib` by path; fo37:208-211 replaces it with govkit's own `parse_conf_assignment`; tr20:38-42, :299-305 |
| 48 | The step `retired_dispatch_args.py` imports govkit itself (`derive_tool_root`, `git()`), and reaches no sibling kit in process | R3 | AGREES | fo48:92-93, :242; tr20:38-39 ("a step program reaches it by importing `govkit`") |
| 13 | The kickoff engine only checks that memory-tree's `gov_map.py` exists, through `resolve_kit_file`, and imports nothing; the scout runs it as a command line | R3 | AGREES | fo13:36-38, :53-55; oc7:202-205 |
| 26 | `derive_attended` reads runlog's owner turns through the `runlog.py turns` subprocess, not by importing `extract.py` | R3 | AGREES | fo26:63 ("the `turns` verb it reads"); fo16:43, :231; fo37:105 |
| 33 | The posture read finds the loop kit with `resolve_kit_dir("loop", "breakpoints.py", KIT_DIR)` and runs it as a subprocess | R3 | AGREES | fo33:44-45; fo34:42, :69-71; oc7:202-205 |
| 34 | The policy key is read through `read_policy_setting`, which runs `policy.py get` as a subprocess and raises on exit 2; `breakpoints.py list` is a bounded subprocess | R3 | AGREES | fo34:36-41, :69-71; br21:41-44, :47-48; br43:105-109 |
| 39 | The bounded runner is an inline copy of one canonical `tools/lib/` block; no sibling kit's `regen.py` is imported | R3 | AGREES | fo39:31-41, :145-146; oc7:202-205 |

**2. Mismatches**

- **fo48 (S14, S17, S18):**
  - fo48 side: fo48:127-128 "The `govkit selftest` row's guard in `tools/gate-legs.json` covers every `descriptor` key"; fo48:143 "The guard gains those directories as rows"; fo48:299 lists `tools/gate-legs.json` as a file touched.
  - Parent side: wb11:36-38 "Each leg is declared exactly once: a `[[gate_leg]]` row in its kit's descriptor … else an `[[exempt_leg]]` row in `tools/govkit/registry.toml`, which now carries the leg's whole row beside its `why`"; wb11:43-45 "`--write` renders `tools/gate-legs.json` from every declaration; `--check` exits 1 when the file differs"; wb11:154 the `fresh` arm reds a manifest that differs from the render.
  - The leg's declaration is the `[[exempt_leg]]` row at `tools/govkit/registry.toml:439` (`name = "govkit selftest"`). `tools/run-gates/leg_factory.py` does not exist yet.
  - Change: S14, S17 and S18 put the guard rows on that registry `[[exempt_leg]]` row and then run `python tools/run-gates/leg_factory.py --write`, so the manifest row is rendered, not typed. Files touched gains `tools/govkit/registry.toml`. If wb11 has not landed by the pass, the pass records that the hand edit stood in for the factory. S16's arm still reads the rendered manifest.
  - Cause: pre-existing. wb11 S1 and S2 read the same at `1a3ce03dd`, and `git log 1a3ce03dd..1a61f21a2` over wb11 and dOrderedCharter's specs prints nothing.
- **fo50 (S1):**
  - fo50 side: fo50:51-52 "The `govkit selftest` row in `tools/gate-legs.json` ends holding exactly the home rows the narrowed term requires"; fo50:175 "Its `tools/gate-legs.json` edit is a watched path"; fo50:184 lists the file as touched.
  - Parent side: wb11:36-38, :43-45 and :154, as above.
  - Change: the narrowing edits the `[[exempt_leg]]` row at `tools/govkit/registry.toml:439` and renders the manifest with `leg_factory.py --write`; Files touched gains the registry. The re-stamp still follows, because the rendered `tools/gate-legs.json` still moves.
  - Cause: pre-existing.
- **fo58 (S17, S25):**
  - fo58 side: fo58:136-137 "The `govkit selftest` row of `tools/gate-legs.json` gains the exact-file row `{prefix}/check-spec-tokens.py`"; fo58:271 lists the file as touched.
  - Parent side: wb11:43-45 and :154, as above.
  - Change: S17's row goes on the registry `[[exempt_leg]]` declaration and is rendered with `--write`. S25 and AC19's `git log -S'{prefix}/roles/' -- tools/gate-legs.json` still hold, provided the declaration and the render land in one commit with the waiver rows. S25 should say so.
  - Cause: pre-existing.

**3. UNKNOWN UNTIL BUILT:** none.

**4. Hits the rule does not bind**

- fo23 (R1): it adds no leg. `answered-calls self-test` is unit 6's leg, named in prose (fo23:149-150). The `loadRoleIndex` reach is unit 6's design, which is Group A1's to judge.
- fo30 (R1): "whatever it enforces" (fo30:168) is about schema checks, not a leg. The `[[contract.clause]]` in S10 is not a leg row, and S6 runs `gov_map.py` as a bounded subprocess.
- fo52 (R1): it reads `tools/gate-legs.json` only as scratch copies passed in (fo52:351) and adds no leg. Its "budget" is the suite budget in `selftest-budgets.txt`.
- fo53 (R1): the edit to `tools/gate-legs.json` is committed in a scratch clone fixture (fo53:142), not the real manifest.
- fo54 (R1): fixtures are parsed copies of the manifest (fo54:155).
- fo54 (R3): `tools/check-spec-tokens.py` is a gov-only `[[exempt]]` file, not a kit (`tools/govkit/registry.toml:218-224`). `tools/govkit/selftest.py` is gov-only too ("the deployer does not travel", `registry.toml:439-442`). No sibling kit is reached.
- fo55, fo56 (R1): they read parsed copies of the manifest only (fo55:136, fo56:41, :138).
- fo59 (R1): the row is planted only in the fixture's copy. fo59:66-67 explicitly leaves the real `tools/gate-legs.json` alone.
- fo60 (R1): it only reads `git show <c>:tools/gate-legs.json` per commit (fo60:119-120, :391). That read still works once the manifest is rendered.
- fo61 (R1): the manifest edit is in a scratch clone (fo61:111).
- fo61 (R3): putting `tools/govkit` on `sys.path` imports govkit's own `matrix` (fo61:400). The by-path loads of `design_lib`, the checker and `derive-ceilings.py` are probes in a scratch clone, not shipped code.
- fo31 (R3): the roles kit calls its own `roles_lib`. `check-arms.py` appears only as a ranked reuse-lookup result (fo31:191-195).
- fo58 (R3): it loads no module itself. S17 only guards the checker unit 54 loads, which is covered by the R1 row above.
- fo49, fo60 (R8): "contention" there is CPU contention in gate-run readings of the suite budget (fo49:61, :137; fo60:213). R8's budget is dDeclaredLoop's rework budget, which contention never draws on (dl30:1, :58).

**5. Revised parent units cited but not depended on:** not applicable, since Group B is rule-wide and has no citation population.

Two things to know when the builds run:
- **Built tree:** today's code is consistent with the three mismatch rows' consequence. `tools/run-gates/leg_factory.py` is absent, and `registry.toml:439` holds only `name` and `why`. So the three hand edits only break once wb11 builds, when `--check`'s `fresh` arm reds them.
- **fo25:** its own S4 text still loads `tree_lib` in process. The AGREES rests entirely on fo37 S34 retiring that load at build, so if fo37 is dropped or reordered, fo25 becomes a MISMATCH under tr20:38-42, a rule that dTotalRecall's re-ground (`794a0f5fb`) wrote.

All paths are under `C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\`:
- `memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-48.md`
- `memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-50.md`
- `memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-58.md`
- `memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-11.md`
- `tools\govkit\registry.toml`
