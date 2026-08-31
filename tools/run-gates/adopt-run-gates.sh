#!/usr/bin/env bash
# adopt-run-gates.sh — the run-gates kit's adopter and its drift check. the run-gates promotion spec's S7.
#
# WHAT THIS IS FOR. `govkit apply` copies this kit into a target and emits that target's
# `[gate_runner]` declaration from the descriptor's `[gate_runner_seed]` (S9). That declaration
# tells the deployer how to READ this runner's verdicts: a line head for a passing leg, a line head
# for a failing one. Those heads are strings in the runner's own `printf` calls, and nothing else
# joins the two. When the runner's output changes and the declaration does not, the deployer goes on
# parsing a format that no longer exists and reports a target's bar as having run nothing — silently,
# because "no lines matched" and "no legs ran" are the same observation to a reader.
#
# `--check` is that join, asserted. It is the arm S7 exists for and the one AC5 grades.
#
# NOT ADOPTED IS A REAL ANSWER, NOT A SKIP. In gov's own tree there is no target and no
# `.governance/deploy.toml`, so this exits 0 saying so and writes nothing. That is why the criterion
# for it (AC6) is paired with a MUTATION arm in the e2e: a `--check` that does nothing at all also
# exits 0 here, and the two are indistinguishable from this side.
set -u

print_usage() {
  cat >&2 <<'USAGE'
usage: adopt-run-gates.sh [--check] [--target <dir>]
  --check           read-only: assert the target's [gate_runner] declaration still matches the
                    installed runner's output strings. Writes nothing, ever.
  --upgrade         convert the target's JSON leg manifest into <prefix>/gate-legs.toml, carrying
                    the prose its source could only hold as data. REPORTS what else must move; it
                    never edits the target's own files and never deletes the legacy manifest.
  --dry-run         with --upgrade: print the TOML and write nothing.
  --force           with --upgrade: overwrite an existing gate-legs.toml.
  --target <dir>    the adopting repo. Defaults to the tree this kit is installed in.
USAGE
  exit 2
}

MODE=adopt
TARGET=""
DRY=0
FORCE=0
while [ $# -gt 0 ]; do
  case "$1" in
    --check)  MODE=check; shift ;;
    --upgrade) MODE=upgrade; shift ;;
    --dry-run) DRY=1; shift ;;
    --force)   FORCE=1; shift ;;
    --target) [ $# -ge 2 ] || print_usage; TARGET=$2; shift 2 ;;
    -h|--help) print_usage ;;
    *) echo "adopt-run-gates: unknown argument '$1'" >&2; print_usage ;;
  esac
done

# The kit dir, and the tree it is installed in — DERIVED from this script's own location, never
# spelled. A kit that hardcodes its prefix breaks silently at any other install location, and a
# hardcoded prefix in a written artifact is worse: it lands a dead path in the adopter's committed
# tree. Membership and the prefix are both decided through GIT rather than by comparing path
# strings; the block below says why.
KITDIR=$(cd "$(dirname "$0")" && pwd)
if [ -z "$TARGET" ]; then
  TARGET=$(cd "$KITDIR" && git rev-parse --show-toplevel 2>/dev/null) || {
    echo "adopt-run-gates: $KITDIR is not inside a git work tree, and no --target was given" >&2
    exit 2
  }
fi
TARGETN=$(cd "$TARGET" 2>/dev/null && pwd) || { echo "adopt-run-gates: --target '$TARGET' does not exist" >&2; exit 2; }

# MEMBERSHIP IS DECIDED BY GIT IDENTITY, NOT BY COMPARING PATH STRINGS. Under MSYS one directory has
# two spellings — a `/tmp/...` mount and the `/c/Users/.../Temp/...` it resolves to — and mount points
# are not symlinks, so `${KITDIR#"$TARGETN"/}` reports a kit sitting INSIDE the target as being
# outside it. Measured here: this refusal fired on a scratch target the e2e had just built around
# this very kit. Both answers below come from the SAME command run in two directories, so they are
# the same flavour by construction.
kit_top=$(cd "$KITDIR" && git rev-parse --show-toplevel 2>/dev/null) || kit_top=""
tgt_top=$(cd "$TARGETN" && git rev-parse --show-toplevel 2>/dev/null) || tgt_top=""
[ -n "$kit_top" ] && [ "$kit_top" = "$tgt_top" ] || {
  echo "adopt-run-gates: REFUSING — this kit at $KITDIR does not belong to the target tree $TARGETN." >&2
  echo "adopt-run-gates: git reports the kit's tree as '${kit_top:-<none>}' and the target's as" >&2
  echo "adopt-run-gates: '${tgt_top:-<none>}'. Adopting across two trees would write a prefix the" >&2
  echo "adopt-run-gates: target cannot resolve." >&2
  exit 2
}
# The install prefix, relative to the tree BOTH sides just agreed on. Derived through git so the two
# operands share one spelling; a `pwd`-vs-`rev-parse` strip is the defect above.
KITREL=$(cd "$KITDIR" && git rev-parse --show-prefix 2>/dev/null); KITREL=${KITREL%/}
[ -n "$KITREL" ] || KITREL="."

# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
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
# ================= --upgrade (TOOL-aGatheredDeclaration-7) =======================================
# DISPATCHED HERE, before the [gate_runner] declaration is read. Converting a manifest must not
# require that declaration to be current: a target whose deploy.toml has drifted is exactly the
# target most likely to need this verb, and refusing it there would make the tool unreachable from
# the state it exists to leave.
if [ "$MODE" = upgrade ]; then
  # The manifest is the kit dir SIBLING, derived rather than spelled -- the runner's own rule, so a
  # one-segment install resolves it at any prefix.
  PREFIX=$(dirname "$KITREL"); [ "$PREFIX" = "." ] && PREFIX=""
  _mdir=$TARGET${PREFIX:+/$PREFIX}
  PYBIN=$(resolve_python) || { echo "adopt-run-gates: no usable python" >&2; exit 2; }
  # THE INTERPRETER PROBE RUNS BEFORE ANYTHING IS WRITTEN. run-gates.sh PREFERS gate-legs.toml
  # wherever it exists, so writing one into a target whose python predates 3.11 converts a working
  # merge bar into a dead one, and --force is discoverable only after the breakage.
  if ! "$PYBIN" -c "import tomllib" 2>/dev/null; then
    _v=$("$PYBIN" -c "import sys; print(sys.version.split()[0])" 2>/dev/null || echo "version unknown")
    echo "adopt-run-gates: $TARGET resolves python to $PYBIN ($_v), which cannot import tomllib." >&2
    echo "adopt-run-gates: gate-legs.toml needs CPython 3.11+ and the runner PREFERS it wherever it" >&2
    echo "adopt-run-gates: exists, so writing one here would leave this target with a manifest its" >&2
    echo "adopt-run-gates: own bar cannot read. Refusing; nothing was written." >&2
    exit 2
  fi
  _src="$_mdir/gate-legs.json"
  [ -f "$_src" ] || { echo "adopt-run-gates: no ${PREFIX:+$PREFIX/}gate-legs.json in $TARGET to convert" >&2; exit 2; }
  "$PYBIN" "$KITDIR/upgrade_manifest.py" "$_src" "$TARGET/$KITREL/gate-profiles.txt" \
      "$_mdir/gate-legs.toml" "$DRY" "$FORCE" "$TARGET" || exit $?
  exit 0
fi


RUNNER="$KITDIR/run-gates.sh"
[ -f "$RUNNER" ] || { echo "adopt-run-gates: no runner at $RUNNER — this kit is not installed here" >&2; exit 2; }

DECL="$TARGETN/.governance/deploy.toml"
if [ ! -f "$DECL" ]; then
  echo "adopt-run-gates: NOT ADOPTED — $TARGETN carries no .governance/deploy.toml, so there is no"
  echo "adopt-run-gates: [gate_runner] declaration to check against $KITREL/run-gates.sh. Nothing written."
  exit 0
fi

