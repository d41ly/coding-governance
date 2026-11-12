"""gov_tag — the one tag resolver, standing in for `gov tag` (PLAY-dOrderedCharter-19 S6, §8 F1).

    python gov_tag.py show|where|refs|check <address> [--json]
    python gov_tag.py bundle <address> [--inline --bytes <n>] [--under <dir>] [--json]
    python gov_tag.py check [--base <rev>] [--only type-registered|target-resolves]
    python gov_tag.py --rebuild | --gc | --list-positional
    python gov_tag.py --fixture --plant <case> [--set <key>=<value>]

`show` returns the tag's row, or its subtree as `tags.slice` says, or for a tag only a `retired` row holds that
row, its redirect; `where` prints `path:line`; `refs`
prints every citation of it, a build record's too; `check` runs the `retired`, `resolves` and `owned`
arms over the citations outside `<MEMORY_ROOT>/builds/`, and the shape check, the joins and the
name-check slot (PLAY-dOrderedCharter-10), and the `purpose` arm, the namespace rows' `owner` and
`purpose-source` and the chain registry joined to the design view (PLAY-dOrderedCharter-22), and the `positional` arm, the
tree's positional references against `positional-refs.txt` with every pinned line and symbol citation resolved
(PLAY-dOrderedCharter-26, `positional.py`), the list under `<MEMORY_ROOT>/project/` (PLAY-dOrderedCharter-72).
`bundle` prints the node and every inbound edge as ranges to pull, and `check --only` runs one edge arm alone (PLAY-dOrderedCharter-25, `tag_bundle.py`). An address is a tag, `doc.<name>#<seg>`, or a
positional label `aliases.toml` maps. `--gc` collects the index rows of every extractor version no live
worktree derives (PLAY-dOrderedCharter-51 S5). Every line opens `tags:`; `--json` is the index's only JSON.
Exit 0 green, 1 red, 2 a refusal (an unreadable registry, a refused policy read, a locked index).

The policy keys are read through `policy_value.read_policy_value`, the committed policy at its landed
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

import instruction_units  # noqa: E402  PLAY-dOrderedCharter-72: the fixture's kit at this install's layout
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


def read_refs(con, tag) -> list[dict]:
    """Every citation of `tag`, `{path, line}` each: `refs`' rows, and a bundle's `cites` rows."""
    return [{"path": p, "line": n} for _t, p, n, *_ in ti.read_rows(con, ("span",), tag=tag)]


def read_retired_rows(con, tag) -> list[dict]:
    """`tag`'s `retired` rows, `show`'s fallback where no definition holds it. A retired row is a name and no
    prefix, so `tags.slice` does not reach it, and no other read serves it: nothing resolves it as live."""
    out = []
    for t, path, line, kind, blob, ex in ti.read_rows(con, ("retired",), tag=tag):
        end, text = ti.read_text_of(con, blob, ex, kind, line)
        out.append({"tag": t, "path": path, "line": line, "end_line": end, "kind": kind, "text": text})
    return out


def run_bundle_verb(con, root, kit_rel, address, aliases, *, sets, opts, as_json) -> int:
    """`bundle` (PLAY-dOrderedCharter-25 S1-S4): the node `show` resolves, then tag_bundle's manifest."""
    import tag_bundle
    mode = read_key("tags.bundle", root, sets, lambda: read_policy_value("tags.bundle", root)[0][0])
    budget = read_key("tags.bundle-rows", root, sets, lambda: read_policy_value("tags.bundle-rows", root)[0][0])
    try:
        budget = int(budget)
    except ValueError:
        print(f"tags: refused · tags.bundle-rows is '{budget}', which is no row count", file=sys.stderr)
        return 2
    nodes = ti.resolve_address(con, address, "leaf", aliases)
    if not nodes:
        print(f"tags: {address} resolves to no row", file=sys.stderr)
        return 1
    return tag_bundle.run_bundle(root, con, root / kit_rel / "namespaces.toml", nodes[0],
                                 read_refs(con, nodes[0]["tag"]), tool_root=pathlib.PurePosixPath(kit_rel).parent.as_posix(),
                                 mode=mode, budget=budget, inline=opts.get("inline", False), nbytes=opts.get("nbytes"),
                                 under=opts.get("under"), as_json=as_json)


def run_kit_verb(root, verb, address, *, sets, as_json=False, base=None, kit_rel=None, opts=None) -> int:
    kit_rel = kit_rel or derive_kit_rel(root)
    opts = opts or {}
    ctx = ti.derive_context(root, root / kit_rel / "namespaces.toml")
    aliases = ti.read_aliases(root / kit_rel / "aliases.toml")
    con = ti.load_index(root)
    try:
        state = ti.load_view(con, root, ctx)
        if verb == "rebuild":
            print(f"tags: index {state['tree'][:12]} built, {derive_build_counts(state)}")
            return state["parsed"]
        if verb in ("show", "where", "refs", "bundle") and not address:
            print(f"tags: {verb} needs an address", file=sys.stderr)
            return 2
        if verb == "show":
            slice_ = read_key("tags.slice", root, sets, lambda: read_policy_value("tags.slice", root)[0][0])
            rows = (ti.resolve_address(con, address, slice_, aliases)
                    or read_retired_rows(con, aliases.get(address, address)))
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
            rows = read_refs(con, tag)
            if as_json:
                print(json.dumps(rows))
            for r in rows if not as_json else ():
                print(f"tags: {r['path']}:{r['line']}")
            print(f"tags: {len(rows)} citation(s) of {tag}", file=sys.stderr)
            return 0
        if verb == "bundle":
            return run_bundle_verb(con, root, kit_rel, address, aliases, sets=sets, opts=opts, as_json=as_json)
        if opts.get("only"):  # one edge arm alone, so `check`'s own verdict prints no edge red twice
            import tag_bundle
            return tag_bundle.run_edge_arm(root, con, root / kit_rel / "namespaces.toml", opts["only"], base)
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


