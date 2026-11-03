"""gov_tag — the one tag resolver, standing in for `gov tag` (PLAY-dOrderedCharter-19 S6, §8 F1).

    python gov_tag.py show|where|refs|check <address> [--json]
    python gov_tag.py check [--base <rev>]
    python gov_tag.py --rebuild | --gc | --list-positional
    python gov_tag.py --fixture --plant <case> [--set <key>=<value>]

`show` returns the tag's row, or its subtree as `tags.slice` says; `where` prints `path:line`; `refs`
prints every citation of it, a build record's too; `check` runs the `retired`, `resolves` and `owned`
arms over the citations outside `<MEMORY_ROOT>/builds/`, and the shape check, the joins and the
name-check slot (PLAY-dOrderedCharter-10), and the `purpose` arm, the namespace rows' `owner` and
`purpose-source` and the chain registry joined to the design view (PLAY-dOrderedCharter-22), and the `positional` arm, the
tree's positional references against `positional-refs.txt` with every pinned line and symbol citation resolved
(PLAY-dOrderedCharter-26, `positional.py`). An address is a tag, `doc.<name>#<seg>`, or a
positional label `aliases.toml` maps. `--gc` collects the index rows of every extractor version no live
worktree derives (PLAY-dOrderedCharter-51 S5). Every line opens `tags:`; `--json` is the index's only JSON.
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
import types

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


def derive_build_counts(state) -> str:
    """A build's summary: blobs parsed, extractor runs, and (blob, extractor) pairs skipped as fresh."""
    n = state["parsed"]
    return (f"{n} blob{'s' if n != 1 else ''} parsed, {sum(state['runs'].values())} extractor runs, "
            f"{sum(state['skipped'].values())} skipped as fresh")


def run_kit_verb(root, verb, address, *, sets, as_json=False, base=None, kit_rel=None) -> int:
    kit_rel = kit_rel or derive_kit_rel(root)
    ctx = ti.derive_context(root, root / kit_rel / "namespaces.toml")
    aliases = ti.read_aliases(root / kit_rel / "aliases.toml")
    con = ti.load_index(root)
    try:
        state = ti.load_view(con, root, ctx)
        if verb == "rebuild":
            print(f"tags: index {state['tree'][:12]} built, {derive_build_counts(state)}")
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


def run_gc(root, kit_rel) -> int:
    """`--gc`: the rows of every extractor version no live worktree derives leave the index, one line
    saying how many; a worktree whose registry cannot be read refuses it, a TagError (exit 2)."""
    con = ti.load_index(root)
    try:
        rows, versions = ti.remove_dead_versions(con, root, kit_rel)
    finally:
        con.close()
    print(f"tag-index — collected: {rows} rows of {versions} versions")
    return 0


NAME_CHECK = "slot point.instruction.name-check"


def run_name_check(root, tags) -> tuple[list, str]:
    """S6, the name-check point: where the lexicon kit resolves, every shape-graded tag goes to its
    `lexicon.py --tags` in one call, which reads the namespace words from the registry itself (§8 F2).
    -> (reds, the slot line). No kit is the declared fallback; an answer it cannot give is red."""
    from policy_value import resolve_kit_dir
    try:
        lex = resolve_kit_dir("lexicon", "lexicon.py", KIT_DIR) / "lexicon.py"
    except LookupError:
        return [], f"{NAME_CHECK} · not-installed: the shape check stands alone"
    p = subprocess.run([sys.executable, str(lex), "--tags"], input="".join(f"{t}\n" for t in sorted(set(tags))),
                       capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(root))
    if p.returncode == 0:
        return [], f"{NAME_CHECK} · searched-empty"
    lines = [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]
    if p.returncode == 1:
        return [f"tags: name-check · {ln}" for ln in lines if ln.startswith("lexicon: tag ")], f"{NAME_CHECK} · filled"
    return [f"tags: name-check · the lexicon could not answer (exit {p.returncode}): {ln}" for ln in lines[-3:]], \
        f"{NAME_CHECK} · filled"


