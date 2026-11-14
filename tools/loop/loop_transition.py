#!/usr/bin/env python3
"""loop_transition.py — a build's stage transition recorded three ways, the set `transitions.record` selects (TOOL-dDeclaredLoop-3).

    python loop_transition.py record --build <slug> --from <state> --item <tag> --outcome <o> --witness <sha>
                                     [--fact k=v]... [--field k=v]... [--root <path>]
    python loop_transition.py check --build <slug> [--root <path>]
    python loop_transition.py check --selftest
    python loop_transition.py --fixture --plant <case>

THE CHANNELS. The policy key `transitions.record`, read through the policy kit's `resolve` at one
revision per move, selects any non-empty subset of three, all three by default:

    trailer        Gov-Transition: <from> -> <to> · build=<slug> · item=<tag> · sha=<sha8>[ · <name>=<value>]...
    log            <date>-build-<anchor id>-transition-<n>.md in the build's build/ folder, written through the
                   memory-tree kit's `write_record`: Build, From, To, Item, Sha, then each extension field capitalised
    micro-format   transition — <slug> · <from> → <to> · <item tag> · <sha>, printed after the commit

`build`, `item` and `sha` come first in that order, and any other field name is one of
`TRANSITION_FIELDS`; every value matches `VALUE`, so none holds the separator. The anchor is the lowest
unit id a tracked spec H1 under the build defines. A move made before the build's first spec writes no
record, and the writer's next move after it back-fills one per earlier trailer, oldest first.

`record` (`write_transition`) reads the set at HEAD, the move's parent; answers the move by the build
table's `derive_move`, printing `refused — ...` and exiting 1 where no row holds it; resolves `--witness`
to HEAD or an ancestor of it, adding `stand-in=<owner>` where the item has a `[[stand-in]]` row; refuses
a staged index; back-fills, writes this move's record, commits the records, or an empty commit, as
`loop transition(<slug>): <from> -> <to>` with the trailer where selected, and prints the line where
selected. A set storing neither the trailer nor the log writes no commit.

`check` (`check_transition_channels`) holds each channel to the trailer: per trailer whose commit's set
holds `log`, one record with equal `**Key:**` fields; no record left over where its adding commit's set
holds `trailer`; and the `transition` definition of the micro-format fence of `AGENTS.md` at `--root`
equal to `TRANSITION_LINE`. A record whose adding commit's set lacks `trailer` is its move's source.
It prints each finding as `loop: transition · ...`, naming the commit, the channel and the field;
`pending — <n> move(s) before the build's first spec` while trailers wait on a spec; `unstored — ...`
where the set at HEAD stores nothing; then its summary. `read_transitions(build, repo)` is the build's
moves newest first, from the trailer where one was written and from the record otherwise.

Exit: `record` 0 recorded, 1 refused by the table; `check` 0 clean, 1 on a finding, `pending` or
`unstored`. Both exit 2 printing `loop: unanswered · <why>` on a value outside its grammar, a witness
that is not HEAD or its ancestor, a staged index, or a policy refusal naming `transitions.record`, an
empty set with no valid revision before it among them; and 2 printing `loop: unarmed · <why>` where the
policy or memory-tree kit does not resolve, never a default. The loop kit takes no edge to the policy
kit, which is why.

`--fixture --plant <case>` builds a scratch repository under the host temp directory holding the build
`tFix`, runs `record` and `check` there in process, prints each verdict, removes the scratch and exits
as its last verb. `check --selftest` holds the definition of `AGENTS.md` in the current directory, then
runs every plant through `run_selftest_cases`, each plant once however many cases read it.

WHAT THIS DOES NOT CHECK: that a witness holds beyond resolving; a record's lines after its fields; a
feature- or unit-level move; a charter other than the one `AGENTS.md`. A record pairs with a trailer by
order, the n-th owing trailer with the n-th such record, so two records swapped read as two drifts.
"""
import argparse
import contextlib
import io
import pathlib
import re
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import read_definition, read_memory_tree, run_selftest_cases  # noqa: E402
from loop_parents import read_policy_kit  # noqa: E402
from loop_table import TransitionRefused, derive_move, read_stand_ins, read_transition_rows  # noqa: E402
from loop_witness import read_git, remove_tree, resolve_commit, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "loop"
KEY = "transitions.record"
TRAILER_KEY = "Gov-Transition"
KIND = "transition"
#: The extension fields a trailer and a record may carry after `build`, `item` and `sha`, in the order
#: they are written; later units extend it.
TRANSITION_FIELDS = ("stand-in",)
#: The micro-format definition `render_transition_line` fills, held equal to `AGENTS.md`'s by `check`.
TRANSITION_LINE = "transition — <slug> · <from> → <to> · <item tag> · <sha>"
#: Each placeholder of `TRANSITION_LINE` and the field that fills it.
LINE_FIELDS = (("<slug>", "build"), ("<from>", "from"), ("<to>", "to"), ("<item tag>", "item"), ("<sha>", "sha"))
#: The fields every trailer carries after its head, in this order.
HEAD_FIELDS = ("build", "item", "sha")
#: A field value: never a space, so never the separator.
VALUE = re.compile(r"[A-Za-z0-9._:+@-]+")
STATE = re.compile(r"[a-z0-9][a-z0-9-]*")
SHA = re.compile(r"[0-9a-f]{8,40}")
SEP = " · "
FENCE = ("<!-- microformats -->", "<!-- /microformats -->")
PLANTS = {"default": "the default set, one B4 move with its witness",
          "subset-trailer-line": "the set [\"trailer\", \"micro-format\"], one B4 move",
          "subset-log": "the set [\"log\"], one B4 move",
          "empty-set": "the set [], the policy file's one revision",
          "log-drift": "one B4 move, its record then edited to To: building",
          "orphan-log": "one B4 move, then a second record committed with no trailer",
          "no-row": "planning to building through item.design.exit, which no row holds",
          "line-drift": "an AGENTS.md whose definition drops <item tag>",
          "pre-spec": "a build with no spec moved once, then a spec planted and a second move",
          "field": "composition registered, a move with --field composition=3f9c2a71 and one with colour=red"}
