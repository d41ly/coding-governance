**Serves:** research PLAY-dClosedLoop-1

# Instruments: the packet instrument's plants and acceptance (Phase 0, P0.3 with P0.1 row 10)

Dispatch 236's record, as its brief asks (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-packet.md`): every
command run for a plant or an acceptance check, in order, with its exit code and the line that proves it. `build/` is
`memory/builds/dClosedLoop/build/`, and `packet.py` is `build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py`, at blob
`986dd43f0d2ff9cf5f49106e323b3ae014d67078` in every run below and in the commit that carries this record.

**Where the runs happened.** The harness refused this session's writes to the worktree the brief names
(`.claude/worktrees/p0-packet`). So the instrument was written and committed in a clone of `branch/p0-packet` at
`4bfca2c74`, in the session's scratch folder. Every run below was made in a second clone of that commit, "the
acceptance clone", whose scratch commits carry the instrument (so its own blob pins) and the planted files. No
command wrote one of the repository's own worktrees, and no chain build's folder or packet is committed.

**Ids.** A unit no build has minted is written `missing:<id>`, so the build index joins nothing; restore the ids to
re-run a command. `<unit 1>` is `missing:TOOL-dTrueNorth-1`, the placeholder first unit, in the family TOOL that the
execution plan's P0.5 table derives for dTrueNorth. The roster plant's units are `missing:TOOL-dTrueNorth-1` to
`missing:TOOL-dTrueNorth-7`. `<packet>` is `memory/builds/dTrueNorth/prompts/2026-10-20-prompt-<unit 1>-packet.md` and
`<handoff>` is `memory/builds/dTrueNorth/prompts/2026-10-20-prompt-<unit 1>-1-spec-writer.md`. Every command ran from
the clone's root under a bounded timeout.

## [fixture]

The plants in the instrument's own `--fixture`, over dTrueNorth's packet rendered in memory from the tree. The tree
gives dTrueNorth no `[owed]` line, no README roster and no open ask, so the fixture seeds one of each with `FIXTURE`
ids no family declares, and no arm reads an empty population. Plants clause to ask drop one item from the
renderer's input while the arms read the sources whole, so the byte compare stays green and only the arm can see the
omission.

1. `python packet.py --fixture`: exit 0. "byte compare green · completeness 0 findings over clauses 6, gaps 3, parents
   1, owed 1, roster 6, asks 1 · pin arm 5 instruments, 0 findings"
2. `python packet.py --fixture --plant clause`: exit 1. "clause arm: `cl-dClosedLoop-0004@c374ccd0` of dTrueNorth's row
   is not in Items", with the byte compare green
3. `python packet.py --fixture --plant gap`: exit 1. "gap arm: `gap-mem-47`, which dTrueNorth owns, is not in Gaps",
   with the byte compare green
4. `python packet.py --fixture --plant parent`: exit 1. "parent arm: dClosedLoop is not in Parents", with the byte
   compare green
5. `python packet.py --fixture --plant owed`: exit 1. "owed arm: v2:fixture `[owed]`, naming dTrueNorth, is not in
   Obligations", with the byte compare green
6. `python packet.py --fixture --plant roster`: exit 1. "roster arm: `FIXTURE-dTrueNorth-6` of the opened README is not
   in Obligations", with the byte compare green
7. `python packet.py --fixture --plant ask`: exit 1. "ask arm: `FIXTURE-dClosedLoop-1` (fixture) is not in
   Obligations", with the byte compare green
8. `python packet.py --fixture --plant hand-edit`: exit 1. "byte compare: the packet differs from its render from line
   15: A hand edit."
9. `python packet.py --fixture --plant pin`: exit 1. "byte compare green · completeness 0 findings over ... owed 2 ...
   · pin arm 5 instruments, 1 findings" and "pin arm: instrument
   memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py moved: pinned 1f113e30ebfe, HEAD
   holds 6b827f0e7160". `carries.py`'s blob is moved by one added byte, a second `[owed]` line makes the packet stale,
   and the re-render keeps the pins
10. `python packet.py --fixture --plant pin --control no-pin-arm`: exit 0. "byte compare green · completeness 0 findings
    ... · pin arm removed"
11. `python packet.py --fixture --plant pin --control repin`: exit 0. "byte compare green · completeness 0 findings ... ·
    pin arm 5 instruments, 0 findings"
12. `python packet.py --fixture --plant run-live`: exit 1. "--repin refused: memory/builds/dTrueNorth/RUN.md (phase
    BUILDING)"
13. `python packet.py --fixture --plant run-landed`: exit 0. "--repin not refused: no live chain run"

## [acceptance]

The real tree, in the acceptance clone.

1. `python packet.py --check dTrueNorth`: exit 2. "dTrueNorth has no packet under memory/builds/dTrueNorth/prompts/, so
   there is nothing to check"
