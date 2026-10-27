#!/usr/bin/env bash
# push-main.test.sh — proves push-main.sh + the pre-push marker gate (TOOL-aLeasedGauntlet-1),
# against a scratch bare remote with a STUBBED gate (GOV_GATE_CMD). Exit 0 = all cases pass.
#
# Cases 1-8 are the ATTENDED landing, from a primary tree with the default branch checked out, and
# so are the cases after them up to AC1 (TOOL-aRepatriatedFork-5, -8: the lander marker, the one
# dirty definition, the refusal channel). Then cases 9-23 AGAIN, a separate block: the IN-PLACE
# landing flags (TOOL-dDerivedDocket-2), over a second fixture that adds
# what they need: a linked worktree on a run branch, and a local default branch carrying commits
# nobody pushed. What this file does NOT check: anything about a real remote or a real bar — the
# gate is stubbed and every remote here is a path on disk.
set -u
# THE SUBJECT IS FOUND FROM THIS FILE'S OWN LOCATION (TOOL-aRepatriatedFork-8 S6). This suite ships
# beside its lander to whatever prefix an adopter installs the kit at (`scripts/` at adopter ic), and it
# used to spell `<prefix>/` for both, so an adopter had to fork it to run it. KIT_REL is where the pair
# sits relative to the root, as git reports it: `<prefix>/` here, empty at a root install.
HERE=$(cd "$(dirname "$0")" && pwd)
SRC=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 2; }
KIT_REL=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-prefix 2>/dev/null)
[ -f "$HERE/push-main.sh" ] || { echo "push-main.sh missing beside this suite"; exit 1; }
[ -f "$SRC/.githooks/pre-push" ] || { echo ".githooks/pre-push missing"; exit 1; }
lander="${KIT_REL}push-main.sh"   # the lander's path inside every fixture, the same prefix as here
# The launcher resolver, INLINE: arm 33 runs the prepared merge's own checks, which are Python, and
# this suite ships beside its lander where `<prefix>/lib/` does not travel (TOOL-dGroundRules-25 S2).
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file, so a consumer never spawns
        # the Windows App Execution Alias again; the launcher's own name otherwise.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
  } >&2
  return 1
}
# <<< resolve_python

tmp=$(mktemp -d) || exit 2
trap 'rm -rf "$tmp"' EXIT
# Fixture identity and line endings for every git below, the racers' included, through the
# environment and not per repo (TOOL-aSparedSpawn-9 S1): no spawn, and command scope outranks a
# node's global autocrlf=true, which used to reach a clone's first checkout before its config did.
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@e GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@e
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
fail=0
ok()  { echo "  ok   — $1"; }
bad() { echo "  FAIL — $1"; fail=1; }

# stub gate: RED iff $tmp/gate-fail; on $tmp/race-once, advance origin behind our back, then remove it.
# A RED run prints `connection`, the word the pre-S2 lander read as an unreachable remote (case 4c).
cat > "$tmp/stub.sh" <<STUB
#!/usr/bin/env bash
if [ -f "$tmp/race-once" ]; then rm -f "$tmp/race-once"; git -C "$tmp/racer" commit -q --allow-empty -m race; git -C "$tmp/racer" push -q origin main; fi
if [ -f "$tmp/race2-once" ]; then rm -f "$tmp/race2-once"; git -C "$tmp/racer2" commit -q --allow-empty -m race2; git -C "$tmp/racer2" push -q origin main; fi
[ -f "$tmp/gate-fail" ] && { echo "FAKE LEG: lost its connection to the test database"; exit 1; } || exit 0
STUB
chmod +x "$tmp/stub.sh"
export GOV_GATE_CMD="bash $tmp/stub.sh"
# THE DECLARED TEST ESCAPE (TOOL-aRepatriatedFork-5). The stub above lives under mktemp and is
# untracked by construction, and .githooks/pre-push refuses an untracked merge bar. This waives the
# tracked-file requirement, marks the hook's decision line 'bar: STUB', and makes push-main withhold
# the lander marker, which case 9 grades. Case 9b unsets it deliberately.
export GOV_GATE_CMD_TEST=1
# The scratch work repo is `git init`+`remote add` (origin/HEAD unset); pin the default so the hook's
# and lander's fail-CLOSED resolution doesn't refuse every case (that path is tested by cases 7-8).
export GOV_DEFAULT_BRANCH=main

setup_repo() {  # $1 = repo dir · $2 = remote name (origin) · $3 = remote path ($tmp/remote.git)
  local r=$1 name=${2:-origin} url=${3:-$tmp/remote.git}
  git init -q --template= "$r"; cd "$r" || exit 2
  mkdir -p "./$KIT_REL" .githooks
  cp "$HERE/push-main.sh" "$lander"
  cp "$SRC/.githooks/pre-push"  .githooks/pre-push
  git config core.hooksPath .githooks
  git add -A && git commit -q -m init && git branch -M main
  git remote add "$name" "$url"
}

git init -q --template= --bare "$tmp/remote.git"
setup_repo "$tmp/work"
git push -q --no-verify origin main
git -C "$tmp/remote.git" symbolic-ref HEAD refs/heads/main
git clone -q "$tmp/remote.git" "$tmp/racer"
git -C "$tmp/racer" checkout -q -B main origin/main
cd "$tmp/work" || exit 2
gitdir=$(git rev-parse --git-dir)
read_refusal_token() { [ -s "$gitdir/pre-push-refusal" ] && cut -f1 < "$gitdir/pre-push-refusal" || echo ""; }

# 1 — hook refuses a raw default-branch push (no marker)
git commit -q --allow-empty -m c1
if git push -q origin main 2>/dev/null; then bad "1 raw push must be refused (no marker)"; else ok "1 raw push refused (no marker)"; fi
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${probe_n:-1} assertions)" || echo "FAIL (${probe_n:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi
# 1b — and records WHY as a machine token the lander reads, not as prose (TOOL-aRepatriatedFork-8 S2).
[ "$(read_refusal_token)" = raw-push ] && ok "1b the refusal is recorded as the token raw-push" || bad "1b refusal token should be raw-push, got '$(read_refusal_token)'"

# 2 — push-main lands it; marker cleared after
if bash "$lander" >/dev/null 2>&1; then ok "2 push-main lands (marker + green gate)"; else bad "2 push-main should land"; fi
[ -f "$gitdir/push-main-active" ] && bad "2b marker leaked" || ok "2b marker cleared"
# 2c — case 1's token does not survive a later SUCCESSFUL push, or the lander would one day report a
#      refusal that never happened.
[ -f "$gitdir/pre-push-refusal" ] && bad "2c a stale refusal token survived a successful push" || ok "2c a successful push leaves no refusal token"

# 2d — a claim push in flight in this git dir holds the lander until its recorded deadline, then it
#      lands (TOOL-aGraftedHelix-36 S10). RED with the wait cut: it pushes at once beside the lock.
#      LOAD-INDEPENDENT (TOOL-aClassedKnob-2): a deadline 3s out expired before a loaded host's lander
#      reached it. The deadline is now far, under the 120s ceiling, and a releaser removes the lock 3s
#      after the lander's marker appears — the lander touches it immediately before it waits, so the
#      lock is still held when it first looks. The verdict reads the lander's own announcements.
git commit -q --allow-empty -m c2d
mkdir "$gitdir/claim-push.lock"; echo "$(( $(date +%s) + 100 ))" > "$gitdir/claim-push.lock/until"
( for _i in $(seq 1 1000); do [ -e "$gitdir/push-main-active" ] && break; sleep 0.1; done
  sleep 3; rm -rf "$gitdir/claim-push.lock" ) & rel2d=$!
out2d=$(bash "$lander" 2>&1); rc2d=$?
wait "$rel2d"
case "$out2d" in
  *"proceeding past a claim-push lock"*) bad "2d the lander passed the lock instead of waiting for its release: $out2d" ;;
  *"waited "*"s for a claim push in flight in this git dir"*) [ "$rc2d" = 0 ] \
    && ok "2d a live claim-push lock holds the lander until it is released, then it lands" || bad "2d rc=$rc2d: $out2d" ;;
  *) bad "2d the lander did not wait for a live claim-push lock: $out2d" ;;
esac
# 2e — an expired lock is announced and passed at once.
git commit -q --allow-empty -m c2e
mkdir -p "$gitdir/claim-push.lock"; echo "$(( $(date +%s) - 5 ))" > "$gitdir/claim-push.lock/until"
out2e=$(bash "$lander" 2>&1); rc2e=$?
case "$out2e" in
  *"waited "*) bad "2e the lander waited on an expired claim-push lock: $out2e" ;;
  *"proceeding past a claim-push lock whose deadline passed"*) [ "$rc2e" = 0 ] \
    && ok "2e an expired claim-push lock is announced and passed, and the push lands" || bad "2e rc=$rc2e $out2e" ;;
  *) bad "2e an expired claim-push lock was not announced: $out2e" ;;
esac
rm -rf "$gitdir/claim-push.lock"

# 3 — reconcile-before-gate
git -C "$tmp/racer" pull -q; git -C "$tmp/racer" commit -q --allow-empty -m ahead; git -C "$tmp/racer" push -q origin main
git commit -q --allow-empty -m c3
if bash "$lander" >/dev/null 2>&1 && git log -1 --format=%s | grep -q 'push-main reconcile'; then ok "3 reconcile-before-gate then landed"; else bad "3 should reconcile then land"; fi

# 4 — red gate surfaced, not retried
touch "$tmp/gate-fail"; git commit -q --allow-empty -m c4
out4=$(bash "$lander" 2>&1); rc4=$?
if [ "$rc4" -eq 0 ]; then bad "4 red gate must block"; else ok "4 red gate surfaced"; fi
# 4c — reported as a bar that RAN and is red, from the hook's token. The stub printed `connection`,
#      which the pre-S2 lander, grepping the push's own output, reported as an unreachable remote.
case "$out4" in
  *"could not reach"*)      bad "4c a red bar was misreported as an unreachable remote: $out4" ;;
  *"no leg ran"*)           bad "4c a red bar was misreported as a precondition refusal: $out4" ;;
  *"bar RAN and is RED"*"gate-last-summary.txt"*) ok "4c a red bar is reported as a bar that ran, naming its summary file" ;;
  *)                        bad "4c the red-bar message is unrecognised: $out4" ;;
esac
rm -f "$tmp/gate-fail"

# 5 — mid-gate race → re-gate → land
git -C "$tmp/racer" pull -q; touch "$tmp/race-once"; git commit -q --allow-empty -m c5
if bash "$lander" >/dev/null 2>&1; then ok "5 mid-gate race recovered + landed"; else bad "5 should recover from a mid-gate race"; fi
rm -f "$tmp/race-once"

# 6 — conflicting reconcile aborts clean
git -C "$tmp/racer" pull -q; echo racer > "$tmp/racer/CONF"; git -C "$tmp/racer" add CONF; git -C "$tmp/racer" commit -q -m rc; git -C "$tmp/racer" push -q origin main
echo mine > CONF; git add CONF; git commit -q -m mc
bash "$lander" >/dev/null 2>&1
if [ -z "$(git status --porcelain)" ] && [ ! -f "$gitdir/push-main-active" ]; then ok "6 conflict aborted clean, marker gone"; else bad "6 conflict must abort clean"; fi

# 7 — a DIRTY working tree is refused early (commit/stash), NOT misreported as a reconcile conflict
echo v1 > junk; git add junk; git commit -q -m junk; echo v2 > junk
out7=$(bash "$lander" 2>&1)
case "$out7" in *"uncommitted changes"*) ok "7 dirty tree refused early (commit/stash)";; *) bad "7 dirty tree must be refused: $out7";; esac
git checkout -q -- junk 2>/dev/null || true

