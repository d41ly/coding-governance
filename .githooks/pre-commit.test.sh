#!/usr/bin/env bash
# Runnable check for the .githooks/pre-commit BRANCH GUARD (playbook §3 enforcement).
# Spins a throwaway repo, wires this repo's pre-commit via core.hooksPath, and asserts:
#   1) a commit ON the default branch is allowed
#   2) a commit parked OFF the default branch in the primary tree is refused
#   3) --no-verify overrides the refusal
# The throwaway repo has none of the gate-leg scripts (<prefix>/…, skills/…), so those legs
# self-skip and only the guard is exercised — except the codebase-map leg, whose arms follow the
# guard's and plant a stand-in gate. Run: bash .githooks/pre-commit.test.sh  (exit 0 = pass)
set -u
HOOK="$(cd "$(dirname "$0")" && pwd)/pre-commit"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
pass=0; fail=0
ck() { # name  actual_exit  expected_pass(0)/fail(1)
  local ok; if [ "$3" = 0 ]; then [ "$2" = 0 ] && ok=1 || ok=0; else [ "$2" != 0 ] && ok=1 || ok=0; fi
  if [ "$ok" = 1 ]; then echo "ok   $1 (exit $2)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $2)"; fail=$((fail+1)); fi
}

cd "$tmp" || exit 2
git init -q -b main
git config user.email t@example.com; git config user.name test
git config core.autocrlf false   # hermetic: a global autocrlf=true otherwise reaches this repo
mkdir hk; cp "$HOOK" hk/pre-commit; chmod +x hk/pre-commit
git config core.hooksPath hk
export GOV_DEFAULT_BRANCH=main   # throwaway has no origin/HEAD — pin the default explicitly