#: The plants' policy values, committed as `.governance/policy.toml`; a plant not here commits none.
PLANT_SETS = {"subset-trailer-line": '["trailer", "micro-format"]', "subset-log": '["log"]', "empty-set": "[]"}
FX_BUILD = "tFix"
FX_UNIT = "TOOL-tFix-1"
FX_SPEC = "memory/builds/tFix/spec/2026-01-01-spec-%s.md" % FX_UNIT


# ------------------------------------------------------------------------------------------ the grammar
def render_transition_trailer(fields):
    """`Gov-Transition: <from> -> <to> · build=<slug> · item=<tag> · sha=<sha>`, then each extension field
    `fields` carries as ` · <name>=<value>`, in `TRANSITION_FIELDS` order."""
    names = HEAD_FIELDS + tuple(n for n in TRANSITION_FIELDS if n in fields)
    return "%s: %s -> %s%s" % (TRAILER_KEY, fields["from"], fields["to"],
                               "".join("%s%s=%s" % (SEP, n, fields[n]) for n in names))


def parse_transition_trailer(value):
    """The fields of one `Gov-Transition` value, `from` and `to` first; ValueError naming what is outside
    the grammar."""
    parts = value.split(SEP)
    head = re.fullmatch(r"(\S+) -> (\S+)", parts[0])
    if not head or not all(STATE.fullmatch(s) for s in head.groups()):
        raise ValueError("the head %r is not <from> -> <to>, each one state word" % parts[0])
    fields = {"from": head.group(1), "to": head.group(2)}
    for part in parts[1:]:
        name, eq, v = part.partition("=")
        if not eq or name in fields:
            raise ValueError("the field %r is not one <name>=<value> named once" % part)
        fields[name] = v
    names = list(fields)[2:]
    if names[:3] != list(HEAD_FIELDS):
        raise ValueError("the fields open %s, not build, item and sha in that order" % " ".join(names[:3]))
    extra = [n for n in names[3:] if n not in TRANSITION_FIELDS]
    if extra:
        raise ValueError("the field %s is no registered extension field: %s" % (extra[0], " ".join(TRANSITION_FIELDS)))
    bad = [n for n in names if not VALUE.fullmatch(fields[n])] + [n for n in ("sha",) if not SHA.fullmatch(fields[n])]
    if bad:
        raise ValueError("the value of %s is outside its grammar: %r" % (bad[0], fields[bad[0]]))
    return fields


