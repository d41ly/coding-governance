#!/usr/bin/env bash
# check-hook-destinations.sh — every hook path a fragment DECLARES, and every hook destination an
# adopter script WRITES, must resolve to a destination some kit.toml rule actually ships.
#
#   bash <prefix>/check-hook-destinations.sh
#
# WHY THIS EXISTS, and it is not hypothetical. TOOL-dRetiredFork-14 withdrew the `.claude/hooks/`
# destinations for three hooks. Two of the three had their path supplied by a committed FRAGMENT
# rather than by the engine default, and `adopt-memory-recall.sh --with-hook` copied a fourth back
# into `.claude/hooks/` on every run. So the unit written to stop a silent unwiring produced two
# fragments and one installer pointing at a path that had stopped shipping — the exact failure its
# own section 5 called the highest risk in the build. TOOL-dRetiredFork-21.
#
# WHAT THIS DOES NOT CHECK. It does not verify that a settings.json anywhere is wired, that the hook
# FIRES, or that an adopter's installed copy matches gov's. `check-wiring.sh` owns the first, the
# hook's own suite the second, and the parity arms the third. This gate answers one question: does
# every declared hook path name something a descriptor ships. Nor does it observe a target's
# `adopter-owned` hook join: gov keeps no install receipt, so both readers below take the no-receipt
# path here and any comparison of that join would be a probe that cannot move. The join has ONE
# reader, settings-merge.py, which check-wiring.sh calls, and the recall block of
# `check-wiring.test.sh` grades it over crafted receipts (the round-1 closing-diff fold, S5).
#
# HOW A PATH IS RESOLVED, and by whom. This gate does NOT expand `{kit}` or `{here}` itself. It asks
# the two readers that decide the value — `check-wiring.sh --resolve-fragment` and
# `settings-merge.py --resolve-fragment` — and REFUSES when they disagree, so the writer cannot wire
# a path the checker cannot find. A third derivation here would be a third answer to one question,
# and it is exactly what this file used to carry. TOOL-aReplayedCard-2.
#
# A `{here}` FRAGMENT IS JUDGED AT ITS ADOPTER PATH. `{here}` is the fragment's own directory, and
# it exists for a `kind = "flat"` kit: its engine ships to `{prefix}/<file>`, so the in-tree path
# (`skills/session-kickoff/manifest-check.sh`) and the shipped path (`<prefix>/manifest-check.sh` under
# the canonical prefix) DIFFER BY DESIGN, and comparing the in-tree spelling against the declared
# set would red every correct flat-kit fragment. So where the fragment's directory is the `home` of
# at least one flat descriptor, `{prefix}/<path relative to that directory>` is compared against the
# WHOLE declared destination set, both spellings printed. Where it is instead the home of a
# DIRECTORY-shaped descriptor, the kit ships its tree unchanged, the fragment lands in the same
# directory as its engine, and `{here}` names that directory at every prefix — including a kit
# directory an adopter RENAMED, which `{kit}/<name>/` cannot follow (inCMS homes memory-recall at
# `scripts/recall/`; TOOL-aRepatriatedFork-2 S4). That fragment is compared at its in-tree
# resolution, as a `{kit}` one is. A directory that is the home of NO descriptor ships from nowhere,
# and the gate refuses naming it.
set -u
_self_dir=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || _self_dir=""   # before the cd: $0 may be relative
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "hook-dest: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
st=0
# THE TOOL ROOT, DERIVED (TOOL-aRepatriatedFork-29 S3): this gate sits in it, beside the deployer,
# the resolver and the two readers it asks. Underivable is a refusal, never a guessed prefix.
if ! SELF_PRE=$(unset GIT_DIR GIT_WORK_TREE; git -C "$_self_dir" rev-parse --show-prefix 2>/dev/null); then
  echo "hook-dest: cannot derive this gate's own directory from '$_self_dir' — REFUSING"
  exit 2
fi

# TOOL-aRepatriatedFork-46: the resolver is carried INLINE. It was sourced from the library directory
# beside this gate, which ships nowhere, spelled as a kit name after this gate's own prefix.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # The direct executable where the probe named a file, so a consumer never spawns the
        # Windows App Execution Alias again; the candidate's own name otherwise.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
  } >&2
  return 1
}
# <<< resolve_python
PY="$(resolve_python)" || { echo "hook-dest: no usable python — refusing rather than skipping"; exit 2; }

FRAGS=$(git ls-files '*.fragment.json' 2>/dev/null)

