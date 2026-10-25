# TOOL-dGroundRules-70 — the unattended suite's reader-count arm counts the readers that reach the shared derivation through read_open_passes

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base 533bd309 · streams tooling · order 24

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-70-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-70-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-70-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-70-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Shard 4 of the unattended driver's suite fails one arm, `the driver's five readers call it rather
than parsing the rows their own way: expected [5], got [4]`. Every reader still reaches the run-state
rows through the one shared derivation. `TOOL-dGroundRules-66` routed two of them through the new
`read_open_passes`, which calls `read_pass_declarations` itself, so the arm's literal count went
stale. This unit respells the arm to count what it claims, and adds one arm that grades the hop
through `read_open_passes`.

## 2. Scope (IN)

- **S1** — The reader arms. In `tools/unattended/unattended.test.sh`, the arm at `:7591-7592` is
  respelled as the first arm §4 "The arms" gives, and the second arm §4 gives is added directly after
  it. The suite's unsharded floor and its shard-4 floor each rise by one, as §4 "The floors" gives.
  No other byte of the suite changes. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- `tools/unattended/unattended.sh`. The readers are correct as they stand, and this unit only grades
  them.
- The other arms of block (e) at `tools/unattended/unattended.test.sh:7588-7598`, which still hold:
  the one definition in the shared library, check 23's one call, and neither caller defining its own.
- The inherited reds of shards 1, 3, 5 and 7, and any other spec.

### Edges

none

This unit carries out the follow-through of `TOOL-dGroundRules-66` (CLOSED), whose reader routing
made the count stale. It changes nothing that unit built.

## 4. Design

### Evidence

The arm at `tools/unattended/unattended.test.sh:7591-7592` counts uncommented lines of the driver
that spell `read_pass_declarations ` and expects `5`. That count read `5` at `cfdee9fd0^` and `4` at
`cfdee9fd0`, the build commit of `TOOL-dGroundRules-66`. It reads `4` at `533bd3095`. The main loop's
shard-4 runs at `4f76c4b39` and `591cb00d7` failed on it, as the spec brief records.

At `533bd3095` the driver, `tools/unattended/unattended.sh`, holds these reading sites:

| Site | Function | Calls |
|---|---|---|
| `:1613` | `derive_refreshed_at` | `read_pass_declarations` |
| `:8494` | `print_audit` | `read_open_passes` |
| `:13546` | `check_commit_message` | `read_pass_declarations` |
| `:13912` | `verb_dispatch`, the sibling set | `read_open_passes` |
| `:14025` | `verb_dispatch`, the effective declaration | `read_pass_declarations` |

`read_open_passes` is defined at `:13446-13461` and calls `read_pass_declarations` at `:13448`.
`read_pass_declarations` is defined once, in `tools/unattended/lib-unattended.sh:1116`. So there are
five readers, three direct and two through `read_open_passes`, and the old arm's `4` is the three
direct readers plus the call inside `read_open_passes`.

### The arms

Two arms state it, not one. The first counts the five readers, each calling either function, with
`read_open_passes`'s own body left out of the count. The second counts the calls to
`read_pass_declarations` inside that body. A single arm counting both spellings over the whole file
would read `6` and could not tell a reader from the helper. Without the second arm, a
`read_open_passes` that parsed the rows itself would keep the first arm green.

The body is cut with an awk range, from the line that opens `read_open_passes() {` to the next line
that starts with `}`, which at `533bd3095` is `:13461`. The first arm keeps the lines outside that
range and the second keeps the lines inside it. Both keep the old arm's comment filter.

The arm at `:7591-7592` becomes these four lines. The first two respell it and the last two are the
added arm:

```
same "the driver's five readers call it or read_open_passes rather than parsing the rows their own way" \
  "$(grep -v '^[[:space:]]*#' "$HERE/unattended.sh" | awk '/^read_open_passes\(\)/{s=1} !s; s&&/^}/{s=0}' | grep -cE 'read_(pass_declarations|open_passes) ')" "5"
