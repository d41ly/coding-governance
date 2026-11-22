#!/usr/bin/env python3
"""factories.py — the factories of six registered kinds and the command kind's gate (TOOL-dDeclaredLoop-6).

    python factories.py command <verb> --kit <id> --run <path>
    python factories.py policy-key <name> --allowed <toml> --default <toml> --summary <text> --usage <text> --owner <build>
    python factories.py hook <name> --kit <id> --event <event> [--matcher <m>]
    python factories.py role <slot> --workflow <name> --writes <class> --description <text> --reads <keys>
                        --returns <text> --output <text> --ceiling <bytes>
    python factories.py workflow <name> --driver <driver> --harness <path|none> --roles <slots>
                        --enforced-by <text> --trigger <text> --order <n> --step <step tag|none>
    python factories.py scenario <name> --extends <tag|none> --admit <fact>=<value>... --entry <step tag>
    python factories.py check-commands
    python factories.py --fixture --plant <case>
    python factories.py --selftest

THE KINDS. The kinds register's `kind.command`, `kind.policy-key`, `kind.hook`, `kind.role` and
`kind.workflow` rows each name one subcommand here as their `factory`, so `python <prefix>/playbook/core.py
new <kind> <name> ...` runs it with the name and the flags appended. Each writes an instance that already
conforms, then runs the kind's gate over the whole population:

- `command` appends one `[[command]]` row, `verb` and `run`, to the kit descriptor whose top-level `id` is
  `--kit`, the row the playbook kit's `command` namespace reads; `run` is relative to the descriptor's
  directory. Its gate is `check-commands`.
- `policy-key` appends one `[[key]]` row to the policy kit's catalogue, with `summary` and `usage`, so the
  kit's shrink-only list of unsummarised rows is never touched. Its gate is `POLICY_KEY_ARMS`, the four
  arms of the policy kit's `check_policy.py` that read the working tree's catalogue, policy file and the
  kit's own list and never a render at a revision, run in process through its `run_arm`. It writes the
  catalogue, never the repository's policy file nor its mirror: the mirror is its caller's next commit.
- `hook` writes `<name>.js` and `<name>.fragment.json` in the directory of the descriptor whose `id` is
  `--kit`, the fragment holding `name`, `event`, `matcher`, `marker` and `hook_path`, and appends a
  `[[files]]` row shipping each file to `{prefix}/<home>/<file>` where no `include` already matches it.
  Its gate is `check-hook-destinations.sh` in the tool root, which grades tracked fragments only, so it
  runs with `GIT_INDEX_FILE` naming a copy of the caller's index, in a temporary directory, into which
  `git add` has put the three files written; the directory is removed on the way out and the caller's
  index is never written.
- `role` writes `<slot>.agent.md` under the roles kit's `agents/`, `mandatory: no`, an empty `rules` and a
  one-line body; lists the slot in its workflow's `roles`; writes the slot's ceiling row into the roles
  kit's `BODY_CEILINGS`; and re-renders that kit's README catalogue region through `check_roles.py
  --write`, whose grade is the gate.
- `workflow` appends a `[[workflow]]` row to the roles kit's `workflows.toml`, its `name`, `order` and
  `step` row to the loop definition beside this file, and its name to the roles kit's `WORKFLOW_NAMES`,
  then re-renders the README region; its gate is `check_roles.py --write`, then `loop_lib.py --check`.
- `scenario` appends one gov `[[scenario]]` row to the pack `scenarios.toml` beside this file, `activates`
  and `then` empty, each `--admit` a value its fact admits; the name `adopter` is refused, a repository
  writing its own row in its overlay by hand. Its gate is `scenario.py check`, the `kind.scenario` row's
  (TOOL-dDeclaredLoop-27).

The contract every subcommand keeps: its arguments are checked against the kind's grammar first, and one
that fails exits 2 naming it, before any write. Each path it writes, and each path the renderer it runs
writes, is held through `write_guarded`, the guarded write `policy_edit.py` beside this file carries, one
call per path, nested, the gate run as the innermost record step. A green gate prints each path written
and exits 0; a red one raises inside the innermost hold, so every held path is put back and every created
path removed, then prints the gate's output and exits 1. A kit that does not resolve exits 2 naming it. A
value the gate grades is the gate's to refuse, never checked here a second time. What the instance still
needs from its caller, as a hand-made one does: a role's agent render, a hook's wiring and its `[[hook]]`
stage row, a new key's mirror (the catalogue committed, then `policy.py mirror --write` at that HEAD), a
reader of a new key whose owner build has landed, its section of the policy reference page, the kit's
version marker, and the map.

`check-commands` reads every tracked descriptor of the command kind's population, `{prefix}/*kit.toml`, at
its working-tree bytes, and refuses a `[[command]]` row whose `verb` is not one segment of the tag grammar
or repeats in its descriptor, a row whose `run` names no file `git ls-files` holds under the descriptor's
directory, and a descriptor holding a `[[command]]` row and no string `id`. A population holding no row
prints `unarmed` and exits 0. Exit 0 green, 1 a refusal.

`--fixture --plant <case>` runs one case of `PLANTS` in a scratch clone whose HEAD commits this working
tree, the policy kit's `build_source_snapshot`, and relays what ran there with its exit. `--selftest` runs
`check-commands` over the tree, then every case over one such clone, reset before each, through
`loop_lib.run_selftest_cases`.

WHAT THIS DOES NOT CHECK: that a `run` file is executable or does what its verb says, that any harness
wires the command, and a `[[command]]` row in a descriptor outside the kind's population. Over a tree
holding no row `check-commands` prints `unarmed`, which is no coverage: its red is seen only through the
`command-hand` plant. The policy key factory's four arms do not check what the whole `policy check` leg
still does at the merge bar: the mirror against its render at HEAD (`arm_mirror_parity`), red until the
caller's mirror commit; the policy file at HEAD and the mirror at the landed revision; a reader for each
key whose owner build has landed (`arm_reader_coverage`); and the single-reader joins, the legacy homes
and the cap census, whose inputs it never writes. The wrapped gates' own limits are their headers',
unchanged.
"""
import argparse
import fnmatch
import json
import os
import pathlib
import re
import subprocess
import sys
import tomllib

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import SEG, resolve_kit_dir, run_selftest_cases  # noqa: E402

