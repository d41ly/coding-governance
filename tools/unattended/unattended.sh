#!/usr/bin/env bash
# unattended.sh — the driver for a run that will merge and push with no owner turn.
# Contract: memory/guides/UNATTENDED-PROTOCOL.md (binding). Project layer: .unattended.conf.
#
#   unattended.sh --preflight <slug> --keepalive-id <id>   # assert, pin, record, render
#   unattended.sh --plan <slug>                            # per-unit state, and the next unit
#   unattended.sh --phase <slug> <phase> --witness <sha>   # move the run, with its witness
#   unattended.sh --status <slug>                          # one line: phase · witness · next unit
#   unattended.sh --resume <slug>                          # the same line, plus the next action
#   unattended.sh --close <slug> [--override <item> --reason <text>]
#
# Exit 0 = the verb succeeded · 1 = a refusal, named · 2 = misconfigured (not a repo, no conf).
#
# THE DRIVER DOES LESS THAN IT LOOKS LIKE IT SHOULD, ON PURPOSE. Three of its verbs were specified
# with effects a script cannot produce, and the fix each time was to remove the effect rather than
# fake it:
#
#   * It RECORDS a keepalive id; it never schedules or reaps one. The scheduling store is in-memory
#     and session-scoped, reachable only through the agent's own tool calls. A verb that claimed to
#     schedule would be claiming an effect it cannot produce, and the DoD item keyed on it would be
#     a check that cannot fail.
#   * It ASSERTS the mandate; it never writes one, under any flag. A run that can author its own
#     authorization has none, and every gate downstream would certify it.
#   * It delegates wiring to the project's NON-repairing check. The repairing mode sets git config
#     and rewrites tracked bytes; the run's first act is not that.
#
# It also derives NOTHING. The generated region is a COPY of the build README's already-derived,
# already-byte-compared slice. One derivation in the tree; this file is not a second one.
set -u
KIT_UNATTENDED_VERSION=1.2   # gov:kit unattended@1.2 — kit identity; set HERE, never from .unattended.conf

# ------------------------------------------------------------------------------ the dereference pin
# A sha is a NAME, and turning a name into bytes or into ancestry happens in the run's own object
# store. Two one-command levers rewrite that dereference without touching a single tracked byte, and
# both defeat the mandate comparison no matter how trustworthy the anchor it is measured against is.
# Both MEASURED on this node, each against a live control:
#
#   * `git replace -f <base> <forged>` made `git show "<base>:<path>"` return bytes written seconds
#     earlier, at the true unforged base sha, with a clean worktree and an empty `git status`.
#   * a two-line `info/grafts` gave two UNRELATED histories a merge-base — a commit the run authored,
#     and not HEAD, so the degenerate-base refusal does not fire either.
#
# The suppressions are NOT interchangeable and neither covers both: `-c core.useReplaceRefs=false`
# left the graft fully effective, and `GIT_NO_REPLACE_OBJECTS=1` did too. Only `GIT_GRAFT_FILE`
# pointed away from the repo restored the honest answer. A command-line `-c` was measured to beat a
# repo-local `core.useReplaceRefs=true`, which is why it is spelled per-invocation and not configured.
#
# Every read below that turns a sha into bytes or into ancestry goes through GIT(). Reads of the
# index, the worktree or the ref NAMESPACE stay plain `git` — they are not dereferences.
export GIT_GRAFT_FILE=/dev/null
GIT() { git -c core.useReplaceRefs=false -c advice.graftFileDeprecated=false "$@"; }

ROOT="$(GIT rev-parse --show-toplevel 2>/dev/null)" || { echo "unattended: not a GIT repo"; exit 2; }
cd "$ROOT" || exit 2
CONF="$ROOT/.unattended.conf"
[ -f "$CONF" ] || { echo "unattended: no .unattended.conf at the repo root — the kit reads every"; \
                    echo "unattended: project-specific value from there and restates none of them."; exit 2; }
MEMORY_ROOT=memory; LANDER=""; BYPASS_BAN=""; GATE_CMD=""; WIRING_CHECK=""
KEEPALIVE_CREATE=""; KEEPALIVE_DELETE=""; PHASES_EXTRA=""; DOD_EXTRA=""
# shellcheck disable=SC1090
. "$CONF"
M="$MEMORY_ROOT"

status=0
fail() { echo "UNATTENDED check $1 FAILED — $2"; status=1; }

# ---------------------------------------------------------------- the kit-owned core declarations
# CORE, in run order. A project EXTENDS via PHASES_EXTRA and deletes nothing: the gate leg asserts
# core membership against a shrink-only floor, because a deletable core member is a silent,
# reason-free override of everything keyed on it.
PHASES_CORE="PREFLIGHT SPECCING REVIEWING FOLDING BUILDING RUNNING VERIFYING LANDING LANDED ABORTED"
PHASES_TERMINAL="LANDED ABORTED"
# CORE DoD items, `<item>:<checker>`. `agent` items are ATTESTED, never machine-verdicted, and they
# do not spend the --close override budget — counting attestation as a verdict is what makes an
# override look like a check that failed.
DOD_CORE="gates-green:machine records-current:machine authorization-reachable:machine landed-via-lander:machine keepalive-reaped:agent parked-decisions-surfaced:agent"

phases()  { printf '%s %s\n' "$PHASES_CORE" "$PHASES_EXTRA"; }
dod()     { printf '%s %s\n' "$DOD_CORE" "$DOD_EXTRA"; }
is_terminal() { case " $PHASES_TERMINAL " in *" $1 "*) return 0;; esac; return 1; }
checker_of()  { local p; for p in $(dod); do case "$p" in "$1:"*) printf '%s' "${p#*:}"; return;; esac; done; printf 'machine'; }

