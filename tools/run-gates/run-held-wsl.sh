#!/usr/bin/env bash
# run-held-wsl.sh — the held self-test tier split in two: the Linux-safe legs in WSL2 from a mirror on
# WSL's own ext4 disk, the declared Windows-only legs natively, one combined verdict. TOOL-aSparedSpawn-5.
#
#   bash <prefix>/run-gates/run-held-wsl.sh            # one combined run; held-green once parity holds
#   bash <prefix>/run-gates/run-held-wsl.sh --paired   # the WSL legs on BOTH hosts; records parity only
#   bash <prefix>/run-gates/run-held-wsl.sh --setup    # clone this node's WSL mirror, once
#
# Two internal modes, each reached only through the modes above:
#   --half <S> <tree> <out>   the WSL half, run INSIDE WSL from the worktree at S
#   --leg <argv…>             every partition row's leg: GATE_LEGS unset, then exec
#
# Exit: the combiner's. 0 GREEN, 1 RED, 2 REFUSED, 3 TREE MOVED, 4 HOST.
#
# THE HOST is resolved by `held_halves.py --host`, never typed here: a node's distro and mirror from
# `<git-common-dir>/gate-wsl.conf`, else WSL's default distro and the shared default mirror in
# `.githooks/gate-env.sh`, each printed with its source on every run.
#
# EACH HALF IS AN ORDINARY RUNNER INVOCATION over a partition manifest through `GATE_LEGS`, with
# `GATE_FULL=1 GATE_SELFTESTS=1`, in a tree whose git dir no boundary reads: the Windows half in a
# scratch `git clone --local` of S, the WSL half in a detached worktree of the mirror. So neither half
# can write this clone's `gate-full-green`, and only the combiner writes `held-green` here.
#
# WSL NEVER WRITES THE WINDOWS `.git`. The mirror's remote `win` is a FETCH source only, every
# `wsl.exe` runs with `WSLENV` empty so no `GIT_DIR` crosses, and MSYS path conversion is off for
# those calls so a Linux path reaches WSL as written.
#
# WHAT THIS DOES NOT CHECK. It does not prove a WSL green means what a Windows green means — the
# paired runs and the combiner's parity record do that, for the legs both hosts ran. It does not set
# up a node: `--setup` clones, and a distro, a writable mirror parent and git's ownership rules for
# `/mnt/c` are the owner's to provide. No boundary reads `held-green`.
set -u

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

# THE LEG SHIM, first and cheap: the runner exports GATE_LEGS to every leg, and both canaries read it
# as their subject, so a leg of a partition must not inherit the partition. The runner maps a python
# launcher at argv[0] to its resolved one, and argv[0] is now `bash`, so the shim maps it instead.
if [ "${1:-}" = --leg ]; then
  shift
  unset GATE_LEGS
  case "${1:-}" in
    python|python3) PYBIN=$(resolve_python) || exit 127; set -- "$PYBIN" "${@:2}" ;;
  esac
  exec "$@"
fi

print_refusal() { echo "run-held-wsl: REFUSED — $*" >&2; exit 2; }

