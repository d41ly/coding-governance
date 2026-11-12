#!/usr/bin/env bash
# check-microformats.sh — grade the charter's micro-format DEFINITIONS against their own grammar.
#
#   bash <prefix>/check-microformats.sh [<file>]
#
# SUBJECT. The RULESET — `coding-governance-agents.template.md` — because that is the source. A
# target's rendered charter carries the same block, and it is proved equal to this one by
# `<prefix>/playbook/adopt-playbook.sh --check` rather than graded twice. With no argument the gate
# reads the template beside the playbook-render kit's engine, where an install lands it, and gov's
# root template where that kit holds none; an argument still wins (PLAY-dOrderedCharter-80 S4).
#
# WHAT IT KEYS ON. The HTML-comment fence pair around the definition list, and nothing else. It
# cannot key on a heading: the section has none. It cannot key on a column-zero list marker either,
# because the emission rule de-indents the definitions into siblings of the section's own prose
# rules, so a marker-anchored selector would select the whole section. Each marker is a WHOLE line,
# as every reader of the fence finds it: a marker inside a longer line is no marker, so it counts
# zero and the gate cannot run. Check 9 refuses a head two definitions share, because a reader
# keeping a head's first definition and one keeping its last would read two different shapes. Check
# 10 refuses a field whose head word is a credential word, `pw`, `pass`, `passwd`, `password`,
# `secret`, `token` or `apikey`, in any case.
#
# WHAT IT DOES NOT CHECK, said here rather than implied away: it holds SYNTAX. Whether a shape's
# FIELDS are the right fields is a design question this gate has no opinion about, and a shape that
# is perfectly well-formed and semantically wrong passes.
#
# Exit 0 = every definition satisfies the grammar · 1 = an offender · 2 = could not run.
set -u
# The interpreter the sibling-kit resolver runs under, INLINED byte-identically from the
# canonical copy named on its marker line, since this gate ships alone (PLAY-dOrderedCharter-80 S4).
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
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. `resolve_kit_dir <python> <home> <anchor> <here>` prints the kit directory ABSOLUTE, since
# the subject's repository need not be the one this gate sits in, or the resolver's named refusal
# on stderr and exits 1.
resolve_kit_dir() {
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
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
  "$1" -c "${_rkd%$'\n'}"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
print(d.as_posix())' "$2" "$3" "$4"
}

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "check-microformats: not a git tree"; exit 2; }

# THE SUBJECT WITH NO ARGUMENT (PLAY-dOrderedCharter-80 S4): the template beside the playbook-render
# kit's engine, `render_playbook.py` the anchor, found BEFORE the `cd` because the resolver's `here`
# reads against the caller's directory. Where no python runs, the resolver refuses or the kit's
# directory holds no template, gov's root template as before: at gov the kit holds none.
FILE=${1:-}
if [ -z "$FILE" ]; then
  FILE=coding-governance-agents.template.md
  case "${BASH_SOURCE[0]:-}" in */*) _self_dir=${BASH_SOURCE[0]%/*} ;; *) _self_dir=. ;; esac
  if _py=$(resolve_python "" 2>/dev/null) \
     && _kd=$(resolve_kit_dir "$_py" playbook render_playbook.py "$_self_dir" 2>/dev/null); then
    _kd=${_kd%$'\r'}
    [ -f "$_kd/coding-governance-agents.template.md" ] && FILE=$_kd/coding-governance-agents.template.md
  fi
fi
cd "$ROOT" || exit 2
OPEN='<!-- microformats -->'
CLOSE='<!-- /microformats -->'
# The frozen SENTINEL. The keyword set is DERIVED from the block — a hand-typed copy inside this gate
# would be a mirror of the subject it grades, which the charter forbids by name. That derivation can
# break silently and certify an empty set, so one membership is pinned.
SENTINEL=committed

status=0
fail() { printf 'MICROFORMAT check %s FAILED — %s\n' "$1" "$2"; status=1; }

[ -f "$FILE" ] || { echo "check-microformats: no such file: $FILE"; exit 2; }

n_open=$(grep -cxF "$OPEN" "$FILE" || true)
n_close=$(grep -cxF "$CLOSE" "$FILE" || true)
if [ "$n_open" -ne 1 ] || [ "$n_close" -ne 1 ]; then
  echo "check-microformats: the definition block is not delimited by exactly one fence pair in"
  echo "check-microformats: $FILE — found $n_open opener(s) and $n_close closer(s). A gate that"
  echo "check-microformats: cannot find its block must say so, never report a clean set."
  exit 2
fi

block=$(awk -v o="$OPEN" -v c="$CLOSE" '$0 == o {f=1; next} $0 == c {f=0} f' "$FILE")
defs=$(printf '%s\n' "$block" | grep -E '^- `.*`$' || true)
n_defs=$(printf '%s\n' "$defs" | grep -c . || true)

if [ "$n_defs" -eq 0 ]; then
  echo "check-microformats: the fence pair is present and encloses no definition line, so every"
  echo "check-microformats: predicate below would pass over an empty set."
  exit 2
fi

keywords=$(printf '%s\n' "$defs" | sed -E 's/^- `([^ ]+).*/\1/')
if ! printf '%s\n' "$keywords" | grep -qx "$SENTINEL"; then
  fail 1 "the keyword derivation lost its frozen sentinel member, so the derivation is broken rather than the block being empty: expected to find $SENTINEL"
