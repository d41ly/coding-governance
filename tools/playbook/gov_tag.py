"""gov_tag — the one tag resolver, standing in for `gov tag` (PLAY-dOrderedCharter-19 S6, §8 F1).

    python gov_tag.py show|where|refs|check <address> [--json]
    python gov_tag.py check [--base <rev>]
    python gov_tag.py --rebuild | --list-positional
    python gov_tag.py --fixture --plant <case> [--set <key>=<value>]

`show` returns the tag's row, or its subtree as `tags.slice` says; `where` prints `path:line`; `refs`
prints every citation of it, a build record's too; `check` runs the `retired`, `resolves` and `owned`
arms over the citations outside `<MEMORY_ROOT>/builds/`. An address is a tag, `doc.<name>#<seg>`, or a
positional label `aliases.toml` maps. Every line opens `tags:`; `--json` is the index's only JSON.
Exit 0 green, 1 red, 2 a refusal (an unreadable registry, a refused policy read, a locked index).

The three keys are read through `policy_value.read_policy_value`, the committed policy at its landed
revision. `--set` is honoured under `--fixture` only, so the leg cannot be relaxed past the policy file.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import tempfile

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
sys.path.insert(0, str(KIT_DIR))

import tag_index as ti  # noqa: E402
from policy_value import PolicyRefused, read_policy_value  # noqa: E402

POSITIONAL_RE = re.compile(r"\b(BUILD-METHOD)(?:\.md)?`? (M\d+)\b|\b(HYGIENE)(?:\.md)?`? (check \d+)\b")


def resolve_repo_root() -> pathlib.Path:
    """The repository this kit sits in: the top of the worktree holding this file."""
    return pathlib.Path(ti.read_git(KIT_DIR, "rev-parse", "--show-toplevel").strip())


def derive_kit_rel(root: pathlib.Path) -> str:
    return pathlib.Path(os.path.relpath(KIT_DIR, root)).as_posix()


def read_key(key, root, sets, reader):
    """`--set`'s value under the fixture, else the policy's: the caller passes its own literal read."""
    return sets[key] if key in sets else reader()


def run_kit_verb(root, verb, address, *, sets, as_json=False, base=None, kit_rel=None) -> int:
    kit_rel = kit_rel or derive_kit_rel(root)
    ctx = ti.derive_context(root, root / kit_rel / "namespaces.toml")
    aliases = ti.read_aliases(root / kit_rel / "aliases.toml")
    con = ti.load_index(root)
    try:
        state = ti.load_view(con, root, ctx)
        if verb == "rebuild":
            print(f"tags: index {state['tree'][:12]} built, {state['parsed']} blob{'s' if state['parsed'] != 1 else ''} parsed")
            return state["parsed"]
        if verb in ("show", "where", "refs") and not address:
            print(f"tags: {verb} needs an address", file=sys.stderr)
            return 2
        if verb == "show":
            slice_ = read_key("tags.slice", root, sets, lambda: read_policy_value("tags.slice", root)[0][0])
            rows = ti.resolve_address(con, address, slice_, aliases)
            if as_json:
                print(json.dumps(rows, indent=2, sort_keys=True))
            for r in rows if not as_json else ():
                print(f"tags: {r['tag']} · {r['path']}:{r['line']}-{r['end_line']} · {r['kind']}")
                for ln in r["text"].splitlines():
                    print(f"tags:   {ln}")
            if not rows:
                print(f"tags: {address} resolves to no row ({slice_})")
            return 0 if rows else 1
        if verb == "where":
            rows = ti.resolve_address(con, address, "leaf", aliases)
            if as_json:
                print(json.dumps([{"path": r["path"], "line": r["line"]} for r in rows]))
            for r in rows if not as_json else ():
                print(f"tags: {r['path']}:{r['line']}")
            if not rows:
                print(f"tags: {address} resolves to no row", file=sys.stderr)
            return 0 if rows else 1
        if verb == "refs":
            tag = aliases.get(address, address)
            rows = [{"path": p, "line": n} for _t, p, n, *_ in ti.read_rows(con, ("span",), tag=tag)]
            if as_json:
                print(json.dumps(rows))
            for r in rows if not as_json else ():
                print(f"tags: {r['path']}:{r['line']}")
            print(f"tags: {len(rows)} citation(s) of {tag}", file=sys.stderr)
            return 0
        return run_check(con, root, ctx, kit_rel, sets=sets, base=base, as_json=as_json, state=state)
    finally:
        con.close()


def run_check(con, root, ctx, kit_rel, *, sets, base, as_json, state) -> int:
    counts = ti.derive_namespace_state(con, ctx)
    armed = counts  # ns -> defined-tag count; 0 is unarmed
    bare_mode = read_key("tags.bare-refs", root, sets, lambda: read_policy_value("tags.bare-refs", root)[0][0])
    retired_mode = read_key("tags.retired-cites", root, sets,
                            lambda: read_policy_value("tags.retired-cites", root)[0][0])
    reds, c = ti.check_resolves(con, ctx, bare_mode, armed)
    base_spans, base_why = None, ""
    if con.execute(ti.VIEW_ROWS + " WHERE p.kind='retired' LIMIT 1").fetchone():
        if base is None:
            from_mt = ti.load_memory_tree()  # noqa: F841 - puts memory-tree on sys.path
            from coverage_join import resolve_compare_base
            base, base_why = resolve_compare_base(root)
        if base:
            base_tree = ti.read_git(root, "rev-parse", f"{base}^{{tree}}").strip()
            ti.load_view(con, root, ctx, tree=base_tree, overlay=False)
            base_spans = {(p, t) for t, p, *_ in ti.read_rows(con, ("span",))}
            ti.load_view(con, root, ctx)
        else:
            print(f"tags: retired: no base ({base_why}), so every citation reads as new")
    r_reds, warns, cited = ti.check_retired(con, ctx, retired_mode, base_spans, armed)
    o_reds = ti.check_owned(con, ctx, root / kit_rel / "layers.toml")
    reds += r_reds + o_reds
    tags = sum(counts.values())
    unread = con.execute("SELECT COUNT(*) FROM view_path WHERE path NOT LIKE '%.md'").fetchone()[0]
    summary = {
        "namespaces": len(counts), "tags": tags, "graded": c["graded"], "unresolved": c["unresolved"],
        "retired_cited": cited, "bare_refs": c["bare"], "records_not_graded": c["records"], "paths_not_markdown": unread,
        "unarmed": {ns: c["unarmed"].get(ns, 0) for ns, n in counts.items() if not n},
        "reds": reds, "warns": warns, "blobs_parsed": state["parsed"],
    }
    if as_json:
        print(json.dumps(summary, indent=2, sort_keys=True))
        return 1 if reds else 0
    for line in c["notes"] + warns + reds:
        print(line)
    print(f"tags: {len(counts)} namespaces, {tags} tags, {c['graded']} citations graded, {c['unresolved']} unresolved, "
          f"{cited} retired-cited, {c['bare']} bare refs; {c['records']} in build records not graded; "
          f"{unread} paths outside Markdown not read; "
          f"{state['parsed']} blob{'s' if state['parsed'] != 1 else ''} parsed")
    for ns in summary["unarmed"]:
        print(f"tags: unarmed {ns} ({summary['unarmed'][ns]} not graded)")
    print(f"tags: {'RED' if reds else 'green'} · {len(reds)} red")
    return 1 if reds else 0


def read_positional(root) -> list[str]:
    """`<path>\\t<ref>` for every positional reference in tracked Markdown that an alias row could key."""
    try:
        out = subprocess.run(["git", "-C", str(root), "grep", "-I", "-n", "-E",
                              r"(BUILD-METHOD|HYGIENE)(\.md)?`? (M[0-9]+|check [0-9]+)", "--", "*.md"],
                             capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    except OSError as exc:
        raise ti.TagError(f"git grep could not run: {exc}") from None
    rows = set()
    for rec in out.splitlines():
        path, _, rest = rec.partition(":")
        _line, _, text = rest.partition(":")
        for m in POSITIONAL_RE.finditer(text):
            doc, label = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
            rows.add(f"{path}\t{doc} {label}")
    return sorted(rows)


# ------------------------------------------------------------------------------------------ the fixture

FIXTURE_REGISTRY = '''[[namespace]]
ns = "doc"
owner = "fixture"
layer = "layer.instruction"
source = "the charter and memory/guides/*.md"
extractor = "tag_index:extract_doc"
role = "describes"
purpose-source = "fixture"
join-armed-by = "fixture"

[[namespace]]
ns = "practice"
owner = "fixture"
layer = "layer.instruction"
source = "every *.tags file"
extractor = "fixture_tags:extract_declared"
role = "describes"
purpose-source = "fixture"
join-armed-by = "fixture"

[[namespace]]
ns = "layer"
owner = "fixture"
layer = "layer.instruction"
source = "every *.tags file"
extractor = "fixture_tags:extract_declared"
role = "selects"
purpose-source = "fixture"
join-armed-by = "fixture"
'''
FIXTURE_UNIT_ROW = '''
[[namespace]]
ns = "unit"
owner = "fixture"
layer = "layer.instruction"
source = "every instructions.toml"
extractor = "tag_index:extract_unit"
role = "selects"
purpose-source = "fixture"
join-armed-by = "fixture"
'''
FIXTURE_EXTRACTOR = '''"""The fixture's declaring extractor: each line of a `*.tags` file is a tag, `retired <tag>` a retirement."""


