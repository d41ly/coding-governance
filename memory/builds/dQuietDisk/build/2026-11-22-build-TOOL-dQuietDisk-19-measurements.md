# TOOL-dQuietDisk-19 — before and after measurements

**Serves:** journal TOOL-dQuietDisk-19

## Instrument

The instrument of TOOL-dQuietDisk-19 §4 "The instrument", byte for byte at its rev-3, run by the main loop:

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

## Limits

- M3 at B0 ran its argv behind `bash -c 'git branch -q qd-measured HEAD && exec python tools/govkit/selftest.py'`. The suite refuses a working tree that no ref reaches, and the instrument's `remote remove origin` deletes the clone's remote-tracking refs, so a first B0 M3 run refused in 468 ms with 5 git processes. The wrapper adds 1 git process. The A readings take M3 the same way.
- M1 reads 8 failed arms and M3 96 FAILED in the bare scratch clone, which has no `origin` and sits at another path. The clone is the same at every label, so a count compares; a failed arm does not grade this build.
- M2 at B0 reads the same on both runs: today's leg holds no store, so its warm run is a second cold run.
- Wall time is indicative. The B0 readings ran beside this run's own spec and build passes and other sessions' work on the host.
- Peak temp is a sample every 0.5 s, so it is a lower bound on the true peak.
