#!/usr/bin/env python3
"""loop_lib — the one reader of the loop's definition, `loop.toml` beside this file (TOOL-dDeclaredLoop-1).

    python loop_lib.py --check                    # read the definition, print what was read
    python loop_lib.py --fixture --plant <case>   # read it with one break planted in memory
    python loop_lib.py --grade-site <site> <entry>...   # grade one declaration site's witness entries

The definition holds the gov steps as `[[step]]` rows and one `[[workflow]]` row per workflow of the roles
kit: its build order, the step its work sits in and, where it differs from that step's own word, the reach
word its work orders load practices under. Every other kit reads those facts through this module:
`load_loop` returns the definition whole, `read_steps` its step rows, `read_workflow_order` each workflow's
order and `read_workflow_reach` each workflow's reach word.

The definition also holds the one closed disposition set (TOOL-dDeclaredLoop-16): `[dispositions]` with its
`set`, the words a placing item returns, and `[[disposition-alias]]` rows mapping a legacy `word` to the
member it `means`. `read_dispositions` returns the members, `resolve_disposition` a member for a member or
an alias, `read_outcome_set` the closed outcome set of one `[[item]]` row, the set above where the row
declares `outcomes = "dispositions"` and the row's own list otherwise, and `check_disposition_record`
joins an owner's disposition record to its item's set: True for a member, LoopError for any other word,
None for an item the definition does not declare, which a caller prints as `unarmed` and never as green.
The join compares the word as written, never through an alias.

The definition also classes every witness (TOOL-dDeclaredLoop-5): `[witnesses]` with its `classes`, the
facts the acting agent cannot type, and its `refused` class `actor`, a fact it typed; `[[witness-alias]]`
rows mapping the unattended driver's checker words onto a class, `machine` to `history` and `agent` to
`actor`; and a `witness = { class, by }` on every `[[step]]` row. `read_witness_classes` returns the two
lists and `check_witness_classes` grades the three. Neither runs inside `load_loop`, so a reader that
copies this module and a definition with no witness keeps reading. `actor-witnesses.txt` beside this
file is the shrink-only list of actor witnesses, `<site>\\t<witness>\\t<build>` per row, the build being
the one whose computed witness takes its place: `check_actor_list` grades it both ways against the
definition, against itself at the compare base `read_actor_base` reads, and against each build's
folder. `--grade-site` joins a declaration site outside the definition, `DOD_CORE` or `DOD_EXTRA` of
the unattended driver, to the aliases and the list, both ways.

A definition that does not hold is refused with `LoopError`, a `ValueError` naming the file and the row: a
file that does not read or is no TOML; a `step` or `workflow` table that is no array of tables; the gov
steps missing, repeated or out of order, a tag that is no gov step, or an `order` that is not the step's
place; a step row without a `state` or an `exit`; a workflow row with no name or named twice, an `order`
that is not an integer at or above 0, a `step` that is absent or is neither a step tag nor `none`, or a
`reach` outside `REACH_WORDS`; a `[dispositions]` table whose `set` is not a non-empty array of words
of the `SEG` shape, or holds a word twice; a `[[disposition-alias]]` row whose `word` is a member or
repeats an earlier row's, or whose `means` is no member. The table is graded where the definition holds
it; `read_dispositions` and `--check` refuse a definition that declares no set.

`--check` prints one line per step and per workflow, the set and one line per alias, then a count, and exits 0; a refused definition is one
line and exit 1. It then prints the witness classes, one line per witness alias and per witness, one
line per list row with its build and the list's base line, the base or `no comparison` and why, and
each refusal of the list as `loop: refused · ...`, exit 1. `--fixture --plant <case>` reads the shipped
definition and list with the named break made in memory, never on disk, the list's base being the
shipped list as read, and exits 1 on the refusal the break must draw, 0 if the reader accepted it. The
plants are `PLANTS`. `--grade-site <site> <entry>...` prints `loop: site <site> · <item> · <word> ·
<class>` per entry, `· until <build>` on an actor entry, then each refusal, and exits 0, or 1 on a
refusal. Exit 2 is a usage error, a site outside `DECLARATION_SITES` included.

WHAT THIS DOES NOT CHECK: that a workflow row names a workflow the roles kit holds, which is that kit's
catalogue check, both ways; that a step tag or an exit item is registered in its namespace, which is the
tag index's; that the item an `exit` names exists, since the item rows are not in this file yet; what a
`state` word means; an `[[item]]` row beyond the `tag` and `outcomes` the outcome read asks of it, since
the item schema is its own unit's; that a disposition record's `Item` names a declared item, which reads
None; or that a writer resolved an alias before it wrote. An unknown key on a row is not read and not
refused. That a witness's `by` is true. Stdlib only, but for `read_actor_base`, which imports the
memory-tree kit's compare base inside the function, so a reader calling `load_loop` never reaches it.
"""
import pathlib
import re
import sys
import tomllib

