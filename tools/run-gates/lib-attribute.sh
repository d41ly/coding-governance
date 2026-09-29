#!/usr/bin/env bash
# lib-attribute.sh — the two halves an attribution needs and must not spell twice. SOURCED, never run.
#
# ONE NORMALISER AND ONE SCRATCH-WORKTREE RUNNER, shared by both runners in this kit directory. The
# held-suite baseline (`--attribute` on the self-test runner, TOOL-dDerivedDocket-1) built both
# inline; the bar's red attribution (`GATE_ATTRIBUTE` on the merge-bar runner, TOOL-dDerivedDocket-23)
# needs the same two, and two normalisers disagree about which failure is the same failure. So they
# live here, and each runner sources this file ONLY on the path that attributes: a runner copied into
# a fixture without this file still runs every other mode byte-for-byte as before.
#
# WHAT THE NORMALISER STRIPS, in this order, and NOTHING ELSE: every absolute root it is handed, in
# all three spellings this platform produces; mktemp-shaped directory names; durations; trailing CR
# and whitespace. The restraint is the design. Over-normalising collapses two different failures onto
# one line, which reads a NEW failure as inherited and passes the unit that caused it — the blocker
# this repo's own attribution critique ranked first (KF14). A varying value it does not know reads as
# a difference, which fails toward noise rather than toward a false pass.
#
# WHAT THIS FILE DOES NOT DO: decide a verdict. Each runner owns its own classifier; this file owns
# only the two mechanisms whose divergence would make the two classifiers disagree about their input.
#
# NAMES NOTHING OUTSIDE ITSELF. Every path arrives as an argument (charter §12).

# A string, escaped for use as a literal inside a sed ERE.
render_rx_literal() { printf '%s' "$1" | sed 's,[][(){}.*+?^$\\|],\\&,g'; }

# One absolute root -> its forward-slash, backslash and MSYS `/c/` spellings, one per line.
render_path_spellings() {
  local r=$1 d rest
  printf '%s\n' "$r"
  printf '%s\n' "$(printf '%s' "$r" | tr '/' '\\')"
  case "$r" in
    [A-Za-z]:/*)
      d=$(printf '%s' "$r" | cut -c1 | tr 'A-Z' 'a-z'); rest=${r#?:}
      printf '/%s%s\n' "$d" "$rest" ;;
  esac
}

# write_normaliser <sed-file> <root>... — writes the sed -E program, truncating the file first.
# Apply it with `sed -E -f <sed-file>`. The roots are stripped in the order given.
write_normaliser() {
  local f=$1 root sp; shift
  : > "$f" || return 1
  for root in "$@"; do
    [ -n "$root" ] || continue
    render_path_spellings "$root" | while IFS= read -r sp; do
      [ -n "$sp" ] || continue
      printf 's|%s||g\n' "$(render_rx_literal "$sp")" >> "$f"
    done
  done
  printf '%s\n' 's|tmp\.[A-Za-z0-9]+||g' >> "$f"
  printf '%s\n' 's|\b[0-9]+(\.[0-9]+)?m?s\b||g' >> "$f"
  printf '%s\n' 's|\r$||' >> "$f"
  printf '%s\n' 's|[[:space:]]+$||' >> "$f"
}

# add_scratch_worktree <path> <sha> — a DETACHED worktree of <sha> at <path>. rc 0 on success. The
# caller names the path, places it (under the git COMMON dir, where a long scratch pad cannot push it
# past MAX_PATH) and owns every message: the two runners word their refusals differently.
add_scratch_worktree() { git worktree add --detach "$1" "$2" >/dev/null 2>&1; }

# remove_scratch_worktree <path> — rc 0 when the worktree is gone. The caller reports a failure,
# because an orphaned worktree is removable by hand only if somebody is told its path.
remove_scratch_worktree() { git worktree remove --force "$1" >/dev/null 2>&1; }
