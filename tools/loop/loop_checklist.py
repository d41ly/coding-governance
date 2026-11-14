#!/usr/bin/env python3
"""loop_checklist.py — each core checklist handle mapped onto the declared item it reads (TOOL-dDeclaredLoop-11).

    python loop_checklist.py check                # the map, both ways, against the driver's registries
    python loop_checklist.py check --selftest     # check over the tree, then every plant, then show
    python loop_checklist.py --fixture --plant <case>
    python loop_checklist.py show <handle>        # the handle's registry and item tag, from the rows alone

The loop definition beside this file holds one `[[checklist]]` row per handle of the unattended driver's
`DOD_CORE` and `DIRECTIVES_CORE`, read through `loop_lib.read_checklist_rows` and graded by
`loop_lib.check_checklist_rows`. `read_core_registries` reads the two registry lines from the driver,
found through `resolve_kit_dir`, as the unattended kit's checker reads them: the first line that is
`<NAME>="<members>"` once a trailing CR and trailing whitespace are stripped, its members split on
whitespace, each handle the text before a member's first `:`. The driver is read, never sourced or run.

`check` prints one `loop: checklist <registry> · <handle> · <item>` line per row, a `loop: checklist-count`
line per registry and each refusal as `loop: refused · ...`, and exits 0, or 1 on a refusal. It exits 2
where the driver does not resolve, naming the kit and where it looked, or where a registry line is
absent or empty, never green over nothing; a definition `read_items` refuses exits 1 naming it.
`--fixture --plant <case>` runs `check` with one break of `PLANTS` made in memory on the rows or the
registries as read, never on disk, and exits 1 on the refusal the break draws. `check --selftest` runs
`check` over the tree, every plant, each owed exit 1 naming its break, and `show` on a mapped handle
and an absent one, printing PASS or FAIL per case; exit 0 only when every case holds. `show <handle>`
prints `<registry> <item>` from the rows alone, exit 2 for a handle no row maps.

WHAT THIS DOES NOT CHECK: that a pairing is the right item, a judgement per handle a review reads; that
a handle's checker word agrees with its item's witness class; the `DOD_EXTRA` and `DIRECTIVES_EXTRA`
handles, an adopter's own; and the members' fields after the handle. The unattended kit requires this
kit, so the driver read takes no descriptor edge; the leg running `check --selftest` is gov's own.
"""
import argparse
import contextlib
import io
import pathlib
import re
import sys

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import (CHECKLIST_REGISTRIES, LoopError, check_checklist_rows,  # noqa: E402
                      read_checklist_rows, read_items, resolve_kit_dir)

SAY = "loop"
#: `--plant`'s cases, each a break made in memory on the rows or the registries as read, and the text
#: its refusal must name.
PLANTS = {"missing-handle": ("a DoD handle unmapped-check added to DOD_CORE as read", "unmapped-check"),
          "stale-row": ("a row whose handle retired-check no registry holds", "retired-check"),
          "two-rows": ("a second row for gates-green", "maps already"),
          "undeclared-item": ("the gates-green row mapped onto item.deploy.nosuch", "item.deploy.nosuch"),
          "bare-item": ("the landed-via-lander row mapped onto deploy.land", "onto deploy.land,"),
          "numbered-row": ("the first row given number = 3", "the key number"),
          "bad-registry": ("a row whose registry is DOD_EXTRA", "registry DOD_EXTRA")}


def read_core_registries(kit_dir):
    """`{registry: [handles in order]}` for each of `CHECKLIST_REGISTRIES`, from the unattended driver
    found from `kit_dir`; LookupError where the driver does not resolve or read, or a line is absent or
    empty."""
    driver = resolve_kit_dir("unattended", "unattended.sh", kit_dir) / "unattended.sh"
    try:
        text = driver.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        raise LookupError("%s cannot be read: %s" % (driver.as_posix(), e))
    found = {}
    for line in text.splitlines():
        line = line.rstrip("\r").rstrip()
        for name in CHECKLIST_REGISTRIES:
            m = re.fullmatch(r'%s="(.*)"' % name, line)
            if m and name not in found:
                found[name] = [member.split(":", 1)[0] for member in m.group(1).split()]
    for name in CHECKLIST_REGISTRIES:
        if not found.get(name):
            raise LookupError("%s holds no %s=\"<members>\" line with a member: nothing to check the map "
                              "against" % (driver.as_posix(), name))
    return found


