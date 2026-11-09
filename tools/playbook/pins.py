#!/usr/bin/env python3
"""pins.py — pins and drift: each gov change record's mark checked, a repository's pinned edge walked
(PLAY-dOrderedCharter-33).

    python pins.py drift --target <repo> --gov <gov tree> --to <rev> [--from <rev>] --stale order|refuse|warn [--write]
    python pins.py --fixture [--plant <case>]     # the plants, each in a throwaway repository

THE MARK. `derive_change_mark` reads two texts of a unit `editorial` when, each folded by the pin
normaliser's whitespace rule, they are equal (whitespace), equal with every character outside letters,
digits and spaces removed (punctuation), or equal once `before`'s whole words are respelled through the
shipped `spelling-map.toml` (spelling); or when the record carries an owner's `**Ruling:**` that its
`Proof` shows (`tty-cli`, or a signed proof). Anything else is `semantic`. A change record holds pins, so
`check_change_mark` reads its `Before` text from the kit manifests at its commit's first parent and its
`After` text at its commit, and reds a pin the text does not hash to, a ruling no proof shows, and an
`editorial` mark the texts do not bear out, naming the record, the unit and the first differing word.

THE WALK. `derive_pin_state` follows gov's change records of a tag from the revision its pin names to its
current text: none or only editorial ones, `standing`; a semantic one, `stale`; a rename, `renamed` to its
successor with the pin kept; a split or a removal, `orphaned`. A pin no record reaches is held `stale`,
never standing; naming it is PLAY-dOrderedCharter-28's red.

THE DRIFT VERB. `run_unit_drift` reads the target's overlay at HEAD, walks every pinned edge against gov's
units at `--to`, checks every editorial record it walked, and prints one JSON object: `lines`, one per
pinned edge in the update's verdict shape and one `new-beside` line per gov unit new since `--from` at a
level and a selection an overlay unit holds; `orders`, each `{path, body}` with the order's whole text;
`refuse`; `reds`; `render`, the composed units; and `rows`, the row kinds the kinds register lists.
Under `order` a stale or orphaned edge files an order; under `warn` a stale edge is journaled under
`--write` to `.governance/journal/stale-edges.tsv` and an orphan files an order; under `refuse` either
holds the update and nothing is written. A stale edge renders gov's new text and the repository's unit;
an orphaned `amends` is held out, an orphaned `supersedes` renders alone. Exit 0, 1 held or red, 2 usage.

THE STEP GATE CLASS `unit`. `read_unit_members` returns every gov unit tag, `write_unit_plant` removes
one in a clone, and `read_change_successors` returns each tag a change record ends with a `Successor`.
"""
from __future__ import annotations

import dataclasses
import datetime
import functools
import json
import os
import pathlib
import re
import shutil
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import instruction_units as iu  # noqa: E402
import overlay as ov  # noqa: E402

SAY = "pins"
STALE_MODES = ("order", "refuse", "warn")
SPELLING_MAP = "spelling-map.toml"
JOURNAL = ".governance/journal/stale-edges.tsv"
RULING_PROOFS = re.compile(r"tty-cli|signed\b.*")
ROLE = "unit"


# ------------------------------------------------------------------------------------------ the mark

def fold_text(text) -> str:
    """The pin normaliser's whitespace rule: each whitespace run one space, the ends stripped."""
    return re.sub(r"\s+", " ", text or "").strip()


def strip_text(text) -> str:
    """The punctuation class's transform: every character outside letters, digits and spaces removed."""
    return fold_text("".join(ch for ch in fold_text(text) if ch.isalnum() or ch == " "))


def derive_change_mark(before, after, spelling, ruling) -> str:
    """S1: `editorial` where the two texts differ by whitespace, punctuation or a declared respelling of
    `before`, or where an admitted owner's `ruling` says so; `semantic` otherwise."""
    if ruling:
        return "editorial"
    b, a = fold_text(before), fold_text(after)
    if b == a or strip_text(b) == strip_text(a):
        return "editorial"
    respelled = re.sub(r"\w+", lambda m: (spelling or {}).get(m[0], m[0]), b)
    return "editorial" if strip_text(respelled) == strip_text(a) else "semantic"


def derive_first_difference(before, after) -> str:
    """The first word at which the two texts, punctuation stripped, differ: `before`'s, else `after`'s."""
    b, a = strip_text(before).split(), strip_text(after).split()
    for x, y in zip(b, a):
        if x != y:
            return x
    return (b[len(a):] or a[len(b):] or ["(none)"])[0]


