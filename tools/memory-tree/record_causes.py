#!/usr/bin/env python3
"""record_causes.py — every record names its cause (TOOL-dTotalRecall-19).

    python <prefix>/memory-tree/record_causes.py --check               # the causes and orphan checks
    python <prefix>/memory-tree/record_causes.py --measure             # the legacy-records seed's rows
    python <prefix>/memory-tree/record_causes.py --print-stand-ins     # the made-by-stand-in class's members
    python <prefix>/memory-tree/record_causes.py --print-record-keys   # the record-key class's members
    python <prefix>/memory-tree/record_causes.py --backfill            # write the cause line the causes check lacks
    python <prefix>/memory-tree/record_causes.py --fixture --plant <case>

A record's header names what made it and why it exists: `**Made-by:**` and `**Caused-by:**` after its
`**Serves:**` line, or a typed kind's `- **Made-by:**` and `- **Caused-by:**` fields, read by
`tree_lib.read_header_edges`. The record door writes both (`gov_record.py new <kind> --caused-by <target>`).

THE GRADED SET (`read_grading`, TOOL-dTotalRecall-51 S3). The Markdown members of `tree_lib.record_paths`,
and each non-Markdown member whose first Serves line wears a comment prefix (`tree_lib.BIND_RE`'s `prefix`),
whose cause line wears the same prefix. A non-Markdown record whose Serves line is bare, or that has none, is
not graded, and record keys stay Markdown stems.

THE CAUSES CHECK (`check_causes`). A graded record with no `<path> -` row of the `legacy-records`
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
writes is. A file kept as rendering a pinned instrument's bytes (`KEPT_INSTRUMENT`, TOOL-dTotalRecall-49
S3) is red where that stops being true: where `design_lib.read_design_keys` reads the design keys off or
refuses them, or where the record `DESIGN_VIEW` names has no `<path> -` row of the `legacy-records`
population. Then the build folders' scripts (TOOL-dTotalRecall-50 S1), every tracked `*.py`, `*.sh` or `*.js`
file under `<memory root>/builds/*/build/`, test-named files excepted, read past their `BIND_HEAD_LINES`
binding window by both tests, so a file's own binding is never a hit; each census file is kept by its
repository path in `CAUSE_WRITER_KEPT` or is the instrument of a `CAUSE_WRITER_PINNED` row, and its count
line counts them apart.

THE PINNED WRITERS (`CAUSE_WRITER_PINNED`, TOOL-dTotalRecall-50 S2 S3). One `(instrument, glob, ask id)` row
per pinned instrument that writes a record with no cause, whose owner alone moves its pin. `--check` prints
each row with its ask id and the records its glob reads, red where the instrument is untracked, spells
`Caused-by` past its binding window (drain the row), or its ask is no ask `backlog.parse_file` reads in the
`BACKLOG.md` of the build its id names. While a row stands, a new record its glob reads that carries no
`Caused-by` is read as caused by its first Serves id, by the causes and orphan checks alike.

THE LEGACY POPULATION. `--measure` prints one TAB row `<path> - 1` per tracked Markdown record and, under
`memory.legacy-anchors` `derived`, one `<path> <anchor> 1` row per untagged `##` or `###` heading, its
anchor the playbook kit's `derive_anchor`; `legacy_ledger.py seed --population legacy-records` writes them
to the population's home. `read_legacy_anchors` is the one reader of the key: `derived` (the default)
derives anchors for untagged headings and reads a legacy record's Serves lines as its cause; `none`
derives none and reads a legacy record as reached; `retag` reads the authored tags alone,
`## [section.<anchor>] <heading>`, the form TOOL-dTotalRecall-20's retag step writes.

Exit: 0 green or unarmed (no registration, an absent or unarmed home, an empty population), 1 a red, 2 a
refused read, `memory.legacy-anchors` named. `--print-*` exit 3 where the class has no member here.
WHAT IT DOES NOT CHECK: a non-Markdown record whose head is not a comment; whether a `Made-by`
names who really wrote it; the edge grammar of a header's targets, which `edge_grammar.py --check` grades;
whether a census file that spells `Caused-by` writes the line at run time, since the census grades spelling;
whether a pinned row's glob names the records its instrument really writes, or its ask is live past filed.

THE BACKFILL (`write_missing_causes`, TOOL-dTotalRecall-47). `--backfill` keeps the causes check's findings
whose rule is the absent cause (`ABSENT_CAUSE`), so it selects what the check reds and never a copy of the
selection, and writes `**Caused-by:** <first Serves id>` on the line after the record's first Serves line,
in the file's own line ending, printing each path it wrote and a count. It refuses to guess, listing under
`not backfilled` with its reason and leaving byte-identical: a record that is not Markdown (its cause line
wears its Serves line's comment prefix, TOOL-dTotalRecall-51), one a typed kind's name grammar matches (its
cause is a `- **Caused-by:**` field its kind's writer writes), one whose Serves line names no id, and one
whose Serves line is the last line of the head window, where a cause line would fall outside what
`read_header_edges` reads. A second run writes nothing. Exit 0, a refused read 2.
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
PLANTS = ("legacy", "causeless", "typed-causeless", "orphan", "claim-root", "none", "writer-without-cause",
          "bulleted-cause", "bulleted-twice", "script-cause-prefixed", "script-cause-bare", "script-causeless",
          "backfill-selection", "backfill-refusals", "kept-instrument-not-legacy", "pinned-writer-drained",
          "departures-pinned")
#: TOOL-dTotalRecall-47 S1: the causes check's absent-cause rule, the one finding `--backfill` selects
ABSENT_CAUSE = "names no Caused-by, and its kind is no root"
#: TOOL-dTotalRecall-47 AC1 AC3: each backfill plant's new records, `{<path>: <text>}`, `{build}` the fixture's
#: build folder, `{unit}` its unit. The selection plant: a causeless record the verb writes, a record of the
#: kind the plant's registry marks root, a `.sh` record and a record whose Serves line names no id; the
#: refusals plant: a typed record with no `Caused-by` field and a record whose Serves line is the head
#: window's last unfenced line
BACKFILL_PLANTS = {
    "backfill-selection": {
        "{build}/2026-01-02-build-{unit}-new.md": "# New\n\n**Serves:** research {unit}\n",
        "memory/builds/fRoot/reviews/2026-01-02-review-{unit}-audit.md": "**Serves:** spec-audit {unit}\n\n# An audit\n",
        "{build}/2026-01-02-build-{unit}-probe.sh": "# **Serves:** log {unit}\necho probe\n",
        "{build}/2026-01-02-build-{unit}-unbound.md": "# Unbound\n\n**Serves:** research\n",
    },
    "backfill-refusals": {
        "{build}/2026-01-02-build-{unit}-deviation-1.md": "# {unit} deviation 1 — no cause field\n\n"
                                                         "**Serves:** deviation {unit}\n\n- **Summary:** a departure\n",
        "{build}/2026-01-02-build-{unit}-late.md": "# Late\n" + "a line of the head\n" * 10
                                                   + "**Serves:** research {unit}\n",
    },
}
#: each backfill plant's expected first `--backfill`: `({<path>: <reason token>} not backfilled, [paths written])`
BACKFILL_EXPECTED = {
    "backfill-selection": ({"{build}/2026-01-02-build-{unit}-probe.sh": "not markdown",
                            "{build}/2026-01-02-build-{unit}-unbound.md": "no id"},
                           ["{build}/2026-01-02-build-{unit}-new.md"]),
    "backfill-refusals": ({"{build}/2026-01-02-build-{unit}-deviation-1.md": "typed kind",
                           "{build}/2026-01-02-build-{unit}-late.md": "head window"}, []),
}
#: TOOL-dTotalRecall-39 AC2 AC3: the plants whose typed record's cause is a bulleted field, each the number of
#: `- **Caused-by:**` fields it writes; both checks read the record, the causes check and the edge walk
BULLETED_PLANTS = {"bulleted-cause": 1, "bulleted-twice": 2}
BULLETED_UNIT = "TOOL-tFix-1"
BULLETED_RECORD = f"memory/builds/tFix/build/2026-01-02-build-{BULLETED_UNIT}-deviation-1.md"
#: the record's head, its fields following from the line after its last
BULLETED_HEAD = f"# {BULLETED_UNIT} deviation 1 — a bulleted cause\n\n**Serves:** deviation {BULLETED_UNIT}\n\n"
#: TOOL-dTotalRecall-51 AC1 to AC3: each script plant's records, `{<name after the record's unit>: <text>}`,
#: `{unit}` the fixture's unit; a cause line wears its Serves line's prefix, and a bare head is not graded
SCRIPT_PLANTS = {
    "script-cause-prefixed": {"probe.py": "# **Serves:** log {unit}\n# **Caused-by:** {unit}\nprint('probe')\n"},
    "script-cause-bare": {"probe.sh": "# **Serves:** log {unit}\n**Caused-by:** {unit}\necho probe\n"},
    "script-causeless": {"probe.sh": "# **Serves:** log {unit}\necho probe\n",
                         "atlas.html": "**Serves:** research {unit}\n<p>an atlas</p>\n"},
}
CLAIM_NS = "refs/gov/claims/"
#: TOOL-dTotalRecall-49 S2 S3: the kept reason of a file whose one output is a pinned instrument's bytes, and
#: the as-built view's renderer, kept for it; the census reds the reason where DESIGN_VIEW is no legacy record
KEPT_INSTRUMENT = "renders a pinned instrument's bytes; its one output is a legacy record"
KEPT_INSTRUMENT_KEY = "/".join(("memory-tree", "asbuilt_view.py"))
#: TOOL-dTotalRecall-36 S7: the writer census's kept files, `{<path under the tool root>: <reason>}`, each
#: whose `**Serves:** ` literals are fixture, instruction or reader-prefix text only, so it writes no
#: record, or, TOOL-dTotalRecall-49 S2, whose one output is a pinned instrument's legacy record. Each key
#: is spelled in parts: the install-prefix ban reads a kit path. TOOL-dTotalRecall-50 S1: a build folder's
#: census file is keyed by its repository path, kept as a `pinned instrument` the dClosedLoop packet's
#: INSTRUMENTS names or as `outside the write set`.
KEPT_PINNED = "pinned instrument"
KEPT_OUTSIDE = "outside the write set"
CLOSED_LOOP = "memory/builds/dClosedLoop/build/"
CAUSE_WRITER_KEPT = {
    CLOSED_LOOP + "2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py": KEPT_PINNED,
    CLOSED_LOOP + "2026-10-20-build-PLAY-dClosedLoop-1-packet.py": KEPT_PINNED,
    CLOSED_LOOP + "2026-10-19-build-PLAY-dClosedLoop-1-walk.py": KEPT_OUTSIDE,
    CLOSED_LOOP + "2026-10-20-build-PLAY-dClosedLoop-1-fold-inventory.py": KEPT_OUTSIDE,
    CLOSED_LOOP + "2026-10-20-build-PLAY-dClosedLoop-1-walk-seed.py": KEPT_OUTSIDE,
    "memory/builds/aMendedFleet/build/2026-10-06-build-TOOL-aMendedFleet-73-harness.py": KEPT_OUTSIDE,
    "memory/builds/aMendedFleet/build/2026-10-06-build-TOOL-aMendedFleet-93-ab.py": KEPT_OUTSIDE,
    "memory/builds/dDerivedDocket/build/2026-09-22-build-TOOL-dDerivedDocket-33-signer.py": KEPT_OUTSIDE,
    KEPT_INSTRUMENT_KEY: KEPT_INSTRUMENT,
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
#: TOOL-dTotalRecall-50 S2: the records the departures instrument writes, `deviations.py#derive_report_path`'s name
DEPARTURES_GLOB = "memory/builds/*/build/*-build-*-departures-*.md"
#: TOOL-dTotalRecall-50 S2: one `(instrument, glob, ask id)` row per pinned instrument writing a record with no
#: cause: its repository path, the glob of the records it writes, and the filed ask asking its owner for the
#: line. A row is red where its instrument is untracked or spells `Caused-by` past its binding window, or where
#: its ask is no filed ask; while it stands, S3 reads a causeless new record its glob matches as caused by
#: its first Serves id.
CAUSE_WRITER_PINNED = (
    (CLOSED_LOOP + "2026-10-19-build-PLAY-dClosedLoop-1-deviations.py", DEPARTURES_GLOB, "PLAY-dClosedLoop-1002"),
)


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


def read_pinned_records(root, pinned) -> dict:
    """`{glob: [paths]}`: the tracked records each standing row of `pinned` (CAUSE_WRITER_PINNED's shape)
    reads, through `record_kinds.read_tracked`, `*` never crossing a `/`. ValueError where git refuses."""
    import record_kinds   # noqa: E402  the one tracked-glob walk
    try:
        return {glob: record_kinds.read_tracked(root, glob) for _instrument, glob, _ask in pinned}
    except record_kinds.RecordKindsError as exc:
        raise ValueError(str(exc)) from None


def read_grading(root, pinned=CAUSE_WRITER_PINNED) -> dict:
    """Everything both checks read, once: the graded records (the Markdown ones, then each non-Markdown one
    whose first Serves line wears a comment prefix, TOOL-dTotalRecall-51 S3), their texts and bindings, the
    two target sets, the registry's rows by kind, the legacy paths, `memory.legacy-anchors`, and the records
    the standing rows of `pinned` read (TOOL-dTotalRecall-50 S3). ValueError for a refused read."""
    import record_kinds   # noqa: E402  the registry's reader
    root = pathlib.Path(root)
    conf = read_conf(root)
    tracked = read_tracked(root)
    paths = read_record_paths(root, tracked, conf)

    def read_serves_prefix(text):
        """The comment prefix the first Serves line in `text`'s head wears, `""` bare, None for no Serves line."""
        for line in list(tree_lib.unfenced(text))[:tree_lib.BIND_HEAD_LINES]:
            mo = tree_lib.BIND_RE.match(line)
            if mo and mo.group("key") == "Serves":
                return mo.group("prefix") or ""
        return None

    texts = {}
    for p in paths + [p for p in tree_lib.record_paths(tracked, conf["MEMORY_ROOT"]) if not p.endswith(".md")]:
        try:
            text = tree_lib.read_text(os.path.join(str(root), p))
        except (OSError, UnicodeDecodeError):
            continue
        if p.endswith(".md") or read_serves_prefix(text):
            texts[p] = text
    try:
        rows = {r.get("name"): r for r in record_kinds.read_record_kinds(root) or []}
    except record_kinds.RecordKindsError as exc:
        raise ValueError(str(exc)) from None
    legacy, note = read_legacy_paths(root)
    return {"root": root, "conf": conf, "tracked": tracked, "texts": texts, "rows": rows, "legacy": legacy,
            "note": note, "bindings": tree_lib.read_bindings(str(root), list(texts), conf),
            "keys": read_record_keys(root, [p for p in texts if p.endswith(".md")]), "ids": read_defined_ids(root) if legacy is not None else set(),
            "value": read_anchor_value(root),
            "pinned": {p for paths in read_pinned_records(root, pinned if legacy is not None else ()).values()
                       for p in paths}}


def derive_record_cause(g, path) -> tuple:
    """`(how, targets, finding)` of one record: `how` `root`, `serves` (a legacy record, or a typed kind
    declaring no `Caused-by`, graded on its Serves units; or, TOOL-dTotalRecall-50 S3, a record a standing
    pinned row's glob reads that carries no `Caused-by`, graded on its first Serves id alone) or `caused-by`;
    `finding` its header's refusal."""
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
    targets = [t for e in edges if e["type"] == "caused-by" for t in e["targets"]]
    if not targets and path in g.get("pinned", ()):   # S3: the interim read, while its writer's row stands
        return "serves", list(binding.get("ids") or [])[:1], None
    return "caused-by", targets, None


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
                                                       else ABSENT_CAUSE))
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


