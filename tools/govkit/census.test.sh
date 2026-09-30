#!/usr/bin/env bash
# Arms for <prefix>/govkit/census.py — DEPL-dRetiredFork-7.
#
# DELIBERATELY NOT A BAR LEG, and this header states the compensating check rather than leaving
# the exemption bare (§7: an exemption is not coverage). The census reads repositories gov does
# not own; nothing on gov's bar reaches outside this repository, so a leg that ran it would
# either red on a machine where the adopters are absent or pass by finding nothing — the
# green-by-absence shape this build has spent units removing. Compensating check: these arms run
# ON DEMAND against SYNTHETIC repositories built here, so they need no adopter present and are
# the thing to run whenever census.py changes.
#
#   bash <prefix>/govkit/census.test.sh
#
# Every arm below builds its own gov and its own adopter. None of them reads a real adopter tree:
# a fixture that depends on inCMS's current bytes grades a moving target and reports the wrong
# thing on the day inCMS changes.

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
KIT_REL=$(derive_self_rel "$HERE") || { echo "census.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
case "$KIT_REL" in */*) PFX="${KIT_REL%/*}/" ;; *) PFX="" ;; esac
HERE=$(cd "$(dirname "$0")/../.." && pwd)
CENSUS="$HERE/$KIT_REL/census.py"   # this kit's own file, by the directory it sits in (TOOL-aRepatriatedFork-46)

# THROUGH THE ONE RESOLVER, never a bare launcher name. The MS-Store `python3` stub answers
# `command -v` and then exits 9009, so a bare name is not an answer — and the invocation ban in
# `<prefix>/lib/resolve-python.test.sh` refuses one repo-wide, which is how this file was caught:
# it shipped with six bare `python` calls and redded that leg on the closing bar.
# TOOL-aRepatriatedFork-46: carried INLINE; it was sourced from the library directory, which ships nowhere.
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
PY="$(resolve_python)"
n=0; st=0

ok()   { n=$((n+1)); echo "ok   $1"; }
bad()  { n=$((n+1)); echo "FAIL $1"; st=1; }
has()  { case "$1" in *"$2"*) return 0 ;; *) return 1 ;; esac; }

# ---------------------------------------------------------------- a gov with a real HISTORY -----
# Two commits, so exactly one blob per file is HEAD's and exactly one is a prior vintage. Without
# the second commit there is no DRIFT class to test and every arm below would be vacuous.
GOV=$(mktemp -d)
(
  cd "$GOV" && git init -q . && git config user.email t@t && git config user.name t
  mkdir -p ${PFX}kit
  printf 'v1 engine\n' > ${PFX}kit/engine.sh
  printf 'stable\n'    > ${PFX}kit/stable.sh
  git add -A && git commit -q -m v1 --no-verify
  printf 'v2 engine\n' > ${PFX}kit/engine.sh
  git add -A && git commit -q -m v2 --no-verify
) >/dev/null 2>&1

mkadopter() { # $1 = dir; builds a tree with one file of each class
  mkdir -p "$1/.governance" "$1/scripts"
  printf 'stable\n'     > "$1/scripts/stable.sh"   # == gov HEAD          -> IN-SYNC
  printf 'v1 engine\n'  > "$1/scripts/engine.sh"   # == gov's FIRST commit -> DRIFT
  printf 'local only\n' > "$1/scripts/mine.sh"     # in no gov commit ever -> FORK
  cat > "$1/.governance/install.json" <<JSON
{"schema":3,"gov_commit":"none","prefix":"scripts","kits":["kit"],"files":[
 {"path":"scripts/stable.sh","role":"engine","kit":"kit","source":"${PFX}kit/stable.sh"},
 {"path":"scripts/engine.sh","role":"engine","kit":"kit","source":"${PFX}kit/engine.sh"},
 {"path":"scripts/mine.sh","role":"engine","kit":"kit","source":"${PFX}kit/mine.sh"}]}
JSON
  ( cd "$1" && git init -q . && git config user.email t@t && git config user.name t \
      && git add -A && git commit -q -m a --no-verify ) >/dev/null 2>&1
}

# ---- ARM 1: the three classes are actually DISTINGUISHED ----------------------------------------
# The whole thesis of this census is that DRIFT and FORK are different questions. If a stale copy
# and a novel file landed in one bucket the tool would be a HEAD-diff wearing a costume, and every
# number this build rests on would be inflated by every stale copy in every adopter.
A1=$(mktemp -d); mkadopter "$A1"
out=$("$PY" "$CENSUS" --adopter "$A1" --name t --gov "$GOV" 2>&1)
has "$out" "IN-SYNC: 1" && ok "the HEAD-identical file is IN-SYNC" \
                        || bad "IN-SYNC not 1: $(printf '%s' "$out" | head -12)"
has "$out" "DRIFT: 1"   && ok "the file matching gov's FIRST commit is DRIFT, not a fork" \
                        || bad "DRIFT not 1: $(printf '%s' "$out" | head -12)"
has "$out" "FORK: 1"    && ok "the file in no gov commit ever is a FORK" \
                        || bad "FORK not 1: $(printf '%s' "$out" | head -12)"
has "$out" 'scripts/mine.sh' && ok "the fork is NAMED, not just counted" \
                             || bad "the fork was counted but not named"

# ---- ARM 2: AC4, the vacuity refusal, with its FAILING CASE OBSERVED ----------------------------
# Staged deliberately: an adopter whose receipt maps nothing. A census that printed "0 forks" here
# would be indistinguishable from a clean tree, which is the exact defect class this build keeps
# finding. The refusal must be LOUD and the exit code must not be 0.
A2=$(mktemp -d)
mkdir -p "$A2/.governance"
printf '{"schema":3,"prefix":"scripts","kits":[],"files":[]}\n' > "$A2/.governance/install.json"
( cd "$A2" && git init -q . && git config user.email t@t && git config user.name t \
    && git add -A && git commit -q -m e --no-verify ) >/dev/null 2>&1
out=$("$PY" "$CENSUS" --adopter "$A2" --name t --gov "$GOV" 2>&1); rc=$?
[ "$rc" -ne 0 ] && ok "a census mapping ZERO files exits non-zero (got $rc)" \
                || bad "a zero-map census exited 0 — it reported a clean tree it never measured"
has "$out" "REFUSED" && ok "and says REFUSED in as many words" \
                     || bad "no REFUSED in: $out"
has "$out" "cannot report a clean tree" && ok "and says why a zero map is not a clean result" \
                                        || bad "the refusal does not explain itself"

# ---- ARM 3: the refusal is NOT vacuous ---------------------------------------------------------
# ARM 2 alone would pass if the tool refused ALWAYS. This is the negative half, and without it
# ARM 2 proves only that the program can print a word.
out=$("$PY" "$CENSUS" --adopter "$A1" --name t --gov "$GOV" 2>&1); rc=$?
[ "$rc" -eq 0 ] && ok "a census that DOES map files runs to completion" \
                || bad "the tool refuses even a good tree (rc=$rc)"
has "$out" "REFUSED" && bad "a populated census still printed REFUSED" \
                     || ok "and does not print REFUSED"

# ---- ARM 4: an ABSENT file is its own class, never a fork --------------------------------------
# A receipt row whose file was deleted has NO blob to test. Calling that "in no gov commit ever"
# is true and useless: it would put every deleted file in the retirement programme.
A4=$(mktemp -d); mkadopter "$A4"; rm -f "$A4/scripts/mine.sh"
out=$("$PY" "$CENSUS" --adopter "$A4" --name t --gov "$GOV" 2>&1)
has "$out" "ABSENT: 1" && ok "a declared-but-deleted file is ABSENT, not a fork" \
                       || bad "deleted file misclassified: $(printf '%s' "$out" | head -12)"

# ---- ARM 5: the census is READ-ONLY in both trees -----------------------------------------------
# It reads repositories gov does not own. A tool that writes to a foreign tree while measuring it
# would be uninvitable, and nothing else here would catch a stray write.
before_gov=$(cd "$GOV" && git status --porcelain | wc -l)
before_ad=$(cd "$A1" && git status --porcelain | wc -l)
"$PY" "$CENSUS" --adopter "$A1" --name t --gov "$GOV" >/dev/null 2>&1
after_gov=$(cd "$GOV" && git status --porcelain | wc -l)
after_ad=$(cd "$A1" && git status --porcelain | wc -l)
[ "$before_gov" = "$after_gov" ] && [ "$before_ad" = "$after_ad" ] \
  && ok "neither tree changed: the census only reads" \
  || bad "the census dirtied a tree (gov $before_gov->$after_gov, adopter $before_ad->$after_ad)"

# ---- ARM 6: a DRIFT row is not silently promoted when gov's HEAD moves --------------------------
# The regression this guards: re-testing against HEAD only. Move gov forward again; the adopter's
# v1 file must STILL be DRIFT, because v1 is still in the history even though HEAD has left it.
( cd "$GOV" && printf 'v3 engine\n' > ${PFX}kit/engine.sh && git add -A \
    && git commit -q -m v3 --no-verify ) >/dev/null 2>&1
out=$("$PY" "$CENSUS" --adopter "$A1" --name t --gov "$GOV" 2>&1)
has "$out" "DRIFT: 1" && ok "a vintage stays DRIFT after gov's HEAD moves past it again" \
                      || bad "moving HEAD reclassified a vintage: $(printf '%s' "$out" | head -12)"

rm -rf "$GOV" "$A1" "$A2" "$A4"
echo "census.test.sh: $n arms, $([ $st -eq 0 ] && echo PASS || echo FAIL)"
exit $st