def render_transition_line(fields):
    """The micro-format line of one move: `TRANSITION_LINE` with each placeholder filled from `fields`."""
    line = TRANSITION_LINE
    for placeholder, name in LINE_FIELDS:
        line = line.replace(placeholder, fields[name])
    return line


def render_record_key(name):
    """A field name as a record's `**Key:**`: `stand-in` reads `Stand-in`."""
    return name[:1].upper() + name[1:]


def check_transition_definition(root):
    """The findings of the `transition` definition in the micro-format fence of `AGENTS.md` at `root`
    against `TRANSITION_LINE`: none where one definition equals it."""
    try:
        text = (pathlib.Path(root) / "AGENTS.md").read_bytes().decode("utf-8", "replace")
    except OSError as e:
        return ["definition · AGENTS.md does not read: %s" % e.strerror]
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    if FENCE[0] not in lines or FENCE[1] not in lines[lines.index(FENCE[0]):]:
        return ["definition · AGENTS.md holds no %s fence, so the renderer's %s is defined nowhere" % (
            FENCE[0], TRANSITION_LINE)]
    start = lines.index(FENCE[0])
    held = [ln[3:-1] for ln in lines[start:lines.index(FENCE[1], start)]
            if ln.startswith("- `transition — ") and ln.endswith("`")]
    if not held:
        return ["definition · the micro-format fence of AGENTS.md defines no transition line; the renderer "
                "writes %s" % TRANSITION_LINE]
    return ["definition · AGENTS.md reads %s, while the renderer writes %s" % (d, TRANSITION_LINE)
            for d in held if d != TRANSITION_LINE]


# ------------------------------------------------------------------------------------------ the reads
def read_record_channels(root, rev):
    """The channel set `transitions.record` selects at `rev`, a frozenset. ValueError naming the key on a
    policy refusal; LookupError where the policy kit does not resolve."""
    policy, _guard = read_policy_kit()
    try:
        value = policy.resolve(KEY, str(root), rev).value
    except policy.Refusal as e:
        raise ValueError("%s does not resolve at %s: %s" % (KEY, rev, e)) from None
    return frozenset(value)


def read_cached_channels(root, rev, cache):
    """`read_record_channels` once per revision, `cache` keyed by the revision as given."""
    if rev not in cache:
        cache[rev] = read_record_channels(root, rev)
    return cache[rev]