def read_build_code_paths(root) -> tuple:
    """`(build glob, paths)`: every tracked `*.py`, `*.sh` and `*.js` file under `<memory root>/builds/*/build/`
    (TOOL-dTotalRecall-50 S1), each glob through `record_kinds.read_tracked`, test-named files excepted, sorted.
    ValueError where git refuses."""
    import record_kinds   # noqa: E402  the memory root and the tracked-glob walk
    folder = f"{record_kinds.read_memory_root(root)}/builds/*/build"
    try:
        paths = {p for ext in ("py", "sh", "js") for p in record_kinds.read_tracked(root, f"{folder}/*.{ext}")}
    except record_kinds.RecordKindsError as exc:
        raise ValueError(str(exc)) from None
    return folder, sorted(p for p in paths if not CAUSE_WRITER_TEST_RE.search(p))


def check_ask_filed(root, ask_id) -> str | None:
    """Why `ask_id` is no filed ask, or None where it is one (TOOL-dTotalRecall-50 S2): an ask
    `backlog.parse_file` reads in the `BACKLOG.md` of the build `id_grammar.parse_id_parts` names in the id,
    under the grammar of the conf's FAMILIES. Its liveness past being filed is not read."""
    import backlog   # noqa: E402  the backlog's one parser
    import record_kinds   # noqa: E402  the memory root
    from id_grammar import parse_id_parts   # noqa: E402  the id's build
    try:
        _family, slug, _seq = parse_id_parts(ask_id, root)
    except ValueError as exc:
        return str(exc)
    rel = f"{record_kinds.read_memory_root(root)}/builds/{slug}/BACKLOG.md"
    try:
        text = pathlib.Path(root, rel).read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return f"{rel} does not read: {exc}"
    families = [p.split(":", 1)[1] for p in (read_conf(root).get("FAMILIES") or "").split() if ":" in p]
    try:
        parsed = backlog.parse_file(rel, text, backlog.build_grammar(families))
    except backlog.Problem as exc:
        return f"the conf's FAMILIES do not compile: {exc}"
    return None if any(a.id == ask_id for a in parsed.asks) else f"{rel} files no ask {ask_id}"