def read_spelling_map(root) -> dict:
    """`{from: to}` of the shipped spelling map's `[[spelling]]` rows, whole words; empty where absent."""
    path = iu.derive_kit_file(root, SPELLING_MAP)
    if not path.is_file():
        return {}
    rows = tomllib.loads(path.read_text(encoding="utf-8")).get("spelling") or []
    return {r["from"]: r["to"] for r in rows if isinstance(r, dict) and isinstance(r.get("from"), str)
            and isinstance(r.get("to"), str)}


@functools.lru_cache(maxsize=None)
def read_rev_units(root, rev) -> dict:
    """`{tag: Unit}` of every kit manifest in `root`'s tree at `rev`, in path then row order."""
    prefix = iu.derive_kit_prefix()
    paths = sorted(p for p in iu.run_git(root, "ls-tree", "-r", "--name-only", "-z", rev).split("\0")
                   if p and iu.derive_manifest_kind(p, prefix) == "kit")
    out = {}
    for rel in paths:
        units, faults = iu.parse_unit_rows(iu.run_git(root, "show", f"{rev}:{rel}"), rel)
        if faults:
            raise iu.UnitRowError("\n".join(str(f) for f in faults))
        out.update({u.tag: u for u in units if u.tag})
    return out


@functools.lru_cache(maxsize=None)
def read_record_commit(root, path) -> tuple:
    """`(the commit adding the record at `path`, its first parent)`, each None where git has none."""
    commit = iu.run_git(root, "log", "--diff-filter=A", "--format=%H", "-1", "--", path).strip() or None
    if commit is None:
        return None, None
    parents = iu.run_git(root, "rev-list", "--parents", "-n", "1", commit).split()
    return commit, (parents[1] if len(parents) > 1 else None)


def read_pin_text(root, rev, pin):
    """The text of the unit a `<tag>@<hash8>` pin names at `rev`, and whether it hashes to the pin."""
    tag, _, want = (pin or "").partition("@")
    unit = read_rev_units(root, rev).get(tag) if rev and want else None
    text = None if unit is None else (unit.text or "")
    return text, text is not None and iu.derive_unit_pin(text) == want


def check_change_mark(root, record, spelling) -> list:
    """S1 over one change record: its pins against the manifests' texts, its ruling's proof, and an
    `editorial` mark against `derive_change_mark`. -> one red per fault."""
    rid, unit = record.get("id"), record.get("Unit")
    where = f"{SAY}: red · {rid} · {unit}"
    commit, parent = read_record_commit(str(root), record.get("path"))
    ruling, proof = record.get("Ruling"), record.get("Proof") or ""
    reds = []
    if ruling and not RULING_PROOFS.fullmatch(proof):
        reds.append(f"{where} · its ruling shows no proof (Proof: {proof or 'none'}) · remedy: record the "
                    f"ruling through instructions.edit's tty-cli or signed proof")
    if record.get("Mark") != "editorial":
        return reds
    if commit is None:
        return reds + [f"{where} · is not committed, so no text bears its editorial mark out"]
    before, b_ok = read_pin_text(str(root), parent, record.get("Before"))
    after, a_ok = read_pin_text(str(root), commit, record.get("After"))
    if not (b_ok and a_ok):
        return reds + [f"{where} · does not match its change: the manifests' texts hash to neither "
                       f"{record.get('Before')} at its commit's parent nor {record.get('After')} at its commit"]
    admitted = bool(ruling) and RULING_PROOFS.fullmatch(proof) is not None
    if derive_change_mark(before, after, spelling, admitted) == "semantic":
        reds.append(f"{where} · marked editorial, but the change is semantic at "
                    f"`{derive_first_difference(before, after)}` · remedy: mark it semantic, or declare the "
                    f"respelling in {SPELLING_MAP}")
    return reds


# ------------------------------------------------------------------------------------------ the walk

def derive_edge_pins(unit) -> list:
    """`(type, gov tag, hash8)` per pinned `amends` or `supersedes` target of an overlay unit."""
    out = []
    for kind, _, rest in (e.partition("=") for e in unit.edges):
        if kind in ov.EDGE_TYPES:
            out += [(kind, *t.partition("@")[::2]) for t in rest.split(",")]
    return out


