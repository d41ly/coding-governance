#!/usr/bin/env bash
# manifest-check.sh — kickoff-manifest ratchet gate (coding-governance session-kickoff kit).
# Verifies a project's SESSION-KICKOFF.md kickoff manifest against mechanical truth signals:
#   C1 no surviving {{PLACEHOLDER}}      C2 audit block present + parseable
#   C3 anchor sha real + ancestor        C4 verify-paths tracked
#   C5 no unaudited watch drift          C6 watch list alive
# Single source: CI, pre-commit, the manifest's gate fence, and the kickoff engine all invoke THIS
# script — never hand-copy the checks. Spec: the manifest-ratchet design record in coding-governance.
#
#   manifest-check.sh [<manifest-path>]   # full check (discovers the manifest when no path given;
#                                         # a relative path resolves from the repo root, then from
#                                         # the invoking directory)
#   manifest-check.sh --staged [<path>]   # pre-commit fast leg: C1 C2 C4 C6 C7 C8 + C5s, or ONE
#                                         # NOTE and exit 0 when nothing staged touches the
#                                         # manifest, its watch list or its verify-paths.
#                                         # C9/C10/C11 are FULL-RUN only: they judge the working
#                                         # tree, not what this commit stages, and the hook that
#                                         # runs this leg fires on every commit.
#   manifest-check.sh --card --write [--session <sid>]    # write the session's orientation card
#   manifest-check.sh --card --replay [--session <sid>]   # print it back, plus one `now —` line
#   manifest-check.sh --card --path [--session <sid>]     # print where it lives, touch nothing
#   manifest-check.sh --card --append --session <sid>     # stdin = the kickoff's body: check every
#                                         # cited path, range and id for EXISTENCE in two spawns,
#                                         # annotate each miss `UNVERIFIED — <token>`, store it
#   manifest-check.sh --card --check --session <sid>      # the same check over the stored card
#   manifest-check.sh --card --path --build <slug>        # the build card's cache path, touch nothing
#   manifest-check.sh --card --publish --build <slug> --session <sid>   # the build card, from the
#                                         # session's card, written to each store card.store selects
#   manifest-check.sh --card --follow --build <slug> --to <state> [--terminal]   # the build card
#                                         # re-published at a stage move, as card.follows says
#   manifest-check.sh --card --lookup --build <slug> --session <sid>    # the build card read back from
#                                         # its first store that answers, re-keyed into the session's card
#   manifest-check.sh --card --pointers --build <slug> [--session <sid>]   # the `## pointers` section
#                                         # published to each store card.store selects, and with
#                                         # --session written into that session's card too
#   manifest-check.sh --card --boundary --build <slug> --session <sid> [--transcript <path>] [--out <file>]
#                                         # the item boundary, I12: the card's `item —` line moved to
#                                         # HEAD, and a crossing written and published as card.pointers says
#   manifest-check.sh --card --fixture-run <scratch-dir>   # run card-compaction.fixture.sh there and
#                                         # record its verdict in <git-common-dir>/orientation/card-fixture.verdict
#   manifest-check.sh --brief-skeleton   # the brief record's skeleton and the card's `## route`
#                                         # skeleton; like --task-skeleton, it needs no repository
#     A body carrying `## route` is held to the route rules beside `check_card_route`: every unit,
#     its spec and the brief must RESOLVE, or nothing is appended (KICK-aRoutedQuill-1).
#     The card verbs run NO manifest check: the session id comes from the SessionStart hook's JSON
#     on stdin, else --session (--append: --session alone, stdin is the body); the card lives at
#     <git-common-dir>/orientation/<sid>.md, shared by every worktree, and --write, --replay and
#     --append re-render it, enveloped, into the session tree's ignored .claude/orientation-card.md
#     (PLAY-dOrderedCharter-8: the payload `cwd`'s toplevel, else this tree); the `node —` cell resolves
#     through the manifest audit block's `registry:` key. The append and the check do NOT judge
#     relevance, scope, tier, or the truth of a claim at the line it cites — existence only.
#
# Exit 0 + no FAILED lines = clean (WARN:/NOTE: lines permitted). Exit 1 = a check failed — for
#          the card verbs: a body or card with nothing to check (DEAD PROBE), a --check miss, a
#          real READY line with no `## task` beneath it, a READY body whose `## task` leaves a field
#          --task-skeleton prints absent, repeated, empty or a placeholder, or a body whose
#          `## route` breaks a rule.
# Exit 2 = environment error (not a git repo / no manifest found / path outside the repo / a card
#          verb with no session id, a path-shaped one, a card over its byte cap, an append whose
#          READY line pins a BASE that is not HEAD, an id reader that could not answer, or a route
#          the tree cannot check: no MEMORY_ROOT, or no defined-id set).
set -u
KIT_MANIFEST_VERSION="1.39"   # gov:kit kickoff-manifest@1.39 — the registry id
# TWO NUMBERS, not one (TOOL-aRepatriatedFork-15 S4). KIT_MANIFEST_VERSION above is the kit's
# VINTAGE: it bumps whenever a shipped byte of this kit moves, which is what `govkit.py epoch` grades.
# MANIFEST_FORMAT is the manifest FORMAT, the only number an adopter's `kickoff-manifest: v<N>`
# marker and the shipped seed's marker are compared with. It was one number, so every vintage bump
# told every adopter to upgrade a format that had not moved. Raise it only with an upgrade step.
MANIFEST_FORMAT="1.5"

# THE ONE LIST of places a kickoff manifest may live, in precedence order. Every consumer reads it
# from here — the discovery loop, the not-found message, and the `--locations` verb that the kickoff
# engine and WIRE-INTO-PROJECT.md invoke INSTEAD of restating the list. It used to be spelled in five
# files that did not agree with each other, and two of the four spellings named directories no live
# install has ever used.
#
# The skill's own base directory is a THIRD location the ENGINE honours and this script deliberately
# does not list: it sits outside every repository, and this script decides membership by git identity
# and refuses an out-of-repo path with exit 2 by design. It cannot check that one, so it does not
# claim to. A manifest found there is read but never audited, and the engine says so on the card.
MANIFEST_LOCATIONS="memory/guides/SESSION-KICKOFF.md .claude/SESSION-KICKOFF.md"

# THE CANONICAL TASK FIELD SET, and its ONE home. §A of a manifest used to restate what the kickoff
# engine's Step 3 already said, with the manifest outranking the engine on conflict — two binding
# spellings of one contract, which is the drift this kit exists to remove. Sealing the manifest's copy
# against a constant would have FROZEN that duplication; giving the field set one home removes it.
#
# It lives HERE because this script is the only kickoff-kit file that is present, byte-identical and
# overwritten wholesale in every adopting repo. MANIFEST-TEMPLATE.md cannot hold it: the template is a
# SEED that BECOMES the manifest, so an adopting tree has no reference copy left to compare against.
#
# NO PLACEHOLDER inside the region. A tier value is optional by the template's own customize note, and
# a region whose content is conditional cannot be byte-compared — it would be simultaneously required
# by check 10 and banned by check 1. The tier enumeration already has a home in §B's tier rule, so
# dropping it here is a deduplication that happens to be what makes the seal implementable.
#
# It is also the LABEL source: `check_card_task` reads the eight field labels out of it at run time, so
# the append's refusal and this skeleton cannot name different fields (KICK-aOrientedCast-1).
read -r -d '' TASK_SKELETON <<'KICKOFF_TASK_SKELETON' || true
<!-- kickoff:task -->
> - **Title:** …
> - **Goal (1–2 sentences):** …
> - **IN scope:** …
> - **OUT / non-goals** (explicit cut-line): …
> - **To-do:** (the steps in order, each naming what it changes) …
> - **Reuse:** (each seam this extends, by path, or "no seam fits" with the probe's evidence) …
> - **Acceptance check** (the observation that proves THIS change — a test it adds, a gate it
>   moves, an observed behavior; *not* an unrelated green check): …
> - **Gates it must pass:** …
<!-- /kickoff:task -->
KICKOFF_TASK_SKELETON

# FORMAT 1.4's region, FROZEN — the six fields before To-do and Reuse. Check 10 is its only reader: it
# passes this region, with a NOTE naming the re-paste, only in a manifest whose marker is older than
# 1.5, so an adopter's ratchet stays green through the `govkit update` that brings the eight fields.
# Never edit it; a format that moves the region again freezes ITS predecessor beside this one.
read -r -d '' TASK_SKELETON_FORMAT_1_4 <<'KICKOFF_TASK_SKELETON_1_4' || true
<!-- kickoff:task -->
> - **Title:** …
> - **Goal (1–2 sentences):** …
> - **IN scope:** …
> - **OUT / non-goals** (explicit cut-line): …
> - **Acceptance check** (the observation that proves THIS change — a test it adds, a gate it
>   moves, an observed behavior; *not* an unrelated green check): …
> - **Gates it must pass:** …
<!-- /kickoff:task -->
KICKOFF_TASK_SKELETON_1_4

# THE ONE BRIEF SHAPE, and the card's route shape beneath it (KICK-aRoutedQuill-1). A kickoff whose
# task writes product code drafts its brief from this, and the session pipes the filled route section
# to `--card --append`, which grades it by `check_card_route`. It lives here for the reason the task
# field set does: this script is the one kickoff-kit file overwritten whole in every adopter. The five
# sub-heads up to `### Non-goals` and the two single-line forms are TOOL-aQuotedBrief-1's §4 fence,
# spelled byte for byte; `### Limitations` and `### Reuse` follow them, so a reader grading the five in
# order still finds them. Unlike TASK_SKELETON, nothing seals a copy of this against the constant.
read -r -d '' BRIEF_SKELETON <<'KICKOFF_BRIEF_SKELETON' || true
<!-- the brief: <MEMORY_ROOT>/builds/<build>/prompts/<date>-prompt-<FAMILY>-<slug>-<seq>-brief.md, named for the first unit it serves; drafted at Step 3, written at Step 5, committed with that unit's spec after go -->
# Brief — <build>: <the build in a few words>

**Serves:** research <FAMILY-slug-seq> [<FAMILY-slug-seq> …]

## The prompt

> <the owner's words that asked for this build, verbatim>

## The brief

### Goal
<the build in one or two sentences, readable with no conversation>

### Items
1. <one thing the owner asked for>

### Acceptance
<the observation that proves each item>

### Gates
<the gate legs the build keeps green>

### Non-goals
<the cut-line: what the build must not build>

### Limitations
<every constraint the build must respect>

### Reuse
<the seam the reuse probe named and the records the recall query returned, or that none fits>

## Drawn from the session

> <a passage the brief relied on, verbatim>
— <owner|agent>, <turn or time>

## Owner confirmation

Asked: <the hand-back question, verbatim>
Answer: <the owner's reply, verbatim>

<!-- the card's route: once every spec it names is tracked, pipe from the heading down to --card --append --session <sid>; append again when that set changes -->
## route
- build: <build>
- unit: <FAMILY-slug-seq> · spec <repo-relative path>
- brief: <repo-relative path of the brief, or of the build README an unattended run was authorized by>
KICKOFF_BRIEF_SKELETON

# The read-only verbs answer BEFORE the repo probe below, because the whole point of `--locations` is
# to be readable from OUTSIDE a repository — and the probe exits 2 there without ever reading argv.
# They print and exit 0, adding no `fail` branch, so the harness meta-gate's shrink-only floor for this
# script counts none of them.
for _a in "$@"; do
  case "$_a" in
    --locations)      printf '%s\n' $MANIFEST_LOCATIONS; exit 0 ;;
    --task-skeleton)  printf '%s\n' "$TASK_SKELETON"; exit 0 ;;
    --brief-skeleton) printf '%s\n' "$BRIEF_SKELETON"; exit 0 ;;
  esac
done

# The card verbs are CONSUMED here, before the manifest loop below, whose catch-all reads any other
# argument as a manifest path. `--card` alone is a refusal, not a default: a verb the caller did not
# name is a card the caller did not ask for. Without `--card`, `--write` and its siblings still fall
# through to that catch-all exactly as they did before this block existed.
# The build card's verbs (TOOL-dPlacedRequest-2) take `--build <slug>`, and the follow `--to <state>`
# and `--terminal`; each value is held to its grammar here, before it is joined into a ref or a path.
CARD=""; CARD_VERB=""; CARD_SID=""; CARD_BUILD=""; CARD_STEP=""; CARD_TERMINAL=0; CARD_FIXTURE_DIR=""; _rest=(); _want=""
CARD_TX_ARG=""; CARD_OUT=""
for _a in "$@"; do [ "$_a" = --card ] && CARD=1; done
for _a in "$@"; do
  case "$_want" in
    sid) CARD_SID="$_a"; _want=""; continue ;;
    build) CARD_BUILD="$_a"; _want=""; continue ;;
    to) CARD_STEP="$_a"; _want=""; continue ;;
    fixture) CARD_FIXTURE_DIR="$_a"; _want=""; continue ;;
    tx) CARD_TX_ARG="$_a"; _want=""; continue ;;
    out) CARD_OUT="$_a"; _want=""; continue ;;
  esac
  case "$CARD$_a" in
    1--card) ;;
    1--write|1--replay|1--path|1--append|1--check|1--publish|1--follow|1--lookup|1--pointers|1--boundary) CARD_VERB="${_a#--}" ;;
    1--fixture-run) CARD_VERB=fixture-run; _want=fixture ;;
    1--session) _want=sid ;;
    1--session=*) CARD_SID="${_a#--session=}" ;;
    1--build) _want=build ;;
    1--to) _want=to ;;
    1--terminal) CARD_TERMINAL=1 ;;
    1--transcript) _want=tx ;;
    1--out) _want=out ;;
    *) _rest+=("$_a") ;;
  esac
done
set -- ${_rest[@]+"${_rest[@]}"}
if [ -n "$CARD" ] && [ -z "$CARD_VERB" ]; then
  echo "MANIFEST env ERROR — --card needs one of --write, --replay, --path, --append, --check, --publish, --follow, --lookup, --pointers, --boundary or --fixture-run"; exit 2
