#!/usr/bin/env python3
"""instructions_edit.py — the one write path for instruction units, and the pack catalogue's reader
(PLAY-dOrderedCharter-15).

    python instructions_edit.py add|edit|remove|rename|split --manifest <kit id>|overlay --tag <tag> [row flags]
                                [--build <slug> --unit <id> --mark <mark>] [--successor <tag[,tag]>]
    python instructions_edit.py propose <write verb> <the same flags>
    python instructions_edit.py list [--manifest <kit id>|overlay]
    python instructions_edit.py render
    python instructions_edit.py check             # the leg: every check of a write, over the tree
    python instructions_edit.py fixture [--plant <case>]

THE MANIFESTS. `read_manifests` lists each kit's `instructions.toml` and the overlay, the one list a write
reads. Across nodes they are row stores: `merge-rows.py` merges them per entry, by each table's `tag` or `key`.

A WRITE, in `run_write`'s order. `instructions.edit` and `instructions.proof` are read at load, for every
verb: a refused read exits 2, and so does a value selecting a component no core row of the layer register
declares. While no core row declares `point.instruction.guard` every write exits 1 printing its proposal,
and a build records a kit manifest change through `build_records.py new change`, the stand-in door. Under
`flow-only` the flow's item writes and the command does not. Under `owner-command-agents-propose` a write
whose caller shows no proof prints its proposal and exits 1, `tty-cli` being standard error a terminal, the
stream the minimal guard's hook tests: a second test of one signal, since that hook is inline shell. The
record's inputs are flags tested only after those branches, each absent one exit 2. `check_tree` then grades
the would-be tree, and a green write writes the row, its change record, stages both, and re-renders.

THE CHECKS. `check_tree` holds every row of every manifest to the schema, one fact, the statement grammar,
one tag per row and no retired name minted again; the two arms of this module, conflicts at one level and
references; the tag checks over the tree; the pack catalogue; and, with the guard's point undeclared, no
change record but the stand-in door's. Where the tree holds a lock, the grammar's document and lock halves
join; a tree no render has reached yet owes neither. Exit 0 green, 1 red or refused, 2 a usage or load refusal.

THE PACKS. `packs.toml` holds one `[[pack]]` row per instruction pack, apart from the policy presets;
`resolve_practices` turns a `charter.practices` value naming packs and practices into practice tags.
"""
from __future__ import annotations

import argparse
import contextlib
import dataclasses
import difflib
import functools
import io
import json
import os
import pathlib
import re
import shlex
import subprocess
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import instruction_units as iu  # noqa: E402
from policy_value import PolicyRefused, read_policy_value, resolve_kit_dir  # noqa: E402

iu.load_memory_tree_path()
import build_records  # noqa: E402  the record factory, reached as the units module reaches it

SAY = "instructions-edit"
WRITE_VERBS = build_records.CHANGE_ACTIONS
OWNER_VALUE = "owner-command-agents-propose"
FLOW_VALUE = "flow-only"
FOR_ALL_VALUE = "command-for-all"
TTY_PROOF = "tty-cli"
FX_MANIFEST = "tools/alpha/instructions.toml"
FX_HEADER_LINES = 'before\n[[unit]]\ntag = "unit.fake"\nafter'
SIGNED_PROOFS = ("signed", "both")
GUARD_POINT = "point.instruction.guard"
FLOW_POINT = "point.instruction.flow"
SIGNED_POINT = "point.instruction.signed-proof"
LAYERS_TABLE = "layers.toml"
PACKS_TABLE = "packs.toml"
PRACTICES_TABLE = "practices.toml"
PACK_KINDS = ("methodology", "governance", "language")
PACK_ALL = "all"
ROW_ORDER = ("tag", "level", "type", "scope", "trigger", "budget", "text", "source", "owner", "usage", "help",
             "required-by", "enforced-by", "class", "fixed-by", "edges")
OPPOSED = re.compile(r"(MUST|NEVER)\s+(\S.*)", re.S)
#: the flags a write's change record is made from, each with the placeholder a proposal prints
RECORD_FLAGS = (("build", "--build", "<slug>"), ("unit", "--unit", "<id>"), ("mark", "--mark", "<editorial|semantic>"))
SUCCESSOR_FLAG = ("successor", "--successor", "<tag[,tag]>")


class Refused(Exception):
    """A verb that stops: `code` its exit and `lines` what it prints."""

    def __init__(self, code, *lines):
        super().__init__(lines[0] if lines else "")
        self.code, self.lines = code, list(lines)


@dataclasses.dataclass(frozen=True)
class Candidate:
    """A write's would-be manifest: `text`, and the change record's two pins."""
    text: str
    before: str
    after: str


def resolve_root() -> pathlib.Path:
    """The repository this kit sits in."""
    return pathlib.Path(iu.run_git(KIT_DIR, "rev-parse", "--show-toplevel").strip())


def read_declared_points(root) -> set:
    """Every point a core row of the tree's layer register declares."""
    import check_layers
    try:
        register = check_layers.read_layers(iu.derive_kit_file(root, LAYERS_TABLE))
    except check_layers.Unreadable as exc:
        raise Refused(2, f"{SAY}: refused · {exc}") from None
    return {p for r in register["layer"] if r.get("kind") == "core" for p in r.get("declares") or ()}


def read_load(root) -> tuple[str, str, set]:
    """S3, S5: `(instructions.edit, instructions.proof, the declared points)`, or the load refusal, exit 2."""
    policy_reader = functools.partial(read_policy_value, root=root)
    try:
        value = policy_reader("instructions.edit")[0][0]
        proof = policy_reader("instructions.proof")[0][0]
    except PolicyRefused as exc:
        raise Refused(2, f"{SAY}: refused · {exc.key} · {exc.line}") from None
    points = read_declared_points(root)
    if value == FLOW_VALUE and FLOW_POINT not in points:
        raise Refused(2, f"{SAY}: refused · instructions.edit = {value} selects an absent component: the flow, "
                         f"whose {FLOW_POINT} no core row declares · remedy: dDeclaredLoop's flow lands it")
    if proof in SIGNED_PROOFS and SIGNED_POINT not in points:
        raise Refused(2, f"{SAY}: refused · instructions.proof = {proof} selects an absent component: the signed "
                         f"proof, whose {SIGNED_POINT} no core row declares · remedy: use {TTY_PROOF}")
    return value, proof, points


def read_manifests(root) -> dict:
    """S1: `{<kit id>: its manifest's path, "overlay": the overlay's}`, a manifest not written yet included."""
    prefix, out = iu.derive_kit_prefix(), {}
    for desc in sorted(pathlib.Path(root, prefix).glob("*/kit.toml")):
        try:
            kit = tomllib.loads(desc.read_text(encoding="utf-8")).get("id")
        except (OSError, tomllib.TOMLDecodeError):
            continue
        if isinstance(kit, str):
            out[kit] = iu.derive_tool_rel(desc.parent.name, iu.MANIFEST)
    out["overlay"] = iu.OVERLAY
    return out


def read_text(root, rel) -> str | None:
    """A manifest's bytes as text, its line endings kept; None for a manifest not written yet."""
    path = pathlib.Path(root, rel)
    return path.read_bytes().decode("utf-8") if path.is_file() else None


def read_tree_rows(root, candidate=None) -> tuple[list, dict, list]:
    """`(units, tables, faults)` of every manifest, `candidate`, `{path: text}`, standing in for what it names:
    `tables` each manifest's `[[unit]]` tables as TOML reads them."""
    units, tables, faults = [], {}, []
    for kit, rel in read_manifests(root).items():
        text = (candidate or {}).get(rel, None)
        try:
            text = read_text(root, rel) if text is None else text
        except (OSError, UnicodeDecodeError) as exc:
            faults.append(f"{rel}: the manifest is unreadable: {exc}")
            continue
        if text is None:
            continue
        got, bad = iu.parse_unit_rows(text, rel, None if rel == iu.OVERLAY else kit)
        units += got
        faults += [str(f) for f in bad]
        if got:
            tables[rel] = tomllib.loads(text)["unit"]
    return units, tables, faults


