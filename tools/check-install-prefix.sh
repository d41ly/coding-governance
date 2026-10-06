#!/usr/bin/env bash
# check-install-prefix.sh — nothing this repo tracks under its kit surface may spell a kit path.
#
#   bash <prefix>/check-install-prefix.sh            # assert; exit 1 naming every <path>:<line>
#   bash <prefix>/check-install-prefix.sh --list     # print every hit and every render left out
#   bash <prefix>/check-install-prefix.sh --offenders   # one <path> TAB ban TAB <spelling> per hit; exits as --check
#
# --offenders IS THE SIGNATURE THE MERGE BAR GRADES THIS LEG WITH (TOOL-dDerivedDocket-23 S3). Its red
# attribution compares two trees' offender SETS, and `--check` cannot feed that: it keys every hit by
# `<path>:<line>`, so one unrelated edit above an inherited hit moves it. This mode prints a KEY per
# counted spelling and nothing else — no line number, no count, no prose; a key repeating inside one
# file carries `#<k>`, its occurrence ordinal there. Every other line goes to /dev/null. The keys
# come out of the counter in ONE write at its end, so a refusal or a counter that dies leaves NO key,
# which the attribution reads as a probe that could not answer, never as a clean set. Merged into the
# pure ban from dDerivedDocket's carried-prefix shape, whose `root`/`carried`/`runtime` kinds were the
# three arms this gate no longer has: every hit here is one kind, `ban`.
#
# WHY. `govkit apply` writes gov's bytes VERBATIM: nothing substitutes into a file body anywhere, so
# a kit path a file spells arrives unchanged in a target installed at another prefix and resolves to
# nothing in their tree. Those fail quietly. Measured before this gate existed: a `tools/` install
# scaffolded the adopter's own committed `HYGIENE.md` with seven kit paths that resolve to nothing
# in their tree, and the hygiene gate exited 0 over it.
#
# A PURE BAN, since TOOL-aRepatriatedFork-30. ONE predicate, ZERO tolerance, and no remedy but
# deriving the path. There is no list of carried literals, no waiver registry, no line marker and no
# mode that writes anything: every one of those was an exemption a pass could grant itself, and the
# drain units that preceded this one emptied all three before they were deleted. A future widening
# of the predicate reds its new hits, and they are drained before the widening lands.
#
# WHAT "SHIPS" MEANS, and where this gate grades nothing. A repo ships what its govkit registry
# resolves (TOOL-aRepatriatedFork-16). Installed at a repo whose engine and registry do not resolve
# from this gate's directory — a consumer, which ships nothing onward — it prints a SKIP line and
# exits 0. It does not grade a consumer's own tree or the gov files that consumer received.
#
# THE POPULATION is every tracked file under this gate's own tool root, `skills/`, `.githooks/`,
# every `*.template.*` and the runbook, shipped or not (TOOL-aRepatriatedFork-23 S2) — LESS A
# RENDER. A tracked file that matches, whole, a `rendered` template the registry ships is gov's own
# render of it, which is the rendered-at-deploy-time form an adopter regenerates at its own prefix
# (TOOL-aRepatriatedFork-29 §8 F3 (a)). The match reads each `{{TOKEN}}` as one line of any text and
# a repeated token as the same text, so it is a re-render proved structurally, without the values.
# The TEMPLATE stays in the population, so a literal reaches a render only through a graded file,
# and a hand edit that breaks the match puts the render straight back.
#
# THE PREDICATE is the counter below, five rules over each line, read in order:
#   1. a quoted `"tools"` segment JOINED — by `/`, by `,` to a quoted segment, or inside `join(`;
#   2. gov's prefix followed by a kit, directory-only or not, or by a loose `<name>.<ext>`, after
#      any lead but a path character or a brace, `/` included, so `$ROOT/` and `<gov>/` leads count;
#   3. a kit segment followed by a file, at the root, under ANY literal prefix and under a derived
#      base (`${PFX}`, `$HERE/../`): a kit's name typed as a literal is the class whatever leads it;
#   4. a quoted kit segment used as a path segment — joined by `/`, or after a quoted literal
#      segment and a comma inside an open `join(`, `joinpath(` or `Path(` call;
#   5. the DRAINED spellings, which count nothing: the render tokens `{prefix}/`, `{kit}/` and
#      `{{TOOL_ROOT}}`, and the prose tokens `<prefix>/` and `<tool-root>/`.
# The kit-name alternation is DERIVED from the tracked directories under this gate's tool root,
# never listed, so a new kit is covered the day it lands.
#
# WHAT THIS GATE DOES NOT CHECK, said out loud because a structural check reads as a semantic one to
# everyone who did not write it:
#   * a path ASSEMBLED FROM TWO VARIABLES. A kit's name held in a variable and joined at run time
#     spells no literal, which is exactly how a fixture laid out at a foreign prefix names its kits;
#   * a literal inside `eval` or `sh -c` text BUILT AT RUN TIME from pieces;
#   * any file OUTSIDE THE GLOBS above: `memory/`, this repo's own records, `.claude/`, and the
#     repo-root dotfiles.
# It does not know whether a path is CORRECT, only whether it names a kit literally. The render rule
# proves a file is a render for SOME token values and not which ones: the owning kit's parity leg
# re-renders with the real values. The homonym rules in rules 3 and 4 are context heuristics, and
# each states its ceiling where it lives in the counter.
set -u
# --offenders: stdout is KEYS and nothing else, so prose goes to /dev/null from the first line and the
# counter's keys to fd 3. Decided before anything can print, the not-a-repo refusal included.
MODE="${1:---check}"
[ "$MODE" = --offenders ] && exec 3>&1 1>/dev/null
# TOOL-cWidenedNet-1 S4 — CAPTURED BEFORE THE `cd`, because `$0` may be relative and the `cd` below
# moves out from under it.
_self_dir=$(cd "$(dirname "$0")" 2>/dev/null && pwd) || _self_dir=""
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "install-prefix: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

