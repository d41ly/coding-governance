# KICK-dKeptSession-69 — the run branch reconciled with origin/main in one merge commit, one list factory kept, and the run's own reds cleared

**Status:** DEFERRED · rev-3 · 2026-11-22 · node d · Tier-2 · base e7ab8c81 · streams tooling · order 9 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-22-build-KICK-dKeptSession-69-1-acceptance-ledger.md](../build/2026-11-22-build-KICK-dKeptSession-69-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-KICK-dKeptSession-69-red-fix-10.md](../build/2026-11-22-build-KICK-dKeptSession-69-red-fix-10.md) | red-fix | — |
| [2026-11-22-build-KICK-dKeptSession-69-red-fix-9.md](../build/2026-11-22-build-KICK-dKeptSession-69-red-fix-9.md) | red-fix | — |
| [2026-11-22-build-KICK-dKeptSession-69-widen-1.md](../build/2026-11-22-build-KICK-dKeptSession-69-widen-1.md) | widen | — |
| [2026-11-22-build-KICK-dKeptSession-69-widen-2.md](../build/2026-11-22-build-KICK-dKeptSession-69-widen-2.md) | widen | — |
| [2026-11-22-prompt-KICK-dKeptSession-69-1-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-69-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-69-2-builder.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-69-2-builder.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-69-3-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-69-3-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-69-4-builder.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-69-4-builder.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-69-5-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-69-5-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-69-build-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-69-build-brief.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-69-divergence-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-69-divergence-brief.md) | research | — |
| [2026-11-22-prompt-KICK-dKeptSession-69-readers-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-69-readers-brief.md) | research | — |
| [2026-11-22-prompt-KICK-dKeptSession-69-spec-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-69-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`origin/main` stands at `8b8b1374`, past this run's BASE `c2a407b0`, and every commit in this worktree
now runs the primary tree's hooks, which are main's, over this branch's pre-main tree. So no commit
lands, a records-only one included. This unit is the one commit that reconciles them: a merge of
`origin/main` whose conflicts are resolved by rule, whose two list factories become main's one, and
which clears the reds this run's own units left, so main's hooks pass over it.

## 2. Scope (IN)

- **S1** — The reconcile commit (F-merge). The main loop runs `git merge --no-ff --no-commit
  origin/main` in the run worktree. The builder resolves the conflicts by S2, S3 and S7 and makes S4
  to S6 and S8 to S11 in that worktree, and commits nothing. The main loop then commits the merge with
  this spec, its records and the trailer `Pass: KICK-dKeptSession-69`, through `git commit` with the
  hooks running. A refused commit goes back to the builder; the merge is never committed with a hook
  skipped. Observed by AC1, AC2.
- **S2** — The three generated outputs are re-rendered, never hand-merged: `.governance/policy.json`,
  `help/reference/policy.md` and `memory/map/generated/symbols.json`. Each conflicted file is first
  checked out from main's side, to clear its markers, then rewritten by S4's regeneration. Observed
  by AC3.
- **S3** — The row registries, each unioned and then shrunk or re-derived by its own verb, per §4
  "The thirteen files". Main has converted three of them to the ledger grammar, so the union starts
  from main's ledger, then each file's own verb shrinks it to the tree. The one key the run gained,
  the dKeptSession packet's spec-count fact, enters `memory/project/unpinned-facts.txt` through the
  factory's widen route under this unit's widen record. Observed by AC4.
- **S4** — The regeneration and the stamp. With every conflict resolved and staged, the builder
  regenerates over a provisional commit of the merge, as `run_pass_tree_regen` does
  (`tools/unattended/pass-tree.sh#run_pass_tree_regen`): `git write-tree`, `git commit-tree <tree> -p
  HEAD -p MERGE_HEAD -m provisional`, `git update-ref --no-deref HEAD <it>`, `python
  tools/run-gates/regen.py --write`, then `git symbolic-ref HEAD refs/heads/<the run branch>` whatever
  the write's exit. The kickoff manifest's `last-audit:` line in `memory/guides/SESSION-KICKOFF.md` is
  written as one stamp, `<ISO-8601 now> @ <the full sha of the merge's first parent>`, as both sides
  stamp their own parent. Observed by AC3, AC5.
- **S5** — One list factory (F-factory, §8 F1). The shrink-list factory is deleted:
  `read_shrink_base`, `write_shrink_file`, `check_shrink_list`, `write_shrink_list` and
  `read_base_pairs` in `tools/policy/policy.py`, with `UNNAMED_HEADER` and `UNPURPOSED_HEADER`. The
  legacy-home list is main's ledger as main has it. `tools/policy/unnamed-keys.txt` and
  `tools/policy/unpurposed-namespaces.txt` are deleted and become two populations of main's baseline
  ledger factory (`tools/memory-tree/legacy_ledger.py`), `unnamed-keys` and `unpurposed-namespaces`,
  each a `[[ledger]]` table in `tools/govkit/registry.toml` beside `legacy-homes`, gov's own (§8 F2):
  `leg = "policy check"`, `key = "key"`, `fields` `["name"]` and `["namespace"]`, `drain = "key"`,
  `direction = "shrink-only"`, homes `memory/project/unnamed-keys.txt` and
  `memory/project/unpurposed-namespaces.txt`, seeds `["python", "{prefix}/policy/policy.py", "lists",
  "--derive", "<population>"]`. Each home is seeded once at the reconcile by `python
  tools/memory-tree/legacy_ledger.py seed --population <population>`, and `.gitattributes` gains a
  `merge=rows` line per home, as TOOL-dWitnessedBar-13 §3 leaves to each unit adding one, the two
  under one comment line naming this unit, as `legacy-homes.txt`'s line has its own.
  `.memory-tree.conf`'s `PROJECT_REGISTRY_EXTRA` gains `unnamed-keys.txt` and
  `unpurposed-namespaces.txt`, since check 3 admits a file directly under `memory/project/` only
  when its named list or that key names it, and the key's comment block gains one member note for
  the pair in the style of `legacy-homes.txt`'s (TOOL-dWitnessedBar-20 §8 F7): moved here from the
  policy kit's directory, the ledger populations of the reader-join and purposes arms, by §8 F2, and
  gov-only. No fixture case S6 moves reads either gov home, each seeding its own in a scratch
  repository, so the `policy fixtures` guard in `tools/govkit/registry.toml` gains neither. Where the
  guard trace names one, that guard gains it, as TOOL-dWitnessedBar-20 S2 gave it `legacy-homes.txt`,
  and S4's regeneration re-renders `tools/gate-legs.json` from it. Observed by AC6, AC7, AC18.
  **Readers:** by name: `tools/policy/policy.py` spells all seven names, `tools/policy/README.md`
  the four factory functions, and `tools/policy/check_policy.py` spelled the list writer and the
  unnamed-keys header in `run_reader_join` until S6 moves that arm to the population, so the built
  tree spells neither there; the two list files are spelled by `tools/policy/policy.py`,
  `tools/policy/check_policy.py`, `tools/policy/README.md`, `help/policy.md`, `tools/policy/kit.toml`
  for unnamed-keys and the `tools/policy/catalogue.toml` comment for unpurposed-namespaces, which
  keeps the file's name · by value:
  `check_unnamed_list`, `check_unpurposed_list`, `cmd_lists`, `arm_reader_join` and `arm_purposes`
  compare the two lists' rows, and each moves to the population in S6.
- **S6** — The callers (§4 "The callers"). `read_legacy_registration` and `check_legacy_graded` take
  `population=LEGACY_POPULATION`, so their callers stay as main has them. Two shared functions grade
  and drain a population of plain names through the factory's calls, `check_name_ledger(repo, kit,
  population, derived, unlisted)` and `write_name_ledger(repo, kit, population, derived)`.
  `check_unnamed_list(repo, kit, design)` and `check_unpurposed_list(repo, kit)` become one call each.
  `cmd_derive_list` admits the two populations. `cmd_lists`, `arm_reader_join`, `arm_purposes` and the
  fixture cases `reader-join`, `reader-join-blank` and `purposes-*` move to the populations, and
  `build_repo` and `run_fixture` stop copying `policy.UNPURPOSED_LIST`. Observed by AC7, AC8, AC9.
- **S7** — The product hunks, by F-factory (§4 "The thirteen files"): `tools/policy/policy.py`,
  `tools/policy/check_policy.py`, `tools/policy/kit.toml` and `tools/policy/README.md`. The page
  `help/policy.md` names the two homes and says the lists are ledgers. Observed by AC6, AC10.
- **S8** — The shell-hygiene reds (F-own-reds). In `skills/session-kickoff/card-store.fixture.sh` the
  three bare probes, the `RT=`, `WT=` and `C2=` captures of `git -C <dir> rev-parse
  --show-toplevel`, each open their substitution with `unset GIT_DIR GIT_WORK_TREE; `, the one scrub
  the lint accepts, as the file's own `GOVROOT=` capture does. `write_card_records`
  (`skills/session-kickoff/card-store.fixture.sh#write_card_records`) tests the stage before its
  commit, `! git -C "$R" diff --cached --quiet &&`, as `write_card_fixture` tests its own. In
  `skills/session-kickoff/manifest-check.sh` `read_session_cli_version` assigns a named variable by
  `printf -v`, as `getval` does (`skills/session-kickoff/manifest-check.sh#getval`), and its three
  callers stop capturing it. Each `$(cat <file>)` this run added to `tools/hooks/scratch-guard.test.sh`
  becomes `$(<file)`. Each count returns to its row and no registry row moves. Observed by AC11,
  AC12.