# ------------------------------------------------------------------------------ the region grammar
# Kit-owned, NOT a project declaration: an adopter chooses paths and commands, not the file's shape.
SRC_OPEN='<!-- gen:build-index -->'; SRC_CLOSE='<!-- /gen:build-index -->'
GEN_OPEN='<!-- run:generated -->';   GEN_CLOSE='<!-- /run:generated -->'

# Exactly one open, exactly one close, CLOSE AFTER OPEN, print the slice between them. Never a
# whole-file regex — the splice contract this borrows from gen_build_index.py's apply_region().
# Exit 3 = the marker pair is malformed, which is a different answer from "the slice is empty".
#
# THE ORDER CHECK IS NOT DECORATION. Both comments promised close-after-open and neither awk enforced
# it: a TRANSPOSED pair satisfies `no==1 && nc==1`, so `region` returned an empty slice at exit 0 and
# `splice` emitted everything up to the close, then dropped from the open marker to EOF — and the
# caller, seeing exit 0, moved that truncation over the run-state file. That deletes the
# owner-authored mandate block. Recording the two line numbers and comparing them is the whole fix.
region() { # file · open · close   (reads stdin when file is `-`)
  awk -v o="$2" -v c="$3" '
    { ln = $0; sub(/\r$/, "", ln) }
    index(ln, o) == 1 { if (ln != o) bad = 1; no++; if (no == 1) oat = NR; if (nc == 0) inside = 1; next }
    index(ln, c) == 1 { if (ln != c) bad = 1; nc++; if (nc == 1) cat = NR; inside = 0; next }
    inside { print }
    END { if (bad || no != 1 || nc != 1 || cat < oat) exit 3 }
  ' "$1"
}

# Replace the slice between the markers with the payload, keeping both markers. Same contract, and
# the same order check — this is the copy whose absence destroyed data rather than merely lying.
splice() { # file · open · close · payload-file
  awk -v o="$2" -v c="$3" -v pf="$4" '
    { ln = $0; sub(/\r$/, "", ln) }
    index(ln, o) == 1 { if (ln != o) bad = 1; no++; if (no == 1) oat = NR; print
                        while ((getline pl < pf) > 0) { sub(/\r$/, "", pl); print pl }
                        close(pf); skip = 1; next }
    index(ln, c) == 1 { if (ln != c) bad = 1; nc++; if (nc == 1) cat = NR; skip = 0; print; next }
    skip { next }
    { print }
    END { if (bad || no != 1 || nc != 1 || cat < oat) exit 3 }
  ' "$1"
}

runmd_of() { printf '%s/builds/%s/RUN.md' "$M" "$1"; }
readme_of() { printf '%s/builds/%s/README.md' "$M" "$1"; }
# One key per line, so a grep is the parser and no verb needs a second one.
fact() { # run-state file · key
  [ -f "$1" ] || return 1
  sed -n "s/^$2: *//p" "$1" | head -1 | tr -d '\r'
}

