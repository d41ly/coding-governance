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
#   manifest-check.sh --staged [<path>]   # pre-commit fast leg: C1 C2 C4 C6 C7 C8 + C5s.
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
#     The card verbs run NO manifest check: the session id comes from the SessionStart hook's JSON
#     on stdin, else --session (--append: --session alone, stdin is the body); the card lives at
#     <git-common-dir>/orientation/<sid>.md, shared by every worktree; the `node —` cell resolves
#     through the manifest audit block's `registry:` key. The append and the check do NOT judge
#     relevance, scope, tier, or the truth of a claim at the line it cites — existence only.
#
# Exit 0 + no FAILED lines = clean (WARN:/NOTE: lines permitted). Exit 1 = a check failed — for
#          the card verbs: a body or card with nothing to check (DEAD PROBE), a --check miss, or a
#          real READY line with no `## task` beneath it.
# Exit 2 = environment error (not a git repo / no manifest found / path outside the repo / a card
#          verb with no session id, a path-shaped one, a card over its byte cap, an append whose
#          READY line pins a BASE that is not HEAD, or an id reader that could not answer).
set -u
KIT_MANIFEST_VERSION="1.4"   # gov:kit kickoff-manifest@1.4 — the registry id

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
read -r -d '' TASK_SKELETON <<'KICKOFF_TASK_SKELETON' || true
<!-- kickoff:task -->
> - **Title:** …
> - **Goal (1–2 sentences):** …
> - **IN scope:** …
> - **OUT / non-goals** (explicit cut-line): …
> - **Acceptance check** (the observation that proves THIS change — a test it adds, a gate it
>   moves, an observed behavior; *not* an unrelated green check): …
> - **Gates it must pass:** …
<!-- /kickoff:task -->
KICKOFF_TASK_SKELETON

# Both read-only verbs answer BEFORE the repo probe below, because the whole point of `--locations` is
# to be readable from OUTSIDE a repository — and the probe exits 2 there without ever reading argv.
# They print and exit 0, adding no `fail` branch, so the harness meta-gate's shrink-only floor for this
# script counts neither of them.
for _a in "$@"; do
  case "$_a" in
    --locations)     printf '%s\n' $MANIFEST_LOCATIONS; exit 0 ;;
    --task-skeleton) printf '%s\n' "$TASK_SKELETON"; exit 0 ;;
  esac
done

# The card verbs are CONSUMED here, before the manifest loop below, whose catch-all reads any other
# argument as a manifest path. `--card` alone is a refusal, not a default: a verb the caller did not
# name is a card the caller did not ask for. Without `--card`, `--write` and its siblings still fall
# through to that catch-all exactly as they did before this block existed.
CARD=""; CARD_VERB=""; CARD_SID=""; _rest=(); _want_sid=0
for _a in "$@"; do [ "$_a" = --card ] && CARD=1; done
for _a in "$@"; do
  if [ "$_want_sid" = 1 ]; then CARD_SID="$_a"; _want_sid=0; continue; fi
  case "$CARD$_a" in
    1--card) ;;
    1--write|1--replay|1--path|1--append|1--check) CARD_VERB="${_a#--}" ;;
    1--session) _want_sid=1 ;;
    1--session=*) CARD_SID="${_a#--session=}" ;;
    *) _rest+=("$_a") ;;
  esac
done
set -- ${_rest[@]+"${_rest[@]}"}
if [ -n "$CARD" ] && [ -z "$CARD_VERB" ]; then
  echo "MANIFEST env ERROR — --card needs one of --write, --replay, --path, --append or --check"; exit 2
fi

CALLER_PWD=$PWD
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

