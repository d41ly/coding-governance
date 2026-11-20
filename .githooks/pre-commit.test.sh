#!/usr/bin/env bash
# Runnable check for the .githooks/pre-commit BRANCH GUARD (charter [isolate] enforcement).
# Spins a throwaway repo, wires this repo's pre-commit via core.hooksPath, and asserts:
#   1) a commit ON the default branch is allowed
#   2) a commit parked OFF the default branch in the primary tree is refused
#   3) --no-verify overrides the refusal
# The throwaway repo has none of the gate-leg scripts (<prefix>/…, skills/…), so those legs
# self-skip and only the guard is exercised; the arms after the guard's plant stand-ins of their own,
# and the derived legs' arms copy this repository's runner. Run: bash .githooks/pre-commit.test.sh  (exit 0 = pass)
set -u
HOOK="$(cd "$(dirname "$0")" && pwd)/pre-commit"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
# Fixture identity and line endings for every git below, through the environment and not per repo
# (TOOL-aSparedSpawn-9 S1): no spawn, and command scope outranks a node's global autocrlf=true.
export GIT_AUTHOR_NAME=test GIT_AUTHOR_EMAIL=t@example.com GIT_COMMITTER_NAME=test GIT_COMMITTER_EMAIL=t@example.com
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
pass=0; fail=0
ck() { # name  actual_exit  expected_pass(0)/fail(1)
  local ok; if [ "$3" = 0 ]; then [ "$2" = 0 ] && ok=1 || ok=0; else [ "$2" != 0 ] && ok=1 || ok=0; fi
  if [ "$ok" = 1 ]; then echo "ok   $1 (exit $2)"; pass=$((pass+1))
  else echo "FAIL $1 (exit $2)"; fail=$((fail+1)); fi
}

cd "$tmp" || exit 2
git init -q --template= -b main
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

# ---- this repository's sources the stand-ins below copy ------------------------------------------
# The tracked resolver, found by name and never spelled at gov's prefix. The codebase-map leg's arms
# that once followed here retired with the hand-named leg (TOOL-dWitnessedBar-10 S4): the leg is a
# derived row now, its unstaged-artifact check moved into the gate's `--precommit`, and the derived
# arms at the end of this file drive the one call that runs it.
git checkout -q main
repo_src="${HOOK%/*}/.."
resolver=$(cd "$repo_src" && git ls-files -- '*resolve-python.sh' | head -n 1)
[ -n "$resolver" ] || { echo "FAIL no tracked resolve-python.sh in $repo_src — the launcher arms cannot run"; exit 2; }

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
    git init -q --template= -b main
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

# ---- the policy guard, TOOL-dGroundRules-6 AC9 ----------------------------------------------------
# A stand-in guard at the root install says it ran and exits as written; its list, committed, names
# one path. Every commit below captures stderr, so none sits at a terminal and the owner's proof never
# admits. Staging the listed path is refused when the guard exits 1, when it exits 2, and when the
# index tracks no python resolver, so no launcher can judge it; staging none runs nothing and prints
# no policy guard line. The REAL guard's verdicts are the policy kit's `guard-*` fixture cases.
pk=policy; pl=.governance/policy.toml; d="$tmp/policy-guard"; rm -rf "$d"; mkdir -p "$d"
cd "$d" || exit 2
git init -q --template= -b main
mkdir hk; cp "$HOOK" hk/pre-commit; chmod +x hk/pre-commit; git config core.hooksPath hk
mkdir -p "$pk" vendor .governance; cp "$repo_src/$resolver" vendor/
printf '# the guarded set\n%s\n' "$pl" > "$pk/guarded-paths.txt"
printf 'print("GUARD RAN")\nraise SystemExit(1)\n' > "$pk/guard.py"
echo base > "$pl"; git add -A; git commit -q --no-verify -m fixture
for ex in 1 2; do
  printf 'print("GUARD RAN")\nraise SystemExit(%s)\n' "$ex" > "$pk/guard.py"
  echo "$ex" > "$pl"; git add "$pl"
  out=$(git commit -q -m "g$ex" 2>&1); rc=$?
  case "$out" in *"GUARD RAN"*) r=$rc ;; *) r=0 ;; esac
  ck "AC9 a listed path staged and the guard exiting $ex: refused" "$r" 1
