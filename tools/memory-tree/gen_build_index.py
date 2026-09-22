#!/usr/bin/env python3
"""gen_build_index.py — the generated build index for a flat memory tree (memory-tree kit 1.5).

    python tools/memory-tree/gen_build_index.py --check         # drift gate (writes nothing)
    python tools/memory-tree/gen_build_index.py --write         # (re)render every artifact
    python tools/memory-tree/gen_build_index.py --check-format  # the slot contract + heading canon
    python tools/memory-tree/gen_build_index.py --survey        # the canon over every README, never fails
    python tools/memory-tree/gen_build_index.py --selftest      # fixtures, in a temp dir

WHAT --check-format DOES NOT CHECK. It grades POSITION for every tracked build README and SHAPE — the
closed heading canon — only for the ones the declared registry BINDS. It never grades what a slot
SAYS, whether the description is the one first authored, or how large any slot is. Size is a separate
declared budget; the description's immutability is a DOCUMENTED check in HYGIENE.md and deliberately
not a gated one, because 26 of 61 description blocks already carry more than one commit and a
history-based predicate would have no green starting state to land on.

It replaces the retired directory-listing generator. A listing carried paths, which git already
prints better; this carries STATUS, which git does not — and a build's status is a PURE FUNCTION of
its units' statuses, so nothing here is authored and nothing rots.

THREE SOURCES, NOTHING ELSE
  * each build's README front matter (slug node opened streams roster [status])
  * every `**Status:**` header under that build's spec/, at any depth
  * for the ROSTER only, every tracked file under the memory root EXCEPT this field's own outputs —
    the build's own README and the generated index and shards. `ids` is therefore an OUTPUT, not a
    source: `--write` overwrites whatever was authored there.
No git history and no mtimes. A source the renderer does not read cannot make the render drift; a
source the renderer WRITES must not also be read, or a wrong value defends itself forever.

ONE SOURCE OF TRUTH PER BUILD
  * any spec carries a parseable header -> the status is DERIVED, and an authored `status:` is an
    ERROR (two answers to one question is the drift this file exists to remove);
  * no spec carries one -> `status:` is REQUIRED, and its absence is a named error.
Three builds in the originating corpus are grandfathered recordings with no status header at all;
every plausible default for them was wrong, so the fallback is explicit and gated instead.

THE THREE BLIND SPOTS THIS CLOSES (each armed in --selftest)
  1. a README with no marker PAIR used to leave the universe silently -> named error;
  2. an orphaned generated file was permanent and invisible -> reported, and removed by --write,
     BOUNDED to a `ledger/<YYYY-MM>.md` name; anything else in ledger/ is reported and left alone,
     because a generator that deletes inside the memory tree on its own authority is a data-loss path;
  3. an absent README killed both modes with a traceback -> named error, never a stack.
"""
from __future__ import annotations

import os
import pathlib
import re
import subprocess
import sys
import tempfile

CR = chr(13)   # one carriage return; see _is() and _one_cr()
RECORD_KINDS = ("spec", "build", "reviews", "prompts")
MARK_OPEN = "<!-- gen:build-index -->"
MARK_CLOSE = "<!-- /gen:build-index -->"

# The AUTHORED plan region. This generator NEVER writes between these two markers. The RULE still
# holds; the reason it was first given has EXPIRED, and the pair is recorded here so the next reader
# does not delete a live rule along with its dead justification. It WAS that check_authorization
# byte-compared this slice across a run's pinned BASE. TOOL-aBoundedVerdict-11 moved that comparison
# to the generated unit-ID set, so no byte-compare reaches here any more. What still reads the pair
# is the unattended driver's roster_ids, which answers which units are PLANNED but unspecced — a
# question the generated region cannot answer, because it is rendered from the specs that exist. A
# renderer writing here would therefore corrupt a plan rather than invalidate an authorization. It is
# listed so the slot walk can FIND it, not so anything can render into it.
PLAN_OPEN = "<!-- roster:units -->"
PLAN_CLOSE = "<!-- /roster:units -->"

# Every generated region, in CANONICAL SLOT ORDER. `--write` creates a missing pair at its position
# here; `--check` never demands one (TOOL-aRuledFrontispiece-1 S1c). The order is a property of this
# list rather than of whoever edited a README last.
#
# The renderer is looked up by name at call time rather than stored, so this stays a plain data
# declaration and a region cannot be half-registered.
# TOOL-aBoundedVerdict-11 S1 — the units table's own pair, NESTED inside `build-index` rather than a
# fifth GEN_REGIONS entry. It is deliberately not in GEN_REGIONS: that tuple drives region CREATION
# and the canonical order check, and registering this one there would place the units table outside
# the region every existing reader brackets. Consumers address it with `region()` like any other pair.
UNITS_OPEN = "<!-- gen:build-units -->"
UNITS_CLOSE = "<!-- /gen:build-units -->"

GEN_REGIONS = (
    ("build-index", MARK_OPEN, MARK_CLOSE),
    ("build-order", "<!-- gen:build-order -->", "<!-- /gen:build-order -->"),
    ("build-edges", "<!-- gen:build-edges -->", "<!-- /gen:build-edges -->"),
)
# TOOL-dFramedEntrypoint-5 — `build-docs` was the LAST entry and is gone. Removing the last entry
# shifts no surviving index, which is why no sibling region moved; the selftest arms that addressed
# it BY TUPLE INDEX did have to move, and a grep for the marker name could not have found them.
# The orphaned marker pair is removed from every tracked build README in the SAME commit: a region
# whose registration is gone but whose pair remains becomes authored content sitting after the first
# generated marker, which is trigger 1 of the slot contract, measured at 750 violation lines.
DEAD_REGIONS = (("build-docs", "<!-- gen:build-docs -->", "<!-- /gen:build-docs -->"),)

# TOOL-dFramedEntrypoint-1 — the CLOSED heading canon for a build README's authored half. The slot
# contract above constrains only WHERE authored content sits; this constrains WHAT it is. Position
# stays the mechanism: no slot gets a marker pair of its own, which is what TOOL-aRuledFrontispiece-1
# refused and what that refusal's surviving reason (two more lines per README to solve a problem
# position already solves) still forbids. Its OTHER refusal — heading-detection, because
# check_authorization byte-compared a marker-delimited region — expired at TOOL-aBoundedVerdict-11,
# and reading the two as one refusal is how a live rule gets deleted with its dead neighbour.
#
# `(heading, empty_ok, bullets)`. The FIRST entry is also the build's GOAL BOUND, the sentence M3's
# rescope rule may not amend: folded into the description rather than given a slot of its own,
# because two slots that must agree are one fact in two places.
SLOT_CANON = (
    ("## The problem this build exists to solve", False, False),
    ("## Expected improvements", False, True),
    ("## Detriments if this is not built", False, True),
    ("## Build-level rules", True, False),
    ("## Parked decisions", True, False),
)
# The registry declaring which build READMEs the canon BINDS. Unit 3 writes the file; this reader
# ships here so the predicate is complete before its population exists, and returns the EMPTY SET
# when the file is absent — which unit 3 then replaces with a refusal. Until then an empty
# population is legal and is ANNOUNCED on every run, because a rule binding nothing that reports
# `clean` is the vacuous-selector class this repo names.
CONTRACT_REGISTRY = "project/readme-contract.txt"

# TOOL-dFramedEntrypoint-6 — records render inside the SPEC they serve. The pair sits between a
# spec's status header and its first numbered section, which is the one place in a spec that hygiene
# check 12 does not look: its section-equality compare collects `## ` headings and this is not one,
# and its empty-body walk has not started. Measured on a scratch clone before the unit was written.
# An eleventh `## ` section would have needed a new canon AND a dated cutoff, and would have left
# every landed spec without the region.
SPEC_RECORDS_OPEN = "<!-- gen:spec-records -->"
SPEC_RECORDS_CLOSE = "<!-- /gen:spec-records -->"
# The stamped header names THIS install's prefix, derived from the module's own location rather
# than spelled. It is written INTO the adopter's generated artifacts and committed there, so a
# hardcoded prefix does not merely mislead — it lands a dead path in their tree, and the byte-compare
# that guards these files happily agrees with it. `kit_rel()` falls back to the bare kit name when the
# module sits outside the resolved root (a test fixture, an odd checkout); the header is a pointer,
# never a gate input.
def kit_rel() -> str:
    here = pathlib.Path(__file__).resolve().parent
    for anc in [here] + list(here.parents):
        if (anc / ".git").exists():
            try:
                return here.relative_to(anc).as_posix()
            except ValueError:
                break
    return here.name


GEN_HEADER = (
    f"<!-- generated by {kit_rel()}/gen_build_index.py --write — do not hand-edit -->"
)

STATUS_TOKENS = ("OPEN", "SPECCED", "INPROGRESS", "BLOCKED", "DEFERRED", "CLOSED", "WONTDO")
TERMINAL = ("CLOSED", "WONTDO")
# Precedence for the derived status, most-live first. A build is as live as its liveliest unit.
PRECEDENCE = ("INPROGRESS", "BLOCKED", "OPEN", "SPECCED", "DEFERRED")

HDR_RE = re.compile(
    r"^\*\*Status:\*\* (?P<token>" + "|".join(STATUS_TOKENS) + r")"
    r" · rev-(?P<rev>\d+) · (?P<date>\d{4}-\d{2}-\d{2}) · node (?P<node>[a-z])"
    r" · Tier-(?P<tier>[12]) · base (?P<base>[0-9a-f]{8,})"
)
H1_RE = re.compile(r"^#\s+(?P<id>[A-Za-z0-9][A-Za-z0-9-]*)\s+—\s+(?P<title>.+?)\s*$")
# The build-order verb, appended after `base` in a spec's status header. Units sharing a value are
# the parallel group; the owner resolved against a second `group` verb, which would have needed its
# own contradiction refusals to render an identical region.
# TOOL-dFramedEntrypoint-4 S2 — ANCHORED on both sides. The shipped form ended `(?![0-9])`, which
# rejects a longer number and nothing else: `order 0x2` matched `0` and rendered as step 0, and
# `order 2x` matched `2` and rendered as step 2 — both probed on the shipped regex before this change.
# A malformed value must be a REFUSAL rather than a plausible step, so the trailing context is now a
# field separator or end-of-header, and `parse_spec` raises on a value that looks like the verb but
# does not conform. That refusal is what makes the verb safe to require later; a silent misread is
# the shape TOOL-aRuledFrontispiece-2's §4 specified and never shipped.
ORDER_RE = re.compile(r"·\s*order\s+(\d+)\s*(?=·|$)")
ORDER_LOOSE_RE = re.compile(r"·\s*order\s+(\S+)")
SHARD_RE = re.compile(r"^\d{4}-\d{2}\.md$")
REQUIRED_KEYS = ("slug", "node", "opened", "streams", "roster", "ids")


class Problem(Exception):
    """A named, user-facing failure. Never a traceback: blind spot 3."""


class StaleHeader(Problem):
    """A build README header that is PRESENT and does not conform — NOT one that is absent.

    TOOL-dRetiredFork-3, absorbed from NicoCares `nc carve-out 9/20`. Those two states were one
    `Problem` here, so a CORRUPTED header read as a MISSING one and the index regenerated around it.
    They are different animals: an absent header is a build nobody wrote front matter for, and a
    corrupt one is front matter that rotted after someone did.

    It subclasses `Problem` rather than `Exception` directly, so an unhandled one still reports as a
    named failure instead of a traceback — this file's blind-spot-3 rule. `collect()` catches it
    specifically, BEFORE the generic handler, and decides tolerance there.
    """

    def __init__(self, path: str, region: str, detail: str) -> None:
        super().__init__(f"{path}: header present but unparseable — {detail}")
        self.path = path
        self.region = region
        self.detail = detail


# --------------------------------------------------------------------------------------- plumbing
#: The variables git EXPORTS to a hook, which then reach any subprocess that hook starts.
#: TOOL-dRetiredFork-2, absorbed from NicoCares `nc carve-out 16/20`. Taken VERBATIM from gov's own
#: hook-side scrub at `.githooks/pre-push` rather than re-derived, because these are two halves of
#: ONE defect and a second list would be the place they drift apart.
_GIT_ENV_LEAKS = (
    "GIT_DIR",
    "GIT_WORK_TREE",
    "GIT_INDEX_FILE",
    "GIT_OBJECT_DIRECTORY",
    "GIT_ALTERNATE_OBJECT_DIRECTORIES",
    "GIT_COMMON_DIR",
    "GIT_NAMESPACE",
    "GIT_PREFIX",
)


def _build_git_env() -> dict[str, str]:
    """The parent environment with git's exported repository pointers removed.

    Git exports `GIT_DIR` whenever the repository is reached through a `.git` FILE rather than a
    `.git` directory — every linked worktree — so a generator started from a hook inherits a pointer
    to a DIFFERENT tree than the one it was asked about, and reads it silently. There is no error;
    the answer is just about the wrong repository.

    Named `_build_git_env` and not nc's `_clean_git_env`: gov's lexicon table declares no `clean`
    verb, and `build` is declared as "create a new value and return it", which is exactly this.
    """
    return {k: v for k, v in os.environ.items() if k not in _GIT_ENV_LEAKS}


def run(*argv: str, cwd: str | None = None) -> str:
    # `env=` HERE, at the one choke point every git call in this file goes through, rather than at
    # seven call sites that would each have to remember.
    return subprocess.run(
        argv, cwd=cwd, capture_output=True, text=True, check=True, env=_build_git_env()
    ).stdout


def read_text(path: str) -> str:
    # Bytes in, decode, normalise CR. Windows checkouts hand back CRLF and every comparison below
    # would then differ on every line — the exact green-by-accident shape a byte gate must not have.
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8").replace("\r\n", "\n")


def read_text_or_none(path: str) -> tuple[str | None, str]:
    """(text, "") or (None, why). The ONE reader for scanners that walk ARBITRARY tracked files.

    TOOL-dScrubbedConduit-1 S1. Three scanners — spec_ids, read_bindings and rosters — read whatever
    `git ls-files` hands them, and each had invented its own guard: two caught `OSError`, one caught
    `Problem`. None of the three catches `UnicodeDecodeError`, which is what `read_text` actually
    raises on a tracked binary, so a single PNG under a build's `reviews/` took the whole generator
    down with a traceback. An adopter hit exactly that: a UI review screenshot is a legitimate record.

    `except Problem` at the third site was DEAD CODE — `read_text` raises `OSError` or
    `UnicodeDecodeError` and never `Problem`. And the obvious repair, `(Problem, UnicodeDecodeError)`,
    still dies with `FileNotFoundError` on a tracked-but-missing file, which the two sibling sites
    already survived. Hence one helper with one named tuple, rather than three near-misses.

    Deliberately NOT a blanket `except Exception`: a caller that cannot read a file must be able to
    tell "not text" and "not there" from "the reader is broken".
    """
    try:
        return read_text(path), ""
    except (OSError, UnicodeDecodeError) as exc:
        return None, f"unreadable: {exc}"


def write_text(path: str, text: str) -> None:
    # BYTES, never write_text(): on Windows the text mode would re-expand \n to \r\n and the very
    # next --check would report the file this call just wrote as stale.
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "wb") as fh:
        fh.write(text.encode("utf-8"))


# TOOL-aWeldedTribunal-5 -- ONE `.memory-tree.conf` parser for the whole kit. Six readers held an
# identical naive body while the shell gate SOURCES the same file, so a legal spelling bash accepts
# and the python half mis-read REMOVED coverage with the gate still green. `row_grammar.py` already
# used this sys.path pattern to reach a sibling; the edges are new and are priced in the unit's
# section 4, against a backlog row that claimed reuse here was free.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus_ids import parse_conf  # noqa: E402  the kit's ONE conf parser

def load_conf(root: str) -> dict:
    conf = {"MEMORY_ROOT": "memory", "DISCIPLINES": "", "FAMILIES": ""}
    path = os.path.join(root, ".memory-tree.conf")
    if os.path.isfile(path):
        parse_conf(read_text(path), conf)
    return conf


def unfenced_lines(text: str):
    """Yield (lineno, line) for every line OUTSIDE a fenced block, then the open fence's line.

    The final yield is `(opened_at, None)` when the document ends inside a fence, and nothing when it
    does not. A caller that only wants the text ignores it; a caller that must REFUSE a document it
    could not fully read needs it, and no reader in either kit had it — the shell `_unfenced` and this
    module's own generator both end silently with the fence still open, dropping every later line at
    exit 0. That is invisible by construction: a fence opened near the top of a row document hides
    every duplicate below it, and hiding duplicates is what the check that reads this exists to stop.
    """
    fence = ""
    opened_at = 0
    for n, line in enumerate(text.split("\n"), 1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            mark = "```" if stripped.startswith("```") else "~~~"
            if not fence:
                fence, opened_at = mark, n
                continue
            # Only the marker that OPENED the fence closes it: a ``` line inside a ~~~ block is
            # content, not a toggle.
            if mark == fence:
                fence = ""
                continue
        if not fence:
            yield n, line
    if fence:
        yield opened_at, None


def unfenced(text: str):
    """The text-only view, kept as the one fence machine's façade rather than a second copy."""
    for _n, line in unfenced_lines(text):
        if line is not None:
            yield line


# ----------------------------------------------------------------------------------------- parsing
def parse_front_matter(path: str, slug: str) -> dict:
    """Front matter opens at LINE 1 and nowhere else.

    `---` is also a markdown horizontal rule, and one already separates the two merged halves of a
    real build README in the originating corpus. A parser that scanned for the first two `---`
    anywhere would swallow that whole half as front matter.
    """
    lines = read_text(path).split("\n")
    # THE ONE ABSENT CASE. Line 1 is not `---`, so no header was ever opened and there is nothing to
    # call stale. Every failure BELOW this point is a header that opened and then did not conform,
    # and those raise StaleHeader — TOOL-dRetiredFork-3, which is the whole distinction.
    if not lines or lines[0].strip() != "---":
        raise Problem(f"{path}: no front matter — line 1 must be '---' (build '{slug}')")

    def _extract_region(upto: int | None = None) -> str:
        """The raw header text, for the report. Bounded so a file with no closing `---` cannot
        hand the operator the entire document as its 'region'."""
        return "\n".join(lines[: (upto if upto is not None else min(len(lines), 40))])

    fm: dict = {}
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
        if not line.strip():
            continue
        if line[:1].isspace():
            raise StaleHeader(
                path, _extract_region(i + 1),
                f"line {i + 1}: front-matter key is indented — keys live at COLUMN 0, and an "
                f"indented key is silently dropped by every simple parser",
            )
        if ":" not in line:
            raise StaleHeader(path, _extract_region(i + 1), f"line {i + 1}: not 'key: value'")
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    if end is None:
        raise StaleHeader(path, _extract_region(), "front matter opened at line 1 but never closed with '---'")
    missing = [k for k in REQUIRED_KEYS if k not in fm]
    if missing:
        raise StaleHeader(path, _extract_region(end + 1), f"missing required key(s): {', '.join(missing)}")
    if fm["slug"] != slug:
        raise StaleHeader(path, _extract_region(end + 1),
                          f"front matter slug '{fm['slug']}' != folder name '{slug}'")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fm["opened"]):
        raise StaleHeader(path, _extract_region(end + 1),
                          f"opened '{fm['opened']}' is not a YYYY-MM-DD date")
    if "status" in fm and fm["status"] not in STATUS_TOKENS:
        raise Problem(f"{path}: status '{fm['status']}' is not one of {' '.join(STATUS_TOKENS)}")
    return fm