- **S9** — The `python reads` red (F-own-reds). The guard of each leg the guard arm names, the
  build-index selftest, the gotchas selftest, the memory-recall kit selftest, the recall floor and the
  recall floor arms, gains each module its import closure walks outside it, as `python
  tools/run-gates/py_reads.py --guards <leg>` prints them on the merged tree: `{prefix}/policy/presets.py`
  on each, and `{prefix}/memory-tree/design_lib.py` on the three whose guards name memory-tree files
  one by one. Observed by AC13.
- **S10** — The `step-rows-frozen` red (F-own-reds, §8 F3). The landed step program
  `tools/govkit/steps/kickoff_facts_to_overlay.py` returns to its landed blob, `bf63aab8`, the same at
  `c2a407b0` and at `8b8b1374`. Its fixture's bare `scaffold` call is then refused by `cmd_scaffold`
  (`tools/policy/policy.py#cmd_scaffold`), so `build_fact_fixture` writes an empty policy file, which
  resolves every key to its catalogue default, the values the starter file held before
  KICK-dKeptSession-4. AC15's plants decide §8 F3. Where all hold, nothing else moves. Where one
  fails, `cmd_scaffold` admits a call naming neither flag and prints `render_scaffold(rows, None)`,
  exit 0, `--kept` with no `--preset` stays refused, `USAGE` spells `scaffold [--preset <name>
  [--kept <file>]]`, and a fixture case `scaffold-bare` observes it. No new step row is shipped.
  Observed by AC14, AC15.
