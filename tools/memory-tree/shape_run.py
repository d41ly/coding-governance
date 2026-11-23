#!/usr/bin/env python3
"""shape_run.py — the parser of the `review-shape` line and the conformance of the shape-run kind
(TOOL-dTotalRecall-11).

    python <prefix>/memory-tree/shape_run.py --parse-line <line>   # its fields, one `key=value` each
    python <prefix>/memory-tree/shape_run.py --parse-file <path>   # every non-empty line of a file
    python <prefix>/memory-tree/shape_run.py --check               # each shape-run record against its line

THE GRAMMAR. Every review exit prints one byte-stable `review-shape` line, rendered by the review
harness's `renderShapeLine`, and `SHAPE_RE` is that line's one grammar: the kind, round, intensity and
stage, the nine counts, `agents` and `out-tokens`, with `merged=` optional (lines before TOOL-dFairHearing-5
lack it) and the four `review.cost` fields `trigger=`, `shape=`, `efforts=` and `role-sha=` optional together
at the end (lines before TOOL-dDeclaredLoop-20 lack them). A count the stage has not produced is `-` and
stays `-`, never `0`. `SHAPE_FIELDS` is the table the regex is compiled from, and the refusal reads the
same table left to right, so a refused line names the first field whose sub-pattern does not match. The
closed words are the record factory's `SHAPE_KINDS`, `SHAPE_INTENSITIES` and `SHAPE_STAGES`.

`--parse-line` prints the fields in line order as `key=value`, a group name for a key (`out_tokens`,
`role_sha`), an absent optional field omitted, exit 0; or `shape-run: refused · <field>`, exit 2.
`--parse-file` parses every non-empty line, prints one `shape-run: refused · <field> · line <k>` per
refused line and `shape-run: <n> parsed · <m> refused`, exit 0, or 2 where `<m>` is not 0.

THE CHECK. `check_shape_runs` reads every tracked file the factory's name grammar reads as a `shape-run`
record, through `build_records.read_record` under the kind's entry; its `Caused-by` names one tracked
`<memory root>/builds/*/reviews/<stem>.md`, whose line must parse to the same value for every field either
side carries. A malformed record, a `Caused-by` naming no review or two, a review whose line is refused,
and a field whose two values differ are each one red line naming the record: exit 1. No record at all is
`shape-run: unarmed — 0 shape-run record(s), <reason>`, exit 0, announced and never a green, its reason
the `shape-run` row's `unarmed` key in the record-kind registry, read through
`record_kinds.read_record_kinds`, the reason's one home (TOOL-dTotalRecall-53 S37). Exit 2 where the
tracked population cannot be read.

WHAT IT DOES NOT CHECK: that a review exit has a shape-run record (no writer calls the door yet), that the
review record is the one its harness wrote, or a prose-wrapped line, which the strict grammar refuses.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
import build_records  # noqa: E402  the record factory: the kind's entry, its reader and its closed words
from design_lib import DesignRefusal, read_tracked_builds  # noqa: E402  the tracked population

SAY = "shape-run"
KIND = "shape-run"
LINE_HEAD = "review-shape"
UNARMED = f"{SAY}: unarmed — 0 shape-run record(s), "
_N = r"(?:\d+|-)"
#: The line's fields in line order: (the name the line spells, its sub-pattern, the optional run it belongs
#: to or None). A run's fields are present together or absent together.
SHAPE_FIELDS = (
    ("kind", "|".join(build_records.SHAPE_KINDS), None),
    ("round", r"\d+", None),
    ("intensity", "|".join(build_records.SHAPE_INTENSITIES), None),
    ("at", "|".join(build_records.SHAPE_STAGES), None),
    ("raw", _N, None), ("confirmed", _N, None), ("refuted", _N, None),
    ("merged", _N, "merged"),
    ("unverified", _N, None), ("blocker", _N, None), ("high", _N, None), ("medium", _N, None), ("low", _N, None),
    ("agents", r"\d+", None),
    ("out-tokens", r"\d+|unknown", None),
    ("trigger", r"\S+", "cost"), ("shape", r"\S+", "cost"), ("efforts", r"\S+", "cost"), ("role-sha", r"\S+", "cost"),
)


def derive_shape_pattern(fields=SHAPE_FIELDS):
    """The regex source of `fields`: `^review-shape`, each field ` <name>=(?P<group>…)`, each optional run
    wrapped in one `(?:…)?`, then `$`. A group is the name with `-` read as `_`."""
    out, run, held = [rf"^{LINE_HEAD}"], None, []
    for name, pattern, optional in list(fields) + [(None, None, None)]:
        if optional != run and held:
            out.append(f"(?:{''.join(held)})?")
            held = []
        run = optional
        if name is None:
            break
        part = f" {name}=(?P<{name.replace('-', '_')}>{pattern})"
        (held if optional else out).append(part)
    return "".join(out) + "$"


SHAPE_RE = re.compile(derive_shape_pattern())


def derive_record_field(name):
    """The record's field name of the line's `name`: its first letter upper-cased (`out-tokens` reads
    `Out-tokens`)."""
    return name[:1].upper() + name[1:]


def derive_refused_field(line):
    """The first field of `line`, left to right, that its sub-pattern does not match; `review-shape` where the
    line does not open with it, None where every field matches."""
    tokens = line.split(" ")
    if tokens[0] != LINE_HEAD:
        return LINE_HEAD
    i = 1
    runs = []
    for name, pattern, optional in SHAPE_FIELDS:
        if runs and runs[-1][0] == optional and optional is not None:
            runs[-1][1].append((name, pattern))
        else:
            runs.append((optional, [(name, pattern)]))
    for optional, fields in runs:
        if optional is not None and (i >= len(tokens) or tokens[i].partition("=")[0] != fields[0][0]):
            continue
        for name, pattern in fields:
            key, eq, value = tokens[i].partition("=") if i < len(tokens) else ("", "", "")
            if key != name or not eq or not re.fullmatch(pattern, value):
                return name
            i += 1
    if i < len(tokens):
        return tokens[i].partition("=")[0] or LINE_HEAD
    return None


def parse_shape_line(line):
    """`{group: value}` of one `review-shape` line in line order, an absent optional field omitted; or
    ValueError whose text is the first field that does not match. A trailing line ending is not part of
    the line."""
    line = line.rstrip("\r\n")
    m = SHAPE_RE.fullmatch(line)
    if not m:
        raise ValueError(derive_refused_field(line) or LINE_HEAD)
    return {g: m.group(g) for g in (name.replace("-", "_") for name, _p, _o in SHAPE_FIELDS)
            if m.group(g) is not None}


def read_shape_line(text):
    """The one column-0 `review-shape` line of a record's text, or ValueError naming none, or every such line
    with its line number where there are two or more."""
    hits = [(n, ln) for n, ln in enumerate(text.replace("\r\n", "\n").split("\n"), 1)
            if ln.startswith(LINE_HEAD + " ")]
    if not hits:
        raise ValueError(f"no column-0 {LINE_HEAD} line")
    if len(hits) > 1:
        raise ValueError(f"{len(hits)} {LINE_HEAD} lines, at lines {', '.join(str(n) for n, _l in hits)}")
    return hits[0][1]


def read_shape_record(rel, text):
    """One shape-run record read by the factory's `read_record` under the kind's entry, as `read_records`
    takes it: `path`, `build`, `n`, `malformed` and `fields`."""
    fields, bad, name = build_records.read_record(rel, text, KIND)
    return {"path": rel, "build": name.group("build") if name else None, "n": name.group("n") if name else None,
            "malformed": bad, "fields": fields}


def read_unarmed_reason(root) -> str:
    """The `shape-run` row's `unarmed` key, read through `record_kinds.read_record_kinds` at `root`
    (TOOL-dTotalRecall-53 S37): the unarmed line's reason, spelled in the registry alone. A registry that is
    absent or refused, or a row carrying no key, is said as such."""
    import record_kinds  # noqa: E402  the registry's one reader
    try:
        rows = record_kinds.read_record_kinds(root) or []
    except record_kinds.RecordKindsError as exc:
        return f"the registry's reason does not read: {exc}"
    row = next((r for r in rows if r.get("name") == KIND), None)
    reason = (row or {}).get(record_kinds.UNARMED)
    if isinstance(reason, str) and reason.strip():
        return reason.strip()
    return f"the registry's {KIND} row carries no {record_kinds.UNARMED} reason"


def check_shape_runs(root):
    """S5: every tracked shape-run record against the line of the review record its `Caused-by` names.
    -> `(lines, exit)`: 0 green or unarmed, 1 a red, 2 an unreadable population."""
    root = pathlib.Path(root)
    conf = build_records.read_design_conf(root)
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    try:
        records = build_records.read_records(root, conf, KIND, read_shape_record)
        tracked = read_tracked_builds(root, memory_root)
    except DesignRefusal as exc:
        return [f"{SAY}: refused · {exc}"], 2
    if not records:
        return [UNARMED + read_unarmed_reason(root)], 0
    review = re.compile(re.escape(memory_root) + r"/builds/[^/]+/reviews/(?P<stem>[^/]+)\.md")
    by_stem = {}
    for rel in tracked:
        m = review.fullmatch(rel)
        if m:
            by_stem.setdefault(m.group("stem"), []).append(rel)
    reds = []
    for rec in records:
        rel, fields = rec["path"], rec["fields"]
        reds += [f"{rel} · {key} {why}" for key, why in rec["malformed"]]
        stem = fields.get("Caused-by", "").strip("`")
        hits = [p for p in by_stem.get(stem, []) if pathlib.Path(root, p).is_file()]
        if len(hits) != 1:
            reds.append(f"{rel} · Caused-by {stem or '(absent)'} names "
                        + (f"{len(hits)} tracked review records, {', '.join(hits)}" if hits
                           else f"no tracked {memory_root}/builds/*/reviews/{stem or '<stem>'}.md"))
            continue
        try:
            line = parse_shape_line(read_shape_line(pathlib.Path(root, hits[0]).read_bytes().decode("utf-8", "replace")))
        except ValueError as exc:
            reds.append(f"{rel} · its review {hits[0]} gives no parsed line: {exc}")
            continue
        for name, _p, _o in SHAPE_FIELDS:
            field, said = derive_record_field(name), line.get(name.replace("-", "_"))
            have = fields.get(field)
            if have != said:
                reds.append(f"{rel} · {field} · record {have if have is not None else 'absent'} · line "
                            f"{said if said is not None else 'absent'}")
    lines = [f"{SAY}: {len(records)} shape-run record(s) graded"] + [f"{SAY}: RED {r}" for r in reds]
    lines.append(f"{SAY}: {'red' if reds else 'green'}")
    return lines, 1 if reds else 0


def main(argv):
    if len(argv) == 2 and argv[0] == "--parse-line":
        try:
            fields = parse_shape_line(argv[1])
        except ValueError as exc:
            print(f"{SAY}: refused · {exc}")
            return 2
        for key, value in fields.items():
            print(f"{key}={value}")
        return 0
    if len(argv) == 2 and argv[0] == "--parse-file":
        try:
            text = pathlib.Path(argv[1]).read_bytes().decode("utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"{SAY}: refused · {argv[1]} did not read: {exc}")
            return 2
        parsed = refused = 0
        for n, ln in enumerate(text.replace("\r\n", "\n").split("\n"), 1):
            if not ln.strip():
                continue
            try:
                parse_shape_line(ln)
                parsed += 1
            except ValueError as exc:
                refused += 1
                print(f"{SAY}: refused · {exc} · line {n}")
        print(f"{SAY}: {parsed} parsed · {refused} refused")
        return 2 if refused else 0
    if argv == ["--check"]:
        p = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, encoding="utf-8")
        if p.returncode != 0:
            print(f"{SAY}: refused · the working directory is in no git repository")
            return 2
        lines, rc = check_shape_runs(p.stdout.strip())
        for ln in lines:
            print(ln)
        return rc
    print(__doc__.split("\n\n")[1], file=sys.stderr)
    return 2


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
