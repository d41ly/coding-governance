#!/usr/bin/env bash
# spec-audit-optin.test.sh — the review kit's spec-audit opt-in pack, spec-audit-optin.js, which holds
# rule 0 of the agent-cap hook whole since TOOL-dFairHearing-16. Every arm from the rule-0 section on
# came from <prefix>/hooks/agent-cap.test.sh with the rule, keeping its label, its payload and its
# verdict: the pack is a PreToolUse hook of its own, so it is judged exactly as the hook was, by its
# stdin and its exit code, and `HOOK` below names it. The arms after them are the pack's own: a copy
# with no hooks kit beside it, whose readers it cannot load.
#
#   bash <prefix>/workflows/spec-audit-optin.test.sh   (exit 0 = every arm held)
set -u
# A suite run from inside a session inherits the session's directory; no arm here wants it.
unset CLAUDE_PROJECT_DIR
HERE="$(cd "$(dirname "$0")" && pwd)"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0
# The one resolver, not the retired `command -v python3 || python` idiom this repo banned — which the
# ban could not see here, because it matches only `command -v`.
# TOOL-aRepatriatedFork-46: the resolver is carried INLINE. It was sourced from a probe of the
# library directory beside this kit, which ships nowhere, with a bare launcher as the fallback.
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
TESTPY=$(resolve_python) || { echo "spec-audit-optin.test: no usable python"; exit 2; }
# The pack the arms judge, as the hook was judged: a payload on stdin, from "$TMP", which no checkout holds.
HOOK="$HERE/spec-audit-optin.js"
check() { # name expected_exit json
  printf '%s' "$3" | (cd "$TMP" && node "$HOOK") >/dev/null 2>"$TMP/err"; local got=$?
  if [ "$got" = "$2" ]; then echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $got, want $2)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}
# NODE'S VIEW OF THE PATH, not the shell's: under MSYS `mktemp -d` hands back a POSIX spelling node
# cannot open. GOOD is the clean script the rule-0 arms carry, so each differs from its neighbour in
# args alone.
NODEDIR=$(cd "$TMP" && pwd -W 2>/dev/null || printf '%s' "$TMP")
printf 'const s = await agent("one")\n' > "$TMP/good.js"
GOOD="$NODEDIR/good.js"