# --------------------------------------------------------------------------------- the anchor
# THE ANCHOR IS AN OBSERVATION OF THE REMOTE, not a read of any local ref and not a name from the
# environment. Both reported routes die by CONSTRUCTION rather than by detection: no `refs/remotes/*`
# is read at all, and no branch name from the environment ever reaches the anchor.
#
# What that is worth, stated exactly, because the comment this replaces overstated and it took two
# Tier-2 reviews to notice. This does NOT put the anchor outside the run's reach. A design panel
# broke four independent mechanisms and converged on the reduction: a check running under the run's
# own uid reads refs, objects, worktree files and config, and the run writes all four. What stays
# reachable is enumerated in memory/guides/UNATTENDED-PROTOCOL.md - a run that edits this kit, shims
# the tools it calls, skips the hook layer, or relays through an endpoint it seeded. None of those is
# closed here, and the control that actually binds lives on the remote.
#
# What IS bought: the two one-command offline forgeries become inert, the branch name comes from the
# party being pushed to, and the observation is RECORDED so a verifier off this machine can re-derive
# the pin without trusting a byte the run wrote.
AREF=""; ASHA=""; AURL=""
observe_anchor() {
  local v names rem uf up nrem levers adv rc aref asha envd
  # ---- 22: git config supplied through the ENVIRONMENT. A check reading a config its own caller
  # ---- injected is reading the run's answer rather than the repo's.
  names=""
  for v in GIT_CONFIG_COUNT GIT_CONFIG_PARAMETERS GIT_CONFIG_GLOBAL GIT_CONFIG_SYSTEM \
           GIT_DIR GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES GIT_NAMESPACE; do
    eval "[ -n \"\${$v:-}\" ]" && names="$names $v"
  done
  if [ -n "$names" ]; then
    fail 22 "git configuration is being supplied through the environment, and a check that reads a config its own caller injected is reading the run's answer rather than the repo's:$names"
    return 1
  fi
  # ---- 23: an object-substitution lever left on disk. The dereference pin above makes both INERT
  # ---- for this script's own reads, so this is a tripwire and not a barrier: it says the lever is
  # ---- here, and an unattended run is the wrong moment to guess why.
  levers=""
  [ -n "$(GIT for-each-ref --format='%(refname)' refs/replace 2>/dev/null)" ] && levers="$levers refs/replace"
  [ -f "$(GIT rev-parse --git-path info/grafts)" ] && levers="$levers info/grafts"
  if [ -n "$levers" ]; then
    fail 23 "this clone carries an object-substitution lever, which rewrites what a sha MEANS for every read below it, so the anchor can be honest and the bytes at it forged:$levers"
    return 1
  fi
  # ---- 24: exactly one remote. With two the kit would be CHOOSING which endpoint to believe, and
  # ---- the one it believes has to be the one the landing push goes to.
  nrem=$(GIT remote | grep -c . || true)
  if [ "$nrem" != 1 ]; then
    fail 24 "this clone declares a number of remotes other than one, and the anchor has to be the endpoint the landing push goes to, so the kit refuses to pick one: $nrem"
    return 1
  fi
  rem=$(GIT remote | head -1)
  # ---- 25: observe and push must be the SAME endpoint. A cost-raiser, NOT the property: a relay the
  # ---- run seeded satisfies it with one URL and one config source. Kept because it is free and
  # ---- catches the honest misconfiguration.
  uf=$(GIT ls-remote --get-url "$rem" 2>/dev/null)
  up=$(GIT remote get-url --push "$rem" 2>/dev/null)
  if [ "$uf" != "$up" ]; then
    fail 25 "the URL this clone would OBSERVE is not the URL it would PUSH to, so the anchor and the landing name two different endpoints: fetch $uf, push $up"
    return 1
  fi
  # ---- 27/28: the REMOTE names its own default branch. `--exit-code` is what makes "answered but
  # ---- advertised nothing" distinguishable from "answered": without it the call exits 0 and prints
  # ---- nothing, which is exactly what a bare repo with a dangling HEAD produces.
  adv=$(GIT_TERMINAL_PROMPT=0 GIT ls-remote --symref --exit-code "$rem" HEAD 2>/dev/null) && rc=0 || rc=$?
  if [ "$rc" != 0 ] && [ "$rc" != 2 ]; then
    fail 27 "the remote did not answer, and the anchor is an observation of it rather than of any local ref; a run that cannot reach the remote cannot land on it either: $rem at $uf"
    return 1
  fi
  aref=$(printf '%s\n' "$adv" | awk -F'\t' '{ sub(/\r$/,"",$2) } $2=="HEAD" && $1 ~ /^ref: / { sub(/^ref: /,"",$1); print $1; exit }')
  asha=$(printf '%s\n' "$adv" | awk -F'\t' '{ sub(/\r$/,"",$2) } $2=="HEAD" && $1 ~ /^[0-9a-f]+$/ { print $1; exit }')
  if [ -z "$aref" ] || [ -z "$asha" ]; then
    fail 28 "the remote answered but advertised no HEAD symref, so it named no default branch of its own and this kit will not choose one for it: $rem at $uf"
    return 1
  fi
  # ---- 29: the override becomes a CROSS-CHECK that can only refuse. As an INPUT it was route 2 of
  # ---- the reproduced bypass, and the gate leg read the same variable, so it computed the same
  # ---- wrong value and agreed with it.
  envd=${GOV_DEFAULT_BRANCH:-}
  if [ -n "$envd" ] && [ "refs/heads/$envd" != "$aref" ]; then
    fail 29 "GOV_DEFAULT_BRANCH names a branch the remote does not advertise as its default, and a branch the run can create with one push is not an anchor: env $envd against advertised $aref"
    return 1
  fi
  # ---- 30: the advertised tip has to BE here before a merge-base against it means anything.
  if ! GIT rev-parse --verify --quiet "$asha^{commit}" >/dev/null 2>&1; then
    fail 30 "the remote advertises a tip this clone does not have, so no merge-base can be computed against it; fetch and re-run: $aref at $asha"
    return 1
  fi
  AREF="$aref"; ASHA="$asha"; AURL="$uf"
  return 0
}

# Kept ONLY for check_branch's "am I standing on the default branch" question, and sourced from the
# observation whenever there is one. It is no longer on the authorization path.
default_branch() {
  [ -n "$AREF" ] && { printf '%s' "${AREF#refs/heads/}"; return 0; }
  if [ -n "${GOV_DEFAULT_BRANCH:-}" ]; then printf '%s' "$GOV_DEFAULT_BRANCH"; return 0; fi
  local d; d=$(GIT symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null) || return 1
  printf '%s' "${d#origin/}"
}

# BASE is the merge-base against the OBSERVED tip. Two non-zero returns carry meaning:
#   2 = the merge-base equals HEAD. Nothing was built on top of the anchor, so the comparison would
#       be trivially true. Still a refusal: F2 ratified equality over ancestry, because relaxing a
#       guard for a hazard nobody has reproduced is how the anchor bypass survived in the first place.
#   1 = there is no observed anchor, or no shared history with it.
resolve_base() {
  local mb
  [ -n "$ASHA" ] || return 1
  mb=$(GIT merge-base "$ASHA" HEAD 2>/dev/null) || return 1
  [ -n "$mb" ] || return 1
  [ "$mb" = "$(GIT rev-parse HEAD)" ] && return 2
  printf '%s\n' "$mb"; return 0
}

