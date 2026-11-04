#!/usr/bin/env python3
"""core.py — the core that cannot be built around (PLAY-dOrderedCharter-7, principle P16).

    python core.py meta-check            every principle joined both ways to what enforces it
    python core.py kinds [skill|practice]  the conformance-gate contract, or one kind's population gate
    python core.py new <kind> <name> ...   the kind row's factory
    python core.py exceptions            the exception register under `core.exceptions`
    python core.py fixture [--plant <case>]  the plants, each in a throwaway repository

THE REGISTRIES, beside this file: `principles.toml` (one `[[principle]]` row per design principle, fixed),
`kinds.toml` (one `[[kind]]` row per extension kind: `tag`, `owner`, `binds`, `population`, `factory`, `gate`),
`core-pending.txt` (the shrink-only pending list, `<principle|practice|leg|kind> TAB <name> TAB <arming build>`)
and `practices.toml` (the practice catalogue, `unarmed` until it lands). A leg of `<prefix>/gate-legs.json`
names what it enforces in `enforces`, each a `principle.*` or `practice.*` tag.

META-CHECK joins through memory-tree's `compute_coverage`, the join factory the tag resolver joins through: a
principle no leg's `enforces` and no kind's `binds` names is red, a tag no registry row holds is red, a leg
carrying no `enforces` is red, each excused only by a pending row, and a pending row whose item is enforced
is red as stale. The registry is read against the `P<n>` heads of the design record's `[principles]`, the
conf's `DESIGN_RECORD`, both ways. Under `core.bypass` `never`, a leg whose `enforces` is non-empty and which
carries a `guard` is red, so no leg guard can skip a core check. Every run prints each pending count.

KINDS reds a kind row outside the `kind` namespace, a `binds` tag no registry row holds, a pending row naming
a kind the register lacks, and, for a kind off the pending list, a factory naming no file or a gate naming no
leg whose `enforces` holds every tag of the kind's `binds`; a pending kind that conforms is red as stale.
`kinds skill` and `kinds practice` are the two population gates this unit owns.

THE EXCEPTION REGISTER is memory-tree's exception records (`build_records.py`), read by every core gate: a red
whose principle and part an admitted record names prints `excepted`, naming the record. `core.exceptions`:
`any-session-recorded` admits every well-formed record; `owner-only-expiring` reds a record with no
`Expires` or an expired one, and admits only one written under PLAY-dOrderedCharter-15's owner proof, which
no record carries before that check lands, so it admits none; `none` admits none and reds every record.
Both keys are read through `policy_value.read_policy_value`, the root's committed policy at its landed
revision; a refused read is red naming the key, and no check runs on a guessed value.

Exit 0 green, 1 red, 2 a usage refusal.
"""
from __future__ import annotations

import datetime
import json
import os
import pathlib
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))
from policy_value import PolicyRefused, read_policy_value, resolve_kit_dir  # noqa: E402
from tag_index import SEG_RE  # noqa: E402  the tag grammar's one segment rule

SAY = "core"
CORE = "principle.p16"                 # the principle every structural red of the core is a red of
PENDING_KEYS = ("principle", "practice", "leg", "kind")
SKILL_DESCRIPTION_MAX = 1024
PRACTICE_LINE_MAX = 200
OWN_FACTORY = re.compile(r"core\.py new (?P<kind>[a-z-]+)$")


class CoreRefused(Exception):
    """A registry that cannot be read: red, naming the file."""


def load_memory_tree():
    """memory-tree's `coverage_join`, `build_records` and `design_lib`, reached through the inline
    `resolve_kit_dir`, never a spelled sibling path."""
    try:
        mt = resolve_kit_dir("memory-tree", "coverage_join.py", KIT_DIR)
    except LookupError as exc:
        raise CoreRefused(f"the core joins through memory-tree's coverage_join.py: {exc}") from None
    if str(mt) not in sys.path:
        sys.path.append(str(mt))
    import build_records
    import coverage_join
    import design_lib
    return coverage_join, build_records, design_lib


# ------------------------------------------------------------------------------------------- readers
def read_toml_rows(path, table):
    """The `[[table]]` rows of a TOML file, or None where the file is absent."""
    try:
        data = tomllib.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise CoreRefused(f"{pathlib.Path(path).name} does not parse: {exc}") from None
    rows = data.get(table) or []
    return [r for r in rows if isinstance(r, dict)]


def read_legs(root, prefix):
    try:
        legs = json.loads(pathlib.Path(root, prefix, "gate-legs.json").read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, ValueError) as exc:
        raise CoreRefused(f"gate-legs.json does not parse: {exc}") from None
    return [r for r in legs if isinstance(r, dict) and isinstance(r.get("name"), str)]


def read_pending(path):
    """-> ({key: {name: arming build}}, reds) from the pending list, or (None, []) where it is absent."""
    try:
        text = pathlib.Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return None, []
    rows, reds = {k: {} for k in PENDING_KEYS}, []
    for n, ln in enumerate(text.splitlines(), 1):
        if not ln.strip() or ln.startswith("#"):
            continue
        cells = ln.split("\t")
        if len(cells) != 3 or cells[0] not in PENDING_KEYS or not cells[1] or not cells[2]:
            reds.append((CORE, f"pending row {n}", f"core-pending.txt row {n} is not <{'|'.join(PENDING_KEYS)}>"
                         f" TAB <name> TAB <arming build>: {ln!r}"))
            continue
        if cells[1] in rows[cells[0]]:
            reds.append((CORE, f"pending row {n}", f"core-pending.txt row {n} repeats {cells[0]} {cells[1]}"))
        rows[cells[0]][cells[1]] = cells[2]
    return rows, reds