fi
# The session the caller named, before a follow's or a pointers publish's default fills CARD_SID below:
# `--card --pointers` writes a session card only when one was named (KICK-dKeptSession-13 S4).
CARD_SID_GIVEN=${CARD_SID:+1}
if [ -n "$CARD" ]; then
  case "$CARD_VERB:${CARD_BUILD:+b}" in
    publish:|follow:|lookup:|pointers:|boundary:) echo "MANIFEST env ERROR — --card --$CARD_VERB needs --build <slug>"; exit 2 ;;
    write:b|replay:b|append:b|check:b|fixture-run:b) echo "MANIFEST env ERROR — --build is the build card's flag, and --card --$CARD_VERB takes none"; exit 2 ;;
  esac
  # The boundary verb's flags (KICK-dKeptSession-13 S6): it reads one named session's card, and its `--out`
  # file is written through a temp beside it, so a directory that does not exist is refused here.
  if [ "$CARD_VERB" = boundary ]; then
    [ -n "$CARD_SID" ] || { echo "MANIFEST env ERROR — --card --boundary needs --session <sid>, the session whose card holds the item"; exit 2; }
    if [ -n "$CARD_OUT" ]; then
      case "$CARD_OUT" in /*|[A-Za-z]:*) ;; *) CARD_OUT="$PWD/$CARD_OUT" ;; esac
      [ -d "${CARD_OUT%/*}" ] || { echo "MANIFEST env ERROR — --out $CARD_OUT names a file in a directory that does not exist, so nothing ran"; exit 2; }
    fi
  elif [ -n "$CARD_TX_ARG" ] || [ -n "$CARD_OUT" ]; then
    echo "MANIFEST env ERROR — --transcript and --out are --card --boundary's flags"; exit 2
  fi
  [ "$CARD_VERB" != fixture-run ] || [ -n "$CARD_FIXTURE_DIR" ] \
    || { echo "MANIFEST env ERROR — --card --fixture-run needs <scratch-dir>, the directory the card-import fixture builds under"; exit 2; }
  [ -z "$CARD_BUILD" ] || [[ $CARD_BUILD =~ ^[A-Za-z0-9]+$ ]] \
    || { echo "MANIFEST env ERROR — --build '$CARD_BUILD' is not a build slug, [A-Za-z0-9]+, and is not joined into a ref or a path"; exit 2; }
  if [ "$CARD_VERB" = follow ]; then
    [[ $CARD_STEP =~ ^[a-z0-9][a-z0-9-]*$ ]] || { echo "MANIFEST env ERROR — --card --follow needs --to <state>, one word, and was given '$CARD_STEP'"; exit 2; }
  elif [ -n "$CARD_STEP" ] || [ "$CARD_TERMINAL" = 1 ]; then
    echo "MANIFEST env ERROR — --to and --terminal are --card --follow's flags"; exit 2
  fi
fi

CALLER_PWD=$PWD
# This kit's own directory, captured before the `cd` below: the sibling resolver walks from it.
MC_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd) || MC_DIR=$PWD
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "MANIFEST env ERROR — not a git repository"; exit 2; }
TOPLEVEL=$ROOT   # the bytes git prints, kept for the card's `tree —` cell: ONE declared spelling, before the normalisation below
ROOT=$(cd "$ROOT" 2>/dev/null && pwd) || { echo "MANIFEST env ERROR — cannot enter repo root"; exit 2; }   # normalize to the shell's path flavor (git-bash: C:/ vs /c/)
cd "$ROOT" || exit 2

# ---- the orientation card ------------------------------------------------------------------------
# One file per session under the git COMMON dir, so every worktree of one repository shares the
# directory and a card names the tree it was written in. Every startup field is DERIVED — nothing
# here is authored, and nothing here is imperative: hook-injected text reads to the model as an
# instruction from nobody. The cap is one constant; the append verb of the next unit refuses against
# the same one. The env override exists for the self-test's over-cap arm and is not an adopter knob.
CARD_CAP_BYTES=${CARD_CAP_BYTES:-8192}
# The card-import fixture `--card --fixture-run` runs and `read_card_fixture_verdict` hashes, the kickoff
# engine's sibling (KICK-dKeptSession-12 S1). The env override exists for the self-test's stub fixture,
# as CARD_CAP_BYTES's does, and is not an adopter knob.
CARD_FIXTURE=${CARD_FIXTURE:-$MC_DIR/card-compaction.fixture.sh}
CARD_FIXTURE_VERDICT=card-fixture.verdict
# The `overlaps —` cell's two constants (KICK-aMendedFleet-2): the read's bound in seconds and the
# row cap. The bound's env override exists for the self-test's slow-driver arm, as CARD_CAP_BYTES's
# does; neither is an adopter knob.
CARD_OVERLAP_BOUND=${CARD_OVERLAP_BOUND:-10}
CARD_OVERLAP_ROWS=5
# The replay's `map —` block's bound in seconds (PLAY-dOrderedCharter-4); the env override exists for
# the self-test's slow-stub arm and is not an adopter knob.
CARD_MAP_BOUND=${CARD_MAP_BOUND:-5}
# The `## pockets` section's bound on the playbook kit's `pockets` verb, in seconds (TOOL-dPlacedRequest-9);
# the env override exists for the self-test's slow-stub arm and is not an adopter knob.
CARD_POCKETS_BOUND=${CARD_POCKETS_BOUND:-5}
# The `cli —` cell's bound on `claude --version`, in seconds (KICK-aMendedFleet-4); the env override
# exists for the self-test's slow-stub arm and is not an adopter knob.
CARD_CLI_BOUND=${CARD_CLI_BOUND:-5}
# The `memory —` cell's bound on the playbook kit's index measure, in seconds (PLAY-dOrderedCharter-14);
# the env override exists for the self-test's slow-stub arm and is not an adopter knob.
CARD_MEMORY_BOUND=${CARD_MEMORY_BOUND:-5}
# The `## pointers` section's two bounds, in seconds (KICK-dKeptSession-13): the loop kit's item boundary,
# `position.py --boundary`, PINNED 2026-11-21 at KICK-dKeptSession-15's figure for the same read, above the
# 7.3 s measured over dKeptSession; and the records reader, `gen_build_index.py --latest-records`. The env
# overrides exist for the self-test's slow-stub arms, as CARD_CLI_BOUND's does; neither is an adopter knob.
CARD_POSITION_BOUND=${CARD_POSITION_BOUND:-10}
CARD_RECORDS_BOUND=${CARD_RECORDS_BOUND:-5}
# The `budget —` line's bound on the loop kit's `budget.py state`, in seconds (KICK-dKeptSession-26),
# PINNED 2026-11-21: the module reads the build's homes with no remote call, and its `ending` verb, the
# same read and more, took 1.1 s over dKeptSession. The env override exists for the self-test's stub
# fixture, as CARD_CLI_BOUND's does, and is not an adopter knob.
CARD_BUDGET_BOUND=${CARD_BUDGET_BOUND:-10}
# The `context —` line's bound on the runlog kit's `runlog.py context <transcript>`, in seconds
# (KICK-dKeptSession-14 S5), the map's own figure, above the 1.5 s a main-file parse of a 232 MB
# transcript took, PINNED 2026-11-21 by that unit. The env override exists for the self-test's slow-stub
# plant, as CARD_MAP_BOUND's does, and is not an adopter knob.
CARD_CONTEXT_BOUND=${CARD_CONTEXT_BOUND:-5}
# The lines a stored `## pointers` section holds, the one list `check_card_pointers` reads: each later
# session unit appends its own word (KICK-dKeptSession-26 `budget`, KICK-dKeptSession-5 `mail`).
POINTER_LINES="records forks item budget"
# The `claims —` cell's three constants (TOOL-aGraftedHelix-2): the read's bound in seconds, the
# second clock's hide age, and the row cap. The bound's env override exists for the self-test's
# slow-driver arm, as CARD_CAP_BYTES's does; none of the three is an adopter knob.
CARD_CLAIMS_BOUND=${CARD_CLAIMS_BOUND:-15}
CARD_CLAIMS_HIDE_S=86400
CARD_CLAIMS_ROWS=8
# The `health —` cell's window (TOOL-aGraftedHelix-8): every card counts the same last 24 hours of the
# health log, because cards are per session and "since the previous card" would be whichever card
# another session wrote seconds earlier and never read. Not an adopter knob.
HEALTH_WINDOW_S=86400
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

# The session id, in PRECEDENCE order: `--session` answers FIRST and SUPPRESSES the stdin read;
# only a caller that passed none falls through to the `{"session_id": …}` JSON the SessionStart hook
# hands on stdin. That order is the fix for TOOL-cMendedVintage-9 and supersedes the stdin-first one
# KICK-aReplayedCard-1 §S2 recorded: `[ -t 0 ]` admits a terminal and the hook's closing pipe, and
# not the third case — the never-closing pipe every tool-invoked shell hands its child — on which
# the `sed` below blocks forever, including for a caller that had already answered by flag.
# Neither channel is a refusal naming both, never a card under a guessed id; a separator, `..` or
# any byte outside [A-Za-z0-9._-] is refused before it can be joined into a path. `--append` never
# reads stdin here — stdin is the body it stores — so it takes `--session` alone. The payload is read
# ONCE, and its `cwd` kept in CARD_CWD for the card file's tree (PLAY-dOrderedCharter-8 S2); JSON's
# escaped backslash reads as `/`, the spelling git accepts on every host. The same read keeps the
# payload's `transcript_path` in CARD_TRANSCRIPT, unescaped alike, and its `source` in CARD_SOURCE, the
# card file's owner and its `clear` takeover (PLAY-dOrderedCharter-54 S1); no payload leaves both empty.
CARD_CWD=""; CARD_TRANSCRIPT=""; CARD_SOURCE=""
read_session_id() {
  local sid="" payload="" re_sid='"session_id"[[:space:]]*:[[:space:]]*"([^"]*)"' re_cwd='"cwd"[[:space:]]*:[[:space:]]*"([^"]*)"'
  local re_tx='"transcript_path"[[:space:]]*:[[:space:]]*"([^"]*)"' re_src='"source"[[:space:]]*:[[:space:]]*"([^"]*)"'
  [ "$CARD_VERB" = append ] || [ -n "$CARD_SID" ] || [ -t 0 ] || payload=$(cat)
  [[ $payload =~ $re_sid ]] && sid=${BASH_REMATCH[1]}
  # ponytail: a POSIX directory whose name holds a backslash reads wrong here, and the tree falls back to $ROOT
  [[ $payload =~ $re_cwd ]] && CARD_CWD=${BASH_REMATCH[1]//\\\\//}
  [[ $payload =~ $re_tx ]] && CARD_TRANSCRIPT=${BASH_REMATCH[1]//\\\\//}
  [[ $payload =~ $re_src ]] && CARD_SOURCE=${BASH_REMATCH[1]}
  [ -n "$sid" ] || sid="$CARD_SID"
  if [ -z "$sid" ] && [ "$CARD_VERB" = append ]; then
    echo "MANIFEST env ERROR — --card --append has no session id: stdin is the body, so pass --session <sid>"; exit 2
  fi
  [ -n "$sid" ] || { echo "MANIFEST env ERROR — --card --$CARD_VERB has no session id: none in the JSON on stdin (the SessionStart hook's channel) and no --session <sid> given"; exit 2; }
  case "$sid" in
    *..*) echo "MANIFEST env ERROR — session id '$sid' carries '..' and is not joined into a path"; exit 2 ;;
  esac
  printf '%s' "$sid" | grep -qE '^[A-Za-z0-9][A-Za-z0-9._-]*$' \
    || { echo "MANIFEST env ERROR — session id '$sid' carries a path separator or a byte outside [A-Za-z0-9._-] and is not joined into a path"; exit 2; }
  CARD_SID="$sid"
}

# The session's Claude Code version, read from `AI_AGENT` by the unattended driver's rule, spelled again
# here because this kit names no file of another: a `claude-code_` prefix, the field before the next
# `_`, dashes as dots, two to four integers. ONE READER (KICK-dKeptSession-12 S1): the `cli —` cell and
# the card-import fixture's verdict both ask it. It assigns the variable its argument names by `printf
# -v`, as `getval` does, so no caller forks a subshell to read it (KICK-dKeptSession-69 S8); that name
# is never `_rv`, the one local here, which `printf -v` would write instead.
read_session_cli_version() { # VAR -> VAR set to the version; 1 and VAR empty when AI_AGENT names none
  local _rv=""
  printf -v "$1" '%s' ''
  case "${AI_AGENT:-}" in claude-code_*) _rv=${AI_AGENT#claude-code_}; _rv=${_rv%%_*}; _rv=${_rv//-/.} ;; esac
  [[ $_rv =~ ^[0-9]+(\.[0-9]+){1,3}$ ]] || return 1
  printf -v "$1" '%s' "$_rv"
}

# PATH's `claude` version, ONE READ (KICK-dKeptSession-37 S1): the `cli —` cell and the card-import
# fixture's verdict both ask it, so the bound and the parse live once. Bounded by CARD_CLI_BOUND and
# landed in a scratch file under the card dir, never a `$( )` capture a grandchild could hold open;
# the first token of two to four integers on the first line it prints.
read_claude_version() { # -> the version, 0; or `unknown: <why>`, 1
  local p="" t sf rc
  local -a toks
  command -v claude >/dev/null 2>&1 || { printf 'unknown: no claude on PATH\n'; return 1; }
  sf="$CARD_DIR/.cli.$$"
  mkdir -p "$CARD_DIR" 2>/dev/null
  timeout -k 2 "$CARD_CLI_BOUND" claude --version </dev/null >"$sf" 2>/dev/null; rc=$?
  [ -f "$sf" ] && read -r -a toks < "$sf"
  rm -f "$sf" 2>/dev/null
  case "$rc" in 124|137) printf 'unknown: claude --version did not answer within %ss\n' "$CARD_CLI_BOUND"; return 1 ;; esac
  for t in ${toks[@]+"${toks[@]}"}; do
    t=${t%$'\r'}
    [[ $t =~ ^[0-9]+(\.[0-9]+){1,3}$ ]] && { p=$t; break; }
  done
  [ -n "$p" ] || { printf 'unknown: claude --version printed no version\n'; return 1; }
  printf '%s\n' "$p"
}

# THE CARD-IMPORT FIXTURE'S VERDICT (KICK-dKeptSession-12 S1, S2): one line in the card directory,
# `card-fixture — <verdict> · fixture <blob8> · cli <version> · <iso>`, node-local because the harness
# that compacts is the node's, and overwritten by every `--card --fixture-run`. The verdict is `pass`
# for the fixture's exit 0, `red <limb>` for exit 1 with the limb its last line names after `FAILED
# limb`, `absent` for its could-not-run exit 2, and `red exit <rc>` otherwise; the blob is `git
# hash-object` over the fixture, the version `read_claude_version`'s, read just before the fixture runs,
# so it names the binary the fixture's `claude -p` resolves and never the session's (KICK-dKeptSession-37
# S2), else `unknown`. The writer writes nothing outside the scratch directory but this file and the
# version read's scratch file, which it removes; the fixture's harness keeps its own
# transcripts, the one write it names. WHAT THIS DOES NOT CHECK: that the fixture judged anything — a
# stub under CARD_FIXTURE records a pass as readily as the real one, and the blob is what tells them apart.
write_card_fixture_verdict() { # scratch dir -> the line it wrote; 2 with nothing written when no fixture runs
  local dir=$1 out rc verdict blob ver at line re_limb='FAILED limb ([A-Za-z0-9]+)'
  [ -f "$CARD_FIXTURE" ] || { echo "MANIFEST env ERROR — no card-import fixture at $CARD_FIXTURE, so nothing ran and no verdict was written"; return 2; }
  blob=$(git hash-object -- "$CARD_FIXTURE" 2>/dev/null) && [ -n "$blob" ] \
    || { echo "MANIFEST env ERROR — git hash-object could not read $CARD_FIXTURE, so nothing ran and no verdict was written"; return 2; }
  case "$dir" in /*|[A-Za-z]:*) ;; *) dir="$CALLER_PWD/$dir" ;; esac
  ver=$(read_claude_version) || ver=unknown
  out=$(bash "$CARD_FIXTURE" "$dir" </dev/null 2>&1); rc=$?
  out=${out//$'\r'/}
  case "$rc" in
    0) verdict=pass ;;
    1) verdict="red exit 1"; [[ ${out##*$'\n'} =~ $re_limb ]] && verdict="red ${BASH_REMATCH[1]}" ;;
    2) verdict=absent ;;
    *) verdict="red exit $rc" ;;
  esac
  printf -v at '%(%Y-%m-%dT%H:%M:%S%z)T' -1
  line="card-fixture — $verdict · fixture ${blob:0:8} · cli $ver · $at"
  { mkdir -p "$CARD_DIR" && printf '%s\n' "$line" > "$CARD_DIR/$CARD_FIXTURE_VERDICT"; } 2>/dev/null \
    || { echo "MANIFEST env ERROR — cannot write $CARD_DIR/$CARD_FIXTURE_VERDICT, so the fixture's $verdict is unrecorded"; return 2; }
  printf '%s\n' "$line"
}

# The verdict's reader, which `derive_resume_lines`' `always-resume` arm asks: `pass` only while the
# recorded verdict is `pass`, its blob is the installed fixture's now, and its version is both PATH's
# `claude`'s now, `read_claude_version`'s, and the session's now, `read_session_cli_version`'s
# (KICK-dKeptSession-38 S1); otherwise one `red: <why>` line. The tests run in that order and the first
# that fails answers, so a recorded red keeps its own reason and a verdict that is no pass spawns no
# `claude --version`. An unknown version on any side is red, never an equality (S2). A line off the
# writer's grammar reads as no run, so the override can only fail towards recommending a fresh session.
read_card_fixture_verdict() { # -> pass, or red: <why>; one line on stdout, 0 always
  local l="" v old8 oldv blob p="" s=""
  local re='^card-fixture — (pass|absent|red [A-Za-z0-9 ]+) · fixture ([0-9a-f]{8}) · cli ([0-9]+(\.[0-9]+){1,3}|unknown) · [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+-][0-9]{4}$'
  [ -f "$CARD_FIXTURE" ] || { echo "red: no fixture installed"; return 0; }
  [ -f "$CARD_DIR/$CARD_FIXTURE_VERDICT" ] && IFS= read -r l < "$CARD_DIR/$CARD_FIXTURE_VERDICT"
  l=${l%$'\r'}
  [[ $l =~ $re ]] || { echo "red: no recorded run"; return 0; }
  v=${BASH_REMATCH[1]}; old8=${BASH_REMATCH[2]}; oldv=${BASH_REMATCH[3]}
  [ "$v" = pass ] || { echo "red: $v"; return 0; }
  blob=$(git hash-object -- "$CARD_FIXTURE" 2>/dev/null); blob=${blob:-unhashed}
  [ "${blob:0:8}" = "$old8" ] || { echo "red: recorded for fixture $old8, now ${blob:0:8}"; return 0; }
  [ "$oldv" != unknown ] || { echo "red: cli version unknown · recorded"; return 0; }
  p=$(read_claude_version) || { echo "red: cli version unknown · PATH"; return 0; }
  read_session_cli_version s || { echo "red: cli version unknown · session"; return 0; }
  [ "$p" = "$oldv" ] || { echo "red: recorded under cli $oldv, PATH now $p"; return 0; }
  [ "$s" = "$oldv" ] || { echo "red: fixture ran cli $oldv, this session runs $s"; return 0; }
  echo pass
}

# `--path` answers here, before the manifest resolves: it needs the repository (for the common dir)
# and the id, and nothing else. Print-only, exit 0, no `fail` branch — the `--locations` shape.
if [ -n "$CARD" ]; then
  CARD_DIR=$(cd "$(git rev-parse --git-common-dir 2>/dev/null)" 2>/dev/null && pwd) \
    || { echo "MANIFEST env ERROR — cannot resolve the git common dir, so the card has no home"; exit 2; }
  CARD_DIR="$CARD_DIR/orientation"
  # The build card's cache path is keyed by the build, so it needs no session (TOOL-dPlacedRequest-2 S10).
  [ "$CARD_VERB:${CARD_BUILD:+b}" = path:b ] && { printf '%s/%s.md\n' "$CARD_DIR" "$CARD_BUILD"; exit 0; }
  # The fixture's run judges the node's harness, not a session's, so it takes no session and reads no
  # stdin, and answers before `read_session_id`, which would refuse it or wait on stdin (KICK-dKeptSession-12 S1).
  [ "$CARD_VERB" != fixture-run ] || { write_card_fixture_verdict "$CARD_FIXTURE_DIR"; exit $?; }
  # A follow runs from the loop kit's transition writer, which holds no session: the card names the
  # harness's session where one is in the environment, else `none`.
  [ "$CARD_VERB" != follow ] || [ -n "$CARD_SID" ] || CARD_SID=${CLAUDE_CODE_SESSION_ID:-none}
  # A pointers publish with no session names a build card alone, and is by that session or `none` alike.
  [ "$CARD_VERB" != pointers ] || [ -n "$CARD_SID" ] || CARD_SID=${CLAUDE_CODE_SESSION_ID:-none}
  read_session_id
  # The boundary verb's transcript, for the card file's owner line (KICK-dKeptSession-13 S6).
  [ -z "$CARD_TX_ARG" ] || CARD_TRANSCRIPT=$CARD_TX_ARG
  CARD_FILE="$CARD_DIR/$CARD_SID.md"
  [ "$CARD_VERB" = path ] && { printf '%s\n' "$CARD_FILE"; exit 0; }
  # The session's own tree, resolved once: the payload's `cwd` when git places it in a repository.
  CARD_TREE=$ROOT
  if [ -n "$CARD_CWD" ] && _ct=$(unset GIT_DIR GIT_WORK_TREE; git -C "$CARD_CWD" rev-parse --show-toplevel 2>/dev/null) && [ -n "$_ct" ]; then
    CARD_TREE=${_ct%$'\r'}
  fi
fi

STAGED=0; MF=""
for a in "$@"; do
  case "$a" in
    --staged) STAGED=1 ;;
    *) MF="$a" ;;
  esac
done

# Resolve a path argument: repo-root-relative first, then caller-cwd-relative; never outside the
# repo. Membership is decided by git identity (file's toplevel == this ROOT, both normalized the
# same way), never by path-string comparison — under MSYS one directory has two spellings
# (/tmp/x vs /c/.../Temp/x) and realpath can't unify them (mount points aren't symlinks).
if [ -n "$MF" ]; then
  case "$MF" in
    /*|[A-Za-z]:*) abs="$MF" ;;
    *) if [ -f "$ROOT/$MF" ]; then abs="$ROOT/$MF"; else abs="$CALLER_PWD/$MF"; fi ;;
  esac
  [ -f "$abs" ] || { echo "MANIFEST env ERROR — '$MF' not found (tried the repo root, then $CALLER_PWD)"; exit 2; }
  dir=$(cd "$(dirname -- "$abs")" 2>/dev/null && pwd) || dir=""
  froot=""
  if [ -n "$dir" ]; then
    froot=$(unset GIT_DIR GIT_WORK_TREE; git -C "$dir" rev-parse --show-toplevel 2>/dev/null) || froot=""
    [ -n "$froot" ] && { froot=$(cd "$froot" 2>/dev/null && pwd) || froot=""; }
  fi
  if [ -z "$froot" ] || [ "$froot" != "$ROOT" ]; then
    echo "MANIFEST env ERROR — '$MF' resolves outside this repository"; exit 2
  fi
  MF="$(unset GIT_DIR GIT_WORK_TREE; git -C "$dir" rev-parse --show-prefix 2>/dev/null)$(basename -- "$abs")"
else
  for p in $MANIFEST_LOCATIONS; do
    [ -f "$p" ] && { MF="$p"; break; }
  done
fi

# The audit block's text, CR-stripped; `getval` reads one key from it. Defined here because the card
# reads the block's `registry:` key before the checks below ever run, and one reader is one reader.
# Both are read on every commit by the staged leg, so neither pipes (KICK-aTrimmedHook-1): the CR goes
# inside the one awk, and the key is matched in the shell. `getval KEY VAR` answers what the retired
# `sed | head | sed` did: the FIRST matching line, the value after the colon with leading and
# trailing whitespace removed, and the empty string when no line matches. It assigns VAR by
# `printf -v` instead of printing, so no caller forks a subshell to capture it, and it empties VAR
# first because `LBC` has no initialiser and would otherwise keep a value the environment exported.
# VAR is never `_gl` or `_gre`: `printf -v` into a name declared local here writes this copy.
read_block() { awk '{ gsub(/\r/, "") } /<!-- manifest-audit/{f=1;next} f&&/-->/{exit} f' "$1"; }
getval() {
  local _gl _gre="^[[:space:]]*$1:[[:space:]]*(.*)$"
  printf -v "$2" '%s' ''
  while IFS= read -r _gl; do
    if [[ $_gl =~ $_gre ]]; then
      _gl=${BASH_REMATCH[1]}
      printf -v "$2" '%s' "${_gl%"${_gl##*[![:space:]]}"}"
      return 0
    fi
  done <<<"$BLOCK"
}

# The `node —` cell: the FIRST table under a `## Node registry` heading of the file the manifest's
# `registry:` key names, backticks stripped, `$USERNAME` (else `$USER`) matched against the
# Machine/user cell's user, the text before ` @` — never row-wide, because the Remote column repeats
# one github user on every row and a row-wide match hits all of them. No unique match is UNKNOWN with
# the reason, printed, never guessed; the card still writes. ONE REGISTRY, ONE RULE
# (TOOL-dPlacedRequest-43 S20): the table is the one the playbook kit's `derive_node_table` renders
# from `fleet.toml`, and the user is case-folded and equal to the row's, `read_fleet_tag`'s rule, which
# the unattended driver's `resolve_fleet_tag` asks. It stays a read of the rendered table because this
# kit is copy-installed and carries no playbook kit. GOV_NODE FIRST (TOOL-dPlacedRequest-49 S23, F4):
# a set GOV_NODE names the row whose Tag cell it equals, as `resolve_node_tag` and `resolve_fleet_tag`
# answer it first, so the three resolvers agree on a node that sets it; one naming no row is UNKNOWN
# with the reason, and the user is not read.
derive_node_tag() {
  local reg="$1" user="${USERNAME:-${USER:-}}" node="${GOV_NODE:-}" hits tag mu
  [ -n "$reg" ] || { printf 'node — UNKNOWN: no registry\n'; return 0; }
  [ -f "$reg" ] || { printf 'node — UNKNOWN: registry %s is not a file in this tree\n' "$reg"; return 0; }
  [ -n "$node$user" ] || { printf 'node — UNKNOWN: neither USERNAME nor USER names a user\n'; return 0; }
  IFS=$'\t' read -r hits tag mu < <(awk -v user="$user" -v node="$node" '
    { ln=$0; sub(/\r$/,"",ln) }
    !intab && ln ~ /^## Node registry/ { sect=1; next }
    sect && !intab && ln ~ /^## / { exit }
    sect && !intab && ln ~ /^\|/ { intab=1 }
    intab && ln !~ /^\|/ { exit }
    !intab { next }
    { gsub(/`/,"",ln); split(ln, c, "|"); tag=c[2]; mu=c[3]
      gsub(/^[ \t]+|[ \t]+$/,"",tag); gsub(/^[ \t]+|[ \t]+$/,"",mu)
      if (tag=="Tag" || tag ~ /^:?-+:?$/) next
      mt=mu; i=index(mt, " @"); if (i) mt=substr(mt, 1, i-1)
      if (node != "" ? (tag == node) : (tolower(mt) == tolower(user))) { hits++; found=tag; foundmu=mu } }
    END { printf "%d\t%s\t%s\n", hits+0, found, foundmu }' "$reg")
  case "$hits:${node:+node}" in
    1:*) printf 'node — %s · %s\n' "$tag" "$mu" ;;
    0:node) printf 'node — UNKNOWN: GOV_NODE %s names no Tag cell in %s\n' "$node" "$reg" ;;
    0:) printf 'node — UNKNOWN: no Machine/user cell in %s matches %s\n' "$reg" "$user" ;;
    *:node) printf 'node — UNKNOWN: %s Tag cells in %s read GOV_NODE %s\n' "$hits" "$reg" "$node" ;;
    *) printf 'node — UNKNOWN: %s Machine/user cells in %s match %s\n' "$hits" "$reg" "$user" ;;
  esac
}

# The `cli —` cell (KICK-aMendedFleet-4): PATH's `claude --version` against the running session's
# version. The session's is `read_session_cli_version`'s, the one reader of `AI_AGENT`, and PATH's
# `read_claude_version`'s, the one read of that binary, whose `unknown:` reason is the `skipped:` line.
# Fields compare as integers, a missing one as 0; every failure is its own `skipped:` line, and none
# moves the card's exit.
derive_cli_line() {
  local s="" p="" c=0 i
  local -a a b
  read_session_cli_version s || { printf 'cli — skipped: AI_AGENT names no Claude Code version\n'; return 0; }
  p=$(read_claude_version) || { printf 'cli — skipped: %s\n' "${p#unknown: }"; return 0; }
  a=(${p//./ }); b=(${s//./ })
  for i in 0 1 2 3; do
    (( 10#${a[i]:-0} == 10#${b[i]:-0} )) && continue
    if (( 10#${a[i]:-0} < 10#${b[i]:-0} )); then c=-1; else c=1; fi
    break
  done
  case "$c" in
    0) printf 'cli — %s · PATH claude matches this session\n' "$s" ;;
    -1) printf "cli — NOTE: PATH claude %s is older than this session's %s, so a session started from PATH runs the older CLI\n" "$p" "$s" ;;
    *) printf "cli — PATH claude %s is newer than this session's %s\n" "$p" "$s" ;;
  esac
}

# The `drift —` cell (KICK-aMendedFleet-1): the LAST group of `drift-history.tsv` in the git common
# dir, the file every bar's `drift-audit records` leg appends to (TOOL-aMendedFleet-48). It READS that
# file and never runs the report: one `head` and one `tail -n 400` into one C-locale awk, so the
# 320-byte cut is a byte count. Columns are found by the header, one leading `#` stripped; a line
# whose field count differs from the header's is a write in progress and is skipped. The group is
# every trailing row sharing the last complete row's utc and sha. Callers run `derive_head_state`.
derive_drift_line() {
  local hist="${CARD_DIR%/orientation}/drift-history.tsv"
  [ -f "$hist" ] || { printf 'drift — skipped: no drift-history.tsv in the git common dir\n'; return 0; }
  { head -n 1 "$hist"; tail -n 400 "$hist"; } | LC_ALL=C awk -F'\t' -v head="$HEAD_SHA" '
    { sub(/\r$/, "") }
    NR == 1 { nf = NF
      for (i = 1; i <= NF; i++) { h = $i; sub(/^#/, "", h); col[h] = i }
      split("utc sha signal state value of", need, " ")
      for (i = 1; i <= 6; i++) if (!(need[i] in col)) { missing = need[i]; exit }
      next }
    $1 ~ /^#/ || NF != nf { next }
    { n++; key[n] = $col["utc"] "\t" $col["sha"]; sig[n] = $col["signal"]; st[n] = $col["state"]
      val[n] = $col["value"]; of[n] = $col["of"]; utc[n] = $col["utc"]; sha[n] = $col["sha"] }
    END {
      if (missing != "") { printf "drift — UNKNOWN: drift-history.tsv header lacks %s\n", missing; exit }
      if (n == 0) { print "drift — skipped: drift-history.tsv holds no reading"; exit }
      for (s = n; s > 1 && key[s - 1] == key[n]; s--) ;
      g = n - s + 1; z = 0; d = 0; m = 0
      for (i = s; i <= n; i++) {
        if (st[i] == "dead") { d++; names[++m] = sig[i] " DEAD" }
        else if (st[i] == "live" && val[i] ~ /^[0-9]+$/ && val[i] + 0 > 0) { z++; nz[z] = i }
      }
      for (i = 2; i <= z; i++) for (j = i; j > 1 && val[nz[j]] + 0 > val[nz[j - 1]] + 0; j--) {
        t = nz[j]; nz[j] = nz[j - 1]; nz[j - 1] = t }
      for (i = 1; i <= z; i++) names[++m] = sig[nz[i]] "=" val[nz[i]] "/" of[nz[i]]
      line = sprintf("drift — last bar %s at %s · %s · %d signals · %d nonzero · %d dead", utc[n],
        substr(sha[n], 1, 8), (sha[n] == head ? "HEAD" : "not HEAD"), g, z, d)
      for (i = 1; i <= m; i++) {
        add = (i == 1 ? " · " : ", ") names[i]
        if (length(line add) + (i < m ? 24 : 0) > 320) { line = line (i == 1 ? " · " : ", ") "… " (m - i + 1) " more"; break }
        line = line add
      }
      print line
    }'
}

# The startup card, rendered from facts a script can derive: it runs no fetch of its own, moves no
# branch or remote-tracking ref, writes no FETCH_HEAD and runs no manifest audit — the engine's
# Step 1 and Step 2b own those and each costs a kickoff, not a session start. Its one remote contact
# is the bounded `claims —` read below; the `overlaps —` read sees local remote-tracking refs only.
# `$1` names the writer verb the header carries; a card the replay wrote fresh says `--card --replay`,
# which is the one byte-level fact that tells a session started before the writer was wired from one
# whose startup ran it. The `live —` cell reads the memory-tree conf when there is one and reports
# `skipped:` otherwise, because this kit requires no other kit. The `cli —` cell, directly after
# `node —`, is `derive_cli_line`: PATH's `claude --version` against the session's own version from
# `AI_AGENT`, a NOTE when PATH is older, one line always. The `drift —` cell, between
# `worktrees —` and `live —`, is `derive_drift_line`: the last group of `drift-history.tsv` in the
# git common dir, read from that file and never from a report run. The `overlaps —` cell, after any
# `drift —` cell and before `live —`, is `derive_overlaps_line`: the unattended driver's
# `--overlaps`, which reads local remote-tracking refs and never the network. The `claims —` cell,
# after `live —`, is `derive_claims_line`, and the `health —` cell after it, above `recent —`, is
# `render_health_cell`. The `memory —` cell, between `live —` and `claims —`, is `derive_memory_line`.
derive_head_state() {   # → HEAD_BRANCH HEAD_SHA HEAD_DIRTY, read once by the card and once by the `now —` line
  local n
  HEAD_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null) || HEAD_BRANCH=HEAD
  HEAD_SHA=$(git rev-parse -q --verify 'HEAD^{commit}' 2>/dev/null) || HEAD_SHA=unborn
  n=$(git status --porcelain 2>/dev/null | wc -l | tr -d '[:space:]')
  if [ "$n" -eq 0 ]; then HEAD_DIRTY=clean; else HEAD_DIRTY="dirty $n"; fi
}
# The memory tree's root, the one read of `MEMORY_ROOT` in this script: the `live —` cell and the
# route rules both call it. Prints the value, empty when the conf declares none; returns 1 when the
# tree has no `.memory-tree.conf` at all, so a caller can tell the two apart. The conf is SOURCED in a
# subshell, as `derive_routed_candidate` in the memory-tree adopter does, so an exported, quoted,
# commented or twice-assigned spelling reads as the value bash gives it (TOOL-aRoutedQuill-12 S1).
read_memory_root() {
  local v
  [ -f "$ROOT/.memory-tree.conf" ] || return 1
  v=$( set +u; unset MEMORY_ROOT; . "$ROOT/.memory-tree.conf" >/dev/null 2>&1; printf '%s' "${MEMORY_ROOT-}" )
  printf '%s' "${v%$'\r'}"
}
render_card() {
  local verb="$1" registry="" memroot live body
  [ -n "$MF" ] && [ -f "$MF" ] && { BLOCK=$(read_block "$MF"); getval 'registry' registry; }
  derive_head_state
  if ! memroot=$(read_memory_root); then
    live='live — skipped: no .memory-tree.conf in this tree'
  else
    if [ -z "$memroot" ]; then
      live='live — skipped: .memory-tree.conf declares no MEMORY_ROOT'
    elif [ ! -f "$ROOT/$memroot/LIVE.md" ]; then
      live="live — skipped: $memroot/LIVE.md is absent"
    else
      live="live — LIVE.md · $(awk '/^\|/ && !/^\|[-|: ]*$/ {n++} END{print (n>0?n-1:0)}' "$ROOT/$memroot/LIVE.md") non-terminal builds"
    fi
  fi
  # The cells below the header first, so the `keys —` cell's remote key is taken after the `claims —`
  # read has fetched; then the header, that cell and the cells, in that order (TOOL-dDeclaredLoop-8 S5).
  body=$(
    derive_node_tag "$registry"
    derive_cli_line
    render_tree_cell
    printf 'worktrees — %s\n' "$(git worktree list 2>/dev/null | wc -l | tr -d '[:space:]')"
    derive_drift_line
    derive_overlaps_line
    printf '%s\n' "$live"
    derive_memory_line
    derive_claims_line "$verb"
    render_health_cell
    printf 'recent —\n'
    git log --oneline -5 2>/dev/null
    printf 'READY — none yet\n'
  )
  printf 'orientation — %s · written %s · by %s --card --%s\n' "$CARD_SID" "$(date +%Y-%m-%dT%H:%M:%S%z)" "${0##*/}" "$verb"
  render_keys_cell
  printf '%s\n' "$body"
}

# The `keys —` cell (TOOL-dDeclaredLoop-8 S5): the loop kit's `claims.py card-keys` over this tree, found
# as every sibling is by `resolve_kit_file`, printed as `keys — view <k> · remote <k> · at <iso>`. Each
# cell joins one of the two keys by its class, declared in that module's CARD_CELL_CLASSES: `overlaps —`
# and `claims —` the remote key, every other cell the view key. No loop kit, no python or a key read
# that fails is one `keys — skipped:` line, and the card still writes.
# WHAT THIS DOES NOT CHECK: the `cli —`, `worktrees —`, `drift —`, `memory —` and `health —` cells' own
# inputs, which sit outside the commit and the refs, so the view key does not move with them.
render_keys_cell() {
  local ck py out rc
  ck=$(resolve_kit_file loop claims.py)
  [ -n "$ck" ] || { printf 'keys — skipped: no loop kit resolves in this tree\n'; return 0; }
  py=$(resolve_python 2>/dev/null) || { printf 'keys — skipped: no Python resolves on this node\n'; return 0; }
  out=$("$py" "$ck" card-keys 2>/dev/null); rc=$?
  [ "$rc" = 0 ] || { printf 'keys — skipped: card-keys exited %s\n' "$rc"; return 0; }
  printf '%s\n' "$out" | awk '{ sub(/\r$/, "") } $1 == "view" { v = $2 } $1 == "remote" { r = $2 } $1 == "at" { a = $2 }
    END { if (v == "" || r == "" || a == "") print "keys — skipped: card-keys printed no view, remote and at lines"
          else print "keys — view " v " · remote " r " · at " a }'
}

# The `overlaps —` cell (KICK-aMendedFleet-2): which unmerged remote refs share a path with this
# tree's branch, read through the unattended kit's own `--overlaps` and never joined here, because
# the driver owns the join, its exclusions and its wording. The card parses nothing inside the
# probe's lines: the first prints verbatim, later ones indented and cut. THE BOUND IS A KILL INTO A
# FILE, never a `$( )` capture, which would wait for any grandchild holding the pipe; stdin is
# /dev/null, since the hook's pipe never closes; GOV_RUNLOG=0 keeps a card write out of the driver
# journal. Every failure is its own `skipped:` form, never a clean answer, and the card still writes.
# WHAT THIS DOES NOT CHECK: that the refs are fresh — they are as of this clone's last fetch.
derive_overlaps_line() {
  local sf rc
  sf=$(mkdir -p "$CARD_DIR" && mktemp "$CARD_DIR/.overlaps.XXXXXX") \
    || { printf 'overlaps — skipped: no scratch file under %s to capture the read in\n' "$CARD_DIR"; return 0; }
  run_driver_bounded "$CARD_OVERLAP_BOUND" "$sf" /dev/null --overlaps; rc=$?
  case "$rc${CARD_REF_WHY:+:skip}" in
    125:skip)
      printf 'overlaps — skipped: %s\n' "$CARD_REF_WHY" ;;
    0)
      # ponytail: a cut that splits a UTF-8 character drops the high bytes it left.
      LC_ALL=C awk -v cap="$CARD_OVERLAP_ROWS" '
        { sub(/\r$/, "") }
        NR == 1 { print "overlaps — " $0; next }
        { l = $0; sub(/^[ \t]+/, "", l); if (l == "") next
          if (++m > cap) next
          l = "  " l
          if (length(l) > 200) { l = substr(l, 1, 200); sub(/[\200-\377]+$/, "", l) }
          print l }
        END { if (NR == 0) print "overlaps — skipped: --overlaps exited 0 and printed nothing, so overlaps are unknown, not none"
              if (m > cap) printf "  … %d more\n", m - cap }' "$sf" ;;
    124|137)
      printf 'overlaps — skipped: --overlaps did not answer within %ss, so overlaps are unknown, not none\n' "$CARD_OVERLAP_BOUND" ;;
    *)
      LC_ALL=C awk -v rc="$rc" '{ sub(/\r$/, "") }
        NF && f == "" { f = $0 }
        END { if (f == "") f = "--overlaps exited " rc " and printed nothing"
              if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }
              print "overlaps — skipped: " f }' "$sf" ;;
  esac
  rm -f "$sf" 2>/dev/null
  return 0
}

