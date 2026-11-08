"""edge_grammar — the edge-type registry's reader, the one edge parser, and the edge check over every site
(PLAY-dOrderedCharter-24, PLAY-dOrderedCharter-28).

    python edge_grammar.py --list
    python edge_grammar.py --parse <file>
    python edge_grammar.py --check [--base <rev>]
    python edge_grammar.py --fixture --plant <case>

THE REGISTRY is `edges.toml` beside this file: one `[[edge]]` row per type of one closed set, with
`type`, `inverse`, `from`, `to`, `pin` (`none`, `tag` or `clause`), `status` (`declared` or `derived`)
and `declared-at`, and an optional `writer`, the one site that writes the type, so an edge of it read at
any other site is red. An inverse is derived from its row, never declared at a site. Its `[[trailer]]`
rows map each commit trailer key to the type it declares, so a key is registered once.

NATIVE IDS. `namespaces.toml`'s `[[native]]` rows register each native-id class: `class`, `owner`,
`pattern` (`<module>:<name>`, the memory-tree regex or grammar accessor that compiles it, never a second
regex) and `resolver` (`<module>:--<flag>`, a script whose lines are the members, or `<module>:<function>`).
A row's `from` and `to` may name a class beside the namespace words.

THE GRAMMAR. At a Markdown site an edge is one line at column 0, `**Edges:** type=target[,target]`, one
line per type, outside code fences. A target holds no space, comma or bracket and is one address form:
`tag` (`TAG_RE`), `pinned-tag` (`<tag>@<hash8>`), `section` (`<tag>#<seg>`), `id` (a native id),
`id#tag` (`<id>#<seg>(.<seg>)*`) or `pinned-id` (`<id>@<hash8>`). A pinned tag is legal only on a row
whose `pin` is `tag` (`amends`, `supersedes`), a pinned id only on one whose `pin` is `clause`
(`carries-clause`); a final eight-hex run behind `:`, `/` or `=` is red, since a pin is written `@<hash8>`.

THE SITES, one adapter each: a record's header (`**Serves:**` through `tree_lib.read_bindings`,
`**Caused-by:**`, `**Made-by:**`), a record's section (`**Edges:**`), an instruction unit's row (`edges`,
`scope`, `required-by`, `enforced-by`, read through the registry's `parse_unit_rows`), code (a `gov:note` line's `refs=` segment), a commit's trailers
(the `[[trailer]]` table), a work order's `gov:handoff` marker (`unit=` and `build=`) and a spec's
`**Carries:**` line (through `design_lib.parse_binding_lines`, its one parser).

RESOLUTION. A tag or section resolves through the tag index's `resolve_address`; a pinned tag when some
committed revision of its unit's text hashes to its pin (`derive_pin_hash`); a native id when its class's
resolver prints it; a pinned clause id when the clause's text in some committed revision of the design
view hashes to its pin (`derive_clause_hash`), the baseline's included.

Every line opens `edges:`. Exit 0 green, 1 red or a malformed edge line, 2 an unreadable registry.
What it does not check: an edge's source against its row's `from`, since no source namespace (record,
commit, act) is registered; an `id#tag` target, `unarmed` until dTotalRecall arms the record namespace;
an id whose class is not registered, `unarmed`; and a `serves` target no spec defines, which check 21
reds, so `--check` counts it as unresolved and adds no second verdict.
"""
from __future__ import annotations

import argparse
import importlib
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import tomllib

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import tag_index as ti  # noqa: E402

EDGE_HEAD = "**Edges:**"
GRAMMAR = "`**Edges:** type=target[,target]`, one line per type"
EDGE_FIELDS = ("type", "inverse", "from", "to", "pin", "status", "declared-at")
NATIVE_FIELDS = ("class", "owner", "pattern", "resolver")
TYPE_RE = re.compile(r"[a-z][a-z0-9-]*")
_ID = r"[A-Za-z0-9][A-Za-z0-9_-]*"
_HASH8 = r"@[0-9a-f]{8}"
PIN_SEP = re.compile(r"[:/=][0-9a-f]{8}$")
# One pattern per address form, tried in order; group 1 is the tag whose first segment is its namespace.
FORMS = (
    ("tag", re.compile(rf"({ti.TAG_RE.pattern})")),
    ("pinned-tag", re.compile(rf"({ti.TAG_RE.pattern}){_HASH8}")),
    ("section", re.compile(rf"({ti.TAG_RE.pattern})#{ti.SEG}")),
    ("id", re.compile(_ID)),
    ("id#tag", re.compile(rf"{_ID}#{ti.SEG}(?:\.{ti.SEG})*")),
    ("pinned-id", re.compile(rf"{_ID}{_HASH8}")),
)
#: the pin word each pinned form needs on its row
PIN_OF = {"pinned-tag": "tag", "pinned-id": "clause"}
HEADER_RE = re.compile(r"^\*\*(Caused-by|Made-by):\*\*[ \t]+(\S.*?)[ \t]*$")
NOTE_RE = re.compile(r"^[ \t]*(?:#+|//|--|;|/?\*+|<!--)[ \t]*gov:note[ \t].*?[ \t]refs=(.*?)[ \t]*(?:-->|\*/)?[ \t]*$")
UNIT_FIELDS = (("scope", "instructs", False), ("required-by", "instructs", True), ("enforced-by", "enforces", True))


class EdgeError(RuntimeError):
    """An unreadable or malformed registry: the CLI exits 2, since nothing was graded."""


class EdgeRefusal(ValueError):
    """One refusal naming every malformed edge line of a text."""


def read_toml_rows(path, table, label) -> list:
    path = pathlib.Path(path)
    try:
        return tomllib.loads(path.read_text(encoding="utf-8")).get(table) or []
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise EdgeError(f"the {label} {path.as_posix()} is unreadable: {exc}") from None


