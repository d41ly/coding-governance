#!/usr/bin/env python3
"""gov_record.py — the one `record` write door (TOOL-dTotalRecall-2).

    python <prefix>/memory-tree/gov_record.py new <kind> --build <slug> --unit <id> --title <text>
                                              [--name <stem>] [--field <Name>=<value>]...
    python <prefix>/memory-tree/gov_record.py new build-readme <slug> --asks <IDLIST>
    python <prefix>/memory-tree/gov_record.py new spec <id> --tier 1|2 [--order <n>] [--base <sha>]
    python <prefix>/memory-tree/gov_record.py new ask --build <slug> --family <FAMILY> --text <text> --sev <LEVEL> <why>
                                              [--clause <label> <value>]... [--unit] [--pointer <path>]

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
`--new-build` and `--new-spec` scaffolds of `gen_build_index.py`, imported, every flag passed through;
`ask` grades the ask's clauses by `asks.acceptance` before any mint, then writes its ask and `SEV` rows
into the build's `BACKLOG.md` under an id the `--family` counter mints (TOOL-dTotalRecall-7), printing
`wrote <path> <id> key <key>` or `exists <path> <id> key <key>`, and `graded: not ready (R5)` under `grade`.

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


def derive_ask_key(text, unit, pointer, clauses):
    """The content key of one ask: `build_records.derive_content_key("ask", …)` over its text, its `unit`
    marker (`unit` or empty), its pointer and each clause pair in written order. Its id, filed date and
    `SEV` row are not keyed, so a replayed filing derives the key the filed row re-derives."""
    fields = [("text", text), ("unit", "unit" if unit else ""), ("pointer", pointer or "")]
    return build_records.derive_content_key("ask", fields + [(label, value) for label, value in clauses])


def render_backlog_text(prior, slug, ask_row, sev_row):
    """The build's `BACKLOG.md` with `ask_row` after the last row under `## Asks` and `sev_row` after the last
    row under `## Dispositions`, each heading made where absent and the file with its H1 where `prior` is
    None: the layout `unattended.sh#write_backlog_rows` writes, so both writers append alike."""
    import backlog  # noqa: E402  the headings, spelled once
    if prior is None:
        return f"# {slug} — asks\n\n{backlog.H_ASKS}\n{ask_row}\n\n{backlog.H_DISPOSITIONS}\n{sev_row}\n"
    lines = [ln[:-1] if ln.endswith("\r") else ln for ln in prior.split("\n")]
    if lines and lines[-1] == "":
        lines.pop()
    ai = next((i for i, ln in enumerate(lines) if ln == backlog.H_ASKS), None)
    di = next((i for i, ln in enumerate(lines) if ln == backlog.H_DISPOSITIONS), None)
    at = dl = None
    if ai is not None:
        stop = di if di is not None and di > ai else len(lines)
        at = max([ai] + [i for i in range(ai + 1, stop) if lines[i].strip()])
    if di is not None:
        dl = max([di] + [i for i in range(di + 1, len(lines)) if lines[i].strip()])
    out = []
    for i, ln in enumerate(lines):
        if ai is None and i == di:
            out += [backlog.H_ASKS, ask_row, ""]
        out.append(ln)
        if i == at:
            out.append(ask_row)
        if i == dl:
            out.append(sev_row)
    if ai is None and di is None:
        out += ["", backlog.H_ASKS, ask_row]
    if di is None:
        out += ["", backlog.H_DISPOSITIONS, sev_row]
    return "\n".join(out) + "\n"


def write_new_ask(root, argv):
    """`new ask --build <slug> --family <FAMILY> --text <text> --sev <LEVEL> <why> [--clause <label> <value>]…
    [--unit] [--pointer <path>]`: the ask kind's handler (TOOL-dTotalRecall-7 S2, §4 "The door verb"). In
    order: the arguments, `--family` one the conf's `FAMILIES` declares; `asks.acceptance` read; the
    `--clause` mapping graded by `backlog.check_ask_acceptable`, a false grade under `refuse` the refusal,
    before any listing, mint or write; the content key; the listing of the build's `BACKLOG.md`, an ask of
    that key `exists`; the counter mint `build_records.write_seq_mint`; both rows rendered, written, staged
    and parsed back, the file put back as it was where the read-back fails. ValueError for every refusal.
    WHAT IT DOES NOT CHECK: an ask of the same key filed on another branch, which the counter hands the
    same id; an ask of the same text whose clauses differ, which is another key; a clause VALUE's own
    grammar, which the read-back and V13 read (TOOL-dTotalRecall-41 moves it to the door)."""
    import datetime
    import backlog  # noqa: E402  the predicate, the renderers and the parser, spelled once
    from tree_lib import read_policy_value  # noqa: E402  the kit's one policy read
    ap = argparse.ArgumentParser(prog="gov_record.py new ask", allow_abbrev=False)
    for flag in ("--build", "--family", "--text", "--pointer"):
        ap.add_argument(flag)
    ap.add_argument("--sev", nargs=2, metavar=("LEVEL", "WHY"))
    ap.add_argument("--clause", nargs=2, action="append", default=[], metavar=("LABEL", "VALUE"))
    ap.add_argument("--unit", action="store_true")
    a = ap.parse_args(argv)
    conf = build_records.read_design_conf(root)
    families = [p.split(":", 1)[1] for p in (conf.get("FAMILIES") or "").split() if ":" in p]
    if not a.family:
        raise ValueError(f"--family <FAMILY> is required, one of the conf's FAMILIES: {' '.join(families) or 'none'}")
    if a.family not in families:
        raise ValueError(f"--family {a.family} is no family the conf's FAMILIES declare: "
                         f"{' '.join(families) or 'none'}")
    for flag, value in (("--build", a.build), ("--text", a.text)):
        if not value:
            raise ValueError(f"{flag} is required")
    if not a.sev:
        raise ValueError(f"--sev <LEVEL> <why> is required, LEVEL one of {' '.join(backlog.SEVERITIES)}")
    if not build_records.SLUG.match(a.build):
        raise ValueError(f"--build {a.build!r} is not a build slug")
    level, why = a.sev
    if level not in backlog.SEVERITIES:
        raise ValueError(f"--sev {level} is no level of {' '.join(backlog.SEVERITIES)}")
    bad = [label for label, _ in a.clause if label not in backlog.CLAUSE_LABELS]
    if bad:
        raise ValueError(f"--clause {' '.join(bad)} is no label of {' '.join(backlog.CLAUSE_LABELS)}")
    pairs = [(label, value) for label, value in a.clause]
    given = [("--text", a.text), ("--sev why", why)] + ([("--pointer", a.pointer)] if a.pointer is not None else [])
    for name, value in given + pairs:
        if not value.strip() or "\n" in value or "\r" in value:
            raise ValueError(f"{name}: a value is one line and not empty")
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    if not pathlib.Path(root, memory_root, "builds", a.build).is_dir():
        raise ValueError(f"{memory_root}/builds/{a.build}/ is no build folder of this tree")
    try:
        grammar = backlog.build_grammar(families)
    except backlog.Problem as exc:
        raise ValueError(f"the conf's FAMILIES do not compile: {exc}") from None

    try:
        value = read_policy_value("asks.acceptance", root)
    except (LookupError, ValueError) as exc:
        raise ValueError(f"asks.acceptance did not read, so no ask is filed on a guessed value: {exc}") from None
    if value not in ("refuse", "grade"):
        raise ValueError(f"asks.acceptance reads {value!r}, neither refuse nor grade")
    clauses = {label: tuple(backlog.read_clause_values(pairs, label)) for label in backlog.CLAUSE_LABELS
               if backlog.read_clause_values(pairs, label)}
    ready = backlog.check_ask_acceptable(clauses)
    if not ready and value == "refuse":
        raise ValueError(f"asks.acceptance is refuse and the ask {a.text!r} states no acceptance: it states "
                         f"`accept <what done looks like>` or a `seen … run`, `seen <locator> run <command>`, "
                         f"each a --clause")
    key = derive_ask_key(a.text, a.unit, a.pointer, pairs)

    rel = f"{memory_root}/builds/{a.build}/BACKLOG.md"
    path = pathlib.Path(root, rel)
    held = path.read_bytes() if path.is_file() else None
    prior = held.decode("utf-8") if held is not None else None
    if prior is not None:
        for ask in backlog.parse_file(rel, prior, grammar).asks:
            if derive_ask_key(ask.text, ask.unit, ask.pointer, ask.clauses) == key:
                print(f"exists {rel} {ask.id} key {key}")
                return 0

    word, said, lines = build_records.write_seq_mint(root, a.family, a.build, key)
    for line in lines:
        print(line)
    if word == "waiting":
        print(said)
        return 4
    today = datetime.date.today().isoformat()
    text = render_backlog_text(prior, a.build, backlog.render_ask_row(said, today, a.text, a.unit, a.pointer or "",
                                                                     pairs),
                               backlog.render_sev_row(said, level, why))
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    subprocess.run(["git", "add", "--", rel], cwd=str(root), capture_output=True, check=False)
    back = backlog.parse_file(rel, path.read_bytes().decode("utf-8"), grammar)
    asks = [x for x in back.asks if x.id == said]
    sevs = [r for r in back.rows if r.verb == backlog.SEV_VERB and r.target == said]
    if (len(asks) != 1 or len(sevs) != 1 or sevs[0].value != level
            or derive_ask_key(asks[0].text, asks[0].unit, asks[0].pointer, asks[0].clauses) != key):
        if prior is None:
            subprocess.run(["git", "rm", "-q", "--cached", "-f", "--", rel], cwd=str(root), capture_output=True,
                           check=False)
            path.unlink()
        else:
            path.write_bytes(held)
            subprocess.run(["git", "add", "--", rel], cwd=str(root), capture_output=True, check=False)
        raise ValueError(f"{rel} did not read {said} back as one ask of key {key} and one SEV row at {level} "
                         f"({len(asks)} ask(s), {len(sevs)} SEV row(s)), so the rows were removed and the file put "
                         f"back as it was")
    print(f"wrote {rel} {said} key {key}")
    if not ready:
        print("graded: not ready (R5)")
    return 0


#: The kinds whose input is no field list, each a handler taking the repository and its own arguments.
KIND_HANDLERS = {"build-readme": run_build_readme, "spec": run_spec, "ask": write_new_ask}


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
