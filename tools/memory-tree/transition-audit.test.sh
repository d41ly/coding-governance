#!/usr/bin/env bash
# transition-audit.test.sh — the arms for hygiene check 25 and its commit-time carrier.
#
#   bash tools/memory-tree/transition-audit.test.sh     # "PASS (n assertions)" + exit 0 = good
#
# WHAT IT GRADES. `transition_audit.py` classifies MERGES by lineage, computes the delta of the
# shards-side parent, accounts each entry against a tree, and refuses. Every arm below builds a
# throwaway git repository, seeds this kit and its memory-recall sibling into it, writes a history
# whose shape is the question, and runs the real checker inside it. Nothing here re-implements the
# subject: a fixture that graded a re-implementation would grade the fixture.
#
# WHY IT IS A REPO-SUBJECT LEG AND NOT A HELD SELF-TEST. Its subject is this repository as much as
# it is the checker: one arm compares the tracked hook-named files under the hooks directory with
# `GOV_WIRING_HOOKS`, both ways, and that comparison goes stale with nobody editing the kit. So the
# leg's `subject` is `repo` and the suite itself is WITHHELD from adopters — an adopter's hook
# population is theirs, and this arm would red in their tree on arrival.
#
# WHAT IT DOES NOT GRADE, said out loud because a structural check reads as a semantic one. It never
# asserts the hygiene engine's OVERALL exit status over a fixture: a scratch tree is not a conforming
# memory tree and two dozen other checks have opinions about it. Where an arm needs the engine it
# greps for check 25's own line prefix, which is exactly the delegation being asserted. It does not
# grade the module's cost, and it does not reach the classes check 25 itself declares out of scope —
# a rebase or a squash that drops rows leaves no merge, and arm 6 pins that as absence rather than
# closing it.
#
# EVERY PATH IS DERIVED from this script's own location, never spelled: a hardcoded install prefix is
# wrong at every prefix but the one it assumed, which is the class this repo gates repo-wide.
#
# This file deliberately does NOT define `fail() {`: check-arms.py discovers any tracked *.sh that
# does and demands a sibling test for it, and a test-for-the-test is not a thing these arms need.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
# ASK GIT for the repo-relative prefix; never subtract one path string from another. Under MSYS one
# directory has two spellings and the strip silently does not strip.
KIT_MT="$(git -C "$(dirname "$0")" rev-parse --show-prefix)"; KIT_MT="${KIT_MT%/}"
[ -n "$KIT_MT" ] || { echo "FAIL cannot derive this kit's own directory"; exit 2; }
TOOL_ROOT="$(dirname "$KIT_MT")"
KIT_MR="$TOOL_ROOT/memory-recall"
KIT_LIB="$TOOL_ROOT/lib"
[ -f "$KIT_MR/extract.py" ] || { echo "FAIL the memory-recall sibling is not beside this kit at $KIT_MR, and check 25 keys every row through its grammar — there is nothing to grade"; exit 2; }
# shellcheck source=/dev/null
. "$KIT_LIB/resolve-python.sh"
PY=$(resolve_python) || { echo "FAIL no usable python launcher"; exit 2; }

FLOOR_ASSERTIONS=58

TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' EXIT
n=0; st=0
ok()  { n=$((n+1)); }
bad() { echo "FAIL $1"; st=1; n=$((n+1)); }
has() { printf '%s' "$1" | grep -qF -- "$2"; }

# ------------------------------------------------------------------------------ fixture machinery
# ONE seeded template, copied per fixture. A `git init` is one process and a kit copy is fifty file
# writes; doing both per arm is the cost this harness would otherwise be.
SEED="$TMP/seed"
mkdir -p "$SEED/tools" "$SEED/memory/backlog" "$SEED/memory/builds/aSeed" "$SEED/memory/project"
cp -r "$KIT_MT" "$SEED/tools/memory-tree"
cp -r "$KIT_MR" "$SEED/tools/memory-recall"
cp -r "$KIT_LIB" "$SEED/tools/lib"
rm -rf "$SEED/tools/memory-tree/__pycache__" "$SEED/tools/memory-recall/__pycache__"
printf '# the seed build\n' > "$SEED/memory/builds/aSeed/README.md"
printf '# decisions\n\n- TOOL-aSeed-9 - a decision\n' > "$SEED/memory/DECISIONS.md"

write_conf() { # $1 = repo dir, $2 = mode
  {
    printf 'MEMORY_ROOT=memory\n'
    printf 'DISCIPLINES="tooling"\n'
    printf 'FAMILIES="tooling:TOOL"\n'
    printf 'ROTATION_MODE="cut"\n'
    printf 'BACKLOG_MODE="%s"\n' "$2"
  } > "$1/.memory-tree.conf"
}

