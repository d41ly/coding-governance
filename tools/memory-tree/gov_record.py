#!/usr/bin/env python3
"""gov_record.py — the one `record` write door (TOOL-dTotalRecall-2).

    python <prefix>/memory-tree/gov_record.py new <kind> --build <slug> --unit <id> --title <text>
                                              [--caused-by <target>] [--name <stem>] [--field <Name>=<value>]...
                                              [--edge "<anchor> <type>=<target>[,<target>]"]...
    python <prefix>/memory-tree/gov_record.py new build-readme <slug> --asks <IDLIST>
    python <prefix>/memory-tree/gov_record.py new spec <id> --tier 1|2 [--order <n>] [--base <sha>]
    python <prefix>/memory-tree/gov_record.py new ask --build <slug> --family <FAMILY> --text <text> --sev <LEVEL> <why>
                                              [--clause <label> <value>]... [--unit] [--pointer <path>]
    python <prefix>/memory-tree/gov_record.py new shape-run --review <path>
    python <prefix>/memory-tree/gov_record.py find [<question> --terms <words>] [--kind <k>] [--tag <t>] [--build <slug>] [--paths <glob>]
    python <prefix>/memory-tree/gov_record.py show <key>[#<tag>][@<blob>]
    python <prefix>/memory-tree/gov_record.py budget --role <role> <key>...

It stands in for `gov record` the way `gov_tag.py` stands in for `gov tag`, and runs in the repository at
the current directory. A kind is written here only where its `[[record-kind]]` row in `record-kinds.toml`
names `gov_record.py new <kind>` its writer: a kind with no row, or another door, exits 2 naming the
registry or that door, so a factory door's kind (`build_records.py new <kind>`) is refused naming it.

A `fields` kind is `build_records.write_new_record`: the row's template filled with each `--field`, a key
the row does not name following in the caller's order; the bytes parsed back by the kind's own check
before anything is written; a record of the kind whose content key matches is the same write, `exists`;
then the build's lease or claim is read, the id minted by the row's `id-rule` (a typed kind's `<n>`
through `write_record`, an empty rule's `--name`, a `<FAMILY>-<slug>-<seq>` counter through
`gov-claim.sh ask`, the family the unit's) and the file written and staged, never committed. Its header
(TOOL-dTotalRecall-19): `**Made-by:**` and `**Caused-by:**` after the Serves line, a typed kind's as its
last fields; `--caused-by` (or a `Caused-by` field) is refused absent on a kind whose row is no `root`, and
refused where it is neither a family id the corpus defines nor a tracked record's stem; `Made-by` is
`lease-<slug>` under the build lease this session holds, else `owner`. Each `--edge` is a column-0
`**Edges:** <type>=<targets>` line under the heading of that anchor, refused for a type `edges.toml` lacks,
an anchor the record does not carry, a second line of one type under one heading or a target the edge
grammar cannot classify, nothing written. A kind whose
input is not a field list takes its handler in `KIND_HANDLERS`: `build-readme` and `spec` run the
`--new-build` and `--new-spec` scaffolds of `gen_build_index.py`, imported, every flag passed through;
`ask` refuses a line break or row separator in any value and grades the clauses parsed back from the row
it would write by `asks.acceptance` before any mint (TOOL-dTotalRecall-41), then writes its ask and `SEV` rows
into the build's `BACKLOG.md` under an id the `--family` counter mints (TOOL-dTotalRecall-7), printing
`wrote <path> <id> key <key>` or `exists <path> <id> key <key>`, and `graded: not ready (R5)` under `grade`;
`shape-run` takes `--review <path>` alone, a tracked review record whose one `review-shape` line `shape_run.py`
parses, and writes its fields through `write_new_record` (TOOL-dTotalRecall-11).

Exit and stdout: 0 `wrote <path> key <content key>` · 0 `exists <path> key <content key>` · 2 `refused
<kind>: <why>` · 4 `waiting offline <ref>`, nothing written. A handler prints its scaffold's lines.
The read verbs write nothing in the tree (TOOL-dTotalRecall-9): `find` lists at most 40 records, never
their content, `show` prints one record or one section of it, and `budget` sums a role's read set against
`memory.item-budget`; `record_find.py` beside this door holds all three and says what each prints.
WHAT IT DOES NOT CHECK: whether a cause is reached
from a root, which `record_causes.py --check` grades; whether two builds hold a `--name` record of one stem and one content key, which
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
    from id_grammar import parse_id_parts  # noqa: E402  the one id parser (TOOL-dTotalRecall-53 S16)
    args = gbi.read_new_spec_args(argv)
    try:
        slug = parse_id_parts(args["id"], root)[1]
    except ValueError:   # an id the grammar refuses names no build; the scaffold refuses it with its reason
        slug = None
    if slug is not None:
        for line in build_records.check_mint_authority(root, slug):
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


def check_rows_added(before, after, ask_id, level):
    """What `after` adds to `before` (two `backlog.parse_file` results, `before` None for an absent file),
    where the ask door writes exactly one ask `ask_id` and one verb row, its `SEV` row at `level`: an empty
    string where it adds exactly those, else what it added (TOOL-dTotalRecall-41 S3).
    WHAT IT DOES NOT CHECK: a row of `before` that `after` rewrites in place, since it counts and names."""
    import backlog  # noqa: E402  the SEV verb, spelled once
    asks = len(after.asks) - (len(before.asks) if before is not None else 0)
    rows = len(after.rows) - (len(before.rows) if before is not None else 0)
    named = [x for x in after.asks if x.id == ask_id]
    sevs = [r for r in after.rows if r.verb == backlog.SEV_VERB and r.target == ask_id and r.value == level]
    if asks == 1 and rows == 1 and len(named) == 1 and len(sevs) == 1:
        return ""
    return (f"add {asks} ask(s) and {rows} verb row(s), {len(named)} ask(s) {ask_id} and {len(sevs)} SEV row(s) "
            f"at {level} naming it, where exactly one of each is added")


def write_new_ask(root, argv):
    """`new ask --build <slug> --family <FAMILY> --text <text> --sev <LEVEL> <why> [--clause <label> <value>]…
    [--unit] [--pointer <path>]`: the ask kind's handler (TOOL-dTotalRecall-7 S2, §4 "The door verb";
    TOOL-dTotalRecall-41 §4 "The handler's order"). In order: the arguments, `--family` one the conf's
    `FAMILIES` declares; `backlog.check_row_value` on every value; `asks.acceptance` read; the build's
    `BACKLOG.md` parsed once, both rows rendered under the provisional id `<FAMILY>-<slug>-0` into the
    would-be file and parsed, which must add exactly that ask and its `SEV` row (`check_rows_added`); that
    parsed ask's clauses, through `derive_clauses`, graded by `backlog.check_ask_acceptable`, a false grade
    under `refuse` the refusal, before any listing, mint or write; the listing of the before-parse, an ask of
    the content key `exists`; the counter mint `build_records.write_seq_mint`; both rows rendered under the
    minted id, written by compare-and-swap (TOOL-dTotalRecall-53 S40): the file re-read just before the
    write, a refusal where its bytes moved since the parse, then `legacy_ledger._write_atomic`'s temp file
    and `os.replace`; staged and parsed back to the same count, the file put back as it was where the
    read-back fails, which prints `refused ask:` naming the file and exits 3. ValueError for every other
    refusal, exit 2; a refusal after the mint leaves the minted id unused.
    WHAT IT DOES NOT CHECK: an ask of the same key filed on another branch, which the counter hands the
    same id; an ask of the same text whose clauses differ, which is another key; the rows rendered under the
    minted id, which are counted and keyed, never graded; an ask the file already holds under the
    provisional id, which the offline mint never hands out and whose clauses would merge into the grade."""
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
    for name, value in given + [(f"--clause {label}", value) for label, value in pairs]:
        if not value.strip():
            raise ValueError(f"{name}: a value is not empty")
        backlog.check_row_value(name, value)
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
    key = derive_ask_key(a.text, a.unit, a.pointer, pairs)

    rel = f"{memory_root}/builds/{a.build}/BACKLOG.md"
    path = pathlib.Path(root, rel)
    held = path.read_bytes() if path.is_file() else None
    prior = held.decode("utf-8") if held is not None else None
    before = backlog.parse_file(rel, prior, grammar) if prior is not None else None
    today = datetime.date.today().isoformat()

    def render_rows(ask_id):
        """The would-be file with the ask and its `SEV` row rendered under `ask_id`, through the module so
        a rebound renderer is the one read."""
        return render_backlog_text(prior, a.build, backlog.render_ask_row(ask_id, today, a.text, a.unit,
                                                                          a.pointer or "", pairs),
                                   backlog.render_sev_row(ask_id, level, why))

    provisional = f"{a.family}-{a.build}-0"
    would = backlog.parse_file(rel, render_rows(provisional), grammar)
    wrong = check_rows_added(before, would, provisional, level)
    if wrong:
        raise ValueError(f"the rows rendered under the provisional id {provisional} {wrong}, so nothing was "
                         f"minted or written")
    ready = backlog.check_ask_acceptable(
        backlog.derive_clauses(backlog.build_corpus([would])).get(provisional, {}))
    if not ready and value == "refuse":
        raise ValueError(f"asks.acceptance is refuse and the ask {a.text!r} states no acceptance: it states "
                         f"`accept <what done looks like>` or a `seen … run`, `seen <locator> run <command>`, "
                         f"each a --clause")
    for ask in before.asks if before is not None else ():
        if derive_ask_key(ask.text, ask.unit, ask.pointer, ask.clauses) == key:
            print(f"exists {rel} {ask.id} key {key}")
            return 0

    word, said, lines = build_records.write_seq_mint(root, a.family, a.build, key)
    for line in lines:
        print(line)
    if word == "waiting":
        print(said)
        return 4
    from legacy_ledger import _write_atomic  # noqa: E402  the kit's one temp-file-and-replace write
    now = path.read_bytes() if path.is_file() else None   # S40: compare, then swap, the file as parsed or nothing
    if now != held:
        raise ValueError(f"{rel} moved since it was parsed, another writer's bytes in it, so nothing was written and "
                         f"{said} stays unused: file the ask again")
    _write_atomic(path, render_rows(said).encode("utf-8"))
    subprocess.run(["git", "add", "--", rel], cwd=str(root), capture_output=True, check=False)
    back = backlog.parse_file(rel, path.read_bytes().decode("utf-8"), grammar)
    wrong = check_rows_added(before, back, said, level)
    asks = [x for x in back.asks if x.id == said]
    if wrong or derive_ask_key(asks[0].text, asks[0].unit, asks[0].pointer, asks[0].clauses) != key:
        if prior is None:
            subprocess.run(["git", "rm", "-q", "--cached", "-f", "--", rel], cwd=str(root), capture_output=True,
                           check=False)
            path.unlink()
        else:
            _write_atomic(path, held)
            subprocess.run(["git", "add", "--", rel], cwd=str(root), capture_output=True, check=False)
        print(f"refused ask: {rel} did not read {said} back as one ask of key {key} and one SEV row at {level}: "
              f"the written rows {wrong or 'read another key'}, so the rows were removed and the file put back as it "
              f"was")
        return 3
    print(f"wrote {rel} {said} key {key}")
    if not ready:
        print("graded: not ready (R5)")
    return 0


def write_shape_run(root, review):
    """`new shape-run --review <path>`: one review exit's `review-shape` line as a shape-run record
    (TOOL-dTotalRecall-11 S4). `review` is a tracked file of a `<memory root>/builds/<slug>/reviews/` folder,
    read from the working copy; its one column-0 line is taken by `shape_run.read_shape_line` and parsed by
    `parse_shape_line`, and the record written by `build_records.write_new_record` under `<slug>`, serving
    the first id of the review's `**Serves:**` line with its `@rev-<N>` pin cut (§8 F5), titled with the
    review's stem, its fields the line's in line order and `Caused-by` that stem. The content key makes a
    second call for the same line `exists`. ValueError for every refusal, nothing written.
    WHAT IT DOES NOT CHECK: that the line is the one the review's harness printed."""
    import re
    import shape_run  # noqa: E402  the line's one grammar
    from tree_lib import read_bindings  # noqa: E402  the Serves line's one reader
    conf = build_records.read_design_conf(root)
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    where = f"a tracked file of a {memory_root}/builds/<slug>/reviews/ folder"
    path = pathlib.Path(review)
    path = (path if path.is_absolute() else pathlib.Path.cwd() / path).resolve()
    try:
        rel = path.relative_to(pathlib.Path(root).resolve()).as_posix()
    except ValueError:
        raise ValueError(f"--review {review} is not {where}") from None
    m = re.fullmatch(re.escape(memory_root) + r"/builds/(?P<slug>[^/]+)/reviews/(?P<stem>[^/]+)\.md", rel)
    tracked = subprocess.run(["git", "ls-files", "--", f":(literal){rel}"], cwd=str(root), capture_output=True,
                             text=True, encoding="utf-8").stdout.strip()
    if not m or tracked != rel or not path.is_file():
        raise ValueError(f"--review {review} is not {where}")
    try:
        line = shape_run.read_shape_line(path.read_bytes().decode("utf-8"))
    except UnicodeDecodeError:
        raise ValueError(f"{rel} is not UTF-8 text") from None
    except ValueError as exc:
        raise ValueError(f"{rel} carries {exc}") from None
    try:
        parsed = shape_run.parse_shape_line(line)
    except ValueError as exc:
        raise ValueError(f"the {shape_run.LINE_HEAD} line of {rel} is refused at {exc}") from None
    binding = read_bindings(str(root), [rel], dict(conf, MEMORY_ROOT=memory_root)).get(rel) or {}
    if binding.get("state") != "bound":
        raise ValueError(f"{rel} binds no unit on its **Serves:** line: {binding.get('why') or 'not read'}")
    fields = [(shape_run.derive_record_field(name), parsed[name.replace("-", "_")])
              for name, _p, _o in shape_run.SHAPE_FIELDS if name.replace("-", "_") in parsed]
    fields.append(("Caused-by", m.group("stem")))
    return print_written(*build_records.write_new_record(root, shape_run.KIND, m.group("slug"), binding["ids"][0],
                                                         m.group("stem"), fields))


