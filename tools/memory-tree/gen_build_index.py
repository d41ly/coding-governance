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

FOUR SOURCES, NOTHING ELSE
  * each build's README front matter (slug node opened streams roster [status])
  * every `**Status:**` header under that build's spec/, at any depth
  * for the ROSTER only, every tracked file under the memory root EXCEPT this field's own outputs —
    the build's own README and the generated index and shards. `ids` is therefore an OUTPUT, not a
    source: `--write` overwrites whatever was authored there.
  * under `BACKLOG_MODE=builds` ONLY, every tracked `builds/<slug>/BACKLOG.md`, read through
    `backlog.py`'s grammar and folded into the family views. Under `shards` that source does not
    exist and not one branch below it is reached, which is what keeps this change dark.
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

import contextlib
import datetime
import io
import json
import os
import pathlib
import re
import shutil
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
# TOOL-dDerivedDocket-6 -- the backlog grammar, the two status-header verbs and the status fold. The
# DEPENDENCY RUNS ONE WAY: this module calls into that one and that one imports nothing from here,
# so the two cannot deadlock at import and `backlog.py` stays usable by a reader that never renders
# an index. The verbs it reads are PERMITTED and never required, so a header carrying neither parses
# byte-identically to how it parsed before this import existed.
import backlog  # noqa: E402  a sibling of this file, reached by the path insert above

def load_conf(root: str) -> dict:
    conf = {"MEMORY_ROOT": "memory", "DISCIPLINES": "", "FAMILIES": ""}
    path = os.path.join(root, ".memory-tree.conf")
    if os.path.isfile(path):
        parse_conf(read_text(path), conf)
    return conf


def read_conf_at_rev(root: str, rev: str) -> dict:
    """The conf AS OF `rev`, through the same parser `load_conf` uses, or a named refusal.

    TOOL-dDerivedDocket-53. A read pinned at a rev used to mix a pinned tree with evaluation-time
    DECLARATIONS: `main()` resolves the working-tree root and calls `load_conf` on it above every
    mode dispatch, so a mode that knows a rev was named is reached with the conf already read from
    whatever the checkout happens to hold. This is the sibling such a mode calls instead, and it
    pins the DECLARATIONS only — a conf VALUE naming a path still points into whatever tree the
    caller then reads (`read_contract_rows` is the instance), which is the caller's to route.

    A SIBLING, NOT A DEFAULTED PARAMETER on `load_conf`. One name with two meanings would make
    every existing caller in the kit a pinned read that happens to be pinned at the working tree,
    and the shell gate that SOURCES the same file would have no way to say which it meant.

    IT NEVER FALLS BACK. Each of the three refusals is a state that would otherwise answer with
    evaluation-time declarations while still LOOKING pinned, which is the whole defect wearing a
    different hat.

    THE THIRD REFUSAL COUNTS DECLARATIONS, AND COUNTS WHAT THE BLOB YIELDED. `parse_conf` cannot
    fail: it keeps whatever `parse_conf_line` returns and silently drops every line that yields
    nothing, so a blob of arbitrary bytes does not raise — it parses to the caller's own defaults
    with nothing merged in, and the grade then rests on those defaults. Counting is not the second
    grammar S1 bans: it reads no line, accepts every spelling that parser accepts, and decides
    nothing the shell gate could disagree with. The count is taken from a parse into an EMPTY dict
    and never from the size of the dict returned below, because the seed would keep that dict
    non-empty however empty the blob was — a reader grading the returned size would never refuse,
    which is this refusal's own defect wearing the mechanism meant to catch it.

    STATED RESIDUAL: a conf that is legally all comments and blank lines refuses here. That is
    deliberate. A file declaring nothing cannot pin anything, and it makes this reader stricter than
    `load_conf`, which treats an absent file as defaults — the two never have to agree, which is why
    that one keeps its bytes.

    The seed below is RESPELLED rather than hoisted out of `load_conf` for that same reason; the two
    literals are held equal by a selftest arm instead of by one constant.
    """
    name = ".memory-tree.conf"
    try:
        sha = run("git", "rev-parse", "--verify", "--quiet", rev + "^{commit}", cwd=root).strip()
    except subprocess.CalledProcessError:
        sha = ""
    if not sha:
        raise Problem(
            f"conf at rev {rev}: that rev resolves to no commit in this repository, so {name} "
            f"could not be looked up at it — and a pinned read never falls back to the working tree")
    try:
        # BYTES, and NOT through `run()`, which is this module's one git choke point — the only
        # site in the file that does not use it. `run()` decodes with the locale encoding and
        # UNIVERSAL-NEWLINES the result, and both of those make this reader disagree with
        # `read_text`, which decodes utf-8 and folds `\r\n` alone. A lone CR is the machine-
        # independent half: universal newlines turns it into a line break, so `A=1<CR>B=2` parses
        # to TWO declarations here and to one in the working tree — and to one in the shell gate
        # that SOURCES the same file, which is the split the one-parser rule exists to close. The
        # locale half hides on a node in UTF-8 mode and appears on one that is not. The env scrub
        # `run()` centralises is passed explicitly here rather than forgotten, which is the thing
        # that choke point is for; what it cannot give is bytes. A blob that is not utf-8 raises
        # here exactly as `read_text` raises for the working-tree read — parity with the reader
        # this one shadows, rather than a fourth state only one of the two knows about.
        blob = subprocess.run(("git", "show", f"{sha}:{name}"), cwd=root, capture_output=True,
                              check=True, env=_build_git_env()).stdout
        text = blob.decode("utf-8").replace("\r\n", "\n")
    except subprocess.CalledProcessError:
        raise Problem(
            f"conf at rev {rev} ({sha[:12]}): the tree at that rev carries no {name} blob, so "
            f"there is nothing there to pin — and a pinned read never falls back to the working "
            f"tree") from None
    declared = parse_conf(text, {})
    count = len(declared)
    if count == 0:
        raise Problem(
            f"conf at rev {rev} ({sha[:12]}): the {name} blob at that rev yields zero "
            f"declarations, so a pinned answer would grade on this reader's own defaults while "
            f"still reading as pinned — and a file declaring nothing pins nothing")
    # S3 — the SOURCE, on every pinned read, on stderr. A pinned read that says nothing about where
    # its declarations came from is indistinguishable from an unpinned one, and stderr is the
    # channel every notice in this module already takes: stdout is a value a program parses.
    print(f"build-index: conf pinned at {rev} ({sha[:12]}) · {name} · {count} declaration(s)",
          file=sys.stderr)
    conf = {"MEMORY_ROOT": "memory", "DISCIPLINES": "", "FAMILIES": ""}
    conf.update(declared)
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


def _read_backlog_verbs(header: str, path: str, alt: str) -> dict:
    try:
        return backlog.read_header_verbs(header, path, lambda rest: _expand_ids(rest, alt))
    except backlog.Problem as exc:
        raise Problem(str(exc)) from None


def parse_spec(path: str, alt: str = "(?!)") -> dict | None:
    """`parse_spec_text` over the file at `path`. The working-tree binding, and the only one the
    render path uses."""
    return parse_spec_text(read_text(path), path, alt)


def parse_spec_text(text: str, path: str, alt: str = "(?!)") -> dict | None:
    """Return the unit record, or None when the text carries no parseable status header.

    SPLIT FROM `parse_spec` by TOOL-dDerivedDocket-15, because a read pinned at a rev holds the
    spec's BYTES and has no file to hand a reader. One parser with two bindings, so a pinned grade
    and a working-tree grade cannot disagree about what a status header says.

    A grandfathered recording legitimately has none; check 12 already rejects a post-cutoff spec
    that is missing one, so this file never has to defend against a malformed header.

    `alt` is the caller's family alternation, used only to expand the two backlog verbs. It DEFAULTS
    TO A NEVER-MATCHING PATTERN rather than to this repo's families: a caller that did not pass one
    has no id grammar to offer, and admitting every token would be a grammar bound to the wrong tree
    — the shape whose empty classification reads exactly like a clean corpus.
    """
    body = list(unfenced(text))
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
        # The two BACKLOG verbs, on the same terms as `order` and refusing on the same grounds. The
        # reader is `backlog.py`'s, and the range expansion is this module's own `_expand_ids`,
        # passed IN rather than imported there: the id alternation is derived from the caller's conf
        # and that module must not grow a second one. `backlog.Problem` is re-raised as this file's
        # own, because `collect()` is reached by --check and --write through one call site and an
        # unfamiliar exception class there would be a traceback rather than a named failure.
        **_read_backlog_verbs(hdr.string, path, alt),
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


def rosters(root: str, tracked: list, m: str, families: set,
            skip_backlog: bool = False) -> dict:
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
        # UNDER `builds` THE FAMILY VIEWS JOIN THAT OUTPUT SET, and under `shards` they must not.
        # The family shards are an INPUT in that mode — a roster legitimately names an id that
        # appears in its shard and nowhere else — so an UNCONDITIONAL skip here would move rosters
        # in every shards adopter on upgrade, for a mode they have not adopted. Measured on this
        # corpus when the unconditional form was tried: 31 of 107 rosters changed.
        if skip_backlog and p.startswith(f"{m}/backlog/"):
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


def collect(root: str, conf: dict, backlog_out: dict | None = None) -> list:
    """Every indexed build. `backlog_out`, when passed, is FILLED with this run's backlog reading.

    AN OUT-PARAMETER RATHER THAN A SECOND RETURN VALUE. The render path is the only caller that
    wants the backlog; widening the return to a tuple would move every other call site and every
    selftest arm that indexes this list, for a value none of them reads. The dict it fills carries
    `mode`, `conf`, `corpus`, `fold`, `families`, `excerpt`, `verdicts` and `line`.
    """
    m = conf["MEMORY_ROOT"]
    tracked = [p for p in run("git", "ls-files", "--", m + "/", cwd=root).split("\n") if p]
    bconf = _read_backlog_conf(conf)
    stale_waived = read_stale_header_waiver(root, m, tracked)
    tolerated: list = []
    slugs = sorted({p.split("/")[2] for p in tracked if p.startswith(m + "/builds/") and p.count("/") >= 3})
    disciplines = set(conf["DISCIPLINES"].split())
    families = {pair.split(":")[1] for pair in conf["FAMILIES"].split() if ":" in pair}
    # Two granularities, as the hygiene engine's own guard does it. The PRECONDITION asks whether the
    # scan recognised anything at all; the per-build POPULATION asks whether this build did. Without
    # the first, a families list bound to the wrong tree renders every roster empty — and an empty
    # classification is exactly what a clean corpus yields, so the failure would look like success.
    roster_by_slug = rosters(root, tracked, m, families,
                             skip_backlog=bconf.mode == "builds")
    # NO EMPTINESS PRECONDITION HERE, deliberately. The wrong-root class says an unrecognising
    # grammar yields the same empty result a clean corpus does, so a guard is wanted — but every
    # signal available HERE is one this function derives from the same conf, which makes the
    # assertion a tautology (the repo's assertion-between-two-derived-values class). Build count
    # fails on a sparse tree; spec-file existence fails too, because a legacy recording legitimately
    # carries no id. The guard that actually holds is INDEPENDENT and already runs below: every
    # build's authored `roster:` value must be a declared family, so a FAMILIES list bound to the
    # wrong tree reds there, by name, before any roster is rendered.
    builds = []
    spec_index: dict = {}
    for slug in slugs:
        readme = f"{m}/builds/{slug}/README.md"
        if readme not in tracked:
            # A FILING HOME, under `builds` ONLY. A folder holding one tracked `BACKLOG.md` and
            # nothing else is where a straggler's relocated asks land before any build claims them.
            # It has no front matter because it is not a build, and it must reach neither LIVE.md
            # nor a ledger shard — which is exactly what skipping it here achieves, since both are
            # rendered from this list. The asks in it are still read: the backlog walk below reads
            # every tracked `BACKLOG.md`, not only the ones sitting beside a README.
            #
            # The tolerance is NARROW (one file, that name) and MODE-SCOPED. A shards adopter's
            # README-less build folder is still the silent departure this refusal was written for,
            # and widening it for them would retire a live refusal to buy a mode they never set.
            own = [p for p in tracked if p.startswith(f"{m}/builds/{slug}/")]
            if bconf.mode == "builds" and own == [f"{m}/builds/{slug}/BACKLOG.md"]:
                continue
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
        units = [parse_spec(os.path.join(root, p), _id_alternation(conf)) for p in specs]
        # THE SPEC INDEX THE FOLD READS, built from the parse this loop already performs and keyed
        # by the spec's H1 id. The path stored is the REPO-RELATIVE one, not `parse_spec`'s
        # absolute argument: every verdict message names it, and an absolute Windows path in a
        # verdict is a string no reader can grep for and no other node can resolve.
        for rel, unit in zip(specs, units):
            if unit:
                spec_index[unit["id"]] = backlog.Spec(unit["id"], rel, unit["status"],
                                                      tuple(unit["closes"]),
                                                      tuple(unit["advances"]))
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
    reading = read_backlog(root, conf, tracked, {b["slug"]: b["status"] for b in builds},
                           spec_index, bconf, tuple(sorted(families)))
    # ON EVERY RUN, INCLUDING THE SHARDS ONE, which says the layout is shards and that no view was
    # rendered. A builds-mode tree whose `BACKLOG.md` files parse to nothing would otherwise print
    # nothing here, and an absent line reads exactly like an empty clean backlog — the reassuring
    # zero a liveness assertion exists to refuse.
    print(reading["line"])
    if backlog_out is not None:
        backlog_out.update(reading)
    return builds


# ------------------------------------------------------------------------------- the backlog
# THREE CODES THIS FILE ADDS to the ones `backlog.py` exports. They continue that module's ONE
# sequence past V16 rather than opening a namespace of their own: the docs unit's drift arm reads
# the codes as one list, and a second sequence starting at 1 would collide with it on every number.
# None of the three is a CONTENT verdict — each is a property of the POPULATION this generator
# walks, which is why they are computed here and not in a module that never reads a tree.
GUARD_DATA_LOSS = 17
GUARD_MODE = 18
GUARD_ARCHIVE = 19
GUARD_CODES = (GUARD_DATA_LOSS, GUARD_MODE, GUARD_ARCHIVE)

#: The markers a three-way merge leaves behind. Matched as a PREFIX, because git writes the branch
#: name after the marker and a full-line compare would miss every real one.
CONFLICT_MARKS = ("<<<<<<<", "=======", ">>>>>>>")


def _read_backlog_conf(conf: dict):
    """`backlog.read_conf`, with its refusal re-raised as this file's own named failure.

    The same seam `_read_backlog_verbs` already draws, and for the same reason: `collect()` is
    reached by every mode through one call site, and an unfamiliar exception class there is a
    traceback rather than the named failure this file's blind-spot-3 rule promises.
    """
    try:
        return backlog.read_conf(conf)
    except backlog.Problem as exc:
        raise Problem(str(exc)) from None


def _read_excerpt(conf: dict) -> int:
    try:
        return backlog.read_excerpt_chars(conf)
    except backlog.Problem as exc:
        raise Problem(str(exc)) from None


def scan_mode_guard(tracked: list, specs: dict, m: str) -> list:
    """Under `shards`: the half-migration shape, from both of its sides.

    A tracked `BACKLOG.md` under `shards` is asks nobody reads — the fold is not running. A spec
    header carrying `closes` or `advances` under `shards` is the same half-migration seen from the
    spec side: a verb that links to asks no tree holds. Both are silent without this, because
    neither is malformed; they are simply inert, and an inert record looks exactly like a clean one.
    """
    out = []
    for rel in sorted(p for p in tracked
                      if p.startswith(f"{m}/builds/") and p.endswith("/BACKLOG.md")):
        out.append(backlog.Verdict(
            GUARD_MODE,
            f"{rel}: a tracked BACKLOG.md while {backlog.MODE_KEY} is `shards`, so every ask in it "
            f"is read by nothing and disposed of by nothing — set the key or remove the file",
            (rel,)))
    for spec in sorted(specs.values()):
        if spec.closes or spec.advances:
            named = " ".join(sorted(set(spec.closes) | set(spec.advances)))
            out.append(backlog.Verdict(
                GUARD_MODE,
                f"{spec.path}: the status header links {named} while {backlog.MODE_KEY} is "
                f"`shards`, so the verb names asks no tracked file files",
                (spec.path,)))
    return out


def scan_archive_guard(tracked: list, m: str, families) -> list:
    """Under `builds`: a rotated backlog archive, which the per-build model does not have.

    THE PREDICATE IS THE STEM, NOT THE DIRECTORY. Every archive lives under the same folder and the
    decision log rotates into it too, so a rule matching every name there would red
    `DECISIONS.<date>.md` on every run — the innocent-file class a candidate predicate is supposed
    to be run over the real tree to catch.
    """
    fams = set(families)
    out = []
    for rel in sorted(p for p in tracked if p.startswith(f"{m}/archive/")):
        stem = os.path.basename(rel).split(".")[0]
        if stem in fams:
            out.append(backlog.Verdict(
                GUARD_ARCHIVE,
                f"{rel}: a rotated `{stem}` backlog archive while {backlog.MODE_KEY} is `builds`, "
                f"where an ask is never rotated out of its build — its rows belong in the build "
                f"folders the ids name",
                (rel,)))
    return out


def read_backlog(root: str, conf: dict, tracked: list, statuses: dict, specs: dict,
                 bconf, families: tuple) -> dict:
    """Everything the backlog model contributes to one run, read ONCE, by `collect()`.

    CONTENT NEVER RAISES HERE either. An unreadable `BACKLOG.md` becomes a V2 naming it, on the
    same grounds the parser gives: one bad file in one build must not refuse every artifact this
    generator renders.
    """
    m = conf["MEMORY_ROOT"]
    out = {"mode": bconf.mode, "conf": bconf, "corpus": None, "fold": None, "families": families,
           "excerpt": backlog.EXCERPT_DEFAULT, "verdicts": [], "line": ""}
    if bconf.mode != "builds":
        out["verdicts"] = scan_mode_guard(tracked, specs, m)
        out["line"] = (f"build-index: backlog layout is `shards` — asks live in {m}/backlog/, no "
                       f"family view is rendered and {len(out['verdicts'])} mode verdict(s) stand")
        return out
    out["excerpt"] = _read_excerpt(conf)
    grammar = backlog.build_grammar(families)
    files, verdicts = [], []
    for rel in sorted(p for p in tracked
                      if p.startswith(f"{m}/builds/") and p.endswith("/BACKLOG.md")
                      and p.count("/") == 3):
        text, why = read_text_or_none(os.path.join(root, rel))
        if text is None:
            verdicts.append(backlog.Verdict(2, f"{rel}: {why}", (rel,)))
            continue
        files.append(backlog.parse_file(rel, text, grammar))
    corpus = backlog.build_corpus(files, specs, statuses)
    fold = backlog.derive_statuses(corpus)
    verdicts += backlog.derive_verdicts(corpus, bconf)
    verdicts += scan_archive_guard(tracked, m, families)
    c = fold.counts
    out.update(corpus=corpus, fold=fold, verdicts=verdicts,
               line=(f"build-index: backlog {c['asks']} ask(s) · {c['rows']} row(s) · "
                     f"{c['links']} link(s) in {c['files']} file(s) · {c['live']} live · "
                     f"{len(verdicts)} verdict(s)"))
    return out


def _build_authored_row_re(families) -> "re.Pattern":
    """A list row leading with an id — the one shape the view grammar never emits.

    That is the whole test for authored content, and it is deliberately narrow. Every authored
    backlog shard this corpus has ever held keys its rows on an id after a list marker, and the
    view's own first cell is link-wrapped precisely so this pattern cannot match it. A looser
    predicate would red a view over its own prose.
    """
    alt = "|".join(sorted(re.escape(f) for f in families)) or "(?!)"
    return re.compile(r"^\s*[-*]\s+[\[`*]*(?:" + alt + r")-[A-Za-z0-9]+-\d+\b")