def check_cause_writers(root, pinned=CAUSE_WRITER_PINNED) -> tuple:
    """S7's writer census: `(lines, reds)` over the alias census's population, every tracked `*.py`, `*.sh`
    and `*.js` file under the tool root (`record_kinds.read_code_paths`), test-named files excepted. A census
    file spells a `**Serves:** ` literal and no `Caused-by`, and is red unless `CAUSE_WRITER_KEPT` keys it by
    its path under the tool root, then printed `kept <reason>`; one line per census file at its first Serves
    literal, then a count line. It grades spelling, never whether the file writes the line at run time.
    A file kept for `KEPT_INSTRUMENT` (TOOL-dTotalRecall-49 S3) is red, named with why, where the design keys
    read off or refuse, or where the record `DESIGN_VIEW` names has no `-` row of the legacy population.
    TOOL-dTotalRecall-50 S1 S2: then the build folders' code files (`read_build_code_paths`), both tests read
    past each file's `BIND_HEAD_LINES` binding window, each census file kept by its repository path or the
    instrument of a `pinned` row; each row is printed with its ask id and the records its glob reads, and is
    red where its instrument is untracked or spells `Caused-by` past the window, or its ask is not filed;
    then the build folders' own count line."""
    import record_kinds   # noqa: E402  the tool root and the code census's one walk
    tool_rel = record_kinds.derive_tool_rel(record_kinds.derive_kit_rel())
    try:
        paths = [p for p in record_kinds.read_code_paths(root, tool_rel) if not CAUSE_WRITER_TEST_RE.search(p)]
    except record_kinds.RecordKindsError as exc:
        raise ValueError(str(exc)) from None
    folder, build_paths = read_build_code_paths(root)
    records = read_pinned_records(root, pinned)
    lines, reds, kept = [], [], 0
    for path in paths:
        text = pathlib.Path(root, path).read_bytes().decode("utf-8", "replace")
        if SERVES_LITERAL not in text or CAUSE_LITERAL in text:
            continue
        n = next(i for i, ln in enumerate(text.splitlines(), 1) if SERVES_LITERAL in ln)
        key = path[len(tool_rel) + 1:] if tool_rel else path
        if key in CAUSE_WRITER_KEPT:
            reason, why = CAUSE_WRITER_KEPT[key], None
            if reason == KEPT_INSTRUMENT:   # TOOL-dTotalRecall-49 S3: the reason holds over a legacy view only
                from design_lib import DesignRefusal, read_design_conf, read_design_keys   # noqa: E402  the keys' one reader
                try:
                    design = read_design_keys(root, read_design_conf(root))
                    why = None if design else "the design keys are off, so DESIGN_VIEW names no record"
                except DesignRefusal as exc:
                    design, why = None, f"the design keys refuse: {exc}"
                if design:
                    legacy, note = read_legacy_paths(root)
                    if design["DESIGN_VIEW"] not in (legacy or ()):
                        why = (f"DESIGN_VIEW {design['DESIGN_VIEW']} has no `<path> -` row of {POPULATION}"
                               + ("" if legacy else f" ({note})"))
            if why is None:
                kept += 1
                lines.append(f"cause-writer · {path}:{n} · kept {reason}")
                continue
            lines.append(f"cause-writer · {path}:{n} · red · kept {reason}, but {why}")
            reds.append(f"cause-writer {path}:{n}: kept because it {reason}, but {why}; restore the record's "
                        f"legacy row or write the cause line under its Serves line")
            continue
        lines.append(f"cause-writer · {path}:{n} · red")
        reds.append(f"cause-writer {path}:{n}: spells a Serves line and no Caused-by; write the cause line under "
                    f"its Serves line, or key the file in CAUSE_WRITER_KEPT with its reason")
    lines.append(f"cause-writer · {len(paths)} code files under {tool_rel or '.'} · {kept + len(reds)} census "
                 f"file(s) · {kept} kept · {len(reds)} red")
    rows = {}   # S2: {instrument: (ask id, glob, why red or None)}
    for instrument, glob, ask in pinned:
        try:
            tracked = record_kinds.read_tracked(root, instrument)
        except record_kinds.RecordKindsError as exc:
            raise ValueError(str(exc)) from None
        if not tracked:
            why = "is not tracked, so the row pins nothing: drain the row"
        elif CAUSE_LITERAL in "\n".join(pathlib.Path(root, instrument).read_bytes().decode("utf-8", "replace")
                                        .splitlines()[tree_lib.BIND_HEAD_LINES:]):
            why = (f"spells {CAUSE_LITERAL} past its binding window, so the records it writes carry their cause: "
                   "drain the row")
        else:
            why = check_ask_filed(root, ask)
            why = why and f"names ask {ask}, which is not a filed ask: {why}"
        rows[instrument] = (ask, glob, why)
        state = f"red · {why}" if why else "filed"
        lines.append(f"cause-writer · pinned · {instrument} · ask {ask} · {state} · {glob} reads "
                     f"{len(records[glob])} record(s)")
        if why:
            reds.append(f"cause-writer CAUSE_WRITER_PINNED {instrument} (ask {ask}): {why}")
    b_kept = b_pinned = b_red = 0
    for path in build_paths:
        body = pathlib.Path(root, path).read_bytes().decode("utf-8", "replace").splitlines()
        past = body[tree_lib.BIND_HEAD_LINES:]
        if not any(SERVES_LITERAL in ln for ln in past) or any(CAUSE_LITERAL in ln for ln in past):
            continue
        n = next(i for i, ln in enumerate(past, tree_lib.BIND_HEAD_LINES + 1) if SERVES_LITERAL in ln)
        if path in rows:
            b_pinned += 1
            lines.append(f"cause-writer · {path}:{n} · pinned CAUSE_WRITER_PINNED · ask {rows[path][0]}")
        elif path in CAUSE_WRITER_KEPT:
            b_kept += 1
            lines.append(f"cause-writer · {path}:{n} · kept {CAUSE_WRITER_KEPT[path]}")
        else:
            b_red += 1
            lines.append(f"cause-writer · {path}:{n} · red")
            reds.append(f"cause-writer {path}:{n}: spells a Serves line past its binding window and no Caused-by; "
                        f"write the cause line under its Serves line, key the file in CAUSE_WRITER_KEPT with its "
                        f"reason, or declare its CAUSE_WRITER_PINNED row")
    lines.append(f"cause-writer · {len(build_paths)} code files under {folder} · {b_kept + b_pinned + b_red} census "
                 f"file(s) · {b_kept} kept · {b_pinned} pinned · {b_red} red")
    return lines, reds


