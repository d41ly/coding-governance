#!/usr/bin/env bash
# check-install-prefix.sh — nothing this repo SHIPS may spell a root-install kit path.
#
#   bash tools/check-install-prefix.sh            # assert; exit 1 on an unwaived hit
#   bash tools/check-install-prefix.sh --list     # print every hit, waived or not (authoring aid)
#   bash tools/check-install-prefix.sh --write-ratchet   # (re)write the carried-prefix ratchet
#
# WHY. Kits install at `tools/<kit>/` in a target repo (one segment; the codebase-map gate template
# resolves no deeper). Every ENGINE already derives its own prefix, so what actually strands an
# adopter is a path SPELLED in something they receive: a runbook step, a usage header, a remedy
# string, a rendered artifact. Those fail quietly. Measured before this gate existed: a `tools/`
# install scaffolded the adopter's own committed `HYGIENE.md` with seven kit paths that resolve to
# nothing in their tree, and the hygiene gate exited 0 over it.
#
# THE POPULATION is what a target repo RECEIVES, and the two exclusions are principled rather than
# convenient. Test and selftest files are excluded because they BUILD root-prefix installs on
# purpose, to prove the dual-spelling support this repo keeps for its existing adopters — gating
# them would forbid testing the thing that support exists for. `*.conf.example` is excluded because
# its values are stamped by an adopter at install time.
#
# THE PREDICATE matches a kit name followed by a real FILE. A bare `memory-tree/` in prose names the
# kit, not a path anyone runs, and gating it would make every sentence about a kit a violation. The
# kit-name alternation is DERIVED from the tracked `tools/*` directories, never listed, so a new kit
# is covered the day it lands.
#
# WAIVERS are a tracked file, one `<path>:<line>` per row with a reason after whitespace. Every entry
# today is a deliberate root spelling that supports the not-retrofitted adopters. Shrink-only: the
# count may fall, never rise, so a new spelling cannot be waived away quietly.
set -u
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "install-prefix: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

WAIVERS="tools/install-prefix-waivers.txt"
MODE="${1:---check}"
case "$MODE" in --check|--list|--write-ratchet|--rebaseline) ;;
  *) echo "usage: $(basename "$0") [--check|--list|--write-ratchet|--rebaseline]"; exit 2 ;; esac
# The python launcher for the carried-prefix arm below, resolved through the repo's ONE resolver and
# through nothing else. There is deliberately no `PY=python` fallback: the MS-Store `python3` stub
# answers `command -v` and exits 9009, so a bare launcher name is not an answer — and the idiom ban
# in `tools/lib/resolve-python.test.sh` reds on one, which is how this line got written correctly the
# second time. A tree without the resolver has no shippable set to grade either; the arm says so and
# skips, rather than guessing at an interpreter.

# The kit names, derived. `git ls-files` so the answer is the same on every node and in every
# checkout — a directory listing would also see untracked scratch dirs.
kits=$(git ls-files -- 'tools/*/*' | awk -F/ 'NF>2 {print $2}' | sort -u)
[ -n "$kits" ] || { echo "install-prefix: no kit directories under tools/ — that is not a pass"; exit 1; }
alt=$(printf '%s' "$kits" | tr '\n' '|'); alt=${alt%|}

# The shipped surface: what a target repo receives, plus the file that tells them where to put it.
# WIRE-INTO-PROJECT.md is in the population even though nothing copies it — it PRESCRIBES the install
# paths, so a root spelling there becomes a root install in every repo that follows it. Highest
# leverage member of the set, not an edge case.
files=$(git ls-files -- 'tools/*' 'skills/*' '.githooks/*' '*.template.*' '*.fragment.json' \
                       'coding-governance-agents.template.md' 'WIRE-INTO-PROJECT.md' \
        | grep -vE '(\.test\.sh|\.test\.py|selftest\.py|\.conf\.example)$' \
        | grep -vE '^tools/(check-install-prefix\.sh|install-prefix-waivers\.txt)$')
[ -n "$files" ] || { echo "install-prefix: the shipped surface is empty — that is not a pass"; exit 1; }

# `}` and `{` join the excluded lead characters so a placeholder-prefixed path — the very fix this
# gate exists to encourage — is not itself a hit. Without it `{{TOOL_ROOT}}codebase-map/x.py` reds,
# which would make the gate refuse the corrected form and accept only the broken one.
RE="(^|[^/{}[:alnum:]._-])($alt)/[A-Za-z0-9_.-]+\.(sh|py|js|md|json|toml)"

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

