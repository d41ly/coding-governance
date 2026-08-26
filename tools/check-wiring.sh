#!/usr/bin/env bash
# check-wiring.sh — detect coding-governance tools installed-but-unwired in THIS repo, and
# (with --fix/--session) wire the zero-risk ones. Spec: memory/builds/aWireWarden/.
#
#   check-wiring.sh            # --check (default): report; exit 1 if any installed tool is unwired
#   check-wiring.sh --fix      # wire the safe cases (core.hooksPath when unset); exit reflects remainder
#   check-wiring.sh --session  # like --fix but ALWAYS exit 0 — the SessionStart hook mode
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
# rewriting settings.json, the file the SessionStart hook lives in.
KIT_CHECK_WIRING_VERSION=1.1
set -u

MODE=check
case "${1:-}" in
  ""|--check) MODE=check ;;
  --fix)      MODE=fix ;;
  --session)  MODE=session ;;
  *) echo "usage: $(basename "$0") [--check|--fix|--session]" >&2; exit 2 ;;
esac

# Not a git repo → nothing to wire; never an error (and never break session start).
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "skip     — not a git repo"; exit 0; }
cd "$ROOT" || { [ "$MODE" = session ] && exit 0; exit 0; }

DO_FIX=0; case "$MODE" in fix|session) DO_FIX=1 ;; esac
unwired=0

# Absolute path of an existing directory ("" if it does not resolve).
abspath() { ( cd "$1" 2>/dev/null && pwd ); }

# First of the candidates that is a file ("" if none).
first_of() { for c in "$@"; do [ -f "$c" ] && { echo "$c"; return; }; done; }

# THE wired signal, for every arm: the hook's marker substring present in .claude/settings.json —
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
matchers_of() { # marker -> the matcher of each group carrying it (empty if the marker is absent)
  [ -f .claude/settings.json ] || return 0
  tr -d ' \t\r\n' < .claude/settings.json \
    | sed 's/{"matcher":/\n{"matcher":/g' \
    | sed 's/\].*$//' \
    | grep -F "$1" \
    | sed -n 's/^{"matcher":"\([^"]*\)".*/\1/p'
}
wired() { # marker · the matcher the fragment declares
  [ -n "$2" ] && matchers_of "$1" | grep -qxF "$2"
}

# The launcher named in a remedy string. It is PRINTED rather than run, which is exactly why it
# must be resolved by running: a remedy line naming a launcher that cannot execute is a wrong
# answer that looks like a right one. A host with no usable python still gets a remedy — the
# fallback name is honest about being a guess.
# Resolved relative to THIS SCRIPT, never to the repo being checked. `$ROOT` is the tree under
# inspection, which in the self-test is a throwaway repo with no kits in it at all — sourcing from
# there printed "No such file or directory" and then "resolve_python: command not found" on every
# scratch run, and the arms downstream went green anyway.
_CW_HERE="$(cd "$(dirname "$0")" && pwd)"
if [ -f "$_CW_HERE/lib/resolve-python.sh" ]; then
  . "$_CW_HERE/lib/resolve-python.sh"
  PY=$(resolve_python) || PY=python3   # gov:literal-python — a NAME for a remedy string; nothing here is executed
else
  PY=python3   # gov:literal-python — printed in a remedy string, never executed; the resolver is not installed beside this script
fi

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
    else
      echo "UNWIRED  hooks     — core.hooksPath='$cur' resolves to no pre-commit; NOT overwriting (deliberate?). Fix: git config core.hooksPath .githooks"
      unwired=$((unwired+1))
    fi
    return
  fi
  # unset — the fresh-clone case
  if [ "$DO_FIX" = 1 ]; then
    git config core.hooksPath .githooks && echo "FIXED    hooks     — set core.hooksPath -> .githooks"
  else
    echo "UNWIRED  hooks     — core.hooksPath unset; .githooks gates (incl. branch guard) dormant. Fix: git config core.hooksPath .githooks"
    unwired=$((unwired+1))
  fi
}

