#!/usr/bin/env bash
# run-selftests.sh — the self-tests, ON DEMAND, and a cost verdict for each. TOOL-aQuenchedHarness-4.
#
# THE SPLIT THIS RESTS ON, owner ruling 2026-08-23. Two kinds of check live in this repo's kits and
# they have different subjects. A RECORD-OR-WIRING check reads the REPOSITORY and can go stale with
# nobody editing a kit, so it stays a merge-bar leg. A SELF-TEST reads the KIT — it stages a break
# into a copy of a checker and asserts the checker still catches it — so it has a job only when the
# source under that kit changes, and none at all in a tree that copy-installs the kit and never edits
# it. `tools/unattended/run-unattended-gates.sh` took that ruling for ONE kit. This is the same thing
# for every kit, which is what the ruling always implied and nobody had built.
#
# WHAT IS THEREFORE NOT COVERED, said plainly because an exemption is not coverage (charter §7):
# nothing runs these automatically. A change under a kit that guts a check lands green. The
# compensating check is a person invoking this script, and the Definition of Done for any work
# touching a kit is a GREEN verdict from it pasted into the landing report.
#
# AND THE COST OF THAT, said just as plainly, because it is the argument for units 5 and 6 rather
# than an aside: the declared budgets sum to more leg-seconds than anyone will sit through, and
# `--list` prints the figure rather than this comment carrying one -- a number typed beside the
# declarations that own it is the defect this same file names sixty lines down, and it had
# already gone 30% stale before the closing review caught it. Nobody runs a check measured in
# hours, which is why `TOOL-aQuenchedHarness-9` exists — `govkit selftest` sat
# with two arms red for long enough that nobody can say when they broke.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || {
  echo "run-selftests: not a git work tree"; exit 2; }
cd "$ROOT" || exit 2
# THIS SCRIPT'S OWN REPO-RELATIVE PATH, DERIVED. Spelling it as a literal would ship gov's
# prefix into an adopter installed elsewhere, where it resolves to nothing -- the install-prefix
# ban, which this file is graded by. An empty derivation REFUSES rather than printing `bash `.
SELF="$(git -C "$(dirname -- "$0")" rev-parse --show-prefix 2>/dev/null)$(basename -- "$0")"
[ -n "$SELF" ] || { echo "run-selftests: cannot derive this script's own path" >&2; exit 2; }

BUDGETS="$HERE/selftest-budgets.txt"
LEGS="${GATE_LEGS:-$ROOT/tools/gate-legs.json}"
# The python-launcher resolver, INLINED byte-identically from the canonical copy named on
# the marker line below, for
# the reason the sibling runner states: this kit is deployable and tools/lib/ is gov-internal.
# The line this replaces used `command -v`, which the MS-Store python3 stub answers before
# exiting 9009 -- the exact idiom the resolver-parity gate bans, and it had been red on it.
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
PYBIN=$(resolve_python) || { echo "run-selftests: no usable python"; exit 2; }

print_usage() {
  cat <<'USAGE'
usage: bash tools/run-gates/run-selftests.sh (--serial|--pooled [--calibrate [--reset <row>]]) [--kit <dir>] | --check | --list | --rank
  --serial    run the declared population ONE suite at a time, time each against
              its own budget, RED on a breach. The only mode that issues a cost
              verdict, because an uncontended clock is the only one that can grade
              a budget.
  --pooled    the same population through a bounded OUTER pool, so the wall clock
              falls toward the longest suite instead of the sum of all of them.
              It answers ONE question -- did every suite run to its own end and
              MATCH its calibrated baseline (rc, ^FAIL count, executed count),
              which is PARITY -- and issues NO cost verdict at all: every reading
              it takes is contended by the other suites, and a contended clock
              cannot grade a budget. Use --serial for that. A red-by-design suite
              that completed and matched is GREEN here; a crash, a kill, a wall,
              an unrun or an unstarted row is RED. Each row's HANG bound is
              max(serial budget, worst calibrated reading) plus ceiling-margin.txt's
              headroom, read from selftest-pooled-evidence.txt under this node and
              the run's condition token; a row with NO reading REFUSES the run by
              name and nothing executes. SELFTEST_OUTER_WIDTH overrides the outer
              width (clamped to the resolved one); SELFTEST_WALL overrides the run
              bound and is REFUSED below the largest per-suite bound. --sweep is an
              alias, kept so every recorded invocation still runs.
              IT PAYS IN PROPORTION TO HOW UNDOMINATED THE POPULATION IS. The wall
              clock cannot fall below the longest member, so a selection of three
              suites where one holds most of the time is a LOSS — measured at 56s
              serial against 62s pooled. Nine suites measured 1692s against 981s.
  --calibrate with --pooled ONLY: run every selected row under ONE wall, the SUM
              of their serial budgets, grade NOTHING, and write each completed
              row's reading (worst seconds, monotone; rc, FAIL and executed
              counts, latest) to selftest-pooled-evidence.txt. A row the wall
              killed, whose output carries no trailer, or whose output carries
              the no-baseline sentinel (a batched group with no expected set yet)
              writes NO reading and reds the calibrate; an UNSOUND run (pool over
              its bound, fingerprint not taken or changed) writes NOTHING and
              says so. Every row's output is kept under
              <git-dir>/gate-logs/selftests/ and the path printed on each row
              that is not ok. Off --pooled it REFUSES.
  --reset <row>  with --pooled --calibrate ONLY: drop that row's reading, run
              ONLY the reset rows, and write the new seconds even when lower — the
              one path that lowers a bound. Off --calibrate, or naming a row the
              evidence file lacks, it REFUSES.
  (no mode)   REFUSED. A run that executes a suite declares --serial or --pooled;
              a silent default in either direction is a verdict nobody asked for.
  --kit <dir> only the suites whose argv lies under <dir>; a filter matching
              nothing is a REFUSAL, because an unknown filter and a clean sweep
              are indistinguishable from outside
  --check     the gate: assert the declaration against tools/gate-legs.json in
              BOTH directions, the pooled evidence's shape, and — over the rows
              under each `# pooled-kit:` the evidence header declares — that a
              row's script prints its trailer OUTSIDE a `[ "$<var>" = 0 ] &&` guard
              unless declared `# no-trailer:`, because a green-only trailer is
              UNTRAILED under --pooled the moment the suite reds; run nothing;
              takes no mode and no --kit
  --list      print the population and the derived total, run nothing; no mode
  --rank      rank the population by its RECORDED seconds and mark the set that
              carries the declared majority share; REFUSES if any row's reading
              states no condition, because ranking two conditions together ranks
              the conditions; takes no mode
USAGE
}

# `run` IS THE UNDECLARED STATE, NOT A MODE. Nothing below executes a suite under it: the refusal
# past the --list exit turns it away, so the serial loop at the bottom is reached only by --serial
# and the pool only by --pooled. TOOL-aBatchedArm-4 S2.
MODE=run; FILTER=""; CALIBRATE=0; RESETS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --kit)   FILTER=${2:-}; shift 2 ;;
    --check) MODE=check; shift ;;
    --list)  MODE=list; shift ;;
    --rank)  MODE=rank; shift ;;
    --serial) MODE=serial; shift ;;
    # ONE BRANCH, TWO SPELLINGS. --sweep is the name every recorded invocation carries and --pooled
    # is the declared mode; an alias that kept its own branch would be two answers to one question.
    --pooled|--sweep) MODE=sweep; shift ;;
    # THE BOOTSTRAP IS A DECLARED MODE, not a fallback. TOOL-aBatchedArm-5 S2: the evidence shape
    # cannot bound a row nobody has observed, so the first observation is taken under a wall that
    # says it is calibrating and grades nothing. It is a modifier of --pooled and of nothing else,
    # and --reset is a modifier of it; both refusals sit right below the loop so that
    # `--serial --calibrate`, `--check --calibrate` and a bare `--calibrate` execute NOTHING.
    --calibrate) CALIBRATE=1; shift ;;
    --reset) [ -n "${2:-}" ] || { echo "run-selftests: --reset takes a row name"; exit 2; }
             RESETS+=("$2"); shift 2 ;;
    -h|--help) print_usage; exit 0 ;;
    *) echo "run-selftests: unknown argument '$1'"; print_usage; exit 2 ;;
  esac
done
if [ "$CALIBRATE" = 1 ] && [ "$MODE" != sweep ]; then
  echo "run-selftests: --calibrate modifies --pooled and nothing else, and was given with '$( [ "$MODE" = run ] && echo "no mode" || echo "--$MODE" )'." >&2
  echo "run-selftests: A calibrate that ran the serial loop, or the gate, and wrote nothing would be" >&2
  echo "run-selftests: silent in a mode whose whole point is announcing itself. Nothing was run." >&2
  echo "run-selftests: Spell it: bash $SELF --pooled --calibrate [--kit <dir>]" >&2
  exit 2
fi
if [ "${#RESETS[@]}" -gt 0 ] && [ "$CALIBRATE" != 1 ]; then
  echo "run-selftests: --reset lowers a row's calibrated seconds and is a modifier of --calibrate," >&2
  echo "run-selftests: which was not given; a reset with no re-reading would leave the row unbounded" >&2
  echo "run-selftests: and say nothing. Nothing was run. Rows named: ${RESETS[*]}" >&2
  echo "run-selftests: Spell it: bash $SELF --pooled --calibrate --reset <row>" >&2
  exit 2
fi
# --check TAKES NO --kit, and the usage line says so. Its trailer arm iterates the population
# against a whole-file `# pooled-kit:` declaration, so a filter outside that kit made the gate red
# by selecting nothing — a false red on a manual invocation (aBatchedArm closing review R4).
# Refused by name here, beside the two refusals above, rather than filtered inside the arm.
if [ "$MODE" = check ] && [ -n "$FILTER" ]; then
  echo "run-selftests: --check grades the WHOLE declaration and takes no --kit, and was given '--kit $FILTER'." >&2
  echo "run-selftests: A filtered gate would red its trailer arm for selecting nothing outside the declared" >&2
  echo "run-selftests: pooled kit, or pass a filtered declaration off as the whole. Nothing was run." >&2
  echo "run-selftests: Spell it: bash $SELF --check" >&2
  exit 2
fi

[ -f "$BUDGETS" ] || { echo "run-selftests: no declaration at $BUDGETS"; exit 2; }

# ---- THE POOLED EVIDENCE, and the three readers of it. TOOL-aBatchedArm-5 S1, S2, S3 -------------
# ---- Siblings of this script, DERIVED as `$HERE/...` like the declaration above: a literal
# ---- kit path here would ship gov's prefix into an adopter installed elsewhere (the
# ---- install-prefix ban). The evidence file itself ships to NO adopter — it is a
# ---- `project-owned` row in this kit's descriptor, beside the declaration, for the same reason.
EVIDENCE="$HERE/selftest-pooled-evidence.txt"
MARGIN="$HERE/ceiling-margin.txt"
# THE TRAILER, ONE REGEX CONSTANT. A completed exit is a READING only when the filed output carries
# the suite's trailer — `PASS (` from the harness, the executed-count line from a shard, the shard
# leg's own line — because a red-by-design row exits 1 at 0.3 s on an unbound variable exactly as it
# does after 1300 s of work, and TOOL-aBatchedArm-3 AC4's ratified rule asks for an artifact of the
# work beside the exit (the `ab-arm-never-did-the-work` class).
SWEEP_TRAILER_RX='PASS \(|assertions executed|this leg ran shard'
# THE NO-BASELINE SENTINEL. A batched group whose expected signature set is still `"?"` prints
# `FAIL check_emitted: expected set not yet observed` and its observed set beneath, and the shard
# still prints its trailer — so a calibrate would fold those refusals into `fails` and the next
# --pooled would print parity GREEN over a suite that refused by name in every such group
# (aBatchedArm closing review D3). A hit is UNTRAILED at calibrate and MISMATCH under --pooled,
# so the landing order can never matter again. The phrase is the suite's own, verbatim.
SWEEP_NOBASELINE_RX='expected set not yet observed'

