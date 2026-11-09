"""writing_practice — the writing practice's checks over records as well as units (PLAY-dOrderedCharter-29).

    python writing_practice.py check [one-subject|pinned-facts|one-door|rationale-apart|one-owner] [--explain]
    python writing_practice.py check pinned-facts --seed | --shrink
    python writing_practice.py --fixture --plant <case>

`practice.writing` in practices.toml names eight rules; this module checks five, the rest are the resolver's and
the edge leg's. Every arm reads three populations once: the UNITS, every row `instruction_units.read_unit_rows`
reads and the overlay's, the overlay's origin the repository; the RECORDS, every tracked `*.md` under the memory
root, its generated regions (`<!-- gen:` to `<!-- /gen:`) left out, each split into sections at its `##` headings,
a heading's slug the `doc` namespace's fold `tag_index.derive_heading_seg`; and the DOCUMENTS, the tracked files of
the document registry `instruction_units.read_document_registry` reads. Each arm prints
`<arm>: <n> units · <m> records · <k> documents`, refuses a zero records or documents population (exit 2), and
prints `units unarmed` while the tree holds no unit row, grading the populations it did read.

A record under `<MEMORY_ROOT>/builds/` is frozen: `one-subject` and `one-door` print a finding there as `frozen`
and never red it; `pinned-facts` holds today's in the keyed list and reds a new one wherever it sits.

`one-subject`: a unit tag on two rows, or a heading slug twice in one record or one document, is red.
`pinned-facts`: a line quoting a number before a word of FACT_UNITS carries a pin on that line. Today's unpinned
facts are the keyed list `unpinned-facts.txt` under `<MEMORY_ROOT>/project/`, `<path>\\t<fact>`; a new fact is red,
a listed one gone from the tree red as stale until `--shrink` takes it off; `--seed` writes the list once.
`one-door`: `doors.toml`, one `[[door]]` row per kind of DOOR_KINDS, each writer a tracked file and each node of a
kind with a witness carrying it. `rationale-apart`: a unit's `help` inside a registered document, and a build
record's path in the registry or a unit's text or source, are red. `one-owner`: every namespace, kind and kit unit
row names exactly one owner, a build `memory/builds/` holds or a layer `layers.toml` names; a repository unit
names none. `check` with no arm runs the first four, the `writing practice (records and units)` leg; `check
one-owner` is the `one-owner` leg. Exit 0 green, 1 red, 2 a refusal.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import re
import shutil
import stat
import sys
import tempfile
import tomllib

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
sys.path.insert(0, str(KIT_DIR))

import instruction_units as iu  # noqa: E402
import positional  # noqa: E402
import tag_index as ti  # noqa: E402

LEG_ARMS = ("one-subject", "pinned-facts", "one-door", "rationale-apart")
ARMS = (*LEG_ARMS, "one-owner")
FACTS_NAME = "unpinned-facts.txt"
DOORS = "doors.toml"
#: the closed set of words a quoted derived fact's number is followed by
FACT_UNITS = ("bytes", "B", "KB", "KiB", "MB", "lines", "files", "legs", "units", "rows", "specs", "records",
              "commits", "citations", "tokens", "calls", "seconds", "s")
FACT_RE = re.compile(r"(?<![\w.#@/-])(\d[\d,]*) ?(" + "|".join(FACT_UNITS) + r")\b")
PIN_RE = re.compile(r"\b[0-9a-f]{8,40}\b|[A-Za-z0-9_./-]+\.[A-Za-z0-9]+(?:@[0-9a-f]{8,40})?:\d+|\b(?:PINNED|DERIVED)\b")
CODE_SPAN_RE = re.compile(r"(`+).+?\1")
#: the memory plan's edge-site door kinds, each one `[[door]]` row of doors.toml until dTotalRecall's kind registry
DOOR_KINDS = ("instruction-unit", "instruction-change", "work-order", "override", "exception", "record", "trailer",
              "act")
FIRST_UNIT_WRITER = "PLAY-dOrderedCharter-40"
EXPLAIN = {
    "one-subject": ("a unit tag on two unit rows; a `##` heading slug twice in one record or one registered "
                    "document, the slug the doc namespace's fold",
                    "a `#`, `###` or deeper heading; a heading inside a fence or a generated region; one subject "
                    "split across two records; one subject under two differently worded headings"),
    "pinned-facts": ("a number of one or more digits, commas allowed, followed within one space by a word of "
                     f"FACT_UNITS ({', '.join(FACT_UNITS)}), outside fences and inline code, in a record line or a "
                     "unit's text; a pin on the same line: a hex id of 8 to 40 characters, a `path:<n>` or "
                     "`path@<oid>:<n>` citation, or PINNED or DERIVED",
                     "a fact spelled in words (\"eight legs\"), a percentage, a number inside code or a fence, a "
                     "pin on a neighbouring line, whether a pin is true, and a number that is no derived fact"),
    "one-door": ("each kind of DOOR_KINDS has one `[[door]]` row; a row's writer is a tracked file; each node its "
                 "population matches carries its witness, where the row declares one",
                 "whether the writer wrote a node (only its witness is read); a kind whose row declares no witness "
                 "(unobserved); a `pending` row's kind (named, never graded)"),
    "rationale-apart": ("a unit's `help` text inside a registered document's tracked file; a build record's path "
                        "in a document registry row or in a unit's text or source",
                        "a paraphrase of a help text; an untracked registry row's file; a record path reached "
                        "through a pointer the document follows"),
    "one-owner": ("every namespace, kind and kit unit row names exactly one owner, a build memory/builds/ holds or "
                  "a layer of layers.toml; a repository unit names none",
                  "whether the owner is the right one; registry rows outside namespaces.toml, kinds.toml and the "
                  "unit manifests"),
}


class Refused(Exception):
    """A population or a list the arm cannot read: exit 2."""


# ------------------------------------------------------------------------------------------ the populations

def read_records(root, memory_root) -> list:
    """(path, [(line number, line)]) of every tracked `*.md` under the memory root, outside fences and
    generated regions, sorted by path."""
    tree_lib, _ = ti.load_memory_tree()
    paths = sorted(p for p in iu.run_git(root, "ls-files", "-z", "--", f"{memory_root}/*.md").split("\0") if p)
    out = []
    for rel in paths:
        try:
            text = (pathlib.Path(root) / rel).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        out.append((rel, derive_text_lines(tree_lib, text)))
    return out


def derive_text_lines(tree_lib, text) -> list:
    lines, gen = [], False
    for n, line in tree_lib.unfenced_lines("\n".join(text.splitlines())):
        if line is None:
            continue
        if line.lstrip().startswith("<!-- gen:"):
            gen = True
        elif line.lstrip().startswith("<!-- /gen:"):
            gen = False
        elif not gen:
            lines.append((n, line))
    return lines


def read_populations(root) -> dict:
    """The three populations and the tree's memory root, read once."""
    root = pathlib.Path(root)
    memory_root = positional.read_memory_root(root)
    units, _faults = iu.read_unit_rows(root)  # a row the reader cannot read is the schema leg's red
    overlay = root / iu.OVERLAY
    if overlay.is_file():
        units += iu.parse_unit_rows(overlay.read_text(encoding="utf-8"), iu.OVERLAY, "repository")[0]
    try:
        registry = iu.read_document_registry(root)
    except iu.DocumentRefused:
        registry = []
    tree_lib, _ = ti.load_memory_tree()
    documents = []
    for row in registry:
        if row["untracked"]:
            continue
        for rel in iu.derive_tracked(root, row["resolved"]):
            text = (root / rel).read_text(encoding="utf-8", errors="replace")
            documents.append((rel, text, derive_text_lines(tree_lib, text)))
    return {"root": root, "memory_root": memory_root, "units": units, "records": read_records(root, memory_root),
            "documents": documents, "registry": registry}


