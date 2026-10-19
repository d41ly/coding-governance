#!/usr/bin/env bash
# adopt-roles.sh — install the role catalogue's project-facing surface: the `/build` Skill, one
# agent type per agent role under `.claude/agents/`, and the role index `.claude/roles.json`.
#
#   <prefix>/roles/adopt-roles.sh --scaffold   # render all three, print each written path and the restart notice
#   <prefix>/roles/adopt-roles.sh --check      # render in memory and byte-compare all three with the files on disk
#
# Exit 0 = rendered / in sync · 1 = stale, absent, a surviving token, a stage disagreement or a
# refused agent render, each named · 2 = usage, a failed derivation, an absent conf or a dead
# catalogue probe · 3 = no governing doc at `CHARTER`: the Skill alone rendered or compared, and one
# line names the doc and the key.
#
# NO GOVERNING DOC IS A DECLARED OUTCOME, NOT A REFUSAL (TOOL-aOrientedCast-8 section 8 F3). A default
# install lands the playbook wherever its answers put it while the memory-tree seed writes
# `CHARTER="AGENTS.md"`, so a fresh adopter often has no file there. Every agent type appends the
# charter's cited rule lines and carried sections, so none can be rendered; the Skill needs no
# charter, so it still is, and the descriptor's
# `no-governing-doc` outcome accepts exit 3, so the apply succeeds and check-wiring names the doc.
#
# THE AGENT RENDER is `render_agents.py --write` or `--check` beside this file, run through the
# resolved python; its lines pass through, and under `--check` its own `--write` remedy line is
# replaced by this script's `--scaffold`, so one leg and one remedy grade all three artifacts
# (TOOL-aOrientedCast-8 S4).
#
# The shape is the unattended kit's adopter (KICK-aOrientedCast-2): the same `.git` walk derives the
# kit's repo-relative path and the tool root, every `{{TOKEN}}` is substituted literally, and both
# sides of the compare are CR-normalised. NO `fail()` HELPER, for that adopter's reason: check-arms
# grades a script defining one as a gate, and an adopter is not a gate.
#
# THE HARNESS CITATIONS (TOOL-dRenderedAnchor-2, TOOL-dRenderedAnchor-3). Before the plain
# `{{TOOL_ROOT}}` substitution, every `{{TOOL_ROOT}}<home>/<file>` citation of the template that
# `roles_lib.resolve_cited_paths` holds is replaced by the path it resolves, one whole citation at a
# time, so a held citation never rewrites a longer one it prefixes. Only a
# `workflow`-driver harness of the workflow table resolves through the role index's call, with the
# tool root as `here`, so `/build` names each harness where the role index lists it, a kit landed
# under its id behind a `rendered` receipt row included. Every other citation resolves from the kit
# directory, the call `derive_kit_paths` makes, so its probes stop at `<tool root>/<home>/`, and at a
# prefixed install an adopter's file at the repository root is never named. A citation neither call
# holds falls through to the plain substitution. In gov every citation is held at
# `<tool root>/<home>/`, so the render is unchanged.
# The answer reads the disk at render time: an `apply` that runs this before the harnesses are
# rendered writes the plain path, and `--check` then reads the Skill out of sync until `--scaffold`.
#
# THE STAGE BINDING. Each `## Stage <n> — <workflow>` heading of the template must name a
# `[[workflow]]` of the catalogue whose `stage` is <n>, the headings run in strictly ascending stage
# order, and every workflow of stage 1 or more is named by exactly one heading. It runs inside
# `render_skill`, so `--check` grades exactly what `--scaffold` would write.
#
# WHAT THIS DOES NOT CHECK: what a stage's body says, whether the commands it names exist, or any
# catalogue key but `name` and `stage`. The catalogue is read with awk over `[[workflow]]` blocks, so
# an inline-table reformat reads zero workflows and refuses as a dead probe rather than passing.
set -u
MODE="${1-}"
case "$MODE" in
  --scaffold|--check) ;;
  *) echo "usage: $0 --scaffold | --check"; exit 2 ;;
esac

