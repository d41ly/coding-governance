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
ROOT=$(git -C "$HERE" rev-parse --show-toplevel)
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
UNATTENDED_DIR=$(resolve_kit_dir "$REALPY" unattended check-unattended.sh "$HERE") || exit 2
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
resolve_prefix_token|$ROOT/$KIT_REL/resolve_prefix_token.py|$KIT_REL/resolve_prefix_token
resolve_prefix_sh|$ROOT/$KIT_REL/kit-rel.sh|$KIT_REL/kit-rel
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
# resolve_prefix_token and resolve_prefix_sh (TOOL-aRepatriatedFork-47) are the `{prefix}` token's
# two canonicals, one per language; §2b below holds them to one answer. The runbook's embedded
# migration program carries the Python one, so the population grep reads that one Markdown file too.
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
#     attached. Measured today: three such lines, each a launcher NAME printed or rendered rather
#     than executed (a remedy string, a committed Skill render, an adopter-layout fallback).
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
