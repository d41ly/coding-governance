#!/usr/bin/env bash
# foreign-prefix.gov.test.sh — does every declared self-test still FIND ITS SUBJECT once gov's tool
# root sits at a foreign prefix? TOOL-aRepatriatedFork-52, which redesigned TOOL-aRepatriatedFork-30
# S1's leg (a calibrate pass plus three pooled runs of every suite whole, hours long and silent) so
# that it asks only that question.
#
#   bash <prefix>/run-gates/foreign-prefix.gov.test.sh [--kit <substring>] [--plan]
#
# `--plan` prints each row's kind and the dispatch order at gov's own prefix, runs the stale
# declaration guard, and exits: no clone, no move, no suite run (TOOL-aSparedSpawn-10 S4).
#
# WHY. The install-prefix ban grades the SPELLING of kit paths. Whether a suite still RUNS once its
# tool root sits somewhere else is a different question, and only running it there answers it: a
# suite whose prologue finds its subject through a literal prefix passes every text check and fails
# at the first prefix it was not written for. Its prologue and ONE arm that touches its subject are
# enough to ask that, and the rest of its arms are the bar's business at gov's own prefix.
#
# HOW, and every step reads an existing seam.
#   1. A scratch clone of this repository at HEAD, under `mktemp -d`, deleted on exit.
#   2. THE BASELINE is the bar's own record, never a calibrate: the newest `<git-dir>/gate-run/<id>/`
#      whose header names HEAD with `tree_clean yes`. A row red there is named once and not graded at
#      a foreign prefix, because the bar's own leg for it already reds. No such record: every row is
#      expected green, and that is said once.
#   3. THE MOVE. The whole tool root moves with `git mv` to `scripts/`, then `vendor/gov/`, then the
#      repository root (TOOL-aRepatriatedFork-30 §8 F1 (b)), each from a fresh reset. gov's own
#      declarations move with it, re-spelled by the old root's path head as an install at that
#      prefix carries them (`write_declarations`, VERIFYING repair R2's patch). The budget file and the
#      leg manifest move and are otherwise byte-identical to HEAD, which is asserted.
#   4. THE POPULATION is every row `run-selftests.sh --list` prints AT THAT PREFIX, with the argv it
#      prints there, less this leg's own row, skipped while iterating rather than edited out.
#   5. THE PROBE. Each row runs with FOREIGN_PREFIX_PROBE=1, which every suite honours by stopping
#      after its first subject-touching arm with the line `foreign-prefix-probe: stopped after 1 arm`,
#      in a pool of the width `run-gates.sh --print-profile` reports, each killed as a HANG at HANG_FACTOR
#      times its declared budget. One line per row as it completes is the progress, and the heartbeat a registered run
#      reads. A row is green when it exits 0 and, unless declared whole below, printed the marker.
#      SHARDED FAMILIES are DERIVED, never declared: rows whose argv ends `--shard <i>/<n>` and is
#      otherwise identical are one family, and one row of each is probed. Every other row prints
#      `represented · by shard <k>/<n>`, a skip that announces itself and is counted neither graded
#      nor passed. The representative ROTATES BY COMMIT: HEAD's sha as an integer, mod the family's
#      selected size, picks a row in shard order; and when the version marker of the suite's kit (the
#      line its `kit.toml` `version_from` names) differs from HEAD's first parent's, every shard is
#      probed, since a bump is when a prefix defect is likeliest to ship (TOOL-aSparedSpawn-10 §8 F1
#      (a)). Each family prints the rule's input and its answer on every run.
#   6. FAIL FAST at the PREFIX grain (§8 F3 (a)): a red prefix is finished, so every red row at it is
#      named in one run, then each later prefix prints `not run`. The clone must be clean after each
#      prefix, or the leg reds naming what a suite wrote outside its scratch.
#
# WHOLE-RUN ROWS are DECLARED in `WHOLE_RUN` below with a reason (§8 F4 (b)), and red in both
# directions: a declared row that prints the probe marker is a stale declaration, and an undeclared
# row that prints none is an undeclared whole run. Every declared row is printed on every run.
# Whole rows enter the SAME pool as the probes, ahead of them and longest budget first, each bounded
# by `run_row`'s load-scaled hang guard like any other row: their budget is a hang guard here and not
# a cost verdict, so nothing is gained by holding them for a serial tail (TOOL-aSparedSpawn-10 S3).
#
# WHAT THIS DOES NOT CHECK:
#   * HISTORY-BOUND arms — govkit selftest's vintage arms, say, which read gov's history at its
#     historical prefix. They are outside the prefix question by construction, and a probe that stops
#     after one arm does not reach them;
#   * whether a suite's probe arm TOUCHES ITS SUBJECT. Where the honouring site sits is that suite's
#     claim, and nothing here grades it; a site placed before the subject runs passes vacuously;
#   * GOV'S OWN PREFIX, which is never probed here: the bar runs every suite there;
#   * a declaration naming the old root in any spelling but its PATH HEAD — `tools/` followed by a
#     path. Those keep gov's spelling at every prefix, and the record corpus is never re-spelled;
#   * an ADOPTER's tree. This moves GOV, it installs into nobody's repository: `govkit apply` has its
#     own suites, and an apply target lacks the records and withheld suites this leg runs;
#   * EVERY SHARD of a sharded suite. Each shard's probe runs the prologue plus the first arm of its
#     own region, so a shard-specific prefix defect in a region's first arm is seen only when that
#     region's shard is the representative — rotation reaches each within about n landings, and a
#     kit version bump probes them all.
# COST: one prologue and one arm per suite per prefix, one shard per sharded family, whole rows
# pooled beside the probes; minutes, and held, run once per build.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "foreign-prefix: not inside a git work tree"; exit 2; }
# The tool root and this kit's directory name, DERIVED. Moving the tool root is the whole leg, so
# a literal here would be the one path it could never move.
if ! TROOT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE/.." rev-parse --show-prefix 2>/dev/null); then
  echo "foreign-prefix: cannot derive the tool root above $HERE — REFUSING"; exit 2
