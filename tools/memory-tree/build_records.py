#!/usr/bin/env python3
"""build_records.py — the typed build-folder record factory (PLAY-dOrderedCharter-7 S7, S8).

Extracted from `deviation_join.py` at its second instance, the exception kind. A typed record is one file,
`<MEMORY_ROOT>/builds/<build>/build/<date>-build-<unit id>-<kind>-<n>.md`, `<n>` unique within its build and
kind, its id the file's stem. Its fields are bold-key bullets, `- **Key:** value`, read with `FIELD`, the one
field grammar of this kit. Each kind in `KINDS` names its required fields and its closed sets;
`read_record` refuses a field given twice, a required field missing, a value outside its closed set, a
`Caused-by` that is not one id and a file name outside the grammar, naming each, and returns the fields
whatever it found. `read_records` reads a kind's TRACKED population, the one `design_lib.read_tracked_builds`
lists, and names two files of one build sharing one `<n>`. A kind's own rules ride in as hooks: the
deviation kind's `**After:**` pipe, `DEPARTS`, `FOLLOW` and `**Supersedes:**` stay in `deviation_join.py`.

THE EXCEPTION KIND and its stand-in door (S8): `build_records.py new exception --build <slug> --unit <id>
--principle <tag> --excuses <part> --reason <text> [--expires <YYYY-MM-DD>]` writes the next
`<date>-build-<unit id>-exception-<n>.md` in that build's `build/` folder of the session's own tree, its
`**Serves:** exception <unit id>`, for the session's own commit. It is the door the memory plan lists until
dTotalRecall's record door adopts it. The core gates read the register (`core.py exceptions`).

THE CHANGE KIND and its stand-in door (PLAY-dOrderedCharter-15 S7, S14): `write_change` is the one writer of a
record of an instruction unit's change, `read_changes` the register, by date, build and `<n>`, since a unit's
status is its last record. Its two callers are `instructions_edit.py` and `build_records.py new change --build
<slug> --unit <id> --tag <unit tag> --action <verb> --mark <mark> --before <pin> --after <pin> [--successor
<tag[,tag]>] [--promoted-from <source>]`, the door a build's builder records a kit manifest change through
while that command refuses every write. A pin is `none` or `<tag>@<hash8>`. `--tag` fills `Unit`, `--unit` names
the file and fills `Caused-by`, and `Proof` reads `DOOR_PROOF`, no flag, so no caller of the door claims a proof.
Two builds' same-day records of one tag order by slug, the read's known ceiling.

`build_records.py read <path>` prints one record's fields and every refusal: exit 0 well-formed, 1 malformed,
2 an unreadable path or a pending kind.

ONE KIND LIST (PLAY-dOrderedCharter-42 S2): `KINDS`' keys are `tree_lib.TYPED_RECORD_KINDS`, the kinds the
bindings reader admits and joins to their file names, and an import whose table differs from that tuple
raises naming each kind. A kind whose fields a later unit owns holds a declared-pending entry,
`{"pending": "<unit id>"}`. `build_records.py --fixture --plant typed-kinds` writes one record of every typed
kind into a scratch git repository, through `new <kind>` where the kind has a door and `write_record`
otherwise, asserts `tree_lib.read_bindings` reads each `bound` and `gen_build_index.py --print-bindings`
prints no `A` row, and asserts no door takes another door's flags: exit 0 PASS, 1 FAIL naming each failure.
"""
from __future__ import annotations

import argparse
import datetime
import pathlib
import re
import sys

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from design_lib import read_design_conf, read_tracked_builds  # noqa: E402  the tracked population
from tree_lib import TYPED_RECORD_KINDS  # noqa: E402  the reader's kind list, this table's keys

FIELD = re.compile(r"^- \*\*([A-Z][a-z-]+(?: [a-z]+)?):\*\* (.+)$")     # the instrument deviations.py's
ID = r"[A-Za-z]+-[A-Za-z0-9]+-\d+"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]*$")
PRINCIPLE = re.compile(r"^principle\.p[1-9]\d*$")
TAG = r"[a-z0-9][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+"
PIN = re.compile(TAG + r"@[0-9a-f]{8}")
CHANGE_ACTIONS = ("add", "edit", "remove", "rename", "split")   # the one list `instructions_edit.WRITE_VERBS` reads
ENDING_ACTIONS = ("remove", "rename", "split")                   # those that end a tag and so name a `Successor`
CHANGE_MARKS = ("editorial", "semantic")
PROOF = re.compile(r"tty-cli|none — \S.*")
DOOR_PROOF = "none — stand-in door"