SAY = "factories"
#: A role slot, a hook or a workflow name: the shape the roles kit's slots and the hooks' file stems take.
NAME_RE = re.compile(r"[a-z][a-z0-9-]*")
EVENT_RE = re.compile(r"[A-Z][A-Za-z]*")
#: The gate each kind's row names, as the factory prints it.
GATES = {"command": "loop command conformance", "policy-key": "policy check",
         "hook": "hook destinations (every declared hook path ships)", "role": "roles catalogue",
         "workflow": "roles catalogue", "scenario": "loop scenario fixtures"}
#: The policy key factory's gate: the arms of `check_policy.py` that read the working tree's catalogue, its
#: policy file and the kit's own list, never a render at a revision (TOOL-dDeclaredLoop-6 F7).
POLICY_KEY_ARMS = ("arm_schema", "arm_shape", "arm_summaries", "arm_direction")
#: The tools and model a factory-made agent role carries until its author narrows them.
ROLE_TOOLS, ROLE_MODEL = "Read, Grep, Glob, Bash", "inherit"
PLANTS = {
    "command-new": "core.py new command check --kit loop --run loop_lib.py, then check-commands",
    "command-hand": "a hand [[command]] row in the loop kit's descriptor whose run names no file",
    "policy-key-new": "core.py new policy-key fixture.knob --owner dDeclaredLoop, its gate the four POLICY_KEY_ARMS",
    "policy-key-hand": "a hand [[key]] row with no owner, under the four POLICY_KEY_ARMS",
    "hook-new": "core.py new hook fixture-hook --kit agent-cap --event Stop, its gate under a throwaway index",
    "hook-hand": "a hand fragment, staged, naming a path no [[files]] rule ships",
    "role-new": "core.py new role gov-fixture --workflow build --writes none, then check_roles.py",
    "role-hand": "a hand role file missing writes",
    "workflow-new": "core.py new workflow fixture --driver program --harness none, then check_roles.py and loop_lib.py --check",
    "workflow-hand": "a hand [[workflow]] row listing a slot with no role file",
    "factory-restores": "core.py new policy-key fixture.bad whose --default its --allowed refuses",
    "factory-restores-create": "core.py new hook fixture-hook over a committed hand fragment that holds its gate red",
    "scenario-new": "core.py new scenario trial --extends scenario.feature --admit entry=trial, then scenario.py check",
    "scenario-hand": "a hand [[scenario]] row in gov's pack whose entry names no step",
    "factory-interrupt": "the role kind's writes in process, KeyboardInterrupt raised at the second held path's "
                         "rename, then a stray temp planted beside a held path",
}
#: The register's factory verb each `-new` case and `factory-restores` runs, after `core.py new`.
NEW_ARGV = {
    "command-new": ["command", "check", "--kit", "loop", "--run", "loop_lib.py"],
    "policy-key-new": ["policy-key", "fixture.knob", "--allowed", '["a", "b"]', "--default", '"a"', "--summary",
                       "A fixture knob.", "--usage", 'fixture.knob = "b"', "--owner", "dDeclaredLoop"],
    "hook-new": ["hook", "fixture-hook", "--kit", "agent-cap", "--event", "Stop"],
    "role-new": ["role", "gov-fixture", "--workflow", "build", "--writes", "none", "--description",
                 "A fixture role.", "--reads", "input:question", "--returns", "a fixture answer", "--output",
                 "the answer, to its caller", "--ceiling", "1024"],
    "workflow-new": ["workflow", "fixture", "--driver", "program", "--harness", "none", "--roles", "",
                     "--enforced-by", "none — a fixture", "--trigger", "never, a fixture", "--order", "0",
                     "--step", "none"],
    "factory-restores": ["policy-key", "fixture.bad", "--allowed", '["a", "b"]', "--default", '"c"', "--summary",
                         "A fixture knob.", "--usage", 'fixture.bad = "a"', "--owner", "dDeclaredLoop"],
    "scenario-new": ["scenario", "trial", "--extends", "scenario.feature", "--admit", "entry=trial", "--entry",
                     "step.plan"],
}
NEW_ARGV["factory-restores-create"] = NEW_ARGV["hook-new"]
#: Each selftest case: the case, its owed exit, and the opening and needle of the line it owes.
CASES = (("check-commands", 0, "factories: check-commands", "descriptor(s)"),
         ("command-new", 0, "factories: fixture · command-new", "gate green"),
         ("command-hand", 1, "factories: gate", "command.loop.hand"),
         ("policy-key-new", 0, "factories: fixture · policy-key-new", "gate green"),
         ("policy-key-hand", 1, "factories: gate", "fixture.hand"),
         ("hook-new", 0, "factories: fixture · hook-new", "nothing staged · gate green"),
         ("hook-hand", 1, "factories: gate", "fixture-hand.fragment.json"),
         ("role-new", 0, "factories: fixture · role-new", "gate green"),
         ("role-hand", 1, "factories: gate", "R2"),
         ("workflow-new", 0, "factories: fixture · workflow-new", "gate green"),
         ("workflow-hand", 1, "factories: gate", "R8"),
         ("factory-restores", 1, "factories: fixture · factory-restores", "porcelain clean"),
         ("factory-restores-create", 1, "factories: fixture · factory-restores-create", "porcelain clean"),
         ("scenario-new", 0, "factories: fixture · scenario-new", "gate green"),
         ("scenario-hand", 1, "factories: gate", "step.nowhere"),
         ("factory-interrupt", 0, "factories: fixture · factory-interrupt", "leftover named"))


class Refused(Exception):
    """An argument or a kit the factory refuses before any write: exit 2."""


class KindGateRed(Exception):
    """The kind's gate exited non-zero inside the innermost hold: `lines` its output."""

    def __init__(self, lines):
        super().__init__("gate red")
        self.lines = lines


