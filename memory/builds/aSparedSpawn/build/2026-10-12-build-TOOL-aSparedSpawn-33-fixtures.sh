#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-33
# Direct fixtures for TOOL-aSparedSpawn-33 AC1 to AC5, over a kit source tree:
#   fx.sh <kit tree> <label>
# <kit tree> holds .githooks/pre-push and tools/run-gates/{run-gates.sh,gate-fingerprint.sh,gate-profiles.txt}.
# Every remote is a local bare repository under a scratch dir; nothing reaches a real remote.
# Each criterion prints one `<AC> GREEN|RED — <what>` line; the evidence lines follow it, indented.
set -u
KT=$(cd "$1" && pwd); LABEL=$2
T=$(mktemp -d "${TMPDIR:-/tmp}/u33fx.XXXXXX")
export GATE_TURNSTILE_DIR="$T/turnstile" GATE_TURNSTILE=0 GATE_MEMPAUSE=0 GOV_RUNLOG=0 GOV_DEFAULT_BRANCH=main
export GATE_PROFILE=minimal GATE_WALL=0
unset GOV_GATE_CMD GOV_GATE_CMD_TEST GATE_FULL GATE_REUSE GATE_REUSE_PUSH GATE_REUSE_LINEAGE GATE_REUSE_DIGEST_ENV GATE_LEGS GATE_BASE LC_CTYPE
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@e GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@e
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
say() { printf '%s\n' "$*"; }
ind() { sed 's/^/      /'; }
# The runner's PATH reading: each /bin component as /usr/bin where the two are one directory.
canon() { local p=":$1:" b=:/bin: u=:/usr/bin:; if [ /bin -ef /usr/bin ]; then while [[ $p == *"$b"* ]]; do p=${p//"$b"/"$u"}; done; fi; p=${p#:}; printf '%s' "${p%:}"; }
echo "== $LABEL · kit tree $KT · scratch $T"
want() { case " ${FX_ONLY:-dg sv ru} " in *" $1 "*) return 0 ;; esac; return 1; }
new_fixture() { # dir -> a work clone at $1/work, hooked by a copy of the hook, origin a bare repo
  mkdir -p "$1/hooks"; cp "$KT/.githooks/pre-push" "$1/hooks/pre-push"
  git init -q --template= --bare "$1/remote.git"; git init -q --template= "$1/work"
  cd "$1/work" || exit 2
  git config core.hooksPath "$1/hooks"
}

# ------------------------------------------------- hook + real runner: AC1 and AC3
if want dg; then
D="$T/dg"; new_fixture "$D"
mkdir -p run-gates fx ga gb
cp "$KT/tools/run-gates/run-gates.sh" "$KT/tools/run-gates/gate-fingerprint.sh" "$KT/tools/run-gates/gate-profiles.txt" run-gates/
export DG_GEP="$T/dg.gep"
printf '#!/usr/bin/env bash\nprintf "%%s\\n" "${GIT_EXEC_PATH-unset}" > "$DG_GEP"\n' > fx/a.sh
printf '#!/usr/bin/env bash\necho r\n' > fx/r.sh
echo x > ga/f; echo y > gb/f
printf '%s\n' '[' '  {"name": "pa", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"]},' \
  '  {"name": "pr", "argv": ["bash", "fx/r.sh"], "guard": ["gb/"], "reads": {"remote": "fixture"}}' ']' > gate-legs.json
git add -A; git commit -q -m init; git branch -M main; git remote add origin "$D/remote.git"
DG=$(cd "$(git rev-parse --git-dir)" && pwd); touch "$DG/push-main-active"
o=$(git push origin main 2>&1); say "   push 1: rc $? · $(printf '%s\n' "$o" | grep -m1 'gate on main push' | cut -c1-140)"
# The entry, earned by a DIRECT bar from this plain shell at the very commit the push then sends: a
# remote leg is keyed on HEAD. Both guards move past the scoped base here, so the push's guard pass
# runs both legs rather than skipping them as unchanged.
echo x2 > ga/f; echo y2 > gb/f; git add -A; git commit -q -m earn
RE=$(git hash-object -t tree /dev/null)
# The direct bar stamps its own full green, which would cover the push and run no bar at all; push 1's
# stamp is put back, so the push is scoped against the remote's commit.
cp "$DG/gate-full-green" "$T/dg.green1"
GATE_BASE="$RE" bash run-gates/run-gates.sh > "$T/dg.direct" 2>&1; say "   direct bar rc $? · cache entries $(find "$DG/gate-cache" -mindepth 2 -type f 2>/dev/null | grep -c .)"
cp "$T/dg.green1" "$DG/gate-full-green"
grep '^GATE ' "$T/dg.direct" | ind
rm -f "$DG_GEP"
o=$(git push origin main 2>&1); rc=$?
d=$(printf '%s\n' "$o" | grep -m1 'gate on main push')
say "   push 2: rc $rc · ${d:0:220}"
printf '%s\n' "$o" | grep -E '^GATE |not honoured|reuse' | ind
case "$d" in *"scoped gate"*"reuse offered"*) ;; *) say "AC1 RED — push 2 was not a scoped decision offering reuse, so the arm proves nothing" ;; esac
if printf '%s\n' "$o" | grep -qE '^GATE reuse +pr|^GATE ok +pr.*sampled against a cached ok'; then
  say "AC1 GREEN — the push bar met the direct bar's entry for the remote leg (reused, or drawn by the sample against it)"