def derive_pin_state(tag, pin, records, units) -> tuple:
    """S2: `(state, detail, walked)` of the edge pinned `tag@pin` against `units`, gov's current
    `{tag: Unit}`: `standing`; `stale` with the semantic records; `renamed` with the successor; `orphaned`
    with the successor list or `none`. `walked` is every record followed, oldest first."""
    current = {t: iu.derive_unit_pin(u.text or "") for t, u in units.items()}
    walked, renamed, cur_tag, cur_pin = [], None, tag, pin
    while current.get(cur_tag) != cur_pin:
        rec = next((r for r in records if r.get("Unit") == cur_tag and r.get("Before") == f"{cur_tag}@{cur_pin}"
                    and r not in walked), None)
        if rec is None:   # ponytail: a pin no record reaches is unit 28's red; held stale, never standing
            return "stale", [r for r in walked if r.get("Mark") == "semantic"], walked
        walked.append(rec)
        if rec.get("Action") in ("split", "remove"):
            return "orphaned", rec.get("Successor") or "none", walked
        cur_tag, _, cur_pin = (rec.get("After") or "").partition("@")
        if rec.get("Action") == "rename":
            renamed = cur_tag
    semantic = [r for r in walked if r.get("Mark") == "semantic"]
    if semantic:
        return "stale", semantic, walked
    return ("renamed", renamed, walked) if renamed else ("standing", None, walked)


# ------------------------------------------------------------------------------------------ the drift

def read_row_kinds(root) -> list:
    """The kinds register's rows carrying a `schema`, the row kinds an overlay may carry (PLAY-dOrderedCharter-35)."""
    path = iu.derive_kit_file(root, "kinds.toml")
    rows = tomllib.loads(path.read_text(encoding="utf-8")).get("kind") or [] if path.is_file() else []
    return [r for r in rows if isinstance(r, dict) and r.get("schema")]


def derive_edit_command(target, repo_tag, kind, gov_tag, pin) -> str:
    """The command that re-pins or re-points one edge, spelled at the target's own playbook install."""
    from policy_value import resolve_kit_dir
    try:
        kit = resolve_kit_dir("playbook", "instructions_edit.py", target).relative_to(pathlib.Path(target).absolute())
        tool = f"{kit.as_posix()}/instructions_edit.py"
    except (LookupError, ValueError):
        tool = "<playbook kit>/instructions_edit.py"
    return f"python {tool} edit --manifest overlay --tag {repo_tag} --edges {kind}={gov_tag}@{pin}"


def render_stale_order(edge, line, target_rev, old, new, command) -> str:
    """One order's whole text: its title, the target revision, the verdict line, gov's old and new text
    and the command. The title is the edge's own, never `render_row_order`'s."""
    kind, gov_tag, repo_tag, state = edge["kind"], edge["gov"], edge["repo"], edge["state"]
    return (f"# {repo_tag}'s {kind} edge on {gov_tag} is {state}\n\n"
            f"target revision {target_rev}\n\n{line.strip()}\n\n"
            f"gov's text at the pin:\n\n{old or '(not found)'}\n\n"
            f"gov's text now:\n\n{new or '(gov no longer ships the unit under this tag)'}\n\n"
            f"Re-pin it, or re-point it at a successor, once the repository's unit reads right against gov's:\n\n"
            f"    {command}\n")


def write_stale_journal(target, rows) -> None:
    """S3's `warn` journal: one tab-separated line per stale edge, appended."""
    path = pathlib.Path(target) / JOURNAL
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8", newline="\n") as fh:
        fh.writelines("\t".join(map(str, r)) + "\n" for r in rows)


def derive_new_beside(old_tags, units, overlay_units) -> list:
    """S6: one line per gov unit absent from `old_tags` whose level and selection an overlay unit holds."""
    lines = []
    for u in units.values():
        if u.tag in old_tags or u.level is None:
            continue
        beside = [o.tag for o in overlay_units if o.level == u.level and set(o.scope) & set(u.scope)]
        if beside:
            lines.append(f"  {'new-beside':<18} [{ROLE:<13}] {u.tag} at level {u.level} beside {', '.join(beside)}")
    return lines