if [ "$MODE" = --list ]; then
  printf '%s\n' "$hits" | grep -c . | xargs -I{} echo "install-prefix: {} hit(s) over $(printf '%s\n' "$files" | grep -c .) shipped files"
  printf '%s\n' "$hits" | while IFS= read -r h; do
    [ -n "$h" ] || continue
    if printf '%s\n' "$waived_rows" | grep -qxF "$h"; then printf '  waived  %s\n' "$h"
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
while IFS= read -r h; do
  [ -n "$h" ] || continue
  printf '%s\n' "$waived_rows" | grep -qxF "$h" && continue
  if [ "$bad" = 0 ]; then
    echo "install-prefix: a SHIPPED file spells a root-install kit path. An adopter installs kits at"
    echo "install-prefix: tools/<kit>/, so these resolve to nothing in their tree — and nothing else"
    echo "install-prefix: reds. Fix the path, or add a row to $WAIVERS with the reason it must stay."
  fi
  bad=$((bad+1))
  printf '  %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"
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

echo "install-prefix: clean — $(printf '%s\n' "$files" | grep -c .) shipped files, $waived_n declared waiver(s), no undeclared root-install spelling"
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
# `tools/install-prefix-carried.txt` carries them, and ONE function below emits both that file and
# the `--list` section, so the artifact and the report cannot disagree.
#
# INERT WHERE THIS REPO IS NOT A KIT SOURCE, and it SAYS SO rather than passing silently. This script
# is itself shipped, to adopters who install at their own prefix; an arm keying on the local prefix
# would red every usage header in every kit they received.
CARRIED="tools/install-prefix-carried.txt"

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
PREDICATE_EPOCH=2

# epoch 1 — `tools/<kit>/<file>.<ext>`, a kit DIRECTORY segment required.
# epoch 2 — TOOL-aScouredKit-20. Adds a LOOSE file directly under `tools/`, which epoch 1 could not
#   see at all: five wave-2 hardcoded-prefix findings were green on this leg for that reason.
#   Counted ONLY when the named file actually exists in the tree, and that test is not tidiness —
#   measured over the real population before wiring, per S5, it separates 50 real literals from 76
#   FIXTURE names (`gate-a.sh`, `some-gate.sh`, `alpha.sh`) inside test helpers, which would
#   otherwise red seven innocent files. Its one known false drop is `tools/manifest-check.sh`,
#   which is real but ships from `skills/session-kickoff/`, so gov does not carry it at that path;
#   recorded here rather than papered over, because a heuristic with an unstated blind spot is how
#   this arm got its first one.

carried_population() {
  # Every distinct SOURCE path the descriptors resolve, deduplicated — the same pair `planned_writes`
  # walks — PLUS the one named addition. `WIRE-INTO-PROJECT.md` is resolved for no kit and would be
  # graded nowhere by a derived-only population, while it PRESCRIBES the install paths: a root
  # spelling there becomes a root install in every repo that follows it. One member, one reason.
  # NO test or selftest exclusion here, and that is where this population and the arm above part
  # company: a shipped test IS received.
  # shellcheck source=/dev/null
  . tools/lib/resolve-python.sh
  CARRIED_SELF="$CARRIED" "$(resolve_python)" - <<'PYEOF'
import os
import pathlib, sys
CARRIED_SELF = os.environ.get("CARRIED_SELF", "")
sys.path.insert(0, "tools/govkit")
import govkit
root = pathlib.Path(".").resolve()
reg = govkit.load_toml(root / "tools" / "govkit" / "registry.toml")
srcs = set()
for eid, (d, _p) in govkit.read_descriptors(root, reg, govkit.Report()).items():
    for row in govkit.resolve_entry(root, d, govkit.canonical_ctx(eid))["survivors"]:
        if row.get("src"):
            srcs.add(row["src"])
srcs.add("WIRE-INTO-PROJECT.md")
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
# already drops this script and the waiver registry from its own population.
srcs.discard(str(CARRIED_SELF))
print("\n".join(sorted(srcs)))
PYEOF
}

carried_live() {
  # L1, from ROUND 2. The liveness assertion used to sit on `rows`, the HIT set -- so a live
  # derivation over a repo that genuinely carries zero literals was indistinguishable from a dead
  # one, and on the day this repo reaches DEPL-dCarriedReceipt-15's own stated goal the leg would
  # red with a false statement and no override short of editing the gate. Reproduced with a positive
  # control: one shipped file carrying one literal writes a row and exits 0; change that literal to
  # the placeholder form arm 9 blesses and the identical run claims the derivation DIED.
  #
  # The population is what proves the probe can move. The hit count is the answer and is free to be
  # zero.
  carried_population | tr -d '\r' | grep -c . || true
}

