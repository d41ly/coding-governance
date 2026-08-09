#!/usr/bin/env bash
# check-wiring.sh — detect coding-governance tools installed-but-unwired in THIS repo, and
# (with --fix/--session) wire the zero-risk ones. Spec: memory/tooling/builds/2026-07-15-TOOL-aWireWarden/.
#
#   check-wiring.sh            # --check (default): report; exit 1 if any installed tool is unwired
#   check-wiring.sh --fix      # wire the safe cases (core.hooksPath when unset); exit reflects remainder
#   check-wiring.sh --session  # like --fix but ALWAYS exit 0 — the SessionStart hook mode
#
# Wiring the git hooks opts into running this repo's committed hooks (a git trust boundary). Auto-fix
# sets core.hooksPath ONLY when unset and NEVER overwrites an already-set value (e.g. a deliberate
# out-of-tree copy per WIRE-INTO-PROJECT.md §5). Agent-cap wiring is never auto-applied — it would mean
# rewriting settings.json, the file the SessionStart hook lives in.
KIT_CHECK_WIRING_VERSION=1.0
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

# THE wired signal, for every arm: the hook's marker substring present in .claude/settings.json.
# settings-merge.py documents that same substring as the deployer's is-it-wired test (its module
# docstring), so this is the one predicate stated once — not a second spelling of it. Grepping it
# directly also removes the "settings-merge.py absent, cannot verify" skip, which was a false
# all-clear in every adopter (the tool is copied in per WIRE §3c step 4 / §5, so an arm that
# REQUIRED it to answer reported `skip … exit 0` on the state the runbook calls the one bad state).
wired() { [ -f .claude/settings.json ] && grep -qF "$1" .claude/settings.json; }

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
check_agentcap() {
  local smerge; smerge=$(first_of tools/settings-merge.py settings-merge.py)
  # Left as a plain skip on purpose: agent-cap's hook path is not declared anywhere this script can
  # read (settings-merge.py hardcodes it), so "settings wired, script missing" cannot be told from a
  # deliberate out-of-tree copy. The recall arm below CAN — its fragment declares `hook_path`.
  if [ ! -f .claude/hooks/agent-cap.js ]; then
    echo "skip     agent-cap — not adopted (.claude/hooks/agent-cap.js absent)"
    return
  fi
  if wired "agent-cap.js"; then
    echo "ok       agent-cap — PreToolUse hook wired in .claude/settings.json"
  else
    echo "UNWIRED  agent-cap — agent-cap.js present but hook not in settings.json. Fix: $PY ${smerge:-tools/settings-merge.py}"
    unwired=$((unwired+1))
  fi
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
  local frag smerge marker hookjs
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
  if [ -z "$marker" ] || [ -z "$hookjs" ]; then
    echo "UNWIRED  recall    — $frag declares no marker/hook_path; settings-merge.py refuses it too. Fix: restore the shipped fragment"
    unwired=$((unwired+1))
    return
  fi
  if [ ! -f "$hookjs" ]; then
    if wired "$marker"; then
      echo "UNWIRED  recall    — settings.json dispatches the hook but $hookjs is missing; every Read runs node against nothing. Fix: bash $(dirname "$frag")/adopt-memory-recall.sh --scaffold --with-hook"
      unwired=$((unwired+1))
    else
      echo "skip     recall    — recall-opened hook opt-in not taken (adopt-memory-recall.sh --with-hook)"
    fi
    return
  fi
  if wired "$marker"; then
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
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    echo "UNWIRED  eol       — $f holds CRLF despite its eol=lf pin; a byte-comparing gate will report every line as drift. Fix: bash tools/check-wiring.sh --fix"
    unwired=$((unwired+1))
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
  local drv shim want cur declared
  # Resolved by path because the kit is COPIED: <root>/memory-tree/ in an adopter,
  # <root>/tools/memory-tree/ here. The remedy string is BUILT from the two resolved paths rather
  # than hand-kept, so it cannot drift from the layout it is describing.
  drv=$(first_of tools/memory-tree/merge-rows.py memory-tree/merge-rows.py)
  if [ -z "$drv" ]; then
    echo "skip     merge     — memory-tree merge driver not adopted (no merge-rows.py)"
    return
  fi
  shim=$(first_of tools/lib/pyrun.sh lib/pyrun.sh)
  if [ -z "$shim" ]; then
    echo "UNWIRED  merge     — $drv is present but the shim it names is missing (tools/lib/pyrun.sh); git would exec a command that cannot start. Fix: copy tools/lib/pyrun.sh + tools/lib/resolve-python.sh in"
    unwired=$((unwired+1))
    return
  fi
  want="bash $shim $drv %O %A %B %P"
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
  # merges", and the three tests above — driver exists, shim exists, config string matches — are all
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
  # Three one-line scratch inputs that merge CLEANLY exercise the whole chain in one python start:
  # launcher resolution, the driver's own syntax, the `.memory-tree.conf` walk-up, the deferred
  # grammar import, and the `%A` write. That is one process per session-start, which is what a
  # verifier that verifies costs.
  local smoke rc_smoke=0
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
  printf 'x\n'    > "$smoke/o"
  printf 'a\nx\n' > "$smoke/a"
  printf 'x\nb\n' > "$smoke/b"
  bash "$shim" "$drv" "$smoke/o" "$smoke/a" "$smoke/b" merge-rows-smoke \
    >/dev/null 2>"$smoke/err" || rc_smoke=$?
  # rc alone is not enough: assert the driver WROTE theirs' line into %A. A driver that exits 0
  # without touching %A is the same silent take-ours by another route.
  if [ "$rc_smoke" != 0 ] || ! grep -q '^b$' "$smoke/a"; then
    echo "UNWIRED  merge     — the configured driver cannot merge: 'bash $shim $drv' exited $rc_smoke on a no-op three-way ($(head -1 "$smoke/err" 2>/dev/null | tr -d '\r')). git prints CONFLICT and leaves the path holding OURS-only content with NO markers. Fix: restore $(dirname "$shim")/resolve-python.sh and the sibling memory-recall kit, then re-run"
    unwired=$((unwired+1))
    rm -rf "$smoke"
    return
  fi
  rm -rf "$smoke"
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

check_hooks
check_agentcap
check_recall_opened
check_merge_rows
check_eol

[ "$MODE" = session ] && exit 0
[ "$unwired" = 0 ] && exit 0 || exit 1