# The `memory —` cell (PLAY-dOrderedCharter-14): the harness's auto-memory index measured against
# `memory.load-budget` and its standing directives counted, by the playbook kit's `memory_index.py
# measure`, found as every sibling is by `resolve_kit_file` and bounded as the `overlaps —` cell bounds
# its read: a kill into a scratch file under the card dir, never a `$( )` capture, stdin /dev/null. The
# measure derives the index's place itself, so this script spells no second project key; `--home` hands
# it this shell's `~`. Its first line prints on exit 0, and every failure is one `memory — skipped:` line.
# WHAT THIS DOES NOT CHECK: the line's figures, which are the measure's to derive and bound.
derive_memory_line() {
  local mi py sf rc
  mi=$(resolve_kit_file playbook memory_index.py)
  [ -n "$mi" ] || { printf 'memory — skipped: no playbook memory_index.py resolves in this tree\n'; return 0; }
  py=$(resolve_python 2>/dev/null) || { printf 'memory — skipped: no Python resolves on this node\n'; return 0; }
  timeout -k 1 5 true </dev/null >/dev/null 2>&1 \
    || { printf 'memory — skipped: this node has no working timeout -k, so the read would be unbounded and none ran\n'; return 0; }
  sf=$(mkdir -p "$CARD_DIR" && mktemp "$CARD_DIR/.memory.XXXXXX") \
    || { printf 'memory — skipped: no scratch file under %s to capture the measure in\n' "$CARD_DIR"; return 0; }
  timeout -k 2 "$CARD_MEMORY_BOUND" "$py" "$mi" measure ${HOME:+--home "$HOME"} </dev/null >"$sf" 2>/dev/null; rc=$?
  case "$rc" in
    0) LC_ALL=C awk '{ sub(/\r$/, "") } NR == 1 { print; f = 1 }
         END { if (!f) print "memory — skipped: the measure exited 0 and printed nothing" }' "$sf" ;;
    124|137) printf 'memory — skipped: the measure did not answer within %ss\n' "$CARD_MEMORY_BOUND" ;;
    *)
      LC_ALL=C awk -v rc="$rc" '{ sub(/\r$/, "") }
        NF && f == "" { f = $0 }
        END { if (f == "") f = "the measure exited " rc " and printed nothing"
              if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }
              print "memory — skipped: " f }' "$sf" ;;
  esac
  rm -f "$sf" 2>/dev/null
  return 0
}

# The `health —` cell (TOOL-aGraftedHelix-8): the I3 health log under the common dir `--card` already
# resolved for CARD_DIR, so the cell spawns no git, counted over the last HEALTH_WINDOW_S seconds. The
# window's start is a UTC stamp of I3's own spelling (GNU `date -d @<epoch>`, then BSD `-r`), and the
# stamps compare as text. At most four `<source> <event> ×<k>` pairs from the window, by count then by
# name. A line that is not four TAB fields or whose stamp is not I3's is `unreadable`, never an event.
# It sits ABOVE `recent —` because CARD_PARTS_AWK files everything after that block into the TAIL an
# append replaces. No time bound: one local file the appender caps at 500 lines, no network, no lock.
# WHAT THIS DOES NOT CHECK: whether a logged event was a real repair, or that any writer kit is
# installed here; an absent log says so (`none recorded`) rather than reporting a zero it never read.
render_health_cell() {
  local log now since
  log=$(derive_health_log "${CARD_DIR%/orientation}")
  [ -e "$log" ] || { printf 'health — none recorded: no health.log in the git common dir\n'; return 0; }
  { [ -f "$log" ] && [ -r "$log" ]; } || { printf 'health — skipped: health.log exists and cannot be read\n'; return 0; }
  now=$EPOCHSECONDS
  since=$(date -u -d "@$((now - HEALTH_WINDOW_S))" +%Y-%m-%dT%H:%M:%S+00:00 2>/dev/null) \
    || since=$(date -u -r "$((now - HEALTH_WINDOW_S))" +%Y-%m-%dT%H:%M:%S+00:00 2>/dev/null) || since=""
  [ -n "$since" ] || { printf 'health — skipped: date computes no UTC stamp for the window start on this host\n'; return 0; }
  awk -F '\t' -v since="$since" -v hours="$((HEALTH_WINDOW_S / 3600))" '
    { sub(/\r$/, "") }
    NF != 4 || $1 !~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9][+]00:00$/ { bad++; next }
    { all++; if ($1 >= since) { n++; k = $2 " " $3; if (!(k in c)) keys[++nk] = k; c[k]++ } }
    END {
      line = sprintf("health — %d in the last %dh of %d logged", n, hours, all)
      for (s = 1; s <= 4 && s <= nk; s++) {
        b = 0
        for (i = 1; i <= nk; i++) {
          if (keys[i] in done) continue
          if (!b || c[keys[i]] > c[keys[b]] || (c[keys[i]] == c[keys[b]] && keys[i] < keys[b])) b = i
        }
        done[keys[b]] = 1
        line = line sprintf(" · %s ×%d", keys[b], c[keys[b]])
      }
      if (nk > 4) line = line sprintf(" · +%d more kinds", nk - 4)
      if (bad) line = line sprintf(" · %d unreadable", bad)
      print line
    }' "$log"
}

# The `claims —` cell (TOOL-aGraftedHelix-2): the remote's run claims, read through the unattended
# kit's own `--claims` verb and never re-derived here, because the driver owns the claim format, the
# stale bound and the verdict table, and a second reader of them is a second implementation. That
# read moves no branch or remote-tracking ref and writes no FETCH_HEAD; the driver's private claim
# cache is the only ref namespace it touches. TWO CLOCKS: the driver's splits `live` from `stale`;
# this one hides a `stale`, `terminal` or `released` claim whose beat is older than CARD_CLAIMS_HIDE_S, and never
# a `live`, `held` or `unknown` one, which want a reader whatever their age. THE BOUND IS A KILL INTO
# A FILE: `timeout` kills its own process group, and a `$( )` capture would still wait for any
# grandchild holding the pipe, so the bound would decide the verdict and not the clock. stdin is
# /dev/null, since the hook's pipe never closes; GOV_RUNLOG=0 keeps a card write out of the driver
# journal the runlog kit reads as runs. Every failure is its own `skipped:` form, never `none`, and
# the card still writes. A replay reads no remote. THE SWITCH IS THE DRIVER'S (TOOL-aGraftedHelix-32):
# where RUN_CLAIMS is not `on`, `--claims` prints `claims: off` and reads nothing, and the cell says so;
# this card never reads the conf's switch itself, so the driver stays its one reader. WHAT THIS DOES
# NOT CHECK: who drives a slug, or whether a claim is honest — it prints what the driver answered.
# Each row is six TAB fields, the sixth the claim's key or `-` (TOOL-dDeclaredLoop-8 S7), printed as
# ` · key ` and the eight characters after `k1:`. The read asks `--claims --with-key`, and a row of five,
# from a driver released before the flag, which ignores it, prints ` · key -` (TOOL-dDeclaredLoop-56 S8),
# so neither side of a kit skew loses the cell. A `released` row, a build lease handed over at a run's
# end (TOOL-dPlacedRequest-16 S9), ranks beside `terminal` and hides under the same bound.
derive_claims_line() {   # $1 = the writer verb → the cell's head line and its rows
  local sd rc
  [ "$1" = replay ] && { printf 'claims — skipped: --card --replay reads no remote\n'; return 0; }
  sd=$(mkdir -p "$CARD_DIR" && mktemp -d "$CARD_DIR/.claims.XXXXXX") \
    || { printf 'claims — skipped: no scratch directory under %s to capture the read in\n' "$CARD_DIR"; return 0; }
  run_driver_bounded "$CARD_CLAIMS_BOUND" "$sd/out" "$sd/err" --claims --with-key; rc=$?
  case "$rc${CARD_REF_WHY:+:skip}" in
    125:skip)
      printf 'claims — skipped: %s\n' "$CARD_REF_WHY" ;;
    0)
      # Split on the TAB in awk, never `read`: an empty field collapses under `read`. Ordered by
      # verdict, then slug, so a busy remote cannot push a live claim off the card.
      # ponytail: insertion sort, O(n^2) over a card's handful of claims; sort(1) if a remote holds hundreds.
      LC_ALL=C awk -F'\t' -v hide="$CARD_CLAIMS_HIDE_S" -v cap="$CARD_CLAIMS_ROWS" '
        BEGIN { n = split("live held unknown stale terminal", o, " "); for (i = 1; i <= n; i++) rk[o[i]] = i; rk["released"] = rk["terminal"] }
        { sub(/\r$/, "") }
        $0 == "claims: none" { none = 1; next }
        $0 == "claims: off" { off = 1; next }
        (NF == 5 || NF == 6) && ($5 in rk) {
          all++
          if (($5 == "stale" || $5 == "terminal" || $5 == "released") && $4 ~ /^[0-9]+$/ && $4 + 0 > hide + 0) { hid++; next }
          k = rk[$5] "\t" $1
          r = "  " $1 " · " $2 " · " $3 " · beat " ($4 ~ /^[0-9]+$/ ? $4 "s" : "-") " · " $5 " · key " (NF == 6 && $6 ~ /^k1:/ ? substr($6, 4, 8) : "-")
          for (i = ++m; i > 1 && key[i - 1] > k; i--) { key[i] = key[i - 1]; row[i] = row[i - 1] }
          key[i] = k; row[i] = r; next
        }
        NF && bad == "" { bad = $0 }
        END {
          if (bad != "") { print "claims — skipped: --claims printed a line this card cannot read: " substr(bad, 1, 120); exit }
          if (all == 0) {
            if (off) print "claims — skipped: RUN_CLAIMS is off"
            else if (none) print "claims — none on the remote"
            else print "claims — skipped: --claims exited 0 with neither a claim row nor claims: none, so the remote'"'"'s claims are unknown, not none"
            exit
          }
          printf "claims — %d on the remote · %d shown · %d hidden\n", all, m, hid
          for (i = 1; i <= m && i <= cap; i++) print row[i]
          if (m > cap) printf "  … %d more\n", m - cap
        }' "$sd/out" ;;
    124|137)
      printf "claims — skipped: --claims did not answer within %ss, so the remote's claims are unknown, not none\n" "$CARD_CLAIMS_BOUND" ;;
    *)
      # The driver's first refusal line — `fail` prints to stdout — else its first line of any kind,
      # cut at 160 bytes. ponytail: a cut that splits a UTF-8 character drops the high bytes it left.
      LC_ALL=C awk -v rc="$rc" '{ sub(/\r$/, "") }
        NF && f == "" { f = $0 }
        /FAILED/ { f = $0; exit }
        END { if (f == "") f = "--claims exited " rc " and printed nothing"
              if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }
              print "claims — skipped: " f }' "$sd/out" "$sd/err" ;;
  esac
  rm -rf "$sd" 2>/dev/null
  return 0
}

# Persist the rendered card and print the same bytes. Rendered to a variable FIRST so an over-cap
# card leaves no file: every startup field is bounded, so an overflow means a derivation went wrong
# and a truncated card would carry that error into every later reader.
write_card() {
  local card bytes breach
  card=$(render_card "$1" | derive_pockets_block)
  bytes=$(printf '%s\n' "$card" | wc -c | tr -d '[:space:]')
  if [ "$bytes" -gt "$CARD_CAP_BYTES" ]; then
    echo "MANIFEST env ERROR — the startup card is $bytes bytes, $((bytes - CARD_CAP_BYTES)) over the $CARD_CAP_BYTES-byte cap (CARD_CAP_BYTES); a bounded derivation overflowed, so nothing was written"
    exit 2
  fi
  mkdir -p "$CARD_DIR" || { echo "MANIFEST env ERROR — cannot create $CARD_DIR"; exit 2; }
  printf '%s\n' "$card" > "$CARD_FILE" || { echo "MANIFEST env ERROR — cannot write $CARD_FILE"; exit 2; }
  breach=$(derive_injected_breaches)
  if [ -n "$breach" ]; then
    printf '%s\n' "$breach" >> "$CARD_FILE"
    card="$card"$'\n'"$breach"
  fi
  printf '%s\n' "$card"
}

# The injected load points, measured once the card is on disk (PLAY-dOrderedCharter-11 S5): the playbook
# kit's `load_sets.py injected` over the agent list, the Skill list and the card just written, its
# `injected — breach` lines kept and every other line dropped, so a card over nothing gains no line.
# The kit is found as every sibling is, by `resolve_kit_file`; no kit, no python or no working
# `timeout` adds nothing. CARD_INJECTED_CAPS hands in `<name>=<bytes>` caps the cap census does not hold.
# WHAT THIS DOES NOT CHECK: the harness's own composition of those lists, only the bytes they carry.
derive_injected_breaches() {
  local ls py caps=()
  ls=$(resolve_kit_file playbook load_sets.py)
  [ -n "$ls" ] || return 0
  py=$(resolve_python 2>/dev/null) || return 0
  timeout -k 1 5 true </dev/null >/dev/null 2>&1 || return 0
  read -ra caps <<< "${CARD_INJECTED_CAPS:-}"
  timeout -k 1 "${CARD_INJECTED_BOUND:-10}" "$py" "$ls" injected --root "$ROOT" --card "$CARD_FILE" \
    ${caps[@]+"${caps[@]/#/--cap=}"} </dev/null 2>/dev/null | tr -d '\r' | grep '^injected — breach'
  return 0
}

# The replay's `map —` block (PLAY-dOrderedCharter-4): the playbook kit's instruction map, its `map`
# verb's lines verbatim, found as every sibling is by `resolve_kit_file` and bounded as the `overlaps —`
# cell bounds its read: a kill into a scratch file under the card dir, never a `$( )` capture, stdin
# /dev/null. Every failure is one `map — skipped:` line; the replay's exit and the card file are never
# touched. WHAT THIS DOES NOT CHECK: the map's content, which is the verb's to derive and bound.
derive_map_block() {
  local iu py sf rc
  iu=$(resolve_kit_file playbook instruction_units.py)
  [ -n "$iu" ] || { printf 'map — skipped: no playbook instruction map resolves in this tree\n'; return 0; }
  py=$(resolve_python 2>/dev/null) || { printf 'map — skipped: no Python resolves on this node\n'; return 0; }
  timeout -k 1 5 true </dev/null >/dev/null 2>&1 \
    || { printf 'map — skipped: this node has no working timeout -k, so the read would be unbounded and none ran\n'; return 0; }
  sf=$(mkdir -p "$CARD_DIR" && mktemp "$CARD_DIR/.map.XXXXXX") \
    || { printf 'map — skipped: no scratch file under %s to capture the map in\n' "$CARD_DIR"; return 0; }
  # PLAY-dOrderedCharter-49 S73: the session's own tree, the payload's `cwd`, never the hook's working directory
  timeout -k 2 "$CARD_MAP_BOUND" "$py" "$iu" map --root "$CARD_TREE" </dev/null >"$sf" 2>/dev/null; rc=$?
  case "$rc" in
    0) tr -d '\r' < "$sf" ;;
    124|137) printf 'map — skipped: the map did not answer within %ss\n' "$CARD_MAP_BOUND" ;;
    *)
      LC_ALL=C awk -v rc="$rc" '{ sub(/\r$/, "") }
        NF && f == "" { f = $0 }
        END { if (f == "") f = "the map exited " rc " and printed nothing"
              if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }
              print "map — skipped: " f }' "$sf" ;;
  esac
  rm -f "$sf" 2>/dev/null
  return 0
}

# The card's `## pockets` section (TOOL-dPlacedRequest-9 S4): a composed card on stdin, printed with the
# section fitted to the card's one cap. Any stored section, the run from a `## pockets` or `pockets —
# skipped:` line up to the first `recent —` line, is taken out and the rest measured; the playbook kit's
# `pockets` verb is handed the room the cap leaves and its lines go in immediately above `recent —`. The
# verb is found as every sibling is, by `resolve_kit_file`, over the session's tree, and bounded as the
# `overlaps —` cell bounds its read: a kill into a scratch file under the card dir, stdin /dev/null. Every
# failure is one `pockets — skipped:` line, printed where it fits the room and omitted where it does not.
# A card is never refused for its pockets: a card whose other parts leave no room carries no section.
# WHAT THIS DOES NOT CHECK: the units' text, which is the verb's to compose, or the `injected — breach`
# lines `write_card` appends after its cap check, which sit outside the room as they sit outside that check.
derive_pockets_block() {
  local rest bytes room iu py sf rc block=""
  rest=$(awk '{ ln = $0; sub(/\r$/, "", ln) }
    !seen && (ln ~ /^## pockets$/ || ln ~ /^pockets — skipped: /) { skip = 1 }
    !seen && ln ~ /^recent —/ { seen = 1; skip = 0 }
    !skip { print ln }')
  bytes=$(printf '%s\n' "$rest" | wc -c | tr -d '[:space:]')
  room=$((CARD_CAP_BYTES - bytes))
  if [ "$room" -gt 0 ]; then
    iu=$(resolve_kit_file playbook instruction_units.py)
    if [ -z "$iu" ]; then
      block='pockets — skipped: no playbook instruction_units.py resolves in this tree'
    elif ! py=$(resolve_python 2>/dev/null); then
      block='pockets — skipped: no Python resolves on this node'
    elif ! timeout -k 1 5 true </dev/null >/dev/null 2>&1; then
      block='pockets — skipped: this node has no working timeout -k, so the read would be unbounded and none ran'
    elif ! sf=$(mkdir -p "$CARD_DIR" && mktemp "$CARD_DIR/.pockets.XXXXXX"); then
      block="pockets — skipped: no scratch file under $CARD_DIR to capture the section in"
    else
      timeout -k 2 "$CARD_POCKETS_BOUND" "$py" "$iu" pockets --root "$CARD_TREE" --room "$room" </dev/null >"$sf" 2>/dev/null; rc=$?
      case "$rc" in
        0) block=$(tr -d '\r' < "$sf") ;;
        124|137) block="pockets — skipped: the pockets verb did not answer within ${CARD_POCKETS_BOUND}s" ;;
        *)
          block=$(LC_ALL=C awk -v rc="$rc" '{ sub(/\r$/, "") }
            NF && f == "" { f = $0 }
            END { if (f == "") f = "the pockets verb exited " rc " and printed nothing"
                  if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }
                  print "pockets — skipped: " f }' "$sf") ;;
      esac
      rm -f "$sf" 2>/dev/null
    fi
    # Whatever printed it, a section or a skipped: line past the room is omitted, never cut.
    [ -z "$block" ] || [ "$(printf '%s\n' "$block" | wc -c | tr -d '[:space:]')" -le "$room" ] || block=""
  fi
  printf '%s\n' "$rest" | PK_BLOCK="$block" awk '!done && /^recent —/ { if (ENVIRON["PK_BLOCK"] != "") print ENVIRON["PK_BLOCK"]; done = 1 } { print }'
}

# The instruction map first, so the harness's cut of a hook's output takes a card's tail and never the
# map; then the stored card, re-keyed by `print_rekeyed_card`, then ONE `now —` line computed here and
# never stored — a second replay must print one, not two. The line names this tree's toplevel and how
# its keys read. A missing card is written fresh under the replay's own name in its header.
# THE RESUME (TOOL-dPlacedRequest-2 S7): a stored card whose `## route` names a build is first re-keyed
# from that build's card by `resolve_build_card`, and its `card —` line, the route re-check and the
# `resume —` and `partial —` lines print after the card, before the `now —` line.
REPLAY_KEYS=""
print_replay() {
  local build="" said="" keep
  # I10, THE REPLAY ORDER, stated here alone and fixed by the order of these calls (KICK-dKeptSession-12
  # S5): the map block, the stored card re-keyed, its `card —` line, then `derive_resume_lines`' `route —`,
  # `resume —` and `partial —` lines, then the computed lines the session units add after `partial —` —
  # `position —` and, after a compaction, its `lead —` notice (KICK-dKeptSession-15), then `context —`
  # (KICK-dKeptSession-14) — and the one `now —` line last.
  derive_map_block
  if [ -f "$CARD_FILE" ]; then
    build=$(read_card_build "$CARD_FILE")
    [ -z "$build" ] || said=$(resolve_build_card "$build")
    keep=$CARD_TMP
    print_rekeyed_card
    CARD_TMP=$keep
    [ -z "$build" ] || { printf '%s\n' "$said"; derive_resume_lines "$build"; }
  else
    write_card replay
    REPLAY_KEYS=$(awk '{ sub(/\r$/, "") } sub(/^keys — skipped: /, "keys skipped: ") { print; exit }
      /^keys — view / { print "keys view fresh · remote evidence"; exit }' "$CARD_FILE")
  fi
  render_position_line "$build"
  render_lead_notice
  render_context_line
  derive_head_state
  printf 'now — HEAD %s · %s · %s · %s · %s\n' "$HEAD_SHA" "$HEAD_BRANCH" "$HEAD_DIRTY" "$TOPLEVEL" "$REPLAY_KEYS"
}

# The replay's re-key (TOOL-dDeclaredLoop-8 S6, F5): the view key recomputed by `claims.py card-keys` in
# the tree the replay runs in and judged by its `verdict` against the stored `keys —` cell. A fresh key
# prints the stored card unchanged. A moved key, or a stored card with no `keys —` view key, re-renders
# the startup cells under `--card --replay` and carries, from the stored card, its header line, each
# cell `card-keys` names on its `remote-cells` line (the head line and the indented lines under it),
# the remote key and `at`, and its whole TAIL, the READY line and `## route` the scratch guard admits a
# commit by, byte for byte; the result is written under CARD_CAP_BYTES and printed. The header is
# carried because the scratch guard reads a `--card --replay` header as a session that started before
# the writer was wired. A replay reads no remote, so its remote verdict is always `evidence`. Sets
# REPLAY_KEYS, the `now —` line's tail. Over the cap, or with no scratch to build in, the stored card
# prints and nothing is written. WHAT THIS DOES NOT CHECK: the five cells whose inputs no key covers.
print_rekeyed_card() {
  local ck py out view cells stored verdict sd bytes
  REPLAY_KEYS="keys skipped: no loop kit resolves in this tree"
  ck=$(resolve_kit_file loop claims.py)
  [ -n "$ck" ] || { cat "$CARD_FILE"; return 0; }
  py=$(resolve_python 2>/dev/null) || { REPLAY_KEYS="keys skipped: no Python resolves on this node"; cat "$CARD_FILE"; return 0; }
  out=$("$py" "$ck" card-keys 2>/dev/null) || { REPLAY_KEYS="keys skipped: card-keys exited $?"; cat "$CARD_FILE"; return 0; }
  out=${out//$'\r'/}
  view=$(printf '%s\n' "$out" | awk '$1 == "view" { print $2; exit }')
  cells=$(printf '%s\n' "$out" | awk '$1 == "remote-cells" { $1 = ""; sub(/^ +/, ""); print; exit }')
  stored=$(awk '{ sub(/\r$/, "") } /^keys — view / { print $4; exit }' "$CARD_FILE")
  verdict=re-derived
  if [ -n "$stored" ] && [ -n "$view" ]; then
    verdict=$("$py" "$ck" verdict --stored "$stored" --class view --recomputed "$view" 2>/dev/null) || verdict=re-derived
    verdict=${verdict%$'\r'}
  fi
  if [ "$verdict" = fresh ]; then
    REPLAY_KEYS="keys view fresh · remote evidence"; cat "$CARD_FILE"; return 0
  fi
  REPLAY_KEYS="keys view moved · not re-derived: no scratch directory under $CARD_DIR · remote evidence"
  sd=$(mkdir -p "$CARD_DIR" && mktemp -d "$CARD_DIR/.replay.XXXXXX") || { cat "$CARD_FILE"; return 0; }
  CARD_TMP=$sd
  extract_card_parts "$CARD_FILE"
  render_card replay > "$sd/fresh"
  awk -v want=startup "$CARD_PARTS_AWK" "$sd/fresh" > "$sd/fstartup"
  # PATHS AND THE CELL LIST REACH awk THROUGH THE ENVIRONMENT: `-v` processes escapes.
  RK_STORED="$sd/startup" RK_CELLS="$cells" awk '
    BEGIN {
      n = split(ENVIRON["RK_CELLS"], c, " "); for (i = 1; i <= n; i++) want[c[i]] = 1
      while ((getline l < ENVIRON["RK_STORED"]) > 0) {
        if (++sn == 1) head = l
        if (l ~ /^keys — view /) { split(l, f, " "); srem = f[7]; sat = f[10] }
        if (cur != "" && l ~ /^  /) { blk[cur] = blk[cur] "\n" l; continue }
        cur = ""
        split(l, h, " ")
        if ((h[1] in want) && h[2] == "—") { cur = h[1]; blk[cur] = l }
      }
    }
    FNR == 1 { print head; next }
    skip && /^  / { next }
    { skip = 0; split($0, h, " ") }
    /^keys — view / { print "keys — view " h[4] " · remote " (srem == "" ? "k1:?" : srem) " · at " (sat == "" ? "?" : sat); next }
    (h[1] in want) && h[2] == "—" && (h[1] in blk) { print blk[h[1]]; skip = 1; next }
    { print }' "$sd/fstartup" > "$sd/new"
  cat "$sd/tail" >> "$sd/new"
  derive_pockets_block < "$sd/new" > "$sd/new.p" && mv "$sd/new.p" "$sd/new"   # TOOL-dPlacedRequest-9 S4
  bytes=$(wc -c < "$sd/new" | tr -d '[:space:]')
  if [ "$bytes" -gt "$CARD_CAP_BYTES" ]; then
    REPLAY_KEYS="keys view moved · not re-derived: over the cap · remote evidence"; cat "$CARD_FILE"
  elif cat "$sd/new" > "$CARD_FILE"; then
    REPLAY_KEYS="keys view re-derived · remote evidence"; cat "$CARD_FILE"
  else
    REPLAY_KEYS="keys view moved · not re-derived: $CARD_FILE could not be written · remote evidence"; cat "$CARD_FILE"
  fi
  rm -rf "$sd" 2>/dev/null
  return 0
}

# >>> envelope_sh — canonical copy: envelope.sh in the gov lib dir (byte-identical; gated)
# `render_envelope_sh <path> <level> <direction> [<body-file>]` prints the opener, the body file's
# bytes with a final newline added where it lacks one, and the closer: `render_envelope` of the Python
# twin byte for byte. No body file, or an empty one, renders the two lines alone. A level that is no
# unsigned integer returns 2 printing nothing; a body file that does not read returns 1.
render_envelope_sh() {
  case "${2:-}" in ''|*[!0-9]*) return 2 ;; esac
  printf '[%s · Level %s · %s]\n' "$1" "$((10#$2))" "$3"
  if [ -n "${4:-}" ] && [ -s "$4" ]; then
    cat -- "$4" || return 1
    [ -z "$(tail -c 1 -- "$4")" ] || printf '\n'
  fi
  printf '[/%s]\n' "$1"
}
# <<< envelope_sh


# The card file (PLAY-dOrderedCharter-8 S2, S3): the stored card rendered into `<CARD_TREE>/.claude/
# orientation-card.md` inside its level-1 envelope, the values of the playbook kit's `doc.orientation-card`
# registry row, through a temp beside it renamed into place, so a reader never sees half a card. The
# file is ignored before it is first written: a `check-ignore` miss appends the one exclude line to the
# clone's `info/exclude`, which covers every worktree, and a second miss writes nothing. Silent when
# written; any failure prints ONE `card-file — skipped:` line and returns 0, so it never changes a verb's
# exit: the stored card is the record and this file its render. WHAT THIS DOES NOT DO: load the file;
# nothing imports it until the charter's entry file does (PLAY-dOrderedCharter-43).
# ONE OWNER PER TREE (PLAY-dOrderedCharter-49 S54, PLAY-dOrderedCharter-54): the file's second line is
# `card-owner — <session id> · <transcript>`, the payload's transcript, else the one this session's own
# owner line already records, else `absent`. Another session's owner is LIVE while its transcript is a
# file `stat -c %Y` dates within CARD_OWNER_BOUND seconds of now, since the CLI appends to it every turn;
# a live owner's file is left as it is, printing one skipped: line. Every other owner is dead: an id-only
# or absent transcript, a missing file, an older one, or a time stat cannot read. A dead owner's file, or
# any owner's under a `clear` payload, is taken over, printing one `took over:` line after the rename.
# WHAT THIS DOES NOT CHECK: a sub-agent's transcript (an owner waiting on its agents past the bound reads
# dead), a path spelled with a \uXXXX escape or an escaped quote (reads missing, so dead), a host whose
# stat lacks -c (every owner dead), and a `resume` payload, which gets no `clear` treatment.
CARD_FILE_REL=.claude/orientation-card.md
CARD_FILE_DIRECTION="the build's card: where this session stands; level 0 outranks it"
CARD_OWNER_BOUND=1800
write_card_file() {
  local dest="$CARD_TREE/$CARD_FILE_REL" common tmp body owner="" osid="" otx="" mtime="" took="" tx=${CARD_TRANSCRIPT:-absent}
  local re_owner='^card-owner — ([A-Za-z0-9][A-Za-z0-9._-]*)( · (.+))?$'
  if [ -f "$dest" ]; then
    { IFS= read -r _; IFS= read -r owner; } < "$dest" 2>/dev/null
    owner=${owner%$'\r'}
    [[ $owner =~ $re_owner ]] && osid=${BASH_REMATCH[1]} && otx=${BASH_REMATCH[3]}
    if [ "$osid" = "$CARD_SID" ]; then
      [ -n "$CARD_TRANSCRIPT" ] || [ -z "$otx" ] || tx=$otx
    elif [ "$CARD_SOURCE" = clear ]; then
      took="session ${osid:-none} · source clear"
    else
      took="session ${osid:-none} · transcript absent"
      if [ -n "$otx" ] && [ "$otx" != absent ] && [ -f "$otx" ] && mtime=$(stat -c %Y -- "$otx" 2>/dev/null) && [[ $mtime =~ ^[0-9]+$ ]]; then
        if (( EPOCHSECONDS - mtime <= CARD_OWNER_BOUND )); then
          printf 'card-file — skipped: another live session %s owns this tree\n' "$osid"; return 0
        fi
        took="session $osid · transcript $((EPOCHSECONDS - mtime))s old"
      fi
    fi
  fi
  if ! git -C "$CARD_TREE" check-ignore -q "$CARD_FILE_REL" 2>/dev/null; then
    common=$(git -C "$CARD_TREE" rev-parse --path-format=absolute --git-common-dir 2>/dev/null) && common=${common%$'\r'} && [ -n "$common" ] \
      || { printf 'card-file — skipped: no git common dir resolves for %s\n' "$CARD_TREE"; return 0; }
    # A line already there is not appended again: a tracked file at the path misses the probe either way.
    grep -qxF "/$CARD_FILE_REL" "$common/info/exclude" 2>/dev/null \
      || { mkdir -p "$common/info" \
        && { [ ! -s "$common/info/exclude" ] || [ -z "$(tail -c 1 "$common/info/exclude")" ] || printf '\n'; } >> "$common/info/exclude" \
        && printf '/%s\n' "$CARD_FILE_REL" >> "$common/info/exclude"; } 2>/dev/null \
      || { printf 'card-file — skipped: the ignore line could not be appended to %s/info/exclude\n' "$common"; return 0; }
    git -C "$CARD_TREE" check-ignore -q "$CARD_FILE_REL" 2>/dev/null \
      || { printf 'card-file — skipped: %s is not ignored after the exclude line, so no file was written\n' "$CARD_FILE_REL"; return 0; }
  fi
  [ ! -d "$dest" ] || { printf 'card-file — skipped: %s is a directory\n' "$dest"; return 0; }
  mkdir -p "$CARD_TREE/.claude" 2>/dev/null || { printf 'card-file — skipped: cannot create %s/.claude\n' "$CARD_TREE"; return 0; }
  tmp=$(mktemp "$dest.XXXXXXXX" 2>/dev/null) || { printf 'card-file — skipped: no temp beside %s\n' "$dest"; return 0; }
  body=$(mktemp "$dest.XXXXXXXX" 2>/dev/null) || { rm -f "$tmp"; printf 'card-file — skipped: no temp beside %s\n' "$dest"; return 0; }
  if { printf 'card-owner — %s · %s\n' "$CARD_SID" "$tx" && { [ ! -f "$CARD_FILE" ] || cat -- "$CARD_FILE"; }; } > "$body" 2>/dev/null \
      && render_envelope_sh "$CARD_FILE_REL" 1 "$CARD_FILE_DIRECTION" "$body" > "$tmp" 2>/dev/null \
      && mv -f "$tmp" "$dest" 2>/dev/null; then
    rm -f "$body" 2>/dev/null
    [ -z "$took" ] || printf 'card-file — took over: %s\n' "$took"
    return 0
  fi
  rm -f "$tmp" "$body" 2>/dev/null
  printf 'card-file — skipped: cannot write %s\n' "$dest"
  return 0
}

# ---- the append and the citation check (KICK-aReplayedCard-2) -------------------------------------
# WHAT THESE DO NOT CHECK, stated here because a structural check reads as a semantic one to
# everybody who did not write it: relevance, scope correctness, tier, and the truth of a claim at
# the line it cites. They resolve EXISTENCE — a cited path is tracked, a cited range is inside the
# file, a cited id is DEFINED by a spec H1, a backlog row or a decision row — and nothing else. An
# untracked record is invisible to both probes and reports as a miss. Two spawns per run, never one
# per token: one `git ls-files -- …` over every path and basename cited, and one
# `corpus_ids.py --print-defined-ids`, the memory-tree kit's reader, which owns the id grammar and
# prints it on its first line as a POSIX ERE — this script spells no id grammar of its own.
CARD_ID_ERE_KEY='# id-ere: '
CARD_ID_ERE=""; CARD_TOKENS=0; CARD_TMP=""

# The one spelling of the `tree —` line. `render_card` writes it at session start and `add_card_body`
# re-renders it in the tree the append runs in, so the deny that compares the cell to the commit's
# toplevel sees the tree the kickoff ran in. Callers run `derive_head_state` first.
render_tree_cell() {
  local kind
  if [ -f "$ROOT/.git" ]; then kind=worktree; else kind=primary; fi
  printf 'tree — %s · %s · branch %s · BASE %s · %s\n' "$TOPLEVEL" "$kind" "$HEAD_BRANCH" "$HEAD_SHA" "$HEAD_DIRTY"
}

# The python that spawns the id reader. INLINED from the shared resolver named on the marker line
# below, byte-identical and gated by that resolver's own self-test, because this kit is
# copy-installed flat and has no `../lib/` to source. It RUNS each candidate: `${GOV_PYTHON:-python}` was a second, narrower
# resolver here, and on a host with only `python3` or with the Store stub it exited 127 or 9009,
# the append refused every body, and the commit deny's remedy re-ran the refusing append
# (the aReplayedCard closing review, F2).
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  # THE BAR'S OWN RESOLUTION, taken with no spawn (TOOL-aMeasuredDrag-11). The run-gates runner
  # exports GATE_RESOLVED_PY as four lines: the version, the launcher it resolved, and GOV_PYTHON and
  # PATH as it saw them. With no caller override the loop below is decided by GOV_PYTHON, PATH and the
  # floor, so a memo matching both byte for byte, at or above THIS floor, is what the loop would print.
  # Anything else, malformed or partial included, is ignored and the loop runs. Only an absolute
  # launcher is admitted (TOOL-aMeasuredDrag-12): a relative one names another file once a leg
  # changes directory, and a bare name does too under a PATH holding `.`.
  _rp_re=$'^([0-9]+)\\.([0-9]+)\n(/[^\n]*|[A-Za-z]:/[^\n]*|[A-Za-z]:\\\\[^\n]*)\n([^\n]*)\n(.*)$'
  if [ -z "${1:-}" ] && [[ ${GATE_RESOLVED_PY:-} =~ $_rp_re ]] \
    && [ "${BASH_REMATCH[4]}" = "${GOV_PYTHON:-}" ] && [ "${BASH_REMATCH[5]}" = "$PATH" ] \
    && [ $(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} )) -ge "$_rp_fv" ]; then
    printf '%s\n' "${BASH_REMATCH[3]}"
    return 0
  fi
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file; the launcher's own name
        # otherwise. The `[ -f ]` HOLDS on a Windows App Execution Alias, so a Store Python whose
        # own sys.executable is an alias is echoed as printed: a gap the run-gates kit's
        # check_app_alias closes for the legs it measures, and this block does not.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
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
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
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
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
    # LAST, verbatim: the first line names the refusal and this one the candidates, and the lines
    # between them carry the outcomes, the overrides and the install (TOOL-dSafePassage-26 S20).
    echo "resolve_python: tried:$_rp_tried"
  } >&2
  return 1
}
# <<< resolve_python
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
refuse_wrong_shell || exit 2

# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
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
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
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
  "$1" -c "${_rkd%$'\n'}"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}

# A sibling kit's file, `resolve_kit_file <home> <anchor>`, through the sibling resolver
# (TOOL-aRepatriatedFork-2 S3): the receipt, which is the only record of a flat or renamed install,
# then the two probes beside this kit. Anchored at this script's dir FIRST, then at the repo root:
# the per-machine junction copy resolves into gov's checkout, where neither rung sees the graded repo
# (closing review round 1 L3). An answer counts only if the file is in THIS repo. Gov homes THIS kit
# under skills/, which no probe walks from, and gov keeps no receipt, so the last rung is the ONE
# <anchor> this repo TRACKS. It is derived from the index, where the rung it replaced was two spelled
# prefixes, gov's and the root (TOOL-aRepatriatedFork-24 S8). Two tracked anchors are ambiguous, and
# so is none; either way this returns empty, and the caller says so. ONE body for every sibling this
# kit reads — the memory-tree id reader and the unattended driver (TOOL-aGraftedHelix-2 S3) — so no
# sibling kit's path is spelled here.
resolve_kit_file() {
  local d py here
  py=$(resolve_python 2>/dev/null) || py=""
  if [ -n "$py" ]; then
    for here in "$MC_DIR" "$ROOT"; do
      d=$(resolve_kit_dir "$py" "$1" "$2" "$here" 2>/dev/null) || continue
      [ -f "$ROOT/$d/$2" ] && { printf '%s\n' "$ROOT/$d/$2"; return 0; }
    done
  fi
  d=$(git -C "$ROOT" ls-files -- "$2" "*/$2" 2>/dev/null)
  case "$d" in *"
"*|"") ;; *) [ -f "$ROOT/$d" ] && printf '%s\n' "$ROOT/$d" ;; esac
  return 0
}

# The memory-tree kit's id reader.
resolve_id_reader() {
  resolve_kit_file memory-tree corpus_ids.py
}

