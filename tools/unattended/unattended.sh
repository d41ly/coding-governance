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
#   unattended.sh --propose <slug> --item <text> --step <s> --reason <text>  # amend a playbook LATER
#   unattended.sh --rescope <slug> --act <retire|supersede|add> --item <id> [--successor <id>] --reason <text>
#   unattended.sh --dispatch <slug> --pass <id> --writes <path> [--writes <path> ...]
#   unattended.sh --review <slug> --subject <id> --verdict <verdict> --blockers <N>  # a review round
#   unattended.sh --abort <slug> --reason <text>           # end it, with the reason on the record
#   unattended.sh --attest <slug> --item <item> [--value <text>]  # the agent-checked DoD items
#   unattended.sh --record-piece <slug> --path <p> --leg <n> --verdict <PASS|FAIL|NA>
#   unattended.sh --record-set <slug> --leg <n> --verdict <PASS|FAIL|NA>
#   unattended.sh --version                                        # the kit version, then exit
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
KIT_UNATTENDED_VERSION=1.10   # gov:kit unattended@1.10 — kit identity; set HERE, never from .unattended.conf

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
# THE KIT'S OWN DIRECTORY, DERIVED, and the LIBRARY it sources from there. ONE name for one
# derivation: `KIT_DIR` is what the Skill placeholder, the sibling-script lookup and the header
# self-read all spell, so this block uses it rather than minting a second name for the same path.
#
# The library is sourced before anything reads history. It holds every predicate this script and
# the gate leg must answer identically — `GIT`, the anchored id tests, path containment, and "has
# this pass committed yet". Sourced by absolute path derived from THIS file's location, because the
# `cd` to the repo root happens below and a relative source would resolve against the caller's cwd.
KIT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
[ -f "$KIT_DIR/lib-unattended.sh" ] || {
  echo "unattended: the kit library is missing beside this script, so the predicates it shares with its own gate leg are unavailable and no answer here would be trustworthy: $KIT_DIR/lib-unattended.sh" >&2
  exit 2
}
# shellcheck source=lib-unattended.sh
. "$KIT_DIR/lib-unattended.sh"

