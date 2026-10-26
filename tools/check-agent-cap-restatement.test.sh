#!/usr/bin/env bash
# Self-test for check-agent-cap-restatement.sh — TOOL-aDeclaredBound-5.
#
# The gate's whole job is to NAME a bare fan-out number in live prose, so every arm here is about
# whether it can still fire. Its two waiver mechanisms are separate — a PATH PREFIX for frozen trees
# and MATCHED TEXT for live exceptions — and each gets its own red, green and stale arm, because a
# text-keyed waiver written for a frozen record would silence every live carrier sharing the
# sentence, which is the reason the two are not one registry.
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-agent-cap-restatement.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
PFX="${KIT_REL:+$KIT_REL/}"
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME.
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
        # way to the direct executable where the probe named a file, so a consumer never spawns
        # the Windows App Execution Alias again; the launcher's own name otherwise.
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
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
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
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
_rkd_py=$(resolve_python) || { echo "check-agent-cap-restatement.test: no usable python, so the sibling kits cannot be resolved"; exit 2; }
HOOKS_DIR=$(resolve_kit_dir "$_rkd_py" hooks agent-cap.js "$HERE") || exit 2
HOOKS="${HOOKS_DIR##*/}"
GATE="$HERE/check-agent-cap-restatement.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
st=0; n=0

mk() {   # $1 = tree name; builds a repo whose markdown the gate will scan
  R="$TMP/$1"; mkdir -p "$R/memory/builds/tOne" "$R/memory/backlog" "$R/${PFX}"
  ( cd "$R" && git init -q . && git config user.email t@t.test && git config user.name t \
      && git config core.autocrlf false )
  printf '# doc\n' > "$R/README.md"
  : > "$R/waivers.txt"
}
run() {  # runs the gate inside $R with $R/waivers.txt; sets $out and $rc
  ( cd "$R" && git add -A >/dev/null 2>&1 && git commit -q -m f --no-verify >/dev/null 2>&1 || true )
  # POSITIONAL, not an env var. The gate stopped reading `$WAIVERS` because an ambient one greens
  # the bar with no diff; this suite is the reason the knob exists at all, so it uses the shape the
  # gate actually ships rather than a private back door.
  out=$(cd "$R" && bash "$GATE" waivers.txt 2>&1); rc=$?
}
ck() { n=$((n+1)); eval "$2" || { echo "FAIL $1"; st=1; }; }

# ---- RED: a live carrier asserting a bare bound is named.
mk red
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/GUIDE.md"
run
ck "a bare bound in live prose is NAMED"            '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "GUIDE.md"'
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi

# ---- GREEN CONTROL: a digit near a bound word with NO fan-out noun stays silent. This is the real
# ---- sentence from the kickoff engine — "report ≤5 lines" — which an earlier pattern DID flag.
mk green
printf '# rules\n\nStep 1 — Orient (ONE batched command; report ≤5 lines).\n' > "$R/GUIDE.md"
run
ck "a bound with no fan-out noun stays silent"      '[ "$rc" = 0 ]'

# ---- POINTER: the fixed form — no digit, names the resolver — is silent.
mk pointed
printf '# rules\n\nA review spawns at most the total `'"${PFX}${HOOKS}/agent-cap.js"'` resolves.\n' > "$R/GUIDE.md"
run
ck "a pointer with no digit is silent"              '[ "$rc" = 0 ]'

# ---- FROZEN PREFIX: the identical sentence under a frozen tree is excluded by PATH, and the live
# ---- copy sharing that sentence is still named. One fixture, both halves — which is what proves the
# ---- exclusion is a prefix rather than a text match.
mk frozen
printf '# past\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/memory/builds/tOne/README.md"
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/GUIDE.md"
run
ck "a frozen-tree copy is excluded by prefix"       '! printf "%s" "$out" | grep -q "memory/builds"'
ck "...while the live copy sharing its sentence is still named" 'printf "%s" "$out" | grep -q "GUIDE.md"'

# ---- TEXT WAIVER: a live exception is excused by its matched text.
mk waived
printf '# rules\n\nMeasured: at most 5 agents TOTAL in that run.\n' > "$R/GUIDE.md"
printf 'at most 5 agents TOTAL in that run\ta measurement of one run, not the enforced rule\n' > "$R/waivers.txt"
run
ck "a text-keyed waiver excuses its hit"            '[ "$rc" = 0 ]'

# ---- STALE WAIVER: a row whose text is gone reds, because a waiver outliving its hit widens the gate.
mk stale
printf '# rules\n\nnothing to see.\n' > "$R/GUIDE.md"
printf 'at most 5 agents TOTAL in that run\tthe hit this excused is gone\n' > "$R/waivers.txt"
run
ck "a waiver matching nothing reds as STALE"        '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "matches nothing"'

# ---- VACUITY: an empty markdown population is a refusal, never a green. A scanner that passes by
# ---- finding nothing is this repo's own named class.
mk empty
rm -f "$R/README.md"
run
ck "an empty population REFUSES rather than passing" '[ "$rc" = 2 ]'

