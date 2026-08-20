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
#   unattended.sh --landed <slug>                          # after the push: observe, then mark LANDED
#   unattended.sh --park <slug> --item <text> --reason <text>   # park a decision MID-RUN
#   unattended.sh --rescope <slug> --act <retire|supersede|add> --item <id> [--successor <id>] --reason <text>
#   unattended.sh --dispatch <slug> --pass <id> --writes <path> [--writes <path> ...]
#   unattended.sh --abort <slug> --reason <text>           # end it, with the reason on the record
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
# The generated region holds NO copy: the unit list is DERIVED from the build README's already-derived,
# already-byte-compared slice. One derivation in the tree; this file is not a second one.
set -u
KIT_UNATTENDED_VERSION=1.7   # gov:kit unattended@1.7 — kit identity; set HERE, never from .unattended.conf

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
# TOOL-dUnstalledConvoy-9 - condition 3's two halves are DECLARED, and both defaults sit ON the two
# init lines below for the reason ANCHOR_SCOPE's comment already gives. SHARED_RECORDS defaults to a
# memory tree at its conventional layout. GENERATED_INDEXES defaults to the EMPTY SET on purpose: its
# value pairs an index with its GENERATOR, and a generator belongs to some other kit whose install
# path this kit may not presume. A project declares it; blank means the conditional half is off.
# ANCHOR_SCOPE defaults to the STRICT anchor: a blank, a typo or a value from a newer kit all keep
# `default-branch`, because a value-set guard falling through to the wide behaviour would let a
# misspelling grant what nobody declared. It sits ON the second line because the source-level arm
# greps the line below with -A1, and anything inserted between them hides it.
MEMORY_ROOT=memory; LANDER=""; BYPASS_BAN=""; GATE_CMD=""; WIRING_CHECK=""
KEEPALIVE_CREATE=""; KEEPALIVE_DELETE=""; PHASES_EXTRA=""; DOD_EXTRA=""; DIRECTIVES_EXTRA=""; ANCHOR_SCOPE=""; UNITS_REGION_CUTOFF=""; SHARED_RECORDS="$MEMORY_ROOT/DECISIONS.md $MEMORY_ROOT/backlog"; GENERATED_INDEXES=""
# shellcheck disable=SC1090
. "$CONF"
# ARGV STATE, not a conf default. Initialised AFTER the conf is sourced: in the default block above,
# a tracked `.unattended.conf` could pre-set it and defeat the "--park requires --item" refusal by
# supplying the item nobody typed.
PK_ITEM=""
M="$MEMORY_ROOT"

status=0
fail() { echo "UNATTENDED check $1 FAILED — $2"; status=1; }

# ---------------------------------------------------------------- the kit-owned core declarations
# CORE, in run order. A project EXTENDS via PHASES_EXTRA and deletes nothing: the gate leg asserts
# core membership against a shrink-only floor, because a deletable core member is a silent,
# reason-free override of everything keyed on it.
PHASES_CORE="PREFLIGHT RESEARCHING TESTING SPECCING REVIEWING FOLDING BUILDING RUNNING VERIFYING LANDING LANDED ABORTED"
PHASES_TERMINAL="LANDED ABORTED"
# TOOL-aPromptedMandate-2 - the subset NAMED FOR the build method's pass kinds, published so the
# protocol's claim about it can be JOINED rather than believed. RESEARCHING and TESTING are
# deliberately absent: the method closes its pass set and neither is in it, so they are POSITIONS a
# prompt-started run occupies while performing the passes that set does name. Adding a phase and
# calling it a pass kind now has to move this line, and the leg reds if the contract disagrees.
PHASES_PASSKIND="SPECCING REVIEWING FOLDING BUILDING"
# CORE DoD items, `<item>:<checker>`. `agent` items are ATTESTED, never machine-verdicted, and they
# do not spend the --close override budget — counting attestation as a verdict is what makes an
# override look like a check that failed.
DOD_CORE="gates-green:machine records-current:machine authorization-reachable:machine landed-via-lander:machine build-complete:machine closing-review-recorded:machine keepalive-reaped:agent parked-decisions-surfaced:agent"

# TOOL-cBriefedPilot-2 - the DEFAULT DIRECTIVE SET. Eleven handles, each a NAME and a POINTER into
# a section of the build method, and NOT ONE of them a restatement of the rule it points at. The
# method's own M1 forbids a rule appearing both there and in a carrier it points at, and this is a
# carrier; a gloss here that grew into a condition would be that defect.
#
# Kit-owned, like the two sets above it, and for the same reason: the owner asked that these be
# MUST-by-default. A conf key would let a project declare zero directives, which is a global waiver
# carrying no name, no reason and no record. DIRECTIVES_EXTRA is where a project ADDS.
#
# Two handles may cite one section - the section is the carrier, not the rule.
# TOOL-aPromptedMandate-4 - an entry is `<handle>:<section>[:<scope>]`. The THIRD field is the
# layer's first CONDITIONAL member: `prompt` binds only a run whose authorization declared that
# mode, `all` (the default, and what an absent field means) binds every run. Two-field entries are
# therefore unchanged in meaning, which is what keeps every adopter's registry working untouched.
#
# The scope is NOT a project knob. A project may EXTEND the set; it may not narrow the core, and a
# project-selectable scope is narrowing wearing a different name.
DIRECTIVES_CORE="minimal-prose:M10 sub-specced:M2 forks-resolved:M3 specs-reviewed:M4 reuse-first:M5 parallel-when-disjoint:M6 passes-committed:M6 diff-reviewed:M8 land-once-done:M8 conflicts-reconciled:M8 wrap-up-derived:M9 researched:M12:prompt solution-tested:M12:prompt"

phases()  { printf '%s %s\n' "$PHASES_CORE" "$PHASES_EXTRA"; }
dod()     { printf '%s %s\n' "$DOD_CORE" "$DOD_EXTRA"; }
# TOOL-cBriefedPilot-2 - the third instance of a shape that already had two. Unit 3's membership test
# for a --waive handle reads THIS, so the effective set is composed in one place rather than in each
# consumer.
directives() { printf '%s %s\n' "$DIRECTIVES_CORE" "$DIRECTIVES_EXTRA"; }
# TOOL-aPromptedMandate-4 - ONE splitter for the three-field entry, so no consumer re-derives it.
# The two-field default falls out of the shortest/longest-prefix pair rather than being tested for,
# which is why it cannot disagree with itself: with no third field `${rest#*:}` returns `rest`.
scope_of() { # handle -> its declared scope; `all` when the entry carries no third field
  local p rest sc
  for p in $(directives); do
    case "$p" in "$1:"*) rest=${p#*:}; sc=${rest#*:}
      [ "$sc" = "$rest" ] && sc=all
      printf '%s' "$sc"; return ;;
    esac
  done
  printf 'all'
}
is_terminal() { case " $PHASES_TERMINAL " in *" $1 "*) return 0;; esac; return 1; }
checker_of()  { local p; for p in $(dod); do case "$p" in "$1:"*) printf '%s' "${p#*:}"; return;; esac; done; printf 'machine'; }