# kind -> its required fields and its closed sets, `(field, allowed values)` in refusal order
KINDS = {
    "deviation": {
        "required": ("Departs from", "Hand-off", "Before", "After", "Cause", "Reason", "Evidence", "Risk",
                     "Approver", "Follow-through", "Caused-by"),
        "closed": (("Hand-off", ("design-to-spec", "design-revised", "spec-revised", "spec-to-code",
                                 "code-to-record")),
                   ("Cause", ("design defect", "owner ruling", "builder discovery", "review finding", "external")),
                   ("Risk", ("editorial", "additive", "stricter", "loosening", "breaking"))),
    },
    "exception": {
        "required": ("Principle", "Excuses", "Reason", "Caused-by"),
        "closed": (),
    },
    "override": {"pending": "PLAY-dOrderedCharter-2"},
    "change": {
        "required": ("Unit", "Action", "Before", "After", "Mark", "Proof", "Caused-by"),
        "closed": (("Mark", CHANGE_MARKS), ("Action", CHANGE_ACTIONS)),
    },
}
if set(KINDS) != set(TYPED_RECORD_KINDS):
    raise ImportError("build_records: the kind table and tree_lib.TYPED_RECORD_KINDS differ on "
                      + ", ".join(sorted(set(KINDS) ^ set(TYPED_RECORD_KINDS))))
DOORS = ("exception", "change")  # the kinds `new <kind>` writes; every other kind is `write_record`'s alone
PLANTS = ("typed-kinds",)


def derive_stem(kind):
    """A `kind` record's stem as a regex, its `<n>` following."""
    return r"\d{4}-\d{2}-\d{2}-build-" + ID + "-" + re.escape(kind) + "-"


def derive_record_name(kind):
    """The name grammar of a `kind` record in a build's `build/` folder, `build` and `n` its groups."""
    return re.compile(r"(?:^|/)builds/(?P<build>[^/]+)/build/" + derive_stem(kind) + r"(?P<n>\d+)\.md$")


def read_record(path, text, kind, check_line=None, check_fields=None):
    """-> (fields, malformed, name match) for one `kind` record. `check_line(key, value, next line)` returns
    the refusals of one field as it is read, `check_fields(fields)` those of the whole record before the
    `Caused-by` rule; both are a kind's own rules."""
    lines = text.replace("\r\n", "\n").split("\n")
    fields, bad, seen = {}, [], {}
    for n, ln in enumerate(lines):
        m = FIELD.match(ln)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if key in seen:
            bad.append((key, f"is given twice, at lines {seen[key]} and {n + 1}"))
            continue
        seen[key] = n + 1
        fields[key] = value
        if check_line:
            bad += check_line(key, value, lines[n + 1] if n + 1 < len(lines) else "")
    spec = KINDS[kind]
    name = derive_record_name(kind).search(path)
    if not name:
        bad.append(("file name", f"is not <date>-build-<unit id>-{kind}-<n>.md in a build's build/ folder"))
    bad += [(k, "is missing") for k in spec["required"] if k not in fields]
    for key, allowed in spec["closed"]:
        if key in fields and fields[key] not in allowed:
            bad.append((key, f"{fields[key]} is outside {' · '.join(allowed)}"))
    if check_fields:
        bad += check_fields(fields)
    if "Caused-by" in fields and not re.fullmatch(r"`?[^\s`]+`?", fields["Caused-by"]):
        bad.append(("Caused-by", f"{fields['Caused-by']} is not one id"))
    return fields, bad, name


