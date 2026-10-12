#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-16
# The direct checks TOOL-aSparedSpawn-16's pass ran. Usage: bash <this> reuse|contended|push <tree>
#
#   reuse <tree>      a hand-built two-leg repo carrying <tree>'s tools/run-gates and tools/lib: the
#                     entry's count field (S11, AC12), the K2 dirty execution leaving K1's count, the
#                     aged and sampled tails (S17, AC18), the nondeterministic red's `log:` file (S16,
#                     AC17) and a `git` that fails `hash-object` (S18, AC19).
#   contended <file>  arm 9f's spinner and contended legs under runner <file>, then whether each leg's
#                     key holds a cache entry (S13, AC14); run over a copy whose cache writer reads
#                     `.retry.rc` to see the arm's assertion red.
#   push <tree>       <tree>'s .githooks/pre-push in a scratch clone pushing to a local bare remote,
#                     a stub bar recording the two reuse seams (S6, AC6).
# Run once over the changed tree and once over `git show <base>:` copies of the same files. No step
# runs a suite, a slice of one, or the tree's bar.
set -u
case=${1:-}; SRC=${2:-}
[ -n "$SRC" ] || { echo "usage: $0 reuse|contended|push <tree or runner file>"; exit 2; }
HERE_SRC=$(cd "$(dirname "$0")/../../../.." && pwd)
T=$(mktemp -d); OUT="$T.out"
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@example.com GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@example.com
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
say() { printf '%-58s %s\n' "$1" "$2"; }