# ------------------------------------------------------------------------------ the region grammar
# Kit-owned, NOT a project declaration: an adopter chooses paths and commands, not the file's shape.
SRC_OPEN='<!-- gen:build-index -->'; SRC_CLOSE='<!-- /gen:build-index -->'
GEN_OPEN='<!-- run:generated -->';   GEN_CLOSE='<!-- /run:generated -->'
# S8 - the marker pair delimiting the build method's roster. It does NOT introduce a second roster:
# M2 already makes the README's authored Units table the roster, and this only makes that same table
# machine-locatable. Locating it structurally instead - the slice between one heading and the next -
# was the cheaper option and was refused: a renamed heading silently empties the comparison, which is
# a check that passes by finding nothing.
# TOOL-aBoundedVerdict-11 S8 - NARROWED, not retired. Four of the authored pair's five readers moved
# to the GENERATED units region: the authorization scope comparison, `--plan`'s malformed-pair refusal,
# and `build-complete`'s presence and non-empty terms. The FIFTH stays - `roster_ids`, which feeds
# `missing_units` - because an authored plan is the only thing that can name a unit nobody has specced
# yet, and reading the generated region there made the difference empty by construction. Absent, the
# pair costs nothing. The spec said RETIRED; that was wrong and is corrected there too.
ROSTER_OPEN='<!-- roster:units -->'; ROSTER_CLOSE='<!-- /roster:units -->'
# TOOL-aBoundedVerdict-11 S1/S2 - the GENERATED units region, nested inside the build-index pair.
# Addressed BY NAME. The three readers below used to select unit rows out of the enclosing region by
# ROW SHAPE, and `gen_build_index.py` renders a records table into that same region, so every review
# and journal record counted as an unfinished unit: `build-complete` could not pass on any build
# holding a record, `--landed` would have frozen record filenames as the units a run covered, and
# `--status` told a resuming agent its next unit was a shell script under `build/`.
UNITS_OPEN='<!-- gen:build-units -->'; UNITS_CLOSE='<!-- /gen:build-units -->'

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
#
# NO LIVE CALLER since the unit list became derived rather than copied. KEPT, deliberately and with
# the reason in place rather than left to be rediscovered: it is the marker-region WRITE half of a
# contract whose read half (`region`) is still load-bearing, the two are gated together by
# `marker-contract.test.sh`'s case table, and deleting it would leave that contract with only a
# reader. A function retained for a stated reason is not the same thing as one nobody noticed.
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
# PURE BASH, no forks. This was `sed … | head -1 | tr -d '\r'` — three processes per call, at sixteen
# call sites. Process spawn dominates on Windows and it is what made the sibling self-tests cost 77s
# and 73s for ~1.4s of CPU apiece. Same semantics: first matching line wins, `key:` followed by any
# run of spaces, a valueless key yields the empty string, a trailing CR is stripped.
fact() { # run-state file · key
  [ -f "$1" ] || return 1
  local l p="$2:"
  while IFS= read -r l || [ -n "$l" ]; do
    l=${l%$'\r'}
    case "$l" in
      "$p"*) l=${l#"$p"}; while [ "${l# }" != "$l" ]; do l=${l# }; done; printf '%s\n' "$l"; return 0 ;;
    esac
  done < "$1"
  return 0
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
# TOOL-aPromptedMandate-1 - the authorization MODE, read from the build README at the pinned BASE by
# check_authorization and recorded by --preflight. An out-parameter with the return code as the
# verdict, which is this file's idiom for every other derived value (observe_anchor, resolve_base,
# trusted_base, dod_met). It is EVIDENCE and never an input: nothing in this kit branches on the
# recorded value, for the reason anchor-kind carries in its own comment.
AUTH_MODE=""
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

# THE SECOND ANCHOR, and it is an observation of the SAME endpoint the first one used. It runs only
# when `resolve_base` needs it, so an adopter on `default-branch` pays no extra `ls-remote`.
#
# The run's own branch NAME is read locally and that is sound: a forged local name merely selects a
# different remote ref to observe, and the authorization still requires the remote to advertise that
# ref AND a conforming build README to resolve at the tip it advertises. What is never read locally
# is the TIP — that comes from the advertisement, exactly as the first anchor's does.
BREF=""; BSHA=""
# SILENT, and that is load-bearing. `fail` sets the global `status`, which has no reset in this
# file, so a SPECULATIVE probe that called it would make every run that merely CONSIDERED the second
# anchor exit non-zero. S12's monotone test probes speculatively on a path where the first anchor
# already succeeded, so the two concerns are split: this returns a tip or nothing and says why via
# its return code, and observe_branch turns those codes into the numbered refusals.
#   1 = not on a named branch · 2 = the remote advertises no tip for it
#   3 = advertised a tip this clone lacks · 4 = the tip is not an ancestor of HEAD
branch_tip_quiet() { # -> prints "<ref> <sha>" on stdout
  local cur rem adv sha
  cur=$(GIT rev-parse --abbrev-ref HEAD 2>/dev/null) || return 1
  [ -n "$cur" ] && [ "$cur" != HEAD ] || return 1
  rem=$(GIT remote 2>/dev/null | head -1)
  [ -n "$rem" ] || return 2
  adv=$(GIT_TERMINAL_PROMPT=0 GIT ls-remote --exit-code "$rem" "refs/heads/$cur" 2>/dev/null) || return 2
  sha=$(printf '%s\n' "$adv" | awk -F'\t' '{ sub(/\r$/,"",$2) } $1 ~ /^[0-9a-f]+$/ { print $1; exit }')
  [ -n "$sha" ] || return 2
  GIT rev-parse --verify --quiet "$sha^{commit}" >/dev/null 2>&1 || return 3
  # S2: a tip that is NOT an ancestor of HEAD is a branch this run is not building on, and pinning
  # to it would measure the authorization against history this run does not contain.
  GIT merge-base --is-ancestor "$sha" HEAD 2>/dev/null || return 4
  printf '%s %s\n' "refs/heads/$cur" "$sha"
  return 0
}
# THE MESSAGE CHANNEL, separate from the value channel ON PURPOSE. `resolve_base` sets globals and
# must therefore run WITHOUT a command substitution; it also must not `fail`, because a refusal raised
# inside it competes with the value it is computing. So it records WHY in BR_RC and stays silent, and
# this turns that code into the numbered refusal — called by trusted_base, which has the caller's
# context. Both halves of that split were learned here the hard way: first the refusal was captured
# into `$fresh`, then the globals were discarded by the subshell.
BR_RC=""
emit_branch_fail() { # BR_RC -> the numbered refusal it stands for
  local cur; cur=$(GIT rev-parse --abbrev-ref HEAD 2>/dev/null)
  case "${1:-}" in
    1) fail 31 "the run is not on a named branch, so there is no branch for the remote to advertise a tip for, and a detached HEAD cannot be the second anchor" ;;
    2) fail 32 "the remote advertises no tip for the branch this run is on, so nothing published authorizes it; push the branch first: refs/heads/$cur" ;;
    3) fail 30 "the remote advertises a branch tip this clone does not have, so no comparison against it means anything; fetch and re-run: refs/heads/$cur" ;;
    4) fail 33 "the advertised tip of this run's branch is not an ancestor of HEAD, so it names history this run does not build on and cannot be its base: refs/heads/$cur" ;;
    *) return 0 ;;
  esac
  return 1
}
# BASE is the merge-base against the OBSERVED tip. Two non-zero returns carry meaning:
#   2 = the merge-base equals HEAD. Nothing was built on top of the anchor, so the comparison would
#       be trivially true. Still a refusal: F2 ratified equality over ancestry, because relaxing a
#       guard for a hazard nobody has reproduced is how the anchor bypass survived in the first place.
#   1 = there is no observed anchor, or no shared history with it.
#
# S1: it takes the resolved README PATH so the fallback has a trigger. The trigger is a SILENT
# existence probe and NOT a call to check_authorization: that function answers by calling `fail 6`,
# which prints a numbered refusal and sets the global `status` that has no reset in this file, so
# every successful branch-anchored preflight would have emitted "UNATTENDED check 6 FAILED" on its
# way to succeeding. Shape only lives in check_authorization; existence only lives here.
ANCHOR_KIND=""; RB_BASE=""
# RETURNS VIA A GLOBAL, not stdout — the same rule `trusted_base` states below, and for a reason this
# unit re-learned the hard way. A caller written as `fresh=$(resolve_base …)` runs it in a SUBSHELL,
# so ANCHOR_KIND, BREF, BSHA and BR_RC were all set and then thrown away, and every second-anchor
# refusal surfaced as check 16 while the recorded anchor-kind silently stayed default-branch.
resolve_base() { # readme path (may be empty) -> sets RB_BASE, ANCHOR_KIND, BREF, BSHA, BR_RC
  local mb rel="${1:-}" head _bt
  ANCHOR_KIND=""; RB_BASE=""
  [ -n "$ASHA" ] || return 1
  mb=$(GIT merge-base "$ASHA" HEAD 2>/dev/null) || return 1
  [ -n "$mb" ] || return 1
  head=$(GIT rev-parse HEAD)
  # The FIRST anchor, unchanged, and it keeps its rc=2 contract.
  if [ -z "$rel" ] || GIT show "$mb:$rel" >/dev/null 2>&1; then
    ANCHOR_KIND=default-branch
    [ "$mb" = "$head" ] && return 2
    RB_BASE="$mb"; return 0
  fi
  # The README does not resolve at the merge-base. Widen ONLY when the project declared it; any
  # other value — blank, misspelled, from a newer kit — keeps the strict anchor and the caller gets
  # the same refusal it got before this unit existed.
  [ "$ANCHOR_SCOPE" = published ] || { ANCHOR_KIND=default-branch; [ "$mb" = "$head" ] && return 2; RB_BASE="$mb"; return 0; }
  # SILENT. This function's stdout is the VALUE channel — a `fail` raised here lands in the
  # caller's variable instead of reaching the operator, which is how every second-anchor refusal
  # came out as check 16. trusted_base emits, outside the substitution.
  _bt=$(branch_tip_quiet); BR_RC=$?
  [ "$BR_RC" = 0 ] || return 1
  BREF=${_bt%% *}; BSHA=${_bt##* }
  # S11: the rc=2 contract is PRESERVED on this path too. Both `fail 16` branches gate on it, and
  # without this the fallback would reach them through rc=0 and silence both for every
  # branch-anchored run — while check-arms stays green, because the branches are still reachable on
  # the default-branch path.
  ANCHOR_KIND=run-branch
  [ "$BSHA" = "$head" ] && return 2
  RB_BASE="$BSHA"; return 0
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
# Set by dod_met when an unmet item has something to SAY beyond its name; verb_close prints it
# indented under the refusal and clears it. Empty means the item had nothing to add.
DOD_OUT=""
trusted_base() { # run-state file [· allow-degenerate]  ->  sets TB
  local fresh rc rec head rec0 _tb_rd _tb_alt
  TB=""
  # S1's plumbing: the README beside the run-state file, derived the way the gate leg derives it
  # (`${f%/RUN.md}/README.md`) so the two halves of one kit spell it once. `resolve_base` needs it to
  # decide whether the FIRST anchor carries the build folder; handed nothing it keeps the old
  # behaviour, which is what the degenerate preflight path relies on.
  _tb_rd="${1%/RUN.md}/README.md"
  ANCHOR_KIND=""; BREF=""; BSHA=""; BR_RC=""
  resolve_base "$_tb_rd"; rc=$?; fresh="$RB_BASE"
  # The second anchor's refusals are emitted HERE, outside the command substitution that would have
  # eaten them. Without this the operator saw check 16 ("no merge-base") for every one of them.
  if [ "$rc" = 1 ] && [ -n "$BR_RC" ] && [ "$BR_RC" != 0 ]; then
    emit_branch_fail "$BR_RC"
    return 1
  fi
  if [ "$rc" = 2 ]; then
    # BASE == HEAD. Legal outright where the caller says so, and only ONE caller does - see
    # verb_preflight, where a run has correctly built nothing yet and the file may not exist at all.
    if [ "${2:-}" = "allow-degenerate" ]; then
      TB=$(GIT rev-parse HEAD)
      return 0
    fi
    # NARROWED, not deleted. The refusal that used to sit here fired UNCONDITIONALLY at --close and
    # said "the run authored every byte the authorization comparison would read; nothing was built on
    # top of the anchor". Under the OBSERVED anchor that sentence is false: a merge-base equal to HEAD
    # means HEAD is an ANCESTOR of the tip the remote advertises, so every byte at the base is
    # PUBLISHED. It dates from an anchor that was a local ref the run could rewrite offline, where the
    # same condition really did mean "the anchor is my own commit" - and verb_preflight's own comment
    # already says the relaxation is sound precisely because the anchor moved.
    #
    # Reproduced on this repo's tree with a control: --close refused, and the record was byte-identical
    # afterwards, so it was a WEDGE rather than a corruption. Every successful landing ends in exactly
    # this state, so the kit could not close any run that had landed.
    #
    # What the refusal bought was the run that built NOTHING, and the merge-base cannot express that:
    # it equals HEAD in the built-nothing state AND in the fully-landed state. The RECORDED base can,
    # because it is pinned once at preflight and does not move. So the guard stays at the verb the
    # owner scoped it to and its QUESTION changes.
    #
    # THE COST, ACCEPTED BY THE OWNER WITH IT NAMED (build fork F3, 2026-08-13): the recorded base is
    # written by the run, so a run can edit one line to pass this refusal. Three things bound it and
    # none removes it. It decides only WHETHER to refuse - the commit the authorization comparison
    # reads is the derived, published one, never this value. An ABSENT value is a refusal, not a pass,
    # which is what keeps this path out of the class where a deleted base line degenerated a
    # comparison to the git index. And leg check 9 asserts the same facts independently on the bar.
    head=$(GIT rev-parse HEAD)
    rec0=$(fact "$1" base)
    if [ -z "$rec0" ]; then
      fail 16 "the merge-base equals HEAD and the record pins no BASE to tell a landed run from one that built nothing, and an absent discriminator is a refusal rather than a pass"
      return 1
    fi
    if [ "$rec0" = "$head" ]; then
      fail 16 "the recorded BASE equals HEAD, so this run built nothing on top of the anchor and has nothing to land; that is the state the merge-base could not distinguish from a landed one"
      return 1
    fi
    # FALL THROUGH to the shared cross-check below with the derived value set to HEAD. The early
    # return this replaces SKIPPED that cross-check entirely, so --close now runs a comparison on this
    # path that no caller used to run.
    fresh="$head"
  elif [ "$rc" != 0 ] || [ -z "$fresh" ]; then
    fail 16 "no merge-base against the tip the remote advertises, so this run shares no history with the branch it means to land on; the anchor is never a local ref and never a name from the environment"
    return 1
  fi
  # ANCESTRY, NOT EQUALITY — carried here from this kit's own gate leg (check 9), which was moved off
  # equality for a reason the driver was never given. Equality wedged the bar permanently: merging and
  # then pushing, the two acts an authorization grants, move the merge-base past the pin forever. It
  # is worse than that in practice, because the MANDATED lander reconciles origin BEFORE the gate — so
  # every run whose remote moved met a refusal on the one path it is required to take, and the only
  # exits were to stall or to edit this kit. Reproduced live on 2026-08-11 with no attacker anywhere
  # near it.
  #
  # What survives, and what the leg tests in the same words: the recorded BASE lies on the history the
  # ANCHOR blesses rather than on the branch the run authored. `--is-ancestor $rec $fresh` is exactly
  # the leg's pair of ancestor tests — a commit that is an ancestor of both the anchor and HEAD is an
  # ancestor of their merge-base, and `$fresh` IS that merge-base — so this is one rule with one
  # spelling, not a second opinion. A base the run forged on its own branch is an ancestor of HEAD and
  # NOT of `$fresh`, which is the case that must still refuse.
  #
  # The recorded value stays EVIDENCE and never becomes the input: `TB` is the freshly derived base,
  # exactly as before.
  if [ -f "$1" ]; then
    rec=$(fact "$1" base)
    if [ -n "$rec" ]; then
      if ! GIT rev-parse --verify --quiet "$rec^{commit}" >/dev/null 2>&1; then
        fail 18 "the BASE recorded in the run-state file does not resolve to a commit in this history, and the recorded value is written by the run: recorded $rec"
        return 1
      fi
      # S12, and it is a MONOTONE derivation rather than a discriminator. With two anchors the
      # derivation stops being stable across a run: if the build folder reaches the default branch
      # mid-run — another node lands it, or this run merges origin — the FIRST anchor starts firing,
      # `$fresh` moves to the merge-base, and a recorded branch tip is not an ancestor of it. That
      # refuses at `--close`, `authorization-reachable` is not overridable and `LANDING` is
      # close-only, so the run wedges in a non-terminal phase with `--abort` as its only exit. A
      # wedge with no attacker in it, reachable by another node simply doing its job.
      #
      # The fix is NOT to read `anchor-kind` back: the run writes that value, and a verb branching on
      # it would be the inputs-inside-the-subject's-reach defect wearing a new key — the class this
      # kit has been burned by three times. Instead nothing selects: a recorded BASE on EITHER
      # derivation is accepted, so the anchor that fired is irrelevant and never has to be remembered.
      #
      # THE COST: `fail 18` widens. It now fires only for a base on NEITHER history, which is
      # strictly smaller than before, so S9 carries an arm proving it still has a failing case. A
      # widened guard with no failing-case arm is indistinguishable from a deleted one.
      if ! GIT merge-base --is-ancestor "$rec" "$fresh" 2>/dev/null \
         && ! { [ "$ANCHOR_SCOPE" = published ] \
                && _tb_alt=$(branch_tip_quiet) \
                && GIT merge-base --is-ancestor "$rec" "${_tb_alt##* }" 2>/dev/null; }; then
        fail 18 "the BASE recorded in the run-state file is not an ancestor of the base this history derives, so it names a commit off the history the anchor blesses - which is where a run's own commits live: recorded $rec, derived $fresh"
        return 1
      fi
      # NO THIRD BRANCH. The leg tests ancestor-of-anchor AND ancestor-of-HEAD separately, and both
      # are reachable THERE because it compares against the anchor ref. Here the comparison is
      # against the merge-base, and an ancestor of the merge-base is an ancestor of HEAD by
      # construction — so a second test could never fire. It was written, found unreachable, and
      # removed rather than shipped as a guard with no failing case.
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
  local wout
  wout=$($WIRING_CHECK 2>&1) && return 0
  fail 4 "the declared wiring check failed, and a dormant hook makes every later green meaningless: $WIRING_CHECK"
  # The declared check's OWN output, indented under the refusal rather than discarded. It already
  # carries whatever remedy that project's check knows about, and this kit may not spell a repairing
  # command itself: nothing it may read holds one — the conf declares no repairing counterpart and
  # the allow-list above refuses any token outside --check|--dry-run|--verify|-n — and the driver
  # self-test reds if this source spells one at all. Surfacing beats naming, and works for any adopter.
  [ -n "$wout" ] && printf '%s\n' "$wout" | sed 's/^/    /'
  return 1
}

# At most one run-state file may be non-terminal, or "the run" is not well-defined and anything
# keyed on it must either OR the phases together or pick one arbitrarily.
# TOOL-cBriefedPilot-4 - every directive this run is bound by is a POINTER into a section of the
# build method. A tree with no carrier holds a directive set that resolves to nothing, and before
# this branch the run started anyway with nobody present to notice.
#
# The path expression is verb_resume's, not a second spelling and not a conf key: a key would be a
# second name for a derivable value, which .unattended.conf's own header bans, and two spellings of
# one path is how they drift apart. EXISTENCE only - what the sections CONTAIN is leg check 16 arm
# B's question, and that arm stays SILENT exactly where this refuses, because the leg grades the
# TREE and the driver grades the RUN.
#
# The path is bound to a NAME and placed last. check-arms reads the literal text up to the first
# interpolation as the branch's signature, so a message that resumes after one can never be armed.
check_method() {
  local carrier="$M/guides/BUILD-METHOD.md"
  [ -f "$carrier" ] && return 0
  fail 34 "no build method under the memory root, so every directive this run is bound by points into a file that does not exist: $carrier"
  return 1
}

# TOOL-cBriefedPilot-3 - refusals 2 through 5. These CAN live in the precondition block, because
# they are about the invocation's own content and verb_preflight is the only verb that reaches them.
# The block writes nothing until every one has passed, so a refused invocation leaves the run-state
# file byte-identical - which is the property the arms assert, not merely the exit code.
recorded_waivers() { # run-state file -> the handles already parked, sorted
  [ -f "$1" ] || return 0
  # ANCHORED on the timestamp the writer emits, not on `^.*`. Greedy, that leading wildcard matched
  # the LAST " waiver · item X · reason " on the line, so a reason quoting that shape could name a
  # handle the owner never waived — and refusal 38 compares against exactly this reading.
  sed -n 's/^[0-9][0-9-]*T[0-9:]*Z waiver · item \([^ ]*\) · reason .*$/\1/p' "$1" | sort -u
}
check_waiver_scope() { # -> refuses a scoped waiver a run of this mode is not bound by
  local n=${#WAIVE_ITEMS[@]} i=0 h sc
  [ "$n" -gt 0 ] || return 0
  while [ "$i" -lt "$n" ]; do
    h=${WAIVE_ITEMS[$i]}; sc=$(scope_of "$h")
    if [ "$sc" = prompt ] && [ "${AUTH_MODE:-}" != prompt ]; then
      fail 45 "--waive names a directive scoped to prompt-authorized runs while this run is not one, so the waiver would record the relaxation of a rule that never bound it: $h"
      return 1
    fi
    i=$((i + 1))
  done
  return 0
}

check_waivers() { # run-state file
  local rel="$1" n=${#WAIVE_ITEMS[@]} i=0 h r want have
  [ "$n" -gt 0 ] || return 0
  while [ "$i" -lt "$n" ]; do
    h=${WAIVE_ITEMS[$i]}; r=${WAIVE_REASONS[$i]}
    case " $(directives) " in *" $h:"*) ;;
      *) fail 39 "--waive names a handle that is not in the effective directive set, and a waiver on a directive nobody declared relaxes nothing: $h"; return 1;; esac
    if [ -z "$r" ]; then
      fail 40 "--waive requires --reason, because a waiver with no recorded reason is indistinguishable from one nobody meant and the wrap-up has nothing to surface"
      return 1
    fi
    # park() writes the reason VERBATIM and the leg greps this file whole, so a truthful reason
    # naming the bypass flag would red the bar permanently on a record no verb rewrites. A newline
    # is refused in the same branch because park()'s grammar is one line per entry: a reason
    # carrying one forges a second, well-formed entry the owner never granted.
    # GUARDED on non-empty. An empty BYPASS_BAN makes this glob `*""*`, which matches every
    # string — so an undeclared bypass flag would refuse every waiver ever offered.
    case "${BYPASS_BAN:+x}$r" in "") ;; *"$BYPASS_BAN"*)
      fail 41 "a waiver reason may not spell the declared bypass flag or contain a newline; park writes it verbatim into a line-oriented region that the leg greps whole, so either one corrupts a record no verb rewrites"
      return 1 ;;
    esac
    if [ "$(printf '%s' "$r" | wc -l | tr -d ' ')" != "0" ]; then
      fail 41 "a waiver reason may not spell the declared bypass flag or contain a newline; park writes it verbatim into a line-oriented region that the leg greps whole, so either one corrupts a record no verb rewrites"
      return 1
    fi
    i=$((i + 1))
  done
  # Refusal 2, and it runs ONLY when the invocation carries a pair. An invocation naming no handle
  # leaves the recorded set untouched and is not a refusal - which is what keeps the --preflight that
  # unit 5's design requires before every --close legal over a run that waived something.
  if [ -f "$rel" ]; then
    want=$(printf '%s\n' "${WAIVE_ITEMS[@]}" | sort -u)
    have=$(recorded_waivers "$rel")
    # The `[ -n "$have" ]` half is GONE, and unit 13's cross-component arm is what found it.
    # With it, a record created by a waiver-free preflight had an EMPTY recorded set, so a
    # SECOND preflight could add waivers to it - a second owner turn, which is the one thing
    # this ordering exists to prevent. Leg check 17 then refused the resulting record forever,
    # because the line is absent from the file's first committed blob. Driver and leg
    # disagreed, and the driver was wrong.
    #
    # The first preflight is unaffected: it runs BEFORE scaffold_runmd, so the file does not
    # exist yet and this block is skipped entirely.
    if [ "$want" != "$have" ]; then
      fail 38 "the requested waiver set differs from the one already recorded, and a re-preflight is a RESUME rather than a second owner turn; re-issue the recorded set or none at all"
      return 1
    fi
  fi
  return 0
}

