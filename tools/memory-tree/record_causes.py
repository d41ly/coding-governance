#!/usr/bin/env python3
"""record_causes.py — every record names its cause (TOOL-dTotalRecall-19).

    python <prefix>/memory-tree/record_causes.py --check               # the causes and orphan checks
    python <prefix>/memory-tree/record_causes.py --measure             # the legacy-records seed's rows
    python <prefix>/memory-tree/record_causes.py --print-stand-ins     # the made-by-stand-in class's members
    python <prefix>/memory-tree/record_causes.py --print-record-keys   # the record-key class's members
    python <prefix>/memory-tree/record_causes.py --fixture --plant <case>

A record's header names what made it and why it exists: `**Made-by:**` and `**Caused-by:**` after its
`**Serves:**` line, or a typed kind's `- **Made-by:**` and `- **Caused-by:**` fields, read by
`tree_lib.read_header_edges`. The record door writes both (`gov_record.py new <kind> --caused-by <target>`).

THE CAUSES CHECK (`check_causes`). A tracked Markdown record with no `<path> -` row of the `legacy-records`
population, whose kind's `record-kinds.toml` row is not `root = true`, is red when it carries no
`Caused-by` or one that does not resolve: a target resolves when it is a family id the corpus defines
(`corpus_ids.py`'s defined-id set) or a record key, the stem of a tracked Markdown record. A record of a
typed kind whose row's `schema.fields` hold no `Caused-by`, written by its parent's own command, is graded
on its Serves units instead, each of which must resolve. A legacy record is never red.

THE ORPHAN CHECK (`check_orphans`). The roots are each build whose `README.md` is tracked, and each whose
claim ref `refs/gov/claims/<slug>` this repository holds. A unit id is reached when its README's `ids:`
names it, or, for a claim-rooted build, when its slug is the claim's; a record is reached when its cause
is, its `Caused-by` target or, for a legacy record, its Serves units, the walk a fixed point from the
roots outward, so two new records caused by each other are reached by neither and both are orphans. A
new record no root reaches is red.

THE WRITER CENSUS (`check_cause_writers`, TOOL-dTotalRecall-36 S7). Every tracked `*.py`, `*.sh` or `*.js`
file under the tool root, the alias census's walk (`record_kinds.read_code_paths`), test-named files
excepted, that spells a `**Serves:** ` literal and no `Caused-by` is red unless `CAUSE_WRITER_KEPT` keys it
with a reason, so the next writer that omits the cause line is red at its own pass, before the record it
writes is.

THE LEGACY POPULATION. `--measure` prints one TAB row `<path> - 1` per tracked Markdown record and, under
`memory.legacy-anchors` `derived`, one `<path> <anchor> 1` row per untagged `##` or `###` heading, its
anchor the playbook kit's `derive_anchor`; `legacy_ledger.py seed --population legacy-records` writes them
to the population's home. `read_legacy_anchors` is the one reader of the key: `derived` (the default)
derives anchors for untagged headings and reads a legacy record's Serves lines as its cause; `none`
derives none and reads a legacy record as reached; `retag` reads the authored tags alone,
`## [section.<anchor>] <heading>`, the form TOOL-dTotalRecall-20's retag step writes.

Exit: 0 green or unarmed (no registration, an absent or unarmed home, an empty population), 1 a red, 2 a
refused read, `memory.legacy-anchors` named. `--print-*` exit 3 where the class has no member here.
WHAT IT DOES NOT CHECK: a record that is not Markdown, which carries no header; whether a `Made-by`
names who really wrote it; the edge grammar of a header's targets, which `edge_grammar.py --check` grades;
whether a census file that spells `Caused-by` writes the line at run time, since the census grades spelling.
"""
from __future__ import annotations

import os
import pathlib
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
import tree_lib  # noqa: E402  the record population, its bindings and its header reader

