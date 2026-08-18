#!/usr/bin/env bash
# check-dead-paths.sh — nothing outside `memory/` may name a file this repo DELETED.
#
#   bash tools/check-dead-paths.sh            # assert; exit 1 on an unwaived hit
#   bash tools/check-dead-paths.sh --list     # print every hit, waived or not (authoring aid)
#   bash tools/check-dead-paths.sh --needles  # print the derived needle set (authoring aid)
#
# WHY. `tools/check-install-prefix.sh` already owns half of the dead-path class: a path spelled at
# the wrong PREFIX. The other half is a path that is dead because the file was DELETED, and until
# this gate landed nothing held it. Measured on the v3.0 charter convergence, which deleted two
# companion files: carriers still naming them survived in the repo's front door, the charter every
# session reads, the install runbook, kit READMEs an adopter receives, the kickoff engine's hand-back
# offer, two self-test rule citations, a registry reason string, and a gate's own over-budget REMEDY
# — a message that fires ~1.4 KiB from the ceiling, at the one moment someone needs a followable
# instruction. Several sat on a line the same diff edited: the filename was updated and the clause
# beside it was not. That is not a run of independent oversights, it is one missing gate.
#
# NO COUNT OF THAT POPULATION IS WRITTEN HERE. `--list` derives it, and a figure in this header would
# be a number nothing recomputes — which is the same rot the gate exists to catch.
#
# THE NEEDLES ARE DERIVED FROM GIT, never listed. A basename this repo once tracked and no longer
# tracks is a name that resolves to nothing, and git knows the set exactly. That derivation is what
# keeps the false-positive rate at zero: `package.json`, `GEMINI.md` and `docs/PARALLEL.md` are named
# all over the shipped surface and were never files here, so they are never needles. MEASURED against
# the alternative — flagging any path-shaped token that does not resolve — 217 hits, essentially all
# of them legitimate fixture literals inside Python selftests. That gate would have been waived into
# uselessness on its first day.
#
# EACH NEEDLE ALSO CONTRIBUTES ITS DISTINCTIVE TAIL, because carriers abbreviate. The dead
# `parallel-coding-governance.domain-rules.md` was spelled `.domain-rules.md` in the README and
# `…domain-rules.md` in a kit README, and a full-basename scan saw NEITHER — it is not a refinement,
# it is most of what this gate finds on the real tree. `check-dead-paths.test.sh` arms both spellings
# separately for that reason.
# The tail is the last dotted component plus the extension, and it stops there: the bare extension
# would match everything. A tail that still names a tracked file is DROPPED, so a deleted `a.test.sh`
# cannot make every `test.sh` in the tree a violation.
#
# WHAT IT DOES NOT CATCH, said plainly because a reader who over-trusts this gate is worse off than
# one who does not use it. It matches FILENAMES. A carrier that names the deleted thing in prose
# without spelling a filename — "per its customize companion", "its own 'Customize before use'
# block", "the product template + its two companions" — is invisible here, and carriers of exactly
# that shape were in the v3.0 set. They were found by READING, not by this gate, and nothing here
# would have caught them. It is a floor, not the answer.
#
# `memory/` IS OUT OF SCOPE, and that is a rule rather than a convenience. Specs, reviews, build
# ledgers and archived snapshots are append-only records: they describe what WAS true, and a record
# that names a file deleted after it was written is correct, not stale. Rewriting one to please a
# gate would be falsifying the record.
#
# WAIVERS are a tracked file, one `<path>:<line>` per row with a reason after whitespace, matching
# `install-prefix-waivers.txt` exactly. Shrink-only, and a waiver whose hit is gone reds as stale.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "dead-paths: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

WAIVERS="tools/dead-path-waivers.txt"
# FROZEN SENTINEL. The needle derivation walks history and could go silently empty — a bad
# `--diff-filter`, a shallow clone, a `git log` that stops answering — and an empty needle set makes
# this gate pass by matching nothing, which is the vacuous-selector shape
# (`memory/gotchas/vacuous-selector-empty-population.md`). This basename was deleted at 5b00666 and
# will never return, so its ABSENCE from the derived set means the derivation broke, not that the
# tree got clean.
SENTINEL="parallel-coding-governance.domain-rules.md"

MODE="${1:---check}"
case "$MODE" in --check|--list|--needles) ;; *) echo "usage: $(basename "$0") [--check|--list|--needles]"; exit 2 ;; esac

# --- the needle set, derived ----------------------------------------------------------------------
# Every path ever deleted, reduced to basenames, minus every basename the tree still carries. A file
# deleted from one directory and re-added in another is NOT dead: the name still resolves.
tracked=$(git ls-files)
[ -n "$tracked" ] || { echo "dead-paths: git ls-files is empty — that is not a pass"; exit 2; }
tracked_base=$(printf '%s\n' "$tracked" | sed 's|.*/||' | sort -u)

deleted_base=$(git log --diff-filter=D --name-only --pretty=format: -- . \
               | sed '/^$/d; s|.*/||' | sort -u)
[ -n "$deleted_base" ] || { echo "dead-paths: git history reports no deletion at all — the derivation is broken, not the tree clean"; exit 2; }

gone=$(printf '%s\n' "$deleted_base" | grep -vxF -f <(printf '%s\n' "$tracked_base") || true)

