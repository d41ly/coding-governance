#!/usr/bin/env bash
# pre-push.runlog.test.sh — the pre-push hook's run-log lines, observed from OUTSIDE the hook.
#
#   bash .githooks/pre-push.runlog.test.sh                         # every arm, against the floor
#   PPRL_ARMS="AC3 CAP" bash .githooks/pre-push.runlog.test.sh     # the named arms only, no floor
#   PPRL_BEFORE=<a hook> bash .githooks/pre-push.runlog.test.sh    # AC7 against a named baseline
#
# TOOL-dLoggedFlight-4. Every push the hook sees writes to `runlog/pushes.log` under the git common
# dir: a START after its ref loop and an END from its EXIT trap, or one `ev=once` line for a refusal
# that comes before that loop. Every arm drives a COPY of the hook beside this file in a scratch
# clone, through a real `git push` or by invoking it the way git does, and reads what it wrote. Nothing
# here reads or writes the journal of the clone this file lives in. The bar is a stub everywhere
# except AC4's second half, which runs a COPY of the real runner over one fixture leg.
#
# WITHHELD FROM ADOPTERS, AND HELD ON GOV'S BAR. Its subject is the hook beside it, which an adopter
# receives verbatim and never edits, so the push-main entry withholds this file with a
# `project-owned` rule and the deployer's registry carries its leg with an `[[exempt_leg]]` row, per
# TOOL-aQuenchedHarness-3. The sibling `pre-push.test.sh` still ships, and that is not this unit's.
#
# ONE ARM PER ACCEPTANCE CRITERION of the unit's spec, named by it:
#   AC1   a feature push, a marked green default-branch push and an unmarked one: three START and END
#         pairs with their decisions, rc, lander and refs; a refusal before the loop writes one line
#   AC2   a credentialed URL through a named remote, bare, typed and rewritten by `insteadOf`, and
#         refused before the loop: the remote fields S3 names, and no password on any line
#   AC3   TERM while the bar runs ends the hook with exit=unclean while the bar is still running
#   AC4   a stub bar sees GATE_RUN_ID equal to END's gate_run; a real runner copy writes run= that id,
#         and a leg of that bar sees no GATE_RUN_ID at all
#   AC5   a failed append leaves rc and stdout alone and says so once; GOV_RUNLOG=0 writes nothing
#   AC6   21 refs: ref.1 to ref.10, ref_more=11, and the line under the cap
#   AC7   the writer adds no external exec, from a linked worktree and from a primary clone, both
#         write the COMMON journal, and a clone's first push pays one mkdir
#   AC8   this suite's own declarations: withheld, budgeted, a held leg with a ceiling, an exempt row
#   DEC   the decisions AC1 does not reach: skip-delete, refuse-manifest, refuse-head, scoped, and the
#         other two refusals before the loop
#   CAP   a line over the cap is fitted exactly as the runlog kit's `render_line` fits it, both steps
#   EXITS every `exit` in the hook maps to a decision or a named exemption, every one after the trap
#         carries the clean-exit mark, and every decision was seen on a line (runs last for that)
#
# WHAT THIS DOES NOT CHECK. Whether a line MEANS anything past the fields named here: the run model is
# a later unit. The hook's gating decisions as such, which `pre-push.test.sh` grades. A KILL, which
# runs no trap. Wall time, except in AC3, whose verdict is "the bar was still running when the hook
# ended" and not a threshold. The lexer is a COPY of the one in the gate runner's run-log suite,
# changed to key a site on its CODE and not its comment, because kits do not source each other's
# tests; each copy is graded by its own staged arms.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$(cd "$HERE/.." && pwd)"
# Where this repository keeps its kits, the hook's own default. The suite never ships, so only gov's
# layout and a caller's override are ever asked for.
KIT_REL="${KIT_REL:-tools}"
FLOOR_ASSERTIONS=240
n=0; st=0
SEEN=" "; WRITER_FNS=""

# THE AMBIENT ENVIRONMENT IS CLEARED ONCE. A leg of the real bar inherits GATE_SELFTESTS, a push
# boundary exports GATE_BASE and GATE_FULL, and the hook reads the first in its decision while AC4's
# runner copy reads the rest: an inherited value would answer a question about the OUTER run, which is
# the class `inputs-inside-the-subjects-reach`. The default branch is pinned here and nowhere else.
unset GATE_BASE GATE_FULL GATE_REUSE GATE_JOBS GATE_PROFILES GATE_PROFILE GATE_RUN_ID GATE_SELFTESTS \
  GATE_WALL GATE_LEGS GATE_TURNSTILE GATE_TURNSTILE_HELD GATE_RUN_KEEP GOV_RUNLOG GOV_GATE_CMD \
  GOV_DEFAULT_BRANCH GIT_SSH_COMMAND PPRL_SEEN GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR \
  GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES GIT_NAMESPACE GIT_PREFIX
export GOV_DEFAULT_BRANCH=main

check() { # name · got · want
  n=$((n + 1))
  [ "$2" = "$3" ] && return 0
  echo "FAIL $1: expected [$3], got [$2]"; st=1; return 1
}

# An arm runs when no selection is made, or when the selection names it. A SELECTED run grades its
# arms and never the floor, and says so at its end rather than printing a PASS it did not earn.
check_selected() { # arm name -> 0 when it runs
  [ -z "${PPRL_ARMS:-}" ] && return 0
  case " $PPRL_ARMS " in *" $1 "*) return 0 ;; esac
  return 1
}

add_seen() { SEEN="$SEEN$1 "; }   # decision -> recorded as observed on a line this run wrote

# ------------------------------------------------------------------------------ the scratch clone
# A MISSING CAPABILITY IS A FAILURE HERE, not a skip: these arms are the only observation the writer
# has, and a suite that skipped them would print a count that proves nothing.
PY=""
if [ -f "$SRC/$KIT_REL/lib/resolve-python.sh" ]; then
  # shellcheck source=/dev/null
  . "$SRC/$KIT_REL/lib/resolve-python.sh"
  PY=$(resolve_python 2>/dev/null) || PY=""
fi
RUNLOG_KIT="$SRC/$KIT_REL/runlog"
RUNNER_KIT="$SRC/$KIT_REL/run-gates"
[ -n "$PY" ] && [ -f "$RUNLOG_KIT/runlog_lib.py" ] || {
  echo "FAIL no python, or no runlog kit under $KIT_REL: the journal cannot be graded, so nothing below can be"; exit 1; }
[ -f "$RUNNER_KIT/run-gates.sh" ] || { echo "FAIL no gate runner under $KIT_REL: AC4 cannot run its real bar"; exit 1; }
[ -f "$HERE/pre-push" ] || { echo "FAIL no hook beside this suite"; exit 1; }
WORK=$(mktemp -d 2>/dev/null) || { echo "FAIL no mktemp -d on this host"; exit 1; }
BG_PIDS=""
remove_scratch() {
  local p
  for p in $BG_PIDS; do kill "$p" 2>/dev/null; done
  cd / && rm -rf "$WORK"
}
trap remove_scratch EXIT
REPO="$WORK/work"
HOOK="$WORK/hooks/pre-push"
JOURNAL="$REPO/.git/runlog/pushes.log"
GATES="$REPO/.git/runlog/gates.log"
ZERO=0000000000000000000000000000000000000000

# The journal reader is the runlog kit's own library. Written to a FILE, never fed on stdin.
cat > "$WORK/jl.py" <<'PYEOF'
import json
import sys
sys.path.insert(0, sys.argv[1])
import runlog_lib as r

mode = sys.argv[2]
if mode == "grade":
    j = r.read_journal(sys.argv[3])
    orphan = sum(1 for x in r.build_invocations(j.lines) if x.state == "orphan-end")
    print(f"state={j.state} bad={j.bad} orphan={orphan}")
    for lineno, why in j.refusals[:3]:
        print(f"  refusal line {lineno}: {why}")
elif mode == "render":
    # ONE written START, rebuilt as the hook held it BEFORE the fit: its own fields in their order,
    # every ref line fed to it back in place under the count cap, and the uncut remote name when one is
    # given. The REFERENCE writer must fit that to the same bytes.
    # The count cap is the HOOK's, read from it by the caller and passed in, never a second copy here.
    raw = open(sys.argv[3], "rb").read().decode("utf-8").rstrip("\n")
    refs = [x for x in open(sys.argv[4], "rb").read().decode("utf-8").split("\n") if x]
    cap = int(sys.argv[6])
    fields = {}
    for part in raw.split("\t"):
        k, _, v = part.partition("=")
        fields[k] = r._parse_value(v)
    base = {k: v for k, v in fields.items() if not (k.startswith("ref.") or k == "ref_more")}
    if sys.argv[5] != "-":
        base["remote"] = open(sys.argv[5], "rb").read().decode("utf-8")
    for i, ref in enumerate(refs[:cap], 1):
        base[f"ref.{i}"] = ref
    if len(refs) > cap:
        base["ref_more"] = str(len(refs) - cap)
    same = r.render_line(base) == raw and r.check_line(raw) is None
    print(len(raw.encode("utf-8")), fields.get("ref_more", "-"), "SAME" if same else "DIFF")