2. `python packet.py --repin carries.py`: exit 2. "no chain build has a packet, so there is nothing to re-pin"
3. `python packet.py --write dTrueNorth`: exit 1. "refused: no first unit of dTrueNorth: no opened README roster names
   one, and --unit gave '', not <FAMILY>-dTrueNorth-<n>"
4. `python packet.py --write dTrueNorth --unit <unit 1>`, before the build folder exists: exit 1. "refused:
   memory/builds/dTrueNorth does not exist: the opening writes a chain build's folder"
5. Edit: a minimal `memory/builds/dTrueNorth/README.md` (an H1 and one line), and `memory/builds/dTrueNorth/RUN.md`
   holding `phase: RUNNING`.
6. `python packet.py --write dTrueNorth --unit <unit 1>`: exit 1. "refused: a first render pins every instrument, and a
   chain run never pins: memory/builds/dTrueNorth/RUN.md (phase RUNNING)"
7. `rm memory/builds/dTrueNorth/RUN.md`: exit 0.
8. `python packet.py --write dTrueNorth --unit <unit 1>`: exit 0. "packet: wrote <packet>"
9. `python packet.py --write dTrueNorth`: exit 0. "<packet> is current, nothing written"
10. `python packet.py --check dTrueNorth`: exit 0. "byte compare green · completeness 0 findings over clauses 6, gaps 3,
    parents 1, owed 0, roster 0, asks 0 · pin arm 5 instruments, 0 findings"
11. `grep -o 'cl-dClosedLoop-000[1-6]@[0-9a-f]\{8\}' <packet> | sort -u`: exit 0. Six lines,
    `cl-dClosedLoop-0001@83b6b117`, `-0002@6acd9ea9`, `-0003@d2811290`, `-0004@c374ccd0`, `-0005@5417efbc` and
    `-0006@06ceb3cc`; `grep -c` of the numbered Items lines prints 6. This is the handoffs return's worked example
    (`build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-handoffs.md:135-141`), and the packet flags
    `cl-dClosedLoop-0002` as one the token arm cannot see, as the example does.
12. `grep -n` over `<packet>` for the node, the gaps, the child and the extra unit: exit 0. "63:- `record-kind.deviation`";
    "71:- dGroundRules"; "75:- `gap-design-13` · HIGH · `…gap-register.md:361`"; "76:- `gap-build-07` · HIGH ·
    `…gap-register.md:368`"; "77:- `gap-mem-47` · MED · `…gap-register.md:230`"; "100:- 1 unit beyond v2's row, the
    schedule script's `EXTRA`, `**Derived:**` from `missing:PLAY-dClosedLoop-2`: the execution plan's P0.8 row 1".
    The packet also names cl-0004's stand-ins dOrderedCharter and dDeclaredLoop, and cl-0006's stand-in dOrderedCharter,
    and the key `deviation.approval` that dDeclaredLoop owns, as the example does.
13. `file <packet>; tail -c1 <packet> | od -c`: exit 0. "UTF-8 text" with no CRLF, and a final `\n`.
14. Exit 0 for
    `python tools/roles/handoff.py render --role gov-spec-writer --build dTrueNorth --unit <unit 1> --input prompt=<packet>`.
    It prints "<handoff>" and "handoff: description — dTrueNorth · <unit 1> · spec-write".
    The spec writer is the role that reads all five brief keys as required.
15. `python tools/roles/handoff.py check <handoff>`: exit 0. "<handoff> role-sha=06b14b1ac42a task-sha=00117bbda552"
16. `grep -n '^### ' <handoff>`: exit 0. "51:### brief:goal", "55:### brief:items", "66:### brief:acceptance", "72:###
    brief:gates", "78:### brief:non-goals". `grep -c 'cl-dClosedLoop-000[1-6]@'` prints 6.
17. Edit: the README gains a `roster:units` pair of seven rows, `<unit 1>` to `missing:TOOL-dTrueNorth-7`, the seventh
    `**Derived:** missing:PLAY-dClosedLoop-2`.
18. `python packet.py --check dTrueNorth`: exit 1. "byte compare: the packet differs from its render from line 98: -
    none: the opened README's `roster:units` pair names no unit", then "roster arm: `missing:TOOL-dTrueNorth-1` of the
    opened README is not in Obligations" and the same line for each of units 2 to 7.
19. `python packet.py --write dTrueNorth`: exit 0. "packet: wrote <packet>"
20. `python packet.py --check dTrueNorth`: exit 0. "byte compare green · completeness 0 findings over ... roster 7,
    asks 0 · pin arm 5 instruments, 0 findings"
21. `python -c` over every line of `<packet>`, through `tools/memory-tree/corpus_ids.py`'s `resolve_anchor`: exit 0.
    "lines 133 defining an id 0 []". A unit or ask line opens with "unit id" or "ask id", so no list item led by an id
    claims it for dTrueNorth's folder (hygiene check 13).
22. `git commit` of the README, the packet and the handoff (scratch): exit 0.
23. Edit: one byte added to `carries.py`, a `#` after its last line (16018 to 16019 bytes; `git diff --numstat` "1 1"),
    and v2's `[owed]` gains "- dTrueNorth owes a scratch obligation, planted for the packet instrument's pin plant.";
    then `git commit -am` (scratch): exit 0.
