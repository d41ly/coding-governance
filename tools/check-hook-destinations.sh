#!/usr/bin/env bash
# check-hook-destinations.sh — every hook path a fragment DECLARES, and every hook destination an
# adopter script WRITES, must resolve to a destination some kit.toml rule actually ships.
#
#   bash tools/check-hook-destinations.sh
#
# WHY THIS EXISTS, and it is not hypothetical. TOOL-dRetiredFork-14 withdrew the `.claude/hooks/`
# destinations for three hooks. Two of the three had their path supplied by a committed FRAGMENT
# rather than by the engine default, and `adopt-memory-recall.sh --with-hook` copied a fourth back
# into `.claude/hooks/` on every run. So the unit written to stop a silent unwiring produced two
# fragments and one installer pointing at a path that had stopped shipping — the exact failure its
# own section 5 called the highest risk in the build. TOOL-dRetiredFork-21.
#
# WHAT THIS DOES NOT CHECK. It does not verify that a settings.json anywhere is wired, that the hook
# FIRES, or that an adopter's installed copy matches gov's. `check-wiring.sh` owns the first, the
# hook's own suite the second, and the parity arms the third. This gate answers one question: does
# every declared hook path name something a descriptor ships.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "hook-dest: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
st=0

# shellcheck source=/dev/null
. tools/lib/resolve-python.sh
PY="$(resolve_python)" || { echo "hook-dest: no usable python — refusing rather than skipping"; exit 2; }

FRAGS=$(git ls-files '*.fragment.json' 2>/dev/null)

# AC5 — AN EMPTY POPULATION IS A REFUSAL. A gate that found no fragments prints the same zero as a
# gate over a clean tree, and this repo has a catalogue entry for exactly that shape. The fragments
# are tracked and this file ships beside them, so zero means the selector broke, not that the tree
# is tidy.
if [ -z "$FRAGS" ]; then
  echo "hook-dest: REFUSING — no *.fragment.json is tracked, so this gate has no subject."
  echo "           A population of zero is a broken selector, not a clean tree."
  exit 1
fi

n=$(printf '%s\n' "$FRAGS" | grep -c .)

# The declared destinations, from the descriptors themselves — never a list typed here. A gate that
# carried its own copy of the shipped set would agree with itself and not with the deployer.
DESTS=$("$PY" - <<'PYEOF'
import pathlib, sys
sys.path.insert(0, "tools/govkit")
import govkit
root = pathlib.Path(".").resolve()
reg = govkit.load_toml(root / "tools" / "govkit" / "registry.toml")
out = set()
for eid, (d, _p) in govkit.read_descriptors(root, reg, govkit.Report()).items():
    for row in govkit.resolve_entry(root, d, govkit.canonical_ctx(eid))["survivors"]:
        dst = row.get("dest") or row.get("dst") or row.get("to")
        if isinstance(dst, str):
            out.add(dst)
        elif isinstance(dst, (list, tuple)):
            out.update(x for x in dst if isinstance(x, str))
print("\n".join(sorted(out)))
PYEOF
) || { echo "hook-dest: could not resolve the descriptors — refusing"; exit 2; }

[ -n "$DESTS" ] || { echo "hook-dest: REFUSING — the descriptors resolved NO destinations at all"; exit 1; }

echo "hook-dest: $n fragment(s) against $(printf '%s\n' "$DESTS" | grep -c .) declared destination(s)"

# ---- arm 1: every fragment's hook_path resolves to a declared destination -------------------------
for f in $FRAGS; do
  hp=$("$PY" -c 'import json,sys;print(json.load(open(sys.argv[1],encoding="utf-8")).get("hook_path",""))' "$f" 2>/dev/null)
  if [ -z "$hp" ]; then
    echo "hook-dest: FAIL $f declares no hook_path — a fragment with no destination cannot be wired"
    st=1
    continue
  fi
  # `{kit}` expands against THE FRAGMENT'S OWN LOCATION, two directories up, which is the same rule
  # settings-merge.py and check-wiring.sh use. Three readers of one token have to agree or the
  # writer wires a path the checkers cannot find.
  kitpfx=$(dirname "$(dirname "$f")"); [ "$kitpfx" = "." ] && kitpfx=""
  resolved=$(printf '%s' "$hp" | sed "s|{kit}/|${kitpfx:+$kitpfx/}|g")
  if printf '%s\n' "$DESTS" | grep -qxF -- "$resolved"; then
    echo "hook-dest: ok   $f -> $resolved"
  else
    echo "hook-dest: FAIL $f declares hook_path '$hp' -> '$resolved', which NO kit.toml rule ships."
    echo "           A fragment naming a path no descriptor delivers is a wiring hole: the merge"
    echo "           writes the command, the file never arrives, and every matching tool call runs"
    echo "           node against nothing."
    st=1
  fi
done

# ---- arm 2: no adopter script installs a hook into a destination nothing declares -----------------
# The fragment half above would have passed the whole time `adopt-memory-recall.sh` was re-creating
# `.claude/hooks/recall-opened.js`, because that installer never reads a fragment. A gate over
# declarations alone cannot see an installer, which is why this arm quantifies over the scripts.
ADOPTERS=$(git ls-files 'tools/*/adopt-*.sh' 2>/dev/null)
if [ -z "$ADOPTERS" ]; then
  echo "hook-dest: REFUSING — no adopter script is tracked, so arm 2 has no subject"
  exit 1
fi
for a in $ADOPTERS; do
  # a WRITE into a hooks directory: cp/install/mv naming a path under some */hooks/
  hits=$(grep -nE '(cp|install|mv)[^|;&]*\.claude/hooks/' "$a" 2>/dev/null || true)
  if [ -n "$hits" ]; then
    echo "hook-dest: FAIL $a installs a hook into .claude/hooks/, which no kit.toml rule ships:"
    printf '%s\n' "$hits" | sed 's/^/           /'
    echo "           gov withdrew that destination; an installer that re-creates it hands the"
    echo "           adopter back the duplicate and a stale instruction naming it."
    st=1
  fi
done
[ "$st" = 0 ] && echo "hook-dest: clean — every declared hook path resolves, and no adopter writes an undeclared one"
exit $st