def scan_view_guard(root: str, rel: str, family: str, conf: dict, kit: str,
                    families: tuple) -> tuple:
    """Read whatever sits at a view path and answer whether `--write` may render over it.

    THE FILE IS READ WHETHER OR NOT IT IS A VIEW, and the view predicate is never consulted here
    (fork F6). A pre-flip shard left in place, and a view whose conflict somebody resolved by
    taking the authored side, both carry the generator's header on neither line one nor line two —
    so a guard that only read files the predicate recognises would hand `--write` exactly the two
    files it must never overwrite.

    Returns `(offending_lines, conflicted)`. `conflicted` says a conflict region was found whose
    two sides hold only lines the view grammar emits: that is a view merged with a view, the render
    repairs it, and refusing it would point a lander at a straggler recipe where no straggler is.
    """
    path = os.path.join(root, rel)
    if not os.path.isfile(path):
        return [], False
    text, why = read_text_or_none(path)
    if text is None:
        return [f"{rel}: {why}"], False
    grammar_lines = backlog.read_view_grammar_lines(family, conf["MEMORY_ROOT"], kit, GEN_HEADER)
    # THE FAMILIES ARE PASSED IN, ALREADY VALIDATED. Re-splitting them out of the raw conf here
    # would be a second derivation of a value `backlog.build_grammar` has already refused on, and
    # these tokens go into a REGEX — where a quoted value matches nothing and a value carrying a
    # pipe swallows a subtree, both in silence.
    authored = _build_authored_row_re(families)
    lines = text.split("\n")
    offending, conflicted = [], False
    n = 0
    while n < len(lines):
        line = lines[n]
        if line.startswith(CONFLICT_MARKS[0]):
            end = n + 1
            while end < len(lines) and not lines[end].startswith(CONFLICT_MARKS[2]):
                end += 1
            if end >= len(lines):
                offending.append(f"{rel}:{n + 1}: a conflict marker with nothing closing it")
                break
            sides = [x for x in lines[n + 1:end] if not x.startswith(CONFLICT_MARKS[1])]
            bad = [x for x in sides if not backlog.check_view_line(x, grammar_lines)]
            if bad:
                offending.append(f"{rel}:{n + 1}: a conflict region carrying {len(bad)} line(s) "
                                 f"the view grammar never emits, the first being: {bad[0].strip()}")
            else:
                conflicted = True
            n = end + 1
            continue
        if line.startswith(CONFLICT_MARKS[1]) or line.startswith(CONFLICT_MARKS[2]):
            offending.append(f"{rel}:{n + 1}: a conflict marker with no `{CONFLICT_MARKS[0]}` "
                             f"opening it")
        elif authored.match(line):
            offending.append(f"{rel}:{n + 1}: {line.strip()}")
        n += 1
    return offending, conflicted


def render_views(root: str, conf: dict, reading: dict) -> tuple:
    """One view per DECLARED family, and the set of view paths `--write` must not touch.

    EVERY DECLARED FAMILY GETS A FILE, including the ones with no live ask. An absent view and an
    empty family are otherwise the same byte on disk, and a reader who finds no file cannot tell
    "nothing is open" from "the render never ran".
    """
    m = conf["MEMORY_ROOT"]
    kit = kit_rel()
    asks = [a for parsed in reading["corpus"].files for a in parsed.asks]
    views, guarded = {}, {}
    for family in reading["families"]:
        rel = f"{m}/backlog/{family}.md"
        offending, conflicted = scan_view_guard(root, rel, family, conf, kit,
                                                reading["families"])
        if offending:
            guarded[rel] = offending
            continue
        if conflicted:
            print(f"build-index: re-rendered over a view conflict: {rel}")
        views[rel] = backlog.render_family_view(family, asks, reading["fold"], m, kit, GEN_HEADER,
                                                reading["excerpt"])
    return views, guarded


def print_verdicts(verdicts: list, guarded: dict, conf: dict) -> int:
    """The VERDICT list, separate from the DRIFT list and carrying a code on every row.

    SEPARATE BECAUSE THE REMEDIES DIFFER, and one shared header would name the wrong one. Drift is
    repaired by `--write`. A verdict is repaired by editing the record it names. And a GUARDED VIEW
    is repaired by the relocation recipe — never by `--write`, which is the one action that would
    destroy the rows the guard is standing in front of. That remedy line is why this function
    exists: `--check`'s single `--write` remedy is what made the data-loss path reachable.
    """
    if not verdicts and not guarded:
        return 0
    print("build-index VERDICT — records the backlog fold read and disagrees with")
    for v in sorted(verdicts, key=lambda x: (x.code, x.text)):
        print(f"    V{v.code} {v.text}")
    for rel, lines in sorted(guarded.items()):
        print(f"    V{GUARD_DATA_LOSS} {rel} carries content the view grammar never emits, so "
              f"--write leaves this file byte-unchanged and renders every other artifact:")
        for line in lines:
            print("        " + line)
        for line in backlog.render_relocation_recipe(kit_rel(), conf["MEMORY_ROOT"]):
            print("        " + line)
    return 1


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
    reading: dict = {}
    builds = collect(root, conf, backlog_out=reading)
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
    # THE VIEWS ARE RENDERED AFTER THE ORPHAN SCAN, whose population is the ledger directory alone:
    # a view is neither a build README nor a month shard, and adding it to that scan's input would
    # have it reported as an unmanaged file on the first run that wrote one.
    verdicts = list(reading.get("verdicts") or ())
    guarded: dict = {}
    if reading.get("mode") == "builds":
        views, guarded = render_views(root, conf, reading)
        artifacts.update(views)
    return artifacts, sorted(orphans), sorted(unmanaged), verdicts, guarded


# -------------------------------------------------------------------------------------------- modes
def cmd_check(root: str, conf: dict) -> int:
    artifacts, orphans, unmanaged, verdicts, guarded = plan(root, conf)
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
    rc = 0
    if bad:
        print(f"build-index DRIFT — run: python {kit_rel()}/gen_build_index.py --write")
        for line in bad:
            print("    " + line)
        rc = 1
    # A GUARDED VIEW IS NEVER IN `bad`: it is not in `artifacts` at all, so the remedy above cannot
    # be printed against it. That is the whole point — the line it would have printed is `--write`.
    rc = print_verdicts(verdicts, guarded, conf) or rc
    if rc == 0:
        print(f"build-index: clean ({len(artifacts)} artifact(s))")
    return rc


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
    artifacts, orphans, unmanaged, verdicts, guarded = plan(root, conf, create_missing=True)
    for rel, text in sorted(artifacts.items()):
        write_text(os.path.join(root, rel), text)
    for p in orphans:
        os.remove(os.path.join(root, p))
        print(f"build-index: removed orphaned shard {p}")
    for p in unmanaged:
        print(f"build-index: WARNING unmanaged file under ledger/ left in place: {p}")
    print(f"build-index: wrote {len(artifacts)} artifact(s)")
    # A RENDER IS NOT A VERDICT (fork F1). One unparseable ask row must not leave a whole tree
    # unrendered — that is the shape this file's own docstring forbids — so every verdict is
    # PRINTED here and the refusal belongs to `--check`. The data-loss guard is the one exception,
    # and it earns it: the view it names is the only artifact this verb did NOT write, and exiting
    # 0 after skipping a write would read as a successful render of it.
    print_verdicts(verdicts, guarded, conf)
    return 1 if guarded else 0


# ----------------------------------------------------------------------------------------- selftest
# ----------------------------------------------------------------------------- the print modes
#: The tokens `--status` accepts. The seven the fold can derive, plus the placeholder it renders
#: when a hold target names nothing — a reader asking "what is UNRESOLVED right now" is asking the
#: same question as one asking what is BLOCKED, and leaving it out would make that question
#: unanswerable by the one mode built to answer it.
ASK_STATUS_TOKENS = STATUS_TOKENS + (backlog.UNRESOLVED,)
ASK_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*-[A-Za-z0-9]+-\d+$")
ASK_USAGE = ("usage: gen_build_index.py --asks [FAMILY|ID] [--all] [--status <token>] "
             "[--build <slug>] [--json|--tsv] [--ready [IDLIST]] [--target <slug>] "
             "[--live-builds <slug>…] [--at <rev>] [--probe <id>]")
#: The options that take a LIST of bare words rather than one value. Their list ends at the next
#: `--option` or at the end of argv, and NOT at the first token starting with `-`: an IDLIST
#: continuation is spelled `-4`, so a one-dash stop would silently truncate every mandate that
#: used the continuation form — the fix-F2 narrowing, reintroduced by the argument parser.
ASK_LIST_OPTIONS = {"--ready": "ready", "--live-builds": "live_builds"}
ASK_VALUE_OPTIONS = {"--status": "status", "--build": "build", "--target": "target",
                     "--at": "at", "--probe": "probe"}


def read_asks_args(argv: list) -> dict:
    """`--asks`'s own argument parse. One positional, ten options, and no silent tolerance.

    The positional is `pick` and NOT `target`: `--target` is TOOL-dDerivedDocket-15's option naming
    the build folder R2 admits a live closing spec from, and one key answering both questions is
    how a filter silently becomes a grading input.
    """
    out = {"pick": "", "all": False, "status": "", "build": "", "json": False, "tsv": False,
           "ready": None, "target": "", "live_builds": None, "at": "", "probe": ""}
    rest = list(argv)
    while rest:
        token = rest.pop(0)
        if token in ("--all", "--json", "--tsv"):
            out[token[2:]] = True
        elif token in ASK_VALUE_OPTIONS:
            if not rest:
                raise Problem(f"{token} takes a value. {ASK_USAGE}")
            out[ASK_VALUE_OPTIONS[token]] = rest.pop(0)
        elif token in ASK_LIST_OPTIONS:
            got: list = []
            while rest and not rest[0].startswith("--"):
                got.append(rest.pop(0))
            # AN EMPTY LIST IS ACCEPTED, not a usage error (S6). `--ready` with no id sets an EMPTY
            # mandate and an EMPTY examined population, which is a legitimate answer — nothing was
            # mandated, so nothing is graded — and refusing it would make a caller that assembles
            # its list from a filter have to special-case the day the filter matches nothing.
            out[ASK_LIST_OPTIONS[token]] = got
        elif token.startswith("--"):
            raise Problem(f"--asks: unknown option {token}. {ASK_USAGE}")
        elif out["pick"]:
            raise Problem(f"--asks takes at most one FAMILY or ID, and was given `{out['pick']}` "
                          f"and `{token}`. {ASK_USAGE}")
        else:
            out["pick"] = token
    if out["json"] and out["tsv"]:
        raise Problem("--asks: --json and --tsv are two projections of one answer, and a run that "
                      "printed both would put a JSON object in a consumer's TAB stream. "
                      f"{ASK_USAGE}")
    return out


def build_ask_row(ask, fold, evidence: dict) -> dict:
    """One ask's PINNED projection. These field names are a contract, not a convenience.

    The switch-over's drift signals read `closing`, `declining`, `live_specs` and `sev` by name, and
    the agent carriers read the rest. Renaming one is a breaking change to a consumer this file
    cannot see, which is why they are listed in the spec and asserted by an arm.
    """
    return {
        "id": ask.id,
        "home": ask.slug,
        "file": ask.path,
        "line": ask.line,
        "filed": ask.filed,
        "unit": bool(ask.unit),
        "status": fold.statuses.get(ask.id, backlog.UNRESOLVED),
        "decided_by": fold.decided.get(ask.id, ""),
        "sev": fold.severities.get(ask.id, backlog.UNLABELLED),
        "closing": list(evidence.get("closing", ())),
        "declining": list(evidence.get("declining", ())),
        "holds": list(evidence.get("holds", ())),
        "live_specs": list(evidence.get("live_specs", ())),
    }


def render_asks_table(picked: list, excerpt: int) -> str:
    """The human form. Header and separator ALWAYS, so an empty result is a visible empty set."""
    out = ["| Ask | Status | Sev | Decided by | Filed | Home | Summary |",
           "|---|---|---|---|---|---|---|"]
    for ask, row in picked:
        out.append(f"| {row['id']} | {row['status']} | {row['sev']} | "
                   f"{row['decided_by'] or backlog.VIEW_NONE} | {row['filed']} | {row['home']} | "
                   f"{backlog.render_summary_cell(ask.text, excerpt)} |")
    return "\n".join(out)


def render_ask_detail(ask, row: dict, clauses: dict = None) -> str:
    """One ask, and EVERYTHING that decided it — which is what the view header promises.

    A terminal ask leaves every view, so this is the only place its story is told; printing the
    status without the evidence would answer "what" and leave "why" to a grep of four files.

    THE MERGED CLAUSES PRINT ONE LINE PER VALUE, not one per label (TOOL-dDerivedDocket-15). A
    label carrying two values — the ask row's and a SCOPE row's — is the normal case once a
    non-filer may scope somebody else's ask, and folding them to one line would be the one-value
    field recording a mixed outcome that this kit already keeps a gotcha about.
    """
    out = [f"{row['id']} · {row['status']} · sev {row['sev']} · filed {row['filed']} · "
           f"home {row['home']} · {row['file']}:{row['line']}"]
    for label, value in (("decided by", row["decided_by"]),
                         ("closing", " ".join(row["closing"])),
                         ("declining", " ".join(row["declining"])),
                         ("held on", " ".join(row["holds"])),
                         ("live specs", " ".join(row["live_specs"]))):
        out.append(f"  {label:<11} {value or backlog.VIEW_NONE}")
    for label in backlog.CLAUSE_LABELS:
        for value in (clauses or {}).get(label, ()):
            out.append(f"  {label:<11} {value}")
    out.append(f"  {'text':<11} {ask.text}")
    return "\n".join(out)


# ------------------------------------------------ TOOL-dDerivedDocket-15 — the ask ENVELOPE
# An unattended run pointed at asks can only execute one that says what was seen, what done looks
# like and where the work lives. The grammar and the predicate are `backlog.py`'s, because they are
# pure text and a pure fold; everything HERE is the part that touches a tree: which paths exist,
# which blobs a rev holds, which command a declaration admits, and what gets written.
IDLIST_ELISIONS = ("...", "…")
#: A bare `-N` or `-N..M` continuation: the family and slug of the id before it, a new sequence.
IDLIST_CONT_RE = re.compile(r"^-(?P<lo>\d+)(?:\.\.(?P<hi>\d+))?$")

#: Every empty field of the machine projection carries THIS, never nothing. The kit reads TAB
#: records with a TAB-separated `read`, where a RUN of tabs collapses, so an empty field would
#: shift every field after it left and a consumer parsing by position would misread a row that
#: still carried the right number of separators.
TSV_NONE = "-"
ASK_TSV_HEAD = "ask"
ASK_TSV_COUNT = 11
ASK_TSV_EXAMINED = "examined"
READY_COLUMNS = ("Ask", "Status", "Sev", "Ready", "Missing", "Holds", "Grant", "Closers")


def read_idlist(tokens, alt: str) -> list:
    """The IDLIST grammar of design §19.2, read ALL OR NOTHING (fix F2).

    A token that fails REFUSES THE WHOLE LIST rather than being dropped, because a re-typed prompt
    once silently narrowed six asks to two and the four it lost were simply never built. An elision
    is refused BY NAME for the same reason: `…` is the one token a reader is sure of and a parser
    cannot be, so it must never expand to "whatever the tool guessed".

    Duplicates collapse, order is preserved, and the answer is the list a caller can iterate.
    """
    ids: list = []
    bad: list = []
    stem = ""
    for token in tokens:
        # AN ELISION IS MATCHED INSIDE A TOKEN, not only as one. `EXMP-aFoo-3...5` is the shape a
        # re-typed prompt actually produced, and a whole-token test reported it as "not an id" —
        # true, and useless to the reader, who then has to work out that the third dot is the
        # whole story. The two-dot RANGE is unaffected, because `..` does not contain `...`.
        hit = [e for e in IDLIST_ELISIONS if e in token]
        if hit:
            bad.append(f"`{token}` (carries `{hit[0]}`, and an elision names no id; write "
                       f"every one, or a `lo..hi` range)")
            continue
        cont = IDLIST_CONT_RE.match(token)
        if cont:
            if not stem:
                bad.append(f"`{token}` (a continuation with no id before it to continue)")
                continue
            lo = int(cont.group("lo"))
            hi = int(cont.group("hi") or cont.group("lo"))
            if hi < lo:
                bad.append(f"`{token}` (a range that counts backwards)")
                continue
            ids += [f"{stem}-{n}" for n in range(lo, hi + 1)]
            continue
        got, wrong = _expand_ids(token, alt)
        if wrong or not got:
            bad.append(f"`{token}` (neither an id, an id range, nor a `-N` continuation)")
            continue
        ids += got
        stem = got[-1].rsplit("-", 1)[0]
    if bad:
        raise Problem("the id list is read ALL or NOTHING, because a dropped token is a mandate "
                      "that silently narrowed: " + "; ".join(bad))
    return list(dict.fromkeys(ids))


def read_tree_paths(root: str, rev: str) -> list:
    """Every path in ONE pinned tree. `git ls-tree`, never `ls-files`, which reads the INDEX."""
    return [p for p in run("git", "ls-tree", "-r", "--name-only", rev, cwd=root).split("\n") if p]


def read_blobs_at_rev(root: str, rev: str, paths: list) -> dict:
    """`path -> text`, or `None` per path the rev does not hold, in ONE `git cat-file --batch`.

    ONE PROCESS FOR THE WHOLE READ. A corpus is a few hundred blobs, and this repo's own memory
    note prices process creation as the dominant cost of a suite on the node that measured it.

    BYTES, and deliberately not through `run()`. That helper decodes with the locale encoding and
    universal-newlines the result; this reader must decode utf-8 and fold CRLF alone, exactly as
    `read_text` does, or a pinned read and a working-tree read of one file would disagree about a
    lone CR. It is the same split `read_conf_at_rev` records, for the same reason.
    """
    if not paths:
        return {}
    stdin = "".join(f"{rev}:{p}\n" for p in paths).encode("utf-8")
    done = subprocess.run(("git", "cat-file", "--batch"), cwd=root, input=stdin,
                          capture_output=True, check=True, env=_build_git_env())
    out: dict = {}
    data, at = done.stdout, 0
    for path in paths:
        end = data.find(b"\n", at)
        if end < 0:
            out[path] = None
            continue
        header = data[at:end].decode("utf-8", "replace").split()
        at = end + 1
        # `<sha> blob <size>`, or `<name> missing` with no body. A TREE under a path this walk
        # selected is not a file either, so it is `None` for the same reason a missing object is.
        if len(header) < 3 or header[1] != "blob":
            out[path] = None
            continue
        size = int(header[2])
        try:
            out[path] = data[at:at + size].decode("utf-8").replace("\r\n", "\n")
        except UnicodeDecodeError:
            out[path] = None
        at += size + 1
    return out


def build_path_probe(paths):
    """`path -> bool` over a tracked path list, with every DIRECTORY prefix admitted too.

    Directories are admitted because a POINTER legitimately names a folder — a kit's own directory
    is where a reader is often being sent — and R4 asks whether the tree HOLDS the thing pointed
    at, not whether it is a regular file.

    The prefixes are precomputed rather than tested with a per-call prefix scan: the walk happens
    once per RUN and the probe is called several times per ask, so the scan would otherwise be
    quadratic in a corpus this mode already reads every blob of.
    """
    have = set(paths)
    dirs: set = set()
    for path in have:
        parts = path.split("/")
        for i in range(1, len(parts)):
            dirs.add("/".join(parts[:i]))
    return lambda path: bool(path) and (path in have or path in dirs)


def read_backlog_at_rev(root: str, rev: str, conf: dict) -> dict:
    """`read_backlog`'s reading, over a PINNED tree. The same keys, plus `tracked`.

    **WHAT THIS DOES NOT READ**, because a structural reader reads as a semantic one to everybody
    who did not write it. It reads the BACKLOG files and the spec headers at `<rev>` and nothing
    else: no build README, so the build-status map is empty and V10 — the closeout join over
    FINISHED builds — cannot fire here. That is right for a print mode and wrong for a merge bar,
    which is why this is not the function `--check` calls. The conf is the CALLER's, and a caller
    that means a pinned one reads it with `read_conf_at_rev`.
    """
    m = conf["MEMORY_ROOT"]
    bconf = _read_backlog_conf(conf)
    tracked = read_tree_paths(root, rev)
    families = tuple(sorted({pair.split(":")[1] for pair in conf["FAMILIES"].split()
                             if ":" in pair}))
    out = {"mode": bconf.mode, "conf": bconf, "corpus": None, "fold": None, "families": families,
           "excerpt": backlog.EXCERPT_DEFAULT, "verdicts": [], "line": "", "tracked": tracked}
    if bconf.mode != "builds":
        out["corpus"] = backlog.build_corpus([])
        out["fold"] = backlog.derive_statuses(out["corpus"])
        out["line"] = (f"build-index: backlog layout is `shards` at {rev} — no ask is filed per "
                       f"build there, so every id in a mandate grades `no` on R1")
        return out
    out["excerpt"] = _read_excerpt(conf)
    grammar = backlog.build_grammar(families)
    rows = sorted(p for p in tracked if p.startswith(f"{m}/builds/")
                  and p.endswith("/BACKLOG.md") and p.count("/") == 3)
    spec_sel = re.compile(r"^" + re.escape(m) + r"/builds/[^/]+/spec/.*\.md$")
    specs = sorted(p for p in tracked if spec_sel.match(p))
    blobs = read_blobs_at_rev(root, rev, rows + specs)
    files, verdicts = [], []
    for rel in rows:
        text = blobs.get(rel)
        if text is None:
            verdicts.append(backlog.Verdict(2, f"{rel}: unreadable at {rev}", (rel,)))
            continue
        files.append(backlog.parse_file(rel, text, grammar))
    index: dict = {}
    for rel in specs:
        text = blobs.get(rel)
        if text is None:
            continue
        try:
            unit = parse_spec_text(text, rel, _id_alternation(conf))
        except Problem as exc:
            # A MALFORMED HEADER AT A PINNED REV IS NOT THIS MODE'S REFUSAL. `--check` grades the
            # working tree and owes that verdict there; a print mode asked about history must not
            # refuse to answer because a spec somebody has since repaired was once wrong.
            #
            # IT IS STILL A DEGRADATION, AND IT SAYS SO. A spec dropped here is a spec absent from
            # the index, which moves the status of every ask it closes and therefore moves R2 —
            # so a run that swallowed it would hand back a grade computed over a corpus it never
            # mentioned. The notice is on stderr, with the rest of this mode's notices.
            print(f"build-index: at {rev}, {rel} carries a header this reader refuses, so it is "
                  f"absent from the pinned spec index and any ask it closes grades without it: "
                  f"{exc}", file=sys.stderr)
            continue
        if unit:
            index[unit["id"]] = backlog.Spec(unit["id"], rel, unit["status"],
                                             tuple(unit["closes"]), tuple(unit["advances"]))
    corpus = backlog.build_corpus(files, index, {})
    fold = backlog.derive_statuses(corpus)
    verdicts += backlog.derive_verdicts(corpus, bconf)
    counts = fold.counts
    out.update(corpus=corpus, fold=fold, verdicts=verdicts,
               line=(f"build-index: backlog at {rev} — {counts['asks']} ask(s) · "
                     f"{counts['rows']} row(s) · {counts['links']} link(s) in "
                     f"{counts['files']} file(s) · {counts['live']} live · "
                     f"{len(verdicts)} verdict(s)"))
    return out