# AC5 — AN EMPTY POPULATION IS A REFUSAL. A gate that found no fragments prints the same zero as a
# gate over a clean tree, and this repo has a catalogue entry for exactly that shape. The fragments
# are tracked and this file ships beside them, so zero means the selector broke, not that the tree
# is tidy.
if [ -z "$FRAGS" ]; then
  echo "hook-dest: REFUSING — no *.fragment.json is tracked, so this gate has no subject."
  echo "           A population of zero is a broken selector, not a clean tree."
  exit 1
fi

n=$(printf '%s\n' "$FRAGS" | grep -c .)

# The declared destinations, from the descriptors themselves — never a list typed here. A gate that
# carried its own copy of the shipped set would agree with itself and not with the deployer.
DESTS=$("$PY" - "${SELF_PRE}govkit" <<'PYEOF'
import pathlib, sys
sys.path.insert(0, sys.argv[1])
import govkit
root = pathlib.Path(".").resolve()
reg = govkit.load_registry(root)
out = set()
for eid, (d, _p) in govkit.read_descriptors(root, reg, govkit.Report()).items():
    for row in govkit.resolve_entry(root, d, govkit.canonical_ctx(eid))["survivors"]:
        dst = row.get("dest") or row.get("dst") or row.get("to")
        if isinstance(dst, str):
            out.add(dst)
        elif isinstance(dst, (list, tuple)):
            out.update(x for x in dst if isinstance(x, str))
# At a ROOT install the canonical prefix is ".", so a destination reads "./<kit>/<file>" where the
# readers resolve "<kit>/<file>": one path, two spellings, compared as strings (VERIFYING repair).
print("\n".join(sorted(x[2:] if x.startswith("./") else x for x in out)))
PYEOF
) || { echo "hook-dest: could not resolve the descriptors — refusing"; exit 2; }

[ -n "$DESTS" ] || { echo "hook-dest: REFUSING — the descriptors resolved NO destinations at all"; exit 1; }

# The canonical prefix the destinations above were resolved under, and every `kind = "flat"` home
# — both from the deployer, never typed here. The flat-home set is what decides whether a `{here}`
# fragment ships from anywhere at all.
FLAT=$("$PY" - "${SELF_PRE}govkit" <<'PYEOF'
import pathlib, sys
sys.path.insert(0, sys.argv[1])
import govkit
root = pathlib.Path(".").resolve()
reg = govkit.load_registry(root)
print(govkit.canonical_ctx("hook-dest")["prefix"])
homes = set()
for eid, (d, _p) in govkit.read_descriptors(root, reg, govkit.Report()).items():
    # A flat home at a ROOT install resolves to "", the directory `dirname` spells "." (VERIFYING
    # repair: skipping the empty home left every root-level {here} fragment homeless).
    if isinstance(d.get("home"), str):
        homes.add(("F " if d.get("kind") == "flat" else "D ") + (d["home"].rstrip("/") or "."))
print("\n".join(sorted(homes)))
PYEOF
) || { echo "hook-dest: could not read the flat-kit homes — refusing"; exit 2; }
PFX=$(printf '%s\n' "$FLAT" | head -1)
FLAT_HOMES=$(printf '%s\n' "$FLAT" | tail -n +2 | sed -n 's/^F //p')
DIR_HOMES=$(printf '%s\n' "$FLAT" | tail -n +2 | sed -n 's/^D //p')
[ -n "$PFX" ] || { echo "hook-dest: REFUSING — the deployer names no canonical prefix"; exit 1; }
# A ZERO here is a broken selector, not a tree with no flat kits: this repo's own kickoff engine is
# one, and the arm below would otherwise refuse every `{here}` fragment for a reason that is false.
[ -n "$FLAT_HOMES" ] || { echo "hook-dest: REFUSING — the descriptors declare NO kind=flat home, so no flat-kit {here} fragment could be judged"; exit 1; }

echo "hook-dest: $n fragment(s) against $(printf '%s\n' "$DESTS" | grep -c .) declared destination(s), $(printf '%s\n' "$FLAT_HOMES" | grep -c .) flat home(s), prefix $PFX"

# The two readers whose value this gate asserts. Both are asked per fragment, below.
CW="${SELF_PRE}check-wiring.sh"; SM="${SELF_PRE}settings-merge.py"
for r in "$CW" "$SM"; do
  [ -f "$r" ] || { echo "hook-dest: REFUSING — $r is not here, and this gate reads its answer rather than deriving one"; exit 2; }
done