def run_purpose_check(con, root, ctx, chain, chain_rel) -> tuple[list, list, dict]:
    """The `purpose` arm (PLAY-dOrderedCharter-22 S5): the namespace rows' `owner` and `purpose-source`
    against the chain registry `chain`, read from `chain_rel`, then the registry joined to the design view,
    or one line saying there is no chain to read where the DESIGN_* keys are blank. An owner the registry
    does not hold prints one unarmed line (PLAY-dOrderedCharter-78 S3). -> (reds, lines, the summary's
    counts)."""
    reds, ns = ti.check_namespace_purpose(con, ctx, chain)
    from design_lib import read_design_conf  # memory-tree is on sys.path once derive_context has run
    c_reds, cs = ti.check_chain_registry(root, read_design_conf(root), chain, chain_rel)
    graded = ns["graded"]
    lines = [f"tags: purpose · owner '{o}' · unarmed: no build of {chain_rel}, {len(rows)} namespace row(s) "
             "not graded for it" for o, rows in sorted(ns["unarmed"].items())]
    lines += [f"tags: purpose · pending {n} · {src}" for n, src in ns["pending"]]
    lines.append(f"tags: purpose · {len(graded)} graded over {sum(graded.values())} members, "
                 f"{len(ns['path_only'])} path-only, pending {len(ns['pending'])}")
    if cs is None:
        lines.append("tags: purpose · no chain to read: the DESIGN_* keys are blank, so the chain registry is not "
                     "joined")
    else:
        lines.append(f"tags: purpose · {cs['rows']} registry rows joined to {cs['builds']} view builds, "
                     f"{len(cs['awaiting'])} rows awaiting PM-5's review")
    counts = {"graded": graded, "path_only": ns["path_only"], "pending": [list(p) for p in ns["pending"]],
              "unarmed": ns["unarmed"], "chain": cs}
    return reds + c_reds, lines, counts


def run_check(con, root, ctx, kit_rel, *, sets, base, as_json, state) -> int:
    counts = ti.derive_namespace_state(con, ctx)
    armed = counts  # ns -> defined-tag count; 0 is unarmed
    bare_mode = read_key("tags.bare-refs", root, sets, lambda: read_policy_value("tags.bare-refs", root)[0][0])
    retired_mode = read_key("tags.retired-cites", root, sets,
                            lambda: read_policy_value("tags.retired-cites", root)[0][0])
    file_names = ti.read_view_file_names(con)
    reds, shaped = ti.check_tag_shape(con, ctx)
    j_reds, j_lines = ti.check_namespace_joins(con, ctx, file_names, every=instruction_units.EVERY)
    s_reds, c = ti.check_resolves(con, ctx, bare_mode, armed, file_names)
    reds += j_reds + s_reds
    base_spans, base_sections, base_why = None, None, ""
    has_retired = con.execute(ti.VIEW_ROWS + " WHERE p.kind='retired' LIMIT 1").fetchone()
    if base is None:  # PLAY-dOrderedCharter-29 S8: the base's section rows are read on every run
        from_mt = ti.load_memory_tree()  # noqa: F841 - puts memory-tree on sys.path
        from coverage_join import resolve_compare_base
        base, base_why = resolve_compare_base(root)
    if base:
        base_tree = ti.read_git(root, "rev-parse", f"{base}^{{tree}}").strip()
        ti.load_view(con, root, ctx, tree=base_tree, overlay=False)
        if has_retired:
            base_spans = {(p, t) for t, p, *_ in ti.read_rows(con, ("span",))}
        base_sections = {t for t, *_ in ti.read_rows(con, ("section",))}
        ti.load_view(con, root, ctx)
    else:
        print(f"tags: retired: no base ({base_why}), so every citation reads as new and no section as vanished")
    aliases = ti.read_aliases(root / kit_rel / "aliases.toml")
    r_reds, warns, cited = ti.check_retired(con, ctx, retired_mode, base_spans, armed, base_sections, aliases)
    o_reds = ti.check_owned(con, ctx, root / kit_rel / "layers.toml")
    n_reds, slot = run_name_check(root, shaped)
    chain_rel = f"{ctx['memory_root']}/{ti.CHAIN_REGISTRY}"  # read once, for the two arms that grade owners
    chain = ti.read_chain_registry(root / chain_rel)
    p_reds, p_lines, purpose = run_purpose_check(con, root, ctx, chain, chain_rel)
    from edge_grammar import check_native_classes   # PLAY-dOrderedCharter-28 S2: the native-id classes
    x_reds, x_lines = check_native_classes(root, root / kit_rel / "namespaces.toml", {r["slug"] for r in chain})
    p_lines += x_lines
    from positional import check_positional, read_positional_mode  # PLAY-dOrderedCharter-26: the positional arm
    q_reds, q_lines, positional = check_positional(root, kit_rel, read_positional_mode(root, sets), ctx["memory_root"])
    p_lines += q_lines
    u_reds, u_lines = ti.check_unclosed(con, ctx)  # PLAY-dOrderedCharter-68: a fence that never closes
    p_lines += u_lines
    reds += r_reds + o_reds + n_reds + p_reds + x_reds + q_reds + u_reds
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
extractor = "instruction_units:extract_unit"
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
ALIASES = '[[alias]]\nref = "ALPHA M5"\ntarget = "doc.alpha#m5-recall-and-reuse"\n'
GUIDE = "# Alpha\n\n## Intro\n\nthe intro text\n\n## M5 — Recall and reuse\n\nrecall first\n"
FIXTURE_KIT = instruction_units.derive_tool_rel(KIT_DIR.name)  # the fixture lays its kit out at this install's layout
#: PLAY-dOrderedCharter-68's two plants: a fence opened and never closed, then the citation it hides
UNCLOSED = "\n```\nand [doc.nope]\n"
PLANTS = ("none", "rebuild", "two-paths", "dirty", "one-commit", "slice", "retired", "retired-old",
          "retired-reminted", "bare", "bare-charter", "owned", "owned-core", "scope", "scope-guide",
          "bad-ns", "bad-seg", "long-tag", "ns-word", "unregistered-cite", "dead-selector", "unscoped-unit",
          "every-selector",
          "empty-ns", "escaped-word", "file-name", "new-extractor", "extractor-edit", "tagless", "schema",
          "no-owner", "ghost-owner", "no-purpose-source", "bad-purpose-source", "member-no-field", "pending-source",
          "registry-ghost", "registry-missing", "registry-joined", "new-no-purpose", "two-versions",
          "served-across", "positional-seed", "positional-new", "positional-stale", "positional-listed",
          "positional-symbol", "positional-pinned", "positional-pin", "positional-forked-before",
          "positional-edited-after", "positional-renamed-after", "positional-uncommitted", "positional-producer-new", "positional-producer-stale", "bundle-manifest", "bundle-fold",
          "bundle-rows-values", "bundle-inline", "bundle-mode-values", "bundle-unregistered-type",
          "bundle-dangling-target", "bundle-empty-sections", "unclosed-fence", "unclosed-record", "git-env",
          "toml-row", "dirty-rename", "charter-warm", "charter-dirty", "retired-section",
          "retired-section-aliased", "retired-section-reminted", "reference-row", "reference-no-h1",
          "foreign-native", "held-native", "positional-no-tree", "positional-absent", "dirty-revert",
          "worktree-recreate", "helper-edit", "held-open", "extractor-removed", "worktree-spelling",
          "positional-spec-revbump", "positional-bulk-move", "queued-writers")
