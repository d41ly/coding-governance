#!/usr/bin/env python3
"""asbuilt_view.py — the as-built view, rendered from the design baseline and the deviation records.

TOOL-dTrueNorth-6. THE VIEW is the file `DESIGN_VIEW` names: `DESIGN_RECORD`'s `[chain]` at
`DESIGN_BASELINE`, each deviation record's `amends` or `supersedes` row applied, each changed clause
citing its record. It is generated and never edited by hand. Its host is the build-index generator:
`gen_build_index.py --write` writes it after every other artifact, and `gen_build_index.py --check`
compares the file with its render, a hand edit joining its `build-index DRIFT` list under the `--write`
remedy and every other finding printed in an `as-built VERDICT` block, each exiting 1. The coverage
join, and later the help and atlas renders, read the view through `design_lib.read_design_view`.

It is the product successor of the bootstrap instrument `asbuilt.py` (the dClosedLoop build's records,
blob `97c8f8fb`). Until the report-switch step re-points the departures report, it renders byte for
byte what `asbuilt.py --write` renders, its head included, so `VIEW_HEAD` names the instrument: either
one may write the file and the other's `--check` stays green.

THE INPUTS, each read through the kit's one reader of it:
  - the clauses, `design_lib.read_chain_clauses` over `git show <DESIGN_BASELINE>:<DESIGN_RECORD>`;
  - the records, `deviation_join.read_records`: every `<MEMORY_ROOT>/builds/*/build/*-deviation-*.md`,
    sorted by path, each one's `**Departs from:**`, `**After:**` and `**Follow-through:**`;
  - from `DESIGN_RECORD`'s working tree, its first `**Serves:**` line, which the head carries
    verbatim, and its `Baseline:` line, compared with the pin and never rendered from (P0.1 row 5a).

THE RULE (TOOL-dTrueNorth-8, widened by TOOL-dTrueNorth-17), superseding TOOL-dTrueNorth-6's §3
non-goal and §4 Migration sentence on the view's bytes. The view's inputs are DESIGN_RECORD at
DESIGN_BASELINE, every record the instrument's glob names, read as above, and the render's code, which
renders and compares it: this file, `design_lib.py` and the host calls in `gen_build_index.py`.
A commit adding or editing a record the glob `*/build/*-deviation-*.md` matches re-renders the view
in that same commit, and so does a commit changing the render's code: `gen_build_index.py --write` is
the one writer that re-renders it, and no byte of the view is edited by hand. Check 9 holds the rule
at the commit: a staged record is a build-index input by `check_index_input`, and so is a staged path
under this kit's directory, so `--check --staged` renders rather than skips, and lists a view stale
against its inputs under `build-index DRIFT`. A `--no-verify` commit skips check 9; the full `--check`
still reads the view.
THE TRANSITION (TOOL-dTrueNorth-17). When the records and the render's code land in two passes at one
order, as TOOL-dTrueNorth-4's records and TOOL-dTrueNorth-6's render did at order 3, the second order-3
pass to land owns the transition: it runs `gen_build_index.py --write`, stages DESIGN_VIEW in its own
commit, and is dispatched with DESIGN_VIEW among its `--dispatch --writes` paths.

THE ROW is a record's `**Follow-through:**`, read as the instrument reads it:
  amends <clause id>@<hash8>                      the record's **After:** in the clause's place
  supersedes <clause id>@<hash8> by <clause id>   the new id and its **After:** in the clause's place
Its last cell cites `deviation` and the record's id, an unchanged row `baseline`.

THE HEAD (TOOL-dTrueNorth-18), `resolve_clause_rows`, superseding TOOL-dTrueNorth-6 S2's path order
for a set whose texts differ. A clause's set is the records whose `**Follow-through:**` row names it.
When every `**After:**` in the set agrees, the later file by path cites it, as the instrument's
ordering does, and the text is the shared `**After:**`, so the view keeps its bytes. When they differ, a member another member names in `**Supersedes:**`, the optional field
holding one record's stem, is superseded, and the one member left, the head, supplies the row's text
and citation whatever its path. A set left with two or more unsuperseded members, or none, is an
`unordered amends of <clause>` finding naming every member, and a `**Supersedes:**` naming a record
outside its clause's set is a finding naming both; either renders the clause's row from the baseline,
as a refused record's does. Neither path order nor a commit date decides.

THE FINDINGS, each naming its record or clause: a record departing from a clause with no amends or
supersedes row; the head rule's two, above; a record pinning a hash its clause does not carry at the
baseline; the working tree's `Baseline:` line differing from the pin, the view still rendering from
the pin; and under `--check`, a file differing from its render, named at its first differing line,
and a `baseline` row whose text is not the baseline's, a changed clause with no citation.

Usage (from the worktree root):
  python asbuilt_view.py --write [--out <path>]      render the view, by default to DESIGN_VIEW
  python asbuilt_view.py --check [--out <path>]      render it again and compare the bytes with the file
  python asbuilt_view.py --fixture [--plant <case>]  this tree's DESIGN_RECORD at its pin with fixture
                                                     records, in memory, damaged one way per plant
  python asbuilt_view.py --selftest                  every plant against the exit it must take
The plants: hand-edit, no-row, no-citation and baseline, ported from the instrument's, then
pin-mismatch, supersedes and amends-reader, which writes its render to a temporary file and reads it
back through `read_design_view`; then the head rule's, each record read through `read_record`:
amends-order, `…-deviation-10` naming `…-deviation-9` in `**Supersedes:**` although its path sorts
first, unordered-amends, the two with no field, same-after, two amends with one `**After:**`, and
supersedes-stray, a field naming a record of another clause. Exit 0 green, 1 on a finding, 2 when the
pin's design record cannot be read, so there is nothing to render.

OFF when DESIGN_RECORD, DESIGN_BASELINE or DESIGN_VIEW is blank, as an adopter's conf ships them: one
`as-built view: off` line naming the key, nothing read, exit 0. The host prints the same line.

What it does not read: whether a record's new text is what its approver approved, which the deviation
join and the closing review judge; a record's grammar beyond the row and the `**Supersedes:**` it
gives the view, which is `deviation_join.read_record`'s; any section of the design record outside `[chain]`, which changes only
by a record of its own; DESIGN_NODES; and the departures report, which runs the instrument's
`--check` until the report-switch step.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import re
import sys
import tempfile

KIT = os.path.dirname(os.path.abspath(__file__))
if KIT not in sys.path:
    sys.path.insert(0, KIT)
from deviation_join import read_baseline_line, read_record, read_records  # noqa: E402  the record grammar's one reader
from design_lib import (  # noqa: E402  the one parser of the design
    DESIGN_KEYS, VIEW_ROW, DesignRefusal, derive_clause_hash, read_chain_clauses, read_design_view, read_repo_root,
    run_git)
from tree_lib import parse_conf  # noqa: E402

SAY = "as-built view"
VIEW_KEYS = DESIGN_KEYS[:3]     # DESIGN_RECORD, DESIGN_BASELINE, DESIGN_VIEW: the view reads no owned node
_CL = r"cl-d[A-Z]\w+-\d{4}"
ROW_FOLLOW = re.compile(r"(amends|supersedes) (" + _CL + r")@([0-9a-f]{8})(?: by (" + _CL + r"))?")   # asbuilt.py:59
ROW_DEPARTS = re.compile(r"`?(" + _CL + r")@")                                                          # asbuilt.py:60
# The instrument's own head (asbuilt.py:72-76), its three slots the **Serves:** line, the pin and the
# record count. It names the instrument until the report-switch step's follow-on re-points it (§8 F2).
VIEW_HEAD = ("# As built: the design at its baseline, with its deviations\n\n{serves}\n\n"
             "Generated by `build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py` from v2's `[chain]` at `{sha}` and "
             "{count} deviation records. Never edit it by hand: `--check` renders it again and compares the bytes.")
ORDER_PLANTS = ("amends-order", "unordered-amends", "same-after", "supersedes-stray")    # TOOL-dTrueNorth-18's
PLANTS = ("hand-edit", "no-row", "no-citation", "baseline", "pin-mismatch", "supersedes", "amends-reader") + ORDER_PLANTS
PLANT_EXITS = {None: 0, "hand-edit": 1, "no-row": 1, "no-citation": 1, "baseline": 1, "pin-mismatch": 1,
               "supersedes": 0, "amends-reader": 0, "amends-order": 0, "unordered-amends": 1, "same-after": 0,
               "supersedes-stray": 1}
SUCCESSOR = "cl-dClosedLoop-9999"     # the supersedes plant's new id, which the pin's [chain] must not hold
LOOSENED = "cl-dClosedLoop-0119"      # the baseline plant's clause, the instrument's (asbuilt.py:110)
# The head rule's two records, older first: by path `…-deviation-10` sorts before `…-deviation-9`.
ORDER_IDS = tuple(f"2026-10-21-build-FIX-dTrueNorth-18-deviation-{n}" for n in (9, 10))
BASELINE_NOTE = "the row is the baseline's text, citing none"
# What a plant's lines must carry, so an arm holds for its own reason and not another's.
PLANT_NEEDLES = {None: ("findings 0 · view at",), "hand-edit": ("differs from its render from line",),
                 "no-row": ("fixture-deviation-3: departs from", "carries no amends or supersedes row"),
                 "no-citation": ("its text differs from the baseline's and cites no record",),
                 "baseline": ("its Baseline: line moved from", f"{LOOSENED} renders the pin's text"),
                 "pin-mismatch": ("fixture-deviation-5: pins", "and the baseline's clause hashes"),
                 "supersedes": (f"superseded by {SUCCESSOR}",),
                 "amends-reader": ("derive_clause_hash of its **After:** is", "since `deviation fixture-deviation-1`"),
                 "amends-order": (f"{ORDER_IDS[1]} supersedes {ORDER_IDS[0]} and supplies the row's **After:** and "
                                  "citation, though its path sorts first",),
                 "unordered-amends": ("unordered amends of ", f"{ORDER_IDS[1]}, {ORDER_IDS[0]} give it differing",
                                      BASELINE_NOTE),
                 "same-after": (f"two amends with one **After:** cite the later path, {ORDER_IDS[0]}",),
                 "supersedes-stray": (f"{ORDER_IDS[0]}: its **Supersedes:** names {ORDER_IDS[1]}, no amends of",
                                      BASELINE_NOTE)}


def read_view_state(conf):
    """`(armed, line)`: armed only when the three keys the view reads are all declared, else the one off
    line naming each blank key. It reads no file and makes no git call, so the host prints it for free."""
    blank = [k for k in VIEW_KEYS if not str(conf.get(k) or "").strip()]
    if not blank:
        return True, ""
    return False, (f"{SAY}: off — {', '.join(blank)} {'is' if len(blank) == 1 else 'are'} blank in "
                   ".memory-tree.conf, so nothing is read and no view is rendered")


def check_baseline(text, pin, record):
    """The finding when the `Baseline:` line of `text`, a design record's working tree, differs from the
    pin, else None; a record with no such line has moved it to none (`deviations.py:185-190`)."""
    line = read_baseline_line(text)
    if line and pin.startswith(line):
        return None
    return (f"{record}: its Baseline: line moved from {pin[:9]} to {line[:9] if line else 'none'}, and the view "
            "renders from the pin; only the owner's re-pin of DESIGN_BASELINE moves it")


def read_view_inputs(root, conf):
    """`(sha, clauses, records, serves, findings)`, everything the view renders from (S1).

    `sha` is DESIGN_BASELINE; `clauses` are `read_chain_clauses` over DESIGN_RECORD at that commit,
    `(build, clause id, text, hash8)` in row order; `records` are `read_records`, sorted by path;
    `serves` is the first `**Serves:**` line of DESIGN_RECORD's working tree, verbatim; and `findings`
    holds its moved `Baseline:` line. A blank key, a pin naming no commit, a record absent at the pin or
    holding no `[chain]` there, and a working tree that cannot be read are each a `DesignRefusal`: there
    is nothing to render.
    """
    armed, line = read_view_state(conf)
    if not armed:
        raise DesignRefusal(line, blank=[k for k in VIEW_KEYS if not str(conf.get(k) or "").strip()])
    record, sha = (str(conf[k]).strip() for k in ("DESIGN_RECORD", "DESIGN_BASELINE"))
    if run_git(root, "cat-file", "-e", f"{sha}^{{commit}}").returncode:
        raise DesignRefusal(f"DESIGN_BASELINE {sha} names no commit, so the view has no baseline to render")
    pinned = run_git(root, "show", f"{sha}:{record}")
    if pinned.returncode:
        raise DesignRefusal(f"DESIGN_RECORD {record} is absent at DESIGN_BASELINE {sha[:9]}, so the view has no "
                            "clause to render")
    clauses = read_chain_clauses(pinned.stdout.decode("utf-8", "replace"), f"{record} at {sha[:9]}")
    try:
        now = (pathlib.Path(root) / record).read_bytes().decode("utf-8").replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as exc:
        raise DesignRefusal(f"DESIGN_RECORD {record} cannot be read in the working tree, so the view's head has "
                            f"no **Serves:** line to carry: {exc}") from None
    serves = re.search(r"^\*\*Serves:\*\*.*$", now, flags=re.M)
    moved = check_baseline(now, sha, record)
    return sha, clauses, read_records(root, conf), serves.group(0) if serves else "", [moved] if moved else []


def resolve_clause_rows(records):
    """`(changes, findings)`: each clause the head rule gives a record's row, mapped to that row's
    `(pinned hash8, new id or None, **After:**, record id)`, and the findings (TOOL-dTrueNorth-18 S2, S3).

    A record departing from a clause with no `amends` or `supersedes` row is a finding and joins no set.
    A clause's set is the records whose `**Follow-through:**` row names it, in `records`' path order.
    When every `**After:**` in it agrees, the later file by path cites the shared text, as the
    instrument's ordering does; when they differ, the head supplies the row, the one member no other
    names in `**Supersedes:**`, whatever its path. Two or more such members or none is an `unordered
    amends of <clause>` finding naming every member, and a `**Supersedes:**` naming a record outside the
    set is a finding naming both; either leaves the clause out of `changes`, so it renders the baseline.
    """
    findings, sets, changes = [], {}, {}
    for r in records:
        row = ROW_FOLLOW.match(r.get("follow") or "")
        departs = ROW_DEPARTS.match(r.get("departs") or "")
        if departs and not row:
            findings.append(f"{r['id']}: departs from {departs.group(1)} and carries no amends or supersedes row")
            continue
        if row:
            sets.setdefault(row.group(2), []).append((r, row))
    for cid, members in sets.items():
        ids = [r["id"] for r, _row in members]
        stray = [(r["id"], r["supersedes"]) for r, _row in members
                 if r.get("supersedes") and r["supersedes"] not in ids]
        for rid, named in stray:
            findings.append(f"{rid}: its **Supersedes:** names {named}, no amends of {cid}, whose amends are "
                            f"{', '.join(ids)}; {cid} renders its baseline row")
        head = members[-1:]
        if len({(r.get("after") or "").strip() for r, _row in members}) > 1:
            superseded = {r["supersedes"] for r, _row in members if r.get("supersedes") not in (None, r["id"])}
            head = [(r, row) for r, row in members if r["id"] not in superseded]
            if len(head) != 1:
                findings.append(f"unordered amends of {cid}: {', '.join(ids)} give it differing **After:** texts, and "
                                + (f"no **Supersedes:** orders {', '.join(r['id'] for r, _row in head)}" if head else
                                   "each is named in another's **Supersedes:**, a cycle with no head")
                                + f"; {cid} renders its baseline row")
        if stray or len(head) != 1:
            continue
        r, row = head[0]
        changes[cid] = (row.group(3), row.group(4), (r.get("after") or "").strip(), r["id"])
    return changes, findings


def render_view(sha, clauses, records, serves):
    """`(text, findings)`: the view, a port of `asbuilt.py:54-79` that keeps every byte — the head, the
    table head, one row per baseline clause, the record count over every record read, a trailing newline.

    The row each clause takes, and the findings that refuse one, are `resolve_clause_rows`'s; a record
    pinning a hash the clause does not carry at the baseline is a finding while the row still renders.
    """
    rows = []
    changes, findings = resolve_clause_rows(records)
    for build, cid, text, h in clauses:
        if cid in changes:
            pinned, new_id, after, rid = changes[cid]
            if pinned != h:
                findings.append(f"{rid}: pins {cid}@{pinned}, and the baseline's clause hashes {h}")
            rows.append(f"| {build} | `{new_id or cid}` | {after} | deviation `{rid}` |")
        else:
            rows.append(f"| {build} | `{cid}` | {text} | baseline |")
    head = VIEW_HEAD.format(serves=serves, sha=sha, count=len(records))
    return "\n".join([head, "", "| Build | Clause | Text | Since |", "|---|---|---|---|"] + rows) + "\n", findings


def check_view(body, rendered, clauses):
    """The findings of a view file's `body` against its render, a port of `asbuilt.py:82-93`: the first
    line where the two differ, a hand edit, and each row of the BODY citing `baseline` whose text is not
    its clause's at the pin, read with the instrument's row grammar (`design_lib.VIEW_ROW`)."""
    findings = []
    if body != rendered:
        a, b = body.split("\n"), rendered.split("\n")
        n = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        findings.append(f"the file differs from its render from line {n + 1} (a hand edit): "
                        f"{a[n][:90] if n < len(a) else 'EOF'}")
    texts = {cid: text for _b, cid, text, _h in clauses}
    for ln in body.split("\n"):
        m = VIEW_ROW.match(ln)
        if m and m.group(4) == "baseline" and m.group(2) in texts and m.group(3) != texts[m.group(2)]:
            findings.append(f"{m.group(2)}: its text differs from the baseline's and cites no record")
    return findings


def read_fixture_row(text, cid):
    """`(text, since cell)` of the view row carrying `cid`, or None."""
    for ln in text.split("\n"):
        m = VIEW_ROW.match(ln)
        if m and m.group(2) == cid:
            return m.group(3), m.group(4)
    return None


def build_fixture_record(stem, cid, h, after, supersedes=None):
    """A record amending `cid@h` to `after`, written in the record grammar's row fields and read back
    through `read_record`, so a head-rule plant reads `**Supersedes:**` through its one reader."""
    fields = [("Departs from", f"`{cid}@{h}` [chain]"), ("After", after), ("Follow-through", f"amends {cid}@{h}")]
    fields += [("Supersedes", supersedes)] if supersedes else []
    return read_record(f"memory/builds/dFixture/build/{stem}.md", "".join(f"- **{k}:** {v}\n" for k, v in fields))


def render_fixture(root, conf, plant=None):
    """`(body, rendered, clauses, findings, notes, sha)` of the fixture: this tree's DESIGN_RECORD at its
    pin, never a synthetic chain, with fixture records in memory and `plant`'s damage in `body`.

    The base, as the instrument's (`asbuilt.py:96-122`): the seventh clause amended, and a record
    departing from no clause. The head rule's plants amend the ninth, and the stray's named record the
    eleventh. `findings` are the render's and a plant's own observation; `notes` are what a plant
    observed holding. Nothing is written but amends-reader's temporary view.
    """
    sha, clauses, _records, serves, _moved = read_view_inputs(root, conf)
    if len(clauses) < 11 or any(c == SUCCESSOR for _b, c, _t, _h in clauses):
        raise DesignRefusal(f"the fixture plants on clauses 7, 9 and 11 of the pin's [chain], which holds "
                            f"{len(clauses)}, and on the new id {SUCCESSOR}, which it must not hold")
    _b, cid, text, h = clauses[6]
    _b, tid, ttext, th = clauses[10]
    records = [{"id": "fixture-deviation-1", "departs": f"{cid}@{h} [chain]", "follow": f"amends {cid}@{h}",
                "after": text + ", and a planted amendment"},
               {"id": "fixture-deviation-2", "departs": "missing:PLAY-dTrueNorth-2@rev-2 [acceptance]",
                "follow": "new unit missing:PLAY-dTrueNorth-7", "after": ""}]
    notes, findings = [], []
    if plant == "baseline":
        # Loosen the clause and re-point the working tree's Baseline: past it (P0.1 row 5a): the view
        # renders from the pin, and the moved line is the one finding, so no record rides along.
        record = str(conf["DESIGN_RECORD"]).strip()
        now = (pathlib.Path(root) / record).read_bytes().decode("utf-8").replace("\r\n", "\n")
        if f"`{LOOSENED}`" not in now:
            raise DesignRefusal(f"the baseline plant loosens {LOOSENED}, which {record} does not hold")
        i = now.index(f"`{LOOSENED}`")
        now = now[:i] + "loosened, so the owner is never asked, " + now[i:]
        head = run_git(root, "rev-parse", "HEAD").stdout.decode("utf-8", "replace").strip()
        now = re.sub(r"(?m)^Baseline: `[0-9a-f]+`", f"Baseline: `{head}`", now)
        moved = check_baseline(now, sha, record)
        rendered, more = render_view(sha, clauses, [], serves)
        pin = {c: t for _b, c, t, _h in clauses}.get(LOOSENED)
        loose = {c: t for _b, c, t, _h in read_chain_clauses(now, record)}.get(LOOSENED)
        row = read_fixture_row(rendered, LOOSENED)
        if pin is not None and loose != pin and row == (pin, "baseline"):
            notes.append(f"{LOOSENED} renders the pin's text, not the working tree's loosened one")
        else:
            findings.append(f"{LOOSENED} does not render the pin's text over a loosened working tree: {row}")
        return rendered, rendered, clauses, ([moved] if moved else []) + more + findings, notes, sha
    if plant == "no-row":
        records.append({"id": "fixture-deviation-3", "departs": f"{clauses[8][1]}@{clauses[8][3]} [chain]",
                        "follow": "gap gap-build-08", "after": "x"})
    elif plant == "pin-mismatch":
        wrong = "f" * 8 if th == "0" * 8 else "0" * 8
        records.append({"id": "fixture-deviation-5", "departs": f"{tid}@{wrong} [chain]",
                        "follow": f"amends {tid}@{wrong}", "after": ttext + ", pinned at a hash it never carried"})
    elif plant == "supersedes":
        records.append({"id": "fixture-deviation-4", "departs": f"{tid}@{th} [chain]",
                        "follow": f"supersedes {tid}@{th} by {SUCCESSOR}", "after": "a planted successor clause"})
    elif plant in ORDER_PLANTS:
        # Two records on the ninth clause, appended in path order as `read_records` sorts them; the
        # stray plant's second amends the eleventh instead, and the first names it.
        _b, oid, otext, oh = clauses[8]
        old, new = ORDER_IDS
        if plant == "supersedes-stray":
            pair = [build_fixture_record(old, oid, oh, otext + ", amended once", supersedes=new),
                    build_fixture_record(new, tid, th, ttext + ", amended once")]
        else:
            pair = [build_fixture_record(old, oid, oh, otext + ", amended once"),
                    build_fixture_record(new, oid, oh, otext + (", amended once" if plant == "same-after" else
                                                                ", amended again"),
                                         supersedes=old if plant == "amends-order" else None)]
        records += sorted(pair, key=lambda r: r["path"])
    rendered, more = render_view(sha, clauses, records, serves)
    body = rendered
    if plant == "hand-edit":
        body = rendered.replace("a planted amendment", "a quiet amendment")
    elif plant == "no-citation":
        body = rendered.replace("deviation `fixture-deviation-1`", "baseline")
    elif plant == "supersedes":
        row = read_fixture_row(rendered, SUCCESSOR)
        if row == ("a planted successor clause", "deviation `fixture-deviation-4`") and \
                read_fixture_row(rendered, tid) is None:
            notes.append(f"{tid} superseded by {SUCCESSOR}: its row carries the new id, the record's **After:** "
                         "and deviation `fixture-deviation-4`")
        else:
            findings.append(f"{tid}'s supersedes row does not carry {SUCCESSOR}, its **After:** and its "
                            f"citation: {row}")
    elif plant == "amends-reader":
        with tempfile.TemporaryDirectory() as tmp:
            pathlib.Path(tmp, "view.md").write_bytes(rendered.encode("utf-8"))
            got = next((r for r in read_design_view("view.md", tmp) if r[1] == cid), None)
        after = records[0]["after"]
        want = derive_clause_hash(after)
        notes.append(f"{cid}: read_design_view reads hash {got[3] if got else 'none'} and since "
                     f"`{got[4] if got else 'none'}`; derive_clause_hash of its **After:** is {want}")
        if not got or (got[2], got[3], got[4]) != (after, want, "deviation fixture-deviation-1"):
            findings.append(f"{cid}: the rendered row and read_design_view disagree on its text or its citation")
    elif plant in ORDER_PLANTS:
        row, other = read_fixture_row(rendered, oid), read_fixture_row(rendered, tid)
        bad = [f"{r['id']}: Supersedes {why}" for r in pair for field, why in r["malformed"] if field == "Supersedes"]
        sorts = [r["id"] for r in records[-2:]] == [new, old]
        held = {"amends-order": (row == (pair[1]["after"], f"deviation `{new}`") and sorts,
                                 f"{new} supersedes {old} and supplies the row's **After:** and citation, though its "
                                 "path sorts first"),
                "same-after": (row == (pair[0]["after"], f"deviation `{old}`") and sorts,
                               f"two amends with one **After:** cite the later path, {old}"),
                "unordered-amends": (row == (otext, "baseline"), BASELINE_NOTE),
                "supersedes-stray": (row == (otext, "baseline") and other == (pair[1]["after"], f"deviation `{new}`"),
                                     BASELINE_NOTE)}[plant]
        if held[0] and not bad:
            notes.append(f"{oid}: {held[1]}")
        else:
            findings.append(f"{oid}: the head rule's row is not the plant's: {row}, the eleventh clause {other}; "
                            + "; ".join(bad))
    return body, rendered, clauses, more + findings, notes, sha


def run_fixture(root, conf, plant=None):
    """`(exit, lines, live)` of one fixture run, `lines` what the CLI prints. `live` holds when the
    render gave every clause at the pin one row and, but under the baseline plant, cited the base's
    amends record, so a fixture that rendered nothing cannot pass by finding nothing."""
    body, rendered, clauses, findings, notes, sha = render_fixture(root, conf, plant)
    findings = findings + check_view(body, rendered, clauses)
    rows = sum(1 for ln in rendered.split("\n") if VIEW_ROW.match(ln))
    live = bool(clauses) and rows == len(clauses) and (plant == "baseline"
                                                       or "deviation `fixture-deviation-1`" in rendered)
    label = " · fixture" + (f" · plant {plant}" if plant else "")
    return (1 if findings else 0), ([f"{SAY}: {n}" for n in notes]
                                    + [f"{SAY}: findings {len(findings)} · view at {sha[:9]}{label}"]
                                    + [f"  {f}" for f in findings]), live


def run_plant_arms(root, conf):
    """Every plant, and the fixture with none, against the exit it must take and the lines it must
    print: `[(held, what, detail)]`. The build-index generator's self-test runs these arms too."""
    arms = []
    for plant in (None,) + PLANTS:
        want = PLANT_EXITS[plant]
        unit = "TOOL-dTrueNorth-18" if plant in ORDER_PLANTS else "TOOL-dTrueNorth-6"
        what = (f"{unit} {'plant ' + plant if plant else 'the fixture with no plant'} exits {want}, "
                f"naming {' and '.join(repr(n) for n in PLANT_NEEDLES[plant])}")
        try:
            rc, lines, live = run_fixture(root, conf, plant)
        except DesignRefusal as exc:
            arms.append((False, what, f"nothing to render: {exc}"))
            continue
        out = "\n".join(lines)
        arms.append((rc == want and live and all(n in out for n in PLANT_NEEDLES[plant]), what, out))
    return arms


