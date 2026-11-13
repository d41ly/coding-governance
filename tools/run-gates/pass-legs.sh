#!/usr/bin/env bash
# pass-legs.sh — the declared pass legs, run over ONE pass's diff through the bar runner.
# TOOL-aNimbleMend-5.
#
#   bash <this kit>/pass-legs.sh --base <rev>
#
# Exit: the runner's own code, unchanged. 0 too when `pass.fast-legs` is off or cannot be read, and
# when no row carries the field. 2 when --base is absent or resolves to no commit, with nothing run.
#
# WHAT IT DOES. It holds no leg command and no verdict logic. It filters the leg manifest to the
# rows whose `pass_leg` is true (`pass_legs.py` derives that field), writes them to
# `<git-dir>/gate-pass-legs.json`, each with its `argv` behind `bash <kit>/run-held-wsl.sh --leg`,
# the shim that unsets `GATE_LEGS`, so every pass leg reads the manifest beside its kit and only the
# list the runner starts is narrow. It starts `run-gates.sh` beside it ONCE with that file as
# `GATE_LEGS`, the resolved base as `GATE_BASE`, a pinned `GATE_RUN_ID` of the form
# `pass-<UTC stamp>-<pid>`, and `GATE_FULL` and `GATE_SELFTESTS` EMPTY, so each leg's own guard
# decides against the pass's diff and a flag the calling session exported cannot widen the run.
# `GATE_TURNSTILE=0`: the run starts beside a queued bar instead of behind it, because a run that
# waits out another worktree's bar cannot be held to a budget of its own.
#
# THE RUNNER'S OUTPUT IS NEVER CAPTURED. A captured runner is bounded through a pipe, which is not
# bounded. Only the two small python calls are read.
#
# THE RECORD, `<git-dir>/gate-pass-legs.txt`, `key TAB value` per line, replaced on every run that
# got as far as reading the manifest: run_id, base, head, started, exit, verdict, declared, wall_s,
# budget_s, limit_s, over, held, and one `leg TAB name TAB status TAB seconds` line per declared leg.
# A declared leg with no row in the runner's record reads `not-run`: its guard skipped it, or the
# runner held it.
#
# TWO FINDINGS, each one stdout line opening `pass-legs: FINDING`, and NEITHER MOVES THE EXIT CODE:
# the wall time around the runner call went over `PASS_LIMIT_SECONDS`, and the runner held a
# declared leg. Over `PASS_BUDGET_SECONDS` and inside the limit is a `pass-legs: NOTE` line. Both
# figures are constants of `pass_legs.py`, read from it at each run and typed nowhere here.
#
# WHAT IT DOES NOT CHECK. Whether the declared list is the rule's own output or inside its budget:
# those are `pass_legs.py --check` and `--budget`. Which legs a guard skipped for a good reason. And
# it scrubs no runner knob beyond the two named above: an inherited `GATE_DOCS_BASE` or `GATE_REUSE`
# reaches the runner as the caller set it. A caller's own `GATE_LEGS` is the manifest filtered, and
# its legs still grade the one beside the kit.
#
# WHAT A RUN COSTS THE BAR'S RECORDS is in this kit's README, under the pass-leg runner.
set -u
KITDIR=$(cd "$(dirname "$0")" && pwd)

# The python-launcher resolver, INLINED byte-identically from its canonical copy: this kit is
# copy-installed and gov's lib dir travels to nobody. The parity gate finds this copy by its marker.
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
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file; the launcher's own name
        # otherwise. The `[ -f ]` HOLDS on a Windows App Execution Alias, so a Store Python whose
        # own sys.executable is an alias is echoed as printed: a gap the run-gates kit's
        # check_app_alias closes for the legs it measures, and this block does not.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
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
    # LAST, verbatim: the first line names the refusal and this one the candidates, and the lines
    # between them carry the outcomes, the overrides and the install (TOOL-dSafePassage-26 S20).
    echo "resolve_python: tried:$_rp_tried"
  } >&2
  return 1
}
# <<< resolve_python

# The sibling-kit resolver, inlined the same way and read ONCE into a variable by a builtin. The
# `|| :` is owed because `read -d ''` returns 1 at the end of its input.
RKD_PROGRAM=""
IFS= read -r -d '' RKD_PROGRAM <<'RKD' || :
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