write_shard() { # $1 = repo dir, $2 = the text of row 1
  { printf '# TOOL backlog\n\n'
    printf -- '- TOOL-aSeed-1 \xc2\xb7 filed 2026-01-01 \xc2\xb7 %s\n' "$2"
    printf -- '- TOOL-aSeed-2 \xc2\xb7 filed 2026-01-02 \xc2\xb7 the second ask\n'
  } > "$1/memory/backlog/TOOL.md"
}

write_relocated() { # $1 = repo dir, $2 = slug, $3 = id, $4 = sha
  mkdir -p "$1/memory/builds/$2"
  { printf '# %s\n\n## Asks\n\n' "$2"
    printf '## Dispositions\n\n'
    printf -- '- RELOCATED \xc2\xb7 %s \xc2\xb7 by %s \xc2\xb7 kept: carried forward across the transition\n' "$3" "$4"
  } > "$1/memory/builds/$2/BACKLOG.md"
}

new_repo() { # $1 = repo dir — a shards-mode base commit with two rows
  cp -r "$SEED" "$1"
  git init -q -b main "$1"
  git -C "$1" config user.email arms@example.invalid
  git -C "$1" config user.name arms
  git -C "$1" config commit.gpgsign false
  git -C "$1" config core.autocrlf false
  git -C "$1" config core.hooksPath "$1/.nohooks"
  write_conf "$1" shards
  write_shard "$1" "the first ask"
  git -C "$1" add -A >/dev/null 2>&1
  git -C "$1" commit -qm base
}

flip_to_builds() { # $1 = repo dir — the commit that switches the default branch
  write_conf "$1" builds
  mkdir -p "$1/memory/builds/aFlip"
  { printf '# aFlip\n\n## Asks\n\n'
    printf -- '- TOOL-aFlip-1 \xc2\xb7 filed 2026-02-01 \xc2\xb7 an ask filed after the switch\n\n'
    printf '## Dispositions\n'
  } > "$1/memory/builds/aFlip/BACKLOG.md"
  git -C "$1" add -A >/dev/null 2>&1
  git -C "$1" commit -qm "flip to builds"
}

audit() { # $1 = repo dir, rest = argv — the real checker, inside the fixture
  local d="$1"; shift
  ( cd "$d" && "$PY" tools/memory-tree/transition_audit.py "$@" 2>&1 )
}
audit_rc() { # same, but the exit status
  local d="$1"; shift
  ( cd "$d" && "$PY" tools/memory-tree/transition_audit.py "$@" >/dev/null 2>&1 ); echo $?
}
engine() { # $1 = repo dir — the hygiene engine, inside the fixture
  ( cd "$1" && bash tools/memory-tree/check-memory-hygiene.sh 2>&1 )
}

# ====================================================================== F1 — straggler into builds
# The canonical shape: a branch still editing the authored shard is merged into a default branch
# that has already switched. The straggler's edit lands in a file the default branch no longer
# authors, so the merge resolves without a conflict either way.
F1="$TMP/f1"
new_repo "$F1"
git -C "$F1" checkout -q -b strag
write_shard "$F1" "the first ask, REWORDED by the straggler"
git -C "$F1" commit -qam "the straggler edits a row"
F1_STRAG=$(git -C "$F1" rev-parse HEAD)
git -C "$F1" checkout -q main
flip_to_builds "$F1"
git -C "$F1" merge -q --no-ff -m "merge the straggler" strag
F1_MERGE=$(git -C "$F1" rev-parse HEAD)

out=$(audit "$F1" --expect-builds)
rc=$(audit_rc "$F1" --expect-builds)
[ "$rc" = 1 ] || bad "AC1: an unaccounted transition did not exit 1 (rc=$rc)"; ok
has "$out" "$F1_MERGE" || bad "AC1: the refusal does not name the merge sha"; ok
has "$out" "TOOL-aSeed-1" || bad "AC1: the refusal does not name the lost id"; ok
has "$out" "$F1_STRAG" || bad "AC1: the refusal does not name the change commit"; ok
has "$out" "transitions examined 1" || bad "AC5: the liveness line does not report one examined transition"; ok

# The ENGINE carries it. Asserted by the check's own line prefix rather than by the engine's exit
# status: a scratch tree is not a conforming memory tree, and grading its overall verdict would
# grade every other check at the same time.
eout=$(engine "$F1")
has "$eout" "memory-hygiene: check 25 UNACCOUNTED" || bad "AC1: the hygiene engine does not carry check 25's refusal"; ok
has "$eout" "$F1_MERGE" || bad "AC1: the engine's check 25 line does not name the merge"; ok

# --- AC2 — accounting is EXACTLY ONE row, keyed on the id AND the sha ----------------------------
write_relocated "$F1" aFlip TOOL-aSeed-1 "$F1_STRAG"
git -C "$F1" add -A >/dev/null 2>&1; git -C "$F1" commit -qm "account for the relocation"
F1_OK=$(git -C "$F1" rev-parse HEAD)
[ "$(audit_rc "$F1" --expect-builds)" = 0 ] || bad "AC1: one RELOCATED row per entry did not account for it"; ok

