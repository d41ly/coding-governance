#!/usr/bin/env bash
# adopt-drift-audit.sh — wire the drift-audit kit into a project.
#
# gov:kit drift-audit@1.9
#
# Run from anywhere INSIDE the target repo AFTER copying this kit dir in as `tools/drift-audit/`.
# The kit dir's NAME is load-bearing; the one-segment prefix is free and every path below is derived
# from it, so a root install still works and still prints runnable commands:
#
#   tools/drift-audit/adopt-drift-audit.sh            # seed the project layer + render the Skill
#   tools/drift-audit/adopt-drift-audit.sh --check    # verify the rendered Skill still matches the kit
#
# Steps: require .memory-tree.conf (owned by the memory-tree kit; refuse, never create) -> seed
# drift_signals.py from the template IF ABSENT (never overwrite: the pins are measured project
# state) -> render .claude/skills/drift-audit/SKILL.md from SKILL.template.md -> report next steps.
#
# `--check` is the merge-bar arm: the rendered Skill must still match what the template plus the
# adopter's conf produce. It renders to a temp file and diffs, so a hand-edited Skill reds instead of
# silently outliving the kit it came from.
#
#   Exit 0 = adopted / in sync · 1 = out of sync or unusable · 2 = wrong invocation or not a repo.
set -u

# TOOL-aScouredKit-15 — the second argument is the SIBLING KIT'S installed directory: optional,
# positional, and it exists because this kit cannot DERIVE it and an environment variable is not
# DURABLE. The gate leg re-invokes this script with a fresh environment on every bar, so an
# env-only answer set at render time is gone by the time `--check` grades what was rendered, and
# the two disagree. The descriptor passes `{prefix}/review-harness` instead, so the answer travels
# with the install. Absent, the derivation further down still applies, which is what keeps a
# hand-install — and this repo's own dogfood, where the sibling really is `tools/workflows` —
# working unchanged.
MODE=""
WORKFLOWS_ARG=""
for _a in "${@:-}"; do
  case "$_a" in
    "") ;;
    --check) MODE="--check" ;;
    -*) echo "usage: $0 [--check] [<workflows-dir>]"; exit 2 ;;
    *) [ -z "$WORKFLOWS_ARG" ] || { echo "usage: $0 [--check] [<workflows-dir>]"; exit 2; }
       WORKFLOWS_ARG="$_a" ;;
  esac
done

KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(git -C "$KIT_DIR" rev-parse --show-toplevel 2>/dev/null)" || { echo "drift-audit: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

CONF="$ROOT/.memory-tree.conf"
if [ ! -f "$CONF" ]; then
  cat >&2 <<'EOF'
drift-audit: .memory-tree.conf not found.

It is owned by the memory-tree kit, so this kit refuses rather than creating a second declaration of
the corpus root. Adopt memory-tree first, or write the minimum stub:

  MEMORY_ROOT=memory
  DISCIPLINES="<your disciplines>"
EOF
  exit 1
fi

# CR-strip: a CRLF-committed conf keeps \r in sourced values on Linux (MSYS masks this).
MEMORY_ROOT="$(tr -d '\r' < "$CONF" | sed -n 's/^MEMORY_ROOT=//p' | head -1)"
MEMORY_ROOT="${MEMORY_ROOT:-memory}"

SKILL_DIR="$ROOT/.claude/skills/drift-audit"
SKILL_OUT="$SKILL_DIR/SKILL.md"
TEMPLATE="$KIT_DIR/SKILL.template.md"
[ -f "$TEMPLATE" ] || { echo "drift-audit: SKILL.template.md missing from the kit"; exit 1; }

# The kit dir's name as the adopter sees it, so the rendered Skill's commands are copy-pasteable.
# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to tools/lib/resolve-python.sh
# and tools/lib/resolve-python.test.sh reds if any copy drifts.
#
# This site spelled `python` BARE, which is why V5's migration missed it: the idiom ban matches
# `command -v`, and a bare launcher name carries no such marker. On a python3-only host — or one
# where the MS-Store stub answers for python3 — this line produced an empty KIT_REL and the
# `--check` leg then reported drift on a Skill that had never changed.
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
DA_PY=$(resolve_python) || exit 2
KIT_REL="$("$DA_PY" -c "import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]).replace(os.sep,'/'))" "$KIT_DIR" "$ROOT")"
[ -n "$KIT_REL" ] || { echo "drift-audit: could not derive the kit path — refusing to render a Skill with an empty command prefix"; exit 2; }

