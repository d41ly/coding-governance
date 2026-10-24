#!/usr/bin/env python3
"""design_lib.py — the design's clauses and a spec's binding lines, parsed once (TOOL-dTrueNorth-1).

THE ONE PARSER every reader of the design imports: the carries join in the spec-token checker, the
coverage region and the hygiene refusal, the deviation population and the as-built generator. Before
it, the only reader was a bootstrap instrument no gate ran (`carries.py`), and its grammars are lifted
here rather than re-invented, so the product and the instrument read one grammar while both run:
`carries.py:50-56` for the binding lines, `:85-87` for the hash, `:104` for the clause tokens,
`:106-107` for the withdrawn ids, `:108-119` for the owned nodes, and `asbuilt.py:33` for a row of the
as-built view.

WHERE THE DESIGN IS comes from four keys of `.memory-tree.conf`, `DESIGN_KEYS`:
  DESIGN_RECORD     the design record, read ONLY at the baseline blob for its `[clause-ids]` section
  DESIGN_BASELINE   the 40-hex commit the design was pinned at
  DESIGN_VIEW       the as-built view, whose table is the clause population: each row's build, id,
                    text and `since` cell, the hash derived from the text
  DESIGN_NODES      the owned-node deriver, a tracked `.py` file loaded by path: its `derive()` and its
                    own `OWNED` tuple, nothing else in it
THE KEY RULE, `read_design_keys`, the one reading of the four keys (TOOL-dTrueNorth-16 S5), which
`read_design`, the deviation join, the as-built view and its host all take their states from, so no
reader of the keys hand-rolls them: all four blank or absent is OFF, nothing read; some set and some
not is a refusal naming each blank key; all four set is ARMED, `DESIGN_BASELINE` a 40-hex commit pin
that resolves to a commit in the repository or a refusal naming it. `read_design` refuses the off
state as well, naming every key, and the CLI exits 2 on a blank key. The keys are gov's: the kit's
example conf declares them blank, which is off, so an adopter's engines read them as off.
The chain builds are the view's Build column; no build list is typed anywhere.

THE CUTOFF AND THE KEY RULE (S7), applied by the carries join and the coverage read:
`SPEC_CARRIES_CUTOFF` blank is off, one line, whatever the design keys hold; set with every design key
blank, a refusal naming the cutoff and the keys; set over a partial set, the key rule's refusal; set
over all four, armed. The deviation join and the as-built view read the key rule alone.

ONE CONF READ, `read_design_conf`: `.memory-tree.conf` through `tree_lib.parse_conf`, the last
declaration of a key winning and an `export ` prefix read as bash reads it, so the carries join and
the generator read one value of each key (S14).

ONE REVISION READER, `read_spec_revisions` (S10, S12): every non-merge commit that changed a spec,
oldest first, with its text before and after, in two git spawns whatever the revision count or the
path count, the log over one glob pathspec and the blobs through `tree_lib.read_blobs_at`, the kit's
one bytes reader (TOOL-dTrueNorth-20 S18, S33). The carries join and the deviation population both
read it.

ONE SPEC FILENAME DATE, `SPEC_FILE_DATE`, the spec-token checker's pattern, which its `SPEC_DATE` is
bound to (S32), and one fixture design, `write_design_fixture`, which the deviation join's and the
as-built view's fixtures both write their designs with (S19). ONE SPEC FILE PREDICATE,
`build_spec_file_re`, which the revision reader refuses by and `scan_chain_specs` selects by, and ONE
TRACKED READ of the build folders, `read_tracked_builds`, which `--chain-specs` and the deviation
join's records and specs read (TOOL-dTrueNorth-26 S5, S7).

THE `[chain]` ROWS of a design record are read by `read_chain_clauses` (TOOL-dTrueNorth-4 S9), the
one reader the deviation population's clause-move arm and the as-built generator share; it takes the
record's text, so a caller reads it at whichever commit it measures.

THE BINDING GRAMMAR, the home it has until the spec template carries a section for it. A binding is a
line at column 0, outside a fenced block, opening with one of five bold keys, with optional trailing
whitespace and nothing else on the line:
  **Carries:** <cl-id>@<hash8> whole          the clause, whole, pinned to its text's hash
  **Carries:** <cl-id>@<hash8> part k/n       one of n carriers, 1 <= k <= n and n >= 2
  **Carries:** node:<ns>.<key>                an owned node, <ns> as [a-z-]+
  **Derived:** <decision id>                  a spec no clause asks for, and the decision behind it
  **Moved:** <cl-id> to <build> by <decision id>
  **Retired:** <cl-id> by <decision id>       and likewise **Deferred:**
The shapes are the instrument's: <cl-id> `cl-d[A-Z]\\w+-\\d{4}`, <hash8> eight lowercase hex digits,
<build> `d[A-Z]\\w+`, <decision id> `[A-Z]+-d[A-Z]\\w+-\\d+`. Two tightenings over the instrument's
`RELEASED`, each refusing a line it would misread rather than reading one it refuses: a **Moved:** line
names its receiving build, and a **Retired:** or **Deferred:** line does not. A clause's hash is the
first eight hex digits of the SHA-256 of its UTF-8 text with its trailing id cut off and each
whitespace run folded to one space.

A MALFORMED LINE IS COLLECTED, NOT FIRST-HIT: a line opening with a key and failing its grammar is
gathered with every other, and `parse_binding_lines` raises ONE `DesignRefusal` naming each
`path:line`, the line and the grammar it fails. A text ending inside an open fence is a refusal naming
the fence's line, because every line after it would otherwise go unread. `strict=False` is the one
exception, for history: a revision a later commit corrected is read for what it carried, and its
malformed lines are not this commit's finding. A fenced line is never a binding, which is the house
rule of the spec-token checker's claims join; the instrument reads fences, so a spec author still
keeps a column-0 example out of prose.

THE CUTOFF GATES THE POPULATION, NOT THE PARSER. `SPEC_CARRIES_CUTOFF` reaches this module only as a
parameter of `scan_chain_specs`, its value tested by the caller through `check_cutoff_value` in
`<prefix>/check-spec-tokens.py`, so the date has one test. This module reads no date key.

Usage (from the repository root):
  python design_lib.py --parse <path>...           every binding of each file, or its refusal
  python design_lib.py --design [--build <slug>]   the counts read; with --build, that build's rows
  python design_lib.py --chain-specs <cutoff>      the chain builds' tracked specs dated on or after it
Exit 0 clean · 1 on a malformed line or a refusal · 2 when a DESIGN_* key is blank, so nothing was read.

What it does not read: whether a spec carries a clause it names, which is the carries join's; which
statuses carry; and any reader for an adopter — the keys are gov's, declared blank in the example
conf, which is off, so an adopter's engines read them as off.
"""
from __future__ import annotations

