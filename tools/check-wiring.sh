#!/usr/bin/env bash
# check-wiring.sh — detect coding-governance tools installed-but-unwired in THIS repo, and
# (with --fix/--session) wire the zero-risk ones. Spec: memory/builds/aWireWarden/.
#
#   check-wiring.sh            # --check (default): report; exit 1 if any installed tool is unwired
#   check-wiring.sh --fix      # wire the safe cases (core.hooksPath when unset); exit reflects remainder
#   check-wiring.sh --session  # like --fix but ALWAYS exit 0 — the SessionStart hook mode
#   check-wiring.sh --resolve-fragment <f.fragment.json>   # print the fragment's hook path with
#                              # {kit}/{here} expanded — the value the arms below decide on, twinned
#                              # on settings-merge.py so the hook-destinations gate can assert parity.
#                              # A target's `adopter-owned` copy is NOT twinned: settings-merge.py is
#                              # its one reader, and this script calls it (`--resolve-hook`)
#
# WHERE A KIT FILE IS: every arm asks the install receipt (`.governance/install.json`, written by
# govkit) FIRST, through `resolve_receipt_path`, and only then probes gov's own `<prefix>/<kit>/` layout. A
# tree with no receipt — gov's own — resolves exactly as the probes always did.
#
# SEVERITY IS A VOCABULARY, and only `UNWIRED` gates. `ok` / `skip` / `fixed` / `note` do not. `note`
# is for a condition that is TRUE and worth printing but is not dormant wiring — today only the eol
# arm, whose subject is a working copy while the committed bytes are already correct. Reusing
# `UNWIRED` there would make the one word that means "this gates" stop meaning it, and a consumer
# that treats a non-zero exit as a refusal — `.unattended.conf` declares this script as its
# `WIRING_CHECK` — cannot tell the two apart from the status alone.
#
# Wiring the git hooks opts into running this repo's committed hooks (a git trust boundary). Auto-fix
# sets core.hooksPath ONLY when unset and NEVER overwrites an already-set value (e.g. a deliberate
# out-of-tree copy per WIRE-INTO-PROJECT.md §5). Agent-cap wiring is never auto-applied — it would mean
# rewriting settings.json, the file the SessionStart hook lives in. Each auto-fix that sets a value
# appends one `hookspath-set` or `merge-driver-set` line to the health log under the git common dir,
# which the orientation card counts; the format is the `health_log_sh` block's header below.
KIT_CHECK_WIRING_VERSION=1.25   # gov:kit check-wiring@1.25 — the deployer's read
set -u
# ---- S6: this file's own install prefix, DERIVED ------------------------------------------------
# TOOL-dRetiredFork-8. Six `tools/<kit>/` literals were spelled here, and `govkit apply` ships these
# bytes VERBATIM — so each one arrives unchanged in a target installed at another prefix and resolves
# to nothing there. That is the fork class this build exists to stop manufacturing. The walk is the
# unattended adopter's, copied rather than invented: a `.git` boundary walk from THIS file, because a
# junctioned worktree makes a `${DIR#$ROOT/}` strip a no-op and `git rev-parse --show-prefix` answers
# with a junction's TARGET.
_HERE="$(cd "$(dirname "$0")" && pwd)"
_KIT_ROOT=""; KIT_REL=""; _p="$_HERE"
while : ; do
  if [ -e "$_p/.git" ]; then _KIT_ROOT="$_p"; break; fi
  _parent="$(dirname "$_p")"
  [ "$_parent" = "$_p" ] && break
  KIT_REL="$(basename "$_p")${KIT_REL:+/$KIT_REL}"
  _p="$_parent"
done
# KIT_REL is this file's own directory relative to the repo root — `tools` here, whatever an adopter
# installs it under there. Empty is legal AND reachable: TOOL-cMendedVintage-3 moved the `.git` test
# ABOVE the append, so a ROOT install breaks on iteration one with no segment. It used to append
# first and test the PARENT, so `$_p` was never tested as the root: a root install walked PAST the
# repository to the filesystem root and handed every rung a prefix of directories ABOVE the tree —
# measured as `c/Temp/kw3/repo`, and the agent-cap arm skipped `not adopted` over a hook that was
# there. OUTSIDE a repo the walk still ends at the filesystem root with that same path in KIT_REL;
# that is not fixed here because `--check` exits at `skip — not a git repo` before any rung reads it.
KIT_REL=${KIT_REL:-}

# ---- S1: the settings file is RESOLVED, never spelled --------------------------------------------
# gov hardcoded the settings path at ten sites. adopter ic's live settings file sits OUTSIDE the
# worktree on every one of its nodes BY DESIGN, so that spelling resolves to nothing there and every
# arm below passed BY FINDING NO FILE — the worktree false-green recorded at ARCH-dBriskLanyard-1 S10.
#
# THE INVERSION FROM THE ADOPTER'S VERSION IS THE UNIT. Theirs returns an empty string when nothing
# resolves; this one REFUSES. An empty string is precisely what let every downstream arm pass by
# absence, so a path that resolves to nothing must be a refusal and not a non-match — the rule
# TOOL-aBoundedCeiling-7 records for `.githooks/pre-push`.
#
# THE DECOY HAZARD, carried from the source that records it: a printed remedy can CREATE a settings
# file at the worktree root, and a naive walk-up then finds the DECOY first and reports ok forever
# over a machine-global hook nothing wired. Reproduced live at that adopter. So the walk stops at the
# repo root rather than continuing to the filesystem root, and the override is checked FIRST: a
# deliberate out-of-tree layout is declared, never discovered by walking past the boundary.
GOV_SETTINGS_JSON=${GOV_SETTINGS_JSON:-}
_SETTINGS_CACHE=""
settings_json() {
  [ -n "$_SETTINGS_CACHE" ] && { printf '%s\n' "$_SETTINGS_CACHE"; return 0; }
  local cand="" _pref="$ROOT/.claude/settings.json"
  if [ -n "$GOV_SETTINGS_JSON" ]; then
    # DECLARED wins, and a declared path that is not there is a refusal rather than a fallthrough:
    # silently ignoring it would resolve a DIFFERENT file than the operator named, and every arm
    # would then be confidently wrong about the wrong file.
    if [ ! -f "$GOV_SETTINGS_JSON" ]; then
      echo "check-wiring: REFUSED — GOV_SETTINGS_JSON names $GOV_SETTINGS_JSON, which is not a file." >&2
      return 2
    fi
    cand="$GOV_SETTINGS_JSON"
  else
    # The PREFERENCE RUNG, bound once above so this file spells the path exactly ONCE — which is
    # what AC5 greps for, because byte-identity cannot catch a caller left on the literal here.
    [ -f "$_pref" ] && cand="$_pref"
  fi
  if [ -z "$cand" ]; then
    echo "check-wiring: REFUSED — no settings file resolved. Looked for GOV_SETTINGS_JSON, then" >&2
    echo "  $_pref (the preference rung). A path that resolves to nothing is" >&2
    echo "  a REFUSAL, not a non-match: every wiring arm below would otherwise pass by finding" >&2
    echo "  no file, which is the worktree false-green this resolver exists to remove." >&2
    return 2
  fi
  _SETTINGS_CACHE="$cand"
  printf '%s\n' "$cand"
}

