#!/usr/bin/env python3
"""render_agents.py — the role catalogue rendered into Claude Code agent types (TOOL-aOrientedCast-3).

    python render_agents.py --write | --check | --selftest

`--write` renders one agent type per role whose `agent` is true, at `.claude/agents/<name>.md` under
the repository root: the role's Claude keys, then `omitClaudeMd: true`, then gov's `workflow` and
`writes`, then a body that is `roles_lib.render_role`'s output followed, under `## Charter`, by one
`### charter §<n>` block per id the role's `charter` key names. Beside them it writes the generated
index `.claude/roles.json`: every role with its `workflow`, `writes` and `agent`, and `harnesses`, the
repo-relative scripts of every workflow whose `driver` is `workflow`. Everything is rendered in memory
first, so a role, overlay or charter section that fails to resolve writes nothing.

OWNERSHIP. The renderer owns the agent types its catalogue names plus every name the on-disk index
lists, which is exactly the set a previous render wrote. `--write` unlinks an owned file the
catalogue no longer renders; it never touches any other file under `.claude/agents/`, where an
adopter keeps definitions of its own.

RESTART. A Claude Code session reads its agent registry at session start, so a type written, changed
or unlinked here is not spawnable as changed in a session started before the write. `--write` says so
in one line whenever an agent type moved.

`--check` writes nothing: it renders the same set and names every `missing`, `drift` or `stale`
owned path, comparing with carriage returns stripped from the on-disk side, because a worktree can
check a pinned path out CRLF while git reports it clean. `--selftest` runs this script's arms over a
catalogue it builds in a temporary directory, never the repository's files.

The kit directory is `git rev-parse --show-prefix` run in this script's own directory, the tool root
is its parent, and the target root is `git rev-parse --show-toplevel`; an empty derivation refuses.
Every file is read through the kit's own `roles_lib.py`; nothing here parses a role, an overlay, the
workflow table, the conf or the governing doc itself.

Exit 0 when written, fresh or passing; 1 on drift or a failed arm, every offending path named; 2 on
usage, a `RolesError` from the library, or a catalogue holding zero roles, since a render of nothing
compares clean against an empty directory.

WHAT THIS DOES NOT CHECK: whether a role's text is any good, or whether its front matter obeys the
catalogue's grammar, which `check_roles.py` grades; whether the Claude Code that spawns a type honours
`omitClaudeMd`, which rests on the CLI version and a server flag and is observed only by a live probe;
and whether a running session has restarted since the last write.
"""
import argparse
import contextlib
import io
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

KIT_DIR = pathlib.Path(__file__).absolute().parent
sys.path.insert(0, str(KIT_DIR))
import roles_lib as lib  # noqa: E402  (the kit's own library, beside this file)

#: Claude Code's own front-matter keys, in the order a rendered type carries them.
CLAUDE_KEYS = tuple("name description tools model maxTurns".split())
AGENTS_REL = ".claude/agents"
INDEX_REL = ".claude/roles.json"
NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
RESTART_LINE = ("render_agents: %d agent type(s) changed — a Claude Code session started before this "
                "write cannot spawn the change; start a new session in this repository before spawning one.")
NOTE_LINE = ("render_agents: note — %s is named by the workflow table and absent here; "
             "its kit is not installed")
#: The self-test fixture's two workflow-driver harnesses, spelled as its own table writes them. The
#: arms format each with the fixture's tool root instead of typing a second literal of the path.
FIXTURE_HARNESS = "{prefix}/workflows/a.js"
FIXTURE_MISSING = "{prefix}/workflows/missing.js"
FIXTURE_ROOT = "toolroot"


