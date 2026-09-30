#!/usr/bin/env bash
# check-install-prefix.sh — nothing this repo SHIPS may spell a root-install kit path.
#
#   bash <prefix>/check-install-prefix.sh            # assert; exit 1 on an unwaived hit
#   bash <prefix>/check-install-prefix.sh --list     # print every hit, waived or not (authoring aid)
#   bash <prefix>/check-install-prefix.sh --write-ratchet   # (re)write the carried-prefix ratchet
#
# WHY. Kits install at `tools/<kit>/` in a target repo (one segment; the codebase-map gate template
# resolves no deeper). Every ENGINE already derives its own prefix, so what actually strands an
# adopter is a path SPELLED in something they receive: a runbook step, a usage header, a remedy
# string, a rendered artifact. Those fail quietly. Measured before this gate existed: a `tools/`
# install scaffolded the adopter's own committed `HYGIENE.md` with seven kit paths that resolve to
# nothing in their tree, and the hygiene gate exited 0 over it.
#
# WHAT "SHIPS" MEANS, and where this gate grades nothing. A repo ships what its govkit registry
# resolves (TOOL-aRepatriatedFork-16). Installed at a repo that carries no registry — a consumer,
# which ships nothing onward — BOTH arms skip, each printing a SKIP line, and the gate exits 0. It
# does not grade a consumer's own tree or the gov files that consumer received.
#
# THE POPULATION is what a target repo RECEIVES. Tests, selftests and `*.conf.example` are dropped
# from the glob and then added back IF the descriptors say an adopter receives them (S5). They were
# excluded outright until TOOL-cWidenedNet-1, for a reason that was half right: those files BUILD
# root-prefix installs on purpose, to prove the dual-spelling support this repo keeps for its
# not-retrofitted adopters, and gating them wholesale forbids testing the thing that support exists
# for. What the file-level drop also excused was their USAGE HEADERS, and six shipped files were
# telling an adopter to run a path that resolves to nothing in their tree. The fixture exemption is
# now per LINE, which is where the distinction actually lives.
#
# THE PREDICATE matches a kit name followed by a real FILE. A bare `memory-tree/` in prose names the
# kit, not a path anyone runs, and gating it would make every sentence about a kit a violation. The
# kit-name alternation is DERIVED from the tracked `tools/*` directories, never listed, so a new kit
# is covered the day it lands; the extension class is ONE string both arms read, at the epoch the
# ratchet records.
#
# TWO EXEMPTIONS, and they are not interchangeable. `gov:root-fixture — <reason>` on the offending
# LINE is the live one, and a marker with no reason is a refusal. The `<path>:<line>` WAIVER
# registry is frozen at its existing rows and takes no new ones: it keys on position, so any edit
# above a waived line unpins it and reds a merge that touched nothing it guarded
# (TOOL-aSealedCaravan-1). Shrink-only, so the count may fall and never rise.
#
# WHAT THIS GATE DOES NOT CHECK, said out loud because a structural check reads as a semantic one to
# everyone who did not write it. It does not know whether a path is CORRECT — only whether it is
# spelled at a prefix that will not exist in an adopter's tree. It does not read `memory/`, this
# repo's own records, which are not shipped and are repo-root-relative by convention. Arms 1 and 3
# do not grade a file no descriptor resolves; the ban list below DOES, since epoch 5, because its
# population is every tracked file under the kit surface, shipped or not, and it is the one account
# of what is left to drain. It grades TEXT: a path assembled at run time from two variables is
# outside every predicate. The ban does not count a bare `tools/` with no segment after it, a
# directory-only kit reference under any prefix but gov's, or a kit segment with no file after it;
# its homonym rules are context heuristics (see the epoch-5 and epoch-6 blocks) and say where they
# stop.
set -u
# TOOL-cWidenedNet-1 S4 — CAPTURED BEFORE THE `cd`, because `$0` may be relative and the `cd` below
# moves out from under it.
_self_dir=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || _self_dir=""
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "install-prefix: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

# TOOL-cWidenedNet-1 S4 — THIS GATE'S OWN SIDECARS ARE DERIVED, and an empty derivation REFUSES.
# Both lines used to spell `tools/`. That is the literal ban this script enforces, broken inside the
# enforcer, and invisible to it: `.txt` sat outside the predicate's extension class until S1 widened
# it, so the arm graded every kit in the tree and never itself. The consequence at any prefix but
# `tools/` is not a crash — the waiver registry reads as ABSENT, every declared waiver silently
# stops applying, and the ban list reads as missing. A wrong verdict, quietly.
#
# `git -C <dir> rev-parse --show-prefix` and not `${_self_dir#"$ROOT"/}`: on Windows a junction makes
# the two spellings of one tree differ as strings, so the strip no-ops and the result comes out
# ABSOLUTE. The unattended kit's own adopter records the same defect at its line 38.
#
# An EMPTY prefix is the repo root, which is a legal install and not a failure — the two are told
# apart by git's exit status, not by the emptiness of its answer.
if ! SELF_REL=$(git -C "$_self_dir" rev-parse --show-prefix 2>/dev/null); then
  echo "install-prefix: cannot derive this gate's own directory from '$_self_dir', so its waiver"
  echo "install-prefix: registry and ban list cannot be resolved. REFUSING rather than falling back"
  echo "install-prefix: to a guessed prefix, which is the shape that makes a broken install look"
  echo "install-prefix: like a working one."
  exit 2
fi
SELF_REL=${SELF_REL%/}
SELF_PREFIX=${SELF_REL:+$SELF_REL/}
# The awk field the kit-name walk reads, derived from the same answer: the path is
# `<prefix…>/<kit>/<file>` and the kit is the field after the prefix's own segments, so a root
# install reads field 1, `scripts/` field 2, `vendor/gov/` field 3. The first cut of this line
# pinned the field at 2, which held for a one-segment prefix only — at `vendor/gov/` the walk
# named `gov` as every kit's name and the refusal below fired (the self-test's S4 arm, red from
# the day that cut landed).
_seg_kit=$(( $(printf '%s' "$SELF_PREFIX" | tr -cd '/' | wc -c) + 1 )); _seg_min=$_seg_kit
WAIVERS="${SELF_PREFIX}install-prefix-waivers.txt"
# Derived for the same reason and hoisted to sit beside its sibling; the ban arm's own section below
# says what this file IS.
CARRIED="${SELF_PREFIX}install-prefix-carried.txt"
MODE="${1:---check}"
case "$MODE" in --check|--list|--write-ratchet|--rebaseline) ;;
  *) echo "usage: $(basename "$0") [--check|--list|--write-ratchet|--rebaseline]"; exit 2 ;; esac

# TOOL-cWidenedNet-1 S5 made this THE KIT-SOURCE TEST, ONCE; TOOL-aRepatriatedFork-16 S2 hoisted it
# above BOTH arms. A repo SHIPS what its registry resolves — `govkit apply` writes nothing a registry
# does not name — so a repo with no registry ships nothing and neither arm has a population. Arm 1
# used to grade `${SELF_PREFIX}*` regardless, and at a consumer that is the consumer's own tree plus
# every gov file it received, against waivers keyed on gov's paths: measured at a `scripts/` adopter,
# nine hits, five of them gov's own waived bytes, and the kit was deselected.
# TOOL-aRepatriatedFork-29 S3: BOTH PATHS ARE DERIVED from `SELF_PREFIX`. They used to stay literal
# on the argument that a kit source's registry sits at gov's layout by definition — true of the
# layout BELOW the tool root, and false of the tool root itself, which gov may be checked out under
# at any name. The registry and the resolver sit beside this gate's own directory in a source, and a
# consumer receives neither, so the test answers the same question at every prefix.
# TOOL-aRepatriatedFork-46 S4: NEITHER IS PROBED BY NAME ANY MORE. Both were spelled as a kit name
# joined to `SELF_PREFIX`, which is the class this gate bans, and `<prefix>/lib/` ships nowhere. The
# python resolver is carried INLINE, and govkit is found by the sibling-kit resolver below, which
# reads the install receipt first. Its anchor is govkit's ENGINE and not the registry, because the
# registry also ships inside the playbook renderer: a consumer's receipt names a registry row, and
# anchoring on it would read that consumer as a kit source. The engine ships nowhere.
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
    here = pathlib.Path(here).resolve()
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
        hit = (root / str(row["path"])).resolve()
        if hit.is_file() and root in hit.parents:
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
# The python the kit-source test needs. A launcher that does not run is a REFUSAL and never a
# consumer: read as "no kit source here", it would skip a kit source's whole verdict at exit 0.
PY_GATE=$(resolve_python) || {
  echo "install-prefix: no usable python, so this gate cannot tell whether this repo is a kit"
  echo "install-prefix: SOURCE. REFUSING rather than reading that as a consumer with nothing to police."
  exit 2
}
KIT_SOURCE=no
REGISTRY=""
if _gk_dir=$(resolve_kit_dir "$PY_GATE" govkit govkit.py "$_self_dir" 2>/dev/null) \
   && [ -f "$_gk_dir/registry.toml" ]; then
  KIT_SOURCE=yes
  REGISTRY="$_gk_dir/registry.toml"
