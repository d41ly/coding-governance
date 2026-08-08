#!/usr/bin/env bash
# Self-test for check-verdict-epoch.sh. Every arm runs in a throwaway repo with a synthetic engine,
# because the arm that matters — "the engine moved and the version did not" — cannot be staged in
# this tree without leaving the merge bar red.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
GATE="$HERE/check-verdict-epoch.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
fails=0
# THE EXIT CODE IS PART OF THE ASSERTION. The first cut captured `rc` and only printed it, so the
# message and the verdict were never checked together: mutating the gate's FAILED branch from
# `exit 1` to `exit 0` left all ten arms green and printed PASS, while run-gates.sh judges a leg
# purely by its exit status. A gate that has been turned into a printer is exactly the shape this
# repo exists to catch, and this harness could not see it happen to its own gate.
arm() { # label · want-rc · expected-substring · dir · [base]
  local label=$1 wantrc=$2 want=$3 dir=$4 base=${5:-}
  local out rc bad=0
  out=$(cd "$dir" && bash "$GATE" $base 2>&1); rc=$?
  [ "$rc" = "$wantrc" ] || bad=1
  case "$out" in *"$want"*) ;; *) bad=1 ;; esac
  if [ "$bad" = 0 ]; then printf 'arm ok    %s\n' "$label"; return; fi
  fails=$((fails+1))
  printf 'arm FAIL  %s — wanted rc=%s + %s, got rc=%s\n' "$label" "$wantrc" "$want" "$rc"
  printf '%s\n' "$out" | sed 's/^/      /'
}

engine() { # $1=dir $2=version $3=extra-body-line
  mkdir -p "$1/tools/memory-tree"
  { printf '#!/usr/bin/env bash\n'
    printf 'KIT_MEMORY_TREE_VERSION=%s   # gov:kit memory-tree@%s — engine identity\n' "$2" "$2"
    printf '# a comment line that never changes behaviour\n'
    printf 'echo hygiene\n'
    [ -n "$3" ] && printf '%s\n' "$3"
  } > "$1/tools/memory-tree/check-memory-hygiene.sh"
}

newrepo() { # $1=name -> echoes the dir
  local d="$TMP/$1"
  mkdir -p "$d"
  ( cd "$d" && git init -q -b main . && git config user.email t@t.test && git config user.name t \
    && git config commit.gpgsign false ) >/dev/null 2>&1
  printf '%s' "$d"
}

# ---- 1. the defect, reproduced: the engine's behaviour moves, the constant does not ----------------
A=$(newrepo moved); engine "$A" 1.5 ""
( cd "$A" && git add -A && git commit -qm base --no-verify ) >/dev/null
BASE_A=$(cd "$A" && git rev-parse HEAD)
engine "$A" 1.5 "echo an extra behaviour-bearing line"
( cd "$A" && git add -A && git commit -qm change --no-verify ) >/dev/null
arm 'an engine change with a still constant FAILS' 1 'is 1.5 at BOTH ends' "$A" "$BASE_A"
arm '...and the remedy names all three files' 1 'kit-dogfood-parity.test.sh --render' "$A" "$BASE_A"

# ---- 2. the same range with the version bumped is clean ------------------------------------------
B=$(newrepo bumped); engine "$B" 1.5 ""
( cd "$B" && git add -A && git commit -qm base --no-verify ) >/dev/null
BASE_B=$(cd "$B" && git rev-parse HEAD)
engine "$B" 1.6 "echo an extra behaviour-bearing line"
( cd "$B" && git add -A && git commit -qm bump --no-verify ) >/dev/null
arm 'the same change WITH a bump is clean' 0 'the version moved 1.5 -> 1.6' "$B" "$BASE_B"

# ---- 3. a COMMENT-only change does not demand a bump ----------------------------------------------
# Without this the gate would demand a version bump for editing prose, and the next person would
# start bumping reflexively — which makes the constant meaningless in the other direction.
C=$(newrepo comment); engine "$C" 1.5 ""
( cd "$C" && git add -A && git commit -qm base --no-verify ) >/dev/null
BASE_C=$(cd "$C" && git rev-parse HEAD)
printf '# one more comment, and a blank line follows\n\n' >> "$C/tools/memory-tree/check-memory-hygiene.sh"
( cd "$C" && git add -A && git commit -qm prose --no-verify ) >/dev/null
arm 'a comment-only change needs no bump' 0 'behaviour-bearing lines are unchanged' "$C" "$BASE_C"

# ---- 4. an INDENTED comment counts as a comment; an indented statement does not -------------------
D=$(newrepo indent); engine "$D" 1.5 ""
( cd "$D" && git add -A && git commit -qm base --no-verify ) >/dev/null
BASE_D=$(cd "$D" && git rev-parse HEAD)
printf '    # an indented comment\n' >> "$D/tools/memory-tree/check-memory-hygiene.sh"
( cd "$D" && git add -A && git commit -qm indented --no-verify ) >/dev/null
arm 'an indented comment is still a comment' 0 'behaviour-bearing lines are unchanged' "$D" "$BASE_D"
printf '    echo indented statement\n' >> "$D/tools/memory-tree/check-memory-hygiene.sh"
( cd "$D" && git add -A && git commit -qm stmt --no-verify ) >/dev/null
arm '...and an indented STATEMENT is not' 1 'is 1.5 at BOTH ends' "$D" "$BASE_D"

# ---- 5. the misconfigured cases are NAMED, never silently green ----------------------------------
E=$(newrepo noengine)
( cd "$E" && printf 'x\n' > README.md && git add -A && git commit -qm base --no-verify ) >/dev/null
arm 'a missing engine is a named failure' 2 'is missing' "$E"
# A repo with no `main` at all — a fresh clone of a differently-named default, or a detached probe.
# The skip must SAY it skipped: silence here is indistinguishable from "the constant is fine", which
# is the exact failure this gate exists for.
F="$TMP/nomain"; mkdir -p "$F"
( cd "$F" && git init -q -b work . && git config user.email t@t.test && git config user.name t   && git config commit.gpgsign false ) >/dev/null 2>&1
engine "$F" 1.5 ""
( cd "$F" && git add -A && git commit -qm base --no-verify ) >/dev/null
arm 'an unresolvable base is a REFUSAL, not a pass' 1 'no mainline base' "$F"
arm 'a bogus base is a named failure' 2 'is not a commit in this repo' "$A" deadbeefdeadbeef

# ---- 6. this repo, right now --------------------------------------------------------------------
# The live tree must be clean, and it must be clean because the constant MOVED — not because nothing
# changed. Asserting the message discriminates the two.
# `verdict-epoch:` prefixes EVERY message this gate emits, failures included — the first cut
# asserted that and could not fail while its own comment claimed it discriminated. The live tree must
# be clean BECAUSE the constant moved, which is a different sentence from "clean".
arm 'the live tree is clean because the version MOVED' 0 'the version moved' "$HERE/../.."

if [ "$fails" = 0 ]; then echo "PASS — check-verdict-epoch: all arms held"; exit 0; fi
echo "FAIL — $fails arm(s) failed"
exit 1