elif mode == "legs":
    rows = [l for l in json.load(open(sys.argv[3], encoding="utf-8")) if l.get("name") == sys.argv[4]]
    ok = (len(rows) == 1 and rows[0]["argv"][-1].endswith("/pre-push.runlog.test.sh")
          and rows[0].get("chunk") == "selftests" and rows[0].get("subject") == "repo"
          and isinstance(rows[0].get("ceiling"), int) and rows[0]["ceiling"] > 0
          and ".githooks/" in rows[0].get("guard", []))
    print("declared" if ok else "not declared")
PYEOF

build_scratch() {
  mkdir -p "$WORK/hooks" || return 1
  cp "$HERE/pre-push" "$HOOK" || return 1
  git init -q --bare "$WORK/remote.git" || return 1
  git init -q -b main "$REPO" || return 1
  cd "$REPO" || return 1
  # autocrlf OFF: the global conf on a Windows node would check files out with CRLF in the linked
  # worktree AC7 makes. The hook itself is a copy, never a checkout.
  git config user.email t@t; git config user.name t; git config commit.gpgsign false
  git config core.autocrlf false; git config core.hooksPath "$WORK/hooks"
  git commit -q --allow-empty -m base || return 1
  git remote add origin "$WORK/remote.git" || return 1
  printf '#!/usr/bin/env bash\nexit 0\n' > "$WORK/green.sh"
  printf '#!/usr/bin/env bash\necho "FAKE LEG failed"\nexit 1\n' > "$WORK/red.sh"
  # Records what it was handed and nothing else: a stub bar in AC4's first half, a leg in its second.
  printf '#!/usr/bin/env bash\nprintf "%%s" "${GATE_RUN_ID-<unset>}" > "$PPRL_SEEN"\nexit 0\n' > "$WORK/idstub.sh"
  return 0
}

# One real push from the scratch clone, both streams into a FILE: a pipe would be held open by any
# child the hook leaves behind.
run_push() { # NAME=VALUE... -- push arguments -> PUSH_RC, PUSH_OUT
  local -a envs=()
  while [ "$#" -gt 0 ] && [ "$1" != -- ]; do envs+=("$1"); shift; done
  [ "$#" -gt 0 ] && shift
  env ${envs[@]+"${envs[@]}"} git push -q "$@" >"$WORK/push.out" 2>&1; PUSH_RC=$?
  PUSH_OUT=$(cat "$WORK/push.out")
}

# The hook invoked the way git invokes it: the remote's name and URL as its arguments, the ref lines
# on stdin, from the tree being pushed. Cheaper than a push, and able to feed lines no push would.
run_hook() { # ref-lines file · remote · url · NAME=VALUE... -> RC, OUT, ERR
  local refs=$1 a1=$2 a2=$3
  shift 3
  env "$@" bash "$HOOK" "$a1" "$a2" <"$refs" >"$WORK/hook.out" 2>"$WORK/hook.err"; RC=$?
  OUT=$(cat "$WORK/hook.out"); ERR=$(cat "$WORK/hook.err")
}

write_refs() { # file · ref line... -> the file, one line per argument
  local f=$1 r
  shift
  : > "$f"
  for r in "$@"; do printf '%s\n' "$r" >> "$f"; done
}

measure_lines() { # -> the journal's line count, 0 when it is absent
  if [ -f "$JOURNAL" ]; then wc -l < "$JOURNAL" | tr -d ' '; else echo 0; fi
}

read_line() { sed -n "${1}p" "$JOURNAL"; }   # line number -> that line, raw

read_field() { # line number · key -> the value as written, or the literal <absent>
  awk -F'\t' -v l="$1" -v k="$2" 'NR == l { for (i = 1; i <= NF; i++) if (index($i, k "=") == 1) { print substr($i, length(k) + 2); f = 1 } }
    END { if (!f) print "<absent>" }' "$JOURNAL"
}

check_journal() { # label -> the whole journal parses, pairs, and carries no password
  local got
  got=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" grade "$JOURNAL" | head -1)
  check "$1: the journal reads" "${got%% *}" state=read
  check "$1: no bad line in the journal" "$(printf '%s' "$got" | sed -n 's/.* \(bad=[0-9]*\) .*/\1/p')" bad=0
  check "$1: every END's nonce has its START" "${got##* }" orphan=0
  check "$1: no line of the whole journal carries the password" "$(grep -c pass "$JOURNAL")" 0
}

check_shape_run() { # value -> "shaped" when it is push-<digits>-<digits>, else the value in brackets
  case "$1" in push-*-*) ;; *) echo "[$1]"; return 0 ;; esac
  local mid=${1#push-} tail=${1##*-}
  mid=${mid%-*}
  case "$mid:$tail" in *[!0-9:]*|:*|*:) echo "[$1]" ;; *) echo shaped ;; esac
}

# ------------------------------------------------------------------------------------------ AC1
check_ac1_decisions() {
  local l0 l s1 s2 s3 top
  top=$(git rev-parse --show-toplevel)
  git checkout -q -b feature && git commit -q --allow-empty -m f1
  s1=$(git rev-parse HEAD)
  l0=$(measure_lines)
  run_push GOV_GATE_CMD="bash $WORK/red.sh" -- origin feature
  check "AC1 a feature push is not gated, so a red stub lets it through" "$PUSH_RC" 0
  git checkout -q main && git commit -q --allow-empty -m m1
  s2=$(git rev-parse HEAD)
  : > "$REPO/.git/push-main-active"
  run_push GOV_GATE_CMD="bash $WORK/green.sh" -- origin main
  check "AC1 a marked default-branch push with a green stub lands" "$PUSH_RC" 0
  rm -f "$REPO/.git/push-main-active"
  git commit -q --allow-empty -m m2
  s3=$(git rev-parse HEAD)
  run_push GOV_GATE_CMD="bash $WORK/green.sh" -- origin main
  check "AC1 an unmarked default-branch push is refused" "$PUSH_RC" 1
  check "AC1 three pushes, three START and END pairs" "$(( $(measure_lines) - l0 ))" 6
  # The feature push.
  l=$((l0 + 1))
  check "AC1 feature: its first line is a START" "$(read_field $l ev)" start
  check "AC1 feature: END pairs on START's nonce" "$(read_field $((l + 1)) n)" "$(read_field $l n)"
  check "AC1 feature: the ref line is recorded whole" "$(read_field $l ref.1)" "refs/heads/feature $s1 refs/heads/feature $ZERO"
  check "AC1 feature: no ref past the one pushed" "$(read_field $l ref.2)|$(read_field $l ref_more)" "<absent>|<absent>"
  check "AC1 feature: lander=0 is written, not omitted" "$(read_field $l lander)" 0
  check "AC1 feature: the remote's name" "$(read_field $l remote)" origin
  check "AC1 feature: a local path holds no userinfo" "$(read_field $l url_userinfo)" "<absent>"
  check "AC1 feature: the worktree" "$(read_field $l wt)" "$top"
  check "AC1 feature: decision" "$(read_field $((l + 1)) decision)" skip-nondefault
  check "AC1 feature: rc" "$(read_field $((l + 1)) rc)" 0
  check "AC1 feature: exit" "$(read_field $((l + 1)) exit)" clean
  check "AC1 feature: no bar ran, so no gate_run" "$(read_field $((l + 1)) gate_run)" "<absent>"
  [ "$(read_field $((l + 1)) decision)" = skip-nondefault ] && add_seen skip-nondefault
  # The marked, gated default-branch push.
  l=$((l0 + 3))
  check "AC1 full: END pairs on START's nonce" "$(read_field $((l + 1)) n)" "$(read_field $l n)"
  check "AC1 full: the ref line" "$(read_field $l ref.1)" "refs/heads/main $s2 refs/heads/main $ZERO"
  check "AC1 full: lander=1" "$(read_field $l lander)" 1
  check "AC1 full: decision, since no recorded green exists" "$(read_field $((l + 1)) decision)" full
  check "AC1 full: rc" "$(read_field $((l + 1)) rc)" 0
  check "AC1 full: exit" "$(read_field $((l + 1)) exit)" clean
  check "AC1 full: gate_run names a push-shaped run" "$(check_shape_run "$(read_field $((l + 1)) gate_run)")" shaped
  [ "$(read_field $((l + 1)) decision)" = full ] && add_seen full
  # The unmarked one.
  l=$((l0 + 5))
  check "AC1 raw: END pairs on START's nonce" "$(read_field $((l + 1)) n)" "$(read_field $l n)"
  check "AC1 raw: the ref line names what the remote held" "$(read_field $l ref.1)" "refs/heads/main $s3 refs/heads/main $s2"
  check "AC1 raw: lander=0" "$(read_field $l lander)" 0
  check "AC1 raw: decision" "$(read_field $((l + 1)) decision)" refuse-raw
  check "AC1 raw: rc" "$(read_field $((l + 1)) rc)" 1
  check "AC1 raw: exit" "$(read_field $((l + 1)) exit)" clean
  [ "$(read_field $((l + 1)) decision)" = refuse-raw ] && add_seen refuse-raw
  # A DEFAULT-BRANCH REFUSAL BEFORE THE LOOP: the environment names a default the clone does not
  # observe, which needs an observed one, so the remote's HEAD is set first.
  git remote set-head origin main >/dev/null 2>&1
  l0=$(measure_lines)
  run_push GOV_DEFAULT_BRANCH=feature GOV_GATE_CMD="bash $WORK/green.sh" -- origin main
  check "AC1 once: an env default the clone does not observe is refused" "$PUSH_RC" 1
  check "AC1 once: by the observed-default refusal" "$(printf '%s\n' "$PUSH_OUT" | grep -c 'does not observe as the default')" 1
  l=$(measure_lines)
  check "AC1 once: ONE line and no pair" "$((l - l0))" 1
  check "AC1 once: ev" "$(read_field $l ev)" once
  check "AC1 once: decision" "$(read_field $l decision)" refuse-default-branch
  check "AC1 once: the worktree" "$(read_field $l wt)" "$top"
  check "AC1 once: lander" "$(read_field $l lander)" 0
  check "AC1 once: the remote's name" "$(read_field $l remote)" origin
  check "AC1 once: no nonce, since it pairs with nothing" "$(read_field $l n)" "<absent>"
  [ "$(read_field $l decision)" = refuse-default-branch ] && add_seen refuse-default-branch
  check_journal AC1
}