fi
if [ "$KIT_SOURCE" != yes ]; then
  # A SKIP ANNOUNCES ITSELF (§7), and exits 0 (§8 F1, owner): a consumer's bar stays green when it
  # has nothing to police, and a printed skip cannot be misread as a graded run.
  echo "install-prefix: root-install arm SKIPPED — this repo is not a kit SOURCE (no govkit engine"
  echo "install-prefix: and registry resolve from this gate's directory), so it ships nothing and"
  echo "install-prefix: its files under ${SELF_PREFIX:-the repo root} were NOT graded on this run."
  echo "install-prefix: carried-prefix arm SKIPPED — this repo is not a kit SOURCE (no govkit engine"
  echo "install-prefix: and registry resolve from this gate's directory) and so has no"
  echo "install-prefix: shippable set to grade. Said out loud rather than passed silently: a skip"
  echo "install-prefix: that looks like a pass is indistinguishable from coverage."
  exit 0
fi
# The python launcher for the carried-prefix arm below, resolved through the repo's ONE resolver and
# through nothing else. There is deliberately no `PY=python` fallback: the MS-Store `python3` stub
# answers `command -v` and exits 9009, so a bare launcher name is not an answer — and the idiom ban
# in `<prefix>/lib/resolve-python.test.sh` reds on one, which is how this line got written correctly the
# second time. A tree without the resolver has no shippable set to grade either; the arm says so and
# skips, rather than guessing at an interpreter.

# The kit names, derived. `git ls-files` so the answer is the same on every node and in every
# checkout — a directory listing would also see untracked scratch dirs.
#
# THE PREFIX IS `SELF_PREFIX`, not the literal `tools/`, and this is the same defect the sidecar
# derivation twenty lines up was written to close — met a second time in the same file, which is why
# one fix did not cover it. At an adopter installed anywhere else the glob matched NOTHING and the
# refusal below fired, so the one gate guarding this whole class could only ever REFUSE outside gov.
# Measured at a `scripts/` adopter, which had been carrying a local carve-out for exactly this line.
kits=$(git ls-files -- "${SELF_PREFIX}*/*" | awk -F/ "NF>${_seg_min} {print \$${_seg_kit}}" | sort -u)
[ -n "$kits" ] || { echo "install-prefix: no kit directories under ${SELF_PREFIX:-the repo root} — that is not a pass"; exit 1; }
alt=$(printf '%s' "$kits" | tr '\n' '|'); alt=${alt%|}

# TOOL-cWidenedNet-1 S5 — HOISTED, and the hoist is the whole reason this sits here rather than
# beside the ban it was written for: bash resolves a function at CALL time, and its first caller is
# now arm 1, a few lines below. It feeds both.
derive_received_files() {
  # Every distinct SOURCE path the descriptors resolve, deduplicated — the same pair `planned_writes`
  # walks — PLUS the one named addition. `WIRE-INTO-PROJECT.md` is resolved for no kit and would be
  # graded nowhere by a derived-only population, while it PRESCRIBES the install paths: a root
  # spelling there becomes a root install in every repo that follows it. One member, one reason.
  # NO test or selftest exclusion here, and that is where this population and arm 1's own glob part
  # company: a shipped test IS received.
  #
  # TOOL-cWidenedNet-1 S5 renamed it from `carried_population`. It is no longer the ban's population
  # alone: arm 1 intersects its own suffix-excluded files with this set, so a received test is graded
  # for the ROOT spelling while an unshipped one is not. The name now says what the set IS rather
  # than which arm happened to ask first.
  #
  # TOOL-aRepatriatedFork-16 S1 — the set itself is govkit's `shipped` verb, the ONE derivation of
  # what this repo ships; this function used to carry its own heredoc over the same calls. The verb
  # sits beside the registry the kit-source test already found. A verb that fails prints NOTHING
  # here, not the named addition alone, so the liveness checks below still see a dead probe.
  local _shipped
  _shipped=$("$(resolve_python)" "${REGISTRY%/*}/govkit.py" shipped) || return 0
  [ -n "$_shipped" ] || return 0
  # TOOL-dTieredTribunal-27, AND IT DOES REPRODUCE — under epoch 2, which is how it was finally
  # seen. THE RATCHET MUST NOT GRADE ITSELF. Every row in it IS a path, so the file counts its own
  # rows as carried literals: writing it moves its own count, the next --check reds, and no
  # hand-edit settles it because the edit changes the count again. Under epoch 1 the number
  # happened to sit still and the defect read as FIXED — my own brief recorded it as not
  # reproducing, on a one-pass fixed-point measurement. Widening the predicate moved it 96 -> 107
  # and the loop was immediate.
  #
  # A file whose entire content is a list of paths cannot CARRY one: the paths are its data, not a
  # reference that would arrive at a target and resolve to nothing there. Same reason the arm above
  # already drops this script and the waiver registry from its own population. The verb prints
  # every survivor, this one included; dropping it is this gate's business, so it happens here.
  { printf '%s\n' "$_shipped" | tr -d '\r' | cut -f3 | grep -vxF "$CARRIED"
    echo "WIRE-INTO-PROJECT.md"; } | LC_ALL=C sort -u
}

# The shipped surface: what a target repo receives, plus the file that tells them where to put it.
# WIRE-INTO-PROJECT.md is in the population even though nothing copies it — it PRESCRIBES the install
# paths, so a root spelling there becomes a root install in every repo that follows it. Highest
# leverage member of the set, not an edge case.
#
# TOOL-cWidenedNet-1 S5 — THE SUFFIX EXCLUSION IS NO LONGER THE WHOLE STORY. A test, a selftest and
# a `.conf.example` are dropped here because they build root-prefix installs ON PURPOSE, to prove
# the dual-spelling support this repo keeps for its not-retrofitted adopters; gating them wholesale
# would forbid testing the thing that support exists for. But a file being excused for its FIXTURES
# also excused its USAGE HEADER, and six shipped files were telling an adopter to run a path that
# resolves to nothing in their tree. So the excluded files come back IF THEY ARE RECEIVED, and the
# per-LINE marker below is what carries the fixture exemption the file-level drop used to carry.
SUFFIX_EXCL='(\.test\.sh|\.test\.py|selftest\.py|\.conf\.example)$'
self_excl="^${SELF_PREFIX}(check-install-prefix\.sh|install-prefix-waivers\.txt)$"
# `${SELF_PREFIX}*`, the third place this file spelled its own prefix as a literal: at any other
# install the kit surface matched nothing and the empty-population refusal below fired instead of a
# verdict — the same shape the kit walk had, one block down.
glob_set=$(git ls-files -- "${SELF_PREFIX}*" 'skills/*' '.githooks/*' '*.template.*' '*.fragment.json' \
                       'coding-governance-agents.template.md' 'WIRE-INTO-PROJECT.md' \
        | grep -vE "$self_excl")
files=$(printf '%s\n' "$glob_set" | grep -vE "$SUFFIX_EXCL" || true)
[ -n "$files" ] || { echo "install-prefix: the shipped surface is empty — that is not a pass"; exit 1; }

# The suffix-excluded members come back IF AND ONLY IF an adopter RECEIVES them, which is the
# descriptor-resolved set the ban arm has always used. An unshipped test is still dropped: nobody
# reads it but us, and its fixtures are none of this arm's business. Only a kit source reaches this
# line (the test above), so the received set always exists here.
_recv=$(derive_received_files | tr -d '\r' | grep -v '^$' | LC_ALL=C sort)
if [ -n "$_recv" ]; then
  _extra=$(printf '%s\n' "$glob_set" | grep -E "$SUFFIX_EXCL" | LC_ALL=C sort \
           | comm -12 - <(printf '%s\n' "$_recv") || true)
  [ -n "$_extra" ] && files=$(printf '%s\n%s\n' "$files" "$_extra" | grep -v '^$' | LC_ALL=C sort -u)
else
  # The population DIED rather than being empty. Both other arms already refuse on this, and a
  # silent narrowing here would be the same defect with a quieter failure mode.
  echo "install-prefix: the received-set derivation resolved NOTHING, so arm 1 cannot tell a"
  echo "install-prefix: shipped test from an unshipped one. Refusing to grade a narrowed"
  echo "install-prefix: population over a probe that cannot move."
  exit 1
fi