carried_rows() {
  # THE ONE EMITTER. `--list`'s section and the ratchet file are the same rows from the same call, so
  # a report that disagrees with the artifact is not reachable. A row is
  # `<path>\t<count>\t<kits>`: the count is OCCURRENCES per path,
  # not hit lines. `grep -c` counted a line carrying two literals ONCE, so a second literal added
  # beside an existing one -- or one kit's path swapped for another's -- held the count level while
  # the surface it grades changed. DEPL-dGaugedVintage-7. Measured before the change: appending one
  # line carrying two literals moved a file 3 -> 4 where occurrences make it 3 -> 5. `grep -o` emits
  # one line per MATCH prefixed `<path>:`, and awk tallies per path; repo-relative paths carry no
  # colon, so splitting on the first is exact here. The old note read: hit LINES per path, a
  # line carrying two literals counts once. The regex is the arm above's with the SHIPPING prefix
  # bound, and `{`/`}` stay in the excluded lead class for the reason that arm already gives — the
  # corrected placeholder form must not be a hit.
  # EPOCH 2. The second alternative is the loose file, and it is fenced on both sides: `(?!/)` is
  # unavailable in POSIX ERE, so the trailing `[^/]` job is done by the existence filter below —
  # a `tools/foo/` prefix never names an existing loose file, so it cannot double-count.
  local re_ship="(^|[^/{}[:alnum:]._-])tools/(($alt)/[A-Za-z0-9_.-]+|[A-Za-z0-9_.-]+)\.(sh|py|js|md|json|toml)"
  # `tr -d '\r'` because python's `print` translates newlines on Windows, so every path arrives with
  # a trailing CR and `[ -f "$f" ]` answers false for all 181 of them — a population that silently
  # becomes empty, which is the shape this whole unit is written against. The arm above already does
  # this to its own file list, one line up, for the same reason.
  # TOOL-aScouredKit-6 — ONE `grep -cE` over the whole population, not one PER FILE. With several
  # files `grep -c` prefixes each count with `<file>:`, which is the `<file>\t<count>` pair this
  # loop was building by hand — so the awk below only re-shapes the separator and drops the zeros
  # the loop was dropping with its own `-gt 0` test. Output is byte-identical, sort included.
  #
  # The `[ -f "$f" ]` guard is preserved as a filter on the LIST rather than as a per-file test:
  # grep would report a missing path on stderr and skip it, so dropping the guard would change
  # what a stale population does, and this arm exists to grade one.
  #
  # `grep -c` exits 1 when every file counts zero, which is a legitimate and desirable state here,
  # so the pipeline is terminated with `|| true`.
  carried_population | tr -d '\r' | while IFS= read -r f; do
    [ -n "$f" ] || continue
    [ -f "$f" ] || continue
    printf '%s\0' "$f"
  done | xargs -0 -r grep -oHE "$re_ship" -- 2>/dev/null \
       | awk -F: -v tracked="$(git ls-files -- 'tools/*' | tr '\n' ' ')" '
           BEGIN { n = split(tracked, T, " "); for (i = 1; i <= n; i++) have[T[i]] = 1 }
           {
             p = $1; m = $0; sub(/^[^:]*:/, "", m)
             if (match(m, /tools\/[^\/]+\//)) { k = substr(m, RSTART+6, RLENGTH-7) }
             else {
               # EPOCH 2, THE EXISTENCE FILTER. A loose-file literal counts only when the file it
               # names is really there. Without it, 76 FIXTURE names in seven test helpers become
               # hits and the arm reds files whose only crime is having a fixture called `gate-a.sh`.
               if (match(m, /tools\/[A-Za-z0-9_.-]+\.(sh|py|js|md|json|toml)/) == 0) next
               lit = substr(m, RSTART, RLENGTH)
               sub(/^[^t]*/, "", lit)
               if (!(lit in have)) next
               k = "(loose)"
             }
             print p "\t" k
           }' \
       | LC_ALL=C sort \
       | awk -F'\t' '{ n[$1]++; if ($2 != last[$1]) { kits[$1] = (kits[$1] == "" ? $2 : kits[$1] "," $2); last[$1] = $2 } } END { for (q in n) printf "%s\t%s\t%s\n", q, n[q], kits[q] }' \
       | LC_ALL=C sort || true
}

if [ ! -f tools/govkit/registry.toml ] || [ ! -f tools/lib/resolve-python.sh ]; then
  echo "install-prefix: carried-prefix arm SKIPPED — this repo is not a kit SOURCE (no"
  echo "install-prefix: tools/govkit/registry.toml, or no tools/lib/resolve-python.sh) and has no"
  echo "install-prefix: shippable set to grade. Said out loud rather than passed silently: a skip"
  echo "install-prefix: that looks like a pass is indistinguishable from coverage."
elif [ "$MODE" = --write-ratchet ]; then
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
  rows=$(carried_rows)
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
  rows=$(carried_rows)
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
  echo "install-prefix: carried-prefix rows (the shipping spelling, inside the shippable set):"
  carried_rows | sed 's/^/  /'
else
  # D3's other half: the same liveness assertion on the CHECK path, so a dead derivation cannot
  # report a clean empty population against an empty ratchet either. It is FIRST because everything
  # below reads a population this proves can move.
  [ "$(carried_live)" -gt 0 ] || { echo "install-prefix: the carried-prefix POPULATION is empty — that is not a pass.
install-prefix: the derivation resolved no shippable sources, which means it DIED rather than that
install-prefix: this repo ships nothing. A zero HIT count is fine; a zero population is a dead probe."; exit 1; }
  rows=$(carried_rows)
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
