**Serves:** research TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18

# Fix brief — dTendedCadence, the spec stage's cross-writer rulings and mechanical reds

The six writers authored all 18 specs under `memory/builds/dTendedCadence/spec/`, staged and NOT committed. The main
loop read their returns and ran the checks the spec brief names. This brief does two things: it RULES on every point
where two writers spelled one interface two ways, and it lists every mechanical red. Apply each ruling and each fix
in the spec it names, and nothing else: no new scope, no design change beyond a ruling, no edit to a spec this list
does not name. The specs have never been committed, so a fix stays at `rev-1` and owes no §9 line. Read the spec brief
`memory/builds/dTendedCadence/prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md`, sections "Every spec,
whatever its unit" and "What the last spec runs had to fix", before the first edit.

## The asks now have ids — replace every letter

The main loop filed every foreign ask the writers named in `memory/builds/dTendedCadence/BACKLOG.md`. Replace each
lettered or numbered ask citation in every spec and in deviation 11 with its id, cited inside prose:

| Was | Now | Target |
|---|---|---|
| A | TOOL-dTendedCadence-21 | dWellOiledMachine |
| B | TOOL-dTendedCadence-22 | dWellOiledMachine |
| C | TOOL-dTendedCadence-23 | dPlacedRequest |
| D | TOOL-dTendedCadence-24 | dPlacedRequest |
| E | TOOL-dTendedCadence-25 | dDeclaredLoop |
| F | TOOL-dTendedCadence-26 | dMindYourWords |
| G | TOOL-dTendedCadence-27 | dWellOiledMachine |
| H | TOOL-dTendedCadence-28 | dDeclaredLoop |
| Q | TOOL-dTendedCadence-29 | dWellOiledMachine |
| R | TOOL-dTendedCadence-30 | dWellOiledMachine |
| 16-1 | TOOL-dTendedCadence-31 | dWellOiledMachine |
| 16-2 | TOOL-dTendedCadence-32 | dWellOiledMachine |
| 9-1 | TOOL-dTendedCadence-33 | dPlacedRequest |
| writer 2's zero-pin finding | TOOL-dTendedCadence-34 | dWitnessedBar |

`grep -n "ask [A-HQR]\b\|ask 16-\|ask 9-\|asks\? [A-HQR]\b" memory/builds/dTendedCadence/spec/*.md` finds them; read
each hit, since a bare capital letter in prose is not always an ask.

## Rulings — one spelling for each interface two writers spelled twice

Each is final for this run. Where the ruling changes what a spec's acceptance observes, rewrite that criterion so it
observes the ruled spelling.

1. **`read_policy_value` is unit 4's.** The one reader is drift-audit's `read_policy_value(key, root, rev=None)` with
   `PolicyRefused`, defined by TOOL-dTendedCadence-4, the key FIRST, because the policy kit's reader-coverage scan
   recognises only a call whose first argument is the key literal (`READER_SHAPES`, `tools/policy/check_policy.py:423`).
   Unit 15's S6 copy is deleted; units 1, 3, 9, 15, 16 and 17 call unit 4's as `read_policy_value("<key>", root)` and
   cite TOOL-dTendedCadence-4 for it. Edges: unit 4 hands off `read_policy_value` to 1, 3, 9, 15, 16 and 17, and each
   consumes it from 4; unit 9's and unit 15's edge pair for it is removed, and any other edge between 9 and 15 stays
   only if a token other than this one carries it.
