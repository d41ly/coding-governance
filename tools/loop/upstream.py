#!/usr/bin/env python3
"""upstream.py — an item's upstream field: the commitments one item establishes handed on as rows, and
the return that answers each one (TOOL-dDeclaredLoop-29).

    python upstream.py rows <item> --return <upstream item>=<path>...
    python upstream.py join <item> --rows <rows file> --return <return path> [--write --build <slug> --unit <id>]
    python upstream.py --fixture --plant <case>
    python upstream.py --selftest

THE FIELD. An `[[item]]` row may carry `upstream`, a list of one-line inline tables
`{ item = "<item tag>", gate = "record" | "measured" }`, the gate `record` where the entry gives none. An
entry at `measured` also carries `measured-by`, a path whose blob HEAD holds, and `measured-line`, a line
that blob holds whole: the measurement that lets the edge gate. `check_upstream_rows(rows, root)` holds
every composed row to that shape, reads git once for every `measured` entry and not at all without one,
and refuses an item with a non-empty `upstream` whose outcome set lacks `finding`; the item kind's own
`check`, `loop_items.py check`, calls it after its grades and prints `loop: upstream edges · <n> record ·
<m> measured`.

THE ROWS. An item's return declares what it establishes under `## Establishes`, one row per line,
`- <row id> · <kind> · <text>`, the kind one of `ESTABLISH_KINDS` and the id one tag segment, unique in
its return. `rows` prints, one per line, every establishes row of each upstream item's return handed with
`--return`, in entry order, its id qualified as `<upstream item>#<row id>`; an upstream item handed no
return, or whose return has no `## Establishes` section, refuses the hand-on by name. The caller hands the
file on, through the roles kit's `handoff.py render --upstream`.

THE JOIN. The item's return answers each handed row once under `## Upstream`,
`- <row id> · used|bypassed|not-applicable · <reason>`. `join` grades the composition first, as `check`
does, and refuses where it refuses; then every handed id is answered, `dropped` or `doubled`, an answered
id no handed row carries is `invented`, and an answered row is `bad-answer` or `no-reason` where it fails.
A `bypassed` answer is a finding on either edge. Each finding is graded on the gate of the edge its id
names, an invented id naming no edge on the item's strictest gate: on a `measured` edge every finding but
`bypassed` refuses the return, exit 1; on a `record` edge each is a finding and the return stands, exit 0.
A return with no `## Upstream` section answers nothing, so every handed row is `dropped`. With `--write
--build <slug> --unit <id>` it writes every line into `<MEMORY_ROOT>/builds/<slug>/build/<date>-build-<unit
id>-upstream-<n>.md`, created exclusively, and prints its path. Paths resolve inside the repository or
refuse. Both verbs exit 2 on a usage error or a composition that does not read, and print a refusal as
`upstream · refused · <why>`.

`--fixture --plant <case>` builds one scratch repository holding a committed measurement record and the
build folder `dUpstream`, gives the shipped definition's `item.design.unit-spec`, in memory, an entry
naming `item.design.seams` and the outcome `finding`, and runs the case; `--selftest` runs every case of
`PLANTS` over one scratch through `loop_lib.run_selftest_cases`.

WHAT THIS DOES NOT CHECK: that an upstream item precedes the item in the needs graph; that a row's text
says anything true or a `bypassed` reason is a good one; that the measurement record measured the edge it
names, since the check reads one line of it; and that a role was told to write its `## Establishes`
section, which is its build's prompt frame.
"""
import argparse
import copy
import datetime
import pathlib
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_items import read_composed_items  # noqa: E402
from loop_lib import (OUTCOMES_REF, SEG, LoopError, read_definition, read_dispositions, read_item_rows,  # noqa: E402
                      read_memory_tree, resolve_memory_root, run_selftest_cases)

SAY = "upstream"
SEP = " · "
GATES = ("record", "measured")
ENTRY_KEYS = ("item", "gate", "measured-by", "measured-line")
ESTABLISH_KINDS = ("seam", "criterion", "interface", "fork", "finding", "repair")
ANSWERS = ("used", "bypassed", "not-applicable")
FINDING = "finding"
#: The sentence a finding prints where it carries no reason of its own.
CLASS_SENTENCES = {"dropped": "no answer names it", "doubled": "two or more answers name it",
                   "invented": "no handed row carries it", "no-reason": "its reason is empty"}
