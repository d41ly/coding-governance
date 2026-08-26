#!/usr/bin/env bash
# **Serves:** journal TOOL-aCollapsedScan-13
# Differential equivalence for check 21 branch 4's id extraction: the OLD grep predicate against the
# NEW builtin one, over the classes closing-review round 3 named plus a sweep.
set -u
FAM_ALT=${FAM_ALT:-PLAY|KICK|TOOL|DEPL}
FAMILIES=${FAMILIES:-playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL}

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

CASES="TOOL-1 DEPL-007 ARCH-12ab PLAY-1 TOOL-aFoo-12 TOOL-aFoo-12a TOOL-aFoo-1-extra
KICK-bBar-9 DEPL-dBaz-100 TOOL-aFoo TOOL- TOOL -aFoo-1 NOPE-aFoo-1 TOOL-aFoo-x
TOOL-a1B2-07 tool-aFoo-1 TOOL--1 TOOL-aFoo-0 review-TOOL-aFoo-1"
# plus a sweep over shapes
for f in PLAY KICK TOOL DEPL NOPE; do
  for s in aFoo a1 1 1a "" X; do
    for n in 1 007 12a "" x 0; do
      CASES="$CASES $f-$s-$n $f-$s $f$s$n"
    done
  done
done

bad=0; n=0
for c in $CASES; do
  n=$((n+1))
  o=$(old "$c"); w=$(new "$c")
  if [ "$o" != "$w" ]; then bad=$((bad+1)); printf 'DIVERGE  rest=%-22s old=[%s] new=[%s]\n' "$c" "$o" "$w"; fi
done
printf 'checked %d input(s), %d divergence(s)\n' "$n" "$bad"

# the hyphenated-family case the old first-segment code could not handle
echo "--- hyphenated FAMILY (adopter case)"
FAM_ALT='MY-FAM' FAMILIES='x:MY-FAM'
o=$(printf '%s\n' 'MY-FAM-aSlug-1' | grep -oE "^(MY-FAM)-[A-Za-z0-9]+-[0-9]+" || true)
w=$(FAMILIES='x:MY-FAM' new 'MY-FAM-aSlug-1')
printf '  rest=MY-FAM-aSlug-1  old=[%s] new=[%s]  %s\n' "$o" "$w" "$([ "$o" = "$w" ] && echo AGREE || echo DIVERGE)"
[ "$bad" = 0 ] && [ "$o" = "$w" ]
