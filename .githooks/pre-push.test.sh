#!/usr/bin/env bash
# pre-push.test.sh — drives a REAL git push through .githooks/pre-push in a throwaway scratch repo,
# with the gate stubbed via GOV_GATE_CMD so the bar never actually runs. Proves the hook FIRES and
# classifies correctly. Exit 0 = all cases ok.
set -u
SRC=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "pre-push.test: not a git repo"; exit 2; }
# The kit root is the one the hook itself reads: GOV_KITROOT as `.githooks/gate-env.sh` declares it
# (TOOL-aRepatriatedFork-28), never a literal prefix typed here.
KIT_REL=$( . "$SRC/.githooks/gate-env.sh" >/dev/null 2>&1; printf '%s' "${GOV_KITROOT:-}" )
[ -n "$KIT_REL" ] || { echo "pre-push.test: .githooks/gate-env.sh declares no GOV_KITROOT"; exit 2; }
[ -f "$SRC/.githooks/pre-push" ] || { echo "pre-push.test: .githooks/pre-push missing"; exit 1; }
# TOOL-aRepatriatedFork-46: the run-gates kit is named by the NAME its directory has under that kit
# root, found through the resolver, which reads the install receipt first, never typed.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  "$1" -c "$(cat <<'RKD'
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
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
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
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
)"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
_rkd_py=$(resolve_python) || { echo "pre-push.test: no usable python, so the run-gates kit cannot be resolved"; exit 2; }
RUN_GATES_DIR=$(resolve_kit_dir "$_rkd_py" run-gates run-gates.sh "$SRC/$KIT_REL") || exit 2
RUN_GATES="${RUN_GATES_DIR##*/}"

tmp=$(mktemp -d) || exit 2
trap 'rm -rf "$tmp"' EXIT
fail=0
ok() { echo "  ok   — $1"; }
bad() { echo "  FAIL — $1"; fail=1; }
# The scratch repo is `git init`+`remote add` (origin/HEAD unset); pin the default so the hook's
# fail-CLOSED resolution doesn't refuse the gate cases (case 6 unsets it to test that path).
export GOV_DEFAULT_BRANCH=main
# THE DECLARED TEST ESCAPE (TOOL-aRepatriatedFork-5, from adopter nc's PKG-dCandidLodestar-5). Every
# stub below is an mktemp script, which is untracked by construction, and the hook refuses an
# untracked merge bar. Without this the whole file would test a refusal path and nothing else.
# Cases 25-27 unset it deliberately.
export GOV_GATE_CMD_TEST=1

# Isolate ONLY the pre-push hook (a scratch hooks dir) so the repo's pre-commit branch-guard does not
# fire on the test's own setup commits. A clone does NOT carry core.hooksPath — set it explicitly.
mkdir -p "$tmp/hooks"
cp "$SRC/.githooks/pre-push" "$tmp/hooks/pre-push"

git init -q --bare "$tmp/remote.git"
git init -q "$tmp/work"
cd "$tmp/work" || exit 2
git config user.email t@example.com; git config user.name t
git config core.hooksPath "$tmp/hooks"
git commit -q --allow-empty -m init
git branch -M main
git remote add origin "$tmp/remote.git"

# case 0 — a raw default-branch push with NO push-main marker is refused (TOOL-aLeasedGauntlet-1).
git commit -q --allow-empty -m c0
if git push -q origin main >/dev/null 2>&1; then bad "0 raw push (no marker) must be refused"; else ok "0 raw push (no marker) refused"; fi
# The remaining cases exercise the GATE — set the marker push-main would set (the hook only CHECKS it).
touch "$(git rev-parse --git-dir)/push-main-active"

red="$tmp/red.sh";   printf '#!/usr/bin/env bash\necho "FAKE LEG failed"; exit 1\n' > "$red"
green="$tmp/green.sh"; printf '#!/usr/bin/env bash\nexit 0\n' > "$green"

# case 1 — push to main with a RED gate → blocked (non-zero push).
if GOV_GATE_CMD="bash $red" git push -q origin main >/dev/null 2>&1; then bad "1 red gate must block a main push"; else ok "1 red gate blocks a main push"; fi
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${probe_n:-1} assertions)" || echo "FAIL (${probe_n:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi

# case 2 — push to main with a GREEN gate → proceeds (the gate actually ran).
if GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1; then ok "2 green gate lets a main push through"; else bad "2 green gate must let a main push through"; fi

# case 3 — push a NON-main ref → hook skips the gate, so even a RED stub proceeds.
git checkout -q -b feature
git commit -q --allow-empty -m f
if GOV_GATE_CMD="bash $red" git push -q origin feature >/dev/null 2>&1; then ok "3 non-main ref skips the gate"; else bad "3 non-main ref must skip the gate"; fi

# case 4 — push a DIFFERENTLY-NAMED local ref to main (feature:refs/heads/main) with RED → blocked.
#          Proves classification is on the remote_ref (3rd field), not the local ref name.
if GOV_GATE_CMD="bash $red" git push -q origin feature:refs/heads/main >/dev/null 2>&1; then bad "4 renamed local ref to main must be gated"; else ok "4 renamed local ref to main is gated (3rd-field classify)"; fi

# case 5 — multi-ref push including main (a new main commit + feature) with RED → blocked.
git checkout -q main
git commit -q --allow-empty -m m2
if GOV_GATE_CMD="bash $red" git push -q origin main feature >/dev/null 2>&1; then bad "5 multi-ref push incl. main must be gated"; else ok "5 multi-ref push incl. main is gated"; fi

# case 6 — fail CLOSED when the default branch is unresolvable (origin/HEAD unset AND GOV_DEFAULT_BRANCH
#          unset): the hook must REFUSE, not silently assume 'main' and BYPASS the gate on a non-main default.
git checkout -q main
msg=$( ( unset GOV_DEFAULT_BRANCH; GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 1>/dev/null ) )
case "$msg" in
  *"determine the default branch"*) ok "6 unresolvable default branch → fail closed" ;;
  *) bad "6 expected fail-closed refusal, got: ${msg:-<push SUCCEEDED>}" ;;
esac

# case 7 — a NON-EMPTY but meaningless GOV_DEFAULT_BRANCH must be refused, not classified against.
#          Reproduced as a live, repo-wide bypass on 2026-08-11: the loop never matched, main_local
#          stayed empty, and the hook exited 0 down the "nothing to gate" path — skipping the lander
#          refusal AND the full bar. Case 6 covers an EMPTY value; this is the worse, non-empty one.
git checkout -q main
git commit -q --allow-empty -m c7
msg=$( ( GOV_DEFAULT_BRANCH=nosuchthing GOV_GATE_CMD="bash $red" git push -q origin main 2>&1 1>/dev/null ) )
case "$msg" in
  *"no branch in this clone"*) ok "7 non-empty but unresolvable default branch → refused" ;;
  *) bad "7 expected a refusal, got: ${msg:-<push SUCCEEDED — the whole bar was skipped>}" ;;
esac
# case 7c — the LIVE CONTROL for 7, one variable changed: the honest value on the same tree must reach
#           the gate and be blocked BY THE GATE, not by the classification refusal. Without this, case
#           7 would also pass against a hook that refuses everything.
# NOTE: both streams here. The hook's gate-RED line goes to STDOUT while its refusals go to stderr,
# so the stderr-only capture used above would have discarded exactly the evidence this control needs.
msg=$( ( GOV_DEFAULT_BRANCH=main GOV_GATE_CMD="bash $red" git push -q origin main 2>&1 ) )
case "$msg" in
  *"gate RED"*) ok "7c control — the honest value classifies, and the gate runs" ;;
  *) bad "7c control expected the gate to run, got: ${msg:-<push SUCCEEDED>}" ;;
esac

# case 8 — once a default branch IS observable, the environment may only AGREE with it. This is the
#          shape the real repo is in (refs/remotes/origin/HEAD is set there), and it is why the
#          reproduced bypass is closed rather than merely made harder: `feature` exists, so this is
#          refused for DISAGREEING, not for being unresolvable. Runs last: it sets origin/HEAD.
git remote set-head origin main >/dev/null 2>&1
git commit -q --allow-empty -m c8
msg=$( ( GOV_DEFAULT_BRANCH=feature GOV_GATE_CMD="bash $red" git push -q origin main 2>&1 1>/dev/null ) )
case "$msg" in
  *"does not observe as the default"*) ok "8 env disagreeing with the observed default → refused" ;;
  *) bad "8 expected a refusal, got: ${msg:-<push SUCCEEDED — the whole bar was skipped>}" ;;
esac

# case 9 — THE RED IS ATTRIBUTED AGAINST THE LANDING BASE (TOOL-dDerivedDocket-23 AC7). The runner is
#          handed GATE_ATTRIBUTE = the REMOTE sha git feeds the hook on stdin, never the local one: a
#          red attributed against the tree that has it reads every red as inherited. The hook is
#          driven DIRECTLY with a hand-fed stdin line, because only then are both shas known to the
#          arm, and a fake runner prints its environment and exits 3 so the hook's exit is visible.
git checkout -q main
git commit -q --allow-empty -m c9
_c9r=$(git ls-remote origin refs/heads/main | cut -f1)
_c9l=$(git rev-parse HEAD)
envr="$tmp/envr.sh"
printf '#!/usr/bin/env bash\nprintf "ATTR=%%s\\n" "${GATE_ATTRIBUTE:-}"\nexit %s\n' 3 > "$envr"
msg=$( GATE_ATTRIBUTE= GOV_GATE_CMD="bash $envr" bash "$tmp/hooks/pre-push" origin "$tmp/remote.git" \
       <<<"refs/heads/main $_c9l refs/heads/main $_c9r" 2>&1 ); _c9rc=$?
if [ -z "$_c9r" ] || [ "$_c9r" = "$_c9l" ]; then
  bad "9 precondition — the remote and local shas must both exist and differ, or the arm grades nothing"
else
  case "$msg" in
    *"ATTR=$_c9r"*) ok "9 the runner is handed GATE_ATTRIBUTE = the remote sha fed on stdin" ;;
    *"ATTR=$_c9l"*) bad "9 the hook exported its LOCAL sha, which attributes a red against the tree that has it" ;;
    *) bad "9 GATE_ATTRIBUTE did not reach the runner as the remote sha: ${msg:-<no output>}" ;;
  esac
  [ "$_c9rc" = 3 ] && ok "9 the hook's exit is the runner's (3)" || bad "9 the hook exited $_c9rc where the runner exited 3"
fi
# 9b — THE CONTROL: a remote sha of all zeroes is a branch the remote does not have, and exports nothing.
_c9z=0000000000000000000000000000000000000000
msg=$( GATE_ATTRIBUTE= GOV_GATE_CMD="bash $envr" bash "$tmp/hooks/pre-push" origin "$tmp/remote.git" \
       <<<"refs/heads/main $_c9l refs/heads/main $_c9z" 2>&1 )
case "$msg" in
  *"ATTR=$_c9z"*) bad "9b an all-zero remote sha was exported as a base to attribute against" ;;
  *"ATTR="*) ok "9b an all-zero remote sha exports no GATE_ATTRIBUTE" ;;
  *) bad "9b the runner did not run, so the control grades nothing: ${msg:-<no output>}" ;;
esac

# ============================================================================================
# THE BOUNDARY DECIDES. One arm per forcing predicate, plus the one that matters most: the arm
# proving a scoped run is EVER chosen. Without it every predicate below is satisfied by a hook
# that forces unconditionally — which is the hook this unit replaced, passing its own tests.
#
# The gate is stubbed, so what these grade is the DECISION LINE the hook prints, not a bar run.
decide() {   # -> the hook's decision line for a push of the current main
  # A COMMIT FIRST, because a push with nothing to send never invokes the hook at all — and a hook
  # that did not run is indistinguishable from one that decided nothing. Earlier cases have already
  # pushed main, so without this every arm below reads an empty line and reports a failure that is
  # really 'there was no push'.
  git commit -q --allow-empty -m "decide $RANDOM" >/dev/null 2>&1
  # BOTH streams. The refusal cases above capture stderr only, because a refusal is an error; the
  # decision line is ordinary progress output on STDOUT, and `1>/dev/null` threw it away — which
  # read as 'the hook made no decision' rather than 'the arm looked in the wrong place'.
  # GATE_SELFTESTS IS CLEARED, NOT INHERITED. It is an INPUT to the decision this function grades
  # (TOOL-dUnstalledConvoy-27's predicate 8), and the bar itself exports it — so under
  # `GATE_SELFTESTS=1 run-gates.sh` every arm below silently switched to the forcing case and the
  # control arm reported a hook bug that was really an uncontrolled input.
  ( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 ) | grep -m1 -E 'gate on main push' || true
}
stamp() {    # write a full-green record naming a sha, with a reproducible fingerprint
  # $2, when given, is the `selftests` value the record claims. OMITTED writes no key at all, which
  # is the shape of every record written before TOOL-dUnstalledConvoy-26 and is what AC4 grades.
  local sha=$1 st=${2-} gd; gd=$(git rev-parse --git-dir)
  local fp=""
  [ -x $KIT_REL/${RUN_GATES}/gate-fingerprint.sh ] && fp=$(bash $KIT_REL/${RUN_GATES}/gate-fingerprint.sh "$sha" 2>/dev/null)
  printf 'sha\t%s\nfingerprint\t%s\nmanifest_blob\t%s\nrun_id\ttest\n' \
    "$sha" "$fp" "$(git hash-object -- gate-legs.json 2>/dev/null)" > "$gd/gate-full-green"
  [ -n "$st" ] && printf 'selftests\t%s\n' "$st" >> "$gd/gate-full-green"
  return 0
}
decide_on() {   # the hook's decision line for a push made WITH the self-test switch on
  git commit -q --allow-empty -m "decide-on $RANDOM" >/dev/null 2>&1
  ( GATE_SELFTESTS=1 GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 ) | grep -m1 -E 'gate on main push' || true
}

# --- the control FIRST: a fresh, covered record must choose SCOPED ---------------------------
stamp "$(git rev-parse HEAD)"
line=$(decide)
case "$line" in
  *"scoped gate"*) ok "9 control — a current, covered recorded green chooses a SCOPED run" ;;
  *) bad "9 a current recorded green did not produce a scoped run, so every forcing arm below is vacuous: ${line:-<no decision line>}" ;;
esac

# --- no record at all -------------------------------------------------------------------------
rm -f "$(git rev-parse --git-dir)/gate-full-green"
case "$(decide)" in
  *"FULL gate"*"no recorded full green"*) ok "10 no recorded green → FULL, and the reason says so" ;;
  *) bad "10 an absent record did not force a full run" ;;
esac

# --- a record naming a sha that is not an ancestor of the pushed tip --------------------------
stamp "0000000000000000000000000000000000000000"
case "$(decide)" in
  *"FULL gate"*) ok "11 a record naming an unreachable sha → FULL" ;;
  *) bad "11 a record naming an unreachable sha did not force" ;;
esac

# --- the record is further behind than the declared bound -------------------------------------
base_sha=$(git rev-parse HEAD)
lagbound=$(grep -m1 -oE 'GATE_FULL_MAX_LAG=[0-9]+' "$tmp/hooks/pre-push" | grep -oE '[0-9]+')
# READ FROM THE HOOK rather than pinned here: a bound written into this arm is satisfied by
# whatever the source happens to say, including a value that makes the arm unreachable.
if [ -z "$lagbound" ]; then
  bad "12 could not read GATE_FULL_MAX_LAG out of the hook, so the lag arm has no bound to grade"
else
  i=0; while [ "$i" -le "$lagbound" ]; do i=$((i+1)); echo "lag $i" >> lagfile.txt; git add -A >/dev/null 2>&1; git commit -qm "lag $i" >/dev/null 2>&1; done
  stamp "$base_sha"
  case "$(decide)" in
    *"FULL gate"*"first-parent landings behind the tip"*) ok "12 a record more than GATE_FULL_MAX_LAG=$lagbound first-parent landings back → FULL" ;;
    *) bad "12 a stale-by-lag record did not force a full run" ;;
  esac
fi

# --- 12b: the lag is counted in FIRST-PARENT LANDINGS (TOOL-aFrugalTurnstile-1 AC1; arm 12 is AC2) ---
# A green at a branch tip, then main takes a 12-commit --no-ff landing, then the branch lands --no-ff.
# All-commit counting charged the green 14 for that and forced FULL; first-parent counting charges the
# two landings plus decide's own commit. Arm 12 above keeps the linear run past the bound forcing.
git checkout -q -b ft-feat >/dev/null 2>&1
echo f > ftfeat.txt; git add ftfeat.txt >/dev/null 2>&1; git commit -qm "ft feat" >/dev/null 2>&1
stamp "$(git rev-parse HEAD)"
git checkout -q main >/dev/null 2>&1; git checkout -q -b ft-side >/dev/null 2>&1
for i in 1 2 3 4 5 6 7 8 9 10 11 12; do
  echo "$i" > ftside.txt; git add ftside.txt >/dev/null 2>&1; git commit -qm "ft side $i" >/dev/null 2>&1
done
git checkout -q main >/dev/null 2>&1
git merge -q --no-ff -m "land ft-side" ft-side >/dev/null 2>&1
git merge -q --no-ff -m "land ft-feat" ft-feat >/dev/null 2>&1
case "$(decide)" in
  *"scoped gate"*"first-parent landing(s) back"*) ok "12b a branch green landed after a 12-commit landing scopes, counted in first-parent landings" ;;
  *) bad "12b a branch green behind two first-parent landings did not scope" ;;
esac

# --- 12c: a record earned on ANOTHER leg manifest (TOOL-aFrugalTurnstile-1 AC3) -----------------
stamp "$(git rev-parse HEAD)"
printf 'manifest\t%s\n' elsewhere/legs.json >> "$(git rev-parse --git-dir)/gate-full-green"
case "$(decide)" in
  *"FULL gate"*"leg manifest elsewhere/legs.json"*"reads gate-legs.json"*) ok "12c a record naming a foreign manifest → FULL, naming both manifests" ;;
  *) bad "12c a record earned on elsewhere/legs.json did not force FULL with both paths named" ;;
esac

# --- the pushed diff touches the leg manifest -------------------------------------------------
stamp "$(git rev-parse HEAD)"
case "$(decide)" in *"scoped gate"*) : ;; *) bad "13 precondition — could not get back to a scoped decision" ;; esac
prev=$(git rev-parse HEAD)
# AT THE ROOT, which the hook's ladder finds with no declaration (TOOL-aRepatriatedFork-24 S2). A
# manifest under a prefix this fixture never declares is the refusal case the AC3 arm below grades.
printf '%s\n' '[{"name":"x","argv":["bash","x.sh"]}]' > gate-legs.json
git add -A >/dev/null 2>&1; git commit -qm "touch the manifest" >/dev/null 2>&1
stamp "$prev"
case "$(decide)" in
  *"FULL gate"*) ok "14 a diff touching the leg manifest → FULL (the scoping rules themselves moved)" ;;
  *) bad "14 a diff that moved the leg manifest did not force a full run" ;;
esac

# --- and the decision is ALWAYS announced -----------------------------------------------------
case "$(decide)" in
  *"gate on main push"*) ok "15 the boundary prints its decision and its reason on one line, every time" ;;
  *) bad "15 the boundary made a decision without announcing it" ;;
esac
# --- 19-23: THE SWITCH FIELD IS READ (TOOL-dUnstalledConvoy-27) -------------------------------
# The stamp records whether the kit-subject legs ran. Written and never read, that field is a byte
# nobody consults and the boundary trusts a partial bar as a whole one. The relation is COVERAGE,
# not equality: a record that covered MORE still satisfies a push that needs less.
cd "$tmp/work" || exit 2

# 19 — a record earned switch-OFF does not satisfy a switch-ON push. This is the only direction
#      that forces, and it is the one the whole unit is for.
stamp "$(git rev-parse HEAD)" 0
line=$(decide_on)
case "$line" in
  *"FULL gate"*) ok "19 a switch-OFF record offered for a switch-ON push → FULL" ;;
  *) bad "19 a record that never ran the kit self-tests satisfied a push that does: ${line:-<no decision line>}" ;;
esac

# 20 — and the reason NAMES the switch. A run forced for an unstated reason teaches its operator
#      nothing, and this line is the only window into the decision.
case "$line" in
  *"kit self-tests"*"HELD"*) ok "20 and the forcing reason names the switch" ;;
  *) bad "20 the boundary forced without saying the switch was why: ${line:-<no decision line>}" ;;
esac