def read_edge_types(path=None) -> dict:
    """`{type: row}` of the registry's `[[edge]]` rows, each carrying every field of EDGE_FIELDS, or
    EdgeError: a missing field, a `pin` or `status` outside its words, a type or inverse named twice."""
    path = pathlib.Path(path or KIT_DIR / "edges.toml")
    types, words = {}, set()
    for i, row in enumerate(read_toml_rows(path, "edge", "edge registry"), 1):
        missing = [f for f in EDGE_FIELDS if not row.get(f)]
        if missing:
            raise EdgeError(f"{path.as_posix()}: edge row {i} lacks {', '.join(missing)}")
        if row["pin"] not in ("none", "tag", "clause") or row["status"] not in ("declared", "derived"):
            raise EdgeError(f"{path.as_posix()}: edge '{row['type']}' has pin '{row['pin']}' and status "
                            f"'{row['status']}': pin is none, tag or clause, status declared or derived")
        for word in (row["type"], row["inverse"]):
            if word in words:
                raise EdgeError(f"{path.as_posix()}: '{word}' is named twice as a type or an inverse")
            words.add(word)
        types[row["type"]] = row
    if not types:
        raise EdgeError(f"{path.as_posix()}: holds no [[edge]] row, which is never an empty set")
    return types


def read_trailer_keys(types, path=None) -> dict:
    """`{trailer key: type}` of the registry's `[[trailer]]` rows, or EdgeError: a key named twice, or a
    type the closed set does not hold."""
    path = pathlib.Path(path or KIT_DIR / "edges.toml")
    keys = {}
    for i, row in enumerate(read_toml_rows(path, "trailer", "edge registry"), 1):
        key, kind = row.get("key"), row.get("type")
        if not key or kind not in types or key in keys:
            raise EdgeError(f"{path.as_posix()}: trailer row {i} needs a key named once and a type of the set")
        keys[key] = kind
    return keys


def read_native_classes(path, root) -> dict:
    """`{class: row}` of the namespace registry's `[[native]]` rows, each with its compiled pattern under
    `re`, or EdgeError: a missing field, a class named twice, a pattern that names nothing."""
    path = pathlib.Path(path)
    ti.load_memory_tree()   # puts memory-tree on sys.path, where every pattern's module lives
    classes = {}
    for i, row in enumerate(read_toml_rows(path, "native", "namespace registry"), 1):
        missing = [f for f in NATIVE_FIELDS if not row.get(f)]
        if missing or row.get("class") in classes:
            raise EdgeError(f"{path.as_posix()}: native row {i} " + (f"lacks {', '.join(missing)}" if missing
                            else f"names the class '{row['class']}' twice"))
        mod, _, name = row["pattern"].partition(":")
        try:
            pat = getattr(importlib.import_module(mod), name)
        except (ImportError, AttributeError) as exc:
            raise EdgeError(f"{path.as_posix()}: native '{row['class']}' pattern {row['pattern']}: {exc}") from None
        if callable(pat):   # ponytail: a grammar accessor, `grammar_for(root).ID`; a third shape names its own read
            pat = pat(root).ID
        classes[row["class"]] = {**row, "re": re.compile(pat)}
    return classes


def derive_native_class(target, classes):
    """The class whose pattern matches `target`'s id, its pin and section cut off; None for none."""
    base = re.split(r"[@#]", target, maxsplit=1)[0]
    return next((c for c, row in classes.items() if row["re"].fullmatch(base)), None)


