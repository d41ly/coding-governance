#!/usr/bin/env python3
"""row_kind.py — the fixture kind of PLAY-dOrderedCharter-35 and 36: one scratch tree, one plant, one composition.

    python row_kind.py --plant <case> [--exclude <tag>] [--stale order|warn|refuse] [--policy <key>=<tag>]...

Each plant builds a throwaway repository holding a namespace registry row for `fixture`, a kinds register
row naming the kind's schema, the schema (FIELDS below: open set fields `grants` and `needs`, open scalars
`actor` and `ceiling`, the `rises-only` scalar `reach` (TOOL-dBoundRoles-82), the parser-fixed `witness`, the undeclared `note`, the fixed row `fixture.epsilon`,
owner seat 1), gov's principle registry and this file, which the schema's `fixed-by` sources resolve
against, gov's pack and the overlay, commits it, and where the case needs one commits gov's next revision
under a change record. It then composes the kind at HEAD through `overlay_rows` and prints what it expects,
each composed row, each gov row's state, each held patch, stale edge, order and journal line, each
classified patch operation, each widening and the rows each row check read. `--exclude` commits
`instructions.exclude` in the tree's policy file; `--stale` is `instructions.stale`; `--policy` sets a
tag-valued policy key's one member over what `read_tag_policy` read. Where an exclusion is set the leg
manifest's names are read by `read_leg_names` and handed on (TOOL-dBoundRoles-83); the `exclude-leg-`
plants commit a manifest of LEG_ROWS. The `front-matter-` plants (TOOL-dBoundRoles-81) register the `role`
and `workflow` kinds instead, each namespace row naming the reader READER, and compose both at HEAD through
`overlay_rows.derive_kind_composition`, so gov's rows are read from role files under a glob and from
`[[workflow]]` entries by the roles kit's `check_roles.py --print-rows`.

Exit 0 the composition held · 1 it was refused · 2 usage, a plant that could not be built, or a kind unarmed.
"""
from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import instruction_units as iu  # noqa: E402
import overlay as ov  # noqa: E402
import overlay_rows as orows  # noqa: E402
import pins  # noqa: E402
import policy_value as pv  # noqa: E402
import row_checks as rc  # noqa: E402

SAY = "row-kind"
KIND = "fixture"
PREFIX = iu.derive_kit_prefix()
SCHEMA = f"{PREFIX}/{KIND}/schema.toml" if PREFIX else f"{KIND}/schema.toml"
PACK = f"{PREFIX}/{KIND}/rows.toml" if PREFIX else f"{KIND}/rows.toml"
BUILD, UNIT = "tFx", "PLAY-tFx-1"
SOURCE = iu.derive_tool_rel(iu.KIT_DIR.name, "fixtures", pathlib.Path(__file__).name)
FIELDS = ({"name": "grants", "shape": "set", "ref": "grants", "widens": "add"},
          {"name": "needs", "shape": "set", "ref": "needs", "widens": "remove"},
          {"name": "actor", "shape": "scalar", "ref": "actor", "widens": ["fixture.beta", "fixture.gamma"]},
          {"name": "ceiling", "shape": "scalar", "widens": ["low", "mid", "high"]},
          {"name": "reach", "shape": "scalar", "widens": "rises-only"},
          {"name": "witness", "shape": "scalar", "fixed-by": [f"parser={SOURCE}#render_rows"]},
          {"name": "note", "shape": "scalar"})
FIXED_ROW = {"tag": "fixture.epsilon", "fixed-by": ["principle=principle.p16"]}
GOV = [{"tag": "fixture.alpha", "grants": ["read"], "needs": ["fixture.beta", "fixture.gamma"],
        "ceiling": "low by default"},
       {"tag": "fixture.beta", "grants": ["list"], "needs": [], "ceiling": "low"},
       {"tag": "fixture.gamma", "grants": ["write"], "needs": [], "ceiling": "high"}]
STATE_GOV = GOV + [{"tag": f"fixture.{t}", "grants": ["read"], "needs": [], "ceiling": "low"}
                   for t in ("delta", "epsilon", "zeta")]