def derive_tool_root(script_dir):
    """`(kit_dir, tool_root, target_root)` through git; a RolesError when either derivation is empty.

    Two spawns: the toplevel and prefix of the script's own directory, which place the kit, and the
    toplevel of the working directory, which is the tree rendered into.
    """
    answers = []
    for args, cwd in ((["--show-toplevel", "--show-prefix"], script_dir), (["--show-toplevel"], os.getcwd())):
        g = subprocess.run(["git", "rev-parse"] + args, cwd=str(cwd), capture_output=True, encoding="utf-8")
        answers += (g.stdout.split("\n") + ["", ""])[:len(args)] if g.returncode == 0 else [""] * len(args)
    kit_top, prefix, top = (x.strip() for x in answers)
    prefix = prefix.strip("/")
    if not kit_top or not prefix or not top:
        raise lib.RolesError("the kit directory or the repository root derived empty through git, so "
                             "there is no tree to render into: run from inside the repository")
    kit_dir = pathlib.Path(kit_top) / prefix
    return kit_dir, kit_dir.parent, pathlib.Path(top)


def load_catalogue(kit_dir, target_root):
    """The roles, the workflow table, MEMORY_ROOT and the governing doc's sections, through the library."""
    roles = lib.load_roles(kit_dir)
    if not roles:
        raise lib.RolesError("%s holds zero roles, and a render of nothing compares clean against an "
                             "empty directory" % (pathlib.Path(kit_dir) / "agents").as_posix())
    conf = pathlib.Path(target_root) / ".memory-tree.conf"
    memory_root = lib.read_conf_key(conf, "MEMORY_ROOT") if conf.is_file() else None
    if not memory_root:
        raise lib.RolesError("%s declares no MEMORY_ROOT, or is absent" % conf.as_posix())
    charter_path = lib.resolve_charter_path(target_root)
    return {"roles": roles, "workflows": lib.load_workflows(kit_dir), "memory_root": memory_root,
            "charter_path": charter_path,
            "sections": lib.extract_charter_sections(lib.load_text(charter_path))}


def render_agent_file(kit_dir, slot, role, memory_root, sections, charter_path):
    """One agent type's text: Claude keys, the trim, gov's two keys, the rendered role, its charter blocks."""
    keys = role["keys"]
    head = ["---"] + ["%s: %s" % (k, keys[k]) for k in CLAUDE_KEYS if k in keys]
    head += ["omitClaudeMd: true", "workflow: %s" % keys.get("workflow", ""),
             "writes: %s" % keys.get("writes", ""), "---"]
    text = "\n".join(head) + "\n" + lib.render_role(kit_dir, slot, memory_root)
    ids = [x.strip() for x in keys.get("charter", "").split(",") if x.strip()]
    if ids:
        text += "\n## Charter\n"
    for cid in ids:
        if cid not in sections:
            raise lib.RolesError("%s: charter %s names no section of %s" % (
                role["path"].as_posix(), cid, pathlib.Path(charter_path).as_posix()))
        text += "\n### charter %s\n\n%s\n" % (cid, sections[cid])
    return text


def derive_harness_paths(workflows, tool_root, target_root):
    """`(harnesses, absent)`: each `workflow`-driver harness resolved, repo-relative, sorted and unique."""
    found, absent = set(), set()
    for w in workflows:
        if w.get("driver") != "workflow":
            continue
        path, held = lib.resolve_harness_path(tool_root, w.get("harness"))
        rel = pathlib.Path(os.path.relpath(str(path), str(target_root))).as_posix()
        found.add(rel)
        if not held:
            absent.add(rel)
    return sorted(found), sorted(absent)


def render_roles_index(roles, harnesses):
    """The index bytes: every role's `workflow`, `writes` and `agent`, and the harness list."""
    obj = {"harnesses": harnesses,
           "roles": {slot: {"agent": r["keys"].get("agent", "true") == "true",
                            "workflow": r["keys"].get("workflow", ""),
                            "writes": r["keys"].get("writes", "")} for slot, r in roles.items()}}
    return json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=True) + "\n"


def load_owned_names(target_root):
    """The role names the on-disk index lists; an absent or unreadable index lists none."""
    try:
        with open(pathlib.Path(target_root) / INDEX_REL, encoding="utf-8") as fh:
            names = json.load(fh).get("roles") or {}
    except (OSError, ValueError, AttributeError):
        return []
    return [n for n in names if isinstance(n, str) and NAME_RE.match(n)] if isinstance(names, dict) else []