def check_frozen(pop, path) -> bool:
    return path.startswith(pop["memory_root"] + "/builds/")


def derive_counts(arm, pop) -> list:
    lines = [f"{arm}: {len(pop['units'])} units · {len(pop['records'])} records · {len(pop['documents'])} documents"]
    if not pop["records"]:
        raise Refused(f"{arm}: refused · the records population is empty: no tracked *.md under "
                      f"{pop['memory_root']}/, and an empty population is no coverage")
    if not pop["documents"]:
        raise Refused(f"{arm}: refused · the documents population is empty: the document registry names no "
                      "tracked file, and an empty population is no coverage")
    if not pop["units"]:
        lines.append(f"{arm}: units unarmed · the tree holds no unit row ({FIRST_UNIT_WRITER} writes the first)")
    return lines


def write_finding(arm, pop, path, text, reds, lines) -> None:
    """A finding on `path`: printed as frozen under the builds folder, red elsewhere."""
    if check_frozen(pop, path):
        lines.append(f"{arm}: frozen · {text}")
    else:
        reds.append(f"{arm}: red · {text}")


# ------------------------------------------------------------------------------------------ the arms

def derive_sections(lines) -> dict:
    """{slug: [line numbers]} of the `##` headings of one file's lines."""
    out = {}
    for n, line in lines:
        if line.startswith("## "):
            seg = ti.derive_heading_seg(line[3:].strip())
            if seg:
                out.setdefault(seg, []).append(n)
    return out