def render_value(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_rows(rows, order=None) -> str:
    """`[[fixture]]` tables, each row's keys in `order` where given; a `str` value given as `("raw", text)`
    is written as it stands."""
    out = []
    for row in rows:
        keys = order or list(row)
        body = "".join(f"{k} = {row[k][1] if isinstance(row[k], tuple) else render_value(row[k])}\n"
                       for k in keys if k in row)
        out.append(f"[[{KIND}]]\n{body}")
    return "\n".join(out)


def render_schema(**patch) -> str:
    """The fixture kind's schema, `patch` mapping a field's name to the keys it writes over FIELDS'."""
    tables = [("field", {**f, **patch.get(f["name"], {})}) for f in FIELDS] + [("fixed-row", FIXED_ROW)]
    return f'[kind]\nname = "{KIND}"\nowner-seat = 1\n' + "".join(
        f"\n[[{name}]]\n" + "".join(f"{k} = {render_value(v)}\n" for k, v in t.items()) for name, t in tables)


def derive_schema() -> dict:
    return {"name": KIND, "owner-seat": 1, "fields": {f["name"]: f["shape"] for f in FIELDS}}


def derive_pin(row) -> str:
    return iu.derive_unit_pin(orows.derive_row_canon(derive_schema(), row))


def write_files(top, files):
    for rel, text in files.items():
        path = top / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="")
        iu.run_git(top, "add", "--", rel)


def write_change(top, tag, action, before_row, after_rows, successor=None, mark=None):
    """One change record of a gov row through the kind's writer, its mark the classifier's over the two
    canonical forms where `mark` is not given."""
    iu.load_memory_tree_path()
    import build_records
    schema = derive_schema()
    before = f"{tag}@{derive_pin(before_row)}"
    after = ",".join(f"{r['tag']}@{derive_pin(r)}" for r in after_rows) or "none"
    if mark is None:
        mark = pins.derive_change_mark(orows.derive_row_canon(schema, before_row),
                                       orows.derive_row_canon(schema, after_rows[0]), {}, None)
    rel = build_records.write_change(top, BUILD, UNIT, tag, action, mark, before, after,
                                     build_records.DOOR_PROOF, successor)
    iu.run_git(top, "add", "--", rel)


def build_tree(top, gov=GOV, overlay="", schema=None, exclude=None, policy="", more=None):
    """Commit 1: the registers, gov's principle registry, this file, the schema, gov's pack, the overlay and
    the policy file, `policy` text after its `instructions.exclude`, and `more`'s `{path: text}` beside."""
    files = {".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="play:PLAY"\n',
             f"memory/builds/{BUILD}/README.md": "# the fixture build\n",
             iu.derive_kit_file(".", "namespaces.toml").as_posix():
                 f'[[namespace]]\nns = "{KIND}"\nowner = "{BUILD}"\nsource = "{PACK}"\n',
             iu.derive_kit_file(".", "kinds.toml").as_posix():
                 f'[[kind]]\ntag = "kind.{KIND}"\nowner = "{BUILD}"\nschema = "{{prefix}}/{KIND}/schema.toml"\n',
             iu.derive_kit_file(".", "principles.toml").as_posix():
                 (iu.KIT_DIR / "principles.toml").read_text(encoding="utf-8"),
             SOURCE: pathlib.Path(__file__).read_text(encoding="utf-8"),
             SCHEMA: schema or render_schema(), PACK: render_rows(gov), iu.OVERLAY: overlay}
    if exclude:
        files[".governance/policy.toml"] = f"[instructions]\nexclude = {render_value([exclude])}\n{policy}"
    write_files(top, {**files, **(more or {})})
    iu.run_commit(top, "the fixture")


def build_next(top, gov, changes):
    """Commit 2: gov's next pack and its change records, each `(tag, action, before, afters, successor)`."""
    write_files(top, {PACK: render_rows(gov)})
    for tag, action, before, afters, successor, *mark in changes:
        write_change(top, tag, action, before, afters, successor, *mark)
    iu.run_commit(top, "gov's next revision")


def render_patch(tag, target, edge="amends", pin=None, **fields) -> str:
    row = {"tag": tag, "edges": f"{edge}={target['tag']}@{pin or derive_pin(target)}", **fields}
    return render_rows([{k: ("raw", v) if k in ("add", "remove") else v for k, v in row.items()}])