def derive_layout(here=KIT):
    """(the work tree's top above `here`, `here` relative to it): a factory writes the tree it sits in."""
    top = next((d for d in (here, *here.parents) if (d / ".git").exists()), None)
    if top is None:
        raise Refused("no work tree above %s" % here.as_posix())
    return top, here.relative_to(top).as_posix()


def read_clean_env():
    """The environment with every GIT_ variable stripped, so a hook's GIT_DIR cannot retarget a child."""
    return {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}


def run_git(top, *args):
    p = subprocess.run(["git", "-C", str(top), *args], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=read_clean_env(), stdin=subprocess.DEVNULL)
    if p.returncode:
        raise Refused("git %s exited %d: %s" % (" ".join(args), p.returncode, p.stderr.strip()[:200]))
    return p.stdout


def read_text_exact(path):
    """`path`'s text with its line endings as stored, which `read_text` would translate."""
    return pathlib.Path(path).read_bytes().decode("utf-8")


def check_one_line(flag, value):
    if not value.strip() or "\n" in value or "\r" in value:
        raise Refused("%s %r is not one non-empty line" % (flag, value))
    return value


def render_row_after(text, table, block):
    """`text` with `block` inserted after the last `[[table]]` row, before the blank lines, comments and
    header that follow it, or appended where the file holds no such row; in the file's own line ending."""
    nl = "\r\n" if "\r\n" in text else "\n"
    lines = text.replace("\r\n", "\n").splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    heads = [i for i, ln in enumerate(lines) if ln.strip() == "[[%s]]" % table]
    if not heads:
        out = "".join(lines).rstrip("\n") + "\n\n" + block
    else:
        end = next((j for j in range(heads[-1] + 1, len(lines)) if lines[j].lstrip().startswith("[")), len(lines))
        while end > heads[-1] + 1 and (not lines[end - 1].strip() or lines[end - 1].lstrip().startswith("#")):
            end -= 1
        out = "".join(lines[:end]) + "\n" + block + "".join(lines[end:])
    return out.replace("\n", nl)


def read_kit_descriptor(top, kit_rel, kid):
    """(path, data) of the one tracked descriptor of the command kind's population whose `id` is `kid`."""
    troot = pathlib.PurePosixPath(kit_rel).parent.as_posix()
    spec = "*kit.toml" if troot == "." else troot + "/*kit.toml"
    hits = []
    for rel in run_git(top, "ls-files", "--", spec).splitlines():
        try:
            data = tomllib.loads((top / rel).read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            continue
        if data.get("id") == kid:
            hits.append((top / rel, data))
    if len(hits) != 1:
        raise Refused("--kit %r names %d descriptor(s) of %s, not one" % (kid, len(hits), spec))
    return hits[0]


def derive_roles_kit(top, kit_rel):
    """The roles kit's directory in this install, its `roles_lib` imported."""
    try:
        roles = resolve_kit_dir("roles", "check_roles.py", top / kit_rel)
    except LookupError as exc:
        raise Refused(str(exc))
    if str(roles) not in sys.path:
        sys.path.insert(0, str(roles))
    import roles_lib  # noqa: F401  (the roles kit's key list, read by render_front_matter)
    return roles


def check_commands(top, kit_rel):
    """-> (lines, rc): every `[[command]]` row of the population graded both ways."""
    troot = pathlib.PurePosixPath(kit_rel).parent.as_posix()
    spec = "*kit.toml" if troot == "." else troot + "/*kit.toml"
    paths = run_git(top, "ls-files", "--", spec).splitlines()
    tracked = set(run_git(top, "ls-files").splitlines())
    refusals, n_rows = [], 0
    for rel in paths:
        try:
            data = tomllib.loads((top / rel).read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            refusals.append("%s does not read as TOML: %s" % (rel, exc))
            continue
        rows = data.get("command") or []
        if not rows:
            continue
        kid = data.get("id")
        if not isinstance(kid, str) or not kid:
            refusals.append("%s holds %d [[command]] row(s) and no string id, so the command namespace yields "
                            "none of them" % (rel, len(rows)))
            kid = "?"
        home, seen = pathlib.PurePosixPath(rel).parent, set()
        for row in rows:
            n_rows += 1
            verb, run = row.get("verb"), row.get("run")
            tag = "command.%s.%s" % (kid, verb)
            if not isinstance(verb, str) or not SEG.fullmatch(verb):
                refusals.append("%s %s: its verb %r is not one segment of the tag grammar" % (rel, tag, verb))
            elif verb in seen:
                refusals.append("%s %s: its verb repeats in the descriptor" % (rel, tag))
            seen.add(verb)
            target = (home / run).as_posix() if isinstance(run, str) and run else None
            if target is None or target not in tracked:
                refusals.append("%s %s: its run %r names no file git holds under %s" % (rel, tag, run, home.as_posix()))
    if refusals:
        return (["%s: check-commands · red · %d finding(s)" % (SAY, len(refusals))]
                + ["%s: refused · %s" % (SAY, r) for r in refusals]), 1
    if not n_rows:
        return ["%s: check-commands · unarmed · no [[command]] row in %d descriptor(s)" % (SAY, len(paths))], 0
    return ["%s: check-commands · green · %d row(s) over %d descriptor(s)" % (SAY, n_rows, len(paths))], 0


def run_policy_key_arms(top, kit_rel):
    """-> (rc, lines): each of `POLICY_KEY_ARMS` run in process over the tree at `top` and its policy kit,
    printed as `check_policy.py`'s own main prints an arm; any finding is the red."""
    try:
        from floor import read_policy_modules
        read_policy_modules()
        kit = resolve_kit_dir("policy", "check_policy.py", top / kit_rel)
    except LookupError as exc:
        raise Refused(str(exc))
    import check_policy
    lines, red = [], 0
    for name in POLICY_KEY_ARMS:
        verdict, findings = check_policy.run_arm(check_policy.ARM[name], str(top), kit)
        lines.append("policy-check: %s · %s" % (name, verdict))
        lines += ["  %s: %s" % (key, why) for key, why in findings]
        red += len(findings)
    return (1 if red else 0), lines


def run_hook_gate(argv, top, written):
    """-> (rc, lines) of the hook gate's `argv` with `GIT_INDEX_FILE` naming a copy of the caller's index,
    in a temporary directory, into which `git add` has put `written`: the gate grades tracked fragments
    only, so the copy holds the new one, and the caller's index is never written. The directory is removed
    on the way out, green or red."""
    import shutil
    import tempfile
    own = pathlib.Path(run_git(top, "rev-parse", "--git-path", "index").strip())
    own = own if own.is_absolute() else top / own
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="factory-index-"))
    try:
        index = scratch / "index"
        if own.is_file():
            shutil.copyfile(own, index)
        env = {**read_clean_env(), "GIT_INDEX_FILE": str(index)}
        rels = [p.relative_to(top).as_posix() for p in written]
        p = subprocess.run(["git", "-C", str(top), "add", "--", *rels], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env, stdin=subprocess.DEVNULL)
        if p.returncode:
            return p.returncode, ["git add into the gate's index exited %d: %s" % (p.returncode, p.stderr.strip()[:200])]
        p = subprocess.run(argv, cwd=str(top), capture_output=True, text=True, encoding="utf-8", errors="replace",
                           env=env, stdin=subprocess.DEVNULL)
        return p.returncode, (p.stdout + p.stderr).splitlines()
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