# One token per line, `<line>\t<kind>\t<token>\t<range>`, kinds `path` (a slash and an extension —
# the first half of the rule the spec-token lint applies to a spec's acceptance bullets), `cand`
# (its second half: a slashless dotted token — `AGENTS.md`, `README.md` — that COUNTS as a path
# only on an exact tracked hit, so `e.g` is never an UNVERIFIED and a root-level file cited by name
# is never "nothing to check"; the aReplayedCard closing review, F7), `base` (a basename with an
# extension and a `:<line>` tail, the house style `run-gates.sh:407`) and `id` (the reader's
# grammar). Not a token: a glob, a `{{placeholder}}`, a `$var`, a `<slot>`, a `GATE_` knob, a URL,
# a `..` segment (a claim about some other tree, and `git ls-files` fatals on it — F8), and an
# absolute path — the `tree —` cell carries one, and a checkout location is not a claim about the
# tree. Backticks, brackets and quotes separate; trailing sentence punctuation is dropped.
# A line that is itself an annotation is BLANKED, not deleted, so line numbers still address the
# rows they belong to — which is what lets `--check` re-run over a card it annotated.
extract_card_tokens() {
  local filtered="$CARD_TMP/filtered"
  awk '/^UNVERIFIED — /{print ""; next} {print}' "$1" | tr -d '\r' > "$filtered"
  awk -v q="'" '
    { ln=$0; gsub(/`/, " ", ln); gsub(/[()]/, " ", ln); gsub(/\[/, " ", ln); gsub(/\]/, " ", ln)
      gsub(/"/, " ", ln); gsub(q, " ", ln)
      n=split(ln, w, /[ \t]+/)
      for (i=1; i<=n; i++) {
        t=w[i]; sub(/[,.;:]+$/, "", t)
        if (t=="" || index(t,"://") || t ~ /[*?]/ || t ~ /\/$/) continue
        c=substr(t,1,1)
        if (c=="/" || c==":" || c=="$" || c=="~" || c=="<" || substr(t,1,2)=="{{" || substr(t,1,5)=="GATE_") continue
        if (t ~ /^[A-Za-z]:/ || t ~ /(^|\/)\.\.(\/|$)/) continue
        r=""
        if (match(t, /:[0-9]+(-[0-9]+)?$/)) { r=substr(t, RSTART+1); t=substr(t, 1, RSTART-1) }
        if (t ~ /[\/.]$/) continue
        k=split(t, seg, "/"); base=seg[k]
        if (index(base, ".")==0) continue
        if (k>1) print NR "\tpath\t" t "\t" r
        else if (r!="") print NR "\tbase\t" t "\t" r
        else print NR "\tcand\t" t "\t"
      } }' "$filtered"
  [ -n "$CARD_ID_ERE" ] && grep -noE "\\b($CARD_ID_ERE)\\b" "$filtered" | awk -F: '{print $1 "\tid\t" $2 "\t"}'
  return 0
}

# The check over one file: the two spawns, then a verdict per token. Misses land in
# `$CARD_TMP/misses` as `<line>\t<annotation>`; `CARD_TOKENS` says how many tokens were judged, so
# a caller can tell "clean" from "nothing to check". Every refusal here is a reader that could not
# answer — a set that could not be read is UNKNOWN, never empty.
check_card_citations() {
  local f="$1" reader py st ln kind tok rng hit n note count hi
  local -a paths=() globs=()
  CARD_ID_ERE=""; : > "$CARD_TMP/ids"
  reader=$(resolve_id_reader)
  if [ -z "$reader" ]; then
    echo "NOTE: id citations unchecked — no memory-tree corpus_ids.py in this tree, by the receipt or beside this kit, so only paths are judged"
  else
    py=$(resolve_python) || { echo "MANIFEST env ERROR — no usable python launcher for the id reader $reader, so the defined-id set is unknown rather than empty; resolve_python's refusal above names every candidate it ran, and GOV_PYTHON=<launcher> is the override"; exit 2; }
    "$py" "$reader" --print-defined-ids > "$CARD_TMP/idout" 2>&1; st=$?
    # Exit 3 is the reader's NAMED degradation — memory-tree installed without its id_grammar.py, so
    # no grammar and no set — and it lands on the same branch as "no reader": paths are still
    # judged and the append proceeds. Every other non-zero status is a reader that could not answer.
    if [ "$st" = 3 ]; then
      echo "NOTE: id citations unchecked — $(tr -d '\r' < "$CARD_TMP/idout" | head -1 | head -c 300); only paths are judged"
      CARD_ID_ERE=""; : > "$CARD_TMP/ids"
    elif [ "$st" != 0 ]; then
      echo "MANIFEST env ERROR — the id reader exited $st, so the defined-id set is unknown rather than empty: $py $reader --print-defined-ids — $(tr -d '\r' < "$CARD_TMP/idout" | head -c 300)"; exit 2
    else
      CARD_ID_ERE=$(sed -n "1s/^$CARD_ID_ERE_KEY//p" "$CARD_TMP/idout" | tr -d '\r')
      [ -n "$CARD_ID_ERE" ] || { echo "MANIFEST env ERROR — the id reader's first line is not the id grammar ('${CARD_ID_ERE_KEY}…'), so no id token can be recognised: $(head -1 "$CARD_TMP/idout" | tr -d '\r')"; exit 2; }
      sed '1d' "$CARD_TMP/idout" | tr -d '\r' > "$CARD_TMP/ids"
    fi
  fi
  extract_card_tokens "$f" | sort -u | sort -t "$(printf '\t')" -k1,1n -s > "$CARD_TMP/tokens"
  CARD_TOKENS=$(grep -c . "$CARD_TMP/tokens"); CARD_TOKENS=${CARD_TOKENS:-0}
  while IFS=$'\t' read -r ln kind tok rng; do
    case "$kind" in
      path|cand) paths+=("$tok") ;;
      base) globs+=("$tok" "*/$tok") ;;
    esac
  done < "$CARD_TMP/tokens"
  : > "$CARD_TMP/tracked"
  if [ ${#paths[@]} -gt 0 ] || [ ${#globs[@]} -gt 0 ]; then
    git ls-files -- ${paths[@]+"${paths[@]}"} ${globs[@]+"${globs[@]}"} > "$CARD_TMP/tracked" 2> "$CARD_TMP/git.err" \
      || { echo "MANIFEST env ERROR — git ls-files failed over the cited paths, so the tracked set is unknown: $(tr -d '\r' < "$CARD_TMP/git.err" | head -c 300)"; exit 2; }
  fi
  : > "$CARD_TMP/misses"
  while IFS=$'\t' read -r ln kind tok rng; do
    hit=""; note=""
    case "$kind" in
      id)   grep -qxF -- "$tok" "$CARD_TMP/ids" && continue ;;
      path) grep -qxF -- "$tok" "$CARD_TMP/tracked" && hit="$tok" ;;
      cand) grep -qxF -- "$tok" "$CARD_TMP/tracked" && continue
            CARD_TOKENS=$((CARD_TOKENS - 1)); continue ;;   # a candidate that is not tracked was never a token
      base) n=$(awk -v b="$tok" '{k=split($0,s,"/"); if (s[k]==b) c++} END{print c+0}' "$CARD_TMP/tracked")
            if [ "$n" = 1 ]; then hit=$(awk -v b="$tok" '{k=split($0,s,"/"); if (s[k]==b) print}' "$CARD_TMP/tracked")
            elif [ "$n" -gt 1 ]; then note=" (ambiguous: $n matches)"; fi ;;
    esac
    if [ -n "$hit" ] && [ -n "$rng" ]; then
      hi=${rng##*-}; count=$(awk 'END{print NR}' "$ROOT/$hit" 2>/dev/null); count=${count:-0}
      if [ "$hi" -le "$count" ]; then continue; fi
      note=" (past end: $count lines)"
    elif [ -n "$hit" ]; then
      continue
    fi
    printf '%s\tUNVERIFIED — %s%s\n' "$ln" "$tok${rng:+:$rng}" "$note" >> "$CARD_TMP/misses"
  done < "$CARD_TMP/tokens"
  return 0
}

# A stored card is STARTUP + TAIL: the header through the `recent —` line and the run of
# `<sha> <subject>` lines beneath it, then everything after, which holds the card's one READY line
# last. Written to two scratch files, CR-stripped.
extract_card_parts() {
  awk -v want=startup "$CARD_PARTS_AWK" "$1" > "$CARD_TMP/startup"
  awk -v want=tail "$CARD_PARTS_AWK" "$1" > "$CARD_TMP/tail"
}
CARD_PARTS_AWK='{ ln=$0; sub(/\r$/, "", ln)
  if (!intail) { if (ln ~ /^recent —/) inlog=1; else if (inlog && ln !~ /^[0-9a-f]{7,40} /) intail=1 }
  if ((want=="tail") == (intail==1)) print ln }'

# THE READY ANCHOR, and the one place it is spelled. The optional leading `- ` is not cosmetic: the
# charter's [r1] rule requires an emitted micro-format to be a markdown list item — `- ` at column 0 —
# so a kickoff body that OBEYS the charter was read here as carrying NO READY line, and the append
# then reported success while leaving the sentinel in place and skipping the `tree —` re-render.
# Both forms are accepted, and that is a WIDENING rather than a swap: the sentinel this script
# renders is bare, as is every card already on disk, and dropping the bare form would strand them.
# The reader moves; [r1] does not (TOOL-cMendedVintage-16).
CARD_READY_RE='^\(- \)\{0,1\}READY — '

# The route rules (KICK-aRoutedQuill-1 §4): a body's `## route` section names its build, each unit
# with its spec, and the brief, and every one of them resolves or nothing lands — a route is read by
# the write gate and handed to subagents, so an annotated miss would hand both a line naming nothing.
# The section runs from `## route` to the line before the next `## ` heading, READY line or the end.
# R3 to R5 read the two sets `check_card_citations` already holds, so no rule spawns git or the id
# reader; R4 reads one spec file per unit line. Sets CARD_ROUTE=1 when the body carries a route.
# WHAT THIS DOES NOT CHECK: the brief's content, a routed unit's status (the write gate's question,
# asked at write time), or that the owner said go — existence and pairing only.
# R7 (TOOL-dPlacedRequest-2 S9), `check_card_terminal`: a route whose build's card, as this node's cache
# ref `refs/gov/remote/builds/<slug>/card` holds it, reads a step its follow marked terminal — the
# message's third line `step: <state> · terminal` — is refused, since that build has ended. That cache
# ref is the one a publish sets and a lookup refreshes (TOOL-dPlacedRequest-34 S7), so a terminal follow
# here is refused with no lookup, and one on another node once a publish or a lookup here fetched it.
check_card_terminal() { # body file -> R7's verdict line, or nothing
  local at b step
  at=$(LC_ALL=C awk '/^[[:space:]]*## route[[:space:]]*$/ { inr = 1; next } inr && (/^## / || /^(- )?READY — /) { inr = 0 }
    inr && /^- build: [A-Za-z0-9]+$/ { print NR "\t" substr($0, 10); exit }' "$1")
  [ -n "$at" ] || return 0
  b=${at#*$'\t'}
  step=$(git log -1 --format=%B "refs/gov/remote/builds/$b/card" -- 2>/dev/null | sed -n '3s/^step: //p' | tr -d '\r')
  case "$step" in
    *" · terminal") printf 'R7\t%s\t- build: %s\tthe build %s has ended: its card ref refs/gov/remote/builds/%s/card reads step %s, which its follow marked terminal, so a route to it does not land' \
      "${at%%$'\t'*}" "$b" "$b" "$b" "${step% · terminal}" ;;
  esac
}
CARD_ROUTE=0; CARD_APPEND_READY=0
check_card_route() {
  local body="$1" nready="$2" n memroot verdict rule ln line why where="" self=${0##*/}
  CARD_ROUTE=0
  n=$(grep -c '^[[:space:]]*## route[[:space:]]*$' "$body"); n=${n:-0}
  [ "$n" -gt 0 ] || return 0
  CARD_ROUTE=1
  memroot=$(read_memory_root) || memroot=""
  [ -n "$memroot" ] || { echo "MANIFEST env ERROR — route R0: this tree's .memory-tree.conf declares no MEMORY_ROOT (or there is no conf), so the route's build folder cannot be checked; nothing was appended"; exit 2; }
  [ -n "$CARD_ID_ERE" ] || { echo "MANIFEST env ERROR — route R0: no defined-id set, because the id reader is absent or could not read the grammar, so the route's unit ids cannot be checked; nothing was appended"; exit 2; }
  [ "$n" = 1 ] || { echo "MANIFEST route R1 REFUSED — the body carries $n '## route' sections, and a card holds one; the shape is what $self --brief-skeleton prints, and nothing was appended"; exit 1; }
  verdict=$(LC_ALL=C awk -v mr="$memroot" -v root="$ROOT" -v idf="$CARD_TMP/ids" -v trf="$CARD_TMP/tracked" '
    BEGIN { while ((getline l < idf) > 0) I[l] = 1; while ((getline l < trf) > 0) T[l] = 1 }
    function out(r, n, s, w) { gsub(/\t/, " ", s); if (!done) printf "%s\t%s\t%s\t%s\n", r, n, s, w; done = 1 }
    /^[[:space:]]*## route[[:space:]]*$/ { inr = 1; at = NR; next }
    inr && (/^## / || /^(- )?READY — /) { inr = 0 }
    !inr || done || /^[ \t]*$/ { next }
    index($0, "`") { out("R2", NR, $0, "a route line carries no backticks"); next }
    /^- build: [A-Za-z0-9]+$/ { nb++; build = substr($0, 10); next }
    /^- brief: [^ \t]+$/ { nf++; brief = substr($0, 10); bn = NR; bs = $0; next }
    /^- unit: [^ \t]+ · spec [^ \t]+$/ {
      r = substr($0, 9); k = index(r, " · spec ")
      nu++; uid[nu] = substr(r, 1, k - 1); usp[nu] = substr(r, k + length(" · spec ")); un[nu] = NR; us[nu] = $0; next }
    { out("R2", NR, $0, "a line outside the route grammar: - build: <build>, - unit: <id> · spec <path>, - brief: <path>") }
    END {
      if (done) exit
      if (nb != 1) out("R2", at, "## route", "the section carries " nb + 0 " - build: lines, and takes exactly one")
      else if (nf != 1) out("R2", at, "## route", "the section carries " nf + 0 " - brief: lines, and takes exactly one")
      else if (nu == 0) out("R2", at, "## route", "the section carries no - unit: line")
      dir = mr "/builds/" build "/"
      for (i = 1; i <= nu && !done; i++) {
        if (!(uid[i] in I)) { out("R3", un[i], us[i], "no spec H1, backlog row or decision row defines " uid[i]); break }
        if (!(usp[i] in T)) { out("R4", un[i], us[i], usp[i] " is not a tracked file"); break }
        if (index(usp[i], dir "spec/") != 1) { out("R4", un[i], us[i], usp[i] " is outside " dir "spec/"); break }
        fence = 0; hit = 0; f = root "/" usp[i]
        while (!hit && (getline l < f) > 0) {
          sub(/\r$/, "", l)
          if (l ~ /^ ? ? ?(```|~~~)/) { fence = !fence; continue }
          if (fence || l !~ /^#[ \t]/) continue
          split(l, w, /[ \t]+/); t = w[2]; gsub(/[`*]/, "", t); sub(/[:.,;]+$/, "", t)
          if (t == uid[i]) hit = 1
        }
        close(f)
        if (!hit) out("R4", un[i], us[i], usp[i] " carries no unfenced H1 whose first token is " uid[i])
      }
      if (done) exit
      if (!(brief in T)) out("R5", bn, bs, brief " is not a tracked file")
      else if (index(brief, dir "prompts/") != 1 && brief != dir "README.md") out("R5", bn, bs, brief " is neither under " dir "prompts/ nor " dir "README.md")
    }' "$body")
  if [ -z "$verdict" ] && [ "$nready" = 0 ] && grep "$CARD_READY_RE" "$CARD_TMP/tail" | grep -q 'READY — none yet$'; then
    verdict=$(printf 'R6\t-\t-\tthe card still reads READY — none yet: no kickoff has appended to it, and a route lands only on an oriented card')
  fi
  [ -n "$verdict" ] || verdict=$(check_card_terminal "$body")
  [ -n "$verdict" ] || return 0
  IFS=$'\t' read -r rule ln line why <<<"$verdict"
  [ "$ln" = - ] || where="line $ln: $line — "
  echo "MANIFEST route $rule REFUSED — $where$why; the shape is what $self --brief-skeleton prints, and nothing was appended"
  exit 1
}

# The task fields (KICK-aOrientedCast-1): a real READY body's `## task` holds every field TASK_SKELETON
# names, each once, none empty and none a placeholder. ONE awk, the skeleton on its first input and the
# body on its second, so the labels graded are the skeleton's by construction. This is the one grammar
# for a card's task fields, and TOOL-aOrientedCast-2's renderer reads `task:` keys by it:
#   section — the lines after the LAST `## task` heading, to the next `## ` heading, READY line or end;
#   line    — leading whitespace, then any run of `>` each with an optional space, then one `- ` or
#             `* ` marker, stripped; a line then opening `<!--` or `UNVERIFIED — ` is not field text;
#   field   — a line opening `**`: its label runs to the first `:**` when that comes no later than the
#             first closing `**`, else to that `**`, trimmed; the rest of the line and each following
#             line, up to the next field line, is its raw text;
#   value   — trimmed, one leading balanced `(…)` group stripped, then one leading `:`, trimmed again;
#   verdict — whitespace runs collapsed; EMPTY, or a PLACEHOLDER: one of … ... tbd todo n/a none - ?
#             in any case, only `.` and `…`, or one `<slot>` holding no further angle bracket.
# A field line whose label is not one of the eight ends the field above it and is otherwise ignored.
# It spawns no git and no id reader. WHAT THIS DOES NOT CHECK: what a value says beyond present, single,
# non-empty and not a placeholder; a stored card, since `--card --check` keeps its rules and a card
# written before this landed still checks clean; or a body with no real READY line.
check_card_task() {
  local verdict
  verdict=$(printf '%s\n' "$TASK_SKELETON" | LC_ALL=C awk -v q="'" '
    function strip(s) { sub(/^[[:space:]]+/, "", s); sub(/^(> ?)+/, "", s); sub(/^[-*] /, "", s); return s }
    function trim(s) { sub(/^[[:space:]]+/, "", s); sub(/[[:space:]]+$/, "", s); return s }
    function field(s,   k, b) {
      if (substr(s, 1, 2) != "**") return 0
      s = substr(s, 3); k = index(s, ":**"); b = index(s, "**")
      if (!b) return 0
      if (k && k < b) { LBL = trim(substr(s, 1, k - 1)); REST = substr(s, k + 3) }
      else { LBL = trim(substr(s, 1, b - 1)); REST = substr(s, b + 2) }
      return 1
    }
    function value(r,   d, i, ch) {
      r = trim(r)
      if (substr(r, 1, 1) == "(")
        for (i = 1; i <= length(r); i++) {
          ch = substr(r, i, 1)
          if (ch == "(") d++
          else if (ch == ")" && --d == 0) { r = substr(r, i + 1); break }
        }
      r = trim(r)
      if (substr(r, 1, 1) == ":") r = substr(r, 2)
      r = trim(r); gsub(/[[:space:]]+/, " ", r)
      return r
    }
    function placeholder(v,   t) {
      t = tolower(v)
      if (t == "…" || t == "..." || t == "tbd" || t == "todo" || t == "n/a" || t == "none" || t == "-" || t == "?") return 1
      t = v; gsub(/\.|…/, "", t)
      return t == "" || v ~ /^<[^<>]*>$/
    }
    NR == FNR { s = strip($0); if (substr(s, 1, 4) != "<!--" && field(s)) { nl++; L[nl] = LBL; W[LBL] = nl }; next }
    { sub(/\r$/, "") }
    /^## task[[:space:]]*$/ { insec = 1; cur = 0; split("", cnt); split("", raw); next }
    insec && (/^## / || /^(- )?READY — /) { insec = 0 }
    !insec { next }
    { s = strip($0) }
    substr(s, 1, 4) == "<!--" || index(s, "UNVERIFIED — ") == 1 { next }
    field(s) { cur = (LBL in W) ? W[LBL] : 0; if (cur && ++cnt[cur] == 1) raw[cur] = REST; next }
    cur && cnt[cur] == 1 { raw[cur] = raw[cur] "\n" s }
    END {
      for (i = 1; i <= nl; i++) {
        if (!cnt[i]) c = "has no " L[i] " field"
        else if (cnt[i] > 1) c = "carries " L[i] " twice"
        else if ((v = value(raw[i])) == "") c = "leaves " L[i] " empty"
        else if (placeholder(v)) c = "leaves " L[i] " a placeholder (" q v q ")"
        else continue
        out = out (out == "" ? "" : "; ") c
      }
      if (out != "") print out
    }' - "$1")
  [ -z "$verdict" ] || { echo "MANIFEST task REFUSED — the '## task' section $verdict; every field --task-skeleton prints is filled before a kickoff lands, and nothing was appended"; exit 1; }
}

# `--card --append`: the body on stdin, checked, annotated, and stored — or refused with the file
# byte-identical. Order: the body's READY-line count, the citation check (its refusals come from a
# reader that could not answer), DEAD PROBE on zero tokens, the `## task` refusal, the task fields,
# the stale-BASE refusal, the card's own shape, the route rules, the cap. A real-READY body replaces the whole TAIL and re-renders the `tree —` cell; a body
# without one goes in before the TAIL's READY line, so the card always ends with its one READY line.
add_card_body() {
  local body="$CARD_TMP/body" nready ready sha tree bytes l
  [ -f "$CARD_FILE" ] || { echo "MANIFEST env ERROR — no card for session $CARD_SID at $CARD_FILE; write one with --card --write --session $CARD_SID before appending to it"; exit 2; }
  tr -d '\r' > "$body"
  grep -v "${CARD_READY_RE}none yet\$" "$body" > "$body.x"; mv "$body.x" "$body"
  nready=$(grep -c "$CARD_READY_RE" "$body"); nready=${nready:-0}; CARD_APPEND_READY=$nready
  [ "$nready" -le 1 ] || { echo "MANIFEST env ERROR — the body carries $nready READY lines; one card holds one kickoff, so exactly one is accepted and nothing was appended"; exit 2; }
  check_card_citations "$body"
  [ "$CARD_TOKENS" -gt 0 ] || { echo "MANIFEST env ERROR — DEAD PROBE: nothing to check — the body carries no path-shaped and no id-shaped token, so nothing was appended"; exit 1; }
  # The write-boundary half of `--card --check`'s `## task` refusal (TOOL-aReplayedCard-11): a kickoff
  # that left no scope does not land. After DEAD PROBE, so a token-free body keeps that verdict.
  if [ "$nready" = 1 ] && ! grep -q '^## task' "$body"; then
    echo "MANIFEST env ERROR — the body carries a real READY line and no '## task' section: a kickoff that left no scope does not land on the card, and nothing was appended"; exit 1
  fi
  # The fields under it, before the stale-BASE refusal; a body with no real READY line carries no task.
  if [ "$nready" = 1 ]; then check_card_task "$body"; fi
  derive_head_state
  if [ "$nready" = 1 ]; then
    ready=$(grep -m1 "$CARD_READY_RE" "$body")
    sha=$(printf '%s\n' "$ready" | sed -n 's/.*[ ·]base \([0-9a-f]\{7,40\}\)\([ ·].*\)\{0,1\}$/\1/p')
    case "$HEAD_SHA" in "$sha"*) [ -n "$sha" ] ;; *) false ;; esac \
      || { echo "MANIFEST env ERROR — the READY line's base ${sha:-<none>} is not HEAD $HEAD_SHA at append time; a kickoff pinned to a stale BASE does not land on the card — kick off again, and nothing was appended"; exit 2; }
  fi
  extract_card_parts "$CARD_FILE"
  [ "$(grep -c "$CARD_READY_RE" "$CARD_TMP/tail")" = 1 ] \
    || { echo "MANIFEST env ERROR — $CARD_FILE holds $(grep -c "$CARD_READY_RE" "$CARD_TMP/tail") READY lines after its startup lines, not one; rewrite it with --card --write --session $CARD_SID, and nothing was appended"; exit 2; }
  check_card_route "$body" "$nready"
  awk -F '\t' -v m="$CARD_TMP/misses" 'BEGIN { while ((getline l < m) > 0) { split(l, p, "\t"); a[p[1]] = a[p[1]] p[2] "\n" } }
    { print; if (FNR in a) printf "%s", a[FNR] }' "$body" > "$CARD_TMP/annotated"
  if [ "$nready" = 1 ]; then
    tree=$(render_tree_cell)
    { while IFS= read -r l; do case "$l" in "tree — "*) printf '%s\n' "$tree" ;; *) printf '%s\n' "$l" ;; esac; done < "$CARD_TMP/startup"
      cat "$CARD_TMP/annotated"; } > "$CARD_TMP/new"
  else
    # A body carrying a route takes the stored route section's place, so a card holds at most one.
    grep -v "$CARD_READY_RE" "$CARD_TMP/tail" > "$CARD_TMP/kept"
    if [ "$CARD_ROUTE" = 1 ]; then
      awk '/^[[:space:]]*## route[[:space:]]*$/ { skip = 1; next } skip && /^## / { skip = 0 } !skip' "$CARD_TMP/kept" > "$CARD_TMP/kept.x" && mv "$CARD_TMP/kept.x" "$CARD_TMP/kept"
    fi
    { cat "$CARD_TMP/startup"; cat "$CARD_TMP/kept"; cat "$CARD_TMP/annotated"; grep "$CARD_READY_RE" "$CARD_TMP/tail"; } > "$CARD_TMP/new"
  fi
  # The `## pockets` section refitted to the room this body leaves (TOOL-dPlacedRequest-9 S4).
  derive_pockets_block < "$CARD_TMP/new" > "$CARD_TMP/new.p" && mv "$CARD_TMP/new.p" "$CARD_TMP/new"
  bytes=$(wc -c < "$CARD_TMP/new" | tr -d '[:space:]')
  if [ "$bytes" -gt "$CARD_CAP_BYTES" ]; then
    echo "MANIFEST env ERROR — the card would be $bytes bytes, $((bytes - CARD_CAP_BYTES)) over the $CARD_CAP_BYTES-byte cap (CARD_CAP_BYTES), so nothing was appended"; exit 2
  fi
  cat "$CARD_TMP/new" > "$CARD_FILE" || { echo "MANIFEST env ERROR — cannot write $CARD_FILE"; exit 2; }
  cut -f2 "$CARD_TMP/misses"
  printf 'appended — %s · %s tokens · %s unverified · %s/%s bytes\n' "$CARD_FILE" "$CARD_TOKENS" "$(grep -c . "$CARD_TMP/misses")" "$bytes" "$CARD_CAP_BYTES"
}

# `--card --check`: the same check over the whole stored card, its own annotations skipped, one line
# per miss and exit 1 on any; exit 1 too for a real READY line with no `## task` beneath it (a
# kickoff ran and left no scope on disk) and for a card with nothing to check. Writes nothing.
# The `recent —` run — git's own `<sha> <subject>` lines, which the session never wrote and cannot
# fix — is BLANKED before the check, the way annotation lines are (blanked, not deleted, so line
# numbers still address the rows they belong to): a commit subject naming a since-removed path is
# not a citation (the aReplayedCard closing review, F9).
check_card() {
  local real lacks
  [ -f "$CARD_FILE" ] || { echo "MANIFEST env ERROR — no card for session $CARD_SID at $CARD_FILE; write one with --card --write --session $CARD_SID"; exit 2; }
  real=$(grep "$CARD_READY_RE" "$CARD_FILE" | grep -vc "${CARD_READY_RE}none yet"); real=${real:-0}
  if [ "$real" -gt 0 ] && ! grep -q '^## task' "$CARD_FILE"; then
    echo "MANIFEST env ERROR — $CARD_FILE carries a real READY line and no '## task' section: a kickoff ran and left no scope on disk"; exit 1
  fi
  awk '{ ln=$0; sub(/\r$/, "", ln) }
       ln ~ /^recent —/ { inlog=1; print ""; next }
       inlog && ln ~ /^[0-9a-f]{7,40} / { print ""; next }
       { inlog=0; print ln }' "$CARD_FILE" > "$CARD_TMP/checked"
  check_card_citations "$CARD_TMP/checked"
  [ "$CARD_TOKENS" -gt 0 ] || { echo "MANIFEST env ERROR — DEAD PROBE: nothing to check — $CARD_FILE carries no path-shaped and no id-shaped token"; exit 1; }
  lacks=$(check_card_pointers "$CARD_FILE")
  if [ -s "$CARD_TMP/misses" ] || [ -n "$lacks" ]; then
    awk -F '\t' '{print $2 " · line " $1}' "$CARD_TMP/misses"
    for real in $lacks; do printf "POINTERS — the '## pointers' section has no '%s —' line, which POINTER_LINES lists; --card --pointers --build <slug> --session %s renders it\n" "$real" "$CARD_SID"; done
    exit 1
  fi
  exit 0
}

# The `## pointers` section's required lines (KICK-dKeptSession-13 S2): each POINTER_LINES word the
# section of the card at `$1` carries no `<word> —` line for, one per line. A card with no section
# prints nothing, so a card written before the section landed checks as it did.
check_card_pointers() { # card file -> each missing word on stdout; 0 always
  LC_ALL=C awk -v want="$POINTER_LINES" '{ sub(/\r$/, "") }
    /^## pointers[[:space:]]*$/ { inp = 1; seen = 1; next }
    inp && (/^## / || /^(- )?READY — /) { inp = 0 }
    inp { split($0, w, " "); if (w[2] == "—") has[w[1]] = 1 }
    END { if (!seen) exit; n = split(want, k, " "); for (i = 1; i <= n; i++) if (!(k[i] in has)) print k[i] }' "$1"
}

# ---- the build card (TOOL-dPlacedRequest-2) ------------------------------------------------------
# A build's card, kept per build so a new session, another node or a resumed one finds it. THREE
# STORES, `card.store` selecting any non-empty subset and every write going to each selected store and
# no other: `remote-ref`, the ref refs/gov/builds/<slug>/card on the remote, the truth, one commit per
# write, written by the unattended driver's `--card-ref write` (TOOL-dPlacedRequest-33), which builds
# it on the tip it reads and writes it by compare-and-swap, so it joins the change feed. The driver is
# resolved by `resolve_kit_file` and run through `run_driver_bounded`, as `derive_claims_line` runs
# `--claims`: stdin closed, GOV_RUNLOG=0, its output to a scratch file, the lookup under
# CARD_FETCH_BOUND and the write under CARD_PUBLISH_BOUND, a killed write `remote-ref unknown`. DARK BEHIND
# RUN_CLAIMS, the switch the driver alone reads: `card-ref — off` prints `card — remote-ref not
# written: RUN_CLAIMS is off`, and so does every other unwritten answer, with its reason; on a written
# one the cache ref the driver's write set gives the full sha, and a cache ref that does not read back
# as the driver's sha leaves the cache's `# card-ref` at `local`. No local card ref exists: the one
# name this engine reads is that cache ref (TOOL-dPlacedRequest-34 S8).
# The message is `gov-card <slug>`, a blank line, `step:
# <state>` (` · terminal` after it at a terminal follow, which R7 reads), `session: <sid>`, a blank line
# and the card, every line after the fifth. `local-clone`, the cache <common dir>/orientation/<slug>.md,
# its first line `# card-ref <the ref's commit, or local>`, trusted only while that equals the ref. And
# `build-folder`, a `card` record of the record factory committed alone in the session's own tree, its
# anchor the loop kit's `resolve_build_anchor`, written as `card.snapshot` says. The ref is read by the
# driver's `--card-ref lookup` (TOOL-dPlacedRequest-34 S10 to S12), never by a fetch here: the driver
# fetches from the remote it resolves into the cache ref, writing no `FETCH_HEAD`, and sights the feed,
# so this engine carries no feed block and no writer. A lost compare-and-swap re-reads the tip, re-renders once on it and writes
# again. Every store's failure is its own `card —` line and never changes the caller's exit.
# THE POLICY KEYS this engine reads, `card.follows`, `card.store`, `card.snapshot`, `card.pointers`,
# `resume.context`, `resume.partial`, `context.on-full` and `context.threshold`, are read by
# `read_card_policy`, one literal `get` line per key, the shape the policy kit's reader coverage counts
# (as `read_spec_audit_switch` in the unattended driver does).
# WHAT THIS DOES NOT CHECK: that the card's text is true, which its cells derive; who may publish a build's
# card, which the lease and the claim decide.
# THE LOOKUP BOUND (TOOL-dPlacedRequest-49 S2): a reader's bound sits inside the claims cell's, so
# CARD_FETCH_BOUND defaults to CARD_CLAIMS_BOUND's, the kill bound of a remote read
# (TOOL-aGraftedHelix-2): 15 s, PINNED. A lookup the bound kills still reads the next store.
CARD_FETCH_BOUND=${CARD_FETCH_BOUND:-15}   # seconds each lookup of the card ref may take; the env override is the fixture's
# THE PUBLISH BOUND (TOOL-dPlacedRequest-43 S16): the driver's `--card-ref write` alone, a writer, so it
# sits above that verb's worst case, two REMOTE_BOUND calls and the feed lock's wait, and never kills a
# write the remote is still answering; the lookup, a reader the session waits on, keeps the fetch bound.
CARD_PUBLISH_BOUND=${CARD_PUBLISH_BOUND:-140}   # seconds the driver's write of the card ref may take; the env override is the fixture's
# A session idle longer than this is recommended a fresh start: the prompt cache's five-minute lifetime,
# PINNED 2026-10-25 and unverified against the platform's documentation in this tree.
RESUME_IDLE_S=300
CARD_REF_TIP=""; CARD_REF_WHY=""; CARD_DRV=""; CARD_STORED_STEP=""; CARD_STORED_FROM=""; CARD_REC=""; CARD_REC_STEP=""

read_card_policy() { # card.follows|card.store|card.snapshot|card.pointers|resume.context|resume.partial|context.on-full|context.threshold -> its value on stdout, a set's members one per line; 1 and the refusal on stdout
  local def pk d py out v n=0
  case "${1:-}" in
    card.follows) def=re-render-at-transition ;;
    card.store) def="remote-ref build-folder local-clone" ;;
    card.snapshot) def=terminal-only ;;
    card.pointers) def=every-item ;;
    resume.context) def=fresh-when-idle ;;
    resume.partial) def=continue-item ;;
    context.on-full) def=fresh-at-boundary ;;
    context.threshold) def=60% ;;
    *) printf "read_card_policy reads card.follows, card.store, card.snapshot, card.pointers, resume.context, resume.partial, context.on-full or context.threshold, and was asked for '%s'\n" "${1:-}"
       return 1 ;;
  esac
  pk=$(resolve_kit_file policy policy.py)
  if [ -z "$pk" ] || ! py=$(resolve_python 2>/dev/null); then
    printf 'card: NOTE - no policy kit resolves beside this kit, so %s takes its catalogue default %s\n' "$1" "$def" >&2
    printf '%s\n' $def
    return 0
  fi
  d=${pk%/*}
  case "$1" in
    card.follows) out=$("$py" "$d/policy.py" get card.follows 2>&1) ;;
    card.store) out=$("$py" "$d/policy.py" get card.store 2>&1) ;;
    card.snapshot) out=$("$py" "$d/policy.py" get card.snapshot 2>&1) ;;
    card.pointers) out=$("$py" "$d/policy.py" get card.pointers 2>&1) ;;
    resume.context) out=$("$py" "$d/policy.py" get resume.context 2>&1) ;;
    resume.partial) out=$("$py" "$d/policy.py" get resume.partial 2>&1) ;;
    context.on-full) out=$("$py" "$d/policy.py" get context.on-full 2>&1) ;;
    context.threshold) out=$("$py" "$d/policy.py" get context.threshold 2>&1) ;;
  esac || { printf '%s\n' "${out:-policy.py get $1 exited non-zero}"; return 1; }
  out=${out//$'\r'/}
  for v in $out; do
    n=$((n + 1))
    case "$1:$v" in
      card.follows:re-render-at-transition|card.follows:card-per-step|card.follows:fixed-at-start) ;;
      card.store:remote-ref|card.store:build-folder|card.store:local-clone) ;;
      card.snapshot:terminal-only|card.snapshot:every-transition) ;;
      card.pointers:every-item|card.pointers:at-transitions) ;;
      resume.context:fresh-when-idle|resume.context:always-resume|resume.context:always-fresh) ;;
      resume.partial:continue-item|resume.partial:restart-item|resume.partial:ask-owner) ;;
      context.on-full:compact-with-card|context.on-full:fresh-at-boundary) ;;
      context.threshold:*)
        [[ $v =~ ^(100|[1-9]?[0-9])%$ ]] \
          || { printf "%s answered '%s', which is outside the row's pattern (100|[1-9]?[0-9])%%\n" "$1" "$v"; return 1; } ;;
      *) printf "%s answered '%s', which is outside the closed set this engine branches on\n" "$1" "$v"; return 1 ;;
    esac
  done
  case "$1:$n" in
    *:0) printf '%s answered no value\n' "$1"; return 1 ;;
    card.store:*|*:1) ;;
    *) printf '%s answered %s values, and takes one\n' "$1" "$n"; return 1 ;;
  esac
  printf '%s\n' $out
}

# The driver beside this kit, which reads and writes the card ref: CARD_DRV, or CARD_REF_WHY and 1.
resolve_card_driver() { # -> 0 with CARD_DRV, 1 with CARD_REF_WHY
  CARD_DRV=""
  timeout -k 1 5 true </dev/null >/dev/null 2>&1 \
    || { CARD_REF_WHY="this node has no working timeout -k, so the read would be unbounded and none ran"; return 1; }
  [ -f "$ROOT/.unattended.conf" ] || { CARD_REF_WHY="no .unattended.conf in this tree"; return 1; }
  CARD_DRV=$(resolve_kit_file unattended unattended.sh)
  [ -n "$CARD_DRV" ] || { CARD_REF_WHY="no unattended driver resolves in this tree"; return 1; }
  return 0
}

# THE BOUNDED DRIVER CALL (TOOL-dPlacedRequest-43 S19), spelled once for the engine's four calls of the
# unattended driver, the `overlaps —` and `claims —` cells and the card ref's lookup and write:
# `resolve_card_driver`'s three checks, then the driver under the caller's bound with stdin closed,
# GOV_RUNLOG=0 and its output into the caller's files, a kill into a file and never a `$( )` capture a
# grandchild could hold open. -> the verb's exit, 124 or 137 the kill; 125 where no driver resolves,
# CARD_REF_WHY saying why and the caller printing its own skip line. THE SKIP SIGNAL
# (TOOL-dPlacedRequest-52 S19): CARD_REF_WHY is emptied on entry and set only by a skip, so each
# caller reads a skip from 125 with CARD_REF_WHY non-empty alone, and a driver's own 125, or
# `timeout`'s, reaches the caller's failure branch with the driver's first line.
run_driver_bounded() { # bound · out file · err file · verb args -> the verb's exit, 125 not run
  local b=$1 o=$2 e=$3
  shift 3
  CARD_REF_WHY=""
  resolve_card_driver || return 125
  GOV_RUNLOG=0 timeout -k 2 "$b" bash "$CARD_DRV" "$@" </dev/null >"$o" 2>"$e"
}

# The one read of the remote (TOOL-dPlacedRequest-34 S10 to S12): the driver's read-only
# `--card-ref lookup <slug>`, run through `run_driver_bounded` as `derive_claims_line` runs `--claims`,
# under CARD_FETCH_BOUND; a killed lookup wrote nothing, so it stays `not written`. The driver fetches into the
# cache ref refs/gov/remote/builds/<slug>/card and sights the feed, so nothing here fetches or writes a
# ref. Sets CARD_REF_TIP, empty where the remote holds no card, or CARD_REF_WHY: `RUN_CLAIMS is off`, a
# driver that did not answer within the bound or printed no `card-ref` line, each naming itself; 1 then,
# so a caller reads the next store and its verdict is `evidence`.
read_card_ref() { # slug -> 0 the remote answered, 1 not
  local o="$CARD_TMP/lookup" rc a
  CARD_REF_TIP=""; CARD_REF_WHY=""
  run_driver_bounded "$CARD_FETCH_BOUND" "$o" /dev/null --card-ref lookup "$1"; rc=$?
  [ "$rc" != 125 ] || [ -z "$CARD_REF_WHY" ] || return 1
  a=$(tr -d '\r' < "$o" 2>/dev/null | grep -m1 '^card-ref ')
  case "$rc:$a" in
    124:*|137:*) CARD_REF_WHY="no answer within ${CARD_FETCH_BOUND}s" ;;
    "0:card-ref — off") CARD_REF_WHY="RUN_CLAIMS is off" ;;
    "0:card-ref — none") return 0 ;;
    "0:card-ref — "*)
      CARD_REF_TIP=${a#card-ref — }
      [[ $CARD_REF_TIP =~ ^[0-9a-f]{40}([0-9a-f]{24})?$ ]] && return 0
      CARD_REF_WHY="--card-ref lookup printed no commit: ${a:0:160}"; CARD_REF_TIP="" ;;
    *:"card-ref not read — "*) CARD_REF_WHY=${a#card-ref not read — } ;;
    *) CARD_REF_WHY="--card-ref lookup exited $rc and printed no card-ref line" ;;
  esac
  return 1
}

# The instant a card's `card —` header line was published, as epoch seconds: its `published <at>`
# field, which `render_build_card` writes in local time with its offset, so two stamps from two
# offsets compare as instants. Pure arithmetic, the days-from-civil count, so no `date -d` is needed.
derive_card_epoch() { # var · header line -> the epoch seconds bound to var; 1 when the line carries no stamp that parses
  local rx='published ([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})([+-])([0-9]{2})([0-9]{2})( |$)'
  local y m d era yoe doy doe off
  [[ ${2:-} =~ $rx ]] || return 1
  y=$((10#${BASH_REMATCH[1]})); m=$((10#${BASH_REMATCH[2]})); d=$((10#${BASH_REMATCH[3]}))
  [ "$m" -le 2 ] && y=$((y - 1))
  era=$(( (y >= 0 ? y : y - 399) / 400 )); yoe=$((y - era * 400))
  doy=$(( (153 * (m > 2 ? m - 3 : m + 9) + 2) / 5 + d - 1 )); doe=$((yoe * 365 + yoe / 4 - yoe / 100 + doy))
  off=$(( 10#${BASH_REMATCH[8]} * 3600 + 10#${BASH_REMATCH[9]} * 60 )); [ "${BASH_REMATCH[7]}" = + ] || off=$((-off))
  printf -v "$1" '%s' $(( (era * 146097 + doe - 719468) * 86400 + 10#${BASH_REMATCH[4]} * 3600 + 10#${BASH_REMATCH[5]} * 60 + 10#${BASH_REMATCH[6]} - off ))
}

# A stored build card's text, from the stores `card.store` selects, chosen by FRESHNESS
# (TOOL-dPlacedRequest-99 S4) rather than a fixed ref-first order, which served an older ref over a
# newer card published offline into the cache: (1) the cache, where its `# card-ref` is `local` and
# no ref resolves or the cache's `published` stamp is the later instant; (2) the cache ref, as the
# last lookup or publish left it; (3) the cache; (4) the newest `card` record. `write_card_cache`
# stores `local` or the commit this node's own publish produced, so a sha `# card-ref` that differs
# from the ref means another writer published later, and the ref wins as `resolve_build_card` reads
# it; a `local` cache wins only by its stamp, a stamp that does not parse losing to one that does and
# two that do not falling to the ref. Written to the file; sets CARD_STORED_STEP and CARD_STORED_FROM.
read_card_stored() { # slug · outfile · the selected stores, space-padded -> 0 a card was found, 1 none
  local ref="refs/gov/remote/builds/$1/card" cache="" cref="" refc="" ac ar
  CARD_STORED_STEP=""; CARD_STORED_FROM=""
  case "$3" in *" local-clone "*) [ ! -f "$CARD_DIR/$1.md" ] || cache="$CARD_DIR/$1.md" ;; esac
  [ -z "$cache" ] || cref=$(sed -n '1s/^# card-ref //p' "$cache" | tr -d '\r')
  case "$3" in *" remote-ref "*) refc=$(git rev-parse --verify -q "$ref^{commit}" 2>/dev/null | tr -d '\r') ;; esac
  if [ -n "$cache" ] && [ "$cref" = local ] && [ -n "$refc" ]; then
    if derive_card_epoch ac "$(sed -n '2p' "$cache" | tr -d '\r')"; then
      derive_card_epoch ar "$(git log -1 --format=%B "$refc" -- 2>/dev/null | sed -n '6p' | tr -d '\r')" \
        && [ "$ac" -le "$ar" ] || refc=""
    fi
  fi
  if [ -n "$cache" ] && [ "$cref" = local ] && [ -z "$refc" ]; then
    tail -n +2 "$cache" | tr -d '\r' > "$2"
    CARD_STORED_FROM=cache
  elif [ -n "$refc" ]; then
    git log -1 --format=%B "$refc" -- 2>/dev/null | tr -d '\r' | awk 'NR > 5 { l[++n] = $0 } END { while (n > 0 && l[n] == "") n--; for (i = 1; i <= n; i++) print l[i] }' > "$2"
    CARD_STORED_STEP=$(git log -1 --format=%B "$refc" -- 2>/dev/null | sed -n '3s/^step: \([^ ]*\).*/\1/p' | tr -d '\r')
    CARD_STORED_FROM=ref
  elif [ -n "$cache" ]; then
    tail -n +2 "$cache" | tr -d '\r' > "$2"
    CARD_STORED_FROM=cache
  elif case "$3" in *" build-folder "*) read_card_record "$1" ;; *) false ;; esac; then
    awk '/^~~~~$/ { if (f++) exit; next } f' "$CARD_REC" | tr -d '\r' > "$2"
    CARD_STORED_STEP=$CARD_REC_STEP; CARD_STORED_FROM=record
  else
    return 1
  fi
  [ -n "$CARD_STORED_STEP" ] || CARD_STORED_STEP=$(sed -n '1s/^card — [^ ]* · step \([^ ]*\) .*/\1/p' "$2")
  return 0
}