def derive_layout(root=None):
    """(repo root, the kit's repo-relative dir, the tool root) of this install, or of `root`'s fixture."""
    if root is not None:
        return pathlib.Path(root), "tools/playbook", "tools"
    top = next((d for d in (KIT_DIR, *KIT_DIR.parents) if (d / ".git").exists()), None)
    if top is None:
        raise CoreRefused(f"no work tree above {KIT_DIR.as_posix()}")
    kit_rel = KIT_DIR.relative_to(top).as_posix()
    return top, kit_rel, pathlib.PurePosixPath(kit_rel).parent.as_posix()


def read_value(root, key):
    """One core key's value; PolicyRefused names the key and the reader's line."""
    if key == "core.bypass":
        return read_policy_value("core.bypass", root)[0][0]
    return read_policy_value("core.exceptions", root)[0][0]


def derive_tag_reds(tag, ns, what):
    if not isinstance(tag, str) or not tag.startswith(ns + ".") or not all(
            SEG_RE.fullmatch(s) for s in tag.split(".")[1:]) or tag.count(".") != 1:
        return [(CORE, str(tag), f"{what} {tag!r} is outside the {ns} namespace: a tag is {ns}.<seg>")]
    return []


# --------------------------------------------------------------------------------------- exceptions
def derive_admission(record, value, today):
    """-> ('admitted' | 'not admitted' | 'red', why) for one exception record under `core.exceptions`."""
    if record["malformed"]:
        return "red", "malformed: " + "; ".join(f"{k} {w}" for k, w in record["malformed"])
    if value == "none":
        return "red", "core.exceptions is none, so no record is admitted and every record is red"
    if value == "owner-only-expiring":
        expires = record.get("expires")
        if not expires:
            return "red", "carries no **Expires:**, which owner-only-expiring requires"
        if expires <= today:
            return "red", f"expired on {expires}"
        return "not admitted", ("written without the owner proof: PLAY-dOrderedCharter-15's check has not "
                                "landed, so no record carries it")
    return "admitted", "any-session-recorded admits every well-formed record"


def read_register(root, value, today=None):
    """-> ([(record, state, why)], admitted {(principle, part): record id})."""
    _cov, build_records, _dl = load_memory_tree()
    today = today or datetime.date.today().isoformat()
    out, admitted = [], {}
    for record in build_records.read_exceptions(root):
        state, why = derive_admission(record, value, today)
        out.append((record, state, why))
        if state == "admitted":
            admitted.setdefault((record["principle"], record["excuses"]), record["id"])
    return out, admitted


def check_exceptions(root, reds, lines):
    """Read `core.exceptions`, print each excused red as `excepted` and every register red. -> rc."""
    try:
        value = read_value(root, "core.exceptions")
    except PolicyRefused as exc:
        lines.append(f"{SAY}: refused · core.exceptions · {exc.line} · no core check runs on a guessed value")
        return 1
    register, admitted = read_register(root, value)
    rc = 0
    for principle, part, text in reds:
        rid = admitted.get((principle, part))
        if rid:
            lines.append(f"{SAY}: excepted · {text} · by {rid}")
        else:
            lines.append(f"{SAY}: red · {text}")
            rc = 1
    for record, state, why in register:
        if state == "red":
            lines.append(f"{SAY}: red · exception {record['path']} · {why}")
            rc = 1
    return rc


def run_exceptions(root=None):
    root, _kit_rel, _prefix = derive_layout(root)
    try:
        value = read_value(root, "core.exceptions")
    except PolicyRefused as exc:
        return [f"{SAY}: refused · core.exceptions · {exc.line}"], 1
    register, _ = read_register(root, value)
    lines = [f"{SAY}: exceptions · core.exceptions is {value} · {len(register)} records"]
    for record, state, why in register:
        lines.append(f"{SAY}: exception {record['path']} · {record['principle'] or '?'} · excuses "
                     f"{record['excuses'] or '?'} · {state} · {why}")
    return lines, 1 if any(s == "red" for _r, s, _w in register) else 0


# --------------------------------------------------------------------------------------- meta-check
def read_design_heads(root, design_lib):
    """-> (the design record's `P<n>` heads as ids, its path), or (None, why) where none is named."""
    rel = (design_lib.read_design_conf(root).get("DESIGN_RECORD") or "").strip()
    if not rel:
        return None, "DESIGN_RECORD is blank in .memory-tree.conf, so the registry is read against no design"
    try:
        text = pathlib.Path(root, rel).read_text(encoding="utf-8").replace("\r\n", "\n")
    except OSError as exc:
        raise CoreRefused(f"the design record {rel} cannot be read: {exc}") from None
    if "\n## [principles]" not in text:
        raise CoreRefused(f"the design record {rel} holds no ## [principles] section")
    sec = text.split("\n## [principles]", 1)[1].split("\n## ", 1)[0]
    return {f"P{n}" for n in re.findall(r"^- \*\*P(\d+) ", sec, re.M)}, rel