def check_one_subject(pop, opts) -> tuple:
    reds, lines, seen = [], [], {}
    for u in pop["units"]:
        if u.tag:
            seen.setdefault(u.tag, []).append(f"{u.path}:{u.line}")
    for tag, where in sorted(seen.items()):
        if len(where) > 1:
            reds.append(f"one-subject: red · unit tag {tag} on two rows: {' and '.join(where)}")
    records = {p for p, _ in pop["records"]}
    files = pop["records"] + [(p, ls) for p, _t, ls in pop["documents"] if p not in records]
    for path, ls in files:
        for seg, ns in sorted(derive_sections(ls).items()):
            if len(ns) > 1:
                write_finding("one-subject", pop, path, f"{path} · heading #{seg} twice: "
                       + " and ".join(f"{path}:{n}" for n in ns), reds, lines)
    return reds, lines


def derive_facts(line) -> list:
    """The unpinned facts of one line, inline code cut: [] where a pin sits on the line."""
    text = CODE_SPAN_RE.sub(" ", line)
    facts = [m.group(0) for m in FACT_RE.finditer(text)]
    if facts and PIN_RE.search(FACT_RE.sub(" ", text)):
        return []
    return facts


def read_fact_rows(pop) -> set:
    rows = set()
    for path, ls in pop["records"]:
        for _n, line in ls:
            rows.update(f"{path}\t{f}" for f in derive_facts(line))
    for u in pop["units"]:
        for line in (u.text or "").splitlines():
            rows.update(f"{u.path}\t{f}" for f in derive_facts(line))
    return rows


def derive_facts_path(pop) -> pathlib.Path:
    return positional.derive_list_path(pop["root"], pop["memory_root"], FACTS_NAME)


def check_pinned_facts(pop, opts) -> tuple:
    path = derive_facts_path(pop)
    listed = positional.read_list(path)
    tree = read_fact_rows(pop)
    if opts.seed:
        if listed:
            raise Refused(f"pinned-facts: refused · --seed · {path.name} already holds {len(listed)} rows: the seed "
                          "runs once, and --shrink takes rows out")
        positional.write_list(path, tree)
        return [], [f"pinned-facts: seeded {path.name} with {len(tree)} rows"]
    if listed is None:
        raise Refused(f"pinned-facts: refused · {pop['memory_root']}/project/{FACTS_NAME} is absent: run `writing_practice.py check "
                      "pinned-facts --seed` once to list today's unpinned facts")
    listed = set(listed)
    if opts.shrink:
        keep = listed & tree
        positional.write_list(path, keep)
        return [], [f"pinned-facts: shrink dropped {len(listed - keep)} stale rows, {len(keep)} remain"]
    reds, lines = [], []
    for row in sorted(tree - listed):
        p, _, fact = row.partition("\t")
        reds.append(f"pinned-facts: red · {p} · unpinned fact `{fact}`: pin it on its line (an id, a path:line, "
                    "PINNED or DERIVED)")
    for row in sorted(listed - tree):
        p, _, fact = row.partition("\t")
        reds.append(f"pinned-facts: red · stale row {p} · `{fact}` is no unpinned fact of the tree: "
                    "`check pinned-facts --shrink` takes it off")
    lines.append(f"pinned-facts: {len(tree)} unpinned facts, {len(listed & tree)} listed")
    return reds, lines