#: PLAY-dOrderedCharter-78 S4's two plants: a `family-id` native class over the fixture's own id grammar,
#: owned by a build the chain registry lacks, and by the one it holds
NATIVE_OWNERS = {"foreign-native": "dGhost", "held-native": "fixture"}
#: PLAY-dOrderedCharter-40's two plants: a fixture reference row, with its `h1` and without
REFERENCE_ROW = ('[[reference]]\nregistry = "doc.reference.fixture"\nh1 = "The fixture\'s reference page"\n'
                 'page = "help/reference/fixture.md"\n')
#: PLAY-dOrderedCharter-70 S3's `toml-row`: a list naming a tag above the row that carries it
TOML_ROWS = ('foundation = ["practice.b"]\n\n[[practice]]\ntag = "practice.a"\nline = "a"\n\n'
             '[[practice]]\ntag = "practice.b"\nline = "b"\n\n[practice.reach]\nbuild = "b"\n')
#: PLAY-dOrderedCharter-44's `extractor-edit`: the fixture extractor's module edited to stop yielding one tag
EDITED_EXTRACTOR = FIXTURE_EXTRACTOR.replace("elif len(word) == 1:",
                                             'elif len(word) == 1 and word[0] != "layer.memory.recall":')
#: PLAY-dOrderedCharter-55 S13's third version of the extractor, for the third worktree of `two-versions`
THIRD_EXTRACTOR = FIXTURE_EXTRACTOR.replace("elif len(word) == 1:",
                                            'elif len(word) == 1 and word[0] != "layer.memory":')