# THIS GATE'S OWN TOOL ROOT IS DERIVED, and an empty derivation REFUSES. `git -C <dir> rev-parse
# --show-prefix` and not `${_self_dir#"$ROOT"/}`: on Windows a junction makes the two spellings of
# one tree differ as strings, so the strip no-ops and the result comes out ABSOLUTE. An EMPTY prefix
# is the repo root, which is a legal install and not a failure — the two are told apart by git's
# exit status, not by the emptiness of its answer.
if ! SELF_REL=$(git -C "$_self_dir" rev-parse --show-prefix 2>/dev/null); then
  echo "install-prefix: cannot derive this gate's own directory from '$_self_dir', so its tool root"
  echo "install-prefix: and population cannot be resolved. REFUSING rather than falling back to a"
  echo "install-prefix: guessed prefix, which is the shape that makes a broken install look like a"
  echo "install-prefix: working one."
  exit 2
fi
SELF_REL=${SELF_REL%/}
SELF_PREFIX=${SELF_REL:+$SELF_REL/}
# The awk field the kit-name walk reads, derived from the same answer: the path is
# `<prefix…>/<kit>/<file>` and the kit is the field after the prefix's own segments, so a root
# install reads field 1, `scripts/` field 2, `vendor/gov/` field 3.
_seg_kit=$(( $(printf '%s' "$SELF_PREFIX" | tr -cd '/' | wc -c) + 1 ))
case "$MODE" in --check|--list|--offenders) ;;
  *) echo "usage: $(basename "$0") [--check|--list|--offenders] — a pure ban has no mode that writes anything"; exit 2 ;; esac

