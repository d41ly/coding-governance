**Serves:** journal TOOL-dTotalRecall-6

# TOOL-dTotalRecall-6 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `803a3b802` from [2026-11-22-prompt-TOOL-dTotalRecall-6-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-6-build-brief.md), recorded whole; the pass tip is `ce198f660`.

## Why

TOOL-dTotalRecall-6 was built from spec rev-4 and committed as one pass commit. The commit carries `Pass: TOOL-dTotalRecall-6` and the spec header set to CLOSED, and its hooks passed. Before building I checked the spec against the tree and found nothing that blocked building it as written. One base observation is incomplete: AC10's grep at base also matches `derive_front_matter`'s own `fm.get("parents"` split, which the criterion does not mention. S3 already covers that change, so it is recorded in deviation 63 and not treated as a divergence.

## Summary

Built and committed TOOL-dTotalRecall-6 as ce198f660 on branch/unattended-dtotalrecall-ae256e, starting from 803a3b802. No gate, suite or `--selftest` was run in this pass; the arms and gates it owes are listed at the end.

**What changed**
- `tools/playbook/edges.toml`: a new `[[front-matter]]` table with six rows. `depends-on` and `parents` both map to the `after` type. `implements`, `amends` and `supersedes` now accept a build as source, and `patches` accepts a family id as target.
- `tools/memory-tree/gen_build_index.py`: the seven functions the spec lists (`read_relation_rows`, `parse_relations`, `derive_relation_inverses`, `check_relation_cycles`, `read_build_refs`, `resolve_relation_target`, `cmd_print_relations`) and the new `--print-relations` mode.
  - `collect`'s `parents` field now holds the `after` targets, and `derive_front_matter` reads them.
  - `plan()` refuses a `depends-on` cycle and a red target. A target outside the tree is now pending instead of refused.
  - `render_edges` writes one line per relation type and per inverse. Today's tree, which uses `parents:` only, renders byte-identically.
- Loop kit: the three `parents:` readers in `budget.py`, `loop_parents.py` and `position.py` now go through `parse_relations`. `loop_parents.py` gains the `depends-on-parent` plant and selftest case.
- `tools/unattended/unattended.sh`: `verb_plan` reads `depends-on:` as well as `parents:`.
- Docs: `help/loop.md`, `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md` name `depends-on:`.
- Selftest arms in `gen_build_index.py`, all written but not run here:
  - a new `test_relations` with arms for AC2, AC3, AC5, AC6, AC7 and AC8;
  - the `tGhost` arm turned into the found-nowhere arms;
  - the two TOOL-aTrimmedWait-8 AC3 arms now stage the `parents:` plus `depends-on:` pair.
- Records:
  - Deviation 62 replaces deviation 61, which named `amends.to` where the rows needed `supersedes.from`.
  - Deviation 63 lists the extra names, fallbacks and messages the build added beyond the spec's inventory.
  - The acceptance ledger has one line per criterion.
  - `symbols.json` was regenerated. The derived indexes (`LIVE.md`, `TOOL.md`, the build README, the dClosedLoop as-built view) are committed as the generator rewrote them.

**Checks run (probes of this unit's own code)**
- **AC9:** a `tomllib` read of `edges.toml` found the six rows, both alias keys typed `after`, and the widened lists. It stands in for the `edges` leg.
- **AC2 to AC8:** run through the generator's `--write`, `--print-relations` and `--check` on scratch fixture repos under `%TEMP%`, each matching its criterion. The AC2, AC3, AC7 and AC8 trees were also run against a clone of the base, and each failed there as the spec predicts. These stand in for the `build-index selftest` leg.
- **AC10:**
  - the `depends-on-parent` plant printed the same route line as `withdrawn-parent`;
  - the position engine's `parent-unlanded` and the budget's `patch-draw` plants answered as before;
  - the AC10 grep now prints nothing.
  
  These stand in for the `loop parent routes`, `loop position fixtures` and `loop budget fixtures` legs.
- **AC11:** the greps found `depends-on:` where required, and `docs_leg.py --fingerprints` showed no usage fingerprint moved. Stands in for the `docs` leg.
- **AC12:** in a scratch clone with the README's `parents:` line respelled `depends-on:`, `--plan` printed the three `parent` lines; the base driver printed none.
- **Other probes:**
  - `id_grammar.py --readers` lists no line in `gen_build_index.py`;
  - the naming lexicon accepted every new function and helper name;
  - the pre-commit memory-hygiene leg passed on the second attempt, after I reworded a literal markdown link in the ledger.

**Owed to the close (main loop)**
- AC1's `--write` in a scratch clone of the pass tip.
- Every leg listed in spec §7.
- The RED-first observation of both `New arm:` entries:
  - the `gen_build_index` arms, staged by restoring the folder-only `parents:` check in `plan()`;
  - `loop_parents`'s `depends-on-parent` case, staged by restoring the `fm.get("parents")` split.

**For the main loop to decide**
- **Refused dispatch:** a `--dispatch` declaring the four derived index paths was refused by check 49. The cause was a spec-token red in TOOL-dTotalRecall-2's uncommitted working-tree edit, made by another session, not by this unit. The same run's output said `--check-commit` accepts generated outputs undeclared, so I committed them without the declaration. The commit-message hook accepted it, and a `Decided:` trailer records this.
- **Other units' rows left unstaged:** the build README rows for units 22, 3, 2 and 7 still have unstaged changes, because the render read those specs' uncommitted revisions from the other session.
- **Ask TOOL-dTotalRecall-31:** it was deferred until this unit and now reads OPEN. Its acceptance (the README-site table in `edges.toml`) is met at this commit, but this spec names no `closes`, so I left it for you to dispose.
- **Untested refusal paths:** the bug-class checklist ran (it exited 0). It flagged that three new refusal paths have no test arm, and the spec did not ask for one:
  - a relation key used with no playbook kit installed;
  - a malformed `[[front-matter]]` row;
  - a slug that fails the grammar in `read_build_refs`.

No command timed out or was skipped.
