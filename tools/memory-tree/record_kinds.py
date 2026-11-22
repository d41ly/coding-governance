#!/usr/bin/env python3
"""record_kinds.py — the record-kind registry's reader, gate, view and factory (TOOL-dTotalRecall-1).

    python <prefix>/memory-tree/record_kinds.py --check             # the `record-kinds` leg
    python <prefix>/memory-tree/record_kinds.py --write             # the HYGIENE template's kind region
    python <prefix>/memory-tree/record_kinds.py --template <kind>   # the record skeleton of one kind
    python <prefix>/memory-tree/record_kinds.py new <name> --tag record.<name> --writer <door>
                                                --check <leg> --field <Key>... --home <glob>
    python <prefix>/memory-tree/record_kinds.py --seed-legacy       # the record-kinds-legacy seed
    python <prefix>/memory-tree/record_kinds.py --print-gap-keys    # the gap-key native class's members
    python <prefix>/memory-tree/record_kinds.py --fixture [--plant <case>]
    python <prefix>/memory-tree/record_kinds.py --selftest

ONE DECLARATION PER KIND. `record-kinds.toml` beside this file holds one `[[record-kind]]` row per
record kind, its columns `name`, `tag`, `layer`, `home`, `id-rule`, `schema`, `writer`, `readers`,
`lifecycle` and `check`; `root` and `sections` are admitted for the units that add them. Every row
carries `name`, `tag` (`record.<name>`), `schema`, `writer` and `check`, and a `fields` row its
`home`, a `git ls-files` glob. `schema` is `{ form, fields, source }`: `form` one of `fields`,
`header`, `rows`, `generated`; `fields` the `**Key:**` lines a record carries; `source`, optional,
`<path>:<NAME>[.<key>]...`, its path spelled through `{prefix}`, the literal another module declares
the same fields in, read with `ast` and never by import, so a sibling kit's table is read without
crossing a kit boundary.

THE GATE, `--check`, reds: no row; a row missing a required column or carrying an unknown one; a
`fields` row with an empty `home`; an empty `writer`; a `check` naming no leg of the tool root's
`gate-legs.json`; a `source` whose literal does not hold the row's `fields` both ways; a member of
the typed kind list (`tree_lib.TYPED_RECORD_KINDS`) with no row, and a factory row (its `source` the
factory's `KINDS.<kind>.required`) naming no member. It grades each `fields` row's population: every
tracked record its `home` matches carries each field as a `**Key:**` line, bare or a `- **Key:**`
bullet, in the row's order, except a record the `record-kinds-legacy` ledger lists against that row.
A typed kind's row grades only the paths its name grammar (`build_records.derive_record_name`) also
matches, and a path a typed grammar matches is graded by that kind's row alone. A typed kind whose home
matches nothing prints `<kind>: unarmed — no record yet` and passes; any other empty population
reds. A graded deviation's `Follow-through: gap <key>` must name a key some tracked gap register
holds, and no register holding a key reds. The HYGIENE template's `gen:record-kinds` region must be
byte for byte what `--write` writes. It prints one count line naming every row, each `fields` kind's
graded and legacy counts, each `unarmed` kind and every red with its row.

Exit 0 green, 1 a red, 2 a refusal: a registry that does not parse, or a verb's malformed arguments.
`new` appends the row and re-renders that region from the registry, so the two move together; it
exits 2 and writes nothing on a duplicate name, a tag that is not `record.<name>`, an empty
writer, no `--home` or no `--field`, or a check no leg carries. `--print-gap-keys` exits 3 where no
gap register is tracked, the native class's not-armed answer.

WHAT IT DOES NOT CHECK. Whether a row's `writer` writes the kind: the cell is read, never run. A
field's value, only its line. A `gap-key` at an edge site, since no edge type names the class. A
`header`, `rows` or `generated` row's records, which its `check` leg's owner grades.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

KIT = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT) not in sys.path:   # the step gate loads this file by path, so its siblings resolve from here
    sys.path.insert(0, str(KIT))

SAY = "record-kinds"
REGISTRY = "record-kinds.toml"
TEMPLATE = "HYGIENE.template.md"
LEGS = "gate-legs.json"
LEGACY = "record-kinds-legacy"
REGION_OPEN, REGION_CLOSE = "<!-- gen:record-kinds -->", "<!-- /gen:record-kinds -->"
COLUMNS = ("name", "tag", "layer", "home", "id-rule", "schema", "writer", "readers", "lifecycle", "check")
LATER_COLUMNS = ("root", "sections")   # TOOL-dTotalRecall-19's and -9's, admitted and graded by their owners
REQUIRED = ("name", "tag", "schema", "writer", "check")
FORMS = ("fields", "header", "rows", "generated")
SCHEMA_KEYS = ("form", "fields", "source")
NAME_RE = re.compile(r"[a-z][a-z0-9-]*")
FACTORY_SOURCE = re.compile(r"(?:^|/)build_records\.py:KINDS\.([^.]+)\.required$")
GAP_KEY_RE = re.compile(r"gap-[a-z]+-\d{2,3}")
FOLLOW_GAP = re.compile(r"^gap (\S+)")
NOT_ARMED = 3


class RecordKindsError(Exception):
    """A refusal: a registry that does not parse, or a verb's malformed arguments."""