# ------------------------------------------------------------------------------ THE VERB SET, ONCE
# the verb-carrier unit. Four carriers used to type this set independently - the header
# docstring, the usage line, refusal 14 and the dispatch - and THREE were stale the day this landed:
# `--record-set` had shipped into the dispatch alone, which is precisely the drift a prior unit's own
# comment claimed to have fixed. The dispatch now READS this line, so a verb missing from it does not
# read wrong, it does not RUN; the usage text is rendered from the docstring above, which is the only
# place a verb's arguments are spelled; and the two carriers in other files are joined to this one by
# the gate leg, because no runtime derivation crosses a file boundary.
VERBS_SLUG="--preflight --status --resume --close --landed --abort --park --propose --attest --record-piece --record-set --rescope --dispatch --review"
# The verbs whose argument is POSITIONAL and which exit inside the parse loop. Separate because the
# dispatch cannot treat them alike, and merged again for every reader, who does not care.
VERBS_INLINE="--plan --phase --version"
verbs_all()   { printf '%s %s' "$VERBS_SLUG" "$VERBS_INLINE"; }
is_slug_verb(){ case " $VERBS_SLUG " in *" $1 "*) return 0 ;; esac; return 1; }
verb_list() { # -> "--a, --b and --c", for a human reading a refusal
  local out="" w n=0 total
  total=$(set -- $(verbs_all); echo $#)
  for w in $(verbs_all); do
    n=$((n+1))
    if   [ "$n" = 1 ];      then out="$w"
    elif [ "$n" = "$total" ]; then out="$out and $w"
    else out="$out, $w"; fi
  done
  printf '%s' "$out"
}
# The usage text, READ FROM THIS FILE'S OWN HEADER. A second spelling of every verb's arguments is
# the drift this block removes, and the header is the spelling that documents them. The self-read
# assumes $0 names this file - which KIT_DIR above already assumes, so it adds no new one.
SELF="$KIT_DIR/$(basename -- "$0")"
usage() {
  local u; u=$(sed -n 's|^#   unattended[.]sh |  unattended.sh |p' "$SELF")
  # A PROBE THAT CANNOT MOVE SAYS SO. Read through a copy whose header was stripped, or through any
  # invocation where $0 does not name this file, the sed above matches nothing - and a bare "usage:"
  # over an empty list is indistinguishable from a driver with no verbs. Refuse into the derived set
  # instead, which is the one carrier that cannot go missing.
  [ -n "$u" ] || { echo "usage: cannot read this file's own header at $SELF, so the argument shapes are unavailable; the verbs are $(verb_list)"; return 0; }
  echo "usage:"; printf '%s\n' "$u"
}

# The dereference pins live in NAMED constants because there are now two readers: GIT() below, and
# the bounded remote helper further down, which cannot call a shell function — `timeout` needs an
# external command, so it must spell `git` itself. Two spellings of one pin is the class this repo
# calls two-answers-to-one-question, and a pin added to one copy and not the other is silent.
# GIT and its two pins come from the kit library sourced above - one definition, shared with the
# gate leg, which is what that library is for.

# THE WALL-CLOCK BOUND on a remote observation, in seconds, and the ssh connect bound inside it.
# FILE CONSTANTS with no conf channel and no environment override, on the same argument the review
# protocol's fan-out cap is a file constant: a ceiling raisable from the environment leaves no diff
# behind. Generous on purpose — the failure being guarded is a PARTITION, not a slow link, and a
# tight bound converts a working close into a refused one, which is a new stall wearing the fix's
# clothes. Both are stated in the refusal, so the number is discoverable without reading source.
REMOTE_BOUND="60"
REMOTE_CONNECT_BOUND="20"
# The low-speed floor: bytes/sec under which git treats a transfer as stalled, for the window the
# wall-clock bound already allows. This is the only mechanism that reaches a server which ACCEPTS
# and then stalls mid-transfer, which no wall-clock cap can distinguish from a slow success.
REMOTE_LOWSPEED_BYTES="1000"

# LIVENESS, probed with the options the run actually uses. A bare `timeout 1 true` passes on a build
# whose `-k` is unsupported, and the gate runner already learned to probe with the real option set.
# A node without a working `timeout` still runs — refusing every run over a missing coreutils binary
# is worse than the hang — but it must SAY the bound is inert, because a skip that looks like a pass
# is indistinguishable from coverage.
REMOTE_BOUND_LIVE=1
timeout -k 1s 1 true >/dev/null 2>&1 || REMOTE_BOUND_LIVE=0
# AND IT SAYS SO, which the comment above has always required and the code did not do: the flag's
# only reader was the `if` in observe_remote, so a node without a working `timeout -k` produced
# byte-identical output while running unbounded. The transport options survive on that path.
[ "$REMOTE_BOUND_LIVE" = 1 ] || echo "unattended: NOTE - this node has no working 'timeout -k', so the ${REMOTE_BOUND}s wall-clock bound on remote observation is INERT; http.lowSpeed and ssh ConnectTimeout still apply" >&2

# EVERY remote observation goes through here, and the source-level arm asserts that no `ls-remote`
# appears outside it. Three bounds, because no single mechanism covers every transport: the outer
# wall clock catches blackholed packets, `http.lowSpeed*` catches an HTTP server that accepts and
# then stalls, and `ssh -o ConnectTimeout` catches the ssh handshake. A wall-clock cap alone kills a
# slow-but-working clone; a transport option alone does not bound a server that stalls after
# accepting.
#
# CAPTURED THROUGH A FILE, NOT A COMMAND SUBSTITUTION, and that is the whole difference between a
# bound and a decoration. `out=$(timeout N cmd)` reads until EOF, and EOF arrives only when the last
# inherited write end closes, so a surviving descendant holds the pipe while `timeout` cheerfully
# reports 124. MEASURED on this node before this helper was written:
# `out=$(timeout 1 bash -c 'sleep 6 & exit 0')` returned after 6 s against a declared 1 s bound; the
# same command redirected to a file returned in 0 s. The gate runner carries the identical fix and
# the identical measurement, which is where this shape comes from rather than being invented here.
#
# The credential path is CLOSED, not merely un-prompted. `GIT_TERMINAL_PROMPT=0` bounds git's OWN
# prompt and says nothing about a configured helper: a helper that opens a GUI dialog blocks forever
# with nothing on stdout. `credential.interactive=never` is what a helper reads. It is passed with
# `-c`, so it is scoped to THIS invocation and cannot reach the landing push, which is a different
# process and must still authenticate — a helper that can answer from its store still answers, and
# only one that would PROMPT refuses.
#
# Returns the subprocess status, or 124 when the wall clock fired. Writes the advertisement to the
# file named by the caller, never to stdout, so no caller can reintroduce the pipe this exists to
# avoid.
observe_remote() { # <outfile> · <git args…> -> rc (124 = the bound fired)
  local out="$1"; shift
  local rc
  if [ "$REMOTE_BOUND_LIVE" = 1 ]; then
    timeout -k 5s "$REMOTE_BOUND" \
      env GIT_TERMINAL_PROMPT=0 \
          "GIT_SSH_COMMAND=ssh -o ConnectTimeout=$REMOTE_CONNECT_BOUND -o BatchMode=yes" \
      git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV" \
          -c credential.interactive=never \
          -c "http.lowSpeedLimit=$REMOTE_LOWSPEED_BYTES" -c "http.lowSpeedTime=$REMOTE_BOUND" \
          "$@" >"$out" 2>/dev/null
    rc=$?
  else
    env GIT_TERMINAL_PROMPT=0 \
        "GIT_SSH_COMMAND=ssh -o ConnectTimeout=$REMOTE_CONNECT_BOUND -o BatchMode=yes" \
    git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV" \
        -c credential.interactive=never \
        -c "http.lowSpeedLimit=$REMOTE_LOWSPEED_BYTES" -c "http.lowSpeedTime=$REMOTE_BOUND" \
        "$@" >"$out" 2>/dev/null
    rc=$?
  fi
  return "$rc"
}

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
KEEPALIVE_CREATE=""; KEEPALIVE_DELETE=""; PHASES_EXTRA=""; DOD_EXTRA=""; DIRECTIVES_EXTRA=""; ANCHOR_SCOPE=""; UNITS_REGION_CUTOFF=""; SHARED_RECORDS="__kit-default__"; GENERATED_INDEXES=""
HALT_CODES_EXTRA=""; HALT_FLOOR=""; LANDER_MARKER=""
# shellcheck disable=SC1090
. "$CONF"
# ARGV STATE, not a conf default. Initialised AFTER the conf is sourced: in the default block above,
# a tracked `.unattended.conf` could pre-set it and defeat the "--park requires --item" refusal by
# supplying the item nobody typed.
PK_ITEM=""; PK_STEP=""
HALT_CODE=""
RV_SUBJECT=""; RV_BLOCKERS=""
M="$MEMORY_ROOT"
# SHARED_RECORDS's DEFAULT IS RESOLVED HERE, not in the block above, because it is expressed in terms
# of MEMORY_ROOT and the conf is what sets that. Computed before the source it baked in this kit's own
# `memory`, so an adopter at any other layout got a default naming a directory it does not have — a
# refusal that can never fire, which is the same shape as no refusal at all. The sentinel is what
# keeps a DECLARED blank meaning the empty set, as the protocol's own conf table promises.
[ "$SHARED_RECORDS" = "__kit-default__" ] && SHARED_RECORDS="$MEMORY_ROOT/DECISIONS.md $MEMORY_ROOT/backlog"

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
DOD_CORE="gates-green:machine records-current:machine authorization-reachable:machine landed-via-lander:machine build-complete:machine closing-review-recorded:machine pieces-complete:machine set-checks-recorded:machine keepalive-reaped:agent parked-decisions-surfaced:agent"

# the proposal-kind unit - the PARKED KINDS, closed and kit-owned like the three sets above it, and
# for the reason those are: a parked row whose kind is outside this set lands in a region every
# reader parses BY kind, so it is a row nothing counts and nothing surfaces. It became a declaration
# when a fifth kind arrived and found the alternation that recognises a row typed into `verb_status`
# - one spelling of a vocabulary that two files read.
PARK_KINDS="decision abort override waiver proposal rescope dispatch review"
# The kinds that are OWED to the owner as an ANSWER. Three are deliberately absent, and they are
# absent for one reason: each is a DECLARATION the run made, not a question it refused. A proposal is
# an improvement it noticed, a rescope is an amendment it took under a delegated authority, a
# dispatch is a claim about what two passes will write. Counting any of them as parked would make a
# run that recorded six of its own acts look like a run that stalled on six decisions.
PARK_KINDS_OWED="decision abort override waiver"
# The Definition-of-Done items an override may NOT buy. A DECLARED set rather than a name hardcoded
# into a case arm: it WAS one name, and the second arrived as an acceptance criterion this build had
# ratified and never implemented — found by writing the arms the item never had.
#
# `pieces-complete` joins it because it is the item that says the run produced what the owner asked
# for, over content nothing else in the bar can grade. An override on it is the run certifying its
# own output, which is the same shape the authorization item is protected from.
DOD_NO_OVERRIDE="authorization-reachable pieces-complete"

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
# TWO NAMES FOR ONE FACT, CONVERGED AT THE MERGE. This block arrived declaring
# `PARK_KINDS_OWED="decision abort override waiver"` while the other side of the merge
# declared `PARK_KINDS_OWED` with the same four values and a `PARK_KINDS` superset holding three
# more. One set, two spellings, and the checks keyed on each would have agreed for exactly as
# long as nobody added a kind. `PARK_KINDS_OWED` survives because it names the PROPERTY - these
# are the kinds the owner owes an answer to - and because the unowed set is DERIVED from the
# difference rather than typed a third time.
# THE PARKED-KIND TAXONOMY, and the word `decision` released back to one job. It was doing two —
# the literal KIND TOKEN this kit writes into a parked line, and the CLASS the surfaced count
# measures — and neither this constant nor the counter below is buildable while one name means both.
# The two classes are `surfaced`, which the owner must be shown, and `history`, which the owner need
# not adjudicate.
#
# MEMBERSHIP IS DECLARED HERE AND NOWHERE ELSE, and `history` is the COMPLEMENT: a kind absent from
# this line is history by construction, so there is no second set to keep in step. That is the whole
# reason it is one constant and not two.
#
# All four live kinds are `surfaced`, WAIVER INCLUDED — the protocol already records that a waiver
# entry is surfaced by the wrap-up derivation with the other parked kinds, so a set built from an
# earlier two-name reading ships short that member and regresses a stated behaviour. What follows is
# that the counter below over-counts by NOTHING against any record that exists today; it becomes wrong
# the moment the first `history` kind lands, which is why this taxonomy has to be declared BEFORE the
# unit that adds one rather than alongside it.
#
# The shrink-only FLOOR this set deserves is NOT here, and that is stated rather than left to be
# noticed: the two sets it sits beside pin their counts from the project conf, and a new conf key is a
# new public surface for the kit. So the taxonomy ships with its constant and its single reader, and
# its shrink-only property is UNARMED until that carrier is an owner decision. No criterion pretends
# otherwise.
# THE HALT VOCABULARY. A run that stops has to say WHY in a token something can read, and until this
# existed the single `ABORTED` terminal said nothing at all — the reason lived in free prose in a
# parked entry, which the owner reads and no check does.
#
# ONE MEMBER PER HALT SITE THIS BUILD ACTUALLY ENUMERATED, and none invented for symmetry. A vocabulary
# with a member nothing produces is the phase vocabulary's own disease, and a catch-all member is a
# hole that swallows the set within a few runs — so an unclassifiable halt takes the CLOSEST code and
# puts the specifics in the free-text reason, and the mismatch earns a backlog row when it happens.
#   runaway-ceiling-unclean   the review loop hit its runaway ceiling with the subject not clean. Its
#                             being reached is itself a defect in the convergence predicate.
#   fork-unresolvable         a fork survived the method vetoes with no resolution the mandate delegates.
#   scope-approval-needed     a unit awaits owner scope approval the mandate does not supply.
#   external-prerequisite     a unit is blocked on something outside the repo. A DIFFERENT owner turn
#                             from an unapproved scope, and conflating them tells a returning owner to
#                             do the wrong thing.
#   acceptance-underivable    a unit acceptance or gate set could not be derived, so it is not Ready
#                             and no run can split it.
#   repo-state-out-of-mandate the repository state at start was outside what the mandate reaches.
#   gate-red-out-of-scope     a gate is red and its fix lies outside the mandate scope.
# THE RUNAWAY CEILING, and it is a BACKSTOP rather than the mechanism. The loop is bounded by a
# CONVERGENCE PREDICATE, not by a count; this exists so a defect in that predicate cannot produce an
# unbounded loop. It is set well above any observed converging sequence, so REACHING it is itself a
# defect worth reporting rather than a routine outcome — and under the owner resolution the run
# promotes and lands anyway rather than halting, which is why it must be loud in two carriers.
# A file constant, not a conf key and not an environment variable, on the argument this repo already
# recorded for its agent fan-out bound: a ceiling raisable from the environment leaves no diff behind.
RUNAWAY_CEILING="8"
# THE REVIEW VERDICT VOCABULARY, closed and kit-owned. Its CANONICAL home is the memory-tree kit,
# which enforces review-record grammar and renders the build method; a copy-installed kit cannot
# import across that boundary, so this is a STATED duplication whose drift is armed by a row in that
# kit's conformance table rather than hoped away. Pipe-separated because one member contains a space,
# which a space-separated set cannot hold.
REVIEW_VERDICTS="CLEAN|CLEAN WITH FIXES|BLOCKED"
HALT_CODES_CORE="runaway-ceiling-unclean fork-unresolvable scope-approval-needed external-prerequisite acceptance-underivable repo-state-out-of-mandate gate-red-out-of-scope"
DIRECTIVES_CORE="minimal-prose:M10 sub-specced:M2 forks-resolved:M3 specs-reviewed:M4 reuse-first:M5 parallel-when-disjoint:M6 passes-committed:M6 diff-reviewed:M8 land-once-done:M8 conflicts-reconciled:M8 wrap-up-derived:M9 researched:M12:prompt solution-tested:M12:prompt pieces-recorded:M9:recipe playbook-followed:M7:recipe"

# the AUTHORIZATION MODE set, published as a constant so it is spelled
# ONCE. It was a `case` arm in one file and a hardcoded pair in another, which is why check 19 could
# compare two records carrying the same misspelling and agree with both: it asked whether they
# MATCH and never whether either is LEGAL. Kit-owned like the three sets below it, with no
# `MODES_EXTRA` - a project-declarable authorization discipline is one nobody wrote. No floor
# either: the sets below pin a shrink-only count because a project may EXTEND them, and nothing
# extends this one, so a pin here would guard a variable only this kit moves.
AUTH_MODES="slug prompt recipe"
# TOOL-dNarrowedAnchor-1 - the PARTITION of that vocabulary by whether the mode's own discipline is
# to AUTHOR the build folder the run is authorized by. `slug` is defined as a folder that already
# exists, so a `slug` run never needs the second anchor and a `slug` run that REACHED it has
# contradicted its own declaration. `prompt` always authors one; `recipe` may, and SKILL.template.md
# tells a playbook author in as many words that authoring it "needs `published`" - so excluding
# `recipe` would make this kit refuse a path its own carrier instructs.
#
# KIT-OWNED, with no conf channel, for the reason AUTH_MODES states one line up and one more of its
# own: an adopter-declarable set is an adopter-reopenable hole, and there is no project in which a
# `slug` run legitimately authorizes itself off a branch it pushed.
#
# ABSENT `authorized-by:` DEFAULTS TO `slug`, so every build README written before that key existed
# is outside this set. That is the right answer for all of them - they were landed on the default
# branch, which is the first anchor, and this set is only ever consulted on the second.
SECOND_ANCHOR_MODES="prompt recipe"
is_second_anchor_mode(){ case " $SECOND_ANCHOR_MODES " in *" $1 "*) return 0;; esac; return 1; }

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
# the directive SCOPE set is DERIVED, never a second constant: a scope is
# exactly "every run" or "a run in mode M", so `all` plus every member IS the set. Deriving it is
# what stops the two disagreeing - a second literal would need editing in step with this one, and
# the pair that already existed did not.
scopes()      { printf 'all %s\n' "$AUTH_MODES"; }
is_auth_mode(){ case " $AUTH_MODES " in *" $1 "*) return 0;; esac; return 1; }
is_scope()    { case " $(scopes) " in *" $1 "*) return 0;; esac; return 1; }
is_terminal() { case " $PHASES_TERMINAL " in *" $1 "*) return 0;; esac; return 1; }
# The EFFECTIVE halt vocabulary: kit core plus whatever the project appended. Same shape as the phase
# and Definition-of-Done sets, so a project can extend it and cannot delete from it.
halt_codes() { printf '%s %s\n' "$HALT_CODES_CORE" "$HALT_CODES_EXTRA"; }
# ENDPOINT NORMALISATION for the fetch-vs-push comparison. Two spellings of the same place are not a
# misconfiguration, and the check that compared them literally made an UN-OVERRIDABLE Definition-of-Done
# item unsatisfiable for anyone whose clone carries a split fetch/push URL — which git offers two
# separate mechanisms for. The rules are exactly the equivalences git itself accepts:
#   scheme dropped            https://h/p and ssh://h/p are the same endpoint for this question
#   scp-style recognised      git@host:owner/repo  ==  ssh://host/owner/repo
#   userinfo dropped          a username is a credential, not an endpoint
#   trailing .git and /       cosmetic in every form git accepts
#   host case-folded          hostnames are case-insensitive; paths are NOT and stay exact
# What it deliberately does NOT do: parse URLs in general, or judge whether the run CAN push over its
# push URL. That is the lander's business. This asks one question — are these the same place — and
# a genuinely different host or path is still a refusal, which is the honest misconfiguration the
# check was written for.
norm_endpoint() { # <url> -> host/path, comparable
  local u="$1"
  u=${u%/}; u=${u%.git}; u=${u%/}
  # SCP-STYLE IS DETECTED BY GIT'S OWN RULE — a colon before any slash — and NOT by the presence of a
  # user. Keying on `*@*:*` was wrong twice over, and both ways were measured against the shipped
  # function before this fix: a USERLESS `github.com:alice/repo` fell through to the scheme path, where
  # `${u%%/*}` then `${host%%:*}` DELETED the first path segment, so `github.com:alice/repo` and
  # `github.com:bob/repo` both normalised to `github.com/repo` — two different repositories comparing
  # EQUAL, which would let a split across repos take the warning branch and let a run anchor on one
  # repo while landing on another. And `git@github.com:alice/repo` normalised differently from
  # `github.com:alice/repo`, so one place in two spellings compared DIFFERENT, which is the wedge this
  # unit exists to remove.
  case "$u" in
    *://*) u=${u#*://}; u=${u#*@} ;;            # scheme form: strip scheme, then userinfo
    *)     u=${u#*@}                            # scp form: userinfo is optional
           case "${u%%/*}" in
             *:*) u="${u%%:*}/${u#*:}" ;;       # a colon BEFORE any slash separates host from path
           esac ;;
  esac
  local host=${u%%/*} rest=""
  case "$u" in */*) rest=${u#*/} ;; esac
  host=$(printf '%s' "$host" | tr 'A-Z' 'a-z')
  host=${host%%:*}                              # an explicit port is not an identity difference here
  printf '%s/%s\n' "$host" "$rest"
}
is_halt_code() { case " $(halt_codes) " in *" $1 "*) return 0;; esac; return 1; }
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
# fork 8's hybrid. The build README at BASE names the PLAYBOOK PATH and
# the requested piece COUNT; the playbook at that same BASE carries the output globs and the piece
# grain. The path must come from somewhere the run cannot have written, and the globs must travel
# with the playbook - a playbook re-run next month must not depend on a run author retyping its
# outputs correctly. Both are read ONLY in `recipe` mode; absent under any other mode is legal and
# means nothing.
AUTH_PLAYBOOK=""
AUTH_PIECES=""
AUTH_OUTPUTS=""
AUTH_GRAIN=""
AUTH_RECORDS=""
observe_anchor() {
  local v names rem uf up nrem levers adv rc aref asha envd
  # ---- 22: git config supplied through the ENVIRONMENT. A check reading a config its own caller
  # ---- injected is reading the run's answer rather than the repo's.
  names=""
  for v in GIT_CONFIG_COUNT GIT_CONFIG_PARAMETERS GIT_CONFIG_GLOBAL GIT_CONFIG_SYSTEM \
           GIT_DIR GIT_COMMON_DIR GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES GIT_NAMESPACE; do
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
    # NORMALISE BEFORE JUDGING. A literal comparison read two spellings of one endpoint as two
    # endpoints, and this check gates `authorization-reachable`, which has no override — so a clone
    # with a split fetch/push URL could not satisfy an item it is not allowed to waive. git offers
    # two separate mechanisms for that split and only one of them shows up in `remote.<n>.url`.
    if [ "$(norm_endpoint "$uf")" = "$(norm_endpoint "$up")" ]; then
      # SAME PLACE, two spellings. A warning and not a refusal, because this check's own comment
      # says it is a cost-raiser and not the property — a relay the run seeded satisfies it with one
      # URL — and a cost-raiser that wedges an un-overridable item is disproportionate to its stated
      # purpose. STDOUT ONLY. It used to also append to DOD_OUT, claiming that "a caller that
      # discards output does not discard the fact" — and no caller ever read it: `verb_close` calls
      # observe_anchor, then the DoD loop opens with `gates-green`, whose arm begins with an
      # unconditional `DOD_OUT=""`. So the note was destroyed on every ordinary close, and on a close
      # where `gates-green` was OVERRIDDEN the arm was skipped, the stale text survived, and the next
      # unmet item printed an endpoint note indented as ITS detail.
      echo "unattended: NOTE — fetch and push URLs differ in spelling and normalise to the same endpoint: fetch $uf, push $up"
    else
      fail 25 "the URL this clone would OBSERVE is not the URL it would PUSH to, so the anchor and the landing name two different endpoints: fetch $uf, push $up"
      return 1
    fi
  fi
  # ---- 27/28: the REMOTE names its own default branch. `--exit-code` is what makes "answered but
  # ---- advertised nothing" distinguishable from "answered": without it the call exits 0 and prints
  # ---- nothing, which is exactly what a bare repo with a dangling HEAD produces.
  # BOUNDED, and captured through a FILE rather than a command substitution — the substitution is
  # what makes a wall-clock bound a decoration, measured on this node before the helper was written.
  # A fired bound is reported as ITSELF: "did not answer" and "was not waited for" are different
  # facts, and check 27's message would have told an operator the remote was unreachable when the
  # truth is that this kit stopped waiting.
  local advf; advf=$(mktemp) || { fail 27 "cannot create a scratch file to capture the remote advertisement, so the observation cannot be bounded and an unbounded one is what this refuses"; return 1; }
  observe_remote "$advf" ls-remote --symref --exit-code "$rem" HEAD && rc=0 || rc=$?
  adv=$(cat "$advf" 2>/dev/null); rm -f "$advf"
  if [ "$rc" = 124 ]; then
    fail 27 "the remote observation was KILLED by this kit's own wall-clock bound rather than answered, so nothing was learned about the endpoint and this is a timeout and not a refusal by the remote: $rem at $uf, bound ${REMOTE_BOUND}s, connect ${REMOTE_CONNECT_BOUND}s"
    return 1
  fi
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
#   5 = the remote could not be reached, or the wall-clock bound fired. NOT 2, and that split is the
#       whole of it: `|| return 2` collapsed git's 128 (could not connect) into "answered, no
#       matching ref", so a network fault told the operator to push a branch that is already
#       pushed — advice that is not merely unhelpful but wrong, and acted on it does nothing. The
#       sibling function one file up already splits the same pair correctly; this is that logic
#       applied at the call site whose author wrote the collapse.
branch_tip_quiet() { # -> prints "<ref> <sha>" on stdout
  local cur rem adv sha rc advf
  cur=$(GIT rev-parse --abbrev-ref HEAD 2>/dev/null) || return 1
  [ -n "$cur" ] && [ "$cur" != HEAD ] || return 1
  rem=$(GIT remote 2>/dev/null | head -1)
  [ -n "$rem" ] || return 2
  # RETURNS 5, THE UNKNOWN CODE, and a distinct code for a local scratch failure was tried and
  # DELETED. It could not fire: this function is only reached through `[ -n "$ASHA" ] && trusted_base`,
  # and a TMPDIR broken enough to fail mktemp here has already failed observe_anchor, which leaves
  # ASHA empty. The two scratch failures have one cause, and observe_anchor names it first. What the
  # distinct code was FOR - not sending the operator at the network for a local fault - is kept by
  # code 5 naming all three possibilities instead of asserting the first.
  advf=$(mktemp) || return 5
  observe_remote "$advf" ls-remote --exit-code "$rem" "refs/heads/$cur"; rc=$?
  adv=$(cat "$advf" 2>/dev/null); rm -f "$advf"
  # 0 = advertised · 2 = git's own "answered, advertised nothing" from --exit-code · anything else
  # is a transport fault or the bound firing, and both are 5.
  case "$rc" in
    0) ;;
    2) return 2 ;;
    *) return 5 ;;
  esac
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
    5) fail 32 "the remote could not be reached for this run's branch, the wall-clock bound fired, or this side could not create the scratch file the observation needs, so whether the branch is published is UNKNOWN rather than answered no; pushing it is not the remedy, and the endpoint and the local scratch dir are: refs/heads/$cur" ;;
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
    # ANY mode scope, not the one literal. `all` binds every run; a scope
    # naming a mode binds only a run of that mode. The test used to name `prompt` twice, so a
    # handle scoped to a later member was silently unenforced - accepted rather than refused,
    # which is the direction that loses.
    if [ "$sc" != all ] && [ "$sc" != "${AUTH_MODE:-}" ]; then
      fail 45 "--waive names a directive whose scope is a mode this run is not, so the waiver would record the relaxation of a rule that never bound it - handle $h, directive scope $sc, run mode ${AUTH_MODE:-unset}"
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
  local slug="$1" base="$2" rel blob fmslug _fm _pb
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
    /^authorized-by:/ { v = $0; sub(/^authorized-by:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print "mode=" v; next }
    /^playbook:/ { v = $0; sub(/^playbook:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print "playbook=" v; next }
    /^pieces:/ { v = $0; sub(/^pieces:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print "pieces=" v; next }')
  fmslug=$(printf '%s\n' "$_fm" | sed -n 's/^slug=//p' | head -1)
  AUTH_MODE=$(printf '%s\n' "$_fm" | sed -n 's/^mode=//p' | head -1)
  # out of the SAME scan. The `No second GIT show` rule above bounds THAT
  # front-matter parse and is not a rule against reading a second FILE, which S2b does.
  AUTH_PLAYBOOK=$(printf '%s\n' "$_fm" | sed -n 's/^playbook=//p' | head -1)
  AUTH_PIECES=$(printf '%s\n' "$_fm" | sed -n 's/^pieces=//p' | head -1)
  # ABSENT is `slug` - every build README in every adopter's tree today declares nothing, and that
  # is the ordinary case, not a defect. A value OUTSIDE the closed set is a refusal rather than a
  # default: defaulting an unrecognised mode to either member lets a typo select a discipline
  # nobody declared, which is the failure shape ANCHOR_SCOPE's own value guard exists to avoid.
  [ -n "$AUTH_MODE" ] || AUTH_MODE=slug
  # MEMBERSHIP of the published set, and the message DERIVES the legal
  # values from that same set. The refusal used to enumerate them in its own prose, so a third
  # member would have left the sentence naming two and nothing would have reported the drift.
  if ! is_auth_mode "$AUTH_MODE"; then
    fail 44 "the build README at the pinned BASE declares an authorization mode outside the closed set, and defaulting an unrecognised mode would select a discipline nobody declared - legal values are $AUTH_MODES, declared: $AUTH_MODE"
    return 1
  fi
  # TOOL-dNarrowedAnchor-1 - THE SECOND ANCHOR IS ADMISSIBLE PER MODE. `ANCHOR_SCOPE` is a
  # whole-project switch: an adopter turns it on for the prompt path and, before this branch, also
  # got a `slug`-mode run that could author its own build folder, push its own branch and be
  # authorized by it - with nothing anywhere saying so. Reported by an adopter that had to write the
  # concession into its own charter because the kit gave it no way to scope one.
  #
  # AFTER the membership test and not before, because AUTH_MODE has no meaning until it is known to
  # be legal, and a refusal keyed on an unrecognised value would name a discipline nobody declared.
  #
  # ORDER, and it is the reason this is a refusal rather than a selector: the mode lives in a blob
  # the anchor must resolve BEFORE anything can read it, so the anchor cannot be chosen by the mode.
  # Both facts exist only here, and here is where they are compared.
  #
  # `ANCHOR_KIND` IS FRESH, not recalled. The evidence-never-an-input rule bans reading a value back
  # out of the run-state file, which is a byte the subject wrote; this one was derived by
  # `resolve_base` from the remote observation and the local history inside this same invocation,
  # exactly as the `recipe` branch below reads a freshly-parsed AUTH_MODE.
  if [ "$ANCHOR_KIND" = run-branch ] && ! is_second_anchor_mode "$AUTH_MODE"; then
    fail 50 "the BASE came from the second anchor - a tip this run pushed - while the build README declares a mode whose discipline is that the folder already existed, so the run authorized itself with a declaration that says it did not: mode $AUTH_MODE, admissible on this anchor are $SECOND_ANCHOR_MODES; land the build folder on the default branch, or declare the discipline the run is actually under"
    return 1
  fi
  # the declaration seam, evaluated where the MODE exists and nowhere else.
  # Each refusal is its own message: a single ANDed verdict would send a reader to diff a parse
  # against a path, which is the defect the Definition-of-Done evaluation already fixed once by
  # splitting its terms.
  if [ "$AUTH_MODE" = recipe ]; then
    if [ -z "$AUTH_PLAYBOOK" ]; then
      fail 46 "a recipe-mode build README declares no playbook, and the mode is the discipline of FOLLOWING one, so there is nothing for this run to follow - add a playbook: key naming a repo-relative path at BASE"
      return 1
    fi
    if ! _pb=$(GIT show "$base:$AUTH_PLAYBOOK" 2>/dev/null); then
      fail 46 "a recipe-mode build README names a playbook that does not resolve at the pinned BASE, so the instructions this run would follow are not ones anything committed before it can vouch for - path and base follow: $AUTH_PLAYBOOK at $base"
      return 1
    fi
    # The declaration block is unit 2's fenced TOML. Read for the two keys THIS unit owns; the rest
    # belong to the units that read them and are parsed there.
    # THROUGH THE SHARED PARSER. The fold moved `grain` and `records` onto it and left this line
    # alone, and the guard below string-compared the raw text against `[]` - so the kit's OWN template
    # line, `outputs      = []    # globs. Where pieces land.`, matched neither alternative and
    # `fail 46` never fired. An adopter who copied the template and never filled `outputs` was
    # authorized for a recipe-mode run declaring no output globs, which is exactly the state the
    # refusal's own message says leaves the scope check with nothing to compare against. Round 2's M1,
    # one key over, on the other member of DOD_NO_OVERRIDE.
    if ! AUTH_OUTPUTS=$(declared_list "$_pb" outputs); then
      fail 46 "the playbook at the pinned BASE opens an output-glob list it does not close on the same line, so the globs bounding where a recipe-mode run may write are unreadable and an unarmed parse must red rather than return the declared null: $AUTH_PLAYBOOK"
      return 1
    fi
    AUTH_GRAIN=$(declared_scalar "$_pb" grain)
    AUTH_RECORDS=$(declared_scalar "$_pb" records)
    case "$_pb" in
      *'```toml'*) ;;
      *) fail 46 "the playbook at the pinned BASE carries no declaration block, so its output globs, its piece grain and its gate legs are all unreadable and every check keyed on them would pass over nothing: $AUTH_PLAYBOOK"
         return 1 ;;
    esac
    case "$AUTH_OUTPUTS" in
      '') fail 46 "the playbook at the pinned BASE declares no output globs, so a recipe-mode run has nowhere its pieces may legally land and the scope refusal would have nothing to compare against: $AUTH_PLAYBOOK"
         return 1 ;;
    esac
    if [ -z "$AUTH_GRAIN" ]; then
      fail 46 "the playbook at the pinned BASE declares no piece grain, and a grain is what says whether three changed files are three pieces or one, so refusing beats defaulting a count nobody declared: $AUTH_PLAYBOOK"
      return 1
    fi
    if [ -z "$AUTH_PIECES" ]; then
      fail 46 "a recipe-mode build README declares no piece count, so the run has no number to be measured against and the Definition-of-Done item that means it made what was asked would compare against nothing - add a pieces: key"
      return 1
    fi
    case "$AUTH_PIECES" in
      *[!0-9]*) fail 46 "a recipe-mode build README declares a non-numeric piece count, and defaulting or truncating one would put a number nobody wrote into the record the close is judged against - declared: $AUTH_PIECES"
         return 1 ;;
      0) fail 46 "a recipe-mode build README declares a piece count of zero, which asks for a run that produces nothing and would satisfy its own completeness check vacuously - declared: $AUTH_PIECES"
         return 1 ;;
    esac
  fi
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
# THE FORK MARK, and the one place this kit spells it. A bare `RESOLVED` anywhere on the section's
# FIRST line used to decide the whole question, which had two failure modes and both were live: a §8
# whose opening line ANNOUNCED that a fork was unresolved classified as resolved, because the word
# appeared in the sentence saying it had not happened; and any unresolved bullet BELOW a `none` first
# line was invisible, because nothing past that line was read. So the rule every other unit in this
# build writes about forks was unenforceable — a section could declare itself open and be graded shut.
#
# The mark is now the DOCUMENTED one: the resolution word, then a parenthesised attribution whose
# first field is the resolver class, whose second is a date, and whose optional third is the
# delegation qualifier. Prose containing the word no longer resolves anything.
#
# The sibling reader in the memory-tree kit grades the same grammar and cannot import this one — a
# cross-kit edge is what that kit's conformance harness exists to forbid — so AGREEMENT is proven by
# a case table there rather than by sharing code here. Change this regex and that table reds.
# SPELLED AS A REGEX LITERAL INSIDE the awk program, and that is not a style choice. Handing it in
# with `-v mark=...` cost a cycle here: awk processes escape sequences in a -v ASSIGNMENT, so `\(`
# arrived as a bare `(` and the pattern became a GROUP instead of a literal paren — it then matched
# nothing, and every spec in the live build read FORKED. Exactly the escape-reaches-the-regex class
# this repo catalogues, one delimiter over. A single-quoted `/.../` literal has no escape level to
# lose, and it also keeps this function SLICEABLE: the sibling kit's conformance harness lifts this
# body out of the shipped bytes and evaluates it, so a constant defined outside it would arrive empty.
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
      if (cur == "forks") { fl[++nf] = line; if (forkline == "") forkline = line } }
    END {
      thin = (seen["scope"] == "" || seen["acc"] == "" || seen["gates"] == "")
      # M2 orders the checks and the FIRST match wins, so THIN is decided before FORKED.
      if (thin) { print "THIN"; exit }
      # THE WHOLE SECTION IS ONE STRING, so a mark WRAPPED across a line break still matches. Measured
      # over the tracked corpus: TWELVE specs carry a mark that wraps, which is the house
      # style at its line width — a line-by-line match reported every one of them as unresolved.
      blob = ""
      for (i = 1; i <= nf; i++) blob = blob " " fl[i]
      gsub(/[[:space:]]+/, " ", blob)   # the squeeze the hygiene reader does, so the two agree by construction
      any_mark = (blob ~ /RESOLVED \((owner|agent), [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9](, delegated)?\)/)
      items = 0
      for (i = 1; i <= nf; i++)
        if (fl[i] ~ /^[-*][[:space:]]/ || fl[i] ~ /^###[[:space:]]/) items++
      # WHY THIS IS NOT A PER-ITEM WALK, stated because the obvious tightening is WRONG here and was
      # measured wrong. A per-item walk needs to tell a FORK bullet from an OPTION bullet, and this
      # corpus does not distinguish them: of 287 section-8 bullets, 69 carry descriptive labels, and
      # among those are both resolved forks and genuinely OPEN ones. A label-shape discriminator
      # therefore UNDER-counts — it would let a real open fork pass, which is worse than the
      # over-counting it replaces. Measured: a per-item walk called a RESOLVED fork FORKED on a live
      # tracked spec, because its three option bullets each demanded their own mark.
      #
      # So the reader grades what it CAN: a first line that merely CONTAINS the resolution word no
      # longer resolves the section — that was the live defect, a section announcing a fork was NOT
      # resolved reading as resolved — and a section with items and no conforming mark ANYWHERE is
      # unresolved. What it cannot see is an unresolved fork sitting below an honest-looking `none`
      # line; that needs section 8 to have a regular shape, and making it regular is a scope change
      # rather than a predicate change. Parked, not implied away.
      lf = tolower(forkline)
      # AN EMPTY SECTION IS A REFUSAL, not a pass — the ratified fork, and TEMPLATE-SPEC names both
      # readers: "A section 8 with neither an item nor a `none` form is a refusal, not a pass." The
      # hygiene reader already refused it; this one printed READY, so the two readers the spec pairs
      # disagreed on the one case that distinguishes a resolved section from a hollow one.
      if (items == 0) {
        if (lf ~ /^none/ || lf ~ /^n\/a/) print "READY"; else print "FORKED"
      } else {
        # WITH ITEMS PRESENT THE OPENING LINE DOES NOT VOTE. It used to, and `/^none/` is an
        # UNANCHORED prefix on a lowercased line, so "None of the forks below are resolved." - a
        # sentence saying the exact opposite - read as a none-form and resolved the section. The
        # hygiene reader rejected that one only by accident of case, and aligning the two on case
        # aligned them on the WRONG behaviour. A section with items is resolved by a MARK or not at
        # all. Measured over the corpus: no terminal spec at or after FORK_MARK_CUTOFF loses by this,
        # and the 12 older ones that would are already exempt by that cutoff.
        if (any_mark) print "READY"; else print "FORKED"
      }
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
  # TOOL-dHonouredPark-1 S5. `region` REFUSES a malformed pair with exit 3, and this function used
  # to pipe it straight into `grep | sort` and take the LAST stage's status - so the refusal was
  # discarded and whatever `region` printed BEFORE failing was parsed as ids. A malformed pair
  # yielded a partial id list and no error at all.
  #
  # PIPEFAIL IS NOT THE FIX, and it was measured before this was written rather than after. A
  # well-formed but EMPTY pair is LEGAL - it means the build plans exactly its specced units - and
  # `grep -oE` exits 1 on no match, so `set -o pipefail` would turn the legal case into a refusal.
  # The status is tested on `region` ALONE instead.
  local slug="$1" rel _reg; rel=$(readme_of "$slug")
  [ -f "$rel" ] || return 0
  grep -qF -- "$ROSTER_OPEN" "$rel" || return 0
  _reg=$(region "$rel" "$ROSTER_OPEN" "$ROSTER_CLOSE" 2>/dev/null) || return 3
  printf '%s\n' "$_reg" | grep -oE "[A-Z]+-$slug-[0-9]+" | sort -u
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
  # THE STATUS IS TESTED. `set -u` is on and `set -e` is not, so a status this caller did not read
  # would change nothing observable however carefully roster_ids returned it - which is the defect
  # round 2 found in S5's first draft: the item would have gone green over a surviving vacuous pass.
  #
  # The `[ -n "$want" ] || return 0` guard that stood here is GONE. With the pair mandatory on every
  # tracked build README it is unreachable, and it was measured INERT anyway: `comm` over an empty
  # side emits one blank line, which command substitution strips to length 0 and `for` word-splits
  # to zero iterations. Deleted because it is dead, not because deleting it changes behaviour.
  local want have; want=$(roster_ids "$1") || return 3
  have=$(spec_ids "$2")
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
  # TOOL-dHonouredPark-4 S5. The ABSENT case no longer falls through. It used to be guarded away by
  # the `grep -qF` below, so a README with no units region at all got the old spec-derived listing
  # while a MALFORMED one refused - and a silent fall-back restores the divergence this unit removes
  # exactly when the tree is in the state most likely to hide it.
  if ! grep -qF -- "$UNITS_OPEN" "$_rmp" 2>/dev/null; then
    fail 42 "the build README carries no units marker at all, and this verb takes its unit SET and ORDER from that region: $_rmp · repair: the --write mode of tools/memory-tree/gen_build_index.py"
    return 1
  fi
  if ! region "$_rmp" "$UNITS_OPEN" "$UNITS_CLOSE" >/dev/null 2>&1; then
    fail 42 "the build README carries a units marker but not exactly one well-formed pair, so the roster this verb would join against is not a single slice: $_rmp"
    return 1
  fi
  # R2-M3 — THE ROSTER IS RESOLVED HERE, beside the other region guards and before a single row is
  # printed. It used to sit after the whole listing, so a malformed pair produced a complete-looking
  # table and only then a refusal; and the arm that was meant to catch that asserted the refusal TEXT
  # without looking at the table above it, which is how it shipped.
  local _rids
  if ! _rids=$(roster_ids "$slug"); then
    fail 42 "the build README carries a roster marker but not exactly one well-formed pair, so the id set this line reports is not a single slice: $_rmp"
    return 1
  fi
  specs=$(git ls-files "$dir/spec/*.md" 2>/dev/null)
  if [ -z "$specs" ]; then
    fail 19 "no tracked spec under this build, so every planned unit is MISSING; the README roster is what this verb reads to say WHICH, and with no spec beside it there is nothing to join that roster against: $dir/spec"
    return 1
  fi
  # S6 - THE TWO `NOT A UNIT` DIAGNOSTICS, reported FIRST and from the spec files, because the region
  # cannot carry them: `render_region` emits rows only for specs whose status header parsed, so a file
  # with none has no row to appear in. Five tracked specs produce the first row today and ZERO produce
  # the second, which the driver's own comment below already states - so the second is armed by
  # fixture or not at all.
  # R3-M4 — the renderable count comes from `spec_ids`, which is this driver's OWN answer to "does
  # this spec parse as a unit" and whose comment says it exists so two callers cannot disagree. The
  # inline count that stood here was a third spelling of that predicate, looser than the generator's,
  # so the stale-region refusal could name an inert repair. Latent — zero of 277 tracked specs
  # disagree today — and removed rather than left to be discovered by the first one that does.
  local _sid _renderable
  _renderable=$(spec_ids "$dir" | grep -c . || true)
  for spec in $specs; do
    st=$(awk '{ sub(/\r$/,"") } /^\*\*Status:\*\* [A-Z]+ / { print $2; exit }' "$spec")
    if [ -z "$st" ]; then
      printf '%-34s %-11s %s\n' "$(basename "$spec")" "-" "NOT A UNIT (no status header)"
      continue
    fi
    _sid=$(awk '{ sub(/\r$/,"") } /^# [A-Za-z0-9][A-Za-z0-9-]* / { print $2; exit }' "$spec")
    [ -n "$_sid" ] || printf '%-34s %-11s %s\n' "$(basename "$spec")" "$st" "NOT A UNIT (heading id does not parse)"
  done

  # R2-H2 — the EMPTY-REGION guard, ordered HERE and conditioned on `_renderable`. Above the two
  # passes it refused on 7 of 63 live builds — every build whose specs render no row at all — and
  # named `--write` as the repair on trees where `--check` was already clean, so the remedy was
  # provably inert. A refusal whose fix cannot change anything is worse than the vacuity it replaced.
  # Now it fires only where a spec that WOULD render a row exists and the region has none, which is
  # the stale-render case it was written for; where nothing renders, the NOT A UNIT rows above ARE
  # the answer.
  local _rows; _rows=$(unit_rows "$_rmp")
  if [ "$_renderable" -gt 0 ] && [ -z "$_rows" ]; then
    fail 42 "the generated units region carries no unit rows but this build has specs that would render them, so the region is stale: $_rmp · repair: the --write mode of tools/memory-tree/gen_build_index.py"
    return 1
  fi
  # S1/S2 - the SET and its ORDER come from the REGION, which is rendered in BUILD ORDER. `--status`
  # already reads it, so this makes three verbs agree instead of two disagreeing with a third. The
  # join key is the ID, never the row's LINK: `unit_rows` pattern-matches the link and never opens it,
  # and the harness fixture links a bare `one.md` while `mkspec` writes a dated filename, so a
  # link-resolving join would break every arm that reads this output.
  # ONE id per ROW, not one per MATCH. A rendered row spells its id twice - once as the link's text
  # and once inside the link's target - so a `grep -o` over the whole region emits every unit twice.
  # Measured on the real corpus before this was written: the listing doubled.
  #
  # SCOPED TO $slug, which the closing review found: `[A-Za-z]+` admits no DIGIT in the slug
  # segment, and every other reader here does - check_slug, the folder grammar, the heading
  # parser. A build slugged `tRun2` listed ZERO units beside a roster line reporting one, the two
  # halves of one report contradicting each other on screen. Scoping fixes the digit case and the
  # not-scoped case together, and matches `unit_ids_of` rather than adding a third spelling.
  # R2-H1 — COLLECTED FIRST, so "the region had rows and none of them named a unit of this build" is
  # a state this verb can SEE. Iterating the substitution directly made it indistinguishable from an
  # empty region, and the verb answered `next: none - every tracked spec is terminal` at exit 0 — a
  # false all-clear on the one verb an agent reads to pick up work.
  local _ids _graded=0
  _ids=$(printf '%s
' "$_rows" | while IFS= read -r _row; do
        printf '%s
' "$_row" | grep -oE "[A-Z]+-$slug-[0-9]+" | head -1
      done)
  if [ -n "$_rows" ] && [ -z "$_ids" ]; then
    fail 42 "the generated units region carries rows but none names an id of this build, so this verb has no unit set to grade: $_rmp"
    return 1
  fi
  for id in $_ids; do
    spec=""
    for _c in $specs; do
      _sid=$(awk '{ sub(/\r$/,"") } /^# [A-Za-z0-9][A-Za-z0-9-]* / { print $2; exit }' "$_c")
      [ "$_sid" = "$id" ] && { spec="$_c"; break; }
    done
    # S7 - a region row whose id no tracked spec defines. It cannot arise while the region is rendered
    # FROM those specs, but S1 makes it representable and a row that fell through would be invisible.
    # Distinct from the authored pair's MISSING, which is about a PLANNED unit nobody has specced.
    if [ -z "$spec" ]; then
      printf '%-34s %-11s %s\n' "$id" "-" "NO TRACKED SPEC (rendered row without one)"
      continue
    fi
    # The status comes from the spec the id resolved to. Its two unparseable shapes were reported by
    # the S6 pass above and cannot reach here: a row exists in the region only for a spec whose status
    # header parsed, so this branch grades a file already known to be a unit.
    st=$(awk '{ sub(/\r$/,"") } /^\*\*Status:\*\* [A-Z]+ / { print $2; exit }' "$spec")
    state=$(plan_state "$spec")
    case "$st" in CLOSED|WONTDO) state="DONE" ;; esac
    printf '%-34s %-11s %s\n' "$id" "${st:-?}" "$state"
    _graded=1
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
  # The value resolved at the top of this verb, not re-derived. R2-M3: two `$( )` calls here meant two
  # discarded exit-3s, and the guard that replaced them still sat AFTER the listing.
  if [ -n "$_rids" ]; then
    echo "roster: the README roster region, $(printf '%s\n' "$_rids" | grep -c .) id(s); $nmiss with no tracked spec"
  else
    echo "roster: the generated units region, in build order (the authored pair names no id of this build)"
  fi
  # R3-B1 — THE TERMINAL WORDING IS EARNED, not defaulted. "every tracked spec is terminal" was
  # printed at exit 0 over builds where no spec graded as a unit at all, one line below the NOT A
  # UNIT rows saying so. A reader — or an agent picking up work — is told the build is finished.
  if [ -n "$next" ]; then
    echo "next: $next"
  elif [ "$_graded" = 0 ]; then
    echo "next: none - no tracked spec grades as a unit (see the NOT A UNIT rows above)"
  else
    echo "next: none - every tracked spec is terminal"
  fi
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
    # A LANDING EVALUATED IN ANOTHER TREE DOES NOT TRAVEL. `--close` stages the phase and the RUN
    # commits it, so a run that closed in a linked worktree and then merged from the primary tree
    # arrives here carrying the older phase. The refusal was already accurate and named nothing that
    # helps: the recovery is to commit the phase where it was evaluated, or to re-close here, and a
    # run cannot choose between those without knowing which tree holds it. TOOL-dUnstalledConvoy-24.
    _elsewhere=""
    while IFS= read -r _wl; do
      case "$_wl" in "worktree "*) _wp=${_wl#worktree } ;; *) continue ;; esac
      [ "$_wp" = "$ROOT" ] && continue
      [ -f "$_wp/$rel" ] || continue
      case "$(sed -n 's/^phase: //p' "$_wp/$rel" 2>/dev/null | head -1)" in
        LANDING) _elsewhere="$_elsewhere $_wp" ;;
      esac
    done <<WTS
