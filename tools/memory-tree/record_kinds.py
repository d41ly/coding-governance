#!/usr/bin/env python3
"""record_kinds.py — the record-kind registry's reader, gate, view and factory (TOOL-dTotalRecall-1, -18, -16, -25).

    python <prefix>/memory-tree/record_kinds.py --check             # the `record-kinds` leg
    python <prefix>/memory-tree/record_kinds.py --write             # the HYGIENE template's kind region
    python <prefix>/memory-tree/record_kinds.py --template <kind>   # the record skeleton of one kind
    python <prefix>/memory-tree/record_kinds.py new <name> --tag record.<name> --writer <door>
                                                --check <leg> --home <glob>
                                                --layer <tag> --lifecycle <value> --purpose <text>
                                                (--reader <key>... | --readers-none <reason>)
                                                (--field <Key>... | --form fence --validator <module>:<function>)
    python <prefix>/memory-tree/record_kinds.py --purpose-review [--from <path>] [--write [--ask <id>]]
    python <prefix>/memory-tree/record_kinds.py --print-purpose-pending   # the purpose-pending seed
    python <prefix>/memory-tree/record_kinds.py --seed-legacy       # the record-kinds-legacy seed
    python <prefix>/memory-tree/record_kinds.py --print-gap-keys    # the gap-key native class's members
    python <prefix>/memory-tree/record_kinds.py --fixture [--plant <case>]
    python <prefix>/memory-tree/record_kinds.py --selftest

ONE DECLARATION PER KIND. `record-kinds.toml` beside this file holds one `[[record-kind]]` row per
record kind, its columns `name`, `tag`, `layer`, `home`, `id-rule`, `schema`, `writer`, `readers`,
`readers-none`, `lifecycle`, `check` and `purpose`; `root` and `sections` are admitted for the units that
add them. Every row carries `name`, `tag` (`record.<name>`), `layer` (a `layer.<name>` tag, the
layer of the kit whose writer writes the kind), `home`, `schema`, `writer`, `readers`, `lifecycle`
(one of `LIFECYCLES`), `check` and `purpose`. `purpose` is `{ text, source }`, one line of at most
`PURPOSE_BYTES` and its source `<path>:<line>`, a tracked path and a line in it, or `owner`; or
`{ pending = "<id>" }`, which `memory.map-purpose` grades. `home` is one glob or a list of them, each a tracked-path glob,
a ref glob `refs/gov/<glob>` or `<git-common-dir>/<glob>`; a `fields` row's is one tracked glob, the
population it grades. `readers` lists the work-order read keys a handoff fills from a record of the
kind, each a member of the roles kit's `READ_KEYS` that some role's `reads:` names; a kind no role
reads carries `readers = []` and a non-empty `readers-none` reason. `schema` is
`{ form, fields, source, validator }`: `form` one of `fields`, `header`, `rows`, `generated`, `fence`;
`fields` the `**Key:**` lines a record carries; `source`, optional, `<path>:<NAME>[.<key>]...`, its path
spelled through `{prefix}`, the literal another module declares the same fields in, read with `ast` and
never by import, so a sibling kit's table is read without crossing a kit boundary; `validator`, on a
`fence` row alone and required there, `<module>:<function>`, a `<module>.py` of this kit's own directory
and a function at its top level taking a record's text and returning its reds (`resolve_validator`).

THE VIEW, the HYGIENE template's `gen:record-kinds` region, is one `<n> kinds · <p> purposes pending`
line and one table line per row: `Kind`, `Tag`, `Home`, `Writer`, `Read by`, `Written by`, `Check` and
`Purpose`, the text or `—`, each `|` in a value written `\\|`. `Read by`
is the roles whose `reads:` holds one of the row's `readers` and the loop items whose `inputs` hold a
typed record reference `<layer tag>:record-kind.<name>[@<n>]` (`loop_items.derive_record_ref`); a
prose input joins nothing. `Written by` is the roles whose `writes:` folder in the roles kit's
`WRITE_FOLDERS` covers one of the row's homes, `<slug>` read as `*`, and the items whose `returns`
reads as `record-kind.<name>`. The roles come from `roles_lib.load_roles` and the items from
`loop_lib.read_definition` and `read_item_rows`, both kits found by the inline `resolve_kit_dir`
block (the `requires_if` rows of this kit's `kit.toml`), their modules from this install and their
role files and definition from the tree checked. `--check`, `--write` and `new` each read them
afresh, so the byte compare is with a live re-derivation; an empty role population, a kit that does
not resolve or a definition that does not read is `unarmed` naming it: red under `--check`, `unarmed`
cells under `--write` and `new`.

THE GATE, `--check`, reds: no row; a row missing a required column or carrying an unknown one; a
column outside its grammar; a reader key outside `READ_KEYS` or read by no role; an empty `writer`;
a `check` naming no leg of the tool root's `gate-legs.json`; a `source` whose literal does not hold
the row's `fields` both ways; a member of the typed kind list (`tree_lib.TYPED_RECORD_KINDS`) with no
row, and a factory row (its `source` the factory's `KINDS.<kind>.required`) naming no member. It
grades each `fields` row's population: every tracked record its `home` matches carries each field as
a `**Key:**` line, bare or a `- **Key:**` bullet, in the row's order, except a record the
`record-kinds-legacy` ledger lists against that row, each ledger row's section read through
`tree_lib.resolve_kind`, so the rows keyed `journal` stand for the `log` row with their bytes kept.
A typed kind's row grades only the paths its name grammar (`build_records.derive_record_name`) also
matches, and a path a typed grammar matches is graded by that kind's row alone. A typed kind whose home
matches nothing prints `<kind>: unarmed — no record yet` and passes; any other empty population
reds. THE FENCE ARM, `check_fence_records`, runs each `fence` row's resolved validator over every
tracked record its home matches, narrowed as a `fields` row's is, each red prefixed `row <kind>: <path>:`
and the row counted `<kind> fence <n> graded`; a validator that does not resolve is one red of the row
and grades nothing. `check_stream_plan` is the `stream-plan` kind's: its one TOML fence of `[[stream]]`
tables, each unit's `order` read by the spec header verb's grammar, and its unarmed line names its
writer (`STREAM_PLAN_UNARMED`). A graded deviation's `Follow-through: gap <key>` must name a key some tracked gap register
holds, and no register holding a key reds. The HYGIENE template's `gen:record-kinds` region must be
byte for byte what `--write` writes. THE POCKET ARM, `check_pockets`, lists the top-level entries of
the common git dir (the inline `common_git_dir` block), skips git's own (`GIT_OWN`), and reds each
entry no row's `<git-common-dir>/` home glob matches on its first segment. THE ALIAS JOIN reads the
runlog kit's `SERVES_ALIASES` from its `record.py` by `ast` and reds where it differs from the
`tree_lib.KIND_ALIASES` keys whose target is `log`; where that kit does not resolve it prints
`unarmed` and passes, since this kit does not require it. THE PENDING RULE reads `memory.map-purpose`
once through `tree_lib.read_policy_value` and grades each `pending` row by it: under `review` an open
ask, a row of a tracked `<memory root>/builds/*/BACKLOG.md` no `CLOSED` or `WONTDO` row names; under
`ledger` `purpose-pending` and the node a row of that `[[ledger]]` population, a listed node now
carrying a text red; under `derive` `none-found`; under `refuse` no pending at all. No policy kit
reads the default `review` with one line saying so; a refused read exits 2 naming the key. It prints one
count line naming every row, each `fields` kind's graded and legacy counts, each `unarmed` kind, the
purpose line, one `view` line per row, each pocket entry with the row it matched, and every red with
its row.

THE PURPOSE REVIEW, `--purpose-review`, tries each registry row with no `text` and each row of the
chain registry with no `purpose` (`<memory root>/` plus the playbook kit's `tag_index.py`
CHAIN_REGISTRY, read by `ast`; `unarmed chain` where it does not resolve) in order: the H1 of the
node's file after its name and the dash (a chain build's README; a kind has none), then the row of a
Markdown table of the tracked `--from` record whose first cell, `-` read as a space and through
`resolve_kind`, names the kind, its last cell the text; a text cut at a word boundary under
`PURPOSE_BYTES`, one only repeating the name tried past. It prints `derived <node> · <text> ·
<source>` or `none <node> · <found>` per node and one `ask <namespace> · …` draft per namespace with a
`none` node, none under `derive`. `--write` inserts one line per node: a registry row's `purpose`
table, a chain row's `purpose` string, and each `none` registry row's pending, `--ask`'s open ask
under `review`, `purpose-pending` under `ledger`, `none-found` under `derive`, nothing under
`refuse`; a `none` chain row is never written. It exits 2 writing nothing on an untracked `--from`, an
`--ask` that is no open ask, or `ledger` with no `[[ledger]]` row registering `purpose-pending`.

Exit 0 green, 1 a red, 2 a refusal: a registry that does not parse, or a verb's malformed arguments.
`new` appends the row and re-renders that region from the registry, so the two move together; it
exits 2 and writes nothing on a duplicate name, a tag that is not `record.<name>`, an empty
writer, no `--home`, a `--form` other than `fields`, its default, or `fence`, a `fields` row with no
`--field` or with a `--validator`, a `fence` row with a `--field` or with no `--validator` or one that
does not resolve, a check no leg carries, no `--layer` or one that is no
`layer.<name>` tag, no `--lifecycle` or one outside `LIFECYCLES`, no `--reader` and no
`--readers-none`, both, or a reader key the roles do not read, or no `--purpose`, an empty one, one
past `PURPOSE_BYTES` or one holding a newline; its row's purpose `source` is `owner`, and a member of the
typed kind list gets the factory's `KINDS.<name>.required` as its schema `source` and
`<date>-build-<unit id>-<name>-<n>.md` as its `id-rule`. `--print-gap-keys` exits 3 where no
gap register is tracked, the native class's not-armed answer.

WHAT IT DOES NOT CHECK. Whether a row's `writer` writes the kind: the cell is read, never run. A
field's value, only its line. A `gap-key` at an edge site, since no edge type names the class. A
`header`, `rows` or `generated` row's records, which its `check` leg's owner grades. Whether a stream
plan's unit id names a spec, or agrees with the specs' `order` verbs. Whether a
non-`fields` row's tracked home matches a file, or a `refs/gov/` home a ref. Whether a `layer` tag
is a row of the playbook kit's layer register: its shape only. A `WRITE_FOLDERS` value that is no
folder (the product class's conf key) covers no home. A pocket's contents, which it never reads.
Whether a derived purpose describes its node: the citation makes it checkable, never checked. An ask
closed only by a spec header's `closes`, read as open. The chain rows, which `--check` never grades.
"""
from __future__ import annotations

import argparse
import ast
import fnmatch
import importlib
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
COLUMNS = ("name", "tag", "layer", "home", "id-rule", "schema", "writer", "readers", "readers-none", "lifecycle",
           "check", "purpose")
LATER_COLUMNS = ("root", "sections")   # TOOL-dTotalRecall-19's and -9's, admitted and graded by their owners
REQUIRED = ("name", "tag", "layer", "home", "schema", "writer", "readers", "lifecycle", "check", "purpose")
#: TOOL-dTotalRecall-16 S1: a purpose's one line, in UTF-8 bytes (PINNED, the cap that spec sets).
PURPOSE_BYTES = 120
PURPOSE_KEYS = ("text", "source", "pending")
PURPOSE_SOURCE_RE = re.compile(r"(?P<path>[^\s:][^:]*):(?P<line>[1-9][0-9]*)")
#: `memory.map-purpose`'s values, its catalogue default, and the two pending values S6 mints.
MAP_PURPOSE_VALUES = ("review", "ledger", "derive", "refuse")
MAP_PURPOSE_DEFAULT = "review"
PURPOSE_PENDING = "purpose-pending"
NONE_FOUND = "none-found"
REGISTRY_NS, CHAIN_NS = "record-kind", "chain"
LIFECYCLES = ("append-only", "current-state", "frozen", "generated", "out")
LAYER_RE = re.compile(r"layer\.[a-z][a-z0-9-]*(?:\.[a-z][a-z0-9-]*)*")
COMMON_DIR_HOME = "<git-common-dir>/"
REF_HOME = "refs/gov/"
#: Git's own entries of a common dir, never a pocket (TOOL-dTotalRecall-18 S6).
GIT_OWN = frozenset(("HEAD", "ORIG_HEAD", "FETCH_HEAD", "MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD",
                     "COMMIT_EDITMSG", "config", "description", "hooks", "index", "info", "logs", "objects",
                     "packed-refs", "refs", "worktrees", "modules", "lost-found", "shallow", "gc.log"))
