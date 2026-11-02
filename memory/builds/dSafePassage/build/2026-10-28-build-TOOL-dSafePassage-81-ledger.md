**Serves:** journal TOOL-dSafePassage-81

# TOOL-dSafePassage-81 — acceptance ledger

The unit as built, at spec rev-4, over the pass's parent `17c1a89b1`, the last of order 16. The pass
opened by re-running §4's join with `60d90cb71` and its own base. It read 1212 offenders at the base
and 1289 at the head. That is 82 pairs new at the head, all in files this build changed, and 5 gone:
§4's four moved pairs and `make_target`. The 82 are §4's 70, the 4 moved pairs, and 8 the order-16
siblings added after `83817478f`, in `tools/govkit/selftest.py`, nested in `check_upgrade_steps`
(TOOL-dSafePassage-72), and in `tools/govkit/upgrade_walk.py`, nested in `check_graders`
(TOOL-dSafePassage-77). S5 renames those eight by S1's rule and F2's:

| Old | New | Verdict | Why |
|---|---|---|---|
| `plant_image72` | `write_image72` | UNRULED | writes a step's before-image file |
| `plant_link72` | `write_link72` | UNRULED | makes a junction or symlink on disk |
| `make_repo` | `build_repo` | DEBT | `--suggest make_repo` answers `build_repo` |
| `grade_order_kind`, `grade_arm_needle`, `grade_tree_clean`, `grade_case_counts`, `grade_fixture_keys` | `check_grade_order_kind` and the same `check_grade_` prefix on each of the other four | UNRULED | each is a grader that returns a red line; `check_tree_clean` and `check_arm_caught` are already module bindings, so the leading `check_` keeps the grader's own stem |

The §4 table's 70 rows were renamed to the targets it gives. Line numbers had drifted, so each was
found by its scope and name. Every rename is a scope-local substitution by AST position: the
definition and each `ast.Name` load that resolves to it. The script stops on any store, any rebinding
in a nested scope, or a target already bound in the scope or at module top. None fired. S3's literals
were moved: the nine of §4 "Readers by content", the two arm labels that name `submodule_paths`, and the
`_rb_finish` comment in `tools/govkit/govkit.py`. A second sweep compared the string constants of
every tracked `.py` under `tools/` and `.githooks/` against the renamed files at `17c1a89b1`. It
found no constant that was a substring of a renamed file there and is not one now, so no
`src.replace` or `src.count` anchor broke.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. On node a (Windows 11, Git
Bash), by the spec's own probes over this worktree's working copy. The base list came from a
`git clone --shared` at `60d90cb71` under `%TEMP%/lx81b`.

**Evidences:** TOOL-dSafePassage-81
- AC1 — §4's join over `python tools/lexicon/lexicon.py --list` at `60d90cb71` and at the pass tree printed `base 1212 head 1211`, no `UNCHANGED` line, and only the four `CHANGED` pairs of §4 "Moved, not introduced": `blob_at`, `demand_safe_token`, `sub` and `target_context` in `tools/govkit/upgrade_steps.py`.
- AC2 — `python tools/lexicon/lexicon.py --suggest <target> --as py.function` over the 66 distinct Python targets, the 70 rows' plus the eight above, gave 66 lines beginning `OK —` and 0 others. `--as sh.function` for `measure37` and `measure_raw37` printed `OK —` for each.
- AC3 — the symtable probe, with `tools/govkit/upgrade_walk.py` added to its file list, printed nothing. The `git grep -nwE '_rb_finish|submodule_paths|…|count37|raw37' -- tools .githooks skills help`, with the eight sibling names added, printed 0 lines. Staged red on a scratch copy of `tools/govkit/upgrade_steps.py` with only the definition of `write_lock_plant` turned back to `plant_lock`, the probe printed `run_lock_fixture write_lock_plant`.
- AC4 — `grep -cF -- '<literal>' tools/govkit/selftest.py` printed each "Becomes" literal's Count, 1 each and 2 for `n.name == "read_submodule_paths"`, and 0 for each "Literal at the head". `grep -c 'check_ok(rep.get("count") == str(rep.get("pairs"))' tools/govkit/upgrade_steps.py` printed 1.
- AC5 — `grep -cwE 'count37|raw37' tools/push-main.test.sh` printed 0 and `grep -cwE 'measure37|measure_raw37' tools/push-main.test.sh` printed 5. `bash -n` over the file exits 0.
- AC6 — a `python` one-liner over `memory/map/generated/symbols.json` found `remove_arm_dir` and `write` for `tools/govkit/fixtures/release-0/arms/arm_step.py`, and `measure37` and `measure_raw37` among the `tools/push-main.test.sh` entries, with none of `put`, `clear`, `count37` or `raw37`. `python tools/codebase-map/gen_map.py --check` exited 0 after `--write`, which rewrote `symbols.json` alone.
- AC7 — `python tools/lexicon/lexicon.py --check` exited 0 and printed `P1 verb   graded=7246 offenders=1211`, with no `over pin` and no `UNDER pin` line. `VERB_OFFENDER_PIN` reads `1211`, the value `--measure` printed.
- AC8 — `python tools/lexicon/lexicon.py --check` exited 0 at `offenders=1211`, and `grep -n VERB_OFFENDER_PIN .lexicon.conf` prints `VERB_OFFENDER_PIN="1211"`. `git diff -U0` over `.lexicon.conf` shows one hunk: the pin line and the added `# RE-MEASURED 1211 at TOOL-dSafePassage-81` block above it. OWED to the main loop at the close: `bash tools/lexicon/adopt-lexicon.sh --check`, the `lexicon wiring` leg's own command, which scratch-guard row G1 refuses a role agent.

OWED AT THE CLOSE: AC8's `adopt-lexicon.sh --check` run, and the legs of §7. Among them are
`push-main self-test`, `upgrade-walk` and `govkit selftest`, the suites that run the renamed
helpers. The unit adds no `New arm:` line.