24. `python packet.py --check dTrueNorth`, then `--write dTrueNorth`, then `--check dTrueNorth`: exit 1 each. "refused:
    gen_build_index.py --asks exited 1, so the open asks cannot be read". The index generator refused the minimal
    README once it was tracked, and the instrument refused rather than read the asks as none.
25. `python tools/memory-tree/gen_build_index.py --asks --build dClosedLoop --json`, piped through `tail`, so its exit
    was not captured: "README.md: no front matter — line 1 must be '---' (build 'dTrueNorth')"
26. Edit: the README gains front matter (`slug`, `node`, `opened`, `streams`, `roster`, `status`). The same command,
    redirected: exit 1, "header present but unparseable — missing required key(s): ids"
27. Edit: the front matter gains an `ids:` line naming the seven units. The same command: exit 0, `"asks": []`. Then
    `git commit -am` (scratch): exit 0.
28. `python packet.py --check dTrueNorth`: exit 1. "byte compare: the packet differs from its render from line 51: - v2:
    …", "owed arm: v2:1957 `[owed]`, naming dTrueNorth, is not in Obligations", and "pin arm: instrument
    memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py moved: pinned 1f113e30ebfe, HEAD
    holds e55d9402958d"
29. `python packet.py --write dTrueNorth`, the pin-keeping re-render: exit 0. "packet: wrote <packet>"
30. `python packet.py --check dTrueNorth`: exit 1. "byte compare green · completeness 0 findings over ... owed 1, roster
    7, asks 0 · pin arm 5 instruments, 1 findings" and "pin arm: instrument …carries.py moved: pinned 1f113e30ebfe, HEAD
    holds e55d9402958d". This is P0.1 row 10's plant on a real tree: the pin arm reds while the byte compare stays green.
31. Control 1 on the same plant: `python <scratch>/variants/packet-no-pin-arm.py --check dTrueNorth`, a copy of
    `packet.py` whose `moved = check_pins(pins, blob_of) if pin_arm else []` reads `moved = []`: exit 0. "byte compare
    green · completeness 0 findings ... · pin arm 5 instruments, 0 findings"
32. `git checkout -- <packet>`, the packet as it was before the re-render: exit 0.
33. Control 2 on the same plant: `python <scratch>/variants/packet-repin-write.py --write dTrueNorth`, a copy whose
    `render_packet` adds `pins = {p: read_head_blob(p) for p in pins}` after reading the packet's pins: exit 0, "packet:
    wrote <packet>". Then `python packet.py --check dTrueNorth`: exit 0, "pin arm 5 instruments, 0 findings"
34. `git checkout -- <packet>; python packet.py --write dTrueNorth`: exit 0. Then
    `python packet.py --check dTrueNorth`: exit 1, the pin arm's line of step 30 again.
35. Edit: `memory/builds/dTrueNorth/RUN.md` holding `phase: BUILDING`. `python packet.py --repin carries.py`: exit 1.
    "refused: --repin is the owner's, and never runs inside a chain run: memory/builds/dTrueNorth/RUN.md (phase
    BUILDING)". Then `python packet.py --check dTrueNorth`: exit 1, with the packet unchanged.
36. Edit: the same `RUN.md` at `phase: LANDED`. `python packet.py --repin carries.py`: exit 0. "packet: dTrueNorth ·
    …carries.py pinned 1f113e30ebfe -> e55d9402958d · <packet>". Then `python packet.py --check dTrueNorth`: exit 0,
    "pin arm 5 instruments, 0 findings"
37. `python packet.py --repin nosuch.py`: exit 1. "refused: --repin nosuch.py names 0 of the instruments: …"
38. `python packet.py --repin open.py`: exit 1. "refused: memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-open.py
    is not tracked at HEAD, so it has no blob to pin"

## [population]

Probes of the instrument over the whole chain, in the work clone, writing nothing.

1. `python -c` rendering every chain build's packet in memory and running the completeness arms over each: exit 0.
   "22 packets 670401 bytes, arm findings 0". The rows sum to 509 clauses and 386 gaps, no Gaps cell holds an unparsed
   part, and the largest packet is dWellOiledMachine's at 93985 bytes.
2. `python -c` joining every row's gap keys with the register: exit 0. "gap keys 386 distinct 386 not in the register []
   register rows 386"

## [not-checked]

- The real opening: the main loop observes the handoff render again on the opened dTrueNorth, with its real first
  unit and README.
- The opening script's pin. `build/2026-10-20-build-PLAY-dClosedLoop-1-open.py` does not exist yet, so no run pinned it.
  A packet rendered before the opening script is tracked pins only the five instruments above, and `--repin open.py`
  adds its pin later.
- An open ask in dClosedLoop's `BACKLOG.md`: the file is absent, so the real ask arm read an empty population. Only the
  fixture's seeded ask was seen red.