def read_records(root, conf, kind, reader):
    """Every TRACKED `<MEMORY_ROOT>/builds/*/build/*-<kind>-*.md`, sorted by path, each read by `reader(rel,
    text)` from its working copy, a dict carrying `build`, `n` and `malformed`; two files of one build at
    one `<n>` are each malformed, naming the other. A tracked path absent from the working tree is absent."""
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    glob = re.compile(re.escape(memory_root) + r"/builds/[^/]+/build/[^/]*-" + re.escape(kind) + r"-[^/]*\.md")
    # PLAY-dOrderedCharter-70 S4: a typed kind selects by its own name grammar, so `<kind>-plan-<n>.md` of another
    # kind is never read as one; the deviation kind keeps its instrument's glob, its one explicit exception.
    named = derive_record_name(kind) if kind != "deviation" else None
    keep = (lambda p: named.search(p)) if named else glob.fullmatch
    records = []
    for rel in sorted(p for p in read_tracked_builds(root, memory_root) if keep(p)):
        p = pathlib.Path(root, rel)
        if p.is_file():
            records.append(reader(rel, p.read_bytes().decode("utf-8", "replace")))
    shared = {}
    for r in records:
        if r["n"] is not None:
            shared.setdefault((r["build"], r["n"]), []).append(r)
    for (_b, n), group in shared.items():
        for r in group if len(group) > 1 else ():
            others = ", ".join(o["path"] for o in group if o is not r)
            r["malformed"].append(("file name", f"shares {kind}-{n} with {others}"))
    return records


# -------------------------------------------------------------------------------- the exception kind
def check_exception_fields(fields):
    """The exception kind's own field rules: `Principle` a principle tag, `Expires` a date."""
    bad = []
    if "Principle" in fields and not PRINCIPLE.match(fields["Principle"].strip("`")):
        bad.append(("Principle", f"{fields['Principle']} is not a principle.p<n> tag"))
    if "Expires" in fields and not DATE.match(fields["Expires"]):
        bad.append(("Expires", f"{fields['Expires']} is not a YYYY-MM-DD date"))
    return bad


def read_exception(path, text):
    """One exception record: its fields, keyed for the core gates, and `malformed`."""
    fields, bad, name = read_record(path, text, "exception", check_fields=check_exception_fields)
    return {"id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "principle": fields.get("Principle", "").strip("`"), "excuses": fields.get("Excuses", "").strip("`"),
            "reason": fields.get("Reason"), "expires": fields.get("Expires"), "caused_by": fields.get("Caused-by"),
            "malformed": bad}


def read_exceptions(root, conf=None):
    """The exception register: every tracked exception record of `root`, read by `read_exception`."""
    return read_records(root, read_design_conf(root) if conf is None else conf, "exception", read_exception)


def write_exception(root, build, unit, principle, excuses, reason, expires=None, today=None):
    """The stand-in door: the next exception record of `build`, written under `root`'s own memory tree.
    -> its repo-relative path. Every value is validated here, the write boundary; a refusal is ValueError."""
    for name, value in (("--excuses", excuses), ("--reason", reason)):
        if not value or not value.strip() or "\n" in value or "\r" in value:
            raise ValueError(f"{name} is one non-empty line")
    if not PRINCIPLE.match(principle):
        raise ValueError(f"--principle {principle!r} is not a principle.p<n> tag")
    if expires is not None and not DATE.match(expires):
        raise ValueError(f"--expires {expires!r} is not a YYYY-MM-DD date")
    fields = [("Principle", principle), ("Excuses", excuses), ("Reason", reason)]
    if expires is not None:
        fields.append(("Expires", expires))
    fields.append(("Caused-by", unit))
    return write_record(root, build, unit, "exception", f"{principle} excused for {excuses}", fields, today)


# -------------------------------------------------------------------------------- the change kind
def check_change_fields(fields):
    """The change kind's own field rules: `Unit` a tag, the pin shapes, `Proof`, and `Successor` on an ending
    action alone: one tag on a rename, `none` on a removal, a list on a split, whose `After` holds one pin per
    successor in that order."""
    bad = []
    action, heir = fields.get("Action"), fields.get("Successor")
    if "Unit" in fields and not re.fullmatch(TAG, fields["Unit"]):
        bad.append(("Unit", f"{fields['Unit']} is no tag"))
    for key in ("Before", "After"):
        pins = fields.get(key, "none").split(",") if key == "After" and action == "split" else [fields.get(key, "none")]
        bad += [(key, f"{p} is neither none nor <tag>@<hash8>") for p in pins if p != "none" and not PIN.fullmatch(p)]
    if "Proof" in fields and not PROOF.fullmatch(fields["Proof"]):
        bad.append(("Proof", f"{fields['Proof']} is neither tty-cli nor none — <value>"))
    if action not in ENDING_ACTIONS:
        if heir is not None:
            bad.append(("Successor", f"is given on {action}, which ends no tag"))
        return bad
    if heir is None:
        return bad + [("Successor", f"is missing on {action}")]
    heirs = heir.split(",")
    if action == "remove" and heir != "none":
        bad.append(("Successor", f"{heir} on a removal, which is none"))
    if action != "remove" and not all(re.fullmatch(TAG, h) for h in heirs):
        bad.append(("Successor", f"{heir} is no tag or comma list of tags"))
    if action == "rename" and len(heirs) != 1:
        bad.append(("Successor", f"{heir} on a rename, which is one tag"))
    if action == "split" and [p.split("@")[0] for p in fields.get("After", "").split(",")] != heirs:
        bad.append(("After", f"{fields.get('After')} is not one pin per successor of {heir}, in its order"))
    return bad


