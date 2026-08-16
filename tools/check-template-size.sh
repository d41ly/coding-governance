#!/usr/bin/env bash
# check-template-size.sh — size gate for the governance playbook template.
# The template is the operational ruleset an agent reads every session; it must stay lean.
# Prose that doesn't affect instruction clarity still belongs in a companion
# (parallel-coding-governance.customize.md / .domain-rules.md) rather than the template. The ceiling
# moved 32 KiB -> 48 KiB on owner order (TOOL-aSiftedPlaybook-1); the PREFERENCE for externalizing
# did not move with it, and the high-water ratchet below is what prices growth now that the ceiling
# is no longer doing it.
#
#   tools/check-template-size.sh            # gate the tracked template
#   MAX_BYTES=49152 tools/check-template-size.sh <file>   # override target / limit
#   tools/check-template-size.sh --bump [<file> [<limit> [<record>]]]   # re-record the high-water
#
# Exit 0 = within budget (prints one line). Exit 1 = over budget. Exit 2 = file missing.
# Exit 3 = the high-water record exists but this subject's row is not a number.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || ROOT=.

# `--bump` is a FLAG, not a positional, because the three positionals below are already spoken for
# (subject, limit, record path) and a mode sharing a slot with a path is how one of them silently
# becomes the other. Strip it wherever it appears, then read the positionals from what is left.
BUMP=0
ARGS=""
for a in "$@"; do
  if [ "$a" = "--bump" ]; then BUMP=1; else ARGS="$ARGS $a"; fi
done
# shellcheck disable=SC2086
set -- $ARGS

FILE=${1:-"$ROOT/parallel-coding-governance.template.md"}
# The limit, in precedence order: positional $2, then the environment, then the playbook's own 48 KiB.
# The POSITIONAL exists because a gate leg cannot set an environment variable: `run-gates.sh` execs
# its argument vector directly with no shell, and the canary pins argv[0] to a known interpreter, so
# neither `env MAX_BYTES=… bash …` nor a variable assignment is a legal leg. This one line is what
# lets a second file ride this script instead of a sibling script being written for it.
MAX_BYTES=${2:-${MAX_BYTES:-49152}}   # 48 KiB default — the ceiling for the playbook template.
                                      # Raised from 32768 by owner order; prefer externalizing to
                                      # spending it, and expect the ratchet below to price growth.

# The high-water record, resolved the same three ways MAX_BYTES is — positional $3, then the
# environment, then the tracked default — because a gate leg cannot set an environment variable and
# the self-test must point the gate at a scratch copy without writing the tracked one.
HIGHWATER=${3:-${HIGHWATER:-"$ROOT/tools/template-size-highwater.txt"}}

[ -f "$FILE" ] || { echo "TEMPLATE-SIZE env ERROR — file not found: $FILE"; exit 2; }
# Measure LF-NORMALIZED bytes (strip CR) so the gate is checkout-independent — a Windows autocrlf
# smudge to CRLF must not inflate the count and spuriously fail the limit.
bytes=$(tr -d '\r' < "$FILE" | wc -c | tr -d '[:space:]')
name=$(basename "$FILE")

if [ "$bytes" -gt "$MAX_BYTES" ]; then
  over=$((bytes - MAX_BYTES))
  echo "TEMPLATE-SIZE FAILED — $name is $bytes bytes, $over over the $MAX_BYTES-byte limit."
  echo "  Trim non-instructional prose, or move an activity-scoped section to"
  echo "  parallel-coding-governance.domain-rules.md (leaving a §-stub pointer), per the v2.3 pattern."
  echo "  Raising the limit is an OWNER decision recorded in memory/DECISIONS.md, never a fix for"
  echo "  the edit that hit it — and this message is shared with the kickoff engine at its own limit."
  exit 1
fi

# --- the high-water ratchet -------------------------------------------------------------------
# Advisory: it never changes the exit code. Rows are `<path>\t<bytes>`, KEYED BY MEASURED FILE,
# because two consumers ride this script ~14 KB apart and one shared number can only ever serve one
# of them. Absent record = no ratchet plus an explicit line; a non-numeric row is a NAMED failure,
# never a `set -u` explosion at the numeric comparison below.
# The key is REPO-RELATIVE, and both sides are normalized through the same `cd && pwd` before the
# prefix is stripped. `git rev-parse --show-toplevel` answers `C:/projects/...` on this fleet while
# `pwd` answers `/c/projects/...`, so comparing the two raw never matches and every key lands as a
# machine-absolute path — which would make a TRACKED record differ per machine and per worktree.
# A subject outside the repo (the self-test's scratch files) keeps its absolute path, which is
# correct: it has no repo-relative name to have.
root_p=$(cd "$ROOT" 2>/dev/null && pwd) || root_p=$ROOT
key=$(cd "$(dirname "$FILE")" && pwd)/$name
case "$key" in
  "$root_p"/*) key=${key#"$root_p"/} ;;
esac
recorded=""
if [ -f "$HIGHWATER" ]; then
  recorded=$(awk -F'\t' -v k="$key" '$1 == k { print $2 }' "$HIGHWATER" | tr -d '[:space:]')
fi

if [ "$BUMP" = 1 ]; then
  tmp="${HIGHWATER}.tmp.$$"
  if [ -f "$HIGHWATER" ]; then
    awk -F'\t' -v k="$key" '$1 != k' "$HIGHWATER" > "$tmp"
  else
    : > "$tmp"
  fi
  printf '%s\t%d\n' "$key" "$bytes" >> "$tmp"
  LC_ALL=C sort -o "$tmp" "$tmp"
  mv "$tmp" "$HIGHWATER"
  if [ -n "$recorded" ]; then
    echo "TEMPLATE-SIZE BUMP — $key high-water $recorded -> $bytes ($((bytes - recorded)) bytes)."
  else
    echo "TEMPLATE-SIZE BUMP — $key high-water recorded at $bytes (no prior row)."
  fi
elif [ ! -f "$HIGHWATER" ]; then
  echo "TEMPLATE-SIZE no-ratchet — no high-water record at $HIGHWATER; growth is unpriced."
elif [ -z "$recorded" ]; then
  echo "TEMPLATE-SIZE no-ratchet — $key has no row in $HIGHWATER; growth is unpriced."
elif ! printf '%s' "$recorded" | grep -qE '^[0-9]+$'; then
  echo "TEMPLATE-SIZE RECORD ERROR — $key's high-water in $HIGHWATER is not a number: '$recorded'."
  exit 3
elif [ "$bytes" -gt "$recorded" ]; then
  echo "TEMPLATE-SIZE WARN — $name grew past its recorded high-water: $recorded -> $bytes (+$((bytes - recorded))). Advisory only; re-record with --bump when the growth is intended."
fi

printf 'template-size OK — %s: %d / %d bytes (%d under, %.1f%%)\n' "$name" "$bytes" "$MAX_BYTES" "$((MAX_BYTES - bytes))" "$(awk "BEGIN{print $bytes/$MAX_BYTES*100}")"
