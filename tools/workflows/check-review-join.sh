#!/usr/bin/env bash
# check-review-join.sh — the retirement gate for the ref-keyed verdict join.
#
#   bash <prefix>/workflows/check-review-join.sh          # every *.js under tools/ or .claude/workflows/ git can see
#   bash <prefix>/workflows/check-review-join.sh <file>…  # explicit files (the self-test's fixtures)
#
# Exit 0 = clean · 1 = a ref-keyed join reappeared · 2 = THIS GATE REFUSED.
#
# A 2 is never a finding about the code under it. It means this gate declined to return a verdict:
# not a git repo, the predicate absent, node missing, the predicate returning a status this gate
# cannot classify, or the predicate exiting 2 without naming a line, which is its own refusal being
# handed up rather than a join. The last two arrived with the delegation and this line did not move
# with them - a stale exit-code contract is the same defect class as a stale pointer.
#
# WHAT THIS BANS AND WHY. A Tier-2 review harness joins each finding to its skeptic verdict. Keying
# that join on a `file:line` STRING the skeptic has to reproduce byte-for-byte has two failure modes,
# both of which shipped upstream and one of which was live in this kit:
#   * echo drift — a re-wrapped path or a re-derived line number misses the join, and the finding
#     silently leaves the count;
#   * COLLISION — two findings at one file:line (normal when two lenses read one function) collapse
#     into a single map entry, and BOTH inherit whichever verdict landed last.
# The class has no runtime signal — a mis-keyed harness reports a clean bill. Removing the selectable
# defective construct is the whole remedy, so this gate asserts the construct is gone.
#
# COMMENT STRIPPING IS LOAD-BEARING, not politeness. `tier2-review.js` explains the retired join in a
# comment that necessarily SPELLS the banned expression. A whole-file-text absence assertion would
# red on the documentation of its own fix — the exact trap recorded in the kickoff manifest's
# environment traps. Only code lines are judged.
#
# THE GATE IS OUTSIDE ITS OWN POPULATION for the same reason: this file holds every banned pattern
# verbatim in order to search for it. The population is `*.js`; this is `.sh`; and SELF_EXCLUDE below
# keeps that true if the gate is ever rewritten in JavaScript.
set -u
set -o pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "review-join: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

SELF_EXCLUDE='(^|/)check-review-join\.(sh|js|test\.sh)$'
# BASENAME-anchored, because the exclusion must travel with the population it scopes:
# parametrising one and not the other converts a fork into a red bar. Basename is the
# right form HERE -- these are individual FILES -- and the wrong form for the population,
# which is a subtree whose name is the thing that varies. See the parked decision.
# The ban table is check-review-join.js's since TOOL-dFairHearing-16, and that file is excluded by
# name: the retired-identifier ban is a bare regex literal, and a regex literal survives the literal
# blanking, so the predicate run over its own table returns one hit on exactly the table's line.
# The agent limit hook held the table from TOOL-dTieredTribunal-14 S6 until then, and left the exclusion
# with it; that hook retired in TOOL-dBoundRoles-25.

# ---- WHERE THIS KIT LIVES, DERIVED -- TOOL-dRetiredFork-10 ------------------------------------
# This script spells no install prefix. It is `tools/` here, `scripts/` at both measured adopters,
# and whatever the next one picks. Three carve-outs and three divergence rows existed for a path
# each script can work out from its own location.
#
# GIT COMPUTES THE REPO-RELATIVE PATH. This does NOT subtract `--show-toplevel` from `pwd`, which
# is the obvious spelling and is broken on MSYS: `pwd` yields /c/projects/... while
# `--show-toplevel` yields C:/projects/..., so the subtraction leaves the string untouched and the
# population matches NOTHING. Measured during this unit -- population 0, no error, no diagnostic.
#
# An EMPTY prefix is a real layout, not a bug: a kit installed at the repository root has no
# prefix to strip, and the population is then every *.js the repo holds.
HERE="$(cd "$(dirname "$0")" && pwd)"
KIT_PREFIX="$(unset GIT_DIR GIT_WORK_TREE; cd "$HERE/.." && git rev-parse --show-prefix 2>/dev/null)"
KIT_PREFIX="${KIT_PREFIX%/}"
#
# THE PREFIX PLUS `.claude/workflows/` -- TOOL-aRepatriatedFork-4. Both adopters keep their review
# harnesses there, so a prefix-only population judged none of them and printed clean. It joins as a
# literal for the reason rung 3 below is one: the harness's own convention, not an install prefix.
# NOT `.claude/` wholesale: `.claude/hooks/` holds the ban tables that trip this predicate, and this
# gate applies no marker filter to keep them out (F1: it keeps the union rather than take one).
if [ -n "$KIT_PREFIX" ]; then
  POP_RE="^($KIT_PREFIX|\.claude/workflows)/.*\.js$"; POP_SAYS="$KIT_PREFIX/ or .claude/workflows/"