# THE KIT-SOURCE TEST (TOOL-aRepatriatedFork-16 S2). A repo SHIPS what its registry resolves, so a
# repo with none ships nothing and there is no population to police. Neither path is probed by NAME
# (TOOL-aRepatriatedFork-46 S4): the python resolver is carried INLINE, and govkit is found by the
# sibling-kit resolver below, which reads the install receipt first. Its anchor is govkit's ENGINE
# and not the registry, because the registry also ships inside the playbook renderer: a consumer's
# receipt names a registry row, and anchoring on it would read that consumer as a kit source.
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
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
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
REGISTRY=""
if _gk_dir=$(resolve_kit_dir "$PY_GATE" govkit govkit.py "$_self_dir" 2>/dev/null) \
   && [ -f "$_gk_dir/registry.toml" ]; then
  REGISTRY="$_gk_dir/registry.toml"
fi
if [ -z "$REGISTRY" ]; then
  # A SKIP ANNOUNCES ITSELF (§7), and exits 0 (TOOL-aRepatriatedFork-16 §8 F1, owner): a consumer's
  # bar stays green when it has nothing to police, and a printed skip cannot be misread as a graded run.
  echo "install-prefix: SKIPPED — this repo is not a kit SOURCE (no govkit engine and registry resolve"
  echo "install-prefix: from this gate's directory), so it ships nothing and its files under"
  echo "install-prefix: ${SELF_PREFIX:-the repo root} were NOT graded on this run. Said out loud rather"
  echo "install-prefix: than passed silently: a skip that looks like a pass is indistinguishable from coverage."
  exit 0
fi

# The kit names, derived. `git ls-files` so the answer is the same on every node and in every
# checkout — a directory listing would also see untracked scratch dirs. The prefix is `SELF_PREFIX`:
# at an install anywhere but gov's, a literal here matched nothing and the refusal below fired.
kits=$(git ls-files -- "${SELF_PREFIX}*/*" | awk -F/ "NF>${_seg_kit} {print \$${_seg_kit}}" | sort -u)
[ -n "$kits" ] || { echo "install-prefix: no kit directories under ${SELF_PREFIX:-the repo root} — that is not a pass"; exit 1; }

# THE EXTENSION CLASS. `txt|tsv|conf|example` joined the original six at TOOL-cWidenedNet-1: every
# kit keeps its declaration sidecars as `.txt` or `.tsv` and ships a `.conf.example`. The remaining
# blind extensions are deliberate: `.yml`, `.ini` and `.cfg` appear nowhere in this tree, and an
# alternative matching nothing is an assertion about nothing.
EXT="sh|py|js|md|json|toml|txt|tsv|conf|example"

# THE TEMPLATES the render rule matches against: every `rendered` row of govkit's `shipped` verb,
# the ONE derivation of what this repo ships. A verb that FAILS is a refusal, never an empty list:
# read as "no templates", every render would be graded and the gate would red on gov's own renders
# for a reason nobody could see.
_shipped=$("$PY_GATE" "${REGISTRY%/*}/govkit.py" shipped) || {
  echo "install-prefix: govkit's shipped verb failed, so the templates the render rule matches against"
  echo "install-prefix: are unknown. REFUSING rather than grading a population whose renders it cannot tell."
  exit 1
}
TEMPLATES=$(printf '%s\n' "$_shipped" | tr -d '\r' | awk -F'\t' '$2 == "rendered" { print $3 }')

derive_ban_files() {
  # TOOL-aRepatriatedFork-23 S2 — EVERY tracked file under the kit surface, shipped or not. A
  # descriptor-resolved population left 57 files at 2143b6d6 carrying literals nobody counted.
  git ls-files -- "${SELF_PREFIX}*" 'skills/*' '.githooks/*' '*.template.*' 'WIRE-INTO-PROJECT.md' \
    | tr -d '\r' | LC_ALL=C sort -u
}

IFS= read -r -d '' _ban_src <<'BAN_PY' || true
import os
import re
import sys