def run_check(root, pinned=CAUSE_WRITER_PINNED) -> tuple:
    """`--check`: `(lines, exit)`, `pinned` the pinned-writer rows read (TOOL-dTotalRecall-50 S2 S3), a
    fixture's own where it plants one; an unarmed tree reads none."""
    try:
        g = read_grading(root, pinned)
    except ValueError as exc:
        return [f"{SAY}: refused · {exc}"], 2
    if g["legacy"] is None:
        return [f"{SAY}: unarmed · {g['note']}"], 0
    causes, orphans = check_causes(root, g), check_orphans(root, g)
    try:
        writer_lines, writer_reds = check_cause_writers(root, pinned)
    except ValueError as exc:
        return [f"{SAY}: refused · {exc}"], 2
    script = sum(1 for p in g["texts"] if not p.endswith(".md"))
    lines = [f"{SAY}: {POPULATION} · {g['note']} · memory.legacy-anchors {g['value']}",
             f"{SAY}: {len(g['texts']) - script} Markdown record(s) · {script} comment-headed · "
             f"{len(g['legacy'] & set(g['texts']))} legacy"]
    lines += causes + orphans
    lines += [f"{SAY}: {ln}" for ln in writer_lines] + [f"{SAY}: RED {r}" for r in writer_reds]
    lines.append(f"{SAY}: {len(causes)} causeless · {len(orphans)} orphan(s)")
    red = bool(causes or orphans or writer_reds)
    lines.append(f"{SAY}: {'RED' if red else 'green'}")
    return lines, 1 if red else 0


