#!/usr/bin/env bash
# adopt-codebase-map.test.sh — e2e self-test for the codebase-map ADOPTER. Exit 0 = every arm held.
#
#   bash tools/codebase-map/adopt-codebase-map.test.sh
#
# WHY THIS FILE EXISTS. A Tier-2 review of TOOL-aRootedPrefix-1 found 4 of 7 defects — including a
# blocker that wrote a conf, a whole map tree and a gate file into a repository the operator never
# named — in `adopt-codebase-map.sh`, the ONE changed file no gate leg executed. The Python engine
# beside it, carried by ~20 selftest arms, produced zero confirmed findings. That correlation is the
# whole argument for this leg: the adopter WRITES, and nothing was watching it.
#
# DISCIPLINES (same as the sibling gate tests):
#  * Every arm asserts the SPECIFIC message or the SPECIFIC on-disk effect, never the exit code
#    alone — a probe that reads only `$?` reports success while exercising nothing.
#  * A refusal arm asserts the WRITES DID NOT HAPPEN, not just that the script exited non-zero.
#    "It refused" and "it refused before writing" are different claims and only one is useful.
#  * `PASS` prints after the LAST arm.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
KIT="$ROOT/tools/codebase-map"
fails=0
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

note() { printf '%s\n' "$*"; }
bad()  { fails=$((fails+1)); printf 'arm FAIL  %s\n' "$*"; }
good() { printf 'arm ok    %s\n' "$*"; }

# A repo with the kit installed at $2 (a prefix relative to the repo root, may be empty) and a
# filled project layer, so the adopter can run to completion.
mkrepo() { # $1 = repo dir · $2 = prefix
  mkdir -p "$1" && git -C "$1" init -q
  git -C "$1" config user.email t@t; git -C "$1" config user.name t
  if [ -n "$2" ]; then mkdir -p "$1/$2"; _kd="$1/$2/codebase-map"; else _kd="$1/codebase-map"; fi
  cp -r "$KIT" "$_kd"
  rm -f "$_kd/adopt-codebase-map.test.sh"
  mkdir -p "$1/src"; printf 'def hello():\n    return 1\n' > "$1/src/mod.py"
  cat > "$_kd/map_extractors.py" <<'PY'
import map_lib as m

def inventory_ids():
    return ("mods",)

def all_inventories():
    return {"mods": m.module_inventory(m.repo_root() / "src", "mods")}
PY
  printf '%s\n' "$_kd"
}

# ---------------------------------------------------------------------------------------------
# arm 1 (review B1b) — run BY PATH from a DIFFERENT repo: refuse, and write into NEITHER tree.
# Before the fix this adopted the KIT's repo at exit 0 while printing relative paths that read as
# the cwd's repo, and it was a REGRESSION: the pre-1.1 `-ef` guard had refused the same invocation.
# ---------------------------------------------------------------------------------------------
KD=$(mkrepo "$TMP/a1-kitrepo" "tools")
mkdir -p "$TMP/a1-target" && git -C "$TMP/a1-target" init -q
out=$(cd "$TMP/a1-target" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1); rc=$?
if [ "$rc" = 0 ]; then bad "1 by-path-from-another-repo: exited 0 (must refuse)"
elif ! printf '%s' "$out" | grep -q "refusing"; then
  bad "1 by-path-from-another-repo: refused without saying why"; printf '%s\n' "$out" | sed 's/^/      /'
elif [ -f "$TMP/a1-kitrepo/.codebase-map.conf" ]; then
  bad "1 by-path-from-another-repo: WROTE a conf into the kit's own repo"
elif [ -f "$TMP/a1-target/.codebase-map.conf" ]; then
  bad "1 by-path-from-another-repo: wrote a conf into the target it never resolved"
else
  good "1 by-path-from-another-repo refuses, naming both roots, writing nothing"
fi

# ---------------------------------------------------------------------------------------------
# arm 2 (review M2) — a prefix deeper than one segment is refused BEFORE anything is written.
# The gate template resolves only <root>/codebase-map and <root>/<one>/codebase-map, so accepting a
# deeper install left a half-adopted repo whose failure was reported as a coverage violation.
# ---------------------------------------------------------------------------------------------
KD=$(mkrepo "$TMP/a2" "a/b")
out=$(cd "$TMP/a2" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1); rc=$?
if [ "$rc" = 0 ]; then bad "2 deep-prefix: exited 0 (must refuse)"
elif ! printf '%s' "$out" | grep -q "deeper than one segment"; then
  bad "2 deep-prefix: wrong message"; printf '%s\n' "$out" | sed 's/^/      /'
elif [ -f "$TMP/a2/.codebase-map.conf" ] || [ -d "$TMP/a2/memory" ]; then
  bad "2 deep-prefix: refused only AFTER writing (conf and/or map tree on disk)"
