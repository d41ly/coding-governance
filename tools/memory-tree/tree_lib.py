#!/usr/bin/env python3
"""tree_lib.py — the helpers two or more memory-tree engines share, and nothing else.

TOOL-aRepatriatedFork-9. `check-arms.py`, `row_grammar.py` and `gotchas.py` used to import these from
`corpus_ids.py` and `gen_build_index.py`, which made those two files a hard prerequisite of every
engine beside them. At an adopter whose copies of those two are its own programs — adopter ic, measured —
both gov engines died on import with an `ImportError`, so a fork of one file forced a fork of three.
The helpers live here now, and the two modules that defined them re-import them, so every caller
that reaches them through the old name keeps working.

WHAT BELONGS HERE: a name at least two engines in this directory read. A name one engine owns stays
in that engine; this is a seam, not a utility drawer. A shared name's helpers live beside it, because
this module imports no engine: `read_bindings` brought the record-kind, id-token and text readers it
calls (TOOL-dTrueNorth-29 S2). `row_grammar.py --selftest` carries the arm that refuses a sibling
engine importing from `corpus_ids` or `gen_build_index` again.

The module name follows the codebase-map kit's `map_lib.py` and the runlog kit's `runlog_lib.py`.
"""
from __future__ import annotations

import os
import pathlib
import re
import subprocess

# The lifecycle vocabulary, one declaration for the index generator's front-matter check, check 24's
# rotation grading and the backlog-row census.
STATUS_TOKENS = ("OPEN", "SPECCED", "INPROGRESS", "BLOCKED", "DEFERRED", "CLOSED", "WONTDO")
# What the INDEX generator and check 24 call terminal: a `DEFERRED` build or row stays in the live
# index, because parked work is still work somebody owes.
TERMINAL = ("CLOSED", "WONTDO")
# What the backlog-row CENSUS calls terminal, and it is DELIBERATELY WIDER (the unit's section 8 F1,
# owner-resolved). `memory/TEMPLATE-SPEC.md` names CLOSED / DEFERRED / WONTDO as the terminal set a
# spec header flips to, and a report-only census counting a deferred row as outstanding work would
# overstate the debt. The index answers "what must stay visible", the census "what is still owed";
# two questions, two tuples, and both are declared HERE so the difference is one decision in one place
# rather than two modules that happen to disagree.
CENSUS_TERMINAL = ("CLOSED", "WONTDO", "DEFERRED")

# A gotcha record's front-matter block: `---` at line 1, the column-0 `key: value` lines, `---`.
# Read by `gotchas.py` (checks 17-19, which grade the keys) and by `row_grammar.py`'s record
# enumeration (check 27, which ranks a record by its `description`). TOOL-aGraftedHelix-9 moved it
# here so the kit holds one copy: two engines spelling one block are free to disagree on where a
# record's front matter ends.
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def kit_rel() -> str:
    """This kit's directory relative to the enclosing checkout, DERIVED and never spelled.

    Written into generated artifacts and into remedy strings an operator copies, so a hardcoded
    prefix lands a dead path in an adopter's tree. Falls back to the bare kit name when the module
    sits outside any checkout (a test fixture, an odd install); the result is a pointer, never a gate
    input.
    """
    here = pathlib.Path(__file__).resolve().parent
    for anc in [here] + list(here.parents):
        if (anc / ".git").exists():
            try:
                return here.relative_to(anc).as_posix()
            except ValueError:
                break
    return here.name


