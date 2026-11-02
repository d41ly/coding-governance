#!/usr/bin/env bash
# check-kit-placeholders.test.sh — red/green arms for <prefix>/check-kit-placeholders.py
# (TOOL-dRetiredFork-19).
#
# HERMETIC: every arm builds its own scratch tree under mktemp -d and never touches the real one, so
# the suite is safe beside the other heavy legs in a concurrent bar.
#
# THE ARM THAT MATTERS MOST is the ESCAPED-SPELLING one. The pre-wiring run over the real tree
# (section 7's rule, and this unit's S5) caught the first draft of the predicate redding 17 innocent
# tokens across five kits: the adopters write the substitution as `${out//\{\{KIT_DIR\}\}/...}` with
# the braces backslash-escaped for the shell, and a predicate matching only the bare `{{KIT_DIR}}`
# finds NOTHING in the one file it exists to read. That arm is what stops the fix regressing.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-kit-placeholders.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
PFX="${KIT_REL:+$KIT_REL/}"

# The shrink-only assertion floor. A suite that stops running arms must RED rather than report a
# smaller success: `check-testsuite-counts.sh` reads this pin, the printed count, and the comparison
# between them, because a pin nothing reads is the same nothing as no pin.
FLOOR_ASSERTIONS=12
GATE="$(cd "$(dirname "$0")" && pwd)/check-kit-placeholders.py"
# The launcher is RESOLVED by running it; `PY=` overrides. A bare default here was the
# parameter-default shape the resolver ban now catches. TOOL-aRepatriatedFork-46: the resolver is
# carried INLINE; it was sourced from the library directory beside this suite, which ships nowhere.
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
[ -n "${PY:-}" ] || PY=$(resolve_python) || exit 2
pass=0; fail=0

arm() {              # $1 = what it asserts, $2 = expected rc, $3 = actual rc, $4 = haystack, $5 = needle
  local ok=1
  [ "$2" = "$3" ] || ok=0
  if [ -n "${5:-}" ]; then case "$4" in *"$5"*) ;; *) ok=0 ;; esac; fi
  if [ "$ok" = 1 ]; then echo "arm ok    $1"; pass=$((pass+1))
  else echo "arm FAIL  $1 (want rc $2, got rc $3)"; echo "$4" | head -3; fail=$((fail+1)); fi
}

# A scratch tree: $1 = root, $2 = the placeholders list body, $3 = the adopter's SPELLING MODE,
# $4 = the [adopt] block body.
#
# $3 IS A MODE, NOT THE TEXT, and that is deliberate. Passing the spelling as a literal meant it
# crossed a single-quote, a printf `%s` (which does NOT expand backslashes in its argument) and a
# `sed` rewrite, and it arrived doubled as `\\{\\{` where a real adopter carries `\{\{` — so the arm
# for the escaped form failed against a fixture that never contained the escaped form. The bytes are
# written HERE, by the format string, where the escaping is read exactly once.
spell() {
  case "$1" in
    escaped) printf 'out=${out//\\{\\{KIT_DIR\\}\\}/"$V"}\n' ;;
    bare)    printf 'out=${out//{{KIT_DIR}}/"$V"}\n' ;;
    *)       printf 'out=$out  # substitutes nothing\n' ;;
  esac
}
scratch() {
  mkdir -p "$1/${PFX}demo"
  cat > "$1/${PFX}demo/kit.toml" <<TOML
[[files]]
include = ["t.md"]
role = "rendered"
placeholders = [$2]

[adopt]
$4
TOML
  { printf '#!/usr/bin/env bash\n# demo adopter\n'; spell "$3"; } > "$1/${PFX}demo/adopt-demo.sh"
}

run() { "$PY" "$GATE" --root "$1" ${2:-} 2>&1; }