# ------------------------------------------------------------------------------------------ AC2
# A CREDENTIALED URL THAT A PUSH CAN REALLY REACH. Git runs pre-push only after it has connected, so
# the URL must lead somewhere: `ssh://` through a stand-in for ssh that drops the destination and runs
# the remote command here. Git hands the hook the URL as configured, userinfo and all.
check_ac2_credentials() {
  local url l0 l
  cat > "$WORK/fakessh.sh" <<'EOF'
#!/usr/bin/env bash
# a stand-in for ssh: drop every option and the destination, run the remote command in this host
while [ "$#" -gt 1 ]; do shift; done
case "${1:-}" in
  git-receive-pack\ *) eval "git receive-pack ${1#git-receive-pack }" ;;
  git-upload-pack\ *)  eval "git upload-pack ${1#git-upload-pack }" ;;
  *) exit 97 ;;
esac
EOF
  url="ssh://user:pass@localhost$WORK/remote.git"
  git remote add cred "$url"
  git checkout -q -b cred-a main && git commit -q --allow-empty -m ca
  l0=$(measure_lines)
  run_push GIT_SSH_COMMAND="bash $WORK/fakessh.sh" -- cred cred-a
  check "AC2 the named credentialed remote is reached" "$PUSH_RC" 0
  l=$((l0 + 1))
  check "AC2 named: a START and an END" "$(( $(measure_lines) - l0 ))" 2
  check "AC2 named: remote is the name" "$(read_field $l remote)" cred
  check "AC2 named: the userinfo is flagged" "$(read_field $l url_userinfo)" 1
  check "AC2 named: not unnamed" "$(read_field $l remote_unnamed)" "<absent>"
  git checkout -q -b cred-b && git commit -q --allow-empty -m cb
  l0=$(measure_lines)
  run_push GIT_SSH_COMMAND="bash $WORK/fakessh.sh" -- "$url" cred-b
  check "AC2 the bare credentialed URL is reached" "$PUSH_RC" 0
  l=$((l0 + 1))
  check "AC2 bare: a START and an END" "$(( $(measure_lines) - l0 ))" 2
  check "AC2 bare: no remote field, since git passed the URL as both" "$(read_field $l remote)" "<absent>"
  check "AC2 bare: remote_unnamed" "$(read_field $l remote_unnamed)" 1
  check "AC2 bare: the userinfo is flagged" "$(read_field $l url_userinfo)" 1
  # THE REFUSAL BEFORE THE LOOP, to the same bare URL: its line meets the same renderer.
  git checkout -q main && git commit -q --allow-empty -m c3
  l0=$(measure_lines)
  run_push GIT_SSH_COMMAND="bash $WORK/fakessh.sh" GOV_DEFAULT_BRANCH=nosuchthing -- "$url" main
  check "AC2 refused: a misconfigured default refuses before the loop" "$PUSH_RC" 1
  l=$(measure_lines)
  check "AC2 refused: one line" "$((l - l0))" 1
  check "AC2 refused: it is the once line" "$(read_field $l ev)|$(read_field $l decision)" "once|refuse-default-branch"
  check "AC2 refused: remote_unnamed" "$(read_field $l remote_unnamed)" 1
  check "AC2 refused: the userinfo is flagged" "$(read_field $l url_userinfo)" 1
  check "AC2 refused: lander is written" "$(read_field $l lander)" 0
  check "AC2 refused: no remote field" "$(read_field $l remote)" "<absent>"
  # A TYPED URL THROUGH A REWRITE, L1 of the closing diff review, round 1. Under `url.<base>.insteadOf`
  # git hands the hook the URL as TYPED in $1 and the rewritten one in $2, so $1 differs from $2 and is
  # still no name. The rule rewrites a credentialed URL to the origin's own, so the push is a real one
  # that reaches the remote, and $2 holds no userinfo for a guard reading $2 alone to find.
  local base typed
  base=$(git config --get remote.origin.url)
  typed="https://user:pass@rewrite.invalid/typed.git"
  git config "url.$base.insteadOf" "$typed"
  git checkout -q -b cred-c main && git commit -q --allow-empty -m cc
  l0=$(measure_lines)
  run_push -- "$typed" cred-c
  check "AC2 rewritten: the typed credentialed URL reaches the remote through insteadOf" "$PUSH_RC" 0
  l=$((l0 + 1))
  check "AC2 rewritten: a START and an END" "$(( $(measure_lines) - l0 ))" 2
  check "AC2 rewritten: no remote field, since \$1 is the typed URL" "$(read_field $l remote)" "<absent>"
  check "AC2 rewritten: remote_unnamed" "$(read_field $l remote_unnamed)" 1
  check "AC2 rewritten: the typed URL's userinfo is flagged, though \$2 holds none" \
    "$(read_field $l url_userinfo)" 1
  check "AC2 rewritten: neither line of the pair holds :// or @" \
    "$(sed -n "${l},$((l + 1))p" "$JOURNAL" | grep -c -e '://' -e '@')" 0
  # ...and refused before the loop through the same rewrite, which is the once line's writer.
  git checkout -q main && git commit -q --allow-empty -m c4
  l0=$(measure_lines)
  run_push GOV_DEFAULT_BRANCH=nosuchthing -- "$typed" main
  check "AC2 rewritten and refused: a misconfigured default refuses before the loop" "$PUSH_RC" 1
  l=$(measure_lines)
  check "AC2 rewritten and refused: one line" "$((l - l0))" 1
  check "AC2 rewritten and refused: it is the once line" "$(read_field $l ev)|$(read_field $l decision)" \
    "once|refuse-default-branch"
  check "AC2 rewritten and refused: remote_unnamed, and no remote field" \
    "$(read_field $l remote_unnamed)|$(read_field $l remote)" "1|<absent>"
  check "AC2 rewritten and refused: the userinfo is flagged" "$(read_field $l url_userinfo)" 1
  check "AC2 rewritten and refused: the line holds neither :// nor @" \
    "$(sed -n "${l}p" "$JOURNAL" | grep -c -e '://' -e '@')" 0
  git config --unset "url.$base.insteadOf"
  check_journal AC2
}

