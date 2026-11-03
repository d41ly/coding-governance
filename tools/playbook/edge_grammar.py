"""edge_grammar — the edge-type registry's reader and the one edge parser (PLAY-dOrderedCharter-24).

    python edge_grammar.py --list
    python edge_grammar.py --parse <file>
    python edge_grammar.py --fixture --plant <case>

THE REGISTRY is `edges.toml` beside this file: one `[[edge]]` row per type of one closed set, with
`type`, `inverse`, `from`, `to`, `pin` (`none`, `tag` or `clause`), `status` (`declared` or `derived`)
and `declared-at`. An inverse is derived from its row, never declared at a site.

THE GRAMMAR. At a Markdown site an edge is one line at column 0, `**Edges:** type=target[,target]`, one
line per type, outside code fences. A target holds no space, comma or bracket and is one address form:
`tag` (`TAG_RE`), `pinned-tag` (`<tag>@<hash8>`), `section` (`<tag>#<seg>`), `id` (a native id),
`id#tag` (`<id>#<seg>(.<seg>)*`) or `pinned-id` (`<id>@<hash8>`).

THE CLOSED SET. An edge whose type no row holds, a declared inverse, a declared `cites`, a target whose
namespace is outside its row's `to`, and a pin on a row whose `pin` is `none` are red. A row's `to` names
namespace words of `namespaces.toml`, `any` (every registered namespace and every native id), or
`selects` (every namespace whose registry row has `role = "selects"`), so a selector a later build
registers is an `instructs` target with no edit here. A word not registered yet admits nothing.

Every line opens `edges:`. Exit 0 green, 1 red or a malformed edge line, 2 an unreadable registry.
What it does not check: an edge's source against its row's `from`, whether a target resolves to a node,
and a pin's hash; those are PLAY-dOrderedCharter-28's.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import re
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
TYPE_RE = re.compile(r"[a-z][a-z0-9-]*")
_ID = r"[A-Za-z0-9][A-Za-z0-9_-]*"
_HASH8 = r"@[0-9a-f]{8}"
# One pattern per address form, tried in order; group 1 is the tag whose first segment is its namespace.
FORMS = (
    ("tag", re.compile(rf"({ti.TAG_RE.pattern})")),
    ("pinned-tag", re.compile(rf"({ti.TAG_RE.pattern}){_HASH8}")),
    ("section", re.compile(rf"({ti.TAG_RE.pattern})#{ti.SEG}")),
    ("id", re.compile(_ID)),
    ("id#tag", re.compile(rf"{_ID}#{ti.SEG}(?:\.{ti.SEG})*")),
    ("pinned-id", re.compile(rf"{_ID}{_HASH8}")),
)


class EdgeError(RuntimeError):
    """An unreadable or malformed registry: the CLI exits 2, since nothing was graded."""


class EdgeRefusal(ValueError):
    """One refusal naming every malformed edge line of a text."""


def read_edge_types(path=None) -> dict:
    """`{type: row}` of the registry's `[[edge]]` rows, each carrying every field of EDGE_FIELDS, or
    EdgeError: a missing field, a `pin` or `status` outside its words, a type or inverse named twice."""
    path = pathlib.Path(path or KIT_DIR / "edges.toml")
    try:
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("edge") or []
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise EdgeError(f"the edge registry {path.as_posix()} is unreadable: {exc}") from None
    types, words = {}, set()
    for i, row in enumerate(rows, 1):
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


def parse_edge_target(text):
    """`(form, ns)` of one target, `ns` the namespace of a tag form and None for an id form; or None
    when the target matches no address form."""
    for form, pat in FORMS:
        m = pat.fullmatch(text)
        if m:
            return form, (m.group(1).split(".")[0] if m.groups() else None)
    return None


def parse_edge_lines(text, path) -> list[dict]:
    """Every edge line of `text`, `{path, line, type, targets}` each, in line order.

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
        why = None
        if not pair.startswith(" ") or not eq:
            why = "holds no `type=` pair"
        elif "=" in rest:
            why = "carries a second `type=` pair, and a line holds one type"
        elif not TYPE_RE.fullmatch(kind):
            why = f"names the type '{kind}', which is no type word [a-z][a-z0-9-]*"
        else:
            for t in rest.split(","):
                if not t:
                    why = "holds an empty target, a comma with no target beside it"
                elif re.search(r"\s", t):
                    why = f"holds the target '{t}', and a target holds no space"
                elif re.search(r"[][(){}<>]", t):
                    why = f"holds the target '{t}', and a target holds no bracket"
                elif parse_edge_target(t) is None:
                    why = (f"holds the target '{t}', which matches no address form "
                           f"({', '.join(f for f, _ in FORMS)})")
                if why:
                    break
        if why:
            bad.append(f"{path}:{n}: `{shown}` {why}; the grammar is {GRAMMAR}")
            continue
        edges.append({"path": path, "line": n, "type": kind, "targets": rest.split(",")})
    if bad:
        raise EdgeRefusal(f"edges: {path}: {len(bad)} edge line(s) refused:\n" + "\n".join(f"  {b}" for b in bad))
    return edges


