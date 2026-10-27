#!/usr/bin/env bash
# adopt-memory-recall.sh — render the memory-recall Skill from `.memory-tree.conf` and converge.
#
#   <prefix>/memory-recall/adopt-memory-recall.sh --scaffold [--with-hook]
#   <prefix>/memory-recall/adopt-memory-recall.sh --check                  # gate leg: has the skill drifted?
#
# The Skill's `description` is the whole trigger mechanism and it names project values (the id
# families, the query-script path, the corpus root), so the skill is GENERATED from the conf rather
# than shipped. `--check` re-renders and diffs, which is how a `FAMILIES` edit that nobody
# re-rendered turns into a red leg instead of a silently stale trigger.
#
# The on-disk side of that diff is CR-NORMALISED, and the render side is LF by construction. A
# byte-comparing gate needs BOTH halves: the `eol=lf` pin so the committed bytes are right, AND
# normalisation in the comparison so a working copy that carries CRLF does not report every line of
# an untouched file as drift. Deleting the `tr` because the pin "already handles it" restores a red
# leg on a file nobody edited — that is what this normalisation was added for, not redundancy.
# The `[ -s ]` refusal above it belongs to the same seam: without it an empty render compared to an
# equally empty Skill is a PASS, which is the green-by-absence shape this kit refuses.
#
# `--with-hook` is the ONLY way the `recall-opened` PostToolUse hook is wired, and govkit lands the
# file only for a target that declared `[kit.memory-recall] with_hook = "yes"`. Skipping both is a
# supported end state: a hook file copied in but never merged into settings.json reads as UNWIRED
# forever, which is the fastest way to train every node to ignore the wiring verifier.
#
# The interpreter is resolved python3-first with a `python` fallback (the <prefix>/check-wiring.sh:69
# form), overridable with RECALL_PY. `--check` is a merge-bar leg, and a stock Debian/Ubuntu adopter
# without `python-is-python3` would red the whole gate suite on a working kit if this defaulted to
# bare `python`. The gate runner's argv rewrite cannot rescue it — this leg's argv[0] is `bash`.
set -u