done
printf 'print("GUARD RAN")\n' > "$pk/guard.py"
git rm -q --cached "vendor/${resolver##*/}"; echo 3 > "$pl"; git add "$pl"
out=$(git commit -q -m g3 2>&1); rc=$?
case "$out" in *"GUARD RAN"*) r=0 ;; *"no python launcher to judge them"*) r=$rc ;; *) r=0 ;; esac
ck "AC9 a listed path staged and no launcher: refused, not skipped" "$r" 1
git reset -q
printf 'print("GUARD RAN")\nraise SystemExit(1)\n' > "$pk/guard.py"
echo x > other.txt; git add other.txt
out=$(git commit -q -m other 2>&1); rc=$?
case "$out" in *"GUARD RAN"*|*"policy guard"*|*"policy-guard"*) r=1 ;; *) r=$rc ;; esac
ck "AC9 a commit staging no listed path runs no guard and prints no policy guard line" "$r" 0
# TOOL-dGroundRules-72: a listed path committed by `git commit -a` or `git commit -- <path>`, never
# added. Git hands the hook a temporary index and the real one stages nothing, so the block and the
# guard must both read the handed one. This stand-in refuses only when ITS OWN staged read names the
# listed path, so an arm reds when either read misses it. Each arm resets the real index first.
printf 'import subprocess, sys\nseen = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True).stdout.split()\nprint("GUARD SAW", *seen)\nsys.exit(1 if "%s" in seen else 0)\n' "$pl" > "$pk/guard.py"
git reset -q; echo 5 > "$pl"
out=$(git commit -qam g5 2>&1); rc=$?
case "$out" in *"GUARD SAW"*"$pl"*) r=$rc ;; *) r=0 ;; esac
ck "S1 a listed path committed by git commit -a, never added: refused by a guard that saw it" "$r" 1
git reset -q; echo 6 > "$pl"
out=$(git commit -qm g6 -- "$pl" 2>&1); rc=$?
case "$out" in *"GUARD SAW"*"$pl"*) r=$rc ;; *) r=0 ;; esac
ck "S1 a listed path committed by git commit -- <path>, never added: refused by a guard that saw it" "$r" 1
# TOOL-dDeclaredLoop-2 S11 (AC15): a stand-in loop kit guard.py beside the stand-in policy guard must
# run INSTEAD of it, so the verdict reads the guard values and the floor where the loop kit resolves.
# Each stand-in names itself; the policy one admits, the loop one refuses, so the commit is refused
# only when the loop guard ran, and its output must not carry the policy stand-in's line. Red with the
# block's verdict put back to "$g".
git reset -q; lk=loop; mkdir -p "$lk"
printf 'print("GUARD RAN")\n' > "$pk/guard.py"
printf 'print("LOOP VERDICT RAN")\nraise SystemExit(1)\n' > "$lk/guard.py"
echo 8 > "$pl"; git add "$pl"
out=$(git commit -q -m g8 2>&1); rc=$?
case "$out" in *"GUARD RAN"*) r=0 ;; *"LOOP VERDICT RAN"*) r=$rc ;; *) r=0 ;; esac
ck "S11 a loop kit guard.py beside the policy guard runs instead of it, and its refusal holds" "$r" 1
git reset -q; rm -rf "$lk"
printf 'print("GUARD RAN")\nraise SystemExit(1)\n' > "$pk/guard.py"
# TOOL-dGroundRules-21 S21: guard.py removed from the working tree while its list stays at HEAD, and a
# listed path staged. No rung resolves the guard, so the block's `else` refuses, naming the rungs.
rm -f "$pk/guard.py"; echo 4 > "$pl"; git add "$pl"
out=$(git commit -q -m g4 2>&1); rc=$?
case "$out" in *"policy guard"*) r=$rc ;; *) r=0 ;; esac
ck "S21 guard.py removed with its list at HEAD and a listed path staged: refused naming the policy guard" "$r" 1
# TOOL-dGroundRules-72: the same guard-less refusal for a listed path committed by path, never added.
git reset -q; echo 7 > "$pl"
out=$(git commit -qm g7 -- "$pl" 2>&1); rc=$?
case "$out" in *"no guard.py resolves"*) r=$rc ;; *) r=0 ;; esac
ck "S1 guard.py removed and a listed path committed by git commit -- <path>, never added: refused" "$r" 1
# ---- the red-fix join's staged form, TOOL-aNimbleMend-15 S12 --------------------------------------
# A stand-in join at the root install says how it was called and exits 1 while HEAD's message carries
# a `Red-fix:` trailer, the real join's staged verdict on a fix with no record; the real join's own
# refusal is armed in the memory-tree kit. The hook ran that join only inside the hygiene leg, so
# only beside a staged memory path. These arms hold the other branch: a commit staging NO memory
# path runs the join's staged form by itself, a product-only commit on top of an unrecorded fix is
# refused, a staged memory path still takes the hygiene leg alone, and a launcher or a kit that
# does not resolve is an announced skip that commits. Red with the `else` branch taken out of the hook.
rj=build_records.py; d="$tmp/red-fix-join"; rm -rf "$d"; mkdir -p "$d"
cd "$d" || exit 2
git init -q --template= -b main
mkdir hk; cp "$HOOK" hk/pre-commit; chmod +x hk/pre-commit; git config core.hooksPath hk
mkdir -p "$mt" vendor src memory; cp "$repo_src/$resolver" vendor/
printf 'import subprocess, sys\nprint("JOIN RAN", *sys.argv[1:])\nsaid = subprocess.run(["git", "log", "-1", "--format=%%B"], capture_output=True, text=True).stdout\nsys.exit(1 if "Red-fix:" in said else 0)\n' > "$mt/$rj"
printf '#!/usr/bin/env bash\necho "HYGIENE RAN $*"\n' > "$mt/$hy"
echo 0 > src/app.txt; git add -A; git commit -q --no-verify -m fixture
echo 1 > src/app.txt; git add src/app.txt
out=$(git commit -q -m plain 2>&1); rc=$?
case "$out" in *"HYGIENE RAN"*) r=1 ;; *"JOIN RAN join red-fix --staged"*) r=$rc ;; *) r=1 ;; esac
ck "S12 a commit staging no memory path runs the join's staged form, and over a clean HEAD it commits" "$r" 0
echo 2 > src/app.txt; git add src/app.txt; git commit -q --no-verify -m "fix: the leg reads green again" -m "Red-fix: a leg"
echo 3 > src/app.txt; git add src/app.txt
out=$(git commit -q -m product 2>&1); rc=$?
case "$out" in *"JOIN RAN join red-fix --staged"*) r=$rc ;; *) r=0 ;; esac
ck "S12 a product-only commit on top of an unrecorded fix is refused by the join" "$r" 1
git reset -q; echo x > memory/rec.md; git add memory/rec.md
out=$(git commit -q -m record 2>&1); rc=$?
case "$out" in *"JOIN RAN"*) r=1 ;; *"HYGIENE RAN --staged"*) r=$rc ;; *) r=1 ;; esac
ck "S12 a commit staging a memory path runs the hygiene leg, and the join's own branch does not run" "$r" 0
git rm -q --cached "vendor/${resolver##*/}"; git add src/app.txt
out=$(git commit -q -m no-launcher 2>&1); rc=$?
case "$out" in *"JOIN RAN"*) r=1 ;; *"pre-commit: red-fix join leg SKIPPED — no tracked python resolver, or no usable launcher, to run $mt/$rj."*) r=$rc ;; *) r=1 ;; esac
ck "S12 no tracked resolver is an announced skip of the join, and the commit proceeds" "$r" 0
rm -f "$mt/$rj"; echo 4 > src/app.txt; git add src/app.txt
out=$(git commit -q -m no-kit 2>&1); rc=$?
case "$out" in *"JOIN RAN"*) r=1 ;; *"pre-commit: red-fix join leg SKIPPED — no kit root: no install-receipt row for $mt/$rj, no $mt/$rj at the root, and no GOV_KITROOT declared in .githooks/gate-env.sh."*) r=$rc ;; *) r=1 ;; esac
ck "S12 a join no rung resolves is an announced skip naming every rung, and the commit proceeds" "$r" 0
cd "$tmp" || exit 2