# 21 — AC4: a record with NO switch key at all reads as OFF. Every stamp written before the parent
#      unit lacks the key, and reading its absence as 'covered everything' would make each of them
#      certify legs it never ran.
stamp "$(git rev-parse HEAD)"
case "$(decide_on)" in
  *"FULL gate"*"kit self-tests"*) ok "21 a record with NO switch key reads as OFF" ;;
  *) bad "21 a record missing the switch key was treated as covering the kit self-tests" ;;
esac

# 22 — COVERAGE, not equality: a record earned switch-ON satisfies a switch-OFF push. Equality here
#      would force a full run on every adopter's ordinary push and delete the parent unit's saving.
stamp "$(git rev-parse HEAD)" 1
case "$(decide)" in
  *"scoped gate"*) ok "22 a switch-ON record satisfies a switch-OFF push (coverage, not equality)" ;;
  *) bad "22 a STRONGER record forced a full run, which is equality wearing coverage's name" ;;
esac

# 23 — its control: switch-ON record, switch-ON push. Without this, an implementation that forced
#      on every switch-ON push would still pass 19 through 22.
stamp "$(git rev-parse HEAD)" 1
case "$(decide_on)" in
  *"scoped gate"*) ok "23 control — a switch-ON record satisfies a switch-ON push" ;;
  *) bad "23 a record that covered the kit self-tests did not satisfy a push that runs them" ;;
esac

# 24 — THE HOOK SOURCES THE REPOSITORY'S OWN GATE POLICY. TOOL-dUnstalledConvoy-28 moved gov's
#      GATE_SELFTESTS out of this hook — which ships verbatim to every push-main adopter — and into
#      `.githooks/gate-env.sh`, which no kit claims. The MECHANISM travels and the CHOICE does not,
#      and until now nothing anywhere arms the mechanism half: delete the two source lines and every
#      other arm in this file stays green while gov silently stops running its own kit self-tests.
#      Driven through the DECISION, not through the environment: the switch is only observable here
#      by what predicate 8 does with it.
mkdir -p "$tmp/work/.githooks"
printf '#!/usr/bin/env sh\nexport GATE_SELFTESTS=1\n' > "$tmp/work/.githooks/gate-env.sh"
git -C "$tmp/work" add -A >/dev/null 2>&1
stamp "$(git rev-parse HEAD)" 0
case "$(decide)" in
  *"FULL gate"*"kit self-tests"*) ok "24 the hook sources .githooks/gate-env.sh, so the repo's own switch reaches the decision" ;;
  *) bad "24 a gate-env.sh setting the switch did not reach the boundary — the sourcing is dead: $(decide)" ;;
esac
# ITS CONTROL: remove the file and the same push decides SCOPED again. Without it the arm above
# passes on a hook that forces unconditionally.
rm -f "$tmp/work/.githooks/gate-env.sh"
git -C "$tmp/work" add -A >/dev/null 2>&1
stamp "$(git rev-parse HEAD)" 0
case "$(decide)" in
  *"scoped gate"*) ok "24b control — with no gate-env.sh the same push is SCOPED" ;;
  *) bad "24b the boundary forced with no gate-env.sh present, so arm 24 proves nothing" ;;
esac

# --- 25-29b: WHICH BAR RAN (TOOL-aRepatriatedFork-5, adopter nc's PKG-dCandidLodestar-5) --------
# Until this unit `gate` was resolved from GOV_GATE_CMD with no check at all, and the decision line
# named the SCOPE of the run without naming WHAT ran. `GOV_GATE_CMD=true git push` landed a commit
# over a bar that never existed, under a line byte-identical to a full run's. THE ESCAPE IS UNSET IN
# EACH ARM BELOW rather than at the top, because every earlier case in this file depends on it.
# `.githooks/pre_push_bar_selftest.py` covers the evasions and disables the arms that refuse them.
cd "$tmp/work" || exit 2
printf '#!/usr/bin/env bash\nexit 0\n' > tracked-bar.sh
# DECLARED, since the hook refuses a tracked bar that `.unattended.conf` does not name as GATE_CMD
# (closing review round 1 M1); `.githooks/pre_push_bar_selftest.py` grades the undeclared case.
printf 'GATE_CMD="bash tracked-bar.sh"\n' > .unattended.conf
git add -A >/dev/null 2>&1; git commit -qm "a tracked bar" >/dev/null 2>&1

# 25 — THE CONTROL FIRST: a bar this repo TRACKS is accepted with no escape. Without it, 26 and 27
#      are satisfied by a hook that refuses every value it is handed, which is its own outage.
git commit -q --allow-empty -m c25 >/dev/null 2>&1
if ( unset GOV_GATE_CMD_TEST; GOV_GATE_CMD="bash tracked-bar.sh" git push -q origin main >/dev/null 2>&1 ); then
  ok "25 control — a TRACKED bar command is accepted with no test escape"
else
  bad "25 a tracked bar was refused, so 26-27 prove only that the hook refuses everything"
fi

# 25b — a tracked bar that is NOT this kit's runner adopts no runner stamp (TOOL-aFrugalTurnstile-1
#       AC4): a green the runner earned proves the runner's legs, never this bar's. The stamp is at the
#       tip and otherwise valid, so before the unit this push scoped.
git commit -q --allow-empty -m c25b >/dev/null 2>&1
stamp "$(git rev-parse HEAD)"
git commit -q --allow-empty -m c25b2 >/dev/null 2>&1
line=$( ( unset GOV_GATE_CMD_TEST; GOV_GATE_CMD="bash tracked-bar.sh" git push -q origin main 2>&1 ) | grep -m1 -E 'gate on main push' || true )
case "$line" in
  *"FULL gate"*"is not this kit's runner"*) ok "25b a non-runner bar forces FULL and names why no runner stamp is a candidate" ;;
  *) bad "25b a runner stamp was a candidate for a bar that is not the runner: ${line:-<no decision line>}" ;;
esac

# 26 — an UNTRACKED bar is refused. $green lives under mktemp, so it is untracked by construction —
#      the same shape every stub in this file has. GREEN, not red, deliberately: with a red stub the
#      push fails either way and the arm cannot tell a refusal from a bar doing its job.
git commit -q --allow-empty -m c26 >/dev/null 2>&1
msg=$( ( unset GOV_GATE_CMD_TEST; GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 1>/dev/null ) )
case "$msg" in
  *"does not track"*) ok "26 an UNTRACKED bar command is refused" ;;
  *) bad "26 expected a refusal naming the untracked bar, got: ${msg:-<push SUCCEEDED over a bar nobody has read>}" ;;
esac

# 26b — and a tracked name may not merely TRAIL the one that runs. `bash $green tracked-bar.sh`
#       ends in a tracked script and executes an untracked one, so a rule reading only the LAST
#       path-shaped token accepts it — gating the instance rather than the class.
git commit -q --allow-empty -m c26b >/dev/null 2>&1
msg=$( ( unset GOV_GATE_CMD_TEST; GOV_GATE_CMD="bash $green tracked-bar.sh" git push -q origin main 2>&1 1>/dev/null ) )
case "$msg" in
  *"does not track"*) ok "26b an untracked token is refused even when a tracked one follows it" ;;
  *) bad "26b a tracked name trailing an untracked command was accepted: ${msg:-<push SUCCEEDED>}" ;;
esac

# 27 — a value naming NO script at all is refused outright. `true` is the unit's own reproduction: a
#      real command that exits 0 and gates nothing.
git commit -q --allow-empty -m c27 >/dev/null 2>&1
msg=$( ( unset GOV_GATE_CMD_TEST; GOV_GATE_CMD=true git push -q origin main 2>&1 1>/dev/null ) )
case "$msg" in
  *"names no script"*) ok "27 GOV_GATE_CMD=true is refused — a no-op bar names nothing" ;;
  *) bad "27 'true' was accepted as the merge bar, got: ${msg:-<push SUCCEEDED with no bar at all>}" ;;
esac

# 28 — the escape DECLARES ITSELF. Under GOV_GATE_CMD_TEST the untracked stub is let through, and
#      the decision line says so. A silent waiver would be the defect wearing a test's name.
line=$(decide)
case "$line" in
  *"bar: STUB "*) ok "28 under the test escape the decision line marks the bar as a STUB" ;;
  *) bad "28 the test escape waived the check without saying so: ${line:-<no decision line>}" ;;
esac

# 29 — and the bar is named in BOTH arms. This line is the only durable record of which bar ran, and
#      a field added to one arm is half a record.
stamp "$(git rev-parse HEAD)"
line=$(decide)
case "$line" in
  *"scoped gate"*"bar: "*) ok "29 the SCOPED decision line names the bar that ran" ;;
  *) bad "29 the scoped arm reports a scope without naming the bar: ${line:-<no decision line>}" ;;
esac
rm -f "$(git rev-parse --git-dir)/gate-full-green"
line=$(decide)
case "$line" in
  *"FULL gate"*"bar: "*) ok "29b the FULL decision line names the bar that ran" ;;
  *) bad "29b the full arm reports a scope without naming the bar: ${line:-<no decision line>}" ;;
esac

# 30 — TOOL-dThriftyLanding-2: A GREEN FROM ANOTHER WORKTREE SERVES THIS PUSH. This fixture is a plain
#      clone, so its git dir IS the common dir and its own stamp is the primary's; a linked worktree's
#      runner writes `gate-full-green.shared` beside it. With no own stamp and a usable shared one, the
#      decision is scoped and names where its record came from; with an unusable shared one it is FULL
#      and names BOTH refusals, so neither is silent; and the own stamp still wins when it is usable.
_gd30=$(git rev-parse --git-dir)
rm -f "$_gd30/gate-full-green" "$_gd30/gate-full-green.shared"
printf 'sha\t%s\nfingerprint\t\nmanifest_blob\t\nrun_id\ttest\n' "$(git rev-parse HEAD)" > "$_gd30/gate-full-green.shared"
line=$(decide)
case "$line" in
  *"scoped gate"*"gate-full-green.shared"*) ok "30 a shared green from another worktree scopes the push and is named" ;;
  *) bad "30 a usable shared green was not adopted: ${line:-<no decision line>}" ;;
esac
printf 'sha\t%s\nfingerprint\t\nmanifest_blob\t\nrun_id\ttest\n' 0000000000000000000000000000000000000000 > "$_gd30/gate-full-green.shared"
line=$(decide)
case "$line" in
  *"FULL gate"*"no recorded full green"*"gate-full-green.shared"*"not an ancestor"*) ok "30b an unusable shared green forces FULL and both refusals are named" ;;
  *) bad "30b expected FULL naming the own and the shared refusal: ${line:-<no decision line>}" ;;
esac
stamp "$(git rev-parse HEAD)"
line=$(decide)
case "$line" in
  *"scoped gate"*" from "*) bad "30c a usable own stamp was passed over for a shared one: $line" ;;
  *"scoped gate"*) ok "30c control — a usable own stamp is adopted first, worded as before" ;;
  *) bad "30c control — a current own stamp did not scope: ${line:-<no decision line>}" ;;
esac
rm -f "$_gd30/gate-full-green" "$_gd30/gate-full-green.shared"

# --- 16-18: TOOL-dScrubbedConduit-1 S2/S5. A LINKED WORKTREE, because that is the shape this
# --- harness could not previously see. Every fixture above is `git init` plus `git init --bare`, and
# --- neither exports GIT_DIR into a hook — which is exactly why this class went unobserved here
# --- while an adopter hit it head-on. The fixture had to change for the RED to be observable.
SCRUB="GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES GIT_COMMON_DIR GIT_NAMESPACE GIT_PREFIX"

# 16 — the hook still CARRIES the scrub. Asserted against the hook's own bytes so that deleting the
# unset line reds this arm, rather than the arm silently testing its own inlined copy.
miss=""
for v in $SCRUB; do
  grep -qE "^unset .*\b$v\b|^ +$v\b" "$tmp/hooks/pre-push" || miss="$miss $v"
done
if [ -n "$miss" ]; then
  bad "16 the hook no longer scrubs:$miss — a leg that git-inits a scratch repo can rewrite the shared config"
else
  ok "16 the hook scrubs every injected git variable before running anything"
fi
# GIT_EXEC_PATH must SURVIVE: it locates git's own helpers and clearing it breaks git rather than
# protecting it. A scrub that over-reaches is its own defect.
if grep -qE "^unset .*GIT_EXEC_PATH|^ +GIT_EXEC_PATH\b" "$tmp/hooks/pre-push"; then
  bad "16b the hook scrubs GIT_EXEC_PATH, which breaks git instead of protecting it"
else
  ok "16b the scrub leaves GIT_EXEC_PATH alone"
fi

# 17 — the MECHANISM, in a real linked worktree: unscrubbed it poisons the shared config, scrubbed it
# does not. Both directions, because a one-sided arm cannot tell a working scrub from a fixture that
# never reproduced the bug.
wt=$(mktemp -d)
( git init -q "$wt/w" && cd "$wt/w" && git config user.email t@t && git config user.name t \
    && echo x > a && git add -A && git commit -qm init && git worktree add -q "$wt/lw" -b lw ) >/dev/null 2>&1
wtcfg="$wt/w/.git/config"
wtgd="$wt/w/.git/worktrees/lw"
if [ -d "$wtgd" ]; then
  git config --file "$wtcfg" core.bare false
  ( cd "$wt" && GIT_DIR="$wtgd" sh -c 'd=$(mktemp -d); cd "$d" && git init -q .' ) >/dev/null 2>&1
  poisoned=$(git config --file "$wtcfg" --get core.bare)
  git config --file "$wtcfg" core.bare false
  ( cd "$wt" && GIT_DIR="$wtgd" sh -c "unset $SCRUB; d=\$(mktemp -d); cd \"\$d\" && git init -q ." ) >/dev/null 2>&1
  guarded=$(git config --file "$wtcfg" --get core.bare)
  if [ "$poisoned" != true ]; then
    bad "17 the fixture did not reproduce the injection, so this arm proves nothing (git behaviour changed?)"
  elif [ "$guarded" = true ]; then
    bad "17 the scrub did not stop a scratch-repo leg rewriting the shared config"
  else
    ok "17 unscrubbed poisons the shared config and scrubbed does not (linked worktree, no submodule)"
  fi
else
  bad "17 could not build a linked-worktree fixture, so the GIT_DIR-injection class went UNTESTED"
fi

# 18 — the hook REFUSES when it cannot resolve its repo. This used to `exit 0`, and exit 0 from a
# pre-push hook means ALLOW: measured end to end, a push landed on the remote with the bar never run.
nr=$(mktemp -d)
printf 'main\nrefs/heads/main\n' > "$nr/in"
( cd "$nr" && bash "$tmp/hooks/pre-push" origin git@example:x.git < "$nr/in" ) >/dev/null 2>&1
if [ "$?" = 0 ]; then
  bad "18 the hook ALLOWED a push from a tree whose repo it could not resolve — fail-open"
else
  ok "18 the hook refuses when it cannot resolve its repo, instead of failing open"
fi
rm -rf "$wt" "$nr"


# ============================================================================================
# TOOL-dRetiredFork-11 — THE HOOK RESOLVES ITS OWN KIT ROOT.
#
# Everything above this line runs in a fixture that keeps its leg manifest at ONE fixed place — gov's
# own prefix when this was written, the root since TOOL-aRepatriatedFork-24 — so every arm above
# would pass unchanged with that place hardcoded, and did.
# That is the shape of the defect: the suite could not tell a resolving hook from a hardcoded one,
# because it only ever asked in the layout the hardcoding happened to match.
#
# These arms ask in the OTHER layout, and they compare against the pre-change hook on the SAME
# fixture. A new arm that has only ever been run against the fixed code proves nothing about what
# it fixed.
pfx_home=$PWD
# `git -C "$SRC"`, NOT a bare `git show`: by this line the suite is standing inside its own scratch
# repo, where HEAD carries no .githooks/ at all. The bare form wrote an EMPTY file, the red-first
# control below hit its `[ -s ]` guard and skipped, and the suite still printed all-ok — a control
# that silently does not run is worse than no control.
# PINNED TO AN IMMUTABLE SHA, not HEAD. Reading HEAD made this control SELF-INVALIDATING: the
# moment TOOL-dRetiredFork-11 landed, "the pre-change hook" became the fixed one and the arm
# reported that it "already forced — this arm proves nothing". It was green when run before the
# commit and red immediately after, which is the worst possible timing for a control nobody re-runs.
# 05455c45 is the last commit that touched this hook BEFORE that unit.
PREPUSH_PRE=05455c45fc0fc32f7de331541daea5c57cb856e0
git -C "$SRC" show "$PREPUSH_PRE:.githooks/pre-push" > "$tmp/hooks-old-pre-push" 2>/dev/null || true
# THE RED-FIRST CONTROL IS GOV-ONLY, AND THE SKIP SAYS SO OUT LOUD (TOOL-aRepatriatedFork-5 S6, the
# form of adopter nc's carve-out 25). `PREPUSH_PRE` is a commit in the coding-governance repository.
# This file ships to every push-main adopter, and no adopter has that object, so the arm cannot
# resolve there and `bad` reddened the leg over gov's history rather than over anything the adopter
# did. Substituting an adopter sha does not rescue it: the control has to be a hook that did NOT
# force in the fixture's layout, which is structurally gov's fix. So it SKIPS, loudly, naming what
# went unexercised; it is counted as neither a pass nor a failure. The loop below then skips the
# `old` pass by its own `[ -s ]` guard.
if [ ! -s "$tmp/hooks-old-pre-push" ]; then
  echo "  SKIP — AC1 red-first control NOT RUN: $PREPUSH_PRE is a coding-governance commit and"
  echo "         this repository does not carry it. The AC1/AC2/AC3 arms below still run; what"
  echo "         is unexercised is the proof that the PRE-fix hook failed where they pass."
fi

# Build a scratch repo whose kits live at $1, push once so a record can name a real sha, and leave
# the caller standing in it.
pfx_fixture() {
  local pfx=$1 hook=$2 tag=$3
  # SPLIT deliberately: `local a=$1 d="...$a..."` reads $a as unset under `set -u` here, so the
  # fixture builder died before it built anything. One name per statement.
  local d="$tmp/pfx-$pfx-$tag"
  mkdir -p "$d/hooks"; cp "$hook" "$d/hooks/pre-push"
  git init -q --bare "$d/remote.git"; git init -q "$d/work"
  cd "$d/work" || return 1
  git config user.email t@example.com; git config user.name t
  git config core.hooksPath "$d/hooks"
  mkdir -p "$pfx"
  printf '%s\n' '[{"name":"x","argv":["bash","a.sh"]}]' > "$pfx/gate-legs.json"
  # THE ROOT IS DECLARED, as a copy-installed adopter declares it (TOOL-aRepatriatedFork-24 S2): no
  # receipt and no root install, so the committed gate-env.sh is the rung that reaches it. `nowhere`
  # declares nothing, because the AC3 arm grades a manifest the ladder does NOT reach.
  if [ "$pfx" != nowhere ]; then
    mkdir -p .githooks; printf 'GOV_KITROOT=%s\n' "$pfx" > .githooks/gate-env.sh
  fi
  git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
  git remote add origin "$d/remote.git"
  touch "$(git rev-parse --git-dir)/push-main-active"
  GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1
}
# A full-green record for a fixture at $1, naming sha $2. Deliberately NOT the `stamp` above: that
# one spells `<prefix>/` itself, which is the very assumption under test here.
pfx_stamp() {
  local pfx=$1 sha=$2 blob=${3-} gd; gd=$(git rev-parse --git-dir)
  [ -n "$blob" ] || blob=$(git hash-object -- "$pfx/gate-legs.json" 2>/dev/null)
  printf 'sha\t%s\nfingerprint\t%s\nmanifest_blob\t%s\nrun_id\ttest\n' "$sha" "" "$blob" \
    > "$gd/gate-full-green"
}
pfx_decide() {
  git commit -q --allow-empty -m "decide $RANDOM" >/dev/null 2>&1
  ( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 ) \
    | grep -m1 -E 'gate on main push' || true
}