write_relocated "$F1" aSecond TOOL-aSeed-1 "$F1_STRAG"
git -C "$F1" add -A >/dev/null 2>&1; git -C "$F1" commit -qm "a second provenance row for one entry"
dout=$(audit "$F1" --expect-builds)
[ "$(audit_rc "$F1" --expect-builds)" = 1 ] || bad "AC2: two RELOCATED rows for one entry did not refuse"; ok
{ has "$dout" "aFlip/BACKLOG.md" && has "$dout" "aSecond/BACKLOG.md"; } \
  || bad "AC2: the duplicate verdict does not name both files"; ok
git -C "$F1" rm -rq memory/builds/aSecond; git -C "$F1" commit -qm "drop the duplicate"

write_relocated "$F1" aFlip TOOL-aSeed-1 "0000000"
git -C "$F1" add -A >/dev/null 2>&1; git -C "$F1" commit -qm "a provenance row naming another commit"
[ "$(audit_rc "$F1" --expect-builds)" = 1 ] || bad "AC2: a RELOCATED row whose sha names another commit still accounted"; ok
git -C "$F1" revert --no-edit HEAD >/dev/null 2>&1
[ "$(audit_rc "$F1" --expect-builds)" = 0 ] || bad "AC2: reverting the mis-keyed provenance row did not restore the accounting"; ok