SAY = "record causes"
POPULATION = "legacy-records"
ANCHOR_VALUES = ("derived", "none", "retag")
ANCHOR_DEFAULT = "derived"   # the catalogue default, which holds where no policy kit resolves
LEGACY_SECTION = "-"   # a population row's section cell naming the record itself
#: the `made-by-stand-in` class (TOOL-dTotalRecall-19 S4): `owner`, or the build lease a mint ran under
STAND_IN_RE = re.compile(r"owner|lease-[A-Za-z0-9][A-Za-z0-9_-]*")
HEADING_RE = re.compile(r"#{2,3} (?P<text>.*\S)")
#: an authored heading tag, the `[section.<anchor>]` TOOL-dTotalRecall-20's retag step writes
AUTHORED_TAG_RE = re.compile(r"\[section\.(?P<seg>[a-z0-9][a-z0-9-]*)\](?:[ \t]|$)")
PLANTS = ("legacy", "causeless", "typed-causeless", "orphan", "claim-root", "none", "writer-without-cause")
CLAIM_NS = "refs/gov/claims/"
#: TOOL-dTotalRecall-36 S7: the writer census's kept files, `{<path under the tool root>: <reason>}`, each
#: whose `**Serves:** ` literals are fixture, instruction or reader-prefix text only, so it writes no
#: record. Each key is spelled in parts: the install-prefix ban reads a kit path.
CAUSE_WRITER_KEPT = {
    "/".join(("loop", "placement.py")): "fixture: the disposition record its fixture reads back",
    "/".join(("memory-tree", "seen_red.py")): "fixture: the acceptance ledger its fixture plants",
    "/".join(("playbook", "instruction_units.py")): "fixture: the handoff head its fixture plants",
    "/".join(("policy", "check_policy.py")): "fixture: the handoff record its fixture plants",
    "/".join(("memory-tree", "adopt-memory-tree.sh")): "instruction: the binding grammar its next steps print",
    "/".join(("workflows", "replay_scorer.py")): "reader-prefix: SERVES_PREFIX and SPEC_SERVES_PREFIX, beside "
                                                 "fixture heads",
    "/".join(("workflows", "review_replay.py")): "reader-prefix: the spec mode's binding prefix, beside its "
                                                 "docstring and fixture records",
}
#: the census's test-named files, never census members: `*.test.sh`, `selftest.py`, `test_*.py`
CAUSE_WRITER_TEST_RE = re.compile(r"(?:^|/)(?:[^/]*\.test\.sh|selftest\.py|test_[^/]*\.py)$")
SERVES_LITERAL = "**Serves:** "
CAUSE_LITERAL = "Caused-by"
#: the writer plant's code file, under the fixture's tool root; its red line names it by line
CAUSE_WRITER_PLANT = "planted/writer.py"


def run_git(root, *args) -> subprocess.CompletedProcess:
    """`git -C <root> <args>`, UTF-8 text, never raising on a non-zero exit."""
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", stdin=subprocess.DEVNULL)


def read_conf(root) -> dict:
    """The tree's `.memory-tree.conf`, `MEMORY_ROOT` defaulted to `memory`."""
    from design_lib import read_design_conf   # noqa: E402  the conf's one reader
    conf = dict(read_design_conf(root))
    conf["MEMORY_ROOT"] = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/") or "memory"
    return conf


def read_tracked(root) -> list:
    """Every tracked path at `root`; ValueError where git does not list them."""
    p = run_git(root, "ls-files", "-z")
    if p.returncode != 0:
        raise ValueError(f"git ls-files failed at {root}")
    return [x for x in p.stdout.split("\0") if x]


def read_record_paths(root, tracked=None, conf=None) -> list:
    """The Markdown members of `tree_lib.record_paths` at `root`: the records that carry a header."""
    conf = conf or read_conf(root)
    tracked = read_tracked(root) if tracked is None else tracked
    return [p for p in tree_lib.record_paths(tracked, conf["MEMORY_ROOT"]) if p.endswith(".md")]


def read_record_keys(root, paths=None) -> dict:
    """`{stem: [paths]}` of the record-key class: a stem several records share resolves once."""
    keys = {}
    for p in read_record_paths(root) if paths is None else paths:
        keys.setdefault(pathlib.PurePosixPath(p).stem, []).append(p)
    return keys


