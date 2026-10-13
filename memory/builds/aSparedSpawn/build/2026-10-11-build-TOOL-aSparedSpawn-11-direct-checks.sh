#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-11
# TOOL-aSparedSpawn-11 (spec rev-2) — the pass-time direct checks. No arm of any suite runs here and no
# suite prologue is copied: each check drives the CHANGED program itself over a hand-built fixture.
#   bash <this> <gov root> <scratch dir> [ac7|runner|onesignal]...   (no step named = all three)
#   ac7        build_commit's walk memo in a hand-built repository, then the memo key staged to omit
#              the range in a scratch copy of the library, which must red.
#   runner     the agent-cap no-regress runner, extracted verbatim from the suite's quoted heredoc,
#              over the real tracked population plus four hand fixtures; its parity mode on a stride
#              sample; then the exit stub staged to drop its code (parity must red) and the marker
#              strip staged to a no-op (the property must red on zero ratifications).
#   onesignal  selftest.read_one_signal against the report subprocess for every signal, over a
#              hand-built repository; no selftest test function is called.
set -u
# The launcher, resolved before any cd from the repository this record sits in, four levels up.
_d=.; [[ ${BASH_SOURCE[0]} == */* ]] && _d=${BASH_SOURCE[0]%/*}; . "$_d/../../../../tools/lib/resolve-python.sh" || exit 2
PY=$(resolve_python) || exit 2
GOV=$1; W=$2; shift 2
STEPS=${*:-ac7 runner onesignal}
mkdir -p "$W"
fails=0
check_step() { if [ "$1" = 0 ]; then echo "ok    $2"; else echo "FAIL  $2"; fails=$((fails+1)); fi; }

read_ac7_probe() {   # $1 = library, $2 = repository dir; prints the observation line
  (
    probe_lib=$1; probe_dir=$2
    rm -rf "$probe_dir"; mkdir -p "$probe_dir"; cd "$probe_dir" || exit 2
    git init -q -b main . && git config user.email t@t && git config user.name t && git config core.autocrlf false
    printf 'x\n' > seed.txt && git add -A && git commit -q -m seed --no-verify
    base=$(git rev-parse HEAD)
    mkdir -p work && printf 'a\n' > work/one.txt
    git add -A && git commit -q -m "lane" -m "Pass: ARCH-tRun-1" --no-verify
    want=$(git rev-parse HEAD)
    . "$probe_lib"
    # The suite arm's counter: a `git` stub first on PATH, in the PATH's own (MSYS) spelling.
    LOG="$probe_dir.revlist.log"; rm -f "$LOG"
    stub_dir="$PWD.bin"; mkdir -p "$stub_dir"
    printf '#!/usr/bin/env bash\ncase " $* " in *" rev-list "*) echo r >> "%s" ;; esac\nexec "%s" "$@"\n' \
      "$LOG" "$(command -v git)" > "$stub_dir/git"
    chmod +x "$stub_dir/git"
    PATH="$stub_dir:$PATH"
    walks=0
    measure_walks() { walks=0; [ -f "$LOG" ] && while IFS= read -r _l; do walks=$((walks+1)); done < "$LOG"; rm -f "$LOG"; }
    build_commit "$base..HEAD" ARCH-tRun-1 memory/builds/tRun "" "" >/dev/null; u1=$_BC_OUT
    build_commit "$base..HEAD" ARCH-tRun-1 memory/builds/tRun "" "" >/dev/null; u2=$_BC_OUT
    measure_walks; un=$walks
    declare -A _BC_MEMO=()
    build_commit "$base..HEAD" ARCH-tRun-1 memory/builds/tRun "" "" >/dev/null; m1=$_BC_OUT
    build_commit "$base..HEAD" ARCH-tRun-1 memory/builds/tRun "" "" >/dev/null; m2=$_BC_OUT
    build_commit "$want..HEAD" ARCH-tRun-1 memory/builds/tRun "" "" >/dev/null; m3=$_BC_OUT
    build_commit "$base..HEAD" ARCH-tRun-1 memory/builds/tRun "" "" 5 "" >/dev/null; m4=$_BC_OUT
    measure_walks; mn=$walks
    [ "$u1" = "$want" ] && u1=WANT; [ "$u2" = "$want" ] && u2=WANT
    [ "$m1" = "$want" ] && m1=WANT; [ "$m2" = "$want" ] && m2=WANT
    [ "$m3" = "$want" ] && m3=WANT; [ "$m4" = "$want" ] && m4=WANT
    echo "u=$u1,$u2 m=$m1,$m2 other=$m3 capped=$m4 walks undeclared=$un declared=$mn"
  )
}

case " $STEPS " in *" ac7 "*)
  want="u=WANT,WANT m=WANT,WANT other= capped=WANT walks undeclared=2 declared=3"
  got=$(read_ac7_probe "$GOV/tools/unattended/lib-unattended.sh" "$W/ac7repo")
  echo "      $got"
  [ "$got" = "$want" ]; check_step $? "AC7 the memo walks once per (range, order, count) and answers as an undeclared call"
  sed 's/_bc_key="$_bc_ord|$_bc_mc|$_bc_range"/_bc_key="$_bc_ord|$_bc_mc"/' \
    "$GOV/tools/unattended/lib-unattended.sh" > "$W/lib-keybreak.sh"
  cmp -s "$GOV/tools/unattended/lib-unattended.sh" "$W/lib-keybreak.sh"; [ $? = 1 ]; check_step $? "AC7 break staged"
  got=$(read_ac7_probe "$W/lib-keybreak.sh" "$W/ac7repo2")
  echo "      $got"
  [ "$got" != "$want" ]; check_step $? "AC7 a key that omits the range reds"
;; esac

case " $STEPS " in *" runner "*)
  awk '/<<.JSEOF.$/{f=1;next} /^JSEOF$/{f=0} f' "$GOV/tools/hooks/agent-cap.test.sh" > "$W/nr.js"
  git -C "$GOV" show d65da7ab:tools/hooks/agent-cap.js > "$W/base-hook.js"
  F="$W/fix"; rm -rf "$F"; mkdir -p "$F"
  printf '%s\n' 'const MAX = 5' 'const units = [1, 2, 3, 4, 5]' 'const out = []' \
    'for (const u of units) { // gov:sequential-agents(MAX)' "  out.push(await agent('do ' + u, { label: 'u' }))" '}' > "$F/seq-marked.js"
  printf '%s\n' 'const units = [1, 2, 3]' 'const out = []' \
    "for (const u of units) out.push(await agent('do ' + u, { label: 'u' }))" > "$F/seq-unmarked.js"
  printf '%s\n' 'await parallel(all.map(f))' > "$F/raw.js"
  printf '%s\n' 'const x = 1' > "$F/plain.js"
  t0=$EPOCHSECONDS
  node "$W/nr.js" property "$W/base-hook.js" "$GOV/tools/hooks/agent-cap.js" "$GOV" "$F" > "$W/prop.out" 2>&1
  check_step $? "AC1 the property in one node: $(tail -1 "$W/prop.out") in $((EPOCHSECONDS - t0)) s"
  node "$W/nr.js" parity "$W/base-hook.js" "$GOV/tools/hooks/agent-cap.js" "$GOV" "$F" 400 > "$W/par.out" 2>&1
  check_step $? "S2 parity: $(tail -1 "$W/par.out")"
  sed 's/if (code === null) code = c === undefined ? 0 : c; throw STOP/if (code === null) code = 0; throw STOP/' \
    "$W/nr.js" > "$W/nr-ac2.js"
  cmp -s "$W/nr.js" "$W/nr-ac2.js"; [ $? = 1 ]; check_step $? "AC2 break staged"
  node "$W/nr-ac2.js" parity "$W/base-hook.js" "$GOV/tools/hooks/agent-cap.js" "$GOV" "$F" 400 > "$W/ac2.out" 2>&1
  [ $? = 1 ] && grep -q '^DISAGREE ' "$W/ac2.out"; check_step $? "AC2 the dropped exit code reds the parity, naming: $(grep -m1 '^DISAGREE ' "$W/ac2.out")"
  sed "s/body.split('gov:sequential-agents').join('')/body/" "$W/nr.js" > "$W/nr-ac3.js"
  cmp -s "$W/nr.js" "$W/nr-ac3.js"; [ $? = 1 ]; check_step $? "AC3 break staged"
  node "$W/nr-ac3.js" property "$W/base-hook.js" "$GOV/tools/hooks/agent-cap.js" "$GOV" "$F" > "$W/ac3.out" 2>&1
  [ $? = 1 ] && grep -q ' 0 ratified$' "$W/ac3.out"; check_step $? "AC3 a no-op strip reds: $(tail -1 "$W/ac3.out")"
;; esac

case " $STEPS " in *" onesignal "*)
  IFS= read -r -d '' ONESIG <<'PY' || :
import json, os, pathlib, shutil, subprocess, sys, tempfile, time
kit, work = pathlib.Path(sys.argv[1]).resolve(), sys.argv[2]
sys.path.insert(0, str(kit))
import selftest as st
tmp = pathlib.Path(tempfile.mkdtemp(dir=work))
r = tmp / "hand"
(r / kit.name).mkdir(parents=True)
(r / "src").mkdir()
(r / "memory").mkdir()
(r / ".memory-tree.conf").write_text("MEMORY_ROOT=memory\n", encoding="utf-8", newline="\n")
(r / "AGENTS.md").write_text("# charter\n", encoding="utf-8", newline="\n")
(r / "src" / "app.py").write_text("# app\n", encoding="utf-8", newline="\n")
(r / "keep.txt").write_text("a\nb\n", encoding="utf-8", newline="\n")
for f in ("drift_report.py", "drift_signals.template.py"):
    shutil.copyfile(kit / f, r / kit.name / f)
(r / kit.name / "drift_signals.py").write_text(
    "PRODUCT_GLOBS = ['src']\nSHRINK_ONLY = {'keep.txt': 'shrinks'}\nHANDKEPT = []\nPINS = {}\n",
    encoding="utf-8", newline="\n")
env = dict(os.environ, GOV_DEFAULT_BRANCH="main")
for cmd in (["git", "init", "-q", "-b", "main"], ["git", "config", "user.email", "h@x"],
            ["git", "config", "user.name", "h"], ["git", "add", "-A"],
            ["git", "commit", "-q", "-m", "seed", "--no-verify"]):
    subprocess.run(cmd, cwd=r, check=True, env=env, capture_output=True)
t0 = time.time()
rep = st.report(r)
t1 = time.time()
st.SIGNAL_ORDER.update({n: i for i, n in enumerate(rep)})
import drift_report as dr
bad = []
for n in st.SIGNAL_ORDER:
    mine = st.read_one_signal(r, n)
    theirs = json.loads(json.dumps({k: rep[n].get(k) for k in mine}))
    if mine != theirs:
        bad.append(n)
        print("DIFFER", n)
t2 = time.time()
print("map %d for %d SIGNALS; report() %.1fs; %d in-process reads %.1fs; %d differ" % (
    len(st.SIGNAL_ORDER), len(dr.SIGNALS), t1 - t0, len(st.SIGNAL_ORDER), t2 - t1, len(bad)))
shutil.rmtree(tmp, ignore_errors=True)
sys.exit(1 if bad or len(st.SIGNAL_ORDER) != len(dr.SIGNALS) else 0)
PY
  "$PY" -B -c "$ONESIG" "$GOV/tools/drift-audit" "$W" > "$W/onesig.out" 2>&1
  check_step $? "AC4 on a hand-built repository: $(tail -1 "$W/onesig.out")"
;; esac

echo "direct checks: $fails failing"
[ "$fails" = 0 ]
