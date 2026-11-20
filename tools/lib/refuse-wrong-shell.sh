#!/usr/bin/env bash
# The one wrong-shell refusal: WSL's bash running a gov script from a Windows checkout (TOOL-dWitnessedBar-27).
#
# WSL mounts a Windows drive at `/mnt/<drive>/`, so a gov script that WSL's bash starts from a Windows
# checkout runs against a Linux interpreter and another filesystem's view of the tree (AP-33). The
# block below refuses that at once and names Git's bash. Two facts decide it, each read with
# builtins only, so it adds no fork to any entry point: the hosting file's own path under a
# single-letter `/mnt/<drive>/`, and a WSL marker (`WSL_DISTRO_NAME`, or WSL's interop entry under
# `/proc`). The deliberate WSL mirror of `<prefix>/run-gates/run-held-wsl.sh`, on WSL's own disk, and
# a Linux node's own bash, which carries no marker, stay green.
#
# USAGE — an entry point that carries the `resolve_python` block INLINE carries this block directly
# after it, byte-identical, and the line after `# <<< refuse_wrong_shell` is the call. One that
# SOURCES `resolve-python.sh` sources this file from the same directory on the next line, then calls:
#
#   . "$HERE/resolve-python.sh"
#   . "$HERE/refuse-wrong-shell.sh"
#   refuse_wrong_shell || exit 2
#
# `resolve-python.test.sh` gates every inline copy against this one and both shapes over the
# population; `resolve-python.sh` itself carries neither, being only ever sourced.
#
# Run rather than sourced, it is a probe, and sourced it runs nothing:
#
#   bash <prefix>/lib/refuse-wrong-shell.sh                  # judges this file's own location
#   bash <prefix>/lib/refuse-wrong-shell.sh --probe <path>   # judges <path>, an absolute path
#   bash <prefix>/lib/refuse-wrong-shell.sh --coverage       # holds the derived population to the refusal
#
#   Exit 0 clean · 1 a coverage break, each naming its file · 2 with the refusal on stderr, or a wrong
#   invocation.
#
# THE POPULATION IS A PREDICATE, NEVER A LIST (TOOL-dWitnessedBar-50 S1): every tracked shell file under
# tools/, skills/ and .githooks/ (one named *.sh, or whose first line is a bash or sh shebang) that
# carries a `# >>> resolve_python` block or calls resolve_python at command position (opening a `$(` or
# backtick command substitution, or the first word of a command after whitespace, `;`, `&`, `|`, `!`, a
# group's `{` or `(`, `if`, `then`, `do`, `else`, `elif`, `while` or `until`, with no `#` before it on its
# line, never a `resolve_python()` definition) outside such a block (TOOL-dWitnessedBar-57 S1,
# TOOL-dWitnessedBar-62 S25);
# resolve-python.sh itself is outside it, and `--coverage` names it dropped with that reason (S4).
# A typed list missed .githooks/pre-commit, which sources the resolver from a path it derives at run
# time. `--coverage` derives it, prints its count and each named exclusion with its reason, and exits 1
# naming each member that neither carries this block nor sources this file, or never calls
# `refuse_wrong_shell || exit 2`, or whose first such line outside the block does not precede its first
# line calling resolve_python outside a `# >>> resolve_python` block and outside a function body
# (TOOL-dWitnessedBar-51 S29), and each exclusion written without a reason. WHAT IT DOES NOT CHECK: a
# function whose body resolves python, called at top level above the refusal, which the text order
# does not follow; and that a named exclusion is still selected by the predicate.