def write_missing_causes(root) -> tuple:
    """`--backfill` (TOOL-dTotalRecall-47 S1 S2): `(lines, exit)`. Writes `**Caused-by:** <first Serves id>`
    under the first Serves line of each record the causes check names with `ABSENT_CAUSE`, in the file's own
    line ending, and lists each record S2 refuses under `not backfilled` with its reason, byte-identical."""
    import build_records   # noqa: E402  the typed kinds' name grammar
    try:
        g = read_grading(root)
    except ValueError as exc:
        return [f"{SAY}: refused · {exc}"], 2
    if g["legacy"] is None:
        return [f"{SAY}: unarmed · {g['note']}", f"{SAY}: 0 backfilled · 0 not backfilled"], 0

    def derive_backfill_refusal(path):
        """`(reason, Serves line number, target)` of one selected record, `reason` None where S2 admits it."""
        if not path.endswith(".md"):
            return "not markdown: its cause line wears its Serves line's comment prefix", 0, None
        if any(build_records.derive_record_name(k).search(path) for k in tree_lib.TYPED_RECORD_KINDS):
            return "typed kind: its cause is a `- **Caused-by:**` field its kind's writer writes", 0, None
        ids = (g["bindings"].get(path) or {}).get("ids") or []
        head = [(n, ln) for n, ln in tree_lib.unfenced_lines(g["texts"][path]) if ln is not None]
        at = next((i for i, (_n, ln) in enumerate(head[:tree_lib.BIND_HEAD_LINES])
                   if (mo := tree_lib.BIND_RE.match(ln)) and mo.group("key") == "Serves"
                   and mo.group("rest").split("<!--", 1)[0].strip()), None)
        if not ids or at is None:
            return "no id: its Serves line names no unit", 0, None
        if at == tree_lib.BIND_HEAD_LINES - 1:
            return (f"head window: its Serves line is unfenced line {tree_lib.BIND_HEAD_LINES}, the head's last, "
                    "so a cause line under it would not be read"), 0, None
        return None, head[at][0], ids[0]

    lines, written, refused = [], 0, 0
    for finding in check_causes(root, g):
        _rule, path, why = finding.split(" · ", 2)
        if why != ABSENT_CAUSE:
            continue
        reason, n, target = derive_backfill_refusal(path)
        if reason:
            refused += 1
            lines.append(f"{SAY}: not backfilled · {path} · {reason}")
            continue
        file = pathlib.Path(root, path)
        raw = file.read_bytes().decode("utf-8")
        eol, parts, cause = "\r\n" if "\r\n" in raw else "\n", raw.split("\n"), f"**Caused-by:** {target}"
        if n < len(parts):   # a line follows the Serves line: the cause goes between, ended as the file ends lines
            parts.insert(n, cause + eol[:-1])
            raw = "\n".join(parts)
        else:   # the Serves line ends the file unterminated, and so does the cause line after it
            raw += eol + cause
        file.write_bytes(raw.encode("utf-8"))
        written += 1
        lines.append(f"{SAY}: backfilled · {path} · Caused-by {target}")
    lines.append(f"{SAY}: {written} backfilled · {refused} not backfilled")
    return lines, 0