# The remote --setup names as the mirror's hosted origin, by the lander's ladder: a literal remote
# name is what the remote-literals gate bans in kit code.
# >>> remote_ladder_sh -- canonical copy: resolve-remote.sh in the gov lib dir (byte-identical; gated)
# resolve_remote_sh -> RR_REMOTE RR_BRANCH RR_OBSERVED RR_WHY, rc 0; rc 1 with RR_WHY on a refusal.
# The ladder, row for row, is resolve_remote.py in the gov lib dir: GOV_REMOTE, else the current
# branch remote unless it is ".", else the ONLY remote; several and none chosen, or a name that is
# no remote here, refuses naming GOV_REMOTE; no remote at all is RR_REMOTE="" and rc 0. RR_OBSERVED
# is what <remote>/HEAD names; RR_BRANCH is GOV_DEFAULT_BRANCH, else RR_OBSERVED. Fetches nothing.
# RR_GIT names the git command, so a caller holding a pinned wrapper function passes it.
resolve_remote_sh() {
  local _rr_git=${RR_GIT:-git} _rr_names _rr_n _rr_list _rr_cur _rr_where _rr_how=GOV_REMOTE _rr_head _rr_bad
  RR_REMOTE=${GOV_REMOTE:-}; RR_BRANCH=""; RR_OBSERVED=""; RR_WHY=""
  _rr_names=$("$_rr_git" remote 2>/dev/null) || _rr_names=""
  _rr_n=$(printf "%s" "$_rr_names" | grep -c . || true)
  _rr_list=$(printf "%s" "$_rr_names" | tr "\n" " ")
  [ -n "$_rr_list" ] || _rr_list=none
  # FULL refs, never `--short`: a tag or branch sharing the name makes the short form ambiguous.
  _rr_cur=$("$_rr_git" symbolic-ref --quiet HEAD 2>/dev/null) || _rr_cur=""
  case "$_rr_cur" in refs/heads/?*) _rr_cur=${_rr_cur#refs/heads/} ;; *) _rr_cur="" ;; esac
  if [ -z "$RR_REMOTE" ] && [ -n "$_rr_cur" ]; then
    RR_REMOTE=$("$_rr_git" config "branch.$_rr_cur.remote" 2>/dev/null) || RR_REMOTE=""
    _rr_how="branch.$_rr_cur.remote"
    [ "$RR_REMOTE" != . ] || RR_REMOTE=""
  fi
  if [ -z "$RR_REMOTE" ] && [ "$_rr_n" -eq 1 ]; then RR_REMOTE=$_rr_names; fi
  if [ -z "$RR_REMOTE" ] && [ "$_rr_n" -gt 1 ]; then
    _rr_where="a detached HEAD"; [ -z "$_rr_cur" ] || _rr_where="branch $_rr_cur"
    RR_WHY="cannot choose a remote: GOV_REMOTE is unset, $_rr_where has no configured remote, and this repository has $_rr_n remotes ($_rr_list). Name it: export GOV_REMOTE=<remote>."
    return 1
  fi
  # A name holding whitespace is no remote: `grep -F` would split it into several patterns.
  case "$RR_REMOTE" in *[[:space:]]*) _rr_bad=1 ;; *) _rr_bad=0 ;; esac
  if [ -n "$RR_REMOTE" ] && { [ "$_rr_bad" = 1 ] || ! printf "%s\n" "$_rr_names" | grep -qxF -- "$RR_REMOTE"; }; then
    RR_WHY="$_rr_how names $RR_REMOTE, which is no remote of this repository ($_rr_list). Name one that is: export GOV_REMOTE=<remote>."
    RR_REMOTE=""
    return 1
  fi
  if [ -n "$RR_REMOTE" ]; then
    _rr_head=$("$_rr_git" symbolic-ref --quiet "refs/remotes/$RR_REMOTE/HEAD" 2>/dev/null) || _rr_head=""
    case "$_rr_head" in "refs/remotes/$RR_REMOTE"/?*) RR_OBSERVED=${_rr_head#"refs/remotes/$RR_REMOTE"/} ;; esac
  fi
  RR_BRANCH=${GOV_DEFAULT_BRANCH:-$RR_OBSERVED}
  return 0
}
# <<< remote_ladder_sh

KITDIR=$(cd "$(dirname "$0")" && pwd) || print_refusal "cannot resolve this script's directory"
KITREL=$(unset GIT_DIR GIT_WORK_TREE; cd "$KITDIR" && git rev-parse --show-prefix 2>/dev/null) \
  || print_refusal "this script's directory $KITDIR is not inside a git work tree"
KITREL=${KITREL%/}
[ -n "$KITREL" ] || print_refusal "this script sits at its repository's root, so no kit path derives"
MANIFEST_REL="$(dirname "$KITREL")/gate-legs.json"

# One half: partition, run, collect. The run record is copied out of the half's own git dir, so the
# combiner never reads a git dir it did not ask about.
run_half() { # <host> <tree> <half dir> <partition half> <run id>
  local host=$1 tree=$2 hd=$3 part=$4 id=$5 s gd rc
  mkdir -p "$hd" || return 2
  s=$EPOCHSECONDS
  ( cd "$tree" && "$PYBIN" "$KITREL/held_halves.py" --partition --half "$part" --out "$hd/partition.json" ) \
    > "$hd/partition.log" 2>&1 || { cat "$hd/partition.log" >&2; return 2; }
  ( cd "$tree" && unset GATE_REUSE GIT_DIR GIT_WORK_TREE GIT_COMMON_DIR GIT_INDEX_FILE \
      && GOV_PYTHON=$PYBIN GATE_LEGS="$hd/partition.json" GATE_FULL=1 GATE_SELFTESTS=1 GATE_RUN_ID="$id" \
         bash "$KITREL/run-gates.sh" ) > "$hd/stdout" 2> "$hd/stderr" < /dev/null
  rc=$?
  gd=$(git -C "$tree" rev-parse --absolute-git-dir 2>/dev/null) || gd=""
  [ -n "$gd" ] && cp "$gd/gate-run/$id/verdict" "$gd/gate-run/$id/header" "$hd/" 2>/dev/null
  printf 'host\t%s\nrun_id\t%s\nsha\t%s\nmanifest_blob\t%s\nwall_s\t%s\nrunner_rc\t%s\n' \
    "$host" "$id" "$(git -C "$tree" rev-parse HEAD 2>/dev/null)" \
    "$(git -C "$tree" rev-parse "HEAD:$MANIFEST_REL" 2>/dev/null)" "$((EPOCHSECONDS - s))" "$rc" > "$hd/meta"
  return 0
}