# Each gone basename plus its distinctive tail. `a.b.md` -> `a.b.md` and `b.md`; `a.md` -> `a.md`.
# Then drop any needle that still SUFFIXES a tracked path, which is what stops a generic tail.
#
# ONE awk PASS, deliberately. The first draft filtered in a shell loop that spawned sed and grep per
# needle; measured at 12.3s on this tree and ~2s in a two-commit fixture, which made the self-test the
# slowest leg on the bar by an order of magnitude. The comparison is O(tracked x needles) either way —
# what cost the twelve seconds was process creation, not the string work.
needles=$(printf '%s\n' "$gone" \
  | awk 'NF { print; n = split($0, p, "."); if (n > 2) print p[n-1] "." p[n] }' \
  | sort -u \
  | awk -v tracked="$tracked" '
      BEGIN { nt = split(tracked, tp, "\n") }
      # A compiled artifact or an editor scratch name is not a documentation carrier; excluding it
      # keeps the waiver list about prose. Extension-driven so it needs no per-name list.
      /\.(pyc|pyo|orig|rej)$/ || $0 == ".gitkeep" { next }
      {
        n = $0; ln = length(n)
        for (i = 1; i <= nt; i++) {
          p = tp[i]
          if (p == n) next
          d = length(p) - ln
          if (d > 0 && substr(p, d + 1) == n) {
            c = substr(p, d, 1)
            if (c == "/" || c == ".") next
          }
        }
        print n
      }')
[ -n "$needles" ] || { echo "dead-paths: the derived needle set is EMPTY, so this gate would match nothing and pass"; exit 1; }

if ! printf '%s\n' "$needles" | grep -qxF "$SENTINEL"; then
  echo "dead-paths: the frozen sentinel '$SENTINEL' is not in the derived needle set."
  echo "dead-paths: it was deleted at 5b00666 and cannot come back, so the DERIVATION is broken —"
  echo "dead-paths: a clean verdict from here would be this gate matching nothing and calling it green."
  exit 1
fi

if [ "$MODE" = --needles ]; then
  printf '%s\n' "$needles"
  exit 0
fi

# --- the haystack ---------------------------------------------------------------------------------
# Everything tracked except `memory/` (append-only records) and this gate's own two files, which name
# every needle by construction.
RE=$(printf '%s\n' "$needles" | sed 's/[.[\*^$]/\\&/g' | tr '\n' '|'); RE=${RE%|}
hits=$(git grep -nE "$RE" -- ':(exclude)memory/*' \
                            ":(exclude)$WAIVERS" \
                            ':(exclude)tools/check-dead-paths.sh' \
                            ':(exclude)tools/check-dead-paths.test.sh' 2>/dev/null \
       | awk -F: '{print $1":"$2}' | sort -u)

waived_rows=""
[ -f "$WAIVERS" ] && waived_rows=$(grep -vE '^[[:space:]]*(#|$)' "$WAIVERS" | awk '{print $1}')
waived_n=$(printf '%s' "$waived_rows" | grep -c . || true)

if [ "$MODE" = --list ]; then
  echo "dead-paths: $(printf '%s\n' "$hits" | grep -c .) hit(s) over $(printf '%s\n' "$needles" | grep -c .) derived needle(s)"
  printf '%s\n' "$hits" | while IFS= read -r h; do
    [ -n "$h" ] || continue
    if printf '%s\n' "$waived_rows" | grep -qxF "$h"; then printf '  waived  %s\n' "$h"
    else printf '  HIT     %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"; fi
  done
  exit 0
fi

# SET DIFFERENCE, not a grep per row. Same reason as the needle pass above: the loops below now only
# ever walk the rows that will actually be printed.
#
# NO `-e ''` GUARD ON THE PATTERN SIDE, which the first draft carried to "handle" an empty registry.
# MEASURED: `grep -vxF -e '' -f <file>` ignores the `-f` patterns entirely — all nine waived hits on
# this tree came back as unwaived. It is not needed either: `-f` with a pattern file that is empty,
# or that holds a single empty line, contributes no matches under `-xF`, so both spellings of an
# absent registry already behave. Checked both by hand rather than reasoned about.
unwaived=$(printf '%s\n' "$hits" | grep -vxF -f <(printf '%s' "$waived_rows") || true)
stale_rows=$(printf '%s\n' "$waived_rows" | grep -vxF -f <(printf '%s' "$hits") || true)

bad=0
for h in $unwaived; do
  if [ "$bad" = 0 ]; then
    echo "dead-paths: a file outside memory/ names a path this repo DELETED. A reader who follows it"
    echo "dead-paths: finds nothing, and nothing else in the bar reds. Repoint it at what replaced the"
    echo "dead-paths: file, or add a row to $WAIVERS with the reason the name must stay."
  fi
  bad=$((bad+1))
  printf '  %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"
done
[ "$bad" = 0 ] || exit 1

# A waiver that no longer names a hit is a stale row: the carrier it excused is gone, and leaving it
# lets the NEXT one in silently under a pin that never fell.
stale=0
for w in $stale_rows; do
  [ "$stale" = 0 ] && echo "dead-paths: stale waiver(s) — the carrier they excuse is gone; delete the row:"
  stale=$((stale+1)); printf '  %s\n' "$w"
done
[ "$stale" = 0 ] || exit 1

echo "dead-paths: clean — $(printf '%s\n' "$needles" | grep -c .) derived needle(s), $waived_n declared waiver(s), no undeclared carrier"
