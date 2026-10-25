#!/usr/bin/env bash
# Self-test for the one python-launcher resolver. Three things, because the resolver is only as good
# as the weakest of them:
#   1. BEHAVIOUR — against a fake stub that answers `command -v` and exits 9009, which is the exact
#      Microsoft Store defect this unit exists for. A fixture that used a merely-absent launcher
#      would pass against the OLD code too.
#   2. PARITY — every INLINE copy is byte-identical to the canonical block. Copy-installed kits
#      cannot source `../lib/`, so copies exist by design; drift between them is what a gate is for.
#   3. THE BAN — the retired `command -v python3 || python` idiom cannot come back in any tracked
#      `*.sh`, and the population is derived by scanning, not by listing.
#   bash <prefix>/lib/resolve-python.test.sh    # "PASS (…)" + exit 0 = good
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "resolve-python.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
ROOT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)
CANON="$HERE/resolve-python.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
st=0; n=0
ok()  { n=$((n+1)); }
bad() { echo "FAIL $1"; st=1; n=$((n+1)); }

# ---- 1. BEHAVIOUR -------------------------------------------------------------------------------
# A real python, found by the resolver itself before any fixture PATH is in play. If this repo has
# no python at all the whole bar is already dead, so an unresolvable launcher here is a hard error
# rather than a skip that reports success.
# shellcheck source=/dev/null
. "$CANON"
REALPY=$(resolve_python) || { echo "FAIL no python on this host at all — the arms below cannot run"; exit 2; }
REALPY_ABS=$(command -v "$REALPY")

mkfake() { # $1=dir $2=name $3=exit-code — a launcher that EXISTS, answers `command -v`, and cannot run
  mkdir -p "$1"
  printf '#!/usr/bin/env bash\nexit %s\n' "$3" > "$1/$2"
  chmod +x "$1/$2"
  # Windows resolves .exe/.cmd before an extensionless file on PATH; git-bash runs the extensionless
  # one, which is what this fixture needs, so no .exe twin is written.
}

# (a) the stub SHADOWS the real python3 — PREPENDED to the live PATH, never replacing it. A PATH cut
# down to the fixture dirs takes bash and every coreutil with it, and the arm then fails for a reason
# that has nothing to do with the resolver.
B="$TMP/stub"; mkfake "$B" python3 9009
got=$(PATH="$B:$PATH" bash -c '. "$1"; resolve_python' _ "$CANON" 2>/dev/null)
{ [ -n "$got" ] && [ "$got" != python3 ]; } || bad "a 9009 stub first on PATH was accepted (got '$got')"; ok
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${st:-0}" = 0 ] && echo "PASS (${n:-1} assertions)" || echo "FAIL (${n:-1} assertions)"; [ "${st:-0}" = 0 ] && exit 0; exit 1; fi
PATH="$B:$PATH" "${got:-false}" -c 'import sys' >/dev/null 2>&1 || bad "the resolver returned '$got', which does not run"; ok
# ...and the same PATH under the OLD idiom picks the stub — the arm is only meaningful because the
# defect reproduces. Without this the green half above could be passing for an unrelated reason.
oldpick=$(PATH="$B:$PATH" bash -c 'p=python3; command -v python3 >/dev/null 2>&1 || p=python; echo "$p"')
[ "$oldpick" = python3 ] || bad "the retired idiom did NOT pick the stub — the fixture does not reproduce the defect"; ok
PATH="$B:$PATH" python3 -c 'import sys' >/dev/null 2>&1 \
  && { bad "the fake stub actually ran — it is not standing in for a stub"; }; ok

# (b) nothing on PATH runs: all three launcher names shadowed by stubs.
C="$TMP/allbad"; mkfake "$C" python3 9009; mkfake "$C" python 9009; mkfake "$C" py 9009
out=$(PATH="$C:$PATH" bash -c '. "$1"; resolve_python' _ "$CANON" 2>&1); rc=$?
[ "$rc" != 0 ] || bad "an all-broken PATH still returned 0"; ok
grep -qF 'no usable python launcher' <<<"$out" || bad "the all-broken failure does not name itself"; ok
grep -qF 'tried: python3 python py' <<<"$out" || bad "the failure does not list the candidates it tried"; ok

# (c) GOV_PYTHON, both states. An override that is set and unusable must be a NAMED failure — the
# operator believes they chose, and a silent fall-through hides that they did not.
got=$(PATH="$B:$PATH" GOV_PYTHON="$REALPY_ABS" bash -c '. "$1"; resolve_python' _ "$CANON" 2>/dev/null)
[ "$got" = "$REALPY_ABS" ] || bad "a working GOV_PYTHON was not used (got '$got')"; ok
out=$(PATH="$C:$PATH" GOV_PYTHON="$C/python3" bash -c '. "$1"; resolve_python' _ "$CANON" 2>&1); rc=$?
[ "$rc" != 0 ] || bad "an unusable GOV_PYTHON fell through to a 0 exit"; ok
grep -qF "GOV_PYTHON is set to '$C/python3' and did not run" <<<"$out" \
  || bad "an unusable GOV_PYTHON was not NAMED in the failure"; ok

# (d) the caller's own published override goes first and is named on failure.
got=$(PATH="$B:$PATH" bash -c '. "$1"; resolve_python "$2"' _ "$CANON" "$REALPY_ABS" 2>/dev/null)
[ "$got" = "$REALPY_ABS" ] || bad "a working caller override was not used first (got '$got')"; ok
out=$(PATH="$C:$PATH" bash -c '. "$1"; resolve_python "$2"' _ "$CANON" "$C/py" 2>&1)
grep -qF "the caller's override '$C/py' was tried FIRST and did not run" <<<"$out" \
  || bad "an unusable caller override was not named"; ok

# (e) echo-and-return, not exit. Six of the seven consumers run `set -u` WITHOUT `set -e`, so a
# resolver that only `return 1`s cannot halt them — the caller has to be able to test a substitution.
out=$(PATH="$C:$PATH" bash -c 'set -u; . "$1"; PY=$(resolve_python) || { echo HALTED; exit 3; }; echo "NOTHALTED $PY"' _ "$CANON" 2>/dev/null); rc=$?
[ "$out" = HALTED ] && [ "$rc" = 3 ] || bad "the caller could not halt on failure (out='$out' rc=$rc)"; ok

# TOOL-aRepatriatedFork-46: the kickoff region's canonical copy lives in a SIBLING kit, found through the
# resolver rather than by typing that kit's name after the prefix.
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
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
  "$1" -c "${_rkd%$'\n'}"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