def run_kind_gate(kind, top, kit_rel, render=False, written=()):
    """-> (rc, lines) of `kind`'s gate over the tree at `top`; `render` runs the roles README render first,
    which grades as it writes; `written`, the hook factory's files, are put into the hook gate's throwaway
    index. A kit that does not resolve raises Refused."""
    if kind == "command":
        lines, rc = check_commands(top, kit_rel)
        return rc, lines
    if kind == "policy-key":
        return run_policy_key_arms(top, kit_rel)
    here = top / kit_rel
    try:
        if kind == "scenario":
            argvs = [[sys.executable, str(here / "scenario.py"), "check"]]
        elif kind == "hook":
            from loop_witness import resolve_bash
            gate = resolve_kit_dir(".", "check-hook-destinations.sh", here) / "check-hook-destinations.sh"
            bash = resolve_bash(gate.as_posix())
            if not bash:
                raise Refused(f"no bash can see {gate.as_posix()}; set GOV_BASH to Git's bash")
            argv = [bash, gate.as_posix()]
            if written:
                return run_hook_gate(argv, top, written)
            argvs = [argv]
        else:
            roles = resolve_kit_dir("roles", "check_roles.py", here) / "check_roles.py"
            argvs = [[sys.executable, str(roles), *(["--write"] if render else [])]]
            if kind == "workflow":
                argvs.append([sys.executable, str(here / "loop_lib.py"), "--check"])
    except LookupError as exc:
        raise Refused(str(exc))
    lines = []
    for argv in argvs:
        p = subprocess.run(argv, cwd=str(top), capture_output=True, text=True, encoding="utf-8", errors="replace",
                           env=read_clean_env(), stdin=subprocess.DEVNULL)
        lines += (p.stdout + p.stderr).splitlines()
        if p.returncode:
            return p.returncode, lines
    return 0, lines


def read_leftover_temps(paths):
    """Each sibling temp `<name>.*.tmp` beside a path of `paths`, the guarded write's own temp shape, that
    an interrupted write left behind, in path order."""
    return [tmp for path in paths for tmp in sorted(path.parent.glob(path.name + ".*.tmp"))]


def write_kind_instance(kind, name, top, kit_rel, writes, render=None):
    """Each `(path, text)` of `writes` held through the guarded write, nested, with `render`, a path the
    renderer writes, held at its own bytes, and the kind's gate run innermost: -> the exit. Before the
    first write, each leftover temp beside a held path is named on one `leftover` line, and the write goes
    on (TOOL-dDeclaredLoop-67 S38)."""
    from policy_edit import write_guarded
    held = list(writes) + ([(render, lambda _tmp: None)] if render else [])
    before = {p: (p.read_bytes() if p.is_file() else None) for p, _t in held}
    for tmp in read_leftover_temps([p for p, _t in held]):
        print("%s: leftover · %s" % (SAY, tmp.relative_to(top).as_posix()))

    def write_held(rest):
        if not rest:
            rc, lines = run_kind_gate(kind, top, kit_rel, render is not None,
                                      [p for p, _t in writes] if kind == "hook" else ())
            if rc:
                raise KindGateRed(lines)
            return lines
        path, text = rest[0]
        return write_guarded(path, text, lambda: write_held(rest[1:]))

    try:
        said = write_held(held)
    except KindGateRed as red:
        print("%s: new %s %s · gate %s red · every held path put back" % (SAY, kind, name, GATES[kind]))
        for line in red.lines:
            print("%s: gate · %s" % (SAY, line))
        return 1
    print("%s: new %s %s · gate %s green" % (SAY, kind, name, GATES[kind]))
    for line in said:
        print("%s: gate · %s" % (SAY, line))
    for path, _t in held:
        if not path.is_file() or path.read_bytes() != before[path]:
            print("%s: wrote %s" % (SAY, path.relative_to(top).as_posix()))
    return 0


def write_command(top, kit_rel, verb, kit, run):
    if not SEG.fullmatch(verb):
        raise Refused("the verb %r is not one segment of the tag grammar" % verb)
    check_one_line("--run", run)
    if run.startswith(("/", "\\")) or ".." in pathlib.PurePosixPath(run).parts or "\\" in run or ":" in run:
        raise Refused("--run %r is not a path relative to the descriptor's directory" % run)
    path, _data = read_kit_descriptor(top, kit_rel, kit)
    block = "[[command]]\nverb = %s\nrun = %s\n" % (json.dumps(verb), json.dumps(run, ensure_ascii=False))
    return write_kind_instance("command", verb, top, kit_rel,
                               [(path, render_row_after(read_text_exact(path), "command", block))])


