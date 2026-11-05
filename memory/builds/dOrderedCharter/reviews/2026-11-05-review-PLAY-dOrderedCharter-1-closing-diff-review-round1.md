**Serves:** diff-review PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65

# dOrderedCharter — Tier-2 closing diff review, round 1

*Node `d`, 2026-11-05, on `branch/unattended-dorderedcharter-725f52`. This review covers the cumulative diff landing on main: 131 commits, 460 files, +77641/−3834. Five finder lenses ran, then five skeptic batches prompted to refute each finding, then this synthesis. The binding line names the 30 units with a build commit in the range, which are the 30 specs the review was given. The diff also touches spec files of units still DEFERRED; their code is not in it. Each pin below names the file's blob at the reviewed sha.*

**Range reviewed: `8bec4cefd957d194660a8d7c2916f420b7299074...de8d2d3a1ac4c7601b961e198ff1123067f5bc69`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker. Twenty-two items need fixes: 3 HIGH, 18 MEDIUM and 1 LOW. The three HIGHs are a scoped bar that reuses a green after an `id_grammar.py` edit, a tag check that goes green over text it never read, and a selftest that can set `core.bare` on the real repository under an inherited `GIT_DIR`. Each HIGH sits on a narrow path, and that keeps it below blocker.

One action is owed outside the fixes. This review's own probe replaced the shared `index.db`, and it has not been rebuilt (M17). Run `python tools/playbook/gov_tag.py --rebuild` from the main loop.

## Review shape

Intensity full: raw 27, confirmed 23, refuted 4, unverified 0 (0 uncertain), precision 0.85.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 4 | 2 | 2 | 0 | 0 | 0.50 |
| correctness | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| seams | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| verification | yes | 8 | 7 | 1 | 0 | 0 | 0.88 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 0 BLOCKER, 3 HIGH, 18 MEDIUM, 1 LOW, 22 items in all.

Adjudicated tally by raw confirmed finding: 0 blocker, 3 high, 19 medium, 1 low, 23 in all.

The two differ by one merge: findings 4 and 9 are one defect, item M2.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Verdicts: 0 contradictory demoted to unverified, 0 spurious discarded, 0 duplicates.
- Fixes on confirmed findings: 17 judged sound, 6 judged UNSOUND, 0 none proposed, 0 NOT JUDGED. An unjudged fix would be the finder's proposal and nothing more; none is here.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED (finding 26, high to medium).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 30 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 121 items, each assigned to exactly one of 5 lenses: security 25, correctness 24, seams 24, verification 24, intent 24.
- By design: none supplied, no caller byDesign and no block.

This run is not described as complete, for four reasons.

- The fix and re-grade counts above are non-zero.
- The intent lens read every spec's goal and acceptance criteria, but read the scope sections of only specs 26, 45, 47, 48 and 53, where its task asked for all 30 whole.
- The skeptic confirming finding 13 recorded no reasoning. Its corrected fix stands, and the evidence in M8 is the finder's probe.
- Two probes wrote to the live repository against the write-nothing rule. One set `core.bare` in the shared config, since restored (H3). One replaced the shared `index.db`, not repaired (M17).

## HIGH

### H1 — The recall suites' guards miss the moved `id_grammar.py` (finding 11)

**Where:** `tools/gate-legs.json@cd5bbe15:881`, the guards of `memory-recall kit selftest`, `recall floor` and `recall floor arms`.

**What is wrong:** PLAY-dOrderedCharter-18 moved the id grammar, the conf layer and the index builder out of `memory-recall/` into `tools/memory-tree/id_grammar.py`. Commit 2d03321ab changed no recall guard, and all three guards still name only `memory-recall/` plus unrelated paths. `bench.py`, `extract.py`, `recall_conf.py` and `selftest.py` now import the moved file.

**Consequence:** An edit to `id_grammar.py` alone changes what these suites grade, including `eras`, `extract_records`, `build_index` and `Conf.digest`. `changed()` diffs only the guard paths and `input_key` hashes `git ls-files -s` over the guard alone, so the local scoped bar skips the legs or reuses an earlier green. Before this diff the grammar sat inside the guard. This was read from `run-gates.sh` and the leg guards; no bar was run. Remote CI's `GATE_FULL=1` run ignores guards, so the hole is in the local scoped bar, which is why this is HIGH and not BLOCKER.

**Fix (skeptic judged SOUND):** Add `{prefix}/memory-tree/id_grammar.py` to the guard of all three recall legs and of `drift-audit selftest`, whose `_resolve_ident` and `_resolve_anchors` import it. The `drift-audit` gap is pre-existing, and adding the path is harmless. Prove the fix with a probe that touches `id_grammar.py` alone and shows a scoped bar runs the legs. The `GATE_SELFTESTS=changed` selection for an owned leg reads the epoch set and stays incomplete; `run-gates.sh` documents that as a stated ceiling. None of the three legs has a `[[gate_leg]]` copy in `kit.toml` to keep in sync.

**Left-shift gate:** Checklist class `held-suite-guard-misses-a-sibling-kit` (C38). Add a bar arm that walks each held suite's imports and reds a sibling-kit module outside the leg's guard.

### H2 — `scan_unfenced` drops every line after an unclosed fence at exit 0 (finding 17)

**Where:** `tools/playbook/tag_index.py@6d2d1c9d:211`. Its callers are `extract_doc` (`tag_index.py:239`), `extract_citations` (`tag_index.py:363`), `positional.py:247` and `instruction_units.py:643`.

**What is wrong:** `scan_unfenced` is a second fence walker, new in this diff, and it ends silently inside an unclosed fence. The shared reader `tree_lib.unfenced_lines` yields `(opened_at, None)` so a caller can refuse, and `edge_grammar.py:231` and `design_lib.py:371` do refuse that state. On `intro`, then a line opening with ```` ```x``` ````, then a citation, `scan_unfenced` returned `[(1,'intro')]` and `tree_lib.unfenced_lines` returned `[(1,'intro'),(2,None)]`.

**Consequence:** One stray fence line hides every later span row, symbol citation, retired cite and statement, and the `tags` leg stays green over text it never read. A scan of 10,457 tracked `.md` files found one such file: `memory/builds/dFramedEntrypoint/build/2026-08-24-build-TOOL-dFramedEntrypoint-1-enforcement.md`, open from line 717. So the path is real but narrow. Positional `file:line` rows use `git grep` and are not affected. No plant opens an unclosed fence, so nothing can red this.

**Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Walk `tree_lib.unfenced_lines` and report the `None` sentinel. Print it and never red under `<MEMORY_ROOT>/builds/`, as `positional.py` treats frozen records. Red it elsewhere, and add the bad-citation-after-an-unclosed-fence plant.

**Left-shift gate:** Checklist classes C4 and C49. Add the plant above as an arm of the `tags` leg, and add a checklist line that a Markdown reader walks `tree_lib.unfenced_lines` and never a fence walker of its own.

### H3 — `instruction_units` selftest re-initialises the real repository under an inherited `GIT_DIR` (finding 25)

**Where:** `tools/playbook/instruction_units.py@535bb290:203` (`run_git`), reached from `run_fixture` at line 1682.

**What is wrong:** `run_git` passes the caller's environment through, and `run_fixture` first calls `run_git(top, "init", "-q")`. With `GIT_DIR` inherited, that init acts on the real repository. The sibling `instructions_edit.run_fixture` (lines 948-949) wraps the same call in `set_env_aside(GIT_ENV_LEAKS)`, so the two fixtures disagree. The file is new in this diff.