def _parse_order(header: str, path: str):
    """The build-order verb, or None. A value that LOOKS like the verb but does not conform REFUSES.

    Dropping a malformed value silently would be worse than the misread it replaces: the unit would
    simply render as unordered, and an author who typed a bad value would see a plausible build order
    with their unit missing from it.
    """
    # ORDER MATTERS HERE, and the first draft got it wrong: the duplicate check sat BELOW the
    # early return, so a header whose FIRST occurrence was well-formed never reached it. The refusal
    # existed, read correctly, and was unreachable. Caught by running it rather than by reading it.
    if len(ORDER_LOOSE_RE.findall(header)) > 1:
        raise Problem(f"{path}: status header carries the `order` verb more than once, so which step "
                      f"this unit occupies has two answers")
    ok = ORDER_RE.search(header)
    if ok:
        return int(ok.group(1))
    loose = ORDER_LOOSE_RE.search(header)
    if loose:
        raise Problem(f"{path}: status header carries `order {loose.group(1)}`, which is not a "
                      f"positive integer followed by a field separator or the end of the header")
    return None


def parse_spec(path: str) -> dict | None:
    """Return the unit record, or None when the file carries no parseable status header.

    A grandfathered recording legitimately has none; check 12 already rejects a post-cutoff spec
    that is missing one, so this file never has to defend against a malformed header.
    """
    body = list(unfenced(read_text(path)))
    hdr = None
    for line in body[:5]:
        m = HDR_RE.match(line)
        if m:
            hdr = m
            break
    if hdr is None:
        return None
    unit_id, title = os.path.basename(path)[:-3], ""
    for line in body[:5]:
        m = H1_RE.match(line)
        if m:
            unit_id, title = m.group("id"), m.group("title")
            break
    return {
        "path": path,
        "id": unit_id,
        "title": title,
        "status": hdr.group("token"),
        "rev": hdr.group("rev"),
        "date": hdr.group("date"),
        # PERMITTED, never required (fork 5). HDR_RE has no end anchor, so a header carrying this
        # verb parses identically with or without it and no landed spec goes retroactively red.
        "order": _parse_order(hdr.string, path),
        # Tier was captured by HDR_RE and discarded here, one line after the match. The roster now
        # renders it, which costs this key and one cell. It is MANDATORY in the header regex, so a
        # unit row always has a value and only the ORDER cell can be empty.
        "tier": hdr.group("tier"),
    }


# ------------------------------------------------------------------------------ record -> spec bindings
# Every record under a build's non-spec folders names the spec(s) it is
# evidence about, in its own head. This parser READS that and CLASSIFIES; it never raises, because
# `collect()` is reached by both --check and --write through one call site, so a raising parser would
# let one unannotated record refuse to render every artifact.
BIND_HEAD_LINES = 12
RECORD_KIND_TOKENS = ("spec-audit", "diff-review", "journal", "research")
# Optional leading whitespace and an optional comment marker: the corpus holds a non-markdown record
# (a shell script), where the line can only be a comment. An extension-scoped rule would structurally
# exclude the one file most easily forgotten.
BIND_RE = re.compile(
    r"^[ \t]*(?:#+|//|;)?[ \t]*\*\*(?P<key>Serves|Commissions):\*\*[ \t]+(?P<rest>.*\S)[ \t]*$"
)
UNBOUND_RE = re.compile(r"^none\b[\s—–:-]*(?P<reason>\S.*)$")


def _id_alternation(conf: dict) -> str:
    fams = [p.split(":", 1)[1] for p in conf.get("FAMILIES", "").split() if ":" in p]
    return "|".join(sorted(fams)) or "(?!)"


def spec_ids(root: str, tracked: list, conf: dict) -> set:
    """The resolution set: ids DEFINED by a spec H1, one per file, at any depth under a build's spec/.

    Deliberately NOT the build README `ids:` roster. That roster is a reservation RANGE generated from
    citations anywhere, and it admits backlog and decision rows as if they were units — measured on
    this corpus, two thirds of its ids had no spec at all. Resolving a record against it would let a
    binding name something no spec ever defined.
    """
    m = conf["MEMORY_ROOT"]
    pat = re.compile(r"^#\s+[`*]*(?P<id>(?:" + _id_alternation(conf) + r")-[A-Za-z0-9]+-\d+)\b")
    sel = re.compile(r"^" + re.escape(m) + r"/builds/[^/]+/spec/")
    out = set()
    for rel in tracked:
        if not sel.match(rel):
            continue
        text, _why = read_text_or_none(os.path.join(root, rel))
        if text is None:
            continue
        for line in unfenced(text):
            mm = pat.match(line)
            if mm:
                out.add(mm.group("id"))
                break
    return out


def record_paths(tracked: list, m: str) -> list:
    """Every tracked record: any depth, ANY extension, under a build's non-spec kind folders."""
    kinds = "|".join(k for k in RECORD_KINDS if k != "spec")
    sel = re.compile(r"^" + re.escape(m) + r"/builds/[^/]+/(?:" + kinds + r")/")
    return [p for p in tracked if sel.match(p)]


def _expand_ids(rest: str, alt: str) -> tuple:
    """Return (ids, bad_tokens). A contiguous run may be written N..M and EXPANDS here, at authoring
    time, to a fixed set — unlike a wildcard it cannot rot when the build later gains a unit."""
    ids, bad = [], []
    one = re.compile(r"^(?P<fam>" + alt + r")-(?P<slug>[A-Za-z0-9]+)-(?P<seq>\d+)(?:@rev-\d+)?$")
    rng = re.compile(r"^(?P<fam>" + alt + r")-(?P<slug>[A-Za-z0-9]+)-(?P<lo>\d+)\.\.(?P<hi>\d+)$")
    for tok in rest.split():
        mo = one.match(tok)
        if mo:
            ids.append(f"{mo.group('fam')}-{mo.group('slug')}-{mo.group('seq')}")
            continue
        mr = rng.match(tok)
        if mr and int(mr.group("lo")) <= int(mr.group("hi")):
            for n in range(int(mr.group("lo")), int(mr.group("hi")) + 1):
                ids.append(f"{mr.group('fam')}-{mr.group('slug')}-{n}")
            continue
        bad.append(tok)
    return ids, bad


def read_bindings(root: str, tracked: list, conf: dict) -> dict:
    """path -> {state, kind, ids, commissions, reason, bad}.

    Does not raise for an UNREADABLE file — a decode or IO failure becomes a `state` row carrying
    `why`. It CAN still raise for a malformed conf. The former docstring said "Never raises."
    unqualified, which is what let the blanket catch at the caller look reasonable.

    state is one of: bound · unbound · malformed · absent.
    """
    m = conf["MEMORY_ROOT"]
    alt = _id_alternation(conf)
    out = {}
    for rel in record_paths(tracked, m):
        rec = {"state": "absent", "kind": None, "ids": [], "commissions": [], "reason": None,
               "bad": [], "why": "no Serves line in the first %d unfenced lines" % BIND_HEAD_LINES}
        try:
            text = read_text(os.path.join(root, rel))
        except UnicodeDecodeError:
            # NOT TEXT, so NOT A RECORD (TOOL-dScrubbedConduit-1 S1). A record is prose that carries a
            # `**Serves:**` line binding it to a spec; a file that does not decode cannot carry one,
            # and emitting it as an `A` row only moves the failure to hygiene check 21, which would
            # then demand a Serves line from a PNG. record_paths admits ANY extension by design — a
            # record's kind comes from its folder, not its suffix — so the exclusion belongs here,
            # where the bytes are actually read, rather than in a filename guess upstream.
            #
            # An adopter carrying a UI review screenshot under `reviews/` is the case this serves.
            continue
        except OSError as exc:
            # Present in the index and unreadable from disk is a REAL anomaly and stays a row.
            rec["why"] = f"unreadable: {exc}"
            out[rel] = rec
            continue
        for line in list(unfenced(text))[:BIND_HEAD_LINES]:
            mo = BIND_RE.match(line)
            if not mo:
                continue
            # A trailing HTML comment is a NOTE, not a token. The retrofit records the adjudication
            # rule that produced an inferred binding on the line itself, so a reviewer grades it in
            # the file rather than in a commit body no gate reads — and without this the note's
            # every word parsed as a malformed id.
            rest = mo.group("rest").split("<!--", 1)[0].strip()
            if not rest:
                continue
            if mo.group("key") == "Commissions":
                cids, bad = _expand_ids(rest, alt)
                rec["commissions"] = cids
                rec["bad"] += bad
                continue
            if rec["state"] != "absent":
                continue                      # first Serves line wins
            un = UNBOUND_RE.match(rest)
            if un:
                # The kind is OPTIONAL here and required below: an unbound record names no ids, so
                # there is no relation for a kind token to describe. The REASON is mandatory either
                # way — a bare `none` is malformed, because "no gate named" and "gate not yet
                # written" are indistinguishable from outside and only one of them is acceptable.
                rec["state"] = "unbound"
                rec["reason"] = un.group("reason")
                rec["why"] = ""
                continue
            toks = rest.split()
            if toks and toks[0] in RECORD_KIND_TOKENS:
                ids, bad = _expand_ids(" ".join(toks[1:]), alt)
                rec["kind"] = toks[0]
                rec["ids"] = ids
                rec["bad"] += bad
                if not ids:
                    rec["state"] = "malformed"
                    rec["why"] = "kind token with no resolvable id"
                else:
                    rec["state"] = "bound"
                    rec["why"] = ""
            else:
                rec["state"] = "malformed"
                got = toks[0] if toks else "(empty)"
                rec["why"] = (f"first token {got} is not one of "
                              + " ".join(RECORD_KIND_TOKENS) + ", and the line is not the none form")
        out[rel] = rec
    return out


def cmd_print_bindings(root: str, conf: dict) -> int:
    """READ-ONLY. Classifies and prints; writes nothing and always exits 0.

    It is the retrofit's own checklist AND the predicate the gate reads, so a seed list and a gate
    that disagree is structurally impossible here.
    """
    m = conf["MEMORY_ROOT"]
    tracked = [p for p in run("git", "ls-files", cwd=root).split("\n") if p]
    defined = spec_ids(root, tracked, conf)
    binds = read_bindings(root, tracked, conf)
    unbound = 0
    for rel in sorted(binds):
        rec = binds[rel]
        if rec["state"] in ("absent", "malformed"):
            print(f"A\t{rel}\t{rec['why']}")
            continue
        if rec["state"] == "unbound":
            unbound += 1
        # One S row per BOUND record, carrying the resolved SET. A conformant record is not a
        # finding, so the A/B/N rows say nothing about it — and check 21's filename-vs-header
        # branch needs exactly this set to test membership against. Without it that branch would
        # have to parse every record a second time, which is the two-answers class in the one
        # place this build exists to remove it.
        if rec["state"] == "bound":
            print(f"S\t{rel}\t{rec['kind']}\t{' '.join(rec['ids'])}")
        for tok in rec["bad"]:
            print(f"B\t{rel}\t{tok} is not a family-qualified id or range")
        for i in rec["ids"] + rec["commissions"]:
            if i not in defined:
                print(f"B\t{rel}\t{i} is named but no spec H1 in this tree defines it")
    print(f"N\t{unbound}")
    return 0


def derive_status(units: list, fm: dict, readme: str) -> str:
    parsed = [u for u in units if u]
    if not parsed:
        if "status" not in fm:
            raise Problem(
                f"{readme}: no spec under this build carries a parseable **Status:** header, so the "
                f"build status cannot be derived — declare it explicitly with a 'status:' front-matter key"
            )
        return fm["status"]
    if "status" in fm:
        raise Problem(
            f"{readme}: front matter declares 'status: {fm['status']}' but {len(parsed)} spec(s) "
            f"carry a status header — the build status is DERIVED from them, and two answers to one "
            f"question is exactly the drift this index removes. Delete the 'status:' key."
        )
    seen = {u["status"] for u in parsed}
    for token in PRECEDENCE:
        if token in seen:
            return token
    return "WONTDO" if seen == {"WONTDO"} else "CLOSED"


# ----------------------------------------------------------------------------------- roster scanning
def _roster_sort_key(i: str):
    """Family, then NUMERIC sequence. Lexical order puts `-10` before `-2`, which reads as data loss
    to anyone scanning the rendered list for the newest id."""
    return (i.split("-", 1)[0], int(i.rsplit("-", 1)[1]))


def rosters(root: str, tracked: list, m: str, families: set) -> dict:
    """slug -> sorted ids belonging to that build, from the id's own slug component.

    An id spells its build: family-slug-sequence. So a build's roster needs no side table and no
    anchor grammar — only the declared family alternation, which this module already loads. The
    sequence must be all DIGITS: revision-suffixed anchors (`-6q`) are amendments to a decision, not
    ids of their own, and admitting them multiplied one build's roster from 8 to 38.

    THE READ SET EXCLUDES THIS FIELD'S OWN OUTPUTS. A build's README is skipped for its OWN slug, and
    the generated index and shards are skipped entirely, because all three are rendered FROM the
    value being derived. A derivation that reads its own output cannot correct a wrong value — it
    republishes it forever, and every gate agrees, because a fresh render reproduces it exactly. That
    is the defect this change exists to remove, so it must not be reintroduced by the fix.
    """
    fam = "|".join(sorted(re.escape(f) for f in families))
    if not fam:
        raise Problem("build-index: FAMILIES is empty, so no id can be recognised and every roster "
                      "would render empty — which is also what a clean corpus looks like")
    id_re = re.compile(r"\b(?:" + fam + r")-([A-Za-z0-9]+)-\d+\b")
    out: dict = {}
    for p in tracked:
        if p == f"{m}/LIVE.md" or p.startswith(f"{m}/ledger/"):
            continue
        text, _why = read_text_or_none(os.path.join(root, p))
        if text is None:
            # A roster is built from ids in PROSE, so a file that is not text cannot contribute one
            # and skipping it changes no output. Verified by artifact equality, not by assertion.
            continue
        for mm in id_re.finditer(text):
            slug = mm.group(1)
            if p == f"{m}/builds/{slug}/README.md":
                continue
            out.setdefault(slug, set()).add(mm.group(0))
    return {s: sorted(v, key=_roster_sort_key) for s, v in out.items()}


# --------------------------------------------------------------------------------------- collecting
#: Where the tolerated-header rows live. Sibling of the nine registries already under this dir.
STALE_HEADER_WAIVER = "project/stale-header-waiver.txt"


def read_stale_header_waiver(root: str, m: str, tracked: list) -> dict:
    """The tolerated set, read ONCE per collect() and never per file.

    Read at the CALLER and not inside the parser, which is the seam nc's own comment argues for and
    is right about: a parser that knows about tolerance cannot be reused by a caller that wants
    strictness, and this parser has two readers who want different answers.

    A MISSING file refuses. An EMPTY one is the expected state — the mechanism is inert until a
    header actually corrupts — and a row naming a path the tree no longer tracks refuses, because a
    stale exception cannot hide a live hit.
    """
    rel = f"{m}/{STALE_HEADER_WAIVER}"
    full = os.path.join(root, rel)
    if not os.path.exists(full):
        raise Problem(
            f"{rel}: absent. The stale-header waiver registry is REQUIRED even when empty — a file "
            f"nobody created is a decision nobody made, and defaulting it to empty would silently "
            f"disarm the distinction it exists to keep."
        )
    rows = {}
    for line in read_text(full).split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        path, _, why = line.partition(" ")
        rows[path.strip()] = why.strip()
    stale = sorted(p for p in rows if p not in tracked)
    if stale:
        raise Problem(
            f"{rel}: {len(stale)} row(s) name a path the tree does not track, so the exception "
            f"outlived the header it excused: {', '.join(stale)}"
        )
    return rows


