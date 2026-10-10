#!/usr/bin/env bash
# Runnable check for <prefix>/check-wiring.sh. Spins throwaway repos and asserts the wired/unwired
# detection, the never-clobber auto-fix, and the always-exit-0 --session mode. Run: bash <prefix>/check-wiring.test.sh
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# The repository, asked of git: `$HERE/..` is the root only at a one-segment prefix (VERIFYING repair).
REPO="$(git -C "$HERE" rev-parse --show-toplevel)" || exit 2   # safe dir to return to before any rm -rf
# THIS SUITE'S OWN DIRECTORY, DERIVED (TOOL-aRepatriatedFork-19 S4, on the canonical block
# TOOL-aRepatriatedFork-18 S2 ships). It was a spelled gov-prefix default that nothing ever set, so at
# any prefix but gov's every fixture below laid its kit files where the checker under test does not
# look. The suite sits beside the checker, so its directory IS the checker's own KIT_REL.
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-wiring.test: not inside a git repository"; exit 2; }
KP=${KIT_REL:+$KIT_REL/}   # the prefix as a path head: empty at a root install, never a bare '/'
# ROOTPFX is a ROOT install's prefix, empty by definition: a fixture that models a root install,
# or a key relative to the tool root, is spelled through it rather than bare (TOOL-aRepatriatedFork-28 S2).
ROOTPFX=""
SCRIPT="$HERE/check-wiring.sh"
SMERGE="$HERE/settings-merge.py"
pass=0; fail=0
ck() { if [ "$2" = 1 ]; then echo "ok   $1"; pass=$((pass+1)); else echo "FAIL $1"; fail=$((fail+1)); fi; }

D=""; OOT=""
newrepo() {   # cd (in THIS shell) into a fresh repo with a tracked .githooks/pre-commit
  D=$(mktemp -d); cd "$D" || exit 2
  git init -q -b main; git config core.autocrlf false; git config user.email t@e; git config user.name t
  mkdir .githooks; printf '#!/bin/sh\nexit 0\n' > .githooks/pre-commit; chmod +x .githooks/pre-commit
  # `--chmod=+x`, not the filesystem bit: on a core.fileMode=false host `git add` stages 100644 from
  # an executable file, and the hook-mode arm would then grade every fixture here (TOOL-aLevelledCopy-3 S7).
  git add --chmod=+x .githooks/pre-commit; git commit -q -m init
}
cleanup() { cd "$REPO"; [ -n "$D" ] && rm -rf "$D"; [ -n "$OOT" ] && rm -rf "$OOT"; D=""; OOT=""; }
chk() { bash "$SCRIPT" "$@" 2>/dev/null; }   # run the checker, drop stderr noise
# ...and the variant that KEEPS stderr. The resolver's refusals are written there, so an arm that
# asserts on a refusal MESSAGE through `chk` would be asserting on text it discarded — a fixture
# that cannot see what it grades. TOOL-dRetiredFork-8.
chke() { bash "$SCRIPT" "$@" 2>&1; }

# ONE PYTHON, resolved by the resolver carried INLINE (TOOL-aRepatriatedFork-19 S4). This sourced
# the resolver library beside the suite, which exists only in gov: that library is gov-internal and
# ships to no adopter, so at an adopter the suite fell back to a bare launcher NAME. The block is
# byte-identical to the canonical copy its marker line names, gated by the parity table in the
# resolve-python self-test.
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
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME.
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
_rkd_py=$(resolve_python) || { echo "check-wiring.test: no usable python, so the sibling kits cannot be resolved"; exit 2; }
HOOKS_DIR=$(resolve_kit_dir "$_rkd_py" hooks agent-cap.js "$HERE") || exit 2
HOOKS="${HOOKS_DIR##*/}"
MT_KIT_DIR=$(resolve_kit_dir "$_rkd_py" memory-tree merge-rows.py "$HERE") || exit 2
MT_KIT="${MT_KIT_DIR##*/}"
MEMORY_RECALL_DIR=$(resolve_kit_dir "$_rkd_py" memory-recall extract.py "$HERE") || exit 2
MEMORY_RECALL="${MEMORY_RECALL_DIR##*/}"
LIB_DIR=$(resolve_kit_dir "$_rkd_py" lib pyrun.sh "$HERE") || exit 2
LIB="${LIB_DIR##*/}"
ROOT_ABS="$(git -C "$HERE" rev-parse --show-toplevel)" || exit 2
py=$(resolve_python "${PYBIN:-}") || { echo "check-wiring.test: no usable python"; exit 2; }

# A kit file in THIS repo, resolved across both install layouts the way every arm resolves them:
# beside this suite (`<prefix>/<rel>` here, `scripts/<rel>` at an adopter that installs the kits there),
# or at the root in a copy-installed adopter. The prefix is this file's own directory, DERIVED
# (TOOL-aRepatriatedFork-8 S6); it used to be the literal `<prefix>/`, which adopter nc patched with a
# third rung for `scripts/`.
src_of() { for c in "$HERE/$1" "$REPO/$1"; do [ -e "$c" ] && { echo "$c"; return; }; done; }

# THE MEMORY-TREE KIT'S OWN MODULES, laid WHOLE into $1 and DERIVED from the directory the shipped
# driver sits in rather than typed. `merge-rows.py` loads siblings at run time: `backlog.py` for the
# view/shard refusal that opens EVERY merge, and `tree_lib.py` for its conf read. A fixture carrying a
# typed subset holds a driver that cannot start, so every arm that RUNS it reads UNWIRED for the
# fixture's reasons. That is how AC10, AC12 and U19 AC1 went red when TOOL-dDerivedDocket-10 gave the
# driver its view predicate: the lists here predated `backlog.py`. A glob of the kit is what a
# copy-install lays, so a sibling the driver gains later reaches these fixtures with no edit here.
seed_driver_kit() {  # $1 = destination directory -> every python module of the memory-tree kit
  local drv
  drv=$(src_of "${ROOTPFX}${MT_KIT}/merge-rows.py")  # src_of keys under the tool root; the kit dir is the driver's own
  [ -n "$drv" ] || { ck "seed_driver_kit: the memory-tree kit is not installed in $REPO (the driver cannot run without it)" 0; return 1; }
  cp "${drv%/*}/"*.py "$1/"
}

# Lay a COMPLETE, RUNNABLE merge-driver install into the cwd under prefix $1 ("<prefix>/" here, "" for
# the copy-installed adopter layout). Complete is the point: the driver sources a resolver through
# its shim, imports its anchor grammar from the sibling memory-recall kit and its view layer from its
# own kit (`seed_driver_kit`), and walks up for `.memory-tree.conf`. A fixture missing any of those
# holds a driver that CANNOT START — which is exactly the state the arm under test has to report, so
# it must be reachable on purpose and never by accident.
install_driver() {
  local p="$1" rel src
  mkdir -p "${p}memory-tree" "${p}lib" "${p}memory-recall" memory/backlog
  # A CONTINUED LINE CANNOT CARRY A COMMENT — the backslash would escape the space before it,
  # not the newline — so the list is two assignments, each of which can be marked.
  _rels="${ROOTPFX}${MT_KIT}/merge-rows.py ${ROOTPFX}${MT_KIT}/merge-rows.sh ${ROOTPFX}${LIB}/pyrun.sh ${ROOTPFX}${LIB}/resolve-python.sh"
  _rels="$_rels ${ROOTPFX}${MEMORY_RECALL}/extract.py ${ROOTPFX}${MEMORY_RECALL}/recall_conf.py"
  for rel in $_rels; do
    src=$(src_of "$rel")
    # A NAMED cause instead of `cp: cannot stat ''`. Every file in this list is a runtime dependency
    # of the driver — the shim's resolver, the memory-recall kit the anchor grammar is imported
    # from — so a repo carrying `merge-rows.py` without one of them carries a driver that cannot
    # start. That is a defect in the repo, not a gap in the fixture, and it reds rather than skips.
    [ -n "$src" ] || { ck "install_driver: $rel is not installed in $REPO (the driver cannot run without it)" 0; return 1; }
    cp "$src" "${p}${rel}"
  done
  seed_driver_kit "${p}${ROOTPFX}${MT_KIT}" || return 1
  printf 'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\n' > .memory-tree.conf
  # A REAL ANCHORED ROW, not an empty index. The merge arm harvests the family prefix each row LEADS
  # with and requires the conf to declare it — over an index with no rows that harvest is empty and
  # state 5d below would pass by finding nothing, which is the vacuity this repo's pop_guard idiom
  # exists to refuse. State 5d IS the liveness proof: it only reds if this row is here and harvested.
  printf '# tooling backlog\n\n- TOOL-001 | a landed row, so the family harvest has a population\n' > memory/backlog/TOOL.md
  printf 'memory/backlog/*.md merge=rows\n' > .gitattributes
  git add -A; git commit -q -m driver
}

# AC1 — unset core.hooksPath -> UNWIRED + exit 1
newrepo
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  hooks'; } && ck "AC1 unset -> UNWIRED, exit 1" 1 || ck "AC1 unset -> UNWIRED, exit 1" 0
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${pass:-1} assertions)" || echo "FAIL (${pass:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi
# AC2 — --fix sets it, re-check exits 0
chk --fix >/dev/null; got=$(git config core.hooksPath); chk --check >/dev/null; rc=$?
{ [ "$got" = ".githooks" ] && [ "$rc" = 0 ]; } && ck "AC2 --fix wires, re-check exit 0" 1 || ck "AC2 --fix wires, re-check exit 0" 0
cleanup

# AC3 — valid out-of-tree hooksPath -> WIRED, --fix never clobbers
newrepo
OOT=$(mktemp -d); printf '#!/bin/sh\nexit 0\n' > "$OOT/pre-commit"; chmod +x "$OOT/pre-commit"
git config core.hooksPath "$OOT"
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       hooks'; } && ck "AC3 out-of-tree -> WIRED" 1 || ck "AC3 out-of-tree -> WIRED" 0
# never-clobber: git may re-spell the path (MSYS /tmp -> C:/Temp), so compare git's OWN value
# before vs after --fix, and assert it was NOT reset to the .githooks fix target.
before=$(git config core.hooksPath); chk --fix >/dev/null; after=$(git config core.hooksPath)
{ [ "$after" = "$before" ] && [ "$after" != ".githooks" ]; } && ck "AC3 --fix never clobbers a set value" 1 || ck "AC3 --fix never clobbers a set value" 0
cleanup

# AC4 — non-literal ./.githooks -> WIRED
newrepo; git config core.hooksPath ./.githooks
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       hooks'; } && ck "AC4 ./.githooks -> WIRED" 1 || ck "AC4 ./.githooks -> WIRED" 0
cleanup

# AC5a — all wired -> exit 0
newrepo; git config core.hooksPath .githooks; chk --check >/dev/null; [ "$?" = 0 ] && ck "AC5 all wired -> exit 0" 1 || ck "AC5 all wired -> exit 0" 0
cleanup
# AC5b — non-git dir -> exit 0
D=$(mktemp -d); cd "$D" || exit 2; chk --check >/dev/null; [ "$?" = 0 ] && ck "AC5 non-git -> exit 0" 1 || ck "AC5 non-git -> exit 0" 0
cleanup
# AC5c — repo without .githooks -> skip, exit 0
D=$(mktemp -d); cd "$D" || exit 2; git init -q -b main; git config user.email t@e; git config user.name t; git commit -q --allow-empty -m init
chk --check >/dev/null; [ "$?" = 0 ] && ck "AC5 no .githooks -> skip, exit 0" 1 || ck "AC5 no .githooks -> skip, exit 0" 0
cleanup

# AC6 — --session auto-wires unset AND exits 0
newrepo
chk --session >/dev/null; rc=$?; got=$(git config core.hooksPath)
{ [ "$rc" = 0 ] && [ "$got" = ".githooks" ]; } && ck "AC6 --session wires + exit 0" 1 || ck "AC6 --session wires + exit 0" 0
# TOOL-aGraftedHelix-8 AC4 — the auto-wire is a self-heal, so it appends ONE I3 line to the health log
# under the common dir, and only on the branch that ran `git config`: a second SessionStart over the
# wired tree prints `ok` and appends nothing, or the card would count a heal on every session start.
# WHAT THIS DOES NOT CHECK: the line's stamp or fold, which the resolver suite's §2c owns.
hl="$(git rev-parse --path-format=absolute --git-common-dir)/health.log"
ck "U8 AC4 --session's hooks auto-wire appends one check-wiring hookspath-set line" \
   "$([ "$(awk -F'\t' '$2 == "check-wiring" && $3 == "hookspath-set" && $4 ~ /mode session$/' "$hl" 2>/dev/null | wc -l | tr -d ' ')" = 1 ] && [ "$(grep -c . "$hl")" = 1 ] && echo 1 || echo 0)"
nb=$(grep -c . "$hl" 2>/dev/null); out=$(chk --session)
ck "U8 AC4 ...and a second --session over the wired tree prints ok and appends none" \
   "$(printf '%s\n' "$out" | grep -q '^ok       hooks' && [ "$(grep -c . "$hl" 2>/dev/null)" = "$nb" ] && echo 1 || echo 0)"
cleanup

# AC7 — agent-cap adopted but unwired -> --check UNWIRED (exit 1); --session still exits 0
if [ -f "$SMERGE" ]; then
  newrepo; mkdir -p $KIT_REL/${HOOKS} .claude/hooks; cp "$SMERGE" ${KP}settings-merge.py
  # The stub goes where the FRAGMENT declares the hook, not at `.claude/hooks/`.
  # TOOL-dRetiredFork-14 moved the shipped copy under the kit directory, so a fixture that
  # keeps installing into `.claude/hooks/` is testing a layout the kit no longer produces --
  # the arm then reports "not adopted" and the state it exists to catch goes ungraded.
  printf '// stub\n' > $KIT_REL/${HOOKS}/agent-cap.js
  git config core.hooksPath .githooks     # isolate: hooks wired, so only agent-cap can be unwired
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  agent-cap'; } && ck "AC7 agent-cap unwired -> UNWIRED, exit 1" 1 || ck "AC7 agent-cap unwired -> UNWIRED, exit 1" 0
  chk --session >/dev/null; [ "$?" = 0 ] && ck "AC6 --session exit 0 despite agent-cap unwired" 1 || ck "AC6 --session exit 0 despite agent-cap unwired" 0

  # AC7b — THE STALE MATCHER. `.claude/settings.json` carries the hook under `Workflow` alone: the
  # state where a direct `Agent` spawn meets no rule at all, and the state every repo was in before
  # the widening. The retired predicate grepped the whole file for `agent-cap.js`, so it reported
  # `ok` here — it could not tell a correctly-widened wiring from a stale one and never could have.
  # This arm fails against that predicate, which is what makes it a test rather than a restatement.
  cat > .claude/settings.json <<'JSON'
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Workflow",
        "hooks": [
          {
            "type": "command",
            "command": "node \"${CLAUDE_PROJECT_DIR}/{KP}{HOOKS}/agent-cap.js\""
          }
        ]
      }
    ]
  }
}
JSON
  sed -i "s#{KP}#${KP}#; s#{HOOKS}#${HOOKS}#" .claude/settings.json   # the quoted heredoc cannot expand either
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  agent-cap' \
      && printf '%s' "$out" | grep -q "wired under matcher 'Workflow'"; } \
    && ck "AC7b a stale Workflow-only matcher -> UNWIRED naming the value found" 1 \
    || ck "AC7b a stale Workflow-only matcher -> UNWIRED naming the value found" 0
  # ...and the widened value is the one that reads ok. Without this half the arm is satisfied by a
  # checker that denies every matcher there is. Written directly rather than merged: settings-merge
  # ADDS the widened group beside a stale one instead of migrating it, so a merge here would test
  # the two-group state, which is a different fact.
  sed -i 's/"matcher": "Workflow"/"matcher": "Workflow|Agent"/' .claude/settings.json
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       agent-cap'; } \
    && ck "AC7b the widened matcher -> ok, exit 0" 1 || ck "AC7b the widened matcher -> ok, exit 0" 0
  # AC7d — THE --only BYPASS, and the arm that should have landed with the guard. `--only=<rule>`
  # narrows agent-cap to one rule, so a wired command carrying `--only=join` turns the three cap
  # rules off with no diff and a hook that still looks wired. The guard's FIRST spelling bounded
  # every character class with [^"]*, which cannot cross the escaped quote this settings.json
  # actually ships, so it matched nothing and printed `ok` over a live bypass — a check that could
  # not fail, guarding a bypass the same build introduced. This arm fails against that spelling.
  sed -i 's|agent-cap\.js\\"|agent-cap.js\\" --only=join|' .claude/settings.json
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  agent-cap' \
      && printf '%s' "$out" | grep -q -- '--only'; } \
    && ck "AC7d a wired command carrying --only -> UNWIRED" 1 \
    || ck "AC7d a wired command carrying --only -> UNWIRED" 0
  # ...and it goes back to ok when the flag leaves. Without this half the arm is satisfied by a
  # checker that denies every wired command there is.
  sed -i 's| --only=join||' .claude/settings.json
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       agent-cap'; } \
    && ck "AC7d the flag removed -> ok, exit 0" 1 || ck "AC7d the flag removed -> ok, exit 0" 0
  cleanup
