#!/usr/bin/env python3
"""render_agents.py — the role catalogue rendered into Claude Code agent types (TOOL-aOrientedCast-3).

    python render_agents.py --write | --check | --selftest

`--write` renders one agent type per role whose `agent` is true, at `.claude/agents/<name>.md` under
the repository root: the role's Claude keys, then `effort: <level>` as `roles_lib.resolve_effort`
reads it from the kit's `house/policy.toml` (TOOL-aOrientedCast-10) with no model named, so a type
carries the default tables' level and never a profile's (TOOL-aProfiledEffort-1), then
`omitClaudeMd: true`, then gov's `workflow` and
`writes`, then a body that is `roles_lib.render_role`'s output and, under `## Charter`,
`roles_lib.render_charter_blocks` for the role: the practice lines its `rules` key cites, then
the charter's carried sections whole (TOOL-aOrientedCast-16). Where the playbook kit's document registry
reads, the body is ranked (PLAY-dOrderedCharter-5 S1): `## Charter` first, in the envelope of the charter's
registry row, level 0, then the role, all in the agent file's own level-5 envelope; with no playbook kit the
role comes first and the charter after it, unenveloped, and one `envelope — unarmed` note prints; a registry
that does not read refuses, naming it. A pre-tag charter renders no
`## Charter` and prints one note. Beside them it writes the generated
index `.claude/roles.json`: every role with its `workflow`, `writes`, `agent` and `gates`, the gate legs
the policy's `[gates]` table lets it run (empty where it names none), `harnesses`, the repo-relative
scripts of every workflow whose `driver` is `workflow`, and `gates.manifest`, the repo-relative path of
the tool root's gate manifest or null when no file is there (TOOL-aOrientedCast-11; scratch-guard.js reads
both to refuse a role agent a gate), and `effort`, the resolved role and stage levels of the default
tables and of every profile (TOOL-aGuardedEffort-1; agent-cap.js grades a spawn's level against
them). Everything is rendered in memory first, so a role, overlay or
rule tag that fails to resolve writes nothing.

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

A HARNESS the kit resolver did not hold prints one line under either mode. Where a file of its name
sits directly inside a directory under the tool root, beside the harness's template
`<stem>.template<suffix>` or a `kit.toml` declaring the home its listed path names, that is a
`misplaced` line naming each such file, and `--check` exits 1 on it, because the index then lists a
path the install does not hold while its kit holds the harness elsewhere (TOOL-dRenderedAnchor-1,
TOOL-dRenderedAnchor-2). A file of its name beside neither mark is not counted as its kit's, so it
reads like no file at all: a note that the kit is not installed, which never reds.

The kit directory is `git rev-parse --show-prefix` run in this script's own directory, the tool root
is its parent, and the target root is `git rev-parse --show-toplevel`; an empty derivation refuses.
Every file is read through the kit's own `roles_lib.py`; nothing here parses a role, an overlay, the
workflow table, the conf or the governing doc itself.

Exit 0 when written, fresh or passing; 1 on drift, a misplaced harness under `--check` or a failed
arm, every offending path named; 2 on usage, a `RolesError` from the library (a policy defect among
them), or a catalogue holding zero roles, since a render of nothing compares clean against an empty
directory.

WHAT THIS DOES NOT CHECK: whether a role's text is any good, or whether its front matter obeys the
catalogue's grammar, which `check_roles.py` grades; whether the Claude Code that spawns a type honours
`omitClaudeMd`, which rests on the CLI version and a server flag and is observed only by a live probe;
whether a running session has restarted since the last write; and a harness copy anywhere but
directly inside a directory under the tool root beside its template or a `kit.toml` declaring its
home, which the misplaced scan does not count, nor whether a marked copy holds the kit's bytes.
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
import tomllib

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
#: A harness the resolver did not hold while its kit's own copy sits elsewhere under the tool root:
#: a file of its name directly inside a directory there, beside the harness's template or a
#: `kit.toml` declaring the home its listed path names.
MISPLACED_LINE = ("render_agents: misplaced %s — the workflow table names it and it is absent "
                  "here, while its kit holds it at %s; the kit resolver did not find it")
MANIFEST_NOTE = ("render_agents: note — %s is absent, so the index names no gate manifest and a role "
                 "agent's gate-leg row is unarmed")
#: The self-test fixture's two workflow-driver harnesses, spelled as its own table writes them. The
#: arms format each with the fixture's tool root instead of typing a second literal of the path.
FIXTURE_HARNESS = "{prefix}/workflows/a.js"
FIXTURE_MISSING = "{prefix}/workflows/missing.js"
FIXTURE_ROOT = "toolroot"
#: Every fixture kit carries a policy, so an absent file never reads as the fixture's normal state.
FIXTURE_POLICY = '[effort]\ndefault = "medium"\n'
#: The fixture's governing doc: a tagged charter inside a playbook region, its practices between their
#: markers under an unnumbered heading, a tagged micro-format rule after them, an authored section after it.
FIXTURE_DOC = ("<!-- gov:playbook -->\n# Doc\n\n## Practices\n\n<!-- gov:practices -->\n<!-- one-line -->\n"
               "- [one] Rule one.\n- [two] Rule two.\n<!-- /one-line -->\n<!-- /gov:practices -->\n\n"
               "### Micro-formats\n\n- [state] A micro-format rule.\n\n"
               "## Protocols — read the one whose trigger holds\n\n"
               "- A pass: `mem/P.md`.\n\n## Facts\n\n- **Fact:** one.\n<!-- /gov:playbook -->\n\n"
               "## Authored\n\nafter the region\n")
#: A charter seeded before the practices markers (PLAY-dOrderedCharter-2 S6), its rules under a numbered first heading.
LEGACY_FIXTURE_DOC = "<!-- gov:playbook -->\n# Doc\n\n## 1. Practices\n\n- [one] Rule one.\n- [two] Rule two.\n\n" + FIXTURE_DOC[FIXTURE_DOC.index("## Protocols"):]


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
    """The roles, the workflow table, MEMORY_ROOT and the parsed governing doc, through the library."""
    roles = lib.load_roles(kit_dir)
    if not roles:
        raise lib.RolesError("%s holds zero roles, and a render of nothing compares clean against an "
                             "empty directory" % (pathlib.Path(kit_dir) / "agents").as_posix())
    conf = pathlib.Path(target_root) / ".memory-tree.conf"
    memory_root = lib.read_conf_key(conf, "MEMORY_ROOT") if conf.is_file() else None
    if not memory_root:
        raise lib.RolesError("%s declares no MEMORY_ROOT, or is absent" % conf.as_posix())
    charter_path = lib.resolve_charter_path(target_root)
    doc = pathlib.Path(os.path.relpath(str(charter_path), str(target_root))).as_posix()
    charter = lib.parse_charter(lib.load_text(charter_path), doc)
    workflows = lib.load_workflows(kit_dir)
    notes = [lib.LEGACY_NOTE % doc] if charter["shape"] == "legacy" else []
    return {"roles": roles, "workflows": workflows, "memory_root": memory_root,
            "policy": lib.load_policy(kit_dir, roles, workflows, notes),
            "notes": notes, "charter": charter, "charter_doc": doc}


def render_agent_file(kit_dir, slot, role, memory_root, charter, notes, effort, missing=(), rows=None,
                      charter_doc=""):
    """One agent type's text: Claude keys, its effort, the trim, gov's two keys, then the body. With
    `rows`, the document registry, the body is ranked (PLAY-dOrderedCharter-5 S1): `## Charter` and the
    role's charter blocks first, in the envelope of the charter's row at `charter_doc`, then the rendered
    role and each `Missing required unit:` line the load-set check printed for it under `warn`, all in the
    agent file's own envelope. With `rows` None, no playbook kit, the role comes first and the charter
    after it, unenveloped. A charter that yields no block renders no `## Charter`."""
    keys = role["keys"]
    head = ["---"] + ["%s: %s" % (k, keys[k]) for k in CLAUDE_KEYS if k in keys]
    head += ["effort: %s" % effort, "omitClaudeMd: true", "workflow: %s" % keys.get("workflow", ""),
             "writes: %s" % keys.get("writes", ""), "---"]
    body = lib.render_role(kit_dir, slot, memory_root)
    if missing:
        body += "\n" + "\n".join(missing) + "\n"
    blocks = lib.render_charter_blocks(charter, role["path"].as_posix(), keys.get("rules", ""), notes)
    if blocks and rows is None:
        body += "\n## Charter\n\n" + blocks
    elif blocks:
        blocks = "## Charter\n\n" + blocks
        row = lib.read_envelope_row(rows, charter_doc, memory_root)
        if row is not None:
            blocks = lib.render_envelope(charter_doc, row[0], row[1], blocks)
        body = blocks + "\n" + body
    # PLAY-dOrderedCharter-3 S4: the body after the front matter in its envelope, where a registry row names it
    rel = "%s/%s.md" % (AGENTS_REL, slot)
    row = lib.read_envelope_row(rows, rel, memory_root)
    if row is not None:
        body = lib.render_envelope(rel, row[0], row[1], body)
    return "\n".join(head) + "\n" + body


def derive_harness_paths(workflows, tool_root, target_root):
    """`(harnesses, absent)`: each `workflow`-driver harness resolved, repo-relative, sorted and unique."""
    found, absent = set(), set()
    for harness in lib.extract_workflow_harnesses(workflows):
        path, held = lib.resolve_harness_path(tool_root, harness)
        rel = pathlib.Path(os.path.relpath(str(path), str(target_root))).as_posix()
        found.add(rel)
        if not held:
            absent.add(rel)
    return sorted(found), sorted(absent)


def read_kit_home(descriptor):
    """The `home` a `kit.toml` declares, or None when it is absent, unreadable or not TOML."""
    try:
        with open(descriptor, "rb") as fh:
            home = tomllib.load(fh).get("home")
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError):
        return None
    return home if isinstance(home, str) else None


def scan_misplaced_harnesses(absent, tool_root, target_root):
    """`{rel: [found rel, ...]}` for each absent harness whose file sits directly inside a directory
    under the tool root beside a mark of its kit: the harness's template, `<stem>.template<suffix>`,
    or a `kit.toml` declaring the home its listed path names. Any other harness is not a key.

    It reads the disk, never the receipt or the resolver it guards (TOOL-dRenderedAnchor-2). The
    listed path's home is its parent's name, because `resolve_harness_path` spells an unheld
    harness `<tool root>/<home>/<file>`."""
    misplaced = {}
    for rel in absent:
        listed = pathlib.PurePosixPath(rel)
        template = listed.stem + ".template" + listed.suffix
        hits = [pathlib.Path(os.path.relpath(str(d / listed.name), str(target_root))).as_posix()
                for d in sorted(pathlib.Path(tool_root).iterdir())
                if d.is_dir() and (d / listed.name).is_file()
                and ((d / template).is_file() or read_kit_home(d / "kit.toml") == listed.parent.name)]
        if hits:
            misplaced[rel] = hits
    return misplaced


def resolve_gate_manifest(tool_root, target_root):
    """The tool root's gate manifest, repo-relative, or None when no file is there."""
    p = pathlib.Path(tool_root) / lib.GATE_MANIFEST
    return pathlib.Path(os.path.relpath(str(p), str(target_root))).as_posix() if p.is_file() else None