# ------------------------------------------------------------------------------------------ the fixture
FIXTURE_UNIT = "TOOL-fRoot-1"
FIXTURE_CLAIM = "TOOL-fClaim-1"
#: TOOL-dTotalRecall-50 AC2 AC3: the pinned plants, their instrument, its row and the ask the row names, filed
#: in fRoot's BACKLOG.md; the drained plant's instrument spells the cause past its binding window
PINNED_PLANTS = ("pinned-writer-drained", "departures-pinned")
PINNED_INSTRUMENT = f"memory/builds/fRoot/build/2026-01-01-build-{FIXTURE_UNIT}-deviations.py"
PINNED_ASK = "TOOL-fRoot-2"
FIXTURE_PINNED = ((PINNED_INSTRUMENT, DEPARTURES_GLOB, PINNED_ASK),)
PINNED_RECORD = f"memory/builds/fRoot/build/2026-01-02-build-{FIXTURE_UNIT}-departures-build.md"
PINNED_BACKLOG = "memory/builds/fRoot/BACKLOG.md"


def render_pinned_instrument(drained) -> str:
    """The pinned plants' instrument: a comment head naming its cause, padded to its binding window, then
    the record head it writes, and where `drained` the cause line it now writes too."""
    head = f"# **Serves:** research {FIXTURE_UNIT}\n# **Caused-by:** {FIXTURE_UNIT}\n"
    head += "# a line of the head\n" * (tree_lib.BIND_HEAD_LINES - 2)
    body = f'HEAD = "{SERVES_LITERAL}journal {{first}}"\n'
    return head + body + (f'CAUSE = "**{CAUSE_LITERAL}:** {{first}}"\n' if drained else "")


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
    if plant in BULLETED_PLANTS or plant == "backfill-refusals":   # a typed kind whose fields hold `Caused-by`
        rows["deviation"] = ("memory/builds/*/build/*-build-*-deviation-*.md", '["Serves", "Caused-by"]')
    roots = set()
    if plant == "backfill-selection":   # TOOL-dTotalRecall-47 AC1: a kind the registry marks root
        rows["spec-audit"] = ("memory/builds/*/reviews/*.md", '["Serves"]')
        roots.add("spec-audit")
    conf = 'MEMORY_ROOT="memory"\nFAMILIES="tooling:TOOL"\n'
    write_file(".memory-tree.conf", conf)
    write_file(f"{kit_rel}/{record_kinds.REGISTRY}", "".join(
        f'[[record-kind]]\nname = "{n}"\nhome = "{h}"\nschema = {{ form = "fields", fields = {f} }}\n'
        + ("root = true\n" if n in roots else "") + "\n" for n, (h, f) in rows.items()))
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
    build = "memory/builds/fRoot/build"
    view = f"{build}/2026-01-01-build-{FIXTURE_UNIT}-as-built.md"
    if plant == "kept-instrument-not-legacy":   # TOOL-dTotalRecall-49 S3: the view, in the legacy tree and caused
        write_file(view, f"# As built\n\n**Serves:** research {FIXTURE_UNIT}\n**Caused-by:** {FIXTURE_UNIT}\n")
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
    elif plant in BULLETED_PLANTS:   # TOOL-dTotalRecall-39: a rooted build's typed record, its cause bulleted
        write_file("memory/builds/tFix/README.md", f"---\nslug: tFix\nopened: 2026-01-01\nids: {BULLETED_UNIT}\n---\n\n# tFix\n")
        write_file(f"memory/builds/tFix/spec/2026-01-01-spec-{BULLETED_UNIT}.md",
                   f"# {BULLETED_UNIT} — the fixture's unit\n\n**Status:** OPEN · rev-1 · 2026-01-01 · node a · Tier-1 · base 00000000\n")
        write_file(BULLETED_RECORD, BULLETED_HEAD + f"- **Caused-by:** {BULLETED_UNIT}\n" * BULLETED_PLANTS[plant])
    elif plant in SCRIPT_PLANTS:   # TOOL-dTotalRecall-51 AC1 to AC3: non-Markdown records, their heads comments
        for name, text in SCRIPT_PLANTS[plant].items():
            write_file(f"{build}/2026-01-02-build-{FIXTURE_UNIT}-{name}", text.format(unit=FIXTURE_UNIT))
    elif plant in BACKFILL_PLANTS:   # TOOL-dTotalRecall-47 AC1 AC3: what the backfill selects and refuses
        for rel, text in BACKFILL_PLANTS[plant].items():
            write_file(rel.format(build=build, unit=FIXTURE_UNIT), text.format(unit=FIXTURE_UNIT))
    elif plant in PINNED_PLANTS:   # TOOL-dTotalRecall-50 AC2 AC3: a pinned instrument, its filed ask, a record
        import backlog   # noqa: E402  the ask door's row renderers
        from gov_record import render_backlog_text   # noqa: E402  the ask door's file layout
        write_file(PINNED_INSTRUMENT, render_pinned_instrument(plant == "pinned-writer-drained"))
        write_file(PINNED_BACKLOG, render_backlog_text(
            None, "fRoot", backlog.render_ask_row(PINNED_ASK, "2026-01-02", "THE PLANTED INSTRUMENT WRITES NO CAUSE.",
                                                  clauses=[("accept", "its records carry the line")]),
            backlog.render_sev_row(PINNED_ASK, "LOW", "its records read their cause from their Serves unit")))
        if plant == "departures-pinned":
            write_file(PINNED_RECORD, f"# Departures: fRoot, its build run\n\n**Serves:** journal {FIXTURE_UNIT}\n")
    elif plant == "claim-root":
        write_file(f"memory/builds/fClaim/build/2026-01-02-build-{FIXTURE_CLAIM}-claimed.md",
                   f"# Claimed\n\n**Serves:** research {FIXTURE_CLAIM}\n**Made-by:** owner\n**Caused-by:** {FIXTURE_CLAIM}\n")
    else:   # legacy, none and the writer plant: a new record caused by a unit, beside the legacy tree
        write_file(f"{build}/2026-01-02-build-{FIXTURE_UNIT}-caused.md",
                   f"# Caused\n\n**Serves:** research {FIXTURE_UNIT}\n**Made-by:** owner\n**Caused-by:** {FIXTURE_UNIT}\n")
    if plant == "writer-without-cause":   # TOOL-dTotalRecall-36 S7: a code file spelling a Serves literal, no cause
        write_file(f"{tool_rel}/{CAUSE_WRITER_PLANT}" if tool_rel else CAUSE_WRITER_PLANT,
                   f'"""A record writer."""\nHEAD = "{SERVES_LITERAL}log {FIXTURE_UNIT}\\n"\n')
    if plant == "kept-instrument-not-legacy":   # the four design keys set over the view, its `-` row cut
        pin = run_git(root, "rev-parse", "HEAD").stdout.strip()
        home = root / reg.home
        home.write_bytes("".join(ln for ln in home.read_bytes().decode("utf-8").splitlines(True)
                                 if not ln.startswith(f"{view}\t{LEGACY_SECTION}\t")).encode("utf-8"))
        write_file(".memory-tree.conf", conf + f'DESIGN_RECORD="{build}/2026-01-01-build-{FIXTURE_UNIT}-notes.md"\n'
                   f'DESIGN_BASELINE="{pin}"\nDESIGN_VIEW="{view}"\nDESIGN_NODES="{build}/map.py"\n')
        write_file(f"{tool_rel}/{KEPT_INSTRUMENT_KEY}" if tool_rel else KEPT_INSTRUMENT_KEY,
                   f'"""A view renderer."""\nHEAD = "{SERVES_LITERAL}research {FIXTURE_UNIT}\\n"\n')
    run_commit(f"record-causes fixture: {plant}")
    if plant == "claim-root":
        p = run_git(root, "update-ref", f"{CLAIM_NS}fClaim", run_git(root, "rev-parse", "HEAD").stdout.strip())
        if p.returncode:
            raise ValueError(f"the fixture's claim ref refused: {p.stderr.strip()}")
    return root


