#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-32
# Direct fixtures for TOOL-aSparedSpawn-32 AC7 to AC10 and AC12, over a kit source tree:
#   fx.sh <kit tree> <label>
# <kit tree> holds .githooks/pre-push and tools/run-gates/{run-gates.sh,gate-fingerprint.sh,gate-profiles.txt}.
# Every remote is a local bare repository under a scratch dir; nothing reaches a real remote.
# Each criterion prints one `<AC> GREEN|RED — <what>` line; the evidence lines follow it, indented.
set -u
KT=$(cd "$1" && pwd); LABEL=$2
T=$(mktemp -d "${TMPDIR:-/tmp}/u32fx.XXXXXX")
export GATE_TURNSTILE_DIR="$T/turnstile" GATE_MEMPAUSE=0 GOV_RUNLOG=0 GOV_DEFAULT_BRANCH=main
unset GOV_GATE_CMD GOV_GATE_CMD_TEST GATE_FULL GATE_REUSE GATE_REUSE_PUSH GATE_REUSE_LINEAGE GATE_LEGS GATE_BASE
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@e GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@e
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
say() { printf '%s\n' "$*"; }
ind() { sed 's/^/      /'; }
echo "== $LABEL · kit tree $KT · scratch $T"
want() { case " ${FX_ONLY:-ru lin rp} " in *" $1 "*) return 0 ;; esac; return 1; }

# ---------------------------------------------------------------- runner fixture (AC9 AC10 AC12)
if want ru; then
R="$T/ru"; mkdir -p "$R/run-gates" "$R/fx" "$R/ga" "$R/gb"
cp "$KT/tools/run-gates/run-gates.sh" "$KT/tools/run-gates/gate-fingerprint.sh" "$KT/tools/run-gates/gate-profiles.txt" "$R/run-gates/"
( cd "$R" && git init -q --template= -b main . )
printf '#!/usr/bin/env bash\necho a\n' > "$R/fx/a.sh"; printf '#!/usr/bin/env bash\necho b\n' > "$R/fx/b.sh"
echo x > "$R/ga/f"; echo y > "$R/gb/f"
printf '%s\n' '[' '  {"name": "pa", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"]},' \
  '  {"name": "pb", "argv": ["bash", "fx/b.sh"], "guard": ["gb/"]}' ']' > "$R/gate-legs.json"
( cd "$R" && git add -A && git commit -qm seed && git remote add origin "$R.origin.git" \
    && git update-ref refs/remotes/origin/main HEAD && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main )
RE=$(git -C "$R" hash-object -w -t tree /dev/null)
run_ru() { ( cd "$R" && env GATE_BASE="$RE" GATE_REUSE_SAMPLE=0 GATE_PROFILE=minimal GATE_WALL=0 "$@" bash run-gates/run-gates.sh > "$T/ru.out" 2> "$T/ru.err"; echo $? ); }
read_reuse() { local c=""; IFS= read -r c < "$R/.git/gate-run/current"; awk -F'\t' '$1 == "reuse" { printf "%s%s", s, $2; s="," }' "$R/.git/gate-run/$c/header"; }

rc=$(run_ru); say "   earning bar rc=$rc · cache entries $(find "$R/.git/gate-cache" -mindepth 2 -type f 2>/dev/null | grep -c .)"
# AC9
rc=$(run_ru GATE_REUSE=1); h=$(read_reuse)
if grep -q '^GATE reuse pa' "$T/ru.out" && [ "$h" = env ]; then say "AC9 GREEN — GATE_REUSE=1 prints GATE reuse pa and the header records reuse env"
else say "AC9 RED — GATE_REUSE=1: header reuse '$h'"; fi
grep '^GATE ' "$T/ru.out" | ind
# AC10: the cache holds ok for pa (written above); the ledger rows carry an empty full.
say "   ledger full fields: $(cut -f7 "$R/.git/gate-ledger.tsv" | tr '\n' '|')"
rc=$(run_ru GATE_FULL=1 GATE_REUSE_LINEAGE=1); h=$(read_reuse)
if grep -q '^GATE ok    pa' "$T/ru.out" && ! grep -q '^GATE reuse' "$T/ru.out" && [ "$h" = lineage ]; then
  say "AC10 GREEN — GATE_FULL=1 GATE_REUSE_LINEAGE=1 executes pa over a cached ok and records reuse lineage"
else say "AC10 RED — the lineage run: header reuse '$h'"; fi
grep '^GATE ' "$T/ru.out" | ind
# AC12
rc=$(run_ru GATE_FULL=1 GATE_REUSE=1 GATE_REUSE_LINEAGE=1); h=$(read_reuse)
if [ "$h" = lineage ] && grep -q 'not used: GATE_REUSE$' "$T/ru.err"; then
  say "AC12 GREEN — full + both knobs: header reuse lineage, stderr names GATE_REUSE as not used"
else say "AC12 RED — full + both knobs: header reuse '$h'"; fi
grep 'reuse' "$T/ru.err" | ind
rc=$(run_ru GATE_REUSE=1 GATE_REUSE_LINEAGE=1); h=$(read_reuse)
if [ "$h" = env ] && grep -q 'GATE_REUSE_LINEAGE is not used' "$T/ru.err"; then
  say "AC12 GREEN — no full + both knobs: header reuse env, stderr names GATE_REUSE_LINEAGE"
