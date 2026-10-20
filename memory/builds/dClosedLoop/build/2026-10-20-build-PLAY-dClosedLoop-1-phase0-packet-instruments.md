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

## The pinned baseline and one roster reader

Dispatch 243's evidence for its brief (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-packet-2.md`): the two
defects dispatch 241 found outside its paths (`build/…-phase0-deviations-instruments.md`, `## P0.1 and P0.2`). Built in
a `--shared` clone of the main loop's branch at `db3ea9981`, committed on `p0-packet-2` as `93c1d481d`. The old code is
the two files at `db3ea9981`, `packet.py` blob `986dd43f0` and `bare-ids.py` blob `50d0385f1`; the new is `bc8d65536`
and `ea671312d`. Every command ran from a tree's root with `python -B`, under a bounded timeout, and a script named
`d243/…` is in this session's scratch folder. Ids follow this record's rule above: a unit no build has minted is
written `missing:<id>`, though each output held it bare, and `<packet>` is the packet `--write` names.

**What changed.** `packet.py`'s `read_tree` takes the baseline from `deviations.BASELINE`, through the module
`asbuilt.py` loads, so the packet and the as-built view render from one pin. It no longer reads v2's `Baseline:` line,
so its refusal for a v2 with no such line is deleted, and the Pins line reads "the pin `deviations.py` carries (P0.1 row
5)". On a moved line the packet renders from the pin; it does not refuse. `bare-ids.py`'s new `read_roster(text, id_re,
slug=None)` is the `roster:units` pair's one reader. `read_roster_units`, which `deviations.py` calls, and
`packet.read_roster`, which the opening calls, are adapters over it, so neither caller changed. It lives in
`bare-ids.py` because that file cannot load `packet.py`: `packet.py` loads it, by path, through `asbuilt.py` and
`deviations.py`. Where the two old readers agreed, on the markers, it keeps their reading. Where they differed it takes
the generator's id grammar from `bare-ids.py` (declared families only, and a `missing:` citation is no unit) and one
unit per table row, the row's first id, from `packet.py`.

**1. Both instruments' modes, before and after** (`d243/runs.py`, which logs each command's exit and output): at
`db3ea9981`, then with the change uncommitted, then at `93c1d481d`. The three logs are byte-identical (`diff` exit 0).

| Command | Exit | The line that proves it |
|---|---|---|
| `packet.py --fixture` | 0 | byte compare green · completeness 0 findings over clauses 6, gaps 3, parents 1, owed 1, roster 6, asks 1 · pin arm 6 instruments, 0 findings |
| `packet.py --fixture --plant clause` | 1 | clause arm: `cl-dClosedLoop-0004@c374ccd0` of dTrueNorth's row is not in Items; the byte compare green |
| `… --plant gap` | 1 | gap arm: `gap-mem-47`, which dTrueNorth owns, is not in Gaps; the byte compare green |
| `… --plant parent` | 1 | parent arm: dClosedLoop is not in Parents; the byte compare green |
| `… --plant owed` | 1 | owed arm: v2:fixture `[owed]`, naming dTrueNorth, is not in Obligations; the byte compare green |
| `… --plant roster` | 1 | roster arm: `FIXTURE-dTrueNorth-6` of the opened README is not in Obligations; the byte compare green |
| `… --plant ask` | 1 | ask arm: `FIXTURE-dClosedLoop-1` (fixture) is not in Obligations; the byte compare green |
| `… --plant hand-edit` | 1 | byte compare: the packet differs from its render from line 15: A hand edit. |
| `… --plant pin` | 1 | pin arm: instrument …-carries.py moved: pinned 0b5fab9cc06d, HEAD holds 5b44b718e5ed; the byte compare green |
| `… --plant pin --control no-pin-arm` | 0 | byte compare green · completeness 0 findings over … owed 2 … · pin arm removed |
| `… --plant pin --control repin` | 0 | byte compare green · completeness 0 findings over … owed 2 … · pin arm 6 instruments, 0 findings |
| `… --plant run-live` | 1 | --repin refused: memory/builds/dTrueNorth/RUN.md (phase BUILDING) |
| `… --plant run-landed` | 0 | --repin not refused: no live chain run |
| `packet.py --check dTrueNorth` | 2 | dTrueNorth has no packet under memory/builds/dTrueNorth/prompts/, so there is nothing to check |
| `packet.py --repin carries.py` | 2 | no chain build has a packet, so there is nothing to re-pin |
| `bare-ids.py` | 0 | nothing printed |
| `bare-ids.py --opened` | 0 | nothing printed |

The fixture never reads a README's roster: the tree holds no chain build's README, so the fixture seeds one. Item 4's
rows C1 and C2 run the roster arm over real opened READMEs.

**2. The baseline plant** (item 1). The control, in a worktree at `db3ea9981` with nothing planted: a minimal
`memory/builds/dTrueNorth/README.md`, untracked, then `packet.py --write dTrueNorth --unit missing:TOOL-dTrueNorth-1`,
exit 0, "packet: wrote <packet>"; `grep -n '^- baseline:' <packet>`, "50:- baseline:
`59ff8f2ac04a967751eae00de6856afbea66c033`, v2's `[clause-ids]` `Baseline:`"; `d243/baseline_probe.py <packet>`, exit
0, "departures from the pin 0". The folder was then removed. The probe compares the packet's Pins baseline and each
Items pin with `deviations.BASELINE` and with the hashes `deviations.read_chain_clauses` gives v2 at that sha, and
exits 1 listing each departure.

The plant, `d243/plant_baseline.py`, ran in a worktree at `db3ea9981` and in one at `93c1d481d`. It loosened
cl-dClosedLoop-0004's text in v2 from "green on a status-only edit" to "green on a status-only edit or on any edit" and
committed that (scratch: `f708a45d8` on the old code, `baed32c15` on the new). It then re-pointed v2's `Baseline:` line
to that commit in the working tree and wrote the minimal README. Then, in each tree:

| Command | Old code | New code |
|---|---|---|
| `packet.py --write dTrueNorth --unit missing:TOOL-dTrueNorth-1` | exit 0, "packet: wrote <packet>" | exit 0, the same |
| `grep -n '^- baseline:' <packet>` | "50:- baseline: `f708a45d8…`, v2's `[clause-ids]` `Baseline:`": it followed the moved line | "50:- baseline: `59ff8f2ac…`, the pin `deviations.py` carries (P0.1 row 5)" |
| the packet's line 24, Items 4 | "4. `cl-dClosedLoop-0004@19b7aa97` · now `c374ccd0` ·": the loosened text pinned as the baseline's, and the frozen hash, which the as-built view renders from the pin, read as its change | "4. `cl-dClosedLoop-0004@c374ccd0` · now `c374ccd0`, as at the baseline; v2's text now hashes `19b7aa97`, a departure from the frozen design" |
| `d243/baseline_probe.py <packet>` | exit 1, "Pins baseline f708a45d8, not the pin 59ff8f2ac" and "Items pins cl-dClosedLoop-0004@19b7aa97, and v2 at the pin hashes it c374ccd0" | exit 0, "departures from the pin 0" |
| `packet.py --check dTrueNorth` | exit 0, "byte compare green · completeness 0 findings over clauses 6, gaps 3, parents 1, owed 0, roster 0, asks 0 · pin arm 6 instruments, 0 findings" | exit 0, the same |

`--check` is green in both trees, because the renderer and the arms read one tree. Comparing v2's line with the pin
is `deviations.py`'s job, which lists the move, and `asbuilt.py --check` reports it (dispatch 241's item 2).

**3. The two old readers against the merged one** (`d243/roster_probe.py`, exit 0). It ran on the new tree, with the
old blobs of both files at `db3ea9981` loaded beside it.

- Over the README that `open.py`'s `render_readme` writes for each of the 22 chain builds: `packet.read_roster` gave the
  same rows on all 22, and `read_roster_units` gave the same units on 21. The one that differs is dTrueNorth. Its row 7
  carries "**Derived:** missing:PLAY-dClosedLoop-2", and the opening writes that id bare (`open.py`'s
  `derive_decision_id`). The old `read_roster_units` read it as an eighth unit; the merged reader reads 7.
- Over the deviation fixture's README (`render_fixture_readme`, family `FIX`), both read `FIX-dTrueNorth-80` and
  `FIX-dTrueNorth-81`.
- One row planted in the pair for each case where the two old readers disagreed (`packet.read_roster` under dTrueNorth's
  slug):

| Row in the pair | `packet.read_roster`, old | new | `read_roster_units`, old | new |
|---|---|---|---|---|
| a unit in its `missing:` form | the unit | none | none | none |
| row 7's shape, the decision id bare | unit 7 | unit 7 | unit 7 and the decision id | unit 7 |
| a unit of `FIXTURE`, a family no conf declares | the unit | none | none | none |
| two units in one row | the first | the first | both | the first |
| a prose line inside the pair | none | none | its id | none |

**4. `bare-ids.py` plain and `--opened`, with their plants** (`d243/bareids_plants.py`), in a fresh worktree at
`db3ea9981` and in one at `93c1d481d`. Each planted file is restored after its run. The two logs are byte-identical
(`diff` exit 0).

| Step | Command | Exit | Output |
|---|---|---|---|
| A1 | `bare-ids.py`, nothing opened | 0 | nothing |
| A2 | the same, a bare missing:TOOL-dTrueNorth-1 appended to `…-recheck-brief-a.md` | 1 | one line, `…-recheck-brief-a.md:112: missing:TOOL-dTrueNorth-1` |
| A3 | the same id behind `x:` | 1 | the same line |
| A4 | control: the same id in its `missing:` form | 0 | nothing |
| B0 | `d243/opened.py dTrueNorth dGroundRules`, the opening script's own `render_readme` and `render_backlog`; both folders staged; `gen_build_index.py --write` | 0, 0 | dTrueNorth roster units 1 to 7 and no ask; dGroundRules units 1 to 11 and ask 12; "build-index: wrote 1541 artifact(s)" |
| B1 | `bare-ids.py` | 1 | two lines, `memory/builds/dGroundRules/BACKLOG.md:5: missing:TOOL-dGroundRules-12` and `:9:`, the ask the opening minted |
| B2 | `bare-ids.py --opened` | 0 | nothing |
| B3 | `--opened`, a bare missing:TOOL-dGroundRules-40 appended | 1 | one line, `…-recheck-brief-a.md:112: missing:TOOL-dGroundRules-40` |
| B4 | `--opened`, control: roster unit missing:TOOL-dGroundRules-3 cited | 0 | nothing |
| B5 | `--opened`, the same citation, its row removed from `roster:units` | 1 | one line, `…-recheck-brief-a.md:112: missing:TOOL-dGroundRules-3` |
| B6 | `--opened`, both files restored | 0 | nothing |
| C1 | `packet.py --write dTrueNorth`, then `--check dTrueNorth` | 0, 0 | "packet: wrote <packet>"; "… owed 0, roster 7, asks 0 · pin arm 6 instruments, 0 findings" |
| C2 | `packet.py --write dGroundRules`, then `--check dGroundRules` | 0, 0 | "packet: wrote …"; "… clauses 11, gaps 3, parents 1, owed 1, roster 11, asks 0 · pin arm 6 instruments, 0 findings" |

Rows C1 and C2 run the packet's roster arm over a real opened README through the merged reader, and the packet's name
comes from the roster's first row.

**5. The readers of what changed.**

- `deviations.py`'s run kind (`derive_run_kind`), probed with `python -c` over each opened tree's index, as a
  `git write-tree` object, so nothing was committed. On the old code, dTrueNorth gave "kind build asks [] units with no
  spec 8", the last two being missing:TOOL-dTrueNorth-7 and missing:PLAY-dClosedLoop-2. On the new code it gave "kind
  build asks [] units with no spec 7". dGroundRules gave the same on both: "kind spec asks
  [missing:TOOL-dGroundRules-12] units with no spec 11". The departures report prints that list as "units with no
  spec". On dTrueNorth's real opening, the old reader would have listed the decision id there for good, since no spec
  defines it. The run kind is unchanged, because dTrueNorth has no carry-forward ask.
- `d243/readers_runs.py`, in the clone's own checkout at `db3ea9981` and in the new tree:
  - `deviations.py`: exit 0, "baseline 59ff8f2ac read, chain-build specs 0, members 0 (0 unjoined), records 0 ·
    refused 0 · policy report".
  - `--fixture`: exit 0, "chain-build specs 16, members 25 (10 unjoined), records 15 · refused 6 · policy report ·
    fixture".
  - `--report dTrueNorth --fixture`: exit 0, "build run · …-departures-build.md · entries 34 · byte compare green ·
    validating arm green".
  - Its plants: `kind-spec` exit 0 ("spec run", entries 15); `kind-build` and `kind-whole` exit 0 ("build run",
    entries 14); `kind-norun` exit 2 ("nothing measured: memory/builds/dTrueNorth/RUN.md is absent").
  - `open.py --summary`: exit 0, "summary of the 22 chain builds".

  With each run of 9 to 40 hex digits replaced, the two logs are identical. The raw logs differ only in the fixture
  repository's shas, which move with the `packet.py` bytes the fixture copies.
- `open.py` takes the "at the baseline" sha it writes in each README from `packet.read_tree()`, so it now writes the
  pin. On today's tree v2's line names the pin, so its output is unchanged.
- The naming lexicon: `lexicon.py --suggest read_roster --as py.function`, exit 0, "OK — read_roster leads with `read`,
  which the declaration carries, and satisfies snake for cell `py.function`". The plain run after the commit graded
  `py.function` 3869 (3868 before) with P1 offenders still 1211. It exits 1 on the pin mismatch "verb offenders 1211
  UNDER pin 1219", which dispatch 241 handed back.

**6. What these runs do not show.**

- The packet flagging a v2 whose `Baseline:` line moved. `--check` stays green on the planted tree (item 2);
  `deviations.py` and `asbuilt.py --check` see the move.
- An edit of `bare-ids.py`'s reader as a moved pin. The packet now reads its roster through `bare-ids.py`, which is not
  among its pinned instruments, and `deviations.py` already loaded it unpinned.
- An indented marker. The merged reader keeps the old readers' `ln.strip()` read of the markers rather than the
  generator's column-0 `check_marker_line`, so it still reads a marker that the generator's structure check refuses.
- A row whose first id is not its own unit. Under `read_roster_units`, which takes no slug, that id is the row's unit;
  no README the opening renders has such a row.

**After the commit, the M6 checklist.** `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` over
`93c1d481d`: exit 0, 16 classes, 10 by anchor and 6 universal. Five were checked:

- **A fixture that passes by finding nothing.** `packet.py --fixture` seeds its roster, so its unchanged verdicts say
  nothing about the reader. Items 3 and 4 (C1, C2) read real READMEs.
- **Two answers to one question.** That is the defect fixed here. The roster's readers are now `bare-ids.py`'s
  `read_roster` and its two adapters. For the baseline, `asbuilt.py` and `packet.py` take `deviations.BASELINE` through
  one module object, and `open.py` takes it from `packet.read_tree()`. `deviations.read_baseline_line` alone reads v2's
  line, and only to check it against the pin.
- **A retirement inventory that misses readers by value.** The deleted refusal's text, "records no Baseline": a
  `grep -rn` over the tree's `.py`, `.md` and `.sh` files finds nothing. Its exit 2 had no reader but `open.py`'s
  generic `Unmeasured` catch.
- **An amendment that leaves its other half standing.** Each was amended with the code: `packet.py`'s docstring fields
  1 and 9, its "What it does not check", its `genindex` comment and the Pins line, and `bare-ids.py`'s docstring.
- **A synthetic value standing in.** The plant moves the real line in a real tree to a real commit, and the opened
  trees are the opening script's own renders.

The remaining classes concern heredocs, fences, table cells split on a pipe, ledgers, merge ranges and owner items.
None of them applies here.

**7. `bare-ids.py` pinned** (the main loop's follow-up, after its merge `82cd88009`). This closes the second bullet of
item 6: a run that edited `bare-ids.py`'s reader used to move no pin. The worktree was fast-forwarded onto
`82cd88009`, whose tree is `e5402134d`'s, and the change is committed as `b200f3c2d`, giving `packet.py` blob
`1a8159416`. `INSTRUMENTS` gains `build/2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py` as its last entry, so the
indexed loads (`INSTRUMENTS[0]`, `[2]` and `[4]`) keep their meaning, and field 1 of the docstring names it. Every
command ran from a tree's root with `python -B`, under a bounded timeout. On 2026-10-21 `--write` names
`<packet>` `memory/builds/dTrueNorth/prompts/2026-10-21-prompt-<unit 1>-packet.md`.

- `d243/runs.py` at `b200f3c2d`, compared with item 1's log at `93c1d481d`, whose two blobs `82cd88009` carries: all
  17 commands keep their exits and finding lines. The two logs differ only on the 10 summary lines that count the
  pin arm's instruments, each now "pin arm 7 instruments" where it read 6. With that count replaced, `diff` exits 0.
  The fixture's `--plant pin` and its controls still move `carries.py`, so the fixture never moves `bare-ids.py`'s
  pin; the run below does.
- The pin arm's plant on `bare-ids.py`, run by `d243/pin_plant.py` in a fresh worktree at `82cd88009` (the old code)
  and in one at `b200f3c2d`. First, a minimal untracked `memory/builds/dTrueNorth/README.md`; then
  `packet.py --write dTrueNorth --unit missing:TOOL-dTrueNorth-1`, exit 0 on both, "packet: wrote <packet>"; then
  `--check dTrueNorth`, exit 0 on both. The old packet holds 6 instrument pins, none of them `bare-ids.py`. The new
  packet holds 7, one being "- instrument: `…-bare-ids.py` blob `ea671312d2969bed2fc82f738bc02703d6f19c73`". Then
  one byte, a `#` after the last line, was added to `bare-ids.py` and committed (scratch: `68424be03` on the old
  code, `a2ceb8f35` on the new). `git diff --numstat` gives "1 0", and the blob moves from `ea671312d296` to
  `ae0327ae8b7d`.

