"""record_extract — the memory namespaces' extractors over the one tag index (TOOL-dTotalRecall-9 S1).

Each is one `[[namespace]]` row of `namespaces.toml` beside this file and keeps `tag_index`'s extractor
contract: `extract_<x>(ctx, path, None)` answers None for a path it does not read and `""` for one it
does, every tag it writes being whole; `extract_<x>(ctx, path, text)` returns the `(tag, kind, line,
end_line, text)` rows `tag_index._write_parsed` writes. A row of kind `tag` or `section` defines its tag
(`tag_index.DEFINE_KINDS`); a `record` row defines nothing.

  record   each `[[record-kind]]` row of memory-tree's `record-kinds.toml`, `record.<kind>` at its row,
           kind `tag`, so a pocket kind with no record file resolves; and one row per record, kind
           `record`, tag `record.<kind>` with `derive_record_kind`'s kind (empty where it answers
           None), text the record's key: an id-anchored entry of any Markdown under MEMORY_ROOT,
           `archive/` included, keyed by its id, a spec's defining H1 spanning its whole file; and a
           record file under a build's `build`, `reviews` or `prompts` folder, keyed by its stem.
  section  each `##` to `######` heading of a record file or a spec, kind `section`, `line` to the line
           before the next heading of its level or above, text the heading: an authored
           `[section.<seg>]` tag under `memory.legacy-anchors = retag`, the kind's `sections` table's tag
           where it maps the title, else `section.<derive_anchor>` under `derived`.
  feature  each feature-tag anchor in tracked code outside Markdown: the marker word `feature` after the
           `gov` prefix and a colon, then a `feature.<seg>` tag.
  class    each `<MEMORY_ROOT>/gotchas/*.md` whose front matter `gotchas.parse_front_matter` reads as
           kind `class`, `class.<name>`.
  marker   each `gov` marker word of tracked text whose word fits `seg`, `marker.<word>`, once per file
           at its first line.

The memory-tree modules are reached through `tag_index.load_memory_tree`, as every extractor may (§8 F7).
WHAT THESE DO NOT READ: a record file that is not UTF-8, and the policy value of `memory.legacy-anchors`
after the first read in a process, which keys no extractor version.
"""
from __future__ import annotations

import functools
import itertools
import os
import pathlib
import re
import sys

sys.dont_write_bytecode = True
KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import tag_index as ti  # noqa: E402

#: the folders whose files are records keyed by stem (memory-tree's `tree_lib.RECORD_KINDS` less `spec`)
FILE_RECORD_RE = r"/builds/[^/]+/(?:build|reviews|prompts)/[^/]+$"
SPEC_RE = r"/builds/[^/]+/spec/[^/]+\.md$"
HEADING_RE = re.compile(r"(?P<hashes>#{2,6}) (?P<text>.*\S)")
AUTHORED_RE = ti.AUTHORED_SECTION_RE   # the one authored-tag grammar, the anchor seed's (TOOL-dTotalRecall-43 S44)
FEATURE_RE = re.compile(r"\bgov:feature[ \t]+`?(feature(?:\." + ti.SEG + r")+)")
MARKER_RE = re.compile(r"\bgov:(" + ti.SEG + r")")


def load_memory_modules():
    """memory-tree's `tree_lib`, `id_grammar`, `record_kinds` and `gotchas`, through the index's one reach."""
    tree_lib, id_grammar = ti.load_memory_tree()
    import gotchas  # noqa: E402  memory-tree's, on the path load_memory_tree put it on
    import record_kinds  # noqa: E402
    return tree_lib, id_grammar, record_kinds, gotchas


@functools.cache
def read_kind_rows(root: str) -> tuple:
    """The record-kind registry's rows at `root`, read once per process; () where it does not read."""
    _t, _i, record_kinds, _g = load_memory_modules()
    try:
        return tuple(record_kinds.read_record_kinds(root) or ())
    except record_kinds.RecordKindsError:
        return ()


@functools.cache
def read_tree_written_kinds(root: str) -> dict:
    """`{path: Serves kind token or None}` over every tracked file under `root`'s memory root, each record's
    kind `tree_lib.read_bindings` classifies `bound`, read once per process through
    `record_kinds.read_written_kinds` (TOOL-dTotalRecall-53 S21); {} where git does not list the tree."""
    _t, _i, record_kinds, _g = load_memory_modules()
    try:
        tracked = record_kinds.read_tracked(root, f"{record_kinds.read_memory_root(root)}/**")
    except record_kinds.RecordKindsError:
        return {}
    return record_kinds.read_written_kinds(root, tracked)


@functools.cache
def read_anchor_mode(root: str) -> str:
    """`memory.legacy-anchors` at `root`, read once per process; its default where the read refuses."""
    load_memory_modules()
    import record_causes  # noqa: E402  the key's one reader (TOOL-dTotalRecall-19)
    try:
        return record_causes.read_anchor_value(root)
    except ValueError:
        return record_causes.ANCHOR_DEFAULT


def check_registry_path(ctx, path) -> bool:
    """Whether `path` is the record-kind registry under the tool root the namespace registry sits in."""
    _t, _i, record_kinds, _g = load_memory_modules()
    return ti._read_tool_file(ctx, path, record_kinds.KIT.name, record_kinds.REGISTRY)


def check_record_file(ctx, path) -> bool:
    return re.match(re.escape(ctx["memory_root"]) + FILE_RECORD_RE, path) is not None


def check_spec_file(ctx, path) -> bool:
    return re.match(re.escape(ctx["memory_root"]) + SPEC_RE, path) is not None