def read_readme_slugs(root, tracked=None, conf=None) -> list:
    """The slug of every build whose `README.md` is tracked at `root`."""
    conf = conf or read_conf(root)
    tracked = read_tracked(root) if tracked is None else tracked
    sel = re.compile(re.escape(conf["MEMORY_ROOT"]) + r"/builds/([^/]+)/README\.md")
    return sorted(m.group(1) for p in tracked if (m := sel.fullmatch(p)))


def read_stand_ins(root) -> set:
    """The `made-by-stand-in` class's members: `owner` always, `lease-<slug>` for each tracked build README."""
    return {"owner"} | {f"lease-{s}" for s in read_readme_slugs(root)}


def read_defined_ids(root) -> set:
    """The family ids the corpus defines, the `family-id` class's members (`corpus_ids.py`'s walk)."""
    import corpus_ids  # noqa: E402  the defined-id set's one walk
    try:
        return set(corpus_ids.walk(str(root), corpus_ids.load_conf(str(root)))["defs"])
    except Exception as exc:   # its Problem and a conf it cannot read alike: the set is unread
        raise ValueError(f"the defined-id set did not read: {exc}") from None


def derive_target_class(root, target) -> str | None:
    """`record-key` or `family-id`, the class `target` matches, or None for neither."""
    if tree_lib.RECORD_KEY_RE.fullmatch(target):
        return "record-key"
    from id_grammar import grammar_for   # noqa: E402  the family-id grammar
    if re.fullmatch(grammar_for(root).ID, target):
        return "family-id"
    return None


def check_cause_target(root, target, keys=None, ids=None) -> str | None:
    """Why `target` does not resolve as a cause, or None where it does (TOOL-dTotalRecall-19 S5): a family
    id in the defined-id set, or a record key. `keys` and `ids` are the two sets, read where None."""
    cls = derive_target_class(root, target)
    if cls == "record-key":
        keys = read_record_keys(root) if keys is None else keys
        return None if target in keys else f"no tracked record's stem is {target}"
    if cls == "family-id":
        ids = read_defined_ids(root) if ids is None else ids
        return None if target in ids else f"the corpus defines no {target}"
    return f"{target} is neither a family id nor a record key"


def read_anchor_value(root) -> str:
    """`memory.legacy-anchors` at `root`'s landed revision; the default where no policy kit resolves.
    ValueError naming the key where the reader refuses or answers outside the key's values."""
    try:
        value = tree_lib.read_policy_value("memory.legacy-anchors", root)
    except LookupError:
        return ANCHOR_DEFAULT
    if value not in ANCHOR_VALUES:
        raise ValueError(f"memory.legacy-anchors reads {value!r}, outside {' | '.join(ANCHOR_VALUES)}")
    return value


def read_legacy_anchors(root, path, text=None, value=None) -> list:
    """The anchors of the record at `path` that `memory.legacy-anchors` admits (S10): under `derived` the
    derived anchor of each untagged `##` or `###` heading outside fences, through the playbook kit's
    `derive_anchor`; under `none` none; under `retag` each authored `[section.<anchor>]` tag. `text` the
    record's text, read where None; `value` the key's, read where None. ValueError where the key's read
    is refused."""
    value = read_anchor_value(root) if value is None else value
    if value == "none":
        return []
    if text is None:
        text = tree_lib.read_text(os.path.join(str(root), path))
    derive_anchor = None
    if value == "derived":
        from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
        kit = resolve_kit_dir("playbook", "tag_index.py", KIT)
        if str(kit) not in sys.path:
            sys.path.append(str(kit))
        from tag_index import derive_anchor   # noqa: E402  the one anchor rule (TOOL-dTotalRecall-10)
    out, seen = [], set()
    for _n, line in tree_lib.unfenced_lines(text):
        if line is None:
            break
        m = HEADING_RE.fullmatch(line.rstrip())
        if not m:
            continue
        tag = AUTHORED_TAG_RE.match(m.group("text"))
        if value == "retag":
            if tag:
                out.append(tag.group("seg"))
        elif not tag:
            anchor = derive_anchor(m.group("text"), seen)
            if anchor:
                out.append(anchor)
    return out