def check_plant_walk(root, plant, lines, rc) -> tuple:
    """TOOL-dTotalRecall-39 AC2 AC3: the playbook kit's edge walk, `read_tree_edges`, over a bulleted plant's
    `root`, beside the causes check's `lines` and exit `rc`. -> `(walk lines, ok)`: the walk's `caused-by`
    edges and refusals of BULLETED_RECORD, then one PASS or FAIL line. One field passes when the causes check
    is green and the walk reads the one edge to BULLETED_UNIT and refuses nothing; two pass when the walk
    reads no edge of the record and refuses it once naming both lines, and the causes check names it refused."""
    import gen_build_index   # noqa: E402  the route to the playbook kit's edge grammar
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    try:
        eg = gen_build_index.load_edge_grammar(resolve_kit_dir("playbook", "edge_grammar.py", KIT))
    except LookupError as exc:
        raise ValueError(f"the edge grammar does not resolve: {exc}") from None
    edges, bad = eg.read_tree_edges(pathlib.Path(root), None)
    mine = [t for e in edges if e["path"] == BULLETED_RECORD and e["type"] == "caused-by" for t in e["targets"]]
    refused = [r for r in bad if BULLETED_RECORD in r]
    out = [f"{SAY}: fixture {plant} · walk · caused-by {BULLETED_RECORD} -> {t}" for t in mine]
    out += [f"{SAY}: fixture {plant} · walk · refused · {r}" for r in bad]
    first = BULLETED_HEAD.count("\n") + 1
    if BULLETED_PLANTS[plant] == 1:
        ok = rc == 0 and mine == [BULLETED_UNIT] and not bad
    else:
        named = [ln for ln in lines if BULLETED_RECORD in ln and "its header is refused" in ln]
        ok = not mine and len(bad) == 1 and len(refused) == 1 and f"lines {first} and {first + 1}" in refused[0] \
            and len(named) == 1
    out.append(f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · both checks read {BULLETED_RECORD}")
    return out, ok


def check_backfill_plant(root, plant) -> tuple:
    """TOOL-dTotalRecall-47 AC1 AC3: `--backfill` over a backfill plant's `root`, then, for the selection
    plant, `--check` and `--backfill` again. -> `(lines, ok)`: each run's lines, then one PASS or FAIL line.
    It passes when the first run writes exactly BACKFILL_EXPECTED's paths and lists exactly its refusals,
    each under its reason, `git status --porcelain` names only what it wrote, and, for the selection plant,
    the check names exactly the refused records under `causes` and the second run prints `0 backfilled`."""
    build = "memory/builds/fRoot/build"
    want, wrote = BACKFILL_EXPECTED[plant]
    want = {k.format(build=build, unit=FIXTURE_UNIT): v for k, v in want.items()}
    wrote = [p.format(build=build, unit=FIXTURE_UNIT) for p in wrote]
    first, _rc = write_missing_causes(root)
    out = [f"{SAY}: fixture {plant} · backfill 1 · {ln}" for ln in first]
    refused = {ln.split(" · ")[1]: ln.split(" · ")[2] for ln in first if ln.startswith(f"{SAY}: not backfilled · ")}
    done = [ln.split(" · ")[1] for ln in first if ln.startswith(f"{SAY}: backfilled · ")]
    status = sorted(ln[3:] for ln in run_git(root, "status", "--porcelain").stdout.splitlines())
    out += [f"{SAY}: fixture {plant} · status · {ln}" for ln in status]
    ok = done == wrote and status == sorted(wrote) and set(refused) == set(want) \
        and all(refused[p].startswith(r) for p, r in want.items())
    if plant == "backfill-selection":
        lines, _rc = run_check(root, ())
        second, _rc = write_missing_causes(root)
        out += [f"{SAY}: fixture {plant} · check · {ln}" for ln in lines]
        out += [f"{SAY}: fixture {plant} · backfill 2 · {ln}" for ln in second]
        named = {ln.split(" · ")[1] for ln in lines if ln.startswith(f"{SAY}: causes · ")}
        ok = ok and named == set(want) and second[-1].startswith(f"{SAY}: 0 backfilled")
    out.append(f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · the backfill writes what the causes check "
               "lacks and refuses to guess")
    return out, ok


def check_pinned_plant(root, plant) -> tuple:
    """TOOL-dTotalRecall-50 AC2 AC3: `--check` twice over a pinned plant's `root`. -> `(lines, ok)`: each
    run's lines and exit, then one PASS or FAIL line. The drained plant passes when the first run exits 1
    naming the row drained, and the second, its instrument written causeless and its ask row deleted from
    PINNED_BACKLOG, exits 1 naming the ask not filed and the row not drained. The departures plant passes
    when the first run, under FIXTURE_PINNED, exits 0, and the second, the row cut, exits 1 naming
    PINNED_RECORD under causes."""
    first, rc1 = run_check(root, FIXTURE_PINNED)
    if plant == "pinned-writer-drained":
        pathlib.Path(root, PINNED_INSTRUMENT).write_bytes(render_pinned_instrument(False).encode("utf-8"))
        backlog = pathlib.Path(root, PINNED_BACKLOG)
        backlog.write_bytes("".join(ln for ln in backlog.read_bytes().decode("utf-8").splitlines(True)
                                    if not ln.startswith(f"- {PINNED_ASK} ")).encode("utf-8"))
        second, rc2 = run_check(root, FIXTURE_PINNED)
        row = f"CAUSE_WRITER_PINNED {PINNED_INSTRUMENT} (ask {PINNED_ASK}): "
        drained = [ln for ln in first if row in ln and f"spells {CAUSE_LITERAL} past" in ln]
        unfiled = [ln for ln in second if row in ln and f"{PINNED_ASK}, which is not a filed ask" in ln]
        ok = rc1 == 1 and rc2 == 1 and len(drained) == 1 and len(unfiled) == 1 \
            and not any(row in ln and f"spells {CAUSE_LITERAL} past" in ln for ln in second)
    else:
        second, rc2 = run_check(root, ())
        named = [ln for ln in second if ln.startswith(f"{SAY}: causes · {PINNED_RECORD} · ")]
        ok = rc1 == 0 and rc2 == 1 and len(named) == 1
    out = [f"{SAY}: fixture {plant} · check {n} · {ln}" for n, run in ((1, first), (2, second)) for ln in run]
    out += [f"{SAY}: fixture {plant} · check 1 exit {rc1} · check 2 exit {rc2}",
            f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · a pinned writer's row stands until it drains "
            "or its ask is unfiled, and reads its records' cause from their Serves unit while it stands"]
    return out, ok


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
            if plant in BACKFILL_PLANTS:
                lines, ok = check_backfill_plant(root, plant)
                return head + lines, 0 if ok else 1
            if plant in PINNED_PLANTS:
                lines, ok = check_pinned_plant(root, plant)
                return head + lines, 0 if ok else 1
            lines, rc = run_check(root, ())
            if plant in BULLETED_PLANTS:
                walk, ok = check_plant_walk(root, plant, lines, rc)
                return head + lines + walk, 0 if ok else 1
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
    elif argv == ["--backfill"]:
        lines, rc = write_missing_causes(root)
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