# --- AC1: a manifest change at a NON-tools prefix must force a full run ------------------------
for _h in new old; do
  case $_h in new) _hook="$SRC/.githooks/pre-push" ;; old) _hook="$tmp/hooks-old-pre-push" ;; esac
  [ -s "$_hook" ] || continue
  pfx_fixture scripts "$_hook" "ac1$_h" || { bad "AC1 could not build the $_h fixture"; continue; }
  pfx_stamp scripts "$(git rev-parse HEAD)"
  case "$(pfx_decide)" in
    *"scoped gate"*) [ "$_h" = new ] && ok "AC1 precondition — a scripts/ tree reaches a SCOPED decision" ;;
    *) [ "$_h" = new ] && bad "AC1 precondition — no scoped decision at a scripts/ prefix" ;;
  esac
  _prev=$(git rev-parse HEAD)
  printf '%s\n' '[{"name":"x","argv":["bash","b.sh"]},{"name":"y","argv":["bash","c.sh"]}]' \
    > scripts/gate-legs.json
  git add -A >/dev/null 2>&1; git commit -qm "move the manifest" >/dev/null 2>&1
  pfx_stamp scripts "$_prev"
  _dec=$(pfx_decide)
  case "$_h:$_dec" in
    new:*"FULL gate"*) ok "AC1 a manifest change at scripts/ FORCES a full run (predicate 6 fires)" ;;
    new:*) bad "AC1 predicate 6 did not fire at a scripts/ prefix: ${_dec:-<no decision>}" ;;
    old:*"FULL gate"*) bad "AC1 the PRE-CHANGE hook already forced — this arm proves nothing" ;;
    old:*) ok "AC1 red-first: the pre-change hook did NOT force here — it matched nothing" ;;
  esac
done

# --- AC2: a recorded manifest blob that differs, at that same prefix ---------------------------
pfx_fixture scripts "$SRC/.githooks/pre-push" ac2 || bad "AC2 could not build its fixture"
pfx_stamp scripts "$(git rev-parse HEAD)" "0000000000000000000000000000000000000000"
_dec=$(pfx_decide)
case "$_dec" in
  *"differs from the one the recorded green was earned on"*)
    ok "AC2 a differing recorded manifest blob at scripts/ FORCES (predicate 7 fires)" ;;
  *) bad "AC2 predicate 7 did not fire at a scripts/ prefix: ${_dec:-<no decision>}" ;;
esac

# --- AC3: a manifest the resolved root does NOT point at is a REFUSAL, not a non-match ---------
# The distinction the whole unit turns on. A tree that tracks a manifest somewhere the hook does not
# look must SAY SO; reading it as "no change here" is what let a manifest-wide change land scoped.
pfx_fixture nowhere "$SRC/.githooks/pre-push" ac3 >/dev/null 2>&1
git commit -q --allow-empty -m c >/dev/null 2>&1
_out=$( GOV_GATE_CMD="bash $green" git push -q origin main 2>&1 )
case "$_out" in
  *"REFUSING"*"resolved its kit root"*)
    ok "AC3 a manifest outside the resolved root REFUSES and names the resolution" ;;
  *) bad "AC3 expected a refusal naming the failed resolution, got: ${_out:-<push SUCCEEDED>}" ;;
esac
# ANTI-VACUITY: a repo with NO manifest anywhere is a legitimate case and must NOT refuse, or the
# arm above is satisfied by a hook that refuses everything.
pfx_fixture scripts "$SRC/.githooks/pre-push" ac3b >/dev/null 2>&1
rm -f scripts/gate-legs.json; git add -A >/dev/null 2>&1
git commit -qm "no manifest at all" >/dev/null 2>&1
if GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1; then
  ok "AC3 a tree with no manifest ANYWHERE is left alone, so the refusal is not universal"
else bad "AC3 the hook refused a tree that simply has no leg manifest"; fi

# --- TOOL-aRepatriatedFork-24 AC3: the DEFAULT bar under `vendor/gov/`, a prefix the old probe
# --- could never produce. `tools` or `scripts` were its only answers, so the bar named a runner that
# --- does not exist. The kit and its runner are joined at run time, as the hook joins them.
vg=vendor/gov; rgk=run-gates
vgd="$tmp/vg"; mkdir -p "$vgd/hooks"; cp "$SRC/.githooks/pre-push" "$vgd/hooks/pre-push"
git init -q --bare "$vgd/remote.git"; git init -q "$vgd/work"
cd "$vgd/work" || exit 2
git config user.email t@example.com; git config user.name t; git config core.autocrlf false
git config core.hooksPath "$vgd/hooks"
mkdir -p "${vg}/$rgk" .githooks
# The stub writes the GREEN run record a real runner would: an exit 0 with no verdict is RED since
# TOOL-dDerivedDocket-26, and this arm is about which runner is named, not about that rule.
printf '%s\n' '#!/usr/bin/env bash' 'echo "VENDOR BAR RAN"'   'd="$(git rev-parse --git-dir)/gate-run/$GATE_RUN_ID"; mkdir -p "$d"; printf "verdict\tGREEN\n" > "$d/verdict"'   'exit 0' > "${vg}/$rgk/$rgk.sh"
printf '%s\n' '[]' > "${vg}/gate-legs.json"
printf 'GOV_KITROOT=%s\n' "$vg" > .githooks/gate-env.sh
git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
git remote add origin "$vgd/remote.git"
touch "$(git rev-parse --git-dir)/push-main-active"
_out=$( ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; git push -q origin main 2>&1 ) ); _rc=$?
case "$_rc|$_out" in
  0\|*"bar: bash ${vg}/$rgk/$rgk.sh"*"VENDOR BAR RAN"*)
    ok "AC3 (24) the default bar at ${vg}/ names that runner and runs it" ;;
  *) bad "AC3 (24) the default bar did not name the ${vg}/ runner: rc=$_rc ${_out:-<no output>}" ;;
esac
git commit -q --allow-empty -m again
printf '#!/usr/bin/env bash\necho "MODIFIED BAR RAN"; exit 0\n' > "${vg}/$rgk/$rgk.sh"
_out=$( ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; git push -q origin main 2>&1 ) ); _rc=$?
case "$_rc|$_out" in
  0\|*|*"MODIFIED BAR RAN"*) bad "AC3 (24) a modified runner at ${vg}/ was run or passed: rc=$_rc $_out" ;;
  *) ok "AC3 (24) a modified runner at ${vg}/ is refused before it runs" ;;
esac
git checkout -q -- "${vg}/$rgk/$rgk.sh"
# ...and with NOTHING declared the same default bar is REFUSED by name (F1 (c)), never run as a
# guessed path that reads as a red bar.
git rm -q .githooks/gate-env.sh; git commit -q -m undeclare
_out=$( ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; git push -q origin main 2>&1 ) ); _rc=$?
case "$_rc|$_out" in
  0\|*) bad "AC3 (24) an undeclared ${vg}/ root let the default-bar push through" ;;
  *"leg manifest at '${vg}/gate-legs.json'"*"resolved its kit root nowhere"*)
    ok "AC3 (24) an undeclared root with a tracked manifest refuses, naming every rung that missed" ;;
  *) bad "AC3 (24) expected the manifest refusal naming the missed rungs, got: $_out" ;;
esac
git rm -q "${vg}/gate-legs.json"; git commit -q -m nomanifest
_out=$( ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; git push -q origin main 2>&1 ) ); _rc=$?
case "$_rc|$_out" in
  0\|*) bad "AC3 (24) an unresolvable kit root let the default-bar push through" ;;
  *"the default bar is this tree's kit runner, and the kit root resolved nowhere"*)
    ok "AC3 (24) an unresolvable kit root refuses the default bar by name (F1 c)" ;;
  *) bad "AC3 (24) expected the no-kit-root refusal, got: $_out" ;;
esac

# --- closing review round 1 B1 (TOOL-aRepatriatedFork-24): THE RECEIPT AND THE RUNNER IT NAMES ARE
# --- VETTED AS gate-env.sh IS. The default bar is the runner the install receipt names, and neither
# --- had to be tracked: an ignored receipt pointing at a runner under `.git/`, beside a planted
# --- manifest, ran that runner over a RED tracked bar and landed, with `git status` empty. Each arm
# --- stages that shape; the control proves a clean, tracked receipt still reaches its bar.
b1="$tmp/b1"; mkdir -p "$b1/hooks"; cp "$SRC/.githooks/pre-push" "$b1/hooks/pre-push"
git init -q --bare "$b1/remote.git"; git init -q "$b1/work"
cd "$b1/work" || exit 2
git config user.email t@example.com; git config user.name t; git config core.autocrlf false
git config core.hooksPath "$b1/hooks"
mkdir -p "$RUN_GATES"
printf '#!/usr/bin/env bash\necho "TRACKED BAR RAN - RED"; exit 1\n' > "$RUN_GATES/$RUN_GATES.sh"
printf '%s\n' '[]' > gate-legs.json
git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
git remote add origin "$b1/remote.git"
touch "$(git rev-parse --git-dir)/push-main-active"
b1_gd=$(git rev-parse --git-dir)
mkdir -p "$b1_gd/x/$RUN_GATES" .governance
printf '#!/usr/bin/env bash\necho "PLANTED BAR RAN"; exit 0\n' > "$b1_gd/x/$RUN_GATES/$RUN_GATES.sh"
printf '%s\n' '[]' > "$b1_gd/x/gate-legs.json"
printf '.governance/\n' >> "$b1_gd/info/exclude"
write_b1_receipt() { # <path the runner row records> -> the receipt, one key per line as the hook's reader expects
  printf '{\n  "files": [\n    {\n      "path": "%s",\n      "source": "%s/%s.sh"\n    }\n  ]\n}\n' \
    "$1" "$RUN_GATES" "$RUN_GATES" > .governance/install.json
}
run_b1_push() { git commit -q --allow-empty -m "b1 $RANDOM"; ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; git push -q origin main 2>&1 ); }
read_b1_token() { cut -f1 "$b1_gd/pre-push-refusal" 2>/dev/null; }
write_b1_receipt ".git/x/$RUN_GATES/$RUN_GATES.sh"
[ -z "$(git status --porcelain)" ] || bad "B1 fixture — the planted receipt is visible to git status, so the arm below tests nothing hidden"
_out=$(run_b1_push); _rc=$?
case "$_rc|$_out|$(read_b1_token)" in
  0\|*|*"PLANTED BAR RAN"*) bad "B1 an ignored receipt naming a runner under .git/ was followed: rc=$_rc $_out" ;;
  *".governance/install.json"*"|bar-refused") ok "B1 an ignored install receipt is refused as bar-refused before its runner runs" ;;
  *) bad "B1 expected the ignored receipt to be refused as bar-refused, got rc=$_rc: $_out | token '$(read_b1_token)'" ;;
esac
git add -f .governance/install.json; git commit -q -m "a tracked receipt naming an untracked runner"
_out=$(run_b1_push); _rc=$?
case "$_rc|$_out|$(read_b1_token)" in
  0\|*|*"PLANTED BAR RAN"*) bad "B1 a tracked receipt naming an untracked runner was followed: rc=$_rc $_out" ;;
  *"$RUN_GATES/$RUN_GATES.sh"*"|bar-refused") ok "B1 a tracked receipt naming an untracked runner is refused as bar-refused" ;;
  *) bad "B1 expected the untracked runner to be refused as bar-refused, got rc=$_rc: $_out | token '$(read_b1_token)'" ;;
esac
write_b1_receipt "$RUN_GATES/$RUN_GATES.sh"
git add -f .governance/install.json; git commit -q -m "a tracked receipt naming the tracked runner"
_out=$(run_b1_push); _rc=$?
case "$_rc|$_out|$(read_b1_token)" in
  0\|*) bad "B1 control — the tracked RED runner let the push through: $_out" ;;
  *"TRACKED BAR RAN - RED"*"|gate-red") ok "B1 control — a clean tracked receipt reaches its tracked runner, which refuses" ;;
  *) bad "B1 control expected the tracked bar to run and refuse, got rc=$_rc: $_out | token '$(read_b1_token)'" ;;
esac
write_b1_receipt ".git/x/$RUN_GATES/$RUN_GATES.sh"
_out=$(run_b1_push); _rc=$?
case "$_rc|$_out|$(read_b1_token)" in
  0\|*|*"PLANTED BAR RAN"*) bad "B1 a modified tracked receipt was followed: rc=$_rc $_out" ;;
  *".governance/install.json"*"differs"*"|bar-refused") ok "B1 a tracked receipt whose working copy differs is refused as bar-refused" ;;
  *) bad "B1 expected the modified receipt to be refused as bar-refused, got rc=$_rc: $_out | token '$(read_b1_token)'" ;;
esac

cd "$pfx_home" || exit 2

# --- closing review round 2 H1 (TOOL-aRepatriatedFork-49): THE BAR'S MANIFEST AND PYTHON ARE THE
# --- TRACKED ONES. B1 vetted the runner, and the runner still took its leg manifest from GATE_LEGS,
# --- its python from GOV_PYTHON, reused a ledger row under GATE_REUSE, and read an IGNORED manifest
# --- like a tracked one. Each route below landed a RED tracked bar on the ce8a78f5 hook. The fixture
# --- runs a COPY OF THE REAL RUNNER, because a stub runner reads none of those knobs and would pass
# --- every arm by never being asked. Each planted route writes a marker when it runs.
h49="$tmp/h49"; h49_mark="$h49/mark"; mkdir -p "$h49/hooks" "$h49_mark"
cp "$SRC/.githooks/pre-push" "$h49/hooks/pre-push"
git init -q --bare "$h49/remote.git"; git init -q "$h49/work"
cd "$h49/work" || exit 2
git config user.email t@example.com; git config user.name t; git config core.autocrlf false
git config core.hooksPath "$h49/hooks"
mkdir -p "$RUN_GATES" fx
cp "$SRC/$RUN_GATES_DIR/run-gates.sh" "$SRC/$RUN_GATES_DIR/gate-fingerprint.sh" \
   "$SRC/$RUN_GATES_DIR/gate-profiles.txt" "$RUN_GATES/"
printf 'import os, sys\nsys.exit(int(os.environ.get("H49_LEG_RC", "1")))\n' > fx/leg.py
printf '%s\n' '[{"name": "red leg", "argv": ["python3", "fx/leg.py"]}]' > gate-legs.json
git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
git remote add origin "$h49/remote.git"
h49_gd=$(cd "$(git rev-parse --git-dir)" && pwd)
touch "$h49_gd/push-main-active"
run_h49_push() { # NAME=VALUE... -> the output of a default-bar push of HEAD; the record is cleared so every push runs FULL
  ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST; rm -f "$h49_gd/gate-full-green"
    env GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_WALL=0 "$@" git push -q origin main 2>&1 )
}
read_h49_token() { cut -f1 "$h49_gd/pre-push-refusal" 2>/dev/null; }
read_h49_mark() { [ -e "$h49_mark/$1" ] && echo MARK; }
printf '[{"name": "planted", "argv": ["bash", "-c", "touch %s/legs"]}]\n' "$h49_mark" > "$h49/green.json"
printf '#!/usr/bin/env bash\ncase "$*" in *fx/leg.py*) touch "%s/python"; exit 0 ;; esac\nexec %s "$@"\n' \
  "$h49_mark" "$_rkd_py" > "$h49/fakepy"
chmod +x "$h49/fakepy"

git commit -q --allow-empty -m "h49 control"
_out=$(run_h49_push); _rc=$?
case "$_rc|$(read_h49_token)|$_out" in
  0\|*) bad "H49 control — the tracked RED leg let the push through: $_out" ;;
  *"|gate-red|"*"red leg"*) ok "H49 control — with nothing planted the tracked RED leg runs and refuses" ;;
  *) bad "H49 control expected the tracked red leg to refuse as gate-red, got rc=$_rc token '$(read_h49_token)': $_out" ;;
esac

git commit -q --allow-empty -m "h49 GATE_LEGS"
_out=$(run_h49_push GATE_LEGS="$h49/green.json"); _rc=$?
case "$_rc|$(read_h49_token)|$(read_h49_mark legs)|$_out" in
  0\|*|*\|MARK\|*) bad "H49 GATE_LEGS from the environment chose the manifest the bar ran: rc=$_rc $_out" ;;
  *"|gate-red||"*GATE_LEGS*) ok "H49 GATE_LEGS is not honoured: the tracked manifest runs, and the push names the knob" ;;
  *) bad "H49 expected GATE_LEGS to be ignored and named, with the push refused as gate-red, got rc=$_rc token '$(read_h49_token)': $_out" ;;
esac

git commit -q --allow-empty -m "h49 GOV_PYTHON"
_out=$(run_h49_push GOV_PYTHON="$h49/fakepy"); _rc=$?
case "$_rc|$(read_h49_token)|$(read_h49_mark python)" in
  0\|*|*\|MARK) bad "H49 GOV_PYTHON from the environment chose the python the bar ran: rc=$_rc $_out" ;;
  *"|gate-red|") ok "H49 GOV_PYTHON is not honoured: the red python leg runs under a resolved launcher" ;;
  *) bad "H49 expected GOV_PYTHON to be dropped and the push refused as gate-red, got rc=$_rc token '$(read_h49_token)': $_out" ;;
esac

# A direct green run writes the ledger row; the push then runs over the SAME tree and base, so on the
# old hook the row's key matched and the red leg was never executed.
# RE-STAGED BY TOOL-aFrugalTurnstile-4 S9: the row is earned WITHOUT GATE_FULL, so its `full` field is
# empty. The hook now exports GATE_REUSE=lineage on its own FULL decision, and a row a full run earned
# would be reused there, because this leg's verdict depends on H49_LEG_RC, which no input key sees:
# the not-checked class of the runner's reuse block, staged on purpose. An empty `full` keeps this arm
# testing what it names — `GATE_REUSE=1` semantics would reuse the row, lineage refuses it, and the
# red leg runs.
git commit -q --allow-empty -m "h49 GATE_REUSE"
( unset GOV_GATE_CMD GOV_GATE_CMD_TEST
  env -u GATE_FULL GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_WALL=0 H49_LEG_RC=0 bash "$RUN_GATES/run-gates.sh" >/dev/null 2>&1 )
_out=$(run_h49_push GATE_REUSE=1); _rc=$?
case "$_rc|$(read_h49_token)" in
  0\|*) bad "H49 GATE_REUSE from the environment reused a green row over the RED leg: $_out" ;;
  *"|gate-red") ok "H49 GATE_REUSE is not honoured: the red leg executes and refuses" ;;
  *) bad "H49 expected GATE_REUSE to be ignored and the push refused as gate-red, got rc=$_rc token '$(read_h49_token)': $_out" ;;
esac

# The IGNORED manifest: the repository tracks the runner and no manifest, and `git status` is empty.
git rm -q --cached gate-legs.json; printf 'gate-legs.json\n' >> "$h49_gd/info/exclude"
printf '[{"name": "planted", "argv": ["bash", "-c", "touch %s/ignored"]}]\n' "$h49_mark" > gate-legs.json
git commit -q -m "h49 an ignored manifest"
[ -z "$(git status --porcelain)" ] || bad "H49 fixture — the ignored manifest is visible to git status, so the arm below tests nothing hidden"
_out=$(run_h49_push); _rc=$?
case "$_rc|$(read_h49_token)|$(read_h49_mark ignored)|$_out" in
  0\|*|*\|MARK\|*) bad "H49 an ignored gate-legs.json was read as the bar's manifest: rc=$_rc $_out" ;;
  *"|bar-refused||"*gate-legs.json*) ok "H49 an ignored leg manifest is refused as bar-refused before the bar reads it" ;;
  *) bad "H49 expected the ignored manifest to be refused as bar-refused, got rc=$_rc token '$(read_h49_token)': $_out" ;;
esac

# --- TOOL-aFrugalTurnstile-4 S7: LINEAGE REUSE AT THE BOUNDARY. On a FULL decision for this kit's
# --- runner the hook exports GATE_REUSE=lineage itself, after the scrub, so the push that fixes a red
# --- re-runs the failed leg and the legs whose key moved, and lands on a stamp that says `reused 1`.
# --- No other bar gets the mode. A COPY OF THE REAL RUNNER again, for H49's reason: three legs, `pa`
# --- guarded on ga/, `pb` guarded on gb/ and red until gb/f says fixed, `pu` unguarded.
lin="$tmp/lin"; mkdir -p "$lin/hooks"
cp "$SRC/.githooks/pre-push" "$lin/hooks/pre-push"
git init -q --bare "$lin/remote.git"; git init -q "$lin/work"
cd "$lin/work" || exit 2
git config user.email t@example.com; git config user.name t; git config core.autocrlf false
git config core.hooksPath "$lin/hooks"
mkdir -p "$RUN_GATES" fx ga gb
cp "$SRC/$RUN_GATES_DIR/run-gates.sh" "$SRC/$RUN_GATES_DIR/gate-fingerprint.sh" \
   "$SRC/$RUN_GATES_DIR/gate-profiles.txt" "$RUN_GATES/"
