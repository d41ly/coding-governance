# TOOL-dQuietDisk-19 — the before and after measurements, with their instruments

**Status:** SPECCED · rev-4 · 2026-11-22 · node d · Tier-1 · base e4699ee7 · streams tooling · order 7 · ratified 2026-11-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-26 |
| [2026-11-20-build-TOOL-dQuietDisk-19-analysis.md](../build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md) | research | — |
| [2026-11-22-build-TOOL-dQuietDisk-19-measurements.md](../build/2026-11-22-build-TOOL-dQuietDisk-19-measurements.md) | journal | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 |
| [2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md) | research | TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-17 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-14 TOOL-dQuietDisk-9 |

<!-- /gen:spec-records -->

## 1. Goal

The build's claim is that gov's suites and history legs stop spending git processes and file
creates on answers they already hold. This unit writes the one record that backs the claim with
numbers: four subjects read before and after, each beside the instrument that read it, and a
comparison derived from those readings.

## 2. Scope (IN)

- **S1** — The instrument `qd-measure.sh`, the fenced block under §4 "The instrument", is carried
  byte for byte into the record. Every reading in the record is a row it printed. Observed by AC1.
- **S2** — The B0 readings. Before the first unit pass, the main loop runs the instrument over
  subjects M1, M2 (cold and warm) and M3 at the build base `e4699ee75`, the merge that brought
  dWitnessedBar's land tip `ed833f684` in, where the owner's ruling of 2026-11-22 puts every before
  reading. It commits the rows as the record's first version in a records commit carrying
  `Pass: none`. Observed by AC2 and AC3.
- **S3** — The A readings. After every unit at orders 1 to 6 is terminal, TOOL-dQuietDisk-26,
  TOOL-dQuietDisk-17 and TOOL-dQuietDisk-9 among them, and before this unit is dispatched, the main loop takes two row sets at one sha A: A-off, with every switch this build
  added held at its today value, and A-on, with every switch at its default. It re-takes the A-on
  M2 rows once to show the instrument repeats, and commits all rows into the record in a records
  commit carrying `Pass: none`. Observed by AC2, AC3 and AC8.
- **S4** — The unit pass writes the record's Comparison section. Every cell is derived from the
  Readings table, and every row names the unit that owns the saving and quotes the bound that
  unit's spec promises. Observed by AC4, AC5 and AC6.
- **S5** — The unit pass writes the nicocares seed-suite section from the nicocares session's own
  record, cited by repository, commit and path. While that record does not exist, the section holds
  the line `awaiting: fix4-nicocares-landed.md`, naming the nicocares session and the readings it
  owes, and the unit closes; a records commit adds the readings when they land (F1). Observed by
  AC7.
- **S6** — The record carries the binding line, the dated filename and the seven sections §4 names
  in order, its Limits section included. Observed by AC9.

## 3. Non-goals (OUT)

- A product instrument. The instrument stays a fenced block in a record and is run from the run's
  scratch. A per-leg git-process ceiling is the G-B ask, `TOOL-dQuietDisk-22`, and a per-row temp
  ceiling is the G-A ask, `TOOL-dQuietDisk-21`, both filed in this build's `BACKLOG.md`.
- Any write to `tools/run-gates/selftest-budgets.txt` or `tools/run-gates/ceiling-evidence.txt`.
  dWitnessedBar owns both, and a reading taken on a loaded host is not ceiling evidence.
- A verdict. Each unit's own spec proves its verdict did not move. The rc column here is a sanity
  column, and AC5 only names a pair that differs.
- Any reading of the unattended kit's own suites (owner rule, 2026-08-23).
- Any reading inside the live worktree, dWitnessedBar's worktree or either `gov-upgrade` worktree.
  Every reading runs in a detached scratch `git clone --shared` with its own `TEMP`.
- Running nicocares' suite from gov. Its numbers are the nicocares session's (brief item 22).
- A `--shard` reading of `tools/govkit/selftest.py`. The suite takes no shard flag at BASE, at
  `609cd40b1` or at `e4699ee75` (`grep -c shard` prints 0 over each), so M3 is the whole leg.
- Commits the closing review folds in after A. They are not re-measured.

### Edges