# ---- rule 0: a spec audit is OPT-IN, declared in the build README's front matter ----------------
# TOOL-aBlindedTrial-4. The rule reads `tool_input.args` ONLY — never the script text, which both
# shipped harnesses fill with the word `spec-audit` — so every arm here carries the CLEAN script
# above and differs from its neighbour in args alone. Every deny arm asserts its own branch text,
# since every rule exits 2; `check_spec_audit` runs each payload TWICE, args as an OBJECT and as a JSON STRING,
# because the Workflow tool delivers both and the first cut of tier2-review's own guard refused one.
SAREPO="$TMP/sarepo"; mkdir -p "$SAREPO/memory/builds/tSA/reviews"
SAJ="$NODEDIR/sarepo"; SAREADME="$SAREPO/memory/builds/tSA/README.md"
check_spec_audit() { # name expected_exit needles(;;-joined, empty for an allow) args-json
  local name=$1 want=$2 needles=$3 args=$4 form payload got n miss
  for form in object string; do
    payload=$("$TESTPY" -c 'import json,sys
g,a,form=sys.argv[1:4]
args=json.loads(a)
print(json.dumps({"tool_name":"Workflow","tool_input":{"scriptPath":g,"args":args if form=="object" else json.dumps(args)}}))' "$GOOD" "$args" "$form")
    printf '%s' "$payload" | (cd "$TMP" && node "$HOOK") >/dev/null 2>"$TMP/err"; got=$?
    if [ "$got" != "$want" ]; then
      echo "FAIL $name [args as $form] (exit $got, want $want)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); continue
    fi
    miss=""
    if [ -n "$needles" ]; then
      # Split on `;;` alone — a needle may carry spaces ("not a date"), so no word-splitting here.
      # Fed from a scratch FILE, never a here-string holding a command substitution: the
      # shell-hygiene leg reds that shape because a failed substitution leaves the read at EOF.
      # WITH a trailing newline (TOOL-aBlindedTrial-7): `read` returns non-zero on the final
      # unterminated line, so `printf '%s'` left every arm's LAST needle unchecked and a
      # single-needle arm checking nothing - observed when a needle absent from the deny passed.
      printf '%s\n' "$needles" | sed 's/;;/\n/g' > "$TMP/needles"
      while IFS= read -r n; do
        [ -n "$n" ] && ! grep -qF -- "$n" "$TMP/err" && miss="$miss [$n]"
      done < "$TMP/needles"
    fi
    # A deny that spells a kit-install path strands every adopter that installed the kit elsewhere
    # — the shipped-surface ratchet holds this hook at its current count, and this arm holds the text.
    if [ "$want" = 2 ] && grep -q 'tools[/]' "$TMP/err"; then miss="$miss <a-kit-path-literal>"; fi
    if [ -z "$miss" ]; then echo "ok   $name [args as $form]"; pass=$((pass+1))
    else echo "FAIL $name [args as $form] (exit $got as wanted, but the message misses:$miss)"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
  done
}
# AC1 — the README exists and carries no key: denied, naming the decision, the key and the README.
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
check_spec_audit "rule0: spec-audit, README without the key → deny naming id + key + README" 2 \
  "TOOL-aBlindedTrial-6;;spec-audit:;;builds/tSA/README.md" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"}]}"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1, here since TOOL-dFairHearing-27 S4): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${pass:-1} assertions)" || echo "FAIL (${pass:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi
# S5 — the rule sits ABOVE the script read, so a `name:`-only invocation is judged too.
check "rule0: spec-audit by NAME only, README without the key → deny" 2 \
  "{\"tool_name\":\"Workflow\",\"tool_input\":{\"name\":\"tier2-review\",\"args\":{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}"
# AC4 — a diff review, and an absent kind, are not this rule's business; the same undeclared README.
check_spec_audit "rule0: kind diff-review on the same undeclared README → allow" 0 "" \
  "{\"kind\":\"diff-review\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
check_spec_audit "rule0: no kind at all → allow" 0 "" "{\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# CONTROL — script TEXT spelling the kind, args carrying none: the rule keys on args, never on text.
check "rule0: control, 'spec-audit' in the script text with no such args → allow" 0 \
  '{"tool_name":"Workflow","tool_input":{"script":"// kind: '"'"'spec-audit'"'"' — prose only\nconst s = await agent(\"one\")"}}'
# STATED LIMIT — an args string that does not parse shows the hook no kind; the harness throws on it.
check "rule0: unparseable args string → allow (stated limit: no kind is visible)" 0 \
  "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$GOOD\",\"args\":\"{kind: spec-audit, not json\"}}"
# AC2 — the key in the front matter, dated: allowed.
printf -- '---\nslug: tSA\nspec-audit: 2026-09-20\n---\n' > "$SAREADME"
check_spec_audit "rule0: spec-audit, README declares spec-audit: <date> → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC3 — a non-date value is a claim with no owner date behind it; a body-only key is not front matter.
printf -- '---\nslug: tSA\nspec-audit: yes\n---\n' > "$SAREADME"
check_spec_audit "rule0: spec-audit: yes → deny, not a date" 2 "not a date;;spec-audit: yes" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf -- '---\nslug: tSA\n---\n\n```\nspec-audit: 2026-09-20\n```\n' > "$SAREADME"
check_spec_audit "rule0: key only inside a fenced BODY block → deny (front matter only)" 2 "front matter" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC5 — an unplaceable call fails CLOSED, naming the field: a numeric repo, a reviewDir outside
# any builds/<slug>/ folder, and no reviewDir at all.
printf -- '---\nslug: tSA\nspec-audit: 2026-09-20\n---\n' > "$SAREADME"
check_spec_audit "rule0: repo is a number → deny naming repo" 2 '`repo`' \
  "{\"kind\":\"spec-audit\",\"repo\":7,\"reviewDir\":\"memory/builds/tSA/reviews\"}"
check_spec_audit "rule0: reviewDir outside builds/<slug>/ → deny naming reviewDir" 2 '`reviewDir`;;docs/reviews' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"docs/reviews\"}"
check_spec_audit "rule0: reviewDir absent → deny naming reviewDir" 2 '`reviewDir`' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\"}"
# AC6 — a README this hook cannot READ is a deny, never a stack trace at exit 1 (which admits).
mkdir -p "$SAREPO/memory/builds/tDir/reviews" "$SAREPO/memory/builds/tDir/README.md"
check_spec_audit "rule0: README path is a DIRECTORY → deny (exit 2, not a crash at 1)" 2 "could not be read;;spec-audit:" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tDir/reviews\"}"
check_spec_audit "rule0: README absent → deny naming the path tried" 2 "builds/tNone/README.md;;could not be read" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tNone/reviews\"}"
# F1 (closing review of units 2–5, round 1) — the guard and its callee must agree on WHAT a spec-audit
# call IS. `tier2-review.js` derives `kind` as `String(a.kind)`, so `["spec-audit"]` runs a full audit
# there; the hook's strict equality ADMITTED it. Both delivery forms, on the undeclared README.
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
check_spec_audit "rule0: kind [\"spec-audit\"] (an array) on the undeclared README → deny" 2 "TOOL-aBlindedTrial-6;;spec-audit:" \
  "{\"kind\":[\"spec-audit\"],\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# ...and the CLASS: one payload set fed to the hook AND to the callee's own `kind` line — the one line
# of tier2-review.js that decides `isSpec` — asserting the two agree. An edit to either side reds
# here until the other follows. The harness sits beside this kit in this repo; an adopter layout
# without it gets an ANNOUNCED skip, never a silent green.
T2R=""; _wf_dir=$(resolve_kit_dir "$TESTPY" workflows tier2-review.js "$HERE" 2>/dev/null) && T2R="$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)/$_wf_dir/tier2-review.js"
if [ -f "$T2R" ]; then
  kind_line=$(grep -m1 '^const kind = ' "$T2R")
  for k in '"spec-audit"' '["spec-audit"]' '"diff-review"' '"SPEC-AUDIT"' '{"k":"spec-audit"}' '7'; do
    callee=$(node -e "const a={kind:$k}; $kind_line; console.log(kind==='spec-audit'?2:0)" 2>/dev/null)
    printf '%s' "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$GOOD\",\"args\":{\"kind\":$k,\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}" \
      | (cd "$TMP" && node "$HOOK") >/dev/null 2>"$TMP/err"; got=$?
    if [ -n "$callee" ] && [ "$got" = "$callee" ]; then echo "ok   rule0: pair — hook and tier2-review agree on kind $k (exit $got)"; pass=$((pass+1))
    else echo "FAIL rule0: pair — hook exit $got, tier2-review isSpec says exit-equivalent '$callee' for kind $k"; fail=$((fail+1)); fi
  done
else
  echo "skip rule0: pair arm — tier2-review.js is not beside this kit (adopter layout); the class arm did NOT run"
fi
# F2 — the declaration is read from where the RECORD lands (`reviewDir`), so the SUBJECTS must sit
# under that same `builds/<slug>/`, else naming a declared build's reviews folder audits an
# undeclared build's specs. And a `reviewDir` that climbs through `..` is not placed by its own text.
printf -- '---\nslug: tSA\nspec-audit: 2026-09-20\n---\n' > "$SAREADME"
mkdir -p "$SAREPO/memory/builds/tOther/reviews"; printf -- '---\nslug: tOther\n---\n' > "$SAREPO/memory/builds/tOther/README.md"
check_spec_audit "rule0: declared reviewDir, one subject under ANOTHER build → deny naming subjects + the path" 2 '`subjects`;;builds/tOther/spec/s.md' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"},{\"path\":\"memory/builds/tOther/spec/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: declared reviewDir, every subject under the SAME build → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"},{\"path\":\"memory/builds/tSA/spec/t.md\",\"blob\":\"abc1235\"}]}"
check_spec_audit "rule0: declared reviewDir, a subject with NO builds/<slug> segment → deny naming subjects" 2 '`subjects`' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"docs/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: declared reviewDir, a subject re-routed through .. → deny naming subjects" 2 '`subjects`' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"memory/builds/tSA/../tOther/spec/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: reviewDir climbing through .. into a declared build → deny naming reviewDir" 2 '`reviewDir`;;..' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ/memory/builds/tOther\",\"reviewDir\":\"../../builds/tSA/reviews\"}"
# F5 — an MSYS-form `repo` (`/c/...`) is a spelling this node's corpus carries and the harness's own
# `git -C` accepts; `path.resolve` on win32 made it `C:\c\...` and denied a DECLARED build with ENOENT.
# Derived from $SAJ, so on a host where `pwd -W` is not a thing the arm feeds the unchanged POSIX path.
SAM=$(printf '%s' "$SAJ" | sed 's|^\([A-Za-z]\):/|/\L\1/|')
check_spec_audit "rule0: declared build, repo in MSYS /<drive>/ form → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAM\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# R1 (round 2) — containment must hold on the ROOT axis, not only the slug axis. A SECOND checkout
# beside the first, same slug, no declaration: an ABSOLUTE or `~`-rooted subject spelling it was
# admitted, because the walk found `builds/tSA` somewhere in the string and never asked whether the
# path sits under `repo`. A direct spec-audit subject is repo-relative by the harness's own contract,
# so every other spelling is denied by the same `subjects` sentence. The repo-relative allow above
# is the control.
SAREPO2="$TMP/sarepo2"; mkdir -p "$SAREPO2/memory/builds/tSA/spec"; printf -- '---\nslug: tSA\n---\n' > "$SAREPO2/memory/builds/tSA/README.md"
SAJ2="$NODEDIR/sarepo2"; SAM2=$(printf '%s' "$SAJ2" | sed 's|^\([A-Za-z]\):/|/\L\1/|')
check_spec_audit "rule0: declared reviewDir, an ABSOLUTE subject into a same-slug second checkout → deny naming subjects" 2 '`subjects`;;sarepo2/memory/builds/tSA/spec/s.md' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"$SAJ2/memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: ...the same subject in MSYS /<drive>/ form → deny naming subjects" 2 '`subjects`' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"$SAM2/memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"}]}"
check_spec_audit "rule0: declared reviewDir, a ~-rooted subject → deny naming subjects" 2 '`subjects`;;~/memory/builds/tSA/spec/s.md' \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\",\"subjects\":[{\"path\":\"~/memory/builds/tSA/spec/s.md\",\"blob\":\"abc1234\"}]}"
# R2 (round 2) — the F5 fold corrects a WIN32 rule and must run there alone: on POSIX `/w/repo` is a
# real root and the fold turned it into a cwd-relative `w:/repo` that ENOENTs. The hook exports
# nothing, so the fold line is read out of the source and run under an overridden platform — the F1
# pair arm's trick. A line that stops matching is a loud FAIL, never a silent pass.
fold_line=$(grep -m1 '^[[:space:]]*const repo = ' "$HOOK")
for plat_in_want in 'linux|/w/repo|/w/repo' 'win32|/w/repo|w:/repo' 'linux|C:/x/y|C:/x/y' 'win32|/tmp/x|/tmp/x'; do
  IFS='|' read -r plat rin rwant <<<"$plat_in_want"
  rgot=$(node -e "Object.defineProperty(process,'platform',{value:'$plat'}); const a={repo:'$rin'}; $fold_line; console.log(repo)" 2>/dev/null)
  if [ -n "$fold_line" ] && [ "$rgot" = "$rwant" ]; then echo "ok   rule0: fold — on $plat repo $rin folds to $rwant"; pass=$((pass+1))
  else echo "FAIL rule0: fold — on $plat repo $rin folded to '$rgot', want $rwant"; fail=$((fail+1)); fi