| Command | Old code | New code |
|---|---|---|
| `packet.py --check dTrueNorth` | exit 0, "byte compare green · completeness 0 findings over clauses 6, gaps 3, parents 1, owed 0, roster 0, asks 0 · pin arm 6 instruments, 0 findings": the edit moves no pin | exit 1, "byte compare green · completeness 0 findings over clauses 6, gaps 3, parents 1, owed 0, roster 0, asks 0 · pin arm 7 instruments, 1 findings" and "pin arm: instrument memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py moved: pinned ea671312d296, HEAD holds ae0327ae8b7d" |
| `packet.py --write dTrueNorth`, the pin-keeping re-render | exit 0, "<packet> is current, nothing written" | exit 0, the same |
| `packet.py --check dTrueNorth` | exit 0, the same line as above | exit 1, the same two lines as above: the re-render kept the pin |
| `packet.py --repin bare-ids.py` | exit 1, "refused: --repin bare-ids.py names 0 of the instruments: …" | exit 0, "packet: dTrueNorth · memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py pinned ea671312d296 -> ae0327ae8b7d · <packet>" |
| `packet.py --check dTrueNorth` | exit 0, the same line as above | exit 0, "… pin arm 7 instruments, 0 findings" |

- The checklist over `b200f3c2d`: `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` exits 0 with the same
  16 classes as above. Three were checked:
  - **A synthetic value standing in.** The plant is a real one-byte commit, read through `git rev-parse HEAD:<path>`
    as the pin arm reads it. It is not the blob the fixture derives.
  - **A fixture that passes by finding nothing.** The fixture's pin plant leaves `bare-ids.py`'s pin unmoved, as the
    first bullet says.
  - **An amendment that leaves its other half standing.** This item names item 6's bullet it closes. A
    `grep -rn` over `build/*.py` for a typed count of the instruments ("6 instruments", "five instruments" and the
    like) finds none. `INSTRUMENTS` has no reader outside `packet.py`, since `deviations.py` keeps its own list.