#: The fixture's item, its upstream item, its finding route and its build.
FX_ITEM, FX_UP, FX_ROUTE = "item.design.unit-spec", "item.design.seams", "item.design.decompose"
FX_BUILD, FX_UNIT = "dUpstream", "FIX-dUpstream-1"
FX_MEASURED_BY = "memory/builds/dUpstream/build/2026-11-16-build-FIX-dUpstream-1-measurement.md"
FX_MEASURED_LINE = "## Verdict: CLEAN"
FX_ESTABLISHES = ("## Establishes\n"
                  "- seam-1 · seam · the kit resolver already finds a sibling kit\n"
                  "- must-2 · criterion · no second copy of the remote ladder\n"
                  "- iface-3 · interface · the rows file is one row per line\n")
PLANTS = {
    "clean": "every row answered used with a reason, on the measured edge",
    "drop-gating": "must-2 unanswered, on a measured edge whose record holds its line",
    "drop-recorded": "the same return on a record edge",
    "bypassed": "seam-1 bypassed with a reason, on each edge in turn",
    "invented": "a further answer for item.design.seams#seam-9",
    "doubled": "seam-1 answered twice",
    "bad-answer": "seam-1 answered skipped",
    "no-reason": "seam-1 answered used with an empty reason",
    "measured-unproven": "a measured-line its record lacks",
    "measured-untracked": "a measured-by HEAD holds no blob for, the file in the working tree alone",
    "no-establishes": "an upstream return with no ## Establishes section",
    "no-finding-route": "the item's finding outcome and route taken out",
    "record-written": "bypassed on the record edge, joined with --write --build dUpstream --unit FIX-dUpstream-1",
}
#: Each selftest case: the case, its owed exit, and the opening and needle of the line it owes.
CASES = (("clean", 0, "upstream · verdict · clean", ""),
         ("drop-gating", 1, "upstream · finding · dropped", "item.design.seams#must-2"),
         ("drop-recorded", 0, "upstream · finding · dropped", "item.design.seams#must-2"),
         ("bypassed", 0, "upstream · finding · bypassed", "item.design.seams#seam-1"),
         ("invented", 1, "upstream · finding · invented", "item.design.seams#seam-9"),
         ("doubled", 1, "upstream · finding · doubled", "item.design.seams#seam-1"),
         ("bad-answer", 1, "upstream · finding · bad-answer", "item.design.seams#seam-1"),
         ("no-reason", 1, "upstream · finding · no-reason", "item.design.seams#seam-1"),
         ("measured-unproven", 1, "upstream · refused", "measured-line"),
         ("measured-untracked", 1, "upstream · refused", "measured-by"),
         ("no-establishes", 1, "upstream · refused", "item.design.seams"),
         ("no-finding-route", 1, "upstream · refused", "item.design.unit-spec"),
         ("record-written", 0, "upstream · record", "FIX-dUpstream-1-upstream-"))


def read_return_section(text, heading):
    """The bullet rows under `## <heading>` of a return, each `- a · b · c` split into three stripped
    fields, missing ones empty, up to the next `## ` line; lines not opening `- ` are skipped. None where
    the return holds no such heading."""
    lines = text.replace("\r\n", "\n").split("\n")
    head = "## %s" % heading
    if head not in (ln.rstrip() for ln in lines):
        return None
    at = [ln.rstrip() for ln in lines].index(head) + 1
    out = []
    for ln in lines[at:]:
        if ln.startswith("## "):
            break
        if ln.startswith("- "):
            parts = [p.strip() for p in ln[2:].split(SEP, 2)]
            out.append(tuple(parts + [""] * (3 - len(parts))))
    return out


