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

THE OVERRIDE KIND and its stand-in door (PLAY-dOrderedCharter-2 S4): `build_records.py new override --build
<slug> --unit <id> --rule <tag> --words <text> --session <id>` writes the next
`<date>-build-<unit id>-override-<n>.md`, a record of the owner setting a charter rule aside in so many words,
its fields `Rule` (the tag set aside), `Words` (the owner's words, verbatim), `Session`, `Value` (the
`charter.override` value it was taken under, read at the tree's landed revision through the policy kit's
`policy.py get`) and `Caused-by`. It refuses, exit 1 and writing nothing, under `absolute`, where no override
is taken, with any field empty, where no policy kit answers the key, and where `--rule` names no tag of the
playbook kit's practice catalogue, a practice or its `<practice>.<rule>`. It is a door the memory plan lists
until dTotalRecall's record door adopts it.

THE RED-FIX KIND, its door and its join (TOOL-aNimbleMend-9): `build_records.py new red-fix --build <slug>
--unit <id> --leg <leg name> --red-line <line> --commit <rev> --rerun <command · result>` writes the next
`<date>-build-<unit id>-red-fix-<n>.md`, the record of an inline red fix, after the fix: `Leg`, `Red line`,
`Files` and `Commit` (both derived from the commit, the sha in full), `Rerun` and `Caused-by`. It refuses,
exit 1 and writing nothing, a rev naming no commit reachable from HEAD, a commit carrying no `Red-fix:`
trailer or none naming `--leg`, and an empty text flag. `build_records.py join red-fix [--staged] [--root
<path>]` joins every `Red-fix:` commit reachable from HEAD to its record both ways, findings J1 to J6 of
`check_red_fix_join`: exit 0 clean, 1 on a finding, 2 where git or the tracked population cannot be read,
its last line a summary. A fix at HEAD with no record is printed as owed, since its record is the next
commit; `--staged` grades HEAD alone and refuses that same fix, so the commit after a fix is its record's.
NOT CHECKED: that the record is the fix's direct child, that `Rerun` or `Red line` is true, or that the leg
was red. `--fixture --plant red-fix-join` stages the door's refusals and each finding.

ONE LINE PER VALUE, at the one writer (PLAY-dOrderedCharter-49 S53): `write_record` refuses a field value
holding a CR or an LF, or opening `**<Word>:**`, before it writes anything, so no door's value forges a
field; every door's refusal exits 1, writing nothing.

`build_records.py read <path>` prints one record's fields and every refusal: exit 0 well-formed, 1 malformed,
2 an unreadable path or a pending kind.

ONE KIND LIST (PLAY-dOrderedCharter-42 S2): `KINDS`' keys are `tree_lib.TYPED_RECORD_KINDS`, the kinds the
bindings reader admits and joins to their file names, and an import whose table differs from that tuple
raises naming each kind. A kind whose fields a later unit owns holds a declared-pending entry,
`{"pending": "<unit id>"}`, which `read` and `write_record` each refuse naming the unit, the second before
any write; `--fixture --plant pending-kind` stages one in a copy of this module. `build_records.py --fixture --plant typed-kinds` writes one record of every typed
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
from tree_lib import RED_FIX_TRAILER, TYPED_RECORD_KINDS  # noqa: E402  the reader's kind list, this table's keys

FIELD = re.compile(r"^- \*\*([A-Z][a-z-]+(?: [a-z]+)?):\*\* (.+)$")     # the instrument deviations.py's
ID = r"[A-Za-z]+-[A-Za-z0-9]+-\d+"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]*$")
PRINCIPLE = re.compile(r"^principle\.p[1-9]\d*$")
TAG = r"[a-z0-9][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+"
PIN = re.compile(TAG + r"@[0-9a-f]{8}")
FORGED_FIELD = re.compile(r"^\s*\*\*[A-Za-z][A-Za-z-]*(?: [a-z]+)?:\*\*")   # a value that would read as a field
CHANGE_ACTIONS = ("add", "edit", "remove", "rename", "split")   # the one list `instructions_edit.WRITE_VERBS` reads
ENDING_ACTIONS = ("remove", "rename", "split")                   # those that end a tag and so name a `Successor`
CHANGE_MARKS = ("editorial", "semantic")
OVERRIDE_TAKEN = ("explicit-override", "live-owner-wins")   # the `charter.override` values an override is taken under
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
    "override": {
        "required": ("Rule", "Words", "Session", "Value", "Caused-by"),
        "closed": (("Value", OVERRIDE_TAKEN),),
    },
    "change": {
        "required": ("Unit", "Action", "Before", "After", "Mark", "Proof", "Caused-by"),
        "closed": (("Mark", CHANGE_MARKS), ("Action", CHANGE_ACTIONS)),
    },
    "red-fix": {
        "required": ("Leg", "Red line", "Files", "Commit", "Rerun", "Caused-by"),
        "closed": (),
    },
}
if set(KINDS) != set(TYPED_RECORD_KINDS):
    raise ImportError("build_records: the kind table and tree_lib.TYPED_RECORD_KINDS differ on "
                      + ", ".join(sorted(set(KINDS) ^ set(TYPED_RECORD_KINDS))))
