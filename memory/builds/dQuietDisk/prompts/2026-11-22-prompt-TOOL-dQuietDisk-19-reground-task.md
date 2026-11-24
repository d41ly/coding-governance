**Serves:** research TOOL-dQuietDisk-19

# Spec task — dQuietDisk: re-ground order 7 on the built orders 1 to 6

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read the spec brief first,
`memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`. Its rules bind this task.

## The base

Every product unit is terminal. CLOSED: 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 26 and 28. WONTDO: 6 (its
F1 (b)) and 17 (its F2 (c)). DEFERRED: 15 (its F1 (c), ask TOOL-dQuietDisk-33). The last product pass is
TOOL-dQuietDisk-9 (`525d33285`). Your spec was last grounded at `b3f5a2bc`. Its B0 readings are already committed in
`memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-19-measurements.md`.

## Re-ground TOOL-dQuietDisk-19

- **Re-check every code fact** at `HEAD`, and re-cite each moved one by symbol or as `<path>@<blob>:<line>`: the three
  leg argvs in `tools/gate-legs.json`, the pass-order leg's remote and range reading, and the role and guard rows that
  keep M1 and M3 with the main loop.
- **Name the switches as built.** S3's A-off holds "every switch this build added" at its today value. Read each built
  unit and list the switches that exist at `HEAD`, each with its exact key, today's value, its default and the subjects
  it governs. At least TOOL-dQuietDisk-1's history verdict store and TOOL-dQuietDisk-7's `tests.fixture-templates`
  (read through `read_template_mode`) are candidates; confirm each by reading the code, and say for every other unit
  that it added no switch. A switch that a single environment variable cannot hold for one measured command takes the
  `not taken` cell your spec already describes.
- **Correct the edges and limits to what was built:**
  - TOOL-dQuietDisk-10 added no switch (its F3 (a)): its M1 saving shows between B0 and A, as for units 9 and 26, not
    between A-off and A-on.
  - TOOL-dQuietDisk-6 and TOOL-dQuietDisk-17 are WONTDO: they own no saving and their rows say so.
  - TOOL-dQuietDisk-26 lists the tree once per `check-wiring.sh` invocation, a saving inside M1.
  - TOOL-dQuietDisk-11's saving is inside M3; TOOL-dQuietDisk-9 changes where M1 and M3 put their scratch, so state
    whether the instrument's temp counters still see it, and how.
- **The instrument stays byte for byte** as S1 carries it, unless a built unit makes a reading impossible; if so, name
  it in section 8 as a fork.
- **Check every git command, flag and shell idiom against the real tool** before the spec relies on it. This build has
  already ruled on these false facts: `git rev-parse --short` takes a single revision; a local `git clone --shared`
  spawns two processes; an MSYS shell rewrites a `!/path` argument; `git hash-object --stdin-paths` and an alternates
  line both refuse an MSYS `/c/...` path.
- **Record the re-ground.** Set the header's base to the `HEAD` you read at, bump the rev and add a revision-log line:
  `re-grounded at <sha> (orders 1 to 6 built), <what moved>`.

Nothing in the unit's goal moves. Where the re-ground changes scope or acceptance, say why in the revision-log line.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-19`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Run `python tools/playbook/writing_practice.py check pinned-facts` and fix any red in your spec.
- Mark every figure you add PINNED, DERIVED or with an id on its own line. A section number before a noun reads as a
  count, so word around it.

Return: the new rev, what moved, the switch table (unit, key, today's value, default, subjects), and any fork.