def parse_conf_line(line: str):
    """One `.memory-tree.conf` line -> `(key, value)`, or `None` for a line that declares nothing.

    TOOL-aScouredKit-19. SIX readers in this kit held this body and the shell gate SOURCES the same
    file in bash, so any spelling bash accepts and the python half mis-reads REMOVES coverage while
    the gate stays green. Reproduced: `MEMORY_ROOT=memory   # note` took `gotchas.py --check` from
    rc=1 to rc=0 over an identical planted violation, because the python half then walked a directory
    that does not exist. Coverage removed, not failed closed.

    TWO SPELLINGS BASH ACCEPTS THAT THE OLD BODY DID NOT, both measured against `set -a; . conf`:

        MEMORY_ROOT=memory   # note   ->  memory        (an unquoted inline comment is stripped)
        export FAMILIES="TOOL DEPL"   ->  TOOL DEPL     (the export prefix is not part of the key)

    AND ONE IT MUST NOT BREAK, which is why the comment strip is not unconditional:

        QUOTED="a # b"                ->  a # b         (a `#` inside quotes is DATA)

    Stripping `#` unconditionally would turn that into `a`, a silent wrong value where today's bug is
    at least a loud directory miss. So the strip runs BEFORE the quote peel and only on an unquoted
    `#` that begins a word, which is bash's own rule.

    NOT a general shell grammar, and deliberately: command substitution, parameter expansion, line
    continuations and quoted whitespace are all legal bash and none is in scope. These two are the
    spellings an adopter actually writes and the ones the kit's own example neither shows nor forbids.
    """
    line = line.strip()
    if not line or line.startswith("#") or "=" not in line:
        return None
    k, _, v = line.partition("=")
    k = k.strip()
    if k.startswith("export ") or k.startswith("export\t"):
        k = k[len("export"):].strip()
    if not k:
        return None
    # TOOL-aRepatriatedFork-38 rev-3 (the closing review's C4): the WORD rule, decided on the text
    # right after `=`. Whitespace there ends the assignment, so `K= x` and `K=   # note` are empty in
    # bash; a `#` begins a comment only AFTER whitespace, so `K=#x` keeps `#x`.
    if v[:1].isspace():
        return k, ""
    v = v.strip()
    # A QUOTED VALUE AND AN UNQUOTED ONE NEED DIFFERENT SCANS, and the first cut of this function
    # had only the second — so `KEY="v"  # note` kept both the comment AND a stray quote, which is
    # live on five lines of this kit's own shipped `.memory-tree.conf.example`. Found by the closing
    # diff review, reproduced against `set -a; . conf`.
    #
    # QUOTED: take the text between the opening quote and its MATCH, then treat only the remainder
    # as comment territory. That is what makes `Q="a # b"` keep its `#` while `Q="a"  # note` loses
    # its trailing one — the two directions this parser has to get right at once.
    if v[:1] in ("'", '"'):
        q = v[0]
        end = v.find(q, 1)
        if end >= 0:
            return k, v[1:end]
        # An UNTERMINATED quote is not something to guess at. Fall through to the unquoted scan,
        # which is what the old body did for every value, so this is no worse than before for a
        # spelling bash itself would reject.
    # UNQUOTED: a `#` that FOLLOWS whitespace starts a comment. Position 0 is not one: the
    # leading-whitespace case returned above, so a `#` there is the first character of the word.
    cut = -1
    for i, ch in enumerate(v):
        if ch == "#" and i > 0 and v[i - 1].isspace():
            cut = i
            break
    if cut >= 0:
        v = v[:cut].strip()
    return k, v.strip('"').strip("'")


def parse_conf(text: str, conf: dict) -> dict:
    """Merge every declaration in `text` into `conf`, which carries the caller's OWN defaults.

    The defaults stay per-reader on purpose: they differ (`CHARTER` and the pins for corpus_ids, the
    universal budget for gotchas, the arms floors for check-arms), and one merged dict would give
    every reader keys it has no use for and hide which reader depends on which.
    """
    for line in text.split("\n"):
        kv = parse_conf_line(line)
        if kv is not None:
            conf[kv[0]] = kv[1]
    return conf