## The packet's file name

Dispatch 244's evidence for its brief (`build/2026-10-21-build-PLAY-dClosedLoop-1-phase0-brief-packet-name.md`). The
opening at `b50573ef4` redded hygiene check 21 on all 22 packets. Each was named for its build's first unit, and each
one's Serves line lists PLAY-dClosedLoop-1. The work was built in a `--shared` clone of the main loop's branch at
`45a825043`, on `p0-packet-name`: `a5a331d9e` carries the code, `738dca981` the re-rendered opening, and the commit
after them this section. Every command ran from a tree's root with `python -B`, under a bounded timeout, and a script
named `d244/…` is in this session's scratch folder. `<packet>` is a build's
`memory/builds/<slug>/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`.

**What changed.** `packet.py` declares `SERVES = "PLAY-dClosedLoop-1"` once and builds both the packet's Serves line
and its file name from it. `scan_packets` globs `*-prompt-PLAY-dClosedLoop-1-packet.md`, so it finds a build's packet
by that name alone, and `render_packet` writes a first render under it. The first unit fed only the name, so three
things that served it are deleted: its derivation, its two refusals ("no first unit of <slug>" and "--unit <id> is not
<first unit>"), and the `--unit` flag that supplied it. `render_packet(slug)` is the call `open.py` already made. Both
docstrings name the new form. `packet.py`'s blob moves from `1a8159416` to `7dd2b7972`, and `open.py`'s from
`43cdb6d77` to `b8c9e9c04`. The code is committed before the re-render because a first render pins each instrument's
blob at HEAD. Rendered in the code's own commit, every packet would pin the old blobs of both files and carry the old
generator version, so its check would red as soon as that commit landed.

**1. The commands, in order.**

| # | Tree | Command | Exit | The line that proves it |
|---|---|---|---|---|
| 1 | scratch | `git clone --shared` of the main loop's worktree at `branch/unruffled-aryabhata-d89ede`, `git config core.hooksPath .githooks`, `git worktree add -b p0-packet-name` | 0 | "HEAD is now at 45a825043" |
| 2 | `45a825043` | `tools/lexicon/lexicon.py --suggest SERVES --as py.constant` | 2 | "cell `py.constant` is UNDECLARED — no CELLS row names it, so there is no convention to answer in". No new function is named. |
| 3 | `45a825043`, the clone's own checkout | `d244/runs.py`: `packet.py --fixture` and its 12 plant and control runs | 0 | item 2 |
| 4 | the change, uncommitted | `d244/names.py`: per build, what `scan_packets` finds, the path `render_packet` names, and that path's id against the rendered Serves line | 0 | "builds 22 · name/Serves mismatches 0"; `scan_packets` finds none of the 22 old-named packets |
| 5 | `45a825043` | the same | 0 | "builds 22 · name/Serves mismatches 22", e.g. "render names memory/builds/dTrueNorth/prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-packet.md · claims TOOL-dTrueNorth-1 · Serves ['PLAY-dClosedLoop-1'] · MISMATCH" |
| 6 | the change, staged | `git ls-files --eol` and `git cat-file -p :<path>` over the two files | 0 | "i/lf w/lf attr/text eol=lf" for both, and no CR in either staged blob. `git show :<path>` counted 696 and 709 CR lines, a rendered view of the same blobs and not their bytes. |
| 7 | | `git commit`, through the pre-commit hook | 0 | "[p0-packet-name a5a331d9e] …" |
| 8 | `a5a331d9e` | `git rm` of the 22 `*-prompt-<first unit>-packet.md` files | 0 | `git status --short`: 22 `D` lines |
| 9 | | `open.py --write` | 0 | "open: wrote and staged 43 files, 22 contract rows in memory/project/readme-contract.txt and 22 packets, opened 2026-10-21; run `gen_build_index.py --write` next" |
| 10 | | `tools/memory-tree/gen_build_index.py --write` | 0 | "build-index: wrote 1561 artifact(s)" |
| 11 | | `git diff HEAD --stat`, then `git add` of the 22 READMEs it refilled | 0 | "22 files changed, 88 insertions(+), 88 deletions(-)": the 22 packets alone, every README back at its committed bytes and no other view changed |
| 12 | | `git ls-files --eol` and `git cat-file -p` over the 22 new packets | 0 | "i/lf w/lf" for all 22, no CR in any staged blob |
| 13 | | `open.py --check`, before the commit | 0 | "… summary arm over 22 rows, 0 disagreements · findings 0" |
| 14 | | `git commit`, through the pre-commit hook | 0 | "[p0-packet-name 738dca981] …", 22 renames, each moving four lines: the `packet.py` and `open.py` pins, the render HEAD and the generator version |
| 15 | `738dca981` | `open.py --check` | 0 | "open: check of the opening of 2026-10-21 · 65 files byte-compared · roster arm over 509 clauses · summary arm over 22 rows, 0 disagreements · findings 0" |
| 16 | `738dca981` | `packet.py --check <slug>` for each of the 22 | 0 for all 22 | item 3 |
| 17 | `738dca981` | `gen_build_index.py --check` | 0 | "build-index: clean (1561 artifact(s))", with "0 verdict(s)" |
| 18 | `738dca981` | `d244/runs.py` | 0 | item 2: its log is byte-identical to step 3's (`diff` exit 0) |
| 19 | a throwaway worktree at `738dca981` | `d244/red.py`, open.py's red tests, run in the background while steps 20 to 25 ran | 0 | item 4 |
| 20 | `738dca981` | `tools/memory-tree/gotchas.py --for-diff 45a825043..HEAD` | 0 | item 6 |
| 21 | `738dca981` | `bash tools/memory-tree/check-memory-hygiene.sh`, the whole tree | not run | "BLOCKED by scratch-guard: a role agent runs no gate. Agent type gov-builder ran … which is row G1 leg, the leg "memory hygiene"." Owed (item 5). |
| 22 | `738dca981` | `d244/check21.py` | 0 | "packet S rows 22 · packet findings 0 · branch 4 findings tree-wide, unfiltered 0" |
| 23 | `45a825043` | the same | 0 | "packet S rows 22 · packet findings 22 · branch 4 findings tree-wide, unfiltered 22", each "S row: <the old packet> — the name claims <its build's first unit>" |
| 24 | `738dca981` | `packet.py --write dTrueNorth --unit TOOL-dTrueNorth-1` | 2 | "packet.py: error: unrecognized arguments: --unit TOOL-dTrueNorth-1" |
| 25 | `738dca981` | `packet.py --write dTrueNorth` | 0 | "packet: memory/builds/dTrueNorth/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md is current, nothing written", and `git status --short` empty |
| 26 | the throwaway worktree | red 7 again, with the codebase map regenerated | 1 | item 4 |
| 27 | the throwaway worktree | `tools/roles/handoff.py render --role gov-spec-writer --build dTrueNorth --unit TOOL-dTrueNorth-1 --input prompt=<packet>`, then `handoff.py check` on what it wrote, then `git clean` of it | 0, 0 | "handoff: description — dTrueNorth · TOOL-dTrueNorth-1 · spec-write"; "role-sha=06b14b1ac42a task-sha=3be43a7f5124"; its five `### brief:` heads at lines 51 to 78, and 6 lines naming `cl-dClosedLoop-000[1-6]@` |

**2. The packet plants, before and after** (steps 3 and 18). The two logs are byte-identical.

| Command | Exit | The line that proves it |
|---|---|---|
| `packet.py --fixture` | 0 | byte compare green · completeness 0 findings over clauses 6, gaps 3, parents 1, owed 1, roster 7, asks 7 · pin arm 7 instruments, 0 findings |
| `… --plant clause` | 1 | clause arm: `cl-dClosedLoop-0004@c374ccd0` of dTrueNorth's row is not in Items; the byte compare green |
| `… --plant gap` | 1 | gap arm: `gap-mem-47`, which dTrueNorth owns, is not in Gaps; the byte compare green |
| `… --plant parent` | 1 | parent arm: dClosedLoop is not in Parents; the byte compare green |
| `… --plant owed` | 1 | owed arm: v2:fixture `[owed]`, naming dTrueNorth, is not in Obligations; the byte compare green |
| `… --plant roster` | 1 | roster arm: `TOOL-dTrueNorth-7` of the opened README is not in Obligations; the byte compare green |
| `… --plant ask` | 1 | ask arm: `PLAY-dClosedLoop-17` (memory/builds/dClosedLoop/BACKLOG.md:11) is not in Obligations; the byte compare green |
| `… --plant hand-edit` | 1 | byte compare: the packet differs from its render from line 15: A hand edit. |
| `… --plant pin` | 1 | pin arm: instrument …-carries.py moved: pinned 0b5fab9cc06d, HEAD holds 5b44b718e5ed; the byte compare green |
| `… --plant pin --control no-pin-arm` | 0 | byte compare green · completeness 0 findings over … owed 2 … · pin arm removed |
| `… --plant pin --control repin` | 0 | byte compare green · completeness 0 findings over … owed 2 … · pin arm 7 instruments, 0 findings |
| `… --plant run-live` | 1 | --repin refused: memory/builds/dTrueNorth/RUN.md (phase BUILDING) |
| `… --plant run-landed` | 0 | --repin not refused: no live chain run |

Since the opening, the fixture's roster of 7 and its 7 asks are the tree's own: dTrueNorth's README roster and the
clean-reading asks in dClosedLoop's `BACKLOG.md`. So the roster and ask plants drop real items, and only the `[owed]`
line is seeded.

**3. Each packet's check** (step 16). Each printed "packet: <slug> · <packet> · byte compare green · completeness 0
findings over clauses C, gaps G, parents P, owed O, roster R, asks 7 · pin arm 7 instruments, 0 findings". The counts
are those of the opening's own record (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-open-instruments.md`,
`[acceptance]` 6), whose pin arm then read 6 instruments:

| Build | C | G | P | O | R |
|---|---|---|---|---|---|
| dTrueNorth | 6 | 3 | 1 | 0 | 7 |
| dGroundRules | 11 | 3 | 1 | 1 | 11 |
| dSafePassage | 13 | 13 | 1 | 0 | 13 |
| dOrderedCharter | 37 | 31 | 1 | 3 | 37 |
| dFairHearing | 18 | 13 | 1 | 0 | 18 |
| dDeclaredLoop | 34 | 17 | 2 | 4 | 34 |
| dPlacedRequest | 21 | 18 | 1 | 0 | 21 |
| dKeptSession | 28 | 8 | 2 | 1 | 28 |
| dBoundRoles | 26 | 22 | 3 | 4 | 26 |
| dFurnishedOrders | 20 | 13 | 1 | 0 | 20 |
| dTotalRecall | 26 | 22 | 3 | 7 | 26 |
| dLinkedLibrary | 25 | 23 | 1 | 0 | 25 |
| dMindYourWords | 17 | 11 | 4 | 1 | 17 |
| dWellOiledMachine | 61 | 63 | 3 | 5 | 61 |
| dWitnessedBar | 30 | 27 | 1 | 0 | 30 |
| dRankedPlan | 16 | 10 | 3 | 1 | 16 |
| dIndexedDesign | 16 | 13 | 5 | 2 | 16 |
| dScopedBuild | 15 | 10 | 4 | 1 | 15 |
| dShippedRelease | 31 | 24 | 6 | 1 | 31 |
| dTendedCadence | 18 | 14 | 5 | 2 | 18 |
| dCalibratedLens | 17 | 13 | 2 | 0 | 17 |
| dConvergedCharter | 23 | 15 | 4 | 1 | 23 |