# THE NODE IS THE CHARTER'S §2 REGISTRY TAG, never a hostname, which the registry does not know:
# GOV_NODE when set, else USERNAME/USER matched against the registry table of the charter at the
# repo root — `AGENTS.md`, then `CLAUDE.md`, the precedent `run-gates.gov.test.sh` spells — with the
# row regex the drift audit's `_resolve_node_tag` uses (the registry's machine/user token is a
# SUBSTRING of the lowercased user). Prints the tag; returns 1 when no row
# matches, and the caller refuses BY NAME rather than falling back to a hostname.
_rs_reg_rx='^\|[[:space:]]*`([a-z])`[[:space:]]*\|[[:space:]]*`?([A-Za-z0-9_@.-]+)`?'
read_registry_tags() {  # every tag the registry table carries, one per line
  local f line
  for f in "$ROOT/AGENTS.md" "$ROOT/CLAUDE.md"; do
    [ -r "$f" ] || continue
    while IFS= read -r line; do
      [[ "$line" =~ $_rs_reg_rx ]] && printf '%s\n' "${BASH_REMATCH[1]}"
    done < "$f"
  done
}
resolve_node_tag() {
  if [ -n "${GOV_NODE:-}" ]; then
    # VALIDATED AGAINST THE SAME TABLE --check ENFORCES on the field it writes: an unregistered
    # GOV_NODE used to reach the evidence file verbatim, and the unguarded --check leg then redded
    # every bar on every node until the tracked file was hand-edited (aBatchedArm closing D11).
    # Refused by name, and the refusal is the caller's: return 2 is "set but not a tag".
    # ANCHORED, one tag per line: the space-joined `case` this replaced was a substring match,
    # so `GOV_NODE='a b'` — two adjacent registered tags — was accepted and written as a node
    # (aBatchedArm closing review R5, the `id-matched-as-a-substring` class).
    if read_registry_tags | grep -qxF -- "$GOV_NODE"; then printf '%s' "$GOV_NODE"; return 0; fi
    return 2
  fi
  local user=${USERNAME:-${USER:-}} f line tok
  user=${user,,}
  [ -n "$user" ] || return 1
  for f in "$ROOT/AGENTS.md" "$ROOT/CLAUDE.md"; do
    [ -r "$f" ] || continue
    while IFS= read -r line; do
      if [[ "$line" =~ $_rs_reg_rx ]]; then
        tok=${BASH_REMATCH[2],,}
        case "$user" in *"$tok"*) printf '%s' "${BASH_REMATCH[1]}"; return 0 ;; esac
      fi
    done < "$f"
  done
  return 1
}

# THE MARGIN, READ FROM THE FILE BESIDE THIS SCRIPT and REFUSED when absent — the rule
# `derive-ceilings.py` `read_margin` applies, reused as a RULE and not imported, because this runner
# is bash. Headroom over a bound's base is `max(<floor seconds>, <fraction> x base)`; a silent
# zero-margin default is a bound nobody chose. Sets MARGIN_FLOOR and MARGIN_FRAC.
read_margin() {
  [ -f "$MARGIN" ] || {
    echo "run-selftests: no margin declared at $MARGIN — a pooled hang bound with an undeclared" >&2
    echo "run-selftests: headroom is a number nobody chose. Refusing rather than defaulting; nothing was run." >&2
    return 1; }
  local line f1 f2
  while IFS= read -r line; do
    line=${line%$'\r'}
    case "$line" in ''|'#'*) continue ;; esac
    f1=${line%%$'\t'*}; f2=${line#*$'\t'}; f2=${f2%%$'\t'*}
    case "$f1" in ''|*[!0-9]*) continue ;; esac
    case "$f2" in ''|*[!0-9.]*) continue ;; esac
    MARGIN_FLOOR=$f1; MARGIN_FRAC=$f2; return 0
  done < "$MARGIN"
  echo "run-selftests: $MARGIN declares no <floor seconds>, tab, <fraction> row, so no headroom" >&2
  echo "run-selftests: could be derived. Nothing was run." >&2
  return 1
}

# THE EVIDENCE, READ ONCE AND EMITTED AS ROWS the shell loads into keyed arrays. Nine tab fields per
# row: name, condition token, node, max seconds, rc, fails, executed, readings, date. Emits
# `ROW<TAB>...` for a well-formed row, `BAD<TAB><line>:<why>` for one that does not parse (which
# `--check` reds by line and `--pooled` REFUSES on, naming the file), `DUP<TAB><line>:<key>` for a
# repeated (row, token, node) key, `NOTRAILER<TAB><row>` for each row the header declares as
# printing no trailer, and `POOLEDKIT<TAB><dir>` for each `# pooled-kit:` the header declares —
# the population --check's static trailer arm grades. An ABSENT file emits nothing: that is the
# bootstrap state --calibrate fills and --pooled refuses row by row.
read_evidence() {
  [ -f "$EVIDENCE" ] || return 0
  "$PYBIN" - "$EVIDENCE" <<'PY'
import re, sys
sys.stdout.reconfigure(newline="")
seen = {}
for n, raw in enumerate(open(sys.argv[1], encoding="utf-8"), 1):
    line = raw.rstrip("\r\n")
    s = line.strip()
    if not s:
        continue
    if s.startswith("#"):
        m = re.match(r"#\s*no-trailer:\s*(.+?)\s*$", s)
        if m:
            print("NOTRAILER\t" + m.group(1))
        m = re.match(r"#\s*pooled-kit:\s*(.+?)\s*$", s)
        if m:
            print("POOLEDKIT\t" + m.group(1))
        continue
    f = line.split("\t")
    if len(f) != 9:
        print("BAD\t%d:%d field(s), not 9" % (n, len(f)))
        continue
    name, cond, node, secs, rc, fails, executed, readings, date = f
    why = None
    if not name or not cond or not node or not date:
        why = "an empty name, condition, node or date"
    elif not (secs.isdigit() and rc.isdigit() and fails.isdigit() and readings.isdigit()):
        why = "seconds, rc, fails and readings must be integers"
    elif not (executed == "-" or executed.isdigit()):
        why = "executed must be an integer or '-'"
    elif int(readings) < 1:
        why = "readings is %s, and a row nobody has read is not evidence" % readings
    if why:
        print("BAD\t%d:%s" % (n, why))
        continue
    key = (name, cond, node)
    if key in seen:
        print("DUP\t%d:%s under %s on node %s (first at line %d)" % (n, name, cond, node, seen[key]))
        continue
    seen[key] = n
    print("\t".join(["ROW"] + f))
PY
}

# ---- --rank: which suites carry the cost, and therefore which are worth rebuilding -------------
# ---- It runs BEFORE the width resolution below, because ranking is a read of a text file and has
# ---- no business paying for a profile probe.
if [ "$MODE" = rank ]; then
  "$PYBIN" - "$BUDGETS" <<'PY'
import re, sys

# THE CONDITION VOCABULARY IS CLOSED, and that is the whole point of this verb. Spec 6 S3a: the
# readings in this file come from two sources under two conditions — retained `gate-run` windows for
# a held leg, and a direct timed invocation for a suite with no manifest row — so sorting them
# together ranks the CONDITIONS as much as the suites. A phrasing not listed here is not ranked
# leniently; it is reported as unbacked. Adding one is a deliberate edit, which is the point.
# CONTENDED READINGS ARE REFUSED, NOT RANKED. `--sweep` composes this token, so the emitter and this
# reader share one spelling; `run-selftests.test.sh` captures the tag from a real sweep and feeds it
# here, because a fixture that hand-types it on both sides observes nothing about the join.
REFUSED = [re.compile(r"pooled@")]

CONDS = [
    (re.compile(r"worst of (\d+) readings (\d+)s"),
     lambda m: (int(m.group(2)), "worst of %s gate-run windows" % m.group(1))),
    (re.compile(r"measured (\d+)s (?:on )?(.+?)(?:,|$)"),
     lambda m: (int(m.group(1)), "direct, %s" % m.group(2).strip())),
]

share = factor = None
rows, unbacked = [], []
for line in open(sys.argv[1], encoding="utf-8"):
    s = line.strip()
    if s.startswith("#"):
        m = re.match(r"#\s*port-majority-share:\s*([0-9.]+)", s)
        if m:
            share = float(m.group(1))
        m = re.match(r"#\s*port-minimum-factor:\s*([0-9.]+)", s)
        if m:
            factor = float(m.group(1))
        continue
    if not s:
        continue
    f = line.rstrip("\r\n").split("\t")
    if len(f) < 2:
        continue
    name, reading = f[0], (f[3] if len(f) > 3 else "")
    # REFUSED BEFORE THE RANKERS ARE OFFERED THE ROW, and the order is the whole mechanism. A CONDS
    # match is what RANKS a row -- the loop below breaks on the first hit and appends to `rows`, and
    # only the for/else fall-through reaches `unbacked`. So a pooled pattern added to CONDS would
    # make a contended reading RANK, the exact inverse of the intent; and the lenient `measured`
    # entry accepts any text after the seconds, so it would match `measured 42s pooled@8x1 on node
    # a` first anyway. Eleven rows in this file already use that spelling, three of them with a
    # width clause, so it is the likely spelling rather than a contrived one.
    #
    # What it buys: `--sweep` states its own condition and a reading taken under it can be pasted
    # into this file by any hand. Ranking it against serial ones is the ranking-the-conditions
    # defect TOOL-aQuenchedHarness-6 S3a exists to prevent, and nothing refused it until now.
    if any(rx.search(reading) for rx in REFUSED):
        unbacked.append((name, reading))
        continue
    for rx, take in CONDS:
        m = rx.search(reading)
        if m:
            secs, cond = take(m)
            rows.append((secs, cond, name))
            break
    else:
        unbacked.append((name, reading))

# A THRESHOLD THAT IS NOT DECLARED IS NOT A THRESHOLD. Defaulting it here would let the file lose its
# declaration and the ranking carry on reporting a selected set against a number nobody wrote.
missing = [k for k, v in (("port-majority-share", share), ("port-minimum-factor", factor)) if v is None]
if missing:
    print("run-selftests: the declaration states no " + " and no ".join(missing) + ", so a selected")
    print("run-selftests: set could not be computed against anything. Declare them in the header of")
    print("run-selftests: %s beside the reading each was taken from." % sys.argv[1])
    raise SystemExit(1)

if unbacked:
    print("run-selftests: these row(s) carry no reading whose CONDITION this verb recognises, so they")
    print("run-selftests: cannot be ranked against rows that do — and a denominator missing its")
    print("run-selftests: largest members is not a majority of anything. NO share was computed.")
    for name, reading in unbacked:
        print("  %-46s %s" % (name, reading or "(no reading at all)"))
    print("run-selftests: produce them with  GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh")
    print("run-selftests: and, for a row with no manifest leg, a direct timed run of its argv; then")
    print("run-selftests: write the seconds and the condition into this file's fourth column.")
    raise SystemExit(1)

if not rows:
    print("run-selftests: the declaration ranked NO row at all, so this verb graded nothing")
    raise SystemExit(2)

total = sum(r[0] for r in rows)
rows.sort(key=lambda r: (-r[0], r[2]))
print("run-selftests: %d row(s), %d s of recorded time; the declared majority share is %.0f%% and"
      % (len(rows), total, share * 100))
print("run-selftests: the declared minimum port factor is %.2fx." % factor)
cum, cut = 0, None
for i, (secs, cond, name) in enumerate(rows, 1):
    cum += secs
    frac = cum / float(total)
    mark = " "
    if cut is None and frac >= share:
        cut, mark = i, "<"
    print("  %2d  %6d s  cum %5.1f%% %s  %-30s  %s" % (i, secs, frac * 100, mark, cond, name))
print("----")
print("run-selftests: the declared share is carried by the TOP %d suite(s) — %d s of %d, %.1f%%."
      % (cut, sum(r[0] for r in rows[:cut]), total, sum(r[0] for r in rows[:cut]) / float(total) * 100))
PY
  exit $?
fi