KIT_LOOP_VERSION = "1.0"

DEFINITION = "loop.toml"
#: The shrink-only list of actor witnesses beside the definition, `<site>\t<witness>\t<build>` per row.
ACTOR_LIST = "actor-witnesses.txt"
#: The gov steps, in the loop's order. A definition holds exactly these `[[step]]` rows, in this order.
STEP_TAGS = ("step.plan", "step.design", "step.build", "step.test", "step.deploy")
#: A workflow's `step` when its work sits in no gov step.
NO_STEP = "none"
#: The reach words that are no gov step: the entry step and the review breakpoint.
REACH_WORDS = ("entry", "review")
#: One word of a disposition set or an outcome set: the segment a tag is composed of.
SEG = re.compile(r"[a-z0-9][a-z0-9-]*")
#: An `[[item]]` row's `outcomes` when its closed outcome set is the `[dispositions]` set.
OUTCOMES_REF = "dispositions"
#: `--plant`'s cases, each a break made in the definition as read, and what it does.
PLANTS = {"missing-step": "the step.deploy row taken out",
          "reordered": "the step.test row moved before step.build",
          "bad-step": "the build workflow's step set to step.ship",
          "bad-reach": "the spec-review workflow's reach set to revew",
          "disposition-unknown": "the disposition ask given twice in the set",
          "disposition-alias": "the defer alias's means set to postpone",
          "witness-no-class": "step.plan's witness given no class",
          "witness-bad-class": "step.plan's witness class set to agent-said",
          "witness-actor-unlisted": "step.plan's witness class set to actor",
          "witness-actor-listed": "step.plan's witness class set to actor, and listed in the list and its base",
          "actor-list-grown": "a list row the base lacks",
          "actor-list-stale": "a row for step.design, whose witness is history, in the list and its base",
          "actor-list-no-build": "a row naming dNoSuchBuild in the list and its base"}
#: The declaration sites outside the definition whose entries `--grade-site` grades: the unattended
#: driver's core Definition of Done and the conf's extra one, each a set of `<item>:<word>` entries.
DECLARATION_SITES = ("DOD_CORE", "DOD_EXTRA")


class LoopError(ValueError):
    """The definition does not hold; the message is `<where>: <what>`, the file and the row."""

    def __init__(self, where, what):
        super().__init__("%s: %s" % (where, what))