else say "AC1 RED — the push bar executed the remote leg pr with no cached ok under its key"; fi
g=""; [ -f "$DG_GEP" ] && IFS= read -r g < "$DG_GEP"
case "$g" in ""|unset) say "AC3 RED — leg pa saw GIT_EXEC_PATH '${g:-not run}' during the push" ;;
  *) say "AC3 GREEN — leg pa saw GIT_EXEC_PATH=$g during the push, so the legs kept the hook's environment" ;; esac
cd "$T" || exit 2
fi

# ------------------------------------------------- hook + stub bar copying the view: AC2 and AC4
if want sv; then
S="$T/sv"; new_fixture "$S"
git commit -q --allow-empty -m init; git branch -M main; git remote add origin "$S/remote.git"
SG=$(cd "$(git rev-parse --git-dir)" && pwd); touch "$SG/push-main-active"
printf '#!/usr/bin/env bash\nrm -f "$SV_COPY"\n[ -n "${GATE_REUSE_DIGEST_ENV:-}" ] && cp "$GATE_REUSE_DIGEST_ENV" "$SV_COPY"\nexit 0\n' > "$S/stub.sh"
export SV_COPY="$T/sv.copy"
GOV_GATE_CMD_TEST=1 GOV_GATE_CMD="bash $S/stub.sh" git push -q origin main >/dev/null 2>&1
run_sv() { # push-side words... -> the push output in $T/sv.out
  printf 'sha\t%s\nreused\t0\nreused_cache\t0\n' "$(git rev-parse HEAD)" > "$SG/gate-full-green"
  git commit -q --allow-empty -m "sv $RANDOM"
  env GOV_GATE_CMD_TEST=1 GOV_GATE_CMD="bash $S/stub.sh" "$@" push origin main > "$T/sv.out" 2>&1
}
caller_path=$(canon "$PATH")
run_sv git -c fx.knob=1
say "   push: $(grep -m1 'gate on main push' "$T/sv.out" | cut -c1-200)"
if [ ! -f "$SV_COPY" ]; then say "AC2 RED — the stub found no GATE_REUSE_DIGEST_ENV file to copy"
else
  bad=$(grep -E '^env (GIT_EXEC_PATH|GIT_PREFIX|GIT_CONFIG_PARAMETERS|LC_CTYPE)=' "$SV_COPY")
  vpath=$(sed -n 's/^env PATH=//p' "$SV_COPY")
  if [ -z "$bad" ] && [ "$(canon "$vpath")" = "$caller_path" ]; then
    say "AC2 GREEN — the view holds no git addition and no LC_CTYPE (caller's unset), and its PATH is the caller's under the /bin reading"
  else say "AC2 RED — additions: [${bad//$'\n'/; }] · PATH equal: $([ "$(canon "$vpath")" = "$caller_path" ] && echo yes || echo no)"; fi
  say "      view lines $(grep -c . "$SV_COPY"), names: $(sed 's/^env \([^=]*\)=.*/\1/' "$SV_COPY" | tr '\n' ' ')"
  [ "$vpath" = "$PATH" ] || say "      raw view PATH differs from the caller's before the /bin reading, as measured: $(diff <(tr ':' '\n' <<<"$PATH") <(tr ':' '\n' <<<"$vpath") | grep '^[<>]' | sort | uniq -c | tr '\n' ' ')"
