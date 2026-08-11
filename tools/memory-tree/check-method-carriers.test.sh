#!/usr/bin/env bash
# check-method-carriers.test.sh — the self-test for the method-carrier gate.
#
#   bash tools/memory-tree/check-method-carriers.test.sh   # "PASS (…assertions)" + exit 0 = good
#
# Every arm runs against a SCRATCH repo, never this tree: the leg reads `git ls-files`, so a fixture
# built in place would either see gov's real population or need this repo mutated to fail. The green
# control comes FIRST — a leg that reds on everything arms every branch and checks nothing.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
LEG="$HERE/check-method-carriers.sh"
TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' EXIT
n=0; st=0
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }

seed() { # dir -> a git repo with the kit, a conf, a memory tree and ONE declared carrier
  rm -rf "$1"; mkdir -p "$1/tools/memory-tree" "$1/memory/project" "$1/memory/guides"
  cp "$LEG" "$1/tools/memory-tree/"
  ( cd "$1" && git init -q -b main . && git config user.email t@t.test && git config user.name t )
  printf 'MEMORY_ROOT=memory\n' > "$1/.memory-tree.conf"
  printf '# the method\n' > "$1/memory/guides/BUILD-METHOD.md"
  printf 'See memory/guides/BUILD-METHOD.md for the build method.\n' > "$1/POINTER.md"
  printf '# method-carriers\nPOINTER.md \xc2\xb7 the one declared carrier\n' > "$1/memory/project/method-carriers.txt"
  ( cd "$1" && git add -A >/dev/null 2>&1 )
}
run() { ( cd "$1" && bash tools/memory-tree/check-method-carriers.sh 2>&1 ); }

R="$TMP/r"

# ---- THE GREEN CONTROL. Without it every red arm below proves only that the leg can complain.
seed "$R"
out=$(run "$R"); rc=$?
same "a conforming tree exits 0" "$rc" "0"
hit "$out" "1 carrier(s), all declared and pointing"

# ---- check 1: an ABSENT registry is a refusal, not an empty set. This is the arm that keeps the
# ---- whole leg from passing vacuously on a tree that never scaffolded one.
seed "$R"; rm -f "$R/memory/project/method-carriers.txt"; ( cd "$R" && git add -A >/dev/null 2>&1 )
out=$(run "$R"); rc=$?
same "an absent registry exits 1" "$rc" "1"
hit "$out" ", and an absent registry is not an empty one — scaffold it with 'bash"

# ---- check 2: an EMPTY population is a refusal. If nothing points at the method any more it has
# ---- been unwired, which is louder drift than any undeclared carrier — and it is the shape that
# ---- makes every other arm vacuously true.
seed "$R"; rm -f "$R/POINTER.md"
printf '# method-carriers\n' > "$R/memory/project/method-carriers.txt"
( cd "$R" && git add -A >/dev/null 2>&1 )
out=$(run "$R"); rc=$?
same "an empty population exits 1" "$rc" "1"
hit "$out" "at all, so either the method has been unwired or this selector is mis-segmented — an empty population is not a clean one"

# ---- check 3: an UNDECLARED carrier. The drift this leg exists to catch.
seed "$R"
printf 'Also see memory/guides/BUILD-METHOD.md here.\n' > "$R/SNEAKY.md"
( cd "$R" && git add -A >/dev/null 2>&1 )
out=$(run "$R"); rc=$?
same "an undeclared carrier exits 1" "$rc" "1"
hit "$out" ", so nobody decided whether it points at the method or restates it"
hit "$out" "SNEAKY.md"

# ---- check 4, both directions: a row whose file is GONE, and a row whose file stopped pointing.
seed "$R"
printf '# method-carriers\nPOINTER.md \xc2\xb7 ok\nVANISHED.md \xc2\xb7 never existed\n' > "$R/memory/project/method-carriers.txt"
( cd "$R" && git add -A >/dev/null 2>&1 )
out=$(run "$R"); rc=$?
same "a row for a missing file exits 1" "$rc" "1"
hit "$out" "a declared carrier no longer exists, so its row guards nothing"

seed "$R"
printf 'this file no longer mentions the method\n' > "$R/POINTER.md"
printf 'See memory/guides/BUILD-METHOD.md.\n' > "$R/OTHER.md"
printf '# method-carriers\nPOINTER.md \xc2\xb7 stale\nOTHER.md \xc2\xb7 real\n' > "$R/memory/project/method-carriers.txt"
( cd "$R" && git add -A >/dev/null 2>&1 )
out=$(run "$R"); rc=$?
same "a stale row exits 1" "$rc" "1"
hit "$out" ", so its row is stale and would mask the next real one"

# ---- check 5: a carrier that COPIED a section rather than pointing at one.
seed "$R"
printf 'See memory/guides/BUILD-METHOD.md.\n\n## M3 — Forks\n\nRatify the most feature-rich option.\n' > "$R/POINTER.md"
( cd "$R" && git add -A >/dev/null 2>&1 )
out=$(run "$R"); rc=$?
same "a copied section exits 1" "$rc" "1"
hit "$out" "a carrier holds a '## M<n>' heading, the method's own section grammar and the shape a COPY takes rather than a pointer"

# ---- The exclusions are real, not decorative: a *.test.sh mentioning the method must NOT red, or
# ---- this very file would red the leg it tests. Same for the memory tree's own records.
seed "$R"
printf 'fixture mentioning memory/guides/BUILD-METHOD.md on purpose\n' > "$R/tools/memory-tree/some.test.sh"
printf 'a spec discussing memory/guides/BUILD-METHOD.md at length\n' > "$R/memory/builds-note.md"
( cd "$R" && git add -A >/dev/null 2>&1 )
out=$(run "$R"); rc=$?
same "a test fixture and a memory record are excluded" "$rc" "0"

[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