UNATTENDED_DIR=$(resolve_kit_dir "$REALPY" unattended check-unattended.sh "$HERE") || exit 2
RUNGATES_DIR=$(resolve_kit_dir "$REALPY" run-gates run-gates.sh "$HERE") || exit 2
# ---- 2. PARITY ----------------------------------------------------------------------------------
# A TABLE of (marker, canonical source, exclude-prefix), not one hardcoded predicate. It held exactly
# one row for a long time and read as a population; it was not one — the marker was hardcoded in both
# the extractor and the discovery grep, so a second shared predicate had nowhere to join. The kickoff
# kit's `region()` is that second predicate: `<prefix>/lib/` is gov-internal and ships nothing, so a
# copy-installed kit cannot source a shared library and must carry the function inline. An inline copy
# of a hard-won predicate with no parity gate is precisely what this arm exists to police.
#
# Each row is:  <marker-stem>|<canonical file>|<prefix excluded from the copy population>
PARITY_ROWS="
resolve_python|$CANON|$KIT_REL/resolve-python
kickoff_region|$ROOT/$UNATTENDED_DIR/check-unattended.sh|$UNATTENDED_DIR/check-unattended
render_doc|$ROOT/$KIT_REL/render-doc.sh|$KIT_REL/render-doc
resolve_kit_dir|$ROOT/$KIT_REL/resolve_kit_dir.py|$KIT_REL/resolve_kit_dir
derive_self_rel|$ROOT/$KIT_REL/kit-rel.sh|$KIT_REL/kit-rel
derive_kit_paths|$ROOT/$KIT_REL/render-doc.sh|$KIT_REL/render-doc
render_kit_cites|$ROOT/$KIT_REL/render-doc.sh|$KIT_REL/render-doc
check_kit_cites|$ROOT/$KIT_REL/render-doc.sh|$KIT_REL/render-doc
resolve_prefix_token|$ROOT/$KIT_REL/resolve_prefix_token.py|$KIT_REL/resolve_prefix_token
resolve_prefix_sh|$ROOT/$KIT_REL/kit-rel.sh|$KIT_REL/kit-rel
mempause_sh|$ROOT/$RUNGATES_DIR/run-gates.sh|$RUNGATES_DIR/run-gates.sh
health_log_sh|$ROOT/$KIT_REL/health-log.sh|$KIT_REL/health-log
health_log_py|$ROOT/$KIT_REL/health_log.py|$KIT_REL/health_log
remote_ladder_py|$ROOT/$KIT_REL/resolve_remote.py|$KIT_REL/resolve_remote
remote_ladder_sh|$ROOT/$KIT_REL/resolve-remote.sh|$KIT_REL/resolve-remote
compare_base_py|$ROOT/$KIT_REL/compare_base.py|$KIT_REL/compare_base
git_env_leaks_py|$ROOT/$KIT_REL/git_env_leaks.py|$KIT_REL/git_env_leaks
resolve_bash_py|$ROOT/$KIT_REL/resolve_bash.py|$KIT_REL/resolve_bash
"
# CRs are dropped before the compare: a Python copy may sit CRLF in a Windows working copy while git
# stores it LF, and the parity asked is of the block, not of a checkout's line endings.
# resolve_kit_dir (TOOL-aRepatriatedFork-2 S3) is the one row whose copies are Python as well as
# shell, so the population grep below reads both. TOOL-aRepatriatedFork-46: it reads the extensionless
# git hooks too, because the pre-push hook carries both blocks inline and a copy no row reads drifts.
# derive_self_rel (TOOL-aRepatriatedFork-18 S2) is the shipped suites' own-directory walk: each suite
# that ships carries it inline because `<prefix>/lib/` travels to nobody.
# derive_kit_paths (TOOL-aRepatriatedFork-10, closing review round 1 L4) is the receipt read the two
# memory-tree renderers each used to spell as their own grep, with nothing comparing the two.
# render_kit_cites (TOOL-dRenderedAnchor-6) is the filtered apply step of the two renderers that own
# none of render_doc's conf facts, the review-harness parity script and the unattended adopter; both
# carry it inline beside a copy of derive_kit_paths, and §2g below holds the canonical to its filter.
# check_kit_cites (TOOL-dRenderedAnchor-7) is the charset guard the same two renderers carry beside it,
# over the same lines, and §2i below holds the canonical to its filter and its set.
# resolve_prefix_token and resolve_prefix_sh (TOOL-aRepatriatedFork-47) are the `{prefix}` token's
# two canonicals, one per language; §2b below holds them to one answer. mempause_sh
# (TOOL-aGraftedHelix-7) is the memory pause both of the run-gates kit's dispatchers carry inline; like
# kickoff_region its canonical is a kit file, the bar's runner, and the self-test runner holds the copy.
# health_log_sh and health_log_py (TOOL-aGraftedHelix-8) are the health log's appender, one canonical
# per language beside this file; every writer kit and the card engine carry one inline, and §2c below
# holds the two canonicals to one format. The runbook's embedded migration program carries the Python one, so the population grep reads that one Markdown file too.
# remote_ladder_py and remote_ladder_sh (TOOL-dLadderedRemote-1) are the remote and default-branch
# ladder, one canonical per language beside this file; every probe that asks which ref "landed"
# means carries one inline, and §2d below holds the two canonicals to one truth table.
# compare_base_py (TOOL-dGroundRules-21 S7) is the shrink-only compare base the codebase map and the
# policy kit both read, and git_env_leaks_py (S9) the git variables the policy reader drops, the
# memory-tree kit's GIT_ENV_LEAKS member for member; each had a copy with no canonical to drift from.
# resolve_bash_py (TOOL-dGroundRules-25 S28) is the run-gates kit's bash rule the policy kit's checker
# carries; the other copies return another shape and are TOOL-dSettledRoster-6's ask.
#
# EVERY BLOCK IN A FILE IS GRADED, not the first (TOOL-aRepatriatedFork-47 S5). `blk` takes the
# block's ordinal: the extractor used to stop at the first closing marker, so a second copy in one
# file — `run-selftests.sh` carries two, one per embedded program — was never compared at all.
blk() { awk -v s="$1" -v k="${3:-1}" '$0 ~ ("^# >>> " s){i++; if(i==k)f=1} f{print} f && $0 ~ ("^# <<< " s){exit}' "$2" | tr -d '\r'; }
while IFS='|' read -r stem canon excl; do
  [ -n "$stem" ] || continue
  want=$(blk "$stem" "$canon")
  [ -n "$want" ] || bad "the canonical block for '$stem' is missing from $canon"; ok
  copies=$(cd "$ROOT" && git grep -l "^# >>> $stem" -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md | grep -v "^$excl" || true)
  # NON-EMPTY POPULATION IS ITS OWN ARM, per row. A row whose copies all disappeared would otherwise
  # pass by judging nothing, which is the vacuity this whole file refuses.
  [ -n "$copies" ] || bad "no inline copy of '$stem' found — this row would be judging an empty population"; ok
  while IFS= read -r rel; do
    [ -n "$rel" ] || continue
    nblk=$(grep -c "^# >>> $stem" "$ROOT/$rel")
    k=1
    while [ "$k" -le "$nblk" ]; do
      if [ "$(blk "$stem" "$ROOT/$rel" "$k")" != "$want" ]; then
        bad "inline copy of '$stem' drifted from $canon: $rel (block $k of $nblk)"
      fi
      ok; k=$((k+1))
    done
  done <<<"$copies"
done <<<"$PARITY_ROWS"