# ---- 1. the one argument -------------------------------------------------------------------------
# A value opening with `-` is refused here, so nothing git could read as an option reaches it.
case "$#:${1:-}:${2:-}" in
  2:--base:-*|2:--base:) _pl_usage=1 ;;
  2:--base:*) _pl_usage=0 ;;
  *) _pl_usage=1 ;;
esac
if [ "$_pl_usage" = 1 ]; then
  echo "pass-legs: usage: bash pass-legs.sh --base <rev> — --base is required and names the commit the pass started from; nothing ran" >&2
  exit 2
fi
PL_ASK=$2

# ---- 2. the git dir and the base -----------------------------------------------------------------
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "pass-legs: not a git repo" >&2; exit 2; }
cd "$ROOT" || exit 2
PL_GD=$(git rev-parse --absolute-git-dir 2>/dev/null) || { echo "pass-legs: no git dir resolves" >&2; exit 2; }
# An unresolvable base must stop HERE: the runner reads one as empty and runs every leg.
PL_BASE=$(git rev-parse --verify -q "$PL_ASK^{commit}" 2>/dev/null) || PL_BASE=""
if [ -z "$PL_BASE" ]; then
  echo "pass-legs: --base '$PL_ASK' resolves to no commit, so nothing ran" >&2
  exit 2
fi
PL_HEAD=$(git rev-parse --verify -q HEAD 2>/dev/null) || PL_HEAD="-"

PYBIN=$(resolve_python) || { echo "pass-legs: no usable python — required to read the leg manifest" >&2; exit 2; }

# ---- 3. the switch, asked once and before anything starts ----------------------------------------
# The ask contract's five rows (the policy kit's README): on acts; off is absent and silent; no
# policy kit acts with one NOTE; a refused read is absent under the reader's own line, which goes
# to stderr uncaptured; any other value is absent under one line naming it.
PL_POLICY=$("$PYBIN" -I -c "${RKD_PROGRAM%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$KITDIR" 2>/dev/null) || PL_POLICY=""
PL_POLICY=${PL_POLICY%$'\r'}
if [ -z "$PL_POLICY" ]; then
  echo "pass-legs: NOTE - no policy kit resolves beside this kit, so pass.fast-legs reads on." >&2
else
  PL_ANSWER=$("$PYBIN" "$PL_POLICY/policy.py" get pass.fast-legs) || exit 0
  PL_ANSWER=${PL_ANSWER%$'\r'}
  case "$PL_ANSWER" in
    on) ;;
    off) exit 0 ;;
    *) echo "pass-legs: pass.fast-legs answered '$PL_ANSWER', which is neither on nor off, so no pass leg ran." >&2
       exit 0 ;;
  esac
fi

# ---- 4. the list and the two figures, one python call --------------------------------------------
# `read_manifest` is the declaration module's own reader, so `GATE_LEGS` outranks the kit dir's
# sibling here exactly as it does there. Each selected row is copied in manifest order with its
# `argv` behind the leg shim (TOOL-aNimbleMend-13): the runner exports `GATE_LEGS` to every leg, and
# a leg that reads it as its subject must grade the manifest beside its kit, never this filtered
# list. The shim is the held tier's own, named by `held_halves.SHIM`; an import that fails ends
# this call, and the `|| exit 2` below, with nothing run.
PL_FIGURES=$("$PYBIN" -B -c '
import json, os, sys
sys.path.insert(0, sys.argv[1])
import held_halves
import pass_legs
try:
    _text, legs = pass_legs.read_manifest()
except pass_legs.Refusal as e:
    sys.exit("pass-legs: REFUSED — %s" % e)
rows = [dict(l, argv=["bash", held_halves.SHIM, "--leg"] + list(l.get("argv") or []))
        for l in legs if l.get("pass_leg") is True]
tmp = "%s.%d.tmp" % (sys.argv[2], os.getpid())
with open(tmp, "w", encoding="utf-8", newline="\n") as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)
    f.write("\n")
os.replace(tmp, sys.argv[2])
sys.stdout.reconfigure(newline="\n")
print("%d %d %d" % (len(rows), pass_legs.PASS_BUDGET_SECONDS, pass_legs.PASS_LIMIT_SECONDS))
' "$KITDIR" "$PL_GD/gate-pass-legs.json") || exit 2
read -r PL_DECLARED PL_BUDGET PL_LIMIT <<<"${PL_FIGURES%$'\r'}"
case "$PL_DECLARED:$PL_BUDGET:$PL_LIMIT" in
  *[!0-9:]*|:*|*::*|*:) echo "pass-legs: the declaration module answered '$PL_FIGURES', which is not three integers, so nothing ran" >&2; exit 2 ;;