def collect(root: str, conf: dict) -> list:
    m = conf["MEMORY_ROOT"]
    tracked = [p for p in run("git", "ls-files", "--", m + "/", cwd=root).split("\n") if p]
    stale_waived = read_stale_header_waiver(root, m, tracked)
    tolerated: list = []
    slugs = sorted({p.split("/")[2] for p in tracked if p.startswith(m + "/builds/") and p.count("/") >= 3})
    disciplines = set(conf["DISCIPLINES"].split())
    families = {pair.split(":")[1] for pair in conf["FAMILIES"].split() if ":" in pair}
    # Two granularities, as the hygiene engine's own guard does it. The PRECONDITION asks whether the
    # scan recognised anything at all; the per-build POPULATION asks whether this build did. Without
    # the first, a families list bound to the wrong tree renders every roster empty — and an empty
    # classification is exactly what a clean corpus yields, so the failure would look like success.
    roster_by_slug = rosters(root, tracked, m, families)
    # NO EMPTINESS PRECONDITION HERE, deliberately. The wrong-root class says an unrecognising
    # grammar yields the same empty result a clean corpus does, so a guard is wanted — but every
    # signal available HERE is one this function derives from the same conf, which makes the
    # assertion a tautology (the repo's assertion-between-two-derived-values class). Build count
    # fails on a sparse tree; spec-file existence fails too, because a legacy recording legitimately
    # carries no id. The guard that actually holds is INDEPENDENT and already runs below: every
    # build's authored `roster:` value must be a declared family, so a FAMILIES list bound to the
    # wrong tree reds there, by name, before any roster is rendered.
    builds = []
    for slug in slugs:
        readme = f"{m}/builds/{slug}/README.md"
        if readme not in tracked:
            raise Problem(
                f"{m}/builds/{slug}/: no tracked README.md — a build with no front matter cannot be "
                f"indexed, and an unindexed build is a silent departure from the universe"
            )
        try:
            fm = parse_front_matter(os.path.join(root, readme), slug)
        except StaleHeader as exc:
            # PRESENT and unparseable. Tolerance is decided HERE, by the caller, from the registry
            # read once above — never inside the parser.
            if readme not in stale_waived:
                raise Problem(
                    f"{exc}\n"
                    f"  the header region follows; repair it, or add a row to "
                    f"{m}/{STALE_HEADER_WAIVER} naming this path and why:\n"
                    f"{exc.region}"
                ) from None
            tolerated.append(readme)
            continue
        for value in fm["streams"].split("+"):
            if disciplines and value.strip() not in disciplines:
                raise Problem(f"{readme}: streams value '{value.strip()}' is outside the DISCIPLINES enum")
        for value in fm["roster"].split("+"):
            if families and value.strip() not in families:
                raise Problem(f"{readme}: roster value '{value.strip()}' is outside the FAMILIES set")
        specs = sorted(p for p in tracked if p.startswith(f"{m}/builds/{slug}/spec/") and p.endswith(".md"))
        units = [parse_spec(os.path.join(root, p)) for p in specs]
        # BOOTSTRAP, not failure. A build whose ids appear nowhere but its own README is young, not
        # broken, and there is nothing to correct the authored value against — so it stands. The
        # anti-self-reference property still holds where it can bite: the moment any independent
        # source names the id, the derivation takes over and a wrong authored value loses. Global
        # emptiness is the dangerous case, and the precondition above owns it.
        roster = roster_by_slug.get(slug) or [i for i in fm["ids"].split() if i]
        # Which record folders this build actually HAS. Authored as prose in 17 READMEs and wrong
        # in 15 of them: the sentence is written when a build opens, predicting the folders it will
        # grow, and nothing revisits it. Seven claim a build/ that was never created.
        kinds = [k for k in RECORD_KINDS
                 if any(t.startswith(f"{m}/builds/{slug}/{k}/") for t in tracked)]
        builds.append(
            {
                "slug": slug,
                "readme": readme,
                "fm": fm,
                "roster": roster,
                "kinds": kinds,
                # Every tracked record, for the document-inventory region. The filename grammar is
                # NOT parsed: five files under legacy-files.txt carry grandfathered names, and a
                # renderer that parsed names would have to waive them or render them degraded.
                "docs": sorted(t for t in tracked
                               if any(t.startswith(f"{m}/builds/{slug}/{k}/") for k in RECORD_KINDS)),
                "parents": [s.strip() for s in fm.get("parents", "").split() if s.strip()],
                "units": [u for u in units if u],
                "status": derive_status(units, fm, readme),
            }
        )
    # UNCONDITIONALLY, including at zero — the ratified F2. A clean run that printed nothing here
    # would be indistinguishable from a check that never consulted the registry at all, and a
    # tolerance that grows silently is the failure this whole mechanism exists to prevent.
    print(f"build-index: {len(tolerated)} header(s) tolerated by waiver")
    return builds


# ---------------------------------------------------------------------------------------- rendering
def render_region(build: dict) -> str:
    fm = build["fm"]
    out = [
        MARK_OPEN,
        # `unit(s)` and `ids` answer DIFFERENT questions and are deliberately not reconciled: a unit
        # is a spec carrying a status header, a roster member is an id that exists in the record.
        # aUnmannedHelm is 7 and 10 because three of its ids never got a spec. Rendering them as one
        # number would re-create, inverted, the defect this derivation removes.
        f"**Build status:** {build['status']} · {len(build['units'])} unit(s) · node {fm['node']} · "
        f"opened {fm['opened']} · streams {fm['streams']}",
    ]
    # THE FULL ROSTER STAYS, WRAPPED. Replacing it with a count would reverse TOOL-aMouldedFolio-2 S4,
    # which deliberately renders the full roster HERE and only the count in LIVE.md and the ledger —
    # and render_region's own comment above says `unit(s)` and `ids` answer different questions.
    #
    # WRAPPED AT 300, one tier BELOW the 350 this class is capped at. `length()` in the entry-budget
    # awk counts bytes or characters depending on the awk build and the ambient locale, which that
    # check's own comment refuses to pin — and this line carries six two-byte middots. A render
    # sitting exactly at the cap would pass on one node and red on another.
    out += _wrap_ids(build["roster"])
    out.append("")
    # TOOL-aBoundedVerdict-11 S1 — the units table gets its own NESTED marker pair. The unattended
    # driver used to select unit rows out of the enclosing region by ROW SHAPE (`^| \[`), which also
    # matches the records table below, so every review and journal record counted as an unfinished
    # unit and `build-complete` could not pass on any build holding a record. The pair is nested
    # rather than a new GEN_REGIONS entry so the enclosing region's extent is byte-unchanged and the
    # three legs and two dossiers that bracket it keep working; what changes is that the units table
    # now has an ADDRESS a reader can name instead of a shape it has to guess.
    out.append(UNITS_OPEN)
    if build["units"]:
        # TOOL-dFramedEntrypoint-4 S4/S5 — ORDER and TIER join the roster, and the sort key becomes
        # the BUILD order rather than the path. Both values were already parsed and thrown away: tier
        # was a named group of HDR_RE discarded one line after the match, and order reached only the
        # order region. The LINK CELL STAYS FIRST and STATUS STAYS A WHOLE |-DELIMITED CELL, because
        # the unattended driver selects unit rows by `^| \[.*\]\(spec/` and terminal units by
        # `| (CLOSED|WONTDO) |`; inserting columns between them is safe, moving either is not.
        # Only ORDER can be empty — tier is mandatory in the header regex, so a row that exists has one.
        out += ["| Unit | Order | Tier | Status | Rev | Last change |", "|---|---|---|---|---|---|"]
        for u in sorted(build["units"], key=lambda x: (x.get("order") is None, x.get("order") or 0,
                                                       x["id"])):
            rel = u["path"].split(f"/builds/{build['slug']}/", 1)[1]
            label = f"{u['id']} — {u['title']}" if u["title"] else u["id"]
            order = str(u["order"]) if u.get("order") is not None else "—"
            out.append(f"| [{label}]({rel}) | {order} | {u.get('tier', '—')} | {u['status']} | "
                       f"rev-{u['rev']} | {u['date']} |")
    else:
        out.append("*No spec under this build carries a status header; the status above is declared "
                   "in the front matter.*")
    out.append(UNITS_CLOSE)
    # TOOL-dFramedEntrypoint-5 S4b — the derived folder sentence is GONE, and it was the record
    # selector's liveness assertion: nine arms detected a mis-segmented selector by noticing the
    # sentence went missing. What replaces it is an explicit NON-EMPTY assertion over the selector,
    # stated as a rendered fact rather than inferred from a sentence's presence. A build that holds
    # records and shows a zero here is a mis-segmented selector, which is exactly what the sentence
    # used to reveal by vanishing.
    recs = build.get("records") or []
    out += ["", f"Records: {len(recs)} bound to this build, across "
                f"{len(build['kinds'])} record folder(s)."]
    # THE TABLE IS GONE — the owner ruled records belong in the specs they serve, and unit 6 renders
    # them there. THE TWO COVERAGE JOINS STAY, and they are the only spec-to-record coverage signal in
    # this repo: hygiene check 21 grades record-to-spec and does not cover this direction. They are
    # COMPUTED from the build's records and units, never parsed from the table, so the data survived
    # the deletion — but the emitting branch did not, and re-emitting it is the point of S3.
    #
    # UNCONDITIONAL. Each join used to hide behind its own non-empty test, so a build with FULL
    # coverage rendered NOTHING and was indistinguishable from a build whose joins were never
    # computed. That is the absence-reads-as-coverage class, and full coverage is the COMMON case,
    # not the rare one.
    named = {i for r in recs for i in r.get("ids", [])}
    audited = {i for r in recs if r.get("kind") == "spec-audit" for i in r.get("ids", [])}
    own = [u["id"] for u in build["units"]]
    gap = [i for i in own if i not in named]
    agap = [i for i in own if i not in audited]
    # WRAPPED, through the helper written for these two lines (TOOL-dRetiredFork-18). Both are
    # graded by check 7 against the AUTHORED-prose entry cap, and both grow with every unit a build
    # carries, so an unwrapped list makes a build's unit COUNT the bound — 24 units rendered 509 and
    # 531 characters against 350. `_render_wrapped_ids` was written for exactly this and carried
    # selftest arms while nothing called it; arms that grade a helper in isolation cannot see that.
    # The `none` branches stay UNWRAPPED and unchanged: the helper appends its own terminator and
    # would render `Ids no record names.`, a different sentence, for the commonest case of all.
    out += [""] + (_render_wrapped_ids("Ids no record names:", gap) if gap else
                   ["Ids no record names: none — every unit id is named by a record."])
    # NOT "unreviewed". The reviewed rev is optional, so this reports ids no spec-audit record names
    # EVER — a spec audited at rev-1 and since bumped does not appear here. An "unreviewed" label
    # would be a coverage claim the data cannot support.
    out += [""] + (_render_wrapped_ids("Ids no `spec-audit` record has ever named:", agap) if agap
                   else ["Ids no `spec-audit` record has ever named: none — every unit id has one."])
    out.append(MARK_CLOSE)
    return "\n".join(out)


IDS_WRAP = 300


def _render_id_ranges(ids: list) -> str:
    """`FAMILY-slug-2 … FAMILY-slug-15` as `FAMILY-slug-2..15`, contiguous runs only.

    A TABLE cell cannot wrap the way `_render_wrapped_ids` wraps a paragraph, so the bindings row needs
    a shorter spelling rather than more lines. This is `TOOL-dUnstalledConvoy-13`: a record serving
    a build past about eleven units cannot fit the row under the entry cap BY CONSTRUCTION, because
    the row carries the filename, the path AND every id it serves. Measured at 505 characters for a
    fourteen-unit spec audit, against a 350 ceiling.

    The range spelling is not invented here — it is the one the AUTHORING grammar already accepts and
    expands, so a reader of the generated row and a reader of a hand-written `Serves:` line are
    reading the same notation. Only a run of consecutive ordinals sharing a family and slug collapses;
    anything else is emitted verbatim, so a gap can never be swallowed by the abbreviation.
    """
    if not ids:
        return ""
    out, i = [], 0
    while i < len(ids):
        head = ids[i]
        stem, _, num = head.rpartition("-")
        if not num.isdigit():
            out.append(head)
            i += 1
            continue
        j, last = i, int(num)
        while j + 1 < len(ids):
            nstem, _, nnum = ids[j + 1].rpartition("-")
            if nstem != stem or not nnum.isdigit() or int(nnum) != last + 1:
                break
            j += 1
            last = int(nnum)
        out.append(head if j == i else f"{stem}-{int(num)}..{last}")
        i = j + 1
    return " ".join(out)


def _render_wrapped_ids(prefix: str, ids: list, cap: int = IDS_WRAP) -> list:
    """`<prefix> <id> <id> ….` as one or more lines, none wider than `cap`.

    Consecutive non-blank lines join into ONE markdown paragraph, so the wrap is invisible to a
    reader and the rendered text is unchanged — while every emitted line stays under the per-line
    entry cap check 7 enforces. Hit for real by a thirteen-unit build: the `spec-audit` gap line
    reached 399 characters against a 350 ceiling and the build could not be committed. The remedy
    must never be raising that ceiling, because this population grows with every unit a build
    carries, so a raise buys one build and reds the next. Same renderer-shaped class as
    `TOOL-dUnstalledConvoy-13` and NOT a fix for it: that row is the generated record-BINDINGS row,
    a different line with a different grammar, and it stays open.
    """
    lines, cur = [], prefix
    for i in ids:
        if cur not in ("", prefix) and len(cur) + 1 + len(i) > cap:
            lines.append(cur)
            cur = ""
        cur += (" " if cur else "") + i
    lines.append(cur + ".")
    return lines


def _wrap_ids(roster: list) -> list:
    """`ids` as one or more lines, none wider than IDS_WRAP. Empty roster renders no line at all."""
    if not roster:
        return []
    lines, cur = [], "ids"
    for i in roster:
        if len(cur) + 1 + len(i) > IDS_WRAP and cur != "ids":
            lines.append(cur)
            cur = "ids"
        cur += " " + i
    lines.append(cur)
    return lines


def render_order(build: dict) -> str:
    """The BUILD ORDER region. Units sharing an `order` value are the parallel group."""
    mo, mc = GEN_REGIONS[1][1], GEN_REGIONS[1][2]
    out = [mo, ""]
    steps = {}
    for u in build["units"]:
        if u.get("order") is not None:
            steps.setdefault(u["order"], []).append(u)
    if not steps:
        out.append("*No spec under this build declares an `order` verb; the build order is whatever "
                   "its authored plan states.*")
    else:
        out += ["| Step | Units | Parallel |", "|---|---|---|"]
        for n in sorted(steps):
            us = sorted(steps[n], key=lambda x: x["id"])
            ids = ", ".join(f"`{u['id']}`" for u in us)
            out.append(f"| {n} | {ids} | {'yes' if len(us) > 1 else 'no'} |")
        # RESIDUAL, stated rather than silently dropped: a unit with no verb is not ordered, and a
        # region that omitted it would read as a complete order while hiding a unit.
        rest = sorted((u["id"] for u in build["units"] if u.get("order") is None))
        if rest:
            out += ["", "Unordered: " + ", ".join(f"`{i}`" for i in rest) + "."]
    out.append(mc)
    return "\n".join(out)


def render_edges(build: dict) -> str:
    """The DEPENDENCY EDGE region. `parents:` is AUTHORED; the child set is DERIVED by inverting it.

    Slugs, never ids (fork 4). `rosters()` keys on an id's own slug component, so a slug joins no
    roster and this region leaves LIVE.md and both ledger shards byte-neutral. A bare id in a leading
    table cell would additionally ANCHOR via the extractor and rewrite the other build's `ids:` line.
    """
    mo, mc = GEN_REGIONS[2][1], GEN_REGIONS[2][2]
    out = [mo, ""]
    parents, children = build["parents"], build.get("children", [])
    if not parents and not children:
        out.append("*This build declares no parent and no build declares it as one.*")
    else:
        for label, vals in (("Parent", parents), ("Child", children)):
            if vals:
                links = ", ".join(f"[{s}](../{s}/README.md)" for s in sorted(vals))
                out.append(f"- **{label} builds:** {links}")
    out.append(mc)
    return "\n".join(out)


REGION_RENDERERS = {
    "build-index": render_region,
    "build-order": render_order,
    "build-edges": render_edges,
}

# TOOL-dFramedEntrypoint-5 S4c — `strip_records_sentence`, `RECORDS_SENTENCE` and `RECORDS_ANCHOR`
# were RETIRED here. They existed to remove an AUTHORED copy of a sentence this generator also
# rendered, so the tree carried one and not two. This unit stops rendering that sentence, and a
# remover whose subject is no longer generated is not inert: it deletes an author's sentence and
# writes nothing in its place, which is the prose-eating class the module's own `apply_region`
# warning names. Retired in the same commit that removes its subject rather than left to be
# rediscovered by whoever next writes the words "Records live under" in a build README.
def apply_front_matter_ids(readme_text: str, roster: list, readme: str) -> str:
    """Rewrite the front matter's `ids:` line from the roster, in place.

    Bounded exactly like `apply_region`: only the ONE line whose key is `ids` inside the front-matter
    block is touched, and the block ends at the first closing `---`. `parse_front_matter` has already
    proved the block opens at line 1 and closes, so this walk cannot run away; it still refuses
    rather than guessing if the key is absent, because writing a key that was never there would make
    this function a scaffolder, which it is not.
    """
    lines = readme_text.split("\n")
    want = ("ids: " + " ".join(roster)).rstrip()
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            break
        if line.startswith("ids:"):
            lines[i] = want
            return "\n".join(lines)
    raise Problem(f"{readme}: front matter has no 'ids:' line to rewrite")


def apply_region(readme_text: str, region: str, readme: str,
                 mark_open: str = MARK_OPEN, mark_close: str = MARK_CLOSE) -> str:
    """Replace the marked slice EXACTLY. Never a regex substitution over the whole file: this
    generator owns a region inside an AUTHORED file, and getting it wrong eats prose."""
    lines = readme_text.split("\n")
    # COLUMN 0, EXACT EQUALITY after one trailing CR — the contract the three awk readers in the
    # unattended kit already enforce. `.strip()` was permissive AND mutating: it accepted an
    # indented marker and a marker with trailing whitespace (two spaces is a Markdown hard break,
    # so an authored construct), then re-emitted the bare marker — silently rewriting a line the
    # author wrote, in a file they ran this tool over for another reason. Refusing is the only
    # reading that cannot edit prose behind the author.
    def _is(line, mark):
        # ONE trailing CR, not all of them. awk's `sub(/\r$/, "")` in the three unattended readers
        # removes exactly one, so `rstrip("\r")` would accept a line ending in two CRs that they
        # refuse — a divergence introduced by the very change that removed two others. It cannot be
        # demonstrated on an MSYS node, where the runtime strips CR before awk sees a byte, so it is
        # asserted at SOURCE level here rather than by a fixture that would pass either way.
        return check_marker_line(line, mark)
    opens = [i for i, l in enumerate(lines) if _is(l, mark_open)]
    closes = [i for i, l in enumerate(lines) if _is(l, mark_close)]
    if not opens and not closes:
        # NAMES THE PAIR IT WAS CALLED WITH, not the module constants. "Preserved verbatim per named
        # pair" is impossible for a message built from the constants: it would be both unchanged and
        # wrong about a different region (TOOL-aRuledFrontispiece-1 S3a).
        raise Problem(f"{readme}: no '{mark_open}' / '{mark_close}' marker pair — the generated "
                      f"region has nowhere to go, and a README without one leaves the index silently")
    if len(opens) != 1 or len(closes) != 1:
        raise Problem(f"{readme}: expected exactly one '{mark_open}' marker pair, found "
                      f"{len(opens)} open and {len(closes)} close")
    if closes[0] < opens[0]:
        raise Problem(f"{readme}: the '{mark_close}' marker precedes its opening one")
    return "\n".join(lines[: opens[0]] + region.split("\n") + lines[closes[0] + 1 :])


def render_live(builds: list, m: str) -> str:
    live = [b for b in builds if b["status"] not in TERMINAL]
    out = [
        GEN_HEADER,
        f"# {m}/LIVE.md — builds with at least one non-terminal unit",
        "",
        "Derived, never authored: a build leaves this file when every one of its units reaches a",
        "terminal status. Nothing here is edited by hand.",
        "",
    ]
    if live:
        # A COUNT, not the list. This file is in check 7's entry-budget population and the build
        # README's region is not, so the full roster renders there and a bounded number renders here:
        # a ten-id row measured 316 chars against a 300-char cap, on a file with no slack.
        out += ["| Build | Status | Node | Opened | Streams | Ids (n) |", "|---|---|---|---|---|---|"]
        for b in live:
            fm = b["fm"]
            out.append(
                f"| [{b['slug']}](builds/{b['slug']}/README.md) | {b['status']} | {fm['node']} | "
                f"{fm['opened']} | {fm['streams']} | {len(b['roster'])} |"
            )
    else:
        out.append("*No live build.*")
    return "\n".join(out) + "\n"


