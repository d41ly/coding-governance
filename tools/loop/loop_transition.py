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
table's `derive_move`, printing `refused — ...` and exiting 1 where no row holds it, and where Test's exit
into deploying (`TREE_GATED_MOVE`) carries no `--field tree=<hash>` whose full per-tree verdict, the
runner's `<common dir>/gate-verdict/<hash>`, reads GREEN (TOOL-dWitnessedBar-4 S6); resolves `--witness`
to HEAD or an ancestor of it, adding `stand-in=<owner>` where the item has a `[[stand-in]]` row and
`composition=<sha8>`, the commit HEAD names (`composition.py`, TOOL-dDeclaredLoop-26), which a `--field`
may not give; refuses a move into `designing` of a build whose claim body, as `claim.py`'s `read_claim_body`
reads this node's cache of `refs/gov/claims/<slug>`, says `disposition: patch` while `check_patch_ratified`
holds it under `patch.ratify` = `owner`, naming that key and the owner item, exit 2 (TOOL-dPlacedRequest-21
S6); adds `scenario=<tags>`, the scenarios the build runs under joined by `+`, and
`scenario-settled=<entries>` where a conflict settled, both derived by `scenario.py`'s
`derive_move_scenarios` and never given, printing `loop: scenario · unread · <why>` and recording neither
where the scenario composition at HEAD is unarmed (TOOL-dDeclaredLoop-27); refuses a staged index; where the build's previous move was pinned at another commit,
files `composition.py`'s `item-ended` orders, printing `loop: order · <path>` per order or
`loop: composition · unread · <why>` where the composition at HEAD does not answer; on a forward move
prints `adapt.py`'s path comparison, `loop: path · ...`, filing a `flow-deviation` order per deviation it
reads, and on a forward or backward move gives each pending flow change of the build its state row in
`RUN.md` under `flow.adapt`, the file staged beside the records and cut back to its length where the move
does not record (TOOL-dDeclaredLoop-28), and where a state row reads `applied` holds the composition the move
applies, its scenarios and applied changes at HEAD, to `termination.py`'s check, refusing the move on a
finding or a program `check_program` refuses, naming it (TOOL-dDeclaredLoop-33); back-fills, writes this move's record, commits the records, or an empty commit, as
`loop transition(<slug>): <from> -> <to>` with the trailer where selected, prints
`loop: recorded · <from> -> <to> · <direction> · commit <sha8>`, and prints the line where selected. A
set storing neither the trailer nor the log writes no commit. A backward move, testing to building say,
goes through this one writer, its channels and its fields as a forward move does: the direction is
`loop_table`'s `derive_direction`, derived on every print and read, and never stored. The rework budget
rides the same records (`budget.py`, TOOL-dDeclaredLoop-30): a backward move draws `route-back`, refused
before any write where the budget is spent, save on a row reading `draws = "none"`, an ending, which draws
nothing (TOOL-dDeclaredLoop-31); and the move from `designing` to `building` writes the freeze
row, once; each row is a line after the record's fields, the build's first record copying the rows before
it. Where the move writes no record its rows take the first home that exists (TOOL-dDeclaredLoop-48):
under a set without `log`, the build's newest record, staged into the move's commit, else the trailer's
derived `BUDGET_FIELDS`, `budget=` and `draw=`, where the set holds `trailer`; else run-state lines. With
none, a route-back is refused naming the build and the freeze writes nothing.

`check` (`check_transition_channels`) holds each channel to the trailer: per trailer whose commit's set
holds `log`, one record with equal `**Key:**` fields; no record left over where its adding commit's set
holds `trailer`; and the `transition` definition of the micro-format fence of `AGENTS.md` at `--root`
equal to `TRANSITION_LINE`. A record whose adding commit's set lacks `trailer` is its move's source.
It prints each finding as `loop: transition · ...`, naming the commit, the channel and the field;
`pending — <n> move(s) before the build's first spec` while trailers wait on a spec; `unstored — ...`
where the set at HEAD stores nothing; then its summary. `read_transitions(build, repo)` is the build's
moves newest first, from the trailer where one was written and from the record otherwise, each with
its `direction` derived over this kit's definition.

