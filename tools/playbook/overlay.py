#!/usr/bin/env python3
"""overlay.py — the repository's instruction overlay, `.governance/instructions.toml` (PLAY-dOrderedCharter-32).

    python overlay.py check                       # gov's units' classes, the overlay's units, keys and states
    python overlay.py --fixture [--plant <case>]  # the plants, each in a throwaway repository

THE HOME. The overlay holds the repository's own `[[unit]]` rows, in the kit manifests' row grammar, and its
`[[policy]]` rows. `read_overlay` is the composers' one reader of it: the blob `HEAD:<overlay>` through
`git cat-file`, never the index and never the working tree, through `parse_unit_rows` (PLAY-dOrderedCharter-46
S1). Its `state` says which: `landed`; `absent`, a commit holding no such file, the empty overlay; `unarmed`,
no commit at all, the empty overlay each render names in `UNARMED_LINE`; `candidate`, text a write verb's
render passes in place of the blob, which every check verb refuses. Every unit it
returns carries `origin = "repository"`. It refuses a row the schema check reds in the `repo` namespace, a
typed origin and a typed `fixed` class among them, a unit at level 1, 6 or 7, and a `[[policy]]` key
outside `adopter.`, whose tag `policy.adopter.<name>` it derives from the key.

THE COMPOSITION. `derive_unit_composition` walks gov's units in their order: one `instructions.exclude`
lists is skipped (`excluded`), a repository unit whose `edges` hold `supersedes=<tag>@<hash8>` renders in
its place (`replaced`), one holding `amends=<tag>@<hash8>` renders right after it (`amended`), else gov's
unit renders (`unchanged`). A repository unit with no such edge takes its place by level after gov's units
of the same level. A repository unit whose `trigger` is `policy.adopter.<name>.<value>` composes only while
`policy.py get adopter.<name> --rev HEAD` prints that value. `read_excluded_tags` is the one reader of
`instructions.exclude`. `derive_slot_units` is what one unit slot of the renderer of record renders.

THE CLASS. A gov unit is fixed when it is a `principle.` unit, when a `fixed-by` entry resolves, or when it
declares no class; open only when it declares `class = "open"` and nothing fixes it. `check_fixed_sources`
is the one resolver of a `fixed-by` list, `principle=<tag>`, `floor=<tag>` or `parser=<path#symbol>`. A
fixed unit refuses an `amends`, a `supersedes` and an exclusion, each naming the source that fixes it.

THE WRITER. `write_overlay_units` adds rows to the overlay by level then tag, refusing a tag it holds with
the file left byte-identical; the command's overlay `add` and the upgrade step are its callers.

CHECK reds a gov unit tagged `repo.`, a gov unit whose `trigger` reads a `policy.adopter.` key, a `fixed-by`
list that does not resolve, a unit typing `class = "fixed"` or declaring `open` while a source fixes it, and
every refusal of the reader and the composition; it prints each gov unit's class, each `[[policy]]` key with
its derived tag, and each gov unit's state. Exit 0 green, 1 red or refused, 2 usage.
"""
from __future__ import annotations

import functools
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import dataclass, field

sys.dont_write_bytecode = True

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import instruction_units as iu  # noqa: E402
from policy_value import PolicyRefused, read_policy_value  # noqa: E402

SAY = "overlay"
ORIGIN = "repository"
NS = "repo"
BARRED_LEVELS = (1, 6, 7)
EDGE_TYPES = ("amends", "supersedes")
FIXED_TYPES = ("principle", "floor", "parser")
ADOPTER_WHEN = "policy.adopter."
ADOPTER_KEY = "adopter."
UNDECLARED = "its undeclared class"
UNARMED_LINE = f"{SAY} — unarmed: no commit yet, so there is no landed revision to read"


class OverlayRefused(ValueError):
    """A read, composition or write the overlay refuses: `code` the exit, the message its lines."""

    def __init__(self, code, line):
        super().__init__(line)
        self.code = code


@dataclass(frozen=True)
class Overlay:
    """The overlay at HEAD: its `Unit`s, each `origin` the repository, `(key, tag)` per `[[policy]]` row, and
    its `state`: `landed`, `absent`, `unarmed` or `candidate`. `tables` is each other top-level key with its
    value from the one parse, the row tables `overlay_rows.read_overlay_rows` reads (PLAY-dOrderedCharter-35 S1)."""
    units: tuple
    policies: tuple
    state: str
    tables: dict = field(default_factory=dict, hash=False)


def check_born(root) -> bool:
    """Whether HEAD names a commit at `root`: an unborn HEAD reads as the `unarmed` overlay and the default
    exclusion set, since no commit holds a policy file (PLAY-dOrderedCharter-46 S2, S6)."""
    return not subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "-q", "HEAD"],
                              capture_output=True).returncode


def read_landed_text(root) -> str | None:
    """The overlay's blob at HEAD through `git cat-file`, None where HEAD holds no such file."""
    if not iu.run_git(root, "ls-tree", "--name-only", "HEAD", "--", iu.OVERLAY).strip():
        return None
    return iu.run_git(root, "cat-file", "blob", f"HEAD:{iu.OVERLAY}")