def build_grade_row(grader, deciders: dict, ask_id: str) -> dict:
    """One ask's WHOLE answer, as the values both projections print. No field is ever empty.

    The human table and the machine line are rendered from THIS dict and never computed twice: a
    reader comparing a pasted table against a parsed row is entitled to find the same answer, and
    two renderers each deriving their own is how those two stop agreeing.
    """
    rows = [a for p in grader.corpus.files for a in p.asks if a.id == ask_id]
    ready = backlog.derive_ready(grader, ask_id)
    sev = grader.fold.severities.get(ask_id, backlog.UNLABELLED)
    # THE HOME IS NEVER EMPTY. A filed ask's home is the folder it is filed in; an id nobody filed
    # still names its build in its own slug component, and printing THAT rather than a blank is
    # what lets the reader of a `no · R1` row go and look in the right place.
    home = rows[0].slug if len(rows) == 1 and rows[0].slug else (
        ask_id.split("-")[1] if ask_id.count("-") >= 2 else ask_id)
    return {
        "id": ask_id,
        "status": grader.fold.statuses.get(ask_id, backlog.UNRESOLVED),
        "decided_by": ",".join(deciders.get(ask_id, ())) or TSV_NONE,
        "home": home,
        "sev": TSV_NONE if sev == backlog.UNLABELLED else sev,
        "ready": ready.grade,
        "missing": ",".join(ready.missing) or TSV_NONE,
        "holds": ",".join(ready.holds) or TSV_NONE,
        "grant": ",".join(ready.grant) or TSV_NONE,
        "closers": ",".join(ready.closers) or TSV_NONE,
        "file": rows[0].path if len(rows) == 1 else "",
        "text": rows[0].text if rows else "",
    }


def render_grade_tsv(row: dict) -> str:
    """The eleven-field machine line. The field ORDER is the contract; see this unit's §4."""
    return "\t".join((ASK_TSV_HEAD, row["id"], row["status"], row["decided_by"], row["home"],
                      row["sev"], row["ready"], row["missing"], row["holds"], row["grant"],
                      row["closers"]))


def render_ready_table(rows: list, m: str) -> str:
    """The human form of the same data. Header and separator ALWAYS, so empty is a VISIBLE empty.

    THE FIRST CELL IS LINK-WRAPPED, and that is not decoration. The sibling kit's anchor grammar
    reads a bare-id first cell as a line DEFINING that record, so a pasted copy of such a table
    would make every ask in it a second claimant under the id-corpus check. A backtick would not
    help — the anchor pattern admits one. A markdown link does, because its bracket is outside the
    character set that pattern allows in front of the id.
    """
    out = ["| " + " | ".join(READY_COLUMNS) + " |", "|" + "---|" * len(READY_COLUMNS)]
    for row in rows:
        link = row["file"] or f"{m}/builds/{row['home']}/BACKLOG.md"
        out.append(f"| [{row['id']}]({link}) | {row['status']} | {row['sev']} | {row['ready']} "
                   f"| {row['missing']} | {row['holds']} | {row['grant']} | {row['closers']} |")
    return "\n".join(out)


def render_ready_summary(rows: list, at: str) -> str:
    """Every grade counted, and the tree the grades are about.

    The counts are not derivable by a reader who would have to count rows, and `at` is the field a
    stale paste is caught by — a table with no tree named is a claim about no particular day.
    """
    grades = [r["ready"] for r in rows]
    return (f"asks: {len(rows)} examined · {grades.count('yes')} ready · "
            f"{grades.count('legacy')} legacy · {grades.count('no')} not ready · "
            f"at {at or 'the working tree'}")


# ------------------------------------------------------------------------------- the probe runner
#: The conf key that DECLARES which commands `--probe` may execute. Blank ships everywhere,
#: including here (owner ruling D12-e): ask text is written by whoever filed the ask, so this is
#: the one place in the kit that would execute a filer's bytes, and a tree that has not thought
#: about that must not be able to do it by default.
PROBE_ALLOW_KEY = "PROBE_ALLOW"
#: Entries are separated by this and by nothing else, because an ENTRY is a sequence of argv tokens
#: separated by whitespace — the two separators cannot be the same character or a two-token entry
#: would be indistinguishable from two one-token ones.
PROBE_ENTRY_SEP = "|"
#: The bound, in seconds. A command that outlives it is KILLED and reported as never answered,
#: which is a different outcome from a failure and is printed as one: a probe that hung tells you
#: nothing about the ask, and reporting it as a red would be a claim the run cannot support.
PROBE_TIMEOUT_SECONDS = 30
#: How much of a probe's output is printed. The whole of it would land in a transcript.
PROBE_TAIL_LINES = 20
#: Refused BEFORE the command is split, never escaped. Every one of these means something to a
#: shell, this runner starts no shell, and a token carrying one is therefore either a mistake or an
#: attempt — and the two are indistinguishable from here, which is exactly why neither runs.
PROBE_METACHARS = ";|&$<>()[]{}`\\'\"*?!#~\n\r\t"


def read_probe_allow(conf: dict) -> tuple:
    """`PROBE_ALLOW` as a tuple of entries, each a tuple of argv tokens. Blank is the empty tuple."""
    raw = (conf.get(PROBE_ALLOW_KEY) or "").strip()
    return tuple(tuple(entry.split()) for entry in raw.split(PROBE_ENTRY_SEP) if entry.split())


def check_probe_command(command: str, entries: tuple) -> tuple:
    """`(argv, why)` — the command's argv when a declared entry admits it, else the refusal.

    THE MATCH IS TOKEN FOR TOKEN ON A PREFIX, never a string prefix (§8 F5). A string prefix admits
    `python3x` under an entry reading `python3`, and `tools/../x` under one reading `tools/`; both
    were the reason the string form was rejected rather than a hypothetical.

    A SINGLE-TOKEN INTERPRETER ENTRY ADMITS ARBITRARY CODE — `python3` admits `python3 -c` followed
    by anything a filer wrote. That is stated here and in the conf example rather than prevented,
    because a tree may legitimately declare one; what it may not do is declare one unknowingly.
    """
    bad = [c for c in PROBE_METACHARS if c in command]
    if bad:
        shown = " ".join(repr(c) for c in bad)
        return (), (f"the command carries {shown}, which mean something to a shell; this runner "
                    f"starts no shell, so a command carrying one is refused before it is split "
                    f"rather than escaped")
    argv = tuple(command.split())
    if not argv:
        return (), "the command is empty"
    if not entries:
        return (), (f"{PROBE_ALLOW_KEY} is blank in this tree, so no command is admitted; the key "
                    f"that would admit `{' '.join(argv)}` is {PROBE_ALLOW_KEY}")
    for entry in entries:
        if len(entry) <= len(argv) and all(a == b for a, b in zip(entry, argv)):
            return argv, ""
    declared = PROBE_ENTRY_SEP.join(" ".join(e) for e in entries)
    return (), (f"no {PROBE_ALLOW_KEY} entry matches `{' '.join(argv)}` token for token; the tree "
                f"declares: {declared}")


def run_probe(root: str, argv: tuple, timeout: int) -> tuple:
    """`(status, output, answered)` for one bounded run from the repo root, with NO shell.

    `answered` is False when the bound killed it, and the caller prints that rather than a status:
    a killed probe answered nothing, and reporting a synthesised non-zero would be a verdict the
    run did not earn.
    """
    try:
        done = subprocess.run(argv, cwd=root, capture_output=True, text=True, timeout=timeout,
                              shell=False)
    except subprocess.TimeoutExpired:
        return None, "", False
    except OSError as exc:
        return None, f"{type(exc).__name__}: {exc}", True
    return done.returncode, (done.stdout or "") + (done.stderr or ""), True


def scan_run_commands(corpus, ask_id: str) -> list:
    """`[(where, seen)]` — every merged `seen` carrying a `run`, WITH the row that wrote it.

    The merge in `backlog.derive_clauses` answers "what do the clauses say"; this walk answers
    "who said it", which is the question the ambiguity refusal has to answer. Two rows carrying a
    command is a refusal naming BOTH, because running one of them would be running a second
    writer's command for somebody else's ask and ignoring the other would be silent (§8 F7).
    """
    out = []
    for parsed in corpus.files:
        for ask in parsed.asks:
            if ask.id != ask_id:
                continue
            for value in backlog.read_clause_values(ask.clauses, "seen"):
                seen = backlog.parse_seen(value)
                if seen.command:
                    out.append((f"{ask.path}:{ask.line}", seen))
        for row in parsed.rows:
            if row.cls != "scope" or row.target != ask_id:
                continue
            for value in backlog.read_clause_values(row.extra["clauses"], "seen"):
                seen = backlog.parse_seen(value)
                if seen.command:
                    out.append((f"{row.path}:{row.line}", seen))
    return out


def cmd_probe(root: str, conf: dict, corpus, ask_id: str) -> int:
    """`--asks --probe <id>`: the ONE path in this kit that may execute a filer's bytes.

    Everything it prints goes to STDOUT, because a probe's answer IS its value; the refusals go to
    stderr with the rest of this mode's notices. It exits 0 when it ran and 2 when it refused,
    which is the shape a caller can tell apart from the probed command's own status.
    """
    found = scan_run_commands(corpus, ask_id)
    if not found:
        print(f"build-index: {ask_id} carries no `seen … run` command in its merged clauses, so "
              f"there is nothing to probe", file=sys.stderr)
        return 2
    if len(found) > 1:
        rows = "; ".join(f"{where} runs `{seen.command}`" for where, seen in found)
        print(f"build-index: {ask_id}'s merged clauses carry {len(found)} `seen … run` commands "
              f"and which one answers it has more than one answer, so nothing ran — {rows}",
              file=sys.stderr)
        return 2
    where, seen = found[0]
    argv, why = check_probe_command(seen.command, read_probe_allow(conf))
    print(f"probe {ask_id} · {where} · locator {seen.kind or 'unreadable'} {seen.path}")
    if why:
        print(f"probe {ask_id} · REFUSED · {why}")
        return 2
    status, output, answered = run_probe(root, argv, PROBE_TIMEOUT_SECONDS)
    if not answered:
        print(f"probe {ask_id} · NEVER ANSWERED · `{' '.join(argv)}` outlived the "
              f"{PROBE_TIMEOUT_SECONDS}s bound and was killed, so it says nothing about this ask")
        return 2
    print(f"probe {ask_id} · RAN · `{' '.join(argv)}` · exit {status}")
    tail = [line for line in output.split("\n") if line.strip()][-PROBE_TAIL_LINES:]
    for line in tail:
        print("    " + line)
    return 0


def cmd_asks(root: str, conf: dict, args: dict) -> int:
    """The print modes. They write no file, and stdout carries the mode's VALUE and nothing else.

    THE REDIRECT IS AROUND THE WHOLE READ, not around the two notices this file happens to print
    today. `collect()` prints a tolerated-header line and a liveness line on every run, and a JSON
    consumer handed either of them ahead of the object gets a decode error — the class the hygiene
    engine's own ON STDERR note records. Redirecting the read wholesale means a notice added to any
    callee later is on stderr by construction rather than by somebody remembering this rule. Under
    `--tsv` the same rule is what leaves stdout holding the `ask` lines and the `examined` line and
    nothing else, which is the whole reason a consumer may parse it by position.

    EXIT 0 ON A FOLD VERDICT (fork F8). The one tool built to explain a verdict must not refuse to
    run while one exists. A `collect()` REFUSAL is the opposite case and exits 1 with nothing on
    stdout: the tree could not be read, so there is no value to print and a partial one would be
    worse than none. A GRADE NEVER DECIDES THE EXIT STATUS either — an all-`no` mandate is an
    answer, printed in full, at 0; reported as a non-zero it would reach a caller's preflight as a
    producer FAILURE naming an exit status instead of as the refusal that names each id's rules.

    WHICH TREE. `--at <rev>` pins both the records and the DECLARATIONS: the conf is re-read at
    that rev through `read_conf_at_rev`, because `ASK_CUTOFF` decides a `legacy` grade and a grade
    mixing a pinned tree with evaluation-time declarations is not a function of the rev it names.
    """
    if args["status"] and args["status"] not in ASK_STATUS_TOKENS:
        print(f"build-index: --status {args['status']} is not a derived status token; the set is "
              f"{' '.join(ASK_STATUS_TOKENS)}", file=sys.stderr)
        return 2
    at = args["at"]
    reading: dict = {}
    tracked: list = []
    with contextlib.redirect_stdout(sys.stderr):
        try:
            if at:
                conf = read_conf_at_rev(root, at)
                reading = read_backlog_at_rev(root, at, conf)
                tracked = reading["tracked"]
                print(reading["line"], file=sys.stderr)
            else:
                collect(root, conf, backlog_out=reading)
                tracked = [p for p in run("git", "ls-files", cwd=root).split("\n") if p]
        except Problem as exc:
            print(f"build-index: {exc}", file=sys.stderr)
            return 1
    # AN EMPTY CORPUS RATHER THAN `None`, so every reader below is written once. Under `shards`
    # there is no per-build ask at all, and the honest answer to "is this id ready" is then `no` on
    # R1 for every id — which is what an empty corpus produces, with the layout line saying why.
    corpus = reading.get("corpus") or backlog.build_corpus([])
    fold = reading.get("fold") or backlog.derive_statuses(corpus)
    if args["probe"]:
        return cmd_probe(root, conf, corpus, args["probe"])
    pick = args["pick"]
    one = bool(pick) and bool(ASK_ID_RE.match(pick))
    if pick and not one and pick not in reading.get("families", ()):
        print(f"build-index: --asks {pick} is neither an id nor a declared family; the families "
              f"are {' '.join(reading.get('families', ()))}", file=sys.stderr)
        return 2
    evidence = backlog.derive_evidence(corpus)
    picked = []
    for ask in sorted((a for p in corpus.files for a in p.asks), key=backlog.build_ask_sort_key):
        if one and ask.id != pick:
            continue
        if pick and not one and ask.id.split("-")[0] != pick:
            continue
        if args["build"] and ask.slug != args["build"]:
            continue
        row = build_ask_row(ask, fold, evidence.get(ask.id, {}))
        # AN ID ARGUMENT IGNORES BOTH FILTERS ON LIVENESS. The header of every view tells a reader
        # that an id it does not list is terminal and that this mode says what decided it, so a
        # terminal id must answer here or that sentence is false.
        if not one and not args["all"] and row["status"] in backlog.TERMINAL:
            continue
        if args["status"] and row["status"] != args["status"]:
            continue
        picked.append((ask, row))
    if args["json"]:
        print(json.dumps({"mode": reading.get("mode", ""),
                          "examined": len(corpus.files),
                          "asks": [row for _ask, row in picked]}, indent=2, sort_keys=True))
        return 0
    # THE READY MODES. Asked for by `--tsv` or by any of the three options that only READY reads;
    # asked for by none of them, this mode is byte-identical to what the view unit shipped.
    if args["tsv"] or args["ready"] is not None or args["target"] or args["live_builds"] is not None:
        return cmd_ready(root, conf, args, reading, corpus, fold, tracked,
                         [ask.id for ask, _row in picked])
    if one:
        if not picked:
            print(f"build-index: {pick} is filed in no tracked BACKLOG.md", file=sys.stderr)
            return 0
        print(render_ask_detail(*picked[0], backlog.derive_clauses(corpus).get(pick, {})))
        return 0
    print(render_asks_table(picked, reading.get("excerpt", backlog.EXCERPT_DEFAULT)))
    return 0


def cmd_ready(root: str, conf: dict, args: dict, reading: dict, corpus, fold, tracked: list,
              filtered: list) -> int:
    """The READY grades, in one of the two projections. Writes nothing, and exits 0 on any grade.

    `--ready` SETS THE EXAMINED POPULATION to the ids its list names, and the mandate M to the same
    set (S6). Without it the population is whatever the view unit's filters picked and each ask is
    graded with M = {A}, which is the conservative reading: an ask held on something nobody
    mandated is not ready, and a single-ask query has mandated exactly one thing.
    """
    try:
        if args["ready"] is not None:
            population = read_idlist(args["ready"], _id_alternation(conf))
            mandate = frozenset(population)
        else:
            population, mandate = list(filtered), None
        grader = backlog.build_grader(corpus, fold, reading["conf"],
                                      build_path_probe(tracked),
                                      mandate=mandate or (), target=args["target"],
                                      live_builds=args["live_builds"])
    except Problem as exc:
        print(f"build-index: {exc}", file=sys.stderr)
        return 2
    except backlog.Problem as exc:
        print(f"build-index: {exc}", file=sys.stderr)
        return 2
    deciders = backlog.derive_deciders(corpus, fold, grader.evidence)
    rows = [build_grade_row(grader if mandate is not None
                            else grader._replace(mandate=frozenset([ask_id])),
                            deciders, ask_id)
            for ask_id in population]
    if args["tsv"]:
        for row in rows:
            print(render_grade_tsv(row))
        print(f"{ASK_TSV_EXAMINED}\t{len(rows)}")
        return 0
    print(render_ready_table(rows, conf["MEMORY_ROOT"]))
    print(render_ready_summary(rows, args["at"]))
    return 0


# ------------------------------------------------------------------------------- the scaffold
NEW_BUILD_USAGE = "usage: gen_build_index.py --new-build <slug> --asks <IDLIST>"
#: The front-matter key naming what a run may execute without asking anybody. `slug` says: the
#: authority is this build folder, which an OWNER committed. The scaffold writes that value and no
#: other, because owner ruling D12-a dropped the zero-commit start it was the alternative to.
AUTHORIZED_BY_SLUG = "slug"
#: The one-line key the mandate lives on. ONE PHYSICAL LINE, ranges collapsed, because a list whose
#: rows each led with an id would make the new build a second claimant for every ask it names.
ASKS_KEY = "asks"


def read_new_build_args(argv: list) -> dict:
    """`--new-build`'s own parse: one positional slug and one `--asks` list."""
    out = {"slug": "", "asks": []}
    rest = list(argv)
    if rest and not rest[0].startswith("--"):
        out["slug"] = rest.pop(0)
    while rest:
        token = rest.pop(0)
        if token == "--asks":
            while rest and not rest[0].startswith("--"):
                out["asks"].append(rest.pop(0))
        else:
            raise Problem(f"--new-build: unknown option {token}. {NEW_BUILD_USAGE}")
    if not out["slug"]:
        raise Problem(f"--new-build takes a slug. {NEW_BUILD_USAGE}")
    if not out["asks"]:
        raise Problem(f"--new-build takes the asks it is opened for; a build answering no ask is "
                      f"a folder. {NEW_BUILD_USAGE}")
    return out


def read_discipline_map(conf: dict) -> dict:
    """`family -> discipline`, from the declared `FAMILIES` pairs and from nothing else."""
    return {p.split(":", 1)[1]: p.split(":", 1)[0]
            for p in conf.get("FAMILIES", "").split() if ":" in p}


def read_git_lines(root: str, *argv: str) -> list:
    """A git command's lines, tolerating the exit 1 that MEANS "no match" for the search verbs.

    A no-match `git grep` exits non-zero and a caller chaining on it reads a PASSING zero-count
    probe as a failure — the class this repo keeps a rule about. Anything above 1 is still a real
    failure and raises, because "the command is broken" and "nothing matched" must not be one
    answer.
    """
    done = subprocess.run(("git",) + argv, cwd=root, capture_output=True, text=True,
                          env=_build_git_env())
    if done.returncode > 1:
        raise Problem(f"git {' '.join(argv)} failed ({done.returncode}): "
                      f"{(done.stderr or '').strip()[:200]}")
    return [line for line in done.stdout.split("\n") if line]