# ---- 2b. THE {prefix} CONTRACT, BEHAVIOUR ---------------------------------------------------------
# Parity holds each copy to its canonical; this holds the two canonicals to ONE answer. Both run over
# the contract table of TOOL-aRepatriatedFork-47 §4 and must print its third column, row for row.
PT='{prefix}'
PFX_ROWS="$PT/a/b||a/b
$PT/a/b|.|a/b
$PT||.
$PT/a|tools|tools/a
$PT/a|vendor/gov|vendor/gov/a
x/y|tools|x/y"
pfx_want=$(printf '%s\n' "$PFX_ROWS" | awk -F'|' '{print $3}')
pfx_py=$(printf '%s\n' "$PFX_ROWS" | "$REALPY" -B -c '
import sys
sys.path.insert(0, sys.argv[1])
from resolve_prefix_token import resolve_prefix_token
for line in sys.stdin.read().splitlines():
    s, t, _ = line.split("|")
    print(resolve_prefix_token(s, t))' "$HERE" | tr -d '\r')
pfx_sh=$(printf '%s\n' "$PFX_ROWS" | bash -c '. "$1"; while IFS="|" read -r s t _; do resolve_prefix_sh "$s" "$t"; done' _ "$HERE/kit-rel.sh")
[ "$(printf '%s\n' "$pfx_want" | grep -c .)" = 6 ] || bad "the {prefix} contract table did not read as six rows"; ok
[ "$pfx_py" = "$pfx_want" ] || bad "the Python {prefix} canonical disagrees with the contract table: $(printf '%s' "$pfx_py" | tr '\n' ' ')"; ok
[ "$pfx_sh" = "$pfx_want" ] || bad "the shell {prefix} canonical disagrees with the contract table: $(printf '%s' "$pfx_sh" | tr '\n' ' ')"; ok

# ---- 2c. THE HEALTH LOG, BEHAVIOUR (TOOL-aGraftedHelix-8) ------------------------------------------
# Parity holds each inline copy to its canonical; this holds the two CANONICALS to one I3 format. Both
# append to one scratch log, and every line must be four TAB fields under I3's stamp with its detail
# folded; then each language over both sides of the cap: a 499-line log takes one append untrimmed,
# a 500-line one keeps its newest 250 and then appends. WHAT THIS DOES NOT CHECK: any writer's call
# site, which belongs to the suite of the kit that writes it, nor a refused write's NOTE line.
hl="$TMP/health.log"; : > "$hl"
bash -c '. "$1"; add_health_event "$2" check-wiring hookspath-set "$3"' _ "$HERE/health-log.sh" "$hl" $'a\tb\nc'
"$REALPY" -B -c 'import sys; sys.path.insert(0, sys.argv[1]); import health_log; health_log.add_health_event(sys.argv[2], "reap", "tree-killed", sys.argv[3])' "$HERE" "$hl" $'c\rd'
[ "$(grep -c . "$hl")" = 2 ] || bad "the two canonicals did not append two lines to one log: $(grep -c . "$hl")"; ok
[ -z "$(awk -F'\t' 'NF != 4' "$hl")" ] || bad "a health line is not four TAB fields: $(awk -F'\t' 'NF != 4' "$hl" | head -1)"; ok
[ "$(cut -f1 "$hl" | grep -cE '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+]00:00$')" = 2 ] \
  || bad "a canonical stamps outside I3's spelling: $(cut -f1 "$hl" | tr '\n' ' ')"; ok
[ "$(cut -f2- "$hl" | tr '\t\n' '|;')" = "check-wiring|hookspath-set|a b c;reap|tree-killed|c d;" ] \
  || bad "the canonicals disagree on the source, event or folded detail: $(cut -f2- "$hl" | tr '\t\n' '|;')"; ok
for lang in sh py; do
  for start in 499 500; do
    seq 1 "$start" > "$hl"
    case "$lang" in
      sh) bash -c '. "$1"; add_health_event "$2" run-gates retry-passed x' _ "$HERE/health-log.sh" "$hl" ;;
      py) "$REALPY" -B -c 'import sys; sys.path.insert(0, sys.argv[1]); import health_log; health_log.add_health_event(sys.argv[2], "reap", "tree-killed", "x")' "$HERE" "$hl" ;;
    esac
    case "$start" in 499) want="500 1 4" ;; *) want="251 251 4" ;; esac
    got="$(grep -c . "$hl") $(head -1 "$hl") $(tail -1 "$hl" | awk -F'\t' '{print NF}')"
    [ "$got" = "$want" ] || bad "the $lang appender over a $start-line log left '$got' (lines, first line, last line's fields), not '$want'"; ok
  done
done

# ---- 2d. THE REMOTE LADDER, BEHAVIOUR (TOOL-dLadderedRemote-1) ------------------------------------
# Parity holds each inline copy to its canonical; this holds the two CANONICALS to one truth table,
# refusal text included, over git fixtures whose remotes are named anything but `origin` where the
# row is about that. The ambient GOV_REMOTE and GOV_DEFAULT_BRANCH are cleared per row, so a node that
# exports either cannot make a row pass. WHAT THIS DOES NOT CHECK: any consumer's call site, which is
# the suite of the kit that calls it, nor a remote URL — the ladder never reads one.
build_rr_fixture() { # dir -> a repo on branch `feature` with one empty commit and no remote
  git init -q -b main "$1" && git -C "$1" -c user.email=t@e -c user.name=t commit -q --allow-empty -m x \
    && git -C "$1" checkout -q -b feature
}
add_rr_remote() { # dir name [default] -> the remote configured, its tracking ref at HEAD, and HEAD's symref
  git -C "$1" remote add "$2" "../$2.git" && git -C "$1" update-ref "refs/remotes/$2/${3:-main}" HEAD \
    && git -C "$1" symbolic-ref "refs/remotes/$2/HEAD" "refs/remotes/$2/${3:-main}"
}
RR="$TMP/rr"; mkdir -p "$RR"
build_rr_fixture "$RR/one" && add_rr_remote "$RR/one" incms
build_rr_fixture "$RR/two" && add_rr_remote "$RR/two" incms && add_rr_remote "$RR/two" origin
build_rr_fixture "$RR/up" && add_rr_remote "$RR/up" incms && add_rr_remote "$RR/up" origin trunk && git -C "$RR/up" config branch.feature.remote origin
build_rr_fixture "$RR/none"
build_rr_fixture "$RR/nohead" && git -C "$RR/nohead" remote add r ../r.git
build_rr_fixture "$RR/dot" && add_rr_remote "$RR/dot" incms && git -C "$RR/dot" config branch.feature.remote .
# TOOL-dLadderedRemote-5: the two refusal texts no row graded, then the two names a SHORT ref read
# ambiguously — a tag sharing the branch's name, and a local branch named like the remote's default.
build_rr_fixture "$RR/detached" && add_rr_remote "$RR/detached" incms && add_rr_remote "$RR/detached" origin && git -C "$RR/detached" checkout -q --detach
build_rr_fixture "$RR/badcfg" && add_rr_remote "$RR/badcfg" incms && git -C "$RR/badcfg" config branch.feature.remote zz
build_rr_fixture "$RR/tag" && add_rr_remote "$RR/tag" incms && add_rr_remote "$RR/tag" origin trunk && git -C "$RR/tag" config branch.feature.remote origin && git -C "$RR/tag" tag feature
build_rr_fixture "$RR/ambig" && add_rr_remote "$RR/ambig" incms && git -C "$RR/ambig" branch incms/main
RR_ROWS="one||incms|main|main|
two|||||cannot choose a remote: GOV_REMOTE is unset, branch feature has no configured remote, and this repository has 2 remotes (incms origin). Name it: export GOV_REMOTE=<remote>.
two|GOV_REMOTE=incms|incms|main|main|
up||origin|trunk|trunk|
one|GOV_REMOTE=nosuch||||GOV_REMOTE names nosuch, which is no remote of this repository (incms). Name one that is: export GOV_REMOTE=<remote>.
none|GOV_DEFAULT_BRANCH=dev||dev||
nohead|GOV_DEFAULT_BRANCH=main|r|main||
dot||incms|main|main|
detached|||||cannot choose a remote: GOV_REMOTE is unset, a detached HEAD has no configured remote, and this repository has 2 remotes (incms origin). Name it: export GOV_REMOTE=<remote>.
badcfg|||||branch.feature.remote names zz, which is no remote of this repository (incms). Name one that is: export GOV_REMOTE=<remote>.
tag||origin|trunk|trunk|
ambig||incms|main|main|"
rr_k=0
while IFS='|' read -r fx envset want; do
  [ -n "$fx" ] || continue
  rr_k=$((rr_k+1))
  # shellcheck disable=SC2086
  rr_py=$(env -u GOV_REMOTE -u GOV_DEFAULT_BRANCH $envset "$REALPY" -B -c 'import sys; sys.path.insert(0, sys.argv[1]); from resolve_remote import resolve_remote; print("|".join(resolve_remote(sys.argv[2])))' "$HERE" "$RR/$fx" | tr -d '\r')
  # shellcheck disable=SC2086
  rr_sh=$(cd "$RR/$fx" && env -u GOV_REMOTE -u GOV_DEFAULT_BRANCH $envset bash -c '. "$1"; resolve_remote_sh; printf "%s|%s|%s|%s\n" "$RR_REMOTE" "$RR_BRANCH" "$RR_OBSERVED" "$RR_WHY"' _ "$HERE/resolve-remote.sh")
  [ "$rr_py" = "$want" ] || bad "remote ladder row $rr_k ($fx ${envset:-no env}): Python printed '$rr_py', the table says '$want'"; ok
  [ "$rr_sh" = "$want" ] || bad "remote ladder row $rr_k ($fx ${envset:-no env}): shell printed '$rr_sh', the table says '$want'"; ok