def run_meta_check(root=None):
    root, kit_rel, prefix = derive_layout(root)
    lines, reds = [], []
    try:
        bypass = read_value(root, "core.bypass")
    except PolicyRefused as exc:
        return [f"{SAY}: refused · core.bypass · {exc.line} · no core check runs on a guessed value"], 1
    try:
        cov, _br, design_lib = load_memory_tree()
        kit = pathlib.Path(root, kit_rel)
        principles = read_toml_rows(kit / "principles.toml", "principle")
        kinds = read_toml_rows(kit / "kinds.toml", "kind")
        practices = read_toml_rows(kit / "practices.toml", "practice")
        legs = read_legs(root, prefix)
        pending, pending_reds = read_pending(kit / "core-pending.txt")
        for name, have in (("principles.toml", principles), ("kinds.toml", kinds), ("core-pending.txt", pending),
                           (f"{prefix}/gate-legs.json", legs)):
            if have is None:
                raise CoreRefused(f"{name} is absent, so nothing is joined")
        heads, design = read_design_heads(root, design_lib)
    except CoreRefused as exc:
        return [f"{SAY}: red · {exc}"], 1
    reds += pending_reds
    ids = {}
    for row in principles:
        reds += derive_tag_reds(row.get("tag"), "principle", "principle row")
        pid = row.get("id")
        if not (isinstance(pid, str) and row.get("tag") == f"principle.{str(pid).lower()}"):
            reds.append((CORE, str(row.get("tag")), f"principle row {row.get('tag')!r}: its id {pid!r} is not "
                                                    "the P<n> its tag names"))
        if not isinstance(row.get("line"), str) or not row["line"].strip() or "\n" in row["line"]:
            reds.append((CORE, str(row.get("tag")), f"principle row {row.get('tag')!r}: its line is not one line"))
        ids[pid] = row.get("tag")
    if heads is None:
        lines.append(f"{SAY}: registry · {design}")
    else:
        reds += [(CORE, ids[p], f"registry row {p} is no P<n> head of {design}'s [principles]: an amendment "
                                f"the owner did not ratify, or the design dropped it") for p in sorted(set(ids) - heads)]
        reds += [(CORE, f"principle.{p.lower()}", f"{p} heads {design}'s [principles] and no registry row "
                                                  f"holds it: add its [[principle]] row") for p in sorted(heads - set(ids))]
        lines.append(f"{SAY}: registry · {len(ids)} rows against {len(heads)} principles of {design}")
    enforced = {}
    for leg in legs:
        tags = leg.get("enforces")
        if tags is None:
            continue
        if not isinstance(tags, list) or not tags or not all(isinstance(t, str) for t in tags):
            reds.append((CORE, leg["name"], f"leg {leg['name']!r}: enforces is not a non-empty list of tags"))
            continue
        for t in tags:
            ns = t.split(".")[0]
            if ns not in ("principle", "practice"):
                reds.append((CORE, leg["name"], f"leg {leg['name']!r} enforces {t}, outside principle.* and practice.*"))
            enforced.setdefault(ns, set()).add(t)
        if bypass == "never" and leg.get("guard"):
            reds.append((CORE, leg["name"], f"leg {leg['name']!r} enforces {', '.join(tags)} and carries a guard, "
                                            "and core.bypass is never: no leg guard may skip a core check"))
    bound = {t for k in kinds for t in (k.get("binds") or []) if isinstance(t, str)}
    owners = {"leg enforces": {"principle": tuple(sorted(enforced.get("principle", ()))),
                               "practice": tuple(sorted(enforced.get("practice", ())))},
              "kind binds": {"principle": tuple(sorted(t for t in bound if t.startswith("principle."))),
                             "practice": tuple(sorted(t for t in bound if t.startswith("practice.")))}}
    inventories = {"principle": sorted(t for t in ids.values() if isinstance(t, str))}
    if practices is None:
        lines.append(f"{SAY}: practice · unarmed: {kit_rel}/practices.toml is absent, so no practice is joined")
        owners = {o: {"principle": c["principle"]} for o, c in owners.items()}
    else:
        inventories["practice"] = sorted(r["tag"] for r in practices if isinstance(r.get("tag"), str))
    inventories["leg"] = sorted({leg["name"] for leg in legs})
    owners["leg enforces"]["leg"] = tuple(sorted(leg["name"] for leg in legs if leg.get("enforces")))
    baseline = {k: tuple(sorted(pending[k])) for k in ("principle", "practice", "leg")}
    got = cov.compute_coverage(inventories, owners, baseline)
    for ns, missing in got.unclaimed.items():
        for item in missing:
            if ns == "leg":
                reds.append((CORE, item, f"leg {item!r} carries no enforces and no pending row: name the "
                                         "principles it enforces, or a leg row with its arming build"))
            else:
                reds.append((item if ns == "principle" else CORE, item,
                             f"{item}: no leg's enforces and no kind's binds names it, and no pending row "
                             f"excuses it: a leg enforcing it, or a {ns} row naming the build that arms it"))
    for ns, stale in got.stale_claims.items():
        for claim in stale:
            owner, _, tag = claim.partition(": ")
            reds.append((CORE, tag, f"{tag}: a {owner} tag no {ns} row holds"))
    for ns, stale in got.stale_baseline.items():
        for item in stale:
            reds.append((CORE, item, f"pending {ns} row {item} names no {ns} of the tree: delete the row"))
    for ns, lazy in got.lazy_baseline.items():
        for item in lazy:
            reds.append((CORE, item, f"pending {ns} row {item} is stale: it is enforced now, so delete the row "
                                     f"(armed by {pending[ns][item]})"))
    lines.append(f"{SAY}: pending · " + " · ".join(f"{k} {len(pending[k])}" for k in PENDING_KEYS))
    rc = check_exceptions(root, reds, lines)
    lines.append(f"{SAY}: meta-check · {'red' if rc else 'green'} · {len(ids)} principles, {len(legs)} legs, "
                 f"{len(kinds)} kinds · core.bypass {bypass}")
    return lines, rc


# -------------------------------------------------------------------------------------------- kinds
def derive_command_file(root, prefix, command):
    """The repo-relative script a factory command runs, its `{prefix}` resolved, or None."""
    words = shlex.split(command.replace("{prefix}", prefix))
    return next((w for w in words if w.endswith((".py", ".sh", ".js"))), None)


def check_kind_row(root, prefix, row, legs, principle_tags):
    """-> (reds, conforms): a non-pending kind's contract, `conforms` true where factory and gate hold."""
    tag, reds = row.get("tag"), []
    for t in row.get("binds") or []:
        if t not in principle_tags:
            reds.append((CORE, tag, f"{tag} binds {t}, which no principle row holds"))
    factory, gate = row.get("factory") or "", row.get("gate") or ""
    script = derive_command_file(root, prefix, factory) if factory else None
    if not script or not pathlib.Path(root, script).is_file():
        reds.append((CORE, tag, f"{tag}: its factory {factory!r} names no file of the tree"))
    leg = next((g for g in legs if g["name"] == gate), None)
    if leg is None:
        reds.append((CORE, tag, f"{tag}: its gate {gate!r} names no leg of gate-legs.json"))
    else:
        lack = sorted(set(row.get("binds") or []) - set(leg.get("enforces") or []))
        if lack:
            reds.append((CORE, tag, f"{tag}: its gate leg {gate!r} does not enforce {', '.join(lack)} of its binds"))
    return reds, not reds