def check_slug_claimed(root: str, conf: dict, slug: str) -> str:
    """Why this slug is already taken, or "" when three probes all find nothing.

    **WHAT THIS DOES NOT CHECK**, stated because a structural reader reads it as a semantic one. It
    is not a content grep of every blob in history: that costs a full-tree grep per commit, and a
    scaffold nobody can afford to run is a scaffold that gets bypassed. The three probes are the
    ones that are cheap AND decisive for a BUILD slug — has any commit ever touched that build
    folder, does any tracked file name the token today, and does any commit message name it. A slug
    that slipped past all three is one that was never a build, never landed and was never
    committed about, which is the residual §2's grep-then-re-roll rule already lives with.
    """
    m = conf["MEMORY_ROOT"]
    ever = read_git_lines(root, "rev-list", "--all", "--max-count=1", "--",
                          f"{m}/builds/{slug}")
    if ever:
        return (f"a commit ({ever[0][:12]}) has already touched {m}/builds/{slug}/, so that folder "
                f"has existed on some ref and its ids are already minted")
    named = read_git_lines(root, "grep", "-I", "-l", "--fixed-strings", "-e", slug, "--", ".")
    if named:
        return (f"{len(named)} tracked file(s) already name `{slug}`, the first being {named[0]}; "
                f"a slug is minted ONCE and re-using one makes two records contest each other")
    logged = read_git_lines(root, "log", "--all", "--max-count=1", "--format=%H",
                            "--fixed-strings", f"--grep={slug}")
    if logged:
        return (f"a commit message ({logged[0][:12]}) already names `{slug}`, so a session has "
                f"already minted it even if nothing it wrote survives in the tree")
    return ""


def render_new_build_readme(slug: str, conf: dict, ids: list, opened: str, at: str) -> str:
    """The scaffolded README: front matter, a title, five GENERATED slot bodies, and the pairs.

    NO AUTHORED PROSE ANYWHERE. Every line below is derived from the mandate, the conf and the
    tree it was read at, so the file an owner lands says nothing a later reader has to verify by
    hand — and the five canonical slots are filled rather than left empty, because three of them
    may not be empty and a scaffold that produced a README the bar refuses is not a scaffold.

    THE BODIES WRAP, through the generator's own id wrapper. A slot body naming one id per mandated
    ask crosses the hygiene engine's per-line build-README entry cap at about a dozen ids, and the
    remedy is never raising that cap: the population grows with every ask a mandate carries, so a
    raise buys one build and reds the next.

    THE PER-SLOT BYTE BUDGET IS A REAL BOUND ON A MANDATE'S SIZE, and it is stated rather than
    discovered. Only the first slot names every id, so only it grows with the mandate; a mandate
    large enough to pass that slot's declared ceiling REDS the budget leg by name, which is the
    outcome a scaffold should have — not a README nobody may land.
    """
    families = sorted({i.split("-")[0] for i in ids})
    disciplines = read_discipline_map(conf)
    streams = sorted({disciplines[f] for f in families if f in disciplines})
    head = [
        "---",
        f"slug: {slug}",
        f"node: {slug[0]}",
        f"opened: {opened}",
        f"streams: {'+'.join(streams)}",
        f"roster: {'+'.join(families)}",
        "ids:",
        "status: OPEN",
        f"authorized-by: {AUTHORIZED_BY_SLUG}",
        f"{ASKS_KEY}: {_render_id_ranges(ids)}",
        "---",
        "",
        f"# {slug} — the {len(ids)} filed ask(s) this build carries",
        "",
    ]
    body = [SLOT_CANON[0][0]]
    body += _render_wrapped_ids(
        f"Read at {at or 'the working tree'}, each ask below is filed and live in the build that "
        f"raised it, and no build's roster claims it. This build is the one that answers them:",
        ids)
    body += [
        "",
        SLOT_CANON[1][0],
        "- Every ask named above has ONE build answering it, so no second build claims one.",
        "- What done means for each is read off its own clauses and is never re-decided here.",
        "",
        SLOT_CANON[2][0],
        "- Each ask stays live in its home build with nothing carrying it to done.",
        "- The next run pointed at this mandate grades it and stops, because no build claims it.",
        "",
        SLOT_CANON[3][0],
        f"- Scaffolded from the `{ASKS_KEY}:` key above; the owner's commit of this folder IS the "
        f"authorization a run asserts.",
        "- This README carries no grant key, so it grants nothing that a spec does not.",
        "",
        SLOT_CANON[4][0],
        "",
        PLAN_OPEN,
        PLAN_CLOSE,
        "",
        MARK_OPEN,
        MARK_CLOSE,
    ]
    return "\n".join(head + body) + "\n"


def add_contract_row(root: str, conf: dict, rel: str) -> None:
    """Append `rel` to the registry as a BOUND row. The exempt list and its pin are NOT touched.

    Bound and not exempt, because an exemption is not coverage and a brand-new README has no
    history to be grandfathered for — it is written by this very function, to the canon's shape.
    """
    path = os.path.join(root, conf["MEMORY_ROOT"], CONTRACT_REGISTRY)
    text = read_text(path)
    if any(line.strip() == rel for line in text.split("\n")):
        return
    write_text(path, text.rstrip("\n") + "\n" + rel + "\n")


def cmd_new_build(root: str, conf: dict, args: dict) -> int:
    """Owner ruling D12-a: an owner's id list becomes a build README the OWNER lands.

    THE READINESS TABLE PRINTS BEFORE ANYTHING IS WRITTEN, and a mandate whose every id grades
    `no` stops there. That ordering is the whole ergonomics of the command: a refusal that printed
    nothing would send the owner to a second command to find out why, and a write that happened
    first would leave a folder behind after a refusal.

    IT STAGES THE TWO FILES IT WROTE, and then renders. It has to: `collect()` reads `git
    ls-files`, so an UNTRACKED README is invisible to the render and the generated regions this
    command promises would never be filled. The staging is announced, the commit is still the
    owner's, and nothing else in the index is touched.
    """
    m = conf["MEMORY_ROOT"]
    slug = args["slug"]
    if not backlog.SLUG_RE.match(slug) or not (slug[0].isalpha() and slug[0].islower()):
        raise Problem(f"`{slug}` is not a build slug: a slug is the node's own lower-case tag "
                      f"followed by a CamelCase adjective-noun, letters and digits only")
    ids = read_idlist(args["asks"], _id_alternation(conf))
    ids.sort(key=lambda i: (i.split("-")[1], i.split("-")[0], int(i.rsplit("-", 1)[1])))
    claimed = check_slug_claimed(root, conf, slug)
    if claimed:
        raise Problem(f"--new-build {slug}: {claimed}")
    reading: dict = {}
    collect(root, conf, backlog_out=reading)
    corpus = reading.get("corpus") or backlog.build_corpus([])
    fold = reading.get("fold") or backlog.derive_statuses(corpus)
    tracked = [p for p in run("git", "ls-files", cwd=root).split("\n") if p]
    grader = backlog.build_grader(corpus, fold, reading["conf"], build_path_probe(tracked),
                                  mandate=ids, target=slug, live_builds=None)
    deciders = backlog.derive_deciders(corpus, fold, grader.evidence)
    rows = [build_grade_row(grader, deciders, i) for i in ids]
    print(render_ready_table(rows, m))
    print(render_ready_summary(rows, ""))
    filed = {a.id for p in corpus.files for a in p.asks}
    unfiled = [i for i in ids if i not in filed]
    if unfiled:
        raise Problem(f"--new-build {slug}: {' '.join(unfiled)} is filed by no tracked "
                      f"{m}/builds/*/BACKLOG.md, so this build would open against an ask nobody "
                      f"raised; nothing was written")
    if all(row["ready"] == "no" for row in rows):
        raise Problem(f"--new-build {slug}: every id in the mandate grades `no` — the table above "
                      f"names each one's failing rules — so there is nothing a run could execute "
                      f"unasked; nothing was written")
    rel = f"{m}/builds/{slug}/README.md"
    opened = datetime.date.today().isoformat()
    write_text(os.path.join(root, rel), render_new_build_readme(slug, conf, ids, opened, ""))
    registry = os.path.join(m, CONTRACT_REGISTRY).replace(os.sep, "/")
    add_contract_row(root, conf, rel)
    run("git", "add", "--", rel, registry, cwd=root)
    print(f"build-index: wrote {rel} and its BOUND row in {registry}, and staged both so the "
          f"render below can see them")
    return cmd_write(root, conf)


# --------------------------------------------------------------- the backlog fixture helpers
#: The fixture corpus declares FOUR families and fills TWO, so "a family with no live ask renders a
#: file" is observable at all. A declaration nothing exercises is a rule with no population.
BL_FAMILIES = ("EXMP", "OTHR", "THRD", "FRTH")

#: The ONE `<discipline>:<FAMILY>` pair a scratch fixture of this kit may declare for the EXAMPLE
#: ids this corpus writes (TOOL-dDerivedDocket-51 S1). One carrier and not two, because the pair is
#: written into a scratch conf in two fields — `DISCIPLINES` takes the half before the colon,
#: `FAMILIES` takes the row whole — and two spellings of one value is how those two fields stop
#: agreeing: a fixture would declare a family under a discipline it never added, and the generator's
#: streams refusal would hide the roster one it was built to reach.
#:
#: DELIBERATELY ABSENT from this repository's own `.memory-tree.conf`. The example family is outside
#: the declared allowlist ON PURPOSE, which is what lets a tracked spec write `EXMP-aFoo-3` in prose
#: and anchor, define and cite nothing; declaring it here would make every example id in every
#: tracked record a real one and the id-corpus checks would start counting them. The declaration is
#: local to a scratch tree by construction, because the sibling kit's `grammar_for(root)` re-reads
#: the conf AT THE ROOT it is handed.
EXAMPLE_ROW = "example:EXMP"


def _render_backlog_conf(mode: str, cutoff: str, excerpt: str) -> str:
    rows = ["MEMORY_ROOT=memory", 'DISCIPLINES="tool"',
            'FAMILIES="tool:EXMP other:OTHR third:THRD fourth:FRTH"',
            f'BACKLOG_MODE="{mode}"', f'ASK_CUTOFF="{cutoff}"']
    if excerpt != "":
        rows.append(f'BACKLOG_EXCERPT_CHARS="{excerpt}"')
    return "\n".join(rows) + "\n"


def _render_backlog_readme(slug: str) -> str:
    return ("---\nslug: " + slug + "\nnode: a\nopened: 2026-09-01\nstreams: tool\n"
            "roster: EXMP\nids: EXMP-" + slug + "-1\n---\n\n# " + slug + "\n\n"
            + MARK_OPEN + "\n" + MARK_CLOSE + "\n")


def _render_backlog_spec(spec_id: str, status: str = "SPECCED", tail: str = "") -> str:
    return (f"# {spec_id} — a unit\n\n**Status:** {status} · rev-1 · 2026-09-01 · node a · "
            f"Tier-2 · base 0123abcd{tail}\n")


def _render_backlog_file(slug: str, asks=(), rows=()) -> str:
    """A build's BACKLOG.md, always through `backlog.py`'s own renderers, so no fixture below
    spells a row by hand and drifts from the grammar the parser reads."""
    body = ([f"# {slug} — asks", "", backlog.H_ASKS] + list(asks)
            + ["", backlog.H_DISPOSITIONS] + list(rows))
    return "\n".join(body) + "\n"


def _build_backlog_fixture(tmp: str, files: dict, *, mode: str = "builds", cutoff: str = "2099-01-01",
                     excerpt: str = "") -> dict:
    """A fixture repo whose memory tree is REPLACED, not added to, on every call.

    Replaced, so no arm can inherit a file — or a rendered view — from the arm before it; and ONE
    `git init` serves every arm below, because `git ls-files` reads the INDEX and a single
    `git add -A` restages a whole tree. Thirty arms at four processes each was the alternative, on
    a node whose own memory note prices process creation as the dominant cost of a suite.
    """
    if not os.path.isdir(os.path.join(tmp, ".git")):
        run("git", "init", "-q", ".", cwd=tmp)
        run("git", "config", "user.email", "t@t.test", cwd=tmp)
        run("git", "config", "user.name", "t", cwd=tmp)
    shutil.rmtree(os.path.join(tmp, "memory"), ignore_errors=True)
    write_text(os.path.join(tmp, ".memory-tree.conf"), _render_backlog_conf(mode, cutoff, excerpt))
    write_text(os.path.join(tmp, "memory", STALE_HEADER_WAIVER), "# empty\n")
    for rel, text in files.items():
        write_text(os.path.join(tmp, rel), text)
    run("git", "add", "-A", cwd=tmp)
    return load_conf(tmp)


def _read_mode(fn, *args) -> tuple:
    """(rc, stdout) for a mode function, with `main()`'s own Problem handling reproduced.

    Reproduced rather than called, because `main()` resolves the root with `git rev-parse` in the
    PROCESS's cwd and every fixture here lives somewhere else.
    """
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            rc = fn(*args)
        except Problem as exc:
            return 1, buf.getvalue() + f"build-index: {exc}"
    return rc, buf.getvalue()


def _read_asks_run(root: str, conf: dict, argv: list) -> tuple:
    """(rc, stdout, stderr) for `--asks`. The two streams are captured SEPARATELY, which is the
    whole property under test: stdout is the value and every notice is on the other one."""
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            rc = cmd_asks(root, conf, read_asks_args(argv))
        except Problem as exc:
            print(f"build-index: {exc}", file=sys.stderr)
            rc = 2
    return rc, out.getvalue(), err.getvalue()


def _render_fixture_conf(example_family: bool = False) -> str:
    """The scratch `.memory-tree.conf` every fixture below is graded against.

    OFF is byte-identical to what this helper wrote before the keyword existed, and that is the
    whole blast-radius answer: the widening is a property of the arms that ASK for it, and every
    arm that does not is the control saying nothing else moved. Both halves of `EXAMPLE_ROW` move
    together or neither does — see that constant for why one carrier.
    """
    disc = EXAMPLE_ROW.partition(":")[0]
    return ('MEMORY_ROOT=memory\nDISCIPLINES="arch%s"\nFAMILIES="arch:ARCH%s"\n'
            % ((" " + disc, " " + EXAMPLE_ROW) if example_family else ("", "")))