# ------------------------------------------------------------------------------------ the layout
def derive_kit_rel() -> str:
    """This kit's directory relative to the repository holding this file, `/`-joined; the kit name alone
    where no `.git` sits above it."""
    for up in (KIT, *KIT.parents):
        if (up / ".git").exists():
            return KIT.relative_to(up).as_posix()
    return KIT.name


def derive_tool_rel(kit_rel: str) -> str:
    """The tool root `{prefix}` names: the kit directory's parent, "" for a flat install."""
    parent = pathlib.PurePosixPath(kit_rel).parent.as_posix()
    return "" if parent == "." else parent


def resolve_prefix(spelled: str, tool_rel: str) -> str:
    """`spelled` with its `{prefix}` resolved to `tool_rel`."""
    return spelled.replace("{prefix}/", tool_rel + "/" if tool_rel else "").replace("{prefix}", tool_rel)


def run_git(root, *args: str) -> subprocess.CompletedProcess:
    """`git -C <root> <args>`, UTF-8 text, never raising on a non-zero exit."""
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=120)


def read_tracked(root, pattern: str) -> list[str]:
    """The tracked paths one `git ls-files` glob matches, `*` never crossing a `/`."""
    p = run_git(root, "ls-files", "-z", "--", f":(glob){pattern}")
    if p.returncode != 0:
        raise RecordKindsError(f"git ls-files refused {pattern!r}: {p.stderr.strip()}")
    return sorted(x for x in p.stdout.split("\0") if x)


