**Serves:** journal TOOL-dTotalRecall-65
**Caused-by:** TOOL-dTotalRecall-65

# Brief — dTotalRecall: TOOL-dTotalRecall-65 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem,
so a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Apply items 1 to 6 of `memory/builds/dTotalRecall/prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-reground-brief.md` to this spec. Read them
   whole; they bind here, with this spec's id and path for that one's, and its built-so-far list holds.
2. Built since that brief: TOOL-dTotalRecall-55 (`5b5895a49`: `tree_lib.py#CENSUS_KEPT_PATHS` and its one reader `read_kept_rows(census, table=CENSUS_KEPT_PATHS)`, `CAUSE_WRITER_KEPT` retired), -56 (`798f98fc1`: the alias census keeps by `read_kept_path("check_alias_compares", path)`, `ALIAS_COMPARE_KEPT` retired) and -57 (`5ff76c2e2`: `tree_lib.py#KEPT_PATH_DOMAIN`, `read_kept_rows` raising ValueError on any row outside `memory/builds/*/build/*`, `check_alias_compares` taking `kept`) are CLOSED. -58 (rev-3, the census marker refused in a build folder by a new `id_grammar.py#check_marker_domain` in each build-folder walk, never in `read_kept_reason`) is building now; read its commit when it lands. The run moved to node a on 2026-11-23. Each unit of an order is re-grounded by its own writer: edit no other unit's spec, and name in your return any edge you need from one.
3. Notes from the main loop, each to verify against the tree before folding. Units 55 and 57 built the table as
   `tree_lib.py#CENSUS_KEPT_PATHS` with the reader `read_kept_rows(census, table=CENSUS_KEPT_PATHS)`, `read_kept_path`
   answering through it, the `kept` argument of `check_cause_writers`, `run_check` and `check_alias_compares` (None
   reads the table), and `KEPT_PATH_DOMAIN`'s refusal inside `read_kept_rows`. Re-point the `table` default, the `kept`
   arguments and the plant `kept-row-editable` (unit 57, its arm in `tools/memory-tree/check-memory-hygiene.test.sh`)
   when the rows move into the project registry, and re-derive the row count and every reader with a command.
   Unit 60 builds before this one at order 31 and is being re-grounded now by its own writer; its S26 grades the
   reasons this unit moves.
4. A registry under `memory/project/` joins `PROJECT_REGISTRY_EXTRA` in `.memory-tree.conf`, a `watch:` file of the
   kickoff manifest; TOOL-dTotalRecall-69 re-stamps it. Check how hygiene check 3 and any `[[ledger]]` population rule
   read a new file there at HEAD, and whether TOOL-dTotalRecall-68 (registering it as a `[[ledger]]` population through
   `tools/govkit/registry.toml`) still fits what you state.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-65` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-65. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-65.md` alone. Temporary files go under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/65/`, spelled absolute. Do not commit: the main loop commits the re-ground. Each command is bounded, and a
command that runs past two minutes is run in the background and waited for, never polled.

### Reuse

The spec's §10 seam, re-verified at HEAD.