# 8 — the lander fails CLOSED when the default branch is unresolvable (origin/HEAD unset here)
out8=$( ( unset GOV_DEFAULT_BRANCH; bash "$lander" 2>&1 ) )
case "$out8" in *"determine the default branch"*) ok "8 unresolvable default → fail closed";; *) bad "8 expected fail-closed: $out8";; esac

# 9 — a push gated by the declared STUB is not a landing: with LANDER_MARKER declared, push-main lands
#     the push under GOV_GATE_CMD_TEST, writes NO marker, and says why. Without this, a stub-gated push
#     leaves exactly the artifact `unattended.sh --landed` accepts (TOOL-aRepatriatedFork-5).
#     Back onto origin first: case 6 left a conflicting commit that would stop the reconcile.
git fetch -q origin main && git reset -q --hard origin/main
printf 'LANDER_MARKER=unattended-landed\n' > .unattended.conf
git add .unattended.conf && git commit -q -m lander-conf
gcd=$(cd "$(git rev-parse --git-common-dir)" && pwd)
rm -f "$gcd/unattended-landed"
out9=$(bash "$lander" 2>&1); rc9=$?
if [ "$rc9" -ne 0 ]; then bad "9 push-main should land under the stub: $out9"
elif [ -f "$gcd/unattended-landed" ]; then bad "9 a STUB-gated push wrote the lander marker: $(cat "$gcd/unattended-landed")"
else
  case "$out9" in
    *"NOT writing the lander marker"*) ok "9 a STUB-gated landing writes no lander marker, and says so" ;;
    *) bad "9 the marker was withheld without saying why: $out9" ;;
  esac
fi

# 9b — ITS CONTROL: the same lander with a TRACKED bar and no escape writes the marker naming the
#      pushed commit. Without it, 9 passes on a push-main that never writes a marker at all.
#      The bar is DECLARED as the conf's GATE_CMD, since the hook refuses an undeclared one (closing
#      review round 1 M1), and the marker names it by class and path after the pushed commit.
printf '#!/usr/bin/env bash\nexit 0\n' > bar.sh
printf 'GATE_CMD="bash bar.sh"\n' >> .unattended.conf
git add bar.sh .unattended.conf && git commit -q -m tracked-bar
out9b=$( ( unset GOV_GATE_CMD_TEST; GOV_GATE_CMD="bash bar.sh" bash "$lander" 2>&1 ) ); rc9b=$?
if [ "$rc9b" -eq 0 ] && grep -q "$(git rev-parse HEAD) by push-main bar tracked bar.sh " "$gcd/unattended-landed" 2>/dev/null; then
  ok "9b control — a push gated by a tracked bar writes the lander marker naming the pushed commit and the bar"
else
  bad "9b a tracked-bar landing did not write its marker naming the bar (rc $rc9b): $out9b | $(cat "$gcd/unattended-landed" 2>/dev/null)"
fi
# SG AC4 (TOOL-aSignalledHook-1) — and the hook that allowed 9b's push says so: its allow record
#      names the pushed commit, which is the record the lander now requires before it says landed.
if [ "$(cut -f1 "$gitdir/pre-push-allow" 2>/dev/null)" = "$(git rev-parse HEAD)" ]; then
  ok "SG AC4 a gated landing leaves the hook's allow record naming the pushed commit"
else
  bad "SG AC4 the allow record after 9b reads '$(cat "$gitdir/pre-push-allow" 2>/dev/null)', not $(git rev-parse --short HEAD)"
fi

# SG AC3 (TOOL-aSignalledHook-1) — A PUSH GIT CALLS SUCCESSFUL WITH NO HOOK VERDICT. On Git for Windows
#      a hook killed by a signal, KILL included, reads to git as exit 0, and 69e0ff0f landed that way.
#      The stand-in reproduces what such a hook leaves, on any platform: it vets the bar as `default`,
#      as the real hook does before its bar runs, and ends 0 with no allow record. The lander must say
#      the push landed UNGATED, exit 4 and withhold the marker; before the record existed it wrote one.
mkdir -p "$tmp/killed-hook"
printf '#!/usr/bin/env bash\nprintf "default\\tstub-bar.sh\\t0\\n" > "$(git rev-parse --git-dir)/pre-push-bar"\nexit 0\n' \
  > "$tmp/killed-hook/pre-push"
chmod +x "$tmp/killed-hook/pre-push"
git commit -q --allow-empty -m sg-ac3
rm -f "$gcd/unattended-landed"
git config core.hooksPath "$tmp/killed-hook"
outsg=$( ( unset GOV_GATE_CMD_TEST; bash "$lander" 2>&1 ) ); rcsg=$?
git config core.hooksPath .githooks
case "$rcsg|$([ -f "$gcd/unattended-landed" ] && echo marker || echo none)|$(git -C "$tmp/remote.git" rev-parse main)" in
  "4|none|$(git rev-parse HEAD)")
    case "$outsg" in
      *"landed UNGATED"*) ok "SG AC3 a push with no hook allow record is reported landed UNGATED, exit 4, no lander marker" ;;
      *) bad "SG AC3 exit 4 and no marker, but the UNGATED line is missing: $outsg" ;;
    esac ;;
  0*) bad "SG AC3 the lander called a push with no hook verdict landed (rc 0): $outsg" ;;
  *) bad "SG AC3 expected rc 4, no marker and the remote at HEAD, got rc $rcsg marker $([ -f "$gcd/unattended-landed" ] && echo yes || echo no): $outsg" ;;
esac
# SG re-run (closing review round 1) — NOTHING PUSHED IS NOT UNGATED. The remote now holds HEAD, so git
#      runs the real hook with no ref lines, it exits as skip-nondefault and writes no allow record, and
#      git still exits 0. The lander must say nothing was pushed, not that a hook was killed.
outre=$( ( unset GOV_GATE_CMD_TEST; bash "$lander" 2>&1 ) ); rcre=$?
case "$rcre|$outre" in
  *"landed UNGATED"*) bad "SG re-run a push of nothing was reported landed UNGATED (rc $rcre): $outre" ;;
  "0|"*"already held"*"nothing was pushed"*) ok "SG re-run a lander with nothing to push says so and exits 0, not UNGATED" ;;
  *) bad "SG re-run expected rc 0 and 'nothing was pushed', got rc $rcre: $outre" ;;
esac

# H1 — ONE CHANNEL (closing review round 1 H1). The hook and this lander used to answer "was the bar a
#      stub?" from two environments, and the hook's includes whatever gate-env.sh sets. Here a
#      COMMITTED gate-env.sh sets the escape and names `true`, over a default bar that would be RED
#      (this fixture has no runner at all). The lander's own environment carries no escape, and it
#      must still withhold the marker, because the hook's verdict says `stub`.
mkdir -p .githooks
printf 'GOV_GATE_CMD_TEST=1\nGOV_GATE_CMD=true\n' > .githooks/gate-env.sh
git add .githooks/gate-env.sh && git commit -q -m h1-env
rm -f "$gcd/unattended-landed"
outh1=$( ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; bash "$lander" 2>&1 ) ); rch1=$?
if [ -f "$gcd/unattended-landed" ]; then
  bad "H1 a stub set by a committed gate-env.sh still got the lander marker: $(cat "$gcd/unattended-landed")"
else
  case "$rch1:$outh1" in
    0:*"STUB"*"NOT writing the lander marker"*) ok "H1 a stub set by gate-env.sh lands with NO marker, read from the hook's verdict" ;;
    *) bad "H1 expected a landing with the marker withheld as a STUB (rc $rch1): $outh1" ;;
  esac
fi
git rm -q .githooks/gate-env.sh && git commit -q -m h1-env-gone

# H1b — the same file UNTRACKED and hidden by .git/info/exclude, which `git status` never reports, so
#       neither dirty check sees it. The hook must refuse to source it, so nothing lands and no marker.
printf 'GOV_GATE_CMD_TEST=1\nGOV_GATE_CMD=true\n' > .githooks/gate-env.sh
mkdir -p "$gitdir/info"; cp "$gitdir/info/exclude" "$tmp/exclude.keep" 2>/dev/null || : > "$tmp/exclude.keep"
printf '.githooks/gate-env.sh\n' >> "$gitdir/info/exclude"
before1b=$(git -C "$tmp/remote.git" rev-parse main)
outh1b=$( ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; bash "$lander" 2>&1 ) ); rch1b=$?
if [ -f "$gcd/unattended-landed" ]; then
  bad "H1b an excluded gate-env.sh setting the escape still got the lander marker: $(cat "$gcd/unattended-landed")"
elif [ "$before1b" != "$(git -C "$tmp/remote.git" rev-parse main)" ]; then
  bad "H1b an excluded gate-env.sh was sourced and the push LANDED (rc $rch1b): $outh1b"
else
  case "$outh1b" in
    *"gate-env.sh"*"bar-refused"*) ok "H1b an excluded gate-env.sh is refused before it is sourced: no landing, no marker" ;;
    *) bad "H1b nothing landed, but not for the stated reason (rc $rch1b): $outh1b" ;;
  esac
fi
rm -f .githooks/gate-env.sh; cp "$tmp/exclude.keep" "$gitdir/info/exclude"

# 11 — an untracked file in the SUPERPROJECT blocks (S3). `-uno`, this lander's old definition of
#      dirty, passed it, and the bar then certified a file the push did not carry.
echo 'x = 1' > brand_new_module.py
out11=$(bash "$lander" 2>&1)
case "$out11" in
  *"uncommitted changes"*"brand_new_module.py"*) ok "11 an untracked superproject file blocks, and is named" ;;
  *) bad "11 an untracked superproject file must block: $out11" ;;
esac
rm -f brand_new_module.py

# 12 — no wording in the bar's output can FAKE a race or an outage (S2; adopter ic's ABL-aWeighedAssay-2).
#      The remote refuses by pre-receive while the stub, GREEN, floods both poison words. The remote
#      does not move and the hook wrote no verdict, so the one correct reading is "reachable,
#      unchanged, unclaimed", reported once, after exactly one bar run. A re-gate is the regression.
cat > "$tmp/noise.sh" <<'NOISE'
#!/usr/bin/env bash
echo "  ! [rejected] some-fixture -> some-fixture (fetch first, stale info)"
echo "  worker: connection reset by peer, could not read from remote"
exit 0
NOISE
git commit -q --allow-empty -m c12
before12=$(git -C "$tmp/remote.git" rev-parse main)
mkdir -p "$tmp/remote.git/hooks"   # the remote is initialised with no template, so no hooks dir
printf '#!/bin/sh\nexit 1\n' > "$tmp/remote.git/hooks/pre-receive"; chmod +x "$tmp/remote.git/hooks/pre-receive"
out12=$(GOV_GATE_CMD="bash $tmp/noise.sh" bash "$lander" 2>&1); rc12=$?
rm -f "$tmp/remote.git/hooks/pre-receive"
gates12=$(printf '%s\n' "$out12" | grep -c 'gating + pushing')
if [ "$before12" != "$(git -C "$tmp/remote.git" rev-parse main)" ]; then
  bad "12 fixture broken: the remote accepted a push it was told to refuse"
else
  case "$out12" in
    *"advanced during the gate"*|*"moving faster than the gate"*) bad "12 the bar's output faked a race; the bar ran $gates12 time(s)" ;;
    *"could not reach"*) bad "12 the bar's output faked an unreachable remote: $out12" ;;
    *) if [ "$rc12" = 1 ] && [ "$gates12" = 1 ]; then ok "12 the bar's own words cannot fake a race or an outage (one run, rc 1)"
       else bad "12 expected one bar run and rc 1 (rc $rc12, runs $gates12): $out12"; fi ;;
  esac
fi