def derive_population_rows(root, value=None) -> list:
    """`[(path, section)]`, the `legacy-records` rows of the tree at `root`: `(path, "-")` per Markdown
    record, then `(path, anchor)` per anchor `read_legacy_anchors` admits."""
    value = read_anchor_value(root) if value is None else value
    rows = []
    for p in read_record_paths(root):
        try:
            text = tree_lib.read_text(os.path.join(str(root), p))
        except (OSError, UnicodeDecodeError):
            continue
        rows.append((p, LEGACY_SECTION))
        rows += [(p, a) for a in read_legacy_anchors(root, p, text, value)]
    return rows


def read_legacy_paths(root) -> tuple:
    """`(paths, note)`: the paths of the population's `-` rows, or None and why the check is unarmed."""
    import legacy_ledger as ll   # noqa: E402  the ledger factory
    try:
        reg = next((r for r in ll.read_registrations(root) if r.population == POPULATION), None)
    except ValueError as exc:
        raise ValueError(f"the ledger registrations do not read: {str(exc).splitlines()[0]}") from None
    if reg is None:
        return None, f"no [[ledger]] table registers {POPULATION}"
    home = pathlib.Path(root, reg.home)
    state = ll.read_home_state(home)
    if state != "armed":
        return None, f"{POPULATION}'s home {reg.home} is {state}"
    rows, bad = ll.read_ledger(root, reg)
    if bad:
        raise ValueError(f"{reg.home}: {ll.render_malformed(bad[0])}")
    paths = {k[0] for k in rows if k[1] == LEGACY_SECTION}
    if not paths:
        return None, f"{POPULATION}'s home {reg.home} holds no record row"
    return paths, f"{len(paths)} record row(s) (-), {len(rows) - len(paths)} section row(s)"


def read_grading(root) -> dict:
    """Everything both checks read, once: the records, their texts and bindings, the two target sets, the
    registry's rows by kind, the legacy paths and `memory.legacy-anchors`. ValueError for a refused read."""
    import record_kinds   # noqa: E402  the registry's reader
    root = pathlib.Path(root)
    conf = read_conf(root)
    tracked = read_tracked(root)
    paths = read_record_paths(root, tracked, conf)
    texts = {}
    for p in paths:
        try:
            texts[p] = tree_lib.read_text(os.path.join(str(root), p))
        except (OSError, UnicodeDecodeError):
            continue
    try:
        rows = {r.get("name"): r for r in record_kinds.read_record_kinds(root) or []}
    except record_kinds.RecordKindsError as exc:
        raise ValueError(str(exc)) from None
    legacy, note = read_legacy_paths(root)
    return {"root": root, "conf": conf, "tracked": tracked, "texts": texts, "rows": rows, "legacy": legacy,
            "note": note, "bindings": tree_lib.read_bindings(str(root), list(texts), conf),
            "keys": read_record_keys(root, list(texts)), "ids": read_defined_ids(root) if legacy is not None else set(),
            "value": read_anchor_value(root)}


def derive_record_cause(g, path) -> tuple:
    """`(how, targets, finding)` of one record: `how` `root`, `serves` (a legacy record, or a typed kind
    declaring no `Caused-by`, graded on its Serves units) or `caused-by`; `finding` its header's refusal."""
    binding = g["bindings"].get(path) or {}
    kind = tree_lib.resolve_kind(binding.get("kind") or "")
    import build_records   # noqa: E402  the typed kinds' name grammar
    named = next((k for k in tree_lib.TYPED_RECORD_KINDS if build_records.derive_record_name(k).search(path)), None)
    kind = named or kind
    row = g["rows"].get(kind) or {}
    if row.get("root") is True:
        return "root", [], None
    fields = (row.get("schema") or {}).get("fields", []) if isinstance(row.get("schema"), dict) else []
    if path in g["legacy"] or (kind in tree_lib.TYPED_RECORD_KINDS and "Caused-by" not in fields):
        return "serves", list(binding.get("ids") or []), None
    try:
        edges = tree_lib.read_header_edges(g["texts"][path], path, binding)
    except ValueError as exc:
        return "caused-by", [], f"its header is refused: {exc}"
    return "caused-by", [t for e in edges if e["type"] == "caused-by" for t in e["targets"]], None


