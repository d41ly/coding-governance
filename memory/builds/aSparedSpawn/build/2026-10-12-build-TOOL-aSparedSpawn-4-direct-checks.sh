#!/usr/bin/env bash
# TOOL-aSparedSpawn-4 — the pass's direct checks: the runner itself, a copy at the pass's base and the
# working tree's, driven over hand-built fixture repositories with tiny manifests of `bash -c` legs.
# No suite, no slice of one: every counter and comparison here is written for this record.
#
# Usage: bash <this file> <base runner> <new runner> <scratch root> <case>...
#   cases: forks (AC8 AC9 figures), bytes (AC1 AC2 AC3 AC4), pool (AC5), keys (AC6), git (AC7),
#          procmon (AC10), parity (AC11), ban (AC12)
# Every line is `ok`, `FAIL` or `info`, naming the values it read; the exit status is the FAIL count.
set -u
BASE_RG=$1; NEW_RG=$2; S=$3; shift 3
REPO=${DC_REPO:-$(cd "$(dirname "$0")/../../../.." && pwd)}   # DC_REPO when a frozen copy of this file runs
mkdir -p "$S"
fails=0
check_step() { if [ "$1" = 0 ]; then echo "ok    $2"; else echo "FAIL  $2"; fails=$((fails+1)); fi; }
CLEAN_ENV=(GATE_FULL= GATE_BASE= GATE_REUSE= GATE_WALL=0 GATE_SELFTESTS= GATE_ATTRIBUTE= GATE_RUN_ID=
  GATE_PROFILES= GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_MEMPAUSE=0 GATE_RUN_KEEP=1000)

build_kit() { # dir · runner -> a kit dir holding the runner and its two siblings
  mkdir -p "$1"
  cp "$2" "$1/run-gates.sh"
  cp "$REPO/tools/run-gates/gate-fingerprint.sh" "$REPO/tools/run-gates/gate-profiles.txt" "$1/"
}
build_repo() { # dir -> a committed scratch repository with a few guarded paths
  local t=$1
  rm -rf "$t"; mkdir -p "$t/ga/sub" "$t/gb" "$t/fx"
  printf 'one\n' > "$t/ga/one.txt"; printf 'two\n' > "$t/ga/sub/two.txt"; printf 'f\n' > "$t/gb/f.txt"
  printf 'g\n' > "$t/gb/g.txt"; printf '#!/usr/bin/env bash\nexit 0\n' > "$t/fx/ok.sh"
  ( cd "$t" && git init -q -b main . && git config user.email fx@test.invalid && git config user.name fx \
      && git config core.autocrlf false && git add -A && git commit -qm seed ) >/dev/null 2>&1
}
run_bar() { # repo · kit dir · output file · VAR=value…
  local t=$1 k=$2 o=$3; shift 3
  ( cd "$t" && env "${CLEAN_ENV[@]}" "$@" bash "$k/run-gates.sh" > "$o" 2>&1; echo $? > "$o.rc" )
}
read_run_dir() { local c=""; IFS= read -r c < "$1/.git/gate-run/current" 2>/dev/null; printf '%s/.git/gate-run/%s' "$1" "$c"; }