UNARMED = "unarmed"
FORMS = ("fields", "header", "rows", "generated", "fence")
SCHEMA_KEYS = ("form", "fields", "source", "validator")
NEW_FORMS = ("fields", "fence")   # the forms `new` writes (TOOL-dTotalRecall-25 S7)
#: a `fence` row's `schema.validator`: a bare module of this kit's directory and a function at its top level
VALIDATOR_RE = re.compile(r"(?P<module>[A-Za-z_][A-Za-z0-9_]*):(?P<function>[A-Za-z_][A-Za-z0-9_]*)")
#: a record's machine half, the regex the codebase map's `parse_dossier` reads a dossier's with, carried as
#: its own constant since the kits do not import each other
TOML_FENCE_RE = re.compile(r"^```toml[ \t]*\r?$(.*?)^```[ \t]*\r?$", re.MULTILINE | re.DOTALL)
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


def read_git_stdout(repo, *args: str) -> str:
    """`git -C <repo> <args>`'s standard output; RecordKindsError where git refuses."""
    p = run_git(repo, *args)
    if p.returncode != 0:
        raise RecordKindsError(f"git {' '.join(args)} refused in {repo}: {p.stderr.strip()}")
    return p.stdout


git = read_git_stdout  # the name the common_git_dir block below calls

# >>> common_git_dir -- canonical copy: common_dir.py in the gov lib dir (byte-identical; gated)
def common_git_dir(repo: pathlib.Path) -> pathlib.Path:
    """The MAIN repository's git directory, shared by every worktree.

    ``--git-dir`` in a linked worktree is ``.git/worktrees/<name>``, which ``git worktree remove``
    deletes outright -- taking the query log with it. It is also RELATIVE (bare ``.git``) when run
    at the repo root and absolute elsewhere, so the raw value is not a usable path either way.
    """
    raw = git(repo, "rev-parse", "--git-common-dir").strip()
    p = pathlib.Path(raw)
    return p.resolve() if p.is_absolute() else (repo / raw).resolve()
# <<< common_git_dir

# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


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


def derive_home_globs(home) -> list[str]:
    """A row's `home` as its list of globs: one string, or each string of a list."""
    if isinstance(home, str):
        return [home] if home.strip() else []
    return [h for h in home if isinstance(h, str)] if isinstance(home, list) else []


def check_home(home, at: str, form) -> list[str]:
    """The reds of one row's `home`: one glob or a non-empty list, each a tracked-path glob, `refs/gov/<glob>`
    or `<git-common-dir>/<glob>`; a `fields` row's one tracked glob."""
    if not (isinstance(home, str) or (isinstance(home, list) and home and all(isinstance(h, str) for h in home))):
        return [f"{at}: `home` is neither a glob nor a non-empty list of globs"]
    globs = derive_home_globs(home)
    if not globs:
        return [f"{at}: the column `home` is empty: name the glob its records live at"]
    reds = []
    for g in globs:
        lead = next((p for p in (COMMON_DIR_HOME, REF_HOME) if g.startswith(p)), "")
        rest = g[len(lead):]
        if (not rest.strip() or rest.startswith("/") or "\\" in g or ".." in rest.split("/")
                or (not lead and ("<" in g or g.startswith("refs/")))):
            reds.append(f"{at}: home {g!r} is none of a tracked-path glob, `{REF_HOME}<glob>` or `{COMMON_DIR_HOME}<glob>`")
        elif form == "fields" and (lead or not isinstance(home, str)):
            reds.append(f"{at}: a `fields` row's home {g!r} is not one tracked-path glob, the population it grades")
    return reds


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
    for col in ("layer", "lifecycle", "id-rule"):
        if col in row and not isinstance(row[col], str):
            reds.append(f"{at}: `{col}` is not a string")
    if isinstance(row.get("layer"), str) and not LAYER_RE.fullmatch(row["layer"]):
        reds.append(f"{at}: the column `layer` {row['layer']!r} is no `layer.<name>` tag: name the layer of the "
                    f"kit whose writer writes the kind")
    if isinstance(row.get("lifecycle"), str) and row["lifecycle"] not in LIFECYCLES:
        reds.append(f"{at}: the column `lifecycle` {row['lifecycle']!r} is not one of {', '.join(LIFECYCLES)}")
    if "home" in row:
        reds += check_home(row["home"], at, (row.get("schema") or {}).get("form") if isinstance(row.get("schema"), dict) else None)
    readers, none_why = row.get("readers"), row.get("readers-none")
    if "readers" in row and not (isinstance(readers, list) and all(isinstance(r, str) and r for r in readers)):
        reds.append(f"{at}: `readers` is not a list of read keys")
    elif "readers" in row and not readers and not (isinstance(none_why, str) and none_why.strip()):
        reds.append(f"{at}: `readers` is empty and `readers-none` gives no reason: name the read keys a handoff "
                    f"fills from the kind, or say why no role reads it")
    elif readers and "readers-none" in row:
        reds.append(f"{at}: `readers` names keys and `readers-none` says no role reads the kind: keep one")
    if "purpose" in row:
        reds += check_purpose_cell(row["purpose"], at, root)
    schema = row.get("schema")
    if "schema" not in row:
        return reds
    if not isinstance(schema, dict):
        return reds + [f"{at}: `schema` is not a table"]
    reds += [f"{at}: `schema.{k}` is no schema key ({', '.join(SCHEMA_KEYS)})" for k in schema if k not in SCHEMA_KEYS]
    fields = schema.get("fields", [])
    if schema.get("form") not in FORMS:
        reds.append(f"{at}: schema.form {schema.get('form')!r} is not one of {', '.join(FORMS)}")
    if schema.get("form") == "fence":   # S4: a fence row's validator resolves, and no other form names one
        if "validator" not in schema:
            reds.append(f"{at}: a `fence` row names no `schema.validator` <module>:<function>, so no record of it is graded")
        else:
            reds += [f"{at}: {why}" for fn, why in [resolve_validator(schema["validator"])] if fn is None]
    elif "validator" in schema:
        reds.append(f"{at}: `schema.validator` on a {schema.get('form')!r} row: only a `fence` row names a validator")
    if not (isinstance(fields, list) and all(isinstance(f, str) and f for f in fields)):
        return reds + [f"{at}: schema.fields is not a list of field names"]
    if schema.get("form") == "fields":
        if not fields:
            reds.append(f"{at}: a `fields` row declares no field")
        if not (isinstance(row.get("home"), str) and row["home"].strip()):
            reds.append(f"{at}: a `fields` row's `home` is not one tracked glob, so it grades no record")
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


def check_purpose_cell(purpose, at: str, root) -> list[str]:
    """S1's grammar of one row's `purpose`: `{ text, source }` or `{ pending }`, no other key and never both
    forms; `text` one line of at most `PURPOSE_BYTES`; `source` `owner` or `<path>:<line>`, a tracked path
    and a line inside it."""
    if not isinstance(purpose, dict):
        return [f"{at}: `purpose` is not a table: write {{ text, source }} or {{ pending }}"]
    reds = [f"{at}: `purpose.{k}` is no purpose key ({', '.join(PURPOSE_KEYS)})" for k in purpose if k not in PURPOSE_KEYS]
    if "pending" in purpose and ("text" in purpose or "source" in purpose):
        return reds + [f"{at}: `purpose` holds a text and a pending at once: keep one"]
    if "pending" in purpose:
        if not (isinstance(purpose["pending"], str) and purpose["pending"].strip()):
            reds.append(f"{at}: `purpose.pending` is no id: name the ask, `{PURPOSE_PENDING}` or `{NONE_FOUND}`")
        return reds
    text, source = purpose.get("text"), purpose.get("source")
    if not (isinstance(text, str) and text.strip()):
        reds.append(f"{at}: `purpose.text` is empty or missing: say what the kind is for in one line")
    elif "\n" in text or "\r" in text:
        reds.append(f"{at}: `purpose.text` holds a newline: a purpose is one line")
    elif len(text.encode("utf-8")) > PURPOSE_BYTES:
        reds.append(f"{at}: `purpose.text` is {len(text.encode('utf-8'))} bytes, past PURPOSE_BYTES {PURPOSE_BYTES}")
    m = PURPOSE_SOURCE_RE.fullmatch(source) if isinstance(source, str) else None
    if source == "owner":
        return reds
    if m is None:
        return reds + [f"{at}: `purpose.source` {source!r} is neither `owner` nor `<path>:<line>`"]
    path = pathlib.Path(root, m["path"])
    tracked = run_git(root, "ls-files", "--", f":(literal){m['path']}").stdout.strip()
    if not tracked or not path.is_file():
        return reds + [f"{at}: `purpose.source` {source!r} cites {m['path']}, which is no tracked file"]
    if int(m["line"]) > len(path.read_bytes().decode("utf-8", "replace").rstrip("\n").split("\n")):
        reds.append(f"{at}: `purpose.source` {source!r} cites a line past the end of {m['path']}")
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


def scan_fence_records(root, rows: list[dict], typed_kinds) -> dict:
    """`{row name: [path...]}`: every tracked record each `fence` row's tracked-path home globs match,
    narrowed as `scan_legacy_records` narrows a `fields` row's: a typed kind's row keeps the paths its name
    grammar also matches, and a path some typed grammar matches is kept for that kind's row alone."""
    from build_records import derive_record_name
    grammars = {k: derive_record_name(k) for k in typed_kinds}
    out = {}
    for row in rows:
        schema = row.get("schema") if isinstance(row.get("schema"), dict) else {}
        if schema.get("form") != "fence":
            continue
        name, keep = row.get("name"), []
        for glob in derive_home_globs(row.get("home")):
            if glob.startswith((COMMON_DIR_HOME, REF_HOME)):
                continue
            for path in read_tracked(root, glob):
                typed = [k for k, g in grammars.items() if g.search(path)]
                if ((name in typed) if name in grammars else not typed) and path not in keep:
                    keep.append(path)
        out[name] = keep
    return out


def resolve_validator(spelled):
    """S4: `(callable, "")` for a `fence` row's `<module>:<function>`, the module a `<module>.py` in this
    kit's own directory and the function a callable at its top level; `(None, reason)` where it does not
    resolve. Only a bare module name of this directory is imported, so a registry cell names no code
    elsewhere."""
    m = VALIDATOR_RE.fullmatch(spelled) if isinstance(spelled, str) else None
    if m is None:
        return None, (f"validator {spelled!r} is not <module>:<function>, a bare module of the memory-tree kit's "
                      f"directory and a function at its top level")
    module, function = m["module"], m["function"]
    if not (KIT / f"{module}.py").is_file():
        return None, f"validator {spelled}: no {module}.py in the memory-tree kit's directory"
    try:   # this module by its own name, whether it runs as a script or was loaded by path
        mod = sys.modules[__name__] if module == pathlib.Path(__file__).stem else importlib.import_module(module)
    except Exception as e:   # noqa: BLE001 — any import failure is the reason the cell does not resolve
        return None, f"validator {spelled}: {module} does not import: {type(e).__name__}: {e}"
    if pathlib.Path(getattr(mod, "__file__", "") or "").resolve().parent != KIT.resolve():
        return None, f"validator {spelled}: {module} imports from outside the memory-tree kit's directory"
    fn = vars(mod).get(function)
    if not callable(fn):
        return None, f"validator {spelled}: {module} holds no top-level function {function}"
    return fn, ""