# ---- AC3: every declared token substituted -> exit 0, and the run NAMES what it graded.
T=$(mktemp -d); scratch "$T" '"KIT_DIR"' escaped 'argv = ["bash", "{kit}/adopt-demo.sh"]'
o=$(run "$T"); rc=$?
arm "every declared token substituted exits 0" 0 "$rc" "$o" "1 kit(s) graded"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${pass:-1} assertions)" || echo "FAIL (${pass:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi
arm "...and the green line names the pair count" 0 "$rc" "$o" "rule-token pair(s)"

# ---- THE ESCAPED SPELLING. This is the defect S5's pre-wiring run found; without it the gate reds
# ---- every real adopter in the tree.
arm "the shell-ESCAPED spelling counts as substituted" 0 "$rc" "$o" "graded"

# ---- the BARE spelling must also count: a template-renderer may write it unescaped.
T2=$(mktemp -d); scratch "$T2" '"KIT_DIR"' bare 'argv = ["bash", "{kit}/adopt-demo.sh"]'
o2=$(run "$T2"); rc2=$?
arm "the BARE spelling counts as substituted too" 0 "$rc2" "$o2" "graded"

# ---- AC2: a declared token the adopter never substitutes REDS, naming token AND adopter.
T3=$(mktemp -d); scratch "$T3" '"KIT_DIR", "TOOL_ROOT"' escaped 'argv = ["bash", "{kit}/adopt-demo.sh"]'
o3=$(run "$T3"); rc3=$?
arm "an unsubstituted declared token REDS" 1 "$rc3" "$o3" "TOOL_ROOT"
arm "...and the refusal names the adopter that omits it" 1 "$rc3" "$o3" "adopt-demo.sh"

# ---- AC4: an EMPTY population REFUSES. A gate that scanned nothing reports the same zero as a
# ---- clean tree, which is the vacuous-selector shape this repo refuses.
T4=$(mktemp -d); mkdir -p "$T4/${PFX}demo"
printf '[[files]]\ninclude = ["t.md"]\nrole = "engine"\n\n[adopt]\nargv = []\n' > "$T4/${PFX}demo/kit.toml"
o4=$(run "$T4"); rc4=$?
arm "an EMPTY declaring population REFUSES rather than passing" 2 "$rc4" "$o4" "REFUSED"

# ---- a DECLARED `why_no_adopter` is honoured, counted and NAMED — an exemption is not coverage.
T5=$(mktemp -d); scratch "$T5" '"TOOL_ROOT"' none 'argv = []
why_no_adopter = "rendered by the parity gate"'
o5=$(run "$T5"); rc5=$?
arm "a declared why_no_adopter is exempt, not red" 0 "$rc5" "$o5" "exempt by a declared"

# ---- ...and an UNRESOLVABLE adopter with NO declared reason still REDS. The exemption must be
# ---- written down; a missing block is not a silent pass.
T6=$(mktemp -d); scratch "$T6" '"TOOL_ROOT"' none 'argv = []'
o6=$(run "$T6"); rc6=$?
arm "an adopter-less kit with NO stated reason REDS" 1 "$rc6" "$o6" "no resolvable"

# ---- TOOL-aRepatriatedFork-10 S7: a RENDERED template spelling `KEY=value` for a key its own kit's
# ---- conf example declares REDS, naming the key — the shipping repo's value would ship as every
# ---- adopter's. The key is in NO `[config]` list on purpose: the caps a template cites live in the
# ---- example alone, so an arm reading the lists only would pass this fixture by scanning nothing.
T7=$(mktemp -d); scratch "$T7" '"KIT_DIR"' escaped 'argv = ["bash", "{kit}/adopt-demo.sh"]'
printf '\n[config]\nfile = ".demo.conf"\noptional_keys = ["OTHER_KEY"]\n' >> "$T7/${PFX}demo/kit.toml"
printf 'INDEX_CAP_LINES="250"\n' > "$T7/${PFX}demo/.demo.conf.example"
printf 'This repo declares `INDEX_CAP_LINES=0`.\n' > "$T7/${PFX}demo/t.md"
o7=$(run "$T7"); rc7=$?
arm "a rendered template spelling its own kit's conf value REDS" 1 "$rc7" "$o7" "INDEX_CAP_LINES"
# ...and the render form passes: the same key through a placeholder is what the arm asks for.
printf 'This tree declares `INDEX_CAP_LINES={{KIT_DIR}}`.\n' > "$T7/${PFX}demo/t.md"
o8=$(run "$T7"); rc8=$?
arm "the same key rendered through a placeholder passes" 0 "$rc8" "$o8" "spell no conf value"

# ...and a FORMAT description of the value is not a value: a quoted `<placeholder>` states no
# ---- value of gov's, so it passes (gate repair at VERIFYING, TOOL-aRepatriatedFork-10).
printf 'Pinned per gate, `INDEX_CAP_LINES="<gate>:<n>"`.\n' > "$T7/${PFX}demo/t.md"
o9=$(run "$T7"); rc9=$?
arm "a quoted <placeholder> format description is not a conf value" 0 "$rc9" "$o9" "spell no conf value"

rm -rf "$T" "$T2" "$T3" "$T4" "$T5" "$T6" "$T7"
total=$((pass+fail))
if [ "$total" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "check-kit-placeholders: $total assertion(s) executed, below the declared floor of $FLOOR_ASSERTIONS —"
  echo "  arms went missing rather than failing, which reports as success without this check."
  exit 1
fi
[ "$fail" = 0 ] && echo "PASS ($total assertions)"
[ "$fail" = 0 ] || { echo "check-kit-placeholders: $fail of $total assertion(s) failed"; exit 1; }