def unfenced_lines(text: str):
    """Yield (lineno, line) for every line OUTSIDE a fenced block, then the open fence's line.

    The final yield is `(opened_at, None)` when the document ends inside a fence, and nothing when it
    does not. A caller that only wants the text ignores it; a caller that must REFUSE a document it
    could not fully read needs it, and no reader in either kit had it — the shell `_unfenced` and the
    index generator both ended silently with the fence still open, dropping every later line at
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


#: The declared-gap citation form (TOOL-aMendedFleet-26): this prefix written immediately before an
#: id says "this id has no record", so check 14 does not count it as an orphan and the roster
#: derivation does not file it on its slug's build. Spelled here and nowhere else.
MISSING_PREFIX = "missing:"


def scan_missing_citations(text: str, id_re) -> tuple[list, str]:
    """`(ids, blanked)`: every id written in the `missing:` form, and `text` with each form and its
    id overwritten by spaces of the same length, so offsets and line numbers still hold.

    `id_re` is the CALLER's own compiled id regex, so the form needs no second id grammar: each
    reader recognises a marked id by exactly the predicate it already uses for a cited one. A plain
    regex cannot tell the two apart on its own, because the colon is a word boundary.
    """
    pat = re.compile(re.escape(MISSING_PREFIX) + "(?:" + id_re.pattern + ")", id_re.flags)
    ids = [mm.group(0)[len(MISSING_PREFIX):] for mm in pat.finditer(text)]
    if not ids:
        return ids, text
    return ids, pat.sub(lambda mm: " " * len(mm.group(0)), text)


def build_spec_path_re(memory_root: str):
    """The path half of `parse_spec_h1`: a build's `spec/` folder, at any depth. Exposed so a caller
    walking a whole tree can skip reading a file the predicate would refuse on its path alone."""
    return re.compile(r"^" + re.escape(memory_root) + r"/builds/[^/]+/spec/")


def parse_spec_h1(rel: str, text: str, memory_root: str, families) -> tuple[int, str] | None:
    """`(lineno, id)` of the H1 that DEFINES a unit id in a spec file, or None.

    THE one predicate for "which id does this spec define" (TOOL-aRepatriatedFork-40). Two kits read
    it: `gen_build_index.spec_ids`, the index generator's resolution set, and the memory-recall
    kit's `extract_records`, which anchors a record on the same line. The recall kit reaches it
    through the sibling-kit resolver because it `requires` this kit; a copy of the regex there is
    the two-answers-to-one-question class.

    `rel` is repo-relative and must sit under `<memory_root>/builds/<slug>/spec/`, at any depth. The
    first UNFENCED H1 whose first token is `<FAMILY>-<slug>-<seq>` wins, one per file. `families`
    is the prefixes alone (`TOOL`, not `tooling:TOOL`).
    """
    if not build_spec_path_re(memory_root).match(rel):
        return None
    alt = "|".join(sorted(set(families))) or "(?!)"
    pat = re.compile(r"^#\s+[`*]*(?P<id>(?:" + alt + r")-[A-Za-z0-9]+-\d+)\b")
    for n, line in unfenced_lines(text):
        if line is None:
            continue
        m = pat.match(line)
        if m:
            return n, m.group("id")
    return None


def build_git_env() -> dict:
    """The environment every pinned git call in this kit runs under — the kit's ONE pin policy.

    `GIT_GRAFT_FILE=/dev/null` is the spelling the unattended kit's history leg uses and it works
    under Git for Windows, whose MSYS layer maps the name. A graft file re-parents commits, so
    without this pin every ancestry answer could be honest about a sha and wrong about what that sha
    means. Callers add `--no-replace-objects` to the argv. Read by `transition_audit.py` and
    `routed_commits.py`; it moved here from the first when the second arrived (TOOL-aRoutedQuill-3).
    """
    env = dict(os.environ)
    env["GIT_GRAFT_FILE"] = "/dev/null"
    return env


#: What a git reader of this kit must not inherit, in TWO HALVES. ONE list for the kit: it moved here
#: from `gen_build_index.py`, which re-imports it, when the readers below became its second caller
#: (TOOL-dTrueNorth-20), and every runner that reads it strips both halves.
#:
#: The EIGHT location variables are the ones git EXPORTS to a hook, which then reach any subprocess
#: that hook starts: a reader started from a hook in a linked worktree inherits a `GIT_DIR` naming a
#: different tree than the one it was asked about, and reads it silently. TOOL-dRetiredFork-2,
#: absorbed from adopter nc `nc carve-out 16/20`, taken VERBATIM from gov's own hook-side scrub at
#: `.githooks/pre-push:100`, because these are two halves of ONE defect and a second list is where
#: they drift apart. That hook list is a subset of this one, unchanged.
#:
#: The FOUR pathspec-mode variables are taken VERBATIM from gov's own unset at
#: `<prefix>/check-playbook-parity.sh:334` (TOOL-aDistilledCharter-7 G6). Git exports none of them to a
#: hook, but a caller's own environment can carry one, and `GIT_LITERAL_PATHSPECS` turns every
#: `:(glob)` pathspec this kit reads into a literal name that matches nothing: the log answers empty,
#: exit 0, and a join over it reports green over a population it never read (TOOL-dTrueNorth-23).
GIT_ENV_LEAKS = (
    "GIT_DIR",
    "GIT_WORK_TREE",
    "GIT_INDEX_FILE",
    "GIT_OBJECT_DIRECTORY",
    "GIT_ALTERNATE_OBJECT_DIRECTORIES",
    "GIT_COMMON_DIR",
    "GIT_NAMESPACE",
    "GIT_PREFIX",
    "GIT_LITERAL_PATHSPECS",
    "GIT_GLOB_PATHSPECS",
    "GIT_NOGLOB_PATHSPECS",
    "GIT_ICASE_PATHSPECS",
)


def read_git_output(root, argv, stdin=None) -> bytes:
    """A git command's stdout as bytes, run at `root` under `build_git_env` less `GIT_ENV_LEAKS`, or
    `OSError` naming the command and git's first stderr line, or why it could not start. A caller
    reading through it never passes a failed call for an empty answer; each turns the error into its
    own named refusal.

    The four pathspec-mode variables are stripped with the location ones, because the caller's
    environment is not the reader's: under an ambient `GIT_LITERAL_PATHSPECS` a `:(glob)` pathspec
    matches nothing and git still exits 0, so the empty answer would be read as the true one, which
    no refusal above can catch (TOOL-dTrueNorth-23)."""
    cmd = ("git", *argv)
    shown = " ".join(cmd)
    env = {k: v for k, v in build_git_env().items() if k not in GIT_ENV_LEAKS}
    try:
        done = subprocess.run(cmd, cwd=root, input=stdin, capture_output=True, env=env)
    except OSError as exc:
        raise OSError(f"`{shown}` could not start: {exc}") from None
    if done.returncode:
        first = next((ln.strip() for ln in done.stderr.decode("utf-8", "replace").splitlines() if ln.strip()),
                     "git printed nothing on stderr")
        raise OSError(f"`{shown}` exited {done.returncode}: {first}")
    return done.stdout


def read_adding_commits(root, pathspec, wanted) -> dict:
    """`{path: sha}`, the commit that ADDED each path of `wanted`, the OLDEST where a path was added
    twice, from ONE `git log --reverse --no-renames --diff-filter=A` at HEAD over ONE glob `pathspec`.

    THE one adding-commit reader (TOOL-dTrueNorth-20 S32): the audit-writer test and the deviation
    join's pin anchors both call it, so the two cannot disagree on a record deleted and re-added. The
    argv is constant whatever `wanted` holds, never the paths themselves (TOOL-dTrueNorth-19 S1); every
    add outside `wanted` is ignored. A path with no add under the pathspec, staged and not committed
    say, is absent from the answer. A failed git call is `OSError` naming it; an empty `wanted` makes
    no call.
    """
    wanted = set(wanted)
    if not wanted:
        return {}
    log = read_git_output(root, ("log", "--no-renames", "--diff-filter=A", "--reverse", "--format=%x00%H",
                                  "--name-only", "--", pathspec))
    added: dict = {}
    for chunk in log.decode("utf-8", "replace").split("\x00")[1:]:
        sha, _, names = chunk.partition("\n")
        for name in names.split("\n"):
            name = name.rstrip("\r")
            if name in wanted:
                added.setdefault(name, sha.strip())      # oldest first, so the first add seen is kept
    return added


def read_blobs_at(root, requests) -> dict:
    """`{(rev, path): text, or None}` for every `(rev, path)` pair, in ONE `git cat-file --batch`.

    THE one `<rev>:<path>` bytes reader (TOOL-dTrueNorth-20 S33). THE STREAM IS BYTES: each body is
    sliced by its header's byte size before it is decoded, because a stream decoded first is shorter
    than its sizes after any multi-byte character and cuts the next blob short; then it is decoded as
    UTF-8 with CRLF folded, as a working-tree read is. None for an object the rev does not hold
    (`missing`, `ambiguous`), for one that is not a blob, its body skipped so the next header is read
    where it starts, and for one that is not UTF-8. A failed call, a stream ending before a request's
    header, or a header of no known shape is `OSError` naming it, never a partial answer.
    """
    requests = list(dict.fromkeys((str(rev), str(path)) for rev, path in requests))
    if not requests:
        return {}
    data = read_git_output(root, ("cat-file", "--batch"),
                            "".join(f"{rev}:{path}\n" for rev, path in requests).encode("utf-8"))
    out: dict = {}
    at = 0
    for rev, path in requests:
        end = data.find(b"\n", at)
        if end < 0:
            raise OSError(f"`git cat-file --batch` ended before {rev}:{path}, so its blob cannot be read")
        head, at = data[at:end], end + 1
        if head.endswith((b" missing", b" ambiguous")):
            out[(rev, path)] = None
            continue
        fields = head.rsplit(b" ", 2)
        if len(fields) != 3 or not fields[2].isdigit():
            raise OSError(f"`git cat-file --batch` answered `{head.decode('utf-8', 'replace')}` for {rev}:{path}, "
                          "so its blob cannot be read")
        size = int(fields[2])
        body, at = data[at:at + size], at + size + 1
        if fields[1] != b"blob":
            out[(rev, path)] = None
            continue
        try:
            out[(rev, path)] = body.decode("utf-8").replace("\r\n", "\n")
        except UnicodeDecodeError:
            out[(rev, path)] = None
    return out


# ------------------------------------------------------------------------------ record -> spec bindings
# TOOL-dTrueNorth-29 S2 -- the record-binding reader and the spec status-header grammar, read by the
# index generator and the deviation join, moved here verbatim from `gen_build_index.py`, which
# re-imports every name below so a caller reaching one through it keeps working.
RECORD_KINDS = ("spec", "build", "reviews", "prompts")

HDR_RE = re.compile(
    r"^\*\*Status:\*\* (?P<token>" + "|".join(STATUS_TOKENS) + r")"
    r" · rev-(?P<rev>\d+) · (?P<date>\d{4}-\d{2}-\d{2}) · node (?P<node>[a-z])"
    r" · Tier-(?P<tier>[12]) · base (?P<base>[0-9a-f]{8,})"
)


def read_text(path: str) -> str:
    # Bytes in, decode, normalise CR. Windows checkouts hand back CRLF and every comparison below
    # would then differ on every line — the exact green-by-accident shape a byte gate must not have.
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8").replace("\r\n", "\n")


def unfenced(text: str):
    """The text-only view, kept as the one fence machine's façade rather than a second copy."""
    for _n, line in unfenced_lines(text):
        if line is not None:
            yield line