else say "AC12 RED — no full + both knobs: header reuse '$h'"; fi
grep 'reuse' "$T/ru.err" | ind
fi

# ---------------------------------------------------------------- hook fixture, real runner (AC7)
if want lin; then
L="$T/lin"; mkdir -p "$L/hooks"; cp "$KT/.githooks/pre-push" "$L/hooks/pre-push"
git init -q --template= --bare "$L/remote.git"; git init -q --template= "$L/work"
cd "$L/work" || exit 2
git config core.hooksPath "$L/hooks"
mkdir -p run-gates fx ga gb
cp "$KT/tools/run-gates/run-gates.sh" "$KT/tools/run-gates/gate-fingerprint.sh" "$KT/tools/run-gates/gate-profiles.txt" run-gates/
printf '#!/usr/bin/env bash\necho a\n' > fx/a.sh; printf '#!/usr/bin/env bash\ngrep -q fixed gb/f\n' > fx/b.sh
printf '#!/usr/bin/env bash\necho u\n' > fx/u.sh
echo x > ga/f; echo broken > gb/f
printf '%s\n' '[' '  {"name": "pa", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"]},' \
  '  {"name": "pb", "argv": ["bash", "fx/b.sh"], "guard": ["gb/"]},' '  {"name": "pu", "argv": ["bash", "fx/u.sh"]}' ']' > gate-legs.json
git add -A; git commit -q -m init; git branch -M main; git remote add origin "$L/remote.git"
LG=$(cd "$(git rev-parse --git-dir)" && pwd); touch "$LG/push-main-active"
run_lin() { env GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_WALL=0 "$@" git push -q origin main 2>&1; }
o1=$(run_lin); say "   push 1 (red): $(printf '%s\n' "$o1" | grep -m1 'gate on main push' | cut -c1-160)"
echo fixed > gb/f; git add -A; git commit -q -m fix
o2=$(run_lin); say "   push 2 (fix): $(printf '%s\n' "$o2" | grep -m1 'gate on main push' | cut -c1-160)"
printf '%s\n' "$o2" | grep -E '^GATE |not honoured' | ind
say "   stamp after push 2: $(tr '\t\n' '= ' < "$LG/gate-full-green" 2>/dev/null | cut -c1-400)"
echo after > after.txt; git add after.txt; git commit -q -m next
o3=$(run_lin); d3=$(printf '%s\n' "$o3" | grep -m1 'gate on main push')
case "$d3" in
  *"FULL gate"*"reused"*) say "AC7 RED — the push after a lineage green is forced FULL by its reused field" ;;
  *"FULL gate"*) say "AC7 RED — the push after the fix push is FULL for another reason" ;;
  *"scoped gate"*) say "AC7 GREEN — the push after a lineage green (reused >0, reused_cache 0) is scoped, no reused force" ;;
  *) say "AC7 RED — no decision line" ;;
esac
say "      $d3" | cut -c1-300
fi

# ---------------------------------------------------------------- hook fixture, stub bar (AC8)
if want rp; then
P="$T/rp"; mkdir -p "$P/hooks"; cp "$KT/.githooks/pre-push" "$P/hooks/pre-push"
git init -q --template= --bare "$P/remote.git"; git init -q --template= "$P/work"
cd "$P/work" || exit 2
git config core.hooksPath "$P/hooks"
git commit -q --allow-empty -m init; git branch -M main; git remote add origin "$P/remote.git"
PG=$(cd "$(git rev-parse --git-dir)" && pwd); touch "$PG/push-main-active"
printf '#!/usr/bin/env bash\nexit 0\n' > "$P/stub.sh"
GOV_GATE_CMD_TEST=1 GOV_GATE_CMD="bash $P/stub.sh" git push -q origin main >/dev/null 2>&1
run_rp() { # extra stamp lines -> the decision line
  printf 'sha\t%s\n%s' "$(git rev-parse HEAD)" "$1" > "$PG/gate-full-green"
  git commit -q --allow-empty -m "rp $RANDOM"
  env GOV_GATE_CMD_TEST=1 GOV_GATE_CMD="bash $P/stub.sh" git push origin main 2>&1 | grep -m1 'gate on main push'
}
d=$(run_rp $'reused\t0\nreused_cache\t1\n')
case "$d" in *"FULL gate"*reused*) say "AC8 GREEN — a stamp with reused_cache 1 forces FULL naming reused" ;; *) say "AC8 RED — a stamp with reused_cache 1 was trusted" ;; esac
say "      $d" | cut -c1-300
d=$(run_rp $'reused\t2\n')
case "$d" in *"FULL gate"*reused*) say "AC8 GREEN — a stamp with reused 2 and no reused_cache forces FULL naming reused" ;; *) say "AC8 RED — an unlabelled reused 2 stamp was trusted" ;; esac
say "      $d" | cut -c1-300
d=$(run_rp $'reused\t2\nreused_cache\t0\n')
case "$d" in *"scoped gate"*) say "   control GREEN — a lineage stamp, reused 2 and reused_cache 0, scopes" ;; *) say "   control RED — a lineage stamp was refused" ;; esac
say "      $d" | cut -c1-300
fi
echo "kept $T"