fi
TROOT=${TROOT%/}
KIT=$(basename "$HERE")
if [ -z "$TROOT" ]; then
  echo "foreign-prefix: gov sits at the repo root here, so there is no tool root to move — REFUSING"
  echo "foreign-prefix: rather than grading a relocation that cannot be performed."
  exit 2
fi
# The python-launcher resolver, INLINED byte-identically from the canonical copy named on its
# marker line: a bare launcher name is not an answer on a host with the Store stub.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
SELF_ROW="foreign-prefix parity (every self-test at three prefixes)"
FLOOR_ASSERTIONS=3
MARKER="foreign-prefix-probe: stopped after 1 arm"
# THE WHOLE-RUN DECLARATION, `row|reason`. A row here runs whole at every prefix and must NOT print
# the marker; a row absent from here must print it. Both directions red.
WHOLE_RUN=(
  "backlog migration selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "build-index selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "check-arms selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "corpus-ids selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "gotchas selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "row-grammar selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "settings-merge selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "shell-hygiene selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "playbook render selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "review-replay selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "held-halves selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "roles render selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "routed-commits selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing"
  "tier2-review self-test|its arms run inside ONE node process, which no shell site can stop between arms"
)
# THE GOV-LAYOUT DECLARATION, `row|reason` (S3, rev-6). An unshipped suite whose first arm grades
# gov's own registry layout, which gov at the repo root is not. Not graded at the root, printed there.
GOV_LAYOUT=(
  "govkit selftest|its first arm is selfcheck over gov's own registry; govkit ships to no adopter, and gov at the repo root is no layout gov has"
)
FILTER=""; PLAN=0
while [ $# -gt 0 ]; do
  case "$1" in
    --kit) FILTER=${2:-}; [ -n "$FILTER" ] || { echo "foreign-prefix: --kit takes a substring"; exit 2; }; shift 2 ;;
    --plan) PLAN=1; shift ;;
    *) echo "usage: bash $0 [--kit <substring>] [--plan]"; exit 2 ;;
  esac
done

fails=0; passed=0
print_fail() { fails=$((fails+1)); printf 'FAIL  %s\n' "$*"; }
print_pass() { passed=$((passed+1)); printf 'ok    %s\n' "$*"; }
HEADSHA=$(git -C "$ROOT" rev-parse HEAD) || exit 2

# ---- THE POPULATION AND ITS KINDS, S1 to S4 (TOOL-aSparedSpawn-10). ONE classifier for `--plan` and
# the run: the `--list` text becomes row arrays, each row gets its kind (probe, whole or represented),
# and the dispatch order is derived from the kinds. `--kit` filters BEFORE families are formed, so a
# filtered run's family is the rows it selected.
R_NAME=(); R_BOUND=(); R_ARGV=(); R_KIND=(); R_REP=(); ORDER=()
declare -A KIT_BUMP=() FAM_WANT=()
load_population() { # $1 = the `--list` text -> R_NAME R_BOUND R_ARGV, less this leg's own row and every row --kit leaves out
  local name bound argv
  R_NAME=(); R_BOUND=(); R_ARGV=()
  while IFS=$'\t' read -r -u 3 name bound argv; do
    [ -n "$name" ] || continue
    [ "$name" = "$SELF_ROW" ] && continue
    if [ -n "$FILTER" ]; then case "$name $argv" in *"$FILTER"*) ;; *) continue ;; esac; fi
    R_NAME+=("$name"); R_BOUND+=("$bound"); R_ARGV+=("$argv")
  done 3< <(printf '%s\n' "$1" | sed -nE 's/^  (.*[^ ]) +([0-9]+)s  (.+)$/\1\t\2\t\3/p')
  return 0
}

