# TOOL-aSwiftRefusal-3 — `read_open_passes` leaves out every key of a deferred unit, naming each on stderr

**Status:** CLOSED · rev-2 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aSwiftRefusal-1-agent-ledger.md](../build/2026-11-10-build-TOOL-aSwiftRefusal-1-agent-ledger.md) | journal | TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-4 |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-brief.md) | research | TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-1-token-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-token-fix-brief.md) | research | TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-3-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-3-1-spec-writer.md) | journal | — |
| [2026-11-10-review-TOOL-aSwiftRefusal-1-3-closing-diff-round1.md](../reviews/2026-11-10-review-TOOL-aSwiftRefusal-1-3-closing-diff-round1.md) | diff-review | TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 |

<!-- /gen:spec-records -->

## 1. Goal

A unit set aside with `--rescope --act defer` keeps every open key it dispatched reserved, so a
sibling declaring one of its paths is refused by condition 1 until a commit carrying the unit's
`Pass:` trailer lands. This unit makes the one open-pass reader leave a deferred unit's keys out,
by the build's one deferral predicate, and name each released key on stderr.

## 2. Scope (IN)

- **S1** — The release. `read_open_passes` in `tools/unattended/unattended.sh` leaves out every
  key that `check_pass_open` calls open when `check_unit_deferred`, the predicate
  `TOOL-aSwiftRefusal-2` mints, answers 0 for its unit. For each such key it prints one line on
  stderr and no row:
  `unattended: <anchor> <unit> left out as deferred, so its declared paths reserve nothing until it is dispatched again: <paths>`.
  A key of a unit the predicate does not call deferred is printed as before. Observed by AC1, AC2,
  AC3.
- **S2** — One predicate. The reader calls `check_unit_deferred` and parses no `rescope` or
  `dispatch` row itself. Observed by AC4.
- **S3** — The comments. The signature comment of `read_open_passes` names the deferred skip
  beside the terminal one, and its header comment says why a deferred unit reserves nothing and
  that a later dispatch re-takes it. Observed by AC5.
- **S4** — The verbs contract. `tools/unattended/VERBS.template.md` and its dogfood copy
  `memory/guides/UNATTENDED-VERBS.md` gain one sentence directly after the sentence "A pass of a
  unit whose spec is CLOSED or WONTDO is not a sibling":
  `A pass of a deferred unit, whose spec reads DEFERRED and whose latest rescope defer row follows every dispatch row naming it, is not a sibling either, until the unit is dispatched again.`
  The two files stay byte-equal past their kit marker line. Observed by AC6.
- **S5** — The suite arm on the §7 `New arm:` line. NOT OBSERVED by a criterion here: it
  re-observes AC1 to AC3 end to end through `--dispatch`'s condition 1, and the main loop observes
  it red, then green, at the close.

## 3. Non-goals (OUT)

- The deferral predicate itself, its row reading and its status half. `TOOL-aSwiftRefusal-2`
  mints it for the order gate, and this unit only calls it.
- The order gate, the edge refusal and the spec-token block's position in `verb_dispatch`. Those
  are units 2 and 1, and the edge refusal is a non-goal of the build.
- `check_pass_open`, `pass_commit`, `read_pass_declarations` and `check_commit_message`. The brief
  names them as non-goals. `--check-commit` keeps asking `check_pass_open` alone, as
  `TOOL-dGroundRules-66` §4 says why (`tools/unattended/unattended.sh:14184-14195`).
- Check 23's history grading in `tools/unattended/check-unattended.sh`. A deferred unit's unclosed
  window still counts there, the stricter direction.
- Any new rescope act, any new run-state row, and any refusal's text.

### Edges

- **consumes-from** `TOOL-aSwiftRefusal-2` — `check_unit_deferred <run-state file> <unit> <spec status>`, as that unit's §4 "The predicate" defines it; without it this unit has nothing to call, and a second reading of the defer rows here would break the build rule of one predicate
- **consumes-from** external — `check_pass_open`, `read_pass_declarations` and the caller-loaded `SPEC_PATH` and `SPEC_ST` maps as they stand at base `ae6735c1`; this unit changes none of them

## 4. Design

### Evidence

Read at base `ae6735c1`, where `tools/` equals this branch's tip `52e1f752`.