# The newest `card` record of the build in the session's own tree, by its `<n>`: CARD_REC and CARD_REC_STEP.
read_card_record() { # slug -> 0 found, 1 none
  local memroot
  CARD_REC=""; CARD_REC_STEP=""
  memroot=$(read_memory_root) && [ -n "$memroot" ] || return 1
  CARD_REC=$(for f in "$CARD_TREE/$memroot/builds/$1/build/"*-card-*.md; do [ -f "$f" ] && printf '%s\n' "$f"; done \
    | LC_ALL=C awk '{ n = $0; sub(/^.*\//, "", n) }
        n ~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}-build-.+-card-[0-9]+\.md$/ { sub(/^.*-card-/, "", n); sub(/\.md$/, "", n)
          if (n + 0 > best) { best = n + 0; p = $0 } }
        END { if (p != "") print p }')
  [ -n "$CARD_REC" ] || return 1
  CARD_REC_STEP=$(sed -n 's/^- \*\*Step:\*\* \([^ ]*\).*/\1/p' "$CARD_REC" | head -n 1 | tr -d '\r')
  return 0
}

# The build card's text: one header line, the startup cells `render_card` re-renders here with the
# `## pockets` section fitted to the cap, and the tail file — the `## task`, `## route` and other body
# sections and the READY line. Refused past CARD_CAP_BYTES, as `write_card` refuses.
render_build_card() { # slug · step · tail file · writer verb -> the card on stdout; 1 and the refusal on stdout
  local out="$CARD_TMP/bc.render" bytes at
  printf -v at '%(%Y-%m-%dT%H:%M:%S%z)T' -1
  {
    printf 'card — %s · step %s · published %s · by %s\n' "$1" "$2" "$at" "$CARD_SID"
    render_card "$4" | awk -v want=startup "$CARD_PARTS_AWK" | tail -n +2
    cat "$3"
  } | derive_pockets_block > "$out"
  bytes=$(wc -c < "$out" | tr -d '[:space:]')
  if [ "$bytes" -gt "$CARD_CAP_BYTES" ]; then
    printf 'card — not written: the build card is %s bytes, over the %s-byte cap (CARD_CAP_BYTES)\n' "$bytes" "$CARD_CAP_BYTES"
    return 1
  fi
  cat "$out"
}

# The build card written to each store `card.store` selects. The tail comes from the session's card
# (`session`), the stored build card (`stored`) or is `READY — none yet` alone (`none`); an empty step is
# the stored card's, else `unrecorded`. Snapshot 1 writes the `card` record where build-folder is selected.
write_build_card() { # slug · step or empty · session|stored|none · writer verb · snapshot 0|1 · terminal 0|1 -> its card — lines; 0 always
  local slug=$1 step=$2 mode=$3 verb=$4 snap=$5 term=$6 stores ref="refs/gov/remote/builds/$1/card" card="$CARD_TMP/bc.card"
  local tail="$CARD_TMP/bc.tail" tip="" c rc try oid=local remote=0 msg mark="" a from="" bytes sb
  [ "$term" != 1 ] || mark=" · terminal"
  stores=$(read_card_policy card.store) || { printf 'card — skipped: card.store refused: %s\n' "${stores%%$'\n'*}"; return 0; }
  stores=" ${stores//$'\n'/ } "
  case "$stores" in *" remote-ref "*) remote=1 ;; esac
  if [ "$remote" = 1 ] && ! read_card_ref "$slug"; then
    printf 'card — remote-ref not written: %s\n' "$CARD_REF_WHY"; remote=2
  fi
  # The driver writes the ref (TOOL-dPlacedRequest-33 S2), through `run_driver_bounded` under its own
  # publish bound (TOOL-dPlacedRequest-43 S16, S19).
  tip=$CARD_REF_TIP
  for try in 1 2; do
    case "$mode" in
      session) awk -v want=tail "$CARD_PARTS_AWK" "$CARD_FILE" > "$tail" ;;
      # THE STORE THE TAIL CAME FROM rides each success line below (TOOL-dPlacedRequest-99 S6), in this
      # mode alone, the one that reads a stored tail.
      stored) from=""
              if read_card_stored "$slug" "$CARD_TMP/bc.stored" "$stores"; then awk -v want=tail "$CARD_PARTS_AWK" "$CARD_TMP/bc.stored" > "$tail"; from=" · tail from $CARD_STORED_FROM"
              else printf 'READY — none yet\n' > "$tail"; fi ;;
      none) printf 'READY — none yet\n' > "$tail" ;;
    esac
    # Every tail carries a fresh `## pointers` section, so every publish and every follow does, under
    # both values of card.pointers (KICK-dKeptSession-13 S4, S8).
    write_pointers "$tail" "$slug"
    if [ -z "$2" ]; then
      step=unrecorded
      ! read_card_stored "$slug" "$CARD_TMP/bc.stored" "$stores" || [ -z "$CARD_STORED_STEP" ] || step=$CARD_STORED_STEP
    fi
    if ! render_build_card "$slug" "$step" "$tail" "$verb" > "$card"; then
      # A card the section alone pushes past the cap is named as the section's refusal (S4).
      bytes=$(wc -c < "$CARD_TMP/bc.render" | tr -d '[:space:]')
      sb=$(wc -c < "$CARD_TMP/pointers.sec" 2>/dev/null | tr -d '[:space:]')
      if [ -n "$sb" ] && [ $((bytes - sb)) -le "$CARD_CAP_BYTES" ]; then
        printf 'card — pointers not written: %s bytes over the cap\n' "$((bytes - CARD_CAP_BYTES))"
      else
        cat "$card"
      fi
      return 0
    fi
    [ "$remote" = 1 ] || break
    printf -v msg 'gov-card %s\n\nstep: %s%s\nsession: %s\n\n%s' "$slug" "$step" "$mark" "$CARD_SID" "$(<"$card")"
    printf '%s' "$msg" > "$CARD_TMP/bc.msg" || { printf 'card — remote-ref not written: cannot write the message to %s\n' "$CARD_TMP/bc.msg"; remote=2; break; }
    run_driver_bounded "$CARD_PUBLISH_BOUND" "$CARD_TMP/bc.ref" "$CARD_TMP/bc.err" --card-ref write "$slug" --message "$CARD_TMP/bc.msg"; rc=$?
    a=$(tr -d '\r' < "$CARD_TMP/bc.ref" 2>/dev/null | grep -m1 '^card-ref ')
    # A KILLED PUBLISH MAY HAVE LANDED (TOOL-dPlacedRequest-43 S17): the write can reach the remote before
    # the bound fires, and a landed one reaches the feed at the next sighting, so its outcome is unknown.
    case "$rc${CARD_REF_WHY:+:skip}:$a" in
      125:skip:*) printf 'card — remote-ref not written: %s\n' "$CARD_REF_WHY"; remote=2; break ;;
      124:*|137:*) printf 'card — remote-ref unknown: no answer within %ss\n' "$CARD_PUBLISH_BOUND"; remote=2; break ;;
      "0:card-ref — off") printf 'card — remote-ref not written: RUN_CLAIMS is off\n'; remote=2; break ;;
      "0:card-ref — "*)
        c=$(git rev-parse --verify -q "$ref^{commit}" 2>/dev/null | tr -d '\r')
        [ -z "$c" ] || [ "${c:0:8}" != "${a##* · }" ] || oid=$c
        printf 'card — %s · step %s · remote-ref %s%s\n' "$slug" "$step" "${a##* · }" "$from"
        break ;;
      "1:card-ref lost — "*)
        if [ "$try" = 1 ] && read_card_ref "$slug" && [ "$CARD_REF_TIP" != "$tip" ]; then
          tip=$CARD_REF_TIP
          continue
        fi
        printf 'card — remote-ref not written: lost to %s\n' "${a##*— }"; remote=2; break ;;
      *:"card-ref not written — "*) printf 'card — remote-ref not written: %s\n' "${a#card-ref not written — }"; remote=2; break ;;
    esac
    # No `card-ref` line: the driver's first refusal line — `fail` prints to stdout — else its first
    # line of any kind, cut at 160 bytes, as `derive_claims_line` words a `--claims` that did not answer.
    LC_ALL=C awk -v rc="$rc" '{ sub(/\r$/, "") }
      NF && f == "" { f = $0 }
      /FAILED/ { f = $0; exit }
      END { if (f == "") f = "--card-ref exited " rc " and printed nothing"
            if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }
            print "card — remote-ref not written: " f }' "$CARD_TMP/bc.ref" "$CARD_TMP/bc.err"
    remote=2; break
  done
  case "$stores" in
    *" local-clone "*)
      if write_card_cache "$slug" "$oid" "$card"; then
        printf 'card — %s · step %s · local-clone %s%s\n' "$slug" "$step" "$CARD_DIR/$slug.md" "$from"
      else
        printf 'card — local-clone not written: cannot write %s\n' "$CARD_DIR/$slug.md"
      fi ;;
  esac
  case "$stores:$snap" in
    *" build-folder "*:1) write_card_snapshot "$slug" "$step" "${oid/#local/none}" "$card" "$from" ;;
  esac
  return 0
}

# The cache, written through a temp `mktemp` names beside it and renamed into place, so a reader never
# sees half a card and no other writer can know the temp's name before it exists.
write_card_cache() { # slug · the ref's commit or local · card file -> 0 written, 1 not
  local t
  mkdir -p "$CARD_DIR" 2>/dev/null && t=$(mktemp "$CARD_DIR/.card.XXXXXX" 2>/dev/null) || return 1
  if { printf '# card-ref %s\n' "$2"; cat -- "$3"; } > "$t" 2>/dev/null && mv -f "$t" "$CARD_DIR/$1.md" 2>/dev/null; then
    return 0
  fi
  rm -f "$t" 2>/dev/null
  return 1
}

# The `card` record, through the record factory's `write_record` (no door), its anchor the loop kit's
# `resolve_build_anchor`, committed ALONE in the session's own tree: a staged index refuses it, named,
# and a commit git refuses leaves no file behind.
CARD_SNAPSHOT_PY='import pathlib, sys
sys.path[:0] = sys.argv[1:3]
from build_records import write_record
from loop_transition import resolve_build_anchor
root = pathlib.Path(sys.argv[3]).absolute()
build, step, ref, card = sys.argv[4:8]
anchor = resolve_build_anchor(build, root)
if anchor is None:
    sys.exit("no spec H1 under the build defines a unit, so the record has no anchor")
text = pathlib.Path(card).read_text(encoding="utf-8").replace("\r", "").rstrip("\n").split("\n")
try:
    print(write_record(root, build, anchor, "card", step, [("Build", build), ("Step", step), ("Ref", ref)],
                       lines=["~~~~", *text, "~~~~"]))
except (ValueError, OSError) as e:
    sys.exit(str(e))'
write_card_snapshot() { # slug · step · ref commit or none · card file · [success-line suffix] -> one card — line; 0 always
  local br lt py rel why
  br=$(resolve_kit_file memory-tree build_records.py); lt=$(resolve_kit_file loop loop_transition.py)
  [ -n "$br" ] || { printf 'card — build-folder not written: no memory-tree build_records.py resolves in this tree\n'; return 0; }
  [ -n "$lt" ] || { printf 'card — build-folder not written: no loop kit resolves the build anchor\n'; return 0; }
  py=$(resolve_python 2>/dev/null) || { printf 'card — build-folder not written: no Python resolves on this node\n'; return 0; }
  git -C "$CARD_TREE" diff --cached --quiet 2>/dev/null \
    || { printf 'card — build-folder not written: the index of %s holds staged changes, and a snapshot is committed alone\n' "$CARD_TREE"; return 0; }
  rel=$("$py" -c "$CARD_SNAPSHOT_PY" "${br%/*}" "${lt%/*}" "$CARD_TREE" "$1" "$2" "$3" "$4" 2>&1) \
    || { why=${rel//$'\r'/}; why=${why#$'\n'}; why=${why%%$'\n'*}; printf 'card — build-folder not written: %s\n' "${why:0:200}"; return 0; }
  rel=${rel//$'\r'/}; rel=${rel##*$'\n'}
  if git -C "$CARD_TREE" add -- "$rel" 2>/dev/null && ! git -C "$CARD_TREE" diff --cached --quiet 2>/dev/null \
    && git -C "$CARD_TREE" commit -q -m "card snapshot($1): $2" >/dev/null 2>&1; then
    printf 'card — %s · step %s · build-folder %s · commit %s%s\n' "$1" "$2" "$rel" "$(git -C "$CARD_TREE" rev-parse --short=8 HEAD 2>/dev/null | tr -d '\r')" "${5:-}"
  else
    git -C "$CARD_TREE" reset -q -- "$rel" 2>/dev/null; rm -f "$CARD_TREE/$rel"
    printf 'card — build-folder not written: git could not commit %s\n' "$rel"
  fi
  return 0
}

# The publish from the session's card (S3), at READY and by hand: no step of its own, and a snapshot
# only where `card.snapshot` is `every-transition`.
write_card_publish() { # slug · writer verb -> its card — lines; 0 always
  local snapshot snap=0
  snapshot=$(read_card_policy card.snapshot) || { printf 'card — skipped: card.snapshot refused: %s\n' "${snapshot%%$'\n'*}"; return 0; }
  [ "$snapshot" != every-transition ] || snap=1
  write_build_card "$1" "" session "$2" "$snap" 0
}

# The follow at a stage move (S4): `card.follows` decides what is re-published, `card.snapshot` whether
# the move writes a `card` record. A terminal move always publishes; a terminal move whose state the
# newest record already names writes no second record.
write_card_follow() { # slug · state · terminal 0|1 -> its card — lines; 0 always
  local follows snapshot snap=0 mode=stored
  follows=$(read_card_policy card.follows) || { printf 'card — skipped: card.follows refused: %s\n' "${follows%%$'\n'*}"; return 0; }
  if [ "$follows" = fixed-at-start ] && [ "$3" = 0 ]; then
    printf 'card — %s · step %s · fixed-at-start: nothing written\n' "$1" "$2"; return 0
  fi
  [ "$follows" != card-per-step ] || mode=none
  snapshot=$(read_card_policy card.snapshot) || { printf 'card — skipped: card.snapshot refused: %s\n' "${snapshot%%$'\n'*}"; return 0; }
  if [ "$3" = 1 ] || [ "$snapshot" = every-transition ]; then snap=1; fi
  if [ "$3" = 1 ] && read_card_record "$1" && [ "$CARD_REC_STEP" = "$2" ]; then
    printf 'card — snapshot kept: %s already recorded\n' "$2"; snap=0
  fi
  write_build_card "$1" "$2" "$mode" follow "$snap" "$3"
}

# ---- the card's pointers (KICK-dKeptSession-13) ---------------------------------------------------
# THE SECTION, I11: `## pointers` and its lines, in each tail `write_build_card` builds and in a session's
# card, directly above the READY line, which stays last:
#   records — <kind> <path> · …      the build's newest bound record of each kind, `gen_build_index.py
#                                     --latest-records`, under CARD_RECORDS_BOUND
#   forks — <spec path> §8 · …       each unit the item boundary's derivation grades FORKED, by its tracked
#                                     spec under the build's `spec/`; the `§8` a word apart, so the path is
#                                     one token `extract_card_tokens` finds tracked
#   item — <instance key|none> · at <sha8>   the boundary's answer and the HEAD it was derived at
#   budget — <answer>                the build's rework budget, the loop kit's `budget.py state --build
#                                     <slug>` line as it prints it, under CARD_BUDGET_BOUND (KICK-dKeptSession-26)
# A source that does not resolve is its line's `<word> — skipped: <why>`, the `item —` line still ending
# ` · at <sha8>`. THE ITEM BOUNDARY, I12, is the loop kit's `position.py <slug> --boundary <pointer>`, run by
# `run_item_boundary` under CARD_POSITION_BOUND, once per process: its file is kept for every later write.
# `card.pointers` decides what a crossing publishes: `every-item` the build card, `at-transitions`
# nothing, a follow re-rendering the section under both. WHAT THIS DOES NOT CHECK: that a record's text or
# a fork is current between two boundaries; the section is as fresh as its last write.
run_item_boundary() { # slug · pointer · file -> 0 with the boundary's two lines in the file, 1 with one why line in it
  local pos py rc
  pos=$(resolve_kit_file loop position.py)
  [ -n "$pos" ] || { printf 'no loop kit position.py resolves in this tree\n' > "$3"; return 1; }
  py=$(resolve_python 2>/dev/null) || { printf 'no Python resolves on this node\n' > "$3"; return 1; }
  timeout -k 1 5 true </dev/null >/dev/null 2>&1 \
    || { printf 'this node has no working timeout -k, so the read would be unbounded and none ran\n' > "$3"; return 1; }
  timeout -k 2 "$CARD_POSITION_BOUND" "$py" "$pos" "$1" --boundary "$2" </dev/null > "$3.raw" 2>&1; rc=$?
  if { [ "$rc" = 0 ] || [ "$rc" = 2 ]; } && tr -d '\r' < "$3.raw" | head -n 1 | grep -q '^boundary — '; then
    tr -d '\r' < "$3.raw" > "$3"; rm -f "$3.raw"; return 0
  fi
  case "$rc" in
    124|137) printf 'the position read did not answer within %ss\n' "$CARD_POSITION_BOUND" > "$3" ;;
    *) LC_ALL=C awk -v rc="$rc" '{ sub(/\r$/, "") }
         NF && f == "" { f = $0 }
         END { if (f == "") f = "position.py --boundary exited " rc " and printed nothing"
               if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }
               print f }' "$3.raw" > "$3" ;;
  esac
  rm -f "$3.raw"
  return 1
}

# The section over one boundary file, `run_item_boundary`'s: its key the crossing's target, or the
# pointer it kept; the `at` HEAD now, read in the same process that derived it.
render_pointers() { # slug · boundary file -> the section on stdout; 0 always
  local at gbi py rc recs b item ids id spec forks="" memroot
  at=$(git rev-parse --short=8 HEAD 2>/dev/null | tr -d '\r'); at=${at:-unborn}
  printf '## pointers\n'
  gbi=$(resolve_kit_file memory-tree gen_build_index.py)
  if [ -z "$gbi" ]; then
    printf 'records — skipped: no memory-tree gen_build_index.py resolves in this tree\n'
  elif ! py=$(resolve_python 2>/dev/null); then
    printf 'records — skipped: no Python resolves on this node\n'
  else
    timeout -k 2 "$CARD_RECORDS_BOUND" "$py" "$gbi" --latest-records "$1" </dev/null > "$CARD_TMP/pointers.recs" 2>&1; rc=$?
    case "$rc" in
      0) recs=$(LC_ALL=C awk '{ sub(/\r$/, "") } NF { printf "%s%s", (n++ ? " · " : ""), $0 }' "$CARD_TMP/pointers.recs")
         printf 'records — %s\n' "${recs:-none}" ;;
      124|137) printf 'records — skipped: the records read did not answer within %ss\n' "$CARD_RECORDS_BOUND" ;;
      *) LC_ALL=C awk -v rc="$rc" '{ sub(/\r$/, "") } NF && f == "" { f = $0 }
           END { if (f == "") f = "gen_build_index.py --latest-records exited " rc " and printed nothing"
                 if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }
                 print "records — skipped: " f }' "$CARD_TMP/pointers.recs" ;;
    esac
  fi
  b=$(sed -n '1p' "$2" 2>/dev/null)
  case "$b" in
    "boundary — none crossed · item "*) item=${b#boundary — none crossed · item }; item=${item%% · *} ;;
    "boundary — "*" → "*) item=${b##* → } ;;
    *) printf 'forks — skipped: %s\n' "${b:-no boundary was read}"
       printf 'item — skipped: %s · at %s\n' "${b:-no boundary was read}" "$at"; render_budget_line "$1"; return 0 ;;
  esac
  ids=$(sed -n 's/^forked — //p' "$2" | head -n 1)
  memroot=$(read_memory_root) || memroot=""
  if [ -z "$memroot" ]; then
    printf 'forks — skipped: no MEMORY_ROOT names the build folder\n'
  else
    for id in ${ids// · / }; do
      [[ $id =~ ^[A-Za-z]+-[A-Za-z0-9]+-[0-9]+$ ]] || continue
      spec=$(git ls-files -- "$memroot/builds/$1/spec/*-spec-$id.md" 2>/dev/null | head -n 1)
      [ -z "$spec" ] || forks="${forks:+$forks · }$spec §8"
    done
    printf 'forks — %s\n' "${forks:-none}"
  fi
  printf 'item — %s · at %s\n' "$item" "$at"
  render_budget_line "$1"
}

# The section's `budget —` line (KICK-dKeptSession-26 S1): the one line the loop kit's `budget.py state
# --build <slug>` prints, `open <spent>/<total>`, `spent` or `unfrozen <spent>/<total>`, never re-derived
# here. Run in `$ROOT`, whose build the module reads under the working directory, stdin closed, into a
# scratch file under CARD_BUDGET_BOUND, as `derive_map_block` bounds the map; the answer held to one line
# of printable text. Every failure is one `budget — skipped:` line, and the section is still written.
# WHAT THIS DOES NOT CHECK: that the answer is current past this render; a draw shows at the next one.
render_budget_line() { # slug -> one budget — line on stdout; 0 always
  local bk py rc sf="$CARD_TMP/pointers.budget" line
  bk=$(resolve_kit_file loop budget.py)
  [ -n "$bk" ] || { printf 'budget — skipped: no loop kit\n'; return 0; }
  py=$(resolve_python 2>/dev/null) || { printf 'budget — skipped: no Python resolves on this node\n'; return 0; }
  timeout -k 1 5 true </dev/null >/dev/null 2>&1 \
    || { printf 'budget — skipped: this node has no working timeout -k, so the read would be unbounded and none ran\n'; return 0; }
  (cd "$ROOT" && timeout -k 2 "$CARD_BUDGET_BOUND" "$py" "$bk" state --build "$1" </dev/null > "$sf" 2>/dev/null); rc=$?
  case "$rc" in
    0) line=$(LC_ALL=C awk '{ sub(/\r$/, ""); gsub(/[[:cntrl:]]/, "") }
         NF { f = $0; if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }; print f; exit }' "$sf")
       if [ -n "$line" ]; then printf 'budget — %s\n' "$line"
       else printf 'budget — skipped: budget.py state exited 0 and printed nothing\n'; fi ;;
    124|137) printf 'budget — skipped: budget.py state did not answer within %ss\n' "$CARD_BUDGET_BOUND" ;;
    *) printf 'budget — skipped: budget.py state exited %s\n' "$rc" ;;
  esac
  rm -f "$sf" 2>/dev/null
  return 0
}

# The `item —` line's key in a card or a tail, `none` where the section, the line or a key is absent.
read_card_item_key() { # card or tail file -> the key on stdout; 0 always
  local k
  k=$(LC_ALL=C awk '{ sub(/\r$/, "") } /^## pointers[[:space:]]*$/ { inp = 1; next } inp && (/^## / || /^(- )?READY — /) { inp = 0 }
    inp && /^item — [^ ]+ · at / { split($0, w, " "); print w[3]; exit }' "$1")
  case "$k" in ""|skipped:) k=none ;; esac
  printf '%s\n' "$k"
}

# S4: the tail's `## pointers` section replaced, its heading to the line before the next `## ` heading or
# READY line, or inserted directly before the READY line. The boundary is read once per process, at the
# tail's own `item —` key; the section written is kept in `$CARD_TMP/pointers.sec` for the cap's refusal.
write_pointers() { # tail file · slug -> 0 always
  local bf="$CARD_TMP/pointers.boundary" sec="$CARD_TMP/pointers.sec"
  [ -f "$bf" ] || run_item_boundary "$2" "$(read_card_item_key "$1")" "$bf"
  render_pointers "$2" "$bf" > "$sec"
  PT_SEC="$sec" LC_ALL=C awk 'BEGIN { while ((getline l < ENVIRON["PT_SEC"]) > 0) s = s l "\n" }
    { sub(/\r$/, "") }
    /^## pointers[[:space:]]*$/ { skip = 1; next }
    skip && (/^## / || /^(- )?READY — /) { skip = 0 }
    skip { next }
    !done && /^(- )?READY — / { printf "%s", s; done = 1 }
    { print }
    END { if (!done) printf "%s", s }' "$1" > "$1.p" && mv -f "$1.p" "$1"
  return 0
}

# The session's card rewritten from `$CARD_TMP/startup` and the tail file, its `## pockets` section refitted
# to the room, then re-rendered into the card file; refused past CARD_CAP_BYTES with the card left as it was.
write_card_parts() { # tail file -> 0 written, 1 not, its card — line printed
  local new="$CARD_TMP/parts.new" bytes
  cat "$CARD_TMP/startup" "$1" | derive_pockets_block > "$new"
  bytes=$(wc -c < "$new" | tr -d '[:space:]')
  if [ "$bytes" -gt "$CARD_CAP_BYTES" ]; then
    printf 'card — pointers not written: %s bytes over the cap\n' "$((bytes - CARD_CAP_BYTES))"; return 1
  fi
  cat "$new" > "$CARD_FILE" 2>/dev/null || { printf 'card — pointers not written: cannot write %s\n' "$CARD_FILE"; return 1; }
  write_card_file
  return 0
}

# The section written into the session's card (S4's `--session`, S6's crossing).
write_card_pointers() { # slug -> 0 always
  extract_card_parts "$CARD_FILE"
  write_pointers "$CARD_TMP/tail" "$1"
  write_card_parts "$CARD_TMP/tail"
  return 0
}

# S6, the one item-boundary point. First the session card's `item —` line moves to HEAD, a section holding
# `item — none · at <sha8>` written where the card has none, so the hook starts no second verb at this
# HEAD; then the boundary is read once at the line's old key. A crossing rewrites the session card's
# section and, under `every-item`, publishes the build card in `stored` mode; with none crossed nothing is
# published, and the section is rewritten only where it lacks a POINTER_LINES line, so a card the first
# step gave a section passes `--card --check`. Every later item-boundary reader runs here, after S1:
# `context.on-full` (KICK-dKeptSession-14), `mailbox.reads` (KICK-dKeptSession-10) and `mailbox.notice`
# (KICK-dKeptSession-21); `actions.free` (KICK-dKeptSession-8) reads the `item —` line this leaves.
run_card_boundary() { # slug -> the verb's lines on stdout; 0, or 2 with no session card
  local slug=$1 old at b mode bf="$CARD_TMP/pointers.boundary"
  [ -f "$CARD_FILE" ] || { echo "MANIFEST env ERROR — no card for session $CARD_SID at $CARD_FILE, so it holds no item"; return 2; }
  old=$(read_card_item_key "$CARD_FILE")
  at=$(git rev-parse --short=8 HEAD 2>/dev/null | tr -d '\r'); at=${at:-unborn}
  extract_card_parts "$CARD_FILE"
  LC_ALL=C awk -v at="$at" '{ sub(/\r$/, "") }
    /^## pointers[[:space:]]*$/ { inp = 1; seen = 1; print; next }
    inp && (/^## / || /^(- )?READY — /) { if (!item) print "item — none · at " at; inp = 0; item = 1 }
    inp && /^item — / { sub(/ · at [^ ]*$/, ""); print $0 " · at " at; item = 1; next }
    !seen && /^(- )?READY — / { print "## pointers"; print "item — none · at " at; seen = 1; item = 1 }
    { print }
    END { if (inp && !item) print "item — none · at " at; if (!seen) { print "## pointers"; print "item — none · at " at } }' \
    "$CARD_TMP/tail" > "$CARD_TMP/tail.at" && write_card_parts "$CARD_TMP/tail.at"
  run_item_boundary "$slug" "$old" "$bf"
  b=$(sed -n '1p' "$bf")
  case "$b" in
    "boundary — none crossed"*)
      printf '%s\n' "$b"
      [ -z "$(check_card_pointers "$CARD_FILE")" ] || write_card_pointers "$slug" ;;
    "boundary — "*" → "*)
      printf '%s\n' "$b"
      write_card_pointers "$slug"
      if mode=$(read_card_policy card.pointers); then
        [ "$mode" != every-item ] || write_build_card "$slug" "" stored boundary 0 0
      else
        printf 'card — skipped: card.pointers refused: %s\n' "${mode%%$'\n'*}"
      fi
      run_context_boundary ;;
    *)
      printf 'boundary — skipped: %s\n' "$b"
      write_card_pointers "$slug" ;;
  esac
  return 0
}

