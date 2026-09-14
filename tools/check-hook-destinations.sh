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
#
# HOW A PATH IS RESOLVED, and by whom. This gate does NOT expand `{kit}` or `{here}` itself. It asks
# the two readers that decide the value — `check-wiring.sh --resolve-fragment` and
# `settings-merge.py --resolve-fragment` — and REFUSES when they disagree, so the writer cannot wire
# a path the checker cannot find. A third derivation here would be a third answer to one question,
# and it is exactly what this file used to carry. TOOL-aReplayedCard-2.
#
# A `{here}` FRAGMENT IS JUDGED AT ITS ADOPTER PATH. `{here}` is the fragment's own directory, and
# it exists for a `kind = "flat"` kit: its engine ships to `{prefix}/<file>`, so the in-tree path
# (`skills/session-kickoff/manifest-check.sh`) and the shipped path (`tools/manifest-check.sh` under
# the canonical prefix) DIFFER BY DESIGN, and comparing the in-tree spelling against the declared
# set would red every correct flat-kit fragment. So the fragment's directory must be the `home` of
# at least one flat descriptor — else the fragment ships from nowhere and the gate refuses naming
# the directory — and `{prefix}/<path relative to that directory>` is compared against the WHOLE
# declared destination set, both spellings printed. A `{kit}` fragment is compared at its in-tree
# resolution as before, because a directory-shaped kit ships its tree under `{kit}` unchanged.
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

# The canonical prefix the destinations above were resolved under, and every `kind = "flat"` home
# — both from the deployer, never typed here. The flat-home set is what decides whether a `{here}`
# fragment ships from anywhere at all.
FLAT=$("$PY" - <<'PYEOF'
import pathlib, sys
sys.path.insert(0, "tools/govkit")
import govkit
root = pathlib.Path(".").resolve()
reg = govkit.load_toml(root / "tools" / "govkit" / "registry.toml")
print(govkit.canonical_ctx("hook-dest")["prefix"])
homes = set()
for eid, (d, _p) in govkit.read_descriptors(root, reg, govkit.Report()).items():
    if d.get("kind") == "flat" and d.get("home"):
        homes.add(d["home"].rstrip("/"))
print("\n".join(sorted(homes)))
PYEOF
) || { echo "hook-dest: could not read the flat-kit homes — refusing"; exit 2; }
PFX=$(printf '%s\n' "$FLAT" | head -1)
FLAT_HOMES=$(printf '%s\n' "$FLAT" | tail -n +2 | grep . || true)
[ -n "$PFX" ] || { echo "hook-dest: REFUSING — the deployer names no canonical prefix"; exit 1; }
# A ZERO here is a broken selector, not a tree with no flat kits: this repo's own kickoff engine is
# one, and the arm below would otherwise refuse every `{here}` fragment for a reason that is false.
[ -n "$FLAT_HOMES" ] || { echo "hook-dest: REFUSING — the descriptors declare NO kind=flat home, so no {here} fragment could be judged"; exit 1; }

echo "hook-dest: $n fragment(s) against $(printf '%s\n' "$DESTS" | grep -c .) declared destination(s), $(printf '%s\n' "$FLAT_HOMES" | grep -c .) flat home(s), prefix $PFX"

# The two readers whose value this gate asserts. Both are asked per fragment, below.
CW="tools/check-wiring.sh"; SM="tools/settings-merge.py"
for r in "$CW" "$SM"; do
  [ -f "$r" ] || { echo "hook-dest: REFUSING — $r is not here, and this gate reads its answer rather than deriving one"; exit 2; }
done

# ---- arm 1: every fragment's hook_path resolves to a declared destination -------------------------
# ---- and the two readers agree on what it resolves to (the parity arm) ---------------------------
for f in $FRAGS; do
  hp=$("$PY" -c 'import json,sys;print(json.load(open(sys.argv[1],encoding="utf-8")).get("hook_path",""))' "$f" 2>/dev/null)
  if [ -z "$hp" ]; then
    echo "hook-dest: FAIL $f declares no hook_path — a fragment with no destination cannot be wired"
    st=1
    continue
  fi
  a=$(bash "$CW" --resolve-fragment "$f" 2>&1); ra=$?
  b=$("$PY" "$SM" --resolve-fragment "$f" 2>&1); rb=$?
  if [ "$ra" != 0 ] || [ "$rb" != 0 ]; then
    echo "hook-dest: FAIL $f — a reader refused it: check-wiring rc=$ra ($a) · settings-merge rc=$rb ($b)"
    st=1
    continue
  fi
  if [ "$a" != "$b" ]; then
    echo "hook-dest: FAIL $f — the two readers DISAGREE: check-wiring resolves '$a', settings-merge '$b'."
    echo "           The writer would wire one path and the checker look for another; a fragment"
    echo "           token has one meaning or the wiring check cannot see what the merge wrote."
    st=1
    continue
  fi
  resolved=$a
  case "$hp" in
    *"{here}"*)
      dir=$(dirname "$f")
      if ! printf '%s\n' "$FLAT_HOMES" | grep -qxF -- "$dir"; then
        echo "hook-dest: FAIL $f is {here}-shaped but its directory '$dir' is the home of NO kind=flat descriptor,"
        echo "           so nothing ships it beside its engine and '$resolved' arrives nowhere. A {here}"
        echo "           fragment belongs beside the flat kit's engine (flat homes: $(printf '%s\n' "$FLAT_HOMES" | paste -sd, -))."
        st=1
        continue
      fi
      adopter="$PFX/${resolved#"$dir"/}"
      if printf '%s\n' "$DESTS" | grep -qxF -- "$adopter"; then
        echo "hook-dest: ok   $f -> $resolved in the tree, ships as $adopter"
      else
        echo "hook-dest: FAIL $f declares hook_path '$hp' -> '$resolved' in the tree, which would ship as"
        echo "           '$adopter' — and NO kit.toml rule delivers that. A flat kit's fragment is judged at"
        echo "           its adopter path, and this one names a file the kit does not ship beside it."
        st=1
      fi
      ;;
    *)
      if printf '%s\n' "$DESTS" | grep -qxF -- "$resolved"; then
        echo "hook-dest: ok   $f -> $resolved"
      else
        echo "hook-dest: FAIL $f declares hook_path '$hp' -> '$resolved', which NO kit.toml rule ships."
        echo "           A fragment naming a path no descriptor delivers is a wiring hole: the merge"
        echo "           writes the command, the file never arrives, and every matching tool call runs"
        echo "           the interpreter against nothing."
        st=1
      fi
      ;;
  esac
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