else
  echo "skip agent-cap cases — settings-merge.py not found next to script"
fi

# AC13 — the scratch-guard arm, FOUR states in one repo. Written like the recall arm rather than the
# agent-cap one because this arm reads marker/matcher/hook_path from the shipped fragment, so a
# fixture that hardcodes them would be testing a second spelling of the contract instead of the one
# the kit declares. Unlike recall the guard is NOT an opt-in, so a present-but-unwired hook is a real
# UNWIRED and an absent hook file is "kit not adopted here".
SGFRAG="$ROOT_ABS/$HOOKS_DIR/scratch-guard.fragment.json"
if [ -f "$SGFRAG" ] && [ -f "$SMERGE" ]; then
  newrepo; mkdir -p $KIT_REL/${HOOKS} $KIT_REL/${MEMORY_RECALL} .claude/hooks
  cp "$SMERGE" ${KP}settings-merge.py
  cp "$SGFRAG" $KIT_REL/${HOOKS}/scratch-guard.fragment.json
  git config core.hooksPath .githooks    # isolate: hooks wired, so only scratch-guard can move the exit

  # 13a — fragment shipped, hook not installed, nothing in settings: NOT adopted, must not gate.
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     scratch'; } \
    && ck "AC13a fragment present, hook absent -> skip, exit 0" 1 \
    || ck "AC13a fragment present, hook absent -> skip, exit 0" 0

  # 13b — hook installed but nothing in settings.json: the dormant-guard state, and the whole reason
  # this arm exists. A guard that is silent because it is unwired looks exactly like one that passed.
  # The stub goes where the FRAGMENT declares the hook, not at `.claude/hooks/`.
  # TOOL-dRetiredFork-14 moved the shipped copy under the kit directory, so a fixture that
  # keeps installing into `.claude/hooks/` is testing a layout the kit no longer produces --
  # the arm then reports "not adopted" and the state it exists to catch goes ungraded.
  printf '// stub\n' > $KIT_REL/${HOOKS}/scratch-guard.js
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  scratch'; } \
    && ck "AC13b hook present, unwired -> UNWIRED, exit 1" 1 \
    || ck "AC13b hook present, unwired -> UNWIRED, exit 1" 0
  chk --session >/dev/null; [ "$?" = 0 ] \
    && ck "AC13b --session exits 0 despite scratch-guard unwired" 1 \
    || ck "AC13b --session exits 0 despite scratch-guard unwired" 0

  # 13c — THE STALE MATCHER. Wired under `Bash` alone: the state where the same write through the
  # PowerShell surface meets no rule at all. A file-wide grep for the marker reports ok here, which
  # is why the arm reads the matcher and why this fixture is written directly rather than merged —
  # settings-merge ADDS a group beside a stale one instead of migrating it.
  cat > .claude/settings.json <<'JSON'
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "node \"${CLAUDE_PROJECT_DIR}/{KP}{HOOKS}/scratch-guard.js\""
          }
        ]
      }
    ]
  }
}
JSON
  sed -i "s#{KP}#${KP}#; s#{HOOKS}#${HOOKS}#" .claude/settings.json   # the quoted heredoc cannot expand either
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  scratch' \
      && printf '%s' "$out" | grep -q "wired under matcher 'Bash'"; } \
    && ck "AC13c a stale Bash-only matcher -> UNWIRED naming the value found" 1 \
    || ck "AC13c a stale Bash-only matcher -> UNWIRED naming the value found" 0

  # 13d — and the declared matcher reads ok. Without this half the arm is satisfied by a checker that
  # denies every matcher there is.
  rm -f .claude/settings.json
  "$py" ${KP}settings-merge.py --fragment $KIT_REL/${HOOKS}/scratch-guard.fragment.json >/dev/null 2>&1
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       scratch'; } \
    && ck "AC13d the fragment's own matcher -> ok, exit 0" 1 \
    || ck "AC13d the fragment's own matcher -> ok, exit 0" 0
  cleanup
else
  echo "skip scratch-guard cases — fragment or settings-merge.py not found next to script"
fi

# AC8 — the memory-recall recall-opened arm, all SIX states in one repo. The hook is copied only
# under `adopt-memory-recall.sh --with-hook`, so an ABSENT hook file is a TRUE signal and must print
# a skip: mirroring the agent-cap arm literally would print a permanent false UNWIRED in the repo
# that runs check-wiring.sh as its own SessionStart hook. The fragment is resolved the way the arm
# itself resolves it, so this test works in both layouts (adopter: <root>/memory-recall/).
FRAG=""; for c in "$ROOT_ABS/$MEMORY_RECALL_DIR/recall-opened.fragment.json"; do
  [ -f "$c" ] && { FRAG="$c"; break; }
done
if [ -f "$SMERGE" ] && [ -n "$FRAG" ]; then
  newrepo
  git config core.hooksPath .githooks        # isolate: hooks wired, so only the recall arm can be unwired
  # THE CHECKER'S OWN PREFIX, not the root: the arm probes the receipt and ${KP}${MEMORY_RECALL}/, and the
  # bare root rung that used to follow them is gone (TOOL-aRepatriatedFork-24 S8), so a fixture laid
  # at the root under a checker at another prefix is the mixed layout that now SKIPS by name.
  rk=${KP}${MEMORY_RECALL}
  mkdir -p ${KIT_REL:-.} "$rk" .claude/hooks; cp "$SMERGE" ${KP}settings-merge.py

  # state 1 — kit not adopted (no fragment anywhere) -> skip, exit 0
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     recall' && printf '%s' "$out" | grep -q 'kit not adopted'; } \
    && ck "AC8 recall kit absent -> skip, exit 0" 1 || ck "AC8 recall kit absent -> skip, exit 0" 0

  # state 2 — kit adopted, hook opt-in NOT taken -> skip, exit 0 (never UNWIRED)
  cp "$FRAG" "$rk/recall-opened.fragment.json"
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     recall' && printf '%s' "$out" | grep -q 'opt-in not taken'; } \
    && ck "AC8 recall opt-in not taken -> skip, exit 0" 1 || ck "AC8 recall opt-in not taken -> skip, exit 0" 0

  # state 3 — hook file present but no settings block -> UNWIRED, exit 1; --session still exits 0
  # The stub goes where the FRAGMENT declares the hook, not at `.claude/hooks/`.
  # TOOL-dRetiredFork-14 moved the shipped copy under the kit directory, so a fixture that
  # keeps installing into `.claude/hooks/` is testing a layout the kit no longer produces --
  # the arm then reports "not adopted" and the state it exists to catch goes ungraded.
  printf '// stub\n' > "$rk/recall-opened.js"
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  recall'; } \
    && ck "AC8 recall hook present, unmerged -> UNWIRED, exit 1" 1 || ck "AC8 recall hook present, unmerged -> UNWIRED, exit 1" 0
  chk --session >/dev/null; [ "$?" = 0 ] && ck "AC6 --session exit 0 despite recall unwired" 1 || ck "AC6 --session exit 0 despite recall unwired" 0

  # state 3b — the SAME state with NO settings-merge.py anywhere: still UNWIRED, still exit 1.
  # This is the adopter layout the runbook produced before the delivery step existed, where the arm
  # used to print `skip … cannot verify` and exit 0 on the state the doc calls the one bad state.
  rm -f ${KP}settings-merge.py
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  recall'; } \
    && ck "AC8 recall unmerged, no settings-merge.py -> UNWIRED, exit 1" 1 || ck "AC8 recall unmerged, no settings-merge.py -> UNWIRED, exit 1" 0
  cp "$SMERGE" ${KP}settings-merge.py

  # state 4 — merged into settings.json -> ok, exit 0
  "$py" ${KP}settings-merge.py --fragment "$rk/recall-opened.fragment.json" >/dev/null 2>&1
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       recall'; } \
    && ck "AC8 recall merged -> ok, exit 0" 1 || ck "AC8 recall merged -> ok, exit 0" 0

  # state 5 — settings still dispatch the hook, the script is gone: UNWIRED, exit 1. Reachable from
  # WIRE §3c step 4 (two separate commands) in reverse order, and from any later loss of the
  # untracked hook file; Claude Code then runs `node` against nothing on every Read.
  rm -f "$rk/recall-opened.js"
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  recall' && printf '%s' "$out" | grep -q 'is missing'; } \
    && ck "AC8 recall wired but script gone -> UNWIRED, exit 1" 1 || ck "AC8 recall wired but script gone -> UNWIRED, exit 1" 0

  # state 6 — TOOL-aRepatriatedFork-36: the SAME state, but the target keeps its own hook at
  # `.claude/hooks/` and declared it `[[own]]`, so the receipt carries an `adopter-owned` row with the
  # source of gov's engine row at the fragment's path. The fragment resolves to the owned copy, both
  # readers agree on it, and the arm is ok. Without the seam this is state 5's false UNWIRED.
  src6="$KIT_REL/${MEMORY_RECALL}/recall-opened.js"   # the receipt's gov-side source, any string both rows share
  write_owned_receipt() {  # <owned path, raw JSON string body> [role] -> a pretty receipt: gov's engine row, then the owned row
    printf '{\n  "files": [\n    {\n      "path": "%s",\n      "role": "engine",\n      "source": "%s"\n    },\n    {\n      "path": "%s",\n      "role": "%s",\n      "source": "%s"\n    }\n  ]\n}\n' \
      "$rk/recall-opened.js" "$src6" "$1" "${2:-adopter-owned}" "$src6" > .governance/install.json
  }
  mkdir -p .governance; printf '// the target'"'"'s own\n' > .claude/hooks/recall-opened.js
  write_owned_receipt .claude/hooks/recall-opened.js
  got=$(bash "$SCRIPT" --resolve-fragment "$rk/recall-opened.fragment.json" 2>/dev/null)
  ck "AC8 an adopter-owned receipt row moves the resolved hook to the target's copy" "$([ "$got" = .claude/hooks/recall-opened.js ] && echo 1 || echo 0)"
  got2=$("$py" ${KP}settings-merge.py --resolve-fragment "$rk/recall-opened.fragment.json" 2>/dev/null)
  ck "AC8 ...and settings-merge.py resolves the same path" "$([ "$got2" = "$got" ] && echo 1 || echo 0)"
  # I1 (round-1 fold): settings.json still runs the KIT copy state 4 merged, which is not the copy
  # the declaration resolves to, so the arm names the mismatch instead of reading the marker as ok.
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  recall    — settings.json runs a recall-opened hook, but not the resolved copy'; } \
    && ck "AC8 an entry running another copy than the resolved one -> UNWIRED, exit 1" 1 || ck "AC8 an entry running another copy than the resolved one -> UNWIRED, exit 1" 0
  # ...and one merge REWRITES that entry in place to the owned copy, after which the arm is ok.
  "$py" ${KP}settings-merge.py --fragment "$rk/recall-opened.fragment.json" >/dev/null 2>&1
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       recall' \
      && [ "$(grep -c 'recall-opened.js' .claude/settings.json)" = 1 ]; } \
    && ck "AC8 recall hook kept elsewhere and declared owned -> ok, exit 0, one entry" 1 || ck "AC8 recall hook kept elsewhere and declared owned -> ok, exit 0, one entry" 0
  # I1, BOTH COPIES PRESENT: gov's copy lands beside the kit, settings.json runs the out-of-kit one,
  # and nothing declares it. The retired marker join printed `ok` here, and kept printing it after
  # the copy that actually runs was deleted.
  printf '// gov'"'"'s\n' > "$rk/recall-opened.js"
  printf '{\n  "files": [\n    {\n      "path": "%s",\n      "role": "engine",\n      "source": "%s"\n    }\n  ]\n}\n' \
    "$rk/recall-opened.js" "$src6" > .governance/install.json
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  recall    — settings.json runs a recall-opened hook, but not the resolved copy'; } \
    && ck "AC8 both copies present, the undeclared one wired -> UNWIRED, exit 1" 1 || ck "AC8 both copies present, the undeclared one wired -> UNWIRED, exit 1" 0
  mv .claude/hooks/recall-opened.js .claude/hooks/held.js
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  recall'; } \
    && ck "AC8 ...and still UNWIRED once the copy that runs is deleted" 1 || ck "AC8 ...and still UNWIRED once the copy that runs is deleted" 0
  mv .claude/hooks/held.js .claude/hooks/recall-opened.js
  # S1-S5 (round-1 fold): the receipt spellings the retired awk reader split from settings-merge's.
  # Each bad owned row is REFUSED by the one reader, and check-wiring reports that refusal; each
  # good spelling resolves to the owned copy in both CLIs. The rows are RAW JSON bodies, so a
  # backslash or `\u` reaches the parser undecoded.
  for bad in '..\\..\\other\\recall-opened.js' '.claude/caf\u00e9/recall-opened.js' '.claude/h\"x/recall-opened.js' \
             '../other/recall-opened.js' '/abs/recall-opened.js' 'C:/abs/recall-opened.js' \
             'h/$(touch PWNED)/recall-opened.js' '.claude/hooks/my-recall.js'; do
    write_owned_receipt "$bad"
    bash "$SCRIPT" --resolve-fragment "$rk/recall-opened.fragment.json" >/dev/null 2>&1; r1=$?
    "$py" ${KP}settings-merge.py --resolve-fragment "$rk/recall-opened.fragment.json" >/dev/null 2>&1; r2=$?
    ck "AC8 an owned row of $bad is refused by both CLIs" "$([ "$r1" != 0 ] && [ "$r2" != 0 ] && echo 1 || echo 0)"
  done
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q "UNWIRED  recall    — .*refused"; } \
    && ck "AC8 ...and the recall arm reports the last refusal as UNWIRED, exit 1" 1 || ck "AC8 ...and the recall arm reports the last refusal as UNWIRED, exit 1" 0
  write_owned_receipt .claude/hooks/recall-opened.js '\u0061dopter-owned'
  got=$(bash "$SCRIPT" --resolve-fragment "$rk/recall-opened.fragment.json" 2>/dev/null)
  ck "AC8 a \\u-escaped owned role still joins, through the one reader" "$([ "$got" = .claude/hooks/recall-opened.js ] && echo 1 || echo 0)"
  write_owned_receipt .claude/hooks/recall-opened.js; tr -d ' \n' < .governance/install.json > .governance/c.json && mv .governance/c.json .governance/install.json
  got=$(bash "$SCRIPT" --resolve-fragment "$rk/recall-opened.fragment.json" 2>/dev/null)
  ck "AC8 a compact one-line receipt joins the same" "$([ "$got" = .claude/hooks/recall-opened.js ] && echo 1 || echo 0)"
  rm -f "$rk/recall-opened.js"
  # its control: the owned row alone, with no engine row at the fragment's path, joins to nothing.
  printf '{\n  "files": [\n    {\n      "path": "%s",\n      "role": "adopter-owned",\n      "source": "%s"\n    }\n  ]\n}\n' \
    .claude/hooks/recall-opened.js "$src6" > .governance/install.json
  got=$(bash "$SCRIPT" --resolve-fragment "$rk/recall-opened.fragment.json" 2>/dev/null)
  ck "AC8 control — with no engine row at the fragment's path the hook stays beside the fragment" "$([ "$got" = "$rk/recall-opened.js" ] && echo 1 || echo 0)"
  rm -rf .governance .claude/hooks/recall-opened.js
  cleanup
else
  echo "skip recall cases — settings-merge.py or recall-opened.fragment.json not found"
fi

# AC14 — the orientation-card arm (TOOL-aReplayedCard-2), SIX states in one repo, plus the
# `--resolve-fragment` print verb. The two fragments are `{here}`-shaped: they sit beside the
# kickoff engine, which is `kind = "flat"` and ships to `{prefix}/`, so the fixture installs them
# at `$KIT_REL/` next to a stub engine — the adopter layout — and reads the matchers back from the
# fragments themselves, never from a second spelling here.
CARDFRAG=""; REPLAYFRAG=""
for c in "$HERE/orientation-card.fragment.json" "$REPO/skills/session-kickoff/orientation-card.fragment.json"; do
  [ -f "$c" ] && { CARDFRAG="$c"; REPLAYFRAG="$(dirname "$c")/orientation-replay.fragment.json"; break; }