# The two deep-tier workflow scripts live in a SIBLING kit, so their path is DERIVED from this kit's
# own install prefix, never spelled. Measured: the template hardcoded
# `workflows/`, so at this repo's own `tools/` prefix the rendered Skill instructed an agent to run
# two files that do not exist — and `--check` reported "in sync", because it diffs the render against
# the template and BOTH carried the same wrong spelling. Parameterising this kit's own dir while
# hardcoding a sibling's is the whole defect; a derived value cannot drift from the install.
# TOOL-aScouredKit-15 — THE DERIVATION GUESSES THE SIBLING'S DIRECTORY NAME, and in a govkit-deployed
# tree the guess is wrong. govkit lands a kit at `{prefix}/{entry-id}` and the harnesses' entry id is
# `review-harness`, not `workflows` — so an adopter at `vendor/gov` got a Skill pointing at
# `vendor/gov/workflows/`, which govkit never creates. gov itself is right BY COINCIDENCE: its own
# directory is literally `tools/workflows` and it does not deploy into itself. The comment above
# claimed a derived value "cannot drift from the install"; it cannot drift from the PREFIX, which is
# a different and weaker property, and this is what that gap cost.
#
# Two changes, and the second is the one that matters. `DRIFT_WORKFLOWS_REL` lets whoever knows the
# real destination say so. And the paths are ASSERTED to exist below rather than assumed, so a wrong
# answer is a refusal naming the override instead of a Skill that instructs an agent to run nothing.
case "$KIT_REL" in
  */*) WORKFLOWS_REL="${KIT_REL%/*}/workflows" ;;   # prefixed install: sibling of this kit
  *)   WORKFLOWS_REL="workflows" ;;                 # root install: sibling at the root
esac
# THE ANSWER IS PERSISTED, and that file is the point. The gate LEG cannot carry the sibling's path
# in its argv — `govkit selfcheck` refuses a leg naming a path this entry does not ship, correctly,
# because an adopter may install drift-audit alone — and an environment variable does not survive
# to the leg's own fresh process. So the ADOPT run writes the answer next to the kit and every
# TOOL-aScouredKit-30 — ONE DERIVATION, BOTH INVOCATIONS, and the persistence that used to sit here
# is GONE. Three review rounds each produced a fix whose next round refuted it, for one reason the
# first design missed: `adopt` and `--check` must resolve the SAME value, and `--check` cannot be
# given one. `govkit selfcheck` refuses a gate-leg argv naming a path the entry does not ship — an
# adopter may install drift-audit alone — so the leg carries nothing. Every channel that reached
# `adopt` alone therefore made the two DISAGREE, and the diff arm then reds with a message that
# misdiagnoses the cause and a remedy that overwrites the correct Skill with the wrong one: a red
# turned into a green over a broken artifact, which is worse than the silence this started from.
#
# The `{kit}/.workflows-rel` store was the attempt to bridge that, and it failed separately: it is
# untracked, claimed by no `[[files]]` rule and in no receipt, so it does not survive a fresh
# checkout — where the leg re-derives, disagrees with the committed Skill, and reds.
#
# So no answer is carried. The pointer is WRONG in a govkit-deployed tree, exactly as it was before
# this build; what changed is that it is no longer SILENT, which was the actual finding. The real
# fix needs a cross-entry destination token govkit does not have: `TOOL-aScouredKit-26`.
#
# `DRIFT_WORKFLOWS_REL` survives for a hand-install, where one person runs both invocations and can
# export it for both. It is deliberately NOT a deployment channel.
WORKFLOWS_REL="${WORKFLOWS_ARG:-${DRIFT_WORKFLOWS_REL:-$WORKFLOWS_REL}}"

# The two files the rendered Skill tells an agent to run. Named once, checked in both modes.
#
# NO "IS THE KIT INSTALLED AT ALL" BRANCH. One stood here and round 3 proved it cannot be written:
# it inspected the DERIVED path, so "the sibling kit is not installed" and "it is installed
# somewhere else" produced the same answer — and the second is the defect. It therefore reported a
# clean bill over exactly the tree this check exists for, restoring the silence it was added to
# remove. Measured with the harnesses really at `tools/review-harness` and no answer supplied:
# adopt printed nothing and `--check` exited 0 asserting the kit was absent.
_wf_missing() {
  local miss="" f
  for f in drift-audit-code.js drift-audit-state.js; do
    [ -f "$ROOT/$WORKFLOWS_REL/$f" ] || miss="$miss $WORKFLOWS_REL/$f"
  done
  printf '%s' "$miss"
}
_wf_complain() { # $1 = the missing list, non-empty
  echo "drift-audit: the rendered Skill points at deep-tier harnesses that are NOT THERE:$1"
  echo "drift-audit: this kit derives its sibling's directory from its own install prefix, which"
  echo "drift-audit: assumes the sibling is named 'workflows'. A govkit-deployed tree lands it under"
  # SUGGESTED FROM THIS KIT'S OWN PARENT, never from WORKFLOWS_REL — deriving the hint from the
  # value being complained about prints "set it to X" when X is what it already is.
  case "$KIT_REL" in
    */*) echo "drift-audit: the ENTRY ID instead — '${KIT_REL%/*}/review-harness' is the usual answer." ;;
    *)   echo "drift-audit: the ENTRY ID instead — 'review-harness' is the usual answer." ;;
  esac
  echo "drift-audit: Set DRIFT_WORKFLOWS_REL to the real path and re-run this script."
}