import datetime
import hashlib
import importlib.util
import os
import pathlib
import re
import subprocess
import sys

KIT = os.path.dirname(os.path.abspath(__file__))
if KIT not in sys.path:
    sys.path.insert(0, KIT)
from tree_lib import (  # noqa: E402
    GIT_ENV_LEAKS, build_git_env, build_spec_path_re, parse_conf, read_blobs_at, read_git_output, unfenced_lines)

_CL = r"cl-d[A-Z]\w+-\d{4}"
_DECISION = r"[A-Z]+-d[A-Z]\w+-\d+"
_BUILD = r"d[A-Z]\w+"
# A clause's trailing backticked id, cut off before its text is hashed (`carries.py:50`, `CID`).
CLAUSE_ID = re.compile(r"`(" + _CL + r")`\s*$")
CARRY = re.compile(r"^\*\*Carries:\*\* (?:(" + _CL + r")@([0-9a-f]{8}) (whole|part (\d+)/(\d+))"
                   r"|node:([a-z-]+)\.(\S+))\s*$")
DERIVED = re.compile(r"^\*\*Derived:\*\* (" + _DECISION + r")\s*$")
# The instrument's release grammar, its optional `to` kept: the two tightenings are applied by the
# parser, so the line that fails one is named for the tightening it fails.
RELEASED = re.compile(r"^\*\*(Moved|Retired|Deferred):\*\* (" + _CL + r")(?: to (" + _BUILD + r"))? by ("
                      + _DECISION + r")\s*$")
BINDING_HEAD = re.compile(r"^\*\*(Carries|Derived|Moved|Retired|Deferred):\*\*")
# Built from `_CL` and `_BUILD` as `CARRY` is, so the clause-id grammar is spelled once in the kit and
# the view's two importers read `_CL` from here (TOOL-dTrueNorth-26 S8).
VIEW_ROW = re.compile(r"^\| (" + _BUILD + r") \| `(" + _CL + r")` \| (.*) \| (baseline|deviation `([^`]+)`) \|$")
DESIGN_KEYS = ("DESIGN_RECORD", "DESIGN_BASELINE", "DESIGN_VIEW", "DESIGN_NODES")

# A spec's filename date, the spec-token checker's own pattern, compiled here once: the checker's
# `SPEC_DATE` is bound to this object and `scan_chain_specs` reads it (TOOL-dTrueNorth-16 S32).
SPEC_FILE_DATE = re.compile(r"/([0-9]{4}-[0-9]{2}-[0-9]{2})-spec-")
_TABLE_RULE = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")
_GRAMMARS = {
    "Carries": "`**Carries:** <cl-id>@<hash8> whole`, `**Carries:** <cl-id>@<hash8> part k/n` "
               "(1 <= k <= n, n >= 2) or `**Carries:** node:<ns>.<key>`",
    "Derived": "`**Derived:** <decision id>`",
    "Moved": "`**Moved:** <cl-id> to <build> by <decision id>`",
    "Retired": "`**Retired:** <cl-id> by <decision id>`",
    "Deferred": "`**Deferred:** <cl-id> by <decision id>`",
}


class DesignRefusal(ValueError):
    """Every refusal this module makes. Its message names the key, the path or the `path:line`, so a
    caller prints it whole. `blank` holds the DESIGN_* keys found blank, and is empty for any other
    refusal: the CLI exits 2 on those, because nothing was read."""

    def __init__(self, message, blank=()):
        super().__init__(message)
        self.blank = tuple(blank)