- **S11** — The two inherited reds (F-inherited) and any further red the merged tree shows. Each leg
  of the pre-commit set that is red on the merged tree is read alone at `8b8b1374` in a detached
  scratch worktree. Red there too, it is INHERITED: the main loop's close attributes it with
  `GATE_ATTRIBUTE=8b8b1374` and this unit's ledger names it. Green there, it is this unit's to fix,
  in this commit, and its ledger names the fix. Observed by AC16.
- **S12** — The superseded CLOSED text (§4 "Superseded text"), answered in this unit's own acceptance
  ledger, `memory/builds/dKeptSession/build/2026-11-22-build-KICK-dKeptSession-69-1-acceptance-ledger.md`,
  which quotes each passage and states which scope item here supersedes it, as KICK-dKeptSession-49
  rev-6 ruled. No CLOSED unit's spec or ledger is written. Observed by AC17.

## 3. Non-goals (OUT)

- The summary list `tools/policy/unsummarised-keys.txt`. It stays on main's own `check_list` and
  `write_list`. It ships to every adopter, so moving it onto the ledger factory owes an upgrade step.
- The unscanned-readers list. It is AUTHORED, one reason per row, and read by `read_unscanned_readers`
  (`tools/policy/check_policy.py#read_unscanned_readers`), never by the shrink-list factory, so it
  does not move. The brief's sentence placing it on that factory does not hold at `e7ab8c81`.
- A new `[[upgrade]]` row for KICK-dKeptSession-4's edit (§8 F3).
- Any auto-merged file beyond what a fix here needs. Each arrives as the merge writes it.
- Committing, rendering an index, or starting the merge in this pass. Those are the main loop's acts.

### Edges

- **consumes-from** external — `origin/main` at `8b8b1374` and the primary tree's hooks, which grade the reconcile commit; this unit edits neither the hooks nor main's history
- **hands-off** external — the summary list's move onto the ledger factory with its adopter step, an ask the main loop files at the close

## 4. Design

### Evidence

- A read-only `git merge-tree --write-tree HEAD origin/main` at `e7ab8c81` conflicts in thirteen
  files, PINNED 2026-11-22, the brief's set. Its hunk counts: `policy.py` 6, `check_policy.py` 2,
  `kit.toml` 2, `README.md` 4, `policy.json` 2, `symbols.json` 15, one in each other file, PINNED
  2026-11-22 by `grep -c '^<<<<<<<'` over that tree.
- Main's legacy list is a ledger: `check_legacy_homes` and `write_legacy_homes` grade and write the
  `legacy-homes` population through the factory's `read_ledger`, `compare_counts`, `compare_to_base`
  and `write_rows`, and `read_legacy_registration` finds its registration in govkit's registry
  (`tools/policy/policy.py#check_legacy_homes` at `8b8b1374`). The run's six `policy.py` hunks are the
  same functions on the shrink-list factory, plus the module head, `USAGE` and `cmd_lists`.
- The factory carries a population of plain names: a `key`-kind table with one field, rows `<name>
  TAB <count> TAB <sha> TAB <disposition>`. Its compare grades `gained` and `raised` under
  `shrink-only`, and `compare_counts` grades an undeclared and an unmeasured key both ways
  (`tools/memory-tree/legacy_ledger.py#compare_counts`, `#compare_to_base` at `8b8b1374`). Those are
  the three findings `check_shrink_list` makes: unlisted, stale and grown.
- `check_unnamed_list` and `check_unpurposed_list` each return one `check_shrink_list` call, and
  `cmd_lists` drains both by `write_shrink_list` (`tools/policy/policy.py#cmd_lists`). The fixtures
  that read the lists are `run_reader_join`, `run_purposes_case`, `build_repo`, `run_fixture` and
  `build_legacy_repo` (`tools/policy/check_policy.py#run_reader_join` and siblings).
- Main's registrations under `memory/project/` each have a `merge=rows` line in `.gitattributes` at
  `8b8b1374`, `memory/project/legacy-homes.txt` among them.
- Memory hygiene's check 3, in `tools/memory-tree/check-memory-hygiene.sh`, prints its failure line
  naming each file directly under `memory/project/` that neither its named case list nor a
  `PROJECT_REGISTRY_EXTRA` word matches exactly. `.memory-tree.conf` at `8b8b1374` names
  `legacy-homes.txt` there, with its member note, and neither new home. The `policy fixtures`
  `[[exempt_leg]]` guard names `memory/project/legacy-homes.txt` because its `legacy-homes-present`
  case reads gov's home, and `check_guard_trace` prints `policy-fixture: guard-trace · WRONG <path> ·
  not under the policy fixtures guard` for a traced source read that guard misses
  (`tools/policy/check_policy.py#check_guard_trace`).
- The run's registry deltas against `c2a407b0`, PINNED 2026-11-22 by `git diff c2a407b0 HEAD`:
  `positional-refs.txt` and `docs-undocumented.txt` only drop rows, `core-pending.txt` drops `kind
  kind.preset dKeptSession`, `selftest-budgets.txt` moves the `loop scenario fixtures` row and its
  `plants=` token from 13 to 16, and `unpinned-facts.txt` drops rows and re-keys one, the dKeptSession
  packet's spec count. Rows the run holds that neither main nor `c2a407b0` holds: that packet row
  alone, by `comm` over the key fields, PINNED 2026-11-22.
