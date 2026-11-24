#!/usr/bin/env bash
# template-cache.sh — the bash face of the suite template cache (TOOL-dQuietDisk-7 S6).
#
# The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so the block below travels
# INLINE, byte-identical, in `lib-selftest.sh` beside this file and in any copy-installed suite, and
# `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts. The protocol both
# faces implement is stated once, in `template_cache.py`'s module docstring beside this file.
#
# USAGE — source it, then:
#
#   root=$(resolve_template_root) || exit 2              # S2's one rule for the cache root
#   key=$(derive_template_key <builder> <input file>...) || exit 2
#   t=$(resolve_template "$root" "$key" <builder> [<arg>...]) || exit 2   # <root>/<key>/repo, or
#                                                        # <root>/<the key folded with the args>/repo
#   build_template_clone "$t" <dest> || exit 2           # a --shared clone, no remote
#   mode=$(read_template_mode <python> <policy.py>)      # tests.fixture-templates: per-case or shared
#
# resolve_template says `template: <key8> built` or `template: <key8> reused` once on stderr, and
# its builder's own output goes there too, so stdout carries the template path alone. Every call
# but the clone and the key is builtins; the key is two `git hash-object` processes, the clone
# three git processes, and a resolve_template call carrying builder arguments one more
# `git hash-object`, which folds each argument's `%q` line into the key it names its directory by,
# so two argument lists never share a template. The key, the template and the clone each run in a
# subshell that first calls remove_git_env_leaks, so no git call and no builder sees an inherited
# GIT_DIR or its eleven kin; resolve_template_root and read_template_mode run no git and keep the
# caller's environment (TOOL-dQuietDisk-36). WHAT THIS DOES NOT CHECK: a builder function's helpers,
# whose definitions the key does not read, a value a builder reads from its environment rather than
# from its arguments, which no key folds, and a template a racing run left half-built, which no
# `ready` names.