# AC5 — an unreachable remote with no verdict is reported only after a PROBE of it fails. The push
#       URL is pointed at nothing while the fetch URL still works, so the push dies before the hook.
git remote set-url --push origin "$tmp/nowhere.git"
out5u=$(bash "$lander" 2>&1); rc5u=$?
git config --unset remote.origin.pushurl
case "$rc5u:$out5u" in
  1:*"could not reach origin"*"probe"*) ok "AC5 an unreachable push URL is reported after its probe fails" ;;
  *) bad "AC5 expected the probed-unreachable verdict at rc 1, got rc $rc5u: $out5u" ;;
esac

# 13 — ONE definition of dirty, in the lander and the hook alike (S3). When they disagreed at adopter ic
#      (ARCH-dWaryGatepost-1) the lander cleared a push the hook then refused. Compared as a STRING:
#      the failure this gates is a divergence in the flag.
DIRTY_PRED='git status --porcelain --ignore-submodules=untracked'
pm_hits=$(grep -cF -- "$DIRTY_PRED" "$HERE/push-main.sh" || true)
hk_hits=$(grep -cF -- "$DIRTY_PRED" "$SRC/.githooks/pre-push" || true)
if [ "${pm_hits:-0}" -ge 1 ] && [ "${hk_hits:-0}" -ge 1 ]; then
  ok "13 the lander and the hook share one dirty definition"
else
  bad "13 the dirty definition diverged: push-main.sh ${pm_hits:-0}, .githooks/pre-push ${hk_hits:-0} occurrence(s) of '$DIRTY_PRED'"
fi

# 14 — and the RETIRED spelling does not come back beside it, which is what a careless merge makes.
for f in "$HERE/push-main.sh" "$SRC/.githooks/pre-push"; do
  if grep -qE 'git status --porcelain -uno' "$f"; then bad "14 ${f##*/} carries the retired '-uno' dirty definition"
  else ok "14 ${f##*/} carries no retired dirty definition"; fi
done

# AC1 — a remote NOT named origin (adopter ic's node `d` names it after the project): the lander resolves the remote
#       first and reads ITS HEAD, and the hook reads the remote git names in $1. With no
#       GOV_DEFAULT_BRANCH exported, the pre-S1 lander exited 2 before its first fetch.
git init -q --template= --bare "$tmp/mirror.git"
setup_repo "$tmp/wi" mirror "$tmp/mirror.git"
git push -q --no-verify mirror main
git -C "$tmp/mirror.git" symbolic-ref HEAD refs/heads/main
git remote set-head mirror main >/dev/null 2>&1
git commit -q --allow-empty -m ci
out1i=$( ( unset GOV_DEFAULT_BRANCH; bash "$lander" 2>&1 ) ); rc1i=$?
if [ "$rc1i" -eq 0 ] && [ "$(git -C "$tmp/mirror.git" rev-parse main)" = "$(git rev-parse HEAD)" ]; then
  ok "AC1 a remote named mirror lands with no GOV_DEFAULT_BRANCH"
else
  bad "AC1 a remote named mirror did not land (rc $rc1i): $out1i"
fi
# ...and with SEVERAL remotes and none configured for the branch it refuses rather than guess (F2).
git remote add second "$tmp/remote.git"
out2r=$( ( unset GOV_DEFAULT_BRANCH; bash "$lander" 2>&1 ) ); rc2r=$?
case "$rc2r:$out2r" in
  2:*"GOV_REMOTE"*) ok "AC1 several remotes and none configured is refused, naming GOV_REMOTE" ;;
  *) bad "AC1 expected a refusal naming GOV_REMOTE with two remotes, got rc $rc2r: $out2r" ;;
esac
cd "$tmp" || exit 2

# ---- THE IN-PLACE LANDING FLAGS — TOOL-dDerivedDocket-2 -----------------------------------------
# A SECOND fixture, because these cases need a shape the one above does not have: a bare remote, a
# primary tree with the default branch checked out, and a LINKED WORKTREE on a run branch. Every arm
# below was observed RED against a staged break of the flag it covers before it landed — the push
# spelled as the local default branch, the carry set computed as T minus that branch, a precondition
# that accepts any two-parent HEAD, an observation failure sharing exit 2 with an argument refusal,
# an unrecognised argument falling through to the attended path, a prepare that merges the tip INTO
# the branch, and a conflict path that does not put the branch back.
#
# FOUR CASES PIN MESSAGE TEXT, and an edit to any of these strands its case silently — the case goes
# on passing for the wrong reason or fails for a reason that is not a defect. They are `--prepare`
# in case 18, `git merge origin/main` in case 19, `landed main on origin` in case 21b, and the whole
# merge subject in case 9. Change one of those strings and change its case in the same commit. The
# F7 arms pin a SHAPE as well: the carry line's `<sha8> · <build> ·` and its trailing `FOREIGN`.
git init -q --template= --bare "$tmp/remote2.git"
setup_repo "$tmp/work2" origin "$tmp/remote2.git"
echo seed > src-seed.txt; git add src-seed.txt; git commit -q -m seed
git push -q --no-verify origin main
git -C "$tmp/remote2.git" symbolic-ref HEAD refs/heads/main
git clone -q "$tmp/remote2.git" "$tmp/racer2"
git worktree add -q "$tmp/wt" -b feat main

build_main() {  # local main back onto the remote tip; the caller adds whatever it needs on top
  git -C "$tmp/work2" fetch -q origin
  git -C "$tmp/work2" reset -q --hard origin/main
}
build_feat() {  # the run branch, off the remote tip, carrying one commit of this build
  git -C "$tmp/wt" checkout -q -B feat "$(git -C "$tmp/work2" rev-parse refs/remotes/origin/main)"
  echo "u1 $RANDOM" > "$tmp/wt/src-u1.txt"
  git -C "$tmp/wt" add src-u1.txt
  git -C "$tmp/wt" commit -q -m "TOOL-tFix-1: unit one"
}
run_wt() { ( cd "$tmp/wt" && bash "$lander" "$@" ) ; }

# 9 — --prepare makes the merge the whole design rests on: onto the ADVERTISED tip, branch moved
build_main; build_feat
oldb=$(git -C "$tmp/wt" rev-parse HEAD)
R=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
out9=$(run_wt --prepare --slug tFix 2>&1); rc9=$?
t=$(git -C "$tmp/wt" rev-parse HEAD)
p1=$(git -C "$tmp/wt" rev-parse HEAD^1); p2=$(git -C "$tmp/wt" rev-parse HEAD^2)
subj=$(git -C "$tmp/wt" log -1 --format=%s)
[ "$rc9" = 0 ] && [ "$p1" = "$R" ] && [ "$p2" = "$oldb" ] \
  && [ "$(git -C "$tmp/wt" rev-parse refs/heads/feat)" = "$t" ] \
  && [ "$(git -C "$tmp/wt" symbolic-ref --short HEAD)" = feat ] \
  && case "$subj" in "merge: tFix — land onto origin/main at ${R:0:8}") true ;; *) false ;; esac \
  && ok "9 prepared: first parent the advertised tip, second the old tip, branch moved, subject names the slug" \
  || bad "9 rc=$rc9 subj='$subj' p1=${p1:0:8} R=${R:0:8} p2=${p2:0:8} old=${oldb:0:8} $out9"
# 9b — and NO unit id in it: build_commit joins a commit to a unit by the id as a whole token, so an
# id here would make the landing merge some unit's build commit.
case "$subj" in *TOOL-*|*PLAY-*|*KICK-*|*DEPL-*) bad "9b the merge subject names a unit id: $subj" ;;
  *) ok "9b the merge subject names no unit id" ;; esac

# 10 — --prepared agrees with that, and writes nothing
st=$(git -C "$tmp/wt" rev-parse HEAD)$(git -C "$tmp/wt" rev-parse refs/heads/feat)$(git -C "$tmp/wt" status --porcelain)
out10=$(run_wt --prepared --slug tFix 2>&1); rc10=$?
st2=$(git -C "$tmp/wt" rev-parse HEAD)$(git -C "$tmp/wt" rev-parse refs/heads/feat)$(git -C "$tmp/wt" status --porcelain)
[ "$rc10" = 0 ] && [ "$st" = "$st2" ] && ok "10 --prepared 0 on a prepared HEAD, nothing moved" \
  || bad "10 rc=$rc10 $out10"

# 11 — the unattended kit's own build_commit answers the same before and after the prepare, which is
#      what the merge subject's missing unit id buys. The library is LOCATED and never spelled: this
#      file ships to adopters who install kits at their own prefix, or who carry no such kit at all,
#      and a skip that looks like a pass is indistinguishable from coverage.
lib=$(git -C "$SRC" ls-files -- '*lib-unattended.sh' 2>/dev/null | head -1)
if [ -n "$lib" ] && [ -f "$SRC/$lib" ]; then
  ( cd "$tmp/wt" && . "$SRC/$lib"
    build_commit "$(git rev-parse HEAD^2^)..HEAD^2" TOOL-tFix-1 memory/builds/tFix "" "" > "$tmp/bc-before" )
  ( cd "$tmp/wt" && . "$SRC/$lib"
    build_commit "$(git rev-parse HEAD^1)..HEAD" TOOL-tFix-1 memory/builds/tFix "" "" > "$tmp/bc-after" )
  if [ -s "$tmp/bc-before" ] && [ "$(cat "$tmp/bc-before")" = "$(cat "$tmp/bc-after")" ]; then
    ok "11 build_commit returns the same commit before and after --prepare"
  else
    bad "11 before=$(cat "$tmp/bc-before" 2>/dev/null) after=$(cat "$tmp/bc-after" 2>/dev/null)"
  fi
else
  echo "  skip — 11 build_commit: this tree carries no unattended-kit library, so the join this case grades does not exist here"
fi

# 12 — the hook refuses an unmarked worktree push; --land is accepted; and the foreign commit
#      sitting unpushed on local main stays there, which is the defect these flags close.
git -C "$tmp/work2" commit -q --allow-empty -m "TOOL-zOther-3: another build unit"
foreign=$(git -C "$tmp/work2" rev-parse HEAD)
if ( cd "$tmp/wt" && git push -q origin HEAD:refs/heads/main 2>/dev/null ); then
  bad "12 raw worktree push must be refused (no marker)"; else ok "12 raw worktree push refused"; fi
out12=$(run_wt --land --slug tFix 2>&1); rc12=$?
rem=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc12" = 0 ] && [ "$rem" = "$t" ] && ok "12b --land pushed exactly the prepared merge" \
  || bad "12b rc=$rc12 remote=${rem:0:8} T=${t:0:8} $out12"
if git -C "$tmp/remote2.git" merge-base --is-ancestor "$foreign" "$rem" 2>/dev/null; then
  bad "12c the foreign commit on local main reached the remote"
else ok "12c the foreign commit on local main did not reach the remote"; fi
[ -f "$(git -C "$tmp/wt" rev-parse --git-dir)/push-main-active" ] && bad "12d marker leaked" || ok "12d marker cleared"

# 13 — merged in, that same commit refuses the landing, and --carry names the sha --land names
build_main
git -C "$tmp/work2" commit -q --allow-empty -m "TOOL-zOther-4: another build unit again"
foreign2=$(git -C "$tmp/work2" rev-parse HEAD)
build_feat
git -C "$tmp/wt" merge -q --no-ff -m "merge local main" main
run_wt --prepare --slug tFix >/dev/null 2>&1
outc=$(run_wt --carry --slug tFix 2>&1); rcc=$?
outl=$(run_wt --land --slug tFix 2>&1); rcl=$?
rem2=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rcc" = 1 ] && [ "$rcl" = 1 ] && [ "$rem2" = "$rem" ] \
  && case "$outc" in *"${foreign2:0:8}"*) true ;; *) false ;; esac \
  && case "$outl" in *"${foreign2:0:8}"*zOther*) true ;; *) false ;; esac \
  && ok "13 --carry and --land both refuse, both naming ${foreign2:0:8} as zOther, remote unchanged" \
  || bad "13 rcc=$rcc rcl=$rcl carry=$outc land=$outl"