- The widen route appends only the keys a home lacks, each `widened:<record>`
  (`tools/memory-tree/legacy_ledger.py#seed_population` at `8b8b1374`). Main's widen records are
  `memory/builds/<slug>/build/<date>-build-<id>-widen-<n>.md`, carrying Population, Keys, Reason and
  Caused-by lines.
- `check_frozen` reds a landed step whose argv's program moved bytes between the push base and HEAD
  (`tools/govkit/upgrade_steps.py#check_frozen`). The row `kickoff-manifest/facts-to-overlay` names
  `kickoff_facts_to_overlay.py` in its three argvs (`tools/govkit/entries/kickoff-manifest.kit.toml`).
  KICK-dKeptSession-4's edit to it is one line of `build_fact_fixture`, the program's own fixture,
  adding `--preset standard` to its `scaffold` call; its up, down and witness are untouched.
- `cmd_scaffold` refuses a call naming no `--preset` (`tools/policy/policy.py#cmd_scaffold`), so
  the restored fixture would write an empty policy file, the outcome KICK-dKeptSession-4 S4 names
  for its two bare runs. The adopter refuses a posture-less scaffold on its own, before it calls the module
  (`tools/policy/adopt-policy.sh`, its "names no preset to write" refusal).
- `cmd_mirror` renders a committed revision and refuses uncommitted inputs, and the lander and
  `pass-tree.sh` regenerate over a provisional commit for that reason (KICK-dKeptSession-67 §4).
- The spawn-idiom lint classes `$(f …)` as `pure-fn-subst` where `f`'s body spawns nothing, and
  `$(cat <word>)` as `cat-file`, `$(<file)` being its no-fork form
  (`tools/gate-lint/sh_hygiene.py#run_spawn_scan`). `read_session_cli_version` spawns nothing and
  three new captures of it are the three sites over the row.
- The guard arm reds a module a leg's import closure walks outside its guard, a literal
  `resolve_kit_dir` call included (`tools/run-gates/py_reads.py`, its header). `policy.py` imports
  `presets` and resolves `design_lib.py` by such a call at `e7ab8c81`.
- `arm_reader_coverage` grades the catalogue keys whose owner has landed
  (`tools/policy/check_policy.py#arm_reader_coverage`). dWitnessedBar landed at `8b8b1374`, so its
  keys' readers are main's code, absent from the run head. The drift ratchet compares the tree's
  pins with the base's, which main moved into `memory/project/drift-pins.txt`; the run touches no
  drift-audit file. Both reds read main's state against a tree without main's code, so both are
  expected green on the merged tree, and S11 decides if not.

### The thirteen files

| File | Resolution |
|---|---|
| `tools/policy/policy.py` | Main's `check_legacy_homes`, `write_legacy_homes` and `cmd_derive_list`; `read_base_pairs` dropped. The module head names main's ledger sentence and the run's presets sentence, with KICK-dKeptSession-19's and -16's lists as ledger populations. `USAGE` unions both sides' verbs, `lists --derive <population>` among them. `cmd_lists` is main's legacy branch, then the run's single design read, then S6's two populations. |
| `tools/policy/check_policy.py` | The module head keeps main's legacy sentence and the run's two arm sentences, each list named a gov-own ledger population at its home. `build_legacy_repo` is main's body, its docstring main's, the run's `policy.UNPURPOSED_LIST` copy dropped. |
| `tools/policy/kit.toml` | Main's two hunks: the `project-owned` rule names `unscanned-readers.txt` alone, and the comment says the other lists are ledgers at their homes. |
| `tools/policy/README.md` | Main's text in its four hunks, plus the run's presets rows and the run's `adopt-policy.sh` row. The two lists leave the kit's file table and are described as legacy-homes is. |
| `.governance/policy.json` · `help/reference/policy.md` · `memory/map/generated/symbols.json` | S2: main's side, then S4's render. |
| `memory/project/positional-refs.txt` | Main's ledger, then `python tools/playbook/positional.py shrink`. |
| `memory/project/unpinned-facts.txt` | Main's ledger, then `python tools/playbook/writing_practice.py check pinned-facts --shrink`, then `python tools/memory-tree/legacy_ledger.py seed --population unpinned-facts --widen 2026-11-22-build-KICK-dKeptSession-69-widen-1`. |
| `memory/project/docs-undocumented.txt` | Main's ledger less `policy:card.pointers`, deleted by hand as the file's leg asks, since KICK-dKeptSession-13 documents it. |
| `tools/playbook/core-pending.txt` | Both deletions: neither `kind.preset` nor `kind.gate-leg` keeps a row. |
| `tools/run-gates/selftest-budgets.txt` | Main's rows, with the run's `loop scenario fixtures` row, budget 275 and `plants=16`, in place of main's. |
| `memory/guides/SESSION-KICKOFF.md` | S4's one stamp. |

### The callers

- `check_name_ledger` reads the registration through `read_legacy_registration(repo, kit,
  population)`. It compares the home's first line with `render_header`, then runs
  `compare_counts({(n,): 1 for n in derived}, <declared counts>, reg.direction)` and
  `compare_to_base(repo, reg)`. An `undeclared site` is `(name, unlisted)`, an `unmeasured row` is
  `(name, "stale: drain it with lists --write")`, and a `gained` row is `(name, "added to a
  shrink-only list above the base")`. A malformed row is `(line, its render)`. Its note is the
  `compare_to_base` reason. It returns `(findings, note)`, the shape both arms already read.
- `write_name_ledger` writes `declared ∩ derived` through `write_rows`, each kept row's count, sha and
  disposition unchanged, and returns the drained names. It creates no home: only the seed does.