$(GIT worktree list --porcelain 2>/dev/null)
WTS
    if [ -n "$_elsewhere" ]; then
      fail 31 "a run reaches LANDED only from LANDING, because LANDING is the record that --close evaluated the Definition-of-Done set and this verb does not evaluate it a second time: $cur here, and an UNCOMMITTED LANDING is sitting in:$_elsewhere — commit the run-state file there, or re-run --close in this tree"
    else
      fail 31 "a run reaches LANDED only from LANDING, because LANDING is the record that --close evaluated the Definition-of-Done set and this verb does not evaluate it a second time: $cur"
    fi
    return 1
  fi
  check_clean || return 1
  # THE LANDER MARKER, read BEFORE the remote observation. It is the only verb that runs after the
  # push, so this is where the evidence can exist — and it goes first because it is a local file read
  # against a remote round-trip, and because an operator who has not run the lander should be told
  # THAT rather than told about ancestry. Cheapest and most specific first.
  #
  # It carries IDENTITY, not existence: a bare touched file is satisfied by any previous landing, which
  # is the pass-by-finding-anything shape this kit's own Definition of Done was stuck in.
  #
  # AN UNDECLARED KEY DEGRADES rather than refusing, deliberately: an adopter who has not adapted their
  # lander must not be wedged by a key they have never heard of. A DECLARED key whose marker is absent
  # or names another commit IS a refusal, because then the project asked for the observation.
  #
  # RESOLVED AGAINST THE GIT COMMON DIR, exactly as the lander resolves it. The key used to be a
  # tree-relative path, which named a different file in each half - the lander wrote relative to its
  # own top, this verb read relative to ROOT - and could not be written AT ALL from a linked
  # worktree, where `.git` is a file rather than a directory. One resolution rule, spelled the same
  # way on both sides, and the key is now a bare name.
  local _lm_head _lm_gcd _lm_path
  _lm_head=$(GIT rev-parse HEAD)
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
  # THE WITNESS IS THE COMMIT THE TAKEN ARM ACTUALLY VALIDATED. The local arm tests the run's own
  # branch tip against the local default branch and never looks at HEAD; recording HEAD there writes a
  # terminal fact about a commit nothing in this verb examined, and the two differ exactly when the
  # worktree has moved on since the merge — which is the ordinary case, not a corner one.
  local wit="$head"
  [ "$akind" = local ] && wit="$rbtip"

  # THE MARKER IS A REMOTE-ARM OBLIGATION, and gating it here rather than above the arms is the whole
  # of this fix. It used to run BEFORE anchor selection and return on a missing marker, so on exactly
  # the state the local arm exists for - merged into local main, the push did not land HEAD -
  # push-main has not written a marker (it writes one only inside its rc=0 branch) and the run could
  # not reach the fallback at all. Two features that each work, deadlocking in composition.
  #
  # Compared against the WITNESS the taken arm validated, not against HEAD, for the reason the witness
  # itself exists: on the local arm HEAD is a commit this verb never examined.
  if [ "$akind" = remote ] && [ -n "$LANDER_MARKER" ]; then
    # A BARE NAME, and the key says so - so a value carrying a separator is REFUSED rather than joined
    # into a path. Joined, it resolves somewhere the declaration never named, and the lander and this
    # verb can disagree about where while both look like they are following the conf.
    case "$LANDER_MARKER" in
      */*|*"\\"*|.|..) fail 34 "LANDER_MARKER must be a bare NAME resolved against the git common dir, and this value carries a path separator, so the lander and this verb would each join it somewhere the declaration never named: $LANDER_MARKER"
         return 1 ;;
    esac
    _lm_gcd=$(cd "$(GIT rev-parse --git-common-dir 2>/dev/null)" 2>/dev/null && pwd) || _lm_gcd=""
    _lm_path="$_lm_gcd/$LANDER_MARKER"
    # NO SEPARATE REFUSAL FOR AN UNRESOLVABLE COMMON DIR, and that is a deletion rather than an
    # oversight. One was written and could never fire: this driver resolves ROOT with `rev-parse
    # --show-toplevel` at startup and exits when that fails, so by the time this runs the repository
    # is known good and `--git-common-dir` cannot fail. An unarmable branch is an assertion about
    # nothing. What the branch was FOR - not blaming the lander for a fault on this side - is kept by
    # printing the directory this side resolved, so an empty one is visible in the refusal itself.
    if [ ! -f "$_lm_path" ]; then
      fail 34 "the project declares a lander marker and the lander wrote none, so nothing observed this landing and the phase would be a claim rather than a reading. looked in the git common dir this side resolved, which was [$_lm_gcd], for: $_lm_path"
      return 1
    fi
    # AGAINST THE WITNESS, not HEAD. They are the same commit on this arm, which is exactly why the
    # distinction is worth writing down: the gate is scoped to `remote` today, and a future arm that
    # validates something other than HEAD would silently start grading the wrong commit.
    if ! grep -qF -- "$wit" "$_lm_path" 2>/dev/null; then
      fail 34 "the lander marker names a different commit, so it is evidence of an EARLIER landing standing in for this one; re-run the lander or fix what it writes to name the commit this landing records. wanted $wit, marker holds: $(tr -d '\r' < "$_lm_path" | head -1)"
      return 1
    fi
  fi

  set_fact "$rel" witness "$wit" || return 1
  # WRITTEN ON BOTH ARMS AND NEVER DEFAULTED. An absent `landed-anchor` would read as `remote` to any
  # later reader, silently promoting a record to the stronger claim.
  set_fact "$rel" landed-anchor "$akind" || return 1
  # The message names the commit the RECORD carries. It printed `$head` while writing `$wit`, so on
  # the local arm the operator was told one sha and the terminal record kept another.
  head="$wit"
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
verb_abort() { # slug · reason · code
  local slug="$1" reason="$2" code="$3" rel head item ck key
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to abort: $rel"; return 1; }
  # ALREADY FINISHED beats every argument complaint below it. A terminal record is not going to
  # become abortable because the operator supplies a better reason or a halt code, so telling them
  # to supply one sends them to fix a thing that is not the problem. This moved above the argument
  # validation when the code became required; the ordering is the point, not a side effect.
  refuse_if_terminal "$rel" --abort || return 1
  if [ -z "$reason" ]; then
    fail 33 "--abort requires --reason, because an abort with no recorded reason is indistinguishable from a run that simply stopped, and the reason is the only thing the owner gets in place of the turn nobody took"
    return 1
  fi
  # ...and it sits WITH the reason checks rather than after the code ones: it is a fact about the
  # REASON, and grouping it below the code validation made a reason problem report as a code one.
  # A REASON MAY NOT SPELL THE BYPASS FLAG. park() writes it verbatim into the run-state file, and leg
  # check 11 greps that file WHOLE for the declared flag - so a perfectly truthful abort reason ("the
  # lander refused and I would not use it") would red the bar permanently, on a terminal record no
  # verb can rewrite afterwards. Refusing the spelling is cheaper than mangling the operator's prose,
  # and the message says which word to drop.
  if [ -n "$BYPASS_BAN" ] && printf '%s' "$reason" | grep -qF -- "$BYPASS_BAN"; then
    fail 36 "the reason spells the declared bypass flag, and the gate greps this file whole for it, so recording this sentence would red the bar on a terminal record nothing can rewrite; say it without the literal flag: $BYPASS_BAN"
    return 1
  fi
  # THE CODE IS REQUIRED, and it is validated against the effective vocabulary rather than accepted as
  # free text. A reason is for the owner; a code is for everything else — the status line, the resume
  # path and the gate leg all read it by key. Refusing names the legal set, because a validated
  # vocabulary whose refusal does not say what is legal costs the operator a source read.
  # THE LEGAL SET IS BOUND TO A NAME before it reaches either message, and that is not style: the
  # arms gate signs a branch with the LITERAL source text of its `fail` call, so a `$(...)`
  # substitution inside one becomes part of the signature and no runtime arm can ever match it. A
  # plain interpolation at the END of the sentence is the shape that arms.
  local legal; legal=$(halt_codes)
  if [ -z "$code" ]; then
    fail 33 "--abort requires --code, because a single ABORTED terminal says a run stopped and never says why; the reason is prose for the owner and the code is the field every reader joins on: $legal"
    return 1
  fi
  if ! is_halt_code "$code"; then
    fail 33 "--abort names a halt code that is not in the effective vocabulary, and an unvalidated code is free text wearing a field name; declare it in HALT_CODES_EXTRA or use one of these: $legal"
    return 1
  fi
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
  # AN AUTHORED FACT, not a substring of the reason. A reader is a field read rather than a parse, and
  # three readers want it by key. It is a per-run SINGLETON written by a terminal verb, which is the
  # same shape the roster-at-landing fact already has — the in-tree precedent, not an argument by
  # analogy. Append-only history takes a park KIND instead, which is what the review-round unit does.
  set_fact "$rel" halt-code "$code" || return 1
  park "$rel" abort "$slug" "$reason"
  stage_or_fail "$rel" || return 1
  echo "unattended: phase ABORTED · witness $head · halt-code $code · reason recorded as a parked entry"
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
  # the resolved binding, recorded so a later reader can tell WHICH
  # playbook bound the run without re-deriving it, and so the leg has a recorded answer to
  # SECOND-OPINION rather than a value only the driver ever saw. Recorded only in recipe mode:
  # under any other mode there is no binding, and a blank fact would be a key that reads as
  # configured while carrying nothing.
  if [ "${AUTH_MODE:-}" = recipe ]; then
    [ -n "$(fact "$rel" playbook)" ] || set_fact "$rel" playbook "$AUTH_PLAYBOOK" || return 1
    [ -n "$(fact "$rel" pieces)" ]   || set_fact "$rel" pieces   "$AUTH_PIECES"   || return 1
    [ -n "$(fact "$rel" grain)" ]    || set_fact "$rel" grain    "$AUTH_GRAIN"    || return 1
    [ -n "$(fact "$rel" records)" ]  || set_fact "$rel" records  "$AUTH_RECORDS"  || return 1
  fi
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
  local slug="$1" rel p w unit nparked parked unowed nnoted
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
  # DERIVED alternation. This line typed four kinds, so the fifth was a row --status did not
  # recognise at all - the silent-skip shape, one verb over from the gate that bans it.
  nparked=$(grep -cE "^[0-9][0-9-]*T[0-9:]*Z ($(kinds_re "$PARK_KINDS_OWED")) · item " "$rel" 2>/dev/null || true)
  if [ "${nparked:-0}" -gt 0 ] 2>/dev/null; then parked=" · parked $nparked"; else parked=""; fi
  # The rows the owner is TOLD about but owes no answer to, counted apart and printed apart. Folded
  # into `parked`, a run that recorded six of its own acts would read exactly like a run that stalled
  # on six decisions, and the owner would open the file to tell them apart. The field is `noted`
  # rather than any kind's name: the unowed set is DERIVED and holds three kinds, so a label naming
  # one of them would be wrong about the other two the day a merge added them - which is the day
  # this line was written.
  unowed=$(park_kinds_unowed)
  if [ -n "$unowed" ]; then
    nnoted=$(grep -cE "^[0-9][0-9-]*T[0-9:]*Z ($(kinds_re "$unowed")) · item " "$rel" 2>/dev/null || true)
    [ "${nnoted:-0}" -gt 0 ] 2>/dev/null && parked="$parked · noted $nnoted"
  fi
    # The halt code on the status line, when the record carries one. A vocabulary with no reader
    # is decoration, and this kit says so about its own phase writer.
    local hc; hc=$(fact "$rel" halt-code)
    [ -n "$hc" ] && hc=" · halt-code $hc" || hc=""
  printf 'unattended: %s · phase %s · witness %s%s · next %s%s
' "$slug" "$p" "${w:-NONE}" "$hc" "$unit" "$parked"
  [ -n "$w" ] || { fail 11 "the phase carries no witness, and presence is its own refusal: an oracle that skips an unwitnessed claim makes naming no witness the cheapest way to say nothing. Phase: $p"; return 1; }
  return 0
}

verb_resume() { # slug
  verb_status "$1" || return 1
  local rel p; rel=$(runmd_of "$1"); p=$(fact "$rel" phase)
  if is_terminal "$p"; then
    local rhc; rhc=$(fact "$rel" halt-code)
    if [ -n "$rhc" ]; then
      echo "unattended: nothing to resume — phase $p is terminal, and this run FINISHED rather than paused: halt-code $rhc"
    else
      echo "unattended: nothing to resume — phase $p is terminal"
    fi
  else
    echo "unattended: resume at phase $p — read $rel, then continue the first non-terminal unit above"
    # The method path is DERIVED from MEMORY_ROOT, never recorded as a run fact: the authored region
    # carries twelve facts and never restates a derivable one (protocol section 2).
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
  local slug="$1" rel item ck unmet=0 i=0 n ov reason _why
  n=${#OV_ITEMS[@]}
  check_slug "$slug" || return 1
  # THE FREE REFUSALS COME FIRST, and the ordering is the point rather than tidiness. This function
  # used to open with a network round-trip and only then discover that the record was already
  # terminal, or absent — so a close against a finished record paid a full remote observation, and
  # on an unreachable endpoint it paid the whole wall-clock bound, to reach a refusal that needed no
  # network at all. The prologue's own refusals are explicitly NON-FATAL to --close (see below), so
  # nothing downstream depended on it having run first, which is what makes the move safe as well as
  # cheaper.
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 10 "no run-state file, so there is no run to close: $rel"; return 1; }
  refuse_if_terminal "$rel" --close || return 1
  # The SAME observation preflight made, made again here rather than read back from the record the
  # run wrote. Its refusals are not fatal to --close: authorization-reachable simply cannot be met without
  # an anchor, which is the honest outcome and is not overridable.
  # One line BEFORE the network round-trip, so a close that is about to spend one has printed
  # something. It sits with the observation rather than at the top of the verb: a run whose record is
  # already terminal now spends no round-trip, so announcing one would be announcing something that
  # does not happen. The arm that proves the line reads stdout on a LIVE record, which is the case
  # the line exists for.
  echo "unattended: --close $slug - observing the anchor, then evaluating the Definition of Done"
  # S1 - the redirect is GONE. `fail` echoes to stdout, so `>/dev/null 2>&1` destroyed all EIGHT of
  # observe_anchor's named refusals (checks 22-25 and 27-30), and the only surviving output was the
  # bare `authorization-reachable` line - the one item `fail 21` forbids overriding. A wedge with no
  # stated cause and no forward move. `|| true` alone is the form --landed and --preflight already use:
  # the refusals are not fatal to --close, which is why they were suppressed rather than returned on,
  # and that reasoning was always about the STATUS and never about the message.
  observe_anchor || true
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
    case " $DOD_NO_OVERRIDE " in
      *" $ov "*)
        case "$ov" in
          authorization-reachable) _why="an override on the authorization check IS the authorization check" ;;
          *) _why="it is the item that says this run made what the owner asked for, so an override on it is the run certifying its own output" ;;
        esac
        fail 21 "a Definition-of-Done item in the non-overridable set cannot be bought with --override, and --abort is the honest exit when it cannot be met - item and reason follow: $ov, $_why"
        return 1 ;;
    esac
    i=$((i + 1))
  done
  for item in $(dod); do
    item=${item%%:*}; ck=$(checker_of "$item")
    is_overridden "$item" && continue
    # CLEARED BEFORE THE CALL, not only after a print. `dod_met` does not clear it on entry, so an
    # item that says nothing would otherwise inherit whatever the previous item left behind and
    # attribute one item's explanation to another.
    DOD_OUT=""
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
        # The DETAIL, when the item computed one. An agent-attested item is not necessarily
        # detail-free: the parked-decisions count is machine-COMPARABLE even though the surfacing
        # itself is not observable, and this branch used to discard that text — a message written
        # into a channel nobody reads, which is the class this kit refuses by name elsewhere. Printed
        # BEFORE the record-key hint, which stays because it is the remedy for the ordinary case.
        [ -n "${DOD_OUT:-}" ] && printf '%s
' "$DOD_OUT" | sed 's/^/    /'
        DOD_OUT=""
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
        [ -n "${DOD_OUT:-}" ] && printf '%s\n' "$DOD_OUT" | grep -vE '^(GATE (ok|skip) )' | sed 's/^/    /'
        DOD_OUT=""
      fi
    else
      # the playbook-authoring unit - A MET ITEM WITH SOMETHING TO SAY SAYS IT. The piece-scoped items
      # carry a term zero that is MET for every non-recipe run and sets DOD_OUT to announce the skip,
      # under a comment reading "a silent pass is indistinguishable from coverage" - and the print
      # above reached only the UNMET arm, so the announcement went nowhere and the skip was silent.
      # The defect the announcing branch exists to prevent, one level up from where it was written,
      # and found by an acceptance criterion asking to OBSERVE the announcement rather than the code.
      [ -n "${DOD_OUT:-}" ] && printf 'unattended: %s
' "$DOD_OUT"
      DOD_OUT=""
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
  # THE COMMIT IS NAMED because this verb only STAGES the phase. A run that merges from another
  # tree without committing carries the older phase into the merge, and `--landed` then refuses a
  # run whose Definition of Done was in fact evaluated. TOOL-dUnstalledConvoy-24.
  echo "unattended: close OK — every declared DoD item met; phase LANDING. COMMIT the run-state file, then land with: $LANDER"
  return 0
}

# What the driver can honestly answer for each core item. Anything it cannot observe is reported as
# agent-attested and read back from the record, never invented.
dod_met() { # slug · run-state file · item · checker
  local slug="$1" rel="$2" item="$3" ck="$4" rb _pv _pn _pa
  # CLEARED ON ENTRY. This is called in a loop and only some arms assign DOD_OUT, so an arm that set
  # it left its text attached to whichever LATER item happened not to — printing one item's diagnostic
  # as another item's detail. Clearing here means the channel always belongs to the item being graded.
  DOD_OUT=""
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
    pieces-complete|set-checks-recorded)
      # TERM ZERO, and it is first because everything else depends on it. `verb_close` evaluates
      # DOD_CORE for EVERY run with no mode branch anywhere, so an item only a recipe-mode run can
      # satisfy would block --close on every slug- and prompt-mode run in the fleet, on an item whose
      # only exit is --abort. Implemented HERE rather than as a third DOD_CORE field: `checker_of`
      # uses shortest-prefix removal and would route a three-field entry silently down the machine
      # path in both consumers.
      #
      # MET, and it ANNOUNCES the skip. A silent pass is indistinguishable from coverage.
      if [ "$(fact "$rel" mode)" != recipe ]; then
        DOD_OUT="skipped — $item is scoped to recipe-mode runs and this run's recorded mode is $(fact "$rel" mode)"
        return 0
      fi
      _pb=$(fact "$rel" playbook)
      _n=$(fact "$rel" pieces)
      if [ -z "$_pb" ] || [ -z "$_n" ]; then
        DOD_OUT="a recipe-mode run records no playbook or no piece count, so there is nothing to measure this item against: playbook '$_pb' count '$_n'"
        return 1
      fi
      # THE WHOLE PLAYBOOK COMES FROM THE PINNED BASE, not from the working tree. Round-1 HIGH 4
      # found this arm handing `--counts` a PATH the leg read off disk while `set-checks-recorded`
      # below it read the BASE blob; the fix pinned `grain` and `records` and LEFT `piece_checks` on
      # disk, so one uncommitted line still moved a piece from `unchecked` to `verified` — on the
      # item that takes no override. Round 2 caught that inside the commit that introduced it.
      #
      # A SHA, not a field list. A per-field pin is a list somebody has to remember to extend, and
      # the evidence that nobody does is this arm's own history.
      # THE PIN IS BOUND AND CHECKED BEFORE THE CALL. `fact` returns empty with exit 0 for an
      # absent key, so passing it straight through let an absent BASE reach the leg as "no pin" —
      # which silently read the working tree. The leg refuses that now too; both ends, because this
      # is the third round in which an optional pin turned out to be the whole defect.
      _at=$(fact "$rel" base)
      if [ -z "$_at" ]; then
        DOD_OUT="this run's record pins no BASE, so the playbook this item measures could only be read from the working tree - the file the run itself can edit: $rel"
        return 1
      fi
      # CAPTURED ONCE, SELECTED FROM. Piping the leg straight into `grep -m1 '^pieces='` threw away
      # every refusal it prints — an unresolvable sha, an undeclared records root, a git failure and
      # an unterminated declaration all arrived here as the same empty string, and the generic
      # sentence below named none of them. The `gates-green` arm eleven lines up carries this exact
      # lesson in its own comment: SURFACED, not discarded.
      _raw=$(bash "$KIT_DIR/check-playbook.sh" --counts "$_pb" "$slug" "$_at" 2>&1)
      _counts=$(printf '%s\n' "$_raw" | grep -m1 '^pieces=')
      # THE LEG'S EXIT STATUS IS DELIBERATELY NOT READ HERE, and that is a measurement rather than an
      # oversight. `--counts` runs the SAME per-playbook validity checks the full leg does, so the leg
      # exits non-zero for a curator, a step floor or a tag-grammar finding — none of which say
      # anything about whether the census is trustworthy. Blocking on the status was written, run, and
      # reverted: it turned nine specific DoD refusals into one generic sentence, because the driver's
      # own fixture playbook declares a step floor it cannot meet and the leg has always red on it.
      #
      # THE TWO REFUSALS THAT DO INVALIDATE A CENSUS ALREADY REACH THIS CALLER, by two different
      # routes and neither of them the exit status. An unparseable `piece_checks` makes the leg
      # `continue` past that playbook, so no `pieces=` line is printed at all and the missing-count
      # branch below fires with the leg's own words attached. An unparseable `set_checks` is refused by
      # `set-checks-recorded` reading the same blob directly, one item down. Check 28a is what keeps
      # that second claim true: it enumerates every call site of a parser that can refuse and reds one
      # that drops the status, which is the rule this item's sibling broke.

      # SELECTED BY SHAPE, never by position. `head -1` took whatever the leg printed first, so any
      # note reaching stdout made every field below parse to that line's first word — the parse
      # cannot fail, it just yields nonsense, and the close then blocks on a fabricated count.
      if [ -z "$_counts" ]; then
        DOD_OUT="the piece enumerator produced no machine-readable count line, so there is no population to measure this item against and a parsed value here would be invented: $_pb"
        # THE ENUMERATOR'S OWN WORDS, when it had any. Without this the operator learns only THAT the
        # count is missing and has to re-run the leg by hand to learn why.
        _why=$(printf '%s\n' "$_raw" | grep -m1 'FAILED' || true)
        [ -z "$_why" ] || DOD_OUT="$DOD_OUT
    $_why"
        return 1
      fi
      _pc=${_counts#pieces=}; _pc=${_pc%% *}
      _vc=${_counts#*verified=}; _vc=${_vc%% *}
      _fc=${_counts#*failed=}; _fc=${_fc%% *}
      _sc=${_counts#*stale=}; _sc=${_sc%% *}
      _uc=${_counts#*unrecorded=}; _uc=${_uc%% *}
      _xc=${_counts#*unchecked=}; _xc=${_xc%% *}
      if [ "$item" = pieces-complete ]; then
        # TERM 1 - the VACUITY GUARD, and it is ordered before term 2 for `build-complete`'s reason:
        # "every piece is verified" is vacuously true over no pieces at all.
        if [ "${_pc:-0}" -eq 0 ]; then
          DOD_OUT="this run produced no piece under the playbook's declared grain, and 'every piece is verified' is vacuously true over none of them, so completeness cannot be read from it: $_pb"
          return 1
        fi
        [ "${_sc:-0}" -eq 0 ] || { DOD_OUT="a piece this run produced is STALE - its record describes bytes the piece no longer has, so the verdict on it is about a different file: $_sc stale"; return 1; }
        # M7 (round-1 diff review): THERE IS NO `unrecorded` TERM, and its absence is the honest
        # state rather than an omission. `--counts` run-scoped derives membership FROM the records,
        # so a piece with no record belongs to no run and is excluded before it can be counted — the
        # enumerator says so in its own comment. This arm therefore read `_uc`, which is structurally
        # always zero here, under a message that reads as enforcement. Term 3's count comparison
        # catches the same condition and can actually fire. A branch no fixture can reach is the
        # shape this kit gates against everywhere else.
        # TERM 2 - PROVENANCE and DONENESS are two questions. `verified` requires the hash join AND
        # every declared leg recording PASS, which is what makes "its declared legs green" implemented
        # rather than merely cited.
        [ "${_fc:-0}" -eq 0 ] || { DOD_OUT="a piece this run produced records a FAILING leg verdict, so its declared checks ran and one of them said no: $_fc failed"; return 1; }
        # TERM 2b - UNCHECKED. A piece whose record names no verdict for a leg the playbook DECLARES
        # is not verified and never was: before this term the census tested for the ABSENCE of a FAIL,
        # so a record carrying no verdict at all counted as verified and this item certified pieces
        # nothing had checked. An explicit NA satisfies a declared leg; an absent row does not.
        [ "${_xc:-0}" -eq 0 ] || { DOD_OUT="a piece this run produced records no verdict for a leg its playbook DECLARES, so the check was never run and 'verified' would be a word about provenance alone: $_xc unchecked"; return 1; }
        # TERM 3 - the COUNT, against the number the owner asked for at BASE.
        [ "${_vc:-0}" -eq "${_n:-0}" ] || { DOD_OUT="this run's verified piece count is not the count its build README asked for at the pinned BASE - verified against requested: $_vc against $_n"; return 1; }
        DOD_OUT=""; return 0
      fi
      # set-checks-recorded. It reads the VERDICTS and not merely their existence: the sibling item it
      # was modelled on asserts a bound review EXISTS because a prose verdict grammar cannot be
      # anchored, and that limit does not transfer here - a set check is a declared leg with a binary
      # anchored verdict, so declining to read it shipped the exact green this unit exists to prevent.
      # THE BLOB, READ ONCE AND ASSERTED. M2 (round-1 diff review): both extractions below came from
      # separate `GIT show` calls with stderr discarded, so a wrong path, a wrong base or a swallowed
      # failure ALL yielded the empty string — which the `case` immediately read as "declares
      # nothing" and returned MET. A probe that cannot move must say so, and the sibling arm has
      # exactly that assertion, so the asymmetry was internal and the coverage accidental.
      _blob=$(GIT show "$(fact "$rel" base):$_pb" 2>/dev/null)
      if [ -z "$_blob" ] || ! printf '%s\n' "$_blob" | grep -q '^```toml'; then
        DOD_OUT="the playbook does not resolve at the pinned BASE or carries no declaration block there, so this item would read an empty set_checks and certify set coverage over a playbook nothing could read: $_pb"
        return 1
      fi
      _rr=$(declared_scalar "$_blob" records)
      # M1: the escape is matched against a TRIMMED value. It compared RAW text, and the line the
      # kit's own template ships - `set_checks   = []    # the checks that run over ALL N…` - does not
      # equal `[]`, so an author who declares none and keeps the template's own comment was told they
      # declared some, on a run with nobody present to make the call. The `_rr` extraction one line up
      # already trimmed; the inconsistency was between two lines of one arm.
      #
      # The comment strip requires WHITESPACE before the `#`, so a legal `["a#b"]` survives it.
      # THE REFUSAL IS READ. Round 4's second blocker: this was a bare assignment, so the rc 2 the
      # round-3 fold added arrived as empty stdout, the `''` alternative below matched it first, and
      # a declaration the parser could not read returned MET with no record, no verdict and no
      # override entry. Two of the parser's three call sites branched on the status and the commit
      # message claimed all three did. Check 28 now counts them.
      if ! _declared=$(declared_list "$_blob" set_checks); then
        DOD_OUT="the playbook at the pinned BASE opens a set-scoped check list it does not close on the same line, so this item would read the declared null and certify set coverage over a declaration nothing could parse: $_pb"
        return 1
      fi
      # HIGH 3 (round-3): the declared null is the WORD `none`, not any value starting with it. A
      # set check named `nonempty-rows` read as "declares nothing" and this item returned MET with no
      # record, no verdict and no override entry.
      case "$_declared" in
        ''|none|'none '*|none[!A-Za-z0-9-]*) DOD_OUT=""; return 0 ;;
      esac
      # M2, second half: with checks DECLARED and no records root, `_rr` was empty and `_set`
      # degenerated to the absolute path `/set-<slug>.md`, so the item red naming a path outside the
      # repository — a true refusal for a false reason, which sends the reader to the wrong file.
      if [ -z "$_rr" ]; then
        DOD_OUT="the playbook declares set-scoped checks and no records root at the pinned BASE, so a set verdict has nowhere to be written that this item could read: $_pb"
        return 1
      fi
      _set="$_rr/set-$slug.md"
      [ -f "$_set" ] || { DOD_OUT="the playbook declares set-scoped checks and this run recorded no set verdict, so the population a per-piece review structurally cannot see went unmeasured: $_set"; return 1; }
      if grep -q '^leg .* · verdict FAIL$' "$_set"; then
        DOD_OUT="a set-scoped check recorded a FAILING verdict, and these are the checks that see what a per-piece review cannot - a monoculture passes every piece and fails here: $_set"
        return 1
      fi
      # THE JOIN, against the DECLARED set. Round-1 HIGH 1: this arm required a set record to exist
      # and to carry no FAIL, so ONE `NA` on a leg the playbook never declared satisfied it while the
      # declared checks went unrun - the same hole as the per-piece blocker, one population up, under
      # a comment claiming it "reads the VERDICTS and not merely their existence". An explicit NA
      # satisfies a declared check; an absent row does not.
      _smiss=""
      for _sl in $_declared; do
        grep -qxF -- "leg $_sl · verdict PASS" "$_set" && continue
        grep -qxF -- "leg $_sl · verdict NA" "$_set" && continue
        _smiss="$_smiss $_sl"
      done
      if [ -n "$_smiss" ]; then
        DOD_OUT="the playbook declares a set-scoped check this run's set record carries no verdict for, so the population a per-piece review structurally cannot see went unmeasured under a record that looks complete - declared and unrecorded:$_smiss in $_set"
        return 1
      fi
      # L1 (round-1 diff review): the SET IDENTITY, compared. `record_set` writes the ordered member
      # hashes and its own comment names a `superseded` state — a set verdict beside a stale member
      # list is a verdict about a different set — and nothing anywhere read the line. The reachable
      # path is ordinary: record a set PASS, then re-record any piece, which re-stamps that piece's
      # hash, and the verdict now describes a set that no longer exists. Derived the same way the
      # writer derives it, so the two cannot disagree about what the set IS.
      _live=$(for _r in $(GIT ls-files -- "$_rr/*.md"); do
                [ "$(sed -n 's/^run: //p' "$_r" | head -1)" = "$slug" ] || continue
                sed -n 's/^hash: //p' "$_r" | head -1
              done | LC_ALL=C sort | tr '\n' ',' | sed 's/,$//')
      _rec=$(sed -n 's/^set: //p' "$_set" | head -1)
      if [ "$_rec" != "$_live" ]; then
        DOD_OUT="the set verdict describes a SUPERSEDED set - its recorded member list is not this run's pieces as they now stand, so a passing set check was taken over a population that has since changed: $_set"
        return 1
      fi
      DOD_OUT=""; return 0 ;;
    landed-via-lander)
      # THE NARROW CLAIM, stated honestly, and the redundant grep is GONE. This asserted three facts:
      # that LANDER is declared, that BYPASS_BAN is declared, and that the record does not name the
      # flag. The third duplicates leg check 11 inside the same close — two answers to one question —
      # and the first two only say the conf parsed. So the item cannot fail for anything the run DID,
      # and it says so now rather than implying a check it does not run.
      #
      # THE REAL OBSERVATION IS NOT HERE, and that is a sequencing fact rather than a compromise: this
      # predicate runs inside `--close`, which happens BEFORE the landing the item is named for. A
      # marker written by the lander cannot exist yet, so requiring one here would make the item
      # unsatisfiable by construction — the class this build has already fixed three times. The
      # observation lives in `--landed`, the only verb that runs after the push.
      if [ -z "$LANDER" ]; then
        DOD_OUT="the project declares no LANDER, so there is no landing command this item could be about"
        return 1
      fi
      return 0 ;;
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
      # THE STATUS IS READ HERE TOO. TOOL-dHonouredPark-1 taught `roster_ids` to refuse a malformed
      # pair with exit 3 and taught `missing_units` to propagate it — and then this caller took the
      # value into a bare assignment and never looked, so the refusal died one hop from the term it
      # exists to protect. `set -e` is off; an unread status changes nothing anywhere.
      if ! _bcmiss=$(missing_units "$slug" "$M/builds/$slug"); then
        DOD_OUT="the build README's authored roster pair is absent or malformed, so the planned-vs-specced join this term makes cannot be made: $(readme_of "$slug")"
        return 1
      fi
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
      # STILL AGENT-ATTESTED — no machine can observe a wrap-up — but "I surfaced them" becomes "I
      # surfaced N, and the record holds N". The value is read off the SAME key rather than from a new
      # authored fact, because the existing predicate already tolerates trailing text after the
      # yes-or-true, so a richer value costs no new fact and does not move the authored region's
      # count pin. Omitting the number keeps the old behaviour exactly, so nothing that attested
      # before this landed becomes red.
      grep -qE '^parked-surfaced: (yes|true)' "$rel" || return 1
      _pv=$(fact "$rel" parked-surfaced)
      case "$_pv" in
        *[0-9]*) ;;
        *) return 0 ;;   # no count offered: the attestation stands as it always did
      esac
      _pn=$(printf '%s' "$_pv" | grep -oE '[0-9]+' | head -1)
      # The SURFACED class only, and the qualifier is load-bearing: a count inflated by `history`
      # lines would report the opposite of what it is for.
      _pa=$(grep -cE "^[0-9][0-9-]*T[0-9:]*Z ($(printf '%s' "$PARK_KINDS_OWED" | tr ' ' '|')) · item " "$rel" 2>/dev/null || true)
      # THE CLOSE VERB'S OWN OVERRIDE PARKS NEED NO ARITHMETIC, and getting that wrong once is why
      # this comment is here. They are appended AFTER the Definition of Done is evaluated, so at the
      # moment this predicate runs the record holds exactly the N the agent should have attested. The
      # exclusion is a property of the ORDERING. Subtracting them as well double-counts and makes the
      # honest case unsatisfiable — measured: a fixture attesting the true count then failed, which is
      # precisely the defect the spec describes, reproduced while implementing the warning about it.
      if [ "$_pn" != "$_pa" ]; then
        DOD_OUT="the attested count of surfaced parked decisions does not match the record: attested $_pn, and this run-state file holds $_pa in the surfaced class (the overrides this close is about to write are excluded, because the Definition of Done is evaluated before they are appended)"
        return 1
      fi
      return 0 ;;
    *)  # a PROJECT item the kit knows nothing about: it is attested unless the project says otherwise
      grep -qE "^$item: (yes|true)" "$rel" ;;
  esac
}

# S11 - the KIND is an argument, because this helper had the override grammar HARDCODED and exactly one
# caller. Routing --abort's reason through it unchanged would have written "override · item …" into the
# parked region, and the build method derives the owner's open/parked row from parked entries "plus any
# recorded DoD override" - so an abort would have arrived in the one turn the owner gets, wearing the
# label of a Definition-of-Done override that never happened.
# ---------------------------------------------------------------- the DECLARED-LIST parse, ONCE
# A TOML list value from the declaration block -> its members, space-separated. THREE call sites had
# three spellings of this, which is why the trailing-comment strip landed in two of them and not the
# third: round 1 fixed `set_checks`, the fold added `piece_checks` seventy-five lines away without it,
# and the kit's OWN template ships `piece_checks = []    # the checks that run over ONE piece.` — a
# line that word-splits into eight phantom legs and grades every piece `unchecked`.
#
# The helper cannot live in a shared file: each kit script is copy-installed standalone. So it is
# inlined once per script and the two copies are compared against each other by a leg check, which is
# the only way two inlined copies stay one answer.
#
# The comment strip requires WHITESPACE before the `#`, so a legal `["a#b"]` survives it.
declared_list() { # body · key -> members space-separated; rc 2 on an unterminated array
  # THE LINE SELECTION LIVES HERE, and that is the whole point. Round 3's blocker: all three call
  # sites did their own `sed … | head -1`, so a LEGAL multi-line TOML array yielded the bare `[`,
  # parsed to the declared null, and every piece carrying no verdict graded `verified` — on the one
  # Definition-of-Done item that takes no `--override`. No attacker needed; an author formatting an
  # array the ordinary way was enough.
  #
  # AN UNARMED PARSE REDS RATHER THAN RETURNING THE DECLARED NULL (charter §7). Spanning the value
  # would be the other honest fix; refusing is cheaper and cannot be wrong about what it did not read.
  # THE COMMENT COMES OFF BEFORE THE TERMINATOR TEST, and the order is the whole fix. Round 4's
  # blocker: this ran the `case` on the RAW line, so a `]` anywhere in a trailing comment satisfied
  # the closed arm, the strip below then reduced the value to a bare `[`, and a legal multi-line
  # array parsed to the DECLARED NULL at rc 0 - the round-3 blocker restored by the commit that
  # fixed it. `piece_checks = [   # one per piece [see section 7]` is ordinary TOML authoring, and
  # the kit's own template puts a trailing comment on every declaration line.
  #
  # THE STRIP REQUIRES WHITESPACE BEFORE THE `#`, so a legal `["a#b"]` survives it. A `#` that IS
  # preceded by whitespace inside a quoted member (`["a", "b #c"]`) now REFUSES rather than
  # corrupting silently - the honest outcome for a line-oriented shell parser that cannot tokenise
  # TOML, and the reason this returns rather than guessing.
  # THE COMMENT COMES OFF THE WHOLE LINE, BEFORE THE KEY IS REMOVED, and the ORDER of those two is
  # the fix. Round 4 moved the strip in front of the terminator test and left it AFTER the key strip,
  # which had already eaten the whitespace the strip needs: `outputs = # globs...` lost `outputs =`
  # first, so the `#` no longer had whitespace before it, survived, and became the VALUE. Measured on
  # the shipped parser, that returned the comment text at rc 0 for every empty-valued declaration -
  # and the round-4 fold had just narrowed the outputs guard to the empty string, so a recipe-mode run
  # declaring no output globs was authorized by the repair.
  #
  # Stripping the whole line first cannot have that ordering hazard: the whitespace before a trailing
  # `#` is still there when the strip runs. A `#` with NO whitespace before it is a member character
  # (`["a#b"]`) and survives, which is the property the strip was written to keep.
  # NORMALISE FIRST, CLASSIFY SECOND, and never the other way round. Every round of this build has
  # broken here and always the same way: a decision taken on the LINE rather than on the TOKEN it is
  # about. `*'['*']'*` asked whether a `]` appeared anywhere; the comment strip asked for whitespace
  # the key strip had already eaten; and the positional closer that replaced them ran BEFORE the trims,
  # so `["a", "b"] ` - one trailing space on a perfectly closed array - was refused at rc 2 and the
  # driver told the author their bracket was unclosed. Three spellings of one mistake, each introduced
  # by the commit fixing the last.
  #
  # So the pipeline below produces a fully normalised VALUE - comment gone, key gone, CR gone, ends
  # trimmed - and nothing is asked about it until it is. A `#` at position zero is then unambiguous:
  # a TOML value cannot begin with one, so it is a comment on a key with no value at all.
  local raw
  raw=$(printf '%s\n' "$1" | grep -m1 -E "^$2[[:space:]]*=" \
        | sed 's/[[:space:]][[:space:]]*#.*$//' \
        | sed "s/^$2[[:space:]]*=[[:space:]]*//" \
        | tr -d '\r' \
        | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')
  case "$raw" in '#'*) raw='' ;; esac
  # AND THE CLOSER IS ANCHORED AT BOTH ENDS. A value is an array only if it STARTS with `[`, so
  # `k = "a[0]"` is not one and is not refused for failing to close; an array that starts is closed
  # only if it ENDS with `]`, so `["a[0]",` refuses instead of silently dropping the members below it.
  case "$raw" in
    '['*']') ;;
    '['*) return 2 ;;
  esac
  printf '%s\n' "$raw" | tr -d '"' \
    | sed 's/^\[//; s/\]$//; s/,/ /g' | tr -s ' ' | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}