def check_causes(root, g=None) -> list:
    """S8: one finding line per new record with no resolving cause."""
    g = g or read_grading(root)
    out = []
    for path in g["texts"]:
        how, targets, finding = derive_record_cause(g, path)
        if how == "root" or (how == "serves" and path in g["legacy"]):
            continue
        if finding:
            out.append(f"{SAY}: causes · {path} · {finding}")
        elif not targets:
            out.append(f"{SAY}: causes · {path} · " + ("serves no unit, its kind's cause" if how == "serves"
                                                       else "names no Caused-by, and its kind is no root"))
        for t in targets:
            why = check_cause_target(root, t, g["keys"], g["ids"])
            if why:
                out.append(f"{SAY}: causes · {path} · {'Serves' if how == 'serves' else 'Caused-by'} {t} does not "
                           f"resolve: {why}")
    return out


def read_claim_slugs(root) -> set:
    """The slugs of the build claim refs `refs/gov/claims/<slug>` this repository holds, never an ask counter."""
    p = run_git(root, "for-each-ref", "--format=%(refname)", CLAIM_NS)
    return {r[len(CLAIM_NS):] for r in p.stdout.splitlines() if r.startswith(CLAIM_NS) and "/" not in r[len(CLAIM_NS):]}


def read_rooted_units(g) -> tuple:
    """`(unit ids the tracked READMEs' ids: name, claim-rooted slugs)`, the walk's roots."""
    alt = tree_lib._id_alternation(g["conf"])
    ids = set()
    for slug in read_readme_slugs(g["root"], g["tracked"], g["conf"]):
        try:
            text = tree_lib.read_text(os.path.join(str(g["root"]), g["conf"]["MEMORY_ROOT"], "builds", slug, "README.md"))
        except (OSError, UnicodeDecodeError):
            continue
        fm = tree_lib.FM_RE.match(text)
        for line in (fm.group(1).split("\n") if fm else []):
            if line.startswith("ids:"):
                ids |= set(tree_lib._expand_ids(line[4:].strip(), alt, str(g["root"]))[0])
    return ids, read_claim_slugs(g["root"])


def derive_reached(g) -> set:
    """The paths of the records the roots reach, a fixed point from the roots outward (§4 "The walk")."""
    units, claims = read_rooted_units(g)

    def check_unit_reached(uid):
        """A unit is reached when a rooted README names it or its slug is a claim's."""
        parts = uid.split("-")
        return uid in units or (len(parts) >= 3 and "-".join(parts[1:-1]) in claims)

    causes, reached = {}, set()
    for path in g["texts"]:
        how, targets, _f = derive_record_cause(g, path)
        if how == "root" or (path in g["legacy"] and g["value"] == "none"):
            reached.add(path)
        else:
            causes[path] = targets
    keys = {pathlib.PurePosixPath(p).stem for p in reached}
    moved = True
    while moved:
        moved = False
        for path, targets in causes.items():
            if path in reached:
                continue
            if any(t in keys if tree_lib.RECORD_KEY_RE.fullmatch(t) else check_unit_reached(t) for t in targets):
                reached.add(path)
                keys.add(pathlib.PurePosixPath(path).stem)
                moved = True
    return reached


def check_orphans(root, g=None) -> list:
    """S9: one finding line per new record no root reaches; a legacy record is never red."""
    g = g or read_grading(root)
    reached = derive_reached(g)
    return [f"{SAY}: orphans · {p} · no root reaches it through its cause" for p in g["texts"]
            if p not in reached and p not in g["legacy"]]