# The mandate assertion's inputs, re-derived and cross-checked, in ONE place so preflight and close
# cannot disagree about them. Returns the trustworthy base on stdout.
#
# `--close` used to read the base out of the run-state file — a file the run writes. With the
# `base:` line simply DELETED, the empty value made the comparison `git show ":$path"`, which is the
# git INDEX: both sides of the "did the run author this" test became bytes the run had just staged,
# and a forged mandate passed. So the recorded value is now EVIDENCE, never the input: it is
# compared against the freshly derived one and a mismatch or an absence is a refusal.
#
# RETURNS VIA A GLOBAL, not stdout. `fail` writes to stdout, so a caller written as
# `tb=$(trusted_base …)` CAPTURED the refusal into the variable instead of showing it: --close
# printed only the downstream symptom and never said why. Separating the value channel from the
# message channel is the fix, and it is why this function returns 0/1 and sets `TB`.
TB=""
trusted_base() { # run-state file [· allow-degenerate]  ->  sets TB
  local fresh rc rec
  TB=""
  fresh=$(resolve_base); rc=$?
  if [ "$rc" = 2 ]; then
    # BASE == HEAD. Legal only where the caller says so, and only ONE caller does - see verb_preflight.
    if [ "${2:-}" = "allow-degenerate" ]; then
      TB=$(GIT rev-parse HEAD)
      return 0
    fi
    fail 16 "the merge-base equals HEAD, so the run authored every byte the authorization comparison would read; nothing was built on top of the anchor"
    return 1
  fi
  if [ "$rc" != 0 ] || [ -z "$fresh" ]; then
    fail 16 "no merge-base against the tip the remote advertises, so this run shares no history with the branch it means to land on; the anchor is never a local ref and never a name from the environment"
    return 1
  fi
  if [ -f "$1" ]; then
    rec=$(fact "$1" base)
    if [ -n "$rec" ] && [ "$rec" != "$fresh" ]; then
      fail 18 "the BASE recorded in the run-state file is not the one this history derives, and the recorded value is written by the run: recorded $rec, derived $fresh"
      return 1
    fi
  fi
  TB="$fresh"
}

# ------------------------------------------------------------------------------------ preconditions
# The slug is validated against the SAME grammar hygiene check 4 enforces on a build folder, so a
# traversal argument is refused by the rule that would have refused the folder — not by a second one.
check_slug() {
  # Bound to a NAME, not used as `$1`: check-arms reads `${?[A-Za-z_]…` as an interpolation and a
  # bare positional as literal text, so a `$1` in a message lands in the signature and nothing can
  # arm the branch. Same reason the value trails the sentence.
  local slug="$1"
  case "$slug" in
    *[!A-Za-z0-9-]* | "" | [!A-Za-z]*)
      fail 1 "the slug is not a build-folder name; expected the slug alone, a letter then letters, digits or dashes: $slug"
      return 1 ;;
  esac
  return 0
}

check_clean() {
  # `git status --porcelain` alone is NOT the test. A linked worktree can carry a stale stat cache
  # and report a path modified whose content is byte-identical after the eol filter — measured on
  # this repo's own `.claude/skills/*/SKILL.md` renders. Refresh first, then ask about CONTENT.
  GIT update-index -q --refresh >/dev/null 2>&1 || true
  local d
  d=$( { GIT diff --name-only; GIT diff --cached --name-only; \
         GIT ls-files --others --exclude-standard; } | grep -c . || true)
  [ "$d" = 0 ] && return 0
  fail 2 "the working tree is dirty, so the pinned BASE would name a state that is not what runs: $d path(s)"
  return 1
}

check_branch() {
  local cur def; cur=$(GIT rev-parse --abbrev-ref HEAD 2>/dev/null)
  def=$(default_branch) || { fail 3 "cannot resolve the default branch (set GOV_DEFAULT_BRANCH) — refusing rather than assuming one"; return 1; }
  [ "$cur" != "$def" ] && return 0
  fail 3 "the run is on the default branch, where its own commits would land unreviewed on the branch it means to merge INTO: $def"
  return 1
}

check_wiring() {
  [ -n "$WIRING_CHECK" ] || { fail 4 "WIRING_CHECK is not declared in .unattended.conf — an undeclared wiring probe is not a passing one"; return 1; }
  # The NON-repairing mode, by declaration — expressed as an ALLOW-LIST, because the blacklist form
  # was one substring wide. `*--fix*` is walked through by every other repairing spelling a project
  # might declare, `--session` among them, and that mode repairs too. Naming what IS permitted makes
  # the unknown case a refusal instead of a pass.
  # Every DASH-LED token must be one this kit recognises as read-only. Word-split rather than
  # substring-matched, so `--session` (which repairs) is refused instead of walking through a
  # `*--fix*` blacklist, and a bare command with no flags is still legal.
  local tok
  for tok in $WIRING_CHECK; do
    case "$tok" in
      -*) case "$tok" in
            --check|--dry-run|--verify|-n) ;;
            *) fail 4 "WIRING_CHECK carries a flag this kit does not recognise as READ-ONLY, and preflight delegates to a check rather than a fix; permitted: --check, --dry-run, --verify, -n: $tok" ; return 1 ;;
          esac ;;
    esac
  done
  $WIRING_CHECK >/dev/null 2>&1 && return 0
  fail 4 "the declared wiring check failed, and a dormant hook makes every later green meaningless: $WIRING_CHECK"
  return 1
}

# At most one run-state file may be non-terminal, or "the run" is not well-defined and anything
# keyed on it must either OR the phases together or pick one arbitrarily.
check_single_live() {
  local n=0 f p live=""
  for f in $(GIT ls-files "$M/builds/*/RUN.md" 2>/dev/null); do
    p=$(fact "$f" phase); [ -n "$p" ] || continue
    is_terminal "$p" && continue
    n=$((n + 1)); live="$live $f"
  done
  [ "$n" -le 1 ] && return 0
  fail 5 "more than one run-state file is in a non-terminal phase, so 'the run' is not well-defined: $n live,${live}"
  return 1
}

