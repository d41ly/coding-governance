#!/usr/bin/env bash
# check-method-carriers.sh — every file that POINTS AT the build method is declared, and points
# rather than copies. Exit 0 = clean · 1 = drift · 2 = misconfigured.
#
#   bash tools/memory-tree/check-method-carriers.sh
#
# WHY THIS EXISTS. The build method landed with four pointers, each a path and never a summary.
# Nothing stopped a fifth being added tomorrow as a paraphrase, and this repo grew FOUR spellings of
# its unattended rules exactly that way — one well-meaning summary at a time, none of them wrong on
# the day it was written. A new carrier should be a decision somebody makes, not a thing that happens.
#
# WHAT IT IS NOT. It does not read prose and judge whether a file restates M3. The test is structural
# — is this file declared, and does its mention look like a pointer rather than a copied section —
# and that is all it claims. A fluent paraphrase that invents its own headings passes here.
#
# THE REGISTRY IS PER-REPO, under <MEMORY_ROOT>/project/ with the gate's other waiver registries. The
# kit ships no registry: gov's rows would otherwise travel to an adopter whose tree does not contain
# those paths, and every adopter would red on install. `adopt-memory-tree.sh` scaffolds an adopter's
# from their OWN measured population.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "method-carriers: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
MEMORY_ROOT=memory
[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"
M="$MEMORY_ROOT"
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT_N="$(cd "$ROOT" && pwd)"
KITREL=${HERE#"$ROOT_N"/}
[ "$KITREL" = "$HERE" ] && { echo "method-carriers: cannot locate this kit inside the repo"; exit 2; }

DOC="BUILD-METHOD.md"
REG="$M/project/method-carriers.txt"
st=0
fail() { echo "METHOD-CARRIERS check $1 FAILED — $2"; st=1; }

# ---- 1: the registry must EXIST. An absent registry is the violation, not the exemption — the same
# ---- rule this tree's other registries carry. Without it every arm below reads a green empty set.
if [ ! -f "$REG" ]; then
  fail 1 "no registry at $REG, and an absent registry is not an empty one — scaffold it with 'bash $KITREL/adopt-memory-tree.sh --scaffold'"
  exit "$st"
fi

# The population. EXCLUSIONS, each for its own reason:
#   <MEMORY_ROOT>/  — the method's own render, its records, specs, reviews and backlog rows all
#                     discuss it legitimately. This also SUBSUMES the registry, which lives under
#                     project/: one exclusion, not two, and saying so keeps a future reader from
#                     adding a second that can never fire.
#   the template    — it IS the method, one render away.
#   *.test.sh       — a test builds a violating fixture on purpose, which is why
#                     `check-install-prefix.sh` excludes its own tests too.
#   this leg        — it necessarily contains the literal it greps for.
# TOOL-aScouredKit-6 — ONE grep over the whole eligible set, not one grep PER FILE. The exclusions
# are unchanged and are still applied first; only the search is batched. Measured on node `a`:
# 1156 spawns and 22.45 s became 0.69 s, at byte-identical output. This leg is `subject = repo` with
# an empty guard, so it runs on every bar in every adopting tree and its cost scaled with THEIR
# tracked file count rather than with the kit's.
#
# `grep -l` exits 1 on no match, which is the passing-zero-reads-as-failure class the charter names —
# so the pipeline is terminated with `|| true` and the EMPTY case is decided by the explicit refusal
# below, which is where it belongs. `xargs -0` with a NUL-delimited list is what keeps a path
# containing a space or a quote from being re-split, and `-r` keeps an empty list from running grep
# against stdin, which would hang the bar waiting for input nobody types.
carriers=$(git ls-files -z | while IFS= read -r -d '' f; do
  case "$f" in
    "$M"/*) continue ;;
    "$KITREL"/BUILD-METHOD.template.md) continue ;;
    "$KITREL"/check-method-carriers.sh) continue ;;
    *.test.sh) continue ;;
  esac
  printf '%s\0' "$f"
done | xargs -0 -r grep -lF -- "$DOC" 2>/dev/null || true)

# ---- 2: an EMPTY population is a refusal. If nothing outside the memory tree points at the method,
# ---- either it has been unwired — the loudest possible drift — or this selector is mis-segmented,
# ---- which is the shape that makes every arm below vacuously true. Guarded explicitly, because
# ---- `vacuous-selector-empty-population` is a class this repo has already been bitten by.
if [ -z "$carriers" ]; then
  fail 2 "no file outside $M/ mentions $DOC at all, so either the method has been unwired or this selector is mis-segmented — an empty population is not a clean one"
  exit "$st"
fi

declared=$(grep -vE '^\s*(#|$)' "$REG" | sed 's/ *·.*//;s/[[:space:]]*$//')

# ONE pass, collecting into variables the MAIN shell owns. Every `while` below would otherwise run in
# a pipeline subshell, where `st=1` is set and discarded — the defect that makes a red gate print its
# complaint and exit 0.
# `while read`, never `for x in $list`: an unquoted expansion word-splits, so any path with a space
# becomes two nonexistent paths and reds forever with no fix available to the adopter. gov's tree has
# no such path, which is exactly why this was invisible here.
undeclared=""; copied=""
while IFS= read -r c; do
  [ -n "$c" ] || continue
  printf '%s\n' "$declared" | grep -qxF "$c" || undeclared="$undeclared$c
"
  grep -qE '^## M[0-9]+' "$c" 2>/dev/null && copied="$copied$c
"
done <<EOF
$carriers
EOF
gone=""; stale=""
while IFS= read -r d; do
  [ -n "$d" ] || continue
  if [ ! -f "$d" ]; then gone="$gone$d
"
  elif ! grep -qF "$DOC" "$d"; then stale="$stale$d
"
  fi
done <<EOF
$declared
EOF

# ---- 3: every carrier is DECLARED. The drift this leg exists to catch — a new file starts
# ---- mentioning the method and nobody decided whether it points at it or restates it.
[ -z "$undeclared" ] || fail 3 "a file mentions $DOC and is not declared in $REG, so nobody decided whether it points at the method or restates it:
$(printf '%s' "$undeclared" | sed 's/^/    /')"

# ---- 4: every declared row still HITS, in both directions. A stale row is the failure
# ---- `install-prefix-waivers.txt` produced by keying on <path>:<line> — an edit ABOVE the line
# ---- unpinned it and the gate redded on a merge that touched nothing it guarded
# ---- (TOOL-aSealedCaravan-1). This registry keys on PATH alone, so a row goes stale only when its
# ---- file really stops pointing.
[ -z "$gone" ] || fail 4 "a declared carrier no longer exists, so its row guards nothing:
$(printf '%s' "$gone" | sed 's/^/    /')"
[ -z "$stale" ] || fail 4 "a declared carrier no longer mentions $DOC, so its row is stale and would mask the next real one:
$(printf '%s' "$stale" | sed 's/^/    /')"

# ---- 5: a carrier POINTS, it does not COPY. `## M<n>` is the method's own heading grammar. It is
# ---- NOT unique tree-wide — review records use it — but every such occurrence sits inside the
# ---- <MEMORY_ROOT>/ region excluded above, so the heuristic is sound over the SCANNED population
# ---- and unsound as a general claim. Narrow on purpose: it catches the shape the four unattended
# ---- spellings actually took, a copied bulleted section, not a subtle rewording.
[ -z "$copied" ] || fail 5 "a carrier holds a '## M<n>' heading, the method's own section grammar and the shape a COPY takes rather than a pointer:
$(printf '%s' "$copied" | sed 's/^/    /')"

n=$(printf '%s\n' "$carriers" | grep -c .)
[ "$st" = 0 ] && echo "method-carriers: $n carrier(s), all declared and pointing"
exit "$st"
