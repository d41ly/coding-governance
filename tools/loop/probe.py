#!/usr/bin/env python3
"""probe.py — the probe program: testing outside Test, opened, pinned, designed, run, judged and returned (TOOL-dPlacedRequest-7).

    python probe.py trigger --cause <c> --asker <item tag> --subject <text> (--build <slug> --unit <id> | --request <key>) [--at <item tag>]
    python probe.py pin --trigger <record> --sha <sha> --kind verification|reproduction|experiment --question <text> --losing <text>
    python probe.py design --probe <record> --cmd <command> --expect <exit>:<hash> [--mark "judge claimed"] [--mark visual]
    python probe.py run --probe <record>
    python probe.py judge --probe <record>
    python probe.py return --probe <record>
    python probe.py points --build <slug>
    python probe.py --fixture --plant <case>
    python probe.py --selftest

Every verb runs in the repository at the current directory and prints one `probe — ` line naming the record
and the route taken, `· to <target>`: a declared probe item, the asker named in the line, or an owner item,
`OWNER_ITEM`, the unattended driver's stand-in. A route to the probe tool's stand-in, `PROBE_STAND_IN`, is
that line: the asker is re-entered with it as its input.

THE TWO WAYS IN. `trigger` opens a probe for one of the causes the loop definition's `[[trigger-cause]]`
rows hold for the program `probe`, read by `loop_lib.read_trigger_causes`; any other cause exits 2 naming
the set. The policy keys decide whether it opens, each read through the policy kit's `resolve` at the
landed revision: `point` opens where `--at` is a member of `probe.points`, read through `composition.py`'s
`read_tag_policy` at the build's pin with `--build`, else as the key's value; `owner` opens unless
`probe.raise` is `off`; `raised` only under `roles-and-owner`; `observation` at `item.entry.place` under
`probe.observations=verify-before-place`, at `item.plan.input` under `verify-at-plan` and nowhere under
`on-request`, where the owner opens a probe with `--cause owner`; `reproduction` always. A refused cause
writes nothing and prints `probe — not opened · <key>: <why> · to <asker>`, exit 1. With `--build` and
`--unit` it writes the `probe-trigger` record through the memory-tree kit's `write_record`; `--build`
without `--unit` exits 2. With `--request <content key>` it writes `<key>.probe-trigger.md` beside the
request's local text in `<git-common-dir>/requests/`, minting no id: a request holds one entry-time probe,
so a trigger for a key whose probe is open with a new subject joins it, adding its `Subject` line and
printing `probe — joined`, and the same subject again, or a probe already returned, exits 1.

THE HEAD. `pin` reads the trigger record, resolves `--sha` to its commit (exit 2 where it names none) and
writes the `probe` record's head, `Sha`, `Kind`, `Question`, `Losing`, `Asker` and `Trigger`, before any
command runs: a build-folder record is committed alone, subject `probe pin(<asker>): <kind>`, and an
entry-time head is written as `<key>.probe.md` in the requests store, committed nowhere. A verification or
a reproduction routes to `item.probe.design`, an experiment to `item.probe.experiment`, whose stand-in
prints the owner item naming dBoundRoles and `probe.experiment.authority` with its value, the experiment
shape being unbuilt.

THE METHOD. `design` appends one `- method · <exit>:<hash> · <command>` entry, its marks trailing, to the
record's `## Method` section, the method's one writer. It refuses, exit 2 and the record's bytes unchanged,
an `--expect` outside `loop_witness.EXPECT`, a `--mark` outside the two, a command holding the field
separator ` · `, and a frozen record, one already holding a run line.

RUN, JUDGE, RETURN. `run` reads the method. An entry marked `visual` makes it run nothing and write
`Verdict: unrunnable` and `Judged: computed`, routing to `item.probe.return`. Otherwise it calls
`loop_witness.py rerun --sha <pinned>` once, one `--cmd` and `--expect` pair per entry, never a second
runner, and writes each `run · <exit> · <hash> · <command>` line; a re-run that did not run, its exit `-`,
writes nothing and exits 1. `judge` reads the re-run's per-command answers from the run lines against the
entries' predictions, as `rerun` answers them: confirmed where the exit and the hash equal the prediction,
inconclusive on a timeout, refuted otherwise. Every one confirmed is `confirmed`, any refuted is
`refuted`, otherwise `inconclusive`, written as `Verdict` with `Judged: computed`; a method holding a
`judge claimed` entry is written `Judged: claimed` with no `Verdict` and routes to
`item.probe.judge-claimed`. `return` writes `Writer: stand-in` and prints `probe — <verdict> · <record> ·
to <asker>`; a record `Judged: claimed` or `Verdict: unrunnable` routes to the owner item instead.
An experiment's record is never run: `run` prints the owner item and exits 1.

`points --build <slug>` lists `probe.points` at the build's pin and refuses, exit 1 naming the key, a member
no item of the composition declares.

`--fixture --plant <case>` runs one case of `PLANTS` in a throwaway repository under the system temp
directory, its policy file the stub each case commits and its pinned commit the fixture's HEAD, printing
one `probe: <case> · ...` line ending `held` or `MISSED`; exit 0 held, 1 missed. `--selftest` runs every
case through `loop_lib.run_selftest_cases`, the `loop probe fixtures` leg.

WHAT THIS DOES NOT CHECK: that a method's command tests what the question asks, or that its prediction was
made before the output was seen beyond the freeze at the first run line; that the asker names an item a
loop declares; that a request key names a stored request; a claimed judgment's truth, which is held as
claimed and goes to the owner, never to a gate. No probe verdict feeds a landing.
"""
import argparse
import pathlib
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import (PROBE_STAND_IN, LoopError, read_memory_tree, read_trigger_causes,  # noqa: E402
                      run_selftest_cases)
from loop_parents import read_policy_kit  # noqa: E402
from loop_witness import (EXPECT, TIMEOUT, read_clean_env, remove_tree, resolve_commit,  # noqa: E402
                          run_fixture_git, run_witness_commands, write_fixture_files)