# 14 — a carry of THIS build's own commit is not foreign and lands
build_main
mkdir -p "$tmp/work2/memory/builds/tFix"
echo note > "$tmp/work2/memory/builds/tFix/NOTE.md"
git -C "$tmp/work2" add memory/builds/tFix/NOTE.md
git -C "$tmp/work2" commit -q -m "records for this build"
ownc=$(git -C "$tmp/work2" rev-parse HEAD)
build_feat
git -C "$tmp/wt" merge -q --no-ff -m "merge local main" main
run_wt --prepare --slug tFix >/dev/null 2>&1
out14=$(run_wt --carry --slug tFix 2>&1); rc14=$?
out14b=$(run_wt --land --slug tFix 2>&1); rc14b=$?
rem=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc14" = 0 ] && [ "$rc14b" = 0 ] && [ "$rem" = "$(git -C "$tmp/wt" rev-parse HEAD)" ] \
  && case "$out14" in *"${ownc:0:8}"*tFix*) true ;; *) false ;; esac \
  && ok "14 a carry attributed to this build by its folder lands" \
  || bad "14 rc-carry=$rc14 rc-land=$rc14b carry=$out14 land=$out14b"

# 15 — and one that names no unit id and touches no build folder is `unknown`, which is foreign
build_main
echo x > "$tmp/work2/src-loose.txt"
git -C "$tmp/work2" add src-loose.txt
git -C "$tmp/work2" commit -q -m "a commit naming nothing"
unkn=$(git -C "$tmp/work2" rev-parse HEAD)
build_feat
git -C "$tmp/wt" merge -q --no-ff -m "merge local main" main
run_wt --prepare --slug tFix >/dev/null 2>&1
out15=$(run_wt --carry --slug tFix 2>&1); rc15=$?
[ "$rc15" = 1 ] && case "$out15" in *"${unkn:0:8}"*unknown*) true ;; *) false ;; esac \
  && ok "15 an unattributable carry is named unknown and refuses" || bad "15 rc=$rc15 $out15"

# F7 — OWNERSHIP IS CLAIMED ONLY AT A SUBJECT'S HEAD, AND THE BUILD FOLDERS DECIDE FIRST (closing diff
#      review round 1, F7). The rule these arms replace took the first unit id ANYWHERE in the subject
#      as the owner, before the folders. Each arm puts one commit on local main and merges it in.
build_carry() {  # subject · build folder to touch, or "" -> the carry's sha; B merged local main and is prepared
  build_main
  if [ -n "$2" ]; then
    mkdir -p "$tmp/work2/memory/builds/$2"
    echo "row $RANDOM" >> "$tmp/work2/memory/builds/$2/BACKLOG.md"
    git -C "$tmp/work2" add "memory/builds/$2/BACKLOG.md"
  fi
  git -C "$tmp/work2" commit -q --allow-empty -m "$1"
  git -C "$tmp/work2" rev-parse HEAD
  build_feat >/dev/null 2>&1
  git -C "$tmp/wt" merge -q --no-ff -m "merge local main" main >/dev/null 2>&1
  run_wt --prepare --slug tFix >/dev/null 2>&1
}
# F7a — the finding's own shape: another build's records commit, touching ONLY its own folder, whose
#       subject cites this build's unit id first. Before the fix `--land` published it unflagged.
f7a=$(build_carry "records(zOther): TOOL-tFix-1 closes behind TOOL-zOther-2" zOther)
remf7=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
outf7a=$(run_wt --land --slug tFix 2>&1); rcf7a=$?
[ "$rcf7a" = 1 ] && [ "$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')" = "$remf7" ] \
  && case "$outf7a" in *"${f7a:0:8} · zOther ·"*FOREIGN*) true ;; *) false ;; esac \
  && ok "F7a another build's commit citing this build's id first is FOREIGN, and --land refuses it with the remote unchanged" \
  || bad "F7a rc=$rcf7a $outf7a"
# F7b — a CITATION alone is no claim: no build folder, and this build's id cited after the head.
f7b=$(build_carry "records: TOOL-tFix-1 cited by a commit that claims nothing" "")
outf7b=$(run_wt --carry --slug tFix 2>&1); rcf7b=$?
[ "$rcf7b" = 1 ] && case "$outf7b" in *"${f7b:0:8} · unknown ·"*FOREIGN*) true ;; *) false ;; esac \
  && ok "F7b an id cited after the subject's head claims nothing, so the carry is unknown and refuses" \
  || bad "F7b rc=$rcf7b $outf7b"
# F7c — the reverse: every folder is this build's, and the head claims another build.
f7c=$(build_carry "records(zOther): disposes TOOL-tFix-1 in its home build" tFix)
outf7c=$(run_wt --carry --slug tFix 2>&1); rcf7c=$?
[ "$rcf7c" = 1 ] && case "$outf7c" in *"${f7c:0:8} · zOther ·"*FOREIGN*) true ;; *) false ;; esac \
  && ok "F7c a head claiming another build is FOREIGN even when every folder it touches is this build's" \
  || bad "F7c rc=$rcf7c $outf7c"
# F7d — ITS CONTROL: this build's head claim citing a foreign id, touching no folder, is this build's.
#       Without it, the three arms above pass on a rule that refuses every subject carrying an id.
f7d=$(build_carry "records(tFix): TOOL-zOther-3 is cited here, not owned" "")
outf7d=$(run_wt --carry --slug tFix 2>&1); rcf7d=$?
[ "$rcf7d" = 0 ] && case "$outf7d" in *"${f7d:0:8} · tFix ·"*) true ;; *) false ;; esac \
  && ok "F7d control — this build's head claim citing another build's id is this build's and does not refuse" \
  || bad "F7d rc=$rcf7d $outf7d"

# 16 — a single-parent records commit on top of T is accepted, and HEAD is what gets pushed
build_main; build_feat
run_wt --prepare --slug tFix >/dev/null 2>&1
git -C "$tmp/wt" commit -q --allow-empty -m "close records"
out16p=$(run_wt --prepared --slug tFix 2>&1); rc16p=$?
out16=$(run_wt --land --slug tFix 2>&1); rc16=$?
rem=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc16p" = 0 ] && [ "$rc16" = 0 ] && [ "$rem" = "$(git -C "$tmp/wt" rev-parse HEAD)" ] \
  && ok "16 a records commit on the prepared merge lands, HEAD and not T being what was pushed" \
  || bad "16 rc-prepared=$rc16p rc-land=$rc16 prepared=$out16p land=$out16"

# 17 — a SECOND merge on top of it is not a prepared merge, and both readers say so
build_main
git -C "$tmp/wt" checkout -q -B side "$(git -C "$tmp/work2" rev-parse refs/remotes/origin/main)"
echo s > "$tmp/wt/src-side.txt"; git -C "$tmp/wt" add src-side.txt; git -C "$tmp/wt" commit -q -m "a side line"
build_feat
run_wt --prepare --slug tFix >/dev/null 2>&1
git -C "$tmp/wt" merge -q --no-ff -m "a second merge" side
out17p=$(run_wt --prepared --slug tFix 2>&1); rc17p=$?
out17=$(run_wt --land --slug tFix 2>&1); rc17=$?
rem2=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc17p" = 1 ] && [ "$rc17" = 1 ] && [ "$rem2" = "$rem" ] \
  && ok "17 a second merge on the prepared one is refused by --prepared and by --land alike" \
  || bad "17 rc-prepared=$rc17p rc-land=$rc17 $out17"

# 18 — the attended reconcile shape (a plain merge of the remote INTO the branch) is refused, and
#      the refusal names the flag that makes the right shape
build_main; build_feat
git -C "$tmp/racer2" pull -q; git -C "$tmp/racer2" commit -q --allow-empty -m "remote moved"
git -C "$tmp/racer2" push -q origin main
git -C "$tmp/wt" fetch -q origin main
git -C "$tmp/wt" merge -q --no-ff -m "reconcile" FETCH_HEAD
out18p=$(run_wt --prepared --slug tFix 2>&1); rc18p=$?
out18=$(run_wt --land --slug tFix 2>&1); rc18=$?
[ "$rc18p" = 1 ] && [ "$rc18" = 1 ] && case "$out18" in *--prepare*) true ;; *) false ;; esac \
  && ok "18 a plain reconcile is refused and the refusal names --prepare" \
  || bad "18 rc-prepared=$rc18p rc-land=$rc18 $out18"

# 19 — a conflicting prepare leaves the branch exactly where it was, checked out, with a clean tree
build_main; build_feat
git -C "$tmp/racer2" pull -q; echo racer > "$tmp/racer2/src-seed.txt"; git -C "$tmp/racer2" add src-seed.txt
git -C "$tmp/racer2" commit -q -m "racer edits seed"; git -C "$tmp/racer2" push -q origin main
echo mine > "$tmp/wt/src-seed.txt"; git -C "$tmp/wt" add src-seed.txt
git -C "$tmp/wt" commit -q -m "TOOL-tFix-2: mine edits seed"
before19=$(git -C "$tmp/wt" rev-parse refs/heads/feat)
out19=$(run_wt --prepare --slug tFix 2>&1); rc19=$?
[ "$rc19" = 1 ] \
  && [ "$(git -C "$tmp/wt" rev-parse refs/heads/feat)" = "$before19" ] \
  && [ "$(git -C "$tmp/wt" symbolic-ref --short HEAD 2>/dev/null)" = feat ] \
  && [ -z "$(git -C "$tmp/wt" status --porcelain)" ] \
  && case "$out19" in *"git merge origin/main"*) true ;; *) false ;; esac \
  && ok "19 conflict: branch unmoved, HEAD on it, tree clean, the reconcile to run named" \
  || bad "19 rc=$rc19 head=$(git -C "$tmp/wt" symbolic-ref --short HEAD 2>/dev/null) $out19"

# 20 — the remote advancing DURING the gate re-prepares onto the new tip and lands, with the merge
#      that was already graded still an ancestor of what is finally pushed
build_main
git -C "$tmp/wt" checkout -q -B feat "$(git -C "$tmp/work2" rev-parse refs/remotes/origin/main)"
echo u2 > "$tmp/wt/src-u2.txt"; git -C "$tmp/wt" add src-u2.txt
git -C "$tmp/wt" commit -q -m "TOOL-tFix-3: unit three"
run_wt --prepare --slug tFix >/dev/null 2>&1
t20=$(git -C "$tmp/wt" rev-parse HEAD)
touch "$tmp/race2-once"
out20=$(run_wt --land --slug tFix 2>&1); rc20=$?
rm -f "$tmp/race2-once"
rem=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc20" = 0 ] && [ "$rem" = "$(git -C "$tmp/wt" rev-parse HEAD)" ] \
  && git -C "$tmp/wt" merge-base --is-ancestor "$t20" "$rem" \
  && ok "20 raced, re-prepared, landed; the first prepared merge is an ancestor of the pushed tip" \
  || bad "20 rc=$rc20 $out20"