esac

# ---- 5 to 7. the runner, once, timed by the shell's own clock ------------------------------------
PL_STARTED=$(date -u +%Y-%m-%dT%H:%M:%SZ)
PL_RUN="-"; PL_RC="-"; PL_WALL=0
if [ "$PL_DECLARED" -gt 0 ]; then
  PL_RUN="pass-$(date -u +%Y%m%dT%H%M%SZ)-$$"
  _pl_t0=$SECONDS
  GATE_LEGS="$PL_GD/gate-pass-legs.json" GATE_BASE="$PL_BASE" GATE_RUN_ID="$PL_RUN" GATE_FULL= GATE_SELFTESTS= \
    GATE_TURNSTILE=0 "${BASH:-bash}" "$KITDIR/run-gates.sh"
  PL_RC=$?
  PL_WALL=$((SECONDS - _pl_t0))
fi

# ---- 8. the record and the findings --------------------------------------------------------------
# Every status and count is COPIED from the runner's own record of this run id; the one comparison
# made here is the wall time against the two declared figures.
"$PYBIN" -B -c '
import json, os, sys
gd, run_id, base, head, started, rc = sys.argv[1:7]
wall, budget, limit = (int(a) for a in sys.argv[7:10])
with open(os.path.join(gd, "gate-pass-legs.json"), encoding="utf-8") as f:
    names = [l["name"] for l in json.load(f)]
run = os.path.join(gd, "gate-run", run_id)
keys, rows = {}, {}
try:
    with open(os.path.join(run, "verdict"), encoding="utf-8", errors="replace") as f:
        for line in f:
            k, _, v = line.rstrip("\r\n").partition("\t")
            keys[k] = v
except OSError:
    pass
# A retried leg leaves `<i>.retry.leg` beside `<i>.leg`; sorted last, the retry row wins.
for fn in sorted(os.listdir(run) if os.path.isdir(run) else [], key=lambda n: n.endswith(".retry.leg")):
    if not fn.endswith(".leg"):
        continue
    try:
        with open(os.path.join(run, fn), encoding="utf-8", errors="replace") as f:
            fields = f.read().rstrip("\r\n").split("\t")
    except OSError:
        continue
    if len(fields) >= 4:
        rows[fields[0]] = (fields[1], fields[3])
held = keys.get("held", "0")
verdict = "EMPTY" if not names else keys.get("verdict") or "NO-VERDICT"
over = "limit" if wall > limit else "tolerance" if wall > budget else "none"
out = [("run_id", run_id), ("base", base), ("head", head), ("started", started), ("exit", rc),
       ("verdict", verdict), ("declared", len(names)), ("wall_s", wall), ("budget_s", budget),
       ("limit_s", limit), ("over", over), ("held", held)]
text = "".join("%s\t%s\n" % kv for kv in out)
text += "".join("leg\t%s\t%s\t%s\n" % ((n,) + rows.get(n, ("not-run", "-"))) for n in names)
path = os.path.join(gd, "gate-pass-legs.txt")
tmp = "%s.%d.tmp" % (path, os.getpid())
fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
    f.write(text)
os.replace(tmp, path)
sys.stdout.reconfigure(encoding="utf-8", errors="replace", newline="\n")
if not names:
    print("pass-legs: 0 legs declared, nothing ran")
if over == "limit":
    print("pass-legs: FINDING overrun: the run took %ds, over the %ds limit (budget %ds)" % (wall, limit, budget))
elif over == "tolerance":
    print("pass-legs: NOTE the run took %ds, inside the tolerance above the %ds budget" % (wall, budget))
if held.isdigit() and int(held) > 0:
    print("pass-legs: FINDING held: %s declared leg(s) did not run, held as a self-test or a kit-subject leg" % held)
' "$PL_GD" "$PL_RUN" "$PL_BASE" "$PL_HEAD" "$PL_STARTED" "$PL_RC" "$PL_WALL" "$PL_BUDGET" "$PL_LIMIT" \
  || echo "pass-legs: the run record at $PL_GD/gate-pass-legs.txt was not written" >&2

[ "$PL_RC" = "-" ] && exit 0
exit "$PL_RC"
