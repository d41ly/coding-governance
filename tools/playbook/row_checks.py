#!/usr/bin/env python3
"""row_checks.py — the row checks over every registered kind (PLAY-dOrderedCharter-36).

`derive_row_composition` in `overlay_rows.py` calls `check_rows(schema, entries, rows, exclude, policy)`
after its edge loop, and a red refuses the composition. The schema is `read_kind_schema`'s, whose `decl`
carries each field's `ref`, `fixed-by` and `widens`, and whose `fixed-rows` maps a fixed row's tag to its
`fixed-by` sources, each source resolved by `overlay.check_fixed_sources` when the schema was read.

THE FIXED SET. A field is open when it declares `widens`, fixed otherwise: its `fixed-by` resolves, or it
declares neither and reads fixed by its undeclared class. An `amends` naming a fixed field as written,
whether or not gov's row ships it, an `amends` or `supersedes` of a fixed row, a `supersedes` changing or
dropping a fixed field, and an `instructions.exclude` entry naming a fixed row each refuse, naming the
row, the field where one applies and the sources; a refusal the classifier reads widening says so.

THE EXCLUSION WALK. An excluded tag another active row holds in a field whose `ref` role is `needs`,
`actor` or `grants` refuses, naming that row and the field; one a tag-valued policy key's members name
refuses, naming the key. `instructions.exclude` is never its own requirer.

THE CLASSIFIER. `derive_patch_class` reads one operation against gov's value from the field's declared
direction alone: `add` or `remove` on a set (the one equal to `widens` widens), a new value on a scalar
whose `widens` is an order, a later value widening. A value outside the order refuses; gov's own value
outside it ranks below every listed one. `derive_widenings` lists the operations that widen.
"""
from __future__ import annotations

import json
import os
import pathlib
import sys

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import overlay as ov  # noqa: E402

SAY = "row-checks"
REF_ROLES = ("needs", "actor", "grants")
POLICY_SELF = "instructions.exclude"


def derive_set_value(value) -> list:
    """A field's members as a list: none for an absent field, one for a bare value."""
    if value is None:
        return []
    return list(value) if isinstance(value, list) else [value]


def derive_entry_ops(schema, row, etype, gov_row) -> tuple:
    """`(named, ops)` of one edge's row as written: the fields it names, and each `(field, op, value)` it
    writes over gov's row, `op` `add`, `remove` or `set`. An `amends` names its `add` and `remove` tables'
    fields and its field keys; a `supersedes` names each field whose value differs from gov's. A set field
    written whole is its gained members' `add` and its lost members' `remove`."""
    fields, named, ops = schema["fields"], [], []
    if etype == "amends":
        for op in ("add", "remove"):
            for f, vals in (row.get(op) or {}).items():
                named.append(f)
                ops.append((f, op, derive_set_value(vals)))
        keys = [k for k in row if k in fields and k != "tag"]
    else:
        keys = [k for k in fields if k != "tag" and json.dumps(row.get(k), sort_keys=True) != json.dumps(
            gov_row.get(k), sort_keys=True)]
    for f in keys:
        named.append(f)
        if fields[f] == "set":
            new, old = derive_set_value(row.get(f)), derive_set_value(gov_row.get(f))
            ops += [(f, "add", [v for v in new if v not in old]), (f, "remove", [v for v in old if v not in new])]
        else:
            ops.append((f, "set", row.get(f)))
    return named, ops


def derive_patch_class(decl, op, gov_value, value):
    """S5: `widens`, `narrows`, or None where the operation changes nothing: a set `op` moving no member
    gov's value lacks (`add`) or holds (`remove`), a scalar equal to gov's. ValueError for a scalar value
    outside the field's order; gov's value outside it ranks below every listed value (section 8 F8)."""
    order = decl["widens"]
    if op in ("add", "remove"):
        held = derive_set_value(gov_value)
        if not [v for v in value if (v in held) == (op == "remove")]:
            return None
        return "widens" if op == order else "narrows"
    if value == gov_value:
        return None
    if value not in order:
        raise ValueError(f"value {value!r} is outside its order {', '.join(map(str, order))}")
    if gov_value not in order:
        return "widens"
    return "widens" if order.index(value) > order.index(gov_value) else "narrows"


def check_rows(schema, entries, rows, exclude, policy) -> tuple:
    """S3 to S7 over one kind's composition. `entries` holds `(overlay row, edge type, gov's row, applied)`
    per pinned edge whose target gov ships; `rows` the composed rows; `exclude` the excluded tags; `policy`
    `{tag-valued key: [member]}`. -> `(reds, checks)`, `checks` `{"operations": [...], "counts": {...}}`."""
    decl, fixed_rows, reds, operations = schema["decl"], schema["fixed-rows"], [], []
    for row, etype, gov_row, applied in entries:
        otag, gtag = row.get("tag"), gov_row["tag"]
        named, ops = derive_entry_ops(schema, row, etype, gov_row)
        widened = []
        for f, op, value in ops:
            if decl.get(f, {}).get("widens") is None or (not applied and gtag not in fixed_rows):
                continue
            try:
                klass = derive_patch_class(decl[f], op, gov_row.get(f), value)
            except ValueError as exc:
                reds.append(f"{SAY}: red · widens · {otag} {etype} {gtag} · field {f} · {exc}")
                continue
            if klass is None:
                continue
            widened += [f] if klass == "widens" else []
            if applied:
                operations.append({"row": otag, "tag": gtag, "field": f, "op": op, "value": value,
                                   "gov": gov_row.get(f), "class": klass})
        if gtag in fixed_rows:
            wide = f" · a widening of {', '.join(sorted(set(widened)))}" if widened else ""
            reds.append(f"{SAY}: red · fixed · {otag} {etype} the fixed row {gtag}{wide} · fixed by "
                        f"{', '.join(fixed_rows[gtag])} · remedy: drop the row; gov's fixed rows take no change")
            continue
        for f in dict.fromkeys(named):
            if f in decl and decl[f].get("widens") is None:
                reds.append(f"{SAY}: red · fixed · {otag} {etype} {gtag} · field {f} · fixed by "
                            f"{', '.join(decl[f].get('fixed-by') or [ov.UNDECLARED])} · remedy: drop the field "
                            f"from the row")
    reds += [f"{SAY}: red · fixed · instructions.exclude lists the fixed row {tag} · fixed by "
             f"{', '.join(fixed_rows[tag])} · remedy: drop it from the set" for tag in sorted(exclude) if tag in fixed_rows]
    refs = {f: d["ref"] for f, d in decl.items() if d.get("ref") in REF_ROLES}
    for tag in sorted(exclude):
        for row in rows:
            reds += [f"{SAY}: red · exclude · instructions.exclude lists {tag}, which {row.get('tag')} still "
                     f"holds in its {refs[f]} field `{f}` · remedy: take {tag} from that field, or drop the exclusion"
                     for f in refs if tag in derive_set_value(row.get(f))]
        reds += [f"{SAY}: red · exclude · instructions.exclude lists {tag}, which the policy key {key} names · "
                 f"remedy: take {tag} from {key}, or drop the exclusion"
                 for key, members in sorted(policy.items()) if key != POLICY_SELF and tag in members]
    counts = {"fixed": len(entries) + len(exclude), "classify": sum(1 for e in entries if e[3]),
              "exclude": len(rows) if exclude else 0, "policy": len(policy) if exclude else 0}
    return reds, {"operations": operations, "counts": counts}


def derive_widenings(checks) -> list:
    """S6: every operation in `checks` whose class is `widens`, each with its row, field, operation and gov's value."""
    return [op for op in checks["operations"] if op["class"] == "widens"]
