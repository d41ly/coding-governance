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