def run_unit_drift(target, gov_root, from_rev, to_rev, stale, write) -> tuple:
    """S7: `(report, exit)` of the drift of `target`'s pinned edges against gov's units at `to_rev`."""
    if stale not in STALE_MODES:
        raise ValueError(f"--stale {stale!r} is none of {', '.join(STALE_MODES)}")
    target, gov_root = pathlib.Path(target), pathlib.Path(gov_root)
    kinds = read_row_kinds(gov_root)
    report = {"lines": [], "orders": [], "refuse": False, "reds": [], "render": [],
              # ponytail: the row pass is unit 35's composer; until a kind registers one, the count alone
              "rows": f"{len(kinds)} row kinds registered"}
    try:
        overlay = ov.read_overlay(target)
        units = read_rev_units(str(gov_root), to_rev)
        records = iu.read_change_records(gov_root) if overlay.units else []
    except (ov.OverlayRefused, iu.UnitRowError, iu.LevelError) as exc:
        report["reds"] += str(exc).splitlines()
        return report, 1
    if not overlay.units:
        return report, 0
    spelling, edges, checked = read_spelling_map(gov_root), [], set()
    target_rev = iu.run_git(target, "rev-parse", "HEAD").strip()
    for o in overlay.units:
        for kind, gov_tag, pin in derive_edge_pins(o):
            state, detail, walked = derive_pin_state(gov_tag, pin, records, units)
            for rec in walked:
                if rec["id"] not in checked:
                    checked.add(rec["id"])
                    report["reds"] += check_change_mark(gov_root, rec, spelling)
            edges.append({"unit": o, "kind": kind, "gov": gov_tag, "pin": pin, "repo": o.tag, "state": state,
                          "detail": detail, "walked": walked})
    journal = []
    for e in edges:
        o, kind, gov_tag, state = e["unit"], e["kind"], e["gov"], e["state"]
        landed = units.get(e["detail"] if state == "renamed" else gov_tag)
        now = iu.derive_unit_pin(landed.text or "") if landed else "none"
        if state == "stale":
            since = e["detail"][0]["Before"].partition("@")[2] if e["detail"] else e["pin"]
            line = f"  {'stale':<18} [{ROLE:<13}] {gov_tag} <- {e['repo']} (semantic since {since})"
        elif state == "orphaned":
            line = f"  {'orphaned':<18} [{ROLE:<13}] {gov_tag} <- {e['repo']} (successor: {e['detail']})"
        else:
            shown = "replaced" if kind == "supersedes" else "amended"
            moved = f" (renamed from {gov_tag}, pin kept)" if state == "renamed" else ""
            line = f"  {shown:<18} [{ROLE:<13}] {e['detail'] if moved else gov_tag} <- {e['repo']}{moved}"
        report["lines"].append(line)
        if state not in ("stale", "orphaned"):
            continue
        command = derive_edit_command(target, e["repo"], kind,
                                      gov_tag if state == "stale" else "<successor>", now if state == "stale" else e["pin"])
        if stale == "refuse":
            report["refuse"] = True
            report["lines"].append(f"  held · {e['repo']} <- {gov_tag}: instructions.stale = refuse · {command}")
        elif state == "orphaned" or stale == "order":
            first = e["walked"][0] if e["walked"] else None
            old = read_pin_text(str(gov_root), read_record_commit(str(gov_root), first["path"])[1],
                                f"{gov_tag}@{e['pin']}")[0] if first else None
            report["orders"].append({"path": f"{iu.OVERLAY}#{e['repo']}",
                                     "body": render_stale_order(e, line, target_rev, old,
                                                                landed.text if landed else None, command)})
        else:
            journal.append((datetime.date.today().isoformat(), target_rev, e["repo"], gov_tag, e["pin"], now, stale))
    if from_rev:
        old_tags = set(read_rev_units(str(gov_root), from_rev))
        report["lines"] += derive_new_beside(old_tags, units, overlay.units)
    if report["refuse"] or report["reds"]:
        return report, 1
    report["render"] = derive_drift_composition(target, gov_root, units, overlay.units, edges)
    if isinstance(report["render"], str):
        report["reds"].append(report["render"])
        report["render"] = []
        return report, 1
    if write and journal:
        write_stale_journal(target, journal)
    return report, 0


def derive_drift_composition(target, gov_root, units, overlay_units, edges):
    """The units the target composes with each walked edge applied: a rename re-pointed, a stale
    `supersedes` rendered beside gov's text, an orphaned `amends` held out and an orphaned `supersedes`
    alone. -> `[{tag, text}]`, or the refusal's text."""
    by_unit = {}
    for e in edges:
        by_unit.setdefault(e["repo"], []).append(e)
    placed = []
    for o in overlay_units:
        kept, drop = [], False
        for e in by_unit.get(o.tag, []):
            if e["state"] == "orphaned":
                drop = drop or e["kind"] == "amends"
                continue
            tag = e["detail"] if e["state"] == "renamed" else e["gov"]
            kind = "amends" if e["state"] == "stale" else e["kind"]
            kept.append(f"{kind}={tag}@{e['pin']}")
        plain = [x for x in o.edges if x.partition("=")[0] not in ov.EDGE_TYPES]
        if not drop:
            placed.append(dataclasses.replace(o, edges=tuple(plain + kept)))
    gov = list(units.values())
    try:
        composed, _states = ov.derive_unit_composition(
            gov, placed, ov.read_excluded_tags(target), fixed=ov.derive_fixed_units(gov, gov_root),
            policy_reader=ov.derive_policy_reader(target))
    except ov.OverlayRefused as exc:
        return str(exc)
    return [{"tag": u.tag, "text": u.text} for u in composed]