# HERE BEFORE the cd: `$0` may be relative, and resolving it after moving to the root resolves it
# against the wrong directory (measured — it found `C:/Program Files/Git/recall_conf.py`).
HERE="$(cd "$(dirname "$0")" && pwd)" || exit 2
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
# Re-read it through `pwd`: git spells the root `C:/x` under MSYS while `pwd` spells it `/c/x`, and
# every path this script joins against ROOT should be in the shell's own spelling.
ROOT="$(pwd)"
# The kit dir as the adopting repo spells it, RELATIVE. git computes it, so the two operands
# cannot be two spellings of one directory: stripping a `pwd`-derived ROOT off a `pwd`-derived
# HERE still no-ops under an MSYS mount alias, and REL then comes out ABSOLUTE and machine-local
# — measured, the same tree at the same commit gave --check EXIT 0 from one spelling and a
# three-hunk DRIFTED diff from the other, and --scaffold writes that into a COMMITTED artifact
# silently. Works whether the kit sits at <root>/memory-recall/ or <root>/<prefix>/memory-recall/.
REL="$(unset GIT_DIR GIT_WORK_TREE; cd "$HERE" && git rev-parse --show-prefix)" || exit 2
REL="${REL%/}"
# THE TOOL ROOT, derived exactly as `adopt-unattended.sh` derives it and for the same reason: the
# settings merger lives BESIDE this kit rather than inside it, so the closing instruction below has
# to name the adopter's own prefix. A literal `tools/` there resolves to nothing in a root install
# and told the operator to copy the tool somewhere the next line would not look. TOOL-cMendedVintage-4.
TOOL_ROOT=${REL%/*}; [ "$TOOL_ROOT" = "$REL" ] && TOOL_ROOT=""   # "tools" at a prefix, "" at the root
[ -z "$TOOL_ROOT" ] || TOOL_ROOT="$TOOL_ROOT/"                   # trailing slash so a root install renders clean

# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to resolve-python.sh in gov's lib dir,
# and that dir's resolve-python.test.sh reds if any copy drifts.
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
# RECALL_PY is a PUBLISHED contract — the kit README, WIRE-INTO-PROJECT.md and this script's own
# usage line all name it — so it goes in as the caller override rather than being quietly
# replaced by GOV_PYTHON.
PY=$(resolve_python "${RECALL_PY:-}") || exit 2

mode=""; with_hook=0
for a in "$@"; do
  case "$a" in
    --scaffold|--check) mode="$a" ;;
    --with-hook) with_hook=1 ;;
    *) echo "usage: $0 --scaffold [--with-hook] | --check   (RECALL_PY overrides the launcher)"; exit 2 ;;
  esac
done
[ -n "$mode" ] || { echo "usage: $0 --scaffold [--with-hook] | --check"; exit 2; }

# The conf refusal lives in ONE place — recall_conf.py prints it, this script just forwards it.
conf="$("$PY" "$HERE/recall_conf.py")" || exit 1
# Belt-and-braces against a CR-bearing producer. recall_conf.py now pins LF on its KEY=VALUE
# protocol, but `read` would otherwise hand every value a trailing CR on Windows, and those CRs
# rendered straight into SKILL.md (`memory<CR>/`) and broke its YAML frontmatter. Stripping here
# keeps the consumer correct even against an older or third-party producer.
conf="${conf//$'\r'/}"
memory_root=""; families=""
while IFS='=' read -r k v; do
  case "$k" in MEMORY_ROOT) memory_root="$v" ;; FAMILIES) families="$v" ;; esac
done <<EOF
$conf
EOF

TEMPLATE="$HERE/SKILL.template.md"
SKILL_DIR="$ROOT/.claude/skills/memory-recall"
SKILL="$SKILL_DIR/SKILL.md"

# Three states, not two. The Skill surface is a separate artifact in this kit directory; when it is
# not installed there is nothing to render and nothing that can drift, so `--check` SKIPS rather
# than reds (a red an adopter cannot fix by editing their own repo trains them to ignore the leg).
# A rendered SKILL.md with no template is the one genuinely unverifiable state, and it reds.
if [ ! -f "$TEMPLATE" ]; then
  if [ -f "$SKILL" ]; then
    echo "memory-recall: $SKILL exists but $REL/SKILL.template.md does not — cannot verify drift"; exit 1
  fi
  echo "skip     memory-recall skill — $REL/SKILL.template.md not installed, nothing to render"
  [ "$mode" = "--check" ] && exit 0
  exit 1
fi

# `python3` LITERAL, not the resolved $PY: this render is a COMMITTED artifact shared across a
# fleet, so baking one node's answer reds --check on every node that resolves differently. Bare
# `python` is not an option either — a stock Debian/Ubuntu adopter without python-is-python3 has
# only python3, and every command in the kit's primary agent-facing surface would exit 127.
render() { # -> stdout
  # No `sed`: a substituted value carrying `|` closes the s||| delimiter and `&` re-inserts the
  # whole match. Parameter substitution has neither, PROVIDED the replacement is quoted — bash
  # 5.1 gave an unquoted one the same `&` meaning sed has.
  # The `X` sentinel is because `$( )` strips ALL trailing newlines. `cat` runs in its own
  # subshell with an explicit `exit 1` because the substitution reports the LAST command's
  # status, which is printf's and always 0 — the guard was unreachable without it.
  local out
  out=$( cat "$TEMPLATE" || exit 1; printf X ) || return 1
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{FAMILIES\}\}/"$families"}
  out=${out//\{\{MEMORY_ROOT\}\}/"$memory_root"}
  out=${out//\{\{QUERY_CLI\}\}/"python3 $REL/query.py"}   # gov:literal-python — a COMMITTED render shared across the fleet; see the note above
  printf '%s' "$out"
}

# An unsubstituted placeholder is a template that grew a value this script does not know how to
# fill — silently shipping `{{...}}` into a Skill description would break the trigger, so it reds.
leftover="$(render | grep -o '{{[A-Z_]*}}' | sort -u | tr '\n' ' ')"
if [ -n "$leftover" ]; then
  echo "memory-recall: unsubstituted placeholder(s) in SKILL.template.md: $leftover"; exit 1
fi

if [ "$mode" = "--check" ]; then
  [ -f "$SKILL" ] || { echo "memory-recall: $SKILL not rendered — run $REL/adopt-memory-recall.sh --scaffold"; exit 1; }
  TMP="$(mktemp)" || exit 2
  trap 'rm -f "$TMP"' EXIT
  render > "$TMP"
  [ -s "$TMP" ] || { echo "memory-recall: the render produced an EMPTY file — comparing it to an equally empty Skill is the green-by-absence shape this kit refuses"; exit 1; }
  if diff -q <(tr -d '\r' < "$SKILL") "$TMP" >/dev/null 2>&1; then
    echo "ok       memory-recall skill — SKILL.md matches the conf (FAMILIES: $families)"
    exit 0
  fi
  echo "memory-recall: .claude/skills/memory-recall/SKILL.md has DRIFTED from .memory-tree.conf."
  diff -u <(tr -d '\r' < "$SKILL") "$TMP" | head -40
  echo "Fix: $REL/adopt-memory-recall.sh --scaffold"
  exit 1
fi

mkdir -p "$SKILL_DIR"
render > "$SKILL.tmp" && mv "$SKILL.tmp" "$SKILL" || exit 1
echo "rendered $SKILL (FAMILIES: $families, corpus: $memory_root)"

if [ "$with_hook" = 1 ]; then
  if [ ! -f "$HERE/recall-opened.js" ]; then
    echo "memory-recall: --with-hook asked for, but $REL/recall-opened.js is not installed. govkit lands it"
    echo "  once .governance/deploy.toml declares [kit.memory-recall] with_hook = \"yes\" (then: govkit update --write)"; exit 1
  fi
  # NOTHING IS COPIED ANY MORE. The hook SHIPS at $REL/recall-opened.js and is wired there.
  #
  # This block used to `mkdir -p .claude/hooks` and copy into it, which RE-CREATED the exact
  # duplicate TOOL-dRetiredFork-14 withdrew: an adopter who took this opt-in got the second copy
  # back whatever the descriptor said, and a closing instruction naming it. That instruction is the
  # last thing they read at the moment they wire the hook, so a stale path here is worse than a
  # stale path in a descriptor -- one is followed by hand, the other is resolved by a tool.
  echo "$REL/recall-opened.js is installed — now merge it into settings.json:"
  # RESOLVED THROUGH THIS KIT'S OWN PREFIX, not hardcoded — this is the last instruction an adopter
  # sees at the moment they take the opt-in, and the step whose omission leaves the hook inert. The
  # probe, the copy destination and the fallback are one spelling, `$TOOL_ROOT`, so the directory the
  # operator is told to copy the merger INTO is the directory the next line then runs it from. A
  # hardcoded tools/ path printed here died with errno 2 in an adopter, because no runbook step
  # delivered the tool; at any prefix but gov's own it also named a directory that is not there.
  # The `<gov>/` source half names gov's OWN checkout, whose kit root no adopter tree can reveal, so it
# is spelled with the `<prefix>/` prose token rather than guessed (TOOL-aRepatriatedFork-23 §8 F2).
  smerge=""
  for c in "${TOOL_ROOT}settings-merge.py" settings-merge.py; do [ -f "$ROOT/$c" ] && { smerge="$c"; break; }; done
  if [ -z "$smerge" ]; then
    echo "  cp <gov>/<prefix>/settings-merge.py ${TOOL_ROOT:-./}     # <prefix>: where your gov checkout keeps its kits; not installed here yet (WIRE §3c step 4)"
    smerge="${TOOL_ROOT}settings-merge.py"
  fi
  echo "  $PY $smerge --fragment $REL/recall-opened.fragment.json"
fi

echo "Adopted. Next:"
echo "  1. Add both legs to your gate runner AND your CI config (see WIRE-INTO-PROJECT.md):"
echo "       $PY $REL/selftest.py"
echo "       bash $REL/adopt-memory-recall.sh --check"
echo "     Without this the skill-drift check silently never runs."
echo "  2. Re-run --scaffold after any FAMILIES/MEMORY_ROOT edit; --check reds until you do."
