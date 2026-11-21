"""presets.py - the policy kit's named presets (KICK-dKeptSession-1): the store `presets.toml` beside
this file, its completeness check, the repository side `validate` calls, and the core-only load.

    python <this kit>/presets.py check                        # the shipped store; exit 0 green, 1 red
    python <this kit>/presets.py load <name> [--repo <dir>]   # one preset's load; exit 0, 2 refused
    python <this kit>/presets.py slot [--repo <dir>]          # a scenario's slot on stdin; exit 0, 1 refused
    python <this kit>/presets.py pairs                        # `slot`'s answer on stdin; exit 0, 1 refused

THE STORE. One `[preset.<name>]` table per shipped preset, each assigning every presettable key by a
quoted dotted key, `"hooks.bypass" = "refused"`; a top-level `never` list, the keys presets never
touch; a top-level `literal` list, the derived-default rows the presets assign literal values
(KICK-dKeptSession-33); and a top-level `pairs` list of `[<higher>, <lower>]` pairs. A presettable key
is a catalogue row `never` does not name whose default `policy.check_derived` does not flag or which
`literal` names. The derived rows, `derive_derived_rows`, less `literal` are the unassigned rows: no
preset carries a key on one. The store's one writer is the preset kind's factory, `core.py new preset
<name> --from <preset>`, in the loop kit's `factories.py`; every reader takes a preset's values
through `derive_preset_assignment`.

THE CHECK, `check_presets(rows, presets)`: every presettable row matched by a key of each shipped
preset and every preset key matching a presettable row, both through `policy.read_catalogue_row`;
each value admitted by `policy.check_value`, and none equal to, or holding as a member, its row's
derived default text; the default preset, the `preset` row's default, equal to each presettable row's
default, a derived one on a set-typed row read as its text split on `, ` and compared as a set, on any
other derived row judged by `check_value` alone (§8 F3); under a presettable placeholder row such as
`review.<stage>`, each key one preset assigns held by every other; the `preset` row's `of` and the
table names one set; each `never` entry a row; `literal` an array of strings, each naming a derived
row `never` lacks; each pair held in each preset. Each finding names the preset and the key. `check`
prints it after one line per preset and one `unassigned` line naming the unassigned rows, and the
policy kit's `arm_presets` grades it.

THE REPOSITORY SIDE, `check_repo_presets(doc, text, rows)`, which `validate` imports and calls after
`budgets.check_budgets` only for a policy file holding a top-level `presets` table: each
`[presets.<name>]` table declares a repository preset whose `extends` names a shipped preset and
whose other keys are presettable, each value admitted; and the file's `preset` value names a shipped
or a declared preset. Each problem sits at the line `policy.derive_key_line` finds. It judges no pair:
the pair rules judge the store alone, and a repository file's round count above its ceiling stays the
loop kit's `review_bounds.py` refusal (§8 F10). A file declaring presets where this module does not
import is `validate`'s one problem naming it, and a store that does not read is one problem here.

THE LOAD, `load_preset(name, table)`: the named preset's assignment, every pair one `<key>=<toml
value>` line to one run of the loop kit's `guard.py --expansion`, found through the kit's inlined
`resolve_kit_dir` and no `requires` edge, so a refusal is the expansion rule's own and never a second
copy of it. `load` prints one `refused` line per refused key and exits 2; the loop kit not found, it
exits 2 naming it. `--repo <dir>` reads that repository's working-tree policy file for its declared
presets and runs the verb there; the working directory by default.

THE READER'S STEP. `policy.read_preset_value`, between the file and the default in `policy.py`'s
RESOLUTION_ORDER, answers a key the file does not set from the named preset's assignment, over
`derive_declared_presets`, the file's `[presets]` table rebuilt from the reader's flattened leaves
(KICK-dKeptSession-2).

A SCENARIO'S SLOT (KICK-dKeptSession-20), the loop kit's `scenario.py check` running both verbs as
subprocesses. `slot --repo <dir>` reads `{"scenario", "preset", "overrides"}` as JSON on stdin and
refuses a preset that is no shipped name and each override key `check_preset_key` refuses: no
catalogue row, a key presets never touch, a derived row `literal` lacks, or a value `check_value`
refuses. Otherwise it prints `{"scenario", "assignment"}`, the assignment keyed by dotted key: the
slot's preset's, else the preset `<dir>`'s working-tree policy file names, else the `preset` row's
default, with the overrides on top and the file's own keys on top of both. `pairs` reads that object
on stdin and refuses each pair `check_pairs` returns over it. Each prints one `presets: refused ·
<scenario> · <key> · <why>` line per refusal and exits 1.

WHAT THIS DOES NOT CHECK: that a preset's values are the posture its name promises, only that it is
complete, inside each key's schema and inside the pairs; a pair whose two values are not both numbers
is a finding, never a comparison; a repository file's own pair, which `validate` leaves to
`review_bounds.py`; and on a core-only install the load admits `build.closes =
"after-release-verifies"`, since the core Flow row declares its point, until the ask
TOOL-dDeclaredLoop-101 judges a point no installed expansion attaches at.

Exit 0 green or loaded, 1 red, 2 usage, a refused load or a store that does not read.
"""
import json
import os
import re
import subprocess
import sys
import tomllib
from collections import namedtuple
from pathlib import Path