def run_purpose_check(con, root, ctx) -> tuple[list, list, dict]:
    """The `purpose` arm (PLAY-dOrderedCharter-22 S5): the namespace rows' `owner` and `purpose-source`
    against the chain registry, then the registry joined to the design view, or one line saying there is
    no chain to read where the DESIGN_* keys are blank. -> (reds, lines, the summary's counts)."""
    chain_rel = f"{ctx['memory_root']}/{ti.CHAIN_REGISTRY}"
    chain = ti.read_chain_registry(root / chain_rel)
    reds, ns = ti.check_namespace_purpose(con, ctx, chain, chain_rel)
    from design_lib import read_design_conf  # memory-tree is on sys.path once derive_context has run
    c_reds, cs = ti.check_chain_registry(root, read_design_conf(root), chain, chain_rel)
    graded = ns["graded"]
    lines = [f"tags: purpose · pending {n} · {src}" for n, src in ns["pending"]]
    lines.append(f"tags: purpose · {len(graded)} graded over {sum(graded.values())} members, "
                 f"{len(ns['path_only'])} path-only, pending {len(ns['pending'])}")
    if cs is None:
        lines.append("tags: purpose · no chain to read: the DESIGN_* keys are blank, so the chain registry is not "
                     "joined")
    else:
        lines.append(f"tags: purpose · {cs['rows']} registry rows joined to {cs['builds']} view builds, "
                     f"{len(cs['awaiting'])} rows awaiting PM-5's review")
    counts = {"graded": graded, "path_only": ns["path_only"], "pending": [list(p) for p in ns["pending"]],
              "chain": cs}
    return reds + c_reds, lines, counts


def run_check(con, root, ctx, kit_rel, *, sets, base, as_json, state) -> int:
    counts = ti.derive_namespace_state(con, ctx)
    armed = counts  # ns -> defined-tag count; 0 is unarmed
    bare_mode = read_key("tags.bare-refs", root, sets, lambda: read_policy_value("tags.bare-refs", root)[0][0])
    retired_mode = read_key("tags.retired-cites", root, sets,
                            lambda: read_policy_value("tags.retired-cites", root)[0][0])
    file_names = ti.read_view_file_names(con)
    reds, shaped = ti.check_tag_shape(con, ctx)
    j_reds, j_lines = ti.check_namespace_joins(con, ctx, file_names)
    s_reds, c = ti.check_resolves(con, ctx, bare_mode, armed, file_names)
    reds += j_reds + s_reds
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
    n_reds, slot = run_name_check(root, shaped)
    p_reds, p_lines, purpose = run_purpose_check(con, root, ctx)
    from edge_grammar import check_native_classes   # PLAY-dOrderedCharter-28 S2: the native-id classes
    x_reds, x_lines = check_native_classes(root, root / kit_rel / "namespaces.toml")
    p_lines += x_lines
    from positional import check_positional, read_positional_mode  # PLAY-dOrderedCharter-26: the positional arm
    q_reds, q_lines, positional = check_positional(root, kit_rel, read_positional_mode(root, sets), ctx["memory_root"])
    p_lines += q_lines
    reds += r_reds + o_reds + n_reds + p_reds + x_reds + q_reds
    tags = sum(counts.values())
    unread = con.execute("SELECT COUNT(*) FROM view_path WHERE path NOT LIKE '%.md'").fetchone()[0]
    summary = {
        "namespaces": len(counts), "tags": tags, "graded": c["graded"], "unresolved": c["unresolved"],
        "retired_cited": cited, "bare_refs": c["bare"], "records_not_graded": c["records"], "paths_not_markdown": unread,
        "shape_graded": len(shaped), "file_names_not_graded": c["file_names"], "name_check": slot,
        "unarmed": {ns: c["unarmed"].get(ns, 0) for ns, n in counts.items() if not n},
        "purpose": purpose, "positional": positional, "reds": reds, "warns": warns, "blobs_parsed": state["parsed"],
        "extractor_runs": sum(state["runs"].values()), "skipped_fresh": sum(state["skipped"].values()),
    }
    if as_json:
        print(json.dumps(summary, indent=2, sort_keys=True))
        return 1 if reds else 0
    for line in c["notes"] + j_lines + p_lines + warns + reds:
        print(line)
    print(f"tags: {slot}")
    print(f"tags: {len(counts)} namespaces, {tags} tags, {len(shaped)} shape-graded, {c['graded']} citations graded, "
          f"{c['unresolved']} unresolved, {cited} retired-cited, {c['bare']} bare refs; {c['file_names']} file names "
          f"not graded; {c['records']} in build records not graded; {unread} paths outside Markdown not read; "
          f"{derive_build_counts(state)}")
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
purpose-source = "AGENTS.md"
join-armed-by = "fixture"

[[namespace]]
ns = "practice"
owner = "fixture"
layer = "layer.instruction"
source = "every *.tags file"
extractor = "fixture_tags:extract_declared"
role = "describes"
purpose-source = "AGENTS.md"
join-armed-by = "fixture"