# ---- the spawn counter: forks are distinct BASHPIDs in an xtrace, execs are command words that are no
# builtin, keyword, assignment or function the traced runner defines. Written for this record.
TRACE_PS4='+${BASHPID}|${BASH_SOURCE##*/}:${LINENO}|'
measure_spawns() { # trace · runner -> SP_FORKS SP_EXECS, and SP_SITES "<site> <events>" lines; rc 2 on an empty trace
  local line pid site cmd w root="" known
  local -A seen=() per=()
  SP_FORKS=0; SP_EXECS=0; SP_SITES=""
  [ -s "$1" ] || return 2
  known=" $(compgen -b | tr '\n' ' ') $(compgen -k | tr '\n' ' ') "
  known="$known$(sed -n 's/^[[:space:]]*\([A-Za-z_][A-Za-z0-9_]*\)[[:space:]]*()[[:space:]]*{.*/\1/p' "$2" | tr '\n' ' ') "
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in +*'|'*'|'*) ;; *) continue ;; esac
    line=${line#"${line%%[!+]*}"}; pid=${line%%|*}; line=${line#*|}; site=${line%%|*}; cmd=${line#*|}
    case "$pid" in ''|*[!0-9]*) continue ;; esac
    [ -n "$root" ] || root=$pid
    if [ "$pid" != "$root" ] && [ -z "${seen[$pid]+x}" ]; then
      seen[$pid]=1; SP_FORKS=$((SP_FORKS + 1)); per[$site]=$(( ${per[$site]:-0} + 1 ))
    fi
    w=${cmd%% *}; w=${w#\'}; w=${w%\'}
    case "$w" in ''|*=*|\(*) continue ;; esac
    case "$known" in *" $w "*) continue ;; esac
    SP_EXECS=$((SP_EXECS + 1)); per[$site]=$(( ${per[$site]:-0} + 1 ))
  done < "$1"
  [ -n "$root" ] || return 2
  for site in "${!per[@]}"; do SP_SITES+="$site ${per[$site]}"$'\n'; done
}
# The spawn floor is pinned at one microsecond, so no bar rewrites it: a first draft read a per-bar
# floor write in one trace and not the other as three phantom per-leg events.
run_traced_bar() { # repo · kit dir · trace file · manifest
  printf '0.001\t2026-01-01T00:00:00Z\n' > "$S/spawn-floor"
  ( cd "$1" && env "${CLEAN_ENV[@]}" GATE_JOBS=1 GATE_LEGS="$4" GATE_SPAWN_FLOOR="$S/spawn-floor" PS4="$TRACE_PS4" BASH_XTRACEFD=9 \
      bash -x "$2/run-gates.sh" 9>"$3" >/dev/null 2>&1 )
}