# --- AC9 — the cache holds the delta, and a foreign epoch is DETECTED ----------------------------
rm -rf "$F1/.git/transition-audit-cache"
audit "$F1" --report --expect-builds >/dev/null
c2=$(audit "$F1" --report --expect-builds)
has "$c2" "cache hits 1" || bad "AC9: the second run did not read the cached delta"; ok
cf=$(ls "$F1/.git/transition-audit-cache"/*.json 2>/dev/null | head -1)
[ -n "$cf" ] || bad "AC9: no cache file was written under the git dir"; ok
if [ -n "$cf" ]; then
  "$PY" -c "import json,sys; p=sys.argv[1]; d=json.load(open(p)); d['epoch']='foreign'; json.dump(d,open(p,'w'))" "$cf"
  c3=$(audit "$F1" --report --expect-builds)
  has "$c3" "cache recomputed 1 (foreign epoch)" || bad "AC9: a foreign-epoch cache entry was not reported as recomputed"; ok
  has "$c3" "cache hits 0" || bad "AC9: a foreign-epoch cache entry was still counted as a hit"; ok
fi

# --- AC7 — the pinned registry -------------------------------------------------------------------
pinout=$(audit "$F1" --pin --expect-builds)
has "$pinout" "$F1_MERGE accounted" || bad "AC7: --pin does not print a row for the unpinned transition"; ok
[ -f "$F1/memory/project/transition-audit.txt" ] && bad "AC7: --pin wrote the registry instead of printing it"; ok
printf '# pins\n0123456789abcdef0123456789abcdef01234567 accounted\n' > "$F1/memory/project/transition-audit.txt"
sout=$(audit "$F1" --expect-builds)
{ [ "$(audit_rc "$F1" --expect-builds)" = 1 ] && has "$sout" "STALE PIN"; } \
  || bad "AC7: a registry row naming a sha this history does not hold was not refused"; ok
printf '# pins\n%s accounted\n' "$F1_MERGE" > "$F1/memory/project/transition-audit.txt"
[ "$(audit_rc "$F1" --expect-builds)" = 0 ] || bad "AC7: a live pinned transition was refused"; ok
rm -f "$F1/memory/project/transition-audit.txt"

# --- AC13 — the dereference pin: a replace ref and a graft file cannot hide the merge -------------
git -C "$F1" replace --graft "$F1_MERGE" "$(git -C "$F1" rev-parse "$F1_MERGE^1")" >/dev/null
[ -n "$(git -C "$F1" replace -l)" ] || bad "AC13: the replace ref fixture was not created, so the pin went unexercised"; ok
rm -f "$F1/memory/builds/aFlip/BACKLOG.md"; rmdir "$F1/memory/builds/aFlip" 2>/dev/null
git -C "$F1" add -A >/dev/null 2>&1; git -C "$F1" commit -qm "drop the accounting again"
rout=$(audit "$F1" --expect-builds)
has "$rout" "$F1_MERGE" || bad "AC13: a replace ref re-parenting the merge hid it from the audit"; ok
printf '%s %s\n' "$F1_MERGE" "$(git -C "$F1" rev-parse "$F1_MERGE^1")" > "$TMP/grafts"
gout=$( cd "$F1" && GIT_GRAFT_FILE="$TMP/grafts" "$PY" tools/memory-tree/transition_audit.py --expect-builds 2>&1 )
has "$gout" "$F1_MERGE" || bad "AC13: an inherited GIT_GRAFT_FILE hid the merge from the audit"; ok
# THE POSITIVE CONTROL. A graft file that git ignores makes the arm above pass for the wrong
# reason, and grafts are deprecated, so the fixture proves it still re-parents before the pin
# is credited with resisting it.
greal=$( cd "$F1" && GIT_GRAFT_FILE="$TMP/grafts" git rev-list --parents -n1 "$F1_MERGE" 2>/dev/null | wc -w )
[ "$greal" = 2 ] || bad "AC13: the graft fixture does not re-parent the merge for git itself, so the pin arm asserts nothing (fields=$greal)"; ok
git -C "$F1" replace -d "$F1_MERGE" >/dev/null 2>&1

# --- AC12 — `--at` reads the NAMED tip's history and tree, never HEAD's ---------------------------
# Two commits whose trees differ in exactly their RELOCATED rows. Only that pair can tell an
# implementation bound to HEAD from one bound to the named tip, in either direction.
F1_BAD=$(git -C "$F1" rev-parse HEAD)
[ "$(audit_rc "$F1" --expect-builds)" = 1 ] \
  || bad "AC12: the fixture checked out at the unaccounted tip passed with no --at"; ok
[ "$(audit_rc "$F1" --at "$F1_OK" --expect-builds)" = 0 ] \
  || bad "AC12: --at over a tip whose tree carries the provenance rows still refused"; ok
git -C "$F1" checkout -q "$F1_OK"
[ "$(audit_rc "$F1" --at "$F1_BAD" --expect-builds)" = 1 ] \
  || bad "AC12: --at over an unaccounted tip passed because HEAD's tree accounted for it"; ok
git -C "$F1" checkout -q main
noflag=$(audit "$F1" --at "$F1_OK")
has "$noflag" "reader cross-check not run" || bad "AC12: --at without --expect-builds does not announce the skipped cross-check"; ok

# --- AC6 — the three DEAD PROBE refusals, each staged ---------------------------------------------
B="$TMP/f1broken"; cp -r "$F1" "$B"
"$PY" - "$B/tools/memory-tree/transition_audit.py" <<'PYEOF'
import io, sys
p = sys.argv[1]
s = io.open(p, encoding="utf-8", newline="").read()
old = "        return backlog.read_conf(conf).mode"
assert s.count(old) == 1
io.open(p, "w", encoding="utf-8", newline="").write(s.replace(old, '        return "shards"', 1))
PYEOF
cout=$(audit "$B" --expect-builds)
{ [ "$(audit_rc "$B" --expect-builds)" = 2 ] && has "$cout" "DEAD PROBE"; } \
  || bad "AC6: a conf reader that calls every blob shards did not refuse as a DEAD PROBE"; ok

D="$TMP/f1noboundary"; cp -r "$F1" "$D"
"$PY" - "$D/tools/memory-tree/transition_audit.py" <<'PYEOF'
import io, sys
p = sys.argv[1]
s = io.open(p, encoding="utf-8", newline="").read()
old = "    return boundaries, reaches"
assert s.count(old) == 1
io.open(p, "w", encoding="utf-8", newline="").write(s.replace(old, "    return set(), {}", 1))
PYEOF
bout=$(audit "$D" --expect-builds)
{ [ "$(audit_rc "$D" --expect-builds)" = 2 ] && has "$bout" "no mode boundary"; } \
  || bad "AC6: a boundary detector that answers nothing did not refuse as a DEAD PROBE"; ok

SH="$TMP/f1shallow"
git clone -q --depth 1 "file://$F1" "$SH" 2>/dev/null
if [ -d "$SH" ]; then
  shout=$(audit "$SH" --expect-builds)
  { [ "$(audit_rc "$SH" --expect-builds)" = 2 ] && has "$shout" "SHALLOW"; } \
    || bad "AC6: a shallow clone did not refuse as a DEAD PROBE"; ok
else
  bad "AC6: the shallow clone fixture could not be built, so the refusal went unexercised"; ok
fi

# --- AC15 — the memory-recall kit is a NAMED prerequisite, never a degraded mode -------------------
NR="$TMP/f1norecall"; cp -r "$F1" "$NR"; rm -rf "$NR/tools/memory-recall"
nout=$(audit "$NR" --expect-builds)
{ [ "$(audit_rc "$NR" --expect-builds)" = 1 ] && has "$nout" "memory-recall" \
  && has "$nout" "install the memory-recall kit" && has "$nout" "tools/memory-recall"; } \
  || bad "AC15: an absent memory-recall kit did not refuse by name with the path and the remedy"; ok

# ================================================================== F5 — a shards-mode tree is DARK
F5="$TMP/f5"; new_repo "$F5"
e5=$(engine "$F5")
has "$e5" "memory-hygiene: check 25 is DORMANT" || bad "AC5: a shards-mode tree does not announce that check 25 is dormant"; ok
printf '%s\n' "$e5" | grep -F 'memory-hygiene: check 25 ' | grep -qv 'is DORMANT' \
  && bad "AC5: a shards-mode tree printed a check 25 line other than the dormant announcement"; ok
rm -rf "$F5/tools/memory-recall"
[ "$(audit_rc "$F5")" = 0 ] || bad "AC15: a shards-mode tree with no memory-recall kit did not stay dormant at exit 0"; ok

# ============================================================ F2/F3/F4 — what IS and IS NOT a merge
F2="$TMP/f2"; new_repo "$F2"
git -C "$F2" checkout -q -b strag
write_shard "$F2" "the first ask, REWORDED by the straggler"
git -C "$F2" commit -qam "the straggler edits a row"
git -C "$F2" checkout -q main
flip_to_builds "$F2"
git -C "$F2" checkout -q strag
git -C "$F2" merge -q --no-ff -m "merge the default INTO the straggler" main
r2=$(audit "$F2" --report --expect-builds)
has "$r2" "transitions examined 1" || bad "AC3: merging the default into the straggler was not classified as a transition"; ok

F3="$TMP/f3"; new_repo "$F3"
git -C "$F3" checkout -q -b strag
write_shard "$F3" "the first ask, REWORDED by the straggler"
git -C "$F3" commit -qam "the straggler edits a row"
git -C "$F3" checkout -q main
flip_to_builds "$F3"
git -C "$F3" merge -q --squash strag >/dev/null 2>&1 || true
git -C "$F3" commit -qam "squash the straggler" >/dev/null 2>&1 || true
r3=$(audit "$F3" --report --expect-builds)
has "$r3" "transitions examined 0" || bad "AC3: a squashed straggler was classified as a transition"; ok

F4="$TMP/f4"; new_repo "$F4"
git -C "$F4" checkout -q -b strag
write_shard "$F4" "the first ask, REWORDED by the straggler"
git -C "$F4" commit -qam "the straggler edits a row"
git -C "$F4" checkout -q main
flip_to_builds "$F4"
git -C "$F4" checkout -q strag
git -C "$F4" rebase -q main >/dev/null 2>&1 || true
git -C "$F4" checkout -q main
git -C "$F4" merge -q --ff-only strag >/dev/null 2>&1 || true
r4=$(audit "$F4" --report --expect-builds)
has "$r4" "transitions examined 0" || bad "AC3: a rebased straggler was classified as a transition"; ok

# ====================================================== F6 — a LINEAR flip is not a DEAD PROBE
F6="$TMP/f6"; new_repo "$F6"
flip_to_builds "$F6"
l6=$(audit "$F6" --expect-builds)
{ [ "$(audit_rc "$F6" --expect-builds)" = 0 ] && has "$l6" "transitions examined 0"; } \
  || bad "AC6: a linear flip with no transition merge did not pass with a zero count"; ok

# =========================================== F7 — the criss-cross: EVERY merge base, never the first
# Two merge bases. The row version at `ours` equals one of them, so nobody lost anything and the
# delta must omit it — while a row `ours` changed after both bases is still its own.
F7="$TMP/f7"; new_repo "$F7"
git -C "$F7" checkout -q -b sideA
write_shard "$F7" "the first ask, changed on A"
git -C "$F7" commit -qam "A changes row 1"
git -C "$F7" checkout -q -b sideB main
git -C "$F7" commit -q --allow-empty -m "B changes nothing"
git -C "$F7" checkout -q sideA
git -C "$F7" merge -q --no-ff -m "A takes B" sideB
F7_A=$(git -C "$F7" rev-parse HEAD)
git -C "$F7" checkout -q sideB
git -C "$F7" merge -q --no-ff -m "B takes A" sideA 2>/dev/null || git -C "$F7" merge -q --no-ff -m "B takes A" "$F7_A"
F7_B=$(git -C "$F7" rev-parse HEAD)
xout=$( cd "$F7" && "$PY" - "$F7" "$F7_A" "$F7_B" <<'PYEOF'
import sys
sys.path.insert(0, "tools/memory-tree")
import transition_audit as TA
root, ours, theirs = sys.argv[1], sys.argv[2], sys.argv[3]
print(" ".join(sorted(e["id"] for e in TA.delta(ours, theirs, root=root))) or "(none)")
PYEOF
)
[ "$xout" = "(none)" ] || bad "AC4: a row equal to ONE merge base was reported as a delta entry ($xout)"; ok

# =========================================== F8 — rotation: the watched set is not the whole archive
# The straggler rotates its DECISION LOG and a FAMILY shard in one commit, and drops a row entirely.
# Only the family half is watched: a routine decision-log rotation must contribute nothing.
F8="$TMP/f8"; new_repo "$F8"
git -C "$F8" checkout -q -b strag
mkdir -p "$F8/memory/archive"
printf '# decisions, rotated\n\n- TOOL-aSeed-9 - a decision\n- TOOL-aSeed-8 - another decision\n' \
  > "$F8/memory/archive/DECISIONS.2026-01-05.md"
printf '# decisions\n' > "$F8/memory/DECISIONS.md"
{ printf '# TOOL backlog, rotated\n\n'
  printf -- '- TOOL-aSeed-2 \xc2\xb7 filed 2026-01-02 \xc2\xb7 the second ask, CLOSED on rotation\n'
} > "$F8/memory/archive/TOOL.2026-01-05.md"
{ printf '# TOOL backlog\n\n'
  printf -- '- TOOL-aSeed-1 \xc2\xb7 filed 2026-01-01 \xc2\xb7 the first ask\n'
} > "$F8/memory/backlog/TOOL.md"
git -C "$F8" add -A >/dev/null 2>&1
git -C "$F8" commit -qm "the straggler rotates its decision log and its shard"
git -C "$F8" checkout -q main
flip_to_builds "$F8"
git -C "$F8" merge -q --no-ff -m "merge the rotating straggler" strag
r8=$(audit "$F8" --report --expect-builds)
has "$r8" "TOOL-aSeed-9" && bad "AC4: an id anchored in a ROTATED DECISION LOG was reported as a lost backlog row"; ok
has "$r8" "TOOL-aSeed-2" || bad "AC4: a row rotated into a FAMILY-named archive with its text changed was not reported"; ok

F8B="$TMP/f8b"; new_repo "$F8B"
git -C "$F8B" checkout -q -b strag
{ printf '# TOOL backlog\n\n'
  printf -- '- TOOL-aSeed-1 \xc2\xb7 filed 2026-01-01 \xc2\xb7 the first ask\n'
} > "$F8B/memory/backlog/TOOL.md"
git -C "$F8B" commit -qam "the straggler deletes a row outright"
git -C "$F8B" checkout -q main
flip_to_builds "$F8B"
git -C "$F8B" merge -q --no-ff -m "merge the deleting straggler" strag
r8b=$(audit "$F8B" --report --expect-builds)
has "$r8b" "TOOL-aSeed-2 \xc2\xb7 removed" || has "$r8b" "TOOL-aSeed-2" \
  || bad "AC4: a row removed from the shard and absent from any archive was not reported"; ok
printf '%s' "$r8b" | grep -q "removed" || bad "AC4: the removal was not reported with the REMOVED kind"; ok

# ================================= F9 — A6: a version the OTHER side already held is not ours to own
# The straggler takes the default branch's own row change across by cherry-pick, so the merge base
# does NOT carry it and only the A6 clause can tell whose change it is. A fixture that MERGED the
# commit cannot arm this: the merge base would then be that commit and the version would match it.
F9="$TMP/f9"; new_repo "$F9"
F9_BASE=$(git -C "$F9" rev-parse HEAD)
write_shard "$F9" "the first ask, changed on the DEFAULT branch"
git -C "$F9" commit -qam "the default branch changes row 1"
F9_CX=$(git -C "$F9" rev-parse HEAD)
git -C "$F9" checkout -q -b strag "$F9_BASE"
git -C "$F9" cherry-pick -q "$F9_CX" >/dev/null 2>&1
{ printf '# TOOL backlog\n\n'
  printf -- '- TOOL-aSeed-1 \xc2\xb7 filed 2026-01-01 \xc2\xb7 the first ask, changed on the DEFAULT branch\n'
  printf -- '- TOOL-aSeed-2 \xc2\xb7 filed 2026-01-02 \xc2\xb7 the second ask, REWORDED by the straggler\n'
} > "$F9/memory/backlog/TOOL.md"
git -C "$F9" commit -qam "the straggler changes a row of its own"
git -C "$F9" checkout -q main
flip_to_builds "$F9"
git -C "$F9" merge -q --no-ff -m "merge the straggler" strag 2>/dev/null || {
  git -C "$F9" checkout -q --theirs memory/backlog/TOOL.md 2>/dev/null
  git -C "$F9" add -A >/dev/null 2>&1; git -C "$F9" commit -qm "merge the straggler" >/dev/null 2>&1; }
r9=$(audit "$F9" --report --expect-builds)
has "$r9" "TOOL-aSeed-2" || bad "AC14: the straggler's OWN row change was not reported"; ok
has "$r9" "TOOL-aSeed-1" && bad "AC14: a row whose version the default side already held was reported as the straggler's change"; ok

# ========================== F11 — the CALLABLES units 12 and 13 consume, before any merge exists
# `delta(ours, theirs)` must answer over two TIPS with no merge between them, because the relocation
# tools run before the merge is made and the pre-push body runs over a branch that may never be
# merged at all. Its answer must be the one `--report` gives for the merge of the same two commits
# once that merge exists, or the two callers are grading different things.
F11="$TMP/f11"; new_repo "$F11"
git -C "$F11" checkout -q -b strag
write_shard "$F11" "the first ask, REWORDED by the straggler"
git -C "$F11" commit -qam "the straggler edits a row"
F11_STRAG=$(git -C "$F11" rev-parse HEAD)
git -C "$F11" checkout -q main
flip_to_builds "$F11"
F11_FLIP=$(git -C "$F11" rev-parse HEAD)
before=$( cd "$F11" && "$PY" - "$F11" "$F11_STRAG" "$F11_FLIP" <<'PYEOF'
import sys
sys.path.insert(0, "tools/memory-tree")
import transition_audit as TA
root, ours, theirs = sys.argv[1], sys.argv[2], sys.argv[3]
for e in sorted(TA.delta(ours, theirs, root=root), key=lambda e: e["id"]):
    print(f"{e['id']}|{e['kind']}|{e['change']}")
PYEOF
)
[ -n "$before" ] || bad "AC11: delta() over two tips with no merge between them returned nothing"; ok
git -C "$F11" merge -q --no-ff -m "merge the straggler" strag
after=$(audit "$F11" --report --expect-builds | sed -n 's/^entry [0-9a-f]* \xc2\xb7 \([^ ]*\) \xc2\xb7 \([^ ]*\) \xc2\xb7 \([0-9a-f]*\) .*/\1|\2|\3/p' | LC_ALL=C sort)
[ "$before" = "$after" ] \
  || bad "AC11: delta() before the merge and --report after it disagree (before='$before' after='$after')"; ok

write_relocated "$F11" aFlip TOOL-aSeed-1 "$F11_STRAG"
git -C "$F11" add -A >/dev/null 2>&1; git -C "$F11" commit -qm "account for the relocation"
F11_OK=$(git -C "$F11" rev-parse HEAD)
F11_BAD=$(git -C "$F11" rev-parse HEAD^1)
acct() { # $1 = the tip to account against, with HEAD checked out at $2
  git -C "$F11" checkout -q "$2"
  ( cd "$F11" && "$PY" - "$F11" "$F11_STRAG" "$F11_FLIP" "$1" <<'PYEOF'
import sys
sys.path.insert(0, "tools/memory-tree")
import transition_audit as TA
root, ours, theirs, tip = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
entries = TA.delta(ours, theirs, root=root)
verdicts = TA.accounted(entries, tip, root=root)
print("all" if entries and all(v == "ok" for v in verdicts.values()) else "not-all")
PYEOF
)
}
[ "$(acct "$F11_OK" "$F11_BAD")" = all ] \
  || bad "AC11: accounted() over a tip carrying one RELOCATED row per entry did not account for them while HEAD lacked the rows"; ok
[ "$(acct "$F11_BAD" "$F11_OK")" = not-all ] \
  || bad "AC11: accounted() read HEAD's tree instead of the tip's — HEAD carried the rows and the tip did not"; ok
git -C "$F11" checkout -q main

# ================================================= F10 — the commit-msg carrier, both merge shapes
HOOK="$ROOT/.githooks/commit-msg"
if [ ! -f "$HOOK" ]; then
  bad "AC8: the tracked commit-msg hook is absent, so its arms went unexercised"; ok
else
  F10="$TMP/f10"; new_repo "$F10"
  mkdir -p "$F10/.ghooks"; cp "$HOOK" "$F10/.ghooks/commit-msg"; chmod +x "$F10/.ghooks/commit-msg"
  git -C "$F10" config core.hooksPath "$F10/.ghooks"
  git -C "$F10" checkout -q -b strag
  write_shard "$F10" "the first ask, REWORDED by the straggler"
  git -C "$F10" commit -qam "the straggler edits a row"
  git -C "$F10" checkout -q main
  flip_to_builds "$F10"
  # A NON-MERGE commit passes with no output at all.
  printf 'a note\n' > "$F10/memory/builds/aSeed/README.md"
  hout=$( cd "$F10" && git commit -qam "an ordinary commit" 2>&1 )
  [ -z "$hout" ] || bad "AC8: the hook printed something on an ordinary non-merge commit: $hout"; ok
  # The CLEAN merge, which fires pre-merge-commit with no MERGE_HEAD and then this hook with one.
  mout=$( cd "$F10" && git merge --no-ff -m "merge the straggler" strag 2>&1 ); mrc=$?
  { [ "$mrc" != 0 ] && has "$mout" "refuses this merge"; } \
    || bad "AC8: the commit-msg hook did not refuse a clean merge carrying an unaccounted row"; ok
  git -C "$F10" merge -q --abort 2>/dev/null || true
  # The CONFLICTED merge, concluded by `git commit`.
  write_shard "$F10" "the first ask, changed on the DEFAULT branch too"
  git -C "$F10" commit -qam "the default branch touches the same row"
  git -C "$F10" merge --no-ff -m "merge the straggler" strag >/dev/null 2>&1
  git -C "$F10" checkout -q --theirs memory/backlog/TOOL.md 2>/dev/null || true
  git -C "$F10" add memory/backlog/TOOL.md >/dev/null 2>&1
  cout2=$( cd "$F10" && git commit -m "conclude the conflicted merge" 2>&1 ); crc=$?
  { [ "$crc" != 0 ] && has "$cout2" "refuses this merge"; } \
    || bad "AC8: the commit-msg hook did not refuse a conflicted merge concluded by git commit"; ok
fi

# ==================================================== the REAL tree: this repo's own declarations
# AC16 — the tracked hook-named files and GOV_WIRING_HOOKS agree BOTH WAYS. A name left in the list
# after its file is deleted passes a one-directional comparison, and so does a hook added to the
# tree that nobody listed — which is the state check H was in before this unit.
WIRING=""
for c in "$ROOT/$TOOL_ROOT/check-wiring.sh" "$ROOT/check-wiring.sh"; do
  [ -f "$c" ] && { WIRING="$c"; break; }
done
if [ -z "$WIRING" ]; then
  bad "AC16: the wiring checker is not resolvable, so the hook-list comparison went unexercised"; ok
else
  # The CLOSED list of git hook names, from githooks(5). A tracked file under the hooks directory
  # whose name is not one of these is not a hook and is none of check H's business.
  HOOKNAMES="applypatch-msg pre-applypatch post-applypatch pre-commit pre-merge-commit prepare-commit-msg commit-msg post-commit pre-rebase post-checkout post-merge pre-push pre-receive update proc-receive post-receive post-update reference-transaction push-to-checkout pre-auto-gc post-rewrite sendemail-validate fsmonitor-watchman p4-changelist p4-prepare-changelist p4-post-changelist p4-pre-submit post-index-change"
  declared=$(sed -n 's/^GOV_WIRING_HOOKS="\(.*\)"$/\1/p' "$WIRING" | head -1)
  [ -n "$declared" ] || bad "AC16: GOV_WIRING_HOOKS is not readable from the wiring checker"; ok
  tracked=$(git ls-files -- '.githooks/*' | while IFS= read -r p; do
      b=${p##*/}
      case " $HOOKNAMES " in *" $b "*) printf '%s\n' "$b" ;; esac
    done | LC_ALL=C sort -u)
  [ -n "$tracked" ] || bad "AC16: no tracked file under the hooks directory carries a git hook name, so this comparison would pass by finding nothing"; ok
  missing=""
  for b in $tracked; do
    case " $declared " in *" $b "*) ;; *) missing="$missing $b" ;; esac
  done
  [ -z "$missing" ] || bad "AC16: a tracked git hook is absent from GOV_WIRING_HOOKS, so check H will never report it diverged:$missing"; ok
  extra=""
  for b in $declared; do
    printf '%s\n' "$tracked" | grep -qx "$b" || extra="$extra $b"
  done
  [ -z "$extra" ] || bad "AC16: GOV_WIRING_HOOKS names a hook this tree does not track, so the list outlived its file:$extra"; ok