def derive_row_pin(tag, row) -> str:
    """S7: `<tag>@<hash8>`, the pin over a row's `text`, or its `source` on a row with no `text`."""
    return f"{tag}@{iu.derive_unit_pin(row.get('text') or row.get('source') or '')}"


def render_row(row) -> str:
    """One `[[unit]]` table, its keys in `ROW_ORDER`, any other after them. JSON's strings are TOML's."""
    keys = [*ROW_ORDER, *sorted(set(row) - set(ROW_ORDER))]
    return "[[unit]]\n" + "".join(f"{k} = {json.dumps(row[k], ensure_ascii=False)}\n" for k in keys if k in row)


def derive_row(args, base=None) -> dict:
    """The row a write's flags give, over `base`. A level no digit spells stays text, for the schema to red."""
    row = dict(base or {"tag": args.tag})
    for key in ROW_ORDER[1:]:
        value = getattr(args, key.replace("-", "_"), None)
        if value is not None:
            row[key] = value
    if isinstance(row.get("level"), str) and row["level"].isdigit():
        row["level"] = int(row["level"])
    held = row.get("enforced-by")
    if isinstance(held, list) and len(held) == 1 and held[0].startswith(iu.ENFORCED_NONE):
        row["enforced-by"] = held[0]
    return row


def derive_candidate(text, rel, verb, args) -> Candidate:
    """The manifest after `verb`, and the record's pins. ponytail: `edit` and `rename` re-render the row, so a
    comment inside its table goes; a comment-keeping TOML writer is no stdlib, add one if rows grow comments."""
    units, faults = iu.parse_unit_rows(text, rel)
    if faults:
        raise Refused(1, *[f"{SAY}: red · {f}" for f in faults])
    if verb == "add":
        row = derive_row(args)
        if rel == iu.OVERLAY:   # PLAY-dOrderedCharter-32 S8: the overlay's rows by level then tag
            import overlay
            try:
                return Candidate(overlay.derive_overlay_text(text, [row]), "none", derive_row_pin(row["tag"], row))
            except overlay.OverlayRefused as exc:
                raise Refused(exc.code, str(exc)) from None
        lead = text.rstrip("\r\n") + "\n\n" if text.strip() else ""
        return Candidate(lead + render_row(row), "none", derive_row_pin(row["tag"], row))
    held = {u.tag: u for u in units}
    unit = held.get(args.tag)
    if unit is None:
        raise Refused(1, f"{SAY}: red · {rel} holds no row {args.tag} · remedy: `list` prints what it holds")
    table = tomllib.loads(text)["unit"][unit.index - 1]
    before = derive_row_pin(args.tag, table)
    tail = unit.body[len(unit.body.rstrip()):]
    if verb == "remove":
        return Candidate(text.replace(unit.body, "", 1), before, "none")
    if verb == "split":
        heirs = [s for s in (args.successor or "").split(",") if s]
        missing = [s for s in heirs if s not in held]
        if missing:
            raise Refused(1, f"{SAY}: red · {rel} holds no row {', '.join(missing)} · remedy: add each successor first")
        rows = tomllib.loads(text)["unit"]
        pins = [derive_row_pin(s, rows[held[s].index - 1]) for s in heirs]
        return Candidate(text.replace(unit.body, "", 1), before, ",".join(pins))
    row = derive_row(args, table)
    if verb == "rename":
        row["tag"] = args.successor or SUCCESSOR_FLAG[2]
    return Candidate(text.replace(unit.body, render_row(row) + tail, 1), before, derive_row_pin(row["tag"], row))


def derive_absent_flags(verb, args) -> list:
    """The record flags `verb` needs and `args` lacks, each `(attribute, flag, placeholder)`."""
    needed = RECORD_FLAGS + ((SUCCESSOR_FLAG,) if verb in ("rename", "split") else ())
    return [f for f in needed if not getattr(args, f[0], None)]


def render_proposal(rel, text, candidate, verb, args, given) -> list:
    """S2: the row diff, then the command that applies it: the flags given and a placeholder for each absent."""
    diff = difflib.unified_diff(text.splitlines(), candidate.text.splitlines(), rel, rel, lineterm="", n=1)
    flags = [f"{flag} {shown}" for _attr, flag, shown in derive_absent_flags(verb, args)]
    command = " ".join([f"python {iu.derive_kit_rel('instructions_edit.py')} {verb}", shlex.join(given), *flags])
    return [f"{SAY}: proposal · {verb} {args.tag} · {rel}", *diff, f"{SAY}: apply with: {command}"]


def read_target(root, args) -> tuple[str, str]:
    """`--manifest`'s path and text, an empty text for a manifest not written yet; an unknown id exits 2."""
    manifests = read_manifests(root)
    if args.manifest not in manifests:
        raise Refused(2, f"{SAY}: refused · --manifest {args.manifest!r} names no kit: {', '.join(manifests)}")
    rel = manifests[args.manifest]
    return rel, read_text(root, rel) or ""


def run_propose(root, verb, args, given) -> tuple[list, int]:
    rel, text = read_target(root, args)
    return render_proposal(rel, text, derive_candidate(text, rel, verb, args), verb, args, given), 0


def run_write(root, verb, args, given, load) -> tuple[list, int]:
    """S2's write, in the Data model's order; `load` is `read_load`'s."""
    value, proof, points = load
    rel, text = read_target(root, args)
    try:
        candidate = derive_candidate(text, rel, verb, args)
        proposal = render_proposal(rel, text, candidate, verb, args, given)
    except Refused as exc:
        candidate, proposal = None, exc.lines
    if GUARD_POINT not in points:
        raise Refused(1, f"{SAY}: refused · every write waits on the guard: no core row declares {GUARD_POINT}, "
                         f"which dDeclaredLoop's guard lands · a build records a kit manifest change through "
                         f"`python {build_records.KIT.parent.name}/{build_records.KIT.name}/build_records.py new change`, "
                         f"the stand-in door",
                      *proposal)
    if value == FLOW_VALUE:
        raise Refused(1, f"{SAY}: refused · instructions.edit = {value}: writes come from the flow's item, never "
                         f"this command", *proposal)
    if value == OWNER_VALUE and not (proof == TTY_PROOF and sys.stderr.isatty()):
        raise Refused(1, f"{SAY}: not proven · instructions.proof = {proof} shows no owner here, so this stays "
                         f"a proposal and nothing is written", *proposal)
    absent = derive_absent_flags(verb, args)
    if absent:
        raise Refused(2, f"{SAY}: refused · {verb} needs " + ", ".join(f[1] for f in absent) + " · nothing written")
    if candidate is None:
        raise Refused(1, *proposal)
    reds = check_tree(root, {rel: candidate.text})[0]
    if reds:
        raise Refused(1, *reds, f"{SAY}: refused · the would-be tree holds {len(reds)} red · nothing written")
    return write_candidate(root, rel, candidate, verb, args, proof if value == OWNER_VALUE else f"none — {value}")


def write_candidate(root, rel, candidate, verb, args, proof) -> tuple[list, int]:
    """The row, its record, both staged, since every read of a manifest or a record reads tracked paths, and
    the re-render. A record refused puts the manifest back: no row lands without its record."""
    path = pathlib.Path(root, rel)
    held = path.read_bytes() if path.is_file() else None
    path.parent.mkdir(parents=True, exist_ok=True)
    if rel == iu.OVERLAY and verb == "add":   # the overlay's one adder, writing the bytes `derive_candidate` checked
        import overlay
        overlay.write_overlay_units(path, [derive_row(args)])
    else:
        path.write_bytes(candidate.text.encode("utf-8"))
    successor = args.successor if verb in ("rename", "split") else "none" if verb == "remove" else None
    try:
        record = build_records.write_change(root, args.build, args.unit, args.tag, verb, args.mark, candidate.before,
                                             candidate.after, proof, successor, getattr(args, "promoted_from", None))
    except (ValueError, OSError) as exc:
        if held is None:
            path.unlink()
        else:
            path.write_bytes(held)
        raise Refused(2, f"{SAY}: refused · {exc} · nothing written") from None
    iu.run_git(root, "add", "--", rel, record)
    dirty = read_dirty(root)
    # PLAY-dOrderedCharter-46 S4: the overlay renders from the bytes just written; kit manifests are read
    # from the working tree already
    lines, rc = run_render(root, path if rel == iu.OVERLAY else None)
    # ponytail: a target dirty before the render prints nothing; a per-file snapshot would name it
    wrote = [rel, record, *sorted(p[3:] for p in read_dirty(root) - dirty)]
    return [f"{SAY}: wrote {p}" for p in wrote] + (lines if rc else []), rc