# ---- S2: is the resolved file inside the repo? REPORT, never RED (ratified F1) --------------------
# A per-machine layout that keeps settings outside the worktree is deliberate at at least one
# adopter, so this reports. A project that wants it RED promotes it through TOOL-dRetiredFork-16's
# extension point rather than by changing this kit for everyone.
render_settings_path() { # the resolved path as a reader wants it: relative in-tree, absolute out
  local p; p=$(settings_json 2>/dev/null) || { printf '%s\n' "(unresolved)"; return 0; }
  case "$p" in
    "$ROOT"/*) printf '%s\n' "${p#"$ROOT"/}" ;;
    *)         printf '%s\n' "$p" ;;
  esac
}

check_settings_scope() {
  local sj; sj=$1
  case "$sj" in
    "$ROOT"/*) echo "ok       settings  — resolved $sj (inside the repo root)" ;;
    *)          echo "note     settings  — resolved $sj, which is OUTSIDE the repo root $ROOT. That is a"
                echo "note     settings    legitimate per-machine layout and is reported, not failed. It is also the"
                echo "note     settings    shape in which a hardcoded path silently graded nothing." ;;
  esac
}


# ---- the fragment reader, ONE for every arm ------------------------------------------------------
json_str() {  # value of a top-level "key": "..." in a small flat JSON file
  sed -n 's|.*"'"$2"'"[[:space:]]*:[[:space:]]*"\([^"]*\)".*|\1|p' "$1" | head -1
}
# `{kit}` and `{here}` ARE EXPANDED HERE, at the one place the value is read. A fragment ships
# verbatim, so it names its kit symbolically rather than spelling a prefix that is only correct in
# gov; leaving a token unexpanded makes an arm test for a file literally called `{kit}/...` and
# report a missing hook that is present. TOOL-dRetiredFork-14.
# Both resolve against THE FRAGMENT WE FOUND, never against this script's own KIT_REL. Those differ
# whenever the checker is run against a tree other than its own -- which is exactly what its
# self-test does -- and gov's prefix applied to a foreign layout names a file nobody has. `{kit}` is
# two dirnames up (a fragment sits at <kit>/<dir>/x.fragment.json), empty for a kit installed at
# the repo root; `{here}` is the fragment's OWN directory, which is what a `kind = "flat"` kit needs
# because its engine ships to `{prefix}/` and `{kit}` would name the prefix's PARENT there.
# TOOL-aReplayedCard-2: this used to be two inline copies, one per arm, and a third reader in the
# hook-destinations gate; it is one function now, printable through `--resolve-fragment`, so that
# gate reads the value the arms decide on rather than deriving a fourth beside them.
resolve_fragment_hook() { # fragment path -> its hook_path, tokens expanded; rc 1 + a reason on stderr when it declares none
  local frag="$1" hp here kitpfx
  # ONE spelling, repo-relative, whichever way the caller spelled the root: git's (`C:/…`) or the
  # shell's own after the cd (`/c/…` under MSYS). Both readers must print the same bytes.
  case "$frag" in
    "${ROOT:-/nonexistent}"/*) frag=${frag#"$ROOT"/} ;;
    "$PWD"/*)                  frag=${frag#"$PWD"/} ;;
  esac
  [ -f "$frag" ] || { echo "check-wiring: $frag is not a file" >&2; return 1; }
  hp=$(json_str "$frag" hook_path)
  [ -n "$hp" ] || { echo "check-wiring: $frag declares no hook_path" >&2; return 1; }
  here=$(dirname "$frag"); [ "$here" = . ] && here=""
  kitpfx=$(dirname "${here:-.}"); [ "$kitpfx" = . ] && kitpfx=""
  hp=$(printf '%s\n' "$hp" | sed -e "s|{kit}/|${kitpfx:+$kitpfx/}|g" -e "s|{here}/|${here:+$here/}|g")
  resolve_owned_hook "$hp"
}
# A HOOK THE TARGET KEEPS ELSEWHERE — TOOL-aRepatriatedFork-36. The fragment names gov's copy beside
# the kit; a target that runs its own copy at another path declares it `[[own]]`, and `adopt` records
# that as an `adopter-owned` receipt row carrying the SAME `source` as gov's engine row at the
# resolved path.
#
# ONE READER, AND IT IS NOT THIS FILE (the round-1 closing-diff fold). This used to be an awk parser
# beside settings-merge.py's `json.loads`, and the two split on every receipt that was not
# pretty-printed ASCII: a `\u` escape, a backslash, an embedded quote, compact JSON. The writer wired
# one path while this graded another, and the parity gate never saw it because gov keeps no receipt.
# So the question goes to settings-merge.py `--resolve-hook`, which also GRADES the owned path the
# way govkit grades an `[[own]]` path and refuses one it cannot trust; a refusal here is rc 1 with
# its reason on stderr, which the arms report as UNWIRED.
#
# THE PRE-FILTER IS EXACT, not a second reader: a JSON string can decode to `adopter-owned` only by
# spelling those letters or by carrying a `\u` escape, so a receipt holding neither has no owned row
# and needs no python. That keeps gov's own tree, and every adopter that owns no hook, as fast as it
# was on a host with no python at session start.
resolve_owned_hook() { # resolved hook path -> the adopter-owned path implementing its source, else itself
  if [ ! -f .governance/install.json ] || ! grep -q -e 'adopter-owned' -e '\\u' .governance/install.json; then
    printf '%s\n' "$1"; return 0
  fi
  if [ ! -f "$SMERGE" ]; then
    echo "check-wiring: the receipt may carry an adopter-owned row, and settings-merge.py, its one reader, is not installed at $SMERGE" >&2
    return 1
  fi
  local got why
  got=$("$PY" "$SMERGE" --resolve-hook "$1" 2>/dev/null) && { printf '%s\n' "$got"; return 0; }
  # Re-asked for the REASON only on the refusal path: stderr also carries import-time notes on a
  # clean run, so it cannot share the capture that yields the path.
  why=$("$PY" "$SMERGE" --resolve-hook "$1" 2>&1 >/dev/null | tail -1)
  echo "check-wiring: ${why:-settings-merge.py did not run under '$PY'} — the owned-hook join for $1 refused" >&2
  return 1
}

MODE=check; FRAG_ARG=""
case "${1:-}" in
  ""|--check) MODE=check ;;
  --fix)      MODE=fix ;;
  --session)  MODE=session ;;
  --resolve-fragment) MODE=resolve; FRAG_ARG=${2:-}
    [ -n "$FRAG_ARG" ] || { echo "usage: $(basename "$0") --resolve-fragment <fragment.json>" >&2; exit 2; } ;;
  *) echo "usage: $(basename "$0") [--check|--fix|--session|--resolve-fragment <fragment.json>]" >&2; exit 2 ;;
esac

# Not a git repo → nothing to wire; never an error (and never break session start).
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "skip     — not a git repo"; exit 0; }
cd "$ROOT" || { [ "$MODE" = session ] && exit 0; exit 0; }

DO_FIX=0; case "$MODE" in fix|session) DO_FIX=1 ;; esac
unwired=0

# Absolute path of an existing directory ("" if it does not resolve).
abspath() { ( cd "$1" 2>/dev/null && pwd ); }

# >>> health_log_sh — canonical copy: health-log.sh in gov's lib dir (byte-identical; gated)
# I3, THE HEALTH LOG (TOOL-aGraftedHelix-8): `<git-common-dir>/health.log`, one LF-terminated UTF-8
# line per automatic self-heal, four TAB-separated fields: utc (`YYYY-MM-DDTHH:MM:SS+00:00`), source
# and event (each `^[a-z][a-z0-9-]*$`), and a detail whose TAB, CR and LF are each folded to one space
# and which is cut to 240 characters. At HEALTH_LOG_CAP_LINES lines the appender first keeps the
# newest half, through a temp file and a rename, then appends. `derive_health_log <common-dir>` prints
# the path and spawns nothing; `resolve_health_log <repo-dir>` asks git once and prints it, or fails
# printing nothing; `add_health_event <log> <source> <event> <detail>` is the only writer. A refused
# token, an empty path or a failed write prints ONE `health: NOTE -` line on stderr and returns 0: it
# never fails its caller. WHAT IT DOES NOT DO: serialize concurrent writers (a trim racing an append
# can lose that line; ponytail: one rename, a lock file if a lost line is ever observed); validate
# what a detail means; or tell a repository with no writer installed from one where nothing healed.
HEALTH_LOG_CAP_LINES=500
derive_health_log() { printf '%s/health.log\n' "$1"; }
resolve_health_log() {
  local _hl_c
  _hl_c=$(git -C "$1" rev-parse --path-format=absolute --git-common-dir 2>/dev/null) || return 1
  _hl_c=${_hl_c%$'\r'}
  [ -n "$_hl_c" ] || return 1
  derive_health_log "$_hl_c"
}
add_health_event() {
  local _hl_log=${1:-} _hl_src=${2:-} _hl_ev=${3:-} _hl_d=${4:-} _hl_why="" _hl_n=0 _hl_t
  local _hl_a=abcdefghijklmnopqrstuvwxyz
  case "$_hl_src" in ''|[!$_hl_a]*|*[!$_hl_a'0123456789-']*) _hl_why="source '$_hl_src' is not a lowercase token" ;; esac
  case "$_hl_ev" in ''|[!$_hl_a]*|*[!$_hl_a'0123456789-']*) _hl_why="event '$_hl_ev' is not a lowercase token" ;; esac
  [ -n "$_hl_log" ] || _hl_why="no log path resolved"
  if [ -z "$_hl_why" ]; then
    _hl_d=${_hl_d//$'\t'/ }; _hl_d=${_hl_d//$'\r'/ }; _hl_d=${_hl_d//$'\n'/ }; _hl_d=${_hl_d:0:240}
    _hl_t=$(date -u +%Y-%m-%dT%H:%M:%S+00:00 2>/dev/null) || _hl_t=""
    [ -n "$_hl_t" ] || _hl_why="date printed no UTC stamp"
  fi
  if [ -z "$_hl_why" ] && [ -f "$_hl_log" ]; then
    _hl_n=$(wc -l < "$_hl_log" 2>/dev/null) || _hl_n=0
    _hl_n=${_hl_n//[!0-9]/}
    if [ "${_hl_n:-0}" -ge "$HEALTH_LOG_CAP_LINES" ]; then
      { tail -n $((HEALTH_LOG_CAP_LINES / 2)) "$_hl_log" > "$_hl_log.trim.$$" && mv -f "$_hl_log.trim.$$" "$_hl_log"; } 2>/dev/null \
        || { rm -f "$_hl_log.trim.$$" 2>/dev/null; _hl_why="the trim to the newest $((HEALTH_LOG_CAP_LINES / 2)) lines failed"; }
    fi
  fi
  if [ -z "$_hl_why" ]; then
    { printf '%s\t%s\t%s\t%s\n' "$_hl_t" "$_hl_src" "$_hl_ev" "$_hl_d" >> "$_hl_log"; } 2>/dev/null && return 0
    _hl_why="the append failed"
  fi
  printf 'health: NOTE - %s: %s; nothing written\n' "${_hl_log:-(no path)}" "$_hl_why" >&2
  return 0
}
# <<< health_log_sh

# First of the candidates that is a file ("" if none).
# STILL TWO RUNGS, and TOOL-dRetiredFork-8 measured why the obvious collapse is wrong. `KIT_REL` is
# derived from where THIS SCRIPT lives, not from the tree it grades, and those differ exactly when it
# matters: the self-test runs the real checker against root-install fixtures, and five recall arms
# plus the two-layout arm went RED the moment the bare rung was dropped. What the derivation buys is
# that the PREFIXED rung is no longer a literal `tools/` that ships verbatim and resolves to nothing
# at another prefix; the root-install rung stays, waived as it always was.
first_of() { for c in "$@"; do [ -f "$c" ] && { echo "$c"; return; }; done; }

# THE RECEIPT RUNG, FIRST in every list that finds a kit file (TOOL-aRepatriatedFork-19 S1). Every
# probe above is a guess about gov's own `<prefix>/<kit>/` layout, and an adopter that homed a kit at
# `scripts/recall/` or put the merge driver flat under `scripts/` defeated all of them: the arm printed
# `skip … not adopted` over a kit that was installed and wired. `govkit` already recorded where each
# file landed, so the checker asks that record before guessing.
#
# The arguments are the Python `resolve_kit_dir`'s own pair, the kit's HOME and a file in it (a
# tool-root file passes an empty home), joined and matched as a whole-segment SUFFIX of the row's
# `source`: the whole source would spell gov's tool root, which ships verbatim and means nothing here,
# and the last two segments are exactly that reader's join, which the self-test holds this one equal to.
# ONE awk pass, no python: this runs as a SessionStart hook on a host that may have none. The writer
# is `json.dumps(indent=2)`, so a row is `{` alone on a line, its keys one per line, `}` alone; the
# pair is collected per object, so key order does not matter. A row whose path is absolute or climbs
# with `..` is skipped, as the Python reader skips one that escapes the tree. Absent receipt, or no
# row: prints nothing, and every rung after it resolves exactly as it did before this one existed.
resolve_receipt_path() { # <kit-home> <file> -> the repo-relative path the receipt row records ("" if none)
  [ -f .governance/install.json ] || return 0
  awk -v want="${1:+$1/}$2" '
    function val(l) { sub(/^[^:]*:[[:space:]]*"/, "", l); sub(/".*$/, "", l); return l }
    /^[[:space:]]*\{[[:space:]]*$/          { p = ""; s = ""; next }
    /^[[:space:]]*"path"[[:space:]]*:/      { p = val($0); next }
    /^[[:space:]]*"source"[[:space:]]*:/    { s = val($0); next }
    /^[[:space:]]*\}[[:space:]]*,?[[:space:]]*$/ {
      if (p != "" && (s == want || (length(s) > length(want) && substr(s, length(s) - length(want)) == "/" want)) \
          && p !~ /^\// && p !~ /^[A-Za-z]:/ && p !~ /(^|\/)\.\.(\/|$)/) { print p; exit }
      p = ""; s = ""
    }' .governance/install.json 2>/dev/null
}
# S2: the skip a receipt CONTRADICTS says so. A row naming a file that is not there is the receipt
# leg's red, not wiring's, so the arm still skips — but "not adopted" would be false, and it names
# the row and the missing path instead. Prints nothing when the receipt has no row or the file exists.
derive_receipt_miss() { # <kit-home> <file> -> a skip reason, or ""
  local p; p=$(resolve_receipt_path "$1" "$2")
  [ -n "$p" ] && [ ! -f "$p" ] && printf '%s' "the .governance/install.json row for ${1:+$1/}$2 names $p, which is absent (the receipt leg owns a missing installed file)"
}

# THE wired signal, for every arm: the hook's marker substring present in the RESOLVED settings file —
# INSIDE A GROUP WHOSE MATCHER IS THE ONE THE FRAGMENT DECLARES. settings-merge.py documents that
# same substring as the deployer's is-it-wired test (its module docstring), so the marker half is the
# one predicate stated once — not a second spelling of it. Reading it here also removes the
# "settings-merge.py absent, cannot verify" skip, which was a false all-clear in every adopter (the
# tool is copied in per WIRE §3c step 4 / §5, so an arm that REQUIRED it to answer reported
# `skip … exit 0` on the state the runbook calls the one bad state).
#
# THE MATCHER HALF IS NEW, AND IT IS THE WHOLE POINT. A file-wide grep for `agent-cap.js` answers
# "is the hook mentioned"; the question is "does it fire on the events it must". A group still
# matching only `Workflow` — the state where a direct `Agent` spawn meets no rule at all — contains
# the string and reported `ok`, so the arm could not tell a correctly-widened wiring from a stale one
# and never could have. Same class as the merge arm's "declared vs wired" gap.
#
# Read WITHOUT a JSON parser on purpose: this runs as a SessionStart hook and must answer on a host
# with no python. Flattened, each `{"matcher": …}` group starts a chunk and its own hooks array ends
# at the first `]`, so the marker and the matcher that governs it are one contiguous span.
# EVERY matcher whose group carries the marker, one per line — not just the first. A settings.json
# may legitimately hold several groups, and `settings-merge.py` ADDS the widened group rather than
# migrating a stale one, so "the first group mentioning the hook" is the wrong question to ask.
matchers_of() { # marker [hook-basename] -> the matcher of each group carrying BOTH (empty if absent)
  # A REFUSAL PROPAGATES. The retired form tested the settings path with `|| return 0`, so a
  # missing file was indistinguishable from a present file with no matching group — which is the
  # whole defect. Returning 2 keeps them apart even though `wired` treats both as not-wired.
  local _sj; _sj=$(settings_json 2>/dev/null) || return 2
  # `-e` BEFORE THE MARKER. The card markers are `--write` and `--replay`, dash-leading by design
  # (they are the verb's own arguments), and a bare `grep -F "$1"` reads one as an OPTION: grep
  # exits 2, the pipeline yields nothing, and every card check prints UNWIRED over a correctly
  # merged file forever. TOOL-aReplayedCard-2.
  # THE SECOND KEY, `$2`, is the hook's BASENAME, which the stripped view keeps intact: a bare-flag
  # marker (`--write`) alone took an adopter's own `--write-log` hook for the card writer, in this
  # reader and in the merger's (the aReplayedCard closing review, F5). Absent, it defaults to the
  # marker itself, so a one-key caller filters twice on one key and reads exactly as before.
  tr -d ' \t\r\n' < "$_sj" \
    | sed 's/{"matcher":/\n{"matcher":/g' \
    | sed 's/\].*$//' \
    | grep -F -e "$1" \
    | grep -F -e "${2:-$1}" \
    | sed -n 's/^{"matcher":"\([^"]*\)".*/\1/p'
}
# THE THIRD KEY IS THE HOOK'S RESOLVED PATH, as the command names it (the round-1 fold, I1). The
# basename could not tell two copies of one hook apart: with gov's copy landed beside the kit and
# settings.json still running an out-of-kit copy, the recall arm printed `ok` for the copy that runs
# nothing — and kept printing it after the running copy was deleted. The key is the path behind
# `${CLAUDE_PROJECT_DIR}/` up to the closing escaped quote, the one spelling settings-merge.py
# renders, so a path that is a suffix of another cannot match it. Absent, the marker alone joins.
wired() { # marker · the matcher the fragment declares · [the hook's resolved path]
  [ -n "$2" ] && matchers_of "$1" "${3:+{CLAUDE_PROJECT_DIR\}/$3\\\"}" | grep -qxF "$2"
}

