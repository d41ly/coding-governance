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
#
#   Exit 0 clean · 2 with the refusal on stderr, or a wrong invocation.

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

if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  case "${1:-}:$#" in
    :0) refuse_wrong_shell || exit 2 ;;
    --probe:2)
      _rws_wsl=0
      { [ -n "${WSL_DISTRO_NAME:-}" ] || [ -e /proc/sys/fs/binfmt_misc/WSLInterop ]; } && _rws_wsl=1
      wrong_shell_at "$2" "$_rws_wsl" || exit 0
      echo "refuse_wrong_shell: WSL's bash is running $2 from a Windows checkout under /mnt/;" >&2
      echo "refuse_wrong_shell: run it with Git's bash (C:/Program Files/Git/bin/bash.exe)." >&2
      exit 2
      ;;
    *) echo "usage: bash refuse-wrong-shell.sh [--probe <abs path>]" >&2; exit 2 ;;
  esac
  exit 0
fi