# ONE comparison enforces BOTH provenance properties. At a pinned merge-base, "was it reachable from
# the BASE" and "did the run author it" are the same question, so there is one answer and one place
# for it to be wrong.
# S1 - THE AUTHORIZATION IS THE BUILD FOLDER, not a block the owner hand-writes into the file this
# driver then splices. A build README committed on the default branch before the run's branch existed
# is outside the run's reach in exactly the way the mandate block was, and it is a file the owner
# already writes when they shape a build. The owner's act is `/unattended <slug>` and nothing else.
#
# What this deletes, on purpose: the mandate marker pair and every comparison over it. The prior
# review found that a transposed pair made --preflight truncate the run-state file from the open
# marker to EOF - destroying the owner's only authored bytes - and only then print an unrelated
# refusal. There are no owner-authored bytes in that file now, so the worst case of that bug is the
# loss of regenerable state.
#
# What it costs, stated here because a reader of this function should not have to find it elsewhere:
# the check degrades from INTEGRITY to EXISTENCE. The README is a living document whose generated
# region the run legitimately re-renders, so no whole-file equality is assertable. The grant also
# widens from one build to every build folder in the tree, it names no ACTIONS, it cannot be revoked,
# and a run that lands a NEW build README authorizes the next run. All five are enumerated in
# memory/guides/UNATTENDED-PROTOCOL.md; the fifth is parked as P1 in the build README.
check_authorization() { # slug · base
  local slug="$1" base="$2" rel blob fmslug
  rel=$(readme_of "$slug")
  # NO GUARD HERE FOR AN EMPTY BASE, deliberately, and the reason is unchanged from the function this
  # replaces: an empty one makes the line below read `git show ":path"` - the git INDEX, i.e. bytes
  # the run itself staged, on both sides of a test about provenance. `trusted_base` is the ONLY
  # producer of this argument and refuses before returning, so a guard here would be a branch no
  # fixture can reach. The SOURCE-level arm in unattended.test.sh is what holds that invariant.
  if ! blob=$(GIT show "$base:$rel" 2>/dev/null); then
    fail 6 "no build README at the pinned BASE, so nothing committed before this run branched authorizes it, and a build folder the run created on its own branch authorizes nothing: $base:$rel"
    return 1
  fi
  # Front matter opens at LINE 1 and nowhere else - the same rule the build-index generator enforces, and for
  # the same reason: `---` is also a horizontal rule, so a parser that scans for the first pair can
  # swallow half a document. A blob that resolves but is not a build README means the path pointed at
  # something else entirely, which is a different failure from the folder being absent.
  case "$blob" in
    "---"*) ;;
    *) fail 7 "the blob at the pinned BASE is not a build README - front matter opens at line 1 and this does not, so the path resolved to something that is not a build: $base:$rel"
       return 1 ;;
  esac
  fmslug=$(printf '%s\n' "$blob" | awk '
    NR == 1 { next }
    /^---[[:space:]]*\r?$/ { exit }
    /^slug:/ { sub(/^slug:[[:space:]]*/, ""); sub(/[[:space:]]*\r?$/, ""); print; exit }')
  if [ "$fmslug" != "$slug" ]; then
    fail 20 "the build README at the pinned BASE declares a different slug, so the folder was renamed or its README copied from another build and the authorization does not name this one: declared $fmslug, requested $slug"
    return 1
  fi
  return 0
}

# S2 - the run-state file is CREATED by --preflight rather than asserted. It holds no owner bytes now,
# so there is nothing for the owner to author and nothing for a truncation to destroy.
#
# It is STAGED, not committed. The gate leg's whole per-run population is `git ls-files`, which reads
# the INDEX, so staging is what makes the run visible to every leg check; leaving it untracked would
# hand the run a silent opt-out from the entire leg. Committing it from here was the alternative and
# was rejected: a driver that makes commits has to decide about hooks, and the one flag it would reach
# for is the flag this kit bans.
scaffold_runmd() { # slug -> writes and stages <MEMORY_ROOT>/builds/<slug>/RUN.md
  local slug="$1" rel
  rel=$(runmd_of "$slug")
  mkdir -p "$(dirname "$rel")" || return 1
  {
    printf '# %s - run state\n\n' "$slug"
    printf 'Generated by `unattended.sh --preflight`. The generated region is a COPY of the build\n'
    printf 'README slice named by the same marker grammar; never hand-edit it.\n\n'
    printf '%s\n%s\n\n' "$GEN_OPEN" "$GEN_CLOSE"
    printf '## Run facts\n\n'
    printf '## Parked\n'
  } > "$rel" || return 1
  return 0
}

# Staged only AFTER the facts are written. Staging the blank scaffold put a blob with no base, phase
# or witness into the index - which is precisely what the gate leg reads.
stage_runmd() { # run-state file
  GIT add -- "$1" >/dev/null 2>&1 || return 1
  return 0
}