# TOOL-cWidenedNet-1 S1 — THE EXTENSION CLASS, WRITTEN ONCE. Both arms read this string. Two copies
# of one predicate is two places for the pair to disagree, and only one of them gets widened next
# time — which is how the loose-file half of TOOL-aScouredKit-20 landed at epoch 2 while the
# extension half sat open.
#
# `txt|tsv|conf|example` joined the original six at epoch 3. Every kit here keeps its declaration
# sidecars as `.txt` or `.tsv` and ships a `.conf.example`, so those were the extensions the real
# literals used and the only ones neither arm could see. Measured before wiring, per §7's
# run-it-over-the-real-tree rule: the widening adds exactly ONE hit to this arm — a `cp` step in a
# kit README that an adopter follows — and 31 occurrences to the ban below.
EXT="sh|py|js|md|json|toml|txt|tsv|conf|example"

# `}` and `{` join the excluded lead characters so a placeholder-prefixed path — the very fix this
# gate exists to encourage — is not itself a hit. Without it `{{TOOL_ROOT}}codebase-map/x.py` reds,
# which would make the gate refuse the corrected form and accept only the broken one.
RE="(^|[^/{}[:alnum:]._-])($alt)/[A-Za-z0-9_.-]+\.($EXT)"

# TOOL-aScouredKit-6 — ONE grep over the file list, not one PER FILE. `grep -nE` over many files
# already prefixes each match with `<file>:<lineno>:`, which is the `<file>:<line>` shape this arm
# was assembling by hand — so the per-file loop existed only to add a prefix grep already emits.
# The `cut` keeps the first two colon-separated fields, which is exactly `${m%%:*}` applied twice.
#
# `grep` exits 1 on no match and a zero hit count is the SUCCESS state here, so the pipeline is
# terminated with `|| true` — the passing-zero-reads-as-failure class the charter names. `xargs -r`
# keeps an empty list from making grep read stdin.
#
# `-0` AND `-H`, both bought by this build's own closing review, and both are the difference between
# a gate and a gate-shaped no-op. BARE `xargs` applies shell-like quote processing to its input: a
# path holding a quote ABORTS the invocation and a path holding a space is silently split, and with
# stderr going to /dev/null and the status swallowed by `|| true` this arm would then print a clean
# result over files it never read. The two sibling scripts batched in the same commit use `-0` for
# exactly this reason and this one did not. `-H` forces the `<file>:` prefix that the `cut` below
# assumes: grep omits it when handed exactly ONE file, so a single-file population produced
# `<lineno>:<text>` and the cut took the line number as the path.
hits=$(printf '%s\n' "$files" | tr -d '\r' | grep -v '^$' | tr '\n' '\0' \
  | xargs -0 -r grep -HnE "$RE" -- 2>/dev/null | cut -d: -f1,2 || true)

waived_rows=""
[ -f "$WAIVERS" ] && waived_rows=$(grep -vE '^\s*(#|$)' "$WAIVERS" | awk '{print $1}')
waived_n=$(printf '%s' "$waived_rows" | grep -c . || true)

# TOOL-cWidenedNet-1 S6 — THE PER-LINE EXEMPTION, and it is a MARKER rather than a registry row.
# The registry above keys on `<path>:<line>`, and this corpus has already paid for that choice: an
# edit ABOVE a waived line unpins it, so the gate reds a merge that touched nothing the waiver
# guards (TOOL-aSealedCaravan-1, and `check-method-carriers.sh` and `lexicon.py` both cite it as the
# reason they key on text instead). A marker travels with the line it excuses.
#
# It is ALSO the thing that makes S5's population growth affordable. Those files build root-prefix
# installs on purpose; each such line now says so in place, where the next reader is already looking,
# instead of in a registry nobody opens.
#
# THREE STATES, not two. A marker with no reason is a REFUSAL: the exemption is meant to cost a
# sentence, and one that can be bought with eleven characters is a self-service exemption form — the
# same defect the ban arm below converted away from. `sed 's/^[^A-Za-z0-9]*//'` eats whatever
# separator the author used, em dash included, without this script having an opinion about encoding.
check_marker_reason() {
  _ln=$(sed -n "${1##*:}p" "${1%:*}" 2>/dev/null) || return 1
  case "$_ln" in *gov:root-fixture*) ;; *) return 1 ;; esac
  _why=$(printf '%s' "${_ln#*gov:root-fixture}" | sed 's/^[^A-Za-z0-9]*//')
  [ "${#_why}" -ge 3 ] || return 2
  return 0
}

if [ "$MODE" = --list ]; then
  printf '%s\n' "$hits" | grep -c . | xargs -I{} echo "install-prefix: {} hit(s) over $(printf '%s\n' "$files" | grep -c .) shipped files"
  printf '%s\n' "$hits" | while IFS= read -r h; do
    [ -n "$h" ] || continue
    if printf '%s\n' "$waived_rows" | grep -qxF "$h"; then printf '  waived  %s\n' "$h"
    elif check_marker_reason "$h"; then printf '  marked  %s\n' "$h"
    else printf '  HIT     %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"; fi
  done
fi

if [ "$MODE" = --check ]; then
bad=0
# LINE-DELIMITED, not word-split. `for h in $hits` splits on IFS, so a hit whose path holds a space
# becomes two bogus rows and neither matches a waiver — the reverse of the `-0` hardening applied to
# the PRODUCER above, left standing in its CONSUMER. Latent in this repo (0 spaced tracked paths,
# measured) and not latent in an adopter, whose tree this same gate grades. Same change on the
# waiver loop below, for the same reason.
marked_n=0
while IFS= read -r h; do
  [ -n "$h" ] || continue
  printf '%s\n' "$waived_rows" | grep -qxF "$h" && continue
  check_marker_reason "$h"; _m=$?
  if [ "$_m" = 0 ]; then marked_n=$((marked_n+1)); continue; fi
  if [ "$bad" = 0 ]; then
    # TOOL-aRepatriatedFork-16 S4: the prefix is the DERIVED one. This line used to name gov's
    # default, which is false at every other prefix this gate runs under.
    echo "install-prefix: a SHIPPED file spells a root-install kit path. Kits install at"
    echo "install-prefix: ${SELF_PREFIX:-the repo root/}<kit>/ here and at an adopter's own prefix there, so"
    echo "install-prefix: these resolve to nothing in their tree — and nothing else"
    echo "install-prefix: reds. Fix the path, or mark the line \`gov:root-fixture — <reason>\` when the"
    echo "install-prefix: spelling is a deliberate fixture. (The $WAIVERS registry still holds its"
    echo "install-prefix: existing rows and takes no new ones: it keys on <path>:<line> and unpins.)"
  fi
  bad=$((bad+1))
  if [ "$_m" = 2 ]; then
    printf '  %s  MARKER WITH NO REASON — %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-70)"
  else
    printf '  %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"
  fi
done <<EOF
$hits
EOF
[ "$bad" = 0 ] || exit 1

# A waiver that no longer names a hit is a stale row: the spelling it excused is gone, and leaving it
# lets the NEXT one in silently under a pin that never fell.
stale=0
while IFS= read -r w; do
  [ -n "$w" ] || continue
  printf '%s\n' "$hits" | grep -qxF "$w" && continue
  [ "$stale" = 0 ] && echo "install-prefix: stale waiver(s) — the spelling they excuse is gone; delete the row:"
  stale=$((stale+1)); printf '  %s\n' "$w"
done <<EOF
$waived_rows
EOF
[ "$stale" = 0 ] || exit 1

echo "install-prefix: clean — $(printf '%s\n' "$files" | grep -c .) shipped files, $waived_n declared waiver(s), $marked_n marked fixture line(s), no undeclared root-install spelling"
fi