def render_shards(builds: list, m: str) -> dict:
    months: dict = {}
    for b in builds:
        months.setdefault(b["fm"]["opened"][:7], []).append(b)
    out = {}
    for month, rows in months.items():
        body = [
            GEN_HEADER,
            f"# {m}/ledger/{month}.md — builds opened in {month}",
            "",
            "Frozen once the month passes: its inputs stop changing, so no rotation rule is needed.",
            "",
            "| Build | Status | Node | Streams | Ids (n) |",
            "|---|---|---|---|---|",
        ]
        for b in sorted(rows, key=lambda x: x["slug"]):
            fm = b["fm"]
            body.append(
                f"| [{b['slug']}](../builds/{b['slug']}/README.md) | {b['status']} | {fm['node']} | "
                f"{fm['streams']} | {len(b['roster'])} |"
            )
        out[f"{m}/ledger/{month}.md"] = "\n".join(body) + "\n"
    return out


def check_marker_line(line: str, mark: str) -> bool:
    """The ONE spelling of "is this line exactly this marker", CR-stripped.

    R2-L2 (closing review round 2). This predicate had FOUR live spellings in this file — two nested
    `_is` helpers, `_marker_index`'s inline compare, and `slot_violations`' own — inside a module
    whose comments forbid two answers to one question. They agreed, which is why nothing caught it;
    the cost of four copies is that the NEXT edit makes them disagree, and this build already spent
    two rounds on exactly that between this file and the driver.
    """
    return (line[:-1] if line.endswith(CR) else line) == mark


def _marker_index(lines: list, mark: str):
    """The index of a marker line, or None. Same COLUMN-0, one-trailing-CR contract as apply_region."""
    for i, l in enumerate(lines):
        if check_marker_line(l, mark):
            return i
    return None


SLOT_LIMITS = "build-readme-slot-limits.txt"
SLOT_HIGHWATER = "build-readme-slot-highwater.txt"

# TOOL-dFramedEntrypoint, round-3 HIGH. Every reader of the two files above resolved them from
# `__file__`, so nothing could point them at a fixture — and that is exactly why the arms covering
# `cmd_bump` twice ended up RESTATING its filter inline instead of calling it: the verb writes into
# the installed kit directory, so an arm that called it would have rewritten this repo's own
# high-water file. One seam fixes the class. Production resolves from `__file__` as before; the
# selftest sets the override, calls the real verb, and asserts on real bytes.
_SLOT_DATA_DIR = None


def resolve_slot_data_dir():
    """Where the two slot declaration files live. Overridable ONLY so an arm can call the verbs."""
    return pathlib.Path(_SLOT_DATA_DIR) if _SLOT_DATA_DIR \
        else pathlib.Path(__file__).resolve().parent


def read_slot_table(path: str) -> dict:
    """`heading -> int | None` from a tab-separated declaration file. None is the UNARMED state.

    A COMMENT IS A LINE WITH NO TAB, never a line starting with `#`. Every canonical slot heading
    starts with `#`, so the obvious comment predicate ate every data row: the table parsed to empty
    and the leg reported five slots UNARMED, which reads exactly like a deliberate configuration.
    Found by running the verb, and it is the reason `check_slot_table` below exists — a data file
    that parses to nothing must be a refusal, not a plausible state.
    """
    out = {}
    for raw in read_text(path).split("\n"):
        if not raw.strip() or "\t" not in raw:
            continue
        head, _tab, val = raw.partition("\t")
        head, val = head.strip(), val.strip()
        if not head:
            continue
        out[head] = int(val) if val.isdigit() else None
    return out


def check_slot_table(limits: dict, where: str) -> None:
    """Both directions over the declared ceilings. Runs whether or not any README is BOUND.

    An earlier cut checked this only while grading a bound file, so with an empty population a
    completely unparsed limits file reported as deliberate UNARMED slots. A declaration's integrity
    cannot depend on whether anything happens to be using it.
    """
    canon = [h for h, _e, _b in SLOT_CANON]
    for h in canon:
        if h not in limits:
            raise Problem(f"{where} has NO ROW for the canonical slot `{h}`; a slot nobody priced is "
                          f"a slot nobody decided about, which is not the same as one deliberately "
                          f"left unarmed")
    for h in limits:
        if h not in canon:
            raise Problem(f"{where} carries a row for `{h}`, which SLOT_CANON does not declare — a "
                          f"ceiling outliving its slot silently widens what it was written to bound")


def measure_slot_sizes(readme_text: str) -> list:
    """`[(heading, bytes)]` over the AUTHORED slice of each canonical slot, in canon order.

    A slot runs from its heading line to the line before the next canonical heading; the LAST slot
    stops at the authored roster pair where one is present and at the first generated marker
    otherwise. Stopping unconditionally at the generated marker would bill the roster table to the
    parked-decisions slot, which unit 1's non-goals forbid touching.

    BYTES, not characters — and the reason is not the one an earlier draft gave. The hygiene entry cap
    is DECLARED in characters; what its own comment refuses to pin is awk's `length()`, which counts
    bytes or characters depending on the build and the locale. This check is Python, where the choice
    is explicit, and it picks bytes so the verdict is node-independent by construction.
    """
    lines = readme_text.split("\n")
    stop = len(lines)
    for _n, mo, _mc in GEN_REGIONS:
        i = _marker_index(lines, mo)
        if i is not None:
            stop = min(stop, i)
    po = _marker_index(lines, PLAN_OPEN)
    if po is not None and po < stop:
        stop = po
    heads = {h: None for h, _e, _b in SLOT_CANON}
    idx = []
    for i in range(0, stop):
        if lines[i] in heads:
            idx.append((i, lines[i]))
    out = []
    for n, (i, h) in enumerate(idx):
        end = idx[n + 1][0] if n + 1 < len(idx) else stop
        out.append((h, len("\n".join(lines[i + 1:end]).strip().encode("utf-8"))))
    return out


def scan_slot_budget(root: str, conf: dict, rel: str) -> tuple:
    """`(hard, advisory)` for one build README. Hard fails the bar; advisory never does."""
    here = resolve_slot_data_dir()
    limits_p, hw_p = str(here / SLOT_LIMITS), str(here / SLOT_HIGHWATER)
    if not os.path.exists(limits_p):
        raise Problem(f"{SLOT_LIMITS} is absent at {limits_p}; a slot budget with no declared "
                      f"ceilings would grade nothing and report clean")
    limits = read_slot_table(limits_p)
    highs = read_slot_table(hw_p) if os.path.exists(hw_p) else {}
    check_slot_table(limits, SLOT_LIMITS)
    hard, adv = [], []
    for head, size in measure_slot_sizes(read_text(os.path.join(root, rel))):
        cap, hw = limits.get(head), highs.get(head)
        if cap is not None and size > cap:
            hard.append(f"    {rel} — slot `{head}` is {size} B over its declared ceiling of {cap} B")
        elif hw is not None and size > hw:
            adv.append(f"    {rel} — slot `{head}` is {size} B, past its recorded high-water of "
                       f"{hw} B and under its {cap} B ceiling")
    return hard, adv


def scan_unarmed_slots() -> list:
    """Canonical slots whose declared ceiling is blank — the ANNOUNCED unarmed state."""
    here = resolve_slot_data_dir()
    p = str(here / SLOT_LIMITS)
    if not os.path.exists(p):
        return []
    limits = read_slot_table(p)
    return [h for h, _e, _b in SLOT_CANON if limits.get(h) is None]


def read_contract_registry(root: str, conf: dict) -> set:
    """The build READMEs the heading canon BINDS. Bound rows only; see `read_contract_rows` for both.

    TOOL-dFramedEntrypoint-3 REPLACED unit 1's behaviour here: an absent registry was the empty set,
    which is a pass, and is now a refusal. Unit 1 shipped the permissive form deliberately so it did
    not depend on a file unit 3 had not written; this is the handover, and it is stated in both specs
    rather than left as two specs disagreeing.
    """
    bound, _exempt, _pin = read_contract_rows(root, conf)
    return bound


def read_contract_rows(root: str, conf: dict) -> tuple:
    """`(bound, exempt, declared_pin)` from the declared registry. An absent file REFUSES."""
    rel = os.path.join(conf["MEMORY_ROOT"], CONTRACT_REGISTRY).replace(os.sep, "/")
    full = os.path.join(root, conf["MEMORY_ROOT"], CONTRACT_REGISTRY)
    if not os.path.exists(full):
        raise Problem(f"{rel} is absent; the heading canon and the slot budgets would then bind "
                      f"nothing and report clean, which is coverage of nothing")
    bound, exempt, pin = set(), {}, None
    for n, raw in enumerate(read_text(full).split("\n"), 1):
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("exempt-pin:"):
            v = s.split(":", 1)[1].strip()
            if not v.isdigit():
                raise Problem(f"{rel}:{n}: exempt-pin is `{v}`, which is not a count")
            pin = int(v)
            continue
        if s.startswith("!"):
            path, _sep, why = s[1:].partition(" - ")
            path = path.strip()
            if not why.strip():
                raise Problem(f"{rel}:{n}: exempt row `{path}` carries no reason; an exemption whose "
                              f"reason lives elsewhere is one nobody can drain")
            exempt[path] = why.strip()
            continue
        if " " in s:
            raise Problem(f"{rel}:{n}: `{s}` is neither a bare bound path, an `!`-prefixed exempt "
                          f"row with a reason, nor an `exempt-pin:` line")
        bound.add(s)
    if pin is None:
        raise Problem(f"{rel}: no `exempt-pin:` line; the exempt list is shrink-only and a list with "
                      f"no pin cannot report that it stopped shrinking")
    return bound, exempt, pin


def check_contract_registry(root: str, conf: dict, tracked: list) -> None:
    """Both directions, plus the equality pin. Every failure names the row or the path."""
    rel = os.path.join(conf["MEMORY_ROOT"], CONTRACT_REGISTRY).replace(os.sep, "/")
    bound, exempt, pin = read_contract_rows(root, conf)
    named, have = bound | set(exempt), set(tracked)
    # FORWARD — a tracked build README nothing names cannot silently escape the contract.
    for miss in sorted(have - named):
        raise Problem(f"{rel} names neither a bound nor an exempt row for `{miss}`, so a new build "
                      f"would escape the contract by existing")
    # REVERSE — a row naming a path that is not a tracked build README widens what it narrowed.
    for dead in sorted(named - have):
        raise Problem(f"{rel} carries a row for `{dead}`, which is not a tracked build README; a "
                      f"stale row silently widens the surface it was written to narrow")
    # The pin is an EQUALITY in both directions: above the count is permanent slack after a drain.
    if pin != len(exempt):
        raise Problem(f"{rel}: exempt-pin is {pin} and the measured exempt count is {len(exempt)}; "
                      f"the pin is an equality, because a pin left above the count after a drain is "
                      f"slack nothing reports")


def scan_canon(lines: list, first_open: int) -> list:
    """The CLOSED heading canon over the authored half. Trigger 3 (TOOL-dFramedEntrypoint-1 S1).

    The authored half runs from the title to whichever comes first: the authored plan pair's opening
    marker, or the first generated marker. The plan pair belongs to NO slot — terminating at the
    generated marker instead would bill its table to the last slot, which unit 2's budget then
    charges to a block this unit's own non-goals forbid touching.
    """
    stop = first_open
    po = _marker_index(lines, PLAN_OPEN)
    if po is not None and po < stop:
        stop = po
    title = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if title is None:
        return [(1, "no `# ` title line, so the authored half has no start")]
    out, seen = [], []
    for i in range(title + 1, stop):
        l = lines[i]
        if l.startswith("## "):
            seen.append((i, l.rstrip()))
        elif l.strip() and not seen:
            out.append((i + 1, "authored content between the title and the first canonical heading"))
    # DUPLICATES FIRST. With a heading repeated, `got` no longer equals `want`, the sequence branch
    # reports a missing/out-of-order slot and RETURNS — so every body check below is skipped and one
    # appended line disabled the whole canon while the leg still printed clean. Refuse the duplicate
    # by name instead of letting it fall through the equality.
    canon_heads = [h for h, _e, _b in SLOT_CANON]
    for i, h in seen:
        # CANONICAL headings only. Scanning every `## ` heading reported a repeated NON-canonical one
        # as a duplicated canonical slot AND suppressed the accurate `heading outside the canon`
        # message through the early return below — two wrong answers out of one over-wide population.
        if h in canon_heads and [x for _j, x in seen].count(h) > 1:
            out.append((i + 1, f"canonical slot heading appears more than once: {h}"))
    if out and any("more than once" in why for _l, why in out):
        return sorted(set(out))
    want = [h for h, _e, _b in SLOT_CANON]
    got = [h for _i, h in seen]
    if got != want:
        for i, h in seen:
            if h not in want:
                out.append((i + 1, f"heading outside the canon: {h}"))
        for n, h in enumerate(want):
            if h not in got:
                out.append((title + 1, f"canonical slot missing: {h}"))
            elif [g for g in got if g in want].index(h) != n:
                out.append((title + 1, f"canonical slot out of order: {h}"))
        return sorted(set(out))
    # Bodies. A slot runs to the next canonical heading, or to `stop` for the last.
    for n, (idx, head) in enumerate(seen):
        end = seen[n + 1][0] if n + 1 < len(seen) else stop
        body = [l for l in lines[idx + 1:end] if l.strip()]
        _h, empty_ok, bullets = SLOT_CANON[n]
        if not body and not empty_ok:
            out.append((idx + 1, f"canonical slot has an empty body and may not: {head}"))
        if bullets:
            for j in range(idx + 1, end):
                s = lines[j].strip()
                if s and not s.startswith(("- ", "* ")) and not lines[j].startswith("  "):
                    out.append((j + 1, f"slot requires a bullet list: {head}"))
    return sorted(set(out))


def slot_violations(readme_text: str, readme: str, canon: bool = False) -> list:
    """Authored content sitting where the slot contract forbids it (TOOL-aRuledFrontispiece-1 S4).

    THREE triggers since TOOL-dFramedEntrypoint-1, and the third is OPT-IN per file: the canon binds
    only the READMEs the declared registry names, so a caller grading an unbound file passes
    `canon=False` and gets the two position triggers alone.

    **WHAT THIS DOES NOT CHECK.** It grades SHAPE — heading text, heading order, body emptiness, and
    whether a body that must be a list is one. It never grades whether a slot says anything true,
    whether the description is the one first authored, or whether the improvements are improvements.
    The immutability of the description is a DOCUMENTED check in `memory/HYGIENE.md` and deliberately
    not a gated one: 26 of 61 description blocks already carry more than one commit, so a
    history-based predicate has no green starting state. Nor does it grade SIZE — that is
    TOOL-dFramedEntrypoint-2's declared per-slot budget, kept separate so a shape failure and a size
    failure are distinguishable to whoever reads the red.
    """
    lines = readme_text.split("\n")
    spans = []            # (open_index, close_index) of every registered generated region present
    for _name, mo, mc in GEN_REGIONS:
        o, c = _marker_index(lines, mo), _marker_index(lines, mc)
        if o is not None and c is not None and c > o:
            spans.append((o, c))
    if not spans:
        # TOOL-dFramedEntrypoint-1 S4 — the TOTAL-EXEMPTION hole. This returned [] unconditionally,
        # so a README carrying no generated pair passed every trigger however much prose it held:
        # measured on a 45,185-byte fixture with two invented sections, which reported clean. No file
        # in the live corpus reaches it today, which is exactly why it went unnoticed.
        return [(1, "no generated region pair, so every slot trigger would pass vacuously — "
                    "run --write to create the pairs")]
    first_open = min(o for o, _c in spans)
    inside = {i for o, c in spans for i in range(o, c + 1)}
    out = []
    # Trigger 1 — authored prose AFTER the first generated marker, outside every generated region.
    for i, l in enumerate(lines):
        if i > first_open and i not in inside and l.strip():
            out.append((i + 1, "authored content after the first generated marker"))
    # Trigger 2 — authored prose BETWEEN the plan pair's close and the first generated open.
    pc = _marker_index(lines, PLAN_CLOSE)
    if pc is not None and pc < first_open:
        for i in range(pc + 1, first_open):
            if lines[i].strip():
                out.append((i + 1, "authored content between the plan pair and the generated region"))
    # Trigger 4 — the authored roster pair is MANDATORY, on EVERY tracked build README.
    # TOOL-dHonouredPark-1. It is not gated on `canon`: the contract registry declares which READMEs
    # the heading canon and the SLOT BUDGETS bind, and a roster is neither. The owner ruled this
    # population on 2026-08-25, and the reason it is the whole tracked set is that `build-complete`
    # term 3 reads the pair on every build — so binding a subset would leave a later deletion
    # silently restoring the vacuous pass it exists to remove.
    #
    # THE DISCIPLINE IS THE DRIVER'S, not `_marker_index`'s. `region()` in
    # tools/unattended/unattended.sh refuses unless there is exactly one open, exactly one close, and
    # the open comes first; `_marker_index` returns the FIRST match and has no notion of duplicates or
    # order. An assertion built on the helper would accept what the driver rejects, which is two
    # answers to one question in the two tools that both read this marker.
    #
    # The vocabulary is the driver's too — absent, duplicated, transposed — because it already spells
    # those three words for the sibling region, forty lines from where this is read.
    # H4 (closing review) — MATCH THE DRIVER BYTE FOR BYTE. `region()` compares at column 0 with a
    # trailing CR stripped and nothing else, so `l.strip()` here made this gate CERTIFY an indented
    # or trailing-space pair that the driver then refuses. That is the exact two-answers-to-one-
    # question defect S4 was written to prevent, reintroduced by the implementation of S4.
    # R2-M2 — THE NEAR-MISS SET IS COMPUTED FIRST and reported on its own. A marker indented by two
    # spaces is not an ABSENT marker and it is certainly not a DUPLICATED one, and the count branch
    # said both: it saw zero of that marker and then blamed whichever count was not one. A reader
    # sent to find a duplicate that does not exist reads the file twice and trusts the gate less.
    near = []
    for i, l in enumerate(lines):
        s = l[:-1] if l.endswith("\r") else l
        st = s.strip()
        for m in (PLAN_OPEN, PLAN_CLOSE):
            if s != m and (st == m or s.startswith(m) or st.startswith(m)):
                near.append((i + 1, "a roster marker line is not the marker alone — the driver "
                                    "compares at column 0 with nothing before or after it: %r" % s[:60]))
    # R3-M1 — ACCUMULATE, never return. The first cut returned here, and a canon-bound README with a
    # perturbed marker lost all six of its canon findings — a trigger suppressing another inside a
    # function whose whole contract is that its findings are a union.
    out += near
    n_open = sum(1 for l in lines if check_marker_line(l, PLAN_OPEN))
    n_close = sum(1 for l in lines if check_marker_line(l, PLAN_CLOSE))
    if near:
        pass  # a perturbed marker is already named above; do not also diagnose it as absent
    elif n_open == 0 and n_close == 0:
        out.append((1, "no authored %s pair, which every build README must carry" % PLAN_OPEN))
    elif n_open != 1 or n_close != 1:
        out.append((1, "the authored roster pair is not exactly one open and one close marker — "
                       "found %d open and %d close" % (n_open, n_close)))
    else:
        oi = next(i for i, l in enumerate(lines) if check_marker_line(l, PLAN_OPEN))
        ci = next(i for i, l in enumerate(lines) if check_marker_line(l, PLAN_CLOSE))
        if ci < oi:
            out.append((ci + 1, "the authored roster pair is TRANSPOSED — the close marker precedes "
                                "the open one"))
    # Trigger 3 — the closed heading canon, only over a file the registry BINDS.
    if canon:
        out += scan_canon(lines, first_open)
    return sorted(set(out))


