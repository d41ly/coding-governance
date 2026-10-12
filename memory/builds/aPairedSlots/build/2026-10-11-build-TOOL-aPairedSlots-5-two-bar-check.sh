#!/usr/bin/env bash
# **Serves:** journal TOOL-aPairedSlots-5 TOOL-aPairedSlots-7
# Two REAL full bars on two worktrees of ONE repository: first one after the other, then both at
# once under two slots. Passes when, for each worktree, the two runs give the same leg verdicts, and
# nothing either bar keeps is lost or torn: its ledger rows, its run-log line, its run record.
#
# ONE REPOSITORY, TWO WORKTREES, on purpose: they share the git common dir, which is where the run
# log, the health log, the shared full green and the drift history live, and each has its own git
# dir, which is where the ledger and the run records live. A frozen clone of the build tip behind a
# bare remote that advertises only `main`, exactly as the A/B instrument freezes its clones.
#
# A PRIVATE TURNSTILE (`GATE_TURNSTILE_DIR` under the root), so the pair neither waits behind nor
# blocks the host's other bars: this checks what two holders write, not how long they take.
#
# Usage, forward-slashed:
#   two-bar-check.sh init <root> <source-repo> <sha>
#   two-bar-check.sh run  <root>
#   two-bar-check.sh grade <root>   re-grade a run from what it left, without running a bar
# Rows land in <root>/check.tsv; the verdict is the last line of <root>/check.out.
set -u

print_err() { printf 'two-bar: %s\n' "$*" >&2; }

cmd_init() { # root source sha
  local root=$1 src=$2 sha
  mkdir -p "$root" || return 1
  [ -e "$root/remote.git" ] && { print_err "init: $root/remote.git exists; pick a fresh root"; return 1; }
  sha=$(git -C "$src" rev-parse --verify -q "$3^{commit}") || { print_err "init: $3 names no commit"; return 1; }
  git init -q --bare "$root/remote.git" || return 1
  git -C "$root/remote.git" fetch -q --no-tags "$src" "+$sha:refs/heads/main" 2>/dev/null \
    || git -C "$root/remote.git" fetch -q --no-tags "$src" "+HEAD:refs/ab/src" || return 1
  git -C "$root/remote.git" cat-file -e "$sha^{commit}" || { print_err "init: $sha did not arrive"; return 1; }
  git -C "$root/remote.git" update-ref refs/heads/main "$sha" || return 1
  git -C "$root/remote.git" update-ref -d refs/ab/src 2>/dev/null
  git -C "$root/remote.git" symbolic-ref HEAD refs/heads/main
  git clone -q --no-hardlinks "$root/remote.git" "$root/w1" || return 1
  git -C "$root/w1" worktree add -q -b w2 "$root/w2" main || return 1
  git -C "$src" config --local --get-regexp '^(merge\.|core\.hookspath)' 2>/dev/null \
    | while read -r k v; do git -C "$root/w1" config "$k" "$v"; done
  mkdir -p "$root/turnstile" "$root/out"
  printf 'sha\t%s\n' "$sha" > "$root/init.tsv"
  printf 'mode\tbar\tstart\tend\trc\tok\tfail\trunlog_lines\trecord_verdict\tledger_rows_this_run\n' > "$root/check.tsv"
}

run_bar() { # root mode bar
  local root=$1 mode=$2 bar=$3 o="$1/out/$2-$3"
  date +%s > "$o.start"
  (cd "$root/$bar" && GATE_FULL=1 GATE_TURNSTILE_DIR="$root/turnstile" GATE_TURNSTILE_SLOTS=2 \
     bash tools/run-gates/run-gates.sh) > "$o.log" 2>&1
  echo $? > "$o.rc"
  date +%s > "$o.end"
}

# The bar's own git dir: `git rev-parse --absolute-git-dir` asked from inside that worktree.
read_git_dir() { (unset GIT_DIR GIT_WORK_TREE; cd "$1" && git rev-parse --absolute-git-dir); }