# ------------------------------------------------------------------------------------------ AC3
# THE SIGNAL IS SENT ONLY ONCE THE BAR IS PROVABLY RUNNING. The stub bar writes its pid as its FIRST
# act and then becomes the sleep, so the poll proves the hook is waiting on it before TERM is sent, and
# the pid read is the process that must still be alive afterwards. A fixed sleep would place the
# signal wherever the scheduler happened to be.
check_ac3_term() {
  local ready="$WORK/ready" hp spid i l0 l
  printf '#!/usr/bin/env bash\necho $$ > "%s.tmp" && mv "%s.tmp" "%s"\nexec sleep 20\n' \
    "$ready" "$ready" "$ready" > "$WORK/slow.sh"
  git checkout -q main && git commit -q --allow-empty -m t3
  : > "$REPO/.git/push-main-active"; rm -f "$REPO/.git/gate-full-green" "$ready"
  write_refs "$WORK/refs.main" "refs/heads/main $(git rev-parse HEAD) refs/heads/main $ZERO"
  l0=$(measure_lines)
  GOV_GATE_CMD="bash $WORK/slow.sh" bash "$HOOK" origin "$WORK/remote.git" <"$WORK/refs.main" \
    >"$WORK/ac3.out" 2>&1 &
  hp=$!; BG_PIDS="$BG_PIDS $hp"
  i=0; while [ ! -s "$ready" ] && [ "$i" -lt 600 ]; do sleep 0.1; i=$((i + 1)); done
  spid=$(cat "$ready" 2>/dev/null); BG_PIDS="$BG_PIDS $spid"
  check "AC3 the stub bar reported ready" "$([ -n "$spid" ] && echo yes)" yes
  check "AC3 the stub bar is running when TERM is sent" "$(kill -0 "$spid" 2>/dev/null && echo alive)" alive
  kill -TERM "$hp" 2>/dev/null
  wait "$hp" 2>/dev/null
  # The hook is gone and the bar it was waiting on is NOT: it did not wait out the stub's 20 s.
  check "AC3 the hook ended while its bar still ran" "$(kill -0 "$spid" 2>/dev/null && echo alive)" alive
  kill "$spid" 2>/dev/null
  l=$(measure_lines)
  check "AC3 START and END" "$((l - l0))" 2
  check "AC3 END reads unclean" "$(read_field $l exit)" unclean
  check "AC3 END keeps the decision set before the bar" "$(read_field $l decision)" full
  check "AC3 END names the bar it was waiting on" "$(check_shape_run "$(read_field $l gate_run)")" shaped
  rm -f "$REPO/.git/push-main-active"
  check_journal AC3
}

# ------------------------------------------------------------------------------------------ AC4
check_ac4_join() {
  local l id rg g0 g
  git checkout -q main && git commit -q --allow-empty -m a4
  : > "$REPO/.git/push-main-active"; rm -f "$REPO/.git/gate-full-green" "$WORK/seen"
  run_push GOV_GATE_CMD="bash $WORK/idstub.sh" PPRL_SEEN="$WORK/seen" -- origin main
  check "AC4 the stubbed push lands" "$PUSH_RC" 0
  l=$(measure_lines); id=$(cat "$WORK/seen" 2>/dev/null)
  check "AC4 the stub bar was handed a push-shaped id" "$(check_shape_run "$id")" shaped
  check "AC4 END's gate_run is the id the bar was handed" "$(read_field $l gate_run)" "$id"
  # A COPY OF THE REAL RUNNER, outside the scratch tree so the tree stays clean, over ONE leg that
  # records what the runner handed it.
  rg="$WORK/rg/run-gates"
  mkdir -p "$rg" && cp "$RUNNER_KIT/run-gates.sh" "$RUNNER_KIT/gate-fingerprint.sh" "$RUNNER_KIT/gate-profiles.txt" "$rg/"
  printf '[{"name": "records its environment", "argv": ["bash", "%s"]}]\n' "$WORK/idstub.sh" > "$WORK/legs.json"
  git commit -q --allow-empty -m a4b; rm -f "$WORK/seen"
  g0=0; [ -f "$GATES" ] && g0=$(wc -l < "$GATES" | tr -d ' ')
  run_push GOV_GATE_CMD="bash $rg/run-gates.sh" GATE_LEGS="$WORK/legs.json" GATE_PROFILE=minimal \
    GATE_TURNSTILE=0 GATE_WALL=0 PPRL_SEEN="$WORK/seen" -- origin main
  check "AC4 the real runner's bar is green, so the push lands" "$PUSH_RC" 0
  l=$(measure_lines)
  g=0; [ -f "$GATES" ] && g=$(wc -l < "$GATES" | tr -d ' ')
  check "AC4 the runner wrote one line" "$((g - g0))" 1
  check "AC4 the runner's line names the run END records" \
    "$(awk -F'\t' -v l="$g" 'NR == l { for (i = 1; i <= NF; i++) if (index($i, "run=") == 1) print substr($i, 5) }' "$GATES" 2>/dev/null)" \
    "$(read_field $l gate_run)"
  check "AC4 END names a push-shaped run" "$(check_shape_run "$(read_field $l gate_run)")" shaped
  check "AC4 the leg ran" "$([ -f "$WORK/seen" ] && echo ran)" ran
  check "AC4 a leg of that bar sees no GATE_RUN_ID" "$(cat "$WORK/seen" 2>/dev/null)" "<unset>"
  rm -f "$REPO/.git/push-main-active" "$REPO/.git/gate-full-green"
  check_journal AC4
}

# ------------------------------------------------------------------------------------------ AC5
check_ac5_write_failure() {
  local out_off rc_off err_off l0
  git checkout -q main && git commit -q --allow-empty -m a5
  : > "$REPO/.git/push-main-active"; rm -f "$REPO/.git/gate-full-green"
  write_refs "$WORK/refs.main" "refs/heads/main $(git rev-parse HEAD) refs/heads/main $ZERO"
  [ -d "$REPO/.git/runlog" ] || mkdir "$REPO/.git/runlog"
  mv "$REPO/.git/runlog" "$WORK/runlog.keep"
  : > "$REPO/.git/runlog"
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_RUNLOG=0 GOV_GATE_CMD="bash $WORK/green.sh"
  out_off=$OUT; rc_off=$RC; err_off=$ERR
  check "AC5 the switch-off push ran its bar green, so two runs that did the work are compared" "$rc_off" 0
  check "AC5 and it printed its decision" "$(printf '%s\n' "$out_off" | grep -c 'FULL gate on main push')" 1
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_GATE_CMD="bash $WORK/green.sh"
  check "AC5 a failed append leaves rc alone" "$RC" "$rc_off"
  check "AC5 a failed append leaves stdout alone" "$OUT" "$out_off"
  check "AC5 stderr carries ONE run-log line for two failed writes" "$(printf '%s\n' "$ERR" | grep -c '^pre-push: run log')" 1
  check "AC5 that line names the file it could not write" "$(printf '%s\n' "$ERR" | grep '^pre-push: run log' | grep -c 'runlog/pushes.log')" 1
  check "AC5 and nothing else new on stderr" "$(printf '%s\n' "$ERR" | grep -v '^pre-push: run log')" "$err_off"
  # A RED bar: its rc is the one a failed write must never turn green.
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_GATE_CMD="bash $WORK/red.sh"
  check "AC5 a red bar keeps its rc when the append fails" "$RC" 1
  check "AC5 and says so once" "$(printf '%s\n' "$ERR" | grep -c '^pre-push: run log')" 1
  # A refusal before the loop, whose one line fails the same way.
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_DEFAULT_BRANCH=nosuchthing
  check "AC5 a refusal before the loop keeps its rc when its append fails" "$RC" 1
  check "AC5 and says so once" "$(printf '%s\n' "$ERR" | grep -c '^pre-push: run log')" 1
  rm -f "$REPO/.git/runlog"; mv "$WORK/runlog.keep" "$REPO/.git/runlog"
  l0=$(measure_lines)
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_RUNLOG=0 GOV_GATE_CMD="bash $WORK/green.sh"
  check "AC5 GOV_RUNLOG=0 writes nothing" "$(measure_lines)" "$l0"
  check "AC5 and says nothing on stderr about the log" "$(printf '%s\n' "$ERR" | grep -c '^pre-push: run log')" 0
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_RUNLOG=1 GOV_GATE_CMD="bash $WORK/green.sh"
  check "AC5 any other value of the switch writes" "$(measure_lines)" "$((l0 + 2))"
  rm -f "$REPO/.git/push-main-active"
  check_journal AC5
}