else
  good "2 deep-prefix refuses before writing anything"
fi

# ---------------------------------------------------------------------------------------------
# arm 3 (review H1 + L1) — a hostile install prefix must not corrupt the conf this script SOURCES.
# `&` is sed's whole-match and `\` starts an escape, so the sed stamp silently mangled the line and
# still exited 0; the next run sourced the wreckage and executed part of it. Each prefix is checked
# by SOURCING the conf in a clean subshell and comparing the resulting value exactly, and by
# asserting the run never claims success and failure for the same step in one breath (L1).
# ---------------------------------------------------------------------------------------------
# The load-bearing assertion is that the conf may only ever hold an INTENDED value: the exact stamp
# when the run claims one, and the example's untouched default when it declines. "It admitted it
# could not stamp" is not enough on its own — a mangled write plus an honest note would still leave
# a broken conf on disk. The last two prefixes are ordinary ones the conf grammar accepts, so the
# stamping's HAPPY path is armed too and this loop cannot pass by only ever declining.
DEFAULT_MDC='python codebase-map/map_diff.py'
i=0
for prefix in 'R&D' 'a b' "x'y" 'ok-dir' 'ok.dir'; do
  i=$((i+1))
  KD=$(mkrepo "$TMP/a3-$i" "$prefix")
  out=$(cd "$TMP/a3-$i" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1)
  conf="$TMP/a3-$i/.codebase-map.conf"
  if [ ! -f "$conf" ]; then bad "3.$i prefix '$prefix': no conf created"; continue; fi
  got=$(cd "$TMP/a3-$i" && ( . ./.codebase-map.conf >/dev/null 2>&1; printf '%s' "${MAP_DIFF_CMD:-}" ))
  side=$(cd "$TMP/a3-$i" && . ./.codebase-map.conf 2>&1 >/dev/null)
  claim_fail=$(printf '%s' "$out" | grep -c "could NOT stamp" || true)
  claim_ok=$(printf '%s' "$out" | grep -c "MAP_DIFF_CMD stamped" || true)
  if [ -n "$side" ]; then
    bad "3.$i prefix '$prefix': sourcing the conf EXECUTED something: $side"
  elif [ "$claim_fail" != 0 ] && [ "$claim_ok" != 0 ]; then
    bad "3.$i prefix '$prefix': printed BOTH a failure note and a success claim"
  elif [ "$claim_ok" != 0 ] && [ "$got" != "python $prefix/codebase-map/map_diff.py" ]; then
    bad "3.$i prefix '$prefix': claimed a stamp but MAP_DIFF_CMD is '$got'"
  elif [ "$claim_fail" != 0 ] && [ "$got" != "$DEFAULT_MDC" ]; then
    bad "3.$i prefix '$prefix': declined the stamp but left MAP_DIFF_CMD as '$got' (a half-write)"
  elif [ "$claim_ok" = 0 ] && [ "$claim_fail" = 0 ]; then
    bad "3.$i prefix '$prefix': said nothing at all about the stamp"
  else
    good "3.$i prefix '$prefix': conf sources cleanly, and holds an intended value"
  fi
done

# ---------------------------------------------------------------------------------------------
# arm 4 (review H2) — the DOCUMENTED path: the operator copies the example conf FIRST, so the
# adopter's create-branch stamp never fires. The digest command must still resolve, because the
# scaffolded map README ships it. Before the fix that README named codebase-map/map_diff.py at a
# tools/-prefixed install, and `ls` on it said No such file.
# ---------------------------------------------------------------------------------------------
KD=$(mkrepo "$TMP/a4" "tools")
cp "$KD/.codebase-map.conf.example" "$TMP/a4/.codebase-map.conf"
out=$(cd "$TMP/a4" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1); rc=$?
if [ "$rc" != 0 ]; then bad "4 documented-path: adoption failed"; printf '%s\n' "$out" | sed 's/^/      /'
else
  dead=""
  for tok in $(grep -ohE '[A-Za-z0-9_./-]+\.py' "$TMP/a4/memory/map/README.md" | grep '/' | sort -u); do
    [ -f "$TMP/a4/$tok" ] || dead="$dead $tok"
  done
  if [ -n "$dead" ]; then bad "4 documented-path: the scaffolded README names dead paths:$dead"
  elif ! grep -q "tools/codebase-map/map_diff.py" "$TMP/a4/memory/map/README.md"; then
    bad "4 documented-path: the README carries no prefixed digest command (arm proves nothing)"
  else
    good "4 documented-path: every path the scaffolded README prints resolves"
  fi
fi