def read_change(path, text):
    """One change record: its fields under their own names, the mapping `derive_status` reads, and `id`, `path`,
    `date`, `build`, `n` and `malformed`."""
    fields, bad, name = read_record(path, text, "change", check_fields=check_change_fields)
    stem = pathlib.PurePosixPath(path).stem
    return {**fields, "id": stem, "path": path, "date": stem[:10], "build": name.group("build") if name else None,
            "n": int(name.group("n")) if name else None, "malformed": bad}


def read_changes(root, conf=None):
    """The change register: every tracked change record of `root`, by date, build and `<n>` as a number."""
    records = read_records(root, read_design_conf(root) if conf is None else conf, "change", read_change)
    return sorted(records, key=lambda r: (r["date"], r["build"] or "", r["n"] or 0))


def write_change(root, build, unit, tag, action, mark, before, after, proof, successor=None, promoted_from=None,
                 today=None):
    """The one writer of a change record, under `root`'s own memory tree. -> its repo-relative path. Every value
    is validated here, the write boundary; a refusal is ValueError."""
    fields = [("Unit", tag), ("Action", action), ("Before", before), ("After", after), ("Mark", mark)]
    fields += [("Successor", successor)] * (successor is not None)
    fields += [("Proof", proof)] + [("Promoted-from", promoted_from)] * (promoted_from is not None)
    fields.append(("Caused-by", unit))
    spec, held = KINDS["change"], dict(fields)
    bad = [f"{k} is one non-empty line" for k, v in fields if not v or not v.strip() or "\n" in v or "\r" in v]
    bad += [f"{k} {held[k]} is outside {' · '.join(allowed)}" for k, allowed in spec["closed"] if held[k] not in allowed]
    bad += [f"{k} {why}" for k, why in check_change_fields(held)]
    if bad:
        raise ValueError("; ".join(bad))
    return write_record(root, build, unit, "change", f"{action} {tag}", fields, today)