def write_policy_key(top, kit_rel, name, allowed, default, summary, usage, owner):
    if not re.fullmatch(r"%s(?:\.%s)*" % (SEG.pattern, SEG.pattern), name):
        raise Refused("the key %r is not dotted segments of the tag grammar" % name)
    for flag, text in (("--allowed", allowed), ("--default", default)):
        check_one_line(flag, text)
        try:
            tomllib.loads("v = " + text)
        except tomllib.TOMLDecodeError as exc:
            raise Refused("%s %r is not one TOML value: %s" % (flag, text, exc))
    for flag, text in (("--summary", summary), ("--usage", usage), ("--owner", owner)):
        check_one_line(flag, text)
    try:
        path = resolve_kit_dir("policy", "catalogue.toml", top / kit_rel) / "catalogue.toml"
    except LookupError as exc:
        raise Refused(str(exc))
    block = "[[key]]\nname = %s\nallowed = %s\ndefault = %s\nsummary = %s\nusage = %s\nowner = %s\n" % (
        json.dumps(name), allowed, default, *(json.dumps(t, ensure_ascii=False) for t in (summary, usage, owner)))
    return write_kind_instance("policy-key", name, top, kit_rel,
                               [(path, render_row_after(read_text_exact(path), "key", block))])


def write_hook(top, kit_rel, name, kit, event, matcher):
    if not NAME_RE.fullmatch(name):
        raise Refused("the hook name %r is not %s" % (name, NAME_RE.pattern))
    if not EVENT_RE.fullmatch(event):
        raise Refused("--event %r is not a hook event's name, %s" % (event, EVENT_RE.pattern))
    check_one_line("--matcher", matcher)
    desc, data = read_kit_descriptor(top, kit_rel, kit)
    troot = (top / kit_rel).parent
    home = desc.parent.relative_to(troot).as_posix()
    script, fragment = desc.parent / ("%s.js" % name), desc.parent / ("%s.fragment.json" % name)
    for p in (script, fragment):
        if p.exists():
            raise Refused("%s exists; the factory writes a new hook" % p.relative_to(top).as_posix())
    frag = {"name": name, "event": event, "matcher": matcher, "marker": script.name,
            "hook_path": "{kit}/%s/%s" % (home, script.name)}
    includes = [pat for row in data.get("files") or [] for pat in (row.get("include") or [])]
    text = read_text_exact(desc)
    for f in (script.name, fragment.name):
        if not any(fnmatch.fnmatchcase(f, pat) for pat in includes):
            text = render_row_after(text, "files", '[[files]]\ninclude = [%s]\nrole = "engine"\nto = "{prefix}/%s/%s"\n'
                                    % (json.dumps(f), home, f))
    body = ("#!/usr/bin/env node\n// %s.js — a %s hook the hook kind's factory wrote; what it checks is its author's"
            " to write.\nprocess.exit(0);\n" % (name, event))
    return write_kind_instance("hook", name, top, kit_rel,
                               [(script, body), (fragment, json.dumps(frag, indent=2) + "\n"), (desc, text)])


def write_scenario(top, kit_rel, name, extends, admits, entry):
    """TOOL-dDeclaredLoop-27 S11: one gov `[[scenario]]` row appended to the pack beside this file, `activates`
    and `then` empty, its gate `scenario.py check`. A name that is not one tag segment or is `adopter`, a
    tag the pack holds and an `--admit` not shaped `<fact>=<value>` are refused before any write; a
    repository writes its own row in its overlay by hand."""
    if not SEG.fullmatch(name) or name == "adopter":
        raise Refused("the name %r is not one tag segment other than adopter, the repository's seat" % name)
    path = top / kit_rel / "scenarios.toml"
    text = read_text_exact(path)
    tag = "scenario.%s" % name
    if any(r.get("tag") == tag for r in tomllib.loads(text).get("scenario", [])):
        raise Refused("%s is a tag the pack already holds" % tag)
    table = {}
    for pair in admits:
        fact, eq, value = pair.partition("=")
        if not (SEG.fullmatch(fact) and eq and value.strip()):
            raise Refused("--admit %r is not <fact>=<value>" % pair)
        table.setdefault(fact, []).append(check_one_line("--admit", value))
    lines = ["[[scenario]]", "tag = %s" % json.dumps(tag), "extends = %s" % json.dumps(check_one_line("--extends", extends)),
             "admits = { %s }" % ", ".join("%s = %s" % (json.dumps(k), json.dumps(v, ensure_ascii=False))
                                          for k, v in table.items()),
             "entry = %s" % json.dumps(check_one_line("--entry", entry)), "activates = {}", "then = []", ""]
    return write_kind_instance("scenario", name, top, kit_rel,
                               [(path, render_row_after(text, "scenario", chr(10).join(lines)))])


def render_front_matter(keys, values):
    """A role file's front matter, its lines in the roles kit's key order."""
    return "---\n" + "".join("%s: %s\n" % (k, values[k]) for k in keys if k in values) + "---\n"


def render_closed_set(text, anchor, close, insert):
    """`text` with `insert` placed before the first `close` after `anchor`, which must occur exactly once."""
    if text.count(anchor) != 1:
        raise Refused("%r occurs %d time(s) in the roles kit's checker, not once" % (anchor, text.count(anchor)))
    at = text.find(close, text.index(anchor))
    if at < 0:
        raise Refused("%r is not closed by %r in the roles kit's checker" % (anchor, close))
    return text[:at] + insert + text[at:]


def write_workflow_roles(text, workflow, slot):
    """workflows.toml's `text` with `slot` added to the `roles` of the row named `workflow`."""
    lines = text.splitlines(keepends=True)
    heads = [i for i, ln in enumerate(lines) if ln.strip() == "[[workflow]]"] + [len(lines)]
    for a, b in zip(heads, heads[1:]):
        block = lines[a:b]
        if not any(re.fullmatch(r"name\s*=\s*%s\s*" % re.escape(json.dumps(workflow)), ln.strip()) for ln in block):
            continue
        for k, ln in enumerate(block):
            m = re.fullmatch(r"(roles\s*=\s*\[)(.*)(\]\s*)", ln.rstrip("\r\n"))
            if m:
                inner = m.group(2).strip()
                lines[a + k] = "%s%s%s%s%s" % (m.group(1), inner, ", " if inner else "", json.dumps(slot),
                                               m.group(3)) + ln[len(ln.rstrip("\r\n")):]
                return "".join(lines)
    raise Refused("--workflow %r names no workflows.toml row holding a one-line roles list" % workflow)