def read_overlay(root, candidate: str | None = None) -> Overlay:
    """S1 to S3 of PLAY-dOrderedCharter-46: the overlay at HEAD, or `candidate`'s text in its place; every red
    of its rows raises one OverlayRefused naming each row."""
    if candidate is not None:
        text, state = candidate, "candidate"
    elif not check_born(root):
        return Overlay((), (), "unarmed")
    else:
        text, state = read_landed_text(root), "landed"
    if text is None:
        return Overlay((), (), "absent")
    units, faults = iu.parse_unit_rows(text, iu.OVERLAY, ORIGIN)
    reds = [f"{SAY}: red · {f}" for f in faults]
    doc = {} if faults and not units else tomllib.loads(text)
    tables = doc.get("unit") or []
    for u in units:
        reds += iu.check_unit_row(u, tables[u.index - 1], NS)
        if u.level in BARRED_LEVELS:
            reds.append(f"{SAY}: red · {iu.OVERLAY} · {u.tag} · level {u.level} is no repository level: the "
                        f"repository writes neither the card, the task nor memory · remedy: place it at 0, 2 to 5")
    policies = []
    rows = doc.get("policy") or []
    for i, row in enumerate(rows if isinstance(rows, list) else [rows], 1):
        key = row.get("key") if isinstance(row, dict) else None
        if not isinstance(key, str) or not key.startswith(ADOPTER_KEY) or key.count(".") != 1:
            reds.append(f"{SAY}: red · {iu.OVERLAY} · [[policy]] row {i} ({key}) · a repository key is "
                        f"adopter.<name>, never a catalogue key · remedy: key it under adopter.")
        else:
            policies.append((key, f"policy.{key}"))
    if reds:
        raise OverlayRefused(1, "\n".join(reds))
    return Overlay(tuple(units), tuple(policies), state, {k: v for k, v in doc.items() if k not in ("unit", "policy")})


def derive_policy_reader(root):
    """The composition's policy read: `read_policy_value` over `root` at `rev` HEAD, as `read_load` binds it."""
    return functools.partial(read_policy_value, root=root, rev="HEAD")


def read_excluded_tags(root) -> set:
    """S4: `instructions.exclude`'s members at HEAD, the key's one reader; a refused read refuses the
    composition, naming the key and the reader's line. An unborn HEAD reads the default, the empty set."""
    if not check_born(root):
        return set()
    policy_reader = derive_policy_reader(root)
    try:
        return {ln.strip() for ln in policy_reader("instructions.exclude")[0] if ln.strip()}
    except PolicyRefused as exc:
        raise OverlayRefused(1, f"{SAY}: red · the composition is refused: policy {exc.key}: {exc.line}") from None


def check_fixed_sources(entries, root) -> list:
    """S5: one red per `fixed-by` entry that is no source, naming it: an empty list, a type outside
    principle, floor and parser, a `principle=` tag no `[[principle]]` row holds, a `floor=` source while no
    namespace registers `floor`, and a `parser=<path#symbol>` whose path is untracked or defines no symbol."""
    if not entries:
        return [f"{SAY}: red · fixed-by · the list is empty · remedy: name a source, or drop the field"]
    import core
    import positional
    reds = []
    for entry in entries:
        kind, _, arg = entry.partition("=")
        why = None
        if kind not in FIXED_TYPES or not arg:
            why = f"is no `<type>=<source>` of {', '.join(FIXED_TYPES)}"
        elif kind == "principle":
            rows = core.read_toml_rows(iu.derive_kit_file(root, "principles.toml"), "principle") or []
            why = None if arg in {r.get("tag") for r in rows} else "names no [[principle]] row"
        elif kind == "floor":
            if "floor" not in iu.read_namespace_words():
                why = "names the `floor` namespace, which no row of the registry registers"
            elif not iu.load_resolver(root)(arg):
                why = "resolves to no floor"
        else:
            path, _, symbol = arg.partition("#")
            tracked = path and symbol and iu.run_git(root, "ls-files", "--", path).strip() == path
            text = pathlib.Path(root, path).read_text(encoding="utf-8", errors="replace") if tracked else ""
            why = None if tracked and symbol in positional.read_symbol_defs(path, text) else \
                "names a path git does not track or a symbol it does not define"
        if why:
            reds.append(f"{SAY}: red · fixed-by · {entry!r} {why} · remedy: name a source that resolves")
    return reds


def derive_fixing_sources(unit, root) -> list:
    """The sources that fix `unit`: `principle` for a `principle.` unit, then each `fixed-by` entry that resolves."""
    found = ["principle"] if (unit.tag or "").startswith("principle.") else []
    return found + [e for e in unit.fixed_by or () if not check_fixed_sources([e], root)]


def derive_unit_class(unit, sources) -> str:
    """S5: `open` only where the unit declares `open` and no source fixes it; `fixed` otherwise."""
    return "open" if unit.klass == "open" and not sources else "fixed"