- `read_open_passes` (`tools/unattended/unattended.sh:14098-14113`) reads every key from
  `read_pass_declarations`, drops a closed one through `check_pass_open` (`:14105`), then reads the
  unit's status from `SPEC_PATH` and `SPEC_ST` and skips `CLOSED` or `WONTDO` with one stderr line
  (`:14106-14110`). Any other status, `DEFERRED` included, prints the row.
- Its two callers are `verb_dispatch`'s sibling set (`:14567`), which condition 1 iterates
  (`:14621-14637`), and `print_audit`'s open units (`:8657`), loaded after its `load_spec_facts`
  probe (`:8656`).
- A defer row is `<iso> rescope · item defer <unit> · reason <why>`, written by `park` from
  `verb_rescope` (`:14058`), and a dispatch row is `<iso> dispatch · item <anchor> <unit> · reason
  <paths>`. The run-state file is append-only, so line order is the order the rows were written.
- Probed on 2026-11-10 at the base: a run-state fixture carrying one dispatch row for `TOOL-x-1`
  and a later defer row, with `SPEC_ST` reading `DEFERRED`, prints the dispatch row from
  `read_open_passes`. With `CLOSED` it prints the terminal stderr line and no row. AC1 stages the
  same fixture.
- dOrderedCharter's run: unit 37 was refused on paths deferred unit 31 still held, released only by
  a commit carrying `Pass: PLAY-dOrderedCharter-31` (the brief, "Drawn from the session").

### The reader

```
read_open_passes() { # run-state file · [current] -> the open keys of units neither terminal nor deferred
  read_pass_declarations "$1" ${2:+"$2"} | while IFS= read -r _r; do
    <cut anchor, unit and declared paths, unchanged>
    check_pass_open "$_g" "$_u" "$1" "$_decl" || continue
    <terminal skip, unchanged>
    if check_unit_deferred "$1" "$_u" "$_st"; then
      printf 'unattended: %s %s left out as deferred, so its declared paths reserve nothing until it is dispatched again: %s\n' "$_g" "$_u" "$_decl" >&2
      continue
    fi
    printf '%s\n' "$_r"
  done
}
```

Openness is asked first, as for the terminal skip, so the stderr line names only keys the skip
releases. The deferral is per unit, so every key of the unit is left out, the keys at older
anchors included. The reader passes the predicate the `_st` it already read for the terminal skip
(`:14106`) and the run-state file it was given, and loads nothing itself. The predicate answers 1
at once for any status but DEFERRED, so a key of any other unit costs no extra read. An unreadable
run-state file also answers 1, which keeps the key reserved.

A dispatch row written after the defer row makes the predicate false, so every key of the unit is
reserved again, the older ones included. That is how a unit re-taken after a deferral reserves its
paths (AC3), and it is the conservative direction a disjointness proof wants.

### Both verbs

`--dispatch` and `--audit` read open passes through this one reader (`TOOL-dGroundRules-66`), so
both stop counting a deferred unit's keys. For `--audit` that means a deferred unit is no longer
graded, STALLED included, from a key it will not commit against, which matches the terminal skip.
Giving the two verbs two answers is the two-answers class that reader exists to close.

### What it does not see

- **A deferral with work in flight.** A unit deferred while its builder still writes stops
  reserving its paths at the defer row. Its uncommitted writes are not protected from a sibling
  declared after that row, as `TOOL-dGroundRules-66` states for the flip-to-commit window.
- **A status read from the working tree.** The status the reader passes comes from the maps the
  caller loaded, as the terminal skip's does. A spec flipped to DEFERRED before its defer row is
  written still reserves, because the row half is false.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `left out as deferred` | stderr line, S1 | `read_open_passes` |

This unit mints no function. `check_unit_deferred` is `TOOL-aSwiftRefusal-2`'s to mint and to
grade against the lexicon.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

The kit version marker moves through the lander's `mint`, never by hand (the build README).

### Alternatives rejected

- **A deferral reading inside `read_open_passes`.** It would read the defer rows a second way
  beside the order gate's, and the build rule is one predicate for both.
- **The skip inside `check_pass_open`.** `--check-commit` would inherit it. A deferred unit's own
  later pass commit would then find no open pass, the defect `TOOL-dGroundRules-66` §4 records for
  the terminal skip.
