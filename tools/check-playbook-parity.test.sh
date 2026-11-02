#!/usr/bin/env bash
# check-playbook-parity.test.sh — self-test for <prefix>/check-playbook-parity.sh.
#
#   bash <prefix>/check-playbook-parity.test.sh
#
# Exit 0 = every arm held · 1 = an arm failed · 2 = the harness could not set up.
#
# WHY EACH ARM IS A RED PROOF. The gate under test exists to catch coverage checks that pass by
# checking nothing, so a harness that only ever watched it pass would be the very defect it gates.
# The charter's `[gate]` practice: a gate is not landed until its failing case has been observed.
#
# HOW THE ARMS WORK. Every arm builds a scratch WORKTREE-SHAPED fixture — a real git repo with its
# own <prefix>/, charter and runbook — and runs the gate inside it. Nothing here mutates the real tree,
# which matters because the gate derives its kit set from govkit's registry and `git ls-files`
# (TOOL-aRepatriatedFork-54), so every fixture carries its own registry, and would otherwise see
# this repo's own population.
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-playbook-parity.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
PFX="${KIT_REL:+$KIT_REL/}"
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
GATE_SRC="$ROOT/${PFX}check-playbook-parity.sh"
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
_rkd_py=$(resolve_python) || { echo "check-playbook-parity.test: no usable python, so the sibling kits cannot be resolved"; exit 2; }
HOOKS_DIR=$(resolve_kit_dir "$_rkd_py" hooks agent-cap.js "$HERE") || exit 2
HOOKS="${HOOKS_DIR##*/}"
MT_KIT_DIR=$(resolve_kit_dir "$_rkd_py" memory-tree check-memory-hygiene.sh "$HERE") || exit 2
MT_KIT="${MT_KIT_DIR##*/}"
# TOOL-aRepatriatedFork-54: the gate reads its kit population from govkit's registry, so every
# fixture carries one and DECLARES the kits it plants; an undeclared directory is not a kit.
GK_DIR=$(resolve_kit_dir "$_rkd_py" govkit registry.toml "$HERE") || exit 2
GK="${GK_DIR##*/}"
PB_DIR=$(resolve_kit_dir "$_rkd_py" playbook render_playbook.py "$HERE") || exit 2
PB="${PB_DIR##*/}"
# FX is the prefix the NEXT fixture is built at: this suite's own by default, and empty for the
# root-install arms, which every install owes whatever prefix this suite itself sits at.
FX=$PFX
fails=0
TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' EXIT

say_ok()   { printf 'arm ok    %s\n' "$1"; }
say_fail() { fails=$((fails+1)); printf 'arm FAIL  %s — %s\n' "$1" "$2"; }