def derive_fixed_units(gov_units, root) -> dict:
    """`{tag: the source that fixes it}` of each fixed gov unit, an undeclared class named as one."""
    out = {}
    for u in gov_units:
        sources = derive_fixing_sources(u, root)
        if derive_unit_class(u, sources) == "fixed":
            out[u.tag] = sources[0] if sources else UNDECLARED
    return out


def derive_edge_targets(unit) -> list:
    """`(type, gov tag)` per `amends` or `supersedes` target of `unit`, its pin cut."""
    return [(kind, t.split("@", 1)[0]) for kind, _, rest in (e.partition("=") for e in unit.edges)
            if kind in EDGE_TYPES for t in rest.split(",")]


def check_when(unit, policy_reader) -> bool:
    """Whether `unit` composes under its `trigger`: always, unless it is `policy.adopter.<name>.<value>`, then
    only while the key reads that value. A refused read refuses the composition, naming the unit and key."""
    trigger = unit.trigger or ""
    if not trigger.startswith(ADOPTER_WHEN):
        return True
    name, _, value = trigger[len(ADOPTER_WHEN):].partition(".")
    try:
        return value in policy_reader(f"{ADOPTER_KEY}{name}")[0]
    except PolicyRefused as exc:
        raise OverlayRefused(1, f"{SAY}: red · {unit.tag} · the composition is refused: policy {exc.key}: "
                                f"{exc.line}") from None


def derive_unit_composition(gov_units, overlay_units, exclude, *, fixed=None, policy_reader=None) -> tuple:
    """S4: `(units, states)`, the ordered units a document renders and `{gov tag: unchanged | amended |
    replaced | excluded}`. `fixed` is `derive_fixed_units`', `policy_reader` reads a `when` key. Writes nothing."""
    fixed = fixed or {}
    gov = {u.tag for u in gov_units}
    amends, supersedes, free, reds = {}, {}, [], []
    for u in overlay_units:
        if policy_reader is not None and not check_when(u, policy_reader):
            continue
        edges = derive_edge_targets(u)
        if not edges:
            free.append(u)
        for kind, tag in edges:
            if tag not in gov:
                reds.append(f"{SAY}: red · {u.tag} {kind} {tag}, which names no gov unit · remedy: pin a gov unit's tag")
            elif tag in fixed:
                reds.append(f"{SAY}: red · {u.tag} {kind} {tag}, which is fixed by {fixed[tag]} · remedy: add a unit "
                            f"of your own instead")
            else:
                (supersedes if kind == "supersedes" else amends).setdefault(tag, []).append(u)
    reds += [f"{SAY}: red · instructions.exclude lists {tag}, which is fixed by {fixed[tag]} · remedy: drop it "
             f"from the set" for tag in sorted(exclude) if tag in fixed]
    if reds:
        raise OverlayRefused(1, "\n".join(reds))
    placed, states = [], {}
    for g in gov_units:
        level = len(iu.LEVELS) if g.level is None else g.level
        if g.tag in exclude:
            states[g.tag] = "excluded"
            continue
        here = supersedes.get(g.tag) or [g]
        placed += [(level, u) for u in here + amends.get(g.tag, [])]
        states[g.tag] = "replaced" if g.tag in supersedes else "amended" if g.tag in amends else "unchanged"
    placed += [(len(iu.LEVELS) if u.level is None else u.level, u) for u in free]
    return [u for _level, u in sorted(placed, key=lambda p: p[0])], states   # stable: gov's first at a level


def derive_slot_units(gov_units, overlay_units, selector, exclude, fixed, policy_reader) -> tuple:
    """One unit slot's composition: the gov units `selector` selects, the repository units it selects that
    carry no edge, and those whose edge targets a selected gov unit."""
    chosen = iu.derive_unit_selection(gov_units, selector)
    held = {u.tag for u in chosen}
    # ponytail: a unit amending gov units of two slots refuses in each; split it in two if one ever must
    picked = [u for u in overlay_units if {t for _k, t in derive_edge_targets(u)} & held
              or (not derive_edge_targets(u) and iu.derive_unit_selection([u], selector))]
    return derive_unit_composition(chosen, picked, exclude, fixed=fixed, policy_reader=policy_reader)