# THE LAUNCHER, resolved by RUNNING each candidate — the block below is the canonical resolver,
# inline because the shared copy ships to no adopter. It named a remedy string only, until the
# round-1 fold made settings-merge.py the one reader of an adopter-owned hook: `resolve_owned_hook`
# above RUNS it now, so a name that cannot execute refuses every owned hook, never a stale hint.
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
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  "$1" -c "$(cat <<'RKD'
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
)"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
# THE PROBE RUNG, through the sibling-kit resolver (TOOL-aRepatriatedFork-46). It used to be a kit's
# name typed after this checker's own prefix, which is the class the carried-prefix ban counts. The
# resolver probes the same two places, `<this dir>/<home>` and one level up, after its own receipt
# read. It needs python, and this runs as a SessionStart hook on a host that may have none. With no
# launcher the SAME two places are probed in bash (closing review round 1 M6): costing the rung
# printed `not adopted` over a hook that was present, naming a place nothing had looked at. The awk
# receipt rung above it runs either way.
resolve_kit_file() { # <kit-home> <file> -> <repo-relative kit dir>/<file>, or nothing
  local py d
  if ! py=$(resolve_python 2>/dev/null); then
    echo "note     resolver  — no usable python, so the probe rung beside this checker ran in bash for $1/$2" >&2
    for d in "${KIT_REL:+$KIT_REL/}$1" "$(dirname -- "${KIT_REL:-.}")/$1"; do
      d=${d#./}
      [ -f "$_KIT_ROOT/$d/$2" ] && { printf '%s/%s\n' "$d" "$2"; return 0; }
    done
    return 0
  fi
  d=$(resolve_kit_dir "$py" "$1" "$2" "$_KIT_ROOT/$KIT_REL" 2>/dev/null) || return 0
  printf '%s/%s\n' "$d" "$2"
}
PY=$(resolve_python 2>/dev/null) || PY=python3   # gov:literal-python — a NAME a remedy prints when no launcher runs; the owned-hook call then refuses by name

# The merger every remedy names, resolved ONCE across both install layouts. Four arms used to
# resolve it each; one spelling is one fewer carried literal per arm that names it.
# DERIVED, and NEVER EMPTY. This file sits directly under the tool root, so its own KIT_REL IS that
# root. The remedies below used to fall back to the merger under a literal `tools/` prefix, which names
# nothing at any install prefix but gov's own — an operator at `scripts/gov/` was handed a command
# that cannot start, and TOOL-cMendedVintage-3 made a root install REACH that line for the first
# time. With the fallback derived, every tail collapses to the bare variable and the literal is
# deleted rather than repathed, which is what removes the class instead of moving it.
# Resolved HERE, above the print verb, since the round-1 fold: `resolve_owned_hook` calls it.
SMERGE_DEFAULT="${KIT_REL:+$KIT_REL/}settings-merge.py"
SMERGE=$(first_of "$(resolve_receipt_path "" settings-merge.py)" "$SMERGE_DEFAULT" settings-merge.py); SMERGE=${SMERGE:-$SMERGE_DEFAULT}

# The print verb answers and leaves BEFORE the settings resolver and the arms run: it is a reader
# of one fragment, and its output is compared byte-for-byte against settings-merge.py's.
if [ "$MODE" = resolve ]; then
  resolve_fragment_hook "$FRAG_ARG"; exit $?
fi

# TOOL-aWeldedTribunal-7 — WHICH HOOK WILL ACTUALLY RUN. The shared `core.hooksPath` applies unless a worktree's config.worktree sets its own,
# and the value in effect decides which hook files run: an ABSOLUTE value runs the hooks of the
# checkout it names, the relative `.githooks` this script writes runs each worktree's own. Measured at
# `TOOL-dUnstalledConvoy-26`'s landing: the primary tree sat on adopter ic's recall contrib branch, so the
# push ran that branch's `pre-push` — no gate-env sourcing, no predicate 8, and the boundary's own
# coverage check simply absent. Nothing wrong shipped, because a separate full bar had verified the
# pushed tree; the BOUNDARY was not the one that shipped.
#
# WHAT THIS DOES NOT CHECK, stated because a structural check reads as a semantic one to everybody
# who did not write it: it reports a divergence, it does not PREVENT one, and a push made after the
# report still runs the other checkout's hook. Closing that needs a refusal inside the hook itself,
# which is a separate decision about what the push boundary REFUSES.
#
# IT IS A `note`, NOT AN `UNWIRED`, and that is the load-bearing half. `unwired` is exactly what
# this script's final line turns into its exit code, and `.unattended.conf` makes `--check` an unattended
# run's precondition — so an UNWIRED line here would refuse every unattended run whenever a sibling
# checkout moved to a branch that touched `.githooks/`. A primary tree parked on a feature branch is
# a NORMAL state of this layout, and a gate that reds on a structural condition is a gate that gets
# bypassed. The severity carries the whole fork resolution.
#
# WRITTEN OVER A LIST, so a third hook is one row rather than a third copy of the comparison.
GOV_WIRING_HOOKS="commit-msg pre-commit pre-push pre-rebase"
check_hook_blobs() { # $1 = resolved hooks dir, $2 = the configured value as written
  local dir="$1" shown="$2" hook resolved tracked otherbranch
  for hook in $GOV_WIRING_HOOKS; do
    # A hook this tree does not TRACK is a SKIP, never a comparison and never a finding. Check H's
    # entry guard is tracked `.githooks/pre-commit` alone, so an adopter that owns its own pre-commit
    # and ships no pre-push must not acquire a permanent report it has no action to clear.
    if ! git ls-files --error-unmatch ".githooks/$hook" >/dev/null 2>&1; then
      echo "skip     hooks     — .githooks/$hook is not tracked here, so there is nothing to compare"
      continue
    fi
    # `ls-tree`, not `rev-parse HEAD:<path>`: a POSIX-emulation shell on Windows can mangle the
    # `<rev>:.dotpath` spelling and report ABSENT for a file that is present.
    tracked=$(git ls-tree HEAD -- ".githooks/$hook" 2>/dev/null | awk '{print $3}')
    resolved=$([ -f "$dir/$hook" ] && git hash-object "$dir/$hook" 2>/dev/null)
    # LIVENESS: an unreadable side is never printed as `ok`. "Could not compare" and "compared and
    # agreed" are different facts, and only one of them is evidence.
    if [ -z "$tracked" ] || [ -z "$resolved" ]; then
      echo "note     hooks     — $hook: UNKNOWN, could not read both sides (tracked='${tracked:-?}' resolved='${resolved:-?}')"
      continue
    fi
    [ "$tracked" = "$resolved" ] && continue
    otherbranch=$(git -C "$(dirname "$dir")" rev-parse --abbrev-ref HEAD 2>/dev/null || true)
    echo "note     hooks     — $hook DIVERGES: the hook that will run is $resolved from $shown"
    echo "note     hooks       (checkout on '${otherbranch:-unknown}'), this tree tracks $tracked."
    echo "note     hooks       the core.hooksPath value in effect names another checkout, which supplies the hook."
  done
}

# --- Check H: git hooks (core.hooksPath) ---------------------------------------------------------
check_hooks() {
  if ! { [ -f .githooks/pre-commit ] && git ls-files --error-unmatch .githooks/pre-commit >/dev/null 2>&1; }; then
    echo "skip     hooks     — no tracked .githooks/pre-commit"
    return
  fi
  local cur curdir
  cur=$(git config core.hooksPath 2>/dev/null || true)
  if [ -n "$cur" ]; then
    curdir=$(abspath "$cur")
    if [ -n "$curdir" ] && [ -f "$curdir/pre-commit" ]; then
      echo "ok       hooks     — core.hooksPath -> $cur"
      check_hook_blobs "$curdir" "$cur"
    else
      echo "UNWIRED  hooks     — core.hooksPath='$cur' resolves to no pre-commit; NOT overwriting (deliberate?). Fix: git config core.hooksPath .githooks"
      unwired=$((unwired+1))
    fi
    return
  fi
  # unset — the fresh-clone case. The self-heal is logged (I3, TOOL-aGraftedHelix-8) only on the
  # branch that ran `git config`, so a wired tree's next SessionStart writes nothing.
  if [ "$DO_FIX" = 1 ]; then
    if git config core.hooksPath .githooks; then
      echo "FIXED    hooks     — set core.hooksPath -> .githooks"
      CW_HEALTH_LOG=${CW_HEALTH_LOG:-$(resolve_health_log "$ROOT")}
      add_health_event "$CW_HEALTH_LOG" check-wiring hookspath-set "core.hooksPath -> .githooks · mode $MODE"
    fi
  else
    echo "UNWIRED  hooks     — core.hooksPath unset; .githooks gates (incl. branch guard) dormant. Fix: git config core.hooksPath .githooks"
    unwired=$((unwired+1))
  fi
}

# S2 runs ONCE, before any arm, so the resolved path and its scope are on the record BEFORE any
# verdict that depends on them. A scope arm nobody calls is the same silent nothing this unit
# removes one level down.
#
# IT DOES NOT EXIT. The refusal belongs to the arms that NEED the file, not to the run: a repo with
# no settings file is a legal state — a fresh clone before anything is wired — and refusing there
# says nothing about the hooks, skills and eol wiring the run was asked to grade. Measured: an eager
# exit killed 45 of 76 self-test arms, not one of which was about settings. What the refusal buys is
# that no arm can read "no file" as "nothing to check": `matchers_of` propagates it, `wired` is then
# false, and each settings arm reports UNWIRED with the reason instead of passing by absence.
_sj_err=$(mktemp)
if _sj_for_scope=$(settings_json 2>"$_sj_err"); then
  check_settings_scope "$_sj_for_scope"
else
  # THE RESOLVER'S OWN WORDS, not a generic substitute. "You named a path that is not there"
  # and "there is no settings file anywhere" are different operator problems with different
  # fixes, and discarding stderr here made them the same sentence.
  sed 's/^/note     settings  /' "$_sj_err"
  echo "note     settings  — every settings-dependent arm below reports UNWIRED rather than"
  echo "note     settings    passing by absence."
fi
rm -f "$_sj_err"

# --- Check A: agent-cap PreToolUse hook in the resolved settings file -----------------------------
# Advisory: no mode mutates settings.json (the SessionStart hook must not rewrite its own file).
#
# THE MATCHER IS A LIST OF EXACT STRINGS separated by `|`, not a regular expression: the hook fires
# for `Workflow` (where it reads the script) and for `Agent` (where a direct spawn would otherwise
# meet no rule at all). A group carrying only `Workflow` is the stale state, and it is named by the
# value found rather than reported as a generic miss — an operator who is told "unwired" about a
# hook that is plainly in the file will conclude the checker is broken.
AGENTCAP_MATCHER='Workflow|Agent'
check_agentcap() {
  local smerge found shipped; smerge=$SMERGE
  # THE ADOPTION TEST PROBES FOR THE HOOK, IT DOES NOT NAME ONE COPY. This used to key on
  # `.claude/hooks/agent-cap.js` and said so on purpose: the hook path "is not declared anywhere this
  # script can read". That reason stopped being true at TOOL-dRetiredFork-14, which moved `hook_path`
  # into the fragment exactly as the recall arm below already had it.
  #
  # Keying on the withdrawn copy was not merely stale, it was DANGEROUS: the moment the duplicate was
  # dropped this arm printed `skip — not adopted` about a hook that is adopted and wired, over the
  # most important guard in the repo. A skip that reads as a pass is the shape this repo keeps
  # finding, and here it was one commit away from hiding an unwired security hook.
  # The adopter rung is spelled through KIT_REL rather than as a bare `hooks/...`. Both forms probe
  # the same place; only the bare one is a root-install spelling the prefix gate bans, and its
  # waiver registry is shrink-only, so buying a new row here would spend a budget meant for the
  # probes that already have one.
  # `${KIT_REL:+...}` LIKE EVERY SIBLING ARM, and this one was the only probe in the file
  # without it. Unguarded, a ROOT install (KIT_REL empty) built the absolute path
  # rooted at `/` with the hook's kit-relative path, matched nothing, and printed `skip -- not adopted` over a hook that
  # was present and correctly wired. A silent skip over the concurrency hook, which is the
  # one arm in this file where a false skip has a security shape. Found by the closing review
  # of TOOL-dRetiredFork-17, reproduced on a scratch root-layout tree.
  #
  # The guard buys no waiver row: with KIT_REL empty the rung IS the bare spelling, so the
  # form the prefix gate bans never appears in the source.
  shipped=$(first_of "$(resolve_receipt_path hooks agent-cap.js)" "$(resolve_kit_file hooks agent-cap.js)" .claude/hooks/agent-cap.js)
  if [ -z "$shipped" ]; then
    # THE MESSAGE NAMES WHAT THE PROBE ACTUALLY TRIED. It used to advertise three locations
    # for a two-rung probe, one of them a hardcoded install-prefix literal in prose that
    # ships verbatim to an adopter at another prefix -- the class this build exists to drain,
    # inside the arm whose own comment is about skips that read as passes.
    local miss; miss=$(derive_receipt_miss hooks agent-cap.js)
    echo "skip     agent-cap — ${miss:-not adopted (no agent-cap.js at ${KIT_REL:+$KIT_REL/}hooks/ or .claude/hooks/)}"
    return
  fi
  # S4: a LEGACY second copy is REPORTED, never redded. An adopter mid-migration has both, and their
  # wired command may still name either; blocking them would make the safe ordering -- move the
  # command first, withdraw second -- impossible to perform.
  if [ "$shipped" != ".claude/hooks/agent-cap.js" ] && [ -f .claude/hooks/agent-cap.js ]; then
    echo "note     agent-cap — a legacy copy remains at .claude/hooks/agent-cap.js while the shipped copy is $shipped; withdraw it once your wired command names the shipped one"
  fi
  if wired "agent-cap.js" "$AGENTCAP_MATCHER"; then
    # TOOL-dTieredTribunal-14 S7 - a WIRED command may never carry --only. The flag narrows the hook
    # to one rule, so `--only=join` in settings.json turns the three cap rules off with no diff and a
    # hook that still looks wired. That is the class of the AGENT_CAP environment knob this file
    # deleted, whose own header records that it survived two releases by appearing to work.
    # matchers_of() discards the command, so the command text is read here rather than there.
    # M8 closing review, BLOCKER: the first spelling of this guard could never fire. Every class was
    # bounded with [^"]*, and the command settings.json actually ships is
    #   "command": "node \"${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js\""
    # so no class could cross the ESCAPED quote and the match was always empty. The only declared
    # control on a bypass this same build introduced was itself a check that could not fail. Scoped
    # to the LINE now, which no quoting defeats, and the test file observes the failing case.
    if grep 'agent-cap\.js' "$(settings_json)" 2>/dev/null | grep -q -- '--only'; then
      echo "UNWIRED  agent-cap — the wired command carries --only, which runs ONE rule and silently disables the rest. Remove the flag from $(render_settings_path)."
      unwired=$((unwired+1))
      return
    fi
    # WIRED IS NOT ENOUGH -- it must name the copy that actually ships. A command pointing at a
    # withdrawn path satisfies the marker test and loads nothing, which is precisely the silent
    # unwiring this unit's migration ordering exists to prevent.
    if ! grep -q "$shipped" "$(settings_json)" 2>/dev/null; then
      echo "UNWIRED  agent-cap — wired, but the command does not name the shipped copy $shipped. Repath with: $PY $smerge"
      unwired=$((unwired+1))
      return
    fi
    echo "ok       agent-cap — PreToolUse hook wired in $(render_settings_path) at $shipped (matcher '$AGENTCAP_MATCHER')"
    return
  fi
  found=$(matchers_of "agent-cap.js" | paste -sd, - 2>/dev/null || matchers_of "agent-cap.js" | tr '\n' ',')
  if [ -n "$found" ]; then
    echo "UNWIRED  agent-cap — the hook is wired under matcher '$found', not '$AGENTCAP_MATCHER'; it never fires for a direct Agent spawn, which is the modality the arity rule was blind to. Fix: $PY $smerge"
  else
    echo "UNWIRED  agent-cap — agent-cap.js present but hook not in settings.json. Fix: $PY $smerge"
  fi
  unwired=$((unwired+1))
}

# --- Check S: scratch-guard PreToolUse hook -------------------------------------------------------
# Reads marker, matcher and hook path from the SHIPPED fragment, the way the recall arm does and the
# agent-cap arm above does not. That is deliberate: this arm should assert nothing the kit does not
# itself declare, so widening the matcher is a one-line fragment edit rather than a two-file edit
# with a drift window between them.
#
# Unlike recall, this hook is NOT an opt-in — it ships wired with the hooks kit — so an absent hook
# file means "kit not adopted here" and a present-but-unwired one is a real UNWIRED, exactly as for
# agent-cap. A guard that is silent when unwired looks identical to a guard that is passing.
# Advisory like every other arm: no mode rewrites settings.json.
check_scratch_guard() {
  local frag smerge marker hookjs smatcher found
  # TWO RUNGS, the receipt and this checker's own prefix. A third, bare root spelling used to follow
  # them, a guess at a layout the derivation had already missed. A miss is now the skip below, which
  # names both rungs (TOOL-aRepatriatedFork-24 S8), and the same holds for the recall and merge arms.
  frag=$(first_of "$(resolve_receipt_path hooks scratch-guard.fragment.json)" "$(resolve_kit_file hooks scratch-guard.fragment.json)")
  if [ -z "$frag" ]; then
    local miss; miss=$(derive_receipt_miss hooks scratch-guard.fragment.json)
    echo "skip     scratch   — ${miss:-hooks kit does not ship scratch-guard.fragment.json here (no install-receipt row, and none at ${KIT_REL:+$KIT_REL/}hooks/)}"
    return
  fi
  smerge=$SMERGE
  marker=$(json_str "$frag" marker)
  # A REFUSED owned-hook join is UNWIRED naming its reason, never a blank path read as a bad fragment.
  if ! hookjs=$(resolve_fragment_hook "$frag" 2>&1); then
    echo "UNWIRED  scratch   — ${hookjs##*check-wiring: }"
    unwired=$((unwired+1))
    return
  fi
  smatcher=$(json_str "$frag" matcher)
  if [ -z "$marker" ] || [ -z "$hookjs" ] || [ -z "$smatcher" ]; then
    echo "UNWIRED  scratch   — $frag declares no marker/matcher/hook_path; settings-merge.py refuses it too. Fix: restore the shipped fragment"
    unwired=$((unwired+1))
    return
  fi
  if [ ! -f "$hookjs" ]; then
    if wired "$marker" "$smatcher"; then
      echo "UNWIRED  scratch   — settings.json dispatches the guard but $hookjs is missing; every shell call runs node against nothing. Fix: cp ${frag%/*}/scratch-guard.js $hookjs"
      unwired=$((unwired+1))
    else
      echo "skip     scratch   — not adopted ($hookjs absent)"
    fi
    return
  fi
  if wired "$marker" "$smatcher" "$hookjs"; then
    echo "ok       scratch   — PreToolUse guard wired in $(render_settings_path) (matcher '$smatcher')"
    return
  fi
  if wired "$marker" "$smatcher"; then
    echo "UNWIRED  scratch   — settings.json dispatches a guard under '$smatcher', but not the resolved copy $hookjs. Fix: $PY $smerge --fragment $frag"
    unwired=$((unwired+1))
    return
  fi
  # Name the value FOUND rather than reporting a generic miss: an operator told "unwired" about a
  # hook plainly present in the file concludes the checker is broken. Same reasoning as agent-cap.
  found=$(matchers_of "$marker" | paste -sd, - 2>/dev/null || matchers_of "$marker" | tr '\n' ',')
  if [ -n "$found" ]; then
    echo "UNWIRED  scratch   — the guard is wired under matcher '$found', not '$smatcher'; it never fires for the shells the fragment declares. Fix: $PY $smerge --fragment $frag"
  else
    echo "UNWIRED  scratch   — $hookjs present but the guard is not in settings.json. Fix: $PY $smerge --fragment $frag"
  fi
  unwired=$((unwired+1))
}

# --- Check R: recall-opened PostToolUse hook (memory-recall kit — an OPT-IN) ----------------------
# FIVE states, not two. `adopt-memory-recall.sh` copies the hook only under `--with-hook`, so an
# absent hook file with nothing in settings.json is a TRUE signal ("opt-in not taken"), never
# UNWIRED. Mirroring the agent-cap arm literally would print a permanent false alarm in the repo
# that runs THIS script as its own SessionStart hook, which is the fastest way to train every node
# to ignore the wiring verifier. Both halves — the marker and the script path — are read from the
# fragment, so this arm asserts nothing the shipped kit does not itself declare.
# Advisory like every other arm: no mode rewrites settings.json.
check_recall_opened() {
  local frag smerge marker hookjs rmatcher
  # Resolved by path because the kit is COPIED: <root>/memory-recall/ in an adopter,
  # <root>/$KIT_REL/memory-recall/ in this repo.
  frag=$(first_of "$(resolve_receipt_path memory-recall recall-opened.fragment.json)" "$(resolve_kit_file memory-recall recall-opened.fragment.json)")
  if [ -z "$frag" ]; then
    local miss; miss=$(derive_receipt_miss memory-recall recall-opened.fragment.json)
    echo "skip     recall    — ${miss:-memory-recall kit not adopted (no recall-opened.fragment.json: no install-receipt row, and none at ${KIT_REL:+$KIT_REL/}memory-recall/)}"
    return
  fi
  smerge=$SMERGE
  marker=$(json_str "$frag" marker)
  # A REFUSED owned-hook join is UNWIRED naming its reason, never a blank path read as a bad fragment.
  if ! hookjs=$(resolve_fragment_hook "$frag" 2>&1); then
    echo "UNWIRED  recall    — ${hookjs##*check-wiring: }"
    unwired=$((unwired+1))
    return
  fi
  # The MATCHER comes from the fragment too, so this arm still asserts nothing the shipped kit does
  # not itself declare — the same rule the marker already followed, applied to the half that decides
  # whether the hook fires at all.
  rmatcher=$(json_str "$frag" matcher)
  if [ -z "$marker" ] || [ -z "$hookjs" ] || [ -z "$rmatcher" ]; then
    echo "UNWIRED  recall    — $frag declares no marker/matcher/hook_path; settings-merge.py refuses it too. Fix: restore the shipped fragment"
    unwired=$((unwired+1))
    return
  fi
  if [ ! -f "$hookjs" ]; then
    if wired "$marker" "$rmatcher"; then
      echo "UNWIRED  recall    — settings.json dispatches the hook but $hookjs is missing; every Read runs node against nothing. Fix: bash $(dirname "$frag")/adopt-memory-recall.sh --scaffold --with-hook"
      unwired=$((unwired+1))
    else
      echo "skip     recall    — recall-opened hook opt-in not taken (adopt-memory-recall.sh --with-hook)"
    fi
    return
  fi
  # THE PATH IS GRADED, not the marker alone (the round-1 fold, I1): gov's copy beside the kit and a
  # target's own copy elsewhere share the marker AND the basename, so only the path in the command
  # says which one runs. An entry running another copy is named, with both ways to reconcile it.
  if wired "$marker" "$rmatcher" "$hookjs"; then
    echo "ok       recall    — recall-opened PostToolUse hook wired in $(render_settings_path) at $hookjs"
  elif wired "$marker" "$rmatcher"; then
    echo "UNWIRED  recall    — settings.json runs a recall-opened hook, but not the resolved copy $hookjs; the copy it runs is graded by nothing. Fix: declare that copy [[own]] in .governance/deploy.toml and run govkit adopt --re-adopt --write, or rewire with $PY $smerge --fragment $frag"
    unwired=$((unwired+1))
  else
    echo "UNWIRED  recall    — $hookjs present but hook not in settings.json. Fix: $PY $smerge --fragment $frag"
    unwired=$((unwired+1))
  fi
}

# --- Check C: the orientation card's two SessionStart entries (kickoff-manifest kit) --------------
# TOOL-aReplayedCard-2. Two fragments beside the kickoff engine, each one verb of `manifest-check.sh
# --card`: the WRITER at `startup|clear`, the REPLAY at `resume|compact`. Their matchers are the
# whole point — a SessionStart entry with no matcher runs on every compaction, and a matcher that
# is misspelled or narrowed never fires at all while looking exactly like one that is wired. So
# this arm asserts the LITERAL matcher each fragment declares, the way the scratch arm does, and
# names the value it found instead. Both fragments must be present, and both wired, for `ok`: a
# writer with no replay is a card every compaction drops, and a replay with no writer replays a
# card nothing wrote.
#
# The fragments sit at the kit's HOME in this repo and at `{prefix}/` in an adopter — the kit is
# `kind = "flat"`, so the engine and its two fragments ship side by side — and their `{here}` token
# resolves to whichever of those the fragment was found at. Advisory like every other arm.
#
# WHAT THIS DOES NOT CHECK: any other SessionStart entry. The `check-wiring.sh --session` entry and
# the process-monitor session entry ship fragments too, and NO arm here reads their matchers — the
# merger re-matches them on apply, and a hand edit or a later narrowing to `startup` passes green
# (the aReplayedCard closing review, F12). The two card fragments are graded; the count is two.
check_card() {
  local name frag marker hooksh cmatcher found miss nfound=0 nok=0 line=""
  for name in orientation-card orientation-replay; do
    frag=$(first_of "$(resolve_receipt_path session-kickoff "$name.fragment.json")" "skills/session-kickoff/$name.fragment.json" "${KIT_REL:+$KIT_REL/}$name.fragment.json" "$name.fragment.json")
    if [ -z "$frag" ]; then
      miss=$(derive_receipt_miss session-kickoff "$name.fragment.json")
      echo "skip     card      — ${miss:-kickoff-manifest kit does not ship $name.fragment.json here}"
      return
    fi
    nfound=$((nfound+1))
    marker=$(json_str "$frag" marker)
    if ! hooksh=$(resolve_fragment_hook "$frag" 2>&1); then
      echo "UNWIRED  card      — ${hooksh##*check-wiring: }"
      unwired=$((unwired+1))
      return
    fi
    cmatcher=$(json_str "$frag" matcher)
    if [ -z "$marker" ] || [ -z "$hooksh" ] || [ -z "$cmatcher" ]; then
      echo "UNWIRED  card      — $frag declares no marker/matcher/hook_path; settings-merge.py refuses it too. Fix: restore the shipped fragment"
      unwired=$((unwired+1))
      return
    fi
    if [ ! -f "$hooksh" ]; then
      if matchers_of "$marker" "$(basename "$hooksh")" | grep -qxF "$cmatcher"; then
        echo "UNWIRED  card      — settings.json dispatches $marker but $hooksh is missing; every session start runs bash against nothing. Fix: re-copy the kickoff-manifest kit beside $frag"
        unwired=$((unwired+1))
      else
        echo "skip     card      — not adopted ($hooksh absent)"
      fi
      return
    fi
    if wired "$marker" "$cmatcher" "$hooksh"; then
      nok=$((nok+1)); line="$line${line:+, }$marker at '$cmatcher'"
      continue
    fi
    if matchers_of "$marker" "$(basename "$hooksh")" | grep -qxF "$cmatcher"; then
      echo "UNWIRED  card      — the $name entry ($marker) is wired under '$cmatcher', but not at the resolved $hooksh. Fix: $PY $SMERGE --fragment $frag"
      unwired=$((unwired+1))
      continue
    fi
    # Name the value FOUND rather than a generic miss, and the matcher EXPECTED beside it: the
    # replay wired under `resume` alone is the exact state this arm exists to catch — it looks
    # wired, and the card is gone after the first compaction.
    found=$(matchers_of "$marker" "$(basename "$hooksh")" | paste -sd, - 2>/dev/null || matchers_of "$marker" "$(basename "$hooksh")" | tr '\n' ',')
    if [ -n "$found" ]; then
      echo "UNWIRED  card      — the $name entry ($marker) is wired under matcher '$found', not '$cmatcher'; it never fires for the events the fragment declares. Fix: $PY $SMERGE --fragment $frag"
    else
      echo "UNWIRED  card      — $hooksh present but the $name entry ($marker) is not in settings.json. Fix: $PY $SMERGE --fragment $frag"
    fi
    unwired=$((unwired+1))
  done
  [ "$nok" = "$nfound" ] && [ "$nfound" = 2 ] \
    && echo "ok       card      — SessionStart card entries wired in $(render_settings_path) ($line)"
}


# --- Check E: line endings on the RENDERED wiring files -------------------------------------------
# A `git worktree` checkout can land CRLF on a path .gitattributes pins `eol=lf`, and `git status`
# stays CLEAN because the index normalises on commit. The symptom is a gate that diffs a rendered
# file against a fresh render and reports EVERY line as drift on a file the session never touched.
#
# THE BOUND IS DERIVED, and it is deliberately not "every eol=lf path": that attribute covers 46
# files here, which is far wider than anything this arm should rewrite. The population is the tracked
# files under .claude/ that carry the pin — check-wiring.sh's OWN domain, intersected with the pin,
# both read from the tree rather than listed here. Measured: exactly the two rendered Skills, which
# are also exactly the files an adopt script byte-compares.
#
# The repair REWRITES THE BYTES, because a `git checkout --` remedy is state-dependent and this is
# not. Measured: `git diff` reports NO content change on such a file (the clean filter normalises)
# while `git status --porcelain` DOES list it — the two disagree, so a checkout-based repair restores
# the file or silently no-ops depending on which one git consults. A previous build hit the no-op and
# needed `rm` first. Rewriting the bytes is correct in both states.
check_eol() {
  local pop f bad=""
  # THE POPULATION IS THE RENDERED SKILL MARKDOWN, not "every eol=lf path under .claude/". Measured
  # in a scratch repo with a `* text=auto eol=lf` .gitattributes — an ordinary thing to write — the
  # wider selector pulled in the settings file and a PNG, and `--fix` rewrote both: three CR
  # bytes stripped out of the middle of the image, md5 changed, reported as "fixed". A repair whose
  # bound depends on how an adopter spelled their attributes has no bound.
  #
  # NUL-byte guard as well, because a bound stated in a glob is still a claim: a binary that lands
  # under .claude/skills/ with a .md name is skipped rather than rewritten.
  # PER-PATH, not `xargs`: xargs word-splits on whitespace, so `.claude/skills/my skill/SKILL.md`
  # reached `git check-attr` as two nonexistent paths, the population came back empty, and the arm
  # printed a green `skip`. Reproduced — a folder name with a space is an ordinary thing to type. The
  # population is two files; a fork each is not a cost worth a silent collapse.
  # A SECOND NAMED GLOB, not a wider one (TOOL-aRepatriatedFork-19 S3): tracked `.claude/workflows/*.js`
  # carrying the pin. The review-harness kit pins those scripts because CR bytes made a shipped
  # harness unlaunchable, and nothing on the wiring side looked at them. It is named beside the Skill
  # glob, so the "every eol=lf path under .claude/" selector the paragraph above forbids stays unwritten.
  pop=$(git ls-files .claude/skills/ .claude/workflows/ 2>/dev/null \
        | grep -E '^\.claude/skills/.*\.md$|^\.claude/workflows/[^/]*\.js$' | while IFS= read -r _p; do
          [ -n "$_p" ] || continue
          git check-attr eol -- "$_p" 2>/dev/null | sed -n 's/^\(.*\): eol: lf$/\1/p'
        done)
  if [ -z "$pop" ]; then
    echo "skip     eol       — no tracked .claude/skills/**.md or .claude/workflows/*.js carries an eol=lf pin"
    return
  fi
  # `while read`, not `for f in $pop`: a Skill directory with a space in its name — ordinary on a
  # machine where someone typed the folder name — word-split into fragments that matched no file, and
  # the arm reported "ok" over a population of zero.
  while IFS= read -r f; do
    [ -n "$f" ] && [ -f "$f" ] || continue
    # NUL test WITHOUT a NUL in the pattern. Bash cannot hold a NUL byte in a string, so `$'\000'`
    # is the EMPTY string and `grep -q ''` matches EVERY file — the first cut skipped the whole
    # population and then reported "ok", a guard that could not fire protecting a check that could
    # not fire. Compare byte counts instead.
    if [ "$(LC_ALL=C tr -d '\000' < "$f" | wc -c)" != "$(wc -c < "$f")" ]; then
      echo "skip     eol       — $f holds NUL bytes; not text, not repaired"
      continue
    fi
    if LC_ALL=C grep -qU $'\r' "$f" 2>/dev/null; then bad="$bad
$f"; fi
  done <<EOF
$pop
EOF
  bad=$(printf '%s\n' "$bad" | grep . || true)
  if [ -z "$bad" ]; then
    echo "ok       eol       — every eol=lf-pinned .claude/ file is LF in the worktree"
    return
  fi
  # `--session` REPORTS; only `--fix` rewrites. The unit's own ratified fork said exactly this and the
  # first cut implemented DO_FIX=1 for both — so a SessionStart hook rewrote file bytes unattended,
  # which is a far bigger act than setting an unset git config, the only thing --session was ever
  # allowed to do.
  if [ "$DO_FIX" = 1 ] && [ "$MODE" != session ]; then
    while IFS= read -r f; do
      [ -n "$f" ] || continue
      # Rewrite in place, then verify: a repair that reports success without checking is the class of
      # bug this whole arm exists to catch one level up.
      LC_ALL=C tr -d '\r' < "$f" > "$f.eoltmp" && mv -f "$f.eoltmp" "$f"
      if LC_ALL=C grep -qU $'\r' "$f" 2>/dev/null; then
        echo "UNWIRED  eol       — $f still holds CRLF after the repair. Fix by hand: tr -d '\\r'"
        unwired=$((unwired+1))
      else
        echo "fixed    eol       — $f rewritten to LF (the index already normalised, so git status was clean)"
      fi
    done <<EOF
$bad
EOF
    return
  fi
  # `note`, and NO `unwired++`. This arm's subject is a WORKING COPY: the committed bytes are LF on
  # every node, so nothing in the repository is wrong and nothing is dormant. It gated once because
  # the harm was real — one adopter byte-compared without normalising, and reported every line of an
  # untouched file as drift. That adopter now normalises, so the exit status funded nothing while a
  # consumer that reads it as a refusal (`WIRING_CHECK` in .unattended.conf) refused every run in a
  # worktree carrying the artifact. The REPORT is what has value here; the status was the accident.
  # If a renderer is ever found emitting CRLF into a committed file, this is the line to reopen.
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    echo "note     eol       — $f holds CRLF despite its eol=lf pin; the committed bytes are LF, so this is a working-copy artifact and does not gate. Fix: bash ${KIT_REL:+$KIT_REL/}$(basename "$0") --fix"
  done <<EOF
$bad
EOF
}

# --- Check M: the row-keyed merge driver (memory-tree kit) ----------------------------------------
# `.gitattributes` declares `merge=rows` on the authored indexes, but a merge DRIVER is per-node
# config: git falls back to its built-in three-way text merge, with a warning, on any node that never
# ran this. That fallback is the pre-change behaviour, so the attribute and the config can land in one
# commit — and this arm is what turns "declared" into "wired" on each node.
#
# Setting it under `--session` as well as `--fix` mirrors check_hooks, which already sets a git config
# in both. The eol arm's session exemption is deliberately NOT copied: that arm rewrites file BYTES,
# and this one sets a repo-local config, which is the class of act `--session` exists for.
#
# The arm RUNS the command it is about to bless — see the smoke block below. It runs the command this
# script BUILDS, never the arbitrary string a node may have put in `merge.rows.driver`: a foreign
# value is reported and refused a few lines further down without being executed, so the only command
# that ever reaches a subprocess here is the one shipped in this repo. Whenever the arm can print
# `ok`, the built command and the configured one are the same string, which is the case that had to
# be covered. (aMendedLedger U5)
check_merge_rows() {
  local drv launcher want cur declared
  # Resolved by path because the kit is COPIED: <root>/memory-tree/ in an adopter,
  # <root>/$KIT_REL/memory-tree/ here. The remedy string is BUILT from the two resolved paths rather
  # than hand-kept, so it cannot drift from the layout it is describing.
  drv=$(first_of "$(resolve_receipt_path memory-tree merge-rows.py)" "$(resolve_kit_file memory-tree merge-rows.py)")
  if [ -z "$drv" ]; then
    local miss; miss=$(derive_receipt_miss memory-tree merge-rows.py)
    echo "skip     merge     — ${miss:-memory-tree merge driver not adopted (no merge-rows.py: no install-receipt row, and none at ${KIT_REL:+$KIT_REL/}memory-tree/)}"
    return
  fi
  # The KIT-INTERNAL launcher first. It travels with the kit, so it is the only one an adopter is
  # guaranteed to have; gov's lib-dir `pyrun.sh` is gov-internal and ships nothing, and a wiring that
  # names it in an adopting repo execs a command that cannot start. A driver that never starts never
  # writes %A, so git reports CONFLICT and leaves the path holding OURS-ONLY content with no markers.
  launcher=$(first_of "$(dirname "$drv")/merge-rows.sh" "$(resolve_kit_file lib pyrun.sh)")
  if [ -z "$launcher" ]; then
    echo "UNWIRED  merge     — $drv is present but no launcher is: expected $(dirname "$drv")/merge-rows.sh beside it. git would exec a command that cannot start, and a driver that never starts leaves OURS-only content with no conflict markers. Fix: re-copy the memory-tree kit"
    unwired=$((unwired+1))
    return
  fi
  # pyrun.sh takes the driver as an argument; the kit launcher already knows its own sibling.
  case "$launcher" in
    */merge-rows.sh) want="bash $launcher %O %A %B %P" ;;
    *)               want="bash $launcher $drv %O %A %B %P" ;;
  esac
  # ONE call over every tracked path, and it reads what GIT judges rather than grepping
  # `.gitattributes` — attributes come from several files, the same rule check_eol follows. Looping
  # per file would be ~500 process spawns inside a SessionStart hook; `--stdin` is one process
  # regardless of tree size.
  declared=$(git ls-files 2>/dev/null | git check-attr --stdin merge 2>/dev/null | sed -n 's/: merge: rows$//p')
  if [ -z "$declared" ]; then
    echo "skip     merge     — no tracked path declares merge=rows"
    return
  fi
  # RUN THE COMMAND, do not pattern-match its parts. "Wired" is "the command git will exec actually
  # merges", and the three tests above — driver exists, launcher exists, config string matches — are all
  # path-and-string. They cannot see the two runtime dependencies the driver reaches for at merge
  # time: the resolve-python helper, which `pyrun.sh` sources, and the sibling memory-recall kit that
  # owns the anchor grammar. Both were MEASURED printing `ok  merge  — merge.rows.driver wired`
  # here while the very next merge left `memory/DECISIONS.md` holding OURS-only content with zero
  # conflict markers and status `UU` — the silent take-ours the driver's own fail-closed wrapper
  # exists to prevent, arriving one level up where that wrapper never gets to run.
  #
  # A no-op THREE-WAY rather than the cheaper usage/arity call. `merge-rows.py` defers its grammar
  # import into `merge()`, so an argument-less invocation exits 2 with its usage text even when the
  # memory-recall kit is missing outright — it would prove the interpreter starts and nothing else.
  # Three scratch inputs that merge CLEANLY exercise the whole chain in one python start: launcher
  # resolution, the driver's own syntax, the `.memory-tree.conf` walk-up, the deferred grammar
  # import, the KEYED path, and the `%A` write. That is one process per session-start, which is what
  # a verifier that verifies costs.
  #
  # AND THE FIXTURE CARRIES ANCHORED ROWS, one APPEND COLLISION PER DECLARED FAMILY. The first cut
  # used three unkeyable lines (`x` / `a\nx` / `x\nb`): `split_regions` found no anchor, so the whole
  # file was preamble and the run was a plain `git merge-file` — `rows()`, `merge()`, `lead()`, the
  # splice and both postconditions were never entered. MEASURED: one token of drift in
  # `.memory-tree.conf` FAMILIES (`tooling:TOOL` -> `tooling:TOOLS`) makes the driver key ZERO rows,
  # every governed-index append-collision then conflicts forever, the driver is completely inert —
  # and the arm still printed `ok  merge  — merge.rows.driver wired`.
  #
  # An append collision is the ONE shape that discriminates: git's built-in three-way CONFLICTS on it
  # (both sides add a different line after the same predecessor), so a clean rc 0 is only reachable
  # through the keyed path. Per family, because a fixture built on one family goes green on drift in
  # any other. The ids use the FLAT era (`\d{3}`), which is in the grammar's `ERAS` unconditionally
  # and needs no node tag; the `- <id> | <text>` form is the shipped dash-anchor shape in ASCII.
  local smoke rc_smoke=0 fams f n miss=""
  # Sourced in a SUBSHELL so a project conf cannot redefine this script's own variables. Absent conf
  # -> a placeholder family: the driver then cannot resolve a grammar either, raises, and this arm
  # reports UNWIRED with a real reason rather than being special-cased into silence here.
  fams=$( . ./.memory-tree.conf >/dev/null 2>&1; for f in ${FAMILIES:-}; do printf '%s ' "${f##*:}"; done )
  [ -n "$fams" ] || fams="ROWS"
  smoke=$(mktemp -d 2>/dev/null) || smoke=""
  # "Could not verify" is NOT a clean bill, and this file already made that call once: the recall arm
  # above deleted its `settings-merge.py absent, cannot verify` skip precisely because it reported
  # exit 0 on the one state the runbook calls bad. Same rule here — an unrunnable check reports
  # UNWIRED, never `ok`.
  if [ -z "$smoke" ]; then
    echo "UNWIRED  merge     — cannot verify the driver: 'mktemp -d' failed, so the no-op three-way never ran and this arm has nothing to report. Fix: make a temp dir writable (TMPDIR), then re-run"
    unwired=$((unwired+1))
    return
  fi
  : > "$smoke/o"; : > "$smoke/a"; : > "$smoke/b"
  for f in $fams; do
    printf -- '- %s-001 | base\n'                     "$f"      >> "$smoke/o"
    printf -- '- %s-001 | base\n- %s-002 | ours\n'    "$f" "$f" >> "$smoke/a"
    printf -- '- %s-001 | base\n- %s-003 | theirs\n'  "$f" "$f" >> "$smoke/b"
  done
  # Run the SAME argv the wiring declares, minus git's placeholders, so the smoke proves the
  # CONFIGURED command starts rather than a second spelling of it that might start when it does
  # not. The two launcher shapes take different argv, so rebuilding the command here by hand was
  # a standing way for the probe to disagree with the thing it blesses.
  # shellcheck disable=SC2086
  set -- ${want%% %O %A %B %P}
  "$@" "$smoke/o" "$smoke/a" "$smoke/b" merge-rows-smoke \
    >/dev/null 2>"$smoke/err" || rc_smoke=$?
  # rc alone is not enough: assert every row of all three inputs is in %A exactly once. A driver that
  # exits 0 without touching %A is the same silent take-ours by another route, and one that keys only
  # SOME families resolves the rest by line merge — which is the state this arm exists to name.
  for f in $fams; do
    for n in 001 002 003; do
      [ "$(grep -c -- "^- $f-$n |" "$smoke/a" 2>/dev/null)" = 1 ] || miss="$miss $f-$n"
    done
  done
  if [ "$rc_smoke" != 0 ] || [ -n "$miss" ]; then
    echo "UNWIRED  merge     — the configured driver cannot merge: '$launcher' exited $rc_smoke on a per-family append collision, missing or duplicated:${miss:- none} ($(head -1 "$smoke/err" 2>/dev/null | tr -d '\r')). git prints CONFLICT and leaves the path holding OURS-only content with NO markers. Fix: restore the launcher beside $drv and the sibling memory-recall kit, check .memory-tree.conf FAMILIES, then re-run"
    unwired=$((unwired+1))
    rm -rf "$smoke"
    return
  fi
  # ...AND THE SMOKE'S OWN ROWS ACTUALLY KEYED, which is a NEW obligation and not a tidy-up. Under
  # the retired driver a dead anchor grammar made the append collision conflict, so the arm above
  # caught it: inert was LOUD. Under the two-plane driver a row the grammar cannot key is still a
  # ROW — it falls to a hashed token, reconciliation rule 3 resolves the collision anyway, and all
  # three ids land exactly once. MEASURED with `anchor_at` stubbed to return None on this same
  # 4-family / 12-row fixture: rc 0, 12 of 12 present, and `git merge-file` on the identical three
  # blobs returns rc 1. So the driver is BETTER than git while being completely inert on the ids it
  # exists to key, and every check above is green over it. The audit line's keyed/hashed split is
  # the only surviving signal, and this is where it is read.
  local kd hs
  kd=$(sed -n 's/.*written (\([0-9]*\) keyed.*/\1/p' "$smoke/err" | tail -1)
  hs=$(sed -n 's/.*keyed, \([0-9]*\) hashed.*/\1/p' "$smoke/err" | tail -1)
  if [ -z "$hs" ]; then
    echo "UNWIRED  merge     — the driver merged the smoke but printed no keyed/hashed audit line, so there is no way to tell whether it KEYED the rows or merely copied them; a driver whose anchor grammar is dead resolves this fixture too. Fix: the installed $drv predates the audit line — re-copy the kit, then re-run"
    unwired=$((unwired+1))
    rm -rf "$smoke"
    return
  fi
  if [ "$hs" != 0 ]; then
    echo "UNWIRED  merge     — the driver runs and resolves, but it keyed only $kd of the smoke's $((kd + hs)) rows and HASHED $hs of them: the anchor grammar it imports does not recognise ids it declares (families:${fams:+ }${fams% }). Rows that only hash still merge, so nothing fails loudly, but the id-level no-duplicate guarantee is off on the files this driver is wired to. Fix: check .memory-tree.conf FAMILIES against the ids the indexes use and that the memory-recall kit beside $drv ships the grammar, then re-run"
    unwired=$((unwired+1))
    rm -rf "$smoke"
    return
  fi
  rm -rf "$smoke"
  # ...AND THE DECLARED FAMILIES ARE THE ONES THE INDEXES ACTUALLY USE. The fixture above is built
  # FROM the conf, so it stays self-consistent under a family RENAME: one token of drift
  # (`tooling:TOOL` -> `tooling:TOOLS`) leaves the smoke green while every real `- TOOL-…` row stops
  # keying, every governed append-collision conflicts forever, and the driver is inert on the only
  # files it is wired to. MEASURED: the arm printed `ok  merge  — merge.rows.driver wired`. So the
  # declared indexes are asked directly — harvest the family prefix each ROW LEADS with, and require
  # every harvested prefix to be declared. A prefix nothing declares is drift by definition; the
  # reverse (a declared family with no rows yet) is the ordinary empty-section state and is not.
  local seen undeclared=""
  seen=$(printf '%s\n' "$declared" | grep . | while IFS= read -r p; do
           [ -f "$p" ] && sed -n 's/^[[:space:]]*[-*][[:space:]]\{1,\}[`*]*\([A-Z][A-Z0-9]\{1,\}\)-[A-Za-z0-9].*/\1/p' "$p"
         done | LC_ALL=C sort -u)
  for f in $seen; do
    case " $fams " in *" $f "*) ;; *) undeclared="$undeclared $f" ;; esac
  done
  if [ -n "$undeclared" ]; then
    echo "UNWIRED  merge     — the driver runs, but .memory-tree.conf FAMILIES does not declare$undeclared, which rows in the merge=rows indexes LEAD with; those rows key as unstructured content, so every append-collision on them conflicts forever and the driver is inert on the files it is wired to. Fix: add the family to FAMILIES in .memory-tree.conf (declared:${fams:+ }${fams% })"
    unwired=$((unwired+1))
    return
  fi
  cur=$(git config merge.rows.driver 2>/dev/null || true)
  if [ -z "$cur" ]; then
    if [ "$DO_FIX" = 1 ]; then
      if git config merge.rows.driver "$want"; then
        echo "FIXED    merge     — set merge.rows.driver"
        CW_HEALTH_LOG=${CW_HEALTH_LOG:-$(resolve_health_log "$ROOT")}
        add_health_event "$CW_HEALTH_LOG" check-wiring merge-driver-set "merge.rows.driver · mode $MODE"
      fi
    else
      echo "UNWIRED  merge     — paths declare merge=rows but merge.rows.driver is unset; git falls back to a line merge that can duplicate a row. Fix: git config merge.rows.driver '$want'"
      unwired=$((unwired+1))
    fi
    return
  fi
  if [ "$cur" = "$want" ]; then
    echo "ok       merge     — merge.rows.driver wired"
  else
    echo "UNWIRED  merge     — merge.rows.driver='$cur', not '$want'; NOT overwriting (deliberate?)"
    unwired=$((unwired+1))
  fi
}