def check_rendered(target_root, rendered):
    """`[(kind, rel)]` for every owned path that is missing, drifted or stale; reads, never writes."""
    offenders = []
    for rel, text in rendered.items():
        p = pathlib.Path(target_root) / rel
        if not p.is_file():
            offenders.append(("missing", rel))
        elif p.read_bytes().replace(b"\r", b"") != text.encode("utf-8"):
            offenders.append(("drift", rel))
    for name in load_owned_names(target_root):
        rel = "%s/%s.md" % (AGENTS_REL, name)
        if rel not in rendered and (pathlib.Path(target_root) / rel).is_file():
            offenders.append(("stale", rel))
    return offenders


def write_rendered(target_root, rendered, stale):
    """`(written, unlinked)`: stale owned types unlinked, types whose bytes differ written, the index last."""
    written, unlinked = [], []
    for gone in stale:
        (pathlib.Path(target_root) / gone).unlink()
        unlinked.append(gone)
    for rel in sorted(r for r in rendered if r != INDEX_REL) + [INDEX_REL]:
        p = pathlib.Path(target_root) / rel
        if p.is_file() and p.read_bytes().replace(b"\r", b"") == rendered[rel].encode("utf-8"):
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(rendered[rel])
        written.append(rel)
    return written, unlinked


def print_drift(offenders, remedy):
    """One line per offender, then the remedy."""
    for kind, rel in offenders:
        print("render_agents: %s %s" % (kind, rel))
    print("render_agents: remedy — %s" % remedy)


def run_mode(mode, kit_dir, tool_root, target_root):
    """Render the catalogue at kit_dir into target_root and `--write` or `--check` it; the exit code."""
    try:
        cat = load_catalogue(kit_dir, target_root)
        rendered = {}
        for slot, role in cat["roles"].items():
            if role["keys"].get("agent", "true") == "true":
                rendered["%s/%s.md" % (AGENTS_REL, slot)] = render_agent_file(
                    kit_dir, slot, role, cat["memory_root"], cat["sections"], cat["charter_path"])
        harnesses, absent = derive_harness_paths(cat["workflows"], tool_root, target_root)
        rendered[INDEX_REL] = render_roles_index(cat["roles"], harnesses)
    except lib.RolesError as e:
        print("\n".join("render_agents: " + ln for ln in str(e).split("\n")), file=sys.stderr)
        return 2
    for rel in absent:
        print(NOTE_LINE % rel)
    types = len(rendered) - 1
    kit_rel = pathlib.Path(os.path.relpath(str(kit_dir), str(target_root))).as_posix()
    remedy = "python %s/render_agents.py --write" % kit_rel
    offenders = check_rendered(target_root, rendered)
    if mode == "check":
        print("render_agents: %d agent type(s) and 1 index graded" % types)
        if offenders:
            print_drift(offenders, remedy)
            return 1
        return 0
    stale = [rel for kind, rel in offenders if kind == "stale"]
    written, unlinked = write_rendered(target_root, rendered, stale)
    for rel in written:
        print("render_agents: wrote %s" % rel)
    for rel in unlinked:
        print("render_agents: unlinked %s" % rel)
    if not written and not unlinked:
        print("render_agents: unchanged — %d agent type(s) and 1 index fresh" % types)
        return 0
    print("render_agents: %d written, %d unlinked" % (len(written), len(unlinked)))
    moved = len([r for r in written if r != INDEX_REL]) + len(unlinked)
    if moved:
        print(RESTART_LINE % moved)
    return 0