# ==================== TOOL-aRepatriatedFork-2 S8 — ARM 3, RUNTIME LITERALS =======================
# The two arms above grade SPELLINGS in text, prose and code alike, and the ban is shrink-only: a
# runtime literal rides inside a file's recorded count. This arm grades CODE lines only, with ZERO
# tolerance, because a path an engine RUNS or READS at run time is a defect the day it lands, not a
# count to drain. Measured before it was wired: the first carried-prefix-style grep missed every
# argv spelled under the repo root's own prefix and every quoted prefix segment joined to a kit,
# and those were the forks both adopters
# carried.
#
# THE POPULATION is `govkit shipped` rows with role `engine` or `rendered`, minus the suffix
# exclusion above. `seed` is out (written once, adopter-owned after), and so is `merged`: no writer
# lands that role (TOOL-aRepatriatedFork-2 spec rev-4). Of those, only CODE files are read — `.py`,
# `.sh`, `.js`, an extensionless hook, and a fragment's `hook_path`. A rendered `.md` is prose.
#
# CODE IS: in `.py`, every line with its comments and its docstring-shaped strings blanked by
# `tokenize`; in shell, every line whose first non-blank byte is not `#`, heredoc bodies included
# because they are printed; in `.js`, text outside `//` and `/* */`. THREE PREDICATES: P1 is gov's
# `tools/` followed by a tracked kit dir or loose file, after a non-path lead character or a
# `$VAR/`, `${VAR}/` or `$(…)/`; P2 is a quoted `tools` segment joined by `/` or `,` to a quoted
# segment P1 would accept (py, js); P3 is a quoted kit HOME name used as a path segment beside `/`
# outside the resolver's own copy (py). A hit exits 1 naming `<path>:<line>` and its predicate.
#
# THE MARKER is `gov:prefix-literal — <reason>` on the line, read in the three states
# `check_marker_reason` reads `gov:root-fixture` in: none, one with no reason (a refusal), one with.
#
# WHAT THIS ARM CANNOT SEE: a path assembled from two variables, a literal inside `eval` or `sh -c`
# text built at run time, a Python path built by `str.join`, and any file no descriptor resolves.
# An empty population is a dead probe and refuses; it never reads as clean.
if [ "$MODE" = --check ] || [ "$MODE" = --list ]; then
  _rt_py=$(resolve_python) || { echo "install-prefix: the runtime-literal arm has no usable python"; exit 1; }
  _rt_pop=$("$_rt_py" "${REGISTRY%/*}/govkit.py" shipped | tr -d '\r' \
            | awk -F'\t' '$2 == "engine" || $2 == "rendered" { print $3 }' \
            | grep -vE "$SUFFIX_EXCL" | LC_ALL=C sort -u)
  IFS= read -r -d '' _rt_src <<'RT' || true
import io
import os
import re
import sys
import tokenize

MODE = sys.argv[1]
files = [f for f in sys.stdin.read().split("\n") if f.strip()]
tracked = [t for t in os.environ.get("RT_TRACKED", "").split("\n") if t.startswith("tools/")]
dirs = {t.split("/")[1] for t in tracked if t.count("/") >= 2}
loose = {t.split("/")[1] for t in tracked if t.count("/") == 1}
if not files or not dirs:
    print("install-prefix: runtime-literal arm has an EMPTY population (%d file(s), %d kit dir(s))"
          " — that is a dead probe, not a pass" % (len(files), len(dirs)))
    sys.exit(1)
SEG = "|".join(sorted(map(re.escape, dirs | loose), key=len, reverse=True))
HOME = "|".join(sorted(map(re.escape, dirs), key=len, reverse=True))
P1 = re.compile(r"tools/(?:%s)(?![A-Za-z0-9_.-])" % SEG)
LEAD_VAR = re.compile(r"(\$\{?[A-Za-z_][A-Za-z0-9_]*\}?\"?|\$\([^()]*\)\"?)/$")
P2 = re.compile(r"""(["'])tools\1\s*[/,]\s*(["'])(?:%s)\2""" % SEG)
P3 = re.compile(r"""/\s*(["'])(?:%s)\1|(["'])(?:%s)\2\s*/(?!/)""" % (HOME, HOME))
PATHCH = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_./")
MARK = "gov:prefix-literal"


def check_p1(text):
    for m in P1.finditer(text):
        i = m.start()
        if i == 0 or text[i - 1] not in PATHCH or LEAD_VAR.search(text[:i]):
            return True
    return False


def read_code_py(src):
    """Source lines with every COMMENT and every docstring-shaped string blanked."""
    lines = src.split("\n")
    blank = []
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, SyntaxError, IndentationError):
        return lines
    skip = {tokenize.NL, tokenize.COMMENT, tokenize.INDENT, tokenize.DEDENT}
    sig = [t for t in toks if t.type not in skip]
    for k, t in enumerate(toks):
        if t.type == tokenize.COMMENT:
            blank.append((t.start, t.end))
    for k, t in enumerate(sig):
        if t.type != tokenize.STRING:
            continue
        prev = sig[k - 1].type if k else tokenize.NEWLINE
        nxt = sig[k + 1].type if k + 1 < len(sig) else tokenize.NEWLINE
        if prev in (tokenize.NEWLINE, tokenize.ENCODING) and nxt in (tokenize.NEWLINE, tokenize.ENDMARKER):
            blank.append((t.start, t.end))
    for (sr, sc), (er, ec) in blank:
        for r in range(sr, er + 1):
            ln = lines[r - 1]
            a = sc if r == sr else 0
            b = ec if r == er else len(ln)
            lines[r - 1] = ln[:a] + " " * (b - a) + ln[b:]
    return lines


def read_code_js(src):
    """Text outside `//` and `/* */`, read by a scanner that knows its strings: a `/*` inside a
    quoted glob opened a comment the first cut never closed, and every line after it went unread."""
    out, mode, quote = [], None, None
    for ln in src.split("\n"):
        text, i = [], 0
        while i < len(ln):
            c, two = ln[i], ln[i:i + 2]
            if mode == "block":
                mode, i = (None, i + 2) if two == "*/" else (mode, i + 1)
                continue
            if mode == "str":
                text.append(ln[i:i + 2] if c == "\\" else c)
                i += 2 if c == "\\" else 1
                if c == quote:
                    mode = None
                continue
            if two == "/*":
                mode, i = "block", i + 2
                continue
            if two == "//":
                break
            if c in "'\"`":
                mode, quote = "str", c
            text.append(c)
            i += 1
        if mode == "str" and quote != "`":
            mode = None
        out.append("".join(text))
    return out


def read_code(path, src):
    base = os.path.basename(path)
    if path.endswith(".py"):
        return read_code_py(src), ("P1", "P2", "P3")
    if path.endswith(".js"):
        return read_code_js(src), ("P1", "P2")
    if base.endswith(".fragment.json"):
        return [ln if '"hook_path"' in ln else "" for ln in src.split("\n")], ("P1",)
    if path.endswith(".sh") or "." not in base:
        return [("" if ln.lstrip().startswith("#") else ln) for ln in src.split("\n")], ("P1",)
    return None, ()


pop = hits = marked = 0
bad = []
for f in files:
    try:
        src = open(f, encoding="utf-8", errors="replace", newline="").read().replace("\r\n", "\n")
    except OSError:
        continue
    code, preds = read_code(f, src)
    if code is None:
        continue
    pop += 1
    raw = src.split("\n")
    in_rkd = False
    for n, text in enumerate(code, 1):
        if raw[n - 1].startswith("# >>> resolve_kit_dir"):
            in_rkd = True
        if raw[n - 1].startswith("# <<< resolve_kit_dir"):
            in_rkd = False
        which = [p for p, test in (("P1", lambda t: check_p1(t)),
                                   ("P2", lambda t: P2.search(t)),
                                   ("P3", lambda t: not in_rkd and P3.search(t)))
                 if p in preds and test(text)]
        if not which:
            continue
        hits += 1
        line = raw[n - 1]
        state = "HIT"
        if MARK in line:
            why = re.sub(r"^[^A-Za-z0-9]*", "", line.split(MARK, 1)[1])
            state = "marked" if len(why) >= 3 else "NO REASON"
        if state == "marked":
            marked += 1
        else:
            bad.append((f, n, which, state, line.strip()[:90]))
        if MODE == "--list":
            print("  %-9s %s:%d  %s  %s" % (state, f, n, "+".join(which), line.strip()[:80]))

if pop == 0:
    print("install-prefix: runtime-literal arm graded NO code file out of %d shipped — a dead probe" % len(files))
    sys.exit(1)
if MODE == "--list":
    print("install-prefix: runtime-literal arm: %d hit line(s) over %d shipped code file(s), %d marked"
          % (hits, pop, marked))
    sys.exit(0)
if bad:
    print("install-prefix: a SHIPPED engine spells gov's own `tools/` prefix, or a sibling kit's")
    print("install-prefix: directory, in a string it RUNS or READS at run time. At any other install")
    print("install-prefix: that resolves to nothing. Derive it from the file's own location, route a")
    print("install-prefix: sibling kit through resolve_kit_dir, or — when the line is correct by")
    print("install-prefix: construction — mark it `gov:prefix-literal — <reason>`.")
    for f, n, which, state, line in bad:
        tag = "MARKER WITH NO REASON — " if state == "NO REASON" else ""
        print("  %s:%d  %s  %s%s" % (f, n, "+".join(which), tag, line))
    sys.exit(1)
print("install-prefix: runtime literals clean — %d shipped code file(s), %d marked line(s), no unmarked"
      " runtime literal" % (pop, marked))
RT
  printf '%s\n' "$_rt_pop" | RT_TRACKED="$(git ls-files -- 'tools/*')" "$_rt_py" -c "$_rt_src" "$MODE"
  _rt=$?
  [ "$MODE" = --check ] && [ "$_rt" != 0 ] && exit 1
fi