# ------------------------------------------------------------------------------------------ AC6
# NAMED SHORT ENOUGH THAT ELEVEN WOULD FIT THE BYTE CAP, so a missing `ref.11` is the COUNT cap's
# doing and nothing else's. With names long enough that only ten fit, the byte cap alone writes the
# same ten fields and the same `ref_more=11`, and a hook with no count cap passes. The byte cap has
# its own arm, CAP.
check_ac6_many_refs() {
  local i nm l0 l head
  local -a specs=()
  git checkout -q main
  head=$(git rev-parse HEAD)
  for i in $(seq -w 1 21); do
    nm="many-refs-arm-$i"
    git branch -f "$nm" HEAD >/dev/null 2>&1
    specs+=("$nm")
  done
  l0=$(measure_lines)
  run_push -- origin "${specs[@]}"
  check "AC6 the 21-ref push is not gated, so it lands" "$PUSH_RC" 0
  l=$((l0 + 1))
  check "AC6 one START and one END" "$(( $(measure_lines) - l0 ))" 2
  check "AC6 ref.10 is written" "$(read_field $l ref.10 | cut -d' ' -f2)" "$head"
  check "AC6 no ref.11" "$(read_field $l ref.11)" "<absent>"
  check "AC6 ref_more counts the other eleven" "$(read_field $l ref_more)" 11
  check "AC6 the line is at or under 2048 bytes" "$(read_line $l | LC_ALL=C awk '{ print (length($0) <= 2048) ? "under" : "over" }')" under
  # NOTHING WAS CUT: every ref written is a whole line of four fields, the last a full sha.
  check "AC6 every written ref is whole" "$(for i in 1 2 3 4 5 6 7 8 9 10; do read_field $l ref.$i; done | awk 'NF == 4 && length($4) == 40 { w++ } END { print w + 0 }')" 10
  check_journal AC6
}

# ------------------------------------------------------------------------------------------ DEC
# THE DECISIONS AC1 DOES NOT REACH, one push each, invoked the way git invokes the hook.
check_dec_rest() {
  local l0 l head
  git checkout -q main && git commit -q --allow-empty -m d1
  head=$(git rev-parse HEAD)
  : > "$REPO/.git/push-main-active"; rm -f "$REPO/.git/gate-full-green"
  write_refs "$WORK/refs.main" "refs/heads/main $head refs/heads/main $ZERO"
  # A delete of the default branch.
  write_refs "$WORK/refs.del" "(delete) $ZERO refs/heads/main $head"
  l0=$(measure_lines)
  run_hook "$WORK/refs.del" origin "$WORK/remote.git" GOV_GATE_CMD="bash $WORK/red.sh"
  l=$(measure_lines)
  check "DEC delete: not gated" "$RC" 0
  check "DEC delete: a pair" "$((l - l0))" 2
  check "DEC delete: decision" "$(read_field $l decision)" skip-delete
  check "DEC delete: the delete's ref line" "$(read_field $((l - 1)) ref.1)" "(delete) $ZERO refs/heads/main $head"
  [ "$(read_field $l decision)" = skip-delete ] && add_seen skip-delete
  # A leg manifest the index tracks outside the kit root the hook resolved.
  mkdir -p elsewhere && printf '[]\n' > elsewhere/gate-legs.json && git add elsewhere/gate-legs.json
  l0=$(measure_lines)
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_GATE_CMD="bash $WORK/green.sh"
  l=$(measure_lines)
  check "DEC manifest: refused" "$RC" 1
  check "DEC manifest: by the manifest refusal" "$(printf '%s\n' "$ERR" | grep -c 'resolved its kit root')" 1
  check "DEC manifest: decision" "$(read_field $l decision)|$(read_field $l exit)" "refuse-manifest|clean"
  [ "$(read_field $l decision)" = refuse-manifest ] && add_seen refuse-manifest
  git rm -q --cached elsewhere/gate-legs.json && rm -rf elsewhere
  # A default-branch sha that is not this tree's HEAD.
  write_refs "$WORK/refs.head" "refs/heads/main $(git rev-parse HEAD~1) refs/heads/main $ZERO"
  run_hook "$WORK/refs.head" origin "$WORK/remote.git" GOV_GATE_CMD="bash $WORK/green.sh"
  l=$(measure_lines)
  check "DEC head: refused" "$RC" 1
  check "DEC head: by the tip refusal" "$(printf '%s\n' "$OUT" | grep -c 'this working tree is at')" 1
  check "DEC head: decision" "$(read_field $l decision)|$(read_field $l exit)" "refuse-head|clean"
  [ "$(read_field $l decision)" = refuse-head ] && add_seen refuse-head
  # A recorded green that covers the tip: the scoped decision, and its bar still pins an id.
  printf 'sha\t%s\n' "$head" > "$REPO/.git/gate-full-green"
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_GATE_CMD="bash $WORK/green.sh"
  l=$(measure_lines)
  check "DEC scoped: the bar ran green" "$RC" 0
  check "DEC scoped: the hook chose a scoped run" "$(printf '%s\n' "$OUT" | grep -c 'scoped gate on main push')" 1
  check "DEC scoped: decision" "$(read_field $l decision)" scoped
  check "DEC scoped: gate_run" "$(check_shape_run "$(read_field $l gate_run)")" shaped
  [ "$(read_field $l decision)" = scoped ] && add_seen scoped
  rm -f "$REPO/.git/gate-full-green"
  # The other two refusals before the loop, which need NO observed default.
  git remote set-head origin -d >/dev/null 2>&1
  l0=$(measure_lines)
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_DEFAULT_BRANCH=
  l=$(measure_lines)
  check "DEC undetermined: refused" "$RC" 1
  check "DEC undetermined: by that refusal" "$(printf '%s\n' "$ERR" | grep -c "can't determine the default branch")" 1
  check "DEC undetermined: one once line" "$((l - l0))|$(read_field $l ev)|$(read_field $l decision)" "1|once|refuse-default-branch"
  check "DEC undetermined: lander, since the marker is present" "$(read_field $l lander)" 1
  l0=$(measure_lines)
  run_hook "$WORK/refs.main" origin "$WORK/remote.git" GOV_DEFAULT_BRANCH=nosuchthing
  l=$(measure_lines)
  check "DEC no-branch: refused" "$RC" 1
  check "DEC no-branch: by that refusal" "$(printf '%s\n' "$ERR" | grep -c 'no branch in this clone')" 1
  check "DEC no-branch: one once line" "$((l - l0))|$(read_field $l ev)|$(read_field $l decision)" "1|once|refuse-default-branch"
  git remote set-head origin main >/dev/null 2>&1
  rm -f "$REPO/.git/push-main-active"
  check_journal DEC
}

# ------------------------------------------------------------------------------------------ CAP
# BOTH STEPS OF THE FIT, each re-rendered by the runlog kit's reference writer from what the hook held
# before it fitted the line, and each required to come back byte-identical.
#   Step one: twelve refs whose names overflow the cap, so the count cap writes ref_more=2 and whole
#   ref.<i> fields then drop, highest first, into it.
#   Step two: no ref at all and a remote name longer than the cap, so the name is the longest value
#   and is cut: plain ASCII, a three-byte character behind a zero-, one- and two-byte prefix so a cut
#   lands INSIDE a character, and TABs, whose two-byte escape a cut can halve, behind the same prefixes.
check_cap_fit() {
  local i nm res pre id short=0 halved=0 l l0 head cap
  git checkout -q main
  head=$(git rev-parse HEAD)
  cap=$(sed -n 's/^RUNLOG_REF_CAP=\([0-9][0-9]*\).*/\1/p' "$HOOK" | head -1)
  check "CAP the hook's count cap is read from the hook" "$(case "$cap" in ''|*[!0-9]*) echo unread ;; *) echo read ;; esac)" read
  : > "$WORK/cap.refs"
  for i in $(seq -w 1 12); do
    nm="refs/heads/cap-$i-$(printf 'n%.0s' $(seq 1 180))"
    printf '%s\n' "$nm $head $nm $ZERO" >> "$WORK/cap.refs"
  done
  l0=$(measure_lines)
  run_hook "$WORK/cap.refs" origin "$WORK/remote.git"
  l=$((l0 + 1)); read_line "$l" > "$WORK/one.log"
  res=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" render "$WORK/one.log" "$WORK/cap.refs" - "${cap:-0}")
  check "CAP step one: the START is fitted as render_line fits it" "${res##* }" SAME
  check "CAP step one: whole refs dropped into the ref_more the count cap wrote" \
    "$(read_field $l ref_more | awk '{ print ($1 > 2) ? "added" : "not added" }')" added
  check "CAP step one: ref.1 survives the drop whole" "$(read_field $l ref.1)" "$(head -1 "$WORK/cap.refs")"
  : > "$WORK/none.refs"
  for pre in ascii "" a ab tab tab.a tab.aa; do
    case "$pre" in
      ascii) id=$(printf 'X%.0s' $(seq 1 2500)) ;;
      tab*)  id="${pre#tab}"; id="${id#.}$(printf 'a\t%.0s' $(seq 1 1100))" ;;
      *)     id="$pre$(printf '€%.0s' $(seq 1 900))" ;;
    esac
    printf '%s' "$id" > "$WORK/full"
    l0=$(measure_lines)
    run_hook "$WORK/none.refs" "$id" "$WORK/remote.git"
    l=$((l0 + 1)); read_line "$l" > "$WORK/one.log"
    check "CAP step two [$pre]: the push still ends, with its decision" "$RC|$(read_field $((l + 1)) decision)" "0|skip-nondefault"
    res=$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" render "$WORK/one.log" "$WORK/none.refs" "$WORK/full" "${cap:-0}")
    check "CAP step two [$pre]: the remote name is cut as render_line cuts it" "${res##* }" SAME
    case "$pre" in
      tab*) case "$res" in "2047 "*) halved=$((halved + 1)) ;; esac ;;
      ascii) ;;
      *) case "$res" in "2048 "*) ;; *) short=$((short + 1)) ;; esac ;;
    esac
  done
  check "CAP a cut landed inside a character at least once" "$([ "$short" -gt 0 ] && echo yes)" yes
  check "CAP a cut halved an escape at least once" "$([ "$halved" -gt 0 ] && echo yes)" yes
  check_journal CAP
}