def check_fence_records(root, rows: list[dict], typed_kinds) -> tuple[list[str], list[str]]:
    """S4's grading arm: `(reds, unarmed)`. Each `fence` row whose validator resolves runs it over every record
    `scan_fence_records` keeps for it, each red it returns prefixed `row <kind>: <path>:`; a row whose
    validator does not resolve is `check_row`'s red alone, skipped here. A typed row matching no record is
    `unarmed`, the stream-plan kind's line naming its writer; any other empty population reds."""
    reds, unarmed = [], []
    population = scan_fence_records(root, rows, typed_kinds)
    for row in rows:
        name = row.get("name")
        if name not in population:
            continue
        fn, _why = resolve_validator((row.get("schema") or {}).get("validator"))
        if fn is None:
            continue
        paths = population[name]
        if not paths and name in typed_kinds:
            tail = f"; {STREAM_PLAN_UNARMED}" if getattr(fn, "__name__", "") == check_stream_plan.__name__ else ""
            unarmed.append(f"{name}: {UNARMED} — no record yet{tail}")
        elif not paths:
            reds.append(f"row {name}: its home {row.get('home')!r} matches no tracked record")
        for p in paths:
            text = pathlib.Path(root, p).read_bytes().decode("utf-8", "replace")
            try:
                got = fn(text)
            except Exception as e:   # noqa: BLE001 — a validator that raises grades nothing, and says so
                got = [f"its validator raised {type(e).__name__}: {e}"]
            reds += [f"row {name}: {p}: {r}" for r in got]
    return reds, unarmed


#: the tail of the stream-plan kind's unarmed line, the text TOOL-dTotalRecall-42 S3 moves onto the row
STREAM_PLAN_UNARMED = "its writer is dIndexedDesign's planner"


def check_stream_plan(text: str) -> list[str]:
    """S3: the reds of one stream-plan record, its one TOML fence of `[[stream]]` tables, each a `name` of
    `build_records.SEG`'s shape and `units`, a non-empty list of `{ id, order }`: a missing or unparseable
    fence, a stream with no units, a unit with no `order`, an `order` that is no `int` above zero matched
    whole by the spec header verb's grammar (`gen_build_index.ORDER_RE`), and a unit id named twice."""
    from build_records import SEG
    from gen_build_index import ORDER_RE
    m = TOML_FENCE_RE.search(text)
    if m is None:
        return ["no ```toml fence: a stream plan is one TOML fence of [[stream]] tables"]
    try:
        data = tomllib.loads(m.group(1))
    except tomllib.TOMLDecodeError as e:
        return [f"its toml fence does not parse: {e}"]
    streams = data.get("stream")
    if not (isinstance(streams, list) and streams and all(isinstance(s, dict) for s in streams)):
        return ["its toml fence holds no [[stream]] table"]
    reds, seen = [], {}
    for i, stream in enumerate(streams, 1):
        name = stream.get("name")
        at = f"stream {name}" if isinstance(name, str) and name else f"stream #{i}"
        if not (isinstance(name, str) and re.fullmatch(SEG, name)):
            reds.append(f"{at}: name {name!r} is no word of {SEG}")
        units = stream.get("units")
        if not (isinstance(units, list) and units):
            reds.append(f"{at}: no units: a stream lists one {{ id, order }} per unit")
            continue
        for j, unit in enumerate(units, 1):
            uid = unit.get("id") if isinstance(unit, dict) else None
            if not (isinstance(uid, str) and uid.strip()):
                reds.append(f"{at}: unit #{j} names no id")
                continue
            seen.setdefault(uid, []).append(at)
            if "order" not in unit:
                reds.append(f"{at}: unit {uid} carries no order")
                continue
            n = unit["order"]
            hit = ORDER_RE.search(f"· order {n}") if isinstance(n, int) and not isinstance(n, bool) and n > 0 else None
            if not (hit and hit.group(1) == str(n)):
                reds.append(f"{at}: unit {uid}: order {n!r} is no whole number above zero, the grammar a spec "
                            f"header's `· order <n>` is read by")
    reds += [f"unit {uid} is named in {' and '.join(ats)}: a unit sits in one stream"
             for uid, ats in seen.items() if len(ats) > 1]
    return reds


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
def read_view_joins(root, kit_rel: str) -> dict:
    """S2's sources, read afresh from the tree at `root`: `{"unarmed": [why...], "roles": {slot: (reads, writes)},
    "items": [(tag, inputs, returns)], "read_keys", "folders", "record_ref", "memory_root"}`. The roles and loop
    kits' modules are this install's, found by `resolve_kit_dir` from this file; their role files and their
    definition are the tree's, found from the kit directory under `root`. A kit that does not resolve, an empty
    role population or a definition that does not read is one `unarmed` reason naming it."""
    out = {"unarmed": [], "roles": {}, "items": [], "read_keys": frozenset(), "folders": {}, "record_ref": None,
           "memory_root": "memory"}
    here = pathlib.Path(root, kit_rel)
    try:
        out["memory_root"] = read_memory_root(root)
    except (OSError, ValueError):
        pass
    try:
        code = resolve_kit_dir("roles", "roles_lib.py", KIT)
        if str(code) not in sys.path:
            sys.path.append(str(code))
        import check_roles
        import roles_lib
        out["read_keys"], out["folders"] = roles_lib.READ_KEYS, dict(check_roles.WRITE_FOLDERS)
        tree = resolve_kit_dir("roles", "roles_lib.py", here)
        roles = roles_lib.load_roles(tree)
        if not roles:
            out["unarmed"].append(f"the roles kit at {tree.as_posix()} holds no role under agents/, so no role reads "
                                  f"or writes a kind")
        for slot, role in roles.items():
            keys = role.get("keys") or {}
            reads = {k.strip().rstrip("?") for k in str(keys.get("reads") or "").split(",") if k.strip()}
            out["roles"][slot] = (reads, str(keys.get("writes") or "").strip())
    except LookupError as e:
        out["unarmed"].append(f"the roles kit does not resolve: {e}")
    except Exception as e:   # noqa: BLE001 — `RolesError`, the roles kit's one refusal, is a bare Exception
        out["unarmed"].append(f"the roles kit's role files do not read: {type(e).__name__}: {e}")
    try:
        code = resolve_kit_dir("loop", "loop_lib.py", KIT)
        if str(code) not in sys.path:
            sys.path.append(str(code))
        import loop_items
        import loop_lib
        out["record_ref"] = loop_items.derive_record_ref
        data, where = loop_lib.read_definition(resolve_kit_dir("loop", "loop_lib.py", here))
        for r in loop_lib.read_item_rows(data, where):
            inputs = r.get("inputs") if isinstance(r.get("inputs"), list) else []
            returns = r.get("returns")
            out["items"].append((str(r.get("tag") or "?"), [i for i in inputs if isinstance(i, str)],
                                 [x for x in (returns if isinstance(returns, list) else [returns]) if isinstance(x, str)]))
    except LookupError as e:
        out["unarmed"].append(f"the loop kit does not resolve: {e}")
    except (ImportError, OSError, ValueError) as e:   # LoopError is a ValueError naming the file and the row
        out["unarmed"].append(f"the loop kit's definition does not read: {type(e).__name__}: {e}")
    return out


def derive_read_by(row: dict, joins: dict) -> list[str]:
    """The roles whose `reads:` holds one of the row's `readers`, then the items whose `inputs` hold a typed
    record reference to the row's kind; never an input's prose."""
    keys = set(row.get("readers") or []) if isinstance(row.get("readers"), list) else set()
    roles = [slot for slot, (reads, _w) in sorted(joins["roles"].items()) if reads & keys]
    want = f"record-kind.{row.get('name')}"
    ref = joins["record_ref"]
    items = [tag for tag, inputs, _r in joins["items"]
             if ref and any((got := ref(i.partition(":")[2])) and got[0] == want for i in inputs)]
    return roles + items


def derive_folder_glob(folder: str, memory_root: str) -> str | None:
    """A `WRITE_FOLDERS` value as a home-glob prefix, `<slug>` read as `*`; None for a value that is no folder."""
    if not folder.endswith("/"):
        return None
    return folder.replace("{{MEMORY_ROOT}}", memory_root).replace("<slug>", "*")


def derive_written_by(row: dict, joins: dict) -> list[str]:
    """The roles whose `writes:` folder covers one of the row's homes, then the items whose `returns` reads as
    the row's kind."""
    homes = derive_home_globs(row.get("home"))
    roles = []
    for slot, (_reads, writes) in sorted(joins["roles"].items()):
        prefix = derive_folder_glob(joins["folders"].get(writes, ""), joins["memory_root"])
        if prefix and any(h.startswith(prefix) for h in homes):
            roles.append(slot)
    want, ref = f"record-kind.{row.get('name')}", joins["record_ref"]
    items = [tag for tag, _i, returns in joins["items"]
             if ref and any((got := ref(x)) and got[0] == want for x in returns)]
    return roles + items


def render_kind_region(rows: list[dict], joins: dict) -> str:
    """The `gen:record-kinds` region, its markers included: one table line per row, its `Read by` and
    `Written by` cells derived from `joins` (`unarmed` where they are), each `|` in a value written `\\|`."""
    def render_cell(v):
        if isinstance(v, list):
            return ", ".join(render_cell(x) for x in v) if v else "—"
        return ("`" + v.replace("|", "\\|") + "`") if isinstance(v, str) and v else "—"
    def render_join(names):
        return UNARMED if joins["unarmed"] else render_cell(names)
    def render_purpose(purpose):   # the text as prose, its `|` escaped; `—` for a pending or no purpose
        text = purpose.get("text") if isinstance(purpose, dict) else None
        return text.replace("|", "\\|") if isinstance(text, str) and text else "—"
    pending = sum(1 for r in rows if isinstance(r.get("purpose"), dict) and "pending" in r["purpose"])
    lines = [REGION_OPEN, "", f"{len(rows)} kinds · {pending} purposes pending", "",
             "| Kind | Tag | Home | Writer | Read by | Written by | Check | Purpose |",
             "|---|---|---|---|---|---|---|---|"]
    lines += [f"| {render_cell(r.get('name'))} | {render_cell(r.get('tag'))} | {render_cell(r.get('home'))} | "
              f"{render_cell(r.get('writer'))} | {render_join(derive_read_by(r, joins))} | "
              f"{render_join(derive_written_by(r, joins))} | {render_cell(r.get('check'))} | "
              f"{render_purpose(r.get('purpose'))} |" for r in rows]
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
    joins = read_view_joins(root, kit_rel)
    for why in joins["unarmed"]:
        print(f"{SAY}: {UNARMED} — {why}; the view's read-by and written-by cells say so")
    new = text[:span[0]] + render_kind_region(rows, joins) + text[span[1]:]
    if new != text:
        path.write_bytes(new.encode("utf-8"))
    print(f"{SAY}: wrote the region of {TEMPLATE}, {len(rows)} rows" if new != text else f"{SAY}: region current")
    return 0


# -------------------------------------------------------------------------------------- the gate
def check_readers(rows: list[dict], joins: dict) -> list[str]:
    """S1's reader grammar: each key of a row's `readers` a member of `READ_KEYS` some role's `reads:` names."""
    read = set().union(*(reads for reads, _w in joins["roles"].values())) if joins["roles"] else set()
    reds = []
    for row in rows:
        for key in row.get("readers") or [] if isinstance(row.get("readers"), list) else []:
            if key not in joins["read_keys"]:
                reds.append(f"row {row.get('name')}: reader {key!r} is no read key of the roles kit's READ_KEYS")
            elif key not in read:
                reds.append(f"row {row.get('name')}: reader {key!r} is a read key no role's `reads:` names")
    return reds