def resolve_checklist_handle(rows, handle):
    """`(registry, item)` of the first `[[checklist]]` row mapping `handle`, or None: by the handle, never
    by a position."""
    return next(((r.get("registry"), r.get("item")) for r in rows if r.get("handle") == handle), None)


def write_checklist_plant(case, rows, registries):
    """`rows` and `registries`, as read, with the break `case` names made in them, in place."""
    first = {r.get("handle"): r for r in reversed(rows)}
    if case == "missing-handle":
        registries["DOD_CORE"].append("unmapped-check")
    elif case == "stale-row":
        rows.append({"registry": "DOD_CORE", "handle": "retired-check", "item": "item.test.verdict"})
    elif case == "two-rows":
        rows.append({"registry": "DOD_CORE", "handle": "gates-green", "item": "item.deploy.land"})
    elif case == "undeclared-item":
        first["gates-green"]["item"] = "item.deploy.nosuch"
    elif case == "bare-item":
        first["landed-via-lander"]["item"] = "deploy.land"
    elif case == "numbered-row":
        rows[0]["number"] = 3
    elif case == "bad-registry":
        rows.append({"registry": "DOD_EXTRA", "handle": "site-checked", "item": "item.test.verdict"})


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="loop_checklist.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run check with one plant made in memory")
    ap.add_argument("--plant", choices=list(PLANTS))
    sub = ap.add_subparsers(dest="verb")
    chk = sub.add_parser("check", help="check the map both ways against the driver's two registries")
    chk.add_argument("--selftest", action="store_true", help="check, every plant, and show")
    shw = sub.add_parser("show", help="print a handle's registry and item tag")
    shw.add_argument("handle")
    args = ap.parse_args(argv)
    if args.fixture != bool(args.plant) or (args.fixture and args.verb):
        ap.error("--fixture takes --plant <case> and no verb")
    if args.verb == "show":
        try:
            hit = resolve_checklist_handle(read_checklist_rows(KIT), args.handle)
        except LoopError as e:
            print("%s: refused · %s" % (SAY, e))
            return 1
        if hit is None:
            print("%s: no [[checklist]] row maps the handle %s" % (SAY, args.handle))
            return 2
        print("%s %s" % hit)
        return 0
    if not args.fixture and args.verb != "check":
        ap.error("a verb, check or show, or --fixture --plant <case>")
    if args.verb == "check" and args.selftest:
        # each case: its name, its argv, the exit it owes, and the line it owes, by its opening and a needle
        cases = [("check", ["check"], 0, "%s: checklist-count" % SAY, "")]
        cases += [(p, ["--fixture", "--plant", p], 1, "%s: refused · " % SAY, PLANTS[p][1]) for p in PLANTS]
        cases += [("show gates-green", ["show", "gates-green"], 0, "DOD_CORE item.test.verdict", ""),
                  ("show nosuch", ["show", "nosuch"], 2, "%s: no [[checklist]] row" % SAY, "nosuch")]
        failed = []
        for name, case_argv, owed, opening, needle in cases:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rc = main(case_argv)
            said = out.getvalue()
            line = next((ln for ln in said.splitlines() if ln.startswith(opening) and needle in ln), None)
            if rc == owed and line:
                print("%s: checklist selftest · PASS %s · exit %d · %s" % (SAY, name, rc, line[:200]))
            else:
                failed.append(name)
                print("%s: checklist selftest · FAIL %s · exit %d, owed %d and a line %r naming %r: %s" % (
                    SAY, name, rc, owed, opening, needle, said[-400:]))
        print("%s: checklist selftest · %s · %d case(s) · %d failed%s" % (
            SAY, "FAIL" if failed else "PASS", len(cases), len(failed), (": " + " ".join(failed)) if failed else ""))
        return 1 if failed else 0
    try:
        registries = read_core_registries(KIT)
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    try:
        rows, items = read_checklist_rows(KIT), read_items(KIT)
    except LoopError as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    if args.plant:
        print("%s: fixture · plant %s · %s" % (SAY, args.plant, PLANTS[args.plant][0]))
        write_checklist_plant(args.plant, rows, registries)
    lines, refusals = check_checklist_rows(rows, registries, items)
    for line in lines:
        print(line)
    for why in refusals:
        print("%s: refused · %s" % (SAY, why))
    return 1 if refusals else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