# >>> refuse_wrong_shell — canonical copy: refuse-wrong-shell.sh in gov's lib dir (byte-identical; gated)
wrong_shell_at() {   # <abs path> <wsl 0|1>; returns 0 when the path is a Windows checkout under WSL
  [ "$2" = 1 ] || return 1
  case "$1" in /mnt/[a-z]/*) return 0 ;; esac
  return 1
}
refuse_wrong_shell() {
  _rws_wsl=0
  { [ -n "${WSL_DISTRO_NAME:-}" ] || [ -e /proc/sys/fs/binfmt_misc/WSLInterop ]; } && _rws_wsl=1
  _rws_p=${BASH_SOURCE[0]:-$0}
  case "$_rws_p" in /*) ;; *) _rws_p=$PWD/$_rws_p ;; esac
  wrong_shell_at "$_rws_p" "$_rws_wsl" || return 0
  echo "refuse_wrong_shell: WSL's bash is running $_rws_p from a Windows checkout under /mnt/;" >&2
  echo "refuse_wrong_shell: run it with Git's bash (C:/Program Files/Git/bin/bash.exe)." >&2
  return 1
}
# <<< refuse_wrong_shell

# THE CALL, read alike by both readers below (TOOL-dWitnessedBar-57 S1, widened by TOOL-dWitnessedBar-62
# S25): the name opening a command substitution, `$(` or a backtick, after optional whitespace; or the
# name as the first word of a command, after optional whitespace, at the line's start or after a `;`,
# `&`, `|` or `!`, after a `{` or `(` opening a group, or after the words `if`, `then`, `do`, `else`,
# `elif`, `while` or `until`, so an indented call is one. A match with a `#` before it on its line is no
# call: the line is cut at its first `#` before it is read. A `resolve_python()` definition, a test's
# stub included, is taken out of the line before it is read, so it is never a call (S3).
RWS_CALL_AWK='
function check_rws_call(l,   h) {
  h = index(l, "#"); if (h) l = substr(l, 1, h - 1)
  gsub(/resolve_python[ \t]*\([ \t]*\)/, "", l)
  return l ~ /(\$\(|`)[ \t]*resolve_python([^A-Za-z0-9_]|$)/ \
    || l ~ /(^|[;&|!])[ \t]*resolve_python([^A-Za-z0-9_]|$)/ \
    || l ~ /(^|[ \t;&|])[({][ \t]*resolve_python([^A-Za-z0-9_]|$)/ \
    || l ~ /(^|[^A-Za-z0-9_])(if|then|do|else|elif|while|until)[ \t]+resolve_python([^A-Za-z0-9_]|$)/
}'

derive_rws_population() {  # <repo root> <resolve-python.sh rel> -> one member path per line (S1)
  (cd "$1" && unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE && git ls-files -- tools skills .githooks) | (cd "$1" && awk "$RWS_CALL_AWK"'
    {
      f = $0; first = 1; b = 0; c = 0; i = 0
      while ((getline l < f) > 0) {
        if (first) { first = 0; if (f !~ /\.sh$/ && l !~ /^#!.*[^A-Za-z0-9_](ba)?sh([^A-Za-z0-9_]|$)/) break }
        sub(/\r$/, "", l)
        if (l ~ /^# >>> resolve_python/) { b = 1; i = 1; continue }
        if (l ~ /^# <<< resolve_python/) { i = 0; continue }
        if (!i && check_rws_call(l)) c = 1
      }
      close(f)
      if ((b || c) && f != canon) print f
    }' canon="$2")
}

# A line inside a function body defined at column 0 calls nothing where it stands, so the order read
# skips it: the first resolve_python CALL is the first one the file's own top level runs.
scan_rws_order() {  # <repo root>, member paths on stdin -> `o <path>|<refusal line>|<first resolve_python call line>`
  (cd "$1" && awk "$RWS_CALL_AWK"'
    {
      f = $0; n = 0; i = 0; fn = 0; rws = 0; rp = 0
      while ((getline l < f) > 0) {
        n++; sub(/\r$/, "", l)
        if (l ~ /^# >>> resolve_python/) { i = 1; continue }
        if (l ~ /^# <<< resolve_python/) { i = 0; continue }
        if (i) continue
        if (fn) { if (l ~ /^}/) fn = 0; continue }
        if (l ~ /^(function[ \t]+)?[A-Za-z_][A-Za-z0-9_]*[ \t]*(\(\))?[ \t]*\{/) { if (l !~ /}[ \t;]*$/) fn = 1; continue }
        if (!rws && l ~ /^[ \t]*refuse_wrong_shell \|\| exit 2[ \t]*$/) rws = n
        if (!rp && check_rws_call(l)) rp = n
      }
      close(f)
      print "o " f "|" rws "|" rp
    }')
}

if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  case "${1:-}:$#" in
    :0) refuse_wrong_shell || exit 2 ;;
    --coverage:1)
      # S2 — each one the predicate selects, outside because a file it sources or is sourced by
      # refuses before its first call. `<path>|<reason>`; a row with no reason is refused, not honoured.
      _rws_here=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd) || exit 2
      _rws_lib=$(cd "$_rws_here" && unset GIT_DIR GIT_WORK_TREE && git rev-parse --show-prefix) \
        && _rws_root=$(cd "$_rws_here/$(cd "$_rws_here" && unset GIT_DIR GIT_WORK_TREE && git rev-parse --show-cdup)" && pwd) \
        || { echo "refuse_wrong_shell: --coverage: $_rws_here is not inside a git work tree" >&2; exit 2; }
      # the exclusions sit under the install prefix this file derives, the kit named once (install-prefix)
      _rws_ux="${_rws_lib%lib/}unattended"
      _rws_excl="$_rws_ux/lib-unattended.sh|sourced by members, and each of its calls sits behind \`declare -F resolve_python\`
$_rws_ux/pass-tree.sh|sources $_rws_ux/unattended.sh, an inline member that refuses as it is sourced, before its call
$_rws_ux/pass-tree.test.sh|sources $_rws_ux/unattended.sh, an inline member that refuses as it is sourced, before its call"
      _rws_pop=$(derive_rws_population "$_rws_root" "${_rws_lib}resolve-python.sh")
      _rws_out=$(
        cd "$_rws_root" && unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE || exit 2
        { printf '%s\n' "$_rws_excl" | sed 's/^/x /'
          printf '%s\n' "$_rws_pop" | sed 's/^/m /'
          printf '%s\n' "$_rws_pop" | scan_rws_order "$_rws_root"
          git grep -l '^# >>> refuse_wrong_shell' -- tools skills .githooks | sed 's/^/b /'
          git grep -l -E '^[[:space:]]*(\.|source)[[:space:]]+[^[:space:]]*refuse-wrong-shell\.sh' -- tools skills .githooks | sed 's/^/s /'
          git grep -l -E '^[[:space:]]*refuse_wrong_shell \|\| exit 2[[:space:]]*$' -- tools skills .githooks | sed 's/^/c /'
        } | awk -v drop="${_rws_lib}resolve-python.sh" '
          { t = substr($0, 1, 1); k = substr($0, 3); if (k == "") next }
          t == "x" { p = k; r = ""; if (index(k, "|")) { p = substr(k, 1, index(k, "|") - 1); r = substr(k, index(k, "|") + 1) }
                     if (r ~ /^[ \t]*$/) bad[++nb] = "exclusion " p " carries no reason, so it is refused"
                     else { ex[p] = r; xo[++nx] = p }
                     next }
          t == "m" { m[++nm] = k; next }
          t == "o" { split(k, o, "|"); orws[o[1]] = o[2] + 0; orp[o[1]] = o[3] + 0; next }
          { s[t, k] = 1 }
          END {
            for (j = 1; j <= nm; j++) {
              f = m[j]
              if (f in ex) continue
              n++
              if (!s["b", f] && !s["s", f]) bad[++nb] = f " neither carries the refuse_wrong_shell block nor sources refuse-wrong-shell.sh"
              if (!s["c", f]) bad[++nb] = f " never calls refuse_wrong_shell || exit 2"
              else if (orp[f] && (!orws[f] || orws[f] > orp[f])) bad[++nb] = f " refuses only after it resolved python: its first refuse_wrong_shell || exit 2 is line " orws[f] ", its first resolve_python call line " orp[f]
            }
            print "refuse_wrong_shell coverage: " (n + 0) " members, derived from " (nm + 0) " files the predicate selects less " (nx + 0) " named exclusions"
            for (j = 1; j <= nx; j++) print "  excluded: " xo[j] " (" ex[xo[j]] ")"
            print "  dropped: " drop " (TOOL-dWitnessedBar-27'"'"'s listed member the predicate excludes: it is only ever sourced, so it carries no refuse_wrong_shell || exit 2 its sourcer would run)"
            if (n + 0 == 0) bad[++nb] = "the predicate derived an empty population, which judges nothing"
            for (j = 1; j <= nb; j++) print "BREAK " bad[j]
            exit (nb > 0)
          }'
      ) && { printf '%s\n' "$_rws_out"; exit 0; }
      printf '%s\n' "$_rws_out"
      exit 1
      ;;
    --probe:2)
      _rws_wsl=0
      { [ -n "${WSL_DISTRO_NAME:-}" ] || [ -e /proc/sys/fs/binfmt_misc/WSLInterop ]; } && _rws_wsl=1
      wrong_shell_at "$2" "$_rws_wsl" || exit 0
      echo "refuse_wrong_shell: WSL's bash is running $2 from a Windows checkout under /mnt/;" >&2
      echo "refuse_wrong_shell: run it with Git's bash (C:/Program Files/Git/bin/bash.exe)." >&2
      exit 2
      ;;
    *) echo "usage: bash refuse-wrong-shell.sh [--probe <abs path> | --coverage]" >&2; exit 2 ;;
  esac
  exit 0
fi