done
if [ -f "$SMERGE" ] && [ -n "$CARDFRAG" ] && [ -f "$REPLAYFRAG" ]; then
  newrepo
  git config core.hooksPath .githooks        # isolate: hooks wired, so only the card arm can move the exit
  mkdir -p $KIT_REL .claude; cp "$SMERGE" $KIT_REL/settings-merge.py

  # state 1 — no fragment anywhere -> skip, exit 0
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     card' && printf '%s' "$out" | grep -q 'does not ship'; } \
    && ck "AC14 card fragments absent -> skip, exit 0" 1 || ck "AC14 card fragments absent -> skip, exit 0" 0

  # state 2 — fragments shipped, engine absent -> skip (not adopted), exit 0
  cp "$CARDFRAG" $KIT_REL/orientation-card.fragment.json
  cp "$REPLAYFRAG" $KIT_REL/orientation-replay.fragment.json
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     card' && printf '%s' "$out" | grep -q 'not adopted'; } \
    && ck "AC14 fragments present, engine absent -> skip, exit 0" 1 || ck "AC14 fragments present, engine absent -> skip, exit 0" 0

  # the print verb: `{here}` is the fragment's OWN directory, `{kit}` two up, and a fragment with
  # no hook_path is a non-zero answer rather than an empty line that reads as a root path.
  got=$(bash "$SCRIPT" --resolve-fragment $KIT_REL/orientation-card.fragment.json 2>/dev/null)
  ck "AC14 --resolve-fragment expands {here} to the fragment's directory" "$([ "$got" = "$KIT_REL/manifest-check.sh" ] && echo 1 || echo 0)"
  mkdir -p $KIT_REL/${HOOKS}; printf '{"hook_path": "{kit}/hooks/x.js", "marker": "x.js", "matcher": "M", "event": "E", "name": "x"}\n' > $KIT_REL/${HOOKS}/x.fragment.json
  got=$(bash "$SCRIPT" --resolve-fragment $KIT_REL/${HOOKS}/x.fragment.json 2>/dev/null)
  ck "AC14 --resolve-fragment expands {kit} two directories up" "$([ "$got" = "$KIT_REL/${HOOKS}/x.js" ] && echo 1 || echo 0)"
  printf '{"marker": "x.js"}\n' > $KIT_REL/${HOOKS}/nohook.fragment.json
  got=$(bash "$SCRIPT" --resolve-fragment $KIT_REL/${HOOKS}/nohook.fragment.json 2>/dev/null); rc=$?
  ck "AC14 --resolve-fragment refuses a fragment with no hook_path" "$([ "$rc" != 0 ] && [ -z "$got" ] && echo 1 || echo 0)"
  rm -rf $KIT_REL/${HOOKS}

  # state 3 — engine present, nothing in settings.json -> UNWIRED, exit 1; --session still exits 0
  printf '#!/usr/bin/env bash\nexit 0\n' > $KIT_REL/manifest-check.sh
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  card' && printf '%s' "$out" | grep -q 'orientation-card entry (--write)'; } \
    && ck "AC14 engine present, unmerged -> UNWIRED naming the entry, exit 1" 1 || ck "AC14 engine present, unmerged -> UNWIRED naming the entry, exit 1" 0
  chk --session >/dev/null; [ "$?" = 0 ] && ck "AC6 --session exit 0 despite card unwired" 1 || ck "AC6 --session exit 0 despite card unwired" 0

  # state 4 — THE NARROWED MATCHER (AC7). The writer is right; the replay sits under `resume`
  # alone, so the card is gone after the first compaction while the file reads as wired to a
  # marker grep. Written by hand, because the merger would re-match it.
  cat > .claude/settings.json <<JSON
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|clear",
        "hooks": [
          {
            "type": "command",
            "command": "bash \\"\${CLAUDE_PROJECT_DIR}/$KIT_REL/manifest-check.sh\\" --card --write"
          }
        ]
      },
      {
        "matcher": "resume",
        "hooks": [
          {
            "type": "command",
            "command": "bash \\"\${CLAUDE_PROJECT_DIR}/$KIT_REL/manifest-check.sh\\" --card --replay"
          }
        ]
      }
    ]
  }
}
JSON
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  card' \
      && printf '%s' "$out" | grep -q "wired under matcher 'resume', not 'resume|compact'"; } \
    && ck "AC14 a replay matcher lacking compact -> UNWIRED naming compact" 1 \
    || ck "AC14 a replay matcher lacking compact -> UNWIRED naming compact" 0
  ck "AC14 ...and the correctly wired writer does not print ok on its own" \
    "$(printf '%s' "$out" | grep -q 'ok       card' && echo 0 || echo 1)"

  # state 5 — both merged by the merger itself -> ok, exit 0. This is the arm that reds when
  # `matchers_of` greps a dash-leading marker without `-e`: grep exits 2 on `--write` as an option.
  rm -f .claude/settings.json
  "$py" $KIT_REL/settings-merge.py --fragment $KIT_REL/orientation-card.fragment.json >/dev/null 2>&1
  "$py" $KIT_REL/settings-merge.py --fragment $KIT_REL/orientation-replay.fragment.json >/dev/null 2>&1
  out=$(chk --check); rc=$?
  { [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       card' \
      && printf '%s' "$out" | grep -q -- "--write at 'startup|clear', --replay at 'resume|compact'"; } \
    && ck "AC14 both merged -> ok naming both matchers, exit 0" 1 || ck "AC14 both merged -> ok naming both matchers, exit 0" 0

  # state 6 — the writer alone merged: half a wiring is UNWIRED naming the half that is missing.
  rm -f .claude/settings.json
  "$py" $KIT_REL/settings-merge.py --fragment $KIT_REL/orientation-card.fragment.json >/dev/null 2>&1
  out=$(chk --check); rc=$?
  { [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'orientation-replay entry (--replay) is not in settings.json'; } \
    && ck "AC14 writer merged, replay not -> UNWIRED naming the replay" 1 || ck "AC14 writer merged, replay not -> UNWIRED naming the replay" 0
  cleanup
else
  echo "skip card cases — settings-merge.py or the orientation fragments not found"
fi

# AC9 — the eol arm: detect in --check, repair in --fix, and never reach past its bound.
# THE BOUND IS THE POINT, and this fixture uses the BROADEST attribute spelling an adopter might
# reasonably write. An earlier cut pinned only `.claude/**/*.md`, which pre-narrowed the population
# and made "stays inside its bound" green for the fixture's reasons rather than the gate's. Under
# `* text=auto eol=lf` the first implementation rewrote `.claude/settings.json` and stripped CR bytes
# out of the middle of a PNG — md5 changed, reported as "fixed".
newrepo
mkdir -p .claude/skills/x memory
printf '* text=auto eol=lf\n' > .gitattributes
printf 'a\nb\n' > .claude/skills/x/SKILL.md              # a rendered Skill: the whole population
printf 'a\nb\n' > memory/NOTES.md                        # outside .claude/ entirely
printf '{\n  "hooks": {}\n}\n' > .claude/settings.json    # under .claude/, pinned, NOT a Skill
printf 'PNG\r\n\032\r\nIDAT\n' > .claude/skills/x/logo.png   # binary bytes a `tr -d` would eat
git add -A; git commit -q -m eolbase
git config core.hooksPath .githooks                      # isolate: only the eol arm can be unwired
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       eol'; } \
  && ck "AC9 clean LF tree -> ok" 1 || ck "AC9 clean LF tree -> ok" 0
# the checkout defect, reproduced: CRLF in the worktree while the index stays normalised, so
# `git status` is CLEAN and only a byte-comparing gate ever notices.
printf 'a\r\nb\r\n' > .claude/skills/x/SKILL.md
printf 'a\r\nb\r\n' > memory/NOTES.md
printf '{\r\n  "hooks": {}\r\n}\r\n' > .claude/settings.json
cp .claude/skills/x/logo.png "$D/logo.before"

# THE INVISIBILITY, measured rather than asserted from the trap note. `git diff` reports NO content
# difference on the pinned file — the clean filter normalises, so there is nothing to commit — while
# the bytes on disk are CRLF. (`git status --porcelain` does list it: that is the stat cache, not a
# content verdict, and the two disagree here. The trap note's "git status stays clean" was the
# looser half of the observation; this is the half that actually explains the no-op below.)
{ [ -z "$(git diff --numstat -- .claude/skills/x/SKILL.md)" ]; } \
  && ck "AC9 git sees no content change (the defect reproduces)" 1 \
  || ck "AC9 git sees no content change (the defect reproduces)" 0
# A `git checkout --` remedy is NOT asserted here, and the reason is a measurement rather than a
# preference: on this git it DOES restore the file in this fixture, because status' stat cache flags
# it even though diff sees no content change. The two disagree, so a repair built on `git checkout`
# works or no-ops depending on which of them git consults — the previous build hit the no-op and
# needed `rm` first. Rewriting the bytes is correct in BOTH states, which is why it is what --fix
# does. Do not "simplify" it back.
out=$(chk --check); rc=$?
# REPORTS, does NOT gate. The committed bytes are LF, so nothing in the repository is wrong and
# nothing is dormant — and a consumer that reads the exit status as a refusal (.unattended.conf
# declares this script as its WIRING_CHECK) refused every run in a worktree carrying the artifact.
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'note     eol' && printf '%s' "$out" | grep -q 'SKILL.md'; } \
  && ck "AC9 CRLF on a pinned .claude/ file -> note, exit 0" 1 || ck "AC9 CRLF on a pinned .claude/ file -> note, exit 0" 0
printf '%s' "$out" | grep -q 'UNWIRED  eol' \
  && ck "AC9 the eol arm no longer spells the gating label" 0 || ck "AC9 the eol arm no longer spells the gating label" 1
printf '%s' "$out" | grep -q 'memory/NOTES.md' \
  && ck "AC9 --check stays inside its bound" 0 || ck "AC9 --check stays inside its bound" 1
# THE SIBLING, and without it the arm above is indistinguishable from having DELETED the eol arm:
# a genuinely dormant item in the SAME run, with the same CRLF still present, still gives rc 1 and
# still names itself. `--check` never sets config, so unsetting here does not leak into the arms
# below; it is restored immediately.
git config --unset core.hooksPath
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  hooks' && printf '%s' "$out" | grep -q 'note     eol'; } \
  && ck "AC9 a dormant item in the same run still gates, alongside the note" 1 \
  || ck "AC9 a dormant item in the same run still gates, alongside the note" 0
git config core.hooksPath .githooks
# --session REPORTS; only --fix rewrites. A SessionStart hook editing file bytes unattended is a far
# bigger act than setting an unset git config, which is all --session was ever allowed to do.
chk --session >/dev/null
LC_ALL=C grep -qU $'\r' .claude/skills/x/SKILL.md \
  && ck "AC9 --session reports without rewriting" 1 || ck "AC9 --session reports without rewriting" 0
chk --fix >/dev/null
LC_ALL=C grep -qU $'\r' .claude/skills/x/SKILL.md \
  && ck "AC9 --fix rewrote the pinned file to LF" 0 || ck "AC9 --fix rewrote the pinned file to LF" 1
# ...and everything OUTSIDE the bound is untouched, under the broadest attribute spelling there is.
# A repair that reaches past its population is worse than one that never ran: it rewrites bytes
# nobody asked it to.
LC_ALL=C grep -qU $'\r' memory/NOTES.md \
  && ck "AC9 --fix left the file outside .claude/ alone" 1 || ck "AC9 --fix left the file outside .claude/ alone" 0
LC_ALL=C grep -qU $'\r' .claude/settings.json \
  && ck "AC9 --fix left .claude/settings.json alone" 1 || ck "AC9 --fix left .claude/settings.json alone" 0
cmp -s .claude/skills/x/logo.png "$D/logo.before" \
  && ck "AC9 --fix did not corrupt a binary in the domain" 1 || ck "AC9 --fix did not corrupt a binary in the domain" 0
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       eol'; } \
  && ck "AC9 re-check after --fix -> ok, exit 0" 1 || ck "AC9 re-check after --fix -> ok, exit 0" 0
# A Skill directory whose name carries a SPACE. `xargs` word-split it into two nonexistent paths, the
# population came back empty, and the arm printed a green `skip` over a file with real CRLF in it.
mkdir -p ".claude/skills/my skill"
printf 'a\nb\n' > ".claude/skills/my skill/SKILL.md"
git add -A; git commit -q -m spaced
printf 'a\r\nb\r\n' > ".claude/skills/my skill/SKILL.md"
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'my skill/SKILL.md'; } \
  && ck "AC9 a Skill path with a space is still seen" 1 || ck "AC9 a Skill path with a space is still seen" 0
chk --fix >/dev/null
LC_ALL=C grep -qU $'\r' ".claude/skills/my skill/SKILL.md" \
  && ck "AC9 --fix repairs a spaced path" 0 || ck "AC9 --fix repairs a spaced path" 1
cleanup

# AC9b — no pinned .claude/ path at all: the arm SKIPS rather than reporting a clean bill over an
# empty population, which is the distinction the empty-population guard exists to make.
newrepo
git config core.hooksPath .githooks
out=$(chk --check)
printf '%s' "$out" | grep -q 'skip     eol' \
  && ck "AC9b no eol=lf pin under .claude/ -> skip, not a silent ok" 1 \
  || ck "AC9b no eol=lf pin under .claude/ -> skip, not a silent ok" 0
cleanup

# AC10 — the row-keyed merge driver arm, all NINE states in one repo. A merge DRIVER is per-node
# config while `.gitattributes` is committed, so "declared" and "wired" are different facts and the
# gap between them is silent: git falls back to a line merge, and that line merge is the one that
# duplicates a row. The remedy string is BUILT from the two resolved paths, so this asserts the
# string the arm PRINTS is the string `--fix` SETS — one truth, not two.
#
# The fixture lays a COMPLETE install (driver + shim + resolver + the memory-recall kit the anchor
# grammar is imported from + the conf naming the families), because the arm now RUNS the configured
# command before it says `ok`. A fixture that could not start the driver would turn every green
# below into a green for the fixture's reasons instead of the tool's.
newrepo
git config core.hooksPath .githooks        # isolate: hooks wired, so only the merge arm can be unwired
mkdir -p ${KP}${MT_KIT} ${KP}${LIB} memory/backlog
WANT="bash $KIT_REL/${MT_KIT}/merge-rows.sh %O %A %B %P"

# state 1 — kit not adopted -> skip, exit 0
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     merge' && printf '%s' "$out" | grep -q 'not adopted'; } \
  && ck "AC10 merge driver absent -> skip, exit 0" 1 || ck "AC10 merge driver absent -> skip, exit 0" 0

# state 2 — the driver is present but NO launcher is. git would exec a command that cannot start, and
# a merge driver that cannot start exits non-zero without writing %A: git then reports CONFLICT and
# leaves the path holding OURS-only content with no markers. The remedy has to name the launcher that
# TRAVELS WITH THE KIT, because `<prefix>/lib/pyrun.sh` is gov-internal and an adopter never receives it.
cp "$(src_of "${ROOTPFX}${MT_KIT}/merge-rows.py")" $KIT_REL/${MT_KIT}/merge-rows.py
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'merge-rows.sh beside it'; } \
  && ck "AC10 no launcher -> UNWIRED naming the kit-internal one, exit 1" 1 \
  || ck "AC10 no launcher -> UNWIRED naming the kit-internal one, exit 1" 0

# state 3 — the whole kit is present, but no tracked path declares merge=rows: nothing to wire, so a
# SKIP rather than a permanent false UNWIRED in every repo that carries the kit without the
# attribute. `install_driver` writes the attribute, so it is stripped again for this one state.
install_driver "${KP}"
printf '# nothing declared here\n' > .gitattributes
git add -A; git commit -q -m nodeclare
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     merge' && printf '%s' "$out" | grep -q 'no tracked path declares'; } \
  && ck "AC10 no merge=rows attribute -> skip, exit 0" 1 || ck "AC10 no merge=rows attribute -> skip, exit 0" 0

# state 4 — declared, config unset -> UNWIRED, exit 1, and the remedy carries the BUILT command
printf 'memory/backlog/*.md merge=rows\n' > .gitattributes
git add -A; git commit -q -m attrs
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -qF "$WANT"; } \
  && ck "AC10 declared but unset -> UNWIRED + built remedy, exit 1" 1 || ck "AC10 declared but unset -> UNWIRED + built remedy, exit 1" 0