THE MAIL GUARD (KICK-dKeptSession-5 S9, S10): after the set is read and before the table answers, `record`
runs the unattended driver's `--mail read <slug>` once (`read_mail_rows`, under `MAIL_GUARD_SECONDS`). A
row reading `open`, a message addressed to the build or one of its units neither answered, acknowledged
nor past its deadline, refuses the move as `refused — <slug> · mail open <id> …`, exit 1, writing nothing
(`MailHeld`); a message this node first saw more than its `deadline` hours ago reads `expired`
(KICK-dKeptSession-24 S5), its asker's `default` the answer, and holds nothing. `mail — off`, no driver, or a root with no `.unattended.conf` passes with one `loop: mail ·
unarmed · <why>` line; a driver no bash sees, a read silent within the bound, or a non-zero read with no
row is `loop: unanswered · mail unknown: ...`, exit 2. Past the guard, each `answered`, `acked` or
`expired` row no earlier move names is recorded in the derived field `disposed=<id>+<id>`, and where the
set holds `log` one `mailbox-message` record per id is written after the move's own record and committed
with it (`write_mail_records`). `--fixture --plant mail-open` holds the refusal over an open question on
a bare remote, `mail-disposed` the disposal after its `ack` and a second move that disposes nothing, and
`mail-expired` the disposal of a question carrying `deadline: 30`, first sighted 31 hours ago and never
answered, its record's `State` reading `expired`.

Exit: `record` 0 recorded, 1 refused by the table or held by open mail; `check` 0 clean, 1 on a finding, `pending` or
`unstored`. Both exit 2 printing `loop: unanswered · <why>` on a value outside its grammar, a witness
that is not HEAD or its ancestor, a staged index, or a policy refusal naming `transitions.record`, an
empty set with no valid revision before it among them; and 2 printing `loop: unarmed · <why>` where the
policy or memory-tree kit does not resolve, never a default. The loop kit takes no edge to the policy
kit, which is why.

`--fixture --plant <case>` builds a scratch repository under the host temp directory holding the build
`tFix`, runs `record` and `check` there in process, prints each verdict, removes the scratch and exits
as its last verb. `field` records a `colour=red` move and a `composition=3f9c2a71` move, each refused,
then a plain move carrying its derived `composition`. `backward-rows` and `skip-backward` record `BACKWARD_MOVES`, three moves forward and
three back; the first prints every trailer and read with its direction, the second deletes the newest
record and owes its move's finding. `check --selftest` holds the definition of `AGENTS.md` in the
current directory, then runs every plant through `run_selftest_cases`, each plant once however many
cases read it.

WHAT THIS DOES NOT CHECK: that a witness holds beyond resolving; a record's lines after its fields; a
feature- or unit-level move; a charter other than the one `AGENTS.md`; an old move's direction against
the definition at its commit, since it is derived from today's. A record pairs with a trailer by
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
from loop_lib import read_definition, read_memory_tree, resolve_memory_root, run_selftest_cases  # noqa: E402
from loop_parents import read_policy_kit  # noqa: E402
from loop_table import (TransitionRefused, derive_direction, derive_move, read_stand_ins,  # noqa: E402
                        read_transition_rows)
from loop_witness import FIXTURE_REMOTE, read_git, remove_tree, resolve_commit, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "loop"
KEY = "transitions.record"
TRAILER_KEY = "Gov-Transition"
KIND = "transition"
#: The rework budget's fields (`budget.py`, TOOL-dDeclaredLoop-48), `budget=frozen@<units>@<total>` and
#: `draw=<cause>@<item>@<spent>+<total>`: the writer puts a move's rows on its trailer where the set holds
#: `trailer` and no `log` and the build holds no log record, and refuses either from a `--field`.
BUDGET_FIELDS = ("budget", "draw")
#: The extension fields a trailer and a record may carry after `build`, `item` and `sha`, in the order
#: they are written; later units extend it. `composition`, `scenario`, `scenario-settled`, the
#: `BUDGET_FIELDS` and `disposed`, the mail the move disposed (KICK-dKeptSession-5 S10), are derived by
#: the writer, never given; the `mail-open` and `mail-disposed` plants hold the guard and the disposal,
#: and `mail-expired` the disposal of a question past its deadline (KICK-dKeptSession-24 S5).
TRANSITION_FIELDS = ("stand-in", "composition", "scenario", "scenario-settled") + BUDGET_FIELDS + ("tree", "disposed")
#: The mail guard's bound in seconds on the unattended driver's `--mail read` (KICK-dKeptSession-5 S9),
#: twice the kickoff engine's claims read, since the guard fetches every build's mail refs.
MAIL_GUARD_SECONDS = 30
#: The first eleven columns of one `--mail read` row, in order (KICK-dKeptSession-5 S6), which the guard
#: reads; the row's later columns, `seq`, `after` and `content-key` (KICK-dKeptSession-27 S4), it does
#: not. Then the states a move disposes.
MAIL_COLUMNS = ("id", "kind", "to", "state", "first-seen", "from-build", "subject", "answers", "ref", "commit", "reply")
MAIL_DISPOSED_STATES = ("answered", "acked", "expired")
#: The record kind a disposed message is written as (KICK-dKeptSession-5 S12).
MAIL_KIND = "mailbox-message"
#: The move whose `tree` field must name a GREEN full per-tree verdict (TOOL-dWitnessedBar-4 S6): Test's
#: exit, `item.test.exit` from testing into deploying, and the runner's directory it reads under the
#: common dir.
TREE_GATED_MOVE = ("testing", "item.test.exit", "deploying")
VERDICT_DIR = "gate-verdict"
#: A tree hash, SHA-1 or SHA-256: the one shape that may name a file under the verdict directory.
TREE_HASH = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
#: The fields `scenario.py`'s `derive_move_scenarios` derives for each move (TOOL-dDeclaredLoop-27).
DERIVED_SCENARIO_FIELDS = ("scenario", "scenario-settled")
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
#: A spec's status header, its first word the unit's status.
STATUS_HEADER = re.compile(r"^\*\*Status:\*\* ([A-Z]+)", re.M)
#: That header's tier, the digits of its `Tier-<n>` (TOOL-dDeclaredLoop-19).
TIER_HEADER = re.compile(r"^\*\*Status:\*\* .*?\bTier-(\d+)", re.M)
FENCE =("<!-- microformats -->", "<!-- /microformats -->")
PLANTS = {"default": "the default set, one B4 move with its witness",
          "subset-trailer-line": "the set [\"trailer\", \"micro-format\"], one B4 move",
          "subset-log": "the set [\"log\"], one B4 move",
          "empty-set": "the set [], the policy file's one revision",
          "log-drift": "one B4 move, its record then edited to To: building",
          "orphan-log": "one B4 move, then a second record committed with no trailer",
          "no-row": "planning to building through item.design.exit, which no row holds",
          "line-drift": "an AGENTS.md whose definition drops <item tag>",
          "pre-spec": "a build with no spec moved once, then a spec planted and a second move",
          "field": "a move with --field colour=red, one with composition=3f9c2a71, refused as derived, then a plain move",
          "backward-rows": "B4, B5 and B7 forward, then B13, B8 and B6 back, each trailer and read printed",
          "skip-backward": "the six moves of backward-rows, then the newest record, B6's, deleted",
          "descope-spent": "flow.rework-budget = 0: B4, B5 and B7 forward, B13 back refused as spent, then "
                           "@any's descope from testing",
          "mail-open": "the driver's conf with RUN_CLAIMS on and a bare remote holding fy's question to build:tFix: "
                       "B4 refused naming it, no commit",
          "mail-disposed": "the same question and tFix's ack of it: B4 disposes it in one commit, its record read, "
                           "then B5 disposes nothing",
          "mail-expired": "the same question with deadline: 30 and default: no, first sighted 31 hours ago and "
                          "never answered: B4 disposes it as expired in one commit, its record read",
          "mail-argv": "the driver's conf with RUN_CLAIMS on and subprocess.run wrapped: B4's --mail read argv "
                       "recorded, answered zero rows, and held to the located driver and the bash that sees it",
          "mail-no-driver": "the driver's conf, the driver's locator run over an empty scratch directory: B4 "
                            "records with the mailbox unarmed",
          "mail-no-bash": "the driver's conf and resolve_bash answering None: B4 refused as mail unknown, no commit"}
#: The mail plants' messages, each `(ref, build, id, to, kind, subject, answers)`, put straight on the fixture's
#: remote; `mail-disposed` adds the ack. `mail-expired` writes the question with `FX_DEADLINE`'s two keys and
#: its first sighting `FX_SIGHTED_HOURS` back in the fixture's feed, past the 30-hour deadline.
FX_QUESTION = ("refs/gov/mail/fy/z/s-other", "fy", "a1b2c3d4e5f6", "build:tFix", "question", "the fixture's question", "none")
FX_ACK = ("refs/gov/mail/tFix/z/s-fx", "tFix", "0f1e2d3c4b5a", "build:fy", "ack", "the fixture's question", "a1b2c3d4e5f6")
FX_DEADLINE = {"deadline": "30", "default": "no"}
FX_SIGHTED_HOURS = 31
#: The moves the backward plants record in order, each an argv tail for `record` before its witness.
BACKWARD_MOVES = (("--from", "planning", "--item", "item.plan.exit", "--outcome", "recorded"),
                  ("--from", "designing", "--item", "item.design.exit", "--outcome", "recorded"),
                  ("--from", "building", "--item", "item.build.exit", "--outcome", "recorded"),
                  ("--from", "testing", "--item", "item.test.attribute", "--outcome", "code-miss"),
                  ("--from", "building", "--item", "item.build.unit-pass", "--outcome", "spec-wrong"),
                  ("--from", "designing", "--item", "item.design.decompose", "--outcome", "goal-fork"))
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


def resolve_build_anchor(build, root):
    """The lowest unit id a tracked spec H1 under `build` defines, by its number, or None."""
    ids = read_build_unit_ids(build, root)
    return min(ids, key=lambda i: (int(i.rsplit("-", 1)[1]), i), default=None)


def read_build_unit_ids(build, root):
    """The unit ids the tracked spec H1s under `build` define, in `git ls-files` order: the anchor's walk,
    and the units the rework budget counts at its freeze (`budget.py`)."""
    return [uid for uid, _status in read_build_specs(build, root)]


def read_build_specs(build, root):
    """`[(unit id, status)]` of each tracked spec H1 under `build`, in `git ls-files` order: the status the
    word its `**Status:**` header opens with, empty where it carries none, `read_build_headers`' pairs.
    `budget.py`'s ending reads the statuses (TOOL-dDeclaredLoop-31)."""
    return [(uid, status) for uid, status, _tier in read_build_headers(build, root)]


def read_build_headers(build, root):
    """`[(unit id, status, tier)]` of each tracked spec H1 under `build`, in `git ls-files` order: the status
    the word its `**Status:**` header opens with, the tier the digits of that header's `Tier-<n>`, each empty
    where the header carries none. `breakpoints.py` reads the tiers (TOOL-dDeclaredLoop-19)."""
    read_memory_tree("tree_lib.py")
    from design_lib import read_design_conf, read_tracked_builds
    from tree_lib import parse_spec_h1
    conf = read_design_conf(root)
    memory_root = resolve_memory_root(root)
    families = [p.split(":", 1)[1] for p in conf.get("FAMILIES", "").split() if ":" in p]
    prefix = "%s/builds/%s/spec/" % (memory_root, build)
    ids = []
    for rel in read_tracked_builds(root, memory_root):
        path = pathlib.Path(root, rel)
        if rel.startswith(prefix) and rel.endswith(".md") and path.is_file():
            text = path.read_bytes().decode("utf-8", "replace")
            hit = parse_spec_h1(rel, text, memory_root, families)
            if hit:
                status, tier = STATUS_HEADER.search(text), TIER_HEADER.search(text)
                ids.append((hit[1], status.group(1) if status else "", tier.group(1) if tier else ""))
    return ids


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
    folder = pathlib.Path(root, resolve_memory_root(root), "builds", build, "build")
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
    glob = "%s/builds/%s/build/*-%s-*.md" % (resolve_memory_root(root), build, KIND)
    adding = read_adding_commits(str(root), glob, [r["path"] for r in records])
    paired = [r for r in records if "trailer" in read_cached_channels(root, adding.get(r["path"], "HEAD"), cache)]
    return {"trailers": trailers, "owing": [(c, t) for c, t in trailers
                                            if "log" in read_cached_channels(root, c["sha"], cache)],
            "paired": paired, "sourced": [r for r in records if r not in paired], "adding": adding,
            "findings": findings}


def read_transitions(build, repo):
    """The build's recorded moves, newest first: each the fields of its trailer, or of its record where
    the move wrote no trailer, with `commit`, `source` (`trailer` or `log`) and `direction`, derived on
    read by `derive_direction` over this kit's definition and never stored. ValueError or OSError where a
    read is refused; LookupError where a kit does not resolve."""
    root = pathlib.Path(repo).absolute()
    tables = read_transition_rows(*read_definition(KIT))
    moves = read_transition_moves(build, root, {})
    out = [dict(t, commit=c["sha"], source="trailer") for c, t in moves["trailers"]]
    if moves["sourced"]:
        order = read_git(root, "rev-list", "--reverse", "HEAD")[1].split()
        at = {sha: n for n, sha in enumerate(order)}
        out += [dict(r["fields"], commit=moves["adding"].get(r["path"]), source="log") for r in moves["sourced"]]
        out.sort(key=lambda m: at.get(m["commit"], len(at)))
    for m in out:
        m["direction"] = derive_direction(m.get("from"), m.get("to"), tables)
    return out[::-1]


# ------------------------------------------------------------------------------------------ the writer
class TreeUnverified(TransitionRefused):
    """Test's exit asked for a tree no GREEN full per-tree verdict covers; the message names the tree."""

    def __init__(self, tree, why):
        Exception.__init__(self, "%s · tree %s: %s" % (TREE_GATED_MOVE[1], tree or "-", why))


def check_tree_verdict(root, tree):
    """None where the runner's full per-tree verdict `<common dir>/gate-verdict/<tree>` in the repository
    at `root` reads `verdict GREEN` for `tree`; else why not. WHAT IT DOES NOT CHECK: that `tree` is the
    one `verdict.tree` selects, the prepared merge's or the build tip's; the caller names it."""
    if not tree:
        return "the move names no tree; give --field tree=<tree hash>"
    if not TREE_HASH.fullmatch(tree):
        return "%s is no tree hash" % tree
    rc, common = read_git(root, "rev-parse", "--path-format=absolute", "--git-common-dir")
    if rc != 0 or not common:
        return "the git common dir of %s does not resolve" % root.as_posix()
    path = pathlib.Path(common, VERDICT_DIR, tree)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return "no full per-tree verdict at %s" % path.as_posix()
    keys = dict(ln.split("\t", 1) for ln in text.splitlines() if "\t" in ln)
    if keys.get("tree") != tree:
        return "%s names tree %s" % (path.as_posix(), keys.get("tree") or "none")
    if keys.get("verdict") != "GREEN":
        return "%s reads verdict %s, not GREEN" % (path.as_posix(), keys.get("verdict") or "none")
    return None


class MailHeld(TransitionRefused):
    """A message addressed to the build is open, neither answered, acknowledged nor past its deadline
    (KICK-dKeptSession-5 S9, KICK-dKeptSession-24 S5); the message names the build and every open id."""

    def __init__(self, build, ids):
        Exception.__init__(self, "%s · mail open %s · a message addressed to the build holds its moves until it is "
                                 "answered, acknowledged or past its deadline" % (build, " ".join(ids)))


def read_mail_rows(root, build):
    """The build's mailbox as the unattended driver's `--mail read <build>` prints it, run in `root` with stdin
    closed, under `read_clean_env()` and `MAIL_GUARD_SECONDS`, the bash `resolve_bash`'s, as `write_card_follow`
    runs the engine: `(rows, unarmed)`, each row a dict of `MAIL_COLUMNS`, `unarmed` why the mailbox was not
    read or None. Unarmed: the driver's locator answering LookupError, a `root` with no `.unattended.conf`,
    which launches nothing, and `mail — off`. ValueError, `mail unknown: ...`, for a driver no bash sees, a
    read silent within the bound, and any other non-zero read with no row: unknown, never none."""
    import subprocess
    import loop_witness
    from loop_lib import resolve_kit_dir
    try:
        driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
    except LookupError as e:
        return [], str(e)
    if not pathlib.Path(root, ".unattended.conf").is_file():
        return [], "no .unattended.conf at %s, so no driver reads its mailbox" % pathlib.Path(root).as_posix()
    bash = loop_witness.resolve_bash(driver.as_posix())
    if bash is None:
        raise ValueError("mail unknown: no bash that can see %s" % driver.as_posix())
    try:
        p = subprocess.run([bash, driver.as_posix(), "--mail", "read", build], cwd=str(root), stdin=subprocess.DEVNULL,
                           capture_output=True, encoding="utf-8", errors="replace", timeout=MAIL_GUARD_SECONDS,
                           env=loop_witness.read_clean_env())
    except subprocess.TimeoutExpired:
        raise ValueError("mail unknown: --mail read %s printed no answer within %ds" % (build, MAIL_GUARD_SECONDS)) from None
    except OSError as e:
        raise ValueError("mail unknown: --mail read %s did not start: %s" % (build, e)) from None
    lines = [ln.rstrip("\r") for ln in p.stdout.splitlines() if ln.strip()]
    rows = [dict(zip(MAIL_COLUMNS, ln.split("\t"))) for ln in lines if ln.count("\t") >= len(MAIL_COLUMNS) - 1]
    if lines[:1] == ["mail — off"]:
        return [], "mail — off"
    if p.returncode != 0 and not rows:
        raise ValueError("mail unknown: --mail read %s exited %d: %s" % (
            build, p.returncode, (lines or p.stderr.strip().splitlines() or ["no output"])[0]))
    return rows, None


def write_mail_records(root, build, anchor, rows):
    """One `mailbox-message` record per row under `anchor`, the build's anchor unit (KICK-dKeptSession-5 S12):
    its fields from the row, its body the message's text after its `key: value` block, read from the row's
    commit in `root`, in one `~~~~` fenced block. -> the records' repo-relative paths. ValueError where a
    commit does not read or the factory refuses a record."""
    read_memory_tree("build_records.py")
    from build_records import write_record
    out = []
    for r in rows:
        rc, text = read_git(root, "log", "-1", "--format=%B", r["commit"], "--")
        if rc != 0:
            raise ValueError("the message %s's commit %s does not read in %s" % (r["id"], r["commit"], root.as_posix()))
        lines = text.replace("\r\n", "\n").split("\n")
        at = next((i for i in range(2, len(lines)) if lines[i] == ""), len(lines))
        body = lines[at + 1:]
        while body and body[-1] == "":
            body.pop()
        fields = [(k.capitalize(), r[n]) for k, n in (("id", "id"), ("from", "from-build"), ("to", "to"),
                                                       ("kind", "kind"), ("subject", "subject"), ("answers", "answers"),
                                                       ("state", "state"), ("reply", "reply"), ("ref", "ref"))]
        out.append(write_record(root, build, anchor, MAIL_KIND, "%s %s" % (r["kind"], r["id"]), fields,
                                lines=["~~~~", *body, "~~~~"]))
    return out


def render_fixture_mail(build, mid, to, kind, subject, answers="none", deadline=None, default=None):
    """A mail commit's message as `KICK-dKeptSession-5`'s post recorded it, with no deadline, for a plant that puts
    one straight on its remote: the header, the ten keys, `from-tag` `z` and `from-session` `s-other`, and a
    one-line body; `deadline` and `default`, where given, append the two keys KICK-dKeptSession-24's post writes."""
    keys = (("id", mid), ("build", build), ("from-tag", "z"), ("from-session", "s-other"), ("to", to), ("kind", kind),
            ("item", "none"), ("pass", "none"), ("subject", subject), ("answers", answers))
    keys += tuple((k, v) for k, v in (("deadline", deadline), ("default", default)) if v is not None)
    return "gov-mail %s/%s\n\n%s\nthe fixture's message\n" % (build, mid, "".join("%s: %s\n" % kv for kv in keys))


def write_transition_record(root, anchor, move, lines=()):
    """The next transition record of the move's build, under `anchor`, from `move`'s fields, then `lines`,
    the rework budget's rows: its path."""
    read_memory_tree("build_records.py")
    from build_records import write_record
    names = ("build", "from", "to", "item", "sha") + tuple(n for n in TRANSITION_FIELDS if n in move)
    return write_record(root, move["build"], anchor, KIND, "%s -> %s" % (move["from"], move["to"]),
                        [(render_record_key(n), move[n]) for n in names], lines=tuple(lines))


def write_transition(root, build, state, item, outcome, witness, facts, fields):
    """Record one build move in the repository at `root`, an absolute path: `(move fields, the commit's
    sha or None, [record paths], the line or None, [order lines])`, the order lines `loop: order · <path>`
    per `item-ended` order or one `loop: composition · unread · <why>`, after a `loop: scenario · unread`
    line where the scenario composition is unarmed, then the build card follow's `card —` lines
    (`write_card_follow`, TOOL-dPlacedRequest-2 S4), a `loop: mail · unarmed` line first where the mailbox
    was not read. TransitionRefused where no row holds the move, `MailHeld` where a message addressed to the
    build is open; ValueError on a value, witness, index, policy read, tag resolver, scenario conflict or
    unknown mailbox refused, writing no record; LookupError where a kit it reads does not resolve."""
    from composition import PINNED, derive_composition_revision, read_step_composition, write_ended_orders
    from scenario import derive_move_scenarios   # it imports this module through composition.py, so here
    cache = {}
    chosen = read_cached_channels(root, "HEAD", cache)
    # the mail guard (KICK-dKeptSession-5 S9): one read of the build's mailbox, its open rows refusing the
    # move before any write and its answered and acknowledged rows disposed below; an unarmed mailbox is a line
    said = []
    mail, unarmed = read_mail_rows(root, build)
    if unarmed:
        said.append("%s: mail · unarmed · %s" % (SAY, unarmed))
    held = [r["id"] for r in mail if r.get("state") == "open"]
    if held:
        raise MailHeld(build, held)
    data, where = read_definition(KIT)
    row, to = derive_move("build", state, item, outcome, facts, read_transition_rows(data, where))
    if to == "designing":   # a placed patch waits on its owner's ratification (TOOL-dPlacedRequest-21 S6)
        from claim import PatchHeld, check_patch_ratified, read_anchor_unit, read_claim_body
        if read_claim_body(root, build).get("disposition") == "patch":
            held = check_patch_ratified(root, build)
            if held in ("held", "rejected"):
                raise PatchHeld("patch.ratify is owner and %s's patch is %s: the owner item ratify %s, item.entry.claim "
                                "disposed ratified under %s, releases the record into designing"
                                % (build, "rejected for good" if held == "rejected" else "unratified", build,
                                   read_anchor_unit(root, build)))
    sha = resolve_commit(root, witness)
    if sha is None:
        raise ValueError("--witness %s names no commit in %s" % (witness, root.as_posix()))
    if read_git(root, "merge-base", "--is-ancestor", sha, "HEAD")[0] != 0:
        raise ValueError("--witness %s is neither HEAD nor an ancestor of it" % witness)
    move = {"from": state, "to": to, "build": build, "item": item, "sha": sha[:8]}
    for name, value in fields.items():
        if name not in TRANSITION_FIELDS:
            raise ValueError("--field %s is no registered extension field: %s" % (name, " ".join(TRANSITION_FIELDS)))
        if name == "composition":
            raise ValueError("--field composition is derived: the writer sets it to the commit HEAD names, so it "
                             "is never given")
        if name in DERIVED_SCENARIO_FIELDS:
            raise ValueError("--field %s is derived: the writer places the build's scenarios from the move's facts "
                             "and the previous move, so it is never given" % name)
        if name in BUDGET_FIELDS:
            raise ValueError("--field %s is derived: the writer places the move's rework budget rows on the trailer "
                             "where no log record holds them, so it is never given" % name)
        if name == "disposed":
            raise ValueError("--field disposed is derived: the writer sets it to the mail the move disposes, so it is "
                             "never given")
        move[name] = value
    if (state, item, to) == TREE_GATED_MOVE:
        why = check_tree_verdict(root, move.get("tree"))
        if why:
            raise TreeUnverified(move.get("tree"), why)
    owner = {r.get("item"): r.get("owner") for r in read_stand_ins(data, where)}.get(item)
    if owner:
        move["stand-in"] = owner
    move["composition"] = derive_composition_revision(root)[:8]
    before = read_transitions(build, root)
    # the disposal (KICK-dKeptSession-5 S10): each answered, acknowledged or expired message no earlier move
    # names in `disposed`, joined by `+`, so the trailer and the log record both carry it
    done = {i for m in before for i in (m.get("disposed") or "").split("+") if i}
    disposing = [r for r in mail if r.get("state") in MAIL_DISPOSED_STATES and r.get("id") not in done]
    if disposing:
        move["disposed"] = "+".join(r["id"] for r in disposing)
    placed = derive_move_scenarios(root, state, facts, before)
    if placed is None:
        said.append("%s: scenario · unread · the scenario composition at HEAD answers unarmed, so the move records "
                    "no scenario" % SAY)
    else:
        move["scenario"] = placed[0]
        if placed[1]:
            move["scenario-settled"] = placed[1]
    bad = [n for n, v in move.items() if not (isinstance(v, str) and VALUE.fullmatch(v))]
    if bad:
        raise ValueError("the value of %s, %r, is outside [A-Za-z0-9._:+@-]+" % (bad[0], move[bad[0]]))
    if read_git(root, "diff", "--cached", "--quiet")[0] != 0:
        raise ValueError("the index holds staged changes, and a transition commit carries its own records alone")
    # the rework budget (TOOL-dDeclaredLoop-30): a backward move draws `route-back`, refused here before any
    # write where the budget is spent, and the move from designing to building freezes it, once. The rows
    # are lines of this move's record, the build's first record copying the rows before them, or, where the
    # move writes no record, the first home that exists (TOOL-dDeclaredLoop-48): under a set without log
    # the build's newest record, staged into this commit, else the trailer where the set holds trailer;
    # else run-state lines. A route-back draw with no home is refused, and a freeze with none writes nothing
    from adapt import read_adapt_mode, read_pending_rows, read_run_file, write_flow_states, write_path_orders
    # budget.py imports this module, so its names are imported here
    from budget import freeze_budget, read_budget_rows, record_draw, render_budget_fields, write_budget_rows
    direction = derive_direction(state, to, read_transition_rows(data, where))
    anchor = resolve_build_anchor(build, root) if "log" in chosen else None
    records = [] if "log" in chosen else read_transition_records(build, root)
    newest = pathlib.Path(root, records[-1]["path"]) if records else None
    on_trailer = "trailer" in chosen and "log" not in chosen
    run, rows = read_run_file(root, build), []
    homed = bool(anchor or newest or on_trailer or run.is_file())
    if direction == "backward" and row.get("draws") != "none":   # an ending row draws nothing (TOOL-dDeclaredLoop-31)
        answer, drawn = record_draw(build, "route-back", item, root, lines=rows, moves=before)
        if answer == "exhausted":
            raise ValueError("the rework budget is spent, %s, so the backward move is refused and nothing is "
                             "recorded; flow.on-exhausted names the ending" % drawn)
        if rows and not homed:
            raise ValueError("%s has neither a transition log record nor a run-state file, and %s holds no trailer "
                             "to carry it, so the route-back draw has no home" % (build, KEY))
    elif (state, to) == ("designing", "building"):
        rows += [r for r in (freeze_budget(build, root),) if r and homed]
    carried = read_budget_rows(build, root, before)["carried"] if anchor and not read_transition_records(
        build, root) else []
    pin, state_read = read_step_composition(root, before)
    if state_read == PINNED and not pin.startswith(move["composition"]):
        try:
            orders, unread = write_ended_orders(root, build, before)
        except LookupError as e:   # the writer answers an unanswered resolver exit 2, `unanswered`
            raise ValueError(str(e)) from None
        said += ["%s: order · %s" % (SAY, p) for p in orders]
        said += ["%s: composition · unread · %s" % (SAY, unread)] if unread else []
    # the build's own flow changes at this boundary (TOOL-dDeclaredLoop-28): the walked path held to the
    # composition on a forward move, then each pending change given its state row in RUN.md, which rides
    # this move's commit and is cut back to its length here where the move does not record
    if direction == "forward":
        said += write_path_orders(root, build, state)
    size, written = None, []
    if direction in ("forward", "backward") and read_pending_rows(root, build):
        mode = read_adapt_mode(root)
        size = run.stat().st_size
        written = write_flow_states(root, build, mode)
    staged = [run.relative_to(root).as_posix()] if size is not None else []
    wrote, prior = [], None
    try:
        # a change applied here is held to the termination check over the composition this move applies, its
        # scenarios and its applied changes at HEAD; a finding, or a program check_program refuses, refuses the
        # move, RUN.md cut back below (TOOL-dDeclaredLoop-33)
        if any(" · applied · " in line for line in written):
            from termination import check_termination, read_termination_inputs, render_finding
            try:
                found = check_termination(read_termination_inputs(root, build, [move] + before))
            except LookupError as e:
                raise ValueError("the termination check is unarmed, so the move applying a flow change is refused: "
                                 "%s" % e) from None
            except ValueError as e:
                raise ValueError("the build's composition does not read, so the move applying a flow change is "
                                 "refused: %s" % e) from None
            if found:
                raise ValueError("the termination check refuses the move applying a flow change: %s" % "; ".join(
                    render_finding(f) for f in found))
        if "log" in chosen:
            if anchor is None and "trailer" not in chosen:
                raise ValueError("%s selects log without trailer and %s defines no spec, so the move has no record "
                                 "to write and no trailer to back-fill one from" % (KEY, build))
            if anchor:
                moves = read_transition_moves(build, root, cache)
                try:
                    for _c, t in moves["owing"][len(moves["paired"]):]:
                        wrote.append(write_transition_record(root, anchor, t, () if wrote else carried))
                    wrote.append(write_transition_record(root, anchor, move, ([] if wrote else carried) + rows))
                    # one record per disposed message after this move's own, staged by the one commit below
                    wrote += write_mail_records(root, build, anchor, disposing)
                except (ValueError, OSError):
                    for rel in wrote:
                        pathlib.Path(root, rel).unlink()
                    raise
        if rows and not wrote and newest:   # its bytes written back below where the move does not commit
            prior = newest.read_bytes()
            write_budget_rows(newest, rows, True)
            staged.append(newest.relative_to(root).as_posix())
        elif rows and not wrote and on_trailer:
            move.update(render_budget_fields(rows))
        elif rows and not wrote:
            size = run.stat().st_size if size is None else size
            write_budget_rows(run, rows, False)
            staged = [run.relative_to(root).as_posix()]
        commit = None
        if wrote or "trailer" in chosen:
            argv = ["commit", "-q", "--allow-empty", "-m", "loop transition(%s): %s -> %s" % (build, state, to)]
            argv += ["-m", render_transition_trailer(move)] if "trailer" in chosen else []
            if ((wrote or staged) and read_git(root, "add", "--", *wrote, *staged)[0] != 0) \
                    or read_git(root, *argv)[0] != 0:
                if wrote or staged:
                    read_git(root, "reset", "-q", "--", *wrote, *staged)
                for rel in wrote:
                    pathlib.Path(root, rel).unlink()
                raise ValueError("git could not commit the move in %s, so nothing is recorded" % root.as_posix())
            commit = read_git(root, "rev-parse", "HEAD")[1]
    except (ValueError, OSError):
        if size is not None:
            with open(run, "r+b") as fh:
                fh.truncate(size)
        if prior is not None:
            newest.write_bytes(prior)
        raise
    # the build's card follows the move, its last step (TOOL-dPlacedRequest-2 S4); the move stands whatever it prints
    said += write_card_follow(root, build, to, to in read_transition_rows(data, where)["terminal"])
    return move, commit, wrote, render_transition_line(move) if "micro-format" in chosen else None, said


#: The kickoff engine the card follow runs, homed as the roles kit's handoff finds it (TOOL-dPlacedRequest-2 S4).
KICKOFF_HOME, KICKOFF_ENGINE = "session-kickoff", "manifest-check.sh"
#: The follow's bound in seconds: the engine's own reads and its push are each bounded inside it.
CARD_FOLLOW_BOUND_S = 120


def resolve_kickoff_engine(root):
    """The kickoff engine, an optional sibling: through the inline kit resolver from this kit, else the ONE
    file of that name `root` tracks, since gov homes that kit under `skills/`, where no probe walks. None
    when neither answers, or the index names two."""
    from loop_lib import resolve_kit_dir
    try:
        return resolve_kit_dir(KICKOFF_HOME, KICKOFF_ENGINE, KIT) / KICKOFF_ENGINE
    except LookupError:
        pass
    rc, out = read_git(root, "ls-files", "--", KICKOFF_ENGINE, "*/" + KICKOFF_ENGINE)
    hits = [ln for ln in out.splitlines() if ln.strip()] if rc == 0 else []
    return pathlib.Path(root, hits[0]) if len(hits) == 1 and pathlib.Path(root, hits[0]).is_file() else None


def write_card_follow(root, build, state, terminal):
    """The build card follows a recorded move: `manifest-check.sh --card --follow --build <build> --to <state>`,
    `--terminal` where the state is in the `terminal` set, run in `root` with stdin closed and a bound. ->
    its printed lines, or one `card — skipped:` line where no engine or bash resolves or the run does not
    answer. Never raises: the move stands whatever the card does."""
    import subprocess
    from loop_witness import read_clean_env, resolve_bash
    engine = resolve_kickoff_engine(root)
    if engine is None:
        return ["card — skipped: no kickoff engine"]
    bash = resolve_bash(engine.as_posix())
    if bash is None:
        return ["card — skipped: no bash runs the kickoff engine %s" % engine.as_posix()]
    argv = [bash, engine.as_posix(), "--card", "--follow", "--build", build, "--to", state]
    try:
        p = subprocess.run(argv + ["--terminal"] * bool(terminal), cwd=str(root), stdin=subprocess.DEVNULL,
                           capture_output=True, encoding="utf-8", errors="replace", timeout=CARD_FOLLOW_BOUND_S,
                           env=read_clean_env())
    except (OSError, subprocess.SubprocessError) as e:
        return ["card — skipped: the follow did not answer: %s" % e]
    lines = [ln for ln in p.stdout.splitlines() if ln.strip()]
    if p.returncode != 0 and not lines:
        lines = ["card — skipped: the follow exited %d: %s" % (p.returncode, (p.stderr.strip() or "no output").split("\n")[0])]
    return lines


# ------------------------------------------------------------------------------------------ the check
def check_transition_channels(build, root):
    """`(lines, findings)` of the build's channels held to its trailers, and the definition held to
    `TRANSITION_LINE`: `lines` the `pending` or `unstored` line and the summary. ValueError or OSError
    where a read is refused; LookupError where a kit does not resolve."""
    cache = {}
    head = read_cached_channels(root, "HEAD", cache)
    findings = check_transition_definition(root)
    if not head & {"trailer", "log"}:
        return derive_floor_report(root, [
            "unstored — %s · %s selects %s at HEAD, which stores no move" % (build, KEY, " ".join(sorted(head))),
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
    return derive_floor_report(root, lines, findings)


def derive_floor_report(root, lines, findings):
    """`(lines, findings)` as the check owes them, or, where a finding, a `pending` or an `unstored` line
    stands and `floor.record-changes` reads `off` at `root`'s landed revision (TOOL-dDeclaredLoop-2 S14),
    `floor: record-changes off` and each of them reported as a line, with no finding left to exit on."""
    held = [ln for ln in lines if ln.startswith(("pending — ", "unstored — "))]
    if not (findings or held):
        return lines, findings
    from floor import read_floor
    if read_floor(root)["record-changes"] != "off":
        return lines, findings
    return (["floor: record-changes off"] + ["%s: reported · %s" % (SAY, f) for f in findings]
            + [("%s: reported · %s" % (SAY, ln)) if ln in held else ln for ln in lines]), []


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
    if case == "descope-spent":
        files[".governance/policy.toml"] = "[flow]\nrework-budget = 0\n"
    if case.startswith("mail-"):   # the driver's conf, RUN_CLAIMS on, as the placement plants copy it
        src = next((d for d in (KIT, *KIT.parents) if (d / ".unattended.conf").is_file()), None)
        if src is None:
            raise LookupError("the mail plants copy .unattended.conf from this tree, which holds none")
        files[".unattended.conf"] = (src / ".unattended.conf").read_text(encoding="utf-8") + \
            '\nSPEC_TOKENS_CLI=""\nRUN_CLAIMS="on"\n'
    write_fixture_files(top, files)
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "fixture")
    if case in ("mail-open", "mail-disposed", "mail-expired"):   # a bare remote inside the git dir, so the scratch's removal takes it too
        from placement import write_fixture_gov_ref
        origin = top / ".git" / "fx-origin.git"
        run_fixture_git(top, "init", "-q", "--bare", "--template=", str(origin))
        run_fixture_git(top, "remote", "add", FIXTURE_REMOTE, str(origin))
        run_fixture_git(top, "push", "-q", FIXTURE_REMOTE, "main")
        for ref, *mail in (FX_QUESTION, FX_ACK) if case == "mail-disposed" else (FX_QUESTION,):
            write_fixture_gov_ref(top, ref, render_fixture_mail(*mail, **(FX_DEADLINE if case == "mail-expired" else {})))
        if case == "mail-expired":
            # its first sighting, the six-field line `claim.py`'s stale-holder plant writes for a lease: the commit
            # the remote holds, seen FX_SIGHTED_HOURS back. The driver's sightings walk appends its own line for
            # the tip at the read, after this one, and the first line of a ref and commit is the one it ages
            import datetime
            ref = FX_QUESTION[0]
            sha = run_fixture_git(top, "ls-remote", FIXTURE_REMOTE, ref).split("\t", 1)[0]
            feed = pathlib.Path(run_fixture_git(top, "rev-parse", "--path-format=absolute", "--git-common-dir")) / "gov-feed.log"
            rows = feed.read_text(encoding="utf-8").splitlines() if feed.exists() else []
            seq = max([int(r.split("\t", 1)[0]) for r in rows if r.split("\t", 1)[0].isdigit()] or [0]) + 1
            ago = (datetime.datetime.now(datetime.timezone.utc)
                   - datetime.timedelta(hours=FX_SIGHTED_HOURS)).strftime("%Y-%m-%dT%H:%M:%SZ")
            with feed.open("a", encoding="utf-8", newline="\n") as fh:
                fh.write("%d\t%s\tmail\t%s\t%s\t%s\n" % (seq, ref, run_fixture_git(top, "rev-parse", sha + "^{tree}"), sha, ago))
    return run_fixture_git(top, "rev-parse", "HEAD")


def run_transition_fixture(case):
    """`record` and `check` over a scratch repository planted as `case`: the last verb's exit."""
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

        if case == "descope-spent":   # the ending row E5 records a backward move on a spent budget, drawing nothing
            for n, tail in enumerate(BACKWARD_MOVES[:3]):
                run_verb(["record", *at, *tail, "--witness", "HEAD" if n else witness])
            before = read_count()
            refused = run_verb(["record", *at, *BACKWARD_MOVES[3], "--witness", "HEAD"])
            kept = read_count() == before
            rc = run_verb(["record", *at, "--from", "testing", "--item", "@any", "--outcome", "descope", "--witness", "HEAD"])
            from budget import read_budget_rows   # it imports this module, so here
            held, moves = read_budget_rows(FX_BUILD, top), read_transitions(FX_BUILD, top)
            print("%s: fixture · rows %s" % (SAY, " | ".join(held["rows"]) or "none"))
            misses = [why for ok, why in (
                (refused == 2 and kept, "the backward move on item.test.attribute's code-miss was not refused"),
                (rc == 0 and bool(moves) and (moves[0]["from"], moves[0]["to"], moves[0]["item"]) == (
                    "testing", "building", "@any"), "the descope did not record testing -> building on @any"),
                (not held["draws"], "the descope drew a row")) if not ok]
            print("%s: fixture · descope-spent · %s" % (SAY, "held" if not misses else "MISSED " + "; ".join(misses)))
            return 0 if not misses else 1
        if case == "mail-open":   # KICK-dKeptSession-5 AC6: the open question refuses B4, writing nothing
            before = read_count()
            rc = run_verb(b4)
            print("%s: fixture · commits %s" % (SAY, "unchanged" if read_count() == before else "changed"))
            return rc
        if case in ("mail-disposed", "mail-expired"):   # KICK-dKeptSession-5 AC6: B4 disposes the acknowledged
            # question in one commit; KICK-dKeptSession-24 AC2: B4 disposes the question past its deadline, never
            # answered, as expired
            read_memory_tree("build_records.py")
            import build_records
            before = read_count()
            moved = run_verb(b4)
            files = [p for p in run_fixture_git(top, "show", "--format=", "--name-only", "HEAD").splitlines() if p]
            mails = [p for p in files if "-%s-" % MAIL_KIND in p]
            print("%s: fixture · commits %d · %d file(s) · %d %s record(s)" % (
                SAY, int(read_count()) - int(before), len(files), len(mails), MAIL_KIND))
            print("%s: fixture · trailer %s" % (SAY, run_fixture_git(top, "log", "-1", "--format=%%(trailers:key=%s,valueonly)"
                                                                      % TRAILER_KEY) or "none"))
            for rec in read_folder():
                print("%s: fixture · record %s-%d · disposed %s" % (SAY, KIND, rec["n"], rec["fields"].get("disposed", "none")))
            for rel in mails:
                out = io.StringIO()
                with contextlib.redirect_stdout(out):
                    rc = build_records.main(["read", str(top / rel)])
                text = (top / rel).read_text(encoding="utf-8")
                serves, state = (re.search(r"^%s$" % p, text, re.M) for p in (r"\*\*Serves:\*\* (.+)", r"- \*\*State:\*\* (.+)"))
                print("%s: fixture · %s · read exit %d · Serves %s · State %s" % (
                    SAY, rel, rc, serves.group(1) if serves else "none", state.group(1) if state else "none"))
            if case == "mail-expired":
                return moved
            run_verb(["record", *at, *BACKWARD_MOVES[1][:6], "--witness", "HEAD"])
            value = run_fixture_git(top, "log", "-1", "--format=%%(trailers:key=%s,valueonly)" % TRAILER_KEY)
            print("%s: fixture · next move · %s" % (SAY, "disposes again: " + value if "disposed=" in value else "disposes nothing"))
            return run_verb(["check", *at])
        if case in ("mail-argv", "mail-no-driver", "mail-no-bash"):   # KICK-dKeptSession-36 S4: the guard's launch
            import subprocess   # each plant rebinds the name the guard imports inside its function, then restores it
            import loop_lib
            import loop_witness
            spawned, real_run, real_locate = [], subprocess.run, loop_lib.resolve_kit_dir
            empty = top / ".git" / "fx-empty"   # inside the git dir, so the scratch's removal takes it too
            empty.mkdir()

            def run_mail_spawn(argv, *rest, **kw):   # the one --mail call recorded and answered zero rows
                if "--mail" in [str(a) for a in argv]:
                    spawned.append([str(a) for a in argv])
                    return subprocess.CompletedProcess(argv, 0, "", "")
                return real_run(argv, *rest, **kw)

            def resolve_empty_kit(home, anchor, here):   # the driver's locator over an empty scratch directory
                return real_locate(home, anchor, empty if (home, anchor) == ("unattended", "unattended.sh") else here)

            def resolve_no_bash(script):
                return None
            owner, name, stand_in = {"mail-argv": (subprocess, "run", run_mail_spawn),
                                     "mail-no-driver": (loop_lib, "resolve_kit_dir", resolve_empty_kit),
                                     "mail-no-bash": (loop_witness, "resolve_bash", resolve_no_bash)}[case]
            real, before = getattr(owner, name), read_count()
            setattr(owner, name, stand_in)
            try:
                rc = run_verb(b4)
            finally:
                setattr(owner, name, real)
            if case == "mail-no-bash":
                print("%s: fixture · commits %s" % (SAY, "unchanged" if read_count() == before else "changed"))
            if case != "mail-argv":
                return rc
            try:
                driver = (real_locate("unattended", "unattended.sh", KIT) / "unattended.sh").as_posix()
            except LookupError as e:
                driver = "unlocated: %s" % e
            got = spawned[0] if len(spawned) == 1 else ["none"] * 3
            misses = [why for ok, why in (
                (len(spawned) == 1, "%d --mail call(s) recorded, not one" % len(spawned)),
                (got[1] == driver, "argv[1] is not the located driver %s" % driver),
                (len(spawned) == 1 and got[0] == loop_witness.resolve_bash(got[1]), "argv[0] is not resolve_bash(argv[1])"),
                (got[2:] == ["--mail", "read", FX_BUILD], "the rest is not --mail read %s" % FX_BUILD),
                (rc == 0, "the move did not record")) if not ok]
            print("%s: fixture · mail-argv · %s" % (SAY, "held" if not misses else "MISSED %s · argv %s" % (
                "; ".join(misses), spawned or "none")))
            return 0 if not misses else 1
        if case in ("no-row", "empty-set"):
            before = read_count()
            argv = b4 if case == "empty-set" else b4[:7] + ["--item", "item.design.exit"] + b4[9:]
            rc = run_verb(argv)
            print("%s: fixture · commits %s" % (SAY, "unchanged" if read_count() == before else "changed"))
            return rc if case == "no-row" else run_verb(["check", *at])
        if case == "field":
            run_verb(b4 + ["--field", "colour=red"])
            run_verb(b4 + ["--field", "composition=3f9c2a71"])
            run_verb(b4)
        elif case in ("backward-rows", "skip-backward"):
            for n, tail in enumerate(BACKWARD_MOVES):
                run_verb(["record", *at, *tail, "--witness", "HEAD" if n else witness])
        else:
            run_verb(b4)
        span = "--reverse" if case == "backward-rows" else "-1"
        values = [v for v in run_fixture_git(top, "log", span, "--format=%%(trailers:key=%s,valueonly)" % TRAILER_KEY)
                  .splitlines() if v]
        for value in values or ["none"]:
            print("%s: fixture · trailer %s" % (SAY, value))
        recs = read_folder()
        if case == "default" and recs:
            read_memory_tree("build_records.py")
            import build_records
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rc = build_records.main(["read", str(top / recs[0]["path"])])
            print("%s: fixture · build_records read · exit %d · %d field(s)" % (SAY, rc, out.getvalue().count("\n")))
        if case in ("subset-log", "field", "backward-rows"):
            for m in read_transitions(FX_BUILD, top):
                print("%s: fixture · read %s · %s · %s" % (
                    SAY, m["source"], render_transition_trailer(m).split(": ", 1)[1], m["direction"]))
        if case == "backward-rows":
            held = [r for r in recs if "direction" in (top / r["path"]).read_bytes().decode("utf-8", "replace")]
            print("%s: fixture · direction stored · %d trailer(s) · %d record(s)" % (
                SAY, sum("direction" in v for v in values), len(held)))
        if case == "skip-backward" and recs:
            (top / recs[-1]["path"]).unlink()
            write_commit("the newest record, B6's, deleted")
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
             ("field derived", fx("field"), 0, "%s: unanswered" % SAY, "composition is derived"),
             ("field trailer", fx("field"), 0, trailer, " · composition="),
             ("field read", fx("field"), 0, "%s: fixture · read trailer · " % SAY, " · composition="),
             ("field check", fx("field"), 0, check, "· 0 finding(s)"),
             ("backward-rows trailer", fx("backward-rows"), 0, "%s: fixture · trailer testing -> building · build=%s · "
              "item=item.test.attribute · sha=" % (SAY, FX_BUILD), " · stand-in=dWitnessedBar"),
             ("backward-rows records", fx("backward-rows"), 0, "%s: fixture · records 6" % SAY,
              "transition-6 designing -> planning"),
             ("backward-rows recorded", fx("backward-rows"), 0, "%s: recorded · testing -> building · backward" % SAY,
              ""),
             ("backward-rows read", fx("backward-rows"), 0, "%s: fixture · read trailer · designing -> planning" % SAY,
              " · backward"),
             ("backward-rows stored", fx("backward-rows"), 0,
              "%s: fixture · direction stored · 0 trailer(s) · 0 record(s)" % SAY, ""),
             ("backward-rows check", fx("backward-rows"), 0, check, "· 0 finding(s)"),
             ("skip-backward", fx("skip-backward"), 1, "%s: transition · commit " % SAY,
              "· log · the move designing -> planning owes a record, and none holds it"),
             ("descope-spent refused", fx("descope-spent"), 0, "%s: unanswered · the rework budget is spent" % SAY, ""),
             ("descope-spent", fx("descope-spent"), 0, "%s: fixture · descope-spent · held" % SAY, ""),
             ("mail-open", fx("mail-open"), 1, "refused — %s · mail open %s" % (FX_BUILD, FX_QUESTION[2]), ""),
             ("mail-open commits", fx("mail-open"), 1, "%s: fixture · commits unchanged" % SAY, ""),
             ("mail-disposed commit", fx("mail-disposed"), 0, "%s: fixture · commits 1 · " % SAY,
              "1 %s record(s)" % MAIL_KIND),
             ("mail-disposed trailer", fx("mail-disposed"), 0, trailer, " · disposed=%s" % FX_QUESTION[2]),
             ("mail-disposed log", fx("mail-disposed"), 0, "%s: fixture · record %s-1 · disposed %s" % (
                 SAY, KIND, FX_QUESTION[2]), ""),
             ("mail-disposed record", fx("mail-disposed"), 0, "%s: fixture · memory/builds/%s/build/" % (SAY, FX_BUILD),
              "%s-1.md · read exit 0 · Serves %s %s · State acked" % (MAIL_KIND, MAIL_KIND, FX_UNIT)),
             ("mail-disposed next", fx("mail-disposed"), 0, "%s: fixture · next move · disposes nothing" % SAY, ""),
             ("mail-disposed check", fx("mail-disposed"), 0, check, "· 0 finding(s)"),
             ("mail-expired recorded", fx("mail-expired"), 0, "%s: recorded · planning -> designing" % SAY, ""),
             ("mail-expired commit", fx("mail-expired"), 0, "%s: fixture · commits 1 · " % SAY,
              "1 %s record(s)" % MAIL_KIND),
             ("mail-expired trailer", fx("mail-expired"), 0, trailer, " · disposed=%s" % FX_QUESTION[2]),
             ("mail-expired record", fx("mail-expired"), 0, "%s: fixture · memory/builds/%s/build/" % (SAY, FX_BUILD),
              "%s-1.md · read exit 0 · Serves %s %s · State expired" % (MAIL_KIND, MAIL_KIND, FX_UNIT)),
             ("mail-argv", fx("mail-argv"), 0, "%s: fixture · mail-argv · held" % SAY, ""),
             ("mail-no-driver", fx("mail-no-driver"), 0,
              "%s: mail · unarmed · no unattended kit holding unattended.sh in this install" % SAY, ""),
             ("mail-no-driver recorded", fx("mail-no-driver"), 0, "%s: recorded · planning -> designing" % SAY, ""),
             ("mail-no-bash", fx("mail-no-bash"), 2, "%s: unanswered · mail unknown: no bash that can see " % SAY,
              "unattended.sh"),
             ("mail-no-bash commits", fx("mail-no-bash"), 2, "%s: fixture · commits unchanged" % SAY, "")]
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
            move, commit, wrote, line, said = write_transition(root, args.build, getattr(args, "from"), args.item,
                                                               args.outcome, args.witness, pairs["fact"], pairs["field"])
            for text in said:
                print(text)
            for rel in wrote:
                print("%s: wrote %s" % (SAY, rel))
            direction = derive_direction(move["from"], move["to"], read_transition_rows(*read_definition(KIT)))
            print("%s: recorded · %s -> %s · %s · %s" % (
                SAY, move["from"], move["to"], direction,
                "commit %s" % commit[:8] if commit else "no commit: the set stores neither trailer nor log"))
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