check_single_live() {
  local n=0 f p live=""
  # BOTH globs: the live record AND every archived one. Rotation puts finished records beside the
  # live one, and a rule that quantified over `RUN.md` alone would let an archive hand-edited back to
  # a non-terminal phase sit there as an unseen second run — which is exactly what this check exists
  # to make impossible.
  for f in $(GIT ls-files "$M/builds/*/RUN.md" "$M/builds/*/RUN.*.md" 2>/dev/null); do
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
  local slug="$1" base="$2" rel blob fmslug _fm
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
  # TOOL-aPromptedMandate-1 - ONE read, TWO answers. The program this replaces printed the slug and
  # EXITED on its first match, so a second arm below it could never run, and an arm placed above it
  # starved `fmslug` of the value the refusal below compares - tripping the slug mismatch instead.
  # Both keys are emitted KEY-TAGGED and nothing exits on a match; the front-matter close still
  # terminates the scan, which is what bounds it. No second `GIT show`: one blob, one parse.
  _fm=$(printf '%s\n' "$blob" | awk '
    NR == 1 { next }
    /^---[[:space:]]*\r?$/ { exit }
    /^slug:/ { v = $0; sub(/^slug:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print "slug=" v; next }
    /^authorized-by:/ { v = $0; sub(/^authorized-by:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print "mode=" v; next }')
  fmslug=$(printf '%s\n' "$_fm" | sed -n 's/^slug=//p' | head -1)
  AUTH_MODE=$(printf '%s\n' "$_fm" | sed -n 's/^mode=//p' | head -1)
  # ABSENT is `slug` - every build README in every adopter's tree today declares nothing, and that
  # is the ordinary case, not a defect. A value OUTSIDE the closed set is a refusal rather than a
  # default: defaulting an unrecognised mode to either member lets a typo select a discipline
  # nobody declared, which is the failure shape ANCHOR_SCOPE's own value guard exists to avoid.
  [ -n "$AUTH_MODE" ] || AUTH_MODE=slug
  case "$AUTH_MODE" in
    prompt|slug) ;;
    *) fail 44 "the build README at the pinned BASE declares an authorization mode outside the closed set of prompt and slug, and defaulting an unrecognised mode would select a discipline nobody declared: $AUTH_MODE"
       return 1 ;;
  esac
  if [ "$fmslug" != "$slug" ]; then
    fail 20 "the build README at the pinned BASE declares a different slug, so the folder was renamed or its README copied from another build and the authorization does not name this one: declared $fmslug, requested $slug"
    return 1
  fi
  # TOOL-aBoundedVerdict-11 S6/S6a/S6b - the frozen scope is the GENERATED units region's unit-ID SET,
  # compared BASE -> HEAD and required to be a SUBSET. Additions admitted, removals refused. This
  # REPLACES the authored roster pair's byte comparison, which S8 retires by deleting this reader; the
  # four build READMEs that carry such a pair keep their bytes, because a region nothing reads is inert.
  #
  # WHY IDS AND NOT BYTES. A row carries the unit's status, rev and last-change date, all rendered from
  # its spec header, so they move whenever a unit is built. A byte-level "no row changed" test would
  # refuse every run that BUILT anything, on the one item `verb_close` will not override - strictly
  # worse than the opt-in hole it replaces. The id set IS the scope: which units the run may work on is
  # frozen, and everything else in a row is derived from a document the run is authorized to edit. A
  # RENAMED id is still refused, because renaming removes a BASE id.
  #
  # WHY A CUTOFF (S6a). A run's BASE is pinned BEFORE its own work, so the BASE of the run that lands
  # the migration render cannot carry the region this check wants. Without the cutoff the unit is
  # unlandable by ANY run - measured on the run that built it, the BASE blob carried no pair at all -
  # so a BASE committed before UNITS_REGION_CUTOFF keeps presence-based opt-in.
  #
  # WHAT THIS BUYS, SCOPED (S6b). On the DEFAULT-BRANCH anchor the BASE blob is outside the run's reach
  # and this is a real integrity check. On the BRANCH anchor it is NOT - the run pushed that tip - and
  # `.unattended.conf`'s own comment plus the protocol's section 1 already say roster integrity stops
  # being enforceable there. This check does not close that hole and must not read as though it did.
  #
  # PRESENCE is decided by grepping for the open marker, NOT by `region`'s exit status. `region` exits 3
  # for "absent" AND for "malformed or duplicated", and treating that one status as "absent" is how a
  # second block once went uncompared - the discarded-signal defect this kit has already paid for.
  if printf '%s\n' "$blob" | grep -qF -- "$UNITS_OPEN"; then
    local ub uh miss
    if ! ub=$(printf '%s\n' "$blob" | region - "$UNITS_OPEN" "$UNITS_CLOSE" 2>/dev/null); then
      fail 20 "the build README at the pinned BASE carries a units marker but not exactly one well-formed pair, so there is no single scope to compare against: $base:$rel"
      return 1
    fi
    if ! uh=$(region "$rel" "$UNITS_OPEN" "$UNITS_CLOSE" 2>/dev/null); then
      fail 20 "the working copy's build README does not carry exactly one well-formed units pair while the pinned BASE does, so the scope this run is executing against cannot be compared: $rel"
      return 1
    fi
    miss=$(comm -23 <(printf '%s\n' "$ub" | _ids_of) <(printf '%s\n' "$uh" | _ids_of) | tr '\n' ' ' | sed 's/[[:space:]]*$//')
    if [ -n "$miss" ]; then
      fail 20 "a unit in the scope at the pinned BASE is absent from it now, so this run narrowed or renamed the scope it was authorized for; additions are admitted and removals are not: $miss"
      return 1
    fi
  elif [ -n "${UNITS_REGION_CUTOFF:-}" ]; then
    local bdate
    bdate=$(GIT show -s --format=%cs "$base" 2>/dev/null)
    # `sort -C` exits 0 when its input is ALREADY SORTED, so cutoff-then-bdate sorted means
    # bdate >= cutoff — exactly the refusal condition. The first cut NEGATED this and therefore
    # refused every BASE before the cutoff while admitting every one after: the precise inversion
    # the cutoff exists to prevent, and it would have refused the run that built this unit.
    if [ -n "$bdate" ] && printf '%s\n%s\n' "$UNITS_REGION_CUTOFF" "$bdate" | sort -C; then
      fail 20 "the build README at the pinned BASE carries no units marker pair and this BASE is dated at or after UNITS_REGION_CUTOFF, so an empty set would satisfy the subset test vacuously: $base:$rel · repair: the --write mode of tools/memory-tree/gen_build_index.py"
      return 1
    fi
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
    printf 'Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED\n'
    printf 'from the build README on every read, so it cannot go stale between them. This file holds\n'
    printf 'only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE\n'
    printf 'with its anchor evidence, and the parked decisions.\n\n'
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

# ONE staging refusal for THREE callers. The terminal producers need exactly the refusal --preflight
# already had, and writing it out at each call site would have made three branches of one rule - three
# ordinals for check-arms to track, three signatures to keep in step, and two more rows for a pin file
# whose whole purpose is to stay short. The rule is one rule, so it gets one branch.
stage_or_fail() { # run-state file
  # BOUND TO A NAME, not used as `$1`. check-arms reads a bare positional as LITERAL text, so it lands
  # inside the branch's signature and no assertion — and no pin — can ever match it. The repo carries
  # this trap in writing and it still cost a cycle here.
  local rel="$1"
  stage_runmd "$rel" && return 0
  fail 9 "cannot stage the run-state file, and the gate leg's whole per-run population is the index, so an unstaged run is invisible to every check it has: $rel"
  return 1
}

# EVERY verb that writes a phase refuses a FINISHED run, and the rule lives in ONE place because the
# first cut of it did not. --phase and --abort each grew their own copy; --close and --preflight grew
# neither, and both write a phase. So `--close` on a LANDED record printed "close OK" and rewrote the
# phase to LANDING, and from that re-opened LANDING `--landed` re-pointed the witness - the one field
# check 15 judges - at a different commit, with the bar green the whole way. `--preflight` preserved
# the terminal phase and rewrote the witness anyway, leaving a LANDED record the leg reds on and no
# verb can repair.
#
# The lesson is the shape, not the two misses: a rule spelled at each call site is a rule that will be
# missing from the next call site. This is the single branch, and the self-test derives the
# phase-writer population from source and drives a terminal record through every one of them.
# WHERE A RETIRED RECORD GOES. DERIVED from the record itself, never chosen: the terminal phase plus
# the first 8 hex of the record's own blob hash. That makes the name TOTAL, which the obvious
# `<witness8>` spelling is not — NO driver verb commits (`grep -c "git commit"` over this file and the
# leg returns 0 for both), so run A aborting at commit W and run B aborting at the same W produce one
# name for two records, and a refusal on collision would then block every later run with no operator
# path out. Two records with the same CONTENT are the same record twice, so overwriting is lossless.
#
# The `<phase>` half cannot carry a path separator: it comes from PHASES_TERMINAL through the same
# `is_terminal` test that decides whether to rotate at all. The witness could — nothing constrains a
# non-LANDED witness to a sha — which is a second reason the name does not use it.
#
# Stable across the fleet: .gitattributes pins `memory/**/*.md text eol=lf`, which covers RUN.*.md,
# and `git hash-object` applies the path's clean filter, so this is the INDEX blob on every platform.
archive_name_of() { # run-state file -> its immutable archive path
  local rel="$1" ph blob
  ph=$(fact "$rel" phase)
  blob=$(GIT hash-object "$rel" 2>/dev/null) || return 1
  [ -n "$ph" ] && [ -n "$blob" ] || return 1
  printf '%s/RUN.%s.%.8s.md' "${rel%/RUN.md}" "$ph" "$blob"
}

refuse_if_terminal() { # run-state file · verb
  local rel="$1" verb="$2" cur
  [ -f "$rel" ] || return 0
  cur=$(fact "$rel" phase)
  [ -n "$cur" ] && is_terminal "$cur" || return 0
  fail 26 "the run is already finished and a finished record is not something to move, re-open or re-pin; every later run is measured against the counter this record left, and the verb that would rewrite it names itself here: $cur via $verb"
  return 1
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

# TOOL-cBriefedPilot-6 - the roster join. M2 makes the README's authored Units table the roster and
# this verb did not parse it, so it enumerated the half of the roster that already had specs and said
# so in its own output. These read that table.
#
# The ids are matched against the build's OWN slug. A looser pattern would mint units out of prose:
# a roster row citing a sibling build's id names a DEPENDENCY, not a unit of this build.
# TOOL-aBoundedVerdict-11 S8, CORRECTED mid-build. This reads the AUTHORED pair, deliberately: it is
# the only carrier of a unit that is PLANNED and has no spec yet. Pointing it at the generated region
# made `missing_units` a TAUTOLOGY - that region is rendered FROM the specs that exist, so roster_ids
# became a subset of spec_ids by construction and the difference was empty always. Same class as
# memory/gotchas/assertion-between-two-derived-values.md, and the M6 checklist named that class for
# the very diff that introduced it.
#
# The two questions are SPLIT rather than merged. Authorization, the presence term and terminality read
# the GENERATED region, which is what makes them satisfiable without a hand-edit. The
# planned-but-unspecced question keeps the authored pair: absent, `missing_units` is trivially
# satisfied, which is the status quo for 45 of 49 builds and weakens nothing that worked before.
roster_ids() { # slug -> ids the AUTHORED plan names, which may include unspecced units
  local slug="$1" rel; rel=$(readme_of "$slug")
  [ -f "$rel" ] || return 0
  grep -qF -- "$ROSTER_OPEN" "$rel" || return 0
  region "$rel" "$ROSTER_OPEN" "$ROSTER_CLOSE" 2>/dev/null \
    | grep -oE "[A-Z]+-$slug-[0-9]+" | sort -u
}
# The GENERATED region's ids - what a build's units actually ARE. `build-complete`'s non-empty term
# uses this rather than the authored plan, so the term is meetable on a build nobody hand-wrapped.
unit_ids_of() { # slug
  local slug="$1" rel; rel=$(readme_of "$slug")
  [ -f "$rel" ] || return 0
  region "$rel" "$UNITS_OPEN" "$UNITS_CLOSE" 2>/dev/null \
    | grep -oE "[A-Z]+-$slug-[0-9]+" | sort -u
}
# The ids verb_plan already derives, lifted so the listing and the join cannot disagree about what a
# unit's id IS. A spec whose heading and status header disagree is then invisible to both halves in
# the same way, rather than counted present by one and absent by the other.
spec_ids() { # dir
  local dir="$1" spec
  for spec in $(git ls-files "$dir/spec/*.md" 2>/dev/null); do
    awk '{ sub(/\r$/,"") } /^\*\*Status:\*\* [A-Z]+ /{ hdr=1 } /^# [A-Za-z0-9][A-Za-z0-9-]* /{ if (id=="") id=$2 } END { if (hdr && id != "") print id }' "$spec"
  done | sort -u
}
missing_units() { # slug · dir
  local want have; want=$(roster_ids "$1"); have=$(spec_ids "$2")
  [ -n "$want" ] || return 0
  comm -23 <(printf '%s\n' "$want") <(printf '%s\n' "$have")
}
# S6 - extracted out of verb_status's inline pipeline, ahead of the unit that consumes it. Unit 7's
# build-complete asks the same two questions, and a second copy would be two answers to one question
# in the two verbs that report on the same region.
# Reads the BUILD README's pair — the one home of the unit list since main's redesign removed the
# run-state copy and required that region to be EMPTY. Pointing these at the emptied region made
# `build-complete` unsatisfiable: a check that cannot PASS, caught by its own green control.
# TOOL-aBoundedVerdict-11 S2/S3. Returns rows on stdout and NOTHING else, because callers capture it
# in a command substitution and test it for emptiness - a diagnostic printed here would be captured
# as a row. So absence-or-malformation is an EXIT STATUS (3, the same one `region` uses) and the
# message is the caller's to print; `units_refusal` is the one place that message is spelled.
#
# TWO independent guards against the record-row defect TOOL-aPromptedMandate-12 measured, because
# they fail differently. The REGION is the nested `gen:build-units` pair, which encloses the units
# table only, so a record row is out of range structurally rather than by filter. The SELECTOR is
# still `](spec/` - the link target, which is what M2 already uses to define a unit's spec - so a
# mis-rendered or hand-widened region cannot smuggle a record row back in. Either alone was enough
# on the day it was written; a false GREEN here passes build-complete over an unfinished unit, and
# that is worth paying one grep for.
#
# `.*` and NOT `[^]]*`: a negated class stops at the first `]`, so a unit whose title contains one
# would be DROPPED - and a dropped unit row is a false GREEN, because nonterminal_units cannot see
# it. Greedy `.*` takes the last `](spec/` on the line.
unit_rows() { # build README -> unit rows; rc 3 = no single well-formed pair
  local out
  out=$(region "$1" "$UNITS_OPEN" "$UNITS_CLOSE" 2>/dev/null) || return 3
  printf '%s\n' "$out" | grep -E '^\| \[.*\]\(spec/'
}
nonterminal_units() { unit_rows "$1" | grep -vE '\| (CLOSED|WONTDO) \|'; }
# TOOL-aBoundedVerdict-11 S6 - ids out of whatever row text it is handed, sorted and deduplicated so
# two callers cannot disagree about order. Reads stdin, so it composes with either side of the compare.
_ids_of() { grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u; }
# S3 - a malformed or absent pair is a NAMED refusal rather than a silent empty selection. `region`
# exits 3 for ABSENT and for MALFORMED alike and this kit has already paid once for reading that one
# status as "absent", so the message names both possibilities and the repair.
units_refusal() { # build README path
  # The remedy names the SCRIPT and its flag, never a launcher. Spelling a bare launcher here
  # tripped the driver's own resolver ban, and the ban is right about more than form: a bare
  # launcher is what this repo cannot assume exists, so telling an operator to type one is the
  # defect the ban exists to stop. Same shape as absence-assertion-over-whole-file-text: the
  # check cannot tell an invocation from a sentence about one, and need not when the sentence
  # is right anyway.
  printf 'the build README carries no single well-formed %s pair, so the unit list cannot be read (absent, duplicated or transposed): %s\n  repair: the --write mode of tools/memory-tree/gen_build_index.py\n' "$UNITS_OPEN" "$1"
}

verb_plan() { # slug
  local slug="$1" dir specs spec id st state next="" miss nmiss=0
  check_slug "$slug" || return 1
  dir="$M/builds/$slug"
  # A malformed pair is a NAMED refusal, never a silent fall-through to the no-roster path. `region`
  # exits 3 for ABSENT and for MALFORMED alike, and treating that one status as "absent" is the
  # discarded-signal defect this kit has already paid for once - a build whose markers are duplicated
  # or transposed would otherwise get the complete-looking list this unit exists to stop printing.
  # The path is bound to a NAME. check-arms reads the literal text up to the first interpolation as
  # the branch's signature, and a $( ) inside the message lands IN that signature - so no arm can
  # ever match it. Same class as the positional trap this repo already documents.
  local _rmp; _rmp=$(readme_of "$slug")
  if grep -qF -- "$UNITS_OPEN" "$_rmp" 2>/dev/null; then
    if ! region "$_rmp" "$UNITS_OPEN" "$UNITS_CLOSE" >/dev/null 2>&1; then
      fail 42 "the build README carries a units marker but not exactly one well-formed pair, so the roster this verb would join against is not a single slice: $_rmp"
      return 1
    fi
  fi
  specs=$(git ls-files "$dir/spec/*.md" 2>/dev/null)
  if [ -z "$specs" ]; then
    fail 19 "no tracked spec under this build, so every planned unit is MISSING; the README roster is what this verb reads to say WHICH, and with no spec beside it there is nothing to join that roster against: $dir/spec"
    return 1
  fi
  for spec in $specs; do
    # ONE awk, not three chained processes. Same semantics: first matching line wins, a trailing CR
    # is stripped, and nothing is printed when the file carries no status header.
    st=$(awk '{ sub(/\r$/,"") } /^\*\*Status:\*\* [A-Z]+ / { print $2; exit }' "$spec")
    # NO status header, NO unit. M2 defines a unit's spec as the file whose STATUS HEADER carries the
    # id, so a file without one is a recording that happens to live here. Taking it anyway made this
    # verb invent units and name one as `next` on 5 of the 25 builds in this corpus.
    if [ -z "$st" ]; then
      printf '%-34s %-11s %s\n' "$(basename "$spec")" "-" "NOT A UNIT (no status header)"
      continue
    fi
    id=$(awk '{ sub(/\r$/,"") } /^# [A-Za-z0-9][A-Za-z0-9-]* / { print $2; exit }' "$spec")
    # NO basename fallback. `spec_ids` prints only when BOTH the status header and the id parse, so a
    # fallback here made the two halves disagree about an unparseable heading: the file listed under
    # its basename with a real status, and the SAME unit counted absent by `missing_units` — printed
    # twice, once as a phantom MISSING that sends an unattended agent to re-spec a specced unit.
    # Zero divergent files across all tracked specs today; this keeps both halves blind alike.
    if [ -z "$id" ]; then
      printf '%-34s %-11s %s\n' "$(basename "$spec")" "$st" "NOT A UNIT (heading id does not parse)"
      continue
    fi
    state=$(plan_state "$spec")
    case "$st" in CLOSED|WONTDO) state="DONE" ;; esac
    printf '%-34s %-11s %s\n' "$id" "${st:-?}" "$state"
    case "$state" in
      THIN|FORKED) [ -n "$next" ] || next="$id ($state)" ;;
      READY)       [ -n "$next" ] || next="$id (READY - build it)" ;;
    esac
  done
  # The planned units nobody has specced. These are what M2 calls MISSING, and until this
  # unit they were simply absent from the listing rather than reported.
  for miss in $(missing_units "$slug" "$dir"); do
    printf '%-34s %-11s %s
' "$miss" "-" "MISSING"
    nmiss=$((nmiss + 1))
    [ -n "$next" ] || next="$miss (MISSING - spec it first)"
  done
  if [ -n "$(roster_ids "$slug")" ]; then
    echo "roster: the README roster region, $(roster_ids "$slug" | grep -c .) id(s); $nmiss with no tracked spec"
  else
    echo "roster: tracked specs under $dir/spec (a planned unit with no spec is invisible here)"
  fi
  if [ -n "$next" ]; then echo "next: $next"; else echo "next: none - every tracked spec is terminal"; fi
  return 0
}