# ---- arm 1: every fragment's hook_path resolves to a declared destination -------------------------
# ---- and the two readers agree on what it resolves to (the parity arm) ---------------------------
for f in $FRAGS; do
  hp=$("$PY" -c 'import json,sys;print(json.load(open(sys.argv[1],encoding="utf-8")).get("hook_path",""))' "$f" 2>/dev/null)
  if [ -z "$hp" ]; then
    echo "hook-dest: FAIL $f declares no hook_path — a fragment with no destination cannot be wired"
    st=1
    continue
  fi
  a=$(bash "$CW" --resolve-fragment "$f" 2>&1); ra=$?
  b=$("$PY" "$SM" --resolve-fragment "$f" 2>&1); rb=$?
  if [ "$ra" != 0 ] || [ "$rb" != 0 ]; then
    echo "hook-dest: FAIL $f — a reader refused it: check-wiring rc=$ra ($a) · settings-merge rc=$rb ($b)"
    st=1
    continue
  fi
  if [ "$a" != "$b" ]; then
    echo "hook-dest: FAIL $f — the two readers DISAGREE: check-wiring resolves '$a', settings-merge '$b'."
    echo "           The writer would wire one path and the checker look for another; a fragment"
    echo "           token has one meaning or the wiring check cannot see what the merge wrote."
    st=1
    continue
  fi
  resolved=$a
  case "$hp" in
    *"{here}"*)
      dir=$(dirname "$f")
      if ! printf '%s\n' "$FLAT_HOMES" | grep -qxF -- "$dir"; then
        if printf '%s\n' "$DIR_HOMES" | grep -qxF -- "$dir"; then
          # A directory kit ships its tree unchanged: the in-tree resolution IS the shipped path.
          if printf '%s\n' "$DESTS" | grep -qxF -- "$resolved"; then
            echo "hook-dest: ok   $f -> $resolved (beside its directory kit's engine)"
          else
            echo "hook-dest: FAIL $f declares hook_path '$hp' -> '$resolved', which NO kit.toml rule ships"
            echo "           from the directory kit homed at '$dir'."
            st=1
          fi
          continue
        fi
        echo "hook-dest: FAIL $f is {here}-shaped but its directory '$dir' is the home of NO descriptor,"
        echo "           so nothing ships it beside its engine and '$resolved' arrives nowhere. A {here}"
        echo "           fragment belongs beside its kit's engine (flat homes: $(printf '%s\n' "$FLAT_HOMES" | paste -sd, -))."
        st=1
        continue
      fi
      adopter="$PFX/${resolved#"$dir"/}"; adopter="${adopter#./}"   # "." is a root install's prefix
      if printf '%s\n' "$DESTS" | grep -qxF -- "$adopter"; then
        echo "hook-dest: ok   $f -> $resolved in the tree, ships as $adopter"
      else
        echo "hook-dest: FAIL $f declares hook_path '$hp' -> '$resolved' in the tree, which would ship as"
        echo "           '$adopter' — and NO kit.toml rule delivers that. A flat kit's fragment is judged at"
        echo "           its adopter path, and this one names a file the kit does not ship beside it."
        st=1
      fi
      ;;
    *)
      if printf '%s\n' "$DESTS" | grep -qxF -- "$resolved"; then
        echo "hook-dest: ok   $f -> $resolved"
      else
        echo "hook-dest: FAIL $f declares hook_path '$hp' -> '$resolved', which NO kit.toml rule ships."
        echo "           A fragment naming a path no descriptor delivers is a wiring hole: the merge"
        echo "           writes the command, the file never arrives, and every matching tool call runs"
        echo "           the interpreter against nothing."
        st=1
      fi
      ;;
  esac
done

# ---- arm 2: no adopter script installs a hook into a destination nothing declares -----------------
# The fragment half above would have passed the whole time `adopt-memory-recall.sh` was re-creating
# `.claude/hooks/recall-opened.js`, because that installer never reads a fragment. A gate over
# declarations alone cannot see an installer, which is why this arm quantifies over the scripts.
ADOPTERS=$(git ls-files "${SELF_PRE}*/adopt-*.sh" 2>/dev/null)
if [ -z "$ADOPTERS" ]; then
  echo "hook-dest: REFUSING — no adopter script is tracked, so arm 2 has no subject"
  exit 1
fi
for a in $ADOPTERS; do
  # a WRITE into a hooks directory: cp/install/mv naming a path under some */hooks/
  hits=$(grep -nE '(cp|install|mv)[^|;&]*\.claude/hooks/' "$a" 2>/dev/null || true)
  if [ -n "$hits" ]; then
    echo "hook-dest: FAIL $a installs a hook into .claude/hooks/, which no kit.toml rule ships:"
    printf '%s\n' "$hits" | sed 's/^/           /'
    echo "           gov withdrew that destination; an installer that re-creates it hands the"
    echo "           adopter back the duplicate and a stale instruction naming it."
    st=1
  fi
done
[ "$st" = 0 ] && echo "hook-dest: clean — every declared hook path resolves, and no adopter writes an undeclared one"
exit $st