def check_cause_writers(root) -> tuple:
    """S7's writer census: `(lines, reds)` over the alias census's population, every tracked `*.py`, `*.sh`
    and `*.js` file under the tool root (`record_kinds.read_code_paths`), test-named files excepted. A census
    file spells a `**Serves:** ` literal and no `Caused-by`, and is red unless `CAUSE_WRITER_KEPT` keys it by
    its path under the tool root, then printed `kept <reason>`; one line per census file at its first Serves
    literal, then a count line. It grades spelling, never whether the file writes the line at run time."""
    import record_kinds   # noqa: E402  the tool root and the code census's one walk
    tool_rel = record_kinds.derive_tool_rel(record_kinds.derive_kit_rel())
    try:
        paths = [p for p in record_kinds.read_code_paths(root, tool_rel) if not CAUSE_WRITER_TEST_RE.search(p)]
    except record_kinds.RecordKindsError as exc:
        raise ValueError(str(exc)) from None
    lines, reds, kept = [], [], 0
    for path in paths:
        text = pathlib.Path(root, path).read_bytes().decode("utf-8", "replace")
        if SERVES_LITERAL not in text or CAUSE_LITERAL in text:
            continue
        n = next(i for i, ln in enumerate(text.splitlines(), 1) if SERVES_LITERAL in ln)
        key = path[len(tool_rel) + 1:] if tool_rel else path
        if key in CAUSE_WRITER_KEPT:
            kept += 1
            lines.append(f"cause-writer · {path}:{n} · kept {CAUSE_WRITER_KEPT[key]}")
            continue
        lines.append(f"cause-writer · {path}:{n} · red")
        reds.append(f"cause-writer {path}:{n}: spells a Serves line and no Caused-by; write the cause line under "
                    f"its Serves line, or key the file in CAUSE_WRITER_KEPT with its reason")
    lines.append(f"cause-writer · {len(paths)} code files under {tool_rel or '.'} · {kept + len(reds)} census "
                 f"file(s) · {kept} kept · {len(reds)} red")
    return lines, reds


def run_check(root) -> tuple:
    """`--check`: `(lines, exit)`."""
    try:
        g = read_grading(root)
    except ValueError as exc:
        return [f"{SAY}: refused · {exc}"], 2
    if g["legacy"] is None:
        return [f"{SAY}: unarmed · {g['note']}"], 0
    causes, orphans = check_causes(root, g), check_orphans(root, g)
    try:
        writer_lines, writer_reds = check_cause_writers(root)
    except ValueError as exc:
        return [f"{SAY}: refused · {exc}"], 2
    lines = [f"{SAY}: {POPULATION} · {g['note']} · memory.legacy-anchors {g['value']}",
             f"{SAY}: {len(g['texts'])} Markdown record(s) · {len(g['legacy'] & set(g['texts']))} legacy"]
    lines += causes + orphans
    lines += [f"{SAY}: {ln}" for ln in writer_lines] + [f"{SAY}: RED {r}" for r in writer_reds]
    lines.append(f"{SAY}: {len(causes)} causeless · {len(orphans)} orphan(s)")
    red = bool(causes or orphans or writer_reds)
    lines.append(f"{SAY}: {'RED' if red else 'green'}")
    return lines, 1 if red else 0


# ------------------------------------------------------------------------------------------ the fixture
FIXTURE_UNIT = "TOOL-fRoot-1"
FIXTURE_CLAIM = "TOOL-fClaim-1"