declared_scalar() { # body · key -> the scalar it declares, comment/quotes/space stripped
  # THE SIBLING OF `declared_list`, and it selects its own line for that helper's reason: a `head -1`
  # spelled at each call site is a decision nobody reviews again. Round 3, HIGH 6: the list parse was
  # consolidated while five scalar reads stayed ad-hoc, so an adopter who filled the shipped template
  # in place and kept its comments got `grain` parsed WITH the comment — a DEAD PROBE over a tree of
  # real pieces — while `curated = ""    # who ratified…` satisfied the freeze on an unratified
  # playbook.
  #
  # Same copy-inlined discipline as its sibling: each kit script installs standalone and cannot
  # import, so both copies are byte-compared by the leg check that compares that one's.
  # THE COMMENT COMES OFF THE WHOLE LINE FIRST. Same ordering repair as the list parser, same reason:
  # the key strip consumed the whitespace this strip requires, so `curated = # who ratified...` parsed
  # to its own comment and the freeze - fork 4's only machine consequence - passed on an unratified
  # playbook. A `#` with no whitespace before it stays, because that is a value character.
  # THE `#` AT POSITION ZERO, for its sibling's reason: the trailing-comment strip needs whitespace
  # before the `#` and a key with no value at all leaves none, so `k =# note` and `k =#note` came back
  # as their own comment text at rc 0. A TOML value cannot begin with `#`.
  printf '%s\n' "$1" | grep -m1 -E "^$2[[:space:]]*=" \
    | sed 's/[[:space:]][[:space:]]*#.*$//' \
    | sed "s/^$2[[:space:]]*=[[:space:]]*//" | sed 's/^#.*$//' | tr -d '\r' \
    | sed 's/^[[:space:]]*//; s/[[:space:]]*$//' | sed 's/^"//; s/"$//' \
    | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}