# The session id, in PRECEDENCE order: `--session` answers FIRST and SUPPRESSES the stdin read;
# only a caller that passed none falls through to the `{"session_id": …}` JSON the SessionStart hook
# hands on stdin. That order is the fix for TOOL-cMendedVintage-9 and supersedes the stdin-first one
# KICK-aReplayedCard-1 §S2 recorded: `[ -t 0 ]` admits a terminal and the hook's closing pipe, and
# not the third case — the never-closing pipe every tool-invoked shell hands its child — on which
# the `sed` below blocks forever, including for a caller that had already answered by flag.
# Neither channel is a refusal naming both, never a card under a guessed id; a separator, `..` or
# any byte outside [A-Za-z0-9._-] is refused before it can be joined into a path. `--append` never
# reads stdin here — stdin is the body it stores — so it takes `--session` alone.
read_session_id() {
  local sid=""
  [ "$CARD_VERB" = append ] || [ -n "$CARD_SID" ] || [ -t 0 ] || sid=$(sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
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

# `--path` answers here, before the manifest resolves: it needs the repository (for the common dir)
# and the id, and nothing else. Print-only, exit 0, no `fail` branch — the `--locations` shape.
if [ -n "$CARD" ]; then
  CARD_DIR=$(cd "$(git rev-parse --git-common-dir 2>/dev/null)" 2>/dev/null && pwd) \
    || { echo "MANIFEST env ERROR — cannot resolve the git common dir, so the card has no home"; exit 2; }
  CARD_DIR="$CARD_DIR/orientation"
  read_session_id
  CARD_FILE="$CARD_DIR/$CARD_SID.md"
  [ "$CARD_VERB" = path ] && { printf '%s\n' "$CARD_FILE"; exit 0; }
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
    froot=$(git -C "$dir" rev-parse --show-toplevel 2>/dev/null) || froot=""
    [ -n "$froot" ] && { froot=$(cd "$froot" 2>/dev/null && pwd) || froot=""; }
  fi
  if [ -z "$froot" ] || [ "$froot" != "$ROOT" ]; then
    echo "MANIFEST env ERROR — '$MF' resolves outside this repository"; exit 2
  fi
  MF="$(git -C "$dir" rev-parse --show-prefix 2>/dev/null)$(basename -- "$abs")"
else
  for p in $MANIFEST_LOCATIONS; do
    [ -f "$p" ] && { MF="$p"; break; }
  done
fi

# The audit block's text, CR-stripped; `getval` reads one key from it. Defined here because the card
# reads the block's `registry:` key before the checks below ever run, and one reader is one reader.
read_block() { awk '/<!-- manifest-audit/{f=1;next} f&&/-->/{exit} f' "$1" | tr -d '\r'; }
getval() { printf '%s\n' "$BLOCK" | sed -n "s/^[[:space:]]*$1:[[:space:]]*\(.*\)$/\1/p" | head -1 | sed 's/[[:space:]]*$//'; }

# The `node —` cell: the FIRST table under a `## Node registry` heading of the file the manifest's
# `registry:` key names, backticks stripped, `$USERNAME` (else `$USER`) matched against the
# Machine/user cell by equality or by the prefix `<user> @` — never row-wide, because the Remote
# column repeats one github user on every row and a row-wide match hits all of them. No unique
# match is UNKNOWN with the reason, printed, never guessed; the card still writes.
derive_node_tag() {
  local reg="$1" user="${USERNAME:-${USER:-}}" hits tag mu
  [ -n "$reg" ] || { printf 'node — UNKNOWN: no registry\n'; return 0; }
  [ -f "$reg" ] || { printf 'node — UNKNOWN: registry %s is not a file in this tree\n' "$reg"; return 0; }
  [ -n "$user" ] || { printf 'node — UNKNOWN: neither USERNAME nor USER names a user\n'; return 0; }
  IFS=$'\t' read -r hits tag mu < <(awk -v user="$user" '
    { ln=$0; sub(/\r$/,"",ln) }
    !intab && ln ~ /^## Node registry/ { sect=1; next }
    sect && !intab && ln ~ /^## / { exit }
    sect && !intab && ln ~ /^\|/ { intab=1 }
    intab && ln !~ /^\|/ { exit }
    !intab { next }
    { gsub(/`/,"",ln); split(ln, c, "|"); tag=c[2]; mu=c[3]
      gsub(/^[ \t]+|[ \t]+$/,"",tag); gsub(/^[ \t]+|[ \t]+$/,"",mu)
      if (tag=="Tag" || tag ~ /^:?-+:?$/) next
      if (mu==user || index(mu, user " @")==1) { hits++; found=tag; foundmu=mu } }
    END { printf "%d\t%s\t%s\n", hits+0, found, foundmu }' "$reg")
  case "$hits" in
    1) printf 'node — %s · %s\n' "$tag" "$mu" ;;
    0) printf 'node — UNKNOWN: no Machine/user cell in %s matches %s\n' "$reg" "$user" ;;
    *) printf 'node — UNKNOWN: %s Machine/user cells in %s match %s\n' "$hits" "$reg" "$user" ;;
  esac
}

# The startup card, rendered from facts a script can derive: no fetch, no ref move, no manifest
# audit — the engine's Step 1 and Step 2b own those and each costs a kickoff, not a session start.
# `$1` names the writer verb the header carries; a card the replay wrote fresh says `--card --replay`,
# which is the one byte-level fact that tells a session started before the writer was wired from one
# whose startup ran it. The `live —` cell reads the memory-tree conf when there is one and reports
# `skipped:` otherwise, because this kit requires no other kit.
derive_head_state() {   # → HEAD_BRANCH HEAD_SHA HEAD_DIRTY, read once by the card and once by the `now —` line
  local n
  HEAD_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null) || HEAD_BRANCH=HEAD
  HEAD_SHA=$(git rev-parse -q --verify 'HEAD^{commit}' 2>/dev/null) || HEAD_SHA=unborn
  n=$(git status --porcelain 2>/dev/null | wc -l | tr -d '[:space:]')
  if [ "$n" -eq 0 ]; then HEAD_DIRTY=clean; else HEAD_DIRTY="dirty $n"; fi
}
render_card() {
  local verb="$1" registry="" memroot live conf
  [ -n "$MF" ] && [ -f "$MF" ] && { BLOCK=$(read_block "$MF"); registry=$(getval 'registry'); }
  derive_head_state
  conf="$ROOT/.memory-tree.conf"
  if [ ! -f "$conf" ]; then
    live='live — skipped: no .memory-tree.conf in this tree'
  else
    memroot=$(sed -n 's/^MEMORY_ROOT=[[:space:]]*//p' "$conf" | head -1 | tr -d '\r"'"'")
    if [ -z "$memroot" ]; then
      live='live — skipped: .memory-tree.conf declares no MEMORY_ROOT'
    elif [ ! -f "$ROOT/$memroot/LIVE.md" ]; then
      live="live — skipped: $memroot/LIVE.md is absent"
    else
      live="live — LIVE.md · $(awk '/^\|/ && !/^\|[-|: ]*$/ {n++} END{print (n>0?n-1:0)}' "$ROOT/$memroot/LIVE.md") non-terminal builds"
    fi
  fi
  printf 'orientation — %s · written %s · by %s --card --%s\n' "$CARD_SID" "$(date +%Y-%m-%dT%H:%M:%S%z)" "${0##*/}" "$verb"
  derive_node_tag "$registry"
  render_tree_cell
  printf 'worktrees — %s\n' "$(git worktree list 2>/dev/null | wc -l | tr -d '[:space:]')"
  printf '%s\n' "$live"
  printf 'recent —\n'
  git log --oneline -5 2>/dev/null
  printf 'READY — none yet\n'
}

# Persist the rendered card and print the same bytes. Rendered to a variable FIRST so an over-cap
# card leaves no file: every startup field is bounded, so an overflow means a derivation went wrong
# and a truncated card would carry that error into every later reader.
write_card() {
  local card bytes
  card=$(render_card "$1")
  bytes=$(printf '%s\n' "$card" | wc -c | tr -d '[:space:]')
  if [ "$bytes" -gt "$CARD_CAP_BYTES" ]; then
    echo "MANIFEST env ERROR — the startup card is $bytes bytes, $((bytes - CARD_CAP_BYTES)) over the $CARD_CAP_BYTES-byte cap (CARD_CAP_BYTES); a bounded derivation overflowed, so nothing was written"
    exit 2
  fi
  mkdir -p "$CARD_DIR" || { echo "MANIFEST env ERROR — cannot create $CARD_DIR"; exit 2; }
  printf '%s\n' "$card" > "$CARD_FILE" || { echo "MANIFEST env ERROR — cannot write $CARD_FILE"; exit 2; }
  printf '%s\n' "$card"
}

# The stored card, unchanged, then ONE `now —` line computed here and never stored — a second replay
# must print one, not two. A missing card is written fresh under the replay's own name in its header.
print_replay() {
  if [ -f "$CARD_FILE" ]; then cat "$CARD_FILE"; else write_card replay; fi
  derive_head_state
  printf 'now — HEAD %s · %s · %s\n' "$HEAD_SHA" "$HEAD_BRANCH" "$HEAD_DIRTY"
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
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
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

# The memory-tree kit's id reader, by the engine's own <MEMORY_TREE_KIT> rule: whichever of
# `tools/memory-tree/` or `memory-tree/` holds it. Empty when neither does; the caller says so.
resolve_id_reader() {
  local d
  for d in tools/memory-tree memory-tree; do
    [ -f "$ROOT/$d/corpus_ids.py" ] && { printf '%s\n' "$ROOT/$d/corpus_ids.py"; return 0; }
  done
  return 0
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
    echo "NOTE: id citations unchecked — no corpus_ids.py under tools/memory-tree/ or memory-tree/ in this tree, so only paths are judged"
  else
    py=$(resolve_python) || { echo "MANIFEST env ERROR — no usable python launcher for the id reader $reader, so the defined-id set is unknown rather than empty; resolve_python's refusal above names every candidate it ran, and GOV_PYTHON=<launcher> is the override"; exit 2; }
    "$py" "$reader" --print-defined-ids > "$CARD_TMP/idout" 2>&1; st=$?
    # Exit 3 is the reader's NAMED degradation — memory-tree installed without memory-recall, so
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
# charter's §16 R1 requires an emitted micro-format to be a markdown list item — `- ` at column 0 —
# so a kickoff body that OBEYS the charter was read here as carrying NO READY line, and the append
# then reported success while leaving the sentinel in place and skipping the `tree —` re-render.
# Both forms are accepted, and that is a WIDENING rather than a swap: the sentinel this script
# renders is bare, as is every card already on disk, and dropping the bare form would strand them.
# The reader moves; §16 R1 does not (TOOL-cMendedVintage-16).
CARD_READY_RE='^\(- \)\{0,1\}READY — '

# `--card --append`: the body on stdin, checked, annotated, and stored — or refused with the file
# byte-identical. Order: the body's READY-line count, the citation check (its refusals come from a
# reader that could not answer), DEAD PROBE on zero tokens, the stale-BASE refusal, the card's own
# shape, the cap. A real-READY body replaces the whole TAIL and re-renders the `tree —` cell; a body
# without one goes in before the TAIL's READY line, so the card always ends with its one READY line.
add_card_body() {
  local body="$CARD_TMP/body" nready ready sha tree bytes l
  [ -f "$CARD_FILE" ] || { echo "MANIFEST env ERROR — no card for session $CARD_SID at $CARD_FILE; write one with --card --write --session $CARD_SID before appending to it"; exit 2; }
  tr -d '\r' > "$body"
  grep -v "${CARD_READY_RE}none yet\$" "$body" > "$body.x"; mv "$body.x" "$body"
  nready=$(grep -c "$CARD_READY_RE" "$body"); nready=${nready:-0}
  [ "$nready" -le 1 ] || { echo "MANIFEST env ERROR — the body carries $nready READY lines; one card holds one kickoff, so exactly one is accepted and nothing was appended"; exit 2; }
  check_card_citations "$body"
  [ "$CARD_TOKENS" -gt 0 ] || { echo "MANIFEST env ERROR — DEAD PROBE: nothing to check — the body carries no path-shaped and no id-shaped token, so nothing was appended"; exit 1; }
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
  awk -F '\t' -v m="$CARD_TMP/misses" 'BEGIN { while ((getline l < m) > 0) { split(l, p, "\t"); a[p[1]] = a[p[1]] p[2] "\n" } }
    { print; if (FNR in a) printf "%s", a[FNR] }' "$body" > "$CARD_TMP/annotated"
  if [ "$nready" = 1 ]; then
    tree=$(render_tree_cell)
    { while IFS= read -r l; do case "$l" in "tree — "*) printf '%s\n' "$tree" ;; *) printf '%s\n' "$l" ;; esac; done < "$CARD_TMP/startup"
      cat "$CARD_TMP/annotated"; } > "$CARD_TMP/new"
  else
    { cat "$CARD_TMP/startup"; grep -v "$CARD_READY_RE" "$CARD_TMP/tail"; cat "$CARD_TMP/annotated"; grep "$CARD_READY_RE" "$CARD_TMP/tail"; } > "$CARD_TMP/new"
  fi
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
  local real
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
  if [ -s "$CARD_TMP/misses" ]; then
    awk -F '\t' '{print $2 " · line " $1}' "$CARD_TMP/misses"
    exit 1
  fi
  exit 0
}

if [ -n "$CARD" ]; then
  case "$CARD_VERB" in
    write)  write_card write ;;
    replay) print_replay ;;
    append|check)
      CARD_TMP=$(mktemp -d "${TMPDIR:-/tmp}/mfcard.XXXXXX") || { echo "MANIFEST env ERROR — cannot create a scratch dir under ${TMPDIR:-/tmp}"; exit 2; }
      trap 'rm -rf "$CARD_TMP"' EXIT
      if [ "$CARD_VERB" = append ]; then add_card_body; else check_card; fi ;;
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

# Forward-drift signal: manifest format older than this kit copy (no sort -V — BSD/busybox safe).
ver_older() { awk -v a="$1" -v b="$2" 'BEGIN{na=split(a,x,".");nb=split(b,y,".");n=(na>nb?na:nb);for(i=1;i<=n;i++){d=(x[i]+0)-(y[i]+0);if(d<0){print "y";exit}if(d>0)exit}}'; }
mver=$(sed -n 's/.*kickoff-manifest: v\([0-9][0-9.]*\).*/\1/p' "$MF" | head -1); mver=${mver%.}
if [ -n "$mver" ] && [ "$(ver_older "$mver" "$KIT_MANIFEST_VERSION")" = "y" ]; then
  echo "WARN: manifest format v$mver < kit v$KIT_MANIFEST_VERSION — see the upgrade recipe in coding-governance/WIRE-INTO-PROJECT.md §4."
fi

status=0
fail() { echo "MANIFEST check $1 FAILED — $2"; status=1; }

# LIFTED VERBATIM from tools/unattended/check-unattended.sh, and gated as an inline copy by the
# parity table in tools/lib/resolve-python.test.sh. Do not re-type it:
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

# C7 — SIZE. LF-NORMALISED bytes, because the manifest is not eol-pinned in every adopting tree and
# an unnormalised count answers differently per platform — the split that already cost this repo a
# blocked push on the memory-tree byte caps. `check-template-size.sh` is the in-repo precedent and
# measures the same way. The env override exists so the self-test can drive the limit without writing
# a 25 KiB fixture on every run; it is NOT an adopter escape hatch, and the message says so.
MAX_MANIFEST_BYTES=${MAX_MANIFEST_BYTES:-25600}
c7bytes=$(tr -d '\r' < "$MF" | wc -c | tr -d '[:space:]')
if [ "$c7bytes" -gt "$MAX_MANIFEST_BYTES" ]; then
  c7over=$((c7bytes - MAX_MANIFEST_BYTES))
  fail 7 "the manifest is over its size limit and must be trimmed, not have the limit raised: $c7bytes bytes, $c7over over the $MAX_MANIFEST_BYTES-byte limit in $MF"
fi

# C8 — LINE LENGTH, in BYTES. awk's length() counts bytes on this platform, and portable character
# counting across busybox, mawk and BSD awk does not exist — so the limit is bytes and the message
# says bytes rather than claiming characters it does not measure.
#
# Two regions are exempt. The audit block is machine-maintained data with no prose to wrap: its watch
# list is one line that grows as pathspecs are added. Fenced blocks hold commands that cannot be
# wrapped without breaking them. NOTHING else is exempt — a table row or a body bullet over the limit
# is prose someone wrote, which is exactly what this check is for.
c8=$(awk '
  { ln=$0; sub(/\r$/,"",ln) }
  index(ln,"<!-- manifest-audit")==1 { inblk=1; next }
  inblk && ln ~ /-->/ { inblk=0; next }
  inblk { next }
  ln ~ /^[[:space:]]*(```|~~~)/ { fence=!fence; next }
  fence { next }
  length(ln) > 400 { printf "  line %d: %d bytes\n", NR, length(ln) }
' "$MF")
[ -n "$c8" ] && fail 8 "a manifest line is over the 400-byte limit; wrap the prose or move the detail out:
$c8"

# C2 — exactly one manifest-audit block, four keys with non-empty, well-formed values.
RETROFIT="retrofit: (1) body deltas — rewrite the §B intro to 're-audited every kickoff; accretes', add the ratchet + dated-corrections (never delete the section) + traps-accrete text; (2) add the manifest-audit block: last-audit '<ISO datetime> @ <full sha>' (sha = HEAD on the default branch, else \$(git merge-base <remote>/<default> HEAD)), watch = gate-defining pathspecs, verify-paths = 2-3 anchors, last-body-change = the sha where the BODY was last revised; (2b) paste the sealed task region from --task-skeleton into §A; (3) copy manifest-check.sh in, add the .gitattributes LF rule + the gate-fence line, git add everything; (4) run this check to 0; (5) pull the manifest DoD + reconcile lines into the project's playbook; (5b) add registry = the file whose first table under '## Node registry' names this node, which the card verbs read; (6) bump the marker to v1.4 LAST. Full recipe: coding-governance/WIRE-INTO-PROJECT.md §4."
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
  LA=$(getval 'last-audit'); WATCH_RAW=$(getval 'watch'); VP_RAW=$(getval 'verify-paths')
  LBC=$(getval 'last-body-change')
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
  for w in "${WATCH[@]}"; do
    n=$(git ls-files -- "$w" 2>/dev/null | wc -l | tr -d '[:space:]')
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

  STAMP_SHA_RULE="sha = HEAD on the default branch, else \$(git merge-base <remote>/<default> HEAD)"
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
      if [ "$c10have" != "$c10want" ]; then
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
    c11=$(awk '
      { ln=$0; sub(/\r$/,"",ln) }
      /^###[[:space:]]+Environment traps/ { intraps=1; next }
      intraps && /^##[^#]/ { intraps=0 }
      intraps && /^###[[:space:]]/ { intraps=0 }
      !intraps { next }
      /^-[[:space:]]/ {
        if (n > 0 && len > 400) printf "  the bullet starting %s is %d bytes\n", head, len
        n++; len = length(ln) + 1; head = "\"" substr(ln, 3, 40) "…\""; next
      }
      { len += length(ln) + 1 }
      END { if (n > 0 && len > 400) printf "  the bullet starting %s is %d bytes\n", head, len }
    ' "$MF")
    [ -n "$c11" ] && fail 11 "an environment-traps bullet is over the 400-byte cap; the template asks for one line each with the detail linked out, and a record under the memory tree is where the detail belongs:
    $c11"

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

exit "$status"