AMEND = {"add": '{ grants = ["write"] }', "remove": '{ needs = ["fixture.beta"] }', "ceiling": "high"}
REPLACE = {"grants": ["read"], "needs": [], "ceiling": "low"}


def render_amend(target=GOV[0], **more) -> str:
    return render_patch("fixture.adopter.alpha-tuned", target, **{**AMEND, **more})


def render_replace(target=GOV[2]) -> str:
    return render_patch("fixture.adopter.gamma-own", target, "supersedes", **REPLACE)


EXTRA = render_rows([{"tag": "fixture.adopter.extra", "grants": ["read"], "ceiling": "low"}])
UNNEED = render_patch("fixture.adopter.alpha-tuned", GOV[0], remove='{ needs = ["fixture.beta"] }')
EPSILON = STATE_GOV[4]
CLASSIFY = "\n".join([
    render_patch("fixture.adopter.alpha-tuned", GOV[0], add='{ grants = ["write"] }',
                 remove='{ needs = ["fixture.beta"] }', ceiling="mid"),
    render_patch("fixture.adopter.beta-tuned", GOV[1], add='{ needs = ["fixture.gamma"] }', ceiling="high")])


def build_exclude_plant(top, a, overlay="", policy=""):
    """An exclusion of `--exclude`, `fixture.beta` by default, whose overlay takes it from `fixture.alpha`'s
    needs, with `overlay`'s rows beside and `policy` text in the policy file."""
    build_tree(top, overlay="\n".join(o for o in (UNNEED, overlay) if o), exclude=a.exclude or "fixture.beta",
               policy=policy)


LEGS = iu.derive_tool_rel("gate-legs.json")
LEG_ROWS = [{"name": "fixture leg", "tag": "leg.fixture.fixture-leg"}, {"name": "other leg", "tag": "leg.fixture.other"}]


def build_leg_plant(top, a, exclude):
    """TOOL-dBoundRoles-83: a leg manifest of LEG_ROWS in the tree, an overlay row granting `fixture leg?`
    by its leg name, and `--exclude`, `exclude` by default, in `instructions.exclude`."""
    build_tree(top, overlay=render_rows([{"tag": "fixture.adopter.granter", "grants": ["fixture leg?"]}]),
               exclude=a.exclude or exclude, more={LEGS: json.dumps(LEG_ROWS, indent=1) + "\n"})


def build_semantic_plant(top, row=None):
    new = row or {**GOV[0], "grants": ["read", "list"]}
    build_tree(top, overlay=render_amend())
    build_next(top, [new, *GOV[1:]], [("fixture.alpha", "edit", GOV[0], [new], None)])


def build_reordered_plant(top, _args=None):
    build_tree(top, overlay=render_amend())
    wrapped = [{**GOV[0], "ceiling": ("raw", '"""low by\n   default"""')}, *GOV[1:]]
    write_files(top, {PACK: render_rows(wrapped, order=["ceiling", "needs", "grants", "tag"])})
    iu.run_commit(top, "gov's rows reordered and re-wrapped")


def build_ending_plant(top, action):
    """Both edges' targets ended: split into two successors, or removed."""
    over = render_amend() + "\n" + render_replace()
    build_tree(top, overlay=over)
    heirs = {t: [{**r, "tag": f"{t}-{n}"} for n in ("a", "b")] if action == "split" else []
             for t, r in ((GOV[0]["tag"], GOV[0]), (GOV[2]["tag"], GOV[2]))}
    gov = [GOV[1]] + [r for rows in heirs.values() for r in rows]
    build_next(top, gov, [(r["tag"], action, r, heirs[r["tag"]],
                           ",".join(h["tag"] for h in heirs[r["tag"]]) or "none", "editorial")
                          for r in (GOV[0], GOV[2])])


def build_renamed_plant(top, _args=None):
    build_tree(top, overlay=render_amend())
    moved = {**GOV[0], "tag": "fixture.alpha2"}
    build_next(top, [moved, *GOV[1:]], [("fixture.alpha", "rename", GOV[0], [moved], "fixture.alpha2", "editorial")])