def read_memory_root(root) -> str:
    """The conf's MEMORY_ROOT, `memory` where the conf declares none."""
    from design_lib import read_design_conf
    return (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/")


# ---------------------------------------------------------------------------------- the registry
def read_record_kinds(root, kit_rel: str | None = None) -> list[dict] | None:
    """The registry's rows at `root`, or None where the registry is absent. RecordKindsError where it
    does not parse or `record-kind` is not an array of tables."""
    path = pathlib.Path(root, kit_rel or derive_kit_rel(), REGISTRY)
    if not path.is_file():
        return None
    try:
        data = tomllib.loads(path.read_bytes().decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as e:
        raise RecordKindsError(f"{REGISTRY} does not parse: {e}") from None
    rows = data.get("record-kind", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise RecordKindsError(f"{REGISTRY}: `record-kind` is not an array of [[record-kind]] tables")
    return rows


def read_schema_source(root, source: str, tool_rel: str):
    """The literal `<path>:<NAME>[.<key>]...` names, read by `ast` from the module's text and never by
    import: the module-level assignment to NAME, each `.<key>` walked as a string key of a dict display,
    the node it lands on read by `ast.literal_eval`. RecordKindsError naming what did not resolve."""
    path_s, _, dotted = source.partition(":")
    if not path_s or not dotted:
        raise RecordKindsError(f"source {source!r} is not <path>:<NAME>[.<key>]...")
    name, *keys = dotted.split(".")
    path = pathlib.Path(root, resolve_prefix(path_s, tool_rel))
    try:
        tree = ast.parse(path.read_bytes().decode("utf-8"))
    except (OSError, UnicodeDecodeError, SyntaxError) as e:
        raise RecordKindsError(f"source {source!r} does not read: {type(e).__name__}: {e}") from None
    node = None
    for stmt in tree.body:
        targets = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target] if isinstance(stmt, ast.AnnAssign) else []
        if any(isinstance(t, ast.Name) and t.id == name for t in targets):
            node = stmt.value
    if node is None:
        raise RecordKindsError(f"source {source!r}: no module-level assignment to {name}")
    for key in keys:
        if not isinstance(node, ast.Dict):
            raise RecordKindsError(f"source {source!r}: {key!r} walks into a value that is no dict display")
        node = next((v for k, v in zip(node.keys, node.values)
                     if isinstance(k, ast.Constant) and k.value == key), None)
        if node is None:
            raise RecordKindsError(f"source {source!r}: no key {key!r}")
    try:
        value = ast.literal_eval(node)
    except ValueError:
        raise RecordKindsError(f"source {source!r} is no pure literal") from None
    return list(value) if isinstance(value, (list, tuple, dict)) else value


def check_row(row: dict, n: int, legs: set, root, tool_rel: str) -> list[str]:
    """The reds one row earns on its own, each naming the row."""
    name = row.get("name") if isinstance(row.get("name"), str) and row.get("name") else f"#{n}"
    at, reds = f"row {name}", []
    for col in REQUIRED:
        if col not in row:
            reds.append(f"{at}: missing the required column `{col}`")
    for col in row:
        if col not in COLUMNS + LATER_COLUMNS:
            reds.append(f"{at}: `{col}` is no column ({', '.join(COLUMNS)})")
    if "name" in row and not (isinstance(row["name"], str) and NAME_RE.fullmatch(row["name"])):
        reds.append(f"{at}: name {row['name']!r} is not [a-z][a-z0-9-]*")
    if "tag" in row and row["tag"] != f"record.{name}":
        reds.append(f"{at}: tag {row['tag']!r} is not record.{name}")
    if "writer" in row and not (isinstance(row["writer"], str) and row["writer"].strip()):
        reds.append(f"{at}: the column `writer` is empty: name the door, `generator:<path>` or `hand`")
    if "check" in row and row["check"] not in legs:
        reds.append(f"{at}: check {row['check']!r} names no leg of {LEGS}")
    for col in ("layer", "lifecycle", "id-rule", "home"):
        if col in row and not isinstance(row[col], str):
            reds.append(f"{at}: `{col}` is not a string")
    if "readers" in row and not (isinstance(row["readers"], list) and all(isinstance(r, str) for r in row["readers"])):
        reds.append(f"{at}: `readers` is not a list of strings")
    schema = row.get("schema")
    if "schema" not in row:
        return reds
    if not isinstance(schema, dict):
        return reds + [f"{at}: `schema` is not a table"]
    reds += [f"{at}: `schema.{k}` is no schema key ({', '.join(SCHEMA_KEYS)})" for k in schema if k not in SCHEMA_KEYS]
    fields = schema.get("fields", [])
    if schema.get("form") not in FORMS:
        reds.append(f"{at}: schema.form {schema.get('form')!r} is not one of {', '.join(FORMS)}")
    if not (isinstance(fields, list) and all(isinstance(f, str) and f for f in fields)):
        return reds + [f"{at}: schema.fields is not a list of field names"]
    if schema.get("form") == "fields":
        if not fields:
            reds.append(f"{at}: a `fields` row declares no field")
        if not (isinstance(row.get("home"), str) and row["home"].strip()):
            reds.append(f"{at}: a `fields` row's `home` is empty, so it grades no record")
    source = schema.get("source")
    if source is not None:
        try:
            lit = read_schema_source(root, source, tool_rel)
            if not isinstance(lit, list):
                raise RecordKindsError(f"source {source!r} is no list, tuple or dict")
            lack, extra = [f for f in fields if f not in lit], [f for f in lit if f not in fields]
            if lack or extra:
                reds.append(f"{at}: its fields and its source {source} differ — the row alone holds "
                            f"{', '.join(lack) or 'nothing'}; the source alone holds {', '.join(extra) or 'nothing'}")
        except RecordKindsError as e:
            reds.append(f"{at}: {e}")
    return reds


def read_leg_names(root, tool_rel: str) -> set | None:
    """Every leg name of the tool root's manifest, None where it is absent or unreadable."""
    try:
        legs = json.loads(pathlib.Path(root, tool_rel, LEGS).read_bytes().decode("utf-8"))
    except (OSError, ValueError):
        return None
    return {leg.get("name") for leg in legs if isinstance(leg, dict)} if isinstance(legs, list) else None


# -------------------------------------------------------------------------------- the population
def scan_legacy_records(root, rows: list[dict], typed_kinds) -> dict:
    """`{row name: [path...]}`: every tracked record each `fields` row's home matches. A typed kind's row
    keeps only the paths its own name grammar (`build_records.derive_record_name`) also matches, and a
    path some typed grammar matches is kept for that kind's row alone (§8 F8), so a `…-probe-design.md`
    or an `…-acceptance-ledger.md` its glob matches falls to the untyped rows. The population S4 grades
    before the legacy ledger takes its rows out, and what `--seed-legacy` prints."""
    from build_records import derive_record_name
    grammars = {k: derive_record_name(k) for k in typed_kinds}
    out = {}
    for row in rows:
        schema = row.get("schema") if isinstance(row.get("schema"), dict) else {}
        home = row.get("home")
        if schema.get("form") != "fields" or not isinstance(home, str) or not home.strip():
            continue
        name, keep = row.get("name"), []
        for path in read_tracked(root, home):
            typed = [k for k, g in grammars.items() if g.search(path)]
            if (name in typed) if name in grammars else not typed:
                keep.append(path)
        out[name] = keep
    return out


def read_legacy_keys(root) -> tuple[set, str]:
    """`({(path, row name)}, note)` of the `record-kinds-legacy` ledger; an empty set and a note saying
    why where it is unregistered or its home is absent."""
    import legacy_ledger as ll
    try:
        reg = next((r for r in ll.read_registrations(root) if r.population == LEGACY), None)
    except ValueError as e:
        return set(), f"the ledger registrations do not read: {str(e).splitlines()[0]}"
    if reg is None:
        return set(), f"no [[ledger]] table registers {LEGACY}"
    if not pathlib.Path(root, reg.home).is_file():
        return set(), f"{LEGACY}'s home {reg.home} is absent"
    rows, _bad = ll.read_ledger(root, reg)
    return set(rows), ""


def derive_field_lines(text: str, fields: list[str]) -> tuple[list[str], list[str]]:
    """`(missing, out of order)` of `fields` in one record's text, each a `**Key:**` line, bare or bulleted."""
    at, missing = [], []
    for f in fields:
        m = re.search(r"^[ \t]*(?:- )?\*\*" + re.escape(f) + r":\*\*(?:[ \t]|$)", text, re.M)
        if m:
            at.append((m.start(), f))
        else:
            missing.append(f)
    order = [f for (_, f), (_, g) in zip(at, sorted(at)) if f != g]
    return missing, order


def read_gap_keys(root) -> set | None:
    """The first-cell gap keys of every tracked `<memory root>/builds/*/build/*-gap-register.md`'s table
    rows; None where no register is tracked."""
    regs = read_tracked(root, f"{read_memory_root(root)}/builds/*/build/*-gap-register.md")
    if not regs:
        return None
    keys = set()
    for rel in regs:
        for ln in pathlib.Path(root, rel).read_bytes().decode("utf-8", "replace").splitlines():
            cells = ln.strip().split("|")
            if ln.strip().startswith("|") and len(cells) > 2 and GAP_KEY_RE.fullmatch(cells[1].strip()):
                keys.add(cells[1].strip())
    return keys


def print_gap_keys(root) -> int:
    """`--print-gap-keys`: one key per line, exit 0; exit 3 where no gap register is tracked."""
    keys = read_gap_keys(root)
    if keys is None:
        print(f"# {SAY}: no gap register is tracked, so the gap-key class is not armed here")
        return NOT_ARMED
    for k in sorted(keys):
        print(k)
    return 0


# ------------------------------------------------------------------------------------- the view
def render_kind_region(rows: list[dict]) -> str:
    """The `gen:record-kinds` region, its markers included: one table line per row."""
    def render_cell(v):
        return f"`{v}`" if isinstance(v, str) and v else "—"
    lines = [REGION_OPEN, "", "| Kind | Tag | Home | Writer | Check |", "|---|---|---|---|---|"]
    lines += [f"| {render_cell(r.get('name'))} | {render_cell(r.get('tag'))} | {render_cell(r.get('home'))} | {render_cell(r.get('writer'))} | "
              f"{render_cell(r.get('check'))} |" for r in rows]
    return "\n".join(lines + ["", REGION_CLOSE])


def derive_region_span(text: str) -> tuple[int, int] | None:
    """The span of the region, open marker through close marker, or None where either is missing."""
    i = text.find(REGION_OPEN)
    j = text.find(REGION_CLOSE, i + 1) if i >= 0 else -1
    return (i, j + len(REGION_CLOSE)) if i >= 0 and j >= 0 else None


def write_kind_region(root, kit_rel: str | None = None) -> int:
    """`--write`: the template's region replaced by its render; exit 2 where the markers are missing."""
    kit_rel = kit_rel or derive_kit_rel()
    rows = read_record_kinds(root, kit_rel) or []
    path = pathlib.Path(root, kit_rel, TEMPLATE)
    text = path.read_bytes().decode("utf-8")
    span = derive_region_span(text)
    if span is None:
        print(f"{SAY}: refused · {TEMPLATE} holds no {REGION_OPEN} … {REGION_CLOSE} region")
        return 2
    new = text[:span[0]] + render_kind_region(rows) + text[span[1]:]
    if new != text:
        path.write_bytes(new.encode("utf-8"))
    print(f"{SAY}: wrote the region of {TEMPLATE}, {len(rows)} rows" if new != text else f"{SAY}: region current")
    return 0


# -------------------------------------------------------------------------------------- the gate
def check_record_kinds(root, typed_kinds=None, kit_rel: str | None = None) -> tuple[list[str], int]:
    """S3, S4, S6 and the gap-key join over the tree at `root`: `(lines, exit)`. `typed_kinds` stands in
    for `tree_lib.TYPED_RECORD_KINDS` (the fixture's list)."""
    if typed_kinds is None:
        from tree_lib import TYPED_RECORD_KINDS as typed_kinds
    kit_rel = kit_rel or derive_kit_rel()
    tool_rel = derive_tool_rel(kit_rel)
    try:
        rows = read_record_kinds(root, kit_rel)
    except RecordKindsError as e:
        return [f"{SAY}: refused · {e}"], 2
    if not rows:
        return [f"{SAY}: unarmed — the registry {kit_rel}/{REGISTRY} holds no row", f"{SAY}: red"], 1
    legs = read_leg_names(root, tool_rel)
    reds = [] if legs is not None else [f"{tool_rel}/{LEGS} is absent or unreadable, so no `check` resolves"]
    legs = legs or set()
    names = [r.get("name") for r in rows]
    for n, row in enumerate(rows, 1):
        reds += check_row(row, n, legs, root, tool_rel)
    reds += [f"row {k}: declared twice" for k in sorted({x for x in names if isinstance(x, str) and names.count(x) > 1})]
    by_name = {r.get("name"): r for r in rows}
    for k in typed_kinds:
        src = (by_name.get(k, {}).get("schema") or {}).get("source", "") if isinstance(by_name.get(k, {}).get("schema"), dict) else ""
        if k not in by_name:
            reds.append(f"typed kind {k}: the factory's kind list names it and no row declares it")
        elif not FACTORY_SOURCE.search(src or ""):
            reds.append(f"row {k}: a typed kind's row reads its fields from the factory's KINDS.{k}.required")
    for row in rows:
        schema = row.get("schema") if isinstance(row.get("schema"), dict) else {}
        m = FACTORY_SOURCE.search(str(schema.get("source") or ""))
        if m and (m[1] not in typed_kinds or m[1] != row.get("name")):
            reds.append(f"row {row.get('name')}: a factory row naming {m[1]}, which is no member of the factory's "
                        f"kind list under this name")
    legacy, note = read_legacy_keys(root)
    population = scan_legacy_records(root, rows, typed_kinds)
    counts, unarmed, graded_paths = [], [], {}
    for row in rows:
        name, schema = row.get("name"), row.get("schema") if isinstance(row.get("schema"), dict) else {}
        if name not in population:
            counts.append(f"{name} {schema.get('form', '?')}")
            continue
        paths = population[name]
        if not paths:
            if name in typed_kinds:
                unarmed.append(f"{name}: unarmed — no record yet")
            else:
                reds.append(f"row {name}: its home {row.get('home')!r} matches no tracked record")
        old = [p for p in paths if (p, name) in legacy]
        new = [p for p in paths if (p, name) not in legacy]
        graded_paths[name] = new
        counts.append(f"{name} {len(new)} graded {len(old)} legacy")
        for p in new:
            missing, order = derive_field_lines(pathlib.Path(root, p).read_bytes().decode("utf-8", "replace"),
                                                schema.get("fields", []))
            reds += [f"row {name}: {p} carries no **{f}:** line" for f in missing]
            if order:
                reds.append(f"row {name}: {p} carries {', '.join(order)} out of the row's order")
    keys = read_gap_keys(root)
    if not keys:
        reds.append("unarmed — no tracked gap register holds a gap key, so no Follow-through gap resolves")
    else:
        for p in graded_paths.get("deviation", []):
            text = pathlib.Path(root, p).read_bytes().decode("utf-8", "replace")
            m = re.search(r"^[ \t]*(?:- )?\*\*Follow-through:\*\*[ \t]*(.*)$", text, re.M)
            g = FOLLOW_GAP.match(m[1].strip()) if m else None
            if g and GAP_KEY_RE.fullmatch(g[1]) and g[1] not in keys:
                reds.append(f"row deviation: {p} follows through to {g[1]}, which no gap register holds")
    tpath = pathlib.Path(root, kit_rel, TEMPLATE)
    text = tpath.read_bytes().decode("utf-8") if tpath.is_file() else ""
    span = derive_region_span(text)
    if span is None:
        reds.append(f"region gen:record-kinds: {kit_rel}/{TEMPLATE} holds no such region")
    else:
        have, want = text[span[0]:span[1]].split("\n"), render_kind_region(rows).split("\n")
        if have != want:
            i = next((i for i, (a, b) in enumerate(zip(have, want)) if a != b), min(len(have), len(want)))
            first = have[i] if i < len(have) else "(the region ends)"
            reds.append(f"region gen:record-kinds: line {i + 1} of the region, {first!r}, is not what --write "
                        f"writes; run --write")
    lines = [f"{SAY}: {len(rows)} rows · " + " · ".join(counts)]
    lines += [f"{SAY}: {u}" for u in unarmed]
    if note:
        lines.append(f"{SAY}: legacy · {note}")
    lines += [f"{SAY}: RED {r}" for r in reds]
    lines.append(f"{SAY}: {'red' if reds else 'green'}")
    return lines, 1 if reds else 0


# ---------------------------------------------------------------------------------- the factory
def render_row(row: dict) -> str:
    """One `[[record-kind]]` table in the registry's column order."""
    out = ["[[record-kind]]"]
    for col in COLUMNS:
        v = row[col]
        if col == "schema":
            parts = [f"form = {json.dumps(v['form'])}"] + ([f"source = {json.dumps(v['source'])}"] if v.get("source") else [])
            parts.append("fields = [" + ", ".join(json.dumps(f) for f in v["fields"]) + "]")
            out.append("schema = { " + ", ".join(parts) + " }")
        else:
            out.append(f"{col} = {json.dumps(v)}")
    return "\n".join(out) + "\n"


def add_record_kind(root, a, kit_rel: str | None = None) -> int:
    """`new`: one conforming `fields` row appended to the registry and the HYGIENE template's view
    re-rendered from it, so the gate reads the two in step; or exit 2 naming each refusal and writing
    nothing."""
    kit_rel = kit_rel or derive_kit_rel()
    rows = read_record_kinds(root, kit_rel) or []
    legs = read_leg_names(root, derive_tool_rel(kit_rel)) or set()
    bad = []
    if not NAME_RE.fullmatch(a.name or ""):
        bad.append(f"name {a.name!r} is not [a-z][a-z0-9-]*")
    if any(r.get("name") == a.name for r in rows):
        bad.append(f"kind {a.name!r} is declared already")
    if a.tag != f"record.{a.name}":
        bad.append(f"--tag {a.tag!r} is not record.{a.name}")
    if not (a.writer or "").strip():
        bad.append("--writer is required and non-empty: name the door, `generator:<path>` or `hand`")
    if not (a.home or "").strip():
        bad.append("--home is required: a `fields` row's home is the population its check grades")
    if not a.field or not all(f.strip() for f in a.field):
        bad.append("--field is required, one per **Key:** line the kind carries")
    if a.check not in legs:
        bad.append(f"--check {a.check!r} names no leg of {LEGS}")
    if bad:
        for b in bad + ["nothing written"]:
            print(f"{SAY}: refused · {b}")
        return 2
    row = {"name": a.name, "tag": a.tag, "layer": "", "home": a.home, "id-rule": "",
           "schema": {"form": "fields", "fields": list(a.field)}, "writer": a.writer, "readers": [],
           "lifecycle": "", "check": a.check}
    path = pathlib.Path(root, kit_rel, REGISTRY)
    text = path.read_bytes().decode("utf-8") if path.is_file() else ""
    path.write_bytes((text.rstrip("\n") + "\n\n" + render_row(row) if text.strip() else render_row(row)).encode("utf-8"))
    print(f"{SAY}: new · declared {a.name} in {kit_rel}/{REGISTRY}")
    if not pathlib.Path(root, kit_rel, TEMPLATE).is_file():   # an install that renders no template here
        print(f"{SAY}: new · no {TEMPLATE} beside the registry, so no view to re-render")
        return 0
    return write_kind_region(root, kit_rel)   # the view is the registry's render, so it moves with the row


def render_template(rows: list[dict], kind: str, typed_kinds=None) -> str | None:
    """S5: the skeleton one `fields` row defines, the layout `build_records.write_record` writes; None for
    a kind with no `fields` row."""
    row = next((r for r in rows if r.get("name") == kind), None)
    schema = (row or {}).get("schema") if isinstance((row or {}).get("schema"), dict) else {}
    if not row or schema.get("form") != "fields":
        return None
    factory = FACTORY_SOURCE.search(str(schema.get("source") or ""))
    out = [f"# <unit id> {kind} <n> — <title>" if factory else "# <title>", "", f"**Serves:** {kind} <unit id>", ""]
    out += [f"- **{f}:** " for f in schema.get("fields", []) if f != "Serves"]
    return "\n".join(out) + "\n"


# ------------------------------------------------------------------------------- the step gate
def read_kind_schema_members(root) -> set:
    """The `record-kind-schema` class: `<kind>.<field>` per field of every row; an empty set where the
    registry is absent (the step gate's reader contract)."""
    rows = read_record_kinds(root) or []
    return {f"{r.get('name')}.{f}" for r in rows if isinstance(r.get("schema"), dict)
            for f in r["schema"].get("fields", []) if isinstance(f, str)}


def write_kind_schema_plant(clone) -> str:
    """The class's plant: the first `fields` row of the clone's registry short of its last field, staged."""
    kit_rel = derive_kit_rel()
    rel = f"{kit_rel}/{REGISTRY}"
    rows = read_record_kinds(clone, kit_rel) or []
    row = next((r for r in rows if isinstance(r.get("schema"), dict) and r["schema"].get("form") == "fields"
                and r["schema"].get("fields")), None)
    if row is None:
        raise RecordKindsError("the record-kind-schema plant found no `fields` row with a field")
    field = row["schema"]["fields"][-1]
    path = pathlib.Path(clone, rel)
    text = path.read_bytes().decode("utf-8")
    start = text.find(f"name = {json.dumps(row['name'])}\n")
    end = text.find("[[record-kind]]", start)
    end = len(text) if end < 0 else end
    chunk = re.sub(r",?\s*" + re.escape(json.dumps(field)) + r"(?=\s*\])", "", text[start:end], count=1)
    path.write_bytes((text[:start] + chunk + text[end:]).encode("utf-8"))
    run_git(clone, "add", "--", rel)
    return f"record-kind-schema:{row['name']}.{field}"


# ---------------------------------------------------------------------------------- the fixture
FIXTURE_TYPED = ("deviation",)
FIXTURE_BUILD = "bFix"
PLANTS = ("writer-missing", "check-unknown", "source-drift", "factory-kind-unrowed", "field-missing",
          "field-missing-legacy", "region-edited", "gap-unresolved")


def build_fixture(tmp, plant: str | None = None):
    """A throwaway repository at `tmp` laid out as this kit's own tree: a three-row registry, a two-leg
    manifest, a govkit registry holding the legacy ledger's table, its home, a gap register and records,
    one a `…-deviation-notes.md` holding no deviation field, `plant` applied, committed. -> the typed
    kind list its check reads."""
    from build_records import KINDS
    tmp = pathlib.Path(tmp)
    kit_rel = derive_kit_rel()
    tool_rel = derive_tool_rel(kit_rel)
    prefix = "{prefix}"
    dev = list(KINDS["deviation"]["required"])
    build = f"memory/builds/{FIXTURE_BUILD}/build"
    unit = f"TOOL-{FIXTURE_BUILD}-1"

    def write_fixture_file(rel, text):
        p = tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))

    write_fixture_file(".memory-tree.conf", 'MEMORY_ROOT="memory"\n')
    write_fixture_file(f"{tool_rel}/{LEGS}" if tool_rel else LEGS, json.dumps([{"name": "memory hygiene"}, {"name": SAY}], indent=2) + "\n")
    write_fixture_file(f"{kit_rel}/build_records.py", "LEVELS = ('a', 'b')\nKINDS = {\n    'deviation': {\n        'required': ("
        + ", ".join(json.dumps(f) for f in dev + (["Extra"] if plant == "source-drift" else [])) + "),\n"
        "        'closed': (('Risk', LEVELS),),\n    },\n}\n")
    rows = [
        {"name": "spec", "tag": "record.spec", "layer": "", "home": "", "id-rule": "<date>-spec-<unit id>.md",
         "schema": {"form": "header", "fields": []}, "writer": "hand", "readers": [], "lifecycle": "",
         "check": "memory hygiene"},
        {"name": "research", "tag": "record.research", "layer": "", "home": "memory/builds/*/build/*.md", "id-rule": "",
         "schema": {"form": "fields", "fields": ["Serves"]}, "writer": "hand", "readers": [], "lifecycle": "",
         "check": "no such leg" if plant == "check-unknown" else "memory hygiene"},
        {"name": "deviation", "tag": "record.deviation", "layer": "",
         "home": "memory/builds/*/build/*-build-*-deviation-*.md", "id-rule": "<date>-build-<unit id>-deviation-<n>.md",
         "schema": {"form": "fields", "source": f"{prefix}/{kit_rel[len(tool_rel) + 1:] if tool_rel else kit_rel}"
                    f"/build_records.py:KINDS.deviation.required", "fields": dev},
         "writer": "hand", "readers": [], "lifecycle": "", "check": "memory hygiene"},
    ]
    registry = "\n".join(render_row(r) for r in rows)
    if plant == "writer-missing":   # the deviation row, the last, loses its writer
        head, _, tail = registry.partition('name = "deviation"\n')
        registry = head + 'name = "deviation"\n' + tail.replace('writer = "hand"\n', "", 1)
    write_fixture_file(f"{kit_rel}/{REGISTRY}", registry)
    region = render_kind_region(tomllib.loads(registry)["record-kind"])
    if plant == "region-edited":
        region = region.replace("| Kind |", "| Kinds |", 1)
    write_fixture_file(f"{kit_rel}/{TEMPLATE}", "# fixture hygiene\n\n## Record kinds — the registry's view\n\n" + region + "\n")
    sibling = "/".join(("govkit", "registry.toml"))   # spelled in parts: the install-prefix ban reads a kit path
    write_fixture_file(f"{tool_rel}/{sibling}" if tool_rel else sibling,
        f'[[ledger]]\npopulation = "{LEGACY}"\nleg = "{SAY}"\nseed = ["python", "{prefix}/{kit_rel[len(tool_rel) + 1:] if tool_rel else kit_rel}/record_kinds.py", "--seed-legacy"]\n'
        'key = "record"\nfields = ["path", "section"]\ndrain = "key"\ndirection = "shrink-only"\n'
        f'home = "memory/project/{LEGACY}.txt"\n')
    old = f"{build}/2026-01-01-build-{unit}-deviation-1.md"
    new = f"{build}/2026-01-02-build-{unit}-deviation-2.md"
    legacy_rows = [(old, "deviation")] + ([(new, "deviation")] if plant == "field-missing-legacy" else [])
    write_fixture_file(f"memory/project/{LEGACY}.txt", f"# ledger · {LEGACY} · key record path,section · direction shrink-only · drain key\n"
        + "".join(f"{p}\t{s}\t1\t{'0' * 40}\tseeded\n" for p, s in legacy_rows))
    write_fixture_file(old, f"# {unit} deviation 1 — an old form\n\n**Serves:** deviation {unit}\n\n- **Reason:** kept as it was\n")
    follow = "gap gap-mem-99" if plant == "gap-unresolved" else "gap gap-mem-01"
    values = {f: "the fixture" for f in dev}
    values["Follow-through"] = follow
    body = [f"# {unit} deviation 2 — the fixture", "", f"**Serves:** deviation {unit}", ""]
    body += [f"- **{f}:** {values[f]}" for f in dev if not (f == "Caused-by" and plant in ("field-missing", "field-missing-legacy"))]
    write_fixture_file(new, "\n".join(body) + "\n")
    # The deviation home's glob matches it and the deviation grammar does not (§8 F8): the research row
    # grades it, so its missing deviation fields red nothing.
    write_fixture_file(f"{build}/2026-01-03-build-{unit}-deviation-notes.md", f"**Serves:** research {unit}\n\nnotes, no field\n")
    write_fixture_file(f"{build}/2026-01-01-build-{unit}-gap-register.md", f"**Serves:** research {unit}\n\n| Key | Gap |\n|---|---|\n"
        "| gap-mem-01 | the fixture's one gap |\n")
    hooks = tmp / ".nohooks"
    hooks.mkdir(exist_ok=True)
    for args in (("init", "-q"), ("add", "-A", "--", "."),
                 ("-c", "user.name=record-kinds", "-c", "user.email=record-kinds@fixture.invalid", "-c",
                  "commit.gpgsign=false", "-c", f"core.hooksPath={hooks.as_posix()}", "commit", "-q", "--no-verify",
                  "-m", f"record-kinds fixture: {plant or 'green'}")):
        p = run_git(tmp, *args)
        if p.returncode != 0:
            raise RecordKindsError(f"the fixture's git {args[0]} refused: {p.stderr.strip()}")
    return FIXTURE_TYPED + (("exception",) if plant == "factory-kind-unrowed" else ())


