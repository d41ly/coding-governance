#!/usr/bin/env python3
"""overlay_rows.py — the overlay's row mechanism for every registered kind (PLAY-dOrderedCharter-35).

THE ROWS. A kind the kinds register lists with a `schema` may hold repository rows in the overlay,
`.governance/instructions.toml`, as `[[<kind>]]` tables. `read_overlay_rows` reads them through the overlay's
one reader, `overlay.read_overlay`, and its `tables`, parsing no TOML itself; every row it returns carries
`origin = "repository"`, and a row typing `origin` is refused, as is a table naming no row kind or holding
no array of tables.

THE SCHEMA. `read_kind_schema` finds a kind's schema through `pins.read_row_kinds`, its `schema` path
`{prefix}`-relative, and reads the `[kind]` table's `name` and `owner-seat` and each `[[field]]` row's
`name` and `shape` (`set` or `scalar`). Every other schema key is PLAY-dOrderedCharter-36's, added here.

THE COMPOSITION. `derive_row_composition` runs `check_row_owners` (a tag holding `adopter` at the kind's
owner seat is the repository's: legal only on an overlay row, and an overlay row needs it), then:
`instructions.exclude`'s tags of the kind are absent (`excluded`); a `supersedes=<tag>@<hash8>` row
answers to gov's tag (`replaced`); an `amends=<tag>@<hash8>` row patches gov's row by `set_row_patch`,
`add` a set union, `remove` a set difference, a scalar a value (`amended`); each pin is walked by
`pins.derive_pin_state` over the rows' canonical forms (`derive_row_canon`): a semantic change behind it
is `stale` and `instructions.stale` acts, `order` and `warn` applying the patch over gov's new row,
`refuse` holding the composition; a renamed target re-points the edge, a split or ended one orphans it
(`orphaned`), the amendment held out and the replacement composing on its own. Rows with no edge join as
the repository's own. It returns data and writes nothing.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import sys
import tomllib
import types

sys.dont_write_bytecode = True

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import instruction_units as iu  # noqa: E402
import overlay as ov  # noqa: E402
import pins  # noqa: E402

SAY = "overlay-rows"
ADOPTER = "adopter"
SHAPES = ("set", "scalar")
PATCH_KEYS = ("add", "remove")
EDGE_KEYS = ("edges", *PATCH_KEYS)
DERIVED_KEYS = ("origin", "source")
STATES = ("unchanged", "amended", "replaced", "excluded", "stale", "orphaned")
HASH8 = re.compile(r"[0-9a-f]{8}")


def check_reds(reds):
    """Raise one OverlayRefused naming every red, where there is one."""
    if reds:
        raise ov.OverlayRefused(1, "\n".join(reds))


def read_kind_schema(root, kind) -> dict:
    """S10: `{name, owner-seat, fields: {name: shape}, path}` of `kind`'s row schema, found through the kinds
    register under `root`; one OverlayRefused naming the schema file and each fault."""
    from tag_index import resolve_prefix_token
    row = next((r for r in pins.read_row_kinds(root) if r.get("tag") == f"kind.{kind}"), None)
    if row is None:
        check_reds([f"{SAY}: red · kind {kind} · the kinds register lists no such kind with a `schema`"])
    rel = resolve_prefix_token(row["schema"], iu.derive_kit_prefix())
    path = pathlib.Path(root) / rel
    try:
        doc = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        check_reds([f"{SAY}: red · {rel} · the schema of {kind} is unreadable: {exc}"])
    head, reds, fields = doc.get("kind"), [], {}
    seat = head.get("owner-seat") if isinstance(head, dict) else None
    if not isinstance(head, dict):
        reds.append(f"{SAY}: red · {rel} · [kind] · the table is missing")
    elif head.get("name") != kind:
        reds.append(f"{SAY}: red · {rel} · [kind] name · {head.get('name')!r} is not the kind {kind}")
    if isinstance(head, dict) and (type(seat) is not int or seat < 1):
        reds.append(f"{SAY}: red · {rel} · [kind] owner-seat · {seat!r} is no positive integer")
    rows = doc.get("field") or []
    for i, f in enumerate(rows if isinstance(rows, list) else [rows], 1):
        name = f.get("name") if isinstance(f, dict) else None
        shape = f.get("shape") if isinstance(f, dict) else None
        if not isinstance(name, str) or not name:
            reds.append(f"{SAY}: red · {rel} · [[field]] row {i} · names no field")
        elif name in fields:
            reds.append(f"{SAY}: red · {rel} · field {name} · is declared twice")
        elif shape not in SHAPES:
            reds.append(f"{SAY}: red · {rel} · field {name} · shape {shape!r} is neither set nor scalar")
        else:
            fields[name] = shape
    check_reds(reds)
    return {"name": kind, "owner-seat": seat, "fields": fields, "path": rel}


def read_overlay_rows(root) -> dict:
    """S1: `{kind: [row]}` of the overlay's row tables at HEAD, each row's `origin` the repository."""
    kinds = {r["tag"].partition(".")[2] for r in pins.read_row_kinds(root) if isinstance(r.get("tag"), str)}
    out, reds = {}, []
    for name, value in ov.read_overlay(root).tables.items():
        if name not in kinds:
            reds.append(f"{SAY}: red · {iu.OVERLAY} · [[{name}]] · names no kind the kinds register lists with "
                        f"a `schema` · remedy: register the kind's schema, or drop the table")
        elif not isinstance(value, list) or not all(isinstance(r, dict) for r in value):
            reds.append(f"{SAY}: red · {iu.OVERLAY} · {name} · is no array of [[{name}]] tables")
        else:
            for i, row in enumerate(value, 1):
                if "origin" in row:
                    reds.append(f"{SAY}: red · {iu.OVERLAY} · [[{name}]] row {i} ({row.get('tag')}) · types "
                                f"`origin`, which is derived from the file it is read from · remedy: drop the key")
                out.setdefault(name, []).append({**row, "origin": ov.ORIGIN, "source": iu.OVERLAY})
    check_reds(reds)
    return out


def check_row_owners(schema, rows) -> list:
    """S2, the `owned` clause over the rows the composer holds: `adopter` at the schema's owner seat on an
    overlay row and nowhere else. -> one red per row, naming `owned`, the tag and its file."""
    seat, reds = schema["owner-seat"], []
    for row in rows:
        tag = str(row.get("tag") or "")
        parts = tag.split(".")
        held = parts[seat] if len(parts) > seat else None
        mine = row.get("origin") == ov.ORIGIN
        if mine and held != ADOPTER:
            reds.append(f"{SAY}: red · owned · {tag} · {row.get('source')} · a repository row's tag holds no "
                        f"`{ADOPTER}` at segment {seat} · remedy: tag it {parts[0]}.{ADOPTER}.<name>")
        elif not mine and held == ADOPTER:
            reds.append(f"{SAY}: red · owned · {tag} · {row.get('source')} · gov's pack ships a tag holding the "
                        f"repository's `{ADOPTER}` seat")
    return reds


def derive_row_canon(schema, row) -> str:
    """The row's canonical form: JSON, keys sorted, set fields sorted, strings folded by the pin
    normaliser's whitespace rule, the edge and patch keys and the derived ones left out."""
    def derive_folded_value(value, shape):
        if isinstance(value, str):
            return pins.fold_text(value)
        if isinstance(value, list):
            got = [derive_folded_value(v, None) for v in value]
            return sorted(got, key=json.dumps) if shape == "set" else got
        if isinstance(value, dict):
            return {k: derive_folded_value(v, None) for k, v in value.items()}
        return value
    fields = schema["fields"]
    body = {k: derive_folded_value(v, fields.get(k)) for k, v in row.items() if k not in EDGE_KEYS + DERIVED_KEYS}
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def set_row_patch(schema, gov_row, patch) -> tuple:
    """S3: `(row, why)`: gov's row with `patch`'s `add` unioned, `remove` taken away and scalars set, every
    other field gov's; `why` names a patched field gov's row lacks, the patch then held and `row` gov's."""
    lacking = [f for k in PATCH_KEYS for f in (patch.get(k) or {}) if f not in gov_row]
    lacking += [k for k in patch if k in schema["fields"] and k != "tag" and k not in gov_row]
    if lacking:
        return gov_row, f"gov's row {gov_row['tag']} ships no `{'`, `'.join(lacking)}`"
    out = dict(gov_row)
    for f, vals in (patch.get("add") or {}).items():
        out[f] = list(out[f]) + [v for v in vals if v not in out[f]]
    for f, vals in (patch.get("remove") or {}).items():
        out[f] = [v for v in out[f] if v not in vals]
    out.update({k: v for k, v in patch.items() if k in schema["fields"]})
    return out, None


