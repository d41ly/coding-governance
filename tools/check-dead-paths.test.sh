#!/usr/bin/env bash
# check-dead-paths.test.sh — self-test for tools/check-dead-paths.sh.
#
#   bash tools/check-dead-paths.test.sh
#
# Exit 0 = every arm held · 1 = an arm failed · 2 = the harness could not set up.
#
# EVERY ARM IS A RED PROOF OR A NAMED GREEN. The gate under test is a scanner, and a scanner whose
# needle set silently empties passes by matching nothing — so the arms that matter most are the ones
# proving it REFUSES to be vacuous, not the ones proving it finds a planted hit.
#
# EVERY ARM ASSERTS A MESSAGE, never an exit code alone. Several different faults all exit 1 here —
# an unwaived hit, a stale waiver, an empty needle set, a missing sentinel — and an arm reading only
# `$?` cannot tell them apart, so it would report success while the gate failed for the wrong reason.
#
# THE FIXTURES ARE REAL GIT REPOS WITH REAL DELETION HISTORY, because the needle set is derived from
# `git log --diff-filter=D`. A fixture that only writes files exercises nothing: there is no such
# thing as a dead path in a repo that has never deleted one. Each fixture therefore commits a file,
# deletes it in a LATER commit, and only then plants the carrier — never `git mv`, which git records
# as a rename that `--diff-filter=D` never reports.
#
# NOTHING HERE TOUCHES THE REAL TREE. The gate `cd`s to its own git toplevel, so every arm runs it
# from inside the scratch repo it was built for.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
GATE_SRC="$ROOT/tools/check-dead-paths.sh"
[ -f "$GATE_SRC" ] || { echo "dead-paths.test: no gate at $GATE_SRC"; exit 2; }

FLOOR_ASSERTIONS=19
PASS=0
FAIL=0
ok()  { PASS=$((PASS+1)); }
bad() { FAIL=$((FAIL+1)); echo "  FAIL: $1"; }

TMPROOT=$(mktemp -d) || exit 2
trap 'rm -rf "$TMPROOT"' EXIT

# arm <label> <want-rc> <needle> -- <cmd...>
arm() {
  local label="$1" want="$2" needle="$3"; shift 4
  local out rc
  out=$("$@" 2>&1); rc=$?
  if [ "$rc" -ne "$want" ]; then
    bad "$label — wanted rc=$want got $rc: $(printf '%s' "$out" | head -3)"; return
  fi
  case "$out" in *"$needle"*) ok ;; *) bad "$label — rc was right but the message was not: $(printf '%s' "$out" | head -3)" ;; esac
}

# mkrepo <dir> — a repo whose HISTORY contains a deletion of the gate's frozen sentinel basename.
# The sentinel is gov's own deleted companion, so a fixture must delete that exact name for the
# derivation to anchor. The fixtures that exercise the anti-vacuity refusals are built inline instead,
# precisely because they must NOT satisfy the sentinel.
mkrepo() {
  local d="$1"; shift
  mkdir -p "$d/tools"
  ( cd "$d" && git init -q && git config core.autocrlf false \
      && git config user.email t@t && git config user.name t ) || return 1
  cp "$GATE_SRC" "$d/tools/check-dead-paths.sh"
  printf 'placeholder catalogue\n' > "$d/parallel-coding-governance.domain-rules.md"
  printf 'a live file\n' > "$d/README.md"
  ( cd "$d" && git add -A && git commit -qm seed )
  ( cd "$d" && git rm -q parallel-coding-governance.domain-rules.md && git commit -qm delete )
}

run() { ( cd "$1" && bash tools/check-dead-paths.sh "${2:---check}" ); }