def derive_effort_index(policy, roles, workflows, tool_root, target_root):
    """The index's `effort` value (TOOL-aGuardedEffort-1), every level resolved here so the spawn
    guard only looks up: `default` and each `profiles.<name>` hold `roles`, every `agent`-true
    role's level, and `stages`, each stage key's level for every `workflow`-driver workflow, a
    profile's read with its first `match` word as the model and its `match` beside them;
    `harnesses` maps each listed harness, spelled as `derive_harness_paths` spells it, to the
    sorted names of the workflows it runs; `unset` holds each stage key's slot's rendered level.
    A driven workflow with no `stages` table keeps its harness and reads `{}` in every `stages`
    map and in `unset` (TOOL-aGuardedEffort-2 S3): the spawn guard holds the maps to one
    population of stage keys, and a missing entry is a broken index to it."""
    slots = [s for s, r in roles.items() if r["keys"].get("agent", "true") == "true"]
    driven = [w for w in workflows if w.get("driver") == "workflow"]
    tables = {}
    profiles = policy["effort"].get("profiles", {})
    for name, model in [(None, None)] + [(n, p["match"][0]) for n, p in profiles.items()]:
        tables[name] = {"roles": {s: lib.resolve_effort(policy, s, model) for s in slots},
                        "stages": {w["name"]: lib.resolve_stage_efforts(policy, w, model) for w in driven}}
    runs = {}
    for w in driven:
        path, _held = lib.resolve_harness_path(tool_root, w.get("harness"))
        rel = pathlib.Path(os.path.relpath(str(path), str(target_root))).as_posix()
        runs.setdefault(rel, set()).add(w["name"])
    return {"default": tables[None],
            "profiles": {n: dict(tables[n], match=list(p["match"])) for n, p in profiles.items()},
            "harnesses": {rel: sorted(names) for rel, names in runs.items()},
            "unset": {w["name"]: {key: lib.resolve_effort(policy, slot)
                                  for key, slot in (w.get("stages") or {}).items()} for w in driven}}