SAY = "probe"
#: The program whose `[[trigger-cause]]` rows this tool reads, its items' tag segment.
PROGRAM = "probe"
#: The owner item a route names where a probe leaves the program for the owner: the driver's park under a
#: mandate, the owner's own turn when attended.
OWNER_ITEM = "stand-in:{prefix}/unattended/unattended.sh"
#: The position `probe.observations` admits an observation at, per value; `on-request` admits none.
OBSERVATION_AT = {"verify-before-place": "item.entry.place", "verify-at-plan": "item.plan.input"}
#: The field separator of a method entry and a run line, which a command may not hold.
SEPARATOR = " · "
#: A request's content key, the twelve hex digits request.py derives.
REQUEST_KEY = re.compile(r"[0-9a-f]{12}")
ITEM_TAG = re.compile(r"item\.[a-z0-9][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+")
#: The fixture's build, unit, asker, request key and the command its plants pin.
FX_BUILD, FX_UNIT, FX_ASKER, FX_KEY = "dExample", "TOOL-dExample-2", "item.entry.place", "3f9c2a71d0e4"
FX_CMD = "bash replay-case.sh"
PLANTS = {"trigger-causes": "a cause outside the rows, a build trigger with its unit, and one without",
          "raise-owner-only": "probe.raise=owner-only: a raised probe refused, the owner's opened",
          "raise-off": "probe.raise=off: the owner's and a raised probe refused, a reproduction opened",
          "points-unlisted": "probe.points names item.plan.input: a point at item.entry.place refused, at it opened",
          "points-undeclared": "probe.points names a tag no item declares: points refuses it naming the key",
          "observation-at-plan": "probe.observations=verify-at-plan: at item.entry.place refused, at item.plan.input "
                                 "opened",
          "observation-on-request": "probe.observations=on-request: an observation refused at both positions, the "
                                    "owner's probe opened",
          "pin": "a verification pinned and committed alone, an unresolvable sha refused, an entry-time head stored",
          "entry-time": "a request's trigger beside its text, a second subject joined, the first again refused",
          "run-judge": "a reproduction predicting the planted failure: run, judge and return confirm it",
          "run-refuted": "a reproduction whose prediction differs: refuted",
          "visual": "a method entry marked visual: nothing run, unrunnable, the owner item",
          "judge-claimed": "a method entry marked judge claimed: claimed, no verdict, item.probe.judge-claimed",
          "experiment": "an experiment pinned: item.probe.experiment and the owner item naming dBoundRoles",
          "verdict-cross": "a reproduction's record carrying measured: read refuses its Verdict",
          "design": "two entries appended, each refusal writing nothing, and a frozen record refused"}


class ProbeRefused(ValueError):
    """A verb refused: its message is the line's reason; `code` its exit."""

    def __init__(self, why, code=2):
        super().__init__(why)
        self.code = code


def read_build_records():
    """The memory-tree kit's record factory, found by `read_memory_tree`; LookupError where it does not resolve."""
    read_memory_tree("build_records.py")
    import build_records
    return build_records


def resolve_git_paths():
    """`(top level, git common dir)` of the repository at the current directory, both absolute; ProbeRefused
    where it is no repository."""
    out = []
    for flag in ("--show-toplevel", "--git-common-dir"):
        p = subprocess.run(["git", "rev-parse", "--path-format=absolute", flag], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=read_clean_env())
        if p.returncode != 0 or not p.stdout.strip():
            raise ProbeRefused("the current directory is no git repository: %s" % (p.stderr.strip() or flag))
        out.append(pathlib.Path(p.stdout.strip()))
    return out[0], out[1]


def read_probe_policy(root):
    """`{key: value}` of `probe.raise`, `probe.observations` and `probe.experiment.authority` at the landed
    revision of `root`, each read through the policy kit's `resolve` by its literal key. ProbeRefused on a
    policy refusal; LookupError where the policy kit does not resolve."""
    policy, _guard = read_policy_kit()
    try:
        return {"probe.raise": policy.resolve("probe.raise", str(root)).value,
                "probe.observations": policy.resolve("probe.observations", str(root)).value,
                "probe.experiment.authority": policy.resolve("probe.experiment.authority", str(root)).value}
    except policy.Refusal as e:
        raise ProbeRefused("the probe policy does not resolve: %s" % e) from None


def read_probe_points(root, build=None):
    """The members of `probe.points`: at `build`'s pin through `composition.py`'s `read_tag_policy`, each
    renamed tag read as its successor, or, with no build, the key's value at the landed revision. ProbeRefused
    on a policy refusal; LookupError where a kit does not resolve."""
    if build is not None:
        from composition import read_tag_policy   # it reads the composition, so here and not at the top
        try:
            return list(read_tag_policy("probe.points", root, build))
        except ValueError as e:
            raise ProbeRefused(str(e)) from None
    policy, _guard = read_policy_kit()
    try:
        return list(policy.resolve("probe.points", str(root)).value)
    except policy.Refusal as e:
        raise ProbeRefused("probe.points does not resolve: %s" % e) from None


def check_trigger_cause(cause, at, root, build):
    """None where `cause` opens a probe at `at`, else `(key, why)`, by the refusals table of the spec's
    trigger (TOOL-dPlacedRequest-7 S9). ProbeRefused for a cause no rule here reads."""
    if cause == "reproduction":
        return None
    if cause == "point":
        points = read_probe_points(root, build)
        if at in points:
            return None
        return "probe.points", "%s is no point it names: %s" % (at or "no --at", " ".join(points) or "none")
    values = read_probe_policy(root)
    if cause in ("owner", "raised"):
        value = values["probe.raise"]
        if value == "off" or (cause == "raised" and value == "owner-only"):
            return "probe.raise", "%s refuses a probe of the cause %s" % (value, cause)
        return None
    if cause == "observation":
        value = values["probe.observations"]
        admitted = OBSERVATION_AT.get(value)
        if admitted is None:
            return "probe.observations", "%s admits an observation at no position; the owner opens one with " \
                                         "--cause owner" % value
        if at != admitted:
            return "probe.observations", "%s admits an observation at %s, not at %s" % (value, admitted, at or "no --at")
        return None
    raise ProbeRefused("the cause %s has no rule in probe.py, so it opens nothing" % cause)