same "and read_open_passes itself calls it, so the two readers it serves reach the same derivation" \
  "$(grep -v '^[[:space:]]*#' "$HERE/unattended.sh" | awk '/^read_open_passes\(\)/{s=1} s; s&&/^}/{s=0}' | grep -c 'read_pass_declarations ')" "1"
```

Measured at `533bd3095` with these pipelines in a scratch script, the first printed `5` and the
second `1`. The first arm's five lines are the five sites in the table.

What the arms do not check: a reader that calls one of the two functions and also parses the
run-state file on its own beside it, and a call spelled inside a string or a heredoc, which counts as
a reader. A third wrapper's callers spell neither name, so the first arm reads below `5` and reds,
which is the right answer with the wrong cause named. If `read_open_passes` is renamed, both arms
red.

### The floors

Each `same` adds one assertion (`tools/unattended/unattended.test.sh:146`), so the added arm adds one
executed assertion to region four. The arm sits in region four, which opens at `:6567` and ends
before region five opens at `:8600`. The floor check reads `FLOOR_ASSERTIONS` unsharded and
`FLOOR_SHARD_4` under `--shard 4/8` (`:18220-18223`).

`FLOOR_ASSERTIONS=2785` at `:17965` becomes `FLOOR_ASSERTIONS=2786`, with these two comment lines
inserted directly above it, after the `TOOL-dGroundRules-66` comment. The shadowed assignment at
`:17687` does not change.

```
# RAISED 2785 -> 2786 by TOOL-dGroundRules-70: the reader arm's added hop through read_open_passes in
# region four, one `same`, counted off the block's own lines; no suite ran.
```

`FLOOR_SHARD_4=382` at `:18163` becomes `FLOOR_SHARD_4=383`, with this comment line inserted directly
above it, after the `TOOL-dGroundRules-66` comment:

```
# RAISED 382 -> 383 by TOOL-dGroundRules-70: the same 1 region-four reader assertion, see FLOOR_ASSERTIONS.
```

The respelled arm keeps its one assertion, so it moves no floor.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. AC1 runs the `P70` script below.
It holds the two arms' pipelines from §4, copied byte for byte, so it evaluates the arms' predicates
over a driver without running the suite. It prints the first count, a space, and the second count.

```
P70="$TEMP/p70.sh"
cat > "$P70" <<'EOF'
HERE="$1"
echo "$(grep -v '^[[:space:]]*#' "$HERE/unattended.sh" | awk '/^read_open_passes\(\)/{s=1} !s; s&&/^}/{s=0}' | grep -cE 'read_(pass_declarations|open_passes) ')" "$(grep -v '^[[:space:]]*#' "$HERE/unattended.sh" | awk '/^read_open_passes\(\)/{s=1} s; s&&/^}/{s=0}' | grep -c 'read_pass_declarations ')"
EOF
```

The staged breaks of the first criterion run the same script over two scratch copies of the driver,
each with one reader made to parse the rows itself:

```
S70="$TEMP/s70"; rm -rf "$S70"; mkdir -p "$S70/a" "$S70/b"
cp tools/unattended/unattended.sh "$S70/a/unattended.sh"; cp tools/unattended/unattended.sh "$S70/b/unattended.sh"
sed -i '13912s/read_open_passes/awk NF/' "$S70/a/unattended.sh"
sed -i '13448s/read_pass_declarations/awk NF/' "$S70/b/unattended.sh"
```

The whole suite is a self-test this pass may not run. The main loop runs `--shard 4/8` at the close,
and that run prints no `FAIL` line naming `readers` or `read_open_passes`.

- **AC1** — When `bash "$TEMP/p70.sh" tools/unattended` runs, it prints `5 1`.
  Red when: a reader parses the rows itself. Over copy `a`, where the sibling set's call reads the
  file with an inline awk, `bash "$TEMP/p70.sh" "$TEMP/s70/a"` prints `4 1`. Over copy `b`, where
  `read_open_passes` reads the file with an inline awk, `bash "$TEMP/p70.sh" "$TEMP/s70/b"` prints
  `5 0`. Both were measured at `533bd3095`, and so was the old arm's predicate, which printed `4`.
  permission: the suite that holds the arms is a self-test this pass may not run.
- **AC2** — When `grep -cF 'read_open_passes\(\)/{s=1}' tools/unattended/unattended.test.sh` runs, it prints `2`.
  At `533bd3095` it printed `0`.
  Red when: either arm spells a predicate other than §4's, so AC1's script no longer stands for the
  arms the suite runs.
- **AC3** — When `grep -c -e '^FLOOR_ASSERTIONS=2786$' -e '^FLOOR_SHARD_4=383$' tools/unattended/unattended.test.sh` runs, it prints `2`.
  At `533bd3095` it printed `0`.
  Red when: the arm is added and either floor stays where it was, which prints `1` or `0`.
  figure: 2786 and 383 are PINNED, one above the values at `533bd3095`. If another unit moves either
  floor first, the builder adds one to the value it finds and this criterion reads that value.

## 6. Gates

`harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The guards join owes no leg for `tools/unattended/unattended.test.sh`. Run through
`derive_guarded_legs` at `533bd3095`, no non-broad guard trips on it. Every leg
`python tools/check-spec-tokens.py --legs-for tools/unattended/unattended.test.sh` prints trips only
on the broad `tools/`. The first three legs above carry no guard and read the suite on every bar.
`harness arms` reads it as the arm-bearing sibling of the driver, and the two shell-hygiene scans read
it as a tracked shell file. They are named because the edit is in what they read. The suite itself
runs in the pooled self-tests as `unattended driver selftest shard 4/8`
(`tools/run-gates/selftest-budgets.txt`), not as a manifest leg.