# fixture <dir> — a minimal but VALID tree the gate passes on, so each arm breaks exactly one thing.
fixture() {
  local d=$1
  mkdir -p "$d/${FX}${MT_KIT}" "$d/${FX}${HOOKS}" "$d/${FX}lib" "$d/${FX}${GK}" "$d/.claude"
  git -C "$d" init -q 2>/dev/null
  git -C "$d" config user.email t@t; git -C "$d" config user.name t
  cp "$GATE_SRC" "$d/${FX}check-playbook-parity.sh"
  : > "$d/${FX}${MT_KIT}/engine.sh"
  printf 'const CAP = 5\nconst MAX_VERIFIERS = 5\nconst MAX_LENSES = 5\n' > "$d/${FX}${HOOKS}/agent-cap.js"
  # The hook README states two of the bounds, the lens-array bound and the resolved-K ceiling, the
  # latter in the rule-2 sentence its row reads (TOOL-dGroundRules-21 S35, TOOL-dGroundRules-25 S34).
  printf 'an array LITERAL of <=5 elements\n- Any marker `K` it cannot resolve to an integer <=5, the hook MAX_VERIFIERS\n' \
    | sed 's/<=/≤/g' > "$d/${FX}${HOOKS}/README.md"
  # The registry declares the two kits this fixture plants. `lib` is declared and holds no tracked
  # file, so it is no kit; the registry's own directory is declared nowhere, so it is none either.
  printf '[[entry]]\nid = "memory-tree"\ndescriptor = "{prefix}/%s/kit.toml"\n\n[[entry]]\nid = "agent-cap"\ndescriptor = "{prefix}/%s/kit.toml"\n\n[[exempt]]\npath = "{prefix}/lib"\nwhy = "gov-internal"\n' \
    "$MT_KIT" "$HOOKS" > "$d/${FX}${GK}/registry.toml"
  printf '{ "hooks": { "PreToolUse": [ { "matcher": "Workflow|Agent" } ] } }\n' > "$d/.claude/settings.json"
  # The trio. hooks is waived; memory-tree is documented, and it is documented in the RUNBOOK.
  #
  # TWO haystack files since v3.0, and this fixture carried only one — every arm below exited 2 on
  # the gate's own two-file precondition, control included, so thirteen red proofs were proving
  # nothing but a missing file. The kit line sits in the runbook rather than the template ON PURPOSE:
  # written into the template, an empty WIRE-INTO-PROJECT.md would satisfy the precondition while no
  # arm depended on a byte of it, and a haystack half nothing reads is the green-by-absence shape
  # this gate exists to refuse. Here, emptying the runbook reds `memory-tree` as undocumented.
  #
  # Every declared pair's STATED side must appear here, or its anti-vacuity arm reds on the valid-
  # fixture control -- which is exactly what that arm is for. Three pairs were added when the
  # playbook moved under this gate's protection and out of check-agent-cap-restatement.sh's
  # population; the control failed, correctly, until the fixture carried their sentences.
  # v4.0 (TOOL-aDistilledCharter-3) retired four pairs; the verify-agent total is the playbook's one.
  printf '<!-- governance-template: v4.0 -->\ntemplate {{ALPHA}} {{MEMORY_ROOT}}\nat most 5 verify agents TOTAL (batch grows)\n' \
    > "$d/coding-governance-agents.template.md"
  # TOOL-aDistilledCharter-8: the renderer's TEMPLATE_MAJOR pairs with the template marker's major.
  mkdir -p "$d/${FX}${PB}"
  printf 'TEMPLATE_MAJOR = 4\n' > "$d/${FX}${PB}/render_playbook.py"
  # A root install has no root head to name a kit by, so its runbook names it the way gov's does,
  # through the `<prefix>/` token (VERIFYING repair: a bare `memory-tree/` documents nothing).
  # The bare `§2` is S4's NEAR-MISS: a section sign with no charter word, counted and never failed.
  printf 'runbook {{MEMORY_ROOT}}\nadopt '"${FX:-<prefix>/}${MT_KIT}/"' into the target repo\nthe runbook §2 lists the steps\n' > "$d/WIRE-INTO-PROJECT.md"
  printf '# waivers\nhooks   not adopter-facing as a kit.\n' > "$d/${FX}playbook-kit-waivers.txt"
  # The stamp-rule pair (TOOL-aHonedRuleset-5) is the one row whose two homes both sit OUTSIDE
  # <prefix>/: the manifest template states the expression and manifest-check.sh owns it. The control
  # redded on a missing owning source from the day that row landed, because this fixture built no
  # skills/ tree at all.
  mkdir -p "$d/skills/session-kickoff"
  printf -- '- Stamp rule: sha = `HEAD` on any branch; the datetime always advances.\n' > "$d/skills/session-kickoff/MANIFEST-TEMPLATE.md"
  printf 'STAMP_SHA_RULE="sha = HEAD on any branch"\n' > "$d/skills/session-kickoff/manifest-check.sh"
  git -C "$d" add -A >/dev/null 2>&1
  git -C "$d" commit -qm f >/dev/null 2>&1
}

# add_kit <prefix> <kit> — a tracked kit directory the fixture's registry DECLARES. A kit planted
# without its registry row is no kit to the gate, so an arm doing that would pass for the wrong reason.
add_kit() {
  mkdir -p "$1$2" && : > "$1$2/x.sh" &&
    printf '\n[[entry]]\nid = "%s"\ndescriptor = "{prefix}/%s/kit.toml"\n' "$2" "$2" >> "$1${GK}/registry.toml"
}
add_substring_kit() { add_kit "$1" ape && printf 'the shape of a landscape\n' >> coding-governance-agents.template.md; }