kinds_re() { # word-list -> word|word|word
  # DERIVED, never typed. A leading, trailing or doubled space in the source set would otherwise mint
  # an EMPTY alternative, and an empty alternative matches every line: the widest possible predicate,
  # produced by whitespace nobody can see. Unquoted expansion word-splits and drops the empties.
  local out="" w
  for w in $1; do out="${out:+$out|}$w"; done
  printf '%s' "$out"
}
park_kinds_unowed() { # -> the kinds the owner is NOT owed an answer to, by DIFFERENCE
  # A difference rather than a second list, so the two sets cannot disagree. A sixth kind added to
  # PARK_KINDS and not to the owed set appears in the status split automatically instead of becoming
  # a row `--status` counts nowhere.
  local out="" k
  for k in $PARK_KINDS; do
    case " $PARK_KINDS_OWED " in *" $k "*) continue ;; esac
    out="${out:+$out }$k"
  done
  printf '%s' "$out"
}

park() { # file · kind · item · reason · [step]
  # THE STEP IS OPTIONAL AND IT IS NOT LINE-FINAL. `reason` is, and two live readers depend on
  # that: `recorded_waivers` takes the handle as the token between ' · item ' and ' · reason ',
  # and the leg's check 17 recovers an item by stripping a trailing reason. Appending `step`
  # AFTER `reason` would pull it inside both of those matches, so a proposal row could rename the
  # handle a waiver row records. It goes BETWEEN the two fields, where no existing reader looks.
  local step=""
  [ -n "${5:-}" ] && step=" · step $5"
  printf '\n%s %s · item %s%s · reason %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$2" "$3" "$step" "$4" >> "$1"
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

# THE REVIEW LOOP'S BOUND. A round re-arms the loop only if this round's confirmed-blocker count is
# STRICTLY SMALLER than the previous round's; anything else ends it. That is stricter than "the count
# changed", and deliberately so: an oscillating sequence 2, 1, 2 converges under a changed-test and
# never terminates, which is the shape this exists to stop.
#
# WHY A PREDICATE AND NOT A COUNT. Over the tracked review corpus the only exit the method states — a
# literal clean verdict — occurs ZERO times, while BLOCKED occurs dozens of times with no disposition
# anywhere. A round cap does not give a loop an exit; it moves the stall earlier. So the loop exits on
# CONVERGENCE, and every blocker still standing at the exit is PROMOTED to a unit rather than parked.
#
# The verb reports one of four states and refuses none of them at the ceiling: CONVERGED (nothing
# left), NON-CONVERGENT (stop and promote), CEILING (the backstop fired, which is a defect in the
# predicate — reported loudly and survived), CONVERGING (go again).
review_state() { # prior-counts (space separated) · this count -> the state
  local prev="" n=0 c
  for c in $1; do prev=$c; n=$((n+1)); done
  if [ "$2" = 0 ]; then printf 'CONVERGED\n'; return 0; fi
  if [ "$n" -gt 0 ] && [ "$2" -ge "$prev" ]; then printf 'NON-CONVERGENT\n'; return 0; fi
  if [ "$((n + 1))" -ge "$RUNAWAY_CEILING" ]; then printf 'CEILING\n'; return 0; fi
  printf 'CONVERGING\n'
}

# The rounds already recorded for one subject, in order. Derived from the LINE SET — there is no
# round-count fact to parse, and the only grammar split here is the park helper's own output.
review_counts() { # run-state file · subject -> the blocker counts, in order
  awk -v subj="$2" '
    $0 ~ /^[0-9][0-9-]*T[0-9:]*Z review · item / {
      line = $0; sub(/\r$/, "", line)
      i = index(line, " · item "); if (i == 0) next
      rest = substr(line, i + length(" · item "))
      j = index(rest, " · reason "); if (j == 0) next
      item = substr(rest, 1, j - 1)
      if (item != subj) next
      reason = substr(rest, j + length(" · reason "))
      if (match(reason, /blockers [0-9]+/))
        printf "%s ", substr(reason, RSTART + 9, RLENGTH - 9)
    }' "$1"
}

verb_review() { # slug · subject · verdict · blockers
  local slug="$1" subj="$2" verdict="$3" blockers="$4" rel prior state note
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 37 "no run-state file, so there is no run to record a review round against: $rel"; return 1; }
  refuse_if_terminal "$rel" --review || return 1
  [ -n "$subj" ] || { fail 37 "--review requires --subject, because the convergence predicate is per SUBJECT and a round with no subject cannot be sequenced against anything"; return 1; }
  case "|$REVIEW_VERDICTS|" in
    *"|$verdict|"*) ;;
    *) fail 37 "--review names a verdict outside the closed set, and a verdict nothing can compare is prose in a field; legal verdicts: $REVIEW_VERDICTS"; return 1 ;;
  esac
  case "$blockers" in
    ""|*[!0-9]*) fail 37 "--review requires --blockers as a plain integer, because the predicate compares this round's count against the previous one and cannot compare prose"; return 1 ;;
  esac
  if [ -n "$BYPASS_BAN" ] && printf '%s' "$subj" | grep -qF -- "$BYPASS_BAN"; then
    fail 37 "the subject spells the declared bypass flag, and the gate greps this file whole for it, so recording this round would red the bar on a record nothing can rewrite; name the subject without the literal flag: $BYPASS_BAN"
    return 1
  fi
  # THE ROW GRAMMAR IS park()'s, AND SO ARE ITS GUARDS. This verb was the fifth caller of park() and
  # the only one screening nothing but the bypass flag: a newline in the subject forges an arbitrary
  # parked row — a `decision` row among them, which inflates the very count `parked-decisions-surfaced`
  # is compared against — and a subject spelling the reason separator silently re-keys the group,
  # because both readers split on the FIRST occurrence.
  #
  # Spelled here rather than lifted into a helper shared with --park because check-arms discovers a
  # branch by its LITERAL check number; a helper taking the code as a parameter makes every branch
  # inside it invisible to the tool that proves these are armed.
  if [ "$(printf '%s' "$subj" | wc -l)" -ne 0 ]; then
    fail 37 "the review subject contains a newline, and park() appends ONE line that the gate parses line-wise, so this would forge a second parked row nothing wrote"
    return 1
  fi
  case "$subj" in
    *" · "*) fail 37 "the review subject spells the record's own field separator ' · ', which re-keys the round's group and makes the row unparseable by the check that reads it: $subj"; return 1 ;;
  esac
  prior=$(review_counts "$rel" "$subj")
  # A subject whose group already ENDED does not take another round. The loop stopped; recording more
  # rounds against it would make the sequence say the opposite of what happened.
  # TWO FIXES IN ONE LINE. CEILING is terminal — the leg's own `term` set is all three, and omitting
  # it here accepted a round AFTER the backstop fired, which the leg then reds on permanently, on an
  # append-only record no verb can rewrite. And the subject is matched with -F: interpolated into an
  # ERE, a subject carrying `(` MISSED its own recorded terminal line and one carrying `.`
  # over-matched into a spurious refusal. review_counts compares the item EXACTLY in awk, so as a
  # regex here the two readers of one field disagreed on what "the same subject" means.
  # SCOPED TO `review` ROWS, and to the REASON field. The -F rewrite that removed the regex
  # injection also removed both qualifiers the old predicate had: any parked kind carrying the same
  # subject matched, and an exit token appearing anywhere on the line counted - including inside a
  # subject or a park reason that merely quotes one. Both are restored, with -F still doing the
  # subject comparison so the subject is never a pattern.
  if grep -E '^[0-9][0-9-]*T[0-9:]*Z review · item ' "$rel" 2>/dev/null      | grep -F -- " · item $subj · reason "      | sed 's/.* · reason //'      | grep -qE '(CONVERGED|NON-CONVERGENT|CEILING)'; then
    fail 37 "this subject already carries a terminal review round, so the loop ended for it and another round would rewrite that history: $subj"
    return 1
  fi
  state=$(review_state "$prior" "$blockers")
  note=""
  case "$state" in
    CONVERGED|NON-CONVERGENT) note=" · $state" ;;
    CEILING) note=" · CEILING" ;;
  esac
  # THE TERMINAL LINE is the exit token written into the same free-text reason, after the verdict and
  # the count. No new field, no new grammar, no new authored fact: an append-only history of rounds is
  # what a park KIND is for, and the sibling unit takes the FACT route for a per-run singleton instead.
  park "$rel" review "$subj" "verdict $verdict · blockers $blockers$note"
  stage_or_fail "$rel" || return 1
  case "$state" in
    CONVERGED)      echo "unattended: review $subj · round $(( $(printf '%s' "$prior" | wc -w) + 1 )) · $verdict · blockers 0 · CONVERGED — the loop is done for this subject" ;;
    NON-CONVERGENT) echo "unattended: review $subj · round $(( $(printf '%s' "$prior" | wc -w) + 1 )) · $verdict · blockers $blockers · NON-CONVERGENT — the count did not shrink, so the loop STOPS here and every blocker still standing is PROMOTED to a unit of this build, specced at its tier and built. Not parked, not waived, not re-reviewed" ;;
    CEILING)        echo "unattended: review $subj · round $(( $(printf '%s' "$prior" | wc -w) + 1 )) · $verdict · blockers $blockers · CEILING — the runaway backstop fired at $RUNAWAY_CEILING rounds and THE CONVERGENCE PREDICATE DID NOT TERMINATE, which is a defect in the predicate rather than a routine outcome. The run promotes and lands anyway; record this in the build README, because a fact that lives only in a transcript is a fact nobody reads" ;;
    *)              if [ -z "$(printf '%s' "$prior" | tr -d '[:space:]')" ]; then
                      echo "unattended: review $subj · round 1 · $verdict · blockers $blockers · CONVERGING — the first round for a subject has no predecessor to shrink against, so the loop arms"
                    else
                      echo "unattended: review $subj · round $(( $(printf '%s' "$prior" | wc -w) + 1 )) · $verdict · blockers $blockers · CONVERGING — smaller than the round before it, so the loop may re-arm"
                    fi ;;
  esac
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