sys.dont_write_bytecode = True
import policy  # noqa: E402  (the module beside this file; it imports this one inside `validate`)

KIT = policy.KIT
STORE = "presets.toml"
SAY = "presets"
PRESET_KEY = ("preset",)
REPO_TABLE = policy.PRESETS_TABLE  # the policy file's table of repository presets
#: one refusal line of the loop kit's `guard.py --expansion`, its stdin line number and why
REFUSED_LINE = re.compile(r"^loop-guard: refused · stdin:(\d+) · (.*)$")
Load = namedtuple("Load", "assignment refusals lines")   # refusals: [(dotted key, value, why)]


def load_presets(kit=KIT):
    """The parsed store beside `kit`. An absent store, or one that does not parse, is a Refusal naming
    it, at the decoder's line for the second."""
    path = Path(kit) / STORE
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise policy.Refusal(path.as_posix(), 0, f"the preset store does not read: {exc.strerror or exc}") from None
    try:
        return tomllib.loads(policy.derive_bomless_text(text))
    except tomllib.TOMLDecodeError as exc:
        at = re.search(r"at line (\d+)", str(exc))
        raise policy.Refusal(path.as_posix(), getattr(exc, "lineno", None) or (int(at[1]) if at else 0),
                             f"the preset store does not parse: {exc}") from None


def check_same_value(a, b):
    """True when two policy values are one: a set-valued pair compared as a set, else type and value."""
    if isinstance(a, list) and isinstance(b, list):
        return {policy.render_json(m) for m in a} == {policy.render_json(m) for m in b}
    return policy.check_member(a, [b])


def scan_preset_keys(table, rows, prefix=(), raw=()):
    """Yield (raw key path, key path, row or None, value) for each key of a preset table: a quoted
    dotted key such as `"leases.expiry-hours"` read into its segments by `policy.parse_key`, a nested
    table descended into unless a map-valued row names it. The raw path is the table's own keys, the
    one `policy.derive_key_line` finds a line by."""
    for k, v in table.items():
        try:
            segs = prefix + policy.parse_key(k)
        except policy.Refusal:
            segs = prefix + (k,)
        try:
            row = policy.read_catalogue_row(segs, rows)
        except policy.Refusal:
            row = None
        is_map = row is not None and isinstance(row.get("allowed"), dict) and row["allowed"].get("type") == "map"
        if isinstance(v, dict) and not is_map:
            yield from scan_preset_keys(v, rows, segs, raw + (k,))
        else:
            yield raw + (k,), segs, row, v


def derive_never(presets):
    never = presets.get("never")
    return [n for n in never if isinstance(n, str)] if isinstance(never, list) else []


def derive_pairs(presets):
    pairs = presets.get("pairs")
    ok = isinstance(pairs, list)
    return [tuple(p) for p in pairs if ok and isinstance(p, list) and len(p) == 2 and all(isinstance(k, str) for k in p)] if ok else []


def derive_literal(presets):
    """The store's `literal` list: the derived-default rows the presets assign literal values."""
    literal = presets.get("literal")
    return [n for n in literal if isinstance(n, str)] if isinstance(literal, list) else []