def run_kinds(root=None):
    root, kit_rel, prefix = derive_layout(root)
    lines, reds = [], []
    try:
        kit = pathlib.Path(root, kit_rel)
        kinds = read_toml_rows(kit / "kinds.toml", "kind")
        principles = read_toml_rows(kit / "principles.toml", "principle")
        legs = read_legs(root, prefix)
        pending, pending_reds = read_pending(kit / "core-pending.txt")
        for name, have in (("kinds.toml", kinds), ("principles.toml", principles), ("core-pending.txt", pending),
                           (f"{prefix}/gate-legs.json", legs)):
            if have is None:
                raise CoreRefused(f"{name} is absent, so no kind is graded")
    except CoreRefused as exc:
        return [f"{SAY}: red · {exc}"], 1
    reds += pending_reds
    principle_tags = {r.get("tag") for r in principles}
    seen = set()
    for row in kinds:
        tag = row.get("tag")
        reds += derive_tag_reds(tag, "kind", "kind row")
        if tag in seen:
            reds.append((CORE, str(tag), f"{tag} is registered twice"))
        seen.add(tag)
        for key in ("owner", "binds", "population", "factory", "gate"):
            if key not in row:
                reds.append((CORE, str(tag), f"{tag} carries no {key}"))
        row_reds, conforms = check_kind_row(root, prefix, row, legs, principle_tags)
        if tag in pending["kind"]:
            if conforms:
                reds.append((CORE, tag, f"pending kind row {tag} is stale: its factory and gate have landed, so "
                                        f"delete the row (armed by {pending['kind'][tag]})"))
        else:
            reds += row_reds
    for tag in sorted(set(pending["kind"]) - seen):
        reds.append((CORE, tag, f"{tag} is no kind the register holds: a kind outside kinds.toml cannot appear"))
    lines.append(f"{SAY}: kinds · {len(kinds)} registered, {len(pending['kind'])} pending")
    rc = check_exceptions(root, reds, lines)
    lines.append(f"{SAY}: kinds · {'red' if rc else 'green'}")
    return lines, rc