KIT_DIR=.; [[ $0 == */* ]] && KIT_DIR=${0%/*}; KIT_DIR="$(cd "$KIT_DIR" && pwd)"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "roles: not a git repo"; exit 2; }

# A LOGICAL upward walk from the kit dir to the first `.git` (a file in a linked worktree, hence -e),
# building the kit's repo-relative path from basenames. adopt-unattended.sh says why no path string is
# compared and why the walk is not physical.
KIT_REL=""; _p="$KIT_DIR"
while : ; do
  _parent=${_p%/*}; _parent=${_parent:-/}
  [ "$_parent" = "$_p" ] && { KIT_REL=""; break; }
  KIT_REL="${_p##*/}${KIT_REL:+/$KIT_REL}"
  [ -e "$_parent/.git" ] && break
  _p="$_parent"
done
[ -n "$KIT_REL" ] || { echo "roles: KIT_DIR derived empty — no .git above the kit at $KIT_DIR"; exit 2; }
TOOL_ROOT=${KIT_REL%/*}; [ "$TOOL_ROOT" = "$KIT_REL" ] && TOOL_ROOT=""
[ -z "$TOOL_ROOT" ] || TOOL_ROOT="$TOOL_ROOT/"

cd "$ROOT" || exit 2
CONF=".memory-tree.conf"
[ -f "$CONF" ] || { echo "roles: no $CONF at the repo root, so MEMORY_ROOT cannot be read"; exit 2; }

# The resolver, INLINE: this kit is copy-installed as a standalone directory, so the shared lib does
# not exist in an adopting repo. Byte-identical to the canonical copy its marker line names.
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
PY=$(resolve_python) || exit 2

# MEMORY_ROOT and CHARTER are read with the library's ONE conf grammar — `export`, quotes and a
# trailing `# comment` included — never a second parser here (TOOL-aOrientedCast-15 S6: a bare `sed`
# exited 2 on the `export` form and rendered a trailing comment into the Skill).
MEMORY_ROOT=$("$PY" -B -c 'import pathlib, sys
sys.path.insert(0, sys.argv[1])
import roles_lib
print(roles_lib.read_conf_key(pathlib.Path(sys.argv[2]), "MEMORY_ROOT") or "")' "$KIT_DIR" "$CONF") \
  || { echo "roles: MEMORY_ROOT could not be read from $CONF"; exit 2; }
MEMORY_ROOT=${MEMORY_ROOT%$'\r'}
[ -n "$MEMORY_ROOT" ] || { echo "roles: MEMORY_ROOT is blank or absent in $CONF"; exit 2; }

TEMPLATE="$KIT_DIR/SKILL.template.md"
CATALOGUE="$KIT_DIR/workflows.toml"
OUT=".claude/skills/build/SKILL.md"

render_skill() { # -> the render on stdout; 1 a stage disagreement or a surviving token, 2 a dead probe
  [ -f "$TEMPLATE" ] && [ -f "$CATALOGUE" ] || { echo "roles: $KIT_REL lacks SKILL.template.md or workflows.toml" >&2; return 2; }
  local bind rc out left
  bind=$(awk -v cat="$KIT_REL/workflows.toml" -v tpl="$KIT_REL/SKILL.template.md" '
    function close_blk() {
      if (blk) {
        if (name == "" || stage == "") { print "roles: catalogue block at " cat ":" blk " carries no " (name == "" ? "name" : "stage") " line"; bad = 1 }
        else { n++; st[name] = stage }
      }
      blk = 0; name = ""; stage = ""
    }
    function switch_file() { switched = 1; close_blk(); if (n == 0) { print "roles: dead probe — " cat " parsed zero [[workflow]] blocks"; dead = 1; exit 2 } }
    { sub(/\r$/, "") }
    FILENAME == ARGV[1] {
      if ($0 ~ /^\[\[workflow\]\][ \t]*$/) { close_blk(); blk = FNR; next }
      if (blk && $0 ~ /^name = "/) { v = $0; sub(/^name = "/, "", v); sub(/".*/, "", v); name = v }
      if (blk && $0 ~ /^stage = [0-9]+/) { v = $0; sub(/^stage = /, "", v); sub(/[^0-9].*/, "", v); stage = v + 0 }
      next
    }
    !switched { switch_file() }
    /^## Stage / {
      h = "heading \"" $0 "\" at " tpl ":" FNR
      if (NF != 5 || $4 != "—" || $3 !~ /^[0-9]+$/) { print "roles: " h " is not of the form ## Stage <n> — <workflow>"; bad = 1; next }
      num = $3 + 0; wf = $5
      if (!(wf in st)) { print "roles: " h " names no [[workflow]] entry of " cat; bad = 1; next }
      if (st[wf] != num) { print "roles: " h " says stage " num " but the entry " wf " is stage " st[wf]; bad = 1 }
      if (seen[wf]++) { print "roles: " h " names the entry " wf " a second time"; bad = 1 }
      if (num <= last) { print "roles: " h " does not ascend past stage " last; bad = 1 }
      last = num
    }
    END {
      if (dead) exit 2
      if (!switched) switch_file()
      if (dead) exit 2
      for (w in st) if (st[w] >= 1 && !(w in seen)) { print "roles: the entry " w " (stage " st[w] ") of " cat " is named by no ## Stage heading"; bad = 1 }
      exit bad
    }' "$CATALOGUE" "$TEMPLATE"); rc=$?
  [ "$rc" -eq 0 ] || { printf '%s\n' "$bind" >&2; return "$rc"; }
  # The `X` sentinel keeps trailing newlines `$( )` would strip. The replacements are QUOTED, because
  # bash 5.1+ reads an unquoted `&` in one as the matched text.
  # THE CITATION PASS (TOOL-dRenderedAnchor-2, TOOL-dRenderedAnchor-3): the template's text, with each
  # `{{TOOL_ROOT}}` citation `resolve_cited_paths` holds replaced through `TOOL_ROOT_CITE_RE.sub`, one
  # whole match at a time: the pattern's `[\w.-]+` is greedy, so a longer citation is its own match and
  # never takes a shorter one's path. The path is relative to the first directory above the kit
  # holding `.git`, the walk that derived TOOL_ROOT. The bytes go out through `sys.stdout.buffer`, so
  # a Windows python writes no CRLF. The plain substitution then answers every citation not held.
  out=$("$PY" -B -c 'import pathlib, sys
sys.path.insert(0, sys.argv[1])
import roles_lib
kit = pathlib.Path(sys.argv[1]).absolute()
root = next((d for d in (kit, *kit.parents) if (d / ".git").exists()), kit)
text = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8")
held = dict(roles_lib.resolve_cited_paths(text, kit, root, roles_lib.load_workflows(kit)))
sys.stdout.buffer.write(roles_lib.TOOL_ROOT_CITE_RE.sub(
    lambda m: held.get(m.group(0), m.group(0)), text).encode("utf-8"))' "$KIT_DIR" "$TEMPLATE" && printf X) \
    || { echo "roles: the citation pass over $KIT_REL/SKILL.template.md failed" >&2; return 2; }
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{KIT_DIR\}\}/"$KIT_REL"}
  out=${out//\{\{TOOL_ROOT\}\}/"$TOOL_ROOT"}
  out=${out//\{\{MEMORY_ROOT\}\}/"$MEMORY_ROOT"}
  if left=$(printf '%s' "$out" | grep -nF '{{'); then
    echo "roles: a token survived the render of $KIT_REL/SKILL.template.md:" >&2
    printf '    line %s\n' "${left//$'\n'/$'\n'    line }" >&2
    return 1
  fi
  printf '%s' "$out"
}

body=$(render_skill && printf X) || exit $?
body=${body%X}

AGENTS="$KIT_DIR/render_agents.py"
[ -f "$AGENTS" ] || { echo "roles: $KIT_REL lacks render_agents.py, so no agent type can be rendered"; exit 2; }

# THE GOVERNING DOC, read with the library's own conf grammar so this decides exactly where the agent
# render would refuse with R0. A python that cannot read it is exit 2, never a silent "no doc".
CHARTER=$("$PY" -B -c 'import pathlib, sys
sys.path.insert(0, sys.argv[1])
import roles_lib
print(roles_lib.read_conf_key(pathlib.Path(sys.argv[2]), "CHARTER") or "")' "$KIT_DIR" "$CONF") \
  || { echo "roles: CHARTER could not be read from $CONF"; exit 2; }
CHARTER=${CHARTER%$'\r'}
nodoc=""
if [ -z "$CHARTER" ]; then
  nodoc="roles: no governing doc — CHARTER in $CONF is blank or absent, so the agent types and the role index are not rendered. Fix: write the doc, point CHARTER at it, then run bash $KIT_REL/adopt-roles.sh --scaffold"
elif [ ! -f "$CHARTER" ]; then
  nodoc="roles: no governing doc — CHARTER in $CONF names $CHARTER, which is not a file, so the agent types and the role index are not rendered. Fix: write that doc or point CHARTER at it, then run bash $KIT_REL/adopt-roles.sh --scaffold"
fi

if [ "$MODE" = "--check" ]; then
  stale=0
  if [ ! -f "$OUT" ]; then
    echo "roles: $OUT is not rendered"; stale=1
  else
    disk=$(tr -d '\r' < "$OUT" && printf X); disk=${disk%X}
    [ "$disk" = "$body" ] || { echo "roles: $OUT is out of sync with $KIT_REL/SKILL.template.md"; stale=1; }
  fi
  if [ -n "$nodoc" ]; then
    echo "$nodoc"
  else
    # The renderer's own remedy names `--write`, which renders the agent types alone; this script's
    # `--scaffold` is the one remedy for all three artifacts, so that line is replaced below.
    agents_out=$("$PY" -B "$AGENTS" --check 2>&1); arc=$?
    printf '%s\n' "$agents_out" | grep -v '^render_agents: remedy — '
    [ "$arc" -eq 0 ] || stale=1
  fi
  [ "$stale" -eq 0 ] || { echo "roles: remedy — bash $KIT_REL/adopt-roles.sh --scaffold"; exit 1; }
  [ -z "$nodoc" ] || exit 3
  exit 0
fi

# The agent render FIRST: it renders everything in memory before it writes, so a refusal writes
# nothing, and the Skill is then not written beside an unrendered catalogue either.
if [ -z "$nodoc" ]; then
  "$PY" -B "$AGENTS" --write || { echo "roles: the agent render refused, so nothing more was written — fix what it named and re-run $0 --scaffold"; exit 1; }
fi

new=""; [ -f "$OUT" ] || new=1
mkdir -p "${OUT%/*}" || exit 2
printf '%s' "$body" > "$OUT" || exit 2
echo "$OUT"
# Whether a running session lists a Skill written after it started is UNVERIFIED on this CLI; the
# line states the conservative rule.
[ -z "$new" ] || echo "roles: a session started before this write may not list /build until it restarts"
[ -z "$nodoc" ] || { echo "$nodoc"; exit 3; }
exit 0
