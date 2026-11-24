**Serves:** journal TOOL-dTotalRecall-77
**Caused-by:** TOOL-dTotalRecall-77

# Brief — dTotalRecall: TOOL-dTotalRecall-77 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem,
so a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read `memory/builds/dTotalRecall/prompts/2026-11-24-prompt-TOOL-dTotalRecall-77-reground-brief.md` whole: its Notes section is part of this task.
2. Apply items 1 to 6 of `memory/builds/dTotalRecall/prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-reground-brief.md` to this spec, reading them
   whole, with this spec's id and path for that one's.
3. Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-77`,
   `python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/positional.py check` over the spec, and
   fix every finding naming it, save a `stale` row the main loop shrinks. Every number carries an id, a path:line,
   PINNED or DERIVED on its line, and no code line is cited bare as a file, a colon and a number.

### Acceptance

The commands name no finding of the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-77. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-77.md` alone. Temporary files go under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/77/`, spelled absolute. Do not commit: the main loop commits the re-ground. Each command is bounded, and a
command that runs past two minutes is run in the background and waited for, never polled.

### Reuse

The spec's §10 seam, re-verified at HEAD.

## Notes

Built since the brief of unit 58: TOOL-dTotalRecall-55 to -58, -60, -65 (`f1e11ac49`, the kickoff manifest re-stamped, deviation 1012), -68 (`7252440fd`: the `census-kept-paths` registration in `tools/govkit/registry.toml` alone, `read_kept_rows` through `legacy_ledger.read_rows`), -66 (`17aac82e4`: the drain reds, `build_kept_path_re`, `read_pinned_rows`, `CAUSE_WRITER_PINNED` gone), -69 (`f7011dd6f`: nothing stamped) and -70 (`408d05723`: `KEPT_CENSUSES`, two refusals in `read_kept_rows`, check 3 admits `census-kept-paths.txt`, the manifest re-stamped, deviation 1013 of unit 38) are CLOSED. Building in order, each at the spec revision named: -73 (rev-3: `resolve_kept_home(root)`, `check_kept_home(root)`; no `resolve_kept_registration`), -75 (rev-3), -74 (rev-3: `s1-59` count 1 at `206422580`, `s1-46` count 0 at `254057fa6`, no unit-59 record owed), -87 (rev-3: `resolve_memory_root(conf)`, `run_cause_writers(root)`), -76 (rev-4: the sweep is the main loop's; S16's `reads` key moves to `never-gains`, `seed-laundering` and `rename`; plants `kept-row-gained` and `kept-base-unresolved` cut), -83 (rev-4: no unit 59 record) and -84 (rev-3). Take their specs as what lands, and read each commit that lands first. The run is on node a. Each unit of an order is re-grounded by its own writer: edit no other unit's spec, and name in your return any edge you need from one.

From the earlier writers, each to verify before folding. Order 36 is units 77, 78, 79, 80, 85, 86 and 90.
- Unit 76 rev-4 moved its S19 sweep to the main loop: it runs `skills/session-kickoff/manifest-check.sh` in one scratch
  clone at each pass commit, prints each run's status and each `MANIFEST check` failure line the checker prints, and a
  staged `live` red; it no longer greps `fail 5` or `fail 9`, which the checker never prints. Its output is written into
  unit 76's build brief and its ledger. The stamps are bundled, one per pass that edits a watched path, so unit 69
  stamped nothing and its AC1 is answered by unit 76 S20.
- A role agent may not run the checker: what must run it is the main loop's, in the background before the dispatch, its
  output handed in the brief. Where the earlier sweep already answers this unit's question, cut the second run by M3 and
  say what the ledger records in its place.
- This unit's reader (`read_checker`) and unit 76's share their line shapes; read unit 76 section 4.

`packet.py --check dTotalRecall` runs past ten minutes on node a: spell `python tools/chain-packet.py --check
dTotalRecall`, the instrument's own `main` and bytes (TOOL-aBatchedPacket-1), where a criterion needs it. A role agent
may run no gate leg's own command, so a criterion is a probe. The held units (TOOL-dTotalRecall-8, -37, -14, -15, -26)
build nothing: an item that needs one is cut to what HEAD can observe and named in your return. Keep every S and AC,
each built, re-observed, or cut with its reason.