# >>> template_cache_sh — canonical copy: template-cache.sh in gov's lib dir (byte-identical; gated)
resolve_template_root() { # -> the cache root: SELFTEST_TEMPLATE_ROOT, a bar's owned $WORK, or $SELFTEST_ROOT
  local _tc_d=${TMPDIR:-/tmp} _tc_p
  if [ -n "${SELFTEST_TEMPLATE_ROOT:-}" ] && [ -d "$SELFTEST_TEMPLATE_ROOT" ]; then
    printf '%s\n' "$SELFTEST_TEMPLATE_ROOT"; return 0
  fi
  while [ -n "$_tc_d" ]; do
    case ${_tc_d##*/} in gate-work.*) [ -f "$_tc_d/owner" ] && { printf '%s\n' "$_tc_d/templates"; return 0; } ;; esac
    _tc_p=${_tc_d%/*}; [ "$_tc_p" = "$_tc_d" ] && break; _tc_d=$_tc_p
  done
  [ -n "${SELFTEST_ROOT:-}" ] || { echo "template-cache: no root: no SELFTEST_TEMPLATE_ROOT, no owned gate-work, no SELFTEST_ROOT" >&2; return 2; }
  printf '%s\n' "$SELFTEST_ROOT/templates"
}
remove_git_env_leaks() { # unsets, in the calling subshell, the names GIT_ENV_LEAKS drops
  unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES \
    GIT_COMMON_DIR GIT_NAMESPACE GIT_PREFIX GIT_LITERAL_PATHSPECS GIT_GLOB_PATHSPECS \
    GIT_NOGLOB_PATHSPECS GIT_ICASE_PATHSPECS
}
derive_template_key() ( # <builder> [<input file>...] -> the key, 40 hex, from the builder's definition and the inputs' blob ids
  remove_git_env_leaks
  local -; set -o pipefail
  local _tc_b=$1; shift
  { printf 'template-cache v1\nbash\n%s\n' "$_tc_b"
    declare -f "$_tc_b"
    printf 'input %s\n' "$@"
    [ "$#" -eq 0 ] || git hash-object --no-filters -- "$@"
  } | git hash-object --stdin
)
resolve_template() ( # <root> <key> <builder> [<arg>...] -> <root>/<key>/repo, <key> folding the args; built once per root
  remove_git_env_leaks
  local _tc_r=$1 _tc_k=$2 _tc_l _tc_n; shift 2
  if [ "$#" -gt 1 ]; then
    _tc_k=$({ printf 'template-cache args v1\n%s\n' "$_tc_k"; printf '%q\n' "${@:2}"; } | git hash-object --stdin) \
      || { echo "template-cache: the key of $1's arguments could not be derived" >&2; return 2; }
  fi
  local _tc_dir="$_tc_r/$_tc_k" _tc_s="$_tc_r/.stage-$_tc_k-$BASHPID"
  local -a _tc_c=(-c core.autocrlf=false -c core.hooksPath= -c commit.gpgsign=false -c user.name=t -c user.email=t@e)
  if [ -e "$_tc_dir/ready" ]; then
    echo "template: ${_tc_k:0:8} reused" >&2; printf '%s\n' "$_tc_dir/repo"; return 0
  fi
  mkdir -p "$_tc_s/repo" || return 2
  if ! ( cd "$_tc_s/repo" && "$@" ) >&2; then
    rm -rf "$_tc_s"; echo "template-cache: the builder $1 failed, so no template was made" >&2; return 2
  fi
  [ -e "$_tc_s/repo/.git" ] || git -C "$_tc_s/repo" init -q --template= || { rm -rf "$_tc_s"; return 2; }
  git -C "$_tc_s/repo" "${_tc_c[@]}" add -A || { rm -rf "$_tc_s"; return 2; }
  if ! git -C "$_tc_s/repo" "${_tc_c[@]}" commit -q -m base >/dev/null 2>&1; then
    # NOTHING TO COMMIT is a builder that committed its own tree, and only that is not a failure.
    git -C "$_tc_s/repo" rev-parse -q --verify 'HEAD^{commit}' >/dev/null && git -C "$_tc_s/repo" diff --cached --quiet \
      || { rm -rf "$_tc_s"; echo "template-cache: the commit of $1's tree failed" >&2; return 2; }
  fi
  git -C "$_tc_s/repo" config --local --list > "$_tc_s/config-all" || { rm -rf "$_tc_s"; return 2; }
  : > "$_tc_s/config-pins"
  while IFS= read -r _tc_l; do
    _tc_l=${_tc_l%$'\r'}; _tc_n=${_tc_l%%=*}
    case $_tc_n in
      remote.*|branch.*|core.repositoryformatversion|core.filemode|core.bare|core.logallrefupdates) ;;
      core.symlinks|core.ignorecase|core.precomposeunicode|'') ;;
      *) printf '%s\n' "$_tc_l" >> "$_tc_s/config-pins" ;;
    esac
  done < "$_tc_s/config-all"
  rm -f "$_tc_s/config-all"; : > "$_tc_s/ready"
  # `mv -T` FAILS onto the key directory, which is never empty; a plain `mv` would nest the stage in it.
  if mv -T "$_tc_s" "$_tc_dir" 2>/dev/null; then
    echo "template: ${_tc_k:0:8} built" >&2
  else
    rm -rf "$_tc_s"
    [ -e "$_tc_dir/ready" ] || { echo "template-cache: could not place $_tc_dir" >&2; return 2; }
    echo "template: ${_tc_k:0:8} reused" >&2
  fi
  printf '%s\n' "$_tc_dir/repo"
)
build_template_clone() ( # <template repo> <dest> -> a --shared clone carrying the template's config pins and no remote
  remove_git_env_leaks
  local _tc_l; local -a _tc_p=()
  while IFS= read -r _tc_l; do [ -n "$_tc_l" ] && _tc_p+=(-c "$_tc_l"); done < "${1%/*}/config-pins" || return 2
  git -c core.autocrlf=false clone --shared --quiet --template= -o template-source ${_tc_p[@]+"${_tc_p[@]}"} "$1" "$2" \
    && git -C "$2" remote remove template-source
)
read_template_mode() { # <python> <policy.py> -> per-case or shared: tests.fixture-templates, shared unless the reader says per-case
  local _tc_v
  if [ -n "${1:-}" ] && [ -f "${2:-}" ] && _tc_v=$("$1" "$2" get tests.fixture-templates 2>/dev/null) \
     && [ "${_tc_v%$'\r'}" = per-case ]; then echo per-case; else echo shared; fi
}
# <<< template_cache_sh