2. **Band edges live on the `[[reading]]` row** as `edges = [e1, e2]` (unit 14's ruling, because a `drift-pins.txt`
   row's count must be a positive integer, so a zero pin has no row: TOOL-dTendedCadence-34). Unit 8's I3 row admits
   `edges` under that spelling. Units 7 and 17 drop every `edges 0/0` on a `drift-pins.txt` row and every
   `drift-pins.txt` entry at count 0; a zero pin is the reading's tolerance 0 as unit 4's F1 states, with
   `edges = [0, 0]` on its row.
3. **The band name under `maintain.tiers: pins` is `act`**, as units 1 and 14 spell it. Unit 15 renames its `pin`
   band to `act` wherever it names one.
4. **The log band's line is the existing drift-history row, unchanged** (unit 14's ruling: a new `band` column makes
   every node's history file unreadable, and `ev=reading` is no event the journal accepts). Any spec citing
   `ev=reading` or a `band=` column follows unit 14 and cites it.
5. **The event run key's segments.** `check_cadence_segment` (TOOL-dPlacedRequest-18 S1) grades the cadence segment
   `maintain`; `check_lease_segment` (TOOL-dPlacedRequest-1 S1) grades the period segment `<event>.<sha12>`. Unit 8
   spells the key and `derive_event_key`; units 1, 2 and 13, which unit 8 hands `derive_event_key` to, name it in
   backticks where they read the key and declare the `consumes-from` back.
6. **One row per reading.** Unit 7 extends the `dangling_pointers_in_own_ledger` row unit 8 already declares among the
   27, never a second row of the same name, which unit 8's check refuses.
7. **The maintenance record is committed by patch, never by the walk** (unit 1 F4): the Maintain walk commits nothing
   and files a records-only patch intake per written record. Unit 6 rewords any sentence saying the program commits
   the record, and keeps `security-head` written on every completed review whatever `maintain.record-when` says.
8. **The record's fields** are unit 6's I10 grammar and include `unread-nodes:` (unit 16) and
   `retrofit-heat: <value>/<of>` (unit 9). Units 9, 13, 15 and 16 spell their fields exactly as unit 6 does.
9. **`check_body_moved` lives in the `extract_code` block** (`tools/lib/extract_code.py` and its kit copies, unit 12
   F1), since codebase-map may not import memory-tree. Unit 5 cites it there and calls it through
   `measure_dossier_staleness`; the brief's I16 home `code_record.py` is superseded.
10. **The security review launches through `launch_act`**, a Workflow act the cadence program starts
    (TOOL-dWellOiledMachine-1 S2, S3). Unit 10 grants `gov-maintainer` no `Workflow` tool, so unit 13 never says the
    maintainer runs `tier2-review.js`; it says the program launches the harness and the maintainer's item role is
    the filing. Keep unit 10's `gov-maintainer` hand-off to 13 only where 13 still reads the role.
11. **No 8 → 13 `item.maintain.patch` edge.** A security finding names no fix in `maintain.fixes`, so unit 13 files
    through `item.maintain.file` only. Remove that edge pair from units 8 and 13; 13 still consumes the event key from
    8 (ruling 5).
12. **Unit 3's node-scoped readings reach unit 16.** Unit 3 hands `act-direct`, `idle_processes_past_ceiling`,
    `landed_branches_unpruned` and `item.maintain.direct` to unit 16: unit 16 names each in backticks where its node
    pass routes a node-scoped reading with a direct fix to `item.maintain.direct`, and declares the `consumes-from`
    back. Unit 3's hand-off of `maintain.py` and `derive_fix_route` to unit 9 gets its reverse in unit 9.
13. **Unit 16's node pass reaches unit 2.** Unit 2 names `--scope node` where its cadence row runs the node pass and
    declares `consumes-from TOOL-dTendedCadence-16` for it; the per-node row waits on TOOL-dTendedCadence-32.
14. **Unit 18's reading tree reaches 5, 12 and 16.** Each of those names `maintain.reading-tree` in backticks and
    declares `consumes-from TOOL-dTendedCadence-18` for it; units 8 and 18 hand units 7, 5 and 12 the tokens unit 7's
    writer listed (`[[reading]]`, `run_signal_leg`, `maintain.reading-tree`, `item.maintain.patch` for 5) where each
    truly reads them, and each pair is declared both ways.
15. **Unit 15's `maintain.interpreter-eol: file` hand-off to 17.** Unit 17 names `maintain.interpreter-eol: file` in
    backticks where its `file` value files through unit 15's ask, or unit 15 drops the bullet if 17 does not read it.

## Hygiene check 12 — one-sided edges and placeholders

After the rulings, every §3 edge in the folder is declared both ways and runs from an earlier `order` to a later
one. The ones the gate reported, before the rulings, were:

- TOOL-dTendedCadence-1 consumes-from 4, no hands-off back (ruling 1).
- TOOL-dTendedCadence-15 consumes-from 4, no hands-off back (ruling 1).
- TOOL-dTendedCadence-16 hands-off to 2, no consumes-from back (ruling 13).
- TOOL-dTendedCadence-3 consumes-from 4, no hands-off back (ruling 1).
- TOOL-dTendedCadence-3 hands-off to 16, no consumes-from back (ruling 12).
- TOOL-dTendedCadence-9 consumes-from 15, no hands-off back (ruling 1).

Two specs carry an unfilled skeleton placeholder (the gate matches `<FAMILY-slug-seq>`, `YYYY-MM-DD` or `<fill:`):
TOOL-dTendedCadence-6 and TOOL-dTendedCadence-17. Replace each with its value, or reword so the literal is not left
standing; a format string a criterion quotes is spelled with its real value.

## Hygiene check 25 — retirements

- TOOL-dTendedCadence-7, §2 S4, retires a named thing and carries no `**Readers:**` clause: write one, `by name:` and
  every reader that spells the name, then `by value:` and every reader of its value, or `NO VALUE READERS` and a
  reason, each found with `git grep` over the tree.
- TOOL-dTendedCadence-6, §2 S5: its `by name:` half lists `git grep -n "runlog.py record"`, which is a command, not a
  reader. Name each reader that spells the name, by path, or write `READER NOT IN TREE` and a reason on that half.

## `tools/check-spec-tokens.py` — 19 hits on these specs

Leg lines: each §4 path below trips a leg's guard, and that leg goes on the spec's §7 leg line.

- TOOL-dTendedCadence-15: `run-gates canary` (from `tools/gate-legs.json`).
- TOOL-dTendedCadence-18: `check-wiring self-test` and `lexicon naming predicates` (from
  `.claude/skills/drift-audit/SKILL.md`), `straggler-guard arms` (from `.lexicon.conf`).
- TOOL-dTendedCadence-6: `pre-push run-log line` and `run-gates run-log line` (from `tools/runlog/runlog.py`),
  `policy fixtures` (from `tools/runlog/model.py`).
- TOOL-dTendedCadence-8: `policy fixtures` (from `tools/drift-audit/kit.toml`).

Paths and suites:

- TOOL-dTendedCadence-18 §6 cites `tools/lib/signal_leg.py`, which is not tracked: cite it by its basename
  `signal_leg.py` in §6 and keep the full path in §2, §4 and Files touched.
- TOOL-dTendedCadence-6 §6 names `selftest.py` as an observation. A suite is not an acceptance observation: observe
  the checker on a staged break or a fixture, and put the suite on a `New arm:` line in §7.

Hand-off tokens the receiving spec never names, each settled by the ruling beside it:

- TOOL-dTendedCadence-15 → 17 `maintain.interpreter-eol: file` (ruling 15).
- TOOL-dTendedCadence-16 → 2 `--scope node` (ruling 13).
- TOOL-dTendedCadence-3 → 16 `act-direct`, `idle_processes_past_ceiling`, `landed_branches_unpruned`,
  `item.maintain.direct` (ruling 12).
- TOOL-dTendedCadence-8 → 1, 13 and 2 `derive_event_key` (ruling 5).

## Deviation 11

`memory/builds/dTendedCadence/build/2026-11-01-build-TOOL-dTendedCadence-1-deviation-11.md`: the main loop set its
`Follow-through:` to `amends cl-dClosedLoop-0442@53466888`, because the as-built view refuses a clause departure with
no amends row, and TOOL-dTendedCadence-1 now carries `cl-dClosedLoop-0442@d7b64b62`, the hash of its After text, as
TOOL-dTendedCadence-13 carries `cl-dClosedLoop-0454@3bb6c0f8` from deviation 131. Replace "ask H" in its Reason with
TOOL-dTendedCadence-28, and touch nothing else in it.

## When you finish

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25` and fix any red it prints on these files. Return
the list of specs you edited, each with the rulings and fixes applied, and any ruling you could not apply with the
reason. Commit nothing and do not run the index generator.