def insert_region(readme_text: str, mark_open: str, mark_close: str) -> str:
    """Create a missing pair at its CANONICAL slot, moving no authored byte (S1b, S8).

    Canonical means the order GEN_REGIONS declares, so the position is a property of that list and
    not of whoever edited the file last. Over a README that violates the slot sequence there is no
    well-defined 'after the prose' point, which is why this anchors on sibling REGIONS only — that is
    the branch every corpus write takes until the surgery unit lands.
    """
    lines = readme_text.split("\n")
    names = [mo for _n, mo, _mc in GEN_REGIONS]
    here = names.index(mark_open)
    for mo, mc in ((GEN_REGIONS[j][1], GEN_REGIONS[j][2]) for j in range(here - 1, -1, -1)):
        c = _marker_index(lines, mc)
        if c is not None:
            return "\n".join(lines[: c + 1] + ["", mark_open, mark_close] + lines[c + 1 :])
    for j in range(here + 1, len(GEN_REGIONS)):
        o = _marker_index(lines, GEN_REGIONS[j][1])
        if o is not None:
            return "\n".join(lines[:o] + [mark_open, mark_close, ""] + lines[o:])
    tail = lines if lines and lines[-1].strip() else lines[:-1] if lines else []
    return "\n".join(tail + ["", mark_open, mark_close, ""])


def render_spec_records(spec_id: str, recs: list, spec_rel: str) -> str:
    """The records naming `spec_id`, rendered for that spec. The empty case is EXPLICIT, never absent.

    An absent region cannot be told from a spec nobody has recorded against, which is the
    absence-reads-as-coverage class. The population is every tracked spec carrying a status header —
    NOT only the ones a record names, which is the narrowing that made this unit's first draft
    declare two opposite populations for one region.
    """
    out = [SPEC_RECORDS_OPEN, ""]
    if not recs:
        out.append("*No record names this unit.*")
    else:
        out += ["| Record | Kind | Also serves |", "|---|---|---|"]
        for r in sorted(recs, key=lambda x: x["path"]):
            # RELATIVE TO THE SPEC'S OWN DIRECTORY, computed rather than assembled. The first cut
            # special-cased the same-build case and fell back to the repo-relative path for a
            # cross-build record — which a markdown reader resolves against the SPEC's directory, so
            # every one of the 17 cross-build edges rendered a link to nothing. Hygiene check 2 caught
            # it; `os.path.relpath` is what should have been there from the start.
            rel = os.path.relpath(r["path"], spec_rel.rsplit("/", 1)[0]).replace(os.sep, "/")
            label = r["path"].rsplit("/", 1)[-1]
            others = [i for i in r.get("ids", []) if i != spec_id]
            out.append(f"| [{label}]({rel}) | {r.get('kind') or '—'} | "
                       f"{' '.join(others) if others else '—'} |")
    out += ["", SPEC_RECORDS_CLOSE]
    return "\n".join(out)


def build_spec_record_index(builds: list) -> dict:
    """`spec id -> [record]`, inverted from the bindings every build already carries.

    A record filed under one build folder may name a spec in ANOTHER; keying on the id rather than on
    the folder is what puts a cross-build review at the spec a reader is actually looking at.
    """
    out = {}
    for b in builds:
        for r in b.get("records") or []:
            for i in r.get("ids", []):
                out.setdefault(i, []).append(r)
    return out


def add_spec_records_region(spec_text: str) -> str:
    """Create the pair between the status header and the first `## ` section. Nothing else moves."""
    lines = spec_text.split("\n")
    at = next((i for i, l in enumerate(lines) if l.startswith("## ")), None)
    if at is None:
        at = len(lines)
    while at > 0 and not lines[at - 1].strip():
        at -= 1
    return "\n".join(lines[:at] + ["", SPEC_RECORDS_OPEN, SPEC_RECORDS_CLOSE] + lines[at:])


def remove_dead_regions(readme_text: str) -> str:
    """Delete a RETIRED region's marker pair and everything between it, leaving no authored byte.

    A region whose registration is gone but whose pair remains is not inert: `slot_violations` counts
    the orphaned markers and their content as authored material after the first generated marker,
    which is trigger 1. Measured at 750 violation lines across the corpus if the surgery is split
    from the tuple change, which is why they are one commit.
    """
    for _name, mo, mc in DEAD_REGIONS:
        lines = readme_text.split("\n")
        o, c = _marker_index(lines, mo), _marker_index(lines, mc)
        if o is None or c is None or c < o:
            continue
        end = c + 1
        while end < len(lines) and not lines[end].strip():
            end += 1
        start = o
        while start > 0 and not lines[start - 1].strip():
            start -= 1
        readme_text = "\n".join(lines[:start] + lines[end:])
    return readme_text


def plan(root: str, conf: dict, create_missing: bool = False) -> tuple:
    """Return (artifacts, orphans, unmanaged) — the whole render, computed without touching disk.

    `create_missing` is the ONE asymmetry between the two verbs (S7). `--write` passes true and adds
    a registered region a README lacks; `--check` passes false and stays silent about it. Both verbs
    call this function, so without the flag a create-if-missing step would fire under `--check` and
    report every un-paired README stale — which would force a corpus-wide re-render into the commit
    of every unit that registers a region, and is the outcome S1c exists to forbid.
    """
    m = conf["MEMORY_ROOT"]
    builds = collect(root, conf)
    # DERIVE the child set by inverting `parents:`. Authoring both directions would put two answers
    # to one question in two files with no gate on this bar able to reconcile them — the defect
    # TOOL-aMouldedFolio-1 recorded one relation over, when it refused a front-matter schema.
    known = {b["slug"] for b in builds}
    children = {}
    for b in builds:
        for p in b["parents"]:
            if p not in known:
                raise Problem(f"{b['readme']}: parents: names '{p}', which is not a build folder "
                              f"under {m}/builds/ — an edge to nothing is a typo, not a relation")
            children.setdefault(p, []).append(b["slug"])
    for b in builds:
        b["children"] = sorted(children.get(b["slug"], []))
    # The bindings, read ONCE for the whole render and attached per build. Each record is filed under
    # the build folder that HOUSES it, which is not always the build its ids belong to — a
    # cross-build record renders where a reader will look for it.
    try:
        tracked_all = [p for p in run("git", "ls-files", cwd=root).split("\n") if p]
        binds_all = read_bindings(root, tracked_all, conf)
    except Problem as exc:
        # NARROWED from `except Exception` (TOOL-dScrubbedConduit-1 S1). The render must not depend on
        # the parse succeeding, but swallowing EVERY exception meant read_bindings could die of a
        # decode error and the only visible symptom was a silently empty record table on every build
        # README. A Problem is the parse declining; anything else is this tool being broken, and a
        # broken tool must not render a plausible-looking artifact over the top of it.
        print(f"build-index: record scan declined ({exc}); READMEs render without record tables",
              file=sys.stderr)
        binds_all = {}
    for b in builds:
        pre = f"{m}/builds/{b['slug']}/"
        b["records"] = [dict(rec, path=p) for p, rec in binds_all.items()
                        if p.startswith(pre) and rec["state"] in ("bound", "unbound")]
    artifacts = {}
    for b in builds:
        path = os.path.join(root, b["readme"])
        text = remove_dead_regions(read_text(path))
        text = apply_front_matter_ids(text, b["roster"], b["readme"])
        if create_missing:
            for _name, mo, mc in GEN_REGIONS:
                lines = text.split("\n")
                if _marker_index(lines, mo) is None and _marker_index(lines, mc) is None:
                    text = insert_region(text, mo, mc)
        for name, mo, mc in GEN_REGIONS:
            renderer = REGION_RENDERERS[name]
            lines = text.split("\n")
            # S1c's tolerance is for a NEW region a README has not adopted yet. It must NOT extend to
            # `build-index`, whose pair has always been mandatory: apply_region's "leaves the index
            # silently" refusal is the only thing standing between a build README and a hand-authored
            # status block. Measured with a live control — with the skip applied uniformly, deleting
            # four marker lines from a build README left --check, --check-format and the whole hygiene
            # gate green, while the pre-change engine refused the identical tree. The build's own
            # premise is that this file is generated and gated; a skip that covers the index region
            # defeats it in four lines.
            if name != GEN_REGIONS[0][0] and _marker_index(lines, mo) is None \
                    and _marker_index(lines, mc) is None:
                continue  # a region this README has not adopted — S1c
            text = apply_region(text, renderer(b), b["readme"], mo, mc)
        artifacts[b["readme"]] = text
    # TOOL-dFramedEntrypoint-6 — every record renders inside the SPEC it serves. The population is
    # every tracked spec carrying a status header, not only the ones a record names: an unnamed spec
    # renders an EXPLICIT empty case, because an absent region cannot be told from a spec nobody has
    # recorded against. `--write` creates the pair, `--check` never demands one — the same asymmetry
    # the build-README regions rely on, so this ships without demanding a corpus-wide render.
    inverted = build_spec_record_index(builds)
    for b in builds:
        base = b["readme"].rsplit("/", 1)[0]
        for u in b["units"]:
            # `u["path"]` is ABSOLUTE and mixed-separator on Windows. Every other artifact key here
            # is repo-relative, and `cmd_write` joins the key onto `root` — so an absolute key wrote
            # the right file by luck and computed the wrong relative link. Re-derive it the way
            # `render_region` already does, from the build root plus the tail.
            marker = "/builds/" + b["slug"] + "/"
            tail = u["path"].replace(os.sep, "/").split(marker, 1)[1]
            rel = base + "/" + tail
            stext = read_text(os.path.join(root, rel))
            lines = stext.split("\n")
            has = _marker_index(lines, SPEC_RECORDS_OPEN) is not None
            if not has and not create_missing:
                continue
            if not has:
                stext = add_spec_records_region(stext)
            artifacts[rel] = apply_region(
                stext, render_spec_records(u["id"], inverted.get(u["id"], []), rel), rel,
                SPEC_RECORDS_OPEN, SPEC_RECORDS_CLOSE)
    artifacts[f"{m}/LIVE.md"] = render_live(builds, m)
    artifacts.update(render_shards(builds, m))
    # Orphans: a tracked file under ledger/ that this render does not produce. The DELETABLE set is
    # bounded to the month-shard NAME; anything else is reported and left alone.
    tracked = [p for p in run("git", "ls-files", "--", f"{m}/ledger/", cwd=root).split("\n") if p]
    orphans, unmanaged = [], []
    for p in tracked:
        if p in artifacts:
            continue
        (orphans if SHARD_RE.match(os.path.basename(p)) and p.count("/") == 2 else unmanaged).append(p)
    return artifacts, sorted(orphans), sorted(unmanaged)


# -------------------------------------------------------------------------------------------- modes
def cmd_check(root: str, conf: dict) -> int:
    artifacts, orphans, unmanaged = plan(root, conf)
    bad = []
    for rel, want in sorted(artifacts.items()):
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            bad.append(f"{rel} (missing — never rendered)")
        elif read_text(path) != want:
            bad.append(f"{rel} (stale — differs from a fresh render)")
    for p in orphans:
        bad.append(f"{p} (orphaned ledger shard — no build opened in that month; --write deletes it)")
    for p in unmanaged:
        bad.append(f"{p} (unmanaged file under ledger/ — not a month shard; --write LEAVES IT ALONE)")
    if bad:
        print(f"build-index DRIFT — run: python {kit_rel()}/gen_build_index.py --write")
        for line in bad:
            print("    " + line)
        return 1
    print(f"build-index: clean ({len(artifacts)} artifact(s))")
    return 0


def cmd_check_format(root: str, conf: dict) -> int:
    """The SLOT CONTRACT verb — deliberately NOT reachable from plan(), --write or --check (S1a).

    Build READMEs violate the sequence at this unit's base, so a refusal on the render path would red
    hygiene check 9 across the corpus on this unit's own commit. The leg at the last build position
    is what makes this binding; the surgery unit before it is what makes it pass.

    **WHAT THIS VERB DOES NOT CHECK**, stated here because a structural check reads as a semantic one
    to everybody who did not write it. It grades POSITION for every tracked build README, and SHAPE —
    the closed heading canon — only for the READMEs the declared registry BINDS. It does not grade
    what a slot SAYS, whether the description is the one first authored, or how big any slot is. Size
    is TOOL-dFramedEntrypoint-2's separate budget; immutability is a documented check in
    `memory/HYGIENE.md` and not a gated one, because 26 of 61 description blocks already carry more
    than one commit and a history predicate would have no green starting state.
    """
    m = conf["MEMORY_ROOT"]
    tracked = [p for p in run("git", "ls-files", "--", f"{m}/builds/", cwd=root).split("\n")
               if p.endswith("/README.md")]
    check_contract_registry(root, conf, tracked)
    bound = read_contract_registry(root, conf)
    # The declaration is asserted on EVERY run, bound population or not. Its integrity is not
    # conditional on anything using it.
    _here = resolve_slot_data_dir()
    if not (_here / SLOT_LIMITS).exists():
        raise Problem(f"{SLOT_LIMITS} is absent at {_here / SLOT_LIMITS}; a slot budget with no "
                      f"declared ceilings would grade nothing and report clean")
    check_slot_table(read_slot_table(str(_here / SLOT_LIMITS)), SLOT_LIMITS)
    bad, adv = [], []
    for rel in sorted(tracked):
        for line, why in slot_violations(read_text(os.path.join(root, rel)), rel, canon=rel in bound):
            bad.append(f"    {rel}:{line} — {why}")
        if rel in bound:
            h, a = scan_slot_budget(root, conf, rel)
            bad += h
            adv += a
    # The advisory prints BEFORE the verdict and never changes it. It also reaches nobody through the
    # runner on a green leg, which is why `--report` exists and why the per-leg log is the other half.
    for line in adv:
        print("build-index ADVISORY — a slot passed its recorded high-water:")
        print(line)
    if bad:
        print("build-index FORMAT — authored content outside the slot contract:")
        for line in bad:
            print(line)
        return 1
    graded = len([r for r in tracked if r in bound])
    unarmed = scan_unarmed_slots()
    if unarmed:
        print(f"build-index: NOTE {len(unarmed)} canonical slot(s) ship UNARMED — no declared "
              f"ceiling: {', '.join(unarmed)}")
    print(f"build-index: slot contract clean ({len(tracked)} build README(s); "
          f"heading canon BOUND on {graded})")
    if not graded:
        # A rule binding nothing must SAY so. A green line over an empty declared population is
        # indistinguishable from coverage, which is the class the charter names and the reason a
        # date-keyed cutoff was refused for this contract in the first place.
        print(f"build-index: NOTE the heading canon is bound on ZERO build READMEs — "
              f"{m}/{CONTRACT_REGISTRY} declares none, so trigger 3 graded nothing this run")
    return 0


def cmd_report(root: str, conf: dict) -> int:
    """Every bound README's slot sizes against both numbers. The margin, readable BEFORE a breach.

    This exists because the runner prints one ok line for a passing leg and echoes leg stdout only on
    failure, so an advisory inside a green leg reaches nobody. A warning nobody can read is a check
    nobody runs.
    """
    m = conf["MEMORY_ROOT"]
    here = resolve_slot_data_dir()
    limits = read_slot_table(str(here / SLOT_LIMITS)) if (here / SLOT_LIMITS).exists() else {}
    highs = read_slot_table(str(here / SLOT_HIGHWATER)) if (here / SLOT_HIGHWATER).exists() else {}
    bound = sorted(read_contract_registry(root, conf))
    if not bound:
        print(f"build-index: no build README is BOUND — {m}/{CONTRACT_REGISTRY} declares none, so "
              f"there is nothing to report sizes for. The ceilings below are declared and inert.")
        for h, _e, _b in SLOT_CANON:
            c = limits.get(h)
            print(f"    {h} — ceiling {c if c is not None else 'UNARMED'}")
        return 0
    for rel in bound:
        for head, size in measure_slot_sizes(read_text(os.path.join(root, rel))):
            c, hw = limits.get(head), highs.get(head)
            print(f"    {rel} · {head} — {size} B · high-water {hw if hw is not None else '-'} · "
                  f"ceiling {c if c is not None else 'UNARMED'}")
    return 0


def cmd_bump(root: str, conf: dict) -> int:
    """Rewrite the HIGH-WATER file from the measured tree. It never writes the ceiling file."""
    here = resolve_slot_data_dir()
    bound = sorted(read_contract_registry(root, conf))
    peak = {h: 0 for h, _e, _b in SLOT_CANON}
    for rel in bound:
        for head, size in measure_slot_sizes(read_text(os.path.join(root, rel))):
            peak[head] = max(peak.get(head, 0), size)
    p = str(here / SLOT_HIGHWATER)
    # A COMMENT IS A LINE WITH NO TAB — the same rule `read_slot_table` states, for the same reason,
    # and getting it wrong here duplicated all five rows on every run: 5 -> 10 -> 15. The two
    # functions parse ONE grammar, so they must agree about it; that agreement is now armed.
    keep = [l for l in read_text(p).split("\n") if "\t" not in l] if os.path.exists(p) else []
    while keep and not keep[-1].strip():
        keep.pop()
    rows = [f"{h}\t{peak[h]}" for h, _e, _b in SLOT_CANON]
    write_text(p, "\n".join(keep + rows) + "\n")
    print(f"build-index: high-water rewritten for {len(rows)} slot(s) over {len(bound)} bound "
          f"README(s); {SLOT_LIMITS} untouched")
    return 0