# ---------------------------------------------------------------------------------------------
# DEPL-dCarriedReceipt-15 — THE SECOND ARM, over a SECOND population and a SECOND prefix.
#
# The arm above owns the ROOT spelling (`<kit>/file`) over a glob-derived surface. This one owns the
# SHIPPING spelling (`tools/<kit>/file`) inside the set the descriptors declare shippable, which is
# a different question with a different answer: `apply` writes gov's bytes VERBATIM — nothing
# substitutes into a file body anywhere — so every literal `tools/<kit>/…` a kit body spells arrives
# unchanged in a target installed at another prefix and resolves to nothing in their tree.
#
# THE PREDICATE IS THE CLAIM AND THE ARTIFACT IS THE COUNT. An earlier attempt at this unit published
# a file-and-line pair in prose; six candidate populations were re-measured against it afterwards and
# none reproduced the pair, because "shippable" has several defensible spellings and a sentence and a
# script are free to spell it differently forever. So NO number is written here or in the spec.
# `<prefix>/install-prefix-carried.txt` carries them, and ONE function below emits both that file and
# the `--list` section, so the artifact and the report cannot disagree.
#
# INERT WHERE THIS REPO IS NOT A KIT SOURCE, and it SAYS SO rather than passing silently. This script
# is itself shipped, to adopters who install at their own prefix; an arm keying on the local prefix
# would red every usage header in every kit they received.
# `CARRIED` is assigned at the top of this script, beside `WAIVERS`, and DERIVED rather than spelled
# (TOOL-cWidenedNet-1 S4). Its population, `derive_received_files`, is hoisted to the top for the same
# reason: arm 1 now calls it too, and bash resolves a function at CALL time.

# ==================== TOOL-dRetiredFork-17 S4 — THE PREDICATE EPOCH =============================
# WHAT THIS EXISTS TO PREVENT. The block below made this arm a BAN: --write-ratchet may lower a
# count, never add one. That is the whole value, and it creates one honest problem — when the
# PREDICATE itself widens, every newly-visible literal reads as a new carrier, and a ban with no
# way to re-baseline would have to be edited by hand a hundred rows at a time or, far more likely,
# switched off.
#
# A `--rebaseline` mode with no guard is the self-service exemption form again, wearing a new name.
# So it is guarded by a value that a definitional change MUST move and an ordinary pass CANNOT:
# this epoch, recorded in the ratchet's own header. `--rebaseline` refuses unless the two differ,
# which makes it one-shot per predicate change and useless for absorbing a literal.
PREDICATE_EPOCH=6

# epoch 1 — `tools/<kit>/<file>.<ext>`, a kit DIRECTORY segment required.
# epoch 2 — TOOL-aScouredKit-20. Adds a LOOSE file directly under `tools/`, which epoch 1 could not
#   see at all: five wave-2 hardcoded-prefix findings were green on this leg for that reason.
#   Counted ONLY when the named file actually exists in the tree, and that test is not tidiness —
#   measured over the real population before wiring, per S5, it separates 50 real literals from 76
#   FIXTURE names (`gate-a.sh`, `some-gate.sh`, `alpha.sh`) inside test helpers, which would
#   otherwise red seven innocent files. Its one known false drop is `<prefix>/manifest-check.sh`,
#   which is real but ships from `skills/session-kickoff/`, so gov does not carry it at that path;
#   recorded here rather than papered over, because a heuristic with an unstated blind spot is how
#   this arm got its first one.
# epoch 3 — TOOL-cWidenedNet-1 S1. Adds `txt|tsv|conf|example` to the extension class, which BOTH
#   arms read from one string now. Every kit keeps its declaration sidecars as `.txt` or `.tsv` and
#   ships a `.conf.example`, so these were the extensions the real literals used and the only ones
#   neither arm could see — including, measured at `c4f02308`, the four in this script's own body
#   that resolve its waiver registry and this ratchet. Measured before wiring: +1 hit on arm 1 (a
#   `cp` step in a kit README, FIXED rather than waived) and +31 occurrences here, which is what
#   this epoch was spent on. The remaining blind extensions are deliberate: `.yml`, `.ini`, `.cfg`
#   and `.example`'s longer cousins appear nowhere in this tree, and an alternative matching
#   nothing is an assertion about nothing.
# epoch 4 — TOOL-cMendedVintage-5 S1. Drops `-` from the LEAD class both regexes share, so a shell
#   default expansion — `${VAR:-tools/…}` and its `:+` and `:=` cousins — is finally a hit. That
#   spelling is a variable resolving at the target's prefix with a hardcoded fallback resolving
#   only at gov's, which is the commonest shape this ban exists to catch and was the one shape it
#   could not see. MEASURED over the shipped population at this commit: +2 occurrences, both argv
#   defaults in gov-side checkers, and both carry a reason column rather than a repair. The
#   population's own size is NOT written here — the ban list carries every current figure, and this
#   block records what an epoch cost when it was spent.
#   `/` was measured in the same run and DELIBERATELY KEPT: dropping it adds 203 occurrences,
#   dominated by CORRECT `<gov>/…` spellings that name gov's own checkout in runbook and adopter
#   prose, so the ban would red on the one spelling that is right.
#   THE LEAD CLASS IS ALSO THIS COMMENT'S PROBLEM. A backtick is not in it, so a sentence here that
#   quotes a kit path in full is itself a hit — TOOL-cMendedVintage-4 held its own row that way.
#   Name the prefix or name the file, never both.
# epoch 5 — TOOL-aRepatriatedFork-23. The ban stops grading a SUBSET of the class. Epoch 4 counted
#   one spelling inside the shipped set, and a census at 2143b6d6 found about 1500 more literals it
#   could not see, so a drain graded by it would have read zero with most of the class in place.
#   Five changes, each measured over the real tree before it was wired:
#   * THE POPULATION is every tracked file under the kit surface, `skills/`, `.githooks/`, every
#     template and the runbook, shipped or not — `git ls-files`, no descriptor consulted. Only this
#     ban list and the waiver registry stay out, both being lists of paths.
#   * `/` LEFT THE LEAD CLASS, so `$ROOT/`, `<project>/` and `<gov>/` leads count (§8 F2 of the
#     unit's spec: a `<gov>/` spelling is derived where printed and a prose token elsewhere). A
#     directory-only `tools/<kit>` counts, and a loose `tools/<name>.<ext>` counts whether or not that
#     file exists: the epoch-2 existence filter is gone, because a fixture's loose name is a literal
#     the owner ruled in scope.
#   * A KIT SEGMENT followed by a file counts at the root, under ANY literal prefix and under a
#     derived base — F4 and F1: a kit's name typed as a literal is the class whatever leads it. Only
#     the drained forms do not: a `{prefix}`, `{kit}` or `{{TOOL_ROOT}}` render token, or a
#     `<prefix>/` or `<tool-root>/` prose token.
#   * A QUOTED `"tools"` counts when it is JOINED — by `/`, by `,` to a quoted segment, or inside a
#     `join(` call — and a quoted kit segment counts when used as a path segment. A mapping key is
#     not joined and does not count.
#   * HOMONYMS are read from context: a path through a tool-owned dot directory (a Skill directory
#     under `.claude/skills/`, a git `hooks/`, a CI `workflows/`), or joined onto an operand naming a
#     git directory or a transcript. That last one is a NAME heuristic and its ceiling is written
#     where it lives, in the counter below.
#   The grep and awk pipeline could not read a join's operand, so the counter is a python program
#   beside arm 3's, and a counter that DIES refuses rather than printing zero rows (the D3 class).
#   Markers and waiver rows have NO effect here: they still excuse a line from arms 1 and 3, and the
#   ban counts it, so this list is the one account of what is left to drain.
#   COST, measured by the one --rebaseline on node a: rows 139 -> 223 and occurrences 905 -> 3674,
#   over 324 tracked files of which 58 no descriptor ships. The unit's acceptance ledger splits the
#   rise by rule and reconciles it to the census. A --check went from 27-28 s to 22-24 s wall: one
#   python pass replaced three derivations of the received set and a grep per epoch-2 filter.
# epoch 6 — TOOL-aRepatriatedFork-46. Two places epoch 5 misjudged its own class, each measured over
#   the real tree before it was wired:
#   * THE HOMONYM RULE. Rule 4's comma branch counted any quoted kit segment after a quoted literal
#     segment, so a kit id passed as an argument, a list member and a JSON key all read as paths. It
#     now counts only inside an open `join(`, `joinpath(` or `Path(` call. 47 occurrences stopped
#     counting and none started: forty-one `--kits` argv and fixture-builder arguments in govkit's
#     selftest, two system `lib` directories, two JSON `hooks` keys, a deploy list and a keyword
#     tuple. Its ceiling is written beside it in the counter.
#   * THE BRACE RULE. Rule 3 read EVERY brace before a kit name as a render token, so the `${PFX}`
#     spelling an earlier unit drained the literal prefix into left the kit name after it uncounted.
#     Only `{prefix}/`, `{kit}/` and `{{TOOL_ROOT}}`, and the prose tokens `<prefix>/` and
#     `<tool-root>/`, drain now: 426 occurrences in 46 files joined the count.
#   COST, measured on node a before this unit derived a line: rows 56 -> 82 and occurrences
#   625 -> 1004, which is 625 - 47 + 426. The --rebaseline that recorded it ran after the gate's own
#   four kit-source lines were derived in the same commit, so the file it wrote holds four fewer.