def run_git(root, *args, stdin=None, extra_env=None):
    """One git call at `root` under the kit's pin policy, its stdout as bytes and `stdin` its input;
    never raises on a non-zero exit, so each caller names its own refusal. Pathspecs are literal: a
    conf value is a path, never a glob or a magic signature. Its env is `build_git_env` less
    `tree_lib.GIT_ENV_LEAKS`, the strip `tree_lib.read_git_output` applies, so an exported `GIT_DIR`
    never points the call at another repository than `root` (TOOL-dTrueNorth-26 S1). `extra_env` is laid
    over that stripped env, for the one call whose answer must also not read a node's state the strip
    keeps, as the as-built merge check's attribute read (TOOL-dTrueNorth-31 S3). A None value in it
    reads as "absent from this call's env": its key is taken out, so a caller's exported
    `GIT_ATTR_SOURCE` never reaches that read (TOOL-dTrueNorth-32 S1)."""
    env = {k: v for k, v in build_git_env().items() if k not in GIT_ENV_LEAKS}
    env.update(extra_env or {})
    env = {k: v for k, v in env.items() if v is not None}
    return subprocess.run(["git", "--no-replace-objects", "--literal-pathspecs", "-C", str(root), *args],
                          input=stdin, capture_output=True, env=env)


def derive_clause_hash(text):
    """The first eight hex digits of the SHA-256 of a clause's UTF-8 text, its trailing `cl-` id cut
    off and each whitespace run folded to one space (`carries.py:85-87`)."""
    body = re.sub(r"\s+", " ", CLAUSE_ID.sub("", text)).strip()
    return hashlib.sha256(body.encode("utf-8")).hexdigest()[:8]


def extract_clause_tokens(text):
    """A clause's backticked names, sorted and unique, as `carries.py:104` takes them."""
    body = CLAUSE_ID.sub("", text).strip()
    return sorted(set(re.findall(r"`([^`\s][^`]*)`", body)))


def read_design_view(view, root="."):
    """Every row of the as-built view's table, `[(build, clause id, text, hash8, since)]` in view order.

    `since` is `baseline` or `deviation <record id>`, the view's own cell. The table starts at its
    first `|` line, the header, and its rule line; every later line opening with `|`, after any
    indent, is a row and must match `VIEW_ROW` at column 0, so a hand edit that breaks or indents a
    row, or a blank line that splits the table, cannot shrink the clause population silently. A view
    with no row, a row whose id repeats, or a path naming no readable file is a refusal.

    The file is read as bytes, decoded as UTF-8 with CRLF folded, as the view's writer and its
    `--check` read it, so a bare CR stays in its row's text cell for every reader (TOOL-dTrueNorth-26
    S10); a file that is not UTF-8 is the refusal.
    """
    path = pathlib.Path(root) / view
    try:
        text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as e:
        raise DesignRefusal(f"DESIGN_VIEW names {view}, which cannot be read: {e}") from None
    lines = text.split("\n")
    head = next((n for n, ln in enumerate(lines) if ln.startswith("|")), None)
    if head is None or head + 1 >= len(lines) or not _TABLE_RULE.match(lines[head + 1].rstrip("\r")):
        raise DesignRefusal(f"DESIGN_VIEW names {view}, which holds no table: no `|` header line with a "
                            "rule line under it")
    rows, seen, bad = [], {}, []
    for n in range(head + 2, len(lines)):
        ln = lines[n].rstrip("\r")
        if not ln.lstrip().startswith("|"):
            continue
        m = VIEW_ROW.match(ln)
        if not m:
            bad.append(f"{view}:{n + 1}: `{ln[:120]}` is no row of the view's grammar")
            continue
        build, cid, body = m.group(1), m.group(2), m.group(3)
        if cid in seen:
            bad.append(f"{view}:{n + 1}: {cid} repeats the row at line {seen[cid]}")
            continue
        seen[cid] = n + 1
        since = "baseline" if m.group(4) == "baseline" else f"deviation {m.group(5)}"
        rows.append((build, cid, body, derive_clause_hash(body), since))
    if bad:
        raise DesignRefusal(f"DESIGN_VIEW names {view}, whose table holds {len(bad)} line(s) the reader "
                            "refuses:\n" + "\n".join(f"  {b}" for b in bad))
    if not rows:
        raise DesignRefusal(f"DESIGN_VIEW names {view}, whose table holds no row, which is never an "
                            "empty design")
    return rows


def parse_chain_cell(cell):
    """A `[chain]` row's clause cell split into its clauses, on `; ` outside backticks, parentheses
    and double quotes, the clause scan's rule (`carries.py:62-82`)."""
    out, cur, depth, tick, quote, i = [], [], 0, False, False, 0
    while i < len(cell):
        ch = cell[i]
        if ch == "`" and not quote:
            tick = not tick
        elif ch == '"' and not tick:
            quote = not quote
        elif not tick and ch == "(":
            depth += 1
        elif not tick and ch == ")":
            depth = max(0, depth - 1)
        if cell.startswith("; ", i) and not (depth or tick or quote):
            out.append("".join(cur))
            cur, i = [], i + 2
            continue
        cur.append(ch)
        i += 1
    out.append("".join(cur))
    return [c.strip() for c in out if c.strip()]