def build_fixture(root, roles):
    """A catalogue in <root>: kit, overlays, workflow table, conf, governing doc, stub harnesses."""
    root = pathlib.Path(root)
    kit = root / FIXTURE_ROOT / KIT_DIR.name
    stubs = (root / FIXTURE_HARNESS.format(prefix=FIXTURE_ROOT)).parent
    for d in (kit / "agents", kit / "house", stubs):
        d.mkdir(parents=True, exist_ok=True)
    for slot, (extra, overlay) in roles.items():
        (kit / "agents" / (slot + ".agent.md")).write_text(
            "---\nname: %s\ndescription: d %s\ntools: Read, Write\nmodel: inherit\n%s---\n\n"
            "Body of %s, under {{MEMORY_ROOT}}.\n" % (slot, slot, extra, slot), encoding="utf-8")
        (kit / "house" / (slot + ".md")).write_text(overlay, encoding="utf-8")
    for stub in ("a.js", "b.js"):
        (stubs / stub).write_text("// stub\n", encoding="utf-8")
    (kit / "workflows.toml").write_text(
        '[[workflow]]\nname = "w1"\ndriver = "workflow"\nharness = "%s"\n\n'
        '[[workflow]]\nname = "w2"\ndriver = "workflow"\nharness = "%s"\n\n'
        '[[workflow]]\nname = "w3"\ndriver = "program"\nharness = "python {prefix}/roles/x.py"\n\n'
        '[[workflow]]\nname = "w4"\ndriver = "agent"\nharness = "none"\n'
        % (FIXTURE_HARNESS, FIXTURE_HARNESS), encoding="utf-8")
    (root / ".memory-tree.conf").write_text("MEMORY_ROOT=mem\nCHARTER=DOC.md\n", encoding="utf-8")
    (root / "DOC.md").write_text("# Doc\n\n## §1 — One\n\nbody one\n\n## §2 — Two\n\nbody two\n",
                                 encoding="utf-8")
    return kit, root / FIXTURE_ROOT


def check_arm(state, arm, ok, what):
    """Count one assertion, and record arm <arm> as failed with <what> when <ok> is false."""
    state["n"] += 1
    if not ok:
        state["fail"].append("arm %d — %s" % (arm, what))


