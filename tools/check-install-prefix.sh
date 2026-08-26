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

hits=$(printf '%s\n' "$files" | tr -d '\r' | while IFS= read -r f; do
  [ -n "$f" ] || continue
  grep -nE "$RE" -- "$f" 2>/dev/null | while IFS= read -r m; do printf '%s:%s\n' "$f" "${m%%:*}"; done
done)

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
  carried_population | tr -d '\r' | while IFS= read -r f; do
    [ -n "$f" ] || continue
    [ -f "$f" ] || continue
    n=$(grep -cE "$re_ship" -- "$f" 2>/dev/null || true)
    [ "${n:-0}" -gt 0 ] && printf '%s\t%s\n' "$f" "$n"
  done | LC_ALL=C sort
}

if [ ! -f tools/govkit/registry.toml ] || [ ! -f tools/lib/resolve-python.sh ]; then
  echo "install-prefix: carried-prefix arm SKIPPED — this repo is not a kit SOURCE (no"
  echo "install-prefix: tools/govkit/registry.toml, or no tools/lib/resolve-python.sh) and has no"
  echo "install-prefix: shippable set to grade. Said out loud rather than passed silently: a skip"
  echo "install-prefix: that looks like a pass is indistinguishable from coverage."
elif [ "$MODE" = --write-ratchet ]; then
  carried_rows > "$CARRIED.tmp" && mv "$CARRIED.tmp" "$CARRIED"
  echo "install-prefix: wrote $(grep -c . "$CARRIED" || true) carried-prefix row(s) to $CARRIED"
  exit 0
elif [ "$MODE" = --list ]; then
  echo "install-prefix: carried-prefix rows (the shipping spelling, inside the shippable set):"
  carried_rows | sed 's/^/  /'
else
  if [ ! -f "$CARRIED" ]; then
    echo "install-prefix: no $CARRIED — run --write-ratchet once and commit it. A missing ratchet is"
    echo "install-prefix: not a clean one."
    exit 1
  fi
  # SHRINK-ONLY, PER FILE. The existing arm's `<path>:<line>` shape goes stale on every edit above a
  # waived line, and one row per hit line would rot within a week; per file trades swap-blindness for
  # a ratchet that survives ordinary editing. ONE awk over both sides, reporting all four conditions,
  # because a `| while` loop runs in a subshell and its verdict variable never reaches the exit.
  carried_rows > "$CARRIED.now"
  awk -F'\t' -v pinf="$CARRIED" '
    NR==FNR { if ($0 !~ /^[[:space:]]*(#|$)/) pin[$1]=$2; next }
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
    }' "$CARRIED" "$CARRIED.now"
  cstat=$?
  rm -f "$CARRIED.now"
  if [ "$cstat" != 0 ]; then
    echo "install-prefix: apply writes gov's bytes VERBATIM, so a carried tools/<kit>/ literal arrives"
    echo "install-prefix: unchanged in a target installed at another prefix and resolves to nothing"
    echo "install-prefix: there. Derive the path, or re-run --write-ratchet in the pass that earned"
    echo "install-prefix: the drop and commit the file."
    exit 1
  fi
  echo "install-prefix: carried-prefix clean — $(grep -c . "$CARRIED") recorded file(s), none rising"
fi
