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
case "$MODE" in --check|--list|--write-ratchet) ;;
  *) echo "usage: $(basename "$0") [--check|--list|--write-ratchet]"; exit 2 ;; esac
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
# keeps an empty list from making grep read stdin, and the list is newline-delimited exactly as the
# `$files` variable already was, so no path handling changes.
hits=$(printf '%s\n' "$files" | tr -d '\r' | grep -v '^$' \
  | xargs -r grep -nE "$RE" -- 2>/dev/null | cut -d: -f1,2 || true)

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
for h in $hits; do
  printf '%s\n' "$waived_rows" | grep -qxF "$h" && continue
  if [ "$bad" = 0 ]; then
    echo "install-prefix: a SHIPPED file spells a root-install kit path. An adopter installs kits at"
    echo "install-prefix: tools/<kit>/, so these resolve to nothing in their tree — and nothing else"
    echo "install-prefix: reds. Fix the path, or add a row to $WAIVERS with the reason it must stay."
  fi
  bad=$((bad+1))
  printf '  %s  %s\n' "$h" "$(sed -n "${h##*:}p" "${h%:*}" | sed 's/^[[:space:]]*//' | cut -c1-90)"
done
[ "$bad" = 0 ] || exit 1

# A waiver that no longer names a hit is a stale row: the spelling it excused is gone, and leaving it
# lets the NEXT one in silently under a pin that never fell.
stale=0
for w in $waived_rows; do
  printf '%s\n' "$hits" | grep -qxF "$w" && continue
  [ "$stale" = 0 ] && echo "install-prefix: stale waiver(s) — the spelling they excuse is gone; delete the row:"
  stale=$((stale+1)); printf '  %s\n' "$w"
done
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

carried_population() {
  # Every distinct SOURCE path the descriptors resolve, deduplicated — the same pair `planned_writes`
  # walks — PLUS the one named addition. `WIRE-INTO-PROJECT.md` is resolved for no kit and would be
  # graded nowhere by a derived-only population, while it PRESCRIBES the install paths: a root
  # spelling there becomes a root install in every repo that follows it. One member, one reason.
  # NO test or selftest exclusion here, and that is where this population and the arm above part
  # company: a shipped test IS received.
  # shellcheck source=/dev/null
  . tools/lib/resolve-python.sh
  "$(resolve_python)" - <<'PYEOF'
import pathlib, sys
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
  # a report that disagrees with the artifact is not reachable. The count is hit LINES per path: a
  # line carrying two literals counts once. The regex is the arm above's with the SHIPPING prefix
  # bound, and `{`/`}` stay in the excluded lead class for the reason that arm already gives — the
  # corrected placeholder form must not be a hit.
  local re_ship="(^|[^/{}[:alnum:]._-])tools/($alt)/[A-Za-z0-9_.-]+\.(sh|py|js|md|json|toml)"
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
    printf '%s\n' "$f"
  done | xargs -r grep -cE "$re_ship" -- 2>/dev/null \
       | awk -F: 'NF>=2 && $NF+0 > 0 { c=$NF; sub(/:[^:]*$/, "", $0); printf "%s\t%s\n", $0, c }' \
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
  printf '%s
' "$rows" > "$CARRIED.tmp" && mv "$CARRIED.tmp" "$CARRIED"
  echo "install-prefix: wrote $(grep -c . "$CARRIED" || true) carried-prefix row(s) to $CARRIED"
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
    FILENAME == pinf { if ($0 !~ /^[[:space:]]*(#|$)/) pin[$1]=$2; next }
    $1 == "" { next }   # an EMPTY hit set writes one blank line; without this the
                        # awk read it as a path and reported UNRECORDED for the empty
                        # string, so the zero goal state redded on a phantom row
    { now[$1]=$2 }
    END {
      bad=0
      for (p in now) {
        if (!(p in pin)) { printf "  UNRECORDED  %s\t%s — every carrying file needs a row, or the ratchet grades a subset of itself\n", p, now[p]; bad++ }
        else if (now[p]+0 > pin[p]+0) { printf "  ROSE        %s\t%s -> %s\n", p, pin[p], now[p]; bad++ }
      }
      for (p in pin) {
        c = (p in now) ? now[p] : 0
        if (c+0 < pin[p]+0) { printf "  SLACK       %s\t%s -> %s%s\n", p, pin[p], c, (c+0==0 ? " (delete the row)" : "") ; bad++ }
      }
      exit bad ? 1 : 0
    }' "$CARRIED" "$_now"
  cstat=$?
  if [ "$cstat" != 0 ]; then
    echo "install-prefix: apply writes gov's bytes VERBATIM, so a carried tools/<kit>/ literal arrives"
    echo "install-prefix: unchanged in a target installed at another prefix and resolves to nothing"
    echo "install-prefix: there. Derive the path, or re-run --write-ratchet in the pass that earned"
    echo "install-prefix: the drop and commit the file."
    exit 1
  fi
  echo "install-prefix: carried-prefix clean — $(grep -c . "$CARRIED") recorded file(s), none rising"
fi