def check_record_value(name, value):
    """`value` held to the factory's one-line rule: ProbeRefused naming `name` where it is empty, holds a CR or
    an LF, or would read as a field."""
    if not isinstance(value, str) or not value.strip() or "\n" in value or "\r" in value \
            or read_build_records().FORGED_FIELD.match(value):
        raise ProbeRefused("%s is one non-empty line that never opens **<Word>:**" % name)


def read_record_fields(path):
    """`(text, [(key, value)])` of the record at `path`, its text with LF line ends and every `- **Key:** value`
    bullet in file order, a key given twice listed twice."""
    text = pathlib.Path(path).read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")
    field = read_build_records().FIELD
    return text, [(m.group(1), m.group(2).strip()) for ln in text.split("\n") if (m := field.match(ln))]


def write_probe_fields(path, fields=(), lines=()):
    """Each `(key, value)` of `fields` inserted as a bullet after the record's last field, then each of `lines`
    appended after one blank line, the file rewritten with LF line ends."""
    for key, value in fields:
        check_record_value(key, value)
    text, _held = read_record_fields(path)
    rows = text.rstrip("\n").split("\n")
    field = read_build_records().FIELD
    at = max((n for n, ln in enumerate(rows) if field.match(ln)), default=len(rows) - 1) + 1
    rows[at:at] = ["- **%s:** %s" % kv for kv in fields]
    if lines:
        rows += [""] + list(lines)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(rows) + "\n")


def write_request_record(path, head, fields):
    """An entry-time record at `path` in the requests store, never over one already there: `head`, then each
    `(key, value)` of `fields` as a bullet, in the record kinds' field grammar, minting no id."""
    for key, value in fields:
        check_record_value(key, value)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "x", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join([head, ""] + ["- **%s:** %s" % kv for kv in fields]) + "\n")


def resolve_probe_path(arg, root, store, kind):
    """`(path, (build, unit) or None)` of a `kind` record named `arg`: a build-folder record by the factory's
    name grammar, its build and unit, or an entry-time `<key>.<kind>.md` in the requests `store`, None.
    ProbeRefused for any other path or one that does not exist."""
    br = read_build_records()
    path = pathlib.Path(arg)
    path = (path if path.is_absolute() else pathlib.Path.cwd() / path).resolve()
    if not path.is_file():
        raise ProbeRefused("%s names no %s record" % (arg, kind))
    if path.parent == store.resolve() and re.fullmatch(r"[0-9a-f]{12}\.%s\.md" % re.escape(kind), path.name):
        return path, None
    try:
        rel = path.relative_to(root.resolve()).as_posix()
    except ValueError:
        rel = ""
    name = br.derive_record_name(kind).search(rel) if rel else None
    unit = re.match(r"\d{4}-\d{2}-\d{2}-build-(%s)-" % br.ID, path.name) if name else None
    if not unit:
        raise ProbeRefused("%s is neither a %s record of a build folder nor <key>.%s.md in %s" % (
            arg, kind, kind, store.as_posix()))
    return path, (name.group("build"), unit.group(1))


def derive_record_shown(path, root):
    """`path` as a line names it: repository-relative for a build-folder record, absolute otherwise."""
    try:
        return path.relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def read_probe_record(path, root, store):
    """`(path, shown, record)`: a probe record named `path`, `record` the factory's `read_probe` of it, its
    name rule left aside for an entry-time record. ProbeRefused for a path that is no probe record."""
    p, _owner = resolve_probe_path(path, root, store, "probe")
    text, _fields = read_record_fields(p)
    record = read_build_records().read_probe(derive_record_shown(p, root), text)
    if not all(k in record for k in ("Sha", "Kind", "Asker")):
        raise ProbeRefused("%s holds no pinned head: Sha, Kind and Asker" % path)
    return p, derive_record_shown(p, root), record


def write_probe_trigger(args, root, store):
    """The `trigger` verb: -> its exit."""
    causes = read_trigger_causes(PROGRAM)
    if args.cause not in causes:
        raise ProbeRefused("--cause %s is not one of %s, the probe program's trigger-cause rows" % (
            args.cause, " ".join(causes)))
    if (args.build is None) == (args.request is None) or (args.build is None) != (args.unit is None):
        raise ProbeRefused("trigger takes --build <slug> with --unit <id>, or --request <content key>")
    for flag, value in (("--asker", args.asker), ("--at", args.at)):
        if value is not None and not ITEM_TAG.fullmatch(value):
            raise ProbeRefused("%s %s is not an item tag" % (flag, value))
    if args.request is not None and not REQUEST_KEY.fullmatch(args.request):
        raise ProbeRefused("--request %s is not a content key, twelve hex digits" % args.request)
    check_record_value("--subject", args.subject)
    refused = check_trigger_cause(args.cause, args.at, root, args.build)
    if refused:
        print("%s — not opened · %s: %s · to %s" % (SAY, refused[0], refused[1], args.asker))
        return 1
    fields = [("Cause", args.cause), ("Asker", args.asker), ("Subject", args.subject), ("At", args.at or "none"),
              ("Key", args.request or "none")]
    if args.build is not None:
        try:
            rel = read_build_records().write_record(root, args.build, args.unit, "probe-trigger",
                                                    "%s from %s" % (args.cause, args.asker), fields)
        except ValueError as e:
            raise ProbeRefused(str(e)) from None
        print("%s — opened · %s · to item.probe.pin" % (SAY, rel))
        return 0
    path = store / ("%s.probe-trigger.md" % args.request)
    if path.is_file():
        _text, held = read_record_fields(path)
        probe = store / ("%s.probe.md" % args.request)
        if probe.is_file() and any(k == "Writer" for k, _v in read_record_fields(probe)[1]):
            print("%s — already returned · %s · a request holds one entry-time probe" % (SAY, probe.as_posix()))
            return 1
        if args.subject in [v for k, v in held if k == "Subject"]:
            print("%s — already opened · %s · the subject is the probe's already" % (SAY, path.as_posix()))
            return 1
        text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
        last = max(n for n, ln in enumerate(text.split("\n")) if ln.startswith("- **Subject:** "))
        rows = text.split("\n")
        rows.insert(last + 1, "- **Subject:** %s" % args.subject)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(rows))
        print("%s — joined · %s" % (SAY, path.as_posix()))
        return 0
    write_request_record(path, "# request %s probe-trigger — %s from %s" % (args.request, args.cause, args.asker),
                         fields)
    print("%s — opened · %s · to item.probe.pin" % (SAY, path.as_posix()))
    return 0


