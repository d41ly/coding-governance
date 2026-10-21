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
Blank or absent, nothing is read: `read_design` refuses naming each blank key, and the CLI exits 2.
The chain builds are the view's Build column; no build list is typed anywhere.

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
parameter of `scan_chain_specs`, read by the caller through `read_cutoff_key` in
`<prefix>/check-spec-tokens.py`, so the date has one reader. This module reads no date key.

Usage (from the repository root):
  python design_lib.py --parse <path>...           every binding of each file, or its refusal
  python design_lib.py --design [--build <slug>]   the counts read; with --build, that build's rows
  python design_lib.py --chain-specs <cutoff>      the chain builds' tracked specs dated on or after it
Exit 0 clean · 1 on a malformed line or a refusal · 2 when a DESIGN_* key is blank, so nothing was read.

What it does not read: whether a spec carries a clause it names, which is the carries join's; which
statuses carry; and any reader for an adopter — the keys are gov's, and an adopter's tree leaves them
blank.
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
from tree_lib import build_git_env, build_spec_path_re, parse_conf, unfenced_lines  # noqa: E402

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
VIEW_ROW = re.compile(r"^\| (d[A-Z]\w+) \| `(cl-d[A-Z]\w+-\d{4})` \| (.*) \| (baseline|deviation `([^`]+)`) \|$")
DESIGN_KEYS = ("DESIGN_RECORD", "DESIGN_BASELINE", "DESIGN_VIEW", "DESIGN_NODES")

_SPEC_DATE = re.compile(r"/(\d{4}-\d{2}-\d{2})-spec-")
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


def run_git(root, *args):
    """One git call at `root` under the kit's pin policy, its stdout as bytes; never raises on a
    non-zero exit, so each caller names its own refusal. Pathspecs are literal: a conf value is a
    path, never a glob or a magic signature."""
    return subprocess.run(["git", "--no-replace-objects", "--literal-pathspecs", "-C", str(root), *args],
                          capture_output=True, env=build_git_env())


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
    """
    path = pathlib.Path(root) / view
    try:
        text = path.read_text(encoding="utf-8")
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


def scan_chain_specs(paths, builds, cutoff, memory_root="memory"):
    """The chain builds' spec files among `paths`, `([(build, path)], {reason: count})`.

    A path is a spec when it sits under `<memory_root>/builds/<slug>/spec/`, at any depth, and ends
    `.md`; any other path is no spec and is not counted. A spec is kept when its build is one of
    `builds` and its filename date, read as `/(\\d{4}-\\d{2}-\\d{2})-spec-`, is on or after `cutoff`;
    what is passed over is counted as `other-build`, `pre-cutoff` and `undated`. A blank `cutoff`
    reads no date and keeps every chain-build spec, as the instrument reads them. Statuses are not
    read here: which statuses carry is the join's choice.
    """
    memory_root = str(memory_root).replace("\\", "/").rstrip("/")   # `memory/` would match no path
    spec_re = build_spec_path_re(memory_root)
    chain = set(builds)
    lead = len(memory_root) + len("/builds/")
    kept, skipped = [], {"other-build": 0, "pre-cutoff": 0, "undated": 0}
    for p in sorted({str(p).replace("\\", "/") for p in paths}):
        if not spec_re.match(p) or not p.endswith(".md"):
            continue
        build = p[lead:].split("/", 1)[0]
        if build not in chain:
            skipped["other-build"] += 1
            continue
        if cutoff:
            m = _SPEC_DATE.search(p)
            if not m:
                skipped["undated"] += 1
                continue
            if m.group(1) < cutoff:
                skipped["pre-cutoff"] += 1
                continue
        kept.append((build, p))
    return kept, skipped


def read_design(root, conf):
    """The design, read once from the four `DESIGN_KEYS` values of the caller's conf.

    Returns `{"baseline", "view", "rows", "builds", "retired", "nodes"}`: the pin, the view's path, its
    rows in view order, `{build: {cid: (text, hash8, since)}}`, the withdrawn ids at the baseline, and
    `{build: {"<ns>.<key>"}}`. A blank key is a refusal naming it, raised before anything is read.
    """
    values = {k: str(conf.get(k) or "").strip() for k in DESIGN_KEYS}
    blank = [k for k in DESIGN_KEYS if not values[k]]
    if len(blank) == len(DESIGN_KEYS):
        raise DesignRefusal("every DESIGN_* key is blank (" + ", ".join(DESIGN_KEYS) + "), so nothing was "
                            "read", blank=blank)
    if blank:
        raise DesignRefusal(f"{', '.join(blank)} {'is' if len(blank) == 1 else 'are'} blank, so nothing was "
                            "read", blank=blank)
    baseline = values["DESIGN_BASELINE"]
    if not re.fullmatch(r"[0-9a-f]{40}", baseline):
        raise DesignRefusal(f"DESIGN_BASELINE {baseline} is not a 40-hex commit pin")
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
    conf_path = root / ".memory-tree.conf"
    conf = parse_conf(conf_path.read_text(encoding="utf-8"), {}) if conf_path.exists() else {}
    try:
        design = read_design(root, conf)
    except DesignRefusal as e:
        print(f"design-lib: REFUSING — {e}")
        return 2 if e.blank else 1
    if verb == "--chain-specs":
        memory_root = (conf.get("MEMORY_ROOT") or "memory").replace("\\", "/").rstrip("/")
        r = run_git(root, "ls-files", "--", f"{memory_root}/builds")
        if r.returncode:
            print(f"design-lib: REFUSING — git ls-files over {memory_root}/builds failed, so no spec was read")
            return 1
        kept, skipped = scan_chain_specs(r.stdout.decode("utf-8", "replace").splitlines(), design["builds"],
                                         cutoff, memory_root)
        for b, p in kept:
            print(f"  {b} {p}")
        print(f"design-lib: chain specs {len(kept)} in {len({b for b, _ in kept})} build(s) dated on or after "
              f"{cutoff} · passed over: other-build {skipped['other-build']}, pre-cutoff "
              f"{skipped['pre-cutoff']}, undated {skipped['undated']}")
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