if [ "$case" = reuse ]; then
  mkdir -p "$T/tools/run-gates" "$T/tools/lib" "$T/fx" "$T/ga" "$T/gb"
  cp "$SRC/tools/run-gates/run-gates.sh" "$SRC/tools/run-gates/gate-fingerprint.sh" "$SRC/tools/run-gates/gate-profiles.txt" "$T/tools/run-gates/"
  cp "$SRC/tools/lib/resolve-python.sh" "$T/tools/lib/"
  ( cd "$T" && git init -q --template= -b main . )
  printf '#!/usr/bin/env bash\necho a\nexit 0\n' > "$T/fx/a.sh"; printf '#!/usr/bin/env bash\necho b\nexit 0\n' > "$T/fx/b.sh"
  echo x > "$T/ga/f"; echo y > "$T/gb/f"
  ND="$T.nd"
  write_legs() { printf '[\n  {"name": "pa", "argv": %s, "guard": ["ga/"]},\n  {"name": "pb", "argv": ["bash", "fx/b.sh"], "guard": ["gb/"]}\n]\n' "$1" > "$T/tools/gate-legs.json"; ( cd "$T" && git add -A && git commit -qm legs ) >/dev/null 2>&1; }
  write_legs '["bash", "fx/a.sh"]'
  ( cd "$T" && git remote add origin "$T.origin.git" && git update-ref refs/remotes/origin/main HEAD && git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main ) >/dev/null 2>&1
  GD="$T/.git"; E=$(git -C "$T" hash-object -w -t tree /dev/null)
  bar() { ( cd "$T" && env -u GATE_FULL -u GATE_REUSE -u GATE_REUSE_PUSH -u GATE_REUSE_DAY -u GATE_LEGS GATE_BASE="$E" GATE_REUSE_SAMPLE=0 "$@" bash tools/run-gates/run-gates.sh >"$OUT" 2>&1; echo $? ); }
  read_key() { local c=""; IFS= read -r c < "$GD/gate-run/current"; awk -F'\t' -v n="$1" '$1 == n { print $7; exit }' "$GD/gate-run/$c"/[0-9]*.leg 2>/dev/null; }
  write_count() { awk -F'\t' -v OFS='\t' -v c="$2" '{ $6 = c; print }' "$1" > "$1.n" && mv -f "$1.n" "$1"; }
  bar >/dev/null; K=$(read_key pa); ENT="$GD/gate-cache/${K:0:2}/$K"
  say "earned entry" "$(awk -F'\t' '{ print NF " fields, count " $6 }' "$ENT")"
  bar GATE_REUSE=1 >/dev/null
  say "after one reuse" "$(awk -F'\t' '{ print NF " fields, count " $6 }' "$ENT")"
  say "a reuse run's record holds a pa row" "[$(read_key pa)]"
  write_count "$ENT" 9
  echo k2 > "$T/ga/k2"; bar GATE_REUSE=1 >/dev/null; say "K2, a dirty tree's key: pa" "$(grep '^GATE [a-zA-Z]* *pa' "$OUT")"
  rm -f "$T/ga/k2"; bar GATE_REUSE=1 >/dev/null; say "back on K1: pa" "$(grep '^GATE [a-zA-Z]* *pa' "$OUT")"
  bar GATE_REUSE=1 >/dev/null; say "the next K1 run: pa" "$(grep '^GATE [a-zA-Z]* *pa' "$OUT")"
  say "  its age line" "$(grep -c 'pa was reused on 10 runs in a row' "$OUT")"
  bar GATE_REUSE=1 GATE_REUSE_SAMPLE=1 >/dev/null; say "a sampled run: pa" "$(grep '^GATE [a-zA-Z]* *pa' "$OUT")"
  write_legs "[\"bash\", \"-c\", \"if [ -e '$ND' ]; then rm -f '$ND'; exit 0; fi; : > '$ND'; exit 1\"]"
  : > "$ND"; bar >/dev/null
  rm -f "$ND"; rc=$(bar GATE_REUSE=1 GATE_REUSE_SAMPLE=1)
  say "red then green: rc, nondeterministic lines" "$rc, $(grep -c '^nondeterministic · pa$' "$OUT")"
  say "  its FAIL line" "$(grep '^GATE FAIL  pa' "$OUT")"
  LF=$(sed -n 's/^    log: //p' "$GD/gate-last-failure.txt" | head -1); L1=""
  case "$LF" in ''|/*|?:/*) ;; *) LF="$T/$LF" ;; esac
  [ -n "$LF" ] && IFS= read -r L1 < "$LF"
  say "  the log: file's first line" "[$L1]"
  rm -f "$ND"
  write_legs '["bash", "fx/a.sh"]'
  mkdir -p "$T.bin"; printf '#!/usr/bin/env bash\ncase " $* " in *" hash-object "*) exit 1 ;; esac\nexec "%s" "$@"\n' "$(type -P git)" > "$T.bin/git"; chmod +x "$T.bin/git"
  bar GATE_REUSE=1 PATH="$T.bin:$PATH" >/dev/null; say "no hash-object, a reusing bar" "$(grep -c 'the input keys could not be measured (the toolchain digest)' "$OUT")"
  bar PATH="$T.bin:$PATH" >/dev/null; say "no hash-object, a clean plain bar (a write is due)" "$(grep -c 'could not be measured' "$OUT")"
  echo k3 > "$T/ga/k3"; bar PATH="$T.bin:$PATH" >/dev/null; say "no hash-object, a dirty plain bar (nothing due)" "$(grep -c 'could not be measured' "$OUT")"
  rm -rf "$T.bin" "$ND"
elif [ "$case" = contended ]; then
  F="$T.flag"; mkdir -p "$F" "$T/tools/run-gates" "$T/tools/lib" "$T/fx"
  cp "$SRC" "$T/tools/run-gates/run-gates.sh"
  cp "$HERE_SRC/tools/run-gates/gate-fingerprint.sh" "$HERE_SRC/tools/run-gates/gate-profiles.txt" "$T/tools/run-gates/"
  cp "$HERE_SRC/tools/lib/resolve-python.sh" "$T/tools/lib/"
  export HV_FLAG="$F/spinner"
  printf '#!/usr/bin/env bash\n: > "$HV_FLAG"\ni=0; while [ ! -f "$HV_FLAG.hung" ] && [ "$i" -lt 600 ]; do sleep 0.1; i=$((i + 1)); done\nsleep 3\nrm -f "$HV_FLAG"\n: > "$HV_FLAG.done"\n' > "$T/fx/spin.sh"
  printf '#!/usr/bin/env bash\nwhile [ ! -f "$HV_FLAG" ] && [ ! -f "$HV_FLAG.done" ]; do sleep 0.1; done\nif [ -f "$HV_FLAG" ]; then : > "$HV_FLAG.hung"; sleep 60; fi\nexit 0\n' > "$T/fx/contended.sh"
  printf '[{"name": "spinner", "argv": ["bash", "fx/spin.sh"]},\n {"name": "contended", "argv": ["bash", "fx/contended.sh"], "ceiling": 2}]\n' > "$T/tools/gate-legs.json"
  ( cd "$T" && git init -q --template= -b main . && git add -A && git commit -qm base ) >/dev/null 2>&1
  ( cd "$T" && env GATE_FULL= GATE_BASE= GATE_REUSE= GATE_WALL= GATE_SELFTESTS= GATE_ATTRIBUTE= GATE_RUN_ID= GATE_PROFILES= \
      GATE_JOBS=4 GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_REUSE_SAMPLE=0 GATE_REUSE_PUSH= bash tools/run-gates/run-gates.sh > "$OUT" 2>&1 )
  grep '^GATE' "$OUT"
  rec=$(ls -1td "$T"/.git/gate-run/*/ | head -1)
  k=$(cut -f7 "${rec}1.leg"); sk=$(cut -f7 "${rec}0.leg")
  say "contended entry" "$([ -e "$T/.git/gate-cache/${k:0:2}/$k" ] && echo written || echo absent)"
  say "spinner entry" "$([ -e "$T/.git/gate-cache/${sk:0:2}/$sk" ] && echo written || echo absent)"
  rm -rf "$F"