# SG AC3b (TOOL-aSignalledHook-1, closing review round 1) — the --land path, the one 69e0ff0f took: a
#      prepared merge pushed through the killed-hook stand-in from SG AC3 is reported landed UNGATED
#      and exits 4. SG AC3 drives only the attended path, so this guard could be deleted unseen.
build_main
git -C "$tmp/wt" checkout -q -B feat "$(git -C "$tmp/work2" rev-parse refs/remotes/origin/main)"
echo u3 > "$tmp/wt/src-u3.txt"; git -C "$tmp/wt" add src-u3.txt
git -C "$tmp/wt" commit -q -m "TOOL-tFix-4: unit four"
run_wt --prepare --slug tFix >/dev/null 2>&1
t3b=$(git -C "$tmp/wt" rev-parse HEAD)
git -C "$tmp/wt" config core.hooksPath "$tmp/killed-hook"
out3b=$( ( unset GOV_GATE_CMD_TEST; run_wt --land --slug tFix 2>&1 ) ); rc3b=$?
git -C "$tmp/wt" config core.hooksPath .githooks
case "$rc3b|$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')|$out3b" in
  "4|$t3b|"*"landed UNGATED"*) ok "SG AC3b --land through a hook that left no allow record reports landed UNGATED and exits 4" ;;
  0*) bad "SG AC3b --land called a push with no hook verdict landed (rc 0): $out3b" ;;
  *) bad "SG AC3b expected rc 4, the remote at ${t3b:0:8} and landed UNGATED, got rc $rc3b: $out3b" ;;
esac

# 21 — a MISTYPED flag refuses instead of falling through to the attended path, which from this tree
#      would push the local default branch. Run where that fallthrough would actually land.
rembefore=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
out21=$( cd "$tmp/work2" && git checkout -q main && bash "$lander" --lnad 2>&1 ); rc21=$?
remafter=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc21" = 2 ] && [ "$rembefore" = "$remafter" ] && ok "21 --lnad exits 2 and pushes nothing" \
  || bad "21 rc=$rc21 $out21"
# 21b — and the no-argument invocation is still the BASE attended landing
out21b=$( cd "$tmp/work2" && bash "$lander" 2>&1 ); rc21b=$?
[ "$rc21b" = 0 ] && case "$out21b" in *"landed main on origin"*) true ;; *) false ;; esac \
  && ok "21b the no-argument invocation still lands from the primary tree" || bad "21b rc=$rc21b $out21b"

# 22 — an OBSERVATION failure exits 3 and never 2, so a driver cannot read a network fault as a
#      misdeclared flag. Two causes, one code.
git -C "$tmp/wt" symbolic-ref -d refs/remotes/origin/HEAD 2>/dev/null || true
out22=$( cd "$tmp/wt" && unset GOV_DEFAULT_BRANCH && bash "$lander" --carry --slug tFix 2>&1 ); rc22=$?
[ "$rc22" = 3 ] && ok "22 an undeterminable default branch exits 3" || bad "22 rc=$rc22 $out22"
build_main
git -C "$tmp/wt" checkout -q -B feat "$(git -C "$tmp/work2" rev-parse refs/remotes/origin/main)"
echo u4 > "$tmp/wt/src-u4.txt"; git -C "$tmp/wt" add src-u4.txt
git -C "$tmp/wt" commit -q -m "TOOL-tFix-4: unit four"
run_wt --prepare --slug tFix >/dev/null 2>&1
remb=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
git -C "$tmp/wt" remote set-url origin "$tmp/gone.git"
out22b=$(run_wt --carry --slug tFix 2>&1); rc22b=$?
out22c=$(run_wt --prepared --slug tFix 2>&1); rc22c=$?
git -C "$tmp/wt" remote set-url origin "$tmp/remote2.git"
rema=$(git ls-remote "$tmp/remote2.git" refs/heads/main | awk '{print $1}')
[ "$rc22b" = 3 ] && [ "$rc22c" = 3 ] && [ "$remb" = "$rema" ] \
  && ok "22b an unreachable remote exits 3 from both read-only flags, and pushes nothing" \
  || bad "22b rc-carry=$rc22b rc-prepared=$rc22c $out22b $out22c"

# 23 — TOOL-aMendedFleet-3 AC8: --prepare over a branch carrying a merge that LOSES a definition one
#      parent carried refuses BEFORE the branch moves, naming it. The fixture's sideB adds `fb`; the
#      run branch merges sideB resolving the conflict to its own side, merge `01c22e155`'s shape. The
#      lexicon kit is the directory beside this lander that holds its anchor, copied beside the
#      fixture's lander under the same name, where the lander looks for it. Observed RED against the
#      base lander, which moved the branch to the prepared merge and exited 0.
_ml_lex=$(cd "$HERE" && for d in */; do [ -f "$d/lexicon.py" ] && { printf '%s' "${d%/}"; break; }; done)
if [ -n "$_ml_lex" ]; then
  git init -q --template= --bare "$tmp/remote3.git"
  setup_repo "$tmp/work3" origin "$tmp/remote3.git"
  cp -r "$HERE/$_ml_lex" "./$KIT_REL$_ml_lex"; rm -rf "./$KIT_REL$_ml_lex/__pycache__"
  printf 'LANGS="sh:shell-tokens:parser"\n' > .lexicon.conf
  printf '__pycache__/\n' > .gitignore
  printf 'fa() { :; }\n' > a.sh
  git add -A; git commit -q -m "lexicon and a.sh"
  git push -q --no-verify origin main
  git -C "$tmp/remote3.git" symbolic-ref HEAD refs/heads/main
  git checkout -q -b sideB
  printf 'fa() { echo B; }\nfb() { :; }\n' > a.sh; git commit -q -am "side B"
  git checkout -q -b feat main
  printf 'fa() { echo A; }\n' > a.sh; git commit -q -am "TOOL-tFix-5: side A"
  git merge -q --no-ff --no-commit sideB >/dev/null 2>&1
  printf 'fa() { echo A; }\n' > a.sh; git add a.sh; git commit -q -m "merge sideB, taking side A"
  before23=$(git rev-parse refs/heads/feat)
  out23=$(bash "$lander" --prepare --slug fx 2>&1); rc23=$?
  [ "$rc23" = 1 ] && [ "$(git rev-parse refs/heads/feat)" = "$before23" ] \
    && [ "$(git symbolic-ref --short HEAD 2>/dev/null)" = feat ] \
    && case "$out23" in *"a.sh: fb"*) true ;; *) false ;; esac \
    && ok "23 --prepare refuses a merge losing fb, naming it; the branch is unmoved and checked out" \
    || bad "23 rc=$rc23 head=$(git symbolic-ref --short HEAD 2>/dev/null) $out23"
else
  bad "23 no directory beside this lander holds the lexicon kit, so the merge-loss arm did not run"
fi

# 24 — TOOL-aMendedFleet-65 AC1: --prepare MINTS the kit versions the landing owes INTO the prepared
#      merge. A clone of this repository at its committed HEAD, pushed to a bare remote as main; a
#      branch adds a comment line to the runlog kit's extract.py and is prepared. The merge's diff
#      against its first parent moves KIT_RUNLOG_VERSION to the tip's value plus one, and the lander
#      prints one `mint: runlog` line. Observed RED against the base lander, which merged the move
#      under the old value. Needs gov's deployer beside the lander; an install without one says so.
_mt_gk=$(cd "$HERE" && for d in */; do [ -f "$d/govkit.py" ] && [ -f "$d/registry.toml" ] && { printf '%s' "${d%/}"; break; }; done)
_mt_rl=$(cd "$HERE" && for d in */; do [ -f "$d/runlog_lib.py" ] && { printf '%s' "${d%/}"; break; }; done)
if [ -n "$_mt_gk" ] && [ -n "$_mt_rl" ]; then
  git clone -q --bare "$SRC" "$tmp/remote4.git"
  git clone -q "$tmp/remote4.git" "$tmp/work4"
  (
    cd "$tmp/work4" || exit 1
    git checkout -q -B main "$(git -C "$SRC" rev-parse HEAD)"
    git push -q -f origin main
    git -C "$tmp/remote4.git" symbolic-ref HEAD refs/heads/main
    R4=$(git rev-parse HEAD)
    v0=$(sed -n 's/^KIT_RUNLOG_VERSION = "\([0-9.]*\)".*/\1/p' "${KIT_REL}$_mt_rl/runlog_lib.py")
    v1="${v0%.*}.$(( ${v0##*.} + 1 ))"
    git checkout -q -b feat
    printf '# a comment line, push-main.test case 24\n' >> "${KIT_REL}$_mt_rl/extract.py"
    git commit -q -am "move runlog"
    out24=$(unset GATE_PUSH_BASE; bash "$lander" --prepare --slug tMint 2>/dev/null); rc24=$?
    moved=$(git diff HEAD^1 HEAD -- "${KIT_REL}$_mt_rl/runlog_lib.py" | grep -c "^+KIT_RUNLOG_VERSION = \"$v1\"")
    [ "$rc24" = 0 ] && [ "$(git rev-parse HEAD^1)" = "$R4" ] && [ "$moved" = 1 ] \
      && [ "$(printf '%s\n' "$out24" | grep -c '^mint: runlog')" = 1 ] && [ -z "$(git status --porcelain)" ]
  ) && ok "24 --prepare mints runlog's next version into the prepared merge and says so once" \
    || bad "24 the prepared merge does not carry the minted runlog version (or the tree was left dirty)"
else
  echo "  skip — 24 no govkit deployer or runlog kit beside this lander, so the mint arm did not run"
fi

# 25 — TOOL-aMendedFleet-111 AC2: THIS lander run in a tree that lacks the lexicon and govkit files
#      SKIPS both checks by name. The kits resolve beside the lander, but the files are read under the
#      cwd's toplevel, so before the file test python's exit 2 for a missing script read as a DEAD
#      PROBE and a REFUSED mint. Staged red by removing the two file tests.
if [ -n "$_mt_gk" ] && [ -n "$_ml_lex" ]; then
  git clone -q --bare "$SRC" "$tmp/remote5.git"
  git clone -q "$tmp/remote5.git" "$tmp/work5"
  out25=$(
    cd "$tmp/work5" || exit 1
    git checkout -q -B main "$(git -C "$SRC" rev-parse HEAD)"
    git rm -q -- "${KIT_REL}$_ml_lex/lexicon.py" "${KIT_REL}$_mt_gk/govkit.py"
    # The regeneration goes too (TOOL-aPrimedIndex-8): with it present, `--prepare` regenerates after
    # the mint, the lexicon render cannot read its deleted version, and the landing is refused before
    # the merge-loss check prints the skip this arm asserts. Absent, the lander names that skip too.
    _rg25=$(cd "$HERE" && for d in */; do [ -f "$d/regen.py" ] && { printf '%s' "${d%/}"; break; }; done)
    [ -z "$_rg25" ] || git rm -q -- "${KIT_REL}$_rg25/regen.py"
    git commit -q --no-verify -m "drop the lexicon and govkit files"
    git push -q -f --no-verify origin main
    git -C "$tmp/remote5.git" symbolic-ref HEAD refs/heads/main
    git checkout -q -b feat
    echo u25 > src-u25.txt; git add src-u25.txt 2>/dev/null; git commit -q --no-verify -m "TOOL-tFix-25: unit"
    unset GATE_PUSH_BASE; bash "$HERE/push-main.sh" --prepare --slug tSkip 2>&1
  )
  case "$out25" in *"no lexicon kit beside this lander"*) l25=1 ;; *) l25=0 ;; esac
  case "$out25" in *"no govkit deployer beside this lander"*) g25=1 ;; *) g25=0 ;; esac
  case "$out25" in *"DEAD PROBE"*|*"REFUSED"*) x25=1 ;; *) x25=0 ;; esac
  # TOOL-dSafePassage-8 AC6: the same prepare names the skipped gov-first walk once, with its reason.
  f25=$(printf '%s\n' "$out25" | grep -c 'steps were NOT run on gov first — no govkit deployer beside this lander')
  [ "$l25$g25$x25$f25" = 1101 ] \
    && ok "25 a tree without the lexicon and govkit files skips both checks and the gov-first walk by name, with no DEAD PROBE or REFUSED" \
    || bad "25 lexicon-skip=$l25 govkit-skip=$g25 dead-or-refused=$x25 gov-first-skip-lines=$f25 $out25"