def write_fixture(top, plant) -> pathlib.Path:
    """The plant's repository under `top`: a conf, a three-row registry (`log`, `research`, `card`), a govkit
    registry holding the `legacy-records` table as gov registers it, the build `fRoot` (README, a spec, a
    log record and a research record repeating `## Findings`), committed; the population seeded; then the
    plant's new records and refs, committed. `none` commits `memory.legacy-anchors = "none"` first."""
    import json
    import legacy_ledger as ll   # noqa: E402  the seed, run as `seed` runs it
    import record_kinds   # noqa: E402  the kit's path inside a repository
    root = pathlib.Path(top, "repo")
    kit_rel = record_kinds.derive_kit_rel()
    tool_rel = record_kinds.derive_tool_rel(kit_rel)
    prefix = "{prefix}"

    def write_file(rel, text):
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))

    def run_commit(msg):
        for args in (("add", "-A"), ("-c", "user.name=fx", "-c", "user.email=fx@example.invalid", "-c",
                                     "commit.gpgsign=false", "commit", "-q", "--no-verify", "-m", msg)):
            p = run_git(root, *args)
            if p.returncode:
                raise ValueError(f"the fixture's git {args[0]} refused: {p.stderr.strip()}")

    rows = {"log": ("memory/builds/*/prompts/*.md", '["Serves"]'), "research": ("memory/builds/*/build/*.md", '["Serves"]'),
            "card": ("memory/builds/*/build/*-build-*-card-*.md", '["Build", "Step", "Ref"]')}
    write_file(".memory-tree.conf", 'MEMORY_ROOT="memory"\nFAMILIES="tooling:TOOL"\n')
    write_file(f"{kit_rel}/{record_kinds.REGISTRY}", "".join(
        f'[[record-kind]]\nname = "{n}"\nhome = "{h}"\nschema = {{ form = "fields", fields = {f} }}\n\n'
        for n, (h, f) in rows.items()))
    sibling = "/".join(("govkit", "registry.toml"))   # spelled in parts: the install-prefix ban reads a kit path
    write_file(f"{tool_rel}/{sibling}" if tool_rel else sibling,
               f'[[ledger]]\npopulation = "{POPULATION}"\nleg = "record causes"\n'
               f'seed = {json.dumps(["python", f"{prefix}/{kit_rel[len(tool_rel) + 1:] if tool_rel else kit_rel}/record_causes.py", "--measure"])}\n'
               'key = "record"\nfields = ["path", "section"]\nverbatim = ["section"]\ndrain = "key"\n'
               f'direction = "shrink-only"\nhome = "memory/project/{POPULATION}.txt"\n')
    write_file("memory/project/README.md", "the fixture's project registry\n")
    write_file("memory/builds/fRoot/README.md", f"---\nslug: fRoot\nopened: 2026-01-01\nids: {FIXTURE_UNIT}\n---\n\n# fRoot\n")
    for unit in (FIXTURE_UNIT, FIXTURE_CLAIM):
        slug = unit.split("-")[1]
        write_file(f"memory/builds/{slug}/spec/2026-01-01-spec-{unit}.md",
                   f"# {unit} — the fixture's unit\n\n**Status:** OPEN · rev-1 · 2026-01-01 · node a · Tier-1 · base 00000000\n")
    write_file(f"memory/builds/fRoot/prompts/2026-01-01-prompt-{FIXTURE_UNIT}-brief.md",
               f"**Serves:** journal {FIXTURE_UNIT}\n\n# A brief shaped like today's\n\nthe brief\n")
    write_file(f"memory/builds/fRoot/build/2026-01-01-build-{FIXTURE_UNIT}-notes.md",
               f"**Serves:** research {FIXTURE_UNIT}\n\n# Notes\n\n## Findings\n\none\n\n## Findings\n\ntwo\n")
    if plant == "none":
        write_file(".governance/policy.toml", 'memory.legacy-anchors = "none"\n')
    for args in (("init", "-q", "--template="), ("symbolic-ref", "HEAD", "refs/heads/main"),   # main: the landed branch
                 ("config", "core.autocrlf", "false")):
        p = run_git(root, *args)
        if p.returncode:
            raise ValueError(f"the fixture's git {args[0]} refused: {p.stderr.strip()}")
    run_commit("record-causes fixture: the legacy tree")
    reg = next(r for r in ll.read_registrations(root) if r.population == POPULATION)
    line, _ok = ll.seed_population(root, reg, run_git(root, "rev-parse", "HEAD").stdout.strip())
    print(f"{SAY}: fixture {plant} · seed · {line}")
    build = "memory/builds/fRoot/build"
    if plant == "causeless":
        write_file(f"{build}/2026-01-02-build-{FIXTURE_UNIT}-new.md", f"# New\n\n**Serves:** research {FIXTURE_UNIT}\n")
    elif plant == "typed-causeless":
        write_file(f"{build}/2026-01-02-build-{FIXTURE_UNIT}-card-1.md",
                   f"# {FIXTURE_UNIT} card 1 — a card\n\n**Serves:** card {FIXTURE_UNIT}\n\n- **Build:** fRoot\n"
                   "- **Step:** 1\n- **Ref:** refs/x\n")
    elif plant == "orphan":
        a, b = (f"2026-01-02-build-{FIXTURE_UNIT}-cycle-{n}" for n in "ab")
        for me, other in ((a, b), (b, a)):
            write_file(f"{build}/{me}.md", f"# Cycle\n\n**Serves:** research {FIXTURE_UNIT}\n**Made-by:** owner\n"
                                           f"**Caused-by:** {other}\n")
    elif plant == "claim-root":
        write_file(f"memory/builds/fClaim/build/2026-01-02-build-{FIXTURE_CLAIM}-claimed.md",
                   f"# Claimed\n\n**Serves:** research {FIXTURE_CLAIM}\n**Made-by:** owner\n**Caused-by:** {FIXTURE_CLAIM}\n")
    else:   # legacy, none and the writer plant: a new record caused by a unit, beside the legacy tree
        write_file(f"{build}/2026-01-02-build-{FIXTURE_UNIT}-caused.md",
                   f"# Caused\n\n**Serves:** research {FIXTURE_UNIT}\n**Made-by:** owner\n**Caused-by:** {FIXTURE_UNIT}\n")
    if plant == "writer-without-cause":   # TOOL-dTotalRecall-36 S7: a code file spelling a Serves literal, no cause
        write_file(f"{tool_rel}/{CAUSE_WRITER_PLANT}" if tool_rel else CAUSE_WRITER_PLANT,
                   f'"""A record writer."""\nHEAD = "{SERVES_LITERAL}log {FIXTURE_UNIT}\\n"\n')
    run_commit(f"record-causes fixture: {plant}")
    if plant == "claim-root":
        p = run_git(root, "update-ref", f"{CLAIM_NS}fClaim", run_git(root, "rev-parse", "HEAD").stdout.strip())
        if p.returncode:
            raise ValueError(f"the fixture's claim ref refused: {p.stderr.strip()}")
    return root