def read_dirty(root) -> set:
    return {p for p in iu.run_git(root, "status", "--porcelain", "-z").split("\0") if p}


def run_render(root, overlay_from=None) -> tuple[list, int]:
    """Every scope of the renderer of record `renderers.toml` assigns a target, the overlay read from
    `overlay_from` where a write verb just wrote it."""
    import render_playbook
    charter = iu.derive_instruction_tokens(root)["charter"]
    scopes = sorted({r["renderer"].partition(":")[2] for r in iu.read_renderers(root)
                     if r["renderer"].startswith("playbook:")})
    given = [] if overlay_from is None else ["--overlay-from", str(overlay_from)]
    lines, rc = [], 0
    for scope in scopes:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = max(rc, render_playbook.main(["--target", str(root), "--charter", charter, "--render-scope", scope,
                                               *given]))
        lines += out.getvalue().splitlines()
    return lines + [f"{SAY}: render · {len(scopes)} scope(s)"], rc


def run_list(root, manifest) -> tuple[list, int]:
    """`<tag>@<hash8>` of each row, of one manifest with `--manifest`."""
    manifests = read_manifests(root)
    if manifest is not None and manifest not in manifests:
        raise Refused(2, f"{SAY}: refused · --manifest {manifest!r} names no kit: {', '.join(manifests)}")
    units, tables, faults = read_tree_rows(root)
    rows = [derive_row_pin(u.tag, tables[u.path][u.index - 1]) for u in units
            if manifest is None or u.path == manifests[manifest]]
    return [f"{SAY}: red · {f}" for f in faults] + rows, 1 if faults else 0


def check_conflicts(units, records) -> list:
    """S6: two active directives at one level whose texts differ only in an opposite modal."""
    held = {}
    for u in units:
        m = OPPOSED.fullmatch((u.text or "").strip())
        if u.type == iu.DIRECTIVE and m and iu.derive_status(u.tag, records) == iu.ACTIVE:
            held.setdefault((u.level, " ".join(m.group(2).split())), {}).setdefault(m.group(1), u)
    return [f"{SAY}: red · conflict · {sides['MUST'].tag} and {sides['NEVER'].tag} at level {level} differ only in "
            f"MUST against NEVER · remedy: keep one" for (level, _text), sides in held.items() if len(sides) == 2]


def derive_unit_targets(unit) -> list:
    """Every `unit.*` tag a pointer's text or a row's `edges` names, a pin or a section cut."""
    spans = iu.SPAN.findall(unit.text or "") if unit.type == iu.POINTER else []
    entries = [t for e in unit.edges for t in e.partition("=")[2].split(",")]
    return [t for t in (re.split(r"[@#]", s)[0] for s in spans + entries) if t.startswith("unit.")]


def check_references(units, records) -> list:
    """S6: a pointer or an `edges` target naming a `unit.*` tag no active unit and no record's successor holds."""
    live = {u.tag for u in units if iu.derive_status(u.tag, records) == iu.ACTIVE}
    reds = []
    for u in units:
        if iu.derive_status(u.tag, records) != iu.ACTIVE:
            continue
        for tag in derive_unit_targets(u):
            if tag not in live and iu.derive_status(tag, records) in (iu.ACTIVE, "retired:none"):
                reds.append(f"{SAY}: red · reference · {u.tag} in {u.path} names {tag}, which no active unit and no "
                            f"change record's successor holds · remedy: point at a live unit")
    return reds


def check_tags(units, records) -> list:
    """Unit 19's two reads a would-be row can break before the index sees it: a tag held twice, and a retired
    name minted again."""
    seen, reds = {}, []
    for u in units:
        if u.tag in seen:
            reds.append(f"{SAY}: red · tag · {u.tag} is held by {seen[u.tag]} and {u.path} · remedy: keep one row")
        seen.setdefault(u.tag, u.path)
        status = iu.derive_status(u.tag, records)
        if status != iu.ACTIVE:
            reds.append(f"{SAY}: red · tag · {u.tag} in {u.path} is {status}, a retired name minted again · "
                        f"remedy: name it anew")
    return reds


def check_guard_witness(records, points) -> list:
    """No record of the command's while the guard's point is undeclared: such a record is a write admitted."""
    if GUARD_POINT in points:
        return []
    return [f"{SAY}: red · guard · {r['path']} carries Proof {r.get('Proof')!r}, a write admitted while "
            f"{GUARD_POINT} is undeclared · remedy: record through the stand-in door"
            for r in records if r.get("Proof") != build_records.DOOR_PROOF]


def run_tag_check(root) -> list:
    """Unit 19's checks over the tree, its reds as `gov_tag.py check --json` names them."""
    import gov_tag
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        gov_tag.run_kit_verb(pathlib.Path(root), "check", None, sets={}, as_json=True,
                             kit_rel=iu.derive_tool_rel(KIT_DIR.name))
    said = out.getvalue()
    return json.loads(said[said.index("{\n"):])["reds"]


def read_practice_tags(root) -> list | None:
    """The practice catalogue's tags, None until unit 1 writes it."""
    path = iu.derive_kit_file(root, PRACTICES_TABLE)
    if not path.is_file():
        return None
    return [r.get("tag") for r in tomllib.loads(path.read_text(encoding="utf-8")).get("practice") or []]


def read_packs(root=None) -> list:
    """S8: `packs.toml`'s `[[pack]]` rows; an unreadable table raises UnitRowError."""
    path = iu.derive_kit_file(root or resolve_root(), PACKS_TABLE)
    try:
        return tomllib.loads(path.read_text(encoding="utf-8")).get("pack") or []
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise iu.UnitRowError(f"{path.as_posix()} is unreadable: {exc}") from None


def resolve_practices(value, root=None) -> list:
    """S8: a `charter.practices` value, pack names and practice tags, as practice tags in first-named order, a
    pack's `all` every catalogue tag. No catalogue, or a name it lacks, raises UnitRowError, naming the row a
    retired tag's `replaces` points at."""
    root = root or resolve_root()
    packs, catalogue = {p.get("name"): p for p in read_packs(root)}, read_practice_tags(root)
    if catalogue is None:
        raise iu.UnitRowError(f"no practice resolves: {PRACTICES_TABLE} holds no catalogue yet")
    tags = []
    for name in value:
        members = packs[name]["practices"] if name in packs else [name]
        members = catalogue if members == PACK_ALL else members
        unknown = [m for m in members if m not in catalogue]
        if unknown:
            path = iu.derive_kit_file(root, PRACTICES_TABLE)
            successors = iu.derive_successors(tomllib.loads(path.read_text(encoding="utf-8")).get("practice") or [])
            raise iu.UnitRowError(f"`{name}` names {', '.join(unknown)}, which the practice catalogue lacks"
                                  + "".join(f"; {t} is replaced by {successors[t]}" for t in unknown if t in successors))
        tags += [t for t in members if t not in tags]
    return tags