def run_selftest(root, conf):
    held = 0
    arms = run_plant_arms(root, conf)
    for ok, what, detail in arms:
        held += bool(ok)
        print(f"  {'ok  ' if ok else 'FAIL'} — {what}" + ("" if ok else f"\n{detail}"))
    print(f"{SAY} selftest: {held} of {len(arms)} arm(s) held")
    return 0 if held == len(arms) else 1


def main(argv):
    ap = argparse.ArgumentParser(prog="asbuilt_view.py", description="the as-built view (TOOL-dTrueNorth-6)")
    verb = ap.add_mutually_exclusive_group(required=True)
    for flag in ("--write", "--check", "--fixture", "--selftest"):
        verb.add_argument(flag, action="store_true")
    ap.add_argument("--out", metavar="<path>")
    ap.add_argument("--plant", choices=PLANTS)
    a = ap.parse_args(argv)
    if a.plant and not a.fixture:
        ap.error("--plant takes --fixture")
    if a.out and not (a.write or a.check):
        ap.error("--out takes --write or --check")
    root = read_repo_root()
    path = root / ".memory-tree.conf"
    conf = parse_conf(path.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n"), {}) if path.is_file() else {}
    armed, line = read_view_state(conf)
    if not armed:
        print(line)
        return 0
    try:
        if a.selftest:
            return run_selftest(root, conf)
        if a.fixture:
            rc, lines, _live = run_fixture(root, conf, a.plant)
            print("\n".join(lines))
            return rc
        sha, clauses, records, serves, findings = read_view_inputs(root, conf)
    except DesignRefusal as exc:
        print(f"{SAY}: {exc}; nothing was rendered")
        return 2
    rendered, more = render_view(sha, clauses, records, serves)
    findings += more
    out = pathlib.Path(a.out) if a.out else root / str(conf["DESIGN_VIEW"]).strip()
    if a.write:
        out.write_bytes(rendered.encode("utf-8"))
        print(f"{SAY}: wrote {out.as_posix()}")
    elif not out.is_file():
        findings.append(f"{out.as_posix()} is absent, so nothing was compared: run --write")
    else:
        findings += check_view(out.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n"), rendered, clauses)
    print(f"{SAY}: findings {len(findings)} · view at {sha[:9]}")
    for f in findings:
        print(f"  {f}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