def check_pockets(root, rows: list[dict]) -> tuple[list[str], list[str]]:
    """S6's pocket arm: `(lines, reds)` over the top-level entries of the common git dir, git's own
    (`GIT_OWN`) skipped, each other entry matched against every row's `<git-common-dir>/` home glob on its
    first segment; an entry no row matches is a red naming it and the remedy. It lists, never reads."""
    try:
        common = common_git_dir(pathlib.Path(root))
        entries = sorted(p.name for p in common.iterdir())
    except (RecordKindsError, OSError) as e:
        return [], [f"pocket: {UNARMED} — the common git dir does not list: {e}"]
    globs = [(r.get("name"), g[len(COMMON_DIR_HOME):].split("/")[0]) for r in rows
             for g in derive_home_globs(r.get("home")) if g.startswith(COMMON_DIR_HOME)]
    lines, reds, own = [], [], 0
    for entry in entries:
        if entry in GIT_OWN:
            own += 1
            continue
        hit = sorted({str(n) for n, seg in globs if fnmatch.fnmatchcase(entry, seg)})
        if hit:
            lines.append(f"pocket · {entry} · {', '.join(hit)}")
        else:
            lines.append(f"pocket · {entry} · no row")
            reds.append(f"pocket {entry}: no row's `{COMMON_DIR_HOME}` home matches this entry of {common.as_posix()}; "
                        f"register its family as a witness row, or move it out of the common dir")
    lines.append(f"pocket · {len(entries)} entries of {common.as_posix()} · {own} git's own · "
                 f"{len(entries) - own - len(reds)} matched · {len(reds)} unmatched")
    return lines, reds


def check_serves_aliases(root, kit_rel: str, tool_rel: str) -> tuple[str, list[str]]:
    """S13's join: `(line, reds)`, the runlog kit's `SERVES_ALIASES`, read from its `record.py` by `ast`, held
    to the `tree_lib.KIND_ALIASES` keys whose target is `log`; `unarmed` and no red where that kit is absent."""
    from tree_lib import KIND_ALIASES
    want = sorted(a for a, t in KIND_ALIASES.items() if t == "log")
    try:
        kit = resolve_kit_dir("runlog", "record.py", pathlib.Path(root, kit_rel))
    except LookupError:
        return f"alias · {UNARMED} — no runlog kit in this tree, so its SERVES_ALIASES is joined to nothing", []
    rel = pathlib.Path(os.path.relpath(kit / "record.py", pathlib.Path(root).absolute())).as_posix()
    try:
        got = read_schema_source(root, f"{rel}:SERVES_ALIASES", tool_rel)
    except RecordKindsError as e:
        return f"alias · {rel} · red", [f"alias SERVES_ALIASES: {e}"]
    if not isinstance(got, list) or sorted(got) != want:
        return (f"alias · {rel} · red", [f"alias SERVES_ALIASES: {rel} holds {got!r}, and tree_lib's KIND_ALIASES "
                                         f"names {want!r} for `log`: the alias's two homes drift"])
    return f"alias · {rel} · SERVES_ALIASES {', '.join(got)} · held to KIND_ALIASES", []


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
    try:
        value, value_note = read_map_purpose(root)
    except RecordKindsError as e:
        return [f"{SAY}: refused · {e}"], 2
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
    joins = read_view_joins(root, kit_rel)
    reds += [f"{UNARMED} — {why}, so the view's read-by and written-by cells are no derivation" for why in joins["unarmed"]]
    if not joins["unarmed"]:
        reds += check_readers(rows, joins)
    from tree_lib import resolve_kind
    legacy, note = read_legacy_keys(root)
    legacy = {(p, resolve_kind(s)) for p, s in legacy}   # S7: a row keyed `journal` stands for `log`, bytes kept
    population = scan_legacy_records(root, rows, typed_kinds)
    fenced = scan_fence_records(root, rows, typed_kinds)
    counts, unarmed, graded_paths = [], [], {}
    for row in rows:
        name, schema = row.get("name"), row.get("schema") if isinstance(row.get("schema"), dict) else {}
        if name in fenced:   # S4: graded by `check_fence_records` below, 0 where its validator does not resolve
            counts.append(f"{name} fence {len(fenced[name]) if resolve_validator(schema.get('validator'))[0] else 0} graded")
            continue
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
    fence_reds, fence_unarmed = check_fence_records(root, rows, typed_kinds)
    reds += fence_reds
    unarmed += fence_unarmed
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
        have, want = text[span[0]:span[1]].split("\n"), render_kind_region(rows, joins).split("\n")
        if have != want:
            i = next((i for i, (a, b) in enumerate(zip(have, want)) if a != b), min(len(have), len(want)))
            first = have[i] if i < len(have) else "(the region ends)"
            reds.append(f"region gen:record-kinds: line {i + 1} of the region, {first!r}, is not what --write "
                        f"writes from the registry and a fresh read of the roles and items; run --write")
    pocket_lines, pocket_reds = check_pockets(root, rows)
    reds += pocket_reds
    alias_line, alias_reds = check_serves_aliases(root, kit_rel, tool_rel)
    reds += alias_reds
    try:
        purpose_line, purpose_reds = check_purpose(root, rows, value)
    except RecordKindsError as e:
        return [f"{SAY}: refused · {e}"], 2
    reds += purpose_reds
    lines = [f"{SAY}: {len(rows)} rows · " + " · ".join(counts)]
    lines += [f"{SAY}: {ln}" for ln in ([value_note] if value_note else []) + [purpose_line]]
    lines += [f"{SAY}: {u}" for u in unarmed]
    if note:
        lines.append(f"{SAY}: legacy · {note}")
    def render_view_names(names):
        return UNARMED if joins["unarmed"] else ", ".join(names) or "—"
    lines += [f"{SAY}: view · {r.get('name')} · read by {render_view_names(derive_read_by(r, joins))} · written by "
              f"{render_view_names(derive_written_by(r, joins))}" for r in rows]
    lines += [f"{SAY}: {ln}" for ln in pocket_lines + [alias_line]]
    lines += [f"{SAY}: RED {r}" for r in reds]
    lines.append(f"{SAY}: {'red' if reds else 'green'}")
    return lines, 1 if reds else 0


# ---------------------------------------------------------------------------------- the factory
def render_row(row: dict) -> str:
    """One `[[record-kind]]` table in the registry's column order, `readers-none` and `purpose` only where the
    row sets them, `purpose` the last line."""
    out = ["[[record-kind]]"]
    for col in COLUMNS:
        if col in ("readers-none", "purpose") and col not in row:
            continue
        v = row[col]
        if col == "purpose":
            out.append(render_purpose_line(v))
        elif col == "schema":
            parts = [f"form = {json.dumps(v['form'])}"] + ([f"source = {json.dumps(v['source'])}"] if v.get("source") else [])
            parts.append("fields = [" + ", ".join(json.dumps(f) for f in v["fields"]) + "]")
            parts += [f"validator = {json.dumps(v['validator'])}"] if v.get("validator") else []
            out.append("schema = { " + ", ".join(parts) + " }")
        else:
            out.append(f"{col} = {json.dumps(v)}")
    return "\n".join(out) + "\n"


def add_record_kind(root, a, kit_rel: str | None = None) -> int:
    """`new`: one conforming `fields` or `fence` row appended to the registry and the HYGIENE template's view
    re-rendered from it, so the gate reads the two in step; or exit 2 naming each refusal and writing
    nothing. A `fence` row takes `--validator` and no `--field`, a `fields` row the reverse; a member of
    `tree_lib.TYPED_RECORD_KINDS` gets the factory's `KINDS.<name>.required` as its `source` and the typed
    name as its `id-rule` (TOOL-dTotalRecall-25 S7)."""
    from tree_lib import TYPED_RECORD_KINDS
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
        bad.append("--home is required: a row's home is the population its check grades")
    form = a.form or "fields"
    if form not in NEW_FORMS:
        bad.append(f"--form {form!r} is not one of {', '.join(NEW_FORMS)}, the forms `new` writes")
    elif form == "fence":
        if a.field:
            bad.append("--field is refused on a `fence` row: a fence is no field, its validator grades the record")
        if not a.validator:
            bad.append("--validator <module>:<function> is required on a `fence` row, the check its records take")
        else:
            bad += [f"--{why}" for fn, why in [resolve_validator(a.validator)] if fn is None]
    else:
        if a.validator:
            bad.append("--validator is refused on a `fields` row: only a `fence` row names a validator")
        if not a.field or not all(f.strip() for f in a.field):
            bad.append("--field is required, one per **Key:** line the kind carries")
    if a.check not in legs:
        bad.append(f"--check {a.check!r} names no leg of {LEGS}")
    if not LAYER_RE.fullmatch(a.layer or ""):
        bad.append((f"--layer {a.layer!r} is no" if a.layer else "--layer is required, a")
                   + " `layer.<name>` tag: the layer of the kit whose writer writes the kind")
    if a.lifecycle not in LIFECYCLES:
        bad.append(f"--lifecycle {a.lifecycle!r} is not one of {', '.join(LIFECYCLES)}" if a.lifecycle
                   else f"--lifecycle is required, one of {', '.join(LIFECYCLES)}")
    readers, none_why = list(a.reader or []), (a.readers_none or "").strip()
    if bool(readers) == bool(none_why):
        bad.append("--reader <key>, repeated, or --readers-none <reason> is required, and only one of them: "
                   "the read keys a handoff fills from the kind, or why no role reads it")
    elif readers:
        joins = read_view_joins(root, kit_rel)
        if joins["unarmed"]:
            bad += [f"--reader cannot be graded: {UNARMED} — {why}" for why in joins["unarmed"]]
        else:
            row_probe = {"name": a.name, "readers": readers}
            bad += [r.split(": ", 1)[1].replace("reader ", "--reader ", 1) for r in check_readers([row_probe], joins)]
    purpose = a.purpose or ""
    if not purpose.strip():
        bad.append("--purpose <text> is required: one line saying what the kind is for")
    elif "\n" in purpose or "\r" in purpose:
        bad.append("--purpose holds a newline: a purpose is one line")
    elif len(purpose.encode("utf-8")) > PURPOSE_BYTES:
        bad.append(f"--purpose is {len(purpose.encode('utf-8'))} bytes, past PURPOSE_BYTES {PURPOSE_BYTES}")
    if bad:
        for b in bad + ["nothing written"]:
            print(f"{SAY}: refused · {b}")
        return 2
    typed = a.name in TYPED_RECORD_KINDS   # the two cells `check_record_kinds` and `read_bindings` hold it to
    schema = {"form": form, "fields": [] if form == "fence" else list(a.field)}
    if typed:
        schema["source"] = f"{{prefix}}/{pathlib.PurePosixPath(kit_rel).name}/build_records.py:KINDS.{a.name}.required"
    if form == "fence":
        schema["validator"] = a.validator
    row = {"name": a.name, "tag": a.tag, "layer": a.layer, "home": a.home,
           "id-rule": f"<date>-build-<unit id>-{a.name}-<n>.md" if typed else "",
           "schema": schema, "writer": a.writer, "readers": readers,
           "lifecycle": a.lifecycle, "check": a.check}
    if none_why:
        row["readers-none"] = none_why
    row["purpose"] = {"text": purpose, "source": "owner"}
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


# ---------------------------------------------------------------------------------- the purpose
def render_purpose_line(purpose: dict) -> str:
    """One `purpose = { … }` line, each value through `json.dumps` as `render_row` writes every value."""
    if "pending" in purpose:
        return f"purpose = {{ pending = {json.dumps(purpose['pending'])} }}"
    return f"purpose = {{ text = {json.dumps(purpose['text'])}, source = {json.dumps(purpose['source'])} }}"


def read_map_purpose(root) -> tuple[str, str]:
    """S3: `(value, note)` of `memory.map-purpose` at `root`'s landed revision, read once through
    `tree_lib.read_policy_value`. Where no policy kit resolves, the catalogue default `review` and a note
    saying so (§8 F8); RecordKindsError naming the key where the reader refuses."""
    from tree_lib import read_policy_value
    try:
        value = read_policy_value("memory.map-purpose", root)
    except LookupError as e:
        return MAP_PURPOSE_DEFAULT, (f"purpose · no policy kit resolves, so memory.map-purpose reads its "
                                     f"catalogue default {MAP_PURPOSE_DEFAULT}: {e}")
    except ValueError as e:
        raise RecordKindsError(str(e)) from None
    if value not in MAP_PURPOSE_VALUES:
        raise RecordKindsError(f"memory.map-purpose read {value!r}, outside {' | '.join(MAP_PURPOSE_VALUES)}")
    return value, ""