**4. open.py's red tests** (steps 19 and 26): the opening record's `[red]` 1 to 11, in a throwaway worktree at
`738dca981`. Each plant was restored by `git reset --hard 738dca981` before the next, and `git status --short` read
empty after each. Only `open.py`'s commands ran on a plant. Red 3's `gen_build_index.py --check` is a leg of the bar,
not the opening's, and was left out.

| Red | Plant, with `git diff --numstat` | Command | Exit | The line that proves it |
|---|---|---|---|---|
| 1 | dGroundRules's README, `goal bound.` to `goal bound!` ("1 1") | `open.py --check` | 1 | "byte compare: memory/builds/dGroundRules/README.md differs from its render from line 19: … goal bound!" |
| 2 | the `cl-dClosedLoop-0012` roster row deleted ("0 1") | `open.py --check` | 1 | findings 6: "roster arm: dGroundRules: `cl-dClosedLoop-0012` is in 0 roster rows, not exactly one", beside the README's byte compare, the byte compare of dGroundRules's `<packet>` and its packet arm, and the summary arm's Units (`10` against `11`) and Packet lines |
| 3 | `parents: dTrueNorth` to `dTrueNorht` ("1 1") | `open.py --check` | 1 | "byte compare: … from line 10: parents: dTrueNorht" and "summary arm: dGroundRules: `parents:` reads `dTrueNorht` in the files, and the derivation gives `dTrueNorth`" |
| 4 | dGroundRules's README removed from `memory/project/readme-contract.txt` ("0 1") | `open.py --check` | 1 | "summary arm: dGroundRules: Contract row reads `absent` in the files, and the derivation gives `present, bound`" |
| 5 | `roster: TOOL` to `roster: PLAY` ("1 1") | `open.py --check` | 1 | "byte compare: … from line 6: roster: PLAY" and "summary arm: dGroundRules: Family · `streams:` reads `PLAY · tooling` in the files, and the derivation gives `TOOL · tooling`" |
| 6 | `tools/newkit/kit.toml`, committed (scratch `04d2f1b59`) | `open.py --carriers --check` | 1 | "tools/newkit/ (routed product paths; tracked tools/newkit/kit.toml) is under a selector, and the list at the opening commit b50573ef4b42 omits it", with "113 entries now, 112 listed" |
| 7 | `git rm tools/settings-merge.py`, then `git commit` | `git commit` | 1 | the pre-commit hook refused it: "FAIL test_generated_artifacts_are_fresh" and "STALE symbols.json — regen: python tools/codebase-map/gen_map.py --write". Nothing was committed, so `--carriers --check` did not run. |
| 7, step 26 | the same removal, then `tools/codebase-map/gen_map.py --write` (exit 0) and the `memory/map/generated/symbols.json` it rewrote staged, committed through the hook (scratch `03a9825a2`) | `open.py --carriers --check` | 1 | "tools/settings-merge.py is on the list at the opening commit b50573ef4b42, and nothing tracked at HEAD sits under it", with "111 entries now, 112 listed" |
| 8 | `PLAY-dClosedLoop-13`'s ask row removed from dClosedLoop's `BACKLOG.md` ("0 1") | `open.py --check`, then `open.py --write` | 1, 1 | findings 67: "owed asks: memory/builds/dClosedLoop/BACKLOG.md lacks the opening's row: - PLAY-dClosedLoop-13 · filed 2026-10-21 · …", and for each of the 22 packets a byte compare, a packet arm and a summary-arm Packet line. Then "open: refused: memory/builds/dClosedLoop/BACKLOG.md exists without the opening's rows, and the opening writes it once", with `git status --short` showing only the plant. |
| 9 | dGroundRules's `BACKLOG.md` copied into dTrueNorth's folder | `open.py --check` | 1 | "byte compare: memory/builds/dTrueNorth/BACKLOG.md exists, and the opening writes none for a whole-run build" and "summary arm: dTrueNorth: Carry-forward ask reads `TOOL-dGroundRules-12` in the files, and the derivation gives `none: whole run`" |
| 10 | dGroundRules's `<packet>`, `### Goal` to `### Goal!` ("1 1") | `open.py --check` | 1 | findings 3: "byte compare: memory/builds/dGroundRules/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md differs from its render", "packet arm: dGroundRules: byte compare: the packet differs from its render from line 13: ### Goal!", and the summary arm's Packet line, 30358 B with exit 1 against 30357 B with exit 0 |
| 11 | every plant restored, `git status --short` empty | `open.py --check`, then `open.py --carriers --check` | 0, 0 | "… findings 0"; "carriers at HEAD 738dca98145d against the list at the opening commit b50573ef4b42 · 112 entries now, 112 listed · findings 0" |