def derive_derived_rows(rows, never):
    """The catalogue rows, in catalogue order, whose default `policy.check_derived` flags, less those
    `never` names: the class `literal` splits into the assigned rows and the unassigned ones."""
    return [r for r in rows if r.get("name") not in never and policy.check_derived(r.get("default"))]


def derive_presettable(rows, never, literal):
    """The catalogue rows a preset assigns: each row `never` does not name whose default is literal or
    which the store's `literal` list names."""
    return [r for r in rows if r.get("name") not in never
            and (not policy.check_derived(r.get("default")) or r.get("name") in literal)]


def derive_default_preset(rows):
    """The `preset` row's default, the preset a file naming none reads, and that row's `of`."""
    row = policy.read_catalogue_row(PRESET_KEY, rows)
    allowed = row.get("allowed") if isinstance(row.get("allowed"), dict) else {}
    return row.get("default"), list(allowed.get("of") or [])


def derive_preset_assignment(name, presets, table, rows=None):
    """{key path: value} for the preset `name`: a shipped one's table, or for a name the repository's
    `table` declares, its shipped `extends` assignment with the table's own keys on top. A repository
    preset extends a shipped one only, so the walk is one level. The one assignment every reader
    takes. A name neither holds, or an `extends` naming no shipped preset, is a Refusal."""
    rows = policy.load_catalogue(KIT) if rows is None else rows
    shipped = presets.get("preset") if isinstance(presets.get("preset"), dict) else {}
    own = (table or {}).get(name) if isinstance(table, dict) else None
    if name in shipped and own is None:
        return {segs: v for _raw, segs, _row, v in scan_preset_keys(shipped[name], rows)}
    if not isinstance(own, dict):
        raise policy.Refusal((Path(KIT) / STORE).as_posix(), 0, f"{policy.render_json(name)} names no shipped "
                             "preset and no [presets.<name>] table the policy file declares")
    base = own.get("extends")
    if not isinstance(base, str) or base not in shipped:
        raise policy.Refusal(policy.POLICY_REL, 0, f"presets.{name}.extends {policy.render_json(base)} names "
                             "no shipped preset")
    out = derive_preset_assignment(base, presets, None, rows)
    out.update({segs: v for _raw, segs, _row, v in scan_preset_keys(
        {k: v for k, v in own.items() if k != "extends"}, rows)})
    return out


def check_number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def check_pairs(pairs, assignment, name):
    """[(higher, lower, why)] for each pair `assignment` breaks: `higher` below `lower`, or two values
    that are not both numbers. A pair whose two keys are both unset binds nothing."""
    out = []
    for hi, lo in pairs:
        a, b = assignment.get(policy.parse_key(hi)), assignment.get(policy.parse_key(lo))
        if a is None and b is None:
            continue
        if not (check_number(a) and check_number(b)):
            out.append((hi, lo, f"{hi} {policy.render_json(a)} and {lo} {policy.render_json(b)} under preset "
                                f"{name} are not two numbers, so the pair rule cannot hold {hi} at or above {lo}"))
        elif a < b:
            out.append((hi, lo, f"{lo} {policy.render_json(b)} is above {hi} {policy.render_json(a)} under preset "
                                f"{name}: the pair rule holds {hi} at or above {lo}"))
    return out


def check_preset_key(row, value, never, presettable):
    """Why a preset may not assign `value` to the key `row` names, or None."""
    if row is None:
        return "no catalogue row matches this key"
    if row.get("name") in never:
        return "a key presets never touch"
    if row.get("name") not in presettable:
        return "not a presettable key: its row's default is derived"
    default = row.get("default")
    if policy.check_derived(default):
        text = default["derived"]
        if value == text or (isinstance(value, list) and text in value):
            return f"{policy.render_json(text)} is the row's derived default text, not a value"
    return policy.check_value(row, value)