def derive_overlay_text(text, rows) -> str:
    """S8: the overlay's text with `rows` added, each before the first `[[unit]]` that sorts after it by
    level then tag, else after the last; a tag the file or `rows` already holds raises OverlayRefused, exit 2."""
    from instructions_edit import render_row
    units, faults = iu.parse_unit_rows(text, iu.OVERLAY)
    if faults:
        raise OverlayRefused(1, "\n".join(f"{SAY}: red · {f}" for f in faults))
    held, dup = {u.tag for u in units}, []
    for r in rows:
        if r.get("tag") in held:
            dup.append(r.get("tag"))
        held.add(r.get("tag"))
    if dup:
        raise OverlayRefused(2, f"{SAY}: refused · {iu.OVERLAY} already holds {', '.join(map(str, dup))} · "
                                f"nothing written")

    def derive_key(level, tag):
        return (len(iu.LEVELS) if not isinstance(level, int) else level, tag)

    chunks = re.split(r"(?m)^(?=\[)", text) if text else []
    keys, it = [], iter(units)
    for chunk in chunks:
        u = next(it) if chunk.startswith(iu.UNIT_HEADER) else None
        keys.append(None if u is None else derive_key(u.level, u.tag))
    for r in sorted(rows, key=lambda r: derive_key(r.get("level"), r.get("tag"))):
        key = derive_key(r.get("level"), r.get("tag"))
        at = next((i for i, k in enumerate(keys) if k is not None and k > key), None)
        if at is None:
            at = max((i + 1 for i, k in enumerate(keys) if k is not None), default=len(chunks))
        if at and chunks[at - 1].strip() and not chunks[at - 1].endswith("\n\n"):
            chunks[at - 1] = chunks[at - 1].rstrip("\r\n") + "\n\n"
        chunks.insert(at, render_row(r) + ("\n" if at < len(chunks) else ""))
        keys.insert(at, key)
    return "".join(chunks)


