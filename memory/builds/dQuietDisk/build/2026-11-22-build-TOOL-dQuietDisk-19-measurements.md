# TOOL-dQuietDisk-19 — before and after measurements

**Serves:** journal TOOL-dQuietDisk-19

## Instrument

The instrument of TOOL-dQuietDisk-19 §4 "The instrument", byte for byte at its rev-3, run by the main loop:

### The instrument

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

Python 3.15.2 · git 2.54.0.windows.1, on node d.

## Shas

| label | sha | what it is | taken (UTC) |
|---|---|---|---|
| B0 | b3f5a2bc3 | the build base: the merge whose second parent is dWitnessedBar's land tip fb6f1a74c | M1, M2 2026-11-21 22:57 to 23:41; M3 2026-11-21 23:54 to 2026-11-22 01:12 |
| A-on | 1d493fe43 | A: every unit at orders 1 to 6 terminal, the order-7 re-ground committed; the switches at their defaults (W's `main` `35d0dc3ff` sets none) | M1, M2, M3 2026-11-22 14:27 to 16:35 |
| A-on-again | 1d493fe43 | A, M2 re-taken for AC8, between A-on M2 and A-on M3 | 2026-11-22 14:51 to 15:14 |
| A-off | 1d493fe43 | A, M2 and M3 read from the source whose `main` is `198d0fbc1`, one commit on `35d0dc3ff` setting the two keys to today | M2, M3 2026-11-22 16:35 to 18:18 |

## Readings

| label | sha | subject | run | rc | wall ms | git processes | peak temp | residual temp | top git subcommands | last line |
|---|---|---|---|---|---|---|---|---|---|---|
| B0 | b3f5a2bc3 | M1 | 1 | 1 | 350276 | 3772 | 378 | 0 | ls-files 1679, rev-parse 507, check-attr 421, config 398, ls-tree 186 | ---- 247 passed, 8 failed ---- |
| B0 | b3f5a2bc3 | M2 | 1 | 0 | 1057875 | 9319 | 2 | 0 | show 4252, rev-parse 1599, ls-tree 1535, grep 1533, rev-list 165 | pass-order: graded 1709 closed unit(s) · 84 build(s) skipped by the 2026-09-01 cutoff · 50 build(s) graded with no run-state file · 176 unit(s) unbuilt-in-range · 0 pre-anchor violation(s) · 6 wa |
| B0 | b3f5a2bc3 | M2 | 2 | 0 | 1045021 | 9319 | 2 | 0 | show 4252, rev-parse 1599, ls-tree 1535, grep 1533, rev-list 165 | pass-order: graded 1709 closed unit(s) · 84 build(s) skipped by the 2026-09-01 cutoff · 50 build(s) graded with no run-state file · 176 unit(s) unbuilt-in-range · 0 pre-anchor violation(s) · 6 wa |
| B0 | b3f5a2bc3 | M3 | 1 | 1 | 4479811 | 63711 | 73788 | 3526 | ls-files 24462, show 11558, rev-parse 5853, config 5408, cat-file 3282 | govkit-selftest: 96 FAILED — [aRF-1 AC9] the same trailer under [answers] is still refused, [aRF-42 rev-3 AC9] --answers kit.<entry>.<key> agrees with target_context on every overlay and fallback, [ |
| A-on | 1d493fe43 | M1 | 1 | 1 | 267327 | 2047 | 391 | 0 | rev-parse 507, config 368, ls-files 217, check-attr 200, hash-object 178 | ---- 249 passed, 8 failed ---- |
| A-on | 1d493fe43 | M2 | 1 | 0 | 1145863 | 8811 | 4 | 0 | show 3786, rev-parse 1607, ls-tree 1552, grep 1550, rev-list 166 | pass-order: graded 1726 closed unit(s) · 84 build(s) skipped by the 2026-09-01 cutoff · 50 build(s) graded with no run-state file · 176 unit(s) unbuilt-in-range · 0 pre-anchor violation(s) · 6 wa |
| A-on | 1d493fe43 | M2 | 2 | 0 | 38158 | 24 | 5 | 0 | rev-parse 7, show 5, log 3, remote 2, ls-tree 2 | pass-order: graded 1726 closed unit(s) · 84 build(s) skipped by the 2026-09-01 cutoff · 50 build(s) graded with no run-state file · 176 unit(s) unbuilt-in-range · 0 pre-anchor violation(s) · 6 wa |
| A-on | 1d493fe43 | M3 | 1 | 1 | 4812111 | 63475 | 74161 | 0 | ls-files 26103, show 9448, rev-parse 6604, config 4738, cat-file 3487 | govkit-selftest: 96 FAILED — [aRF-1 AC9] the same trailer under [answers] is still refused, [aRF-42 rev-3 AC9] --answers kit.<entry>.<key> agrees with target_context on every overlay and fallback, [ |
| A-on-again | 1d493fe43 | M2 | 1 | 0 | 1269114 | 8811 | 4 | 0 | show 3786, rev-parse 1607, ls-tree 1552, grep 1550, rev-list 166 | pass-order: graded 1726 closed unit(s) · 84 build(s) skipped by the 2026-09-01 cutoff · 50 build(s) graded with no run-state file · 176 unit(s) unbuilt-in-range · 0 pre-anchor violation(s) · 6 wa |
| A-on-again | 1d493fe43 | M2 | 2 | 0 | 37503 | 24 | 5 | 0 | rev-parse 7, show 5, log 3, remote 2, ls-tree 2 | pass-order: graded 1726 closed unit(s) · 84 build(s) skipped by the 2026-09-01 cutoff · 50 build(s) graded with no run-state file · 176 unit(s) unbuilt-in-range · 0 pre-anchor violation(s) · 6 wa |
| A-off | 1d493fe43 | M1 | 1 | not taken | - | - | - | - | - | no switch governs M1: TOOL-dQuietDisk-10 (its F3 (a)), TOOL-dQuietDisk-26 and TOOL-dQuietDisk-9 carry none |
| A-off | 1d493fe43 | M2 | 1 | 0 | 1207712 | 8810 | 4 | 0 | show 3786, rev-parse 1606, ls-tree 1552, grep 1550, rev-list 166 | pass-order: graded 1726 closed unit(s) · 84 build(s) skipped by the 2026-09-01 cutoff · 50 build(s) graded with no run-state file · 176 unit(s) unbuilt-in-range · 0 pre-anchor violation(s) · 6 wa |
| A-off | 1d493fe43 | M3 | 1 | 1 | 4935518 | 64279 | 74668 | 0 | ls-files 26103, show 9448, rev-parse 6604, config 5422, cat-file 3487 | govkit-selftest: 96 FAILED — [aRF-1 AC9] the same trailer under [answers] is still refused, [aRF-42 rev-3 AC9] --answers kit.<entry>.<key> agrees with target_context on every overlay and fallback, [ |

## Switches at A-off

| unit | key | today's value | default | subjects | how A-off held it |
|---|---|---|---|---|---|
| TOOL-dQuietDisk-1 | `tests.history-verdicts` | `regraded` | `stored` | M2, through units 2 and 28 | the source commit `198d0fbc1` on `35d0dc3ff`, whose policy file ends `[tests]`, `history-verdicts = "regraded"`, `fixture-templates = "per-case"`, as the source block printed it |
| TOOL-dQuietDisk-7 | `tests.fixture-templates` | `per-case` | `shared` | M3, through unit 11's cache | the same source commit `198d0fbc1` |
| TOOL-dQuietDisk-18 | `install.baseline` | `run` | `reuse` | none read from the clone | needs no holding: every M3 target that reads it is a fixture the suite writes, alike at both A labels |

## Comparison

Every cell is derived from the Readings table above by TOOL-dQuietDisk-19 §4 "The record", by a Python script in the pass's scratch, never typed. `M2 cold` reads run 1 at every label. `M2 warm` reads run 2 at B0 and A-on, and A-off's run 1, because the leg at today's value keeps no warm store. `before is` reads `A-off` where that cell holds a number, else `B0`. `saved` is the before value less A-on, and `percent` is `saved` over the before value times 100, rounded as Python 3's `round` rounds, `n/a` over a before value of 0. Each bound is quoted from the owning unit's spec at its CLOSED revision. Where that spec states no bound on the row's metric, the row quotes the unit's git-process bound for that run kind, and `met` reads that bound (the Limits name those rows).

| subject | metric | B0 | A-off | A-on | before is | saved | percent | owning unit | promised bound | met |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 | wall ms | 350276 | not taken | 267327 | B0 | 82949 | 24 | TOOL-dQuietDisk-10 | "Under (b) the suite spends at least 32 fewer git processes per run, DERIVED from this table." | yes |
| M1 | git processes | 3772 | not taken | 2047 | B0 | 1725 | 46 | TOOL-dQuietDisk-10 | "Under (b) the suite spends at least 32 fewer git processes per run, DERIVED from this table." | yes |
| M1 | peak temp | 378 | not taken | 391 | B0 | -13 | -3 | TOOL-dQuietDisk-10 | "Peak temp entries do not rise" | no |
| M1 | residual temp | 0 | not taken | 0 | B0 | 0 | n/a | TOOL-dQuietDisk-10 | "the residual temp entries are 0 both times" | yes |
| M2 cold | wall ms | 1057875 | 1207712 | 1145863 | A-off | 61849 | 5 | TOOL-dQuietDisk-2 | "A cold run costs today's per-unit spawns plus 32 store processes, and saves the per-build reads." | yes |
| M2 cold | git processes | 9319 | 8810 | 8811 | A-off | -1 | 0 | TOOL-dQuietDisk-2 | "A cold run costs today's per-unit spawns plus 32 store processes, and saves the per-build reads." | yes |
| M2 cold | peak temp | 2 | 4 | 4 | A-off | 0 | 0 | TOOL-dQuietDisk-2 | "A cold run costs today's per-unit spawns plus 32 store processes, and saves the per-build reads." | yes |
| M2 cold | residual temp | 0 | 0 | 0 | A-off | 0 | n/a | TOOL-dQuietDisk-2 | "The request and answer files sit in `PS_DIR`, so the run leaves no temp entry." | yes |
| M2 warm | wall ms | 1045021 | 1207712 | 38158 | A-off | 1169554 | 97 | TOOL-dQuietDisk-2 | "The main loop takes the unmoved-tip count over the real tree at the close, as TOOL-dQuietDisk-19's M2 after-reading, held to the same 45." | yes |
| M2 warm | git processes | 9319 | 8810 | 24 | A-off | 8786 | 100 | TOOL-dQuietDisk-2 | "The main loop takes the unmoved-tip count over the real tree at the close, as TOOL-dQuietDisk-19's M2 after-reading, held to the same 45." | yes |
| M2 warm | peak temp | 2 | 4 | 5 | A-off | -1 | -25 | TOOL-dQuietDisk-2 | "The main loop takes the unmoved-tip count over the real tree at the close, as TOOL-dQuietDisk-19's M2 after-reading, held to the same 45." | yes |
| M2 warm | residual temp | 0 | 0 | 0 | A-off | 0 | n/a | TOOL-dQuietDisk-2 | "The request and answer files sit in `PS_DIR`, so the run leaves no temp entry." | yes |
| M3 | wall ms | 4479811 | 4935518 | 4812111 | A-off | 123407 | 3 | TOOL-dQuietDisk-11 | "The git process count falls by at least 347" | yes |
| M3 | git processes | 63711 | 64279 | 63475 | A-off | 804 | 1 | TOOL-dQuietDisk-11 | "The git process count falls by at least 347" | yes |
| M3 | peak temp | 73788 | 74668 | 74161 | A-off | 507 | 1 | TOOL-dQuietDisk-11 | "the peak temp entries are below the base's" | yes |
| M3 | residual temp | 3526 | 0 | 0 | A-off | 0 | n/a | TOOL-dQuietDisk-9 | "the directory holds 0 entries after it exits" | yes |

The instrument repeats: the A-on-again M2 rows read 8811 and 24 git processes, the A-on M2 rows' cells (AC8).

## nicocares seed suite

The nicocares session's own record of its seed-suite readings, the dSeededKiln build's measurements file in d41ly/nc, landed on that repository's `main` (`fix4-nicocares-landed.md` in the shared notes). Read here as a committed blob with `git show`, never run from gov.

source: C:/projects/nicocares/main@7b9396cae743d3520c08c9efbd5c64bea494fa79:memory/builds/dSeededKiln/build/measurements.txt

Its rows, copied byte for byte, one JSON object per reading. `before` and `before-churn` are the BASE readings, the `after*` rows the built tree's. The fields are that session's: `git_processes` from `GIT_TRACE2_EVENT`, temp peak and residual from 0.5 s samples, and `py_creates` and `py_deletes` from a Python audit hook.

```text
{"label": "before", "head": "bb2e6543df559ecc145ec540d05330dd9ddbf161", "start": "2026-11-20T12:16:02", "wall_s": 590.8, "exit": 0, "pytest_summary": "598 passed in 587.42s (0:09:47)", "git_processes": 218, "temp_peak": 161, "temp_residual": 145, "temp_top_names_seen": 69, "temp_top_residual": ["pytest-of-d41ly"], "media_added": 1364, "scratch_tmp": "C:/Users/d41ly/AppData/Local/Temp/claude/adb71eb83bee3f7e/594fbd12-f3bb-422b-98ab-d07abd4e01d8/scratchpad/measure/tmp-before-20261120T121602"}
{"label": "after", "head": "8b5ced85b4813ce30dfac60fb68686781a134105", "start": "2026-11-20T12:33:43", "wall_s": 86.0, "exit": 0, "pytest_summary": "598 passed in 84.54s (0:01:24)", "git_processes": 218, "temp_peak": 233, "temp_residual": 88, "temp_top_names_seen": 6, "temp_top_residual": ["pytest-of-d41ly"], "media_added": 0, "scratch_tmp": "C:/Users/d41ly/AppData/Local/Temp/claude/adb71eb83bee3f7e/594fbd12-f3bb-422b-98ab-d07abd4e01d8/scratchpad/measure/tmp-after-20261120T123343"}
{"label": "before-churn", "head": "0ecc3a20d3c2644e695e62c72eb923f472a96474", "start": "2026-11-20T12:49:05", "wall_s": 504.3, "exit": 0, "pytest_summary": "598 passed in 501.45s (0:08:21)", "git_processes": 218, "temp_peak": 161, "temp_residual": 146, "temp_top_names_seen": 68, "temp_top_residual": ["pytest-of-d41ly"], "media_added": 1364, "scratch_tmp": "C:/Users/d41ly/AppData/Local/Temp/claude/adb71eb83bee3f7e/594fbd12-f3bb-422b-98ab-d07abd4e01d8/scratchpad/measure/tmp-before-churn-20261120T124905", "py_creates": 3342, "py_deletes": 2944, "py_processes_counted": 1, "code": "tests/ and scripts/run-core-venv.sh checked out at 4c599687 (BASE) for this run; head names the commit the checkout sat on"}
{"label": "after-churn", "head": "0ecc3a20d3c2644e695e62c72eb923f472a96474", "start": "2026-11-20T12:57:30", "wall_s": 69.7, "exit": 0, "pytest_summary": "598 passed in 68.38s (0:01:08)", "git_processes": 218, "temp_peak": 233, "temp_residual": 87, "temp_top_names_seen": 7, "temp_top_residual": ["pytest-of-d41ly"], "media_added": 0, "scratch_tmp": "C:/Users/d41ly/AppData/Local/Temp/claude/adb71eb83bee3f7e/594fbd12-f3bb-422b-98ab-d07abd4e01d8/scratchpad/measure/tmp-after-churn-20261120T125729", "py_creates": 197, "py_deletes": 202, "py_processes_counted": 1, "code": "the built tree at head, PKG-dSeededKiln-1 and -2"}
{"label": "after-final", "head": "f352fd0fa4a10e6257c7ba1b873ddd93c1ee9f67", "start": "2026-11-20T13:05:01", "wall_s": 72.6, "exit": 0, "pytest_summary": "604 passed in 71.20s (0:01:11)", "git_processes": 218, "temp_peak": 233, "temp_residual": 88, "temp_top_names_seen": 7, "temp_top_residual": ["pytest-of-d41ly"], "media_added": 0, "scratch_tmp": "C:/Users/d41ly/AppData/Local/Temp/claude/adb71eb83bee3f7e/594fbd12-f3bb-422b-98ab-d07abd4e01d8/scratchpad/measure/tmp-after-final-20261120T130501", "py_creates": 206, "py_deletes": 225, "py_processes_counted": 1, "code": "the finished tree, PKG-dSeededKiln-1 to -3"}
{"label": "after-close-fixes", "head": "feb7c890b8fbcd50474bef7a225506e821d837d8", "start": "2026-11-20T13:38:29", "wall_s": 72.6, "exit": 0, "pytest_summary": "604 passed in 71.20s (0:01:11)", "git_processes": 218, "temp_peak": 237, "temp_residual": 88, "temp_top_names_seen": 9, "temp_top_residual": ["pytest-of-d41ly"], "media_added": 0, "scratch_tmp": "C:/Users/d41ly/AppData/Local/Temp/claude/adb71eb83bee3f7e/594fbd12-f3bb-422b-98ab-d07abd4e01d8/scratchpad/measure/tmp-after-close-fixes-20261120T133829", "py_creates": 205, "py_deletes": 225, "py_processes_counted": 1, "code": "the tree with PKG-dSeededKiln-4 applied, uncommitted at the head named"}
```

## Owed by other units

awaiting: TOOL-dQuietDisk-18 AC8, the main loop's at VERIFYING

## Limits

- M3 at B0 ran its argv behind `bash -c 'git branch -q qd-measured HEAD && exec python tools/govkit/selftest.py'`. The suite refuses a working tree that no ref reaches, and the instrument's `remote remove origin` deletes the clone's remote-tracking refs, so a first B0 M3 run refused in 468 ms with 5 git processes. The wrapper adds 1 git process. The A readings take M3 the same way.
- M1 reads 8 failed arms and M3 96 FAILED in the bare scratch clone, which has no `origin` and sits at another path. The clone is the same at every label, so a count compares; a failed arm does not grade this build.
- M2 at B0 reads the same on both runs: today's leg holds no store, so its warm run is a second cold run.
- Wall time is indicative. The B0 readings ran beside this run's own spec and build passes and other sessions' work on the host.
- Peak temp is a sample every 0.5 s, so it is a lower bound on the true peak.
- Wall time is indicative at A too. Other sessions share the host, and this record does not read the load: the A-on and A-on-again M2 cold runs, one tree and one count of 8811 git processes, read 1145863 and 1269114 ms.
- Trace2 counts only git processes that inherit `GIT_TRACE2_EVENT`. A fixture that scrubs the environment is undercounted, and it is undercounted the same way at every label.
- At A, M1 holds one arm, TOOL-dQuietDisk-26's AC1, that points `GIT_TRACE2_EVENT` at its own directory for one `check-wiring.sh --check` (`tools/check-wiring.test.sh@968ec8fd8f5c:420`). That call's git processes are missing from M1's A count, at least 3 (DERIVED from the arm's predicate, which passes only on one `ls-files`, one `ls-tree` and one `check-attr`). B0 has no such arm, so M1's `saved` git processes is high by that call.
- A-off's clone holds as local `main` the A-off source's extra commit, and A-on's holds W's `main` tip. The two differ only in the policy file's `[tests]` table, so every other key reads alike.
- M1's A-off row is `not taken`, so M1's saving is B0 against A-on. It carries the history the run added, the default-branch merge B0 already held, and the units with no switch, as TOOL-dQuietDisk-19 §4 "What the comparison means" says. M1 also runs 2 more arms at A, 249 passed and 8 failed against B0's 247 and 8 (the rows' last line).
- TOOL-dQuietDisk-8 builds no runner snapshot (its F1 (b)). Its per-reader clones show only where M3 reaches one, and the record does not split that out.
- M3 at A makes one owned `gate-work.*` root under the run's `TEMP` (TOOL-dQuietDisk-9). Its peak counts 3 more entries, the root, its owner line and `tmp`, and its git processes 1 more, the root's common-dir read, both DERIVED from `tools/lib/owned_scratch.py#init_owned_tempdir`.
- Commits folded in after A are not measured.
- No owning unit's spec states a wall-time bound, and TOOL-dQuietDisk-2's states no peak-temp bound. So the four `wall ms` rows and the `M2 cold` and `M2 warm` `peak temp` rows quote their unit's git-process bound for that run kind, and their `met` reads that bound, not the row's own metric.
- M1's peak temp is not met: 391 at A-on against 378 at B0, where TOOL-dQuietDisk-10 promises "Peak temp entries do not rise". The pair carries B0 against A's movements, M1's 2 more arms among them, and the record does not split the 13 entries out.
- M2 cold's git processes read 8811 at A-on against 8810 at A-off, 1 more, inside TOOL-dQuietDisk-2's cold cost of today's spawns plus 32 store processes. B0's 9319 is not the before, because B0 against A also moves with the history and the units with no switch.
- M3's residual temp reads 0 at A-off and A-on, so its row saves 0. TOOL-dQuietDisk-9 carries no switch, so its saving shows only as B0's 3526 against A-on's 0, with B0 against A's movements.
- M3's peak temp falls by 507 between A-off and A-on, more than TOOL-dQuietDisk-11's derived "the peak saving is at most 252". Each label is one run sampled every 0.5 s, so the record reads the pair against that unit's "below the base's" alone.