done <<<"$RR_ROWS"
[ "$rr_k" = 12 ] || bad "the remote ladder table read as $rr_k rows, not 12"; ok

# ---- 2e. THE KIT RESOLVER'S RECEIPT JOIN, BEHAVIOUR (TOOL-dRenderedAnchor-2) ----------------------
# Parity holds each inline copy of `resolve_kit_dir` to its canonical; this holds the canonical to the
# six receipt rows of TOOL-dRenderedAnchor-1's section 4 and a seventh, one query each with `here` at
# the tool root `p`. Rows 1 and 2 are held. Row 3 is the one only the join's role term rejects, a
# `merged` row, and row 4 the one only its home term rejects, a `rendered` row from another home's
# template. Row 5, `../out/w.js`, is the one only the `..` term rejects: `absolute()` keeps the `..`,
# so it passes `root in hit.parents`. Row 6 holds the existence test. Row 7 is the one only the
# outside-the-tree term `root in hit.parents` rejects (TOOL-dRenderedAnchor-3 S10): an absolute path
# to a file beside `w.js`, written by the python program in posix form, because a shell `/tmp/...`
# path inside JSON is not converted by MSYS and would name no file on Windows, and the join splits
# `path` on `/` before either term is read. The canonical is imported from beside this file, so a
# staged break of it reaches here. Every name is neutral, home `h`, other home `o`, kit directory
# `k`, because a kit name in a fixture path is an install-prefix hit.
# WHAT THIS DOES NOT CHECK: the probe rungs, which no row reaches, or any copy's call site.
RK="$TMP/rk"; mkdir -p "$RK/.git" "$RK/.governance" "$RK/p/k" "$RK/c" "$TMP/out"
for f in p/k/t.js p/k/u.js c/s.json p/k/v.js; do printf 'x\n' > "$RK/$f"; done
printf 'x\n' > "$TMP/out/w.js"; printf 'x\n' > "$TMP/out/y.js"
printf '%s\n' '{"files": [
 {"role": "rendered", "source": "p/h/t.template.js", "path": "p/k/t.js"},
 {"role": "engine", "source": "p/h/u.js", "path": "p/k/u.js"},
 {"role": "merged", "source": "p/h/s.fragment.json", "path": "c/s.json"},
 {"role": "rendered", "source": "p/o/v.template.js", "path": "p/k/v.js"},
 {"role": "rendered", "source": "p/h/w.template.js", "path": "../out/w.js"},
 {"role": "rendered", "source": "p/h/x.template.js", "path": "p/k/x.js"}]}' > "$RK/.governance/install.json"
