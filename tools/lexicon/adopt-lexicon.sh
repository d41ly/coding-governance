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

# REPO-RELATIVE, via git rather than by trimming ROOT off KIT_DIR. On Windows those two are
# spelled differently -- `git rev-parse --show-toplevel` answers `C:/...` while `cd && pwd` under
# MSYS answers `/c/...` -- so the trim silently does nothing and the ABSOLUTE path renders into a
# committed artifact. Measured here: it shipped into the Skill description before this line
# existed. memory-recall carries the same derivation and the same warning; this is the second
# time that warning has been paid for.
KITREL="$(cd "$KIT_DIR" && git rev-parse --show-prefix)" || exit 2
KITREL="${KITREL%/}"
TEMPLATE="$KIT_DIR/SKILL.template.md"
SKILL="$ROOT/.claude/skills/lexicon/SKILL.md"
KIT_VERSION="$(grep -oE 'KIT_LEXICON_VERSION = "[0-9.]+"' "$KIT_DIR/lexicon.py" | grep -oE '[0-9.]+' | head -1)"
# ---- S4 of TOOL-dScaffoldedMirror-10: the rendered Skill -----------------------------------------
#
# WHY A RENDER AND NOT A POINTER. The charter can only POINT at the declaration -- it has 118 bytes of
# headroom against a 1,787-byte table -- so the only way the table itself travels to an author is a
# separate artifact. And an artifact that carries a copy of a declaration is a second carrier, which
# this repo's own rule says drifts. The answer is that the copy is GENERATED and its gate re-renders
# and byte-compares: a `.lexicon.conf` edit nobody re-rendered REDS. That is the one shape in which
# two carriers are allowed, because only one of them is authored.
#
# THREE STATES, NOT TWO, copied deliberately from memory-recall. A missing template with no rendered
# Skill is "not installed" and SKIPS -- a red an adopter cannot fix by editing their own repo trains
# them to ignore the leg. A rendered Skill with no template is the one genuinely unverifiable state
# and it REDS.
render_skill() { # -> stdout
  local out verbs
  # The table, rendered from the declaration rather than retyped. Every row, in declaration order.
  verbs=$("$PY" - "$CONF" <<'PYEOF'
import io, re, sys
src = io.open(sys.argv[1], encoding="utf-8", errors="replace").read().replace("\r", "")
rows, inblock = [], False
for line in src.split("\n"):
    if line.startswith("VERBS:"):
        inblock = True
        continue
    if inblock:
        if not line.strip():
            continue
        if not line.startswith(" "):
            break
        m = re.match(r"\s+(\S+)\s+(.*)$", line)
        if m:
            rows.append("- `%s` — %s" % (m.group(1), m.group(2).strip()))
print("\n".join(rows))
PYEOF
) || return 1
  [ -n "$verbs" ] || return 1
  out=$( cat "$TEMPLATE" || exit 1; printf X ) || return 1
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{VERBS_TABLE\}\}/"$verbs"}
  out=${out//\{\{SUGGEST_CLI\}\}/"python3 $KITREL/lexicon.py --suggest"}   # gov:literal-python
  out=${out//\{\{BRIEF_CLI\}\}/"python3 $KITREL/lexicon.py --brief"}       # gov:literal-python
  out=${out//\{\{GATE_CLI\}\}/"python3 $KITREL/lexicon.py"}                # gov:literal-python
  out=${out//\{\{CONF\}\}/".lexicon.conf"}
  out=${out//\{\{KIT_VERSION\}\}/"$KIT_VERSION"}
  # STRIP CR AFTER SUBSTITUTION, not only from the template. Python's `print` writes CRLF to stdout
  # on Windows, so `$verbs` arrives CR-bearing however clean the template is — measured here: the
  # render carried \r\n on every verb row while the on-disk Skill carried \n, and `--check` reported
  # DRIFTED against a file it had just written. memory-recall's adopter records the same class one
  # seam earlier ("those CRs rendered straight into SKILL.md and broke its YAML frontmatter"); the
  # lesson that transfers is that the strip belongs at the LAST point before emission, where it
  # covers every value rather than the one the author remembered.
  out=${out//$'\r'/}
  printf '%s' "$out"
}

check_skill() {
  local rendered
  if [ ! -f "$TEMPLATE" ]; then
    if [ -f "$SKILL" ]; then
      echo "lexicon: $SKILL exists but $KITREL/SKILL.template.md does not — cannot verify drift"
      return 1
    fi
    echo "skip     lexicon skill — $KITREL/SKILL.template.md not installed, nothing to render"
    return 0
  fi
  rendered="$(render_skill)" || { echo "lexicon: the Skill render failed"; return 1; }
  # AC7 — an EMPTY render must refuse rather than be compared against an equally empty Skill and
  # pass. Two empty files are byte-identical, so the comparison itself cannot see this.
  if [ -z "$rendered" ]; then
    echo "lexicon: the Skill render produced NOTHING, so a byte-comparison against it would pass"
    echo "lexicon: on emptiness rather than on agreement. Refusing instead."
    return 1
  fi
  # An unsubstituted placeholder ships `{{...}}` into a Skill description and breaks its trigger.
  local leftover
  leftover="$(printf '%s' "$rendered" | grep -o '{{[A-Z_]*}}' | sort -u | tr '\n' ' ')"
  if [ -n "$leftover" ]; then
    echo "lexicon: the Skill template carries placeholders this script cannot fill: $leftover"
    return 1
  fi
  if [ ! -f "$SKILL" ]; then
    echo "lexicon: $SKILL is not rendered — run --scaffold"
    return 1
  fi
  # TWO TEMP FILES, not a pipe into a process substitution. Git-Bash supports `<( )`, but a `diff -q`
  # reading stdin AND a substitution is one of the shapes that fails opaquely there — it returned
  # non-zero on a file it had just rendered, which reads as DRIFTED and is indistinguishable from a
  # real drift. A comparison that cannot be wrong about equality is worth two mktemps.
  local a b
  a="$(mktemp)"; b="$(mktemp)"
  printf '%s' "$rendered" > "$a"
  tr -d '\r' < "$SKILL" > "$b"
  if ! cmp -s "$a" "$b"; then
    rm -f "$a" "$b"
    echo "lexicon: DRIFTED — $SKILL does not match a fresh render of $KITREL/SKILL.template.md."
    echo "lexicon: The declaration moved and nobody re-rendered, so the Skill is teaching a table"
    echo "lexicon: this repo no longer declares. Re-run --render."
    return 1
  fi
  rm -f "$a" "$b"
  return 0
}

write_skill() {
  local rendered
  [ -f "$TEMPLATE" ] || return 0
  rendered="$(render_skill)" || { echo "lexicon: the Skill render failed"; return 1; }
  [ -n "$rendered" ] || { echo "lexicon: the Skill render produced nothing; refusing to write it"; return 1; }
  mkdir -p "$(dirname "$SKILL")"
  printf '%s' "$rendered" > "$SKILL"
  echo "lexicon: rendered $SKILL"
}

MODE="${1:---check}"
case "$MODE" in --scaffold|--check|--render) ;; *) echo "usage: $(basename "$0") [--scaffold|--check|--render]"; exit 2 ;; esac

# --render exists because --scaffold REFUSES on an existing declaration, so without it the only
# remedy for a DRIFTED Skill would be deleting the conf and re-deriving the table. A refusal whose
# only fix is destructive is a refusal people learn to bypass.
if [ "$MODE" = "--render" ]; then
  [ -f "$CONF" ] || { echo "lexicon-adopt: no .lexicon.conf; nothing to render from"; exit 1; }
  write_skill || exit 1
  exit 0
fi

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
  check_skill || fail=1
  [ "$fail" -eq 0 ] && echo "lexicon-adopt OK — .lexicon.conf parses, ratified, $verbs verb(s) declared, Skill in sync"
  exit "$fail"
fi

# ---- --scaffold ---------------------------------------------------------------------------------
if [ -f "$CONF" ]; then
  echo "lexicon-adopt: .lexicon.conf already exists — refusing to overwrite a curated declaration."
  echo "lexicon-adopt: Delete it deliberately if you mean to re-derive the seed."
  exit 1
fi
"$PY" "$KIT_DIR/scaffold_lexicon.py" "$CONF" || exit 1
write_skill
echo "lexicon-adopt: wrote .lexicon.conf marked PROPOSED — curate the table, then stamp \`ratified=\`."