# ---- the check 9 render, TOOL-aTrimmedWait-3 AC5/AC6 ----------------------------------------------
# A stand-in hygiene gate at the root install fails its FIRST run with the check line the real fail()
# prints, read from the producer here so a message edit there reds these arms, and passes every later
# run; it counts its runs. A stand-in generator says how it was called, then exits as `.gen-exit`
# says, staging a file on 0. Check 9 with a staging generator commits that file after a second
# grading; check 12 never runs the generator; a declining generator is never followed by a grading.
hy_src=$(cd "$repo_src" && git ls-files -- "*$hy" | head -n 1)
fail_n=$(grep -c 'echo "HYGIENE check $1 FAILED' "$repo_src/$hy_src")
[ "$fail_n" = 1 ] && r=0 || r=1
ck "AC6 the producer prints its check line from one fail() literal (found $fail_n)" "$r" 0
fail_tpl=$(grep -o 'echo "HYGIENE check $1 FAILED[^"]*"' "$repo_src/$hy_src" | head -n 1)
fail_tpl=${fail_tpl#echo \"}; fail_tpl=${fail_tpl%\"}
run_render_commit() { # <check N> <generator exit> -> the commit's output, its exit, the run count, HEAD's paths
  local d="$tmp/render-$1-$2" line=${fail_tpl/\$1/$1}
  line=${line/\$2/drift}
  rm -rf "$d"; mkdir -p "$d"
  ( cd "$d" || exit 2
    git init -q --template= -b main
    mkdir hk; cp "$HOOK" hk/pre-commit; chmod +x hk/pre-commit; git config core.hooksPath hk
    mkdir -p "$mt" vendor memory; cp "$repo_src/$resolver" vendor/
    printf '%s\n' "$line" > .hy-line; printf '%s\n' "$2" > .gen-exit
    cat > "$mt/$hy" <<'EOF'
#!/usr/bin/env bash
n=$(( $(cat .hy-runs 2>/dev/null || echo 0) + 1 )); echo "$n" > .hy-runs
[ "$n" = 1 ] || { echo "HYGIENE ok"; exit 0; }
cat .hy-line; exit 1
EOF
    cat > "$mt/gen_build_index.py" <<'EOF'
import subprocess, sys
print("GEN RAN", *sys.argv[1:])
if open(".gen-exit").read().strip() != "0":
    sys.exit(1)
open("memory/rendered.md", "w").write("rendered\n")
subprocess.run(["git", "add", "memory/rendered.md"], check=True)
EOF
    git add -A; git commit -q --no-verify -m fixture
    echo x > memory/note.md; git add memory/note.md
    git commit -q -m note 2>&1; echo "COMMIT RC=$?"
    echo "HYGIENE RUNS=$(<.hy-runs)"
    echo "HEAD CARRIES $(git show --name-only --format= HEAD | tr '\n' ' ')" )
}
out=$(run_render_commit 9 0)
case "$out" in *"GEN RAN --write-staged"*"grading the memory hygiene leg again"*"COMMIT RC=0"*"HYGIENE RUNS=2"*"memory/rendered.md"*) r=0 ;; *) r=1 ;; esac
ck "AC5 a check 9 refusal runs --write-staged, grades again, and commits the staged file" "$r" 0
out=$(run_render_commit 12 0)
case "$out" in *"GEN RAN"*) r=1 ;; *"COMMIT RC=0"*) r=1 ;; *"HYGIENE RUNS=1"*) r=0 ;; *) r=1 ;; esac
ck "AC6 a check 12 refusal never runs the generator, and the commit is refused" "$r" 0
out=$(run_render_commit 9 1)
case "$out" in *"COMMIT RC=0"*|*"grading the memory hygiene leg again"*) r=1 ;; *"GEN RAN --write-staged"*"HYGIENE RUNS=1"*) r=0 ;; *) r=1 ;; esac
ck "AC6 a declined render is followed by no second grading, and the commit is refused" "$r" 0