def cmd_survey(root: str, conf: dict) -> int:
    """Run the canon over EVERY tracked build README, bound or not, and report. Never fails.

    This repo requires a new gate predicate to be run over the real tree before it is wired, printing
    hits AND near-misses. It is a verb rather than a flag because `main()` ignores an unrecognised
    argument, so an acceptance criterion naming a flag that does not exist would pass by printing the
    ordinary clean line — which is precisely what this unit's first draft specified.
    """
    m = conf["MEMORY_ROOT"]
    tracked = sorted(p for p in run("git", "ls-files", "--", f"{m}/builds/", cwd=root).split("\n")
                     if p.endswith("/README.md"))
    bound = read_contract_registry(root, conf)
    hits = 0
    for rel in tracked:
        vs = slot_violations(read_text(os.path.join(root, rel)), rel, canon=True)
        tag = "BOUND  " if rel in bound else "unbound"
        if vs:
            hits += 1
            print(f"{tag} {rel} — {len(vs)} violation(s)")
            for line, why in vs:
                print(f"        :{line} — {why}")
        else:
            print(f"{tag} {rel} — conforms")
    print(f"build-index: survey over {len(tracked)} build README(s) — {hits} would fail the canon, "
          f"{len(tracked) - hits} conform; {len(bound)} are BOUND today")
    return 0


def cmd_write(root: str, conf: dict) -> int:
    artifacts, orphans, unmanaged = plan(root, conf, create_missing=True)
    for rel, text in sorted(artifacts.items()):
        write_text(os.path.join(root, rel), text)
    for p in orphans:
        os.remove(os.path.join(root, p))
        print(f"build-index: removed orphaned shard {p}")
    for p in unmanaged:
        print(f"build-index: WARNING unmanaged file under ledger/ left in place: {p}")
    print(f"build-index: wrote {len(artifacts)} artifact(s)")
    return 0


# ----------------------------------------------------------------------------------------- selftest
def _fixture(tmp: str, *, marker=True, readme=True, status_key=None, spec_status="INPROGRESS"):
    run("git", "init", "-q", ".", cwd=tmp)
    run("git", "config", "user.email", "t@t.test", cwd=tmp)
    run("git", "config", "user.name", "t", cwd=tmp)
    write_text(os.path.join(tmp, ".memory-tree.conf"),
               'MEMORY_ROOT=memory\nDISCIPLINES="arch"\nFAMILIES="arch:ARCH"\n')
    # The stale-header waiver registry, EMPTY, because `collect()` refuses without it
    # (TOOL-dRetiredFork-3, AC4) and every fixture below goes through `collect()`. Written here
    # rather than in fifteen fixtures: this helper is the one place they all pass through, and a
    # per-fixture copy is fifteen chances for one of them to drift out of the population.
    write_text(os.path.join(tmp, "memory", STALE_HEADER_WAIVER),
               "# empty: the mechanism is inert until a header corrupts\n")
    d = os.path.join(tmp, "memory", "builds", "tOne", "spec")
    os.makedirs(d, exist_ok=True)
    if spec_status:
        write_text(os.path.join(d, "2026-08-01-spec-tOne-1.md"),
                   "# ARCH-tOne-1 — a unit\n\n**Status:** " + spec_status +
                   " · rev-1 · 2026-08-01 · node a · Tier-2 · base 0123abcd\n")
    else:
        write_text(os.path.join(d, "legacy-note.md"), "# no header here\n")
    if readme:
        fm = ["---", "slug: tOne", "node: a", "opened: 2026-08-01", "streams: arch",
              "roster: ARCH", "ids: ARCH-tOne-1"]
        if status_key:
            fm.append(f"status: {status_key}")
        fm.append("---")
        body = ["", "# tOne", ""]
        if marker:
            body += [MARK_OPEN, MARK_CLOSE]
        else:
            body += [MARK_OPEN]
        write_text(os.path.join(tmp, "memory", "builds", "tOne", "README.md"), "\n".join(fm + body) + "\n")
    run("git", "add", "-A", cwd=tmp)
    run("git", "commit", "-q", "-m", "f", "--no-verify", cwd=tmp)
    return load_conf(tmp)


