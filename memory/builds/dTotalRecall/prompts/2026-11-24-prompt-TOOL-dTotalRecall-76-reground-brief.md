**Serves:** journal TOOL-dTotalRecall-76
**Caused-by:** TOOL-dTotalRecall-76

# Brief — dTotalRecall: TOOL-dTotalRecall-76 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem,
so a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read `memory/builds/dTotalRecall/prompts/2026-11-24-prompt-TOOL-dTotalRecall-76-reground-brief.md` whole: its Notes section is part of this task.
2. Apply items 1 to 6 of `memory/builds/dTotalRecall/prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-reground-brief.md` to this spec, reading them
   whole, with this spec's id and path for that one's.
3. Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-76`,
   `python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/positional.py check` over the spec, and
   fix every finding naming it, save a `stale` row the main loop shrinks. Every number carries an id, a path:line,
   PINNED or DERIVED on its line, and no code line is cited bare as a file, a colon and a number.

### Acceptance

The commands name no finding of the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-76. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-76.md` alone. Temporary files go under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/76/`, spelled absolute. Do not commit: the main loop commits the re-ground. Each command is bounded, and a
command that runs past two minutes is run in the background and waited for, never polled.

### Reuse

The spec's §10 seam, re-verified at HEAD.

## Notes

Built since the brief of unit 58: TOOL-dTotalRecall-55 to -58, -60 (`2ec3df383`, red-fix `cb0e30d2e`), -65 (`f1e11ac49`: the keep rows in `memory/project/census-kept-paths.txt`, the kickoff manifest re-stamped, deviation 1012), -68 (`7252440fd`: the `census-kept-paths` registration in `tools/govkit/registry.toml` alone, `tree_lib.py#read_kept_rows` through `legacy_ledger.read_rows`, `record_kinds.py#write_kept_fixture`; no `compare_to_base`, no plant `kept-row-gained`) and -66 (`17aac82e4`: the drain reds in both build-folder walks, `build_kept_path_re`, `read_pinned_rows` over a row's `records` glob, `CAUSE_WRITER_PINNED` gone, `write_fixture(top, plant, memory="memory")`) are CLOSED. Building in order, each at the spec revision named: -69 (rev-3), -70 (rev-4: S21 cut, S14 writes a deviation record naming pass(64) and unit 38's untaken hand-off), -73 (rev-3: `resolve_kept_home(root)`, `check_kept_home(root)`; `resolve_kept_registration` is not minted), -75 (rev-3: the manifest's `last-body-change` advanced unconditionally), -74 (rev-3: `s1-59` count 1 at `206422580`, `s1-46` count 0 at `254057fa6`, no unit-59 deviation record owed) and -87 (rev-3: `resolve_memory_root(conf)`, a repo-relative string or a ValueError; `run_cause_writers(root)`). Take their specs as what lands, and read each commit that lands first. The run is on node a. Each unit of an order is re-grounded by its own writer: edit no other unit's spec, and name in your return any edge you need from one.

From the earlier writers, each to verify before folding. Order 35 is units 76, 83 and 84.
- Ids 6, 21 and 27 (S10, S15, S16) name a plant and a compare that unit 68 rev-3 does not build. S13's tracked
  `kit.toml` registration has no reader that needs it. The seven registry plants and `pinned-ask-is-spec` keep their
  names (unit 66). S23's Readers clause calls `CAUSE_WRITER_PINNED` absent at base: it is now retired at HEAD.
- It cites `resolve_kept_registration`, never minted: units 73 and 87 mint `resolve_kept_home`, `check_kept_home` and
  `resolve_memory_root`.
- S7 and AC3 expect pass(64) to change unit 38's spec; it changed nothing there, and unit 70's S14 record names that.
  S5 and S6's blob probe is spelled in unit 70 rev-4 section 4.
- AC12 and S19 read `fail 5` and `fail 9` text the checker never prints: it prints `MANIFEST check 9 FAILED`. Unit 69's
  AC1 pair and stamp: unit 65's own commit stamped, so a parent read shows no C5 red.
- Any item reading the checker's exit status runs a leg a role agent may not: make it a probe, or name it as the main
  loop's to run.

`packet.py --check dTotalRecall` runs past ten minutes on node a: spell `python tools/chain-packet.py --check
dTotalRecall`, the instrument's own `main` and bytes (TOOL-aBatchedPacket-1), where a criterion needs it. A role agent
may run no gate leg's own command, so a criterion is a probe. The held units (TOOL-dTotalRecall-8, -37, -14, -15, -26)
build nothing: an item that needs one is cut to what HEAD can observe and named in your return. Keep every S and AC,
each built, re-observed, or cut with its reason.