# --------------------------------------------------------------------------------------- the verbs
# S6 - the phase PRODUCER. Without it the vocabulary is decorative: only --preflight and --close ever
# wrote a phase, so every member between them could enter the file only by an agent hand-editing an
# artifact this kit calls generated. The witness is REQUIRED here for the same reason presence is its
# own refusal in the leg - an unwitnessed phase claim is the cheapest possible lie, and the run is the
# sole author of that field.
# S4 - the gap list, MECHANISED. The four states are the build method's M2 vocabulary spelled exactly
# - MISSING, THIN, FORKED, READY - and the RULE for each stays in M2. That document's own governing
# constraint is that a rule appearing both in it and in a carrier it points at is a defect IN IT, so
# this verb computes the classification and must not restate it. Read M2 for what each state MEANS.
#
# The roster is the tracked specs under the build's own `spec/`. M2 prefers the README's authored
# Units table where one exists; this verb does NOT parse that table, so it cannot see a planned unit
# that has no spec yet, and it says so in its own output rather than reporting a complete-looking
# list. Reporting three READY units and silently omitting the four nobody has specced is worse than
# reporting nothing.
#
# It performs NO filename join to `reviews/`. That join was measured wrong on 7 of 7 multi-unit builds
# in this corpus and right on none: a spec's sequence number is a per-build record counter and a
# review's is "which review is this", and they coincide only at one unit and one review.
plan_state() { # spec file -> prints the M2 state
  awk '
    /^## / { sec = ""
             if ($0 ~ /^## 2\./) sec = "scope"
             else if ($0 ~ /^## 6\./) sec = "acc"
             else if ($0 ~ /^## 7\./) sec = "gates"
             else if ($0 ~ /^## 8\./) sec = "forks"
             cur = sec; next }
    cur == "" { next }
    { line = $0; sub(/\r$/, "", line); gsub(/^[[:space:]]+|[[:space:]]+$/, "", line) }
    line == "" { next }
    { seen[cur] = seen[cur] 1
      if (cur == "forks" && forkline == "") forkline = line }
    END {
      thin = (seen["scope"] == "" || seen["acc"] == "" || seen["gates"] == "")
      # M2 orders the checks and the FIRST match wins, so THIN is decided before FORKED.
      if (thin) { print "THIN"; exit }
      lf = tolower(forkline)
      if (forkline == "" || lf ~ /^none/ || lf ~ /^n\/a/ || forkline ~ /RESOLVED/) print "READY"
      else print "FORKED"
    }' "$1"
}

verb_plan() { # slug
  local slug="$1" dir specs spec id st state next=""
  check_slug "$slug" || return 1
  dir="$M/builds/$slug"
  specs=$(git ls-files "$dir/spec/*.md" 2>/dev/null)
  if [ -z "$specs" ]; then
    fail 19 "no tracked spec under this build, so every planned unit is MISSING and this verb cannot say which - the roster it would need is the README's authored Units table, which it does not parse: $dir/spec"
    return 1
  fi
  for spec in $specs; do
    st=$(sed -n 's/^\*\*Status:\*\* \([A-Z]*\) .*/\1/p' "$spec" | head -1 | tr -d '\r')
    # NO status header, NO unit. M2 defines a unit's spec as the file whose STATUS HEADER carries the
    # id, so a file without one is a recording that happens to live here. Taking it anyway made this
    # verb invent units and name one as `next` on 5 of the 25 builds in this corpus.
    if [ -z "$st" ]; then
      printf '%-34s %-11s %s\n' "$(basename "$spec")" "-" "NOT A UNIT (no status header)"
      continue
    fi
    id=$(sed -n 's/^# \([A-Za-z0-9][A-Za-z0-9-]*\) .*/\1/p' "$spec" | head -1 | tr -d '\r')
    [ -n "$id" ] || id=$(basename "$spec" .md)
    state=$(plan_state "$spec")
    case "$st" in CLOSED|WONTDO) state="DONE" ;; esac
    printf '%-34s %-11s %s\n' "$id" "${st:-?}" "$state"
    case "$state" in
      THIN|FORKED) [ -n "$next" ] || next="$id ($state)" ;;
      READY)       [ -n "$next" ] || next="$id (READY - build it)" ;;
    esac
  done
  echo "roster: tracked specs under $dir/spec (a planned unit with no spec is invisible here)"
  if [ -n "$next" ]; then echo "next: $next"; else echo "next: none - every tracked spec is terminal"; fi
  return 0
}

verb_phase() { # slug · phase · witness
  local slug="$1" want="$2" wit="$3" rel
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to move: $rel"; return 1; }
  case " $(phases) " in
    *" $want "*) ;;
    *) fail 19 "the phase is not in the declared vocabulary, and a phase nothing recognises is not a position: $want" ; return 1 ;;
  esac
  # A TERMINAL phase is --close's to write, never this verb's. Vocabulary membership is not
  # permission: a run that could set LANDED here would skip the entire Definition-of-Done gate, and
  # the two agent-attested items are enforced in no other place.
  if is_terminal "$want"; then
    fail 19 "a terminal phase is --close's to write and not this verb's, because reaching it through here would skip the whole Definition-of-Done gate: $want"
    return 1
  fi
  [ -n "$wit" ] || { fail 11 "a phase claim carries a WITNESS - a sha, a tag or a run id - and presence is its own refusal because an unwitnessed claim is the one an oracle skips: $want"; return 1; }
  set_fact "$rel" phase "$want" || return 1
  set_fact "$rel" witness "$wit" || return 1
  echo "unattended: phase $want · witness $wit"
  return 0
}


