#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-3
# TOOL-aSparedSpawn-3 — the pass's direct checks: the runner itself, driven over hand-built fixture
# repositories with a tiny manifest of sleep and hang legs. No suite, no slice of one.
#
# Usage: bash <this file> <dir holding the run-gates.sh under test> <scratch root> <case>...
#   cases: ac1 (prints AC2's lines too), ac3, ac4, ac5, ac6, ac7
# Run it once against the base runner (`git show <base>:tools/run-gates/run-gates.sh` into a dir) to
# see the criteria red, and once against the working tree's to see them green. Every line is `ok` or
# `FAIL`, naming the values it read; the exit status is the count of FAIL lines.
set -u
KITSRC=$1; S=$2; shift 2
REPO=$(cd "$(dirname "$0")/../../../.." && pwd)
mkdir -p "$S"
fails=0
check_step() { if [ "$1" = 0 ]; then echo "ok    $2"; else echo "FAIL  $2"; fails=$((fails+1)); fi; }
build_fixture() { # dir · manifest json — a committed scratch repo carrying the runner under test
  local t=$1
  rm -rf "$t"; mkdir -p "$t/tools/run-gates" "$t/tools/lib" "$t/fx"
  cp "$KITSRC/run-gates.sh" "$REPO/tools/run-gates/gate-fingerprint.sh" "$REPO/tools/run-gates/gate-profiles.txt" \
    "$t/tools/run-gates/"
  cp "$REPO/tools/lib/resolve-python.sh" "$t/tools/lib/"
  printf '%s\n' "$2" > "$t/tools/gate-legs.json"
  printf '#!/usr/bin/env bash\nexit 0\n' > "$t/fx/ok.sh"
  # sleeps, then lists the runner's work dir (the parent of the TMPDIR the runner exports to legs)
  printf '#!/usr/bin/env bash\nsleep "$1"\nls "$TMPDIR/.." > "$FX_PEEK" 2>/dev/null\nexit 0\n' > "$t/fx/sleep.sh"
  # hangs on its first attempt, dropping a flag outside the tree, and passes on every later one
  printf '#!/usr/bin/env bash\n[ -f "$FX_FLAG" ] && exit 0\n: > "$FX_FLAG"\nsleep 60\n' > "$t/fx/once.sh"
  printf '#!/usr/bin/env bash\nsleep 60\n' > "$t/fx/hang.sh"
  ( cd "$t" && git init -q -b main . && git config user.email fx@test.invalid && git config user.name fx \
      && git add -A && git commit -qm seed && git remote add origin ../origin.git \
      && git update-ref refs/remotes/origin/main HEAD \
      && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main ) >/dev/null 2>&1
}
run_fixture_bar() { # dir · output file · VAR=value…
  local t=$1 o=$2; shift 2
  rm -f "$S/nofloor"   # a bar writes its floor here, and a later case would then read one
  ( cd "$t" && env GATE_FULL= GATE_BASE= GATE_REUSE= GATE_WALL= GATE_SELFTESTS= GATE_ATTRIBUTE= \
      GATE_RUN_ID= GATE_PROFILES= GATE_JOBS=2 GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_MEMPAUSE=0 \
      GATE_SPAWN_FLOOR="$S/nofloor" "$@" bash tools/run-gates/run-gates.sh > "$o" 2>&1; echo $? > "$o.rc" )
}
read_leg_field() { awk -F'\t' -v n="$2" 'NR == 1 { print $n }' "$1" 2>/dev/null; }
read_run_dir() { printf '%s/.git/gate-run/%s' "$1" "$(cat "$1/.git/gate-run/current" 2>/dev/null)"; }
read_dispatch() { awk -F'\t' '$1 == "dispatch" { print $2 }' "$(read_run_dir "$1")/header" 2>/dev/null; }