# ---- the declaration, read once. Emitted as: STATE, name, budget, argv -- in that order.
# ---- A row whose argv is empty takes it from `tools/gate-legs.json`, so the manifest stays the one
# ---- place a held leg's command is written and this file carries only what the manifest cannot.
read_population() {
  "$PYBIN" - "$BUDGETS" "$LEGS" "$FILTER" <<'PY'
import json, sys

# LF, NOT CRLF, and this is a bug fix rather than tidiness. On Windows `print` translates every
# newline to CR LF, so each row below reached the shell with a trailing CR. It was INVISIBLE while
# the state was the LAST field -- `state` merely became "ok<CR>", and nothing compared it
# successfully anyway -- and it turned fatal the moment the argv moved last, because the final
# path token then carried the CR into `git ls-files` and every row read as untracked. Two defects
# hiding each other, and `run-selftests.test.sh` surfaced both on its first run.
sys.stdout.reconfigure(newline="")
budgets, legs_path, filt = sys.argv[1], sys.argv[2], sys.argv[3]
legs = {l["name"]: l for l in json.load(open(legs_path, encoding="utf-8"))}
for line in open(budgets, encoding="utf-8"):
    if not line.strip() or line.lstrip().startswith("#"):
        continue
    f = line.rstrip("\r\n").split("\t")
    if len(f) < 2:
        continue
    name, budget, argv = f[0], f[1], (f[2] if len(f) > 2 else "")
    # A BUDGET NOBODY CAN COMPARE IS NOT A BUDGET. An empty second column emitted `ok` for a row
    # whose argv then read back EMPTY -- the run loop `eval`'d nothing, got rc 0, and printed a
    # green line at 0s for a suite it never executed; and `[ "$took" -gt "$budget" ]` on a
    # non-number errors with `integer expression expected`, returns 2, and reads as "not over
    # budget", so the cost verdict went quiet too. Neither direction of `--check` could see it:
    # the forward one matches names and the reverse one iterates an empty argv zero times.
    if not budget.isdigit():
        print("\t".join(["BADBUDGET", name, budget, argv]))
        continue
    if not argv:
        leg = legs.get(name)
        if not leg:
            print("\t".join(["UNRESOLVED", name, budget, ""]))
            continue
        argv = " ".join(leg.get("argv", []))
    if filt and filt not in argv:
        continue
    print("\t".join(["ok", name, budget, argv]))
PY
}

# ---- THE WIDTH IS RESOLVED ONCE, BY THE BAR'S OWN RESOLVER. Detection, the profile table, the clamp
# ---- and the GATE_JOBS override are 200 lines inside `run-gates.sh`; re-implementing them here is
# ---- the two-spellings drift this repo gates elsewhere. `--print-profile` exits before the
# ---- turnstile, so asking costs nothing and takes no beacon.
W=$(bash "$HERE/run-gates.sh" --print-profile 2>/dev/null | awk -F'\t' '$1=="width"{print $2}')
case "${W:-}" in ''|*[!0-9]*) W=2 ;; esac
# THE COMPOSITE BOUND: outer x inner never exceeds the profile row's declared width. A spec audit
# caught this unit and the harness unit each reading that width independently, which at width 8 would
# be 8 suites x 8 arms = 64 concurrent processes on a host where a bare spawn costs 319 ms.
#
# THE OUTER POOL IS 1 UNDER --serial, because that loop is serial on purpose: it grades each
# suite against its OWN declared budget, so two suites racing would charge each of them the other's
# contention and a breach would name the wrong one. An earlier draft divided by a pool of 4 that does
# not exist, which handed every ported suite a quarter of the width it was entitled to — measured on
# `check-line-length.test.sh`: 13.6 s at the width that division produced against 7.9 s at the
# declared one. The invariant is the PRODUCT, not the constant.
#
# `--sweep` IS THE RE-DIVISION that comment always anticipated (TOOL-aPooledSweep-1). It runs the
# suites concurrently and therefore issues no cost verdict at all, which is what makes the trade
# sound rather than a shortcut: the contention that would have misattributed a breach is admitted,
# and the breach is simply not claimed. Outer takes the whole width there and inner falls to 1,
# because THREE of the population's suites source the selftest harness and the other
# fifty-six have no inner width to spend — so inner parallelism buys 3/59ths of the work and outer
# buys all of it.
OUTER=1
if [ "$MODE" = sweep ]; then
  OUTER=$W
  # THE OVERRIDE IS CLAMPED. The invariant is the product, so a knob that could exceed it would be a
  # knob for breaking the one rule this block exists to keep.
  case "${SELFTEST_OUTER_WIDTH:-}" in
    '') : ;;
    *[!0-9]*|0)
      # NOT SILENTLY DISCARDED. An ignored knob leaves the operator believing a width they never
      # got, and the run then prints a pair that agrees with itself and with nothing they asked for.
      echo "run-selftests: SELFTEST_OUTER_WIDTH is '$SELFTEST_OUTER_WIDTH', which is not a positive" >&2
      echo "run-selftests: integer, so the width you asked for could not be applied. Nothing was run." >&2
      exit 2 ;;
    *) # BASE TEN, FORCED. `08` and `007` pass the digit test above and then read as OCTAL in
       # arithmetic, where `08` is not a number at all — the refusal is bypassed and the failure
       # lands somewhere else entirely.
       OUTER=$((10#$SELFTEST_OUTER_WIDTH))
       [ "$OUTER" -ge 1 ] || { echo "run-selftests: SELFTEST_OUTER_WIDTH resolves to $OUTER" >&2; exit 2; }
       [ "$OUTER" -le "$W" ] || OUTER=$W ;;
  esac
fi
export SELFTEST_INNER_WIDTH=$(( W / OUTER )); [ "$SELFTEST_INNER_WIDTH" -ge 1 ] || SELFTEST_INNER_WIDTH=1

POP=$(read_population)
NROWS=$(printf '%s' "$POP" | grep -c . || true)

# ---- --check: the gate. BOTH DIRECTIONS, because one alone cannot fail usefully -----------------
if [ "$MODE" = check ]; then
  fails=0
  # FORWARD: every leg the bar holds carries a row. A suite that arrives without one would be exempt
  # from the budget rule by the act of arriving.
  missing=$("$PYBIN" - "$BUDGETS" "$LEGS" <<'PY'
import json, sys
declared = set()
for line in open(sys.argv[1], encoding="utf-8"):
    if line.strip() and not line.lstrip().startswith("#"):
        declared.add(line.split("\t")[0])
for l in json.load(open(sys.argv[2], encoding="utf-8")):
    if (l.get("subject") == "kit" or l.get("chunk") == "selftests") and l["name"] not in declared:
        print(l["name"])
PY
)
  if [ -n "$missing" ]; then
    echo "run-selftests: these HELD legs carry no budget row, so their cost is unbounded by declaration:" >&2
    # QUOTED, and printed line-wise: a leg name has spaces in it, so an unquoted $missing
    # word-splits and reports `agent-cap self-test` as two missing legs.
    printf '%s\n' "$missing" | sed 's/^/  /' >&2
    fails=1
  fi
  # REVERSE: a row that is not a held leg must name a TRACKED file, or the declaration is a way to
  # name a suite that does not exist — and a population nobody can execute grades nothing.
  while IFS=$'\t' read -r state name budget argv; do
    [ -n "${name:-}" ] || continue
    if [ "$state" = UNRESOLVED ]; then
      echo "run-selftests: row '$name' has no argv and no leg of that name in the manifest" >&2
      fails=1; continue
    fi
    if [ "$state" = BADBUDGET ]; then
      echo "run-selftests: row '$name' declares a budget that is not a number ('$budget'), so its cost verdict could never fire" >&2
      fails=1; continue
    fi
    for tok in $argv; do
      case "$tok" in
        */*)
          # A NUMERIC RATIO IS A SHARD TOKEN, NOT A PATH. `--shard 1/8` carries a slash and is what a
          # sharded row's argv says, so it must not be handed to `git ls-files`. TOOL-aBatchedArm-4 S1.
          # A REGEX, deliberately: the glob `[0-9]*/[0-9]*` reads as ONE digit then anything, so a
          # digit-led directory name would slip past the tracked-path check — staged and proven.
          [[ "$tok" =~ ^[0-9]+/[0-9]+$ ]] && continue
          git ls-files --error-unmatch -- "$tok" >/dev/null 2>&1 \
               || { echo "run-selftests: row '$name' names '$tok', which git does not track" >&2; fails=1; } ;;
      esac
    done
  done <<EOF
$POP
EOF
  # ---- THE SHARD JOIN, ported from the gov canary's shard contract (run-gates.gov.test.sh, the
  # ---- text `shard contract`) to this file's row format. TOOL-aBatchedArm-3 S4. FORWARD HALF ONLY:
  # ---- a script any row calls with `--shard i/n` is called at ONE arity, and its indices 1..n are
  # ---- each declared exactly once — a missing index is a region nobody runs while the other seven
  # ---- rows report green, which is green-by-absence one row at a time. The canary's REVERSE half
  # ---- ("declares SHARD_ARITY but is called whole") is deliberately NOT ported: the driver suite
  # ---- declares an arity and is called whole here on purpose, so that half would red a row this
  # ---- declaration is right to carry. Scoped to rows that carry `--shard`, so it never reads that
  # ---- row. WHAT IT DOES NOT CHECK: that a shard runs the region it claims — only the suite's own
  # ---- per-mode floor sees that. Run over the real tree before it was wired: 0 sharded scripts.
  shard_faults=$(printf '%s\n' "$POP" | awk -F'\t' '
    { n = split($4, t, " ")
      for (i = 1; i <= n; i++) if (t[i] == "--shard") {
        s = "?"; for (j = 1; j <= n; j++) if (t[j] ~ /\.(sh|py)$/) { s = t[j]; break }
        v = (i < n) ? t[i + 1] : ""
        if (v !~ /^[0-9]+\/[0-9]+$/) { print "row " $2 " carries a malformed --shard value " v; next }
        split(v, p, "/")
        if (!(s in arity)) { arity[s] = p[2]; order[++k] = s }
        else if (arity[s] != p[2]) multi[s] = multi[s] " " p[2]
        seen[s, p[1]]++
      } }
    END {
      for (q = 1; q <= k; q++) { s = order[q]; a = arity[s]
        if (s in multi) { print s " is called with more than one shard arity: " a multi[s]; continue }
        miss = ""; dup = ""; wide = ""
        for (j = 1; j <= a; j++) { if (!((s, j) in seen)) miss = miss " " j; else if (seen[s, j] > 1) dup = dup " " j }
        for (key in seen) { split(key, kk, SUBSEP); if (kk[1] == s && (kk[2] + 0 < 1 || kk[2] + 0 > a)) wide = wide " " kk[2] }
        if (miss != "") print s " declares arity " a " but the declaration carries no row for index" miss " — every index 1.." a " is a region, and one nobody runs is green by absence"
        if (dup != "") print s " declares arity " a " but index" dup " is declared more than once, so one region is graded twice and paid twice"
        if (wide != "") print s " declares arity " a " but the declaration carries index" wide ", outside 1.." a
      } }')
  if [ -n "$shard_faults" ]; then
    echo "run-selftests: the shard join fails — a script called with --shard must be called at one arity with every index 1..n declared once:" >&2
    printf '%s\n' "$shard_faults" | sed 's/^/  /' >&2
    fails=1
  fi
  # ---- THE POOLED EVIDENCE'S SHAPE. TOOL-aBatchedArm-5 S3. A hand-edited, truncated or orphaned
  # ---- row reds HERE, on the unguarded bar leg: nine tab fields, the numbers parse, readings is at
  # ---- least one, the node is a tag the registry table carries, no (row, token, node) key repeats,
  # ---- and every row names a row the declaration declares — an ORPHAN is the right red, because a
  # ---- deleted budget row takes its evidence with it or the file lies. WHAT IT DOES NOT CHECK:
  # ---- that any reading is true, or that the population --pooled reaches is calibrated; the
  # ---- pooled run refuses that by name at run time. An ABSENT file is announced and is not a
  # ---- red: the file ships to no adopter, and --pooled refuses every row until --calibrate
  # ---- writes one, which is the announced-unarmed state.
  if [ -f "$EVIDENCE" ]; then
    ev_tags=$(read_registry_tags)
    ev_rows=0; ev_faults=""; ev_nt="|"; ev_kits=""
    # READ ONCE INTO A VARIABLE and feed the loop from that: a heredoc holding a command
    # substitution is the shape the shell-hygiene leg gates (a loop that can wait for an EOF that
    # never arrives), and the population loops feed from $POP the same way.
    EV_TEXT=$(read_evidence)
    while IFS=$'\t' read -r kind a b c _rest; do
      [ -n "${kind:-}" ] || continue
      case "$kind" in
        NOTRAILER) ev_nt="$ev_nt$a|"; continue ;;
        POOLEDKIT) ev_kits="$ev_kits $a"; continue ;;
        BAD) ev_faults="$ev_faults"$'\n'"  line $a" ;;
        DUP) ev_faults="$ev_faults"$'\n'"  line $a — the (row, token, node) key repeats" ;;
        ROW)
          ev_rows=$((ev_rows + 1))
          # ANCHORED, the same comparison `resolve_node_tag` makes on the write path (R5).
          if ! printf '%s\n' "$ev_tags" | grep -qxF -- "$c"; then
            ev_faults="$ev_faults"$'\n'"  row '$a' under $b names node '$c', which is no tag the charter's registry table carries"
          fi
          # AGAINST THE WHOLE DECLARATION, not the --kit-filtered population: a row outside a
          # filter is declared all the same, and reading it as an orphan would red a true file.
          if ! awk -F'\t' -v n="$a" '/^[[:space:]]*#/ { next } NF >= 2 && $1 == n { hit = 1 } END { exit hit ? 0 : 1 }' "$BUDGETS"; then
            ev_faults="$ev_faults"$'\n'"  row '$a' under $b is an ORPHAN — the declaration carries no row of that name, so its evidence bounds nothing"
          fi ;;
      esac
    done <<EOF
$EV_TEXT
EOF
    if [ -n "$ev_faults" ]; then
      echo "run-selftests: the pooled evidence at $EVIDENCE is malformed — every row is nine tab fields (row, condition, node, seconds, rc, fails, executed, readings, date), keyed once, on a registry tag, naming a declared row:" >&2
      printf '%s\n' "$ev_faults" | grep . >&2
      fails=1
    fi
    ev_note=", $ev_rows pooled evidence row(s) well-formed"
    # ---- THE TRAILER RULE, STATICALLY, before anyone pays for a calibrate. aBatchedArm closing
    # ---- review D4: five of the seven non-shard kit rows printed their only trailer under
    # ---- `[ "$st" = 0 ] &&`, three of them red by design, so the calibrate would have rendered
    # ---- them UNTRAILED, written no reading, and every later --pooled would have refused the whole
    # ---- population — a 5.7 h serial-sum wall declared over rows that could never reach parity.
    # ---- SCOPED to the rows under each `# pooled-kit:` the evidence header declares: run as a
    # ---- candidate over the WHOLE declaration first, it named 34 of 69 rows that print no trailer
    # ---- at all because they are not on the pooled route, and a gate that reds innocent rows is
    # ---- not a gate. A row declared `# no-trailer:` is skipped. WHAT IT DOES NOT CHECK: a trailer
    # ---- behind a guard that is not a `[ "$<var>" = 0 ] &&` prefix, a trailer printed by a file the script sources,
    # ---- or that the print is reached — the calibrate's UNTRAILED verdict is the runtime half.
    # ---- No pooled-kit declared is ANNOUNCED, never a silent skip.
    if [ -n "$ev_kits" ]; then
      tr_graded=0; tr_skipped=0; tr_faults=""
      while IFS=$'\t' read -r state name budget argv; do
        [ "${state:-}" = ok ] || continue
        tr_in=0; for kd in $ev_kits; do case "$argv" in *"$kd"*) tr_in=1 ;; esac; done
        [ "$tr_in" = 1 ] || continue
        case "$ev_nt" in *"|$name|"*) tr_skipped=$((tr_skipped + 1)); continue ;; esac
        tr_script=""; for tok in $argv; do case "$tok" in *.sh|*.py) tr_script=$tok; break ;; esac; done
        tr_graded=$((tr_graded + 1))
        if [ -z "$tr_script" ] || [ ! -f "$tr_script" ]; then
          tr_faults="$tr_faults"$'\n'"  row '$name' names no script this arm can read, so its trailer is unknown"
        elif ! grep -vE '^[[:space:]]*#' "$tr_script" | grep -E "$SWEEP_TRAILER_RX" | grep -qvE '^[[:space:]]*\[ "\$[A-Za-z_]+" = 0 \] &&'; then
          tr_faults="$tr_faults"$'\n'"  row '$name': $tr_script prints no trailer outside a [ \"\$<var>\" = 0 ] && guard, so a red-but-complete run is UNTRAILED under --pooled and writes no reading"
        fi
      done <<EOF