verb_phase() { # slug · phase · witness
  local slug="$1" want="$2" wit="$3" rel cur
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to move: $rel"; return 1; }
  case " $(phases) " in
    *" $want "*) ;;
    *) fail 19 "the phase is not in the declared vocabulary, and a phase nothing recognises is not a position: $want" ; return 1 ;;
  esac
  # A run that is already FINISHED cannot be moved at all. This is the third of the three fixes the
  # aStandingWrit review's F2 asked for, and the only one that was never built - because before the
  # terminal producers below existed, no record could BE terminal and the branch was unreachable.
  # Adding the producers is what makes it reachable, so it lands with them: without it,
  # `--phase <slug> BUILDING` on a LANDED record returns the run to check_single_live and leg check 7,
  # which is the counter this whole unit exists to free.
  refuse_if_terminal "$rel" --phase || return 1
  # A TERMINAL phase is a PRODUCER's to write, never this verb's. Vocabulary membership is not
  # permission: a run that could set LANDED here would skip the entire Definition-of-Done gate, and
  # the two agent-attested items are enforced in no other place.
  #
  # THE MESSAGE USED TO NAME `--close`, AND THAT WAS FALSE. --close writes LANDING, never LANDED, so
  # the sentence sent the reader to a verb that could not do what it claimed - and for the whole life
  # of that message no verb could, which is the defect this unit fixes.
  if is_terminal "$want"; then
    fail 19 "a terminal phase is written by --landed or --abort, which evaluate what it claims, and not by this verb, because reaching it through here would skip the whole Definition-of-Done gate: $want"
    return 1
  fi
  # S9 - LANDING IS CLOSE-ONLY, and without this branch S1's whole precondition is decoration.
  # LANDING is an ordinary non-terminal member of the vocabulary, so `--phase <slug> LANDING` wrote it
  # and `--landed` - which accepts a record AT LANDING - would then reach LANDED with dod_met never
  # invoked. That is the exact hole the terminal refusal above was added to close, reachable in one
  # command. Making --close the only writer of LANDING is what turns "the record is at LANDING" into
  # "the Definition of Done was evaluated".
  if [ "$want" = LANDING ]; then
    fail 15 "LANDING is written by --close alone, because it is the record that the Definition-of-Done set was evaluated; a phase move into it would be that claim without the evaluation: $want"
    return 1
  fi
  [ -n "$wit" ] || { fail 11 "a phase claim carries a WITNESS - a sha, a tag or a run id - and presence is its own refusal because an unwitnessed claim is the one an oracle skips: $want"; return 1; }
  set_fact "$rel" phase "$want" || return 1
  # TOOL-aBoundedVerdict-15 S1 - the SECOND omission, and the reason rev-1's "the only phase writer
  # that does not stage" was wrong. Three of five staged; this and --close were the two that did not.
  stage_or_fail "$rel" || return 1
  set_fact "$rel" witness "$wit" || return 1
  echo "unattended: phase $want · witness $wit"
  return 0
}


# S1 - THE SOLE PRODUCER OF `LANDED`, and it is an OBSERVATION rather than a claim.
#
# Two preconditions, and both are load-bearing:
#
#   * the record must be AT LANDING, which (with the S9 refusal in verb_phase) means --close ran and
#     every declared Definition-of-Done item was met or explicitly overridden. Without S9 this
#     precondition is satisfiable by one --phase call and buys nothing.
#   * HEAD must be an ancestor of the tip the REMOTE advertises for its own HEAD. That is the
#     machine-checkable form of "this work is on the branch the remote calls its default". It is not
#     proof against a run that seeded its own endpoint - section 9 of the protocol enumerates that -
#     and this verb claims nothing further.
#
# IT DOES NOT CALL check_branch, deliberately. Landing happens ON the default branch, because the
# mandated lander refuses to run anywhere else, so the guard that refuses the default branch would
# refuse every correct invocation of this verb. The omission is the point and AC13 stands on the
# default branch explicitly, because a feature-branch fixture cannot tell a guard that was removed
# from a guard that was never called.
#
# The anchor observation is FATAL and its message is NOT suppressed. --close suppresses it and
# reports only the downstream unmet item, which is the message-channel scar this kit already carries;
# this verb does not repeat it.
verb_landed() { # slug
  local slug="$1" rel cur head lbranch unp oldest akind rbref rbtip
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to mark landed: $rel"; return 1; }
  refuse_if_terminal "$rel" --landed || return 1
  cur=$(fact "$rel" phase)
  if [ "$cur" != LANDING ]; then
    fail 31 "a run reaches LANDED only from LANDING, because LANDING is the record that --close evaluated the Definition-of-Done set and this verb does not evaluate it a second time: $cur"
    return 1
  fi
  check_clean || return 1
  # OBSERVE_ANCHOR STAYS MANDATORY ON BOTH ARMS. It is what supplies AREF - the local arm needs the
  # default branch's NAME and takes it from the remote's own advertisement, never from a local ref or
  # from the environment, both of which this kit records as a reproduced bypass. Its checks 22 through
  # 30 are integrity tripwires a local landing needs at least as much as a remote one, and a run that
  # cannot see the remote it means to land on should abort rather than land against a branch name it
  # chose for itself.
  observe_anchor || return 1
  head=$(GIT rev-parse HEAD)
  lbranch=${AREF#refs/heads/}
  # UNPUSHED WORK, counted on BOTH arms. Local main is shared by every build on the node, and this
  # repo records a run whose primary tree was clean and on main while carrying eleven unpushed
  # commits, three of them another build's unreviewed work. A local landing claim sits on top of
  # whatever else is there, and a record that does not say how much else is there is not readable.
  # REPORTED, never refused: making one build's mid-flight work block another build's terminal is the
  # deadlock shape this whole unit exists to remove.
  if GIT rev-parse --verify --quiet "refs/heads/$lbranch" >/dev/null 2>&1; then
    unp=$(GIT rev-list --count "$ASHA..refs/heads/$lbranch" 2>/dev/null || echo 0)
    if [ "${unp:-0}" != 0 ]; then
      oldest=$(GIT rev-list "$ASHA..refs/heads/$lbranch" 2>/dev/null | tail -1)
      unp="$unp oldest $(GIT rev-parse --short=8 "$oldest" 2>/dev/null)"
    fi
  else
    # `unknown` and never `0`. A zero that means "could not measure" is this repo's named
    # green-by-absence class, and it would read as "nothing unpushed" to every later reader.
    unp="unknown"
  fi
  akind=""
  if GIT merge-base --is-ancestor "$head" "$ASHA" 2>/dev/null; then
    akind=remote
  else
    # THE SECOND ARM NAMES AN EXPLICIT REF, and that is the whole of its correctness. Testing HEAD
    # against the local default branch is decided before it reads anything on the only path this verb
    # is invoked: the mandated lander refuses to run anywhere but the default branch, and there HEAD
    # IS that ref, so a commit would be compared with itself. The run's OWN BRANCH TIP is false when
    # nothing was merged and true when it was, which is the question the arm exists to ask.
    rbref=$(fact "$rel" branch-ref)
    if [ -z "$rbref" ]; then
      # NO LOCAL ARM IS AVAILABLE, which is a different state from one that was tried and failed.
      # `branch-ref` is written only where the project's anchor scope makes the run's own branch
      # meaningful, so a record without it has exactly one anchor and the refusal says so rather than
      # implying a fallback the run never had.
      fail 32 "HEAD is not an ancestor of the tip the remote advertises, and this run-state file names no branch ref, so there is no local arm to fall back to and the work this run means to mark landed is not on the branch the remote calls its default; land it first, then mark it: $head against $AREF at $ASHA"
      return 1
    fi
    rbtip=$(GIT rev-parse --verify --quiet "$rbref" 2>/dev/null)
    if [ -z "$rbtip" ]; then
      fail 32 "the run's own branch ref does not resolve in this clone, so whether its work reached the local default branch cannot be judged: $rbref in $rel"
      return 1
    fi
    if GIT merge-base --is-ancestor "$rbtip" "refs/heads/$lbranch" 2>/dev/null; then
      akind=local
    else
      fail 32 "this run is on neither anchor: its HEAD is not an ancestor of the tip the remote advertises, and its own branch tip is not an ancestor of the local default branch either, so the work is not landed anywhere; land it first, then mark it: $head against $AREF at $ASHA, and $rbref at $rbtip against refs/heads/$lbranch"
      return 1
    fi
  fi
  set_fact "$rel" phase LANDED || return 1
  set_fact "$rel" witness "$head" || return 1
  # WRITTEN ON BOTH ARMS AND NEVER DEFAULTED. An absent `landed-anchor` would read as `remote` to any
  # later reader, silently promoting a record to the stronger claim.
  set_fact "$rel" landed-anchor "$akind" || return 1
  set_fact "$rel" unpushed-at-landing "$unp" || return 1
  # THE ROSTER AT LANDING, frozen here and nowhere else. Deriving the unit list from the build README
  # is right while a run is LIVE — it cannot go stale between reads — but a FINISHED record must
  # still answer "which units did this run actually cover", and the README is mutable: a later build
  # adding a unit would retroactively change what this landed run appears to have carried. Freezing
  # the ids at the moment of landing is what keeps a terminal record a record. It is written as an
  # authored FACT because nothing else in the tree holds it once the README moves on.
  # TOOL-aPromptedMandate-12 fold - through `unit_rows`, which is the THIRD reader of this region's
  # row grammar and the one the narrowing missed. Left open-coded it kept the broad `^| [`, so this
  # verb froze RECORD rows into `units-at-landing` - a terminal, permanent fact validated by nothing,
  # and the freeze is the whole reason the field exists. The second closing review reproduced it at
  # 1162 bytes of raw markdown against this build's own README.
  #
  # TOOL-aBoundedVerdict-11 S2 - and the region it reads is now the nested `gen:build-units` pair, so
  # a record filename cannot reach this freeze by row shape either. Both existing frozen facts were
  # measured clean across the change.
  set_fact "$rel" units-at-landing \
    "$(unit_rows "$(readme_of "$slug")" \
       | sed -e 's/^| \[//' -e 's/ —.*//' | tr '\n' ' ' | sed 's/ $//')" || return 1
  stage_or_fail "$rel" || return 1
  if [ "$akind" = remote ]; then
    echo "unattended: phase LANDED · witness $head · anchor remote · observed on $AREF at $ASHA · unpushed on local $lbranch: $unp"
  else
    echo "unattended: phase LANDED · witness $head · anchor LOCAL · $(fact "$rel" branch-ref) is merged into refs/heads/$lbranch, which the remote has not seen · unpushed on local $lbranch: $unp"
  fi
  return 0
}

# S2 - THE SOLE PRODUCER OF `ABORTED`, and deliberately NOT symmetric with --landed.
#
# An aborted run landed nothing, so the four MACHINE-checked Definition-of-Done items assert
# obligations it does not have, and evaluating them would block the exit that exists for a run which
# cannot meet them. Both AGENT-ATTESTED items are still required, and the second one is the half a
# first cut dropped:
#
#   * the keepalive, because the scheduling store is in-memory and session-scoped, so a job left
#     unreaped is orphaned where no later run can see it;
#   * the parked decisions, because an abort is the MAXIMAL case of decisions the owner never saw,
#     and the build method derives the owner's only turn from those entries. The circularity
#     objection - that the wrap-up has not happened yet - is identical at --close, where the same
#     attestation is demanded before the same wrap-up, and it was accepted there.
verb_abort() { # slug · reason
  local slug="$1" reason="$2" rel head item ck key
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to abort: $rel"; return 1; }
  if [ -z "$reason" ]; then
    fail 33 "--abort requires --reason, because an abort with no recorded reason is indistinguishable from a run that simply stopped, and the reason is the only thing the owner gets in place of the turn nobody took"
    return 1
  fi
  # A REASON MAY NOT SPELL THE BYPASS FLAG. park() writes it verbatim into the run-state file, and leg
  # check 11 greps that file WHOLE for the declared flag - so a perfectly truthful abort reason ("the
  # lander refused and I would not use it") would red the bar permanently, on a terminal record no
  # verb can rewrite afterwards. Refusing the spelling is cheaper than mangling the operator's prose,
  # and the message says which word to drop.
  if [ -n "$BYPASS_BAN" ] && printf '%s' "$reason" | grep -qF -- "$BYPASS_BAN"; then
    fail 36 "the reason spells the declared bypass flag, and the gate greps this file whole for it, so recording this sentence would red the bar on a terminal record nothing can rewrite; say it without the literal flag: $BYPASS_BAN"
    return 1
  fi
  refuse_if_terminal "$rel" --abort || return 1
  # BOTH agent-attested items, read back from the record exactly as --close reads them. This is an
  # ATTESTATION and not a machine verdict, and the message says so wherever it reports - counting an
  # attestation as a verdict is what makes an override look like a check that failed.
  for item in keepalive-reaped parked-decisions-surfaced; do
    ck=$(checker_of "$item")
    if ! dod_met "$slug" "$rel" "$item" "$ck"; then
      # NAMES THE RECORD KEY, not only the item. `parked-decisions-surfaced` is read from a line
      # spelled `parked-surfaced:`, so a message naming only the item sends the operator to write a
      # key nothing reads - blocking the abort forever, on the exit that exists for a run which
      # cannot proceed. The mapping is the same one dod_met uses, so the two cannot drift apart.
      case "$item" in parked-decisions-surfaced) key=parked-surfaced ;; *) key="$item" ;; esac
      fail 35 "an agent-attested item is unmet and an abort still owes both; the driver can only read back what the agent recorded, so this is an attestation and not a machine verdict. Write the RECORD KEY, which is not always the item name: $item via $key"
      return 1
    fi
  done
  head=$(GIT rev-parse HEAD)
  set_fact "$rel" phase ABORTED || return 1
  set_fact "$rel" witness "$head" || return 1
  park "$rel" abort "$slug" "$reason"
  stage_or_fail "$rel" || return 1
  echo "unattended: phase ABORTED · witness $head · reason recorded as a parked entry"
  return 0
}