# The ban's counter. A counter that DIES refuses: a dead producer at the head of a pipe yields zero
# hits at exit 0, which is indistinguishable from a clean tree (the D3 class from
# DEPL-dCarriedReceipt's closing review). So every empty input exits 2, and the shell reds on it.
MODE = sys.argv[1]
files = [f.strip("\r") for f in sys.stdin.read().split("\n") if f.strip()]
kits = [k for k in os.environ.get("BAN_KITS", "").split("\n") if k]
EXT = os.environ.get("BAN_EXT", "")
templates = [t for t in os.environ.get("BAN_TEMPLATES", "").split("\n") if t.strip()]
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
# what the variable holds.
NONKIT = re.compile(r"(?i)git|\bcommon\b|\bsdir\b|session|transcript")
# Rule 5: the ONLY spellings that drain a kit segment. Any other brace before a kit name is a derived
# base the kit name was typed after, which is the class (`${PFX}<kit>/`).
DRAINED = re.compile(r"(?:\{prefix\}/|\{kit\}/|\{\{TOOL_ROOT\}\}|<prefix>/|<tool-root>/)$")
# Rule 4's comma branch counts only inside an open path-join call. ponytail: its ceiling is a callee
# that assembles the path from separate arguments, `f('clean', 'scripts', '<kit>')`, which reads as
# an argument list and is not seen: the same blind spot as a path built from two variables.
JOINCALL = re.compile(r"(?:\bjoin|\bjoinpath|\bPath)\s*$")
TOKEN = re.compile(r"\{\{([A-Z_]+)\}\}")


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
        out.append((kit, work[a:b]))  # the spelling, read before its span is masked
        work = work[:a] + "\0" * (b - a) + work[b:]

    # 1. a quoted gov-prefix segment, JOINED: by `/`, by `,` to a quoted segment, or in a join( call
    for m in QGOV.finditer(work):
        a, b = m.span()
        before, after = work[:a], work[b:]
        if not (re.match(r"\s*/(?!/)", after) or re.match(r"\s*,\s*%s" % Q, after)
                or re.search(r"/\s*$", before) or re.search(r"join\([^()]*,\s*$", before)):
            continue  # a mapping key, a list member, an argument: not a path segment
        nx = re.match(r"\s*[/,]\s*(%s)(?P<s>[%s]*)\1" % (Q, NP), after)
        kit, end = "(loose)", b
        if nx:
            kit, end = (nx.group("s") if nx.group("s") in kits else "(loose)"), b + nx.end()
        add(a, end, kit)
    # 2. gov's prefix followed by a kit (directory-only or not) or a loose `<name>.<ext>`, after any
    #    lead but a path character or a brace — `/` included, so `$ROOT/`, `<gov>/`, `<project>/`
    for m in GOVPFX.finditer(work):
        add(m.start(), m.end(), m.group("k") or "(loose)")
    # 3. `<kit>/<file>.<ext>` at the root, under any literal prefix and under a derived base
    for m in KSEG.finditer(work):
        a, before = m.start(), work[:m.start()]
        if not FILE.match(m.group("rest")):
            continue
        if before[-1:] == "\0" or DRAINED.search(before):
            continue  # a render or prose token, or a span an earlier rule counted
        if before.endswith("/"):
            operand = re.split(r"[\s\"'`=(]", before)[-1]
            if any(DOTDIR.match(s) for s in operand.split("/")) or NONKIT.search(operand):
                continue  # a Skill dir, a git `hooks/`, a sidecar under the git dir
        add(a, m.end(), m.group("k"))
    # 4. a quoted kit segment used as a path segment: joined by `/`, or by `,` after a quoted
    #    literal prefix segment inside a path join — unless the operand makes it a homonym
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
                continue  # an argument, a list member, a mapping key: not inside a path join
        add(a, b, m.group("k"))
    return out


def read_text(path):
    try:
        return open(path, encoding="utf-8", errors="replace", newline="").read().replace("\r\n", "\n")
    except OSError:
        return None


def build_render_rx(src):
    """<src>, a template, as one regex a render of it matches WHOLE: each `{{TOKEN}}` one line of
    any text, a repeated token the same text as its first occurrence, the rest literal."""
    out, seen, pos = [], set(), 0
    for m in TOKEN.finditer(src):
        out.append(re.escape(src[pos:m.start()]))
        name = m.group(1)
        out.append("(?P=%s)" % name if name in seen else "(?P<%s>[^\n]*?)" % name)
        seen.add(name)
        pos = m.end()
    out.append(re.escape(src[pos:]))
    return re.compile("".join(out))