# ------------------------------------------------------------------------------------------ AC7
# THE EXEC COUNT, from an xtrace on ITS OWN DESCRIPTOR, so a command inside a `2>/dev/null` is still
# seen, with every trace line prefixed by the function and the source line it ran from. A command
# word that is not an assignment, a builtin, a keyword or a function the traced hook defines is an
# external exec. The whole hook is the window, and two figures come out of it:
#   EXEC_ALL     every external exec, compared against a baseline that never runs the writer. That
#                comparison is blind to code OUTSIDE the writer's functions, which runs on both sides.
#   EXEC_WRITER  the execs the writer owns: any inside one of its six functions, and any on a
#                top-level line carrying one of its names. Measured, the first cut of this arm had
#                only EXEC_ALL, and a `git` call added beside the journal-root line passed it.
measure_execs() { # trace file · the hook it traced -> sets EXEC_ALL and EXEC_WRITER to "<count> <names>"
  local known l w src fn ln c=0 names="" wc=0 wnames="" tok alt
  known=" $(compgen -b | tr '\n' ' ') $(compgen -k | tr '\n' ' ') "
  known="$known$(sed -n 's/^[[:space:]]*\([A-Za-z_][A-Za-z0-9_]*\)[[:space:]]*()[[:space:]]*{.*/\1/p' "$2" | tr '\n' ' ') "
  alt=$(printf '%s\n' $WRITER_FNS | paste -sd'|' -)
  tok=" $(grep -nE "RUNLOG_|GATE_RUN_ID${alt:+|$alt}" "$2" | cut -d: -f1 | tr '\n' ' ') "
  while IFS= read -r l; do
    case "$l" in +*) ;; *) continue ;; esac
    l=${l#"${l%%[!+]*}"}; l=${l# }
    src=${l%% *}; l=${l#* }
    fn=${src%%:*}; ln=${src##*:}
    w=${l%% *}; w=${w#\'}; w=${w%\'}
    case "$w" in ""|*=*|\(*) continue ;; esac
    case "$known" in *" $w "*) continue ;; esac
    c=$((c + 1)); names="$names$w"$'\n'
    if [ "$fn" = main ]; then
      case "$tok" in *" $ln "*) wc=$((wc + 1)); wnames="$wnames$w"$'\n' ;; esac
    else
      case " $WRITER_FNS " in *" $fn "*) wc=$((wc + 1)); wnames="$wnames$w"$'\n' ;; esac
    fi
  done < "$1"
  EXEC_ALL="$c $(printf '%s' "$names" | sort | tr '\n' ' ')"
  EXEC_WRITER="$wc $(printf '%s' "$wnames" | sort | tr '\n' ' ')"
}

# THE WRITER'S FUNCTIONS, derived from the hook by the naming its spec's inventory fixes, `*_push_*`,
# and never listed here: a writer function this suite did not know would run on both sides of the
# baseline and be owned by nobody, so its execs would pass unseen.
read_writer_fns() { # hook -> the writer's function names, space-separated
  sed -n 's/^\([a-z_]*_push_[a-z_]*\)() {.*/\1/p' "$1" | tr '\n' ' '
}

# THE BASELINE NEVER RUNS THE WRITER: every writer function returns at once, so it is this hook's
# decisions with no line written. `GOV_RUNLOG=0` is not that, since the writer still does whatever it
# does before it reads the switch, and an exec placed there would be counted on both sides.
build_baseline() { # -> the baseline hook's path
  local alt
  mkdir -p "$WORK/base"
  if [ -n "${PPRL_BEFORE:-}" ]; then
    cp "$PPRL_BEFORE" "$WORK/base/pre-push"
  else
    alt=$(printf '%s\n' $WRITER_FNS | paste -sd'|' -)
    sed -E "s/^(${alt:-no_writer_found})\(\) \{/& return 0;/" "$HOOK" > "$WORK/base/pre-push"
  fi
  printf '%s' "$WORK/base/pre-push"
}

run_traced() { # trace file · hook · ref-lines file · NAME=VALUE... -> one hook run under xtrace
  local tf=$1 hk=$2 refs=$3
  shift 3
  env PS4='+ ${FUNCNAME[0]:-main}:${LINENO} ' BASH_XTRACEFD=9 "$@" bash -x "$hk" origin "$WORK/remote.git" \
    <"$refs" 9>"$tf" >/dev/null 2>&1
}