- `cmd_derive_list` prints `<name> TAB 1` per derived name for either new population, each name from
  `derive_unnamed_keys` or `derive_unpurposed`. `--marks` names `legacy-homes` alone. A design that
  does not read exits 2 with its reason, so a seed over it is left unarmed.
- `cmd_lists` grades and drains each population where `check_legacy_graded(top, KIT, <population>)`
  holds, and prints `policy lists: <file> · not graded · <LEGACY_WITHHELD>` elsewhere, the legacy
  list's rule. Its lines keep the file names `UNNAMED_LIST` and `UNPURPOSED_LIST` spell.
- `arm_reader_join` grades where that rule holds and otherwise prints its `not graded` line, as today.
  `arm_purposes` keeps `check_namespaces` everywhere; where the rule does not hold it prints `policy
  purposes: unpurposed-namespaces.txt · not graded · <why>`, and every unpurposed namespace prints as
  awaiting review with no finding.
- `reader-join` and `purposes-drain` build on `build_legacy_repo` and seed their population by the
  factory's seed, as main's legacy cases do. `purposes-new` leaves the seed table for
  `run_purposes_case` on that repository, since `build_repo` holds no registry. `reader-join-blank`
  keeps its blank conf.
- Under §8 F3's fallback alone, a case `scaffold-bare` in `tools/policy/check_policy.py` runs the
  copy's `policy.py scaffold` with no flag: exit 0, stdout `render_scaffold(rows, None)`, no `preset =`
  line.

### Superseded text

S12's ledger quotes these passages and names its superseding item:

- KICK-dKeptSession-19 S1, the shrink-list factory, and S2's legacy-home sentences: S5.
- KICK-dKeptSession-19 S4, "the list `tools/policy/unnamed-keys.txt`" and "its name joins the
  `project-owned` `[[files]]` rule", and S5's withheld reading: S5 and S6.
- KICK-dKeptSession-16 S4, "written through KICK-dKeptSession-19's `write_shrink_list`" and "The list
  ships to adopters … so `kit.toml` is unchanged": S5 and S6.
- KICK-dKeptSession-16 S7, "`build_repo` copies the new list" and "`purposes-new` is a seed case":
  S6.
- KICK-dKeptSession-4 S4, its `build_fact_fixture` clause, "the two bare runs read stdout only":
  S10. Under §8 F3's fallback, S2's "a call naming no preset exits 2 with the usage line" too.

### What it does not check

- That a seeded name is not this run's own. The seed is the merged tree's derivation. At `e7ab8c81`
  the brief reads `policy check` red on `arm_reader_coverage` alone, so the run's lists were green
  there, and a name the seed holds that they lacked came with main's tree. AC7 prints those for the
  ledger.
- That an empty policy file and the starter file read alike beyond what the sixteen plants grade.
- Any leg not in the pre-commit set; the close's bar reads those.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_name_ledger`, `write_name_ledger` | function, `policy.py` | `check_`, `write_` verbs |
| `UNNAMED_POPULATION`, `UNPURPOSED_POPULATION` | constant, `policy.py` | none: constants |
| `unnamed-keys`, `unpurposed-namespaces` | ledger population | none |
| `scaffold-bare` | fixture case, under §8 F3's fallback alone | none |
| `2026-11-22-build-KICK-dKeptSession-69-widen-1` | widen record | none |

### Migration

No adopter holds either list: both arrived with this run, which main never held. The two homes are
seeded once at the reconcile, absent at the base, so the base compare prints its reason and grades
nothing until the next landing. Reversal is `git revert -m 1` of the reconcile commit.

### Rollout

Live at the commit. The run's later passes merge onto the reconciled branch.

### Files touched (estimate)

Every other path `git diff --name-only HEAD origin/main` lists arrives as the merge writes it.

- `tools/policy/policy.py`, `tools/policy/check_policy.py`, `tools/policy/kit.toml`,
  `tools/policy/README.md`: S5 to S7, S10
- `tools/policy/unnamed-keys.txt`, `tools/policy/unpurposed-namespaces.txt`: deleted
- `memory/project/unnamed-keys.txt`, `memory/project/unpurposed-namespaces.txt`: seeded
- `tools/govkit/registry.toml`: S5, its two `[[ledger]]` tables, and the `policy fixtures` guard
  only where the guard trace names a home
- `.gitattributes`: S5, the two `merge=rows` lines and their comment line
- `.memory-tree.conf`: S5, the two `PROJECT_REGISTRY_EXTRA` words and their member note
- `help/policy.md`: S7
- `.governance/policy.json`, `help/reference/policy.md`, `memory/map/generated/symbols.json`: S2
- `memory/project/positional-refs.txt`, `memory/project/unpinned-facts.txt`,
  `memory/project/docs-undocumented.txt`, `tools/playbook/core-pending.txt`: S3
- `tools/run-gates/selftest-budgets.txt`: S3, its `loop scenario fixtures` row's `plants=` token
- `skills/session-kickoff/card-store.fixture.sh`, `skills/session-kickoff/manifest-check.sh`,
  `tools/hooks/scratch-guard.test.sh`: S8
- `tools/gate-legs.json`: S9, and S5 where the `policy fixtures` guard gains a home, rendered by
  S4's regeneration from the declarations
- `tools/govkit/steps/kickoff_facts_to_overlay.py`: S10, restored
- `memory/guides/SESSION-KICKOFF.md`: S4's `last-audit` re-stamp, owed because `tools/gate-legs.json`
  and `skills/session-kickoff/manifest-check.sh` sit on its `watch:` line
