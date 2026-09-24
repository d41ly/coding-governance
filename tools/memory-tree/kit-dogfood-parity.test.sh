#!/usr/bin/env bash
# kit-dogfood-parity.test.sh — the two documents this kit SHIPS, RENDERED for this install, must
# equal the two documents this repo RUNS ON. Exit 0 = in parity · 1 = drift · 2 = misconfigured.
#
#   bash tools/memory-tree/kit-dogfood-parity.test.sh            # assert parity
#   bash tools/memory-tree/kit-dogfood-parity.test.sh --render   # rewrite the live copies from the templates
#
# WHY THIS EXISTS. `HYGIENE.template.md` and `SPEC-TEMPLATE.template.md` are what an adopting repo
# installs; `<MEMORY_ROOT>/HYGIENE.md` and `<MEMORY_ROOT>/TEMPLATE-SPEC.md` are this repo's own
# installed copies, and they are what a session reads while working here. Nothing connected them, so
# they drifted: measured 2026-08-08, the shipped spec template still described a NINE-section canon
# and carried no SPEC10_CUTOFF section, while the live copy — and the gate — had required TEN
# sections since 2026-08-04. An adopter would have installed a template the gate rejects. This is the
# kit-versus-dogfood divergence class, and prose alone never catches it.
#
# THE COMPARISON IS A RENDER, NOT A STRIP. The templates carry `{{KIT_DIR}}` (this kit's repo-relative
# directory) and `{{TOOL_ROOT}}` (the install prefix with a trailing slash, empty at a root install),
# and `adopt-memory-tree.sh` substitutes both when it scaffolds. This gate performs the SAME
# substitution and diffs the result, so what it grades is exactly what an adopter receives.
#
# It used to strip a literal `tools/` from the live copy with an unanchored global `sed`, which was
# wrong twice over: it also stripped every `tools/` that was not a kit path (a future `src/tools/x`
# would have been silently mangled and reported as parity), and it left the SHIPPED templates
# spelling a root install — so a kit installed under a prefix scaffolded an adopter's own committed
# rule set with kit paths that resolve to nothing in their tree. Hygiene check 15, which exists to
# catch dead repo-path citations, could not see them: it only classifies a citation as a repo path
# when its FIRST segment is a tracked top-level directory, and at a prefixed install `memory-tree/`
# is not one. The render closes both.
#
# DIRECTION. `--render` writes TEMPLATE -> LIVE. The template is the authored source; the live copy
# is this repo's dogfood render of it, exactly as `.claude/skills/*/SKILL.md` relates to its own
# template. Edit the template, then re-render — never hand-edit the live copy.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "kit-parity: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
MEMORY_ROOT=memory
# TOOL-aJoinedCanon-9: PRESET above the conf source, and it is `set -u` safety rather than a
# default — there is exactly ONE literal row set and it is the conf. Without this line every adopter
# tree whose .memory-tree.conf predates the key ABORTS on an unbound variable inside render_doc,
# which is a reader that fails to RUN rather than one that fails.
READINESS_ROWS="${READINESS_ROWS:-}"
[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
M="$MEMORY_ROOT"
HERE="$(cd "$(dirname "$0")" && pwd)"
# The install prefix is derived from where THIS script lives, not hardcoded — an adopter who installs
# the kit somewhere else gets the right render without editing the test.
# BOTH sides go through the same `cd … && pwd` chain first. Under MSYS/git-bash one directory has two
# spellings (a drive-letter one from `git rev-parse`, a mount-point one from `pwd`), and a raw prefix
# strip across those flavors silently yields an ABSOLUTE path — which then substitutes nothing,
# reports the whole tree as drift, and prints a "fix" command containing a drive letter.
ROOT_N="$(cd "$ROOT" && pwd)"
KITREL=${HERE#"$ROOT_N"/}               # e.g. tools/memory-tree
[ "$KITREL" = "$HERE" ] && { echo "kit-parity: cannot locate this kit inside the repo ($HERE vs $ROOT_N)"; exit 2; }
TOOLROOT=${KITREL%/*}; [ "$TOOLROOT" = "$KITREL" ] && TOOLROOT=""
# The receipt answers through `derive_kit_paths` below, per row, exactly as `adopt-memory-tree.sh`
# asks it; this parent derivation is only the fallback for what no row and no probe resolves.
# TOOL-aRepatriatedFork-10 S6 and closing review round 1 L4.
[ -z "$TOOLROOT" ] || TOOLROOT="$TOOLROOT/"

MODE="${1:---check}"
PAIRS="$M/HYGIENE.md:$KITREL/HYGIENE.template.md $M/TEMPLATE-SPEC.md:$KITREL/SPEC-TEMPLATE.template.md $M/guides/BUILD-METHOD.md:$KITREL/BUILD-METHOD.template.md $M/guides/ANNOTATION-STYLE.md:$KITREL/ANNOTATION-STYLE.template.md"

# NOT "byte-identical IN INTENT" any more, which is what the previous version of this comment
# claimed while the two spellings sat in two files with two variable names and nothing comparing
# them. The block below is now a marked INLINE COPY of `tools/lib/render-doc.sh`, gated byte for
# byte by the parity table in `tools/lib/resolve-python.test.sh` — the same mechanism `resolve_python`
# already runs, one more row. DEPL-dCarriedReceipt-15 S6.
#
# The block reads `KIT_REL` and `TOOL_ROOT`, which is the canonical spelling; this file derives the
# same two values under its own names, so they are bound here rather than in the block.
KIT_REL="$KITREL"
TOOL_ROOT="$TOOLROOT"

# The render resolves every sibling path the templates cite for THIS install, so the dogfood copy
# is graded against what `adopt-memory-tree.sh --render` would write here. Both blocks below are
# marked inline copies, gated byte for byte by the same parity table as `render_doc`.
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
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

# >>> derive_kit_paths — canonical copy: render-doc.sh in gov's lib dir (byte-identical; gated)
# `derive_kit_paths <python> <kit dir> <template>...` prints the KIT_PATHS `render_doc` applies: one
# `{{TOOL_ROOT}}<home>/<file><TAB><path>` line per such citation in the templates that this install
# RESOLVES through `resolve_kit_dir`, receipt row first, so a per-entry `prefix` or `kit` override
# is honoured where govkit records it, per row. Then one bare `{{TOOL_ROOT}}<TAB><prefix>/` line when
# the receipt carries a top-level `prefix`, read as JSON and never grepped, because a FLAT install's
# kit directory has an empty parent (TOOL-aRepatriatedFork-10 S6). A citation nothing resolves gets
# no line and falls through to that prefix, or to the caller's parent-derived `TOOL_ROOT`.
derive_kit_paths() {
  "$1" -c "$(cat <<'RKD'
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).resolve()
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).resolve()
        if hit.is_file() and root in hit.parents:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
)"'
import json
import pathlib
import re
import sys
kit = pathlib.Path(sys.argv[1]).resolve()
root = next((p for p in (kit, *kit.parents) if (p / ".git").exists()), kit)
cites = []
for t in sys.argv[2:]:
    try:
        text = pathlib.Path(t).read_text(encoding="utf-8")
    except OSError:
        continue
    for m in re.finditer(r"\{\{TOOL_ROOT\}\}([\w.-]+)/([\w.-]+)", text):
        if m.group(0) not in cites:
            cites.append(m.group(0))
for cite in cites:
    home, anchor = cite[len("{{TOOL_ROOT}}"):].split("/")
    try:
        path = (resolve_kit_dir(home, anchor, kit) / anchor).relative_to(root)
    except (LookupError, ValueError):
        continue
    print("%s\t%s" % (cite, path.as_posix()))
try:
    pfx = json.loads((root / ".governance" / "install.json").read_text(encoding="utf-8")).get("prefix")
except (OSError, ValueError, AttributeError):
    pfx = None
pfx = str(pfx or "").strip("/")
if pfx and pfx != ".":
    print("{{TOOL_ROOT}}\t%s/" % pfx)' "$2" "${@:3}"
}
# <<< derive_kit_paths
KIT_PATHS=$(derive_kit_paths "$PY" "$KITREL" "$KITREL"/*.template.md) || { echo "kit-parity: could not resolve the sibling paths the templates cite"; exit 2; }

# >>> render_doc — canonical copy: tools/lib/render-doc.sh (byte-identical; gated)
render_doc() {
  # No `sed`: a substituted value carrying `|` closes the s||| delimiter and `&` re-inserts the
  # whole match. Parameter substitution has neither, PROVIDED the replacement is quoted — bash
  # 5.1 gave an unquoted one the same `&` meaning sed has.
  # The `X` sentinel is because `$( )` strips ALL trailing newlines. `cat` runs in its own
  # subshell with an explicit `exit 1` because the substitution reports the LAST command's
  # status, which is printf's and always 0 — the guard was unreachable without it.
  local out
  out=$( cat "$1" || exit 1; printf X ) || return 1
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{KIT_DIR\}\}/"$KIT_REL"}
  # Closing review round 1 L4: the paths `derive_kit_paths` RESOLVED for this install go first, one
  # `<placeholder><TAB><path>` line each, so a sibling the receipt re-homes renders where its row
  # puts it; the parent-derived `TOOL_ROOT` then answers only what no line did. CRs go first: a
  # Windows python prints CRLF, and a CR kept in a path lands in the rendered doc.
  local kp kv kpaths=${KIT_PATHS:-}
  while IFS=$'\t' read -r kp kv; do
    [ -z "$kp" ] || out=${out//"$kp"/"$kv"}
  done <<<"${kpaths//$'\r'/}"
  out=${out//\{\{TOOL_ROOT\}\}/"$TOOL_ROOT"}
  # TOOL-aJoinedCanon-9: the §5 row set is DECLARED, not written into the skeleton. The transform
  # sits INSIDE the marked block rather than in the callers, so the parity table already gating this
  # block covers it too — a per-caller transform would be a second duplication nothing compares,
  # because gov's live copy is written by the parity test and an adopter's by the adopter, so the
  # two formatters never meet.
  local rows=${READINESS_ROWS//|/$'
'- }
  out=${out//\{\{READINESS_ROWS\}\}/"- $rows"}
  # TOOL-aRepatriatedFork-10 S5: two conf FACTS, rendered from the conf this tree declares, so an
  # adopter's rule set states its own values rather than the shipping repo's. An undeclared key names
  # the owner of its default instead of retyping a number that lives in the engine's preset block.
  out=${out//\{\{INDEX_CAP_LINES\}\}/"${INDEX_CAP_LINES:-undeclared — the engine default applies}"}
  out=${out//\{\{ENTRY_CAP_UNIT\}\}/"${ENTRY_CAP_UNIT:-undeclared — the engine default applies}"}
  printf '%s' "$out"
}
# <<< render_doc

render() { render_doc "$@"; }

st=0
for pair in $PAIRS; do
  live=${pair%%:*}; ship=${pair##*:}
  # S3 (TOOL-dScrubbedConduit-1): --render must be able to CREATE a first render.
  # This `continue` fired in EVERY mode, including the one whose whole job is to write this file, so
  # an adopter installing a new template got "missing live copy" from the command documented as the
  # fix for it, forever. --check keeps the failure: there, an absent live copy IS the finding.
  if [ ! -f "$live" ] && [ "$MODE" != --render ]; then
    echo "kit-parity: missing live copy $live"; st=1; continue
  fi
  if [ ! -f "$ship" ]; then echo "kit-parity: missing shipped copy $ship"; st=1; continue; fi
  case "$MODE" in
    --render)
      # mkdir -p, because a FIRST-time adopter has no memory/guides/ at all. Without it the redirect
      # failed with "No such file or directory", the success line printed anyway, and the command
      # exited 0 leaving no file — a write failure reported as a render.
      if ! mkdir -p "$(dirname "$live")"; then
        echo "kit-parity: cannot create $(dirname "$live") for $live"; st=1; continue
      fi
      if ! render "$ship" > "$live"; then
        echo "kit-parity: FAILED to write $live"; st=1; continue
      fi
      echo "kit-parity: rendered $live from $ship" ;;
    --check)
      # CR is stripped from BOTH sides. The live copy is pinned `eol=lf` and the template now is
      # too, but a gate that byte-compares needs the comparison right as well as the bytes: with
      # only the live side normalised, a CRLF-smudged template reds every line and goes green again
      # the moment someone re-renders — green-by-accident, not a gate.
      if ! diff -q <(sed 's/\r$//' "$live") <(render "$ship" | sed 's/\r$//') >/dev/null; then
        echo "kit-parity: DRIFT — $live does not match $ship rendered for this install ('$KITREL')"
        diff <(sed 's/\r$//' "$live") <(render "$ship" | sed 's/\r$//') | head -30 | sed 's/^/    /'
        echo "    fix: bash $KITREL/kit-dogfood-parity.test.sh --render"
        st=1
      fi
      # A render that leaves a placeholder standing would ship a literal `{{KIT_DIR}}` into an
      # adopter's committed rule set. The diff above cannot catch it, because a live copy rendered by
      # the same broken substitution matches perfectly.
      if render "$ship" | grep -q '{{[A-Z_]*}}'; then
        echo "kit-parity: $ship still holds an unsubstituted placeholder after rendering:"
        render "$ship" | grep -n '{{[A-Z_]*}}' | head -5 | sed 's/^/    /'
        st=1
      fi ;;
    *) echo "usage: $0 [--check|--render]"; exit 2 ;;
  esac
done

# The pair list is the population, and an empty one would pass silently — the same green-by-absence
# shape checked elsewhere in this kit.
[ -n "$PAIRS" ] || { echo "kit-parity: no document pairs configured — that is not a pass"; exit 1; }
# S3: was `[ "$MODE" = --render ] && exit 0`, which DISCARDED st — so every --render exited 0 even
# when it had just printed a failure. A mode that cannot report its own failure is not reporting.
[ "$MODE" = --render ] && exit "$st"
# The count is DERIVED from the population it reports on. It was a literal `2 pairs`, which is a
# second hand-kept spelling of PAIRS — the drift class this file exists to catch, sitting in this
# file's own success line. A third pair landed and the leg still said two.
set -- $PAIRS; npairs=$#
[ "$st" = 0 ] && echo "kit-parity: shipped and installed docs agree ($npairs pairs, rendered for '$KITREL')"
exit "$st"