- **consumes-from** `TOOL-dQuietDisk-1` — the switch of the history verdict store, which A-off holds
  at its today value for M2
- **consumes-from** `TOOL-dQuietDisk-2` — the bound M2's saving is held to
- **consumes-from** `TOOL-dQuietDisk-7` — the switch of the template cache, which A-off holds at
  its today value for M1 and M3
- **consumes-from** `TOOL-dQuietDisk-10` — the bound M1's saving is held to
- **consumes-from** `TOOL-dQuietDisk-11` — the bound M3's saving is held to
- **consumes-from** `TOOL-dQuietDisk-26` — the checker's one listing per invocation, which A's M1
  rows hold because A is taken after it lands
- **consumes-from** external — the nicocares session's record of its seed-suite readings

## 4. Design

### Evidence

Read at `e4699ee75`, the build base, unless a line names another sha. It is the merge that brought
dWitnessedBar's land tip `ed833f684` into this run (owner ruling, 2026-11-22).

- The builder role may run one gate, `lexicon naming predicates` (`.claude/roles.json@c6505c35c853`,
  `roles.gov-builder.gates`), unchanged at `e4699ee75`. `tools/hooks/scratch-guard.js#checkGateSuite`
  refuses a role agent any `*.test.sh` or `*selftest.py` script
  (`tools/hooks/scratch-guard.js@e4699ee75:1740`). So
  the unit pass cannot run M1 or M3. M6 refuses it M2, a leg outside its allowlist. The brief's
  line "the unit pass takes the after readings" cannot be built, and S3 gives them to the main loop.
- `tools/unattended/gate-guard.js#readHeadRef` returns null for a detached HEAD, "because a
  detached HEAD keys nothing" (`tools/unattended/gate-guard.js@e4699ee75:708`). Its rows deny
  a suite only where a run record's `run-branch:` equals the ref HEAD names. F2 resolved (a) on
  that reading: the main loop takes the M1 and M3 readings during RUNNING, in a detached scratch
  clone.
- The pass-order leg reads the remote's advertised tip, and a clone with no remote reads "this
  clone declares no remote to observe" (`tools/unattended/lib-unattended.sh@e4699ee75:1513`).
  `read_history_range` then grades the whole history (`:1563-1572`), and the leg's summary line
  ends `range whole (…)`. The same branch held at `609cd40b1` and at BASE, so removing `origin`
  from the clone fixes M2's mode at every sha.
- The leg argvs at `e4699ee75` are `bash {prefix}/check-wiring.test.sh`
  (`tools/gate-legs.json@e4699ee75:752`), `bash {prefix}/unattended/check-pass-order.sh`
  (`:1770`) and `python {prefix}/govkit/selftest.py` (`:2515`). The pass-order script takes only
  `--preview` (`tools/unattended/check-pass-order.sh@e4699ee75:241`).
- Pass-order excludes the build folder from build-commit selection (its `the record surface excluded`
  line, `tools/unattended/check-pass-order.sh@e4699ee75:767`). This unit writes only under the
  build folder, so the leg reads it as `unbuilt-in-range` and never as a violation.