def write_probe_pin(args, root, store):
    """The `pin` verb: -> its exit."""
    path, owner = resolve_probe_path(args.trigger, root, store, "probe-trigger")
    _text, held = read_record_fields(path)
    asker = dict(held).get("Asker")
    if not asker:
        raise ProbeRefused("%s carries no Asker" % args.trigger)
    sha = resolve_commit(root, args.sha)
    if sha is None:
        raise ProbeRefused("--sha %s names no commit in %s" % (args.sha, root.as_posix()))
    for flag, value in (("--question", args.question), ("--losing", args.losing)):
        check_record_value(flag, value)
    trigger = path.name[:-len(".md")]
    fields = [("Sha", sha), ("Kind", args.kind), ("Question", args.question), ("Losing", args.losing),
              ("Asker", asker), ("Trigger", trigger)]
    title = "%s for %s" % (args.kind, asker)
    if owner is None:
        out = store / ("%s.probe.md" % trigger[:-len(".probe-trigger")])
        if out.exists():
            raise ProbeRefused("%s is pinned already: a request holds one entry-time probe" % out.as_posix(), 1)
        write_request_record(out, "# request %s probe — %s" % (trigger[:-len(".probe-trigger")], title), fields)
        shown = out.as_posix()
    else:
        br = read_build_records()
        folder = path.parent
        for other in folder.glob("*-probe-*.md"):
            if br.derive_record_name("probe").search(other.as_posix()) and \
                    ("Trigger", trigger) in read_record_fields(other)[1]:
                raise ProbeRefused("%s is pinned already, by %s" % (trigger, other.name), 1)
        try:
            shown = br.write_record(root, owner[0], owner[1], "probe", title, fields)
        except ValueError as e:
            raise ProbeRefused(str(e)) from None
        subject = "probe pin(%s): %s" % (asker, args.kind)
        env = read_clean_env()
        for argv in (["add", "--", shown], ["commit", "-q", "-m", subject, "--", shown]):
            p = subprocess.run(["git", "-C", str(root), *argv], capture_output=True, text=True, encoding="utf-8",
                               errors="replace", env=env)
            if p.returncode != 0:
                subprocess.run(["git", "-C", str(root), "reset", "-q", "--", shown], capture_output=True, env=env)
                (root / shown).unlink()
                raise ProbeRefused("the head was not committed, so it was removed: git %s exited %d: %s" % (
                    argv[0], p.returncode, (p.stderr or p.stdout).strip()[:300]), 1)
    if args.kind == "experiment":
        print("%s — pinned · %s · to item.probe.experiment" % (SAY, shown))
        print(read_experiment_line(shown, root))
        return 0
    print("%s — pinned · %s · to item.probe.design" % (SAY, shown))
    return 0


def read_experiment_line(shown, root):
    """The experiment stand-in's line: the owner item, naming dBoundRoles, whose experiment shape is unbuilt,
    and `probe.experiment.authority` with its value."""
    try:
        value = read_probe_policy(root)["probe.experiment.authority"]
    except (ProbeRefused, LookupError) as e:
        value = "unarmed (%s)" % e
    return ("%s — beyond-authority · %s · the experiment shape is dBoundRoles', unbuilt · "
            "probe.experiment.authority=%s · to %s" % (SAY, shown, value, OWNER_ITEM))


def write_method_entry(args, root, store):
    """The `design` verb: -> its exit."""
    path, shown, record = read_probe_record(args.probe, root, store)
    if not EXPECT.fullmatch(args.expect or ""):
        raise ProbeRefused("--expect %s is not <exit>:<hash12>, the exit an integer or timeout" % args.expect)
    if not args.cmd or not args.cmd.strip() or SEPARATOR in args.cmd or "\n" in args.cmd or "\r" in args.cmd:
        raise ProbeRefused("--cmd is one non-empty line that never holds the field separator%s" % SEPARATOR.rstrip())
    if record["runs"] or any(ln.startswith("run ·") for ln in read_record_fields(path)[0].split("\n")):
        raise ProbeRefused("%s is frozen: it holds a run line, so its method is read" % shown)
    marks = [m for m in read_build_records().METHOD_MARKS if m in (args.mark or [])]
    entry = "- method · %s · %s%s" % (args.expect, args.cmd, "".join(SEPARATOR + m for m in marks))
    if not read_build_records().METHOD_LINE.fullmatch(entry):
        raise ProbeRefused("the entry %r is not the method grammar" % entry)
    text, _fields = read_record_fields(path)
    rows = text.rstrip("\n").split("\n")
    if "## Method" not in rows:
        rows += ["", "## Method", ""]
    rows.append(entry)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(rows) + "\n")
    print("%s — designed · %s · method %d · to item.probe.run" % (SAY, shown, len(record["method"]) + 1))
    return 0


def run_probe_rerun(args, root, store):
    """The `run` verb: -> its exit."""
    path, shown, record = read_probe_record(args.probe, root, store)
    if record["runs"] or "Judged" in record:
        raise ProbeRefused("%s is run already" % shown, 1)
    if not record["method"]:
        raise ProbeRefused("%s holds no method entry to run" % shown)
    if record["Kind"] == "experiment":
        print(read_experiment_line(shown, root))
        return 1
    if any("visual" in marks for _e, _h, _c, marks in record["method"]):
        write_probe_fields(path, [("Verdict", "unrunnable"), ("Judged", "computed")])
        print("%s — unrunnable · %s · visual: the capture adapter is dWellOiledMachine's, unbuilt · to "
              "item.probe.return" % (SAY, shown))
        return 0
    argv = [sys.executable, str(KIT / "loop_witness.py"), "rerun", "--sha", record["Sha"]]
    for code, digest, command, _marks in record["method"]:
        argv += ["--cmd", command, "--expect", "%s:%s" % (code, digest)]
    try:
        p = subprocess.run(argv, cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=(TIMEOUT + 60) * len(record["method"]))
    except subprocess.TimeoutExpired:
        raise ProbeRefused("the re-run passed its bound, so nothing was written", 1) from None
    answers = [ln.split(SEPARATOR, 4) for ln in p.stdout.splitlines() if ln.startswith("loop-witness: rerun · ")]
    if len(answers) != len(record["method"]) or any(a[2] == "-" for a in answers):
        why = (p.stderr.strip().splitlines() or ["exit %d" % p.returncode])[-1]
        raise ProbeRefused("the re-run did not run, so nothing was written: %s" % why, 1)
    lines = ["run · %s · %s · %s" % (a[2], a[3], command)
             for a, (_c, _h, command, _m) in zip(answers, record["method"])]
    write_probe_fields(path, lines=lines)
    print("%s — ran · %s · %d command(s) · to item.probe.judge" % (SAY, shown, len(lines)))
    return 0