**5. The hygiene run, owed.** The brief names one gate for this unit: the whole-tree `check-memory-hygiene.sh`, run
after the commit. The scratch-guard hook refused it to this role (step 21), so it did not run. It is owed to the main
loop at the close, where no check 21 finding may name a packet. `d244/check21.py` stands in for its check 21 until
then. It runs `gen_build_index.py --print-bindings`, the parse check 21 reads, and applies three arms to every packet's
rows: the A arm (no conformant Serves line), the B arm (a Serves id no spec defines) and branch 4's filename
projection, ported from the awk at `tools/memory-tree/check-memory-hygiene.sh:1446-1478`. On `45a825043` it gives the
opening's 22 findings, each in the check's own words. On `738dca981` it gives none, and no branch 4 finding anywhere
in the tree. It is not the check. It leaves out `extract_graded_rows`'s legacy list and `RECORD_SERVES_CUTOFF`, which
only remove rows, and the U arm's pin, and it runs none of the other checks.

**6. After the commits, the M6 checklist.** `python tools/memory-tree/gotchas.py --for-diff 45a825043..HEAD` over both
commits: exit 0, 16 classes, 10 by anchor and 6 universal. Six were checked:

- **A retirement inventory that misses readers by value.** Retired: the `--unit` flag, `first_unit`, the two refusal
  texts and the per-unit name. `git grep` over the tree's `.py`, `.sh`, `.json` and `.toml` files finds nothing for
  the refusal texts, `first_unit` or "first render's unit", for `packet.py` with `--unit`, or for `render_packet(` with
  a second argument. Of the tools that read a prompt file's name, `handoff.py`'s `derive_prompt_name` counts only
  `<date>-prompt-<unit>-<digits>-` under the unit's own stem, so the packet's name never enters its numbering; step 27
  renders a handoff from a renamed packet. `deviations.py`'s `outside-packet` plant writes a packet-shaped path only as
  a write outside the build's folder, and reads no name. The earlier records that quote the old name are history.