$POP
EOF
      if [ -n "$tr_faults" ]; then
        echo "run-selftests: the trailer rule fails under pooled-kit$ev_kits — every row's script must print a trailer ($SWEEP_TRAILER_RX) unconditionally, or be declared no-trailer in $EVIDENCE:" >&2
        printf '%s\n' "$tr_faults" | grep . >&2
        fails=1
      fi
      [ "$tr_graded" -gt 0 ] || { echo "run-selftests: pooled-kit$ev_kits selects NO row, so the trailer arm graded nothing" >&2; fails=1; }
      ev_note="$ev_note, trailer arm graded $tr_graded row(s) under pooled-kit$ev_kits ($tr_skipped declared no-trailer)"
    else
      ev_note="$ev_note, no pooled-kit declared so the trailer arm graded NOTHING"
    fi
  else
    echo "run-selftests: no pooled evidence at $EVIDENCE, so the evidence-shape arm graded NOTHING — --pooled refuses every row until --pooled --calibrate writes one"
    ev_note=", no pooled evidence file"
  fi
  [ "$NROWS" -gt 0 ] || { echo "run-selftests: the declaration is EMPTY, so both directions above passed by finding nothing" >&2; fails=1; }
  [ "$fails" = 0 ] && echo "run-selftests: declaration clean — $NROWS row(s), every held leg budgeted, every row resolvable$ev_note"
  exit "$fails"
fi

# ---- the derived total. NEVER typed: a figure beside the declarations that own it goes stale on the
# ---- next edit and nobody notices.
TOTAL=$(printf '%s' "$POP" | awk -F'\t' '{s+=$3} END{print s+0}')
if [ "$MODE" = list ]; then
  printf '%s\n' "$POP" | awk -F'\t' '{printf "  %-46s %6ss  %s\n", $2, $3, $4}'
  printf 'run-selftests: %s row(s), declared total %ss (%s minutes) at width %s (outer %s, inner %s)\n' \
    "$NROWS" "$TOTAL" "$(( (TOTAL + 59) / 60 ))" "$W" "$OUTER" "$SELFTEST_INNER_WIDTH"
  exit 0
fi

# ---- THE MODE IS DECLARED, NEVER DEFAULTED. TOOL-aBatchedArm-4 S2. A run that executes a suite
# ---- says which clock it runs on: --serial grades budgets, --pooled withholds them. A silent
# ---- default in EITHER direction is a coupling nobody declared — the one caller that reports
# ---- cost read only the exit code, so a pooled default would have printed GREEN with every
# ---- budget withheld, and a serial default is the contract this refusal makes explicit.
# ---- IT SITS HERE, after --check and --list, which execute nothing and take no mode (--check is
# ---- the unguarded bar leg, and a refusal above it would red every bar), and BEFORE the
# ---- filter-liveness refusal below, because the mode is the invocation's shape and the filter
# ---- is its content: a wrong filter under a declared mode still reds by name.
if [ "$MODE" = run ]; then
  echo "run-selftests: no execution mode was given, and a run that executes a suite declares --serial or --pooled:" >&2
  echo "run-selftests:   --serial   one suite at a time, each graded against its own budget" >&2
  echo "run-selftests:   --pooled   a bounded outer pool, every cost verdict withheld" >&2
  echo "run-selftests: Nothing was run." >&2
  exit 2
fi

# ---- LIVENESS. A run that executed nothing must not print a green line: an unknown filter and a
# ---- clean sweep are indistinguishable from the outside, which is the class this kit's sibling
# ---- spent six review rounds on.
if [ "$NROWS" -eq 0 ]; then
  echo "run-selftests: no suite matched${FILTER:+ --kit $FILTER}, so this run graded NOTHING at all" >&2
  exit 2
fi

# ---- --sweep: the population through a bounded OUTER pool. TOOL-aPooledSweep-1 -----------------
# ---- It answers "did every suite run to its own end and match its calibrated baseline" — PARITY,
# ---- TOOL-aBatchedArm-5 S4 — and NOTHING about cost. The serial loop below is the only mode that
# ---- grades a budget, and that division is the whole reason this one is admissible.
if [ "$MODE" = sweep ]; then
  # THE BOUND IS A PROBED CAPABILITY, NOT AN ASSUMPTION, and its absence REFUSES rather than
  # degrading quietly. the selftest harness probes for `timeout` the same way and runs its
  # arms UNBOUNDED when it is missing, which is right for arms that are seconds long. Here the
  # missing binary deletes the whole property: this mode renders every verdict AFTER the pool
  # drains, so one non-returning suite suppresses all of them, which is strictly worse than the
  # serial loop it replaces.
  # RESOLVED BY NAME, over a candidate list, because coreutils ships as `gtimeout` under a prefix on
  # more than one platform and a hard-coded `timeout` would refuse those hosts for a spelling. The
  # list is overridable so an adopter can name a third; that override is also what gives this
  # refusal its failing case, which a hard-coded name has no honest way to stage.
  SWEEP_TIMEOUT=""
  for _cand in ${SELFTEST_TIMEOUT_BIN:-timeout gtimeout}; do
    command -v "$_cand" >/dev/null 2>&1 && { SWEEP_TIMEOUT=$_cand; break; }
  done
  [ -n "$SWEEP_TIMEOUT" ] || {
    echo "run-selftests: --pooled needs a 'timeout' binary to bound each suite and found none of:" >&2
    echo "run-selftests:   ${SELFTEST_TIMEOUT_BIN:-timeout gtimeout}" >&2
    echo "run-selftests: without one every suite below would run unbounded while this mode claims" >&2
    echo "run-selftests: each one is bounded, and a single hang would suppress all $NROWS verdict" >&2
    echo "run-selftests: lines. Use --serial, which reports each suite as it finishes." >&2
    exit 2; }

  # THE CONDITION, COMPOSED ONCE, and composed HERE because the evidence is keyed on it. Not
  # re-derived per row: the same fact spelled twice in a file whose own header names that defect.
  # It is printed in a stable shape because the `--rank` refusal matches this exact token, and the
  # arm that proves they agree captures it from here.
  SWEEP_CONDITION="pooled@${OUTER}x${SELFTEST_INNER_WIDTH}"

  # THE PER-SUITE BOUND IS EVIDENCE, NOT A FACTOR. TOOL-aBatchedArm-5 S1. The shape this replaces
  # bounded every row at `budget x sweep-ceiling-factor`, which killed 14 of 58 suites in the full
  # sweep of 2026-09-08 and which three records refused as a predictor (`TOOL-dRetiredFork-40`
  # measured 443 s under load against 583 s quiet — a multiplier gets it the wrong way round). The
  # bound is now `max(<serial budget>, <worst reading observed under THIS token on THIS node>)` plus
  # the declared headroom, monotone over whatever was observed. The serial-budget floor is the
  # guard against a fast red: a pooled row cannot legitimately need less than it costs alone, so a
  # 0.3 s refusal recorded as a reading never bounds a repaired suite below its serial budget. A
  # row with NO reading REFUSES the run by name — there is no fallback, because a fallback is the
  # bound that killed 14 of 58 — and the refusal names what to type.
  read_margin || exit 2
  SWEEP_NODE=$(resolve_node_tag) || {
    if [ $? = 2 ]; then
      echo "run-selftests: GOV_NODE is '${GOV_NODE:-}', which is no tag the charter's §2 node table (AGENTS.md," >&2
      echo "run-selftests: then CLAUDE.md, at the repo root) carries — a reading written under it would red" >&2
      echo "run-selftests: --check on every bar until the tracked file was hand-edited. Nothing was run." >&2
      exit 2
    fi
    echo "run-selftests: no registry row matches user '${USERNAME:-${USER:-}}' in the charter's §2" >&2
    echo "run-selftests: node table (AGENTS.md, then CLAUDE.md, at the repo root), and GOV_NODE is" >&2
    echo "run-selftests: unset. Pooled evidence is keyed by NODE — a reading taken on another box" >&2
    echo "run-selftests: bounds nothing here — and a hostname is a name the registry does not know." >&2
    echo "run-selftests: Register the node, or set GOV_NODE=<tag>. Nothing was run." >&2
    exit 2; }

  # THE EVIDENCE, LOADED INTO KEYED ARRAYS. A file that does not parse REFUSES rather than
  # defaulting past the bad row; the shape gate is `--check`, and this is the same predicate read
  # at run time so a hand edit cannot bound a row with a number nobody could parse.
  declare -A EV_SECS=() EV_RC=() EV_FAILS=() EV_EXEC=() EV_READINGS=() EV_DATE=() EV_NOTRAILER=()
  ev_bad=""
  EV_TEXT=$(read_evidence)   # read once, fed as a variable: the shell-hygiene leg's rule
  while IFS=$'\t' read -r kind a b c d e f g h i; do
    [ -n "${kind:-}" ] || continue
    case "$kind" in
      NOTRAILER) EV_NOTRAILER["$a"]=1 ;;
      BAD|DUP) ev_bad="$ev_bad"$'\n'"  line $a" ;;
      ROW) k="$a"$'\t'"$b"$'\t'"$c"
           EV_SECS["$k"]=$d; EV_RC["$k"]=$e; EV_FAILS["$k"]=$f; EV_EXEC["$k"]=$g
           EV_READINGS["$k"]=$h; EV_DATE["$k"]=$i ;;
    esac
  done <<EOF