# The verdict on a cached card against the ref (TOOL-dDeclaredLoop-8 S3's words), the loop kit's
# `claims.py verdict`: `evidence` with no ref read, `fresh` when the cache's `# card-ref` equals the
# ref's commit, `re-derived` when it does not. Where that reader does not resolve the cache is never
# trusted, `re-derived` with a ref read and `evidence` without, so no second copy of its rule is here.
derive_card_verdict() { # cached card-ref or empty · the ref's commit or empty -> fresh, re-derived or evidence
  local ck py v
  ck=$(resolve_kit_file loop claims.py)
  if [ -n "$ck" ] && py=$(resolve_python 2>/dev/null) \
      && v=$("$py" "$ck" verdict --stored "${1:-?}" --class history ${2:+--recomputed "$2"} 2>/dev/null); then
    printf '%s\n' "${v%$'\r'}"; return 0
  fi
  if [ -n "$2" ]; then echo re-derived; else echo evidence; fi
}

# The lookup (S6): the build card from the first selected store that answers — the ref, the cache
# while its `# card-ref` equals the ref, the newest record — then re-keyed into the session's card: its
# own header and the startup cells re-rendered here, the build card's tail kept.
resolve_build_card() { # slug -> one card — line; 0 always
  local slug=$1 stores cache="$CARD_DIR/$1.md" cref="" verdict="" what="" from="$CARD_TMP/bc.found" tip="" bytes
  stores=$(read_card_policy card.store) || { printf 'card — skipped: card.store refused: %s\n' "${stores%%$'\n'*}"; return 0; }
  stores=" ${stores//$'\n'/ } "
  case "$stores" in *" local-clone "*) ;; *) cache="" ;; esac
  [ -z "$cache" ] || [ ! -f "$cache" ] || cref=$(sed -n '1s/^# card-ref //p' "$cache" | tr -d '\r')
  case "$stores" in
    *" remote-ref "*)
      if read_card_ref "$slug" && [ -n "$CARD_REF_TIP" ]; then
        tip=$CARD_REF_TIP
        verdict=$(derive_card_verdict "$cref" "$tip")
        if [ "$verdict" = fresh ]; then
          tail -n +2 "$cache" | tr -d '\r' > "$from"; what="cache trusted"
        else
          verdict=re-derived
          git log -1 --format=%B "refs/gov/remote/builds/$slug/card" -- 2>/dev/null | tr -d '\r' \
            | awk 'NR > 5 { l[++n] = $0 } END { while (n > 0 && l[n] == "") n--; for (i = 1; i <= n; i++) print l[i] }' > "$from"
          what="read the ref"
          case "$stores" in
            *" local-clone "*) write_card_cache "$slug" "$tip" "$from" && what="cache rewritten" ;;
          esac
        fi
      fi ;;
  esac
  if [ -z "$verdict" ]; then
    case "$stores" in *" local-clone "*) [ -n "$cache" ] && [ -f "$cache" ] && { tail -n +2 "$cache" | tr -d '\r' > "$from"; what="read the cache"; verdict=evidence; } ;; esac
  fi
  if [ -z "$verdict" ]; then
    case "$stores" in *" build-folder "*) read_card_record "$slug" && { awk '/^~~~~$/ { if (f++) exit; next } f' "$CARD_REC" | tr -d '\r' > "$from"; what="read the snapshot ${CARD_REC##*/}"; verdict=evidence; } ;; esac
  fi
  if [ -z "$verdict" ]; then
    printf 'card — none published for %s%s\n' "$slug" "${CARD_REF_WHY:+ · the remote did not answer: $CARD_REF_WHY}"; return 0
  fi
  # A session that holds a card keeps its header line, as the replay's re-key does, since the scratch
  # guard reads the writer verb on it; the replay's own render reads no remote.
  local verb=lookup
  [ "$CARD_VERB" != replay ] || verb=replay
  {
    render_card "$verb" | awk -v want=startup "$CARD_PARTS_AWK" \
      | { IFS= read -r hd; if [ -f "$CARD_FILE" ]; then head -n 1 "$CARD_FILE" | tr -d '\r'; else printf '%s\n' "$hd"; fi; cat; }
    awk -v want=tail "$CARD_PARTS_AWK" "$from"
  } | derive_pockets_block > "$CARD_TMP/bc.rekeyed"
  bytes=$(wc -c < "$CARD_TMP/bc.rekeyed" | tr -d '[:space:]')
  if [ "$bytes" -gt "$CARD_CAP_BYTES" ]; then
    what="$what · not re-keyed: $bytes bytes, over the $CARD_CAP_BYTES-byte cap"
  elif mkdir -p "$CARD_DIR" && cat "$CARD_TMP/bc.rekeyed" > "$CARD_FILE"; then
    what="$what · re-keyed into $CARD_SID.md"
  else
    what="$what · not re-keyed: cannot write $CARD_FILE"
  fi
  printf 'card — %s · %s · ref %s · %s\n' "$slug" "$verdict" "${tip:0:8}" "$what"
  [ -n "$tip" ] || [ -z "$CARD_REF_WHY" ] || printf 'card — the remote did not answer: %s\n' "$CARD_REF_WHY"
}

# The route's build on a card or body: its one `- build:` line under `## route`, or nothing.
read_card_build() { # file -> the slug, or nothing
  LC_ALL=C awk '{ sub(/\r$/, "") } /^[[:space:]]*## route[[:space:]]*$/ { inr = 1; next } inr && (/^## / || /^(- )?READY — /) { inr = 0 }
    inr && /^- build: [A-Za-z0-9]+$/ { print substr($0, 10); exit }' "$1"
}

# The publisher's tree (KICK-dKeptSession-12 S4): the `tree —` cell's first field, up to ` · `, of the
# build card `resolve_build_card` stored in `$CARD_TMP/bc.found` before its re-key, since the re-key
# re-renders that cell in the replaying session's own tree. Nothing when no card was found.
read_stored_tree_cell() { # -> the path, or nothing; 0 always
  [ -f "$CARD_TMP/bc.found" ] || return 0
  awk '{ sub(/\r$/, "") } /^tree — / { sub(/^tree — /, ""); i = index($0, " · "); print (i ? substr($0, 1, i - 1) : $0); exit }' "$CARD_TMP/bc.found"
}

# The resume (S7), after the replay's lookup: the route re-checked over the re-keyed card, then the
# `resume —` line under resume.context and the `partial —` line under resume.partial. `always-resume`
# holds only while the card-import fixture's recorded verdict, `read_card_fixture_verdict`, answers
# `pass`. The entry file is not consulted. Every line recommending fresh names the tree to start it in
# (KICK-dKeptSession-12 S4): the stored build card's `tree —` path where `git worktree list` lists it
# byte for byte, else a new worktree of the build. The `partial —` line names the act the kickoff
# skill's resume paragraph states; the replay performs none of them.
derive_resume_lines() { # slug -> the route —, resume — and partial — lines; 0 always
  local out rc rule ctx rec part act v mtime idle n tx=$CARD_TRANSCRIPT tree wl where
  out=$( CARD_TMP="$CARD_TMP/rc" && mkdir -p "$CARD_TMP" && check_card_citations "$CARD_FILE" >/dev/null 2>&1 \
         && extract_card_parts "$CARD_FILE" && check_card_route "$CARD_FILE" 1 2>&1 ); rc=$?
  rule=ok
  if [ "$rc" != 0 ]; then
    rule=""
    [[ $out =~ route\ (R[0-9])[\ :] ]] && rule=${BASH_REMATCH[1]}
  fi
  printf 'route — re-checked · %s\n' "${rule:-unchecked: the check exited $rc}"
  if ctx=$(read_card_policy resume.context); then
    tree=$(read_stored_tree_cell); where="a new worktree of $1"
    if [ -n "$tree" ] && wl=$(git worktree list --porcelain 2>/dev/null); then
      wl=${wl//$'\r'/}
      [[ $'\n'$wl$'\n' == *$'\n'"worktree $tree"$'\n'* ]] && where=$tree
    fi
    rec="fresh recommended: transcript absent · in $where"
    if [ -n "$tx" ] && [ -f "$tx" ] && mtime=$(stat -c %Y -- "$tx" 2>/dev/null) && [[ $mtime =~ ^[0-9]+$ ]]; then
      idle=$(( EPOCHSECONDS - mtime ))
      if [ "$idle" -gt "$RESUME_IDLE_S" ]; then rec="fresh recommended: idle ${idle}s past ${RESUME_IDLE_S}s · in $where"
      else rec="resume recommended: idle ${idle}s within ${RESUME_IDLE_S}s"; fi
    fi
    case "$ctx" in
      always-fresh) printf 'resume — fresh recommended · in %s (resume.context: always-fresh)\n' "$where" ;;
      fresh-when-idle) printf 'resume — %s (resume.context: fresh-when-idle)\n' "$rec" ;;
      always-resume)
        v=$(read_card_fixture_verdict); v=${v:-red: the reader printed nothing}
        if [ "$v" = pass ]; then printf 'resume — resume recommended (resume.context: always-resume)\n'
        else printf 'resume — %s (resume.context: always-resume read as fresh-when-idle · card-import fixture red: %s)\n' "$rec" "${v#red: }"; fi ;;
    esac
  else
    printf 'card — skipped: resume.context refused: %s\n' "${ctx%%$'\n'*}"
  fi
  if part=$(read_card_policy resume.partial); then
    n=$(git -C "$CARD_TREE" status --porcelain 2>/dev/null | wc -l | tr -d '[:space:]')
    case "$part" in
      continue-item) act="kept, the item continues, its witness still owed" ;;
      restart-item) act="commit the work to partial/$1/${CARD_SID:0:8}, then restore the tree to HEAD" ;;
      ask-owner) act="ask the owner, or park it under a mandate" ;;
    esac
    printf 'partial — %s uncommitted path(s) · resume.partial: %s · %s\n' "${n:-0}" "$part" "$act"
  else
    printf 'card — skipped: resume.partial refused: %s\n' "${part%%$'\n'*}"
  fi
  return 0
}

# The replay's `position —` line (KICK-dKeptSession-15 S1, S2, S4): the build's position as the loop kit's
# engine re-derives it from witnesses, `position.py <slug> --json`, and never the card's stored `item —`
# pointer. The engine is found by `resolve_kit_file` and run in the session's own tree, CARD_TREE, entered
# by a `cd` in the call's subshell, since it takes no root and reads the toplevel of its working directory;
# stdin closed, into a scratch file under CARD_POSITION_BOUND, as `derive_map_block` bounds the map. An exit
# 0, or 2, which the engine answers on `invalid-input` and argparse on a refused command line, is read by
# one `[[ =~ ]]` over the output: `answer` held to the engine's ANSWERS (the loop kit's `position.py#ANSWERS`,
# spelled again here because this kit names no file of another), and `next.item`, anchored on `next` since
# `frontier` and `refusals` rows carry an `item` too, held to [A-Za-z0-9._-]+ and named only for `act`.
# Every failure is one `position — skipped:` line. WHAT THIS DOES NOT CHECK: that the answer is still
# current when the session reads it, or any field of the JSON past those two.
render_position_line() { # slug -> one position — line on stdout; 0 always
  local pos py sf rc out="" ans="" item=none
  local re_ans='"answer": "([a-z-]+)"' re_item='"next": [{]"item": "([A-Za-z0-9._-]+)"'
  [ -n "$1" ] || { printf 'position — skipped: the card routes no build\n'; return 0; }
  pos=$(resolve_kit_file loop position.py)
  [ -n "$pos" ] || { printf 'position — skipped: no loop kit\n'; return 0; }
  py=$(resolve_python 2>/dev/null) || { printf 'position — skipped: no Python resolves on this node\n'; return 0; }
  timeout -k 1 5 true </dev/null >/dev/null 2>&1 \
    || { printf 'position — skipped: this node has no working timeout -k, so the read would be unbounded and none ran\n'; return 0; }
  sf=$(mkdir -p "$CARD_DIR" && mktemp "$CARD_DIR/.position.XXXXXX") \
    || { printf 'position — skipped: no scratch file under %s to capture the answer in\n' "$CARD_DIR"; return 0; }
  (cd "$CARD_TREE" && timeout -k 2 "$CARD_POSITION_BOUND" "$py" "$pos" "$1" --json </dev/null >"$sf" 2>/dev/null); rc=$?
  case "$rc" in 0|2) out=$(<"$sf") ;; esac
  rm -f "$sf" 2>/dev/null
  case "$rc" in 124|137) printf 'position — skipped: position.py did not answer within %ss\n' "$CARD_POSITION_BOUND"; return 0 ;; esac
  [[ $out =~ $re_ans ]] && ans=${BASH_REMATCH[1]}
  case "$ans" in act|awaiting|blocked|terminal|stuck|invalid-input|stale-remote) ;; *) ans="" ;; esac
  if [ "$ans" = act ]; then
    if [[ $out =~ $re_item ]]; then item=${BASH_REMATCH[1]}; else ans=""; fi
  fi
  [ -n "$ans" ] || { printf 'position — skipped: position.py printed no answer this replay reads\n'; return 0; }
  printf 'position — %s · next %s\n' "$ans" "$item"
}

# The replay's `lead —` notice (KICK-dKeptSession-15 S3), after a compaction alone: the payload's `source`,
# which `read_session_id` keeps in CARD_SOURCE, reads `compact`. A resume restores the transcript and
# carries no summary, and a replay run with `--session` or stdin closed reads no payload, so neither prints it.
render_lead_notice() { # -> the lead — line on stdout after a compaction, else nothing; 0 always
  [ "$CARD_SOURCE" = compact ] || return 0
  printf '%s\n' "lead — the compaction summary is a lead, never a source: check it against the position above and the card's pointers"
}

# The `context —` line (KICK-dKeptSession-14 S3, S4): how full the owner session's window is, the runlog
# kit's `runlog.py context <transcript>` over CARD_TRANSCRIPT, the payload's `transcript_path` at a replay
# and the boundary verb's `--transcript`, found by `resolve_kit_file` and run as `derive_map_block` runs the
# map: under CARD_CONTEXT_BOUND, stdin closed, into a scratch file under the card dir. Its answer is held
# to `<digits>%` or `none` before any comparison. `context.on-full` decides the line and, under
# `fresh-at-boundary` alone, `context.threshold`, each read once per verb by `read_card_policy`. At a
# replay every outcome is one line, a failure `context — skipped: <why>`. At a boundary, `boundary`, the
# one line is the fresh-now line at or past the threshold; anything else, a skip or a refusal included,
# prints nothing, since a line at every boundary that changes no act teaches the session to skip it, and
# under `compact-with-card` nothing is measured. WHAT THIS DOES NOT CHECK: that the window is the model's
# real one, since the runlog kit derives it, CLAUDE_CODE_MAX_CONTEXT_TOKENS where set, else the node's
# observed usage rounded up to a rung, and nothing checks either; or that the session acts on the line.
render_context_line() { # [boundary] -> one context — line on stdout at a replay; at a boundary the fresh-now line or nothing; 0 always
  local at=${1:-replay} mode thr="" t rl py sf rc out="" n="" why=""
  if ! mode=$(read_card_policy context.on-full); then
    [ "$at" = boundary ] || printf 'context — skipped: context.on-full refused: %s\n' "${mode%%$'\n'*}"
    return 0
  fi
  [ "$at" != boundary ] || [ "$mode" = fresh-at-boundary ] || return 0
  if [ "$mode" = fresh-at-boundary ] && ! thr=$(read_card_policy context.threshold); then
    [ "$at" = boundary ] || printf 'context — skipped: context.threshold refused: %s\n' "${thr%%$'\n'*}"
    return 0
  fi
  if [ -z "$CARD_TRANSCRIPT" ]; then why='no transcript path names the session'
  elif [ ! -f "$CARD_TRANSCRIPT" ]; then why='the transcript path names no file'
  elif rl=$(resolve_kit_file runlog runlog.py); [ -z "$rl" ]; then why='no runlog kit'
  elif ! py=$(resolve_python 2>/dev/null); then why='no Python resolves on this node'
  elif ! timeout -k 1 5 true </dev/null >/dev/null 2>&1; then
    why='this node has no working timeout -k, so the read would be unbounded and none ran'
  elif ! sf=$(mkdir -p "$CARD_DIR" && mktemp "$CARD_DIR/.context.XXXXXX"); then
    why="no scratch file under $CARD_DIR to capture the share in"
  else
    timeout -k 2 "$CARD_CONTEXT_BOUND" "$py" "$rl" context "$CARD_TRANSCRIPT" </dev/null >"$sf" 2>&1; rc=$?
    case "$rc" in
      0) out=$(LC_ALL=C awk '{ sub(/\r$/, "") } /^([0-9]+%|none)$/ { a = $0 } END { print a }' "$sf")
         case "$out" in
           none) why='no main usage in the transcript' ;;
           "") why='runlog.py printed no share this replay reads' ;;
           *) n=${out%\%} ;;
         esac ;;
      124|137) why="runlog.py did not answer within ${CARD_CONTEXT_BOUND}s" ;;
      *) why=$(LC_ALL=C awk -v rc="$rc" '{ sub(/\r$/, "") }
           NF && f == "" { f = $0 }
           END { if (f == "") f = "runlog.py context exited " rc " and printed nothing"
                 if (length(f) > 160) { f = substr(f, 1, 160); sub(/[\200-\377]+$/, "", f) }
                 print f }' "$sf") ;;
    esac
    rm -f "$sf" 2>/dev/null
  fi
  if [ -n "$why" ]; then
    [ "$at" = boundary ] || printf 'context — skipped: %s\n' "$why"
    return 0
  fi
  t=${thr%\%}
  case "$at:$mode" in
    boundary:*)
      [ "$n" -lt "$t" ] \
        || printf 'context — %s%% of window · past %s · fresh now, at this item boundary (context.on-full: fresh-at-boundary)\n' "$n" "$thr" ;;
    *:compact-with-card) printf 'context — %s%% of window (context.on-full: compact-with-card)\n' "$n" ;;
    *)
      if [ "$n" -ge "$t" ]; then
        printf 'context — %s%% of window · past %s · fresh at next item boundary (context.on-full: fresh-at-boundary)\n' "$n" "$thr"
      else
        printf 'context — %s%% of window · under %s\n' "$n" "$thr"
      fi ;;
  esac
  return 0
}

# S3's act, the boundary verb's step after a crossing: the fresh-now line, written with the verb's other
# lines to its `--out` file, which the hook hands the session at its next shell call.
run_context_boundary() { # -> the fresh-now line or nothing on stdout; 0 always
  render_context_line boundary
}

if [ -n "$CARD" ]; then
  case "$CARD_VERB" in
    replay|publish|follow|lookup|pointers|boundary)
      CARD_TMP=$(mktemp -d "${TMPDIR:-/tmp}/mfcard.XXXXXX") || { echo "MANIFEST env ERROR — cannot create a scratch dir under ${TMPDIR:-/tmp}"; exit 2; }
      trap 'rm -rf "$CARD_TMP"' EXIT ;;
  esac
  case "$CARD_VERB" in
    write)  write_card write; write_card_file ;;
    replay) print_replay; write_card_file ;;
    append|check)
      CARD_TMP=$(mktemp -d "${TMPDIR:-/tmp}/mfcard.XXXXXX") || { echo "MANIFEST env ERROR — cannot create a scratch dir under ${TMPDIR:-/tmp}"; exit 2; }
      trap 'rm -rf "$CARD_TMP"' EXIT
      if [ "$CARD_VERB" = append ]; then
        add_card_body; write_card_file
        # The publish at READY (S3): a body landing a real READY line and a route publishes its build's card.
        if [ "$CARD_APPEND_READY" = 1 ] && [ "$CARD_ROUTE" = 1 ] && _b=$(read_card_build "$CARD_TMP/body") && [ -n "$_b" ]; then
          write_card_publish "$_b" append
        fi
      else check_card; fi ;;
    publish)
      [ -f "$CARD_FILE" ] || { echo "MANIFEST env ERROR — no card for session $CARD_SID at $CARD_FILE, so there is no card to publish"; exit 2; }
      write_card_publish "$CARD_BUILD" publish ;;
    follow) write_card_follow "$CARD_BUILD" "$CARD_STEP" "$CARD_TERMINAL" ;;
    lookup) resolve_build_card "$CARD_BUILD"; write_card_file ;;
    # S4: the build card in `stored` mode, its section fresh; with a named session, that card's too.
    pointers)
      [ -z "$CARD_SID_GIVEN" ] || [ -f "$CARD_FILE" ] \
        || { echo "MANIFEST env ERROR — no card for session $CARD_SID at $CARD_FILE, so there is no card to write the pointers into"; exit 2; }
      write_build_card "$CARD_BUILD" "" stored pointers 0 0
      [ -z "$CARD_SID_GIVEN" ] || write_card_pointers "$CARD_BUILD" ;;
    # S6: every line to stdout, or with `--out` to that file through a temp beside it and a rename.
    boundary)
      if [ -z "$CARD_OUT" ]; then run_card_boundary "$CARD_BUILD"; exit $?; fi
      _bt=$(mktemp "$CARD_OUT.XXXXXX" 2>/dev/null) || { echo "MANIFEST env ERROR — no temp beside $CARD_OUT, so nothing ran"; exit 2; }
      run_card_boundary "$CARD_BUILD" > "$_bt" 2>&1; _brc=$?
      mv -f "$_bt" "$CARD_OUT" 2>/dev/null || { rm -f "$_bt"; echo "MANIFEST env ERROR — cannot rename the verb's lines into $CARD_OUT"; exit 2; }
      exit "$_brc" ;;
  esac
  exit 0
fi

# The message is BUILT from the same array the loop walks, so it can never again describe a different
# list than the one that was searched.
[ -n "$MF" ] && [ -f "$MF" ] || {
  echo "MANIFEST env ERROR — no kickoff manifest at $(printf '%s, ' $MANIFEST_LOCATIONS | sed 's/, $//') (and no valid path argument). Move an existing manifest to the first of those, or run this script with --locations to see the list."
  exit 2
}

# Unmanaged manifest (no kickoff-manifest marker, e.g. a prototype) — not ratchet-managed.
# An UNREADABLE manifest is an env error, never a green.
grep -q 'kickoff-manifest:' "$MF"
case $? in
  0) ;;
  1) echo "NOTE: $MF carries no kickoff-manifest marker — not ratchet-managed; skipping all checks."; exit 0 ;;
  *) echo "MANIFEST env ERROR — cannot read $MF"; exit 2 ;;
esac

# THE STAGED LEG'S EARLY EXIT (KICK-aTrimmedHook-1). Every check the staged leg runs reads the manifest
# itself, a watched path or a verify-path, so a commit that stages none of the three cannot move one
# of them; the pre-commit hook runs this leg on EVERY commit, and it used to pay the whole leg for
# that answer. `git diff --cached` lists deletions too, so a staged deletion of a watched file or a
# verify-path still runs the leg. A block that does not parse, an empty list, or a git that cannot
# answer falls through to the leg below, which reports it. The push boundary runs the full leg.
# WHAT IT DOES NOT CHECK: a manifest already broken at HEAD no longer reds a commit staging none of
# the three — that is the full leg's finding, at the push boundary.
if [ "$STAGED" = 1 ]; then
  BLOCK=$(read_block "$MF")
  getval 'watch' _ew; getval 'verify-paths' _ev
  _el=()
  if [ -n "$_ew" ] && [ -n "$_ev" ]; then
    IFS=';' read -ra _ep <<<"$_ew;$_ev"
    for _es in "${_ep[@]}"; do
      _es=${_es#"${_es%%[![:space:]]*}"}; _es=${_es%"${_es##*[![:space:]]}"}
      [ -n "$_es" ] && _el+=("$_es")
    done
  fi
  if [ "${#_el[@]}" -gt 0 ] && _ed=$(git diff --cached --name-only -- "$MF" "${_el[@]}" 2>/dev/null) && [ -z "$_ed" ]; then
    echo "NOTE: staged leg skipped — nothing staged touches the manifest, its watch list or its verify-paths; the full leg runs at the push boundary."
    exit 0
  fi
fi

# Forward-drift signal: manifest format older than this kit copy (no sort -V — BSD/busybox safe).
ver_older() { awk -v a="$1" -v b="$2" 'BEGIN{na=split(a,x,".");nb=split(b,y,".");n=(na>nb?na:nb);for(i=1;i<=n;i++){d=(x[i]+0)-(y[i]+0);if(d<0){print "y";exit}if(d>0)exit}}'; }
mver=$(sed -n 's/.*kickoff-manifest: v\([0-9][0-9.]*\).*/\1/p' "$MF" | head -1); mver=${mver%.}
if [ -n "$mver" ] && [ "$(ver_older "$mver" "$MANIFEST_FORMAT")" = "y" ]; then
  echo "WARN: manifest format v$mver < kit format v$MANIFEST_FORMAT — see the upgrade recipe in coding-governance/WIRE-INTO-PROJECT.md §4."
fi

status=0
fail() { echo "MANIFEST check $1 FAILED — $2"; status=1; }

# LIFTED VERBATIM from <prefix>/unattended/check-unattended.sh, and gated as an inline copy by the
# parity table in resolve-python.test.sh, in gov's lib dir. Do not re-type it:
# it carries two fixes that were each reproduced before they were written. A marker line IS the marker
# or it is malformed — the prefix test IDENTIFIES the line and equality JUDGES it, because the older
# form let a run append its own text to a marker line and still compare byte-equal. And the pair must
# be exactly one open, one close, CLOSE AFTER OPEN: a transposed pair satisfies a count-only check and
# once truncated a file. CR-normalised before comparing, because the prefix test tolerated a CRLF
# worktree by accident and an equality test does not.
# >>> kickoff_region
region()   { awk -v o="$2" -v c="$3" '
               { ln=$0; sub(/\r$/,"",ln) }
               index(ln,o)==1 { if (ln!=o) bad=1; no++; if (no==1) oat=NR; if (nc==0) inside=1; next }
               index(ln,c)==1 { if (ln!=c) bad=1; nc++; if (nc==1) cat=NR; inside=0; next }
               inside { print }
               END { if (bad || no!=1 || nc!=1 || cat<oat) exit 3 }' "$1"; }
# <<< kickoff_region

# The block's last-audit VALUE from a manifest body on stdin (block-scoped: body decoys don't count).
blockstamp() {
  awk '/<!-- manifest-audit/{f=1;next} f&&/-->/{exit} f' | tr -d '\r' \
    | sed -n 's/^[[:space:]]*last-audit:[[:space:]]*\(.*\)$/\1/p' | head -1 | sed 's/[[:space:]]*$//'
}

# C1 — no placeholder survives (placeholder SHAPE only: gate fences legitimately hold ${{ ... }},
# Go-template {{.Field}}, Helm {{ .Values }} — none of which match '{{' + uppercase).
c1=$(grep -nE '\{\{[A-Z]' "$MF" || true)
[ -n "$c1" ] && fail 1 "unfilled {{PLACEHOLDER}} survives in $MF (fill or delete each):
$(printf '%s\n' "$c1" | sed 's/^/  /')"

# THE SWITCH OVER CHECKS 7, 8 AND 11 (TOOL-dGroundRules-9). Each cap is a row of the policy kit's cap
# census: `manifest-bytes`, `manifest-line` and `manifest-trap`. ONE python start asks all three,
# handing in this file's constants as `default:`, and the answers replace them, so a `budgets.<cap>`
# in .governance/policy.toml takes a constant's place. A breach under `warn` prints a `BUDGET WARN` line
# and passes; under `refuse`, or with the cap pinned, it is the check as before, naming the rule. The
# policy kit is found as every sibling this kit reads is, by `resolve_kit_file`. No kit, or a refusal,
# keeps every constant and refuses as before, and says so once, at the first breach. The orientation
# card's cap, CARD_CAP_BYTES, is a consumer's limit outside the switch and reads none of this.
MAX_MANIFEST_BYTES=${MAX_MANIFEST_BYTES:-25600}
MANIFEST_LINE_MAX=400   # check 8's per-line cap
MANIFEST_TRAP_MAX=400   # check 11's per-bullet cap, which reuses check 8's figure
MB_ANSWERS="" MB_NOTE=""
_mb_py=$(resolve_python 2>/dev/null) || _mb_py=""
_mb_pk=$(resolve_kit_file policy budgets.py)
# The last rung searches by NAME, so a repository's own `budgets.py` would answer it: the policy kit
# is the one whose directory also holds its census and its catalogue, and anything else is no kit.
case "$_mb_pk" in */budgets.py) [ -f "${_mb_pk%/*}/caps.toml" ] && [ -f "${_mb_pk%/*}/catalogue.toml" ] || _mb_pk="" ;; esac
if [ -z "$_mb_py" ] && [ -n "$_mb_pk" ]; then  # the no-kit branch, said as what it is (TOOL-dGroundRules-21 S31)
  MB_NOTE="MANIFEST — no python launcher resolved to run the policy kit, so a size breach refuses as before"
elif [ -z "$_mb_py" ] || [ -z "$_mb_pk" ]; then
  MB_NOTE="MANIFEST — no policy kit is installed beside this checker, so a size breach refuses as before"
elif _mb_out=$("$_mb_py" "$_mb_pk" resolve --explain "manifest-bytes=default:$MAX_MANIFEST_BYTES" \
    "manifest-line=default:$MANIFEST_LINE_MAX" "manifest-trap=default:$MANIFEST_TRAP_MAX" 2>&1); then
  MB_ANSWERS=$_mb_out
else
  MB_NOTE="MANIFEST — the policy reader refused, so a size breach refuses as before: $(printf '%s\n' "$_mb_out" | grep -v '^budgets: ' | head -n 1)"
fi
read_budget_field() { printf '%s\n' "$MB_ANSWERS" | awk -F'\t' -v c="$1" -v k="$2" '$1 == c { print $k }'; }
read_budget_rule() { printf '%s\n' "$MB_ANSWERS" | awk -F' · ' -v c="budgets: $1" '$1 == c { print $2 }'; }
# The three values from ONE builtin split of the answer, never a substitution per cap (TOOL-dGroundRules-85).
_mb_ifs=$IFS; IFS=$'\n'; set -f
for _l in $MB_ANSWERS; do
  case "$_l" in *$'\t'*) ;; *) continue ;; esac
  _v=${_l#*$'\t'}; _v=${_v%%$'\t'*}
  case "$_v" in ''|*[!0-9]*) continue ;; esac
  case "${_l%%$'\t'*}" in
    manifest-bytes) MAX_MANIFEST_BYTES=$_v ;;
    manifest-line) MANIFEST_LINE_MAX=$_v ;;
    manifest-trap) MANIFEST_TRAP_MAX=$_v ;;
  esac