# ---- THE WSL HALF, inside WSL ---------------------------------------------------------------------
if [ "${1:-}" = --half ]; then
  [ "$#" = 4 ] || print_refusal "--half takes <S> <tree> <out>"
  S=$2 TREE=$3 OUT=$4
  case "$TREE" in /mnt/*) print_refusal "the half's tree $TREE is on a Windows drive, not WSL's ext4 disk" ;; esac
  # S8: no Windows binary on PATH, scratch on the mirror's own filesystem, no git location inherited.
  _p=""; IFS=: read -ra _parts <<<"$PATH"
  for _d in "${_parts[@]}"; do case "$_d" in /mnt/*) ;; *) _p="${_p:+$_p:}$_d" ;; esac; done
  export PATH=$_p
  unset GIT_DIR GIT_WORK_TREE GIT_COMMON_DIR GIT_INDEX_FILE GATE_LEGS GATE_REUSE
  export TMPDIR="$TREE.tmp"; mkdir -p "$TMPDIR" || print_refusal "cannot create $TMPDIR"
  if command -v tasklist.exe >/dev/null 2>&1; then print_refusal "a Windows binary is still reachable on PATH"; fi
  [ "$(git -C "$TREE" rev-parse HEAD 2>/dev/null)" = "$S" ] || print_refusal "the worktree $TREE is not at $S"
  PYBIN=$(resolve_python) || print_refusal "no usable python inside WSL"
  run_half wsl "$TREE" "$OUT" wsl "held-wsl-${TREE##*/}"
  exit $?
fi

# ---- THE WINDOWS SIDE ------------------------------------------------------------------------------
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) ;;
  *) print_refusal "run this from the Windows side; inside WSL only --half and --leg apply" ;;
esac
MODE=run
case "${1:-}" in
  "") ;;
  --paired) MODE=paired ;;
  --setup) MODE=setup ;;
  *) print_refusal "unknown argument '${1}'; the modes are --paired and --setup, or none" ;;
esac
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || print_refusal "not inside a git work tree"
cd "$ROOT" || exit 2
# AC6: a dirty tree refuses before anything else, because WSL sees committed objects only.
[ "$MODE" = setup ] || [ -z "$(git status --porcelain 2>/dev/null)" ] \
  || print_refusal "the tree is dirty, and the WSL half can only see committed objects"
PYBIN=$(resolve_python) || print_refusal "no usable python"
HOSTOUT=$("$PYBIN" "$KITDIR/held_halves.py" --host) || { printf '%s\n' "$HOSTOUT"; exit 2; }
printf '%s\n' "$HOSTOUT"
DISTRO=$(sed -n 's/^wsl host: distro \([^ ]*\) (.*/\1/p' <<<"$HOSTOUT")
DISTRO_FROM=$(sed -n 's/^wsl host: distro [^ ]* (\(.*\))$/\1/p' <<<"$HOSTOUT")
MIRROR=$(sed -n 's/^wsl host: mirror \([^ ]*\) (.*/\1/p' <<<"$HOSTOUT")
NODE_CONF=$(sed -n 's/^wsl host: node conf \(.*\) (\(declared\|absent\)).*/\1/p' <<<"$HOSTOUT")
[ "$DISTRO" = - ] && DISTRO=""
[ -n "$MIRROR" ] || print_refusal "held_halves.py --host named no mirror"
WSLX=(wsl.exe); [ -n "$DISTRO" ] && WSLX+=(-d "$DISTRO")
run_wsl() { WSLENV= MSYS_NO_PATHCONV=1 MSYS2_ARG_CONV_EXCL='*' "${WSLX[@]}" -e "$@"; }
if ! run_wsl true >/dev/null 2>&1; then
  [ -n "$DISTRO" ] && print_refusal "wsl.exe cannot reach the distro '$DISTRO' that GATE_WSL_DISTRO declares in $NODE_CONF"
  print_refusal "wsl.exe cannot reach WSL's default distro, asked because $NODE_CONF declares no GATE_WSL_DISTRO ($DISTRO_FROM)"