printf '#!/usr/bin/env bash\necho a\n' > fx/a.sh
printf '#!/usr/bin/env bash\ngrep -q fixed gb/f\n' > fx/b.sh
printf '#!/usr/bin/env bash\necho u\n' > fx/u.sh
echo x > ga/f; echo broken > gb/f
printf '%s\n' '[' \
  '  {"name": "pa", "argv": ["bash", "fx/a.sh"], "guard": ["ga/"]},' \
  '  {"name": "pb", "argv": ["bash", "fx/b.sh"], "guard": ["gb/"]},' \
  '  {"name": "pu", "argv": ["bash", "fx/u.sh"]}' \
  ']' > gate-legs.json
git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
git remote add origin "$lin/remote.git"
lin_gd=$(cd "$(git rev-parse --git-dir)" && pwd)
touch "$lin_gd/push-main-active"
run_lin_push() { # NAME=VALUE... -> the output of a push of HEAD; the default bar unless the caller names one
  ( unset GOV_GATE_CMD GOV_GATE_CMD_TEST
    env GATE_PROFILE=minimal GATE_TURNSTILE=0 GATE_WALL=0 "$@" git push -q origin main 2>&1 )
}
read_lin_token() { cut -f1 "$lin_gd/pre-push-refusal" 2>/dev/null; }
read_lin_reused() { awk -F'\t' '$1 == "reused" { print $2 }' "$lin_gd/gate-full-green" 2>/dev/null; }

_out=$(run_lin_push); _rc=$?
case "$_rc|$(read_lin_token)|$_out" in
  *"|gate-red|"*"reuse: lineage"*"GATE FAIL  pb"*) ok "LIN AC11 control — the red push is FULL with reuse: lineage, and pb refuses it" ;;
  *) bad "LIN AC11 control expected a FULL lineage push refused as gate-red on pb, got rc=$_rc token '$(read_lin_token)': $_out" ;;
esac
# AC12's inherited arm rides the fix push: an exported GATE_REUSE=1 is still named as not honoured,
# and the mode the bar receives is the hook's own lineage.
echo fixed > gb/f; git add -A; git commit -q -m "lin fix"; rm -f "$lin_gd/pre-push-refusal"
_out=$(run_lin_push GATE_REUSE=1); _rc=$?
case "$_rc|$(read_lin_reused)|$_out" in
  "0|1|"*"not honoured from the environment by this bar:"*GATE_REUSE*"— reuse: lineage"*"GATE reuse pa  "*)
    ok "LIN AC11 the fix push reuses pa from the red run's ledger, lands, and stamps reused 1" ;;
  *) bad "LIN AC11 expected the fix push to reuse pa, land and stamp reused 1, got rc=$_rc reused '$(read_lin_reused)': $_out" ;;
esac
case "$_out" in
  *"GATE ok    pb"*"GATE ok    pu"*) ok "LIN AC11 control — the fixed leg and the unguarded leg executed on that push" ;;
  *) bad "LIN AC11 control expected pb and pu to execute on the fix push: $_out" ;;
esac

# AC12: the declared STUB gets no mode and no clause.
git commit -q --allow-empty -m "lin stub"; rm -f "$lin_gd"/gate-*green*
printf '#!/usr/bin/env bash\nexit 0\n' > "$lin/stub.sh"
_out=$(run_lin_push GOV_GATE_CMD_TEST=1 GOV_GATE_CMD="bash $lin/stub.sh"); _rc=$?
case "$_rc|$_out" in
  *"reuse: lineage"*) bad "LIN AC12 the STUB bar's FULL line carries reuse: lineage: $_out" ;;
  "0|"*"FULL gate on main push"*"bar: STUB"*) ok "LIN AC12 the STUB bar's FULL line names no reuse mode" ;;
  *) bad "LIN AC12 expected a FULL STUB push with no reuse clause, got rc=$_rc: $_out" ;;
esac
# AC12: a declared GATE_CMD naming another tracked script never receives the mode.
printf '#!/usr/bin/env bash\nprintf "%%s" "${GATE_REUSE-unset}" > "%s/other-saw"\nexit 0\n' "$lin" > other-bar.sh
printf 'GATE_CMD="bash other-bar.sh"\n' > .unattended.conf
git add -A; git commit -q -m "lin other"; rm -f "$lin_gd"/gate-*green*
_out=$(run_lin_push GOV_GATE_CMD="bash other-bar.sh"); _rc=$?
case "$_rc|$(cat "$lin/other-saw" 2>/dev/null)|$_out" in
  *"reuse: lineage"*) bad "LIN AC12 a non-runner bar's FULL line carries reuse: lineage: $_out" ;;
  "0|unset|"*) ok "LIN AC12 a declared non-runner bar runs with GATE_REUSE unset" ;;
  *) bad "LIN AC12 expected the declared bar to run with GATE_REUSE unset, got rc=$_rc saw '$(cat "$lin/other-saw" 2>/dev/null)': $_out" ;;
esac
cd "$pfx_home" || exit 2
# ---- TOOL-dDerivedDocket-24: THE INHERITED-RED POLICY, READ AT R ---------------------------------
# A scratch repo whose `.githooks/gate-env.sh` at the pushed remote tip R declares the policy under
# test, and a stub gate that writes the run record a real runner would: a RED verdict and one
# attribution row in the nine-column order, reading `GATE_RUN_ID` and `GATE_ATTRIBUTE` from the hook.
# The stub also records the policy the hook exported, so an arm can grade what reached the runner.
ir_env="$tmp/ir-env.txt"
irstub="$tmp/irstub.sh"
cat > "$irstub" <<'IRSTUB'
#!/usr/bin/env bash
d="$(git rev-parse --git-dir)/gate-run/$GATE_RUN_ID"; mkdir -p "$d"
printf 'verdict\tRED\nfailed\t1\ntree_moved\t%s\n' "${IR_MOVED:-no}" > "$d/verdict"
printf 'x\t%s\t1\t0\t%s\t%s\t-\t-\tstub\n' "${IR_VERDICT:-INHERITED}" "${GATE_ATTRIBUTE:-none}" "${IR_AGE:-3}" > "$d/attribution"
printf 'policy=%s age=%s attr=%s\n' "${GATE_INHERITED_RED:-}" "${GATE_INHERITED_RED_MAX_AGE:-}" "${GATE_ATTRIBUTE:-}" > "$IR_ENV"
echo "FAKE LEG failed"; exit 1
IRSTUB
build_ir_fixture() { # tag · gate-env body (printf %b) -> a pushed main whose R carries that body; sets IR_R
  local tag=$1 body=$2
  local d="$tmp/ir-$tag"
  mkdir -p "$d/hooks"; cp "$SRC/.githooks/pre-push" "$d/hooks/pre-push"
  git init -q --bare "$d/remote.git"; git init -q "$d/work"
  cd "$d/work" || return 1
  git config user.email t@example.com; git config user.name t
  git config core.hooksPath "$d/hooks"
  mkdir -p .githooks "$KIT_REL"
  printf '%s\n' '[{"name":"x","argv":["bash","a.sh"]}]' > "$KIT_REL/gate-legs.json"
  printf '%b' "$body" > .githooks/gate-env.sh
  # The kit root, on the rung this hook reads it from when no receipt or root install names it.
  printf 'GOV_KITROOT=%s\n' "$KIT_REL" >> .githooks/gate-env.sh
  git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
  git remote add origin "$d/remote.git"
  touch "$(git rev-parse --git-dir)/push-main-active"
  GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1
  IR_R=$(git rev-parse HEAD)
}
run_ir_push() { # [env assignments…] -> the push's merged output, then `rc=<n>` on its own line
  git commit -q --allow-empty -m "ir $RANDOM" >/dev/null 2>&1
  local o r
  o=$( env GATE_SELFTESTS= IR_ENV="$ir_env" GOV_GATE_CMD="bash $irstub" "$@" git push origin main 2>&1 ); r=$?
  printf '%s\nrc=%s\n' "$o" "$r"
}
write_ir_stamp() { # sha · base · max_age -> a planted gate-inherited-green
  printf 'sha\t%s\nfingerprint\t\nmanifest_blob\t\nselftests\t\nbase\t%s\nmax_age\t%s\nlegs\tx\nrun_id\ttest\n' \
    "$1" "$2" "$3" > "$(git rev-parse --git-dir)/gate-inherited-green"
}

# AC1, the hook's half: R says park and the pushed branch commits `land` into its OWN copy. The policy
# line reads park, and an inherited-only red is blocked. A reader of the working tree would land it.
build_ir_fixture ac1 'INHERITED_RED=park\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC1 could not build its fixture"
printf 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\nGOV_KITROOT=%s\n' "$KIT_REL" > .githooks/gate-env.sh
git add -A >/dev/null 2>&1; git commit -q -m "the branch grants itself land" >/dev/null 2>&1
_o=$(run_ir_push)
case "$_o" in
  *"inherited-red policy at ${IR_R:0:8} reads park"*"rc=1") ok "IR AC1 a branch-committed land is not read: R's park binds and the red is blocked" ;;
  *) bad "IR AC1 expected R's park and a blocked push, got: $_o" ;;
esac

# AC2: under land at R, a red whose one leg reads INHERITED and not aged lands, naming the leg; the
# same bar with the leg MIXED is blocked. The export reaches the runner too.
build_ir_fixture ac2 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC2 could not build its fixture"
_o=$(run_ir_push)
case "$_o" in
  *"red on inherited legs only — landing under INHERITED_RED=land: x"*"rc=0") ok "IR AC2 an inherited-only red within its age lands under land" ;;
  *) bad "IR AC2 expected the landing line and exit 0, got: $_o" ;;
esac
case "$(cat "$ir_env" 2>/dev/null)" in
  "policy=land age=10 attr=${IR_R}") ok "IR AC2 the runner is handed land, the bound 10 and R" ;;
  *) bad "IR AC2 the runner was handed: $(cat "$ir_env" 2>/dev/null)" ;;
esac
_o=$(run_ir_push IR_VERDICT=MIXED)
case "$_o" in
  *"this red does not land under INHERITED_RED=land — x reads MIXED"*"rc=1") ok "IR AC2 a MIXED leg is blocked under land" ;;
  *) bad "IR AC2 a MIXED leg must block, got: $_o" ;;
esac

# AC15: the same inherited-only record on a bar whose verdict reads tree_moved yes is blocked, naming it.
_o=$(run_ir_push IR_MOVED=yes)
case "$_o" in
  *"the tree moved while the bar ran, so no verdict describes the pushed commit"*"rc=1") ok "IR AC15 a moved tree blocks an inherited-only red" ;;
  *) bad "IR AC15 a moved tree must block, got: $_o" ;;
esac

# AC17, FLIPPED by TOOL-dUnstuckLanding-16 (ruling TOOL-dUnstuckLanding-22): an aged row, and an
# age-unproven one, LAND under land — the age escalates the driver's ask and decides no landing. Land
# beside a blank, zero or non-numeric bound reads land with NO bound, announced, and lands too; the
# runner is handed no bound.
for _a in aged -; do
  _o=$(run_ir_push IR_AGE="$_a")
  case "$_o" in
    *"red on inherited legs only — landing under INHERITED_RED=land: x"*"rc=0") ok "IR AC17 an inherited leg with age '$_a' lands under land" ;;
    *) bad "IR AC17 an inherited leg with age '$_a' must land under land, got: $_o" ;;
  esac
done
for _b in "" 0 ten; do
  build_ir_fixture "ac17$_b" "INHERITED_RED=land\nINHERITED_RED_MAX_AGE=$_b\n" || bad "IR AC17 could not build its fixture"
  _o=$(run_ir_push)
  case "$_o" in
    *"reads land — declared, with no age bound, so no leg is aged"*"landing under INHERITED_RED=land: x"*"rc=0")
      ok "IR AC17 land with the bound '$_b' reads land with no bound, announced, and lands" ;;
    *) bad "IR AC17 land with the bound '$_b' must read land with no bound, got: $_o" ;;
  esac
  case "$(cat "$ir_env" 2>/dev/null)" in
    "policy=land age= attr=${IR_R}") ok "IR AC17 land with the bound '$_b' hands the runner no bound" ;;
    *) bad "IR AC17 land with the bound '$_b' handed the runner: $(cat "$ir_env" 2>/dev/null)" ;;
  esac
done

# TOOL-dUnstuckLanding-16 AC3: R's policy file declares ONLY a bound. The kit default is land, so the
# policy line names it, and an aged inherited-only red lands. `park` declared beside the same bound
# blocks it, and a malformed value reads park and blocks it — a typo must never land a red. The
# branch's own copy says something else each time, so a reader of the pushed tree is graded too.
build_ir_fixture ac3d 'INHERITED_RED_MAX_AGE=2\n' || bad "IR TOOL-dUnstuckLanding-16 AC3 could not build its fixture"
printf 'INHERITED_RED=park\nINHERITED_RED_MAX_AGE=2\nGOV_KITROOT=%s\n' "$KIT_REL" > .githooks/gate-env.sh
git add -A >/dev/null 2>&1; git commit -q -m "the branch declares park in its own copy" >/dev/null 2>&1
_o=$(run_ir_push IR_AGE=aged)
case "$_o" in
  *"inherited-red policy at ${IR_R:0:8} reads land — no INHERITED_RED is declared in .githooks/gate-env.sh there, so the kit default land applies"*"red on inherited legs only — landing under INHERITED_RED=land: x"*"rc=0")
    ok "IR TOOL-dUnstuckLanding-16 AC3 an undeclared policy reads the kit default land and an aged inherited red lands" ;;
  *) bad "IR TOOL-dUnstuckLanding-16 AC3 an undeclared policy must read the kit default land and land, got: $_o" ;;
esac
case "$(cat "$ir_env" 2>/dev/null)" in
  "policy=land age=2 attr=${IR_R}") ok "IR TOOL-dUnstuckLanding-16 AC3 the kit default hands the runner land and the declared bound 2" ;;
  *) bad "IR TOOL-dUnstuckLanding-16 AC3 the kit default handed the runner: $(cat "$ir_env" 2>/dev/null)" ;;
esac
for _p in park lnad; do
  build_ir_fixture "ac3$_p" "INHERITED_RED=$_p\nINHERITED_RED_MAX_AGE=2\n" || bad "IR TOOL-dUnstuckLanding-16 AC3 could not build its fixture"
  printf 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=2\nGOV_KITROOT=%s\n' "$KIT_REL" > .githooks/gate-env.sh
  git add -A >/dev/null 2>&1; git commit -q -m "the branch grants itself land" >/dev/null 2>&1
  _o=$(run_ir_push IR_AGE=aged)
  case "$_o" in
    *"red on inherited legs only"*) bad "IR TOOL-dUnstuckLanding-16 AC3 INHERITED_RED=$_p at R landed an inherited red: $_o" ;;
    *"inherited-red policy at ${IR_R:0:8} reads park"*"rc=1") ok "IR TOOL-dUnstuckLanding-16 AC3 INHERITED_RED=$_p at R reads park and blocks the red" ;;
    *) bad "IR TOOL-dUnstuckLanding-16 AC3 INHERITED_RED=$_p at R must read park and block, got: $_o" ;;
  esac
done

# Closing review round 1 M12 (id 18), the hook's flipped branch: R carries NO .githooks/gate-env.sh,
# so the policy reads the kit default land, naming the absence, and an inherited-only red lands. The
# branch restores its own copy, which the hook sources and never reads a policy from. RED against a
# hook whose absent branch read park, staged in a scratch copy and restored.
build_ir_fixture m12 'INHERITED_RED_MAX_AGE=2\n' || bad "IR M12 could not build its fixture"
git rm -q .githooks/gate-env.sh >/dev/null 2>&1; git commit -q -m "R carries no gate-env" >/dev/null 2>&1
git push -q --no-verify origin main >/dev/null 2>&1; IR_R=$(git rev-parse HEAD)
mkdir -p .githooks; printf 'INHERITED_RED_MAX_AGE=2\nGOV_KITROOT=%s\n' "$KIT_REL" > .githooks/gate-env.sh
git add -A >/dev/null 2>&1; git commit -q -m "the branch restores its own copy" >/dev/null 2>&1
_o=$(run_ir_push)
case "$_o" in
  *"inherited-red policy at ${IR_R:0:8} reads land — .githooks/gate-env.sh is absent at ${IR_R:0:8}, so the kit default land applies"*"red on inherited legs only — landing under INHERITED_RED=land: x"*"rc=0")
    ok "IR M12 a gate-env absent at R reads the kit default land and an inherited red lands" ;;
  *) bad "IR M12 a gate-env absent at R must read the kit default land and land, got: $_o" ;;
esac

# AC4: an inherited green whose base IS the remote sha selects the scoped gate and names itself; once
# the remote moves past that base, the same stamp forces FULL.
build_ir_fixture ac4 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC4 could not build its fixture"
git commit -q --allow-empty -m c1 >/dev/null 2>&1
write_ir_stamp "$(git rev-parse HEAD)" "$IR_R" 10
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" bash -c 'git commit -q --allow-empty -m c2 && git push origin main' 2>&1 )
case "$_o" in
  *"scoped gate on main push"*"inherited green"*"at base ${IR_R:0:8}"*) ok "IR AC4 an inherited green at the remote sha scopes the gate" ;;
  *) bad "IR AC4 expected a scoped gate naming the inherited green, got: $_o" ;;
esac
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" bash -c 'git commit -q --allow-empty -m c3 && git push origin main' 2>&1 )
case "$_o" in
  *"FULL gate on main push"*"the inherited green was earned against base ${IR_R:0:8}"*) ok "IR AC4 a moved remote sha forces FULL past the inherited green" ;;
  *) bad "IR AC4 expected FULL naming the stale base, got: $_o" ;;
esac

# AC14: a stamp written under max_age 50 while the bound at R is 10 forces FULL, naming both.
build_ir_fixture ac14 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC14 could not build its fixture"
write_ir_stamp "$(git rev-parse HEAD)" "$IR_R" 50
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" bash -c 'git commit -q --allow-empty -m c && git push origin main' 2>&1 )
case "$_o" in
  *"FULL gate on main push"*"written under max_age 50 and the bound at ${IR_R:0:8} is 10"*) ok "IR AC14 a stamp's wider window is not trusted" ;;
  *) bad "IR AC14 expected FULL naming both bounds, got: $_o" ;;
esac

# AC16: a STALE full green that predicate 2 refuses does not hide a usable inherited green.
build_ir_fixture ac16 'INHERITED_RED=land\nINHERITED_RED_MAX_AGE=10\n' || bad "IR AC16 could not build its fixture"
git checkout -q -b elsewhere; git commit -q --allow-empty -m off >/dev/null 2>&1; _off=$(git rev-parse HEAD); git checkout -q main
printf 'sha\t%s\nfingerprint\t\nmanifest_blob\t\nrun_id\ttest\n' "$_off" > "$(git rev-parse --git-dir)/gate-full-green"
write_ir_stamp "$(git rev-parse HEAD)" "$IR_R" 10
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" bash -c 'git commit -q --allow-empty -m c && git push origin main' 2>&1 )
case "$_o" in
  *"scoped gate on main push"*"inherited green"*"is not an ancestor of the pushed tip"*) ok "IR AC16 a stale full green still reaches the inherited green" ;;
  *) bad "IR AC16 expected a scoped gate over a stale full green, got: $_o" ;;
esac

# AC11, the hook's half: its own reader, sliced out of the SHIPPED hook, run over this repository at
# HEAD, resolves the policy THIS repository declares. ADOPTER-CORRECT (TOOL-aClassedKnob-1): the
# expectation is derived, never gov's own `land 10`, because an adopter may declare park. The oracle is
# the shell's own reading, the committed gate-env.sh SOURCED in a subshell as KIT_REL is above, mapped
# through the kit contract the hook states: an absent file or a blank key reads land, a value outside
# `park land` reads park, and a bound that is not a positive integer reads none. A declaration the
# hook's line reader and the shell read differently reds here, naming both.
_ir_fns=$(awk '/^read_policy_key\(\)/,/^}/; /^read_policy_at\(\)/,/^}/' "$SRC/.githooks/pre-push")
read_ir_policy() { # <repo> <sha> -> "<policy> <bound>" as the sliced hook reader resolves it
  ( cd "$1" && _gate_env_rel=".githooks/gate-env.sh" && def=main && eval "$_ir_fns" \
    && read_policy_at "$2" && printf '%s %s' "$PP_POLICY" "$PP_MAX_AGE" )
}
_ir_want=$( cd "$SRC" || exit 1
  if _b=$(git show HEAD:.githooks/gate-env.sh 2>/dev/null); then
    unset INHERITED_RED INHERITED_RED_MAX_AGE
    eval "$_b" >/dev/null 2>&1
    _p=${INHERITED_RED:-}; _a=${INHERITED_RED_MAX_AGE:-}
  else _p=""; _a=""; fi
  case "$_p" in ''|land) _p=land ;; park) ;; *) _p=park ;; esac
  case "$_a" in ''|0*|*[!0-9]*) _a="" ;; esac
  printf '%s %s' "$_p" "$_a" )
