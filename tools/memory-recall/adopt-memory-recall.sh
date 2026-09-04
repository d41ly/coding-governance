#!/usr/bin/env bash
# adopt-memory-recall.sh — render the memory-recall Skill from `.memory-tree.conf` and converge.
#
#   tools/memory-recall/adopt-memory-recall.sh --scaffold [--with-hook]
#   tools/memory-recall/adopt-memory-recall.sh --check                  # gate leg: has the skill drifted?
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
# `--with-hook` is the ONLY way the `recall-opened` PostToolUse hook is installed. Skipping it is a
# supported end state: a hook file copied in but never merged into settings.json reads as UNWIRED
# forever, which is the fastest way to train every node to ignore the wiring verifier.
#
# The interpreter is resolved python3-first with a `python` fallback (the tools/check-wiring.sh:69
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
# silently. Works whether the kit sits at <root>/memory-recall/ or <root>/tools/memory-recall/.
REL="$(cd "$HERE" && git rev-parse --show-prefix)" || exit 2
REL="${REL%/}"

# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to tools/lib/resolve-python.sh
# and tools/lib/resolve-python.test.sh reds if any copy drifts.
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
    echo "memory-recall: --with-hook asked for, but $REL/recall-opened.js is not installed"; exit 1
  fi
  # NOTHING IS COPIED ANY MORE. The hook SHIPS at $REL/recall-opened.js and is wired there.
  #
  # This block used to `mkdir -p .claude/hooks` and copy into it, which RE-CREATED the exact
  # duplicate TOOL-dRetiredFork-14 withdrew: an adopter who took this opt-in got the second copy
  # back whatever the descriptor said, and a closing instruction naming it. That instruction is the
  # last thing they read at the moment they wire the hook, so a stale path here is worse than a
  # stale path in a descriptor -- one is followed by hand, the other is resolved by a tool.
  echo "$REL/recall-opened.js is installed — now merge it into settings.json:"
  # RESOLVED, not hardcoded — this is the last instruction an adopter sees at the moment they take
  # the opt-in, and the step whose omission leaves the hook inert. A hardcoded tools/ path printed
  # here died with errno 2 in an adopter, because no runbook step delivered the tool. WIRE §3c
  # step 4 now copies it to tools/; when it still is not there, say so instead of pretending.
  smerge=""
  for c in tools/settings-merge.py settings-merge.py; do [ -f "$ROOT/$c" ] && { smerge="$c"; break; }; done
  if [ -z "$smerge" ]; then
    echo "  cp <gov>/tools/settings-merge.py tools/     # not installed here yet (WIRE §3c step 4)"
    smerge=tools/settings-merge.py
  fi
  echo "  $PY $smerge --fragment $REL/recall-opened.fragment.json"
fi

echo "Adopted. Next:"
echo "  1. Add both legs to your gate runner AND your CI config (see WIRE-INTO-PROJECT.md):"
echo "       $PY $REL/selftest.py"
echo "       bash $REL/adopt-memory-recall.sh --check"
echo "     Without this the skill-drift check silently never runs."
echo "  2. Re-run --scaffold after any FAMILIES/MEMORY_ROOT edit; --check reds until you do."