else
  POP_RE='\.js$'; POP_SAYS="the repository root"
fi

# ---- NO HOOK -- TOOL-dBoundRoles-25 -----------------------------------------------------------
# The predicate reads its views from this kit's `script-views.js`, beside check-review-join.js, and nothing
# from a hook (§8 F8), so this gate probes no hooks kit: the retired agent limit hook it once resolved
# through the install receipt and the `.claude/hooks/` rung is gone, and the views went with the rule.
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

EXPLAIN=0
ARGS=()
for a in "$@"; do
  case "$a" in
    --explain) EXPLAIN=1 ;;
    *) ARGS+=("$a") ;;
  esac
done
set -- ${ARGS[@]+"${ARGS[@]}"}

if [ "$#" -gt 0 ]; then
  FILES=$(printf '%s\n' "$@")
  EXPLICIT=1
else
  # --cached AND --others: a NEW workflow script is judged the moment it exists, not the moment
  # someone remembers to stage it. --exclude-standard keeps ignored files ignored, and that is the
  # escape hatch: a scratch .js you do not want judged is a .gitignore line, not an unstaged file.
  # This DOES change the landing boundary — <prefix>/push-main.sh gates on `git status --porcelain -uno`
  # and so deliberately permits untracked files at a push — which is the point: a banned join sitting
  # unstaged in the tree was previously invisible to the gate that exists to ban it.
  FILES=$(git ls-files --cached --others --exclude-standard -- '*.js' \
    | grep -E "$POP_RE" | grep -vE "$SELF_EXCLUDE" | LC_ALL=C sort -u || true)
  EXPLICIT=0
fi

if [ "$EXPLICIT" = 0 ] && [ -z "$FILES" ]; then
  echo "review-join: no JavaScript under $POP_SAYS — the population is empty, which is not a pass"
  exit 1
fi

# TOOL-dFairHearing-16 - THE PREDICATE MOVED AGAIN. It was the agent limit hook's rule 5 from
# TOOL-dTieredTribunal-14 S5, run here through the hook's `join` selector, and the owner's NT-27 made it
# this gate's alone: check-review-join.js beside this gate holds the three bans, their `why` text,
# which this gate's own self-test asserts, and the deny message, and nothing else carries the ban.
# Its views are this kit's script-views.js since TOOL-dBoundRoles-25 retired that hook, so the
# stripper still BLANKS string contents where the retired in-file scanner kept them. The retired
# tool's NAME is deliberately not written under this path: a reader grepping for it finds nothing.
SCAN=()
while IFS= read -r f; do [ -n "$f" ] && [ -f "$f" ] && SCAN+=("$f"); done <<<"$FILES"
if [ "${#SCAN[@]}" = 0 ]; then
  echo "review-join: none of the named files exist — nothing was scanned, which is not a pass"
  exit 1
fi

command -v node >/dev/null 2>&1 || { echo "review-join: node is not on PATH, so the predicate cannot run — refusing rather than passing"; exit 2; }
JOINJS="$HERE/check-review-join.js"
[ -f "$JOINJS" ] || { echo "review-join: no check-review-join.js beside this gate at $HERE — the ban table lives there, so a gate without it must say so, not pass"; exit 2; }