# state 5 — --fix sets exactly that command; the re-check is ok, exit 0
chk --fix >/dev/null; got=$(git config merge.rows.driver); out=$(chk --check); rc=$?
{ [ "$got" = "$WANT" ] && [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 --fix sets the driver, re-check ok" 1 || ck "AC10 --fix sets the driver, re-check ok" 0
# ...and it is the KIT-INTERNAL launcher that won, not the gov-internal shim. `install_driver` lays
# both, so without this the fallback could silently win everywhere and every arm here would still
# pass — while an adopter, who receives only the kit, got a command naming a file they do not have.
# The pattern sits in a variable so the marked line carries no line continuation — a trailing
# backslash escapes the space before a comment, not the newline, and the break is valid shell.
_want_launcher="${ROOTPFX}${MT_KIT}/merge-rows.sh"   # the kit launcher's own spelling
{ printf '%s' "$got" | grep -q "$_want_launcher" \
  && ! printf '%s' "$got" | grep -q 'pyrun'; } \
  && ck "AC10 the kit launcher wins over the gov-internal shim" 1 \
  || ck "AC10 the kit launcher wins over the gov-internal shim" 0

# state 5b — the config is UNCHANGED and correct, and the driver still cannot START: the resolver
# `pyrun.sh` sources is gone. MEASURED before this arm existed: `ok  merge  — merge.rows.driver
# wired`, and the very next `git merge` printed CONFLICT and left memory/DECISIONS.md holding
# OURS-only content with `grep -c '<<<<<<<'` = 0 and status UU — the incoming row simply absent.
# "Wired" has to mean the command RUNS, so this state must not be green.
# RE-AIMED: the kit-internal launcher carries the resolver INLINE, so removing `<prefix>/lib/` no
# longer breaks it — that decoupling is the whole point of shipping a launcher with the kit. What it
# still cannot survive is a driver that will not parse. Removing the FILE would trip the
# not-adopted probe one test earlier and never reach this arm, so the content is what breaks.
cp $KIT_REL/${MT_KIT}/merge-rows.py $KIT_REL/${MT_KIT}/merge-rows.py.away
printf 'this is not python(
' > ${KP}${MT_KIT}/merge-rows.py
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'cannot merge'; } \
  && ck "AC10 driver cannot start (unparseable driver) -> UNWIRED, exit 1" 1 || ck "AC10 driver cannot start (unparseable driver) -> UNWIRED, exit 1" 0
# ...and --fix must not DECLARE a broken driver wired either. Wiring a command that cannot run is
# strictly worse than leaving it unset: unset falls back to git's line merge, wired-and-broken is
# the silent take-ours above.
git config --unset merge.rows.driver
chk --fix >/dev/null; got=$(git config merge.rows.driver 2>/dev/null || true)
[ -z "$got" ] && ck "AC10 --fix refuses to wire a driver that cannot run" 1 || ck "AC10 --fix refuses to wire a driver that cannot run" 0
mv -f $KIT_REL/${MT_KIT}/merge-rows.py.away $KIT_REL/${MT_KIT}/merge-rows.py
chk --fix >/dev/null; out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 restoring the driver goes green again" 1 || ck "AC10 restoring the driver goes green again" 0

# state 5b2 — the smoke run itself cannot run. A verifier that could not verify must not print the
# same `ok` as one that did: this file already deleted a `cannot verify` skip from the recall arm for
# reporting exit 0 on the one state the runbook calls bad, and the new dependency on a temp dir is a
# second way into that state. TMPDIR points somewhere that does not exist, so mktemp -d fails.
out=$(TMPDIR=/nonexistent-check-wiring-tmp bash "$SCRIPT" --check 2>/dev/null); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'cannot verify'; } \
  && ck "AC10 unverifiable (no temp dir) -> UNWIRED, not a silent ok" 1 || ck "AC10 unverifiable (no temp dir) -> UNWIRED, not a silent ok" 0

# state 5c — the driver STARTS but cannot key a row: the sibling memory-recall kit that owns the
# anchor grammar is gone, so the deferred import raises and the fail-closed wrapper writes a conflict
# on every governed-index merge, forever. Loud rather than destructive, but the arm's own header
# claims it turns "declared" into "wired"; a driver that conflicts unconditionally is not wired.
mv ${KP}${MEMORY_RECALL} ${KP}${MEMORY_RECALL}.away
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'cannot merge'; } \
  && ck "AC10 driver cannot key rows (no memory-recall) -> UNWIRED, exit 1" 1 || ck "AC10 driver cannot key rows (no memory-recall) -> UNWIRED, exit 1" 0
mv ${KP}${MEMORY_RECALL}.away ${KP}${MEMORY_RECALL}
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 restoring the grammar kit goes green again" 1 || ck "AC10 restoring the grammar kit goes green again" 0

# state 5d — the driver STARTS, the smoke fixture merges CLEANLY, and the driver is still inert on
# the only files it is wired to: one token of drift in `.memory-tree.conf` FAMILIES
# (`tooling:TOOL` -> `tooling:TOOLS`) renames the family every landed row LEADS with. The smoke
# fixture is BUILT from the conf, so it renames with it and stays green — MEASURED: the arm printed
# `ok  merge  — merge.rows.driver wired` while the driver keyed ZERO rows and every governed
# append-collision conflicted forever. So the arm asks the declared indexes directly. This state is
# also the liveness proof for that harvest: it can only red if `install_driver`'s landed row is there
# and really is being read.
sed -i.bak 's/tooling:TOOL"/tooling:TOOLS"/' .memory-tree.conf && rm -f .memory-tree.conf.bak
grep -q 'tooling:TOOLS' .memory-tree.conf || ck "AC10 family-drift fixture: the conf edit did not apply" 0
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'does not declare TOOL'; } \
  && ck "AC10 conf renames the family the indexes use -> UNWIRED, exit 1" 1 || ck "AC10 conf renames the family the indexes use -> UNWIRED, exit 1" 0
sed -i.bak 's/tooling:TOOLS"/tooling:TOOL"/' .memory-tree.conf && rm -f .memory-tree.conf.bak
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 restoring the declared family goes green again" 1 || ck "AC10 restoring the declared family goes green again" 0

# state 5e — THE INERTNESS CHANNEL THE TWO-PLANE DRIVER OPENS, and state 5d cannot reach it.
#
# 5d drifts FAMILIES, and the smoke fixture is built FROM the conf, so its rows rename with it and
# key normally under exactly the drift being applied — 100% keyed. What reds 5d is the pre-existing
# harvest of the LANDED row's prefix, and control only reaches that harvest because the smoke
# PASSED. So 5d is a regression guard on a different arm and proves nothing about the keyed count.
#
# The state that does: a grammar that IMPORTS cleanly and keys NOTHING. Under the retired driver an
# unkeyable row was content, so the append collision conflicted and inert was loud. Under the two
# planes it is a hashed ROW, reconciliation rule 3 resolves the collision, and all twelve ids land
# exactly once at rc 0 — better than `git merge-file`, which refuses the same three blobs, while the
# id-level no-duplicate guarantee is entirely off. Every other assertion in the arm is green over it.
# `anchor_at` is REDEFINED rather than deleted, so the import still succeeds and the fail-closed
# handler is not what answers: this state is about a grammar that works and recognises nothing.
printf '\n\ndef anchor_at(line, g=None):\n    return None\n' >> $KIT_REL/${MEMORY_RECALL}/extract.py
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'UNWIRED  merge' && printf '%s' "$out" | grep -q 'HASHED'; } \
  && ck "AC10 a grammar that keys NOTHING -> UNWIRED naming the hashed count, exit 1" 1 || ck "AC10 a grammar that keys NOTHING -> UNWIRED naming the hashed count, exit 1" 0
# ...and the state really is the quiet one it claims to be: with the keyed-count assertion removed
# from the checker, this same tree passes every other assertion the arm makes. Proved by running the
# smoke's own three-way by hand and observing a clean, complete, id-preserving merge.
Q=$(mktemp -d); printf -- '- TOOL-001 | base\n' > "$Q/o"
printf -- '- TOOL-001 | base\n- TOOL-002 | ours\n' > "$Q/a"; printf -- '- TOOL-001 | base\n- TOOL-003 | theirs\n' > "$Q/b"
qerr=$(bash $KIT_REL/${LIB}/pyrun.sh $KIT_REL/${MT_KIT}/merge-rows.py "$Q/o" "$Q/a" "$Q/b" x 2>&1 >/dev/null); qrc=$?
qn=0; for i in 001 002 003; do [ "$(grep -c -- "^- TOOL-$i |" "$Q/a")" = 1 ] && qn=$((qn+1)); done
{ [ "$qrc" = 0 ] && [ "$qn" = 3 ] && printf '%s' "$qerr" | grep -q '(0 keyed, 3 hashed)'; } \
  && ck "AC10 the dead grammar still merges cleanly (0 keyed, 3 hashed) — the channel is real and quiet" 1 \
  || ck "AC10 the dead grammar still merges cleanly (0 keyed, 3 hashed) — the channel is real and quiet [rc=$qrc ids=$qn err=$qerr]" 0
rm -rf "$Q"
git checkout -q -- $KIT_REL/${MEMORY_RECALL}/extract.py 2>/dev/null || true
if grep -q 'def anchor_at(line, g=None):' $KIT_REL/${MEMORY_RECALL}/extract.py; then
  cp "$(src_of "${ROOTPFX}${MEMORY_RECALL}/extract.py")" $KIT_REL/${MEMORY_RECALL}/extract.py
fi
out=$(chk --check); rc=$?
{ [ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'ok       merge'; } \
  && ck "AC10 restoring the real grammar goes green again" 1 || ck "AC10 restoring the real grammar goes green again" 0

# state 6 — a value somebody else set is REPORTED and never clobbered (the check_hooks rule)
git config merge.rows.driver 'bash vendor/other-driver.sh %O %A %B %P'
out=$(chk --check); rc=$?
{ [ "$rc" = 1 ] && printf '%s' "$out" | grep -q 'NOT overwriting'; } \
  && ck "AC10 a foreign driver -> UNWIRED, exit 1" 1 || ck "AC10 a foreign driver -> UNWIRED, exit 1" 0
before=$(git config merge.rows.driver); chk --fix >/dev/null; after=$(git config merge.rows.driver)
{ [ "$after" = "$before" ] && [ "$after" != "$WANT" ]; } \
  && ck "AC10 --fix never clobbers a set driver" 1 || ck "AC10 --fix never clobbers a set driver" 0

# state 7 — --session wires the unset case too. Setting a repo-local config is exactly the class of
# act --session exists for; the eol arm's session exemption is not copied because that one rewrites
# file bytes.
hl="$(git rev-parse --path-format=absolute --git-common-dir)/health.log"
n0=$(awk -F'\t' '$3 == "merge-driver-set"' "$hl" 2>/dev/null | wc -l | tr -d ' ')
git config --unset merge.rows.driver
chk --session >/dev/null; rc=$?; got=$(git config merge.rows.driver)
{ [ "$rc" = 0 ] && [ "$got" = "$WANT" ]; } \
  && ck "AC10 --session wires the driver + exit 0" 1 || ck "AC10 --session wires the driver + exit 0" 0
# TOOL-aGraftedHelix-8 AC4, the merge arm: one merge-driver-set line naming the session mode, and a
# second --session over the wired driver appends none.
n1=$(awk -F'\t' '$3 == "merge-driver-set"' "$hl" 2>/dev/null | wc -l | tr -d ' ')
last=$(awk -F'\t' '$3 == "merge-driver-set" { d = $4 } END { print d }' "$hl" 2>/dev/null)
chk --session >/dev/null
n2=$(awk -F'\t' '$3 == "merge-driver-set"' "$hl" 2>/dev/null | wc -l | tr -d ' ')
ck "U8 AC4 --session's merge auto-wire appends one merge-driver-set line, and a second run none" \
   "$([ "$n1" = "$((n0 + 1))" ] && [ "$n2" = "$n1" ] && [ "$last" = "merge.rows.driver · mode session" ] && echo 1 || echo 0)"
cleanup

# AC11 — the `merge=rows` ATTRIBUTE, asserted against THIS repo's REAL tree.
# The attribute is what actually ROUTES a conflict through the driver. Without it git falls back to
# its built-in line merge — the one measured introducing a duplicate id in 147 of 151 historical
# DECISIONS.md conflicts — and nothing said so: deleting both `.gitattributes` lines left every leg
# on the bar green, the driver's own replay test included, because that test writes its OWN
# `.gitattributes` inside a scratch repo and therefore proves the driver works against an attribute
# it invented rather than against this repo's.
#
# WHY THIS FILE and not the driver's replay test: that file owns the driver's BEHAVIOUR over fixtures
# it controls, and every fixture it merges is one it wrote. This file owns whether the wiring in the
# real tree is real — the question every arm above asks — and it already holds `$REPO` for exactly
# that reason. It is also already a gate leg, so the attribute becomes gated without a new leg.
#
# Read through `git check-attr`, never by grepping `.gitattributes`: attributes come from several
# files and git is the only authority on the answer. That is the same rule check_eol and
# check_merge_rows already follow, and the rule the end-to-end merge fixture applies to its own tree.
cd "$REPO"
ATTR_DRV=""; for c in "$ROOT_ABS/$MT_KIT_DIR/merge-rows.py"; do
  [ -f "$c" ] && { ATTR_DRV="$c"; break; }
done
if [ -z "$ATTR_DRV" ]; then
  echo "skip merge-attribute case — the row-keyed driver is not installed in this repo"
else
  MROOT=$(sed -n 's/^[[:space:]]*MEMORY_ROOT=//p' "$REPO/.memory-tree.conf" 2>/dev/null \
          | head -1 | tr -d '"'"'"'\r')
  [ -n "$MROOT" ] || MROOT=memory
  POP=$(git ls-files -- "$MROOT/DECISIONS.md" "$MROOT/backlog/*.md" | grep . || true)
  # POP GUARD. "Every governed index declares merge=rows" is vacuously true over zero of them, and a
  # gate that passes by finding nothing is the failure class this repo catalogues. The population is
  # asserted non-empty FIRST, and it is derived from the conf rather than listed here, so a
  # MEMORY_ROOT rename reds instead of quietly emptying the set.
  n=$(printf '%s\n' "$POP" | grep -c . || true)
  [ "${n:-0}" -ge 2 ] && ck "AC11 the governed indexes exist ($n tracked)" 1 \
                      || ck "AC11 the governed indexes exist ($n tracked)" 0
  BAD=$(printf '%s\n' "$POP" | grep . | git check-attr --stdin merge | grep -v ': merge: rows$' || true)
  if [ -z "$BAD" ]; then
    ck "AC11 every governed index declares merge=rows" 1
  else
    ck "AC11 every governed index declares merge=rows" 0
    printf '     %s\n' "$BAD"
  fi
fi

# AC12 — the PUBLISHED wiring command, DERIVED rather than proof-read.
# The kit README used to publish ONE literal that mixed the two install prefixes, naming a driver
# that exists in NEITHER layout. Configuring it verbatim reproduced the whole failure end to end:
# `can't open file '<prefix>/memory-tree/merge-rows.py'`, git printing `CONFLICT (content)`, and the path
# left holding ours-only content with `grep -c '<<<<<<<'` = 0 and status UU. Nothing gated the
# string, because the only other places the command appears either hand-type the correct one inside a
# fixture or BUILD it at runtime.
#
# So this arm does not proof-read the README. It DERIVES both spellings by running `--fix` in a
# complete fixture of each layout, then requires the README to publish exactly those two and no
# third one. A future prefix change moves the derived strings and reds the doc automatically.
newrepo; git config core.hooksPath .githooks; install_driver "${KP}"
chk --fix >/dev/null; S_TOOLS=$(git config merge.rows.driver 2>/dev/null || true); cleanup
# The ROOT layout's command comes from a checker installed AT the root. The checker finds a kit at
# its own prefix or through the receipt and no longer guesses the root from another prefix
# (TOOL-aRepatriatedFork-24 S8), so a root-layout fixture holds its own root copy of the checker.
newrepo; git config core.hooksPath .githooks; install_driver ""; cp "$SCRIPT" ./check-wiring.sh
bash ./check-wiring.sh --fix >/dev/null 2>&1; S_ROOT=$(git config merge.rows.driver 2>/dev/null || true); cleanup
cd "$REPO"
# LIVENESS, before anything is compared against the doc: two layouts that produced the SAME string,
# or no string at all, would turn the two greps below into one assertion wearing two hats.
{ [ -n "$S_TOOLS" ] && [ -n "$S_ROOT" ] && [ "$S_TOOLS" != "$S_ROOT" ]; } \
  && ck "AC12 the two layouts yield two distinct commands" 1 \
  || ck "AC12 the two layouts yield two distinct commands" 0
# Beside this suite first, the way `src_of` and ATTR_DRV above resolve a kit file, so a `scripts/`
# install finds its own README instead of skipping with a false reason (TOOL-aRepatriatedFork-24 S5).
RDM=""; for c in "$ROOT_ABS/$MT_KIT_DIR/README.md"; do
  [ -f "$c" ] && { RDM="$c"; break; }
done
if [ -z "$RDM" ]; then
  echo "skip README-command case — the memory-tree kit README is not installed in this repo"
else
  # The README spells the command ONCE, with the `<prefix>/` prose token (TOOL-aRepatriatedFork-26
  # S9), so each layout's command is that line with the token read as the fixture's prefix or as
  # nothing. Both must come out equal to what `--fix` derived, or the doc names a third command.
  PUB=$(grep -oE 'bash <prefix>/[A-Za-z0-9_./-]*merge-rows\.sh %O %A %B %P' "$RDM" | head -1)
  { [ -n "$PUB" ] && [ "${PUB//<prefix>\//${KP}}" = "$S_TOOLS" ]; } \
    && ck "AC12 README publishes the ${KP}-prefix command" 1 \
    || ck "AC12 README publishes the ${KP}-prefix command" 0
  { [ -n "$PUB" ] && [ "${PUB//<prefix>\//}" = "$S_ROOT" ]; } \
    && ck "AC12 README publishes the root-prefix command" 1 \
    || ck "AC12 README publishes the root-prefix command" 0
  # ...and NO third spelling. This is the half that fires on a mixed-prefix literal, which is a
  # command both greps above are perfectly happy to coexist with.
  STRAY=$(grep -oE 'bash [A-Za-z0-9_./-]*pyrun\.sh [A-Za-z0-9_./-]*merge-rows\.py %O %A %B %P' "$RDM" \
          | grep -vxF "$S_TOOLS" | grep -vxF "$S_ROOT" || true)
  if [ -z "$STRAY" ]; then
    ck "AC12 README publishes no third, unstartable spelling" 1
  else
    ck "AC12 README publishes no third, unstartable spelling" 0
    printf '     stray: %s\n' "$STRAY"
  fi
fi

# ---- the machine-global /session-kickoff install ------------------------------------------------
# Every arm drives HOME at a scratch dir, so nothing reads or writes the operator's real install.
# The tracked side is faked inside the throwaway repo, which is what makes the adopter arm (AC7)
# reachable at all: an adopter has the install and NO tracked kit source.
skill_fixture() {   # $1=1 to lay a tracked skills/session-kickoff/ into the repo
  FAKEHOME=$(mktemp -d); mkdir -p "$FAKEHOME/.claude/skills/session-kickoff"
  if [ "${1:-0}" = 1 ]; then
    mkdir -p skills/session-kickoff
    printf 'engine\n' > skills/session-kickoff/SKILL.md
    printf 'template\n' > skills/session-kickoff/MANIFEST-TEMPLATE.md
    printf 'checker\n' > skills/session-kickoff/manifest-check.sh
    git add -A >/dev/null 2>&1; git commit -q -m skill
  fi
}
install_engine() {  # $1=SKILL.md body
  printf '%s' "$1" > "$FAKEHOME/.claude/skills/session-kickoff/SKILL.md"
  printf 'template\n'  > "$FAKEHOME/.claude/skills/session-kickoff/MANIFEST-TEMPLATE.md"
  printf 'checker\n'   > "$FAKEHOME/.claude/skills/session-kickoff/manifest-check.sh"
}
skill_run() { HOME="$FAKEHOME" bash "$SCRIPT" --check 2>/dev/null | grep ' skill  ' || true; }

newrepo; skill_fixture 1; rm -rf "$FAKEHOME/.claude/skills/session-kickoff"
out=$(skill_run)
case "$out" in "skip     skill"*"not installed on this machine"*) r=1 ;; *) r=0 ;; esac
ck "AC1 no install on this machine -> skip" "$r"; rm -rf "$FAKEHOME"; cleanup