def extract_declared(ctx, path, text=None):
    if text is None:
        return "" if path.endswith(".tags") else None
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        word = line.split()
        if len(word) == 2 and word[0] == "retired":
            rows.append((word[1], "retired", n, n, line))
        elif len(word) == 1:
            rows.append((word[0], "tag", n, n, line))
    return rows
'''
FIXTURE_LAYERS = '''[[layer]]
tag = "layer.instruction"
kind = "core"

[[layer]]
tag = "layer.exp"
kind = "expansion"
'''
GUIDE = "# Alpha\n\n## Intro\n\nthe intro text\n\n## M5 — Recall and reuse\n\nrecall first\n"
FIXTURE_KIT = "tools/playbook"
PLANTS = ("none", "rebuild", "two-paths", "dirty", "one-commit", "slice", "retired", "retired-old",
          "retired-reminted", "bare", "bare-charter", "owned", "owned-core", "scope", "scope-guide")


def write_files(root: pathlib.Path, files: dict) -> None:
    for rel, text in files.items():
        p = root / rel
        if text is None:
            p.unlink()
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))


def run_git(root, *args) -> str:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(GIT_AUTHOR_NAME="f", GIT_AUTHOR_EMAIL="f@f", GIT_COMMITTER_NAME="f", GIT_COMMITTER_EMAIL="f@f")
    p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, env=env,
                       encoding="utf-8", errors="replace")
    if p.returncode:
        raise ti.TagError(f"fixture: git {' '.join(args)}: {p.stderr.strip()}")
    return p.stdout


def write_commit(root, files: dict, msg: str) -> str:
    write_files(root, files)
    run_git(root, "add", "-A")
    run_git(root, "commit", "-q", "--allow-empty", "-m", msg)
    return run_git(root, "rev-parse", "HEAD").strip()


def build_tags_fixture(top: pathlib.Path, plant: str) -> pathlib.Path:
    """A scratch repository at `top`/repo: the conf, a charter, one guide, a three-row registry beside its
    extractor and a layer register, a core kit declaring `practice.*` and `layer.*`, an expansion kit, and
    then `plant`'s files. Returns the repository's root."""
    root = top / "repo"
    root.mkdir(parents=True)
    run_git(root, "init", "-q", "-b", "main")
    run_git(root, "config", "core.autocrlf", "false")
    kit = "tools/playbook"
    files = {
        ".memory-tree.conf": 'MEMORY_ROOT=memory\nCHARTER="AGENTS.md"\n',
        "AGENTS.md": "# Charter\n\n## Practices\n\nthe practices\n",
        "memory/guides/ALPHA.md": GUIDE,
        f"{kit}/namespaces.toml": FIXTURE_REGISTRY + (FIXTURE_UNIT_ROW if plant.startswith("scope") else ""),
        f"{kit}/fixture_tags.py": FIXTURE_EXTRACTOR,
        f"{kit}/layers.toml": FIXTURE_LAYERS,
        f"{kit}/aliases.toml": '[[alias]]\nref = "ALPHA M5"\ntarget = "doc.alpha#m5-recall-and-reuse"\n',
        "tools/corekit/kit.toml": 'id = "corekit"\nlayer = "layer.instruction"\n',
        "tools/corekit/core.tags": "practice.land\npractice.memory\nlayer.memory\nlayer.memory.recall\n",
        "tools/expkit/kit.toml": 'id = "expkit"\nlayer = "layer.exp"\n',
        "tools/expkit/exp.tags": "",
    }
    if plant in ("retired", "retired-old", "retired-reminted"):
        files["tools/corekit/core.tags"] += "retired practice.old\n"
    if plant == "retired-reminted":
        files["tools/corekit/core.tags"] += "practice.old\n"
    if plant == "retired-old":
        files["memory/guides/ALPHA.md"] = GUIDE + "\nsee `practice.old`\n"
    if plant == "bare":
        files["memory/guides/ALPHA.md"] = GUIDE + "\nkeep [land] and `memory`\n"
    if plant == "bare-charter":
        files["AGENTS.md"] += "\n- [land] — land once\n"
    if plant == "owned":
        files["tools/expkit/exp.tags"] = "layer.fixture-x\n"
    if plant == "owned-core":
        files["tools/corekit/core.tags"] += "layer.fixture-x\n"
    if plant.startswith("scope"):
        files["memory/builds/x/README.md"] = "# x\n\ncites [doc.nope] before it lands\n"
        files["tools/corekit/code.py"] = "x = doc.get(1)\n"
        files["memory/guides/ALPHA.md"] = GUIDE + "\nthe unit `unit.x` lands later\n"
        if plant == "scope-guide":
            files["memory/guides/ALPHA.md"] += "\nand [doc.nope]\n"
    if plant == "two-paths":
        files["memory/guides/BETA.md"] = GUIDE
    write_commit(root, files, "base")
    return root


def run_fixture(plant: str, sets: dict) -> int:
    if plant not in PLANTS:
        print(f"tags: no plant '{plant}': one of {', '.join(PLANTS)}", file=sys.stderr)
        return 2
    top = pathlib.Path(tempfile.mkdtemp(prefix="gt"))
    try:
        root = build_tags_fixture(top, plant)
        return run_plant(root, top, plant, sets)
    finally:
        def remove_readonly(fn, path, _exc):
            os.chmod(path, stat.S_IWRITE)
            fn(path)
        shutil.rmtree(top, onerror=remove_readonly)


def read_dump(root) -> list[str]:
    con = ti.load_index(root)
    try:
        return ti.read_index_rows(con)
    finally:
        con.close()


def remove_index(root) -> None:
    (ti.common_git_dir(root) / "gov" / "index.db").unlink(missing_ok=True)


def run_plant(root, top, plant, sets) -> int:
    say = lambda *a: print("tags: plant " + plant + " · " + " ".join(map(str, a)))  # noqa: E731

    def run_verb(*args, **kw):  # every verb of a plant reads the fixture's own kit directory
        return run_kit_verb(*args, kit_rel=FIXTURE_KIT, **kw)
    if plant == "rebuild":
        run_verb(root, "rebuild", None, sets=sets)
        first = read_dump(root)
        remove_index(root)
        run_verb(root, "rebuild", None, sets=sets)
        second = read_dump(root)
        say(f"{len(first)} rows, then {len(second)} rows from nothing:", "dumps equal" if first == second else "dumps DIFFER")
        return 0 if first == second and first else 1
    if plant == "two-paths":
        run_verb(root, "rebuild", None, sets=sets)
        write_commit(root, {"memory/guides/BETA.md": None}, "drop one path")
        run_verb(root, "rebuild", None, sets=sets)
        incremental = read_dump(root)
        remove_index(root)
        run_verb(root, "rebuild", None, sets=sets)
        cold = read_dump(root)
        say("incremental rows", "equal" if incremental == cold else "DIFFER", "a cold build's")
        rc = run_verb(root, "where", "doc.alpha#intro", sets=sets)
        return 0 if incremental == cold and rc == 0 else 1
    if plant == "dirty":
        other = top / "wt2"
        run_git(root, "worktree", "add", "-q", str(other), "-b", "two")
        write_files(root, {"memory/guides/ALPHA.md": GUIDE.replace("the intro text", "edited in one")})
        write_files(other, {"memory/guides/ALPHA.md": GUIDE.replace("the intro text", "edited in two")})
        ok = True
        for where, mine, theirs in ((root, "edited in one", "edited in two"), (other, "edited in two", "edited in one")):
            con = ti.load_index(where)
            try:
                ctx = ti.derive_context(where, where / "tools/playbook/namespaces.toml")
                ti.load_view(con, where, ctx)
                text = "\n".join(r["text"] for r in ti.resolve_address(con, "doc.alpha#intro"))
            finally:
                con.close()
            seen = mine in text and theirs not in text
            ok &= seen
            say(pathlib.Path(where).name, "serves its own edit" if seen else "SERVES ANOTHER'S", "· index",
                (ti.common_git_dir(where) / "gov" / "index.db").as_posix())
        same = ti.common_git_dir(root) == ti.common_git_dir(other)
        say("both worktrees share one index" if same else "the worktrees hold TWO indexes")
        return 0 if ok and same else 1
    if plant == "one-commit":
        run_verb(root, "rebuild", None, sets=sets)
        write_commit(root, {"AGENTS.md": "# Charter\n\n## Practices\n\nchanged\n"}, "one file")
        return 0 if run_verb(root, "rebuild", None, sets=sets) == 1 else 1
    if plant == "slice":
        return run_verb(root, "show", "layer.memory", sets=sets)
    if plant == "retired":
        base = run_git(root, "rev-parse", "HEAD").strip()
        write_commit(root, {"memory/guides/ALPHA.md": GUIDE + "\nsee `practice.old`\n"}, "cite a retired tag")
        return run_verb(root, "check", None, sets=sets, base=base)
    if plant in ("retired-old", "retired-reminted"):
        return run_verb(root, "check", None, sets=sets, base=run_git(root, "rev-parse", "HEAD").strip())
    return run_verb(root, "check", None, sets=sets)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="gov_tag.py", description="the tag resolver (gov tag)")
    ap.add_argument("verb", nargs="?", choices=("show", "where", "refs", "check"))
    ap.add_argument("address", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--base")
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--list-positional", action="store_true")
    ap.add_argument("--fixture", action="store_true")
    ap.add_argument("--plant", default="none")
    ap.add_argument("--set", action="append", default=[], metavar="KEY=VALUE")
    a = ap.parse_args(argv)
    sets = {}
    for item in a.set:
        key, eq, value = item.partition("=")
        if not eq:
            ap.error(f"--set takes <key>=<value>, not {item}")
        sets[key] = value
    if sets and not a.fixture:
        print("tags: --set is honoured under --fixture only", file=sys.stderr)
        return 2
    try:
        if a.fixture:
            return run_fixture(a.plant, sets)
        root = resolve_repo_root()
        if a.list_positional:
            for row in read_positional(root):
                print(row)
            return 0
        if a.rebuild:
            remove_index(root)
            run_kit_verb(root, "rebuild", None, sets={})
            return 0
        if not a.verb:
            ap.error("a verb, --rebuild, --list-positional or --fixture")
        return run_kit_verb(root, a.verb, a.address, sets={}, as_json=a.json, base=a.base)
    except PolicyRefused as exc:
        print(f"tags: refused · {exc.key} · {exc.line}", file=sys.stderr)
        return 2
    except ti.TagError as exc:
        print(f"tags: refused · {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
