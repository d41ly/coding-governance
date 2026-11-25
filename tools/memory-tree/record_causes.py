#!/usr/bin/env python3
"""record_causes.py — every record names its cause (TOOL-dTotalRecall-19).

    python <prefix>/memory-tree/record_causes.py --check               # the causes and orphan checks
    python <prefix>/memory-tree/record_causes.py --measure             # the legacy population's causes rows
    python <prefix>/memory-tree/record_causes.py --print-stand-ins     # the made-by-stand-in class's members
    python <prefix>/memory-tree/record_causes.py --print-record-keys   # the record-key class's members
    python <prefix>/memory-tree/record_causes.py --backfill            # write the cause line the causes check lacks
    python <prefix>/memory-tree/record_causes.py --backfill --build <slug>   # write it in one build's records alone
    python <prefix>/memory-tree/record_causes.py --cause-writers       # the writer census's lines alone
    python <prefix>/memory-tree/record_causes.py --fixture --plant <case>

A record's header names what made it and why it exists: `**Made-by:**` and `**Caused-by:**` after its
`**Serves:**` line, or a typed kind's `- **Made-by:**` and `- **Caused-by:**` fields, read by
`tree_lib.read_header_edges`. The record door writes both (`gov_record.py new <kind> --caused-by <target>`).

THE GRADED SET (`read_grading`, TOOL-dTotalRecall-51 S3). The Markdown members of `tree_lib.record_paths`,
and each non-Markdown member whose first Serves line wears a comment prefix (`tree_lib.BIND_RE`'s `prefix`),
whose cause line wears the same prefix. A non-Markdown record whose Serves line is bare, or that has none, is
not graded, and record keys stay Markdown stems.

THE CAUSES CHECK (`check_causes`). A graded record with no `<path> -` row of the `record-kinds-legacy`
population's `causes` slice, whose kind's `record-kinds.toml` row is not `root = true`, is red when it
carries no `Caused-by` or one that does not resolve: a target resolves when it is a family id the corpus defines
(`corpus_ids.py`'s defined-id set) or a record key, the stem of a tracked Markdown record. A record of a
typed kind whose row's `schema.fields` hold no `Caused-by`, written by its parent's own command, is graded
on its Serves units instead, each of which must resolve. A legacy record is never red.

THE ORPHAN CHECK (`check_orphans`). The roots are each build whose `README.md` is tracked, and each whose
claim `refs/gov/claims/<slug>` of the remote this clone's cache holds, at `refs/gov/remote/claims/<slug>`
(`gen_build_index.CLAIM_CACHE_NS`, TOOL-dTotalRecall-119). A unit id is reached when its README's `ids:`
names it, or, for a claim-rooted build, when its slug is the claim's; a record is reached when its cause
is, its `Caused-by` target or, for a legacy record, its Serves units, the walk a fixed point from the
roots outward, so two new records caused by each other are reached by neither and both are orphans. A
new record no root reaches is red.

THE WRITER CENSUS (`check_cause_writers`, TOOL-dTotalRecall-36 S7). Every tracked `*.py`, `*.sh` or `*.js`
file under the tool root, the alias census's walk (`record_kinds.read_code_paths`), test-named files
excepted, graded by line (TOOL-dTotalRecall-53 S9): a line spelling a `**Serves:** ` literal with no
`Caused-by` on it or the three lines below it is red unless the census marker on its line,
`# census: kept cause-writer <reason>` (`//` in JavaScript, `id_grammar.read_kept_reason`,
TOOL-dTotalRecall-53 S34), keeps it, so the next writer that omits the cause line is red at its own pass,
before the record it writes is, even in a file that answers its other literals. `--cause-writers` prints the
census's lines alone, each open literal with its disposition. A literal kept as rendering a pinned
instrument's bytes (`KEPT_INSTRUMENT`, TOOL-dTotalRecall-49 S3) is red where that stops being true: where
`design_lib.read_design_keys` reads the design keys off or refuses them, or where the record `DESIGN_VIEW`
names has no `<path> -` row of the `record-kinds-legacy` population's `causes` slice. That reason is the
renderer's alone, `KEPT_INSTRUMENT_KEY` under the tool root: a marker or a `census-kept-paths.txt` row giving it on
any other file is red naming the file (TOOL-dTotalRecall-60 S26). Then the build
folders' scripts (TOOL-dTotalRecall-50 S1), every tracked
`*.py`, `*.sh` or `*.js` file under `<memory root>/builds/*/build/`, test-named files excepted, read past their `BIND_HEAD_LINES`
binding window by both tests, so a file's own binding is never a hit; each census file is the instrument of
a pinned row or is kept by a plain path-keyed row of the project registry
`census-kept-paths.txt` (`tree_lib.read_kept_rows`, TOOL-dTotalRecall-65 S2), held outside its bytes
because no pass may edit it, and its count line counts them apart. A line of any of those files carrying the `cause-writer` census marker is red by line, whatever keeps
the file, outside that count line's reds (`id_grammar.check_marker_domain`, TOOL-dTotalRecall-58 S1). A row
cannot outlive its hit (S4, TOOL-dTotalRecall-66 S1): a row whose file the build-folder walk lists as no hit,
because the file is not walked, spells `Caused-by` past its binding window or spells no Serves literal there, is
red, named `census-kept-paths.txt` and its path: drain the row. A row may name only a build folder's file
(`tree_lib.build_kept_path_re`, TOOL-dTotalRecall-66 S11 S13): a registry
holding any other row, a malformed one, one of an unknown census or a second row for one census and path
(TOOL-dTotalRecall-70 S11) is red naming it, an editable file being kept by its census marker,
and the walk then reads every hit unkept; an absent registry holds no rows. Last come the registry's homes
(`check_kept_home`, TOOL-dTotalRecall-73 S3): the one the censuses read, under the conf's memory root, and each
one a ledger registration names, red where the two are not one path. A memory root naming no directory inside
the tree (`tree_lib.resolve_memory_root`, TOOL-dTotalRecall-87) is one red naming `MEMORY_ROOT`, and the home is
then read nowhere.

THE PINNED WRITERS (`read_pinned_rows`, TOOL-dTotalRecall-50 S2 S3, TOOL-dTotalRecall-66 S36). One
`check_cause_writers` row of `census-kept-paths.txt` per pinned instrument that writes a record with no cause,
whose owner alone moves its pin: its `records` field the glob of the records it writes, its disposition
`keep:<ask id>`, the filed ask asking that owner for the line. `--check` prints
each row with its ask id and the records its glob reads, red where the instrument is untracked, spells
`Caused-by` past its binding window (drain the row), its disposition names no ask, or its ask is no ask `backlog.parse_file` reads in the
`BACKLOG.md` of the build its id names, or is not live in the fold at HEAD (`check_ask_live`,
TOOL-dTotalRecall-60 S19). While a row stands, a new record its glob reads that carries no
`Caused-by` is read as caused by its first Serves id, by the causes and orphan checks alike.

THE LEGACY POPULATION. `record-kinds-legacy`, keyed by path, section and check (TOOL-dTotalRecall-52);
this check reads its `causes` slice alone (`read_legacy_paths`), and `record_kinds.py` its `kind-schema`
slice. `--measure` prints one TAB row `<path> - causes 1` per tracked Markdown record and, under
`memory.legacy-anchors` `derived`, one `<path> <anchor> causes 1` row per untagged `##` or `###` heading,
its anchor the playbook kit's `derive_anchor`: the `causes` slice the population's one seed,
`record_kinds.py --seed-legacy`, prints beside its `kind-schema` slice, and `legacy_ledger.py seed
--population record-kinds-legacy` writes both to the population's home. `read_legacy_anchors` is the one
reader of the key: `derived` (the default) derives anchors for untagged headings and reads a legacy record's Serves lines as its cause; `none`
derives none and reads a legacy record as reached; `retag` reads the authored tags alone,
`## [section.<anchor>] <heading>`, the form TOOL-dTotalRecall-20's retag step writes.

Exit: 0 green or unarmed (no registration, an absent or unarmed home, an empty population), 1 a red, 2 a
refused read, `memory.legacy-anchors` named. `--print-*` exit 3 where the class has no member here.
WHAT IT DOES NOT CHECK: a non-Markdown record whose head is not a comment; whether a `Made-by`
names who really wrote it; the edge grammar of a header's targets, which `edge_grammar.py --check` grades;
whether a census file that spells `Caused-by` writes the line at run time, since the census grades spelling;
whether a census marker's lead opens a comment in its line's language, or still sits on an open literal;
whether a pinned row's glob names the records its instrument really writes; its ask's liveness past HEAD;
whether the keep registry is registered at all, under which fields, or stands at either home; a claim this
clone's cache does not hold, since the orphan check fetches nothing: a clone that fetched no claim has no claim
root.

THE BACKFILL (`write_missing_causes`, TOOL-dTotalRecall-47). `--backfill` keeps the causes check's findings
whose rule is the absent cause (`ABSENT_CAUSE`), so it selects what the check reds and never a copy of the
selection, and writes `**Caused-by:** <first Serves id>` on the line after the record's first Serves line,
behind the lead that line wears (TOOL-dTotalRecall-60 S20: `# ` in a script), in the file's own line ending,
printing each path it wrote and a count. It refuses to guess, listing under `not backfilled` with its reason
and leaving byte-identical: one a typed kind's name grammar matches (its cause is a `- **Caused-by:**` field
its kind's writer writes), one whose Serves line names no id, and one whose Serves line is the last line of
the head window, where a cause line would fall outside what `read_header_edges` reads; and, under `--build
<slug>` (TOOL-dTotalRecall-60 S13), one outside that build's folder, `another build's record`. A `--build` value
that is no build slug whole, or names no tracked build README, is refused naming it, exit 2, nothing written
(TOOL-dTotalRecall-66 S25). A second run writes nothing. Exit 0, a refused read 2.
"""
from __future__ import annotations