#: PLAY-dOrderedCharter-55 S15's `helper-edit`: the fixture extractor importing a helper module beside it
HELPED_EXTRACTOR = FIXTURE_EXTRACTOR.replace(
    "\n\n\ndef extract_declared",
    "\nimport os\nimport sys\n\nsys.path.insert(0, os.path.dirname(__file__))\n"
    "import fixture_helper  # noqa: E402,F401  the helper whose edit the version sees\n\n\ndef extract_declared")


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
        f"{FIXTURE_KIT}/readers.toml": '[[reader]]\ntag = "reader.one"\n\n[[reader]]\ntag = "reader.ghost"\n',
        "tools/corekit/instructions.toml": '[[unit]]\ntag = "unit.alpha"\nscope = ["reader.one"]\n',
        "tools/corekit/core.tags": "+layer.memory.lexicon\n"}),
    # PLAY-dOrderedCharter-88: a unit scoped `reader.every` is in every reader's load set, so each selects it
    "every-selector": (FIXTURE_UNIT_ROW + derive_fixture_row("reader", "tag_index:extract_reader", "selects"), {
        f"{FIXTURE_KIT}/readers.toml": '[[reader]]\ntag = "reader.every"\n\n[[reader]]\ntag = "reader.ghost"\n',
        "tools/corekit/instructions.toml": '[[unit]]\ntag = "unit.alpha"\nscope = ["reader.every"]\n'}),
    # PLAY-dOrderedCharter-75: a unit row with no `scope` leaves the `reader` join unarmed
    "unscoped-unit": (FIXTURE_UNIT_ROW + derive_fixture_row("reader", "tag_index:extract_reader", "selects"), {
        f"{FIXTURE_KIT}/readers.toml": '[[reader]]\ntag = "reader.every"\n',
        "tools/corekit/instructions.toml": '[[unit]]\ntag = "unit.alpha"\n'}),
    "empty-ns": (derive_fixture_row("kind", "tag_index:extract_kind"),
                 {f"{FIXTURE_KIT}/kinds.toml": "# declares nothing yet\n",
                  "memory/guides/ALPHA.md": "+\nsee `kind.x`\n"}),
    "file-name": (derive_fixture_row("kit", "tag_index:extract_kit", layer="layer.exp"),
                  {"memory/guides/ALPHA.md": "+\nedit `kit.toml`\n"}),
    # PLAY-dOrderedCharter-22: a guide with no H1 under `#h1`, and a source the fixture does not track yet
    "member-no-field": ("", {"memory/guides/BETA.md": "## Intro\n\nno title line\n"}),
    "pending-source": (derive_fixture_row("reader", "tag_index:extract_reader", "selects",
                                          purpose="{prefix}/playbook/readers.toml#why"), {}),
    # PLAY-dOrderedCharter-40: a reference row's registry tag, graded by `doc`'s `#h1` on its own row
    "reference-row": ("", {f"{FIXTURE_KIT}/references.toml": REFERENCE_ROW}),
    "reference-no-h1": ("", {f"{FIXTURE_KIT}/references.toml": REFERENCE_ROW.replace(
        'h1 = "The fixture\'s reference page"\n', "")}),
}
#: PLAY-dOrderedCharter-22's registry plants: each edits the base registry's first row, `doc`'s
PURPOSE_PLANTS = {
    "no-owner": ('owner = "fixture"', 'owner = ""'),
    "ghost-owner": ('owner = "fixture"', 'owner = "dGhost"'),
    "no-purpose-source": ('purpose-source = "AGENTS.md"', 'purpose-source = ""'),
    "bad-purpose-source": ('purpose-source = "AGENTS.md"', 'purpose-source = "AGENTS.md#practices"'),
    "member-no-field": ('purpose-source = "AGENTS.md"', 'purpose-source = "#h1"'),
    "reference-row": ('purpose-source = "AGENTS.md"', 'purpose-source = "#h1"'),
    "reference-no-h1": ('purpose-source = "AGENTS.md"', 'purpose-source = "#h1"'),
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
    kit = FIXTURE_KIT
    files = {
        ".memory-tree.conf": 'MEMORY_ROOT=memory\nCHARTER="AGENTS.md"\n',
        "AGENTS.md": "# Charter\n\n## Practices\n\nthe practices\n",
        "memory/guides/ALPHA.md": GUIDE,
        f"{kit}/namespaces.toml": FIXTURE_REGISTRY + (FIXTURE_UNIT_ROW if plant.startswith("scope") else ""),
        f"{kit}/fixture_tags.py": FIXTURE_EXTRACTOR,
        f"{kit}/layers.toml": FIXTURE_LAYERS,
        f"{kit}/aliases.toml": ALIASES,
        "tools/corekit/kit.toml": 'id = "corekit"\nlayer = "layer.instruction"\n',
        "tools/corekit/core.tags": "practice.land\npractice.memory\nlayer.memory\nlayer.memory.recall\n",
        "tools/expkit/kit.toml": 'id = "expkit"\nlayer = "layer.exp"\n',
        "tools/expkit/exp.tags": "",
        "memory/project/chain.toml": FIXTURE_CHAIN,
        # PLAY-dOrderedCharter-26: present and empty, so the arm is unarmed; under the memory root (dOC-72)
        "memory/project/positional-refs.txt": "",
    }
    if plant in PURPOSE_PLANTS:
        old, new = PURPOSE_PLANTS[plant]
        files[f"{kit}/namespaces.toml"] = files[f"{kit}/namespaces.toml"].replace(old, new, 1)
    if plant.startswith("bundle-"):  # PLAY-dOrderedCharter-25 S8: `practice` selects, and the case's sources
        import tag_bundle
        old, new = tag_bundle.PRACTICE_ROLE
        files[f"{kit}/namespaces.toml"] = files[f"{kit}/namespaces.toml"].replace(old, new, 1)
        files.update(tag_bundle.PLANT_FILES[plant])
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
    if plant == "unclosed-fence":
        files["memory/guides/ALPHA.md"] = GUIDE + UNCLOSED
    if plant == "unclosed-record":
        files["memory/builds/x/README.md"] = UNCLOSED
    if plant in NATIVE_OWNERS:
        files[".memory-tree.conf"] += 'DISCIPLINES="arch"\nFAMILIES="arch:ARCH"\n'
        files[f"{kit}/namespaces.toml"] += (f'\n[[native]]\nclass = "family-id"\nowner = "{NATIVE_OWNERS[plant]}"\n'
                                            'pattern = "id_grammar:grammar_for"\n'
                                            'resolver = "corpus_ids:--print-defined-ids"\n')
    if plant == "tagless":  # a blob the extractor reads and takes no row from
        files["tools/corekit/none.tags"] = "# declares nothing\n"
    if plant == "queued-writers":  # TOOL-aQueuedIndex-1 S5: a blob holding `pause` parses for 3 s
        files[f"{kit}/fixture_tags.py"] = FIXTURE_EXTRACTOR.replace(
            "    rows = []\n", '    rows = []\n    if "pause" in text: __import__("time").sleep(3)  # noqa: E701\n', 1)
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
    ti.load_memory_tree()  # PLAY-dOrderedCharter-69 S2: the caller's git variables aside for the whole plant
    from deviation_join import set_env_aside
    from tree_lib import GIT_ENV_LEAKS
    top = pathlib.Path(tempfile.mkdtemp(prefix="gt"))
    try:
        with set_env_aside(GIT_ENV_LEAKS):
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
    """The index's tables reset in place through `load_index`'s one transaction, the file never unlinked
    (PLAY-dOrderedCharter-55 S16)."""
    ti.load_index(root, reset=True).close()


def run_plant(root, top, plant, sets) -> int:
    say = lambda *a: print("tags: plant " + plant + " · " + " ".join(map(str, a)))  # noqa: E731

    def run_verb(*args, **kw):  # every verb of a plant reads the fixture's own kit directory
        return run_kit_verb(*args, kit_rel=FIXTURE_KIT, **kw)
    if plant.startswith("positional-"):
        return run_positional_plant(root, top, plant, say, lambda: run_verb(root, "check", None, sets=sets))
    if plant.startswith("bundle-"):
        import contextlib
        import io
        import tag_bundle

        def run_captured(verb, address, more=None, as_json=False, **opts):  # -> (exit, printed lines), echoed
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                rc = run_verb(root, verb, address, sets={**sets, **(more or {})}, as_json=as_json, opts=opts)
            print(buf.getvalue(), end="")
            return rc, buf.getvalue().splitlines()
        return tag_bundle.run_bundle_plant(plant, run_captured, say, lambda files: write_files(root, files))

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
    # PLAY-dOrderedCharter-55's three: a helper's edit moves its importer's version, a schema rebuild under a
    # held reader, and a removed extractor's stored rows never served
    if plant == "helper-edit":
        helper, edited = f"{FIXTURE_KIT}/fixture_helper.py", "fixture_tags:extract_declared"
        write_commit(root, {f"{FIXTURE_KIT}/fixture_tags.py": HELPED_EXTRACTOR, helper: "EDITION = 1\n"},
                     "the extractor imports a helper")
        run_verb(root, "rebuild", None, sets=sets)
        write_commit(root, {helper: "EDITION = 2\n"}, "edit the helper alone")
        con = ti.load_index(root)
        try:
            state = ti.load_view(con, root, ti.derive_context(root, root / FIXTURE_KIT / "namespaces.toml"))
        finally:
            con.close()
        say(f"after the helper edit {edited} re-ran over {state['runs'][edited]} blobs,",
            f"{state['skipped'][edited]} skipped as fresh")
        return 0 if state["runs"][edited] and not state["skipped"][edited] else 1
    if plant == "held-open":
        import sqlite3
        run_verb(root, "rebuild", None, sets=sets)
        path = ti.derive_index_path(root)
        con = sqlite3.connect(str(path))
        con.execute("PRAGMA user_version = 0")  # a stale stamp, so the next open rebuilds
        con.commit()
        con.close()
        held = sqlite3.connect(str(path), timeout=ti.BUSY_TIMEOUT)
        held.execute("SELECT COUNT(*) FROM blob_row").fetchone()  # a reader holding the file across the rebuild
        try:
            run_verb(root, "rebuild", None, sets=sets)
            done = True
        except ti.TagError as exc:
            done = False
            say(f"the rebuild refused: {exc}")
        rows = held.execute("SELECT COUNT(*) FROM blob_row").fetchone()[0]
        stamp = held.execute("PRAGMA user_version").fetchone()[0]
        held.close()
        same = print_equal(read_dump(root), read_cold_dump())
        named = path.name == f"index-s{ti.INDEX_SCHEMA}.db" and path.is_file()
        say(f"the rebuild {'completed' if done else 'FAILED'} under a held reader, which reads {rows} blob rows",
            f"stamped {stamp}; the file is {path.name}")
        return 0 if done and rows and stamp == ti.INDEX_SCHEMA and named and same else 1
    # TOOL-aQueuedIndex-1 S5: two writers over one unbuilt tree, the second holding a view it served first
    if plant == "queued-writers":
        import ast
        import concurrent.futures
        import sqlite3
        import time
        # TOOL-aQueuedIndex-2 S2: every `with con:` block of the index module opens with the write lock
        blocks = [node for node in ast.walk(ast.parse(pathlib.Path(ti.__file__).read_text(encoding="utf-8")))
                  if isinstance(node, ast.With) and ast.unparse(node.items[0].context_expr) == "con"]
        bare = [node for node in blocks if ast.unparse(node.body[0]) != "con.execute('BEGIN IMMEDIATE')"]
        say(f"write blocks: {len(blocks) - len(bare)} of {len(blocks)} open with BEGIN IMMEDIATE")
        for node in bare:
            say(f"write block at line {node.lineno} does not open with BEGIN IMMEDIATE")
        run_verb(root, "rebuild", None, sets=sets)
        base = ti.read_git(root, "rev-parse", "HEAD^{tree}").strip()
        write_commit(root, {"tools/corekit/pause.tags": "pause\n"}, "a blob that parses for 3 s")
        ctx = ti.derive_context(root, root / FIXTURE_KIT / "namespaces.toml")
        path = ti.derive_index_path(root)
        con = ti.load_index(root)
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)  # writer one; writer two is this thread
        state = None
        try:
            ti.load_view(con, root, ctx, tree=base, overlay=False)  # as run_check serves its base tree
            one = pool.submit(run_verb, root, "rebuild", None, sets=sets)
            # writer one is inside its write block once the lock reads held for 0.5 s: its per-open
            # `PRAGMA user_version` write holds it for milliseconds only
            deadline, since = time.monotonic() + 30, None
            while True:
                probe = sqlite3.connect(str(path), timeout=0)
                try:
                    probe.execute("BEGIN IMMEDIATE")
                    probe.rollback()
                    since = None
                except sqlite3.OperationalError:
                    since = since or time.monotonic()
                finally:
                    probe.close()
                if since and time.monotonic() - since >= 0.5:
                    break
                if time.monotonic() > deadline:
                    say("writer one never took the write lock")
                    return 1
                time.sleep(0.05)
            try:
                state = ti.load_view(con, root, ctx)
            except ti.TagError as exc:
                say(f"writer two refused: {exc}")
                return 1
        finally:
            con.close()
            pool.shutdown(wait=True)
        # TOOL-aQueuedIndex-2 S1: a waiter that rebuilt under the lock counts its blobs as runs or skipped
        a, b = one.result(), state["parsed"]
        runs, skipped = sum(state["runs"].values()), sum(state["skipped"].values())
        say(f"writer one parsed {a} blob(s); writer two parsed {b}, ran {runs} and skipped {skipped}")
        say(f"busy timeout {ti.BUSY_TIMEOUT} s")
        # S3: the green line prints last, and only once every check holds
        # TOOL-aQueuedIndex-3 S1: a full tree build measured 95 s, so a timeout below 600 brings the flake back
        green = (print_equal(read_dump(root), read_cold_dump()) and blocks and not bare
                 and a > 0 and b == runs == skipped == 0 and ti.BUSY_TIMEOUT >= 600)
        if green:
            say("both writers green")
        return 0 if green else 1
    if plant == "extractor-removed":
        reg, gone = f"{FIXTURE_KIT}/namespaces.toml", "fixture_again:extract_again"
        base_reg = (root / reg).read_text(encoding="utf-8")
        write_commit(root, {reg: base_reg + derive_fixture_row("kind", gone),
                            f"{FIXTURE_KIT}/fixture_again.py": FIXTURE_EXTRACTOR.replace("extract_declared",
                                                                                         "extract_again")},
                     "register a second extractor")
        run_verb(root, "rebuild", None, sets=sets)
        write_commit(root, {reg: base_reg, f"{FIXTURE_KIT}/fixture_again.py": None}, "remove it")
        run_verb(root, "rebuild", None, sets=sets)
        con = ti.load_index(root)
        try:
            stored = con.execute("SELECT COUNT(*) FROM blob_row WHERE extractor=?", (gone,)).fetchone()[0]
        finally:
            con.close()
        dump = read_dump(root)
        served = sum(1 for r in dump if f"\t{gone}\t" in r)
        say(f"the removed extractor's stored rows: {stored}, served: {served};")
        return 0 if stored and not served and print_equal(dump, read_cold_dump()) else 1
    # PLAY-dOrderedCharter-69 S5: two child fixtures under an exported GIT_DIR act on their own scratch only
    if plant == "git-env":
        from deviation_join import set_env_aside
        linked = top / "linked"
        run_git(root, "worktree", "add", "-q", str(linked), "-b", "linked")
        index, sentinel = ti.derive_index_path(root), b"sentinel, not a database"
        index.parent.mkdir(parents=True, exist_ok=True)
        index.write_bytes(sentinel)
        git_dir = run_git(linked, "rev-parse", "--absolute-git-dir").strip()
        kids = ((KIT_DIR / "gov_tag.py", "two-versions"), (KIT_DIR / "edge_grammar.py", "resolve-tag"))
        with set_env_aside(GIT_DIR=git_dir):
            done = [subprocess.run([sys.executable, str(script), "--fixture", "--plant", kid], cwd=linked,
                                   capture_output=True, stdin=subprocess.DEVNULL) for script, kid in kids]
        bare, same = run_git(root, "config", "core.bare").strip(), index.read_bytes() == sentinel
        if all(d.returncode == 0 for d in done) and bare == "false" and same:
            say("both children green, core.bare false, the outer index unchanged")
            return 0
        for (script, kid), d in zip(kids, done):
            say(f"{script.name} --plant {kid} exited {d.returncode}:",
                (d.stdout + d.stderr).decode("utf-8", "replace").strip())
        say(f"core.bare {bare}, the outer index", "unchanged" if same else "CHANGED")
        return 1
    # PLAY-dOrderedCharter-51's two: each extractor version's rows kept apart, each worktree served its own
    if plant == "two-versions":
        other, third, edited = top / "wt2", top / "wt3", "fixture_tags:extract_declared"
        run_git(root, "worktree", "add", "-q", str(other), "-b", "two")
        write_commit(other, {f"{FIXTURE_KIT}/fixture_tags.py": EDITED_EXTRACTOR}, "edit the extractor in two")
        run_git(root, "worktree", "add", "-q", str(third), "-b", "three")  # PLAY-dOrderedCharter-55 S13
        write_commit(third, {f"{FIXTURE_KIT}/fixture_tags.py": THIRD_EXTRACTOR}, "edit the extractor in three")
        both = (root, other, third)
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
        say(f"round 2 parsed {' and '.join(map(str, second))} blobs; {held} versions of {edited} held side by side")
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
        return 0 if all(same) and second == [0, 0, 0] and held == 3 and rc == 0 and not left and kept else 1
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
    # PLAY-dOrderedCharter-70's four: a TOML row placed on its own line, a staged rename, and a conf edit
    if plant == "toml-row":
        rows = [r[:4] for r in ti.derive_tag_rows(TOML_ROWS, "practice")]
        want = [("practice.a", "tag", 4, 5), ("practice.b", "tag", 8, 9)]
        say(f"rows {rows}", "on their own lines" if rows == want else f"NOT on their own lines, wanted {want}")
        return 0 if rows == want else 1

    def read_paths(where, address):  # the paths `address` resolves to in `where`'s view, overlay included
        con = ti.load_index(where)
        try:
            ti.load_view(con, where, ti.derive_context(where, where / FIXTURE_KIT / "namespaces.toml"))
            return sorted({r["path"] for r in ti.resolve_address(con, address)})
        finally:
            con.close()
    def read_served(where, address):  # the text `address` serves in `where`'s view, overlay included
        con = ti.load_index(where)
        try:
            ti.load_view(con, where, ti.derive_context(where, where / FIXTURE_KIT / "namespaces.toml"))
            return "\n".join(r["text"] for r in ti.resolve_address(con, address))
        finally:
            con.close()
    # PLAY-dOrderedCharter-49 AC41: a dirty row leaves with its edit, and a worktree re-created at a gone
    # one's path inherits none of its rows
    if plant == "dirty-revert":
        write_files(root, {"memory/guides/ALPHA.md": GUIDE.replace("the intro text", "edited, then reverted")})
        dirty = read_served(root, "doc.alpha#intro")
        run_git(root, "checkout", "--", "memory/guides/ALPHA.md")
        clean = read_served(root, "doc.alpha#intro")
        ok = "edited, then reverted" in dirty and "the intro text" in clean and "edited" not in clean
        say("the edit served while dirty" if "edited" in dirty else "the edit NOT served while dirty",
            "· the committed text served once reverted" if ok else "· the reverted edit STILL SERVED")
        return 0 if ok else 1
    if plant == "worktree-recreate":
        other = top / "wt2"
        run_git(root, "worktree", "add", "-q", str(other), "-b", "two")
        write_files(other, {"memory/guides/ALPHA.md": GUIDE.replace("the intro text", "the gone tree's edit")})
        before = read_served(other, "doc.alpha#intro")
        run_git(root, "worktree", "remove", "--force", str(other))
        run_git(root, "worktree", "add", "-q", str(other), "two")
        after = read_served(other, "doc.alpha#intro")
        ok = "the gone tree's edit" in before and "the intro text" in after and "gone tree" not in after
        say("the re-created worktree serves the committed text" if ok else "the re-created worktree INHERITS a row")
        return 0 if ok else 1
    # PLAY-dOrderedCharter-55 S21: a worktree read under a second spelling of its path keeps its dirty rows
    # through another worktree's sweep, and a pruned worktree's rows leave
    if plant == "worktree-spelling":
        other, gone = top / "wt2", top / "wt3"
        for where, branch in ((other, "two"), (gone, "three")):
            run_git(root, "worktree", "add", "-q", str(where), "-b", branch)
            write_files(where, {"memory/guides/ALPHA.md": GUIDE.replace("the intro text", f"edited in {where.name}")})
        real = ti.read_git(other, "rev-parse", "--show-toplevel").strip()
        # the second spelling: a git that prints the caller's own, the drive letter's case swapped and the
        # slashes turned back, which this host's git never prints (deviation 557)
        spelled = (real[0].swapcase() + real[1:]).replace("/", "\\") if real[1:2] == ":" else real
        read_git = ti.read_git

        def read_git_spelled(where, *args):
            out = read_git(where, *args)
            return spelled + "\n" if args == ("rev-parse", "--show-toplevel") and out.strip() == real else out
        ti.read_git = read_git_spelled
        try:
            mine = read_served(other, "doc.alpha#intro")
        finally:
            ti.read_git = read_git
        read_served(gone, "doc.alpha#intro")
        run_git(root, "worktree", "remove", "--force", str(gone))
        run_git(root, "worktree", "prune")
        write_commit(root, {"AGENTS.md": "# Charter\n\n## Practices\n\nchanged\n"}, "a commit the sweep follows")
        run_verb(root, "rebuild", None, sets=sets)
        con = ti.load_index(root)
        try:
            held = dict(con.execute("SELECT worktree, COUNT(*) FROM dirty_path GROUP BY worktree").fetchall())
        finally:
            con.close()
        kept = held.get(ti.derive_worktree_key(spelled), 0)
        left = sum(n for wt, n in held.items() if wt.endswith("/wt3"))
        say(f"{real} read as {spelled}: served its own edit" if "edited in wt2" in mine else "NOT served its edit",
            f"· {kept} dirty rows kept under its key after the sweep, {left} of the pruned worktree's left")
        return 0 if "edited in wt2" in mine and kept and not left else 1
    if plant == "dirty-rename":
        run_verb(root, "rebuild", None, sets=sets)
        run_git(root, "mv", "memory/guides/ALPHA.md", "memory/guides/BETA.md")
        alpha, beta = read_paths(root, "doc.alpha"), read_paths(root, "doc.beta")
        say(f"after a staged rename doc.alpha resolves to {alpha} and doc.beta to {beta}")
        return 0 if not alpha and beta == ["memory/guides/BETA.md"] else 1
    if plant in ("charter-warm", "charter-dirty"):
        run_verb(root, "rebuild", None, sets=sets)
        conf = {".memory-tree.conf": 'MEMORY_ROOT=memory\nCHARTER="CHARTER2.md"\n',
                "CHARTER2.md": "# Charter two\n\n## Practices\n\nthe second charter\n"}
        if plant == "charter-warm":
            write_commit(root, conf, "the charter moves")
            run_verb(root, "rebuild", None, sets=sets)
            same = print_equal(read_dump(root), read_cold_dump())
        else:
            write_commit(root, {"CHARTER2.md": conf["CHARTER2.md"]}, "a second charter, not yet named")
            run_verb(root, "rebuild", None, sets=sets)
            write_files(root, {".memory-tree.conf": conf[".memory-tree.conf"]})
            run_verb(root, "rebuild", None, sets=sets)
            same = print_equal(read_dump(root), read_cold_dump())
        paths = read_paths(root, "doc.charter")
        say(f"doc.charter resolves to {paths}")
        return 0 if same and paths == ["CHARTER2.md"] else 1
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
                ctx = ti.derive_context(where, where / FIXTURE_KIT / "namespaces.toml")
                ti.load_view(con, where, ctx)
                text = "\n".join(r["text"] for r in ti.resolve_address(con, "doc.alpha#intro"))
            finally:
                con.close()
            seen = mine in text and theirs not in text
            ok &= seen
            say(pathlib.Path(where).name, "serves its own edit" if seen else "SERVES ANOTHER'S", "· index",
                ti.derive_index_path(where).as_posix())
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
    if plant.startswith("retired-section"):  # PLAY-dOrderedCharter-29 S8: `## Intro` gone between base and tip
        base = run_git(root, "rev-parse", "HEAD").strip()
        reminted = plant.endswith("reminted")
        guide = GUIDE.replace("## Intro\n", "") + ("\n## Intro.\n\nthe slug minted again\n" if reminted else "")
        files = {"memory/guides/ALPHA.md": guide}
        if plant != "retired-section":
            files[f"{FIXTURE_KIT}/aliases.toml"] = (
                ALIASES + '\n[[alias]]\nref = "doc.alpha#intro"\ntarget = "doc.alpha#m5-recall-and-reuse"\n')
        write_commit(root, files, "a section retired")
        return run_verb(root, "check", None, sets=sets, base=base)
    if plant in ("retired-old", "retired-reminted"):
        return run_verb(root, "check", None, sets=sets, base=run_git(root, "rev-parse", "HEAD").strip())
    if plant in ("dead-selector", "file-name"):  # the plant's exit, then its second half's on one line
        rc = run_verb(root, "check", None, sets=sets)
        if plant == "dead-selector":
            write_commit(root, {f"{FIXTURE_KIT}/readers.toml": '[[reader]]\ntag = "reader.one"\n'}, "no ghost")
            half = "without reader.ghost"
        else:
            run_git(root, "mv", "tools/corekit/kit.toml", "tools/corekit/corekit.kit.toml")
            run_git(root, "mv", "tools/expkit/kit.toml", "tools/expkit/expkit.kit.toml")
            write_commit(root, {}, "no tracked kit.toml")
            half = "no tracked kit.toml"
        say(f"{half}: rc={run_verb(root, 'check', None, sets=sets)}")
        return rc
    if plant == "reference-row":  # PLAY-dOrderedCharter-40: the registry tag resolves to its row, the arm green
        rc = run_verb(root, "show", "doc.reference.fixture", sets=sets)
        checked = run_verb(root, "check", None, sets=sets)
        say(f"show: rc={rc}, check: rc={checked}")
        return 1 if rc or checked else 0
    if plant in ("pending-source", "new-no-purpose"):  # PLAY-dOrderedCharter-22: the source lands, the row gains a purpose
        rc = run_verb(root, "check", None, sets=sets)
        if plant == "pending-source":
            write_commit(root, {f"{FIXTURE_KIT}/readers.toml": '[[reader]]\ntag = "reader.every"\n'},
                         "the source lands")
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