render() { # -> stdout; LF only (the rendered Skill is pinned LF in .gitattributes)
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
  out=${out//\{\{KIT_DIR\}\}/"$KIT_REL"}
  out=${out//\{\{WORKFLOWS_DIR\}\}/"$WORKFLOWS_REL"}
  out=${out//\{\{MEMORY_ROOT\}\}/"$MEMORY_ROOT"}
  printf '%s' "$out"
}

if [ "$MODE" = "--check" ]; then
  [ -f "$SKILL_OUT" ] || { echo "drift-audit: $SKILL_OUT not rendered — run $0"; exit 1; }
  TMP="$(mktemp)"; trap 'rm -f "$TMP"' EXIT
  render > "$TMP"
  if ! diff -q <(tr -d '\r' < "$SKILL_OUT") "$TMP" >/dev/null 2>&1; then
    echo "drift-audit: $SKILL_OUT is out of sync with SKILL.template.md + .memory-tree.conf"
    echo "  re-render with: $0"
    diff <(tr -d '\r' < "$SKILL_OUT") "$TMP" | head -20
    exit 1
  fi
  # The project layer must exist for the report to run at all; --check is where a half-adoption shows.
  [ -f "$KIT_DIR/drift_signals.py" ] || { echo "drift-audit: drift_signals.py missing — the report cannot run"; exit 1; }
  # TOOL-aScouredKit-15 — ASSERT THE RENDERED PATHS, do not merely re-derive them. Everything above
  # compares a render against the template, so both sides carry the same answer and a WRONG answer
  # is invisible: that is how this leg reported "in sync" over a Skill naming two files that did not
  # exist. An assertion against the filesystem is the only operand this check has that the render
  # cannot supply itself.
  # REPORTED, NOT RED. This kit does not require the review-harness kit and neither is in the
  # registry's default selection, so an adopter may legitimately hold one without the other — and a
  # red they cannot clear is a tax, not a check. Nor can this script tell "not installed" from
  # "installed elsewhere": that needs the sibling's real destination, which is
  # `TOOL-aScouredKit-26`. So it says exactly what it observed and exits 0. The finding this whole
  # thread came from was SILENCE, and silence is what is fixed here; the wrongness itself is not.
  _miss=$(_wf_missing)
  if [ -n "$_miss" ]; then
    _wf_complain "$_miss"
    echo "drift-audit: in sync (skill rendered from template, project layer present) — but see above."
    exit 0
  fi
  echo "drift-audit: in sync (skill rendered from template, project layer present, deep-tier harnesses present at $WORKFLOWS_REL/)"
  exit 0
fi

# Seed the project layer ONCE. Never overwrite: PINS are measured project state, and re-seeding a
# repo that already tuned them would silently reset every ratchet to the template's zeros.
if [ -f "$KIT_DIR/drift_signals.py" ]; then
  echo "drift-audit: drift_signals.py already present — left untouched"
else
  cp "$KIT_DIR/drift_signals.template.py" "$KIT_DIR/drift_signals.py"
  echo "drift-audit: seeded drift_signals.py from the template — FILL IT before trusting the report"
fi

mkdir -p "$SKILL_DIR"
render > "$SKILL_OUT"
echo "drift-audit: rendered $SKILL_OUT"
# The same assertion at ADOPT time, as a WARNING rather than a refusal. The render is the useful
# part of this run and withholding it over a sibling kit the operator may not have selected would
# be worse than shipping it with a loud caveat — but silence is what let a dead pointer sit in an
# adopter's Skill unnoticed, so the caveat is not optional. `--check` is where it reds.
_miss=$(_wf_missing)
[ -n "$_miss" ] && _wf_complain "$_miss"

cat <<EOF

Next:
  1. Fill $KIT_REL/drift_signals.py — PRODUCT_GLOBS at minimum.
  2. Run:  python $KIT_REL/drift_report.py
  3. Seed PINS at the values you just measured, not at zero, then re-run with --check (expect 0).
  4. Wire the --check arm into your gate manifest so a regression reds.
EOF
