#!/usr/bin/env python3
"""render_lenses.py — fill each `{{LENS_SLOTS}}` token of a harness template from the lens catalogue.

  python <kit>/render_lenses.py <catalogue>   # stdin: a template, stdout: it with each token filled
  python <kit>/render_lenses.py --markers <file>   # stdout: the line number of each lens-slots marker line

A workflow script has no filesystem at run time, so the review harness cannot read `lenses.toml`
itself: the install render is its one derivation, beside the four tokens the parity script fills.
A MARKER is a line ending `= [ // gov:lens-slots <literal>`, and the line after it is exactly
`{{LENS_SLOTS}}`; that line becomes every row whose `default_in` names the literal, in file order,
each as a `deriveSlotLens('<literal>', { key, brief })` slot, so the harness can swap an opt-in into
it at run time (TOOL-dFairHearing-3), each brief single-quoted with `\\` and `'` escaped. An OPT-IN
marker is a line ending `= [ // gov:lens-optins`, its next line the same token, which becomes every
`optin = true` row as `{ key, presets, brief }`. Every other byte passes through unchanged. The
literal set is DERIVED from the template's lens-slots markers and typed nowhere else.

Exit 0 = rendered · 2 = refused, one stderr line naming the row (its `key`, or its index when the key
is the fault) and the rule. The rules are numbered as this kit's README, section "The lens
catalogue", lists them.

`--markers` (TOOL-dFairHearing-23) prints, one per line, the 1-based number of every line of `<file>`
that `MARKER` matches, the one predicate finding a marked literal: the fan-out leg walks exactly those
lines, so a comment that names `gov:lens-slots` is no marker there either, and a `gov:lens-optins`
line is never printed: an opt-in literal is outside the five-slot count (TOOL-dFairHearing-27 S1).
Exit 2 when the file cannot be read as UTF-8, or below the renderer's own python floor, which
`--markers` shares, so the fan-out leg reads either refusal as its predicate not having run.

WHAT IT DOES NOT CHECK: the slot count. A sixth default row renders a sixth slot, and the fan-out leg,
`check-verifier-fanout.sh`, reds it: that leg reads what runs, and one answer to one question.
"""
import re
import sys

TOKEN = "{{LENS_SLOTS}}"
MARKER = re.compile(r"= \[ // gov:lens-slots (\S+)$")
OPTIN_MARKER = re.compile(r"= \[ // gov:lens-optins$")
FIELDS = {"key": str, "brief": str, "kinds": list, "presets": list, "default_in": list, "optin": bool}
KINDS = ("diff-review", "spec-audit")
KEY = re.compile(r"[a-z][a-z0-9-]*")
BREAKS = ("\r", "\n", " ", " ")


class Refused(Exception):
    pass


def check_python_floor():
    """Refused below the renderer's floor, which `--markers` shares (TOOL-dFairHearing-27 S23, F3 (a))."""
    if sys.version_info < (3, 11):
        raise Refused("rule 1: python %d.%d is below the 3.11 floor, which tomllib needs to read the "
                      "lens catalogue" % sys.version_info[:2])