carried_live() {
  # L1, from ROUND 2. The liveness assertion used to sit on `rows`, the HIT set -- so a live
  # derivation over a repo that genuinely carries zero literals was indistinguishable from a dead
  # one, and on the day this repo reaches DEPL-dCarriedReceipt-15's own stated goal the leg would
  # red with a false statement and no override short of editing the gate. Reproduced with a positive
  # control: one shipped file carrying one literal writes a row and exits 0; change that literal to
  # the placeholder form arm 9 blesses and the identical run claims the derivation DIED.
  #
  # The population is what proves the probe can move. The hit count is the answer and is free to be
  # zero. Epoch 5: it is the ban's OWN population, the one the counter reads.
  derive_carried_files | grep -c . || true
}

derive_carried_files() {
  # TOOL-aRepatriatedFork-23 S2 — EVERY tracked file under the kit surface, shipped or not. The ban
  # used to read `derive_received_files`, so a file no descriptor resolved carried literals nobody
  # counted: 57 of them at 2143b6d6, and the drain would have reached zero with them in place. This
  # list and the waiver registry stay out, because every row in either IS a path.
  git ls-files -- "${SELF_PREFIX}*" 'skills/*' '.githooks/*' '*.template.*' 'WIRE-INTO-PROJECT.md' \
    | tr -d '\r' | grep -vxF -e "$CARRIED" -e "$WAIVERS" | LC_ALL=C sort -u
}

carried_rows() {
  # THE ONE EMITTER. `--list`'s section and the ratchet file are the same rows from the same call, so
  # a report that disagrees with the artifact is not reachable. A row is `<path>\t<count>\t<kits>`:
  # the count is OCCURRENCES per path, not hit lines, because a line carrying two literals counted
  # once held the count level while the surface it grades changed (DEPL-dGaugedVintage-7). The kits
  # column names each kit a path's literals name, sorted, and `(loose)` for a name directly under
  # gov's prefix or a join to no kit.
  #
  # EPOCH 5 — the counter is the python program below, not a `grep -oE` and two awks. What it needs
  # that a regex cannot give it is the OPERAND a join starts from: `common / "<kit>"` and
  # `parent / "<kit>"` are one shape, and only the operand says which is a git-dir sidecar and which
  # names a sibling kit. Its rules and their order are the epoch-5 block above.
  #
  # A COUNTER THAT DIES REFUSES. The D3 class from DEPL-dCarriedReceipt's closing review: a dead
  # producer at the head of a pipe yields zero rows at the pipe's exit 0, and the ban then compares
  # empty against empty forever. So the status returned here is python's, and every caller reds on
  # it. The rows go out as BYTES, because python's text-mode `print` writes CRLF on Windows.
  local _py _out _rc
  _py=$(resolve_python) || return 1
  IFS= read -r -d '' _carried_src <<'CARRIED_PY' || true
import os
import re
import sys

files = [f.strip("\r") for f in sys.stdin.read().split("\n") if f.strip()]
kits = [k for k in os.environ.get("CARRIED_KITS", "").split("\n") if k]
EXT = os.environ.get("CARRIED_EXT", "")
if not files or not kits or not EXT:
    sys.stderr.write("install-prefix: the ban's counter got %d file(s), %d kit name(s) and %s extension"
                     " class — a dead probe, not a pass\n" % (len(files), len(kits), "an" if EXT else "no"))
    sys.exit(2)
NP = "A-Za-z0-9_.-"
Q = "[\"']"
KIT = "|".join(sorted(map(re.escape, kits), key=len, reverse=True))
FILE = re.compile(r"[%s]+\.(?:%s)(?![%s])" % (NP, EXT, NP))
GOVPFX = re.compile(r"(?<![{}A-Za-z0-9_.])tools/(?:(?P<k>%s)(?![%s])(?:/[%s]*)?|[%s]+\.(?:%s)(?![%s]))"
                    % (KIT, NP, NP, NP, EXT, NP))
QGOV = re.compile(r"(%s)tools\1" % Q)
KSEG = re.compile(r"(?<![%s])(?P<k>%s)/(?P<rest>[%s]*)" % (NP, KIT, NP))
QKIT = re.compile(r"(%s)(?P<k>%s)\1" % (Q, KIT))
DOTDIR = re.compile(r"^\.[A-Za-z]")
# ponytail: a NAME heuristic over the operand a join starts from. Its ceiling: a git directory or a
# transcript held in a variable named otherwise counts as a kit path. The remedy is a name that says
# what the variable holds, never a marker: markers have no effect on this list.
NONKIT = re.compile(r"(?i)git|\bgd\b|\bcommon\b|\bsdir\b|session|transcript")


def derive_operand(before):
    """The operand a join starts from: the text after the last `=`, `,`, `(`, `[` or `{`, every
    balanced call collapsed first so that `f(g())` does not hide `f`."""
    s = before
    while True:
        t = re.sub(r"\([^()]*\)", "", s)
        if t == s:
            return re.split(r"[=,(\[{]", s)[-1]
        s = t


def check_homonym(operand):
    return bool(NONKIT.search(operand) or re.search(r"%s\.[A-Za-z]" % Q, operand))


# Epoch 6, the brace rule: the ONLY spellings that drain a kit segment. Any other brace before a kit
# name is a derived base the kit name was typed after, which is the class (`${PFX}<kit>/`).
DRAINED = re.compile(r"(?:\{prefix\}/|\{kit\}/|\{\{TOOL_ROOT\}\}|<prefix>/|<tool-root>/)$")
# Epoch 6, the homonym rule: a quoted kit segment after a quoted literal segment and a comma is a path
# only inside an open path-join call. ponytail: its ceiling is a callee that assembles the path from
# separate arguments, `f('clean', 'scripts', '<kit>')`, which reads as an argument list and is not
# seen: the same blind spot as a path built from two variables.
JOINCALL = re.compile(r"(?:\bjoin|\bjoinpath|\bPath)\s*$")


def check_path_join(before):
    """True when the innermost bracket still open at the end of <before> is a path-join call."""
    s = before
    while True:
        t = re.sub(r"\([^()]*\)|\[[^\[\]]*\]|\{[^{}]*\}", "", s)
        if t == s:
            break
        s = t
    i = max(s.rfind("("), s.rfind("["), s.rfind("{"))
    return i >= 0 and s[i] == "(" and bool(JOINCALL.search(s[:i]))


def scan_line(line):
    work = re.sub(r"\\[ntr]", "  ", line)  # a path after a `\n` escape reads as after a space
    out = []

    def add(a, b, kit):
        nonlocal work
        out.append(kit)
        work = work[:a] + "\0" * (b - a) + work[b:]

    # 1. a quoted gov-prefix segment, JOINED: by `/`, by `,` to a quoted segment, or in a join( call
    for m in QGOV.finditer(work):
        a, b = m.span()
        before, after = work[:a], work[b:]
        if not (re.match(r"\s*/(?!/)", after) or re.match(r"\s*,\s*%s" % Q, after)
                or re.search(r"/\s*$", before) or re.search(r"join\([^()]*,\s*$", before)):
            continue  # a mapping key, a list member, an argument: not a path segment (S4)
        nx = re.match(r"\s*[/,]\s*(%s)(?P<s>[%s]*)\1" % (Q, NP), after)
        kit, end = "(loose)", b
        if nx:
            kit, end = (nx.group("s") if nx.group("s") in kits else "(loose)"), b + nx.end()
        add(a, end, kit)
    # 2. gov's prefix followed by a kit (directory-only or not) or a loose `<name>.<ext>`, after any
    #    lead but a path character or a brace — `/` included, so `$ROOT/`, `<gov>/`, `<project>/`
    for m in GOVPFX.finditer(work):
        add(m.start(), m.end(), m.group("k") or "(loose)")
    # 3. `<kit>/<file>.<ext>` at the root, under any literal prefix (F4) and under a derived base (F1)
    for m in KSEG.finditer(work):
        a, before = m.start(), work[:m.start()]
        if not FILE.match(m.group("rest")):
            continue
        if before[-1:] == "\0" or DRAINED.search(before):
            continue  # a render or prose token (epoch 6), or a span an earlier rule counted
        if before.endswith("/"):
            operand = re.split(r"[\s\"'`=(]", before)[-1]
            if any(DOTDIR.match(s) for s in operand.split("/")) or NONKIT.search(operand):
                continue  # a Skill dir, a git `hooks/`, a sidecar under the git dir (S4)
        add(a, m.end(), m.group("k"))
    # 4. a quoted kit segment used as a path segment: joined by `/` (F1, arm 3's P3 shape), or by `,`
    #    after a quoted literal prefix segment (F4) — unless the operand makes it a homonym (S4)
    for m in QKIT.finditer(work):
        a, b = m.span()
        before, after = work[:a], work[b:]
        if re.search(r"/\s*$", before) or re.match(r"\s*/(?!/)", after):
            if check_homonym(derive_operand(before)):
                continue
        else:
            pre = re.search(r"(%s)(?P<p>[%s]+)\1\s*,\s*$" % (Q, NP), before)
            if not pre or DOTDIR.match(pre.group("p")) or pre.group("p") == ".." \
                    or not check_path_join(before):
                continue  # an argument, a list member, a mapping key: not inside a path join (epoch 6)
        add(a, b, m.group("k"))
    return out


rows = {}
for f in files:
    try:
        src = open(f, encoding="utf-8", errors="replace", newline="").read().replace("\r\n", "\n")
    except OSError:
        continue
    for line in src.split("\n"):
        got = scan_line(line)
        if got:
            rows.setdefault(f, []).extend(got)
sys.stdout.buffer.write("".join("%s\t%d\t%s\n" % (f, len(rows[f]), ",".join(sorted(set(rows[f]))))
                                for f in sorted(rows)).encode("utf-8"))
CARRIED_PY
  _out=$(derive_carried_files | CARRIED_KITS="$kits" CARRIED_EXT="$EXT" "$_py" -c "$_carried_src"); _rc=$?
  [ -n "$_out" ] && printf '%s\n' "$_out"
  return "$_rc"
}