def read_memory_root(root):
    """The memory root `<root>`'s `.memory-tree.conf` names, `memory` where unset."""
    read_memory_tree("design_lib.py")
    from design_lib import read_design_conf
    return (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/")


def resolve_build_anchor(build, root):
    """The lowest unit id a tracked spec H1 under `build` defines, by its number, or None."""
    read_memory_tree("tree_lib.py")
    from design_lib import read_design_conf, read_tracked_builds
    from tree_lib import parse_spec_h1
    conf = read_design_conf(root)
    memory_root = read_memory_root(root)
    families = [p.split(":", 1)[1] for p in conf.get("FAMILIES", "").split() if ":" in p]
    prefix = "%s/builds/%s/spec/" % (memory_root, build)
    ids = []
    for rel in read_tracked_builds(root, memory_root):
        path = pathlib.Path(root, rel)
        if rel.startswith(prefix) and rel.endswith(".md") and path.is_file():
            hit = parse_spec_h1(rel, path.read_bytes().decode("utf-8", "replace"), memory_root, families)
            if hit:
                ids.append(hit[1])
    return min(ids, key=lambda i: (int(i.rsplit("-", 1)[1]), i), default=None)


def read_transition_commits(build, root):
    """`([(commit, fields)], findings)`: every commit reachable from HEAD carrying a `Gov-Transition`
    trailer whose `build` is `build`, oldest first, read by the memory-tree kit's `read_commits`; a
    trailer outside the grammar and a commit carrying two are findings."""
    read_memory_tree("commit_trailers.py")
    from commit_trailers import read_commits
    commits = read_commits(str(root), ["--grep=^%s: " % TRAILER_KEY, "HEAD"], [TRAILER_KEY])
    out, findings = [], []
    for c in reversed(commits):
        values = [v for v in c["trailers"][TRAILER_KEY] if v]
        mine = [v for v in values if "build=%s" % build in v.split(SEP)]
        if not mine:
            continue
        if len(values) > 1:
            findings.append("commit %s · trailer · carries %d %s trailers, and a transition commit carries one" % (
                c["sha"][:8], len(values), TRAILER_KEY))
        try:
            out.append((c, parse_transition_trailer(mine[0])))
        except ValueError as e:
            findings.append("commit %s · trailer · %s" % (c["sha"][:8], e))
    return out, findings


def read_transition_records(build, root):
    """The build's transition records in its `build/` folder, by `<n>`, each read by the memory-tree
    kit's `read_transition`, with `fields`, its `**Key:**` fields under their lowercase names."""
    read_memory_tree("build_records.py")
    from build_records import read_transition
    folder = pathlib.Path(root, read_memory_root(root), "builds", build, "build")
    out = []
    for p in folder.glob("*-%s-*.md" % KIND) if folder.is_dir() else ():
        rec = read_transition(p.relative_to(root).as_posix(), p.read_bytes().decode("utf-8", "replace"))
        if rec["n"] is not None:
            rec["fields"] = {k.lower(): v for k, v in rec.items() if k[:1].isupper()}
            out.append(rec)
    return sorted(out, key=lambda r: r["n"])


def read_transition_moves(build, root, cache):
    """The build's moves as its channels hold them: `trailers` `[(commit, fields)]` oldest first, `owing`
    those whose commit's set holds `log`, `paired` the records whose adding commit's set holds `trailer`
    (the n-th pairs with the n-th owing trailer), `sourced` the rest, each its move's source, `adding`
    `{record path: its adding commit}`, and `findings`."""
    read_memory_tree("tree_lib.py")
    from tree_lib import read_adding_commits
    trailers, findings = read_transition_commits(build, root)
    records = read_transition_records(build, root)
    glob = "%s/builds/%s/build/*-%s-*.md" % (read_memory_root(root), build, KIND)
    adding = read_adding_commits(str(root), glob, [r["path"] for r in records])
    paired = [r for r in records if "trailer" in read_cached_channels(root, adding.get(r["path"], "HEAD"), cache)]
    return {"trailers": trailers, "owing": [(c, t) for c, t in trailers
                                            if "log" in read_cached_channels(root, c["sha"], cache)],
            "paired": paired, "sourced": [r for r in records if r not in paired], "adding": adding,
            "findings": findings}


def read_transitions(build, repo):
    """The build's recorded moves, newest first: each the fields of its trailer, or of its record where
    the move wrote no trailer, with `commit` and `source` (`trailer` or `log`). ValueError or OSError
    where a read is refused; LookupError where a kit does not resolve."""
    root = pathlib.Path(repo).absolute()
    moves = read_transition_moves(build, root, {})
    out = [dict(t, commit=c["sha"], source="trailer") for c, t in moves["trailers"]]
    if moves["sourced"]:
        order = read_git(root, "rev-list", "--reverse", "HEAD")[1].split()
        at = {sha: n for n, sha in enumerate(order)}
        out += [dict(r["fields"], commit=moves["adding"].get(r["path"]), source="log") for r in moves["sourced"]]
        out.sort(key=lambda m: at.get(m["commit"], len(at)))
    return out[::-1]


# ------------------------------------------------------------------------------------------ the writer
def write_transition_record(root, anchor, move):
    """The next transition record of the move's build, under `anchor`, from `move`'s fields: its path."""
    read_memory_tree("build_records.py")
    from build_records import write_record
    names = ("build", "from", "to", "item", "sha") + tuple(n for n in TRANSITION_FIELDS if n in move)
    return write_record(root, move["build"], anchor, KIND, "%s -> %s" % (move["from"], move["to"]),
                        [(render_record_key(n), move[n]) for n in names])


def write_transition(root, build, state, item, outcome, witness, facts, fields):
    """Record one build move in the repository at `root`, an absolute path: `(move fields, the commit's
    sha or None, [record paths], the line or None)`. TransitionRefused where no row holds the move;
    ValueError on a value, witness, index or policy read refused, writing nothing; LookupError where a
    kit it reads does not resolve."""
    cache = {}
    chosen = read_cached_channels(root, "HEAD", cache)
    data, where = read_definition(KIT)
    _row, to = derive_move("build", state, item, outcome, facts, read_transition_rows(data, where))
    sha = resolve_commit(root, witness)
    if sha is None:
        raise ValueError("--witness %s names no commit in %s" % (witness, root.as_posix()))
    if read_git(root, "merge-base", "--is-ancestor", sha, "HEAD")[0] != 0:
        raise ValueError("--witness %s is neither HEAD nor an ancestor of it" % witness)
    move = {"from": state, "to": to, "build": build, "item": item, "sha": sha[:8]}
    for name, value in fields.items():
        if name not in TRANSITION_FIELDS:
            raise ValueError("--field %s is no registered extension field: %s" % (name, " ".join(TRANSITION_FIELDS)))
        move[name] = value
    owner = {r.get("item"): r.get("owner") for r in read_stand_ins(data, where)}.get(item)
    if owner:
        move["stand-in"] = owner
    bad = [n for n, v in move.items() if not (isinstance(v, str) and VALUE.fullmatch(v))]
    if bad:
        raise ValueError("the value of %s, %r, is outside [A-Za-z0-9._:+@-]+" % (bad[0], move[bad[0]]))
    if read_git(root, "diff", "--cached", "--quiet")[0] != 0:
        raise ValueError("the index holds staged changes, and a transition commit carries its own records alone")
    wrote = []
    if "log" in chosen:
        anchor = resolve_build_anchor(build, root)
        if anchor is None and "trailer" not in chosen:
            raise ValueError("%s selects log without trailer and %s defines no spec, so the move has no record to "
                             "write and no trailer to back-fill one from" % (KEY, build))
        if anchor:
            moves = read_transition_moves(build, root, cache)
            try:
                for _c, t in moves["owing"][len(moves["paired"]):]:
                    wrote.append(write_transition_record(root, anchor, t))
                wrote.append(write_transition_record(root, anchor, move))
            except (ValueError, OSError):
                for rel in wrote:
                    pathlib.Path(root, rel).unlink()
                raise
    commit = None
    if wrote or "trailer" in chosen:
        argv = ["commit", "-q", "--allow-empty", "-m", "loop transition(%s): %s -> %s" % (build, state, to)]
        argv += ["-m", render_transition_trailer(move)] if "trailer" in chosen else []
        if (wrote and read_git(root, "add", "--", *wrote)[0] != 0) or read_git(root, *argv)[0] != 0:
            if wrote:
                read_git(root, "reset", "-q", "--", *wrote)
            for rel in wrote:
                pathlib.Path(root, rel).unlink()
            raise ValueError("git could not commit the move in %s, so nothing is recorded" % root.as_posix())
        commit = read_git(root, "rev-parse", "HEAD")[1]
    return move, commit, wrote, render_transition_line(move) if "micro-format" in chosen else None


# ------------------------------------------------------------------------------------------ the check
def check_transition_channels(build, root):
    """`(lines, findings)` of the build's channels held to its trailers, and the definition held to
    `TRANSITION_LINE`: `lines` the `pending` or `unstored` line and the summary. ValueError or OSError
    where a read is refused; LookupError where a kit does not resolve."""
    cache = {}
    head = read_cached_channels(root, "HEAD", cache)
    findings = check_transition_definition(root)
    if not head & {"trailer", "log"}:
        return (["unstored — %s · %s selects %s at HEAD, which stores no move" % (build, KEY, " ".join(sorted(head))),
                 "%s: transition check · %s · unstored · %d finding(s)" % (SAY, build, len(findings))], findings)
    moves = read_transition_moves(build, root, cache)
    findings += moves["findings"]
    lines = []
    for (c, t), rec in zip(moves["owing"], moves["paired"]):
        for name in dict.fromkeys([*t, *rec["fields"]]):
            if t.get(name) != rec["fields"].get(name):
                findings.append("commit %s · log %s · %s: the trailer says %s, the record %s" % (
                    c["sha"][:8], rec["path"], render_record_key(name), t.get(name, "nothing"),
                    rec["fields"].get(name, "nothing")))
    for rec in moves["paired"] + moves["sourced"]:
        findings += ["log %s · malformed · %s %s" % (rec["path"], key, why) for key, why in rec["malformed"]]
    left = moves["owing"][len(moves["paired"]):]
    if left and resolve_build_anchor(build, root) is None:
        lines.append("pending — %d move(s) before the build's first spec" % len(left))
    else:
        findings += ["commit %s · log · the move %s -> %s owes a record, and none holds it" % (
            c["sha"][:8], t["from"], t["to"]) for c, t in left]
    findings += ["log %s · no trailer matches this record, written where %s held trailer" % (rec["path"], KEY)
                 for rec in moves["paired"][len(moves["owing"]):]]
    lines.append("%s: transition check · %s · %d trailer(s) · %d record(s) · %d finding(s)" % (
        SAY, build, len(moves["trailers"]), len(moves["paired"]) + len(moves["sourced"]), len(findings)))
    return lines, findings


# ------------------------------------------------------------------------------------------ the plants
def write_transition_plant(top, case):
    """The scratch repository at `top` for `case`, committed on `main`: the witness commit's sha."""
    run_fixture_git(top, "init", "-q", "--template=", "-b", "main")
    for key, value in (("user.name", "fx"), ("user.email", "fx@example.invalid"), ("commit.gpgsign", "false"),
                       ("core.autocrlf", "false")):
        run_fixture_git(top, "config", key, value)
    line = TRANSITION_LINE.replace(" · <item tag>", "") if case == "line-drift" else TRANSITION_LINE
    files = {".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tool:TOOL"\n',
             "AGENTS.md": "# AGENTS.md\n\n%s\n- `committed — <sha> · <branch> · <subject>`\n- `%s`\n%s\n" % (
                 FENCE[0], line, FENCE[1]),
             "memory/builds/%s/README.md" % FX_BUILD: "# %s\n" % FX_BUILD}
    if case != "pre-spec":
        files[FX_SPEC] = "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n" % FX_UNIT
    if case in PLANT_SETS:
        files[".governance/policy.toml"] = "[transitions]\nrecord = %s\n" % PLANT_SETS[case]
    write_fixture_files(top, files)
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "fixture")
    return run_fixture_git(top, "rev-parse", "HEAD")