def derive_upstream_rows(item, rows, returns):
    """`[(qualified id, kind, text)]`: one row per establishes row of each upstream item's return, in entry
    order, `rows` the composed items and `returns` each upstream item's return text by its tag. ValueError
    naming the item where it is no composed item, an upstream item handed no return, a return handed for
    no upstream item, a return with no `## Establishes` section, or an establishes row that does not hold."""
    row = next((r for r in rows if r.get("tag") == item), None)
    if row is None:
        raise ValueError("%s is no composed item" % item)
    entries = row.get("upstream") or []
    ups = [e.get("item") if isinstance(e, dict) else e for e in entries]
    extra = sorted(set(returns) - set(ups))
    if extra:
        raise ValueError("a return was handed for %s, no upstream item of %s" % (", ".join(extra), item))
    out = []
    for up in ups:
        if up not in returns:
            raise ValueError("the upstream item %s of %s was handed no return" % (up, item))
        established = read_return_section(returns[up], "Establishes")
        if established is None:
            raise ValueError("the return of %s, upstream of %s, holds no ## Establishes section" % (up, item))
        seen = set()
        for rid, kind, text in established:
            if not SEG.fullmatch(rid) or kind not in ESTABLISH_KINDS or not text:
                raise ValueError("the return of %s establishes %r, not `- <row id> · <kind> · <text>` with a one-"
                                 "segment id and a kind of %s" % (up, SEP.join((rid, kind, text)),
                                                                   " ".join(ESTABLISH_KINDS)))
            if rid in seen:
                raise ValueError("the return of %s establishes the row id %s twice" % (up, rid))
            seen.add(rid)
            out.append(("%s#%s" % (up, rid), kind, text))
    return out


def check_upstream_rows(rows, root):
    """`(lines, refusals)` of every composed row's `upstream` over the tree at `root`: the count line
    `loop: upstream edges · <n> record · <m> measured`, and one refusal per entry that is no inline table,
    carries a key outside `ENTRY_KEYS`, names no composed item or one twice, gives a gate outside `GATES`,
    carries a measurement key at `record`, or at `measured` lacks one, names a `measured-by` HEAD holds no
    blob for or a `measured-line` that blob does not hold whole; and one per item with a non-empty
    `upstream` whose outcome set lacks `finding`. Git is read in one batch, and not at all with no
    `measured` entry."""
    declared = {r.get("tag") for r in rows}
    counts, refusals, wants = {g: 0 for g in GATES}, [], []
    for row in rows:
        tag, value = row.get("tag"), row.get("upstream")
        if value is None:
            continue
        if not isinstance(value, list) or not all(isinstance(e, dict) for e in value):
            refusals.append("the item %s upstream is not a list of inline tables { item = <tag>, gate = record | "
                            "measured }" % tag)
            continue
        seen = set()
        for entry in value:
            up, gate = entry.get("item"), entry.get("gate", "record")
            name = "the item %s upstream %s" % (tag, up)
            bad = sorted(k for k in entry if k not in ENTRY_KEYS)
            given = [k for k in ENTRY_KEYS[2:] if k in entry]
            unset = [k for k in ENTRY_KEYS[2:] if not (isinstance(entry.get(k), str) and entry[k].strip())]
            if bad:
                why = "carries %s, outside the keys %s" % (", ".join(bad), " ".join(ENTRY_KEYS))
            elif not isinstance(up, str) or up not in declared:
                why = "item names no composed item"
            elif up in seen:
                why = "item names an upstream item an entry before it names"
            elif gate not in GATES:
                why = "gate %r is none of %s" % (gate, " ".join(GATES))
            elif gate == "record" and given:
                why = "is at gate record and carries %s, a measured entry's key" % " and ".join(given)
            elif gate == "measured" and unset:
                why = "is at gate measured with no %s" % " and no ".join(unset)
            else:
                why = None
            seen.add(up)
            if why:
                refusals.append("%s %s" % (name, why))
                continue
            counts[gate] += 1
            if gate == "measured":
                wants.append((name, entry["measured-by"], entry["measured-line"]))
        if value:
            outcomes = row.get("outcomes")
            try:
                words = read_dispositions(KIT) if outcomes == OUTCOMES_REF else outcomes
            except LoopError:
                words = None
            if not isinstance(words, list) or FINDING not in words:
                refusals.append("the item %s hands on upstream rows and its outcome set lacks %s, the outcome a "
                                "bypassed row takes" % (tag, FINDING))
    if wants:
        try:
            read_memory_tree("tree_lib.py")
            from tree_lib import read_blobs_at
            blobs = read_blobs_at(str(root), [("HEAD", by) for _n, by, _l in wants])
        except (LookupError, ImportError, OSError) as e:
            blobs = None
            refusals += ["%s measured-by %s could not be read at HEAD: %s" % (n, by, e) for n, by, _l in wants]
        for name, by, line in wants if blobs is not None else ():
            text = blobs.get(("HEAD", by))
            if text is None:
                refusals.append("%s measured-by %s: HEAD holds no blob there" % (name, by))
            elif line not in text.split("\n"):
                refusals.append("%s measured-line %r: %s at HEAD holds no such whole line" % (name, line, by))
    return ["loop: upstream edges · %d record · %d measured" % (counts["record"], counts["measured"])], refusals


