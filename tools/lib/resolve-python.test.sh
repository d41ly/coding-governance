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
#   bash tools/lib/resolve-python.test.sh    # "PASS (…)" + exit 0 = good
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT=$(cd "$HERE/../.." && pwd)
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

# ---- 2. PARITY ----------------------------------------------------------------------------------
# A TABLE of (marker, canonical source, exclude-prefix), not one hardcoded predicate. It held exactly
# one row for a long time and read as a population; it was not one — the marker was hardcoded in both
# the extractor and the discovery grep, so a second shared predicate had nowhere to join. The kickoff
# kit's `region()` is that second predicate: `tools/lib/` is gov-internal and ships nothing, so a
# copy-installed kit cannot source a shared library and must carry the function inline. An inline copy
# of a hard-won predicate with no parity gate is precisely what this arm exists to police.
#
# Each row is:  <marker-stem>|<canonical file>|<prefix excluded from the copy population>
PARITY_ROWS="
resolve_python|$CANON|tools/lib/resolve-python
kickoff_region|$ROOT/tools/unattended/check-unattended.sh|tools/unattended/check-unattended
render_doc|$ROOT/tools/lib/render-doc.sh|tools/lib/render-doc
"
blk() { awk -v s="$1" '$0 ~ ("^# >>> " s){f=1} f{print} $0 ~ ("^# <<< " s){if(f)exit}' "$2"; }
while IFS='|' read -r stem canon excl; do
  [ -n "$stem" ] || continue
  want=$(blk "$stem" "$canon")
  [ -n "$want" ] || bad "the canonical block for '$stem' is missing from $canon"; ok
  copies=$(cd "$ROOT" && git grep -l "^# >>> $stem" -- '*.sh' | grep -v "^$excl" || true)
  # NON-EMPTY POPULATION IS ITS OWN ARM, per row. A row whose copies all disappeared would otherwise
  # pass by judging nothing, which is the vacuity this whole file refuses.
  [ -n "$copies" ] || bad "no inline copy of '$stem' found — this row would be judging an empty population"; ok
  while IFS= read -r rel; do
    [ -n "$rel" ] || continue
    if [ "$(blk "$stem" "$ROOT/$rel")" != "$want" ]; then
      bad "inline copy of '$stem' drifted from $canon: $rel"
    fi
    ok
  done <<<"$copies"
done <<<"$PARITY_ROWS"

# ---- 3. THE BAN ---------------------------------------------------------------------------------
# The retired idiom, in any tracked `*.sh`. Comments are stripped first: this file and the resolver
# both EXPLAIN the idiom they replace, and a predicate that fires on the prose documenting the fix is
# the self-inflicted red this repo has a catalogue record about.
banned=$(cd "$ROOT" && git grep -nE 'command -v (python3|python|py)\b' -- '*.sh' \
  | grep -v '^tools/lib/resolve-python' \
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
# it. Measured: exactly that shape shipped in tools/drift-audit/adopt-drift-audit.sh and was found by
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
bare_scan() {  # $1=file -> "file:line:text" per bare-launcher site
  awk -v F="$1" '
    /^# >>> resolve_python/ { b = 1 }
    b { if (/^# <<< resolve_python/) b = 0; next }
    /^[[:space:]]*#/ { next }
    /gov:literal-python/ { next }
    /(^|[;&|(){}`!]|&&|\|\||\$\(|(^|[^A-Za-z0-9_])(if|elif|then|else|while|until|do|exec|env|time|nohup|xargs|sudo|command))[[:space:]]*(python3|python|py)([[:space:]]|$)/ ||
    /(^|[^A-Za-z0-9_$])(export[[:space:]]+)?[A-Za-z_][A-Za-z0-9_]*=["'"'"']?(python3|python|py)["'"'"']?([[:space:]]|;|\)|$)/ \
      { printf "%s:%d:%s\n", F, NR, $0 }
  ' "$1"
}

bare=$(cd "$ROOT" && git ls-files -- '*.sh' | grep -v '^tools/lib/resolve-python' | while IFS= read -r f; do
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
# ...and the ban's own population is real, or it is a gate over nothing.
nsh2=$(cd "$ROOT" && git ls-files -- '*.sh' | grep -cv '^tools/lib/resolve-python' || true)
[ "$nsh2" -gt 10 ] || bad "the invocation ban scanned $nsh2 shell files — the population collapsed"; ok

[ "$st" = 0 ] && echo "PASS — resolve-python: $n assertions held"
exit "$st"