# ---- the derived legs, TOOL-dWitnessedBar-10 AC1/AC2/AC3 ------------------------------------------
# This repository's runner and precommit.py, copied to a root install, read a fixture manifest: leg A
# guarded on a/, whose precommit argv exits as `.a-rc` says, and leg B with no precommit. A staged a/
# path runs A and commits; A failing refuses the commit naming it, and restored the same staged change
# commits; an unrelated staged path prints A not tripped and runs neither; no runner is an announced
# skip. B never runs. Red with the hook's derived call taken out, or with A's guard ignored.
rg_src=$(cd "$repo_src" && git ls-files -- '*run-gates/run-gates.sh' | head -n 1)
[ -n "$rg_src" ] || { echo "FAIL no tracked run-gates.sh in $repo_src — the derived arms cannot run"; exit 2; }
d="$tmp/derived"; rm -rf "$d"; mkdir -p "$d"
cd "$d" || exit 2
git init -q --template= -b main
mkdir hk; cp "$HOOK" hk/pre-commit; chmod +x hk/pre-commit; git config core.hooksPath hk
mkdir -p run-gates a b
cp "$repo_src/$rg_src" "$repo_src/${rg_src%/*}/precommit.py" run-gates/
printf '%s\n' 'echo "A RAN"; exit "$(<.a-rc)"' > a.sh; echo 0 > .a-rc
printf '%s\n' 'echo "B RAN"' > b.sh
printf '%s\n' '[' '  {"name": "A", "argv": ["bash", "a.sh"], "guard": ["a/"], "precommit": ["bash", "a.sh"]},' \
  '  {"name": "B", "argv": ["bash", "b.sh"]}' ']' > gate-legs.json