else
  echo "  skip — 25 no govkit deployer or lexicon kit beside this lander, so the missing-file arm did not run"
fi

# ---- THE POST-MERGE BAR AFTER A LANDING — TOOL-aFrugalTurnstile-8 ---------------------------------
# A sixth fixture behind a stub pre-push hook that allows, so a landing costs seconds: a stub post-merge script in
# a run-gates dir beside the fixture lander sleeps 8 s, then writes its argv to $MARK. Each case
# commits its own gate-env declaration and lands; the markers are read once, after one wait. Observed
# RED against the lander at bef97330 (no marker, no line in any case) and GREEN against the change.
git init -q --bare "$tmp/remote6.git"
setup_repo "$tmp/work6" origin "$tmp/remote6.git"
# An ALLOWING stub hook, not none: the lander requires the hook's allow record (TOOL-aSignalledHook-1),
# so a hookless push reads landed UNGATED and exits 4 (TOOL-aPrimedIndex-10).
mkdir -p "$tmp/allow-hook"
printf '#!/usr/bin/env bash\nwhile read -r _ sha _ _; do printf "%%s\\tstub\\n" "$sha" > "$(git rev-parse --git-dir)/pre-push-allow"; done\nexit 0\n' \
  > "$tmp/allow-hook/pre-push"
chmod +x "$tmp/allow-hook/pre-push"
git config core.hooksPath "$tmp/allow-hook"
pmk="./${KIT_REL}run-gates"   # the stub kit dir beside the fixture lander; spelled bare for the install-prefix ban
mkdir -p "$pmk"
printf '#!/usr/bin/env bash\nsleep 8\necho "$*" > "$MARK"\n' > "$pmk/post-merge.sh"
git add -A; git commit -q -m "stub post-merge"
git push -q --no-verify origin main
git -C "$tmp/remote6.git" symbolic-ref HEAD refs/heads/main
gcd6=$(cd "$(git rev-parse --git-common-dir)" && pwd)
run_pm_case() {  # case · gate-env GATE_POST_MERGE line or '' -> pm_out pm_rc pm_secs pm_sha
  export MARK="$tmp/pm-mark-$1"
  printf 'GATE_JOBS=1\n%s' "$2" > .githooks/gate-env.sh
  echo "$1 $RANDOM" > "src-pm-$1.txt"; git add -A; git commit -q -m "pm case $1"
  local s; s=$(date +%s)
  pm_out=$(bash "$lander" 2>&1); pm_rc=$?
  pm_secs=$(( $(date +%s) - s )); pm_sha=$(git rev-parse HEAD)
}
run_pm_case p1 $'GATE_POST_MERGE=local\n'; o1=$pm_out; r1=$pm_rc; s1=$pm_secs; h1=$pm_sha
run_pm_case p3 $'GATE_POST_MERGE=ci\n'; o3=$pm_out
run_pm_case p4 ''; o4=$pm_out
run_pm_case p5 $'GATE_POST_MERGE=yes\n'; o5=$pm_out
run_pm_case p6r $'GATE_POST_MERGE=local\n'
run_pm_case p6 ''; o6=$pm_out                       # R declares local, the landed commit deletes it
GATE_POST_MERGE=local run_pm_case p6e ''; o6e=$pm_out  # the environment says local, the tip says nothing
git rm -q "$pmk/post-merge.sh"
run_pm_case p7 $'GATE_POST_MERGE=local\n'; o7=$pm_out; r7=$pm_rc; h7=$pm_sha
t7=$(git ls-remote "$tmp/remote6.git" refs/heads/main | cut -f1)   # now: pm8 lands on this remote before the reads
git checkout -q HEAD~1 -- "$pmk/post-merge.sh"
git add -A; git commit -q -m "stub back"; git push -q --no-verify origin main
git worktree add -q "$tmp/wt6" -b feat6 main
export MARK="$tmp/pm-mark-p8"
o8=$(cd "$tmp/wt6" && echo u8 > src-u8.txt && git add src-u8.txt && git commit -q -m "TOOL-tB-1: unit" \
  && bash "$lander" --prepare --slug tB >/dev/null 2>&1 && bash "$lander" --land --slug tB 2>&1)
h8=$(git -C "$tmp/wt6" rev-parse HEAD)
sleep 12
read_pm_mark() { [ -f "$tmp/pm-mark-$1" ] && cat "$tmp/pm-mark-$1" || echo absent; }
# AC1 — local: the capture returns before the 8 s child finishes, and the child ran on the landed tip
[ "$r1" = 0 ] && [ "$s1" -lt 8 ] && [ "$(read_pm_mark p1)" = "$h1 --remote origin" ] \
  && ok "pm1 GATE_POST_MERGE=local starts the post-merge bar on the landed tip, detached (${s1}s capture)" \
  || bad "pm1 rc=$r1 secs=$s1 marker='$(read_pm_mark p1)' tip=$h1 $o1"
# AC2 — the stderr line and the start record in the common dir
rec=$(cat "$gcd6/gate-post-merge.start" 2>/dev/null)
rlog=$(printf '%s\n' "$rec" | awk -F'\t' '$1=="log"{print $2}')
[ "$(printf '%s\n' "$o1" | grep -c "post-merge bar started on ${h1:0:8} — pid")" = 1 ] \
  && printf '%s\n' "$rec" | grep -q "^pid	[0-9]" && printf '%s\n' "$rec" | grep -q "^by	push-main$" \
  && [ -n "$rlog" ] && [ -f "$rlog" ] \
  && ok "pm2 the start is one stderr line and a sha/pid/log/by record" || bad "pm2 record='$rec' $o1"
# (the record now names the in-place landing's sha, the last start; check AC2's sha on p8 below)
# AC3, AC4, AC5 — ci says so, undeclared is silent, a value outside the set is named; none starts
[ "$(printf '%s\n' "$o3" | grep -c 'remote CI runs it')" = 1 ] && [ "$(read_pm_mark p3)" = absent ] \
  && ok "pm3 ci prints one line and starts nothing" || bad "pm3 marker='$(read_pm_mark p3)' $o3"
[ "$(printf '%s\n' "$o4" | grep -c 'post-merge')" = 0 ] && [ "$(read_pm_mark p4)" = absent ] \
  && ok "pm4 undeclared prints nothing and starts nothing" || bad "pm4 marker='$(read_pm_mark p4)' $o4"
case "$o5" in *"is 'yes', outside 'local ci'"*) l5=1 ;; *) l5=0 ;; esac
[ "$l5" = 1 ] && [ "$(read_pm_mark p5)" = absent ] \
  && ok "pm5 a value outside 'local ci' is named and starts nothing" || bad "pm5 marker='$(read_pm_mark p5)' $o5"
# AC6 — read at the landed tip only: not R, not the environment
[ "$(printf '%s\n%s\n' "$o6" "$o6e" | grep -c 'post-merge')" = 0 ] && [ "$(read_pm_mark p6)$(read_pm_mark p6e)" = absentabsent ] \
  && ok "pm6 the declaration is read at the landed tip, never from R or the environment" \
  || bad "pm6 markers='$(read_pm_mark p6)' '$(read_pm_mark p6e)' $o6 $o6e"
# AC7 — no kit: a line, exit 0, the landing stands
[ "$r7" = 0 ] && case "$o7" in *"no run-gates kit holding post-merge.sh"*) true ;; *) false ;; esac \
  && [ "$t7" = "$h7" ] \
  && ok "pm7 a missing post-merge script is one line and exit 0; the landing stands" || bad "pm7 rc=$r7 $o7"
# AC8 — the in-place path starts it too, on the prepared merge
[ "$(read_pm_mark p8)" = "$h8 --remote origin" ] && grep -q "^sha	$h8$" "$gcd6/gate-post-merge.start" \
  && ok "pm8 --land starts the post-merge bar on the prepared merge" || bad "pm8 marker='$(read_pm_mark p8)' tip=$h8 $o8"
cd "$SRC" || exit 2
# AC9 — the copied parser is byte-identical to the hook's; a one-byte break in a scratch copy shows
read_parser_slice() { awk '/^read_policy_key\(\)/,/^}/' "$1"; }
sed 's/ hit=1 ;;/ hit=2 ;;/' "$HERE/push-main.sh" > "$tmp/pm-copy.sh"
d9=$(diff <(read_parser_slice "$HERE/push-main.sh") <(read_parser_slice "$SRC/.githooks/pre-push")); d9b=$(diff <(read_parser_slice "$tmp/pm-copy.sh") <(read_parser_slice "$SRC/.githooks/pre-push"))
[ -z "$d9" ] && [ -n "$(read_parser_slice "$HERE/push-main.sh")" ] && [ -n "$d9b" ] \
  && ok "pm9 read_policy_key is byte-identical to the pre-push hook's, and a staged break shows" \
  || bad "pm9 parity diff: $d9 | break diff empty: $([ -z "$d9b" ] && echo yes || echo no)"
# 26 — TOOL-aRoutedQuill-3 AC11: the ATTENDED landing's mint commit names the newest unit the pushed
#      range attributes, `mint: kit versions onto origin/main at <sha8> for <unit>`, and carries a
#      `Pass: none` trailer, because it touches version carriers under ROUTED_PATHS and the pre-push
#      routed-commits leg reds a routed commit naming no unit. A clone of this repository at its
#      committed HEAD is the remote; one commit naming a unit moves the runlog kit, and the lander
#      runs from main. Observed RED against the base lander, whose mint subject named no unit.
#      THE FIXTURE DEFINES ITS UNIT (TOOL-aPrimedIndex-8): the newest-unit reader names only an id a spec
#      at HEAD defines (TOOL-aRoutedQuill-12), so without one the mint named nothing and this arm redded
#      against every lander. The spec lands in the clone's first build folder that holds one, because
#      the index generator refuses a build folder with no README.
write_unit_spec() { # unit id -> a one-line spec defining it, committed into the fixture's first spec folder
  local mr d
  mr=$(sed -n 's/^MEMORY_ROOT=//p' .memory-tree.conf 2>/dev/null | tr -d "\"'" | tail -n 1)
  for d in "${mr:-memory}"/builds/*/spec; do [ -d "$d" ] && break; done
  [ -d "$d" ] || return 1
  printf '# %s — a fixture unit\n' "$1" > "$d/2026-01-01-spec-$1.md"
  git add "$d/2026-01-01-spec-$1.md" && git commit -q --no-verify -m "a fixture spec defining $1"
}
_mt_rc=$(cd "$HERE" && for d in */; do [ -f "$d/routed_commits.py" ] && { printf '%s' "${d%/}"; break; }; done)
if [ -n "$_mt_gk" ] && [ -n "$_mt_rl" ] && [ -n "$_mt_rc" ]; then
  git clone -q --bare "$SRC" "$tmp/remote26.git"
  git clone -q "$tmp/remote26.git" "$tmp/work26"
  out26=$(
    cd "$tmp/work26" || exit 1
    git config core.hooksPath "$tmp/allow-hook"   # a clone wires no hook; the lander wants its allow record
    git checkout -q -B main "$(git -C "$SRC" rev-parse HEAD)"
    git push -q -f --no-verify origin main
    git -C "$tmp/remote26.git" symbolic-ref HEAD refs/heads/main
    R6=$(git rev-parse HEAD)
    write_unit_spec TOOL-tFix-26 || exit 1
    printf '# a comment line, push-main.test case 26\n' >> "${KIT_REL}$_mt_rl/extract.py"
    # The unit's SPEC is write_unit_spec's, above (TOOL-dHomedResolver-8 found the same need): a new
    # README-less build folder for it would make the lander's index regeneration refuse the landing.
    git add -A
    git commit -q --no-verify -m "TOOL-tFix-26: move runlog"
    unset GATE_PUSH_BASE; bash "$lander" >/dev/null 2>&1 || echo "rc=$?"
    printf 'tip=%s\n' "$(git rev-parse origin/main)"
    printf 'head=%s\n' "$(git rev-parse HEAD)"
    # The mint commit is FOUND BY ITS SUBJECT, not read as the newest: the regeneration
    # TOOL-aPrimedIndex-4 adds commits after it whenever a generated output moved.
    m26=$(git log -1 --format=%H --grep='^mint: kit versions onto' HEAD)
    printf 'subject=%s\n' "$(git log -1 --format=%s "${m26:-HEAD}")"
    printf 'pass=%s\n' "$(git log -1 --format='%(trailers:key=Pass,valueonly)' "${m26:-HEAD}" | tr -d '\n')"
    printf 'want=mint: kit versions onto origin/main at %s for TOOL-tFix-26\n' "${R6:0:8}"
  )
  _w26=$(printf '%s\n' "$out26" | sed -n 's/^want=//p')
  case "$out26" in *rc=*) l26=0 ;; *) l26=1 ;; esac
  [ "$l26" = 1 ] && printf '%s\n' "$out26" | grep -qxF "subject=$_w26" && printf '%s\n' "$out26" | grep -qx 'pass=none' \
    && [ "$(printf '%s\n' "$out26" | sed -n 's/^tip=//p')" = "$(printf '%s\n' "$out26" | sed -n 's/^head=//p')" ] \
    && ok "26 the attended mint commit names the range's newest unit and carries Pass: none, and it lands" \
    || bad "26 the attended mint subject or trailer is wrong, or the landing failed: $out26"