newrepo; skill_fixture 1; install_engine 'engine
'
out=$(skill_run)
case "$out" in "ok       skill"*"matches tracked"*) r=1 ;; *) r=0 ;; esac
ck "AC3 installed engine matches tracked -> ok" "$r"; rm -rf "$FAKEHOME"; cleanup

newrepo; skill_fixture 1; install_engine 'DIFFERENT
'
out=$(skill_run)
case "$out" in "UNWIRED  skill"*"differs from tracked in: SKILL.md"*) r=1 ;; *) r=0 ;; esac
ck "AC2 installed SKILL.md differs -> UNWIRED naming the file" "$r"
case "$out" in *"Fix:"*) r=1 ;; *) r=0 ;; esac
ck "AC2 the UNWIRED line carries a Fix remedy" "$r"; rm -rf "$FAKEHOME"; cleanup

# AC4 — CRLF on the installed side must NOT read as drift. This is the arm that fails if either half
# of the normalisation is dropped, and the one the repo's own trap says a byte-compare always needs.
newrepo; skill_fixture 1; install_engine 'engine
'
printf 'engine\r\n' > "$FAKEHOME/.claude/skills/session-kickoff/SKILL.md"
out=$(skill_run)
case "$out" in "ok       skill"*) r=1 ;; *) r=0 ;; esac
ck "AC4 a CRLF installed copy is not reported as drift" "$r"; rm -rf "$FAKEHOME"; cleanup

newrepo; skill_fixture 1; install_engine 'engine
'
rm -f "$FAKEHOME/.claude/skills/session-kickoff/manifest-check.sh"
out=$(skill_run)
case "$out" in "UNWIRED  skill"*"missing manifest-check.sh"*) r=1 ;; *) r=0 ;; esac
ck "a shipped file absent from the install -> UNWIRED naming it" "$r"; rm -rf "$FAKEHOME"; cleanup

# A LINKED worktree whose own branch edits the engine, while the install matches the primary
# checkout: a note, never UNWIRED, or a build editing the engine can never re-preflight. And the same
# worktree with the install drifting from the primary too: still UNWIRED.
newrepo; skill_fixture 1; install_engine 'engine
'
# A bare origin with its HEAD set, so the note's merge base resolves (TOOL-aGraftedHelix-36 S6).
SKOR=$(mktemp -d); git init -q --bare "$SKOR"; git -C "$SKOR" symbolic-ref HEAD refs/heads/main
git remote add origin "$SKOR"; git push -q origin main >/dev/null 2>&1
git fetch -q origin >/dev/null 2>&1; git remote set-head origin main >/dev/null 2>&1
SKWT=$(mktemp -d); rmdir "$SKWT"; git worktree add -q -b skbr "$SKWT" >/dev/null 2>&1
( cd "$SKWT" && printf 'edited\n' > skills/session-kickoff/SKILL.md && git commit -q -am edit )
out=$(cd "$SKWT" && skill_run)
case "$out" in "note     skill"*"branch edits the engine in: SKILL.md"*) r=1 ;; *) r=0 ;; esac
ck "a linked worktree's own engine edit, install matching the primary -> note" "$r"
case "$out" in *UNWIRED*) r=0 ;; *) r=1 ;; esac
ck "...and never UNWIRED" "$r"
install_engine 'DIFFERENT
'
out=$(cd "$SKWT" && skill_run)
case "$out" in "UNWIRED  skill"*"differs from tracked in: SKILL.md"*) r=1 ;; *) r=0 ;; esac
ck "the same worktree with the install drifting from the primary too -> UNWIRED" "$r"
# ...with no remote HEAD to take a merge base from, the editing worktree cannot earn its note.
install_engine 'engine
'
git remote set-head origin -d >/dev/null 2>&1
out=$(cd "$SKWT" && skill_run)
case "$out" in "UNWIRED  skill"*"no single remote's HEAD resolves"*) r=1 ;; *) r=0 ;; esac
ck "an engine-editing worktree with no remote HEAD -> UNWIRED" "$r"
git remote set-head origin main >/dev/null 2>&1
# ...and a worktree branched from an origin/main whose engine edit the primary never took, with no
# engine edit of its own, while the install matches the lagging primary: UNWIRED, naming the
# fast-forward. RED with the branch-change condition cut: the lagging worktree read the note.
SKCL=$(mktemp -d); rmdir "$SKCL"; git clone -q "$SKOR" "$SKCL" >/dev/null 2>&1
( cd "$SKCL" && git config user.email t@e && git config user.name t \
    && printf 'upstream\n' > skills/session-kickoff/SKILL.md && git commit -q -am upstream && git push -q origin main ) >/dev/null 2>&1
git fetch -q origin >/dev/null 2>&1
SKLG=$(mktemp -d); rmdir "$SKLG"; git worktree add -q -b sklag "$SKLG" origin/main >/dev/null 2>&1
out=$(cd "$SKLG" && skill_run)
case "$out" in "UNWIRED  skill"*"in: SKILL.md"*"pull --ff-only"*) r=1 ;; *) r=0 ;; esac
ck "a worktree off an origin/main the primary lags, no engine edit of its own -> UNWIRED, fast-forward the primary" "$r"
git worktree remove --force "$SKLG" >/dev/null 2>&1
git worktree remove --force "$SKWT" >/dev/null 2>&1; rm -rf "$SKWT" "$SKLG" "$SKCL" "$SKOR" "$FAKEHOME"; cleanup

# AC7 — the adopter shape: the install exists, the repo tracks no kit source. Without this state the
# check is a permanent false alarm in every adopting repo.
newrepo; skill_fixture 0; install_engine 'engine
'
out=$(skill_run)
case "$out" in "skip     skill"*"not adopted in this repo"*) r=1 ;; *) r=0 ;; esac
ck "AC7 install present, kit not adopted here -> skip (not a false alarm)" "$r"; rm -rf "$FAKEHOME"; cleanup

# AC5 — --fix must NOT touch the install. The out-of-repo write is refused by design, so the bytes
# are compared before and after rather than the refusal being argued in prose.
newrepo; skill_fixture 1; install_engine 'DIFFERENT
'
before=$(cat "$FAKEHOME/.claude/skills/session-kickoff/SKILL.md")
HOME="$FAKEHOME" bash "$SCRIPT" --fix >/dev/null 2>&1 || true
after=$(cat "$FAKEHOME/.claude/skills/session-kickoff/SKILL.md")
ck "AC5 --fix leaves the out-of-repo install byte-identical" "$([ "$before" = "$after" ] && echo 1 || echo 0)"
rm -rf "$FAKEHOME"; cleanup

# ---- S4: the settings file is RESOLVED, and an unresolvable one REFUSES (TOOL-dRetiredFork-8) -----
# Three arms, because the three outcomes are three different facts and the defect this unit removes
# was exactly that two of them looked the same. The pre-change script had NO settings file in these
# trees and graded the wiring anyway, reporting ok for every settings-dependent arm.
newrepo
mkdir -p .claude
printf '{"hooks":{}}\n' > .claude/settings.json
out=$(chke --check); ck "S4 in-tree settings resolve and are reported" \
  "$(printf '%s' "$out" | grep -qF 'settings  — resolved' && echo 1 || echo 0)"
ck "S4 an in-tree file is reported as INSIDE the root" \
  "$(printf '%s' "$out" | grep -qF '(inside the repo root)' && echo 1 || echo 0)"

# OUT OF TREE: reported, never failed. This is the layout at least one adopter runs deliberately,
# and it is also the shape in which the hardcoded path silently graded nothing.
OOTS=$(mktemp -d); printf '{"hooks":{}}\n' > "$OOTS/settings.json"
out=$(GOV_SETTINGS_JSON="$OOTS/settings.json" chke --check)
ck "S4 an out-of-tree settings file is REPORTED, not failed" \
  "$(printf '%s' "$out" | grep -qF 'OUTSIDE the repo root' && echo 1 || echo 0)"
ck "S4 ...and the wiring is still graded" \
  "$(printf '%s' "$out" | grep -qE '^(ok|UNWIRED|note) +(hooks|agent-cap|scratch|recall|merge)' && echo 1 || echo 0)"

# UNRESOLVABLE: a REFUSAL, not a non-match. An empty string here is what let every arm pass by
# absence, so this is the arm the whole unit exists for.
rm -f .claude/settings.json
# NOT exit 2. The refusal belongs to the ARMS that need the file, not to the run: a repo with no
# settings file is legal and its hooks, skills and eol wiring must still be graded. Measured: an
# eager whole-run refusal killed 45 of 76 arms, not one of which was about settings. What the
# refusal buys is that no arm reads "no file" as "nothing to check".
chk --check >/dev/null 2>&1; rc=$?
ck "S4 no settings file -> non-zero, the run still grading" "$([ "$rc" != 0 ] && echo 1 || echo 0)"
out=$(chke --check)
ck "S4 ...and the run names the failed resolution" \
  "$(printf '%s' "$out" | grep -qF 'no settings file resolved' && echo 1 || echo 0)"
# THE ARM NEEDS AN ADOPTED KIT. With no kit installed every settings arm reports `skip — not
# adopted`, which is correct and says nothing about this unit; the false-green case is a kit
# that IS installed while the settings file cannot be found.
mkdir -p $KIT_REL/${HOOKS} && printf '// agent-cap\n' > $KIT_REL/${HOOKS}/agent-cap.js
out=$(chke --check)
ck "S4 an ADOPTED kit with no settings file says UNWIRED, not ok" \
  "$(printf '%s' "$out" | grep -qE '^UNWIRED +agent-cap' && echo 1 || echo 0)"

# A DECLARED path that is not there is also a refusal, never a silent fallthrough to the preference
# rung — resolving a DIFFERENT file than the operator named would make every arm confidently wrong.
chk --check >/dev/null 2>&1 || true
out=$(GOV_SETTINGS_JSON="$OOTS/nope.json" chke --check)
ck "S4 a declared path that is absent does NOT fall back to the rung" \
  "$(printf '%s' "$out" | grep -qF 'which is not a file' && echo 1 || echo 0)"
rm -rf "$OOTS"; cleanup

# ---- TOOL-aWeldedTribunal-7: WHICH HOOK WILL ACTUALLY RUN --------------------------------------
# The shared `core.hooksPath` applies unless a worktree's config.worktree sets its own, and the
# value in effect decides which hook files run: an ABSOLUTE value runs the hooks of the checkout it
# names, the relative `.githooks` check-wiring writes runs each worktree's own — so under an
# absolute value a sibling checkout supplies the hook that gates
# your push. The check REPORTS that as a `note` and must never gate on it: `unwired` decides this
# script's exit code and `.unattended.conf` makes `--check` an unattended run's precondition, so an
# UNWIRED line would refuse every unattended run whenever another checkout moved.
#
# ARMS PER HOOK AND PER STATE, derived from the same list the check walks, so a third hook added to
# `GOV_WIRING_HOOKS` arrives with its arms demanded rather than remembered.
newrepo
printf '#!/bin/sh\nexit 0\n' > .githooks/pre-push; chmod +x .githooks/pre-push
git add -A; git commit -q -m "track both hooks"
OOT=$(mktemp -d); cp .githooks/pre-commit .githooks/pre-push "$OOT/"
git config core.hooksPath "$OOT"
out=$(bash "$SCRIPT" --check 2>&1); rc=$?
ck "hooks: identical blobs report no divergence" \
   "$([ "$(printf '%s' "$out" | grep -c 'DIVERGES')" = 0 ] && [ "$rc" = 0 ] && echo 1 || echo 0)"
printf '# planted\n' >> "$OOT/pre-push"
out=$(bash "$SCRIPT" --check 2>&1); rc=$?
ck "hooks: a diverging pre-push is REPORTED, naming both blobs" \
   "$(printf '%s' "$out" | grep -q 'pre-push DIVERGES' && echo 1 || echo 0)"
# THE ONE THAT CARRIES THE FORK RESOLUTION. A report that changes the exit code is the option the
# spec vetoed, shipped under the accepted option's name.
ck "hooks: a divergence does NOT gate — --check still exits 0" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
printf '# planted\n' >> "$OOT/pre-commit"
out=$(bash "$SCRIPT" --check 2>&1); rc=$?
ck "hooks: the pre-commit half is reported too" \
   "$(printf '%s' "$out" | grep -q 'pre-commit DIVERGES' && echo 1 || echo 0)"
ck "hooks: two divergences still exit 0" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
# TOOL-dDerivedDocket-9 — THE THIRD HOOK. `commit-msg` carries hygiene check 26 at the moment
# a merge is CONCLUDED, so a sibling checkout supplying somebody else's copy of it is exactly
# the divergence this check exists to report — and until `commit-msg` joined
# `GOV_WIRING_HOOKS` it could never report one. A FIXTURE arm, because an adopter's hook
# population is theirs; the both-ways comparison against THIS repo's tracked hooks lives in
# the memory-tree kit's transition-audit suite, which is gov-only.
printf '#!/bin/sh\nexit 0\n' > .githooks/commit-msg; chmod +x .githooks/commit-msg
git add -A; git commit -q -m "track the commit-msg hook"
cp .githooks/commit-msg "$OOT/"
out=$(bash "$SCRIPT" --check 2>&1)
ck "hooks: an identical commit-msg reports no divergence" \
   "$(printf '%s' "$out" | grep -q 'commit-msg DIVERGES' && echo 0 || echo 1)"
printf '# planted\n' >> "$OOT/commit-msg"
out=$(bash "$SCRIPT" --check 2>&1); rc=$?
ck "hooks: a diverging commit-msg is REPORTED" \
   "$(printf '%s' "$out" | grep -q 'commit-msg DIVERGES' && echo 1 || echo 0)"
ck "hooks: the commit-msg divergence does not gate either" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
rm -f "$OOT/pre-push"
out=$(bash "$SCRIPT" --check 2>&1)
ck "hooks: an unreadable side is UNKNOWN, never ok" \
   "$(printf '%s' "$out" | grep -q 'pre-push: UNKNOWN' && echo 1 || echo 0)"
cleanup
# A hook this tree does not TRACK is a SKIP. An adopter owning its own pre-commit and shipping no
# pre-push must not acquire a permanent finding it has no action to clear.
newrepo
OOT=$(mktemp -d); cp .githooks/pre-commit "$OOT/"
git config core.hooksPath "$OOT"
out=$(bash "$SCRIPT" --check 2>&1); rc=$?
ck "hooks: an untracked hook announces a skip" \
   "$(printf '%s' "$out" | grep -q 'pre-push is not tracked here' && echo 1 || echo 0)"