def check_packs(root) -> tuple[list, list]:
    """S8: `(lines, reds)`: each row's fields, then, once the catalogue exists, each named practice held by it
    and no pack named as a practice is; with no catalogue that half prints `unarmed`."""
    packs, catalogue, reds = read_packs(root), read_practice_tags(root), []
    for i, p in enumerate(packs, 1):
        name, kind, members = p.get("name"), p.get("kind"), p.get("practices")
        where = f"{SAY}: red · pack · {PACKS_TABLE} row {i} ({name})"
        if not isinstance(name, str) or not name or not isinstance(p.get("description"), str):
            reds.append(f"{where} carries no `name` or `description`")
        if kind not in PACK_KINDS:
            reds.append(f"{where} · `kind` {kind!r} is outside {', '.join(PACK_KINDS)}")
        if members != PACK_ALL and not (isinstance(members, list) and all(isinstance(m, str) for m in members)):
            reds.append(f"{where} · `practices` is no list of practice tags and no `{PACK_ALL}`")
        elif catalogue is not None:
            reds += [f"{where} names {m}, which the catalogue lacks"
                     for m in (() if members == PACK_ALL else members) if m not in catalogue]
            if name in catalogue or f"practice.{name}" in catalogue:
                reds.append(f"{where} · its name equals a practice's")
    armed = "unarmed: no practice catalogue yet" if catalogue is None else f"{len(catalogue)} practice(s)"
    return [f"{SAY}: packs · {len(packs)} row(s) · {armed}"], reds


def check_tree(root, candidate=None) -> tuple[list, list]:
    """S6 over the tree, `candidate` the would-be manifest: `(reds, the lines a green arm prints)`."""
    root = pathlib.Path(root)
    units, tables, faults = read_tree_rows(root, candidate)
    reds = [f"{SAY}: red · {f}" for f in faults]
    try:
        records = iu.read_change_records(root)
    except iu.UnitRowError as exc:
        records = []
        reds += [f"{SAY}: red · status · {ln}" for ln in str(exc).splitlines()]
    held = {u.tag for u in units}

    def resolve(tag):   # a row of the would-be tree is no index row yet, and `unit.*` is the references arm's
        return [{"kind": "tag"}] if tag in held or tag.startswith("unit.") else iu.load_resolver(root)(tag)

    for u in units:
        reds += iu.check_unit_row(u, tables[u.path][u.index - 1], "repo" if u.path == iu.OVERLAY else "unit")
        reds += iu.check_statement({"tag": u.tag, "type": u.type, "text": u.text, "source": u.source,
                                    "trigger": u.trigger, "enforced-by": u.enforced_by}, resolve)
    reds += iu.check_one_fact(units, records) + check_tags(units, records)
    reds += check_conflicts(units, records) + check_references(units, records)
    reds += check_guard_witness(records, read_declared_points(root))
    if iu.read_lock(root):
        reds += [ln for ln in iu.run_grammar(root)[0] if ": red · " in ln]
    try:
        reds += run_tag_check(root)
    except (PolicyRefused, RuntimeError) as exc:     # RuntimeError: the tag index's TagError
        reds.append(f"{SAY}: red · tags · {exc}")
    lines, pack_reds = check_packs(root)
    armed = f"{len(units)} row(s)" if units else "unarmed: the tree holds no unit row"
    return reds + pack_reds, lines + [f"{SAY}: check · {armed}"]


def run_check(root) -> tuple[list, int]:
    reds, lines = check_tree(root)
    return reds + lines + [f"{SAY}: check · {len(reds)} red"], 1 if reds else 0


# ------------------------------------------------------------------------------------------ the fixture

class Terminal(io.StringIO):
    """A standard error that is a terminal: how a case stages the owner, so no test switch ships."""
    isatty = lambda self: True  # noqa: E731


def run_cli(root, *argv, tty=False) -> tuple[int, str]:
    """A verb over the fixture: `(exit, what it printed)`, standard error a terminal under `tty`."""
    out, err = io.StringIO(), Terminal() if tty else io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        rc = run_verb(list(argv), pathlib.Path(root))
    return rc, out.getvalue() + err.getvalue()


FX_BUILD = "tEdit"
FX_UNIT = "ARCH-tEdit-1"
FX_RECORD = ("--build", FX_BUILD, "--unit", FX_UNIT, "--mark", "semantic")
FX_ROW = ("--manifest", "corekit", "--tag", "unit.demo", "--type", "directive", "--level", "3", "--trigger", "always",
          "--text", "MUST demo.")
FX_RENDERERS = '[[target]]\npaths = ["AGENTS.md"]\nrenderer = "hand"\n'
FX_PRACTICES = '[[practice]]\ntag = "practice.land"\n\n[[practice]]\ntag = "practice.memory"\n'


def derive_fx_row(tag, text="MUST hold.", kind="directive", level=3) -> str:
    return render_row({"tag": tag, "level": level, "type": kind, "trigger": "always", "text": text})


def derive_fx_long(tag, text) -> str:
    """A row whose `text` is a multi-line string, a shape the row writer never emits and an author may."""
    return f'[[unit]]\ntag = "{tag}"\nlevel = 3\ntext = """\n{text}\n"""\n'


def derive_fx_policy(key, default="a") -> str:
    return f'[[policy]]\nkey = "{key}"\ndefault = "{default}"\n'


def write_policy(root, **values):
    import gov_tag
    body = "".join(f'{k.replace("_", ".")} = "{v}"\n' for k, v in values.items())
    gov_tag.write_commit(root, {".governance/policy.toml": body}, "the policy")


def write_points(root, *points):
    import gov_tag
    declares = json.dumps(list(points))
    gov_tag.write_commit(root, {iu.derive_tool_rel(KIT_DIR.name, LAYERS_TABLE):
                                f'[[layer]]\ntag = "layer.instruction"\nkind = "core"\ndeclares = {declares}\n\n'
                                '[[layer]]\ntag = "layer.exp"\nkind = "expansion"\n'}, "the points")


def build_tree(c, *points, rows="", **policy) -> pathlib.Path:
    """S10's throwaway repository: unit 19's tag tree with the `unit` namespace, a kit manifest, a build folder,
    a renderer table, the pack catalogue, its own layer register declaring `points`, and a committed policy."""
    import gov_tag
    root = gov_tag.build_tags_fixture(c.top, "none")
    kit = iu.derive_tool_rel(KIT_DIR.name)
    registry = (root / kit / "namespaces.toml").read_text(encoding="utf-8")
    gov_tag.write_commit(root, {f"{kit}/namespaces.toml": registry + gov_tag.FIXTURE_UNIT_ROW,
                                f"{kit}/{iu.RENDERERS_TABLE}": FX_RENDERERS,
                                f"{kit}/{PACKS_TABLE}": (KIT_DIR / PACKS_TABLE).read_text(encoding="utf-8"),
                                f"memory/builds/{FX_BUILD}/README.md": "# tEdit\n",
                                "tools/corekit/instructions.toml": rows}, "the edit tree")
    write_points(root, *points)
    if policy:
        write_policy(root, **policy)
    return root


def read_change_at(root, said) -> str:
    """The change record a write printed, its text."""
    rel = re.search(r"wrote (\S+-change-\d+\.md)", said)
    return (pathlib.Path(root) / rel.group(1)).read_text(encoding="utf-8") if rel else ""


def read_manifest_tags(root) -> list:
    return [u.tag for u in read_tree_rows(root)[0]]


def read_porcelain(root) -> str:
    return iu.run_git(root, "status", "--porcelain")


def write_merge_driver(c):
    """The fixture repository's `main`: the real driver wired to both manifest routes."""
    mt = resolve_kit_dir("memory-tree", "merge-rows.py", KIT_DIR)
    iu.run_git(c.top, "config", "merge.rows.driver",
               f'"{pathlib.Path(sys.executable).as_posix()}" "{(mt / "merge-rows.py").as_posix()}" %O %A %B %P')
    c.write_file(".gitattributes", f"**/{iu.MANIFEST} merge=rows\n{iu.OVERLAY} merge=rows\n")
    iu.run_git(c.top, "checkout", "-q", "-b", "main")
    iu.run_commit(c.top, "the wiring")