done
# ...and what the fold cannot reach ANNOUNCES itself: a repo under any other MSYS mount (`/tmp/…`)
# used to resolve to `C:\tmp\…` and deny as a README that does not exist, hiding the spelling that
# was tried. Win32 only — on POSIX `/tmp/x` is a real path and there is nothing to announce.
if [ "$(node -p process.platform)" = win32 ]; then
  case "$TMP" in /tmp/*) SAMOUNT="$TMP/sarepo" ;; *) SAMOUNT="/tmp/sarepo-msys-mount" ;; esac
  check_spec_audit "rule0: declared build, repo under an MSYS mount other than /<drive>/ → deny naming repo + MSYS" 2 '`repo`;;MSYS' \
    "{\"kind\":\"spec-audit\",\"repo\":\"$SAMOUNT\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
else
  echo "skip rule0: MSYS-mount deny arm — not win32 (the fold and its residual are win32-only); the arm did NOT run"
fi
# TOOL-aBlindedTrial-7 — a PROJECT-WIDE default. When the README carries NO key, the hook reads
# `SPEC_AUDIT_DEFAULT` from `<repo>/.unattended.conf` (the WORKTREE copy — this hook guards a session
# with an owner present; the driver reads BASE). Node cannot source shell, so the read is a deliberate
# re-parse, and the three spellings the two-readers gotcha names are each an arm: single quotes, a
# trailing comment, and a last-wins pair. The value is ARMED: a non-date DENIES by name rather than
# reading as absent. The README, present with any value, wins — a malformed key beside a dated
# default is still the not-a-date deny, never a silent fall-back.
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
SACONF="$SAREPO/.unattended.conf"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"\n' > "$SACONF"
check_spec_audit "rule0/U7: README without the key, conf SPEC_AUDIT_DEFAULT=\"<date>\" → allow by project default" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf "SPEC_AUDIT_DEFAULT='2026-09-21'\n" > "$SACONF"
check_spec_audit "rule0/U7: the single-quoted spelling → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21" # the day the owner ruled\n' > "$SACONF"
check_spec_audit "rule0/U7: a trailing comment after the value → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# closing review of units 7/8, R8 — a `#` GLUED to a bare word is part of the word to the shell, not a
# comment: `2026-09-21#c` is fail 54 in the driver, and rev-1's regex stopped the word at `#` and
# admitted the date. Observed RED-first on that hook. Its sibling, the `;`-joined line, reads as NO
# assignment here (the README deny, the safe direction) while the shell reads the date — a stated
# limit of this reader, pinned so it cannot drift into the permissive direction unnoticed.
printf 'SPEC_AUDIT_DEFAULT=2026-09-21#note\n' > "$SACONF"
check_spec_audit "rule0/U7: a glued #note on a bare value is part of the value → deny, not a date" 2 "SPEC_AUDIT_DEFAULT;;not a date" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"; X=1\n' > "$SACONF"
check_spec_audit "rule0/U7: a ;-joined second command reads as no assignment → the README deny (documented limit)" 2 "TOOL-aBlindedTrial-6;;spec-audit:;;builds/tSA/README.md" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="yes"\nSPEC_AUDIT_DEFAULT="2026-09-21"\n' > "$SACONF"
check_spec_audit "rule0/U7: two assignments, the LAST a date → allow (last wins, as the shell reads it)" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"\nSPEC_AUDIT_DEFAULT="yes"\n' > "$SACONF"
check_spec_audit "rule0/U7: two assignments, the LAST a non-date → deny naming the key" 2 "SPEC_AUDIT_DEFAULT;;not a date" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="yes"\n' > "$SACONF"
check_spec_audit "rule0/U7: conf SPEC_AUDIT_DEFAULT=\"yes\" → deny naming the key, not a date" 2 "SPEC_AUDIT_DEFAULT;;not a date" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT=""\n' > "$SACONF"
check_spec_audit "rule0/U7: conf SPEC_AUDIT_DEFAULT=\"\" (blank) → the README deny, unchanged" 2 "TOOL-aBlindedTrial-6;;spec-audit:;;builds/tSA/README.md" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# ...the deny's REMEDY names both routes, so an adopter learns the project-wide one from the refusal.
check_spec_audit "rule0/U7: the README deny names SPEC_AUDIT_DEFAULT as the other remedy" 2 "SPEC_AUDIT_DEFAULT" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"\n' > "$SACONF"
printf -- '---\nslug: tSA\nspec-audit: yes\n---\n' > "$SAREADME"
check_spec_audit "rule0/U7: README spec-audit: yes beside a dated default → deny, not a date (README wins)" 2 "not a date;;spec-audit: yes" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
check_spec_audit "rule0/U7: dated conf, README absent → still could-not-be-read (fail-closed unchanged)" 2 "builds/tNone/README.md;;could not be read" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tNone/reviews\"}"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
rm -f "$SACONF"
check_spec_audit "rule0/U7: conf removed, README without the key → deny (no conf is no default)" 2 "TOOL-aBlindedTrial-6;;spec-audit:" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"

# ---- TOOL-aWardedAudit-2 — the opt-in is the OWNER's. Each deny below was observed admitting
# ---- against the base hook first: it read the worktree key whoever wrote it.
SARUN="$SAREPO/memory/builds/tSA/RUN.md"
# AC3 — no run-state file, a prompt-mode README carrying a dated key → deny naming the mode.
printf -- '---\nslug: tSA\nauthorized-by: prompt\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
check_spec_audit "rule0/aWardedAudit: prompt README with a dated key → deny naming the mode" 2 "authorized-by: prompt;;admits nothing;;TOOL-aWardedAudit-4" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC1 — a live run that pinned no fact, beside a slug README carrying a dated key → deny naming RUN.md.
printf -- '---\nslug: tSA\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\n\nphase: BUILDING\nslug: tSA\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: live run with no spec-audit fact, worktree key → deny" 2 "builds/tSA/RUN.md;;live unattended run;;phase BUILDING" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC2 — the same live run pinning a dated fact, beside a README with NO key → allow.
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\n\nphase: BUILDING\nspec-audit: 2026-10-05\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: live run pinning a dated fact → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# ...and a non-date fact is no fact: deny.
printf '# run\n\n## Run facts\n\nphase: BUILDING\nspec-audit: yes\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: live run pinning a non-date fact → deny" 2 "live unattended run" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
# AC4 — a FINISHED run's file decides nothing: a LANDED record beside a slug README's dated key → allow.
printf -- '---\nslug: tSA\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\n\nphase: LANDED\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: LANDED run-state file, slug README key → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
rm -f "$SARUN"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"

# ---- TOOL-aWardedAudit-2 S4 — the BUILD HARNESS's `specAudit` is judged by the same predicate: its
# ---- nested audit is a runtime `workflow()` call no hook sees, so this is the one tool call there is.
# ---- The base hook admitted every one of these, because it judged `kind` alone.
SAH="{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\"}"
printf -- '---\nslug: tSA\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\n\nphase: BUILDING\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: harness specAudit, live run pinning no fact → deny" 2 "builds/tSA/RUN.md;;live unattended run" "$SAH"
printf '# run\n\n## Run facts\n\nphase: BUILDING\nspec-audit: 2026-10-05\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: harness specAudit equal to the pinned fact → allow" 0 "" "$SAH"
printf '# run\n\n## Run facts\n\nphase: BUILDING\nspec-audit: 2026-09-01\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit: harness specAudit differing from the pinned fact → deny" 2 "pins \`spec-audit: 2026-09-01\`;;the pinned date or nothing" "$SAH"
check_spec_audit "rule0/aWardedAudit: harness specAudit with an unplaceable slug → deny" 2 "is not one path segment" \
  "{\"repo\":\"$SAJ\",\"slug\":\"../x\",\"specAudit\":\"2026-10-05\"}"
check_spec_audit "rule0/aWardedAudit: harness call with no specAudit → not this rule's business" 0 "" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\"}"
rm -f "$SARUN"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"

# ---- TOOL-aWardedAudit-6 — the closing review's minors on rule 0. Each changed verdict was observed
# ---- against the base hook first.
SAOTH="$SAREPO/memory/builds/tOth"; mkdir -p "$SAOTH"
printf -- '---\nslug: tOth\nspec-audit: 2026-10-05\n---\n' > "$SAOTH/README.md"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"
printf '# run\n\n## Run facts\nphase: BUILDING\n' > "$SARUN"
# S1 / AC1 — a harness call for tSA is placed in tSA: another build's reviewDir or spec path → deny.
check_spec_audit "rule0/aWardedAudit-6: harness reviewDir under another build → deny" 2 "under another build;;memory/builds/tOth/reviews" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\",\"reviewDir\":\"memory/builds/tOth/reviews\"}"
check_spec_audit "rule0/aWardedAudit-6: harness units[].specPath under another build → deny" 2 "units[].specPath;;memory/builds/tOth/spec/a.md" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\",\"units\":[{\"id\":\"x\",\"specPath\":\"memory/builds/tOth/spec/a.md\"},{\"id\":\"y\"}]}"
# S5 / AC1 — an EMPTY reviewDir defaults as the harness does, so the live run's file decides.
check_spec_audit "rule0/aWardedAudit-6: harness reviewDir \"\" → placed in builds/tSA, the live run denies" 2 "builds/tSA/RUN.md;;live unattended run" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\",\"reviewDir\":\"\"}"
# S2 / AC2 — only `## Run facts` is read, and LANDING is no live run.
printf -- '---\nslug: tSA\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
printf '# run\nphase: BUILDING\n\n## Run facts\nphase: LANDING\n\n## Parked\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit-6: a stray phase above Run facts, LANDING inside → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf '# run\nspec-audit: 2026-10-05\n\n## Run facts\nphase: BUILDING\n\n## Parked\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit-6: a spec-audit line outside Run facts is no fact → deny" 2 "live unattended run" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
printf '# run\n\n## Run facts\nphase: ABORTED\n' > "$SARUN"
check_spec_audit "rule0/aWardedAudit-6: an ABORTED record decides nothing → allow on the slug key" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
rm -f "$SARUN"
# S3 / AC3 — a harness call with NO run-state file reads the README and the conf as an attended call.
check_spec_audit "rule0/aWardedAudit-6: harness call, no run-state file, slug README key → allow" 0 "" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\"}"
printf -- '---\nslug: tSA\nauthorized-by: prompt\nspec-audit: 2026-10-05\n---\n' > "$SAREADME"
check_spec_audit "rule0/aWardedAudit-6: harness call, no run-state file, prompt README key → deny" 2 "authorized-by: prompt;;admits nothing" \
  "{\"repo\":\"$SAJ\",\"slug\":\"tSA\",\"specAudit\":\"2026-10-05\"}"
# ...and the mode deny needs a KEY: a prompt README with none, beside a dated default → allow.
printf -- '---\nslug: tSA\nauthorized-by: prompt\n---\n' > "$SAREADME"
printf 'SPEC_AUDIT_DEFAULT="2026-09-21"\n' > "$SACONF"
check_spec_audit "rule0/aWardedAudit-6: prompt README with no key, dated worktree default → allow" 0 "" \
  "{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}"
rm -f "$SACONF"
rm -rf "$SAOTH"
printf -- '---\nslug: tSA\n---\n' > "$SAREADME"

# ---- the pack's own: a reader it cannot load (TOOL-dFairHearing-16 AC6) ----------------------------
# The pack reads agent-cap.js's `extractWorkflowArgs` and scratch-guard.js's `readFrontMatterKey`,
# probed in the hooks kit beside the review kit. A copy with no hooks kit beside it cannot place a call,
# so one whose args may be a spec audit is DENIED naming the reader it could not load, and any other
# call is admitted: a missing reader must not turn the one call the rule refuses into an admission.
# The kit directory names are DERIVED, so the copy types no kit name.
WFK=${HERE##*/}
Q="$TMP/q"; mkdir -p "$Q/$WFK"; cp "$HOOK" "$Q/$WFK/"
QPACK="$Q/$WFK/spec-audit-optin.js"
check_copy() { # name expected_exit needle(empty for an allow) json
  printf '%s' "$4" | (cd "$TMP" && node "$QPACK") >/dev/null 2>"$TMP/err"; local got=$?
  if [ "$got" = "$2" ] && { if [ -z "$3" ]; then [ ! -s "$TMP/err" ]; else grep -qF -- "$3" "$TMP/err"; fi; }; then
    echo "ok   $1 (exit $got)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $got, want $2${3:+, stderr carrying '$3'})"; sed 's/^/     /' "$TMP/err"; fail=$((fail+1)); fi
}
SAQ="{\"tool_name\":\"Workflow\",\"tool_input\":{\"name\":\"tier2-review\",\"args\":{\"kind\":\"spec-audit\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}"
check_copy "no hooks kit beside the pack: a spec-audit call is denied, naming agent-cap.js" 2 'agent-cap.js' "$SAQ"
check_copy "no hooks kit beside the pack: a harness call carrying specAudit is denied too" 2 'could not be loaded' \
  "{\"tool_name\":\"Workflow\",\"tool_input\":{\"scriptPath\":\"$GOOD\",\"args\":\"{\\\"repo\\\":\\\"$SAJ\\\",\\\"slug\\\":\\\"tSA\\\",\\\"specAudit\\\":\\\"2026-10-05\\\"}\"}}"