echo a > a; git add a; git commit -q -m first; ck "commit on default branch allowed" $? 0
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${pass:-1} assertions)" || echo "FAIL (${pass:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi

git checkout -q -b feature/x
echo b > b; git add b; git commit -q -m second 2>/dev/null; ck "commit off default branch refused" $? 1

git commit -q --no-verify -m second; ck "--no-verify overrides the guard" $? 0

# ---- the guard's default branch is the REMOTE LADDER'S (TOOL-dLadderedRemote-2) --------------------
# The only remote is named incms and its HEAD names trunk, so a guard reading a literal remote name
# falls back to main and refuses trunk. With a second remote and no GOV_REMOTE the ladder refuses:
# the guard must announce it, and GOV_DEFAULT_BRANCH must still pin the default (a closing-review
# finding: the pin was dropped on a refusal). An empty GOV_DEFAULT_BRANCH reads as unset.
git checkout -q main
git branch -q trunk
git remote add incms ../incms.git
git update-ref refs/remotes/incms/trunk HEAD; git symbolic-ref refs/remotes/incms/HEAD refs/remotes/incms/trunk
git checkout -q trunk
echo l1 > l1; git add l1
GOV_DEFAULT_BRANCH= git commit -q -m l1 2>/dev/null; ck "the only remote's HEAD names the default (trunk), no pin" $? 0
git remote add origin ../origin.git
echo l2 > l2; git add l2
out=$(GOV_DEFAULT_BRANCH= git commit -q -m l2 2>&1); ck "two remotes and no pin: refused against the main fallback" $? 1
printf '%s\n' "$out" | grep -q 'export GOV_REMOTE=<remote>'; ck "...and the refusal names GOV_REMOTE" $? 0
GOV_DEFAULT_BRANCH=trunk git commit -q -m l2 2>/dev/null; ck "two remotes with GOV_DEFAULT_BRANCH=trunk: the pin holds" $? 0
# TOOL-dLadderedRemote-6: where the pin decides, the refusal is not printed on every commit.
echo l3 > l3; git add l3
out=$(GOV_DEFAULT_BRANCH=trunk git commit -q -m l3 2>&1)
printf '%s\n' "$out" | grep -q 'GOV_REMOTE'; ck "...and with the pin set it prints no GOV_REMOTE line" $? 1
git remote remove origin; git remote remove incms
# A TAG named like the default branch makes `symbolic-ref --short HEAD` read `heads/main`, and a guard
# reading the short form refused a commit ON the default branch (TOOL-dLadderedRemote-6).
git checkout -q main; git tag main
echo t3 > t3; git add t3
git commit -q -m t3 2>/dev/null; ck "a tag named like the default branch does not refuse a commit on it" $? 0
git tag -d main >/dev/null

# ---- the codebase-map leg ------------------------------------------------------------------------
# A stand-in gate, red while a flag file exists. The hook consumes only the gate's exit status and
# output, so that is the whole contract the stand-in holds; the REAL gate was observed red on a staged
# break when the leg landed. These arms keep the trigger, the remedy and the two refusals from
# regressing. The gate, the map root and the resolver sit at paths gov does not use, because the leg
# DERIVES all three and a fixture at gov's own paths would pass a leg that had them spelled back in.
git checkout -q main
repo_src="${HOOK%/*}/.."
resolver=$(cd "$repo_src" && git ls-files -- '*resolve-python.sh' | head -n 1)
[ -n "$resolver" ] || { echo "FAIL no tracked resolve-python.sh in $repo_src — the map arms cannot run"; exit 2; }
mkdir -p gate vendor map/generated
cp "$repo_src/$resolver" vendor/
cat > gate/test_map.py <<'EOF'
import os, sys
if os.path.exists("gate-red"):
    print("FAIL test_generated_artifacts_are_fresh")
    print("STALE symbols.json")
    sys.exit(1)
print("ok   test_generated_artifacts_are_fresh")
EOF
printf 'MAP_ROOT=map\nGATE_FILE=gate/test_map.py\n' > .codebase-map.conf
echo '{"v":1}' > map/generated/x.json
git add -A; git commit -q --no-verify -m map-fixture

touch gate-red
echo 'x = 1' > a.py; git add a.py
out=$(git commit -q -m a 2>&1); ck "a staged .py with a red map gate is refused" $? 1
printf '%s\n' "$out" | grep -q 'gen_map.py --write'; ck "the refusal prints the regen remedy" $? 0
git reset -q

echo 'function f() {}' > e.js; git add e.js
out=$(git commit -q -m e 2>&1); ck "a staged .js with a red map gate is refused" $? 1
printf '%s\n' "$out" | grep -q 'gen_map.py --write'; ck "the .js refusal is the map gate's" $? 0
git reset -q

echo t > b.txt; git add b.txt
git commit -q -m b >/dev/null 2>&1; ck "a commit staging no .py or .js does not run the map gate" $? 0

# Every arm below stages a file no earlier arm could have committed, so a refusal can never be
# git's "nothing to commit" — measured: reusing a.py let this arm pass with the trigger disabled.
rm gate-red
echo '{"v":2}' > map/generated/x.json; echo 'y = 2' > c.py; git add c.py
out=$(git commit -q -m c 2>&1); ck "fresh artifacts left unstaged are refused" $? 1
printf '%s\n' "$out" | grep -q 'NOT staged'; ck "the refusal names the unstaged artifacts" $? 0

git add map/generated/x.json
git commit -q -m d >/dev/null 2>&1; ck "a green map gate with its artifacts staged is allowed" $? 0

printf 'MAP_ROOT=map\nGATE_FILE=gate/moved.py\n' > .codebase-map.conf; git add .codebase-map.conf
echo 'z = 3' > f.py; git add f.py
out=$(git commit -q -m f 2>&1); ck "a GATE_FILE naming no file is refused, not skipped" $? 1
printf '%s\n' "$out" | grep -q 'names no file'; ck "the refusal names the conf key" $? 0

# ---- the kit-root ladder, TOOL-aRepatriatedFork-24 AC1/AC2 ---------------------------------------
# The hygiene leg at three prefixes gov does not use, each reached by a DIFFERENT rung: `vendor/gov/`
# by GOV_KITROOT in gate-env.sh, `scripts/` by an install receipt, the root by the probe. The stand-in
# gate says where it ran from, so an arm can tell "ran from there" from "ran from somewhere". The kit
# and its file are joined at run time, as the hook's own ladder joins them, so no fixture spells a
# kit path. The leg is reached only when memory/ is staged, so every fixture stages a memory file.
mt=memory-tree; hy=check-memory-hygiene.sh
run_prefix_commit() { # <prefix, "" for the root> <rung: env|receipt|root|none> <hook> -> the commit's output
  local pfx=$1 rung=$2 hook=$3 d="$tmp/pfx-$2" kd
  rm -rf "$d"; mkdir -p "$d"
  ( cd "$d" || exit 2
    git init -q -b main; git config user.email t@example.com; git config user.name test
    git config core.autocrlf false
    mkdir hk; cp "$hook" hk/pre-commit; chmod +x hk/pre-commit; git config core.hooksPath hk
    kd=${pfx:+$pfx/}$mt; mkdir -p "$kd" memory
    printf '#!/usr/bin/env bash\necho "HYGIENE RAN from %s $*"\n' "$kd" > "$kd/$hy"
    case "$rung" in
      env) mkdir -p .githooks; printf 'GOV_KITROOT=%s\n' "$pfx" > .githooks/gate-env.sh ;;
      receipt) mkdir -p .governance
        printf '{\n  "files": [\n    {\n      "path": "%s",\n      "source": "gov/%s"\n    }\n  ]\n}\n' \
          "$kd/$hy" "$mt/$hy" > .governance/install.json ;;
    esac
    git add -A; git commit -q --no-verify -m fixture
    echo x > memory/note.md; git add memory/note.md
    git commit -q -m note 2>&1 )
}
out=$(run_prefix_commit vendor/gov env "$HOOK"); rc=$?
case "$out" in *"HYGIENE RAN from vendor/gov/$mt --staged"*) r=$rc ;; *) r=1 ;; esac
ck "AC1 GOV_KITROOT in gate-env.sh reaches the hygiene gate under vendor/gov/" "$r" 0
out=$(run_prefix_commit scripts receipt "$HOOK"); rc=$?
case "$out" in *"HYGIENE RAN from scripts/$mt --staged"*) r=$rc ;; *) r=1 ;; esac
ck "AC1 the install receipt reaches the hygiene gate under scripts/" "$r" 0
out=$(run_prefix_commit "" root "$HOOK"); rc=$?
case "$out" in *"HYGIENE RAN from $mt --staged"*) r=$rc ;; *) r=1 ;; esac
ck "AC1 the root probe reaches the hygiene gate at a root install" "$r" 0
# A MISS is an announced skip that still commits (F1 (c)), never a silent one.
out=$(run_prefix_commit vendor/gov none "$HOOK"); rc=$?
case "$out" in *"HYGIENE RAN"*) r=1 ;; *"memory-tree hygiene leg SKIPPED — no kit root"*) r=$rc ;; *) r=1 ;; esac
ck "AC1 an unresolvable kit root is an announced skip, and the commit proceeds" "$r" 0
# AC2, THE RED-FIRST CONTROL, against the hook as `2143b6d6` holds it: the same vendor/gov/ fixture
# skips the leg silently and exits 0. Pinned to a sha, so landing this unit cannot turn the control
# into the fixed hook. A repository that does not carry the sha SKIPS the control, out loud.
if git -C "$repo_src" show 2143b6d6:.githooks/pre-commit > "$tmp/old-pre-commit" 2>/dev/null && [ -s "$tmp/old-pre-commit" ]; then
  out=$(run_prefix_commit vendor/gov env "$tmp/old-pre-commit"); rc=$?
  case "$out" in *"HYGIENE RAN"*) r=1 ;; *) r=$rc ;; esac
  ck "AC2 red-first: the 2143b6d6 hook skips that leg silently and exits 0" "$r" 0
