**Serves:** journal TOOL-dTotalRecall-68
**Caused-by:** TOOL-dTotalRecall-68

# Brief — dTotalRecall: TOOL-dTotalRecall-68 re-grounded on the tree as built, before dispatch

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
2. Built since that brief: TOOL-dTotalRecall-55 (`5b5895a49`), -56 (`798f98fc1`) and -57 (`5ff76c2e2`: `tree_lib.py#KEPT_PATH_DOMAIN`, `read_kept_rows` raising ValueError on any row outside `memory/builds/*/build/*`) are CLOSED. -58 is CLOSED (`7fd3f8e38`, rev-4: `id_grammar.py#check_marker_domain(path, text, census)` returning `(line number, finding)` pairs, called in each build-folder walk, never in `read_kept_reason`). -60 is CLOSED (`2ec3df383`, rev-3: the split census's widened shapes; `record_causes.py --backfill --build <slug>`, the cause line behind the Serves line's lead, `check_ask_live`, the renderer's kept reason admitted for its one file; `RECORD_SCHEMA["cause_line"]` and the runlog README; its S23 govkit block cut to ride ask TOOL-dTotalRecall-109). -65 (order 31, spec rev-5, the `CENSUS_KEPT_PATHS` rows moved into `memory/project/census-kept-paths.txt`, `read_kept_rows` and `read_kept_path` taking `root`, the `kept` arguments gone) builds now: take its spec as what lands, and read its commit if it lands first. The run is on node a. Each unit of an order is re-grounded by its own writer: edit no other unit's spec, and name in your return any edge you need from one.
3. Notes from the main loop, each to verify against the tree before folding. The registration's place is
   `tools/govkit/registry.toml`, never the shipped `tools/memory-tree/kit.toml`, and a `[[ledger]]` home stays under
   `memory/project/`. Unit 65 rev-5 names the registry, its grammar, its reader's `root`, the domain refusal and the
   malformed-row red: bind to that spec. The factory accepts `seed = []` and a `home` (unit 65's writer read it); read
   `tools/lib/legacy_ledger.py` and the ratchet at HEAD yourself. Unit 66 (same order) is being re-grounded now by its
   own writer.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-68` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-68. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-68.md` alone. Temporary files go under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/68/`, spelled absolute. Do not commit: the main loop commits the re-ground. Each command is bounded, and a
command that runs past two minutes is run in the background and waited for, never polled.

### Reuse

The spec's §10 seam, re-verified at HEAD.