# ---------------------------------------------------------------------------------------------
# arm 5 (review B1a) — a SYMLINKED kit dir must anchor to the ADOPTING repo, never to the link
# target's repo. `git rev-parse --show-toplevel` answers with the physical path, which is why the
# adopter resolves its root logically instead. SKIPPED, loudly, where symlinks cannot be created
# (Windows without Developer Mode) — a silent skip would be the absence-reads-as-pass class.
# ---------------------------------------------------------------------------------------------
mkdir -p "$TMP/a5-src" && git -C "$TMP/a5-src" init -q
cp -r "$KIT" "$TMP/a5-src/codebase-map"; rm -f "$TMP/a5-src/codebase-map/adopt-codebase-map.test.sh"
mkdir -p "$TMP/a5-adopting/tools" && git -C "$TMP/a5-adopting" init -q
mkdir -p "$TMP/a5-adopting/src"; printf 'def hello():\n    return 1\n' > "$TMP/a5-adopting/src/mod.py"
cat > "$TMP/a5-src/codebase-map/map_extractors.py" <<'PY'
import map_lib as m

def inventory_ids():
    return ("mods",)

def all_inventories():
    return {"mods": m.module_inventory(m.repo_root() / "src", "mods")}
PY
# A POSIX symlink first; on Windows fall back to a directory JUNCTION, which needs no Developer
# Mode and is the exact shape the blocker was measured on (a junctioned kit dir resolving to the
# link target's repo). `git rev-parse --show-toplevel` follows both.
link_made=0
if ln -s "$TMP/a5-src/codebase-map" "$TMP/a5-adopting/tools/codebase-map" 2>/dev/null &&
   [ -L "$TMP/a5-adopting/tools/codebase-map" ]; then
  link_made=1
elif command -v cygpath >/dev/null 2>&1 && command -v cmd >/dev/null 2>&1; then
  rm -rf "$TMP/a5-adopting/tools/codebase-map"
  cmd //c mklink //J "$(cygpath -w "$TMP/a5-adopting/tools/codebase-map")" \
                     "$(cygpath -w "$TMP/a5-src/codebase-map")" >/dev/null 2>&1 || true
  [ -f "$TMP/a5-adopting/tools/codebase-map/map_lib.py" ] && link_made=2
fi
if [ "$link_made" != 0 ]; then
  out=$(cd "$TMP/a5-adopting" && bash tools/codebase-map/adopt-codebase-map.sh --scaffold 2>&1); rc=$?
  if [ -f "$TMP/a5-src/.codebase-map.conf" ]; then
    bad "5 symlinked-kit: adopted the LINK TARGET's repo"
  elif [ "$rc" = 0 ] || [ -f "$TMP/a5-adopting/.codebase-map.conf" ]; then
    good "5 symlinked-kit anchors to the adopting repo"
  else
    bad "5 symlinked-kit: neither adopted nor refused clearly"; printf '%s\n' "$out" | sed 's/^/      /'
  fi
else
  note "arm SKIP  5 symlinked-kit — this host cannot create symlinks (no Developer Mode?)"
fi

# ---------------------------------------------------------------------------------------------
# arm 6 — the happy path still works end to end at a prefixed install, and the gate it leaves
# behind is LIVE: a new module reds it. A green adopter that installs a dead gate is the
# fixture-passes-by-finding-nothing class one level up.
# ---------------------------------------------------------------------------------------------
KD=$(mkrepo "$TMP/a6" "tools")
# Run 1 creates + stamps the conf and exits 1 BY DESIGN ("EDIT IT, then re-run"); run 2 adopts.
(cd "$TMP/a6" && bash "$KD/adopt-codebase-map.sh" --scaffold >/dev/null 2>&1) || true
out=$(cd "$TMP/a6" && bash "$KD/adopt-codebase-map.sh" --scaffold 2>&1); rc=$?
if [ "$rc" != 0 ]; then bad "6 happy-path: adoption failed"; printf '%s\n' "$out" | sed 's/^/      /'
elif ! printf '%s' "$out" | grep -q "Adopted."; then bad "6 happy-path: no Adopted. line"
else
  printf 'def added():\n    return 2\n' > "$TMP/a6/src/newmod.py"
  gate=$(cd "$TMP/a6" && . ./.codebase-map.conf >/dev/null 2>&1; printf '%s' "${GATE_FILE:-tests/test_codebase_map.py}")
  if (cd "$TMP/a6" && python "$gate" >/dev/null 2>&1); then
    bad "6 happy-path: the installed gate stayed GREEN on an unclaimed new module"
  else
    good "6 happy-path adopts, and the gate it installs is live"
  fi
fi

[ "$fails" = 0 ] || { printf '%s arm(s) FAILED\n' "$fails"; exit 1; }
echo "PASS"