# the proposal-kind unit - the FIFTH parked kind, and the only one a pass writes for the OWNER's
# benefit rather than its own. A `recipe`-mode run follows a playbook to the letter, so the one thing
# it must not do is improve that playbook mid-run: a run that rewrites the checklist it is graded by
# has no rules left. What it CAN do is say what it would change, joined to the step that provoked it,
# and leave the amendment to a separate authoring run.
#
# A KIND and not a register, which the owner ratified (spec F1). The close blocks on NO parked kind -
# measured against `dod_met` and `--abort`, not assumed - so a proposal is non-blocking already and
# needs no Definition-of-Done item of its own. What surfaces it at the wrap-up is an ATTESTATION,
# `parked-decisions-surfaced`, and the spec says so plainly rather than calling it a derivation.
#
# The guards are verb_park's, REUSED and widened to the new field rather than re-argued. Each exists
# because of a recorded defect, and the STEP is a third place every one of them can be broken: a
# newline forges a row, the separator makes the row unparseable by the check that grades it, and the
# bypass flag reds the bar on a record no verb can rewrite.
verb_propose() { # slug · item · step · reason
  local slug="$1" item="$2" step="$3" reason="$4" rel want pl
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 48 "no run-state file, so there is no run to propose a playbook amendment against: $rel"; return 1; }
  [ -n "$item" ] || { fail 48 "--propose requires --item, because a proposal naming no amendment is the bare 'noticed something' that a wrap-up cannot act on and the next run cannot find"; return 1; }
  [ -n "$step" ] || { fail 48 "--propose requires --step, because an amendment floating free of the playbook step that provoked it is advice, and the owner would have to re-derive where it applies"; return 1; }
  [ -n "$reason" ] || { fail 48 "--propose requires --reason, because a proposal recording no reason is indistinguishable from one nobody meant - the same argument --park and --waive already make"; return 1; }
  if [ "$(printf '%s' "$reason$item$step" | wc -l)" -ne 0 ]; then
    fail 48 "a proposed item, step or reason contains a newline, and park() appends ONE line that the gate parses line-wise, so this would forge a second parked row nothing wrote"; return 1
  fi
  # ITEM AND STEP, not the reason. The reason is the LINE-FINAL field and can hold anything; these
  # two are read back as the tokens between the separators, so either one spelling a separator makes
  # its own record unparseable - by the very check that reads it.
  case "$item$step" in *" · "*) fail 48 "a proposed item or step spells the record's own field separator ' · ', which makes the row unparseable by the check that reads it: $item at step $step"; return 1 ;; esac
  if [ -n "$BYPASS_BAN" ] && printf '%s%s%s' "$item" "$step" "$reason" | grep -qF -- "$BYPASS_BAN"; then
    fail 48 "a proposed item, step or reason spells the declared bypass flag, and the gate greps this file whole for it, so recording this would red the bar on a record no verb can rewrite; say it without the literal flag: $BYPASS_BAN"; return 1
  fi
  refuse_if_terminal "$rel" --propose || return 1
  # EXACT LINE COMPARE, for verb_park's recorded reason: the reason is line-final, so a `grep -qF`
  # matched any row whose reason merely STARTS with this one, and the verb then reported success
  # while writing nothing - silently dropping a distinct proposal.
  want="proposal · item $item · step $step · reason $reason"
  while IFS= read -r pl; do
    [ "$pl" = "$want" ] || continue
    echo "unattended: proposal already recorded, unchanged — $item"
    return 0
  done <<PROPOSED