def render_roles_index(roles, harnesses, policy, manifest, effort):
    """The index bytes: every role's `workflow`, `writes`, `agent` and `gates`, the harness list,
    the gate manifest's path and `derive_effort_index`'s `effort`."""
    allow = policy.get("gates", {})
    obj = {"effort": effort, "gates": {"manifest": manifest}, "harnesses": harnesses,
           "roles": {slot: {"agent": r["keys"].get("agent", "true") == "true",
                            "gates": list(allow.get(slot, [])),
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
        agents = [slot for slot, role in cat["roles"].items() if role["keys"].get("agent", "true") == "true"]
        # PLAY-dOrderedCharter-11 S4: every agent type's load set and role block, ONE check before writing
        refused, gate = lib.check_load_set(target_root, kit_dir, [
            (slot, len(lib.render_role(kit_dir, slot, cat["memory_root"]).encode("utf-8"))) for slot in agents])
        if refused:
            raise lib.RolesError("\n".join(gate))
        missing = {slot: [ln for ln in gate if ln.startswith("Missing required unit:")
                          and ln.endswith(" · role." + slot)] for slot in agents}
        cat["notes"].extend(ln for ln in gate if not ln.startswith("Missing required unit:"))
        try:
            rows = lib.load_document_registry(kit_dir)
        except LookupError as exc:   # no playbook kit: the roles kit does not require it (F4)
            rows = None
            cat["notes"].append(lib.UNRANKED_NOTE % exc)
        rendered = {}
        for slot in agents:
            rendered["%s/%s.md" % (AGENTS_REL, slot)] = render_agent_file(
                kit_dir, slot, cat["roles"][slot], cat["memory_root"], cat["charter"], cat["notes"],
                lib.resolve_effort(cat["policy"], slot), missing[slot], rows, cat["charter_doc"])
        harnesses, absent = derive_harness_paths(cat["workflows"], tool_root, target_root)
        manifest = resolve_gate_manifest(tool_root, target_root)
        rendered[INDEX_REL] = render_roles_index(
            cat["roles"], harnesses, cat["policy"], manifest,
            derive_effort_index(cat["policy"], cat["roles"], cat["workflows"], tool_root, target_root))
    except lib.RolesError as e:
        print("\n".join("render_agents: " + ln for ln in str(e).split("\n")), file=sys.stderr)
        return 2
    misplaced = scan_misplaced_harnesses(absent, tool_root, target_root)
    for rel in absent:
        print(MISPLACED_LINE % (rel, ", ".join(misplaced[rel])) if rel in misplaced else NOTE_LINE % rel)
    if manifest is None:
        print(MANIFEST_NOTE % (pathlib.Path(tool_root) / lib.GATE_MANIFEST).as_posix())
    for line in cat["notes"]:
        print("render_agents: note — %s" % line)
    types = len(rendered) - 1
    kit_rel = pathlib.Path(os.path.relpath(str(kit_dir), str(target_root))).as_posix()
    remedy = "python %s/render_agents.py --write" % kit_rel
    offenders = check_rendered(target_root, rendered)
    if mode == "check":
        print("render_agents: %d agent type(s) and 1 index graded" % types)
        if offenders:
            print_drift(offenders, remedy)
            return 1
        return 1 if misplaced else 0
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


def build_fixture(root, roles, policy=FIXTURE_POLICY):
    """A catalogue in <root>: kit, overlays, policy, workflow table, conf, governing doc, stub harnesses."""
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
    (kit / "house" / "policy.toml").write_text(policy, encoding="utf-8")
    for stub in ("a.js", "b.js"):
        (stubs / stub).write_text("// stub\n", encoding="utf-8")
    (kit / "workflows.toml").write_text(
        '[[workflow]]\nname = "w1"\ndriver = "workflow"\nharness = "%s"\n\n'
        '[[workflow]]\nname = "w2"\ndriver = "workflow"\nharness = "%s"\n\n'
        '[[workflow]]\nname = "w3"\ndriver = "program"\nharness = "python {prefix}/roles/x.py"\n\n'
        '[[workflow]]\nname = "w4"\ndriver = "agent"\nharness = "none"\n'
        % (FIXTURE_HARNESS, FIXTURE_HARNESS), encoding="utf-8")
    (root / ".memory-tree.conf").write_text("MEMORY_ROOT=mem\nCHARTER=DOC.md\n", encoding="utf-8")
    (root / "DOC.md").write_text(FIXTURE_DOC, encoding="utf-8")
    return kit, root / FIXTURE_ROOT


def check_arm(state, arm, ok, what):
    """Count one assertion, and record arm <arm> as failed with <what> when <ok> is false."""
    state["n"] += 1
    if not ok:
        state["fail"].append("arm %d — %s" % (arm, what))


def check_charter_shape_arms(state, roles):
    """Arm 19 (PLAY-dOrderedCharter-2 S6): a charter seeded before the practices markers still renders a
    role's cited rules; a tag outside the markers is no practice, so citing it refuses R4; and a charter
    carrying neither the markers nor the numbered first heading refuses R0."""
    pair = {s: roles[s] for s in ("r-one", "r-two")}
    neither = FIXTURE_DOC.replace("<!-- gov:practices -->\n", "").replace("<!-- /gov:practices -->\n", "")
    cut = dict(pair, **{"r-one": (roles["r-one"][0].replace("rules: two, one", "rules: one, state"), "")})
    for case, doc, cast, want in (("19a", LEGACY_FIXTURE_DOC, pair, 0), ("19b", FIXTURE_DOC, cut, 2),
                                  ("19c", neither, pair, 2)):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            kit, tool_root = build_fixture(root, cast)
            (root / "DOC.md").write_text(doc, encoding="utf-8")
            err = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
                rc = run_mode("write", kit, tool_root, root)
            agent = root / ".claude" / "agents" / "r-one.md"
            text = agent.read_text(encoding="utf-8") if agent.is_file() else ""
            if case == "19a":
                check_arm(state, 19, rc == 0 and "### Charter rules\n\n- [one] Rule one.\n- [two] Rule two.\n" in text,
                          "a charter seeded before the markers exited %d without r-one's two rules" % rc)
            else:
                rule = "R4" if case == "19b" else "R0"
                check_arm(state, 19, rc == want and rule in err.getvalue() and not text,
                          "%s: exited %d without %s, or wrote r-one: %s" % (case, rc, rule, err.getvalue()))


#: Arm 20's document registry (PLAY-dOrderedCharter-5): the fixture's charter at level 0, its agent types at 5.
FIXTURE_REGISTRY = ('[[document]]\ntag = "doc.charter"\npath = "DOC.md"\nlevel = 0\ndirection = "The fixture charter"\n'
                    'source = "DOC.md"\n\n[[document]]\ntag = "doc.agent"\npath = ".claude/agents/*.md"\nlevel = 5\n'
                    'direction = "The fixture role"\nsource = "x"\n')


def check_ranked_arms(state, roles):
    """Arm 20 (PLAY-dOrderedCharter-5): with a playbook kit's registry beside the fixture kit, an agent file
    opens its body with the charter's level-0 envelope inside its own level-5 one (AC1); a handoff carries
    level 5 under `## Role` and levels 0 then 6 under `## Task`, and no charter rule line (AC2, AC3); `check`
    passes it and exits 1 on the level-6 envelope moved above the level-0 one and on a deleted closer, naming
    the envelope (AC4). A registry that does not read refuses naming it; no playbook kit renders unranked
    with one unarmed note (F4). The practices block's reach is handed in for the load-set check's run."""
    import handoff
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        kit, tool_root = build_fixture(root, {"r-one": roles["r-one"]})
        pb_home = "playbook"   # the fixture's playbook home under its tool root, joined through this one name
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            run_mode("write", kit, tool_root, root)
        check_arm(state, 20, sum(lib.UNRANKED_NOTE.split(":")[0] in ln for ln in out.getvalue().splitlines()) == 1,
                  "no playbook kit printed no single unarmed line")
        (tool_root / pb_home).mkdir()
        (tool_root / pb_home / "documents.toml").write_text("[[document]\n", encoding="utf-8")
        err = io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            rc = run_mode("write", kit, tool_root, root)
        check_arm(state, 20, rc == 2 and "documents.toml: the document registry does not read" in err.getvalue(),
                  "a registry that does not read exited %d without naming it: %s" % (rc, err.getvalue()))
        (tool_root / pb_home / "documents.toml").write_text(FIXTURE_REGISTRY, encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc = run_mode("write", kit, tool_root, root)
        agent = (root / AGENTS_REL / "r-one.md").read_text(encoding="utf-8")
        found = lib.read_envelopes(agent)
        check_arm(state, 20, rc == 0 and [(k, d, lv) for _n, k, d, lv, _x in found[:2]] == [
            ("open", ".claude/agents/r-one.md", 5), ("open", "DOC.md", 0)] and found[-1][1:3] == (
            "close", ".claude/agents/r-one.md") and agent.index("- [one] Rule one.") < agent.index("[/DOC.md]")
            < agent.index("Body of r-one"), "the agent file is not ranked, charter first: %r" % agent)
        (root / "mem" / "builds" / "fx" / "prompts").mkdir(parents=True)
        (root / "spec.md").write_text("spec\n", encoding="utf-8")
        saved = (handoff.KIT_DIR, handoff.WORK_ORDER, lib.check_load_set)
        handoff.KIT_DIR, handoff.WORK_ORDER = kit, KIT_DIR / "templates" / "work-order.template.md"
        lib.check_load_set = lambda *a, **k: (False, [handoff.REACH_LINE + "role.r-one · practice.one.build · "
                                                      "Reach of one."])
        try:
            keys = lib.load_roles(kit)["r-one"]["keys"]
            path, text, task = handoff.render_handoff(root, "mem", root / "DOC.md", "r-one", keys, "fx",
                                                      "PLAY-fx-1", None, {"spec": "spec.md"}, None, [])
        finally:
            handoff.KIT_DIR, handoff.WORK_ORDER, lib.check_load_set = saved
        path.write_text(text, encoding="utf-8", newline="\n")
        at = text.index("\n## Task\n")
        levels = [[lv for n, k, _d, lv, _x in lib.read_envelopes(part) if k == "open"]
                  for part in (text[:at], text[at:])]
        check_arm(state, 20, levels == [[5], [0, 6]] and task.split("\n\n", 1)[-1].startswith(
                  "## Task\n\n[DOC.md#practices-at-build · Level 0 · "),
                  "the handoff's levels per part are %r, not [5] then [0, 6] under its heading" % levels)
        check_arm(state, 20, "### Charter rules" not in task and "- [one] Rule one." not in task,
                  "the task part carries the charter")
        rel = path.relative_to(root).as_posix()
        ok, said = handoff.check_handoff(root, rel)
        check_arm(state, 20, ok and said[-1].endswith("envelopes — Role 5 · Task 0 6"),
                  "check over the rendered handoff: %r" % said)
        lines = text.split("\n")
        o0 = next(i for i, ln in enumerate(lines) if ln.startswith("[DOC.md#"))
        c0 = lines.index("[/DOC.md#practices-at-build]")
        for name, planted in (("reordered", lines[:o0] + lines[c0 + 1:-1] + lines[o0:c0 + 1] + [""]),
                              ("unclosed", lines[:c0] + lines[c0 + 1:])):
            plant = "\n".join(planted)
            m = handoff.MARKER_RE.search(plant)
            r, t = plant.index("\n## Role\n") + 1, plant.index("\n## Task\n") + 1
            plant = plant.replace(m.group(0), m.group(0).replace(m.group(5), handoff.derive_section_sha(
                plant[r:t])).replace(m.group(6), handoff.derive_section_sha(plant[t:])))
            path.write_text(plant, encoding="utf-8", newline="\n")
            ok, said = handoff.check_handoff(root, rel)
            want = "opens at level 0 after" if name == "reordered" else "has no closer"
            check_arm(state, 20, not ok and any("DOC.md#practices-at-build" in ln and want in ln for ln in said),
                      "the %s envelope passed check: %r" % (name, said))


def run_selftest():
    """The arms over fixture catalogues; prints PASS or FAIL with the assertion count."""
    state = {"n": 0, "fail": []}
    roles = {"r-one": ("maxTurns: 7\nworkflow: w1\nreads: input:spec\nwrites: product\n"
                       "rules: two, one\n", "Overlay line.\n"),
             "r-two": ("workflow: w1\nreads: input:spec\nwrites: spec\nrules: \n", ""),
             "r-off": ("workflow: w4\nreads: input:spec\nwrites: none\nrules: one\nagent: false\n", "")}
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
        carried = ("### Protocols — read the one whose trigger holds\n\n- A pass: `mem/P.md`.\n\n"
                   "### Facts\n\n- **Fact:** one.\n")
        check_arm(state, 4, texts.get("r-one", "").endswith(
            "\n## Charter\n\n### Charter rules\n\n- [one] Rule one.\n- [two] Rule two.\n\n" + carried),
            "two rule tags were not carried in charter order before the carried sections")
        check_arm(state, 4, texts.get("r-two", "").endswith("\n## Charter\n\n" + carried)
                  and "### Charter rules" not in texts.get("r-two", ""),
                  "an empty rules list did not carry the two sections alone")
        check_arm(state, 4, not any("after the region" in t for t in texts.values()),
                  "a type carries text from outside the playbook region")
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
        # Arm 20 (TOOL-aGuardedEffort-2 S3): `w5` above is a driven workflow with no `stages` table.
        effort = index.get("effort", {})
        check_arm(state, 20, "w5" in effort.get("harnesses", {}).get(missing, []),
                  "a stageless driven workflow left effort.harnesses")
        check_arm(state, 20, effort.get("default", {}).get("stages", {}).get("w5") == {}
                  and effort.get("unset", {}).get("w5") == {},
                  "a stageless driven workflow is not {} in effort.default.stages and effort.unset")
    with tempfile.TemporaryDirectory() as tmp:
        kit, tool_root = build_fixture(tmp, {})
        for mode in ("write", "check"):
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                rc = run_mode(mode, kit, tool_root, pathlib.Path(tmp))
            check_arm(state, 8, rc == 2, "a zero-role catalogue under --%s exited %d, not 2" % (mode, rc))
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        policy = '[effort]\ndefault = "low"\n\n[effort.roles]\nr-one = "high"\n'
        kit, tool_root = build_fixture(root, {s: roles[s] for s in ("r-one", "r-two")}, policy)
        agents = root / ".claude" / "agents"
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc = run_mode("write", kit, tool_root, root)
        for slot, level in (("r-one", "high"), ("r-two", "low")):
            p = agents / (slot + ".md")
            head = p.read_text(encoding="utf-8").split("\n") if p.is_file() else []
            at = head.index("omitClaudeMd: true") if "omitClaudeMd: true" in head else 0
            check_arm(state, 11, rc == 0 and at > 0 and head[at - 1] == "effort: %s" % level,
                      "%s does not carry effort: %s on the line before omitClaudeMd" % (slot, level))
        before = {p.name: p.read_bytes() for p in agents.glob("*")}
        (kit / "house" / "policy.toml").write_text(policy + 'r-two = "extra"\n', encoding="utf-8")
        err = io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            rc = run_mode("write", kit, tool_root, root)
        check_arm(state, 11, rc == 2 and "effort.roles.r-two" in err.getvalue()
                  and ", ".join(lib.EFFORT_LEVELS) in err.getvalue(),
                  "a refused level exited %d without naming r-two and the five levels" % rc)
        check_arm(state, 11, {p.name: p.read_bytes() for p in agents.glob("*")} == before,
                  "a refused level wrote a file")
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        policy = FIXTURE_POLICY + '\n[gates]\nr-one = ["leg a"]\n'
        kit, tool_root = build_fixture(root, {s: roles[s] for s in ("r-one", "r-two")}, policy)
        (tool_root / lib.GATE_MANIFEST).write_text(
            '[{"name": "leg a", "argv": ["bash", "{prefix}/a.sh"]}]\n', encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc = run_mode("write", kit, tool_root, root)
        index_path = root / ".claude" / "roles.json"
        good = index_path.read_bytes() if index_path.is_file() else b"{}"
        index = json.loads(good)
        check_arm(state, 12, rc == 0 and index.get("gates") == {
            "manifest": "%s/%s" % (FIXTURE_ROOT, lib.GATE_MANIFEST)}, "the index's gates is %r, not the "
            "fixture's manifest path" % index.get("gates"))
        held = {s: r.get("gates") for s, r in index.get("roles", {}).items()}
        check_arm(state, 12, held == {"r-one": ["leg a"], "r-two": []},
                  "the index's role gates are %r, not r-one's one leg and r-two's none" % held)
        for staged in ("a role's gates", "the manifest"):
            broken = json.loads(good)
            if staged == "the manifest":
                broken.get("gates", {})["manifest"] = None
            else:
                broken.get("roles", {}).get("r-one", {}).pop("gates", None)
            index_path.write_text(json.dumps(broken, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                rc = run_mode("check", kit, tool_root, root)
            check_arm(state, 12, rc == 1 and "drift %s" % INDEX_REL in out.getvalue(),
                      "an index with %s staged out of the render did not read drift" % staged)
        index_path.write_bytes(good)
        (kit / "house" / "policy.toml").write_text(FIXTURE_POLICY + '\n[gates]\nr-one = ["nope"]\n',
                                                   encoding="utf-8")
        err = io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            rc = run_mode("write", kit, tool_root, root)
        check_arm(state, 12, rc == 2 and "gates.r-one" in err.getvalue() and "'nope'" in err.getvalue(),
                  "a leg name the manifest does not hold exited %d without naming it" % rc)
        check_arm(state, 12, index_path.read_bytes() == good, "a refused leg name wrote the index")
        (kit / "house" / "policy.toml").write_text(
            FIXTURE_POLICY + '\n[gates]\nr-one = ["leg a", "absent?"]\n', encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            rc = run_mode("write", kit, tool_root, root)
        index = json.loads(index_path.read_bytes()) if index_path.is_file() else {}
        held = index.get("roles", {}).get("r-one", {}).get("gates")
        # ONE line carries both (TOOL-aOrientedCast-15 S8): two substrings anywhere in the output
        # would pass a note about something else beside an unrelated line naming the leg.
        check_arm(state, 13, rc == 0 and any(ln.startswith("render_agents: note") and "'absent'" in ln
                                             for ln in out.getvalue().splitlines()),
                  "an optional leg the manifest lacks exited %d without a note naming it" % rc)
        check_arm(state, 13, held == ["leg a", "absent"],
                  "r-one's index gates are %r, not the two leg names with the ? taken off" % held)
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        kit, tool_root = build_fixture(root, {s: roles[s] for s in ("r-one", "r-two")})
        (root / "DOC.md").write_text("# Doc\n\n## §1 — One\n\nbody one\n\n## §2 — Two\n\nbody two\n",
                                     encoding="utf-8")
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            rc = run_mode("write", kit, tool_root, root)
        texts = [p.read_text(encoding="utf-8") for p in (root / ".claude" / "agents").glob("*.md")]
        check_arm(state, 14, rc == 0 and len([ln for ln in out.getvalue().splitlines()
                                              if ln.startswith("render_agents: note") and "reseed" in ln]) == 1,
                  "a pre-tag charter exited %d without one reseed note line" % rc)
        check_arm(state, 14, len(texts) == 2 and not any("## Charter" in t for t in texts),
                  "a pre-tag charter did not render both types with no Charter section")
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        base = roles["r-one"][0]
        for extra, want in ((", three?", 0), (", three", 2)):
            cut = {"r-one": (base.replace("rules: two, one\n", "rules: two, one%s\n" % extra), roles["r-one"][1]),
                   "r-two": roles["r-two"]}
            kit, tool_root = build_fixture(root, cut)
            before = {p: p.read_bytes() for p in (root / ".claude").rglob("*") if p.is_file()}
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                rc = run_mode("write", kit, tool_root, root)
            if want == 0:
                check_arm(state, 15, rc == 0 and len([ln for ln in out.getvalue().splitlines()
                                                      if ln.startswith("render_agents: note")
                                                      and "'three?'" in ln]) == 1,
                          "an optional tag the charter lacks exited %d without one note naming it" % rc)
            else:
                check_arm(state, 15, rc == 2 and "'three'" in err.getvalue() and "R4" in err.getvalue(),
                          "a bare tag the charter lacks exited %d without naming it and R4" % rc)
                after = {p: p.read_bytes() for p in (root / ".claude").rglob("*") if p.is_file()}
                check_arm(state, 15, bool(before) and after == before, "a refused rule tag wrote a file")
    # Arms 16 and 17 (TOOL-dRenderedAnchor-1): the adopter shape, where govkit lands a kit under its
    # id rather than its home, so the stub directory is renamed and `.git` at the root is where the
    # resolver reads the receipt. Arm 16 holds the harness through its rendered row; arm 17 has no
    # receipt, so the harness is misplaced while the file sits in the renamed directory beside a mark
    # of its kit, and a note once it sits nowhere. Every mark and decoy is derived from the listed
    # path, never typed: a literal kit segment followed by a file is an install-prefix hit.
    listed = pathlib.PurePosixPath(FIXTURE_HARNESS.format(prefix=FIXTURE_ROOT))
    held = listed.parent.parent / "renamed" / listed.name
    template = listed.stem + ".template" + listed.suffix
    for arm in (16, 17):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            kit, tool_root = build_fixture(root, {"r-one": roles["r-one"]})
            (root / listed.parent).rename(root / held.parent)
            (root / ".git").mkdir()
            if arm == 16:
                # TOOL-dRenderedAnchor-2 S4: two decoy rows ahead of the real one, each backed by a
                # file of the harness's name under `.claude`. Only the join's role term rejects the
                # `merged` row, and only its home term the `rendered` row from another home's
                # template, so a resolver missing either term lists the decoy.
                decoy = pathlib.PurePosixPath(".claude") / listed.name
                (root / decoy).parent.mkdir(parents=True, exist_ok=True)
                (root / decoy).write_text("// decoy\n", encoding="utf-8")
                fixture = pathlib.PurePosixPath(FIXTURE_HARNESS)
                elsewhere = (fixture.parent.parent / "other" / fixture.name).as_posix()
                (root / ".governance").mkdir()
                (root / ".governance" / "install.json").write_text(json.dumps({"files": [
                    {"role": "merged", "kit": "fixture", "path": decoy.as_posix(),
                     "source": FIXTURE_HARNESS.replace(".js", ".fragment.json")},
                    {"role": "rendered", "kit": "fixture", "path": decoy.as_posix(),
                     "source": elsewhere.replace(".js", ".template.js")},
                    {"role": "rendered", "kit": "fixture", "path": held.as_posix(),
                     "source": FIXTURE_HARNESS.replace(".js", ".template.js")}]}), encoding="utf-8")
            else:
                (root / held.parent / template).write_text("// template\n", encoding="utf-8")
            outs, rcs = [], []
            for mode in ("write", "check"):
                out = io.StringIO()
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                    rcs.append(run_mode(mode, kit, tool_root, root))
                outs.append(out.getvalue().splitlines())
            index_path = root / ".claude" / "roles.json"
            index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.is_file() else {}
            wrong = [ln for lines in outs for ln in lines if ln.startswith("render_agents: misplaced")
                     or ln in (NOTE_LINE % listed, NOTE_LINE % held)]
            if arm == 16:
                check_arm(state, 16, rcs == [0, 0] and index.get("harnesses") == [held.as_posix()],
                          "a harness held by its rendered receipt row exited %r with harnesses %r, not "
                          "0, 0 and %s" % (rcs, index.get("harnesses"), held))
                check_arm(state, 16, not wrong, "a harness held by its rendered receipt row printed %r"
                          % wrong)
                continue
            # 17a, the template beside the file (TOOL-dRenderedAnchor-2 S2).
            line = MISPLACED_LINE % (listed, held)
            check_arm(state, 17, rcs[0] == 0 and [ln for ln in outs[0] if ln.startswith(
                "render_agents: misplaced")] == [line] and (NOTE_LINE % listed) not in outs[0],
                "a harness absent where listed and held beside its template did not write with "
                "exactly its misplaced line and no note")
            check_arm(state, 17, rcs[1] == 1 and line in outs[1] and (NOTE_LINE % listed) not in outs[1],
                      "--check on a harness held beside its template exited %d without its misplaced "
                      "line alone" % rcs[1])
            # 17b, the template unlinked and a kit.toml declaring the listed home; 17c, the file
            # unlinked as well, so the harness sits nowhere.
            (root / held.parent / template).unlink()
            (root / held.parent / "kit.toml").write_text('home = "%s"\n' % listed.parent.name,
                                                         encoding="utf-8")
            for row in ("17b", "17c"):
                if row == "17c":
                    (root / held).unlink()
                out = io.StringIO()
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                    rc = run_mode("check", kit, tool_root, root)
                lines = out.getvalue().splitlines()
                said = [ln for ln in lines if ln.startswith("render_agents: misplaced")]
                if row == "17b":
                    check_arm(state, 17, rc == 1 and said == [line] and (NOTE_LINE % listed) not in lines,
                              "--check on a harness held beside a kit.toml declaring its home exited %d "
                              "without its misplaced line alone" % rc)
                else:
                    check_arm(state, 17, rc == 0 and (NOTE_LINE % listed) in lines and not said,
                              "a harness found nowhere exited %d under --check, or did not read as its "
                              "note alone" % rc)
    # Arm 18 (TOOL-dRenderedAnchor-2 S2): a namesake beside no mark of the harness's kit is the
    # adopter's own file and reads as the note, exit 0: 18a with no mark, 18b beside a kit.toml
    # declaring another home, under the fixture's prefix, and 18c at a root install, where the tool
    # root is the repository root and the scan walks every top-level directory.
    for cases in (("18a", "18b"), ("18c",)):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            kit, tool_root = build_fixture(root, {"r-one": roles["r-one"]})
            (root / ".git").mkdir()
            want, namesake = listed, listed.parent.parent / "ci" / listed.name
            if cases == ("18c",):
                tool_root = root
                want, namesake = (p.relative_to(FIXTURE_ROOT) for p in (want, namesake))
            else:
                (root / listed).unlink()
            (root / namesake.parent).mkdir()
            (root / namesake).write_text("// the adopter's own file\n", encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                run_mode("write", kit, tool_root, root)
            for case in cases:
                if case == "18b":
                    (root / namesake.parent / "kit.toml").write_text(
                        'home = "%s"\n' % namesake.parent.name, encoding="utf-8")
                out = io.StringIO()
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                    rc = run_mode("check", kit, tool_root, root)
                lines = out.getvalue().splitlines()
                check_arm(state, 18, rc == 0 and (NOTE_LINE % want) in lines
                          and not any(ln.startswith("render_agents: misplaced") for ln in lines),
                          "%s: a namesake at %s beside no mark of its kit exited %d under --check, or "
                          "did not read as the note alone" % (case, namesake, rc))
    check_charter_shape_arms(state, roles)
    check_ranked_arms(state, roles)
    # Arm 19 (TOOL-aProfiledEffort-1): a profile table per model family. 19b, a type carries the
    # default tables' level; 19a, 19c, 19d and 19f, the levels a model resolves under each policy;
    # 19e, every profile defect refuses the render under its own dotted key and writes nothing.
    # The rows also hold (TOOL-aProfiledEffort-4): a default-table stage override, `k2`, that a
    # matched profile does not inherit; a model id in mixed case; and a `match` of two words, on
    # the resolve side by its second word and on the defect side by a second word `fam` holds.
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        base = ('[effort]\ndefault = "low"\n\n[effort.roles]\nr-one = "high"\n\n'
                '[effort.stages.w5]\nk2 = "high"\n')
        fam = base + ('\n[effort.profiles.fam]\nmatch = ["fam"]\ndefault = "max"\n\n'
                      '[effort.profiles.fam.roles]\nr-two = "xhigh"\n\n'
                      '[effort.profiles.fam.stages.w5]\nk1 = "medium"\n')
        ven = fam + '\n[effort.profiles.ven]\nmatch = ["vendor", "vend2"]\ndefault = "medium"\n'
        kit, tool_root = build_fixture(root, roles, fam)
        with open(kit / "workflows.toml", "a", encoding="utf-8") as fh:
            fh.write('\n[[workflow]]\nname = "w5"\ndriver = "workflow"\nharness = "%s"\n'
                     'stages = { k1 = "r-one", k2 = "r-two" }\n' % FIXTURE_HARNESS)
        w5 = lib.load_workflows(kit)[-1]
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc = run_mode("write", kit, tool_root, root)
        before = {p: p.read_bytes() for p in (root / ".claude").rglob("*") if p.is_file()}
        for slot, level in (("r-one", "high"), ("r-two", "low")):
            p = root / ".claude" / "agents" / (slot + ".md")
            check_arm(state, 19, rc == 0 and p in before and "effort: %s" % level in before[p].decode(
                "utf-8").split("\n"), "19b: %s does not carry the default tables' effort: %s" % (slot, level))
        plain = ("high", "low", {"k1": "high", "k2": "high"})
        for row, text, model, want in (
                ("19a", base, "vendor-fam-9", plain), ("19a", base, None, plain),
                ("19c", fam, "vendor-fam-9", ("max", "xhigh", {"k1": "medium", "k2": "xhigh"})),
                ("19c", fam, "Vendor-FAM-9", ("max", "xhigh", {"k1": "medium", "k2": "xhigh"})),
                ("19d", fam, "vendor-other-9", plain), ("19d", fam, "affam-9", plain), ("19d", fam, None, plain),
                ("19f", ven, "vendor-other-9", ("medium", "medium", {"k1": "medium", "k2": "medium"})),
                ("19f", ven, "vend2-other-9", ("medium", "medium", {"k1": "medium", "k2": "medium"})),
                ("19f", ven, "vendor-fam-9", None)):
            (kit / "house" / "policy.toml").write_text(text, encoding="utf-8")
            try:
                policy = load_catalogue(kit, root)["policy"]
                got = (lib.resolve_effort(policy, "r-one", model), lib.resolve_effort(policy, "r-two", model),
                       lib.resolve_stage_efforts(policy, w5, model))
            except lib.RolesError as e:
                got = str(e)
            if want is None:   # the model two profiles match: a refusal naming it and both `match` keys
                check_arm(state, 19, isinstance(got, str) and all(s in got for s in (
                    model, "effort.profiles.fam.match", "effort.profiles.ven.match")),
                    "19f: a model two profiles match read %r, not a refusal naming both match keys" % (got,))
                continue
            check_arm(state, 19, got == want, "%s: the model %r read %r, not %r" % (row, model, got, want))
        for lines, key in (
                ('match = ["x"]\ndefault = "low"\nextra = 1\n', "x.extra"),
                ('match = ["x"]\ndefault = "extra"\n', "x.default"),
                ('match = ["x"]\n', "x.default"),
                ('match = ["x"]\ndefault = "low"\n\n[effort.profiles.x.roles]\nr-nobody = "low"\n', "x.roles.r-nobody"),
                ('match = ["x"]\ndefault = "low"\n\n[effort.profiles.x.roles]\nr-off = "low"\n', "x.roles.r-off"),
                ('match = ["x"]\ndefault = "low"\n\n[effort.profiles.x.stages.w5]\nk9 = "low"\n', "x.stages.w5.k9"),
                ('match = ["x"]\ndefault = "low"\n\n[effort.profiles.x.stages.w3]\nk1 = "low"\n', "x.stages.w3"),
                ('default = "low"\n', "x.match"),
                ('match = "x"\ndefault = "low"\n', "x.match"),
                ('match = []\ndefault = "low"\n', "x.match"),
                ('match = ["vendor-x"]\ndefault = "low"\n', "x.match"),
                ('match = ["fam"]\ndefault = "low"\n', "x.match"),
                ('match = ["x", "fam"]\ndefault = "low"\n', "x.match"),
                (None, "x")):
            row = '\n[effort.profiles]\nx = "low"\n' if lines is None else "\n[effort.profiles.x]\n" + lines
            (kit / "house" / "policy.toml").write_text(fam + row, encoding="utf-8")
            err = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
                rc = run_mode("write", kit, tool_root, root)
            said = [ln for ln in err.getvalue().splitlines() if " R12 " in ln]
            check_arm(state, 19, rc == 2 and len(said) == 1 and " — effort.profiles.%s — " % key in said[0],
                      "19e: a profile holding %r exited %d saying %r, not 2 with one line under "
                      "effort.profiles.%s" % (lines, rc, said, key))
            check_arm(state, 19, bool(before) and before == {
                p: p.read_bytes() for p in (root / ".claude").rglob("*") if p.is_file()},
                "19e: a refused profile holding %r moved a file under .claude" % (lines,))
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