# arm <label> <expect: ok|red|refuse> <expected-substring-when-red> <mutator…>
# `refuse` is a red that must ALSO exit 2: the gate could not run, which is not a finding.
arm() {
  local label=$1 expect=$2 want=$3; shift 3
  local d="$TMP/$(printf '%s' "$label" | tr -c 'a-zA-Z0-9' '_')"
  fixture "$d"
  ( cd "$d" && "$@" >/dev/null 2>&1 )
  git -C "$d" add -A >/dev/null 2>&1
  local out rc
  out=$(cd "$d" && bash ${FX}check-playbook-parity.sh 2>&1); rc=$?
  if [ "$expect" = ok ]; then
    if [ "$rc" -eq 0 ]; then say_ok "$label"
    else say_fail "$label" "expected the gate to PASS, it exited $rc"; printf '%s\n' "$out" | sed 's/^/      /'; fi
    return
  fi
  if [ "$rc" -eq 0 ]; then
    say_fail "$label" "expected the gate to RED, it exited 0 — the mutation was not caught"
    printf '%s\n' "$out" | sed 's/^/      /'; return
  fi
  if [ "$expect" = refuse ] && [ "$rc" -ne 2 ]; then
    say_fail "$label" "expected the gate to REFUSE with exit 2, it exited $rc"
    printf '%s\n' "$out" | sed 's/^/      /'; return
  fi
  case "$out" in
    *"$want"*) say_ok "$label" ;;
    *) say_fail "$label" "reds, but not naming: $want"; printf '%s\n' "$out" | sed 's/^/      /' ;;
  esac
}

# --- the control. Without it, every red proof below could be redding for an unrelated reason. -----
arm "control · a valid fixture passes" ok "" true
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fails:-0}" = 0 ] && echo "PASS (${probe_n:-1} assertions)" || echo "FAIL (${probe_n:-1} assertions)"; [ "${fails:-0}" = 0 ] && exit 0; exit 1; fi

# --- the anchored matcher itself ---------------------------------------------------------------
# The gate's header calls a bare substring match "the vacuous-selector shape this gate exists to
# prevent, committed by the gate itself" — and nothing pinned it: loosening `named_in_playbook`
# to `grep -qF` left every other arm green. This fixture names a kit ONLY as a substring inside an
# unrelated word, so a loosened matcher certifies it documented and the arm goes red.
arm "S1 a kit named only as a substring is NOT documented" red \
  "a kit ships and the playbook never names it, with no waiver row to excuse it: ape" \
  add_substring_kit "$PFX"

# --- AC1 · a kit named nowhere and waived nowhere --------------------------------------------------
arm "AC1 an undocumented kit reds by name" red \
  "a kit ships and the playbook never names it, with no waiver row to excuse it: orphankit" \
  add_kit "$PFX" orphankit

# --- TOOL-aRepatriatedFork-54 · the population is the registry's, at this prefix and at the root --------
# Each root arm builds its fixture at the repository root whatever prefix this suite sits at. The
# first is the red-first control of the unit: the listing gate reds on it naming `.claude`.
REGISTRY_REFUSAL="cannot read the kit population from govkit's registry.toml"
arm "AC3 an unresolvable registry REFUSES rather than reading as an empty population" refuse \
  "$REGISTRY_REFUSAL" sh -c 'rm -f '"${PFX}${GK}/registry.toml"''
FX=""
arm "AC2 at a root install .claude/, skills/ and an undeclared dir are not kits" ok "" \
  sh -c 'mkdir -p stray && : > stray/x.sh'
arm "AC3 at a root install an unresolvable registry REFUSES" refuse \
  "$REGISTRY_REFUSAL" sh -c 'rm -f '"${GK}/registry.toml"''
arm "AC3 at a root install a declared kit the playbook never names reds by name" red \
  "a kit ships and the playbook never names it, with no waiver row to excuse it: orphankit" \
  add_kit "" orphankit