DOORS = ("exception", "change", "override", "red-fix")  # the kinds `new <kind>` writes; every other kind is `write_record`'s alone
PLANTS = ("typed-kinds", "pending-kind", "red-fix-join")
SHA40 = re.compile(r"[0-9a-f]{40}")
SAY_JOIN = "build-records: red-fix join"
#: PLAY-dOrderedCharter-55 S8's `pending-kind`: the exception kind's entry staged pending, in a copy of this module
PENDING_ENTRY = ('    "exception": {\n        "required": ("Principle", "Excuses", "Reason", "Caused-by"),\n'
                 '        "closed": (),\n    },\n', '    "exception": {"pending": "ARCH-tKinds-9"},\n')


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
        if not value or not value.strip():
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
    bad = [f"{k} is one non-empty line" for k, v in fields if not v or not v.strip()]
    bad += [f"{k} {held[k]} is outside {' · '.join(allowed)}" for k, allowed in spec["closed"] if held[k] not in allowed]
    bad += [f"{k} {why}" for k, why in check_change_fields(held)]
    if bad:
        raise ValueError("; ".join(bad))
    return write_record(root, build, unit, "change", f"{action} {tag}", fields, today)


# -------------------------------------------------------------------------------- the override kind
def check_override_fields(fields):
    """The override kind's own field rule: `Rule` the tag of the rule set aside."""
    rule = fields.get("Rule", "").strip("`")
    return [("Rule", f"{fields['Rule']} is no tag")] if "Rule" in fields and not re.fullmatch(TAG, rule) else []