$EV_TEXT
EOF
  if [ -n "$ev_bad" ]; then
    echo "run-selftests: the pooled evidence at $EVIDENCE will not parse, and a bound read past a" >&2
    echo "run-selftests: malformed row is a number nobody wrote. Run --check for the shape; nothing was run." >&2
    printf '%s\n' "$ev_bad" | grep . >&2
    exit 2
  fi

  # --reset NARROWS THE CALIBRATE TO THE RESET ROWS: a reset row is uncalibrated by construction
  # and the refusal has nothing else to refuse. Each must name a row the declaration selects AND a
  # key the file carries under this token and node, or there is nothing to lower.
  if [ "${#RESETS[@]}" -gt 0 ]; then
    _rs_narrow=""
    for _r in "${RESETS[@]}"; do
      k="$_r"$'\t'"$SWEEP_CONDITION"$'\t'"$SWEEP_NODE"
      if [ -z "${EV_SECS[$k]+x}" ]; then
        echo "run-selftests: --reset names '$_r', and $EVIDENCE carries no reading for it under" >&2
        echo "run-selftests: $SWEEP_CONDITION on node $SWEEP_NODE, so there is nothing to lower. Nothing was run." >&2
        exit 2
      fi
      if ! printf '%s\n' "$POP" | awk -F'\t' -v n="$_r" '$2 == n { hit = 1 } END { exit hit ? 0 : 1 }'; then
        echo "run-selftests: --reset names '$_r', which the declaration${FILTER:+ under --kit $FILTER} does not select," >&2
        echo "run-selftests: so the narrowed calibrate could not re-read it. Nothing was run." >&2
        exit 2
      fi
      _rs_narrow="$_rs_narrow"$'\n'"$(printf '%s\n' "$POP" | awk -F'\t' -v n="$_r" '$2 == n')"
    done
    POP=$(printf '%s\n' "$_rs_narrow" | grep . | awk '!seen[$0]++')
    echo "run-selftests: --reset narrows this calibrate to ${#RESETS[@]} row(s): ${RESETS[*]}"
  fi

  # THE ROWS, INDEXED, EACH WITH ITS BOUND. Declaration order is the reporting order whatever the
  # pool does with them, so the output is byte-stable against the serial mode's and against itself
  # at another width. Under --calibrate NO per-row bound exists — every row runs under the one wall,
  # and the `timeout` a worker is wrapped in sits ABOVE that wall so the watchdog's TERM (exit 143,
  # rendered WALL) always lands before `timeout`'s own (exit 124, rendered TIMEOUT).
  SW_N=0; SW_STATE=(); SW_NAME=(); SW_BUDGET=(); SW_ARGV=(); SW_BOUND=(); SW_TERM=(); SW_KEY=()
  SWEEP_LARGEST=0; SWEEP_TOTAL=0; SW_RUNNABLE=0; SWEEP_SUM=0; sw_missing=""
  while IFS=$'\t' read -r state name budget argv; do
    [ -n "${name:-}" ] || continue
    SW_N=$((SW_N + 1))
    k="$name"$'\t'"$SWEEP_CONDITION"$'\t'"$SWEEP_NODE"
    SW_STATE+=("$state"); SW_NAME+=("$name"); SW_BUDGET+=("$budget"); SW_ARGV+=("$argv"); SW_KEY+=("$k")
    b=0; term=""
    if [ "$state" = ok ]; then
      SW_RUNNABLE=$((SW_RUNNABLE + 1))
      SWEEP_SUM=$((SWEEP_SUM + budget))
      if [ "$CALIBRATE" != 1 ]; then
        if [ -z "${EV_SECS[$k]+x}" ]; then
          sw_missing="$sw_missing"$'\n'"  $name"
        else
          if [ "${EV_SECS[$k]}" -gt "$budget" ]; then base=${EV_SECS[$k]}; term=reading; else base=$budget; term=budget; fi
          # THE HEADROOM IS `max(floor, fraction x base)`, ceiled, by awk because the fraction is
          # not an integer and this shell's arithmetic is.
          head=$(awk -v b="$base" -v fl="$MARGIN_FLOOR" -v fr="$MARGIN_FRAC" \
                 'BEGIN { h = fr * b; if (h < fl) h = fl; printf "%d", (h == int(h)) ? h : int(h) + 1 }')
          b=$((base + head))
          SWEEP_TOTAL=$((SWEEP_TOTAL + b))
          [ "$b" -gt "$SWEEP_LARGEST" ] && SWEEP_LARGEST=$b
        fi
      fi
    fi
    SW_BOUND+=("$b"); SW_TERM+=("$term")
  done <<EOF