for c in "$@"; do
  case "$c" in
  forks)
    # A specimen with five declared forks and one exec, and the same with the descriptor closed early.
    printf '%s\n' 'f() { printf %s x; }' 'a=$(f)' 'b=$(f)' '( : )' "printf 'x\\n' | while IFS= read -r l; do :; done" \
      'cat </dev/null >/dev/null' > "$S/specimen.sh"
    # The calibration refuses (2) unless the counter reads the specimen's declared figures.
    check_calibration() { # specimen -> 0 when its trace counts 5 forks and 1 exec, else 2
      env PS4="$TRACE_PS4" BASH_XTRACEFD=9 bash -x "$1" 9>"$1.trace" >/dev/null 2>&1
      measure_spawns "$1.trace" "$1" || return 2
      [ "$SP_FORKS|$SP_EXECS" = "5|1" ] || return 2
    }
    check_calibration "$S/specimen.sh"; r=$?
    check_step "$r" "AC8 the specimen counts $SP_FORKS forks and $SP_EXECS exec, declared 5 and 1"
    { printf 'exec 9>&-\n'; cat "$S/specimen.sh"; } > "$S/closed.sh"
    check_calibration "$S/closed.sh"; r=$?
    check_step "$([ "$r" = 2 ] && echo 0 || echo 1)" "AC8 a trace whose descriptor closed early refuses (rc $r) rather than reading $SP_FORKS forks"
    build_repo "$S/fk"
    printf '%s\n' '[{"name":"one","argv":["bash","-c","exit 0"],"ceiling":60}]' > "$S/one.json"
    printf '%s\n' '[{"name":"one","argv":["bash","-c","exit 0"],"ceiling":60},{"name":"two","argv":["bash","-c","exit 0"],"ceiling":60}]' > "$S/two.json"
    # The added fork AC9 stages: one `$(date +%s)` as runleg's seconds line opens.
    d=date
    sed "s/^  local secs; printf -v secs/  : \"\$($d +%s)\"; local secs; printf -v secs/" "$NEW_RG" > "$S/plus-one.sh"
    check_step "$([ "$(grep -c "\$($d +%s)\"; local secs" "$S/plus-one.sh")" = 1 ] && echo 0 || echo 1)" "AC9 the staged copy carries exactly one added substitution"
    for side in ${DC_SIDES:-base new plus}; do
      case "$side" in base) src=$BASE_RG ;; new) src=$NEW_RG ;; plus) src=$S/plus-one.sh ;; esac
      build_kit "$S/kit-$side/run-gates" "$src"
      runs=$(seq 1 "${DC_RUNS:-2}"); [ "$side" = plus ] && runs=1
      for m in one two; do
        for k in $runs; do
          run_traced_bar "$S/fk" "$S/kit-$side/run-gates" "$S/t.$side.$m.$k" "$S/$m.json"
          measure_spawns "$S/t.$side.$m.$k" "$S/kit-$side/run-gates/run-gates.sh" || echo "FAIL  empty trace $side $m $k"
          eval "F_${side}_${m}_$k=\$SP_FORKS; E_${side}_${m}_$k=\$SP_EXECS"
          printf '%s' "$SP_SITES" | sort > "$S/sites.$side.$m.$k"
        done
      done
      for k in $runs; do
        eval "f1=\$F_${side}_one_$k; f2=\$F_${side}_two_$k; e1=\$E_${side}_one_$k; e2=\$E_${side}_two_$k"
        echo "info  $side run $k: one leg ${f1} forks ${e1} execs, two legs ${f2} forks ${e2} execs, per leg $(( (f2 - f1) + (e2 - e1) )) events ($((f2 - f1)) forks, $((e2 - e1)) execs)"
      done
    done
    # The per-leg contributors of the new runner and of the staged copy: sites whose events grew from
    # the one-leg bar to the two-leg bar.
    for side in new plus; do
      echo "info  $side per-leg sites (run 1):"
      join -a 2 -e 0 -o '0,1.2,2.2' "$S/sites.$side.one.1" "$S/sites.$side.two.1" \
        | awk '$3 > $2 { print "        " $1 " +" ($3 - $2) }' | sort -k2 -t+ -rn | head -12
    done
    ;;
  bytes)
    build_repo "$S/by"
    # Legs whose output carries trailing newlines, a NUL, CRLF lines, nothing, a credential URL, and a
    # name with a space, a slash and a two-byte character; one sleeps a second for AC1.
    cat > "$S/bytes.json" <<'JSON'
[{"name":"trail","argv":["bash","-c","printf 'a\\n\\n\\n'"]},
 {"name":"nul","argv":["bash","-c","printf 'x\\0y\\r\\nz\\n'"]},
 {"name":"crlf","argv":["bash","-c","printf 'l1\\r\\nl2\\r\\n\\r\\r\\n'"]},
 {"name":"none","argv":["bash","-c","exit 0"]},
 {"name":"url","argv":["bash","-c","echo fetch https://u:p@host/x; printf 'c\\r\\n'"]},
 {"name":"nourl","argv":["bash","-c","echo see https://host/x and a@b; printf 'd\\r\\n'"]},
 {"name":"sp é/x y","argv":["bash","-c","echo multi"]},
 {"name":"sleeper","argv":["bash","-c","sleep 1"]}]