def read_chain_clauses(text, path="DESIGN_RECORD"):
    """Every clause of a design record's `[chain]` section, `[(build, clause id, text, hash8)]` in row
    and clause order, as `deviations.py:159-170` reads them (TOOL-dTrueNorth-4 S9).

    The section runs from its `## [chain]` heading to the next `## ` heading; a row is
    `| <build> | … | … | <clauses> | … |`, its clause cell split by `parse_chain_cell`, each clause
    kept where it ends in its backticked `cl-` id. `text` is the clause with that id cut off, and the
    hash is `derive_clause_hash`'s. The deviation population's clause-move arm and the as-built
    generator both read the section here, so the two read one grammar. A record with no `[chain]`
    section is a refusal naming `path`, never an empty chain.
    """
    text = text.replace("\r\n", "\n")
    if "\n## [chain]" not in text:
        raise DesignRefusal(f"{path} holds no `## [chain]` section, so no clause of the chain can be read")
    chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    out = []
    for ln in chain.split("\n"):
        m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
        if not m:
            continue
        for clause in parse_chain_cell(m.group(2)):
            cid = CLAUSE_ID.search(clause)
            if cid:
                out.append((m.group(1), cid.group(1), CLAUSE_ID.sub("", clause).strip(),
                            derive_clause_hash(clause)))
    return out


def read_retired_ids(root, record, baseline):
    """The withdrawn ids the `[clause-ids]` section of `record` lists after `Retired:`, read from the
    blob at `baseline` and never from the working tree, as `carries.py:106-107` reads that list.
    A baseline naming no commit, or a record absent at it, is a refusal."""
    if run_git(root, "cat-file", "-e", f"{baseline}^{{commit}}").returncode:
        raise DesignRefusal(f"DESIGN_BASELINE {baseline} names no commit, so the withdrawn ids cannot be "
                            "read at it")
    r = run_git(root, "show", f"{baseline}:{record}")
    if r.returncode:
        raise DesignRefusal(f"DESIGN_RECORD {record} is absent at DESIGN_BASELINE {baseline}, so the "
                            "withdrawn ids cannot be read")
    text = r.stdout.decode("utf-8", "replace").replace("\r\n", "\n")
    if "\n## [clause-ids]" not in text:
        return set()
    section = text.split("\n## [clause-ids]", 1)[1].split("\n## ", 1)[0]
    if "Retired:" not in section:
        return set()
    return set(re.findall(r"`(" + _CL + r")`", section.split("Retired:", 1)[1]))


def read_owned_nodes(root, deriver, builds):
    """Each chain build's owned nodes, `{build: {"<ns>.<key>", ...}}`, read from the deriver `deriver`
    names: its `derive()` and its own `OWNED` tuple, joined by the `owner` relation exactly as
    `carries.py:111-119` joins them. A deriver that is not a tracked `.py` file is refused before any
    import; one whose load or `derive()` raises, or that declares no `OWNED`, is a refusal."""
    if not deriver.endswith(".py"):
        raise DesignRefusal(f"DESIGN_NODES names {deriver}, which is not a .py file, so no deriver is loaded")
    r = run_git(root, "ls-files", "--", deriver)
    if r.returncode or deriver not in r.stdout.decode("utf-8", "replace").splitlines():
        raise DesignRefusal(f"DESIGN_NODES names {deriver}, which is not a tracked file, and only a tracked "
                            "deriver is loaded")
    spec = importlib.util.spec_from_file_location("design_nodes", pathlib.Path(root) / deriver)
    mod = importlib.util.module_from_spec(spec)
    # No write path: the deriver and what it imports load without a bytecode cache beside them.
    cache, sys.dont_write_bytecode = sys.dont_write_bytecode, True
    try:
        try:
            spec.loader.exec_module(mod)
        except (Exception, SystemExit) as e:
            raise DesignRefusal(f"DESIGN_NODES names {deriver}, which raised on load: "
                                f"{type(e).__name__}: {e}") from None
        try:
            _, ns = mod.derive()
        except (Exception, SystemExit) as e:
            raise DesignRefusal(f"DESIGN_NODES names {deriver}, whose derive() raised: "
                                f"{type(e).__name__}: {e}") from None
    finally:
        sys.dont_write_bytecode = cache
    owned = getattr(mod, "OWNED", None)
    if not isinstance(owned, tuple) or not owned:
        raise DesignRefusal(f"DESIGN_NODES names {deriver}, which declares no OWNED tuple of namespaces")
    nodes = {b: set() for b in builds}
    try:
        for name in owned:
            for n in ns.get(name) or []:
                for k, vs in n["rels"]:
                    if k == "owner":
                        for o in vs:
                            if o in nodes:
                                nodes[o].add(f"{name}.{n['key']}")
    except (AttributeError, KeyError, TypeError, ValueError) as e:
        raise DesignRefusal(f"DESIGN_NODES names {deriver}, whose derive() returned a shape the owner join "
                            f"cannot read: {type(e).__name__}: {e}") from None
    return nodes