elif [ "$case" = push ]; then
  export GOV_DEFAULT_BRANCH=main GOV_GATE_CMD_TEST=1
  mkdir -p "$T/hooks"; cp "$SRC/.githooks/pre-push" "$T/hooks/pre-push"
  git init -q --template= --bare "$T/remote.git"; git init -q --template= "$T/work"
  cd "$T/work" || exit 2
  git config core.hooksPath "$T/hooks"
  git commit -q --allow-empty -m init; git branch -M main
  git remote add origin "$T/remote.git"
  gd=$(cd "$(git rev-parse --git-dir)" && pwd)
  touch "$gd/push-main-active"
  printf '#!/usr/bin/env bash\nexit 0\n' > "$T/green.sh"
  GOV_GATE_CMD="bash $T/green.sh" git push -q origin main >/dev/null 2>&1
  printf '#!/usr/bin/env bash\nprintf "%%s|%%s" "${GATE_REUSE_SAMPLE-unset}" "${GATE_REUSE_DAY-unset}" > "%s/seams"\nexit 0\n' "$T" > "$T/stub.sh"
  printf 'sha\t%s\n' "$(git rev-parse HEAD)" > "$gd/gate-full-green"
  git commit -q --allow-empty -m next
  printf 'none' > "$T/seams"
  o=$(env GOV_GATE_CMD="bash $T/stub.sh" GATE_REUSE_SAMPLE=0 GATE_REUSE_DAY=1 git push origin main 2>&1); rc=$?
  say "push rc" "$rc"
  say "not-honoured line" "$(printf '%s\n' "$o" | grep -m1 'not honoured from the environment by this bar:')"
  say "the stub bar saw SAMPLE|DAY" "$(cat "$T/seams")"
  cd / || exit 2
else
  echo "usage: $0 reuse|contended|push <tree or runner file>"; rm -rf "$T"; exit 2
fi
rm -rf "$T" "$OUT"
