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
  # POSITIONAL, not an env var. The gate stopped reading `$WAIVERS` because an ambient one greens
  # the bar with no diff; this suite is the reason the knob exists at all, so it uses the shape the
  # gate actually ships rather than a private back door.
  out=$(cd "$R" && bash "$GATE" waivers.txt 2>&1); rc=$?
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

# ---- SCAN INTEGRITY (H1). A filename holding a SPACE was split by the old batched `xargs grep`
# ---- into fragments that were never opened, and the gate reported a file count taken from the
# ---- LIST rather than from what grep read -- a clean verdict over a file nobody looked at.
mk space
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/Design Notes.md"
run
ck "a filename with a SPACE is scanned, not split"  '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "Design Notes.md"'

# ---- The count must be what grep OPENED. Two files in, two reported.
mk counted
printf '# a\n' > "$R/A.md"; printf '# b\n' > "$R/B.md"; rm -f "$R/README.md"
run
ck "the reported count is the files actually scanned" 'printf "%s" "$out" | grep -q "2 markdown file(s) scanned"'

# ---- SINGLE-FILE POPULATION (H1). `grep` prints no path for a one-file argv unless -H is forced,
# ---- so the remedy said "point at the file" while naming none. A fresh adopter tree IS this case.
mk lone
rm -f "$R/README.md"
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/ONLY.md"
run
ck "a single-file population still names its file"  '[ "$rc" = 1 ] && printf "%s" "$out" | grep -qE "ONLY\.md:[0-9]+:"'

# ---- MEASURED CARRIER SHAPES (H2). Every one of these was live in this corpus while the gate
# ---- reported it clean. They are frozen as fixtures because a pattern written from a pattern is
# ---- what certified them green; a pattern written from the measured population is what caught
# ---- them. A shape that stops matching reds HERE, not in a review six weeks later.
for _shape in \
  'A review spawns at most 5 agents TOTAL.' \
  'CONSOLIDATE before you fan out: at most 5 verify agents TOTAL (batch grows).' \
  'the ≤5 cap is enforced at the Workflow tool-call' \
  'the raw-primitive ban + the ≤5-verifier arity rule' \
  'Route ALL Workflow fan-out through cap-5 helpers.' \
  'CONCURRENCY ≤ 5, ALWAYS — the #1 rate-limit lever.' \
  ; do
  mk shape
  printf '# rules\n\n%s\n' "$_shape" > "$R/GUIDE.md"
  run
  ck "measured carrier shape is caught: $_shape" '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "GUIDE.md"'
done

# ---- The false positive that narrowing REMOVED, frozen so a future widening cannot bring it back.
# ---- `agents?-[0-9]+` matched the node-registry hostname `agent-0`; the reversed form is `cap-N` only.
mk hostname
printf '# nodes\n\n| `c` | agent-0 @ `DESKTOP-8BKM8GN` | `origin` |\n' > "$R/GUIDE.md"
run
ck "a node hostname like agent-0 is NOT a bound"    '[ "$rc" = 0 ]'

# ---- WAIVER KEYS ON TEXT, NOT PATH (M2). A row reading `docs/` waived an entire subtree, because
# ---- the row was matched against the whole `<path>:<line>:<text>` hit line by a registry whose own
# ---- contract says it never keys on a path.
mk pathwaiver
mkdir -p "$R/docs"
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/docs/A.md"
printf '# rules\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/docs/B.md"
printf 'docs/\ta path fragment must not waive a subtree\n' > "$R/waivers.txt"
run
ck "a path-fragment row does NOT waive its subtree" '[ "$rc" = 1 ] && printf "%s" "$out" | grep -q "docs/A.md"'
ck "...and that path-only row reds as STALE"        'printf "%s" "$out" | grep -q "matches nothing"'

# ---- MEMORY_ROOT IS READ (M3). A relocated tree's records must still be excluded, or the gate
# ---- reds an adopter's entire committed history on the day they install it.
mk relocated
mkdir -p "$R/docs/mem/builds/tOne"
printf 'MEMORY_ROOT=docs/mem\n' > "$R/.memory-tree.conf"
printf '# past\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/docs/mem/builds/tOne/README.md"
run
ck "a relocated MEMORY_ROOT's records are excluded" '[ "$rc" = 0 ]'

# ---- ...and the default still holds when no conf declares one.
mk defaultroot
printf '# past\n\nA review spawns at most 5 agents TOTAL.\n' > "$R/memory/builds/tOne/README.md"
run
ck "with no conf, memory/ is still the frozen root" '[ "$rc" = 0 ]'

# ---- PARITY-OWNED EXCLUSION IS NOT A HOLE. The playbook is excluded because check-playbook-parity.sh
# ---- BINDS its digits; if those pairs go, the exclusion silently becomes an unwatched file.
mk hole
printf '# rules\n\nRoute fan-out through cap-5 helpers.\n' > "$R/parallel-coding-governance.template.md"
mkdir -p "$R/tools"
printf 'lens-array bound~$TEMPLATE~sed -n s/x/[0-9]/p~tools/hooks/agent-cap.js~sed -n s/y/z/p\n' > "$R/tools/check-playbook-parity.sh"
run
ck "the playbook is excluded while a digit pair binds it" '[ "$rc" = 0 ]'
printf '# no pairs left\n' > "$R/tools/check-playbook-parity.sh"
run
ck "...and REFUSES once those pairs are gone"       '[ "$rc" = 2 ] && printf "%s" "$out" | grep -q "become a hole"'


FLOOR_ASSERTIONS=24
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