def write_forked_record(root, kit, records: dict) -> None:
    """PLAY-dOrderedCharter-47 S4's history: `records`, path to text, committed on a branch forked before the
    check's module lands on main, then that branch merged."""
    run_git(root, "checkout", "-q", "-b", "side")
    write_commit(root, records, "a record on a branch forked before the check")
    run_git(root, "checkout", "-q", "main")
    write_commit(root, {f"{kit}/positional.py": "# the check\n"}, "the check lands")
    run_git(root, "merge", "-q", "--no-ff", "side", "-m", "the side branch merged")


def run_positional_plant(root, top, plant, say, check) -> int:
    """S8's seven plants, PLAY-dOrderedCharter-47's forked-before plant, PLAY-dOrderedCharter-53's three
    per-line plants and PLAY-dOrderedCharter-48's two producer plants over the fixture's own lists. `check` runs the fixture's whole `check`, whose
    `positional` arm each plant moves; a plant of several steps returns 0 only when every step held. Every
    `positional` call reads the fixture's memory root, `memory` (PLAY-dOrderedCharter-72)."""
    import positional as pos
    kit, guide, mem = FIXTURE_KIT, "memory/guides/ALPHA.md", "memory"
    list_path = pos.derive_list_path(root, mem)

    def read_rows():
        return pos.read_list(list_path) or []
    if plant in ("positional-no-tree", "positional-absent"):  # PLAY-dOrderedCharter-78 S5
        gone = list_path.parent.glob("*") if plant == "positional-no-tree" else [list_path]
        write_commit(root, {p.relative_to(root).as_posix(): None for p in gone}, "the list removed")
        if plant == "positional-no-tree":
            list_path.parent.rmdir()
        return check()
    if plant == "positional-seed":
        write_commit(root, {POS_CODE: POS_MOD, "AGENTS.md": "# Charter\n\nsee HYGIENE check 5\n",
                            guide: GUIDE + f"\nsee {derive_cite(1)}, {derive_cite('2-3')} and {derive_cite(1)} again\n",
                            "memory/guides/BETA.md": f"# Beta\n\nread BUILD-METHOD M5, and {derive_cite(1)}\n",
                            "memory/project/positional-refs.txt": "AGENTS.md\tHYGIENE check 5\n"}, "citations")
        pos.run_seed(root, mem)
        want = {"AGENTS.md\tHYGIENE check 5", f"{guide}\t{derive_cite(1)}", f"{guide}\t{derive_cite('2-3')}",
                f"memory/guides/BETA.md\t{derive_cite(1)}", "memory/guides/BETA.md\tBUILD-METHOD M5"}
        got = read_rows()
        same = sorted(got) == sorted(want)
        say("seed: the list holds every expected row and no other" if same else f"seed: the list DIFFERS: {got}")
        again = pos.run_seed(root, mem)
        say(f"a second seed: rc={again}")
        rc = check()
        return 0 if same and again == 1 and rc == 0 else 1
    if plant in ("positional-new", "positional-stale", "positional-listed"):
        two = f" and {derive_cite(2)}"
        cited = GUIDE + f"\nsee {derive_cite(1)}" + (two if plant == "positional-stale" else "") + ", per BUILD-METHOD M5\n"
        write_commit(root, {POS_CODE: POS_MOD, guide: cited}, "citations")
        pos.run_seed(root, mem)
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
        pos.run_shrink(root, mem)
        after, rc2 = len(read_rows()), check()
        say(f"after shrink: {after - 1} rows, rc={rc2}")  # the M5 row aside
        write_files(root, {guide: cited.replace(two, f" and {derive_cite(3)}")})
        pos.run_shrink(root, mem)
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
    record, cite = "memory/builds/x/build/record.md", "see x.py:{}\n"
    if plant == "positional-spec-revbump":  # PLAY-dOrderedCharter-55 S24: a spec added before the check, bumped after
        spec = "memory/builds/x/spec/spec.md"
        write_forked_record(root, kit, {spec: cite.format(1)})
        write_commit(root, {spec: cite.format(1) + cite.format(3)}, "the spec's rev bump cites a line")
        return check()
    if plant == "positional-bulk-move":  # PLAY-dOrderedCharter-55 S25: three records moved, a line edited in each
        filler = "".join(f"a line of record {{n}} that the move keeps, the {w}\n" for w in
                         ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"))
        old = {n: filler.format(n=n) + cite.format(1) + cite.format(2) for n in (1, 2, 3)}
        write_forked_record(root, kit, {f"memory/builds/x/build/r{n}.md": t for n, t in old.items()})
        moved = {f"memory/builds/x/build/r{n}.md": None for n in old}
        moved.update({f"memory/builds/x/reviews/r{n}.md": t.replace(cite.format(2), cite.format(4 + n))
                      for n, t in old.items()})
        write_commit(root, moved, "three records moved, a line edited in each")
        return check()
    if plant in ("positional-edited-after", "positional-renamed-after", "positional-uncommitted"):
        # PLAY-dOrderedCharter-53 S4: the pre-fork record edited, renamed, or edited and left uncommitted after the merge
        write_forked_record(root, kit, {record: cite.format(1)})
        if plant == "positional-renamed-after":
            run_git(root, "mv", record, "memory/builds/x/build/moved.md")
            write_commit(root, {}, "the record renamed after the merge")
            return check()
        appended = {record: cite.format(1) + cite.format(3)}
        if plant == "positional-uncommitted":
            write_files(root, appended)
        else:
            write_commit(root, appended, "a citation appended after the merge")
        return check()
    if plant == "positional-forked-before":  # PLAY-dOrderedCharter-47 S4: a branch forked before the check lands
        after = "memory/builds/x/build/after.md"
        write_forked_record(root, kit, {record: cite.format(1)})
        rc1 = check()
        write_commit(root, {after: cite.format(2)}, "a record after the merge")
        rc2 = check()
        write_commit(root, {after: None}, "the post-merge record removed")
        run_git(root, "checkout", "-q", "side")  # moved on its own branch, so its add is not the check's either
        write_commit(root, {record: None, instruction_units.derive_tool_rel("notes.md"): cite.format(1)},
                     "the record moved outside the records")
        run_git(root, "checkout", "-q", "main")
        run_git(root, "merge", "-q", "--no-ff", "side", "-m", "the move merged")
        rc3 = check()
        say(f"the pre-fork record: rc={rc1}; a record after the merge: rc={rc2}; "
            f"the pre-fork record moved under tools: rc={rc3}")
        return 0 if (rc1, rc2, rc3) == (0, 1, 1) else 1
    if plant in ("positional-producer-new", "positional-producer-stale"):  # PLAY-dOrderedCharter-48 S5
        role = instruction_units.derive_tool_rel("roles", "agents", "gov-x.agent.md")
        write_commit(root, {role: "# gov-x\n\n- cite it by file:line\n"}, "a role source")
        if plant == "positional-producer-new":
            rc = check()
            write_files(root, {role: "# gov-x\n\n- cite it by `path#symbol`, never by file:line\n"})
            say(f"re-pointed to a stable form: rc={check()}")
            return rc
        seeded = pos.run_producers(root, kit, mem, seed=True)
        rc1, again = check(), pos.run_producers(root, kit, mem, seed=True)
        write_files(root, {role: "# gov-x\n\n- cite it by `path#symbol`\n"})
        rc2 = check()
        say(f"kept: rc={rc1}; a second seed: rc={again}; the kept line re-pointed: rc={rc2}")
        return 0 if (seeded, rc1, again, rc2) == (0, 0, 1, 1) else 1
    # positional-pin: the unlisted citation re-pinned, and a file outside the repository refused
    write_commit(root, {POS_CODE: POS_MOD, guide: GUIDE + f"\nsee {derive_cite(2)}\n"}, "a citation")
    blob = run_git(root, "rev-parse", "--short=8", f"HEAD:{POS_CODE}").strip()
    pinned = pos.run_pin(root, mem, root / guide)
    text = (root / guide).read_text(encoding="utf-8")
    rc = check()
    ok = pinned == 0 and derive_cite(2, blob) in text and derive_cite(2) + "\n" not in text and rc == 0
    say(f"pin {'rewrote the citation to the blob at HEAD' if ok else 'did NOT rewrite the citation'}; check: rc={rc}")
    outside = top / "outside.md"
    outside.write_text(f"see {derive_cite(2)}\n", encoding="utf-8")
    out_rc = pos.run_pin(root, mem, outside)
    kept = outside.read_text(encoding="utf-8") == f"see {derive_cite(2)}\n"
    say(f"pin outside the repository: rc={out_rc}, {'nothing written' if kept else 'the file WRITTEN'}")
    return 0 if ok and out_rc == 1 and kept else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="gov_tag.py", description="the tag resolver (gov tag)")
    ap.add_argument("verb", nargs="?", choices=("show", "where", "refs", "check", "bundle"))
    ap.add_argument("address", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--base")
    ap.add_argument("--inline", action="store_true", help="bundle: inline each row's content under --bytes")
    ap.add_argument("--bytes", type=int, dest="nbytes", metavar="N", help="bundle: the byte budget --inline fills")
    ap.add_argument("--under", metavar="DIR", help="bundle: list one folded group's rows unfolded")
    ap.add_argument("--only", choices=("type-registered", "target-resolves"), help="check: run one edge arm alone")
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
        if (a.inline or a.nbytes is not None or a.under) and a.verb != "bundle" or a.only and a.verb != "check":
            ap.error("--inline, --bytes and --under are bundle's flags, --only is check's")
        opts = {"inline": a.inline, "nbytes": a.nbytes, "under": a.under, "only": a.only}
        return run_kit_verb(root, a.verb, a.address, sets={}, as_json=a.json, base=a.base, opts=opts)
    except PolicyRefused as exc:
        print(f"tags: refused · {exc.key} · {exc.line}", file=sys.stderr)
        return 2
    except ti.TagError as exc:
        print(f"tags: refused · {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