def check_loop(data, where):
    """`data`, a parsed definition, returned as `{"step": [...], "workflow": [...], "dispositions": [...]}`
    once every row holds, `dispositions` the members of the set and empty where the definition holds no
    `[dispositions]` table; LoopError naming `where` and the first row that does not."""
    tables = {}
    for table in ("step", "workflow", "disposition-alias"):
        rows = data.get(table, [])
        if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
            raise LoopError(where, "'%s' is not an array of tables" % table)
        tables[table] = rows
    tags = [r.get("tag") for r in tables["step"]]
    for tag in tags:
        if tag not in STEP_TAGS:
            raise LoopError(where, "step row %r names no gov step; the gov steps are %s" % (tag, " ".join(STEP_TAGS)))
        if tags.count(tag) > 1:
            raise LoopError(where, "the step %s is repeated" % tag)
    for tag in STEP_TAGS:
        if tag not in tags:
            raise LoopError(where, "the step %s is missing" % tag)
    for n, (row, want) in enumerate(zip(tables["step"], STEP_TAGS), 1):
        if row["tag"] != want:
            raise LoopError(where, "the step %s is out of order: row %d is %s's place" % (row["tag"], n, want))
        if row.get("order") != n or isinstance(row.get("order"), bool):
            raise LoopError(where, "the step %s carries order %r, and its place is %d" % (want, row.get("order"), n))
        for key in ("state", "exit"):
            if not isinstance(row.get(key), str) or not row[key]:
                raise LoopError(where, "the step %s carries no %s" % (want, key))
    seen = set()
    for n, row in enumerate(tables["workflow"], 1):
        name = row.get("name")
        at = "workflow row %d (%s)" % (n, name if isinstance(name, str) and name else "unnamed")
        if not isinstance(name, str) or not name:
            raise LoopError(where, "%s carries no name" % at)
        if name in seen:
            raise LoopError(where, "%s repeats the name of an earlier row" % at)
        seen.add(name)
        order = row.get("order")
        if not isinstance(order, int) or isinstance(order, bool) or order < 0:
            raise LoopError(where, "%s order %r is not an integer at or above 0" % (at, order))
        if "step" not in row:
            raise LoopError(where, "%s carries no step" % at)
        if row["step"] != NO_STEP and row["step"] not in STEP_TAGS:
            raise LoopError(where, "%s step %r is neither a declared step tag nor %s" % (at, row["step"], NO_STEP))
        if "reach" in row and row["reach"] not in REACH_WORDS:
            raise LoopError(where, "%s reach %r is not one of %s" % (at, row["reach"], " ".join(REACH_WORDS)))
    members = []
    if "dispositions" in data:
        members = data["dispositions"].get("set") if isinstance(data["dispositions"], dict) else None
        if not isinstance(members, list) or not members:
            raise LoopError(where, "'dispositions' carries no non-empty set")
        for word in members:
            if not isinstance(word, str) or not SEG.fullmatch(word):
                raise LoopError(where, "the disposition %r is not one word of the shape %s" % (word, SEG.pattern))
            if members.count(word) > 1:
                raise LoopError(where, "the disposition %s is given twice" % word)
    check_alias_rows(tables.pop("disposition-alias"), members, "disposition-alias", where)
    tables["dispositions"] = list(members)
    return tables


def check_alias_rows(rows, members, table, where):
    """Each row of the alias table `table`: its `word` is no member and no earlier row's, and its
    `means` is a member; LoopError naming `where` and the first row that does not."""
    words = set()
    for n, row in enumerate(rows, 1):
        word, means = row.get("word"), row.get("means")
        at = "%s row %d (%s)" % (table, n, word if isinstance(word, str) and word else "unnamed")
        if not isinstance(word, str) or not word:
            raise LoopError(where, "%s carries no word" % at)
        if word in members:
            raise LoopError(where, "%s names a member of the set, which needs no alias" % at)
        if word in words:
            raise LoopError(where, "%s repeats the word of an earlier row" % at)
        words.add(word)
        if means not in members:
            raise LoopError(where, "%s means %r, which is no member of the set: %s" % (at, means, " ".join(members)))


def resolve_alias(rows, word):
    """The `means` of the alias row whose `word` is `word`, None where no row holds it."""
    return next((row["means"] for row in rows if row.get("word") == word), None)