def check_presets(rows, presets):
    """[(where, why)] for the shipped store `presets` against the catalogue `rows`, `where` naming the
    preset and the key: `preset.<name> · <key>`, or `never · <key>` and `pairs · <key>` for the two lists."""
    out = []
    names = {r.get("name") for r in rows}
    if not (isinstance(presets.get("never"), list) and len(derive_never(presets)) == len(presets["never"])):
        out.append(("never", "is not an array of catalogue key names"))
    never = derive_never(presets)
    for n in never:
        if n not in names:
            out.append((f"never · {n}", "names no catalogue row"))
    pairs = derive_pairs(presets)
    if not isinstance(presets.get("pairs"), list) or len(pairs) != len(presets["pairs"]):
        out.append(("pairs", "is not an array of [<higher>, <lower>] key pairs"))
    literal = derive_literal(presets)
    if not (isinstance(presets.get("literal"), list) and len(literal) == len(presets["literal"])):
        out.append(("literal", "is not an array of strings"))
    derived = {r.get("name") for r in derive_derived_rows(rows, never)}
    for n in literal:
        if n not in derived:
            out.append((f"literal · {n}", "names no catalogue row whose default is derived and `never` lacks"))
    presettable = {r["name"]: r for r in derive_presettable(rows, never, literal)}
    for pair in pairs:
        for k in pair:
            if k not in presettable:
                out.append((f"pairs · {k}", "names no presettable catalogue row"))
    shipped = presets.get("preset")
    if not isinstance(shipped, dict) or not shipped:
        return out + [("preset", "the store holds no [preset.<name>] table")]
    try:
        default, of = derive_default_preset(rows)
    except policy.Refusal as exc:
        return out + [("preset", exc.why)]
    for name in of:
        if name not in shipped:
            out.append((f"preset.{name} · preset", "a name the preset row's `of` holds and no table of the store"))
    placed = {}   # {preset: the keys it assigns under a presettable placeholder row}
    for name, table in shipped.items():
        if name not in of:
            out.append((f"preset.{name} · preset", "a table the preset row's `of` lacks"))
        if not isinstance(table, dict):
            out.append((f"preset.{name}", "is not a table"))
            continue
        seen, assignment, placed[name] = set(), {}, []
        for _raw, segs, row, value in scan_preset_keys(table, rows):
            at = f"preset.{name} · {policy.render_dotted(segs)}"
            why = check_preset_key(row, value, never, presettable)
            if why is None and name == default:
                # A derived default is judged on a set-typed row by its text split on `, `, as a set,
                # and on any other row by `check_value` alone (§8 F3).
                want = row.get("default")
                if policy.check_derived(want):
                    allowed = row.get("allowed") if isinstance(row.get("allowed"), dict) else {}
                    want = str(want["derived"]).split(", ") if allowed.get("type") == "set" else None
                if want is not None and not check_same_value(value, want):
                    why = f"{policy.render_json(value)} is not the row's default {policy.render_json(want)}"
            if why:
                out.append((at, why))
            if row is not None:
                seen.add(row.get("name"))
                if row.get("name") in presettable and policy.check_pattern_name(row.get("name")):
                    placed[name].append(policy.render_dotted(segs))
            assignment[segs] = value
        out += [(f"preset.{name} · {key}", "lacks this presettable key") for key in presettable if key not in seen]
        out += [(f"preset.{name} · {lo}", why) for _hi, lo, why in check_pairs(pairs, assignment, name)]
    for other, keys in placed.items():
        named = set(keys)   # each key another preset assigns is named once, by the first that does
        for name, theirs in placed.items():
            for key in theirs:
                if key not in named:
                    named.add(key)
                    out.append((f"preset.{other} · {key}", f"lacks this key, which preset {name} assigns"))
    return out