- **Release only the keys at anchors before the defer row.** The keys dispatched after it are
  already reserved because the predicate is false, so the split buys nothing and adds a per-key
  row comparison.

## 5. Production-readiness checklist

- security — this narrows condition 1's refusal set: an open key of a deferred unit no longer
  blocks a sibling. No new write path. The scratch guard is unchanged. The unprotected window is
  §4 "What it does not see", made visible by the S1 line.
- perf / scale — one `check_unit_deferred` call per open key, inside a loop that already walks
  `pass_commit` per key. It reads the run-state file only for a unit reading DEFERRED, and no call
  is made for a closed key.
- error / empty / loading states — a failed spec read leaves no status, and an unreadable
  run-state file answers 1, so the predicate cannot call a unit deferred and every open key stays
  reserved. An empty sibling set still prints the
  existing "proof over an empty set" line (`:14582`).
- observability — one stderr line per released key (S1).
- risks — the in-flight deferral window (§4). A re-dispatch re-takes the unit, so a mistaken
  deferral is undone by dispatching again.
- testing — AC1 to AC6, and the suite arm on the §7 `New arm:` line.
- migration — none. No row format changes. A run already carrying a deferred unit's open keys has
  them released on its next `--dispatch` once units 2 and 3 land.
- user docs — the verbs contract and its dogfood copy (S4). No page under `help/` covers the
  unattended verbs.

## 6. Acceptance criteria

The criteria AC1 to AC5 run from the repository root of the pass's worktree. `S` is that pass's
scratch directory, spelled absolute. `D` selects the driver: `D=.` is AFTER, the driver this pass
built, and `D=$B` is BEFORE, the kit at base `ae6735c1` extracted to a short path outside the
worktree, because the driver sources its library beside itself. Each anchor is a sha no clone
resolves, so `check_pass_open` calls the key open (`:14131`). The block below was run at the base on
2026-11-10, and `probe DEFERRED "$S/run-deferred.md"` printed the dispatch row with both drivers.

```
B="$TEMP/sr3b"; mkdir -p "$B"; git archive ae6735c1 tools/unattended tools/lib | tar -x -C "$B"
printf '%s\n' '2026-11-10T00:00:01Z dispatch · item deadbeef TOOL-x-1 · reason work/a' \
  '2026-11-10T00:00:02Z rescope · item defer TOOL-x-1 · reason set aside' > "$S/run-deferred.md"
cp "$S/run-deferred.md" "$S/run-retaken.md"
printf '%s\n' '2026-11-10T00:00:03Z dispatch · item deadbee2 TOOL-x-1 · reason work/b' >> "$S/run-retaken.md"
probe() { # status · run-state file · [current]  (reads D)
  bash -c 'source "$0/tools/unattended/unattended.sh" >/dev/null 2>&1
    SPEC_PATH[TOOL-x-1]=s1; SPEC_ST[s1]=$1; read_open_passes "$2" ${3:+"$3"} 2>&1' "$D" "$@"; }
```

- **AC1** — When `probe DEFERRED "$S/run-deferred.md"` runs with AFTER, it prints no line carrying
  `TOOL-x-1 · reason` and exactly one line carrying
  `deadbeef TOOL-x-1 left out as deferred, so its declared paths reserve nothing`.
  `probe DEFERRED "$S/run-deferred.md" current` prints the same. With BEFORE the first command
  prints the dispatch row and no `left out as deferred` line.
  Red when: a deferred unit's open key is returned as a row, or is released with no stderr line.
- **AC2** — When `probe INPROGRESS "$S/run-deferred.md"` runs with AFTER, it prints the dispatch
  row ending `TOOL-x-1 · reason work/a` and no `left out as deferred` line. `probe CLOSED` over the
  same file prints `left out as terminal (CLOSED)` and no deferred line.
  Red when: a defer row alone releases a unit whose spec does not read DEFERRED, or the deferred
  skip shadows the terminal one.
- **AC3** — When `probe DEFERRED "$S/run-retaken.md"` runs with AFTER, it prints two rows, one
  carrying `deadbeef TOOL-x-1 · reason work/a` and one carrying `deadbee2 TOOL-x-1 · reason work/b`,
  and no `left out as deferred` line.
  Red when: a unit dispatched again after its defer row stays released, or only its newest key is
  reserved again.