def read_front_matter(text):
    """A SKILL.md's front matter as {key: value}, a `>-` or `|` block folded to one line; None where absent."""
    lines = text.replace("\r\n", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    out, key = {}, None
    for ln in lines[1:]:
        if ln.strip() == "---":
            return out
        m = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(.*)$", ln)
        if m:
            key, value = m.group(1), m.group(2).strip()
            if value.startswith('"'):
                try:
                    value = json.loads(value)
                except ValueError:
                    pass
            out[key] = "" if value in (">", ">-", "|", "|-") else value
        elif key and ln.startswith((" ", "\t")):
            out[key] = (out[key] + " " + ln.strip()).strip()
    return None


def read_kind_row(root, kit_rel, kind):
    rows = read_toml_rows(pathlib.Path(root, kit_rel, "kinds.toml"), "kind") or []
    return next((r for r in rows if r.get("tag") == f"kind.{kind}"), None)


def run_skills(root=None):
    root, kit_rel, prefix = derive_layout(root)
    try:
        row = read_kind_row(root, kit_rel, "skill")
    except CoreRefused as exc:
        return [f"{SAY}: red · {exc}"], 1
    if row is None:
        return [f"{SAY}: red · kinds.toml holds no kind.skill row, so no Skill is graded"], 1
    glob = row.get("population", "").replace("{prefix}", prefix)
    home = pathlib.Path(root, glob.split("/*")[0])
    dirs = sorted(d for d in home.iterdir() if d.is_dir() and not d.name.startswith((".", "__"))) if home.is_dir() else []
    reds = []
    for d in dirs:
        rel = d.relative_to(root).as_posix()
        try:
            meta = read_front_matter((d / "SKILL.md").read_text(encoding="utf-8"))
        except FileNotFoundError:
            reds.append((CORE, rel, f"{rel}/ holds no SKILL.md"))
            continue
        if meta is None:
            reds.append((CORE, rel, f"{rel}/SKILL.md opens with no --- front matter"))
            continue
        name, desc = meta.get("name", ""), meta.get("description", "")
        if name != d.name:
            reds.append((CORE, rel, f"{rel}/SKILL.md names {name!r}, not its directory {d.name!r}"))
        elif not SEG_RE.fullmatch(name):
            reds.append((CORE, rel, f"{rel}/SKILL.md name {name!r} is outside [a-z0-9][a-z0-9-]*"))
        if not desc.strip():
            reds.append((CORE, rel, f"{rel}/SKILL.md has an empty description"))
        elif len(desc) > SKILL_DESCRIPTION_MAX:
            reds.append((CORE, rel, f"{rel}/SKILL.md description is {len(desc)} characters, over "
                                    f"{SKILL_DESCRIPTION_MAX}"))
    lines = [f"{SAY}: skills · {len(dirs)} Skills under {home.relative_to(root).as_posix()}/"]
    rc = check_exceptions(root, reds, lines)
    lines.append(f"{SAY}: skills conformance · {'red' if rc else 'green'}")
    return lines, rc


def run_practices(root=None):
    root, kit_rel, prefix = derive_layout(root)
    try:
        row = read_kind_row(root, kit_rel, "practice")
        if row is None:
            return [f"{SAY}: red · kinds.toml holds no kind.practice row, so no practice is graded"], 1
        rel = row.get("population", "").replace("{prefix}", prefix)
        rows = read_toml_rows(pathlib.Path(root, rel), "practice")
    except CoreRefused as exc:
        return [f"{SAY}: red · {exc}"], 1
    if rows is None:
        return [f"{SAY}: practices conformance · unarmed: {rel} is absent until PLAY-dOrderedCharter-1 writes it"], 0
    reds, seen = [], set()
    for r in rows:
        tag, line = r.get("tag"), r.get("line")
        reds += derive_tag_reds(tag, "practice", "practice row")
        if tag in seen:
            reds.append((CORE, str(tag), f"{tag} is catalogued twice"))
        seen.add(tag)
        if not isinstance(line, str) or not line.strip() or "\n" in line or "\r" in line:
            reds.append((CORE, str(tag), f"{tag}: its line is not one line"))
        elif len(line.encode("utf-8")) > PRACTICE_LINE_MAX:
            reds.append((CORE, str(tag), f"{tag}: its line is {len(line.encode('utf-8'))} bytes, over "
                                         f"{PRACTICE_LINE_MAX}"))
    lines = [f"{SAY}: practices · {len(rows)} rows in {rel}"]
    rc = check_exceptions(root, reds, lines)
    lines.append(f"{SAY}: practices conformance · {'red' if rc else 'green'}")
    return lines, rc


# ------------------------------------------------------------------------------------------ factories
def check_one_line(flag, value, limit):
    if not value or not value.strip() or "\n" in value or "\r" in value:
        raise ValueError(f"{flag} is one non-empty line")
    if len(value.encode("utf-8")) > limit:
        raise ValueError(f"{flag} is over {limit} bytes")


def write_skill(root, home, name, description):
    if not SEG_RE.fullmatch(name):
        raise ValueError(f"{name!r} is outside [a-z0-9][a-z0-9-]*")
    check_one_line("--description", description, SKILL_DESCRIPTION_MAX)
    d = pathlib.Path(root, home, name)
    if d.exists():
        raise ValueError(f"{d.relative_to(root).as_posix()}/ exists already")
    d.mkdir(parents=True)
    with open(d / "SKILL.md", "x", encoding="utf-8", newline="\n") as fh:
        fh.write(f"---\nname: {name}\ndescription: {json.dumps(description, ensure_ascii=False)}\n---\n\n# {name}\n")
    return (d / "SKILL.md").relative_to(root).as_posix()


def write_practice(root, rel, name, line):
    if not SEG_RE.fullmatch(name):
        raise ValueError(f"{name!r} is outside [a-z0-9][a-z0-9-]*")
    check_one_line("--line", line, PRACTICE_LINE_MAX)
    path = pathlib.Path(root, rel)
    rows = read_toml_rows(path, "practice")
    if rows and any(r.get("tag") == f"practice.{name}" for r in rows):
        raise ValueError(f"practice.{name} is catalogued already")
    text = path.read_text(encoding="utf-8") if path.is_file() else (
        "# practices.toml — the practice catalogue, the `practice` namespace's declaring source.\n")
    text = text.rstrip("\n") + f'\n\n[[practice]]\ntag = "practice.{name}"\nline = {json.dumps(line, ensure_ascii=False)}\n'
    path.write_bytes(text.encode("utf-8"))
    return rel


def run_new(argv, root=None):
    root, kit_rel, prefix = derive_layout(root)
    if len(argv) < 2:
        return [f"{SAY}: usage: core.py new <kind> <name> [factory flags]"], 2
    kind, name, rest = argv[0], argv[1], argv[2:]
    try:
        row = read_kind_row(root, kit_rel, kind)
        pending, _ = read_pending(pathlib.Path(root, kit_rel, "core-pending.txt"))
    except CoreRefused as exc:
        return [f"{SAY}: refused · {exc}"], 2
    if row is None:
        return [f"{SAY}: refused · kind.{kind} is no kind the register holds"], 2
    if pending and f"kind.{kind}" in pending["kind"] or not row.get("factory"):
        return [f"{SAY}: refused · kind.{kind}'s factory has not landed: {row.get('owner')} lands it"], 2
    own = OWN_FACTORY.search(row["factory"])
    try:
        if own and own.group("kind") == "skill":
            flags = dict(zip(rest[::2], rest[1::2]))
            if set(flags) != {"--description"} or len(rest) != 2:
                raise ValueError("new skill <name> --description <text>")
            home = row.get("population", "").replace("{prefix}", prefix).split("/*")[0]
            return [f"{SAY}: new · wrote {write_skill(root, home, name, flags['--description'])}"], 0
        if own and own.group("kind") == "practice":
            flags = dict(zip(rest[::2], rest[1::2]))
            if set(flags) != {"--line"} or len(rest) != 2:
                raise ValueError("new practice <name> --line <text>")
            rel = row.get("population", "").replace("{prefix}", prefix)
            return [f"{SAY}: new · appended practice.{name} to {write_practice(root, rel, name, flags['--line'])}"], 0
    except ValueError as exc:
        return [f"{SAY}: refused · {exc}"], 2
    words = shlex.split(row["factory"].replace("{prefix}", prefix))
    argv_ = [sys.executable if w in ("python", "python3") else w for w in words] + [name, *rest]
    p = subprocess.run(argv_, cwd=str(root), stdin=subprocess.DEVNULL)
    return [], p.returncode


# -------------------------------------------------------------------------------------------- fixture
FX_N = 16
FX_TAGS = [f"principle.p{n}" for n in range(1, FX_N + 1)]


def write_fixture(top, policy="# no key set\n"):
    """The base repository every plant mutates: 16 principles, all enforced, two conforming kinds, one
    pending kind, one Skill and no practice catalogue, committed on main."""
    files = {
        ".memory-tree.conf": 'MEMORY_ROOT="memory"\nDESIGN_RECORD="memory/design.md"\n',
        "memory/design.md": "# fixture design\n\n## [principles] What binds\n\n" + "".join(
            f"- **P{n} Fixture principle {n}.** Its text.\n" for n in range(1, FX_N + 1)) + "\n## [enforcement]\n",
        "memory/builds/dFx/README.md": "# dFx\n",
        "tools/playbook/core.py": "# the fixture's factory stand-in\n",
        "tools/playbook/principles.toml": "".join(
            f'[[principle]]\ntag = "principle.p{n}"\nid = "P{n}"\nline = "Fixture principle {n}."\nclauses = []\n\n'
            for n in range(1, FX_N + 1)),
        "tools/playbook/kinds.toml": (
            '[[kind]]\ntag = "kind.skill"\nowner = "dFx"\nbinds = ["principle.p15", "principle.p16"]\n'
            'population = "skills/*/SKILL.md"\nfactory = "python {prefix}/playbook/core.py new skill"\n'
            'gate = "fx skills"\n\n'
            '[[kind]]\ntag = "kind.practice"\nowner = "dFx"\nbinds = ["principle.p16"]\n'
            'population = "{prefix}/playbook/practices.toml"\n'
            'factory = "python {prefix}/playbook/core.py new practice"\ngate = "fx practices"\n\n'
            '[[kind]]\ntag = "kind.layer"\nowner = "dFx"\nbinds = ["principle.p16"]\npopulation = ""\n'
            'factory = ""\ngate = ""\n'),
        "tools/playbook/core-pending.txt": "# fixture pending list\nkind\tkind.layer\tdFx\n",
        "tools/gate-legs.json": json.dumps([
            {"name": "fx meta", "argv": ["python", "x.py"], "enforces": FX_TAGS},
            {"name": "fx skills", "argv": ["python", "x.py"], "enforces": ["principle.p15", "principle.p16"]},
            {"name": "fx practices", "argv": ["python", "x.py"], "enforces": ["principle.p16"]}], indent=1) + "\n",
        "skills/alpha/SKILL.md": "---\nname: alpha\ndescription: >-\n  The fixture's one Skill.\n---\n\n# alpha\n",
        ".governance/policy.toml": policy,
    }
    for rel, text in files.items():
        p = top / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))
    run_fixture_git(top, "init", "-q", "-b", "main")
    write_fixture_commit(top, "fixture base")