def read_override(path, text):
    """One override record: its fields under their own names, and `id`, `path`, `build`, `n` and `malformed`."""
    fields, bad, name = read_record(path, text, "override", check_fields=check_override_fields)
    return {**fields, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


def read_override_value(root):
    """`charter.override` at `root`'s landed revision, through the policy kit's `policy.py get`, found beside
    this kit since a kit imports no sibling. ValueError where no policy kit answers or the reader refuses."""
    from tree_lib import read_policy_value   # noqa: E402  the kit's one policy read (TOOL-aNimbleMend-8 S7)
    try:
        return read_policy_value("charter.override", root)
    except LookupError as exc:
        raise ValueError(f"charter.override cannot be read, so no override is recorded: {exc}") from None


def read_rule_tags():
    """The tags an override's `Rule` may name: each practice of the playbook kit's catalogue and each of its
    `<practice>.<rule>` tags, read beside this kit since a kit imports no sibling. ValueError where no
    catalogue reads."""
    import tomllib
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    try:
        path = resolve_kit_dir("playbook", "practices.toml", KIT) / "practices.toml"
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("practice") or []
    except (LookupError, OSError, ValueError) as exc:
        raise ValueError(f"no practice catalogue reads, so no --rule can be checked: {exc}") from None
    return {r.get("tag") for r in rows} | {f"{r.get('tag')}.{n}" for r in rows for n in r.get("rules") or ()}


def write_override(root, build, unit, rule, words, session, today=None):
    """The stand-in door: the next override record of `build`, written under `root`'s own memory tree, its
    `Value` the key's at the landed revision. -> its repo-relative path. Every value is validated here, the
    write boundary; a refusal, `absolute` among them, is ValueError."""
    for name, value in (("--words", words), ("--session", session)):
        if not value or not value.strip():
            raise ValueError(f"{name} is one non-empty line")
    if not re.fullmatch(TAG, rule or ""):
        raise ValueError(f"--rule {rule!r} is no tag")
    if rule not in read_rule_tags():
        raise ValueError(f"--rule {rule} names no practice or practice rule of the practice catalogue")
    value = read_override_value(root)
    if value not in OVERRIDE_TAKEN:
        raise ValueError(f"charter.override is {value}: the charter outranks every live instruction and no "
                         f"override is taken")
    fields = [("Rule", rule), ("Words", words), ("Session", session), ("Value", value), ("Caused-by", unit)]
    return write_record(root, build, unit, "override", f"{rule} set aside by the owner", fields, today)


# -------------------------------------------------------------------------------- the red-fix kind
def read_red_fix(path, text):
    """One red-fix record: its fields under their own names, and `id`, `path`, `build`, `n` and `malformed`.
    Its own field rule: `Commit` is a full 40-hex sha."""
    fields, bad, name = read_record(
        path, text, "red-fix",
        check_fields=lambda f: [("Commit", f"{f['Commit']} is not a full 40-hex sha")]
        if "Commit" in f and not SHA40.fullmatch(f["Commit"]) else [])
    return {**fields, "id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad}


def write_red_fix(root, build, unit, leg, red_line, commit, rerun, today=None):
    """The door: the next red-fix record of `build`, written under `root`'s own memory tree after the fix,
    its `Commit` the full sha `commit` resolves to and its `Files` that commit's paths, both read from the
    commit and never from a flag. -> its repo-relative path. Every value is validated here, the write
    boundary; a refusal, a commit that is no `Red-fix:` commit of `leg` among them, is ValueError."""
    import routed_commits   # noqa: E402  the trailer's one read; imported here so no cycle forms at load
    for name, value in (("--leg", leg), ("--red-line", red_line), ("--commit", commit), ("--rerun", rerun)):
        if not value or not value.strip():
            raise ValueError(f"{name} is one non-empty line")
    leg = leg.strip()
    try:
        got = routed_commits.run_git(root, "rev-parse", "--verify", "--quiet", "--end-of-options",
                                     commit.strip() + "^{commit}", may_fail=True)
        sha = (got or b"").decode("utf-8", "replace").strip()
        if not SHA40.fullmatch(sha) or routed_commits.run_git(root, "merge-base", "--is-ancestor", sha, "HEAD",
                                                               may_fail=True) is None:
            raise ValueError(f"--commit {commit!r} names no commit reachable from HEAD")
        fix = routed_commits.read_routed_commits(root, ["-1", sha])[0]
    except routed_commits.Refusal as exc:
        raise ValueError(str(exc)) from None
    if not fix["red_fix"]:
        raise ValueError(f"commit {sha[:8]} carries no `{RED_FIX_TRAILER}:` trailer, so it is no red fix")
    if leg not in fix["red_fix"]:
        raise ValueError(f"--leg {leg!r} is no `{RED_FIX_TRAILER}:` trailer value of {sha[:8]}, whose legs are: "
                         + " · ".join(fix["red_fix"]))
    if not fix["paths"]:
        raise ValueError(f"commit {sha[:8]} touches no path, so it has no `Files` to record")
    fields = [("Leg", leg), ("Red line", red_line), ("Files", ", ".join(sorted(fix["paths"]))), ("Commit", sha),
              ("Rerun", rerun), ("Caused-by", unit)]
    return write_record(root, build, unit, "red-fix", f"{leg} fixed in {sha[:8]}", fields, today)


def check_red_fix_join(root, staged=False):
    """`join red-fix`: every `Red-fix:` commit reachable from HEAD against every tracked red-fix record, each
    trailer value owing one record whose `Commit` is that sha and whose `Leg` is that value.
    -> (exit, lines), the last line of exit 0 and 1 a summary.

    J1 a fix commit below HEAD with a value no record answers · J2 a record whose `Commit` is no fix commit
    of the population · J3 a record whose `Leg` is no trailer value of its commit · J4 a record whose `Files`
    differs from the commit's paths · J5 two records answering one commit and leg · J6 a record malformed by
    `read_record`. A value at HEAD with no record is printed as owed and is no finding. `staged` reads HEAD
    alone: an unanswered value there is J1, J2 is not graded since the population is one commit, and a HEAD
    with no trailer is held. Exit 2 where git fails or the tracked population cannot be read; a repository
    with no commit holds an empty population."""
    import routed_commits                  # noqa: E402  imported here so no cycle forms at load
    from design_lib import DesignRefusal   # noqa: E402
    try:
        born = routed_commits.run_git(root, "rev-parse", "--verify", "--quiet", "HEAD^{commit}", may_fail=True)
        commits = routed_commits.read_routed_commits(root, ["-1", "HEAD"] if staged else ["HEAD"]) if born else []
        records = read_records(root, read_design_conf(root), "red-fix", read_red_fix)
    except (routed_commits.Refusal, DesignRefusal, OSError, ValueError) as exc:
        return 2, [f"{SAY_JOIN} · refused · {exc}"]
    head = commits[0]["sha"] if commits else None
    fixes = {c["sha"]: list(dict.fromkeys(c["red_fix"])) for c in commits if c["red_fix"]}
    paths = {c["sha"]: ", ".join(sorted(c["paths"])) for c in commits if c["red_fix"]}
    if staged and not fixes:
        return 0, [f"{SAY_JOIN} · held under --staged · HEAD carries no `{RED_FIX_TRAILER}:` trailer"]
    found, said, answers, owed = [], [], {}, 0
    for r in records:
        if r["malformed"]:
            found += [f"J6 · {r['path']} · {key} {why}" for key, why in r["malformed"]]
            continue
        sha, leg = r["Commit"], r["Leg"]
        if sha not in fixes:
            if not staged:
                found.append(f"J2 · {r['path']} · Commit {sha} is no `{RED_FIX_TRAILER}:` commit reachable from HEAD")
            continue
        if leg not in fixes[sha]:
            found.append(f"J3 · {r['path']} · Leg {leg} is no trailer value of {sha[:8]}, whose legs are: "
                         + " · ".join(fixes[sha]))
            continue
        if r["Files"] != paths[sha]:
            found.append(f"J4 · {r['path']} · Files {r['Files']} differs from {sha[:8]}'s paths: {paths[sha]}")
        answers.setdefault((sha, leg), []).append(r["path"])
    found += [f"J5 · {' · '.join(held)} · two records answer {sha[:8]} · {leg}"
              for (sha, leg), held in answers.items() if len(held) > 1]
    for sha, leg in ((s, v) for s, legs in fixes.items() for v in legs):
        if (sha, leg) in answers:
            continue
        if sha == head and not staged:   # owed and not late: the record is the next commit
            owed += 1
            said.append(f"{SAY_JOIN} · owed · {sha[:8]} · {leg}")
        else:
            found.append(f"J1 · {sha[:8]} · {leg} · the fix commit has no red-fix record")
    lines = [f"{SAY_JOIN} · {f}" for f in found] + said
    lines.append(f"{SAY_JOIN} · {len(fixes)} fix commit(s) · {len(records)} record(s) · {owed} owed")
    return (1 if found else 0), lines


def write_record(root, build, unit, kind, title, fields, today=None):
    """The record writer every door shares: the next `kind` record of `build` under `root`'s own memory tree,
    headed `# <unit> <kind> <n> — <title>`, then `**Serves:** <kind> <unit>` and each `(key, value)` of
    `fields` as a bold-key bullet. -> its repo-relative path. A refusal is ValueError."""
    if kind not in KINDS:
        raise ValueError(f"{kind!r} is not a typed kind: " + ", ".join(KINDS))
    if "pending" in KINDS[kind]:   # PLAY-dOrderedCharter-55 S8: refused before any write, as `read` refuses it
        raise ValueError(f"the {kind} kind is pending on {KINDS[kind]['pending']}, which gives it fields, so no "
                         f"record of it is written")
    if not SLUG.match(build):
        raise ValueError(f"--build {build!r} is not a build slug")
    if not re.fullmatch(ID, unit):
        raise ValueError(f"--unit {unit!r} is not a unit id")
    forged = [key for key, value in fields if "\n" in value or "\r" in value or FORGED_FIELD.match(value)]
    if forged:
        raise ValueError(f"{', '.join(forged)}: a value is one line and never opens **<Word>:**, so it cannot "
                         f"forge a field")
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
    "override": (["--rule", "practice.verify", "--words", "skip the bar on this one", "--session", "fixture"],
                 ["--rule", "practice.verify"]),
    # the fixture's first commit carries the trailer, so HEAD is a fix of this leg when the door runs
    "red-fix": (["--leg", "the fixture leg", "--red-line", "FAIL the fixture leg", "--commit", "HEAD",
                 "--rerun", "the fixture leg · green"], ["--leg", "the fixture leg"]),
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
    if plant == "pending-kind":   # PLAY-dOrderedCharter-55 S8: a copy of this module with one kind pending
        import contextlib
        import io
        import types
        try:
            source = pathlib.Path(__file__).read_text(encoding="utf-8")
            if source.count(PENDING_ENTRY[0]) != 1:
                bad.append("the exception kind's entry is not where the plant stages it")
            mod = types.ModuleType("build_records_pending")
            mod.__file__ = __file__
            try:
                exec(compile(source.replace(PENDING_ENTRY[0], PENDING_ENTRY[1]), __file__, "exec"), mod.__dict__)
                print(f"build-records: {plant} · the module imports with exception pending on ARCH-tKinds-9")
            except ImportError as exc:
                bad.append(f"the import refused a pending entry: {exc}")
                mod = None
            if mod is not None:
                folder = root / "memory/builds/tKinds/build"
                folder.mkdir(parents=True)
                (root / ".memory-tree.conf").write_text("MEMORY_ROOT=memory\n", encoding="utf-8")
                rec = folder / f"2026-01-01-build-{unit}-exception-1.md"
                rec.write_text(f"# {unit} exception 1 — t\n\n**Serves:** exception {unit}\n", encoding="utf-8")
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    rc = mod.main(["read", str(rec)])
                if rc != 2 or "pending on ARCH-tKinds-9" not in buf.getvalue():
                    bad.append(f"read exited {rc}, not 2 naming the unit: {buf.getvalue().strip()[:200]}")
                held = sorted(p.name for p in folder.iterdir())
                try:
                    mod.write_record(root, "tKinds", unit, "exception", "t", [("Caused-by", unit)])
                    bad.append("write_record wrote a pending kind")
                except ValueError as exc:
                    if "pending on ARCH-tKinds-9" not in str(exc):
                        bad.append(f"write_record refused without naming the unit: {exc}")
                if sorted(p.name for p in folder.iterdir()) != held:
                    bad.append("write_record wrote a file for a pending kind")
                print(f"build-records: {plant} · read exited {rc}; write_record refused, writing nothing")
        finally:
            remove_tree(root)
        for why in bad:
            print(f"build-records: FAIL {plant} · {why}")
        if bad:
            return 1
        print(f"build-records: PASS {plant} — the import, read and write_record each hold a pending kind")
        return 0
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
            # the override door reads `charter.override` at the landed revision, so main holds a commit
            run_git("symbolic-ref", "HEAD", "refs/heads/main")
            run_git("add", "-A")
            run_git("-c", "user.name=fx", "-c", "user.email=fx@example.invalid", "-c", "commit.gpgsign=false",
                    "commit", "-qm", "the fixture build", "-m", f"{RED_FIX_TRAILER}: {DOOR_ARGV['red-fix'][1][1]}")
            if plant == "red-fix-join":   # TOOL-aNimbleMend-9 S7: the door's refusals and each finding of the join
                leg, folder = DOOR_ARGV["red-fix"][1][1], root / "memory/builds/tKinds/build"
                door = ["--leg", leg, "--red-line", "FAIL the fixture leg", "--rerun", "the fixture leg · green"]
                cases = [0]

                def run_join(*flags):
                    p = subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve()), "join", "red-fix",
                                        "--root", str(root), *flags], capture_output=True, text=True, encoding="utf-8")
                    return p.returncode, (p.stdout + p.stderr).strip()

                def write_commit(subject, *trailers):
                    run_git("add", "-A")
                    run_git("-c", "user.name=fx", "-c", "user.email=fx@example.invalid", "-c", "commit.gpgsign=false",
                            "commit", "-qm", subject, *(x for t in trailers for x in ("-m", t)))
                    return run_git("rev-parse", "HEAD").strip()

                def check_case(case, got, rc, *needles):
                    """One case: the exit, and one printed line holding every needle."""
                    line = next((ln for ln in got[1].splitlines() if all(n in ln for n in needles)), None)
                    cases[0] += 1
                    if got[0] != rc or line is None:
                        bad.append(f"{case}: exited {got[0]}, not {rc} with one line holding {' and '.join(needles)}: "
                                   f"{got[1][:400]}")
                    print(f"build-records: {plant} · {case} · exit {got[0]} · {line}")

                fix = run_git("rev-parse", "HEAD").strip()
                check_case("owed at HEAD", run_join(), 0, "owed", fix[:8], leg)
                check_case("staged, unrecorded at HEAD", run_join("--staged"), 1, "J1", fix[:8])
                rc, said = run_door(root, "red-fix", unit, door + ["--commit", fix[:8]])
                rel = (re.search(r"wrote (\S+)", said) or [None, ""])[1]
                rec = read_red_fix(rel, (root / rel).read_bytes().decode("utf-8")) if rc == 0 and rel else {}
                files = ".memory-tree.conf, memory/builds/tKinds/spec/2026-01-01-spec-ARCH-tKinds-1.md"
                cases[0] += 1
                if rec.get("Commit") != fix or rec.get("Files") != files or rec.get("malformed"):
                    bad.append(f"door: exited {rc} from the rev {fix[:8]} and wrote Commit {rec.get('Commit')}, Files "
                               f"{rec.get('Files')}, malformed {rec.get('malformed')}: {said.strip()[:200]}")
                print(f"build-records: {plant} · door · exit {rc} · from {fix[:8]} · Commit {rec.get('Commit')} · "
                      f"Files {rec.get('Files')}")
                if not bad:
                    run_git("add", "--", rel)
                    check_case("staged, recorded at HEAD", run_join("--staged"), 0, "1 fix commit(s)")
                    plain = write_commit("the record")
                    check_case("clean", run_join(), 0, "1 fix commit(s) · 1 record(s) · 0 owed")
                    for case, flags in (("a commit with no trailer", door + ["--commit", plain[:8]]),
                                        ("a --leg no trailer names", ["--leg", "another leg", *door[2:], "--commit", fix[:8]]),
                                        ("a rev that names no commit", door + ["--commit", "no-such-rev"])):
                        rc, said = run_door(root, "red-fix", unit, flags)
                        held = len(list(folder.glob("*-red-fix-*.md")))
                        cases[0] += 1
                        if rc != 1 or held != 1:
                            bad.append(f"refusal, {case}: exited {rc}, not 1, with {held} record(s), not 1: {said.strip()[:200]}")
                        print(f"build-records: {plant} · refusal · {case} · exit {rc} · {held} record(s)")
                    text = (root / rel).read_bytes().decode("utf-8")
                    twin = rel.replace("-red-fix-1.md", "-red-fix-2.md")
                    for case, old, new, needles in (
                            ("J4", "- **Files:** .memory-tree.conf, ", "- **Files:** ", (rel,)),
                            ("J3", f"- **Leg:** {leg}", "- **Leg:** another leg", (rel, leg)),
                            ("J2", fix, "0" * 40, (rel, "0" * 40)),
                            ("J6", "- **Rerun:** the fixture leg · green\n", "", (rel, "Rerun is missing")),
                            ("J5", None, None, (rel, twin))):
                        if old is not None and old not in text:
                            bad.append(f"{case}: the record does not hold {old!r}, so the plant stages nothing")
                        with open(root / (rel if old is not None else twin), "w", encoding="utf-8", newline="\n") as fh:
                            fh.write(text.replace(old, new) if old is not None else text)
                        run_git("add", "-A")
                        check_case(case, run_join(), 1, f"· {case} ·", *needles)
                        if old is None:
                            run_git("rm", "-qf", "--", twin)
                        with open(root / rel, "w", encoding="utf-8", newline="\n") as fh:
                            fh.write(text)
                    (root / "fixed.txt").write_text("a second fix\n", encoding="utf-8")
                    late = write_commit("a second fix", f"{RED_FIX_TRAILER}: {leg}")
                    (root / "later.txt").write_text("one more commit\n", encoding="utf-8")
                    write_commit("one more commit on an unrecorded fix")
                    check_case("J1", run_join(), 1, "· J1 ·", late[:8], leg)
                for why in bad:
                    print(f"build-records: FAIL {plant} · {why}")
                if not bad:
                    print(f"build-records: PASS {plant} — {cases[0]} cases: the door, its refusals, owed, --staged "
                          f"and J1 to J6")
                return 1 if bad else 0
            try:
                read_override_value(root)
                unarmed = set()
            except ValueError as exc:
                print(f"build-records: {plant} · unarmed · the override door needs a policy kit: {exc}")
                unarmed = {"override"}
            for kind in TYPED_RECORD_KINDS:
                if kind in DOORS and kind not in unarmed:
                    rc, said = run_door(root, kind, unit, DOOR_ARGV[kind][0])
                    got = re.search(r"wrote (\S+)", said)
                    if rc != 0 or not got:
                        bad.append(f"{kind}: new {kind} exited {rc}")
                        continue
                    written[kind] = got.group(1)
                    for other in (d for d in DOORS if d not in (kind, *unarmed)):
                        rc, said = run_door(root, kind, unit, DOOR_ARGV[kind][0] + DOOR_ARGV[other][1])
                        if rc != 2:
                            bad.append(f"{kind}: new {kind} took {other}'s {DOOR_ARGV[other][1][0]}, exiting {rc}")
                else:
                    written[kind] = write_record(root, "tKinds", unit, kind, "the typed-kinds round trip",
                                                 [("Caused-by", unit)])
            # PLAY-dOrderedCharter-49 S53: a value forging a field and a --rule the catalogue lacks each refuse,
            # exit 1, naming why, and write nothing
            held = sorted(p.name for p in (root / "memory/builds/tKinds/build").glob("*.md"))
            refusals = [("exception", DOOR_ARGV["exception"][0][:4] + ["--reason", "a\nExpires: 2099-01-01"],
                         "cannot forge a field"),
                        ("override", ["--rule", "practice.verify", "--words", "**Value:** owner", "--session", "fx"],
                         "cannot forge a field"),
                        ("override", ["--rule", "practice.nosuch", "--words", "w", "--session", "fx"],
                         "names no practice or practice rule")]
            for kind, flags, why in refusals:
                if kind in unarmed:
                    continue
                rc, said = run_door(root, kind, unit, flags)
                if rc != 1 or why not in said:
                    bad.append(f"{kind}: {flags[-3:]} exited {rc}, not 1 naming `{why}`: {said.strip()[:200]}")
            if sorted(p.name for p in (root / "memory/builds/tKinds/build").glob("*.md")) != held:
                bad.append("a refused door wrote a record")
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
    for flag in ("--rule", "--words", "--session"):
        doors.choices["override"].add_argument(flag, required=True)
    for flag in ("--leg", "--red-line", "--commit", "--rerun"):
        doors.choices["red-fix"].add_argument(flag, required=True)
    read = sub.add_parser("read", help="read one record and name every refusal")
    read.add_argument("path")
    join = sub.add_parser("join", help="join every Red-fix: commit to its red-fix record, both ways")
    join.add_argument("joined", choices=("red-fix",))
    join.add_argument("--staged", action="store_true", help="grade HEAD alone against the records in the index")
    join.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    if args.fixture:
        if args.verb or not args.plant:
            ap.error("--fixture takes --plant <case> and no verb")
        return run_fixture(args.plant)
    if args.plant:
        ap.error("--plant takes --fixture")
    if args.verb is None:
        ap.error("a verb, new, read or join, or --fixture --plant <case>")
    if args.verb == "join":
        rc, lines = check_red_fix_join(pathlib.Path(args.root).absolute(), args.staged)
        if hasattr(sys.stdout, "reconfigure"):   # check 31 reads these lines: UTF-8 and LF whatever the host
            sys.stdout.reconfigure(encoding="utf-8", newline="\n")
        print("\n".join(lines))
        return rc
    if args.verb == "new":
        root = pathlib.Path(args.root).absolute()
        try:
            if args.kind == "change":
                rel = write_change(root, args.build, args.unit, args.tag, args.action, args.mark, args.before,
                                   args.after, DOOR_PROOF, args.successor, args.promoted_from)
            elif args.kind == "override":
                rel = write_override(root, args.build, args.unit, args.rule, args.words, args.session)
            elif args.kind == "red-fix":
                rel = write_red_fix(root, args.build, args.unit, args.leg, args.red_line, args.commit, args.rerun)
            else:
                rel = write_exception(root, args.build, args.unit, args.principle, args.excuses, args.reason,
                                      args.expires)
        except (ValueError, OSError) as exc:
            print(f"build-records: refused · {exc}", file=sys.stderr)
            return 1
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
    elif kind == "override":
        bad = read_override(rel, text)["malformed"]
    elif kind == "red-fix":
        bad = read_red_fix(rel, text)["malformed"]
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