# ------------------------------------------------------------------------------------ the step gate class

def read_unit_members(root) -> set:
    """The `unit` class's reader: every gov unit tag of every kit's `instructions.toml` under `root`."""
    return {u.tag for u in iu.read_units(root) if u.tag}


def write_unit_plant(clone) -> str:
    """The `unit` class's plant: the clone's first gov unit row removed, staged. -> its member id."""
    units = iu.read_units(clone)
    if not units:
        raise ValueError("the unit plant found no gov unit row")
    u = units[0]
    path = pathlib.Path(clone) / u.path
    text = path.read_bytes().decode("utf-8")
    # ponytail: `read_units` reads with universal newlines, so a CRLF checkout holds the row as CRLF.
    body = u.body.replace("\n", "\r\n") if "\r\n" in text else u.body
    if body not in text:
        raise ValueError(f"the unit plant found no row {u.tag} in the bytes of {u.path}")
    path.write_bytes(text.replace(body, "", 1).encode("utf-8"))
    iu.run_git(clone, "add", "--", u.path)
    return f"unit:{u.tag}"


def read_change_successors(root) -> set:
    """The `unit` class's witness: each tag a change record ends with a `Successor`, `none` included."""
    iu.load_memory_tree_path()
    import build_records
    return {r["Unit"] for r in build_records.read_changes(root) if r.get("Unit") and r.get("Successor")}


# ------------------------------------------------------------------------------------------ the fixture

FX_MANIFEST = "tools/alpha/instructions.toml"
FX_BUILD, FX_UNIT, FX_TAG, FX_REPO = "tFx", "PLAY-tFx-1", "unit.push", "repo.push"


def render_gov_row(tag, text, level=3) -> str:
    return ov.render_fx_row(tag, level, text, **{"class": "open"})


def write_change_fx(c, tag, action, mark, before, after, successor=None, proof=None, ruling=None) -> str:
    """One change record through the kind's writer, `ruling` appended as its `**Ruling:**` line, staged."""
    iu.load_memory_tree_path()
    import build_records
    rel = build_records.write_change(c.top, FX_BUILD, FX_UNIT, tag, action, mark, before, after,
                                     proof or build_records.DOOR_PROOF, successor)
    if ruling:
        with open(c.top / rel, "a", encoding="utf-8", newline="\n") as fh:
            fh.write(f"- **Ruling:** {ruling}\n")
    iu.run_git(c.top, "add", "--", rel)
    return rel


def build_drift_gov(c, texts, edge="amends", repo_text="MUST also tell the team.", overlay=True):
    """Commit 1: gov's unit at `texts[0]` and, where `overlay`, the repository's unit pinned on it. Each
    later text is a commit of gov's manifest with an `editorial` or `semantic` record, `(text, mark)`."""
    c.write_file(".memory-tree.conf", 'MEMORY_ROOT=memory\nFAMILIES="play:PLAY"\n')
    c.write_file(f"memory/builds/{FX_BUILD}/README.md", "# the fixture build\n")
    c.write_file("tools/alpha/kit.toml", 'id = "alpha"\n')
    c.write_file(FX_MANIFEST, render_gov_row(FX_TAG, texts[0]))
    if overlay:
        pin = iu.derive_unit_pin(texts[0])
        c.write_file(iu.OVERLAY, ov.render_fx_row(FX_REPO, 3, repo_text, edges=[f"{edge}={FX_TAG}@{pin}"]))
    iu.run_commit(c.top, "release 1")
    for (before, _m), (after, mark) in zip([(texts[0], None), *texts[1:]], texts[1:]):
        c.write_file(FX_MANIFEST, render_gov_row(FX_TAG, after))
        write_change_fx(c, FX_TAG, "edit", mark, f"{FX_TAG}@{iu.derive_unit_pin(before)}",
                        f"{FX_TAG}@{iu.derive_unit_pin(after)}")
        iu.run_commit(c.top, f"release: {mark}")