def run_shape_run(root, argv):
    """`new shape-run --review <path>`, its one flag: `write_shape_run`."""
    ap = argparse.ArgumentParser(prog="gov_record.py new shape-run", allow_abbrev=False)
    ap.add_argument("--review", required=True)
    return write_shape_run(root, ap.parse_args(argv).review)


def print_written(word, said, key, lines):
    """The door's report of one `write_new_record` result: the authority's lines, then `waiting <ref>` exit 4,
    or `<word> <path> key <key>` exit 0."""
    for line in lines:
        print(line)
    if word == "waiting":
        print(said)
        return 4
    print(f"{word} {said} key {key}")
    return 0


#: The kinds whose input is no field list, each a handler taking the repository and its own arguments.
KIND_HANDLERS = {"build-readme": run_build_readme, "spec": run_spec, "ask": write_new_ask, "shape-run": run_shape_run}


def run_read_verb(root, verb, argv):
    """`find`, `show` and `budget` (TOOL-dTotalRecall-9 S3, S5, S6): `record_find`'s, printed; a refusal
    exits 2 naming what refused."""
    import record_find  # noqa: E402  the finder, beside this door
    ap = argparse.ArgumentParser(prog=f"gov_record.py {verb}", allow_abbrev=False)
    if verb == "find":
        ap.add_argument("question", nargs="?")
        ap.add_argument("--terms", action="append", default=[])
        for flag in ("--kind", "--tag", "--build", "--paths"):
            ap.add_argument(flag)
    elif verb == "show":
        ap.add_argument("address")
    else:
        ap.add_argument("--role", required=True)
        ap.add_argument("keys", nargs="+")
    a = ap.parse_args(argv)
    try:
        if verb == "find":
            terms = [t for spelled in a.terms for t in spelled.split()]
            lines, rc = record_find.run_find(root, a.question, terms, kind=a.kind, tag=a.tag, build=a.build,
                                             paths=a.paths), 0
        elif verb == "show":
            sec = record_find.read_section(root, a.address)
            lines, rc = [sec["text"]], 0
        else:
            rc, lines = record_find.check_read_set(root, a.role, a.keys)
    except record_find.FindError as exc:
        print(f"refused {verb}: {exc}")
        return 2
    for line in lines:
        print(line)
    return rc


def main(argv):
    if argv[:1] in (["find"], ["show"], ["budget"]):
        p = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, encoding="utf-8")
        if p.returncode != 0:
            print(f"refused {argv[0]}: the working directory is in no git repository")
            return 2
        return run_read_verb(pathlib.Path(p.stdout.strip()), argv[0], argv[1:])
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
        for flag in ("--build", "--unit", "--title", "--name", "--caused-by"):
            ap.add_argument(flag)
        ap.add_argument("--field", action="append", default=[])
        ap.add_argument("--edge", action="append", default=[])
        a = ap.parse_args(rest)
        fields = []
        for spelled in a.field:
            key, eq, value = spelled.partition("=")
            if not eq or not key:
                raise ValueError(f"--field {spelled!r} is not <Name>=<value>")
            fields.append((key, value))
        written = build_records.write_new_record(root, kind, a.build, a.unit, a.title, fields, a.name, a.caused_by,
                                                 a.edge)
    except ValueError as exc:
        print(f"refused {kind}: {exc}")
        return 2
    return print_written(*written)


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