def parse_binding_lines(text, path, strict=True):
    """Every binding line of `text`, one dict per line with the fields `kind`, `line`, `clause`,
    `hash`, `part`, `node`, `decision` and `to`.

    Walks `tree_lib.unfenced_lines`, so a fenced line is never a binding. Every line opening with a
    key that fails its grammar is collected, and one `DesignRefusal` names each `path:line`, the line
    and the grammar; a text ending inside an open fence is refused naming the fence's line. With
    `strict=False` the well-formed bindings are returned and the rest passed over, for reading a past
    revision a later one corrected.
    """
    bindings, bad = [], []
    for n, line in unfenced_lines(text):
        if line is None:
            bad.append(f"{path}:{n}: a fence opens here and never closes, so every line after it would "
                       "go unread")
            continue
        head = BINDING_HEAD.match(line)
        if not head:
            continue
        key = head.group(1)
        shown = line.rstrip()
        b = {"kind": key.lower(), "line": n, "clause": None, "hash": None, "part": None, "node": None,
             "decision": None, "to": None}
        why = None
        if key == "Carries":
            m = CARRY.match(line)
            if not m:
                why = "fails"
            elif m.group(6):
                b["node"] = f"{m.group(6)}.{m.group(7)}"
            else:
                b["clause"], b["hash"] = m.group(1), m.group(2)
                if m.group(3) != "whole":
                    k, of = int(m.group(4)), int(m.group(5))
                    if of < 2 or not 1 <= k <= of:
                        why = f"carries part {k}/{of}, outside 1 <= k <= n with n >= 2, and so fails"
                    b["part"] = (k, of)
        elif key == "Derived":
            m = DERIVED.match(line)
            if not m:
                why = "fails"
            else:
                b["decision"] = m.group(1)
        else:
            m = RELEASED.match(line)
            if not m:
                why = "fails"
            elif key == "Moved" and not m.group(3):
                why = "names no receiving build, and so fails"
            elif key != "Moved" and m.group(3):
                why = "names a receiving build, which only a **Moved:** line does, and so fails"
            else:
                b["clause"], b["to"], b["decision"] = m.group(2), m.group(3), m.group(4)
        if why:
            bad.append(f"{path}:{n}: `{shown}` {why} {_GRAMMARS[key]}")
            continue
        bindings.append(b)
    if bad and strict:
        raise DesignRefusal(f"{path}: {len(bad)} binding line(s) refused:\n" + "\n".join(f"  {x}" for x in bad))
    return bindings


def build_spec_file_re(memory_root="memory"):
    """THE ONE PREDICATE of what a spec file is (TOOL-dTrueNorth-26 S5), compiled for `fullmatch`: a
    `.md` under `<memory_root>/builds/<slug>/spec/`, at any depth, whose filename holds `-spec-`, the
    shape the revision log's pathspec `:(glob)<memory_root>/builds/*/spec/**/*-spec-*.md` matches.
    `read_spec_revisions` refuses a path it does not match, and `scan_chain_specs` passes over a
    spec-folder `.md` it does not match, counted as `unnamed`, so no selector hands the revision reader
    a file it refuses. What bans a free-named spec-folder file is hygiene check 5, not this."""
    memory_root = str(memory_root).replace("\\", "/").rstrip("/")
    return re.compile(re.escape(memory_root) + r"/builds/[^/]+/spec/(?:[^/]+/)*[^/]*-spec-[^/]*\.md")


def scan_chain_specs(paths, builds, cutoff, memory_root="memory"):
    """The chain builds' spec files among `paths`, `([(build, path)], {reason: count})`.

    A path is a spec-folder file when `tree_lib.build_spec_path_re` places it under
    `<memory_root>/builds/<slug>/spec/`, at any depth, and it ends `.md`; any other path is not
    counted. One is kept when its build is one of `builds`, its filename date, read by
    `SPEC_FILE_DATE`, is on or after `cutoff`, and `build_spec_file_re` calls it a spec; what is passed
    over is counted as `other-build`, `pre-cutoff`, `undated` and `unnamed`, the last a spec-folder
    file whose name holds no `-spec-` (TOOL-dTrueNorth-26 S5). A blank `cutoff` reads no date and keeps
    every chain-build spec, as the instrument reads them. Statuses are not read here: which statuses
    carry is the join's choice.
    """
    memory_root = str(memory_root).replace("\\", "/").rstrip("/")   # `memory/` would match no path
    spec_re = build_spec_path_re(memory_root)
    spec_file = build_spec_file_re(memory_root)
    chain = set(builds)
    lead = len(memory_root) + len("/builds/")
    kept, skipped = [], {"other-build": 0, "pre-cutoff": 0, "undated": 0, "unnamed": 0}
    for p in sorted({str(p).replace("\\", "/") for p in paths}):
        if not spec_re.match(p) or not p.endswith(".md"):
            continue
        build = p[lead:].split("/", 1)[0]
        if build not in chain:
            skipped["other-build"] += 1
            continue
        if cutoff:
            m = SPEC_FILE_DATE.search(p)
            if not m:
                skipped["undated"] += 1
                continue
            if m.group(1) < cutoff:
                skipped["pre-cutoff"] += 1
                continue
        if not spec_file.fullmatch(p):
            skipped["unnamed"] += 1
            continue
        kept.append((build, p))
    return kept, skipped