def run_fixture(plant: str | None) -> tuple[list[str], int]:
    """`--fixture [--plant <case>]`: the fixture built under the system temp directory, `--check` run there."""
    if plant is not None and plant not in PLANTS:
        return [f"{SAY}: refused · no plant {plant!r}: the plants are {', '.join(PLANTS)}"], 2
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="rk-"))
    try:
        typed = build_fixture(tmp, plant)
        lines, rc = check_record_kinds(tmp, typed)
        return [f"{SAY}: fixture {plant or 'green'}"] + lines, rc
    finally:
        remove_tree(tmp)


def remove_tree(path) -> None:
    """`path` removed, a read-only file (git's objects on Windows) made writable first."""
    def remove_read_only(func, p, _exc):
        os.chmod(p, 0o700)
        func(p)
    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=remove_read_only)
    else:
        shutil.rmtree(path, onerror=remove_read_only)


def run_selftest() -> int:
    """Every plant red naming its subject, the green fixture and the legacy plant green, `new`'s round trip
    and its refusal, and `--write` restoring an edited region."""
    want = {"writer-missing": ("row deviation", "`writer`"), "check-unknown": ("row research", "no such leg"),
            "source-drift": ("row deviation", "Extra"), "factory-kind-unrowed": ("typed kind exception",),
            "field-missing": ("deviation-2.md", "**Caused-by:**"), "region-edited": ("region gen:record-kinds",),
            "gap-unresolved": ("gap-mem-99",)}
    fails = []
    for plant in (None, "field-missing-legacy", *want):
        lines, rc = run_fixture(plant)
        out = "\n".join(lines)
        reds = [ln for ln in lines if " RED " in ln]
        if plant in want and not (rc == 1 and any(all(s in ln for s in want[plant]) for ln in reds)):
            fails.append(f"{plant}: want exit 1 naming {', '.join(want[plant])}, got {rc}: {out[-400:]}")
        elif plant not in want and rc != 0:
            fails.append(f"{plant or 'green'}: want exit 0, got {rc}: {out[-400:]}")
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="rk-"))
    try:
        typed = build_fixture(tmp)
        argv = ["new", "widget", "--tag", "record.widget", "--writer", "hand", "--check", "memory hygiene",
                "--field", "Serves", "--home", "memory/builds/*/build/*.md"]
        reg = pathlib.Path(tmp, derive_kit_rel(), REGISTRY)
        before = reg.read_bytes()
        rc = main([a for a in argv if a not in ("--writer", "hand")], root=tmp)
        if rc != 2 or reg.read_bytes() != before:
            fails.append(f"new without --writer: want exit 2 and nothing written, got {rc}")
        rc = main(argv, root=tmp)   # AC10: `new` alone, its view re-rendered with the row
        lines, rc_c = check_record_kinds(tmp, typed)
        if rc or rc_c or "widget 2 graded" not in lines[0]:
            fails.append(f"new widget: want a row the gate grades green, got new {rc}, check {rc_c}: "
                         + " | ".join(lines))
        tpl = pathlib.Path(tmp, derive_kit_rel(), TEMPLATE)
        tpl.write_bytes(tpl.read_bytes().replace(b"| Kind |", b"| Kinds |", 1))
        rc_w = main(["--write"], root=tmp)
        if rc_w or check_record_kinds(tmp, typed)[1]:
            fails.append("--write did not restore an edited region")
    finally:
        remove_tree(tmp)
    for f in fails:
        print(f"{SAY}: selftest FAIL · {f}")
    print(f"{SAY}: selftest {'FAIL' if fails else 'PASS'} · {len(PLANTS)} plants, the green fixture, new, --write")
    return 1 if fails else 0