$POP
EOF
  if [ -n "$sw_missing" ]; then
    echo "run-selftests: these row(s) have NO pooled reading under $SWEEP_CONDITION on node $SWEEP_NODE in" >&2
    echo "run-selftests: $EVIDENCE, so no hang bound can be derived for them and nothing was run:" >&2
    printf '%s\n' "$sw_missing" | grep . >&2
    echo "run-selftests: Take the readings first: bash $SELF --pooled --calibrate${FILTER:+ --kit $FILTER}" >&2
    echo "run-selftests: (a factor wearing a refusal's name is the bound that killed 14 of 58; there is no fallback)" >&2
    exit 2
  fi

  if [ "$CALIBRATE" = 1 ]; then
    # THE CALIBRATE WALL IS THE SERIAL SUM, UNDIVIDED. TOOL-aBatchedArm-5 S2, F5. Nothing pooled can
    # honestly need longer than everything run one after another, so the population fully serialised
    # is the largest backstop derivable with no typed number: a pooled pass exceeding its own serial
    # sum is a HANG and not a cost. The divided form — `ceil(sum / OUTER)` — was rejected because the
    # tree's own sweep record kills it (3860 s against a 7722 s driver row at width 8).
    # SELFTEST_WALL TIGHTENS ONLY: a knob that could loosen a backstop is a knob for disabling it.
    SWEEP_DERIVED=$SWEEP_SUM; SWEEP_WALL=$SWEEP_SUM; wall_term="the serial sum"
    case "${SELFTEST_WALL:-}" in
      '') : ;;
      *[!0-9]*)
        echo "run-selftests: SELFTEST_WALL is '$SELFTEST_WALL', which is not a number of seconds," >&2
        echo "run-selftests: so the run bound you asked for could not be applied. Nothing was run." >&2
        exit 2 ;;
      *) if [ "$((10#$SELFTEST_WALL))" -lt "$SWEEP_SUM" ]; then
           SWEEP_WALL=$((10#$SELFTEST_WALL)); wall_term="SELFTEST_WALL"
         else
           echo "run-selftests: NOTE — SELFTEST_WALL (${SELFTEST_WALL}s) is at or above the serial sum (${SWEEP_SUM}s) and tightens nothing; a calibrate wall only ever tightens."
         fi ;;
    esac
    _sx=0
    while [ "$_sx" -lt "$SW_N" ]; do
      [ "${SW_STATE[$_sx]}" = ok ] && SW_BOUND[$_sx]=$((SWEEP_WALL + 5))
      _sx=$((_sx + 1))
    done
  else
    # THE RUN WALL IS DERIVED FROM THE EVIDENCE BOUNDS by the shape the factor used: the total
    # bounded work spread over the pool, `ceil(sum of bounds / OUTER)`, floored at the largest
    # bound — a pool cannot finish before its longest member's own bound expires, and any smaller
    # wall is an error, not a policy. It is DERIVED rather than borrowed from `run-gates.sh
    # --print-profile`, whose row would sit below the largest bound and kill every sweep for
    # arriving on time. `largest x waves` was rejected: it assumes every wave is as slow as the
    # slowest suite, 2x to 15x the real maximum, and a backstop that cannot fire is not one.
    SWEEP_WALL=$(( (SWEEP_TOTAL + OUTER - 1) / OUTER ))
    [ "$SWEEP_WALL" -ge "$SWEEP_LARGEST" ] || SWEEP_WALL=$SWEEP_LARGEST
    SWEEP_DERIVED=$SWEEP_WALL
    case "${SELFTEST_WALL:-}" in
      '') : ;;
      *[!0-9]*)
        # D5: A KNOB WITH A TYPO IN IT MUST NOT BE SILENTLY IGNORED. Discarding the value leaves the
        # operator believing a bound they never set, which is the same shape as a gate that reports a
        # reassuring zero when it is broken.
        echo "run-selftests: SELFTEST_WALL is '$SELFTEST_WALL', which is not a number of seconds," >&2
        echo "run-selftests: so the run bound you asked for could not be applied. Nothing was run." >&2
        exit 2 ;;
      *) SWEEP_WALL=$((10#$SELFTEST_WALL))
         if [ "$SWEEP_WALL" -lt "$SWEEP_DERIVED" ]; then
           echo "run-selftests: NOTE — the wall you set (${SWEEP_WALL}s) is below the derived one"
           echo "run-selftests: (${SWEEP_DERIVED}s, the bounded work over $OUTER slot(s)), so a legitimately slow run can be killed."
         fi ;;
    esac
    if [ "$SWEEP_WALL" -lt "$SWEEP_LARGEST" ]; then
      echo "run-selftests: the run wall is ${SWEEP_WALL}s but the largest per-suite bound in this" >&2
      echo "run-selftests: population is ${SWEEP_LARGEST}s (an evidence bound), so the run would be killed before its" >&2
      echo "run-selftests: longest suite could legitimately finish. Raise SELFTEST_WALL, or --reset the row" >&2
      echo "run-selftests: whose reading the bound derives from." >&2
      exit 2
    fi
  fi

  SWEEP_ROOT=$(mktemp -d) || { echo "run-selftests: cannot create a scratch root" >&2; exit 2; }
  trap 'rm -rf "$SWEEP_ROOT" 2>/dev/null' EXIT
  # EACH ROW'S OUTPUT OUTLIVES THE TRAP. The render loop copies `$d/out` to
  # `<git-dir>/gate-logs/selftests/<row>.out` — the per-leg pattern `run-gates.sh` already keeps —
  # and prints that path on every row that is not `ok`, because a calibrate's READ row prints none
  # of the suite's output, the two render paths that do print it cap at four un-indented lines, and
  # the trap deletes the rest: the `observed:` lines a batched group's expected set is pasted from
  # were unobtainable from a calibrate (aBatchedArm closing review D3). Resolved ONCE and never
  # composed from an empty git dir; capture OFF is announced, not silent.
  SWEEP_LOGDIR=""
  _gd=$(git rev-parse --git-dir 2>/dev/null) || _gd=""
  if [ -n "$_gd" ] && mkdir -p "$_gd/gate-logs/selftests" 2>/dev/null; then
    SWEEP_LOGDIR="$_gd/gate-logs/selftests"; chmod 700 "$SWEEP_LOGDIR" 2>/dev/null || true
  else
    echo "run-selftests: per-row output capture OFF (no usable git dir) — a row's output dies with the scratch this run" >&2
  fi

  # ---- POOL SAFETY IS OBSERVED, NOT ASSUMED. TOOL-aPooledSweep-3 -------------------------------
  # Running 59 suites together is sound only if each confines its writes to its own scratch. The
  # private TMPDIR below is the redirection; this is the observation that it held.
  #
  # ONE ARM, over the TRACKED working tree. It listed the git common dir too and that arm is DELETED
  # rather than narrowed: that directory is shared by every worktree of the repository and the bar
  # itself writes `gate-bar-beacon` and `gate-bar-queue` at its top level when it claims the
  # turnstile, alongside `gate-ledger.tsv`, `gate-logs`, `index`, `logs` and `refs`. The sweep's
  # floor is its longest suite, so the window between the two readings is tens of minutes wide: any
  # sibling session running a bar flips the listing, and a whole-run fingerprint cannot name a
  # culprit. An instrument that reds on innocent runs is ignored within two sightings.
  #
  # `--untracked-files=no` IS LOAD-BEARING. Plain `--porcelain` lists untracked paths as `??`, so
  # without it every build artifact and freshly written record flips the reading -- this build's own
  # sweep would red on the review report it had just written.
  read_tree_fingerprint() { git status --porcelain --untracked-files=no 2>/dev/null; }

  # THE LIVENESS ASSERTION, and it is NOT emptiness: `git status --porcelain` is EMPTY on a clean
  # tree, so an empty reading is the ordinary case and cannot distinguish a working probe from a
  # broken one. What is asserted is that the command SUCCEEDED.
  if ! FP_BEFORE=$(read_tree_fingerprint) || ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "run-selftests: the tree fingerprint could not be taken, so a sweep would be UNGRADED —" >&2
    echo "run-selftests: a failed reading and a clean tree are the same empty string, and this mode" >&2
    echo "run-selftests: would report the second while meaning the first. Nothing was run." >&2
    exit 2
  fi

  if [ "$CALIBRATE" = 1 ]; then
    echo "run-selftests: CALIBRATE of $SW_N suite(s), width $W (outer $OUTER, inner $SELFTEST_INNER_WIDTH), node $SWEEP_NODE"
    echo "run-selftests: condition: $SWEEP_CONDITION"
    echo "run-selftests: no per-suite bound; run wall ${SWEEP_WALL}s = $wall_term (serial sum ${SWEEP_SUM}s over $SW_RUNNABLE budget(s)); EVERY verdict withheld, readings written to $EVIDENCE"
  else
    echo "run-selftests: SWEEP of $SW_N suite(s), width $W (outer $OUTER, inner $SELFTEST_INNER_WIDTH), node $SWEEP_NODE"
    echo "run-selftests: condition: $SWEEP_CONDITION"
    echo "run-selftests: per-suite bound = max(budget, calibrated reading) + headroom max(${MARGIN_FLOOR}s, ${MARGIN_FRAC} x that); run wall ${SWEEP_WALL}s; NO cost verdict is issued"
  fi

  # THE REAP IS PROBED ONCE, OUTSIDE THE LOOP. `wait -n` returns the exit STATUS of the job that
  # finished, so `wait -n || wait` reads a RED suite as "this shell has no wait -n" and falls back
  # to waiting for all of them — the pool silently degenerates to a barrier per suite, which is
  # serial with extra steps and still prints a width. The selftest harness records the same trap.
  _rs_waitn=0; ( : & wait -n ) >/dev/null 2>&1 && _rs_waitn=1

  # AND SO IS SUB-SECOND `date`. `%N` is a GNU extension: BSD `date` prints the literal `N`, so
  # `$(( $(date +%s%N) / 1000000 ))` is an arithmetic syntax error that aborts EVERY worker before
  # it runs its suite -- a total false RED blaming each suite for the runner's own arithmetic. This
  # script already advertises the platform it cannot run on, by probing for `gtimeout`. Probed once,
  # outside the loop, and the fallback is whole seconds with the resolution SAID rather than
  # silently lost: the peak figure is then blind to a handoff inside one second.
  _rs_ns=0
  case "$(date +%N 2>/dev/null)" in ''|*[!0-9]*) : ;; *) _rs_ns=1 ;; esac
  if [ "$_rs_ns" = 1 ]; then
    read_now_ms() { echo $(( $(date +%s%N) / 1000000 )); }
  else
    read_now_ms() { echo $(( $(date +%s) * 1000 )); }
    echo "run-selftests: this date has no sub-second %N, so stamps are whole seconds and the peak"
    echo "run-selftests: figure below cannot separate a pool handoff from a real overlap."
  fi

  # ONE SUITE, BOUNDED, ITS OWN SCRATCH. The verdict file carries the status, the two stamps and
  # nothing else; the captured output is its own file because a pooled FAIL that printed only an
  # exit code would be a mode you cannot debug without the serial re-run it exists to avoid.
  run_sweep_one() {
    # TWO STATEMENTS, NOT ONE. `local k=$1 d="$SWEEP_ROOT/$k"` expands the whole line BEFORE `local`
    # assigns anything, so `$k` is unbound and `set -u` kills the arm — silently, in a background
    # job, leaving no verdict file. `lib-selftest.sh` sidesteps the same trap by writing `$1` twice.
    local k=$1
    local d="$SWEEP_ROOT/$k"
    mkdir -p "$d/tmp" || return
    local bound=${SW_BOUND[$((k - 1))]}
    local s e rc tp
    s=$(read_now_ms)
    # THE WORKER'S OWN PID, NOT `$$`. A subshell INHERITS `$$` from its parent, so `echo $$` here
    # wrote the RUNNER's pid into every pid file and the wall watchdog SIGTERMed run-selftests.sh
    # itself — exit 143, no verdicts rendered, the suites orphaned and the scratch root deleted from
    # under them. The whole WALL rendering path below was unreachable dead code as a result.
    # Recording the `timeout` child rather than this subshell is what makes the kill reach the work:
    # `timeout` forwards the signal to its own child, and killing the subshell would leave both.
    TMPDIR="$d/tmp" "$SWEEP_TIMEOUT" -k 5 "$bound" bash -c "${SW_ARGV[$((k - 1))]}" > "$d/out" 2>&1 &
    tp=$!
    echo "$tp" > "$d/pid"
    wait "$tp"
    rc=$?
    e=$(read_now_ms)
    rm -f "$d/pid"
    printf '%s\t%s\t%s\n' "$rc" "$s" "$e" > "$d/v"
  }

  # THE WALL WATCHDOG. It records the breach in a FILE before killing anything, so the renderer can
  # tell "this suite was killed by the wall" from "this suite never wrote a verdict" — two states
  # that look identical from a missing file alone.
  # ITS OUTPUT GOES TO /dev/null, AND THAT IS NOT TIDINESS. A background job inherits the caller's
  # stdout, so under `out=$(... --sweep ...)` the watchdog holds the command substitution's pipe open
  # and the CAPTURE blocks for the whole wall even though the sweep finished in seconds. Measured:
  # the round-trip arm below hit its 120s bound against a fixture whose suites take two. It is the
  # same class the selftest harness records for `timeout` and a surviving grandchild.
  #
  # AND ITS SLEEP IS RECORDED, because killing the subshell orphans the sleep rather than ending it.
  ( sleep "$SWEEP_WALL" & echo $! > "$SWEEP_ROOT/dog.sleep"; wait $!
    : > "$SWEEP_ROOT/wall-breached"
    for pf in "$SWEEP_ROOT"/*/pid; do
      [ -r "$pf" ] || continue
      read -r wp < "$pf" 2>/dev/null && kill -TERM "$wp" 2>/dev/null
    done ) >/dev/null 2>&1 &
  SWEEP_DOG=$!
  # DISOWNED, and this is load-bearing rather than tidy: the watchdog sleeps for the whole wall, so
  # a `wait` that can see it blocks until the wall fires even when every suite finished in seconds.
  disown "$SWEEP_DOG" 2>/dev/null || true

  i=1; live=0
  while [ "$i" -le "$SW_N" ]; do
    # THE BREACH STOPS THE DISPATCH, and this line is the whole wall. Before the pid fix the
    # watchdog SIGTERMed the RUNNER, which stopped the run by accident; pointing the kill at the
    # workers -- correct in itself -- removed the only thing that ended it, so the pool kept
    # launching the rest of the population after the wall had fired. Reproduced three times at
    # 16 s, 17 s and 23 s against a 10 s wall. `run-gates.sh` carries the identical guard at the top
    # of its own walk, and this is that line rather than a second invention.
    [ -e "$SWEEP_ROOT/wall-breached" ] && break
    if [ "${SW_STATE[$((i - 1))]}" = ok ]; then
      run_sweep_one "$i" &
      live=$((live + 1))
      if [ "$live" -ge "$OUTER" ]; then
        if [ "$_rs_waitn" = 1 ]; then wait -n; live=$((live - 1)); else wait; live=0; fi
      fi
    fi
    i=$((i + 1))
  done
  wait
  kill "$SWEEP_DOG" 2>/dev/null || true
  if [ -r "$SWEEP_ROOT/dog.sleep" ]; then
    read -r _ds < "$SWEEP_ROOT/dog.sleep" 2>/dev/null && kill "$_ds" 2>/dev/null
  fi

  WALL_BREACHED=0; [ -e "$SWEEP_ROOT/wall-breached" ] && WALL_BREACHED=1

  # RENDERED IN DECLARATION ORDER, by builtins, off the arrays. A suite's position in the output
  # never depends on when the pool happened to free its slot.
  # EVERY NON-COMPLETION OUTCOME HAS ITS OWN WORD AND ITS OWN COUNTER, because two review rounds each
  # found a summary counting fewer outcomes than this loop has. TOOL-aBatchedArm-5 S4: `killed` (own
  # bound), `walled` (the run wall), `unrun` (the wall stopped the dispatch), `unstarted` (no verdict
  # file under no wall breach — the worker-death class the comment on `run_sweep_one` records — or a
  # row that could not be resolved), `mismatched` (completed, and its (rc, FAIL, executed) is not
  # its calibrated baseline). Every place this loop set `st=1` before parity still does, by name;
  # the ONLY change is that a completed, trailed, MATCHED row no longer sets it.
  st=0; ran=0; killed=0; walled=""; unrun=""; withheld=0
  unstarted=0; mismatched=0; untrailed=0; calibrated=0; cal_red=0; cal_rows=""; walled_n=0; unrun_n=0
  # SOUNDNESS IS ITS OWN BIT, cleared by the three post-loop checks (pool wider than OUTER,
  # fingerprint not taken, fingerprint changed): the calibrate's writer used to key on CALIBRATE
  # alone, so a run that had just said "every reading above is suspect" wrote those readings as the
  # monotone bound and the parity baseline anyway (aBatchedArm closing review D7). The cause
  # ACCUMULATES across the three checks rather than being overwritten, so a run that oversubscribed
  # the box AND saw the tree change names both on the one line an operator greps (R6).
  sound=1; unsound_why=""
  outlog=""
  print_outlog() { [ -n "$outlog" ] && printf '        output: %s\n' "$outlog"; return 0; }
  j=1
  while [ "$j" -le "$SW_N" ]; do
    name=${SW_NAME[$((j - 1))]}; state=${SW_STATE[$((j - 1))]}; d="$SWEEP_ROOT/$j"; key=${SW_KEY[$((j - 1))]}
    if [ "$state" != ok ]; then
      st=1; unstarted=$((unstarted + 1))
      printf 'FAIL  %-46s        (%s: this row could not be resolved into a runnable suite)\n' "$name" "$state"
      j=$((j + 1)); continue
    fi
    # THE OUTPUT IS KEPT BEFORE ANY VERDICT IS READ, a killed row's partial capture included.
    # MASKED AND MODE 600 on the way, the sibling runner's `redact()` inlined (a kit file sources no
    # sibling): a suite can echo an operator-exported credential — `fatal: unable to access
    # 'https://user:token@host/…'` from a git call under the operator's global config — and a
    # durable copy that skips the masking its sibling applies is a credential leak the old
    # scratch-dir lifetime was merely hiding (aBatchedArm closing review R1). Every grep below
    # still reads `$d/out`, so no verdict changes.
    outlog=""
    if [ -n "$SWEEP_LOGDIR" ] && [ -f "$d/out" ]; then
      outlog="$SWEEP_LOGDIR/$(printf '%s' "$name" | tr -c 'A-Za-z0-9._-' '_').out"
      sed -E 's#://[^/@[:space:]]+:[^/@[:space:]]+@#://***:***@#g' "$d/out" > "$outlog" 2>/dev/null && chmod 600 "$outlog" 2>/dev/null || outlog=""
    fi
    if [ ! -r "$d/v" ]; then
      st=1
      if [ ! -d "$d" ] && [ "$WALL_BREACHED" = 1 ]; then
        # NEVER LAUNCHED. The wall stopped the dispatch, so this suite has no result of any kind —
        # which is a different fact from a suite that started and was killed, and reporting both as
        # "killed" would tell an operator this suite had been tried.
        unrun="$unrun $name"; unrun_n=$((unrun_n + 1))
        printf 'UNRUN %-46s        (the %ss run wall stopped the dispatch before this suite started)\n' "$name" "$SWEEP_WALL"
      elif [ "$WALL_BREACHED" = 1 ]; then
        ran=$((ran + 1)); walled="$walled $name"; walled_n=$((walled_n + 1))
        printf 'WALL  %-46s        (killed by the %ss run wall before it finished)\n' "$name" "$SWEEP_WALL"
        print_outlog
      else
        ran=$((ran + 1)); unstarted=$((unstarted + 1))
        printf 'FAIL  %-46s        (no verdict was written, so this suite could not start)\n' "$name"
        print_outlog
      fi
      j=$((j + 1)); continue
    fi
    ran=$((ran + 1))
    IFS=$'\t' read -r rc s e < "$d/v"
    took=$(( (e - s) / 1000 ))
    # THE ARTIFACT OF THE WORK, read beside the exit: the `^FAIL` count, whether the trailer is in
    # the filed output, the executed count where the trailer is the executed-count line, and
    # whether the no-baseline sentinel is in it.
    fails=$(grep -c '^FAIL' "$d/out" 2>/dev/null || true); case "$fails" in ''|*[!0-9]*) fails=0 ;; esac
    trailer=0; grep -qE "$SWEEP_TRAILER_RX" "$d/out" 2>/dev/null && trailer=1
    nobase=0; grep -qE "$SWEEP_NOBASELINE_RX" "$d/out" 2>/dev/null && nobase=1
    executed="-"
    if [ "$trailer" = 1 ]; then
      executed=$(grep -oE '\(([0-9]+) assertions executed' "$d/out" 2>/dev/null | head -1 | tr -dc '0-9')
      [ -n "$executed" ] || executed="-"
    fi
    declared_nt=${EV_NOTRAILER[$name]:-0}

    if [ "$CALIBRATE" = 1 ]; then
      # THE CALIBRATE WITHHOLDS EVERY VERDICT and records a reading ONLY for a row that exited on
      # its own AND left its trailer — or is DECLARED trailer-less in the file's header, in which
      # case the reading is rc-plus-FAIL and the gap is printed rather than silent.
      # THE WALL'S WHOLE SIGNAL PATH: its TERM (143) and that TERM escalated to KILL by the
      # worker's `timeout -k` grace (137) are both the wall. Keyed on 143 alone, a suite that
      # ignored TERM under the wall was counted `killed`, `walled` stayed 0, and the summary named
      # a bound the row never hit (aBatchedArm closing review R3). 124 is the row's own bound and
      # stays KILLED below.
      if [ "$WALL_BREACHED" = 1 ] && { [ "$rc" = 143 ] || [ "$rc" = 137 ]; }; then
        st=1; walled="$walled $name"; walled_n=$((walled_n + 1))
        printf 'WALL  %-46s %5ss  (killed by the %ss calibrate wall — NO reading written)\n' "$name" "$took" "$SWEEP_WALL"
        print_outlog
      elif [ "$rc" = 124 ] || [ "$rc" = 137 ] || [ "$rc" = 143 ]; then
        # A KILL IS NOT A COMPLETION whatever the trailer rule says of the row: a declared
        # trailer-less row that outlived TERM (137 after `timeout -k`'s grace) or hit the bound
        # (124) was written as a baseline of that rc, and the next --pooled MISMATCHed a healthy
        # run against it (aBatchedArm closing review D8) — the asymmetry with the graded branch's
        # TIMEOUT clause, closed.
        st=1; killed=$((killed + 1))
        printf 'KILLED %-45s %5ss  (exit %s is a kill, not a completion — NO reading written)\n' "$name" "$took" "$rc"
        print_outlog
      elif [ "$nobase" = 1 ]; then
        # THE SENTINEL IS NOT A BASELINE. The trailer is there and the exit is the suite's own, but
        # a group that says its expected set is unwritten has refused by name, and a reading taken
        # over it would make the next --pooled GREEN over that refusal.
        st=1; untrailed=$((untrailed + 1))
        printf 'UNTRAILED %-42s %5ss  (exit %s, %s FAIL, and its output carries "%s" — a group with no expected set is a refusal, not a reading; paste the observed sets first)\n' "$name" "$took" "$rc" "$fails" "$SWEEP_NOBASELINE_RX"
        print_outlog
      elif [ "$trailer" = 1 ] || [ "$declared_nt" = 1 ]; then
        calibrated=$((calibrated + 1)); [ "$rc" = 0 ] || cal_red=$((cal_red + 1))
        cal_rows="$cal_rows"$'\n'"$name"$'\t'"$took"$'\t'"$rc"$'\t'"$fails"$'\t'"$executed"
        if [ "$declared_nt" = 1 ]; then
          printf 'READ  %-46s %5ss  rc %s, %s FAIL, %s executed  (declared trailer-less: completion NOT witnessed, rc-plus-FAIL only)\n' "$name" "$took" "$rc" "$fails" "$executed"
        else
          printf 'READ  %-46s %5ss  rc %s, %s FAIL, %s executed  (verdict withheld)\n' "$name" "$took" "$rc" "$fails" "$executed"
        fi
        print_outlog
      else
        st=1; untrailed=$((untrailed + 1))
        printf 'UNTRAILED %-42s %5ss  (exit %s, %s FAIL, and NO trailer in its output — a completed exit is not a reading)\n' "$name" "$took" "$rc" "$fails"
        grep -E '^(FAIL|nope|.*FAILED)' "$d/out" 2>/dev/null | head -4 | sed 's/^/        /'
        print_outlog
      fi
      j=$((j + 1)); continue
    fi

    # EVERY ROW THAT RAN CARRIES ITS COST VERDICT, and that verdict is `withheld`. Printing the
    # seconds and nothing else would be a budget silently not graded, which is the green-by-absence
    # class; printing `ok` for the cost would be a verdict taken from a clock this run contended.
    withheld=$((withheld + 1))
    if [ "$WALL_BREACHED" = 1 ] && { [ "$rc" = 143 ] || [ "$rc" = 137 ]; }; then
      # KILLED BY THE WALL, not by its own bound, and the two are different facts. `timeout` exits
      # 124 when ITS bound expires; the watchdog sends TERM, so the worker exits 143 — or 137 when
      # the suite ignored TERM and the `-k` grace escalated the wall's own signal (R3). Rendering both
      # as one lost the distinction, and the WALL branch below -- which only fires on a MISSING
      # verdict -- was unreachable, because a TERMed worker still writes its verdict file. Observed
      # by running it: a 12s wall over an 18s run rendered the killed suite as an ordinary FAIL.
      st=1; walled="$walled $name"; walled_n=$((walled_n + 1))
      printf 'WALL  %-46s %5ss  cost withheld  (killed by the %ss run wall, not by its own bound)
'         "$name" "$took" "$SWEEP_WALL"
      print_outlog
    elif [ "$rc" = 124 ] || [ "$rc" = 137 ]; then
      st=1; killed=$((killed + 1))
      printf 'TIMEOUT %-44s %5ss  (killed at its %ss evidence bound — it did not fail, it did not finish)\n' \
        "$name" "$took" "${SW_BOUND[$((j - 1))]}"
      print_outlog
    else
      # THE POOLED VERDICT IS PARITY. GREEN-by-exit-code is impossible for a population whose
      # baseline is RED by design (unit 3's shard rows exit 1 when complete), so the verdict is
      # re-based: a row that ran to its own end whose (rc, FAIL count, executed count) equals its
      # calibrated baseline is `ok`, and one whose triple differs — or that left no trailer where
      # its baseline has one — is `MISMATCH`, naming both triples and the acceptance. The `FAIL`
      # count is what makes a 0.3 s crash visible: it exits 1 with zero FAIL lines where the
      # baseline carries three. The output grep beneath is the only debug surface a pooled red has.
      got="rc $rc, $fails FAIL, $executed executed"
      base_triple="rc ${EV_RC[$key]}, ${EV_FAILS[$key]} FAIL, ${EV_EXEC[$key]} executed"
      trailer_ok=$trailer; [ "$declared_nt" = 1 ] && trailer_ok=1
      # THE SENTINEL MISMATCHES WHATEVER THE TRIPLE SAYS: a group with no expected set has refused,
      # and a baseline that happened to be taken over the same refusal must not read as parity.
      if [ "$trailer_ok" = 1 ] && [ "$nobase" = 0 ] && [ "$rc" = "${EV_RC[$key]}" ] && [ "$fails" = "${EV_FAILS[$key]}" ] && [ "$executed" = "${EV_EXEC[$key]}" ]; then
        printf 'ok    %-46s %5ss  cost withheld  ok (%s matched)\n' "$name" "$took" "$got"
      else
        st=1; mismatched=$((mismatched + 1))
        printf 'MISMATCH %-43s %5ss  cost withheld  (%s) against baseline (%s)%s%s; --calibrate to take the new baseline, --reset <row> to lower seconds\n' \
          "$name" "$took" "$got" "$base_triple" "$( [ "$trailer_ok" = 1 ] || printf ', and NO trailer in its output' )" \
          "$( [ "$nobase" = 0 ] || printf ', and its output carries "%s" — a group with no expected set is a refusal, never parity' "$SWEEP_NOBASELINE_RX" )"
        grep -E '^(FAIL|nope|.*FAILED)' "$d/out" 2>/dev/null | head -4 | sed 's/^/        /'
        print_outlog
      fi
    fi
    # EVERY POOLED VERDICT NAMES THE READING IT WAS BOUNDED BY — seconds, readings, token, node,
    # date — and which term of the bound won, so a bound is never a number with no provenance.
    printf '        bounded at %ss: %s won (budget %ss; reading %ss over %s reading(s) under %s on node %s, %s) + headroom\n' \
      "${SW_BOUND[$((j - 1))]}" "${SW_TERM[$((j - 1))]}" "${SW_BUDGET[$((j - 1))]}" \
      "${EV_SECS[$key]}" "${EV_READINGS[$key]}" "$SWEEP_CONDITION" "$SWEEP_NODE" "${EV_DATE[$key]}"
    j=$((j + 1))
  done

  echo "----"
  [ -n "$walled" ] && echo "run-selftests: the ${SWEEP_WALL}s run wall killed:$walled"
  # AN UNRUN SUITE IS AN UNGRADED SUITE, said separately because it is the fact an operator acts on:
  # the sweep has no verdict for these at all, and a wall that stops a dispatch leaves more of them
  # the wider the population is.
  [ -n "$unrun" ] && echo "run-selftests: the wall stopped the dispatch, so these were NEVER RUN and are UNGRADED:$unrun"
  # THE PEAK, COMPUTED FROM THE STAMPS BEFORE THE SCRATCH IS REMOVED. The printed width pair says
  # what the pool was ASKED for; this says what it reached. They are different claims, and only the
  # second can catch a pool that ran wide when it was told not to. It is also the number a reader
  # actually wants: "peak 8 of outer 8" says the width was spent, "peak 1" says it was not.
  SWEEP_PEAK=$(
    for vf in "$SWEEP_ROOT"/*/v; do [ -r "$vf" ] && cut -f2,3 "$vf"; done 2>/dev/null | awk '
      { s[NR]=$1; e[NR]=$2 }
      # HALF-OPEN, and the strict `>` is the whole correctness of this figure. Stamps are whole
      # seconds, so with `>=` a suite ENDING at second T and its replacement STARTING at T both
      # count at T -- every pool handoff double-counts. Measured: a strictly serial fixture reported
      # peak 2, and the real 59-row population at outer 8 makes about fifty handoffs, so the guard
      # below would have redded every green sweep.
      END { peak=0
            for (i=1; i<=NR; i++) { c=0
              for (j=1; j<=NR; j++) if (s[j] <= s[i] && e[j] > s[i]) c++
              if (c > peak) peak=c }
            print peak+0 }')
  case "${SWEEP_PEAK:-}" in ''|*[!0-9]*) SWEEP_PEAK=0 ;; esac
  echo "run-selftests: peak concurrency $SWEEP_PEAK of outer $OUTER"
  # AND IT IS A GUARD, not a statistic. The composite invariant is outer x inner within the declared
  # width; a pool that ran wider than its own outer bound has broken it, and the printed pair cannot
  # notice because the pair is what the pool was ASKED for.
  if [ "$SWEEP_PEAK" -gt "$OUTER" ]; then
    st=1; sound=0; unsound_why="${unsound_why:+$unsound_why; }the pool ran wider than its outer bound (peak $SWEEP_PEAK of $OUTER)"
    echo "run-selftests: THE POOL RAN WIDER THAN ITS BOUND — peak $SWEEP_PEAK against an outer width"
    echo "run-selftests: of $OUTER. The composite invariant (outer x inner <= the declared width) is"
    echo "run-selftests: broken, so this run oversubscribed the box and every reading above is suspect."
  fi

  # THE AFTER READING, once the pool has DRAINED. Taken mid-pool it would race fifty-eight writers,
  # which is why this instrument is whole-run and says so rather than pretending to attribute.
  # THE SAME LIVENESS THE BEFORE READING HAS. Without it a `git status` that FAILS here returns the
  # empty string, which on a dirty tree compares unequal and reports the sweep UNSOUND -- a real
  # verdict for a reason that never happened -- and on a clean tree compares equal and reports a
  # match the probe never made.
  if ! FP_AFTER=$(read_tree_fingerprint); then
    st=1; sound=0; unsound_why="${unsound_why:+$unsound_why; }the closing tree fingerprint could not be taken"
    echo "run-selftests: the closing tree fingerprint could not be TAKEN, so this sweep is UNGRADED"
    echo "run-selftests: for pool safety. That is not the same as a clean tree and is not reported"
    echo "run-selftests: as one."
  elif [ "$FP_BEFORE" != "$FP_AFTER" ]; then
    st=1; sound=0; unsound_why="${unsound_why:+$unsound_why; }the tracked working tree changed while the pool ran"
    echo "run-selftests: THE SWEEP IS UNSOUND — the tracked working tree changed while it ran, so a"
    echo "run-selftests: suite wrote outside its own scratch. This cannot name which one: a whole-run"
    echo "run-selftests: fingerprint has no way to attribute, and guessing would be worse than saying"
    echo "run-selftests: so. Re-run the SERIAL mode, which can. What changed:"
    printf '%s\n' "$FP_AFTER" | grep -vxF "$FP_BEFORE" 2>/dev/null | sed 's/^/  /' | head -20
  else
    echo "run-selftests: tree fingerprint MATCHED before and after — no suite wrote outside its scratch"
  fi

  if [ "$CALIBRATE" = 1 ]; then
    # THE READINGS ARE WRITTEN HERE, AFTER THE CLOSING FINGERPRINT, in one pass over the collected
    # verdicts: the evidence file is TRACKED, so a write inside the fingerprinted window would red
    # this run's own soundness. Seconds are MONOTONE per (row, token, node) — raised, never lowered,
    # except by --reset — while rc, fails and executed are the LATEST reading's, so a repaired suite
    # updates its baseline on the next calibrate with no reset. A reset row is DROPPED first: if the
    # narrowed calibrate then walled it or found it untrailed, it stays uncalibrated, named, and the
    # next graded run refuses it by name — a row nobody has seen complete has no bound.
    _rs_resets=""; [ "${#RESETS[@]}" -gt 0 ] && _rs_resets=$(printf '%s\n' "${RESETS[@]}")
    # THE READINGS GO THROUGH A FILE, not the pipe: the heredoc below IS the interpreter's stdin.
    printf '%s\n' "$cal_rows" | grep . > "$SWEEP_ROOT/readings" || true
    # AND ONLY A SOUND RUN WRITES THEM. An unsound calibrate's seconds would become the monotone
    # bound only --reset lowers and its triples the parity baseline every later --pooled is graded
    # against, while the summary blamed walled and untrailed rows at 0 and 0.
    if [ "$sound" != 1 ]; then
      st=1
      echo "run-selftests: readings NOT written: this calibrate was unsound — $unsound_why — so every reading above is suspect and $EVIDENCE is byte-unchanged"
    elif ! "$PYBIN" - "$EVIDENCE" "$SWEEP_CONDITION" "$SWEEP_NODE" "$(date +%Y-%m-%d)" "$_rs_resets" "$SWEEP_ROOT/readings" <<'PY'