def read_tracked_builds(root, memory_root="memory"):
    """Every TRACKED path under `<memory_root>/builds`, repo-relative POSIX in `git ls-files` order: ONE
    `ls-files` through `run_git`, the read `--chain-specs` makes, lifted here so the deviation join's
    records and spec list read the population `gen_build_index.plan()` reads (TOOL-dTrueNorth-26 S7).

    A path in the index is tracked, so a record staged and not committed is read and a draft never
    staged is not. A failed `ls-files` is a `DesignRefusal` naming it, which each caller maps as it
    maps the design's other refusals."""
    memory_root = str(memory_root).replace("\\", "/").strip("/") or "memory"
    r = run_git(root, "ls-files", "-z", "--", f"{memory_root}/builds")
    if r.returncode:
        first = next((ln.strip() for ln in r.stderr.decode("utf-8", "replace").splitlines() if ln.strip()),
                     "git printed nothing on stderr")
        raise DesignRefusal(f"git ls-files over {memory_root}/builds exited {r.returncode}, so no tracked "
                            f"record or spec was read: {first}")
    return [p for p in r.stdout.decode("utf-8", "replace").split("\0") if p]


def read_design_conf(root):
    """`.memory-tree.conf` at `root` through `tree_lib.parse_conf`, `{}` where there is none (S14).

    The ONE read of the conf for the carries keys and the design keys: the carries join takes it
    when its caller passes no conf, and the generator passes its own parse of the same file, so a key
    declared twice, or behind an `export ` prefix, reads one value in both.
    """
    p = pathlib.Path(root) / ".memory-tree.conf"
    if not p.is_file():
        return {}
    return parse_conf(p.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n"), {})


def read_design_keys(root, conf):
    """THE KEY RULE (S5): the four `DESIGN_KEYS` values of `conf`, validated, or None when all four are
    blank or absent, the off state, read with no git call.

    Some set and some not is a `DesignRefusal` naming each blank key, its `blank` holding them. All
    four set, `DESIGN_BASELINE` must be a 40-hex pin naming a commit in `root`, else a refusal naming
    it; one `git cat-file -e` decides. Returns `{key: value}` for the four. What it does not check:
    that the other three name readable files, which each one's own reader refuses by name.
    """
    values = {k: str(conf.get(k) or "").strip() for k in DESIGN_KEYS}
    blank = [k for k in DESIGN_KEYS if not values[k]]
    if len(blank) == len(DESIGN_KEYS):
        return None
    if blank:
        held = [k for k in DESIGN_KEYS if k not in blank]
        raise DesignRefusal(f"{', '.join(blank)} {'is' if len(blank) == 1 else 'are'} blank while "
                            f"{', '.join(held)} {'is' if len(held) == 1 else 'are'} set, so the design is half "
                            "declared and nothing was read", blank=blank)
    pin = values["DESIGN_BASELINE"]
    if not re.fullmatch(r"[0-9a-f]{40}", pin):
        raise DesignRefusal(f"DESIGN_BASELINE {pin} is not a 40-hex commit pin, so nothing was read")
    if run_git(root, "cat-file", "-e", f"{pin}^{{commit}}").returncode:
        raise DesignRefusal(f"DESIGN_BASELINE {pin} names no commit, so nothing was read")
    return values


# A spec's declared write set and its consumed siblings (TOOL-dGroundRules-25 S37, S38): the one read
# the spec-token checker's guards join and the build-order render share.
FILES_TOUCHED_HEAD = re.compile(r"^### Files touched( \(estimate\))?[ \t]*$", re.M)
TICKED = re.compile(r"`([^`\n]+)`")
CONSUMES_BULLET = re.compile(r"^(?:-|\*)[ \t]*\*\*consumes-from\*\*[ \t]+(.*)$")


def read_spec_writes(text):
    """Every word inside backticks under a spec's `### Files touched` sub-head, in order and without
    repeats, or None when the spec has no such sub-head. The body closes at the next heading of any
    depth, because the sub-head has siblings inside section 4. No shape filter: each caller keeps its own."""
    m = FILES_TOUCHED_HEAD.search(text)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^##+ ", rest, re.M)
    out = []
    for tok in TICKED.findall(rest[:nxt.start()] if nxt else rest):
        out += [w for w in tok.split() if w not in out]
    return out


def read_spec_consumes(text):
    """The targets of a spec's `**consumes-from**` bullets under `### Edges` in its Non-goals section,
    in order, by check 12's bullet grammar in `check-memory-hygiene.sh`: the first backticked token
    after the verb, else its leading run of `[A-Za-z0-9_-]`."""
    out, in3, edges = [], False, False
    for line in text.replace("\r", "").split("\n"):
        if line.startswith("## "):
            in3, edges = bool(re.match(r"## [0-9]+[.] Non-goals", line)), False
        elif line.startswith("### "):
            edges = in3 and bool(re.match(r"### Edges[ \t]*$", line))
        elif edges and (m := CONSUMES_BULLET.match(line)):
            t = re.match(r"`([^`]*)`|([A-Za-z0-9_-]*)", m[1])
            target = t[1] if t[1] is not None else t[2]
            if target and target not in out:
                out.append(target)
    return out


def read_spec_revisions(root, paths, memory_root="memory"):
    """`{path: [(sha, before, after)]}`, oldest first, for every path of `paths` (S10, S12): one entry per
    non-merge commit that changed it, `before` its text at that commit's first parent, None at its
    creation, and `after` its text at the commit, None at its deletion.

    TWO GIT SPAWNS whatever the revision count AND whatever the path count: ONE `git log --full-history
    --no-merges --no-renames --date-order --reverse` at HEAD over ONE glob pathspec,
    `:(glob)<memory_root>/builds/*/spec/**/*-spec-*.md`, filtered to `paths` here, never the paths on
    argv (TOOL-dTrueNorth-20 S18), since a few hundred chain specs on one command line raise
    [WinError 206]; and one `git cat-file --batch` for every blob it names, through
    `tree_lib.read_blobs_at`, the kit's one bytes reader (S33). Read without following a rename. A path
    the pathspec cannot match is a refusal naming it, since it would read as no revisions; so is a log
    or a batch that fails or cannot start, which the callers exit 2 on.
    """
    paths = list(dict.fromkeys(str(p).replace("\\", "/") for p in paths))
    out = {p: [] for p in paths}
    if not paths:
        return out
    memory_root = str(memory_root).replace("\\", "/").rstrip("/")
    pathspec = f":(glob){memory_root}/builds/*/spec/**/*-spec-*.md"
    inside = build_spec_file_re(memory_root)    # the predicate `scan_chain_specs` selects by (TOOL-dTrueNorth-26 S5)
    outside = [p for p in paths if not inside.fullmatch(p)]
    if outside:
        raise DesignRefusal(f"{outside[0]} is outside the revision log's pathspec {pathspec}, so its revisions "
                            "would read as none" + (f", and {len(outside) - 1} more" if len(outside) > 1 else ""))
    try:
        log = read_git_output(root, ("--no-replace-objects", "log", "-z", "--full-history", "--no-merges",
                                     "--no-renames", "--date-order", "--reverse", "--name-only",
                                     "--format=%x1e%H%x1f%P%x1f", "HEAD", "--", pathspec))
    except OSError as exc:
        raise DesignRefusal(f"the spec revision log failed, so no revision was read: {exc}") from None
    revs = []
    for rec in log.decode("utf-8", "surrogateescape").split("\x1e")[1:]:
        sha, parents, rest = rec.split("\x1f", 2)
        parent = (parents.split() or [None])[0]
        revs += [(p, sha, parent) for p in dict.fromkeys(x for x in re.split(r"[\0\n]", rest) if x) if p in out]
    asks = list(dict.fromkeys(a for p, sha, parent in revs for a in ([(parent, p)] if parent else []) + [(sha, p)]))
    try:
        blobs = read_blobs_at(root, asks)
    except OSError as exc:
        raise DesignRefusal(f"the spec revisions' blobs could not be read, so no revision was read: {exc}") from None
    for p, sha, parent in revs:
        out[p].append((sha, blobs.get((parent, p)) if parent else None, blobs.get((sha, p))))
    return out


def write_design_fixture(repo):
    """A fixture's own design, written as one commit through `repo.write_commit`, whose sha it returns:
    the builder TOOL-dTrueNorth-12 S3 gave the deviation fixture, moved here at its second instance, the
    as-built view's fixture (TOOL-dTrueNorth-16 S19).

    `repo` is a fixture repository holding `record` and `view`, the two paths, `clause_ids`, the
    clause ids in order, and `builds`, the two chain builds, with `write_commit(files, subject)`
    returning a mark and `read_sha(mark)`. The record's `[chain]` holds one clause per id, the ids
    split across the builds, the first taking the larger half; its `[clause-ids]` section reads
    `No baseline.`, and `repo.v2` holds the record as written. The view is one `baseline` row per
    clause in the grammar `VIEW_ROW` reads. Nothing reads the tree's own DESIGN_RECORD or DESIGN_VIEW.
    """
    ids, (first, second) = list(repo.clause_ids), repo.builds
    half = (len(ids) + 1) // 2
    clauses = [(first if n < half else second, cid, f"the fixture's clause {n + 1} holds `fixture-name-{n + 1}`")
               for n, cid in enumerate(ids)]
    rows = [f"| {b} | Fixture | {'none' if b == first else first} | "
            + "; ".join(f"{text} `{cid}`" for at, cid, text in clauses if at == b) + " | none |" for b in (first, second)]
    repo.v2 = "\n".join(["# The fixture's design record, its own two builds", "",
                         "## [chain] The chain: the fixture's builds and their clauses", "",
                         "| Build | Stage | Parents | Planned units | Gaps owned |", "|---|---|---|---|---|", *rows, "",
                         "## [clause-ids] Clause ids", "", "No baseline.", ""])
    view = "\n".join(["# The fixture's as-built view", "", "| Build | Clause | Text | Since |", "|---|---|---|---|",
                      *(f"| {b} | `{cid}` | {text} | baseline |" for b, cid, text in clauses), ""])
    return repo.read_sha(repo.write_commit({repo.record: repo.v2, repo.view: view},
                                           "fixture: the design's [chain] and its view, the fixture's own"))


def read_design(root, conf):
    """The design, read once from the four `DESIGN_KEYS` values of the caller's conf.

    Returns `{"baseline", "view", "rows", "builds", "retired", "nodes"}`: the pin, the view's path, its
    rows in view order, `{build: {cid: (text, hash8, since)}}`, the withdrawn ids at the baseline, and
    `{build: {"<ns>.<key>"}}`. Its states are `read_design_keys`', the off state among its refusals:
    every key blank is a refusal naming them all, raised before anything is read.
    """
    values = read_design_keys(root, conf)
    if values is None:
        raise DesignRefusal("every DESIGN_* key is blank (" + ", ".join(DESIGN_KEYS) + "), so nothing was "
                            "read", blank=DESIGN_KEYS)
    baseline = values["DESIGN_BASELINE"]
    rows = read_design_view(values["DESIGN_VIEW"], root)
    builds = {}
    for build, cid, text, h, since in rows:
        builds.setdefault(build, {})[cid] = (text, h, since)
    return {"baseline": baseline, "view": values["DESIGN_VIEW"], "rows": rows, "builds": builds,
            "retired": read_retired_ids(root, values["DESIGN_RECORD"], baseline),
            "nodes": read_owned_nodes(root, values["DESIGN_NODES"], list(builds))}


def read_repo_root():
    """The repository root from git, else the working directory."""
    r = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True)
    top = r.stdout.decode("utf-8", "replace").strip()
    return pathlib.Path(top) if r.returncode == 0 and top else pathlib.Path.cwd()