- The analysis took M1 at gov `608aa364c` with the same three instruments: 307.7 s, 3,786 git
  processes, peak 524, residue 0, PINNED 2026-11-20
  (`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, §2). It
  estimated M2 at about 11.5k git processes and 1,054 s [PINNED] (§3 row G3), an estimate and not a reading.
- `govkit selftest` is budgeted 1,600 s, from a worst of 7 readings of 1,065 s, PINNED
  (`tools/run-gates/selftest-budgets.txt@e4699ee75:67`).

### The subjects

| Id | Subject | Argv, read from the leg row at the measured sha | Runs | Summary pattern |
|---|---|---|---|---|
| M1 | check-wiring suite | `bash tools/check-wiring.test.sh` | 1 | `.` |
| M2 | pass-order leg | `bash tools/unattended/check-pass-order.sh` | 2, cold then warm | `^pass-order: graded` |
| M3 | govkit suite | `python tools/govkit/selftest.py` | 1 | `.` |
| M4 | nicocares seed suite | read from the nicocares record, never run here | — | — |

A run's argv is the leg row's own at the sha it measures, with `{prefix}` read as `tools`. If a unit
of this build changes a row's argv, A follows the change. A clone made fresh holds no verdict
store, because the store lives under the clone's own git dir, so run 1 of M2 is cold. Run 2 runs in
the same clone with nothing committed between, so it is warm.

### The instrument

The main loop writes this block byte for byte to `qd-measure.sh` in the run's scratch and runs it
there. `<root>` is a short directory under `%TEMP%`, because a fixture clone under the scratchpad
path fails with Filename too long. The instrument removes its root when it finishes.

```bash
#!/usr/bin/env bash
# qd-measure.sh, the instrument of TOOL-dQuietDisk-19. It prints one Readings row per run.
#   bash qd-measure.sh <root> <repo> <sha> <label> <subject> <runs> <summary-ere> [VAR=value ...] -- <argv...>
# <root>      a short absolute directory under %TEMP%; made fresh, and removed at the end
# <runs>      1, or 2 for a cold run then a warm run in one clone, with nothing committed between
# VAR=value   set for the measured command only, which is how A-off holds a switch at today's value
# QD_LOGS     optional: a directory each run's output is copied to
set -u
[ "$#" -ge 9 ] || { echo "qd-measure: too few arguments" >&2; exit 2; }
root=$1 repo=$2 sha=$3 label=$4 subj=$5 runs=$6 summ=$7; shift 7
sets=(); while [ "$#" -gt 0 ] && [ "$1" != "--" ]; do sets+=("$1"); shift; done
[ "${1:-}" = "--" ] || { echo "qd-measure: no -- before the command" >&2; exit 2; }
shift
rm -rf "$root" && mkdir -p "$root" || exit 2
git clone -q --shared --no-checkout "$repo" "$root/c" \
  && git -C "$root/c" checkout -q --detach "$sha" \
  && git -C "$root/c" remote remove origin || { echo "qd-measure: the scratch clone failed" >&2; exit 2; }
for run in $(seq 1 "$runs"); do
  d="$root/r$run"; mkdir -p "$d/t" "$d/trace"; echo 0 >"$d/peak"
  t=$(cygpath -m "$d/t"); tr=$(cygpath -m "$d/trace")
  ( p=0
    while [ ! -e "$d/stop" ]; do
      n=$(find "$d/t" -mindepth 1 2>/dev/null | wc -l)
      [ "$n" -gt "$p" ] && p=$n && echo "$p" >"$d/peak"
      sleep 0.5
    done ) &
  w=$!
  s=$(date +%s%N)
  ( cd "$root/c" && env "${sets[@]}" TEMP="$t" TMP="$t" TMPDIR="$t" GIT_TRACE2_EVENT="$tr" "$@" ) >"$d/out.log" 2>&1
  rc=$?
  e=$(date +%s%N)
  touch "$d/stop"; wait "$w"
  res=$(find "$d/t" -mindepth 1 2>/dev/null | wc -l)
  gp=$(find "$d/trace" -type f | wc -l)
  top=$(find "$d/trace" -type f -exec cat {} + 2>/dev/null | grep -o '"event":"cmd_name"[^}]*' \
    | sed -n 's/.*"name":"\([^"]*\)".*/\1/p' | sort | uniq -c | sort -rn | head -5 \
    | awk '{ printf "%s%s %s", (NR > 1 ? ", " : ""), $2, $1 }')
  last=$(grep -E "$summ" "$d/out.log" | grep -v '^[[:space:]]*$' | tail -1 | cut -c1-200 \
    | tr '\140' "'" | sed 's/|/\\|/g')
  [ -n "${QD_LOGS:-}" ] && cp "$d/out.log" "$QD_LOGS/$label-$subj-$run.log"
  printf '| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n' "$label" "${sha:0:9}" "$subj" \
    "$run" "$rc" "$(( (e - s) / 1000000 ))" "$gp" "$(cat "$d/peak")" "$res" "$top" "$last"
done
rm -rf "$root"
```

What each column counts:
- **git processes** is the number of files under the run's `GIT_TRACE2_EVENT` directory. Git writes
  one file per process into a directory target.
- **peak temp** is the largest entry count under the run's own `TEMP`, sampled every 0.5 s.
- **residual temp** is the entry count left under it after the command exits.
- **wall ms** is the command's own elapsed time. The clone the instrument makes is outside it.

### The calls

Each row set runs serially, one call at a time, never beside a bar or another reading from this
session. `<scratch>` and `<temp>` are spelled absolute by the main loop. `W` is the repository's
common git dir, so the clone reaches every object of the run branch through its alternates.

```bash
I=<scratch>/qd-measure.sh; R=<temp>/qd; S=<the sha this row set is taken at>
W=$(git rev-parse --path-format=absolute --git-common-dir)
bash "$I" "$R" "$W" "$S" B0 M1 1 . -- bash tools/check-wiring.test.sh
bash "$I" "$R" "$W" "$S" B0 M2 2 '^pass-order: graded' -- bash tools/unattended/check-pass-order.sh
bash "$I" "$R" "$W" "$S" B0 M3 1 . -- python tools/govkit/selftest.py
```

For A-off, the label is `A-off`, M2 takes one run, and each switch goes before `--` as `KEY=value`.
The key is the one its unit's spec names and the value is today's behaviour. A switch that a single
run cannot set gets a hand-written row instead: label, sha and subject, `not taken` in the rc cell,
`-` in each number cell, and the key with its reason in the last cell. For A-on, the label is
`A-on` and the calls are as for B0. M2's call is then made a second time, labelled `A-on-again`,
for AC8.

### The record

`memory/builds/dQuietDisk/build/<date>-build-TOOL-dQuietDisk-19-measurements.md`, dated the day the
B0 commit creates it. Its first line after the title is `**Serves:** journal TOOL-dQuietDisk-19`.
Its sections, in this order:

| Section | Written by | Holds |
|---|---|---|
| `## Instrument` | B0 commit | `### The instrument` and the fence above, byte for byte, then the python version and the git version |
| `## Shas` | B0, then A commit | one row per label: the sha, what it is, the date and time taken; the B0 row names `e4699ee75` |
| `## Readings` | B0, then A commit | the header row, then the instrument's rows as printed, AC8's re-take included |
| `## Switches set for A-off` | A commit | one row per key: the unit, the key, the value set, the subjects it governs |
| `## Comparison` | unit pass | the table below |
| `## nicocares seed suite` | unit pass | the `awaiting:` line, until a records commit puts a `source:` line and its readings in its place |
| `## Limits` | unit pass | one line per limit below, and one `rc differs: <subject>` line per pair AC5 finds |

The Readings header is `| label | sha | subject | run | rc | wall ms | git processes | peak temp | residual temp | top git subcommands | last line |`.
The A re-take for AC8 is labelled `A-on-again`, so AC2 does not read it as a second A-on row.

The Comparison header is
`| subject | metric | B0 | A-off | A-on | before is | saved | percent | owning unit | promised bound | met |`.
It has one row per subject and metric: subjects `M1`, `M2 cold`, `M2 warm` and `M3`, and metrics
`wall ms`, `git processes`, `peak temp` and `residual temp`, so sixteen rows. The cells derive this way:
- `M2 cold` reads run 1 at every label. `M2 warm` reads run 2 at B0 and A-on, and A-off's run 1,
  because the leg at today's value has no warm store to read.
- `before is` is `A-off` when that cell holds a number, and `B0` when it reads `not taken`.
- `saved` is the before value less the A-on value.
- `percent` is `saved` over the before value, times 100, rounded as Python 3's `round` rounds, or
  `n/a` when the before value is 0. The two counts it divides stay beside it in the same row.
- `owning unit` is `TOOL-dQuietDisk-10` for M1, `TOOL-dQuietDisk-2` for M2 and `TOOL-dQuietDisk-11`
  for M3.
- `promised bound` quotes, in double quotes, the bound sentence from that unit's spec, as built.
- `met` is `yes` or `no`, by the unit pass's reading of the bound against the A-on value.

### What the comparison means

A-off and A-on read one tree with one history, so the saving between them belongs to this build's
switches alone. B0 is the reading the brief asks for before the first pass, taken where
dWitnessedBar's work is already merged. B0 against A-off moves as well with the history the run
adds, with any default-branch merge the run takes after B0, and with the units that have no
switch. That is why `before is` prefers A-off. Two runs
of the code at one tree is the fix `memory/gotchas/test-oracle-read-from-a-historical-sha.md` names
for a frozen oracle.

### The limits the record states

- Peak temp is a sample every 0.5 s, so it is a lower bound on the true peak.
- Trace2 counts only git processes that inherit `GIT_TRACE2_EVENT`. A fixture that scrubs the
  environment is undercounted, and it is undercounted the same way at every label.
- Wall time is indicative. Other sessions share the host, and this record does not read the load.
- A direct suite run builds no per-bar snapshot, so `TOOL-dQuietDisk-8`'s saving does not show here.
- `TOOL-dQuietDisk-26` carries no switch, so A-off holds its saving as A-on does. M1's saving between
  A-off and A-on is `TOOL-dQuietDisk-10`'s alone; unit 26's shows in B0 against A, beside the history
  the run adds, and in that unit's own acceptance ledger.
- `TOOL-dQuietDisk-9` carries no switch either, so its residual-temp saving shows only in B0
  against A, beside the history the run adds, and in that unit's own AC5.
- Commits folded in after A are not measured.

### Files touched (estimate)

`memory/builds/dQuietDisk/build/` holds the record and is the only path written.

### Alternatives rejected

- B0 at BASE as the only "before". The history and the merged default branch move between BASE and
  A, so B0 against A-on attributes their cost to this build.
- `tools/run-gates/profile_bar.py`. It times a whole bar's legs and runs the bar, which no unit
  may run. It counts no git processes and no temp entries.

## 5. Acceptance criteria

All commands run from the worktree root in Git Bash. `$REC` is the record's path, from
`REC=$(ls memory/builds/dQuietDisk/build/*-build-TOOL-dQuietDisk-19-measurements.md)`. `$SCRATCH`
is the run's scratch directory, spelled absolute. `$P` is `$SCRATCH/qd-probe.py`, written from this
block:

```python
import glob, re, sys
rec = open(sys.argv[1], encoding="utf-8").read()
def section(name):
    m = re.search(r"^## " + re.escape(name) + r"\n(.*?)(?=^## |\Z)", rec, re.S | re.M)
    return m.group(1) if m else ""
def rows(text):
    return [[c.strip() for c in re.split(r"(?<!\\)\|", ln)[1:-1]]
            for ln in text.splitlines() if ln.startswith("| ") and not set(ln) <= set("|-: ")]
read = {}
for r in rows(section("Readings")):
    if r and r[0] in ("B0", "A-off", "A-on"):
        read[(r[0], r[2], r[3])] = r
want = [("B0", "M1", "1"), ("B0", "M2", "1"), ("B0", "M2", "2"), ("B0", "M3", "1"),
        ("A-off", "M1", "1"), ("A-off", "M2", "1"), ("A-off", "M3", "1"),
        ("A-on", "M1", "1"), ("A-on", "M2", "1"), ("A-on", "M2", "2"), ("A-on", "M3", "1")]
for k in want:
    r = read.get(k)
    if r is None:
        print("missing", *k)
    elif len(r) != 11:
        print("bad", *k, "cells", len(r))
    elif r[4] == "not taken":
        if k[0] != "A-off" or not r[10]:
            print("bad", *k, "not taken with no key named")
    elif not all(re.fullmatch(r"\d+", c) for c in r[4:9]):
        print("bad", *k)
col = {"wall ms": 5, "git processes": 6, "peak temp": 7, "residual temp": 8}
src = {"M1": ("M1", "1", "1"), "M2 cold": ("M2", "1", "1"), "M2 warm": ("M2", "2", "1"),
       "M3": ("M3", "1", "1")}
sq = lambda t: " ".join(t.split())
seen = set()
for r in rows(section("Comparison")):
    if not r or r[0] not in src:
        continue
    if len(r) != 11 or r[1] not in col:
        print("bad-comparison-row", r[:2])
        continue
    seen.add((r[0], r[1]))
    s, run, offrun = src[r[0]]
    i = col[r[1]]
    try:
        b0, on, offr = read[("B0", s, run)][i], read[("A-on", s, run)][i], read[("A-off", s, offrun)]
    except KeyError:
        print("missing-reading-for", r[0], r[1])
        continue
    off = "not taken" if offr[4] == "not taken" else offr[i]
    before, is_ = (b0, "B0") if off == "not taken" else (off, "A-off")
    saved = int(before) - int(on)
    pct = "n/a" if int(before) == 0 else str(round(100 * saved / int(before)))
    want_cells = [b0, off, on, is_, str(saved), pct]
    if r[2:8] != want_cells:
        print("cell-mismatch", r[0], r[1], r[2:8], "derived", want_cells)
    spec = glob.glob("memory/builds/dQuietDisk/spec/*-spec-" + r[8] + ".md")
    if (not re.fullmatch(r"TOOL-dQuietDisk-\d+", r[8]) or len(spec) != 1 or not r[9]
            or sq(r[9].strip('"')) not in sq(open(spec[0], encoding="utf-8").read())):
        print("bound-uncited", r[0], r[1], r[8])
for s in src:
    for m in col:
        if (s, m) not in seen:
            print("missing-comparison", s, m)
limits = section("Limits")
for s, run in (("M1", "1"), ("M2", "1"), ("M2", "2"), ("M3", "1")):
    on, off, b0 = read.get(("A-on", s, run)), read.get(("A-off", s, "1")), read.get(("B0", s, run))
    ref = off if off and off[4] != "not taken" else b0
    if on and ref and on[4] != ref[4] and "rc differs: " + s not in limits:
        print("rc-differs-unnamed", s, ref[4], on[4])
print("probe done")
```

- **AC1** — When the block below runs, it prints `spec True record True identical True`.
  Red when: the record carries no `The instrument` fence, or its fence differs from §4's by a byte,
  so a reading was taken by an instrument this spec does not hold.

  ```bash
  python - memory/builds/dQuietDisk/spec/2026-11-20-spec-TOOL-dQuietDisk-19.md "$REC" <<'EOF'
  import re, sys
  def fence(p):
      t = open(p, encoding="utf-8").read()
      m = re.search(r"^#+ The instrument\n.*?^```bash\n(.*?)^```$", t, re.S | re.M)
      return m.group(1) if m else None
  a, b = fence(sys.argv[1]), fence(sys.argv[2])
  print("spec", a is not None, "record", b is not None, "identical", a is not None and a == b)
  EOF
  ```

- **AC2** — When `python "$P" "$REC"` runs, no line it prints begins `missing ` or `bad `. So the
  record holds the eleven B0, A-off and A-on rows, each with integer rc, wall, git, peak and
  residual cells, or an A-off row that reads `not taken` and names its key.
  Red when: a row is absent, a cell holds no integer, or a `not taken` row names no key.
  figure: DERIVED from the record at observation time.
- **AC3** — When the block below runs, it prints `B0 is the build base` and
  `A is one ancestor of HEAD`, and no `late` line.
  Red when: B0 was taken at another sha than the build base `e4699ee75`, the A rows name two shas,
  or a commit of a unit at orders 1 to 6 lands after A, so A does not hold the work it is said to
  measure.

  ```bash
  BASE=$(sed -n 's/^base:[[:space:]]*//p' memory/builds/dQuietDisk/RUN.md | head -1)
  B0=$(awk -F' [|] ' '/^[|] B0 [|]/ { print $2; exit }' "$REC")
  A=$(awk -F' [|] ' '/^[|] A-o(n|ff) [|]/ { print $2 }' "$REC" | sort -u)
  if [ "$B0" = e4699ee75 ] && [ "$(git rev-parse "$B0^2")" = "$(git rev-parse ed833f684)" ]; then
    echo "B0 is the build base"; else echo "B0 is not the build base"; fi
  [ "$(printf '%s\n' "$A" | wc -l)" = 1 ] && git merge-base --is-ancestor "$A" HEAD \
    && echo "A is one ancestor of HEAD"
  git log --format='%H %s' "$BASE..HEAD" | grep -E ' .*TOOL-dQuietDisk-([1-9]|1[0-8]|26)([^0-9]|$)' \
    | while read -r c _; do git merge-base --is-ancestor "$c" "$A" || echo "late $c"; done
  ```

- **AC4** — When `python "$P" "$REC"` runs, it prints no `cell-mismatch`, `missing-comparison`,
  `missing-reading-for` or `bad-comparison-row` line. So every one of the sixteen Comparison rows
  equals the cells re-derived from Readings by §4's rules.
  Red when: a typed cell disagrees with the readings it derives from, or a row is absent.
- **AC5** — When `python "$P" "$REC"` runs, it prints no `rc-differs-unnamed` line. So every
  subject whose A-on rc differs from its before rc has a `rc differs: <subject>` line in Limits.
  Red when: a suite or leg exits differently after the build and the record does not say so.
- **AC6** — When `python "$P" "$REC"` runs, it prints no `bound-uncited` line. So every Comparison
  row names a unit of this build whose spec exists, and quotes a bound that spec's text contains.
  Red when: a row names no unit, or quotes a bound the named spec does not state.
- **AC7** — When the block below runs, it prints `source resolves`, or the `awaiting:` line F1's
  option (b) writes.
  Red when: the section cites a commit or path the nicocares repository does not hold, or carries
  neither line.
  fixture: `C:/projects/nicocares/main`, read with `git cat-file` only. The tree holds no nicocares
  measurement record today.

  ```bash
  sec=$(awk '/^## nicocares seed suite/ { f = 1; next } /^## / { f = 0 } f' "$REC")
  src=$(printf '%s\n' "$sec" | sed -n 's/^source: //p' | head -1)
  if [ -n "$src" ]; then
    repo=${src%%@*}; rest=${src#*@}
    git -C "$repo" cat-file -e "$rest" && echo "source resolves"
  else
    printf '%s\n' "$sec" | grep -m1 '^awaiting: '
  fi
  ```

- **AC8** — When the main loop re-takes the A-on M2 pair with the call
  `bash "$I" "$R" "$W" "$A" A-on-again M2 2 '^pass-order: graded' -- bash tools/unattended/check-pass-order.sh`,
  both rows' git-process cells equal the A-on M2 rows' cells.
  Red when: the counts differ, so the instrument does not repeat and no saving it reports can be
  told from noise.
  permission: the main loop's only. A role agent runs no leg outside its allowlist (M6).
  cost: two runs of the leg, PINNED by the analysis at about 1,054 s each before the build.
- **AC9** — When the block below runs, it prints `name True serves True sections True`.
  Red when: the file is misnamed, its binding line is absent or names another kind, or a §4 section
  is missing, repeated or out of order.

  ```bash
  python - "$REC" <<'EOF'
  import os, re, sys
  p = sys.argv[1]
  t = open(p, encoding="utf-8").read()
  name = re.fullmatch(r"\d{4}-\d{2}-\d{2}-build-TOOL-dQuietDisk-19-measurements\.md", os.path.basename(p))
  serves = "**Serves:** journal TOOL-dQuietDisk-19" in t.splitlines()[:12]
  want = ["Instrument", "Shas", "Readings", "Switches set for A-off", "Comparison",
          "nicocares seed suite", "Limits"]
  print("name", bool(name), "serves", serves, "sections", re.findall(r"^## (.+)$", t, re.M) == want)
  EOF
  ```

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `pass-order history` · `brief-recorded`

`python tools/check-spec-tokens.py --legs-for` over a record under `memory/builds/dQuietDisk/build/`
names `recall floor` and `recall floor arms`, both through the `memory/` guard. The other three are
unguarded. The memory hygiene leg grades the record's filename and binding line, and the two
history legs grade this unit's pass and brief. No arm is added or moved.

## 7. Open questions

- **F1 — What does the nicocares section hold if that session has not recorded its readings when
  this unit's pass runs?**
  The nicocares session takes its own readings (brief `fix4-brief-nicocares.md`, "Measure before
  and after") and writes its landing to `fix4-nicocares-landed.md` in the shared notes folder.
  Neither exists when this spec is written.
  - (a) Hold this unit, BLOCKED, until the nicocares record exists. Every reading is in place, but
    a session outside this run decides when this run can close.
  - (b) Write `awaiting: fix4-nicocares-landed.md`, naming the session and what it owes, and close.
    A records commit adds the readings when they land, and the wrap-up names the row as waiting.
  - (c) Take the seed suite's readings from gov, in a scratch clone of nicocares. That runs a
    suite the brief gives to another session, under another repository's governance.
  Recommendation: (b). Fix 4 is parked in this build (brief item 22), so its numbers are not this
  run's to take or wait on. AC7 is written for both (a) and (b).
  RESOLVED (agent, 2026-11-20, delegated): (b). The section writes
  `awaiting: fix4-nicocares-landed.md`, names the session and what it owes, and the unit closes; a
  records commit adds the nicocares readings when they land.
- **F2 — May the main loop take the M1 and M3 readings while the run is in RUNNING?**
  gate-guard denies a suite only on a branch whose run is before VERIFYING, and a detached clone
  keys nothing (`tools/unattended/gate-guard.js@1252442ee677:708`). The instrument launches each
  suite as an argument, so the hook's text match does not see the call at all.
  - (a) Yes, as the brief orders for B0. The owner's prompt asks for these readings, every reading
    runs in a detached scratch clone, and no reading grades anything.
  - (b) No. Take every suite reading at VERIFYING. This unit would then close before its M1 and M3
    rows exist, and S2 and S3 move to the close.
  - (c) Park it for the owner.
  Recommendation: (a). It is what the prompt and the brief ask for, in the clone the prompt
  prescribes, and the record's Shas section says where each reading ran.
  RESOLVED (agent, 2026-11-20, delegated): (a). The main loop takes the M1 and M3 readings during
  RUNNING, in a detached scratch clone, and this unit moves from order 4 to order 5, after
  TOOL-dQuietDisk-26.

## 8. Revision log

- rev-1 · 2026-11-20 · initial draft from the build's spec brief
  `2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief`, unit 19, with code read at `609cd40b1` and
  BASE. It diverges from the brief in one place: the after readings are the main loop's, because
  the builder role may not run a suite or a leg (§4 Evidence). It also adds A-off, so that the
  saving is read at one tree.
- rev-2 · 2026-11-20 · S3 · S5 · §3 · §4 · AC3 · §7 · F1 resolved (b) and F2 resolved (a) under
  `2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task`. The unit moves to order 5, after
  TOOL-dQuietDisk-26, so A waits for every unit at orders 1 to 4, and AC3's late set is those units.
  The nicocares section writes the `awaiting:` line. The Limits name unit 26's missing switch and
  units 17 and 9, which land after A.
- rev-3 · 2026-11-22 · re-grounded at e4699ee75 (dWitnessedBar's land tip merged), under
  `2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task`. The unit moves from order 5 to order 7,
  after TOOL-dQuietDisk-9 at order 6, so A waits for every unit at orders 1 to 6: S3 says so, the
  §3 bullet and the Limits line that left units 17 and 9 unmeasured are dropped, and AC3's late set
  is every unit at those orders again, 1 to 18 and 26. B0 is taken at `e4699ee75`, the owner's
  build base, and AC3 checks that sha rather than RUN.md's pinned BASE; the Shas row names it. A
  Limits line names unit 9's missing switch, as unit 26's is named. What moved: every §4 Evidence
  citation is re-cited at `e4699ee75` (scratch-guard's suite test to 1740, the no-remote branch to
  1513 and the whole-history range to 1563-1572, the three leg argvs to 752, 1770 and 2515, the
  record-surface line to 767); the builder's gate, the budget row and the shard count did not.
- rev-4 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  4 the analysis's estimated wall time is marked PINNED, as read from that record. Design, scope and
  acceptance unchanged.

## 9. Reuse audit

No existing seam fits. `python tools/codebase-map/reuse_lookup.py "count git processes and temp entries while a suite runs"`
returned name-token neighbours only: `run`, `git`, `run_git` and `scan_processes`. None counts
trace2 files or temp entries. `tools/run-gates/profile_bar.py` is the nearest instrument in the
tree, and it times a whole bar (§4 Alternatives rejected). No file under `tools/`, `skills/` or
`.githooks/` sets `GIT_TRACE2_EVENT` (`git grep -l` at `e4699ee75`). The analysis's §2 readings used
the same three instruments, but its script lived only in that session's scratch. So this record
carries its instrument itself, and the area is dWitnessedBar's (Test: gate health and budgets).

Recall terms used: `python tools/memory-recall/query.py "how did a build record before and after measurements of git processes and suite wall time" --terms "GIT_TRACE2_EVENT git processes wall time before after measurement scratch clone temp entries evidence record"`