ck "hooks: a tracked-pre-commit-only adopter still exits 0" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
cleanup

# TOOL-cMendedVintage-3 — THE INSTALL PREFIX IS DERIVED, and the ROOT install was the one case the
# derivation could not reach. The `.git` boundary walk appended `basename "$_p"` to KIT_REL BEFORE it
# tested the PARENT for `.git`, so `$_p` was never tested as the repo root: a root install walked
# past the repository to the filesystem root and handed every rung a prefix of directories ABOVE the
# tree. Measured RED against base 859daa67 with these three arms — the probe path read
# `at c/Temp/kw3/repo/hooks/`, and with the guard actually shipped the arm still printed
# `skip — not adopted` over it. The two-segment arm is the CONTROL: it is the case every other rung
# in the file already depends on, and the reorder had to leave it exactly where it was. It is green
# on BOTH sides of the fix, which is what makes the other two mean something.
newrepo
cp "$SCRIPT" ./check-wiring.sh
mkdir -p scripts/gov; cp "$SCRIPT" scripts/gov/check-wiring.sh
git add -A; git commit -q -m "installs at the root and at a two-segment prefix"
out=$(bash ./check-wiring.sh --check 2>&1)
ck "prefix: a ROOT install probes agent-cap at 'hooks/', carrying no prefix segment" \
   "$(printf '%s' "$out" | grep -q 'no agent-cap.js at hooks/ or' && echo 1 || echo 0)"
out=$(bash ./scripts/gov/check-wiring.sh --check 2>&1)
ck "prefix: a two-segment install still carries both segments" \
   "$(printf '%s' "$out" | grep -q 'no agent-cap.js at scripts/gov/hooks/ or' && echo 1 || echo 0)"
# THE SECURITY SHAPE, which the path string on its own does not show: with the hook actually THERE, a
# root install reported the fan-out guard as not adopted. A skip that reads as a pass, over the one
# arm in this file where a false skip has a security shape.
mkdir -p "./${ROOTPFX}${HOOKS}"; printf '// stub\n' > "${ROOTPFX}${HOOKS}/agent-cap.js"
git add -A; git commit -q -m "ship agent-cap.js at the root install"
out=$(bash ./check-wiring.sh --check 2>&1)
ck "prefix: a ROOT install FINDS a shipped agent-cap.js instead of skipping it" \
   "$(printf '%s' "$out" | grep -q 'UNWIRED  agent-cap' && echo 1 || echo 0)"
# TOOL-cMendedVintage-4 — AND THE REMEDY IT PRINTS HAS TO BE RUNNABLE WHERE IT IS PRINTED. `SMERGE`
# used to fall back to a hardcoded `<prefix>/` prefix, so an install at any other prefix with no merger
# beside it handed the operator a command naming a file their tree does not contain. The two-segment
# install is the discriminating one: the old spelling and the new differ in both directions here, so
# the second assertion is not a restatement of the first — it reds if the literal comes back beside
# a derived one. No merger is installed anywhere in this fixture, which is the fallback's own case.
# That second pattern deliberately stops before the extension: spelled whole it would be a carried
# `<prefix>/` literal in this file's own bytes, which the install-prefix ban reds on with no waiver to
# take. Truncated it still matches the dead spelling and nothing else. Do not "complete" it.
mkdir -p "scripts/gov/$HOOKS"; printf '// stub\n' > "scripts/gov/$HOOKS/agent-cap.js"
git add -A; git commit -q -m "ship agent-cap.js at the two-segment install"
out=$(bash ./scripts/gov/check-wiring.sh --check 2>&1)
ck "prefix: the agent-cap remedy names the INSTALL PREFIX's merger" \
   "$(printf '%s' "$out" | grep -q 'scripts/gov/settings-merge.py' && echo 1 || echo 0)"
ck "prefix: no remedy in that install still names the dead ${KP} merger" \
   "$(printf '%s' "$out" | grep -q ''"${KP}settings-merge"'' && echo 0 || echo 1)"
cleanup

# ---- closing review round 1 M6 (TOOL-aRepatriatedFork-46): NO PYTHON, AND THE HOOK IS THERE ------
# This runs as a SessionStart hook on a host that may have no python. The probe rung went through the
# python resolver and was simply lost without one, so the agent-cap arm printed `not adopted` over a
# hook that sat beside the checker, naming a place nothing had probed. Every launcher name is
# shadowed by a stub that exits non-zero, the way the Microsoft Store stub does.
newrepo
OOT=$(mktemp -d)
for _n in python3 python py; do printf '#!/bin/sh\nexit 9\n' > "$OOT/$_n"; chmod +x "$OOT/$_n"; done
mkdir -p "./${KP}$HOOKS"; cp "$SCRIPT" "./${KP}check-wiring.sh"; printf '// stub\n' > "${KP}$HOOKS/agent-cap.js"
git add -A; git commit -q -m "a shipped agent-cap.js, and no usable python"
out=$(PATH="$OOT:$PATH" GOV_PYTHON= bash "./${KP}check-wiring.sh" --check 2>&1)
ck "M6 with no usable python the probe rung still finds a shipped agent-cap.js" \
   "$(printf '%s' "$out" | grep -q 'UNWIRED  agent-cap' && ! printf '%s' "$out" | grep -q 'skip     agent-cap' && echo 1 || echo 0)"
cleanup

# ---- Check T: local branches that still owe a backlog relocation (TOOL-dDerivedDocket-13) -------
# The fixture below publishes a bare origin and observes `origin/HEAD`, so an ambient
# GOV_DEFAULT_BRANCH is machine state that changes what it measures: the inventory's own
# resolver REFUSES when the declared name disagrees with the observed default.
unset GOV_DEFAULT_BRANCH
# The step is REPORT-ONLY by construction: `unwired` decides this script's exit code and
# `.unattended.conf` makes `--check` an unattended run's precondition, so a straggler reported as
# UNWIRED would refuse every unattended run on this node for a branch somebody else owns. These arms
# hold that severity, the mode gate in front of it, and the fact that it names the branch at all.
seed_relocation_kit() { # $1 = install prefix ("" here, the copy-installed adopter layout)
  local p="$1" rel src
  for rel in "${ROOTPFX}${MT_KIT}" "${ROOTPFX}${MEMORY_RECALL}" "${ROOTPFX}${LIB}"; do
    src=$(src_of "$rel")
    [ -n "$src" ] || { ck "seed_relocation_kit: $rel is not installed in $REPO" 0; return 1; }
    cp -r "$src" "${p}${rel}"
  done
  rm -rf "${p}${ROOTPFX}${MT_KIT}/__pycache__" "${p}${ROOTPFX}${MEMORY_RECALL}/__pycache__"
  # The recall-opened OPT-IN pair is dropped on purpose. It is not a dependency of the straggler
  # inventory, and leaving it here makes check R report UNWIRED over a fixture with no settings.json
  # — which would decide this script's exit code and make the `--check` arm below assert nothing
  # about the straggler severity it exists to hold.
  rm -f "${p}${ROOTPFX}${MEMORY_RECALL}/recall-opened.js" "${p}${ROOTPFX}${MEMORY_RECALL}/recall-opened.fragment.json"
}
# A SHARDS-mode tree first: the step must be silent about stragglers where no branch can be one.
newrepo
seed_relocation_kit "" || true
mkdir -p memory/backlog memory/builds/aSeed
printf 'MEMORY_ROOT=memory\nDISCIPLINES="tooling"\nFAMILIES="tooling:TOOL"\nROTATION_MODE="cut"\nBACKLOG_MODE="shards"\n' > .memory-tree.conf
printf '# the seed build\n' > memory/builds/aSeed/README.md
printf '# decisions\n\n- TOOL-aSeed-9 - a decision\n' > memory/DECISIONS.md
printf '# TOOL backlog\n\n- TOOL-aSeed-1 - the first ask\n' > memory/backlog/TOOL.md
printf '__pycache__/\n' > .gitignore
git add -A; git commit -q -m "a shards-mode memory tree"
out=$(chke --session)
ck "straggler: a shards-mode tree reports no straggler line" \
   "$(printf '%s' "$out" | grep -q '^note     straggler' && echo 0 || echo 1)"
ck "straggler: and says which condition held it back" \
   "$(printf '%s' "$out" | grep -q "^skip     straggler — BACKLOG_MODE is not 'builds'" && echo 1 || echo 0)"
# Now the flip, a bare origin so the default branch is OBSERVABLE, and one local straggler.
git checkout -q -b strag
printf '# TOOL backlog\n\n- TOOL-aSeed-1 - the first ask, REWORDED by the straggler\n' > memory/backlog/TOOL.md
git commit -q -am "the straggler edits a row"
git checkout -q main
printf 'MEMORY_ROOT=memory\nDISCIPLINES="tooling"\nFAMILIES="tooling:TOOL"\nROTATION_MODE="cut"\nBACKLOG_MODE="builds"\n' > .memory-tree.conf
mkdir -p memory/builds/aFlip
printf '# aFlip\n\n## Asks\n\n## Dispositions\n' > memory/builds/aFlip/BACKLOG.md
git add -A; git commit -q -m "flip to builds"
OOT=$(mktemp -d); git init -q --bare -b main "$OOT/origin.git"
git remote add origin "$OOT/origin.git"; git push -q origin main
git remote set-head origin -a >/dev/null 2>&1
out=$(chke --session); rc=$?
ck "straggler: --session exits 0 over a tree holding one" "$([ "$rc" = 0 ] && echo 1 || echo 0)"
ck "straggler: exactly one note line" \
   "$([ "$(printf '%s\n' "$out" | grep -c '^note     straggler')" = 1 ] && echo 1 || echo 0)"
ck "straggler: and it names the branch" \
   "$(printf '%s' "$out" | grep -q 'refs/heads/strag' && echo 1 || echo 0)"
# UNDER --check THE SEVERITY IS UNCHANGED AND THE EXIT IGNORES IT. This is the load-bearing arm:
# anything reading a non-zero exit as a refusal must not learn about stragglers that way.
out=$(chke --check); rc=$?
ck "straggler: --check reports it at note severity, never UNWIRED" \
   "$(printf '%s' "$out" | grep -q '^UNWIRED  straggler' && echo 0 || echo 1)"
ck "straggler: --check still names it" \
   "$(printf '%s' "$out" | grep -q '^note     straggler' && echo 1 || echo 0)"
ck "straggler: and the straggler alone does not decide the exit" \
   "$([ "$rc" = 0 ] && echo 1 || echo 0)"
# ONE CONF GRAMMAR (closing diff review round 1, F6): the step's mode read and the kit's own
# `tree_lib.parse_conf` agree over every legal spelling of the flip. The step's answer is read off its
# own line, and an answer that is neither the mode skip nor a straggler line is its own value, so a
# step that printed nothing cannot agree. The pipeline this step used read the commented and the
# exported spellings as not flipped and skipped a flipped tree.
cat > "$D/.git/mode-kit.py" <<'PYEOF'
import sys

sys.path.insert(0, sys.argv[1])
import tree_lib  # noqa: E402  the kit's ONE conf parser

with open(".memory-tree.conf", encoding="utf-8", newline="") as fh:
    conf = tree_lib.parse_conf(fh.read(), {})
sys.stdout.write("builds" if conf.get("BACKLOG_MODE") == "builds" else "not-builds")
PYEOF
for spell in 'absent|' 'blank|BACKLOG_MODE=""' 'quoted|BACKLOG_MODE="builds"' \
             'commented|BACKLOG_MODE=builds   # flipped by the switch-over' \
             'exported|export BACKLOG_MODE=builds' "single|BACKLOG_MODE='builds'" \
             'quoted-commented|BACKLOG_MODE="builds"  # flipped'; do
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="tooling"\nFAMILIES="tooling:TOOL"\nROTATION_MODE="cut"\n%s\n' "${spell#*|}" > .memory-tree.conf
  kitmode=$("$py" "$D/.git/mode-kit.py" "$D/memory-tree" 2>&1)
  out=$(chke --session)
  if printf '%s' "$out" | grep -q "^skip     straggler — BACKLOG_MODE is not 'builds'"; then shmode=not-builds
  elif printf '%s' "$out" | grep -qE '^(note|ok) +straggler '; then shmode=builds
  else shmode="no straggler line"; fi
  ck "straggler F6: the '${spell%%|*}' spelling reads '$kitmode' to the kit's parser and '$shmode' to the step" \
     "$([ "$shmode" = "$kitmode" ] && echo 1 || echo 0)"
done
rm -f "$D/.git/mode-kit.py"
cleanup

