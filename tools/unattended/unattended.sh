#!/usr/bin/env bash
# unattended.sh — the four-verb driver for a run that will merge and push with no owner turn.
# Contract: memory/guides/UNATTENDED-PROTOCOL.md (binding). Project layer: .unattended.conf.
#
#   unattended.sh --preflight <slug> --keepalive-id <id>   # assert, pin, record, render
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
KIT_UNATTENDED_VERSION=1.0   # gov:kit unattended@1.0 — kit identity; set HERE, never from .unattended.conf

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "unattended: not a git repo"; exit 2; }
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
PHASES_CORE="PREFLIGHT RUNNING VERIFYING LANDING LANDED ABORTED"
PHASES_TERMINAL="LANDED ABORTED"
# CORE DoD items, `<item>:<checker>`. `agent` items are ATTESTED, never machine-verdicted, and they
# do not spend the --close override budget — counting attestation as a verdict is what makes an
# override look like a check that failed.
DOD_CORE="gates-green:machine records-current:machine mandate-reachable:machine landed-via-lander:machine keepalive-reaped:agent parked-decisions-surfaced:agent"

phases()  { printf '%s %s\n' "$PHASES_CORE" "$PHASES_EXTRA"; }
dod()     { printf '%s %s\n' "$DOD_CORE" "$DOD_EXTRA"; }
is_terminal() { case " $PHASES_TERMINAL " in *" $1 "*) return 0;; esac; return 1; }
checker_of()  { local p; for p in $(dod); do case "$p" in "$1:"*) printf '%s' "${p#*:}"; return;; esac; done; printf 'machine'; }

# ------------------------------------------------------------------------------ the region grammar
# Kit-owned, NOT a project declaration: an adopter chooses paths and commands, not the file's shape.
SRC_OPEN='<!-- gen:build-index -->'; SRC_CLOSE='<!-- /gen:build-index -->'
GEN_OPEN='<!-- run:generated -->';   GEN_CLOSE='<!-- /run:generated -->'
MAN_OPEN='<!-- run:mandate -->';     MAN_CLOSE='<!-- /run:mandate -->'

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
    index($0, o) == 1 { no++; if (no == 1) oat = NR; if (nc == 0) inside = 1; next }
    index($0, c) == 1 { nc++; if (nc == 1) cat = NR; inside = 0; next }
    inside { print }
    END { if (no != 1 || nc != 1 || cat < oat) exit 3 }
  ' "$1"
}

# Replace the slice between the markers with the payload, keeping both markers. Same contract, and
# the same order check — this is the copy whose absence destroyed data rather than merely lying.
splice() { # file · open · close · payload-file
  awk -v o="$2" -v c="$3" -v pf="$4" '
    index($0, o) == 1 { no++; if (no == 1) oat = NR; print
                        while ((getline pl < pf) > 0) { sub(/\r$/, "", pl); print pl }
                        close(pf); skip = 1; next }
    index($0, c) == 1 { nc++; if (nc == 1) cat = NR; skip = 0; print; next }
    skip { next }
    { print }
    END { if (no != 1 || nc != 1 || cat < oat) exit 3 }
  ' "$1"
}

runmd_of() { printf '%s/builds/%s/RUN.md' "$M" "$1"; }
readme_of() { printf '%s/builds/%s/README.md' "$M" "$1"; }
# One key per line, so a grep is the parser and no verb needs a second one.
fact() { # run-state file · key
  [ -f "$1" ] || return 1
  sed -n "s/^$2: *//p" "$1" | head -1 | tr -d '\r'
}

default_branch() {
  if [ -n "${GOV_DEFAULT_BRANCH:-}" ]; then printf '%s' "$GOV_DEFAULT_BRANCH"; return 0; fi
  local d; d=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null) || return 1
  printf '%s' "${d#origin/}"
}