# The declared templates, read out of the target's own descriptor.
#
# THE ARRAY FORM IS THE ONE THAT MATTERS, and the closing review's D2 is why this reads both. The
# deployer's own reader ITERATES these keys, so what a target actually carries is
# `observed_ran = ["GATE ok    {name}"]`. An earlier draft matched only the SCALAR form and returned
# empty on an array — and empty took the "not declared" branch, which reported only because BOTH
# keys were empty. Against a real array declaration with total runner drift it would have said
# NOT ADOPTED and exited 0: failing OPEN, in the one arm whose whole job is to catch that drift.
#
# A key that is absent is DECLARED ABSENT and reported as such; an empty value silently comparing
# equal to nothing is how this class of check passes by finding nothing.
read_declared() {  # KEY -> every declared template, one per line
  sed -n 's/^[[:space:]]*'"$1"'[[:space:]]*=[[:space:]]*\[\(.*\)\][[:space:]]*$/\1/p' "$DECL" \
    | head -1 | grep -oE '"[^"]*"' | sed 's/^"//; s/"$//'
  sed -n 's/^[[:space:]]*'"$1"'[[:space:]]*=[[:space:]]*"\(.*\)"[[:space:]]*$/\1/p' "$DECL" | head -1
}
is_scalar() {  # KEY -> 0 when the descriptor declares it as a bare string
  grep -qE '^[[:space:]]*'"$1"'[[:space:]]*=[[:space:]]*"' "$DECL"
}
RAN=$(read_declared observed_ran)
FAILED=$(read_declared observed_failed)

if [ -z "$RAN" ] && [ -z "$FAILED" ]; then
  echo "adopt-run-gates: NOT ADOPTED — $DECL declares no [gate_runner] observation templates."
  echo "adopt-run-gates: Nothing written."
  exit 0
fi

rc=0
for key in observed_ran observed_failed observed_skipped; do
  is_scalar "$key" || continue
  echo "adopt-run-gates: $key is declared as a STRING in $DECL; it must be an ARRAY of templates."
  echo "adopt-run-gates: The deployer's reader ITERATES this key, so a string is walked character by"
  echo "adopt-run-gates: character: the head becomes one character, no leg name is ever recovered,"
  echo "adopt-run-gates: and every line is classified by whichever state is scanned first. Re-emit"
  echo "adopt-run-gates: the declaration with 'govkit intake'."
  rc=1
done

# The head is the literal prefix BEFORE the runner's own {name} placeholder. That placeholder is the
# RUNNER's substitution, not the deployer's, so it passes through the seed verbatim and is stripped
# here rather than resolved.
extract_head() { printf '%s' "${1%%\{name\}*}"; }

for key in observed_ran observed_failed; do
  vals=$(read_declared "$key")
  [ -n "$vals" ] || { echo "adopt-run-gates: $key is not declared in $DECL"; rc=1; continue; }
  # EVERY template, not only the first: a declaration may carry several, and a drifted one sitting
  # behind a matching one is exactly the silent case this check exists for.
  while IFS= read -r val; do
    [ -n "$val" ] || continue
    h=$(extract_head "$val")
    [ -n "$h" ] || { echo "adopt-run-gates: $key declares '$val', which has no literal head before {name}"; rc=1; continue; }
    if grep -qF -- "$h" "$RUNNER"; then
      [ "$MODE" = check ] && echo "adopt-run-gates: ok   $key head '$h' still appears in $KITREL/run-gates.sh"
    else
      echo "adopt-run-gates: DRIFT — $key declares the head '$h', which no printf in"
      echo "adopt-run-gates: $KITREL/run-gates.sh emits any more. The deployer reads this target's"
      echo "adopt-run-gates: verdicts by matching that head, so it would report a bar that ran nothing"
      echo "adopt-run-gates: rather than a bar whose format moved. Re-emit the declaration, or restore"
      echo "adopt-run-gates: the runner's output strings."
      rc=1
    fi
  done <<EOF
$vals
EOF
done

if [ "$MODE" = check ]; then
  [ "$rc" = 0 ] && echo "adopt-run-gates: the declaration and $KITREL/run-gates.sh agree"
  exit "$rc"
fi

# ADOPT mode writes nothing today, and says so rather than exiting 0 in silence. The declaration is
# emitted by `govkit intake` from this kit's [gate_runner_seed] (S9), because a declaration written
# at configure time cannot reach the same run's leg-emission step — leaving it to the operator means
# the first `apply` after adopting the runner takes the "ORDERED, not emitted" branch and exits 0.
[ "$rc" = 0 ] || exit "$rc"
echo "adopt-run-gates: nothing to write — the [gate_runner] declaration is emitted by"
echo "adopt-run-gates: \`govkit intake\` from this kit's [gate_runner_seed]. This verb exists for"
echo "adopt-run-gates: --check, which is the arm that catches the declaration drifting from the runner."
exit 0
