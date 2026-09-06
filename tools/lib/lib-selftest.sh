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

# THE DECLARATIONS LIVE IN ARRAYS, NOT IN FILES, and that is the difference between this harness
# helping and this harness BEING the cost. The first draft wrote five files per arm and read them
# back with `cat`, then read the captured output with `cat` and tested it with `grep` — eleven
# processes of bookkeeping around a subject that costs one. Measured porting the first suite: 62 s
# against the 32 s of the suite it replaced, with the subject itself accounting for 20 s of it. An
# arm runs in a subshell of this one, so it INHERITS these arrays; nothing has to be marshalled.
_st_labels=(); _st_wantrc=(); _st_wantout=(); _st_setup=(); _st_subject=()

# Resolved ONCE. `command -v` per arm is a process per arm to answer a question whose answer cannot
# change during a run.
_st_timeout=""; command -v timeout >/dev/null 2>&1 && _st_timeout=timeout

# AND THE POOL'S REAP IS PROBED ONCE, for a reason that cost this harness its whole speed-up. `wait -n`
# returns the exit STATUS of the job that finished, so `wait -n || wait` reads a red arm as "this
# shell has no wait -n" and falls back to waiting for ALL of them — the pool silently degenerates to
# a barrier per arm, which is serial with extra steps. Measured before the fix: 62 s at width 1 and
# 46 s at width 2, where the width-2 run should have been half.
_st_waitn=0; ( : & wait -n ) >/dev/null 2>&1 && _st_waitn=1

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
# A SECOND CALL STARTS A SECOND BATCH, and before this reset it silently re-ran the first one. The
# arrays and the counter survived `run_arms`, so a suite needing two base fixtures — which is most of
# the suites left to port; one of them needs about twenty-five — declared batch two's arms on top of
# batch one's and graded the OLD arms against the NEW snapshot. Every one of them would have passed or
# failed for reasons unrelated to what it was written to ask. Found by reading, not by running, which
# is why it is fixed here rather than after a port had already been built on it.
build_fixture() {
  [ $# -ge 1 ] || { echo "lib-selftest: build_fixture needs a builder" >&2; return 2; }
  _st_n=0
  _st_labels=(); _st_wantrc=(); _st_wantout=(); _st_setup=(); _st_subject=()
  SELFTEST_ROOT=$(mktemp -d) || { echo "lib-selftest: cannot create a scratch root" >&2; return 2; }
  SELFTEST_SNAPSHOT="$SELFTEST_ROOT/snapshot"
  mkdir -p "$SELFTEST_SNAPSHOT" || return 2
  ( cd "$SELFTEST_SNAPSHOT" && "$@" ) || {
    echo "lib-selftest: the fixture builder failed, so every arm below would grade a fixture that was never built" >&2
    return 2; }
  return 0
}

# THERE IS NO SPAWN COUNTER HERE, and its removal is a finding rather than a tidy-up. One lived here
# — `ps -ef | wc -l` before and after — and `run_arms` computed a delta into a variable it never
# printed, so it cost two 351 ms process walks per run to produce nothing. It could not have produced
# much: it counts processes on the HOST, so under a concurrent bar it reports that box's load and not
# this suite's cost. The number this harness's own build actually used came from
# `PS4='+ ' bash -x <suite>`, counting traced lines whose first token is an external binary, and that
# figure IS attributable. It belongs in the measuring record, not in the thing being measured.

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
  case "$2" in ''|*[!0-9]*)
    echo "lib-selftest: arm '$1' wants rc '$2', which is not a number, so nothing could be compared" >&2
    return 2 ;;
  esac
  _st_n=$((_st_n + 1))
  _st_labels+=("$1"); _st_wantrc+=("$2"); _st_wantout+=("$3")
  _st_setup+=("$4");  _st_subject+=("$5")
}

# ONE PROCESS RUNS BOTH HALVES, and the subject's status still arrives ALONE. An earlier harness in
# this repo ran `sh -c 'setup; gate; cleanup'` and compared the rc of the CLEANUP, so every red arm
# reported 0 and the suite would have certified a gate that never fired. Here the setup's failure
# exits with a distinct status BEFORE the subject is reached, and the subject's own status is written
# to a file rather than returned — so nothing downstream of it can overwrite the number being graded.
_ST_BODY='
  cd "$1" || exit 90
  eval "$2" > "$3.setup" 2>&1 || exit 91
  eval "$4" > "$3.out" 2>&1
  printf %s "$?" > "$3.rc"
'