def write_overlay_units(target, rows):
    """S8: the one function adding rows to the overlay file `target`; a refusal writes nothing."""
    path = pathlib.Path(target)
    text = path.read_bytes().decode("utf-8") if path.is_file() else ""
    out = derive_overlay_text(text, rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(out.encode("utf-8"))


def check_gov_units(units, tables, root) -> tuple[list, list]:
    """`(reds, lines)` over gov's units: a `repo.` tag, a `when` reading a repository key, a `fixed-by` red,
    a typed `fixed` class and a declared `open` a source fixes, each red; each unit's class a line."""
    reds, lines = [], []
    for u in units:
        where = f"{SAY}: red · {u.path} · {u.tag}"
        row = tables[u.path][u.index - 1]
        if (u.tag or "").startswith(f"{NS}."):
            reds.append(f"{where} · a gov row holds a `repo.` tag, the repository's namespace · remedy: tag it unit.")
        if (u.trigger or "").startswith(ADOPTER_WHEN):
            reds.append(f"{where} · its trigger {u.trigger} reads a repository key, which only repository units "
                        f"read · remedy: drop the trigger")
        if u.fixed_by is not None:
            reds += [f"{where} · {r.split(' · ', 1)[1]}" for r in check_fixed_sources(u.fixed_by, root)]
        fault = iu.check_declared_class(row)
        if fault:
            reds.append(f"{where} · `class` {fault[0]} · remedy: {fault[1]}")
        sources = derive_fixing_sources(u, root)
        if u.klass == "open" and sources:
            reds.append(f"{where} · declares `open` while {sources[0]} fixes it · remedy: drop the declaration")
        lines.append(f"{SAY}: class · {u.tag} · {derive_unit_class(u, sources)}"
                     + (f" · {sources[0]}" if sources else ""))
    return reds, lines


def run_check(root) -> tuple[list, int]:
    """CHECK over the tree at `root`."""
    root = pathlib.Path(root)
    units, faults = iu.read_unit_rows(root)
    reds = [f"{SAY}: red · {f}" for f in faults]
    tables = {u.path: tomllib.loads((root / u.path).read_text(encoding="utf-8"))["unit"] for u in units}
    more, lines = check_gov_units(units, tables, root)
    reds += more
    try:
        repo = read_overlay(root)
        lines += [f"{SAY}: policy · {key} · tag {tag}" for key, tag in repo.policies]
        lines += [f"{SAY}: unit · {u.tag} · level {u.level}" for u in repo.units]
        exclude = read_excluded_tags(root) if units else set()
        composed, states = derive_unit_composition(units, repo.units, exclude, fixed=derive_fixed_units(units, root),
                                                   policy_reader=derive_policy_reader(root))
        lines += [f"{SAY}: state · {tag} · {state}" for tag, state in states.items()]
    except OverlayRefused as exc:
        reds += str(exc).splitlines()
    armed = f"{len(units)} gov unit(s)" if units or reds else "unarmed: the tree holds no unit row and no overlay"
    return reds + lines + [f"{SAY}: check · {armed} · {len(reds)} red"], 1 if reds else 0


# ------------------------------------------------------------------------------------------ the fixture

FX_KIT = "tools/alpha"
FX_MANIFEST = f"{FX_KIT}/instructions.toml"
FX_GRAMMAR = f"{FX_KIT}/grammar.py"
FX_POLICY = ".governance/policy.toml"
FX_GUARDED = "tools/policy/guarded-paths.txt"
FX_OPEN, FX_FIXED, FX_PRINCIPLE = "unit.open-rule", "unit.fixed-rule", "principle.p1"
FX_WHEN = "policy.adopter.release-train.weekly"
FX_KEY_ROW = ('[[policy]]\nkey = "adopter.release-train"\nvalues = ["weekly", "monthly"]\ndefault = "weekly"\n'
              'summary = "how often this repository cuts a release"\n'
              'usage = "set [adopter] release-train in .governance/policy.toml"\n')


def render_fx_row(tag, level=3, text="MUST hold.", **more) -> str:
    from instructions_edit import render_row
    return render_row({"tag": tag, "level": level, "type": "directive", "scope": ["reader.every"],
                       "trigger": "always", "text": text, **more}) + "\n"


def derive_gov_rows() -> str:
    return (render_fx_row(FX_PRINCIPLE, 2, "MUST keep the principle.") + render_fx_row(FX_OPEN, text="MUST open.",
            **{"class": "open"}) + render_fx_row(FX_FIXED, text="MUST stay."))


def build_fixture(c, gov=None, overlay=None, policy=None, extra=None):
    """A committed tree: a kit `alpha` with gov's rows, the overlay and the policy file where given."""
    files = {f"{FX_KIT}/kit.toml": 'id = "alpha"\n', FX_MANIFEST: derive_gov_rows() if gov is None else gov,
             FX_GRAMMAR: "def parse_grammar(text):\n    return text\n"}
    files.update({iu.OVERLAY: overlay} if overlay is not None else {})
    files.update({FX_POLICY: policy} if policy is not None else {})
    files.update(extra or {})
    for rel, text in files.items():
        c.write_file(rel, text)
    iu.run_commit(c.top, "the fixture")


def run_fx_check(c) -> tuple[int, str]:
    lines, rc = run_check(c.top)
    return rc, "\n".join(lines)


def check_red(c, label, *needles):
    rc, said = run_fx_check(c)
    c.check(label, rc == 1 and all(n in said for n in needles), f"rc {rc} · {said}")


def derive_fx_composition(c, exclude=frozenset()) -> tuple:
    units = iu.read_units(c.top)
    return derive_unit_composition(units, read_overlay(c.top).units, set(exclude), fixed=derive_fixed_units(units, c.top),
                                   policy_reader=derive_policy_reader(c.top))


def render_fx_slot(c) -> str:
    import render_playbook
    return render_playbook.render_unit_slots("<!-- units: reader.every -->\n", c.top, [])


def arm_typed_origin(c):
    build_fixture(c)
    empty = read_overlay(c.top)
    plain = iu.render_units(iu.derive_unit_selection(iu.read_units(c.top), iu.EVERY), None) + "\n"
    c.check("an absent overlay reads zero units", empty.units == () and empty.policies == (), str(empty))
    c.check("the charter renders byte-identical with no overlay", render_fx_slot(c) == plain, render_fx_slot(c))
    build_fixture(c, overlay=render_fx_row("repo.local", origin="playbook"))
    check_red(c, "a typed origin is refused naming the row", "repo.local", "`origin`")


def arm_foreign_tag(c):
    build_fixture(c, overlay=render_fx_row("practice.local-rule"))
    check_red(c, "an overlay unit outside repo. is refused", "practice.local-rule", "`repo` namespace")


def arm_repo_in_gov(c):
    build_fixture(c, gov=derive_gov_rows() + render_fx_row("repo.shipped"))
    check_red(c, "gov shipping a repo. tag is refused", "repo.shipped", "`repo.` tag")


def arm_add_level_3(c):
    build_fixture(c, overlay=render_fx_row("repo.local", text="MUST mind the local rule."))
    lines = render_fx_slot(c).splitlines()
    c.check("the level-3 repository unit renders after gov's level-3 units",
            lines == ["MUST keep the principle.", "MUST open.", "MUST stay.", "MUST mind the local rule."], str(lines))


def arm_add_level_1(c):
    build_fixture(c, overlay=render_fx_row("repo.card", level=1))
    check_red(c, "a level-1 repository unit is refused", "repo.card", "level 1")


def arm_amends(c):
    edge = f"amends={FX_OPEN}@{iu.derive_unit_pin('MUST open.')}"
    build_fixture(c, overlay=render_fx_row("repo.more", text="MUST open wider.", edges=[edge]))
    units, states = derive_fx_composition(c)
    tags = [u.tag for u in units]
    c.check("gov's unit then the amendment, state amended", tags == [FX_PRINCIPLE, FX_OPEN, "repo.more", FX_FIXED]
            and states[FX_OPEN] == "amended", f"{tags} {states}")


def arm_supersedes(c):
    edge = f"supersedes={FX_OPEN}@{iu.derive_unit_pin('MUST open.')}"
    build_fixture(c, overlay=render_fx_row("repo.instead", text="MUST open ours.", edges=[edge]))
    units, states = derive_fx_composition(c)
    tags = [u.tag for u in units]
    c.check("the replacement alone in gov's place, state replaced", tags == [FX_PRINCIPLE, "repo.instead", FX_FIXED]
            and states[FX_OPEN] == "replaced", f"{tags} {states}")


def arm_exclude(c):
    build_fixture(c)
    units, states = derive_fx_composition(c, read_excluded_tags(c.top))
    c.check("with no [instructions] table every gov unit composes", len(units) == 3 and set(states.values())
            == {"unchanged"}, f"{units} {states}")
    build_fixture(c, policy=f'[instructions]\nexclude = ["{FX_OPEN}"]\n')
    units, states = derive_fx_composition(c, read_excluded_tags(c.top))
    c.check("an excluded open unit is absent, state excluded", FX_OPEN not in [u.tag for u in units]
            and states[FX_OPEN] == "excluded", f"{units} {states}")
    needle = "policy_reader(" + '"instructions.exclude"'   # split, so this line is no read the grep counts
    said = iu.run_git(KIT_DIR, "grep", "--untracked", "-n", "-F", needle, "--", ".")
    c.check("one line reads the key, the overlay module's", len(said.splitlines()) == 1 and "overlay.py" in said, said)


def arm_parsed_open(c):
    rows = derive_gov_rows() + render_fx_row("unit.parsed", **{"class": "open", "fixed-by": [f"parser={FX_GRAMMAR}#parse_grammar"]})
    build_fixture(c, gov=rows)
    check_red(c, "a parsed unit declared open is red naming the parser", "unit.parsed", "parser=")
    fixed = derive_fixed_units(iu.read_units(c.top), c.top)
    c.check("a unit declaring no class reads fixed", fixed.get(FX_FIXED) == UNDECLARED and FX_OPEN not in fixed, str(fixed))


def arm_typed_fixed(c):
    build_fixture(c, gov=derive_gov_rows() + render_fx_row("unit.typed", **{"class": "fixed"}))
    check_red(c, "a typed fixed class is refused", "unit.typed", "derived")


def arm_fixed_by(c, entries, needle):
    build_fixture(c, gov=derive_gov_rows() + render_fx_row("unit.sourced", **{"fixed-by": entries}))
    check_red(c, f"fixed-by {entries} is refused naming the entry", "unit.sourced", needle)


def arm_fixed_target(c, kind):
    pin = f"{FX_PRINCIPLE}@{iu.derive_unit_pin('MUST keep the principle.')}"
    if kind == "exclude":
        build_fixture(c, policy=f'[instructions]\nexclude = ["{FX_PRINCIPLE}"]\n')
    else:
        build_fixture(c, overlay=render_fx_row("repo.over", edges=[f"{kind}={pin}"]))
    check_red(c, f"{kind} of a principle unit is refused naming it and principle", FX_PRINCIPLE, "fixed by principle")


def run_policy_cli(c, *argv) -> tuple[int, str]:
    from policy_value import resolve_kit_dir
    kit = resolve_kit_dir("policy", "policy.py", KIT_DIR)
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    done = subprocess.run([sys.executable, str(kit / argv[0]), *argv[1:]], cwd=c.top, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL, env=env)
    return done.returncode, done.stdout + done.stderr


def arm_adopter_key(c):
    unit = render_fx_row("repo.release-train", text="MUST cut the release on Monday.", trigger=FX_WHEN)
    build_fixture(c, overlay=unit + FX_KEY_ROW, policy='[adopter]\nrelease-train = "monthly"\n',
                  extra={FX_GUARDED: ".governance/policy.json\n"})
    got = read_policy_value("adopter.release-train", c.top, "HEAD")[0]
    c.check("get reads the committed repository key", got == ["monthly"], str(got))
    rc, said = run_fx_check(c)
    c.check("check prints the key with its tag on a line apart from the unit's",
            rc == 0 and f"{SAY}: policy · adopter.release-train · tag policy.adopter.release-train" in said.splitlines()
            and f"{SAY}: unit · repo.release-train · level 3" in said.splitlines(), said)
    rc, said = run_policy_cli(c, "policy.py", "mirror", "--write")
    iu.run_git(c.top, "add", "-A")
    iu.run_commit(c.top, "the mirror")
    c.write_file(iu.OVERLAY, unit + FX_KEY_ROW.replace('"weekly", "monthly"', '"weekly", "monthly", "yearly"'))
    iu.run_commit(c.top, "the overlay alone")
    rc, said = run_policy_cli(c, "policy.py", "mirror", "--check")
    c.check("an overlay-only commit stales the mirror", rc == 1 and "legacy_blobs" in said, f"{rc} {said}")
    rc, said = run_policy_cli(c, "policy.py", "mirror", "--write")
    rc2, said2 = run_policy_cli(c, "policy.py", "mirror", "--check")
    c.check("mirror --write makes it fresh", rc == 0 and rc2 == 0, f"{said} {said2}")
    c.write_file(iu.OVERLAY, unit + FX_KEY_ROW)
    c.write_file(".governance/policy.json", (c.top / ".governance/policy.json").read_text(encoding="utf-8"))
    from policy_value import resolve_kit_dir
    guard = resolve_kit_dir("policy", "guard.py", KIT_DIR) / "guard.py"
    done = subprocess.run([sys.executable, str(guard), "--staged"], cwd=c.top, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    c.check("the guard refuses a staged mirror while the overlay differs from HEAD", done.returncode == 1 and
            f"its input {iu.OVERLAY} is staged changed" in done.stdout, done.stdout + done.stderr)
    for name, overlay, policy, needle in (
            ("daily", FX_KEY_ROW, '[adopter]\nrelease-train = "daily"\n', "adopter.release-train"),
            ("an undeclared key", FX_KEY_ROW, '[adopter]\nother = "x"\n', "adopter.other"),
            ("a catalogue key", FX_KEY_ROW.replace("adopter.release-train", "budgets.enforce"), "", "budgets.enforce")):
        top = pathlib.Path(tempfile.mkdtemp(prefix="overlay-fx-"))
        try:
            iu.run_git(top, "init", "-q")
            iu.run_git(top, "config", "core.autocrlf", "false")
            sub = iu.Case(top, c.out)
            build_fixture(sub, overlay=overlay, policy=policy)
            rc, said = run_policy_cli(sub, "policy.py", "get", "adopter.release-train", "--rev", "HEAD")
            c.check(f"get refuses {name}, naming the key", rc == 2 and needle in said, f"{rc} {said}")
        finally:
            shutil.rmtree(top, ignore_errors=True)


def arm_gov_reads_adopter(c):
    build_fixture(c, gov=derive_gov_rows() + render_fx_row("unit.reader", trigger=FX_WHEN))
    check_red(c, "a gov unit reading a repository key is refused", "unit.reader", FX_WHEN)
    unit = render_fx_row("repo.weekly", text="MUST ship weekly.", trigger=FX_WHEN)
    for value, want in (("weekly", True), ("monthly", False)):
        build_fixture(c, overlay=unit + FX_KEY_ROW, policy=f'[adopter]\nrelease-train = "{value}"\n')
        tags = [u.tag for u in derive_fx_composition(c)[0]]
        c.check(f"a repository unit's when composes it only while weekly ({value})", ("repo.weekly" in tags) == want,
                str(tags))


def arm_write_order(c):
    path = c.top / iu.OVERLAY
    path.parent.mkdir(parents=True)
    path.write_bytes(render_fx_row("repo.m").encode("utf-8") + FX_KEY_ROW.encode("utf-8"))
    write_overlay_units(path, [{"tag": "repo.b", "level": 3, "type": "directive", "text": "MUST b."},
                               {"tag": "repo.a", "level": 0, "type": "fact", "source": "policy:adopter.release-train"}])
    text = path.read_text(encoding="utf-8")
    tags = [u.tag for u in iu.parse_unit_rows(text, iu.OVERLAY)[0]]
    c.check("two rows land by level then tag", tags == ["repo.a", "repo.b", "repo.m"] and FX_KEY_ROW in text, text)
    before = path.read_bytes()
    try:
        write_overlay_units(path, [{"tag": "repo.b", "level": 3, "type": "directive", "text": "MUST b."}])
        code = 0
    except OverlayRefused as exc:
        code = exc.code
    c.check("a tag already present exits 2 and leaves the file byte-identical", code == 2 and path.read_bytes() == before,
            str(code))


LOCAL_ROW = render_fx_row("repo.local", text="MUST mind the local rule.")


def write_slot_files(c):
    """Staged, not committed: gov's kit and a charter template holding one unit slot and no practice region."""
    for rel, text in {f"{FX_KIT}/kit.toml": 'id = "alpha"\n', FX_MANIFEST: derive_gov_rows(),
                      ".governance/deploy.toml": iu.SLOT_DEPLOY, iu.derive_template_rel(): iu.SLOT_TEMPLATE.format("reader.every")}.items():
        c.write_file(rel, text)


def run_render_cli(c, *argv) -> tuple[int, str]:
    """The renderer as its own process over the fixture, so an argparse refusal is an exit, not a raise."""
    done = subprocess.run([sys.executable, str(KIT_DIR / "render_playbook.py"), "--target", str(c.top), *argv],
                          capture_output=True, text=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    return done.returncode, done.stdout + done.stderr


def arm_staged_not_landed(c):
    build_fixture(c)
    c.write_file(iu.OVERLAY, LOCAL_ROW)
    got = read_overlay(c.top)
    c.check("a row staged and not committed is absent", got.units == () and got.state == "absent", str(got))
    iu.run_commit(c.top, "the overlay")
    got = read_overlay(c.top)
    c.check("the row is read once committed", [u.tag for u in got.units] == ["repo.local"] and got.state == "landed",
            str(got))


def arm_unborn_head(c):
    write_slot_files(c)
    got = read_overlay(c.top)
    c.check("an unborn HEAD reads the unarmed overlay", got.units == () and got.state == "unarmed", str(got))
    rc, said = iu.run_render(c.top)
    c.check("a render prints the unarmed line once and exits 0", rc == 0 and said.count(UNARMED_LINE) == 1, said)


def arm_check_refuses_candidate(c):
    write_slot_files(c)
    iu.run_commit(c.top, "the charter's inputs")
    candidate = c.top.parent / f"{c.top.name}-candidate.toml"
    candidate.write_bytes(LOCAL_ROW.encode("utf-8"))
    try:
        for verb in (["--check-render", "--scope", "charter"], ["--check-render"], ["--check"]):
            rc, said = run_render_cli(c, *verb, "--overlay-from", str(candidate))
            c.check(f"{' '.join(verb)} refuses a candidate, exit 2 naming the flag", rc == 2 and "--overlay-from" in said,
                    f"rc {rc} · {said}")
        rc, said = run_render_cli(c, "--overlay-from", str(candidate))
        charter = (c.top / "AGENTS.md").read_text(encoding="utf-8") if rc == 0 else ""
        c.check("a render verb reads the candidate, exit 0, naming it", rc == 0 and "MUST mind the local rule." in charter
                and f"{SAY} — candidate:" in said, f"rc {rc} · {said} · {charter}")
    finally:
        candidate.unlink(missing_ok=True)


def arm_write_then_render(c):
    import gov_tag
    import instructions_edit as ie
    root = ie.build_tree(c, ie.GUARD_POINT)
    gov_tag.write_commit(root, {iu.derive_tool_rel(KIT_DIR.name, iu.RENDERERS_TABLE): '[[target]]\npaths = ["AGENTS.md"]\n'
                                'renderer = "playbook:charter"\n', ".governance/deploy.toml": iu.SLOT_DEPLOY,
                                iu.derive_template_rel(): iu.SLOT_TEMPLATE.format("reader.every")}, "a rendered charter")
    rc, said = ie.run_cli(root, "add", "--manifest", "overlay", "--tag", "repo.local", "--type", "directive", "--level",
                          "3", "--trigger", "always", "--scope", "reader.every", "--text", "MUST mind the local rule.",
                          *ie.FX_RECORD, tty=True)
    charter = (root / "AGENTS.md").read_text(encoding="utf-8") if (root / "AGENTS.md").is_file() else ""
    c.check("the write's render holds the new overlay row in the same command",
            rc == 0 and "MUST mind the local rule." in charter, f"rc {rc} · {said} · {charter}")
    iu.run_git(root, "add", "-A")
    iu.run_commit(root, "the write")
    rc, said = iu.run_render(root, "--check-render", "--scope", "charter")
    c.check("once the overlay is committed the render gate agrees", rc == 0, said)


def arm_policy_at_head(c):
    iu.run_git(c.top, "checkout", "-q", "-b", "main")
    build_fixture(c)
    iu.run_git(c.top, "remote", "add", "origin", "https://example.invalid/fixture.git")
    iu.run_git(c.top, "update-ref", "refs/remotes/origin/main", "HEAD")
    iu.run_git(c.top, "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
    build_fixture(c, policy=f'[instructions]\nexclude = ["{FX_OPEN}"]\n')
    landed = read_policy_value("instructions.exclude", c.top)[0]
    c.check("the landed ref is one commit behind and lacks the exclusion", FX_OPEN not in landed, str(landed))
    units, states = derive_fx_composition(c, read_excluded_tags(c.top))
    c.check("the composition reads the policy at HEAD: the unit is absent, state excluded",
            FX_OPEN not in [u.tag for u in units] and states[FX_OPEN] == "excluded", f"{units} {states}")
    c.check("the composed document lacks the unit", "MUST open." not in render_fx_slot(c), render_fx_slot(c))


PLANTS = {"typed-origin": arm_typed_origin, "foreign-tag": arm_foreign_tag, "repo-in-gov": arm_repo_in_gov,
          "add-level-3": arm_add_level_3, "add-level-1": arm_add_level_1, "amends": arm_amends,
          "supersedes": arm_supersedes, "exclude": arm_exclude, "parsed-open": arm_parsed_open,
          "typed-fixed": arm_typed_fixed,
          "fixed-by-unresolved": functools.partial(arm_fixed_by, entries=["principle=principle.nowhere"],
                                                   needle="principle=principle.nowhere"),
          "fixed-by-floor": functools.partial(arm_fixed_by, entries=["floor=floor.any"], needle="floor=floor.any"),
          "fixed-by-empty": functools.partial(arm_fixed_by, entries=[], needle="the list is empty"),
          "fixed-amend": functools.partial(arm_fixed_target, kind="amends"),
          "fixed-supersede": functools.partial(arm_fixed_target, kind="supersedes"),
          "fixed-exclude": functools.partial(arm_fixed_target, kind="exclude"),
          "adopter-key": arm_adopter_key, "gov-reads-adopter": arm_gov_reads_adopter, "write-order": arm_write_order,
          "unborn-head": arm_unborn_head, "staged-not-landed": arm_staged_not_landed,
          "write-then-render": arm_write_then_render, "check-refuses-candidate": arm_check_refuses_candidate,
          "policy-at-head": arm_policy_at_head}


def run_fixture(plant=None) -> tuple[list, int]:
    """Each plant in a throwaway repository, the caller's git variables aside."""
    iu.load_memory_tree_path()
    from deviation_join import set_env_aside
    from tree_lib import GIT_ENV_LEAKS
    out, failed = [], 0
    for name in [plant] if plant else list(PLANTS):
        top = pathlib.Path(tempfile.mkdtemp(prefix="overlay-fx-"))
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
    if argv == ["check"]:
        lines, rc = run_check(iu.run_git(KIT_DIR, "rev-parse", "--show-toplevel").strip())
    elif argv[:1] == ["--fixture"] and (len(argv) == 1 or (len(argv) == 3 and argv[1] == "--plant")):
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
