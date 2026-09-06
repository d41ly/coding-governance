# lib-selftest.sh — a self-test harness whose unit of cost is not a process. TOOL-aQuenchedHarness-5.
#
# SOURCED, never executed. Three verbs and nothing else: `build_fixture`, `arm`, `run_arms`. It is not
# a test framework — no discovery, no fixtures-by-convention, no assertion library. Those exist and
# this repo does not need one; what it needs is for 11.7 hours of declared self-test budget to stop
# being 11.7 hours.
#
# ---- WHAT THE MEASUREMENT SAID, because every decision below follows from it and none of it was
# ---- reasoned out in advance. `memory/builds/aQuenchedHarness/build/2026-09-07-build-TOOL-aQuenchedHarness-5-candidate-test.md`
# ---- traced `tools/check-line-length.test.sh`: 36 s, 18 arms, and the dominant term is the SUBJECT'S
# ---- OWN COST PER INVOCATION — 31 python spawns in the outer script alone at 773 ms each, before
# ---- counting the 12 python call sites inside the subject that `bash -x` cannot see. Not the
# ---- harness. Not fixture construction, which is three file writes.
#
# So the only lever that removes cost WITHOUT changing what is asserted is PARALLELISM. Batching the
# subject was rejected (each arm asks one question about a different staged break, and a checker that
# accepted N trees would be a public surface added for its own test); rewriting arms in-process was
# rejected (the subjects are shell scripts, so in-process means re-implementing them, and then the
# suite grades the re-implementation).
#
# ---- AND WHY THE SNAPSHOT IS NOT AN OPTIMISATION. The suites share ONE fixture directory and mutate
# ---- it in place before every arm:
# ----     W="$TMP/repo";  reset() { ... > "$W/subject.md"; ... }
# ---- Run two of those arms concurrently and the second's setup lands inside the first's subject
# ---- invocation. Naive parallelism does not make such a suite faster, it makes it WRONG — and wrong
# ---- in the worst way, because the arms still pass most of the time. The per-arm COPY is what buys
# ---- isolation, the isolation is what makes the pool safe, and the pool is what removes the cost.
# ---- The candidate test's own §8 F1 had these two as alternatives to choose between. They compose.

# ---------------------------------------------------------------------------------------------
# STATE. Deliberately globals rather than a struct: this is sourced into a shell script, and a
# caller that has to marshal a handle is a caller that will not adopt it.
SELFTEST_ROOT=""          # the one mktemp -d for the whole suite
SELFTEST_SNAPSHOT=""      # the built fixture, copied per arm
SELFTEST_ARM_TIMEOUT=${SELFTEST_ARM_TIMEOUT:-120}
_st_n=0                   # arms DECLARED, which is also the reporting order
_st_spawn_base=0

# THE POOL WIDTH IS READ, NOT RESOLVED. `run-selftests.sh` computes the composite bound and exports
# it, because this harness and that runner each reading the profile row independently is 8x8 = 64
# concurrent processes on a host where a bare spawn costs 319 ms. Falling back to 1 rather than to
# the profile width is deliberate: an unset variable means nobody bounded the product, and serial is
# the only safe answer to that.
_st_width() { local w=${SELFTEST_INNER_WIDTH:-1}; case "$w" in ''|*[!0-9]*) w=1 ;; esac
              [ "$w" -ge 1 ] || w=1; printf '%s' "$w"; }