def run_fixture_git(top, *args):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(GIT_AUTHOR_NAME="fx", GIT_AUTHOR_EMAIL="fx@fx", GIT_COMMITTER_NAME="fx",
               GIT_COMMITTER_EMAIL="fx@fx")
    return subprocess.run(["git", "-C", str(top), "-c", "core.autocrlf=false", "-c", "commit.gpgsign=false",
                           *args], capture_output=True, text=True, env=env, stdin=subprocess.DEVNULL)


def write_fixture_commit(top, msg):
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "--no-verify", "--allow-empty", "-m", msg)


class Case:
    """One plant's run: each `check_gate` runs a gate over the fixture and records what it observed."""

    def __init__(self, top, out):
        self.top, self.out, self.failed = top, out, 0

    def write_file(self, rel, fn):
        p = self.top / rel
        old = p.read_text(encoding="utf-8") if p.exists() else None
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(fn(old).encode("utf-8"))
        return old

    def set_file(self, rel, old):
        p = self.top / rel
        if old is None:
            p.unlink(missing_ok=True)
        else:
            p.write_bytes(old.encode("utf-8"))

    def write_legs(self, fn):
        return self.write_file("tools/gate-legs.json", lambda t: json.dumps(fn(json.loads(t)), indent=1) + "\n")

    def write_policy(self, text):
        self.write_file(".governance/policy.toml", lambda _t: text)
        write_fixture_commit(self.top, "policy")

    def check_gate(self, label, gate, want_rc, *needles, absent=()):
        write_fixture_commit(self.top, label)
        lines, rc = gate(self.top)
        text = "\n".join(lines)
        missing = [n for n in needles if n not in text]
        present = [n for n in absent if n in text]
        ok = rc == want_rc and not missing and not present
        self.failed += not ok
        self.out.append(f"{SAY}: fixture · {label} · rc={rc} (want {want_rc})"
                        + (f" · names {', '.join(needles)}" if needles and not missing else "")
                        + ("" if ok else f" · FAILED, missing {missing} present {present}"))
        if not ok:
            self.out.extend("    " + ln for ln in lines)


def run_new_in(argv):
    return lambda top: run_new(argv, top)


def arm_registry(c):
    c.check_gate("registry: the control, the ids equal the design's heads both ways", run_meta_check, 0, "16 rows against 16")
    old = c.write_file("tools/playbook/principles.toml",
                 lambda t: t + '[[principle]]\ntag = "principle.p43"\nid = "P43"\nline = "Extra."\nclauses = []\n')
    c.write_legs(lambda legs: [dict(g, enforces=g["enforces"] + ["principle.p43"]) if g["name"] == "fx meta" else g
                         for g in legs])
    c.check_gate("registry: a planted extra P43 row", run_meta_check, 1, "registry row P43")
    c.set_file("tools/playbook/principles.toml", old)
    c.write_legs(lambda legs: [dict(g, enforces=FX_TAGS) if g["name"] == "fx meta" else g for g in legs])
    c.write_file("tools/playbook/principles.toml", lambda t: re.sub(
        r'\[\[principle\]\]\ntag = "principle\.p7"\n.*?clauses = \[\]\n\n', "", t, flags=re.S))
    c.write_legs(lambda legs: [dict(g, enforces=[t for t in g["enforces"] if t != "principle.p7"]) for g in legs])
    c.check_gate("registry: a planted missing P7 row", run_meta_check, 1, "P7 heads")
    c.set_file("tools/playbook/principles.toml", old)