def read_doors(pop) -> list:
    path = iu.derive_kit_file(pop["root"], DOORS)
    try:
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("door") or []
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise Refused(f"one-door: refused · the door list {path.as_posix()} does not read: {exc}") from None
    return rows


def check_one_door(pop, opts) -> tuple:
    root, reds, lines = pop["root"], [], []
    rows = read_doors(pop)
    tracked = set(p for p in iu.run_git(root, "ls-files", "-z").split("\0") if p)
    kinds = {}
    for row in rows:
        kinds.setdefault(row.get("kind"), []).append(row)
    for kind in DOOR_KINDS:
        if len(kinds.get(kind, ())) != 1:
            reds.append(f"one-door: red · kind {kind} has {len(kinds.get(kind, ()))} rows in {DOORS}: one door per kind")
    for kind in sorted(set(kinds) - set(DOOR_KINDS), key=str):
        reds.append(f"one-door: red · kind {kind} of {DOORS} is no kind of DOOR_KINDS")
    fill = lambda s: ti.resolve_prefix_token(s, iu.derive_kit_prefix()).replace(  # noqa: E731
        "{memory_root}", pop["memory_root"])
    for row in rows:
        kind = row.get("kind")
        if row.get("pending"):
            lines.append(f"one-door: pending · {kind} · its door lands with {row['pending']}")
            continue
        writer = fill(row.get("writer") or "")
        if writer not in tracked:
            reds.append(f"one-door: red · kind {kind}'s writer {writer or '(none)'} is no tracked file")
        nodes = iu.derive_tracked(root, fill(row.get("population") or "")) if row.get("population") else []
        witness = row.get("witness") or ""
        if not witness:
            lines.append(f"one-door: unobserved · {kind} · {len(nodes)} nodes, no witness to read")
            continue
        missing = [n for n in nodes if witness not in (root / n).read_text(encoding="utf-8", errors="replace")]
        for n in missing:
            write_finding("one-door", pop, n, f"{n} · a {kind} node without its writer's witness `{witness.strip()}`",
                   reds, lines)
        lines.append(f"one-door: {kind} · {len(nodes)} nodes, {len(nodes) - len(missing)} witnessed")
    return reds, lines


def check_rationale_apart(pop, opts) -> tuple:
    reds, builds = [], pop["memory_root"] + "/builds/"
    for u in pop["units"]:
        help_ = (u.help or "").strip()
        for path, text, _ls in pop["documents"]:
            if help_ and help_ in text:
                reds.append(f"rationale-apart: red · unit {u.tag}'s help is rendered in {path}")
        if builds in (u.text or "") + (u.source or ""):
            reds.append(f"rationale-apart: red · unit {u.tag} loads a build record path ({builds})")
    for row in pop["registry"]:
        for key in ("resolved", "source"):
            if str(row.get(key, "")).startswith(builds):
                reds.append(f"rationale-apart: red · document row {row.get('tag')} names the record path "
                            f"{row[key]} in the registry")
    return reds, []