def run_transition_fixture(case):
    """`record` and `check` over a scratch repository planted as `case`: the last verb's exit."""
    global TRANSITION_FIELDS
    registered = TRANSITION_FIELDS
    top = pathlib.Path(tempfile.mkdtemp(prefix="loop-transition-")).absolute()
    try:
        print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
        witness = write_transition_plant(top, case)
        at = ["--build", FX_BUILD, "--root", str(top)]
        b4 = ["record", *at, "--from", "planning", "--item", "item.plan.exit", "--outcome", "recorded",
              "--witness", witness]

        def run_verb(argv):
            rc = main(argv)
            print("%s: fixture · %s · exit %d" % (SAY, argv[0], rc))
            return rc

        def read_count():
            return run_fixture_git(top, "rev-list", "--count", "HEAD")

        def read_folder():
            recs = read_transition_records(FX_BUILD, top)
            print("%s: fixture · records %d%s" % (SAY, len(recs), "".join(" · %s-%d %s -> %s" % (
                KIND, r["n"], r.get("From"), r.get("To")) for r in recs)))
            return recs

        def write_commit(subject):
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", subject)

        if case in ("no-row", "empty-set"):
            before = read_count()
            argv = b4 if case == "empty-set" else b4[:7] + ["--item", "item.design.exit"] + b4[9:]
            rc = run_verb(argv)
            print("%s: fixture · commits %s" % (SAY, "unchanged" if read_count() == before else "changed"))
            return rc if case == "no-row" else run_verb(["check", *at])
        if case == "field":
            TRANSITION_FIELDS = registered + ("composition",)
            run_verb(b4 + ["--field", "colour=red"])
            run_verb(b4 + ["--field", "composition=3f9c2a71"])
        else:
            run_verb(b4)
        value = run_fixture_git(top, "log", "-1", "--format=%%(trailers:key=%s,valueonly)" % TRAILER_KEY)
        print("%s: fixture · trailer %s" % (SAY, value or "none"))
        recs = read_folder()
        if case == "default" and recs:
            read_memory_tree("build_records.py")
            import build_records
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rc = build_records.main(["read", str(top / recs[0]["path"])])
            print("%s: fixture · build_records read · exit %d · %d field(s)" % (SAY, rc, out.getvalue().count("\n")))
        if case in ("subset-log", "field"):
            for m in read_transitions(FX_BUILD, top):
                print("%s: fixture · read %s · %s" % (SAY, m["source"], render_transition_trailer(m).split(": ", 1)[1]))
        if case == "log-drift" and recs:
            path = top / recs[0]["path"]
            path.write_bytes(path.read_bytes().replace(b"- **To:** designing", b"- **To:** building"))
            write_commit("the record edited")
        if case == "orphan-log" and recs:
            write_transition_record(top, FX_UNIT, recs[0]["fields"])
            write_commit("a record no trailer backs")
        if case == "pre-spec":
            run_verb(["check", *at])
            write_fixture_files(top, {FX_SPEC: "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n" % FX_UNIT})
            write_commit("the first spec")
            run_verb(["record", *at, "--from", "designing", "--item", "item.design.exit", "--outcome", "recorded",
                      "--witness", "HEAD"])
            read_folder()
        return run_verb(["check", *at])
    finally:
        TRANSITION_FIELDS = registered
        remove_tree(top)