def check_witness_classes(data, where):
    """`data`'s witnesses graded: `[witnesses]`, then every `[[witness-alias]]` row, then every `[[step]]`
    row's `witness`; `[(site, class, by)]` per witness, a step's site its tag. LoopError naming `where`
    and the table and row that does not hold, a definition declaring no `[witnesses]` included."""
    table = data.get("witnesses")
    if not isinstance(table, dict):
        raise LoopError(where, "declares no witness classes, a [witnesses] table with classes and refused")
    for key in ("classes", "refused"):
        words = table.get(key)
        if not isinstance(words, list) or not words:
            raise LoopError(where, "'witnesses' carries no non-empty %s" % key)
        for word in words:
            if not isinstance(word, str) or not SEG.fullmatch(word):
                raise LoopError(where, "the witness class %r is not one word of the shape %s" % (word, SEG.pattern))
            if words.count(word) > 1:
                raise LoopError(where, "the witness class %s is given twice" % word)
    both = sorted(set(table["classes"]) & set(table["refused"]))
    if both:
        raise LoopError(where, "the witness class %s is both a class and refused" % " ".join(both))
    members = table["classes"] + table["refused"]
    aliases = data.get("witness-alias", [])
    if not isinstance(aliases, list) or not all(isinstance(r, dict) for r in aliases):
        raise LoopError(where, "'witness-alias' is not an array of tables")
    check_alias_rows(aliases, members, "witness-alias", where)
    witnesses = []
    for row in data.get("step", []):
        tag, witness = row.get("tag"), row.get("witness")
        if witness is None:
            raise LoopError(where, "the step %s carries no witness, an inline table { class, by }" % tag)
        if not isinstance(witness, dict) or not isinstance(witness.get("class"), str):
            raise LoopError(where, "the step %s carries a witness with no class" % tag)
        if not isinstance(witness.get("by"), str) or not witness["by"].strip():
            raise LoopError(where, "the step %s carries a witness with no by, what witnesses it" % tag)
        if witness["class"] not in members:
            raise LoopError(where, "the step %s witness class %r is no class and not refused: %s" % (
                tag, witness["class"], " ".join(members)))
        witnesses.append((tag, witness["class"], witness["by"]))
    return witnesses


def read_witness_classes(kit_dir):
    """`{"classes": [...], "refused": [...]}` of the definition in `kit_dir`, its witnesses graded;
    LoopError for a definition that declares no `[witnesses]` table or whose witnesses do not hold."""
    data, where = read_definition(kit_dir)
    check_witness_classes(data, where)
    return {"classes": list(data["witnesses"]["classes"]), "refused": list(data["witnesses"]["refused"])}


def check_actor_list(rows, base_rows, sites, root):
    """One refusal per row of the actor-witness list `rows`, its lines as read, that is not three
    tab-separated fields; that `base_rows`, the list at the compare base, lacks (None is no comparison);
    whose site is a definition site holding no actor witness of that name, or neither such a site nor
    one of `DECLARATION_SITES`; or whose build has no `memory/builds/<build>/README.md` under `root`.
    And one per actor witness of a definition site no row lists. `sites` maps each definition site to
    `{witness: class}`."""
    refusals, listed = [], set()
    for line in rows:
        fields = line.split("\t")
        if len(fields) != 3 or not all(f.strip() for f in fields):
            refusals.append("the list row %r is not three tab-separated fields, <site> <witness> <build>" % line)
            continue
        site, witness, build = fields
        listed.add((site, witness))
        if base_rows is not None and line not in base_rows:
            refusals.append("the list row %s %s %s is absent from the list at its compare base, and the list "
                            "only shrinks" % (site, witness, build))
        if site in sites:
            if sites[site].get(witness) != "actor":
                refusals.append("the list row %s %s names no actor witness: %s's witness %s is %s" % (
                    site, witness, site, witness, sites[site].get(witness, "absent")))
        elif site not in DECLARATION_SITES:
            refusals.append("the list row %s %s names a site that is neither a definition site nor one of %s" % (
                site, witness, " ".join(DECLARATION_SITES)))
        if not (pathlib.Path(root) / "memory" / "builds" / build / "README.md").is_file():
            refusals.append("the list row %s %s names the build %s, which has no memory/builds/%s/README.md" % (
                site, witness, build, build))
    for site, named in sites.items():
        for witness, cls in named.items():
            if cls == "actor" and (site, witness) not in listed:
                refusals.append("the actor witness %s %s has no list row naming the build that computes it" % (
                    site, witness))
    return refusals


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