$(grep -F -- ' proposal · item ' "$rel" 2>/dev/null | sed 's/^[^ ]* //')
PROPOSED
  park "$rel" proposal "$item" "$reason" "$step"
  stage_or_fail "$rel" || return 1
  echo "unattended: proposal recorded against step $step — $item"
  return 0
}

# ------------------------------------------------------------------- the PER-PIECE RECORD writer
# The spec's previous revision had four READERS of this record and no writer at all, so the two
# Definition-of-Done items reading it could only be met by hand — which the same spec forbids.
#
# ONE writer, TWO callers. `record_piece` takes an explicit records ROOT rather than a slug, so the
# attended path — which has no run-state file — reaches this function instead of a second
# implementation that would confirm this one rather than check it.
#
# THE PATH IS DERIVED from the piece's own repo-relative path. The record lives under the BUILD
# folder and not beside the piece, because the output tree is the DELIVERABLE and a governance
# artifact sitting in it is the thing an owner deletes.
record_path_of() { # records-root · piece-path
  # FLAT under the declared root. The root is the playbook's own `records` declaration, so a `pieces/`
  # segment underneath it would be a second naming rule the reader has to know - and the reader globs
  # the root. The driver's self-test caught exactly that split: the writer wrote one place and the
  # reader read another, and the live leg looked green only because the files had been moved by hand.
  printf '%s/%s.md' "$1" "$(printf '%s' "$2" | tr '/' '~')"
}
# HIGH 2 (round-1 diff review) - the ROW DROPPER, and it takes no regex. Both writers spelled this
# `sed -i "/^leg $leg · verdict /d"`, interpolating a CALLER-SUPPLIED leg name into a sed ADDRESS,
# which is a regular expression:
#
#   * a leg named `.*` matched EVERY verdict row and deleted them all, silently erasing a recorded
#     FAIL and flipping the piece back to verified on the next write;
#   * a leg containing `/` — `tools/lint.sh`, an ordinary thing to call a leg — closed the address
#     early, so sed aborted while the `printf` that follows still ran, leaving TWO verdict rows for
#     one leg on a record the reader then cannot decide either way.
#
# The `case` pattern below is a QUOTED expansion, which shell treats as a literal even when the value
# spells a glob, and the single trailing `*` is the only wildcard in it. No escaping to get wrong.
# HIGH 1 (round-2 diff review) - the FIELD RE-STAMP, and it takes no regex either. Both writers
# spelled this `sed -i "s|^set: .*|set: $hashes|"`, interpolating a caller value into a sed
# REPLACEMENT — which is a different injection from the ADDRESS the dropper below fixed, twelve lines
# away, in the same commit:
#
#   * `--set 'AAAA\nleg forged · verdict PASS'` wrote a well-formed verdict row, walking past a
#     newline guard that counts newline BYTES and therefore never saw the two-character escape;
#   * `&` in a replacement re-inserts the whole match, corrupting the line;
#   * `|` closed the delimiter, so sed aborted while the function reported success anyway.
#
# Reachable because `--set` and `--playbook-sha` arrive through the records-root branch, which runs
# BEFORE the slug lookup — the attended path the kit ships and documents.
set_field() { # record · key · value
  local rec="$1" key="$2" val="$3" tmp line
  tmp=$(mktemp) || return 1
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in "$key: "*) printf '%s: %s\n' "$key" "$val" ;; *) printf '%s\n' "$line" ;; esac
  done < "$rec" > "$tmp"
  mv "$tmp" "$rec"
}

drop_leg_row() { # record · leg
  local rec="$1" lg="$2" tmp line
  tmp=$(mktemp) || return 1
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in "leg $lg · verdict "*) continue ;; esac
    printf '%s\n' "$line"
  done < "$rec" > "$tmp"
  mv "$tmp" "$rec"
}