hits=""
for f in "${SCAN[@]}"; do
  out=$(node "$JOINJS" "$f" 2>&1) && rc=0 || rc=$?
  # This loop used to read "the predicate exited non-zero" as "rule 5 fired". Two symptoms, one root.
  # The hook exited 2 on its OWN environment refusal before any rule ran, and that message carries
  # no line starting with two spaces and L, so the sed emptied it and the gate printed a ref-keyed
  # join with a blank body - sending an operator off to rewrite a join that is not there. And a
  # builder that threw once fed empty stdin to a JSON.parse whose catch exits 0, so the file was
  # recorded CLEAN. A status this gate cannot interpret is a refusal, never a verdict: its own header
  # preaches that a probe which cannot move must say so, and it was the counterexample. The predicate
  # is check-review-join.js now: 1 is a join, 2 its own refusal (the hook's exports or the file
  # unreadable), and a 1 naming no line is a refusal too.
  if [ "$rc" != 0 ] && [ "$rc" != 1 ] && [ "$rc" != 2 ]; then
    echo "review-join: the predicate returned $rc on $f, which is neither clean nor a rule hit - refusing rather than reporting"
    printf '%s\n' "$out" | sed 's/^/    /'
    exit 2
  fi
  if [ "$rc" = 2 ]; then
    echo "review-join: the predicate exited 2 on $f, so that is its own refusal and not a join"
    printf '    %s\n' "${out//$'\n'/$'\n'    }"
    exit 2
  fi
  if [ "$rc" = 1 ]; then
    body=$(printf '%s' "$out" | sed -n '/^  L/,$p')
    if [ -z "$body" ]; then
      echo "review-join: the predicate exited 1 on $f without naming a line, so that is its own refusal and not a join"
      printf '%s\n' "$out" | sed 's/^/    /'
      exit 2
    fi
    hits="$hits$f:
$body
"
  fi
done