verb_preflight() { # slug · keepalive-id
  local slug="$1" kid="$2" rel base src payload tmp
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -n "$kid" ] || fail 8 "no --keepalive-id was supplied — scheduling is the AGENT's half of the split and only the agent can do it; the driver records the id it is handed"
  # The anchor is observed BEFORE anything that consumes it, and its refusals do not cascade: a
  # failed observation leaves ASHA empty and the base block below is skipped entirely, so the
  # operator reads why the observation failed rather than a second, unrelated merge-base complaint.
  observe_anchor || true
  check_clean || true
  check_branch || true
  check_wiring || true
  check_single_live || true
  # ONE entry point for the base, shared with --close, so the two verbs cannot disagree about which
  # commit they are measuring against. `trusted_base` names its own refusals.
  #
  # S3 - `allow-degenerate` is passed HERE and nowhere else. A merge-base equal to HEAD is the normal
  # state of a run that has correctly built nothing yet, which is every run at preflight; refusing it
  # here refused every run this kit exists to enable. It stays a refusal at --close, where a run that
  # built nothing has nothing to land. The premise is sound only because the anchor is observed: with
  # merge-base == HEAD, HEAD is an ancestor of the tip the REMOTE advertised, so every byte at BASE is
  # on the remote's default branch. Against a local ref that premise was false, which is why this
  # relaxation could not have shipped before the anchor moved.
  if [ -n "$ASHA" ] && trusted_base "$rel" allow-degenerate; then
    base="$TB"
    check_authorization "$slug" "$base" || true
  fi
  # NOTHING is written until every precondition above has passed. A verb that writes and then
  # discovers a refusal has already changed the state the refusal was about.
  [ "$status" = 0 ] || { echo "unattended: --preflight refused; the run-state file is unchanged"; return 1; }

  # The run-state file is created here, AFTER every precondition passed. A verb that scaffolds and
  # then discovers a refusal has already changed the state the refusal was about.
  if [ ! -f "$rel" ]; then
    scaffold_runmd "$slug" || { fail 9 "cannot create the run-state file, so there is nothing for the run to record its phase, witness and parked decisions in: $rel"; return 1; }
  fi

  src=$(readme_of "$slug")
  payload=$(mktemp) || return 2
  tmp=$(mktemp) || { rm -f "$payload"; return 2; }
  if ! region "$src" "$SRC_OPEN" "$SRC_CLOSE" > "$payload"; then
    rm -f "$payload" "$tmp"
    fail 9 "the build README's generated markers are malformed, and the region is COPIED from there, so an unpaired marker is not something to guess around: $src"
    return 1
  fi
  if ! splice "$rel" "$GEN_OPEN" "$GEN_CLOSE" "$payload" > "$tmp"; then
    rm -f "$payload" "$tmp"
    fail 9 "the run-state file's generated markers are malformed — exactly one open and one close, close after open: $rel"
    return 1
  fi
  mv "$tmp" "$rel"; rm -f "$payload"
  set_fact "$rel" base "$base"      || return 1
  set_fact "$rel" anchor-ref "$AREF" || return 1
  set_fact "$rel" anchor-sha "$ASHA" || return 1
  set_fact "$rel" anchor-url "$AURL" || return 1
  set_fact "$rel" keepalive "$kid"  || return 1
  # ONLY when the file carries no phase yet. Preflight used to rewrite this unconditionally, so a
  # resumed run that had reached BUILDING was silently moved back to RUNNING by the verb it is told
  # to re-run after a compaction.
  [ -n "$(fact "$rel" phase)" ] || set_fact "$rel" phase RUNNING || return 1
  set_fact "$rel" witness "$(GIT rev-parse HEAD)" || return 1
  stage_runmd "$rel" || { fail 9 "cannot stage the run-state file, and the gate leg's whole per-run population is the index, so an unstaged run is invisible to every check it has: $rel"; return 1; }
  echo "unattended: preflight OK — base $base · anchor $AREF at $ASHA · keepalive $kid · region copied from $src"
  return 0
}

# Rewrite one `key: value` line in place, or append it under the Run facts heading if absent.
# A key that can be placed NEITHER way is a REFUSAL, not a silent drop: the caller would otherwise
# report a successful preflight over a file carrying none of the facts it just claimed to record.
set_fact() { # file · key · value
  local f="$1" k="$2" v="$3" tmp; tmp=$(mktemp) || return 2
  if grep -q "^$k: " "$f"; then
    awk -v k="$k" -v v="$v" '{ if (index($0, k ": ") == 1) print k ": " v; else print }' "$f" > "$tmp"
  elif grep -qF '## Run facts' "$f"; then
    awk -v k="$k" -v v="$v" '{ print } index($0, "## Run facts") == 1 { print k ": " v }' "$f" > "$tmp"
  else
    rm -f "$tmp"
    fail 17 "cannot record a run fact — the file carries neither that key's line nor a Run facts heading to put one under: $k in $f"
    return 1
  fi
  mv "$tmp" "$f"
}

verb_status() { # slug
  local slug="$1" rel p w unit
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to report on: $rel"; return 1; }
  p=$(fact "$rel" phase); w=$(fact "$rel" witness)
  [ -n "$p" ] || { fail 10 "the run-state file declares no phase, and a run with no phase is not resumable: $rel"; return 1; }
  # The first non-terminal unit, read from the COPIED generated region — never re-derived.
  unit=$(region "$rel" "$GEN_OPEN" "$GEN_CLOSE" 2>/dev/null \
         | grep -E '^\| \[' | grep -vE '\| (CLOSED|WONTDO) \|' | head -1 \
         | sed -e 's/^| \[//' -e 's/\].*//')
  [ -n "$unit" ] || unit="(no non-terminal unit)"
  printf 'unattended: %s · phase %s · witness %s · next %s\n' "$slug" "$p" "${w:-NONE}" "$unit"
  [ -n "$w" ] || { fail 11 "the phase carries no witness, and presence is its own refusal: an oracle that skips an unwitnessed claim makes naming no witness the cheapest way to say nothing. Phase: $p"; return 1; }
  return 0
}

verb_resume() { # slug
  verb_status "$1" || return 1
  local rel p; rel=$(runmd_of "$1"); p=$(fact "$rel" phase)
  if is_terminal "$p"; then
    echo "unattended: nothing to resume — phase $p is terminal"
  else
    echo "unattended: resume at phase $p — read $rel, then continue the first non-terminal unit above"
    # The method path is DERIVED from MEMORY_ROOT, never recorded as a run fact: the authored region
    # carries five facts and never restates a derivable one (protocol section 2).
    [ -f "$M/guides/BUILD-METHOD.md" ] && echo "unattended: re-read the build method at $M/guides/BUILD-METHOD.md"
  fi
  return 0
}