def run_fx_drift(c, stale="order", write=False, from_rev=None) -> tuple:
    read_rev_units.cache_clear()
    read_record_commit.cache_clear()
    return run_unit_drift(c.top, c.top, from_rev, "HEAD", stale, write)


def arm_meaning_editorial(c):
    build_drift_gov(c, ["MUST never push to main.", ("MUST always push to main.", "editorial")])
    report, rc = run_fx_drift(c)
    said = "\n".join(report["reds"])
    c.check("a meaning change marked editorial exits 1 naming the record, the unit and `never`",
            rc == 1 and "-change-1" in said and FX_TAG in said and "`never`" in said, f"{rc} {report}")


def arm_punctuation_editorial(c):
    build_drift_gov(c, ["MUST verify then push.", ("MUST verify, then push;", "editorial")])
    report, rc = run_fx_drift(c)
    c.check("a comma added and a full stop made a semicolon pass as editorial",
            rc == 0 and not report["reds"] and not any("stale" in ln for ln in report["lines"]), f"{rc} {report}")


def arm_spelling(c):
    build_drift_gov(c, ["MUST mind the colour.", ("MUST mind the color.", "editorial")])
    report, rc = run_fx_drift(c)
    c.check("an undeclared respelling marked editorial exits 1", rc == 1 and "`colour`" in "\n".join(report["reds"]),
            f"{rc} {report}")
    c.write_file(f"tools/playbook/{SPELLING_MAP}", '[[spelling]]\nfrom = "colour"\nto = "color"\n')
    iu.run_commit(c.top, "the spelling row")
    report, rc = run_fx_drift(c)
    c.check("a declared respelling marked editorial exits 0", rc == 0 and not report["reds"], f"{rc} {report}")


def arm_ruling_unproven(c):
    texts = ("MUST never push to main.", "MUST always push to main.")
    build_drift_gov(c, [texts[0]])
    c.write_file(FX_MANIFEST, render_gov_row(FX_TAG, texts[1]))
    rel = write_change_fx(c, FX_TAG, "edit", "editorial", *[f"{FX_TAG}@{iu.derive_unit_pin(t)}" for t in texts],
                          ruling="the owner: this is editorial")
    iu.run_commit(c.top, "an unproven ruling")
    report, rc = run_fx_drift(c)
    c.check("a ruling with no proof marking a meaning change editorial exits 1",
            rc == 1 and "shows no proof" in "\n".join(report["reds"]), f"{rc} {report}")
    record = c.top / rel
    record.write_bytes(record.read_bytes().replace("none — stand-in door".encode("utf-8"), b"tty-cli"))
    iu.run_git(c.top, "add", "--", rel)
    iu.run_commit(c.top, "the ruling proven")
    report, rc = run_fx_drift(c)
    c.check("...the same ruling under a tty-cli proof is admitted", rc == 0 and not report["reds"], f"{rc} {report}")


def arm_editorial_behind(c):
    build_drift_gov(c, ["MUST tell the team.", ("MUST  tell the team.\n", "editorial"),
                        ("MUST tell the team;", "editorial")])
    report, rc = run_fx_drift(c)
    texts = [r["text"] for r in report["render"]]
    c.check("two editorial records past the pin print no stale line",
            rc == 0 and not any("stale" in ln for ln in report["lines"]) and "amended" in report["lines"][0],
            f"{rc} {report}")
    c.check("...and compose gov's new text then the repository's",
            texts == ["MUST tell the team;", "MUST also tell the team."], str(texts))