import sys
path, cond, node, today, resets, readings = sys.argv[1:7]
resets = set(r for r in resets.split("\n") if r)
head, rows, order = [], {}, []
try:
    with open(path, encoding="utf-8", newline="") as fh:
        for raw in fh:
            line = raw.rstrip("\r\n")
            if not line.strip() or line.lstrip().startswith("#"):
                head.append(line)
                continue
            f = line.split("\t")
            if len(f) != 9:
                sys.exit("run-selftests: refusing to rewrite %s past a row that is not nine fields: %r" % (path, line))
            k = (f[0], f[1], f[2])
            rows[k] = f
            order.append(k)
except FileNotFoundError:
    head = ["# selftest-pooled-evidence.txt — pooled hang-bound readings, written by run-selftests.sh --pooled --calibrate.",
            "# <row>\t<condition>\t<node>\t<max seconds>\t<rc>\t<fails>\t<executed>\t<readings>\t<date>"]
for r in sorted(resets):
    k = (r, cond, node)
    if k in rows:
        print("run-selftests: RESET %s under %s on node %s: dropped its %ss reading; the re-reading below replaces it or it stays uncalibrated" % (r, cond, node, rows[k][3]))
        del rows[k]; order.remove(k)
for line in open(readings, encoding="utf-8"):
    line = line.rstrip("\r\n")
    if not line:
        continue
    name, took, rc, fails, executed = line.split("\t")
    k = (name, cond, node)
    if k in rows:
        old = int(rows[k][3]); n = int(rows[k][7]) + 1
        secs = max(old, int(took))
        how = "raised from %ss" % old if secs > old else "kept at %ss (this reading %ss is not worse)" % (old, took)
    else:
        secs, n, how = int(took), 1, ("first reading after --reset" if name in resets else "first reading")
    rows[k] = [name, cond, node, str(secs), rc, fails, executed, str(n), today]
    if k not in order:
        order.append(k)
    print("run-selftests: reading %s under %s on node %s: %ss (%s), rc %s, %s FAIL, %s executed, %s" % (name, cond, node, secs, how, rc, fails, executed, today))