def derive_probe_verdict(method, runs):
    """The computed verdict over the method's predictions and the run lines, each pair answered as `rerun`
    answers it: `confirmed` where every one is confirmed, `refuted` where any is, else `inconclusive`."""
    answers = []
    for n, (code, digest, _command, _marks) in enumerate(method):
        ran = runs[n] if n < len(runs) else None
        if ran is None or ran[1] == "timeout":
            answers.append("inconclusive")
        else:
            answers.append("confirmed" if (ran[1], ran[2]) == (code, digest) else "refuted")
    if answers and all(a == "confirmed" for a in answers):
        return "confirmed"
    return "refuted" if "refuted" in answers else "inconclusive"


def write_probe_verdict(args, root, store):
    """The `judge` verb: -> its exit."""
    path, shown, record = read_probe_record(args.probe, root, store)
    if "Judged" in record:
        raise ProbeRefused("%s is judged already" % shown, 1)
    if not record["runs"]:
        raise ProbeRefused("%s holds no run line to judge" % shown)
    if any("judge claimed" in marks for _e, _h, _c, marks in record["method"]):
        write_probe_fields(path, [("Judged", "claimed")])
        print("%s — claimed · %s · to item.probe.judge-claimed" % (SAY, shown))
        return 0
    verdict = derive_probe_verdict(record["method"], record["runs"])
    write_probe_fields(path, [("Verdict", verdict), ("Judged", "computed")])
    print("%s — judged · %s · %s · to item.probe.return" % (SAY, verdict, shown))
    return 0


def write_probe_return(args, root, store):
    """The `return` verb: -> its exit."""
    path, shown, record = read_probe_record(args.probe, root, store)
    if "Judged" not in record:
        raise ProbeRefused("%s is not judged, so there is nothing to return" % shown)
    if "Writer" in record:
        raise ProbeRefused("%s is returned already" % shown, 1)
    write_probe_fields(path, [("Writer", "stand-in")])
    if record["Judged"] == "claimed" or record.get("Verdict") == "unrunnable":
        word = "claimed" if record["Judged"] == "claimed" else "unrunnable"
        print("%s — %s · %s · to %s · in the place of %s" % (SAY, word, shown, OWNER_ITEM, record["Asker"]))
        return 0
    print("%s — %s · %s · to %s" % (SAY, record["Verdict"], shown, record["Asker"]))
    return 0


def check_probe_points(args, root):
    """The `points` verb: -> its exit."""
    from loop_items import read_composed_items   # it reads the composition, so here and not at the top
    points = read_probe_points(root, args.build)
    try:
        tags = {r.get("tag") for r in read_composed_items(root)}
    except (ValueError, LoopError) as e:
        raise ProbeRefused(str(e)) from None
    print("%s — points · %s · %s" % (SAY, args.build, " ".join(points) or "none"))
    undeclared = [t for t in points if t not in tags]
    for tag in undeclared:
        print("%s — refused · probe.points: %s is no item the loop definition declares" % (SAY, tag))
    return 1 if undeclared else 0


# ------------------------------------------------------------------------------------------ the plants
def write_probe_fixture(policy, kits=False):
    """A throwaway repository under the system temp directory, its branch `main` holding the build `FX_BUILD`
    and its unit's spec, the planted failing command `replay-case.sh` and the stub policy file `policy`,
    committed, so its HEAD is the commit a probe pins. With `kits` it starts from `loop_items.py`'s
    `build_scratch_tree`, the kits a composition read resolves at the repository copied in. The directory is
    removed on any failure."""
    if kits:
        from loop_items import build_scratch_tree   # it copies the kits, so here and only for the plant that reads them
        root = build_scratch_tree()[0]
    else:
        root = pathlib.Path(tempfile.mkdtemp(prefix="pb-"))
    try:
        if not kits:
            run_fixture_git(root, "init", "-q", "--template=")
            run_fixture_git(root, "symbolic-ref", "HEAD", "refs/heads/main")
        for key, value in (("user.name", "fx"), ("user.email", "fx@example.invalid"), ("commit.gpgsign", "false"),
                           ("core.autocrlf", "false")):
            run_fixture_git(root, "config", key, value)
        write_fixture_files(root, {
            ".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tool:TOOL"\n',
            "memory/builds/%s/spec/2026-01-01-spec-%s.md" % (FX_BUILD, FX_UNIT):
                "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01 · node a · Tier-2 · base 0123abcd\n" % FX_UNIT,
            "replay-case.sh": 'echo "the card drops its route after a compaction"\nexit 1\n',
            ".governance/policy.toml": policy})
        run_fixture_git(root, "add", "-A")
        run_fixture_git(root, "commit", "-q", "-m", "the probe fixture")
        run_fixture_git(root, "branch", "-M", "main")
        return root
    except BaseException:
        remove_tree(root)
        raise


def run_probe_command(root, *argv):
    """This script as a process in `root`: `(exit, stdout and stderr)`."""
    p = subprocess.run([sys.executable, str(pathlib.Path(__file__).absolute()), *argv], cwd=root,
                       capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env=dict(read_clean_env(), PYTHONIOENCODING="utf-8"))
    return p.returncode, (p.stdout + p.stderr).strip()


def run_probe_git(root, *argv):
    """A read-only git command in the fixture: its stdout stripped."""
    return run_fixture_git(root, *argv)