def write_role(top, kit_rel, slot, workflow, writes, description, reads, returns, output, ceiling):
    if not NAME_RE.fullmatch(slot):
        raise Refused("the slot %r is not %s" % (slot, NAME_RE.pattern))
    if ceiling <= 0:
        raise Refused("--ceiling %d is not a byte count above 0" % ceiling)
    for flag, text in (("--workflow", workflow), ("--writes", writes), ("--description", description),
                       ("--reads", reads), ("--returns", returns), ("--output", output)):
        check_one_line(flag, text)
    roles = derive_roles_kit(top, kit_rel)
    import roles_lib
    role = roles / "agents" / ("%s.agent.md" % slot)
    if role.exists():
        raise Refused("%s exists; the factory writes a new role" % role.relative_to(top).as_posix())
    table, checker = roles / "workflows.toml", roles / "check_roles.py"
    values = dict(name=slot, description=description, tools=ROLE_TOOLS, model=ROLE_MODEL, workflow=workflow,
                  reads=reads, writes=writes, rules="", returns=returns, mandatory="no", output=output)
    body = "You are the %s role of the %s workflow; what it does beyond its front matter is its author's to write.\n" % (
        slot, workflow)
    text = render_front_matter(roles_lib.FRONT_MATTER_KEYS, values).replace(": \n", ":\n") + "\n" + body
    ceilings = render_closed_set(read_text_exact(checker), "BODY_CEILINGS = {", "\n}",
                                 "\n    %s: %d," % (json.dumps(slot), ceiling))
    return write_kind_instance("role", slot, top, kit_rel, [
        (role, text), (table, write_workflow_roles(read_text_exact(table), workflow, slot)),
        (checker, ceilings)], render=roles / "README.md")


def write_workflow(top, kit_rel, name, driver, harness, roles_csv, enforced_by, trigger, order, step):
    if not NAME_RE.fullmatch(name):
        raise Refused("the workflow name %r is not %s" % (name, NAME_RE.pattern))
    for flag, text in (("--driver", driver), ("--harness", harness), ("--enforced-by", enforced_by),
                       ("--trigger", trigger), ("--step", step)):
        check_one_line(flag, text)
    slots = [s.strip() for s in roles_csv.split(",") if s.strip()]
    roles = derive_roles_kit(top, kit_rel)
    table, checker, loop = roles / "workflows.toml", roles / "check_roles.py", top / kit_rel / "loop.toml"
    by = json.dumps(enforced_by, ensure_ascii=False)
    row = "[[workflow]]\nname = %s\ndriver = %s\nharness = %s\nroles = [%s]\nenforced-by = %s\ntrigger = %s\n" % (
        json.dumps(name), json.dumps(driver), json.dumps(harness), ", ".join(json.dumps(s) for s in slots),
        by if enforced_by.startswith("none — ") else "[%s]" % by, json.dumps(trigger, ensure_ascii=False))
    placed = "[[workflow]]\nname = %s\norder = %d\nstep = %s\n" % (json.dumps(name), order, json.dumps(step))
    names = render_closed_set(read_text_exact(checker), "WORKFLOW_NAMES = (", ")", ", %s" % json.dumps(name))
    return write_kind_instance("workflow", name, top, kit_rel, [
        (table, render_row_after(read_text_exact(table), "workflow", row)),
        (loop, render_row_after(read_text_exact(loop), "workflow", placed)),
        (checker, names)], render=roles / "README.md")


# ------------------------------------------------------------------------------------------- the fixture
def build_fixture_base(top, kit_rel):
    """(clone, sha): the policy kit's snapshot clone of this working tree and its HEAD."""
    sys.path.insert(0, str(resolve_kit_dir("policy", "check_policy.py", top / kit_rel)))
    import check_policy
    clone = check_policy.build_source_snapshot(top)
    return clone, run_git(clone, "rev-parse", "HEAD").strip()


def run_core_new(clone, kit_rel, argv):
    """`core.py new <argv>` in the clone, the register's factory verb: -> (rc, lines)."""
    core = resolve_kit_dir("playbook", "core.py", clone / kit_rel) / "core.py"
    p = subprocess.run([sys.executable, str(core), "new", *argv], cwd=str(clone), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=read_clean_env(), stdin=subprocess.DEVNULL)
    return p.returncode, (p.stdout + p.stderr).splitlines()


def write_hand_plant(clone, kit_rel, case):
    """The hand-made non-conforming instance of `case`'s kind, written in the clone and staged."""
    here = clone / kit_rel
    if case == "command-hand":
        p = here / "kit.toml"
        text = render_row_after(read_text_exact(p), "command", '[[command]]\nverb = "hand"\nrun = "no-such-file.py"\n')
    elif case == "policy-key-hand":
        p = resolve_kit_dir("policy", "catalogue.toml", here) / "catalogue.toml"
        text = render_row_after(read_text_exact(p), "key", '[[key]]\nname = "fixture.hand"\nallowed = ["a", "b"]\n'
                                'default = "a"\nsummary = "A hand knob."\nusage = \'fixture.hand = "b"\'\n')
    elif case == "hook-hand":
        home = resolve_kit_dir("hooks", "agent-cap.js", here)
        p = home / "fixture-hand.fragment.json"
        text = json.dumps({"name": "fixture-hand", "event": "Stop", "matcher": "*", "marker": "fixture-hand.js",
                           "hook_path": "{kit}/%s/fixture-hand.js" % home.relative_to(here.parent).as_posix()},
                          indent=2) + "\n"
    elif case == "role-hand":
        p = resolve_kit_dir("roles", "check_roles.py", here) / "agents" / "gov-hand.agent.md"
        text = ("---\nname: gov-hand\ndescription: A hand role.\ntools: Read\nmodel: inherit\nworkflow: build\n"
                "reads: input:question\nrules:\nreturns: x\nmandatory: no\noutput: x\n---\n\nA hand body.\n")
    elif case == "scenario-hand":
        p = here / "scenarios.toml"
        row = ['[[scenario]]', 'tag = "scenario.hand"', 'extends = "none"', 'admits = { entry = ["hand"] }',
               'entry = "step.nowhere"', 'activates = {}', 'then = []', '']
        text = render_row_after(read_text_exact(p), "scenario", chr(10).join(row))
    else:
        p = resolve_kit_dir("roles", "check_roles.py", here) / "workflows.toml"
        text = render_row_after(read_text_exact(p), "workflow", '[[workflow]]\nname = "handoff-hand"\n'
                                'driver = "program"\nharness = "none"\nroles = ["gov-nobody"]\n'
                                'enforced-by = "none — a hand row"\ntrigger = "never"\n')
    p.write_bytes(text.encode("utf-8"))
    run_git(clone, "add", "-A")