# TOOL-aDistilledCharter-7, G2: with no tool root to scan, S4 takes every derived kit directory.
arm "S4 at a root install a kit file citing a charter section reds" red \
  "a live file cites a charter section by number, and v4.0 has no numbered sections; cite the handle or the owning guide: ${MT_KIT}/engine.sh:" \
  sh -c 'printf "# see \302\2471 Landing\n" >> '"${MT_KIT}/engine.sh"''
FX=$PFX

# --- AC2 · the unit's central proof: a stated value drifting from the source that owns it ----------
arm "AC2 MAX_LENSES drifts from the hook README's stated bound" red \
  "a declared value pair disagrees with the source that owns it. Pair lens-array bound" \
  sh -c 'printf "const MAX_VERIFIERS = 5\nconst MAX_LENSES = 6\n" > '"${PFX}${HOOKS}/agent-cap.js"''
arm "AC4 the renderer's TEMPLATE_MAJOR drifts from the template marker" red \
  "a declared value pair disagrees with the source that owns it. Pair template major" \
  sh -c 'printf "TEMPLATE_MAJOR = 3\n" > '"${PFX}${PB}/render_playbook.py"''
arm "AC2 MAX_VERIFIERS drifts from the template's stated total" red \
  "a declared value pair disagrees with the source that owns it. Pair verify-agent total" \
  sh -c 'printf "const MAX_VERIFIERS = 6\n" > '"${PFX}${HOOKS}/agent-cap.js"''

# --- AC3 · a placeholder added and the catalogue counts not updated ---------------------------------

# --- AC4 · an extraction that matches nothing must never compare empty to empty ----------------------
arm "AC4 an unresolvable pair reds rather than passing" red \
  "an extraction matched NOTHING, so the pair was never compared" \
  sh -c 'sed -i "s/at most 5 verify agents TOTAL (batch grows)//" coding-governance-agents.template.md'

# --- S4 · a charter section cited by number (TOOL-aDistilledCharter-3) -------------------------------
S4_RED="a live file cites a charter section by number, and v4.0 has no numbered sections; cite the handle or the owning guide: "
arm "S4 a charter section cited by number reds by file" red "${S4_RED}WIRE-INTO-PROJECT.md:" \
  sh -c 'printf "see the charter'"'"'s §7 here\n" >> WIRE-INTO-PROJECT.md'
arm "S4 a named v3.5 subsection reds by file" red "${S4_RED}${PFX}${MT_KIT}/engine.sh:" \
  sh -c 'printf "# see §1 Landing\n" >> '"${PFX}${MT_KIT}/engine.sh"''
arm "S4 the spec template's own sections are not a hit" ok "" \
  sh -c 'printf "the spec template'"'"'s §8 readers\n" >> WIRE-INTO-PROJECT.md'
# TOOL-aDistilledCharter-7, G5: the forms the byte-mode predicate missed, one arm each, and the
# protocol template's own sections, which are real.
arm "S4 a curly-apostrophe citation reds" red "${S4_RED}WIRE-INTO-PROJECT.md:" \
  sh -c 'printf "see the charter\342\200\231s \302\2477\n" >> WIRE-INTO-PROJECT.md'
arm "S4 a non-breaking-space citation reds" red "${S4_RED}WIRE-INTO-PROJECT.md:" \
  sh -c 'printf "see the charter\302\240\302\2477\n" >> WIRE-INTO-PROJECT.md'
arm "S4 a trailing-form citation reds" red "${S4_RED}WIRE-INTO-PROJECT.md:" \
  sh -c 'printf "as \302\2477 of the charter says\n" >> WIRE-INTO-PROJECT.md'
arm "S4 the protocol template's own sections are not a hit" ok "" \
  sh -c 'printf "the protocol template'"'"'s \302\24713 exit\n" >> WIRE-INTO-PROJECT.md'
arm "S4 an untracked template refuses rather than grading nothing" red \
  "the section-citation surface is empty, lacks the tracked template or holds no kit file, so no citation could be found and this stage must not report clean" \
  sh -c 'printf "coding-governance-agents.template.md\n" > .gitignore && git rm -q --cached coding-governance-agents.template.md'