verb_preflight() { # slug · keepalive-id
  local slug="$1" kid="$2" rel base src payload tmp arch="" rotate=0
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  # ROTATION, HALF ONE: the TEST. A terminal record is not a reason to refuse a NEW run — it is a
  # reason to retire the old one. The refusal below is right about the RECORD and was wrong as a
  # policy about the BUILD: this build's first run aborted with three units left and no second run
  # could start. So --preflight, and ONLY --preflight, rotates instead of refusing; every other phase
  # writer still routes through refuse_if_terminal untouched, because only this verb starts something.
  #
  # The TEST runs HERE, with the other preconditions, and the RENAME runs after the write gate. That
  # split is the whole correctness of it: the rename is what makes the tree dirty, and `check_clean`
  # fails on any non-zero diff/cached/untracked count — so a rotation placed here would ALWAYS reach
  # the gate, print "the run-state file is unchanged" over a tree where the record had already been
  # renamed away from the path every reader globs, and return 1.
  if [ -f "$rel" ] && is_terminal "$(fact "$rel" phase)"; then
    arch=$(archive_name_of "$rel") || { fail 27 "cannot derive an archive name for the finished record, so there is nothing safe to retire it to and the run does not start: $rel"; return 1; }
    # TWO refusals, both BEFORE the write gate, because everything `GIT mv -f` will not refuse for
    # itself has to be refused here.
    #
    # The non-file case is not paranoia: MEASURED, `git mv -f RUN.md <dir>` exits 0 and moves the
    # record INSIDE the directory, so the retired file ends up at `<dir>/RUN.md` — off the path every
    # reader globs, with the verb reporting success. Letting git decide would have made a silent
    # misfiling the happy path.
    if [ -e "$arch" ] && [ ! -f "$arch" ]; then
      fail 28 "the name this record derives is occupied by something that is not a regular file, and a rename onto it would file the finished record somewhere no reader looks rather than fail: $rel -> $arch"
      return 1
    fi
    if [ -f "$arch" ] && ! cmp -s "$rel" "$arch"; then
      fail 28 "an archive already exists at the name this record derives, carrying DIFFERENT bytes — that cannot happen by rotation, so something placed it by hand and overwriting it would destroy a finished record: $rel -> $arch"
      return 1
    fi
    rotate=1
  else
    refuse_if_terminal "$rel" --preflight || return 1
  fi
  [ -n "$kid" ] || fail 8 "no --keepalive-id was supplied — scheduling is the AGENT's half of the split and only the agent can do it; the driver records the id it is handed"
  # The anchor is observed BEFORE anything that consumes it, and its refusals do not cascade: a
  # failed observation leaves ASHA empty and the base block below is skipped entirely, so the
  # operator reads why the observation failed rather than a second, unrelated merge-base complaint.
  observe_anchor || true
  check_clean || true
  check_branch || true
  check_wiring || true
  check_method || true
  check_waivers "$rel" || true
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
  # TOOL-aBoundedVerdict-11 S4 - the WORKING COPY's units region must be readable, and this is where
  # an agent meets the requirement rather than discovering it at --close. The region is what every
  # later verb reads for the unit list: --plan's roster join, --status's next unit, --landed's freeze
  # and build-complete's terms. Refusing here costs one render; refusing at close costs a whole run.
  #
  # It reports through `status` rather than returning, so this refusal joins the others in one pass and
  # the operator sees every unmet precondition at once instead of one per invocation.
  # The test is on the REGION, not on `unit_rows`. `unit_rows` pipes through grep, so it returns 1 when
  # the pair is WELL-FORMED BUT EMPTY - which is every build that has no specs yet, i.e. every brand
  # new one. Refusing on any non-zero status therefore refused the ordinary case; only "no single
  # well-formed pair" is a refusal, and that is what `region` alone reports.
  if ! region "$(readme_of "$slug")" "$UNITS_OPEN" "$UNITS_CLOSE" >/dev/null 2>&1; then
    fail 46 "the build README's unit list cannot be read, so every verb keyed on it would run blind"
    units_refusal "$(readme_of "$slug")"
    status=1
  fi

  # TOOL-aPromptedMandate-4, S5 - the waiver SCOPE, and it CANNOT live in check_waivers: that runs
  # before the authorization block above, where AUTH_MODE is unset for BOTH modes, so a refusal keyed
  # there never fires for one spelling and always fires for the other. Placed here, after the read
  # that produces the mode, for the same reason the anchor is observed before anything consuming it.
  #
  # Keyed on "the mode is not PROMPT" rather than on "the mode is slug": an UNDERIVABLE mode must
  # refuse a scoped waiver rather than grant it, and those two spellings differ exactly when the
  # authorization read failed - which is the moment a silent grant would matter most.
  check_waiver_scope || true
  # NOTHING is written until every precondition above has passed. A verb that writes and then
  # discovers a refusal has already changed the state the refusal was about.
  [ "$status" = 0 ] || { echo "unattended: --preflight refused; the run-state file is unchanged"; return 1; }

  # ROTATION, HALF TWO: the RENAME, in scaffold_runmd's position and for scaffold_runmd's reason —
  # nothing is written until every precondition above has passed.
  #
  # `-f` is what the TEST above buys. A byte-DIFFERING destination already refused over an untouched
  # tree, so the only destination reachable here is absent or byte-identical, and forcing over
  # identical bytes writes the bytes that were already there. Plain `GIT mv` cannot do it: MEASURED
  # rc=128, `destination exists`, with the destination tracked and with it merely present. What
  # actually reaches the identical case is a hand-placed copy — after a completed rotation RUN.md is
  # the fresh RUNNING record, so refuse_if_terminal returns 0 and rotation is never re-attempted.
  #
  # `GIT mv` and not `mv`: BOTH sides have to enter the index in one operation, because the gate leg's
  # whole per-run population is `git ls-files` and an unstaged archive is invisible to every check the
  # widened population gave it.
  if [ "$rotate" = 1 ]; then
    if ! GIT mv -f -- "$rel" "$arch" >/dev/null 2>&1; then
      fail 29 "cannot retire the finished record, and a half-rotated build is worse than an unrotated one — the run does not start and nothing was moved: $rel -> $arch"
      return 1
    fi
    echo "unattended: retired the finished record — $rel -> $arch"
  fi

  # The unit list is DERIVED at read time, never copied here. A copy has to be refreshed by
  # something, and the only writer was this verb — which refuses once a run is live. So an ordinary
  # pass (a spec rev bump moves the build index) left the copy stale with no reachable way to repair
  # it, and the refusal named a remedy that did not exist. Deriving removes the class rather than
  # adding a verb to service it. Both markers are still VALIDATED, because a malformed pair is
  # something to refuse rather than to guess around.
  #
  # TOOL-aPromptedMandate-6 fold, review M1 - the README's pair is validated BEFORE the scaffold, not
  # after it. The comment below has always said the run-state file is created after EVERY precondition
  # passed, and this one ran later, so a malformed README left an orphan untracked RUN.md behind a
  # refusal - and the retry then met the DIRTY-TREE refusal instead, naming a cause that was this
  # verb's own leftover. Observed during this build's first manual reproduction.
  src=$(readme_of "$slug")
  if ! region "$src" "$SRC_OPEN" "$SRC_CLOSE" >/dev/null 2>&1; then
    fail 9 "the build README's generated markers are malformed, and the unit list is DERIVED from there, so an unpaired marker is not something to guess around: $src"
    return 1
  fi

  # The run-state file is created here, AFTER every precondition passed. A verb that scaffolds and
  # then discovers a refusal has already changed the state the refusal was about.
  if [ ! -f "$rel" ]; then
    scaffold_runmd "$slug" || { fail 9 "cannot create the run-state file, so there is nothing for the run to record its phase, witness and parked decisions in: $rel"; return 1; }
  fi
  if ! region "$rel" "$GEN_OPEN" "$GEN_CLOSE" >/dev/null 2>&1; then
    fail 9 "the run-state file's generated markers are malformed — exactly one open and one close, close after open: $rel"
    return 1
  fi
  # The BASE is pinned ONCE, in the same shape as the phase write below (the unit that established
  # this is deliberately NOT named: its spec is non-terminal, and the drift signal for non-terminal
  # specs cited by product source sits at its shrink-only pin, so naming one reds the bar). It
  # used to be rewritten on every preflight, so the verb a run is TOLD to re-run after a compaction
  # silently re-pinned the run against a merge-base that had moved underneath it - and the mandated
  # lander reconciles origin before the gate, so on this fleet it moves on most runs.
  #
  # Protocol section 2 calls the base a runtime observation pinned ONCE at run start. This is the
  # line that makes that sentence true rather than aspirational.
  #
  # The anchor triple is frozen WITH it, resolving the fork this unit parked (owner, 2026-08-16).
  # Protocol section 2 describes all four as observed at PIN TIME, existing so an outside party can
  # re-derive the pin. Left moving, the triple dated a different moment from the value it is evidence
  # for, and evidence for a pinned value that moves is evidence for nothing. Three more conditions of
  # the same shape as the base's, and no new branch.
  [ -n "$(fact "$rel" base)" ] || set_fact "$rel" base "$base" || return 1
  # Re-read, so the echo below reports what is ON the record rather than what was just derived. A
  # second preflight that printed a base it did not write would be the same lie in the operator's
  # face that the unconditional write was on disk.
  base=$(fact "$rel" base)
  [ -n "$(fact "$rel" anchor-ref)" ] || set_fact "$rel" anchor-ref "$AREF" || return 1
  [ -n "$(fact "$rel" anchor-sha)" ] || set_fact "$rel" anchor-sha "$ASHA" || return 1
  [ -n "$(fact "$rel" anchor-url)" ] || set_fact "$rel" anchor-url "$AURL" || return 1
  set_fact "$rel" keepalive "$kid"  || return 1
  # S4: which anchor authorized this run, and — when it was the second one — the observation it
  # rested on. EVIDENCE, exactly like anchor-ref/sha/url: written so a party off this machine can
  # re-derive the pin, and never read back as an input by this kit. `trusted_base` deliberately does
  # NOT branch on anchor-kind (S12), because a verb that did would be taking a security decision from
  # a value its own subject wrote.
  # PINNED ONCE, exactly as `base` is one line up. Written unconditionally these drifted on a
  # re-preflight — the base stayed pinned while the anchor evidence beside it moved to whatever
  # the remote said today, so the record described two different observations as one.
  [ -n "$(fact "$rel" anchor-kind)" ] || set_fact "$rel" anchor-kind "${ANCHOR_KIND:-default-branch}" || return 1
  # TOOL-aPromptedMandate-1 - the authorization mode, PINNED ONCE for the reason anchor-kind is:
  # written unconditionally it would drift on a re-preflight while the base it is evidence for
  # stayed pinned. `slug` is the fallback because an unreachable check_authorization leaves the
  # global empty, and preflight has already refused by then - the default never reaches disk on a
  # run that got here without the read.
  [ -n "$(fact "$rel" mode)" ] || set_fact "$rel" mode "${AUTH_MODE:-slug}" || return 1
  if [ -n "$BREF" ] && [ -z "$(fact "$rel" branch-ref)" ]; then
    set_fact "$rel" branch-ref "$BREF" || return 1
    set_fact "$rel" branch-sha "$BSHA" || return 1
  fi
  # ONLY when the file carries no phase yet. Preflight used to rewrite this unconditionally, so a
  # resumed run that had reached BUILDING was silently moved back to RUNNING by the verb it is told
  # to re-run after a compaction.
  [ -n "$(fact "$rel" phase)" ] || set_fact "$rel" phase RUNNING || return 1
  set_fact "$rel" witness "$(GIT rev-parse HEAD)" || return 1
  # TOOL-cBriefedPilot-3 - AFTER the facts and BEFORE staging. park() appends with >>, which CREATES
  # the file, so calling it before the scaffold guard makes the later splice fail naming the wrong
  # cause; and the gate leg's whole per-run population is the INDEX, so a waiver written after
  # staging would be invisible to every check it has. Skipped when the set is already recorded,
  # which is what makes a re-preflight idempotent rather than duplicating every entry.
  if [ "${#WAIVE_ITEMS[@]}" -gt 0 ] && [ -z "$(recorded_waivers "$rel")" ]; then
    _wi=0
    while [ "$_wi" -lt "${#WAIVE_ITEMS[@]}" ]; do
      park "$rel" waiver "${WAIVE_ITEMS[$_wi]}" "${WAIVE_REASONS[$_wi]}"
      echo "unattended: directive waived — ${WAIVE_ITEMS[$_wi]} (parked with its reason)"
      _wi=$((_wi + 1))
    done
  fi
  stage_or_fail "$rel" || return 1
  # RE-READ, like the base above and for the identical reason. Unit 5 froze the anchor triple, so on
  # a second preflight $AREF/$ASHA hold what was just OBSERVED while the record holds what is pinned.
  # Printing the observation would be the same lie in the operator's face that the unconditional
  # base write was on disk, one field over.
  echo "unattended: preflight OK — base $base · anchor $(fact "$rel" anchor-ref) at $(fact "$rel" anchor-sha) · keepalive $kid · region copied from $src"
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
  local slug="$1" rel p w unit nparked parked
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to report on: $rel"; return 1; }
  p=$(fact "$rel" phase); w=$(fact "$rel" witness)
  [ -n "$p" ] || { fail 10 "the run-state file declares no phase, and a run with no phase is not resumable: $rel"; return 1; }
  # The first non-terminal unit, DERIVED from the build README on every read. It used to be read
  # from a copy inside this file, which is exactly the staleness that design removes — main's
  # redesign, taken here over this branch's terminal-exemption workaround for the same problem.
  # TOOL-aPromptedMandate-12 - through `nonterminal_units`, not a second copy of its pipeline. This
  # line open-coded the identical `region | grep | grep -v | head -1 | sed` and never called either
  # helper, so narrowing `unit_rows` alone would have left --close reading the units table while
  # --status and --resume kept reading the records table - two answers to one question about one
  # region, which is what the extraction exists to prevent. It was already wrong before the narrowing:
  # --status on a landed build offered a `build/` record filename as the next unit, measured on
  # aBranchedMandate by BOTH nodes independently.
  # `](spec/` and not a bare `]`: the selector deliberately admits a unit whose TITLE contains one,
  # so cutting at the first `]` would display a truncated id for exactly the row the narrowing was
  # written to keep. Cut at the link instead, which is the only `](spec/` a unit row carries.
  unit=$(nonterminal_units "$(readme_of "$slug")" | head -1 | sed -e 's/^| \[//' -e 's/\](spec\/.*//')
  [ -n "$unit" ] || unit="(no non-terminal unit)"
  # PARKED COUNT, when there is one. `--park` writes a decision the owner does not hear until the
  # wrap-up; the verb an agent checks itself with should say something is waiting rather than leave
  # it to a file nobody re-opens. Omitted at zero, so the ordinary line does not grow a `· 0`.
  nparked=$(grep -cE '^[0-9][0-9-]*T[0-9:]*Z (decision|abort|override|waiver) · item ' "$rel" 2>/dev/null || true)
  if [ "${nparked:-0}" -gt 0 ] 2>/dev/null; then parked=" · parked $nparked"; else parked=""; fi
  printf 'unattended: %s · phase %s · witness %s · next %s%s
' "$slug" "$p" "${w:-NONE}" "$unit" "$parked"
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
    # carries seven facts and never restates a derivable one (protocol section 2).
    [ -f "$M/guides/BUILD-METHOD.md" ] && echo "unattended: re-read the build method at $M/guides/BUILD-METHOD.md"
    echo "unattended: the directives and their waivers — the table in the unattended Skill; your waivers are parked in this file"
  fi
  return 0
}