def check_repo_presets(doc, text, rows):
    """[policy.Problem] for the preset half of a parsed policy file `doc`, each at the line of `text`
    that `policy.derive_key_line` finds: a `[presets.<name>]` table whose `extends` names no shipped
    preset or that sets a key no preset may, and a `preset` value naming neither a shipped nor a
    declared preset. `validate` calls it only for a file holding the `presets` table, and it judges no
    pair (§8 F10). A store that does not read is one problem."""
    try:
        store = load_presets()
    except policy.Refusal as exc:
        return [policy.Problem(0, REPO_TABLE, f"{exc.path}:{exc.line} · {exc.why}")]
    out, line = [], (lambda path: policy.derive_key_line(text, path))
    never = derive_never(store)
    presettable = {r["name"] for r in derive_presettable(rows, never, derive_literal(store))}
    shipped = store.get("preset") if isinstance(store.get("preset"), dict) else {}
    declared = doc.get(REPO_TABLE)
    if not isinstance(declared, dict):
        out.append(policy.Problem(line((REPO_TABLE,)), REPO_TABLE, "is not a table of [presets.<name>] tables"))
        declared = {}
    for name, t in declared.items():
        base = (REPO_TABLE, name)
        if not isinstance(t, dict):
            out.append(policy.Problem(line(base), policy.render_dotted(base), "is not a table"))
            continue
        if not (isinstance(t.get("extends"), str) and t["extends"] in shipped):
            out.append(policy.Problem(line(base + ("extends",)), policy.render_dotted(base + ("extends",)),
                                      f"{policy.render_json(t.get('extends'))} names no shipped preset: a repository "
                                      f"preset extends one of {policy.render_json(sorted(shipped))}"))
        for raw, _segs, row, value in scan_preset_keys({k: v for k, v in t.items() if k != "extends"}, rows):
            why = check_preset_key(row, value, never, presettable)
            if why:
                out.append(policy.Problem(line(base + raw), policy.render_dotted(base + raw), why))
    if PRESET_KEY[0] in doc:
        name = doc[PRESET_KEY[0]]
        if not (isinstance(name, str) and (name in shipped or name in declared)):
            out.append(policy.Problem(line(PRESET_KEY), PRESET_KEY[0], f"{policy.render_json(name)} names no shipped "
                                      f"preset, one of {policy.render_json(sorted(shipped))}, and no [presets.<name>] "
                                      "table the file declares"))
    return out


def read_repo_policy(repo):
    """`repo`'s working-tree policy file parsed, {} where it has none; a Refusal where it does not parse."""
    path = Path(repo, policy.POLICY_REL)
    if not path.is_file():
        return {}
    try:
        return tomllib.loads(policy.derive_bomless_text(path.read_text(encoding="utf-8")))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as exc:
        raise policy.Refusal(policy.POLICY_REL, 0, f"does not parse: {exc}") from None


def read_repo_table(repo):
    """The `[presets]` table of `repo`'s working-tree policy file, None where it has none."""
    doc = read_repo_policy(repo)
    return doc.get(REPO_TABLE) if isinstance(doc.get(REPO_TABLE), dict) else None


def check_slot(slot, store, rows):
    """[(key, why)] for a scenario's `slot`, `{"preset", "overrides"}`, against the store and the catalogue
    `rows`: a preset that is no shipped name, overrides that are no table, and each override key
    `check_preset_key` refuses, a key presets never touch among them (KICK-dKeptSession-20)."""
    out = []
    shipped = store.get("preset") if isinstance(store.get("preset"), dict) else {}
    name = slot.get("preset")
    if name is not None and not (isinstance(name, str) and name in shipped):
        out.append((PRESET_KEY[0], f"{policy.render_json(name)} names no shipped preset, one of "
                                   f"{policy.render_json(sorted(shipped))}: a scenario names a shipped preset only"))
    overrides = {} if slot.get("overrides") is None else slot["overrides"]
    if not isinstance(overrides, dict):
        return out + [("overrides", "is not a table from a dotted policy key to its value")]
    never = derive_never(store)
    presettable = {r["name"] for r in derive_presettable(rows, never, derive_literal(store))}
    for key, value in overrides.items():
        try:
            row = policy.read_catalogue_row(policy.parse_key(key), rows)
        except policy.Refusal:
            row = None
        why = check_preset_key(row, value, never, presettable)
        if why:
            out.append((key, why))
    return out


def derive_slot_assignment(slot, store, doc, rows):
    """{key path: value} a build placed under `slot` reads, `doc` the repository's parsed policy file: the
    slot's preset's assignment, else the preset the file names, else the `preset` row's default, with the
    slot's overrides on top and the file's own keys on top of both. A Refusal for a name no preset holds."""
    declared = doc.get(REPO_TABLE) if isinstance(doc.get(REPO_TABLE), dict) else None
    name = slot.get("preset")
    if name is None:
        name = doc.get(PRESET_KEY[0]) if PRESET_KEY[0] in doc else derive_default_preset(rows)[0]
    else:
        declared = None   # a scenario names a shipped preset only (KICK-dKeptSession-20 §8 F2)
    out = dict(derive_preset_assignment(name, store, declared, rows))
    out.update({policy.parse_key(k): v for k, v in (slot.get("overrides") or {}).items()})
    own = {k: v for k, v in doc.items() if k not in (REPO_TABLE, PRESET_KEY[0])}
    out.update({segs: v for _raw, segs, _row, v in scan_preset_keys(own, rows)})
    return out


