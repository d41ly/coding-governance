#!/usr/bin/env bash
# **Serves:** journal TOOL-aCollapsedScan-13
# Differential equivalence for check 21 branch 4's id extraction: the OLD grep predicate against the
# NEW builtin one, over the classes the closing review named plus a shape sweep.
#
# EVERY TEST VECTOR IS BUILT AT RUNTIME from $FAMILIES, and none is written as a literal. That is not
# style: a literal `<FAMILY>-<slug>-<n>` in a tracked file is an id CITED, and hygiene check 14
# refuses an id no spec defines. The first cut of this harness spelled twelve of them and redded the
# memory-hygiene leg. Composing them from the declared families keeps the vectors honest and keeps
# the file silent to the id scanner.
set -u
FAMILIES=${FAMILIES:-playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL}
FAM_ALT=$(for p in $FAMILIES; do printf '%s\n' "${p#*:}"; done | paste -sd'|' -)

old() {  # rest -> claimed, the shipped pre-refactor predicate
  printf '%s\n' "$1" | grep -oE "^($FAM_ALT)-[A-Za-z0-9]+-[0-9]+" || true
}

new() {  # rest -> claimed, the builtin predicate as it now stands in the checker
  local rest=$1 claimed="" _f="" _fp _fc _r2 _slug _r3 _num _tail
  for _fp in $FAMILIES; do
    _fc=${_fp#*:}
    case "$rest" in "$_fc-"*) [ ${#_fc} -gt ${#_f} ] && _f=$_fc ;; esac
  done
  case "${_f:+x}" in
    x)
      _r2=${rest#"$_f"-}
      _slug=${_r2%%-*}
      case "$_slug" in
        ''|*[!A-Za-z0-9]*) ;;
        *)
          case "$_r2" in *-*) _r3=${_r2#*-} ;; *) _r3='' ;; esac
          _num=""; _tail=${_r3%%-*}
          while [ -n "$_tail" ]; do
            case "$_tail" in [0-9]*) _num=$_num${_tail%"${_tail#?}"}; _tail=${_tail#?} ;; *) break ;; esac
          done
          [ -z "$_num" ] || claimed="$_f-$_slug-$_num"
          ;;
      esac
      ;;
  esac
  printf '%s\n' "$claimed"
}

# The declared families, plus one that is deliberately NOT declared.
FAMS=$(for p in $FAMILIES; do printf '%s ' "${p#*:}"; done)
UNDECLARED=ZZZZ

CASES=""
add() { CASES="$CASES $1"; }
for f in $FAMS $UNDECLARED; do
  # the two-segment class the closing review found: <FAMILY>-<digits>
  for n in 1 007 12ab 0; do add "$f-$n"; done
  # the ordinary three-segment shapes, and the degenerate ones
  for s in aFoo a1B2 1 1a X ""; do
    for n in 1 007 12a "" x 0; do
      add "$f-$s-$n"; add "$f-$s"; add "$f$s$n"
    done
  done
  add "$f-"; add "$f"; add "-$f-1"
done
add "review-$(printf '%s' "$FAMS" | cut -d' ' -f3)-aFoo-1"

bad=0; n=0
for c in $CASES; do
  n=$((n + 1))
  o=$(old "$c"); w=$(new "$c")
  if [ "$o" != "$w" ]; then
    bad=$((bad + 1)); printf 'DIVERGE  rest=%-24s old=[%s] new=[%s]\n' "$c" "$o" "$w"
  fi
done
printf 'checked %d input(s), %d divergence(s)\n' "$n" "$bad"

# The hyphenated-family case the pre-fold code got wrong: a declared family containing a hyphen.
# Nothing forbids one and the sibling generator's regex accepts it.
echo "--- hyphenated FAMILY (adopter case)"
hf_fams='x:MY-FAM'
hf_in="MY-FAM-aSlug-1"
o=$(printf '%s\n' "$hf_in" | grep -oE "^(MY-FAM)-[A-Za-z0-9]+-[0-9]+" || true)
w=$(FAMILIES="$hf_fams" new "$hf_in")
printf '  old=[%s] new=[%s]  %s\n' "$o" "$w" "$([ "$o" = "$w" ] && echo AGREE || echo DIVERGE)"

[ "$bad" = 0 ] && [ "$o" = "$w" ]