def check_one_owner(pop, opts) -> tuple:
    root, reds = pop["root"], []
    builds = {p.split("/")[2] for p in iu.run_git(root, "ls-files", "-z", "--", f"{pop['memory_root']}/builds/")
              .split("\0") if p.count("/") >= 3}
    try:
        layers = {r.get("tag") for r in tomllib.loads(iu.derive_kit_file(root, "layers.toml").read_text(
            encoding="utf-8")).get("layer") or []}
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise Refused(f"one-owner: refused · the layer register does not read: {exc}") from None

    def check_names(where, owner):
        names = re.split(r"[\s,]+", owner.strip()) if isinstance(owner, str) else [str(o) for o in owner or []]
        names = [n for n in names if n]
        if len(names) != 1:
            reds.append(f"one-owner: red · {where} names {len(names)} owners ({', '.join(names) or 'none'}): one")
        elif names[0] not in builds and names[0] not in layers:
            reds.append(f"one-owner: red · {where} names {names[0]}, no build memory/builds/ holds and no layer")

    rows = 0
    for name, table in (("namespaces.toml", "namespace"), ("kinds.toml", "kind")):
        try:
            data = tomllib.loads(iu.derive_kit_file(root, name).read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            raise Refused(f"one-owner: refused · {name} does not read: {exc}") from None
        for i, row in enumerate(data.get(table) or [], 1):
            if "owner" in row:
                rows += 1
                check_names(f"{name} row {i} ({row.get('ns') or row.get('tag')})", row["owner"])
    for u in pop["units"]:
        where = f"unit {u.tag} ({u.path}:{u.line})"
        if u.origin == "repository":
            if u.owner:
                reds.append(f"one-owner: red · {where} is the repository's own and names the owner {u.owner}: none")
        elif u.owner is None:
            reds.append(f"one-owner: red · {where}, origin {u.origin}, names no owner: one")
        else:
            check_names(where, u.owner)
    return reds, [f"one-owner: {rows} registry rows, {len(pop['units'])} unit rows"]


CHECKS = {"one-subject": check_one_subject, "pinned-facts": check_pinned_facts, "one-door": check_one_door,
          "rationale-apart": check_rationale_apart, "one-owner": check_one_owner}


def run_arm(arm, pop, opts) -> int:
    if opts.explain:
        reads, unread = EXPLAIN[arm]
        frozen = ("a new fact under {}/builds/ is red as anywhere, today's held by the list" if arm == "pinned-facts"
                  else "a finding under {}/builds/ is printed, never red")
        print(f"{arm}: reads · {reads}\n{arm}: does not read · {unread}\n"
              f"{arm}: frozen · {frozen.format(pop['memory_root'])}")
    try:
        print("\n".join(derive_counts(arm, pop)))
        reds, more = CHECKS[arm](pop, opts)
    except Refused as exc:
        print(exc)
        return 2
    for line in more + reds:
        print(line)
    print(f"{arm}: {'RED' if reds else 'green'} · {len(reds)} red")
    return 1 if reds else 0


def run_check(root, arm, opts) -> int:
    if (opts.seed or opts.shrink) and arm != "pinned-facts":
        print("writing-practice: --seed and --shrink are pinned-facts' alone", file=sys.stderr)
        return 2
    pop = read_populations(root)
    rcs = [run_arm(a, pop, opts) for a in ((arm,) if arm else LEG_ARMS)]
    return 2 if 2 in rcs else max(rcs)


# ------------------------------------------------------------------------------------------ the fixture

FX_DOORS = "".join(
    f'[[door]]\nkind = "{k}"\npopulation = "{p}"\nwriter = "{w}"\nwitness = "{x}"\n\n' for k, p, w, x in (
        ("instruction-unit", "{prefix}/*/instructions.toml", "{prefix}/playbook/instructions_edit.py", ""),
        ("instruction-change", "{memory_root}/builds/*/build/*-change-*.md", "{prefix}/playbook/instructions_edit.py",
         ""),
        ("work-order", "{memory_root}/orders/*.md", "{prefix}/roles/handoff.py", "<!-- gov:handoff "),
        ("override", "{memory_root}/builds/*/build/*-override-*.md", "{prefix}/memory-tree/build_records.py", ""),
        ("exception", "{memory_root}/builds/*/build/*-exception-*.md", "{prefix}/memory-tree/build_records.py", ""))
) + "".join(f'[[door]]\nkind = "{k}"\npending = "dFx"\n\n' for k in ("record", "trailer", "act"))
FX_UNITS = ('[[unit]]\ntag = "unit.fx-one"\nlevel = 3\ntype = "directive"\nscope = ["reader.every"]\n'
            'text = "MUST read the fixture first."\nowner = "dFx"\nhelp = "the fixture rationale, never loaded"\n')
FX_HELP = "the fixture rationale, never loaded"
FX_FILES = {
    ".memory-tree.conf": 'MEMORY_ROOT="memory"\n',
    "AGENTS.md": "# Charter\n\n## Rules\n\n- [fx] Read the fixture first.\n\n## Tools\n\n- none\n",
    "{prefix}/playbook/documents.toml": ('[[document]]\ntag = "doc.charter"\npath = "AGENTS.md"\nlevel = 0\n'
                                      'direction = "the fixture charter"\nsource = "AGENTS.md"\n'),
    "{prefix}/playbook/doors.toml": FX_DOORS,
    "{prefix}/playbook/namespaces.toml": '[[namespace]]\nns = "doc"\nowner = "dFx"\n',
    "{prefix}/playbook/kinds.toml": '[[kind]]\ntag = "kind.fx"\nowner = "layer.instruction"\n',
    "{prefix}/playbook/layers.toml": '[[layer]]\ntag = "layer.instruction"\n',
    "{prefix}/playbook/instructions_edit.py": "# the fixture writer\n",
    "{prefix}/roles/handoff.py": "# the fixture writer\n",
    "{prefix}/memory-tree/build_records.py": "# the fixture writer\n",
    "{prefix}/fx/kit.toml": 'id = "fx-kit"\n',
    "{prefix}/fx/instructions.toml": FX_UNITS,
    "memory/guides/ALPHA.md": "# Alpha\n\n## Scope\n\nThe alpha guide.\n\n## Steps\n\n- read it\n",
    "memory/builds/dFx/README.md": "# dFx\n\n## Goal\n\nThe fixture build.\n",
    "memory/orders/2026-01-01-order.md": "<!-- gov:handoff role=gov-builder -->\n## Role\n",
    "memory/project/unpinned-facts.txt": "",
}
FACT = "the bar runs 142 legs"
#: plant -> (the arm it runs, None for every arm, the files it writes over the base, or a callable of the root)
PLANTS = {
    "none": (None, {}),
    "empty-records": (None, {"memory/guides/ALPHA.md": None, "memory/builds/dFx/README.md": None,
                             "memory/orders/2026-01-01-order.md": None}),
    "duplicate-heading": ("one-subject", {"memory/guides/BETA.md": "# Beta\n\n## Scope\n\na\n\n## Scope\n\nb\n"}),
    "duplicate-heading-frozen": ("one-subject", {"memory/builds/dFx/build/x.md": "# X\n\n## Scope\n\na\n\n## Scope\n"}),
    "duplicate-tag": ("one-subject", {"{prefix}/fx/instructions.toml": FX_UNITS + "\n" + FX_UNITS.replace(
        "MUST read the fixture first.", "MUST read it twice.")}),
    "unpinned-fact": ("pinned-facts", {"memory/guides/BETA.md": f"# Beta\n\n{FACT}\n"}),
    "pinned-fact": ("pinned-facts", {"memory/guides/BETA.md": f"# Beta\n\n{FACT} (PINNED, 2026-10-23)\n"}),
    "pinned-fact-oid": ("pinned-facts", "oid"),
    "fenced-fact": ("pinned-facts", {"memory/guides/BETA.md": f"# Beta\n\n```\n{FACT}\n```\n"}),
    "facts-stale": ("pinned-facts", {"memory/project/unpinned-facts.txt": "memory/guides/ALPHA.md\t9 files\n"}),
    "facts-no-list": ("pinned-facts", {"memory/project/unpinned-facts.txt": None}),
    "facts-seed-twice": ("pinned-facts", "seed-twice"),
    "door-unlisted": ("one-door", {"memory/orders/2026-01-02-order.md": "## Role\n\nwritten by hand\n"}),
    "door-twice": ("one-door", {"{prefix}/playbook/doors.toml": FX_DOORS + '[[door]]\nkind = "act"\npending = "dFy"\n'}),
    "door-untracked-writer": ("one-door", {"{prefix}/playbook/doors.toml": FX_DOORS.replace(
        "{prefix}/roles/handoff.py", "{prefix}/roles/absent.py")}),
    "help-rendered": ("rationale-apart", {"AGENTS.md": FX_FILES["AGENTS.md"] + f"\n{FX_HELP}\n"}),
    "record-loaded": ("rationale-apart", {"{prefix}/playbook/documents.toml": FX_FILES["{prefix}/playbook/documents.toml"]
                      + '\n[[document]]\ntag = "doc.fx-record"\npath = "{memory_root}/builds/dFx/README.md"\n'
                        'level = 3\ndirection = "a record loaded"\nsource = "AGENTS.md"\nh1 = "dFx"\n'}),
    "owner-faults": ("one-owner", {
        "{prefix}/playbook/namespaces.toml": '[[namespace]]\nns = "doc"\nowner = "dFx dFy"\n',
        "{prefix}/fx/instructions.toml": FX_UNITS.replace('owner = "dFx"\n', ""),
        ".governance/instructions.toml": FX_UNITS.replace("unit.fx-one", "unit.fx-repo")}),
}


def derive_fixture_files(files) -> dict:
    """`files` with each path's `{prefix}` the tool root this install lays its kits under."""
    return {ti.resolve_prefix_token(k, iu.derive_kit_prefix()): v for k, v in files.items()}


def write_fixture(root, files) -> None:
    import gov_tag
    gov_tag.run_git(root, "init", "-q", "-b", "main")
    gov_tag.write_commit(root, derive_fixture_files(FX_FILES), "the fixture")
    if callable(files) or isinstance(files, str):
        return
    gov_tag.write_files(root, derive_fixture_files(files))
    gov_tag.run_git(root, "add", "-A")
    gov_tag.run_git(root, "commit", "-q", "--allow-empty", "-m", "the plant")


def run_plant(root, plant) -> int:
    import gov_tag
    arm, files = PLANTS[plant]
    opts = argparse.Namespace(explain=False, seed=False, shrink=False)
    if files == "oid":
        oid = gov_tag.run_git(root, "rev-parse", "HEAD").strip()
        gov_tag.write_commit(root, {"memory/guides/BETA.md": f"# Beta\n\n{FACT} at {oid}\n"}, "the plant")
    if files == "seed-twice":
        gov_tag.write_commit(root, {"memory/project/unpinned-facts.txt": None,
                                    "memory/guides/BETA.md": f"# Beta\n\n{FACT}\n"}, "no list, one fact")
        print(f"writing-practice: plant {plant} · the first --seed")
        first = run_check(root, arm, argparse.Namespace(explain=False, seed=True, shrink=False))
        print(f"writing-practice: plant {plant} · the first --seed exited {first}; the second")
        return run_check(root, arm, argparse.Namespace(explain=False, seed=True, shrink=False))
    if arm:
        return run_check(root, arm, opts)
    pop = read_populations(root)
    rcs = [run_arm(a, pop, opts) for a in ARMS]
    print(f"writing-practice: plant {plant} · every arm exited {' '.join(map(str, rcs))}")
    return rcs[0] if len(set(rcs)) == 1 else 1


def run_fixture(plant) -> int:
    if plant not in PLANTS:
        print(f"writing-practice: no plant '{plant}': one of {', '.join(PLANTS)}", file=sys.stderr)
        return 2
    ti.load_memory_tree()
    from deviation_join import set_env_aside
    from tree_lib import GIT_ENV_LEAKS
    top = pathlib.Path(tempfile.mkdtemp(prefix="wp"))
    try:
        with set_env_aside(GIT_ENV_LEAKS):
            write_fixture(top, PLANTS[plant][1])
            return run_plant(top, plant)
    finally:
        def remove_readonly(fn, path, _exc):
            os.chmod(path, stat.S_IWRITE)
            fn(path)
        shutil.rmtree(top, onerror=remove_readonly)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="writing_practice.py")
    ap.add_argument("verb", nargs="?", choices=("check",))
    ap.add_argument("arm", nargs="?", choices=ARMS)
    ap.add_argument("--explain", action="store_true")
    ap.add_argument("--seed", action="store_true")
    ap.add_argument("--shrink", action="store_true")
    ap.add_argument("--fixture", action="store_true")
    ap.add_argument("--plant", default="none")
    ap.add_argument("--root", default=None)
    a = ap.parse_args(argv)
    if a.fixture:
        return run_fixture(a.plant)
    if a.verb != "check":
        ap.print_usage(sys.stderr)
        return 2
    root = pathlib.Path(a.root or iu.run_git(pathlib.Path.cwd(), "rev-parse", "--show-toplevel").strip())
    return run_check(root, a.arm, a)


if __name__ == "__main__":
    sys.exit(main())
