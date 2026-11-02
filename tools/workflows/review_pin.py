#!/usr/bin/env python3
"""review_pin.py — the stand-in for `review.pin`: the `preset`, `optIn` and `twin` arguments of one review call.

  python <kit>/review_pin.py --subject <path> [--subject <path> ...]
                             [--opt-in none|'<json>'] [--design-record-preset unit-spec|design-audit]
                             [--twin never|design-records|design-and-landing|always]
  # stdout: {"preset": "<literal>"} or {"preset": "<literal>", "optIn": {"<opt-in>": "<default>"}},
  #         plus "twin": "<value>" when --twin is given

It prints the arguments of ONE `tier2-review.js` spec-audit call and runs nothing. A subject is a SPEC
subject when the harness's own `SPEC_SUBJECT_PATH` matches its path, read from the `tier2-review.js`
beside this module so the predicate has one spelling; every other subject is a design record. A set
holding any spec subject maps to `unit-spec`; a set of design records alone maps to
`--design-record-preset`, whose default is `DESIGN_RECORD_PRESET`. `--opt-in` is `review.opt-in`:
`none`, the default, or a JSON object keyed by literal name whose values are `optIn` maps; `optIn` is
the entry for the chosen preset, omitted when there is none. `--twin` is `review.twin` (TOOL-dFairHearing-11),
passed through as the harness's `twin` argument and omitted when not given; its shape is the four values.

Exit 0 = printed · 2 = refused, one stderr line naming the flag or `SPEC_SUBJECT_PATH`.

WHAT IT DOES NOT CHECK: whether an `optIn` key is a shipped opt-in lens of the preset, or its value a
default of it. That membership is the harness's argument boundary, checked once there.
"""
import argparse
import json
import os
import re
import sys

PRESETS = ("unit-spec", "design-audit")
TWINS = ("never", "design-records", "design-and-landing", "always")  # the harness's TWINS, by shape only
DESIGN_RECORD_PRESET = "unit-spec"  # the replay's verdict edits this one value (shared interface S9)
SPEC_LINE = re.compile(r"^const SPEC_SUBJECT_PATH = /(.+)/\s*$")


class Refused(Exception):
    pass


def read_spec_subject_path(harness):
    """The harness's compiled `SPEC_SUBJECT_PATH`, or Refused naming it."""
    try:
        with open(harness, "rb") as fh:
            lines = fh.read().decode("utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as e:
        raise Refused("SPEC_SUBJECT_PATH: %s could not be read: %s" % (harness, e))
    for line in lines:
        m = SPEC_LINE.match(line)
        if m:
            try:
                return re.compile(m.group(1))
            except re.error as e:
                raise Refused("SPEC_SUBJECT_PATH: the line in %s is no regex this module reads: %s" % (harness, e))
    raise Refused("SPEC_SUBJECT_PATH: %s carries no `const SPEC_SUBJECT_PATH = /.../` line, so no subject "
                  "can be classed; refusing rather than guessing" % harness)


def parse_opt_in(text):
    """`None` for `none`, else the JSON object of JSON objects of strings; Refused naming `--opt-in`."""
    if text == "none":
        return None
    try:
        v = json.loads(text)
    except ValueError as e:
        raise Refused("--opt-in: %r is neither none nor JSON: %s" % (text, e))
    if not isinstance(v, dict) or not all(
            isinstance(m, dict) and all(isinstance(x, str) for x in m.values()) for m in v.values()):
        raise Refused("--opt-in: %s is not a JSON object keyed by literal name whose values are objects of "
                      "strings" % json.dumps(v))
    return v


def derive_pin(subjects, spec_path, opt_in, design_preset):
    """The one call's arguments: `preset`, then `optIn` when `opt_in` has an entry for it."""
    preset = design_preset if not any(spec_path.search(s) for s in subjects) else "unit-spec"
    out = {"preset": preset}
    if opt_in is not None and preset in opt_in:
        out["optIn"] = opt_in[preset]
    return out


def main(argv):
    p = argparse.ArgumentParser(prog="review_pin.py", description="the preset and optIn of one review call")
    p.add_argument("--subject", action="append", required=True, help="a pinned subject's path; repeat per subject")
    p.add_argument("--opt-in", default="none", help="none, or the review.opt-in JSON object")
    p.add_argument("--design-record-preset", choices=PRESETS, default=DESIGN_RECORD_PRESET)
    p.add_argument("--twin", choices=TWINS, help="the review.twin value, passed through as the `twin` argument")
    a = p.parse_args(argv[1:])
    try:
        opt_in = parse_opt_in(a.opt_in)
        spec_path = read_spec_subject_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tier2-review.js"))
    except Refused as e:
        sys.stderr.write("review_pin: REFUSED, %s\n" % e)
        return 2
    out = derive_pin(a.subject, spec_path, opt_in, a.design_record_preset)
    if a.twin is not None:
        out["twin"] = a.twin
    sys.stdout.buffer.write((json.dumps(out) + "\n").encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