def read_open_asks(root) -> set:
    """The open asks at `root`: every ask row of a tracked `<memory root>/builds/*/BACKLOG.md`, read by
    `backlog.parse_file` under the conf's FAMILIES, less each id a status row of `backlog.TERMINAL` names.
    An ask closed only by a spec header's `closes` reads as open."""
    import backlog
    from design_lib import read_design_conf
    fams = [p.split(":", 1)[1] for p in (read_design_conf(root).get("FAMILIES") or "").split() if ":" in p]
    try:
        grammar = backlog.build_grammar(fams)
    except backlog.Problem as e:
        raise RecordKindsError(f"the conf's FAMILIES do not compile: {e}") from None
    asks, closed = set(), set()
    for rel in read_tracked(root, f"{read_memory_root(root)}/builds/*/BACKLOG.md"):
        parsed = backlog.parse_file(rel, pathlib.Path(root, rel).read_bytes().decode("utf-8", "replace"), grammar)
        asks |= {a.id for a in parsed.asks}
        closed |= {r.target for r in parsed.rows if r.verb in backlog.TERMINAL}
    return asks - closed


def read_purpose_ledger(root) -> tuple[set | None, str]:
    """`(nodes, why)`: the node keys the `purpose-pending` ledger lists, an empty set where its home is
    absent; None and why where no `[[ledger]]` table registers the population or the registrations do not
    read (§8 F7)."""
    import legacy_ledger as ll
    try:
        reg = next((r for r in ll.read_registrations(root) if r.population == PURPOSE_PENDING), None)
    except ValueError as e:
        return None, f"the ledger registrations do not read: {str(e).splitlines()[0]}"
    if reg is None:
        return None, f"no [[ledger]] table registers {PURPOSE_PENDING}"
    if not pathlib.Path(root, reg.home).is_file():
        return set(), f"{PURPOSE_PENDING}'s home {reg.home} is absent"
    rows, _bad = ll.read_ledger(root, reg)
    return {k[0] for k in rows}, ""


def check_purpose(root, rows: list[dict], value: str) -> tuple[str, list[str]]:
    """S3's pending rule: `(line, reds)`, each `pending` row graded by `memory.map-purpose`'s `value`, §4 "The
    values": under `review` an open ask's id; under `ledger` `purpose-pending` and the row's node on that
    ledger, a listed node now carrying a text red; under `derive` `none-found`; under `refuse` none."""
    def read_cell(r, key):
        p = r.get("purpose")
        return p.get(key) if isinstance(p, dict) and isinstance(p.get(key), str) else None
    pending = [(r.get("name"), read_cell(r, "pending")) for r in rows if read_cell(r, "pending") is not None]
    texts = {r.get("name") for r in rows if read_cell(r, "text")}
    reds = []
    if value == "refuse":
        reds += [f"row {n}: memory.map-purpose is refuse and its purpose is pending on {p}: give it a text"
                 for n, p in pending]
    elif value == "derive":
        reds += [f"row {n}: its purpose is pending on {p}; under derive the one pending is {NONE_FOUND}"
                 for n, p in pending if p != NONE_FOUND]
    elif value == "review" and pending:
        open_asks = read_open_asks(root)
        reds += [f"row {n}: its purpose is pending on {p}, which is no open ask of a tracked BACKLOG.md"
                 for n, p in pending if p not in open_asks]
    elif value == "ledger":
        listed, why = read_purpose_ledger(root)
        for n, p in pending:
            if p != PURPOSE_PENDING:
                reds.append(f"row {n}: its purpose is pending on {p}; under ledger the one pending is {PURPOSE_PENDING}")
            elif not listed or f"{REGISTRY_NS}:{n}" not in listed:
                reds.append(f"row {n}: its purpose is pending on {PURPOSE_PENDING} and no row of that ledger lists "
                            f"{REGISTRY_NS}:{n}{f' ({why})' if why else ''}")
        reds += [f"ledger {PURPOSE_PENDING}: its row {node} names a kind that now carries a text: drain the row"
                 for node in sorted(listed or ()) if node.startswith(f"{REGISTRY_NS}:")
                 and node[len(REGISTRY_NS) + 1:] in texts]
    return f"purpose · memory.map-purpose {value} · {len(texts)} texts · {len(pending)} pending", reds