rk_got=$("$REALPY" -B -c '
import json, pathlib, sys
sys.path.insert(0, sys.argv[1])
from resolve_kit_dir import resolve_kit_dir
root = pathlib.Path(sys.argv[2]).absolute()
receipt = root / ".governance" / "install.json"
data = json.loads(receipt.read_text(encoding="utf-8"))
data["files"].append({"role": "rendered", "source": "p/h/y.template.js",
                      "path": (root.parent / "out" / "y.js").absolute().as_posix()})
receipt.write_text(json.dumps(data), encoding="utf-8")
for anchor in ("t.js", "u.js", "s.json", "v.js", "w.js", "x.js", "y.js"):
    try:
        print(resolve_kit_dir("h", anchor, root / "p").relative_to(root).as_posix())
    except LookupError:
        print("LookupError")' "$HERE" "$RK" 2>&1 | tr -d '\r')
rk_want=$(printf '%s\n' p/k p/k LookupError LookupError LookupError LookupError LookupError)
mapfile -t rk_rows <<<"$rk_got"; rk_n=0
for rk_l in "${rk_rows[@]}"; do [ -z "$rk_l" ] || rk_n=$((rk_n+1)); done
[ "$rk_n" = 7 ] || bad "the receipt-join table did not read as seven rows: ${rk_got//$'\n'/ }"; ok
[ "$rk_got" = "$rk_want" ] || bad "the canonical resolve_kit_dir disagrees with the receipt-join table, rows 1 to 7: ${rk_got//$'\n'/ }"; ok

# ---- 2f. A TEMPLATE CITATION UNDER A RENDERED ROW, BEHAVIOUR (TOOL-dRenderedAnchor-2) -------------
# `derive_kit_paths` resolves every `{{TOOL_ROOT}}<home>/<file>` citation of the templates it is given
# through its inline `resolve_kit_dir`, so the receipt join decides what every rendered doc citing a
# harness names. The canonical in render-doc.sh, sourced, runs over a fixture whose receipt holds one
# `rendered` row, no `prefix` key and no adopter placeholder, and must print that citation's one line.
# Red on the a60b0c7d block, which printed nothing, so the citation fell through to the plain prefix.
# WHAT THIS DOES NOT CHECK: the adopter-placeholder answers and the prefix line, which no row reaches.
RD="$TMP/rd"; RD_CITE='{{TOOL_ROOT}}h/t.js'
mkdir -p "$RD/.git" "$RD/.governance" "$RD/p/mt" "$RD/p/k"
printf 'x\n' > "$RD/p/k/t.js"
printf 'cites %s here\n' "$RD_CITE" > "$RD/p/mt/x.template.md"
printf '%s\n' '{"files": [{"role": "rendered", "source": "p/h/t.template.js", "path": "p/k/t.js"}]}' \
  > "$RD/.governance/install.json"
rd_got=$(bash -c '. "$1"; derive_kit_paths "$2" "$3/p/mt" "$3/p/mt/x.template.md"' _ "$HERE/render-doc.sh" "$REALPY" "$RD" 2>&1 | tr -d '\r')
[ "$rd_got" = "$RD_CITE"$'\t'"p/k/t.js" ] || bad "derive_kit_paths over one rendered receipt row did not print its citation's one line: '$rd_got'"; ok

# ---- 2g. THE FILTERED APPLY STEP, BEHAVIOUR (TOOL-dRenderedAnchor-6) --------------------------------
# `render_kit_cites` applies only the `{{TOOL_ROOT}}<home>/<file>` lines of KIT_PATHS to the caller's
# `out`, with every CR dropped first. The canonical in render-doc.sh, sourced, runs over three CRLF
# lines, one cite, one bare `{{TOOL_ROOT}}` line and one adopter-placeholder line, and must apply the
# cite alone. Red with the case filter taken out, which reads `q/c` and `x`, and with the CR drop
# taken out, which leaves a CR after `t.js`. The output is compared raw, never through a CR strip.
# WHAT THIS DOES NOT CHECK: either inline copy's call site, which the renderers' own arms read.
RC_PATHS=$'{{TOOL_ROOT}}h/t.js\tp/k/t.js\r\n{{TOOL_ROOT}}\tq/\r\n{{GATE_RUNNER}}\tx\r\n'
RC_OUT='a {{TOOL_ROOT}}h/t.js b {{TOOL_ROOT}}c {{GATE_RUNNER}}'
rc_got=$(KIT_PATHS="$RC_PATHS" out="$RC_OUT" bash -c '. "$1"; render_kit_cites; printf %s "$out"' _ "$HERE/render-doc.sh" 2>&1)
[ "$rc_got" = 'a p/k/t.js b {{TOOL_ROOT}}c {{GATE_RUNNER}}' ] || bad "render_kit_cites applied a line that is no cite, or kept a CR: '${rc_got//$'\r'/<CR>}'"; ok

# ---- 2h. A KIT DIRECTORY REACHED THROUGH A JUNCTION, BEHAVIOUR (TOOL-dRenderedAnchor-7) ------------
# `derive_kit_paths` takes its kit directory LOGICALLY, as `resolve_kit_dir` takes `here`, because both
# renderers find their own root with a logical walk: a kit that is a junction inside the adopting
# repository cites that repository's paths, never the link target's. Two repositories, `jb` holding a
# link `.gov/wf` to `jt/tools/wf`, whose prefix differs. The canonical in render-doc.sh, sourced, runs
# over the link and must print the logical `.gov/wf/t.js`; red with `.resolve()`, which prints the
# target's `tools/wf/t.js`. The link is tested with `[ -L ]` AFTER it is made, because on this fleet
# `ln -s` can exit 0 and leave a copy; that copy is removed and a directory junction made instead.
# NEITHER YIELDING A LINK FAILS, never skips: this suite is gov-internal, every host it runs on can link,
# and a skip would be a gate that cannot go red.
# WHAT THIS DOES NOT CHECK: the receipt rung under a junction, which no row here reaches, or any copy's
# call site.
mkdir -p "$TMP/jb/.git" "$TMP/jb/.gov" "$TMP/jt/.git" "$TMP/jt/tools/wf"
printf 'x\n' > "$TMP/jt/tools/wf/t.js"
printf 'cites %s here\n' '{{TOOL_ROOT}}wf/t.js' > "$TMP/jb/x.template.md"
jl_how=""
if ln -s "$TMP/jt/tools/wf" "$TMP/jb/.gov/wf" 2>/dev/null && [ -L "$TMP/jb/.gov/wf" ]; then jl_how=symlink
else
  rm -rf "$TMP/jb/.gov/wf"
  cmd //c mklink //J "$(cygpath -w "$TMP/jb/.gov/wf" 2>/dev/null)" "$(cygpath -w "$TMP/jt/tools/wf" 2>/dev/null)" >/dev/null 2>&1 \
    && [ -L "$TMP/jb/.gov/wf" ] && jl_how=junction
fi
if [ -n "$jl_how" ]; then
  jl_got=$(bash -c '. "$1"; derive_kit_paths "$2" "$3/jb/.gov/wf" "$3/jb/x.template.md"' _ "$HERE/render-doc.sh" "$REALPY" "$TMP" 2>&1 | tr -d '\r')
  [ "$jl_got" = '{{TOOL_ROOT}}wf/t.js'$'\t''.gov/wf/t.js' ] || bad "derive_kit_paths over a kit reached through a $jl_how did not cite the logical .gov/wf/t.js: '$jl_got'"; ok
else
  bad "section 2h could make neither a symlink nor a directory junction at $TMP/jb/.gov/wf, so derive_kit_paths was never run through a link; this suite runs only on hosts that can make one"
fi

# ---- 2i. THE CITATION CHARSET, BEHAVIOUR (TOOL-dRenderedAnchor-7) ------------------------------------
# `check_kit_cites` refuses, at exit 2 and on one line naming the cite, a `{{TOOL_ROOT}}<home>/<file>`
# line of KIT_PATHS whose path is empty or leaves [A-Za-z0-9._/+@-], and reads no other line. The
# canonical in render-doc.sh, sourced, runs over three CRLF inputs: a clean cite with a bare
# `{{TOOL_ROOT}}` line and an adopter-placeholder line, both of whose values hold a space, which must
# return 0 and print nothing; then that set plus a cite holding a quote and a semicolon, and plus a cite
# holding a space, each of which must return 2 naming it. Red with the value case taken out, where all
# three return 0, and with the cite filter taken out, where the first returns 2 on `q r/`.
# WHAT THIS DOES NOT CHECK: either inline copy's call site, which the renderers' own arms read.
CK_BASE=$'{{TOOL_ROOT}}h/t.js\tp/k/t.js\r\n{{TOOL_ROOT}}\tq r/\r\n{{GATE_RUNNER}}\tthe merge bar of this repo\r\n'
for ck_k in 1 2 3; do
  case $ck_k in
    1) ck_in=$CK_BASE; ck_rc=0; ck_cite="" ;;
    2) ck_in=$CK_BASE$'{{TOOL_ROOT}}h/u.js\tp/u\';x;\'/u.js\r\n'; ck_rc=2; ck_cite="{{TOOL_ROOT}}h/u.js resolves to 'p/u';x;'/u.js'" ;;
    *) ck_in=$CK_BASE$'{{TOOL_ROOT}}h/v.js\tp/q r/v.js\r\n'; ck_rc=2; ck_cite="{{TOOL_ROOT}}h/v.js resolves to 'p/q r/v.js'" ;;
  esac
  ck_got=$(bash -c '. "$1"; check_kit_cites t "$2"; echo "rc=$?"' _ "$HERE/render-doc.sh" "$ck_in" 2>&1)
  ck_msg=${ck_got%$'\n'"rc=$ck_rc"}
  if [ "$ck_rc" = 0 ]; then
    [ "$ck_got" = rc=0 ] || bad "check_kit_cites input $ck_k refused a clean cite, a bare {{TOOL_ROOT}} line or an adopter-placeholder line: '${ck_got//$'\r'/<CR>}'"
  else
    { [ "$ck_msg" != "$ck_got" ] && [ "${ck_msg//$'\n'/}" = "$ck_msg" ] && [[ $ck_msg == "t: the citation $ck_cite,"* ]]; } \
      || bad "check_kit_cites input $ck_k did not return 2 with one line naming $ck_cite: '${ck_got//$'\r'/<CR>}'"
  fi; ok