def print_binding(path, b):
    part = f"{b['part'][0]}/{b['part'][1]}" if b["part"] else ("whole" if b["clause"] and b["hash"] else "-")
    fields = " ".join(f"{k}={b[k] or '-'}" for k in ("clause", "hash"))
    rest = " ".join(f"{k}={b[k] or '-'}" for k in ("node", "decision", "to"))
    print(f"  {path}:{b['line']} kind={b['kind']} line={b['line']} {fields} part={part} {rest}")


def main(argv):
    usage = ("usage: design_lib.py --parse <path>... | --design [--build <slug>] | --chain-specs <cutoff>")
    if not argv or argv[0] not in ("--parse", "--design", "--chain-specs"):
        print(f"design-lib: REFUSING — {usage}")
        return 1
    verb = argv[0]
    if verb == "--parse":
        if len(argv) < 2:
            print(f"design-lib: REFUSING — --parse names no file; {usage}")
            return 1
        refused = count = 0
        for path in argv[1:]:
            try:
                text = pathlib.Path(path).read_text(encoding="utf-8")
                bindings = parse_binding_lines(text, path)
            except (OSError, UnicodeDecodeError) as e:
                print(f"design-lib: REFUSING — {path} cannot be read: {e}")
                refused += 1
                continue
            except DesignRefusal as e:
                print(f"design-lib: REFUSING — {e}")
                refused += 1
                continue
            for b in bindings:
                print_binding(path, b)
            count += len(bindings)
        print(f"design-lib: parsed {len(argv) - 1} file(s) · {count} binding(s) · {refused} refused")
        return 1 if refused else 0
    build = cutoff = None
    if verb == "--design":
        rest = argv[1:]
        if rest and (rest[0] != "--build" or len(rest) != 2):
            print(f"design-lib: REFUSING — {usage}")
            return 1
        build = rest[1] if rest else None
    else:
        cutoff = argv[1] if len(argv) == 2 else ""
        try:
            if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", cutoff):
                raise ValueError(cutoff)
            datetime.date.fromisoformat(cutoff)
        except ValueError:
            print(f"design-lib: REFUSING — --chain-specs takes one ISO date (YYYY-MM-DD), not [{cutoff}]")
            return 1
    root = read_repo_root()
    conf = read_design_conf(root)
    try:
        design = read_design(root, conf)
    except DesignRefusal as e:
        print(f"design-lib: REFUSING — {e}")
        return 2 if e.blank else 1
    if verb == "--chain-specs":
        memory_root = (conf.get("MEMORY_ROOT") or "memory").replace("\\", "/").rstrip("/")
        try:
            tracked = read_tracked_builds(root, memory_root)
        except DesignRefusal as e:
            print(f"design-lib: REFUSING — {e}")
            return 1
        kept, skipped = scan_chain_specs(tracked, design["builds"], cutoff, memory_root)
        for b, p in kept:
            print(f"  {b} {p}")
        print(f"design-lib: chain specs {len(kept)} in {len({b for b, _ in kept})} build(s) dated on or after "
              f"{cutoff} · passed over: other-build {skipped['other-build']}, pre-cutoff "
              f"{skipped['pre-cutoff']}, undated {skipped['undated']}, unnamed {skipped['unnamed']}")
        return 0
    nodes = design["nodes"]
    print(f"design-lib: design at {design['baseline'][:9]} · view {design['view']} · {len(design['rows'])} "
          f"clause(s) across {len(design['builds'])} build(s) · {len(design['retired'])} withdrawn · "
          f"{sum(len(v) for v in nodes.values())} owned node(s)")
    if build is None:
        return 0
    if build not in design["builds"]:
        print(f"design-lib: REFUSING — {build} is no chain build of the view {design['view']}")
        return 1
    clauses = design["builds"][build]
    print(f"design-lib: {build} · {len(clauses)} clause(s) · {len(nodes.get(build, ()))} owned node(s)")
    for cid, (_, h, since) in clauses.items():
        print(f"  {cid} {h} {since}")
    for n in sorted(nodes.get(build, ())):
        print(f"  node {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
