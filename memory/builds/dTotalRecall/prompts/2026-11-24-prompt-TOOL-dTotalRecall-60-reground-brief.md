**Serves:** journal TOOL-dTotalRecall-60
**Caused-by:** TOOL-dTotalRecall-60

# Brief — dTotalRecall: TOOL-dTotalRecall-60 re-grounded on the tree as built, before dispatch

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
3. Notes from the main loop, each to verify against the tree before folding. S7 to S9 are a re-check only: unit 45
   rev-3 landed the keyword-only slug of `render_spec_skeleton`. S12 and AC12 replace unit 47's AC2, whose premise
   moved. S17's site count is unit 44 rev-3's, with `derive_run_kind` listed apart. S21 and S25 were done by unit 48
   rev-3 (rewrite each as a re-observation, its criterion kept as the check); unit 48 left the runlog README head and
   its `RECORD_SCHEMA` cause key to this unit (S30, S31). S33 names `tools/lib/resolve-python.test.sh`, not
   `legacy_ledger.py`. The edge to unit 53 names S20's govkit lines, which now ride with held unit TOOL-dTotalRecall-37
   (ask TOOL-dTotalRecall-109): decide S23 over what HEAD holds, and where its four renders do not exist, say so.
   S5 and S6: unit 52 rev-7 retired `legacy-records` for `record-kinds-legacy` with no `absorbs`, and unit 59 built
   what it built; the items observe HEAD. S19's `pinned-ask-closed`, S20's prefix and S24's shapes are over the code
   units 44, 47, 51 and 53 landed. Re-derive every line citation, `tree_lib.py`, `gen_build_index.py`, `backlog.py`
   and `govkit.py` ones included, as `path#symbol`.
4. The held units (TOOL-dTotalRecall-8, -37, -14, -15, -26) build nothing: an item that needs one of them is cut to
   what HEAD can observe, named in your return, and the rest named as riding that unit's ask. This spec's items
   number 35: keep every S and AC, each either built, re-observed, or cut with its reason.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-60` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-60. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-60.md` alone. Temporary files go under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/60/`, spelled absolute. Do not commit: the main loop commits the re-ground. Each command is bounded, and a
command that runs past two minutes is run in the background and waited for, never polled.

### Reuse

The spec's §10 seam, re-verified at HEAD.