# ---- SCAN INTEGRITY (H1). A filename holding a SPACE was split by the old batched `xargs grep`
# ---- into fragments that were never opened, and the gate reported a file count taken from the
# ---- LIST rather than from what grep read -- a clean verdict over a file nobody looked at.
mk space
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/Design Notes.md"
run
ck "a filename with a SPACE is scanned, not split"  '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "Design Notes.md"'

# ---- The count must be what grep OPENED. Two files in, two reported.
mk counted
printf '# a\n' > "$R/A.md"; printf '# b\n' > "$R/B.md"; rm -f "$R/README.md"
run
ck "the reported count is the files actually scanned" 'printf "%s" "$out" | grep -q "2 markdown file(s) scanned"'

# ---- SINGLE-FILE POPULATION (H1). `grep` prints no path for a one-file argv unless -H is forced,
# ---- so the remedy said "point at the file" while naming none. A fresh adopter tree IS this case.
mk lone
rm -f "$R/README.md"
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/ONLY.md"
run
ck "a single-file population still names its file"  '[ "$rc" = 1 ] && printf "%s" "$out" | grep -qE "ONLY\.md:[0-9]+:"'

# ---- MEASURED CARRIER SHAPES (H2). Every one of these was live in this corpus while the gate
# ---- reported it clean. They are frozen as fixtures because a pattern written from a pattern is
# ---- what certified them green; a pattern written from the measured population is what caught
# ---- them. A shape that stops matching reds HERE, not in a review six weeks later.
for _shape in \
  'A review spawns at most 5 agents TOTAL.' \
  'CONSOLIDATE before you fan out: at most 5 verify agents TOTAL (batch grows).' \
  'the ≤5 cap is enforced at the Workflow tool-call' \
  'the raw-primitive ban + the ≤5-verifier arity rule' \
  'Route ALL Workflow fan-out through cap-5 helpers.' \
  'CONCURRENCY ≤ 5, ALWAYS — the #1 rate-limit lever.' \
  ; do
  mk shape
  printf '# rules\n\n%s\n' "$_shape" > "$R/GUIDE.md"
  run
  ck "measured carrier shape is caught: $_shape" '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "GUIDE.md"'
done

# ---- The false positive that narrowing REMOVED, frozen so a future widening cannot bring it back.
# ---- `agents?-[0-9]+` matched the node-registry hostname `agent-0`; the reversed form is `cap-N` only.
mk hostname
printf '# nodes\n\n| `c` | agent-0 @ `DESKTOP-8BKM8GN` | `origin` |\n' > "$R/GUIDE.md"
run
ck "a node hostname like agent-0 is NOT a bound"    '[ "$rc" = 0 ]'

# ---- WAIVER KEYS ON TEXT, NOT PATH (M2). A row reading `docs/` waived an entire subtree, because
# ---- the row was matched against the whole `<path>:<line>:<text>` hit line by a registry whose own
# ---- contract says it never keys on a path.
mk pathwaiver
mkdir -p "$R/docs"
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/docs/A.md"
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/docs/B.md"
printf 'docs/\ta path fragment must not waive a subtree\n' > "$R/waivers.txt"
run
ck "a path-fragment row does NOT waive its subtree" '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "docs/A.md"'
ck "...and that path-only row reds as STALE"        'printf "%s" "$out" | grep -q "matches nothing"'

# ---- MEMORY_ROOT IS READ (M3). A relocated tree's records must still be excluded, or the gate
# ---- reds an adopter's entire committed history on the day they install it.
mk relocated
mkdir -p "$R/docs/mem/builds/tOne"
printf 'MEMORY_ROOT=docs/mem\n' > "$R/.memory-tree.conf"
printf '# past\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/docs/mem/builds/tOne/README.md"
run
ck "a relocated MEMORY_ROOT's records are excluded" '[ "$rc" = 0 ]'

# ---- A QUOTED value is the NORM, not an edge case: 26 of 27 keys in the shipped example conf are
# ---- quoted. Unstripped it built ^"docs/mem"/(...), which matches nothing -- so every committed
# ---- record was scanned as a live carrier and an adopter's whole history reds on install. The
# ---- unquoted fixture above is exactly why this went unseen.
mk quoted
mkdir -p "$R/docs/mem/builds/tOne"
printf 'MEMORY_ROOT="docs/mem"   # the tree\n' > "$R/.memory-tree.conf"
printf '# past\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/docs/mem/builds/tOne/README.md"
run
ck "a QUOTED, commented MEMORY_ROOT still excludes records" '[ "$rc" = 0 ]'

# ---- A metacharacter SHRINKS the population instead of widening it, and no vacuity arm can see a
# ---- partial exclusion -- `^docs|memory/...` made `^docs` swallow a whole subtree while the gate
# ---- printed `clean`. Refused rather than escaped.
mk metachar
mkdir -p "$R/docs"
printf 'MEMORY_ROOT=docs|memory\n' > "$R/.memory-tree.conf"
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/docs/A.md"
run
ck "a MEMORY_ROOT that is not a plain path is REFUSED" '[ "$rc" = 2 ] && printf "%s" "$out" | grep -q "not a plain relative path"'

# ---- ...and the default still holds when no conf declares one.
mk defaultroot
printf '# past\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/memory/builds/tOne/README.md"
run
ck "with no conf, memory/ is still the frozen root" '[ "$rc" = 0 ]'



FLOOR_ASSERTIONS=24
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