_o=$(read_ir_policy "$SRC" "$(cd "$SRC" && git rev-parse HEAD)")
if [ -n "${_ir_want% }" ] && [ "$_o" = "$_ir_want" ]; then
  ok "IR AC11 this repository at HEAD reads the policy its own gate-env.sh declares: '$_o'"
else
  bad "IR AC11 this repository at HEAD read '${_o:-<nothing>}', its committed gate-env.sh declares '$_ir_want'"
fi
# AC11, the reader's failing case: two fixture commits gov's own values cannot satisfy, one declaring
# park with a bound of 7 and one with no gate-env.sh at all, which reads the kit default land, unbounded.
_d="$tmp/ir-ac11-reader"; mkdir -p "$_d/.githooks"
( cd "$_d" && git init -q && git config user.email t@example.com && git config user.name t \
  && printf 'INHERITED_RED=park\nINHERITED_RED_MAX_AGE=7\n' > .githooks/gate-env.sh \
  && git add .githooks/gate-env.sh && git commit -q -m park7 \
  && git rm -q .githooks/gate-env.sh && git commit -q -m absent ) >/dev/null 2>&1
_o1=$(read_ir_policy "$_d" "$(git -C "$_d" rev-parse HEAD~1 2>/dev/null)")
_o2=$(read_ir_policy "$_d" "$(git -C "$_d" rev-parse HEAD 2>/dev/null)")
if [ "$_o1" = "park 7" ] && [ "$_o2" = "land " ]; then
  ok "IR AC11 the hook's reader reads park 7 where it is declared, and land unbounded where gate-env.sh is absent"
else
  bad "IR AC11 the hook's reader read '${_o1:-<nothing>}' for park 7 and '${_o2:-<nothing>}' for an absent gate-env.sh"
fi

cd "$pfx_home" || exit 2

# ---- TOOL-dDerivedDocket-26: AN EXIT 0 IS NOT A VERDICT UNTIL THE RUN RECORD SAYS SO ------------------
# A STUB RUNNER at the hook's DEFAULT command, TRACKED at the runner's own path, so the hook takes it
# for the runner whether GOV_GATE_CMD is unset or names it (F8, below); only the declared STUB and a
# declared GATE_CMD naming another script go unchecked. It exits 0 in every mode; the variable is
# what it writes into the run record of the id the hook pinned. The GREEN mode is the control:
# without it a hook that blocked every push would pass the two arms that expect a block.
build_vr_fixture() { # tag -> a pushed main whose tree carries the stub runner; cwd moves into its work tree
  local d="$tmp/vr-$1"
  mkdir -p "$d/hooks"; cp "$SRC/.githooks/pre-push" "$d/hooks/pre-push"
  git init -q --bare "$d/remote.git"; git init -q "$d/work"
  cd "$d/work" || return 1
  git config user.email t@example.com; git config user.name t
  git config core.hooksPath "$d/hooks"
  mkdir -p "$KIT_REL/$RUN_GATES" .githooks
  # The rung the hook reads the kit root from when no receipt and no root install name it.
  printf 'GOV_KITROOT=%s\n' "$KIT_REL" > .githooks/gate-env.sh
  printf '%s\n' '[{"name":"x","argv":["bash","a.sh"]}]' > "$KIT_REL/gate-legs.json"
  cat > "$KIT_REL/$RUN_GATES/run-gates.sh" <<'VRSTUB'
#!/usr/bin/env bash
[ -n "${VR_IDS:-}" ] && printf '%s\n' "$GATE_RUN_ID" >> "$VR_IDS"
d="$(git rev-parse --git-dir)/gate-run/$GATE_RUN_ID"
case "${VR_MODE:-none}" in
  green) mkdir -p "$d" && printf 'verdict\tGREEN\n' > "$d/verdict" ;;
  red)   mkdir -p "$d" && printf 'verdict\tRED\n' > "$d/verdict" ;;
esac
exit 0
VRSTUB
  git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
  git remote add origin "$d/remote.git"
  touch "$(git rev-parse --git-dir)/push-main-active"
  GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1
}
run_vr_push() { # [env assignments…] -> VR_OUT and VR_RC, the push's merged output and its status
  git commit -q --allow-empty -m "vr $RANDOM" >/dev/null 2>&1
  VR_OUT=$( env -u GOV_GATE_CMD -u GATE_RUN_ID GATE_SELFTESTS= "$@" git push origin main 2>&1 ); VR_RC=$?
}
build_vr_fixture ac5 || bad "VR could not build its fixture"
# AC5, the hook's half: a runner that exits 0 and writes NO record is blocked — the
# TOOL-aSurfacedLexicon-25 shape, where the status alone let a push through with no bar run.
run_vr_push VR_MODE=none
case "$VR_RC|$VR_OUT" in
  1*"left no verdict in its run record"*) ok "VR AC5 an exit 0 with no run record is blocked, naming the missing verdict" ;;
  *) bad "VR AC5 an exit 0 with no run record must block, got rc $VR_RC: $VR_OUT" ;;
esac
git reset -q --hard origin/main
run_vr_push VR_MODE=red
case "$VR_RC|$VR_OUT" in
  1*"reads verdict 'RED', not GREEN"*) ok "VR AC5 an exit 0 over a RED record is blocked" ;;
  *) bad "VR AC5 an exit 0 over a RED record must block, got rc $VR_RC: $VR_OUT" ;;
esac
git reset -q --hard origin/main
run_vr_push VR_MODE=green
[ "$VR_RC" = 0 ] && ok "VR control: an exit 0 over its own GREEN record lands" \
  || bad "VR control: an exit 0 over its own GREEN record must land, got rc $VR_RC: $VR_OUT"
# AC15: an inherited GATE_RUN_ID naming a pre-planted GREEN record buys nothing, because the hook pins
# and clears its OWN id; and two consecutive pushes pin two different ids.
_vgd=$(git rev-parse --git-dir)
mkdir -p "$_vgd/gate-run/planted"; printf 'verdict\tGREEN\n' > "$_vgd/gate-run/planted/verdict"
run_vr_push VR_MODE=none GATE_RUN_ID=planted
[ "$VR_RC" = 1 ] && ok "VR AC15 an inherited id naming a planted GREEN record is not honoured" \
  || bad "VR AC15 a planted GREEN record under an inherited id satisfied the boundary: rc $VR_RC: $VR_OUT"
git reset -q --hard origin/main
: > "$tmp/vr-ids"
run_vr_push VR_MODE=green VR_IDS="$tmp/vr-ids"; run_vr_push VR_MODE=green VR_IDS="$tmp/vr-ids"
case "$(sort -u "$tmp/vr-ids" | grep -c .)|$(grep -c '^planted$' "$tmp/vr-ids")" in
  "2|0") ok "VR AC15 two pushes pin two different ids, neither the inherited one" ;;
  *) bad "VR AC15 the stub runner saw these ids: $(tr '\n' ' ' < "$tmp/vr-ids")" ;;
esac
# S6's announcement: the declared STUB is not the runner and writes no record, so it is not checked.
git commit -q --allow-empty -m "vr override" >/dev/null 2>&1
_o=$( GATE_SELFTESTS= GOV_GATE_CMD="bash $green" git push origin main 2>&1 ); _r=$?
case "$_r|$_o" in
  0*"STUB"*"its run record is not checked for an override command"*) ok "VR a STUB override lands and the skipped record check is announced" ;;
  *) bad "VR a STUB override must land with the skip announced, got rc $_r: $_o" ;;
esac
# F8 (closing diff review round 1): THE KNOB DOES NOT SWITCH S6 OFF. GOV_GATE_CMD naming the runner
# itself, with no test escape, vets as `tracked` and earns the lander marker, so the record check has
# to run for it exactly as for the default command. The stub runner above exits 0 and writes no record.
git reset -q --hard origin/main
run_vr_push VR_MODE=none GOV_GATE_CMD_TEST= GOV_GATE_CMD="bash $KIT_REL/$RUN_GATES/run-gates.sh"
case "$VR_RC|$VR_OUT" in
  1*"left no verdict in its run record"*) ok "VR F8 GOV_GATE_CMD naming the runner is still held to its run record: an exit 0 with none is blocked" ;;
  *) bad "VR F8 GOV_GATE_CMD naming the runner switched the record check off, got rc $VR_RC: $VR_OUT" ;;
esac
# ITS CONTROL: the same override over the runner's own GREEN record lands, so the arm above is the
# record check and not a refusal of the override itself.
git reset -q --hard origin/main
run_vr_push VR_MODE=green GOV_GATE_CMD_TEST= GOV_GATE_CMD="bash $KIT_REL/$RUN_GATES/run-gates.sh"
[ "$VR_RC" = 0 ] && ok "VR F8 control: GOV_GATE_CMD naming the runner lands over the runner's own GREEN record" \
  || bad "VR F8 control: GOV_GATE_CMD naming the runner must land over a GREEN record, got rc $VR_RC: $VR_OUT"
# AND THE ONE SANCTIONED SKIP: a declared GATE_CMD naming ANOTHER tracked script writes no record this
# hook can read, so the check is skipped for it and the skip is announced, naming the script.
printf '#!/usr/bin/env bash\nexit 0\n' > other-bar.sh
printf 'GATE_CMD="bash other-bar.sh"\n' > .unattended.conf
git add other-bar.sh .unattended.conf >/dev/null 2>&1; git commit -q -m "declare another bar" >/dev/null 2>&1
_o=$( env -u GATE_RUN_ID GATE_SELFTESTS= GOV_GATE_CMD_TEST= GOV_GATE_CMD="bash other-bar.sh" git push origin main 2>&1 ); _r=$?
case "$_r|$_o" in
  0*"runs the declared GATE_CMD 'other-bar.sh', not this kit's runner"*"not checked"*) ok "VR F8 a declared GATE_CMD naming another script lands, its record skip announced by name" ;;
  *) bad "VR F8 a declared GATE_CMD naming another script must land with its skip announced, got rc $_r: $_o" ;;
esac
cd "$pfx_home" || exit 2

# THE CLASS (TOOL-aRepatriatedFork-49 S5): every GATE_/GOV_ name the runner reads through `$` is in
# exactly one set — the names the hook clears before gate-env.sh runs, the names it clears before a
# non-stub bar, or the inert set below, each of which the runner's own invariant keeps from turning a
# leg into a PASS or a SKIP. A new knob reds here until someone decides which it is.
#   GATE_BASE GATE_FULL GATE_RUN_ID — the hook sets each on the path where it matters; an inherited
#     GATE_FULL only widens the run, and GATE_FULL=1 makes GATE_BASE irrelevant.
#   GATE_SELFTESTS — adds legs, and predicate 8 forces a full bar for it.
#   the rest — width, timeouts, the wall, the turnstile, reaping and the run log: a breach is RED.
#   GATE_ATTRIBUTE GATE_INHERITED_RED GATE_INHERITED_RED_MAX_AGE — the hook clears the policy pair
#     and sets all three from R itself (TOOL-dDerivedDocket-23, -24), and attribution is report-only.
#   GATE_AMBIENT_TMP GATE_HOST_RATIO — assigned in the runner, from TMPDIR and as a source constant.
#   GATE_DOCS_BASE — the hook clears it for every bar, a STUB included, and sets it only on a doc-only
#     decision (TOOL-dThriftyLanding-3), as it sets GATE_BASE on the path where that matters.
#   GATE_MEMPAUSE GATE_MEMPAUSE_HOLD GATE_MEMINFO — the memory pause's threshold, its hold bound and the
#     reading it takes, GATE_CGROUP_ROOT's sibling: a hold narrows the pool and always ends, and an
#     unreadable host makes it INERT (TOOL-aGraftedHelix-7). Width class.
#   GATE_CENSUS_EVERY — the foreign-load census period; the census writes evidence into each `.leg`
#     row and decides no verdict (TOOL-aGraftedHelix-5). Classified by TOOL-aClassedKnob-1.
#   GOV_REMOTE GOV_DEFAULT_BRANCH — read by the runner's inlined remote ladder for the scope base
#     only (TOOL-dLadderedRemote-2), and the hook sets GATE_BASE or GATE_FULL=1 on every path, either
#     of which outranks that base. The runner takes the OBSERVED branch, so GOV_DEFAULT_BRANCH selects
#     nothing there even when it is read (TOOL-dLadderedRemote-5).
#   GATE_TURNSTILE_DIR — where the host beacon and queue live; it decides contention only, as GATE_TURNSTILE=0 does (TOOL-aFrugalTurnstile-5 F1).
#   GATE_TURNSTILE_HOLDER — a holder's nonce; scrubbing it would queue a pushing leg behind its own parent bar (TOOL-aFrugalTurnstile-5 F1).
BAR_INERT_KNOBS="GOV_REMOTE GOV_DEFAULT_BRANCH GATE_AMBIENT_TMP GATE_DOCS_BASE GATE_ATTRIBUTE GATE_HOST_RATIO GATE_INHERITED_RED GATE_INHERITED_RED_MAX_AGE GATE_BASE GATE_CENSUS_EVERY GATE_CGROUP_ROOT GATE_CORES GATE_FULL GATE_JOBS GATE_MEMINFO GATE_MEMPAUSE GATE_MEMPAUSE_HOLD GATE_PROFILE GATE_PROFILES GATE_RAM_MB GATE_REAP_BOUND GATE_RUN_ID GATE_RUN_KEEP GATE_SELFTESTS GATE_TURNSTILE GATE_TURNSTILE_DIR GATE_TURNSTILE_HELD GATE_TURNSTILE_HOLDER GATE_TURNSTILE_TICK GATE_TURNSTILE_TTL GATE_WALL GOV_RUNLOG"
read_hook_const() { sed -n 's/^'"$1"'="\(.*\)"$/\1/p' "$SRC/.githooks/pre-push"; }
check_knob_classes() { # <runner file> -> one line per unclassified, doubly classified or stale name; empty when clean
  local knobs cleared scrubbed k n
  knobs=" $(grep -oE '\$\{?(GATE|GOV)_[A-Z0-9_]+' "$1" | sed -E 's/^\$\{?//' | sort -u | tr '\n' ' ')"
  cleared=$(read_hook_const ENV_DROPPED_KNOBS); scrubbed=$(read_hook_const BAR_SCRUBBED_KNOBS)
  for k in $knobs; do
    n=0
    for s in "$cleared" "$scrubbed" "$BAR_INERT_KNOBS"; do case " $s " in *" $k "*) n=$((n + 1)) ;; esac; done
    [ "$n" = 1 ] || echo "unclassified-or-twice $k ($n)"
  done
  for k in $scrubbed $BAR_INERT_KNOBS; do case "$knobs " in *" $k "*) ;; *) echo "stale $k" ;; esac; done
}
h49_n=$(grep -oE '\$\{?(GATE|GOV)_[A-Z0-9_]+' "$SRC/$RUN_GATES_DIR/run-gates.sh" | sed -E 's/^\$\{?//' | sort -u | grep -c .)
_cls=$(check_knob_classes "$SRC/$RUN_GATES_DIR/run-gates.sh")
if [ -z "$_cls" ] && [ "$h49_n" -ge 10 ] && grep -qE '\$\{?GATE_LEGS' "$SRC/$RUN_GATES_DIR/run-gates.sh"; then
  ok "H49 class — every one of the runner's $h49_n GATE_/GOV_ knobs is classified exactly once"
else
  bad "H49 class — the runner's knobs ($h49_n) are not each classified exactly once: $(printf '%s' "$_cls" | tr '\n' ';')"
fi
{ cat "$SRC/$RUN_GATES_DIR/run-gates.sh"; printf ': "${GATE_PLANTED:-}"\n'; } > "$tmp/h49-runner-planted.sh"
case "$(check_knob_classes "$tmp/h49-runner-planted.sh")" in
  *"unclassified-or-twice GATE_PLANTED"*) ok "H49 class — a runner knob nobody classified reds by name" ;;
  *) bad "H49 class — an unclassified GATE_PLANTED in a runner copy went unreported" ;;
esac
sed 's/GATE_LEGS/GATE_XLEGS/g' "$SRC/$RUN_GATES_DIR/run-gates.sh" > "$tmp/h49-runner-nolegs.sh"
case "$(check_knob_classes "$tmp/h49-runner-nolegs.sh")" in
  *"stale GATE_LEGS"*) ok "H49 class — a cleared name the runner no longer reads reds as stale" ;;
  *) bad "H49 class — a stale GATE_LEGS member went unreported" ;;
esac

# ============================================================================================
# TOOL-aRepatriatedFork-8 — THE CONTRACTS adopter ic's OWN HOOK CARRIED. A fresh fixture whose ONLY
# remote is named `mirror`, not `origin`, as on adopter ic's node `d`, with its HEAD set and NO GOV_DEFAULT_BRANCH, so
# every arm below also proves S1: the pre-S1 hook read `origin/HEAD` and refused each of these
# pushes with "can't determine the default branch" before any of them reached what it grades.
fx8="$tmp/fx8"
mkdir -p "$fx8"
git init -q --bare "$fx8/mirror.git"
git init -q "$fx8/work"
cd "$fx8/work" || exit 2
git config user.email t@example.com; git config user.name t
git config core.hooksPath "$tmp/hooks"
git commit -q --allow-empty -m init; git branch -M main
git remote add mirror "$fx8/mirror.git"
git push -q --no-verify mirror main
git -C "$fx8/mirror.git" symbolic-ref HEAD refs/heads/main
git remote set-head mirror main >/dev/null 2>&1
read_token() { cut -f1 "$(git rev-parse --git-dir)/pre-push-refusal" 2>/dev/null; }
read_tip() { git -C "$fx8/mirror.git" rev-parse -q --verify "refs/heads/${1:-main}" 2>/dev/null; }

# AC3 — a raw push is refused by the lander-marker rule, NOT the default-branch lookup, and leaves
#       the machine token the lander reads.
git commit -q --allow-empty -m r8
msg=$( ( unset GOV_DEFAULT_BRANCH; git push -q mirror main 2>&1 ) )
case "$msg|$(read_token)" in
  *"refusing a raw push"*"|raw-push") ok "AC3 a raw push to a remote named mirror is refused as raw-push, with its token" ;;
  *) bad "AC3 expected the raw-push refusal and token, got: ${msg:-<push SUCCEEDED>} | token '$(read_token)'" ;;
esac
touch "$(git rev-parse --git-dir)/push-main-active"

# AC2 — the same remote, a RED bar: refused AT THE BAR, and the token says the bar ran.
before=$(read_tip)
msg=$( ( unset GOV_DEFAULT_BRANCH; GOV_GATE_CMD="bash $red" git push -q mirror main 2>&1 ) )
case "$msg|$(read_token)" in
  *"gate RED"*"|gate-red") [ "$(read_tip)" = "$before" ] && ok "AC2 a remote named mirror reaches the bar, which refuses as gate-red" \
                            || bad "AC2 the remote moved over a red bar" ;;
  *) bad "AC2 expected the bar to run and refuse, got: ${msg:-<push SUCCEEDED>} | token '$(read_token)'" ;;
esac

# AC9 — the bar is handed the pushed range from git's own ref line, never from the environment.
pb="$tmp/pushbase.sh"; printf '#!/usr/bin/env bash\necho "PUSH_BASE=[$GATE_PUSH_BASE]"\nexit 0\n' > "$pb"
before=$(read_tip)
msg=$( ( unset GOV_DEFAULT_BRANCH; GATE_PUSH_BASE=inherited GOV_GATE_CMD="bash $pb" git push -q mirror main 2>&1 ) )
case "$msg" in
  *"PUSH_BASE=[$before]"*) ok "AC9 GATE_PUSH_BASE is the remote's pre-push sha, and an inherited value is overwritten" ;;
  *) bad "AC9 expected PUSH_BASE=[$before], got: ${msg:-<nothing>}" ;;
esac