read_kit_marker() { # $1 = revision, $2 = kit directory under gov's tool root -> the version marker line its kit.toml names; 1 when it names none
  local toml file pat re=$'(^|\n)version_from[^"\n]*"([^"]+)"[^"\n]*"([^"]+)"'
  toml=$(git -C "$ROOT" show "$1:$TROOT/$2/kit.toml" 2>/dev/null) || return 1
  [[ $toml =~ $re ]] || return 1
  file=${BASH_REMATCH[2]}; pat=${BASH_REMATCH[3]}
  git -C "$ROOT" show "$1:$TROOT/$2/$file" 2>/dev/null | grep -m1 -E -- "$pat"
  return 0
}

derive_row_kinds() { # $1 = label, $2 = prefix (empty for the root) -> R_KIND R_REP FAM_WANT, and one rule line per sharded family
  local label="$1" p="$2" j k w key stem arity m r x kit path now was bump rep rep_label
  local -A fam=() seen=()
  local -a members
  R_KIND=(); R_REP=(); FAM_WANT=()
  for j in "${!R_NAME[@]}"; do
    R_KIND[j]=probe; R_REP[j]=""
    for w in "${WHOLE_RUN[@]}"; do [ "${w%%|*}" = "${R_NAME[j]}" ] && R_KIND[j]=whole; done
    [ "${R_KIND[j]}" = probe ] || continue
    [[ ${R_ARGV[j]} =~ ^(.*)\ --shard\ ([0-9]+)/([0-9]+)$ ]] || continue
    fam["${BASH_REMATCH[1]} ${BASH_REMATCH[3]}"]+=" ${BASH_REMATCH[2]}:$j"
  done
  for j in "${!R_NAME[@]}"; do
    [ "${R_KIND[j]}" = probe ] || continue
    [[ ${R_ARGV[j]} =~ ^(.*)\ --shard\ ([0-9]+)/([0-9]+)$ ]] || continue
    stem=${BASH_REMATCH[1]}; arity=${BASH_REMATCH[3]}; key="$stem $arity"
    [ -z "${seen[$key]+x}" ] || continue
    seen[$key]=1
    # The family's rows in SHARD order, whatever order the population listed them in.
    members=()
    for ((k = 1; k <= arity; k++)); do
      for w in ${fam[$key]}; do [ "${w%%:*}" = "$k" ] && members+=("${w#*:}"); done
    done
    m=${#members[@]}
    # The suite's kit: the first path word, less the prefix, up to its first slash.
    kit=""
    for w in $stem; do case "$w" in *.sh|*.py) path=${w#"${p:+$p/}"}; kit=${path%%/*}; break ;; esac; done
    if [ -z "${KIT_BUMP[$kit]+x}" ]; then
      if ! git -C "$ROOT" rev-parse -q --verify "$HEADSHA^1" >/dev/null 2>&1; then
        KIT_BUMP[$kit]="yes|HEAD has no first parent to compare kit '$kit's version marker with"
      elif ! now=$(read_kit_marker "$HEADSHA" "$kit") || [ -z "$now" ]; then
        KIT_BUMP[$kit]="no|kit '$kit' declares no version marker at HEAD, so the rotation alone decides"
      else
        was=$(read_kit_marker "$HEADSHA^1" "$kit")
        if [ "$now" = "$was" ]; then KIT_BUMP[$kit]="no|kit '$kit' version marker unchanged since HEAD's first parent ($now)"
        else KIT_BUMP[$kit]="yes|kit '$kit' version marker moved since HEAD's first parent (${was:-absent} -> $now)"; fi
      fi
    fi
    bump=${KIT_BUMP[$kit]}
    if [ "${bump%%|*}" = yes ]; then
      FAM_WANT[$key]=$m
      echo "foreign-prefix: [$label] family '$stem' · $m shard row(s) · ${bump#*|} · every shard is probed"
      continue
    fi
    # HEAD's sha as an integer, mod the family's selected size, one hex digit at a time: no fork.
    r=0; x=$HEADSHA
    while [ -n "$x" ]; do r=$(( (r * 16 + 16#${x:0:1}) % m )); x=${x:1}; done
    rep=${members[r]}
    [[ ${R_ARGV[rep]} =~ --shard\ ([0-9]+/[0-9]+)$ ]] && rep_label=${BASH_REMATCH[1]}
    FAM_WANT[$key]=1
    for w in "${members[@]}"; do
      [ "$w" = "$rep" ] && continue
      R_KIND[w]=represented; R_REP[w]=$rep_label
    done
    echo "foreign-prefix: [$label] family '$stem' · rule input HEAD $HEADSHA as an integer mod $m = $r · ${bump#*|} · probes shard $rep_label, represents the other $((m - 1))"
  done
  return 0
}

derive_dispatch_order() { # -> ORDER: every whole row by descending budget (list order on a tie), then every probe row in list order
  local j k
  ORDER=()
  for j in "${!R_NAME[@]}"; do
    [ "${R_KIND[j]}" = whole ] || continue
    k=${#ORDER[@]}; ORDER+=("$j")
    while [ "$k" -gt 0 ] && [ "${R_BOUND[ORDER[k-1]]}" -lt "${R_BOUND[j]}" ]; do ORDER[k]=${ORDER[k-1]}; k=$((k - 1)); done
    ORDER[k]=$j
  done
  for j in "${!R_NAME[@]}"; do
    if [ "${R_KIND[j]}" = probe ]; then ORDER+=("$j"); fi
  done
  return 0
}

check_declarations() { # -> a FAIL per WHOLE_RUN or GOV_LAYOUT entry naming no row of the loaded population; skipped under --kit
  # A STALE DECLARATION reds too: a whole-run row naming no row in the population exempts nothing.
  local names w
  [ -z "$FILTER" ] || return 0
  printf -v names '%s\n' "${R_NAME[@]}"
  for w in "${WHOLE_RUN[@]}"; do
    printf '%s\n' "$names" | grep -qxF "${w%%|*}" || print_fail "a whole-run declaration names no row in the population: ${w%%|*}"
  done
  for w in "${GOV_LAYOUT[@]}"; do
    printf '%s\n' "$names" | grep -qxF "${w%%|*}" || print_fail "a gov-layout declaration names no row in the population: ${w%%|*}"
  done
  return 0
}

print_plan() { # -> the dispatch order and every represented row, then a count of each family's probes against the rule's answer
  local j k pos=0 rep=0 key
  local -A got=()
  for j in "${ORDER[@]}"; do
    pos=$((pos + 1)); printf '[plan] %s. %s · %s · %ss budget\n' "$pos" "${R_NAME[j]}" "${R_KIND[j]}" "${R_BOUND[j]}"
  done
  for j in "${!R_NAME[@]}"; do
    if [ "${R_KIND[j]}" = represented ]; then rep=$((rep + 1)); printf '[plan] %s · represented · by shard %s\n' "${R_NAME[j]}" "${R_REP[j]}"; fi
    [ "${R_KIND[j]}" != whole ] || continue
    [[ ${R_ARGV[j]} =~ ^(.*)\ --shard\ [0-9]+/([0-9]+)$ ]] || continue
    key="${BASH_REMATCH[1]} ${BASH_REMATCH[2]}"; got[$key]=${got[$key]:-0}
    [ "${R_KIND[j]}" = probe ] && got[$key]=$((got[$key] + 1))
  done
  for key in "${!got[@]}"; do
    [ "${got[$key]}" = "${FAM_WANT[$key]:-1}" ] || print_fail "the family '${key% *}' has ${got[$key]} probe row(s) where the rule answers ${FAM_WANT[$key]:-1}"
  done
  [ $(( ${#ORDER[@]} + rep )) = "${#R_NAME[@]}" ] || print_fail "the plan names $(( ${#ORDER[@]} + rep )) of the ${#R_NAME[@]} selected row(s), so a row is neither dispatched nor represented"
  [ "${#R_NAME[@]}" -gt 0 ] || print_fail "at gov's own prefix the population selected no row${FILTER:+ matching '$FILTER'}, so a run would grade nothing"
  echo "foreign-prefix: plan — ${#R_NAME[@]} selected row(s): ${#ORDER[@]} dispatched, $rep represented; no clone was made and no suite ran"
  return 0
}

if [ "$PLAN" = 1 ]; then
  cd "$ROOT" || exit 2
  echo "foreign-prefix: plan at ${HEADSHA:0:8} for gov's own prefix '$TROOT'${FILTER:+, rows matching '$FILTER'}"
  if ! list=$(bash "$TROOT/$KIT/run-selftests.sh" --list 2>&1); then
    echo "foreign-prefix: run-selftests.sh --list refused at gov's prefix — REFUSING to plan from no population"; exit 2
  fi
  load_population "$list"
  check_declarations
  derive_row_kinds plan "$TROOT"
  derive_dispatch_order
  print_plan
  [ "$fails" = 0 ] || { echo "FAIL — $fails check(s) failed"; exit 1; }
  exit 0
fi

PY=$(resolve_python) || exit 2
WIDTH=$(bash "$HERE/run-gates.sh" --print-profile 2>/dev/null | awk -F'\t' '$1 == "width" { print $2 }')
case "$WIDTH" in ''|*[!0-9]*|0) echo "foreign-prefix: run-gates.sh --print-profile reported no pool width ('$WIDTH') — REFUSING"; exit 2 ;; esac
TMPD=$(mktemp -d) || { echo "foreign-prefix: mktemp failed"; exit 2; }
[ "${GOV_FOREIGN_KEEP:-0}" = 1 ] || trap 'rm -rf "$TMPD"' EXIT
G="$TMPD/g"
git clone -q --no-hardlinks "$ROOT" "$G" || { echo "foreign-prefix: could not clone $ROOT"; exit 2; }
cd "$G" || exit 2
# A named branch, not a detached HEAD: govkit's self-test pins a vintage some ref contains.
git checkout -q -B foreign-prefix "$HEADSHA" || { echo "foreign-prefix: the clone cannot check out HEAD $HEADSHA"; exit 2; }
git config user.email foreign-prefix@gov.test; git config user.name foreign-prefix
BASE=$HEADSHA
echo "foreign-prefix: clone of ${HEADSHA:0:8} at $G, tool root '$TROOT', pool width $WIDTH${FILTER:+, rows matching '$FILTER'}"
echo "foreign-prefix: this leg's own row is skipped at every prefix: $SELF_ROW"
for w in "${WHOLE_RUN[@]}"; do echo "foreign-prefix: declared whole run — ${w%%|*}: ${w#*|}"; done
for w in "${GOV_LAYOUT[@]}"; do echo "foreign-prefix: declared gov layout, not graded at the repo root — ${w%%|*}: ${w#*|}"; done

# ---- THE BASELINE, S5. Read from the HOST's git dir, where the bar wrote it; the clone has none.
INHERITED="$TMPD/inherited.txt"; : > "$INHERITED"
load_baseline() {
  local gd h best="" best_at="" head clean at d f n st
  gd=$(git -C "$ROOT" rev-parse --absolute-git-dir 2>/dev/null) || return 0
  for h in "$gd"/gate-run/*/header; do
    [ -f "$h" ] || continue
    head=$(awk -F'\t' '$1 == "head" { print $2 }' "$h"); clean=$(awk -F'\t' '$1 == "tree_clean" { print $2 }' "$h")
    at=$(awk -F'\t' '$1 == "started" { print $2 }' "$h")
    [ "$head" = "$HEADSHA" ] && [ "$clean" = yes ] || continue
    if [ -z "$best" ] || [[ "$at" > "$best_at" ]]; then best=$(dirname "$h"); best_at=$at; fi
  done
  if [ -z "$best" ]; then
    echo "foreign-prefix: no recorded bar run covers this tree (${HEADSHA:0:8}, tree_clean yes), so every row is expected green"
    return 0
  fi
  echo "foreign-prefix: baseline is bar run $(basename "$best") at ${HEADSHA:0:8}"
  for f in "$best"/*.leg; do
    # A `.tail.leg` is a tail retry the runner set aside, never a first attempt (TOOL-aSparedSpawn-3).
    case "$f" in *.retry.leg|*.tail.leg) continue ;; esac
    [ -f "$f" ] || continue
    IFS=$'\t' read -r n st _ < "$f"
    d="${f%.leg}.retry.leg"
    [ -f "$d" ] && IFS=$'\t' read -r _ st _ < "$d"
    [ "$st" = ok ] && continue
    printf '%s\n' "$n" >> "$INHERITED"
    echo "foreign-prefix: [$TROOT] $n · red ($st) in bar run $(basename "$best") at gov's prefix, so it is not graded at a foreign prefix"
  done
}
load_baseline

# ---- THE MOVE, S4.
set_tool_root() { # $1 = the new prefix, empty for the repo root
  local to="$1" c
  case "$to" in
    "") for c in $(git ls-tree --name-only HEAD "$TROOT/" | sed "s|^$TROOT/||"); do
          [ -e "$c" ] && { echo "foreign-prefix: '$c' already exists at the repo root, so the root move would collide"; return 1; }
          git mv "$TROOT/$c" "$c" || return 1
        done ;;
    *) mkdir -p "$(dirname "$to")"; git mv "$TROOT" "$to" || return 1 ;;
  esac
  write_declarations "$to" || return 1
  git add -A && git commit -q -m "foreign-prefix: tool root at ${to:-the repo root}, gov's declarations with it"
}

write_declarations() { # $1 = the new prefix, empty for the repo root; the move is STAGED, not committed
  # GOV'S OWN DECLARATIONS MOVE WITH ITS TOOL ROOT, as an install at that prefix carries them: the
  # charter, `.claude/`, the hook config's GOV_KITROOT, the conf files, the map, the waiver registries
  # and the renders the install-prefix gate lists. Left naming the old root they made the first whole
  # run red on rows that read them (both pre-push suites, the gov canary, the build harness, the map)
  # for an install no adopter has (TOOL-aRepatriatedFork-30, gate repair at VERIFYING). NOTHING ELSE
  # the move brought in is touched, so a literal an engine or a suite carries still reds where it
  # should, and the record corpus keeps the history it recorded.
  local to="$1" renders
  renders=$(bash "${to:+$to/}check-install-prefix.sh" --list 2>/dev/null | awk '$1 == "render" { print $2 }')
  [ -n "$renders" ] || { echo "foreign-prefix: the install-prefix gate listed no render at ${to:-the repo root} — REFUSING to re-spell blind"; return 1; }
  git diff --cached --no-renames --name-only --diff-filter=A > "$TMPD/moved.txt"
  printf '%s\n' "$renders" > "$TMPD/renders.txt"
  "$PY" -c '
import re, subprocess, sys
old, new, moved_f, renders_f = sys.argv[1:5]
head = new + "/" if new else ""
moved = set(open(moved_f, encoding="utf-8").read().split())
renders = set(open(renders_f, encoding="utf-8").read().split()) & moved
records = ("memory/builds/", "memory/archive/", "memory/ledger/", "memory/backlog/", "memory/DECISIONS.md")
path = re.compile(rb"(?<![A-Za-z0-9_.~-])" + re.escape(old.encode()) + rb"/")
kitroot = re.compile(rb"^(GOV_KITROOT=)" + re.escape(old.encode()) + rb"[ \t]*$", re.M)
n = 0
for f in subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True).stdout.decode("utf-8").split("\0"):
    if not f or f.startswith(records) or (f in moved and f not in renders):
        continue
    try:
        b = open(f, "rb").read()
    except OSError:
        continue
    if b"\0" in b:
        continue
    r = path.sub(head.encode(), kitroot.sub(rb"\g<1>" + (new.encode() or b"."), b))
    if r != b:
        open(f, "wb").write(r)
        n += 1
print("foreign-prefix: %d declaration file(s) re-spelled from %s/ to %s" % (n, old, head or "the repo root"))
if not n:
    sys.exit("foreign-prefix: nothing re-spelled, so the moved tree still names the old root")
' "$TROOT" "$to" "$TMPD/moved.txt" "$TMPD/renders.txt"
}

# ---- ONE ROW, S6. Writes its verdict file and prints its one line as it completes.
# THE BUDGET IS A HANG GUARD HERE, NOT A COST VERDICT (TOOL-aMeteredSweep-1). This leg asks whether a
# suite passes at another prefix; whether it fits its budget is `run-selftests.sh --serial`'s question,
# asked on a quiet host. Each budget is a quiet reading, and inside a loaded bar six rows overran theirs
# at all three prefixes while every one of them was passing. A row is killed at HANG_FACTOR times its
# budget, and that kill reads as a hang, which is the only thing this bound now claims.
#
# AND THE FACTOR SCALES WITH THE HOST'S LOAD, measured, never assumed. Three times a quiet budget still
# killed a passing row beside another repository's bar, so each prefix first times ten spawns and
# divides by the runner's own recorded floor, `<git-common-dir>/gate-spawn-floor` (the HOST rule's
# reading, of the repository under test and never of the scratch clone), rounding up and capping at
# LOAD_RATIO_MAX. No floor, or one that will not read, leaves the
# ratio at 1 and says so: an unmeasured host is never scaled by a guess.
HANG_FACTOR=3
LOAD_RATIO=1; LOAD_RATIO_MAX=20; LOAD_NOTE=""
measure_load_ratio() {
  local f floor whole frac floor_us t0 t1 k bin cur
  LOAD_RATIO=1
  f="$(git -C "$ROOT" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)/gate-spawn-floor"
  { IFS=$'\t' read -r floor _ < "$f"; } 2>/dev/null || { LOAD_NOTE="no spawn floor at $f, so every hang bound is unscaled"; return 0; }
  case "$floor" in [0-9]*.[0-9][0-9][0-9]) ;; *) LOAD_NOTE="the spawn floor at $f does not read, so every hang bound is unscaled"; return 0 ;; esac
  whole=${floor%.*}; frac=${floor#*.}; floor_us=$(( 10#$whole * 1000 + 10#$frac ))
  bin=$(type -P true 2>/dev/null); t0=${EPOCHREALTIME//[.,]/}
  { [ -n "$bin" ] && [ -n "$t0" ] && [ "$floor_us" -gt 0 ]; } || { LOAD_NOTE="no spawn could be timed, so every hang bound is unscaled"; return 0; }
  for k in 1 2 3 4 5 6 7 8 9 10; do "$bin" </dev/null >/dev/null 2>&1; done
  t1=${EPOCHREALTIME//[.,]/}; cur=$(( (10#$t1 - 10#$t0) / 10 ))
  LOAD_RATIO=$(( (cur + floor_us - 1) / floor_us ))
  [ "$LOAD_RATIO" -ge 1 ] || LOAD_RATIO=1
  [ "$LOAD_RATIO" -le "$LOAD_RATIO_MAX" ] || LOAD_RATIO=$LOAD_RATIO_MAX
  LOAD_NOTE="a spawn costs ${cur} us now against this clone's floor of ${floor_us} us, so every hang bound is x${LOAD_RATIO}"
}
run_row() { # $1 = prefix label, $2 = run dir, $3 = row, $4 = budget seconds, $5 = argv, $6 = probe|whole
  local d="$2" rc s marked=0 v=ok why="" x=$(( HANG_FACTOR * LOAD_RATIO ))
  mkdir -p "$d/tmp"
  s=$SECONDS
  FOREIGN_PREFIX_PROBE=1 SELFTEST_INNER_WIDTH=1 TMPDIR="$d/tmp" timeout -k 5 "$(( $4 * x ))" bash -c "$5" > "$d/out" 2>&1
  rc=$?
  grep -qxF "$MARKER" "$d/out" && marked=1
  if [ "$rc" = 124 ] || [ "$rc" = 137 ]; then v=red; why="a hang: killed at ${x}x its $4 s budget (${HANG_FACTOR}x, load x${LOAD_RATIO})"
  elif [ "$rc" != 0 ]; then v=red; why="exit $rc"
  elif [ "$6" = probe ] && [ "$marked" = 0 ]; then v=red; why="an undeclared whole run: it printed no probe marker, so it ran every arm"
  elif [ "$6" = whole ] && [ "$marked" = 1 ]; then v=red; why="a stale whole-run declaration: it printed the probe marker"
  fi
  printf '[%s] %s · %s · rc %s · %ss%s\n' "$1" "$3" "$6" "$rc" "$((SECONDS - s))" "${why:+ · RED, $why}"
  printf '%s\t%s\n' "$v" "$why" > "$d/verdict"
}

run_at_prefix() { # $1 = prefix, empty for the repo root; returns 1 when the prefix is red
  local p="$1" label="${1:-root}" list n=0 i=0 r=0 live=0 j name bound argv kind red=0 d v why dirty b0 b1 f note=""
  git reset -q --hard "$BASE" && git clean -qfdx
  measure_load_ratio; echo "foreign-prefix: [$label] $LOAD_NOTE"
  if ! set_tool_root "$p"; then print_fail "could not move the tool root to ${p:-the repo root}"; return 1; fi
  for f in "$KIT/selftest-budgets.txt" gate-legs.json; do
    b0=$(git rev-parse "$BASE:$TROOT/$f" 2>/dev/null); b1=$(git rev-parse "HEAD:${p:+$p/}$f" 2>/dev/null)
    [ -n "$b0" ] && [ "$b0" = "$b1" ] || { print_fail "the move to ${p:-the repo root} changed $f, so this prefix's population is not HEAD's"; return 1; }
  done
  list=$(bash "${p:+$p/}$KIT/run-selftests.sh" --list 2>&1) || { print_fail "run-selftests.sh --list refused at ${p:-the repo root}: $(printf '%s\n' "$list" | tail -2)"; return 1; }
  rm -rf "$TMPD/runs"; mkdir -p "$TMPD/runs"
  load_population "$list"
  derive_row_kinds "$label" "$p"
  derive_dispatch_order
  n=${#R_NAME[@]}
  # A REPRESENTED row is a skip that announces itself (S1): counted neither graded nor passed.
  for j in "${!R_NAME[@]}"; do
    [ "${R_KIND[j]}" = represented ] || continue
    r=$((r + 1)); printf '[%s] %s · represented · by shard %s\n' "$label" "${R_NAME[j]}" "${R_REP[j]}"
  done
  # The dispatch order puts every whole row first, longest budget first (S3). Each row reads
  # /dev/null: a suite that reads stdin would otherwise eat what the pool's caller holds on it.
  for j in "${ORDER[@]}"; do
    name=${R_NAME[j]}; bound=${R_BOUND[j]}; argv=${R_ARGV[j]}; kind=${R_KIND[j]}
    if grep -qxF "$name" "$INHERITED"; then
      printf '[%s] %s · %s · not graded · red at gov'"'"'s prefix in the baseline bar run\n' "$label" "$name" "$kind"
      continue
    fi
    if [ -z "$p" ]; then
      why=""; for w in "${GOV_LAYOUT[@]}"; do [ "${w%%|*}" = "$name" ] && why=${w#*|}; done
      if [ -n "$why" ]; then printf '[%s] %s · %s · not graded · gov layout: %s\n' "$label" "$name" "$kind" "$why"; continue; fi
    fi
    case "$argv" in python3\ *|python\ *) argv="$PY ${argv#* }" ;; esac
    i=$((i + 1)); d="$TMPD/runs/$i"; mkdir -p "$d"; printf '%s\n' "$name" > "$d/name"
    run_row "$label" "$d" "$name" "$bound" "$argv" "$kind" < /dev/null &
    live=$((live + 1))
    if [ "$live" -ge "$WIDTH" ]; then wait -n; live=$((live - 1)); fi
  done
  wait
  [ "$n" -gt 0 ] || { print_fail "at ${p:-the repo root} the population selected no row${FILTER:+ matching '$FILTER'}, so this prefix graded nothing"; return 1; }
  for d in "$TMPD"/runs/*/; do
    [ -f "$d/name" ] || continue
    IFS= read -r name < "$d/name"; v=""; why=""
    [ -f "$d/verdict" ] && IFS=$'\t' read -r v why < "$d/verdict"
    [ "$v" = ok ] && continue
    red=1
    print_fail "[$label] $name: ${why:-no verdict was written}"
    tail -n 8 "$d/out" 2>/dev/null | sed 's/^/        /'
  done
  dirty=$(git status --porcelain --untracked-files=all 2>/dev/null | head -n 10)
  if [ -n "$dirty" ]; then red=1; print_fail "a suite wrote into the clone at ${p:-the repo root}, outside its scratch: $(printf '%s' "$dirty" | tr '\n' ';')"; fi
  # The summary counts a represented row APART from the graded ones (S1, AC2).
  [ "$r" = 0 ] || note=", $r represented by their family's probe shard and not graded"
  [ "$((n - i - r))" = 0 ] || note="$note, $((n - i - r)) not graded"
  [ -z "$note" ] || note="$note, each named above"
  [ "$red" = 0 ] && print_pass "all $i graded row(s) found their subject at ${p:-the repo root}$note"
  return "$red"
}

# The stale-declaration guard reads gov's own prefix, before any move; a filtered run skips it, and
# its listing, as it always did.
if [ -z "$FILTER" ]; then
  load_population "$(bash "$TROOT/$KIT/run-selftests.sh" --list 2>/dev/null)"
  check_declarations
fi

stopped=""
for P in scripts vendor/gov ""; do
  if [ "$P" = "$TROOT" ]; then echo "foreign-prefix: skip ${P} — it is gov's own prefix, which the bar already runs"; continue; fi
  if [ -n "$stopped" ]; then echo "foreign-prefix: [${P:-root}] not run — ${stopped} was red"; continue; fi
  run_at_prefix "$P" || stopped="${P:-the repo root}"
done
[ "$fails" = 0 ] && [ "$passed" -lt "$FLOOR_ASSERTIONS" ] && print_fail "only $passed of the $FLOOR_ASSERTIONS verdicts ran (floor FLOOR_ASSERTIONS)"
[ "$fails" = 0 ] && echo "PASS ($passed assertions)"
[ "$fails" = 0 ] || { echo "FAIL — $fails check(s) failed"; exit 1; }