measure_bar() { # root mode bar -> appends a row; the leg verdicts go to <out>.verdicts
  local root=$1 mode=$2 bar=$3 o="$1/out/$2-$3" gd rec s e rid lines ver rows
  s=$(cat "$o.start"); e=$(cat "$o.end")
  grep -E '^GATE (ok|FAIL) ' "$o.log" | sed -E 's/^GATE (ok|FAIL) +([^ ].*)$/\1\t\2/; s/  .*$//' \
    | LC_ALL=C sort > "$o.verdicts"
  gd=$(read_git_dir "$root/$bar")
  rid=$(cat "$gd/gate-run/current" 2>/dev/null)
  rec="$gd/gate-run/$rid"
  # BY KEY (TOOL-aPairedSlots-13): the verdict file opens with `ended<TAB><time>`, and a first-line read
  # carried that TAB into the row, which then held eleven fields under a ten-field header.
  ver=$(awk -F'\t' '$1=="verdict" {print $2}' "$rec/verdict" 2>/dev/null); ver=${ver:--}
  # One run-log line per bar, whole: it carries this run's id and parses as TAB-separated k=v fields.
  lines=$(awk -F'\t' -v r="run=$rid" '{for (i=1;i<=NF;i++) if ($i==r) {ok=1; for (j=1;j<=NF;j++) if ($j !~ /^[a-z_.0-9]+=/) ok=0; if (ok) n++}} END {print n+0}' \
    "$root/w1/.git/runlog/gates.log" 2>/dev/null)
  # Ledger rows carrying THIS run's id, the ledger's sixth field. Counted now, because the next run of
  # this worktree rewrites the ledger with its own rows and this run's are gone.
  rows=$(awk -F'\t' -v r="$rid" '$6 == r' "$gd/gate-ledger.tsv" 2>/dev/null | grep -c .)
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$mode" "$bar" "$s" "$e" "$(cat "$o.rc")" \
    "$(grep -c '^ok' "$o.verdicts")" "$(grep -c '^FAIL' "$o.verdicts")" "$lines" "$ver" "$rows" >> "$root/check.tsv"
}

cmd_run() { # root
  local root=$1 p1 p2 bad=0 b
  run_bar "$root" serial w1; run_bar "$root" serial w2
  measure_bar "$root" serial w1; measure_bar "$root" serial w2
  run_bar "$root" concurrent w1 & p1=$!; run_bar "$root" concurrent w2 & p2=$!; wait "$p1" "$p2"
  measure_bar "$root" concurrent w1; measure_bar "$root" concurrent w2
  cmd_grade "$root"
}

# Every bar: one whole run-log line, a run record with a verdict, and ledger rows for its legs. A row
# is ten fields. The earlier copy of this check wrote eleven, the verdict file's `ended` and its time
# in two columns, and such a row is read with those two joined; any other width is named, never graded
# with its columns out of place (TOOL-aPairedSlots-13).
check_rows() { # check.tsv -> rc 0 when every row is whole and kept; prints each row that is not
  awk -F'\t' 'NR == 1 { next }
    NF == 11 && $9 == "ended" { $9 = $9 " " $10; for (i = 10; i < NF; i++) $i = $(i + 1); NF = 10 }
    NF != 10 { print "row malformed (" NF " fields): " $0; b = 1; next }
    ($8 + 0) != 1 || $9 == "-" || ($10 + 0) < ($6 + $7) { print "row lost or torn: " $0; b = 1 }
    END { exit b }' "$1"
}

# The verdict over what a run left: the leg verdicts, the rows and the run records. `run` ends here,
# and `grade` re-reads a run already made, the earlier copy's included.
cmd_grade() { # root
  local root=$1 bad=0 b
  for b in w1 w2; do
    if cmp -s "$root/out/serial-$b.verdicts" "$root/out/concurrent-$b.verdicts"; then
      echo "$b: the same $(grep -c . "$root/out/serial-$b.verdicts") leg verdicts serial and concurrent"
    else
      echo "$b: leg verdicts DIFFER serial against concurrent:"; diff "$root/out/serial-$b.verdicts" "$root/out/concurrent-$b.verdicts" | head -20
      bad=1
    fi
  done
  check_rows "$root/check.tsv" || bad=1
  # Both concurrent bars must actually have overlapped, or the pair proves nothing about two writers.
  if [ "$(awk -F'\t' '$1=="concurrent" {print $3, $4}' "$root/check.tsv" | awk 'NR==1{s1=$1;e1=$2} NR==2{s2=$1;e2=$2} END{print (s1<e2 && s2<e1) ? "yes" : "no"}')" != yes ]; then
    echo "the concurrent pair did not overlap, so it shows nothing about two writers"; bad=1
  fi
  [ "$bad" = 0 ] && echo "TWO-BAR CHECK PASS" || echo "TWO-BAR CHECK FAIL"
  return "$bad"
}

main() {
  local verb=${1:-}; shift || true
  case "$verb" in
    init) cmd_init "$@" ;;
    run)  cmd_run "$@" > "$1/check.out" 2>&1; local rc=$?; cat "$1/check.out"; return "$rc" ;;
    grade) cmd_grade "$@" ;;
    *) print_err "usage: init <root> <source-repo> <sha> | run <root> | grade <root>"; return 2 ;;
  esac
}
main "$@"