fi

# AC10 — the DECLARED edge. selfcheck grades an edge only when one is PRESENT, so deleting it is
# invisible there; this arm is what makes the deletion red.
DESC="$ROOT/$KIT_MT/kit.toml"
if [ ! -f "$DESC" ]; then
  bad "AC10: this kit's own descriptor is not beside it, so the edge-presence arm went unexercised"; ok
else
  edgeout=$("$PY" - "$DESC" <<'PYEOF'
import sys, tomllib
d = tomllib.load(open(sys.argv[1], "rb"))
rows = [r for r in d.get("requires_if", [])
        if r.get("kit") == "memory-recall" and "BACKLOG_MODE" in (r.get("when_any_key_set") or [])]
print("present" if len(rows) == 1 else f"absent ({len(rows)})")
PYEOF
)
  [ "$edgeout" = present ] \
    || bad "AC10: this kit's descriptor declares no single requires_if edge to memory-recall on BACKLOG_MODE, so an adopter switching to builds mode has no declaration naming the prerequisite ($edgeout)"; ok
fi

# ---------------------------------------------------------------------------------------- verdict
if [ "$n" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "FAIL executed $n assertions, below the declared floor of $FLOOR_ASSERTIONS — a block of arms"
  echo "     is stranded past an exit, and a suite that reports success over half of itself is the"
  echo "     green-by-absence shape this floor exists to catch."
  st=1
fi
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