check_ac7_spawns() {
  local base wt="$WORK/wt" tree label path want gd head l0 off on rcoff rcon skip_on="" first extra nfn
  WRITER_FNS=$(read_writer_fns "$HOOK")
  nfn=$(printf '%s\n' $WRITER_FNS | grep -c .)
  echo "AC7 the writer's functions, read from the hook: $WRITER_FNS"
  check "AC7 the writer's functions are found in the hook" "$([ "$nfn" -gt 0 ] && echo found)" found
  base=$(build_baseline)
  if [ -n "${PPRL_BEFORE:-}" ]; then
    echo "AC7 baseline: the hook named by PPRL_BEFORE"
  else
    check "AC7 every writer function in the baseline copy returns at once" "$(grep -cE '^[a-z_]+\(\) \{ return 0;' "$base")" "$nfn"
  fi
  git checkout -q main
  git worktree add -q "$wt" -b wtside >/dev/null 2>&1
  [ -d "$REPO/.git/runlog" ] || mkdir "$REPO/.git/runlog"
  for tree in "$REPO" "$wt"; do
    cd "$tree" || return 1
    case "$tree" in "$REPO") label=primary ;; *) label=worktree ;; esac
    gd=$(git rev-parse --path-format=absolute --git-dir)
    head=$(git rev-parse HEAD)
    : > "$gd/push-main-active"; rm -f "$gd/gate-full-green"
    write_refs "$WORK/refs.skip" "refs/heads/feature $head refs/heads/feature $ZERO"
    write_refs "$WORK/refs.full" "refs/heads/$(git symbolic-ref --short HEAD) $head refs/heads/main $ZERO"
    for path in skip full; do
      case "$path" in skip) want=skip-nondefault ;; full) want=full ;; esac
      l0=$(measure_lines)
      run_traced "$WORK/t.off" "$base" "$WORK/refs.$path" GOV_GATE_CMD="bash $WORK/green.sh"; rcoff=$?
      check "AC7 [$label $path] the baseline wrote no line" "$(measure_lines)" "$l0"
      run_traced "$WORK/t.on" "$HOOK" "$WORK/refs.$path" GOV_GATE_CMD="bash $WORK/green.sh"; rcon=$?
      # BOTH SIDES DID THE WORK: equal counts from two runs that refused early would compare nothing.
      check "AC7 [$label $path] both runs exit 0" "$rcoff|$rcon" "0|0"
      check "AC7 [$label $path] the writer's run wrote START and END to the COMMON journal" "$(measure_lines)" "$((l0 + 2))"
      check "AC7 [$label $path] its decision" "$(read_field $((l0 + 2)) decision)" "$want"
      check "AC7 [$label $path] it names its own worktree" "$(read_field $((l0 + 1)) wt)" "$(git rev-parse --show-toplevel)"
      measure_execs "$WORK/t.off" "$base"; off=$EXEC_ALL
      measure_execs "$WORK/t.on" "$HOOK"; on=$EXEC_ALL
      check "AC7 [$label $path] the probe sees execs at all" "$([ "${off%% *}" -gt 0 ] 2>/dev/null && echo yes)" yes
      echo "AC7 [$label $path] external execs: baseline ${off%% *}, writer on ${on%% *}"
      check "AC7 [$label $path] the writer adds no external exec" "$on" "$off"
      check "AC7 [$label $path] and owns none" "$EXEC_WRITER" "0 "
      [ "$label:$path" = primary:skip ] && skip_on=$on
    done
    rm -f "$gd/push-main-active"
  done
  check "AC7 the worktree's git dir is its own" "$(case "$gd" in */.git/worktrees/*) echo yes ;; esac)" yes
  check "AC7 nothing is journaled under the worktree's git dir" "$([ -e "$gd/runlog" ] && echo present || echo none)" none
  cd "$REPO" || return 1
  git worktree remove --force "$wt" >/dev/null 2>&1
  # The one sanctioned spawn: a clone's FIRST push makes the journal directory, once.
  write_refs "$WORK/refs.skip" "refs/heads/feature $(git rev-parse HEAD) refs/heads/feature $ZERO"
  mv "$REPO/.git/runlog" "$WORK/runlog.keep"
  run_traced "$WORK/t.first" "$HOOK" "$WORK/refs.skip" GOV_GATE_CMD="bash $WORK/green.sh"
  measure_execs "$WORK/t.first" "$HOOK"; first=$EXEC_ALL
  extra=$(comm -13 <(printf '%s\n' ${skip_on#* } | sort) <(printf '%s\n' ${first#* } | sort) | tr '\n' ' ')
  check "AC7 a clone's first push pays exactly one mkdir" "$extra" "mkdir "
  check "AC7 and nothing else" "${first%% *}" "$(( ${skip_on%% *} + 1 ))"
  check "AC7 and that mkdir is the writer's" "$EXEC_WRITER" "1 mkdir "
  check "AC7 and that push still wrote its pair" "$(wc -l < "$REPO/.git/runlog/pushes.log" | tr -d ' ')" 2
  cat "$REPO/.git/runlog/pushes.log" >> "$WORK/runlog.keep/pushes.log"
  rm -rf "$REPO/.git/runlog"; mv "$WORK/runlog.keep" "$REPO/.git/runlog"
  check_journal AC7
}

# ------------------------------------------------------------------------------------------ AC8
# THIS SUITE'S OWN DECLARATIONS, read from the files that make them. The deployer's verdict and the
# budget verdict are their own legs after the build; what is asserted here is that each declaration
# EXISTS, so a suite that ships, runs unbudgeted or drops off the manifest reds here too.
check_ac8_declarations() {
  local kr="$SRC/$KIT_REL"
  check "AC8 the suite is withheld by the push-main entry's project-owned rule" \
    "$(awk '/^\[\[files\]\]/ { inc = "" } /^include = \[/ { inc = $0 } /^role = "project-owned"/ && inc ~ /"\.githooks\/pre-push\.runlog\.test\.sh"/ { print "withheld" }' "$kr/govkit/entries/push-main.kit.toml")" withheld
  check "AC8 the suite's leg has a budget row" \
    "$(awk -F'\t' '$1 == "pre-push run-log line" && $2 ~ /^[0-9]+$/ { print "budgeted" }' "$kr/run-gates/selftest-budgets.txt")" budgeted
  check "AC8 the suite's leg is held, guarded and bounded" \
    "$("$PY" "$WORK/jl.py" "$RUNLOG_KIT" legs "$kr/gate-legs.json" "pre-push run-log line")" declared
  check "AC8 the deployer's registry carries the leg as an exempt row" \
    "$(awk '/^\[\[exempt_leg\]\]/ { e = 1; next } e && $0 == "name = \"pre-push run-log line\"" { print "exempt" } /^\[/ { e = 0 }' "$kr/govkit/registry.toml")" exempt
}

# ---------------------------------------------------------------------------------------- EXITS
# THE EXIT-SITE ENUMERATION. A small lexer, because every cheaper predicate reads something else:
# `exit` appears in this hook's messages and comments, and as a KEY in the END line's field list. It
# tracks single, double and ANSI-C quotes and skips comments and here-document bodies, then reports
# each `exit` word in command position as `<line> TAB <code>`, where code is the line up to any comment,
# trimmed, so a comment edit cannot move a site out of its row.
scan_exit_sites() { # file -> one TAB-separated row per shell exit
  awk '
    FNR == 1 { st = "N"; hd = "" }
    {
      line = $0; sub(/\r$/, "", line)
      if (hd != "") { t = line; sub(/^\t+/, "", t); if (t == hd) hd = ""; next }
      nl = length(line); i = 1; pend = ""; cut = nl + 1; nex = 0
      while (i <= nl) {
        c = substr(line, i, 1)
        if (st == "S") { if (c == "\047") st = "N"; i++; continue }
        if (st == "A") { if (c == "\\") { i += 2; continue }; if (c == "\047") st = "N"; i++; continue }
        if (st == "D") { if (c == "\\") { i += 2; continue }; if (c == "\"") st = "N"; i++; continue }
        if (c == "\\") { i += 2; continue }
        if (c == "$" && substr(line, i + 1, 1) == "\047") { st = "A"; i += 2; continue }
        if (c == "\047") { st = "S"; i++; continue }
        if (c == "\"") { st = "D"; i++; continue }
        b = (i == 1) ? " " : substr(line, i - 1, 1)
        if (c == "#" && b ~ /[ \t;&|()]/) { cut = i; break }
        if (c == "<" && substr(line, i, 3) ~ /^<<[^<]/) {
          rest = substr(line, i + 2); sub(/^-/, "", rest); sub(/^[ \t]*/, "", rest)
          if (match(rest, /^["\047]?[A-Za-z_][A-Za-z0-9_]*/)) { w = substr(rest, RSTART, RLENGTH); gsub(/["\047]/, "", w); pend = w }
          i += 2; continue
        }
        if (substr(line, i, 4) == "exit" && b ~ /[ \t;&|({!]/ && (i + 4 > nl || substr(line, i + 4, 1) ~ /[ \t;)}]/)) {
          pre = substr(line, 1, i - 1); sub(/[ \t]+$/, "", pre)
          # COMMAND POSITION, not merely a word: `f=(… rc "$rc" exit "$ex" …)` names a key.
          if (pre != "" && pre !~ /(;|&&|\|\||\||[{()!]|(^|[ \t])(then|else|do))$/) { i += 4; continue }
          nex++; i += 4; continue
        }
        i++
      }
      if (nex > 0) {
        code = substr(line, 1, cut - 1); sub(/^[ \t]+/, "", code); sub(/[ \t]+$/, "", code)
        for (k = 0; k < nex; k++) printf "%d\t%s\n", FNR, code
      }
      if (pend != "") hd = pend
    }' "$1"
}

# Every exit site, by its CODE and the number of sites carrying it, joined to this table. Code rather
# than a line number, because every edit above an exit moves its line; code AND count, because the
# three refusals before the loop share one code, and a fourth must read as a count that moved. The
# third column is the decision a site writes, which the join below requires this run to have SEEN.
{
  printf '%s\t%s\t%s\n' 'exit 1' 2 'exempt: the two refusals before any journal root, which S1 names as unloggable'
  printf '%s\t%s\t%s\n' 'write_push_once refuse-default-branch; exit 1' 3 refuse-default-branch
  printf '%s\t%s\t%s\n' '[ -z "$main_local" ] && { RUNLOG_DECISION=skip-nondefault; RUNLOG_CLEAN=1; exit 0; }' 1 skip-nondefault
  printf '%s\t%s\t%s\n' '[ -z "${main_local//0/}" ] && { RUNLOG_DECISION=skip-delete; RUNLOG_CLEAN=1; exit 0; }' 1 skip-delete
  printf '%s\t%s\t%s\n' 'RUNLOG_DECISION=refuse-manifest; RUNLOG_CLEAN=1; exit 1' 1 refuse-manifest
  printf '%s\t%s\t%s\n' 'RUNLOG_DECISION=refuse-raw; RUNLOG_CLEAN=1; exit 1' 1 refuse-raw
  printf '%s\t%s\t%s\n' 'RUNLOG_DECISION=refuse-head; RUNLOG_CLEAN=1; exit 1' 1 refuse-head
  printf '%s\t%s\t%s\n' 'RUNLOG_DECISION=refuse-straggler; RUNLOG_CLEAN=1; exit 1' 1 'exempt: the straggler refusal, reachable only with straggler-guard.sh beside the hook and a transition-merge fixture this suite does not build; armed by straggler-guard.test.sh'
  printf '%s\t%s\t%s\n' 'RUNLOG_CLEAN=1; exit "$rc"' 1 'full|scoped'
} > "$WORK/exits.tsv"

check_exit_table() { # hook -> EXIT_ROOT EXIT_TRAP EXIT_SITES EXIT_UNKNOWN EXIT_MISCOUNT EXIT_STALE EXIT_UNMARKED EXIT_MISPLACED
  local cnt text want ln
  EXIT_ROOT=$(grep -nxF 'resolve_push_dirs "$top" || { RUNLOG_GITDIR=""; RUNLOG_DIR=""; }' "$1" | head -1 | cut -d: -f1)
  EXIT_TRAP=$(grep -nxF "trap 'write_push_end \"\$?\"' EXIT" "$1" | head -1 | cut -d: -f1)
  scan_exit_sites "$1" > "$WORK/sites.all"
  EXIT_UNMARKED=""; EXIT_MISPLACED=""
  while IFS=$'\t' read -r ln text; do
    [ -n "$ln" ] || continue
    # Below the trap, the clean-exit mark sits immediately before the exit on its own line.
    if [ "$ln" -gt "${EXIT_TRAP:-999999}" ]; then
      case "$text" in *"RUNLOG_CLEAN=1; exit"*) ;; *) EXIT_UNMARKED="$EXIT_UNMARKED[$text]" ;; esac
    fi
    # The exemptions sit above the journal root, and the once refusals between it and the trap.
    case "$text" in
      "exit 1") [ "$ln" -lt "${EXIT_ROOT:-0}" ] || EXIT_MISPLACED="$EXIT_MISPLACED[$ln $text]" ;;
      "write_push_once "*) { [ "$ln" -gt "${EXIT_ROOT:-999999}" ] && [ "$ln" -lt "${EXIT_TRAP:-0}" ]; } \
                             || EXIT_MISPLACED="$EXIT_MISPLACED[$ln $text]" ;;
    esac
  done < "$WORK/sites.all"
  cut -f2- "$WORK/sites.all" | LC_ALL=C sort | uniq -c > "$WORK/sites.txt"
  EXIT_SITES=0; EXIT_UNKNOWN=""; EXIT_MISCOUNT=""; EXIT_STALE=""
  while read -r cnt text; do
    [ -n "$text" ] || continue
    EXIT_SITES=$((EXIT_SITES + cnt))
    want=$(X="$text" awk -F'\t' '$1 == ENVIRON["X"] { print $2 }' "$WORK/exits.tsv")
    if [ -z "$want" ]; then EXIT_UNKNOWN="$EXIT_UNKNOWN[$text]"
    elif [ "$want" != "$cnt" ]; then EXIT_MISCOUNT="$EXIT_MISCOUNT[$text: $cnt sites, table $want]"; fi
  done < "$WORK/sites.txt"
  while IFS=$'\t' read -r text want _; do
    [ -n "$text" ] || continue
    X="$text" awk '{ sub(/^ *[0-9]+ /, "") } $0 == ENVIRON["X"] { f = 1 } END { exit !f }' "$WORK/sites.txt" \
      || EXIT_STALE="$EXIT_STALE[$text]"
  done < "$WORK/exits.tsv"
}