# AC8 — a bar that COMMITS while it runs and exits green: the green describes a tree git is no
#       longer pushing, so the hook refuses as head-moved and the remote stays put.
mv8="$tmp/moves-head.sh"; printf '#!/usr/bin/env bash\ngit commit -q --allow-empty -m moved-by-the-bar\nexit 0\n' > "$mv8"
git commit -q --allow-empty -m c8m
before=$(read_tip)
msg=$( ( unset GOV_DEFAULT_BRANCH; GOV_GATE_CMD="bash $mv8" git push -q mirror main 2>&1 ) )
case "$msg|$(read_token)" in
  *"HEAD moved"*"|head-moved") [ "$(read_tip)" = "$before" ] && ok "AC8 a HEAD moved by the bar is refused as head-moved" \
                               || bad "AC8 the remote moved although HEAD moved under the bar" ;;
  *) bad "AC8 expected the head-moved refusal, got: ${msg:-<push SUCCEEDED>} | token '$(read_token)'" ;;
esac

# AC6 — an untracked superproject file is dirt: the bar would certify a file the push does not carry.
echo 'x = 1' > brand_new_module.py
msg=$( ( unset GOV_DEFAULT_BRANCH; GOV_GATE_CMD="bash $green" git push -q mirror main 2>&1 ) )
case "$msg|$(read_token)" in
  *"working tree is dirty"*"brand_new_module.py"*"|dirty-tree") ok "AC6 an untracked file refuses the push as dirty-tree, naming it" ;;
  *) bad "AC6 expected the dirty-tree refusal, got: ${msg:-<push SUCCEEDED>} | token '$(read_token)'" ;;
esac
rm -f brand_new_module.py
# ITS CONTROL, which is also AC3's other half: the clean tree lands, and leaves no token behind.
if ( unset GOV_DEFAULT_BRANCH; GOV_GATE_CMD="bash $green" git push -q mirror main >/dev/null 2>&1 ) \
   && [ -z "$(read_token)" ]; then
  ok "AC6 control — the same push from a clean tree lands, and no stale token survives it"
else
  bad "AC6 control — a clean push did not land, or left token '$(read_token)'"
fi

# AC10 — THE BRANCH BAR (S5). Declared in gate-env.sh it gates a feature push; naming an untracked
#        script it is refused as bar-refused; undeclared the push is ungated. The escape is unset in
#        each arm, since it would let an untracked bar through. gate-env.sh is COMMITTED in each arm,
#        since the hook refuses to source an untracked one (closing review round 1 H1).
git checkout -q -b feat8
printf '#!/usr/bin/env bash\necho "BRANCH BAR RED"\nexit 1\n' > branch-red.sh
git add branch-red.sh; git commit -q -m "a tracked branch bar"
mkdir -p .githooks
printf 'GOV_BRANCH_GATE_CMD="bash branch-red.sh"\n' > .githooks/gate-env.sh
git add .githooks/gate-env.sh; git commit -q -m "declare the branch bar"
msg=$( ( unset GOV_DEFAULT_BRANCH GOV_GATE_CMD_TEST; git push -q mirror feat8 2>&1 ) )
case "$msg|$(read_token)|$(read_tip feat8)" in
  *"BRANCH BAR RED"*"|gate-red|") ok "AC10 a declared, tracked, red branch bar refuses a feature push" ;;
  *) bad "AC10 expected the branch bar to run and refuse, got: ${msg:-<push SUCCEEDED>} | token '$(read_token)'" ;;
esac
printf 'GOV_BRANCH_GATE_CMD="bash %s"\n' "$red" > .githooks/gate-env.sh
git add .githooks/gate-env.sh; git commit -q -m "declare an untracked branch bar"
msg=$( ( unset GOV_DEFAULT_BRANCH GOV_GATE_CMD_TEST; git push -q mirror feat8 2>&1 ) )
case "$msg|$(read_token)" in
  *"does not track"*"|bar-refused") ok "AC10 an untracked branch bar is refused as bar-refused" ;;
  *) bad "AC10 expected an untracked branch bar to be refused, got: ${msg:-<push SUCCEEDED>} | token '$(read_token)'" ;;
esac
# H1 — the policy file itself, UNTRACKED: refused before it is sourced, whatever it declares.
git rm -q .githooks/gate-env.sh; git commit -q -m "undeclare the branch bar"
mkdir -p .githooks   # `git rm` took the emptied directory with it
printf 'GOV_BRANCH_GATE_CMD="bash branch-red.sh"\n' > .githooks/gate-env.sh
msg=$( ( unset GOV_DEFAULT_BRANCH GOV_GATE_CMD_TEST; git push -q mirror feat8 2>&1 ) )
case "$msg|$(read_token)|$(read_tip feat8)" in
  *"gate-env.sh is sourced into this hook"*"|bar-refused|") ok "H1 an untracked gate-env.sh is refused as bar-refused, unsourced" ;;
  *) bad "H1 expected an untracked gate-env.sh to be refused, got: ${msg:-<push SUCCEEDED>} | token '$(read_token)'" ;;
esac
rm -f .githooks/gate-env.sh
if ( unset GOV_DEFAULT_BRANCH GOV_GATE_CMD_TEST; git push -q mirror feat8 >/dev/null 2>&1 ) && [ -n "$(read_tip feat8)" ]; then
  ok "AC10 control — with no branch bar declared, the feature push is ungated"
else
  bad "AC10 control — an undeclared branch bar still gated a feature push"
fi
cd "$pfx_home" || exit 2

# ---- TOOL-aMendedFleet-3: A MERGE THAT LOSES A DEFINITION, refused on the default branch -----------
# A fixture whose sideB adds `fb` and whose main merges sideB resolving the conflict to main's side,
# which is merge `01c22e155`'s shape. The lexicon kit is copied to the fixture's root under the name
# its directory has here, committed with a `.lexicon.conf` arming shell, so the hook finds it from
# the pushing tree. Observed RED against the base hook: the token was `raw-push` and nothing named
# the loss. AC7 is the control: the same merge carrying a valid `superseded:` line passes this block
# and reaches the later raw-push refusal.
if _ml_lex=$(resolve_kit_dir "$_rkd_py" lexicon lexicon.py "$SRC/$KIT_REL" 2>/dev/null); then
  _ml_home=${_ml_lex##*/}
  git init -q --bare "$tmp/ml.git"
  git init -q "$tmp/ml"
  cd "$tmp/ml" || exit 2
  git config user.email t@example.com; git config user.name t; git config core.autocrlf false
  git config core.hooksPath "$tmp/hooks"
  cp -r "$SRC/$_ml_lex" "$_ml_home"; rm -rf "$_ml_home/__pycache__"
  printf 'LANGS="sh:shell-tokens:parser"\n' > .lexicon.conf
  printf '__pycache__/\n' > .gitignore
  printf 'fa() { :; }\n' > a.sh
  git add -A; git commit -q -m base; git branch -M main
  git remote add origin "$tmp/ml.git"; git push -q --no-verify origin main
  git -C "$tmp/ml.git" symbolic-ref HEAD refs/heads/main
  git checkout -q -b sideB
  printf 'fa() { echo B; }\nfb() { :; }\n' > a.sh; git commit -q -am "side B"
  git checkout -q main
  printf 'fa() { echo A; }\n' > a.sh; git commit -q -am "side A"
  git merge -q --no-ff --no-commit sideB >/dev/null 2>&1
  printf 'fa() { echo A; }\n' > a.sh; git add a.sh; git commit -q -m "merge sideB, taking side A"
  before=$(git -C "$tmp/ml.git" rev-parse main)
  msg=$(git push origin main 2>&1)
  case "$msg|$(read_token)" in
    *"a.sh: fb"*"|merge-loss") [ "$(git -C "$tmp/ml.git" rev-parse main)" = "$before" ] \
        && ok "AMF3 AC6 a raw push of a merge losing fb is refused as merge-loss, naming it, remote unmoved" \
        || bad "AMF3 AC6 the remote moved over a merge-loss refusal" ;;
    *) bad "AMF3 AC6 expected the merge-loss refusal, got: ${msg:-<push SUCCEEDED>} | token '$(read_token)'" ;;
  esac
  git commit -q --amend -m "merge sideB, taking side A

superseded: fb -> fa"
  msg=$(git push origin main 2>&1)
  case "$(read_token)" in
    merge-loss|"") bad "AMF3 AC7 a superseded merge should pass the merge-loss block, got: ${msg:-<push SUCCEEDED>} | token '$(read_token)'" ;;
    *) ok "AMF3 AC7 a merge carrying a valid superseded: line reaches the later '$(read_token)' refusal" ;;
  esac
  cd "$pfx_home" || exit 2
else
  bad "AMF3 the lexicon kit does not resolve beside this hook's kit root, so the merge-loss arms did not run"
fi
# ---- TOOL-dThriftyLanding-3: A DOC-ONLY PUSH, CLASSIFIED AGAINST THE DOC CLASS AT R ---------------
# A scratch repo whose gate-env file at R declares `GATE_DOC_PATHS`, a stub bar that records the docs
# base it was handed, and a record stamped at R so the decision is scoped unless a predicate forces.
# Each arm grades the DECISION LINE and what reached the bar, against the declaration at R.
docs_env="$tmp/docs-env.txt"
docstub="$tmp/docstub.sh"
printf '#!/usr/bin/env bash\nprintf "docs=%%s\\n" "${GATE_DOCS_BASE:-}" > "$DOCS_ENV"\nexit 0\n' > "$docstub"
build_docs_fixture() { # tag · gate-env body (printf %b) -> a pushed main at R carrying that body
  local d="$tmp/docs-$1"
  mkdir -p "$d/hooks"; cp "$SRC/.githooks/pre-push" "$d/hooks/pre-push"
  git init -q --bare "$d/remote.git"; git init -q "$d/work"
  cd "$d/work" || return 1
  git config user.email t@example.com; git config user.name t; git config core.autocrlf false
  git config core.hooksPath "$d/hooks"
  mkdir -p .githooks "$KIT_REL" notes src
  printf '%s\n' '[{"name":"x","argv":["bash","a.sh"]}]' > "$KIT_REL/gate-legs.json"
  printf '%b' "$2" > .githooks/gate-env.sh
  printf 'GOV_KITROOT=%s\n' "$KIT_REL" >> .githooks/gate-env.sh
  printf 'a\n' > notes/a.md; printf 'b\n' > notes/b.md; printf 'x\n' > src/x.sh
  git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
  git remote add origin "$d/remote.git"
  touch "$(git rev-parse --git-dir)/push-main-active"
  GOV_GATE_CMD="bash $green" git push -q origin main >/dev/null 2>&1
}
set_docs_stamp() { # a full green naming the remote tip, which the arms then push past
  printf 'sha\t%s\nfingerprint\t\nmanifest_blob\t\nrun_id\ttest\n' \
    "$(git ls-remote origin refs/heads/main | cut -f1)" > "$(git rev-parse --git-dir)/gate-full-green"
}
run_docs_push() { # [env…] -> the push's merged output, then the docs base the bar received
  rm -f "$docs_env"
  local o; o=$( env GATE_SELFTESTS= DOCS_ENV="$docs_env" GOV_GATE_CMD="bash $docstub" "$@" git push origin main 2>&1 )
  printf '%s\n%s\n' "$o" "$(cat "$docs_env" 2>/dev/null || echo 'docs=<bar did not run>')"
}
read_docs_tip() { git ls-remote origin refs/heads/main | cut -f1; }

build_docs_fixture ac1 'GATE_DOC_PATHS="notes/"\n' || bad "DOCS AC1 could not build its fixture"
_r=$(read_docs_tip); set_docs_stamp
printf 'a2\n' > notes/a.md; git commit -qam "doc edit"
_o=$(run_docs_push)
case "$_o" in
  *"scoped gate on main push"*"docs-only: 1 path(s) in GATE_DOC_PATHS at ${_r:0:8}"*"docs=$_r"*) ok "DOCS AC1 a doc-only push is named docs-only and the bar receives R as its docs base" ;;
  *) bad "DOCS AC1 expected a docs-only scoped decision and docs=$_r, got: $_o" ;;
esac
_r=$(read_docs_tip); set_docs_stamp
printf 'a3\n' > notes/a.md; printf 'x2\n' > src/x.sh; git commit -qam "mixed"
_o=$(run_docs_push)
case "$_o" in
  *"docs-only"*) bad "DOCS AC2 a push changing src/x.sh was classified doc-only: $_o" ;;
  *"scoped gate on main push"*"docs=") ok "DOCS AC2 a mixed push is not doc-only and receives no docs base" ;;
  *) bad "DOCS AC2 expected a plain scoped decision with no docs base, got: $_o" ;;
esac
_r=$(read_docs_tip); set_docs_stamp
printf 'y\n' > src/y.sh; git add src/y.sh; git commit -qm "add code"
git rm -q src/y.sh; printf 'a4\n' > notes/a.md; git commit -qam "remove it again"
_o=$(run_docs_push)
case "$_o" in
  *"docs-only"*) bad "DOCS AC3 a code file added and removed inside the range read as doc-only: $_o" ;;
  *"gate on main push"*) ok "DOCS AC3 a code touch inside the range keeps the push out of the doc class" ;;
  *) bad "DOCS AC3 no decision line: $_o" ;;
esac
# TOOL-dThriftyLanding-9: the same code touch on a SIDE branch merged with --no-ff. Git's default
# history simplification drops a side branch that nets to nothing, so the linear arm above cannot see it.
_r=$(read_docs_tip); set_docs_stamp
git checkout -q -b side9; printf 'z\n' > src/z.sh; git add src/z.sh; git commit -qm "side code"
git rm -q src/z.sh; printf 'b9\n' > notes/b.md; git commit -qam "side: remove it, edit a doc"
git checkout -q main; printf 'a9\n' > notes/a.md; git commit -qam "main doc"
git merge -q --no-ff -m "land side9" side9 >/dev/null 2>&1
_o=$(run_docs_push)
case "$_o" in
  *"docs-only"*) bad "DOCS U9 a code touch on a merged side branch read as doc-only: $_o" ;;
  *"gate on main push"*) ok "DOCS U9 a code touch on a merged side branch keeps the push out of the doc class" ;;
  *) bad "DOCS U9 no decision line: $_o" ;;
esac
# AC4: a doc-only MERGE whose second parent the record does not cover. Predicate 5 forces it at base.
_r=$(read_docs_tip); set_docs_stamp
git checkout -q -b side; printf 'b2\n' > notes/b.md; git commit -qam "side doc"
git checkout -q main; printf 'a5\n' > notes/a.md; git commit -qam "main doc"
git merge -q --no-ff -m "land side" side >/dev/null 2>&1
_o=$(run_docs_push)
case "$_o" in
  *"scoped gate on main push"*"docs-only"*) ok "DOCS AC4 a doc-only merge is not forced FULL by its second parent" ;;
  *) bad "DOCS AC4 expected a docs-only scoped decision over the merge, got: $_o" ;;
esac
# AC7: the lag bound still forces a doc-only push.
_r=$(read_docs_tip); set_docs_stamp
_lag=$(grep -m1 -oE 'GATE_FULL_MAX_LAG=[0-9]+' "$SRC/.githooks/pre-push" | grep -oE '[0-9]+')
for _i in $(seq 0 "${_lag:-10}"); do printf '%s\n' "$_i" > notes/a.md; git commit -qam "lag $_i"; done
_o=$(run_docs_push)
case "$_o" in
  *"FULL gate on main push"*"doc-only, but"*"first-parent landings behind"*) ok "DOCS AC7 the lag bound still forces FULL on a doc-only push, and says so" ;;
  *) bad "DOCS AC7 expected FULL with doc-only, but and the lag reason, got: $_o" ;;
esac
# AC8: an exported GATE_DOCS_BASE never reaches the bar of a push that is not doc-only.
_r=$(read_docs_tip); set_docs_stamp
printf 'x3\n' > src/x.sh; git commit -qam "code"
_o=$(run_docs_push GATE_DOCS_BASE="$_r")
case "$_o" in
  *"not honoured from the environment"*"GATE_DOCS_BASE"*"docs=") ok "DOCS AC8 an exported docs base is cleared and named, and the bar receives none" ;;
  *) bad "DOCS AC8 expected the knob cleared and named with no docs base at the bar, got: $_o" ;;
esac
# AC5: a class declared only in the pushed tree is not read.
build_docs_fixture ac5 '' || bad "DOCS AC5 could not build its fixture"
set_docs_stamp
printf 'GATE_DOC_PATHS="notes/ .githooks/"\nGOV_KITROOT=%s\n' "$KIT_REL" > .githooks/gate-env.sh
printf 'a2\n' > notes/a.md; git commit -qam "the branch declares its own doc class"
_o=$(run_docs_push)
case "$_o" in
  *"docs-only"*) bad "DOCS AC5 a doc class declared only in the pushed tree was honoured: $_o" ;;
  *"scoped gate on main push"*) ok "DOCS AC5 the doc class is read at R, never from the pushed tree" ;;
  *) bad "DOCS AC5 expected a plain scoped decision, got: $_o" ;;
esac
# AC6: a glob element invalidates the whole declaration, aloud.
build_docs_fixture ac6 'GATE_DOC_PATHS="notes/*"\n' || bad "DOCS AC6 could not build its fixture"
set_docs_stamp
printf 'a2\n' > notes/a.md; git commit -qam "doc edit"
_o=$(run_docs_push)
case "$_o" in
  *"docs-only"*) bad "DOCS AC6 a glob element was honoured: $_o" ;;
  *"not a plain repo path"*"gate on main push"*) ok "DOCS AC6 a glob element voids the doc class and the hook says so" ;;
  *) bad "DOCS AC6 expected the invalid-element notice, got: $_o" ;;
esac
# TOOL-dThriftyLanding-12, closing review M5: `.` excludes the whole tree, so it voids the class too.
build_docs_fixture dot 'GATE_DOC_PATHS="."\n' || bad "DOCS M5 could not build its fixture"
set_docs_stamp
printf 'x2\n' > src/x.sh; git commit -qam "code"
_o=$(run_docs_push)
case "$_o" in
  *"docs-only"*) bad "DOCS M5 a code push under GATE_DOC_PATHS=. was classified doc-only: $_o" ;;
  *"not a plain repo path"*"gate on main push"*) ok "DOCS M5 a '.' element voids the doc class and the hook says so" ;;
  *) bad "DOCS M5 expected the invalid-element notice, got: $_o" ;;
esac
# TOOL-dThriftyLanding-12, closing review M2: under INHERITED_RED=park at R a doc push is not scoped as
# doc-only, because the docs base may sit above an unproven record; the hook names the policy.
build_docs_fixture park 'GATE_DOC_PATHS="notes/"\nINHERITED_RED=park\n' || bad "DOCS M2 could not build its fixture"
set_docs_stamp
printf 'a2\n' > notes/a.md; git commit -qam "doc edit"
_o=$(run_docs_push)
case "$_o" in
  *"docs-only"*) bad "DOCS M2 a doc push under park was scoped as doc-only: $_o" ;;
  *"reads park, so it is not scoped as doc-only"*"gate on main push"*) ok "DOCS M2 under park a doc push keeps today's decision, and the hook names the policy" ;;
  *) bad "DOCS M2 expected the park notice, got: $_o" ;;
esac
# TOOL-dThriftyLanding-12, closing review L3: the inherited-green branch exports the docs base too.
build_docs_fixture inh 'GATE_DOC_PATHS="notes/"\n' || bad "DOCS L3a could not build its fixture"
_r=$(read_docs_tip)
rm -f "$(git rev-parse --git-dir)/gate-full-green"
write_ir_stamp "$_r" "$_r" ""
printf 'a2\n' > notes/a.md; git commit -qam "doc edit"
_o=$(run_docs_push)
case "$_o" in
  *"scoped gate on main push"*"docs-only"*"inherited green"*"docs=$_r") ok "DOCS L3a an inherited-green doc push is docs-only and hands the bar R" ;;
  *) bad "DOCS L3a expected an inherited-green docs-only decision and docs=$_r, got: $_o" ;;
esac
# ...and a LINKED worktree adopts the primary's own stamp, the common dir's gate-full-green.
build_docs_fixture wt 'GATE_DOC_PATHS="notes/"\n' || bad "DOCS L3b could not build its fixture"
_r=$(read_docs_tip); set_docs_stamp
_wt="$tmp/docs-wt-linked"
git worktree add -q "$_wt" -b wtb >/dev/null 2>&1
(
  cd "$_wt" || exit 1
  touch "$(git rev-parse --git-dir)/push-main-active"
  rm -f "$(git rev-parse --git-dir)/gate-full-green"
  printf 'a3\n' > notes/a.md; git commit -qam "doc edit from a linked worktree"
  rm -f "$docs_env"
  env GATE_SELFTESTS= DOCS_ENV="$docs_env" GOV_GATE_CMD="bash $docstub" git push origin HEAD:main 2>&1
) > "$tmp/docs-wt.out"
case "$(cat "$tmp/docs-wt.out")" in
  *"scoped gate on main push"*"from the common dir's gate-full-green "*) ok "DOCS L3b a linked worktree adopts the primary's stamp and names it" ;;
  *) bad "DOCS L3b expected the common dir's own stamp adopted, got: $(cat "$tmp/docs-wt.out")" ;;