# --- Check S: the machine-global /session-kickoff install matches the tracked engine ---------------
# CONTENT, not link-ness. The obvious check — is the install a junction or a symlink — cannot be
# written portably here: under MSYS an NTFS junction is not reported by `test -L`, it presents as an
# ordinary directory, so a link test calls every correctly-junctioned Windows node a copy. And
# link-ness is only a proxy: a junction pointing at a STALE second checkout passes a link test and
# fails the question this check exists to answer. Comparing bytes answers it directly.
#
# NOTHING here writes. The install lives outside every repository, and the deployer build's review
# record establishes that the deployer's own security rule forbids an out-of-tree write — so `--fix`
# prints the command and stops, and this arm never increments on the strength of being fixable.
# (That record is paraphrased rather than cited by id. A non-terminal spec id named from product
# source counts against the drift bar's shrink-only pin, and this file is inside that population —
# the same trap the kickoff manifest records having hit once already.)
check_skill_install() {
  local inst="${HOME}/.claude/skills/session-kickoff"
  local rel=skills/session-kickoff
  local fix f a b bad=""

  if [ ! -d "$inst" ]; then
    echo "skip     skill     — /session-kickoff not installed on this machine (WIRE-INTO-PROJECT.md §1)"
    return
  fi
  # The repo under inspection is usually an ADOPTER, which has the machine-global install and no
  # tracked kit source — the skill is installed once per machine, never copied per project. Without
  # this state the check reports UNWIRED at every SessionStart, forever, in every adopting repo, with
  # a Fix line naming a command the operator has already run. `check_recall_opened`'s own comment
  # records where that road ends: a permanent false alarm trains every node to ignore the verifier.
  if ! git ls-files --error-unmatch -- "$rel/SKILL.md" >/dev/null 2>&1; then
    echo "skip     skill     — the kickoff kit is not adopted in this repo; the install is machine-global"
    return
  fi

  # THE TARGET IS THE PRIMARY WORKTREE, NEVER `$ROOT`. `$ROOT` is the CURRENT worktree, and this arm
  # is content-keyed against the tracked engine — so it fires precisely on a branch that edits the
  # engine, which by this project's convention is a linked worktree under `.claude/worktrees/`. That
  # directory is disposable. An operator who followed a remedy naming it, landed the branch and ran
  # `git worktree remove` would have a dangling junction and NO `/session-kickoff` on the whole
  # machine — and this check returns early when the install directory is absent, so the verifier that
  # caused the breakage could not report it. `git worktree list` puts the main worktree first.
  local primary
  primary=$(git worktree list 2>/dev/null | head -1 | sed 's/[[:space:]].*//')
  [ -n "$primary" ] || primary="$ROOT"
  case "$(uname -s 2>/dev/null || echo unknown)" in
    MINGW*|MSYS*|CYGWIN*)
      # PowerShell wants backslashes throughout; the path arrives forward-slashed under MSYS, so the
      # whole target is converted rather than concatenated across two separator conventions.
      fix="New-Item -ItemType Junction -Path \"\$env:USERPROFILE\\.claude\\skills\\session-kickoff\" -Target \"$(printf '%s\n' "$primary/$rel" | tr '/' '\\')\"" ;;
    *)
      fix="ln -sfn $primary/$rel ~/.claude/skills/session-kickoff" ;;
  esac

  for f in SKILL.md MANIFEST-TEMPLATE.md manifest-check.sh; do
    if [ ! -f "$inst/$f" ]; then
      echo "UNWIRED  skill     — the installed engine is missing $f, so /session-kickoff is running an incomplete kit. Fix: $fix"
      unwired=$((unwired+1))
      return
    fi
    # BOTH halves. `skills/session-kickoff/SKILL.md` carries an eol=lf pin and this fleet runs
    # core.autocrlf=true, so a Windows checkout can hold CRLF on either side. Normalise both through
    # the same filter or the comparison reports every line as drift on a file nobody touched.
    a=$(LC_ALL=C tr -d '\r' < "$inst/$f" | cksum)
    b=$(LC_ALL=C tr -d '\r' < "$ROOT/$rel/$f" | cksum)
    [ "$a" = "$b" ] || bad="$bad $f"
  done

  # A LINKED WORKTREE WHOSE OWN BRANCH EDITS THE ENGINE IS NOT A WIRING FAULT. The install follows the
  # primary checkout, and the remedy above names that checkout, so when the install matches it byte
  # for byte the only difference is this branch's unlanded edit, which reaches the install when the
  # branch lands. Reporting it UNWIRED made `--check` fail in exactly that worktree, and the unattended
  # driver's preflight delegates to `--check`, so a build editing the engine could never re-preflight
  # (aGraftedHelix, 2026-10-05). The install drifting from the primary as well still reds below.
  # WHAT THIS DOES NOT CHECK: that the primary checkout is on the default branch, or current.
  if [ -n "$bad" ] && ! [ "$primary" -ef "$ROOT" ] && [ -d "$primary/$rel" ]; then
    local pbad=""
    for f in SKILL.md MANIFEST-TEMPLATE.md manifest-check.sh; do
      a=$(LC_ALL=C tr -d '\r' < "$inst/$f" | cksum)
      b=$(LC_ALL=C tr -d '\r' < "$primary/$rel/$f" 2>/dev/null | cksum)
      [ "$a" = "$b" ] || pbad="$pbad $f"
    done
    if [ -z "$pbad" ]; then
      echo "note     skill     — this worktree's branch edits the engine in:${bad}; the install matches the primary checkout's, so the edit reaches it when the branch lands"
      return
    fi
  fi
  if [ -n "$bad" ]; then
    echo "UNWIRED  skill     — the installed engine differs from tracked in:${bad}; this session is running a different engine than this repo ships. Fix: $fix"
    unwired=$((unwired+1))
    return
  fi
  echo "ok       skill     — the installed /session-kickoff engine matches tracked"
}