def run_merge_pair(c, name, base, ours, theirs, rel=FX_MANIFEST) -> tuple:
    """`rel` at `base`, one branch to each side, theirs merged into ours: `(exit, git's and the driver's words, the file)`."""
    iu.run_git(c.top, "checkout", "-q", "-b", f"{name}-base", "main")
    c.write_file(rel, base)
    iu.run_commit(c.top, "the base")
    for side, text in (("ours", ours), ("theirs", theirs)):
        iu.run_git(c.top, "checkout", "-q", "-b", f"{name}-{side}", f"{name}-base")
        c.write_file(rel, text)
        iu.run_commit(c.top, side)
    iu.run_git(c.top, "checkout", "-q", f"{name}-ours")
    done = subprocess.run(["git", "-C", str(c.top), "-c", "user.name=f", "-c", "user.email=f@f", "-c",
                           "commit.gpgsign=false", "merge", "-q", "--no-edit", f"{name}-theirs"], capture_output=True,
                          text=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    return done.returncode, done.stdout + done.stderr, (c.top / rel).read_text(encoding="utf-8")


def check_whole_conflict(c, label, rc, said, merged, ours, theirs, named):
    """A whole-file conflict: exit 1, both sides entire between the markers, and a closing label holding `named`."""
    close = merged.rstrip("\n").rsplit("\n", 1)[-1]
    c.check(label, rc == 1 and merged.startswith(f"<<<<<<< ours\n{ours}=======\n{theirs}>>>>>>> theirs")
            and named in close, f"{rc} {close!r} {said}")


def arm_merge(c):
    write_merge_driver(c)
    base = derive_fx_row("unit.base")
    rc, said, merged = run_merge_pair(c, "two", base, base + "\n" + derive_fx_row("unit.ours"),
                                      base + "\n" + derive_fx_row("unit.theirs"))
    tags = [u.tag for u in iu.parse_unit_rows(merged, FX_MANIFEST)[0]]
    c.check("two branches' adds merge with both tags once", rc == 0 and sorted(tags) == ["unit.base", "unit.ours",
            "unit.theirs"], f"{rc} {tags} {said}")
    c.check("the table class ran and the row plane did not", "merge-rows: tables " in said and "merge-rows: rows " not in said,
            said)
    rc, said, merged = run_merge_pair(c, "same", base, base + "\n" + derive_fx_row("unit.both", "MUST one."),
                                      base + "\n" + derive_fx_row("unit.both", "MUST two."))
    c.check("one tag added with different bytes is a conflict the driver names",
            rc == 1 and "unit.both" in said and "<<<<<<<" in merged, f"{rc} {said}")


def arm_merge_edit(c, name):
    """The three both-sides rows over one tag: each a whole-file conflict naming it, nothing kept from one side alone."""
    write_merge_driver(c)
    held, one, two, other = (derive_fx_row("unit.base"), derive_fx_row("unit.base", "MUST one."),
                             derive_fx_row("unit.base", "MUST two."), derive_fx_row("unit.other"))
    base, ours, theirs = {"merge-both-edit": (held, one, two), "merge-delete-edit": (held + other, other, two + other),
                          "merge-edit-delete": (held + other, one + other, other)}[name]
    check_whole_conflict(c, f"{name} is a whole-file conflict naming the tag", *run_merge_pair(c, "edit", base, ours, theirs),
                         ours, theirs, "unit.unit.base")


def arm_merge_one_side(c, name):
    """Rows 9, 12 and 11 of the table envelope over one tag, each beside an ours edit of another so git runs the
    driver: a clean merge, the tag gone where theirs or both deleted it and held once where only theirs added it."""
    write_merge_driver(c)
    held, other, edit = derive_fx_row("unit.base"), derive_fx_row("unit.other"), derive_fx_row("unit.other", "MUST one.")
    base, ours, theirs, want = {"merge-theirs-delete": (held + other, held + edit, other, edit),
                                "merge-both-delete": (held + other, edit, other, edit),
                                "merge-theirs-add": (other, edit, other + held, edit + held)}[name]
    rc, said, merged = run_merge_pair(c, "one", base, ours, theirs)
    c.check(f"{name} merges clean through the driver to ours' entries and theirs' one-sided result",
            rc == 0 and merged == want and "merge-rows: tables " in said, f"{rc} {said} {merged}")


def arm_merge_multiline(c):
    write_merge_driver(c)
    one, two, kept = derive_fx_row("unit.one"), derive_fx_row("unit.two"), derive_fx_long("unit.kept", FX_HEADER_LINES)
    edit_one, edit_two = derive_fx_row("unit.one", "MUST move."), derive_fx_row("unit.two", "MUST move.")
    added = derive_fx_long("unit.added", "plain\nlines")
    rc, said, merged = run_merge_pair(c, "long", one + kept + two, edit_one + kept + two + added, one + kept + edit_two)
    c.check("edits around a string holding a header line merge clean", rc == 0, f"{rc} {said}")
    c.check("the output parses with no tag cut from the string", [u["tag"] for u in tomllib.loads(merged)["unit"]]
            == ["unit.one", "unit.kept", "unit.two", "unit.added"], merged)
    c.check("that unit's chunk is byte-identical to its side's", kept in merged and added in merged, merged)


def arm_merge_same_add(c):
    write_merge_driver(c)
    base, row = derive_fx_row("unit.base"), derive_fx_row("unit.both")
    rc, said, merged = run_merge_pair(c, "same", base, base + row, base + row)
    c.check("one tag added with the same bytes lands once", rc == 0 and merged == base + row, f"{rc} {said} {merged}")


def arm_merge_policy(c):
    write_merge_driver(c)
    one, two, three, four, five = (derive_fx_policy(f"adopter.{n}") for n in ("one", "two", "three", "four", "five"))
    rc, said, merged = run_merge_pair(c, "adds", one, one + two + three, one + four + five, iu.OVERLAY)
    c.check("two policy rows added on each side merge keyed by `key`", rc == 0 and merged == one + two + three + four + five,
            f"{rc} {said} {merged}")
    ours, theirs = derive_fx_policy("adopter.one", "b"), derive_fx_policy("adopter.one", "c")
    check_whole_conflict(c, "both sides editing one row's default names policy.<key>",
                         *run_merge_pair(c, "edits", one, ours, theirs, iu.OVERLAY), ours, theirs, "policy.adopter.one")


def check_failed_merge(c, label, name, base, ours, theirs, message):
    """A merge the driver fails closed on: the whole-file conflict, and the driver's stderr naming `message`, the
    postcondition this plant exists for, never the failure string every postcondition shares."""
    rc, said, merged = run_merge_pair(c, name, base, ours, theirs)
    check_whole_conflict(c, label, rc, said, merged, ours, theirs, "merge-rows failed")
    c.check(f"...and the driver names its own postcondition: {message}", message in said, said)


def arm_merge_parse(c):
    write_merge_driver(c)
    base = derive_fx_row("unit.base")
    ours, theirs = base + '  [[unit]]\ntag = "unit.hidden"\n', base + derive_fx_row("unit.theirs")
    check_failed_merge(c, "an indented header after an entry fails closed with both sides", "cut", base, ours,
                       theirs, "is not one array-of-tables entry")


def arm_merge_cut(c):
    """PLAY-dOrderedCharter-70 S16: an indented header in the preamble parses, and the cut cannot rebuild it."""
    write_merge_driver(c)
    base = derive_fx_row("unit.base")
    ours, theirs = '  [[unit]]\ntag = "unit.hidden"\n' + base, base + derive_fx_row("unit.theirs")
    check_failed_merge(c, "an indented header in the preamble fails closed with both sides", "pre", base, ours,
                       theirs, "the cut does not reproduce tomllib's read")


def arm_merge_unterminated(c):
    """PLAY-dOrderedCharter-70 S6: three sides ending in an unterminated entry, edited apart, merge clean."""
    write_merge_driver(c)
    one, two = derive_fx_row("unit.one"), derive_fx_row("unit.two").rstrip("\n")
    edit_one, edit_two = derive_fx_row("unit.one", "MUST move."), derive_fx_row("unit.two", "MUST move.").rstrip("\n")
    rc, said, merged = run_merge_pair(c, "unterm", one + two, edit_one + two, one + edit_two)
    c.check("disjoint edits over an unterminated last entry merge clean", rc == 0
            and [u["tag"] for u in tomllib.loads(merged)["unit"]] == ["unit.one", "unit.two"], f"{rc} {said}")
    c.check("...holding both edits", edit_one in merged and edit_two in merged, merged)


def arm_merge_moved(c):
    """PLAY-dOrderedCharter-70 S16, its second fork: an unterminated final chunk in ours, an add in theirs."""
    write_merge_driver(c)
    one, two, three = derive_fx_row("unit.one"), derive_fx_row("unit.two"), derive_fx_row("unit.three").rstrip("\n")
    edit_one = derive_fx_row("unit.one", "MUST move.")
    rc, said, merged = run_merge_pair(c, "moved", one + two.rstrip("\n"), edit_one + two.rstrip("\n"), one + two + three)
    c.check("an unterminated final chunk beside an add merges clean", rc == 0
            and [u["tag"] for u in tomllib.loads(merged)["unit"]] == ["unit.one", "unit.two", "unit.three"],
            f"{rc} {said}")


def arm_merge_written(c):
    """PLAY-dOrderedCharter-70 S16, its second fork: a chunk altered on the read of the written lines reaches the
    postcondition that every written chunk is one side's bytes."""
    import importlib.util
    mt = resolve_kit_dir("memory-tree", "merge-rows.py", KIT_DIR)
    spec = importlib.util.spec_from_file_location("merge_rows_fx", mt / "merge-rows.py")
    mr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mr)
    real, calls = mr.read_tables, []

    def read_altered(lines):
        calls.append(1)
        pre, tables = real(lines)
        if len(calls) == 4:  # the written lines: one chunk altered after the merge chose it
            key = next(iter(tables))
            tables[key] = tables[key] + "# altered\n"
        return pre, tables
    mr.read_tables = read_altered
    base = derive_fx_row("unit.base")
    split = lambda t: t.splitlines(keepends=True)  # noqa: E731
    try:
        mr.resolve_tables(split(base), split(base + derive_fx_row("unit.ours")), split(base + derive_fx_row("unit.theirs")))
        said = "merged clean"
    except Exception as exc:  # noqa: BLE001 — the postcondition's own exception is the arm's subject
        said = f"{type(exc).__name__}: {exc}"
    c.check("a written chunk no side wrote fails closed by name", "byte-identical to no side's" in said, said)