def arm_semantic_behind(c):
    build_drift_gov(c, ["MUST tell the team.", ("MUST tell nobody.", "semantic")])
    journal = c.top / JOURNAL
    report, rc = run_fx_drift(c, "order", True)
    texts = [r["text"] for r in report["render"]]
    c.check("order: both texts render and one order is returned", rc == 0 and len(report["orders"]) == 1
            and texts == ["MUST tell nobody.", "MUST also tell the team."]
            and any(ln.lstrip().startswith("stale") for ln in report["lines"]) and not journal.exists(),
            f"{rc} {report}")
    body = report["orders"][0]["body"] if report["orders"] else ""
    c.check("...the order is keyed on the overlay row and carries its own title, both texts and the re-pin",
            report["orders"] and report["orders"][0]["path"] == f"{iu.OVERLAY}#{FX_REPO}"
            and body.startswith(f"# {FX_REPO}'s amends edge on {FX_TAG} is stale") and "MUST tell the team." in body
            and "MUST tell nobody." in body and "--edges amends=" in body, body)
    report, rc = run_fx_drift(c, "refuse", True)
    clean = iu.run_git(c.top, "status", "--porcelain", "--untracked-files=all").strip()
    c.check("refuse: exit 1, nothing written, the edge named", rc == 1 and report["refuse"] and not clean
            and not report["orders"] and any(FX_REPO in ln and "held" in ln for ln in report["lines"]),
            f"{rc} {report} {clean!r}")
    report, rc = run_fx_drift(c, "warn", True)
    rows = journal.read_text(encoding="utf-8").splitlines() if journal.is_file() else []
    c.check("warn: both render, the edge printed, one journal line, no order",
            rc == 0 and len(report["render"]) == 2 and not report["orders"] and len(rows) == 1
            and rows[0].split("\t")[2:4] == [FX_REPO, FX_TAG] and rows[0].endswith("\twarn")
            and any(ln.lstrip().startswith("stale") for ln in report["lines"]), f"{rc} {report} {rows}")


def arm_empty(c):
    build_drift_gov(c, ["MUST tell the team."], overlay=False)
    report, rc = run_fx_drift(c)
    c.check("no overlay prints no unit line, and the row pass says it ran over none",
            rc == 0 and report["lines"] == [] and report["rows"] == "0 row kinds registered", f"{rc} {report}")


def write_ending_fx(c, action, successor, after_tags, edge):
    """Release 1 pinned `edge` on gov's unit; release 2 ends the tag by `action` with its record."""
    text = "MUST tell the team."
    build_drift_gov(c, [text], edge=edge)
    pin = iu.derive_unit_pin(text)
    rows = "".join(render_gov_row(t, text) for t in after_tags)
    c.write_file(FX_MANIFEST, rows or "")
    after = ",".join(f"{t}@{pin}" for t in after_tags) or "none"
    write_change_fx(c, FX_TAG, action, "semantic" if action != "rename" else "editorial", f"{FX_TAG}@{pin}",
                    after, successor=successor)
    iu.run_commit(c.top, f"release: {action}")


def arm_rename(c):
    write_ending_fx(c, "rename", "unit.push-main", ["unit.push-main"], "amends")
    report, rc = run_fx_drift(c)
    texts = [r["tag"] for r in report["render"]]
    c.check("a rename re-points the edge with its pin kept and files no order",
            rc == 0 and not report["orders"] and "unit.push-main <- repo.push (renamed from unit.push, pin kept)"
            in report["lines"][0] and texts == ["unit.push-main", FX_REPO], f"{rc} {report}")


def arm_split(c):
    write_ending_fx(c, "split", "unit.push-a,unit.push-b", ["unit.push-a", "unit.push-b"], "amends")
    report, rc = run_fx_drift(c)
    tags = [r["tag"] for r in report["render"]]
    c.check("a split orphans an amends: absent from the render, one order",
            rc == 0 and "orphaned" in report["lines"][0] and FX_REPO not in tags and len(report["orders"]) == 1,
            f"{rc} {report}")
    report, rc = run_fx_drift(c, "refuse")
    c.check("...and holds the update under refuse", rc == 1 and report["refuse"] and not report["orders"],
            f"{rc} {report}")


def arm_retire(c):
    write_ending_fx(c, "remove", "none", [], "supersedes")
    report, rc = run_fx_drift(c)
    tags = [r["tag"] for r in report["render"]]
    c.check("a retirement orphans a supersedes, which renders alone, and files one order",
            rc == 0 and "(successor: none)" in report["lines"][0] and tags == [FX_REPO]
            and len(report["orders"]) == 1, f"{rc} {report}")


def arm_new_beside(c):
    c.write_file(".memory-tree.conf", 'MEMORY_ROOT=memory\nFAMILIES="play:PLAY"\n')
    c.write_file("tools/alpha/kit.toml", 'id = "alpha"\n')
    c.write_file(FX_MANIFEST, render_gov_row(FX_TAG, "MUST tell the team."))
    c.write_file(iu.OVERLAY, ov.render_fx_row("repo.ships-charter", 0, "MUST ship the charter."))
    iu.run_commit(c.top, "release 1")
    first = iu.run_git(c.top, "rev-parse", "HEAD").strip()
    c.write_file(FX_MANIFEST, render_gov_row(FX_TAG, "MUST tell the team.")
                 + render_gov_row("unit.portable", "MUST stay portable.", 0)
                 + render_gov_row("unit.task-note", "MUST note the task.", 4))
    iu.run_commit(c.top, "release 2")
    report, rc = run_fx_drift(c, from_rev=first)
    beside = [ln for ln in report["lines"] if "new-beside" in ln]
    c.check("a new level-0 gov unit is listed beside the level-0 repository unit, the level-4 one is not",
            rc == 0 and len(beside) == 1 and "unit.portable at level 0 beside repo.ships-charter" in beside[0],
            f"{rc} {report}")