New arm: tools/unattended/unattended.test.sh · covers AC1 · the respelled reader count at `:7591`, whose old spelling is red in shard 4 at `533bd3095`, staged red again by copy `a` of AC1's staged breaks · none
New arm: tools/unattended/unattended.test.sh · covers AC1 · the added `read_open_passes` hop, staged red by copy `b` of AC1's staged breaks, the driver's `:13448` call read with an inline awk · FLOOR_ASSERTIONS 2785 to 2786 and FLOOR_SHARD_4 382 to 383

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the build run's rescope add row for this unit and its spec
  brief, `memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-70-spec-brief.md`,
  grounded at `533bd3095`. Picks two arms over one, because one arm counting both spellings cannot
  tell a reader from the helper, and only a second arm reds a `read_open_passes` that parses the rows
  itself. Every count was measured at `533bd3095`, the staged breaks included. The brief's leg item
  names §7; in this Tier-1 shape the Gates section is §6, and the leg line and arm lines sit there.
  S1 holds this unit's whole change, so a second item the main loop folds in before commit, such as
  the hygiene suite's check-7 fixture, lands as its own S-item with its own criteria and files line.
  Folded in before commit, from the main loop's INPROGRESS token sweep: AC3's command matches the
  floors with two `-e` patterns in place of one alternation. The `|` inside the alternation read to
  the checker's `bar` join as a pipe into the suite path. The `BAR` pattern of
  `tools/check-spec-tokens.py` no longer matches AC3's command. AC1's and AC2's commands never
  matched it.

## 9. Reuse audit

This unit builds no mechanism. It extends block (e) of the driver's suite,
`tools/unattended/unattended.test.sh:7588`, in place, with the `same` helper and the comment-filtered
grep the block already uses, and it raises the floors the suite already declares.
`python tools/codebase-map/reuse_lookup.py "count the readers that reach the shared pass-declaration derivation in the unattended driver"`
ranked only name stems (`read`, `read_text`, `counts`, `read_conf`), and none of them counts call
sites. The recall probe returned only this unit's own brief and handoff on the reader count, plus
`TOOL-aSparedSpawn-8` and `TOOL-aUnblockedFleet-9`, neither of which touches block (e).

Recall terms used: `python tools/memory-recall/query.py "unattended suite arm counting read_pass_declarations readers went stale after read_open_passes" --terms "read_pass_declarations read_open_passes five readers shared derivation FLOOR_SHARD_4 FLOOR_ASSERTIONS"`