def build_rise_plant(top, reach, gov_reach=4, replace=False, schema=None):
    """TOOL-dBoundRoles-82: gov's `fixture.beta` and `fixture.gamma` carrying `reach`, beta's `gov_reach`
    and gamma's 4, and an overlay amending beta's `reach` to `reach`; with `replace`, a `supersedes` of
    gamma beside it, every field gov's but `reach`, written `reach`."""
    beta, gamma = {**GOV[1], "reach": gov_reach}, {**GOV[2], "reach": 4}
    over = [render_patch("fixture.adopter.beta-tuned", beta, reach=reach)]
    if replace:
        own = {k: v for k, v in gamma.items() if k != "tag"}
        over.append(render_patch("fixture.adopter.gamma-own", gamma, "supersedes", **{**own, "reach": reach}))
    build_tree(top, gov=[GOV[0], beta, gamma], overlay="\n".join(over), schema=schema)


FRONT_MATTER = "front-matter-"
READER = "tag_index:read_roles_rows"
FM_SOURCES = {"role": iu.derive_tool_rel(KIND, "agents", "*.agent.md"),
              "workflow": iu.derive_tool_rel(KIND, "workflows.toml")}
FM_FIELDS = {"role": (("name", "scalar"), ("tools", "set"), ("writes", "set")),
             "workflow": (("name", "scalar"), ("driver", "scalar"), ("roles", "set"))}
FM_ROLES = ("gov-alpha", "gov-beta")
FM_FLOWS = "".join(f'[[workflow]]\nname = "{n}"\ndriver = "{d}"\nroles = {render_value(r)}\n\n'
                   for n, d, r in (("triage", "agent", list(FM_ROLES)), ("sweep", "program", [])))
TRIAGER = {"tag": f"role.{orows.ADOPTER}.triager", "name": "triager", "tools": ["Read"], "writes": ["product"]}


def render_role_file(name, indent="") -> str:
    """One role file's front matter for the `role` kind's reader, its `tools` key indented by `indent`."""
    return (f"---\nname: {name}\n{indent}tools: Read, Grep\nwrites: product\ngates: lexicon naming predicates?\n"
            f"never: a limit — a.js; another — b.js\nbudget: 4096\n---\n\nThe {name} role.\n")


def build_front_matter_plant(top, roles=FM_ROLES, indent=""):
    """TOOL-dBoundRoles-81: the `role` and `workflow` kinds registered with fixture schemas, their namespace
    rows naming the reader READER, `role`'s source a glob; one role file per name of `roles`, the first
    one's `tools` key indented by `indent`, a workflows file of two entries, and the overlay row TRIAGER."""
    schema = {k: iu.derive_tool_rel(KIND, f"{k}-schema.toml") for k in FM_SOURCES}
    more = {iu.derive_kit_file(".", "namespaces.toml").as_posix(): "".join(
                f'[[namespace]]\nns = "{k}"\nowner = "{BUILD}"\nsource = "{s}"\nrows = "{READER}"\n\n'
                for k, s in FM_SOURCES.items()),
            iu.derive_kit_file(".", "kinds.toml").as_posix(): "".join(
                f'[[kind]]\ntag = "kind.{k}"\nowner = "{BUILD}"\nschema = "{{prefix}}/{KIND}/{k}-schema.toml"\n\n'
                for k in FM_SOURCES),
            FM_SOURCES["workflow"]: FM_FLOWS}
    for k, fields in FM_FIELDS.items():
        more[schema[k]] = f'[kind]\nname = "{k}"\nowner-seat = 1\n' + "".join(
            f'\n[[field]]\nname = "{n}"\nshape = "{s}"\n' for n, s in fields)
    for i, name in enumerate(roles):
        more[iu.derive_tool_rel(KIND, "agents", f"{name}.agent.md")] = render_role_file(name, indent if not i else "")
    overlay = "[[role]]\n" + "".join(f"{k} = {render_value(v)}\n" for k, v in TRIAGER.items())
    build_tree(top, overlay=overlay, more=more)