def arm_unenforced(c):
    def derive_without(tag):
        return lambda legs: [dict(g, enforces=[t for t in g["enforces"] if t != tag]) for g in legs]
    restore = c.write_legs(derive_without("principle.p5"))
    c.check_gate("unenforced: principle.p5 named by no leg, no kind and no pending row", run_meta_check, 1,
             "principle.p5: no leg's enforces")
    c.set_file("tools/gate-legs.json", restore)
    c.check_gate("unenforced: its enforcing leg restored", run_meta_check, 0, "meta-check · green")
    c.write_legs(lambda legs: [dict(g, enforces=g["enforces"] + ["principle.p99"]) if g["name"] == "fx meta" else g
                         for g in legs])
    c.check_gate("unenforced: an enforces naming principle.p99", run_meta_check, 1, "principle.p99: a leg enforces tag")
    c.set_file("tools/gate-legs.json", restore)
    c.check_gate("unenforced: principle.p99 taken out", run_meta_check, 0, "meta-check · green")


def arm_pending(c):
    restore = c.write_legs(lambda legs: legs + [{"name": "fx bare", "argv": ["python", "x.py"]}])
    c.check_gate("pending: a leg with no enforces and no pending row", run_meta_check, 1, "leg 'fx bare' carries no enforces")
    old = c.write_file("tools/playbook/core-pending.txt", lambda t: t + "leg\tfx bare\tdFx\n")
    c.check_gate("pending: the leg's pending row excuses it, and the counts print", run_meta_check, 0,
             "pending · principle 0 · practice 0 · leg 1 · kind 1")
    c.set_file("tools/gate-legs.json", restore)
    c.write_file("tools/playbook/core-pending.txt", lambda _t: old + "principle\tprinciple.p3\tdFx\n")
    c.check_gate("pending: a pending row for an enforced principle", run_meta_check, 1,
             "pending principle row principle.p3 is stale", "pending · principle 1")
    c.set_file("tools/playbook/core-pending.txt", old)


def arm_kinds(c):
    c.check_gate("kinds: the control", run_kinds, 0, "kinds · green")
    old = c.write_file("tools/playbook/kinds.toml", lambda t: t.replace('gate = "fx skills"', 'gate = "fx nowhere"'))
    c.check_gate("kinds: a kind row whose gate names no leg", run_kinds, 1, "kind.skill: its gate 'fx nowhere' names no leg")
    c.set_file("tools/playbook/kinds.toml", old)
    restore = c.write_legs(lambda legs: [dict(g, enforces=["principle.p16"]) if g["name"] == "fx skills" else g
                                   for g in legs])
    c.check_gate("kinds: a gate leg whose enforces lacks a tag of the kind's binds", run_kinds, 1,
             "does not enforce principle.p15")
    c.set_file("tools/gate-legs.json", restore)
    oldp = c.write_file("tools/playbook/core-pending.txt", lambda t: t + "kind\tkind.widget\tdFx\n")
    c.check_gate("kinds: a kind.widget tag no register row holds", run_kinds, 1, "kind.widget is no kind the register holds")
    c.set_file("tools/playbook/core-pending.txt", oldp)


def arm_skill(c):
    c.check_gate("skill: new skill demo --description x", run_new_in(["skill", "demo", "--description", "x"]), 0,
             "wrote skills/demo/SKILL.md")
    c.check_gate("skill: the factory's Skill passes its gate", run_skills, 0, "skills conformance · green")
    c.write_file("skills/empty/SKILL.md", lambda _t: "---\nname: empty\ndescription:\n---\n")
    c.check_gate("skill: a planted Skill with an empty description", run_skills, 1, "skills/empty/SKILL.md has an empty")
    c.set_file("skills/empty/SKILL.md", None)
    c.write_file("skills/wrong/SKILL.md", lambda _t: "---\nname: other\ndescription: x\n---\n")
    c.check_gate("skill: a planted Skill whose name differs from its directory", run_skills, 1, "names 'other'")


def arm_practice(c):
    c.check_gate("practice: no catalogue reads unarmed", run_practices, 0, "unarmed")
    c.check_gate("practice: new practice demo --line x", run_new_in(["practice", "demo", "--line", "x"]), 0,
             "appended practice.demo")
    c.check_gate("practice: the factory's row passes its gate", run_practices, 0, "practices conformance · green")
    rel = "tools/playbook/practices.toml"
    old = c.write_file(rel, lambda t: t + '\n[[practice]]\ntag = "practice.two"\nline = """a\nb"""\n')
    c.check_gate("practice: a two-line line", run_practices, 1, "practice.two: its line is not one line")
    c.set_file(rel, old)
    c.write_file(rel, lambda t: t + '\n[[practice]]\ntag = "practice.demo"\nline = "again"\n')
    c.check_gate("practice: a repeated tag", run_practices, 1, "practice.demo is catalogued twice")


def run_door(c, *args):
    _cov, build_records, _dl = load_memory_tree()
    p = subprocess.run([sys.executable, build_records.__file__, "new", "exception", "--root", str(c.top),
                        "--build", "dFx", "--unit", "PLAY-dFx-1", *args], capture_output=True, text=True,
                       stdin=subprocess.DEVNULL)
    c.out.append(f"{SAY}: fixture · door · rc={p.returncode} · {(p.stdout or p.stderr).strip()}")
    return p.returncode