def run_probe_plant(case):
    """One case of `PLANTS`: its `probe: <case> · ...` line, and 0 when it held, 1 when it missed."""
    policy = {"raise-owner-only": '[probe]\nraise = "owner-only"\n', "raise-off": '[probe]\nraise = "off"\n',
              "points-unlisted": '[probe]\npoints = ["item.plan.input"]\n',
              "points-undeclared": '[probe]\npoints = ["item.plan.input", "item.plan.nope"]\n',
              "observation-at-plan": '[probe]\nobservations = "verify-at-plan"\n',
              "observation-on-request": '[probe]\nobservations = "on-request"\n'}.get(case, "")
    seen, bad = [], []
    try:
        root = write_probe_fixture(policy, kits=case == "points-undeclared")
    except (subprocess.CalledProcessError, OSError, LookupError) as e:
        print("%s: %s · the fixture could not be built: %s · MISSED" % (SAY, case, e))
        return 1
    try:
        check_probe_plant(case, root, seen, bad)
    except (subprocess.CalledProcessError, OSError, LookupError, ValueError) as e:
        bad.append("the plant could not run: %s" % e)
    finally:
        remove_tree(root)
    held = not bad
    print("%s: %s · %s · %s" % (SAY, case, " · ".join(seen) or "-", "held" if held else "MISSED " + "; ".join(bad)))
    return 0 if held else 1