def run_fixture(case, base, kit_rel):
    """One plant over the clone `base`, `(clone, sha)`, reset to its commit first: -> the exit."""
    from loop_witness import run_fixture_git
    clone, sha = base
    run_fixture_git(clone, "reset", "-q", "--hard", sha)
    run_fixture_git(clone, "clean", "-qfdx")
    print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
    kind = case.rsplit("-", 1)[0] if case != "factory-restores" else "policy-key"
    if case.endswith("-hand"):
        write_hand_plant(clone, kit_rel, case)
        rc, lines = run_kind_gate(kind, clone, kit_rel)
        for line in lines:
            print("%s: gate · %s" % (SAY, line))
        print("%s: fixture · %s · gate %s exit %d" % (SAY, case, GATES[kind], rc))
        return rc
    if case == "factory-interrupt":
        return run_interrupt_plant(clone, kit_rel)
    created = []
    if case == "factory-restores-create":  # TOOL-dDeclaredLoop-56 S37: a gate red before the factory writes
        write_hand_plant(clone, kit_rel, "hook-hand")
        run_fixture_git(clone, "commit", "-q", "--no-verify", "-m", "a hand fragment the hook gate refuses")
        home = resolve_kit_dir("hooks", "agent-cap.js", clone / kit_rel)
        created = [home / "fixture-hook.js", home / "fixture-hook.fragment.json"]
    rc, lines = run_core_new(clone, kit_rel, NEW_ARGV[case])
    for line in lines:
        print("    " + line)
    dirty = [ln[3:] for ln in run_git(clone, "status", "--porcelain").splitlines()]
    arms = read_arm_findings(lines)
    if case == "factory-restores-create":
        left = [p.relative_to(clone).as_posix() for p in created if p.exists()]
        why = ("the factory exited %d, not 1" % rc if rc != 1 else
               "%s on disk" % ", ".join(left) if left else
               "porcelain holds %s" % "; ".join(dirty) if dirty else
               "no gate line names fixture-hand.fragment.json" if not any(
                   "fixture-hand.fragment.json" in ln for ln in lines) else "")
        print("%s: fixture · %s · factory exit %d · %s" % (SAY, case, rc, "FAIL, " + why if why else
                                                           "no created file on disk · porcelain clean"))
        return rc if not why else 3
    if case == "factory-restores":
        why = ("porcelain holds %s" % "; ".join(dirty) if dirty else
               "no arm_shape finding names fixture.bad" if not any("fixture.bad" in f for f in arms.get("arm_shape", ())) else
               "arm_mirror_parity ran" if "arm_mirror_parity" in arms else "")
        print("%s: fixture · %s · factory exit %d · %s" % (SAY, case, rc, "FAIL, " + why if why else "porcelain clean"))
        return rc if not why else 3
    if rc:
        print("%s: fixture · %s · FAIL · the factory exited %d" % (SAY, case, rc))
        return rc
    why = ""
    if case == "policy-key-new":
        cat = (resolve_kit_dir("policy", "catalogue.toml", clone / kit_rel) / "catalogue.toml").relative_to(clone).as_posix()
        why = ("the gate ran %s, not the four arms" % sorted(arms) if sorted(arms) != sorted(POLICY_KEY_ARMS) else
               "porcelain holds %s, not %s alone" % (dirty, cat) if dirty != [cat] else "")
    elif case == "scenario-new":
        rows = tomllib.loads((clone / kit_rel / "scenarios.toml").read_text(encoding="utf-8")).get("scenario", [])
        row = next((r for r in rows if r.get("tag") == "scenario.trial"), None)
        lack = [k for k in ("extends", "admits", "entry", "activates", "then") if k not in (row or {})]
        why = "the pack holds no scenario.trial" if row is None else "scenario.trial lacks %s" % lack if lack else ""
    elif case == "hook-new":
        staged = run_git(clone, "diff", "--cached", "--name-only").split()
        why = ("the index holds %s" % staged if staged else
               "no hook-dest: ok line names fixture-hook.fragment.json" if not any(
                   "hook-dest: ok" in ln and "fixture-hook.fragment.json" in ln for ln in lines) else "")
        print("%s: fixture · %s · %s" % (SAY, case, "FAIL, " + why if why else "nothing staged · gate green"))
        return 3 if why else 0
    print("%s: fixture · %s · factory exit 0 · %s" % (SAY, case, "FAIL, " + why if why else "gate green"))
    return 3 if why else 0