done

# ---- 2j. THE TWO BASH RESOLVERS' CANDIDATE ORDER, BEHAVIOUR (TOOL-dGroundRules-82) -----------------
# Parity holds check_policy.py's copy of resolve_bash to its canonical; this holds the policy kit's JS
# resolveBash to the canonical's candidate ORDER, which no byte compare can, as TOOL-dGroundRules-81 §4
# "The order" states it. Each runs with its spawn stubbed, so every candidate fails and each prints all
# it tried, over a PATH of two fixture directories, each holding the bash name `shutil.which` finds on
# this host. GOV_BASH first and RB_TAIL last are one order on both sides; in the PATH slot the JS tries
# every PATH bash and Python the one `which` names. D1 stands for a first PATH bash that cannot see the
# shim, so D2 in the JS list is the case TOOL-dGroundRules-81 restored. A host with no node prints no
# list and reds, never skips. WHAT THIS DOES NOT CHECK: which candidate a real host keeps, a repeat
# tried once, a `bash.exe` before a `bash` in one directory (git-bash opens `bash.exe` when asked to
# write `bash` beside it), or any resolve_bash copy but the canonical.
POLICY_DIR=$(resolve_kit_dir "$REALPY" policy policy-mirror.js "$HERE") || exit 2
NODE=$(command -v node)
case "$(uname -s)" in MINGW*|MSYS*|CYGWIN*) RB_B=bash.exe ;; *) RB_B=bash ;; esac
RB="$TMP/rb"; mkdir -p "$RB/D1" "$RB/D2"
: > "$RB/D1/$RB_B"; : > "$RB/D2/$RB_B"; chmod +x "$RB/D1/$RB_B" "$RB/D2/$RB_B"
RB_TAIL="C:/Program Files/Git/bin/bash.exe;C:/Program Files/Git/usr/bin/bash.exe;bash"
rb_js=$(cd "$RB" && PATH="$RB/D1:$RB/D2" GOV_BASH=GB "$NODE" -e '
const cp = require("child_process"), path = require("path");
const root = path.dirname(process.env.PATH.split(path.delimiter)[0]), tried = [];
cp.spawnSync = (c) => c === "git" ? { status: 0, stdout: process.cwd() + "\n" } : (tried.push(c), { status: 1 });
try { require(process.argv[1]).readPolicy("runtime.agents-in-flight"); } catch (_e) { /* the refusal is expected */ }
console.log(tried.map((c) => c.split(root).join("F").split(path.sep).join("/")).join(";"));' "$ROOT/$POLICY_DIR/policy-mirror.js" 2>&1)
rb_py=$(cd "$RB" && PATH="$RB/D1:$RB/D2" GOV_BASH=GB "$REALPY_ABS" -B -c '
import os, subprocess, sys
sys.path.insert(0, sys.argv[1])
import resolve_bash
root, tried = os.path.dirname(os.environ["PATH"].split(os.pathsep)[0]), []
subprocess.run = lambda argv, **kw: tried.append(argv[0]) or subprocess.CompletedProcess(argv, 1)
resolve_bash.resolve_bash("x")
print(";".join(c.replace(root, "F").replace(os.sep, "/").replace(".EXE", ".exe") for c in tried))' "$HERE" 2>&1 | tr -d '\r')
[ "$rb_js" = "GB;F/D1/$RB_B;F/D2/$RB_B;$RB_TAIL" ] \
  || bad "the JS resolveBash order left the one TOOL-dGroundRules-81 states: $rb_js"; ok
[ "$rb_py" = "GB;F/D1/$RB_B;$RB_TAIL" ] \
  || bad "the canonical resolve_bash order left the one TOOL-dGroundRules-81 states: $rb_py"; ok

# ---- 3. THE BAN ---------------------------------------------------------------------------------
# The retired idiom, in any tracked `*.sh`. Comments are stripped first: this file and the resolver
# both EXPLAIN the idiom they replace, and a predicate that fires on the prose documenting the fix is
# the self-inflicted red this repo has a catalogue record about.
banned=$(cd "$ROOT" && git grep -nE 'command -v (python3|python|py)\b' -- '*.sh' \
  | grep -v '^'"$KIT_REL/resolve-python"'' \
  | awk -F: '{ line=$0; sub(/^[^:]*:[0-9]+:/, "", line); if (line !~ /^[[:space:]]*#/) print }' || true)
[ -z "$banned" ] || { echo "FAIL the retired python-launcher idiom is back:"; printf '%s\n' "$banned" | sed 's/^/    /'; st=1; }
ok
# ...and the ban's own population is non-empty, or it is a gate over nothing.
nsh=$(cd "$ROOT" && git ls-files -- '*.sh' | grep -c . || true)
[ "$nsh" -gt 10 ] || bad "the ban scanned $nsh shell files — the population collapsed"; ok
# ...and it FIRES on a planted line, so "clean" means "looked and found nothing".
plant="$TMP/plant.sh"; printf '#!/usr/bin/env bash\ncommand -v python3 >/dev/null 2>&1 || PY=python\n' > "$plant"
grep -qE 'command -v (python3|python|py)\b' "$plant" || bad "the ban predicate does not match the idiom it bans"; ok
printf '#!/usr/bin/env bash\n# command -v python3 is the retired idiom\n' > "$plant"
awk '$0 !~ /^[[:space:]]*#/' "$plant" | grep -qE 'command -v (python3|python|py)\b' \
  && bad "the ban fires on a COMMENT explaining the idiom"; ok

# ---- 3a. THE KIT-DIR WRAPPER BAN (TOOL-aSparedSpawn-4 S12) ----------------------------------------
# Every copy of `resolve_kit_dir` reads its heredoc with the builtin `read`, because the `cat` capture
# it replaced forked a subshell and exec'd `cat` at every call of every copy. §2 grades the bytes
# BETWEEN the markers, and the wrapper sits outside them, so without this the old capture could come
# back in any copy with parity still green. The population is §2's own for the `resolve_kit_dir` row,
# suites, product files and the extensionless hooks alike, derived by the same grep. Comments are
# stripped first, for §3's reason. The idiom is spelled in pieces so this file carries none of it, and
# no shell reader takes the line for a heredoc opener.
# WHAT THIS DOES NOT CHECK: a capture of any other heredoc tag, or one split across lines; the
# spawn-idiom lint of the gate-lint kit owns the general class on product files.
RKD_IDIOM="\$(c""at <""<'RKD'"
scan_rkd_capture() {  # file paths on stdin -> "file:line" per non-comment line holding the idiom
  awk -v idiom="$RKD_IDIOM" '
    { f = $0; n = 0
      while ((getline line < f) > 0) {
        n++; sub(/\r$/, "", line)
        if (line ~ /^[[:space:]]*#/) continue
        if (index(line, idiom)) printf "%s:%d\n", f, n
      }
      close(f) }'
}
rkd_pop=$(cd "$ROOT" && git grep -l "^# >>> resolve_kit_dir" -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md \
  | grep -v "^$KIT_REL/resolve_kit_dir" || true)
rkd_hits=$(cd "$ROOT" && printf '%s\n' "$rkd_pop" | scan_rkd_capture)
[ -z "$rkd_hits" ] || { echo "FAIL a resolve_kit_dir copy captures its heredoc with cat again; read it with IFS= read -r -d '' instead:"; printf '    %s\n' "${rkd_hits//$'\n'/$'\n'    }"; st=1; }
ok
# ...the population is real, and holds a suite, a product file and a hook, or it is a gate over less.
mapfile -t rkd_rows <<<"$rkd_pop"
[ "${#rkd_rows[@]}" -gt 10 ] || bad "the kit-dir wrapper ban scanned a collapsed population"; ok
{ [[ $rkd_pop$'\n' == *.test.sh$'\n'* ]] && [[ $'\n'$rkd_pop == *$'\n'.githooks/* ]]; } \
  || bad "the kit-dir wrapper ban population lost its suites or its hooks"; ok
# ...and it FIRES on a planted wrapper, and stays SILENT on a comment spelling the same idiom.
plant="$TMP/rkd.test.sh"
printf 'resolve_kit_dir() {\n  "$1" -c "%s\n' "$RKD_IDIOM" > "$plant"
[ "$(printf '%s\n' "$plant" | scan_rkd_capture | wc -l)" = 1 ] || bad "the kit-dir wrapper ban does not fire on a planted cat capture"; ok
printf '#!/usr/bin/env bash\n  # the old wrapper read %s, which forked\n' "$RKD_IDIOM" > "$plant"
[ -z "$(printf '%s\n' "$plant" | scan_rkd_capture)" ] || bad "the kit-dir wrapper ban fires on a COMMENT spelling the idiom"; ok

# ---- 3b. THE INVOCATION-SHAPE BAN ---------------------------------------------------------------
# The §3 ban above matches the retired IDIOM (`command -v python3 …`). A launcher invoked BARE —
# `python -c "…"`, `PYBIN=python3`, `$(python …)` — carries no idiom to match, so §3 could not see
# it. Measured: exactly that shape shipped in <prefix>/drift-audit/adopt-drift-audit.sh and was found by
# an adversarial review, not by this gate. This ban keys on the INVOCATION instead, so the thing it
# catches is "a python was run without being resolved" rather than "someone wrote the old sentence".
#
# TWO EXEMPTIONS, both narrow and both visible in the source being scanned:
#   * the resolver BLOCK itself — the one place the candidate names must appear, delimited by its own
#     markers, so the exemption cannot spread past them;
# THE ASSIGNMENT HALF IS NOT ANCHORED TO THE LINE START. `PY=$(resolve_python) || PY=python3` puts
# the bare fallback MID-LINE, `export PY=python3` puts a keyword in front of it, and `PY="python3"`
# quotes it — all three passed the first cut, and one of them was two lines above a site this very
# commit had marked `gov:literal-python`. A predicate that only reads column one is a predicate that
# reads the tidiest third of the population.
#
# TWO EXEMPTIONS, both narrow and both visible in the source being scanned:
#   * a line marked `gov:literal-python — <reason>`, which is an author's claim with the reason
#     attached. Which lines carry it is a grep for the marker, not a figure kept here; when this
#     was written each was a launcher NAME printed or rendered rather than executed (a remedy
#     string, a committed Skill render, an adopter-layout fallback).
# Scope is `*.sh`. Widening to .githooks/, *.json and *.md was measured and rejected: 46 further hits
# across 15 files, every one operator prose, which would need a 46-entry allowlist on day one — an
# allowlist that size is a second source of truth, not a gate.
#
# THE THIRD SHAPE is a PARAMETER DEFAULT: `py=${GOV_PYTHON:-python}`, `"${PYBIN:-python}" x.py`. It
# names a launcher after `:-`, so neither predicate above sees it, and it is a resolver of its own —
# one that never RUNS its candidate. Measured (the aReplayedCard closing review, F2): that exact line
# shipped in the kickoff checker's `--card --append` and locked every commit out on a host with only
# `python3`, and six test suites carried the same default. `${GOV_PYTHON:-}` — an EMPTY default —
# is the near-miss the predicate must not fire on: it is the resolver block's own spelling.
bare_scan() {  # $1=file -> "file:line:text" per bare-launcher site
  awk -v F="$1" '
    /^# >>> resolve_python/ { b = 1 }
    b { if (/^# <<< resolve_python/) b = 0; next }
    /^[[:space:]]*#/ { next }
    /gov:literal-python/ { next }
    /(^|[;&|(){}`!]|&&|\|\||\$\(|(^|[^A-Za-z0-9_])(if|elif|then|else|while|until|do|exec|env|time|nohup|xargs|sudo|command))[[:space:]]*(python3|python|py)([[:space:]]|$)/ ||
    /(^|[^A-Za-z0-9_$])(export[[:space:]]+)?[A-Za-z_][A-Za-z0-9_]*=["'"'"']?(python3|python|py)["'"'"']?([[:space:]]|;|\)|$)/ ||
    /:-["'"'"']?(python3|python|py)["'"'"']?\}/ \
      { printf "%s:%d:%s\n", F, NR, $0 }
  ' "$1"
}

bare=$(cd "$ROOT" && git ls-files -- '*.sh' | grep -v '^'"$KIT_REL/resolve-python"'' | while IFS= read -r f; do
         [ -n "$f" ] && [ -f "$f" ] && bare_scan "$f"
       done)
[ -z "$bare" ] || { echo "FAIL a python launcher is invoked without being resolved:"; printf '%s\n' "$bare" | sed 's/^/    /'; st=1; }
ok

# ...and the ban FIRES on the exact line that got past §3. Kept verbatim, with its provenance: this
# shipped, ran, and was caught by a person.
plant="$TMP/bare.sh"
{ printf '#!/usr/bin/env bash\n'
  printf 'KIT_REL="$(python -c "import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]))" "$A" "$B")"\n'
} > "$plant"
[ "$(bare_scan "$plant" | wc -l)" = 1 ] || bad "the ban does not fire on the site that got past the idiom ban"; ok
# ...the second live shape it must catch: an assignment to a bare name.
printf '#!/usr/bin/env bash\nPYBIN=python3\n' > "$plant"
[ "$(bare_scan "$plant" | wc -l)" = 1 ] || bad "the ban does not fire on a bare launcher ASSIGNMENT"; ok
# ...and the resolved shape it must NOT catch, or every migrated site reds.
printf '#!/usr/bin/env bash\nPY=$(resolve_python) || exit 2\n"$PY" x.py\n' > "$plant"
[ -z "$(bare_scan "$plant")" ] || bad "the ban fires on a correctly resolved invocation"; ok
# ...the two exemptions, each with its own red half so neither is a blanket hole.
printf '#!/usr/bin/env bash\nPY=python3   # gov:literal-python — printed, never run\n' > "$plant"
[ -z "$(bare_scan "$plant")" ] || bad "a marked literal is not exempt"; ok
printf '#!/usr/bin/env bash\nPY=python3\n' > "$plant"
[ -n "$(bare_scan "$plant")" ] || bad "the SAME line without the marker is exempt — the marker is doing nothing"; ok
# The block fixture must plant a line the ban DOES match, or "exempt" and "never matched" are the
# same observation. `PY=python3` inside the block is exactly such a line — verified below, outside it.
{ printf '# >>> resolve_python\n'; printf '  PY=python3\n'; printf '# <<< resolve_python\n'; } > "$plant"
[ -z "$(bare_scan "$plant")" ] || bad "the resolver block is not exempt from its own ban"; ok
printf '#!/usr/bin/env bash\n  PY=python3\n' > "$plant"
[ -n "$(bare_scan "$plant")" ] || bad "the block fixture plants a line the ban never matches — the exemption arm proves nothing"; ok
{ printf '# >>> resolve_python\n'; printf '# <<< resolve_python\n'; printf 'python x.py\n'; } > "$plant"
[ -n "$(bare_scan "$plant")" ] || bad "the block exemption leaks past its closing marker"; ok
# ...the three shapes the first cut let through, each measured live on this tree before the fix.
printf '#!/usr/bin/env bash\nPY=$(resolve_python) || PY=python3\n' > "$plant"
[ -n "$(bare_scan "$plant")" ] || bad "a MID-LINE bare fallback is not caught"; ok
printf '#!/usr/bin/env bash\nexport PY=python3\n' > "$plant"
[ -n "$(bare_scan "$plant")" ] || bad "an EXPORTED bare assignment is not caught"; ok
printf '#!/usr/bin/env bash\nPY="python3"\n' > "$plant"
[ -n "$(bare_scan "$plant")" ] || bad "a QUOTED bare assignment is not caught"; ok
# ...the parameter-default shape, the two spellings that shipped, and its one near-miss.
printf '#!/usr/bin/env bash\n    py=${GOV_PYTHON:-python}\n' > "$plant"
[ -n "$(bare_scan "$plant")" ] || bad "a PARAMETER-DEFAULT launcher (\${X:-python}) is not caught — the shape that locked the card append"; ok
printf '#!/usr/bin/env bash\nout=$( "${PYBIN:-python}" x.py 2>&1 )\n' > "$plant"
[ -n "$(bare_scan "$plant")" ] || bad "a quoted parameter-default launcher invocation is not caught"; ok
printf '#!/usr/bin/env bash\nPY=$(resolve_python "${GOV_PYTHON:-}") || exit 2\n' > "$plant"
[ -z "$(bare_scan "$plant")" ] || bad "an EMPTY default \${GOV_PYTHON:-} fires the parameter-default ban"; ok
# ...and the ban's own population is real, or it is a gate over nothing.
nsh2=$(cd "$ROOT" && git ls-files -- '*.sh' | grep -cv '^'"$KIT_REL/resolve-python"'' || true)
[ "$nsh2" -gt 10 ] || bad "the invocation ban scanned $nsh2 shell files — the population collapsed"; ok

# ---- 3c. THE {prefix} RESOLUTION BAN ------------------------------------------------------------
# §2 grades the MARKED copies of the `{prefix}` resolution; this is what stops an UNMARKED one, which
# is how eleven of them came to exist unseen (TOOL-aRepatriatedFork-47 S7). Outside a
# `resolve_prefix_token` or `resolve_prefix_sh` block, no tracked `*.sh` or `*.py` line and no line
# of the runbook may resolve the token by hand. The forms matched are a Python `.replace(` whose
# first argument opens with the token, in either quote style; a shell `#"{prefix}/"` prefix strip;
# and a `sed` substitution whose pattern begins with the token and its slash.
#
# WHAT IT CANNOT SEE, so a green run is not misread: a line whose first non-blank is `#` (every
# comment, so prose explaining the form never reds); `re.sub`, `str.replace(s, …)`, a token held in
# a variable or built by concatenation; a bash `${x/…}` or `${x//…}` substitution; any file outside
# the population named above, including `.githooks/*` and every other Markdown file.
scan_prefix_token() {  # file paths on stdin -> "file:line:text" per hand-written resolution outside a block
  awk '
    { f = $0; b = 0; n = 0
      while ((getline line < f) > 0) {
        n++; sub(/\r$/, "", line)
        if (line ~ /^# >>> resolve_prefix_(token|sh)/) b = 1
        if (b) { if (line ~ /^# <<< resolve_prefix_(token|sh)/) b = 0; continue }
        if (line ~ /^[[:space:]]*#/) continue
        if (line ~ /\.replace\(["\047][{]prefix[}]/ || line ~ /#"[{]prefix[}]\/"/ ||
            line ~ /sed[^|]*s[^[:alnum:][:space:]][{]prefix[}]\//)
          printf "%s:%d:%s\n", f, n, line
      }
      close(f) }'
}
pfx_pop=$(cd "$ROOT" && git ls-files -- '*.sh' '*.py' WIRE-INTO-PROJECT.md)
pfx_hits=$(cd "$ROOT" && printf '%s\n' "$pfx_pop" | scan_prefix_token)
[ -z "$pfx_hits" ] || { echo "FAIL a {prefix} token is resolved by hand outside a marked block:"; printf '%s\n' "$pfx_hits" | sed 's/^/    /'; st=1; }
ok
# ...and the population is real: the shell and Python files, and the one Markdown file named.
[ "$(printf '%s\n' "$pfx_pop" | grep -c .)" -gt 10 ] || bad "the {prefix} ban scanned a collapsed population"; ok
printf '%s\n' "$pfx_pop" | grep -qx 'WIRE-INTO-PROJECT.md' || bad "the {prefix} ban does not read the runbook"; ok
# ...and each banned form FIRES on a plant, spelled through $PT so this file carries none of them.
plant="$TMP/pfx.py"
for form in "x = s.replace(\"$PT/\", \"\")" "x = s.replace('$PT', tr)" \
            "p=\"\${SELF_PRE}\${p#\"$PT/\"}\"" "s=\$(printf x | sed \"s#$PT/#\$pre#g\")"; do
  printf '%s\n' "$form" > "$plant"
  [ "$(printf '%s\n' "$plant" | scan_prefix_token | wc -l)" = 1 ] || bad "the {prefix} ban does not fire on: $form"; ok
done
# ...the block exemption, with its red half and its closing edge.
{ printf '# >>> resolve_prefix_token\n'; printf '    return s.replace("%s/", "")\n' "$PT"; printf '# <<< resolve_prefix_token\n'; } > "$plant"
[ -z "$(printf '%s\n' "$plant" | scan_prefix_token)" ] || bad "a resolution inside a marked block reds the {prefix} ban"; ok
{ printf '# >>> resolve_prefix_sh\n'; printf '# <<< resolve_prefix_sh\n'; printf 'x = s.replace("%s/", "")\n' "$PT"; } > "$plant"
[ -n "$(printf '%s\n' "$plant" | scan_prefix_token)" ] || bad "the {prefix} block exemption leaks past its closing marker"; ok
printf '    # s.replace("%s/", "") is the hand-written form\n' "$PT" > "$plant"
[ -z "$(printf '%s\n' "$plant" | scan_prefix_token)" ] || bad "the {prefix} ban fires on a COMMENT explaining the form"; ok

[ "$st" = 0 ] && echo "PASS — resolve-python: $n assertions held"
exit "$st"
