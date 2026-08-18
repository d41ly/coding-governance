#!/usr/bin/env bash
# Self-test for check-agent-cap-restatement.sh — TOOL-aDeclaredBound-5.
#
# The gate's whole job is to NAME a bare fan-out number in live prose, so every arm here is about
# whether it can still fire. Its two waiver mechanisms are separate — a PATH PREFIX for frozen trees
# and MATCHED TEXT for live exceptions — and each gets its own red, green and stale arm, because a
# text-keyed waiver written for a frozen record would silence every live carrier sharing the
# sentence, which is the reason the two are not one registry.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
GATE="$HERE/check-agent-cap-restatement.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
st=0; n=0

mk() {   # $1 = tree name; builds a repo whose markdown the gate will scan
  R="$TMP/$1"; mkdir -p "$R/memory/builds/tOne" "$R/memory/backlog" "$R/tools"
  ( cd "$R" && git init -q . && git config user.email t@t.test && git config user.name t \
      && git config core.autocrlf false )
  printf '# doc\n' > "$R/README.md"
  : > "$R/waivers.txt"
}
run() {  # runs the gate inside $R with $R/waivers.txt; sets $out and $rc
  ( cd "$R" && git add -A >/dev/null 2>&1 && git commit -q -m f --no-verify >/dev/null 2>&1 || true )
  out=$(cd "$R" && WAIVERS=waivers.txt bash "$GATE" 2>&1); rc=$?
}
ck() { n=$((n+1)); eval "$2" || { echo "FAIL $1"; st=1; }; }

# ---- RED: a live carrier asserting a bare bound is named.
mk red
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/GUIDE.md"
run
ck "a bare bound in live prose is NAMED"            '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "GUIDE.md"'

# ---- GREEN CONTROL: a digit near a bound word with NO fan-out noun stays silent. This is the real
# ---- sentence from the kickoff engine — "report ≤5 lines" — which an earlier pattern DID flag.
mk green
printf '# rules\n\nStep 1 — Orient (ONE batched command; report ≤5 lines).\n' > "$R/GUIDE.md"
run
ck "a bound with no fan-out noun stays silent"      '[ "$rc" = 0 ]'

# ---- POINTER: the fixed form — no digit, names the resolver — is silent.
mk pointed
printf '# rules\n\nA review spawns at most the total `tools/hooks/agent-cap.js` resolves.\n' > "$R/GUIDE.md"
run
ck "a pointer with no digit is silent"              '[ "$rc" = 0 ]'

# ---- FROZEN PREFIX: the identical sentence under a frozen tree is excluded by PATH, and the live
# ---- copy sharing that sentence is still named. One fixture, both halves — which is what proves the
# ---- exclusion is a prefix rather than a text match.
mk frozen
printf '# past\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/memory/builds/tOne/README.md"
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/GUIDE.md"
run
ck "a frozen-tree copy is excluded by prefix"       '! printf "%s" "$out" | grep -q "memory/builds"'
ck "...while the live copy sharing its sentence is still named" 'printf "%s" "$out" | grep -q "GUIDE.md"'

# ---- TEXT WAIVER: a live exception is excused by its matched text.
mk waived
printf '# rules\n\nMeasured: at most 5 agents TOTAL in that run.\n' > "$R/GUIDE.md"
printf 'at most 5 agents TOTAL in that run\ta measurement of one run, not the enforced rule\n' > "$R/waivers.txt"
run
ck "a text-keyed waiver excuses its hit"            '[ "$rc" = 0 ]'

# ---- STALE WAIVER: a row whose text is gone reds, because a waiver outliving its hit widens the gate.
mk stale
printf '# rules\n\nnothing to see.\n' > "$R/GUIDE.md"
printf 'at most 5 agents TOTAL in that run\tthe hit this excused is gone\n' > "$R/waivers.txt"
run
ck "a waiver matching nothing reds as STALE"        '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "matches nothing"'

# ---- VACUITY: an empty markdown population is a refusal, never a green. A scanner that passes by
# ---- finding nothing is this repo's own named class.
mk empty
rm -f "$R/README.md"
run
ck "an empty population REFUSES rather than passing" '[ "$rc" = 2 ]'

n=$((n+1))
FLOOR_ASSERTIONS=9
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