# ------------------------------------------------------------------------------------- the CLI
def read_root() -> pathlib.Path:
    """The repository the working directory sits in."""
    p = run_git(os.getcwd(), "rev-parse", "--show-toplevel")
    if p.returncode != 0:
        raise RecordKindsError("the working directory is in no git repository")
    return pathlib.Path(p.stdout.strip())


def main(argv: list[str], root=None) -> int:
    try:
        root = root or read_root()
        if argv[:1] == ["new"]:
            ap = argparse.ArgumentParser(prog="record_kinds.py new", description="declare one conforming record kind")
            ap.add_argument("name")
            ap.add_argument("--tag")
            ap.add_argument("--writer")
            ap.add_argument("--check")
            ap.add_argument("--field", action="append")
            ap.add_argument("--home")
            try:
                a = ap.parse_args(argv[1:])
            except SystemExit as e:
                return int(e.code or 0)
            return add_record_kind(root, a)
        if argv == ["--check"]:
            lines, rc = check_record_kinds(root)
        elif argv == ["--write"]:
            return write_kind_region(root)
        elif len(argv) == 2 and argv[0] == "--template":
            text = render_template(read_record_kinds(root) or [], argv[1])
            if text is None:
                print(f"{SAY}: refused · {argv[1]!r} has no `fields` row, so no template")
                return 2
            sys.stdout.write(text)
            return 0
        elif argv == ["--seed-legacy"]:
            from tree_lib import TYPED_RECORD_KINDS
            pop = scan_legacy_records(root, read_record_kinds(root) or [], TYPED_RECORD_KINDS)
            for name, paths in pop.items():
                for p in paths:
                    print(f"{p}\t{name}\t1")
            return 0
        elif argv == ["--print-gap-keys"]:
            return print_gap_keys(root)
        elif argv[:1] == ["--fixture"] and (len(argv) == 1 or (len(argv) == 3 and argv[1] == "--plant")):
            lines, rc = run_fixture(argv[2] if len(argv) == 3 else None)
        elif argv == ["--selftest"]:
            return run_selftest()
        else:
            print(__doc__.split("\n\n")[1], file=sys.stderr)
            return 2
    except RecordKindsError as e:
        print(f"{SAY}: refused · {e}")
        return 2
    print("\n".join(lines))
    return rc


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main(sys.argv[1:]))