def run_selftest():
    """The tree's own definition, then every plant's owed lines through `run_selftest_cases`, each plant
    run once and its output read by every case naming it."""
    said = {}

    def run_cached_case(argv):
        key = tuple(argv)
        if key not in said:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                if key == ("definition",):
                    found = check_transition_definition(pathlib.Path(".").absolute())
                    for why in found:
                        print("%s: transition · %s" % (SAY, why))
                    print("%s: transition definition · AGENTS.md · %s" % (SAY, "refused" if found else "held"))
                    rc = 1 if found else 0
                else:
                    rc = main(argv)
            said[key] = (rc, out.getvalue())
        sys.stdout.write(said[key][1])
        return said[key][0]

    def read_plant_argv(plant):
        return ["--fixture", "--plant", plant]
    fx = read_plant_argv
    trailer = "%s: fixture · trailer planning -> designing · build=%s · item=item.plan.exit · sha=" % (SAY, FX_BUILD)
    check = "%s: transition check · %s" % (SAY, FX_BUILD)
    cases = [("definition", ["definition"], 0, "%s: transition definition · AGENTS.md · held" % SAY, ""),
             ("default trailer", fx("default"), 0, trailer, " · stand-in=dRankedPlan"),
             ("default record", fx("default"), 0, "%s: fixture · records 1" % SAY, "transition-1 planning -> designing"),
             ("default read", fx("default"), 0, "%s: fixture · build_records read · exit 0" % SAY, ""),
             ("default line", fx("default"), 0, "transition — %s · planning → designing · item.plan.exit · " % FX_BUILD,
              ""),
             ("default check", fx("default"), 0, check, "· 0 finding(s)"),
             ("subset-trailer-line", fx("subset-trailer-line"), 0, "%s: fixture · records 0" % SAY, ""),
             ("subset-trailer-line trailer", fx("subset-trailer-line"), 0, trailer, ""),
             ("subset-trailer-line check", fx("subset-trailer-line"), 0, check, "· 0 finding(s)"),
             ("subset-log trailer", fx("subset-log"), 0, "%s: fixture · trailer none" % SAY, ""),
             ("subset-log read", fx("subset-log"), 0, "%s: fixture · read log · planning -> designing" % SAY, ""),
             ("empty-set record", fx("empty-set"), 2, "%s: unanswered" % SAY, KEY),
             ("empty-set commits", fx("empty-set"), 2, "%s: fixture · commits unchanged" % SAY, ""),
             ("empty-set check", fx("empty-set"), 2, "%s: fixture · check · exit 2" % SAY, ""),
             ("log-drift", fx("log-drift"), 1, "%s: transition · commit " % SAY,
              "To: the trailer says designing, the record building"),
             ("orphan-log", fx("orphan-log"), 1, "%s: transition · log " % SAY, "transition-2.md · no trailer"),
             ("no-row", fx("no-row"), 1, "refused — build · planning · item.design.exit · recorded", "no row"),
             ("no-row commits", fx("no-row"), 1, "%s: fixture · commits unchanged" % SAY, ""),
             ("line-drift", fx("line-drift"), 1, "%s: transition · definition · AGENTS.md reads" % SAY, ""),
             ("pre-spec pending", fx("pre-spec"), 0, "pending — 1 move(s) before the build's first spec", ""),
             ("pre-spec order", fx("pre-spec"), 0, "%s: fixture · records 2" % SAY,
              "transition-1 planning -> designing · transition-2 designing -> building"),
             ("pre-spec check", fx("pre-spec"), 0, check, "· 0 finding(s)"),
             ("field refused", fx("field"), 0, "%s: unanswered" % SAY, "colour"),
             ("field trailer", fx("field"), 0, trailer, "composition=3f9c2a71"),
             ("field read", fx("field"), 0, "%s: fixture · read trailer · " % SAY, "composition=3f9c2a71"),
             ("field check", fx("field"), 0, check, "· 0 finding(s)")]
    return run_selftest_cases(run_cached_case, cases, "%s: transition selftest" % SAY)


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="loop_transition.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run record and check over a scratch repository")
    ap.add_argument("--plant", choices=list(PLANTS))
    sub = ap.add_subparsers(dest="verb")
    rec = sub.add_parser("record", help="record one build move on the channels the set selects")
    for flag in ("--build", "--from", "--item", "--outcome", "--witness"):
        rec.add_argument(flag, required=True)
    rec.add_argument("--fact", action="append", default=[], help="k=v, a fact a row's guard or target reads")
    rec.add_argument("--field", action="append", default=[], help="k=v, a registered extension field")
    rec.add_argument("--root", default=".")
    chk = sub.add_parser("check", help="hold each channel of a build's moves to its trailer")
    chk.add_argument("--build")
    chk.add_argument("--root", default=".")
    chk.add_argument("--selftest", action="store_true", help="the tree's definition, then every plant")
    args = ap.parse_args(argv)
    if args.fixture != bool(args.plant) or (args.fixture and args.verb):
        ap.error("--fixture takes --plant <case> and no verb")
    if args.fixture:
        return run_transition_fixture(args.plant)
    if args.verb is None:
        ap.error("a verb, record or check, or --fixture --plant <case>")
    if args.verb == "check" and args.selftest != (args.build is None):
        ap.error("check takes --build <slug>, or --selftest alone")
    if args.verb == "check" and args.selftest:
        return run_selftest()
    pairs = {}
    for flag in ("fact", "field"):
        pairs[flag] = {}
        for text in getattr(args, flag, None) or []:
            k, eq, v = text.partition("=")
            if not (k and eq):
                ap.error("--%s takes k=v, and %r is not" % (flag, text))
            pairs[flag][k] = v
    root = pathlib.Path(args.root).absolute()
    try:
        if args.verb == "record":
            move, commit, wrote, line = write_transition(root, args.build, getattr(args, "from"), args.item,
                                                         args.outcome, args.witness, pairs["fact"], pairs["field"])
            for rel in wrote:
                print("%s: wrote %s" % (SAY, rel))
            print("%s: recorded · %s -> %s · %s" % (SAY, move["from"], move["to"], "commit %s" % commit[:8] if commit
                                                  else "no commit: the set stores neither trailer nor log"))
            if line:
                print(line)
            return 0
        lines, findings = check_transition_channels(args.build, root)
    except TransitionRefused as e:
        print("refused — %s" % e)
        return 1
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    except (ValueError, OSError) as e:
        print("%s: unanswered · %s" % (SAY, e))
        return 2
    for why in findings:
        print("%s: transition · %s" % (SAY, why))
    for line in lines:
        print(line)
    return 1 if findings or any(ln.startswith(("pending — ", "unstored — ")) for ln in lines) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