- `memory/builds/dKeptSession/build/2026-11-22-build-KICK-dKeptSession-69-1-acceptance-ledger.md`,
  `memory/builds/dKeptSession/build/2026-11-22-build-KICK-dKeptSession-69-widen-1.md`: S12, S3
- `memory/builds/dKeptSession/README.md`, `memory/LIVE.md`, `memory/backlog/KICK.md`: rendered by the
  memory-hygiene leg's staged write, never hand-edited

### Alternatives rejected

- **Keep the shrink-list factory for the plain-name lists.** Main's factory already carries a
  plain-name population and grades the same three findings, so a second factory of one kind is what
  `[reuse]` refuses (§8 F1).
- **Put main's legacy list back on the shrink-list factory.** It undoes a landed unit,
  TOOL-dWitnessedBar-20, and leaves the run's lists off the factory every other registry uses.
- **Register the moved lists in the policy kit's `kit.toml`, shipped.** Every adopter would carry a
  population to seed whose rows derive from gov's catalogue, the same in every install (§8 F2).
- **Commit the merge, then regenerate in a follow-up commit.** The merge's hooks would grade it before
  its outputs are fresh, and the brief allows one commit.
- **Hand-merge the generated outputs.** No hand can reproduce a render's bytes.
- **Ship KICK-dKeptSession-4's edit as a new step row** (§8 F3).

## 5. Production-readiness checklist

- security — no new write path or surface. The two homes are written by the factory's `write_rows`,
  which refuses a home outside the tree. The commit goes through the hooks.
- perf / scale — two seeds and one regeneration, once.
- error / empty / loading states — a population absent at the base prints its reason, never green. A
  design that does not read exits 2 from `--derive`, and the seed records the home unarmed.
- observability — `lists --check` names each population with its note. Each attributed red is a
  ledger line.
- risks — a leg of main's set red over this run's code that no criterion names. S11 makes it this
  unit's, and the commit cannot land past it.
- testing — the fixture cases S6 moves, red at `e7ab8c81`, and `scaffold-bare` under §8 F3's
  fallback.
- migration — none for adopters; §4 "Migration".
- user docs — `help/policy.md` (S7); `help/reference/policy.md` re-rendered (S2).

## 6. Acceptance criteria

Each criterion is observed in the run worktree, after the main loop's reconcile commit unless it says
"staged", which reads the resolved merge before that commit.

- **AC1** — Staged: `git ls-files -u` prints nothing, and `git grep -n '^<<<<<<< ' --` over the
  thirteen files prints nothing.
  Red when: a conflict is left unmerged or a marker is committed.
- **AC2** — `git rev-parse HEAD^2` prints `8b8b1374c4fc89be2ae3a5aae88dafd74e6acd8e`, `git rev-parse
  HEAD^1` prints the run head the merge started from, and `git log -1 --format=%B | grep -c '^Pass:
  KICK-dKeptSession-69$'` prints `1`.
  Red when: the reconcile is a rebase, a squash or a commit without the trailer.
- **AC3** — `python tools/run-gates/regen.py --check` exits 0, and `python tools/policy/policy.py
  mirror --check` prints `policy: mirror fresh`.
  Red when: a generated output is hand-merged or left at one side's bytes.
- **AC4** — `python tools/playbook/positional.py check` exits 0, `python
  tools/playbook/writing_practice.py check pinned-facts` prints `pinned-facts: green · 0 red`, and
  `python tools/playbook/core.py meta-check` exits 0. Over
  `memory/project/unpinned-facts.txt`, `grep -c widened:2026-11-22-build-KICK-dKeptSession-69-widen-1`
  prints `1`. `grep -c '^policy:card.pointers'
  memory/project/docs-undocumented.txt` prints `0`.
  Red when: a registry is resolved to the run's side, a gained key is hand-written `seeded`, or a
  dropped row survives.
  figure: the widened count of 1 is PINNED 2026-11-22 by the `comm` probe of §4 "Evidence".
- **AC5** — Staged: `bash skills/session-kickoff/manifest-check.sh --staged` exits 0, and
  `grep -c '^last-audit: ' memory/guides/SESSION-KICKOFF.md` prints `1`, its sha the merge's first
  parent.
  Red when: both stamps are kept, or the stamp names a commit the audit did not read.
- **AC6** — `git grep -n -e read_shrink_base -e write_shrink_file -e check_shrink_list -e
  write_shrink_list -e read_base_pairs -- tools/ help/` prints nothing, `git ls-files tools/policy/ |
  grep -c -e unnamed-keys -e unpurposed-namespaces` prints `0`, and `git
  check-attr merge -- memory/project/unnamed-keys.txt memory/project/unpurposed-namespaces.txt`
  prints `merge: rows` for each.
  Red when: a second factory or a kit-dir copy of either list survives.
- **AC7** — `python tools/policy/policy.py lists --check` exits 0 and prints a `policy lists:
  unnamed-keys.txt` and a `policy lists: unpurposed-namespaces.txt` line, neither saying `not graded`
  and neither followed by a header finding, so the unnamed-keys home opens `# ledger · unnamed-keys ·
  key key name · direction shrink-only · drain key`. `comm -23` of each home's sorted first column
  against the sorted names of its `git show e7ab8c81:tools/policy/<file>` prints the names the ledger
  lists as main's.
  Red when: a home is unarmed, a list is not graded in gov's tree, or the ledger omits a printed name.
  figure: the difference is DERIVED at observation.