JSON
    for side in base new; do
      case "$side" in base) src=$BASE_RG ;; new) src=$NEW_RG ;; esac
      build_kit "$S/kit-$side/run-gates" "$src"
      rm -rf "$S/by/.git/gate-logs"
      run_bar "$S/by" "$S/kit-$side/run-gates" "$S/by.$side.out" GATE_LEGS="$S/bytes.json" GATE_JOBS=4
      rm -rf "$S/by.$side.logs" "$S/by.$side.run"
      cp -r "$S/by/.git/gate-logs" "$S/by.$side.logs"; cp -r "$(read_run_dir "$S/by")" "$S/by.$side.run"
    done
    for i in 0 1 2 3 4 5 6 7; do
      cmp -s "$S/by.base.run/$i.out" "$S/by.new.run/$i.out"
      check_step "$?" "AC2/AC4 the run-record copy of leg $i equals the base runner's byte for byte ($(wc -c < "$S/by.new.run/$i.out") bytes)"
    done
    ( cd "$S/by.base.logs" && ls -1 ) > "$S/by.base.names"; ( cd "$S/by.new.logs" && ls -1 ) > "$S/by.new.names"
    cmp -s "$S/by.base.names" "$S/by.new.names"
    check_step "$?" "AC3 the gate-logs file names equal the base runner's: $(tr '\n' ' ' < "$S/by.new.names")"
    check_step "$(grep -qx 'sp____x_y.log' "$S/by.new.names" && echo 0 || echo 1)" "AC3 the two-byte character maps to two underscores"
    while IFS= read -r f; do
      cmp -s "$S/by.base.logs/$f" "$S/by.new.logs/$f"; check_step "$?" "AC2 gate-logs/$f equals the base runner's byte for byte"
    done < "$S/by.new.names"
    check_step "$(grep -q '://\*\*\*:\*\*\*@host/x' "$S/by.new.run/4.out" && echo 0 || echo 1)" "AC4 the credential leg's copy is masked: $(grep fetch "$S/by.new.run/4.out")"
    check_step "$(grep -q 'https://host/x and a@b' "$S/by.new.run/5.out" && echo 0 || echo 1)" "AC4 the URL leg with no userinfo is written as it printed"
    echo "info  modes: base $(stat -c %a "$S/by/.git/gate-run" 2>/dev/null) run dir; new copy $(ls -l "$S/by.new.run/4.out" | cut -c1-10), base copy $(ls -l "$S/by.base.run/4.out" | cut -c1-10)"
    sec=$(awk -F'\t' 'NR==1 { print $4 }' "$S/by.new.run/7.leg")
    check_step "$(printf '%s' "$sec" | grep -qE '^[0-9]+\.[0-9]{3}$' && awk -v s="$sec" 'BEGIN { exit !(s >= 1.0) }' && echo 0 || echo 1)" \
      "AC1 the sleeper's .leg seconds field reads $sec"
    check_step "$(grep -c 'ignored null byte' "$S/by.new.out")" "the new runner prints no NUL warning (base printed $(grep -c 'ignored null byte' "$S/by.base.out"))"
    ;;
  pool)
    build_repo "$S/po"
    printf '%s\n' '[{"name":"a","argv":["bash","-c","exit 0"]},{"name":"b","argv":["bash","-c","echo bad; exit 3"]},
 {"name":"c","argv":["bash","-c","exit 0"]},{"name":"d","argv":["bash","-c","sleep 1"]},
 {"name":"e","argv":["bash","-c","exit 0"]},{"name":"f","argv":["bash","-c","exit 0"]}]' > "$S/pool.json"
    build_kit "$S/kit-new/run-gates" "$NEW_RG"; build_kit "$S/kit-base/run-gates" "$BASE_RG"
    for j in 1 4; do
      run_bar "$S/po" "$S/kit-new/run-gates" "$S/po.new.$j" GATE_LEGS="$S/pool.json" GATE_JOBS=$j
      run_bar "$S/po" "$S/kit-base/run-gates" "$S/po.base.$j" GATE_LEGS="$S/pool.json" GATE_JOBS=$j
      for side in new base; do grep -E '^(GATE|----)' "$S/po.$side.$j" | sed 's/  ([0-9]*s)$//' > "$S/po.$side.$j.lines"; done
    done
    cmp -s "$S/po.new.1.lines" "$S/po.new.4.lines"; check_step "$?" "AC5 the new runner's report at GATE_JOBS=1 equals GATE_JOBS=4"
    cmp -s "$S/po.new.4.lines" "$S/po.base.4.lines"; check_step "$?" "AC5 and equals the base runner's"
    check_step "$(grep -c 'no result' "$S/po.new.1" "$S/po.new.4" | awk -F: '{ s += $2 } END { print s }')" "AC5 no leg reports (no result)"
    sed 's/^/        /' "$S/po.new.4.lines"
    ;;
  keys)
    build_repo "$S/ky"
    printf '%s\n' '[{"name":"ga","argv":["bash","-c","exit 0"],"guard":["ga/"]},
 {"name":"gsub","argv":["bash","-c","exit 0"],"guard":["ga/sub"]},
 {"name":"gbf","argv":["bash","-c","exit 0"],"guard":["gb/f.txt","ga/one.txt"]},
 {"name":"glob","argv":["bash","-c","exit 0"],"guard":["gb/*.txt"]},
 {"name":"none","argv":["bash","-c","exit 0"],"guard":["nosuch/"]},
 {"name":"whole","argv":["bash","-c","exit 0"]}]' > "$S/keys.json"
    # A dirty tree: an edited tracked file, an untracked one under a guard, a staged edit.
    printf 'edited\n' >> "$S/ky/ga/one.txt"; printf 'new\n' > "$S/ky/ga/sub/new.txt"
    printf 'staged\n' >> "$S/ky/gb/g.txt"; git -C "$S/ky" add gb/g.txt
    build_kit "$S/kit-new/run-gates" "$NEW_RG"; build_kit "$S/kit-base/run-gates" "$BASE_RG"
    # GATE_FULL so every guarded leg runs and writes its row.
    run_bar "$S/ky" "$S/kit-base/run-gates" "$S/ky.base" GATE_LEGS="$S/keys.json" GATE_FULL=1 GATE_JOBS=2
    rm -rf "$S/ky.base.run"; cp -r "$(read_run_dir "$S/ky")" "$S/ky.base.run"
    run_bar "$S/ky" "$S/kit-new/run-gates" "$S/ky.new" GATE_LEGS="$S/keys.json" GATE_FULL=1 GATE_JOBS=2
    for i in 0 1 2 3 4 5; do
      kb=$(awk -F'\t' 'NR==1 { print $7 }' "$S/ky.base.run/$i.leg"); kn=$(awk -F'\t' 'NR==1 { print $7 }' "$(read_run_dir "$S/ky")/$i.leg")
      check_step "$({ [ -n "$kn" ] && [ "$kn" != - ] && [ "$kn" = "$kb" ]; } && echo 0 || echo 1)" "AC6 leg $i's ledger key equals the base runner's: $kn"
    done
    # The same over a reuse: a second new bar under GATE_REUSE reuses every leg the first proved.
    run_bar "$S/ky" "$S/kit-new/run-gates" "$S/ky.reuse" GATE_LEGS="$S/keys.json" GATE_FULL=1 GATE_JOBS=2 GATE_REUSE=1
    check_step "$([ "$(grep -c '^GATE reuse' "$S/ky.reuse")" = 6 ] && echo 0 || echo 1)" "AC6 a GATE_REUSE bar reuses all six legs on the precomputed keys: $(grep -c '^GATE reuse' "$S/ky.reuse")"
    ;;
  git)
    t="$S/gt"; rm -rf "$t"; mkdir -p "$t"
    build_repo "$t/p"; git -C "$t/p" worktree add -q "$t/w" >/dev/null 2>&1
    mkdir -p "$t/u"; ( cd "$t/u" && git init -q -b main . && printf 'x\n' > x.txt ) >/dev/null 2>&1
    printf '%s\n' '[{"name":"one","argv":["bash","-c","exit 0"]}]' > "$S/git.json"
    build_kit "$S/kit-new/run-gates" "$NEW_RG"; build_kit "$S/kit-base/run-gates" "$BASE_RG"
    for d in p w u; do
      for side in base new; do
        run_bar "$t/$d" "$S/kit-$side/run-gates" "$S/gt.$d.$side" GATE_LEGS="$S/git.json"
        gdir=$(git -C "$t/$d" rev-parse --absolute-git-dir)
        cur=""; IFS= read -r cur < "$gdir/gate-run/current" 2>/dev/null
        h="$gdir/gate-run/$cur/header"
        printf '%s|%s|%s|%s\n' "$(awk -F'\t' '$1=="head" { print $2 }' "$h")" "$(awk -F'\t' '$1=="worktree" { print $2 }' "$h")" \
          "$([ -f "$gdir/gate-logs/one.log" ] && echo logs-in-gitdir)" "$(cat "$S/gt.$d.$side.rc")" > "$S/gt.$d.$side.fields"
        rm -rf "$gdir/gate-logs"
      done
      echo "info  $d base: $(cat "$S/gt.$d.base.fields")"
      echo "info  $d new:  $(cat "$S/gt.$d.new.fields")"
      if [ "$d" = u ]; then
        check_step "$(awk -F'|' '{ print ($1 == "") ? 0 : 1 }' "$S/gt.u.new.fields")" "AC7 an unborn HEAD reads empty, never the literal HEAD"
        cut -d'|' -f2- "$S/gt.u.base.fields" > "$S/gt.u.base.rest"; cut -d'|' -f2- "$S/gt.u.new.fields" > "$S/gt.u.new.rest"
        cmp -s "$S/gt.u.base.rest" "$S/gt.u.new.rest"; check_step "$?" "AC7 unborn: worktree, log dir and rc equal the base runner's"
      else
        cmp -s "$S/gt.$d.base.fields" "$S/gt.$d.new.fields"; check_step "$?" "AC7 $d: head, worktree, log dir and rc equal the base runner's"
      fi
    done
    ;;
  procmon)
    printf '%s\n' '[{"name":"one","argv":["bash","-c","exit 0"]}]' > "$S/pm.json"
    for kitcase in found missing refusing; do
      for side in base new; do
        case "$side" in base) src=$BASE_RG ;; new) src=$NEW_RG ;; esac
        t="$S/pm.$kitcase.$side"; build_repo "$t"; build_kit "$t/tools/run-gates" "$src"
        : > "$t/.process-monitor.conf"
        if [ "$kitcase" != missing ]; then
          mkdir -p "$t/tools/process-monitor"; : > "$t/tools/process-monitor/reap.py"
          case "$kitcase" in
            found) printf 'print("IN SCOPE")\n' > "$t/tools/process-monitor/scope.py" ;;
            refusing) printf 'print("out of scope")\n' > "$t/tools/process-monitor/scope.py" ;;
          esac
        fi
        ( cd "$t" && git add -A && git commit -qm kit ) >/dev/null 2>&1
        ( cd "$t" && env "${CLEAN_ENV[@]}" GATE_JOBS=1 GATE_LEGS="$S/pm.json" PS4="$TRACE_PS4" BASH_XTRACEFD=9 \
            bash -x tools/run-gates/run-gates.sh 9>"$S/pm.$kitcase.$side.trace" >"$S/pm.$kitcase.$side.out" 2>&1 )
        # The refusal names the fixture's own path, which differs per side by its last segment only.
        grep '^run-gates: process-monitor:' "$S/pm.$kitcase.$side.out" | sed "s#pm\.$kitcase\.$side/#pm.$kitcase.SIDE/#g" > "$S/pm.$kitcase.$side.why"
        # python execs before the first dispatch: command words naming a launcher, up to the first runleg
        awk -F'|' '{ w = $3; sub(/ .*/, "", w); gsub(/\047/, "", w) }
                   w == "runleg" { exit } w ~ /(^|\/)(python3?|py)(\.exe)?$/ { n++ } END { print n + 0 }' \
          "$S/pm.$kitcase.$side.trace" > "$S/pm.$kitcase.$side.py"
      done
      cmp -s "$S/pm.$kitcase.base.why" "$S/pm.$kitcase.new.why"
      check_step "$?" "AC10 $kitcase: the process-monitor line equals the base runner's: $(cat "$S/pm.$kitcase.new.why")"
      pb=$(cat "$S/pm.$kitcase.base.py"); pn=$(cat "$S/pm.$kitcase.new.py")
      check_step "$([ "$pn" = $((pb - 1)) ] && echo 0 || echo 1)" "AC10 $kitcase: python execs before the first dispatch, base $pb, new $pn"
    done
    ;;
  parity)
    want=$(awk '/^# >>> resolve_kit_dir/{f=1} f{print} f && /^# <<< resolve_kit_dir/{exit}' "$REPO/tools/lib/resolve_kit_dir.py" | tr -d '\r')
    pop=$(cd "$REPO" && git grep -l '^# >>> resolve_kit_dir' -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md | grep -v '^tools/lib/resolve_kit_dir')
    all=$(cd "$REPO" && git grep -l '>>> resolve_kit_dir' -- ':!memory/' | grep -v '^tools/lib/resolve_kit_dir')
    nd=0; np=0
    printf '%s\n' "$pop" > "$S/parity.pop"
    while IFS= read -r f; do
      np=$((np + 1))
      got=$(awk '/^# >>> resolve_kit_dir/{f=1} f{print} f && /^# <<< resolve_kit_dir/{exit}' "$REPO/$f" | tr -d '\r')
      [ "$got" = "$want" ] || { nd=$((nd + 1)); echo "FAIL  AC11 $f drifted"; }
    done < "$S/parity.pop"
    check_step "$nd" "AC11 every one of the $np copies' marked regions equals tools/lib/resolve_kit_dir.py"
    missing=$(comm -13 <(printf '%s\n' "$pop" | sort) <(printf '%s\n' "$all" | sort))
    check_step "$([ -z "$missing" ] && echo 0 || echo 1)" "AC11 the population covers every file git grep lists outside memory/: ${missing:-none missing}"
    lt='<''<'; left=$(cd "$REPO" && git grep -l "\$(cat $lt'RKD'" -- ':!memory/' || true)
    check_step "$([ -z "$left" ] && echo 0 || echo 1)" "S11 no file outside memory/ still captures the heredoc with cat: ${left:-none}"
    ;;
  ban)
    # The S12 predicate, run as the suite runs it, over a scratch copy of one suite with its wrapper
    # reverted, and over a comment spelling the same idiom.
    lt='<''<'; tag="${lt}'RKD'"; idiom="\$(cat $tag"
    mkdir -p "$S/ban"
    sed "s/^  IFS= read -r -d '' _rkd $tag || :\$/  \"\$1\" -c \"$idiom/" "$REPO/tools/hooks/agent-cap.test.sh" > "$S/ban/reverted.test.sh"
    printf '#!/usr/bin/env bash\n# the old wrapper read %s, which forked\n' "$idiom" > "$S/ban/comment.test.sh"
    # The S12 scan as the suite spells it, over the two scratch files.
    for b in reverted comment; do
      awk -v F="$b" -v idiom="$idiom" '{ l = $0; sub(/\r$/, "", l) } l !~ /^[[:space:]]*#/ && index(l, idiom) { printf "%s:%d\n", F, NR }' \
        "$S/ban/$b.test.sh" > "$S/ban/hits.$b"
    done
    check_step "$([ "$(grep -c . "$S/ban/hits.reverted")" = 1 ] && echo 0 || echo 1)" "AC12 the reverted wrapper fires the ban: $(tr '\n' ' ' < "$S/ban/hits.reverted")"
    check_step "$([ ! -s "$S/ban/hits.comment" ] && echo 0 || echo 1)" "AC12 a comment spelling the idiom stays silent"
    ;;
  *) echo "FAIL  unknown case $c"; fails=$((fails + 1)) ;;
  esac
done
exit "$fails"
