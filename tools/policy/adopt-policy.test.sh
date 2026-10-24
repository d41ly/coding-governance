#!/usr/bin/env bash
# adopt-policy.test.sh — the policy kit adopter's sibling suite (TOOL-dGroundRules-21 S4): one arm per
# refusal branch of adopt-policy.sh, each planted in a scratch target, so `check-arms.py` reads every
# `exit 1` of the adopter as armed, and `check_policy.py --fixture adopter-suite` runs this file, so a
# leg executes what it reads. It also holds the two outcomes the branches sit beside: `--check` over a
# target its arms red, and `--scaffold` over a target with no commit.
#
#   bash <this kit>/adopt-policy.test.sh     # exit 0 every arm held, 1 one did not
set -u
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null
case "$0" in */*) HERE=${0%/*} ;; *) HERE=. ;; esac
HERE="$(cd "$HERE" && pwd)"
TOOL="$HERE/adopt-policy.sh"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0
ok() { echo "PASS $1"; pass=$((pass+1)); }
bad() { echo "FAIL $1"; echo "     $2"; fail=$((fail+1)); }
mkrepo() { # name [commit] -> a scratch target at $TMP/<name>, on main, committed once when asked
  R="$TMP/$1"; mkdir -p "$R"; git -C "$R" init -q; git -C "$R" symbolic-ref HEAD refs/heads/main
  git -C "$R" config user.email t@t; git -C "$R" config user.name t; git -C "$R" config core.autocrlf false
  if [ "${2:-}" = commit ]; then
    printf 'a target\n' > "$R/README.md"; git -C "$R" add -A; git -C "$R" commit -qm target
  fi
}
want() { # label · exit wanted · text the output must carry · adopter args...
  local label=$1 rc=$2 text=$3 out got; shift 3
  out=$(bash "$TOOL" "$@" 2>&1); got=$?
  if [ "$got" = "$rc" ] && [[ "$out" == *"$text"* ]]; then ok "$label (exit $got)"
  else bad "$label" "exit $got, want $rc carrying '$text': $out"; fi
}

# 1 — a .governance that is a file, not a directory: the directory cannot be made.
mkrepo gov-file commit; printf 'not a directory\n' > "$R/.governance"
want "--scaffold where .governance is a file refuses" 1 'policy: the directory .governance could not be made in ' --scaffold --target "$R"

# 2 — the scaffold's temporary file is a directory: the scaffold cannot be written.
mkrepo tmp-dir commit; mkdir -p "$R/.governance/policy.toml.tmp"
want "--scaffold where the scaffold cannot be written refuses" 1 'policy: the scaffold could not be written to ' --scaffold --target "$R"

# 3 — a settings file that is no JSON object: the render refuses, so --scaffold does.
mkrepo bad-settings commit; mkdir -p "$R/.claude"; printf '{\n' > "$R/.claude/settings.json"
want "--scaffold where the settings render fails refuses" 1 'policy: the harness settings could not be rendered in ' --scaffold --target "$R"

# 3b — a mirror refusal that is no `uncommitted changes` stands (TOOL-dGroundRules-31 S2): a scratch
# copy of the adopter beside a policy.py staged to exit 2 on `mirror`, over a committed policy file.
mkdir -p "$TMP/kit"; cp "$TOOL" "$TMP/kit/adopt-policy.sh"
printf 'import sys\nif sys.argv[1:2] == ["mirror"]:\n    print("policy: refused - a planted mirror refusal")\n    sys.exit(2)\n' > "$TMP/kit/policy.py"
mkrepo mirror-refused commit; mkdir -p "$R/.governance"; printf '' > "$R/.governance/policy.toml"
git -C "$R" add -A; git -C "$R" commit -qm policy
TOOL="$TMP/kit/adopt-policy.sh"
want "--scaffold where the mirror refuses otherwise refuses" 1 'policy: the policy mirror could not be rendered in ' --scaffold --target "$R"
want "--scaffold prints the mirror's own refusal" 1 'policy: refused - a planted mirror refusal' --scaffold --target "$R"
TOOL="$HERE/adopt-policy.sh"

# 3c — an invalid policy file written before the install-day --scaffold is refused through
# check_policy.py's arm_schema, never deferred (TOOL-dGroundRules-34 S20): the real control flow.
mkrepo invalid commit; mkdir -p "$R/.governance"
printf '[policy-file]\non-invalid = "refuse"\n\n[budgets]\nenforce = "bogus"\n' > "$R/.governance/policy.toml"
out=$(bash "$TOOL" --scaffold --target "$R" 2>&1); got=$?
if [ "$got" = 2 ] && [[ "$out" == *"budgets.enforce"* ]] && [[ "$out" != *"mirror deferred"* ]]; then
  ok "--scaffold over an invalid policy file on install day refuses (exit $got)"
else bad "--scaffold over an invalid policy file on install day refuses" "exit $got, want 2 naming budgets.enforce and no 'mirror deferred': $out"; fi

# 4 — the outcomes beside the branches: a committed target is scaffolded and its settings rendered;
# a re-run keeps the file and renders again; a target with no commit names the re-run.
mkrepo fresh commit
want "--scaffold over a committed target writes the file" 0 'wrote    ' --scaffold --target "$R"
want "--scaffold defers the mirror over the uncommitted file" 0 'adopt-policy: mirror deferred · .governance/policy.toml has uncommitted changes' --scaffold --target "$R"
if [ -f "$R/.claude/settings.json" ] && grep -q CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS "$R/.claude/settings.json"; then
  ok "--scaffold rendered the harness settings"
else bad "--scaffold rendered the harness settings" "no .claude/settings.json carrying the limit under $R"; fi
want "--scaffold over a kept file renders again" 0 'kept     ' --scaffold --target "$R"
mkrepo empty
want "--scaffold with no commit names the re-run" 0 're-run --scaffold after the first commit' --scaffold --target "$R"

# 5 — --check is check_policy.py --repo, whose exit it returns: a value its row refuses reds it.
mkrepo zero commit; mkdir -p "$R/.governance"; printf '[runtime]\nagents-in-flight = 0\n' > "$R/.governance/policy.toml"
want "--check over agents-in-flight = 0 exits 1" 1 'runtime.agents-in-flight' --check --target "$R"

echo "==== $pass passed, $fail failed ===="
[ "$fail" = 0 ]