def write_record(root, build, unit, kind, title, fields, today=None):
    """The record writer every door shares: the next `kind` record of `build` under `root`'s own memory tree,
    headed `# <unit> <kind> <n> — <title>`, then `**Serves:** <kind> <unit>` and each `(key, value)` of
    `fields` as a bold-key bullet. -> its repo-relative path. A refusal is ValueError."""
    if kind not in KINDS:
        raise ValueError(f"{kind!r} is not a typed kind: " + ", ".join(KINDS))
    if not SLUG.match(build):
        raise ValueError(f"--build {build!r} is not a build slug")
    if not re.fullmatch(ID, unit):
        raise ValueError(f"--unit {unit!r} is not a unit id")
    memory_root = (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/")
    folder = pathlib.Path(root, memory_root, "builds", build)
    if not folder.is_dir():
        raise ValueError(f"{memory_root}/builds/{build}/ is no build folder of this tree")
    out = folder / "build"
    stem = derive_stem(kind)
    taken = [int(m.group(1)) for p in (out.glob(f"*-{kind}-*.md") if out.is_dir() else ())
             if (m := re.fullmatch(stem + r"(\d+)\.md", p.name))]
    n = max(taken, default=0) + 1
    day = today or datetime.date.today().isoformat()
    path = out / f"{day}-build-{unit}-{kind}-{n}.md"
    body = [f"# {unit} {kind} {n} — {title}", "", f"**Serves:** {kind} {unit}", ""]
    body += [f"- **{key}:** {value}" for key, value in fields]
    out.mkdir(exist_ok=True)
    with open(path, "x", encoding="utf-8", newline="\n") as fh:   # never over a record already there
        fh.write("\n".join(body) + "\n")
    return path.relative_to(root).as_posix()


# -------------------------------------------------------------------------------- the fixture
# each door's flags over the fixture, and a flag only it takes, which every other door refuses
DOOR_ARGV = {
    "exception": (["--principle", "principle.p1", "--excuses", "the fixture", "--reason", "the typed-kinds round trip"],
                  ["--principle", "principle.p1"]),
    "change": (["--tag", "unit.fixture", "--action", "add", "--mark", "semantic", "--before", "none",
                "--after", "unit.fixture@0123abcd"], ["--tag", "unit.fixture"]),
}


def run_door(root, kind, unit, flags):
    """`new <kind>` over the fixture's build: `(exit, what it printed)`, argparse's refusal an exit too."""
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        try:
            rc = main(["new", kind, "--root", str(root), "--build", "tKinds", "--unit", unit, *flags])
        except SystemExit as exc:
            rc = exc.code
    return rc, buf.getvalue()


def run_fixture(plant):
    """`--fixture --plant typed-kinds` (PLAY-dOrderedCharter-42 S4): one record of every kind of
    `TYPED_RECORD_KINDS`, read at run time, in a build folder of a scratch git repository under the host
    temp directory, each read back `bound` as its kind and `--print-bindings` printing no `A` row, and each
    door refusing the flag only another door takes."""
    import subprocess
    import tempfile
    from deviation_join import remove_tree, set_env_aside   # noqa: E402  the kit's fixture helpers
    from tree_lib import GIT_ENV_LEAKS, read_bindings        # noqa: E402
    unit, bad, written = "ARCH-tKinds-1", [], {}
    root = pathlib.Path(tempfile.mkdtemp(prefix="br-"))
    try:
        with set_env_aside(GIT_ENV_LEAKS):
            def run_git(*args):
                return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8",
                                      check=True).stdout
            run_git("init", "-q", "--template=")
            with open(root / ".memory-tree.conf", "w", encoding="utf-8", newline="\n") as fh:
                fh.write('MEMORY_ROOT=memory\nFAMILIES="arch:ARCH"\n')
            spec = root / "memory/builds/tKinds/spec/2026-01-01-spec-ARCH-tKinds-1.md"
            spec.parent.mkdir(parents=True)
            with open(spec, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(f"# {unit} — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01 · node a · Tier-2 · "
                         "base 0123abcd\n")
            for kind in TYPED_RECORD_KINDS:
                if kind in DOORS:
                    rc, said = run_door(root, kind, unit, DOOR_ARGV[kind][0])
                    got = re.search(r"wrote (\S+)", said)
                    if rc != 0 or not got:
                        bad.append(f"{kind}: new {kind} exited {rc}")
                        continue
                    written[kind] = got.group(1)
                    for other in (d for d in DOORS if d != kind):
                        rc, said = run_door(root, kind, unit, DOOR_ARGV[kind][0] + DOOR_ARGV[other][1])
                        if rc != 2:
                            bad.append(f"{kind}: new {kind} took {other}'s {DOOR_ARGV[other][1][0]}, exiting {rc}")
                else:
                    written[kind] = write_record(root, "tKinds", unit, kind, "the typed-kinds round trip",
                                                 [("Caused-by", unit)])
            # PLAY-dOrderedCharter-70 S4: a research record whose name holds `-change-` is no change record
            research = "memory/builds/tKinds/build/2026-01-01-build-ARCH-tKinds-1-change-plan-2.md"
            with open(root / research, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(f"# {unit} — a change plan\n\n**Serves:** research {unit}\n")
            run_git("add", "-A")
            tracked = [p for p in run_git("ls-files").split("\n") if p]
            changes = [r["path"] for r in read_changes(root)]
            if research in changes or changes != [written.get("change")]:
                bad.append(f"read_changes selected {changes}, not the change record alone")
            binds = read_bindings(str(root), tracked, read_design_conf(root))
            for kind, rel in written.items():
                rec = binds.get(rel) or {"state": "absent", "kind": None, "why": "not read"}
                if rec["state"] != "bound" or rec["kind"] != kind:
                    bad.append(f"{kind}: {rel} reads {rec['state']} as {rec['kind']} — {rec['why']}")
                else:
                    print(f"build-records: {plant} · {kind} · {rel} · bound")
            p = subprocess.run([sys.executable, str(KIT / "gen_build_index.py"), "--print-bindings"], cwd=root,
                               capture_output=True, text=True, encoding="utf-8")
            lines = p.stdout.splitlines()
            if p.returncode != 0:
                bad.append(f"--print-bindings exited {p.returncode}: {(p.stdout + p.stderr).strip()[:300]}")
            bad += [f"--print-bindings printed {ln}" for ln in lines if ln.startswith("A\t")]
            # no A row is an answer only where the predicate read the records: each owes its S row
            bad += [f"--print-bindings printed no S row for {rel}" for kind, rel in written.items()
                    if not any(ln.startswith(f"S\t{rel}\t{kind}\t") for ln in lines)]
            if not written:
                bad.append("no typed kind was written, so no A row proves nothing")
    except (subprocess.CalledProcessError, OSError, ValueError) as exc:
        bad.append(f"the fixture could not be built: {exc}")
    finally:
        remove_tree(root)
    for why in bad:
        print(f"build-records: FAIL {plant} · {why}")
    if bad:
        return 1
    print(f"build-records: PASS {plant} — {len(written)} typed kinds bound, --print-bindings printed no A row")
    return 0


def main(argv):
    ap = argparse.ArgumentParser(prog="build_records.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run a plant's round trip over a scratch repository")
    ap.add_argument("--plant", choices=PLANTS)
    sub = ap.add_subparsers(dest="verb")
    new = sub.add_parser("new", help="write the next record of a kind through its door")
    doors = new.add_subparsers(dest="kind", required=True)
    for door in DOORS:
        one = doors.add_parser(door, allow_abbrev=False)
        one.add_argument("--build", required=True)
        one.add_argument("--unit", required=True)
        one.add_argument("--root", default=".")
    doors.choices["exception"].add_argument("--principle", required=True)
    doors.choices["exception"].add_argument("--excuses", required=True)
    doors.choices["exception"].add_argument("--reason", required=True)
    doors.choices["exception"].add_argument("--expires")
    change = doors.choices["change"]
    for flag in ("--tag", "--action", "--mark", "--before", "--after"):
        change.add_argument(flag, required=True)
    change.add_argument("--successor")
    change.add_argument("--promoted-from")
    read = sub.add_parser("read", help="read one record and name every refusal")
    read.add_argument("path")
    args = ap.parse_args(argv)
    if args.fixture:
        if args.verb or not args.plant:
            ap.error("--fixture takes --plant <case> and no verb")
        return run_fixture(args.plant)
    if args.plant:
        ap.error("--plant takes --fixture")
    if args.verb is None:
        ap.error("a verb, new or read, or --fixture --plant <case>")
    if args.verb == "new":
        root = pathlib.Path(args.root).absolute()
        try:
            if args.kind == "change":
                rel = write_change(root, args.build, args.unit, args.tag, args.action, args.mark, args.before,
                                   args.after, DOOR_PROOF, args.successor, args.promoted_from)
            else:
                rel = write_exception(root, args.build, args.unit, args.principle, args.excuses, args.reason,
                                      args.expires)
        except (ValueError, OSError) as exc:
            print(f"build-records: refused · {exc}", file=sys.stderr)
            return 2
        print(f"build-records: wrote {rel}")
        return 0
    rel = args.path.replace("\\", "/")
    kind = next((k for k in KINDS if derive_record_name(k).search(rel)), None)
    try:
        text = pathlib.Path(args.path).read_bytes().decode("utf-8", "replace")
    except OSError as exc:
        print(f"build-records: refused · {exc}", file=sys.stderr)
        return 2
    if kind is None:
        print(f"build-records: {rel} · malformed · file name is no typed record's: " + ", ".join(KINDS))
        return 1
    if "pending" in KINDS[kind]:
        print(f"build-records: {rel} · the {kind} kind is pending on {KINDS[kind]['pending']}, which gives it fields")
        return 2
    if kind == "deviation":
        import deviation_join  # noqa: E402  the deviation kind's own rules live with its join
        bad = deviation_join.read_record(rel, text)["malformed"]
    elif kind == "change":
        bad = read_change(rel, text)["malformed"]
    else:
        bad = read_exception(rel, text)["malformed"]
    for ln in text.replace("\r\n", "\n").split("\n"):
        if m := FIELD.match(ln):
            print(f"build-records: {rel} · {m.group(1)}: {m.group(2).strip()}")
    for key, why in bad:
        print(f"build-records: {rel} · malformed · {key} {why}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