import itertools
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
POPULATION = "record-kinds-legacy"
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
          "departures-pinned", "literal-without-cause", "duplicate-cause", "unmarked-writer", "kept-row-drained",
          "kept-row-editable", "marker-in-build-script", "other-build-causeless", "pinned-ask-closed",
          "reason-on-other-file", "adopter-no-registry", "kept-row-caused", "kept-row-untracked",
          "kept-row-traversal", "kept-row-nested", "kept-row-docs-root", "pinned-ask-is-spec",
          "build-slug-traversal", "build-slug-absent", "kept-row-multiword", "kept-row-arity",
          "kept-row-unknown-census", "kept-row-duplicate", "kept-home-rooted", "kept-home-trailing-root",
          "kept-root-blank")
#: TOOL-dTotalRecall-47 S1: the causes check's absent-cause rule, the one finding `--backfill` selects;
#: TOOL-dTotalRecall-53 S4: it names its remedy, and stays the one spelling the backfill selects by
ABSENT_CAUSE = "names no Caused-by, and its kind is no root; run record_causes.py --backfill"
#: TOOL-dTotalRecall-47 AC1 AC3: each backfill plant's new records, `{<path>: <text>}`, `{build}` the fixture's
#: build folder, `{unit}` its unit. The selection plant: a causeless record the verb writes, a record of the
#: kind the plant's registry marks root, a `.sh` record, a record whose Serves line names no id and
#: (TOOL-dTotalRecall-66 S24) a `.json` and a `.js` record under `//` and a bare `.html` one, never graded; the
#: refusals plant: a typed record with no `Caused-by` field and a record whose Serves line is the head
#: window's last unfenced line; TOOL-dTotalRecall-60 AC13's, one causeless record in each of two builds; and
#: TOOL-dTotalRecall-66 S25's, one causeless record no backfill of a refused build may write
BACKFILL_PLANTS = {
    "backfill-selection": {
        "{build}/2026-01-02-build-{unit}-new.md": "# New\n\n**Serves:** research {unit}\n",  # census: kept cause-writer fixture: a record head its fixture plants
        "memory/builds/fRoot/reviews/2026-01-02-review-{unit}-audit.md": "**Serves:** spec-audit {unit}\n\n# An audit\n",  # census: kept cause-writer fixture: a record head its fixture plants
        "{build}/2026-01-02-build-{unit}-probe.sh": "# **Serves:** log {unit}\necho probe\n",  # census: kept cause-writer fixture: a record head its fixture plants
        "{build}/2026-01-02-build-{unit}-json-prefixed.json": "// **Serves:** log {unit}\n[1]\n",  # census: kept cause-writer fixture: a record head its fixture plants
        "{build}/2026-01-02-build-{unit}-js-prefixed.js": "// **Serves:** log {unit}\nlet probe\n",  # census: kept cause-writer fixture: a record head its fixture plants
        "{build}/2026-01-02-build-{unit}-html-bare.html": "**Serves:** log {unit}\n<p>a page</p>\n",  # census: kept cause-writer fixture: a record head its fixture plants
        "{build}/2026-01-02-build-{unit}-unbound.md": "# Unbound\n\n**Serves:** research\n",  # census: kept cause-writer fixture: a record head its fixture plants
    },
    "backfill-refusals": {
        "{build}/2026-01-02-build-{unit}-deviation-1.md": "# {unit} deviation 1 — no cause field\n\n"
                                                         "**Serves:** deviation {unit}\n\n- **Summary:** a departure\n",  # census: kept cause-writer fixture: a record head its fixture plants
        "{build}/2026-01-02-build-{unit}-late.md": "# Late\n" + "a line of the head\n" * 10
                                                   + "**Serves:** research {unit}\n",  # census: kept cause-writer fixture: a record head its fixture plants
    },
    "other-build-causeless": {
        "{build}/2026-01-02-build-{unit}-new.md": "# New\n\n**Serves:** research {unit}\n",  # census: kept cause-writer fixture: a record head its fixture plants
        "memory/builds/fClaim/build/2026-01-02-build-{claim}-new.md": "# New\n\n**Serves:** research {claim}\n",  # census: kept cause-writer fixture: a record head its fixture plants
    },
    **dict.fromkeys(("build-slug-traversal", "build-slug-absent"), {
        "{build}/2026-01-02-build-{unit}-new.md": "# New\n\n**Serves:** research {unit}\n",  # census: kept cause-writer fixture: a record head its fixture plants
    }),
}
#: each backfill plant's expected first `--backfill`: `({<path>: <reason token>} not backfilled, [paths written])`;
#: a plant with no row here is one whose `--build` value the verb refuses
BACKFILL_EXPECTED = {
    "backfill-selection": ({"{build}/2026-01-02-build-{unit}-unbound.md": "no id"},
                           ["{build}/2026-01-02-build-{unit}-new.md", "{build}/2026-01-02-build-{unit}-probe.sh",
                            "{build}/2026-01-02-build-{unit}-json-prefixed.json",
                            "{build}/2026-01-02-build-{unit}-js-prefixed.js"]),
    "backfill-refusals": ({"{build}/2026-01-02-build-{unit}-deviation-1.md": "typed kind",
                           "{build}/2026-01-02-build-{unit}-late.md": "head window"}, []),
    "other-build-causeless": ({"memory/builds/fClaim/build/2026-01-02-build-{claim}-new.md": "another build's record"},
                              ["{build}/2026-01-02-build-{unit}-new.md"]),
}
#: TOOL-dTotalRecall-60 AC13, TOOL-dTotalRecall-66 AC19: the plants whose backfill names one build, and that build
BACKFILL_BUILDS = {"other-build-causeless": "fRoot", "build-slug-traversal": "..", "build-slug-absent": "absentBuild"}
#: TOOL-dTotalRecall-39 AC2 AC3: the plants whose typed record's cause is a bulleted field, each the number of
#: `- **Caused-by:**` fields it writes; both checks read the record, the causes check and the edge walk
BULLETED_PLANTS = {"bulleted-cause": 1, "bulleted-twice": 2}
BULLETED_UNIT = "TOOL-tFix-1"
BULLETED_RECORD = f"memory/builds/tFix/build/2026-01-02-build-{BULLETED_UNIT}-deviation-1.md"
#: the record's head, its fields following from the line after its last
BULLETED_HEAD = f"# {BULLETED_UNIT} deviation 1 — a bulleted cause\n\n**Serves:** deviation {BULLETED_UNIT}\n\n"  # census: kept cause-writer fixture: a record head its fixture plants
#: TOOL-dTotalRecall-51 AC1 to AC3: each script plant's records, `{<name after the record's unit>: <text>}`,
#: `{unit}` the fixture's unit; a cause line wears its Serves line's prefix, and a bare head is not graded
SCRIPT_PLANTS = {
    "script-cause-prefixed": {"probe.py": "# **Serves:** log {unit}\n# **Caused-by:** {unit}\nprint('probe')\n"},
    "script-cause-bare": {"probe.sh": "# **Serves:** log {unit}\n**Caused-by:** {unit}\necho probe\n"},
    "script-causeless": {"probe.sh": "# **Serves:** log {unit}\necho probe\n",  # census: kept cause-writer fixture: a record head its fixture plants
                         "atlas.html": "**Serves:** research {unit}\n<p>an atlas</p>\n"},  # census: kept cause-writer fixture: a record head its fixture plants
}
#: TOOL-dTotalRecall-49 S2 S3: the kept reason of a literal whose one output is a pinned instrument's bytes,
#: which the as-built view's renderer marks (its path, spelled in parts: the install-prefix ban reads a kit
#: path, is where the fixture plants it); the census reds the reason where DESIGN_VIEW is no legacy record
KEPT_INSTRUMENT = "renders a pinned instrument's bytes; its one output is a legacy record"
KEPT_INSTRUMENT_KEY = "/".join(("memory-tree", "asbuilt_view.py"))
#: the census's test-named files, never census members: `*.test.sh`, `selftest.py`, `test_*.py`
CAUSE_WRITER_TEST_RE = re.compile(r"(?:^|/)(?:[^/]*\.test\.sh|selftest\.py|test_[^/]*\.py)$")
SERVES_LITERAL = "**Serves:** "
CAUSE_LITERAL = "Caused-by"
#: TOOL-dTotalRecall-53 S9: a Serves literal is answered by a cause literal on its own line or the three below it
CAUSE_WINDOW = 4
CAUSE_WRITER_CENSUS = "cause-writer"
#: the writer plant's code file, under the fixture's tool root; its red line names it by line
CAUSE_WRITER_PLANT = "planted/writer.py"
#: TOOL-dTotalRecall-53 AC9 AC34: each census plant's code file under the fixture's tool root, its text, and the
#: lines the census must list red, every other literal answered or kept. `{s}` is the Serves literal, `{c}`
#: the cause literal, `{k}` the census marker's lead; each grades by line, never by file.
CENSUS_PLANTS = {
    "literal-without-cause": ("planted/literals.py",
                              '"""Three record heads."""\nA = "{s}log X  **{c}:** X"\nB = "{s}log X"\nC = 1\nD = 2\n'
                              'E = "**{c}:** X"\nF = "{s}log X"\nG = 1\nH = 2\nI = 3\nJ = "**{c}:** X"\n', [7]),
    "duplicate-cause": ("planted/twice.py",
                        '"""One head written twice."""\nHEAD = "{s}log X"\nCAUSE = "**{c}:** X"\nA = 1\nB = 2\n'
                        'C = 3\nD = 4\nE = 5\nAGAIN = "{s}log X"\n', [9]),
    "unmarked-writer": ("planted/kept.py",
                        '"""A kept head, and a writer added beside it."""\n'
                        'HEAD = "{s}log X"  {k} cause-writer fixture: a planted head\nOTHER = "{s}log Y"\n', [3]),
}
#: TOOL-dTotalRecall-50 S2: the records the departures instrument writes, `deviations.py#derive_report_path`'s name,
#: the `records` field of the fixture's pinned row
DEPARTURES_GLOB = "memory/builds/*/build/*-build-*-departures-*.md"


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
        from tag_index import derive_anchor, read_authored_anchors   # noqa: E402  the one anchor rule (TOOL-dTotalRecall-10)
    out, seen = [], set()
    if value == "derived":   # TOOL-dTotalRecall-43 S44: the authored tags' anchors seed `seen` first
        seen = read_authored_anchors(
            m.group("text") for _n, line in itertools.takewhile(lambda nl: nl[1] is not None, tree_lib.unfenced_lines(text))
            for m in [HEADING_RE.fullmatch(line.rstrip())] if m)
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
    """`[(path, section)]`, the `causes` rows of the tree at `root`: `(path, "-")` per Markdown
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
    """`(paths, note)`: the paths of the `-` rows of the population's `causes` slice, the rows whose
    `check` field is `causes`, or None and why the check is unarmed. ValueError for a registration keyed
    by no `check` field, whose slices do not read apart."""
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
    if "check" not in reg.fields:
        raise ValueError(f"{reg.source}: [[ledger]] {POPULATION!r} is keyed {','.join(reg.fields)}, no check")
    rows, bad = ll.read_ledger(root, reg)
    if bad:
        raise ValueError(f"{reg.home}: {ll.render_malformed(bad[0])}")
    at = reg.fields.index("check")
    rows = [k for k in rows if k[at] == "causes"]
    paths = {k[0] for k in rows if k[1] == LEGACY_SECTION}
    if not paths:
        return None, f"{POPULATION}'s home {reg.home} holds no record row"
    return paths, f"{len(paths)} record row(s) (-), {len(rows) - len(paths)} section row(s)"


def read_pinned_rows(root) -> list:
    """`[(instrument, glob, ask id)]`, the pinned writers (TOOL-dTotalRecall-66 S36): one per
    `check_cause_writers` row of `root`'s `census-kept-paths.txt` whose `records` is not `-`, the ask the text
    after its disposition's `keep:`, None under any other, which the census reds naming the row. `[]` where the
    reader refuses the registry, since the census reds that refusal."""
    try:
        kept = tree_lib.read_kept_rows("check_cause_writers", root)
    except ValueError:
        return []
    return [(path, row["records"], row["disposition"][5:] if row["disposition"].startswith("keep:") else None)
            for path, row in kept.items() if row["records"] != "-"]


def read_pinned_records(root, pinned) -> dict:
    """`{glob: [paths]}`: the tracked records each standing row of `pinned` (`read_pinned_rows`' shape)
    reads, through `record_kinds.read_tracked`, `*` never crossing a `/`; an empty glob, which git reads as the
    whole tree, reads none. ValueError where git refuses."""
    import record_kinds   # noqa: E402  the one tracked-glob walk
    try:
        return {glob: record_kinds.read_tracked(root, glob) if glob else [] for _instrument, glob, _ask in pinned}
    except record_kinds.RecordKindsError as exc:
        raise ValueError(str(exc)) from None


def read_grading(root) -> dict:
    """Everything both checks read, once: the graded records (the Markdown ones, then each non-Markdown one
    whose first Serves line wears a comment prefix, TOOL-dTotalRecall-51 S3), their texts and bindings, the
    two target sets, the registry's rows by kind, the legacy paths, `memory.legacy-anchors`, and the records
    the standing pinned rows read (TOOL-dTotalRecall-50 S3). ValueError for a refused read."""
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
            "pinned": {p for paths in read_pinned_records(root, read_pinned_rows(root) if legacy is not None else ())
                       .values() for p in paths}}


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
    """The slugs of the build claims this clone's cache holds, `gen_build_index.CLAIM_CACHE_NS`, which the claim
    CLI's fetch and its own writes fill; never an ask counter's nested name."""
    import gen_build_index   # noqa: E402  the cache namespace's one spelling
    ns = gen_build_index.CLAIM_CACHE_NS + "/"
    p = run_git(root, "for-each-ref", "--format=%(refname)", ns)
    return {r[len(ns):] for r in p.stdout.splitlines() if r.startswith(ns) and "/" not in r[len(ns):]}


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
    from id_grammar import parse_id_parts   # noqa: E402  the one id parser (TOOL-dTotalRecall-53 S16)
    units, claims = read_rooted_units(g)
    slugs = {}   # uid -> its slug or None, parsed once each across the fixed point

    def check_unit_reached(uid):
        """A unit is reached when a rooted README names it or its slug is a claim's; an id the grammar refuses
        names no slug."""
        if uid in units:
            return True
        if uid not in slugs:
            try:
                slugs[uid] = parse_id_parts(uid, g["root"])[1]
            except ValueError:
                slugs[uid] = None
        return slugs[uid] in claims

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
    under the grammar of the conf's FAMILIES. Its liveness past being filed is `check_ask_live`'s."""
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


def check_ask_live(root, ask_id, read=None) -> str | None:
    """Why `ask_id` is not live, or None where it is (TOOL-dTotalRecall-60 S19): `backlog.check_hold_live` over
    the corpus and the finished fold `gen_build_index.read_backlog_at_rev` reads at HEAD, so an uncommitted row
    is not read. `read` holds that reading across one census's rows, filled at its first call. ValueError where
    the read is refused."""
    import backlog   # noqa: E402  the hold's one liveness test
    import gen_build_index   # noqa: E402  the pinned backlog reader
    read = {} if read is None else read
    try:
        if not read:
            read.update(gen_build_index.read_backlog_at_rev(str(root), "HEAD", gen_build_index.load_conf(str(root))))
    except gen_build_index.Problem as exc:
        raise ValueError(f"the backlog at HEAD does not read: {exc}") from None
    live = backlog.check_hold_live(read["corpus"], read["fold"], ask_id)
    if live is None:
        return "HEAD files neither an ask nor a spec of that id"
    return None if live else f"it reads {read['fold'].statuses.get(ask_id) or read['corpus'].specs[ask_id].status} at HEAD"


def read_open_literals(text) -> list:
    """`[(line number, kept reason or None)]`: each line of `text` spelling a `**Serves:** ` literal that no
    `Caused-by` answers on its own line or the `CAUSE_WINDOW - 1` lines below it (TOOL-dTotalRecall-53 S9),
    with the reason its census marker gives (`id_grammar.read_kept_reason`, census `cause-writer`)."""
    from id_grammar import read_kept_reason   # noqa: E402  the three censuses' one marker reader
    body = text.splitlines()
    return [(n, read_kept_reason(ln, CAUSE_WRITER_CENSUS)) for n, ln in enumerate(body, 1)
            if SERVES_LITERAL in ln and not any(CAUSE_LITERAL in x for x in body[n - 1:n - 1 + CAUSE_WINDOW])]


def check_kept_instrument(root) -> str | None:
    """Why the `KEPT_INSTRUMENT` reason no longer holds, or None where it does (TOOL-dTotalRecall-49 S3): the
    design keys read off or refuse, or the record `DESIGN_VIEW` names has no `-` row of the legacy population."""
    from design_lib import DesignRefusal, read_design_conf, read_design_keys   # noqa: E402  the keys' one reader
    try:
        design = read_design_keys(root, read_design_conf(root))
    except DesignRefusal as exc:
        return f"the design keys refuse: {exc}"
    if not design:
        return "the design keys are off, so DESIGN_VIEW names no record"
    legacy, note = read_legacy_paths(root)
    if design["DESIGN_VIEW"] not in (legacy or ()):
        return f"DESIGN_VIEW {design['DESIGN_VIEW']} has no `<path> -` row of {POPULATION}" + ("" if legacy else f" ({note})")
    return None


def check_kept_home(root) -> tuple:
    """TOOL-dTotalRecall-73 S3: `(lines, reds)` joining the keep registry's one path (`tree_lib.resolve_kept_home`),
    which both censuses read, to each ledger registration of its population, the registry file's stem: one line
    naming the path read, one per registration naming its home and source, or one saying none registers it, and
    one red per registration whose home is another path. A refused memory root is one line naming it and no red,
    `read_kept_rows`' catch being the red (TOOL-dTotalRecall-87 S2). ValueError where the registrations do not read.
    It does not check that a registration exists, its fields, or that a file stands at either home."""
    import legacy_ledger as ll   # noqa: E402  the ledger factory
    lead = "cause-writer · keep registry"
    try:
        home = tree_lib.resolve_kept_home(root)
    except ValueError as exc:   # read_kept_rows' catch is the red
        return [f"{lead} · read nowhere: {exc}"], []
    population = pathlib.PurePosixPath(tree_lib.CENSUS_KEPT_REGISTRY).stem
    try:
        regs = [r for r in ll.read_registrations(root) if r.population == population]
    except ValueError as exc:
        raise ValueError(f"the ledger registrations do not read: {str(exc).splitlines()[0]}") from None
    lines = [f"{lead} · read at {home}"]
    lines += [f"{lead} · registered at {r.home} in {r.source}" for r in regs] or [f"{lead} · registered nowhere"]
    reds = [f"cause-writer {tree_lib.CENSUS_KEPT_REGISTRY}: the censuses read {home} and {r.source} registers {r.home}, "
            "so the ratchet grades a file no census reads; register the home under the conf's MEMORY_ROOT"
            for r in regs if pathlib.PurePosixPath(r.home) != pathlib.PurePosixPath(home)]
    return lines, reds


def check_cause_writers(root) -> tuple:
    """S7's writer census: `(lines, reds)` over the alias census's population, every tracked `*.py`, `*.sh`
    and `*.js` file under the tool root (`record_kinds.read_code_paths`), test-named files excepted. It grades
    each `**Serves:** ` literal, never each file (TOOL-dTotalRecall-53 S9): a literal is answered by a
    `Caused-by` on its own line or the three below it (`read_open_literals`), else kept by the census marker
    on its line (`id_grammar.read_kept_reason`, TOOL-dTotalRecall-53 S34), printed `kept <reason>`, else red.
    One line per open literal, then a count line: the code files, the census files holding an open literal,
    and the literals kept and red. It grades spelling, never whether the file writes the line at run time.
    A literal kept for `KEPT_INSTRUMENT` (TOOL-dTotalRecall-49 S3) is red, named with why, where
    `check_kept_instrument` says the reason no longer holds, and wherever its file is not the one
    `KEPT_INSTRUMENT_KEY` names under the tool root, as is a registry row giving it (TOOL-dTotalRecall-60 S26).
    TOOL-dTotalRecall-50 S1 S2: then the build folders' code files (`read_build_code_paths`), both tests read
    past each file's `BIND_HEAD_LINES` binding window, each census file the instrument of a pinned row
    (`read_pinned_rows`, TOOL-dTotalRecall-66 S36) or kept by its `census-kept-paths.txt` row
    (`tree_lib.read_kept_path`, census `check_cause_writers`, TOOL-dTotalRecall-55 S2, TOOL-dTotalRecall-65 S2);
    each pinned row is printed with its ask id and the records its glob reads, and is red where its
    instrument is untracked or spells `Caused-by` past the window, or its ask is unnamed, not filed or not live
    at HEAD (TOOL-dTotalRecall-60 S19). A registry row, pinned rows included, whose file the walk lists as no
    hit is red once, drained, saying why (S4, TOOL-dTotalRecall-66 S1); then the
    build folders' own count line. Each line of those files carrying this census's marker is red, whatever
    row keeps the file and outside that count line's reds (TOOL-dTotalRecall-58 S1). A registry
    holding a malformed row, one of an unknown census, a second row for one census and path (TOOL-dTotalRecall-70
    S11), or one outside `tree_lib.build_kept_path_re`'s domain, is one red naming it, as is a memory root
    `tree_lib.resolve_memory_root` refuses (TOOL-dTotalRecall-87 S2), and the walk reads every
    hit unkept (TOOL-dTotalRecall-57 S1). Last, the registry's homes (`check_kept_home`, TOOL-dTotalRecall-73 S3)."""
    import record_kinds   # noqa: E402  the tool root and the code census's one walk
    from id_grammar import check_marker_domain   # noqa: E402  the build-folder walk's marker refusal
    tool_rel = record_kinds.derive_tool_rel(record_kinds.derive_kit_rel())
    try:
        paths = [p for p in record_kinds.read_code_paths(root, tool_rel) if not CAUSE_WRITER_TEST_RE.search(p)]
    except record_kinds.RecordKindsError as exc:
        raise ValueError(str(exc)) from None
    folder, build_paths = read_build_code_paths(root)
    pinned = read_pinned_rows(root)
    records = read_pinned_records(root, pinned)
    lines, reds, n_kept, files, instrument = [], [], 0, 0, []
    renderer = f"{tool_rel}/{KEPT_INSTRUMENT_KEY}" if tool_rel else KEPT_INSTRUMENT_KEY
    not_renderer = "is the as-built view renderer's alone"   # TOOL-dTotalRecall-60 S26
    for path in paths:
        text = pathlib.Path(root, path).read_bytes().decode("utf-8", "replace")
        if SERVES_LITERAL not in text:
            continue
        found = read_open_literals(text)
        files += bool(found)
        for n, reason in found:
            if reason is None:
                lines.append(f"cause-writer · {path}:{n} · red")
                reds.append(f"cause-writer {path}:{n}: spells a Serves line and no Caused-by on it or the "
                            f"{CAUSE_WINDOW - 1} lines below it; write the cause line under its Serves line, or "
                            f"mark the line `# census: kept {CAUSE_WRITER_CENSUS} <reason>`")
                continue
            if reason == KEPT_INSTRUMENT and path != renderer:   # S26: whatever the instrument's record says
                lines.append(f"cause-writer · {path}:{n} · red · kept {reason}, which {not_renderer}")
                reds.append(f"cause-writer {path}:{n}: kept because it {reason}, a reason that {not_renderer}; write "
                            f"the cause line under its Serves line, or give the line a reason of its own")
                continue
            if reason == KEPT_INSTRUMENT and not instrument:   # read once, on the first literal kept for it
                instrument.append(check_kept_instrument(root))
            why = instrument[0] if reason == KEPT_INSTRUMENT else None
            if why is None:
                n_kept += 1
                lines.append(f"cause-writer · {path}:{n} · kept {reason}")
                continue
            lines.append(f"cause-writer · {path}:{n} · red · kept {reason}, but {why}")
            reds.append(f"cause-writer {path}:{n}: kept because it {reason}, but {why}; restore the record's "
                        f"legacy row or write the cause line under its Serves line")
    lines.append(f"cause-writer · {len(paths)} code files under {tool_rel or '.'} · {files} census "
                 f"file(s) · {n_kept} kept · {len(reds)} red")
    rows, read, drained = {}, {}, set()   # S2: {instrument: ask id}; the backlog at HEAD, read once; rows S4 leaves
    for instrument, glob, ask in pinned:
        try:
            tracked = record_kinds.read_tracked(root, instrument)
        except record_kinds.RecordKindsError as exc:
            raise ValueError(str(exc)) from None
        if not tracked:
            drained.add(instrument)
            why = "is not tracked, so the row pins nothing: drain the row"
        elif CAUSE_LITERAL in "\n".join(pathlib.Path(root, instrument).read_bytes().decode("utf-8", "replace")
                                        .splitlines()[tree_lib.BIND_HEAD_LINES:]):
            drained.add(instrument)
            why = (f"spells {CAUSE_LITERAL} past its binding window, so the records it writes carry their cause: "
                   "drain the row")
        elif not ask:
            why = "names no ask: a pinned row's disposition is keep:<ask id>"
        else:
            why = check_ask_filed(root, ask)
            why = why and f"names ask {ask}, which is not a filed ask: {why}"
            if not why:   # TOOL-dTotalRecall-60 S19: a filed ask must be live too
                why = check_ask_live(root, ask, read)
                why = why and f"names ask {ask}, which is not live: {why}"
        rows[instrument] = ask
        state = f"red · {why}" if why else "filed"
        lines.append(f"cause-writer · pinned · {instrument} · ask {ask} · {state} · {glob} reads "
                     f"{len(records[glob])} record(s)")
        if why:
            reds.append(f"cause-writer {tree_lib.CENSUS_KEPT_REGISTRY} {instrument} (ask {ask}): {why}")
    try:   # TOOL-dTotalRecall-57 S1: a row naming an editable file is red, and the walk reads every hit unkept
        kept, admitted = tree_lib.read_kept_rows("check_cause_writers", root), True
    except ValueError as exc:
        reds.append(f"cause-writer {exc}")
        kept, admitted = {}, False
    b_kept = b_pinned = b_red = 0
    serving, hits = set(), set()   # S4: the walked files spelling a Serves literal past their window; the hits
    for path in build_paths:
        text = pathlib.Path(root, path).read_bytes().decode("utf-8", "replace")
        for n, finding in check_marker_domain(path, text, CAUSE_WRITER_CENSUS):   # TOOL-dTotalRecall-58 S1
            lines.append(f"{CAUSE_WRITER_CENSUS} · {path}:{n} · red · marker in a build folder")
            reds.append(finding)
        past = text.splitlines()[tree_lib.BIND_HEAD_LINES:]
        if any(SERVES_LITERAL in ln for ln in past):
            serving.add(path)
        if path not in serving or any(CAUSE_LITERAL in ln for ln in past):
            continue
        hits.add(path)
        n = next(i for i, ln in enumerate(past, tree_lib.BIND_HEAD_LINES + 1) if SERVES_LITERAL in ln)
        row = tree_lib.read_kept_path("check_cause_writers", path, root) if admitted else None
        reason = row["reason"] if row else None
        if path in rows:
            b_pinned += 1
            lines.append(f"cause-writer · {path}:{n} · pinned {tree_lib.CENSUS_KEPT_REGISTRY} · ask {rows[path]}")
        elif reason == KEPT_INSTRUMENT:   # TOOL-dTotalRecall-60 S26: its row's red, below, names it
            b_red += 1
            lines.append(f"cause-writer · {path}:{n} · red · kept {reason}, which {not_renderer}")
        elif reason:   # the factory admits an empty key field, and an empty reason keeps nothing
            b_kept += 1
            lines.append(f"cause-writer · {path}:{n} · kept {reason}")
        else:
            b_red += 1
            lines.append(f"cause-writer · {path}:{n} · red")
            reds.append(f"cause-writer {path}:{n}: spells a Serves line past its binding window and no Caused-by; "
                        f"write the cause line under its Serves line, key the file in {tree_lib.CENSUS_KEPT_REGISTRY} "
                        f"with its reason, or, a pinned writer, with its record glob and keep:<ask id> too")
    walked = set(build_paths)
    for path, row in kept.items():   # S4: a row cannot outlive its hit
        reason = row["reason"]
        if reason == KEPT_INSTRUMENT:   # TOOL-dTotalRecall-60 S26: a build folder's file is never the renderer
            reds.append(f"cause-writer {tree_lib.CENSUS_KEPT_REGISTRY} {path}: kept because it {reason}, a reason that "
                        f"{not_renderer}; give the row a reason of its own")
        elif path not in hits and path not in drained:   # a pinned row S2 drained is red there, never twice
            why = ("is no file the build-folder walk reads" if path not in walked else
                   f"spells {CAUSE_LITERAL} past its binding window" if path in serving else
                   "spells no Serves line past its binding window")
            lines.append(f"cause-writer · kept row · {path} · red · drained")
            reds.append(f"cause-writer {tree_lib.CENSUS_KEPT_REGISTRY} {path}: {why}, so the row keeps nothing; "
                        f"drain the row")
    lines.append(f"cause-writer · {len(build_paths)} code files under {folder} · {b_kept + b_pinned + b_red} census "
                 f"file(s) · {b_kept} kept · {b_pinned} pinned · {b_red} red")
    home_lines, home_reds = check_kept_home(root)
    return lines + home_lines, reds + home_reds


def run_cause_writers(root) -> tuple:
    """`--cause-writers`: `(lines, exit)`, the writer census's table alone (TOOL-dTotalRecall-53 S35)."""
    try:
        lines, reds = check_cause_writers(root)
    except ValueError as exc:
        return [f"{SAY}: refused · {exc}"], 2
    return [f"{SAY}: {ln}" for ln in lines] + [f"{SAY}: RED {r}" for r in reds], 1 if reds else 0


def run_check(root) -> tuple:
    """`--check`: `(lines, exit)`; an unarmed tree reads no pinned row."""
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


def write_missing_causes(root, build=None) -> tuple:
    """`--backfill` (TOOL-dTotalRecall-47 S1 S2): `(lines, exit)`. Writes `**Caused-by:** <first Serves id>`
    under the first Serves line of each record the causes check names with `ABSENT_CAUSE`, behind the lead that
    line wears (TOOL-dTotalRecall-60 S20), in the file's own line ending, and lists each record S2 refuses under
    `not backfilled` with its reason, byte-identical. `build` a slug writes under that build's folder alone,
    any other selected record refused (TOOL-dTotalRecall-60 S13); None reads the whole tree. A `build` that is
    no build slug whole, or whose README is not tracked, is refused before any read (TOOL-dTotalRecall-66 S25)."""
    import build_records   # noqa: E402  the typed kinds' name grammar
    from id_grammar import ConfError, derive_slug_grammar   # noqa: E402  the build slug's one grammar
    try:
        if build is not None and not derive_slug_grammar(root).BUILD_SLUG_RE.fullmatch(build):
            raise ValueError(f"--build {build} is no build slug under this tree's grammar")
        if build is not None and build not in read_readme_slugs(root):
            raise ValueError(f"--build {build} names no tracked build README")
        g = read_grading(root)
    except (ValueError, ConfError) as exc:
        return [f"{SAY}: refused · {exc}"], 2
    if g["legacy"] is None:
        return [f"{SAY}: unarmed · {g['note']}", f"{SAY}: 0 backfilled · 0 not backfilled"], 0

    folder = f"{g['conf']['MEMORY_ROOT']}/builds/{build}/"

    def derive_backfill_refusal(path):
        """`(reason, Serves line number, cause line)` of one selected record, `reason` None where S2 admits it."""
        if build and not path.startswith(folder):
            return "another build's record", 0, None
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
        n, line = head[at]
        return None, n, f"{line[:line.index('**Serves:**')]}**Caused-by:** {ids[0]}"

    lines, written, refused = [], 0, 0
    for finding in check_causes(root, g):
        _rule, path, why = finding.split(" · ", 2)
        if why != ABSENT_CAUSE:
            continue
        reason, n, cause = derive_backfill_refusal(path)
        if reason:
            refused += 1
            lines.append(f"{SAY}: not backfilled · {path} · {reason}")
            continue
        file = pathlib.Path(root, path)
        raw = file.read_bytes().decode("utf-8")
        eol, parts = "\r\n" if "\r\n" in raw else "\n", raw.split("\n")
        if n < len(parts):   # a line follows the Serves line: the cause goes between, ended as the file ends lines
            parts.insert(n, cause + eol[:-1])
            raw = "\n".join(parts)
        else:   # the Serves line ends the file unterminated, and so does the cause line after it
            raw += eol + cause
        file.write_bytes(raw.encode("utf-8"))
        written += 1
        lines.append(f"{SAY}: backfilled · {path} · Caused-by {cause.split()[-1]}")
    lines.append(f"{SAY}: {written} backfilled · {refused} not backfilled")
    return lines, 0


# ------------------------------------------------------------------------------------------ the fixture
FIXTURE_UNIT = "TOOL-fRoot-1"
FIXTURE_CLAIM = "TOOL-fClaim-1"
#: TOOL-dTotalRecall-50 AC2 AC3: the pinned plants, their instrument, its row and the ask the row names, filed
#: in fRoot's BACKLOG.md; the drained plant's instrument spells the cause past its binding window, and
#: TOOL-dTotalRecall-58 AC1's carries the census marker on its Serves literal's line; TOOL-dTotalRecall-60
#: AC19's adds a WONTDO row for the ask. Their conf declares the builds layout, without which no ask is live
#: (TOOL-dTotalRecall-66 AC20's row names FIXTURE_UNIT, an open spec, for its ask); TOOL-dTotalRecall-70 S4's
#: multiword plant adds KEPT_SCRIPT under a plain keep
PINNED_PLANTS = ("pinned-writer-drained", "departures-pinned", "marker-in-build-script", "pinned-ask-closed",
                 "pinned-ask-is-spec", "kept-row-multiword")
PINNED_INSTRUMENT = f"memory/builds/fRoot/build/2026-01-01-build-{FIXTURE_UNIT}-deviations.py"
PINNED_ASK = "TOOL-fRoot-2"
PINNED_RECORD = f"memory/builds/fRoot/build/2026-01-02-build-{FIXTURE_UNIT}-departures-build.md"
PINNED_BACKLOG = "memory/builds/fRoot/BACKLOG.md"
#: TOOL-dTotalRecall-55 AC2: the drained plant's build-folder script, a one-line docstring spelling no Serves
#: literal, and the one `check_cause_writers` row keeping it, which S4 reds as a row with no hit behind it
KEPT_SCRIPT = f"memory/builds/fRoot/build/2026-01-01-build-{FIXTURE_UNIT}-kept.py"
KEPT_NO_HIT = '"""A script its row keeps, spelling no record head."""\n'
FIXTURE_KEPT = ("check_cause_writers", KEPT_SCRIPT, "outside the write set")
#: TOOL-dTotalRecall-60 AC26: the renderer's kept reason on two files that are not it, a tool-root writer whose
#: marker gives it and KEPT_SCRIPT spelling a Serves literal past its binding window under a row giving it
REASON_WRITER_PLANT = "planted/reason.py"
FIXTURE_REASON_KEPT = ("check_cause_writers", KEPT_SCRIPT, KEPT_INSTRUMENT)
#: TOOL-dTotalRecall-57 AC1: the editable plant's one `check_cause_writers` row, a Python file in the `planted`
#: folder under the fixture's tool root, which S1 reds as a row outside `tree_lib.build_kept_path_re`'s domain
EDITABLE_KEPT_PLANT = "planted/editable.py"
#: TOOL-dTotalRecall-66 AC9: the one row of each domain plant, a path holding a `..` segment where a build's
#: slug goes, and one under a folder inside `build/`, which a `*` crossing `/` would admit
DOMAIN_KEPT_PLANTS = {"kept-row-traversal": "memory/builds/../build/traversal.py",
                      "kept-row-nested": "memory/builds/fRoot/build/nested/nested.py"}
#: TOOL-dTotalRecall-66 AC1 AC7: KEPT_SCRIPT spelling a Serves literal past its binding window, the hit a row keeps
KEPT_HIT = "# a line of the head\n" * tree_lib.BIND_HEAD_LINES + f'HEAD = "{SERVES_LITERAL}log {FIXTURE_UNIT}"\n'
#: TOOL-dTotalRecall-66 AC7, TOOL-dTotalRecall-73 S4: the plants whose fixture's memory root is not `memory`
FIXTURE_MEMORY_ROOTS = {"kept-row-docs-root": "docs/memory", "kept-home-rooted": "docs/memory",
                        "kept-home-trailing-root": "docs/memory"}
#: TOOL-dTotalRecall-87 S3 S4: the plants whose conf is rewritten to this memory root after the seed, and which grade
#: the writer census alone, since `--check` is red or refused under either value before any census prints
REWRITTEN_ROOTS = {"kept-home-trailing-root": "docs/memory/", "kept-root-blank": ""}
#: TOOL-dTotalRecall-65 S4: the fixture's own registry, where each of those plants writes its row, through
#: `record_kinds.write_kept_fixture` (TOOL-dTotalRecall-68 S6); and the literal home the plant `kept-home-rooted`
#: registers, which its tree under `docs/memory` does not read (TOOL-dTotalRecall-73 S4), where
#: `kept-home-trailing-root` registers it under that root (TOOL-dTotalRecall-87 S3)
FIXTURE_REGISTRY = f"memory/project/{tree_lib.CENSUS_KEPT_REGISTRY}"


def render_pinned_instrument(drained) -> str:
    """The pinned plants' instrument: a comment head naming its cause, padded to its binding window, then
    the record head it writes, and where `drained` the cause line it now writes too."""
    head = f"# **Serves:** research {FIXTURE_UNIT}\n# **Caused-by:** {FIXTURE_UNIT}\n"
    head += "# a line of the head\n" * (tree_lib.BIND_HEAD_LINES - 2)
    body = f'HEAD = "{SERVES_LITERAL}journal {{first}}"\n'
    return head + body + (f'CAUSE = "**{CAUSE_LITERAL}:** {{first}}"\n' if drained else "")


def write_fixture(top, plant, memory="memory") -> pathlib.Path:
    """The plant's repository under `top`: a conf, a three-row registry (`log`, `research`, `card`), a govkit
    registry holding the `record-kinds-legacy` table keyed as gov keys it, its seed the `causes` slice, the
    build `fRoot` (README, a spec, a log record and a research record repeating `## Findings`), committed;
    the population seeded; then the plant's new records and refs, committed. `none` commits `memory.legacy-anchors = "none"` first.
    `memory` is the tree's memory root, every path, home glob and conf line spelled from it."""
    import json
    import legacy_ledger as ll   # noqa: E402  the seed, run as `seed` runs it
    import record_kinds   # noqa: E402  the kit's path inside a repository
    from id_grammar import parse_id_parts   # noqa: E402  the one id parser, under this tree's grammar
    root = pathlib.Path(top, "repo")
    kit_rel = record_kinds.derive_kit_rel()
    tool_rel = record_kinds.derive_tool_rel(kit_rel)
    prefix = "{prefix}"

    def derive_rel(rel):
        """`rel` with a leading `memory/` read as the fixture's memory root."""
        return f"{memory}/{rel.removeprefix('memory/')}" if rel.startswith("memory/") else rel

    def write_file(rel, text):
        p = root / derive_rel(rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))

    def run_commit(msg):
        for args in (("add", "-A"), ("-c", "user.name=fx", "-c", "user.email=fx@example.invalid", "-c",
                                     "commit.gpgsign=false", "commit", "-q", "--no-verify", "-m", msg)):
            p = run_git(root, *args)
            if p.returncode:
                raise ValueError(f"the fixture's git {args[0]} refused: {p.stderr.strip()}")

    rows = {"log": (f"{memory}/builds/*/prompts/*.md", '["Serves"]'), "research": (f"{memory}/builds/*/build/*.md", '["Serves"]'),
            "card": (f"{memory}/builds/*/build/*-build-*-card-*.md", '["Build", "Step", "Ref"]')}
    if plant in BULLETED_PLANTS or plant == "backfill-refusals":   # a typed kind whose fields hold `Caused-by`
        rows["deviation"] = (f"{memory}/builds/*/build/*-build-*-deviation-*.md", '["Serves", "Caused-by"]')
    roots = set()
    if plant == "backfill-selection":   # TOOL-dTotalRecall-47 AC1: a kind the registry marks root
        rows["spec-audit"] = (f"{memory}/builds/*/reviews/*.md", '["Serves"]')
        roots.add("spec-audit")
    conf = f'MEMORY_ROOT="{memory}"\nFAMILIES="tooling:TOOL"\n' + ('BACKLOG_MODE="builds"\n' if plant in PINNED_PLANTS else "")
    write_file(".memory-tree.conf", conf)
    write_file(f"{kit_rel}/{record_kinds.REGISTRY}", "".join(
        f'[[record-kind]]\nname = "{n}"\nhome = "{h}"\nschema = {{ form = "fields", fields = {f} }}\n'
        + ("root = true\n" if n in roots else "") + "\n" for n, (h, f) in rows.items()))
    sibling = "/".join(("govkit", "registry.toml"))   # spelled in parts: the install-prefix ban reads a kit path
    split = ""
    if plant in ("kept-home-rooted", "kept-home-trailing-root"):   # TOOL-dTotalRecall-73 S4, TOOL-dTotalRecall-87 S3
        kept_home = FIXTURE_REGISTRY if plant == "kept-home-rooted" else derive_rel(FIXTURE_REGISTRY)
        split = (f'\n[[ledger]]\npopulation = "{pathlib.PurePosixPath(FIXTURE_REGISTRY).stem}"\nleg = "record causes"\n'
                 f'seed = ["python"]\nkey = "key"\nfields = {json.dumps(tree_lib.KEPT_FIELDS)}\ndrain = "key"\n'
                 f'direction = "shrink-only"\nhome = "{kept_home}"\n')
    write_file(f"{tool_rel}/{sibling}" if tool_rel else sibling,
               f'[[ledger]]\npopulation = "{POPULATION}"\nleg = "record causes"\n'
               f'seed = {json.dumps(["python", f"{prefix}/{kit_rel[len(tool_rel) + 1:] if tool_rel else kit_rel}/record_causes.py", "--measure"])}\n'
               'key = "record"\nfields = ["path", "section", "check"]\nverbatim = ["section"]\ndrain = "key"\n'
               f'direction = "shrink-only"\nhome = "{memory}/project/{POPULATION}.txt"\n' + split)
    write_file("memory/project/README.md", "the fixture's project registry\n")
    write_file("memory/builds/fRoot/README.md", f"---\nslug: fRoot\nopened: 2026-01-01\nids: {FIXTURE_UNIT}\n---\n\n# fRoot\n")
    for unit in (FIXTURE_UNIT, FIXTURE_CLAIM):
        slug = parse_id_parts(unit, None)[1]
        write_file(f"memory/builds/{slug}/spec/2026-01-01-spec-{unit}.md",
                   f"# {unit} — the fixture's unit\n\n**Status:** OPEN · rev-1 · 2026-01-01 · node a · Tier-1 · base 00000000\n")
    write_file(f"memory/builds/fRoot/prompts/2026-01-01-prompt-{FIXTURE_UNIT}-brief.md",
               f"**Serves:** journal {FIXTURE_UNIT}\n\n# A brief shaped like today's\n\nthe brief\n")  # census: kept cause-writer fixture: a record head its fixture plants
    write_file(f"memory/builds/fRoot/build/2026-01-01-build-{FIXTURE_UNIT}-notes.md",
               f"**Serves:** research {FIXTURE_UNIT}\n\n# Notes\n\n## Findings\n\none\n\n## Findings\n\ntwo\n")  # census: kept cause-writer fixture: a record head its fixture plants
    build = f"{memory}/builds/fRoot/build"
    view = f"{build}/2026-01-01-build-{FIXTURE_UNIT}-as-built.md"
    view_plants = ("kept-instrument-not-legacy", "reason-on-other-file")
    if plant in view_plants:   # TOOL-dTotalRecall-49 S3: the view, in the legacy tree and caused
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
        write_file(f"{build}/2026-01-02-build-{FIXTURE_UNIT}-new.md", f"# New\n\n**Serves:** research {FIXTURE_UNIT}\n")  # census: kept cause-writer fixture: a record head its fixture plants
    elif plant == "typed-causeless":
        write_file(f"{build}/2026-01-02-build-{FIXTURE_UNIT}-card-1.md",
                   f"# {FIXTURE_UNIT} card 1 — a card\n\n**Serves:** card {FIXTURE_UNIT}\n\n- **Build:** fRoot\n"  # census: kept cause-writer fixture: a record head its fixture plants
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
            write_file(rel.format(build=build, unit=FIXTURE_UNIT, claim=FIXTURE_CLAIM),
                       text.format(unit=FIXTURE_UNIT, claim=FIXTURE_CLAIM))
    elif plant in PINNED_PLANTS:   # TOOL-dTotalRecall-50 AC2 AC3: a pinned instrument, its filed ask, a record
        import backlog   # noqa: E402  the ask door's row renderers
        from gov_record import render_backlog_text   # noqa: E402  the ask door's file layout
        text = render_pinned_instrument(plant == "pinned-writer-drained")
        if plant == "marker-in-build-script":   # TOOL-dTotalRecall-58 AC1: its last line is its Serves literal's
            text = f"{text.rstrip()}  # census: kept {CAUSE_WRITER_CENSUS} pinned instrument\n"
        write_file(PINNED_INSTRUMENT, text)
        write_file(PINNED_BACKLOG, render_backlog_text(
            None, "fRoot", backlog.render_ask_row(PINNED_ASK, "2026-01-02", "THE PLANTED INSTRUMENT WRITES NO CAUSE.",
                                                  clauses=[("accept", "its records carry the line")]),
            backlog.render_sev_row(PINNED_ASK, "LOW", "its records read their cause from their Serves unit")))
        if plant == "pinned-ask-closed":   # TOOL-dTotalRecall-60 AC19: the ask disposed, its row still filed
            with open(root / PINNED_BACKLOG, "ab") as fh:
                fh.write((backlog.render_status_row("WONTDO", PINNED_ASK, "the planted ask is closed") + "\n").encode("utf-8"))
        kept = [("check_cause_writers", PINNED_INSTRUMENT, "pinned instrument", DEPARTURES_GLOB,   # TOOL-dTotalRecall-66 S36
                 f"keep:{FIXTURE_UNIT if plant == 'pinned-ask-is-spec' else PINNED_ASK}")]
        if plant == "kept-row-multiword":   # TOOL-dTotalRecall-70 S4: a plain keep beside it, its reason of words too
            write_file(KEPT_SCRIPT, KEPT_HIT)
            kept.append(FIXTURE_KEPT)
        record_kinds.write_kept_fixture(root, *kept)
        if plant in ("departures-pinned", "pinned-ask-closed"):
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
    if plant == "kept-row-drained":   # TOOL-dTotalRecall-55 AC2: a kept script whose hit is gone
        write_file(KEPT_SCRIPT, KEPT_NO_HIT)
        record_kinds.write_kept_fixture(root, FIXTURE_KEPT)
    if plant == "kept-row-arity":   # TOOL-dTotalRecall-70 S5: a row of four TAB fields, and one of six
        write_file(KEPT_SCRIPT, KEPT_NO_HIT)
        record_kinds.write_kept_fixture(root)
        with open(root / FIXTURE_REGISTRY, "ab") as fh:
            fh.write("".join("\t".join((*FIXTURE_KEPT, "-", "1", ll.NULL_SHA)[:n]) + "\n" for n in (4, 6)).encode("utf-8"))
    if plant == "kept-row-unknown-census":   # TOOL-dTotalRecall-70 S11: a census no census function bears
        write_file(KEPT_SCRIPT, KEPT_NO_HIT)
        record_kinds.write_kept_fixture(root, ("check_cause_writer", *FIXTURE_KEPT[1:]))
    if plant == "kept-row-duplicate":   # TOOL-dTotalRecall-70 S11: two rows of one pair, their reasons apart
        write_file(KEPT_SCRIPT, KEPT_HIT)
        record_kinds.write_kept_fixture(root, FIXTURE_KEPT, (*FIXTURE_KEPT[:2], "another reason"))
    if plant == "kept-row-editable":   # TOOL-dTotalRecall-57 AC1: a row naming an editable file
        row = f"{tool_rel}/{EDITABLE_KEPT_PLANT}" if tool_rel else EDITABLE_KEPT_PLANT
        record_kinds.write_kept_fixture(root, ("check_cause_writers", row, "outside the write set"))
    if plant in DOMAIN_KEPT_PLANTS:   # TOOL-dTotalRecall-66 AC9: a row outside the domain's segments
        record_kinds.write_kept_fixture(root, ("check_cause_writers", DOMAIN_KEPT_PLANTS[plant], "outside the write set"))
    if plant in ("kept-row-caused", "kept-row-untracked", "kept-row-docs-root"):   # TOOL-dTotalRecall-66 AC1 AC7
        record_kinds.write_kept_fixture(root, ("check_cause_writers", derive_rel(KEPT_SCRIPT), "outside the write set"))
        if plant != "kept-row-untracked":
            write_file(KEPT_SCRIPT, KEPT_HIT + (f'CAUSE = "**{CAUSE_LITERAL}:** {FIXTURE_UNIT}"\n'
                                                if plant == "kept-row-caused" else ""))
    if plant in view_plants:   # the four design keys set over the view, its `-` row cut
        pin = run_git(root, "rev-parse", "HEAD").stdout.strip()
        home = root / reg.home
        if plant == "kept-instrument-not-legacy":
            home.write_bytes("".join(ln for ln in home.read_bytes().decode("utf-8").splitlines(True)
                                     if not ln.startswith(f"{view}\t{LEGACY_SECTION}\t")).encode("utf-8"))
        write_file(".memory-tree.conf", conf + f'DESIGN_RECORD="{build}/2026-01-01-build-{FIXTURE_UNIT}-notes.md"\n'
                   f'DESIGN_BASELINE="{pin}"\nDESIGN_VIEW="{view}"\nDESIGN_NODES="{build}/map.py"\n')
        write_file(f"{tool_rel}/{KEPT_INSTRUMENT_KEY}" if tool_rel else KEPT_INSTRUMENT_KEY,
                   f'"""A view renderer."""\nHEAD = "{SERVES_LITERAL}research {FIXTURE_UNIT}\\n"  '
                   f'# census: kept {CAUSE_WRITER_CENSUS} {KEPT_INSTRUMENT}\n')
    if plant == "reason-on-other-file":   # TOOL-dTotalRecall-60 AC26: the reason holds, on two files not its own
        write_file(f"{tool_rel}/{REASON_WRITER_PLANT}" if tool_rel else REASON_WRITER_PLANT,
                   f'"""A writer."""\nHEAD = "{SERVES_LITERAL}log {FIXTURE_UNIT}\\n"  '
                   f'# census: kept {CAUSE_WRITER_CENSUS} {KEPT_INSTRUMENT}\n')
        write_file(KEPT_SCRIPT, KEPT_HIT)
        record_kinds.write_kept_fixture(root, FIXTURE_REASON_KEPT)
    if plant in REWRITTEN_ROOTS:   # TOOL-dTotalRecall-87 S3 S4: the seed ran under the root the tree is built at
        write_file(".memory-tree.conf", conf.replace(f'MEMORY_ROOT="{memory}"', f'MEMORY_ROOT="{REWRITTEN_ROOTS[plant]}"'))
    if plant in CENSUS_PLANTS:   # TOOL-dTotalRecall-53 AC9 AC34: literals graded by line, a marker kept by line
        rel, text, _red = CENSUS_PLANTS[plant]
        write_file(f"{tool_rel}/{rel}" if tool_rel else rel,
                   text.format(s=SERVES_LITERAL, c=CAUSE_LITERAL, k="# census: kept"))
    run_commit(f"record-causes fixture: {plant}")
    if plant == "kept-row-untracked":   # TOOL-dTotalRecall-66 AC1: the kept script, never added to git
        write_file(KEPT_SCRIPT, KEPT_HIT)
    if plant == "claim-root":   # TOOL-dTotalRecall-119 S2: minted by the claim CLI, on a remote of the fixture's own
        import gen_build_index   # noqa: E402  the claim CLI's one caller
        remote = pathlib.Path(top, "r.git")
        for at, args in ((top, ("init", "-q", "--bare", "--template=", str(remote))),
                         (root, ("remote", "add", "fixture", str(remote))),
                         (root, ("push", "-q", "fixture", "HEAD:refs/heads/main")),
                         (remote, ("symbolic-ref", "HEAD", "refs/heads/main"))):
            p = run_git(at, *args)
            if p.returncode:
                raise ValueError(f"the fixture's git {args[0]} refused: {p.stderr.strip()}")
        try:
            rc, said = gen_build_index.run_claim_cli(str(root), "slug", "fClaim", "--claimant", "a" * 12)
        except gen_build_index.Problem as exc:
            raise ValueError(f"the fixture's claim: {exc}") from None
        if rc:
            raise ValueError(f"the fixture's claim, exit {rc}: {said}")
        held = run_git(root, "for-each-ref", "--format=%(refname)", "refs/gov/").stdout.split()
        print(f"{SAY}: fixture {plant} · claim · {' '.join(held)}")
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
    the check names exactly the refused records under `causes`, the second run prints `0 backfilled`, and each
    non-Markdown record written holds one cause line, under its Serves line and behind its prefix
    (TOOL-dTotalRecall-60 S20, TOOL-dTotalRecall-66 S24).
    A BACKFILL_BUILDS plant's backfill names its build (TOOL-dTotalRecall-60 S13), and one with no
    BACKFILL_EXPECTED row passes when the verb exits 2 naming that value and the status is clean
    (TOOL-dTotalRecall-66 S25)."""
    build = "memory/builds/fRoot/build"
    if plant not in BACKFILL_EXPECTED:
        first, rc = write_missing_causes(root, BACKFILL_BUILDS[plant])
        status = run_git(root, "status", "--porcelain").stdout.splitlines()
        ok = rc == 2 and len(first) == 1 and f"refused · --build {BACKFILL_BUILDS[plant]} " in first[0] and not status
        return [f"{SAY}: fixture {plant} · backfill 1 · {ln}" for ln in first] + [
            f"{SAY}: fixture {plant} · status · {ln}" for ln in status] + [
            f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · backfill exit {rc} · a --build that is no tracked "
            "build's slug is refused and writes nothing"], ok
    want, wrote = BACKFILL_EXPECTED[plant]
    want = {k.format(build=build, unit=FIXTURE_UNIT, claim=FIXTURE_CLAIM): v for k, v in want.items()}
    wrote = [p.format(build=build, unit=FIXTURE_UNIT) for p in wrote]
    first, _rc = write_missing_causes(root, BACKFILL_BUILDS.get(plant))
    out = [f"{SAY}: fixture {plant} · backfill 1 · {ln}" for ln in first]
    refused = {ln.split(" · ")[1]: ln.split(" · ")[2] for ln in first if ln.startswith(f"{SAY}: not backfilled · ")}
    done = [ln.split(" · ")[1] for ln in first if ln.startswith(f"{SAY}: backfilled · ")]
    status = sorted(ln[3:] for ln in run_git(root, "status", "--porcelain").stdout.splitlines())
    out += [f"{SAY}: fixture {plant} · status · {ln}" for ln in status]
    ok = sorted(done) == sorted(wrote) and status == sorted(wrote) and set(refused) == set(want) \
        and all(refused[p].startswith(r) for p, r in want.items())
    if plant == "backfill-selection":
        lines, _rc = run_check(root)
        second, _rc = write_missing_causes(root)
        out += [f"{SAY}: fixture {plant} · check · {ln}" for ln in lines]
        out += [f"{SAY}: fixture {plant} · backfill 2 · {ln}" for ln in second]
        named = {ln.split(" · ")[1] for ln in lines if ln.startswith(f"{SAY}: causes · ")}
        ok = ok and named == set(want) and second[-1].startswith(f"{SAY}: 0 backfilled")
        for p in (p for p in wrote if not p.endswith(".md")):
            body = pathlib.Path(root, p).read_bytes().decode("utf-8").split("\n")
            caused = [n for n, ln in enumerate(body) if CAUSE_LITERAL in ln]
            out += [f"{SAY}: fixture {plant} · {p}:{n + 1}:{body[n]}" for n in caused]
            ok = ok and caused == [1] and body[1] == f"{'#' if p.endswith('.sh') else '//'} **{CAUSE_LITERAL}:** {FIXTURE_UNIT}"
    out.append(f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · the backfill writes what the causes check "
               "lacks and refuses to guess")
    return out, ok


def check_pinned_plant(root, plant) -> tuple:
    """TOOL-dTotalRecall-50 AC2 AC3: `--check` twice over a pinned plant's `root`. -> `(lines, ok)`: each
    run's lines and exit, then one PASS or FAIL line. The drained plant passes when the first run exits 1
    naming the row drained, and the second, its instrument written causeless and its ask row deleted from
    PINNED_BACKLOG, exits 1 naming the ask not filed and the row not drained. The departures plant passes
    when the first run, under the fixture's registry row, exits 0, and the second, the row cut, exits 1 naming
    PINNED_RECORD under causes. The marker plant (TOOL-dTotalRecall-58 AC1) runs the first alone and passes when
    it exits 1 with one red, naming the instrument's Serves literal's line; the closed-ask plant
    (TOOL-dTotalRecall-60 AC19) alike, its one red naming the row and its ask not live, WONTDO, and the spec-ask
    plant (TOOL-dTotalRecall-66 AC20), its one red naming the row and the open spec id no filed ask. The multiword
    plant (TOOL-dTotalRecall-70 S4) passes when the first exits 0, KEPT_SCRIPT's keep line ends with its whole
    reason and the reader answers the pinned row's whole reason in its `reason` field."""
    first, rc1 = run_check(root)
    if plant == "kept-row-multiword":
        line = [ln for ln in first if f" · {KEPT_SCRIPT}:" in ln and ln.endswith(f" · kept {FIXTURE_KEPT[2]}")]
        row = tree_lib.read_kept_path("check_cause_writers", PINNED_INSTRUMENT, root) or {}
        ok = rc1 == 0 and len(line) == 1 and row.get("reason") == "pinned instrument"
        return [f"{SAY}: fixture {plant} · check 1 · {ln}" for ln in first] + [
            f"{SAY}: fixture {plant} · pinned reason · {row.get('reason')}",
            f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · check 1 exit {rc1} · a reason of several words "
            "is read whole, on a plain keep and on a pinned writer's row"], ok
    if plant == "marker-in-build-script":
        at = f"{CAUSE_WRITER_CENSUS} {PINNED_INSTRUMENT}:{tree_lib.BIND_HEAD_LINES + 1}: "
        red = [ln for ln in first if ln.startswith(f"{SAY}: RED ")]
        ok = rc1 == 1 and len(red) == 1 and red[0].startswith(f"{SAY}: RED {at}")
        return [f"{SAY}: fixture {plant} · check 1 · {ln}" for ln in first] + [
            f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · check 1 exit {rc1} · a census marker in a "
            "build folder's script is red by line, its pinned row standing"], ok
    if plant in ("pinned-ask-closed", "pinned-ask-is-spec"):
        ask, why, names, case = {
            "pinned-ask-closed": (PINNED_ASK, "not live", "WONTDO", "once its ask, still filed, is closed"),
            "pinned-ask-is-spec": (FIXTURE_UNIT, "not a filed ask", "files no ask", "where its ask is an open spec's id"),
        }[plant]
        at = f"{SAY}: RED cause-writer {tree_lib.CENSUS_KEPT_REGISTRY} {PINNED_INSTRUMENT} (ask {ask}): "
        red = [ln for ln in first if ln.startswith(f"{SAY}: RED ")]
        ok = rc1 == 1 and len(red) == 1 and red[0].startswith(f"{at}names ask {ask}, which is {why}: ") and names in red[0]
        return [f"{SAY}: fixture {plant} · check 1 · {ln}" for ln in first] + [
            f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · check 1 exit {rc1} · a pinned writer's row is red "
            f"{case}"], ok
    if plant == "pinned-writer-drained":
        pathlib.Path(root, PINNED_INSTRUMENT).write_bytes(render_pinned_instrument(False).encode("utf-8"))
        backlog = pathlib.Path(root, PINNED_BACKLOG)
        backlog.write_bytes("".join(ln for ln in backlog.read_bytes().decode("utf-8").splitlines(True)
                                    if not ln.startswith(f"- {PINNED_ASK} ")).encode("utf-8"))
        second, rc2 = run_check(root)
        row = f"{tree_lib.CENSUS_KEPT_REGISTRY} {PINNED_INSTRUMENT} (ask {PINNED_ASK}): "
        drained = [ln for ln in first if row in ln and f"spells {CAUSE_LITERAL} past" in ln]
        unfiled = [ln for ln in second if row in ln and f"{PINNED_ASK}, which is not a filed ask" in ln]
        ok = rc1 == 1 and rc2 == 1 and len(drained) == 1 and len(unfiled) == 1 \
            and not any(row in ln and f"spells {CAUSE_LITERAL} past" in ln for ln in second)
    else:
        import record_kinds   # noqa: E402  the fixture registry's writer
        record_kinds.write_kept_fixture(root)
        second, rc2 = run_check(root)
        named = [ln for ln in second if ln.startswith(f"{SAY}: causes · {PINNED_RECORD} · ")]
        ok = rc1 == 0 and rc2 == 1 and len(named) == 1
    out = [f"{SAY}: fixture {plant} · check {n} · {ln}" for n, run in ((1, first), (2, second)) for ln in run]
    out += [f"{SAY}: fixture {plant} · check 1 exit {rc1} · check 2 exit {rc2}",
            f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · a pinned writer's row stands until it drains "
            "or its ask is unfiled, and reads its records' cause from their Serves unit while it stands"]
    return out, ok


def check_census_plant(root, plant) -> tuple:
    """TOOL-dTotalRecall-53 AC9 AC34: `--check` over a census plant's `root`. -> `(lines, ok)`: the run's lines,
    then one PASS or FAIL line. It passes when the run exits 1 and the census lists as red exactly the plant's
    lines (`CENSUS_PLANTS`), every other literal of its file answered by a cause in reach or kept by its marker;
    a file-keyed rule, one cause or one marker clearing the file, lists none and fails."""
    import record_kinds   # noqa: E402  the fixture's tool root
    rel, _text, want = CENSUS_PLANTS[plant]
    tool_rel = record_kinds.derive_tool_rel(record_kinds.derive_kit_rel())
    path = f"{tool_rel}/{rel}" if tool_rel else rel
    lines, rc = run_check(root)
    red = sorted(int(ln.split(" · ")[1].rsplit(":", 1)[1]) for ln in lines
                 if ln.startswith(f"{SAY}: cause-writer · {path}:") and ln.endswith(" · red"))
    ok = rc == 1 and red == want
    out = lines + [f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · red line(s) {red or 'none'} of {path}, "
                   f"want {want}: a Serves literal is graded by its own line"]
    return out, ok


def run_fixture(plant) -> tuple:
    """`--fixture --plant <case>`: the plant's repository under the system temp directory, its population's
    rows printed, then `--check` run there, `--cause-writers` under a `REWRITTEN_ROOTS` plant
    (TOOL-dTotalRecall-87 S3 S4). -> `(lines, exit)`. `adopter-no-registry` grades its own check, PASS
    and exit 0 where that exits 0 naming no kept or drained row and the reader answers `{}` for both censuses."""
    if plant not in PLANTS:
        return [f"{SAY}: refused · no plant {plant!r}: the plants are {', '.join(PLANTS)}"], 2
    from deviation_join import remove_tree, set_fixture_env   # noqa: E402  the kit's fixture helpers
    top = pathlib.Path(tempfile.mkdtemp(prefix="rc-"))
    try:
        # TOOL-dTotalRecall-88 S9: a fixture reads nothing of the caller's git environment, config or remote
        with set_fixture_env():
            memory = FIXTURE_MEMORY_ROOTS.get(plant, "memory")
            root = write_fixture(top, plant, memory)
            home = root / memory / "project" / f"{POPULATION}.txt"
            rows = [ln for ln in home.read_bytes().decode("utf-8").split("\n")[1:] if ln]
            head = [f"{SAY}: fixture {plant} · row · " + " ".join(ln.split("\t")[:3]).replace(str(root), "") for ln in rows]
            if plant in BACKFILL_PLANTS:
                lines, ok = check_backfill_plant(root, plant)
                return head + lines, 0 if ok else 1
            if plant in PINNED_PLANTS:
                lines, ok = check_pinned_plant(root, plant)
                return head + lines, 0 if ok else 1
            if plant in CENSUS_PLANTS:
                lines, ok = check_census_plant(root, plant)
                return head + lines, 0 if ok else 1
            lines, rc = run_cause_writers(root) if plant in REWRITTEN_ROOTS else run_check(root)
            if plant == "adopter-no-registry":   # TOOL-dTotalRecall-65 AC3: a row the kit itself held fails it
                read = {c: tree_lib.read_kept_rows(c, root) for c in tree_lib.KEPT_CENSUSES}
                ok = rc == 0 and not (root / FIXTURE_REGISTRY).exists() and not any(read.values()) \
                    and not any(" · kept " in ln for ln in lines)
                lines += [f"{SAY}: fixture {plant} · {c} reads {len(rows)} row(s)" for c, rows in read.items()]
                return head + lines + [f"{SAY}: fixture {plant} · {'PASS' if ok else 'FAIL'} · check exit {rc} · a tree "
                                       f"with no {tree_lib.CENSUS_KEPT_REGISTRY} reads no keep row"], 0 if ok else 1
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
    elif argv == ["--cause-writers"]:   # TOOL-dTotalRecall-53 S35: the writer census's table alone
        lines, rc = run_cause_writers(root)
    elif argv == ["--measure"]:
        try:
            rows = derive_population_rows(root)
        except ValueError as exc:
            print(f"{SAY}: refused · {exc}")
            return 2
        lines, rc = [f"{p}\t{s}\tcauses\t1" for p, s in rows], 0
    elif argv == ["--backfill"]:
        lines, rc = write_missing_causes(root)
    elif len(argv) == 3 and argv[:2] == ["--backfill", "--build"] and argv[2]:   # TOOL-dTotalRecall-60 S13
        lines, rc = write_missing_causes(root, argv[2])
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
