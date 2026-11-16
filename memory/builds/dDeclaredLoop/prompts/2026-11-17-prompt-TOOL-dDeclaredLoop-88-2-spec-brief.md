**Serves:** research TOOL-dDeclaredLoop-88

# Brief: revise spec TOOL-dDeclaredLoop-88 so it uses the loader unit 89 mints

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The re-ground of TOOL-dDeclaredLoop-88 (its rev-6, not yet committed) has S33 create `load_tree_lib()`
in `tools/loop/loop_lib.py` (its §8 F7). Unit 89's committed rev-5 (at 240095e82) mints the same function in its S6 and §8 F5,
and 89 builds before 88 at order 44. Two specs minting one name is a divergence waiting for the second builder.

## The brief

### Goal

Produce rev-6 of `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-88.md`, starting from the uncommitted
draft at the path the dispatcher names below, so that S33 and F7 use unit 89's `load_tree_lib()` as 89's committed spec defines it
and add only what 88 needs on top, with one revision-log line at the END of the log.

### Items

1. Start from the draft at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/pending/88-rev6-draft.md`
   (copy it over your worktree's spec file), then read unit 89's committed spec from
   `branch/unattended-declared-loop-d56bf0` through `git show`, its S6 and F5 whole.
2. Rewrite S33, its criteria, §8 F7, Files touched and the §5 sweep so 88 calls 89's loader and adds only the named
   refusals or catches 89 does not already raise; where 89 already raises one, S33 leaves it to 89. Keep F7's mark,
   `RESOLVED (agent, 2026-11-17, delegated): (<option>)`, and every other fork's.
3. The draft keeps one citation of the build method by its short name; cite it by its alias tag instead
   (`doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`).
4. Keep the unit one mechanism, its carries, its order and its DEFERRED status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Keep the
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them. Do not run the whole-tree memory
   hygiene gate, and do not ask any checker for its help text.
5. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- Only unit 89's spec mints `load_tree_lib`, every fork carries a mark, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