fi
run_sv env LC_CTYPE=en_US.UTF-8 git
if grep -qx 'env LC_CTYPE=en_US.UTF-8' "$SV_COPY" 2>/dev/null; then say "AC2 GREEN — the caller's own LC_CTYPE=en_US.UTF-8 stays in the view"
else say "AC2 RED — the caller's LC_CTYPE=en_US.UTF-8 was dropped: $(grep LC_ "$SV_COPY" 2>/dev/null)"; fi
run_sv env GATE_REUSE_DIGEST_ENV="$T/planted.view" git
l=$(grep -m1 'not honoured from the environment by this bar:' "$T/sv.out")
case "$l" in *GATE_REUSE_DIGEST_ENV*) say "AC4 GREEN — an exported GATE_REUSE_DIGEST_ENV is named as not honoured" ;;
  *) say "AC4 RED — the not-honoured line does not name it: '${l:-none}'" ;; esac
[ -n "$l" ] && say "      $l"
left=$(ls "$SG"/gate-reuse-view.* 2>/dev/null)
[ -z "$left" ] && say "   no view file is left in the git dir after the pushes" || say "   RED — a view file was left behind: $left"
cd "$T" || exit 2
fi

# ------------------------------------------------- the runner, direct: AC5 and S3's push read
if want ru; then
R="$T/ru"; mkdir -p "$R/run-gates" "$R/fx" "$R/ga" "$R/gb"
cp "$KT/tools/run-gates/run-gates.sh" "$KT/tools/run-gates/gate-fingerprint.sh" "$KT/tools/run-gates/gate-profiles.txt" "$R/run-gates/"
cd "$R" || exit 2
git init -q --template= -b main .
printf '#!/usr/bin/env bash\necho a\n' > fx/a.sh; printf '#!/usr/bin/env bash\necho r\n' > fx/r.sh
echo x > ga/f; echo y > gb/f
printf '%s\n' '[' '  {"name": "pa", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"]},' \
  '  {"name": "pr", "argv": ["bash", "fx/r.sh"], "guard": ["gb/"], "reads": {"remote": "fixture"}}' ']' > gate-legs.json
git add -A; git commit -qm seed
git init -q --template= --bare "$R.origin.git"; git remote add origin "$R.origin.git"; git push -q origin main 2>/dev/null
RE=$(git hash-object -t tree /dev/null)
run_ru() { env GATE_BASE="$RE" GATE_REUSE_SAMPLE=0 "$@" bash run-gates/run-gates.sh > "$T/ru.out" 2> "$T/ru.err"; }
run_ru; say "   earning bar rc $? · cache entries $(find .git/gate-cache -mindepth 2 -type f 2>/dev/null | grep -c .)"
printf 'env PATH=/nowhere\nenv GATE_ALTERED=1\n' > "$T/altered.view"
run_ru GATE_REUSE=1 GATE_REUSE_DIGEST_ENV="$T/altered.view"
if grep -q '^GATE reuse pa' "$T/ru.out"; then say "AC5 GREEN — GATE_REUSE=1 with a view file of altered lines still reuses the plain bar's entry"
else say "AC5 RED — the env mode read the view file"; fi
grep '^GATE ' "$T/ru.out" | ind
git ls-remote --heads origin > "$T/adv"; tip=$(awk -F'\t' '$2 == "refs/heads/main" { print $1 }' "$T/adv"); dig=$(git hash-object --stdin < "$T/adv")
push="$(git rev-parse HEAD) $tip $dig"
run_ru GATE_REUSE_PUSH="$push"
grep -q '^GATE reuse pr' "$T/ru.out" && say "   control GREEN — push mode with no view reuses pr on this shell's environment" || say "   control RED — push mode with no view executed pr"
run_ru GATE_REUSE_PUSH="$push" GATE_REUSE_DIGEST_ENV="$T/altered.view"
grep -qE '^GATE ok +pr' "$T/ru.out" && ! grep -q '^GATE reuse' "$T/ru.out" \
  && say "S3 GREEN — push mode keys on the view file: altered lines execute pr" || say "S3 RED — push mode ignored the view file"
grep '^GATE ' "$T/ru.out" | ind
run_ru GATE_REUSE_PUSH="$push" GATE_REUSE_DIGEST_ENV="$T/missing.view"
grep -q 'could not be measured (the toolchain digest)' "$T/ru.err" && ! grep -q '^GATE reuse' "$T/ru.out" \
  && say "S3 GREEN — a missing view file empties the digest, says so, and reuses nothing" || say "S3 RED — a missing view file did not fail the digest"
grep 'reuse' "$T/ru.err" | ind
cd "$T" || exit 2
fi
echo "kept $T"