- **AC4** — When `bash -c 'source tools/unattended/unattended.sh >/dev/null 2>&1; type read_open_passes' | grep -cE 'item defer|dispatch · item [0-9]'`
  runs, it prints `0`, and the same `type` output piped to `grep -cw check_unit_deferred` prints
  `1`. Read together with AC1, the release is decided by `TOOL-aSwiftRefusal-2`'s predicate and not
  by a reading of the rows here.
  Red when: the reader parses defer or dispatch rows itself, so the order gate and the reader can
  disagree on which unit is deferred.
- **AC5** — When `grep -cE '^read_open_passes\(\) \{ #.*deferred' tools/unattended/unattended.sh`
  runs, it prints `1`, and `sed -n '/^# THE OPEN PASSES, ONE READER/,/^read_open_passes()/p' tools/unattended/unattended.sh | grep -c 'dispatched again'`
  prints at least `1`.
  Red when: the reader's comments still name only the terminal skip, so a reader of the code cannot
  tell why a deferred unit's keys vanish.
- **AC6** — When `grep -c "A pass of a deferred unit, whose spec reads DEFERRED" tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md`
  runs, it prints `1` for each file, and
  `diff <(tail -n +2 tools/unattended/VERBS.template.md ) <(tail -n +2 memory/guides/UNATTENDED-VERBS.md )`
  exits 0, the comparison `TOOL-aSwiftRefusal-1` uses for the same two files.
  Red when: the contract still names only CLOSED and WONTDO as not siblings, or the dogfood copy
  drifts from the template.

## 7. Gates

The close runs these legs once, after the last unit of the build is terminal, and observes the new
arm below red on its staged break and green once restored. No pass runs a leg or the suite.

`unattended kit gate` · `unattended skill wiring` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `pass-order history` · `routed commits name a specced unit` · `brief-recorded` · `tier2-review self-test` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · in region four beside `TOOL-dGroundRules-66`'s terminal-unit arm, the first unit declares a path and gets a `rescope · item defer` row appended in `park`'s grammar with its spec mutated to DEFERRED, then the second unit declares the same path: red against the base driver, whose condition 1 refuses it; admitted with the `left out as deferred` line; refused again with the first spec mutated to INPROGRESS; refused again on that path after the first unit is dispatched once more on a disjoint path, which re-takes its older key · FLOOR_ASSERTIONS and FLOOR_SHARD_4, by the arm's own count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft from the build's brief,
  `memory/builds/aSwiftRefusal/prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-brief.md` item 3 and
  acceptance 4 to 6, grounded at base `ae6735c1`.
- rev-2 · 2026-11-10 · token fold from
  `memory/builds/aSwiftRefusal/prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-token-fix-brief.md`:
  the two `[path]` hits on AC6's `diff` command, where each process substitution's `)` sat on the
  path's word. A space now parts each `)` from its path, so the command runs unchanged. Nothing else
  moves.

## 10. Reuse audit

The seam extended is `read_open_passes` in `tools/unattended/unattended.sh:14098`, the one open-pass
reader `--dispatch` and `--audit` share (`TOOL-dGroundRules-66`). Its terminal-status skip
(`:14106-14110`) is the shape the deferred skip copies, stderr line included, and the deferral
itself is `check_unit_deferred`, which `TOOL-aSwiftRefusal-2` mints, so no row reading is added
here. The probe
`python tools/codebase-map/reuse_lookup.py "leave a deferred unit's dispatched pass keys out of the open sibling set"`
ranked name stems only (`key`, `keys`, `units`, `opened`), plus `read_pass_declarations` and
`pass_commit`, which this unit keeps unchanged. None of them decides a deferral, so beyond the reader
and unit 2's predicate no existing seam fits. The recall probe returned `TOOL-aRoutedQuill-13`,
which unit 2 closes, and `TOOL-dGroundRules-66` and `-70`, whose one-reader rule this unit keeps.

Recall terms used:
`python tools/memory-recall/query.py "a deferred unit's open dispatch passes keep reserving paths against siblings" --terms "read_open_passes deferred rescope defer dispatch sibling open pass reserve condition release terminal"`