check_copy "no hooks kit beside the pack: a diff review is admitted" 0 "" \
  "{\"tool_name\":\"Workflow\",\"tool_input\":{\"name\":\"tier2-review\",\"args\":{\"kind\":\"diff-review\",\"repo\":\"$SAJ\",\"reviewDir\":\"memory/builds/tSA/reviews\"}}}"
# ...and with agent-cap.js beside it but no scratch-guard.js, the reader it names is the missing one.
HK_DIR=$(resolve_kit_dir "$TESTPY" hooks agent-cap.js "$HERE") || { echo "FAIL no hooks kit resolves beside this kit, so the last arm has no agent-cap.js to copy"; fail=$((fail+1)); }
mkdir -p "$Q/${HK_DIR##*/}"; cp "$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)/$HK_DIR/agent-cap.js" "$Q/${HK_DIR##*/}/"
check_copy "agent-cap.js beside the pack and no scratch-guard.js: denied, naming scratch-guard.js" 2 'scratch-guard.js' "$SAQ"

# ---- verdict -------------------------------------------------------------------------------------
# FLOOR_ASSERTIONS is the count every host runs: 53 rule-0 calls of check_spec_audit, two forms each,
# 3 check arms, 6 pair and 4 fold arms, and the 4 above; on win32 the MSYS-mount arm adds 2 more.
FLOOR_ASSERTIONS=123
echo "---- $pass passed, $fail failed ----"
if [ "$pass" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "FAIL executed $pass passing assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE or failing rather than absent"
  exit 1
fi
[ "$fail" = 0 ] && echo "PASS ($pass assertions)"
[ "$fail" = 0 ]