check_exits() {
  local text want dec d unseen=""
  check_exit_table "$HERE/pre-push"
  check "EXITS the journal-root line is found" "$([ -n "$EXIT_ROOT" ] && echo found)" found
  check "EXITS the trap line is found, below the root" "$([ -n "$EXIT_TRAP" ] && [ "$EXIT_TRAP" -gt "${EXIT_ROOT:-0}" ] && echo found)" found
  check "EXITS the scan sees as many sites as the table declares" "$EXIT_SITES" \
    "$(awk -F'\t' '{ s += $2 } END { print s + 0 }' "$WORK/exits.tsv")"
  check "EXITS every exit maps to a decision or a named exemption" "${EXIT_UNKNOWN:-none}" none
  check "EXITS every row's site count holds" "${EXIT_MISCOUNT:-none}" none
  check "EXITS every row still names a site" "${EXIT_STALE:-none}" none
  check "EXITS every exit after the trap carries the clean-exit mark" "${EXIT_UNMARKED:-none}" none
  check "EXITS every exemption and once refusal sits where it must" "${EXIT_MISPLACED:-none}" none
  # EVERY DECISION A ROW NAMES WAS SEEN ON A LINE. A selected run did not run every arm, so it says so.
  if [ -z "${PPRL_ARMS:-}" ]; then
    while IFS=$'\t' read -r text want dec; do
      case "$dec" in exempt:*|"") continue ;; esac
      for d in ${dec//|/ }; do
        case "$SEEN" in *" $d "*) ;; *) unseen="$unseen[$d]" ;; esac
      done
    done < "$WORK/exits.tsv"
    check "EXITS every decision the table names was written by some arm" "${unseen:-none}" none
  else
    echo "SKIP EXITS decision join: PPRL_ARMS selected [$PPRL_ARMS], so not every arm the table names ran"
  fi
  # THE ENUMERATION'S FAILING CASES, staged into COPIES every run: an exit nobody armed below the trap;
  # an unmarked decision exit there; a second copy of an armed code, which only the count can see; an
  # exemption moved below the root; and the control, a comment and a string that are not exits.
  awk -v t="$EXIT_TRAP" '{ print } NR == t { print "exit 3" }' "$HERE/pre-push" > "$WORK/mut.sh"
  check_exit_table "$WORK/mut.sh"
  check "EXITS staged: an unarmed exit below the trap is caught" "$EXIT_UNKNOWN" "[exit 3]"
  check "EXITS staged: and it carries no mark" "$EXIT_UNMARKED" "[exit 3]"
  awk -v t="$EXIT_TRAP" '{ print } NR == t { print "RUNLOG_DECISION=refuse-raw; exit 1" }' "$HERE/pre-push" > "$WORK/mut.sh"
  check_exit_table "$WORK/mut.sh"
  check "EXITS staged: a decision exit without the mark is caught" "$EXIT_UNMARKED" "[RUNLOG_DECISION=refuse-raw; exit 1]"
  { cat "$HERE/pre-push"; printf '%s\n' 'RUNLOG_DECISION=refuse-raw; RUNLOG_CLEAN=1; exit 1'; } > "$WORK/mut.sh"
  check_exit_table "$WORK/mut.sh"
  check "EXITS staged: a second copy of an armed code is caught" "$EXIT_MISCOUNT" \
    "[RUNLOG_DECISION=refuse-raw; RUNLOG_CLEAN=1; exit 1: 2 sites, table 1]"
  awk -v r="$EXIT_ROOT" '{ print } NR == r { print "exit 1" }' "$HERE/pre-push" > "$WORK/mut.sh"
  check_exit_table "$WORK/mut.sh"
  check "EXITS staged: an exemption below the journal root is caught" "$(printf '%s' "$EXIT_MISPLACED" | grep -c 'exit 1')" 1
  awk -v t="$EXIT_TRAP" 'NR == t + 1 { print "# exit 3 in a comment"; print "echo \"exit 3\"" } { print }' "$HERE/pre-push" > "$WORK/mut.sh"
  check_exit_table "$WORK/mut.sh"
  check "EXITS control: a comment and a string are not exits" \
    "${EXIT_UNKNOWN:-none}|${EXIT_MISCOUNT:-none}|${EXIT_UNMARKED:-none}" "none|none|none"
}

build_scratch || { echo "FAIL the scratch clone could not be built"; exit 1; }

check_selected AC1 && check_ac1_decisions
check_selected AC2 && check_ac2_credentials
check_selected AC3 && check_ac3_term
check_selected AC4 && check_ac4_join
check_selected AC5 && check_ac5_write_failure
check_selected AC6 && check_ac6_many_refs
check_selected DEC && check_dec_rest
check_selected CAP && check_cap_fit
check_selected AC7 && check_ac7_spawns
check_selected AC8 && check_ac8_declarations
check_selected EXITS && check_exits

if [ -n "${PPRL_ARMS:-}" ]; then
  echo "SELECTED ($n assertions, arms [$PPRL_ARMS]; the floor of $FLOOR_ASSERTIONS grades only a full run)"
  exit "$st"
fi
if [ "$n" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "FAIL $n assertions ran, under the floor of $FLOOR_ASSERTIONS: an arm stopped asserting"; st=1
fi
[ "$st" = 0 ] && echo "PASS ($n assertions)"
[ "$st" = 0 ] || echo "FAILED ($n assertions)"
exit "$st"