# THE RENDER RULE. A candidate sits under its template's directory and ends in the template's own
# extension; a template is never a candidate. The template must itself be in the population, or a
# render would leave the ban with its source graded nowhere.
fileset = set(files)
renders = {}
for t in templates:
    src = read_text(t) if t in fileset else None
    if src is None:
        continue
    rx, d, ext = build_render_rx(src), os.path.dirname(t), os.path.splitext(t)[1]
    for f in files:
        if f in renders or f == t or ".template." in f or not f.endswith(ext) \
                or not f.startswith(d + "/" if d else ""):
            continue
        body = read_text(f)
        if body is not None and rx.fullmatch(body):
            renders[f] = t

graded = hits = 0
bad = []
keys, seen_keys = [], {}
for f in files:
    if f in renders:
        continue
    src = read_text(f)
    if src is None:
        continue
    graded += 1
    for n, line in enumerate(src.split("\n"), 1):
        got = scan_line(line)
        if got:
            hits += len(got)
            bad.append("  %s:%d  %s  %s" % (f, n, ",".join(sorted({k for k, _ in got})), line.strip()[:90]))
            for _, spelling in got:
                # One key per counted spelling, an ordinal on a repeat inside one file: the shape
                # dDerivedDocket's attribution compares as a SET (TOOL-dDerivedDocket-23 S3).
                k = "%s\tban\t%s" % (f, spelling.strip())
                seen_keys[k] = seen_keys.get(k, 0) + 1
                keys.append(k if seen_keys[k] == 1 else "%s#%d" % (k, seen_keys[k]))
if graded == 0:
    sys.stderr.write("install-prefix: the ban's counter graded NO file out of %d tracked — a dead probe,"
                     " not a pass\n" % len(files))
    sys.exit(2)

if MODE == "--offenders":
    # LF bytes in ONE write: a text-mode stdout on Windows ends every line in CR, which an exact-match
    # reader of the set meets as `<key>CR`. Exits as --check does.
    if keys:
        sys.stdout.buffer.write(("\n".join(keys) + "\n").encode("utf-8"))
    sys.exit(1 if bad else 0)

out = []
if MODE == "--list":
    out += ["  render  %s  <- %s" % (f, renders[f]) for f in sorted(renders)]
if bad:
    if MODE == "--check":
        out += ["install-prefix: a tracked file spells a kit path. `govkit apply` writes these bytes verbatim,",
                "install-prefix: so at a target installed at any other prefix they resolve to nothing. Derive the",
                "install-prefix: path from the file's own location, route a sibling kit through resolve_kit_dir,",
                "install-prefix: or spell it through a drained token. This is a pure ban: there is no waiver."]
    out += bad
summary = ("install-prefix: %s — %d tracked file(s) graded, %d render(s) left out as matching their"
           " template, %d kit-path spelling(s) on %d line(s)"
           % ("RED" if bad else "clean", graded, len(renders), hits, len(bad)))
out.append(summary)
sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8"))
sys.exit(1 if bad and MODE == "--check" else 0)
BAN_PY
_out_fd=1; [ "$MODE" = --offenders ] && _out_fd=3   # the keys, and only the keys, reach the caller
derive_ban_files | BAN_KITS="$kits" BAN_EXT="$EXT" BAN_TEMPLATES="$TEMPLATES" "$PY_GATE" -c "$_ban_src" "$MODE" >&"$_out_fd"
rc=$?
case "$rc" in
  0|1) exit "$rc" ;;
  *) echo "install-prefix: the ban's COUNTER died (exit $rc: no usable python, or it refused its input),"
     echo "install-prefix: so it measured nothing. Refusing to read that as a tree carrying zero literals:"
     echo "install-prefix: a dead producer is the D3 class, not a clean result."
     exit 1 ;;
esac