# The BASE the whole mandate assertion hangs on — so every input to it must be OUTSIDE the run's
# reach. It was not. Three separate defeats, all reproduced:
#
#   * A bare LOCAL branch is not an anchor. `git branch -f main HEAD` makes the merge-base equal
#     HEAD, and the mandate at BASE is then the mandate the run just wrote. The earlier code
#     refused to FALL BACK to HEAD and happily accepted being MOVED to it — same destination, and
#     the comment saying otherwise made it harder to see.
#   * A remote-TRACKING ref is the weakest thing the run cannot rewrite. Moving it requires a push,
#     which is the act being authorized, so using it is not circular.
#   * BASE == HEAD is refused outright even when the ref is legitimate. Nothing was built on top of
#     it, so there is no diff to authorize and the comparison is trivially true.
resolve_base() {
  local d b mb; d=$(default_branch) || return 1
  for b in "refs/remotes/origin/$d" "refs/remotes/$d"; do
    git rev-parse --verify --quiet "$b" >/dev/null 2>&1 || continue
    mb=$(git merge-base "$b" HEAD 2>/dev/null) || continue
    [ -n "$mb" ] || continue
    # Degenerate: the anchor is at or ahead of HEAD, so BASE is HEAD and the run authored everything
    # the comparison reads.
    [ "$mb" = "$(git rev-parse HEAD)" ] && return 2
    printf '%s\n' "$mb"; return 0
  done
  return 1
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
trusted_base() { # run-state file  ->  sets TB
  local fresh rc rec
  TB=""
  fresh=$(resolve_base); rc=$?
  if [ "$rc" = 2 ]; then
    fail 16 "the merge-base equals HEAD, so the run authored every byte the mandate comparison would read; nothing was built on top of the anchor"
    return 1
  fi
  if [ "$rc" != 0 ] || [ -z "$fresh" ]; then
    fail 16 "cannot resolve a merge-base against a remote-tracking default branch — refusing rather than trusting a local ref the run can move with 'git branch -f', or HEAD, either of which makes the mandate check pass by construction"
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
  git update-index -q --refresh >/dev/null 2>&1 || true
  local d
  d=$( { git diff --name-only; git diff --cached --name-only; \
         git ls-files --others --exclude-standard; } | grep -c . || true)
  [ "$d" = 0 ] && return 0
  fail 2 "the working tree is dirty, so the pinned BASE would name a state that is not what runs: $d path(s)"
  return 1
}

check_branch() {
  local cur def; cur=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
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
  for f in $(git ls-files "$M/builds/*/RUN.md" 2>/dev/null); do
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
check_mandate() { # slug · base
  local rel base_blob a b rc
  rel=$(runmd_of "$1"); local base="$2"
  # NO GUARD HERE FOR AN EMPTY BASE, deliberately. An empty one would make the line below read
  # `git show ":path"` — the git INDEX, i.e. bytes the run itself staged, on both sides of a test
  # about provenance. That is exactly how a forged mandate passed. The fix is upstream: `trusted_base`
  # is the ONLY producer of this argument and it refuses before returning, so a guard here would be a
  # branch no fixture can reach. `unattended.test.sh` asserts at SOURCE level that every call site
  # is guarded, which is the house pattern for a hazard no input can produce.
  if ! base_blob=$(git show "$base:$rel" 2>/dev/null); then
    fail 6 "no run-state file at the pinned BASE, so the mandate cannot be reachable — the owner authors and commits it BEFORE the run starts: $base:$rel"
    return 1
  fi
  # THE EXIT STATUS IS THE POINT, and `|| true` threw it away on both sides. `region` exits 3 on a
  # malformed pair — including a SECOND mandate block — and swallowing that made a run-authored
  # second block invisible: the first block matched, the extra one granting force-push was never
  # compared to anything, and preflight printed OK.
  a=$(printf '%s\n' "$base_blob" | region - "$MAN_OPEN" "$MAN_CLOSE" 2>/dev/null); rc=$?
  if [ "$rc" != 0 ]; then
    fail 20 "the run-state file at the pinned BASE does not carry exactly one well-formed mandate block, so there is no single authorization to compare against"
    return 1
  fi
  b=$(region "$rel" "$MAN_OPEN" "$MAN_CLOSE" 2>/dev/null); rc=$?
  if [ "$rc" != 0 ]; then
    fail 20 "the working copy does not carry exactly one well-formed mandate block; a second block is a second authorization nobody granted"
    return 1
  fi
  if [ -z "$(printf '%s' "$a" | tr -d '[:space:]')" ]; then
    fail 7 "the mandate block is absent or empty at the pinned BASE — a mandate introduced after the branch point is one the run could have written, and grants nothing"
    return 1
  fi
  if [ "$a" != "$b" ]; then
    fail 7 "the mandate block differs from the one at the pinned BASE — the run edited its own authorization"
    return 1
  fi
  return 0
}

# --------------------------------------------------------------------------------------- the verbs
verb_preflight() { # slug · keepalive-id
  local slug="$1" kid="$2" rel base src payload tmp
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -n "$kid" ] || fail 8 "no --keepalive-id was supplied — scheduling is the AGENT's half of the split and only the agent can do it; the driver records the id it is handed"
  check_clean || true
  check_branch || true
  check_wiring || true
  check_single_live || true
  if [ ! -f "$rel" ]; then
    fail 15 "no run-state file to assert against — preflight asserts a mandate, it does not create one: $rel"
  else
    # ONE entry point for the base, shared with --close, so the two verbs cannot disagree about
    # which commit they are measuring against. `trusted_base` names its own refusals.
    if trusted_base "$rel"; then
      base="$TB"
      check_mandate "$slug" "$base" || true
    fi
  fi
  # NOTHING is written until every precondition above has passed. A verb that writes and then
  # discovers a refusal has already changed the state the refusal was about.
  [ "$status" = 0 ] || { echo "unattended: --preflight refused; the run-state file is unchanged"; return 1; }

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
  set_fact "$rel" keepalive "$kid"  || return 1
  set_fact "$rel" phase RUNNING     || return 1
  set_fact "$rel" witness "$(git rev-parse HEAD)" || return 1
  echo "unattended: preflight OK — base $base · keepalive $kid · region copied from $src"
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
      mandate-reachable)
        fail 21 "the mandate item is NOT overridable; an override on the authorization check IS the authorization check, and the protocol states there is no override for this one"
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
    mandate-reachable)
      # RE-DERIVED, never read out of the run-state file. That file is written by the subject of the
      # test, and an absent `base:` line used to degenerate the comparison to the git index.
      trusted_base "$rel" && check_mandate "$slug" "$TB" >/dev/null 2>&1 ;;
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
    --version)      echo "unattended $KIT_UNATTENDED_VERSION"; exit 0 ;;
    *) arg="$1"; fail 14 "unknown argument; the verbs are --preflight, --status, --resume and --close: $arg"; exit 1 ;;
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