print_counter_death() {
  echo "install-prefix: the ban's COUNTER died (no usable python, or it refused its input), so it"
  echo "install-prefix: measured nothing. Refusing to read that as a population carrying zero"
  echo "install-prefix: literals: a dead producer is the D3 class, not a clean result."
}

# A repo that is not a kit source exited at the kit-source test near the top, with this arm's SKIP.
if [ "$MODE" = --write-ratchet ]; then
  # D3, from the closing review of DEPL-dCarriedReceipt. `carried_rows` ends in a pipe, and this
  # script sets only `set -u` — no `pipefail` — so the status is `sort`'s and a DEAD producer (an
  # unresolvable python, a govkit import error, a `resolve_entry` raise, a traceback out of the
  # heredoc) yields ZERO ROWS AT EXIT 0. That truncated the tracked ratchet and printed
  # `wrote 0 carried-prefix row(s)` cheerfully; once committed, `--check` compared empty against
  # empty and printed `clean` forever. Green-by-absence, on a leg that is on the bar — and reachable
  # by FOLLOWING THE GATE'S OWN REMEDY, since a collapsed population reds as SLACK first and the
  # SLACK message says to re-run this very mode.
  #
  # The class is not hypothetical here: this build's own first `--write-ratchet` wrote zero rows for
  # a CR reason and reported it cheerfully. That INSTANCE was fixed with `tr -d '\r'`; this is
  # CLASS. The first arm of this same script already guards the identical shape twice, by name.
  [ "$(carried_live)" -gt 0 ] || { echo "install-prefix: the carried-prefix POPULATION is empty — that is not a pass.
install-prefix: the derivation resolved no shippable sources at all, which means it DIED rather than
install-prefix: that this repo ships nothing. Refusing to truncate $CARRIED over a probe that cannot
install-prefix: move. A zero HIT count is fine and is the goal; a zero population is a dead probe."; exit 1; }
  rows=$(carried_rows) || { print_counter_death; exit 1; }
  # ==================== TOOL-dRetiredFork-17 S3 — THE RATCHET IS NOW A BAN ====================
  # THE ONE CHANGE THAT CONVERTS THEM, and it is here rather than on the check path. A shrink-only
  # ratchet slows the class without closing it: a new literal may still enter, it just has to be
  # paid for elsewhere. And the payment is self-service — `--write-ratchet` re-stamps the baseline,
  # so anybody who runs the remedy the gate itself prints absorbs the rise and the leg goes green.
  #
  # MEASURED, ON THIS BUILD, BY ME: `DEPL-dRetiredFork-6` added one line to the runbook naming the
  # deployer's entry point, taking that file 28 -> 29. The leg redded correctly. I ran
  # `--write-ratchet`, it rewrote the baseline, and the rise was gone without anyone deciding
  # anything. A speed limit with a self-service exemption form is not a speed limit.
  #
  # AND THIS COMMENT SPELLED THAT PATH OUT AT FIRST, which took THIS file 6 -> 7 and was refused by
  # the block below as I wrote it. A rule against retyping literals, broken inside the sentence
  # explaining the rule. Left recorded rather than quietly fixed, because it is the best evidence
  # the arm has that the class is reflexive and not a thing only other people do.
  #
  # So this mode may now only LOWER a recorded count or DROP a row that reached zero. A path with
  # no row, or a count above its row, is refused HERE — the new literal has to be justified by hand
  # in the file, with a reason, in the pass that wants it. That is the whole ban.
  if [ -s "$CARRIED" ]; then
    added=$(printf '%s\n' "$rows" | awk -F'\t' 'NR==FNR { seen[$1]=1; next } !($1 in seen) { print $1 }' "$CARRIED" -)
    risen=$(printf '%s\n' "$rows" | awk -F'\t' '
      NR==FNR { was[$1]=$2; next }
      ($1 in was) && ($2+0 > was[$1]+0) { printf "%s\t%s -> %s\n", $1, was[$1], $2 }' "$CARRIED" -)
    if [ -n "$added" ] || [ -n "$risen" ]; then
      echo "install-prefix: REFUSING to write. This is a BAN, not a ratchet: --write-ratchet may"
      echo "install-prefix: lower a count or drop a row that reached zero, and may NOT absorb a new"
      echo "install-prefix: one. Otherwise the remedy this gate prints is a self-service exemption"
      echo "install-prefix: form, and the class it exists to drain refills through the gate itself."
      [ -n "$added" ] && { echo "install-prefix: NEW carrier(s), which no row justifies:"; \
                           printf '%s\n' "$added" | sed 's/^/install-prefix:   /'; }
      [ -n "$risen" ] && { echo "install-prefix: RISEN count(s):"; \
                           printf '%s\n' "$risen" | sed 's/^/install-prefix:   /'; }
      echo "install-prefix: Derive the path — that is S1's rule and the reason this arm exists — or,"
      echo "install-prefix: if the literal is genuinely correct, add its row to the ratchet BY HAND"
      echo "install-prefix:   ($CARRIED)"
      echo "install-prefix: with a trailing reason column saying why. A row a human wrote is a"
      echo "install-prefix: decision; a row this script wrote is an accident nobody reviewed."
      exit 1
    fi
  fi
  # THE REASONS SURVIVE THE WRITE. A row's fourth column is a human's justification for a literal
  # the ban would otherwise refuse, and `carried_rows` emits three columns — so without this join,
  # the next legitimate drop would silently erase every reason in the file and leave a ban whose
  # exceptions nobody can account for. Comment lines are carried through untouched for the same
  # reason: the file's own header explains what it is.
  if [ -s "$CARRIED" ]; then
    rows=$(printf '%s\n' "$rows" | awk -F'\t' -v OFS='\t' '
      NR==FNR { if ($0 !~ /^[[:space:]]*(#|$)/ && NF>3) { r[$1]=$4 } next }
      { if ($1 in r) { print $1, $2, $3, r[$1] } else { print } }' "$CARRIED" -)
    hdr=$(grep -E '^[[:space:]]*#' "$CARRIED" || true)
    [ -n "$hdr" ] && rows="$hdr
$rows"
  fi
  printf '%s
' "$rows" > "$CARRIED.tmp" && mv "$CARRIED.tmp" "$CARRIED"
  echo "install-prefix: wrote $(grep -cE '^[^#]' "$CARRIED" || true) carried-prefix row(s) to $CARRIED"
  exit 0
elif [ "$MODE" = --rebaseline ]; then
  # GUARDED BY THE EPOCH, and refuses outright when it has not moved. This is the ONLY way a row is
  # added to a ban list without a human writing it, and it is spendable exactly once per predicate
  # change — which is what stops it from being the exemption form under a new name.
  recorded=$(sed -n 's/^# predicate-epoch: \([0-9][0-9]*\).*/\1/p' "$CARRIED" | head -1)
  recorded=${recorded:-1}
  if [ "$recorded" = "$PREDICATE_EPOCH" ]; then
    echo "install-prefix: REFUSING to rebaseline. The recorded predicate epoch is $recorded and the"
    echo "install-prefix: script declares $PREDICATE_EPOCH — they agree, so the predicate has not"
    echo "install-prefix: changed and there is nothing to re-derive. This mode exists for a"
    echo "install-prefix: DEFINITIONAL widening and for nothing else; a new literal under an"
    echo "install-prefix: unchanged predicate is a decision, and it is made by hand in $CARRIED."
    exit 1
  fi
  [ "$(carried_live)" -gt 0 ] || { echo "install-prefix: the population is empty — refusing to rebaseline over a dead probe."; exit 1; }
  before=$(grep -cE '^[^#]' "$CARRIED" 2>/dev/null || echo 0)
  rows=$(carried_rows) || { print_counter_death; exit 1; }
  keep=$(grep -E '^[[:space:]]*#' "$CARRIED" 2>/dev/null | grep -v '^# predicate-epoch:' || true)
  reasons=$(printf '%s\n' "$rows" | awk -F'\t' -v OFS='\t' '
    NR==FNR { if ($0 !~ /^[[:space:]]*(#|$)/ && NF>3) { r[$1]=$4 } next }
    { if ($1 in r) { print $1, $2, $3, r[$1] } else { print } }' "$CARRIED" -)
  { [ -n "$keep" ] && printf '%s\n' "$keep"
    echo "# predicate-epoch: $PREDICATE_EPOCH"
    printf '%s\n' "$reasons"; } > "$CARRIED.tmp" && mv "$CARRIED.tmp" "$CARRIED"
  after=$(grep -cE '^[^#]' "$CARRIED" || true)
  echo "install-prefix: REBASELINED for predicate epoch $recorded -> $PREDICATE_EPOCH."
  echo "install-prefix: rows $before -> $after. Every hand-written reason column was preserved."
  echo "install-prefix: This is a DEFINITIONAL re-derivation, not an absorption: read the diff and"
  echo "install-prefix: say in the commit message what the predicate now sees that it did not."
  exit 0
elif [ "$MODE" = --list ]; then
  echo "install-prefix: carried-prefix rows (every kit-path spelling, over every tracked file under the kit surface):"
  _lr=$(carried_rows) || print_counter_death
  [ -n "$_lr" ] && printf '%s\n' "$_lr" | sed 's/^/  /'
else
  # D3's other half: the same liveness assertion on the CHECK path, so a dead derivation cannot
  # report a clean empty population against an empty ratchet either. It is FIRST because everything
  # below reads a population this proves can move.
  [ "$(carried_live)" -gt 0 ] || { echo "install-prefix: the carried-prefix POPULATION is empty — that is not a pass.
install-prefix: the derivation resolved no shippable sources, which means it DIED rather than that
install-prefix: this repo ships nothing. A zero HIT count is fine; a zero population is a dead probe."; exit 1; }
  rows=$(carried_rows) || { print_counter_death; exit 1; }
  # `-s` not `-f` (D4): an empty-but-present file passed an existence check and then met the awk.
  # L1's other half: once the hit set legitimately reaches zero, an EMPTY ratchet is the correct
  # committed state, so it is only "missing" while something still carries a literal. This sits
  # AFTER the assignment for the reason `set -u` gives: the first cut read `$rows` one line above
  # the line that sets it.
  # ROUND 4's L2: these are TWO states and one condition was grading both. Narrowing the guard to
  # `-s AND rows non-empty` meant a genuinely MISSING file fell through whenever the hit set was
  # zero -- which is exactly the goal state L1 was added to permit -- and the awk below then could
  # not open its first file, exiting 2 and printing the carried-literal remedy instead of this one.
  # The gate still redded, so it taught the operator the wrong repair rather than passing wrongly.
  # MISSING is unconditional; EMPTY-BUT-PRESENT keeps the narrowing, which is what D4 bought.
  if [ ! -e "$CARRIED" ]; then
    echo "install-prefix: no $CARRIED — run --write-ratchet once and commit it. A missing ratchet is"
    echo "install-prefix: not a clean one."
    exit 1
  fi
  if [ ! -s "$CARRIED" ] && [ -n "$rows" ]; then
    echo "install-prefix: $CARRIED is EMPTY while $(printf '%s
' "$rows" | grep -c .) file(s) still"
    echo "install-prefix: carry a literal — run --write-ratchet once and commit it."
    exit 1
  fi
  # SHRINK-ONLY, PER FILE. The existing arm's `<path>:<line>` shape goes stale on every edit above a
  # waived line, and one row per hit line would rot within a week; per file trades swap-blindness for
  # a ratchet that survives ordinary editing. ONE awk over both sides, reporting all four conditions,
  # because a `| while` loop runs in a subshell and its verdict variable never reaches the exit.
  # D12: this wrote `tools/install-prefix-carried.txt.now` INTO the tree it is grading, with no
  # trap. `gate-fingerprint.sh` folds untracked files into the working-tree fingerprint, so a
  # leftover forced an unnecessary full bar at the push boundary — and it broke the hermetic-leg
  # rule while grading the tree it dirtied. `mktemp` plus a trap, and the rows are already in hand.
  _now=$(mktemp); trap 'rm -f "$_now"' EXIT
  printf '%s
' "$rows" > "$_now"
  awk -F'\t' -v pinf="$CARRIED" '
    # D4 + D13. `NR==FNR` is true for the WHOLE of file 2 when file 1 has zero records, because
    # FNR resets per file and NR does not — so an empty-but-present ratchet filled `pin[]` from the
    # MEASURED file, left `now[]` empty, and printed `SLACK <path> N -> 0 (delete the row)` for
    # every file: telling the operator to delete a ratchet that records nothing, while the correct
    # verdict UNRECORDED never printed. `FILENAME == pinf` cannot swap the roles, and it finally
    # READS the `-v pinf` this program was already being passed and never used (D13).
    FILENAME == pinf { if ($0 !~ /^[[:space:]]*(#|$)/) { pin[$1]=$2; pinkit[$1]=$3 } next }
    $1 == "" { next }   # an EMPTY hit set writes one blank line; without this the
                        # awk read it as a path and reported UNRECORDED for the empty
                        # string, so the zero goal state redded on a phantom row
    { now[$1]=$2; nowkit[$1]=$3 }
    END {
      bad=0
      for (p in now) {
        if (!(p in pin)) { printf "  UNRECORDED  %s\t%s — every carrying file needs a row, or the ratchet grades a subset of itself\n", p, now[p]; bad++ }
        else if (now[p]+0 > pin[p]+0) { printf "  ROSE        %s\t%s -> %s\n", p, pin[p], now[p]; bad++ }
        else if (nowkit[p] != pinkit[p]) { printf "  SWAPPED     %s\t%s: kits %s -> %s — the count held while the kits it names changed\n", p, now[p], pinkit[p], nowkit[p]; bad++ }
      }
      for (p in pin) {
        c = (p in now) ? now[p] : 0
        if (c+0 < pin[p]+0) { printf "  SLACK       %s\t%s -> %s%s\n", p, pin[p], c, (c+0==0 ? " (delete the row)" : "") ; bad++ }
      }
      exit bad ? 1 : 0
    }' "$CARRIED" "$_now"
  cstat=$?
  if [ "$cstat" != 0 ]; then
    echo "install-prefix: apply writes gov's bytes VERBATIM, so a carried literal naming a kit path"
    echo "install-prefix: arrives unchanged in a target installed at another prefix and resolves to"
    echo "install-prefix: nothing there. Derive the path — that is the authoring rule this arm"
    echo "install-prefix: enforces, and it is stated in AGENTS.md and in the hooks README."
    echo "install-prefix:"
    echo "install-prefix: THE REMEDY DEPENDS ON THE VERDICT, and --write-ratchet is no longer a"
    echo "install-prefix: blanket answer to any of them (TOOL-dRetiredFork-17 made this arm a BAN):"
    echo "install-prefix:   SLACK      — a count fell. Re-run --write-ratchet; that is what it is for."
    echo "install-prefix:   ROSE       — a new literal entered. Derive it, or justify it by hand."
    echo "install-prefix:   UNRECORDED — a file started carrying one. Same two options."
    echo "install-prefix:   SWAPPED    — the count held while the kits changed. Read the diff."
    echo "install-prefix: A hand-written row takes a fourth tab-separated column giving the reason,"
    echo "install-prefix: and that column now survives later writes."
    exit 1
  fi
  echo "install-prefix: carried-prefix clean — $(grep -cE '^[^#]' "$CARRIED") recorded file(s), $(awk -F'\t' 'NF>3 && $0 !~ /^[[:space:]]*#/' "$CARRIED" | grep -c . || true) hand-justified, none rising"
fi