fi

COMMON=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || print_refusal "no git common dir"

if [ "$MODE" = setup ]; then
  case "$COMMON" in */.git) PRIMARY=${COMMON%/.git} ;; *) print_refusal "the common git dir $COMMON is not a .git under a primary tree" ;; esac
  case "$PRIMARY" in
    [A-Za-z]:/*) _drv=${PRIMARY:0:1}; WINSRC="/mnt/${_drv,,}${PRIMARY:2}" ;;
    *) print_refusal "cannot spell the primary tree $PRIMARY as a WSL path" ;;
  esac
  resolve_remote_sh || print_refusal "$RR_WHY"
  [ -n "$RR_REMOTE" ] || print_refusal "this repository has no remote, so no hosted URL can name the mirror's origin"
  GH=$(git remote get-url "$RR_REMOTE" 2>/dev/null) || GH=""
  case "$GH" in https://*|ssh://*|git@*) ;; *) print_refusal "$RR_REMOTE is '$GH', not a hosted URL the mirror's origin can name" ;; esac
  run_wsl test -e "$MIRROR" && print_refusal "$MIRROR already exists inside WSL; --setup clones once"
  run_wsl git clone -q --no-checkout --origin win "$WINSRC" "$MIRROR" || print_refusal "the clone of $WINSRC into $MIRROR failed"
  run_wsl git -C "$MIRROR" remote add origin "$GH" || print_refusal "cannot add origin to $MIRROR"
  echo "run-held-wsl: mirror $MIRROR cloned from $WINSRC; remote win fetches, origin is $GH"
  exit 0
fi

S=$(git rev-parse HEAD) || exit 2
FP=$(bash "$KITDIR/gate-fingerprint.sh") || FP=""
[ -n "$FP" ] || print_refusal "gate-fingerprint.sh gave no fingerprint for this tree"
BLOB=$(git rev-parse "$S:$MANIFEST_REL" 2>/dev/null) || print_refusal "$MANIFEST_REL is not tracked at $S"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)-$$"
SCR=$(mktemp -d "${TMPDIR:-/tmp}/hh.XXXXXX") || print_refusal "cannot create a scratch dir"
WT="$MIRROR.held/$STAMP"
remove_scratch() {
  rm -rf "$SCR" 2>/dev/null
  run_wsl git -C "$MIRROR" worktree remove --force "$WT" >/dev/null 2>&1
  run_wsl rm -rf "$WT.half" "$WT.tmp" >/dev/null 2>&1
}
trap remove_scratch EXIT

run_wsl git -C "$MIRROR" fetch -q win || print_refusal "the mirror $MIRROR could not fetch from its remote win (has --setup run?)"
run_wsl git -C "$MIRROR" cat-file -e "$S^{commit}" \
  || print_refusal "$S is on no branch the mirror fetched, so the WSL half cannot see it"
run_wsl mkdir -p "$MIRROR.held" && run_wsl git -C "$MIRROR" worktree add -q --detach "$WT" "$S" \
  || print_refusal "cannot add a worktree at $S in the mirror"
git clone -q --local --no-checkout "$COMMON" "$SCR/w" && git -C "$SCR/w" checkout -q --detach "$S" \
  || print_refusal "cannot make the Windows half's scratch clone at $S"

echo "run-held-wsl: $MODE run at $S · fingerprint $FP · manifest $BLOB"
WPART=windows; [ "$MODE" = paired ] && WPART=all
run_half windows "$SCR/w" "$SCR/wh" "$WPART" "held-windows-$STAMP" & PW=$!
( run_wsl bash "$WT/$KITREL/run-held-wsl.sh" --half "$S" "$WT" "$WT.half" > "$SCR/wsl.log" 2>&1
  mkdir -p "$SCR/lh" && run_wsl tar -C "$WT.half" -cf - . | tar -xf - -C "$SCR/lh" ) & PL=$!
wait "$PW"; wait "$PL"
[ -s "$SCR/wsl.log" ] && sed 's/^/  wsl half: /' "$SCR/wsl.log" | tail -n 20
PAIRED=(); [ "$MODE" = paired ] && PAIRED=(--paired)
"$PYBIN" "$KITDIR/held_halves.py" --combine --windows "$SCR/wh" --wsl "$SCR/lh" --sha "$S" \
  --fingerprint "$FP" --manifest-blob "$BLOB" "${PAIRED[@]}"