def read_chain_rows(root, kit_rel: str) -> tuple[list[dict] | None, str, str]:
    """S4: `(rows, path, why)` of the chain registry, `<memory root>/` plus the path the playbook kit's
    `tag_index.py` holds in CHAIN_REGISTRY, read by `ast` through `read_schema_source` and never by import;
    an absent file holds no row. `rows` None and `why` said where the kit or the literal does not resolve."""
    try:
        kit = resolve_kit_dir("playbook", "tag_index.py", pathlib.Path(root, kit_rel))
    except LookupError as e:
        return None, "", f"no playbook kit in this tree: {e}"
    rel = pathlib.Path(os.path.relpath(kit / "tag_index.py", pathlib.Path(root).absolute())).as_posix()
    try:
        held = read_schema_source(root, f"{rel}:CHAIN_REGISTRY", "")
    except RecordKindsError as e:
        return None, "", str(e)
    if not isinstance(held, str) or not held.strip():
        return None, "", f"{rel}'s CHAIN_REGISTRY is no path"
    chain_rel = f"{read_memory_root(root)}/{held.strip().strip('/')}"
    path = pathlib.Path(root, chain_rel)
    if not path.is_file():
        return [], chain_rel, ""
    try:
        data = tomllib.loads(path.read_bytes().decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as e:
        raise RecordKindsError(f"the chain registry {chain_rel} does not parse: {e}") from None
    builds = data.get("build") or []
    return [r for r in builds if isinstance(r, dict) and isinstance(r.get("slug"), str) and r["slug"]], chain_rel, ""


def derive_purpose_cut(text: str) -> str:
    """A found text as a purpose: its whitespace folded, cut at the last word boundary before
    `PURPOSE_BYTES`, its trailing punctuation dropped and an unclosed code span cut before its tick."""
    text = " ".join(text.split())
    if len(text.encode("utf-8")) > PURPOSE_BYTES:
        head = text.encode("utf-8")[:PURPOSE_BYTES + 1].decode("utf-8", "ignore")
        text = head[:head.rfind(" ")] if " " in head else ""
    text = text.rstrip(" ,;:—–-")
    if text.count("`") % 2:
        text = text[:text.rfind("`")].rstrip(" ,;:—–-")
    return text


def check_repeats_name(text: str, name: str) -> bool:
    """Whether `text` only repeats `name`, `-` read as a space, case, ticks and punctuation aside."""
    def derive_words(s):
        return re.sub(r"[`*_.,;:'\"()]", "", s).replace("-", " ").lower().split()
    return derive_words(text) == derive_words(name)


def derive_purpose(name: str, candidates) -> tuple[tuple[str, str] | None, str]:
    """§4's derivation order: `((text, source), "")` from the first of `candidates`, each `(text or None,
    source, what was found)` in order, whose text survives `derive_purpose_cut` and does not only repeat
    `name`; else `(None, what was found)`, each candidate's finding joined."""
    found = []
    for text, source, what in candidates:
        cut = derive_purpose_cut(text) if text is not None else ""
        if text is None:
            found.append(what)
        elif not cut or check_repeats_name(cut, name):
            found.append(f"{what} only repeats its name")
        else:
            return (cut, source), ""
    return None, "; ".join(found)


def read_readme_h1(root, rel: str, slug: str) -> tuple[str | None, str, str]:
    """§4 step 1 for a chain build: `(text, "<path>:<line>", what)` of the first `# ` line outside a fence of
    its tracked README, after its slug and the dash; `(None, "", what)` where there is none."""
    from tree_lib import unfenced_lines
    path = pathlib.Path(root, rel)
    if not run_git(root, "ls-files", "--", f":(literal){rel}").stdout.strip() or not path.is_file():
        return None, "", f"no tracked README at {rel}"
    for n, line in unfenced_lines(path.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")):
        if line is not None and line.startswith("# "):
            text = line[2:].strip()
            if text.startswith(slug):
                text = text[len(slug):].lstrip(" —–-:")
            return text, f"{rel}:{n}", f"the H1 at {rel}:{n}"
    return None, "", f"no H1 outside a fence in {rel}"


def read_from_table(root, from_rel: str) -> dict:
    """§4 step 2's source: `{kind key: (last cell, "<path>:<line>")}` of every Markdown table row outside a
    fence of the `--from` record, its first cell, `-` read as a space and through `tree_lib.resolve_kind`,
    the key; the first row naming a kind wins."""
    from tree_lib import resolve_kind, unfenced_lines
    out = {}
    text = pathlib.Path(root, from_rel).read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")
    for n, line in unfenced_lines(text):
        if line is None or not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
        if len(cells) < 2 or all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        out.setdefault(" ".join(resolve_kind(cells[0].replace("-", " ").strip()).split()),
                       (cells[-1].replace("\\|", "|"), f"{from_rel}:{n}"))
    return out


def scan_purpose_nodes(root, rows: list[dict], chain_rows, from_rel: str | None) -> list[dict]:
    """S4's two populations, each node tried in §4's derivation order: the registry's rows with no `text`
    and the chain registry's rows with no `purpose`. -> `[{"node", "ns", "name", "derived": (text, source)
    or None, "found"}]`, the registry's first."""
    table = read_from_table(root, from_rel) if from_rel else {}
    nodes = []
    for r in rows:
        p = r.get("purpose")
        if isinstance(p, dict) and isinstance(p.get("text"), str) and p["text"].strip():
            continue
        name = str(r.get("name"))
        hit = table.get(" ".join(name.replace("-", " ").split()))
        cands = [(None, "", "no H1: a record kind lives in the shared registry"),
                 (hit[0], hit[1], f"the --from row at {hit[1]}") if hit else
                 (None, "", "no row of the --from table names it" if from_rel else "no --from record given")]
        derived, found = derive_purpose(name, cands)
        nodes.append({"node": f"{REGISTRY_NS}:{name}", "ns": REGISTRY_NS, "name": name, "derived": derived,
                      "found": found})
    memory_root = read_memory_root(root)
    for r in chain_rows or []:
        if isinstance(r.get("purpose"), str) and r["purpose"].strip():
            continue
        slug = r["slug"]
        derived, found = derive_purpose(slug, [read_readme_h1(root, f"{memory_root}/builds/{slug}/README.md", slug)])
        nodes.append({"node": f"{CHAIN_NS}:{slug}", "ns": CHAIN_NS, "name": slug, "derived": derived, "found": found})
    return nodes


def render_ask_draft(ns: str, nodes: list[dict]) -> str:
    """One namespace's ask draft, every `none` node of it listed with what was found."""
    return f"ask {ns} · " + "; ".join(f"{n['node']} ({n['found']})" for n in nodes)


def write_purpose_line(text: str, table: str, key: str, value: str, line: str) -> str:
    """`text` with `line` as the `purpose` of the `[[<table>]]` row whose `<key>` is `value`: that row's own
    `purpose =` line replaced, else one line inserted after its last key line, so every comment and every
    other row keeps its bytes. RecordKindsError where no such row is found."""
    lines = text.split("\n")
    starts = [i for i, ln in enumerate(lines) if ln.strip() == f"[[{table}]]"]
    want = f"{key} = {json.dumps(value)}"
    for k, s in enumerate(starts):
        body = range(s + 1, starts[k + 1] if k + 1 < len(starts) else len(lines))
        if not any(lines[i].strip() == want for i in body):
            continue
        eol = "\r" if lines[s].endswith("\r") else ""
        at = next((i for i in body if re.match(r"purpose\s*=", lines[i])), None)
        if at is not None:
            lines[at] = line + eol
        else:
            lines.insert(max(i for i in body if re.match(r"[A-Za-z0-9_-]+\s*=", lines[i])) + 1, line + eol)
        return "\n".join(lines)
    raise RecordKindsError(f"no [[{table}]] row holds {want}, so its purpose has no line to take")


def write_purposes(root, kit_rel: str, nodes: list[dict], value: str, ask: str | None, chain_rel: str) -> int:
    """S5 and S6: each derived purpose written into its node's own field, the registry row's `purpose` table
    and the chain row's `purpose` string, and each `none` registry row's pending by `value`: `--ask`'s id
    under `review`, `purpose-pending` under `ledger`, `none-found` under `derive`, nothing under `refuse`. A
    `none` chain row is never written. Exit 2 writing nothing on an `--ask` that is no open ask, an `--ask`
    under another value, or `ledger` with no registration of its population."""
    none_rows = [n for n in nodes if n["derived"] is None and n["ns"] == REGISTRY_NS]
    pending, refusal = None, ""
    if ask and value != "review":
        refusal = f"--ask {ask} files an owner ask, which memory.map-purpose {value} does not take"
    elif ask and ask not in read_open_asks(root):
        refusal = f"--ask {ask} is no open ask of a tracked BACKLOG.md"
    elif value == "review":
        pending = ask
    elif value == "ledger":
        listed, why = read_purpose_ledger(root)
        refusal = f"{why}: register {PURPOSE_PENDING} before a ledger write" if listed is None else ""
        pending = PURPOSE_PENDING
    elif value == "derive":
        pending = NONE_FOUND
    if refusal:
        print(f"{SAY}: refused · {refusal}; nothing written")
        return 2
    reg_path, chain_path = pathlib.Path(root, kit_rel, REGISTRY), pathlib.Path(root, chain_rel or ".")
    reg_text = reg_path.read_bytes().decode("utf-8")
    chain_text = chain_path.read_bytes().decode("utf-8") if chain_rel and chain_path.is_file() else ""
    reg_want, chain_want = {}, {}
    for n in nodes:
        if n["derived"] and n["ns"] == REGISTRY_NS:
            reg_want[n["name"]] = {"text": n["derived"][0], "source": n["derived"][1]}
        elif n["derived"]:
            chain_want[n["name"]] = n["derived"][0]
    for n in none_rows if pending else []:
        reg_want[n["name"]] = {"pending": pending}
    for name, purpose in reg_want.items():
        reg_text = write_purpose_line(reg_text, "record-kind", "name", name, render_purpose_line(purpose))
    for slug, text in chain_want.items():
        chain_text = write_purpose_line(chain_text, "build", "slug", slug, f"purpose = {json.dumps(text)}")
    try:
        got = {r.get("name"): r.get("purpose") for r in tomllib.loads(reg_text).get("record-kind", [])}
        got_chain = {r.get("slug"): r.get("purpose") for r in tomllib.loads(chain_text).get("build", [])}
    except tomllib.TOMLDecodeError as e:
        raise RecordKindsError(f"the purpose write would leave a file that does not parse: {e}") from None
    if any(got.get(k) != v for k, v in reg_want.items()) or any(got_chain.get(k) != v for k, v in chain_want.items()):
        raise RecordKindsError("the purpose write did not read back as written; nothing written")
    if reg_want:
        reg_path.write_bytes(reg_text.encode("utf-8"))
    if chain_want:
        chain_path.write_bytes(chain_text.encode("utf-8"))
    print(f"{SAY}: purpose · wrote {len(reg_want)} registry rows, {sum(1 for v in reg_want.values() if 'pending' in v)} "
          f"of them pending, and {len(chain_want)} chain rows")
    if reg_want and pathlib.Path(root, kit_rel, TEMPLATE).is_file():
        return write_kind_region(root, kit_rel)   # the view renders the column, so it moves with the rows
    return 0


def run_purpose_review(root, from_rel: str | None, write: bool, ask: str | None, kit_rel: str | None = None) -> int:
    """`--purpose-review [--from <path>] [--write [--ask <id>]]`: one `derived <node> · <text> · <source>` or
    `none <node> · <what was found>` line per node of S4's populations, one `ask <namespace> · …` draft per
    namespace holding a `none` node (none under `derive`), then the write where `--write` asks for it."""
    kit_rel = kit_rel or derive_kit_rel()
    rows = read_record_kinds(root, kit_rel)
    if rows is None:
        print(f"{SAY}: refused · no registry {kit_rel}/{REGISTRY} to review")
        return 2
    if from_rel is not None:
        from_rel = from_rel.replace("\\", "/")
        if not run_git(root, "ls-files", "--", f":(literal){from_rel}").stdout.strip():
            print(f"{SAY}: refused · --from {from_rel} is no tracked file")
            return 2
    value, note = read_map_purpose(root)
    print(f"{SAY}: purpose · memory.map-purpose {value}" + (f" · {note}" if note else ""))
    chain_rows, chain_rel, why = read_chain_rows(root, kit_rel)
    if chain_rows is None:
        print(f"unarmed chain · {why}")
    nodes = scan_purpose_nodes(root, rows, chain_rows, from_rel)
    for n in nodes:
        print(f"derived {n['node']} · {n['derived'][0]} · {n['derived'][1]}" if n["derived"]
              else f"none {n['node']} · {n['found']}")
    for ns in (REGISTRY_NS, CHAIN_NS):
        none = [n for n in nodes if n["ns"] == ns and n["derived"] is None]
        if none and value != "derive":
            print(render_ask_draft(ns, none))
    return write_purposes(root, kit_rel, nodes, value, ask, chain_rel) if write else 0


def print_purpose_pending(root, kit_rel: str | None = None) -> int:
    """`--print-purpose-pending`: the `purpose-pending` population for `legacy_ledger.py seed`, `<node> TAB 1`
    per registry row pending on it and per chain row with no purpose."""
    kit_rel = kit_rel or derive_kit_rel()
    for r in read_record_kinds(root, kit_rel) or []:
        p = r.get("purpose")
        if isinstance(p, dict) and p.get("pending") == PURPOSE_PENDING:
            print(f"{REGISTRY_NS}:{r.get('name')}\t1")
    chain_rows, _rel, why = read_chain_rows(root, kit_rel)
    if chain_rows is None:
        print(f"{SAY}: unarmed chain · {why}", file=sys.stderr)
    for r in chain_rows or []:
        if not (isinstance(r.get("purpose"), str) and r["purpose"].strip()):
            print(f"{CHAIN_NS}:{r['slug']}\t1")
    return 0


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
FIXTURE_TYPED = ("deviation", "stream-plan")
FIXTURE_BUILD = "bFix"
PLANTS = ("writer-missing", "check-unknown", "source-drift", "factory-kind-unrowed", "field-missing",
          "field-missing-legacy", "region-edited", "gap-unresolved", "lifecycle-missing", "role-reads-moved",
          "item-inputs", "roles-unresolved", "pocket-stray", "pocket-registered", "new-row", "pipe-cell",
          "alias-drift", "new-purpose", "review", "review-write", "purpose-missing", "purpose-long",
          "pending-closed", "value-refuse", "value-derive", "value-ledger", "value-ledger-unregistered",
          "value-refused", "stream-unordered", "stream-empty", "stream-order-text", "stream-unit-twice",
          "stream-fence-missing", "stream-validator-missing")
#: TOOL-dTotalRecall-25's fixture: the well-formed plan of two streams, and each stream plant's edit of its fence
FIXTURE_PLAN = f"memory/builds/{FIXTURE_BUILD}/build/2026-01-05-build-TOOL-{FIXTURE_BUILD}-1-stream-plan-1.md"
FIXTURE_FENCE = ('```toml\n[[stream]]\nname = "tooling"\n'
                 f'units = [{{ id = "TOOL-{FIXTURE_BUILD}-1", order = 1 }}, {{ id = "TOOL-{FIXTURE_BUILD}-2", order = 2 }}]\n\n'
                 f'[[stream]]\nname = "memory"\nunits = [{{ id = "TOOL-{FIXTURE_BUILD}-3", order = 1 }}]\n```\n')
FIXTURE_STREAM_EDITS = {"stream-unordered": (f'{{ id = "TOOL-{FIXTURE_BUILD}-2", order = 2 }}', f'{{ id = "TOOL-{FIXTURE_BUILD}-2" }}'),
                        "stream-empty": (f'[{{ id = "TOOL-{FIXTURE_BUILD}-3", order = 1 }}]', "[]"),
                        "stream-order-text": ("order = 2 }", 'order = "2" }'),
                        "stream-unit-twice": (f'"TOOL-{FIXTURE_BUILD}-3"', f'"TOOL-{FIXTURE_BUILD}-2"'),
                        "stream-fence-missing": (FIXTURE_FENCE, "")}
#: TOOL-dTotalRecall-16's fixture: its open and closed asks, the plants whose registry holds the review's three
#: purposeless rows, each plant's `memory.map-purpose` value, the `--from` record and the review's two chain builds.
FIXTURE_OPEN_ASK, FIXTURE_CLOSED_ASK = f"TOOL-{FIXTURE_BUILD}-101", f"TOOL-{FIXTURE_BUILD}-102"
REVIEW_PLANTS = ("review", "review-write", "value-derive", "value-ledger", "value-ledger-unregistered")
FIXTURE_VALUES = {"value-refuse": "refuse", "value-derive": "derive", "value-ledger": "ledger",
                  "value-ledger-unregistered": "ledger", "value-refused": "unbounded"}
FIXTURE_FROM = f"memory/builds/{FIXTURE_BUILD}/build/2026-01-04-build-TOOL-{FIXTURE_BUILD}-1-kinds.md"
FIXTURE_CHAIN = ("bOne", "bTwo")
#: The fixture's roles, `slot: (reads, writes)`, and its loop items, `(tag, input)`: the first input a typed
#: record reference, the second the prose a kind's name must never be matched in (S2, §8 F5).
FIXTURE_ROLES = {"gov-builder": ("input:spec", "product"), "gov-diff-reviewer": ("input:diff", "none"),
                 "gov-spec-writer": ("input:spec", "spec")}
FIXTURE_ITEMS = (("item.build.typed", "layer.memory:record-kind.log@1"),
                 ("item.build.prose", "layer.memory:plan record"))
FIXTURE_NEW = ["new", "widget", "--tag", "record.widget", "--writer", "hand", "--check", "memory hygiene", "--field",
               "Serves", "--home", "memory/builds/*/build/*.md", "--layer", "layer.memory", "--lifecycle",
               "append-only", "--purpose", "a planted kind", "--reader", "input:spec"]


def build_fixture(tmp, plant: str | None = None):
    """A throwaway repository at `tmp` laid out as this kit's own tree: a five-row registry, a two-leg
    manifest, a govkit registry holding the legacy ledger's table, its home, a gap register and records,
    one a `…-deviation-notes.md` holding no deviation field, one a stream plan of two streams, its `fence`
    row typed beside `deviation`, a roles kit of three role files, a loop kit
    whose definition holds the items `item-inputs` plants, a runlog kit's alias literal, a BACKLOG.md of
    one open and one closed ask, a two-row chain registry and the playbook kit's literal naming it, the
    purpose review's `--from` record, `plant` applied, committed on `main` (the policy reader's landed
    branch), and its view rendered from the registry and a read of those kits before the commit.
    -> the typed kind list its check reads."""
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

    def derive_sibling_rel(kit, name):   # spelled in parts: the install-prefix ban reads a kit path
        return "/".join(x for x in (tool_rel, kit, name) if x)

    write_fixture_file(".memory-tree.conf", 'MEMORY_ROOT="memory"\nFAMILIES="tooling:TOOL"\n')
    write_fixture_file(f"{tool_rel}/{LEGS}" if tool_rel else LEGS, json.dumps([{"name": "memory hygiene"}, {"name": SAY}], indent=2) + "\n")
    write_fixture_file(f"{kit_rel}/build_records.py", "LEVELS = ('a', 'b')\nKINDS = {\n    'deviation': {\n        'required': ("
        + ", ".join(json.dumps(f) for f in dev + (["Extra"] if plant == "source-drift" else [])) + "),\n"
        "        'closed': (('Risk', LEVELS),),\n    },\n    'stream-plan': {'required': (), 'closed': ()},\n}\n")
    rows = [
        {"name": "spec", "tag": "record.spec", "layer": "layer.memory", "home": "memory/builds/*/spec/*.md",
         "id-rule": "<date>-spec-<unit id>.md", "schema": {"form": "header", "fields": []}, "writer": "hand",
         "readers": ["input:spec"], "lifecycle": "current-state", "check": "memory hygiene"},
        {"name": "log", "tag": "record.log", "layer": "layer.memory", "home": "memory/builds/*/prompts/*.md",
         "id-rule": "", "schema": {"form": "fields", "fields": ["Serves"]}, "writer": "hand", "readers": [],
         "readers-none": "no fixture role reads a brief", "lifecycle": "append-only", "check": "memory hygiene"},
        {"name": "research", "tag": "record.research", "layer": "layer.memory", "home": "memory/builds/*/build/*.md",
         "id-rule": "", "schema": {"form": "fields", "fields": ["Serves"]},
         "writer": "a | b" if plant == "pipe-cell" else "hand", "readers": ["input:diff"], "lifecycle": "append-only",
         "check": "no such leg" if plant == "check-unknown" else "memory hygiene"},
        {"name": "deviation", "tag": "record.deviation", "layer": "layer.memory",
         "home": "memory/builds/*/build/*-build-*-deviation-*.md", "id-rule": "<date>-build-<unit id>-deviation-<n>.md",
         "schema": {"form": "fields", "source": f"{prefix}/{kit_rel[len(tool_rel) + 1:] if tool_rel else kit_rel}"
                    f"/build_records.py:KINDS.deviation.required", "fields": dev},
         "writer": "hand", "readers": [], "readers-none": "a departure is read by the deviation join, no role",
         "lifecycle": "frozen", "check": "memory hygiene"},
    ]
    rows.insert(-1, {   # before the deviation row, which the plants above name as the last
        "name": "stream-plan", "tag": "record.stream-plan", "layer": "layer.memory",
        "home": "memory/builds/*/build/*-stream-plan-*.md", "id-rule": "<date>-build-<unit id>-stream-plan-<n>.md",
        "schema": {"form": "fence", "source": rows[-1]["schema"]["source"].replace(".deviation.", ".stream-plan."),
                   "fields": [], "validator": "record_kinds:" + ("no_such_check" if plant == "stream-validator-missing"
                                                                 else check_stream_plan.__name__)},
        "writer": "hand", "readers": [], "readers-none": "no fixture role reads a plan", "lifecycle": "current-state",
        "check": SAY})
    for row in rows:
        row["purpose"] = {"text": f"the fixture's {row['name']} record", "source": "owner"}
    if plant == "purpose-missing":
        del rows[-1]["purpose"]
    elif plant == "purpose-long":   # one byte past the cap
        rows[-1]["purpose"] = {"text": "x" * (PURPOSE_BYTES + 1), "source": "owner"}
    elif plant == "pending-closed":
        rows[-1]["purpose"] = {"pending": FIXTURE_CLOSED_ASK}
    elif plant == "value-refuse":   # an open ask's pending, which refuse admits no more than any other
        rows[1]["purpose"] = {"pending": FIXTURE_OPEN_ASK}
    if plant in REVIEW_PLANTS:   # S4's population: alpha the --from table names, beta named nowhere, gamma's
        for name in ("alpha", "beta", "gamma"):   # cell only repeating its name
            rows.append({"name": name, "tag": f"record.{name}", "layer": "layer.memory",
                         "home": "memory/builds/*/spec/*.md", "id-rule": "", "schema": {"form": "header", "fields": []},
                         "writer": "hand", "readers": [], "readers-none": "a fixture kind no role reads",
                         "lifecycle": "current-state", "check": "memory hygiene"})
    if plant == "pocket-registered":   # the stray's family registered as a witness row
        rows.append({"name": "stray", "tag": "record.stray", "layer": "layer.memory",
                     "home": [f"{COMMON_DIR_HOME}stray/*"], "id-rule": "", "schema": {"form": "rows", "fields": []},
                     "writer": "hand", "readers": [], "readers-none": "a cache no role reads", "lifecycle": "out",
                     "check": SAY, "purpose": {"text": "the fixture's pocket", "source": "owner"}})
    registry = "\n".join(render_row(r) for r in rows)
    if plant == "writer-missing":   # the deviation row, the last, loses its writer
        head, _, tail = registry.partition('name = "deviation"\n')
        registry = head + 'name = "deviation"\n' + tail.replace('writer = "hand"\n', "", 1)
    if plant == "lifecycle-missing":   # the deviation row loses its lifecycle, now a required column
        registry = registry.replace('lifecycle = "frozen"\n', "", 1)
    write_fixture_file(f"{kit_rel}/{REGISTRY}", registry)
    if plant != "roles-unresolved":
        write_fixture_file(derive_sibling_rel("roles", "roles_lib.py"), "# the fixture's roles kit: its role files\n")
        for slot, (reads, writes) in FIXTURE_ROLES.items():
            write_fixture_file(derive_sibling_rel("roles", f"agents/{slot}.agent.md"),
                               f"---\nname: {slot}\nreads: {reads}\nwrites: {writes}\n---\n\nThe fixture role.\n")
    items = "".join(f'[[item]]\ntag = "{tag}"\ninputs = ["{text}"]\nreturns = "a fixture return"\n\n'
                    for tag, text in FIXTURE_ITEMS) if plant == "item-inputs" else ""
    write_fixture_file(derive_sibling_rel("loop", "loop_lib.py"), "# the fixture's loop kit: its definition\n")
    write_fixture_file(derive_sibling_rel("loop", "loop.toml"), "# the fixture's definition\n\n" + items)
    write_fixture_file(derive_sibling_rel("runlog", "record.py"), 'SERVES_KIND = "log"\nSERVES_ALIASES = '
                       + ("()" if plant == "alias-drift" else '("journal",)') + "\n")
    sibling = "/".join(("govkit", "registry.toml"))   # spelled in parts: the install-prefix ban reads a kit path
    write_fixture_file(f"{tool_rel}/{sibling}" if tool_rel else sibling,
        f'[[ledger]]\npopulation = "{LEGACY}"\nleg = "{SAY}"\nseed = ["python", "{prefix}/{kit_rel[len(tool_rel) + 1:] if tool_rel else kit_rel}/record_kinds.py", "--seed-legacy"]\n'
        'key = "record"\nfields = ["path", "section"]\ndrain = "key"\ndirection = "shrink-only"\n'
        f'home = "memory/project/{LEGACY}.txt"\n' + (   # value-ledger registers the population, its seed this file
            f'\n[[ledger]]\npopulation = "{PURPOSE_PENDING}"\nleg = "{SAY}"\nseed = ["python", '
            f'{json.dumps((KIT / "record_kinds.py").as_posix())}, "--print-purpose-pending"]\nkey = "key"\n'
            f'fields = ["node"]\ndrain = "key"\ndirection = "shrink-only"\nhome = "memory/project/{PURPOSE_PENDING}.txt"\n'
            if plant == "value-ledger" else ""))
    write_fixture_file(f"memory/builds/{FIXTURE_BUILD}/BACKLOG.md", f"# {FIXTURE_BUILD} — asks\n\n## Asks\n\n"
                       f"- {FIXTURE_OPEN_ASK} · filed 2026-01-01 · the fixture's open purpose ask\n"
                       f"- {FIXTURE_CLOSED_ASK} · filed 2026-01-01 · the fixture's closed ask\n\n## Dispositions\n\n"
                       f"- CLOSED · {FIXTURE_CLOSED_ASK} · by {unit} · answered\n")
    write_fixture_file(derive_sibling_rel("playbook", "tag_index.py"), 'CHAIN_REGISTRY = "project/chain.toml"\n')
    write_fixture_file("memory/project/chain.toml", "# the fixture's chain registry\n\n"
                       + "\n".join(f'[[build]]\nslug = "{s}"\n' for s in FIXTURE_CHAIN))
    write_fixture_file(f"memory/builds/{FIXTURE_CHAIN[0]}/README.md",
                       f"# {FIXTURE_CHAIN[0]} — the fixture's first chain build\n\nIts README.\n")
    write_fixture_file(FIXTURE_FROM, f"**Serves:** research {unit}\n\n| Kind | Owner | What names it |\n|---|---|---|\n"
                       f"| alpha | {FIXTURE_BUILD} | the fixture's first kind, which the review derives |\n"
                       f"| gamma | {FIXTURE_BUILD} | gamma |\n")
    if plant in FIXTURE_VALUES:
        write_fixture_file(".governance/policy.toml", f'[memory]\nmap-purpose = "{FIXTURE_VALUES[plant]}"\n')
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
    write_fixture_file(f"memory/builds/{FIXTURE_BUILD}/prompts/2026-01-01-prompt-{unit}-brief.md",
                       f"**Serves:** log {unit}\n\nthe fixture's brief\n")
    fence = FIXTURE_FENCE.replace(*FIXTURE_STREAM_EDITS[plant], 1) if plant in FIXTURE_STREAM_EDITS else FIXTURE_FENCE
    write_fixture_file(FIXTURE_PLAN, f"**Serves:** stream-plan {unit} TOOL-{FIXTURE_BUILD}-2 TOOL-{FIXTURE_BUILD}-3\n\n"
                       f"# {unit} stream-plan 1 — the fixture's plan\n\n{fence}")
    region = render_kind_region(tomllib.loads(registry)["record-kind"], read_view_joins(tmp, kit_rel))
    if plant == "region-edited":
        region = region.replace("| Kind |", "| Kinds |", 1)
    write_fixture_file(f"{kit_rel}/{TEMPLATE}", "# fixture hygiene\n\n## Record kinds — the registry's view\n\n" + region + "\n")
    if plant == "role-reads-moved":   # a role's reads move after its view was rendered
        write_fixture_file(derive_sibling_rel("roles", "agents/gov-builder.agent.md"),
                           "---\nname: gov-builder\nreads: input:spec, input:diff\nwrites: product\n---\n\nThe fixture role.\n")
    hooks = tmp / ".nohooks"
    hooks.mkdir(exist_ok=True)
    for args in (("init", "-q", "-b", "main"), ("add", "-A", "--", "."),   # main: the policy reader's landed branch
                 ("-c", "user.name=record-kinds", "-c", "user.email=record-kinds@fixture.invalid", "-c",
                  "commit.gpgsign=false", "-c", f"core.hooksPath={hooks.as_posix()}", "commit", "-q", "--no-verify",
                  "-m", f"record-kinds fixture: {plant or 'green'}")):
        p = run_git(tmp, *args)
        if p.returncode != 0:
            raise RecordKindsError(f"the fixture's git {args[0]} refused: {p.stderr.strip()}")
    if plant in ("pocket-stray", "pocket-registered"):   # a pocket in the common dir, the worktree's own here
        common_git_dir(tmp).joinpath("stray").mkdir()
    return FIXTURE_TYPED + (("exception",) if plant == "factory-kind-unrowed" else ())


def run_fixture(plant: str | None) -> tuple[list[str], int]:
    """`--fixture [--plant <case>]`: the fixture built under the system temp directory, `--check` run there;
    `new-row` and `new-purpose` run `new` with every flag first, and `pipe-cell` prints the region line of the
    piped row. `review` prints the purpose review alone; `review-write` writes it under the closed ask, then
    the open one, and prints each reviewed node's purpose; the `value-*` writes print theirs, and
    `value-ledger` runs the population's seed before the check."""
    if plant is not None and plant not in PLANTS:
        return [f"{SAY}: refused · no plant {plant!r}: the plants are {', '.join(PLANTS)}"], 2
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="rk-"))
    try:
        typed = build_fixture(tmp, plant)
        head = [f"{SAY}: fixture {plant or 'green'}"]
        if plant in ("new-row", "new-purpose"):
            rc = main(FIXTURE_NEW, root=tmp)
            if rc:
                return head + [f"{SAY}: fixture {plant} · new exited {rc}"], rc
        if plant == "new-purpose":
            row = next((r for r in read_record_kinds(tmp) or [] if r.get("name") == "widget"), {})
            head.append(f"{SAY}: fixture new-purpose · widget · source {(row.get('purpose') or {}).get('source')}")
        review = ["--purpose-review", "--from", FIXTURE_FROM]
        if plant == "review":
            return run_captured(review, tmp, head)
        if plant == "review-write":   # the closed ask first, refused with the bytes kept, then the open one
            reg = pathlib.Path(tmp, derive_kit_rel(), REGISTRY)
            before = reg.read_bytes()
            _out, rc = run_captured(review + ["--write", "--ask", FIXTURE_CLOSED_ASK], tmp, [])
            head.append(f"{SAY}: fixture review-write · closed ask · exit {rc} · registry "
                        f"{'unchanged' if reg.read_bytes() == before else 'changed'}")
            head, rc = run_captured(review + ["--write", "--ask", FIXTURE_OPEN_ASK], tmp, head)
            if rc:
                return head, rc
            head += [f"{SAY}: fixture review-write · {REGISTRY_NS}:{r.get('name')} · {json.dumps(r.get('purpose'))}"
                     for r in read_record_kinds(tmp) or [] if r.get("name") in ("alpha", "beta", "gamma")]
            head += [f"{SAY}: fixture review-write · {CHAIN_NS}:{r['slug']} · {json.dumps(r.get('purpose'))}"
                     for r in (read_chain_rows(tmp, derive_kit_rel())[0] or [])]
        if plant in ("value-derive", "value-ledger", "value-ledger-unregistered"):
            head, rc = run_captured(review + ["--write"], tmp, head)
            if rc:
                return head, rc
            head += [f"{SAY}: fixture {plant} · {REGISTRY_NS}:{r.get('name')} · {json.dumps(r.get('purpose'))}"
                     for r in read_record_kinds(tmp) or [] if r.get("name") in ("alpha", "beta", "gamma")]
        if plant == "value-ledger":   # the registration's seed, `--print-purpose-pending`, run as `seed` runs it
            import legacy_ledger as ll
            reg = next(r for r in ll.read_registrations(tmp) if r.population == PURPOSE_PENDING)
            line, _ok = ll.seed_population(tmp, reg, "0" * 40)
            head.append(f"{SAY}: fixture value-ledger · seed · {line}")
        lines, rc = check_record_kinds(tmp, typed)
        if plant == "pipe-cell":
            text = pathlib.Path(tmp, derive_kit_rel(), TEMPLATE).read_bytes().decode("utf-8")
            head += [f"{SAY}: fixture pipe-cell · region · {ln}" for ln in text.split("\n") if ln.startswith("| `research` |")]
        return head + lines, rc
    finally:
        remove_tree(tmp)