esac
cd "$pfx_home" || exit 2

# ============================================================================================
# THE BAR'S OWN GREEN, BY TREE — TOOL-aFrugalTurnstile-2. A tracked stand-in runner at the kit path
# writes its run record and appends one line to a marker OUTSIDE the repo, so "the bar ran" is a line
# count and never an inference from output. The hook is driven directly with git's stdin line, and the
# remote moves by --no-verify pushes, so each arm names exactly the R and tip it grades. The declared
# STUB escape is lifted per push: a STUB never writes or reads a record, which AC4 grades.
build_bg_fixture() { # tag [gate-env lines] -> a work clone at main=R, pushed; cwd moves in; sets BG_D bg_gd BG_MARK
  BG_D="$tmp/bg-$1"; mkdir -p "$BG_D/hooks"; cp "$SRC/.githooks/pre-push" "$BG_D/hooks/pre-push"
  git init -q --bare "$BG_D/remote.git"; git init -q "$BG_D/w"; cd "$BG_D/w" || return 1
  git config user.email t@example.com; git config user.name t; git config core.autocrlf false
  git config core.hooksPath "$BG_D/hooks"
  mkdir -p "$KIT_REL/$RUN_GATES" .githooks notes src
  cp "$SRC/$RUN_GATES_DIR/gate-fingerprint.sh" "$KIT_REL/$RUN_GATES/"
  printf '%s\n' '[{"name":"x","argv":["bash","a.sh"]}]' > "$KIT_REL/gate-legs.json"
  cat > "$KIT_REL/$RUN_GATES/run-gates.sh" <<'BGSTUB'
#!/usr/bin/env bash
echo "BAR base=${GATE_BASE:-} full=${GATE_FULL:-}"
printf 'run\n' >> "$BG_MARK"
d="$(git rev-parse --git-dir)/gate-run/$GATE_RUN_ID"; mkdir -p "$d"
case "${BG_MODE:-green}" in
  green) printf 'verdict\tGREEN\n' > "$d/verdict"; exit 0 ;;
  red) printf 'verdict\tRED\ntree_moved\tno\nfailed\t1\n' > "$d/verdict"; exit 1 ;;
  inh) printf 'verdict\tRED\ntree_moved\tno\nfailed\t1\n' > "$d/verdict"
       printf 'leg x\tINHERITED\t-\t-\t%s\t-\n' "$GATE_ATTRIBUTE" > "$d/attribution"; exit 1 ;;
esac
BGSTUB
  # A WRAPPER BAR, inCMS's gov-bar shape: a tracked script that hands the runner a derived manifest.
  printf '#!/usr/bin/env bash\nexport GATE_LEGS="$(git rev-parse --git-dir)/wrap-legs.json"\nexec bash %s "$@"\n' \
    "$KIT_REL/$RUN_GATES/run-gates.sh" > wrap-bar.sh
  printf '#!/usr/bin/env bash\nexec bash %s "$@"\n' "$KIT_REL/$RUN_GATES/run-gates.sh" > other-bar.sh
  printf 'GATE_CMD="bash wrap-bar.sh"\n' > .unattended.conf
  printf 'GOV_KITROOT=%s\nINHERITED_RED=land\nGATE_DOC_PATHS="notes/"\n%b' "$KIT_REL" "${2:-}" > .githooks/gate-env.sh
  printf 'a\n' > notes/a.md; printf 'x\n' > src/x.sh; printf '* text eol=lf\n' > .gitattributes
  git add -A >/dev/null 2>&1; git commit -q -m init; git branch -M main
  git remote add origin "$BG_D/remote.git"; git push -q --no-verify origin main >/dev/null 2>&1
  bg_gd=$(git rev-parse --git-dir); BG_MARK="$BG_D/mark"; : > "$BG_MARK"
}
read_bg_marks() { wc -l < "$BG_MARK" | tr -d ' '; }
run_bg_push() { # [env…] -> BG_OUT BG_RC for a push of HEAD to main over the remote's main
  local l r; l=$(git rev-parse HEAD); r=$(git ls-remote origin refs/heads/main | cut -f1)
  touch "$bg_gd/push-main-active"
  BG_OUT=$(env -u GOV_GATE_CMD_TEST -u GOV_GATE_CMD -u GATE_RUN_ID GATE_SELFTESTS= BG_MARK="$BG_MARK" "$@" \
    bash "$BG_D/hooks/pre-push" origin "$BG_D/remote.git" <<<"refs/heads/main $l refs/heads/main ${r:-0000000000000000000000000000000000000000}" 2>&1)
  BG_RC=$?
}
set_bg_remote() { git push -q --no-verify origin HEAD:main >/dev/null 2>&1; }
write_bg_record() { # file · sha · kind · base · bar -> a planted gate-bar-green record
  printf 'sha\t%s\ntree\t%s\nbar\t%s\nbar_paths\t\nkind\t%s\nbase\t%s\nselftests\t\nrun_id\tplanted\nby\tpre-push\nstamped\tx\n' \
    "$2" "$(git rev-parse "$2^{tree}")" "$5" "$3" "$4" > "$1"
}
read_bg_key() { awk -F'\t' -v k="$2" '$1==k{print $2}' "$1" 2>/dev/null; }
set_bg_key() { awk -F'\t' -v k="$2" -v v="$3" 'BEGIN{OFS="\t"} $1==k{$2=v} {print}' "$1" > "$1.x" && mv "$1.x" "$1"; }
write_bg_stamp() { # sha -> a runner gate-full-green with a reproducible fingerprint and the manifest blob
  printf 'sha\t%s\nfingerprint\t%s\nmanifest_blob\t%s\nmanifest\t%s\nselftests\t\nrun_id\ttest\n' "$1" \
    "$(bash "$KIT_REL/$RUN_GATES/gate-fingerprint.sh" "$1")" "$(git rev-parse "$1:$KIT_REL/gate-legs.json")" \
    "$KIT_REL/gate-legs.json" > "$bg_gd/gate-full-green"
}
BG_RUNNER="bash $KIT_REL/$RUN_GATES/run-gates.sh"; BG_WRAP="bash wrap-bar.sh"

# AC1, AC2, AC11, AC3 — branch tip X pushed green writes the record; the --no-ff merge of X is covered.
build_bg_fixture ac1 || bad "BG could not build its fixture"
git checkout -q -b X; echo 1 >> src/x.sh; git commit -qam X; _x=$(git rev-parse HEAD)
run_bg_push
case "$BG_RC|$(cut -f1 "$bg_gd/gate-bar-green" 2>/dev/null | tr '\n' ' ')" in
  "0|sha tree bar bar_paths kind base selftests run_id by stamped ") ok "BG AC1 a green push writes gate-bar-green with the ten keys in order" ;;
  *) bad "BG AC1 expected the ten keys in order after a green push, got rc $BG_RC: $(cat "$bg_gd/gate-bar-green" 2>/dev/null || echo '<absent>')" ;;
esac
[ "$(read_bg_key "$bg_gd/gate-bar-green" sha)|$(read_bg_key "$bg_gd/gate-bar-green" tree)|$(read_bg_key "$bg_gd/gate-bar-green" kind)|$(read_bg_key "$bg_gd/gate-bar-green" by)|$(read_bg_key "$bg_gd/gate-bar-green" bar)" \
  = "$_x|$(git rev-parse "X^{tree}")|full|pre-push|$BG_RUNNER" ] \
  && ok "BG AC1 the record names X, its tree, kind full, by pre-push and the vetted bar" \
  || bad "BG AC1 the record's values are wrong: $(cat "$bg_gd/gate-bar-green" 2>/dev/null)"
set_bg_remote; git checkout -q main; git merge -q --no-ff X -m "merge X" >/dev/null 2>&1
_m0=$(read_bg_marks); run_bg_push
case "$BG_RC|$(read_bg_marks)|$BG_OUT" in
  "0|$_m0|"*"pre-push: covered on main push"*"this git dir's gate-bar-green sha ${_x:0:8}"*"no bar runs"*) ok "BG AC2 the merge of X is covered by X's record and no bar runs" ;;
  *) bad "BG AC2 expected a covered push with the marker at $_m0, got rc $BG_RC marker $(read_bg_marks): $BG_OUT" ;;
esac
case "$(awk -F'\t' '{print NF"|"$1"|"$2}' "$bg_gd/pre-push-bar" 2>/dev/null)|$(tail -1 "$bg_gd/runlog/pushes.log" 2>/dev/null)" in
  "3|default|$KIT_REL/$RUN_GATES/run-gates.sh|"*"ev=end"*"exit=clean"*"decision=covered"*) ok "BG AC11 a covered push writes pre-push-bar's three fields and an END with decision=covered exit=clean" ;;
  *) bad "BG AC11 pre-push-bar or the END line is wrong: $(cat "$bg_gd/pre-push-bar" 2>/dev/null) / $(tail -1 "$bg_gd/runlog/pushes.log" 2>/dev/null)" ;;
esac
set_bg_remote; git checkout -q -b Y; echo 2 >> src/x.sh; git commit -qam Y; run_bg_push; set_bg_remote
git checkout -q main; git merge -q --no-ff Y -m "merge Y" >/dev/null 2>&1; echo 3 >> src/x.sh; git commit -qam byte
_m0=$(read_bg_marks); run_bg_push
case "$(read_bg_marks)|$BG_OUT" in
  "$((_m0 + 1))|"*"not covered"*"it graded tree"*) ok "BG AC3 one more byte is not covered, says why, and the bar runs" ;;
  *) bad "BG AC3 expected not covered with the bar run, got marker $(read_bg_marks) from $_m0: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# AC4, AC5 — no record for the STUB, none for a red bar.
build_bg_fixture ac4 || bad "BG could not build its fixture"
printf '#!/usr/bin/env bash\nexit 0\n' > "$BG_D/stub.sh"
echo 1 >> src/x.sh; git commit -qam c; run_bg_push GOV_GATE_CMD_TEST=1 GOV_GATE_CMD="bash $BG_D/stub.sh"
case "$([ -f "$bg_gd/gate-bar-green" ] && echo present)|$BG_OUT" in
  "|"*"no gate-bar-green written — the bar is the declared STUB"*) ok "BG AC4 the STUB writes no record and says so" ;;
  *) bad "BG AC4 a STUB push wrote a record or did not say so: $BG_OUT" ;;
esac
echo 2 >> src/x.sh; git commit -qam c2; run_bg_push BG_MODE=red
[ "$BG_RC" = 1 ] && [ ! -f "$bg_gd/gate-bar-green" ] && ok "BG AC5 a red bar writes no record" \
  || bad "BG AC5 a red bar must write no record, got rc $BG_RC, record $([ -f "$bg_gd/gate-bar-green" ] && echo present)"
cd "$pfx_home" || exit 2

# AC6, AC7, AC8 — an altered record covers nothing; the unaltered one is the control.
build_bg_fixture ac6 || bad "BG could not build its fixture"
git checkout -q -b X; echo 1 >> src/x.sh; git commit -qam X; _x=$(git rev-parse HEAD)
git checkout -q main; git merge -q --no-ff X -m "merge X" >/dev/null 2>&1
for _c in bar selftests tree control; do
  write_bg_record "$bg_gd/gate-bar-green" "$_x" full "" "$BG_RUNNER"; _e=()
  case $_c in
    bar) set_bg_key "$bg_gd/gate-bar-green" bar "bash other-bar.sh"; _want="it was earned by bar" ;;
    selftests) _e=(GATE_SELFTESTS=1); _want="self-tests HELD" ;;
    tree) set_bg_key "$bg_gd/gate-bar-green" tree ""; _want="could not be read" ;;
    control) _want="pre-push: covered on main push" ;;
  esac
  _m0=$(read_bg_marks); run_bg_push "${_e[@]}"
  case "$_c|$(read_bg_marks)|$BG_OUT" in
    "control|$_m0|"*"$_want"*) ok "BG AC6-8 control: the unaltered record covers the merge" ;;
    "$_c|$((_m0 + 1))|"*"not covered"*"$_want"*) ok "BG AC6-8 an altered $_c is not covered, says '$_want', and the bar runs" ;;
    *) bad "BG AC6-8 the $_c case expected '$_want', got marker $(read_bg_marks) from $_m0: $BG_OUT" ;;
  esac
done
cd "$pfx_home" || exit 2

# AC9, AC10 — a runner stamp covers; a scoped record covers only from the adopted base.
build_bg_fixture ac9 || bad "BG could not build its fixture"
git checkout -q -b X; echo 1 >> src/x.sh; git commit -qam X; _x=$(git rev-parse HEAD)
git checkout -q main; git merge -q --no-ff X -m "merge X" >/dev/null 2>&1; write_bg_stamp "$_x"
_m0=$(read_bg_marks); run_bg_push
case "$(read_bg_marks)|$BG_OUT" in
  "$_m0|"*"covered on main push"*"a full green: this git dir sha ${_x:0:8}"*"by run-gates"*) ok "BG AC9 a runner stamp naming X covers the merge" ;;
  *) bad "BG AC9 expected the runner stamp to cover, got: $BG_OUT" ;;
esac
rm -f "$bg_gd/gate-full-green"; git reset -q --hard origin/main; _r=$(git rev-parse HEAD); write_bg_stamp "$_r"
echo 2 >> src/x.sh; git commit -qam lin; _l=$(git rev-parse HEAD)
write_bg_record "$bg_gd/gate-bar-green" "$_l" scoped "$_r" "$BG_RUNNER"
_m0=$(read_bg_marks); run_bg_push
case "$(read_bg_marks)|$BG_OUT" in
  "$_m0|"*"covered on main push"*"a scoped green"*) ok "BG AC10 a scoped record on the adopted base covers" ;;
  *) bad "BG AC10 a scoped record on the adopted base must cover, got: $BG_OUT" ;;
esac
write_bg_record "$bg_gd/gate-bar-green" "$_l" scoped "$_x" "$BG_RUNNER"
_m0=$(read_bg_marks); run_bg_push
case "$(read_bg_marks)|$BG_OUT" in
  "$((_m0 + 1))|"*"a scoped green against base ${_x:0:8}"*) ok "BG AC10 a scoped record on another base is not covered, naming it" ;;
  *) bad "BG AC10 a scoped record on another base must not cover, got: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# AC12 from a linked worktree; AC13 by slice.
build_bg_fixture ac12 || bad "BG could not build its fixture"
git worktree add -q "$BG_D/wt" -b wtb >/dev/null 2>&1
( cd "$BG_D/wt" || exit 1; bg_gd=$(git rev-parse --git-dir)
  echo 1 >> src/x.sh; git commit -qam wt; run_bg_push
  cmp -s "$bg_gd/gate-bar-green" "$(git rev-parse --git-common-dir)/gate-bar-green.shared" ) \
  && ok "BG AC12 a linked worktree's record is shared byte-identical to the common dir" \
  || bad "BG AC12 the common dir holds no byte-identical gate-bar-green.shared"
sed -n '/^write_bar_green() {/,/^}/p' "$SRC/.githooks/pre-push" > "$BG_D/slice.sh"
( . "$BG_D/slice.sh" || exit 1; rm -f "$bg_gd/gate-bar-green"
  _h=$(git rev-parse HEAD); git commit -q --allow-empty -m moved
  write_bar_green "$bg_gd" "$_h" 0 full "" "$BG_RUNNER" r1 >/dev/null
  _a=$([ -f "$bg_gd/gate-bar-green" ] && echo present)
  _h=$(git rev-parse HEAD); : > untracked.txt
  write_bar_green "$bg_gd" "$_h" 0 full "" "$BG_RUNNER" r2 >/dev/null
  _b=$([ -f "$bg_gd/gate-bar-green" ] && echo present)
  rm -f untracked.txt; write_bar_green "$bg_gd" "$_h" 0 full "" "$BG_RUNNER" r3 >/dev/null
  _c=$([ -f "$bg_gd/gate-bar-green" ] && echo present)
  [ "$_a|$_b|$_c" = "||present" ] ) \
  && ok "BG AC13 the sliced writer writes nothing with HEAD moved or an untracked file, and writes on the control" \
  || bad "BG AC13 the sliced writer wrote a record it must not have, or none on the control"
cd "$pfx_home" || exit 2

# AC14, AC15 — no record for an inherited red landed under land, none for a doc-only push.
build_bg_fixture ac14 || bad "BG could not build its fixture"
echo 1 >> src/x.sh; git commit -qam c; run_bg_push BG_MODE=inh
case "$BG_RC|$([ -f "$bg_gd/gate-bar-green" ] && echo present)|$BG_OUT" in
  "0||"*"red on inherited legs only"*"no gate-bar-green written"*) ok "BG AC14 an inherited red that lands writes no record" ;;
  *) bad "BG AC14 expected the inherited landing with no record, got rc $BG_RC: $BG_OUT" ;;
esac
git reset -q --hard origin/main; write_bg_stamp "$(git rev-parse HEAD)"; echo b >> notes/a.md; git commit -qam doc; run_bg_push
case "$([ -f "$bg_gd/gate-bar-green" ] && echo present)|$BG_OUT" in
  "|"*"docs-only"*"no gate-bar-green written — this push was scoped doc-only"*) ok "BG AC15 a doc-only scoped green writes no record and says so" ;;
  *) bad "BG AC15 expected no record on a doc-only push, got: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# AC17 — a wrapper bar's full record at M scopes the push of M plus one record-only commit.
build_bg_fixture ac17 || bad "BG could not build its fixture"
git checkout -q -b X; echo 1 >> src/x.sh; git commit -qam X; git checkout -q main
git merge -q --no-ff X -m "merge X" >/dev/null 2>&1; _m=$(git rev-parse HEAD)
run_bg_push GOV_GATE_CMD="$BG_WRAP"; set_bg_remote
echo r >> src/x.sh; git commit -qam "records: close"; run_bg_push GOV_GATE_CMD="$BG_WRAP"
case "$BG_OUT" in
  *"scoped gate on main push"*"full bar green ${_m:0:8} from this git dir's gate-bar-green"*"BAR base=$_m full="*) ok "BG AC17 a wrapper bar's full record at M scopes M plus a record commit, with GATE_BASE M" ;;
  *) bad "BG AC17 expected a scoped decision from the record at ${_m:0:8}, got: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# AC18, AC19, AC20 — a scoped record at M is adopted on its full-green base B, lag counted from B.
build_bg_fixture ac18 || bad "BG could not build its fixture"
_b=$(git rev-parse HEAD); for _i in 1 2; do echo "l$_i" >> src/x.sh; git commit -qam "l$_i"; done
_m=$(git rev-parse HEAD); echo c >> src/x.sh; git commit -qam C; set_bg_remote; echo c2 >> src/x.sh; git commit -qam C2
write_bg_record "$bg_gd/gate-bar-green.shared" "$_b" full "" "$BG_WRAP"; write_bg_record "$bg_gd/gate-bar-green" "$_m" scoped "$_b" "$BG_WRAP"
run_bg_push GOV_GATE_CMD="$BG_WRAP"
case "$BG_OUT" in
  *"scoped gate on main push"*"scoped bar green ${_m:0:8}"*"counted from its base ${_b:0:8}, is 4 first-parent"*"BAR base=$_m full="*) ok "BG AC18 a scoped record at M is adopted, scoping from M with the lag counted from B" ;;
  *) bad "BG AC18 expected a scoped decision from M counted from B, got: $BG_OUT" ;;
esac
_c=$(git rev-parse HEAD~1)
write_bg_record "$bg_gd/gate-bar-green" "$_m" scoped "$_c" "$BG_WRAP"; mv "$bg_gd/gate-bar-green.shared" "$BG_D/shared.keep"
run_bg_push GOV_GATE_CMD="$BG_WRAP"
case "$BG_OUT" in
  *"FULL gate on main push"*"its base ${_c:0:8} is no full green this push can adopt"*) ok "BG AC19 a scoped record whose base no full green names is refused, naming its base" ;;
  *) bad "BG AC19 expected the record refused on its base, got: $BG_OUT" ;;