# TOOL-cBriefedPilot-1 - EVERY accumulated override is validated, skipped and parked, not just the
# last one. The override pairs arrive in the OV_ITEMS / OV_REASONS globals rather than as positionals,
# because an array cannot be passed as one argument and splitting it back out of a string is the
# delimiter problem the accumulator exists to avoid.
is_overridden() { # item -> 0 when it appears in OV_ITEMS
  local want="$1" j=0 n=${#OV_ITEMS[@]}
  while [ "$j" -lt "$n" ]; do
    [ "${OV_ITEMS[$j]}" = "$want" ] && return 0
    j=$((j + 1))
  done
  return 1
}

verb_close() { # slug   (override pairs arrive in OV_ITEMS / OV_REASONS)
  local slug="$1" rel item ck unmet=0 i=0 n ov reason
  n=${#OV_ITEMS[@]}
  check_slug "$slug" || return 1
  # The SAME observation preflight made, made again here rather than read back from the record the
  # run wrote. Its refusals are not fatal to --close: authorization-reachable simply cannot be met without
  # an anchor, which is the honest outcome and is not overridable.
  # TOOL-aBoundedVerdict-12 S7 - one line BEFORE the network round-trip, so a close that is about to
  # spend one has printed something. Unconditional: a progress line an unattended run cannot observe
  # is not a progress line, and the arm that proves it needs stdout rather than a tty.
  echo "unattended: --close $slug - observing the anchor, then evaluating the Definition of Done"
  # S1 - the redirect is GONE. `fail` echoes to stdout, so `>/dev/null 2>&1` destroyed all EIGHT of
  # observe_anchor's named refusals (checks 22-25 and 27-30), and the only surviving output was the
  # bare `authorization-reachable` line - the one item `fail 21` forbids overriding. A wedge with no
  # stated cause and no forward move. `|| true` alone is the form --landed and --preflight already use:
  # the refusals are not fatal to --close, which is why they were suppressed rather than returned on,
  # and that reasoning was always about the STATUS and never about the message.
  observe_anchor || true
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to close: $rel"; return 1; }
  refuse_if_terminal "$rel" --close || return 1
  # Validate EVERY pair before any of them is acted on. The three messages below are byte-unchanged
  # from the single-override form, so their arms stay valid and no per-check ordinal moves.
  while [ "$i" -lt "$n" ]; do
    ov=${OV_ITEMS[$i]}; reason=${OV_REASONS[$i]}
    case " $(dod) " in *" $ov:"*) ;;
      *) fail 12 "--override names an item that is not in the declared DoD set, and an override on an item nobody declared is not an override: $ov"; return 1;; esac
    [ -n "$reason" ] || { fail 12 "--override requires --reason: an unrecorded override is indistinguishable from a passing check"; return 1; }
    # TOOL-aBoundedVerdict-15 S3 - the FOURTH caller of a guard that existed in triplicate. --abort,
    # --waive and --park all refuse text spelling the declared bypass flag; the override park did not,
    # so a TRUTHFUL reason - one that says why the flag matters - reds leg check 11 permanently on a
    # record no verb can rewrite. Checked HERE, in the loop that validates every pair before any of
    # them is acted on, because a guard that fires after the write has not prevented anything.
    if [ -n "$BYPASS_BAN" ] && printf '%s%s' "$ov" "$reason" | grep -qF -- "$BYPASS_BAN"; then
      fail 12 "an override item or reason spells the declared bypass flag, and the gate greps this file whole for it, so recording this would red the bar on a record no verb can rewrite; say it without the literal flag: $BYPASS_BAN"
      return 1
    fi
    # THE AUTHORIZATION ITEM IS NOT OVERRIDABLE. The protocol says so in one sentence — "There is no
    # override for this one" — and the generic loop happily accepted it, which makes the override on
    # the authorization check the authorization check. Named here so the refusal cites the rule.
    # It fires wherever the item appears in the list, not only first: the loop reaches every pair.
    case "$ov" in
      authorization-reachable)
        fail 21 "the authorization item is NOT overridable; an override on the authorization check IS the authorization check, and the protocol states there is no override for this one"
        return 1 ;;
    esac
    i=$((i + 1))
  done
  for item in $(dod); do
    item=${item%%:*}; ck=$(checker_of "$item")
    is_overridden "$item" && continue
    if ! dod_met "$slug" "$rel" "$item" "$ck"; then
      unmet=$((unmet + 1))
      if [ "$ck" = agent ]; then
        # TOOL-aBoundedVerdict-12 S5 - the RECORD KEY, not only the item. `parked-decisions-surfaced`
        # is read from a line spelled `parked-surfaced:`, so an operator obeying this refusal wrote a
        # key nothing reads and re-ran forever. --abort already carries this mapping and says the key
        # is not always the item name; this is that fix at the call site its author did not grep for.
        local _akey
        case "$item" in parked-decisions-surfaced) _akey=parked-surfaced ;; *) _akey="$item" ;; esac
        fail 13 "an agent-attested DoD item is unmet; the driver can only read back what the agent recorded, so this is an attestation, not a machine verdict: $item"
        printf '    write the RECORD KEY, which is not always the item name: %s: yes
' "$_akey"
      else
        fail 13 "a machine-checked DoD item is unmet, so --close blocks: $item"
        # What the item had to SAY, indented under the refusal that is still the headline. The
        # bar's own output for gates-green; the missing region for build-complete. Empty for an
        # item with nothing to add, so this prints nothing rather than a blank indent block.
        # FILTERED, not dumped. The first cut printed all 95 lines of a 69-leg bar under one refusal,
        # 68 of them "GATE ok" -- which buries the one line the operator needs in the noise the
        # unit exists to remove. Anything that is not an ok/skip line survives, so a FAIL, a
        # summary and any stderr all reach the operator while the roll-call does not.
        [ -n "${DOD_OUT:-}" ] && printf '%s
' "$DOD_OUT" | grep -vE '^(GATE (ok|skip) )' | sed 's/^/    /'
        DOD_OUT=""
      fi
    fi
  done
  [ "$unmet" = 0 ] || return 1
  i=0
  while [ "$i" -lt "$n" ]; do
    ov=${OV_ITEMS[$i]}
    park "$rel" override "$ov" "${OV_REASONS[$i]}"
    echo "unattended: override recorded for '$ov' (checker $(checker_of "$ov")) — parked entry written"
    i=$((i + 1))
  done
  # The phase write is the CLOSE. Reporting success before checking it printed "close OK" over a
  # file still reading RUNNING, which is the two-answers class in the verb whose whole job is to
  # make the record agree with reality.
  set_fact "$rel" phase LANDING || return 1
  # TOOL-aBoundedVerdict-15 S1 - STAGED, like the four other phase writers. The gate leg's entire
  # per-run population is `git ls-files`, which reads the INDEX, so an unstaged LANDING phase is
  # invisible to every leg check; worse, --landed's `check_clean` then refuses because the tree is
  # dirty and the dirt is THIS verb's own write, with a message that blames the operator's tree.
  stage_or_fail "$rel" || return 1
  echo "unattended: close OK — every declared DoD item met; phase LANDING. Land with: $LANDER"
  return 0
}

# What the driver can honestly answer for each core item. Anything it cannot observe is reported as
# agent-attested and read back from the record, never invented.
dod_met() { # slug · run-state file · item · checker
  local slug="$1" rel="$2" item="$3" ck="$4" rb
  case "$item" in
    authorization-reachable)
      # RE-DERIVED, never read out of the run-state file. That file is written by the subject of the
      # test, and an absent `base:` line used to degenerate the comparison to the git index. The
      # ASHA guard is not decoration: with no observation there is no anchor, and an unanchored
      # merge-base is the thing this item exists to refuse.
      # TOOL-aBoundedVerdict-12 S2 - the redirect is GONE here too, and this one was worse than S1's.
      # A redirection on an `&&` list binds only to its LAST simple command, so it silenced
      # check_authorization's six refusals while trusted_base's continued to print. The failure
      # therefore looked INTERMITTENT: whether the operator saw a cause depended on which of two
      # functions refused, and the silenced half was exactly the operator-repairable one.
      #
      # trusted_base's own header records that it was rebuilt to return through a global BECAUSE a
      # captured refusal made --close print only the downstream symptom. The very next call in the
      # chain re-introduced it. That is the whole argument for S6's rule: the fix was made once,
      # correctly, and never became one.
      [ -n "$ASHA" ] && trusted_base "$rel" && check_authorization "$slug" "$TB" ;;
    gates-green)
      # SURFACED, not discarded. `>/dev/null 2>&1` meant a blocked --close reported THAT the bar was
      # red and never WHICH leg, and recovering the name cost a second full bar run every time.
      # Sibling of the seam check_wiring already uses for $WIRING_CHECK -- TOOL-aBranchedMandate-2
      # fixed that call site and did not grep for this one.
      DOD_OUT=""
      [ -n "$GATE_CMD" ] || return 1
      DOD_OUT=$($GATE_CMD 2>&1) && { DOD_OUT=""; return 0; }
      return 1 ;;
    records-current)
      # The unit list is DERIVED from the build README, so "current" is not a comparison between two
      # copies — it is the ABSENCE of a second copy, plus BOTH marker pairs being well-formed. This
      # used to diff the region against that slice, which made an ordinary spec rev bump block the
      # close with no reachable repair.
      #
      # `region`'s EXIT STATUS is checked, not just its stdout. A malformed pair makes it print
      # nothing and exit non-zero, so testing emptiness alone would score a broken marker pair as a
      # SATISFIED DoD item — the item passing loudest exactly when the file is least readable. The
      # leg spells this the same way; the two must not diverge.
      region "$rel" "$GEN_OPEN" "$GEN_CLOSE" >/dev/null 2>&1 \
        && [ -z "$(region "$rel" "$GEN_OPEN" "$GEN_CLOSE" 2>/dev/null | tr -d '[:space:]')" ] \
        && region "$(readme_of "$slug")" "$SRC_OPEN" "$SRC_CLOSE" >/dev/null 2>&1 ;;
    landed-via-lander)
      [ -n "$LANDER" ] && [ -n "$BYPASS_BAN" ] && ! grep -qF -- "$BYPASS_BAN" "$rel" ;;
    build-complete)
      # The owner's "merge and push only when the entire build is fully done", given a checker.
      # FIVE terms, ALL required. Terms 1-2 guard the roster itself; term 3 is the only one that can
      # see a planned unit nobody specced, because the generated region is rendered from the specs
      # that EXIST; and term 4 is here because term 5 is VACUOUSLY TRUE over an empty selection -
      # `region` exits 0 with empty stdout for a well-formed pair enclosing nothing, so a run-state
      # file spliced empty would satisfy "no unit row is non-terminal" by carrying no unit rows.
      # No new fail branch: this reports through verb_close's fail 13, which already prints the
      # exact --override spelling. A waiver on `land-once-done` relaxes the DIRECTIVE and never this
      # item, so a run that waived it still owes --override build-complete at close.
      # THE UNITS REGION IS REPORTED BY NAME. The five terms were ANDed into one verdict, so a
      # README predating this item failed with a bare "unmet" and nothing said a marker pair was what
      # it wanted -- which is every build folder in this tree older than the item.
      #
      # TOOL-aBoundedVerdict-11 S8 - the GENERATED region, so this term stops being a hand-edit away
      # from satisfiable. Before it, the term read the AUTHORED roster pair, which only four of 49
      # build folders carried and which nothing creates: the item was unmeetable on the rest, and the
      # only exit was `--override build-complete`, the run authorizing itself past the one item that
      # means the build is done.
      if ! region "$(readme_of "$slug")" "$UNITS_OPEN" "$UNITS_CLOSE" >/dev/null 2>&1; then
        DOD_OUT="the build README carries no well-formed units marker pair, and build-complete reads the roster from that region: $(readme_of "$slug") · repair: the --write mode of tools/memory-tree/gen_build_index.py"
        return 1
      fi
      # TOOL-aBoundedVerdict-12 S3 - the four surviving terms are evaluated SEQUENTIALLY so each can
      # say which one failed. They were ANDed into one verdict, so all four printed the same sentence
      # and `--override build-complete` became the natural next move for a reader who could not tell
      # a missing spec from an unfinished unit. Every value below was already computed in a
      # substitution that was thrown away: only the messages were missing.
      DOD_OUT=""
      local _bcids _bcmiss _bcrows _bcnon
      # ROWS BEFORE IDS, deliberately. A region with no rows has no ids either, so testing ids first
      # made the no-rows message unreachable from any fixture - a branch nothing can exercise, which
      # is the same defect as an arm that cannot fire, one layer down. Structure first, then content.
      _bcrows=$(unit_rows "$(readme_of "$slug")")
      if [ -z "$_bcrows" ]; then
        DOD_OUT="the generated units region carries no unit ROWS, and 'no unit row is non-terminal' is vacuously true over none of them, so completeness cannot be read from it: $(readme_of "$slug")"
        return 1
      fi
      _bcids=$(unit_ids_of "$slug")
      if [ -z "$_bcids" ]; then
        DOD_OUT="the build's generated units region names no unit id, so there is no roster to judge completeness against: $(readme_of "$slug")"
        return 1
      fi
      _bcmiss=$(missing_units "$slug" "$M/builds/$slug")
      if [ -n "$_bcmiss" ]; then
        DOD_OUT="the authored plan names a unit that no tracked spec carries, so the build is incomplete by its own roster: $_bcmiss"
        return 1
      fi
      _bcnon=$(nonterminal_units "$(readme_of "$slug")")
      if [ -n "$_bcnon" ]; then
        DOD_OUT="a unit of this build is not terminal, so the build is not done; each row below is a unit whose status is neither CLOSED nor WONTDO:
$_bcnon"
        return 1
      fi
      return 0 ;;
    closing-review-recorded)
      # A tracked review record under this build NAMES the base the run pinned once. The join is the
      # sha because every filename and sequence join was measured wrong on 7 of 7 multi-unit builds
      # in this corpus. Eight characters, because a sha spelled in prose is spelled abbreviated: 15
      # of 46 tracked records carry an eight-hex token and NONE carries a full forty.
      #
      # The length guard is not decoration. `grep -F ""` matches every line of every file, so an
      # absent or truncated `base:` would select the FIRST review record in the build and the item
      # would pass by finding anything - the same degeneration an empty base once caused in
      # check_authorization, where it turned a provenance test into a read of the git index.
      #
      # --cached reads the INDEX, which is this kit's stated per-run population and the reason
      # --preflight stages the run-state file, so an untracked review is excluded by construction
      # rather than by a filter. Through GIT() so the object-substitution lever stays inert.
      #
      # It measures that a record EXISTS and names the pinned base. It does not judge what the
      # review said, and no verdict grammar is anchored: `^## Verdict: CLEAN` matches zero of this
      # corpus's 46 records, so anchoring one would make the item unsatisfiable against every review
      # this repo has ever written.
      # SEVEN characters, not eight. Git's default abbreviation here is seven, so that is how records
      # spell it: measured, 29 of 48 tracked records use seven and an eight-char needle matched NONE
      # of them, this build's own record included. The item was therefore UNMEETABLE and clearable
      # only by a self-authored override, which is the one shape this kit exists to refuse. Seven is
      # a floor rather than a lucky number: a shorter prefix is a prefix of every longer spelling, so
      # it still matches a record written at eight, ten or forty.
      # TOOL-aBoundedVerdict-12 S4 - four distinguishable failure modes where there was one silence.
      # The UNTRACKED case is the likeliest and the least guessable: the join reads --cached, so a
      # review record sitting on disk and never staged is invisible here and the operator has no way
      # to tell that from having written no review at all.
      DOD_OUT=""
      rb=$(fact "$rel" base)
      if [ ${#rb} -lt 7 ] ; then
        DOD_OUT="the run-state file records no usable pinned base, and an absent one would make this join select the FIRST review record in the build - passing by finding anything: $rel"
        return 1
      fi
      if [ -z "$(GIT ls-files -- "$M/builds/$slug/reviews/*.md" 2>/dev/null)" ]; then
        if [ -n "$(ls -1 "$M/builds/$slug/reviews/" 2>/dev/null)" ]; then
          DOD_OUT="a review record exists on disk but is NOT TRACKED, and this join reads the index, so it is invisible here; stage it with git add: $M/builds/$slug/reviews/"
        else
          DOD_OUT="no review record exists under this build at all, so nothing records that the closing review happened: $M/builds/$slug/reviews/"
        fi
        return 1
      fi
      # TOOL-aBoundedVerdict-16 S1/S2/S3 - the join asks for a DIFF-REVIEW naming a commit IN RANGE,
      # where it used to ask for any file quoting the pinned BASE. Measured over the seven tracked runs
      # before the change: three had no matching record at all, and two of the four that matched did so
      # on a SPEC-AUDIT - an item named `closing-review-recorded` satisfied by a spec audit that
      # happened to quote a sha.
      #
      # RANGE, not the pin: a fold-scoped round names the fold's base, which is a DESCENDANT of BASE.
      # Under TOOL-aBoundedVerdict-14 the honest closing round names a sha the old test rejected.
      #
      # Membership is decided by GIT ANCESTRY, both directions, not by string comparison: a substring
      # test cannot express "in this range" and would accept a sha from any branch sharing a prefix.
      local _crfound="" _crkindless="" _crf _crsha
      for _crf in $(GIT ls-files -- "$M/builds/$slug/reviews/*.md" 2>/dev/null); do
        # The KIND comes off the binding line. Read with a local grep rather than through the hygiene
        # engine's parser: that parser lives in the memory-tree kit and this kit ships without it.
        # Grammar owner: memory/HYGIENE.md, "Record bindings".
        GIT grep --cached -qE '^\*\*Serves:\*\*.*diff-review' -- "$_crf" || { _crkindless="$_crkindless $_crf"; continue; }
        for _crsha in $(GIT grep --cached -hoE '[0-9a-f]{7,40}' -- "$_crf" 2>/dev/null | sort -u); do
          GIT merge-base --is-ancestor "$rb" "$_crsha" 2>/dev/null || continue
          GIT merge-base --is-ancestor "$_crsha" HEAD 2>/dev/null || continue
          _crfound="$_crf"; break
        done
        [ -n "$_crfound" ] && break
      done
      if [ -z "$_crfound" ]; then
        if [ -n "$_crkindless" ]; then
          DOD_OUT="tracked review records exist under this build but none is a diff-review naming a commit in BASE..HEAD; these carry no diff-review binding line, so a spec audit cannot stand in for a closing review:$_crkindless"
        else
          DOD_OUT="a tracked diff-review exists but names no commit between the pinned BASE and HEAD, so it reviewed something outside this run's range: looking under $M/builds/$slug/reviews/"
        fi
        return 1
      fi
      return 0 ;;
    keepalive-reaped)
      grep -qE '^keepalive-reaped: (yes|true)' "$rel" ;;
    parked-decisions-surfaced)
      grep -qE '^parked-surfaced: (yes|true)' "$rel" ;;
    *)  # a PROJECT item the kit knows nothing about: it is attested unless the project says otherwise
      grep -qE "^$item: (yes|true)" "$rel" ;;
  esac
}

# S11 - the KIND is an argument, because this helper had the override grammar HARDCODED and exactly one
# caller. Routing --abort's reason through it unchanged would have written "override · item …" into the
# parked region, and the build method derives the owner's open/parked row from parked entries "plus any
# recorded DoD override" - so an abort would have arrived in the one turn the owner gets, wearing the
# label of a Definition-of-Done override that never happened.
park() { # file · kind · item · reason
  printf '\n%s %s · item %s · reason %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$2" "$3" "$4" >> "$1"
}

# TOOL-cSettledDocket-1 - the fourth writer of a parked entry, and the first one available MID-RUN.
# Protocol §2 declares four parked kinds and park() had callers for three: --close --override,
# --abort and --preflight --waive. DECISION - the kind §2 names first, "the question, the options
# seen, and the reason the run refused" - had no writer at all, so an agent that refused a decision
# at pass four had nowhere to put it that any gate reads. Hit during cBriefedPilot's own fold, where
# the workaround was a backlog row: a different document, read by different people, at a later time.
# TOOL-aBoundedVerdict-15 S2 - the two AGENT-ATTESTED DoD keys had no writer anywhere in the kit, so
# --abort (the documented sole exit from a wedged run, which REQUIRES both) was reachable only by
# hand-editing the authored region of a file the kit calls generated and whose grammar the driver owns.
#
# It refuses a MACHINE-checked item, and it does so by reading the item's declared CHECKER rather than
# matching a pair of names: a project that declares its own agent-attested extra item gets the verb,
# and one that renames a machine item still gets the refusal. Writing a machine key by hand is exactly
# the self-certification this kit exists to prevent.
#
# The RECORD KEY is derived here too, so an operator never spells one: `parked-decisions-surfaced` is
# read from a line spelled `parked-surfaced:`, and that mismatch is why the close-path refusal used to
# send people to write a key nothing reads.
verb_attest() { # slug · item · value
  local slug="$1" item="$2" val="${3:-yes}" rel key ck
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 47 "no run-state file, so there is no run to attest anything about: $rel"; return 1; }
  [ -n "$item" ] || { fail 47 "--attest requires --item: an attestation with no item named is not an attestation"; return 1; }
  case " $(dod) " in *" $item:"*) ;;
    *) fail 47 "--attest names an item that is not in the declared DoD set, so nothing would ever read it: $item"; return 1;; esac
  ck=$(checker_of "$item")
  if [ "$ck" != agent ]; then
    fail 47 "--attest refuses a MACHINE-checked item, because writing its key by hand is the self-certification the Definition of Done exists to prevent; this item is checked by the driver: $item"
    return 1
  fi
  refuse_if_terminal "$rel" --attest || return 1
  case "$item" in parked-decisions-surfaced) key=parked-surfaced ;; *) key="$item" ;; esac
  set_fact "$rel" "$key" "$val" || return 1
  stage_or_fail "$rel" || return 1
  echo "unattended: attested — $key: $val (an attestation, not a machine verdict)"
  return 0
}

verb_park() { # slug · item · reason
  local slug="$1" item="$2" reason="$3" rel want pl
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  # TWO guards and not one. `refuse_if_terminal` returns 0 for a record that does not EXIST, so
  # leaning on it alone would let --park mint a parked entry for a run that never started.
  [ -f "$rel" ] || { fail 43 "no run-state file, so there is no run to park a decision against: $rel"; return 1; }
  [ -n "$item" ] || { fail 43 "--park requires --item, because a parked entry with no question recorded is the bare 'parked' the protocol calls indistinguishable from 'forgotten'"; return 1; }
  [ -n "$reason" ] || { fail 43 "--park requires --reason, because an entry recording no reason is indistinguishable from one nobody meant - the same argument --waive already makes"; return 1; }
  # ALL THREE of --waive's reason refusals, not the first. park() appends one LINE and check 17 parses
  # the parked region line-wise, so the NEWLINE refusal is load-bearing here rather than tidy: a
  # reason carrying one forges a second parked row that no verb wrote.
  if [ "$(printf '%s' "$reason$item" | wc -l)" -ne 0 ]; then
    fail 43 "a parked item or reason contains a newline, and park() appends ONE line that the gate parses line-wise, so this would forge a second parked row nothing wrote"; return 1
  fi
  # The item is read back as the token between ' · item ' and ' · reason ', so an item spelling the
  # separator makes its own record unparseable - by the very check that grades it.
  case "$item" in *" · "*) fail 43 "a parked item spells the record's own field separator ' · ', which makes the row unparseable by the check that reads it: $item"; return 1 ;; esac
  # BOTH FIELDS. Check 11 greps the run-state file WHOLE for the flag, so it does not care which
  # field spelled it — screening only the reason left an --item naming the flag free to red the bar
  # permanently, on a terminal record no verb can repair. The same defect one field over.
  if [ -n "$BYPASS_BAN" ] && printf '%s%s' "$item" "$reason" | grep -qF -- "$BYPASS_BAN"; then
    fail 43 "the item or the reason spells the declared bypass flag, and the gate greps this file whole for it, so recording this would red the bar on a record no verb can rewrite; say it without the literal flag: $BYPASS_BAN"; return 1
  fi
  refuse_if_terminal "$rel" --park || return 1
  # IDEMPOTENT, and deliberately NOT by --waive's rule: that one compares handle SETS and refuses a
  # differing one; this compares ONE pair and no-ops on a match. Same purpose - the protocol's
  # post-compaction recovery re-runs the run's own steps, and a re-derived refusal must not
  # duplicate - reached by a different mechanism, because there is no set here to compare.
  # EXACT LINE COMPARE, not a substring search. The reason is the LINE-FINAL field, so `grep -qF`
  # matched any existing row whose reason merely STARTS with this one — and the verb then reported
  # success while writing nothing, silently dropping a distinct decision. Compared in shell against
  # the row with its timestamp stripped, so there is no regex to escape and no anchor to get wrong.
  want="decision · item $item · reason $reason"
  while IFS= read -r pl; do
    [ "$pl" = "$want" ] || continue
    echo "unattended: decision already parked, unchanged — $item"
    return 0
  done <<PARKED
$(grep -F -- ' decision · item ' "$rel" 2>/dev/null | sed 's/^[^ ]* //')
PARKED
  park "$rel" decision "$item" "$reason"
  stage_or_fail "$rel" || return 1
  echo "unattended: decision parked — $item"
  return 0
}

# TOOL-dUnstalledConvoy-5 - the amendment record. M2's AMEND acts are legal in code and were
# undocumented; M3 now delegates the build's own scope. An authority with no record is
# indistinguishable from a run doing whatever it likes, so every amendment leaves a row here.
#
# IT RECORDS AND DOES NOT ACT, deliberately. A record derived from the change it just made is a
# SUMMARY, and a check comparing the two confirms the driver rather than checking it. Recording
# separately is what gives the leg two inputs produced by two acts at two times.
#
# WHAT THIS CANNOT BUY, stated because the pair's honest limit belongs at both ends: nothing forces
# this verb to be called BEFORE the edit, so the row is a declaration in shape rather than in
# enforced ordering. The pair catches an amendment made with NO record - a unit quietly retired
# because it was inconvenient - and does not catch a truthful-looking row attached to a different
# edit.
#
# THE ID SHAPE IS THE DRIVER'S OWN `_ids_of`, never the memory-tree kit's `id_pattern`: that is a
# PYTHON function in a different kit, each kit is copy-installed standalone, and check 10's own
# header records that an adopter may hold one and not the other.
verb_rescope() { # slug · act · unit · successor · reason
  local slug="$1" act="$2" unit="$3" succ="$4" reason="$5" rel want pl ids shaped
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 48 "no run-state file, so there is no run to record an amendment against: $rel"; return 1; }
  # CLOSED SET. A value outside it is a refusal and never a default: defaulting an unrecognised act
  # would let a typo select an amendment nobody asked for, which is the shape ANCHOR_SCOPE's own
  # value guard exists to avoid.
  case "$act" in
    retire|supersede|add) ;;
    *) local _bad=${act:-(none)}
       fail 48 "--rescope --act takes one of retire, supersede or add, and a value outside that closed set may not select one by default: $_bad"; return 1 ;;
  esac
  [ -n "$reason" ] || { fail 48 "--rescope requires --reason, because an amendment recording no reason is indistinguishable from one nobody meant - the same argument --park and --waive already make: $act"; return 1; }
  shaped=$(printf '%s\n' "$unit" | _ids_of)
  [ "$shaped" = "$unit" ] && [ -n "$unit" ] || { local _u=${unit:-(none)}
    fail 48 "--rescope --unit is not id-shaped by the driver's own spelling, so the row would name something no roster can carry: $_u"; return 1; }
  # ARITY BY ACT. A supersession with no successor is a retirement wearing a better name, and an
  # addition with one is describing a relation it does not have.
  case "$act" in
    supersede) [ -n "$succ" ] || { fail 48 "--rescope --act supersede requires --successor, or the row is a retirement wearing a better name: $unit"; return 1; }
               shaped=$(printf '%s\n' "$succ" | _ids_of)
               [ "$shaped" = "$succ" ] || { fail 48 "--rescope --successor is not id-shaped by the driver's own spelling: $succ"; return 1; } ;;
    add)       [ -z "$succ" ] || { fail 48 "--rescope --act add refuses --successor, because an addition names no unit it replaces: $succ"; return 1; } ;;
  esac
  # ALL THREE of --park's field refusals, inherited rather than re-derived. park() appends ONE line
  # and the leg parses the region line-wise, so a newline forges a row nothing wrote; an item
  # spelling the separator makes its own record unparseable by the check that grades it; and the
  # bypass flag in EITHER field reds the bar permanently on a record no verb can rewrite.
  if [ "$(printf '%s' "$reason$unit$succ" | wc -l)" -ne 0 ]; then
    fail 48 "a rescope field contains a newline, and park() appends ONE line the gate parses line-wise, so this would forge a second row nothing wrote: $act"; return 1
  fi
  case "$unit$succ$reason" in *" · "*) fail 48 "a rescope field spells the record's own separator, which makes the row unparseable by the check that reads it: $unit"; return 1 ;; esac
  if [ -n "$BYPASS_BAN" ] && printf '%s%s%s' "$unit" "$succ" "$reason" | grep -qF -- "$BYPASS_BAN"; then
    fail 48 "a rescope field spells the declared bypass flag, and the gate greps this file whole for it, so recording this would red the bar on a record no verb can rewrite; say it without the literal flag: $BYPASS_BAN"; return 1
  fi
  refuse_if_terminal "$rel" --rescope || return 1
  # THE GUARDS ARE ORDERED AND THE ORDER IS THE POINT. The idempotence compare runs FIRST, before any
  # membership test. The units region is RENDERED from the specs that exist, so the moment an
  # amendment is performed the id IS in it - and an unconditional membership refusal on `add` would
  # fire permanently on a run that recorded its row after authoring the spec, while the leg demanded
  # that row permanently. That is the wedge shape this build exists to remove.
  want="rescope · item $act $unit"
  [ -n "$succ" ] && want="$want -> $succ"
  want="$want · reason $reason"
  while IFS= read -r pl; do
    [ "$pl" = "$want" ] || continue
    echo "unattended: amendment already recorded, unchanged — $act $unit"
    return 0
  done <<RESCOPED
$(grep -F -- ' rescope · item ' "$rel" 2>/dev/null | sed 's/^[^ ]* //')
RESCOPED
  ids=$(unit_ids_of "$slug")
  case "$act" in
    retire|supersede)
      printf '%s\n' "$ids" | grep -qxF -- "$unit" || { fail 48 "a rescope names a unit the build README's generated units region does not carry, and a run cannot retire what its roster never held: $unit"; return 1; } ;;
    add)
      printf '%s\n' "$ids" | grep -qxF -- "$unit" && { fail 48 "a rescope adds a unit the generated units region already carries and no matching row explains it, so this records a transition that did not happen: $unit"; return 1; } ;;
  esac
  park "$rel" rescope "$act $unit${succ:+ -> $succ}" "$reason"
  stage_or_fail "$rel" || return 1
  echo "unattended: amendment recorded — $act $unit${succ:+ -> $succ}"
  return 0
}

# TOOL-dUnstalledConvoy-9 - the write-set declaration a concurrent dispatch owes. M6 requires two path
# lists written down before two passes run together, and until now nothing read one, which is the
# whole of why `parallel-when-disjoint` has never produced a concurrent dispatch.
#
# IT RECORDS AND DOES NOT DISPATCH, for the reason its sibling verb records: a row derived from the
# act it describes is a summary, and a check comparing the two confirms the driver rather than
# checking it.
#
# WHAT IT CANNOT BUY. It refuses a declaration that is self-evidently wrong. It cannot refuse one that
# is merely untrue - a pass declaring one path and writing three passes this verb, and is caught, if
# at all, by the leg comparing the declaration against what the commit touched. Stated here so the
# pair's division of labour is readable from either end.
#
# TWO OF M6's THREE CONDITIONS ARE DECIDABLE AND ARE DECIDED HERE. Condition 1 is the intersection
# test below. Condition 3 is the shared-record refusal, in BOTH its halves: the records M6 names
# outright are a flat refusal, and a generated index is refused ONLY together with its generator -
# the qualifier M6 earned through a retraction, because every pass changes a spec header the index is
# rendered from and a flat ban would refuse the ORDINARY declaration. Condition 2 is a judgement about
# meaning and is NOT enforced; a verb that pretended to decide it would be a check that cannot fail.
verb_dispatch() { # slug · unit · writes...
  local slug="$1" unit="$2"; shift 2
  local rel shaped grp p q sib sibpaths want cur curpaths gen idx pair
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 49 "no run-state file, so there is no run to declare a dispatch against: $rel"; return 1; }
  shaped=$(printf '%s\n' "$unit" | _ids_of)
  [ "$shaped" = "$unit" ] && [ -n "$unit" ] || { local _u=${unit:-(none)}
    fail 49 "--dispatch --pass is not id-shaped by the driver's own spelling, and the leg joins a declaration to a commit through that id: $_u"; return 1; }
  [ "$#" -gt 0 ] || { fail 49 "--dispatch requires at least one --writes path, because a declaration naming nothing is not a disjointness proof: $unit"; return 1; }
  # EACH --writes IS ONE PATH. A space-joined value cannot carry the whitespace refusal below: the
  # path has already become two tokens by the time this verb sees it, and nothing recovers that.
  for p in "$@"; do
    case "$p" in
      "") fail 49 "--dispatch was given an empty --writes path, and an empty declaration is not a narrow one: $unit"; return 1 ;;
      /*|?:[/\\]*) fail 49 "--dispatch was given an absolute --writes path, and a declaration is repo-relative or it names a file no comparison can find: $p"; return 1 ;;
      *..*) fail 49 "--dispatch was given a --writes path that escapes the repository, which no pass may declare and no comparison can bound: $p"; return 1 ;;
    esac
    case "$p" in
      *[[:space:]]*) fail 49 "--dispatch was given a --writes path containing whitespace, which the declaration's own field separator cannot carry, so the leg would split it into paths nobody declared: $p"; return 1 ;;
    esac
    # NO SEPARATE NEWLINE OR SEPARATOR BRANCH. Both are subsumed by the whitespace refusal above — a
    # newline IS whitespace and the record's ` · ` separator contains spaces — so a branch for either
    # is unreachable, and `check-arms` named both as having no assertion that could ever fire. A dead
    # branch pinned as unarmed is worse than a deleted one: it reads as coverage.
    if [ -n "$BYPASS_BAN" ] && printf '%s' "$p" | grep -qF -- "$BYPASS_BAN"; then
      fail 49 "--dispatch was given a --writes path spelling the declared bypass flag, and the gate greps this file whole for it: $BYPASS_BAN"; return 1
    fi
  done
  refuse_if_terminal "$rel" --dispatch || return 1
  # CONDITION 3, FLAT HALF. The run-state file is DERIVED rather than declared - it is the one member
  # the kit already knows how to locate - and the rest come from the project's own declaration, so an
  # adopter whose layout differs gets refusals about THEIR paths and not this repo's.
  for p in "$@"; do
    if [ "$p" = "$rel" ]; then
      fail 49 "--dispatch declares the run-state file, which every pass in the run shares, so two passes declaring it are not disjoint by construction: $p"; return 1
    fi
    for q in ${SHARED_RECORDS:-}; do
      case "$p" in "$q"|"$q"/*) fail 49 "--dispatch declares a path under a shared mutable record this project declares, and the build method names those outright rather than conditionally: $p"; return 1 ;; esac
    done
  done
  # CONDITION 3, CONDITIONAL HALF. A generated index alone is ACCEPTED - every pass changes a spec
  # header it is rendered from, and refusing that was the VACUOUS reading M6 retracted. What collides
  # is one pass RENDERING an artifact while another edits its generator, so the refusal fires only
  # when both appear, in this declaration or in a sibling's within the same group.
  grp=$(GIT rev-parse --short=8 HEAD 2>/dev/null)
  [ -n "$grp" ] || { fail 49 "--dispatch cannot resolve HEAD, and HEAD is the group key two passes declared together share: $slug"; return 1; }
  sibpaths=$(grep -F -- " dispatch · item $grp " "$rel" 2>/dev/null | sed 's/.* · reason //' | tr '\n' ' ')
  for pair in ${GENERATED_INDEXES:-}; do
    idx=${pair%%:*}; gen=${pair#*:}
    [ "$idx" = "$pair" ] && continue
    for p in "$@"; do
      case "$p" in "$idx"|"$idx"/*) ;; *) continue ;; esac
      for q in "$@" $sibpaths; do
        case "$q" in "$gen"|"$gen"/*)
          fail 49 "--dispatch declares a generated index together with its generator, which is the one pairing the build method's condition 3 forbids - the index alone is fine and refusing it was the reading that condition retracted: $idx with $gen"; return 1 ;;
        esac
      done
    done
  done
  # CONDITION 1. Two passes in one group claiming one path are not disjoint, and this is decidable the
  # moment the second declaration arrives.
  while IFS= read -r sib; do
    [ -n "$sib" ] || continue
    case "$sib" in *" $unit · reason "*) continue ;; esac   # our own row is not a sibling
    for p in "$@"; do
      for q in ${sib#* · reason }; do
        [ "$p" = "$q" ] || continue
        local _who=${sib#* dispatch · item }; _who=${_who%% · reason *}
        fail 49 "--dispatch declares a path a sibling pass in the same group already declared, and two passes claiming one file are not disjoint: $p also in $_who"; return 1
      done
    done
  done <<SIBS
$(grep -F -- " dispatch · item $grp " "$rel" 2>/dev/null)
SIBS
  # THE RE-DECLARATION RULE, keyed on GROUP plus UNIT. Identical is a no-op; a strict SUPERSET
  # REPLACES, which is the widening repair the leg's own fork resolution commits this build to; a
  # NARROWING is refused, because narrowing a declaration after the fact is how a pass would hide a
  # write it had already made.
  want=$(printf '%s ' "$@"); want=${want% }
  cur=$(grep -F -- " dispatch · item $grp $unit · reason " "$rel" 2>/dev/null | tail -1)
  if [ -n "$cur" ]; then
    curpaths=${cur#* · reason }
    if [ "$curpaths" = "$want" ]; then
      echo "unattended: dispatch already declared, unchanged — $unit"
      return 0
    fi
    for q in $curpaths; do
      for p in "$@"; do [ "$p" = "$q" ] && continue 2; done
      fail 49 "--dispatch re-declares a pass with a path the earlier declaration carried and this one drops, and narrowing a declaration after the fact is how a write gets hidden; widening is the repair, narrowing is not: $q for $unit"; return 1
    done
    park "$rel" dispatch "$grp $unit" "$want"
    stage_or_fail "$rel" || return 1
    echo "unattended: dispatch WIDENED — $unit · $want"
    return 0
  fi
  park "$rel" dispatch "$grp $unit" "$want"
  stage_or_fail "$rel" || return 1
  echo "unattended: dispatch declared — $grp $unit · $want"
  return 0
}

# --------------------------------------------------------------------------------------- dispatch
# TOOL-cBriefedPilot-1 - the PAIRED accumulator. `--override) OV="${2:-}"` stored a scalar, so a
# second occurrence overwrote the first and `verb_close` blocked on the second unmet item forever,
# with nobody to read the block. Reasons contain spaces and may contain anything else an owner types,
# so the pairs go into PARALLEL ARRAYS rather than a delimited string: a record separator inside a
# free-text field the owner supplies is an injection, and the reason is exactly that field.
#
# `--reason` CLOSES the pair its preceding flag opened. With no pair open it keeps its scalar meaning,
# which is what `--abort <slug> --reason <text>` uses. A flag still pending when argv ends keeps the
# EMPTY reason it was pushed with, so it meets the missing-reason refusal that already exists instead
# of vanishing - the refusal is reached by the value, not by a second branch.
VERB=""; SLUG=""; KID=""; REASON=""; arg=""; AT_VALUE="yes"
RS_ACT=""; RS_SUCC=""
DP_WRITES=()
OV_ITEMS=(); OV_REASONS=(); OV_PEND=""
# TOOL-cBriefedPilot-3 - the owner's waiver pairs, through unit 1's accumulator rather than a second
# one. Same reason for parallel arrays: the reason is free text an owner types, and a record
# separator inside it is an injection.
WAIVE_ITEMS=(); WAIVE_REASONS=(); WV_PEND=""
# PRE-SCANNED, because --plan and --phase exit INSIDE the parse loop: at the moment those arms run,
# a later --waive has not been consumed yet and the array is still empty. Asking argv directly is
# the only form of the question that does not depend on where the answer is needed. The first cut
# of this guard read the array and was unreachable for exactly the two verbs the spec named.
WAIVE_SEEN=0
for _a in "$@"; do [ "$_a" = "--waive" ] && WAIVE_SEEN=1; done
# Refusal 1 of five, and it does NOT belong in verb_preflight's precondition block where this spec
# first put it: that function never runs for another verb, so a guard there could never fire. It is a
# DISPATCH guard, and it has to be evaluated inside the --plan and --phase arms too, because both of
# those exit INSIDE the loop and a post-loop check alone never sees them.
refuse_waive_unless_preflight() { # verb
  [ "$WAIVE_SEEN" = 1 ] || return 0
  local v="$1"
  fail 37 "--waive is accepted by --preflight alone; the owner turn that grants a waiver is the last one there is, and a verb reachable mid-run is a place the run could answer its own question: $v"
  return 1
}
while [ $# -gt 0 ]; do
  case "$1" in
    --preflight|--status|--resume|--close|--landed|--abort|--park|--attest|--rescope|--dispatch) VERB="$1"; SLUG="${2:-}"; shift 2 || shift ;;
    --pass)         PK_ITEM="${2:-}"; shift 2 || shift ;;
    --writes)       DP_WRITES+=("${2:-}"); shift 2 || shift ;;
    --act)          RS_ACT="${2:-}"; shift 2 || shift ;;
    --successor)    RS_SUCC="${2:-}"; shift 2 || shift ;;
    --item)         PK_ITEM="${2:-}"; shift 2 || shift ;;
    --keepalive-id) KID="${2:-}"; shift 2 || shift ;;
    # TOOL-aBoundedVerdict-15 S2 - optional, defaulting to `yes`. It exists so the COUNTABLE
    # ATTESTATION unit needs no second verb: that unit wants the parked key's value to carry a COUNT
    # the close can verify, and the current predicate already tolerates trailing text after
    # yes-or-true. Named by what it is, not by its id: it is SPECCED and not built, and shipped source
    # that spells an unbuilt id reads to the drift oracle as a status header nobody updated.
    --value)        AT_VALUE="${2:-}"; shift 2 || shift ;;
    --override)     OV_ITEMS+=("${2:-}"); OV_REASONS+=(""); OV_PEND=ov; WV_PEND=""; shift 2 || shift ;;
    --waive)        WAIVE_ITEMS+=("${2:-}"); WAIVE_REASONS+=(""); WV_PEND=wv; OV_PEND=""; shift 2 || shift ;;
    --reason)       if [ "$OV_PEND" = ov ]; then OV_REASONS[$(( ${#OV_REASONS[@]} - 1 ))]="${2:-}"; OV_PEND=""
                    elif [ "$WV_PEND" = wv ]; then WAIVE_REASONS[$(( ${#WAIVE_REASONS[@]} - 1 ))]="${2:-}"; WV_PEND=""
                    else REASON="${2:-}"; fi; shift 2 || shift ;;
    --plan)         shift; refuse_waive_unless_preflight --plan || exit 1; verb_plan "${1:-}"; exit $? ;;
    --phase)        shift; PH_SLUG=${1:-}; shift 2>/dev/null || true; PH_WANT=${1:-}; shift 2>/dev/null || true
                    PH_WIT=""
                    [ "${1:-}" = "--witness" ] && { shift; PH_WIT=${1:-}; }
                    refuse_waive_unless_preflight --phase || exit 1
                    verb_phase "$PH_SLUG" "$PH_WANT" "$PH_WIT"; exit $? ;;
    --version)      echo "unattended $KIT_UNATTENDED_VERSION"; exit 0 ;;
    *) arg="$1"; fail 14 "unknown argument; the verbs are --preflight, --plan, --phase, --status, --resume, --close, --landed, --park, --rescope, --dispatch and --abort: $arg"; exit 1 ;;
  esac
done
# S10 - THE SAME SET, in all three places the driver spells it. The header docstring, this usage line
# and the refusal above used to name three DIFFERENT sets: the usage line was already two verbs behind
# (it omitted --plan and --phase) and the operator who mistypes a verb reads the refusal, not the
# header. A prior review asked for both to be fixed and only the header landed.
case "$VERB" in --preflight) ;; *) refuse_waive_unless_preflight "${VERB:-(none)}" || exit 1 ;; esac
[ -n "$VERB" ] || { echo "usage: unattended.sh --preflight <slug> --keepalive-id <id> | --plan <slug> | --phase <slug> <phase> --witness <sha> | --status <slug> | --resume <slug> | --close <slug> [--override <item> --reason <text>] | --landed <slug> | --abort <slug> --reason <text> | --park <slug> --item <text> --reason <text> | --rescope <slug> --act <retire|supersede|add> --item <id> [--successor <id>] --reason <text> | --dispatch <slug> --pass <id> --writes <path> [--writes <path> …] | --attest <slug> --item <item> [--value <text>]"; exit 2; }

case "$VERB" in
  --preflight) verb_preflight "$SLUG" "$KID" ;;
  --status)    verb_status "$SLUG" ;;
  --resume)    verb_resume "$SLUG" ;;
  --close)     verb_close "$SLUG" ;;
  --landed)    verb_landed "$SLUG" ;;
  --abort)     verb_abort "$SLUG" "$REASON" ;;
  --park)      verb_park "$SLUG" "$PK_ITEM" "$REASON" ;;
  --attest)    verb_attest "$SLUG" "$PK_ITEM" "$AT_VALUE" ;;
  --rescope)   verb_rescope "$SLUG" "$RS_ACT" "$PK_ITEM" "$RS_SUCC" "$REASON" ;;
  --dispatch)  verb_dispatch "$SLUG" "$PK_ITEM" "${DP_WRITES[@]}" ;;
esac
exit "$status"