def derive_kind_row(ctx, path):
    """The record-kind row a record at `path` takes: `derive_record_kind`'s over the kind `read_bindings`
    classified (`read_tree_written_kinds`), else, for a spec, the row whose home admits it, so its
    `sections` table maps its headings."""
    _t, _i, record_kinds, _g = load_memory_modules()
    rows = list(read_kind_rows(str(ctx["root"])))
    row = record_kinds.derive_record_kind(path, read_tree_written_kinds(str(ctx["root"])).get(path), rows)
    if row is None and check_spec_file(ctx, path):
        row = next((r for r in rows if r.get("name") == "spec"), None)
    return row


def extract_record(ctx, path, text=None):
    """The `record` namespace: the registry's rows, and one `record` row per record (S1)."""
    mr = ctx["memory_root"]
    if text is None:
        if check_registry_path(ctx, path):
            return ""
        return "" if path.startswith(mr + "/") and (path.endswith(".md") or check_record_file(ctx, path)) else None
    if check_registry_path(ctx, path):
        return ti.derive_tag_rows(text, "record-kind")
    _t, id_grammar, record_kinds, _g = load_memory_modules()
    lines = text.splitlines()
    row = record_kinds.derive_record_kind(path, read_tree_written_kinds(str(ctx["root"])).get(path),
                                          list(read_kind_rows(str(ctx["root"]))))
    tag = f"record.{row['name']}" if row else ""
    out = []
    if check_record_file(ctx, path):
        out.append((tag, "record", 1, max(len(lines), 1), pathlib.PurePosixPath(path).stem))
    if not path.endswith(".md"):
        return out
    spec = check_spec_file(ctx, path)
    for rec in id_grammar.extract_records(path, text):
        start = rec["line"]
        end = len(lines) if spec and start == next(
            (n for n, ln in enumerate(lines, 1) if ln.startswith("# ")), 0) else start + rec["text"].count("\n")
        out.append((tag, "record", start, max(end, start), rec["id"]))
    return out


def extract_section(ctx, path, text=None):
    """The `section` namespace: each heading of a record file or a spec, its extent and its tag (S1)."""
    if text is None:
        return "" if (check_record_file(ctx, path) and path.endswith(".md")) or check_spec_file(ctx, path) else None
    tree_lib, _i, record_kinds, _g = load_memory_modules()
    mode = read_anchor_mode(str(ctx["root"]))
    row = derive_kind_row(ctx, path)
    try:
        sections = record_kinds.read_sections(row) if row else []
    except record_kinds.RecordKindsError:
        sections = []
    lines = text.splitlines()
    # TOOL-dTotalRecall-43 S44: the authored tags' anchors seed `seen` before any heading derives one
    heads, seen = [], ti.read_authored_anchors(
        m.group("text") for _n, line in itertools.takewhile(lambda nl: nl[1] is not None,
                                                            tree_lib.unfenced_lines("\n".join(lines)))
        for m in [HEADING_RE.fullmatch(line.rstrip())] if m)
    for n, line in tree_lib.unfenced_lines("\n".join(lines)):
        if line is None:
            break
        m = HEADING_RE.fullmatch(line.rstrip())
        if not m:
            continue
        title, authored = m.group("text"), AUTHORED_RE.match(m.group("text"))
        tag = None
        if authored:
            tag = f"section.{authored.group('seg')}" if mode == "retag" else None
        else:
            anchor = ti.derive_anchor(title, seen)
            tag = record_kinds.read_section_tag(sections, title) or (
                f"section.{anchor}" if anchor and mode == "derived" else None)
        heads.append((n, len(m.group("hashes")), tag, line.rstrip()))
    out = []
    for i, (n, level, tag, head) in enumerate(heads):
        end = next((k - 1 for k, lv, _t, _h in heads[i + 1:] if lv <= level), len(lines))
        if tag:
            out.append((tag, "section", n, max(end, n), head))
    return out


def extract_feature(ctx, path, text=None):
    """The `feature` namespace: each feature-tag anchor in tracked code outside Markdown (S1)."""
    if text is None:
        return None if path.endswith(".md") else ""
    out, seen = [], set()
    for n, line in enumerate(text.splitlines(), 1):
        for m in FEATURE_RE.finditer(line):
            if m.group(1) not in seen and ti.parse_tag(m.group(1))[1] is None:
                seen.add(m.group(1))
                out.append((m.group(1), "tag", n, n, line.strip()))
    return out


def extract_class(ctx, path, text=None):
    """The `class` namespace: each gotcha record `gotchas.py#build_record` reads as kind `class` (S1), the
    catalogue's own record builder, so a record with no `kind:` key reads as `gotchas.py` reads it
    (TOOL-dTotalRecall-43 S52)."""
    mr = ctx["memory_root"]
    if text is None:
        return "" if re.fullmatch(re.escape(mr) + r"/gotchas/[^/]+\.md", path) else None
    _t, _i, _r, gotchas = load_memory_modules()
    try:
        fm = gotchas.build_record(path, text.replace("\r\n", "\n"))
    except gotchas.Problem:
        return []
    tag = f"class.{fm['name']}"
    if fm["kind"] != "class" or ti.parse_tag(tag)[1] is not None:
        return []
    n = next((k for k, ln in enumerate(text.splitlines(), 1) if ln.startswith("name:")), 1)
    return [(tag, "tag", n, n, fm["description"])]


def extract_marker(ctx, path, text=None):
    """The `marker` namespace: each `gov` marker word of tracked text, once per file (S1)."""
    if text is None:
        return ""
    out, seen = [], set()
    for n, line in enumerate(text.splitlines(), 1):
        for m in MARKER_RE.finditer(line):
            tag = f"marker.{m.group(1)}"
            if tag not in seen and ti.parse_tag(tag)[1] is None:
                seen.add(tag)
                out.append((tag, "tag", n, n, line.strip()[:200]))
    return out