def derive_declared_presets(table):
    """The policy file's `[presets]` table, nested as `derive_preset_assignment` reads it, rebuilt from
    `table`, the {key path: value} leaves `policy.parse_policy` flattened: each path under
    `("presets",)` re-nested below its name (KICK-dKeptSession-2 S5). {} where the file declares none."""
    out = {}
    for path, value in (table or {}).items():
        if len(path) < 2 or path[0] != REPO_TABLE:
            continue
        node = out
        for seg in path[1:-1]:
            node = node.setdefault(seg, {})
        node[path[-1]] = value
    return out


def run_expansion_verb(guard, pairs, top="."):
    """-> ([(index into `pairs`, why)], output lines) of one run of `guard`, the loop kit's guard.py,
    under `--expansion` in `top`, each of `pairs` ((dotted key, value)) one `<key>=<toml value>` line
    on its stdin. An exit other than 0 with no refusal, or 2 with one, is a Refusal naming the verb."""
    feed = "".join(f"{k}={policy.render_toml_value(v)}\n" for k, v in pairs)
    env = {k: v for k, v in os.environ.items() if k not in policy.GIT_ENV_LEAKS}
    try:
        p = subprocess.run([sys.executable, str(guard), "--expansion"], input=feed, cwd=str(top), env=env,
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
    except OSError as exc:
        raise policy.Refusal(Path(guard).as_posix(), 0, f"--expansion did not run: {exc}") from None
    lines = (p.stdout + p.stderr).replace("\r", "").splitlines()
    refused = [(int(m[1]) - 1, m[2]) for m in map(REFUSED_LINE.match, lines) if m]
    if (p.returncode, bool(refused)) not in ((0, False), (2, True)) or any(not 0 <= i < len(pairs) for i, _w in refused):
        said = next((ln for ln in reversed(lines) if ln.strip()), "(no output)")
        raise policy.Refusal(Path(guard).as_posix(), 0, f"--expansion exited {p.returncode}: {said}")
    return refused, lines


def load_preset(name, table, presets=None, here=KIT, top="."):
    """-> Load(the assignment, [(dotted key, value, why)] for each pair the expansion rule refuses, the
    verb's lines) for the preset `name`, `table` the repository's declared presets or None: every pair
    to one run of the loop kit's `guard.py --expansion` in `top`, the kit found from `here` through the
    inlined `resolve_kit_dir`. LookupError where the loop kit does not resolve; a Refusal for a name no
    preset holds or a verb that does not answer."""
    presets = load_presets(here) if presets is None else presets
    assignment = derive_preset_assignment(name, presets, table)
    guard = policy.resolve_kit_dir("loop", "guard.py", here) / "guard.py"
    pairs = [(policy.render_dotted(k), v) for k, v in assignment.items()]
    refused, lines = run_expansion_verb(guard, pairs, top)
    return Load(assignment, [(pairs[i][0], pairs[i][1], why) for i, why in refused], lines)


USAGE = "usage: python presets.py check | load <name> [--repo <dir>] | slot [--repo <dir>] | pairs"


def run_check():
    rows = policy.load_catalogue(KIT)
    try:
        store = load_presets()
    except policy.Refusal as exc:
        print(f"{SAY}: refused · {exc.path}:{exc.line} · {exc.why}")
        return 2
    findings = check_presets(rows, store)
    never, literal = derive_never(store), derive_literal(store)
    presettable = derive_presettable(rows, never, literal)
    for name, table in (store.get("preset") or {}).items():
        have = {row.get("name") for _r, _s, row, _v in scan_preset_keys(table, rows) if row is not None} if isinstance(table, dict) else set()
        print(f"{SAY}: check · {name} · {sum(r['name'] in have for r in presettable)} of {len(presettable)} "
              "presettable key(s)")
    unassigned = [r["name"] for r in derive_derived_rows(rows, never) if r["name"] not in literal]
    print(f"{SAY}: check · unassigned · {len(unassigned)} derived row(s) · {', '.join(unassigned)}")
    for where, why in findings:
        print(f"{SAY}: refused · {where} · {why}")
    print(f"{SAY}: check · {'red' if findings else 'green'} · {len(findings)} finding(s)")
    return 1 if findings else 0


def run_load(name, repo):
    try:
        load = load_preset(name, read_repo_table(repo), top=repo)
    except LookupError as exc:
        print(f"{SAY}: load {name} · refused · the loop kit does not resolve: {exc}")
        return 2
    except policy.Refusal as exc:
        print(f"{SAY}: load {name} · refused · {exc.path}:{exc.line} · {exc.why}")
        return 2
    for ln in load.lines:
        if not REFUSED_LINE.match(ln):
            print(ln)
    for key, value, why in load.refusals:
        print(f"{SAY}: load {name} · refused · {key} = {policy.render_toml_value(value)} · {why}")
    if load.refusals:
        return 2
    print(f"{SAY}: load {name} · loaded · {len(load.assignment)} key(s)")
    return 0


def read_stdin_object(*keys):
    """The JSON object on stdin when it holds a string `scenario` and each of `keys`, else None."""
    try:
        got = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return None
    ok = isinstance(got, dict) and isinstance(got.get("scenario"), str) and all(k in got for k in keys)
    return got if ok else None


def run_slot(repo):
    """`slot --repo <repo>`: a scenario's slot on stdin checked by `check_slot`, then the assignment a
    build under it reads printed as JSON keyed by dotted key: -> 0, 1 refused, 2 usage or a store or
    file that does not read."""
    slot = read_stdin_object()
    if slot is None:
        print(f'{USAGE} · slot reads {{"scenario", "preset", "overrides"}} as JSON on stdin', file=sys.stderr)
        return 2
    rows = policy.load_catalogue(KIT)
    try:
        store = load_presets()
        doc = read_repo_policy(repo)
    except policy.Refusal as exc:
        print(f"{SAY}: refused · {exc.path}:{exc.line} · {exc.why}")
        return 2
    refusals = check_slot(slot, store, rows)
    for key, why in refusals:
        print(f"{SAY}: refused · {slot['scenario']} · {key} · {why}")
    if refusals:
        return 1
    try:
        assignment = derive_slot_assignment(slot, store, doc, rows)
    except policy.Refusal as exc:
        print(f"{SAY}: refused · {exc.path}:{exc.line} · {exc.why}")
        return 2
    print(json.dumps({"scenario": slot["scenario"], "assignment": {policy.render_dotted(k): v for k, v in
                                                                  assignment.items()}}, sort_keys=True, default=str))
    return 0


def run_pairs():
    """`pairs`: `slot`'s `{"scenario", "assignment"}` on stdin, each pair `check_pairs` breaks in it one
    refusal: -> 0, 1 refused, 2 usage or a store that does not read."""
    got = read_stdin_object("assignment")
    if got is None or not isinstance(got["assignment"], dict):
        print(f'{USAGE} · pairs reads {{"scenario", "assignment"}} as JSON on stdin', file=sys.stderr)
        return 2
    try:
        store = load_presets()
        assignment = {policy.parse_key(k): v for k, v in got["assignment"].items()}
    except policy.Refusal as exc:
        print(f"{SAY}: refused · {exc.path}:{exc.line} · {exc.why}")
        return 2
    pairs = derive_pairs(store)
    found = check_pairs(pairs, assignment, got["scenario"])
    for _hi, lo, why in found:
        print(f"{SAY}: refused · {got['scenario']} · {lo} · {why}")
    if found:
        return 1
    print(f"{SAY}: pairs · {got['scenario']} · {len(pairs)} pair(s) held")
    return 0


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    if argv == ["check"]:
        return run_check()
    if argv[:1] == ["slot"] and (len(argv) == 1 or (len(argv) == 3 and argv[1] == "--repo")):
        return run_slot(argv[2] if len(argv) == 3 else ".")
    if argv == ["pairs"]:
        return run_pairs()
    if len(argv) in (2, 4) and argv[0] == "load" and (len(argv) == 2 or argv[2] == "--repo"):
        return run_load(argv[1], argv[3] if len(argv) == 4 else ".")
    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