[[namespace]]
ns = "layer"
owner = "fixture"
layer = "layer.instruction"
source = "every *.tags file"
extractor = "fixture_tags:extract_declared"
role = "describes"
purpose-source = "AGENTS.md"
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
purpose-source = "AGENTS.md"
join-armed-by = "fixture"
'''
#: PLAY-dOrderedCharter-22: the fixture's chain registry, its one build owning every fixture namespace
FIXTURE_CHAIN = '[[build]]\nslug = "fixture"\npurpose = "the fixture\'s own build"\n'
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
          "retired-reminted", "bare", "bare-charter", "owned", "owned-core", "scope", "scope-guide",
          "bad-ns", "bad-seg", "long-tag", "ns-word", "unregistered-cite", "dead-selector", "empty-ns",
          "escaped-word", "file-name", "new-extractor", "extractor-edit", "tagless", "schema",
          "no-owner", "ghost-owner", "no-purpose-source", "bad-purpose-source", "member-no-field", "pending-source",
          "registry-ghost", "registry-missing", "registry-joined", "new-no-purpose", "two-versions",
          "served-across", "positional-seed", "positional-new", "positional-stale", "positional-listed",
          "positional-symbol", "positional-pinned", "positional-pin", "positional-forked-before")
#: PLAY-dOrderedCharter-44's `extractor-edit`: the fixture extractor's module edited to stop yielding one tag
EDITED_EXTRACTOR = FIXTURE_EXTRACTOR.replace("elif len(word) == 1:",
                                             'elif len(word) == 1 and word[0] != "layer.memory.recall":')


def derive_fixture_row(ns, extractor, role="describes", layer="layer.instruction", purpose="AGENTS.md") -> str:
    """One fixture registry row (PLAY-dOrderedCharter-10's plants)."""
    return (f'\n[[namespace]]\nns = "{ns}"\nowner = "fixture"\nlayer = "{layer}"\nsource = "fixture"\n'
            f'extractor = "{extractor}"\nrole = "{role}"\npurpose-source = "{purpose}"\njoin-armed-by = "fixture"\n')


#: PLAY-dOrderedCharter-10 S8: each plant's registry rows and the files it adds to the base fixture
SHAPE_PLANTS = {
    "bad-ns": (FIXTURE_UNIT_ROW, {"tools/corekit/instructions.toml": '[[unit]]\ntag = "step.build"\n'}),
    "bad-seg": ("", {"tools/corekit/core.tags": "+layer.Memory\n"}),
    "long-tag": ("", {"tools/corekit/core.tags": "+layer." + "a" * 60 + "\n"}),
    "ns-word": (derive_fixture_row("repo", "fixture_tags:extract_declared"),
                {"tools/corekit/core.tags": "+practice.repo.x\n"}),
    "escaped-word": (derive_fixture_row("a.b", "fixture_tags:extract_declared"),
                     {"tools/corekit/core.tags": "+a.b.c\n"}),
    "unregistered-cite": ("", {"memory/guides/ALPHA.md": "+\nsee `layer.nowhere`\n"}),
    "dead-selector": (FIXTURE_UNIT_ROW + derive_fixture_row("reader", "tag_index:extract_reader", "selects"), {
        "tools/playbook/readers.toml": '[[reader]]\ntag = "reader.every"\n\n[[reader]]\ntag = "reader.ghost"\n',
        "tools/corekit/instructions.toml": '[[unit]]\ntag = "unit.alpha"\nscope = ["reader.every"]\n',
        "tools/corekit/core.tags": "+layer.memory.lexicon\n"}),
    "empty-ns": (derive_fixture_row("kind", "tag_index:extract_kind"),
                 {"tools/playbook/kinds.toml": "# declares nothing yet\n",
                  "memory/guides/ALPHA.md": "+\nsee `kind.x`\n"}),
    "file-name": (derive_fixture_row("kit", "tag_index:extract_kit", layer="layer.exp"),
                  {"memory/guides/ALPHA.md": "+\nedit `kit.toml`\n"}),
    # PLAY-dOrderedCharter-22: a guide with no H1 under `#h1`, and a source the fixture does not track yet
    "member-no-field": ("", {"memory/guides/BETA.md": "## Intro\n\nno title line\n"}),
    "pending-source": (derive_fixture_row("reader", "tag_index:extract_reader", "selects",
                                          purpose="tools/playbook/readers.toml#why"), {}),
}
#: PLAY-dOrderedCharter-22's registry plants: each edits the base registry's first row, `doc`'s
PURPOSE_PLANTS = {
    "no-owner": ('owner = "fixture"', 'owner = ""'),
    "ghost-owner": ('owner = "fixture"', 'owner = "dGhost"'),
    "no-purpose-source": ('purpose-source = "AGENTS.md"', 'purpose-source = ""'),
    "bad-purpose-source": ('purpose-source = "AGENTS.md"', 'purpose-source = "AGENTS.md#practices"'),
    "member-no-field": ('purpose-source = "AGENTS.md"', 'purpose-source = "#h1"'),
}
#: PLAY-dOrderedCharter-22's chain plants: the fixture design's two builds, and each plant's registry rows
DESIGN_BUILDS = ("dFixtureOne", "dFixtureTwo")
CHAIN_PLANTS = {
    "registry-joined": [{"slug": b} for b in DESIGN_BUILDS],
    "registry-ghost": [{"slug": b} for b in DESIGN_BUILDS] + [{"slug": "dGhost", "purpose": "no view build"}],
    "registry-missing": [{"slug": DESIGN_BUILDS[0]}],
    "new-no-purpose": [{"slug": b} for b in DESIGN_BUILDS] + [{"slug": "dFixtureNew"}],
}


def derive_chain_text(rows) -> str:
    return "".join(f'[[build]]\nslug = "{r["slug"]}"\n' + (f'purpose = "{r["purpose"]}"\n' if "purpose" in r else "")
                   + "\n" for r in rows)


def write_chain_fixture(root, plant) -> None:
    """The chain plants' design, through memory-tree's `write_design_fixture` (two builds, its pin the
    baseline), then a commit declaring the four DESIGN_* keys at it, the namespace rows owned by the first
    build, and the plant's registry; `new-no-purpose` adds a view build no baseline row names."""
    ti.load_memory_tree()
    from design_lib import write_design_fixture
    record, view = "memory/builds/fixture/record.md", "memory/builds/fixture/view.md"
    repo = types.SimpleNamespace(record=record, view=view, builds=DESIGN_BUILDS,
                                 clause_ids=("cl-dFixtureOne-0001", "cl-dFixtureOne-0002", "cl-dFixtureTwo-0001"),
                                 write_commit=lambda files, msg: write_commit(root, files, msg), read_sha=lambda s: s)
    pin = write_design_fixture(repo)
    reg = f"{FIXTURE_KIT}/namespaces.toml"
    conf = (root / ".memory-tree.conf").read_text(encoding="utf-8")
    files = {".memory-tree.conf": conf + f'DESIGN_RECORD="{record}"\nDESIGN_BASELINE="{pin}"\nDESIGN_VIEW="{view}"\n'
                                         'DESIGN_NODES="memory/builds/fixture/nodes.py"\n',
             reg: (root / reg).read_text(encoding="utf-8").replace('owner = "fixture"', f'owner = "{DESIGN_BUILDS[0]}"'),
             "memory/project/chain.toml": derive_chain_text(CHAIN_PLANTS[plant])}
    if plant == "new-no-purpose":
        files[view] = (root / view).read_text(encoding="utf-8") + \
            "| dFixtureNew | `cl-dFixtureNew-0001` | the fixture's new build's clause | baseline |\n"
    write_commit(root, files, "the design declared, and the chain registry")


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
        "memory/project/chain.toml": FIXTURE_CHAIN,
        f"{kit}/positional-refs.txt": "",  # PLAY-dOrderedCharter-26: present and empty, so the arm is unarmed
    }
    if plant in PURPOSE_PLANTS:
        old, new = PURPOSE_PLANTS[plant]
        files[f"{kit}/namespaces.toml"] = files[f"{kit}/namespaces.toml"].replace(old, new, 1)
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
    if plant == "tagless":  # a blob the extractor reads and takes no row from
        files["tools/corekit/none.tags"] = "# declares nothing\n"
    if plant in SHAPE_PLANTS:
        rows, extra = SHAPE_PLANTS[plant]
        files[f"{kit}/namespaces.toml"] += rows
        for rel, text in extra.items():  # a leading `+` appends to the base file
            files[rel] = files[rel] + text[1:] if text.startswith("+") else text
    write_commit(root, files, "base")
    if plant in CHAIN_PLANTS:
        write_chain_fixture(root, plant)
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
    """The index rows the fixture worktree at `root` reads at its HEAD, at its own extractor versions."""
    ctx = ti.derive_context(root, root / FIXTURE_KIT / "namespaces.toml")
    tree = ti.read_git(root, "rev-parse", "HEAD^{tree}").strip()
    con = ti.load_index(root)
    try:
        return ti.read_index_rows(con, ctx, tree)
    finally:
        con.close()


def remove_index(root) -> None:
    (ti.common_git_dir(root) / "gov" / "index.db").unlink(missing_ok=True)


def run_plant(root, top, plant, sets) -> int:
    say = lambda *a: print("tags: plant " + plant + " · " + " ".join(map(str, a)))  # noqa: E731

    def run_verb(*args, **kw):  # every verb of a plant reads the fixture's own kit directory
        return run_kit_verb(*args, kit_rel=FIXTURE_KIT, **kw)
    if plant.startswith("positional-"):
        return run_positional_plant(root, top, plant, say, lambda: run_verb(root, "check", None, sets=sets))

    def read_cold_dump():  # the rows a build from nothing writes for the same HEAD
        remove_index(root)
        run_verb(root, "rebuild", None, sets=sets)
        return read_dump(root)

    def print_equal(incremental, cold):
        say("incremental rows", "equal" if incremental == cold else "DIFFER from", "a cold build's")
        return incremental == cold
    # PLAY-dOrderedCharter-44's four: freshness keyed on blob, extractor and version, and the schema stamp
    if plant == "new-extractor":
        run_verb(root, "rebuild", None, sets=sets)
        reg = f"{FIXTURE_KIT}/namespaces.toml"  # a second extractor over the `*.tags` blobs that hold rows
        write_commit(root, {reg: (root / reg).read_text(encoding="utf-8")
                            + derive_fixture_row("kind", "fixture_again:extract_again"),
                            f"{FIXTURE_KIT}/fixture_again.py": FIXTURE_EXTRACTOR.replace("extract_declared",
                                                                                         "extract_again")},
                     "register a second extractor")
        run_verb(root, "rebuild", None, sets=sets)
        incremental = read_dump(root)
        rows = sum(1 for r in incremental if r.startswith("blob_row\t") and "\tfixture_again:extract_again\t" in r)
        say(f"the new extractor's rows over the old blobs: {rows}")
        return 0 if print_equal(incremental, read_cold_dump()) and rows else 1
    if plant == "extractor-edit":
        run_verb(root, "rebuild", None, sets=sets)
        write_commit(root, {f"{FIXTURE_KIT}/fixture_tags.py": EDITED_EXTRACTOR}, "edit the extractor")
        edited = "fixture_tags:extract_declared"
        con = ti.load_index(root)
        try:
            ctx = ti.derive_context(root, root / FIXTURE_KIT / "namespaces.toml")
            state = ti.load_view(con, root, ctx)
            # PLAY-dOrderedCharter-51 S2: the old version's rows stay for another worktree, and are not served
            old = con.execute(ti.VIEW_ROWS + " WHERE p.extractor=? AND p.tag='layer.memory.recall'",
                              (edited,)).fetchall()
            old = len(old)
        finally:
            con.close()
        others = {ex: n for ex, n in state["runs"].items() if ex != edited}
        say(f"{edited} re-ran over {state['runs'][edited]} blobs, {state['skipped'][edited]} skipped;",
            f"the others ran {sum(others.values())} times, {sum(state['skipped'].values())} skipped as fresh;",
            f"{old} rows of the old version served")
        fresh = state["runs"][edited] and not others and not state["skipped"][edited] and not old
        return 0 if print_equal(read_dump(root), read_cold_dump()) and fresh else 1
    if plant == "tagless":
        run_verb(root, "rebuild", None, sets=sets)
        write_commit(root, {"AGENTS.md": "# Charter\n\n## Practices\n\nchanged\n"}, "one file")
        first = run_verb(root, "rebuild", None, sets=sets)
        con = ti.load_index(root)
        with con:  # no change, and the tree walked again: only the ledger keeps the tagless blob unread
            con.execute("DELETE FROM tree_built")
        con.close()
        second = run_verb(root, "rebuild", None, sets=sets)
        say(f"{first} blob parsed after one file changed, {second} on a build with no change")
        return 0 if (first, second) == (1, 0) else 1
    if plant == "schema":
        run_verb(root, "rebuild", None, sets=sets)
        con = ti.load_index(root)
        with con:  # a file of unit 19's shape: no stamp, and a `parsed` sentinel among its blob rows
            blob = con.execute("SELECT blob FROM tree_path LIMIT 1").fetchone()[0]
            con.execute("INSERT INTO blob_row VALUES (?,?,?,?,?,?,?,?)",
                        (blob, ti.CITATIONS, "", "", "parsed", 0, 0, ""))
            con.execute("PRAGMA user_version = 0")
        con.close()
        run_verb(root, "rebuild", None, sets=sets)
        after = read_dump(root)
        con = ti.load_index(root)
        stamp = con.execute("PRAGMA user_version").fetchone()[0]
        con.close()
        say(f"stamped {stamp} after the build;")
        return 0 if print_equal(after, read_cold_dump()) and stamp == ti.INDEX_SCHEMA else 1
    # PLAY-dOrderedCharter-51's two: each extractor version's rows kept apart, each worktree served its own
    if plant == "two-versions":
        other, edited = top / "wt2", "fixture_tags:extract_declared"
        run_git(root, "worktree", "add", "-q", str(other), "-b", "two")
        write_commit(other, {f"{FIXTURE_KIT}/fixture_tags.py": EDITED_EXTRACTOR}, "edit the extractor in two")
        both = (root, other)
        cold = {}
        for where in both:  # each worktree's rows from nothing, the other's never built
            remove_index(root)
            run_verb(where, "rebuild", None, sets=sets)
            cold[where] = read_dump(where)
        remove_index(root)
        for where in both:
            run_verb(where, "rebuild", None, sets=sets)
        second = [run_verb(where, "rebuild", None, sets=sets) for where in both]
        same = [print_equal(read_dump(where), cold[where]) for where in both]
        gone = ti.derive_context(other, other / FIXTURE_KIT / "namespaces.toml")
        con = ti.load_index(root)
        try:
            held = con.execute("SELECT COUNT(DISTINCT version) FROM blob_parsed WHERE extractor=?",
                               (edited,)).fetchone()[0]
        finally:
            con.close()
        say(f"round 2 parsed {second[0]} and {second[1]} blobs; {held} versions of {edited} held side by side")
        before = read_dump(root)
        run_git(root, "worktree", "remove", "--force", str(other))
        run_git(root, "worktree", "prune")
        rc = run_gc(root, FIXTURE_KIT)
        con = ti.load_index(root)
        try:
            left = sum(con.execute(f"SELECT COUNT(*) FROM {t} WHERE extractor=? AND version=?",
                                   (edited, gone["versions"][edited])).fetchone()[0]
                       for t in ("blob_row", "path_row", "blob_parsed"))
            left += con.execute("SELECT COUNT(*) FROM tree_built WHERE versions=?", (gone["digest"],)).fetchone()[0]
        finally:
            con.close()
        kept = read_dump(root) == before
        say(f"two removed and pruned, --gc left {left} rows of its version;",
            "the live dump unchanged" if kept else "the live dump CHANGED")
        return 0 if all(same) and second == [0, 0] and held == 2 and rc == 0 and not left and kept else 1
    if plant == "served-across":
        other = top / "wt2"
        run_git(root, "worktree", "add", "-q", str(other), "-b", "two")
        run_verb(root, "rebuild", None, sets=sets)
        write_files(other, {f"{FIXTURE_KIT}/fixture_tags.py": EDITED_EXTRACTOR})  # one tree, another version
        parsed, served = [], []
        for where in (other, root):  # one still serves the tag its version yields: the zero is not vacuous
            con = ti.load_index(where)
            try:
                ctx = ti.derive_context(where, where / FIXTURE_KIT / "namespaces.toml")
                parsed.append(ti.load_view(con, where, ctx)["parsed"])
                served.append(len(ti.resolve_address(con, "layer.memory.recall")))
            finally:
                con.close()
        say(f"two parsed {parsed[0]} blobs on the tree one built; served {served[0]} rows of one's version,",
            f"and one serves {served[1]}")
        return 0 if parsed[0] and not served[0] and served[1] else 1
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
        same = print_equal(read_dump(root), read_cold_dump())
        rc = run_verb(root, "where", "doc.alpha#intro", sets=sets)
        return 0 if same and rc == 0 else 1
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
    if plant in ("dead-selector", "file-name"):  # the plant's exit, then its second half's on one line
        rc = run_verb(root, "check", None, sets=sets)
        if plant == "dead-selector":
            write_commit(root, {"tools/playbook/readers.toml": '[[reader]]\ntag = "reader.every"\n'}, "no ghost")
            half = "without reader.ghost"
        else:
            run_git(root, "mv", "tools/corekit/kit.toml", "tools/corekit/corekit.kit.toml")
            run_git(root, "mv", "tools/expkit/kit.toml", "tools/expkit/expkit.kit.toml")
            write_commit(root, {}, "no tracked kit.toml")
            half = "no tracked kit.toml"
        say(f"{half}: rc={run_verb(root, 'check', None, sets=sets)}")
        return rc
    if plant in ("pending-source", "new-no-purpose"):  # PLAY-dOrderedCharter-22: the source lands, the row gains a purpose
        rc = run_verb(root, "check", None, sets=sets)
        if plant == "pending-source":
            write_commit(root, {"tools/playbook/readers.toml": '[[reader]]\ntag = "reader.every"\n'}, "the source lands")
            half = "readers.toml landed with a member lacking why"
        else:
            rows = CHAIN_PLANTS[plant][:-1] + [{"slug": "dFixtureNew", "purpose": "a build the baseline does not name"}]
            write_commit(root, {"memory/project/chain.toml": derive_chain_text(rows)}, "the new row's purpose")
            half = "with a purpose"
        say(f"{half}: rc={run_verb(root, 'check', None, sets=sets)}")
        return rc
    return run_verb(root, "check", None, sets=sets)


#: PLAY-dOrderedCharter-26 S8: the positional plants' code file and its citations, spelled in parts so this
#: file holds no file:line citation and no pinned line of its own
POS_CODE = "tools/corekit/code.py"
POS_MOD = "one = 1\ntwo = 2\nthree = 3\n"
POS_SYMBOLS = {
    "tools/corekit/mod.py": "DELTA = 1\n\n\ndef alpha():\n    pass\n\n\nclass Beta:\n    def gamma(self):\n        pass\n",
    "tools/corekit/run.sh": "#!/usr/bin/env bash\nepsilon() {\n  :\n}\n",
    "tools/corekit/app.js": "function zeta() {}\nconst eta = 1\n",
}


def derive_cite(n, oid=None) -> str:
    return f"{POS_CODE}{'@' + oid if oid else ''}:{n}"


def run_positional_plant(root, top, plant, say, check) -> int:
    """S8's seven plants and PLAY-dOrderedCharter-47's forked-before plant over the fixture's own list. `check` runs the fixture's whole `check`, whose
    `positional` arm each plant moves; a plant of several steps returns 0 only when every step held."""
    import positional as pos
    kit, guide = FIXTURE_KIT, "memory/guides/ALPHA.md"
    list_path = pos.derive_list_path(root, kit)

    def read_rows():
        return pos.read_list(list_path) or []
    if plant == "positional-seed":
        write_commit(root, {POS_CODE: POS_MOD, "AGENTS.md": "# Charter\n\nsee HYGIENE check 5\n",
                            guide: GUIDE + f"\nsee {derive_cite(1)}, {derive_cite('2-3')} and {derive_cite(1)} again\n",
                            "memory/guides/BETA.md": f"# Beta\n\nread BUILD-METHOD M5, and {derive_cite(1)}\n",
                            f"{kit}/positional-refs.txt": "AGENTS.md\tHYGIENE check 5\n"}, "citations")
        pos.run_seed(root, kit)
        want = {"AGENTS.md\tHYGIENE check 5", f"{guide}\t{derive_cite(1)}", f"{guide}\t{derive_cite('2-3')}",
                f"memory/guides/BETA.md\t{derive_cite(1)}", "memory/guides/BETA.md\tBUILD-METHOD M5"}
        got = read_rows()
        same = sorted(got) == sorted(want)
        say("seed: the list holds every expected row and no other" if same else f"seed: the list DIFFERS: {got}")
        again = pos.run_seed(root, kit)
        say(f"a second seed: rc={again}")
        rc = check()
        return 0 if same and again == 1 and rc == 0 else 1
    if plant in ("positional-new", "positional-stale", "positional-listed"):
        two = f" and {derive_cite(2)}"
        cited = GUIDE + f"\nsee {derive_cite(1)}" + (two if plant == "positional-stale" else "") + ", per BUILD-METHOD M5\n"
        write_commit(root, {POS_CODE: POS_MOD, guide: cited}, "citations")
        pos.run_seed(root, kit)
        if plant == "positional-listed":
            return check()
        if plant == "positional-new":
            write_files(root, {guide: cited + f"\nand {derive_cite(2)}, per BUILD-METHOD M9\n"})
            rc = check()
            write_files(root, {guide: cited})
            say(f"without the plants: rc={check()}")
            return rc
        before = len(read_rows())
        write_files(root, {guide: cited.replace(two, "")})
        rc1 = check()
        stale = rc1 == 1 and any(r.endswith(derive_cite(2)) for r in read_rows())
        say(f"removed: rc={rc1}, stale {'named' if stale else 'NOT named'}")
        pos.run_shrink(root, kit)
        after, rc2 = len(read_rows()), check()
        say(f"after shrink: {after - 1} rows, rc={rc2}")  # the M5 row aside
        write_files(root, {guide: cited.replace(two, f" and {derive_cite(3)}")})
        pos.run_shrink(root, kit)
        again, rc3 = len(read_rows()), check()
        say(f"a new citation planted: shrink left {again - 1} rows, rc={rc3}")
        return 0 if stale and after == before - 1 and rc2 == 0 and again == after and rc3 == 1 else 1
    if plant == "positional-symbol":
        cites = (("mod.py", "alpha"), ("mod.py", "Beta.gamma"), ("mod.py", "DELTA"), ("run.sh", "epsilon"),
                 ("app.js", "zeta"), ("app.js", "eta"))
        live = "".join(f"see `tools/corekit/{p}#{s}`\n" for p, s in cites)
        ghost = "tools/corekit/mod.py#ghost"
        others = f"\n<!-- usage: script:{ghost} -->\n\nescaped ``{ghost}``\n\nand `tools/corekit/kit.toml#ghost`\n"
        files = dict(POS_SYMBOLS, **{guide: GUIDE + "\n" + live + f"and `{ghost}`\n" + others,
                                    "memory/builds/x/record.md": f"`{ghost}`\n",
                                    "tools/corekit/extra.toml": f'purpose-source = "{ghost}"\n',
                                    "tools/corekit/cites.py": f'GHOST = "{ghost}"\n'})
        write_commit(root, files, "symbol citations")
        rc = check()
        write_files(root, {guide: GUIDE + "\n" + live + others})
        say(f"without the live ghost: rc={check()}")
        return rc
    if plant == "positional-pinned":
        write_commit(root, {POS_CODE: POS_MOD}, "the code")
        blob = run_git(root, "rev-parse", "--short=8", f"HEAD:{POS_CODE}").strip()
        commit = run_git(root, "rev-parse", "--short=8", "HEAD").strip()
        good = f"\nsee {derive_cite(2, blob)} and {derive_cite(3, commit)}\n"
        bad = f"\nand {derive_cite(1, '0' * 8)} and {derive_cite(9, blob)}\n"
        write_commit(root, {guide: GUIDE + good + bad, "memory/builds/x/record.md": f"{derive_cite(1, '0' * 8)}\n"},
                     "pins")
        rc = check()
        write_files(root, {guide: GUIDE + good})
        say(f"without the live bad pins: rc={check()}")
        return rc
    if plant == "positional-forked-before":  # PLAY-dOrderedCharter-47 S4: a branch forked before the check lands
        record, after, cite = "memory/builds/x/build/record.md", "memory/builds/x/build/after.md", "see x.py:{}\n"
        run_git(root, "checkout", "-q", "-b", "side")
        write_commit(root, {record: cite.format(1)}, "a record on a branch forked before the check")
        run_git(root, "checkout", "-q", "main")
        write_commit(root, {f"{kit}/positional.py": "# the check\n"}, "the check lands")
        run_git(root, "merge", "-q", "--no-ff", "side", "-m", "the side branch merged")
        rc1 = check()
        write_commit(root, {after: cite.format(2)}, "a record after the merge")
        rc2 = check()
        write_commit(root, {after: None}, "the post-merge record removed")
        run_git(root, "checkout", "-q", "side")  # moved on its own branch, so its add is not the check's either
        write_commit(root, {record: None, "tools/notes.md": cite.format(1)}, "the record moved outside the records")
        run_git(root, "checkout", "-q", "main")
        run_git(root, "merge", "-q", "--no-ff", "side", "-m", "the move merged")
        rc3 = check()
        say(f"the pre-fork record: rc={rc1}; a record after the merge: rc={rc2}; "
            f"the pre-fork record moved under tools: rc={rc3}")
        return 0 if (rc1, rc2, rc3) == (0, 1, 1) else 1
    # positional-pin: the unlisted citation re-pinned, and a file outside the repository refused
    write_commit(root, {POS_CODE: POS_MOD, guide: GUIDE + f"\nsee {derive_cite(2)}\n"}, "a citation")
    blob = run_git(root, "rev-parse", "--short=8", f"HEAD:{POS_CODE}").strip()
    pinned = pos.run_pin(root, kit, root / guide)
    text = (root / guide).read_text(encoding="utf-8")
    rc = check()
    ok = pinned == 0 and derive_cite(2, blob) in text and derive_cite(2) + "\n" not in text and rc == 0
    say(f"pin {'rewrote the citation to the blob at HEAD' if ok else 'did NOT rewrite the citation'}; check: rc={rc}")
    outside = top / "outside.md"
    outside.write_text(f"see {derive_cite(2)}\n", encoding="utf-8")
    out_rc = pos.run_pin(root, kit, outside)
    kept = outside.read_text(encoding="utf-8") == f"see {derive_cite(2)}\n"
    say(f"pin outside the repository: rc={out_rc}, {'nothing written' if kept else 'the file WRITTEN'}")
    return 0 if ok and out_rc == 1 and kept else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="gov_tag.py", description="the tag resolver (gov tag)")
    ap.add_argument("verb", nargs="?", choices=("show", "where", "refs", "check"))
    ap.add_argument("address", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--base")
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--gc", action="store_true")
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
        if a.gc:
            return run_gc(root, derive_kit_rel(root))
        if a.rebuild:
            remove_index(root)
            run_kit_verb(root, "rebuild", None, sets={})
            return 0
        if not a.verb:
            ap.error("a verb, --rebuild, --gc, --list-positional or --fixture")
        return run_kit_verb(root, a.verb, a.address, sets={}, as_json=a.json, base=a.base)
    except PolicyRefused as exc:
        print(f"tags: refused · {exc.key} · {exc.line}", file=sys.stderr)
        return 2
    except ti.TagError as exc:
        print(f"tags: refused · {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