# ---- ARM 2 — the agent wave that silently drops itself -------------------------------------------
# TOOL-dRetiredFork-7, absorbed from adopter ic, whose registry declared these +117 lines a POPULATION
# REPATH. One stage EARLIER than arm 1: a harness fans out to N lens agents and drops the dead ones
# with a falsy filter. If nothing counts the wave's arity BEFORE that filter, an all-dead wave and an
# all-clean wave both arrive downstream as `[]`. Observed live in THIS kit's tier2-review:
# `clean: 0 findings` returned with agents_done 0 and four ENOTFOUND errors, from a run that read no
# code at all. It is the charter's "a guard that shares a variable with the thing it guards is not a
# guard" — `allFindings.length === 0` was the proxy for "the diff is clean" AND for "nothing ran".
#
# WHAT IT CAN AND CANNOT HONESTLY CLAIM, because a source scan cannot decide reachability and the
# first version of this arm pretended it could. That version keyed on an identifier matching
# `\w*Dead` and told the reader to "refuse to report clean while that count is non-zero" — a
# sentence about a property it never checked. Measured: a harness that KEPT the counter and its
# log(), deleted the early return and hard-coded `note: 'clean: 0 findings'` PASSED it; a CORRECT
# harness whose counter was named `deadLenses` went RED; and the same drop spelled `.filter((r) => r)`
# was not judged at all.
#
# So it decides only the two things a scan CAN decide, and says so in its own output:
#   1. the wave's arity is taken by a length SUBTRACTION into a named variable — the name is CAPTURED
#      from the assignment, never matched against a spelling; and
#   2. that same variable is READ elsewhere in the file — a count computed and never consulted is the
#      same silent pass wearing a number.
# The falsy drop is a FAMILY, recognised by BALANCING the filter argument's parentheses.
#
# BOTH ARE PER-FILE, NOT PER-WAVE. That is a real hole and it is stated in the output rather than
# left for a reader to discover.
arm2=$(awk -v explain="$EXPLAIN" '
  function strip(s,   n, i, c, d, out) {
    n = length(s); out = ""; i = 1
    while (i <= n) {
      c = substr(s, i, 1); d = substr(s, i, 2)
      if (inblk)  { if (d == "*/") { inblk = 0; i += 2 } else i++; continue }
      if (c == "\\") { out = out substr(s, i, 2); i += 2; continue }
      if (q != "") { if (c == q) q = ""; out = out c; i++; continue }
      if (d == "/*") { inblk = 1; i += 2; continue }
      if (d == "//") break
      if (c == "\"" || c == "'"'"'" || c == "`") { q = c }
      out = out c; i++
    }
    return out
  }

  # The falsy-drop FAMILY. The argument of every `.filter(` on the line is taken by BALANCING its
  # parentheses, then compared against the forms that mean "drop the falsy ones". Matching a single
  # spelling (`.filter(Boolean)`) is how `.filter((r) => r)` walked past the first version of this.
  function isfalsy(a,   p, b) {
    gsub(/^[ \t]+/, "", a); gsub(/[ \t]+$/, "", a)
    if (a == "Boolean") return 1
    if (!match(a, /^\(?[ \t]*[A-Za-z_$][A-Za-z0-9_$]*[ \t]*\)?[ \t]*=>/)) return 0
    p = substr(a, 1, RLENGTH); gsub(/[ \t()=>]/, "", p)
    b = substr(a, RLENGTH + 1); gsub(/[ \t]/, "", b)
    if (b == p) return 1                                        # (r) => r
    if (b == "!!" p) return 1                                   # (r) => !!r
    if (b == "Boolean(" p ")") return 1                         # (r) => Boolean(r)
    if (b == p "!=null" || b == p "!==null") return 1           # (r) => r !== null
    if (b == p "!=undefined" || b == p "!==undefined") return 1
    if (b == p "!==null&&" p "!==undefined") return 1
    return 0
  }
  function falsydrop(code,   s, start, i, n, c, depth, arg) {
    s = code
    while (match(s, /\.filter\(/)) {
      start = RSTART + RLENGTH
      depth = 1; i = start; n = length(s); arg = ""
      while (i <= n) {
        c = substr(s, i, 1)
        if (c == "(") depth++
        else if (c == ")") { depth--; if (depth == 0) break }
        arg = arg c; i++
      }
      if (isfalsy(arg)) return 1
      s = substr(s, start)
    }
    return 0
  }

  # Word-boundary occurrence count. Plain index() would count `deadLensesTotal` as a read of
  # `deadLenses`, and `x.lensesDead` as a read of the local — a property access is not this variable.
  function refs(line, name,   n, idx, before, after, cnt, rest) {
    cnt = 0; rest = line; n = length(name)
    while ((idx = index(rest, name)) > 0) {
      before = (idx == 1) ? "" : substr(rest, idx - 1, 1)
      after = substr(rest, idx + n, 1)
      if (before !~ /[A-Za-z0-9_$.]/ && after !~ /[A-Za-z0-9_$]/) cnt++
      rest = substr(rest, idx + n)
    }
    return cnt
  }

  FNR == 1 { inblk = 0; q = ""
    if (!(FILENAME in seenfile)) { seenfile[FILENAME] = 1; order[++nfiles] = FILENAME } }
  { code = strip($0)

    nl[FILENAME]++; L[FILENAME, nl[FILENAME]] = code
    if (code ~ /agent\(/) hasAgent[FILENAME] = 1
    if (falsydrop(code)) { drops[FILENAME] = 1; if (!dropline[FILENAME]) dropline[FILENAME] = FNR }
    # An arity taken by SUBTRACTION, bound to a name this scan CAPTURES rather than guesses.
    if (match(code, /(^|[^A-Za-z0-9_$.])(const|let|var)[ \t]+[A-Za-z_$][A-Za-z0-9_$]*[ \t]*=[^=]/) &&
        (code ~ /\.length[ \t]*-/ || code ~ /-[ \t]*[A-Za-z_$][A-Za-z0-9_$.]*\.length/)) {
      nm = substr(code, RSTART, RLENGTH)
      sub(/^[^A-Za-z_$]*/, "", nm); sub(/^(const|let|var)[ \t]+/, "", nm); sub(/[ \t]*=.*$/, "", nm)
      if (nm != "") { ncount[FILENAME]++; CN[FILENAME, ncount[FILENAME]] = nm }
    }
  }
  END {
    njudged = 0
    for (i = 1; i <= nfiles; i++) {
      f = order[i]
      judged = (hasAgent[f] && drops[f]) ? 1 : 0
      best = 0; bestname = ""
      for (k = 1; k <= ncount[f]; k++) {
        r = 0
        for (m = 1; m <= nl[f]; m++) r += refs(L[f, m], CN[f, k])
        if (explain) printf "EXPLAIN     counter %s — read %d time(s) in code (1 = the assignment alone)\n", CN[f, k], r
        if (r > best) { best = r; bestname = CN[f, k] }
      }
      if (explain)
        printf "EXPLAIN %s — agent(%d) falsy-drop(%d) => %s · %d arity counter(s), best read %d\n",
          f, hasAgent[f] ? 1 : 0, drops[f] ? 1 : 0, judged ? "JUDGED" : "not judged", ncount[f] + 0, best
      if (judged) njudged++
      if (!judged) continue
      if (ncount[f] == 0)
        print "LIVE " f ":" dropline[f] ": drops dead agents with a falsy filter and never counts them"
      else if (best < 2)
        print "LIVE " f ":" dropline[f] ": counts the dead agents (" bestname ") but never reads the count"
    }
    # UNCONDITIONAL, and that is the point: the first cut derived this from the EXPLAIN lines,
    # which only exist under --explain, so the liveness refusal fired on every ordinary run.
    # A counter that exists only in debug output is not a counter.
    nagent = 0
    for (i = 1; i <= nfiles; i++) if (hasAgent[order[i]]) nagent++
    print "JUDGED " njudged
    print "AGENTFILES " nagent
  }' "${SCAN[@]}")

st=0
if [ -n "$hits" ]; then
  echo "review-join: FAILED — a ref-keyed verdict join reappeared. Key the join on the integer id the"
  echo "review-join: orchestrator assigns before the skeptic sees the finding (tier2-review.js)."
  printf '%s\n' "$hits" | sed 's/^/    /'
  st=1
fi

live=$(printf '%s\n' "$arm2" | sed -n 's/^LIVE //p')
judged=$(printf '%s\n' "$arm2" | sed -n 's/^JUDGED //p' | head -1)
judged=${judged:-0}
agentfiles=$(printf '%s\n' "$arm2" | sed -n 's/^AGENTFILES //p' | head -1)
agentfiles=${agentfiles:-0}

if [ "$EXPLAIN" = 1 ]; then
  # Section 5 observability, behind --explain and NOT in the default run: AC1 requires this gate's
  # ordinary output to stay byte-identical to its pre-change run, so an unconditional new line would
  # fail the very criterion it was added to serve. The resolution is fully visible here instead.
  echo "review-join: --explain — predicate at $JOINJS over the views of $HERE/script-views.js, population under $POP_SAYS"
  echo "review-join: --explain — the population, and why each file is or is not judged:"
  printf '%s\n' "$arm2" | sed -n 's/^EXPLAIN /    /p'
fi

if [ -n "$live" ]; then
  echo "review-join: FAILED — a harness drops dead agents with a falsy filter and never counts them,"
  echo "review-join: so an all-dead wave returns the same '0 findings' as a genuinely clean run. Bind"
  echo "review-join: the wave and take its arity BEFORE the filter — const dead = LENSES.length -"
  echo "review-join: live.length — then let that count decide what the run is allowed to call itself."
  echo "review-join: SCOPE — this gate checks only that the count EXISTS and IS READ, per FILE rather"
  echo "review-join: than per WAVE. It is a source scan: it CANNOT see whether the count guards the"
  echo "review-join: clean note, nor that a SECOND wave is counted too."
  printf '%s\n' "$live" | sed 's/^/    /'
  st=1
fi

# S3 — THE LIVENESS ASSERTION. An arm that judged NOTHING reports the same clean line as one that
# judged everything and found nothing, and this arm's population is a SUBSET of the scanned files:
# a file is judged only if it both dispatches agents and drops them falsily. So a refactor that
# renames `agent(` or moves every harness out of the population silently retires the arm while the
# gate keeps saying clean. Measured at absorption: 7 files scanned, 3 judged.
# TIGHTENED after the first cut broke a legitimate arm. "No harness in this tree" and "harnesses
# here and none of them judged" are different facts, and only the second is a liveness failure:
# a fixture tree with no agent dispatch at all has nothing for arm 2 to measure and saying so is
# correct. What must never pass silently is a tree that DOES dispatch agents while arm 2 judges
# none of it — that is the arm being retired by a refactor without anyone noticing.
if [ "$EXPLICIT" = 0 ] && [ "$agentfiles" != 0 ] && [ "$judged" = 0 ]; then
  echo "review-join: REFUSED — $agentfiles file(s) dispatch agents and arm 2 judged NONE of them."
  echo "review-join: dispatch agents and drop them with a falsy filter, and none matched, so this"
  echo "review-join: run measured nothing and a clean line would report coverage that does not exist."
  echo "review-join: Run with --explain to see why each file was excluded."
  exit 2
fi

[ "$st" = 0 ] || exit 1
echo "review-join: clean — no ref-keyed verdict join under $POP_SAYS, and every agent wave that this"
echo "review-join: scan can judge is counted ($judged file(s) judged by arm 2)."
echo "review-join: NOT CHECKED HERE (this is a source scan): that the count actually GUARDS the clean"
echo "review-join: note, and that a SECOND wave is counted too — the counters are tallied per FILE."
