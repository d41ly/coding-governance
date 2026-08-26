#!/usr/bin/env bash
# render-doc.sh — the ONE canonical `render_doc`, and the file every inline copy is gated against.
#
# WHAT IT DOES. Substitutes a kit template's two placeholders — `{{KIT_DIR}}` and `{{TOOL_ROOT}}` —
# and prints the result. It exists because a document the ADOPTER commits must not carry whatever
# prefix the SHIPPING repo happened to use: `apply` writes gov's bytes verbatim, so a verbatim copy
# of a template stamps gov's own layout into a file the adopter now owns.
#
# WHY IT IS A FILE. There were two spellings of it — one in `adopt-memory-tree.sh` and one in
# `kit-dogfood-parity.test.sh`, whose own comment named itself as the drift class and then left the
# drift in place. A kit that is COPY-INSTALLED as a standalone directory cannot source this file
# (`../lib/` does not exist in the adopting repo), so those scripts carry the block between the
# markers below INLINE, byte-identical, and `resolve-python.test.sh`'s parity table gates every copy
# against this one — the same mechanism, the same marker grammar, one more row.
#
# THE CALLER SUPPLIES `KIT_REL` AND `TOOL_ROOT`. Both are the caller's, deliberately: the adopter
# script derives them from where it was invoked, and the parity test derives them from the kit it is
# grading. A block that read them from its own location would answer for the wrong tree in one of
# the two callers, which is how the second spelling was born in the first place.
# DEPL-dCarriedReceipt-15 S6.

# >>> render_doc — canonical copy: tools/lib/render-doc.sh (byte-identical; gated)
render_doc() {
  # No `sed`: a substituted value carrying `|` closes the s||| delimiter and `&` re-inserts the
  # whole match. Parameter substitution has neither, PROVIDED the replacement is quoted — bash
  # 5.1 gave an unquoted one the same `&` meaning sed has.
  # The `X` sentinel is because `$( )` strips ALL trailing newlines. `cat` runs in its own
  # subshell with an explicit `exit 1` because the substitution reports the LAST command's
  # status, which is printf's and always 0 — the guard was unreachable without it.
  local out
  out=$( cat "$1" || exit 1; printf X ) || return 1
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{KIT_DIR\}\}/"$KIT_REL"}
  out=${out//\{\{TOOL_ROOT\}\}/"$TOOL_ROOT"}
  printf '%s' "$out"
}
# <<< render_doc