# Every record under a build's non-spec folders names the spec(s) it is
# evidence about, in its own head. This parser READS that and CLASSIFIES; it never raises, because
# `collect()` is reached by both --check and --write through one call site, so a raising parser would
# let one unannotated record refuse to render every artifact.
BIND_HEAD_LINES = 12
# `deviation` (TOOL-dTrueNorth-4 S2): a departure from the design or from a spec, its grammar the
# deviation join's (`deviation_join.read_record`). Its kind and its file name are joined both ways in
# `read_bindings`, so an untyped departure cannot pass for research and a typed one cannot hide from
# the join's glob.
RECORD_KIND_TOKENS = ("spec-audit", "diff-review", "journal", "research", "deviation")
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


def record_paths(tracked: list, m: str) -> list:
    """Every tracked record: any depth, ANY extension, under a build's non-spec kind folders."""
    kinds = "|".join(k for k in RECORD_KINDS if k != "spec")
    sel = re.compile(r"^" + re.escape(m) + r"/builds/[^/]+/(?:" + kinds + r")/")
    return [p for p in tracked if sel.match(p)]


def build_id_token_re(alt: str):
    """One id token with its optional `@rev-N` pin (TOOL-dTrueNorth-9 S3). The one spelling
    `_expand_ids` and `read_id_pins` both match through, so the reader of the ids and the reader of
    their pins cannot disagree on what an id is."""
    return re.compile(r"^(?P<fam>" + alt + r")-(?P<slug>[A-Za-z0-9]+)-(?P<seq>\d+)(?:@rev-(?P<rev>\d+))?$")