verb_close() { # slug · override-item · reason
  local slug="$1" ov="$2" reason="$3" rel item ck unmet=0
  check_slug "$slug" || return 1
  # The SAME observation preflight made, made again here rather than read back from the record the
  # run wrote. Its refusals are not fatal to --close: authorization-reachable simply cannot be met without
  # an anchor, which is the honest outcome and is not overridable.
  observe_anchor >/dev/null 2>&1 || true
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to close: $rel"; return 1; }
  if [ -n "$ov" ]; then
    case " $(dod) " in *" $ov:"*) ;;
      *) fail 12 "--override names an item that is not in the declared DoD set, and an override on an item nobody declared is not an override: $ov"; return 1;; esac
    [ -n "$reason" ] || { fail 12 "--override requires --reason: an unrecorded override is indistinguishable from a passing check"; return 1; }
    # THE AUTHORIZATION ITEM IS NOT OVERRIDABLE. The protocol says so in one sentence — "There is no
    # override for this one" — and the generic loop happily accepted it, which makes the override on
    # the authorization check the authorization check. Named here so the refusal cites the rule.
    case "$ov" in
      authorization-reachable)
        fail 21 "the authorization item is NOT overridable; an override on the authorization check IS the authorization check, and the protocol states there is no override for this one"
        return 1 ;;
    esac
  fi
  for item in $(dod); do
    item=${item%%:*}; ck=$(checker_of "$item")
    [ "$item" = "$ov" ] && continue
    if ! dod_met "$slug" "$rel" "$item" "$ck"; then
      unmet=$((unmet + 1))
      if [ "$ck" = agent ]; then
        fail 13 "an agent-attested DoD item is unmet; the driver can only read back what the agent recorded, so this is an attestation, not a machine verdict: $item"
      else
        fail 13 "a machine-checked DoD item is unmet, so --close blocks: $item"
      fi
    fi
  done
  [ "$unmet" = 0 ] || return 1
  if [ -n "$ov" ]; then
    park "$rel" "$ov" "$reason"
    echo "unattended: override recorded for '$ov' (checker $(checker_of "$ov")) — parked entry written"
  fi
  # The phase write is the CLOSE. Reporting success before checking it printed "close OK" over a
  # file still reading RUNNING, which is the two-answers class in the verb whose whole job is to
  # make the record agree with reality.
  set_fact "$rel" phase LANDING || return 1
  echo "unattended: close OK — every declared DoD item met; phase LANDING. Land with: $LANDER"
  return 0
}

# What the driver can honestly answer for each core item. Anything it cannot observe is reported as
# agent-attested and read back from the record, never invented.
dod_met() { # slug · run-state file · item · checker
  local slug="$1" rel="$2" item="$3" ck="$4"
  case "$item" in
    authorization-reachable)
      # RE-DERIVED, never read out of the run-state file. That file is written by the subject of the
      # test, and an absent `base:` line used to degenerate the comparison to the git index. The
      # ASHA guard is not decoration: with no observation there is no anchor, and an unanchored
      # merge-base is the thing this item exists to refuse.
      [ -n "$ASHA" ] && trusted_base "$rel" && check_authorization "$slug" "$TB" >/dev/null 2>&1 ;;
    gates-green)
      [ -n "$GATE_CMD" ] && $GATE_CMD >/dev/null 2>&1 ;;
    records-current)
      region "$rel" "$GEN_OPEN" "$GEN_CLOSE" 2>/dev/null \
        | diff -q - <(region "$(readme_of "$slug")" "$SRC_OPEN" "$SRC_CLOSE" 2>/dev/null) >/dev/null 2>&1 ;;
    landed-via-lander)
      [ -n "$LANDER" ] && [ -n "$BYPASS_BAN" ] && ! grep -qF -- "$BYPASS_BAN" "$rel" ;;
    keepalive-reaped)
      grep -qE '^keepalive-reaped: (yes|true)' "$rel" ;;
    parked-decisions-surfaced)
      grep -qE '^parked-surfaced: (yes|true)' "$rel" ;;
    *)  # a PROJECT item the kit knows nothing about: it is attested unless the project says otherwise
      grep -qE "^$item: (yes|true)" "$rel" ;;
  esac
}

park() { # file · item · reason
  printf '\n%s override · item %s · reason %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$2" "$3" >> "$1"
}

# --------------------------------------------------------------------------------------- dispatch
VERB=""; SLUG=""; KID=""; OV=""; REASON=""; arg=""
while [ $# -gt 0 ]; do
  case "$1" in
    --preflight|--status|--resume|--close) VERB="$1"; SLUG="${2:-}"; shift 2 || shift ;;
    --keepalive-id) KID="${2:-}"; shift 2 || shift ;;
    --override)     OV="${2:-}";  shift 2 || shift ;;
    --reason)       REASON="${2:-}"; shift 2 || shift ;;
    --plan)         shift; verb_plan "${1:-}"; exit $? ;;
    --phase)        shift; PH_SLUG=${1:-}; shift 2>/dev/null || true; PH_WANT=${1:-}; shift 2>/dev/null || true
                    PH_WIT=""
                    [ "${1:-}" = "--witness" ] && { shift; PH_WIT=${1:-}; }
                    verb_phase "$PH_SLUG" "$PH_WANT" "$PH_WIT"; exit $? ;;
    --version)      echo "unattended $KIT_UNATTENDED_VERSION"; exit 0 ;;
    *) arg="$1"; fail 14 "unknown argument; the verbs are --preflight, --plan, --phase, --status, --resume and --close: $arg"; exit 1 ;;
  esac
done
[ -n "$VERB" ] || { echo "usage: unattended.sh --preflight <slug> --keepalive-id <id> | --status <slug> | --resume <slug> | --close <slug> [--override <item> --reason <text>]"; exit 2; }

case "$VERB" in
  --preflight) verb_preflight "$SLUG" "$KID" ;;
  --status)    verb_status "$SLUG" ;;
  --resume)    verb_resume "$SLUG" ;;
  --close)     verb_close "$SLUG" "$OV" "$REASON" ;;
esac
exit "$status"