- **AC8** — `python tools/policy/check_policy.py` exits 0, and its `arm_reader_join` and
  `arm_purposes` lines name the populations.
  Red when: an arm still reads a kit-dir list, which is absent, and reds or announces nothing.
- **AC9** — The fixture cases `reader-join`, `purposes-new` and `purposes-drain` hold
  in the policy fixtures leg, read from its run record at the close.
  Red when: a case still writes the unnamed-keys list into its kit copy's directory, as at `e7ab8c81`.
  permission: the leg runs at the close, never in this pass.
- **AC10** — `grep -c 'memory/project/unnamed-keys.txt' help/policy.md` and `grep -c
  'memory/project/unpurposed-namespaces.txt' help/policy.md` each print at least `1`, and `grep -c
  'tools/policy/unnamed-keys.txt\|tools/policy/unpurposed-namespaces.txt' help/policy.md` prints `0`.
  Red when: the page still names the kit-dir lists, as at `e7ab8c81`.
- **AC11** — `python3 tools/gate-lint/sh_hygiene.py --location-probes
  memory/project/location-probe-waivers.txt . ':!memory/'` exits 0, and `python3
  tools/gate-lint/sh_hygiene.py --stage-commits memory/project/stage-commit-sites.txt . ':!*.test.sh'
  ':!memory/'` exits 0. `git diff HEAD^2 HEAD -- memory/project/location-probe-waivers.txt
  memory/project/stage-commit-sites.txt` prints nothing.
  Red when: a probe is waived or a site registered instead of fixed; at `e7ab8c81` both name
  `card-store.fixture.sh`.
- **AC12** — `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt
  . ':!*.test.sh' ':!memory/'` exits 0, printing `pure-fn-subst` × 2 for `manifest-check.sh` and
  `cat-file` × 11 for the scratch-guard suite, and `git diff HEAD^2 HEAD --
  memory/project/spawn-idiom-sites.txt` prints nothing.
  Red when: a row is raised to fit the count; at `e7ab8c81` the counts are 5 and 20, the brief's
  reading.
- **AC13** — `python tools/run-gates/py_reads.py` exits 0 and prints no `py-reads: RED` line.
  Red when: a guard misses a module its closure walks; at `e7ab8c81` it prints `RED guard` lines
  naming `presets.py`.
- **AC14** — `git ls-tree HEAD tools/govkit/steps/kickoff_facts_to_overlay.py` prints the blob
  `bf63aab8aafdcfe3cf645325f945ee97305c73b3`, and `python tools/govkit/upgrade_steps.py frozen` exits
  0.
  Red when: the program keeps KICK-dKeptSession-4's line, which reds the leg naming it.