def run_front_matter_plant(top, out) -> tuple[list, list, int]:
    """TOOL-dBoundRoles-81: compose `role`, then `workflow`, at HEAD through `overlay_rows`, each gov row read
    by its namespace reader: one `row` line per composed row, its `origin` and `source` shown; an unarmed
    kind exits 2 naming why, a refusal 1."""
    try:
        for kind in FM_SOURCES:
            got = orows.derive_kind_composition(top, kind, set(), iu.read_change_records(top))
            if got is None:
                why = orows.read_kind_source(top, kind)[3]
                return out + [f"{SAY}: unarmed · kind {kind} · {why}", f"{SAY}: exit 2"], [], 2
            out += [f"{SAY}: row {r['tag']} · {json.dumps(r, sort_keys=True, ensure_ascii=False)}" for r in got[0]]
    except ov.OverlayRefused as exc:
        return out + str(exc).splitlines() + [f"{SAY}: exit 1"], [], 1
    return out + [f"{SAY}: exit 0"], [], 0


def build_states_plant(top):
    delta, zeta = STATE_GOV[3], STATE_GOV[5]
    over = "\n".join([render_amend(), render_replace(),
                      render_patch("fixture.adopter.delta-tuned", delta, ceiling="high"),
                      render_patch("fixture.adopter.zeta-tuned", zeta, ceiling="high")])
    build_tree(top, gov=STATE_GOV, overlay=over, exclude="fixture.beta")
    new = {**delta, "grants": ["read", "write"]}
    build_next(top, STATE_GOV[:3] + [new, STATE_GOV[4]],
               [(delta["tag"], "edit", delta, [new], None), (zeta["tag"], "remove", zeta, [], "none", "editorial")])


