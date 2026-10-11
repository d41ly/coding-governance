#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-2
# The width A/B of TOOL-aSparedSpawn-2 S1 (AC1): six bars of one leg subset, widths 4, 6 and 8 by
# GATE_JOBS, each quiet and under a declared synthetic spawn load, on a FROZEN clone so no commit
# lands under a running arm. Written by the builder pass and NOT run there: a pass runs no bar. The
# owner runs it, or authorises the main loop to, and commits the rows beside this file.
#
#   bash <this> <frozen-clone> <legs-subset.json> <rows.tsv>
#
# <legs-subset.json> is the owner's F2 pick: a GATE_LEGS manifest of the spawn-heaviest held
# self-test legs. Each arm's row carries wall, leg-seconds, effective concurrency, ceiling fires,
# pause holds, the largest foreign count and the bash count beside the seconds, and the POSITIVE
# ARTIFACT that the arm ran its subject: every leg of the manifest printed a `GATE` verb line. A row
# whose artifact reads `no` measured an arm that exited early and is not a figure. The last row
# records the calibrated pick beside each load's best-wall width.
#
# THE LOAD is AB_LOAD concurrent loops of `true` spawns, armed before the arm's bar and killed by
# pid after it: repeatable, unlike a neighbouring bar.
set -u
clone=${1:?frozen clone}; legs=${2:?legs subset manifest}; rows=${3:?rows file}
AB_LOAD=${AB_LOAD:-8}
legs=$(cd "$(dirname "$legs")" && pwd)/$(basename "$legs")
common=$(git -C "$clone" rev-parse --path-format=absolute --git-common-dir) || exit 2
nlegs=$(python -c 'import json,sys; print(len(json.load(open(sys.argv[1], encoding="utf-8"))))' "$legs") || exit 2
node=$(hostname)
loader=()

arm_loader() { # n — n background loops of `true` spawns, their pids in `loader`
  local i
  for ((i=0; i<$1; i++)); do
    ( while :; do /usr/bin/true; done ) >/dev/null 2>&1 &
    loader+=("$!")
  done
}
remove_loader() {
  [ "${#loader[@]}" -gt 0 ] && kill "${loader[@]}" 2>/dev/null
  wait "${loader[@]}" 2>/dev/null
  loader=()
}
trap remove_loader EXIT

printf 'utc\tnode\tload\twidth\twall_s\tleg_s\teff_conc\tceiling_fires\tpause_holds\tforeign_max\tbash_count\tgate_lines\tlegs\tartifact\n' > "$rows"
declare -A best_w=() best_s=()
for load in quiet loaded; do
  for w in 4 6 8; do
    id="ab-$load-$w-$(date +%s)"
    [ "$load" = loaded ] && arm_loader "$AB_LOAD"
    bashes=$(ps -ef | grep -c '[b]ash')
    t0=$(date +%s)
    ( cd "$clone" && env GATE_TURNSTILE=0 GATE_REUSE= GATE_BASE= GATE_FULL=1 GATE_JOBS="$w" GATE_LEGS="$legs" \
        GATE_RUN_ID="$id" bash tools/run-gates/run-gates.sh ) > "$rows.$id.out" 2>&1
    t1=$(date +%s)
    remove_loader
    rec="$common/gate-run/$id"
    read -r leg_s fires foreign < <(cat "$rec"/*.leg 2>/dev/null | awk -F'\t' '
      { s += $4; if ($2 == "timeout") f++; if ($8 ~ /^[0-9]+$/ && $8 + 0 > m) m = $8 + 0 }
      END { printf "%d %d %d\n", s, f + 0, m + 0 }')
    holds=$(cat "$rec/pauses" 2>/dev/null | wc -l | tr -d ' ')
    gl=$(grep -cE '^GATE [a-z]+ ' "$rows.$id.out")
    wall=$(( t1 - t0 )); [ "$wall" -gt 0 ] || wall=1
    art=no; [ "$gl" -ge "$nlegs" ] && art=yes
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$node" \
      "$load" "$w" "$wall" "$leg_s" "$(awk -v a="$leg_s" -v b="$wall" 'BEGIN { printf "%.2f", a / b }')" \
      "$fires" "$holds" "$foreign" "$bashes" "$gl" "$nlegs" "$art" >> "$rows"
    if [ "$art" = yes ] && { [ -z "${best_s[$load]:-}" ] || [ "$wall" -lt "${best_s[$load]}" ]; }; then
      best_s[$load]=$wall; best_w[$load]=$w
    fi
  done
done
pick=$( cd "$clone" && bash tools/run-gates/run-gates.sh --calibrate-width 2>/dev/null | awk -F'\t' '$1 == "pick" { print $2 }')
printf '# pick %s · best-wall width quiet %s · loaded %s · %s · %s\n' "${pick:-none}" "${best_w[quiet]:-none}" \
  "${best_w[loaded]:-none}" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$node" >> "$rows"