# ---------------------------------------------------------------------------------------------
# build_fixture <builder>  — run the builder ONCE, snapshot what it made.
#
# The builder is a shell function or command; it is invoked with CWD inside a fresh directory and
# should populate it. Whatever it leaves behind becomes the snapshot every arm starts from.
build_fixture() {
  [ $# -ge 1 ] || { echo "lib-selftest: build_fixture needs a builder" >&2; return 2; }
  SELFTEST_ROOT=$(mktemp -d) || { echo "lib-selftest: cannot create a scratch root" >&2; return 2; }
  SELFTEST_SNAPSHOT="$SELFTEST_ROOT/snapshot"
  mkdir -p "$SELFTEST_SNAPSHOT" || return 2
  ( cd "$SELFTEST_SNAPSHOT" && "$@" ) || {
    echo "lib-selftest: the fixture builder failed, so every arm below would grade a fixture that was never built" >&2
    return 2; }
  _st_spawn_base=$(_st_spawns)
  return 0
}

# A SPAWN COUNTER, so a suite's cost is attributable to a NUMBER and not to a stopwatch on a box
# whose load moves 10x. Counts processes on this host; the delta across a run is what matters, and
# the absolute value is meaningless. Best-effort: a host where it cannot count reports `-`, which is
# a different thing from reporting 0.
_st_spawns() { ps -ef 2>/dev/null | wc -l 2>/dev/null || printf -- '-'; }

# ---------------------------------------------------------------------------------------------
# arm <label> <want-rc> <want-substring> <setup> <subject>
#
# DECLARES an arm; it does not run one. That is the whole API change from the shape these suites use
# today, and it is what lets `run_arms` schedule them. `setup` and `subject` are shell strings,
# eval'd with CWD inside this arm's OWN copy of the snapshot.
#
# An EMPTY want-substring means "do not grade the output", for an arm whose only claim is the exit
# code. It is spelled as an empty string rather than omitted, so a caller who forgets the argument
# gets an arity error instead of silently losing the assertion.
arm() {
  [ $# -eq 5 ] || { echo "lib-selftest: arm takes exactly 5 arguments (label, want-rc, want-substring, setup, subject)" >&2; return 2; }
  [ -n "$SELFTEST_ROOT" ] || { echo "lib-selftest: arm called before build_fixture" >&2; return 2; }
  _st_n=$((_st_n + 1))
  local d="$SELFTEST_ROOT/arm.$_st_n"
  mkdir -p "$d" || return 2
  printf '%s\n' "$1" > "$d/label"
  printf '%s\n' "$2" > "$d/want_rc"
  printf '%s\n' "$3" > "$d/want_out"
  printf '%s\n' "$4" > "$d/setup"
  printf '%s\n' "$5" > "$d/subject"
}

# One arm, in its own copy. Runs in a subshell from the pool; writes a verdict file and nothing else,
# so the parent reads results from disk and never from a variable a background job cannot set.
_st_run_one() {
  local i=$1 d="$SELFTEST_ROOT/arm.$i" w="$SELFTEST_ROOT/work.$i"
  rm -rf "$w" 2>/dev/null
  # THE COPY. Filesystem work, not process creation, and it is what makes the pool safe.
  cp -a "$SELFTEST_SNAPSHOT" "$w" 2>/dev/null || { printf 'ERR\tcould not copy the snapshot\n' > "$d/verdict"; return; }
  local setup subject want_rc want_out out rc
  setup=$(cat "$d/setup"); subject=$(cat "$d/subject")
  want_rc=$(cat "$d/want_rc"); want_out=$(cat "$d/want_out")
  if ! ( cd "$w" && eval "$setup" ) >"$d/setup.out" 2>&1; then
    printf 'ERR\tthe arm setup failed: %s\n' "$(head -1 "$d/setup.out" 2>/dev/null)" > "$d/verdict"; return
  fi
  # CAPTURED THROUGH A FILE AND BOUNDED, never through a command substitution: `out=$(timeout N cmd)`
  # reads until EOF, and EOF arrives only when the last inherited write end closes — so a surviving
  # grandchild holds the pipe and the bound applies to the verdict rather than to the clock. The
  # runner beside this harness records that failure costing 51.4 s against a 1 s bound.
  if command -v timeout >/dev/null 2>&1; then
    ( cd "$w" && eval "$subject" ) >"$d/out" 2>&1 &
    local pid=$!
    ( sleep "$SELFTEST_ARM_TIMEOUT"; kill -9 "$pid" 2>/dev/null ) >/dev/null 2>&1 &
    local killer=$!
    wait "$pid" 2>/dev/null; rc=$?
    kill "$killer" 2>/dev/null
  else
    ( cd "$w" && eval "$subject" ) >"$d/out" 2>&1; rc=$?
  fi
  out=$(cat "$d/out" 2>/dev/null)
  if [ "$rc" = "$want_rc" ] && { [ -z "$want_out" ] || printf '%s' "$out" | grep -qF -- "$want_out"; }; then
    printf 'ok\t\n' > "$d/verdict"
  else
    printf 'FAIL\texpected rc %s%s, got %s: %s\n' "$want_rc" \
      "${want_out:+ naming '$want_out'}" "$rc" "$(printf '%s' "$out" | head -2 | tr '\n' ' ')" > "$d/verdict"
  fi
}

# ---------------------------------------------------------------------------------------------
# run_arms [<suite label>] — execute every declared arm, report in DECLARATION order, return 1 on
# any failure.
#
# REPORTING IS ORDER-STABLE WHATEVER THE WIDTH. Arms execute in whatever order the pool frees a slot;
# output is rendered by index afterwards. A suite whose output moves with the width is a suite whose
# byte-pins cannot be trusted, and this repo pins suite output in several places.
run_arms() {
  local label=${1:-selftest}
  # A SUITE THAT DECLARED NOTHING MUST NOT PRINT A GREEN LINE. An empty population and a clean sweep
  # are indistinguishable from outside, which is the class this repo names in a dozen places.
  if [ "$_st_n" -eq 0 ]; then
    echo "$label: NO ARMS were declared, so this run graded nothing at all" >&2
    return 2
  fi
  local w; w=$(_st_width)
  local i=1 live=0
  while [ "$i" -le "$_st_n" ]; do
    _st_run_one "$i" &
    live=$((live + 1))
    if [ "$live" -ge "$w" ]; then wait -n 2>/dev/null || wait; live=$((live - 1)); fi
    i=$((i + 1))
  done
  wait
  local fails=0 j=1 v rest st
  while [ "$j" -le "$_st_n" ]; do
    v="$SELFTEST_ROOT/arm.$j/verdict"
    st=$(cut -f1 "$v" 2>/dev/null); rest=$(cut -f2- "$v" 2>/dev/null)
    case "$st" in
      ok) printf 'ok    %s\n' "$(cat "$SELFTEST_ROOT/arm.$j/label")" ;;
      *)  fails=$((fails + 1))
          printf 'FAIL  %s — %s\n' "$(cat "$SELFTEST_ROOT/arm.$j/label")" "${rest:-no verdict was written}" ;;
    esac
    j=$((j + 1))
  done
  local spawned="-"
  local now; now=$(_st_spawns)
  case "$now$_st_spawn_base" in *-*) ;; *) spawned=$(( now - _st_spawn_base )) ;; esac
  echo "----"
  if [ "$fails" -eq 0 ]; then
    printf 'PASS (%s arms, width %s)\n' "$_st_n" "$w"
  else
    printf 'FAIL (%s of %s arms, width %s)\n' "$fails" "$_st_n" "$w"
  fi
  rm -rf "$SELFTEST_ROOT" 2>/dev/null
  [ "$fails" -eq 0 ]
}