def arm_exception(c):
    c.write_legs(lambda legs: legs + [{"name": "fx bare", "argv": ["python", "x.py"]}])
    c.check_gate("exception: the red before any record", run_meta_check, 1, "red · leg 'fx bare'")
    run_door(c, "--principle", "principle.p16", "--excuses", "fx bare", "--reason", "the fixture's own")
    day = datetime.date.today().isoformat()
    rel = f"memory/builds/dFx/build/{day}-build-PLAY-dFx-1-exception-1.md"
    text = (c.top / rel).read_text(encoding="utf-8") if (c.top / rel).is_file() else ""
    fields = [f for f in ("Principle", "Excuses", "Reason", "Caused-by") if f"- **{f}:** " not in text]
    c.failed += bool(fields) or not text
    c.out.append(f"{SAY}: fixture · exception: the door wrote {rel} · "
                 + ("every field" if text and not fields else f"FAILED, missing {fields or 'the file'}"))
    c.check_gate("exception: the excused red prints excepted, naming the record", run_meta_check, 0,
             f"excepted · leg 'fx bare' carries no enforces", f"by {day}-build-PLAY-dFx-1-exception-1")
    c.write_file(f"memory/builds/dFx/build/{day}-build-PLAY-dFx-1-exception-2.md", lambda _t: (
        "# x\n\n**Serves:** exception PLAY-dFx-1\n\n- **Principle:** principle.p16\n- **Excuses:** fx other\n"
        "- **Caused-by:** PLAY-dFx-1\n"))
    c.check_gate("exception: a record missing Reason is red", run_meta_check, 1, "exception-2.md · malformed: Reason is missing")


def arm_exceptions_values(c):
    c.write_legs(lambda legs: legs + [{"name": "fx bare", "argv": ["python", "x.py"]}])
    b = "memory/builds/dFx/build/2026-01-01-build-PLAY-dFx-1-exception-"
    rec = ("# x\n\n**Serves:** exception PLAY-dFx-1\n\n- **Principle:** principle.p16\n- **Excuses:** fx bare\n"
           "- **Reason:** the fixture's own\n{}- **Caused-by:** PLAY-dFx-1\n")
    c.write_policy('core.exceptions = "owner-only-expiring"\n')
    c.write_file(b + "1.md", lambda _t: rec.format(""))
    c.check_gate("exceptions-values: owner-only-expiring reds a record with no Expires", run_meta_check, 1,
             "exception-1.md · carries no **Expires:**")
    c.write_file(b + "1.md", lambda _t: rec.format("- **Expires:** 2000-01-01\n"))
    c.check_gate("exceptions-values: owner-only-expiring reds an expired record", run_meta_check, 1, "expired on 2000-01-01")
    c.write_file(b + "1.md", lambda _t: rec.format("- **Expires:** 2999-12-31\n"))
    c.check_gate("exceptions-values: a record written without the owner proof is not admitted", run_meta_check, 1,
             "red · leg 'fx bare'", absent=("excepted",))
    c.check_gate("exceptions-values: the register names it not admitted", run_exceptions, 0, "not admitted")
    c.write_policy('core.exceptions = "none"\n')
    c.check_gate("exceptions-values: none reds every record and excuses nothing", run_meta_check, 1,
             "exception-1.md · core.exceptions is none", "red · leg 'fx bare'", absent=("excepted",))
    c.write_policy('core.exceptions = "any-session-recorded"\n')
    c.check_gate("exceptions-values: any-session-recorded admits it", run_meta_check, 0, "excepted · leg 'fx bare'")


def arm_bypass_never(c):
    c.write_legs(lambda legs: [dict(g, guard=["tools/playbook/"]) if g["name"] == "fx meta" else g for g in legs])
    c.write_policy('core.bypass = "never"\n')
    c.check_gate("bypass-never: a core leg carrying a guard under never", run_meta_check, 1,
             "leg 'fx meta' enforces", "core.bypass is never")
    c.write_policy('core.bypass = "with-hooks-report"\n')
    c.check_gate("bypass-never: the same leg under with-hooks-report", run_meta_check, 0, "core.bypass with-hooks-report")
    bad = pathlib.Path(tempfile.mkdtemp(prefix="core-fx-"))
    try:
        write_fixture(bad, policy='core.bypass = "sometimes"\n')
        inner = Case(bad, c.out)
        inner.check_gate("bypass-never: the only committed policy sets core.bypass sometimes", run_meta_check, 1,
                     "refused · core.bypass")
        c.failed += inner.failed
    finally:
        shutil.rmtree(bad, ignore_errors=True)


PLANTS = {"registry": arm_registry, "unenforced": arm_unenforced, "pending": arm_pending,
          "kinds": arm_kinds, "skill": arm_skill, "practice": arm_practice, "exception": arm_exception,
          "exceptions-values": arm_exceptions_values, "bypass-never": arm_bypass_never}


def run_fixture(plant=None):
    out, failed = [], 0
    for name in [plant] if plant else list(PLANTS):
        top = pathlib.Path(tempfile.mkdtemp(prefix="core-fx-"))
        try:
            write_fixture(top)
            case = Case(top, out)
            out.append(f"{SAY}: fixture · plant {name}")
            PLANTS[name](case)
            failed += case.failed
        finally:
            shutil.rmtree(top, ignore_errors=True)
    out.append(f"{SAY}: fixture · {'FAILED' if failed else 'green'} · {failed} expectation(s) failed")
    return out, 1 if failed else 0


def main(argv):
    verb, rest = (argv[0], argv[1:]) if argv else ("", [])
    try:
        if verb == "meta-check" and not rest:
            lines, rc = run_meta_check()
        elif verb == "kinds" and not rest:
            lines, rc = run_kinds()
        elif verb == "kinds" and rest in (["skill"], ["practice"]):
            lines, rc = (run_skills if rest == ["skill"] else run_practices)()
        elif verb == "new":
            lines, rc = run_new(rest)
        elif verb == "exceptions" and not rest:
            lines, rc = run_exceptions()
        elif verb == "fixture" and (not rest or (len(rest) == 2 and rest[0] == "--plant")):
            plant = rest[1] if rest else None
            if plant is not None and plant not in PLANTS:
                lines, rc = [f"{SAY}: no plant {plant!r}; the plants are {', '.join(PLANTS)}"], 2
            else:
                lines, rc = run_fixture(plant)
        else:
            lines, rc = [__doc__.split("\n\n")[1]], 2
    except CoreRefused as exc:
        lines, rc = [f"{SAY}: red · {exc}"], 1
    for line in lines:
        sys.stdout.buffer.write((line + "\n").encode("utf-8"))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