else
  echo "  skip — 26 no govkit deployer, runlog kit or memory-tree kit beside this lander, so the mint-subject arm did not run"
fi

# 27 — TOOL-aRoutedQuill-12 AC16: a `--newest-unit` that REFUSES names no unit. Its refusal prints on
# stdout and exits 2, so a helper piping it into `head` minted the refusal text as the unit id. The
# helper runs cut from the lander, its python and kit resolvers stubbed to a shell stub.
out27=$(
  eval "$(sed -n '/^read_mint_unit() {/,/^}/p' "$lander")"
  resolve_python() { echo bash; }
  resolve_kit_dir() { echo k; }
  top="$tmp/mint27"; self_dir="$top"; mkdir -p "$top/k"
  printf 'echo "routed-commits REFUSED — x"; exit 2\n' > "$top/k/routed_commits.py"
  printf 'refused=[%s]\n' "$(read_mint_unit HEAD~1..HEAD)"
  printf 'echo TOOL-x-1; exit 0\n' > "$top/k/routed_commits.py"
  printf 'named=[%s]\n' "$(read_mint_unit HEAD~1..HEAD)"
)
printf '%s\n' "$out27" | grep -qx 'refused=\[\]' && printf '%s\n' "$out27" | grep -qx 'named=\[TOOL-x-1\]' \
  && ok "27 a refusing --newest-unit mints no unit, and an answering one mints its id" \
  || bad "27 read_mint_unit kept a refusal or lost an answer: $out27"

# 28-32 — TOOL-aPrimedIndex-4 and -8: the lander REGENERATES the declared generated outputs over the tree it
#      is about to push. Each arm is a clone of this repository at its committed HEAD, pushed to a bare
#      remote as main, whose memory root's bug-class index loses one row in a commit; the stale row is
#      what a reconcile merge leaves behind when the index resolves `merge=ours`. The memory root is
#      read from the clone's conf. Needs the run-gates kit's regen.py beside the lander; an install
#      without one says so. Observed RED against the base lander, which pushed the stale row.
_rg_k=$(cd "$HERE" && for d in */; do [ -f "$d/regen.py" ] && { printf '%s' "${d%/}"; break; }; done)
build_regen_fixture() { # remote dir · work dir -> a clone at SRC's HEAD on main, pushed, with origin/HEAD at main
  git clone -q --bare "$SRC" "$1"
  git clone -q "$1" "$2"
  cd "$2" || return 1
  git config user.email t@e; git config user.name t; git config core.autocrlf false
  git config core.hooksPath "$tmp/allow-hook"   # a clone wires no hook; the lander wants its allow record
  git checkout -q -B main "$(git -C "$SRC" rev-parse HEAD)"
  git push -q -f --no-verify origin main
  git -C "$1" symbolic-ref HEAD refs/heads/main
  git remote set-head origin main >/dev/null 2>&1
  _mr=$(sed -n 's/^MEMORY_ROOT=//p' .memory-tree.conf 2>/dev/null | tr -d "\"'" | tail -n 1)
  _gi="${_mr:-memory}/gotchas/INDEX.md"
}
write_stale_index() { # -> one table row of the bug-class index removed and committed, naming a unit
  local n
  n=$(grep -n '^| \[' "$_gi" | sed -n 3p | cut -d: -f1)
  [ -n "$n" ] || return 1
  sed -i "${n}d" "$_gi"
  git commit -q --no-verify -am "TOOL-tFix-$1: a stale bug-class index"
}
if [ -n "$_rg_k" ]; then
  # 28 (AC1) — --prepare folds the regenerated index into the prepared merge, and the tree is clean.
  out28=$(
    build_regen_fixture "$tmp/remote8.git" "$tmp/work8" || exit 1
    R8=$(git rev-parse HEAD)
    git checkout -q -b feat
    write_stale_index 28 || exit 1
    unset GATE_PUSH_BASE; bash "$lander" --prepare --slug tRegen >/dev/null 2>&1 || echo "rc=$?"
    [ "$(git rev-parse HEAD^1)" = "$R8" ] && echo parent=ok
    git diff --quiet "$R8" HEAD -- "$_gi" && echo index=restored
    [ -z "$(git status --porcelain)" ] && echo tree=clean
  )
  case "$out28" in
    *rc=*) bad "28 --prepare refused over a stale bug-class index: $out28" ;;
    *parent=ok*index=restored*tree=clean*) ok "28 --prepare regenerates the stale bug-class index into the prepared merge and leaves a clean tree" ;;
    *) bad "28 the prepared merge carries the stale bug-class index, or the tree was left dirty: $out28" ;;
  esac

  # 29 (AC2) — the attended landing commits the regeneration as `regen: …` with `Pass: none`, and lands it.
  out29=$(
    build_regen_fixture "$tmp/remote9.git" "$tmp/work9" || exit 1
    R9=$(git rev-parse HEAD)
    write_unit_spec TOOL-tFix-29 || exit 1
    write_stale_index 29 || exit 1
    unset GATE_PUSH_BASE; bash "$lander" >/dev/null 2>&1 || echo "rc=$?"
    printf 'subject=%s\n' "$(git log -1 --format=%s)"
    printf 'pass=%s\n' "$(git log -1 --format='%(trailers:key=Pass,valueonly)' | tr -d '\n')"
    printf 'want=regen: generated outputs onto origin/main at %s for TOOL-tFix-29\n' "${R9:0:8}"
    [ "$(git rev-parse origin/main)" = "$(git rev-parse HEAD)" ] && echo landed=1
    git diff --quiet "$R9" origin/main -- "$_gi" && echo index=restored
  )
  _w29=$(printf '%s\n' "$out29" | sed -n 's/^want=//p')
  case "$out29" in *rc=*) l29=0 ;; *) l29=1 ;; esac
  [ "$l29" = 1 ] && [ -n "$_w29" ] && printf '%s\n' "$out29" | grep -qxF "subject=$_w29" \
    && printf '%s\n' "$out29" | grep -qx 'pass=none' && printf '%s\n' "$out29" | grep -qx 'landed=1' \
    && printf '%s\n' "$out29" | grep -qx 'index=restored' \
    && ok "29 the attended landing commits the regeneration as its own regen: commit with Pass: none, and lands it" \
    || bad "29 the attended regen commit is missing, misnamed or untrailered, or the landing failed: $out29"

  # 30 (AC3) — a regen.py that exits 1 refuses --prepare and leaves the branch where it was. It writes
  #      an untracked file first, as a new ledger shard or a render's temporary would, and the refused
  #      landing leaves the tree clean (TOOL-aPrimedIndex-8).
  out30=$(
    build_regen_fixture "$tmp/remote10.git" "$tmp/work10" || exit 1
    git checkout -q -b feat
    printf 'import pathlib, sys\npathlib.Path("regen-litter.txt").write_text("x", encoding="utf-8")\nsys.exit(1)\n' > "${KIT_REL}$_rg_k/regen.py"
    git commit -q --no-verify -am "TOOL-tFix-30: a failing regeneration"
    B30=$(git rev-parse HEAD)
    unset GATE_PUSH_BASE; bash "$lander" --prepare --slug tRegenFail 2>&1 >/dev/null; echo "rc=$?"
    printf 'branch=%s\n' "$(git rev-parse --abbrev-ref HEAD)"
    [ "$(git rev-parse feat)" = "$B30" ] && echo unmoved=1
    [ -z "$(git status --porcelain)" ] && echo clean=1
  )
  case "$out30" in
    *"could NOT be regenerated"*"rc=1"*"branch=feat"*"unmoved=1"*"clean=1"*) ok "30 a failing regeneration refuses --prepare, leaves the branch unmoved and checked out, and cleans what it created" ;;
    *) bad "30 a failing regeneration was not refused with the branch left where it was: $out30" ;;
  esac

  # 31 (AC4) — no regen.py beside the lander: one line says so, and --prepare still prepares. The
  #      removal is on the remote's tip as well as the branch, because a branch that deleted it alone
  #      would publish a merge losing its definitions, which the merge-loss check refuses first.
  out31=$(
    build_regen_fixture "$tmp/remote11.git" "$tmp/work11" || exit 1
    git rm -q -- "${KIT_REL}$_rg_k/regen.py"
    git commit -q --no-verify -m "TOOL-tFix-31: no regeneration"
    git push -q --no-verify origin main
    R11=$(git rev-parse HEAD)
    git checkout -q -b feat
    git commit -q --no-verify --allow-empty -m "TOOL-tFix-31: a unit"
    unset GATE_PUSH_BASE; bash "$lander" --prepare --slug tRegenAbsent 2>&1; echo "rc=$?"
    [ "$(git rev-parse HEAD^1)" = "$R11" ] && echo parent=ok
  )
  case "$out31" in
    *"no regen.py beside this lander"*"rc=0"*"parent=ok"*) ok "31 a lander with no regen.py beside it says so in one line and still prepares" ;;
    *) bad "31 a missing regen.py was silent, or refused the landing: $out31" ;;
  esac
  # 32 (AC3, the attended path) — a regen.py that exits 1 refuses the attended landing with its own
  #      line, and the remote's main does not move.
  out32=$(
    build_regen_fixture "$tmp/remote12.git" "$tmp/work12" || exit 1
    R12=$(git rev-parse HEAD)
    printf 'import sys\nsys.exit(1)\n' > "${KIT_REL}$_rg_k/regen.py"
    git commit -q --no-verify -am "TOOL-tFix-32: a failing regeneration"
    unset GATE_PUSH_BASE; bash "$lander" 2>&1; echo "rc=$?"
    [ "$(git ls-remote origin refs/heads/main | cut -f1)" = "$R12" ] && echo unpushed=1
  )
  case "$out32" in
    *"push-main: the generated outputs this landing owes could not be regenerated (named above). Aborted (no push)."*"rc=1"*"unpushed=1"*)
      ok "32 a failing regeneration refuses the attended landing with its own line, and nothing is pushed" ;;
    *) bad "32 a failing regeneration did not refuse the attended landing, or something was pushed: $out32" ;;
  esac

  # 33 (TOOL-dGroundRules-25 S2-S4) — a policy-file change on `feat`, landed through the real
  #      --prepare, which stales the mirror (it records the policy file's blob): the prepared merge's
  #      own checks, the installed regen.py --check and the policy kit's mirror --check, must each
  #      exit 0 at the prepared HEAD. The lander is asserted to have prepared FIRST, by its exit, its
  #      `push-main: prepared` line and a second parent: a refused --prepare is graded by its exit
  #      status, never by checks over the unmerged branch. Needs the policy kit beside the lander; an
  #      install without one says so, as 28-32 do without regen.py.
  _pk_k=$(cd "$HERE" && for d in */; do [ -f "$d/policy.py" ] && [ -f "$d/catalogue.toml" ] && { printf '%s' "${d%/}"; break; }; done)
  if [ -z "$_pk_k" ]; then
    echo "  skip — 33 no policy kit beside this lander, so the policy-landing arm did not run"
  elif ! _py33=$(resolve_python); then
    bad "33 no python launcher runs, so the prepared merge's checks cannot be read"
  else
    out33=$(
      build_regen_fixture "$tmp/remote13.git" "$tmp/work13" || exit 1
      git checkout -q -b feat
      printf '# a policy change landed through --prepare (TOOL-dGroundRules-25 S2)\n' >> .governance/policy.toml
      git commit -q --no-verify -am "TOOL-tFix-33: a policy change"
      unset GATE_PUSH_BASE; o33=$(bash "$lander" --prepare --slug tPolicy 2>&1); rc33=$?
      printf '%s\n' "$o33"; echo "prepare-rc=$rc33"
      [ "$rc33" = 0 ] || exit 0
      git rev-parse -q --verify 'HEAD^2' >/dev/null && echo merge=1
      "$_py33" "${KIT_REL}$_rg_k/regen.py" --check >/dev/null 2>&1; echo "regen-rc=$?"
      "$_py33" "${KIT_REL}$_pk_k/policy.py" mirror --check >/dev/null 2>&1; echo "mirror-rc=$?"
    )
    _rc33=$(printf '%s\n' "$out33" | sed -n 's/^prepare-rc=//p')
    if [ "$_rc33" != 0 ]; then
      bad "33 --prepare over a policy-file change exited ${_rc33:-(it never ran)}, so neither check was read: $out33"
    elif [[ $'\n'$out33 != *$'\n''push-main: prepared '* || $'\n'$out33$'\n' != *$'\n'merge=1$'\n'* ]]; then
      bad "33 --prepare exited 0 without printing push-main: prepared and leaving a second parent: $out33"
    elif [[ $'\n'$out33$'\n' == *$'\n'regen-rc=0$'\n'* && $'\n'$out33$'\n' == *$'\n'mirror-rc=0$'\n'* ]]; then
      ok "33 a policy-file change landed through --prepare carries generated outputs regen.py --check and mirror --check both call fresh"
    else
      bad "33 the prepared merge carries a generated output its own checks call stale: $(printf '%s\n' "$out33" | grep -E '^(regen|mirror)-rc=' | tr '\n' ' ')"
    fi
  fi