- **AC15** — Each plant `python -I tools/govkit/steps/kickoff_facts_to_overlay.py --fixture --plant
  <case>` lists exits 0 and prints ` · 0 failed`. Under §8 F3's fallback, `python
  tools/policy/policy.py scaffold` also exits 0, and piped into `grep -c '^preset = '` prints `0`.
  Red when: a plant fails over the empty policy file and bare `scaffold` still exits 2.
  cost: sixteen plants, each its own scratch repository, minutes in all.
- **AC16** — `python tools/drift-audit/drift_report.py --check` exits 0 with no `RATCHET WEAKENED`
  line on stderr, and AC8's run prints no `arm_reader_coverage` finding. Any pre-commit leg red at the
  commit has a ledger line naming INHERITED or its fix.
  Red when: a red read OWN at `8b8b1374` is attributed instead of fixed.
  fixture: a detached scratch worktree of `8b8b1374`, made only where a leg stays red.
- **AC17** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger, piped into `grep -c "two bare runs
  read stdout only"` and into `grep -c "ships to adopters"`, prints `1` each, and `git diff --name-only
  HEAD^1 HEAD --` over the specs of KICK-dKeptSession-4, -16 and -19 and their acceptance ledgers
  prints nothing.
  Red when: a superseded passage goes unquoted, or a CLOSED unit's record is written.
- **AC18** — `git ls-files memory/project/unnamed-keys.txt memory/project/unpurposed-namespaces.txt`
  prints both paths, so check 3's population holds both homes. `bash
  tools/memory-tree/check-memory-hygiene.sh --only 3` then exits 0 and prints no failure line for
  memory hygiene's check 3. `grep '^PROJECT_REGISTRY_EXTRA=' .memory-tree.conf | tr ' "' '\n\n' | grep -cx -e
  unnamed-keys.txt -e unpurposed-namespaces.txt` prints `2`. AC9's run record holds no
  `guard-trace · WRONG` line naming either home.
  Red when: a home is seeded with no `PROJECT_REGISTRY_EXTRA` word, which check 3 prints among its
  unexpected entries, the reading the builder's divergence made at `e7ab8c81`.

## 7. Gates

`policy check` · `policy fixtures` · `build-index selftest` · `gotchas selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `routed-commits selftest` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `manifest-check self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `python reads (a name never bound, an import outside its guard)` · `step-rows-frozen` · `drift-audit records` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a stage committed with no staged-diff test)` · `shell hygiene (a fork spent on builtin work)` · `kickoff-manifest ratchet` · `govkit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `ratchet (both ways)` · `ratchet (never gains)` · `ratchet (populated)` · `ratchet (seed laundering)` · `ratchet (unarmed)` · `ratchet (key shape)` · `row-driver view refusal` · `kit/dogfood doc parity` · `straggler-guard arms` · `transition-audit arms`

The pass's own legs are `bash tools/run-gates/pass-legs.sh --base <the run head>`, which the main loop
runs over the staged merge before its commit. No suite runs in this pass.

New arm: tools/policy/check_policy.py · covers AC7 AC9 · `reader-join`, `purposes-new` and `purposes-drain` over a gov-shaped kit copy, with `scaffold-bare` under §8 F3's fallback, staged RED against `policy.py` at e7ab8c81, where the cases write the kit-dir lists · none

## 8. Open questions

- **F1 — How do the two list factories meet?** Options: (a) main's baseline ledger factory alone,
  legacy-homes as main has it, the run's two lists moved onto it and the shrink-list factory deleted;
  (b) keep the shrink-list factory for the plain-name lists beside the ledger; (c) put legacy-homes
  back on the shrink-list factory. (b) keeps two factories of one kind, and the ledger already
  carries a plain-name population. (c) reverses a landed unit. RESOLVED (agent, 2026-11-22,
  delegated): (a), rung 3; the brief's default, one factory, the feature-rich one.
  widens: none · relaxes: none
- **F2 — Where do the moved lists live?** Options: (a) gov's own, in govkit's registry beside
  legacy-homes, homes under `memory/project/`; (b) in the policy kit's `kit.toml`, shipped to
  adopters. Both lists derive from gov's catalogue, the same in every install, and the unnamed-keys
  list from gov's design view, which no adopter declares. (b) gives each adopter a population to seed
  that only re-proves gov's result. RESOLVED (agent, 2026-11-22, delegated): (a), rung 3; the
  narrowest surface, and the rule legacy-homes already follows. widens: none · relaxes: none
- **FACT-QUESTION · F3 — How is the frozen step program cleared?** Options: (a) restore it and ship
  KICK-dKeptSession-4's edit as a new `[[upgrade]]` row, the brief's reading of the leg's remedy;
  (b) restore it alone; (c) restore it and let bare `scaffold` print the no-preset render. The edit is
  in the program's fixture, not its up, down or witness, so (a)'s row would migrate nothing and the
  restored program would still call bare `scaffold`. (b) keeps KICK-dKeptSession-4 F2's refusal,
  deny by default, and gives the fixture an empty policy file, every key at its default. (c) reopens
  that F2 at the module, though the adopter keeps its own refusal. RESOLVED (agent, 2026-11-22,
  delegated): (b), rung 3, with (c) where an AC15 plant fails over the empty file; the probe decides,
  and (b) relaxes nothing. widens: none · relaxes: none, or under (c) KICK-dKeptSession-4 S2's
  module refusal
- **F4 — How does the packet's re-keyed fact enter the shrink-only facts ledger?** Options: (a) the
  factory's widen route under this unit's widen record; (b) a hand-written `seeded` row; (c) a pin in
  the packet. (b) reads `gained` against the base, and (c) edits a rendered record. RESOLVED (agent,
  2026-11-22, delegated): (a), rung 3; the route main's own widen records use.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-22 · initial draft, from the brief `2026-11-22-prompt-KICK-dKeptSession-69-spec-brief`,
  grounded at `e7ab8c81` and at `origin/main` `8b8b1374` through `git show` and a read-only
  `git merge-tree`.
- rev-2 · 2026-11-22 · S5 · §4 · §7 · AC6 · AC9 · AC18 · the two homes join `PROJECT_REGISTRY_EXTRA` with a member
  note, and `.memory-tree.conf` joins Files touched; the `.gitattributes` comment line, the `policy
  fixtures` guard rule and the `tools/gate-legs.json` render are stated; the legs grading every
  registered population, and the three `.memory-tree.conf` trips, join §7; AC6's kit-dir probe greps
  `tools/policy/` and AC9's red names the list, so neither names a path the build deletes; from the brief `2026-11-22-prompt-KICK-dKeptSession-69-divergence-brief`.
- rev-3 · 2026-11-22 · S5 · the Readers clause's by-name half no longer lists the list writer and the
  unnamed-keys header as `tools/policy/check_policy.py` spellings, since S6 removes both from
  `run_reader_join` and the built tree spells neither; §4 and AC18 name memory hygiene's check 3 in
  words, not by its output spelling; from the brief
  `2026-11-22-prompt-KICK-dKeptSession-69-5-spec-writer`.

## 10. Reuse audit

The seam extended is main's baseline ledger factory, `tools/memory-tree/legacy_ledger.py` at
`8b8b1374`: its `read_registrations`, `read_ledger`, `compare_counts`, `compare_to_base`, `write_rows`
and `seed_population`, which the legacy-home list already calls through
`tools/policy/policy.py#read_legacy_registration` there. The regeneration reuses
`tools/unattended/pass-tree.sh#run_pass_tree_regen`'s provisional-commit condition by hand.
`python tools/codebase-map/reuse_lookup.py "a shrink-only list of plain names graded against its
derivation and a compare base, written by a drain verb"`, run 2026-11-22 at `e7ab8c81`, ranked name
stems only (`derive_kit_prefix`, `derive_tool_root`, `resolve_compare_base`); that map predates main's
factory, so the factory was found by `git show origin/main:` reads. The recall query returned the
dLinkedLibrary reuse scout's ledger registration, this unit's brief and KICK-dKeptSession-19's
factory extraction.

Recall terms used: `python tools/memory-recall/query.py "shrink-only list moved onto the baseline ledger factory and registered in the govkit registry" --terms "ledger population registration shrink-only legacy-homes compare_to_base seed widen read_shrink_base write_shrink_list unnamed-keys unpurposed-namespaces"`