with open(path, "w", encoding="utf-8", newline="") as fh:
    for h in head:
        fh.write(h + "\n")
    for k in order:
        fh.write("\t".join(rows[k]) + "\n")
PY
    then
      st=1
      echo "run-selftests: the readings could NOT be written to $EVIDENCE, so this calibrate took nothing"
    fi
    if [ "$st" -eq 0 ]; then
      echo "calibrated $calibrated row(s), $cal_red red, graded none"
    else
      # THE RED SUMMARY NAMES ITS ACTUAL CAUSE. An unsound run has written nothing at all; only a
      # sound one is red for the rows that took no reading.
      echo "calibrated $calibrated row(s), $cal_red red, ${walled_n:-0} walled, $untrailed untrailed, graded none"
      [ "$killed" -gt 0 ] && echo "run-selftests: and $killed row(s) KILLED — exit 124, 137 or 143, killed by a signal or its own bound — wrote NO reading either."
      if [ "$sound" != 1 ]; then
        echo "run-selftests: NO reading was written for ANY row: $unsound_why. Fix that and calibrate again."
      else
        [ "$((${walled_n:-0} + untrailed + killed))" -gt 0 ] && echo "run-selftests: a walled, killed or untrailed row wrote NO reading and stays uncalibrated; the next --pooled refuses it by name."
      fi
      [ "${unrun_n:-0}" -gt 0 ] && echo "run-selftests: and ${unrun_n} row(s) were never dispatched under the wall, so they took no reading either."
    fi
    exit "$st"
  fi

  # THE COUNT IS WHAT STOPS THE WITHHOLDING BEING A SILENT PASS. A green sweep announces on every
  # run how many budgets it did not grade, so it can never be mistaken for a budget-clean run.
  echo "run-selftests: $withheld cost verdict(s) WITHHELD under $SWEEP_CONDITION — a contended clock cannot grade a budget"
  echo "run-selftests: for a cost verdict, run the serial mode: bash $SELF --serial"
  counts="killed $killed · walled ${walled_n:-0} · unrun ${unrun_n:-0} · unstarted $unstarted · mismatched $mismatched"
  if [ "$st" -eq 0 ]; then
    echo "sweep GREEN — $ran suite(s) ran concurrently, every one to its own end and matching its baseline; $counts; NO cost verdict was issued for any of them"
  else
    echo "sweep RED — $ran suite(s) ran concurrently; $counts; NO cost verdict was issued"
    # A POOLED RED IS A PARITY RED, and the summary says what each word means and what resolves it.
    # It is NOT told to confirm itself serially: the question this mode answers is parity with the
    # calibrated baseline, which the serial loop does not ask.
    echo "run-selftests: a pooled RED means a row did not run to its own end, or did and did not match"
    echo "run-selftests: its calibrated (rc, FAIL, executed) baseline. A MISMATCH after a genuine repair is"
    echo "run-selftests: one calibrate away: bash $SELF --pooled --calibrate${FILTER:+ --kit $FILTER}"
    echo "run-selftests: A killed or walled row is a hang, or a box slower than its evidence — the same"
    echo "run-selftests: calibrate raises its bound from what it observes. For a COST verdict use --serial."
  fi
  exit "$st"
fi

echo "run-selftests: $NROWS suite(s), declared total $(( (TOTAL + 59) / 60 )) minutes, width $W (outer $OUTER, inner $SELFTEST_INNER_WIDTH)"
st=0; ran=0; over=0
while IFS=$'\t' read -r state name budget argv; do
  [ -n "${name:-}" ] || continue
  # THE STATE IS READ HERE TOO. This loop used to ignore it entirely, so an UNRESOLVED row -- whose
  # argv is empty by construction -- was `eval`'d as the empty string, returned 0, and printed a
  # green line for a suite that does not exist. `--check` is a separate leg and a separate run; a
  # runner that trusts it has two answers to one question.
  if [ "$state" != ok ]; then
    st=1
    printf 'FAIL  %-46s        (%s: this row could not be resolved into a runnable suite)\n' "$name" "$state"
    continue
  fi
  ran=$((ran + 1))
  s=$(date +%s)
  out=$(eval "$argv" 2>&1); rc=$?
  e=$(date +%s); took=$(( e - s ))
  if [ "$rc" -eq 0 ]; then
    printf 'ok    %-46s %5ss\n' "$name" "$took"
  else
    st=1
    printf 'FAIL  %-46s %5ss  (exit %s)\n' "$name" "$took" "$rc"
    printf '%s\n' "$out" | grep -E '^(FAIL|nope|.*FAILED)' | head -4 | sed 's/^/        /'
  fi
  if [ "$took" -gt "$budget" ]; then
    st=1; over=$((over + 1))
    printf '      OVER BUDGET  %s took %ss against a declared %ss — fix it, or re-declare it with a reason beside the number\n' "$name" "$took" "$budget"
  fi
done <<EOF
$POP
EOF

echo "----"
if [ "$st" -eq 0 ]; then
  echo "self-tests GREEN — $ran ran on demand; none of them runs on the merge bar"
elif [ "$over" -gt 0 ]; then
  echo "self-tests RED — $ran ran on demand, $over over budget"
else
  echo "self-tests RED — $ran ran on demand"
fi
exit "$st"