def check_probe_plant(case, root, seen, bad):
    """Run `case` over the fixture at `root`, appending each observation to `seen` and each miss to `bad`."""
    build = ["--build", FX_BUILD, "--unit", FX_UNIT]
    folder = root / "memory" / "builds" / FX_BUILD / "build"
    store = pathlib.Path(run_probe_git(root, "rev-parse", "--path-format=absolute", "--git-common-dir")) / "requests"

    def trigger(cause, *more, subject="the owner reports the card drops its route"):
        return run_probe_command(root, "trigger", "--cause", cause, "--asker", FX_ASKER, "--subject", subject, *more)

    def expect(what, got, rc, *needles):
        """One observation: `got`, `(exit, output)`, owed `rc` and a line holding every needle."""
        line = next((ln for ln in got[1].splitlines() if all(n in ln for n in needles)), None)
        seen.append("%s exit %d" % (what, got[0]))
        if got[0] != rc or line is None:
            bad.append("%s: exit %d, owed %d with a line holding %s: %s" % (
                what, got[0], rc, " and ".join(needles), got[1][-300:]))
        return line or ""

    def opened(line):
        """The record an opened or pinned line names, as a path."""
        m = re.search(r"probe — (?:opened|pinned) · (\S+) · ", line)
        return pathlib.Path(m.group(1)) if m else None

    def pinned(kind, *more):
        """A trigger by the owner and its probe pinned at HEAD: the probe record's path."""
        rel = opened(expect("trigger", trigger("owner", *build), 0, "probe — opened"))
        got = run_probe_command(root, "pin", "--trigger", str(rel), "--sha", "HEAD", "--kind", kind,
                                "--question", "does a compaction drop the card's route?",
                                "--losing", "the replayed card keeps its route section", *more)
        out = opened(expect("pin", got, 0, "probe — pinned"))
        return root / out if out else root

    def clean(what):
        status = run_probe_git(root, "status", "--porcelain")
        seen.append("%s status %s" % (what, "clean" if not status else "dirty"))
        if status:
            bad.append("%s left the tree dirty: %s" % (what, status))

    if case == "trigger-causes":   # AC2
        expect("hunch", trigger("hunch", *build), 2, "point owner observation raised reproduction")
        rel = opened(expect("owner", trigger("owner", *build), 0, "probe — opened", "to item.probe.pin"))
        if not rel or not re.fullmatch(r"memory/builds/%s/build/\d{4}-\d{2}-\d{2}-build-%s-probe-trigger-1\.md" % (
                FX_BUILD, FX_UNIT), rel.as_posix()):
            bad.append("the trigger record is %s, not <date>-build-%s-probe-trigger-1.md" % (rel, FX_UNIT))
        expect("no unit", trigger("owner", "--build", FX_BUILD), 2, "--unit")
        if len(list(folder.glob("*.md"))) != 1:
            bad.append("the build folder holds %d records, not 1" % len(list(folder.glob("*.md"))))
    elif case in ("raise-owner-only", "raise-off", "points-unlisted", "observation-at-plan",
                  "observation-on-request"):   # AC3
        refused, admitted = {
            "raise-owner-only": ([("raised",)], ("owner",)),
            "raise-off": ([("owner",), ("raised",)], ("reproduction",)),
            "points-unlisted": ([("point", "--at", "item.entry.place")], ("point", "--at", "item.plan.input")),
            "observation-at-plan": ([("observation", "--at", "item.entry.place")],
                                    ("observation", "--at", "item.plan.input")),
            "observation-on-request": ([("observation", "--at", "item.entry.place"),
                                        ("observation", "--at", "item.plan.input")], ("owner",))}[case]
        key = {"raise": "probe.raise", "point": "probe.points", "obser": "probe.observations"}[case[:5]]
        for cause in refused:
            line = expect(cause[0], trigger(*cause, *build), 1, "probe — not opened", key + ":")
            if not line.endswith("· to %s" % FX_ASKER):
                bad.append("the refusal %r does not end · to %s" % (line, FX_ASKER))
            clean(cause[0])
        expect(admitted[0], trigger(*admitted, *build), 0, "probe — opened")
    elif case == "points-undeclared":
        expect("points", run_probe_command(root, "points", "--build", FX_BUILD), 1, "probe — refused · probe.points:",
               "item.plan.nope")
    elif case == "pin":   # AC4
        rel = opened(expect("trigger", trigger("owner", *build), 0, "probe — opened"))
        before = sorted(p.name for p in folder.glob("*.md"))
        expect("bad sha", run_probe_command(root, "pin", "--trigger", str(rel), "--sha", "0badc0de", "--kind",
                                            "verification", "--question", "q", "--losing", "l"), 2, "names no commit")
        if sorted(p.name for p in folder.glob("*.md")) != before:
            bad.append("a refused pin wrote a record")
        got = run_probe_command(root, "pin", "--trigger", str(rel), "--sha", "HEAD", "--kind", "verification",
                                "--question", "does a compaction drop the card's route?",
                                "--losing", "the replayed card keeps its route section")
        out = opened(expect("pin", got, 0, "probe — pinned", "to item.probe.design"))
        subject = run_probe_git(root, "log", "-1", "--format=%s")
        held = run_probe_git(root, "show", "HEAD:%s" % out.as_posix()) if out else ""
        seen.append("subject %s" % subject)
        if subject != "probe pin(%s): verification" % FX_ASKER or "- **Losing:** " not in held or "run ·" in held:
            bad.append("the pin commit reads %r and holds %r" % (subject, held[-300:]))
        head = run_probe_git(root, "rev-parse", "HEAD")
        entry = opened(expect("entry trigger", trigger("observation", "--request", FX_KEY, "--at", FX_ASKER), 0,
                              "probe — opened"))
        expect("entry pin", run_probe_command(root, "pin", "--trigger", str(entry), "--sha", "HEAD", "--kind",
                                              "verification", "--question", "q", "--losing", "the route stays"), 0,
               "probe — pinned", "%s.probe.md" % FX_KEY)
        stored = store / ("%s.probe.md" % FX_KEY)
        if not stored.is_file() or "- **Losing:** the route stays" not in stored.read_text(encoding="utf-8"):
            bad.append("the entry-time head is not %s holding Losing" % stored.as_posix())
        if run_probe_git(root, "rev-parse", "HEAD") != head:
            bad.append("the entry-time pin moved HEAD")
    elif case == "entry-time":   # AC8
        rel = opened(expect("first", trigger("observation", "--request", FX_KEY, "--at", FX_ASKER), 0,
                            "probe — opened"))
        if rel != store / ("%s.probe-trigger.md" % FX_KEY):
            bad.append("the record is %s, not requests/%s.probe-trigger.md" % (rel, FX_KEY))
        if folder.exists() and any(folder.iterdir()):
            bad.append("an entry-time trigger wrote into the build folder")
        expect("second", trigger("observation", "--request", FX_KEY, "--at", FX_ASKER, subject="a second observation"),
               0, "probe — joined")
        text = rel.read_text(encoding="utf-8") if rel and rel.is_file() else ""
        if text.count("- **Subject:** ") != 2:
            bad.append("the record holds %d Subject lines, not 2" % text.count("- **Subject:** "))
        expect("first again", trigger("observation", "--request", FX_KEY, "--at", FX_ASKER), 1, "already opened")
    elif case in ("run-judge", "run-refuted"):   # AC5, AC7
        head = run_probe_git(root, "rev-parse", "HEAD")
        prediction = "1:000000000000"
        if case == "run-judge":
            [(_c, code, digest)] = run_witness_commands(root, head, [FX_CMD])
            prediction = "%s:%s" % (code, digest)
        probe = pinned("reproduction")
        expect("design", run_probe_command(root, "design", "--probe", str(probe), "--cmd", FX_CMD, "--expect",
                                           prediction), 0, "probe — designed")
        expect("run", run_probe_command(root, "run", "--probe", str(probe)), 0, "probe — ran")
        verdict = "confirmed" if case == "run-judge" else "refuted"
        expect("judge", run_probe_command(root, "judge", "--probe", str(probe)), 0, "probe — judged · " + verdict)
        expect("return", run_probe_command(root, "return", "--probe", str(probe)), 0,
               "probe — %s · " % verdict, "· to %s" % FX_ASKER)
        text = probe.read_text(encoding="utf-8")
        if "- **Verdict:** %s" % verdict not in text or "- **Judged:** computed" not in text:
            bad.append("the record does not hold Verdict %s and Judged computed: %s" % (verdict, text[-400:]))
        if case == "run-judge":   # AC7: both read clean and bound as their kinds
            mt = read_memory_tree("gen_build_index.py")
            for rec in sorted(folder.glob("*.md")):
                p = subprocess.run([sys.executable, str(mt / "build_records.py"), "read", str(rec)],
                                   capture_output=True, text=True, encoding="utf-8", errors="replace")
                seen.append("read %s exit %d" % (rec.name, p.returncode))
                if p.returncode != 0:
                    bad.append("build_records.py read %s exited %d: %s" % (rec.name, p.returncode, p.stdout[-300:]))
            run_probe_git(root, "add", "-A")
            p = subprocess.run([sys.executable, str(mt / "gen_build_index.py"), "--print-bindings"], cwd=root,
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
            rows = p.stdout.splitlines()
            for kind in ("probe-trigger", "probe"):
                hit = [r for r in rows if r.startswith("S\t") and r.split("\t")[2:3] == [kind]
                       and re.search(r"-%s-1\.md$" % kind, r.split("\t")[1])]
                seen.append("S %s %d" % (kind, len(hit)))
                if len(hit) != 1:
                    bad.append("--print-bindings printed %d S row(s) of kind %s" % (len(hit), kind))
            if any(r.startswith("A\t") for r in rows):
                bad.append("--print-bindings printed an A row: %s" % [r for r in rows if r.startswith("A\t")])
    elif case in ("visual", "judge-claimed"):   # AC6
        probe = pinned("verification")
        mark = "visual" if case == "visual" else "judge claimed"
        expect("design", run_probe_command(root, "design", "--probe", str(probe), "--cmd", FX_CMD, "--expect",
                                           "1:9c0e5a1b2f33", "--mark", mark), 0, "probe — designed")
        if case == "visual":
            expect("run", run_probe_command(root, "run", "--probe", str(probe)), 0, "probe — unrunnable",
                   "to item.probe.return")
            text = probe.read_text(encoding="utf-8")
            if "run ·" in text or "- **Verdict:** unrunnable" not in text or "- **Judged:** computed" not in text:
                bad.append("the record is not unrunnable, computed and unrun: %s" % text[-400:])
            expect("return", run_probe_command(root, "return", "--probe", str(probe)), 0, "probe — unrunnable",
                   "to %s" % OWNER_ITEM)
        else:
            expect("run", run_probe_command(root, "run", "--probe", str(probe)), 0, "probe — ran")
            expect("judge", run_probe_command(root, "judge", "--probe", str(probe)), 0, "probe — claimed",
                   "to item.probe.judge-claimed")
            text = probe.read_text(encoding="utf-8")
            if "- **Judged:** claimed" not in text or "- **Verdict:** " in text:
                bad.append("the record is not claimed with no verdict: %s" % text[-400:])
            expect("return", run_probe_command(root, "return", "--probe", str(probe)), 0, "probe — claimed",
                   "to %s" % OWNER_ITEM)
    elif case == "experiment":   # AC6
        rel = opened(expect("trigger", trigger("owner", *build), 0, "probe — opened"))
        got = run_probe_command(root, "pin", "--trigger", str(rel), "--sha", "HEAD", "--kind", "experiment",
                                "--question", "how long does a replay take?", "--losing", "it takes no longer")
        expect("pin", got, 0, "probe — pinned", "to item.probe.experiment")
        expect("stand-in", got, 0, "probe — beyond-authority", "dBoundRoles", "probe.experiment.authority=within-cap",
               "to %s" % OWNER_ITEM)
    elif case == "verdict-cross":   # AC7
        probe = pinned("reproduction")
        write_probe_fields(probe, [("Verdict", "measured"), ("Judged", "computed")])
        mt = read_memory_tree("build_records.py")
        p = subprocess.run([sys.executable, str(mt / "build_records.py"), "read", str(probe)], capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        expect("read", (p.returncode, p.stdout + p.stderr), 1, "malformed · Verdict", "measured")
    elif case == "design":   # AC14
        probe = pinned("verification")
        design = ["design", "--probe", str(probe), "--cmd", FX_CMD, "--expect", "1:9c0e5a1b2f33"]
        before = probe.read_bytes()
        for what, argv, needle in (("bad expect", design[:-1] + ["one"], "--expect"),
                                   ("bad mark", design + ["--mark", "audible"], "--mark"),
                                   ("separator", design[:4] + ["bash a.sh · b", "--expect", "1:9c0e5a1b2f33"],
                                    "field separator")):
            expect(what, run_probe_command(root, *argv), 2, needle)
        if probe.read_bytes() != before:
            bad.append("a refused design changed the record")
        expect("first", run_probe_command(root, *design), 0, "probe — designed", "method 1")
        expect("second", run_probe_command(root, *design, "--mark", "visual"), 0, "probe — designed", "method 2")
        entries = [ln for ln in probe.read_text(encoding="utf-8").splitlines() if ln.startswith("- method · ")]
        if len(entries) != 2 or entries[0] != "- method · 1:9c0e5a1b2f33 · %s" % FX_CMD \
                or not entries[1].endswith(" · visual"):
            bad.append("the method holds %r, not the entry and a second ending · visual" % entries)
        frozen = pinned("verification")
        expect("third design", run_probe_command(root, "design", "--probe", str(frozen), "--cmd", FX_CMD, "--expect",
                                                 "1:9c0e5a1b2f33"), 0, "probe — designed")
        expect("run", run_probe_command(root, "run", "--probe", str(frozen)), 0, "probe — ran")
        held = frozen.read_bytes()
        expect("frozen", run_probe_command(root, "design", "--probe", str(frozen), "--cmd", FX_CMD, "--expect",
                                           "1:9c0e5a1b2f33"), 2, "is frozen", frozen.name)
        if frozen.read_bytes() != held:
            bad.append("design wrote to a frozen record")


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    try:   # the kinds and marks are the record factory's, the one home of the probe record's grammar
        br = read_build_records()
    except LookupError as e:
        print("%s — refused · unarmed · %s" % (SAY, e))
        return 2
    ap = argparse.ArgumentParser(prog="probe.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run one fixture case")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--selftest", action="store_true", help="run every fixture case")
    sub = ap.add_subparsers(dest="verb")
    trig = sub.add_parser("trigger", help="open a probe at an item boundary")
    for flag in ("--cause", "--asker", "--subject"):
        trig.add_argument(flag, required=True)
    for flag in ("--build", "--unit", "--request", "--at"):
        trig.add_argument(flag)
    pin = sub.add_parser("pin", help="pin the probe's head before any command runs")
    for flag in ("--trigger", "--sha", "--question", "--losing"):
        pin.add_argument(flag, required=True)
    pin.add_argument("--kind", required=True, choices=list(br.PROBE_KINDS))
    des = sub.add_parser("design", help="append one entry to the probe's method")
    for flag in ("--probe", "--cmd", "--expect"):
        des.add_argument(flag, required=True)
    des.add_argument("--mark", action="append", choices=list(br.METHOD_MARKS))
    for verb, what in (("run", "re-run the method at the pinned commit"), ("judge", "compute the verdict"),
                       ("return", "hand the record back to its asker")):
        sub.add_parser(verb, help=what).add_argument("--probe", required=True)
    sub.add_parser("points", help="list probe.points at a build's pin").add_argument("--build", required=True)
    args = ap.parse_args(argv)
    if args.selftest:
        if args.fixture or args.plant or args.verb:
            ap.error("--selftest takes no verb and no plant")
        cases = [(p, ["--fixture", "--plant", p], 0, "%s: %s · " % (SAY, p), "· held") for p in PLANTS]
        return run_selftest_cases(main, cases, "%s: selftest" % SAY)
    if args.fixture != bool(args.plant) or (args.fixture and args.verb):
        ap.error("--fixture takes --plant <case> and no verb")
    if args.fixture:
        return run_probe_plant(args.plant)
    if args.verb is None:
        ap.error("a verb, trigger, pin, design, run, judge, return or points, or --fixture --plant <case>, or --selftest")
    try:
        root, common = resolve_git_paths()
        store = common / "requests"
        if args.verb == "points":
            return check_probe_points(args, root)
        return {"trigger": write_probe_trigger, "pin": write_probe_pin, "design": write_method_entry,
                "run": run_probe_rerun, "judge": write_probe_verdict, "return": write_probe_return}[args.verb](
            args, root, store)
    except ProbeRefused as e:
        print("%s — refused · %s" % (SAY, e))
        return e.code
    except (LookupError, LoopError, OSError) as e:
        print("%s — refused · unarmed · %s" % (SAY, e))
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