def arm_root_prefix(c):
    """PLAY-dOrderedCharter-70 S5: at a root install the prefix is empty, and no join adds a leading `/`."""
    c.write_file("kitx/kit.toml", 'id = "kitx"\n')
    c.write_file("kitx/instructions.toml", derive_fx_row("unit.rooted"))
    iu.run_commit(c.top, "a root install")
    held = iu.derive_kit_prefix
    iu.derive_kit_prefix = lambda: ""
    try:
        manifests = read_manifests(c.top)
        units, _tables, faults = read_tree_rows(c.top)
    finally:
        iu.derive_kit_prefix = held
    c.check("read_manifests answers the manifest with no leading slash", manifests.get("kitx") == "kitx/instructions.toml",
            str(manifests))
    c.check("...and the row is read", [u.tag for u in units] == ["unit.rooted"] and not faults,
            f"{[u.tag for u in units]} {faults}")


def arm_propose(c):
    root = build_tree(c)
    rc, said = run_cli(root, "propose", "add", *FX_ROW)
    c.check("propose prints the row diff", rc == 0 and '+tag = "unit.demo"' in said, said)
    c.check("propose prints the command, a placeholder for each absent flag",
            "add --manifest corekit" in said and "--build <slug>" in said and "--mark <editorial|semantic>" in said, said)
    c.check("propose writes nothing", read_porcelain(root) == "", read_porcelain(root))


def arm_owner_propose(c):
    root = build_tree(c, GUARD_POINT, instructions_edit=OWNER_VALUE)
    rc, said = run_cli(root, "add", *FX_ROW, *FX_RECORD, tty=True)
    record = read_change_at(root, said)
    c.check("a write from a terminal writes the row", rc == 0 and "unit.demo" in read_manifest_tags(root), said)
    c.check("its change record's Proof reads tty-cli", "- **Proof:** tty-cli" in record, record or said)
    iu.run_commit(root, "the write")
    other = [("unit.other" if a == "unit.demo" else "MUST other." if a == "MUST demo." else a) for a in FX_ROW]
    rc, said = run_cli(root, "add", *other, *FX_RECORD)
    c.check("the same write off a terminal prints the proposal and exits 1",
            rc == 1 and "proposal" in said and '+tag = "unit.other"' in said, said)
    c.check("it writes nothing", read_porcelain(root) == "" and "unit.other" not in read_manifest_tags(root),
            read_porcelain(root))


def arm_rerender(c):
    import gov_tag
    root = build_tree(c, GUARD_POINT)
    kit = iu.derive_tool_rel(KIT_DIR.name)
    gov_tag.write_commit(root, {f"{kit}/{iu.RENDERERS_TABLE}": '[[target]]\npaths = ["AGENTS.md"]\nrenderer = "playbook:charter"\n',
                                ".governance/deploy.toml": iu.SLOT_DEPLOY, iu.derive_template_rel(): iu.SLOT_TEMPLATE.format("reader.every")},
                         "a rendered charter")
    rc, said = run_cli(root, "add", *FX_ROW, "--scope", "reader.every", *FX_RECORD, tty=True)
    charter = (root / "AGENTS.md").read_text(encoding="utf-8")
    c.check("a write re-renders the target the table assigns", rc == 0 and "MUST demo." in charter, said + charter)
    c.check("it prints the paths it wrote", all(f"wrote {p}" in said for p in ("tools/corekit/instructions.toml", "AGENTS.md"))
            and "-change-1.md" in said, said)
    iu.run_commit(root, "the write")
    (root / "AGENTS.md").write_text(charter + "a hand edit\n", encoding="utf-8", newline="")
    other = [("unit.other" if a == "unit.demo" else "MUST other." if a == "MUST demo." else a) for a in FX_ROW]
    rc, said = run_cli(root, "add", *other, *FX_RECORD, tty=True)
    c.check("a would-be tree over a stale render is refused by the lock half of the grammar",
            rc == 1 and "differs from the bytes the renderer wrote" in said, said)


def arm_command_for_all(c):
    root = build_tree(c, GUARD_POINT, instructions_edit=FOR_ALL_VALUE)
    rc, said = run_cli(root, "add", *FX_ROW, *FX_RECORD)
    record = read_change_at(root, said)
    c.check("a non-terminal write writes the row", rc == 0 and "unit.demo" in read_manifest_tags(root), said)
    c.check("its record's Proof reads none — command-for-all", f"- **Proof:** none — {FOR_ALL_VALUE}" in record, record)
    iu.run_commit(root, "the write")
    rc, said = run_cli(root, "add", "--manifest", "corekit", "--tag", "unit.prose", "--type", "prose", "--level", "3",
                       "--text", "Some prose.", *FX_RECORD)
    c.check("a would-be tree failing schema is refused naming the row", rc == 1 and "unit.prose" in said, said)
    c.check("the refused write writes nothing", read_porcelain(root) == "", read_porcelain(root))


def arm_flow_only(c):
    root = build_tree(c, GUARD_POINT, instructions_edit=FLOW_VALUE)
    for argv in (("list",), ("render",), ("check",), ("propose", "add", *FX_ROW), ("add", *FX_ROW)):
        rc, said = run_cli(root, *argv)
        c.check(f"`{argv[0]}` exits 2 naming the absent flow", rc == 2 and FLOW_POINT in said, said)
    write_points(root, GUARD_POINT, FLOW_POINT)
    rc, said = run_cli(root, "add", *FX_ROW, *FX_RECORD, tty=True)
    c.check("with the point declared a write exits 1 naming the flow as the writer",
            rc == 1 and "the flow's item" in said and read_porcelain(root) == "", said)
    rc, said = run_cli(root, "list")
    c.check("with the point declared a read verb loads", rc == 0, said)