def run_captured(argv: list[str], root, head: list[str]) -> tuple[list[str], int]:
    """`(head + the lines main printed, its exit)` of one verb run at the fixture's `root`."""
    import contextlib
    import io
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        rc = main(argv, root=root)
    return head + out.getvalue().splitlines(), rc


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
    """Every plant red naming its subject, the green fixture and the green plants green with what each shows,
    `new`'s round trip and its refusals, and `--write` restoring an edited region."""
    want = {"writer-missing": ("row deviation", "`writer`"), "check-unknown": ("row research", "no such leg"),
            "source-drift": ("row deviation", "Extra"), "factory-kind-unrowed": ("typed kind exception",),
            "field-missing": ("deviation-2.md", "**Caused-by:**"), "region-edited": ("region gen:record-kinds",),
            "gap-unresolved": ("gap-mem-99",), "lifecycle-missing": ("row deviation", "`lifecycle`"),
            "role-reads-moved": ("region gen:record-kinds",), "roles-unresolved": (UNARMED, "roles kit"),
            "pocket-stray": ("pocket stray",), "alias-drift": ("SERVES_ALIASES",),
            "purpose-missing": ("row deviation", "`purpose`"), "purpose-long": ("row deviation", "past PURPOSE_BYTES"),
            "pending-closed": ("row deviation", FIXTURE_CLOSED_ASK), "value-refuse": ("row log", "refuse"),
            "stream-unordered": (FIXTURE_PLAN, "stream tooling", f"unit TOOL-{FIXTURE_BUILD}-2", "no order"),
            "stream-empty": (FIXTURE_PLAN, "stream memory", "no units"),
            "stream-order-text": (FIXTURE_PLAN, f"unit TOOL-{FIXTURE_BUILD}-2", "order '2'"),
            "stream-unit-twice": (FIXTURE_PLAN, f"unit TOOL-{FIXTURE_BUILD}-2 is named in"),
            "stream-fence-missing": (FIXTURE_PLAN, "fence"),
            "stream-validator-missing": ("row stream-plan", "record_kinds:no_such_check")}
    refusals = {"value-ledger-unregistered": PURPOSE_PENDING, "value-refused": "memory.map-purpose"}

    def test_pipe_cell(lines):
        row = next((ln.split(" · region · ", 1)[1] for ln in lines if " · region · " in ln), "")
        return "a \\| b" in row and len(re.split(r"(?<!\\)\|", row)) == 10   # eight cells between nine pipes

    def test_review(lines):   # AC3: the order, a source on every derived line, one draft per namespace
        asks = [ln for ln in lines if ln.startswith("ask ")]
        return (any(ln.startswith(f"derived {REGISTRY_NS}:alpha · ") and f" · {FIXTURE_FROM}:" in ln for ln in lines)
                and any(ln.startswith(f"derived {CHAIN_NS}:bOne · ") and ln.endswith("/bOne/README.md:1") for ln in lines)
                and all(any(ln.startswith(f"none {n} · ") for ln in lines)
                        for n in (f"{REGISTRY_NS}:beta", f"{REGISTRY_NS}:gamma", f"{CHAIN_NS}:bTwo"))
                and len(asks) == 2 and any(ln.startswith(f"ask {REGISTRY_NS} · ") and "beta" in ln and "gamma" in ln
                                           for ln in asks))

    def test_review_write(lines):   # AC4
        return all(any(s in ln for ln in lines) for s in (
            "closed ask · exit 2 · registry unchanged", f'{REGISTRY_NS}:alpha · {{"text": ',
            f'{REGISTRY_NS}:beta · {{"pending": "{FIXTURE_OPEN_ASK}"}}', f'{REGISTRY_NS}:gamma · {{"pending": "{FIXTURE_OPEN_ASK}"}}',
            f"{CHAIN_NS}:bOne · \"the fixture's first chain build\"", f"{CHAIN_NS}:bTwo · null"))

    def test_value_pending(pending, draft):   # AC6: the write's pending, and whether a draft printed
        return lambda ls: (all(any(f'{REGISTRY_NS}:{n} · {{"pending": "{pending}"}}' in ln for ln in ls)
                               for n in ("beta", "gamma")) and draft == any(ln.startswith("ask ") for ln in ls))

    shows = {"item-inputs": lambda ls: any(ln.startswith(f"{SAY}: view · log · read by") and "item.build.typed" in ln
                                           for ln in ls) and not any(" view · " in ln and "item.build.prose" in ln
                                                                      for ln in ls),
             "pocket-registered": lambda ls: f"{SAY}: pocket · stray · stray" in ls,
             "new-row": lambda ls: any(" rows · " in ln and "widget 3 graded" in ln for ln in ls),
             "pipe-cell": test_pipe_cell,
             "new-purpose": lambda ls: f"{SAY}: fixture new-purpose · widget · source owner" in ls,
             "review": test_review, "review-write": test_review_write,
             "value-derive": test_value_pending(NONE_FOUND, False),
             "value-ledger": lambda ls: (test_value_pending(PURPOSE_PENDING, True)(ls)
                                         and any(f"seed · armed {PURPOSE_PENDING} 3" in ln for ln in ls))}
    fails = []
    for plant in (None, "field-missing-legacy", *shows, *want, *refusals):
        lines, rc = run_fixture(plant)
        out = "\n".join(lines)
        reds = [ln for ln in lines if " RED " in ln]
        if plant in want and not (rc == 1 and any(all(s in ln for s in want[plant]) for ln in reds)):
            fails.append(f"{plant}: want exit 1 naming {', '.join(want[plant])}, got {rc}: {out[-400:]}")
        elif plant in refusals and not (rc == 2 and any(refusals[plant] in ln for ln in lines)):
            fails.append(f"{plant}: want exit 2 naming {refusals[plant]}, got {rc}: {out[-400:]}")
        elif plant not in want and plant not in refusals and rc != 0:
            fails.append(f"{plant or 'green'}: want exit 0, got {rc}: {out[-400:]}")
        elif plant is None and not any(" rows · " in ln and "stream-plan fence 1 graded" in ln for ln in lines):
            fails.append(f"green: the well-formed plan was not graded: {out[-400:]}")
        elif plant in shows and not shows[plant](lines):
            fails.append(f"{plant}: exit 0 and not what it shows: {out[-400:]}")
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="rk-"))
    try:
        typed = build_fixture(tmp)
        reg = pathlib.Path(tmp, derive_kit_rel(), REGISTRY)
        before = reg.read_bytes()
        for drop in (("--writer", "hand"), ("--layer", "layer.memory"), ("--lifecycle", "append-only"),
                     ("--reader", "input:spec"), ("--purpose", "a planted kind")):
            argv = [a for i, a in enumerate(FIXTURE_NEW) if not (a == drop[0] or (i and FIXTURE_NEW[i - 1] == drop[0]))]
            rc = main(argv, root=tmp)
            if rc != 2 or reg.read_bytes() != before:
                fails.append(f"new without {drop[0]}: want exit 2 and nothing written, got {rc}")
        for bad in ("", "x" * (PURPOSE_BYTES + 1), "two\nlines"):
            argv = [bad if i and FIXTURE_NEW[i - 1] == "--purpose" else a for i, a in enumerate(FIXTURE_NEW)]
            rc = main(argv, root=tmp)
            if rc != 2 or reg.read_bytes() != before:
                fails.append(f"new with --purpose {bad[:12]!r}: want exit 2 and nothing written, got {rc}")
        rc = main(FIXTURE_NEW[:-2] + ["--reader", "task:goal"], root=tmp)
        if rc != 2 or reg.read_bytes() != before:
            fails.append(f"new with a reader no role reads: want exit 2 and nothing written, got {rc}")
        unfielded = [a for i, a in enumerate(FIXTURE_NEW) if not (a == "--field" or FIXTURE_NEW[i - 1] == "--field")]
        for why, argv in (("an unresolvable --validator", unfielded + ["--form", "fence", "--validator", "record_kinds:no_such_check"]),
                          ("a --field", FIXTURE_NEW + ["--form", "fence", "--validator", f"record_kinds:{check_stream_plan.__name__}"])):
            rc = main(argv, root=tmp)   # S7: each `fence` refusal exits 2 and writes nothing
            if rc != 2 or reg.read_bytes() != before:
                fails.append(f"new --form fence with {why}: want exit 2 and nothing written, got {rc}")
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
            ap.add_argument("--layer")
            ap.add_argument("--lifecycle")
            ap.add_argument("--reader", action="append")
            ap.add_argument("--readers-none", dest="readers_none")
            ap.add_argument("--purpose")
            ap.add_argument("--form")
            ap.add_argument("--validator")
            try:
                a = ap.parse_args(argv[1:])
            except SystemExit as e:
                return int(e.code or 0)
            return add_record_kind(root, a)
        if argv[:1] == ["--purpose-review"]:
            ap = argparse.ArgumentParser(prog="record_kinds.py --purpose-review",
                                         description="review the purposes S4's populations lack")
            ap.add_argument("--from", dest="from_rel")
            ap.add_argument("--write", action="store_true")
            ap.add_argument("--ask")
            try:
                a = ap.parse_args(argv[1:])
            except SystemExit as e:
                return int(e.code or 0)
            if a.ask and not a.write:
                print(f"{SAY}: refused · --ask names the pending a write records: give --write")
                return 2
            return run_purpose_review(root, a.from_rel, a.write, a.ask)
        if argv == ["--print-purpose-pending"]:
            return print_purpose_pending(root)
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