else
  echo "SKIP AC2 red-first control NOT RUN: 2143b6d6 is a coding-governance commit this repository does not carry"
fi

# ---- the unattended skill wiring leg, TOOL-aHomedAnchor-4 AC1/AC2 ---------------------------------
# A stand-in adopter at the root install says how it was called. Staging the conf runs it with
# --check; staging an unrelated file does not run it at all.
ua=unattended; ad=adopt-unattended.sh
d="$tmp/wiring"; rm -rf "$d"; mkdir -p "$d"
out=$( cd "$d" || exit 2
  git init -q -b main; git config user.email t@example.com; git config user.name test
  git config core.autocrlf false
  mkdir hk; cp "$HOOK" hk/pre-commit; chmod +x hk/pre-commit; git config core.hooksPath hk
  mkdir -p "$ua"; printf '#!/usr/bin/env bash
echo "WIRING RAN $*"
' > "$ua/$ad"
  git add -A; git commit -q --no-verify -m fixture
  echo x > other.txt; git add other.txt; git commit -q -m other 2>&1
  echo 'ANCHOR_SCOPE="local"' > .unattended.conf; git add .unattended.conf; git commit -q -m conf 2>&1 ); rc=$?
case "$out" in *"WIRING RAN --check"*) r=$rc ;; *) r=1 ;; esac
ck "AC1 a staged .unattended.conf runs the adopter with --check" "$r" 0
n_runs=$(printf '%s
' "$out" | grep -c 'WIRING RAN' || true)
[ "$n_runs" = 1 ] && r=0 || r=1
ck "AC2 an unrelated staged file does not run the adopter (one run, not $n_runs)" "$r" 0

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]