record_piece() { # records-root · piece-path · leg · verdict · playbook-sha · run-id
  local root="$1" piece="$2" leg="$3" verdict="$4" pbsha="$5" runid="$6" rec want line h
  [ -f "$piece" ] || { fail 47 "a piece record names a path that is not a file in this tree, so the hash it joins on does not exist and the record would describe nothing - path follows: $piece"; return 1; }
  case "$verdict" in
    PASS|FAIL|NA) ;;
    *) fail 47 "a piece verdict is outside the closed set, and a verdict nobody can compare is a record that reads as evidence while carrying an opinion - legal values are PASS FAIL NA, given: $verdict"; return 1 ;;
  esac
  # verb_park's three guards, REUSED rather than re-argued. Each exists because of a recorded defect:
  # a newline forges a row nothing wrote, the field separator makes a row unparseable by the check
  # that reads it, and the bypass flag reds the bar permanently on a record no verb repairs.
  # EVERY CALLER-SUPPLIED FIELD, not the three that happened to be listed. `$pbsha` and `$runid`
  # arrive from argv on the attended path and were covered by none of these guards, so
  # `--playbook-sha "$(printf 'deadbeef\nleg L · verdict PASS')"` forged a PASS on the record's FIRST
  # write with no sed involved at all. §9's rule is ONE composite write-guard on every path that
  # stores parseable content; two writers with two different field sets is the bare-sibling-path hole
  # that rule is written against.
  if [ "$(printf '%s' "$leg$verdict$piece$pbsha$runid" | wc -l)" -ne 0 ]; then
    fail 47 "a piece record field contains a newline, and these records are parsed line-wise, so this would forge a verdict row nothing wrote"; return 1
  fi
  case "$leg$piece$pbsha$runid" in *" · "*) fail 47 "a piece record field spells the record's own field separator, which makes the row unparseable by the check that grades it - the four fields tested follow: leg [$leg] piece [$piece] playbook-sha [$pbsha] run [$runid]"; return 1 ;; esac
  if [ -n "${BYPASS_BAN:-}" ] && printf '%s%s%s%s' "$leg" "$piece" "$pbsha" "$runid" | grep -qF -- "$BYPASS_BAN"; then
    fail 47 "a piece record field spells the declared bypass flag, and check 10 of the playbook leg greps every tracked record under a declared records root for it, so writing this would red the bar on a record no verb can rewrite; say it without the literal flag: $BYPASS_BAN"; return 1
  fi
  rec=$(record_path_of "$root" "$piece")
  mkdir -p "$(dirname "$rec")" || return 1
  h=$(GIT hash-object "$piece") || return 1
  if [ ! -f "$rec" ]; then
    {
      printf '# piece record — %s\n\n' "$piece"
      printf 'piece: %s\n' "$piece"
      printf 'hash: %s\n' "$h"
      # The RUN identity, PASSED IN rather than derived from the records root. `enumerate_run` reads
      # it from the RECORD, so the scope is derivable on the merge bar where no run-state file
      # exists. Deriving it from `basename "$root"` was the first cut and it named a DIRECTORY: the
      # root is the playbook's own `records` declaration, so its basename says where records live and
      # nothing about who wrote them. Wiring the filter is what made that visible.
      printf 'run: %s\n' "$runid"
      printf 'playbook-sha: %s\n' "$pbsha"
      printf '\n## Verdicts\n'
    } > "$rec"
  else
    # The hash is RE-STAMPED on every write. A record is a claim about the piece AS IT STANDS, and a
    # stale hash beside a fresh verdict is exactly the `stale` state the reader exists to name.
    set_field "$rec" hash "$h" || return 1
  fi
  want="leg $leg · verdict $verdict"
  # EXACT LINE compare, not a substring search. `verb_park` had to repair precisely this: a prefix
  # match reported success while writing nothing, silently dropping a distinct entry.
  while IFS= read -r line; do
    [ "$line" = "$want" ] || continue
    # M1 (round-2): STAGE ON THIS PATH TOO. The hash was re-stamped above, so "unchanged" was false
    # the moment the piece had moved — the file was modified and left unstaged, and `--close` has no
    # clean-tree guard, so the run reached LANDING and the lander refused it with a message blaming
    # the operator's tree. This is the one path L1's superseded refusal actively drives runs onto.
    stage_or_fail "$rec" || return 1
    echo "unattended: piece verdict unchanged — $leg on $piece (the record's hash was re-stamped)"
    return 0
  done < "$rec"
  # A leg may be RE-recorded with a different verdict and the newest wins: two verdicts for one leg
  # is a record that cannot be read either way.
  drop_leg_row "$rec" "$leg" || return 1
  printf '%s\n' "$want" >> "$rec"
  stage_or_fail "$rec" || return 1
  echo "unattended: piece verdict recorded — $leg $verdict on $piece"
  return 0
}
record_set() { # records-root · run-id · leg · verdict · ordered-hash-list
  local root="$1" runid="$2" leg="$3" verdict="$4" hashes="$5" rec want line
  case "$verdict" in
    PASS|FAIL|NA) ;;
    *) fail 47 "a set verdict is outside the closed set, and a verdict nobody can compare is a record that reads as evidence while carrying an opinion - legal values are PASS FAIL NA, given: $verdict"; return 1 ;;
  esac
  # HIGH 3 (round-1 diff review) - THE THREE FIELD GUARDS, which this writer alone did not carry
  # while its four siblings all did. A newline in `--leg` forged a second verdict row nothing wrote:
  # the row the run meant to record said FAIL, the forged one said PASS, and the Definition-of-Done
  # reader four functions away greps this file line-wise and saw the PASS. Reproduced against the
  # shipped driver before this landed. Same three refusals, same reasons, same wording as the piece
  # writer's - the point is that a writer of this record has them, not that each argues them again.
  # `$hashes` joins the separator and bypass guards it was missing. It is DERIVED on the slug path
  # and CALLER-SUPPLIED on the attended one, and a guard that covers only the derived callers is a
  # guard against nothing.
  if [ "$(printf '%s' "$leg$verdict$runid$hashes" | wc -l)" -ne 0 ]; then
    fail 47 "a set record field contains a newline, and these records are parsed line-wise, so this would forge a verdict row nothing wrote"; return 1
  fi
  case "$leg$runid$hashes" in *" · "*) fail 47 "a set record field spells the record's own field separator, which makes the row unparseable by the check that grades it - the three fields tested follow: leg [$leg] run [$runid] set [$hashes]"; return 1 ;; esac
  if [ -n "${BYPASS_BAN:-}" ] && printf '%s%s%s' "$leg" "$runid" "$hashes" | grep -qF -- "$BYPASS_BAN"; then
    fail 47 "a set record field spells the declared bypass flag, and check 10 of the playbook leg greps every tracked record under a declared records root for it, so writing this would red the bar on a record no verb can rewrite; say it without the literal flag: $BYPASS_BAN"; return 1
  fi
  rec="$root/set-$runid.md"
  mkdir -p "$(dirname "$rec")" || return 1
  if [ ! -f "$rec" ]; then
    { printf '# set record — %s\n\n' "$runid"
      printf 'run: %s\n' "$runid"
      printf 'set: %s\n' "$hashes"
      printf '\n## Verdicts\n'; } > "$rec"
  else
    # The SET is re-stamped on every write, the way a piece record re-stamps its hash. A set verdict
    # beside a stale member list is a verdict about a different set, which is the `superseded` state.
    set_field "$rec" set "$hashes" || return 1
  fi
  want="leg $leg · verdict $verdict"
  while IFS= read -r line; do
    [ "$line" = "$want" ] || continue
    # M1 (round-2), and this is the writer L1's superseded refusal drives a run back to: the member
    # list was re-stamped above, so leaving it unstaged left the index and the worktree disagreeing
    # about the very field that refusal compares.
    stage_or_fail "$rec" || return 1
    echo "unattended: set verdict unchanged — $leg (the record's member list was re-stamped)"
    return 0
  done < "$rec"
  drop_leg_row "$rec" "$leg" || return 1
  printf '%s\n' "$want" >> "$rec"
  stage_or_fail "$rec" || return 1
  echo "unattended: set verdict recorded — $leg $verdict for $runid"
  return 0
}
verb_record_set() { # slug · leg · verdict
  local slug="$1" leg="$2" verdict="$3" rel rr_root pb hashes
  [ -n "$leg" ] || { fail 47 "--record-set requires --leg, because a set verdict that names no check cannot be compared against the playbook's declared set"; return 1; }
  [ -n "$verdict" ] || { fail 47 "--record-set requires --verdict, because an absent one is indistinguishable from a check that never ran"; return 1; }
  if [ -n "${RP_ROOT:-}" ]; then
    record_set "$RP_ROOT" "${RP_RUN:-$slug}" "$leg" "$verdict" "${RP_SET:-}"
    return $?
  fi
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 47 "no run-state file, so there is no run to record a set against - the attended path calls the records-root form of this writer instead: $rel"; return 1; }
  refuse_if_terminal "$rel" --record-set || return 1
  pb=$(fact "$rel" playbook)
  rr_root=$(declared_scalar "$(GIT show "$(fact "$rel" base):$pb" 2>/dev/null)" records)
  [ -n "$rr_root" ] || { fail 47 "the playbook this run is bound to declares no records root at the pinned BASE, so a set verdict has nowhere to be written that the merge bar will read"; return 1; }
  # The set IDENTITY is the ORDERED list of this run's piece hashes, DERIVED here rather than
  # supplied: a caller that names its own set could name a set it did not produce.
  hashes=$(for r in $(GIT ls-files -- "$rr_root/*.md"); do
             [ "$(sed -n 's/^run: //p' "$r" | head -1)" = "$slug" ] || continue
             sed -n 's/^hash: //p' "$r" | head -1
           done | LC_ALL=C sort | tr '\n' ',' | sed 's/,$//')
  record_set "$rr_root" "$slug" "$leg" "$verdict" "$hashes"
}
verb_record_piece() { # slug · piece · leg · verdict
  local slug="$1" piece="$2" leg="$3" verdict="$4" rel rr_root
  # THE THREE FIELD REFUSALS ARE HOISTED, above the caller branch. They were duplicated once per
  # caller, which is three refusals with two spellings each and six arms to keep in step - the
  # shape that goes stale on the first edit to either copy.
  [ -n "$piece" ] || { fail 47 "--record-piece requires --path, because a verdict with no piece to join to is a verdict about nothing"; return 1; }
  [ -n "$leg" ] || { fail 47 "--record-piece requires --leg, because a verdict that names no check cannot be compared against the playbook's declared set"; return 1; }
  [ -n "$verdict" ] || { fail 47 "--record-piece requires --verdict, because an absent one is indistinguishable from a check that never ran"; return 1; }
  # S3 - THE SECOND CALLER. `--records-root` reaches the SAME writer with an explicit root instead of
  # a slug, which is how the attended path records a piece: it has no run-state file and no run to
  # name. One function, two callers, never two implementations - the second would confirm the first
  # rather than check it, and they would drift the first time either changed.
  if [ -n "${RP_ROOT:-}" ]; then
    record_piece "$RP_ROOT" "$piece" "$leg" "$verdict" "${RP_PBSHA:-}" "${RP_RUN:-$slug}"
    return $?
  fi
  check_slug "$slug" || return 1
  rel=$(runmd_of "$slug")
  [ -f "$rel" ] || { fail 47 "no run-state file, so there is no run to record a piece against - the attended path calls the records-root form of this writer instead, which is why there is one function and two callers: $rel"; return 1; }
  refuse_if_terminal "$rel" --record-piece || return 1
  rr_root=$(declared_scalar "$(GIT show "$(fact "$rel" base):$(fact "$rel" playbook)" 2>/dev/null)" records)
  [ -n "$rr_root" ] || { fail 47 "the playbook this run is bound to declares no records root at the pinned BASE, so a piece verdict has nowhere to be written that the merge bar will read"; return 1; }
  # M6 (round-1 diff review): the BLOB SHA, not the path. This passed `$(fact "$rel" playbook)` —
  # the same expression used one line up as the PATH half of a `GIT show` — into a field printed as
  # `playbook-sha:`. Dead plumbing carrying wrong data is worse than no plumbing: the instant anyone
  # wires the provenance join it exists for, every unattended-written record fails it.
  record_piece "$rr_root" "$piece" "$leg" "$verdict" \
    "$(GIT rev-parse "$(fact "$rel" base):$(fact "$rel" playbook)" 2>/dev/null)" "$slug"
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
      # THE QUESTION IS NOT "is it in the region NOW". It is "was it in the roster this run STARTED
      # with", which is the question check 24 asks and the only one that separates a fabricated row
      # from a late one. Asking the current region instead made the two checks unsatisfiable
      # together: check 24 demands a row for every unit added after the run went live, and by the
      # time anybody writes one the spec exists and the region carries the id, so the row is
      # refused forever. Measured on this build — four units, all added by explicit owner turns
      # mid-run, all unrecordable. TOOL-dUnstalledConvoy-33.
      #
      # NO FALLBACK COMMIT is handed to `baseline_units` here, deliberately. The checker passes its
      # pinned BASE because a comparison it cannot make is a comparison it should SKIP; this caller
      # would be writing a permanent record, so a baseline it could not derive means it refuses.
      if printf '%s\n' "$ids" | grep -qxF -- "$unit"; then
        _rs_base=$(baseline_units "$rel" "$(readme_of "$slug")" "${UNITS_REGION_CUTOFF:-}") || {
          fail 48 "a rescope adds a unit the generated units region already carries, and the roster this run entered its live phase with cannot be derived, so there is no way to tell a late record from a transition that did not happen: $unit ($_rs_base)"; return 1; }
        if id_in "$_rs_base" "$unit"; then
          fail 48 "a rescope adds a unit that was already in the roster this run entered its live phase with, so this records a transition that did not happen: $unit"; return 1
        fi
        echo "unattended: LATE record — $unit entered the roster after this run went live and is only being recorded now"
      fi ;;
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
    fail 49 "--dispatch was given a --pass value that is not id-shaped by the driver's own spelling, and the leg joins a declaration to a commit through that id: $_u"; return 1; }
  [ "$#" -gt 0 ] || { fail 49 "--dispatch requires at least one --writes path, because a declaration naming nothing is not a disjointness proof: $unit"; return 1; }
  # EACH --writes IS ONE PATH. A space-joined value cannot carry the whitespace refusal below: the
  # path has already become two tokens by the time this verb sees it, and nothing recovers that.
  for p in "$@"; do
    case "$p" in
      "") fail 49 "--dispatch was given an empty --writes path, and an empty declaration is not a narrow one: $unit"; return 1 ;;
      /*|?:[/\\]*) fail 49 "--dispatch was given an absolute --writes path, and a declaration is repo-relative or it names a file no comparison can find: $p"; return 1 ;;
      *..*) fail 49 "--dispatch was given a --writes path that escapes the repository, which no pass may declare and no comparison can bound: $p"; return 1 ;;
    esac
    if is_repo_root "$p"; then
      fail 49 "--dispatch declares the repository root, which covers every path and sits under none, so no containment test can express it and a pass declaring it is disjoint from nothing: $p"; return 1
    fi
    case "$p" in
      *'*'*|*'?'*|*'['*|*']'*) fail 49 "--dispatch was given a --writes path carrying a glob metacharacter, and both readers of the recorded row expand it unquoted, so the declared set would differ from the compared one: $p"; return 1 ;;
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
  # BOTH DIRECTIONS, and that is the whole of the refusal's reach. Testing only "is the declared
  # path UNDER a shared record" licenses the widest declaration a pass could possibly make: a bare
  # `--writes memory` contains every shared record in the tree and is under none of them, so the
  # narrow declarations get refused and the one that claims everything sails through.
  for p in "$@"; do
    if overlaps "$p" "$rel"; then
      fail 49 "--dispatch declares the run-state file, or a path containing it, and every pass in the run shares that file, so two passes declaring it are not disjoint by construction: $p"; return 1
    fi
    for q in ${SHARED_RECORDS:-}; do
      if overlaps "$p" "$q"; then
        fail 49 "--dispatch declares a path overlapping a shared mutable record this project declares, and the build method names those outright rather than conditionally: $p against $q"; return 1
      fi
    done
  done
  # CONDITION 3, CONDITIONAL HALF. A generated index alone is ACCEPTED - every pass changes a spec
  # header it is rendered from, and refusing that was the VACUOUS reading M6 retracted. What collides
  # is one pass RENDERING an artifact while another edits its generator, so the refusal fires only
  # when both appear, in this declaration or in a sibling's within the same group.
  grp=$(GIT rev-parse --short=8 HEAD 2>/dev/null)
  [ -n "$grp" ] || { fail 49 "--dispatch cannot resolve HEAD, and HEAD is the group key two passes declared together share: $slug"; return 1; }
  # THE SIBLING SET IS EVERY PASS THAT HAS NOT COMMITTED YET, not the rows sharing this exact HEAD.
  # A commit landing between two concurrent declarations moves HEAD, so a group key that IS HEAD
  # empties the sibling set at the moment the second pass declares, and condition 1 then passes by
  # finding nobody to collide with.
  #
  # OPENNESS COMES FROM `pass_commit` IN THE KIT LIBRARY, which the gate leg calls too. The first
  # version of this hunk answered the question here instead, and asserted in a comment that it read
  # it "the same way the leg reads it". It did not: it counted the run-state bookkeeping commit that
  # carries a pass's OWN declaration, so every pass closed the instant it was declared and this whole
  # proof ran over an empty set. A closing review reproduced that with two controls. The comment is
  # now a function call, which cannot be wrong about what the leg does.
  sibrows=$(grep -F -- " dispatch · item " "$rel" 2>/dev/null | while IFS= read -r _r; do
      [ -n "$_r" ] || continue
      _i=${_r#* dispatch · item }; _i=${_i%% · reason *}
      _g=${_i%% *}; _u=${_i#* }
      # An anchor this clone cannot resolve leaves the pass OPEN — `pass_commit` returns 1 for it.
      # Conservative by choice: the failure of a disjointness proof must be a refusal, never a pass.
      _pcommit=$(pass_commit "$_g" "$_u" "$rel" || true)
      if [ -n "$_pcommit" ]; then
        # ...AND THAT COMMIT MUST HAVE WRITTEN INSIDE THE ROW'S DECLARED SET before it closes the
        # pass. Subtracting the run-state file alone is not enough: a declaration commit made with
        # `git add -A` carries a regenerated index or a formatter fix alongside it, names the unit
        # because it is about that unit, and closed the pass at declaration time. That is the
        # ordinary commit shape a run produces, not an exotic one.
        _decl=${_r#* · reason }
        _wrote=$(GIT diff-tree --no-commit-id --name-only -r "$_pcommit" 2>/dev/null || true)
        _hit=""
        for _dp in $_decl; do
          for _wp in $_wrote; do overlaps "$_dp" "$_wp" && { _hit=1; break 2; }; done
        done
        [ -n "$_hit" ] && continue
      fi
      printf '%s\n' "$_r"
    done)
  sibpaths=$(printf '%s\n' "$sibrows" | sed 's/.* · reason //' | tr '\n' ' ')
  # A PROOF OVER NOBODY SAYS SO. The condition-1 loop below iterates the sibling rows and returns
  # success over zero of them, which is byte-indistinguishable from a proof over somebody — and an
  # empty sibling set is exactly what both openness defects produced. A probe that cannot move must
  # announce it (§7), so the run log carries the difference even when the verdict cannot.
  # MEASURED ON CONDITION 1'S OWN POPULATION, not on `sibrows`. The loop below SKIPS this unit's own
  # rows, so a `sibrows` holding nothing but our own rows is a proof over an empty set that the old
  # announcement stayed silent about — it measured a set the proof does not use.
  _sibothers=$(printf '%s\n' "$sibrows" | while IFS= read -r _r; do
      [ -n "$_r" ] || continue
      case "$_r" in *" $unit · reason "*) continue ;; esac
      printf 'x'
    done)
  if [ -z "$_sibothers" ]; then
    echo "unattended: dispatch — no sibling pass is open, so condition 1 is a proof over an empty set for $unit" >&2
  fi
  for pair in ${GENERATED_INDEXES:-}; do
    idx=${pair%%:*}; gen=${pair#*:}
    [ "$idx" = "$pair" ] && continue
    # BOTH HALVES read our paths AND the siblings'. Searching for the index in our own declaration
    # only made the refusal order-dependent: the pass that declares the index first is clean, and the
    # sibling that later declares the generator never looks for the index anywhere but its own args.
    for p in "$@" $sibpaths; do
      overlaps "$idx" "$p" || continue
      for q in "$@" $sibpaths; do
        # OVERLAP on both halves. `covers` asks whether q sits under the generator, which misses a
        # declaration that CONTAINS the generator — the same one-way reading that let `--writes
        # memory` through the shared-records refusal, left behind at this one site.
        if overlaps "$gen" "$q"; then
          fail 49 "--dispatch declares a generated index together with its generator, which is the one pairing the build method's condition 3 forbids - the index alone is fine and refusing it was the reading that condition retracted: $idx with $gen"; return 1
        fi
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
        # OVERLAP, never equality. Two passes declaring `memory/builds/x/` and
        # `memory/builds/x/spec/s.md` collide on every write, and string equality calls them disjoint.
        overlaps "$p" "$q" || continue
        local _who=${sib#* dispatch · item }; _who=${_who%% · reason *}
        fail 49 "--dispatch declares a path a sibling pass in the same group already declared, and two passes claiming one file are not disjoint: $p also in $_who"; return 1
      done
    done
  done <<SIBS
$sibrows
SIBS
  # PARKED NORMALISED. Every refusal above asks its question through `normpath`; recording the raw
  # spelling meant the guards judged one path and the leg graded another, and `work/sub/` sailed
  # through the driver and then redded the leg permanently.
  want=""
  for p in "$@"; do want="$want $(normpath "$p")"; done
  want=${want# }
  # THE RE-DECLARATION AND WIDENING MACHINERY IS GONE, and its absence is the fix rather than a gap.
  # TOOL-dUnstalledConvoy-23 redesigned what replaced it; four adversarial rounds are recorded under
  # `memory/builds/dUnstalledConvoy/reviews/`.
  #
  # WHY IT WAS REMOVED RATHER THAN REPAIRED. The branch existed to let a pass widen a declaration it
  # had already made, and to refuse a narrowing. Every version of it was wrong in a different
  # direction: keyed on HEAD it lost the row the moment the run committed its own declaration; keyed
  # on the unit it refused a legal second pass forever, which is terminal in a run with no owner turn;
  # keyed on the unit with an overlap gate it let a pass that had ALREADY written outside its lane
  # re-park a widened row at the original anchor and RETRACT a check-23 failure that had already been
  # emitted — rc=1 to rc=0 over the same violating tree, reproduced end to end. A disjointness proof
  # that can be talked out of a finding is worth less than no proof, because it is believed.
  #
  # A declaration is now APPEND-ONLY and each one stands on its own: every `--dispatch` parks a row at
  # the current anchor, and nothing rewrites, supersedes or retracts an earlier one. A pass that needs
  # more paths declares again; both rows are on the record and a redesign can read them. There is no
  # narrowing refusal, because with grading dark there is nothing for a narrowing to hide from — and a
  # refusal nobody can clear is the stall this build exists to remove.
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
# which is what `--abort <slug> --reason <text> --code <halt-code>` uses. A flag still pending when argv ends keeps the
# EMPTY reason it was pushed with, so it meets the missing-reason refusal that already exists instead
# of vanishing - the refusal is reached by the value, not by a second branch.
VERB=""; SLUG=""; KID=""; REASON=""; arg=""; AT_VALUE="yes"
RP_PATH=""; RP_LEG=""; VERDICT=""; RP_ROOT=""; RP_PBSHA=""; RP_RUN=""; RP_SET=""
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
    --pass)         PK_ITEM="${2:-}"; shift 2 || shift ;;
    --writes)       DP_WRITES+=("${2:-}"); shift 2 || shift ;;
    --act)          RS_ACT="${2:-}"; shift 2 || shift ;;
    --successor)    RS_SUCC="${2:-}"; shift 2 || shift ;;
    --item)         PK_ITEM="${2:-}"; shift 2 || shift ;;
    --step)         PK_STEP="${2:-}"; shift 2 || shift ;;
    --path)         RP_PATH="${2:-}"; shift 2 || shift ;;
    --leg)          RP_LEG="${2:-}"; shift 2 || shift ;;
    # ONE ARM FOR ONE FLAG. Both sides of the merge added a `--verdict` case arm - one for the record
    # verbs, one for `--review` - and a `case` takes the first match, so the second was dead and the
    # review verb received an empty verdict from a flag the operator had spelled correctly. A flag is
    # a name; a name gets one variable, and the verbs that read it read the same one.
    --verdict)      VERDICT="${2:-}"; shift 2 || shift ;;
    --records-root) RP_ROOT="${2:-}"; shift 2 || shift ;;
    --playbook-sha) RP_PBSHA="${2:-}"; shift 2 || shift ;;
    --run)          RP_RUN="${2:-}"; shift 2 || shift ;;
    --set)          RP_SET="${2:-}"; shift 2 || shift ;;
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
    --code)         HALT_CODE="${2:-}"; shift 2 || shift ;;
    --review)       VERB=--review; SLUG="${2:-}"; shift 2 || shift ;;
    --subject)      RV_SUBJECT="${2:-}"; shift 2 || shift ;;
    --blockers)     RV_BLOCKERS="${2:-}"; shift 2 || shift ;;
    --plan)         shift; refuse_waive_unless_preflight --plan || exit 1; verb_plan "${1:-}"; exit $? ;;
    --phase)        shift; PH_SLUG=${1:-}; shift 2>/dev/null || true; PH_WANT=${1:-}; shift 2>/dev/null || true
                    PH_WIT=""
                    [ "${1:-}" = "--witness" ] && { shift; PH_WIT=${1:-}; }
                    refuse_waive_unless_preflight --phase || exit 1
                    verb_phase "$PH_SLUG" "$PH_WANT" "$PH_WIT"; exit $? ;;
    --version)      echo "unattended $KIT_UNATTENDED_VERSION"; exit 0 ;;
    # THE SET IS THE DISPATCH. A slug-taking verb is recognised by membership in VERBS_SLUG rather
    # than by an alternation typed here, so the declaration is load-bearing: a verb absent from it
    # falls through to refusal 14 and does not run at all. The arm sits LAST because every flag above
    # would otherwise be tested against it, and it must not shadow --plan, --phase or --version.
    *) if is_slug_verb "${1:-}"; then VERB="$1"; SLUG="${2:-}"; shift 2 || shift
       else arg="$1"; vl=$(verb_list)
            # THE LIST IN A VARIABLE, not a command substitution inside the message. check-arms reads
            # a branch's literal signature up to its first interpolation and does not treat $( ) as
            # one, so the inline form demanded a test arm quoting `$(verb_list)` verbatim - an arm
            # that would pass while the list it renders was empty.
            fail 14 "unknown argument; the verbs are $vl: $arg"; exit 1; fi ;;
  esac
done
# S10, and then the verb-carrier unit, because S10's fix did not hold: the three spellings were
# re-synchronised by hand and drifted again at the next verb. Both survivors now DERIVE - the refusal
# above from VERBS_SLUG, this usage text from the header's own invocation lines - so there is nothing
# left here to re-synchronise.
case "$VERB" in --preflight) ;; *) refuse_waive_unless_preflight "${VERB:-(none)}" || exit 1 ;; esac
[ -n "$VERB" ] || { usage; exit 2; }

case "$VERB" in
  --preflight) verb_preflight "$SLUG" "$KID" ;;
  --status)    verb_status "$SLUG" ;;
  --resume)    verb_resume "$SLUG" ;;
  --close)     verb_close "$SLUG" ;;
  --landed)    verb_landed "$SLUG" ;;
  --abort)     verb_abort "$SLUG" "$REASON" "$HALT_CODE" ;;
  --park)      verb_park "$SLUG" "$PK_ITEM" "$REASON" ;;
  --propose)   verb_propose "$SLUG" "$PK_ITEM" "$PK_STEP" "$REASON" ;;
  --review)    verb_review "$SLUG" "$RV_SUBJECT" "$VERDICT" "$RV_BLOCKERS" ;;
  --attest)    verb_attest "$SLUG" "$PK_ITEM" "$AT_VALUE" ;;
  --record-piece) verb_record_piece "$SLUG" "$RP_PATH" "$RP_LEG" "$VERDICT" ;;
  --record-set)   verb_record_set "$SLUG" "$RP_LEG" "$VERDICT" ;;
  --rescope)   verb_rescope "$SLUG" "$RS_ACT" "$PK_ITEM" "$RS_SUCC" "$REASON" ;;
  --dispatch)  verb_dispatch "$SLUG" "$PK_ITEM" "${DP_WRITES[@]}" ;;
esac
exit "$status"