# One arm, in its own copy. Runs in a subshell from the pool, so it INHERITS the declaration arrays
# and nothing has to be marshalled; it writes a verdict FILE, because the parent cannot read a
# variable a background job set.
#
# THREE PROCESSES PER ARM — the copy, the bound, and the shell that runs the arm — against the eleven
# the first draft spent on bookkeeping around a subject that costs one. That draft wrote five files
# per arm and read them back with `cat`, read the capture with another `cat`, and tested it with
# `grep`; porting the first suite measured it at 62 s against the 32 s of the suite it replaced, with
# the subject itself accounting for only 20 s. A harness whose overhead exceeds its subject is not a
# harness, so every one of those became an array lookup or a builtin.
_st_run_one() {
  local i=$1 k=$(( $1 - 1 )) d="$SELFTEST_ROOT/arm.$i" w="$SELFTEST_ROOT/work.$i"
  # THE COPY. Filesystem work, not process creation, and it is what makes the pool safe.
  cp -a "$SELFTEST_SNAPSHOT" "$w" 2>/dev/null || { printf 'ERR\tcould not copy the snapshot\n' > "$d/verdict"; return; }

  # BOUNDED WITH `timeout`, not with a sleep-and-kill pair: that pair cost two more processes per arm
  # and left its `sleep` orphaned whenever the arm finished early. Capturing to a FILE is what makes
  # `timeout` safe here — `out=$(timeout N cmd)` reads until EOF, and a surviving grandchild holds the
  # pipe open, so the bound would apply to the verdict rather than to the clock. The runner beside
  # this harness records that exact failure costing 51.4 s against a 1 s bound.
  local -a cmd=(bash -c "$_ST_BODY" _ "$w" "${_st_setup[$k]}" "$d/x" "${_st_subject[$k]}")
  [ -n "$_st_timeout" ] && cmd=(timeout -k 5 "$SELFTEST_ARM_TIMEOUT" "${cmd[@]}")
  "${cmd[@]}" >/dev/null 2>&1
  local outer=$?

  if [ "$outer" = 91 ]; then
    # `read` with a redirect is a BUILTIN, so even the failure path forks nothing — and the failure
    # path is the one a wedged suite takes once per arm.
    local why=""; IFS= read -r why < "$d/x.setup" 2>/dev/null
    printf 'ERR\tthe arm setup failed: %s\n' "$why" > "$d/verdict"; return
  fi
  local rc=""
  [ -r "$d/x.rc" ] && read -r rc < "$d/x.rc"
  if [ -z "$rc" ]; then
    printf 'ERR\tthe subject recorded no status (runner exit %s) — it was cut off at the %ss arm bound, or could not start\n' \
      "$outer" "$SELFTEST_ARM_TIMEOUT" > "$d/verdict"; return
  fi

  # THE WHOLE CAPTURE, READ BY A BUILTIN. `read -d ""` stops at NUL, which a text subject never
  # emits, so it takes the file entire; it returns non-zero at EOF, which is why `out` is seeded.
  local out="" want_rc=${_st_wantrc[$k]} want_out=${_st_wantout[$k]} hit=1
  IFS= read -r -d '' out < "$d/x.out" 2>/dev/null
  if [ -z "$want_out" ]; then hit=0
  else case "$out" in *"$want_out"*) hit=0 ;; esac
  fi
  if [ "$rc" = "$want_rc" ] && [ "$hit" = 0 ]; then
    printf 'ok\t\n' > "$d/verdict"
  else
    local snip=${out//$'\n'/ }
    printf 'FAIL\texpected rc %s%s, got %s: %s\n' "$want_rc" \
      "${want_out:+ naming '$want_out'}" "$rc" "${snip:0:200}" > "$d/verdict"
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
  # AND A SUITE THAT SHRINKS is the same defect one arm at a time. Every suite ported onto this
  # harness carried its own `FLOOR_ASSERTIONS` guard for exactly this; the guard lives here so that
  # eighteen ports do not carry eighteen copies of it, and it is a REFUSAL when unreadable rather
  # than a silent 0 — an unparseable floor and no floor at all are indistinguishable from outside.
  local floor=${SELFTEST_FLOOR:-0}
  case "$floor" in ''|*[!0-9]*)
    echo "$label: SELFTEST_FLOOR is '$floor', which is not a number, so the shrink guard graded nothing" >&2
    return 2 ;;
  esac
  if [ "$floor" -gt 0 ] && [ "$_st_n" -lt "$floor" ]; then
    echo "$label: declared $_st_n arm(s), below the pinned floor of $floor — this suite has SHRUNK" >&2
    return 1
  fi
  local w; w=$(_st_width)
  # EVERY ARM'S RESULT DIRECTORY IN ONE CALL. Per-arm `mkdir` is one more process per arm to create a
  # path whose name was known before the run began.
  local i=1; local -a dirs=()
  while [ "$i" -le "$_st_n" ]; do dirs+=("$SELFTEST_ROOT/arm.$i"); i=$((i + 1)); done
  mkdir -p "${dirs[@]}" || return 2

  i=1; local live=0
  while [ "$i" -le "$_st_n" ]; do
    _st_run_one "$i" &
    live=$((live + 1))
    if [ "$live" -ge "$w" ]; then
      if [ "$_st_waitn" = 1 ]; then wait -n; live=$((live - 1)); else wait; live=0; fi
    fi
    i=$((i + 1))
  done
  wait
  # READ BY BUILTINS, off the declaration arrays. The labels were never on disk to begin with, and
  # `read` with a redirect forks nothing — this loop used to spend three processes per arm rendering
  # a line.
  local fails=0 j=1 v line st rest
  while [ "$j" -le "$_st_n" ]; do
    v="$SELFTEST_ROOT/arm.$j/verdict"
    line=""; IFS= read -r line < "$v" 2>/dev/null
    st=${line%%$'\t'*}; rest=${line#*$'\t'}
    case "$st" in
      ok) printf 'ok    %s\n' "${_st_labels[$((j - 1))]}" ;;
      *)  fails=$((fails + 1))
          printf 'FAIL  %s — %s\n' "${_st_labels[$((j - 1))]}" "${rest:-no verdict was written}" ;;
    esac
    j=$((j + 1))
  done
  echo "----"
  if [ "$fails" -eq 0 ]; then
    printf 'PASS (%s arms, width %s)\n' "$_st_n" "$w"
  else
    printf 'FAIL (%s of %s arms, width %s)\n' "$fails" "$_st_n" "$w"
  fi
  rm -rf "$SELFTEST_ROOT" 2>/dev/null
  [ "$fails" -eq 0 ]
}
