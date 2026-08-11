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
[ -z "$TOOLROOT" ] || TOOLROOT="$TOOLROOT/"

MODE="${1:---check}"
PAIRS="$M/HYGIENE.md:$KITREL/HYGIENE.template.md $M/TEMPLATE-SPEC.md:$KITREL/SPEC-TEMPLATE.template.md $M/guides/BUILD-METHOD.md:$KITREL/BUILD-METHOD.template.md"

# Byte-identical in intent to `render_doc` in adopt-memory-tree.sh. Two spellings of one
# substitution is the drift class this file exists to catch, so the SHAPE arm below proves they agree
# on the only thing that matters: no placeholder survives a render.
render() {
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
  out=${out//\{\{KIT_DIR\}\}/"$KITREL"}
  out=${out//\{\{TOOL_ROOT\}\}/"$TOOLROOT"}
  printf '%s' "$out"
}

st=0
for pair in $PAIRS; do
  live=${pair%%:*}; ship=${pair##*:}
  if [ ! -f "$live" ]; then echo "kit-parity: missing live copy $live"; st=1; continue; fi
  if [ ! -f "$ship" ]; then echo "kit-parity: missing shipped copy $ship"; st=1; continue; fi
  case "$MODE" in
    --render) render "$ship" > "$live"; echo "kit-parity: rendered $live from $ship" ;;
    --check)
      if ! diff -q <(sed 's/\r$//' "$live") <(render "$ship") >/dev/null; then
        echo "kit-parity: DRIFT — $live does not match $ship rendered for this install ('$KITREL')"
        diff <(sed 's/\r$//' "$live") <(render "$ship") | head -30 | sed 's/^/    /'
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
[ "$MODE" = --render ] && exit 0
# The count is DERIVED from the population it reports on. It was a literal `2 pairs`, which is a
# second hand-kept spelling of PAIRS — the drift class this file exists to catch, sitting in this
# file's own success line. A third pair landed and the leg still said two.
set -- $PAIRS; npairs=$#
[ "$st" = 0 ] && echo "kit-parity: shipped and installed docs agree ($npairs pairs, rendered for '$KITREL')"
exit "$st"