**Consequence:** `core.bare` flips to true in the shared `.git/config`, and that breaks `git status` in the main checkout and every linked worktree. The finder's probe did this to the live repository: the fixture exited 1 with `fatal: this operation must be run in a work tree`, and all 20 linked worktrees were affected. The finder restored it with `git config --file <common>/.git/config core.bare false`. The skeptic reproduced the mechanism in a disposable main-plus-linked-worktree repo, and the live repo read `core.bare=false` afterwards. Reach is narrow: `.githooks/pre-commit` and `pre-push` unset these names, and `run-gates.sh` unsets `GIT_DIR` in only one subshell (line 370). So it needs the bar or the fixture started with `GIT_DIR` exported. Damage is to config shared across every worktree, which grades it HIGH on a narrow path.

**Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Wrap the body of `instruction_units.run_fixture` in `set_env_aside(GIT_ENV_LEAKS)`, as `instructions_edit.run_fixture` does, calling `load_memory_tree_path()` before importing `deviation_join` and `tree_lib`. Do not take the `run_git`-only option. Add an arm, run in a disposable linked-worktree repo, that asserts both `core.bare` and the outer `index.db` are unchanged.

**Left-shift gate:** Checklist class `inherited-git-dir-pins-the-work-tree-to-the-cwd` (C40). The arm above is the gate. Run it only in a disposable clone, never against this repository.

## MEDIUM

### M1 — `render_unit` runs any `cmd:` row with no registry, bound or cwd (finding 2)

**Where:** `tools/playbook/instruction_units.py@535bb290:430`.

**What is wrong:** `render_unit` runs `subprocess.run(shlex.split(arg))` on any `cmd:<command>` from a manifest row, with no allow-list, timeout or cwd. Spec PLAY-dOrderedCharter-9 section 5 says a command runs "only through the source's own registered probe", and no registry exists. `check_statement` accepts any non-empty `fact` source: `cmd:rm -rf nope` returned no reds. AC5 does require a `cmd:` source to render, so the defect is the unregistered, unbounded, wrong-cwd run and not `cmd:` support itself.

**Consequence:** Once a template carries a `<!-- units: -->` slot, any row in `<prefix>/*/instructions.toml` of the `--target` tree executes on render and on the `--check-render` leg. Gov's tracked tree has neither today, but `resolve_template_path` honours a target's `playbook_path`, so an adopter's own template plus manifest reaches it now. Rendering an untrusted target runs its command. The output lands unvalidated in the agent-loaded charter: a `cmd:python -c` printing two lines rendered as `1\n2`. A hanging command hangs the render. With no cwd, the answer comes from the caller's directory: `cmd:git symbolic-ref --short HEAD` rendered from another repo printed that repo's branch. The effect is contained because a render normally runs on one's own tree.

**Fix (skeptic judged SOUND):** Refuse `cmd:` at the schema check and in `render_unit` unless the command matches a registered entry, as `probe:` already refuses. Run it with `cwd=target`, a timeout and the `GIT_*` scrub, and refuse multi-line output.

**Left-shift gate:** A plant where an unregistered `cmd:` row refuses the render and nothing executes.

### M2 — `print_drift_delta` prints `filled` whatever the reader did (findings 4 and 9)

**Where:** `tools/unattended/unattended.sh@5bd84a9c:1424`.

**What is wrong:** `print_drift_delta` runs `drift_report.py --delta "$base" HEAD || true`, then prints `slot point.runtime.reading · filled` unconditionally. Spec PLAY-dOrderedCharter-17 S6 and S9 make this line carry the slot's state: `filled` when the kit returned something, `searched-empty` when it ran and found nothing. Sibling sites key the state on the outcome: `unattended.sh:14976`, `push-main.sh:884`, and `check_merge_losses`, which maps rc 0 and rc 1.

**Consequence:** `derive_drift_delta` exits 2 on an unresolved argument and a `DriftError` also exits 2, so a failed read prints `filled`. The commoner path is every no-history case: it exits 0 printing `drift-delta: skipped — ...`, and that prints `filled` too. `searched-empty` is unreachable here, and a run's log certifies a reading that never happened. The test arm at `unattended.test.sh:13474` checks only the moved case. The effect is contained: the line is report-only, the reader's error reaches stderr, and the close still returns 0.