def derive_inverse_edges(edges, types=None) -> list[tuple]:
    """`(target, inverse, source)` for every target of every declared edge, `source` its `path:line`;
    derived from the registry row alone, never read from a site."""
    types = types if types is not None else read_edge_types()
    return [(t, types[e["type"]]["inverse"], f"{e['path']}:{e['line']}")
            for e in edges if e["type"] in types for t in e["targets"]]


def check_edges(edges, types, namespaces) -> list[str]:
    """The closed set's reds over parsed edges, one line each; `namespaces` the registry's rows."""
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
        if row["status"] == "derived":
            reds.append(f"edges: {at} · {kind} · is derived ({row['declared-at']}), never declared")
            continue
        to = row["to"]
        for t in e["targets"]:
            form, ns = parse_edge_target(t)
            if form.startswith("pinned") and row["pin"] == "none":
                reds.append(f"edges: {at} · {kind}={t} · pins a target, and {kind}'s row says pin = \"none\"")
            if ns is None:
                ok = "any" in to   # ponytail: an id admits only under `any` until PLAY-dOrderedCharter-28 registers its classes
            else:
                ok = ns in registered and ("any" in to or ns in to or ("selects" in to and registered[ns] == "selects"))
            if not ok:
                reds.append(f"edges: {at} · {kind}={t} · is outside {kind}'s to [{', '.join(to)}]"
                            + ("" if ns is None or ns in registered else f"; namespace '{ns}' is not registered"))
    return reds


def run_parse(path, text, ns_path=None) -> int:
    """Parse, print each edge, then grade; 0 green, 1 red or refused."""
    try:
        edges = parse_edge_lines(text, path)
    except EdgeRefusal as exc:
        print(exc)
        return 1
    types = read_edge_types()
    for e in edges:
        print(f"edges: {e['path']}:{e['line']} · {e['type']} · {', '.join(e['targets'])}")
    reds = check_edges(edges, types, ti.read_namespaces(ns_path or KIT_DIR / "namespaces.toml"))
    for r in reds:
        print(r)
    if not reds:
        for target, inverse, source in derive_inverse_edges(edges, types):
            print(f"edges: inverse · {target} {inverse} {source}")
    print(f"edges: {len(edges)} edge(s), {len(reds)} red" if reds else f"edges: green · {len(edges)} edge(s)")
    return 1 if reds else 0


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
}


def build_edges_fixture(top, plant) -> tuple[pathlib.Path, pathlib.Path]:
    """`(site, registry)` under `top`: the plant's site text, and the shipped namespace registry with a
    `feature` row added where the plant names its role. The edge registry is the shipped file, unread
    and unwritten here."""
    from gov_tag import derive_fixture_row
    text, role = PLANTS[plant]
    top = pathlib.Path(top)
    site, reg = top / "site.md", top / "namespaces.toml"
    site.write_text(text, encoding="utf-8", newline="")
    extra = derive_fixture_row("feature", "fixture_tags:extract_declared", role) if role else ""
    reg.write_text((KIT_DIR / "namespaces.toml").read_text(encoding="utf-8") + extra, encoding="utf-8", newline="")
    return site, reg


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="edge_grammar.py", description="the edge registry and the edge parser")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--parse", metavar="FILE")
    ap.add_argument("--fixture", action="store_true")
    ap.add_argument("--plant", choices=sorted(PLANTS))
    a = ap.parse_args(argv)
    try:
        if a.list:
            types = read_edge_types()
            for t, r in types.items():
                print(f"edges: {t} · inverse {r['inverse']} · from {', '.join(r['from'])} · to {', '.join(r['to'])}"
                      f" · pin {r['pin']} · {r['status']}")
            derived = sum(r["status"] == "derived" for r in types.values())
            print(f"edges: {len(types)} types, {len(types) - derived} declared, {derived} derived")
            return 0
        if a.parse:
            p = pathlib.Path(a.parse)
            try:
                text = p.read_bytes().decode("utf-8").replace("\r\n", "\n")
            except (OSError, UnicodeDecodeError) as exc:
                print(f"edges: refused · {a.parse} cannot be read: {exc}", file=sys.stderr)
                return 2
            return run_parse(a.parse, text)
        if a.fixture and a.plant:
            with tempfile.TemporaryDirectory(prefix="edges-") as top:
                shipped = (KIT_DIR / "edges.toml").read_bytes()
                site, reg = build_edges_fixture(top, a.plant)
                rc = run_parse("site.md", site.read_text(encoding="utf-8"), reg)
                print("edges: edges.toml unchanged" if (KIT_DIR / "edges.toml").read_bytes() == shipped
                      else "edges: edges.toml CHANGED by the fixture")
                return rc if (KIT_DIR / "edges.toml").read_bytes() == shipped else 1
        ap.error("--list, --parse <file>, or --fixture --plant <case>")
    except (EdgeError, ti.TagError) as exc:
        print(f"edges: refused · {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    sys.exit(main())