def _expand_ids(rest: str, alt: str) -> tuple:
    """Return (ids, bad_tokens). A contiguous run may be written N..M and EXPANDS here, at authoring
    time, to a fixed set — unlike a wildcard it cannot rot when the build later gains a unit.

    TWO VALUES, for all four callers (TOOL-dTrueNorth-9 S1): `backlog.read_header_verbs` and
    `read_idlist` unpack a pair, and a third value stranded both. A pin is `read_id_pins`' to read."""
    ids, bad = [], []
    one = build_id_token_re(alt)
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


def read_id_pins(rest: str, alt: str) -> dict:
    """`{id: N}`, the highest N each id carries as `@rev-N` on the line (TOOL-dTrueNorth-9 S2), the
    revision a spec-audit record read. A range token carries no pin, so its ids get none."""
    pins: dict = {}
    one = build_id_token_re(alt)
    for tok in rest.split():
        mo = one.match(tok)
        if mo and mo.group("rev") is not None:
            ident = f"{mo.group('fam')}-{mo.group('slug')}-{mo.group('seq')}"
            pins[ident] = max(pins.get(ident, 0), int(mo.group("rev")))
    return pins


def read_bindings(root: str, tracked: list, conf: dict) -> dict:
    """path -> {state, kind, ids, pins, commissions, reason, bad}.

    `ids` is the kind line's ids once each, in first-seen order (TOOL-dTrueNorth-20 S9). `pins` is the
    kind line's `{id: N}`, the highest `@rev-N` each id carries there, empty when none
    does (TOOL-dTrueNorth-5 S3), read by `read_id_pins` beside the `_expand_ids` call
    (TOOL-dTrueNorth-9 S2). A `**Commissions:**` line pins nothing.

    A file named `-deviation-<n>.md` in a build's `build/` folder must carry kind `deviation`, and a
    `deviation` record must be named `<date>-build-<unit id>-deviation-<n>.md` there; either mismatch is
    `malformed` with its reason (TOOL-dTrueNorth-4 S2).

    Does not raise for an UNREADABLE file — a decode or IO failure becomes a `state` row carrying
    `why`. It CAN still raise for a malformed conf. The former docstring said "Never raises."
    unqualified, which is what let the blanket catch at the caller look reasonable.

    state is one of: bound · unbound · malformed · absent.
    """
    m = conf["MEMORY_ROOT"]
    alt = _id_alternation(conf)
    deviation_named = re.compile(r"^" + re.escape(m) + r"/builds/[^/]+/build/[^/]*-deviation-\d+\.md$")
    deviation_name = re.compile(r"^" + re.escape(m) + r"/builds/[^/]+/build/\d{4}-\d{2}-\d{2}-build-(?:" + alt
                                + r")-[A-Za-z0-9]+-\d+-deviation-\d+\.md$")
    out = {}
    for rel in record_paths(tracked, m):
        rec = {"state": "absent", "kind": None, "ids": [], "pins": {}, "commissions": [], "reason": None,
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
                served = " ".join(toks[1:])
                ids, bad = _expand_ids(served, alt)
                rec["kind"] = toks[0]
                # TOOL-dTrueNorth-20 S9, S36 — A REPEATED ID FOLDS HERE, in first-seen order, and never in
                # `_expand_ids`, whose base return its four callers keep: a record serving one id twice,
                # pinned at two revisions say, then renders it once in a records table and counts once in
                # the ids joins. Its pins are `read_id_pins`' below, the highest kept.
                rec["ids"] = list(dict.fromkeys(ids))
                rec["pins"] = read_id_pins(served, alt)
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
        # TOOL-dTrueNorth-4 S2 — the deviation kind joined to the file name, both ways: a file the
        # deviation join's glob reads must say it is one, and a record saying so must be where the glob
        # reads. A record with no Serves line keeps its own reason.
        named = deviation_named.search(rel)
        if named and rec["state"] in ("bound", "unbound") and rec["kind"] != "deviation":
            rec["state"] = "malformed"
            rec["why"] = (f"named as a deviation record, -deviation-<n>.md in a build/ folder, and its Serves "
                          f"kind is {rec['kind'] or 'the none form'}, not deviation")
        elif rec["kind"] == "deviation" and not deviation_name.match(rel):
            rec["state"] = "malformed"
            rec["why"] = ("Serves kind deviation, and the file is not named "
                          "<date>-build-<unit id>-deviation-<n>.md in a build's build/ folder")
        out[rel] = rec
    return out