def arm_proof_values(c):
    root = build_tree(c)
    for value in SIGNED_PROOFS:
        write_policy(root, instructions_proof=value)
        rc, said = run_cli(root, "list")
        c.check(f"instructions.proof = {value} exits 2 naming the absent signed proof",
                rc == 2 and "signed proof" in said and SIGNED_POINT in said, said)
    write_policy(root, instructions_proof=TTY_PROOF)
    rc, said = run_cli(root, "list")
    c.check("tty-cli loads", rc == 0, said)
    loose = iu.Case(c.top / "loose", c.out)    # the only commit, so no landed revision stands behind the value
    loose.top.mkdir()
    iu.run_git(loose.top, "init", "-q", "-b", "main")
    loose.write_file(".governance/policy.toml", 'instructions.edit = "loose"\n')
    iu.run_commit(loose.top, "a value the catalogue refuses")
    rc, said = run_cli(loose.top, "list")
    c.check("a refused policy read refuses the verb at load, naming the key", rc == 2 and "instructions.edit" in said, said)


def arm_guard(c):
    root = build_tree(c)
    before = (root / "tools/corekit/instructions.toml").read_bytes()
    rc, said = run_cli(root, "add", *FX_ROW, *FX_RECORD, tty=True)
    c.check("a write exits 1 naming the guard's point, dDeclaredLoop and the stand-in door", rc == 1 and all(
        s in said for s in (GUARD_POINT, "dDeclaredLoop", "new change", '+tag = "unit.demo"')), said)
    c.check("the manifest is unchanged", (root / "tools/corekit/instructions.toml").read_bytes() == before)
    args = (root, FX_BUILD, FX_UNIT, "unit.demo", "add", "semantic", "none", "unit.demo@0123abcd")
    rel = build_records.write_change(*args, build_records.DOOR_PROOF)
    iu.run_git(root, "add", "--", rel)
    rc, said = run_cli(root, "check")
    c.check("the stand-in door's record is no admitted write", "a write admitted" not in said, said)
    rel = build_records.write_change(*args, TTY_PROOF)
    iu.run_git(root, "add", "--", rel)
    rc, said = run_cli(root, "check")
    c.check("a command's record with the point undeclared reds the check", rc == 1 and "a write admitted" in said, said)


def arm_checks(c):
    import gov_tag
    root = build_tree(c, rows=derive_fx_row("unit.push", "MUST push after each pass.") + "\n"
                      + derive_fx_row("unit.hold", "NEVER push after each pass."))
    rc, said = run_cli(root, "check")
    c.check("MUST against NEVER at one level reds the conflict arm",
            rc == 1 and "conflict" in said and "unit.push" in said and "unit.hold" in said, said)
    rows = render_row({"tag": "unit.point", "level": 3, "type": "pointer", "text": "When lost, read `unit.gone`."})
    gov_tag.write_commit(root, {"tools/corekit/instructions.toml": rows}, "a pointer")
    rc, said = run_cli(root, "check")
    c.check("a pointer to unit.gone with no successor reds the references arm",
            rc == 1 and "reference" in said and "unit.gone" in said, said)
    rows += "\n" + derive_fx_row("unit.new")
    gov_tag.write_commit(root, {"tools/corekit/instructions.toml": rows}, "its heir")
    rel = build_records.write_change(root, FX_BUILD, FX_UNIT, "unit.gone", "rename", "editorial", "unit.gone@0123abcd",
                                     "unit.new@0123abcd", TTY_PROOF, "unit.new")
    iu.run_git(root, "add", "--", rel)
    rc, said = run_cli(root, "check")
    c.check("a change record naming the successor clears it", "· reference ·" not in said, said)


def arm_record(c):
    two = derive_fx_row("unit.one", "MUST one.") + "\n" + derive_fx_row("unit.left", "MUST left.") + "\n"
    root = build_tree(c, GUARD_POINT, rows=two + derive_fx_row("unit.right", "MUST right.") + "\n"
                      + derive_fx_row("unit.whole", "MUST whole."), instructions_edit=FOR_ALL_VALUE)
    target = ("--manifest", "corekit")
    rc, said = run_cli(root, "rename", *target, "--tag", "unit.one", "--successor", "unit.two", "--build", FX_BUILD,
                       "--unit", FX_UNIT)
    c.check("a rename with no --mark exits 2 naming the flag and writes nothing",
            rc == 2 and "--mark" in said and read_porcelain(root) == "", said)
    rc, said = run_cli(root, "rename", *target, "--tag", "unit.one", "--successor", "unit.two", *FX_RECORD)
    renamed = read_change_at(root, said)
    c.check("the rename writes", rc == 0 and "unit.two" in read_manifest_tags(root), said)
    for want in ("**Unit:** unit.one", "**Action:** rename", "**Before:** unit.one@", "**After:** unit.two@",
                 "**Mark:** semantic", "**Successor:** unit.two", "**Proof:** none"):
        c.check(f"the rename's record holds `{want}`", f"- {want}" in renamed, renamed)
    rc, said = run_cli(root, "split", *target, "--tag", "unit.whole", "--successor", "unit.left,unit.right", *FX_RECORD)
    split = read_change_at(root, said)
    after = iu.read_change_fields(split).get("After", "")
    c.check("the split's After holds one pin per successor, in order", rc == 0
            and [p.split("@")[0] for p in after.split(",")] == ["unit.left", "unit.right"], after or said)
    for record in [p for p in iu.run_git(root, "ls-files", "memory/builds").splitlines() if "-change-" in p]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = build_records.main(["read", (root / record).as_posix()])
        printed = dict(ln.split(" · ", 1)[1].split(": ", 1) for ln in out.getvalue().splitlines())
        c.check(f"build_records.py read grades {pathlib.PurePosixPath(record).name} clean", rc == 0, out.getvalue())
        got = iu.read_change_fields((root / record).read_text(encoding="utf-8"))
        c.check("read_change_fields returns the fields that verb prints", got == printed, f"{got} vs {printed}")
    bare = renamed.replace("- **Successor:** unit.two\n", "")
    bad = build_records.read_change(f"memory/builds/{FX_BUILD}/build/2026-01-01-build-{FX_UNIT}-change-9.md", bare)
    c.check("a record missing Successor on a rename is red", any(k == "Successor" for k, _ in bad["malformed"]),
            str(bad["malformed"]))
    c.check("the two ending-action lists agree", set(iu.ENDING_ACTIONS) == set(build_records.ENDING_ACTIONS))


def arm_packs(c):
    table = iu.derive_tool_rel(KIT_DIR.name, PACKS_TABLE)
    catalogue = iu.derive_tool_rel(KIT_DIR.name, PRACTICES_TABLE)
    shipped = (KIT_DIR / PACKS_TABLE).read_text(encoding="utf-8")
    c.write_file(table, shipped)
    lines, reds = check_packs(c.top)
    c.check("with no catalogue the check prints unarmed", not reds and "unarmed" in lines[0], str(lines + reds))
    c.write_file(catalogue, FX_PRACTICES)
    tags = resolve_practices(["foundation"], c.top)
    c.check("resolve_practices(['foundation']) returns every catalogue tag", tags == ["practice.land", "practice.memory"],
            str(tags))
    c.check("a value naming a pack and a practice holds each tag once",
            resolve_practices(["practice.memory", "foundation"], c.top) == ["practice.memory", "practice.land"])
    row = '[[pack]]\nname = "{}"\nkind = "language"\npractices = {}\ndescription = "x"\n'
    c.write_file(table, shipped + "\n" + row.format("loose", '["practice.nosuch"]'))
    reds = check_packs(c.top)[1]
    c.check("a pack naming practice.nosuch reds", any("practice.nosuch" in r for r in reds), str(reds))
    c.write_file(table, shipped + "\n" + row.format("land", '["practice.land"]'))
    reds = check_packs(c.top)[1]
    c.check("a pack named as a practice reds", any("equals a practice" in r for r in reds), str(reds))