def check_upstream_answers(rows, answers, gates):
    """`(verdict, lines)` of the handed `rows`, `[(id, kind, text)]`, joined with the return's `answers`,
    `[(id, answer, reason)]`, `gates` the gate of each of the item's edges by its upstream item. Each handed
    id is answered, `dropped` or `doubled`; an answered id no handed row carries is `invented`; an answered
    row is `bad-answer` or `no-reason` where it fails, and `bypassed` is a finding. A finding is graded on
    the gate of the edge its id names, an id naming no edge on the item's strictest gate. The verdict is
    `refused` with any finding but `bypassed` on a `measured` edge, else `finding` with any, else `clean`."""
    strictest = "measured" if "measured" in gates.values() else "record"
    handed = [r[0] for r in rows]
    named = {}
    for rid, _a, _r in answers:
        named[rid] = named.get(rid, 0) + 1
    lines, findings = [], []

    def add_finding(cls, rid, why):
        findings.append((cls, rid))
        lines.append(SEP.join((SAY, "finding", cls, rid, why or CLASS_SENTENCES[cls])))

    for rid in handed:
        if not named.get(rid):
            add_finding("dropped", rid, None)
        elif named[rid] > 1:
            add_finding("doubled", rid, None)
    invented = set()
    for rid, word, reason in answers:
        if rid not in handed:
            if rid not in invented:
                invented.add(rid)
                add_finding("invented", rid, None)
            continue
        if named[rid] > 1:
            continue
        lines.append(SEP.join((SAY, rid, word, reason)))
        if word not in ANSWERS:
            add_finding("bad-answer", rid, "its answer %r is none of %s" % (word, ", ".join(ANSWERS)))
        elif not reason:
            add_finding("no-reason", rid, None)
        elif word == "bypassed":
            add_finding("bypassed", rid, reason)
    refused = any(cls != "bypassed" and gates.get(rid.partition("#")[0], strictest) == "measured"
                  for cls, rid in findings)
    verdict = "refused" if refused else FINDING if findings else "clean"
    lines.append(SEP.join((SAY, "verdict", verdict)))
    return verdict, lines


def write_upstream_record(root, build, unit, item, lines, today=None):
    """Write the join's `lines` into `<MEMORY_ROOT>/builds/<build>/build/<date>-build-<unit>-upstream-<n>.md`
    under `root`, `<n>` the next free number, created exclusively: -> its repo-relative path. ValueError
    where the slug or the id does not read, or the build has no folder."""
    read_memory_tree("build_records.py")
    from build_records import ID, SLUG
    if not SLUG.match(build):
        raise ValueError("--build %r is not a build slug" % build)
    if not re.fullmatch(ID, unit):
        raise ValueError("--unit %r is not a unit id" % unit)
    memory_root = resolve_memory_root(root)
    folder = pathlib.Path(root, memory_root, "builds", build)
    if not folder.is_dir():
        raise ValueError("%s/builds/%s/ is no build folder of this tree" % (memory_root, build))
    out = folder / "build"
    out.mkdir(exist_ok=True)
    name = re.compile(r"\d{4}-\d{2}-\d{2}-build-%s-upstream-(\d+)\.md" % re.escape(unit))
    n = max((int(m.group(1)) for p in out.iterdir() if (m := name.fullmatch(p.name))), default=0) + 1
    path = out / ("%s-build-%s-upstream-%d.md" % (today or datetime.date.today().isoformat(), unit, n))
    body = ["# %s upstream %d — %s" % (unit, n, item), "", "**Serves:** log %s" % unit, ""]
    with open(path, "x", encoding="utf-8", newline="\n") as fh:   # never over a record already there
        fh.write("\n".join(body + ["- " + ln for ln in lines]) + "\n")
    return path.relative_to(root).as_posix()