def read_native_members(row, root, conf) -> dict | None:
    """`{member: the row it prints}` of one class, from its resolver, or None where the class is not armed
    here (no id grammar installed, or the DESIGN_* keys blank)."""
    tree_lib, _ = ti.load_memory_tree()
    mod, _, name = row["resolver"].partition(":")
    if name.startswith("--"):
        script = pathlib.Path(tree_lib.__file__).parent / f"{mod}.py"
        p = subprocess.run([sys.executable, str(script), name], cwd=str(root), capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        if p.returncode == 3:
            return None
        if p.returncode:
            raise EdgeError(f"native '{row['class']}': {row['resolver']} exited {p.returncode}: {p.stdout[-300:]}")
        return {ln: f"{row['class']} {ln} (owner {row['owner']})" for ln in p.stdout.splitlines()
                if ln and not ln.startswith("#")}
    # ponytail: the one function resolver is read_design_view, which takes the conf's DESIGN_VIEW; a third
    # class whose resolver takes another argument names its call here
    view = (conf.get("DESIGN_VIEW") or "").strip()
    if not view:
        return None
    fn = getattr(importlib.import_module(mod), name)
    return {cid: f"{row['class']} {cid} · {build} · {text}" for build, cid, text, _h, _s in fn(view, str(root))}


def parse_edge_target(text):
    """`(form, ns)` of one target, `ns` the namespace of a tag form and None for an id form; or None
    when the target matches no address form."""
    for form, pat in FORMS:
        m = pat.fullmatch(text)
        if m:
            return form, (m.group(1).split(".")[0] if m.groups() else None)
    return None


def derive_target_fault(t):
    """Why one target fails the grammar, or None when it is well formed."""
    if not t:
        return "holds an empty target, a comma with no target beside it"
    if re.search(r"\s", t):
        return f"holds the target '{t}', and a target holds no space"
    if re.search(r"[][(){}<>]", t):
        return f"holds the target '{t}', and a target holds no bracket"
    if parse_edge_target(t) is not None:
        return None
    if PIN_SEP.search(t):
        return f"holds the target '{t}', and a pin is written `@<hash8>`"
    if "@" in t:
        return f"holds the target '{t}', whose pin hash is not eight hex digits"
    if "#" in t:
        return f"holds the target '{t}', a malformed section target: a section is written `<doc>#<seg>`"
    return f"holds the target '{t}', which matches no address form ({', '.join(f for f, _ in FORMS)})"


def parse_edge_lines(text, path) -> list[dict]:
    """Every edge line of `text`, `{path, line, type, targets, site}` each, in line order.

    Walks `tree_lib.unfenced_lines`, so a fenced line is never an edge. Every line opening with
    `**Edges:**` at column 0 that fails the grammar is collected, and one EdgeRefusal (a ValueError)
    names each `path:line`, the line and the grammar; a text ending inside an open fence is refused
    naming the fence's line."""
    tree_lib, _ = ti.load_memory_tree()
    edges, bad = [], []
    for n, line in tree_lib.unfenced_lines(text):
        if line is None:
            bad.append(f"{path}:{n}: a fence opens here and never closes, so every line after it would go unread")
            continue
        if not line.lstrip().startswith(EDGE_HEAD):
            continue
        shown = line.rstrip()
        if not line.startswith(EDGE_HEAD):   # an indented edge line is malformed, never passed over unread
            bad.append(f"{path}:{n}: `{shown}` is indented, and an edge line sits at column 0; the grammar is {GRAMMAR}")
            continue
        pair = shown[len(EDGE_HEAD):]
        kind, eq, rest = pair[1:].partition("=")
        targets = rest.split(",")
        why = None
        if not pair.startswith(" ") or not eq:
            why = "holds no `type=` pair"
        elif "=" in rest and not any(PIN_SEP.search(t) for t in targets):
            why = "carries a second `type=` pair, and a line holds one type"
        elif not TYPE_RE.fullmatch(kind):
            why = f"names the type '{kind}', which is no type word [a-z][a-z0-9-]*"
        else:
            why = next(filter(None, map(derive_target_fault, targets)), None)
        if why:
            bad.append(f"{path}:{n}: `{shown}` {why}; the grammar is {GRAMMAR}")
            continue
        edges.append({"path": path, "line": n, "type": kind, "targets": targets, "site": "section"})
    if bad:
        raise EdgeRefusal(f"edges: {path}: {len(bad)} edge line(s) refused:\n" + "\n".join(f"  {b}" for b in bad))
    return edges


# ------------------------------------------------------------------------------------------ the adapters

def read_section_edges(text, path) -> list[dict]:
    """A record section's `**Edges:**` lines, through the one parser."""
    return parse_edge_lines(text, path)


def read_header_edges(text, path, binding=None) -> list[dict]:
    """A record header's edges: `**Serves:**` as `serves`, its ids `tree_lib.read_bindings`' (`binding`, that
    reader's row for `path`, None for a text it did not read), and the column-0 `**Caused-by:**` and
    `**Made-by:**` lines of the same head as `caused-by` and `made-by`, one target each, backticks cut."""
    tree_lib, _ = ti.load_memory_tree()
    edges = []
    for n, line in list(tree_lib.unfenced_lines(text))[:tree_lib.BIND_HEAD_LINES]:
        if line is None:
            break
        mb = tree_lib.BIND_RE.match(line)
        if binding and binding.get("ids") and mb and mb.group("key") == "Serves":
            edges.append({"path": path, "line": n, "type": "serves", "targets": list(binding["ids"]), "site": "header"})
            binding = None
            continue
        m = HEADER_RE.match(line)
        if m:
            edges.append({"path": path, "line": n, "type": m.group(1).lower(), "targets": [m.group(2).strip("`")],
                          "site": "header"})
    return check_site_targets(edges, path)


def check_site_targets(edges, path) -> list[dict]:
    """`edges` whose every target is well formed, or one EdgeRefusal naming each that is not: a site
    read by its own adapter answers to the one target grammar too."""
    bad = [f"{e['path']}:{e['line']}: {e['type']} {why}" for e in edges
           for why in filter(None, map(derive_target_fault, e["targets"]))]
    if bad:
        raise EdgeRefusal(f"edges: {path}: {len(bad)} target(s) refused:\n" + "\n".join(f"  {b}" for b in bad))
    return edges


def read_carries_edges(text, path) -> list[dict]:
    """A spec's `**Carries:**` lines as `carries-clause` edges, read by `design_lib.parse_binding_lines`
    (its `CARRY`), the pin carried; a `node:` carry is no clause and no edge. Refuses as that reader does."""
    ti.load_memory_tree()
    import design_lib
    return [{"path": path, "line": b["line"], "type": "carries-clause", "site": "spec",
             "targets": [f"{b['clause']}@{b['hash']}" if b["hash"] else b["clause"]]}
            for b in design_lib.parse_binding_lines(text, path) if b["kind"] == "carries" and b["clause"]]


def read_unit_edges(text, path) -> list[dict]:
    """An instruction unit file's `[[unit]]` rows, read through the registry's `parse_unit_rows`: each row's
    `edges` list in the edge grammar, its `scope` as `instructs` targets, its `required-by` as the sources
    that instruct it and a list `enforced-by` as the sources that enforce it, the string `none — <why>`
    none. A row the reader cannot read and a malformed entry are each an EdgeRefusal line naming it."""
    from instruction_units import parse_unit_rows
    units, faults = parse_unit_rows(text, path)
    edges, bad = [], [str(f) for f in faults]
    for u in units:
        tag = u.tag or ""
        at = {"path": path, "line": u.line, "site": "unit"}
        for entry in u.edges:
            kind, _, rest = entry.partition("=")
            why = None if TYPE_RE.fullmatch(kind) and rest else "holds no `type=` pair"
            why = why or next(filter(None, map(derive_target_fault, rest.split(","))), None)
            if why:
                bad.append(f"{path}:{u.line}: unit {tag} edges entry '{entry}' {why}")
            else:
                edges.append({**at, "type": kind, "targets": rest.split(","), "source": tag})
        for field, kind, inbound in UNIT_FIELDS:
            vals = getattr(u, field.replace("-", "_"))
            for v in vals if isinstance(vals, tuple) else ():
                edges.append({**at, "type": kind, "targets": [tag] if inbound else [v],
                              "source": v if inbound else tag})
    if bad:
        raise EdgeRefusal(f"edges: {path}: {len(bad)} unit edge(s) refused:\n" + "\n".join(f"  {b}" for b in bad))
    return edges


def read_change_edges(text, path) -> list[dict]:
    """A change record's `Promoted-from` field as a `promoted-from` edge at `instructions.edit`, the site its
    row names as its one writer."""
    from instruction_units import read_change_fields
    fields = read_change_fields(text)
    if "Promoted-from" not in fields:
        return []
    n = next(i for i, ln in enumerate(text.splitlines(), 1) if ln.startswith("- **Promoted-from:**"))
    return check_site_targets([{"path": path, "line": n, "type": "promoted-from", "site": "instructions.edit",
                                "targets": [fields["Promoted-from"]], "source": fields.get("Unit", "")}], path)


def read_note_refs(text, path) -> list[dict]:
    """Each code note's `refs=` segment, its targets in the edge-target form, as the derived `cites`
    edges a note's references are. A malformed segment is an EdgeRefusal naming its line."""
    edges, bad = [], []
    for n, line in enumerate(text.splitlines(), 1):
        m = NOTE_RE.match(line)
        if not m:
            continue
        targets = m.group(1).split(",")
        why = next(filter(None, map(derive_target_fault, targets)), None)
        if why:
            bad.append(f"{path}:{n}: `{line.strip()}` refs segment {why}")
        else:
            edges.append({"path": path, "line": n, "type": "cites", "targets": targets, "site": "note"})
    if bad:
        raise EdgeRefusal(f"edges: {path}: {len(bad)} note refs segment(s) refused:\n" + "\n".join(f"  {b}" for b in bad))
    return edges


def read_handoff_edges(text, path) -> list[dict]:
    """A work order's `gov:handoff` marker, read by the roles kit's `MARKER_RE`: its `unit=`, where it
    names one, and its `build=` as `serves` targets."""
    from policy_value import resolve_kit_dir
    roles = resolve_kit_dir("roles", "roles_lib.py", KIT_DIR)
    if str(roles) not in sys.path:
        sys.path.append(str(roles))
    from roles_lib import MARKER_RE
    edges = []
    for m in MARKER_RE.finditer(text):
        n = text.count("\n", 0, m.start()) + 1
        targets = [t for t in (m.group(3), m.group(2)) if t != "-"]
        edges.append({"path": path, "line": n, "type": "serves", "targets": targets, "site": "work-order"})
    return check_site_targets(edges, path)


def read_trailer_edges(root, base, keys) -> list[dict]:
    """Every registered trailer of the commits in `base..HEAD`, one `git log`: `Decided:` a `decides`
    edge to its commit, every other key its value's whitespace- or comma-split targets, `Pass: none`
    none."""
    out = ti.read_git(root, "log", "--format=%H%x1f%(trailers:only,unfold)%x1e", f"{base}..HEAD")
    edges = []
    for chunk in out.split("\x1e"):
        sha, _, block = chunk.strip("\n").partition("\x1f")
        for n, line in enumerate(block.splitlines(), 1):
            key, sep, value = line.partition(": ")
            if not sep or key not in keys:
                continue
            at = {"path": f"commit {sha[:12]}", "line": n, "type": keys[key], "site": "commit", "key": key}
            if keys[key] == "decides":
                edges.append({**at, "targets": [sha], "source": value.strip()})
            elif value.strip() != "none":
                edges.append({**at, "targets": [t for t in re.split(r"[\s,]+", value.strip()) if t]})
    return check_site_targets(edges, f"{base}..HEAD")


# ------------------------------------------------------------------------------------------ the checks

def check_edges(edges, types, namespaces, classes=None) -> list[str]:
    """The closed set's reds over parsed edges, one line each; `namespaces` the registry's rows, `classes`
    its native classes. An id target matching no class, where the row's `to` names a word no row
    registers yet, is noted `unarmed` on its edge rather than red."""
    classes = classes or {}
    registered = {r["ns"]: r["role"] for r in namespaces}
    inverses = {r["inverse"]: t for t, r in types.items()}
    reds = []
    for e in edges:
        at, kind = f"{e['path']}:{e['line']}", e["type"]
        row = types.get(kind)
        if row is None:
            reds.append(f"edges: {at} · {kind} · " + (
                f"is the inverse of {inverses[kind]}, derived from its row and never declared" if kind in inverses
                else "is no type of edges.toml's closed set"))
            continue
        if row["status"] == "derived" and e.get("site") != "note":
            reds.append(f"edges: {at} · {kind} · is derived ({row['declared-at']}), never declared")
            continue
        if row.get("writer") and e.get("site") != row["writer"]:
            reds.append(f"edges: {at} · {kind} · is written by {row['writer']} alone, its one writer "
                        f"({row['declared-at']}), never at a {e.get('site', 'section')} site")
            continue
        to = row["to"]
        for t in e["targets"]:
            form, ns = parse_edge_target(t)
            if form in PIN_OF and row["pin"] != PIN_OF[form]:
                reds.append(f"edges: {at} · {kind}={t} · pins a target, and {kind}'s row says pin = \"{row['pin']}\""
                            + (": a pin on a type whose row admits none" if row["pin"] == "none"
                               else f"; a {form} is legal only where pin = \"{PIN_OF[form]}\""))
            if ns is None:
                cls = derive_native_class(t, classes)
                ok = "any" in to or cls in to
                if not ok and cls is None and any(w not in registered and w not in classes for w in to
                                                  if w not in ("any", "selects")):
                    e.setdefault("unarmed", []).append(t)
                    ok = True
            else:
                ok = ns in registered and ("any" in to or ns in to or ("selects" in to and registered[ns] == "selects"))
            if not ok:
                reds.append(f"edges: {at} · {kind}={t} · is outside {kind}'s to [{', '.join(to)}]"
                            + ("" if ns is None or ns in registered else f"; namespace '{ns}' is not registered"))
    return reds


def read_text_history(root, path, extract, digest) -> dict:
    """`{key: {hash}}` over every committed revision of `path` at `root`, one `git log` and one
    `tree_lib.read_blobs_at`: `extract(text)` yields `(key, body)` per revision, `digest(body)` its hash."""
    tree_lib, _ = ti.load_memory_tree()
    revs = ti.read_git(root, "log", "--format=%H", "--", path).split()
    out: dict = {}
    for text in tree_lib.read_blobs_at(str(root), [(r, path) for r in revs]).values():
        for key, body in extract(text) if text is not None else ():
            out.setdefault(key, set()).add(digest(body))
    return out


def derive_unit_texts(text):
    """`(tag, body)` of each readable `[[unit]]` row of a unit file, through the registry's
    `parse_unit_rows`: its header line to the next table's."""
    from instruction_units import parse_unit_rows
    for u in parse_unit_rows(text, "")[0]:
        if u.tag:
            yield u.tag, u.body


def derive_view_texts(text):
    """`(clause id, text)` of each row of one revision of the design view, through `design_lib.VIEW_ROW`."""
    import design_lib
    for ln in text.split("\n"):
        m = design_lib.VIEW_ROW.match(ln.rstrip("\r"))
        if m:
            yield m.group(2), m.group(3)


def build_resolve_context(root, ns_path) -> dict:
    """What `resolve_edge` reads, each part loaded on first use: the repository, its conf, the native
    classes and their members, the tag index and the design view's clause revisions."""
    ti.load_memory_tree()
    import design_lib
    root = pathlib.Path(root)
    return {"root": root, "ns_path": pathlib.Path(ns_path), "conf": design_lib.read_design_conf(root),
            "classes": read_native_classes(ns_path, root), "members": {}, "con": None, "history": {}}


def read_tag_rows(rc, address):
    if rc["con"] is None:
        ctx = ti.derive_context(rc["root"], rc["ns_path"])
        rc["con"] = ti.load_index(rc["root"])
        ti.load_view(rc["con"], rc["root"], ctx)
    return ti.resolve_address(rc["con"], address, "leaf")


def resolve_edge(target, rc) -> tuple[str, str]:
    """`(state, row or reason)` of one target: `resolved` with its target's row, `red` with why,
    `unresolved` for an id its class does not hold, `unarmed` for a form or class not armed here."""
    import design_lib
    form, ns = parse_edge_target(target)
    base, _, pin = target.partition("@")
    if form == "id#tag":
        return "unarmed", "an id#tag target resolves once dTotalRecall arms the record namespace"
    if ns is not None:
        rows = read_tag_rows(rc, base)
        if not rows:
            return "red", "resolves to no row of the tag index"
        r = rows[0]
        if form == "pinned-tag":
            key = ("unit", r["path"])
            if key not in rc["history"]:
                rc["history"][key] = read_text_history(rc["root"], r["path"], derive_unit_texts, design_lib.derive_pin_hash)
            hashes = rc["history"][key].get(base, set())
            if pin not in hashes:
                return "red", (f"pins {pin}, which matches no text in its unit's history "
                               f"({len(hashes)} revision hash(es) of {base} in {r['path']})")
        return "resolved", f"{r['tag']} · {r['path']}:{r['line']}-{r['end_line']} · {r['text'].splitlines()[0] if r['text'] else ''}"
    cls = derive_native_class(base, rc["classes"])
    if cls is None:
        return "unarmed", "no registered native class holds it"
    if cls not in rc["members"]:
        rc["members"][cls] = read_native_members(rc["classes"][cls], rc["root"], rc["conf"])
    members = rc["members"][cls]
    if members is None:
        return "unarmed", f"the class {cls} is not armed here"
    if base not in members:
        return "unresolved", f"the class {cls} holds no {base}"
    if form == "pinned-id":
        view = rc["conf"].get("DESIGN_VIEW", "").strip()
        if ("view", view) not in rc["history"]:
            rc["history"][("view", view)] = read_text_history(rc["root"], view, derive_view_texts,
                                                              design_lib.derive_clause_hash)
        hashes = rc["history"][("view", view)].get(base, set())
        if pin not in hashes:
            return "red", (f"pins {base}@{pin}, which matches no revision of its clause "
                           f"({len(hashes)} revision hash(es) of {base} in {view})")
    return "resolved", members[base]


def run_resolve(edges, rc, lenient=("serves",)) -> tuple[list, dict]:
    """Resolve every target of every edge: `(reds, counts)`, each red one line naming its site and line.
    An unresolved target is red, but on a type of `lenient`, where it is counted: a `serves` target no
    spec defines is check 21's verdict, never a second one here."""
    reds, counts = [], {"resolved": 0, "unresolved": 0, "unarmed": 0}
    for e in edges:
        for t in e["targets"]:
            if t in e.get("unarmed", ()):
                counts["unarmed"] += 1
                continue
            state, why = resolve_edge(t, rc)
            line = f"edges: {e['path']}:{e['line']} · {e['type']}={t} · {why}"
            if state == "unresolved" and e["type"] not in lenient:
                state = "red"
            if state == "red":
                reds.append(line)
            else:
                counts[state] += 1
                if state == "resolved" and rc.get("verbose"):
                    print(f"edges: resolved · {e['path']}:{e['line']} · {e['type']}={t} · {why}")
    return reds, counts


def read_tree_edges(root, base) -> tuple[list, list]:
    """Every edge of the tree at `root`: `(edges, refusals)`, the refusals one line per malformed line.
    Markdown under MEMORY_ROOT is read for headers, sections, carries, markers and a change record's field;
    every unit manifest
    `derive_manifest_kind` names for units; every non-Markdown file naming a note for its refs; and the trailers of `base..HEAD`."""
    from instruction_units import CHANGE_RECORD_RE, derive_kit_prefix, derive_manifest_kind
    tree_lib, _ = ti.load_memory_tree()
    import design_lib
    conf = design_lib.read_design_conf(root)
    m = conf.get("MEMORY_ROOT", "memory").strip().strip("/") or "memory"
    tracked = ti.read_git(root, "ls-files", "-z").split("\0")
    bindings = tree_lib.read_bindings(str(root), tracked, conf)
    spec_re = design_lib.build_spec_file_re(m)
    grep = subprocess.run(["git", "-C", str(root), "grep", "-l", "-I", "-F", "gov:note", "--", ".", ":!*.md"],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")
    notes = set(grep.stdout.splitlines()) if grep.returncode == 0 else set()
    prefix = derive_kit_prefix()
    edges, bad = [], []
    for rel in tracked:
        md = rel.endswith(".md") and rel.startswith(m + "/")
        unit = derive_manifest_kind(rel, prefix) is not None
        if not (md or unit or rel in notes):
            continue
        try:
            text = (root / rel).read_bytes().decode("utf-8").replace("\r\n", "\n")
        except (OSError, UnicodeDecodeError):
            continue
        try:
            if md:
                edges += read_header_edges(text, rel, bindings.get(rel))
                if EDGE_HEAD in text:   # a text holding no edge head hides no edge line, fenced or not
                    edges += read_section_edges(text, rel)
                if spec_re.fullmatch(rel):
                    edges += read_carries_edges(text, rel)
                if "gov:handoff" in text:
                    edges += read_handoff_edges(text, rel)
                if CHANGE_RECORD_RE.search(rel):
                    edges += read_change_edges(text, rel)
            elif unit:
                edges += read_unit_edges(text, rel)
            else:
                edges += read_note_refs(text, rel)
        except (EdgeRefusal, design_lib.DesignRefusal) as exc:
            bad += [ln.strip() for ln in str(exc).splitlines()[1:]]
    if base:
        edges += read_trailer_edges(root, base, read_trailer_keys(read_edge_types()))
    return edges, bad


def run_check(root, base) -> int:
    """`--check`: every edge of the tree parsed, graded against the closed set and resolved; one line
    per red, one summary by type and by site."""
    root = pathlib.Path(root)
    why = ""
    if base is None:
        ti.load_memory_tree()
        from coverage_join import resolve_compare_base
        base, why = resolve_compare_base(root)
    if not base:
        print(f"edges: trailers · no base ({why}), so no commit trailer is read")
    types = read_edge_types()
    ns_path = KIT_DIR / "namespaces.toml"
    rc = build_resolve_context(root, ns_path)
    edges, reds = read_tree_edges(root, base)
    reds = [f"edges: refused · {r}" for r in reds]
    reds += check_edges(edges, types, ti.read_namespaces(ns_path), rc["classes"])
    try:
        r_reds, counts = run_resolve(edges, rc)
    finally:
        if rc["con"] is not None:
            rc["con"].close()
    reds += r_reds
    for r in reds:
        print(r)
    by_type, by_site = {}, {}
    for e in edges:
        by_type[e["type"]] = by_type.get(e["type"], 0) + 1
        by_site[e["site"]] = by_site.get(e["site"], 0) + 1
    print("edges: by type · " + ", ".join(f"{k} {v}" for k, v in sorted(by_type.items())))
    print("edges: by site · " + ", ".join(f"{k} {v}" for k, v in sorted(by_site.items())))
    trailers = {}
    for e in edges:
        if e["site"] == "commit":
            trailers[e["key"]] = trailers.get(e["key"], 0) + 1
    print(f"edges: trailers · {base[:12] if base else 'none'}..HEAD · "
          + (", ".join(f"{k}: {v}" for k, v in sorted(trailers.items())) or "none read"))
    print(f"edges: targets · {counts['resolved']} resolved, {counts['unresolved']} serves unresolved "
          f"(check 21's verdict), {counts['unarmed']} unarmed")
    print(f"edges: {'RED' if reds else 'green'} · {len(edges)} edge(s), {len(reds)} red")
    return 1 if reds else 0


def check_native_classes(root, ns_path) -> tuple[list, list]:
    """The native classes for `gov_tag.py check`'s summary: `(reds, lines)`, one line per class naming its
    owner and its population; a class that resolves nothing is red, one not armed here says so."""
    ti.load_memory_tree()
    import design_lib
    conf = design_lib.read_design_conf(root)
    reds, lines = [], []
    try:
        classes = read_native_classes(ns_path, root)
    except EdgeError as exc:
        return [f"tags: native · {exc}"], []
    for cls, row in classes.items():
        try:
            members = read_native_members(row, root, conf)
        except (EdgeError, design_lib.DesignRefusal) as exc:
            reds.append(f"tags: native · {cls} (owner {row['owner']}) · {exc}")
            continue
        if members is None:
            lines.append(f"tags: native · {cls} (owner {row['owner']}) · unarmed here")
        elif not members:
            reds.append(f"tags: native · {cls} (owner {row['owner']}) · resolves nothing through {row['resolver']}")
        else:
            lines.append(f"tags: native · {cls} (owner {row['owner']}) · {len(members)} members")
    return reds, lines


def derive_inverse_edges(edges, types=None) -> list[tuple]:
    """`(target, inverse, source)` for every target of every declared edge, `source` its `path:line`;
    derived from the registry row alone, never read from a site."""
    types = types if types is not None else read_edge_types()
    return [(t, types[e["type"]]["inverse"], f"{e['path']}:{e['line']}")
            for e in edges if e["type"] in types for t in e["targets"]]


def read_site_edges(path, text) -> list[dict]:
    """One file's edges by its kind: a code file's note refs, a Markdown file's header, sections and
    carries lines."""
    if not str(path).endswith(".md"):
        return read_note_refs(text, path)
    return read_header_edges(text, path) + read_section_edges(text, path) + read_carries_edges(text, path)


def run_parse(path, text, ns_path=None, rc=None) -> int:
    """Parse, print each edge, then grade, and with `rc` resolve; 0 green, 1 red or refused."""
    ti.load_memory_tree()
    import design_lib
    ns_path = ns_path or KIT_DIR / "namespaces.toml"
    try:
        edges = read_site_edges(path, text)
    except (EdgeRefusal, design_lib.DesignRefusal) as exc:
        print(exc if isinstance(exc, EdgeRefusal) else f"edges: {exc}")
        return 1
    types = read_edge_types()
    for e in edges:
        print(f"edges: {e['path']}:{e['line']} · {e['type']} · {', '.join(e['targets'])}")
    classes = rc["classes"] if rc else read_native_classes(ns_path, resolve_repo_root())
    reds = check_edges(edges, types, ti.read_namespaces(ns_path), classes)
    if rc and not reds:
        rc["verbose"] = True
        reds, _counts = run_resolve(edges, rc, lenient=())
    for r in reds:
        print(r)
    if not reds:
        for target, inverse, source in derive_inverse_edges(edges, types):
            print(f"edges: inverse · {target} {inverse} {source}")
    print(f"edges: {len(edges)} edge(s), {len(reds)} red" if reds else f"edges: green · {len(edges)} edge(s)")
    return 1 if reds else 0


def resolve_repo_root() -> pathlib.Path:
    return pathlib.Path(ti.read_git(KIT_DIR, "rev-parse", "--show-toplevel").strip())


#: §4's plants: each the site's text, and the role of the `feature` row its fixture registry adds, None for no row
PLANTS = {
    "good-block": ("# Fixture\n\n## A heading\n\n**Edges:** implements=feature.x\n**Edges:** tests=kit.y,kit.z\n",
                   "describes"),
    "fenced-edge": ("# Fixture\n\n```text\n**Edges:** implements=feature.x\n```\n", None),
    "space-target": ("**Edges:** tests=kit.y kit.z\n**Edges:** tests=kit.y\n**Edges:** tests=kit.y, kit.z\n", None),
    "comma-in-pair": ("**Edges:** tests,implements=kit.y\n**Edges:** tests=kit.y\n**Edges:** tests=kit.y,,kit.z\n",
                      None),
    "bracket-target": ("**Edges:** tests=[kit.y]\n**Edges:** tests=kit.y\n**Edges:** tests=kit.y,kit.z]\n", None),
    "two-types-one-line": ("**Edges:** tests=kit.y tests=kit.z\n**Edges:** tests=kit.y\n"
                           "**Edges:** implements=kit.y · tests=kit.z\n", None),
    "no-equals": ("**Edges:** tests kit.y\n**Edges:** tests=kit.y\n**Edges:** tests\n", None),
    "unregistered-type": ("**Edges:** frobs=kit.x\n", None),
    "declared-inverse": ("**Edges:** implemented-by=kit.x\n", None),
    "declared-cites": ("**Edges:** cites=kit.x\n", None),
    "outside-to": ("**Edges:** layer=kit.x\n", None),
    "pin-on-none": ("**Edges:** part-of=kit.x@1a2b3c4d\n", None),
    "selector-registered": ("**Edges:** instructs=feature.x\n", "selects"),
    "selector-describes": ("**Edges:** instructs=feature.x\n", "describes"),
    # PLAY-dOrderedCharter-28 §4: the pin reds the parser and the closed set answer, and the malformed sites
    "promoted-elsewhere": ("# Fixture\n\n## [lesson] A record section\n\n**Edges:** promoted-from=unit.x\n", None),
    "pin-no-at": ("**Edges:** amends=practice.land:1a2b3c4d\n", None),
    "pin-bad-hash": ("**Edges:** amends=practice.land@1a2b3c\n", None),
    "pin-other-type": ("**Edges:** part-of=kit.x@1a2b3c4d\n", None),
    "bad-section": ("# Fixture\n\n## [x] A section\n\n**Edges:** implements=doc.build-method#\n", None),
    "bad-block": ("# Fixture\n\n## [x] A section\n\n**Edges:** tests=kit.y implements=kit.z\n", None),
    "bad-note-refs": ("# gov:note layer.memory — x → y refs=a b\n", None),
}
#: §4's plants that resolve, each its site's name and text over the fixture repository; `{unit}` is the
#: first revision's unit pin and `{clause}` the clause's baseline pin
RESOLVE_PLANTS = {
    "resolve-tag": ("site.md", "**Edges:** layer=layer.memory\n"),
    "resolve-pinned-tag": ("site.md", "**Edges:** amends=unit.x@{unit}\n"),
    "pin-no-text": ("site.md", "**Edges:** amends=unit.x@00000000\n"),
    "resolve-section": ("site.md", "**Edges:** part-of=doc.build-method#m5-recall-and-reuse\n"),
    "resolve-family": ("site.md", "**Edges:** serves=PLAY-dOrderedCharter-28\n"),
    "resolve-clause": ("site.md", "**Edges:** carries-clause=cl-dAlpha-0001\n"),
    "resolve-pinned-clause": ("spec.md", "# PLAY-dOrderedCharter-28 — x\n\n**Carries:** cl-dAlpha-0001@{clause} whole\n"),
    "clause-no-rev": ("spec.md", "# PLAY-dOrderedCharter-28 — x\n\n**Carries:** cl-dAlpha-0001@00000000 whole\n"),
}
FIXTURE_VIEW = "| Build | Clause | Text | Since |\n|---|---|---|---|\n| dAlpha | `cl-dAlpha-0001` | {text} | {since} |\n"
FIXTURE_UNIT = '[[unit]]\ntag = "unit.x"\nhelp = "{help}"\n'


def build_edges_fixture(top, plant) -> tuple[pathlib.Path, pathlib.Path]:
    """`(site, registry)` under `top`: the plant's site text, and the shipped namespace registry with a
    `feature` row added where the plant names its role. The edge registry is the shipped file, unread
    and unwritten here."""
    from gov_tag import derive_fixture_row
    text, role = PLANTS[plant]
    top = pathlib.Path(top)
    site, reg = top / ("site.py" if plant == "bad-note-refs" else "site.md"), top / "namespaces.toml"
    site.write_text(text, encoding="utf-8", newline="")
    extra = derive_fixture_row("feature", "fixture_tags:extract_declared", role) if role else ""
    reg.write_text((KIT_DIR / "namespaces.toml").read_text(encoding="utf-8") + extra, encoding="utf-8", newline="")
    return site, reg


def build_resolve_fixture(top, plant) -> tuple[pathlib.Path, pathlib.Path, pathlib.Path]:
    """`(root, site, registry)`: gov_tag's fixture repository, then a spec defining PLAY-dOrderedCharter-28,
    a guide, the unit `unit.x` and a one-clause design view, each committed, and a second commit moving the
    unit's text and the clause's under a deviation; the registry carries the unit row and the shipped native
    rows. The plant's site sits beside the repository, its pins the first revision's hashes."""
    import gov_tag
    ti.load_memory_tree()
    import design_lib
    top = pathlib.Path(top)
    root = gov_tag.build_tags_fixture(top, "none")
    shipped = (KIT_DIR / "namespaces.toml").read_text(encoding="utf-8")
    reg = gov_tag.FIXTURE_REGISTRY + gov_tag.FIXTURE_UNIT_ROW + "\n" + shipped[shipped.index("\n[[native]]") + 1:]
    unit1, clause1 = FIXTURE_UNIT.format(help="the first text"), "the alpha clause `x`"
    gov_tag.write_commit(root, {
        ".memory-tree.conf": 'MEMORY_ROOT=memory\nCHARTER="AGENTS.md"\nFAMILIES="playbook:PLAY"\n'
                             'DESIGN_VIEW="memory/view.md"\n',
        f"{gov_tag.FIXTURE_KIT}/namespaces.toml": reg,
        "memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md":
            "# PLAY-dOrderedCharter-28 — the fixture unit\n\n**Status:** OPEN · rev-1 · 2026-10-23\n",
        "memory/guides/BUILD-METHOD.md": gov_tag.GUIDE.replace("# Alpha", "# Build method"),
        "tools/kitx/instructions.toml": unit1,
        "memory/view.md": FIXTURE_VIEW.format(text=clause1, since="baseline"),
    }, "edges base")
    gov_tag.write_commit(root, {
        "tools/kitx/instructions.toml": FIXTURE_UNIT.format(help="the second text"),
        "memory/view.md": FIXTURE_VIEW.format(text="the alpha clause `x`, moved", since="deviation `dev-1`"),
    }, "edges deviation")
    name, text = RESOLVE_PLANTS[plant]
    site = top / name
    site.write_text(text.format(unit=design_lib.derive_pin_hash(unit1), clause=design_lib.derive_clause_hash(clause1)),
                    encoding="utf-8", newline="")
    return root, site, root / gov_tag.FIXTURE_KIT / "namespaces.toml"


def run_fixture(plant) -> int:
    """One plant: a parse-and-grade plant over a scratch site, or a resolve plant over a scratch repository;
    `edges.toml` must come out unchanged."""
    shipped = (KIT_DIR / "edges.toml").read_bytes()
    top = tempfile.mkdtemp(prefix="edges-")
    try:
        if plant in RESOLVE_PLANTS:
            ti.load_memory_tree()  # PLAY-dOrderedCharter-69 S3: the caller's git variables aside for the plant
            from deviation_join import set_env_aside
            from tree_lib import GIT_ENV_LEAKS
            with set_env_aside(GIT_ENV_LEAKS):
                root, site, reg = build_resolve_fixture(top, plant)
                rc = build_resolve_context(root, reg)
                try:
                    rc_ = run_parse(site.name, site.read_text(encoding="utf-8"), reg, rc)
                finally:
                    if rc["con"] is not None:
                        rc["con"].close()
        else:
            site, reg = build_edges_fixture(top, plant)
            rc_ = run_parse(site.name, site.read_text(encoding="utf-8"), reg)
    finally:
        def remove_readonly(fn, path, _exc):
            os.chmod(path, stat.S_IWRITE)
            fn(path)
        shutil.rmtree(top, onerror=remove_readonly)
    same = (KIT_DIR / "edges.toml").read_bytes() == shipped
    print("edges: edges.toml unchanged" if same else "edges: edges.toml CHANGED by the fixture")
    return rc_ if same else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="edge_grammar.py", description="the edge registry, the edge parser and the edge check")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--parse", metavar="FILE")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--base", metavar="REV")
    ap.add_argument("--fixture", action="store_true")
    ap.add_argument("--plant", choices=sorted({*PLANTS, *RESOLVE_PLANTS}))
    a = ap.parse_args(argv)
    try:
        if a.list:
            types = read_edge_types()
            for t, r in types.items():
                print(f"edges: {t} · inverse {r['inverse']} · from {', '.join(r['from'])} · to {', '.join(r['to'])}"
                      f" · pin {r['pin']} · {r['status']}" + (f" · writer {r['writer']}" if r.get("writer") else ""))
            derived = sum(r["status"] == "derived" for r in types.values())
            print(f"edges: {len(types)} types, {len(types) - derived} declared, {derived} derived")
            for key, kind in read_trailer_keys(types).items():
                print(f"edges: trailer {key}: · {kind}")
            return 0
        if a.parse:
            p = pathlib.Path(a.parse)
            try:
                text = p.read_bytes().decode("utf-8").replace("\r\n", "\n")
            except (OSError, UnicodeDecodeError) as exc:
                print(f"edges: refused · {a.parse} cannot be read: {exc}", file=sys.stderr)
                return 2
            return run_parse(a.parse, text)
        if a.check:
            return run_check(resolve_repo_root(), a.base)
        if a.fixture and a.plant:
            return run_fixture(a.plant)
        ap.error("--list, --parse <file>, --check [--base <rev>], or --fixture --plant <case>")
    except (EdgeError, ti.TagError) as exc:
        print(f"edges: refused · {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    sys.exit(main())