git add -A; git commit -q --no-verify -m fixture
echo 1 > a/x; git add a/x
out=$(git commit -q -m ax 2>&1); rc=$?
case "$out" in *"B RAN"*) r=1 ;; *"A RAN"*"pre-commit: A ok"*) r=$rc ;; *) r=1 ;; esac
ck "AC2 a staged a/ path runs leg A through the derived list, and the commit proceeds" "$r" 0
echo 1 > .a-rc; echo 2 > a/x; git add a/x
out=$(git commit -q -m ax2 2>&1); rc=$?
case "$out" in *"pre-commit: A FAILED (rc 1)"*) r=$rc ;; *) r=0 ;; esac
ck "AC3 leg A's precommit argv failing refuses the commit, naming it" "$r" 1
echo 0 > .a-rc
git commit -q -m ax2 >/dev/null 2>&1; ck "AC3 ...and with A restored, the same staged change commits" $? 0
echo 1 > .a-rc; echo y > b/y; git add b/y
out=$(git commit -q -m by 2>&1); rc=$?
case "$out" in *"A RAN"*|*"B RAN"*) r=1 ;; *"pre-commit: A not tripped"*) r=$rc ;; *) r=1 ;; esac
ck "AC2 an unrelated staged path prints A not tripped, runs neither leg, and commits" "$r" 0
rm -rf run-gates; echo z > b/y; git add b/y
out=$(git commit -q -m no-runner 2>&1); rc=$?
case "$out" in *"A RAN"*) r=1 ;; *"derived pre-commit leg SKIPPED — no kit root"*) r=$rc ;; *) r=1 ;; esac
ck "S4 a runner no rung resolves is an announced skip, and the commit proceeds" "$r" 0
cd "$tmp" || exit 2

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]