# ------------------------------------------------------------------------------------------ the plants
def build_fixture_repo():
    """A scratch repository under the host temp directory holding the build folder `dUpstream` and its
    committed measurement record: -> its path."""
    from loop_witness import remove_tree, run_fixture_git, write_fixture_files
    top = pathlib.Path(tempfile.mkdtemp(prefix="up-"))
    try:
        write_fixture_files(top, {".memory-tree.conf": "MEMORY_ROOT=memory\n",
                                  "memory/builds/%s/README.md" % FX_BUILD: "# %s\n" % FX_BUILD,
                                  FX_MEASURED_BY: "# the measurement\n\n%s\n" % FX_MEASURED_LINE})
        run_fixture_git(top, "init", "-q", "--template=")
        run_fixture_git(top, "add", "-A")
        run_fixture_git(top, "commit", "-qm", "the measurement record")
        return top
    except BaseException:
        remove_tree(top)
        raise


def run_fixture(case, top):
    """One plant over the scratch `top`, cleaned of any file a case before it left: -> the exit."""
    from loop_witness import run_fixture_git, write_fixture_files
    run_fixture_git(top, "clean", "-qfdx")
    print("%s · fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
    base = read_item_rows(*read_definition(KIT))
    answers = {"seam-1": "used · the renderer calls the resolver",
               "must-2": "not-applicable · this unit adds no remote read",
               "iface-3": "used · the verb prints one row per line"}
    extra = []
    if case == "clean":
        answers["must-2"] = "used · the unit reads no remote, as the row asks"
    elif case.startswith("drop-"):
        del answers["must-2"]
    elif case in ("bypassed", "record-written"):
        answers["seam-1"] = "bypassed · the resolver cannot see a renamed kit"
    elif case == "invented":
        extra = ["- %s#seam-9 · used · a row nobody handed" % FX_UP]
    elif case == "doubled":
        extra = ["- %s#seam-1 · not-applicable · a second answer" % FX_UP]
    elif case == "bad-answer":
        answers["seam-1"] = "skipped · the row was read"
    elif case == "no-reason":
        answers["seam-1"] = "used · "
    returned = "## Upstream\n" + "".join("- %s#%s · %s\n" % (FX_UP, k, v) for k, v in answers.items()) \
        + "".join(ln + "\n" for ln in extra)
    up_return = "## Notes\n- nothing established\n" if case == "no-establishes" else FX_ESTABLISHES
    measured = {"item": FX_UP, "gate": "measured", "measured-by": FX_MEASURED_BY, "measured-line": FX_MEASURED_LINE}
    edges = {"drop-recorded": ["record"], "record-written": ["record"], "bypassed": ["measured", "record"],
             "no-establishes": ["record"], "no-finding-route": ["record"]}.get(case, ["measured"])
    if case == "measured-unproven":
        measured["measured-line"] = "## Verdict: BLOCKED"
    elif case == "measured-untracked":
        measured["measured-by"] = FX_MEASURED_BY.replace("measurement", "untracked")
        write_fixture_files(top, {measured["measured-by"]: "%s\n" % FX_MEASURED_LINE})
    worst = 0
    for gate in edges:
        rows = copy.deepcopy(base)
        row = next(r for r in rows if r.get("tag") == FX_ITEM)
        row["upstream"] = [measured if gate == "measured" else {"item": FX_UP}]
        if case != "no-finding-route":
            row["outcomes"] = list(row["outcomes"]) + [FINDING]
            row["routes"] = dict(row["routes"], **{FINDING: FX_ROUTE})
        print("%s · fixture · edge %s" % (SAY, gate))
        lines, refusals = check_upstream_rows(rows, top)
        for line in lines:
            print(line)
        for why in refusals:
            print("%s · refused · %s" % (SAY, why))
        if refusals:
            worst = 1
            continue
        try:
            handed = derive_upstream_rows(FX_ITEM, rows, {FX_UP: up_return})
        except ValueError as e:
            print("%s · refused · %s" % (SAY, e))
            worst = 1
            continue
        verdict, lines = check_upstream_answers(handed, read_return_section(returned, "Upstream") or [], {FX_UP: gate})
        for line in lines:
            print(line)
        if case == "record-written":
            path = write_upstream_record(top, FX_BUILD, FX_UNIT, FX_ITEM, lines)
            print("%s · record · %s" % (SAY, path))
            text = (top / path).read_text(encoding="utf-8")
            lost = [ln for ln in ["**Serves:** log %s" % FX_UNIT] + ["- " + ln for ln in lines]
                    if ln not in text.split("\n")]
            if lost:
                print("%s · fixture · FAIL · the record %s lacks %s" % (SAY, path, lost[0]))
                worst = 1
        worst = max(worst, 1 if verdict == "refused" else 0)
    return worst


def run_selftest():
    """Every plant over one scratch repository: -> 0 when every case holds."""
    from loop_witness import remove_tree
    try:
        top = build_fixture_repo()
    except (LookupError, OSError, subprocess.CalledProcessError) as exc:
        print("%s · selftest · UNARMED · the scratch could not be built: %s" % (SAY, exc))
        return 2
    try:
        cases = [(c, ["--fixture", "--plant", c], owed, opening, needle) for c, owed, opening, needle in CASES]
        return run_selftest_cases(lambda argv: run_fixture(argv[2], top), cases, "%s · selftest" % SAY)
    finally:
        remove_tree(top)


# ------------------------------------------------------------------------------------------- the verbs
def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if argv == ["--selftest"]:
        return run_selftest()
    if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
        from loop_witness import remove_tree
        try:
            top = build_fixture_repo()
        except (LookupError, OSError, subprocess.CalledProcessError) as exc:
            print("%s · fixture · UNARMED · the scratch could not be built: %s" % (SAY, exc))
            return 2
        try:
            return run_fixture(argv[2], top)
        finally:
            remove_tree(top)
    ap = argparse.ArgumentParser(prog="upstream.py", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    r = sub.add_parser("rows")
    r.add_argument("item")
    r.add_argument("--return", dest="returns", action="append", default=[], metavar="ITEM=PATH")
    j = sub.add_parser("join")
    j.add_argument("item")
    j.add_argument("--rows", required=True)
    j.add_argument("--return", dest="returned", required=True)
    j.add_argument("--write", action="store_true")
    j.add_argument("--build")
    j.add_argument("--unit")
    a = ap.parse_args(argv)
    if a.verb == "join" and not a.write == bool(a.build) == bool(a.unit):
        ap.error("--write takes --build <slug> and --unit <id>, and they take --write")
    from loop_witness import read_git
    rc, top = read_git(".", "rev-parse", "--show-toplevel")
    if rc != 0 or not top:
        print("%s · refused · the working directory is in no git repository" % SAY)
        return 2
    root = pathlib.Path(top).absolute()

    def read_repo_text(value):
        p = pathlib.Path(value).absolute()
        if root not in p.parents or not p.is_file():
            raise ValueError("%s names no file inside the repository %s" % (value, root.as_posix()))
        return p.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")

    try:
        if a.verb == "rows":
            returns = {}
            for spec in a.returns:
                up, eq, path = spec.partition("=")
                if not eq or not up or up in returns:
                    raise ValueError("--return %s is not <upstream item>=<path>, each item once" % spec)
                returns[up] = read_repo_text(path)
        else:
            handed_text, returned = read_repo_text(a.rows), read_repo_text(a.returned)
        items = read_composed_items(root)
    except (ValueError, LoopError, OSError, LookupError) as e:
        print("%s · refused · %s" % (SAY, e))
        return 2
    try:
        if a.verb == "rows":
            for row in derive_upstream_rows(a.item, items, returns):
                print(SEP.join(row))
            return 0
        row = next((r for r in items if r.get("tag") == a.item), None)
        if row is None:
            raise ValueError("%s is no composed item" % a.item)
        _lines, refusals = check_upstream_rows(items, root)
        if refusals:
            raise ValueError("; ".join(refusals))
        handed = []
        for ln in (x for x in handed_text.split("\n") if x.strip()):
            parts = ln.split(SEP, 2)
            if len(parts) != 3:
                raise ValueError("the rows file line %r is not <row id> · <kind> · <text>" % ln)
            handed.append(tuple(p.strip() for p in parts))
        gates = {e["item"]: e.get("gate", "record") for e in row.get("upstream") or []}
        verdict, lines = check_upstream_answers(handed, read_return_section(returned, "Upstream") or [], gates)
    except ValueError as e:
        print("%s · refused · %s" % (SAY, e))
        return 1
    for line in lines:
        print(line)
    if a.write:
        try:
            print("%s · record · %s" % (SAY, write_upstream_record(root, a.build, a.unit, a.item, lines)))
        except (ValueError, OSError) as e:
            print("%s · refused · %s" % (SAY, e))
            return 2
    return 1 if verdict == "refused" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