# --- Check A: agent-cap PreToolUse hook in .claude/settings.json ----------------------------------
# Advisory: no mode mutates settings.json (the SessionStart hook must not rewrite its own file).
#
# THE MATCHER IS A LIST OF EXACT STRINGS separated by `|`, not a regular expression: the hook fires
# for `Workflow` (where it reads the script) and for `Agent` (where a direct spawn would otherwise
# meet no rule at all). A group carrying only `Workflow` is the stale state, and it is named by the
# value found rather than reported as a generic miss — an operator who is told "unwired" about a
# hook that is plainly in the file will conclude the checker is broken.
AGENTCAP_MATCHER='Workflow|Agent'
check_agentcap() {
  local smerge found; smerge=$(first_of tools/settings-merge.py settings-merge.py)
  # Left as a plain skip on purpose: agent-cap's hook path is not declared anywhere this script can
  # read (settings-merge.py hardcodes it), so "settings wired, script missing" cannot be told from a
  # deliberate out-of-tree copy. The recall arm below CAN — its fragment declares `hook_path`.
  if [ ! -f .claude/hooks/agent-cap.js ]; then
    echo "skip     agent-cap — not adopted (.claude/hooks/agent-cap.js absent)"
    return
  fi
  if wired "agent-cap.js" "$AGENTCAP_MATCHER"; then
    # TOOL-dTieredTribunal-14 S7 - a WIRED command may never carry --only. The flag narrows the hook
    # to one rule, so `--only=join` in settings.json turns the three cap rules off with no diff and a
    # hook that still looks wired. That is the class of the AGENT_CAP environment knob this file
    # deleted, whose own header records that it survived two releases by appearing to work.
    # matchers_of() discards the command, so the command text is read here rather than there.
    if grep -o '"command"[^"]*"[^"]*agent-cap\.js[^"]*"' .claude/settings.json 2>/dev/null | grep -q -- '--only'; then
      echo "UNWIRED  agent-cap — the wired command carries --only, which runs ONE rule and silently disables the rest. Remove the flag from .claude/settings.json."
      unwired=$((unwired+1))
      return
    fi
    echo "ok       agent-cap — PreToolUse hook wired in .claude/settings.json (matcher '$AGENTCAP_MATCHER')"
    return
  fi
  found=$(matchers_of "agent-cap.js" | paste -sd, - 2>/dev/null || matchers_of "agent-cap.js" | tr '\n' ',')
  if [ -n "$found" ]; then
    echo "UNWIRED  agent-cap — the hook is wired under matcher '$found', not '$AGENTCAP_MATCHER'; it never fires for a direct Agent spawn, which is the modality the arity rule was blind to. Fix: $PY ${smerge:-tools/settings-merge.py}"
  else
    echo "UNWIRED  agent-cap — agent-cap.js present but hook not in settings.json. Fix: $PY ${smerge:-tools/settings-merge.py}"
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
  frag=$(first_of hooks/scratch-guard.fragment.json tools/hooks/scratch-guard.fragment.json)
  if [ -z "$frag" ]; then
    echo "skip     scratch   — hooks kit does not ship scratch-guard.fragment.json here"
    return
  fi
  smerge=$(first_of tools/settings-merge.py settings-merge.py)
  marker=$(json_str "$frag" marker)
  hookjs=$(json_str "$frag" hook_path)
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
  if wired "$marker" "$smatcher"; then
    echo "ok       scratch   — PreToolUse guard wired in .claude/settings.json (matcher '$smatcher')"
    return
  fi
  # Name the value FOUND rather than reporting a generic miss: an operator told "unwired" about a
  # hook plainly present in the file concludes the checker is broken. Same reasoning as agent-cap.
  found=$(matchers_of "$marker" | paste -sd, - 2>/dev/null || matchers_of "$marker" | tr '\n' ',')
  if [ -n "$found" ]; then
    echo "UNWIRED  scratch   — the guard is wired under matcher '$found', not '$smatcher'; it never fires for the shells the fragment declares. Fix: $PY ${smerge:-tools/settings-merge.py} --fragment $frag"
  else
    echo "UNWIRED  scratch   — $hookjs present but the guard is not in settings.json. Fix: $PY ${smerge:-tools/settings-merge.py} --fragment $frag"
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
json_str() {  # value of a top-level "key": "..." in a small flat JSON file
  sed -n 's|.*"'"$2"'"[[:space:]]*:[[:space:]]*"\([^"]*\)".*|\1|p' "$1" | head -1
}
check_recall_opened() {
  local frag smerge marker hookjs rmatcher
  # Resolved by path because the kit is COPIED: <root>/memory-recall/ in an adopter,
  # <root>/tools/memory-recall/ in this repo.
  frag=$(first_of memory-recall/recall-opened.fragment.json tools/memory-recall/recall-opened.fragment.json)
  if [ -z "$frag" ]; then
    echo "skip     recall    — memory-recall kit not adopted (no recall-opened.fragment.json)"
    return
  fi
  smerge=$(first_of tools/settings-merge.py settings-merge.py)
  marker=$(json_str "$frag" marker)
  hookjs=$(json_str "$frag" hook_path)
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
  if wired "$marker" "$rmatcher"; then
    echo "ok       recall    — recall-opened PostToolUse hook wired in .claude/settings.json"
  else
    echo "UNWIRED  recall    — $hookjs present but hook not in settings.json. Fix: $PY ${smerge:-tools/settings-merge.py} --fragment $frag"
    unwired=$((unwired+1))
  fi
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
  # wider selector pulled in `.claude/settings.json` and a PNG, and `--fix` rewrote both: three CR
  # bytes stripped out of the middle of the image, md5 changed, reported as "fixed". A repair whose
  # bound depends on how an adopter spelled their attributes has no bound.
  #
  # NUL-byte guard as well, because a bound stated in a glob is still a claim: a binary that lands
  # under .claude/skills/ with a .md name is skipped rather than rewritten.
  # PER-PATH, not `xargs`: xargs word-splits on whitespace, so `.claude/skills/my skill/SKILL.md`
  # reached `git check-attr` as two nonexistent paths, the population came back empty, and the arm
  # printed a green `skip`. Reproduced — a folder name with a space is an ordinary thing to type. The
  # population is two files; a fork each is not a cost worth a silent collapse.
  pop=$(git ls-files .claude/skills/ 2>/dev/null | grep -E '\.md$' | while IFS= read -r _p; do
          [ -n "$_p" ] || continue
          git check-attr eol -- "$_p" 2>/dev/null | sed -n 's/^\(.*\): eol: lf$/\1/p'
        done)
  if [ -z "$pop" ]; then
    echo "skip     eol       — no tracked .claude/skills/**.md carries an eol=lf pin"
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
    echo "note     eol       — $f holds CRLF despite its eol=lf pin; the committed bytes are LF, so this is a working-copy artifact and does not gate. Fix: bash tools/check-wiring.sh --fix"
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
  # <root>/tools/memory-tree/ here. The remedy string is BUILT from the two resolved paths rather
  # than hand-kept, so it cannot drift from the layout it is describing.
  drv=$(first_of tools/memory-tree/merge-rows.py memory-tree/merge-rows.py)
  if [ -z "$drv" ]; then
    echo "skip     merge     — memory-tree merge driver not adopted (no merge-rows.py)"
    return
  fi
  # The KIT-INTERNAL launcher first. It travels with the kit, so it is the only one an adopter is
  # guaranteed to have; `tools/lib/pyrun.sh` is gov-internal and ships nothing, and a wiring that
  # names it in an adopting repo execs a command that cannot start. A driver that never starts never
  # writes %A, so git reports CONFLICT and leaves the path holding OURS-ONLY content with no markers.
  launcher=$(first_of "$(dirname "$drv")/merge-rows.sh" tools/lib/pyrun.sh lib/pyrun.sh)
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
  # time: `lib/resolve-python.sh`, which `pyrun.sh` sources, and the sibling memory-recall kit that
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
    echo "UNWIRED  merge     — the driver merged the smoke but printed no keyed/hashed audit line, so there is no way to tell whether it KEYED the rows or merely copied them; a driver whose anchor grammar is dead resolves this fixture too. Fix: the installed tools/memory-tree/merge-rows.py predates the audit line — re-copy the kit, then re-run"
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
      git config merge.rows.driver "$want" && echo "FIXED    merge     — set merge.rows.driver"
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

  if [ -n "$bad" ]; then
    echo "UNWIRED  skill     — the installed engine differs from tracked in:${bad}; this session is running a different engine than this repo ships. Fix: $fix"
    unwired=$((unwired+1))
    return
  fi
  echo "ok       skill     — the installed /session-kickoff engine matches tracked"
}

check_hooks
check_agentcap
check_scratch_guard
check_recall_opened
check_merge_rows
check_eol
check_skill_install

[ "$MODE" = session ] && exit 0
[ "$unwired" = 0 ] && exit 0 || exit 1
