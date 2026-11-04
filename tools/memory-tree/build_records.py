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

`build_records.py read <path>` prints one record's fields and every refusal: exit 0 well-formed, 1 malformed,
2 an unreadable path.
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

FIELD = re.compile(r"^- \*\*([A-Z][a-z-]+(?: [a-z]+)?):\*\* (.+)$")     # the instrument deviations.py's
ID = r"[A-Za-z]+-[A-Za-z0-9]+-\d+"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]*$")
PRINCIPLE = re.compile(r"^principle\.p[1-9]\d*$")

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
}


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
    records = []
    for rel in sorted(p for p in read_tracked_builds(root, memory_root) if glob.fullmatch(p)):
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
    if not SLUG.match(build):
        raise ValueError(f"--build {build!r} is not a build slug")
    if not re.fullmatch(ID, unit):
        raise ValueError(f"--unit {unit!r} is not a unit id")
    if not PRINCIPLE.match(principle):
        raise ValueError(f"--principle {principle!r} is not a principle.p<n> tag")
    if expires is not None and not DATE.match(expires):
        raise ValueError(f"--expires {expires!r} is not a YYYY-MM-DD date")
    memory_root = (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/")
    folder = pathlib.Path(root, memory_root, "builds", build)
    if not folder.is_dir():
        raise ValueError(f"{memory_root}/builds/{build}/ is no build folder of this tree")
    out = folder / "build"
    stem = derive_stem("exception")
    taken = [int(m.group(1)) for p in (out.glob("*-exception-*.md") if out.is_dir() else ())
             if (m := re.fullmatch(stem + r"(\d+)\.md", p.name))]
    n = max(taken, default=0) + 1
    day = today or datetime.date.today().isoformat()
    path = out / f"{day}-build-{unit}-exception-{n}.md"
    body = [f"# {unit} exception {n} — {principle} excused for {excuses}", "",
            f"**Serves:** exception {unit}", "",
            f"- **Principle:** {principle}", f"- **Excuses:** {excuses}", f"- **Reason:** {reason}"]
    if expires is not None:
        body.append(f"- **Expires:** {expires}")
    body.append(f"- **Caused-by:** {unit}")
    out.mkdir(exist_ok=True)
    with open(path, "x", encoding="utf-8", newline="\n") as fh:   # never over a record already there
        fh.write("\n".join(body) + "\n")
    return path.relative_to(root).as_posix()


def main(argv):
    ap = argparse.ArgumentParser(prog="build_records.py", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    new = sub.add_parser("new", help="write the next record of a kind through its door")
    new.add_argument("kind", choices=["exception"])
    new.add_argument("--build", required=True)
    new.add_argument("--unit", required=True)
    new.add_argument("--principle", required=True)
    new.add_argument("--excuses", required=True)
    new.add_argument("--reason", required=True)
    new.add_argument("--expires")
    new.add_argument("--root", default=".")
    read = sub.add_parser("read", help="read one record and name every refusal")
    read.add_argument("path")
    args = ap.parse_args(argv)
    if args.verb == "new":
        root = pathlib.Path(args.root).absolute()
        try:
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
    if kind == "deviation":
        import deviation_join  # noqa: E402  the deviation kind's own rules live with its join
        bad = deviation_join.read_record(rel, text)["malformed"]
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
