#!/usr/bin/env python3
"""gov_record.py — the one `record` write door (TOOL-dTotalRecall-2).

    python <prefix>/memory-tree/gov_record.py new <kind> --build <slug> --unit <id> --title <text>
                                              [--name <stem>] [--field <Name>=<value>]...
    python <prefix>/memory-tree/gov_record.py new build-readme <slug> --asks <IDLIST>
    python <prefix>/memory-tree/gov_record.py new spec <id> --tier 1|2 [--order <n>] [--base <sha>]

It stands in for `gov record` the way `gov_tag.py` stands in for `gov tag`, and runs in the repository at
the current directory. A kind is written here only where its `[[record-kind]]` row in `record-kinds.toml`
names `gov_record.py new <kind>` its writer: a kind with no row, or another door, exits 2 naming the
registry or that door, so a factory door's kind (`build_records.py new <kind>`) is refused naming it.

A `fields` kind is `build_records.write_new_record`: the row's template filled with each `--field`, a key
the row does not name following in the caller's order; the bytes parsed back by the kind's own check
before anything is written; a record of the kind whose content key matches is the same write, `exists`;
then the build's lease or claim is read, the id minted by the row's `id-rule` (a typed kind's `<n>`
through `write_record`, an empty rule's `--name`, a `<FAMILY>-<slug>-<seq>` counter through
`gov-claim.sh ask`, the family the unit's) and the file written and staged, never committed. A kind whose
input is not a field list takes its handler in `KIND_HANDLERS`: `build-readme` and `spec` run the
`--new-build` and `--new-spec` scaffolds of `gen_build_index.py`, imported, every flag passed through.

Exit and stdout: 0 `wrote <path> key <content key>` · 0 `exists <path> key <content key>` · 2 `refused
<kind>: <why>` · 4 `waiting offline <ref>`, nothing written. A handler prints its scaffold's lines.
WHAT IT DOES NOT CHECK: the verbs `find` and `show` (TOOL-dTotalRecall-9); a record's edges and causes
(TOOL-dTotalRecall-19); whether two builds hold a `--name` record of one stem and one content key, which
the listing reads as one write.
"""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
import build_records  # noqa: E402  the record factory this door is grown from


def run_build_readme(root, argv):
    """`new build-readme <slug> --asks <IDLIST>`: the `--new-build` scaffold, whose slug claim is its
    authority (§4 "Minting")."""
    import gen_build_index as gbi  # noqa: E402  the scaffold, imported, never copied
    return gbi.cmd_new_build(str(root), gbi.load_conf(str(root)), gbi.read_new_build_args(argv))


def run_spec(root, argv):
    """`new spec <id> --tier 1|2 [--order <n>] [--base <sha>]`: the `--new-spec` scaffold, after the build's
    lease or claim reads."""
    import gen_build_index as gbi  # noqa: E402  the scaffold, imported, never copied
    args = gbi.read_new_spec_args(argv)
    parts = args["id"].split("-")
    if len(parts) >= 3:
        for line in build_records.check_mint_authority(root, "-".join(parts[1:-1])):
            print(line)
    return gbi.cmd_new_spec(str(root), gbi.load_conf(str(root)), args)


#: The kinds whose input is no field list, each a handler taking the repository and its own arguments.
KIND_HANDLERS = {"build-readme": run_build_readme, "spec": run_spec}


def main(argv):
    if len(argv) < 2 or argv[0] != "new" or argv[1].startswith("-"):
        print(__doc__.split("\n\n")[1], file=sys.stderr)
        return 2
    kind, rest = argv[1], argv[2:]
    p = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, encoding="utf-8")
    if p.returncode != 0:
        print(f"refused {kind}: the working directory is in no git repository")
        return 2
    root = pathlib.Path(p.stdout.strip())
    try:
        if kind in KIND_HANDLERS:
            import gen_build_index as gbi  # noqa: E402  its Problem is a handler's refusal
            build_records.read_kind_row(root, kind)
            try:
                return KIND_HANDLERS[kind](root, rest)
            except gbi.Problem as exc:
                raise ValueError(str(exc)) from None
        ap = argparse.ArgumentParser(prog=f"gov_record.py new {kind}", allow_abbrev=False)
        for flag in ("--build", "--unit", "--title", "--name"):
            ap.add_argument(flag)
        ap.add_argument("--field", action="append", default=[])
        a = ap.parse_args(rest)
        fields = []
        for spelled in a.field:
            key, eq, value = spelled.partition("=")
            if not eq or not key:
                raise ValueError(f"--field {spelled!r} is not <Name>=<value>")
            fields.append((key, value))
        word, said, key, lines = build_records.write_new_record(root, kind, a.build, a.unit, a.title, fields, a.name)
    except ValueError as exc:
        print(f"refused {kind}: {exc}")
        return 2
    for line in lines:
        print(line)
    if word == "waiting":
        print(said)
        return 4
    print(f"{word} {said} key {key}")
    return 0


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
