#!/usr/bin/env bash
# lib-verdict.sh — the block table: which attributed red blocks a landing. SOURCED, never run.
#
# ONE FACT, read by the runner alone (TOOL-dWitnessedBar-3 S1). The runner joins each red's class to
# a `block` or a `pass` here and writes the word into its attribution record's ninth field; the
# pre-push hook and the unattended driver read that field and never re-decide it. This file is in
# the runner's KF3 list beside `lib-attribute.sh`, so a diff against R that edits the table reads
# every red OWN: nobody grades their own grader.
#
# The value is `verdict.blocks`, handed to the runner as GATE_VERDICT_BLOCKS:
#
#   class                        own-only  own-mixed-contended  every-red
#   OWN                          block     block                block
#   MIXED                        pass      block                block
#   CONTENDED                    pass      block                block
#   INHERITED                    pass      pass                 block
#   DEAD PROBE                   block     block                block
#   no row, or an unknown class  block     block                block
#
# DENY BY DEFAULT: an unknown value reads `every-red`, and an empty or unknown class blocks. A DEAD
# PROBE blocks under every value, because it means no comparison was made (§8 F1).
#
# NAMES NOTHING OUTSIDE ITSELF. Every input arrives as an argument (the shipped-surface rule check-install-prefix.sh holds).

derive_red_blocks() { # value · class -> prints block or pass
  local v=$1 c=$2
  case "$v" in own-only|own-mixed-contended|every-red) ;; *) v=every-red ;; esac
  case "$v:$c" in
    every-red:*) echo block ;;
    *:INHERITED) echo pass ;;
    own-only:MIXED|own-only:CONTENDED) echo pass ;;
    *) echo block ;;
  esac
}