def derive_row_composition(kind, schema, gov_rows, overlay_rows, exclude, stale_mode, records) -> tuple:
    """`(rows, states, held, stale, orders)` of `kind`: the composed rows, `{gov tag: state}` from STATES,
    the held patches' lines, the stale edges' lines and `[{kind, path, body}]` per order. One
    OverlayRefused names every refusal, and every stale edge under `refuse`."""
    if stale_mode not in pins.STALE_MODES:
        check_reds([f"{SAY}: red · instructions.stale {stale_mode!r} is none of {', '.join(pins.STALE_MODES)}"])
    fields, gov = schema["fields"], {r["tag"]: r for r in gov_rows}
    reds = check_row_owners(schema, list(gov_rows) + list(overlay_rows))
    words = {t.partition(".")[0] for t in gov} | {schema["name"]}
    reds += [f"{SAY}: red · instructions.exclude lists {t}, which no {kind} row of gov's holds · remedy: drop it "
             f"from the set" for t in sorted(exclude) if t.partition(".")[0] in words and t not in gov]
    current = {t: types.SimpleNamespace(text=derive_row_canon(schema, r)) for t, r in gov.items()}
    edges, own = [], []
    for row in overlay_rows:
        tag, where = row.get("tag"), f"{SAY}: red · {iu.OVERLAY} · {row.get('tag')}"
        for key, value in row.items():
            if key in ("tag", "edges") + DERIVED_KEYS or fields.get(key):
                continue
            if key not in PATCH_KEYS:
                reds.append(f"{where} · key `{key}` is no field the {kind} schema declares")
            elif not isinstance(value, dict):
                reds.append(f"{where} · `{key}` is no table of set fields")
            else:
                reds += [f"{where} · `{key}` names `{f}`, which is no set field of the {kind} schema"
                         for f in value if fields.get(f) != "set"]
        etype, _, target = str(row.get("edges") or "").partition("=")
        if not row.get("edges") or etype not in ov.EDGE_TYPES:
            if "@" in target:
                reds.append(f"{where} · edge `{row['edges']}` · a pin is legal on amends and supersedes alone")
            own.append(row)
            continue
        gtag, at, pin = target.partition("@")
        known = {iu.derive_unit_pin(current[gtag].text)} if gtag in current else set()
        known |= {p.partition("@")[2] for r in records for p in (r.get("Before") or "", *(r.get("After") or "").split(","))
                  if p.partition("@")[0] == gtag}
        if not at:
            reds.append(f"{where} · edge `{row['edges']}` · names no pin: the form is <tag>@<hash8>")
        elif not HASH8.fullmatch(pin):
            reds.append(f"{where} · edge `{row['edges']}` · `{pin}` is no eight-hex pin")
        elif pin not in known:
            reds.append(f"{where} · edge `{row['edges']}` · the pin matches no revision of gov's row {gtag}")
        elif gtag in exclude:
            reds.append(f"{where} · edge `{row['edges']}` · instructions.exclude lists its target")
        else:
            edges.append((row, etype, gtag, pin))
    check_reds(reds)
    rows = {t: r for t, r in gov.items() if t not in exclude}
    states = {t: "excluded" if t in exclude else "unchanged" for t in gov}
    held, stale, orders, replaced = [], [], [], set()
    for row, etype, gtag, pin in edges:
        state, detail, walked = pins.derive_pin_state(gtag, pin, records, current)
        line = f"  {state:<10} [{kind}] {gtag}@{pin} <- {row['tag']}"
        if state == "orphaned":
            states[gtag] = "orphaned"
            if etype == "supersedes":
                own.append({k: v for k, v in row.items() if k != "edges"})
            held.append(f"{line} · successor {detail} · " + ("held out" if etype == "amends" else "composes alone"))
            orders.append({"kind": kind, "path": f"{iu.OVERLAY}#{row['tag']}",
                           "body": f"# {row['tag']}'s {etype} edge on {gtag} is orphaned\n\n{held[-1].strip()}\n\n"
                                   f"Re-point it at a successor, or drop the row, with instructions.edit.\n"})
            continue
        last = (walked[-1].get("After") or "").partition("@")[0] if walked else gtag
        target, why = last if last in gov else gtag, None
        if target not in rows:
            held.append(f"{line} · held: gov ships no row {target} to apply it to")
            continue
        if state == "stale":
            names = ", ".join(r.get("id", "?") for r in detail) or "no record reaches the pin"
            stale.append(f"{line} · semantic since {pin} · {names}")
            if stale_mode == "refuse":
                continue
        if etype == "supersedes":
            if target in replaced:
                check_reds([f"{SAY}: red · {iu.OVERLAY} · {row['tag']} · a second row supersedes {target}"])
            replaced.add(target)
            rows[target] = {**{k: v for k, v in row.items() if k != "edges"}, "tag": target}
        else:
            rows[target], why = set_row_patch(schema, rows[target], row)
            if why:
                held.append(f"{line} · held, gov's row composes as shipped: {why}")
        states[target] = "stale" if state == "stale" else "replaced" if etype == "supersedes" else "amended"
        if state == "stale" and stale_mode == "order":
            orders.append({"kind": kind, "path": f"{iu.OVERLAY}#{row['tag']}",
                           "body": f"# {row['tag']}'s {etype} edge on {gtag} is stale\n\n{stale[-1].strip()}\n\n"
                                   + (f"The patch is held: {why}.\n\n" if why else "The patch is applied over gov's "
                                      "new row.\n\n") + "Re-pin it with instructions.edit once it reads right.\n"})
    if stale_mode == "refuse" and stale:
        check_reds([f"{SAY}: red · instructions.stale = refuse · the update is held until instructions.edit re-pins:",
                *stale])
    return list(rows.values()) + own, states, held, stale, orders