- **Two answers to one question.** The Serves line and the name were typed apart, so they could drift. Both now read
  `SERVES`. The docstrings name the form in prose, as the brief asks.
- **An amendment that leaves its other half standing.** The usage line, the `--write` gloss, the `render_packet` line
  and `open.py`'s list of what it writes were amended with the code. A `grep` for "first unit" and `first_unit` over
  both files finds nothing.
- **A fixture that passes by finding nothing.** The fixture renders in memory and reads no file name, so its unchanged
  verdicts say nothing about the name. The name was seen red first on the old tree, by `d244/names.py` (step 5) and
  `d244/check21.py` (step 23).
- **A synthetic value standing in.** The probes call the real `render_packet` and read the generator's real bindings
  parse, and the red tests plant the opening's own files.
- **A heredoc escape that reaches a regex.** No heredoc: every script and every commit message was written to a file.

The remaining classes concern guards above a fold, fences, merges read as additions, inserts after a repeated key,
ledger tokens, table cells split on a pipe, a record's Serves line and filename, owner items, policy values and quoted
rates. None of them applies here, except the Serves-and-filename class, which this change closes for the packets.

**7. What these runs do not show.**

- Check 21 over the whole tree, and every other hygiene check: owed (item 5).
- A packet under any other name. `scan_packets` does not find it, so neither `packet.py --check` nor `open.py --check`
  reads it. Hygiene check 21 reds it, as it redded the opening's.
- `gen_build_index.py --check-format` and every other leg of the bar: none ran.