def run_interrupt_plant(clone, kit_rel):
    """`factory-interrupt` (TOOL-dDeclaredLoop-67 AC26): the role kind's writes in process over the clone,
    the loop kit's `policy_edit.os.replace` spied to raise KeyboardInterrupt at the second held path's
    rename, as guard.py's `write-guarded-rollback` spies it; every held path then reads its prior bytes,
    the created path is absent and the porcelain is clean. A stray temp planted beside a held path is then
    named on a `leftover` line by the same writes, interrupted alike: -> 0 held, 3 missed."""
    import contextlib
    import io
    import unittest.mock
    import policy_edit
    roles = derive_roles_kit(clone, kit_rel)
    role = roles / "agents" / "gov-fixture.agent.md"
    held = [roles / "workflows.toml", roles / "check_roles.py", roles / "README.md"]
    before = {path: path.read_bytes() for path in held}
    real_replace = policy_edit.os.replace
    args = (clone, kit_rel, "gov-fixture", "build", "none", "A fixture role.", "input:question", "a fixture answer",
            "the answer, to its caller", 1024)

    def run_interrupted():
        """The role kind's writes, interrupted at the second rename onto a held or created path: its output."""
        renamed = []

        def run_replace(src, dst):
            if pathlib.Path(dst) in [role] + held:
                renamed.append(dst)
                if len(renamed) == 2:
                    raise KeyboardInterrupt
            return real_replace(src, dst)
        out = io.StringIO()
        with unittest.mock.patch.object(policy_edit.os, "replace", run_replace), contextlib.redirect_stdout(out):
            try:
                write_role(*args)
                said = "no interrupt"
            except KeyboardInterrupt:
                said = "interrupted"
        print(out.getvalue().rstrip())
        return said, out.getvalue()

    misses = []
    said, _out = run_interrupted()
    moved = [p.relative_to(clone).as_posix() for p in held if p.read_bytes() != before[p]]
    dirty = run_git(clone, "status", "--porcelain").splitlines()
    print("%s: fixture · factory-interrupt · %s · %d held path(s) moved · %s · porcelain %s" % (
        SAY, said, len(moved), "created path present" if role.exists() else "created path absent",
        "clean" if not dirty else "; ".join(dirty)))
    if said != "interrupted" or moved or role.exists() or dirty:
        misses.append("the interrupt left %s, moved %s, the role %s, porcelain %s" % (
            said, moved, "present" if role.exists() else "absent", dirty))
    stray = held[0].with_name(held[0].name + ".fx-stray.tmp")
    stray.write_bytes(b"a stray temp\n")
    try:
        said, out = run_interrupted()
        named = "%s: leftover · %s" % (SAY, stray.relative_to(clone).as_posix()) in out.splitlines()
    finally:
        stray.unlink(missing_ok=True)
    if not named:
        misses.append("no leftover line named %s" % stray.relative_to(clone).as_posix())
    print("%s: fixture · factory-interrupt · %s" % (SAY, "FAIL, " + "; ".join(misses) if misses else
                                                    "held paths at prior bytes · porcelain clean · leftover named"))
    return 3 if misses else 0


def read_arm_findings(lines):
    """{arm: [finding line, ...]} of each `policy-check: <arm> ·` line in `lines` and the findings below it."""
    arms, arm = {}, None
    for ln in lines:
        m = re.search(r"policy-check: (arm_\w+) ·", ln)
        if m:
            arm = m.group(1)
            arms.setdefault(arm, [])
        elif arm and re.search(r"gate ·   \S", ln):
            arms[arm].append(ln)
    return arms


def run_selftest(top, kit_rel):
    """`check-commands` over the tree, then every plant over one clone: -> 0 when every case holds."""
    try:
        base = build_fixture_base(top, kit_rel)
    except (LookupError, OSError, RuntimeError, Refused) as exc:
        print("%s: selftest · UNARMED · the scratch clone could not be built: %s" % (SAY, exc))
        return 2
    import check_policy
    try:
        def run_case(argv):
            if argv == ["check-commands"]:
                lines, rc = check_commands(top, kit_rel)
                print("\n".join(lines))
                return rc
            return run_fixture(argv[2], base, kit_rel)
        cases = [(case, ["check-commands"] if case == "check-commands" else ["--fixture", "--plant", case], owed,
                  opening, needle) for case, owed, opening, needle in CASES]
        return run_selftest_cases(run_case, cases, "%s: selftest" % SAY)
    finally:
        check_policy.remove_repo(base[0])


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:
        top, kit_rel = derive_layout()
        if argv == ["check-commands"]:
            lines, rc = check_commands(top, kit_rel)
            print("\n".join(lines))
            return rc
        if argv == ["--selftest"]:
            return run_selftest(top, kit_rel)
        if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
            try:
                base = build_fixture_base(top, kit_rel)
            except (LookupError, OSError, RuntimeError) as exc:
                print("%s: fixture · UNARMED · the scratch clone could not be built: %s" % (SAY, exc))
                return 2
            import check_policy
            try:
                return run_fixture(argv[2], base, kit_rel)
            finally:
                check_policy.remove_repo(base[0])
        ap = argparse.ArgumentParser(prog="factories.py", epilog="--fixture --plant <%s> | --selftest | check-commands"
                                     % "|".join(PLANTS))
        sub = ap.add_subparsers(dest="kind", required=True)
        for kind, pos, flags in (
                ("command", "verb", ("--kit", "--run")),
                ("policy-key", "name", ("--allowed", "--default", "--summary", "--usage", "--owner")),
                ("hook", "name", ("--kit", "--event")),
                ("role", "slot", ("--workflow", "--writes", "--description", "--reads", "--returns", "--output")),
                ("workflow", "name", ("--driver", "--harness", "--roles", "--enforced-by", "--trigger", "--step")),
                ("scenario", "name", ("--extends", "--entry"))):
            sp = sub.add_parser(kind)
            sp.add_argument(pos)
            for f in flags:
                sp.add_argument(f, required=True)
            if kind == "hook":
                sp.add_argument("--matcher", default="*")
            if kind == "role":
                sp.add_argument("--ceiling", required=True, type=int)
            if kind == "workflow":
                sp.add_argument("--order", required=True, type=int)
            if kind == "scenario":
                sp.add_argument("--admit", required=True, action="append")
        a = ap.parse_args(argv)
        if a.kind == "command":
            return write_command(top, kit_rel, a.verb, a.kit, a.run)
        if a.kind == "policy-key":
            return write_policy_key(top, kit_rel, a.name, a.allowed, a.default, a.summary, a.usage, a.owner)
        if a.kind == "hook":
            return write_hook(top, kit_rel, a.name, a.kit, a.event, a.matcher)
        if a.kind == "scenario":
            return write_scenario(top, kit_rel, a.name, a.extends, a.admit, a.entry)
        if a.kind == "role":
            return write_role(top, kit_rel, a.slot, a.workflow, a.writes, a.description, a.reads, a.returns, a.output,
                              a.ceiling)
        return write_workflow(top, kit_rel, a.name, a.driver, a.harness, a.roles, a.enforced_by, a.trigger, a.order,
                              a.step)
    except Refused as exc:
        print("%s: refused · %s · nothing written" % (SAY, exc))
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