def cmd_selftest() -> int:
    fails = []

    def arm(label, want, fn):
        try:
            got = fn()
        except Problem as exc:
            got = str(exc)
        except Exception as exc:  # noqa: BLE001 — a traceback here IS the finding
            got = f"UNEXPECTED {type(exc).__name__}: {exc}"
        if want in str(got):
            print(f"arm ok    {label}")
        else:
            fails.append(label)
            print(f"arm FAIL  {label} — expected to see: {want}\n      got: {got}")

    # `_render_id_ranges` — the bindings row's cap remedy (TOOL-dUnstalledConvoy-13). The COLLAPSING arm
    # alone is the fixture-passes-by-finding-nothing shape: a stub returning its input joined would
    # fail it, but so would a greedy version that swallows a gap, and only the second arm can tell
    # those apart. The third holds the boundary at two, where a range is not shorter than the pair.
    arm("a contiguous run collapses to a range", "TOOL-dX-2..4",
        lambda: _render_id_ranges(["TOOL-dX-2", "TOOL-dX-3", "TOOL-dX-4"]))
    arm("a GAP is never swallowed by the range", "TOOL-dX-2..3 TOOL-dX-7",
        lambda: _render_id_ranges(["TOOL-dX-2", "TOOL-dX-3", "TOOL-dX-7"]))
    arm("a differing slug does not join a run", "TOOL-dX-2 TOOL-dY-3",
        lambda: _render_id_ranges(["TOOL-dX-2", "TOOL-dY-3"]))
    arm("a non-numeric tail is emitted verbatim", "TOOL-dX-head",
        lambda: _render_id_ranges(["TOOL-dX-head"]))

    # `_render_wrapped_ids` — the gap lines' cap remedy. The arm asserts the WRAP, not the content: a
    # version that never wraps returns one line and fails on the count, which is the property the
    # 399-character overflow was about.
    arm("a long id list wraps below the cap", "True", lambda: str(
        len(_render_wrapped_ids("Ids no record names:", ["TOOL-dLongSlugHere-%d" % n for n in range(40)])) > 1
        and max(len(x) for x in _render_wrapped_ids(
            "Ids no record names:", ["TOOL-dLongSlugHere-%d" % n for n in range(40)])) <= IDS_WRAP + 1))

    with tempfile.TemporaryDirectory() as base:
        # AC5 — a build leaves LIVE.md when its units go terminal, with nothing edited by hand.
        t = os.path.join(base, "live"); os.makedirs(t)
        conf = _fixture(t, spec_status="INPROGRESS")
        arm("live build appears in LIVE.md", "| [tOne](builds/tOne/README.md) | INPROGRESS",
            lambda: plan(t, conf)[0]["memory/LIVE.md"])
        t2 = os.path.join(base, "closed"); os.makedirs(t2)
        conf2 = _fixture(t2, spec_status="CLOSED")
        arm("terminal build leaves LIVE.md", "*No live build.*",
            lambda: plan(t2, conf2)[0]["memory/LIVE.md"])
        arm("terminal build still appears in its month shard", "| [tOne](../builds/tOne/README.md) | CLOSED",
            lambda: plan(t2, conf2)[0]["memory/ledger/2026-08.md"])

        # AC2 — an unpaired marker is a NAMED error, not a silent departure.
        # TOOL-dFramedEntrypoint-5 S4 class (c) — THE SENTENCE-REMOVAL ARMS ARE RETIRED, all of them,
        # because their subject is. `strip_records_sentence` existed to delete an AUTHORED copy of a
        # sentence this generator also rendered; this unit stops rendering it, so the remover was
        # retired rather than left to delete an author's prose and write nothing back.
        #
        # WHAT THOSE ARMS WERE REALLY WATCHING is kept, not dropped. Two of them asserted the
        # OCCURRENCE COUNT of the derived sentence, and the sentence was the record selector's
        # liveness assertion — nine arms detected a mis-segmented selector by noticing it had gone
        # missing. The replacement is the counted `Records: <n> bound to this build` line and its
        # positive arm above: a build that holds records and reports zero is the same
        # mis-segmentation, said out loud instead of inferred from an absence.

        # AC4 — an absent README is a named error on BOTH modes, never a traceback.
        t4 = os.path.join(base, "noreadme"); os.makedirs(t4)
        conf4 = _fixture(t4, readme=False)
        arm("absent README is named, not a traceback", "no tracked README.md",
            lambda: plan(t4, conf4))

        # AC8 — the status: fallback, both arms.
        t5 = os.path.join(base, "noheader"); os.makedirs(t5)
        conf5 = _fixture(t5, spec_status=None)
        arm("no parseable header and no status: is named", "declare it explicitly with a 'status:'",
            lambda: plan(t5, conf5))
        t6 = os.path.join(base, "declared"); os.makedirs(t6)
        conf6 = _fixture(t6, spec_status=None, status_key="SPECCED")
        arm("declared status is used when nothing is derivable", "| SPECCED |",
            lambda: plan(t6, conf6)[0]["memory/LIVE.md"])
        t7 = os.path.join(base, "conflict"); os.makedirs(t7)
        conf7 = _fixture(t7, spec_status="OPEN", status_key="CLOSED")
        arm("declared status alongside a derivable one is a conflict", "two answers to one",
            lambda: plan(t7, conf7))

        # AC3 — orphan handling, and its BOUND.
        t8 = os.path.join(base, "orphan"); os.makedirs(t8)
        conf8 = _fixture(t8, spec_status="OPEN")
        write_text(os.path.join(t8, "memory", "ledger", "1999-01.md"), "stale\n")
        write_text(os.path.join(t8, "memory", "ledger", "notes.md"), "authored\n")
        run("git", "add", "-A", cwd=t8)
        run("git", "commit", "-q", "-m", "orphans", "--no-verify", cwd=t8)
        arm("an orphaned month shard is reported", "memory/ledger/1999-01.md",
            lambda: str(plan(t8, conf8)[1]))
        arm("a non-shard file under ledger/ is NOT deletable", "memory/ledger/notes.md",
            lambda: str(plan(t8, conf8)[2]))
        cmd_write(t8, conf8)
        arm("--write removed the orphan", "False",
            lambda: str(os.path.exists(os.path.join(t8, "memory", "ledger", "1999-01.md"))))
        arm("--write kept the unmanaged file", "True",
            lambda: str(os.path.exists(os.path.join(t8, "memory", "ledger", "notes.md"))))

        # front matter: line 1 only, keys at column 0.
        t9 = os.path.join(base, "fm"); os.makedirs(t9)
        conf9 = _fixture(t9, spec_status="OPEN")
        rd = os.path.join(t9, "memory", "builds", "tOne", "README.md")
        write_text(rd, "# a heading first\n\n" + read_text(rd))
        arm("front matter must open at line 1", "line 1 must be '---'", lambda: plan(t9, conf9))
        t10 = os.path.join(base, "indent"); os.makedirs(t10)
        conf10 = _fixture(t10, spec_status="OPEN")
        rd10 = os.path.join(t10, "memory", "builds", "tOne", "README.md")
        write_text(rd10, read_text(rd10).replace("node: a", "  node: a"))
        arm("an indented front-matter key is named", "keys live at COLUMN 0", lambda: plan(t10, conf10))

        # --write then --check is a fixed point. Without this a renderer that emits CRLF, or a
        # comparison that normalises differently from the writer, is green on the run that wrote it
        # and red forever after.
        t11 = os.path.join(base, "roundtrip"); os.makedirs(t11)
        conf11 = _fixture(t11, spec_status="OPEN")
        cmd_write(t11, conf11)
        arm("write then check is a fixed point", "0", lambda: str(cmd_check(t11, conf11)))

        # ---- TOOL-aRuledFrontispiece-1: the slot contract, region creation, and the ASYMMETRY.
        # A fixture whose README carries ONLY the build-index pair: the other three are absent.
        t12 = os.path.join(base, "regions"); os.makedirs(t12)
        conf12 = _fixture(t12, spec_status="OPEN")
        rd12 = os.path.join(t12, "memory", "builds", "tOne", "README.md")

        # S1c — the ASYMMETRY. --check must be SILENT about the three absent pairs.
        #
        # ORDER IS THE WHOLE ARM. This ran AFTER cmd_write, which had just created the three pairs, so
        # there was no absent pair left to be silent about and the arm could not fail: mutation-proved
        # by patching cmd_check to pass create_missing=True — the exact regression it claims to catch —
        # and watching the suite still report PASS. It runs BEFORE the write now, on a fixture that
        # genuinely lacks the pairs, and asserts the render directly rather than an exit code.
        # THE ARM MUST RUN THROUGH cmd_check, not through plan(). Two earlier spellings did not, and
        # both were mutation-proved useless: one ran after cmd_write so no pair was absent, and one
        # called plan() directly so patching cmd_check — the site that actually carries the defect —
        # left the suite green. The fixture is rendered FIRST so the build-index region is fresh, then
        # the three other pairs are removed. Now the only thing that can make cmd_check report stale is
        # create_missing leaking into it, which is exactly S1c.
        rd12 = os.path.join(t12, "memory", "builds", "tOne", "README.md")
        cmd_write(t12, conf12)
        # WHOLE regions, markers and body together. Stripping only the marker lines orphans the
        # rendered body as loose authored text, which makes the fixture genuinely non-conforming and
        # reds a later arm for a reason that has nothing to do with what this one tests.
        # ADDRESSED BY NAME, not by tuple index. The index form read `for _i in (3, 2, 1)` and
        # raised IndexError the moment TOOL-dFramedEntrypoint-5 removed the last entry — a break no
        # grep for the marker STRING could have predicted, which is why the spec names this as its
        # own blast-radius class.
        _TRAILING = [r for r in GEN_REGIONS if r[0] != "build-index"]
        _ls = read_text(rd12).split("\n")
        for _n, _mo, _mc in reversed(_TRAILING):
            _o, _c = _marker_index(_ls, _mo), _marker_index(_ls, _mc)
            if _o is not None and _c is not None:
                _ls = _ls[:_o] + _ls[_c + 1:]
        write_text(rd12, "\n".join(_ls))
        arm("check does not CREATE an absent pair", "0", lambda: str(cmd_check(t12, conf12)))
        arm("every trailing pair really is absent for that arm", str(len(GEN_REGIONS) - 1),
            lambda: str(sum(mo not in read_text(rd12) for _n, mo, _mc in _TRAILING)))
        cmd_write(t12, conf12)
        arm("write restores them", "0", lambda: str(
            sum(mo not in read_text(rd12) for _n, mo, _mc in _TRAILING)))
        arm("write CREATED every absent trailing pair", str(len(GEN_REGIONS) - 1),
            lambda: str(sum(mo in read_text(rd12) for _n, mo, _mc in _TRAILING)))
        arm("created pairs land in CANONICAL order", "True", lambda: str(
            all(read_text(rd12).index(_TRAILING[k][1]) < read_text(rd12).index(_TRAILING[k + 1][1])
                for k in range(len(_TRAILING) - 1))))

        # S8 — over a README that VIOLATES the sequence, the pair still lands and no authored byte
        # moves. This is the branch the whole corpus takes until the surgery unit lands, so it is the
        # common case rather than an edge one.
        t13 = os.path.join(base, "violator"); os.makedirs(t13)
        conf13 = _fixture(t13, spec_status="OPEN")
        rd13 = os.path.join(t13, "memory", "builds", "tOne", "README.md")
        write_text(rd13, read_text(rd13) + "\n## Afterword\n\nauthored prose below the region.\n")
        cmd_write(t13, conf13)
        arm("a violating README keeps its authored tail", "authored prose below the region.",
            lambda: read_text(rd13))
        arm("a violating README still gains its pairs", "True",
            lambda: str(all(mo in read_text(rd13) for _n, mo, _mc in _TRAILING)))

        # S4 — BOTH triggers. The second one is the arm an earlier draft of the spec had no rule for,
        # and it is the one the single corpus README carrying a plan pair actually trips.
        arm("slot walk names prose after the first generated marker",
            "authored content after the first generated marker",
            lambda: str(slot_violations(read_text(rd13), "x")))
        t14 = os.path.join(base, "planprose"); os.makedirs(t14)
        conf14 = _fixture(t14, spec_status="OPEN")
        rd14 = os.path.join(t14, "memory", "builds", "tOne", "README.md")
        write_text(rd14, read_text(rd14).replace(
            MARK_OPEN, PLAN_OPEN + "\n| # | unit |\n" + PLAN_CLOSE + "\n\nstray prose.\n\n" + MARK_OPEN))
        arm("slot walk names prose between the plan pair and the region",
            "authored content between the plan pair and the generated region",
            lambda: str(slot_violations(read_text(rd14), "x")))
        # S2 — the generator NEVER writes between the plan markers.
        cmd_write(t14, conf14)
        arm("the authored plan region survives a write verbatim", "| # | unit |",
            lambda: read_text(rd14))

        # A conforming README yields NO violations — the arm that keeps the walk from being vacuous.
        arm("a conforming README trips no trigger", "[]",
            lambda: str(slot_violations(
                read_text(rd12).replace(MARK_OPEN, PLAN_OPEN + "\n| # | Unit |\n" + PLAN_CLOSE
                                        + "\n\n" + MARK_OPEN, 1), "x")))


        # ---------------------------------------------------- TOOL-dFramedEntrypoint-1, trigger 3
        # S4 — the TOTAL-EXEMPTION hole. This is the arm that FAILED before this unit: a README with
        # no generated pair returned [] whatever it held. No live file reaches it, so it needs a
        # fixture or it is never exercised at all.
        arm("a README with no generated pair is a violation, not a pass",
            "no generated region pair",
            lambda: str(slot_violations("---\nslug: x\n---\n\n# x\n\n45 KB of prose.\n", "x")))
        arm("the no-pair violation fires even with canon off", "1",
            lambda: str(len(slot_violations("# x\n\nprose\n", "x", canon=False))))

        def build_canon_readme(slots, plan=True):
            """A build README whose authored half is `slots`, plus a valid generated pair.

            `plan` writes the authored roster pair, which TOOL-dHonouredPark-1 made MANDATORY on
            every tracked build README. It defaults ON because a fixture standing for a conforming
            file has to conform: four arms asserting [] were previously passing on a fixture that
            would red the live leg. Pass plan=False to exercise trigger 4 itself.
            """
            head = ["---", "slug: tOne", "node: t", "opened: 2026-01-01", "streams: s",
                    "roster: ARCH", "ids: ARCH-tOne-1", "---", "", "# tOne", ""]
            tail = ([PLAN_OPEN, "| # | Unit |", PLAN_CLOSE, ""] if plan else [])
            return "\n".join(head + slots + [""] + tail + [MARK_OPEN, MARK_CLOSE, ""])

        GOOD = ["## The problem this build exists to solve", "", "It states the problem.", "",
                "## Expected improvements", "", "- one improvement", "",
                "## Detriments if this is not built", "", "- one detriment", "",
                "## Build-level rules", "",
                "## Parked decisions", ""]
        arm("a canon-conforming README trips trigger 3 not at all", "[]",
            lambda: str(slot_violations(build_canon_readme(GOOD), "x", canon=True)))
        arm("the canon is OPT-IN — an unbound file is graded on position alone", "[]",
            lambda: str(slot_violations(build_canon_readme(
                GOOD + ["", "## Afterword", "", "anything at all"]), "x", canon=False)))
        arm("a heading outside the canon is named", "heading outside the canon: ## Afterword",
            lambda: str(slot_violations(build_canon_readme(
                GOOD + ["", "## Afterword", "", "prose"]), "x", canon=True)))
        arm("canonical slots out of order are named", "out of order",
            lambda: str(slot_violations(build_canon_readme(
                GOOD[4:] + GOOD[:4]), "x", canon=True)))
        arm("prose above the first canonical heading is named",
            "authored content between the title and the first canonical heading",
            lambda: str(slot_violations(build_canon_readme(["stray sentence.", ""] + GOOD),
                                        "x", canon=True)))
        arm("a required slot with an empty body is named",
            "empty body and may not: ## The problem this build exists to solve",
            lambda: str(slot_violations(build_canon_readme(
                ["## The problem this build exists to solve", ""] + GOOD[3:]), "x", canon=True)))
        arm("an OPTIONAL slot with an empty body is legal", "[]",
            lambda: str(slot_violations(build_canon_readme(GOOD), "x", canon=True)))
        # D2 — a DUPLICATED heading made the sequence compare return before any body check ran, so
        # one appended line disabled the entire canon while the leg printed clean.
        # M3's SCOPING, which shipped with no arm: with `h in canon_heads and` deleted, a repeated
        # NON-canonical heading is misreported as a duplicated canonical slot AND the accurate
        # message is suppressed by the early return. This arm reaches that guard; the duplicate arm
        # below does not, because a repeated CANONICAL heading trips both spellings identically.
        arm("a repeated NON-canonical heading says `outside the canon`, not `more than once`",
            "heading outside the canon: ## Notes",
            lambda: str(slot_violations(build_canon_readme(
                GOOD + ["", "## Notes", "", "p", "", "## Notes", "", "q"]), "x", canon=True)))
        arm("...and does NOT claim a canonical slot was duplicated", "False",
            lambda: str("more than once" in str(slot_violations(build_canon_readme(
                GOOD + ["", "## Notes", "", "p", "", "## Notes", "", "q"]), "x", canon=True))))
        arm("a canonical heading repeated is named, not silently disabling the body checks",
            "appears more than once",
            lambda: str(slot_violations(build_canon_readme(GOOD + ["", "## Build-level rules", ""]),
                                        "x", canon=True)))
        # D4 — --bump duplicated all five rows per run because its keep-filter read `## ` as a
        # comment. The two functions parse ONE grammar and must AGREE about it; that is the arm.
        # CALLS `cmd_bump` FOR REAL, twice, and asserts the row count is STABLE. Three rounds of
        # review went by with this uncovered because every earlier attempt RESTATED cmd_bump's filter
        # inline rather than running it — the verb wrote into the installed kit directory, so an arm
        # that called it would have rewritten this repo's own high-water file. `_SLOT_DATA_DIR` is
        # the seam that makes the real call possible; without it the only honest options were a
        # copy (which drifts, and had already drifted) or no arm at all.
        _bt = os.path.join(base, "bumpreal"); os.makedirs(_bt)
        _bconf = _fixture(_bt, spec_status="OPEN")
        _brd = "memory/builds/tOne/README.md"
        write_text(os.path.join(_bt, "memory", CONTRACT_REGISTRY),
                   "exempt-pin: 0\n" + _brd + "\n")
        _bdir = os.path.join(base, "bumpdata"); os.makedirs(_bdir)
        write_text(os.path.join(_bdir, SLOT_LIMITS),
                   "# ceilings\n" + "\n".join(f"{h}\t9999" for h, _e, _b in SLOT_CANON) + "\n")
        write_text(os.path.join(_bdir, SLOT_HIGHWATER), "# high-water, seeded empty\n")

        # ------------------------------------------------- TOOL-dHonouredPark-1, trigger 4
        # THE PAIR IS MANDATORY, on every tracked build README and not on the contract's bound
        # subset. Owner ruling. Each of the three conditions is armed by NAME, because a single
        # "malformed" verdict sends a reader to diff a file against a rule it does not state.
        #
        # The discipline is the DRIVER's: exactly one open, exactly one close, open first. The
        # engine's own `_marker_index` returns the first match and has no notion of duplicates or
        # order, so an assertion built on it would accept what the driver refuses.
        arm("an ABSENT roster pair is named", "must carry",
            lambda: str(slot_violations(build_canon_readme(GOOD, plan=False), "x")))
        # R2-M2: the message no longer says DUPLICATED, because it was said over files where nothing
        # was duplicated — a whitespace-perturbed marker counted as absent and then blamed the count.
        arm("a roster pair that is not exactly one open and one close is named", "found 2 open and 1 close",
            lambda: str(slot_violations(build_canon_readme(GOOD)
                                        .replace(PLAN_OPEN, PLAN_OPEN + "\n" + PLAN_OPEN, 1), "x")))
        # R2-M2 / R2-L1 — a marker perturbed by whitespace is NOT absent and NOT duplicated, and the
        # count branch said both. These two arms are the branch's first failing case: it shipped with
        # no arm at all, so nobody had ever seen it red.
        arm("an INDENTED roster marker is named as not-the-marker-alone", "not the marker alone",
            lambda: str(slot_violations(build_canon_readme(GOOD)
                                        .replace(PLAN_OPEN, "  " + PLAN_OPEN, 1), "x")))
        # R3-M3 — the control probes the phrase the module ACTUALLY emits. It probed "DUPLICATED",
        # which R2-M2 had already retired, so it asserted the absence of a string nothing could
        # produce: a fixture passing by finding nothing, which is on this diff's own checklist.
        arm("...and is NOT also diagnosed by the marker-count branch", "False",
            lambda: str("not exactly one open and one close" in str(
                slot_violations(build_canon_readme(GOOD)
                                .replace(PLAN_OPEN, "  " + PLAN_OPEN, 1), "x"))))
        arm("a marker BOTH indented and trailed is still named", "not the marker alone",
            lambda: str(slot_violations(build_canon_readme(GOOD)
                                        .replace(PLAN_OPEN, "  " + PLAN_OPEN + " ", 1), "x")))
        arm("a perturbed marker does NOT suppress the canon findings", "outside the canon",
            lambda: str(slot_violations(build_canon_readme(
                GOOD + ["", "## Notes", "", "p"]).replace(PLAN_OPEN, "  " + PLAN_OPEN, 1),
                "x", canon=True)))
        arm("a TRAILING-SPACE roster marker is named the same way", "not the marker alone",
            lambda: str(slot_violations(build_canon_readme(GOOD)
                                        .replace(PLAN_OPEN, PLAN_OPEN + " ", 1), "x")))
        arm("a TRANSPOSED roster pair is named", "TRANSPOSED",
            lambda: str(slot_violations("\n".join(
                ["---", "slug: tOne", "---", "", "# tOne", ""] + GOOD
                + ["", PLAN_CLOSE, "| # | Unit |", PLAN_OPEN, "", MARK_OPEN, MARK_CLOSE, ""]), "x")))
        # AND IT IS NOT GATED ON `canon`. The contract registry declares which READMEs the heading
        # canon and the SLOT BUDGETS bind; a roster is neither, and binding trigger 4 to that subset
        # would leave a later deletion silently restoring the vacuous pass on every other build.
        arm("trigger 4 fires with canon OFF, like triggers 1 and 2", "must carry",
            lambda: str(slot_violations(build_canon_readme(GOOD, plan=False), "x", canon=False)))
        arm("a well-formed but EMPTY pair is LEGAL", "[]",
            lambda: str(slot_violations(build_canon_readme(GOOD)
                                        .replace("| # | Unit |", ""), "x")))

        def measure_bump_rows():
            global _SLOT_DATA_DIR
            _SLOT_DATA_DIR = _bdir
            try:
                cmd_bump(_bt, _bconf)
                cmd_bump(_bt, _bconf)
                return sum(1 for l in read_text(os.path.join(_bdir, SLOT_HIGHWATER)).split("\n")
                           if "\t" in l)
            finally:
                _SLOT_DATA_DIR = None

        arm("two --bump runs leave exactly one row per canonical slot, not two",
            str(len(SLOT_CANON)), lambda: str(measure_bump_rows()))
        arm("--bump keeps the file's comment lines across a round-trip", "high-water, seeded empty",
            lambda: read_text(os.path.join(_bdir, SLOT_HIGHWATER)))

        arm("a bullet slot carrying prose is named", "requires a bullet list: ## Expected improvements",
            lambda: str(slot_violations(build_canon_readme(
                GOOD[:6] + ["not a bullet."] + GOOD[7:]), "x", canon=True)))
        # The plan pair belongs to NO slot: the authored half must STOP at it, or its table is read
        # as body content of the last canonical slot.
        arm("the authored plan pair does not become body of the last slot", "[]",
            lambda: str(slot_violations("\n".join([
                "# tOne", ""] + GOOD + ["", PLAN_OPEN, "| # | unit |", PLAN_CLOSE, "",
                MARK_OPEN, MARK_CLOSE, ""]), "x", canon=True)))
        # The registry reader: absent file is the EMPTY SET here, and unit 3 turns that into a
        # refusal. Armed so the handover between the two units is visible rather than assumed.
        t16 = os.path.join(base, "registry"); os.makedirs(t16)
        conf16 = _fixture(t16, spec_status="OPEN")
        # INVERTED BY TOOL-dFramedEntrypoint-3, deliberately and in the unit that changed it. Unit 1
        # shipped an absent registry as the EMPTY SET — a pass — so that it did not depend on a file
        # unit 3 had not written yet. Unit 3 makes it a refusal. Leaving unit 1's arm asserting the
        # old behaviour would have been two arms disagreeing about one contract.
        arm("an absent contract registry now REFUSES (was the empty set until unit 3)", "is absent",
            lambda: read_contract_registry(t16, conf16))
        os.makedirs(os.path.join(t16, "memory", "project"), exist_ok=True)
        write_text(os.path.join(t16, "memory", CONTRACT_REGISTRY),
                   "# a comment\nexempt-pin: 0\nmemory/builds/tOne/README.md\n")
        arm("a registry row binds its path and comments are skipped",
            "memory/builds/tOne/README.md",
            lambda: str(read_contract_registry(t16, conf16)))

        # ------------------------------------- TOOL-dFramedEntrypoint-6, records inside their specs
        _R = {"path": "memory/builds/tOne/reviews/2026-08-01-review-tOne-1.md",
              "kind": "spec-audit", "ids": ["ARCH-tOne-1", "ARCH-tTwo-9"]}
        arm("the region renders a record RELATIVE to the spec's own directory",
            "](../reviews/2026-08-01-review-tOne-1.md)",
            lambda: render_spec_records("ARCH-tOne-1", [_R],
                                        "memory/builds/tOne/spec/2026-08-01-spec-tOne-1.md"))
        # The first cut fell back to the REPO-relative path for a cross-build record, which a reader
        # resolves against the spec's directory — so every cross-build edge linked to nothing.
        arm("a CROSS-BUILD record still resolves, which the repo-relative fallback did not",
            "](../../tOne/reviews/2026-08-01-review-tOne-1.md)",
            lambda: render_spec_records("ARCH-tTwo-9", [_R],
                                        "memory/builds/tTwo/spec/2026-08-01-spec-tTwo-9.md"))
        arm("the region names the OTHER ids a shared record serves", "ARCH-tTwo-9",
            lambda: render_spec_records("ARCH-tOne-1", [_R], "memory/builds/tOne/spec/x.md"))
        arm("a spec no record names renders the EXPLICIT empty case", "*No record names this unit.*",
            lambda: render_spec_records("ARCH-tOne-1", [], "memory/builds/tOne/spec/x.md"))
        arm("the pair is created ABOVE the first numbered section, never inside one", "True",
            lambda: str(add_spec_records_region("# t\n\n**Status:** X\n\n## 1. Goal\n\nbody\n")
                        .index(SPEC_RECORDS_OPEN) <
                        add_spec_records_region("# t\n\n**Status:** X\n\n## 1. Goal\n\nbody\n")
                        .index("## 1. Goal")))
        arm("the inversion keys a record on every id it names, not on its folder", "2",
            lambda: str(len(build_spec_record_index([{"records": [_R]}]))))

        # -------------------------------------------- TOOL-dFramedEntrypoint-3, the contract registry
        t18 = os.path.join(base, "contract"); os.makedirs(t18)
        conf18 = _fixture(t18, spec_status="OPEN")
        reg18 = os.path.join(t18, "memory", CONTRACT_REGISTRY)
        os.makedirs(os.path.dirname(reg18), exist_ok=True)
        trk18 = ["memory/builds/tOne/README.md"]

        def build_reg_check(body):
            write_text(reg18, body)
            return lambda: check_contract_registry(t18, conf18, trk18)

        # An ABSENT registry is a REFUSAL here — the behaviour unit 1 shipped as the empty set, and
        # this unit REPLACES it. Stated in both specs rather than left as two specs disagreeing.
        os.path.exists(reg18) and os.remove(reg18)
        arm("an absent registry refuses, replacing unit 1's empty set", "is absent",
            lambda: check_contract_registry(t18, conf18, trk18))
        arm("a registry with no pin refuses", "no `exempt-pin:` line",
            build_reg_check("memory/builds/tOne/README.md\n"))
        arm("a tracked README named by no row refuses", "names neither a bound nor an exempt row",
            build_reg_check("exempt-pin: 0\n"))
        arm("a row naming a path that is not a tracked README refuses", "stale row silently widens",
            build_reg_check("exempt-pin: 0\nmemory/builds/tOne/README.md\nmemory/builds/ghost/README.md\n"))
        arm("an exempt row with no reason refuses", "carries no reason",
            build_reg_check("exempt-pin: 1\n!memory/builds/tOne/README.md\n"))
        arm("the pin ABOVE the measured count refuses, not only below", "the pin is an equality",
            build_reg_check("exempt-pin: 9\n!memory/builds/tOne/README.md - why\n"))
        arm("a bound row and a matching pin pass", "None",
            lambda: str(build_reg_check("exempt-pin: 0\nmemory/builds/tOne/README.md\n")()))
        arm("a bound row is BOUND and an exempt row is not",
            "{'memory/builds/tOne/README.md'}",
            lambda: str(read_contract_rows(t18, conf18)[0]))

        # ------------------------------------------------ TOOL-dFramedEntrypoint-2, the slot budget
        # THE READER'S OWN TRAP, armed because it shipped broken for one commit: every canonical slot
        # heading starts with `#`, so a comment predicate keyed on `#` ate every data row and the
        # table parsed to EMPTY — which the leg then reported as five deliberate UNARMED slots.
        _tbl = os.path.join(base, "tbl.txt")
        write_text(_tbl, "# a real comment, no tab\n"
                         "## The problem this build exists to solve\t900\n"
                         "## Expected improvements\t\n")
        arm("a heading row is DATA even though it starts with a hash", "900",
            lambda: str(read_slot_table(_tbl).get("## The problem this build exists to solve")))
        arm("a line with no tab is the comment, and is skipped", "1",
            lambda: str(sum(1 for k in read_slot_table(_tbl) if "real comment" in k) + 1))
        arm("a row with no value is the ANNOUNCED unarmed state, not a missing row", "None",
            lambda: str(read_slot_table(_tbl)["## Expected improvements"]))
        # Both directions over the declaration, asserted whether or not anything is BOUND.
        arm("a limits table missing a canonical slot is a refusal", "has NO ROW for the canonical slot",
            lambda: check_slot_table({"## Expected improvements": 1}, "t.txt"))
        arm("a limits row for an unknown slot is a refusal", "which SLOT_CANON does not declare",
            lambda: check_slot_table({h: 1 for h, _e, _b in SLOT_CANON} | {"## Nope": 1}, "t.txt"))
        # The measured slice: authored only, and it STOPS at the roster pair.
        _sz = dict(measure_slot_sizes("\n".join(
            ["# t", ""] + GOOD + ["", PLAN_OPEN, "| # | a very wide authored roster row |", PLAN_CLOSE,
             "", MARK_OPEN, "generated bytes that must not be billed to a slot", MARK_CLOSE, ""])))
        arm("the last slot's slice stops at the roster pair, not the generated marker", "0",
            lambda: str(_sz["## Parked decisions"]))
        arm("a slot's size counts its authored body only", "22",
            lambda: str(_sz["## The problem this build exists to solve"]))

        # ------------------------------------------------ TOOL-dFramedEntrypoint-4, the order verb
        # The shipped regex ended `(?![0-9])`, which rejects a longer NUMBER and nothing else. Both
        # of these were PROBED against it before the change and both rendered a plausible step.
        arm("a hex-looking order value is refused, not read as 0", "not a positive integer",
            lambda: _parse_order("x · order 0x2 · y", "f.md"))
        arm("a digit-then-letter order value is refused, not read as its digit",
            "not a positive integer",
            lambda: _parse_order("x · order 2x · y", "f.md"))
        arm("a well-formed order value still parses", "3",
            lambda: str(_parse_order("x · base ab · order 3 · streams s", "f.md")))
        arm("an order value at the end of the header parses", "7",
            lambda: str(_parse_order("x · base ab · order 7", "f.md")))
        arm("an absent order verb is None, not an error", "None",
            lambda: str(_parse_order("x · base ab · streams s", "f.md")))
        # The duplicate refusal sat BELOW the early return in the first draft, so a header whose
        # first occurrence was well-formed never reached it: present, correct, and unreachable.
        arm("the order verb twice in one header is refused", "more than once",
            lambda: _parse_order("x · order 2 · order 3 · y", "f.md"))

        # S4/S5 — the roster carries ORDER and TIER, sorts by build order, and keeps the two cells
        # the unattended driver selects on: the link FIRST and the status as a whole |-delimited cell.
        t17 = os.path.join(base, "roster"); os.makedirs(t17)
        conf17 = _fixture(t17, spec_status="OPEN")
        sp17 = os.path.join(t17, "memory", "builds", "tOne", "spec")
        write_text(os.path.join(sp17, "2026-01-02-spec-tOne-2.md"),
                   "# ARCH-tOne-2 — second\n\n**Status:** OPEN · rev-1 · 2026-01-02 · node t · "
                   "Tier-1 · base abcdef12 · order 1\n")
        run("git", "add", "-A", cwd=t17)
        run("git", "commit", "-q", "-m", "r", "--no-verify", cwd=t17)
        reg17 = plan(t17, conf17)[0]["memory/builds/tOne/README.md"]
        arm("the roster header carries Order and Tier", "| Unit | Order | Tier | Status |",
            lambda: reg17)
        # SCOPED TO THE ROWS. The first spelling compared `reg17.index(...)` over the whole region
        # and read False on a correct sort, because both ids appear earlier in the `ids` roster line
        # than in the table. An arm that measures the wrong string fails honestly and proves nothing.
        _rows17 = [l for l in reg17.splitlines() if l.startswith("| [")]
        arm("an ordered unit sorts ahead of an unordered one", "True",
            lambda: str(_rows17[0].startswith("| [ARCH-tOne-2") and
                        _rows17[1].startswith("| [ARCH-tOne-1")))
        arm("a unit with no order verb renders an em-dash in that cell", "| — |", lambda: reg17)
        arm("the tier cell always renders a value", "| 1 | OPEN |", lambda: reg17)
        arm("the link cell stays FIRST, which the driver selects on", "True",
            lambda: str(all(l.startswith("| [") for l in reg17.split("\n")
                            if l.startswith("| [") or " — second](" in l)))

        # TOOL-dFramedEntrypoint-5 — the document inventory is GONE, and so are the two arms that
        # rendered it. What they were really watching is the record SELECTOR: the original defect
        # bucketed each record by its own filename, so no kind matched and the region rendered EMPTY
        # between two markers, which reads as "this build holds no records" rather than as a fault.
        # That watch is KEPT, moved onto the counted line that replaced the derived sentence — a
        # build holding records and reporting zero is the same mis-segmentation, said out loud.
        arm("the document inventory region is no longer rendered at all", "False",
            lambda: str("gen:build-docs" in render_region(
                [b for b in collect(t12, conf12) if b["slug"] == "tOne"][0])))

        # S10 — an edge to a build that does not exist is a typo, not a relation.
        t15 = os.path.join(base, "badedge"); os.makedirs(t15)
        conf15 = _fixture(t15, spec_status="OPEN")
        rd15 = os.path.join(t15, "memory", "builds", "tOne", "README.md")
        write_text(rd15, read_text(rd15).replace("ids: ARCH-tOne-1", "ids: ARCH-tOne-1\nparents: tGhost"))
        run("git", "add", "-A", cwd=t15)
        arm("an edge to a nonexistent build is named", "which is not a build folder",
            lambda: plan(t15, conf15))
        # ---- the record->spec binding parser.
        # Every arm is a POSITIVE assertion on a classification, because the failure mode of a
        # head-scan is silence: a boundary set one line short reports "absent" for a conformant
        # record and nothing anywhere says so.
        tb = os.path.join(base, "bind"); os.makedirs(tb)
        bconf = {"MEMORY_ROOT": "memory", "FAMILIES": "tooling:TOOL playbook:PLAY"}

        def _rec(rel, body):
            p = os.path.join(tb, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            write_text(p, body)
            return rel

        def _bind(rel):
            return read_bindings(tb, [rel], bconf)[rel]

        r1 = _rec("memory/builds/tOne/reviews/r.md",
                  "# t\n\n**Serves:** spec-audit TOOL-tOne-1 TOOL-tOne-2\n")
        arm("binding parses kind + ids", "bound", lambda: _bind(r1)["state"])
        arm("binding keeps both ids", "['TOOL-tOne-1', 'TOOL-tOne-2']", lambda: str(_bind(r1)["ids"]))

        r2 = _rec("memory/builds/tOne/reviews/r2.md",
                  "# t\n\n**Serves:** none — the build shipped before any spec existed\n")
        arm("none form with a reason is unbound", "unbound", lambda: _bind(r2)["state"])

        r3 = _rec("memory/builds/tOne/reviews/r3.md", "# t\n\n**Serves:** none\n")
        arm("bare none with no reason is malformed", "malformed", lambda: _bind(r3)["state"])

        r4 = _rec("memory/builds/tOne/reviews/r4.md", "# t\n\n**Serves:** postmortem TOOL-tOne-1\n")
        arm("an unknown kind token is malformed", "is not one of", lambda: _bind(r4)["why"])

        r5 = _rec("memory/builds/tOne/build/r5.md", "# t\n\n**Serves:** journal TOOL-tOne-2..4\n")
        arm("a range EXPANDS at authoring time", "['TOOL-tOne-2', 'TOOL-tOne-3', 'TOOL-tOne-4']",
            lambda: str(_bind(r5)["ids"]))

        r6 = _rec("memory/builds/tOne/reviews/r6.md",
                  "\n" * 13 + "**Serves:** spec-audit TOOL-tOne-1\n")
        arm("a Serves line past the head window is not read", "absent", lambda: _bind(r6)["state"])

        r7 = _rec("memory/builds/tOne/reviews/r7.md",
                  "# t\n\n```\n**Serves:** spec-audit TOOL-tOne-1\n```\n")
        arm("a FENCED example never parses as a binding", "absent", lambda: _bind(r7)["state"])

        r8 = _rec("memory/builds/tOne/build/r8.sh",
                  "#!/bin/sh\n# **Serves:** journal TOOL-tOne-1\n")
        arm("a non-markdown record binds through a comment marker", "bound", lambda: _bind(r8)["state"])

        r9 = _rec("memory/builds/tOne/reviews/r9.md",
                  "# t\n\n**Serves:** diff-review TOOL-tOne-1@rev-3 PLAY-tTwo-9\n")
        arm("a rev qualifier is accepted and normalised away",
            "['TOOL-tOne-1', 'PLAY-tTwo-9']", lambda: str(_bind(r9)["ids"]))
        arm("an id may reach into another build", "PLAY-tTwo-9", lambda: str(_bind(r9)["ids"]))

        r10 = _rec("memory/builds/tOne/reviews/r10.md", "# t\n\n**Serves:** journal TOOL-tOne-x\n")
        arm("a malformed id token is reported, not silently dropped", "TOOL-tOne-x",
            lambda: str(_bind(r10)["bad"]))

        r11 = _rec("memory/builds/tOne/reviews/r11.md",
                   "# t\n\n**Serves:** journal TOOL-tOne-1  <!-- inferred: single-spec build -->\n")
        arm("a trailing comment is a note, not a token", "['TOOL-tOne-1']", lambda: str(_bind(r11)["ids"]))
        arm("a trailing comment contributes no malformed token", "[]", lambda: str(_bind(r11)["bad"]))

        _rec("memory/builds/tOne/spec/s.md", "# TOOL-tOne-1 — the unit\n")
        _rec("memory/builds/tOne/spec/units/s2.md", "# PLAY-tTwo-9 — nested, any depth\n")
        arm("spec_ids resolves an H1 id at any depth under spec/", "PLAY-tTwo-9",
            lambda: str(sorted(spec_ids(tb, ["memory/builds/tOne/spec/s.md",
                                             "memory/builds/tOne/spec/units/s2.md"], bconf))))
        arm("a record is NOT a definition source", "[]",
            lambda: str(sorted(spec_ids(tb, [r1], bconf))))

        # The read-only property, asserted as an ON-DISK effect rather than an exit code: a
        # read-only verb that writes is the whole risk of that verb.
        t12 = os.path.join(base, "ro"); os.makedirs(t12)
        conf12 = _fixture(t12)
        cmd_write(t12, conf12)
        _before = {p: read_text(os.path.join(t12, p)) for p in
                   ("memory/LIVE.md", "memory/builds/tOne/README.md")}
        cmd_print_bindings(t12, conf12)
        arm("--print-bindings leaves every generated artifact byte-identical", "True",
            lambda: str(all(read_text(os.path.join(t12, p)) == v for p, v in _before.items())))

        # The S row: a BOUND record is not a finding, so nothing else in this output mentions it,
        # and check 21's filename-vs-header branch has no input without it.
        def _rows(tree, cf):
            import io as _io, contextlib as _cl
            buf = _io.StringIO()
            with _cl.redirect_stdout(buf):
                cmd_print_bindings(tree, cf)
            return buf.getvalue()

        t13 = os.path.join(base, "srow"); os.makedirs(t13)
        conf13 = _fixture(t13)
        p13 = os.path.join(t13, "memory/builds/tOne/reviews/2026-08-01-review-tOne-1.md")
        os.makedirs(os.path.dirname(p13), exist_ok=True)
        write_text(p13, "# r\n\n**Serves:** spec-audit ARCH-tOne-1\n")
        run("git", "add", "-A", cwd=t13)
        arm("a bound record emits an S row carrying kind and the resolved ids",
            "S\tmemory/builds/tOne/reviews/2026-08-01-review-tOne-1.md\tspec-audit\tARCH-tOne-1",
            lambda: _rows(t13, conf13))
        arm("--print-bindings still exits 0 with an S row present", "0",
            lambda: str(cmd_print_bindings(t13, conf13)))

        # ---- the rendered Records table and the two coverage joins.
        # TOOL-dFramedEntrypoint-5 S4 classes (b) and (c). The RECORDS TABLE arm and the FOLDER
        # SENTENCE arm both lose their subject here. The sentence was the record selector's liveness
        # assertion — its absence is what nine arms watched for — so the watch moves onto the counted
        # line that replaced it, over the fixture that actually HOLDS a record. A build holding one
        # record and reporting zero is the same mis-segmentation the sentence used to reveal by
        # vanishing, and this says it out loud instead of inferring it from an absence.
        arm("the record selector reports a NON-ZERO count for a build that holds records",
            "Records: 1 bound to this build",
            lambda: plan(t13, conf13)[0]["memory/builds/tOne/README.md"])
        arm("the record count names how many FOLDERS the records sit in", "record folder(s)",
            lambda: plan(t13, conf13)[0]["memory/builds/tOne/README.md"])
        arm("the records TABLE is no longer rendered", "False",
            lambda: str("| Record | Kind | Serves |" in
                        plan(t13, conf13)[0]["memory/builds/tOne/README.md"]))
        # The record above serves the build's only id, so neither join has anything to report. A
        # positive-population arm: an empty table rendering silently is the failure that matters.
        arm("a fully-covered build STILL renders both joins, saying none", "True",
            lambda: str("Ids no record names: none" in
                        plan(t13, conf13)[0]["memory/builds/tOne/README.md"]))
        t14 = os.path.join(base, "gap"); os.makedirs(t14)
        conf14 = _fixture(t14)
        p14 = os.path.join(t14, "memory/builds/tOne/build/2026-08-01-build-tOne-1.md")
        os.makedirs(os.path.dirname(p14), exist_ok=True)
        write_text(p14, "# j\n\n**Serves:** journal ARCH-tOne-1\n")
        run("git", "add", "-A", cwd=t14)
        arm("a build whose only record is a journal names its id as never spec-audited",
            "Ids no `spec-audit` record has ever named: ARCH-tOne-1",
            lambda: plan(t14, conf14)[0]["memory/builds/tOne/README.md"])
        arm("...and its other join says `none`, because a journal DID name that id", "True",
            lambda: str("Ids no record names: none" in
                        plan(t14, conf14)[0]["memory/builds/tOne/README.md"]))
        t15 = os.path.join(base, "norec"); os.makedirs(t15)
        conf15 = _fixture(t15)
        arm("a build with NO records renders no table, and BOTH joins saying none", "True",
            lambda: str("| Record | Kind | Serves |" not in
                        plan(t15, conf15)[0]["memory/builds/tOne/README.md"]))
        # TOOL-dRetiredFork-18. This arm grades the EMISSION, which is the gap the two arms on
        # `_render_wrapped_ids` could not see: that helper passed in isolation for as long as
        # nothing called it, while a 24-unit build rendered 509- and 531-character gap lines. The
        # subject is therefore the rendered README's widest line, not the helper's return.
        t16 = os.path.join(base, "wide"); os.makedirs(t16)
        conf16 = _fixture(t16)
        d16 = os.path.join(t16, "memory/builds/tOne/spec")
        for n in range(2, 62):
            write_text(os.path.join(d16, "2026-08-01-spec-tOne-%d.md" % n),
                       "# ARCH-tOne-%d — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-08-01 · "
                       "node a · Tier-2 · base 0123abcd\n" % n)
        run("git", "add", "-A", cwd=t16)
        # SCOPED to the gap PARAGRAPHS, and both scopings were mistakes this arm made first.
        # A draft measured the widest line in the whole render and failed on the front-matter
        # `ids:` line at 398 characters, which check 7 does not grade — an arm whose population is
        # wider than the rule it grades reports a defect nobody owes. A second draft counted lines
        # beginning `Ids no `, which counts PARAGRAPH HEADS: a wrapped continuation carries ids and
        # no prefix, so a working wrap scored 2 and read as no wrap at all.
        def _extract_gap_para(head):
            body = plan(t16, conf16)[0]["memory/builds/tOne/README.md"].split("\n")
            i = next((n for n, x in enumerate(body) if x.startswith(head)), None)
            if i is None:
                return []
            out = [body[i]]
            for x in body[i + 1:]:
                if not x.strip():
                    break
                out.append(x)
            return out

        arm("a 61-unit build's gap paragraph wraps in the RENDER, not only in the helper", "True",
            lambda: str(max((len(x) for x in _extract_gap_para("Ids no record names:")), default=10 ** 6)
                        <= IDS_WRAP + 1))
        # ANTI-VACUITY. Without this the arm above passes on a build whose ids happen to fit, which
        # is what a 31-unit fixture did: 291 characters, one line, no wrap ever exercised.
        arm("...and the wrap actually happened, so the arm cannot pass on a short list", "True",
            lambda: str(len(_extract_gap_para("Ids no record names:")) > 1))
        arm("the spec-audit gap paragraph wraps too", "True",
            lambda: str(len(_extract_gap_para("Ids no `spec-audit` record has ever named:")) > 1
                        and max((len(x) for x in
                                 _extract_gap_para("Ids no `spec-audit` record has ever named:")),
                                default=10 ** 6) <= IDS_WRAP + 1))

        # TOOL-dRetiredFork-2 — the git-environment leak. Git exports GIT_DIR to every hook, and a
        # generator started from one inherits a pointer to a DIFFERENT repository, which it then
        # reads silently. Measured before the scrub was wired: with GIT_DIR naming a decoy, `--check`
        # died `build-index: not a git repo` at exit 2; with it, exit 0 and byte-identical output.
        def _run_under_decoy_git_dir():
            with tempfile.TemporaryDirectory() as decoy:
                saved = os.environ.get("GIT_DIR")
                os.environ["GIT_DIR"] = decoy
                try:
                    return run("git", "rev-parse", "--show-toplevel").strip()
                finally:
                    if saved is None:
                        os.environ.pop("GIT_DIR", None)
                    else:
                        os.environ["GIT_DIR"] = saved

        # ANTI-VACUITY: it asserts the REAL toplevel comes back, not merely that nothing raised. A
        # decoy that happened to resolve would still fail this.
        arm("an inherited GIT_DIR does not redirect the generator's git calls", "True",
            lambda: str(_run_under_decoy_git_dir()
                        == run("git", "rev-parse", "--show-toplevel").strip()))
        arm("...and GIT_DIR is not in the environment run() hands the subprocess", "True",
            lambda: str("GIT_DIR" not in _build_git_env()))

        # TOOL-dRetiredFork-3 — a PRESENT but unparseable header is not an ABSENT one. Before this,
        # both raised the same Problem, so a corrupted header read as a missing one and the index
        # regenerated around it.
        def _derive_kind_exc(body: str):
            try:
                parse_front_matter(_build_header(body), "tOne")
            except StaleHeader as exc:
                return exc
            except Problem:
                return None
            return None

        def _build_header(body: str) -> str:
            d = tempfile.mkdtemp()
            p = os.path.join(d, "README.md")
            with open(p, "w", encoding="utf-8", newline="") as fh:
                fh.write(body)
            return p

        _good = ("---\nslug: tOne\nnode: t\nopened: 2026-09-02\nstreams: tooling\n"
                 "roster: TOOL\nids: TOOL-tOne-1\n---\n# t\n")

        def _derive_kind(body: str) -> str:
            try:
                parse_front_matter(_build_header(body), "tOne")
            except StaleHeader:
                return "StaleHeader"
            except Problem:
                return "Problem"
            return "parsed"

        arm("a conforming header parses", "parsed", lambda: _derive_kind(_good))
        # THE DISTINCTION ITSELF, and the reason this unit exists. Absent stays Problem; present
        # and malformed becomes StaleHeader. An arm asserting only the second would pass even if
        # BOTH raised StaleHeader, which is the collapse in the other direction.
        arm("an ABSENT header is a Problem, not a StaleHeader", "Problem",
            lambda: _derive_kind("# no front matter here\n"))
        arm("a PRESENT but indented key is a StaleHeader", "StaleHeader",
            lambda: _derive_kind(_good.replace("node: t", "  node: t")))
        arm("a header that never closes is a StaleHeader", "StaleHeader",
            lambda: _derive_kind("---\nslug: tOne\n# never closed\n"))
        arm("a StaleHeader carries the region for the report", "True",
            lambda: str(bool(getattr(_derive_kind_exc(_good.replace("node: t", "  node: t")), "region", ""))))

        def _read_waiver(body: str | None):
            d = tempfile.mkdtemp()
            os.makedirs(os.path.join(d, "memory", "project"), exist_ok=True)
            if body is not None:
                with open(os.path.join(d, "memory", STALE_HEADER_WAIVER), "w",
                          encoding="utf-8", newline="") as fh:
                    fh.write(body)
            try:
                return str(read_stale_header_waiver(d, "memory", ["memory/builds/x/README.md"]))
            except Problem as exc:
                return str(exc)

        arm("an EMPTY waiver registry is not an error", "{}",
            lambda: _read_waiver("# only comments\n\n"))
        arm("a MISSING waiver registry REFUSES", "absent", lambda: _read_waiver(None))
        arm("a waiver row naming an untracked path REFUSES", "outlived",
            lambda: _read_waiver("memory/builds/ghost/README.md   gone\n"))

    if fails:
        print(f"FAIL — {len(fails)} arm(s) failed")
        return 1
    print("PASS — gen_build_index: all arms held")
    return 0


def main(argv: list) -> int:
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        return cmd_selftest()
    if mode not in ("--check", "--write", "--check-format", "--print-bindings", "--survey",
                    "--report", "--bump"):
        print("usage: gen_build_index.py "
              "[--check|--write|--check-format|--survey|--report|--bump|"
              "--print-bindings|--selftest]")
        return 2
    try:
        root = run("git", "rev-parse", "--show-toplevel").strip()
    except Exception:  # noqa: BLE001
        print("build-index: not a git repo")
        return 2
    conf = load_conf(root)
    if mode == "--print-bindings":
        return cmd_print_bindings(root, conf)
    try:
        if mode == "--check-format":
            return cmd_check_format(root, conf)
        if mode == "--survey":
            return cmd_survey(root, conf)
        if mode == "--report":
            return cmd_report(root, conf)
        if mode == "--bump":
            return cmd_bump(root, conf)
        return cmd_check(root, conf) if mode == "--check" else cmd_write(root, conf)
    except Problem as exc:
        print(f"build-index: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