esac
mv "$BG_D/shared.keep" "$bg_gd/gate-bar-green.shared"
for _i in $(seq 1 10); do echo "p$_i" >> src/x.sh; git commit -qam "p$_i"; done; _m=$(git rev-parse HEAD)
echo c3 >> src/x.sh; git commit -qam C3; set_bg_remote; echo c4 >> src/x.sh; git commit -qam C4
write_bg_record "$bg_gd/gate-bar-green" "$_m" scoped "$_b" "$BG_WRAP"; run_bg_push GOV_GATE_CMD="$BG_WRAP"
case "$BG_OUT" in
  *"FULL gate on main push"*"its base ${_b:0:8} is no full green this push can adopt: the recorded full bar green is 16 first-parent landings behind"*) ok "BG AC20 a scoped record whose base is past the bound is refused on the base's lag" ;;
  *) bad "BG AC20 expected the record refused on its base's lag, got: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# TOOL-aFrugalTurnstile-11 AC1, AC3 — a wrapper bar from one git dir: FULL, scoped, then scoped again.
build_bg_fixture slot1 || bad "BG could not build its fixture"
echo 1 >> src/x.sh; git commit -qam c1; _c1=$(git rev-parse HEAD); run_bg_push GOV_GATE_CMD="$BG_WRAP"; set_bg_remote
echo 2 >> src/x.sh; git commit -qam c2; _c2=$(git rev-parse HEAD); run_bg_push GOV_GATE_CMD="$BG_WRAP"; set_bg_remote
[ "$(read_bg_key "$bg_gd/gate-bar-green" kind)|$(read_bg_key "$bg_gd/gate-bar-green" sha)|$(read_bg_key "$bg_gd/gate-bar-green.scoped" kind)|$(read_bg_key "$bg_gd/gate-bar-green.scoped" sha)" \
  = "full|$_c1|scoped|$_c2" ] \
  && ok "BG slot AC1 a scoped push leaves gate-bar-green kind full and writes gate-bar-green.scoped kind scoped" \
  || bad "BG slot AC1 expected the full record kept and the scoped one in its own slot: $(cat "$bg_gd/gate-bar-green" "$bg_gd/gate-bar-green.scoped" 2>&1)"
echo 3 >> src/x.sh; git commit -qam c3; run_bg_push GOV_GATE_CMD="$BG_WRAP"
case "$BG_OUT" in
  *"FULL gate on main push"*) bad "BG slot AC3 the third push went FULL, the alternation: $BG_OUT" ;;
  *"scoped gate on main push"*) ok "BG slot AC3 the third push from the same git dir reads scoped gate" ;;
  *) bad "BG slot AC3 expected a scoped gate line, got: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# TOOL-aFrugalTurnstile-11 AC2 — the scoped record from a linked worktree is shared to the common dir.
build_bg_fixture slot2 || bad "BG could not build its fixture"
git worktree add -q "$BG_D/wt" -b wtb >/dev/null 2>&1
( cd "$BG_D/wt" || exit 1; bg_gd=$(git rev-parse --git-dir)
  echo 1 >> src/x.sh; git commit -qam w1; run_bg_push GOV_GATE_CMD="$BG_WRAP"; set_bg_remote
  echo 2 >> src/x.sh; git commit -qam w2; run_bg_push GOV_GATE_CMD="$BG_WRAP"
  [ "$(read_bg_key "$bg_gd/gate-bar-green.scoped" kind)" = scoped ] \
    && cmp -s "$bg_gd/gate-bar-green.scoped" "$(git rev-parse --git-common-dir)/gate-bar-green.scoped.shared" ) \
  && ok "BG slot AC2 a linked worktree's scoped record is shared byte-identical as gate-bar-green.scoped.shared" \
  || bad "BG slot AC2 the common dir holds no byte-identical gate-bar-green.scoped.shared"
cd "$pfx_home" || exit 2

# TOOL-aFrugalTurnstile-11 AC4 — a scoped record only in the scoped slot covers a push of its tree.
build_bg_fixture slot4 || bad "BG could not build its fixture"
_b=$(git rev-parse HEAD); echo 1 >> src/x.sh; git commit -qam l; _l=$(git rev-parse HEAD)
write_bg_record "$bg_gd/gate-bar-green" "$_b" full "" "$BG_WRAP"; write_bg_record "$bg_gd/gate-bar-green.scoped" "$_l" scoped "$_b" "$BG_WRAP"
_m0=$(read_bg_marks); run_bg_push GOV_GATE_CMD="$BG_WRAP"
case "$(read_bg_marks)|$BG_OUT" in
  "$_m0|"*"covered on main push"*"this git dir's gate-bar-green.scoped sha ${_l:0:8}"*"no bar runs"*) ok "BG slot AC4 the cover pass reads the scoped slot" ;;
  *) bad "BG slot AC4 expected the scoped-slot record to cover with no bar run, got marker $(read_bg_marks) from $_m0: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# TOOL-aFrugalTurnstile-11 AC5 — a runner stamp at F and a scoped record at M (base F): M is nearer, M wins.
build_bg_fixture slot5 || bad "BG could not build its fixture"
_f=$(git rev-parse HEAD); write_bg_stamp "$_f"
echo 1 >> src/x.sh; git commit -qam m; _m=$(git rev-parse HEAD); write_bg_record "$bg_gd/gate-bar-green" "$_m" scoped "$_f" "$BG_RUNNER"
echo 2 >> src/x.sh; git commit -qam t; run_bg_push
case "$BG_OUT" in
  *"scoped gate on main push"*"scoped bar green ${_m:0:8}"*"counted from its base ${_f:0:8}"*"BAR base=$_m full="*) ok "BG slot AC5 the nearer scoped record at M beats the runner stamp at F" ;;
  *) bad "BG slot AC5 expected the decision to scope from M, got: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# TOOL-aFrugalTurnstile-11 AC6 — a runner stamp and a bar record at one sha: the tie keeps the runner stamp.
build_bg_fixture slot6 || bad "BG could not build its fixture"
echo 1 >> src/x.sh; git commit -qam s; _s=$(git rev-parse HEAD); write_bg_stamp "$_s"
write_bg_record "$bg_gd/gate-bar-green" "$_s" full "" "$BG_RUNNER"; echo 2 >> src/x.sh; git commit -qam t; run_bg_push
case "$BG_OUT" in
  *"scoped gate on main push"*"full green ${_s:0:8} from this git dir's gate-full-green"*) ok "BG slot AC6 a tie names gate-full-green as the adopted record" ;;
  *) bad "BG slot AC6 expected the runner stamp named on a tie, got: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# THE POST-MERGE RED AND THE DECIDE MODE — TOOL-aFrugalTurnstile-7. A git shim first on PATH logs every
# argv the hook spawns, so "the red was read" is a count of ls-remote lines, never an inference. The red
# ref is staged by hand on the bare remote; only post-merge.sh publishes it for real.
PM_GIT=$(command -v git); PM_DECL='GATE_POST_MERGE=local\n'
build_pm_shim() { # -> a git shim under BG_D logging every argv to BG_D/shim.log; PM_PATH puts it first
  mkdir -p "$BG_D/shim"
  printf '#!/usr/bin/env bash\nprintf "%%s\\n" "$*" >> "%s/shim.log"\nexec "%s" "$@"\n' "$BG_D" "$PM_GIT" > "$BG_D/shim/git"
  chmod +x "$BG_D/shim/git"; : > "$BG_D/shim.log"; PM_PATH="$BG_D/shim:$PATH"
}
write_pm_red() { git push -q --no-verify origin "+$1:refs/gov/bar-red" >/dev/null 2>&1; }
run_pm_decide() { # [env…] -- <args> -> PM_OUT (stdout alone) PM_ERR PM_RC for `pre-push --decide <args>`
  local e=(); while [ "$1" != -- ]; do e+=("$1"); shift; done; shift
  PM_OUT=$(env -u GOV_GATE_CMD_TEST -u GOV_GATE_CMD -u GATE_RUN_ID -u GOV_REMOTE GATE_SELFTESTS= BG_MARK="$BG_MARK" "${e[@]}" \
    bash "$BG_D/hooks/pre-push" --decide "$@" 2>"$BG_D/decide.err" </dev/null); PM_RC=$?; PM_ERR=$(cat "$BG_D/decide.err")
}
read_pm_sums() { git status >/dev/null 2>&1; find "$bg_gd" -type f | sort | xargs sha1sum; }   # after git's own warm-up
read_pm_remote() { git ls-remote origin refs/heads/main | cut -f1; }

# AC1, AC5 — a declared red between the recorded full green and the tip forces FULL, read once.
for _pm in "local:AC1" "yes:AC5"; do
  build_bg_fixture "pm-${_pm%%:*}" "GATE_POST_MERGE=${_pm%%:*}\n" || bad "PM could not build its fixture"; build_pm_shim
  _f=$(git rev-parse HEAD); write_bg_stamp "$_f"; echo 1 >> src/x.sh; git commit -qam p; _p=$(git rev-parse HEAD)
  echo 2 >> src/x.sh; git commit -qam t; write_pm_red "$_p"; run_bg_push PATH="$PM_PATH"
  case "$BG_OUT" in
    *"FULL gate on main push"*"a post-merge full bar is RED at ${_p:0:8} (refs/gov/bar-red on origin)"*"BAR base= full=1"*) ok "PM ${_pm#*:} a declared red the green does not descend from forces FULL" ;;
    *) bad "PM ${_pm#*:} expected FULL naming the red ${_p:0:8}, got: $BG_OUT" ;;
  esac
  [ "$(grep -c ls-remote "$BG_D/shim.log")" = 1 ] && ok "PM ${_pm#*:} the red is read with exactly one ls-remote" \
    || bad "PM ${_pm#*:} expected one ls-remote, got: $(grep ls-remote "$BG_D/shim.log")"
  case "${_pm%%:*}|$BG_OUT" in
    local*) ;;
    "yes|"*"GATE_POST_MERGE at "*" is 'yes', outside 'local ci', and is read as declared"*) ok "PM AC5 an unknown value is named and read as declared" ;;
    *) bad "PM AC5 expected the outside 'local ci' line, got: $BG_OUT" ;;
  esac
  cd "$pfx_home" || exit 2
done

# AC2 — the recorded green strictly descends from the red: cleared, and the push scopes.
build_bg_fixture pm-clear "$PM_DECL" || bad "PM could not build its fixture"
_p=$(git rev-parse HEAD); echo 1 >> src/x.sh; git commit -qam x; _x=$(git rev-parse HEAD); write_bg_stamp "$_x"
echo 2 >> src/x.sh; git commit -qam t; write_pm_red "$_p"; run_bg_push
case "$BG_OUT" in
  *"post-merge bar: red ${_p:0:8} on origin is cleared for this push — the adopted green ${_x:0:8} descends from it"*"scoped gate on main push"*) ok "PM AC2 a green descending from the red clears it and scopes" ;;
  *) bad "PM AC2 expected the cleared line and a scoped gate, got: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# AC3 — undeclared at R, a present red is never read and the decision does not move.
build_bg_fixture pm-undecl || bad "PM could not build its fixture"; build_pm_shim
_f=$(git rev-parse HEAD); write_bg_stamp "$_f"; echo 1 >> src/x.sh; git commit -qam p; _p=$(git rev-parse HEAD)
echo 2 >> src/x.sh; git commit -qam t; write_pm_red "$_p"; run_bg_push PATH="$PM_PATH"
case "$(grep -c ls-remote "$BG_D/shim.log")|$BG_OUT" in
  "0|"*"post-merge bar"*) bad "PM AC3 an undeclared push printed a post-merge line: $BG_OUT" ;;
  "0|"*"scoped gate on main push"*"full green ${_f:0:8}"*) ok "PM AC3 undeclared: no ls-remote and the decision is unchanged" ;;
  *) bad "PM AC3 expected no ls-remote and a scoped gate from ${_f:0:8}, got: $(grep ls-remote "$BG_D/shim.log") $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# AC4 — declared, and the push URL reaches nothing: --decide reads unreadable as FULL, never as absent.
build_bg_fixture pm-unread "$PM_DECL" || bad "PM could not build its fixture"
_f=$(git rev-parse HEAD); write_bg_stamp "$_f"; echo 1 >> src/x.sh; git commit -qam t
git remote set-url --push origin "$BG_D/nowhere/x.git"; run_pm_decide -- "$(git rev-parse HEAD)" "$(read_pm_remote)"
case "$PM_RC|$PM_OUT" in
  "0|full GATE_POST_MERGE is declared at "*"refs/gov/bar-red on origin could not be read"*) ok "PM AC4 an unreadable red decides full" ;;
  *) bad "PM AC4 expected one full line naming refs/gov/bar-red as unreadable, got rc $PM_RC: $PM_OUT" ;;
esac
cd "$pfx_home" || exit 2

# AC6 — three states, one stdout line each, exit 0, and nothing under the git dir moves.
build_bg_fixture pm-decide || bad "PM could not build its fixture"
_f=$(git rev-parse HEAD); echo 1 >> src/x.sh; git commit -qam t; _t=$(git rev-parse HEAD); _r=$(read_pm_remote)
for _st in none scoped covered; do
  _e=()
  case $_st in
    scoped) write_bg_stamp "$_f" ;;
    covered) rm -f "$bg_gd/gate-full-green"; write_bg_record "$bg_gd/gate-bar-green" "$_f" full "" "$BG_WRAP"
             write_bg_record "$bg_gd/gate-bar-green.scoped" "$_t" scoped "$_f" "$BG_WRAP"; _e=(GOV_GATE_CMD="$BG_WRAP") ;;
  esac
  read_pm_sums > "$BG_D/s0"; _j0=$(cat "$bg_gd"/runlog/*.log 2>/dev/null | wc -l); _m0=$(read_bg_marks)
  run_pm_decide "${_e[@]}" -- "$_t" "$_r"; read_pm_sums > "$BG_D/s1"
  case "$_st|$PM_RC|$(printf '%s\n' "$PM_OUT" | grep -c .)|$PM_OUT" in
    "none|0|1|full "*|"scoped|0|1|scoped $_f"|"covered|0|1|covered "*"gate-bar-green.scoped") ok "PM AC6 $_st: one decision line, exit 0" ;;
    *) bad "PM AC6 $_st expected one $_st line and exit 0, got rc $PM_RC: $PM_OUT" ;;
  esac
  { cmp -s "$BG_D/s0" "$BG_D/s1" && [ ! -e "$bg_gd/pre-push-refusal" ] && [ ! -e "$bg_gd/pre-push-bar" ] &&
    [ "$(cat "$bg_gd"/runlog/*.log 2>/dev/null | wc -l)" = "$_j0" ] && [ "$(read_bg_marks)" = "$_m0" ]; } \
    && ok "PM AC6 $_st: no file under the git dir changed, no journal line, no bar" \
    || bad "PM AC6 $_st wrote something: $(diff "$BG_D/s0" "$BG_D/s1" | head -3) marks $_m0/$(read_bg_marks)"
done
cd "$pfx_home" || exit 2

# AC7, AC9 — a refusal exits 1 with an empty stdout; a bad call or an unchosen remote exits 2.
build_bg_fixture pm-refuse || bad "PM could not build its fixture"
_f=$(git rev-parse HEAD); write_bg_stamp "$_f"; echo 1 >> src/x.sh; git commit -qam t; _t=$(git rev-parse HEAD); _r=$(read_pm_remote)
echo 3 >> src/x.sh; run_pm_decide -- "$_t" "$_r"; _o1="$PM_RC|$PM_OUT"; git checkout -q src/x.sh
run_pm_decide -- "$_f" "$_r"; _o2="$PM_RC|$PM_OUT"
[ "$_o1|$_o2|$([ -e "$bg_gd/pre-push-refusal" ] && echo file)" = "1||1||" ] \
  && ok "PM AC7 a dirty tree and a tip that is not HEAD exit 1 with an empty stdout and no refusal file" \
  || bad "PM AC7 expected exit 1, empty stdout, no refusal file: dirty '$_o1' tip '$_o2'"
run_pm_decide -- "$_t"; _o1="$PM_RC|$PM_ERR"; run_pm_decide -- nosuch "$_r"
case "$_o1|$PM_RC|$PM_ERR" in
  "2|"*"usage: pre-push --decide"*"|2|"*"usage: pre-push --decide"*) ok "PM AC7 one argument and a tip naming no commit exit 2 with the usage line" ;;
  *) bad "PM AC7 expected exit 2 and a usage line twice, got: $_o1 | $PM_RC $PM_ERR" ;;
esac
git remote add second "$BG_D/remote.git"; git checkout -q --detach
run_pm_decide -- "$_t" "$_r"; _o1="$PM_RC|$PM_ERR"; run_pm_decide -- "$_t" "$_r" origin
case "$_o1|$PM_RC|$PM_OUT" in
  "2|"*GOV_REMOTE*"|0|scoped $_f") ok "PM AC9 two remotes and none named exit 2 naming GOV_REMOTE; a named one decides" ;;
  *) bad "PM AC9 expected exit 2 naming GOV_REMOTE, then a decision, got: $_o1 | $PM_RC $PM_OUT" ;;
esac
cd "$pfx_home" || exit 2

# AC11 — a covering record binds to the red too; and --decide's scoped base is the push's GATE_BASE.
build_bg_fixture pm-cover "$PM_DECL" || bad "PM could not build its fixture"
_b=$(git rev-parse HEAD); echo 1 >> src/x.sh; git commit -qam l; _l=$(git rev-parse HEAD)
for _red in "$_l" "$_b"; do
  write_bg_record "$bg_gd/gate-bar-green" "$_b" full "" "$BG_WRAP"; write_bg_record "$bg_gd/gate-bar-green.scoped" "$_l" scoped "$_b" "$BG_WRAP"
  write_pm_red "$_red"; _m0=$(read_bg_marks); run_bg_push GOV_GATE_CMD="$BG_WRAP"
  case "$_red|$(read_bg_marks)|$BG_OUT" in
    "$_l|$((_m0 + 1))|"*"FULL gate on main push"*"RED at ${_l:0:8}"*) ok "PM AC11 a red the covering record does not strictly descend from forces FULL" ;;
    "$_b|$_m0|"*"covered on main push"*"no bar runs"*) ok "PM AC11 a covering record that descends from the red stays covered" ;;
    *) bad "PM AC11 red ${_red:0:8}: unexpected decision, marker $_m0/$(read_bg_marks): $BG_OUT" ;;
  esac
done
cd "$pfx_home" || exit 2
build_bg_fixture pm-base || bad "PM could not build its fixture"
_f=$(git rev-parse HEAD); write_bg_stamp "$_f"; echo 1 >> src/x.sh; git commit -qam t
run_pm_decide -- "$(git rev-parse HEAD)" "$(read_pm_remote)"; run_bg_push
case "$BG_OUT" in
  *"BAR base=${PM_OUT#scoped } full="*) [ "$PM_OUT" = "scoped $_f" ] && ok "PM AC11 the scoped base --decide prints is the GATE_BASE the bar receives" \
    || bad "PM AC11 --decide printed '$PM_OUT', not scoped $_f" ;;
  *) bad "PM AC11 the bar's GATE_BASE differs from --decide's '$PM_OUT': $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

# AC12 — a scoped record written on a scoped base names that base's FULL green, and the next push adopts it.
build_bg_fixture pm-chain || bad "PM could not build its fixture"
echo 1 >> src/x.sh; git commit -qam c1; _c1=$(git rev-parse HEAD); run_bg_push GOV_GATE_CMD="$BG_WRAP"; set_bg_remote
echo 2 >> src/x.sh; git commit -qam c2; run_bg_push GOV_GATE_CMD="$BG_WRAP"; set_bg_remote
echo 3 >> src/x.sh; git commit -qam c3; _c3=$(git rev-parse HEAD); run_bg_push GOV_GATE_CMD="$BG_WRAP"; set_bg_remote
[ "$(read_bg_key "$bg_gd/gate-bar-green.scoped" sha)|$(read_bg_key "$bg_gd/gate-bar-green.scoped" base)" = "$_c3|$_c1" ] \
  && ok "PM AC12 the scoped record written on a scoped base names the full green ${_c1:0:8}" \
  || bad "PM AC12 expected gate-bar-green.scoped at ${_c3:0:8} with base ${_c1:0:8}: $(cat "$bg_gd/gate-bar-green.scoped" 2>&1)"
echo 4 >> src/x.sh; git commit -qam c4; run_bg_push GOV_GATE_CMD="$BG_WRAP"
case "$BG_OUT" in
  *"scoped gate on main push"*"scoped bar green ${_c3:0:8}"*) ok "PM AC12 the next push adopts the new scoped record" ;;
  *) bad "PM AC12 expected the push to scope from ${_c3:0:8}, got: $BG_OUT" ;;
esac
cd "$pfx_home" || exit 2

[ "$fail" = 0 ] && { echo "pre-push.test: all cases ok"; exit 0; } || { echo "pre-push.test: FAILURES"; exit 1; }