# --- Check T: local branches that still owe a backlog relocation (TOOL-dDerivedDocket-13) ---------
# REPORT-ONLY, ALWAYS. `note`, never `UNWIRED`: `unwired` is what this script's last line turns into
# its exit code and `.unattended.conf` makes `--check` an unattended run's precondition, so redding
# here would refuse every run on this node for a branch somebody else owns. A straggler is a normal
# state of a transition, and a gate that reds on a normal state is a gate that gets bypassed.
#
# WHY EVERY SESSION TREE AND NOT THE PRIMARY ONE. The ref set is repository-wide, and this project's
# sessions routinely open in a linked worktree — a primary-tree-only step would reach almost none of
# them. The inventory is the relocation engine's `--stragglers --local`, which is its one narrowing
# walk over `refs/heads` and nothing else.
#
# `hooks own-tree` IS THE LOAD-BEARING HALF. A straggler checked out in a linked worktree whose
# effective `core.hooksPath` resolves INSIDE that worktree runs its own pre-flip hook files, so the
# commit, rebase and push refusals never fire there at all. This note, the drift signal and the
# merge bar's transition audit are the only layers that reach it, and a reader who does not know
# that will read the absence of a refusal as an absence of a problem.
#
# EVERY PATH IS DERIVED. This file ships verbatim, so the kit directory and the engine's basename
# are VALUES joined to `KIT_REL` at run time rather than a spelled path that resolves to nothing at
# another prefix.
#
# WHAT THIS DOES NOT CHECK: it does not decide whether a row change is accounted — it prints the
# engine's count and names the refs. It reads `refs/heads` only, so a straggler that exists on
# another node and not here is invisible to it; the drift-audit signal walks the remote-tracking
# refs for exactly that reason.
check_backlog_stragglers() {
  local conf mode kit eng path py out rc refs ref names="" wt wtabs hp eff mark
  conf=$(first_of .memory-tree.conf)
  if [ -z "$conf" ]; then
    echo "skip     straggler — no .memory-tree.conf here, so this repo declares no backlog mode"
    return
  fi
  # READ IN THE FILE'S OWN LANGUAGE, as check M above reads FAMILIES: the conf is a shell file the
  # hygiene gate SOURCES, so a subshell source is the kit's reader and not a second one. The pipeline
  # this replaces kept `BACKLOG_MODE=builds   # note` as `builds   # note` and read
  # `export BACKLOG_MODE=builds` as nothing, and skipped a flipped tree as not flipped
  # (closing diff review round 1, F6). A trailing CR is dropped as the kit's python parser drops it;
  # the conf is pinned LF, so that only matters in a working copy that smudged it anyway.
  mode=$( . "./$conf" >/dev/null 2>&1; printf '%s' "${BACKLOG_MODE:-}" )
  mode=${mode%$'\r'}
  if [ "$mode" != builds ]; then
    echo "skip     straggler — BACKLOG_MODE is not 'builds' here, so no branch can be a straggler yet"
    return
  fi
  kit=memory-tree; eng=migrate_backlog.py
  # THE RECEIPT RUNG FIRST, as in every other arm that finds a kit file (TOOL-aRepatriatedFork-19):
  # the two probes after it are guesses about gov's layout, and an adopter that homed the kit where
  # neither spells it read `not installed` over an installed kit (merge-2 skeptic F4).
  path=$(first_of "$(resolve_receipt_path "$kit" "$eng")" "${KIT_REL:+$KIT_REL/}$kit/$eng" "$kit/$eng")
  if [ -z "$path" ]; then
    local miss; miss=$(derive_receipt_miss "$kit" "$eng")
    # The default reason sits in its own assignment: an apostrophe inside `${miss:-…}` within double
    # quotes opens a quote bash never closes.
    [ -n "$miss" ] || miss="the memory-tree kit's $eng is not installed here, so no inventory ran"
    echo "skip     straggler — $miss"
    return
  fi
  if ! command -v resolve_python >/dev/null 2>&1 || ! py=$(resolve_python 2>/dev/null); then
    echo "note     straggler — no usable python launcher resolved, so the straggler inventory did NOT run and this line is not an all-clear"
    return
  fi
  # BOUNDED. The walk is one process per ref pair plus a delta per candidate, and this runs at
  # SessionStart: a repository with hundreds of refs must cost a bounded wait, not an unbounded one.
  # A bound that fires is announced, because a silent timeout is a clean-looking zero.
  if command -v timeout >/dev/null 2>&1; then
    out=$(timeout 60 "$py" "$path" --stragglers --local --tsv 2>/dev/null); rc=$?
  else
    out=$("$py" "$path" --stragglers --local --tsv 2>/dev/null); rc=$?
  fi
  if [ "$rc" != 0 ]; then
    echo "note     straggler — the straggler inventory exited $rc and reported nothing usable, so this line is not an all-clear"
    return
  fi
  refs=$(printf '%s\n' "$out" | awk -F'\t' '$1=="straggler"{print $2}')
  for ref in $refs; do
    mark=""
    wt=$(git worktree list --porcelain 2>/dev/null |
         awk -v want="$ref" '/^worktree /{p=substr($0,10)} /^branch /{if (substr($0,8)==want) print p}')
    if [ -n "$wt" ]; then
      wtabs=$(abspath "$wt")
      hp=$(git -C "$wt" config --get core.hooksPath 2>/dev/null || true)
      eff=""
      if [ -n "$hp" ]; then
        case "$hp" in
          /*|[A-Za-z]:[\\/]*) eff=$(abspath "$hp") ;;
          *)                  eff=$(abspath "$wt/$hp") ;;
        esac
      fi
      if [ -z "$eff" ] || [ -z "$wtabs" ]; then
        mark=" (hooks own-tree)"
      else
        case "$eff" in "$wtabs"|"$wtabs"/*) mark=" (hooks own-tree)" ;; esac
      fi
    fi
    names="$names $ref$mark ·"
  done
  if [ -n "$names" ]; then
    # THE MARK IS NOT IN THIS PROSE, deliberately. A sentence that always carries the marker's own
    # words makes any arm grepping for it pass over a run where nothing was marked — the same
    # could-not-fail shape the charter's §7 names, one level up from the code.
    echo "note     straggler —${names% ·} still edit the authored backlog shards and owe a relocation before they merge; a marked branch runs its own pre-flip hook files, so only this note, the drift signal and the merge bar reach it. Detail: $py $path --stragglers"
  else
    echo "ok       straggler — no local branch still owes a backlog relocation"
  fi
}

check_hooks
check_agentcap
check_scratch_guard
check_recall_opened
check_card
check_merge_rows
check_eol
check_skill_install
check_backlog_stragglers

[ "$MODE" = session ] && exit 0
[ "$unwired" = 0 ] && exit 0 || exit 1