# ---- TOOL-aRepatriatedFork-19: the install RECEIPT is the first rung -----------------------------
# An adopter that homes a kit somewhere no probe spells — the merge driver flat under `scripts/`, the
# recall kit at `scripts/recall/`, the scratch guard in `.claude/hooks/` — got `skip … not adopted`
# over a kit that was installed and wired. The receipt records where every file landed, and these
# arms put each kit ONLY where the receipt says, so a probe cannot be what finds it. The receipt is
# written with the writer's own call, `json.dumps(indent=2)`, and every `source` carries a head that
# is not gov's tool root: the join is on the trailing `<kit-home>/<file>`, and a reader keyed on the
# whole source would miss here exactly as it would at an adopter.
write_receipt() { # <path>=<kit-home/file> ... -> .governance/install.json in the cwd
  mkdir -p .governance
  "$py" -c 'import json, sys
rows = [{"path": a.split("=", 1)[0], "role": "engine", "kit": "fixture", "source": "upstream/" + a.split("=", 1)[1]} for a in sys.argv[1:]]
open(".governance/install.json", "w", newline="\n").write(json.dumps({"schema": 3, "prefix": "scripts", "files": rows}, indent=2) + "\n")' "$@"
}
if [ -f "$SMERGE" ] && [ -f "$SGFRAG" ] && [ -n "$FRAG" ]; then
  newrepo; git config core.hooksPath .githooks   # isolate: hooks wired, so only the arms under test move
  mkdir -p scripts/memory-recall scripts/recall .claude/hooks memory/backlog ${KIT_REL:-.}
  _flat="${ROOTPFX}${MT_KIT}/merge-rows.py ${ROOTPFX}${MT_KIT}/merge-rows.sh"  # src_of keys under the tool root; the scratch repo lays them FLAT under scripts/, where no probe looks
  _grammar="${ROOTPFX}${MEMORY_RECALL}/extract.py ${ROOTPFX}${MEMORY_RECALL}/recall_conf.py"  # src_of keys under the tool root; the grammar kit the flat driver finds beside itself
  for rel in $_flat; do cp "$(src_of "$rel")" "scripts/${rel#*/}"; done
  seed_driver_kit scripts   # FLAT as well: the driver imports its siblings from its own directory
  for rel in $_grammar; do cp "$(src_of "$rel")" "scripts/$rel"; done
  printf 'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\n' > .memory-tree.conf
  printf '# tooling backlog\n\n- TOOL-001 | a landed row, so the family harvest has a population\n' > memory/backlog/TOOL.md
  printf 'memory/backlog/*.md merge=rows\n' > .gitattributes
  cp "$SGFRAG" .claude/hooks/scratch-guard.fragment.json; printf '// stub\n' > .claude/hooks/scratch-guard.js
  cp "$FRAG" scripts/recall/recall-opened.fragment.json; printf '// stub\n' > scripts/recall/recall-opened.js
  cp "$SMERGE" ${KP}settings-merge.py
  _rows="scripts/merge-rows.py=${ROOTPFX}${MT_KIT}/merge-rows.py scripts/merge-rows.sh=${ROOTPFX}${MT_KIT}/merge-rows.sh"  # receipt source suffixes, the join key, not install paths
  _rows="$_rows .claude/hooks/scratch-guard.fragment.json=${ROOTPFX}${HOOKS}/scratch-guard.fragment.json"  # receipt source suffix, the join key, not an install path
  _rows="$_rows scripts/recall/recall-opened.fragment.json=${ROOTPFX}${MEMORY_RECALL}/recall-opened.fragment.json"  # receipt source suffix, the join key, not an install path
  write_receipt $_rows
  "$py" ${KP}settings-merge.py --fragment .claude/hooks/scratch-guard.fragment.json >/dev/null 2>&1
  "$py" ${KP}settings-merge.py --fragment scripts/recall/recall-opened.fragment.json >/dev/null 2>&1
  git add -A; git commit -q -m receipted

  # AC1 — the flat driver is FOUND through its receipt row, and --fix wires the launcher beside it.
  # The second half is the positive artifact: `FIXED` is reachable only after the no-op three-way
  # ran, so the arm proves the driver it found is the one that merges, not merely a line that moved.
  out=$(chk --check)
  line=$(printf '%s\n' "$out" | grep -E '^[A-Za-z]+ +merge ' || true)
  ck "U19 AC1 a receipted flat merge driver is found, not skipped as not adopted" \
     "$([ -n "$line" ] && ! printf '%s' "$line" | grep -q 'not adopted' && echo 1 || echo 0)"
  chk --fix >/dev/null; got=$(git config merge.rows.driver 2>/dev/null || true)
  ck "U19 AC1 ...and --fix wires the flat driver's own launcher" \
     "$([ "$got" = "bash scripts/merge-rows.sh %O %A %B %P" ] && echo 1 || echo 0)"

  # AC2 — the scratch guard receipted into .claude/hooks/, and the recall kit homed at scripts/recall/.
  out=$(chk --check)
  ck "U19 AC2 a receipted, wired scratch guard reads ok" \
     "$(printf '%s' "$out" | grep -q '^ok       scratch' && echo 1 || echo 0)"
  ck "U19 AC2 a receipted, wired recall hook at a renamed kit dir reads ok" \
     "$(printf '%s' "$out" | grep -q '^ok       recall' && echo 1 || echo 0)"

  # S5 parity — the awk rung and the canonical Python reader answer one receipt identically. The
  # Python side is the `resolve_kit_dir` the merge driver itself carries, so this compares against
  # the reader that ships rather than a third spelling of it. Each answer must be NON-EMPTY: two
  # readers agreeing on nothing is the vacuous pass this repo refuses.
  eval "$(sed -n '/^resolve_receipt_path() {/,/^}/p' "$SCRIPT")"
  for pair in memory-tree:merge-rows.py hooks:scratch-guard.fragment.json memory-recall:recall-opened.fragment.json; do
    h=${pair%%:*}; a=${pair#*:}
    sh_ans=$(resolve_receipt_path "$h" "$a"); sh_ans=${sh_ans%/*}
    py_ans=$("$py" -c 'import importlib.util, pathlib, sys
spec = importlib.util.spec_from_file_location("merge_rows", "scripts/merge-rows.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
print(m.resolve_kit_dir(sys.argv[1], sys.argv[2], ".").relative_to(pathlib.Path(".").resolve()).as_posix())' "$h" "$a" 2>/dev/null | tr -d '\r')
    ck "U19 S5 resolve_receipt_path and resolve_kit_dir agree on $h/$a ($sh_ans)" \
       "$([ -n "$sh_ans" ] && [ "$sh_ans" = "$py_ans" ] && echo 1 || echo 0)"
  done

  # AC4 — the receipt names the driver and the file is gone: still a skip (a missing installed file
  # is the receipt leg's red), but one that names the row and the path instead of "not adopted".
  rm -f scripts/merge-rows.py
  _miss_row="install.json row for ${ROOTPFX}${MT_KIT}/merge-rows.py names scripts/merge-rows.py, which is absent"  # the receipt key the checker prints, not a path
  out=$(chk --check)
  line=$(printf '%s\n' "$out" | grep -E '^skip +merge ' || true)
  ck "U19 AC4 a receipted-but-missing driver skips naming the receipt and the path" \
     "$(printf '%s' "$line" | grep -qF "$_miss_row" && echo 1 || echo 0)"
  cleanup
else
  echo "skip receipt cases — settings-merge.py, scratch-guard.fragment.json or recall-opened.fragment.json not found"
fi

# ---- merge-2 skeptic F4: the STRAGGLER arm takes the receipt rung too ------------------------------
# It auto-merged without it, the one arm left finding its kit file by gov's layout alone, so an engine
# homed where no probe spells it read `not installed here` over an installed kit. The engine sits ONLY
# where the receipt says. Whether it then RUNS in this bare fixture is not this arm's question, so the
# first arm asserts only that the line stops calling it missing. Observed RED against the arm without
# the rung, on a scratch copy.
_tk=memory-tree; _te=migrate_backlog.py
if [ -n "$(src_of "$_tk/$_te")" ]; then
  newrepo; mkdir -p scripts
  cp "$(src_of "$_tk/$_te")" "scripts/$_te"
  write_receipt "scripts/$_te=$_tk/$_te"
  printf 'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\nBACKLOG_MODE="builds"\n' > .memory-tree.conf
  git add -A; git commit -q -m "a receipted straggler engine"
  line=$(chk --check | grep -E '^[A-Za-z]+ +straggler ' || true)
  ck "F4 a receipted straggler engine is found, not skipped as not installed" \
     "$([ -n "$line" ] && ! printf '%s' "$line" | grep -q 'is not installed here' && echo 1 || echo 0)"
  rm -f "scripts/$_te"
  line=$(chk --check | grep -E '^skip +straggler ' || true)
  ck "F4 ...and a receipted-but-missing engine skips naming the receipt row and the path" \
     "$(printf '%s' "$line" | grep -qF "install.json row for $_tk/$_te names scripts/$_te, which is absent" && echo 1 || echo 0)"
  cleanup
else
  echo "skip F4 straggler receipt cases — no $_te beside this suite"
fi

# AC5 — the eol arm's SECOND named glob: a tracked, pinned `.claude/workflows/*.js` holding CR bytes
# is named. The bound half rides along: a pinned `.claude/hooks/*.js` with the same CR bytes is NOT,
# because the population is two named globs and never "every eol=lf path under .claude/".
newrepo; git config core.hooksPath .githooks
mkdir -p .claude/skills/y .claude/workflows .claude/hooks
printf '.claude/skills/**/*.md eol=lf\n.claude/workflows/*.js eol=lf\n.claude/hooks/*.js eol=lf\n' > .gitattributes
printf 'a\nb\n' > .claude/skills/y/SKILL.md
printf 'x;\n' > .claude/workflows/harness.js
printf 'x;\n' > .claude/hooks/other.js
git add -A; git commit -q -m pins
printf 'x;\r\n' > .claude/workflows/harness.js
printf 'x;\r\n' > .claude/hooks/other.js
out=$(chk --check); rc=$?
ck "U19 AC5 a CR-carrying pinned workflow script is named by the eol arm" \
   "$([ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'note     eol       — .claude/workflows/harness.js' && echo 1 || echo 0)"
ck "U19 AC5 ...and a pinned .claude/ file outside both globs is not" \
   "$(printf '%s' "$out" | grep -q 'other.js' && echo 0 || echo 1)"
cleanup

# U22 AC3 — the merge=ours arm. git ships `ours` as a strategy, not a driver, so the attribute alone
# falls back to a text merge; the arm names the unset driver, wires `true` under --fix and --session,
# and never overwrites a value somebody else set. The baseline rc is 0 (hooks wired, no other kit
# adopted), so each rc=1 below is this arm's own. Global and system config are cut off for the arm:
# git reads `merge.ours.driver` from them too, so a node that set it globally would make "unset"
# unreachable here and red the arm for the machine's reasons.
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
newrepo; git config core.hooksPath .githooks
mkdir -p memory; printf 'x\n' > memory/LIVE.md
out=$(chk --check); rc=$?
ck "U22 AC3 no path declares merge=ours -> skip, exit 0" \
   "$([ "$rc" = 0 ] && printf '%s' "$out" | grep -q 'skip     merge     — merge=ours is declared on no tracked path' && echo 1 || echo 0)"
printf 'memory/LIVE.md merge=ours\n' > .gitattributes
git add -A; git commit -q -m ours
out=$(chk --check); rc=$?
ck "U22 AC3 merge=ours with the driver unset -> UNWIRED naming merge.ours.driver, exit 1" \
   "$([ "$rc" = 1 ] && printf '%s' "$out" | grep -q '^UNWIRED  merge     — .*merge\.ours\.driver is unset' && echo 1 || echo 0)"
chk --fix >/dev/null; got=$(git config merge.ours.driver 2>/dev/null || true); out=$(chk --check); rc=$?
ck "U22 AC3 ...--fix sets it to true, and the re-check is ok, exit 0" \
   "$([ "$got" = true ] && [ "$rc" = 0 ] && printf '%s' "$out" | grep -q '^ok       merge     — merge.ours.driver wired' && echo 1 || echo 0)"
git config merge.ours.driver false
chk --fix >/dev/null; got=$(git config merge.ours.driver 2>/dev/null || true); out=$(chk --check); rc=$?
ck "U22 AC3 ...a value already set is never overwritten and stays UNWIRED" \
   "$([ "$got" = false ] && [ "$rc" = 1 ] && printf '%s' "$out" | grep -q "merge.ours.driver='false', not 'true'; NOT overwriting" && echo 1 || echo 0)"
git config --unset merge.ours.driver
chk --session >/dev/null; rc=$?; got=$(git config merge.ours.driver 2>/dev/null || true)
ck "U22 AC3 ...--session wires the unset driver, exit 0" \
   "$([ "$rc" = 0 ] && [ "$got" = true ] && echo 1 || echo 0)"
cleanup
unset GIT_CONFIG_GLOBAL GIT_CONFIG_NOSYSTEM

# TOOL-aLevelledCopy-8 S1 — a set-when-unset write that FAILS is UNWIRED, logs no event, and --fix
# exits 1. "The lock" is an empty config.lock beside the fixture's own config: it fails every local
# `git config` write on every OS, where chmod is unreliable on MSYS. The ssh arm's half is LC8 AC1.
for t in hooks ours rows; do
  newrepo
  export GIT_CONFIG_GLOBAL="$D/.git/fixture-global" GIT_CONFIG_NOSYSTEM=1; : > "$GIT_CONFIG_GLOBAL"
  case $t in
    hooks) key=core.hooksPath; lbl='hooks    ' ;;
    ours)  key=merge.ours.driver; lbl='merge    '; git config core.hooksPath .githooks
           printf 'x\n' > ours.txt; printf 'ours.txt merge=ours\n' > .gitattributes; git add -A; git commit -q -m ours ;;
    rows)  key=merge.rows.driver; lbl='merge    '; git config core.hooksPath .githooks; install_driver "${KP}" ;;
  esac
  hl="$(git rev-parse --path-format=absolute --git-common-dir)/health.log"
  : > .git/config.lock
  out=$(chk --fix); rc=$?
  rm -f .git/config.lock
  got=$(git config "$key" 2>/dev/null || true)
  n1=$(grep -c -e $'\thookspath-set\t' -e $'\tmerge-driver-set\t' "$hl" 2>/dev/null)
  ck "LC8 AC2-3 $key write fails under --fix -> UNWIRED 'could not set $key', exit 1, no event, nothing set" \
     "$([ "$rc" = 1 ] && [ -z "$got" ] && [ "${n1:-0}" = 0 ] && printf '%s' "$out" | grep -qF "UNWIRED  $lbl — could not set $key" \
        && ! printf '%s' "$out" | grep -q '^FIXED' && echo 1 || echo 0)"
  cleanup
done
unset GIT_CONFIG_GLOBAL GIT_CONFIG_NOSYSTEM

# TOOL-aLevelledCopy-2 — the ssh arm. core.sshCommand is DERIVED from push-main.sh's one
# GOV_SSH_KEEPALIVE line and set only when no scope sets it. Each fixture's global config is a file of
# its own and system config is cut off, so this node's config cannot decide an arm; the remote is
# example.invalid, never contacted, and nothing pushes. WANT is the definition line run alone.
PM=$(src_of "${ROOTPFX}push-main.sh")
seed_ssh_fixture() {  # $1 = origin URL ("" = no remote) -> a wired repo holding a copy of push-main.sh
  newrepo; git config core.hooksPath .githooks
  export GIT_CONFIG_GLOBAL="$D/.git/fixture-global" GIT_CONFIG_NOSYSTEM=1; : > "$GIT_CONFIG_GLOBAL"
  unset GIT_SSH GIT_SSH_VARIANT   # an operator's SSH choice makes the arm stand back (TOOL-aLevelledCopy-7 S5)
  mkdir -p "${KP:-.}"; cp "$PM" "${KP}push-main.sh"
  [ -z "$1" ] || git remote add origin "$1"
}
if [ -z "$PM" ]; then
  echo "skip LC2 arms — push-main.sh is not installed beside this suite, so the ssh arm has nothing to derive from"
# Kit skew is an adopter's state only: a tree with an install receipt whose push-main.sh has no
# definition line updated check-wiring alone. gov's tree has no receipt, so there a lost line still reds.
elif [ -f "$REPO/.governance/install.json" ] && [ "$(grep -c '^GOV_SSH_KEEPALIVE=' "$PM")" = 0 ]; then
  echo "skip LC2 arms — the installed push-main.sh predates GOV_SSH_KEEPALIVE (kit skew); check-wiring --check reports it UNWIRED with the remedy"
else
WANT=$(eval "$(grep '^GOV_SSH_KEEPALIVE=' "$PM" | tr -d '\r')"; printf '%s' "${GOV_SSH_KEEPALIVE:-}")
SSHURL=git@example.invalid:o/r.git

# LC2 AC1 — unset: --session sets the derived value byte-for-byte, logs one event; a re-run is ok, silent.
# The suite's caller is modelled as a plink node: the fixture must cut that off, or AC1 and AC7 go red
# on exactly the machines TOOL-aLevelledCopy-7 protects (its S5; removing the seed's unset reds them).
export GIT_SSH=/bin/false GIT_SSH_VARIANT=plink
seed_ssh_fixture "$SSHURL"
hl="$(git rev-parse --path-format=absolute --git-common-dir)/health.log"
out=$(chk --session); got=$(git config --local core.sshCommand 2>/dev/null || true)
n1=$(grep -c $'\tsshcommand-set\t' "$hl" 2>/dev/null); out2=$(chk --session)
n2=$(grep -c $'\tsshcommand-set\t' "$hl" 2>/dev/null)
ck "LC2 AC1 unset -> --session sets the derived value, prints FIXED, logs one sshcommand-set" \
   "$([ -n "$WANT" ] && [ "$got" = "$WANT" ] && [ "${n1:-0}" = 1 ] && printf '%s' "$out" | grep -q '^FIXED    ssh' && echo 1 || echo 0)"
ck "LC2 AC1 ...a second --session prints ok and logs nothing more" \
   "$([ "${n2:-0}" = 1 ] && printf '%s' "$out2" | grep -q '^ok       ssh' && echo 1 || echo 0)"
cleanup

# LC2 AC2 — the value is a DERIVATION: an edited definition line moves what gets set.
seed_ssh_fixture "$SSHURL"
sed -i '/^GOV_SSH_KEEPALIVE=/s/ServerAliveInterval=30/ServerAliveInterval=31/' "${KP}push-main.sh"
chk --session >/dev/null; got=$(git config core.sshCommand 2>/dev/null || true)
ck "LC2 AC2 an edited definition line is what gets set (31, not a second literal 30)" \
   "$(case "$got" in *ServerAliveInterval=31*) echo 1 ;; *) echo 0 ;; esac)"
cleanup

# LC2 AC3 — an operator value at local OR global scope is never overwritten nor shadowed.
for sc in local global; do
  seed_ssh_fixture "$SSHURL"
  git config --$sc core.sshCommand 'ssh -i ~/.ssh/id_test'
  chk --fix >/dev/null; out=$(chk --session)
  got=$(git config --show-scope --get-all core.sshCommand 2>/dev/null | tr -d '\r')
  ck "LC2 AC3 a $sc operator value stays the only value and the run notes its scope" \
     "$([ "$got" = "$sc"$'\t''ssh -i ~/.ssh/id_test' ] && printf '%s' "$out" | grep -q "^note     ssh       — core.sshCommand is the operator's ($sc)" && echo 1 || echo 0)"
  cleanup
done

# LC2 AC4 — an operator value carrying its own keepalive is ok, named as the operator's.
seed_ssh_fixture "$SSHURL"
git config core.sshCommand 'ssh -o ServerAliveInterval=15'
out=$(chk --check)
ck "LC2 AC4 an operator value with its own keepalive -> ok, named the operator's" \
   "$(printf '%s' "$out" | grep -q "^ok       ssh       — core.sshCommand is the operator's" && echo 1 || echo 0)"
cleanup

# LC2 AC5 — an https remote, and no remote at all, skip and set nothing.
for url in https://example.invalid/o/r.git ""; do
  seed_ssh_fixture "$url"
  out=$(chk --session); got=$(git config core.sshCommand 2>/dev/null || true)
  ck "LC2 AC5 remote '${url:-none}' -> skip, nothing set" \
     "$([ -z "$got" ] && printf '%s' "$out" | grep -q '^skip     ssh       — no remote pushes over ssh' && echo 1 || echo 0)"
  cleanup
done

# LC2 AC6 — a deleted or duplicated definition line cannot be derived from, and that gates.
for edit in '/^GOV_SSH_KEEPALIVE=/d' '/^GOV_SSH_KEEPALIVE=/p'; do
  seed_ssh_fixture "$SSHURL"
  sed -i "$edit" "${KP}push-main.sh"
  out=$(chk --check); rc=$?
  ck "LC2 AC6 definition line edited by '$edit' -> UNWIRED naming the file, exit 1" \
     "$([ "$rc" = 1 ] && printf '%s' "$out" | grep -q "^UNWIRED  ssh       — cannot derive the keepalive from ${KP}push-main.sh" && echo 1 || echo 0)"
  cleanup
done

# LC2 AC7 — --check on an unset ssh tree reports the fix and writes nothing.
seed_ssh_fixture "$SSHURL"
out=$(chk --check); rc=$?; got=$(git config core.sshCommand 2>/dev/null || true)
ck "LC2 AC7 --check unset -> UNWIRED with a Fix naming git config core.sshCommand, exit 1, nothing written" \
   "$([ "$rc" = 1 ] && [ -z "$got" ] && printf '%s' "$out" | grep -q '^UNWIRED  ssh .*Fix: git config core.sshCommand' && echo 1 || echo 0)"
cleanup

# LC2 AC8 — the option string is spelled ONCE, in push-main.sh's definition line.
ck "LC2 AC8 one literal, on the GOV_SSH_KEEPALIVE line; the default reads it; none in the checker" \
   "$([ "$(grep -c ServerAliveInterval "$PM")" = 1 ] && grep ServerAliveInterval "$PM" | grep -q '^GOV_SSH_KEEPALIVE=' \
      && [ "$(grep -c 'GIT_SSH_COMMAND:=\$GOV_SSH_KEEPALIVE' "$PM")" = 1 ] \
      && [ "$(grep -c ServerAliveInterval "$SCRIPT")" = 0 ] && echo 1 || echo 0)"

# LC2 AC10 — no push-main.sh: no pre-push bar to outlast, so skip and set nothing.
seed_ssh_fixture "$SSHURL"; rm -f "${KP}push-main.sh"
out=$(chk --session); got=$(git config core.sshCommand 2>/dev/null || true)
ck "LC2 AC10 no push-main.sh -> skip naming push-main, nothing set" \
   "$([ -z "$got" ] && printf '%s' "$out" | grep -q '^skip     ssh       — push-main is not adopted' && echo 1 || echo 0)"
cleanup

# TOOL-aLevelledCopy-7 — the operator chose the SSH program: a GIT_SSH, a GIT_SSH_VARIANT or an
# ssh.variant makes the arm note it and write nothing, under --session and --check alike. Each
# variable is exported inside the run's own subshell, so the next seed starts from none.
for t in GIT_SSH GIT_SSH_VARIANT ssh.variant; do
  seed_ssh_fixture "$SSHURL"
  hl="$(git rev-parse --path-format=absolute --git-common-dir)/health.log"
  case $t in
    GIT_SSH) ev=GIT_SSH=/bin/false ;;
    GIT_SSH_VARIANT) ev=GIT_SSH_VARIANT=ssh ;;
    *) ev=""; git config --global ssh.variant plink ;;
  esac
  out=$([ -z "$ev" ] || export "$ev"; chk --session); got=$(git config core.sshCommand 2>/dev/null || true)
  n1=$(grep -c $'\tsshcommand-set\t' "$hl" 2>/dev/null)
  ck "LC7 AC1-3 $t -> --session notes $t as the operator's choice, sets nothing, logs nothing" \
     "$([ -z "$got" ] && [ "${n1:-0}" = 0 ] && printf '%s' "$out" | grep -q "^note     ssh       — $t is the operator's choice of SSH program" \
        && ! printf '%s' "$out" | grep -q '^FIXED    ssh' && echo 1 || echo 0)"
  out=$([ -z "$ev" ] || export "$ev"; chk --check); rc=$?; got=$(git config core.sshCommand 2>/dev/null || true)
  ck "LC7 AC4 $t -> --check exits 0 with the note, no UNWIRED ssh, no Fix, nothing written" \
     "$([ "$rc" = 0 ] && [ -z "$got" ] && printf '%s' "$out" | grep -q "^note     ssh       — $t is the operator's choice" \
        && ! printf '%s' "$out" | grep -q -e '^UNWIRED  ssh' -e 'Fix: git config core.sshCommand' && echo 1 || echo 0)"
  cleanup
done

# LC7 AC5 — a failed ssh.variant read is not an absence: git exits 3 for that one read, and the arm
# notes it and writes nothing rather than taking it as unset. The failing git is a shim first on the
# run's PATH, not a shell function, because a function named `git` is a definition the lexicon grades.
seed_ssh_fixture "$SSHURL"
mkdir "$D/.git/shim"
printf '#!/bin/sh\n[ "$*" = "config --get ssh.variant" ] && exit 3\nexec "%s" "$@"\n' "$(command -v git)" > "$D/.git/shim/git"
chmod +x "$D/.git/shim/git"
out=$(export PATH="$D/.git/shim:$PATH"; chk --session)
got=$(git config core.sshCommand 2>/dev/null || true)
ck "LC7 AC5 ssh.variant read exits 3 -> note 'cannot read ssh.variant', nothing set" \
   "$([ -z "$got" ] && printf '%s' "$out" | grep -q '^note     ssh       — cannot read ssh.variant (git config exit 3)' && echo 1 || echo 0)"
cleanup

# TOOL-aLevelledCopy-8 — the ssh arm's failure states. LC8 AC1: the lock (an empty config.lock, see
# LC8 AC2-3) fails the write, which is UNWIRED under --fix (exit 1) and --session (exit 0) alike.
seed_ssh_fixture "$SSHURL"
hl="$(git rev-parse --path-format=absolute --git-common-dir)/health.log"
: > .git/config.lock
out=$(chk --fix); rc=$?; out2=$(chk --session); rc2=$?
rm -f .git/config.lock
got=$(git config core.sshCommand 2>/dev/null || true); n1=$(grep -c $'\tsshcommand-set\t' "$hl" 2>/dev/null)
ck "LC8 AC1 core.sshCommand write fails -> UNWIRED 'could not set', --fix exit 1, --session exit 0, no event, nothing set" \
   "$([ "$rc" = 1 ] && [ "$rc2" = 0 ] && [ -z "$got" ] && [ "${n1:-0}" = 0 ] \
      && printf '%s' "$out" | grep -q '^UNWIRED  ssh       — could not set core.sshCommand' \
      && printf '%s' "$out2" | grep -q '^UNWIRED  ssh       — could not set core.sshCommand' && echo 1 || echo 0)"
cleanup

# LC8 AC4-5 — set or unset is the read's exit status. A git shim first on PATH fails one read: the
# scope read (129) only relabels an operator's value; the value read (3) is a note, never an absence.
for t in scope value; do
  seed_ssh_fixture "$SSHURL"; mkdir "$D/.git/shim"
  if [ "$t" = scope ]; then
    git config --global core.sshCommand 'ssh -i ~/.ssh/id_test'
    printf '#!/bin/sh\ncase " $* " in *" --show-scope "*) exit 129 ;; esac\nexec "%s" "$@"\n' "$(command -v git)" > "$D/.git/shim/git"
  else
    printf '#!/bin/sh\n[ "$*" = "config --get core.sshCommand" ] && exit 3\nexec "%s" "$@"\n' "$(command -v git)" > "$D/.git/shim/git"
  fi
  chmod +x "$D/.git/shim/git"
  out=$(export PATH="$D/.git/shim:$PATH"; chk --check); out2=$(export PATH="$D/.git/shim:$PATH"; chk --session)
  got=$(git config --local core.sshCommand 2>/dev/null || true)
  if [ "$t" = scope ]; then
    ck "LC8 AC4 the scope read fails on an operator's global value -> 'scope unread' note, nothing local" \
       "$([ -z "$got" ] && printf '%s' "$out2" | grep -qF "note     ssh       — core.sshCommand is the operator's (scope unread)" && echo 1 || echo 0)"
  else
    ck "LC8 AC5 the core.sshCommand read exits 3 -> note 'cannot read', no UNWIRED ssh, --session writes nothing" \
       "$([ -z "$got" ] && printf '%s' "$out" | grep -q '^note     ssh       — cannot read core.sshCommand' \
          && ! printf '%s%s' "$out" "$out2" | grep -q '^UNWIRED  ssh' && echo 1 || echo 0)"
  fi
  cleanup
done

# LC8 AC6 — no definition line is kit skew: still UNWIRED, and the line names the remedy.
seed_ssh_fixture "$SSHURL"; sed -i '/^GOV_SSH_KEEPALIVE=/d' "${KP}push-main.sh"
out=$(chk --check); rc=$?
line=$(printf '%s\n' "$out" | grep '^UNWIRED  ssh       — cannot derive the keepalive from ')
ck "LC8 AC6 no definition line -> UNWIRED naming ${KP}push-main.sh as predating it, remedy 'update the push-main kit', exit 1" \
   "$(case "$rc:$line" in "1:"*"${KP}push-main.sh"*predates*"update the push-main kit"*) echo 1 ;; *) echo 0 ;; esac)"
cleanup

# LC8 AC9 — the definition line is READ with sed, never evaluated: a command substitution in it would
# create a marker file if any eval or source reached it.
seed_ssh_fixture "$SSHURL"; sed -i '/^GOV_SSH_KEEPALIVE=/d' "${KP}push-main.sh"
printf "GOV_SSH_KEEPALIVE='ssh'\$(touch \"%s/ran\")\n" "$D" >> "${KP}push-main.sh"
out=$(chk --session); got=$(git config core.sshCommand 2>/dev/null || true)
ck "LC8 AC9 a command substitution in the definition line never runs -> no marker, UNWIRED cannot derive, nothing set" \
   "$([ ! -e "$D/ran" ] && [ -z "$got" ] && printf '%s' "$out" | grep -q '^UNWIRED  ssh       — cannot derive' && echo 1 || echo 0)"
cleanup

# LC8 AC10 — the classifier's two untested branches: a drive path is a path, ssh:// is ssh.
for url in C:/x/origin.git ssh://git@example.invalid/o/r.git; do
  seed_ssh_fixture "$url"
  out=$(chk --session); got=$(git config --local core.sshCommand 2>/dev/null || true)
  case $url in
    ssh://*) v=$([ -n "$WANT" ] && [ "$got" = "$WANT" ] && printf '%s' "$out" | grep -q '^FIXED    ssh' && echo 1 || echo 0) ;;
    *)       v=$([ -z "$got" ] && printf '%s' "$out" | grep -q '^skip     ssh       — no remote pushes over ssh' && echo 1 || echo 0) ;;
  esac
  ck "LC8 AC10 remote '$url' -> ${url%%:*} classified right (ssh:// set, drive path skipped)" "$v"
  cleanup
done
unset GIT_CONFIG_GLOBAL GIT_CONFIG_NOSYSTEM
fi

# ---- TOOL-aLevelledCopy-3: a tracked hook's INDEX mode -----------------------------------------
# Every mode below is STAGED (`git add --chmod`, `update-index --chmod`), never taken from the
# filesystem, so the fixture is the same on a core.fileMode=false host and on a POSIX one. Each arm
# greps the `hooks` lines: other arms print their own lines in these fixtures.
seed_mode_fixture() {   # hooks pre-commit + post-merge at 100644, pre-push 100755, two non-hooks 100644
  newrepo; git config core.hooksPath .githooks
  printf '#!/bin/sh\nexit 0\n' > .githooks/post-merge; printf '#!/bin/sh\nexit 0\n' > .githooks/pre-push
  printf 'x=1\n' > .githooks/gate-env.sh; printf '#!/bin/sh\nexit 0\n' > .githooks/pre-commit.test.sh
  git add --chmod=-x .githooks/post-merge .githooks/gate-env.sh .githooks/pre-commit.test.sh
  git add --chmod=+x .githooks/pre-push; git update-index --chmod=-x .githooks/pre-commit
  git commit -q -m modes
}
read_mode_lines() { printf '%s\n' "$1" | grep '^UNWIRED  hooks.*tracked 100644'; }

newrepo
ck "LC3 AC9 newrepo stages its pre-commit 100755 whatever core.fileMode says" \
   "$(git ls-files -s .githooks/pre-commit | grep -q '^100755 ' && echo 1 || echo 0)"
cleanup

seed_mode_fixture
m=$(read_mode_lines "$(chk --check)")
ck "LC3 AC2 --check names exactly the two 100644 hooks, pre-commit and post-merge" \
   "$([ "$(printf '%s\n' "$m" | grep -c .)" = 2 ] && printf '%s' "$m" | grep -q '\.githooks/pre-commit is' \
      && printf '%s' "$m" | grep -q '\.githooks/post-merge is' \
      && ! printf '%s' "$m" | grep -q -e pre-push -e gate-env -e '\.test\.sh' && echo 1 || echo 0)"
# AC3: --fix over a hook carrying an UNSTAGED edit moves the mode and nothing else.
read_hook_oids() { git ls-files -s .githooks/pre-commit .githooks/post-merge | awk '{print $2}' | tr '\n' ' '; }
o_before=$(read_hook_oids); printf '# unstaged\n' >> .githooks/pre-commit
hl="$(git rev-parse --path-format=absolute --git-common-dir)/health.log"
out=$(chk --fix); n1=$(grep -c $'\thookmode-set\t' "$hl" 2>/dev/null)
modes=$(git ls-files -s .githooks/pre-commit .githooks/post-merge | awk '{print $1}' | tr '\n' ' ')
cached=$(git diff --cached --numstat -- .githooks | awk '{print $1 $2}' | tr '\n' ' ')
ck "LC3 AC3 --fix stages 100755 for both, oids unmoved, numstat 0 0, the edit unstaged, two hookmode-set" \
   "$([ "$modes" = '100755 100755 ' ] && [ "$(read_hook_oids)" = "$o_before" ] && [ "$cached" = '00 00 ' ] \
      && git diff --numstat -- .githooks/pre-commit | grep -q $'^1\t0\t' && [ "${n1:-0}" = 2 ] \
      && [ "$(printf '%s\n' "$out" | grep -c '^FIXED    hooks')" = 2 ] && echo 1 || echo 0)"
out2=$(chk --fix); n2=$(grep -c $'\thookmode-set\t' "$hl" 2>/dev/null)
ck "LC3 AC3 ...a second --fix repairs nothing and logs nothing" \
   "$([ "${n2:-0}" = 2 ] && ! printf '%s' "$out2" | grep -q '^FIXED    hooks' && echo 1 || echo 0)"
cleanup

seed_mode_fixture
hl="$(git rev-parse --path-format=absolute --git-common-dir)/health.log"
out=$(chk --session); rc=$?; n1=$(grep -c $'\thookmode-set\t' "$hl" 2>/dev/null)   # no log at all is zero
ck "LC3 AC4 --session reports both, exits 0, stages no mode and logs no event" \
   "$([ "$rc" = 0 ] && [ "$(read_mode_lines "$out" | grep -c .)" = 2 ] \
      && git ls-files -s .githooks/pre-commit | grep -q '^100644 ' && [ "${n1:-0}" = 0 ] && echo 1 || echo 0)"
cleanup

# AC5: a linked worktree whose core.hooksPath names the PRIMARY's directory grades the primary's
# index and only notes it, as check_hook_blobs does for a sibling checkout.
seed_mode_fixture
OOT=$(mktemp -d); git worktree add -q -b wt "$OOT/wt" 2>/dev/null
git config core.hooksPath "$D/.githooks"; top=$(git rev-parse --show-toplevel)
out=$(cd "$OOT/wt" && chk --check)
ck "LC3 AC5 another checkout's 100644 hook is a note naming that checkout, never UNWIRED" \
   "$(printf '%s\n' "$out" | grep '^note     hooks' | grep -F "$top" | grep -q 'pre-commit is tracked 100644' \
      && [ -z "$(read_mode_lines "$out")" ] && echo 1 || echo 0)"
cleanup

# AC6: the defect itself, on a filesystem that honours the exec bit. A Windows git runs a 100644
# hook anyway, so there the dormancy is not observable and the arm says so instead of passing.
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*)
    echo "skip LC3 AC6 — $(uname -s) runs a 100644 hook anyway, so a dormant hook cannot be observed here; no pass counted" ;;
  *)
    newrepo; printf '#!/bin/sh\nexit 1\n' > .githooks/pre-commit; chmod -x .githooks/pre-commit
    git add --chmod=-x .githooks/pre-commit; git commit -q -m dormant; git config core.hooksPath .githooks
    git commit -q --allow-empty -m before >/dev/null 2>&1; rc1=$?
    chk --fix >/dev/null; git commit -q --allow-empty -m after >/dev/null 2>&1; rc2=$?
    ck "LC3 AC6 a 100644 hook that exits 1 is skipped by git, and refuses the commit after --fix" \
       "$([ "$rc1" = 0 ] && [ "$rc2" != 0 ] && echo 1 || echo 0)"
    cleanup ;;
esac

newrepo; OOT=$(mktemp -d); printf '#!/bin/sh\nexit 0\n' > "$OOT/pre-commit"; git config core.hooksPath "$OOT"
out=$(chk --check)
ck "LC3 AC7 a hooks dir no checkout tracks is an announced skip, never an ok about modes" \
   "$(printf '%s' "$out" | grep -q '^skip     hooks     — .*tracked by no checkout' \
      && ! printf '%s' "$out" | grep -q '^ok .*executable' && echo 1 || echo 0)"
cleanup

echo "---- $pass passed, $fail failed ----"
[ "$fail" = 0 ]