def run_fixture(plant) -> tuple:
    """`--fixture --plant <case>`: the plant's repository under the system temp directory, its population's
    rows printed, then `--check` run there. -> `(lines, exit)`."""
    if plant not in PLANTS:
        return [f"{SAY}: refused · no plant {plant!r}: the plants are {', '.join(PLANTS)}"], 2
    from deviation_join import remove_tree, set_env_aside   # noqa: E402  the kit's fixture helpers
    top = pathlib.Path(tempfile.mkdtemp(prefix="rc-"))
    try:
        with set_env_aside(tree_lib.GIT_ENV_LEAKS):
            root = write_fixture(top, plant)
            home = root / "memory/project" / f"{POPULATION}.txt"
            rows = [ln for ln in home.read_bytes().decode("utf-8").split("\n")[1:] if ln]
            head = [f"{SAY}: fixture {plant} · row · " + " ".join(ln.split("\t")[:3]).replace(str(root), "") for ln in rows]
            lines, rc = run_check(root)
        return head + lines, rc
    except (ValueError, OSError, StopIteration) as exc:
        return [f"{SAY}: fixture {plant} could not be built: {exc}"], 2
    finally:
        remove_tree(top)


def main(argv) -> int:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace", newline="\n")
    root = pathlib.Path(run_git(".", "rev-parse", "--show-toplevel").stdout.strip() or ".")
    if argv == ["--check"]:
        lines, rc = run_check(root)
    elif argv == ["--measure"]:
        try:
            rows = derive_population_rows(root)
        except ValueError as exc:
            print(f"{SAY}: refused · {exc}")
            return 2
        lines, rc = [f"{p}\t{s}\t1" for p, s in rows], 0
    elif argv == ["--print-stand-ins"]:
        lines, rc = sorted(read_stand_ins(root)), 0
    elif argv == ["--print-record-keys"]:
        keys = sorted(read_record_keys(root))
        lines, rc = keys, 0 if keys else 3
    elif len(argv) == 3 and argv[:2] == ["--fixture", "--plant"]:
        lines, rc = run_fixture(argv[2])
    else:
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    for line in lines:
        print(line)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