def run_selftest():
    """The ten arms over a fixture catalogue; prints PASS or FAIL with the assertion count."""
    state = {"n": 0, "fail": []}
    roles = {"r-one": ("maxTurns: 7\nworkflow: w1\nreads: input:spec\nwrites: product\n"
                       "charter: §2, §1\n", "Overlay line.\n"),
             "r-two": ("workflow: w1\nreads: input:spec\nwrites: spec\ncharter: \n", ""),
             "r-off": ("workflow: w4\nreads: input:spec\nwrites: none\ncharter: §1\nagent: false\n", "")}
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        kit, tool_root = build_fixture(root, roles)
        agents = root / ".claude" / "agents"
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            rc = run_mode("write", kit, tool_root, root)
        texts = {p.stem: p.read_text(encoding="utf-8") for p in agents.glob("*.md")}
        index = json.loads((root / ".claude" / "roles.json").read_text(encoding="utf-8"))
        for slot in ("r-one", "r-two"):
            head = texts.get(slot, "").split("---\n")[1].split("\n") if slot in texts else []
            check_arm(state, 1, rc == 0 and "omitClaudeMd: true" in head,
                      "%s carries no omitClaudeMd: true line" % slot)
            want = roles[slot][0]
            for key in ("workflow", "writes"):
                line = next(ln for ln in want.split("\n") if ln.startswith(key + ":"))
                check_arm(state, 1, line in head, "%s's %s line is not its role's" % (slot, key))
        check_arm(state, 2, "r-off" not in texts, "an agent: false role rendered a type")
        check_arm(state, 2, index["roles"].get("r-off", {}).get("agent") is False,
                  "the index does not carry r-off with agent false")
        check_arm(state, 3, "\n## House rules\n\nOverlay line.\n" in texts.get("r-one", ""),
                  "a one-line overlay did not reach the type")
        check_arm(state, 3, "## House rules" not in texts.get("r-two", "x## House rules"),
                  "an empty overlay added a House rules heading")
        check_arm(state, 4, texts.get("r-one", "").endswith(
            "\n## Charter\n\n### charter §2\n\nbody two\n\n### charter §1\n\nbody one\n"),
            "two charter ids were not appended in list order")
        check_arm(state, 4, "## Charter" not in texts.get("r-two", "## Charter"),
                  "an empty charter list added a Charter heading")
        check_arm(state, 5, index["harnesses"] == [FIXTURE_HARNESS.format(prefix=FIXTURE_ROOT)],
                  "harnesses is %r, not the one workflow-driver script" % index["harnesses"])
        target = agents / "r-one.md"
        target.write_bytes(target.read_bytes() + b"x")
        before = target.read_bytes()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = run_mode("check", kit, tool_root, root)
        check_arm(state, 6, rc == 1 and "drift .claude/agents/r-one.md" in out.getvalue(),
                  "a type with one byte appended did not read drift")
        check_arm(state, 6, target.read_bytes() == before, "--check changed a file's bytes")
        target.write_bytes(before[:-1])
        index["roles"]["r-retired"] = {"agent": True, "workflow": "w1", "writes": "spec"}
        (root / ".claude" / "roles.json").write_text(json.dumps(index), encoding="utf-8")
        (agents / "r-retired.md").write_text("retired\n", encoding="utf-8")
        (agents / "my-agent.md").write_bytes(b"foreign\r\n")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = run_mode("check", kit, tool_root, root)
        check_arm(state, 7, rc == 1 and "stale .claude/agents/r-retired.md" in out.getvalue(),
                  "a name the index lists and the catalogue does not render did not read stale")
        with contextlib.redirect_stdout(io.StringIO()):
            rc = run_mode("write", kit, tool_root, root)
        check_arm(state, 7, rc == 0 and not (agents / "r-retired.md").exists(),
                  "--write did not unlink the stale type")
        check_arm(state, 7, (agents / "my-agent.md").read_bytes() == b"foreign\r\n",
                  "--write moved a file the renderer does not own")
        for p in list(agents.glob("r-*.md")) + [root / ".claude" / "roles.json"]:
            p.write_bytes(p.read_bytes().replace(b"\n", b"\r\n"))
        with contextlib.redirect_stdout(io.StringIO()):
            rc = run_mode("check", kit, tool_root, root)
        check_arm(state, 9, rc == 0, "a CRLF copy of a correct render did not read fresh")
        with open(kit / "workflows.toml", "a", encoding="utf-8") as fh:
            fh.write('\n[[workflow]]\nname = "w5"\ndriver = "workflow"\n'
                     'harness = "%s"\n' % FIXTURE_MISSING)
        missing = FIXTURE_MISSING.format(prefix=FIXTURE_ROOT)
        for p in agents.glob("r-*.md"):
            p.unlink()
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            rc = run_mode("write", kit, tool_root, root)
        index = json.loads((root / ".claude" / "roles.json").read_text(encoding="utf-8"))
        check_arm(state, 10, rc == 0 and (NOTE_LINE % missing) in out.getvalue(),
                  "an absent harness did not print its note line, or the write did not exit 0")
        check_arm(state, 10, missing in index.get("harnesses", []),
                  "an absent harness is not listed in harnesses at the resolver's path")
        check_arm(state, 10, all((agents / (s + ".md")).is_file() for s in ("r-one", "r-two")),
                  "a write noting an absent harness did not write every type")
    with tempfile.TemporaryDirectory() as tmp:
        kit, tool_root = build_fixture(tmp, {})
        for mode in ("write", "check"):
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                rc = run_mode(mode, kit, tool_root, pathlib.Path(tmp))
            check_arm(state, 8, rc == 2, "a zero-role catalogue under --%s exited %d, not 2" % (mode, rc))
    for line in state["fail"]:
        print("render_agents selftest: FAIL %s" % line)
    print("%s (%d assertions)" % ("FAIL" if state["fail"] else "PASS", state["n"]))
    return 1 if state["fail"] else 0


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="render_agents.py",
                                 description="Render the role catalogue into Claude Code agent types.")
    mode = ap.add_mutually_exclusive_group(required=True)
    for flag in ("--write", "--check", "--selftest"):
        mode.add_argument(flag, action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return run_selftest()
    try:
        kit_dir, tool_root, target_root = derive_tool_root(KIT_DIR)
    except lib.RolesError as e:
        print("render_agents: %s" % e, file=sys.stderr)
        return 2
    return run_mode("write" if a.write else "check", kit_dir, tool_root, target_root)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