PLANTS = {
    "add": (0, "gov's three rows unchanged, fixture.adopter.extra composed with origin repository",
            lambda top, a: build_tree(top, overlay=EXTRA)),
    "typed-origin": (1, "refused, naming the row that types origin",
                     lambda top, a: build_tree(top, overlay=EXTRA + 'origin = "playbook"\n')),
    "adopter-tag": (0, "owned passes the overlay row fixture.adopter.extra",
                    lambda top, a: build_tree(top, overlay=EXTRA)),
    "gov-adopter": (1, "owned reds fixture.adopter.x, which gov's pack ships",
                    lambda top, a: build_tree(top, gov=GOV + [{"tag": "fixture.adopter.x", "grants": [], "needs": [],
                                                                "ceiling": "low"}])),
    "no-seat": (1, "owned reds the overlay row fixture.extra, which holds no adopter seat",
                lambda top, a: build_tree(top, overlay=EXTRA.replace("fixture.adopter.extra", "fixture.extra"))),
    "amends": (0, "fixture.alpha: grants read and write, needs fixture.gamma alone, ceiling high",
               lambda top, a: build_tree(top, overlay=render_amend())),
    "amends-undeclared": (1, "refused: `add` names colour, which the schema does not declare",
                          lambda top, a: build_tree(top, overlay=render_amend(add='{ colour = ["red"] }'))),
    "amends-scalar": (1, "refused: `remove` names the scalar ceiling",
                      lambda top, a: build_tree(top, overlay=render_amend(remove='{ ceiling = ["low"] }'))),
    "schema-shape": (1, "refused: the schema's field grants has the shape list",
                     lambda top, a: build_tree(top, overlay=render_amend(),
                                               schema=render_schema(grants={"shape": "list"}))),
    "supersedes": (0, "fixture.gamma answers with the overlay row's fields, fixture.alpha's need of it resolved",
                   lambda top, a: build_tree(top, overlay=render_replace())),
    "exclude": (0, "the excluded row is absent, its state excluded; a tag no row holds is refused",
                lambda top, a: build_exclude_plant(top, a, EXTRA)),
    "amends-fixed": (1, "refused: the patch sets witness, which a parser fixes",
                     lambda top, a: build_tree(top, overlay=render_patch("fixture.adopter.alpha-tuned", GOV[0],
                                                                         witness="parsed"))),
    "widen-fixed": (1, "refused: the patch raises the fixed row fixture.epsilon's ceiling, a widening",
                    lambda top, a: build_tree(top, gov=STATE_GOV, overlay=render_patch(
                        "fixture.adopter.epsilon-tuned", EPSILON, ceiling="high"))),
    "supersedes-fixed": (1, "refused: the row replaces the fixed row fixture.epsilon",
                         lambda top, a: build_tree(top, gov=STATE_GOV, overlay=render_patch(
                             "fixture.adopter.epsilon-own", EPSILON, "supersedes", **{**REPLACE, "ceiling": "mid"}))),
    "exclude-fixed": (1, "refused: instructions.exclude lists the fixed row fixture.epsilon",
                      lambda top, a: build_tree(top, gov=STATE_GOV, exclude="fixture.epsilon")),
    "undeclared": (1, "refused: the patch sets note, which declares no class and reads fixed",
                   lambda top, a: build_tree(top, overlay=render_patch("fixture.adopter.alpha-tuned", GOV[0],
                                                                       note="tuned"))),
    "typed-class": (1, "refused: the schema types `class` on ceiling",
                    lambda top, a: build_tree(top, overlay=render_amend(),
                                              schema=render_schema(ceiling={"class": "open"}))),
    "source-unresolved": (1, "refused: witness is fixed by principle=principle.nowhere, which resolves to nothing",
                          lambda top, a: build_tree(top, overlay=EXTRA, schema=render_schema(
                              witness={"fixed-by": ["principle=principle.nowhere"]}))),
    "both-declared": (1, "refused: witness declares both fixed-by and widens",
                      lambda top, a: build_tree(top, overlay=EXTRA,
                                                schema=render_schema(witness={"widens": ["low", "high"]}))),
    "exclude-needed": (1, "refused: fixture.alpha still needs the excluded tag",
                       lambda top, a: build_tree(top, overlay=EXTRA, exclude=a.exclude or "fixture.beta")),
    "exclude-actor": (1, "refused: fixture.adopter.actor still acts as the excluded tag",
                      lambda top, a: build_exclude_plant(top, a, render_rows(
                          [{"tag": "fixture.adopter.actor", "actor": "fixture.beta"}]))),
    "exclude-actor-spelled": (1, "refused: fixture.adopter.actor acts as fixture:beta, the excluded tag spelled",
                              lambda top, a: build_exclude_plant(top, a, render_rows(
                                  [{"tag": "fixture.adopter.actor", "actor": "fixture:beta"}]))),
    "exclude-leg-named": (1, "refused: fixture.adopter.granter grants fixture leg?, the excluded leg by its name",
                          lambda top, a: build_leg_plant(top, a, "leg.fixture.fixture-leg")),
    "exclude-leg-unnamed": (0, "leg.fixture.other excluded, a leg no member names, composes",
                            lambda top, a: build_leg_plant(top, a, "leg.fixture.other")),
    "exclude-granted": (1, "refused: fixture.adopter.granter still grants the excluded tag",
                        lambda top, a: build_exclude_plant(top, a, render_rows(
                            [{"tag": "fixture.adopter.granter", "grants": ["fixture.beta"]}]))),
    "exclude-policy": (1, "refused with --policy fixture.pick=fixture.beta: a policy key names the excluded tag",
                       lambda top, a: build_exclude_plant(top, a)),
    "exclude-instance": (1, "refused: the policy file's roles.harness.builder names the excluded tag",
                         lambda top, a: build_exclude_plant(top, a, policy='\n[roles.harness]\n'
                                                                            'builder = ["fixture.beta"]\n')),
    "classify": (0, "one line per patch operation: two of fixture.alpha's widen, fixture.beta's need narrows",
                 lambda top, a: build_tree(top, overlay=CLASSIFY)),
    "scalar-off-list": (1, "refused: ceiling's value extreme is outside its order",
                        lambda top, a: build_tree(top, overlay=render_amend(ceiling="extreme"))),
    "no-direction": (1, "refused: the schema's ceiling declares widens = []",
                     lambda top, a: build_tree(top, overlay=render_amend(), schema=render_schema(ceiling={"widens": []}))),
    "widenings": (0, "the widening list: fixture.alpha's grants add and ceiling",
                  lambda top, a: build_tree(top, overlay=render_patch("fixture.adopter.alpha-tuned", GOV[0],
                                                                      add='{ grants = ["write"] }', ceiling="high"))),
    "clean": (0, "a narrowing patch and an exclusion nothing needs compose, every check reading rows",
              lambda top, a: build_tree(top, overlay=render_patch("fixture.adopter.beta-tuned", GOV[1],
                                                                  add='{ needs = ["fixture.gamma"] }'),
                                        exclude="fixture.alpha")),
    "rises-raise": (0, "fixture.beta's reach rises from 4 to 8, a widening",
                    lambda top, a: build_rise_plant(top, 8)),
    "rises-text": (0, "fixture.beta's reach rises from the decimal string \"4\" to 8, a widening",
                   lambda top, a: build_rise_plant(top, 8, gov_reach="4")),
    "rises-lower": (1, "refused: an amends and a supersedes each lower reach from 4 to 2, which is never lowered",
                    lambda top, a: build_rise_plant(top, 2, replace=True)),
    "rises-word": (1, "refused: reach's value wide is no number",
                   lambda top, a: build_rise_plant(top, "wide")),
    "rises-unknown": (1, "refused: the schema's reach declares widens = \"falls\", no direction",
                      lambda top, a: build_rise_plant(top, 8, schema=render_schema(reach={"widens": "falls"}))),
    "front-matter-rows": (0, "two role rows read through the glob and role.adopter.triager from the overlay, then "
                             "two workflow rows, each gov row's origin its kind and source its file",
                          lambda top, a: build_front_matter_plant(top)),
    "front-matter-refused": (1, "refused, naming the role file whose tools key is indented and R2",
                             lambda top, a: build_front_matter_plant(top, indent="  ")),
    "front-matter-unarmed": (2, "unarmed, naming the glob no role file matches",
                             lambda top, a: build_front_matter_plant(top, roles=())),
    "pin-reordered": (0, "no edge stale: gov's row reordered and re-wrapped keeps its pin", build_reordered_plant),
    "pin-no-at": (1, "refused, naming the edge with no pin",
                  lambda top, a: build_tree(top, overlay=render_amend().replace(f"@{derive_pin(GOV[0])}", ""))),
    "pin-bad-hash": (1, "refused, naming the edge whose pin is no eight-hex hash",
                     lambda top, a: build_tree(top, overlay=render_patch("fixture.adopter.alpha-tuned", GOV[0],
                                                                         pin="XYZ", **AMEND))),
    "pin-unknown": (1, "refused, naming the edge whose pin matches no revision of gov's row",
                    lambda top, a: build_tree(top, overlay=render_patch("fixture.adopter.alpha-tuned", GOV[0],
                                                                        pin="00000000", **AMEND))),
    "renamed": (0, "the edge follows fixture.alpha2, keeping its pin; fixture.alpha2 amended", build_renamed_plant),
    "split": (0, "both edges orphaned: the amendment held out, the replacement alone, two orders",
              lambda top, a: build_ending_plant(top, "split")),
    "ended": (0, "both edges orphaned: the amendment held out, the replacement alone, two orders",
              lambda top, a: build_ending_plant(top, "remove")),
    "semantic": (None, "stale: order applies and files one order; warn applies, prints and journals; refuse holds",
                 lambda top, a: build_semantic_plant(top)),
    "vanished-field": (0, "the patch of ceiling is held, gov's row as shipped, the reason named",
                       lambda top, a: build_semantic_plant(top, {k: v for k, v in GOV[0].items() if k != "ceiling"})),
    "editorial": (0, "the pin stands behind an editorial record, no edge stale",
                  lambda top, a: build_semantic_plant(top, {**GOV[0], "ceiling": "low, by default"})),
    "states": (0, "one line per gov row, the six states each once",
               lambda top, a: build_states_plant(top)),
}