else
  echo "  skip — 28-32 no run-gates kit holding regen.py beside this lander, so the regeneration arms did not run"
fi

# 34 — TOOL-dSafePassage-8 AC5: --prepare walks every declared upgrade step on gov's own tree first,
#      into the prepared merge. A clone of this repository at its committed HEAD, pushed to a bare
#      remote as main: a branch with one unit commit prepares a merge whose tree holds gov's
#      source-mode receipt, every declared step applied; a branch whose steps file carries a planted
#      row with a failing witness is refused naming it, the branch unmoved. Needs gov's deployer
#      beside the lander; an install without one says so. Staged red by dropping the call to
#      `run_gov_first` from cmd_prepare.
if [ -n "$_mt_gk" ] && _py34=$(resolve_python 2>/dev/null); then
  out34=$(
    build_regen_fixture "$tmp/remote14.git" "$tmp/work14" || exit 1
    git checkout -q -b feat
    git commit -q --no-verify --allow-empty -m "TOOL-tFix-34: a unit"
    unset GATE_PUSH_BASE; bash "$lander" --prepare --slug tGovFirst >/dev/null 2>&1; echo "clean-rc=$?"
    git show HEAD:.governance/install.json > "$tmp/gf34.json" 2>/dev/null && "$_py34" - "${KIT_REL}$_mt_gk" "$tmp/gf34.json" <<'PY' && echo applied=all
import json, pathlib, sys
sys.path.insert(0, sys.argv[1])
import upgrade_steps as u
r = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
want = {x.id for x in u.read_steps(".", "HEAD", None)}
got = {x["id"] for x in r.get("steps") or [] if x.get("state") == "applied"}
sys.exit(0 if r.get("mode") == "source" and want and got == want and len(r["steps"]) == len(want) else 1)
PY
    git checkout -q -b plant main
    printf '\n[[upgrade]]\nid = "govkit/planted-witness-fails"\nup = ["python", "-c", "pass"]\ndown = ["python", "-c", "pass"]\nwitness = ["python", "-c", "raise SystemExit(1)"]\nsurfaces = []\nneeds-target = false\n' >> "${KIT_REL}$_mt_gk/steps.toml"
    git commit -q --no-verify -am "TOOL-tFix-34: a planted step whose witness never holds"
    B34=$(git rev-parse HEAD)
    bash "$lander" --prepare --slug tGovFirstPlant 2>&1 >/dev/null; echo "plant-rc=$?"
    [ "$(git rev-parse refs/heads/plant)" = "$B34" ] && echo unmoved=1
    # TOOL-dSafePassage-25 AC1/AC2: the refusal leaves nothing the walk made, and the retry without
    # the plant prepares a merge whose .governance (receipt, steps, outbox) is the clean run's.
    st34=$(git status --porcelain); [ -z "$st34" ] && echo plant-clean=1 || echo "plant-left=[$st34]"
    git checkout -q main -- "${KIT_REL}$_mt_gk/steps.toml"
    git commit -q --no-verify -m "TOOL-tFix-34: the planted step removed"
    bash "$lander" --prepare --slug tGovFirstRetry >/dev/null 2>&1; echo "retry-rc=$?"
    gf34a=$(git ls-tree -r --name-only HEAD -- .governance)
    gf34b=$(git ls-tree -r --name-only refs/heads/feat -- .governance)
    [ "$gf34a" = "$gf34b" ] && echo retry-merge=clean || echo "retry-merge=[$gf34a] clean-run=[$gf34b]"
  )
  case "$out34" in
    *"clean-rc=0"*"applied=all"*"govkit/planted-witness-fails"*"plant-rc=1"*"unmoved=1"*"plant-clean=1"*"retry-rc=0"*"retry-merge=clean"*)
      ok "34 --prepare walks every declared step on gov first into the prepared merge, and refuses a step whose witness never holds, the branch unmoved and no file of the walk left behind, so the retry's merge holds none" ;;
    *) bad "34 the prepared merge lacks gov's receipt of every applied step, or a failing step was not refused with the branch unmoved and the tree clean, or the retry folded the refused walk's leftovers: $out34" ;;
  esac
  # 36 — TOOL-dSafePassage-27 AC1/AC2: the walk passes and a committed regen.py exits 1. The
  #      regeneration's refusal cleans against the snapshot taken BEFORE the walk, so the tree is
  #      clean after it, and the retry with the regen.py reverted prepares (exit 0) a merge holding no
  #      leftover of the refused run. Staged red by a lander copy whose regeneration refusal cleans
  #      against a snapshot taken after the walk. Needs regen.py beside the lander too.
  if [ -n "$_rg_k" ]; then
    out36=$(
      build_regen_fixture "$tmp/remote16.git" "$tmp/work16" || exit 1
      git checkout -q -b feat
      printf 'import sys\nsys.exit(1)\n' > "${KIT_REL}$_rg_k/regen.py"
      git commit -q --no-verify -am "TOOL-tFix-36: a failing regeneration"
      B36=$(git rev-parse HEAD)
      unset GATE_PUSH_BASE; bash "$lander" --prepare --slug tRegenAfterWalk 2>&1 >/dev/null; echo "fail-rc=$?"
      [ "$(git rev-parse refs/heads/feat)" = "$B36" ] && echo unmoved=1
      st36=$(git status --porcelain); [ -z "$st36" ] && echo fail-clean=1 || echo "fail-left=[$st36]"
      git checkout -q main -- "${KIT_REL}$_rg_k/regen.py"
      git commit -q --no-verify -m "TOOL-tFix-36: the failing regeneration reverted"
      bash "$lander" --prepare --slug tRegenAfterWalkRetry >/dev/null 2>&1; echo "retry-rc=$?"
      git rev-parse -q --verify 'HEAD^2' >/dev/null && echo merge=1
      printf 'steps-outbox=[%s]\n' "$(git ls-tree -r --name-only HEAD -- .governance/steps .governance/outbox | tr '\n' ' ')"
    )
    case "$out36" in
      *"could NOT be regenerated"*"fail-rc=1"*"unmoved=1"*"fail-clean=1"*"retry-rc=0"*"merge=1"*)
        ok "36 a regeneration refused after a passing gov-first walk leaves no file of the walk behind, and the retry prepares a clean merge" ;;
      *) bad "36 a refused regeneration after a passing walk left the walk's files untracked, or the retry folded or refused on them: $out36" ;;
    esac
  else
    echo "  skip — 36 no run-gates kit holding regen.py beside this lander, so the walk-then-regeneration arm did not run"
  fi
else
  echo "  skip — 34 and 36 no govkit deployer beside this lander or no python launcher, so the gov-first arms did not run"
fi

# 35 — TOOL-dSafePassage-8 AC6: `run_gov_first` cut from the lander. No deployer beside it, with or
#      without a python, is one `steps were NOT run on gov first` line and exit 0; a deployer beside it
#      with the resolver refusing is exit 1, because no later gate runs a step on gov. Staged red by
#      making the no-python branch return 0 whatever is beside the lander.
out35=$(
  eval "$(sed -n '/^run_gov_first() {/,/^}/p' "$lander")"
  top="$tmp/gf35"; self_dir="$top/kits"; mkdir -p "$self_dir"
  resolve_python() { return 1; }
  printf 'nopy-absent=[%s]\n' "$(run_gov_first 2>&1; echo "rc=$?")"
  resolve_python() { echo bash; }
  resolve_kit_dir() { return 1; }
  printf 'py-absent=[%s]\n' "$(run_gov_first 2>&1; echo "rc=$?")"
  mkdir -p "$self_dir/govkit"; : > "$self_dir/govkit/govkit.py"
  resolve_python() { return 1; }
  printf 'nopy-present=[%s]\n' "$(run_gov_first 2>&1; echo "rc=$?")"
)
n35=$(printf '%s\n' "$out35" | grep -c 'steps were NOT run on gov first — no govkit deployer beside this lander')
case "$out35" in
  *"nopy-absent=["*"rc=0]"*"py-absent=["*"rc=0]"*"nopy-present=["*"no usable python launcher"*"rc=1]"*)
    [ "$n35" = 2 ] && ok "35 no deployer beside the lander is one skip line and exit 0; a deployer with no python refuses" \
      || bad "35 the skip line was printed $n35 time(s) over two absent-deployer runs: $out35" ;;
  *) bad "35 run_gov_first skipped a deployer it could not run, or refused an adopter's landing: $out35" ;;
esac

[ "$fail" = 0 ] && { echo "push-main.test: all cases ok"; exit 0; } || { echo "push-main.test: FAILURES"; exit 1; }