**Fix (finding 4's fix judged UNSOUND, this being the skeptic's correction; finding 9's fix judged SOUND and folded in):** Capture the output and the exit code, and print the output as now. On a nonzero exit, print a named line such as `drift-delta: the reader exited <rc>, no delta read`. On exit 0 with a `drift-delta: skipped` line, print `searched-empty`. Otherwise print `filled`. The function still returns 0, so the close is not stopped. Testing for empty output would not work, because the reader always prints at least the `skipped` line.

**Left-shift gate:** Checklist classes `degradation-known-but-unreported` and C17, C71, C116. Add `test.sh` arms for an empty history and for a stub reader that exits 1, asserting no `filled` line on the stub.

### M3 — `read_toml_tags` places a tag on its first mention, not its row (finding 5)

**Where:** `tools/playbook/tag_index.py@6d2d1c9d:265`.

**What is wrong:** `read_toml_tags` takes the first line containing the quoted value. `practices.toml` opens with a `foundation = [...]` list that repeats the tags before any row. Over the shipped file, 36 of 39 rows land on a list line, for example `('practice.yagni','tag',9,9,'  "practice.yagni",')`.

**Consequence:** `gov_tag.py show`, `where` and `bundle`, and an edge's resolved line, serve that path, line and text, so they name the list entry and not the practice's rule. A bundle's node span and byte count for the tag are wrong the same way. No gate result depends on it, so the effect stays in navigation and bundle content.

**Fix (skeptic judged SOUND):** Locate the row, not the value. Scan for the `[[<table>]]` headers and take the `tag =` key line inside the nth table, as `extract_unit` does with its row span. Emit that row's extent as `end_line`.

**Left-shift gate:** Checklist classes `parser-drops-rows-it-cannot-place` and C102. Add a plant with a list naming a tag above its row, and assert every shipped practice row's text starts with `tag =`.

### M4 — `read_records` selects a wider name than `tree_lib` reads (finding 6)

**Where:** `tools/memory-tree/build_records.py@913869b3:144`.

**What is wrong:** `read_records` selects by `[^/]*-<kind>-[^/]*\.md`, while `tree_lib.read_bindings` reads only the exact stem that spec 42 S3 sets. The two copies of the record-name rule disagree on a legal research record such as `2026-11-01-build-PLAY-dX-1-change-plan-2.md` with `**Serves:** research PLAY-dX-1`.

**Consequence:** `tree_lib` keeps that record bound as research, and `build_records` selects it as a change record that `read_change` returns as malformed. `read_change_records` (`instruction_units.py:685`) then raises `UnitRowError`, so the render gate's status arm reds, `render_unit_slots` refuses, and `check_tree` reds status and grades every row with an empty record set. The same shape under `-exception-` gives a malformed exception record, and `derive_admission` turns that into a red in every core gate. No tracked file has this shape today, so it waits for the first such name, and it fails closed. The shape is realistic: spec 42 cites the tracked `-execution-return-plan-2.md` research records.

**Fix (skeptic judged SOUND):** Select with the stem the reader uses, `derive_record_name(kind)` or `tree_lib`'s typed-name rule, for every kind but deviation. Deviation keeps its instrument's glob as the kind's explicit exception.

**Left-shift gate:** Checklist classes `join-key-widened-by-a-shared-location` and C112. Add a plant with a research record named `-change-plan-2.md` that stays out of `read_changes`.

### M5 — An empty install prefix makes manifest paths absolute (finding 7)

**Where:** `tools/playbook/instructions_edit.py@4665b0d5:148` (`read_manifests`), and line 416 (`run_tag_check`'s `kit_rel`).

**What is wrong:** Both lines spell `f"{prefix}/..."`. An empty prefix is a supported layout: `WIRE-INTO-PROJECT.md` says "empty for a root install". It yields `/kitx/instructions.toml`, and `pathlib.Path(root, '/kitx/...')` discards root.

**Consequence:** Over a temp repo at prefix `''`, `read_manifests` returned `{'kitx': '/kitx/instructions.toml'}` and `read_text` returned None, while `derive_manifest_kind` still answered `kit`. A root install reads no kit manifest, so `instructions_edit.py check` prints `unarmed: the tree holds no unit row` over a tree that holds rows. Once the guard point lands, a write would target the filesystem root. No `tools/*/instructions.toml` is tracked at HEAD, so no shipped row is lost today.

**Fix (skeptic judged SOUND):** Join through one helper that drops an empty prefix, for example `'/'.join(p for p in (prefix, dir, name) if p)`, in `read_manifests` and `run_tag_check`.

**Left-shift gate:** Checklist classes `grammar-bound-to-the-wrong-root` and C37. Add a fixture with the kit at the repository top that asserts the row is read.

### M6 — An unterminated last entry turns a clean table merge into a conflict (finding 8)

**Where:** `tools/memory-tree/merge-rows.py@e826638c:1272`, with the check at line 1277.

**What is wrong:** `resolve_tables` appends `term` to an unterminated chunk at line 1272. The byte-identity check at line 1277 then compares that chunk against the unterminated side chunks and refuses it. A side that already holds the terminated form passes, so the failure is the all-unterminated case.

**Consequence:** With O, A and B ending in an unterminated `unit.c`, ours editing `unit.a` and theirs editing `unit.b`, `resolve_tables` raised `StructureDrift` with `the written chunk of unit.unit.c is byte-identical to no side's`. The same inputs with a final newline merged clean. The driver fails closed and writes both whole sides between markers, so nothing is lost. The disjoint edits still go to hand resolution, which is the outcome the table class exists to avoid.

**Fix (skeptic judged SOUND):** Compare with the terminator normalised: fold each side's chunk to end in `term` before the `text not in (...)` check, or terminate each side's last chunk in `read_tables`. The fold must keep the `None` sides from `O.get`.

**Left-shift gate:** Checklist classes `guard-above-a-fold-makes-its-fallback-dead` and C2. Add a merge-rows case with an unterminated final entry that merges clean.

### M7 — A staged rename leaves the source path in the worktree view (finding 12)

**Where:** `tools/playbook/tag_index.py@6d2d1c9d:609` (`build_overlay`).

**What is wrong:** `build_overlay` reads `git diff --name-only -z HEAD` without `--no-renames`. After `git mv OLD.md NEW.md` that prints only `NEW.md`, so no `dirty_path` row exists for `OLD.md`, and `load_view` deletes a view path only for a blob `""` row.

**Consequence:** In a scratch repo, `load_view` served both `doc.old` and `doc.new`, with `OLD.md` still in `view_path`. `gov_tag check`, the resolver and the unit grammar therefore resolve tags and citations into a file the worktree no longer has, and a dirty-tree run reads green over a dangling citation. The effect is limited to a dirty tree with a staged rename and clears once the commit lands. `tools/run-gates/owed_rows.py` in this same diff passes `--no-renames` for this reason.

**Fix (skeptic judged SOUND):** Add `--no-renames` to the diff argv, so the source arrives as a deleted path with blob `""` and takes the existing delete path.

**Left-shift gate:** Checklist classes `porcelain-diff-names-a-rename-by-its-destination` and C23. Add a fixture plant that stages a `git mv` of a doc and asserts the old tag no longer resolves.

### M8 — A warm tag index diverges from a cold one after a conf change (finding 13)

**Where:** `tools/playbook/tag_index.py@6d2d1c9d:536`.

**What is wrong:** Which extractors read a path depends on `ctx` (`CHARTER`, `MEMORY_ROOT`). Path rows are keyed only on path, blob, extractor and version, and nothing removes a row once its path stops being applicable. An uncommitted conf edit is worse: `tree_built` short-circuits at line 536 and the new `ctx` is not applied at all.

**Consequence:** In a scratch repo, committing `CHARTER=CHARTER2.md` with `AGENTS.md` unchanged left the warm index serving `doc.charter` at both files, and after deleting `index.db` it served only `CHARTER2.md`. The old file's `doc.charter#<seg>` sections keep resolving and counting as members until that file's blob changes or the index is deleted. That contradicts the module's claim that the index is purely derived. The fixture's incremental-equals-cold comparison has no conf-change plant.

**Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Take the key route only. Fold `memory_root` and `charter` into the freshness digest and the `path_row` key, bump `INDEX_SCHEMA`, filter the `parsed` lookup and `VIEW_JOIN` on that key, and make `read_live_versions` derive each worktree's digest from that worktree's own conf.

**Left-shift gate:** Add the `CHARTER` warm-equals-cold plant and an uncommitted-conf plant to the tags fixture.

### M9 — The regenerate block's `writes` omits the lock it now writes (finding 14)

**Where:** `tools/playbook/kit.toml@ea16ad85:61`.

**What is wrong:** `render_playbook.py:2445` now writes `.governance/instructions.lock` on every write-mode render, and the `[[regenerate]]` argv is that write mode. The block's `writes` still lists only `AGENTS.md`, so govkit's rollback snapshot (`_rg_set`, `govkit.py:11922-11931`) does not hold the lock.

**Consequence:** On a verify rollback, govkit restores `AGENTS.md` and leaves the lock's `blob` naming the rolled-back render. The provenance row is then false, `lock --check` reds `differs from the bytes the renderer wrote`, and govkit prints its `still differs after the rollback` line. This is read from source; the rollback was not run. `lock --check` runs only in gov's exempt leg, so in an adopter the effect is a false provenance row, not a red bar.

**Fix (skeptic judged SOUND):** Set `writes = ["AGENTS.md", ".governance/instructions.lock"]`.

**Left-shift gate:** Add a rollback arm to the govkit selftest that asserts the lock returns to its snapshot.

### M10 — Gov-only data files ship to adopters as engine (finding 15)

**Where:** `tools/playbook/kit.toml@ea16ad85:25` (`include = ["**"]`).

**What is wrong:** `govkit.py shipped` prints `positional-refs.txt` (4,461,157 bytes of `<gov path>\t<gov file>:<line>` rows), `positional-producers.txt`, `core-pending.txt` and `instructions-legacy.txt` as `playbook-render` engine files. All four are new in this diff. The run-gates descriptor in this same diff withholds gov-only `owed_rows.py` as project-owned.

**Consequence:** `gov_tag.py` and `positional.py` ship too, and `tags.positional` defaults to shrink-only. `check_positional` (`positional.py:416`) reds `listed - tree` as stale in every mode but report, so gov rows absent from an adopter tree red a hand-run `gov_tag.py check`. This is judged from source; the scratch-guard stopped the run. The `tags` leg is an `[[exempt_leg]]`, so no adopter bar shows it. Every adopter also receives 4.4 MB of another repo's citations, and each change to the list is a shipped engine-byte change. README line 289 documents the verb.

**Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Withhold the four files as project-owned, and leave `check_positional`'s absent-list red in place. Have `adopt-playbook.sh` write an empty `positional-refs.txt` and `core-pending.txt` in a target that lacks them; `gov_tag`'s fixture already calls a present, empty list unarmed.

**Left-shift gate:** Probe a scratch install running `gov_tag.py check`, and add a govkit arm that reds a `shipped` engine file holding the source repo's own paths.

### M11 — Shipped text still says the memory-tree checks need memory-recall (finding 16)

**Where:** `tools/memory-tree/HYGIENE.template.md@20846555:396`, and lines 525, 547 and 557. Also `tools/memory-tree/.memory-tree.conf.example` 306-310, `tools/memory-tree/README.md` rows 19, 23, 40, 42, 49 and 477, `manifest-check.sh:1046`, `check-wiring.sh:1379`, and `memory/HYGIENE.md` at the same lines as the template.

**What is wrong:** PLAY-dOrderedCharter-18 removed the kit's memory-recall `requires_if` rows and the runtime dependency. The code now imports this kit's own `id_grammar.py` (`corpus_ids.py:228`, `row_grammar.py:985`, `transition_audit.py:119`) and raises a refusal naming that file. The text still says "arming these checks requires that kit", and that with no memory-recall kit installed there is a named refusal. README line 40 still claims rows naming the kit, and none remain.

**Consequence:** Adopters are told to install a kit they no longer need and to expect a refusal that cannot fire. The next editor is misled about the dependency direction. No behaviour changes. Spec 18's "user docs: N/A" does not make the text true.

**Fix (skeptic judged SOUND):** Re-point each sentence to this kit's `id_grammar.py`, across every site in Where. Keep the kit-dogfood parity between the two HYGIENE copies.

**Left-shift gate:** Checklist classes `amendment-leaves-its-other-half-standing` and C63. A spec that removes a dependency greps its shipped text for the removed kit's name in the same pass.

### M12 — The `owed_rows` selftest cannot trigger its descriptor or dossier arms (finding 18)

**Where:** `tools/run-gates/owed_rows.py@e8776f14:291` (`build_fixture_repo`).

**What is wrong:** The fixture pre-claims `new leg` in `FOUNDATION.md`, and `add_leg` writes its `[[gate_leg]]` row, so `nm not in claimed` and `idx[nm] == ["UNCLAIMED"]` (lines 197-200) can never fire. The `leg added` case asserts only the pin line. Three more behaviours have no failing case: the KNOWN-copies-disagree refusal (exit 2, line 211), the `mode == 'warn'` branch (line 243), and the `deferred` line.

**Consequence:** Deleting lines 197-200 keeps `--selftest` green, and that selftest is the only check `run-gates.test.sh` arm 1a-owed runs. A broken arm would print `0 rows owed` on a pass that owes a descriptor or dossier row. Spec AC2's red condition covers those rows, though S4 and AC3 are met literally. The probe behaves correctly today (0 owed, 14 deferred and 7 warn-admitted breaches over this range), so this is a contained test gap. This was read from source; the selftest was not run.

**Fix (skeptic judged SOUND):** Add cases to `run_selftest`: a leg with no `[[gate_leg]]` or `[[exempt_leg]]` row; a leg no dossier claims (drop `new leg` from the FOUNDATION claims); two differing KNOWN lines expecting rc 2; a warn-mode breach expecting rc 0 and the count on the summary line; a missing ceiling row expecting a `deferred —` line at rc 0.

**Left-shift gate:** The cases above are the gate. Add a checklist line that a fixture must not pre-satisfy the condition its arm exists to catch.

### M13 — No arm asserts the `slot point.flow.version` lines (finding 19)

**Where:** `tools/check-install-prefix.sh@3f6bf0b3:329` and line 336; `tools/run-gates/run-gates.sh:3203` and line 3205.

**What is wrong:** These slot lines are asserted by no arm, so spec 17 AC6 (S7), red when the gate "skips without the state", is discharged by nothing that can fail. `check-install-prefix.test.sh:248` still matches only the old `SKIPPED —` text, and `run-gates.test.sh:4053` matches only `govkit is not reachable`. That arm's stub raises the inner `LookupError` after resolve, so `absent` stays False and the slot branch never runs.

**Consequence:** Deleting either slot line, or the `int(absent)` offset in `run-gates.sh`, stays green on `install-prefix self-test` and `run-gates canary`. Deleting the `out.insert` line outright would red the 4053 arm. The slot grammar S9 calls one spelling for every site can drift unseen at these two sites. The effect is contained to a printed state line, because the skip itself stays asserted.

**Fix (skeptic judged SOUND):** In `check-install-prefix.test.sh`'s no-engine arm, assert `slot point.flow.version · not-installed: `. In `run-gates.test.sh`'s unreachable-govkit arm (near line 4053), hide the kit so `LookupError` fires, then assert the slot line and that the `not reachable` line follows it. On a reachable run, assert `filled` on stderr.

**Left-shift gate:** Checklist classes `observed-by-claim-no-arm-discharges` and C84. The arms above are the gate.

### M14 — The check 37 skip path has no fixture (finding 20)

**Where:** `tools/unattended/check-unattended.test.sh@5541eadf:5845`, for the skip at `check-unattended.sh:3229` and the new branch at line 2354.

**What is wrong:** The AC6 rewrite turned the only `hit` on `check 37 SKIPPED` into a `miss`. No arm now reaches the skip, and `resolved through neither` appears in no test.

**Consequence:** When `id_grammar.py` does not resolve, check 37 must print a named skip. If a later edit makes `scan_foreign_anchors` return 0 on that branch, the unjudged folder prints `found no foreign anchor` and the suite stays green. That is a skip reading as a pass on the check that catches a second claimant for an id.

**Fix (skeptic judged SOUND):** Add an arm that removes `$_ig_dst/id_grammar.py` from the `ak` fixture and asserts `hit "check 37 SKIPPED for memory/builds/tRun"`, `hit "resolved through neither"` and `miss "found no foreign anchor"`, then restores the file. `set_ak_pristine`'s `reset --hard` restores it.

**Left-shift gate:** The arm above is the gate. Add a checklist line that a rewrite turning a `hit` into a `miss` keeps an arm that still reaches the branch.

### M15 — `check_layers` skips an unparsable core file and stays green (finding 21)

**Where:** `tools/playbook/check_layers.py@3b34575c:278`, and the `.sh` decode failure at line 316.

**What is wrong:** A core kit's `.py` file that cannot be read or parsed is skipped by a bare `continue`, with no note and no red. `NOT_READ` does not list this case. `import_walk`'s docstring says it raises so a caller can say the imports were not read, and `derive_import_closure` exits 2 on it; this caller does not.

**Consequence:** The `layer dependencies` leg certifies the core never depends on an expansion. Appending `def broken(:` to the `import` plant's fixture took it from rc 1 with 1 red to rc 0 with 0 edges and no note. Nothing else reads this population. The hole is latent: the tree's 113 core `.py` and `.sh` files all read today, and a file that does not parse is unlikely to survive its own suite.

**Fix (skeptic judged SOUND):** Collect these files and exit 2 (or a contract red) naming each one, as `derive_import_closure` does. That reds nothing today.

**Left-shift gate:** Add an `unparsable` plant to `PLANTS` and an `adopt-playbook.sh` row asserting the rc and the named file.

### M16 — Unit 45's two fail-closed postconditions have no fixture (finding 22)

**Where:** `tools/memory-tree/merge-rows.py@e826638c:1241`, and the arm at line 1277.

**What is wrong:** The `cut does not reproduce its parse` plant of AC4, and its `test.sh` twin, put an indented `  [[unit]]` after an entry. That raises at line 1232 (`is not one array-of-tables entry`), not at line 1241. Both tests match only `merge-rows failed`, so the wrong arm satisfies them. No test names the line 1277 message or plants that case.

**Consequence:** Deleting line 1241's check leaves `merge-rows.test.sh:2255` and `instructions_edit.py`'s `arm_merge_parse` green. An indented header in the preamble would then merge with the hidden entry mis-cut. The line 1277 arm is reachable: an unterminated final chunk in ours plus an add in theirs raises its message.

**Fix (skeptic judged SOUND):** Add a plant with the indented header in the preamble, plus a case where an unterminated final chunk moves mid-file. Have each assert its own message in stderr, not only `merge-rows failed`. The driver's except arm prints the exception text to stderr, so that is available.

**Left-shift gate:** The plants above are the gate. Add a checklist line that a plant asserts the message of the arm it names, never a shared failure string.

### M17 — The `gov_tag` fixture acts on the real `index.db` under an inherited `GIT_DIR` (finding 26)

**Where:** `tools/playbook/gov_tag.py@745547a3:580`, through `tag_index.read_git_stdout` (`tag_index.py:380`).

**What is wrong:** The tags fixture scrubs only its own `run_git` (`gov_tag.py:469`). `tag_index.read_git_stdout` passes no env, and `common_git_dir`, `read_git` and `load_index` all go through it. With `GIT_DIR` exported, `common_git_dir` on a scratch repo returned the outer repo's `.git`. So `remove_index` unlinks, and `run_kit_verb`'s `load_index` (line 109) writes, the outer `<common>/gov/index.db`.

**Consequence:** The finder's probe `GIT_DIR=<worktree gitdir> python gov_tag.py --fixture --plant two-versions` exited 2 and replaced the shared `index.db`. The finder reported the file holding 2 `blob_row` rows of fixture text, `tree_built` rows for the real tree 43bfbef2, and `blob_parsed` rows for only two extractors. The skeptic did not inspect the rows. It was not repaired, because spec 65 leaves `gov_tag.py` check runs to the main loop: run `python tools/playbook/gov_tag.py --rebuild` there. The freshness check keys on tree and versions digest, and the fixture's digest differs, so a real run should rebuild rather than serve fixture rows. That is read from code, not observed. Blob rows are keyed by blob, extractor and version. The consequence is a re-parse (about 35s per `ceiling-evidence.txt`), not a wrong result, and the fixture went red rather than falsely green. The path is the same narrow one as H3.

**Grade:** The finder graded this high. The skeptic re-graded it medium because the file is a derived cache, and that grade binds.

**Fix (skeptic judged SOUND):** Set `GIT_ENV_LEAKS` aside for the whole of `gov_tag`'s `--fixture` path, as `instructions_edit.run_fixture` does, so every in-process `tag_index` git call resolves the scratch repository.

**Left-shift gate:** Checklist class `inherited-git-dir-pins-the-work-tree-to-the-cwd` (C40). Add an arm asserting that a fixture run under an exported `GIT_DIR` leaves the real `index.db` bytes unchanged, run in a disposable clone.

### M18 — `core.py new instruction-unit` prints a command that cannot run (finding 27)

**Where:** `tools/playbook/core.py@eec08ad5:560`, lines 560-561.

**What is wrong:** Unit 20 S9 and AC9 say the factory prints the row and the unit-15 command that writes it. The printed command is only `python tools/playbook/instructions_edit.py add --manifest <kit>`, with no `--tag` or row fields.

**Consequence:** With AC9's arguments the factory exits 0 and prints that truncated command. Run as written, the command exits 2 with `the following arguments are required: --tag` (line 964) and writes nothing. A writer following the factory hits a usage error, and AC9's mechanism was not built. Nothing is corrupted. Separately, no tracked toml declares `point.instruction.guard`, so even a full command stops at the guard refusal (`instructions_edit.py:276`) after printing its proposal.

**Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Compose the command from the row the factory built: `--manifest`, `--tag unit.<name>`, `--type`, `--level`, `--text`, plus `--trigger always` when the type is directive, `--budget <the derived class>`, and the `--build <slug> --unit <id> --mark <editorial|semantic>` placeholders. Quote with `shlex.join`, as `render_proposal` does.

**Left-shift gate:** Extend the fixture to parse the printed command against `build_parser`, and assert that the row `propose` derives from it equals the printed row.

## LOW

### L1 — The "no recall kit" arm keeps the recall kit in place (finding 24)

**Where:** `tools/memory-tree/gotchas.py@271fa8ea:1150`, lines 1147-1153.

**What is wrong:** The arm labelled `with no recall kit, check 18 reds an undefined decision by name` calls `build_tree` and `cmd_check` in process over a corpus fixture, with `tools/memory-recall` still beside the real kit. Spec 17 AC2 and S3 call for a scratch clone with `tools/memory-recall` deleted.

**Consequence:** The label overstates what was observed. The arm shows check 18 reds an undefined id, not that it does so without the kit. If `id_grammar` or `corpus_ids` regained an import of the recall extractor, this arm would stay green. The effect is contained: the code path uses this kit's own `id_grammar.py`, and the layer leg sees a static import.

**Fix (skeptic judged SOUND):** Run the arm from a copy of the memory-tree kit with no `memory-recall` sibling (a subprocess over a scratch `tools/` tree), or rename the arm to what it does check.

**Left-shift gate:** Checklist classes `observed-by-claim-no-arm-discharges` and C84. An arm's label names only the state its setup creates.

review-shape kind=diff-review round=1 intensity=full at=synth raw=27 confirmed=23 refuted=4 unverified=0 blocker=0 high=3 medium=19 low=1 agents=11 out-tokens=290224

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/policy/catalogue.toml:34 | high | low | refuted | By design and largely pre-existing. The base catalogue already holds the same `allowed` list with `with-hooks-block`, so the diff did not make that value acceptable. Spec PLAY-dOrderedCharter-7 section 3 (Non-goals) says: 'The report-after and block-after handling of a core red a bypass let land ... dShippedRelease's lander. This unit reads core.bypass where a leg guard could skip a core check.' Its hands-off row gives dShippedRelease the job of acting on a bypassed red 'as core.bypass says'. S10 states that with-hooks-report and with-hooks-block both let a bypass skip the core legs, and only `never` acts in this unit, which is what core.py:294 does. The finder's grep is correct: no hook or shell reader exists at HEAD. That absence is the declared hand-off, and dShippedRelease's unit 13, which owns the post-landing core read, is still DEFERRED. The only thing the diff added here is the summary S12 ordered, which describes the key's designed meaning in the present tense; it does not mention the deferral. That is a wording nit, not the missing enforcement route claimed. | unsound | policy-value-with-no-route |
| 2 | security | tools/playbook/instruction_units.py:430 | medium | medium | confirmed | Read instruction_units.py:430: `subprocess.run(shlex.split(arg), ...)` has no allow-list, cwd or timeout. check_statement only requires a non-empty fact source. My probe: check_statement on `cmd:rm -rf nope` returned [], and render_unit on a `cmd:python -c` printing two lines returned '1\n2', so multi-line output passes unvalidated. Spec 9 section 5 says render_unit runs a command 'only through the source's own registered probe', and no registry exists; the code's own ponytail comment admits this for `probe:`. AC5 does require a `cmd:` source to render, so the defect is the unregistered, unbounded and wrong-cwd run, not cmd support itself. Reachability is wider than the finder says: render_unit_slots (render_playbook.py:1141) runs on any template with a slot, and resolve_template_path honours a target's `playbook_path`, so an adopter's own template plus manifest reaches it today, though gov's tracked tree has neither. The code is new in this diff. The effect is contained because a render is normally run on one's own tree, hence medium. | sound | - |
| 3 | security | tools/playbook/core.py:203 | medium | - | refuted | The code is as described: check_exceptions (core.py:187) walks reds and flags only register rows in state `red`. But this is by design. Spec 7 section 3 (Non-goals) lists 'The Loop Review's audit of the register: a later build reads `core.py exceptions`', and S9 defines `any-session-recorded` as admitting every well-formed record, with Expires optional. Spec 7's stale-row rule covers pending rows, never exception records. The claimed harm is also overstated. A later regression is not silent: it prints `excepted · <text> · by <id>` on every run. And it lands on the exact (principle, part) the record was written to excuse. Under the default, any session could write that record anew anyway, so a retained record adds no new waiver power. `core.py exceptions` already lists the whole register for the deferred audit. | sound | waiver-row-that-hides-nothing-reds |
| 4 | security | tools/unattended/unattended.sh:1424 | medium | medium | confirmed | unattended.sh:1423-1424 runs `drift_report.py --delta "$base" HEAD \|\| true`, then unconditionally echoes `slot point.runtime.reading · filled`. Spec 17's slot-line section says `searched-empty` is for a kit that ran and found nothing, and `filled` for one that returned something. The siblings honour this: unattended.sh:14976 and push-main.sh:884 both branch. In drift_report.py, derive_drift_delta returns exit 2 on an unresolved argument, and a DriftError also returns 2, so a failed read still prints `filled`. The more common path is worse than the finder states: every no-history case exits 0 printing `drift-delta: skipped — ...`, and that also prints `filled`. The test arm at unattended.test.sh:13474 checks only the moved case. The line is report-only and the close never fails on it, so the effect is contained. The fix is unsound as written because exit 0 never yields empty output: the reader always prints at least a `skipped` line, so a non-empty-output test still prints `filled` on the main miss, and a stub that only exits 1 does not cover that case. | unsound | - |
| 5 | correctness | tools/playbook/tag_index.py:265 | medium | medium | confirmed | tag_index.py:265 takes the first line containing the quoted value. practices.toml opens with `foundation = [...]`, which repeats the tags before any row. My own run of extract_practice over the shipped file: 39 rows, 36 not on a `tag =` line, for example ('practice.yagni','tag',9,9,'  "practice.yagni",'). gov_tag.py:80 and :125 and tag_index.py:725-752 serve that line, end_line and text, so show, where and bundle point at the list entry rather than the practice row. The file is new in this diff. No gate result depends on it, so the effect is contained to navigation and bundle content. The fix suits derive_tag_rows: tomllib row order matches header order, and only that function reads read_toml_tags. | sound | parser-drops-rows-it-cannot-place |
| 6 | correctness | tools/memory-tree/build_records.py:144 | medium | medium | confirmed | build_records.py:144 selects by `[^/]*-<kind>-[^/]*\.md`, while tree_lib.read_bindings reads only the exact stem and its docstring promises such research names stay bound; spec 42 S3 sets that stem rule. My probe: read_change on `.../2026-11-01-build-PLAY-dX-1-change-plan-2.md` with a research Serves line returned malformed with the file name refusal and each required field missing. read_change_records (instruction_units.py:685) then raises UnitRowError, and render_unit_slots turns that into a refusal. The `-exception-` shape reaches derive_admission's red in the core gates the same way. The shape is realistic, since spec 42 cites the tracked `-execution-return-plan-2.md` research records. It is latent: my ls-files search for tracked `-change-`, `-exception-` or `-override-` build records returned none, and it fails closed, so medium. The fix is sound: deviation keeps its glob, as S3 requires, and read_bindings still reds a mis-named record that declares a typed kind, so narrowing hides nothing. The plants I read in core.py and instruction_units.py use on-stem names. | sound | join-key-widened-by-a-shared-location |
| 7 | correctness | tools/playbook/instructions_edit.py:148 | medium | medium | confirmed | instructions_edit.py is new in this diff. Line 148 spells f"{prefix}/{dir}/instructions.toml" and line 416 spells kit_rel the same way. An empty prefix is a supported layout: WIRE-INTO-PROJECT.md says 'empty for a root install', and derive_kit_prefix's docstring says 'empty at the top'. I ran the probe with the prefix forced to '' over a temp repo holding kitx/kit.toml and kitx/instructions.toml. read_manifests returned {'kitx': '/kitx/instructions.toml', ...}, read_text returned None, and derive_manifest_kind('kitx/instructions.toml','') answered 'kit'. So a root install reads no kit manifest. Graded medium because it needs a root install holding rows, and no tools/*/instructions.toml is tracked at HEAD, so no shipped row is lost today. | sound | grammar-bound-to-the-wrong-root |
| 8 | correctness | tools/memory-tree/merge-rows.py:1272 | medium | medium | confirmed | I ran resolve_tables on O/A/B ending in an unterminated unit.c, with ours editing unit.a and theirs editing unit.b. It raised StructureDrift 'the written chunk of unit.unit.c is byte-identical to no side's'. The same inputs with a final newline merged clean. Line 1272 appends term, and the check at line 1277 compares against the unterminated side chunks. 'Can never' is slightly overstated: a side that holds the terminated form passes. The all-unterminated case is real, though, and the disjoint edits go to hand resolution. Spec 45 confirms the driver fails closed, so nothing is lost and the effect is contained. The fix must keep the None sides from O.get when it folds. | sound | guard-above-a-fold-makes-its-fallback-dead |
| 9 | correctness | tools/unattended/unattended.sh:1424 | medium | medium | confirmed | This diff added line 1424. At the base the function was just `... --delta "$base" HEAD \|\| true; return 0`. The new echo runs whatever the exit is. derive_drift_delta returns rc 2 for an unresolvable ref, and the DriftError path also returns 2, so a failed read still prints 'slot point.runtime.reading · filled'. Spec 17 S6 and S9 make the line carry the slot's state. Sibling sites key the state on the outcome: check_merge_losses maps rc 0 to searched-empty and rc 1 to filled, and write_run_record reports a non-zero exit. The effect is contained: the reader's own error also reaches stderr and the close still returns 0. The fix cures the non-zero case. A rc 0 'skipped' reading would still print filled, but that is outside this finding's claim. | sound | degradation-known-but-unreported |
| 10 | correctness | tools/playbook/render_playbook.py:2136 | low | - | refuted | The stated consequence does not hold for the finding's own examples. check_renderers (instruction_units.py:856-859) reds any table path that matches no file in INSTRUCTION_PATHSPECS. `AGENTS.override.md` is not in those pathspecs, so it reds with 'claims no instruction file', and a typo'd path reds the same way. The unscoped --check-render runs check_renderers, and gate-legs.json carries --check-render legs. So the claim that check_renderers does not see these is wrong at the bar; only the single-scope run skips it. What remains is deliberately moving an existing instruction file, such as a guide, onto the entry-files row. renderers.toml holds no such row: that row is only CLAUDE.md, which is in ALIAS_PATHS. I could not establish a reachable effect for a finding graded low. The proposed Refusal would work, because main catches Refusal around derive_entry_aliases at the scope call sites. | sound | parser-drops-rows-it-cannot-place |
| 11 | seams | tools/gate-legs.json:881 | high | high | confirmed | gate-legs.json guards are memory-recall kit selftest ['{prefix}/lib/','{prefix}/memory-recall/'], recall floor ['{prefix}/memory-recall/','memory/','.memory-tree.conf'] and recall floor arms ['{prefix}/memory-recall/','memory/','{prefix}/govkit/']. None of them covers memory-tree/id_grammar.py. The grammar sat in memory-recall/ at the base: base extract.py carries the era pattern, and recall_conf.py is imported there. Commit 2d03321ab moved it out and changed no recall guard, while bench.py, extract.py, recall_conf.py and selftest.py now import it. changed() diffs only the guard paths, and input_key hashes `git ls-files -s` over the guard alone, so an id_grammar-only edit gets a skip or a reused green. `playbook render selftest` shows the guard was added where someone thought of it. Graded high, not blocker, because the remote CI's GATE_FULL=1 run ignores guards and CI also has a held-suite plan through run-selftests.sh, so the hole is in the local scoped bar. The drift-audit part is weaker: its guard also omitted memory-recall/ at the base, so that one is pre-existing, though adding the path is harmless. The guard edit cures the skip and the reuse. The GATE_SELFTESTS=changed selection for an owned leg reads the epoch set rather than the guard, so it stays incomplete; run-gates.sh documents that as a stated ceiling bounded by the lag rule. None of the three legs has a [[gate_leg]] copy in kit.toml to keep in sync. | sound | held-suite-guard-misses-a-sibling-kit |
| 12 | seams | tools/playbook/tag_index.py:609 | medium | medium | confirmed | tag_index.py is new in this diff. In a scratch repo after `git mv OLD.md NEW.md`, `git diff --name-only -z HEAD` printed only NEW.md, and adding --no-renames printed both NEW.md and OLD.md. read_git adds no config that disables rename detection. build_overlay therefore records no dirty_path row for OLD.md, and load_view deletes a view path only for a blob "" row, so OLD.md stays in view_path from tree_path with its tags served. The sibling tools/run-gates/owed_rows.py does pass --no-renames. The effect is limited to a dirty tree with a staged rename and clears once the commit lands. With --no-renames, OLD.md arrives with is_file() False, gets blob "", and goes through the existing delete path. | sound | porcelain-diff-names-a-rename-by-its-destination |
| 13 | seams | tools/playbook/tag_index.py:536 | medium | medium | confirmed | - | unsound | - |
| 14 | seams | tools/playbook/kit.toml:61 | medium | medium | confirmed | render_playbook.py:2445 now writes .governance/instructions.lock on every write-mode render, and the [[regenerate]] argv is that write mode. kit.toml:61 still lists only AGENTS.md. govkit's _rg_set (lines 11922-11931) holds receipt rendered/generated rows plus `writes`. grep finds no lock row in govkit.py or install.json, so the lock is unsnapshotted. Rollback (12262-12278) restores only snapshotted paths, leaving the lock's blob naming the rolled-back render. check_lock would red 'differs from the bytes the renderer wrote', and the touched loop at 12288-12298 prints the 'still differs' line. The lock is tracked and not ignored. Read from source, rollback not run. `lock --check` runs only in gov's exempt leg, so in an adopter the effect is a false provenance row, not a red bar. | sound | - |
| 15 | seams | tools/playbook/kit.toml:25 | medium | medium | confirmed | `govkit.py shipped` prints positional-refs.txt (4,461,157 bytes), positional-producers.txt, core-pending.txt and instructions-legacy.txt as playbook-render engine files; all four are absent at base. The rows are gov paths. catalogue.toml defaults tags.positional to shrink-only, and check_positional (positional.py:416) reds `listed - tree` as stale in every mode except report, which only prints. So gov rows absent from an adopter tree red a hand-run `gov_tag.py check`. This is judged from source: the scratch-guard blocked running that command as a gate, and my attempt stopped there. No adopter bar shows it because the `tags` leg is an [[exempt_leg]], whose why says the resolver ships but the leg is gov's. run-gates withholds owed_rows.py as project-owned by the same mechanism, so the sibling treatment differs. The README line 289 documents the verb; I did not find a help/tags.md under tools/. | unsound | - |
| 16 | seams | tools/memory-tree/HYGIENE.template.md:396 | medium | medium | confirmed | The diff removed the memory-recall requires_if row from tools/memory-tree/kit.toml, and the code now imports this kit's own id_grammar.py: corpus_ids.py:228, row_grammar.py:985 with a refusal naming id_grammar.py, and transition_audit.py:119. Still standing are HYGIENE.template.md 396, 525, 547 and 557, .memory-tree.conf.example 306-310, README 40 and 477, manifest-check.sh:1046 and check-wiring.sh:1379, plus memory/HYGIENE.md at the same lines. README 40 claims requires_if rows naming memory-recall, and none remain. No behaviour changes, but shipped adopter text tells adopters to install a kit they no longer need and describes a refusal that no longer fires. README rows 19, 23, 42 and 49 carry the same stale claim, so the sweep should cover them too. Spec 18's 'user docs: N/A' does not make the text true. | sound | amendment-leaves-its-other-half-standing |
| 17 | verification | tools/playbook/tag_index.py:211 | high | high | confirmed | scan_unfenced is new in this diff. I re-ran the probe: it returned [(1,'intro')], while tree_lib.unfenced_lines returned [(1,'intro'),(2,None)]. Callers are extract_citations:363, extract_doc:239, positional.py:247 and instruction_units.py:643, and none can see that the document ended inside a fence. edge_grammar.py:231 and design_lib.py:371, on the shared reader, refuse the same state as 'a fence opens here and never closes'. tree_lib's docstring names this silent drop as the defect. No grep hit shows a tag plant for it. A scan of 10,457 tracked .md files found exactly one such file, the dFramedEntrypoint record open from line 717 of 977, so the path is real but narrow: the tag check goes green over text it never read. Positional file:line rows use git grep and are not affected; symbol citations and span rows are. | unsound | - |
| 18 | verification | tools/run-gates/owed_rows.py:291 | medium | medium | confirmed | Read from source; the selftest was not run, per the no-gates rule. build_fixture_repo line 291 pre-claims 'new leg' in FOUNDATION, and add_leg writes its [[gate_leg]] row, so `nm not in claimed` and `idx[nm] == ['UNCLAIMED']` can never fire in the fixture. claimant_index returns the FOUNDATION owner. The 'leg added' case asserts only the pin line, so deleting lines 197-200 keeps it green. No case has differing KNOWN copies, a warn mode (the fixture policy sets enforce = refuse), or an asserted deferred line. Spec S4 names only the pin-row plant, so the selftest meets S4 and AC3 literally, but AC2's red condition covers claim and dossier rows and no failing case proves those arms. The probe behaves correctly today, so this is a contained test gap. | sound | - |
| 19 | verification | tools/check-install-prefix.sh:329 | medium | medium | confirmed | Observed: `git grep 'slot point\.'` hits check-install-prefix.sh:329/336 and run-gates.sh:3203/3205. Neither run-gates.test.sh nor any check-install-prefix.test.sh arm asserts them. The only suite hit is the skip echo at line 45. check-install-prefix.test.sh:248 still matches only `SKIPPED — this repo is not a kit SOURCE`. run-gates.test.sh:4053 matches only the `govkit is not reachable` line, and its stub path (GOVKIT_STUB_OFF, exit 1) raises the inner LookupError after resolve, so `absent` stays False and the slot branch is never exercised. Spec 17 AC6's 'skips without the state' therefore has no arm that can fail, and §7 adds none for it. One overstatement: deleting the out.insert line outright would red the 4053 arm; only the `int(absent)` offset and the slot lines are unguarded. The effect is contained to a printed state line, since the skip itself stays asserted. | sound | observed-by-claim-no-arm-discharges |
| 20 | verification | tools/unattended/check-unattended.test.sh:5845 | medium | medium | confirmed | Observed: in check-unattended.test.sh the only mention of `check 37 SKIPPED` is the `miss` at 5850; the diff turned the former `hit` into that `miss`. `resolved through neither` appears only at check-unattended.sh:2355, the new branch, and in no test. No arm reaches the else at the check-37 site (3229), so a regression making scan_foreign_anchors return 0 there would print `found no foreign anchor` and stay green. The loss of the skip arm and the new branch are both from this diff. The fix works in the fixture: run_ak_leg runs $ak's own copy of the check with GOV_UNATTENDED_REPORT=1, _ig_dst is the only id_grammar.py beside it, and set_ak_pristine's reset --hard restores it. | sound | - |
| 21 | verification | tools/playbook/check_layers.py:278 | medium | medium | confirmed | check_layers.py is new in this diff. Lines 274-278 catch OSError, UnicodeDecodeError, SyntaxError and ValueError with a bare `continue`, and the .sh branch does the same on decode failure, with no entry in notes. Probe: the `import` plant fixture gave rc 1 with 1 red; appending `def broken(:` to the fixture's .py files gave rc 0, 0 edges and no note. NOT_READ does not list this case. import_walk's docstring and derive_import_closure treat it as exit 2. Only the delegates closure of the verdict-epoch gate calls that walk, so the layer leg's population has no such backstop. Medium because the hole is latent and a file that does not parse is unlikely to survive its own suite. Fix check: a scan of the real tree's core kits read 113 .py/.sh files with 0 unreadable, so exit 2 reds nothing today. The plant table lives at tools/playbook/adopt-playbook.sh:211, matching the fix's 'adopt-playbook row'. | sound | - |
| 22 | verification | tools/memory-tree/merge-rows.py:1241 | medium | medium | confirmed | Probe through read_tables: the AC4 plant input raises `the chunk ... is not one array-of-tables entry`, while the same indented header in the preamble raises `the cut does not reproduce tomllib's read`. With the 1241 check removed, the plant input still raises the same chunk error, so both merge-rows.test.sh:2255 and instructions_edit.py arm_merge_parse would stay green, since they match only `merge-rows failed`. The preamble input then returns clean and resolve_tables merges it with the hidden entry left in the preamble. The 1277 arm is reachable: an unterminated final chunk in ours plus an add in theirs raised `byte-identical to no side's`. No test names that message or plants that case. Fix check: the driver's except arm prints the exception text to stderr ($TMP/terr), so a per-arm message assertion is available. | sound | - |
| 23 | verification | skills/session-kickoff/manifest-check.test.sh:1450 | medium | - | refuted | By design, not a defect of this diff. Spec 17 S10 and §3 both state the fallback as the arm 'skipping with the S9 line, its assertions counted', and manifest-check.test.sh:1449-1450 does exactly that. The convention predates the diff: at base unattended.test.sh:2570 has `n=$((n+23))   # COUNTED EITHER WAY, so the floor grades this suite and not which kits sit beside it`. That states why: the floor detects arms stranded in the suite, and it must not move with which optional kits an adopter installed. Not counting would risk redding a legitimate install without memory-recall, since kickoff-manifest ships this suite. The skip is not read as coverage either: the printed line says 'its 2 assertions are counted, not run'. What remains is that the PASS total is 2 high in a no-recall tree, on an announced line. That is not an established defect. | sound | - |
| 24 | verification | tools/memory-tree/gotchas.py:1150 | low | low | confirmed | Observed at gotchas.py:1147-1153: the arm calls build_tree and cmd_check in process, with the real kit in place and tools/memory-recall still beside it. Nothing removes or hides the recall kit, yet the label says 'with no recall kit' and spec 17 AC2 and S3 call for a scratch clone with tools/memory-recall deleted. The arm therefore shows check 18 reds an undefined id, not that it does so without the kit. A regained runtime dependency on recall would stay green here. Contained: the code path currently uses this kit's own id_grammar.py, and the layer leg sees a static import. | sound | observed-by-claim-no-arm-discharges |
| 25 | intent | tools/playbook/instruction_units.py:203 | high | high | confirmed | instruction_units.run_git (line 202) passes no env, and run_fixture line 1682 calls run_git(top, "init", "-q") with no scrub. The file is new in this diff, so the defect is not pre-existing. I reproduced the mechanism in a disposable main-plus-linked-worktree repo under the scratchpad, not with the fixture itself: `GIT_DIR=<wt gitdir> git -C ladder init -q` exited 0, left ladder/ empty, and flipped the main repo's core.bare from false to true. `git status` then gave `fatal: this operation must be run in a work tree`. The sibling instructions_edit.run_fixture (lines 948-949) wraps the same call in set_env_aside(GIT_ENV_LEAKS), and pre-push lines 88-100 document this exact failure. Reach is narrow: pre-commit and pre-push unset these names, and run-gates.sh only unsets GIT_DIR in one subshell (line 370), so the `instruction units selftest` leg inherits it when the bar or the fixture starts with GIT_DIR exported. Damage is to shared config across every worktree, so high on a narrow path. The live repo now reads core.bare=false. | unsound | inherited-git-dir-pins-the-work-tree-to-the-cwd |
| 26 | intent | tools/playbook/gov_tag.py:580 | high | medium | confirmed | gov_tag.run_git (line 469) strips GIT_*, but tag_index.read_git_stdout (line 380) passes no env, and common_git_dir, read_git and load_index all go through it. gov_tag.py and tag_index.py are both new in this diff. Disposable-repo probe: with GIT_DIR exported, ti.common_git_dir(<scratch repo built with a scrubbed init>) returned the outer repo's .git. So remove_index (line 580) unlinks, and run_kit_verb's load_index (line 109) writes, the outer <common>/gov/index.db. The live index.db mtime of Nov 5 02:04 fits the finder's account; I did not inspect its rows. Severity is below the finder's high: the file is a derived cache. build_index's freshness check (tag_index.py:536) keys on (tree, versions digest), and the fixture's extractors give a different digest, so a real run rebuilds rather than being served fixture rows. blob rows are keyed by blob, extractor and version. The consequence is a re-parse (about 35s per ceiling-evidence.txt), not a wrong result. The fixture also went red (exit 2) rather than falsely green, and the path is narrow. | sound | inherited-git-dir-pins-the-work-tree-to-the-cwd |
| 27 | intent | tools/playbook/core.py:560 | medium | medium | confirmed | core.py lines 560-561 print only `instructions_edit.py add --manifest <kit>`. I ran the factory with AC9's arguments: exit 0, and that truncated command printed. I then ran the printed command as written: argparse exit 2, `the following arguments are required: --tag` (line 964), with nothing written. Spec S9 and AC9 require the unit-15 command that writes the row, so the mechanism was not built. core.py is new in this diff. A separate limit, not cited by the finder: no tracked toml declares point.instruction.guard, so even a full command currently stops at the guard refusal (instructions_edit.py:276) after printing its proposal. The effect is contained to a writer's usage error, since nothing is corrupted. | unsound | - |
