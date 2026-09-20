#!/usr/bin/env bash
# **Serves:** journal TOOL-aQuenchedHarness-7
#
# THE DIFFERENTIAL CHECK behind the comment in `tools/unattended/lib-unattended.sh`'s `id_in`. That
# comment claims the grep spelling and the pure-bash spelling are equivalent on a multi-line
# haystack, because a newline is itself a member of the negated class the anchors alternate with.
# A claim of that shape is obviously true and occasionally false, so it is checked rather than
# asserted, and the check is kept so a later reader can re-run it instead of re-reasoning it.
#
#   bash memory/builds/aQuenchedHarness/build/2026-09-07-build-TOOL-aQuenchedHarness-7-id-in-equivalence.sh
#
# Result on node `a`, 2026-09-07: 17 of 17 cases agree.
# Differential check: the grep spelling of id_in against the pure-bash one, over the cases that
# distinguish them. The claim being tested is that per-LINE anchors (grep) and per-STRING anchors
# (bash) agree here, because a newline is itself a member of the negated class the anchors alternate
# with. A claim like that is exactly the kind that is obviously true and occasionally false.
set -u

check_rows_old() { printf '%s\n' "$1" | grep -E "(^|[^A-Za-z0-9-])$2([^A-Za-z0-9-]|\$)" || true; }
check_in_old()   { [ -n "$(check_rows_old "$1" "$2")" ]; }
check_in_new()   { [[ $1 =~ (^|[^A-Za-z0-9-])"$2"([^A-Za-z0-9-]|$) ]]; }

n=0; bad=0
check() { # label · haystack · id
  n=$((n+1))
  check_in_old "$2" "$3"; local o=$?
  check_in_new "$2" "$3"; local w=$?
  if [ "$o" = "$w" ]; then
    printf 'ok   %-58s (both %s)\n' "$1" "$o"
  else
    bad=1
    printf 'nope %-58s grep=%s bash=%s\n' "$1" "$o" "$w"
  fi
}

ID=TOOL-aQuenchedHarness-1

check "the id alone"                       "$ID"                            "$ID"
check "the id at line start, text after"   "$ID did a thing"                "$ID"
check "the id at line end"                 "build($ID)"                     "$ID"
check "the id mid-sentence"                "closing $ID now"                "$ID"
check "the -1/-10 trap: -10 must NOT match -1" "closing ${ID}0 now"         "$ID"
check "a hyphenated suffix must not match" "closing $ID-extra now"          "$ID"
check "absent entirely"                    "nothing to see"                 "$ID"
check "MULTILINE, id on the FIRST line"    "$ID first
second line"                                                                "$ID"
check "MULTILINE, id on the LAST line"     "first line
$ID"                                                                        "$ID"
check "MULTILINE, id alone on a MIDDLE line" "first
$ID
third"                                                                      "$ID"
check "MULTILINE, only a -10 on a middle line" "first
${ID}0
third"                                                                      "$ID"
check "the id as the whole of a middle line, no trailing text" "a
$ID
b"                                                                          "$ID"
check "trailing newline in the haystack"   "$ID
"                                                                           "$ID"
check "leading newline in the haystack"    "
$ID"                                                                        "$ID"
check "id followed by a tab"               "$(printf '%s\t x' "$ID")"       "$ID"
check "id preceded by a slash"             "memory/$ID"                     "$ID"
# THE DECOY ID IS BUILT AT RUNTIME, never written as a literal. A record citing an id no spec
# defines creates it as an ORPHAN, and the derived roster then keeps it alive -- so a test
# vector that needs a plausible-but-absent id has to assemble one. Same reason the
# aCollapsedScan equivalence harness builds every vector from parts.
DECOY=$(printf 'TOOL-a%s-1' Other)
check "a DIFFERENT id present, this one absent" "closing $DECOY now" "$ID"

echo
[ "$bad" = 0 ] && echo "PASS ($n cases, the two spellings agree)" || echo "FAILED ($n cases)"
exit "$bad"