done
set +f; IFS=$_mb_ifs
# check_budget_breach <cap> <measured> <unit> <value> <subject> — 0 when the breach WARNS, having printed its
# line; 1 when it refuses, the caller's check then failing as before.
check_budget_breach() {
  if [ "$(read_budget_field "$1" 3)" = warn ]; then
    printf 'BUDGET WARN — %s · %s · %s %s over %s · %s\n' "$1" "$5" "$2" "$3" "$4" "$(read_budget_rule "$1")"
    # The runner's marker on the next line (TOOL-dWitnessedBar-29 S2), so a passing bar shows it.
    printf 'gate-warn\tsize\t%s\t%s · %s %s over %s\n' "${5//[$'\t\r\n']/ }" "$1" "$2" "$3" "$4"
    return 0
  fi
  [ -z "$MB_NOTE" ] || { echo "$MB_NOTE"; MB_NOTE=""; }
  return 1
}

# C7 — SIZE. LF-NORMALISED bytes, because the manifest is not eol-pinned in every adopting tree and
# an unnormalised count answers differently per platform — the split that already cost this repo a
# blocked push on the memory-tree byte caps. `check-template-size.sh` is the in-repo precedent and
# measures the same way. The env override exists so the self-test can drive the limit without writing
# a 25 KiB fixture on every run; it is NOT an adopter escape hatch, and the message says so.
c7bytes=$(tr -d '\r' < "$MF" | wc -c | tr -d '[:space:]')
if [ "$MAX_MANIFEST_BYTES" -gt 0 ] && [ "$c7bytes" -gt "$MAX_MANIFEST_BYTES" ] && ! check_budget_breach manifest-bytes "$c7bytes" bytes "$MAX_MANIFEST_BYTES" "$MF"; then
  c7over=$((c7bytes - MAX_MANIFEST_BYTES))
  _r=$(read_budget_rule manifest-bytes)
  fail 7 "the manifest is over its size limit and must be trimmed, not have the limit raised: $c7bytes bytes, $c7over over the $MAX_MANIFEST_BYTES-byte limit in $MF${_r:+ ($_r)}"
fi

# C8 — LINE LENGTH, in BYTES. awk's length() counts bytes on this platform, and portable character
# counting across busybox, mawk and BSD awk does not exist — so the limit is bytes and the message
# says bytes rather than claiming characters it does not measure.
#
# Two regions are exempt. The audit block is machine-maintained data with no prose to wrap: its watch
# list is one line that grows as pathspecs are added. Fenced blocks hold commands that cannot be
# wrapped without breaking them. NOTHING else is exempt — a table row or a body bullet over the limit
# is prose someone wrote, which is exactly what this check is for.
c8=$(awk -v cap="$MANIFEST_LINE_MAX" '
  { ln=$0; sub(/\r$/,"",ln) }
  index(ln,"<!-- manifest-audit")==1 { inblk=1; next }
  inblk && ln ~ /-->/ { inblk=0; next }
  inblk { next }
  ln ~ /^[[:space:]]*(```|~~~)/ { fence=!fence; next }
  fence { next }
  cap+0 > 0 && length(ln) > cap+0 { printf "  line %d: %d bytes\n", NR, length(ln); if (length(ln) > m) m = length(ln) }
  END { if (m) printf "%d\n", m }
' "$MF")
# The awk's last line is the longest offender's length, the switch's measure, and never a finding.
c8max=${c8##*$'\n'}; c8=${c8%"$c8max"}; c8=${c8%$'\n'}
if [ -n "$c8" ] && ! check_budget_breach manifest-line "$c8max" bytes "$MANIFEST_LINE_MAX" "$MF"; then
  _r=$(read_budget_rule manifest-line)
  fail 8 "a manifest line is over the $MANIFEST_LINE_MAX-byte limit; wrap the prose or move the detail out${_r:+ ($_r)}:
$c8"
fi

# C2 — exactly one manifest-audit block, four keys with non-empty, well-formed values.
# The stamp rule's single MACHINE home. TOOL-aHonedRuleset-5 hoisted it above RETROFIT so that
# string can interpolate it instead of re-typing it, and the playbook-parity gate compares
# this expression against the one MANIFEST-TEMPLATE.md states, so the two cannot drift apart again.
STAMP_SHA_RULE="sha = HEAD on any branch"
RETROFIT="retrofit: (1) body deltas — rewrite the §B intro to 're-audited every kickoff; accretes', add the ratchet + dated-corrections (never delete the section) + traps-accrete text; (2) add the manifest-audit block: last-audit '<ISO datetime> @ <full sha>' (sha = HEAD on the default branch, else \$(git merge-base <remote>/<default> HEAD)), watch = gate-defining pathspecs, verify-paths = 2-3 anchors, last-body-change = the sha where the BODY was last revised; (2b) paste the sealed task region from --task-skeleton into §A; (3) copy manifest-check.sh in, add the .gitattributes LF rule + the gate-fence line, git add everything; (4) run this check to 0; (5) re-render the project's charter — since charter v4.0 it carries no manifest lines, and the ratchet leg's refusals name the write-back and the merge re-stamp; (5b) add registry = the file whose first table under '## Node registry' names this node, which the card verbs read; (6) bump the marker to v$MANIFEST_FORMAT LAST. Full recipe: coding-governance/WIRE-INTO-PROJECT.md §4."
nblocks=$(grep -c '<!-- manifest-audit' "$MF" || true)
BLOCK_OK=1
if [ "$nblocks" -eq 0 ]; then
  fail 2 "no manifest-audit block in $MF — $RETROFIT"
  BLOCK_OK=0
elif [ "$nblocks" -gt 1 ]; then
  fail 2 "$nblocks manifest-audit blocks in $MF — exactly one is allowed; merge them."
  BLOCK_OK=0
fi

LA=""; WATCH_RAW=""; VP_RAW=""
if [ "$BLOCK_OK" = 1 ]; then
  BLOCK=$(read_block "$MF")
  getval 'last-audit' LA; getval 'watch' WATCH_RAW; getval 'verify-paths' VP_RAW
  getval 'last-body-change' LBC
  [ -n "$LA" ] || { fail 2 "manifest-audit block lacks a last-audit value — stamp '<ISO datetime> @ <full sha>' after verifying §B."; BLOCK_OK=0; }
  # The C9 baseline. It is RECORDED rather than derived, because deriving it means walking the
  # manifest's own path history, and a path-scoped `git log --name-status` reports a `git mv` as an
  # ADD, not a rename — so a relocated manifest read as freshly created and a stalled one reported
  # itself maintained. Reproduced at git 2.55 before this key existed.
  [ -n "$LBC" ] || { fail 2 "manifest-audit block lacks a last-body-change value — add the full sha of the commit where this manifest's BODY was last genuinely revised; it is what check 9 measures the stall against."; BLOCK_OK=0; }
  [ -n "$WATCH_RAW" ] || { fail 2 "manifest-audit block lacks a watch value — list the gate-defining pathspecs (a missing watch silently disables the drift check)."; BLOCK_OK=0; }
  [ -n "$VP_RAW" ] || { fail 2 "manifest-audit block lacks a verify-paths value — list the 2-3 anchor paths."; BLOCK_OK=0; }
fi

# ;-split, trimming, EMPTY ELEMENTS DROPPED (a stray ';' must never reach git as '' — fatal 128).
splitspecs() { printf '%s\n' "$1" | tr ';' '\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | grep -v '^$' || true; }

WATCH=(); VPATHS=(); LA_SHA=""
if [ "$BLOCK_OK" = 1 ]; then
  while IFS= read -r _s; do WATCH+=("$_s"); done < <(splitspecs "$WATCH_RAW")
  while IFS= read -r _s; do VPATHS+=("$_s"); done < <(splitspecs "$VP_RAW")
  [ "${#WATCH[@]}" -gt 0 ] || { fail 2 "watch: holds no usable pathspec after splitting — list the gate-defining pathspecs (a missing watch silently disables the drift check)."; BLOCK_OK=0; }
  [ "${#VPATHS[@]}" -gt 0 ] || { fail 2 "verify-paths: holds no usable path after splitting — list the 2-3 anchor paths."; BLOCK_OK=0; }
  if [ "$BLOCK_OK" = 1 ]; then
    if ! printf '%s' "$LA" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?([+-][0-9]{2}:?[0-9]{2}|Z)[[:space:]]*@[[:space:]]*[0-9a-fA-F]{40}$'; then
      fail 2 "last-audit value malformed ('$LA') — want '<ISO-8601 datetime with offset> @ <full 40-hex sha>'."
      BLOCK_OK=0
    else
      LA_SHA=$(printf '%s' "$LA" | sed -n 's/.*@[[:space:]]*\([0-9a-fA-F]\{40\}\)[[:space:]]*$/\1/p')
    fi
  fi
fi

if [ "$BLOCK_OK" = 1 ]; then
  # C6 — watch list is alive (a dead pathspec is a silent permanent false-green on the drift check).
  # ONE listing for the whole watch list (KICK-aTrimmedHook-1), each LITERAL pathspec counted from it:
  # git matches a literal as the path itself or anything under `<spec>/`, which is the case below. A
  # spec carrying glob magic, and any literal counted zero, is asked of git on its own, so a dead
  # verdict is always git's — a case-folding filesystem cannot turn a byte compare into a red.
  # `core.quotePath=false` prints a non-ASCII name as itself, so it compares as itself; a name git still
  # quotes (a quote, a backslash, a control byte) sends every count back to git (TOOL-aTrimmedHook-7).
  _c6all=$(git -c core.quotePath=false ls-files -- "${WATCH[@]}" 2>/dev/null)
  _c6q=""
  case "$_c6all" in \"*|*$'\n'\"*) _c6q=1 ;; esac
  for w in "${WATCH[@]}"; do
    n=0
    case "$w" in
      *'*'*|*'?'*|*'['*|:*) ;;
      # Split on newlines with globbing off, not a loop fed by a here-string of a substitution's value,
      # which the shell-hygiene leg refuses; no line of a git listing is empty.
      *) _c6ifs=$IFS; IFS=$'\n'; set -f
         for _c6f in $_c6all; do
           case "$_c6f" in "$w"|"${w%/}"/*) n=$((n+1)) ;; esac
         done
         set +f; IFS=$_c6ifs ;;
    esac
    # A literal the listing counted zero, or any name git quoted, is asked of git alone, its lines
    # counted by expansion, not by `wc -l` and `tr` (TOOL-dGroundRules-85).
    if [ "$n" -eq 0 ] || [ -n "$_c6q" ]; then
      _c6one=$(git ls-files -- "$w" 2>/dev/null); _c6nl=${_c6one//[!$'\n']/}
      n=0; [ -z "$_c6one" ] || n=$(( ${#_c6nl} + 1 ))
    fi
    if [ "$n" -eq 0 ]; then
      fail 6 "watch pathspec '$w' matches no tracked file — update the watch list to the restructured paths."
    elif [ "$n" -gt 100 ]; then
      echo "WARN: watch pathspec '$w' matches $n tracked files — overly broad; narrow it to the gate-defining slice."
    fi
  done

  # C4 — every verify-path anchors TRACKED content (an untracked leftover must not green the local
  # leg while fresh-clone CI reds).
  for vp in "${VPATHS[@]}"; do
    vp="${vp%/}"
    if git ls-files --error-unmatch -- "$vp" >/dev/null 2>&1; then :
    elif git ls-files -- "$vp/" 2>/dev/null | grep -q .; then :
    else
      fail 4 "verify-path '$vp' is not tracked content — the tree restructured or the anchor is dead; fix the path (or the §B pointer it anchors)."
    fi
  done

  if [ "$STAGED" = 0 ]; then
    SKIP_RANGE=0
    # C3 — anchor sha is real and ours.
    if ! git rev-parse -q --verify 'HEAD^{commit}' >/dev/null 2>&1; then
      fail 3 "HEAD has no commits on this branch — make the first commit, then re-verify §B and re-stamp last-audit at it."
      SKIP_RANGE=1
    elif ! git cat-file -e "$LA_SHA^{commit}" 2>/dev/null; then
      if [ "$(git rev-parse --is-shallow-repository 2>/dev/null)" = "true" ]; then
        echo "WARN: shallow clone and the last-audit sha is absent — skipping C3+C5; set 'fetch-depth: 0' on the CI checkout step so the drift check actually enforces."
        SKIP_RANGE=1
      else
        fail 3 "last-audit sha $LA_SHA is unknown to this repo — the stamp is foreign or predates a history rewrite; re-verify §B, then re-stamp last-audit '<ISO datetime> @ <sha>' with $STAMP_SHA_RULE."
        SKIP_RANGE=1
      fi
    elif ! git merge-base --is-ancestor "$LA_SHA" HEAD 2>/dev/null; then
      fail 3 "last-audit sha $LA_SHA is not an ancestor of HEAD — history was rewritten or the stamp was squash-merged; re-verify §B, then re-stamp last-audit '<ISO datetime> @ <sha>' with $STAMP_SHA_RULE."
      SKIP_RANGE=1
    fi

    # C5 — no unaudited drift (TOPOLOGICAL + STRUCTURAL): the newest watch-touching commit W must be
    # an ancestor of (or equal to) the newest commit S that actually CHANGED the audit block's
    # last-audit VALUE. Candidates come from a pathspec-FREE -G search (with the rename source in the
    # diff, git's rename detection collapses a pure `git mv` of the manifest, which a pathspec-scoped
    # search would mistake for a stamp); each candidate is then validated by comparing the block's
    # stamp value at the commit vs its parent, so body decoy lines and block reorders never count.
    # Residual (documented): a decoy edit in a commit predating the manifest's current path is
    # accepted unvalidated — narrow, and it fails toward green only when combined with a later rename.
    if [ "$SKIP_RANGE" = 0 ]; then
      W=$(git rev-list -1 "$LA_SHA..HEAD" -- "${WATCH[@]}" 2>/dev/null)
      if [ -n "$W" ]; then
        S=""
        while IFS= read -r cand; do
          [ -n "$cand" ] || continue
          cur=$(git show "$cand:$MF" 2>/dev/null | blockstamp)
          prev=$(git show "$cand^:$MF" 2>/dev/null | blockstamp)
          if [ -z "$cur" ] || [ -z "$prev" ] || [ "$cur" != "$prev" ]; then S="$cand"; break; fi
        done < <(git log --format=%H -G'^last-audit:' "$LA_SHA..HEAD" 2>/dev/null)
        if [ -z "$S" ] || ! git merge-base --is-ancestor "$W" "$S" 2>/dev/null; then
          files=$(git diff --name-only "$LA_SHA..HEAD" -- "${WATCH[@]}" 2>/dev/null | sed 's/^/  /')
          fail 5 "watched files changed since last-audit with no re-stamp at/after the change:
$files
  For each file, re-check the §B claims derived from it, update the manifest where stale, then
  re-stamp last-audit ($STAMP_SHA_RULE) — bundled with the watched change or as a follow-up in the
  same PR. After a merge that brought in watch-touching commits, the fresh post-merge audit +
  re-stamp is the close."
        fi
      fi
    fi

    # C10 and C11 live HERE, not beside C7/C8, and the reason is the adopter upgrade path.
    # WIRE-INTO-PROJECT.md installs the --staged leg as an UNCONDITIONAL pre-commit hook and
    # documents overwriting this checker wholesale on a kit update. Both checks judge the
    # WORKING-TREE manifest's structure rather than what a commit stages, so above the split they
    # would block EVERY commit in a repo whose manifest predates this format — with no migration
    # staged and no way to make progress. C9's own comment already drew this line; these two
    # simply had not been held to it.
    # C10 — THE SEALED TASK REGION. §A's field set is a contract, not guidance, and before this check it
    # was prose: deleting §A entirely left every check green.
    #
    # ABSENCE IS A FAILURE, NOT A SKIP. The prior art this borrows from skips silently when its source is
    # absent, and copying that here would make the seal dormant in exactly the population it exists for —
    # every manifest written before this format version has no region at all. Three distinct messages,
    # one per failure mode, so the remedy is never guessed.
    #
    # The comparison appends a SENTINEL. Command substitution strips trailing newlines, so without it a
    # trailing-blank-line difference inside the region is invisible — the weakness the prior art still
    # carries and `kit-dogfood-parity.test.sh` already defeats this way.
    c10n=$(grep -c '<!-- kickoff:task -->' "$MF" || true)
    if [ "$c10n" -eq 0 ]; then
      fail 10 "the manifest carries no sealed task region, so its §A field set is prose that any edit can silently change; paste the region printed by this script's --task-skeleton verb into §A of $MF"
    elif ! c10have=$(region "$MF" '<!-- kickoff:task -->' '<!-- /kickoff:task -->' 2>/dev/null); then
      fail 10 "the sealed task region's markers are malformed, so the region cannot be compared with the contract it copies; the pair must be exactly one open and one close, close after open, each alone on its line in $MF"
    else
      # The sentinel goes INSIDE each substitution. Appended after, both sides have already had their
      # trailing newlines stripped identically and it defends nothing — which is exactly what it did
      # until the closing review pointed at it, and a trailing blank line inside the region passed.
      c10have=$(region "$MF" '<!-- kickoff:task -->' '<!-- /kickoff:task -->' 2>/dev/null; printf X)
      c10want=$(printf '%s\n' "$TASK_SKELETON" | region /dev/stdin '<!-- kickoff:task -->' '<!-- /kickoff:task -->' 2>/dev/null; printf X)
      # Format 1.4's frozen region passes under a marker older than 1.5, the format that replaced it,
      # and ONLY there: the WARN above already names the upgrade, the NOTE names its first step, and a
      # 1.5 marker demands the region this script carries (KICK-aOrientedCast-1 §8 F2). The 1.5 is
      # literal on purpose — it is when THAT region moved, not whatever MANIFEST_FORMAT says today.
      c10old=$(printf '%s\n' "$TASK_SKELETON_FORMAT_1_4" | region /dev/stdin '<!-- kickoff:task -->' '<!-- /kickoff:task -->' 2>/dev/null; printf X)
      if [ "$c10have" = "$c10want" ]; then
        :
      elif [ "$c10have" = "$c10old" ] && [ -n "$mver" ] && [ "$(ver_older "$mver" 1.5)" = y ]; then
        echo "NOTE: the sealed task region is format 1.4's; re-paste it from --task-skeleton, then bump the marker to v$MANIFEST_FORMAT"
      else
        fail 10 "the sealed task region differs from the task contract this script carries, and that region is not hand-authorable; restore it from the --task-skeleton verb rather than editing it in $MF"
      fi
    fi

    # C11 — PER-BULLET CAP on the environment-traps section. Not a new rule: MANIFEST-TEMPLATE.md has
    # always instructed "keep each to one line; link out for detail". It was ignored until this repo's own
    # traps section reached 14,535 bytes across 27 bullets, 19 of them over the cap. C11 makes the kit's
    # own instruction mechanical, and reuses C8's 400 rather than minting a second number — C8 already
    # defines how long a line may be, and one line is what the template asked for.
    #
    # C7 is not a substitute. It bounds the FILE, so traps can re-accrete to the size limit by crowding
    # out every other section; C11 bounds the ENTRY, which is where accretion actually happens.
    # The awk's last line is the longest offender's length, the switch's measure (TOOL-dGroundRules-9).
    c11=$(awk -v cap="$MANIFEST_TRAP_MAX" '
      function over() { if (n > 0 && cap+0 > 0 && len > cap+0) { printf "  the bullet starting %s is %d bytes\n", head, len; if (len > m) m = len } }
      { ln=$0; sub(/\r$/,"",ln) }
      /^###[[:space:]]+Environment traps/ { intraps=1; next }
      intraps && /^##[^#]/ { intraps=0 }
      intraps && /^###[[:space:]]/ { intraps=0 }
      !intraps { next }
      /^-[[:space:]]/ {
        over()
        n++; len = length(ln) + 1; head = "\"" substr(ln, 3, 40) "…\""; next
      }
      { len += length(ln) + 1 }
      END { over(); if (m) printf "%d\n", m }
    ' "$MF")
    c11max=${c11##*$'\n'}; c11=${c11%"$c11max"}; c11=${c11%$'\n'}
    if [ -n "$c11" ] && ! check_budget_breach manifest-trap "$c11max" bytes "$MANIFEST_TRAP_MAX" "$MF"; then
      _r=$(read_budget_rule manifest-trap)
      fail 11 "an environment-traps bullet is over the $MANIFEST_TRAP_MAX-byte cap; the template asks for one line each with the detail linked out, and a record under the memory tree is where the detail belongs${_r:+ ($_r)}:
    $c11"
    fi

    # C9 — MAINTENANCE STALL. Never in the staged leg: the pre-commit hook runs that leg
    # unconditionally on every commit in an adopting repo, and this question is not one a single
    # commit changes.
    #
    # The baseline is READ, not walked. `aRatchetForge` §10.9 set the thresholds and deliberately left
    # them to an owner review because the delta lines it would have read live in commit messages and
    # READY cards, which squash merges do not preserve. A recorded sha survives a squash, survives a
    # rename, needs no candidate cap and cannot be defeated by a graft boundary on a shallow clone.
    #
    # MERGES ARE EXCLUDED. A merge commit carries no content of its own, so counting it alongside the
    # commits it brings in double-counts the same churn. The prior spec said only "watch-pathspec
    # commits" and that one unstated word decides the verdict: this repo measures 11 counting merges
    # and 6 without, against a threshold of 10.
    if [ -n "$LBC" ]; then
      if ! printf '%s' "$LBC" | grep -qE '^[0-9a-fA-F]{40}$'; then
        fail 9 "last-body-change is not a full 40-hex sha, so the stall check has no baseline to measure from: '$LBC'"
      elif ! git cat-file -e "$LBC^{commit}" 2>/dev/null; then
        if [ "$(git rev-parse --is-shallow-repository 2>/dev/null)" = "true" ]; then
          echo "WARN: shallow clone and the last-body-change sha is absent — skipping C9; set 'fetch-depth: 0' on the CI checkout step."
        else
          fail 9 "last-body-change names a commit unknown to this repository, so the stall baseline is foreign or predates a history rewrite: $LBC"
        fi
      elif ! git merge-base --is-ancestor "$LBC" HEAD 2>/dev/null; then
        fail 9 "last-body-change is not an ancestor of HEAD, so the stall baseline was squash-merged or rewritten and measures nothing: $LBC"
      else
        c9n=$(git rev-list --count --no-merges "$LBC..HEAD" -- "${WATCH[@]}" 2>/dev/null || echo 0)
        c9age=$(( ( $(git log -1 --format=%ct HEAD 2>/dev/null || echo 0) - $(git log -1 --format=%ct "$LBC" 2>/dev/null || echo 0) ) / 86400 ))
        if [ "$c9n" -ge 10 ]; then
          fail 9 "the manifest body has not changed across ten or more watched commits, so its front-loaded claims are drifting unverified; re-read §B and advance last-body-change to a current sha: $c9n non-merge commits since $LBC"
        elif [ "$c9age" -ge 90 ]; then
          fail 9 "the manifest body has not changed in three months or more, so its front-loaded claims are drifting unverified; re-read §B and advance last-body-change to a current sha: $c9age days since $LBC"
        fi
      fi
    fi
  else
    # C5s — staged leg (deliberately narrowed: a blocking pre-commit cannot see a future follow-up
    # commit, so the bundle form is the only green path here). STRUCTURAL: the staged blob's block
    # stamp must differ from HEAD's — co-staging an unrelated manifest edit, or a body decoy line,
    # does not count.
    sw=$(git diff --cached --name-only -- "${WATCH[@]}" 2>/dev/null)
    if [ -n "$sw" ]; then
      staged_stamp=$(git show ":$MF" 2>/dev/null | blockstamp)
      head_stamp=$(git show "HEAD:$MF" 2>/dev/null | blockstamp)
      if [ -z "$staged_stamp" ] || [ "$staged_stamp" = "$head_stamp" ]; then
        fail 5 "staged changes touch watched files:
$(printf '%s\n' "$sw" | sed 's/^/  /')
  but the staged manifest's audit block does not update last-audit. Re-verify the §B claims these
  files feed, update the manifest where stale, and bundle the re-stamp into THIS commit
  ($STAMP_SHA_RULE)."
      fi
    fi
  fi
fi

# ---- 12: the manifest carries no CR byte -------------------------------------------------------
# ROUND 3's M1, and the bullet it protects is the one about CR bytes. Twice the manifest was given a
# sentence carrying a raw CR to SHOW the byte it names, and twice the next tool to rewrite the file
# in text mode ate it -- leaving "turns a lone <LF> into <LF>", a sentence asserting that a newline
# becomes a newline, with the one fact it existed to carry gone and nothing red. The manifest is the
# document most likely to be rewritten by a text-mode tool, which is exactly why it is the one that
# must not depend on a control byte surviving. Name the bytes (0x0D, 0x0A); never embed them.
#
# DERIVED, and it names no bullet: any CR anywhere in this file reds, so the rule outlives the
# sentence that motivated it. Failing case observed before wiring -- a CR inserted into the manifest
# reds this check, removed it passes.
# THE BYTE IS BUILT INSIDE awk, and that is not style. `grep -q "$(printf ...)"` cannot work here:
# MSYS command substitution STRIPS a trailing CR, so the pattern arrives EMPTY and matches every
# line of every file -- the check then reds on a clean manifest, which is how this line was
# written the first time. `sprintf("%c", 13)` needs no shell quoting and no escape, and it
# catches a lone CR mid-line as well as a CRLF ending.
if LC_ALL=C awk 'index($0, sprintf("%c", 13)) { hit = 1 } END { exit !hit }' "$MF" 2>/dev/null; then
  fail 12 "the manifest carries a CR byte (0x0D), and a text-mode rewrite silently converts it --
  which has twice destroyed the one fact a §B bullet existed to carry. Name a control byte by its
  hex value instead of embedding it: $MF"
fi

exit "$status"