for c in "$@"; do
  case "$c" in
  ac1)
    T="$S/ac1"; export FX_FLAG="$S/ac1.flag" FX_PEEK="$S/ac1.peek"; rm -f "$FX_FLAG" "$FX_PEEK"
    build_fixture "$T" '[{"name": "sleeper", "argv": ["bash", "fx/sleep.sh", "20"]},
 {"name": "once", "argv": ["bash", "fx/once.sh"], "ceiling": 3}]'
    run_fixture_bar "$T" "$S/ac1.out"
    d=$(read_run_dir "$T"); rs=$(read_leg_field "$d/1.retry.leg" 5); se=$(read_leg_field "$d/0.leg" 6)
    check_step "$({ [ -n "$rs" ] && [ -n "$se" ] && [ "$rs" -lt "$se" ]; } && echo 0 || echo 1)" \
      "AC1 the retry's row starts at $rs, the sleeper's ends at $se"
    check_step "$(grep -qx '1.defer' "$FX_PEEK" 2>/dev/null && echo 0 || echo 1)" \
      "AC1 the work dir held a marker for leg 1 when the sleeper ended: $(grep defer "$FX_PEEK" 2>/dev/null | tr '\n' ' ')"
    grep -E '^(GATE|----)' "$S/ac1.out" > "$S/ac1.lines"
    check_step "$([ "$(grep -cE '^GATE (ok|retry) +once ' "$S/ac1.out")" = 2 ] && echo 0 || echo 1)" \
      "AC2 the leg prints exactly its deferral and one pass"
    sed 's/^/        /' "$S/ac1.lines"
    ;;
  ac3)
    # a 30 s ceiling and a 50 s wall, which fires by 55 s at its 5 s poll: the tail retry starts after
    # the first attempt's 30 s and runs 30 s more, so it is alive at 55 s, and it starts before 50 s
    # whenever the release takes under about 18 s (10 to 14 s measured on node a, the worker's own
    # post-processing included).
    T="$S/ac3"; export FX_PEEK="$S/ac3.peek"
    build_fixture "$T" '[{"name": "sleeper", "argv": ["bash", "fx/sleep.sh", "120"]},
 {"name": "stall", "argv": ["bash", "fx/hang.sh"], "ceiling": 30}]'
    run_fixture_bar "$T" "$S/ac3.out" GATE_WALL=50
    check_step "$(grep -q 'still running at the wall: stall (its serial retry)' "$S/ac3.out" && echo 0 || echo 1)" \
      "AC3 the breach names the leg whose retry it stopped"
    check_step "$(grep -qE '^GATE (ok|FAIL) +stall ' "$S/ac3.out" && echo 1 || echo 0)" \
      "AC3 no line claims a verdict for it"
    grep -E '^(GATE|----|gates|  still)' "$S/ac3.out" | sed 's/^/        /'
    ;;
  ac4)
    T="$S/ac4"; export FX_PEEK="$S/ac4.peek"
    build_fixture "$T" '[{"name": "sleeper", "argv": ["bash", "fx/sleep.sh", "25"]},
 {"name": "stubborn", "argv": ["bash", "fx/hang.sh"], "ceiling": 3}]'
    run_fixture_bar "$T" "$S/ac4.out"
    check_step "$(grep -cx 'GATE FAIL  stubborn  (timed out after 3s, again on its serial retry; no spawn floor is recorded for this clone, so HOST was not measured)' "$S/ac4.out" | grep -qx 1 && echo 0 || echo 1)" \
      "AC4 one FAIL line, today's serial wording and the serial attempt's HOST note"
    d=$(read_run_dir "$T"); se=$(read_leg_field "$d/0.leg" 6)
    ts=$(read_leg_field "$d/1.tail.leg" 5); tst=$(read_leg_field "$d/1.tail.leg" 2); rs=$(read_leg_field "$d/1.retry.leg" 5)
    check_step "$({ [ "$tst" = timeout ] && [ -n "$ts" ] && [ "$ts" -lt "$se" ]; } && echo 0 || echo 1)" \
      "AC4 the tail attempt ran beside the sleeper and was set aside: start $ts, status $tst, sleeper end $se"
    check_step "$({ [ -n "$rs" ] && [ "$rs" -ge "$se" ]; } && echo 0 || echo 1)" \
      "AC4 the deciding attempt started after the drain: start $rs"
    grep -E '^(GATE|----)' "$S/ac4.out" | sed 's/^/        /'
    ;;
  ac5|ac6)
    T="$S/$c"
    if [ "$c" = ac5 ]; then
      build_fixture "$T" '[{"name": "a", "argv": ["bash", "fx/ok.sh"]}, {"name": "b", "argv": ["bash", "fx/ok.sh"]},
 {"name": "c", "argv": ["bash", "fx/ok.sh"]}]'
      want="1 2 0"
    else
      build_fixture "$T" '[{"name": "a", "argv": ["bash", "fx/ok.sh"], "ceiling": 20},
 {"name": "b", "argv": ["bash", "fx/ok.sh"], "ceiling": 50}, {"name": "c", "argv": ["bash", "fx/ok.sh"], "ceiling": 30},
 {"name": "d", "argv": ["bash", "fx/ok.sh"], "ceiling": 40}]'
      printf 'a\t10.0\tok\t-\t0\n' > "$T/.git/gate-ledger.tsv"
      want="0 1 3 2"
    fi
    printf '# fixture\na\t1.0\t1\ta\t2026-10-12\trunner\nb\t5.0\t1\ta\t2026-10-12\trunner\nc\t3.0\t1\ta\t2026-10-12\trunner\n' \
      > "$T/tools/run-gates/ceiling-evidence.txt"
    ( cd "$T" && git add -A && git commit -qm evidence ) >/dev/null 2>&1
    run_fixture_bar "$T" "$S/$c.out"
    got=$(read_dispatch "$T")
    check_step "$([ "$got" = "$want" ] && echo 0 || echo 1)" "${c^^} the header's dispatch key reads '$got', want '$want'"
    ;;
  ac7)
    T="$S/ac7"
    build_fixture "$T" '[{"name": "cached", "argv": ["bash", "fx/ok.sh"]}]'
    run_fixture_bar "$T" "$S/ac7a.out"
    run_fixture_bar "$T" "$S/ac7b.out" GATE_REUSE=1
    check_step "$(grep -q '^GATE reuse cached  ' "$S/ac7b.out" && echo 0 || echo 1)" "AC7 control: the second bar reused its one leg"
    check_step "$(awk -F'\t' '$1 == "cached" { f = 1 } END { exit !f }' "$T/.git/gate-ledger.tsv" 2>/dev/null && echo 0 || echo 1)" \
      "AC7 the ledger still holds the reused leg's row: $(wc -l < "$T/.git/gate-ledger.tsv" 2>/dev/null) row(s)"
    ;;
  *) echo "unknown case $c"; fails=$((fails+1)) ;;
  esac
done
exit "$fails"