fi

nl=$'\n'; seen=$nl; reported=$nl
while IFS= read -r line; do
  [ -n "$line" ] || continue
  body=${line#- \`}; body=${body%\`}
  head=${body%% — *}
  # ---- a head defined twice (TOOL-aOrientedCast-25). The readers disagree on which definition
  #      wins: the hooks kit's format guard and the run-log kit keep the last, so one charter would
  #      read as two shapes to any reader keeping the first. Refused here, at the source every reader
  #      shares, once per head. Fork-free, so it adds no loop, heredoc or substitution.
  case "$seen" in
    *"$nl$head$nl"*)
      if [[ $reported != *"$nl$head$nl"* ]]; then
        fail 9 "a definition head is defined more than once, so a reader keeping its first definition and one keeping its last read two different shapes: $head"
        reported+="$head$nl"
      fi ;;
    *) seen+="$head$nl" ;;
  esac
  # ---- the joiner appears exactly once
  n_join=$(printf '%s' "$body" | grep -o ' — ' | grep -c . || true)
  if [ "$n_join" -ne 1 ]; then
    fail 2 "a definition carries $n_join joiners rather than exactly one, so its head and tail cannot be told apart: $body"
    continue
  fi
  # ---- the joiner's POSITION: nothing but the head precedes it. A separate predicate from the
  # ---- count, because three shapes once satisfied the count while failing the position.
  # THERE IS NO ⏳ EXEMPTION HERE, and there used to be one that could not be taken. The arm read
  # `[ "$head" = "⏳" ] || fail 3`, guarded by a case matching heads that CONTAIN A SPACE — and the
  # hourglass head is three bytes with no space in it, so the case never selected it and the equality
  # was never evaluated. Re-derived over the live block: all heads print space-free. The glyph passes
  # this predicate the same way every keyword does, by being one token; the exemption only told a
  # reader it was special. `memory/gotchas/armed-but-unreachable-rule.md` is the class.
  case "$head" in
    *" "*) fail 3 "a definition puts a field ahead of its joiner, so the head is not one keyword: $body" ;;
  esac
  # ---- parentheses, outside markdown-link syntax
  stripped=$(printf '%s' "$body" | sed -E 's/\[[^]]*\]\([^)]*\)//g')
  case "$stripped" in
    *"("*|*")"*) fail 4 "a definition carries a bare parenthesis, which the grammar admits only as markdown-link syntax: $body" ;;
  esac
  # ---- a colon acting as a joiner or a label. Glued to a value (a port) is legal.
  case "$body" in
    *": "*) fail 5 "a definition uses a colon as a label, which the grammar admits only glued to a value: $body" ;;
  esac
  # ---- the FIELD SEPARATOR. Tail fields break on ' · ' and on nothing else. Added by
  #      TOOL-aHonedRuleset-8's closing review: the charter's connective said a gate held this and
  #      no arm did, so a definition separating fields with a comma or a semicolon passed at exit 0.
  #      Commas INSIDE an opaque field are legal -- the grammar binds shape, never value bytes -- so
  #      this greps the field breaks the shape defines, which are the ones outside <...> and `...`.
  sep=$(printf '%s' "$body" | sed -E 's/<[^>]*>//g; s/`[^`]*`//g')
  case "$sep" in
    *";"*) fail 7 "a definition breaks a tail field on a semicolon, and the grammar admits only ' · ': $body" ;;
  esac
  # ---- ALTERNATION is the ASCII pipe and lives INSIDE a placeholder. A bare pipe in the tail is a
  #      field break the grammar does not define. Same finding, same review.
  case "$sep" in
    *"|"*) fail 8 "a definition carries a bare ASCII pipe outside a placeholder, and the grammar admits alternation only inside <...>: $body" ;;
  esac
  # ---- no field asks for a credential (PLAY-dOrderedCharter-2 S5). A tail field whose head word is a
  #      credential word asks for a secret's value in chat; the shape names where it lives instead
  #      (`up`'s `creds in <where-they-live>`). Each field is split on ' · ' with no fork.
  rest=${body#* — }
  while [ -n "$rest" ]; do
    field=${rest%% · *}
    case "$rest" in *" · "*) rest=${rest#* · } ;; *) rest= ;; esac
    word=${field%% *}
    shopt -s nocasematch   # bash 3.1's case-blind match, where ${word,,} needs bash 4
    case "$word" in
      pw|pass|passwd|password|secret|token|apikey)
        fail 10 "a definition field asks for a credential, and a shape names where one lives, never its value: $word in $body" ;;
    esac
    shopt -u nocasematch
  done
  # ---- placeholders are lowercase angle-bracket names
  while IFS= read -r ph; do
    [ -n "$ph" ] || continue
    case "$ph" in
      *[A-Z]*) fail 6 "a placeholder is not a lowercase angle-bracket name: $ph in $body" ;;
    esac
  done <<EOF
$(printf '%s' "$body" | grep -oE '<[^>]+>' || true)
EOF
done <<EOF
$defs
EOF

[ "$status" -eq 0 ] && printf 'microformats OK — %d definition(s) graded, %d keyword(s) derived\n' \
  "$n_defs" "$(printf '%s\n' "$keywords" | sort -u | grep -c .)"
exit "$status"