def arm_unit_class(c):
    write_ending_fx(c, "remove", "none", [], "supersedes")
    c.write_file(FX_MANIFEST, render_gov_row("unit.kept", "MUST keep.") + render_gov_row("unit.gone", "MUST go."))
    iu.run_commit(c.top, "two units")
    c.check("the reader returns every gov unit tag", read_unit_members(c.top) == {"unit.kept", "unit.gone"},
            str(read_unit_members(c.top)))
    c.check("the witness returns the tag a record ends", read_change_successors(c.top) == {FX_TAG},
            str(read_change_successors(c.top)))
    member = write_unit_plant(c.top)
    c.check("the plant removes one unit, staged, and names it", member == "unit:unit.kept"
            and read_unit_members(c.top) == {"unit.gone"} and "unit.kept" not in
            iu.run_git(c.top, "show", f":{FX_MANIFEST}"), member)


PLANTS = {"meaning-editorial": arm_meaning_editorial, "punctuation-editorial": arm_punctuation_editorial,
          "spelling": arm_spelling, "ruling-unproven": arm_ruling_unproven, "editorial-behind": arm_editorial_behind,
          "semantic-behind": arm_semantic_behind, "empty": arm_empty, "rename": arm_rename, "split": arm_split,
          "retire": arm_retire, "new-beside": arm_new_beside, "unit-class": arm_unit_class}


def run_fixture(plant=None) -> tuple[list, int]:
    """Each plant in a throwaway repository, the caller's git variables aside."""
    iu.load_memory_tree_path()
    from deviation_join import set_env_aside
    from tree_lib import GIT_ENV_LEAKS
    out, failed = [], 0
    for name in [plant] if plant else list(PLANTS):
        top = pathlib.Path(tempfile.mkdtemp(prefix="pins-fx-"))
        try:
            with set_env_aside(GIT_ENV_LEAKS):
                iu.run_git(top, "init", "-q")
                iu.run_git(top, "config", "core.autocrlf", "false")
                case = iu.Case(top, out)
                out.append(f"{SAY}: fixture · plant {name}")
                try:
                    PLANTS[name](case)
                except (ValueError, RuntimeError, OSError) as exc:   # a plant that raises is a failed one
                    case.check(f"{name} ran to its end", False, f"{type(exc).__name__}: {exc}")
                failed += case.failed
        finally:
            shutil.rmtree(top, ignore_errors=True)
    out.append(f"{SAY}: fixture · {'FAILED' if failed else 'green'} · {failed} expectation(s) failed")
    return out, 1 if failed else 0


def main(argv) -> int:
    if argv[:1] == ["drift"]:
        import argparse
        ap = argparse.ArgumentParser(prog="pins.py drift", allow_abbrev=False)
        ap.add_argument("--target", required=True)
        ap.add_argument("--gov", required=True)
        ap.add_argument("--from", dest="from_rev")
        ap.add_argument("--to", required=True)
        ap.add_argument("--stale", required=True, choices=STALE_MODES)
        ap.add_argument("--write", action="store_true")
        a = ap.parse_args(argv[1:])
        report, rc = run_unit_drift(a.target, a.gov, a.from_rev, a.to, a.stale, a.write)
        sys.stdout.buffer.write((json.dumps(report, ensure_ascii=False) + "\n").encode("utf-8"))
        return rc
    if argv[:1] == ["--fixture"] and (len(argv) == 1 or (len(argv) == 3 and argv[1] == "--plant")):
        plant = argv[2] if len(argv) == 3 else None
        if plant is not None and plant not in PLANTS:
            lines, rc = [f"{SAY}: no plant {plant!r}; the plants are {', '.join(PLANTS)}"], 2
        else:
            lines, rc = run_fixture(plant)
    else:
        lines, rc = [__doc__.split("\n\n")[1]], 2
    for line in lines:
        sys.stdout.buffer.write((line + "\n").encode("utf-8"))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