def run_show(root, verb, tag, slice_="leaf") -> tuple[int, str]:
    import gov_tag
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        rc = gov_tag.run_kit_verb(root, verb, tag, sets={"tags.slice": slice_},
                                  kit_rel=iu.derive_tool_rel(KIT_DIR.name))
    return rc, out.getvalue()


def arm_retired_rows(c):
    import edge_grammar
    import gov_tag
    import tag_index
    rows = "\n".join(derive_fx_row(t, f"MUST {t}.") for t in ("unit.old", "unit.both", "unit.b1", "unit.b2"))
    root = build_tree(c, GUARD_POINT, rows=rows, instructions_edit=FOR_ALL_VALUE)
    target = ("--manifest", "corekit")
    run_cli(root, "rename", *target, "--tag", "unit.old", "--successor", "unit.new", *FX_RECORD)
    run_cli(root, "split", *target, "--tag", "unit.both", "--successor", "unit.b1,unit.b2", *FX_RECORD)
    rc, said = run_cli(root, "add", "--manifest", "corekit", "--tag", "unit.seeded", "--type", "directive", "--level", "3",
                       "--trigger", "always", "--text", "MUST seed.", "--promoted-from", "unit.b1", *FX_RECORD)
    record = read_change_at(root, said)
    iu.run_commit(root, "the writes")
    for slice_ in ("leaf", "subtree"):
        rc, said = run_show(root, "show", "unit.old", slice_)
        c.check(f"show unit.old under {slice_} exits 0 with its retired row",
                rc == 0 and "· retired" in said and "**Successor:** unit.new" in said, said)
    rc, said = run_show(root, "where", "unit.old")
    c.check("where unit.old exits 1: a retired tag resolves as live nowhere", rc == 1, said)
    rc, said = run_show(root, "show", "unit.both")
    c.check("a split's row lists both successors", "**Successor:** unit.b1,unit.b2" in said, said)
    gov_tag.write_commit(root, {"memory/guides/ALPHA.md": gov_tag.GUIDE + "\nsee `unit.old`\n"}, "cite a retired tag")
    reds = run_tag_check(root)
    c.check("new text citing unit.old reds the tag check", any("new text cites retired unit.old" in r for r in reds),
            str(reds))
    rel = f"memory/builds/{FX_BUILD}/build/2026-01-01-build-{FX_UNIT}-change-3.md"
    edges = edge_grammar.read_change_edges(record, rel)
    c.check("read_change_edges returns the promoted-from edge at site instructions.edit",
            [(e["type"], e["site"], e["targets"]) for e in edges] == [("promoted-from", "instructions.edit", ["unit.b1"])],
            str(edges))
    types, spaces = edge_grammar.read_edge_types(), tag_index.read_namespaces(KIT_DIR / "namespaces.toml")
    reds = edge_grammar.check_edges(edges, types, spaces)
    c.check("check_edges grades it clean", not reds, str(reds))
    planted = edge_grammar.read_section_edges("**Edges:** promoted-from=unit.b1\n", rel)
    reds = edge_grammar.check_edges(planted, types, spaces)
    c.check("the same edge at a section reds as written outside instructions.edit",
            any("written by instructions.edit" in r for r in reds), str(reds))


PLANTS = {"merge": arm_merge, "merge-multiline": arm_merge_multiline, "merge-same-add": arm_merge_same_add,
          "merge-policy": arm_merge_policy, "merge-parse": arm_merge_parse, "merge-cut": arm_merge_cut,
          "merge-unterminated": arm_merge_unterminated, "merge-moved": arm_merge_moved,
          "merge-written": arm_merge_written, "root-prefix": arm_root_prefix,
          **{name: functools.partial(arm_merge_edit, name=name)
             for name in ("merge-both-edit", "merge-delete-edit", "merge-edit-delete")},
          **{name: functools.partial(arm_merge_one_side, name=name)
             for name in ("merge-theirs-delete", "merge-both-delete", "merge-theirs-add")},
          "propose": arm_propose, "owner-propose": arm_owner_propose, "rerender": arm_rerender,
          "command-for-all": arm_command_for_all, "flow-only": arm_flow_only, "proof-values": arm_proof_values,
          "guard": arm_guard, "checks": arm_checks, "record": arm_record, "packs": arm_packs,
          "retired-rows": arm_retired_rows}


def run_fixture(plant=None) -> tuple[list, int]:
    """Each case in a throwaway repository under the system temp directory, the caller's git variables aside."""
    from deviation_join import remove_tree, set_env_aside
    from tree_lib import GIT_ENV_LEAKS
    out, failed = [], 0
    for name in [plant] if plant else list(PLANTS):
        top = pathlib.Path(tempfile.mkdtemp(prefix="edit-fx-"))
        try:
            with set_env_aside(GIT_ENV_LEAKS):
                iu.run_git(top, "init", "-q")
                case = iu.Case(top, out)
                out.append(f"{SAY}: fixture · plant {name}")
                PLANTS[name](case)
                failed += case.failed
        finally:
            remove_tree(top)
    out.append(f"{SAY}: fixture · {'FAILED' if failed else 'green'} · {failed} expectation(s) failed")
    return out, 1 if failed else 0


# ------------------------------------------------------------------------------------------ the verbs

def add_write_flags(ap, verb):
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--tag", required=True)
    for key in ROW_ORDER[1:]:
        many = key in iu.UNIT_LISTS or key == "enforced-by"
        flag = "--help-text" if key == "help" else f"--{key}"
        ap.add_argument(flag, dest=key.replace("-", "_"), action="append" if many else "store")
    ap.add_argument("--build")
    ap.add_argument("--unit")
    ap.add_argument("--mark")
    if verb in ("rename", "split"):
        ap.add_argument("--successor")
    if verb == "add":
        ap.add_argument("--promoted-from")


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="instructions_edit.py", description=__doc__.split("\n\n")[0], allow_abbrev=False)
    sub = ap.add_subparsers(dest="verb", required=True)
    proposing = sub.add_parser("propose", allow_abbrev=False).add_subparsers(dest="write_verb", required=True)
    for verb in WRITE_VERBS:
        add_write_flags(sub.add_parser(verb, allow_abbrev=False), verb)
        add_write_flags(proposing.add_parser(verb, allow_abbrev=False), verb)
    sub.add_parser("list").add_argument("--manifest")
    sub.add_parser("render")
    sub.add_parser("check")
    sub.add_parser("fixture").add_argument("--plant")
    return ap


def run_verb(argv, root=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.verb == "fixture":
            if args.plant is not None and args.plant not in PLANTS:
                raise Refused(2, f"{SAY}: no plant {args.plant!r}; the plants are {', '.join(PLANTS)}")
            lines, rc = run_fixture(args.plant)
        else:
            root = root or resolve_root()
            load = read_load(root)
            if args.verb in WRITE_VERBS:
                lines, rc = run_write(root, args.verb, args, argv[1:], load)
            elif args.verb == "propose":
                lines, rc = run_propose(root, args.write_verb, args, argv[2:])
            elif args.verb == "list":
                lines, rc = run_list(root, args.manifest)
            elif args.verb == "render":
                lines, rc = run_render(root)
            else:
                lines, rc = run_check(root)
    except Refused as exc:
        lines, rc = exc.lines, exc.code
    except (ValueError, OSError, RuntimeError) as exc:   # UnitRowError, the git reader's LevelError, Unreadable's kin
        lines, rc = [f"{SAY}: red · {exc}"], 1
    print("\n".join(lines))
    return rc


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    return run_verb(sys.argv[1:] if argv is None else argv)


if __name__ == "__main__":
    sys.exit(main())