def _fixture(tmp: str, *, marker=True, readme=True, status_key=None, spec_status="INPROGRESS",
             example_family=False):
    run("git", "init", "-q", ".", cwd=tmp)
    run("git", "config", "user.email", "t@t.test", cwd=tmp)
    run("git", "config", "user.name", "t", cwd=tmp)
    write_text(os.path.join(tmp, ".memory-tree.conf"), _render_fixture_conf(example_family))
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

        # TOOL-dDerivedDocket-6 — the two BACKLOG verbs, read through `backlog.py` and expanded by
        # this module's own `_expand_ids`. THE DARK ARM IS FIRST and is the one that matters here: a
        # header carrying NEITHER verb must parse exactly as it did before, or this unit moves the
        # corpus it was built not to touch.
        def _read_verbs(tail: str):
            p = os.path.join(base, "hdr.md")
            write_text(p, "# EXMP-aFoo-1 — a fixture spec\n\n"
                          "**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · "
                          "base abc12345" + tail + "\n")
            got = parse_spec(p, "EXMP|OTHR")
            return f"closes={got['closes']} advances={got['advances']}"

        arm("a header carrying NEITHER verb parses with both lists empty", "closes=[] advances=[]",
            lambda: _read_verbs(" · streams tooling"))
        arm("a `closes` RANGE expands at parse time", "closes=['EXMP-aFoo-2', 'EXMP-aFoo-3', "
                                                     "'EXMP-aFoo-4']",
            lambda: _read_verbs(" · closes EXMP-aFoo-2..4"))
        arm("`advances` carries its own list", "advances=['EXMP-cBaz-3']",
            lambda: _read_verbs(" · closes EXMP-aFoo-2..4 · advances EXMP-cBaz-3"))
        arm("a malformed value REFUSES naming the file", "hdr.md: status header carries "
                                                         "`closes 2x`",
            lambda: _read_verbs(" · closes 2x"))
        arm("a SECOND `closes` REFUSES naming the file", "hdr.md: status header carries the "
                                                         "`closes` verb 2 times",
            lambda: _read_verbs(" · closes EXMP-aFoo-2 · closes EXMP-aFoo-3"))
        arm("one id under BOTH verbs REFUSES naming the file",
            "hdr.md: status header names EXMP-aFoo-2 under BOTH",
            lambda: _read_verbs(" · closes EXMP-aFoo-2 · advances EXMP-aFoo-2"))
        arm("a `closes` with no value REFUSES", "carries `closes` with no value",
            lambda: _read_verbs(" · closes · streams tooling"))

        # ------------------------------------------- TOOL-dDerivedDocket-7 — the family view
        # ONE fixture repo for every arm below. `_build_backlog_fixture` wipes and restages its memory
        # tree per call, so the arms are order-independent even though the `.git` is shared.
        bt = os.path.join(base, "backlogview"); os.makedirs(bt)
        ask2 = backlog.render_ask_row("EXMP-aFoo-2", "2026-09-01", "the second ask")
        ask10 = backlog.render_ask_row("EXMP-aFoo-10", "2026-09-01", "the tenth ask")
        ask3 = backlog.render_ask_row("EXMP-aFoo-3", "2026-09-02", "the terminal ask")
        wide = backlog.render_ask_row(
            "EXMP-aFoo-4", "2026-09-03",
            "a | pipe, a `deep/path/to/a/file.py` token and a [linked thing](../x.md) followed by "
            "enough prose to run past the excerpt cap with room to spare")
        closed3 = backlog.render_status_row("CLOSED", "EXMP-aFoo-3", "done", value="abc1234")
        spec_rel = "memory/builds/aFoo/spec/2026-09-01-spec-aFoo-1.md"
        foo_rel = "memory/builds/aFoo/BACKLOG.md"
        CORE = {
            "memory/builds/aFoo/README.md": _render_backlog_readme("aFoo"),
            spec_rel: _render_backlog_spec("EXMP-aFoo-1"),
            foo_rel: _render_backlog_file("aFoo", [ask2, ask10, ask3, wide], [closed3]),
            "memory/builds/aBar/README.md": _render_backlog_readme("aBar"),
            "memory/builds/aBar/spec/2026-09-01-spec-aBar-1.md": _render_backlog_spec("EXMP-aBar-1"),
            "memory/builds/aBar/BACKLOG.md": _render_backlog_file(
                "aBar", [backlog.render_ask_row("EXMP-aBar-5", "2026-09-01", "a bar ask")]),
            # THE FILING HOME: one tracked file, no README, and not a build.
            "memory/builds/aHome/BACKLOG.md": _render_backlog_file(
                "aHome", [backlog.render_ask_row("OTHR-aHome-1", "2026-09-01", "a home ask")]),
        }
        NOHOME = {k: v for k, v in CORE.items() if "/aHome/" not in k}

        # AC1 — one view per declared family, and the empty ones say so.
        conf_b = _build_backlog_fixture(bt, CORE)
        arts = plan(bt, conf_b)[0]
        arm("builds mode renders one view per DECLARED family",
            "['memory/backlog/EXMP.md', 'memory/backlog/FRTH.md', 'memory/backlog/OTHR.md', "
            "'memory/backlog/THRD.md']",
            lambda: str(sorted(k for k in arts if k.startswith("memory/backlog/"))))
        arm("a family with no live ask renders the EXPLICIT empty case, not an absent file",
            "*No live ask.*", lambda: arts["memory/backlog/THRD.md"])
        arm("every live ask appears exactly ONCE across the rendered views", "1 1 1 1 1",
            lambda: " ".join(str(sum(v.count(f"[{i}]") for k, v in arts.items()
                                     if k.startswith("memory/backlog/")))
                             for i in ("EXMP-aFoo-2", "EXMP-aFoo-4", "EXMP-aFoo-10",
                                       "EXMP-aBar-5", "OTHR-aHome-1")))

        # AC18 — the sort, the terminal exclusion and the summary cell, byte for byte.
        view = arts["memory/backlog/EXMP.md"]
        arm("the view sorts `-2` before `-10`, by NUMBER and not as a string", "True",
            lambda: str(view.index("[EXMP-aFoo-2]") < view.index("[EXMP-aFoo-10]")))
        arm("a TERMINAL ask is not listed, which is what the header promises", "False",
            lambda: str("[EXMP-aFoo-3]" in view))
        arm("the summary cell is reduced and cut at a space",
            "| a / pipe, a deep/path/to/a/file.py token and a linked thing followed by… |",
            lambda: [x for x in view.split("\n") if "EXMP-aFoo-4" in x][0])

        # AC2 — the anchor property, against the REAL grammar, with its own control.
        _anchor_at, _real_g, _why = backlog._resolve_anchor_at()
        if _anchor_at is None:
            print(f"arm SKIP  the view's anchor arms did not run — {_why}")
            fails.append("the anchor arms were SKIPPED, so the anchor property is unobserved")
        else:
            import extract as _anchor_kit  # noqa: PLC0415 — deferred exactly as backlog.py's is
            # THE GRAMMAR IS BOUND TO THE FIXTURE, not to this repo. Bound to this repo it would
            # recognise none of the fixture's families, return nothing for every line, and pass by
            # finding nothing — the empty-classification shape this kit has measured twice.
            _g = _anchor_kit.grammar_for(bt)
            _view_lines = [x for k, v in arts.items() if k.startswith("memory/backlog/")
                           for x in v.split("\n")]
            arm("no line of any rendered view ANCHORS an id", "[]",
                lambda: str([x for x in _view_lines if _anchor_at(x, _g)]))
            arm("the same grammar DOES anchor a bare-id first cell — the control", "EXMP-aFoo-2",
                lambda: str(_anchor_at("| EXMP-aFoo-2 | OPEN | — | — | 2026-09-01 | x |", _g)))
            arm("no view line opens with a list marker", "[]",
                lambda: str([x for x in _view_lines if x.lstrip().startswith(("- ", "* "))]))

        # AC3 — one recipe constant, rendered into the header with the CALLER's prefix.
        _synth = "<!-- generated by KIT/HERE/gen_build_index.py --write — do not hand-edit -->"
        _probe = backlog.render_family_view("EXMP", (), backlog.Fold({}, {}, {}, {}), "memory",
                                            "KIT/HERE", _synth)
        arm("the view header quotes the recipe constant line for line", "True",
            lambda: str(all(("> " + line) in _probe.split("\n")
                            for line in backlog.render_relocation_recipe("KIT/HERE", "memory"))))
        arm("the view header spells no kit literal of its own", "False",
            lambda: str("tools/memory-tree/" in _probe))
        arm("an empty kit prefix REFUSES rather than rendering a command that cannot run",
            "empty derivation", lambda: backlog.render_relocation_recipe("", "memory"))
        arm("the view predicate's header SHAPE matches this install's own GEN_HEADER", "True",
            lambda: str(bool(backlog.VIEW_HEADER_RE.match(GEN_HEADER))))

        # AC4 and AC15 — every code `backlog.py` EXPORTS, staged one at a time. The loop iterates
        # that tuple rather than a list typed here, so a code added there with no reporting arm
        # reds this leg instead of disappearing from a check that still looks green.
        def _build_code_tree(code):
            files, cutoff = dict(CORE), "2099-01-01"
            if code == 1:
                files[foo_rel] = _render_backlog_file("aFoo", [backlog.render_ask_row(
                    "EXMP-aBar-7", "2026-09-01", "filed in the wrong folder")])
            elif code == 2:
                files[foo_rel] = _render_backlog_file("aFoo", [ask2, "- matches no declared row shape"])
            elif code == 3:
                files[foo_rel] = _render_backlog_file("aFoo", [ask2, ask2])
            elif code == 4:
                files[foo_rel] = _render_backlog_file("aFoo", [ask2], [
                    backlog.render_status_row("KEEP", "EXMP-aFoo-2", "one"),
                    backlog.render_status_row("KEEP", "EXMP-aFoo-2", "and another")])
            elif code == 5:
                files[foo_rel] = _render_backlog_file("aFoo", [ask2],
                                               ["- SPECCED · EXMP-aFoo-2 · a derived token"])
            elif code == 6:
                files[foo_rel] = _render_backlog_file("aFoo", [ask2], [backlog.render_status_row(
                    "BLOCKED", "EXMP-aFoo-2", "on itself", value="EXMP-aFoo-2")])
            elif code == 7:
                files[foo_rel] = _render_backlog_file("aFoo", [ask2], [backlog.render_status_row(
                    "KEEP", "EXMP-aFoo-9", "nobody filed it")])
            elif code == 8:
                files[foo_rel] = _render_backlog_file("aFoo", [ask2], [backlog.render_status_row(
                    "CLOSED", "EXMP-aFoo-2", "by nothing", value="EXMP-aFoo-88")])
            elif code == 9:
                cutoff = "2026-01-01"
                files[foo_rel] = _render_backlog_file(
                    "aFoo", [backlog.render_ask_row("EXMP-aFoo-1", "2026-09-01", "a spec H1 too")],
                    [backlog.render_sev_row("EXMP-aFoo-1", "LOW", "graded")])
            elif code == 10:
                files[spec_rel] = _render_backlog_spec("EXMP-aFoo-1", "CLOSED")
                files[foo_rel] = _render_backlog_file("aFoo", [ask2])
            elif code == 11:
                files[foo_rel] = _render_backlog_file("aFoo", [ask2], [backlog.render_status_row(
                    "REOPEN", "EXMP-aFoo-2", "of nothing that closes it", value="EXMP-aFoo-1")])
            elif code == 12:
                cutoff = "2026-01-01"
                files[foo_rel] = _render_backlog_file("aFoo", [backlog.render_ask_row(
                    "EXMP-aFoo-2", "2026-09-01", "no severity row anywhere")])
            elif code == 13:
                # A `seen` pinning a LINE and no commit — fix F6's own subject, and the one V13
                # case that needs no second row to stage.
                files[foo_rel] = _render_backlog_file("aFoo", [backlog.render_ask_row(
                    "EXMP-aFoo-2", "2026-09-01", "the second ask",
                    clauses=(("seen", "`tools/x.py`:23"),))])
            elif code == 14:
                cutoff = "2026-01-01"
                files[foo_rel] = _render_backlog_file(
                    "aFoo", [ask2], [backlog.render_sev_row("EXMP-aFoo-2", "LOW", "graded")])
            elif code == 15:
                cutoff = ""
            elif code == 16:
                cutoff = "2026-9-30"
            return files, cutoff

        for _code in backlog.VERDICT_CODES:
            _files, _cut = _build_code_tree(_code)
            _c = _build_backlog_fixture(bt, _files, cutoff=_cut)
            _rc_check, _out_check = _read_mode(cmd_check, bt, _c)
            _rc_write, _out_write = _read_mode(cmd_write, bt, _c)
            # THE FAILURE MESSAGE MUST NOT CONTAIN THE WANTED STRING. It did: the first spelling
            # returned `NO ARM FOR V7 rc=1 :: ...` on a miss, which CONTAINS `V7 rc=1`, so the arm
            # passed on the exact tree it was written to refuse. Staging the break — dropping one
            # code from the report — is what found it, which is the whole reason the break is staged.
            arm(f"--check reports V{_code} with its code and exits 1", f"V{_code} rc=1",
                lambda o=_out_check, r=_rc_check, k=_code:
                    (f"V{k} rc={r}" if f"    V{k} " in o
                     else f"that code reached no reporting arm · exit {r} :: {o}"))
            arm(f"--write renders every artifact over a V{_code} tree and exits 0", "rc=0",
                lambda r=_rc_write, o=_out_write: f"rc={r}" if r == 0 else f"rc={r} :: {o}")
            if _code in (15, 16):
                arm(f"V{_code} names the conf key it disarms", backlog.CUTOFF_KEY,
                    lambda o=_out_check: o)

        # AC5 and AC3's second half — the data-loss guard over an APPENDED authored row.
        _guard_conf = _build_backlog_fixture(bt, CORE)
        _read_mode(cmd_write, bt, _guard_conf)
        _vpath = os.path.join(bt, "memory", "backlog", "EXMP.md")
        _fresh = read_text(_vpath)
        _straggler = "- EXMP-aBar-9 · OPEN · a row a straggler merged in\n"
        write_text(_vpath, _fresh + _straggler)
        _rc_g, _out_g = _read_mode(cmd_write, bt, _guard_conf)
        arm("--write refuses a view carrying an authored row and exits 1", "rc=1",
            lambda: f"rc={_rc_g}")
        arm("the guarded view is left BYTE-unchanged", "True",
            lambda: str(read_text(_vpath) == _fresh + _straggler))
        arm("every OTHER artifact is still written", "True",
            lambda: str(os.path.isfile(os.path.join(bt, "memory", "backlog", "OTHR.md"))))
        arm("the guard names the offending line", "EXMP-aBar-9", lambda: _out_g)
        arm("the guard names all three recipe entry points", "True",
            lambda: str(all(v in _out_g for v in ("--relocate", "--repair", "--ingest"))))
        arm("the guard's message quotes the recipe constant byte for byte", "True",
            lambda: str(all(line in _out_g for line in
                            backlog.render_relocation_recipe(kit_rel(), "memory"))))
        _rc_gc, _out_gc = _read_mode(cmd_check, bt, _guard_conf)
        arm("--check names the same line", "EXMP-aBar-9", lambda: _out_gc)
        arm("--check does NOT offer --write as the remedy for a guarded view", "False",
            lambda: str("build-index DRIFT" in _out_gc))

        # AC16 — a conflict region whose two sides are both view rows is RE-RENDERED over.
        _rows = [x for x in _fresh.split("\n") if x.startswith("| [EXMP-")]
        write_text(_vpath, _fresh.rstrip("\n") + "\n<<<<<<< ours\n" + _rows[0]
                   + "\n=======\n" + _rows[1] + "\n>>>>>>> theirs\n")
        _rc_v, _out_v = _read_mode(cmd_write, bt, _guard_conf)
        arm("a view-against-view conflict is re-rendered over, at exit 0", "rc=0",
            lambda: f"rc={_rc_v}" if _rc_v == 0 else f"rc={_rc_v} :: {_out_v}")
        arm("the re-render announces itself rather than repairing in silence",
            "re-rendered over a view conflict", lambda: _out_v)
        arm("the re-rendered view equals a fresh render", "True",
            lambda: str(read_text(_vpath) == _fresh))
        write_text(_vpath, _fresh.rstrip("\n") + "\n<<<<<<< ours\n" + _rows[0]
                   + "\n=======\n" + _straggler.rstrip("\n") + "\n>>>>>>> theirs\n")
        _rc_m, _out_m = _read_mode(cmd_write, bt, _guard_conf)
        arm("a conflict region holding ONE id-leading row still trips the guard", "rc=1",
            lambda: f"rc={_rc_m}")
        arm("that guard names the line the grammar never emits", "EXMP-aBar-9", lambda: _out_m)

        # AC14 — an authored shard at a view path, carrying no generator header at all.
        write_text(_vpath, "# memory/backlog/EXMP.md — the old authored shard\n\n"
                           "- EXMP-aBar-9 · OPEN · a row nobody relocated\n")
        _shard = read_text(_vpath)
        _rc_s, _out_s = _read_mode(cmd_write, bt, _guard_conf)
        arm("an authored shard with NO generator header still trips the guard", "rc=1",
            lambda: f"rc={_rc_s}")
        arm("the take-theirs shard is left byte-unchanged", "True",
            lambda: str(read_text(_vpath) == _shard))
        arm("the guard names the shard's id-leading line", "EXMP-aBar-9", lambda: _out_s)

        # AC6 — the mode guard, from both of its sides.
        _sh = _build_backlog_fixture(bt, NOHOME, mode="shards")
        _rc_sh, _out_sh = _read_mode(cmd_check, bt, _sh)
        arm("a tracked BACKLOG.md under shards is a mode verdict", f"V{GUARD_MODE}",
            lambda: _out_sh)
        arm("the mode verdict names the file", "memory/builds/aFoo/BACKLOG.md", lambda: _out_sh)
        arm("--check exits 1 on the mode guard", "rc=1", lambda: f"rc={_rc_sh}")
        _sh2files = {k: v for k, v in NOHOME.items() if not k.endswith("/BACKLOG.md")}
        _sh2files[spec_rel] = _render_backlog_spec("EXMP-aFoo-1", tail=" · closes EXMP-aBar-5")
        _sh2 = _build_backlog_fixture(bt, _sh2files, mode="shards")
        _rc_sh2, _out_sh2 = _read_mode(cmd_check, bt, _sh2)
        arm("a `closes` header under shards is the same half-migration, seen from the spec side",
            f"V{GUARD_MODE}", lambda: _out_sh2)
        arm("it names the spec that carries the verb", "2026-09-01-spec-aFoo-1.md",
            lambda: _out_sh2)

        # AC7 — the archive guard, with the innocent neighbour it must not red.
        _a7 = dict(CORE)
        _a7["memory/archive/EXMP.2026-01.md"] = "# a rotated family shard\n"
        _a7["memory/archive/DECISIONS.2026-01.md"] = "# a rotated decision log\n"
        _rc_a, _out_a = _read_mode(cmd_check, bt, _build_backlog_fixture(bt, _a7))
        arm("a rotated backlog archive under builds is a verdict", f"V{GUARD_ARCHIVE}",
            lambda: _out_a)
        arm("the archive verdict names the file", "memory/archive/EXMP.2026-01.md",
            lambda: _out_a)
        arm("a rotated DECISION LOG archive raises nothing", "False",
            lambda: str("DECISIONS.2026-01.md" in _out_a))

        # AC8 — the filing home, and the refusal it must not retire for shards adopters.
        _c8 = _build_backlog_fixture(bt, CORE)
        _arts8 = plan(bt, _c8)[0]
        arm("a filing home's asks are collected", "OTHR-aHome-1",
            lambda: _arts8["memory/backlog/OTHR.md"])
        arm("a filing home reaches no LIVE.md row", "False",
            lambda: str("aHome" in _arts8["memory/LIVE.md"]))
        arm("a filing home reaches no ledger row", "False",
            lambda: str("aHome" in _arts8["memory/ledger/2026-09.md"]))
        _c8s = _build_backlog_fixture(bt, CORE, mode="shards")
        arm("the same folder under SHARDS still raises the no-README refusal",
            "no tracked README.md", lambda: plan(bt, _c8s))

        # AC9 — the roster scan, both modes, over one corpus.
        _f9 = dict(NOHOME)
        _f9["memory/backlog/EXMP.md"] = ("# the authored shard\n\n"
                                         "- EXMP-aBar-99 · OPEN · an id only this file names\n")
        _build_backlog_fixture(bt, _f9)
        _tracked9 = [p for p in run("git", "ls-files", "--", "memory/", cwd=bt).split("\n") if p]
        arm("the builds-mode roster scan reads no file under the backlog directory", "False",
            lambda: str(any("EXMP-aBar-99" in v for v in
                            rosters(bt, _tracked9, "memory", set(BL_FAMILIES),
                                    skip_backlog=True).values())))
        arm("the shards-mode roster scan still reads it — the control", "True",
            lambda: str(any("EXMP-aBar-99" in v for v in
                            rosters(bt, _tracked9, "memory", set(BL_FAMILIES)).values())))
        _ids_b = plan(bt, _build_backlog_fixture(bt, NOHOME))[0]
        _ids_s = plan(bt, _build_backlog_fixture(bt, NOHOME, mode="shards"))[0]
        arm("every build README's ids: renders identically in both modes", "True",
            lambda: str(all([x for x in _ids_b[k].split("\n") if x.startswith("ids:")]
                            == [x for x in _ids_s[k].split("\n") if x.startswith("ids:")]
                            for k in _ids_b if k.endswith("README.md"))))
        arm("a shards render produces no view artifact at all", "[]",
            lambda: str(sorted(k for k in _ids_s if k.startswith("memory/backlog/"))))

        # AC10 — the liveness line, every figure of it DERIVED from the fixture.
        _rc10, _out10 = _read_mode(cmd_check, bt, _build_backlog_fixture(bt, CORE))
        arm("the backlog liveness line prints counts that match the fixture",
            "backlog 6 ask(s) · 1 row(s) · 0 link(s) in 3 file(s) · 5 live · 0 verdict(s)",
            lambda: _out10)
        _rc10s, _out10s = _read_mode(cmd_check, bt, _build_backlog_fixture(bt, NOHOME, mode="shards"))
        arm("a shards tree ANNOUNCES its layout instead of printing a clean zero",
            "backlog layout is `shards`", lambda: _out10s)

        # AC11 and AC17 — the print modes.
        _c11 = _build_backlog_fixture(bt, CORE)
        _rc, _so, _se = _read_asks_run(bt, _c11, ["EXMP-aFoo-3"])
        arm("--asks <id> answers for a TERMINAL ask", "CLOSED", lambda: _so)
        arm("--asks <id> names the evidence that decided it", "abc1234", lambda: _so)
        arm("--asks exits 0 and its notices are on stderr", "rc=0 stderr=True",
            lambda: f"rc={_rc} stderr={'build-index: backlog' in _se}")
        _rc, _so, _se = _read_asks_run(bt, _c11, ["EXMP", "--all", "--json"])
        arm("--asks --json decodes as a WHOLE, with the pinned fields", "True",
            lambda: str(all(k in json.loads(_so)["asks"][0] for k in
                            ("id", "home", "file", "line", "filed", "unit", "status", "decided_by",
                             "sev", "closing", "declining", "holds", "live_specs"))))
        arm("--asks --json carries mode and examined", "builds 3",
            lambda: f"{json.loads(_so)['mode']} {json.loads(_so)['examined']}")
        arm("--asks --all lists the terminal ask too", "True",
            lambda: str(any(r["id"] == "EXMP-aFoo-3" for r in json.loads(_so)["asks"])))
        _rc, _so, _se = _read_asks_run(bt, _c11, ["--build", "aBar"])
        # ROWS, not cells. `count("| EXMP-")` counted the Decided-by cell as well, which made
        # a one-row answer read as two — and would have made a two-row answer read as one.
        def _read_row_count(text):
            return sum(1 for x in text.split("\n") if x.startswith("| EXMP-"))

        arm("--asks --build filters to one filing home", "rows=1 bar=True",
            lambda: f"rows={_read_row_count(_so)} bar={'EXMP-aBar-5' in _so}")
        _f11 = dict(CORE)
        _f11[foo_rel] = _render_backlog_file("aFoo", [ask2, ask10], [backlog.render_status_row(
            "BLOCKED", "EXMP-aFoo-2", "waiting on the other one", value="EXMP-aFoo-10")])
        _c11b = _build_backlog_fixture(bt, _f11)
        _rc, _so, _se = _read_asks_run(bt, _c11b, ["EXMP", "--status", "BLOCKED"])
        arm("--status prints only the matching row, at exit 0", "rows=1 blocked=True rc=0",
            lambda: f"rows={_read_row_count(_so)} blocked={'BLOCKED' in _so} rc={_rc}")
        _rc, _so, _se = _read_asks_run(bt, _c11b, ["EXMP", "--status", "NOPE"])
        arm("an unrecognised --status token refuses BY NAME on stderr and prints nothing",
            "rc=2 out='' named=True",
            lambda: f"rc={_rc} out='{_so}' named={'NOPE' in _se}")
        # A verdict-carrying tree, because the mode built to EXPLAIN a verdict must run while one
        # stands. And a refused tree, where there is no value to print at all.
        _f17 = dict(CORE)
        _f17[foo_rel] = _render_backlog_file("aFoo", [ask2, "- matches no declared row shape"])
        _f17["memory/" + STALE_HEADER_WAIVER] = \
            "memory/builds/aBar/README.md  a corrupt header, tolerated for this arm\n"
        _f17["memory/builds/aBar/README.md"] = ("---\nslug: aBar\nthis line has no colon\n---\n"
                                                "\n# aBar\n\n" + MARK_OPEN + "\n"
                                                + MARK_CLOSE + "\n")
        _rc, _so, _se = _read_asks_run(bt, _build_backlog_fixture(bt, _f17), ["EXMP", "--all", "--json"])
        arm("a tolerated header and a fold verdict leave stdout decodable whole", "True",
            lambda: str(isinstance(json.loads(_so), dict)))
        arm("the tolerated-header line went to stderr, not to stdout", "True",
            lambda: str("tolerated by waiver" in _se and "tolerated by waiver" not in _so))
        arm("--asks exits 0 while a fold verdict stands", "rc=0", lambda: f"rc={_rc}")
        _f17b = dict(CORE)
        _f17b["memory/builds/aBar/README.md"] = "not front matter at all\n"
        _rc, _so, _se = _read_asks_run(bt, _build_backlog_fixture(bt, _f17b), ["EXMP", "--json"])
        arm("a collect() REFUSAL exits 1 with nothing on stdout", "rc=1 out=''",
            lambda: f"rc={_rc} out='{_so}'")
        arm("the refusal itself is on stderr", "no front matter", lambda: _se)

        # AC12 — the excerpt key.
        arm("BACKLOG_EXCERPT_CHARS=0 refuses by name", "BACKLOG_EXCERPT_CHARS='0'",
            lambda: plan(bt, _build_backlog_fixture(bt, CORE, excerpt="0")))
        arm("BACKLOG_EXCERPT_CHARS=abc refuses by name", "BACKLOG_EXCERPT_CHARS='abc'",
            lambda: plan(bt, _build_backlog_fixture(bt, CORE, excerpt="abc")))
        arm("a DECLARED excerpt re-cuts the summary",
            "| a / pipe, a deep/path/to/a/file.py… |",
            lambda: [x for x in plan(bt, _build_backlog_fixture(bt, CORE, excerpt="40"))[0]
                     ["memory/backlog/EXMP.md"].split("\n") if "EXMP-aFoo-4" in x][0])

    # ------------------------------------ TOOL-dDerivedDocket-15 — the ask envelope
    # THE CLAUSE GRAMMAR IS GRADED THROUGH THIS FILE'S SELFTEST and not through `backlog.py`'s,
    # because the criteria that own it ask what `--check`, `--asks --tsv` and `--new-build` do with
    # a clause — and only this module has those. The parser arms below call into that module
    # directly, so the grammar is still asserted where a reader of a fixture can see the row.
    _g15 = backlog.build_grammar(BL_FAMILIES)
    #: A locator whose path EXISTS in every fixture below, so R4 turns on the clause rather than on
    #: which file a fixture happened to write.
    _SEEN_HERE = ("seen", "`memory/builds/aFoo/README.md`@abc1234")
    _ACCEPT = ("accept", "the row says what done looks like")

    # AC1 — the tail, read right to left, with the collision that makes a misread LOUD.
    _ac1_row = backlog.extract_row(backlog.render_ask_row(
        "EXMP-aFoo-3", "2026-09-15", "push-main.sh reports a gate RED as a network failure",
        pointer="`tools/push-main.sh`",
        clauses=(("seen", "`tools/push-main.sh`@7484d8d7:23"),
                 ("accept", "a RED bar prints GATE FAIL and exits non-zero"),
                 ("out", "retry policy"))), _g15)
    arm("the §4 example ask yields its three clauses, its pointer and its text",
        "clauses=3 seen=['`tools/push-main.sh`@7484d8d7:23'] "
        "pointer=`tools/push-main.sh` text=push-main.sh reports a gate RED as a network failure",
        lambda: f"clauses={len(_ac1_row.extra['clauses'])} "
                f"seen={backlog.read_clause_values(_ac1_row.extra['clauses'], 'seen')} "
                f"pointer={_ac1_row.extra['pointer']} text={_ac1_row.why}")
    # THE COLLISION FIXTURE: the ask TEXT itself ends ` · out `, ahead of the two real clauses. Read
    # left to right, that `out` would swallow both of them and the ask would grade as carrying no
    # acceptance — silently. Read right to left it costs the writer exactly one clause, and the
    # empty value it leaves behind is what V13 names.
    _ac1_collide = backlog.render_ask_row(
        "EXMP-aFoo-4", "2026-09-15", "the real text · out",
        clauses=(_SEEN_HERE, ("accept", "it works")))
    _ac1_bad = backlog.extract_row(_ac1_collide, _g15)
    arm("a TEXT ending in a clause label still yields the REAL seen and accept, read from the right",
        "text=the real text seen=1 accept=['it works'] out=['']",
        lambda: f"text={_ac1_bad.why} "
                f"seen={len(backlog.read_clause_values(_ac1_bad.extra['clauses'], 'seen'))} "
                f"accept={backlog.read_clause_values(_ac1_bad.extra['clauses'], 'accept')} "
                f"out={backlog.read_clause_values(_ac1_bad.extra['clauses'], 'out')}")
    _ac1_legacy = backlog.extract_row(
        backlog.render_ask_row("EXMP-aFoo-6", "2026-01-01", "a legacy ask with no tail"), _g15)
    arm("a clause-free legacy row yields the fields the view unit yielded, and no clause",
        "cls=ask text=a legacy ask with no tail clauses=() pointer= unit=False",
        lambda: f"cls={_ac1_legacy.cls} text={_ac1_legacy.why} "
                f"clauses={_ac1_legacy.extra['clauses']} pointer={_ac1_legacy.extra['pointer']} "
                f"unit={_ac1_legacy.extra['unit']}")

    with tempfile.TemporaryDirectory() as envbase:
        et = os.path.join(envbase, "envelope")
        os.makedirs(et)

        def _render_env_readme(slug):
            """A fixture build README carrying the AUTHORED roster pair the slot contract makes
            mandatory on every tracked build README, which `_render_backlog_readme` predates."""
            return ("---\nslug: " + slug + "\nnode: a\nopened: 2026-09-01\nstreams: tool\n"
                    "roster: EXMP\nids: EXMP-" + slug + "-1\n---\n\n# " + slug + "\n\n"
                    + PLAN_OPEN + "\n" + PLAN_CLOSE + "\n\n" + MARK_OPEN + "\n" + MARK_CLOSE + "\n")

        def _build_env_tree(foo_asks=(), foo_rows=(), bar_asks=(), bar_rows=(), bar_tail=""):
            """The two-build corpus every arm below is graded over. ONE shape, so an arm that
            changes a row cannot also be changing which files exist."""
            return {
                "memory/builds/aFoo/README.md": _render_env_readme("aFoo"),
                "memory/builds/aFoo/spec/2026-09-01-spec-aFoo-90.md":
                    _render_backlog_spec("EXMP-aFoo-90"),
                "memory/builds/aFoo/BACKLOG.md": _render_backlog_file("aFoo", foo_asks, foo_rows),
                "memory/builds/aBar/README.md": _render_env_readme("aBar"),
                "memory/builds/aBar/spec/2026-09-01-spec-aBar-80.md":
                    _render_backlog_spec("EXMP-aBar-80", tail=bar_tail),
                "memory/builds/aBar/BACKLOG.md": _render_backlog_file("aBar", bar_asks, bar_rows),
            }

        # AC1's second half — the misread `out` value REACHES `--check` as V13, on the real tree.
        _c1 = _build_backlog_fixture(et, _build_env_tree(foo_asks=[_ac1_collide]))
        _rc1, _out1 = _read_mode(cmd_check, et, _c1)
        arm("--check names V13 on the value the TEXT collision misread", "V13", lambda: _out1)
        arm("and it names the label whose value came back empty", "`out` clause with no value",
            lambda: _out1)

        # AC2 — the SCOPE merge: it ADDS a clause and it MOVES no status.
        _ac2_ask = backlog.render_ask_row("EXMP-aFoo-1", "2026-09-01", "seen but not accepted",
                                          clauses=(_SEEN_HERE,))
        _ac2_files = _build_env_tree(
            foo_asks=[_ac2_ask],
            foo_rows=[backlog.render_scope_row("EXMP-aFoo-1", (("accept", "cured from outside"),))])
        _c2 = _build_backlog_fixture(et, _ac2_files)
        _rc, _so, _se = _read_asks_run(et, _c2, ["--tsv", "--all"])
        _ac2_row = [x for x in _so.split("\n") if x.startswith("ask\tEXMP-aFoo-1")][0].split("\t")
        arm("a SCOPE row's `accept` cures an ask the ask row left unaccepted", "ready=yes missing=-",
            lambda: f"ready={_ac2_row[6]} missing={_ac2_row[7]}")
        arm("and the SCOPE row moves no status: the fold still says OPEN", "status=OPEN",
            lambda: f"status={_ac2_row[2]}")
        _ac2_filer, _ac2_scoper = "the filer rule", "the scoper rule"
        _ac2b = _build_env_tree(
            foo_asks=[backlog.render_ask_row("EXMP-aFoo-1", "2026-09-01", "accepted twice over",
                                             clauses=(_SEEN_HERE, ("accept", _ac2_filer)))],
            foo_rows=[backlog.render_scope_row("EXMP-aFoo-1", (("accept", _ac2_scoper),))])
        _c2b = _build_backlog_fixture(et, _ac2b)
        _rc, _so2, _se = _read_asks_run(et, _c2b, ["EXMP-aFoo-1"])
        arm("--asks <id> prints BOTH merged `accept` values, never one picked",
            "filer=True scoper=True",
            lambda: f"filer={_ac2_filer in _so2} scoper={_ac2_scoper in _so2}")
        _ac2c = _build_env_tree(
            foo_asks=[backlog.render_ask_row(
                "EXMP-aFoo-1", "2026-09-01", "granted",
                clauses=(_SEEN_HERE, _ACCEPT, ("may", "`tools/push-main.sh`")))],
            foo_rows=[backlog.render_scope_row("EXMP-aFoo-1", (("may", "none"),))])
        _c2c = _build_backlog_fixture(et, _ac2c)
        _rc, _so3, _se = _read_asks_run(et, _c2c, ["--tsv", "--all"])
        # THE WHOLE FIELD, inside a terminator. `arm` matches a SUBSTRING, so an assertion naming
        # only the grant passed over a field reading `<grant>,none` — measured, by staging the
        # break that stops absorbing `none` and watching this arm stay green.
        arm("a SCOPE row's `may none` is ABSORBED and leaves the ask's grant unchanged",
            "grant=[`tools/push-main.sh`]",
            lambda: "grant=[" + [x for x in _so3.split("\n")
                                 if x.startswith("ask\t")][0].split("\t")[9] + "]")

        # AC3 — V13's four findings in one tree, each naming its file and its row.
        _ac3 = _build_env_tree(
            foo_asks=[
                backlog.render_ask_row("EXMP-aFoo-1", "2026-09-01", "a line that moves",
                                       clauses=(("seen", "`tools/x.py`:23"),)),
                backlog.render_ask_row("EXMP-aFoo-2", "2026-09-01", "said twice",
                                       clauses=(("accept", "once"), ("accept", "and again"))),
            ],
            foo_rows=[
                backlog.render_scope_row("EXMP-aFoo-88", (("accept", "nobody filed it"),)),
                backlog.render_scope_row("EXMP-aFoo-1", (("verify", "the first row"),)),
                backlog.render_scope_row("EXMP-aFoo-1", (("verify", "and a second one"),)),
            ])
        _rc3, _out3 = _read_mode(cmd_check, et, _build_backlog_fixture(et, _ac3))
        _v13 = [x for x in _out3.split("\n") if "    V13 " in x]
        arm("--check names V13 four times over one tree, and exits 1", "hits=4 rc=1",
            lambda: f"hits={len(_v13)} rc={_rc3}")
        arm("V13 names the bare line number as fix F6's own case, with the remedy",
            "pins a line and no commit", lambda: _out3)
        arm("V13 names the doubled label", "writes the `accept` clause more than once",
            lambda: _out3)
        arm("V13 names the SCOPE row nobody filed a target for", "targets EXMP-aFoo-88",
            lambda: _out3)
        arm("V13 names the second SCOPE row for one target in one file",
            "a second SCOPE row for EXMP-aFoo-1 in this file", lambda: _out3)
        arm("and V7 does NOT also report the unfiled SCOPE target — one finding, one code", "False",
            lambda: str(any("V7 " in x and "EXMP-aFoo-88" in x for x in _out3.split("\n"))))


        # AC4 — V14, FORWARD-ONLY, read off the MERGED clauses. Every ask below is filed ON the
        # cutoff except the control, which is filed the day before: the boundary is the whole
        # question, and a fixture filed a month either side of it would not ask it.
        _cut = "2026-06-01"
        _ac4 = _build_env_tree(
            foo_asks=[
                backlog.render_ask_row("EXMP-aFoo-1", _cut, "no clause at all"),
                backlog.render_ask_row("EXMP-aFoo-2", _cut, "seen but never graded",
                                       clauses=(_SEEN_HERE,)),
                backlog.render_ask_row("EXMP-aFoo-3", _cut, "accepted", clauses=(_ACCEPT,)),
                backlog.render_ask_row("EXMP-aFoo-4", _cut, "runnable", clauses=(
                    ("seen", "`memory/builds/aFoo/README.md`@abc1234 run `git --version`"),)),
                backlog.render_ask_row("EXMP-aFoo-5", _cut, "cured from outside"),
                backlog.render_ask_row("EXMP-aFoo-6", "2026-05-31", "the day before, ungraded"),
            ],
            foo_rows=[backlog.render_scope_row("EXMP-aFoo-5", (("accept", "cured here"),))],
            bar_asks=[backlog.render_ask_row("EXMP-aBar-9", "2026-05-01", "a legacy ask")])
        _rc4, _out4 = _read_mode(cmd_check, et, _build_backlog_fixture(et, _ac4, cutoff=_cut))
        _v14 = sorted(x.split(": ")[1].split(" ")[0] for x in _out4.split("\n") if "    V14 " in x)
        arm("V14 names the ungraded asks filed ON the cutoff, and only those",
            "['EXMP-aFoo-1', 'EXMP-aFoo-2']", lambda: str(_v14))
        arm("V14 says which two clauses would have satisfied it",
            "neither `accept` nor a `seen … run`", lambda: _out4)
        _rc4b, _out4b = _read_mode(cmd_check, et, _build_backlog_fixture(
            et, _ac4, cutoff="2026-06-02"))
        arm("moving the cutoff PAST every ask disarms V14 entirely — the forward-only control",
            "0", lambda: str(len([x for x in _out4b.split("\n") if "    V14 " in x])))

        # AC5 — the six rules, one failing fixture each, graded over ONE mandate. The expected
        # table is spelled row by row rather than summarised: a count would pass over two rows that
        # swapped grades.
        _ready_asks = [
            backlog.render_ask_row("EXMP-aFoo-1", "2026-09-01", "open and acceptable",
                                   clauses=(_SEEN_HERE, _ACCEPT)),
            backlog.render_ask_row("EXMP-aFoo-2", "2026-09-01", "held outside the mandate",
                                   clauses=(_SEEN_HERE, _ACCEPT)),
            backlog.render_ask_row("EXMP-aFoo-3", "2026-09-01", "held inside the mandate",
                                   clauses=(_SEEN_HERE, _ACCEPT)),
            backlog.render_ask_row("EXMP-aFoo-4", "2026-09-01", "the hold target",
                                   clauses=(_SEEN_HERE, _ACCEPT)),
            backlog.render_ask_row("EXMP-aFoo-5", "2026-09-01", "filed twice over",
                                   clauses=(_SEEN_HERE, _ACCEPT)),
            backlog.render_ask_row("EXMP-aFoo-5", "2026-09-01", "filed twice over",
                                   clauses=(_SEEN_HERE, _ACCEPT)),
            backlog.render_ask_row("EXMP-aBar-7", "2026-09-01", "filed in a foreign folder",
                                   clauses=(_SEEN_HERE, _ACCEPT)),
            backlog.render_ask_row("EXMP-aFoo-8", "2026-09-01", "pointing at nothing",
                                   clauses=(_ACCEPT,), pointer="`memory/nope/gone.md`"),
            backlog.render_ask_row("EXMP-aFoo-9", "2026-09-01", "outside this repo, unbounded",
                                   clauses=(("seen", "other:tools/x.py@abc1234"), _ACCEPT)),
            backlog.render_ask_row("EXMP-aFoo-10", "2026-01-15", "pre-cutoff, located only",
                                   pointer="`memory/builds/aFoo/README.md`"),
            backlog.render_ask_row("EXMP-aFoo-11", "2026-01-15", "pre-cutoff, neither"),
        ]
        _ready_rows = [
            backlog.render_status_row("BLOCKED", "EXMP-aFoo-2", "w", value="EXMP-aBar-5"),
            backlog.render_status_row("BLOCKED", "EXMP-aFoo-3", "w", value="EXMP-aFoo-4"),
        ]
        _c5 = _build_backlog_fixture(et, _build_env_tree(
            foo_asks=_ready_asks, foo_rows=_ready_rows,
            bar_asks=[backlog.render_ask_row("EXMP-aBar-5", "2026-09-01", "the outside hold")]),
            cutoff=_cut)
        _MANDATE = ["EXMP-aFoo-1", "-2", "-3", "-4", "-5", "-6", "EXMP-aBar-7", "EXMP-aFoo-8",
                    "-9", "-10", "-11"]
        _rc5, _so5, _se5 = _read_asks_run(et, _c5, ["--tsv", "--all", "--ready"] + _MANDATE)

        def _read_grades(text):
            return "\n".join(" ".join((f[1], f[6], f[7]))
                             for f in (x.split("\t") for x in text.rstrip("\n").split("\n"))
                             if f[0] == ASK_TSV_HEAD)

        arm("every READY rule is graded, one failing fixture each, over one mandate",
            "EXMP-aFoo-1 yes -\nEXMP-aFoo-2 no R3\nEXMP-aFoo-3 yes -\nEXMP-aFoo-4 yes -\n"
            "EXMP-aFoo-5 no R1\nEXMP-aFoo-6 no R1,R2,R4,R5\nEXMP-aBar-7 no R1\n"
            "EXMP-aFoo-8 no R4\nEXMP-aFoo-9 no R6\nEXMP-aFoo-10 legacy R5\n"
            "EXMP-aFoo-11 no R4,R5",
            lambda: _read_grades(_so5))
        arm("the `-N` continuation carried the mandate's family and slug", "examined\t11",
            lambda: _so5)
        arm("a pre-cutoff ask failing BOTH R4 and R5 is `no`, never `legacy` — fix F6's rule",
            "EXMP-aFoo-11 no R4,R5", lambda: _read_grades(_so5))
        arm("--ready over a mandate exits 0 whatever the grades are", "rc=0", lambda: f"rc={_rc5}")

        # AC6 — R2, the one rule a caller's own knowledge changes.
        _ac6 = _build_env_tree(
            foo_asks=[
                backlog.render_ask_row("EXMP-aFoo-20", "2026-09-01", "closed from another build",
                                       clauses=(_SEEN_HERE, _ACCEPT)),
                backlog.render_ask_row("EXMP-aFoo-21", "2026-09-01", "a unit of the target folder",
                                       unit=True, clauses=(_SEEN_HERE, _ACCEPT)),
                backlog.render_ask_row("EXMP-aFoo-22", "2026-09-01", "already answered",
                                       clauses=(_SEEN_HERE, _ACCEPT)),
            ],
            foo_rows=[backlog.render_status_row("CLOSED", "EXMP-aFoo-22", "done", value="abc1234")],
            bar_asks=[backlog.render_ask_row("EXMP-aBar-5", "2026-09-01", "an unrelated ask")],
            bar_tail=" · closes EXMP-aFoo-20 EXMP-aFoo-21")
        _c6 = _build_backlog_fixture(et, _ac6, cutoff=_cut)

        def _read_grade(text, ask_id):
            for line in text.rstrip("\n").split("\n"):
                f = line.split("\t")
                if f[0] == ASK_TSV_HEAD and f[1] == ask_id:
                    return f"{f[6]} {f[7]} {f[10]}"
            return "no such row"

        _rc, _so6, _se = _read_asks_run(et, _c6, ["--tsv", "--all"])
        arm("a live closing spec in ANOTHER build is a live claim, so R2 refuses",
            "no R2 EXMP-aBar-80", lambda: _read_grade(_so6, "EXMP-aFoo-20"))
        arm("a TERMINAL ask fails R2 and nothing else", "no R2 -",
            lambda: _read_grade(_so6, "EXMP-aFoo-22"))
        _rc, _so6b, _se = _read_asks_run(et, _c6, ["--tsv", "--all", "--live-builds", "aFoo"])
        arm("--live-builds omitting that build admits the claim and names it STALE",
            "yes - stale:EXMP-aBar-80", lambda: _read_grade(_so6b, "EXMP-aFoo-20"))
        _rc, _so6c, _se = _read_asks_run(et, _c6, ["--tsv", "--all", "--target", "aBar"])
        arm("--target naming that build admits its own spec, unprefixed",
            "yes - EXMP-aBar-80", lambda: _read_grade(_so6c, "EXMP-aFoo-20"))
        _rc, _so6d, _se = _read_asks_run(et, _c6, ["--tsv", "--all", "--target", "aFoo"])
        arm("a `unit` ask of the --target folder is admitted although its closer is foreign",
            "yes - EXMP-aBar-80", lambda: _read_grade(_so6d, "EXMP-aFoo-21"))
        arm("and the SAME option leaves its non-`unit` neighbour refused — the control",
            "no R2 EXMP-aBar-80", lambda: _read_grade(_so6d, "EXMP-aFoo-20"))


        # AC7 — the machine projection, asserted POSITION BY POSITION. A row can carry eleven
        # fields and still be wrong, and a consumer reading it by position would not notice: the
        # arm therefore pins every cell of every row rather than counting tabs.
        # A GRADE NEVER DECIDES THE EXIT STATUS. Reported as a non-zero, an all-`no` mandate would
        # reach a caller's preflight as a PRODUCER FAILURE naming an exit status, instead of as the
        # refusal that names each id's failing rules. Run over AC6's tree, REBUILT here rather than
        # read from the conf that tree was built with: `_build_backlog_fixture` replaces the memory
        # tree on every call, so a conf held from an earlier arm names a tree that is no longer on
        # disk — which is how an arm silently grades the wrong fixture.
        _rc7b, _so7b, _se7b = _read_asks_run(
            et, _build_backlog_fixture(et, _ac6, cutoff=_cut), ["--tsv", "--all"])
        arm("a fixture where every examined ask grades `no` still exits 0, rows and all",
            "rc=0 grades={'no'} rows=4 closes-with=examined\t4",
            lambda: f"rc={_rc7b} "
                    f"grades={ {x.split(chr(9))[6] for x in _so7b.rstrip(chr(10)).split(chr(10)) if x.startswith(ASK_TSV_HEAD)} } "
                    f"rows={len([x for x in _so7b.rstrip(chr(10)).split(chr(10)) if x.startswith(ASK_TSV_HEAD)])} "
                    f"closes-with={_so7b.rstrip(chr(10)).split(chr(10))[-1]}")
        _ac7_asks = [
            backlog.render_ask_row("EXMP-aFoo-30", "2026-09-01", "unlabelled and open"),
            backlog.render_ask_row("EXMP-aFoo-31", "2026-09-01", "answered twice over",
                                   clauses=(_SEEN_HERE, _ACCEPT)),
            backlog.render_ask_row("EXMP-aFoo-32", "2026-09-01", "blocked by its own spec",
                                   clauses=(_SEEN_HERE, _ACCEPT)),
        ]
        _ac7_rows = [
            backlog.render_status_row("CLOSED", "EXMP-aFoo-31", "done", value="abc1234"),
            backlog.render_sev_row("EXMP-aFoo-31", "HIGH", "graded"),
        ]
        _ac7 = {
            "memory/builds/aFoo/README.md": _render_env_readme("aFoo"),
            "memory/builds/aFoo/spec/2026-09-01-spec-aFoo-70.md": _render_backlog_spec(
                "EXMP-aFoo-70", status="CLOSED", tail=" · closes EXMP-aFoo-31"),
            "memory/builds/aFoo/spec/2026-09-01-spec-aFoo-71.md": _render_backlog_spec(
                "EXMP-aFoo-71", status="BLOCKED", tail=" · advances EXMP-aFoo-32"),
            "memory/builds/aFoo/BACKLOG.md": _render_backlog_file("aFoo", _ac7_asks, _ac7_rows),
            # A CORRUPT HEADER, TOLERATED BY WAIVER, so the notice `collect()` prints on every run
            # has somewhere to land — and the arm can say it landed on stderr and not in the rows.
            "memory/builds/aBar/README.md": "---\nslug: aBar\nthis line has no colon\n---\n",
            "memory/" + STALE_HEADER_WAIVER:
                "memory/builds/aBar/README.md  a corrupt header, tolerated for this arm\n",
        }
        _c7 = _build_backlog_fixture(et, _ac7, cutoff=_cut)
        _rc7, _so7, _se7 = _read_asks_run(et, _c7, ["--all", "--tsv"])
        arm("--tsv prints every field of every row, position by position, and nothing else",
            "ask\tEXMP-aFoo-30\tOPEN\t-\taFoo\t-\tno\tR4,R5\t-\t-\t-\n"
            "ask\tEXMP-aFoo-31\tCLOSED\tEXMP-aFoo-70,abc1234\taFoo\tHIGH\tno\tR2\t-\t-\t-\n"
            "ask\tEXMP-aFoo-32\tBLOCKED\tEXMP-aFoo-71\taFoo\t-\tyes\t-\t-\t-\tEXMP-aFoo-71\n"
            "examined\t3",
            lambda: _so7.rstrip("\n"))
        arm("every `ask` line carries exactly eleven TAB-separated fields", "[11, 11, 11]",
            lambda: str([len(x.split("\t")) for x in _so7.rstrip("\n").split("\n")
                         if x.startswith(ASK_TSV_HEAD + "\t")]))
        arm("no field is EMPTY, which a run of tabs would collapse away", "False",
            lambda: str(any(f == "" for x in _so7.rstrip("\n").split("\n") for f in x.split("\t"))))
        arm("the waiver notice went to stderr and never into the row stream", "err=True out=False",
            lambda: f"err={'tolerated by waiver' in _se7} "
                    f"out={'tolerated by waiver' in _so7}")
        arm("--tsv exits 0 over a tree carrying a fold verdict", "rc=0", lambda: f"rc={_rc7}")
        _rc7c, _so7c, _se7c = _read_asks_run(et, _c7, ["--tsv", "--ready"])
        arm("--ready naming NO id is an empty mandate and an empty population, at exit 0",
            "rc=0 out=examined\t0", lambda: f"rc={_rc7c} out={_so7c.rstrip(chr(10))}")
        # THE DECIDED-BY SET AGAINST THE ONE VALUE THE FOLD NAMES. Two computations over one
        # corpus, and this arm is the only thing holding them to one answer: the fold picks the
        # MINIMUM of the set for a field that holds one value, so a set that stopped containing
        # that minimum would mean the projection and the table had started describing different
        # records. WHAT IT DOES NOT BUY, said plainly: both are derived here from the same corpus,
        # so this is a consistency check between two implementations and never evidence that
        # either of them names the right records — that is what the fixture's own pinned cells
        # above are for, and the `mixed` count is what says the population was not all singletons.
        _dec_reading: dict = {}
        with contextlib.redirect_stdout(io.StringIO()):
            collect(et, _c7, backlog_out=_dec_reading)
        _dec_corpus, _dec_fold = _dec_reading["corpus"], _dec_reading["fold"]
        _dec = backlog.derive_deciders(_dec_corpus, _dec_fold,
                                       backlog.derive_evidence(_dec_corpus))
        arm("the decided-by SET's minimum is the value the fold itself names, for every ask",
            "mismatch=[] asks=3 mixed=1",
            lambda: "mismatch=%s asks=%d mixed=%d" % (
                [a for a, m in _dec.items()
                 if (min(m) if m else "") != _dec_fold.decided.get(a, "")],
                len(_dec), len([a for a, m in _dec.items() if len(m) > 1])))

        # AC8 — the pinned read, and the tree it must leave alone. THE CONTROL RUNS FIRST and the
        # porcelain is sampled AFTER it, because the control rebuilds the fixture and a sample
        # taken before it would be measuring this arm's own setup as a write by the mode.
        run("git", "add", "-A", cwd=et)
        run("git", "commit", "-q", "-m", "pinned", "--no-verify", cwd=et)
        _ac8 = dict(_ac7)
        _ac8["memory/builds/aFoo/BACKLOG.md"] = _render_backlog_file(
            "aFoo", _ac7_asks + [backlog.render_ask_row(
                "EXMP-aFoo-33", "2026-09-02", "filed after the pin",
                clauses=(_SEEN_HERE, _ACCEPT))], _ac7_rows)
        _c8 = _build_backlog_fixture(et, _ac8, cutoff=_cut)
        _rc, _so8ctl, _se = _read_asks_run(et, _c8, ["--tsv", "--all", "--ready", "EXMP-aFoo-33"])
        arm("the id IS ready in the working tree — the control that says the pin did the work",
            "EXMP-aFoo-33 yes -", lambda: _read_grades(_so8ctl))
        _before = run("git", "status", "--porcelain", cwd=et)
        _rc8, _so8, _se8 = _read_asks_run(et, _c8, ["--tsv", "--ready", "EXMP-aFoo-33", "--at",
                                                    "HEAD"])
        _after_at = run("git", "status", "--porcelain", cwd=et)
        arm("--at grades the PINNED tree: a row filed after it is not filed there",
            "EXMP-aFoo-33 no R1,R2,R4,R5", lambda: _read_grades(_so8))
        arm("--at names the tree its declarations came from, on stderr", "conf pinned at HEAD",
            lambda: _se8)
        _rc8b, _so8b, _se8b = _read_asks_run(et, _c8, [
            "--tsv", "--all", "--ready", "EXMP-aFoo-32", "--target", "aFoo",
            "--live-builds", "aBar"])
        arm("no print mode writes a byte: the porcelain is what it was before either run",
            "at=True modes=True",
            lambda: f"at={_after_at == _before} "
                    f"modes={run('git', 'status', '--porcelain', cwd=et) == _before}")

        # THE PINNED READ'S ONE DEGRADATION, REPORTED. A spec whose header this reader refuses at
        # `<rev>` is absent from the pinned index, and an absent spec moves the status of every ask
        # it closes and therefore moves R2 — so a run that dropped it in silence would hand back a
        # grade over a corpus it never mentioned. The arm exists because a report nobody has ever
        # seen fire is a branch, not a report.
        _bad_spec = dict(_ac8)
        _bad_spec["memory/builds/aBar/spec/2026-09-01-spec-aBar-80.md"] = _render_backlog_spec(
            "EXMP-aBar-80", tail=" · order 0x2")
        _c8d = _build_backlog_fixture(et, _bad_spec, cutoff=_cut)
        run("git", "add", "-A", cwd=et)
        run("git", "commit", "-q", "-m", "bad header", "--no-verify", cwd=et)
        _rc8d, _so8d, _se8d = _read_asks_run(et, _c8d, ["--tsv", "--ready", "EXMP-aFoo-32",
                                                        "--at", "HEAD"])
        arm("a spec header the pinned reader refuses is NAMED on stderr, not dropped in silence",
            "absent from the pinned spec index", lambda: _se8d)
        arm("and the run still answers, at exit 0 — a print mode does not refuse over history",
            "rc=0 rows=1", lambda: f"rc={_rc8d} rows="
                                   f"{len([x for x in _so8d.split(chr(10)) if x.startswith(ASK_TSV_HEAD)])}")

        # AC9 — `--probe`, the ONE path that may execute a filer's bytes.
        def _build_probe_tree(allow, asks, rows=()):
            conf = _build_backlog_fixture(et, _build_env_tree(foo_asks=asks, foo_rows=rows),
                                          cutoff=_cut)
            path = os.path.join(et, ".memory-tree.conf")
            write_text(path, read_text(path) + 'PROBE_ALLOW="' + allow + '"\n')
            run("git", "add", "-A", cwd=et)
            return load_conf(et)

        _RUNNABLE = "git --version"
        _probe_ask = [backlog.render_ask_row(
            "EXMP-aFoo-40", "2026-09-01", "answerable by a command",
            clauses=(("seen", "`memory/builds/aFoo/README.md`@abc1234 run `" + _RUNNABLE + "`"),))]
        _rc, _so9, _se9 = _read_asks_run(et, _build_probe_tree("", _probe_ask),
                                         ["--probe", "EXMP-aFoo-40"])
        arm("a BLANK PROBE_ALLOW refuses every command and names the key that would admit it",
            "REFUSED · PROBE_ALLOW is blank", lambda: _so9)
        _rc, _so9b, _se9b = _read_asks_run(et, _build_probe_tree("git status", _probe_ask),
                                           ["--probe", "EXMP-aFoo-40"])
        arm("a declared entry that does not match refuses, naming the key and what IS declared",
            "no PROBE_ALLOW entry matches `git --version` token for token", lambda: _so9b)
        _rc, _so9c, _se9c = _read_asks_run(et, _build_probe_tree(_RUNNABLE, _probe_ask),
                                           ["--probe", "EXMP-aFoo-40"])
        arm("the two-token entry admits exactly its command, which RUNS and reports its status",
            "RAN · `git --version` · exit 0", lambda: _so9c)
        arm("and the run prints the locator it answered for", "locator pinned", lambda: _so9c)
        # THE MATCHING ARMS RUN NOTHING. They ask `check_probe_command` directly, because what is
        # under test is the decision and a fixture that had to EXECUTE to ask it could only ever
        # test the entries whose programs this node happens to have.
        arm("the match is token EQUALITY, so `python3` never admits `python3x`",
            "no PROBE_ALLOW entry matches",
            lambda: check_probe_command("python3x -V", read_probe_allow(
                {PROBE_ALLOW_KEY: "python3"}))[1])
        arm("a two-token entry refuses the second script", "no PROBE_ALLOW entry matches",
            lambda: check_probe_command("python3 q.py", read_probe_allow(
                {PROBE_ALLOW_KEY: "python3 p.py"}))[1])
        arm("and admits the one it declared", "('python3', 'p.py')",
            lambda: str(check_probe_command("python3 p.py", read_probe_allow(
                {PROBE_ALLOW_KEY: "python3 p.py"}))[0]))
        arm("a path entry never admits a traversal out of it", "no PROBE_ALLOW entry matches",
            lambda: check_probe_command("tools/../x", read_probe_allow(
                {PROBE_ALLOW_KEY: "tools/"}))[1])
        arm("a single-token interpreter entry DOES admit arbitrary code — the stated residual",
            "('python3', '-c', 'anything')",
            lambda: str(check_probe_command("python3 -c anything", read_probe_allow(
                {PROBE_ALLOW_KEY: "python3"}))[0]))
        arm("a shell metacharacter refuses BEFORE the command is split", "which mean something "
            "to a shell",
            lambda: check_probe_command("git --version ; rm -rf .", read_probe_allow(
                {PROBE_ALLOW_KEY: "git"}))[1])
        arm("a newline refuses on the same ground", "which mean something to a shell",
            lambda: check_probe_command("git --version\nrm -rf .", read_probe_allow(
                {PROBE_ALLOW_KEY: "git"}))[1])
        # THE BOUND, over `run_probe` itself and with a SHORT one. The argv is passed as a tuple
        # rather than parsed from a string, which is what lets this arm name an interpreter whose
        # own path carries a space on some nodes and a banned byte on others.
        _sleep = run_probe(et, (sys.executable, "-c", "import time; time.sleep(30)"), 1)
        arm("a command that outlives the bound is killed and reported as NEVER ANSWERED",
            "status=None answered=False", lambda: f"status={_sleep[0]} answered={_sleep[2]}")
        arm("the declared default bound is a positive number of seconds", "True",
            lambda: str(isinstance(PROBE_TIMEOUT_SECONDS, int) and PROBE_TIMEOUT_SECONDS > 0))
        _rc9d, _so9d, _se9d = _read_asks_run(
            et, _build_probe_tree(_RUNNABLE, _probe_ask, rows=[backlog.render_scope_row(
                "EXMP-aFoo-40", (("seen", "`memory/builds/aBar/README.md`@abc1234 run `git log`"),))]),
            ["--probe", "EXMP-aFoo-40"])
        arm("two merged `run` values refuse as AMBIGUOUS and name both rows, running nothing",
            "2 `seen … run` commands", lambda: _se9d)
        arm("the ambiguity refusal names each row and its command", "runs `git log`",
            lambda: _se9d)
        arm("and it puts nothing on stdout", "rc=2 out=''",
            lambda: f"rc={_rc9d} out='{_so9d}'")


    # AC10, AC11 and AC13 — the scaffold, in a repository of its own. Its own, because the command
    # STAGES what it wrote and runs the whole render: an arm sharing the envelope fixture above
    # would leave every later arm grading a tree this one committed to.
    with tempfile.TemporaryDirectory() as scbase:
        sc = os.path.join(scbase, "scaffold")
        os.makedirs(sc)
        _SC_HOME = "memory/builds/aFoo/README.md"
        _sc_cap = int(re.search(r"BUILD_README_ENTRY_CAP_CHARS=(\d+)", read_text(
            os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "check-memory-hygiene.sh"))).group(1))

        def _render_sc_readme(slug):
            return ("---\nslug: " + slug + "\nnode: a\nopened: 2026-09-01\nstreams: tool\n"
                    "roster: EXMP\nids: EXMP-" + slug + "-1\n---\n\n# " + slug + "\n\n"
                    + PLAN_OPEN + "\n" + PLAN_CLOSE + "\n\n" + MARK_OPEN + "\n" + MARK_CLOSE + "\n")

        def _build_sc_tree(asks):
            """The home build every mandate below is filed in, plus the contract registry the
            slot contract refuses to run without. The home README is EXEMPT and the scaffolded one
            is BOUND, which is the whole point: the canon grades the file this command WRITES."""
            return {
                _SC_HOME: _render_sc_readme("aFoo"),
                "memory/builds/aFoo/spec/2026-09-01-spec-aFoo-90.md":
                    _render_backlog_spec("EXMP-aFoo-90"),
                "memory/builds/aFoo/BACKLOG.md": _render_backlog_file("aFoo", asks),
                "memory/" + CONTRACT_REGISTRY:
                    "# the fixture registry\nexempt-pin: 1\n"
                    "!" + _SC_HOME + " - a fixture home build with no authored half\n",
            }

        def _build_sc_ask(seq, text, clauses=(_SEEN_HERE, _ACCEPT), pointer=""):
            return backlog.render_ask_row(f"EXMP-aFoo-{seq}", "2026-09-01", text,
                                          clauses=clauses, pointer=pointer)

        _sc_conf = _build_backlog_fixture(sc, _build_sc_tree(
            [_build_sc_ask(3, "the first mandated ask"),
             _build_sc_ask(4, "the second mandated ask")]))
        run("git", "commit", "-q", "-m", "home", "--no-verify", cwd=sc)
        _SC_SLUG = "zFreshDocket"
        _rc10, _out10 = _read_mode(cmd_new_build, sc, _sc_conf,
                                   {"slug": _SC_SLUG, "asks": ["EXMP-aFoo-3", "-4"]})
        _sc_rel = f"memory/builds/{_SC_SLUG}/README.md"
        _sc_text = read_text(os.path.join(sc, _sc_rel)) if os.path.isfile(
            os.path.join(sc, _sc_rel)) else ""
        _sc_fm = [x for x in _sc_text.split("\n---")[0].split("\n") if ":" in x]
        arm("the scaffold writes its README and exits 0", "rc=0 wrote=True",
            lambda: f"rc={_rc10} wrote={bool(_sc_text)}" if _rc10 == 0
            else f"rc={_rc10} :: {_out10}")
        arm("the mandate collapses to ONE physical `asks:` line, in the authoring notation",
            "[asks: EXMP-aFoo-3..4]",
            lambda: "[" + [x for x in _sc_fm if x.startswith("asks:")][0] + "]")
        arm("the front matter carries the keys a run and the bar both read",
            "['slug: zFreshDocket', 'node: z', 'streams: tool', 'roster: EXMP', 'ids:', "
            "'status: OPEN', 'authorized-by: slug']",
            lambda: str([x for x in _sc_fm if not x.startswith(("opened:", "asks:"))]))
        arm("the `ids:` line is the RENDER's, which owns it — empty on a build no id names yet",
            "[ids:]", lambda: "[" + [x for x in _sc_fm if x.startswith("ids:")][0] + "]")
        arm("the README is BOUND by the contract registry, never exempted into it",
            f"{_sc_rel}\n",
            lambda: "\n".join(x for x in read_text(
                os.path.join(sc, "memory", CONTRACT_REGISTRY)).split("\n")
                if x.strip() == _sc_rel) + "\n")
        arm("the scaffold writes no grant key, so the build it opens can grant nothing", "False",
            lambda: str(any(x.startswith("may:") for x in _sc_text.split("\n"))))
        _rc10c, _out10c = _read_mode(cmd_check, sc, load_conf(sc))
        _rc10f, _out10f = _read_mode(cmd_check_format, sc, load_conf(sc))
        arm("the tree the scaffold left behind passes BOTH bar verbs", "check=0 format=0",
            lambda: f"check={_rc10c} format={_rc10f}" if _rc10c == 0 and _rc10f == 0
            else f"check={_rc10c} format={_rc10f} :: {_out10c} :: {_out10f}")

        # AC13 — the anchor property, through THIS kit's own route, bound to the tree the scaffold
        # just wrote. A generated body naming one id per mandated ask is exactly the shape that
        # would make the new build a SECOND claimant for every ask it was opened to answer.
        import corpus_ids as _sc_cids  # noqa: PLC0415 — deferred exactly as the anchor arms above
        try:
            _sc_anchor = _sc_cids.resolve_anchor(sc)
        except _sc_cids.Problem as _sc_why:
            _sc_anchor = None
            print(f"arm SKIP  the scaffold's anchor arms did not run — {_sc_why}")
            fails.append("the scaffold anchor arms were SKIPPED, so no anchor property held")
        if _sc_anchor is not None:
            _sc_break = "- EXMP-aFoo-3 — the ask"
            arm("no line the scaffold wrote ANCHORS an id, and the file HAS the ids",
                "anchored=[] carries-the-ids=True",
                lambda: f"anchored={[x for x in _sc_text.split(chr(10)) if _sc_anchor(x)]} "
                        f"carries-the-ids={'EXMP-aFoo-3' in _sc_text}")
            arm("the same predicate over the same root DOES answer the break line — the control",
                "EXMP-aFoo-3", lambda: str(_sc_anchor(_sc_break)))

        # AC10's second half — a mandate large enough that an UNWRAPPED body would cross the cap.
        # The ceiling is read off the hygiene engine rather than typed here, because a number typed
        # beside the thing it counts is wrong on the next commit and nobody notices.
        # TWENTY-FIVE, and the number is MEASURED rather than picked: at fifteen the unwrapped
        # body came to roughly 345 characters and slipped under the 350 the hygiene engine
        # declares, so the break that removes the wrap stayed green and this arm proved nothing.
        _sc_many = [str(n) for n in range(10, 35)]
        _sc_conf2 = _build_backlog_fixture(sc, _build_sc_tree(
            [_build_sc_ask(n, f"mandated ask {n}") for n in _sc_many]))
        run("git", "commit", "-q", "-m", "wide", "--no-verify", cwd=sc)
        _SC_WIDE = "zWideDocket"
        _rc10w, _out10w = _read_mode(cmd_new_build, sc, _sc_conf2, {
            "slug": _SC_WIDE, "asks": [f"EXMP-aFoo-{n}" for n in _sc_many]})
        _sc_wide_text = read_text(os.path.join(sc, f"memory/builds/{_SC_WIDE}/README.md"))

        def _measure_entry_lines(text):
            """Every line check 7 would measure: unfenced, and outside the front-matter block."""
            out, fence, inside = [], "", False
            for n, line in enumerate(text.split("\n"), 1):
                if n == 1 and line == "---":
                    inside = True
                    continue
                if inside:
                    inside = line != "---"
                    continue
                mark = "```" if line.lstrip().startswith("```") else (
                    "~~~" if line.lstrip().startswith("~~~") else "")
                if mark:
                    fence = "" if fence == mark else (fence or mark)
                    continue
                if not fence and not line.startswith("#"):
                    out.append(line)
            return out

        arm("a twenty-five-ask mandate scaffolds, and every measured line stays under the cap",
            "rc=0 over=[]",
            lambda: f"rc={_rc10w} over={[len(x) for x in _measure_entry_lines(_sc_wide_text) if len(x) > _sc_cap]}"
            if _rc10w == 0 else f"rc={_rc10w} :: {_out10w}")
        arm("and it WRAPPED: the body naming the asks is more than one line",
            "True",
            lambda: str(len([x for x in _sc_wide_text.split("\n")
                             if x.startswith("EXMP-aFoo-") or "EXMP-aFoo-" in x]) > 2))

        # AC11 — every refusal, each asserted to have written NOTHING.
        def _read_refusal(slug, asks):
            rc, out = _read_mode(cmd_new_build, sc, load_conf(sc), {"slug": slug, "asks": asks})
            return f"rc={rc} folder={os.path.isdir(os.path.join(sc, 'memory', 'builds', slug))} "\
                   f":: {out}"

        arm("an elision is refused BY NAME and the whole list falls with it",
            "rc=1 folder=False", lambda: _read_refusal("zElidedDocket", ["EXMP-aFoo-3...5"]))
        arm("the elision refusal says what it wanted instead", "an elision names no id",
            lambda: _read_refusal("zElidedDocket", ["EXMP-aFoo-3...5"]))
        arm("an id nobody filed is refused, and nothing is written", "rc=1 folder=False",
            lambda: _read_refusal("zUnfiledDocket", ["EXMP-aFoo-3", "EXMP-aFoo-77"]))
        arm("that refusal names the id and the file it looked in", "EXMP-aFoo-77 is filed by no",
            lambda: _read_refusal("zUnfiledDocket", ["EXMP-aFoo-3", "EXMP-aFoo-77"]))
        arm("a slug the all-time probes find is refused", "rc=1",
            lambda: _read_refusal("aFoo", ["EXMP-aFoo-3"]))
        arm("and it says WHICH probe found it", "already touched memory/builds/aFoo/",
            lambda: _read_refusal("aFoo", ["EXMP-aFoo-3"]))
        _sc_conf3 = _build_backlog_fixture(sc, _build_sc_tree(
            [_build_sc_ask(3, "ungradeable", clauses=()),
             _build_sc_ask(4, "ungradeable too", clauses=())]))
        run("git", "commit", "-q", "-m", "nogrades", "--no-verify", cwd=sc)
        arm("a mandate whose every id grades `no` stops at the table, writing nothing",
            "rc=1 folder=False",
            lambda: _read_refusal("zUngradedDocket", ["EXMP-aFoo-3", "-4"]))
        arm("and the readiness table printed BEFORE the refusal", "asks: 2 examined",
            lambda: _read_refusal("zUngradedDocket", ["EXMP-aFoo-3", "-4"]))
        _sc_conf4 = _build_backlog_fixture(sc, _build_sc_tree(
            [_build_sc_ask(3, "granted", clauses=(_SEEN_HERE, _ACCEPT,
                                                  ("may", "`tools/push-main.sh`")))]))
        run("git", "commit", "-q", "-m", "granted", "--no-verify", cwd=sc)
        _rc11, _out11 = _read_mode(cmd_new_build, sc, _sc_conf4,
                                   {"slug": "zGrantedDocket", "asks": ["EXMP-aFoo-3"]})
        arm("a mandate over a GRANTED ask still scaffolds a README with no grant key",
            "rc=0 may=False",
            lambda: f"rc={_rc11} may=" + str(any(
                x.startswith("may:") for x in read_text(os.path.join(
                    sc, "memory/builds/zGrantedDocket/README.md")).split("\n")))
            if _rc11 == 0 else f"rc={_rc11} :: {_out11}")


    # ---------------------------------------------------- the example family (TOOL-dDerivedDocket-51)
    # DECLARED BY A SCRATCH CONF AND BY NOTHING TRACKED. The sibling kit's id grammar is an ALLOWLIST
    # of the conf's declared families, so before a fixture declared the example family an `EXMP` id
    # anchored nothing anywhere — and a criterion asserting that a generated body anchors nothing was
    # answered by the allowlist rather than by the generator, green before the generator wrote a line.
    # These arms make that assertion reachable INSIDE a fixture while this repository's own corpus
    # keeps the property the example family exists for: an example id in a tracked spec still anchors
    # nothing, defines nothing and is cited by nobody.
    with tempfile.TemporaryDirectory() as exbase:
        _ex_disc, _, _ex_fam = EXAMPLE_ROW.partition(":")
        _ex_id = f"{_ex_fam}-aFoo-3"
        #: The staged break of the spec's §4, kept as a value so the control arm below and the RED
        #: that was observed by hand are the SAME line and cannot drift apart.
        _ex_break = f"- {_ex_id} — the ask"

        def _example_build(root: str) -> dict:
            """The build README `TOOL-dDerivedDocket-15`'s scaffold will write from example asks.

            Written by hand here because that unit is order 15 and lands after this one. The shape
            is the scaffold's and the point is the front matter: `streams` carries the pair's
            discipline half and `roster` its family half, which is exactly the two declarations this
            unit adds — so a fixture holding one of them trades one refusal for the other.
            """
            d = os.path.join(root, "memory", "builds", "aFoo")
            os.makedirs(os.path.join(d, "spec"), exist_ok=True)
            write_text(os.path.join(d, "spec", "2026-08-01-spec-aFoo-1.md"),
                       f"# {_ex_id} — an ask\n\n**Status:** OPEN · rev-1 · 2026-08-01 · node a · "
                       f"Tier-2 · base 0123abcd\n")
            write_text(os.path.join(d, "README.md"), "\n".join(
                ["---", "slug: aFoo", "node: a", "opened: 2026-08-01",
                 f"streams: {_ex_disc}", f"roster: {_ex_fam}", f"ids: {_ex_id}", "---",
                 "", "# aFoo", "", MARK_OPEN, MARK_CLOSE]) + "\n")
            run("git", "add", "-A", cwd=root)
            return load_conf(root)

        # AC1 — ONE carrier, read back OFF DISK. The assertion never respells the pair: it splits the
        # constant and looks for each half in the field the fixture wrote it into, so a second
        # spelling at the writer reds HERE rather than surfacing three arms later as a refusal whose
        # cause is two files away.
        ex1 = os.path.join(exbase, "declared"); os.makedirs(ex1)
        _fixture(ex1, spec_status="OPEN", example_family=True)
        ex2 = os.path.join(exbase, "undeclared"); os.makedirs(ex2)
        _fixture(ex2, spec_status="OPEN")
        # BOTH CONFS ARE READ OFF DISK, from a real `_fixture` call, and never from the renderer
        # they share. Reading the renderer graded the wrong carrier: a staged break that defaulted
        # the FIXTURE HELPER's keyword ON left these two arms green, because the renderer's own
        # default had not moved. The arm has to see what the helper actually wrote.
        _ex_on = read_text(os.path.join(ex1, ".memory-tree.conf"))
        _ex_off = read_text(os.path.join(ex2, ".memory-tree.conf"))
        _ex_written: dict = {"DISCIPLINES": "", "FAMILIES": ""}
        parse_conf(_ex_on, _ex_written)
        arm("the opted-in fixture declares BOTH halves of EXAMPLE_ROW, read back off disk", "True",
            lambda: str(_ex_disc in _ex_written["DISCIPLINES"].split()
                        and EXAMPLE_ROW in _ex_written["FAMILIES"].split()))

        # AC2 — the default is the control. OFF must be the bytes this helper wrote before the
        # keyword existed, or every arm that never asked for the example family is silently graded
        # by a different alternation than the one its assertions were written against.
        arm("the keyword omitted writes the conf this helper wrote before it existed",
            'MEMORY_ROOT=memory\nDISCIPLINES="arch"\nFAMILIES="arch:ARCH"\n',
            lambda: _ex_off)
        arm("the example family reaches no fixture that did not ask for it", "False",
            lambda: str(_ex_fam in _ex_off or _ex_disc in _ex_off))

        # AC3 — what the declaration BUYS, as the three readers it unblocks. The order is the
        # generator's own: streams is validated before roster, so the streams refusal HIDES the
        # roster one until both halves are declared, and an arm asserting only that SOME refusal
        # fired would pass over a fixture carrying half the pair with its real subject unreachable.
        _ex_conf = _example_build(ex1)
        _ex_rc_w, _ex_out_w = _read_mode(cmd_write, ex1, _ex_conf)
        _ex_rc_c, _ex_out_c = _read_mode(cmd_check, ex1, _ex_conf)
        arm("a build README filed under the example family renders and re-reads clean",
            "write=0 check=0", lambda: f"write={_ex_rc_w} check={_ex_rc_c}")
        _ex_rc2, _ex_out2 = _read_mode(cmd_check, ex2, _example_build(ex2))
        arm("with the keyword omitted the STREAMS refusal fires, naming the value and the enum",
            f"streams value '{_ex_disc}' is outside the DISCIPLINES enum", lambda: _ex_out2)
        ex3 = os.path.join(exbase, "halfway"); os.makedirs(ex3)
        _fixture(ex3, spec_status="OPEN")
        write_text(os.path.join(ex3, ".memory-tree.conf"),
                   f'MEMORY_ROOT=memory\nDISCIPLINES="arch {_ex_disc}"\nFAMILIES="arch:ARCH"\n')
        _ex_rc3, _ex_out3 = _read_mode(cmd_check, ex3, _example_build(ex3))
        arm("with the DISCIPLINE half alone the ROSTER refusal fires, naming the value and the set",
            f"roster value '{_ex_fam}' is outside the FAMILIES set", lambda: _ex_out3)

        # AC4 — the anchor property, through THIS kit's own route and bound to the fixture's root.
        # `resolve_anchor` raises rather than returning None for an absent or outdated sibling kit,
        # because None is also what a line that anchors nothing returns and every caller would then
        # read an uninstalled kit as a clean corpus.
        import corpus_ids as _cids  # noqa: PLC0415 — deferred exactly as the anchor arms above are
        try:
            _ex_anchor = _cids.resolve_anchor(ex1)
            _ex_anchor_off = _cids.resolve_anchor(ex2)
        except _cids.Problem as _ex_why:
            _ex_anchor = _ex_anchor_off = None
            print(f"arm SKIP  the example-family anchor arms did not run — {_ex_why}")
            fails.append("the example-family anchor arms were SKIPPED, so no anchor property held")
        if _ex_anchor is not None:
            _ex_lines = read_text(
                os.path.join(ex1, "memory", "builds", "aFoo", "README.md")).split("\n")
            # THE POPULATION IS ASSERTED NON-EMPTY IN THE SAME VALUE. An empty line list yields the
            # same `[]` a clean README does, which is the vacuous-selector shape this whole unit is
            # about — so the arm also says the README CARRIES the id (its `ids:` line does), and the
            # finding is then "the id is in this file and no line of it anchors" rather than "the
            # scan found nothing", which is what an unrendered or unread file would also report.
            arm("no line of the rendered example build README ANCHORS an id, and it HAS the id",
                "anchored=[] carries-the-id=True",
                lambda: f"anchored={[x for x in _ex_lines if _ex_anchor(x)]} "
                        f"carries-the-id={any(_ex_id in x for x in _ex_lines)}")
            # THE CONTROL, and the reason the arm above is evidence rather than a tautology: the
            # same predicate over the same root DOES answer the break line. Observed RED once by
            # hand with that line in the README body, per the spec's §4.
            arm("the fixture's own grammar DOES anchor the break line — the control", _ex_id,
                lambda: str(_ex_anchor(_ex_break)))
            # AC7 in fixture form: a tree that never declared the family anchors nothing in the very
            # line the declaring tree answers. That is the two-tree property this unit rests on, and
            # it is asserted over a SECOND root rather than assumed from the tracked conf.
            arm("a tree that did not declare the family anchors nothing in that same line", "None",
                lambda: str(_ex_anchor_off(_ex_break)))

    # TOOL-dDerivedDocket-53 — `read_conf_at_rev`. ONE fixture repository, four commits, because the
    # property under test is a DIFFERENCE BETWEEN REVS and a single-commit fixture cannot hold one.
    # No arm below reads this repository's own conf: an arm satisfied by whatever gov happens to
    # declare today would be green over a reader that never looked at the rev at all.
    with tempfile.TemporaryDirectory() as cbase:
        cx = os.path.join(cbase, "pinned")
        os.makedirs(cx)
        run("git", "init", "-q", ".", cwd=cx)
        run("git", "config", "user.email", "t@t.test", cwd=cx)
        run("git", "config", "user.name", "t", cwd=cx)

        def _build_conf_commit(label: str) -> str:
            run("git", "add", "-A", cwd=cx)
            run("git", "commit", "-q", "-m", label, "--no-verify", cwd=cx)
            return run("git", "rev-parse", "HEAD", cwd=cx).strip()

        write_text(os.path.join(cx, "seed.txt"), "a tree that predates the conf entirely\n")
        _c_noconf = _build_conf_commit("no conf blob at all")
        write_text(os.path.join(cx, ".memory-tree.conf"),
                   "# every line here is a comment\n\n   \n# and not one of them declares a key\n")
        _c_silent = _build_conf_commit("a conf blob that declares nothing")
        write_text(os.path.join(cx, ".memory-tree.conf"),
                   'MEMORY_ROOT=memory-old\nASK_CUTOFF="2026-01-01"\n')
        _c_old = _build_conf_commit("the older declaration")
        write_text(os.path.join(cx, ".memory-tree.conf"),
                   'MEMORY_ROOT=memory-new\nASK_CUTOFF="2026-09-01"\n')
        _c_new = _build_conf_commit("the newer declaration, which the working tree also holds")

        def _read_pinned_conf(rev: str) -> tuple:
            """(conf, stderr) for one pinned read, with S3's notice captured off the suite's own
            stream so an arm can assert on it instead of it decorating the run."""
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                conf = read_conf_at_rev(cx, rev)
            return conf, err.getvalue()

        def _read_conf_refusal(rev: str) -> str:
            """One refusal's text with the REV ITSELF neutralised, so the distinctness arm below
            measures the WORDING and not the argument. Comparing the raw messages would be vacuous:
            every refusal embeds its own rev, so any two of them differ whatever they say, and three
            copies of one sentence would read as three distinct texts."""
            try:
                read_conf_at_rev(cx, rev)
            except Problem as exc:
                return str(exc).replace(rev, "<rev>").replace(rev[:12], "<sha>")
            return "NO REFUSAL"

        # AC1 — and it is the CONTRAST that makes it evidence. A reader that joined the key's path
        # to the working-tree root returns `memory-new` for both halves of this one value, which is
        # exactly the shape this unit exists to remove.
        arm("a pinned read takes its declarations from the REV, not from the checkout",
            "pinned=memory-old working=memory-new",
            lambda: f"pinned={_read_pinned_conf(_c_old)[0]['MEMORY_ROOT']} "
                    f"working={load_conf(cx)['MEMORY_ROOT']}")
        arm("a second key at the same older rev is pinned too, not just the first",
            "2026-01-01", lambda: _read_pinned_conf(_c_old)[0]["ASK_CUTOFF"])

        # AC2 — the three refusals. Each names the rev and the path, and none of them degrades to
        # the working tree, which would still read as pinned.
        arm("a rev that resolves to nothing is a named refusal", "resolves to no commit",
            lambda: read_conf_at_rev(cx, "deadbeef" * 5))
        arm("a rev whose tree carries no conf blob is a named refusal",
            "carries no .memory-tree.conf blob", lambda: read_conf_at_rev(cx, _c_noconf))
        arm("a conf blob that declares nothing is a named refusal, not a parse to the defaults",
            "yields zero declarations", lambda: read_conf_at_rev(cx, _c_silent))
        _c_texts = [_read_conf_refusal("deadbeef" * 5), _read_conf_refusal(_c_noconf),
                    _read_conf_refusal(_c_silent)]
        # THE COUNT OF REFUSALS IS IN THE SAME VALUE as the count of distinct texts, because three
        # reads that all returned a conf would also be "one distinct text" and would pass a
        # distinctness arm that only compared strings.
        arm("the three refusal texts are distinct from one another", "distinct=3 refused=3",
            lambda: f"distinct={len(set(_c_texts))} "
                    f"refused={sum(1 for t in _c_texts if t != 'NO REFUSAL')}")

        # AC3 — the source notice, on stderr, naming the rev. stdout is asserted EMPTY in the same
        # value: a notice that reached stdout would join a machine-read projection there.
        _c_out, _c_err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(_c_out), contextlib.redirect_stderr(_c_err):
            read_conf_at_rev(cx, _c_new)
        arm("the source notice names the rev, on stderr, and stdout stays empty",
            "notice=True names-rev=True stdout=''",
            lambda: f"notice={'conf pinned at' in _c_err.getvalue()} "
                    f"names-rev={_c_new[:12] in _c_err.getvalue()} "
                    f"stdout={_c_out.getvalue()!r}")

        # AC4 — S5's unchanged working-tree path, asserted on its own rather than only as the
        # contrast above. `load_conf` reads the checkout and nothing about it moved.
        arm("the working-tree read still answers from the checkout", "memory-new",
            lambda: load_conf(cx)["MEMORY_ROOT"])
        # THE SEED IS RESPELLED IN TWO PLACES because S4 keeps `load_conf`'s bytes, so the drift
        # that costs is held here instead of by a shared constant: `load_conf` over a root with no
        # conf file IS the seed, and the pinned read's dict must be it plus what the blob declared.
        _c_bare = os.path.join(cbase, "bare")
        os.makedirs(_c_bare)
        _c_defaults = load_conf(_c_bare)
        _c_pinned_new = _read_pinned_conf(_c_new)[0]
        _c_undeclared = ("DISCIPLINES", "FAMILIES")
        # S1's one-parser property, over the bytes that actually split two readers of one file. A
        # SECOND fixture, because this conf must be what the working tree holds AND what the blob
        # holds, and the repository above pins `memory-new` at both. `core.autocrlf` is turned OFF
        # in it: the global setting is on, and it would fold the CRLF out of the blob before the
        # arm ever saw it.
        cy = os.path.join(cbase, "awkward")
        os.makedirs(cy)
        run("git", "init", "-q", ".", cwd=cy)
        run("git", "config", "user.email", "t@t.test", cwd=cy)
        run("git", "config", "user.name", "t", cwd=cy)
        run("git", "config", "core.autocrlf", "false", cwd=cy)
        # WRITTEN AS BYTES, not through `write_text`, which would normalise the very thing under
        # test. CRLF endings, a LONE CR mid-file, and a utf-8 value outside ASCII: the first is the
        # control, the second is what universal newlines turns into a line break, and the third is
        # what a locale decode mis-reads on a node not in UTF-8 mode.
        with open(os.path.join(cy, ".memory-tree.conf"), "wb") as _c_fh:
            _c_fh.write(b'MEMORY_ROOT=m\xc3\xa9moire\r\nASK_CUTOFF="2026-01-01"\r\nA=1\rB=2\n')
        run("git", "add", "-A", cwd=cy)
        run("git", "commit", "-q", "-m", "an awkward conf", "--no-verify", cwd=cy)
        _c_odd_head = run("git", "rev-parse", "HEAD", cwd=cy).strip()
        _c_odd_err = io.StringIO()
        with contextlib.redirect_stderr(_c_odd_err):
            _c_odd_pinned = read_conf_at_rev(cy, _c_odd_head)
        _c_odd_tree = load_conf(cy)
        arm("the pinned read and the working-tree read agree on a conf built to split them",
            "same=True keys=['A', 'ASK_CUTOFF', 'DISCIPLINES', 'FAMILIES', 'MEMORY_ROOT']",
            lambda: f"same={_c_odd_pinned == _c_odd_tree} keys={sorted(_c_odd_pinned)}")

        arm("the pinned reader's seed is load_conf's seed, key for key and value for value",
            "extra=['ASK_CUTOFF'] missing=[] undeclared-agree=True",
            lambda: f"extra={sorted(set(_c_pinned_new) - set(_c_defaults))} "
                    f"missing={sorted(set(_c_defaults) - set(_c_pinned_new))} "
                    f"undeclared-agree="
                    f"{all(_c_pinned_new[k] == _c_defaults[k] for k in _c_undeclared)}")

    # THE SIBLING MODULE'S OWN ARMS RUN HERE, inside this leg, rather than as a leg of their own.
    # `backlog.py` is a LIBRARY with no bar leg and no adopter-visible verb; a second leg for it
    # would be one more row in the manifest for a file this one already imports. Its arms print
    # their own lines and hand back the labels that failed, so a red there is a red here, named.
    fails += [f"backlog: {label}" for label in backlog.run_arms()]

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
                    "--report", "--bump", "--asks", "--new-build"):
        print("usage: gen_build_index.py "
              "[--check|--write|--check-format|--survey|--report|--bump|"
              "--print-bindings|--asks|--new-build|--selftest]")
        return 2
    try:
        root = run("git", "rev-parse", "--show-toplevel").strip()
    except Exception:  # noqa: BLE001
        print("build-index: not a git repo")
        return 2
    conf = load_conf(root)
    if mode == "--print-bindings":
        return cmd_print_bindings(root, conf)
    # `--asks` IS DISPATCHED OUTSIDE THE HANDLER BELOW, which prints its message to stdout. That is
    # right for every other mode and wrong for this one, whose stdout is a value a program parses:
    # a refusal printed there is a decode error rather than a refusal. `cmd_asks` owns all of its
    # own error paths and puts every one of them on stderr.
    if mode == "--asks":
        try:
            args = read_asks_args(argv[2:])
        except Problem as exc:
            print(f"build-index: {exc}", file=sys.stderr)
            return 2
        return cmd_asks(root, conf, args)
    try:
        if mode == "--new-build":
            return cmd_new_build(root, conf, read_new_build_args(argv[2:]))
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
