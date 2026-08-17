#!/usr/bin/env bash
# adopt-lexicon.sh — scaffold or verify this repo's naming-lexicon declaration.
#
#   bash tools/lexicon/adopt-lexicon.sh --scaffold   # DERIVE a proposed verb table + measure pins
#   bash tools/lexicon/adopt-lexicon.sh --check      # the drift mode every kit here carries
#
# WHY THE SEED IS DERIVED AND THEN FROZEN. Companion §12 bans a gate whose vocabulary is a
# hand-kept mirror of the codebase's own identifiers; a PRESCRIPTIVE verb table is the inverse and
# is safe. But an adopter cannot author a closed vocabulary for a domain they have not read yet, so
# `--scaffold` derives a proposal from their own corpus by leading-token frequency — which for one
# moment IS the banned shape. The resolution is that the proposal is marked PROPOSED, a human
# curates it, and "was edited" is CHECKABLE: `--check` reds while `ratified` is empty, so an
# unedited seed cannot reach the merge bar disguised as a curated vocabulary.
#
# Pins are MEASURED against the adopting corpus, never inherited. `.memory-tree.conf` states the
# rule in its own words: a pin copied from a larger tree is either vacuous or permanently red.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "lexicon-adopt: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
KIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONF="$ROOT/.lexicon.conf"

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

PY="$(resolve_python)" || { echo "$PY"; exit 2; }

MODE="${1:---check}"
case "$MODE" in --scaffold|--check) ;; *) echo "usage: $(basename "$0") [--scaffold|--check]"; exit 2 ;; esac

if [ "$MODE" = "--check" ]; then
  fail=0
  if [ ! -f "$CONF" ]; then
    # THE MID-TEARDOWN ARM. An absent conf is normally just "not adopted" — but if this repo still
    # declares the `lexicon-verbs` inventory, the conf was deleted BEFORE the extractor was removed,
    # which is step 4 done before step 2 of the uninstall order. The map gate does red on that state,
    # but it reds as a stale dossier claim, which reads like a map problem rather than a half-removed
    # kit. Naming it here is the difference between a confusing red and an actionable one.
    if [ -f "$ROOT/tools/codebase-map/map_extractors.py" ] \
       && grep -q '"lexicon-verbs"' "$ROOT/tools/codebase-map/map_extractors.py" 2>/dev/null; then
      echo "lexicon-adopt: ORPHANED EXTRACTOR — .lexicon.conf is gone but map_extractors.py still"
      echo "lexicon-adopt: declares the \`lexicon-verbs\` inventory, so the map's dossier claims now"
      echo "lexicon-adopt: name keys nothing produces. This is the uninstall order run backwards."
      echo "lexicon-adopt: Remove the dossier claims, then the EXTRACTORS entry, then re-render"
      echo "lexicon-adopt: memory/map/generated/ — tools/lexicon/README.md carries the full order."
      exit 1
    fi
    echo "lexicon-adopt: NOT ADOPTED — no .lexicon.conf at the repo root. The kit is opt-in; this is"
    echo "lexicon-adopt: a legal state, not a defect. Run --scaffold to adopt it."
    exit 0
  fi
  # The conf must PARSE through the kit's one reader. A second parser here is the
  # two-answers-to-one-question class, so this shells out rather than re-implementing the grammar.
  if ! "$PY" "$KIT_DIR/lexicon_conf.py" --print-verbs "$CONF" >/dev/null; then
    echo "lexicon-adopt: .lexicon.conf does not parse — see the refusal above"
    fail=1
  fi
  # S10 — the unratified-seed refusal. This is the arm that makes "the human curated it" checkable.
  # `tr -d '\r'` FIRST. Both halves of this are needed and the pin alone is not enough: an anchored
  # `s/"$//` cannot strip a quote that a carriage return follows, so a CRLF conf yields `"\r` — a
  # NON-EMPTY value — and the unratified-seed refusal passes exactly when it should fire.
  ratified=$(tr -d '\r' < "$CONF" | grep -E '^ratified=' | head -1 | sed -E 's/^ratified=//; s/^"//; s/"$//')
  if [ -z "${ratified// /}" ]; then
    echo "lexicon-adopt: .lexicon.conf carries an EMPTY \`ratified\` key. --scaffold DERIVES the verb"
    echo "lexicon-adopt: table from your corpus and marks it PROPOSED; a derived table that nobody"
    echo "lexicon-adopt: curated is a mirror of the code, which is the shape a naming gate must not"
    echo "lexicon-adopt: have. Curate the table, then stamp \`ratified=\"<date> node <tag>\"\`."
    fail=1
  fi
  verbs=$("$PY" "$KIT_DIR/lexicon_conf.py" --print-verbs "$CONF" 2>/dev/null | grep -c . || true)
  if [ "${verbs:-0}" -eq 0 ]; then
    echo "lexicon-adopt: the VERBS table is EMPTY. Every P1 identifier would be an offender, so the"
    echo "lexicon-adopt: pin would absorb the whole corpus and the predicate would assert nothing."
    fail=1
  fi
  [ "$fail" -eq 0 ] && echo "lexicon-adopt OK — .lexicon.conf parses, ratified, $verbs verb(s) declared"
  exit "$fail"
fi

# ---- --scaffold ---------------------------------------------------------------------------------
if [ -f "$CONF" ]; then
  echo "lexicon-adopt: .lexicon.conf already exists — refusing to overwrite a curated declaration."
  echo "lexicon-adopt: Delete it deliberately if you mean to re-derive the seed."
  exit 1
fi
"$PY" "$KIT_DIR/scaffold_lexicon.py" "$CONF" || exit 1
echo "lexicon-adopt: wrote .lexicon.conf marked PROPOSED — curate the table, then stamp \`ratified=\`."
