**Serves:** journal TOOL-dTotalRecall-73
**Caused-by:** TOOL-dTotalRecall-73

# Brief — dTotalRecall: TOOL-dTotalRecall-73 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem,
so a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read `memory/builds/dTotalRecall/prompts/2026-11-24-prompt-TOOL-dTotalRecall-73-reground-brief.md` whole: its Notes section is part of this task.
2. Apply items 1 to 6 of `memory/builds/dTotalRecall/prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-reground-brief.md` to this spec, reading them
   whole, with this spec's id and path for that one's.
3. Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-73`,
   `python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/positional.py check` over the spec, and
   fix every finding naming it, save a `stale` row the main loop shrinks. Every number carries an id, a path:line,
   PINNED or DERIVED on its line, and no code line is cited bare as a file, a colon and a number.

### Acceptance

The commands name no finding of the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-73. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-73.md` alone. Temporary files go under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/73/`, spelled absolute. Do not commit: the main loop commits the re-ground. Each command is bounded, and a
command that runs past two minutes is run in the background and waited for, never polled.

### Reuse

The spec's §10 seam, re-verified at HEAD.

## Notes

Built since the brief of unit 58: TOOL-dTotalRecall-55 (`5b5895a49`), -56 (`798f98fc1`), -57 (`5ff76c2e2`), -58 (`7fd3f8e38`, rev-4: `id_grammar.py#check_marker_domain(path, text, census)`, called in each build-folder walk), -60 (`2ec3df383`, rev-3, red-fix `cb0e30d2e`: the split census's widened shapes; `record_causes.py --backfill --build <slug>`, `check_ask_live`, the renderer's kept reason admitted for its one file; `RECORD_SCHEMA["cause_line"]`; its S23 govkit block cut to ride ask TOOL-dTotalRecall-109) and -65 (`f1e11ac49`, rev-5: the keep rows in `memory/project/census-kept-paths.txt`, `tree_lib.py#read_kept_rows(census, root)` and `read_kept_path(census, path, root)`, the `kept` arguments and `CENSUS_KEPT_PATHS` gone, the kickoff manifest re-stamped in that commit, deviation 1012) are CLOSED. -68 (rev-3: the `census-kept-paths` registration in `tools/govkit/registry.toml` alone, rows in the factory grammar read by `legacy_ledger.read_rows`; no `compare_to_base` in `record_causes.py`, no plant `kept-row-gained`) builds now, then -66 (rev-5) and -69 (rev-3): take their specs as what lands, and read each commit that lands first. The run is on node a. Each unit of an order is re-grounded by its own writer: edit no other unit's spec, and name in your return any edge you need from one.

From the main loop and the order-32 writers, each to verify before folding. Order 33 is units 70, 73 and 75.
- Unit 68 rev-3 puts the registration in gov's `tools/govkit/registry.toml` alone, so an adopter holds no registration:
  a red on an absent registration (S1) would red every adopter. S3's `--check` compare is not built (unit 68 section 8
  F2: the landed leg `ratchet (never gains)` grades every registration). What remains is joining the reader's path to
  the registered home, under the conf's memory root. Decide by M3 what is left to build, and where nothing is, say so.
- TOOL-dTotalRecall-87 (order 34) resolves the memory root `resolve_kept_registration` joins: name what it can expect.

`packet.py --check dTotalRecall` runs past ten minutes on node a: spell `python tools/chain-packet.py --check
dTotalRecall`, the instrument's own `main` and bytes (TOOL-aBatchedPacket-1), where a criterion needs it. A role agent
may run no gate leg's own command, so a criterion is a probe. The held units (TOOL-dTotalRecall-8, -37, -14, -15, -26)
build nothing: an item that needs one is cut to what HEAD can observe and named in your return. Keep every S and AC,
each built, re-observed, or cut with its reason.