def load_catalogue(path):
    """The catalogue's rows, or Refused naming the floor, the file or the parse (rule 1)."""
    check_python_floor()
    import tomllib
    try:
        with open(path, "rb") as fh:
            doc = tomllib.load(fh)
    except OSError as e:
        raise Refused("rule 1: the lens catalogue %s could not be read: %s" % (path, e.strerror or e))
    except tomllib.TOMLDecodeError as e:
        raise Refused("rule 1: the lens catalogue %s is not TOML: %s" % (path, e))
    extra = sorted(k for k in doc if k != "lens")
    if extra:
        raise Refused("rule 1: the lens catalogue holds the top-level key(s) %s; it holds `lens` rows "
                      "only" % ", ".join(extra))
    rows = doc.get("lens", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise Refused("rule 1: `lens` is not an array of tables; write each row as [[lens]]")
    return rows


def check_catalogue(rows, literals):
    """Refused at the first row breaking rules 2 to 10, against the literals the markers declare."""
    for i, row in enumerate(rows):
        k = row.get("key")
        who = "row `%s`" % k if isinstance(k, str) and KEY.fullmatch(k) else "row %d" % (i + 1)
        missing = [f for f in FIELDS if f not in row]
        extra = sorted(f for f in row if f not in FIELDS)
        if missing or extra:
            raise Refused("rule 2: %s %s%s%s" % (
                who, "lacks the field(s) %s" % ", ".join(missing) if missing else "",
                "; " if missing and extra else "",
                "carries the field(s) %s outside the six" % ", ".join(extra) if extra else ""))
        for f, t in FIELDS.items():
            v = row[f]
            if not isinstance(v, t) or (t is list and not all(isinstance(m, str) for m in v)):
                raise Refused("rule 2: %s's field `%s` is not a %s" % (
                    who, f, "list of strings" if t is list else t.__name__))
        if not KEY.fullmatch(row["key"]):
            raise Refused("rule 2: %s's field `key` %r breaks ^[a-z][a-z0-9-]*$" % (who, row["key"]))
        if not row["brief"]:
            raise Refused("rule 2: %s's field `brief` is empty" % who)
        if any(b in row["brief"] for b in BREAKS):
            raise Refused("rule 2: %s's field `brief` carries a CR, LF, U+2028 or U+2029; a brief is one "
                          "line inside a single-quoted JS string" % who)
        for f in ("kinds", "presets"):
            if not row[f] or len(set(row[f])) != len(row[f]):
                raise Refused("rule 3: %s's field `%s` is empty or repeats a member" % (who, f))
        bad = [k for k in row["kinds"] if k not in KINDS]
        if bad:
            raise Refused("rule 3: %s's field `kinds` names %s, outside %s" % (who, ", ".join(bad), " and ".join(KINDS)))
        bad = [p for p in row["default_in"] if p not in row["presets"]]
        if bad:
            raise Refused("rule 4: %s's field `default_in` names %s, which its `presets` does not" % (who, ", ".join(bad)))
        want = {"diff-review" if p == "diff-review" else "spec-audit" for p in row["presets"]}
        if set(row["kinds"]) != want:
            raise Refused("rule 5: %s's `kinds` %s disagrees with the kinds of its `presets`, %s" % (
                who, sorted(row["kinds"]), sorted(want)))
        if row["optin"] and not set(row["presets"]) - set(row["default_in"]):
            raise Refused("rule 10: %s is `optin = true` and names no literal outside its `default_in`, "
                          "so it has nowhere to be swapped into" % who)
    seen = set()
    named = set(literals) | {p for r in rows for p in r["presets"]}
    for row in rows:
        who = "row `%s`" % row["key"]
        for p in row["presets"]:
            if (row["key"], p) in seen:
                raise Refused("rule 6: two rows share the key `%s` and the literal %s" % (row["key"], p))
            seen.add((row["key"], p))
        if row["key"] in named:
            raise Refused("rule 7: %s's `key` equals the literal name %s" % (who, row["key"]))
        bad = [p for p in row["presets"] if p not in literals]
        if bad:
            raise Refused("rule 8: %s names the literal(s) %s, which no `gov:lens-slots` marker in the "
                          "template declares" % (who, ", ".join(bad)))
    for lit in literals:
        if not any(lit in r["default_in"] for r in rows):
            raise Refused("rule 9: the literal %s a marker declares is filled by no default row" % lit)


def render_lens_slots(text, rows):
    """`text` with every marked `{{LENS_SLOTS}}` line filled; Refused on an unmarked token (rule 11)."""
    lines = text.split("\n")
    marks = {}  # the token's line -> its literal, or None under the opt-in marker
    for i, line in enumerate(lines):
        m = MARKER.search(line)
        o = OPTIN_MARKER.search(line)
        if m or o:
            if i + 1 >= len(lines) or lines[i + 1] != TOKEN:
                raise Refused("rule 11: the marker on line %d (%s) is not followed by a line that is "
                              "exactly %s" % (i + 1, m.group(1) if m else "gov:lens-optins", TOKEN))
            marks[i + 1] = m.group(1) if m else None
    for i, line in enumerate(lines):
        if TOKEN in line and i not in marks:
            raise Refused("rule 11: %s on line %d stands without a `gov:lens-slots` marker line above "
                          "it, nor a `gov:lens-optins` one" % (TOKEN, i + 1))
    check_catalogue(rows, list(dict.fromkeys(v for v in marks.values() if v is not None)))
    out = []
    for i, line in enumerate(lines):
        if i not in marks:
            out.append(line)
            continue
        for r in rows:
            brief = r["brief"].replace("\\", "\\\\").replace("'", "\\'")
            if marks[i] is None and r["optin"]:
                out += ["  {", "    key: '%s'," % r["key"],
                        "    presets: [%s]," % ", ".join("'%s'" % p for p in r["presets"]),
                        "    brief:", "      '%s'," % brief, "  },"]
            elif marks[i] is not None and marks[i] in r["default_in"]:
                out += ["  deriveSlotLens('%s', {" % marks[i], "    key: '%s'," % r["key"], "    brief:",
                        "      '%s'," % brief, "  }),"]
    return "\n".join(out)


def read_marker_lines(text):
    """The 1-based number of each line `MARKER` matches, a trailing CR dropped (TOOL-dFairHearing-23 S35)."""
    return [i + 1 for i, line in enumerate(text.split("\n")) if MARKER.search(line.rstrip("\r"))]


def main(argv):
    if len(argv) == 3 and argv[1] == "--markers":
        try:
            check_python_floor()
        except Refused as e:
            sys.stderr.write("render_lenses: REFUSED, --markers: %s\n" % e)
            return 2
        try:
            with open(argv[2], "rb") as fh:
                text = fh.read().decode("utf-8")
        except (OSError, UnicodeDecodeError) as e:
            sys.stderr.write("render_lenses: REFUSED, --markers: %s could not be read as UTF-8: %s\n" % (argv[2], e))
            return 2
        sys.stdout.buffer.write("".join("%d\n" % n for n in read_marker_lines(text)).encode("utf-8"))
        return 0
    if len(argv) != 2:
        sys.stderr.write("usage: render_lenses.py <catalogue>   # stdin: a template, stdout: its render\n"
                         "       render_lenses.py --markers <file>   # stdout: its lens-slots marker line numbers\n")
        return 2
    try:
        try:
            text = sys.stdin.buffer.read().decode("utf-8")
        except UnicodeDecodeError as e:
            raise Refused("the template on stdin is not UTF-8: %s" % e)
        out = render_lens_slots(text, load_catalogue(argv[1]))
    except Refused as e:
        sys.stderr.write("render_lenses: REFUSED, %s\n" % e)
        return 2
    sys.stdout.buffer.write(out.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