# AC3 — the clean fixture's run prints a NON-ZERO near-miss count: a stage that can measure nothing
# would print zero here, which is the reassuring silence this tree refuses.
s4d="$TMP/s4_near_miss"
fixture "$s4d"
s4out=$(cd "$s4d" && bash ${FX}check-playbook-parity.sh 2>&1)
case "$s4out" in
  *"S4 graded "*"; "[1-9]*" line(s) carry a section sign"*) say_ok "S4 a clean run prints a non-zero near-miss count" ;;
  *) say_fail "S4 a clean run prints a non-zero near-miss count" "got: $s4out" ;;
esac

# --- AC5 · the derivation broken to lose its sentinel -------------------------------------------------
arm "AC5 a derivation missing its sentinel reds" red \
  "the kit derivation lost its frozen sentinel member, so the derivation is broken rather than the tree being empty: expected to find " \
  sh -c 'git rm -q -r --cached '"${PFX}${MT_KIT}"' >/dev/null 2>&1; rm -rf '"${PFX}${MT_KIT}"''

# --- AC6 · both waiver-drain arms ----------------------------------------------------------------------
arm "AC6a a waiver for a kit that is gone reds as stale" red \
  "a waiver row names a kit that no longer exists, so the row excuses nothing and is stale" \
  sh -c 'printf "ghostkit  gone\n" >> '"${PFX}playbook-kit-waivers.txt"''
arm "AC6b a waiver for a kit the playbook DOES name reds" red \
  "a waiver row names a kit the playbook DOES document, so the row excuses nothing" \
  sh -c 'printf "memory-tree  redundant\n" >> '"${PFX}playbook-kit-waivers.txt"''

# --- AC9 · the registry absent: red and STOP, never create one -------------------------------------------
arm "AC9 an absent waiver registry reds and stops" red \
  "the kit waiver registry is absent and this gate never creates it: expected " \
  sh -c 'git rm -q --cached '"${PFX}playbook-kit-waivers.txt"' >/dev/null 2>&1; rm -f '"${PFX}playbook-kit-waivers.txt"''

# --- the two S2-stage integrity guards ----------------------------------------------------------
# Both mutate the fixture's OWN copy of the gate, which is what a red proof of THIS kind of guard
# looks like: the guard exists to notice that the stage did not run, so the fixture has to be a
# stage that did not run.
arm "S2 an uncreatable results file reds instead of reporting agreement" red \
  "the value-parity stage could not create its results file, so no pair was compared and this gate must not report agreement" \
  sh -c 'sed -i "s|^PPTMP=.*|PPTMP=/nonexistent-dir-for-the-arm/pp|" '"${PFX}check-playbook-parity.sh"''
arm "S2 a lost results file reds rather than reading as no-disagreement" red \
  "the value-parity stage produced no completion sentinel, so its results were lost rather than empty and no pair was actually compared" \
  sh -c "sed -i \"/^printf 'PAIRSTAGE-RAN/d\" ${PFX}check-playbook-parity.sh"

# --- the structural intersection check must not pass vacuously ---------------------------------------------

# --- the remaining five branches, armed rather than pinned as exceptions -------------------------
# check-arms refuses an unarmed branch that is not written into memory/project/unarmed-branches.txt,

# check 1 · the kit derivation returns an EMPTY set. Distinct from AC5, where the set is non-empty
# and merely lost its sentinel: here coverage would be vacuously true over nothing at all.
arm "S1 an empty kit derivation reds before reporting coverage" red \
  "the kit derivation returned an empty set, so coverage would pass by checking nothing" \
  sh -c 'git rm -q -r --cached '"${PFX%/}"' >/dev/null 2>&1; rm -rf '"${PFX}${MT_KIT}"' '"${PFX}${HOOKS}"' '"${PFX}lib"''

# check 8 · a stated count that cannot be extracted at all. Without this the arithmetic block would
# compare three empty strings and report ok — the same vacuity the pair loop guards against.

# check 13 · the catalogue NAMES a shared placeholder that is not the measured intersection. The
# structural half of S3: check 12 catches naming none, this catches naming the wrong one.

if [ "$fails" -ne 0 ]; then
  printf 'check-playbook-parity.test.sh FAILED — %d arm(s)\n' "$fails"
  exit 1
fi
printf 'PASS — check-playbook-parity.test.sh: every arm held\n'