def run_plant(top, args) -> tuple[list, list, int]:
    """Build the plant in `top`, compose the kind at HEAD. -> `(stdout lines, stderr lines, exit)`."""
    want, what, build = PLANTS[args.plant]
    want = (1 if args.stale == "refuse" else 0) if want is None else want
    if args.plant == "exclude" and args.exclude and args.exclude != "fixture.beta":
        want = 1
    out, err = [f"{SAY}: plant {args.plant} · stale {args.stale} · expects exit {want}: {what}"], []
    build(top, args)
    if args.plant.startswith(FRONT_MATTER):
        return run_front_matter_plant(top, out)
    try:
        schema = orows.read_kind_schema(top, KIND)
        gov = [{**r, "origin": KIND, "source": PACK} for r in
               tomllib.loads(iu.run_git(top, "show", f"HEAD:{PACK}")).get(KIND, [])]
        exclude, policy = ov.read_excluded_tags(top), {}
        try:
            policy = pv.read_tag_policy(top, "HEAD") if exclude else {}
        except pv.PolicyRefused as exc:
            raise ov.OverlayRefused(1, f"{SAY}: red · the composition is refused: policy {exc.key}: {exc.line}") \
                from None
        policy.update({k: [t] for k, _, t in (p.partition("=") for p in args.policy or [])})
        rows, states, held, stale, orders, checks = orows.derive_row_composition(
            KIND, schema, gov, orows.read_overlay_rows(top).get(KIND, []), exclude,
            args.stale, iu.read_change_records(top), policy, legs=orows.read_leg_names(top) if exclude else {})
    except ov.OverlayRefused as exc:
        return out + str(exc).splitlines() + [f"{SAY}: exit 1"], err, 1
    for r in rows:
        shown = {k: v for k, v in r.items() if k != "source"}
        out.append(f"{SAY}: row {r['tag']} · {json.dumps(shown, sort_keys=True, ensure_ascii=False)}")
    out += [f"{SAY}: state {t} · {s}" for t, s in states.items()]
    out += [f"{SAY}: held {h.strip()}" for h in held]
    out += [f"{SAY}: stale {s.strip()}" for s in stale]
    for o in orders:
        first, *rest = o["body"].splitlines()
        out += [f"{SAY}: order {o['kind']} {o['path']} · {first}"] + [f"{SAY}:   {ln}" for ln in rest if ln]
    for o in checks["operations"]:
        how = o["op"] if o["op"] != "set" else f"{o['gov']}->{o['value']}"
        members = f" · {', '.join(o['value'])}" if o["op"] != "set" else ""
        out.append(f"{SAY}: patch {o['tag']} · {o['field']} {how} {o['class']}{members}")
    out += [f"{SAY}: widening {o['row']} -> {o['tag']} · field {o['field']} · {o['op']} {render_value(o['value'])} · "
            f"gov {render_value(o['gov'])}" for o in rc.derive_widenings(checks)]
    out += [f"{SAY}: check {k} · read {n}" for k, n in checks["counts"].items()]
    if args.stale == "warn" and stale:
        err += [f"{SAY}: warn {s.strip()}" for s in stale]
        rev, day = iu.run_git(top, "rev-parse", "HEAD").strip(), datetime.date.today().isoformat()
        pins.write_stale_journal(top, [(day, rev, s.split()[4], *s.split()[2].split("@"), args.stale) for s in stale])
        out += [f"{SAY}: journal {ln}" for ln in (top / pins.JOURNAL).read_text(encoding="utf-8").splitlines()]
    return out + [f"{SAY}: exit 0"], err, 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="row_kind.py")
    ap.add_argument("--plant", required=True, choices=list(PLANTS))
    ap.add_argument("--exclude")
    ap.add_argument("--stale", default="order", choices=pins.STALE_MODES)
    ap.add_argument("--policy", action="append", metavar="KEY=TAG")
    args = ap.parse_args(argv)
    iu.load_memory_tree_path()
    from deviation_join import remove_tree, set_env_aside
    from tree_lib import GIT_ENV_LEAKS
    top = pathlib.Path(tempfile.mkdtemp(prefix="rowkind-"))
    try:
        with set_env_aside(GIT_ENV_LEAKS):
            iu.run_git(top, "init", "-q")
            iu.run_git(top, "config", "core.autocrlf", "false")
            try:
                out, err, rc = run_plant(top, args)
            except (ValueError, OSError, iu.LevelError) as exc:
                out, err, rc = [f"{SAY}: plant {args.plant} could not be built: {exc}"], [], 2
    finally:
        remove_tree(top)   # not ignore_errors: git's objects are read-only on Windows
    sys.stdout.buffer.write("".join(f"{ln}\n" for ln in out).encode("utf-8"))
    sys.stderr.buffer.write("".join(f"{ln}\n" for ln in err).encode("utf-8"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