# ONE repo carries every arm that needs the same HISTORY. `git init` costs seconds on Windows and
# eleven of them made this suite the slowest leg on the bar; the arms below differ in WORKING TREE,
# not in history, so they share one. `git add` (no commit) is enough — `git grep` with no rev reads
# the index and worktree, which is exactly the state the gate grades.
BASE="$TMPROOT/base"
mkrepo "$BASE" || exit 2
# reset_base <carrier-lines...> — restore the fixture to seeded state, then plant the given README
# body. Clears the waiver registry too, so no arm inherits the previous one's.
reset_base() {
  printf 'a live file\n' > "$BASE/README.md"
  rm -f "$BASE/tools/dead-path-waivers.txt"
  rm -rf "$BASE/memory"
  [ $# -gt 0 ] && printf '%s\n' "$@" >> "$BASE/README.md"
  ( cd "$BASE" && git add -A )
}

# ---- 1. the derivation ---------------------------------------------------------------------------
reset_base
arm "green: a repo with a deletion and no carrier is clean" 0 "no undeclared carrier" -- run "$BASE"
arm "the needle set names the deleted basename" 0 "parallel-coding-governance.domain-rules.md" -- run "$BASE" --needles
# THE TAIL IS THE HALF A FULL-BASENAME SCAN MISSES. Four of the eleven real carriers spelled only
# the tail, so this is not a refinement — it is most of the gate.
arm "the needle set also derives the distinctive TAIL" 0 "domain-rules.md" -- run "$BASE" --needles

# ---- 2. the hit branch ---------------------------------------------------------------------------
reset_base 'see parallel-coding-governance.domain-rules.md for the checklists'
arm "red: a carrier naming the deleted file in full" 1 "names a path this repo DELETED" -- run "$BASE"
arm "red: the message points at the carrier's own line" 1 "README.md:2" -- run "$BASE"

# The ABBREVIATED spelling — the form that defeated the first draft of this gate.
reset_base 'the checklists live in `.domain-rules.md` alongside'
arm "red: a carrier spelling only the TAIL" 1 "names a path this repo DELETED" -- run "$BASE"

# ---- 3. memory/ is out of scope ------------------------------------------------------------------
# A record naming a file deleted AFTER the record was written is correct, not stale.
reset_base
mkdir -p "$BASE/memory/builds/x"
printf 'the spec cited parallel-coding-governance.domain-rules.md at the time\n' > "$BASE/memory/builds/x/spec.md"
( cd "$BASE" && git add -A )
arm "green: an append-only record under memory/ is not a carrier" 0 "no undeclared carrier" -- run "$BASE"

# ---- 4. waivers — keyed by TEXT and an occurrence ORDINAL (TOOL-dHonouredPark-3) ------------------
# A row is `<path>\t<ordinal>\t<line-text>\t<reason>`. Tab-separated rows are unreadable written
# inline, so one helper writes them and the arms below read as what they assert.
wrow() { printf '%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4"; }
CARRIER='see parallel-coding-governance.domain-rules.md for the checklists'

reset_base "$CARRIER"
{ printf '# waivers\n'; wrow README.md 1 "$CARRIER" 'deliberate, migration prose'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "green: a declared waiver silences its own hit" 0 "1 declared waiver(s)" -- run "$BASE"

# THE ARM THE WHOLE RE-KEY EXISTS FOR. Under line keying this redded, twice in one build, for a
# change that had nothing to do with the waiver.
reset_base 'an unrelated line inserted above the carrier' "$CARRIER"
{ printf '# waivers\n'; wrow README.md 1 "$CARRIER" 'deliberate, migration prose'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "green: a DIFFERENT line above the carrier does not unpin the waiver" 0 "1 declared waiver(s)" -- run "$BASE"

# A waiver whose carrier is gone must red, or the list stops shrinking.
reset_base
{ printf '# waivers\n'; wrow README.md 1 "$CARRIER" 'the carrier this excuses was already removed'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "red: a waiver whose carrier is gone is stale" 1 "stale waiver(s)" -- run "$BASE"

# REWORDING is the one drift the text key does NOT survive, and that is intended: a reworded line is
# a line whose waiver should be re-read. The message is the UNWAIVED one, not the stale one, because
# the unwaived report comes first and exits — asserted as it behaves rather than as it reads better.
reset_base 'see parallel-coding-governance.domain-rules.md for the checklist'
{ printf '# waivers\n'; wrow README.md 1 "$CARRIER" 'deliberate, migration prose'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "red: a REWORDED carrier is no longer waived" 1 "names a path this repo DELETED" -- run "$BASE"

# A waiver must not silence a DIFFERENT line in the same file.
reset_base 'filler' 'see parallel-coding-governance.domain-rules.md here'
{ printf '# waivers\n'; wrow README.md 1 "$CARRIER" 'waives text that is not here'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "red: a waiver whose text names no line does not cover this hit" 1 "names a path this repo DELETED" -- run "$BASE"

# N IDENTICAL CARRIERS NEED N ROWS. Waiving one occurrence leaves the others unwaived, and an
# unwaived hit reds. This is the case the ordinal exists for and the case rev-2 of the spec got
# wrong, asserting that one ordinal-bearing row could clear it.
reset_base "$CARRIER" "$CARRIER"
{ printf '# waivers\n'; wrow README.md 1 "$CARRIER" 'first occurrence only'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "red: two identical carriers, one row — the second is unwaived" 1 "names a path this repo DELETED" -- run "$BASE"

reset_base "$CARRIER" "$CARRIER"
{ printf '# waivers\n'; wrow README.md 1 "$CARRIER" 'first occurrence'; wrow README.md 2 "$CARRIER" 'second occurrence, its own reason'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "green: two identical carriers, two rows at ordinals 1 and 2" 0 "2 declared waiver(s)" -- run "$BASE"

# THE RESIDUAL, armed rather than argued away. An IDENTICAL line above a waived carrier DOES move the
# ordinal — the one drift the new key keeps, named in the registry header as the case it exists for.
reset_base "$CARRIER" "$CARRIER"
{ printf '# waivers\n'; wrow README.md 2 "$CARRIER" 'pinned to the second occurrence'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "red: an IDENTICAL line above a waived carrier renumbers it" 1 "names a path this repo DELETED" -- run "$BASE"

# A MALFORMED ordinal is its own refusal, distinct from a stale row: line numbers were unique by
# construction and an occurrence index is not, so the property has to be asserted rather than
# inherited.
for bad in 0 zero '' -1; do
  reset_base "$CARRIER"
  { printf '# waivers\n'; wrow README.md "$bad" "$CARRIER" 'ordinal is not a positive integer'; } > "$BASE/tools/dead-path-waivers.txt"
  ( cd "$BASE" && git add -A )
  arm "red: ordinal [$bad] is MALFORMED, not stale" 1 "MALFORMED waiver row" -- run "$BASE"
done

# A row naming a file that is not there resolves to nothing and is stale BY THAT REASON. Without this
# the branch is unreachable in the ordinary case, because a gone file usually leaves its carrier
# behind as an unwaived hit and that report exits first.
reset_base
{ printf '# waivers\n'; wrow NO-SUCH-FILE.md 1 'text that is not a carrier anywhere' 'names a file that is gone'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "red: a row naming an absent file is stale, with its own reason" 1 "file is gone" -- run "$BASE"

# THE `awk -v` TRAP, armed on the shape that bit the real registry. A -v assignment expands backslash
# sequences, so a carrier holding a literal \n compares unequal to itself and the row reads stale for
# a reason nobody can see. ENVIRON does not expand, and this arm is what proves it.
BSLASH='printf "# ARCH \\n" and parallel-coding-governance.domain-rules.md'
reset_base "$BSLASH"
{ printf '# waivers\n'; wrow README.md 1 "$BSLASH" 'carrier text holds a literal backslash-n'; } > "$BASE/tools/dead-path-waivers.txt"
( cd "$BASE" && git add -A )
arm "green: a carrier holding a literal backslash-n still resolves" 0 "1 declared waiver(s)" -- run "$BASE"

# ---- 5. anti-vacuity — the arms that matter ------------------------------------------------------
# A repo that has never deleted anything must REFUSE, not report clean. This is the shape the gate
# exists to avoid being: a selector matching nothing prints nothing, and nothing is what a pass
# prints (memory/gotchas/vacuous-selector-empty-population.md).
NODEL="$TMPROOT/nodel"
mkdir -p "$NODEL/tools"
( cd "$NODEL" && git init -q && git config core.autocrlf false \
    && git config user.email t@t && git config user.name t )
cp "$GATE_SRC" "$NODEL/tools/check-dead-paths.sh"
printf 'nothing was ever deleted here\n' > "$NODEL/README.md"
( cd "$NODEL" && git add -A && git commit -qm seed )
arm "refuse: a repo with no deletion history is not a clean verdict" 2 "the derivation is broken, not the tree clean" -- run "$NODEL"

# A repo that HAS deleted things, but not the frozen sentinel, must red on the sentinel — this is the
# arm that catches a derivation which silently stops finding gov's own deleted companions.
SENT="$TMPROOT/sentinel"
mkdir -p "$SENT/tools"
( cd "$SENT" && git init -q && git config core.autocrlf false \
    && git config user.email t@t && git config user.name t )
cp "$GATE_SRC" "$SENT/tools/check-dead-paths.sh"
printf 'x\n' > "$SENT/unrelated.md"; printf 'y\n' > "$SENT/README.md"
( cd "$SENT" && git add -A && git commit -qm seed )
( cd "$SENT" && git rm -q unrelated.md && git commit -qm del )
arm "red: the frozen sentinel missing from the derived set" 1 "frozen sentinel" -- run "$SENT"
arm "red: and it says the derivation broke, not that the tree is clean" 1 "DERIVATION is broken" -- run "$SENT"

# A repo that HAS deletions but where every deleted basename was re-added leaves the needle set empty
# AFTER filtering, which is a different branch from "git reports no deletion at all". It fired by
# accident while this suite was being written and nothing pinned it, which is how a branch goes quiet.
# Exit 1 (the gate ran and found its own inputs wrong), not 2 (this repo cannot be graded at all).
EMPTY="$TMPROOT/emptyneedles"
mkdir -p "$EMPTY/tools/sub"
( cd "$EMPTY" && git init -q && git config core.autocrlf false \
    && git config user.email t@t && git config user.name t )
cp "$GATE_SRC" "$EMPTY/tools/check-dead-paths.sh"
printf 'x\n' > "$EMPTY/moved.md"; printf 'y\n' > "$EMPTY/README.md"
( cd "$EMPTY" && git add -A && git commit -qm seed )
( cd "$EMPTY" && git rm -q moved.md && git commit -qm remove )
printf 'x\n' > "$EMPTY/tools/sub/moved.md"
( cd "$EMPTY" && git add -A && git commit -qm readd )
arm "red: every deleted basename re-added leaves an EMPTY needle set" 1 "needle set is EMPTY" -- run "$EMPTY"

# ---- 6. a MOVED name is NOT dead -----------------------------------------------------------------
# Deleting a file from one directory and re-adding it in another leaves the NAME resolvable, and a
# gate that reds on it would forbid every move. Asserted POSITIVELY — a carrier naming the moved file
# is planted and the gate must still return its named clean verdict — because an arm that merely
# checks the name is absent from `--needles` passes just as well when the whole derivation is broken.
#
# The moved file is deliberately NOT the frozen sentinel: re-adding that name anywhere would make the
# sentinel resolve again and red the derivation arm, which is the gate working as designed. So the
# fixture keeps the sentinel deleted and moves a third file.
#
# DELETED AND RE-ADDED IN SEPARATE COMMITS, never `git mv`. A rename inside one commit is recorded as
# R and `--diff-filter=D` never sees it, so a `git mv` fixture exercises NOTHING here — it passes
# whether or not the tracked-suffix filter exists. Measured: the first draft of this arm used `git mv`
# and was green against a gate whose filter had never run.
mkrepo "$TMPROOT/readd" || exit 2
mkdir -p "$TMPROOT/readd/docs"
printf 'moved, not deleted\n' > "$TMPROOT/readd/moved-note.md"
( cd "$TMPROOT/readd" && git add -A && git commit -qm addmoved )
( cd "$TMPROOT/readd" && git rm -q moved-note.md && git commit -qm removemoved )
printf 'moved, not deleted\n' > "$TMPROOT/readd/docs/moved-note.md"
( cd "$TMPROOT/readd" && git add -A && git commit -qm readdelsewhere )
printf 'see moved-note.md for the note\n' >> "$TMPROOT/readd/README.md"
( cd "$TMPROOT/readd" && git add -A && git commit -qm carrier )
arm "green: a deleted name re-added elsewhere still resolves" 0 "no undeclared carrier" -- run "$TMPROOT/readd"
arm "and the sentinel still anchors that repo's derivation" 0 "parallel-coding-governance.domain-rules.md" -- run "$TMPROOT/readd" --needles

# ---- 6b. the GENERIC TAIL, which is the only thing the suffix filter actually guards -------------
# The `gone` step already drops a deleted BASENAME the tree still carries, so that filter is not what
# the awk suffix pass is for. Its job is the derived TAIL: deleting `legacy.kit.toml` yields the tail
# `kit.toml`, and this tree carries a dozen live files by that name — unfiltered, every one of their
# mentions becomes a violation and the gate is unusable. Verified by disabling the pass: this arm is
# the one that reds, and the re-add arm above stays green either way.
mkrepo "$TMPROOT/gentail" || exit 2
mkdir -p "$TMPROOT/gentail/tools/live"
printf 'a live descriptor\n' > "$TMPROOT/gentail/tools/live/kit.toml"
printf 'a legacy descriptor\n' > "$TMPROOT/gentail/legacy.kit.toml"
( cd "$TMPROOT/gentail" && git add -A && git commit -qm seedtail )
( cd "$TMPROOT/gentail" && git rm -q legacy.kit.toml && git commit -qm droplegacy )
printf 'every entry declares a kit.toml beside it\n' >> "$TMPROOT/gentail/README.md"
( cd "$TMPROOT/gentail" && git add -A && git commit -qm mention )
arm "green: a derived tail that still names a tracked file is NOT a needle" 0 "no undeclared carrier" -- run "$TMPROOT/gentail"
arm "and the full deleted basename is still derived alongside it" 0 "legacy.kit.toml" -- run "$TMPROOT/gentail" --needles

# ---- 7. usage ------------------------------------------------------------------------------------
arm "an unknown verb is a usage refusal" 2 "usage:" -- run "$BASE" --frobnicate

if [ "$FAIL" -ne 0 ]; then
  echo "check-dead-paths.test FAILED — $FAIL of $((PASS+FAIL)) arm(s)"
  exit 1
fi
if [ "$PASS" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "check-dead-paths.test FAILED — $PASS arm(s) executed, below the floor of $FLOOR_ASSERTIONS;"
  echo "check-dead-paths.test a block of arms is stranded past an exit rather than passing"
  exit 1
fi
echo "PASS ($PASS assertions)"