def read_actor_base(kit_dir):
    """`(rows or None, why)`: the actor-witness list's lines at the compare base and the base, or None
    and why there is no comparison: no work tree, no memory-tree kit, no base, or no list at the base."""
    import subprocess

    def read(*args):
        try:
            p = subprocess.run(["git", "-C", str(kit_dir), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
        except OSError:
            return None
        return p.stdout if p.returncode == 0 else None

    top, prefix = read("rev-parse", "--show-toplevel"), read("rev-parse", "--show-prefix")
    if top is None or prefix is None:
        return None, "the loop kit sits in no git work tree"
    try:
        mt_dir = resolve_kit_dir("memory-tree", "coverage_join.py", kit_dir)
    except LookupError as e:
        return None, str(e)
    if str(mt_dir) not in sys.path:
        sys.path.insert(0, str(mt_dir))
    from coverage_join import resolve_compare_base
    base, why = resolve_compare_base(top.strip())
    if not base:
        return None, why
    text = read("show", "%s:%s%s" % (base, prefix.strip(), ACTOR_LIST))
    if text is None:
        return None, "the list is absent at the base %s" % base
    return [ln for ln in text.splitlines() if ln.strip()], base


def read_actor_rows(kit_dir):
    """The actor-witness list's lines in `kit_dir`, blank lines dropped; LoopError where it does not read."""
    path = pathlib.Path(kit_dir) / ACTOR_LIST
    try:
        return [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    except (OSError, UnicodeDecodeError) as e:
        raise LoopError(path.as_posix(), "cannot be read: %s" % e)


def check_site_witnesses(kit_dir, site, entries):
    """`(lines, refusals)` of the declaration site `site`'s `entries`, each `<item>` or `<item>:<word>`:
    a line per entry whose word resolves through `[[witness-alias]]`; a refusal per entry with no word,
    a word no alias row holds, or an actor word with no `<site> <item>` list row, and per list row of
    `site` whose item is no actor entry. The list is the one in `kit_dir`, read without a base."""
    data, where = read_definition(kit_dir)
    check_witness_classes(data, where)
    refused, aliases = data["witnesses"]["refused"], data.get("witness-alias", [])
    words = " or ".join(":" + r["word"] for r in aliases)
    listed = {}
    for line in read_actor_rows(kit_dir):
        fields = line.split("\t")
        if len(fields) == 3 and fields[0] == site:
            listed[fields[1]] = fields[2]
    lines, refusals, actors = [], [], set()
    for entry in entries:
        item, _sep, word = entry.partition(":")
        if not word:
            refusals.append("%s %s declares no witness class; append %s" % (site, entry, words))
            continue
        cls = resolve_alias(aliases, word)
        if cls is None:
            refusals.append("%s %s: %r is no witness word; the words are %s" % (site, entry, word, words))
            continue
        line = "loop: site %s · %s · %s · %s" % (site, item, word, cls)
        if cls in refused:
            actors.add(item)
            if item in listed:
                line += " · until %s" % listed[item]
            else:
                refusals.append("%s %s is an actor witness and the list holds no row %s %s naming the build "
                                "that computes it" % (site, entry, site, item))
        lines.append(line)
    for item in listed:
        if item not in actors:
            refusals.append("the list row %s %s names no actor entry of %s" % (site, item, site))
    return lines, refusals


def read_definition(kit_dir):
    """`(parsed TOML, the file's path as printed)` of the definition in `kit_dir`, unchecked; LoopError
    when the file does not read or is no TOML."""
    path = pathlib.Path(kit_dir) / DEFINITION
    try:
        with open(path, "rb") as fh:
            return tomllib.load(fh), path.as_posix()
    except OSError as e:
        raise LoopError(path.as_posix(), "cannot be read: %s" % e.strerror)
    except (tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
        raise LoopError(path.as_posix(), "not valid TOML: %s" % e)


def load_loop(kit_dir):
    """The definition in `kit_dir`, checked: `{"step": [rows], "workflow": [rows], "dispositions":
    [members]}`, each in file order."""
    return check_loop(*read_definition(kit_dir))


def read_steps(kit_dir):
    """The gov steps' rows, in the loop's order."""
    return load_loop(kit_dir)["step"]


def read_workflow_order(kit_dir):
    """`{workflow name: order}`, in file order: the build order, 0 for an any-time workflow."""
    return {w["name"]: w["order"] for w in load_loop(kit_dir)["workflow"]}


def derive_reach(row):
    """A checked workflow row's reach word: its `reach`, else its step's last segment, else `none`."""
    return row.get("reach") or row["step"].rsplit(".", 1)[-1]


def read_workflow_reach(kit_dir):
    """`{workflow name: reach word}`: the row's `reach` where it carries one, else the last segment of
    its `step` tag, else `none`."""
    return {w["name"]: derive_reach(w) for w in load_loop(kit_dir)["workflow"]}


def read_dispositions(kit_dir):
    """The members of the one closed disposition set, in file order; LoopError for a definition that
    declares none."""
    data, where = read_definition(kit_dir)
    members = check_loop(data, where)["dispositions"]
    if not members:
        raise LoopError(where, "declares no disposition set, a [dispositions] table with its set")
    return members


def resolve_disposition(kit_dir, word):
    """The member `word` is or, through a `[[disposition-alias]]` row, means; LoopError for any other word."""
    data, where = read_definition(kit_dir)
    members = read_dispositions(kit_dir)
    if word in members:
        return word
    means = resolve_alias(data.get("disposition-alias", []), word)
    if means is not None:
        return means
    raise LoopError(where, "%r is no disposition and no alias of one; the set is %s" % (word, " ".join(members)))


def read_outcome_set(kit_dir, item):
    """The closed outcome set of the `[[item]]` row whose `tag` is `item`: the disposition set for a row
    declaring `outcomes = "dispositions"`, the row's own list otherwise, None for an item the definition
    does not declare. LoopError for an `item` table that is no array of tables, or a row found whose
    `outcomes` is neither."""
    data, where = read_definition(kit_dir)
    check_loop(data, where)
    rows = data.get("item", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise LoopError(where, "'item' is not an array of tables")
    for row in rows:
        if row.get("tag") != item:
            continue
        outcomes = row.get("outcomes")
        if outcomes == OUTCOMES_REF:
            return read_dispositions(kit_dir)
        if not isinstance(outcomes, list) or not outcomes or not all(isinstance(w, str) for w in outcomes):
            raise LoopError(where, "the item %s carries no outcomes, a list of words or %r" % (item, OUTCOMES_REF))
        return list(outcomes)
    return None


def check_disposition_record(kit_dir, record):
    """The value join of an owner's disposition record, `record` a mapping holding `Item` and
    `Disposition`: True where the word, as written and never through an alias, is a member of the item's
    closed outcome set; LoopError naming the item and its set for any other word; None for an item the
    definition does not declare, which is `unarmed` and never green."""
    item, word = record["Item"], record["Disposition"]
    outcomes = read_outcome_set(kit_dir, item)
    if outcomes is None:
        return None
    if word not in outcomes:
        raise LoopError((pathlib.Path(kit_dir) / DEFINITION).as_posix(),
                        "the disposition %r is outside the outcome set of %s: %s" % (word, item, " ".join(outcomes)))
    return True


def write_loop_plant(data, case, rows, base_rows):
    """`data`, the actor-witness list's `rows` and its `base_rows` with the break `case` names made in
    them, in place."""
    steps, workflows = data.get("step", []), {w.get("name"): w for w in data.get("workflow", [])}
    plan = next((r for r in steps if r.get("tag") == "step.plan"), {})
    if case == "witness-no-class":
        plan.get("witness", {}).pop("class", None)
    elif case == "witness-bad-class":
        plan.get("witness", {})["class"] = "agent-said"
    elif case in ("witness-actor-unlisted", "witness-actor-listed"):
        plan.get("witness", {})["class"] = "actor"
        if case == "witness-actor-listed":
            rows.append("step.plan\tstep.plan\tdWellOiledMachine")
            base_rows.append("step.plan\tstep.plan\tdWellOiledMachine")
    elif case == "actor-list-grown":
        rows.append("DOD_CORE\treuse-probed\tdWellOiledMachine")
    elif case == "actor-list-stale":
        rows.append("step.design\tstep.design\tdWellOiledMachine")
        base_rows.append("step.design\tstep.design\tdWellOiledMachine")
    elif case == "actor-list-no-build":
        rows.append("DOD_CORE\tkeepalive-reaped\tdNoSuchBuild")
        base_rows.append("DOD_CORE\tkeepalive-reaped\tdNoSuchBuild")
    elif case == "missing-step":
        data["step"] = [r for r in steps if r.get("tag") != "step.deploy"]
    elif case == "reordered":
        data["step"] = sorted(steps, key=lambda r: {"step.test": 2.5}.get(r.get("tag"), r.get("order", 0)))
    elif case == "bad-step":
        workflows["build"]["step"] = "step.ship"
    elif case == "bad-reach":
        workflows["spec-review"]["reach"] = "revew"
    elif case == "disposition-unknown":
        data["dispositions"]["set"].append("ask")
    else:
        next(r for r in data["disposition-alias"] if r.get("word") == "defer")["means"] = "postpone"


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    kit_dir = pathlib.Path(__file__).absolute().parent
    plant = argv[2] if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] else None
    if argv[:1] == ["--grade-site"] and len(argv) >= 2 and argv[1] in DECLARATION_SITES:
        try:
            lines, refusals = check_site_witnesses(kit_dir, argv[1], argv[2:])
        except LoopError as e:
            print("loop: %s" % e)
            return 1
        for line in lines:
            print(line)
        for r in refusals:
            print("loop: refused · %s" % r)
        return 1 if refusals else 0
    if argv != ["--check"] and plant not in PLANTS:
        print("usage: python loop_lib.py --check | --fixture --plant <%s> | --grade-site <%s> <entry>..." % (
            "|".join(PLANTS), "|".join(DECLARATION_SITES)), file=sys.stderr)
        return 2
    root = next((d for d in (kit_dir, *kit_dir.parents) if (d / ".git").exists()), kit_dir)
    try:
        data, where = read_definition(kit_dir)
        rows = read_actor_rows(kit_dir)
        if plant:
            base_rows, base_why = list(rows), "the shipped list as read"
            print("loop: fixture · plant %s · %s" % (plant, PLANTS[plant]))
            write_loop_plant(data, plant, rows, base_rows)
        loop = check_loop(data, where)
        if not loop["dispositions"]:
            raise LoopError(where, "declares no disposition set, a [dispositions] table with its set")
        witnesses = check_witness_classes(data, where)
    except LoopError as e:
        print("loop: %s" % e)
        return 1
    if not plant:
        base_rows, base_why = read_actor_base(kit_dir)
    for s in loop["step"]:
        print("loop: step %s · order %d · state %s · exit %s" % (s["tag"], s["order"], s["state"], s["exit"]))
    for w in loop["workflow"]:
        print("loop: workflow %s · order %d · step %s · reach %s" % (w["name"], w["order"], w["step"], derive_reach(w)))
    print("loop: dispositions %s" % " ".join(loop["dispositions"]))
    for a in data.get("disposition-alias", []):
        print("loop: disposition-alias %s · means %s" % (a["word"], a["means"]))
    print("loop: %d step(s) and %d workflow(s) read from %s" % (len(loop["step"]), len(loop["workflow"]), where))
    print("loop: witness classes %s · refused %s" % (" ".join(data["witnesses"]["classes"]),
                                                      " ".join(data["witnesses"]["refused"])))
    for a in data.get("witness-alias", []):
        print("loop: witness-alias %s · means %s" % (a["word"], a["means"]))
    sites = {}
    for site, cls, by in witnesses:
        print("loop: witness %s · class %s · by %s" % (site, cls, by))
        sites.setdefault(site, {})[site] = cls
    for line in rows:
        fields = line.split("\t")
        if len(fields) == 3:
            print("loop: actor witness %s · %s · until %s" % tuple(fields))
    if base_rows is None:
        print("loop: actor-list base · no comparison · %s" % base_why)
    else:
        print("loop: actor-list base · %s" % base_why)
    refusals = check_actor_list(rows, base_rows, sites, root)
    for r in refusals:
        print("loop: refused · %s" % r)
    return 1 if refusals else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
