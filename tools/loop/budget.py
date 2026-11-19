#!/usr/bin/env python3
"""budget.py — a build's rework budget: one per build, frozen at Design's exit, drawn by every repetition and never by contention (TOOL-dDeclaredLoop-30).

    python budget.py draw --build <slug> --cause <cause> --item <item>
    python budget.py value
    python budget.py target --build <slug> --item <item>
    python budget.py ending --build <slug> [--explain]
    python budget.py origin --build <slug>
    python budget.py --fixture --plant <case>
    python budget.py --selftest

THE VALUE. `flow.rework-budget` is `<base>+<per-unit>`, or a bare count, a base with no per-unit share,
default `4+2`; `flow.route-backs` is a count, default 3. Both are read at HEAD through the policy kit's
`resolve`, the kit found by `loop_parents.py`'s `read_policy_kit`, and the catalogue's own pattern
refuses a value of another shape. Each row declares `raise-loosens`, so raising either is the owner's.

THE ROWS. A build's budget is the rows of its transition log records (`loop_transition.py`), each
record's lines after its fields, read in record order:

    budget · frozen · <units> unit(s) · <total>
    draw · <cause> · <item> · <spent>/<total> · <draw-id>

`total` is the freeze row's figure, else the base; `spent` is the count of draw rows, re-derived from
the rows alone. The draw id, `<UTC yyyymmddThhmmssZ>-<6 hex>`, is minted once per draw and written on
every home of that draw, so two worktrees making the same draw append two distinct rows that a union
merge keeps both of; rows carrying one id count as one draw, and a row written before the id, which
carries none, counts as its own (TOOL-dDeclaredLoop-61). A draw row's typed `spent` is what its writer counted, and two worktrees drawing at once
each count their own, so a row whose typed figure is not its ordinal is named in the reader's
`disagree` list and refuses nothing (TOOL-dDeclaredLoop-49); the typed `total` is not compared, since a
row drawn before the freeze carries the base. Before the build's first log record the
same rows sit in three homes (TOOL-dDeclaredLoop-48): its run-state file and each record the driver's
preflight rotated beside it, `RUN.<phase>.<blob8>.md`, an aborted or abandoned run's as a landed one's
(TOOL-dDeclaredLoop-60), each row prefixed by its UTC timestamp; the `budget` and `draw` fields of
its `Gov-Transition` trailers, `budget=frozen@<units>@<total>` and `draw=<cause>@<item>@<spent>+<total>`,
the `draw=` field carrying no id since its commit is its identity, each stamped with its commit's committer date in UTC (`read_trailer_rows`); and each row of a `RUN.md`
or a rotated record under the memory root's `builds/` folders suffixed ` · budget <slug>` after its id, read without the suffix, a
suffixed row counting for the build it names and never for its file's own. They are read oldest first
by UTC second, a tie broken by the typed `spent` with a freeze row first, and the transition writer
copies them into the first record it writes.

THE ROOT. A build's records are read under the root `resolve_memory_root` answers: the `MEMORY_ROOT` of
the driver's `.unattended.conf` wherever that file exists, because the unattended driver writes each
run-state file under its own root (`unattended.sh`'s `scaffold_runmd`), else `.memory-tree.conf`'s, and
two confs that name two roots refuse, `records root:`, before anything is read (TOOL-dDeclaredLoop-75 S5).

THE FREEZE. `freeze_budget` answers the row the transition writer writes on the move `designing` to
`building`: the base plus the per-unit share for each unit a tracked spec H1 of the build defines, once,
since a build holding a freeze row in any home writes no second. A build no recorded move names freezes
at its first draw made while it defines a spec, counting its units then.

THE DRAW. `record_draw(build, cause, item)` writes one draw row, the freeze row first where one is owed,
and answers `drawn`; once spent equals total it writes nothing and answers `exhausted`, and the build
ends as `flow.on-exhausted` names. The cause is one of `CAUSES`, and `patch:<slug>` is
derived, never given: a build whose newest recorded move carries `scenario.patch` draws on the first
build its README's `parents:` names, as `patch:<its slug>`. `draw` appends the rows to the build's
newest log record and commits that record alone, its subject `loop budget(<slug>): <cause> <spent>/<total>`,
or, with no log record, appends them to the run-state file (`write_budget_rows`), under any
`transitions.record` set; a build with neither refuses the draw. Where the originating build of a patch
draw holds no log record and the set holds no `log`, the rows go to the patch build's own run-state
file, each suffixed ` · budget <origin>`, and a patch build with none refuses the draw. The transition
writer's rows under a set without `log` take `render_budget_fields`. `classify_repeat` answers `contention` for a repetition
another build or the remote caused, which draws nothing; `count_returns` counts one item's draws against
`flow.route-backs`, a spec subject's `review-round` draws never ending its loop; `promotion_target` answers
`unit`, `ask` or `on-exhausted`; `budget_state` answers `open <spent>/<total>`, `spent` or
`unfrozen <spent>/<total>`.

THE ENDING (TOOL-dDeclaredLoop-31). `derive_ending(value, units)` answers the ending a spent budget takes
under `flow.on-exhausted`'s `value`, `units` each unit's status: `park-for-owner` and `close-incomplete`
answer themselves; `best-effort-ending`, the default, answers `land-green` where every unit not `WONTDO`
is `CLOSED` and one is, `descope` where some unit is `CLOSED`, else `close-incomplete`. `read_ending`
answers the ending line from one `read_budget_rows` read, the value at HEAD, each spec's status header
through `loop_transition.py`'s `read_build_specs`, and the owner's newest disposition record of
`EXHAUSTED_ITEM` through `adapt.py`'s `read_disposition_release`.

Exit: `draw` prints `loop: budget · drawn · <row>` and exits 0, `loop: budget · exhausted · <slug> ·
<spent>/<total> · flow.on-exhausted` and exits 3, `loop: budget · refused · <why>` and exits 2, and
`loop: unarmed · <why>`, exit 2, where the policy or memory-tree kit does not resolve, never a default.
After a `drawn` or `exhausted` verdict, one `loop: budget · disagrees · <row> · typed <a>, derived <b>`
line per disagreeing row of the build drawn on, in the order read, so the verdict stays the first line.
`value` prints `base <n> per-unit <n>`. `target` prints `loop: budget · target · <answer>`, exit 0,
`promotion_target`'s answer for a blocking item as the budget stands, `unit` or `on-exhausted`, which
the unattended driver reads after a round's draw (TOOL-dDeclaredLoop-32); it draws nothing. `ending` prints
`loop: budget · ending · <ending|none> · <open|unfrozen|spent> <spent>/<total> · open <ids|none> ·
disposed <word|unrecorded>`, exit 0, the ending `derive_ending`'s where the state is `spent` and `none`
otherwise, the ids the units whose status is neither `CLOSED` nor `WONTDO`; the unattended driver's
`--exhausted` reads it. With `--explain` it prints first `loop: budget · root <root> · from
<.unattended.conf|.memory-tree.conf|default>`, the pair `resolve_memory_root_source` answers, then one
`loop: budget · read <path>` line per entry of `read_budget_rows`' `read`, or `loop: budget · read none`,
then one `loop: budget · no draw id · <row>` line per draw row read with no draw id, which counts as its
own draw (TOOL-dDeclaredLoop-75 S2, S7). `origin` prints `loop: budget · origin · <slug|none>`, exit 0, the build
`derive_patch_origin` answers, the one whose budget a patch build draws on; the unattended driver asks
it of each live claim before a patch build draws, and refuses the draw where another live run is a
patch of the same origin (TOOL-dDeclaredLoop-67 S35). After a draw appended to a transition log record,
`draw` reads `git check-attr merge` on that record once, and where it answers anything but `union`
prints, after the verdict, `loop: budget · notice · <record> merges as <answer>, not union: add
<root>/builds/*/build/*-transition-*.md merge=union to .gitattributes`, the root the module reads (S34):
two worktrees' draws on one record are two appended rows, which only a union merge keeps both of.
`--fixture --plant <case>` builds a scratch repository under the
host temp directory, runs the case and prints `held` or `MISSED`; `--selftest` runs every plant.

WHAT THIS DOES NOT CHECK: two racing draws, which are two rows; a row typed by hand with a right
ordinal; two distinct draws minting one id, in one second with the same 24 random bits, which count
as one; two byte-identical rows written before the id, which a union merge of the record keeps once;
the `research` cause's site, which no writer reaches yet.
"""
import argparse
import ast
import contextlib
import datetime
import io
import os
import pathlib
import re
import secrets
import shutil
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from adapt import read_disposition_release, read_run_file  # noqa: E402
from loop_lib import (LoopError, check_conf_name, derive_conf_constants, derive_conf_reads,  # noqa: E402
                      derive_fixture_boundary, load_tree_lib, read_memory_tree, resolve_memory_root, resolve_memory_root_source, run_selftest_cases)
from loop_parents import read_policy_kit  # noqa: E402
from loop_transition import (BUDGET_FIELDS, FX_BUILD, FX_SPEC, FX_UNIT, VALUE,  # noqa: E402
                             check_transition_channels, read_build_specs, read_build_unit_ids,
                             read_record_channels, read_transition_commits, read_transition_records,
                             read_transitions, render_transition_trailer, write_transition, write_transition_plant,
                             write_transition_record)
from loop_witness import read_git, remove_tree, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "loop"
BUDGET_KEY = "flow.rework-budget"
ROUTE_KEY = "flow.route-backs"
ENDING_KEY = "flow.on-exhausted"
#: The `Item` of the owner's disposition record that leaves an exhaustion park (TOOL-dDeclaredLoop-31).
EXHAUSTED_ITEM = "item.flow.on-exhausted"
#: The statuses `derive_ending` reads: a unit witnessed green, and one that counts for nothing.
CLOSED, WONTDO = "CLOSED", "WONTDO"
CAUSES = ("route-back", "fix-pass", "review-round", "re-dispatch", "research")
PATCH = "patch:"
PATCH_SCENARIO = "scenario.patch"
#: The repetitions another build or the remote caused: each re-verifies in its turn and draws nothing.
CONTENTION = ("stale-verdict", "conflicted-merge", "lease-wait", "remote-unreachable")
FREEZE_ROW = "budget · frozen · %d unit(s) · %d"
#: The UTC timestamp a run-state row opens with.
STAMP = "%Y-%m-%dT%H:%M:%SZ"
#: A draw row's id is the optional seventh group, so a row written before it still reads (TOOL-dDeclaredLoop-61).
ROW = re.compile(r"budget · frozen · (\d+) unit\(s\) · (\d+)|draw · (\S+) · (\S+) · (\d+)/(\d+)(?: · ([0-9]{8}T[0-9]{6}Z-[0-9a-f]{6}))?")
RUN_ROW = re.compile(r"(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ) ((?:budget|draw) · .*)")
#: A run-state row a patch build wrote for its originating build, ` · budget <slug>` after the row.
SUFFIXED = re.compile(r"(.*) · budget (\S+)")
#: The trailer values of the two budget fields, `budget` and `draw`: a cause never holds `@`, so a
#: `draw` value splits at its first `@` and its last.
TRAILER_ROWS = {"budget": re.compile(r"frozen@(\d+)@(\d+)"), "draw": re.compile(r"([^@]+)@(.+)@(\d+)\+(\d+)")}
#: The driver's archive pathspec: every record its preflight rotated, whatever phase it ended in.
ROTATED = "RUN.*.md"
PLANTS = {"mint-each-lap": "frozen at two units, a unit minted and fix-pass drawn on each lap, nine laps",
          "before-freeze": "designing back to planning and forward again, four laps, then a fifth route back",
          "stale-verdict": "a gates verdict staled by another build's landing, re-verified",
          "patch-draw": "fix-pass drawn by tFixPatch, a patch of the landed tFix, then the derived cause given",
          "route-backs": "one item drawn four times under flow.route-backs = 3, another once, then spent",
          "value": "flow.rework-budget set to 4+2, 6 and 4+, each the policy file's one revision",
          "unknown-cause": "a draw given the cause retry",
          "driver-draws": "the driver's two review rounds of one subject, a second generation, two dispatches",
          "spent-spec-round": "flow.rework-budget = 0, a spec subject's and the build slug's second rounds",
          "re-entry": "designing to building at three units, back, then building again at four",
          "pre-spec": "two draws before any spec or move, then a spec, the first move and a third draw",
          "unrecorded": "a draw on two specs and no move, the run-state file rotated, then a second draw",
          "trailer-only": "transitions.record = [\"trailer\"]: designing to building, fix-pass drawn, then back",
          "patch-trailer-only": "transitions.record = [\"trailer\"]: tFix landed by a trailer, tFixPatch drawing on it",
          "log-dropped": "planning to designing under the default set, then [\"trailer\"] and designing back",
          "parallel-append": "one item drawn alike on main and on a branch, the rows differing in their draw id alone, "
                             "merged under this tree's attribute, then drawn",
          "parallel-append-uneven": "one item drawn on main and two others on a branch, each draw only appending, "
                                    "merged under this tree's attribute",
          "draw-id-rows": "one log record given two identical id-less draw rows, each named by ending --explain, "
                          "one id-bearing row twice, then a malformed id",
          "draws-survive-rotation": "two draws, the run-state file rotated as an aborted run's, then a third draw",
          "patch-archived": "patch-trailer-only through its patch draw, then tFixPatch's run-state file rotated "
                            "as an aborted run's",
          "ending": "a CLOSED and an INPROGRESS unit under flow.rework-budget = 0 and a continue disposition, "
                    "then the default value",
          "driver-exhausted": "the driver's --exhausted unspent, then spent under close-incomplete with one unit "
                              "open: the rounds, the dispatches and the budget-exhausted abort",
          "unattended-root": "the build moved under records, the driver's conf naming MEMORY_ROOT=records and the "
                             "memory tree's conf none, two draws",
          "confs-disagree": "the driver's conf naming MEMORY_ROOT=records beside the memory tree's memory, one draw",
          "no-own-conf-read": "this module's own file graded on its syntax tree for a reader call or a conf name, "
                              "no scratch repository, then a kit pair whose tree_lib lacks derive_constant_charges, "
                              "its loader run in a fresh process: tree_lib lacking derive_constant_charges",
          "root-source": "MEMORY_ROOT=records in the driver's conf, then in the memory tree's conf, then neither, then "
                         "each conf alone with the key unset, each folder's root and the conf it came from",
          "attr-missing": "a draw appended to a log record in a scratch repository with no .gitattributes, then one "
                          "under the union line",
          "patch-concurrent": "the sourced driver's draw for tFixPatch, its claims read standing in with one live row "
                              "naming tFixPatchTwo, a patch of the same origin, then one naming tFix, no patch",
          "unset-driver-root": "the driver's conf setting no MEMORY_ROOT beside the memory tree's records, one draw; "
                               "then the build moved under records, both confs naming it, a draw and ending --explain",
          "patch-claims-unread": "the sourced driver's draw for tFixPatch, its claims read standing in as failed",
          "trailing-slash-agree": "the driver's conf naming MEMORY_ROOT=memory/ beside the memory tree's memory, "
                                  "one draw",
          "no-confs": "the memory tree's conf taken out and no driver's conf written, the root read",
          "driver-root-readers": "the build moved under records, the driver's conf naming MEMORY_ROOT=records and the "
                                 "memory tree's conf no root, then each reader of a build's folder: the ending's "
                                 "disposition, the position engine's README and acceptance reads, a withdrawn parent, "
                                 "an upstream record and the actor list's builds folder, then that folder again with "
                                 "the memory tree's conf naming memory",
          "conf-read-forms": "the conf-read rule over scratch modules beside a loop_lib binding the driver's conf's "
                             "name: a constant, the same line in fixture code, a bash string, an aliased reader, "
                             "docstrings alone, a Path binding, an annotated binding and a star import of the "
                             "loop_lib, a joined path, an os.path.join call, a multi-argument Path and an aliased "
                             "from-import, a join naming no conf, a global loader rebinding a name to the driver's "
                             "conf's path, one holding the memory tree's conf in a with, a walrus, a for target and "
                             "a with target, a global loader naming no conf and one naming the driver's conf in its "
                             "docstring alone, an annotation-only binding, a subscript target and a for body each "
                             "naming a conf, then a name bound to a conf's path by a global in a class body and "
                             "by a walrus in a default, a keyword-only default, a lambda default, a class base and "
                             "a decorator, beside a walrus in a function body and one in a class body binding none, "
                             "each row's loop_lib also run to compare the names it binds with the rule's, then "
                             "the first module with no loop_lib beside it, then with the "
                             "memory-tree kit's tree_lib unlocatable, blocked from import, unparseable, raising "
                             "at import and lacking both names the loop_lib reads, then a module calling each "
                             "conf reader the loop_lib declares, in three spellings"}
PLANT_RUN = "# %s run\n\n## Run facts\nphase: BUILDING\n" % FX_BUILD
PLANT_TRAILER = '[transitions]\nrecord = ["trailer"]\n'
PLANT_SPEC = "# TOOL-%s-%d — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01\n"
PATCH_BUILD = "tFixPatch"


# ------------------------------------------------------------------------------------------ the reads
def read_budget_value(root):
    """`(base, per-unit, route-backs)` at HEAD of `root`. ValueError naming the key on a policy refusal
    or a value of neither form; LookupError where the policy kit does not resolve."""
    policy, _guard = read_policy_kit()

    def read_one(key):
        try:
            return policy.resolve(key, str(root), "HEAD").value
        except policy.Refusal as e:
            raise ValueError("%s does not resolve at HEAD: %s" % (key, e)) from None

    # one call per key, each passing its constant by name, so reader coverage reads both
    # (TOOL-dLandedOwners-2)
    got = {BUDGET_KEY: read_one(BUDGET_KEY)}
    got[ROUTE_KEY] = read_one(ROUTE_KEY)
    value = got[BUDGET_KEY]
    hit = re.fullmatch(r"([0-9]+)\+([0-9]+)", value) if isinstance(value, str) else None
    if hit:
        return int(hit.group(1)), int(hit.group(2)), got[ROUTE_KEY]
    if isinstance(value, int) and not isinstance(value, bool):
        return value, 0, got[ROUTE_KEY]
    raise ValueError("%s is %r, neither <base>+<per-unit> nor a bare count" % (BUDGET_KEY, value))


def read_budget_rows(build, root, moves=None):
    """The build's budget, re-derived from its rows: `rows` its home's rows oldest first, `home` the path a
    draw appends to or None, `record` True where that home is a log record, `carried` the rows of its
    run-state files, its trailers and the ` · budget <slug>` rows, which the build's first log record
    copies, `frozen_any` whether any home holds a freeze row, `spent`,
    `total`, `freeze` the row a draw writes first under the unrecorded-build rule or None, `draws` each
    draw row's `(cause, item)`, `route-backs`, and `disagree`, each draw row whose typed spent is not its
    ordinal as `<row> · typed <a>, derived <b>`, in the order read: the figure is what its writer
    counted, and the count is re-derived from the rows, rows carrying one draw id counting once. `read`,
    the repository-relative paths the rows were taken from: the log records where any exists, else each
    run-state file and rotated record that gave a row, and `trailers` where a trailer row was taken
    (TOOL-dDeclaredLoop-75 S7). `moves`, the build's recorded moves where the
    caller read them. ValueError on a row outside its grammar; LookupError where a kit does not
    resolve."""
    root = pathlib.Path(root)
    records = read_transition_records(build, root)
    run = read_run_file(root, build)
    # its own run-state files, each row it holds for itself; and, for a build holding no log record, its
    # trailers' fields and the rows each build's RUN.md and rotated records hold for it under ` · budget <slug>`
    # (TOOL-dDeclaredLoop-48)
    files = [(path, None) for path in sorted(run.parent.glob(ROTATED)) + [run]]
    # `RUN.*.md` never matches `RUN.md`, so no file is read twice under one owner (TOOL-dDeclaredLoop-60)
    named = sorted(run.parent.parent.glob("*/RUN.md")) + sorted(run.parent.parent.glob("*/" + ROTATED))
    files += [] if records else [(path, build) for path in named]
    carried = [] if records else read_trailer_rows(build, root)
    read = [rec["path"] for rec in records] or (["trailers"] if carried else [])
    for path, owner in files:
        if path.is_file():
            before = len(carried)
            for ln in path.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n").split("\n"):
                hit = RUN_ROW.fullmatch(ln.rstrip())
                mark = SUFFIXED.fullmatch(hit.group(2)) if hit else None
                if hit and owner is None and not mark:
                    carried.append((hit.group(1), hit.group(2)))
                elif mark and owner is not None and mark.group(2) == owner:
                    carried.append((hit.group(1), mark.group(1)))
            if len(carried) > before and not records:
                read.append(path.relative_to(root).as_posix())
    order = []
    for ts, text in carried:   # oldest first by UTC second, a tie broken by the typed spent, a freeze row first
        hit = ROW.fullmatch(text)
        order.append((ts, -1 if hit and hit.group(2) is not None else int(hit.group(5)) if hit else 0, text))
    carried = [text for _ts, _n, text in sorted(order, key=lambda r: r[:2])]
    held = []
    for rec in records:
        text = pathlib.Path(root, rec["path"]).read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")
        held += [ln.rstrip() for ln in text.split("\n") if ln.startswith(("budget · ", "draw · "))]
    rows = held if records else carried
    frozen, draws, disagree, seen = None, [], [], set()
    for row in rows:
        hit = ROW.fullmatch(row)
        if not hit:
            raise ValueError("the budget row %r of %s is outside its grammar" % (row, build))
        if hit.group(2) is not None:
            frozen = int(hit.group(2)) if frozen is None else frozen
            continue
        if hit.group(7) is not None and hit.group(7) in seen:   # a copy of a draw already counted
            continue
        seen.add(hit.group(7))
        draws.append((hit.group(3), hit.group(4)))
        if int(hit.group(5)) != len(draws):   # what its writer counted; two worktrees each count their own
            disagree.append("%s · typed %s, derived %d" % (row, hit.group(5), len(draws)))
    base, per, route_backs = read_budget_value(root)
    frozen_any = any(r.startswith("budget · ") for r in held + carried)
    total, freeze = (frozen if frozen is not None else base), None
    if not frozen_any:
        units = read_build_unit_ids(build, root)
        if units and not (read_transitions(build, root) if moves is None else moves):
            total = base + per * len(units)
            freeze = FREEZE_ROW % (len(units), total)
    home = records[-1]["path"] if records else (run.relative_to(root).as_posix() if run.is_file() else None)
    return {"rows": rows, "home": home, "record": bool(records), "carried": [] if records else carried,
            "frozen_any": frozen_any, "spent": len(draws), "total": total, "freeze": freeze, "draws": draws,
            "route-backs": route_backs, "disagree": disagree, "read": read}


def read_trailer_rows(build, root):
    """The build's `(stamp, row)` pairs from the `budget` and `draw` fields of its `Gov-Transition`
    trailers, oldest first, each stamped with its commit's committer date in UTC. ValueError naming the
    commit on a value outside its grammar."""
    out = []
    for commit, fields in read_transition_commits(build, root)[0]:
        when = datetime.datetime.fromisoformat(commit["date"].replace("Z", "+00:00"))
        stamp = when.astimezone(datetime.timezone.utc).strftime(STAMP)
        for name in BUDGET_FIELDS:
            hit = TRAILER_ROWS[name].fullmatch(fields[name]) if name in fields else None
            if name in fields and not hit:
                raise ValueError("commit %s carries %s=%s, outside its grammar %s" % (
                    commit["sha"][:8], name, fields[name], TRAILER_ROWS[name].pattern))
            if hit and name == "budget":
                out.append((stamp, FREEZE_ROW % (int(hit.group(1)), int(hit.group(2)))))
            elif hit:
                out.append((stamp, "draw · %s · %s · %s/%s" % hit.groups()))
    return out


def derive_patch_origin(build, root, moves=None):
    """The build whose budget `build`'s draws land on where `build` is a patch build, its newest recorded
    move carrying `scenario.patch`: the first slug its README's `parents:` names. None for any other
    build; ValueError where a patch build's README names no parent."""
    moves = read_transitions(build, root) if moves is None else moves
    if not moves or PATCH_SCENARIO not in moves[0].get("scenario", "").split("+"):
        return None
    read_memory_tree("gen_build_index.py")
    from gen_build_index import Problem, parse_front_matter
    readme = pathlib.Path(root, resolve_memory_root(root), "builds", build, "README.md")
    try:
        parents = parse_front_matter(str(readme), build).get("parents", "").split()
    except (Problem, OSError) as e:
        raise ValueError("the patch build %s's README does not read: %s" % (build, e)) from None
    if not parents:
        raise ValueError("%s is a patch build and its README names no parents:, so its draw has no originating "
                         "budget" % build)
    return parents[0]


def budget_state(build, root=".", held=None):
    """`open <spent>/<total>`, `spent`, or `unfrozen <spent>/<total>` where no freeze row is held; `held`,
    what `read_budget_rows` answered where the caller read it, else a fresh read."""
    held = read_budget_rows(build, root) if held is None else held
    if held["spent"] >= held["total"]:
        return "spent"
    return "%s %d/%d" % ("open" if held["frozen_any"] else "unfrozen", held["spent"], held["total"])


def classify_repeat(event):
    """The cause a repetition `event` draws, or `contention` for one another build or the remote caused,
    which draws nothing. ValueError on an event of neither set."""
    if event in CONTENTION:
        return "contention"
    if event in CAUSES:
        return event
    raise ValueError("the repetition %r is neither a cause, %s, nor contention, %s" % (
        event, " ".join(CAUSES), " ".join(CONTENTION)))


def count_returns(build, item, root="."):
    """`(n, converging or non-converging)`: the draws naming `item`, and whether they passed
    `flow.route-backs`. A spec subject's `review-round` draws are counted and never end its loop."""
    held = read_budget_rows(build, root)
    mine = [cause for cause, it in held["draws"] if it == item]
    spec_rounds = item != build and mine and all(c == "review-round" for c in mine)
    return len(mine), "non-converging" if len(mine) > held["route-backs"] and not spec_rounds else "converging"


def promotion_target(build, item, blocking, root="."):
    """Where an item past its early limit goes: `unit` for a blocking item while the budget remains,
    `ask` for a non-blocking one, `on-exhausted` for a blocking one once the budget is spent."""
    if not blocking:
        return "ask"
    return "on-exhausted" if budget_state(build, root) == "spent" else "unit"


def derive_ending(value, units):
    """The ending a spent budget takes under `flow.on-exhausted` = `value`, `units` `{id: status}`: the value
    itself for `park-for-owner` and `close-incomplete`; under `best-effort-ending`, `land-green` where every
    unit not WONTDO is CLOSED and one is, `descope` where some unit is CLOSED, else `close-incomplete`, so a
    build with no units lands nothing. ValueError naming the key on any other value. Never a draw."""
    if value in ("park-for-owner", "close-incomplete"):
        return value
    if value != "best-effort-ending":
        raise ValueError("%s is %r, none of best-effort-ending, park-for-owner and close-incomplete" % (
            ENDING_KEY, value))
    counted = [s for s in units.values() if s != WONTDO]
    if counted and all(s == CLOSED for s in counted):
        return "land-green"
    return "descope" if CLOSED in counted else "close-incomplete"


def read_ending(build, root, held=None):
    """The ending line of `build` at HEAD of `root`: `loop: budget · ending · <ending|none> · <state word>
    <spent>/<total> · open <ids|none> · disposed <word|unrecorded>`; `held`, what `read_budget_rows`
    answered where the caller read it, else a fresh read. ValueError on a value or a row the grammar
    refuses; LookupError where a kit does not resolve."""
    root = pathlib.Path(root)
    held = read_budget_rows(build, root) if held is None else held
    state = budget_state(build, root, held).split(" ", 1)[0]
    policy, _guard = read_policy_kit()
    try:
        value = policy.resolve(ENDING_KEY, str(root), "HEAD").value
    except policy.Refusal as e:
        raise ValueError("%s does not resolve at HEAD: %s" % (ENDING_KEY, e)) from None
    units = dict(read_build_specs(build, root))
    ending = derive_ending(value, units) if state == "spent" else "none"
    opened = [uid for uid, status in units.items() if status not in (CLOSED, WONTDO)]
    disposed = read_disposition_release(root, build, EXHAUSTED_ITEM, ())
    return "%s: budget · ending · %s · %s %d/%d · open %s · disposed %s" % (
        SAY, ending, state, held["spent"], held["total"], " ".join(opened) or "none",
        disposed[1] if disposed else "unrecorded")


# ------------------------------------------------------------------------------------------ the writers
def freeze_budget(build, root):
    """The freeze row of `build` at HEAD, `budget · frozen · <units> unit(s) · <total>`, or None where any
    home of the build already holds one. The transition writer writes it on `designing` to `building`."""
    held = read_budget_rows(build, root, moves=[None])   # a non-empty `moves` skips the unrecorded-build read
    if held["frozen_any"]:
        return None
    base, per, _routes = read_budget_value(root)
    units = len(read_build_unit_ids(build, root))
    return FREEZE_ROW % (units, base + per * units)


def read_merge_attribute(root, rel):
    """What `git check-attr merge` answers for `rel` in `root`: `union`, `unspecified`, `set` or another
    driver; `unread` where git cannot answer."""
    rc, out = read_git(root, "check-attr", "merge", "--", rel)
    return out.rsplit(": ", 1)[-1].strip() if rc == 0 and out else "unread"


def record_draw(build, cause, item, root=".", lines=None, moves=None, notes=None, merges=None):
    """`("drawn", row)` after writing one draw row of `build`, a freeze row before it where one is owed,
    or `("exhausted", "<slug> · <spent>/<total>")` writing nothing. Where `lines` is a list the rows are
    added to it, the transition writer's record, and no file is written, save a patch build's, which
    lands on its originating build's home, or, where that build holds no log record and the set holds no
    `log`, on the patch build's own run-state file, each row suffixed ` · budget <origin>` and the answer
    with it. Where `notes` is a list it is extended with the `disagree` entries of the build drawn on, and
    where `merges` is one, a draw committed to a log record adds `(record, its merge attribute)` to it.
    ValueError on a cause outside `CAUSES`, a derived cause given, an item outside `VALUE`, or a
    build with no home, a patch build with no run-state file under that rule among them."""
    if cause.startswith(PATCH):
        raise ValueError("the cause %s is derived: a patch build's draw is named patch:<its slug> from its "
                         "scenario, so it is never given" % cause)
    if cause not in CAUSES:
        raise ValueError("the cause %s is outside the closed set: %s %s<slug>" % (cause, " ".join(CAUSES), PATCH))
    if not VALUE.fullmatch(item or ""):
        raise ValueError("the item %r is outside [A-Za-z0-9._:+@-]+" % item)
    root = pathlib.Path(root).absolute()
    moves = read_transitions(build, root) if moves is None else moves
    origin, suffix = derive_patch_origin(build, root, moves), ""
    if origin:
        patch, build, cause, lines, moves = build, origin, PATCH + build, None, None
    held = read_budget_rows(build, root, moves)
    if origin and not held["record"] and "log" not in read_record_channels(root, "HEAD"):
        run = read_run_file(root, patch)
        if not run.is_file():
            raise ValueError("the patch build %s has no run-state file, and its draw on %s, which holds no transition "
                             "log record under a set without log, has no other home" % (patch, origin))
        held["home"], suffix = run.relative_to(root).as_posix(), " · budget %s" % origin
    if notes is not None:
        notes.extend(held["disagree"])
    if held["spent"] >= held["total"]:
        return "exhausted", "%s · %d/%d" % (build, held["spent"], held["total"])
    # the draw id, one per draw and the same on every home it is written to (TOOL-dDeclaredLoop-61)
    row = "draw · %s · %s · %d/%d · %s-%s" % (cause, item, held["spent"] + 1, held["total"], datetime.datetime.now(
        datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ"), secrets.token_hex(3))
    add = ([held["freeze"]] if held["freeze"] else []) + [row]
    if lines is not None:
        lines.extend(add)
        return "drawn", row
    if held["home"] is None:
        raise ValueError("%s has neither a transition log record nor a run-state file, so the draw has no "
                         "home" % build)
    path = pathlib.Path(root, held["home"])
    if not held["record"]:
        write_budget_rows(path, [r + suffix for r in add], False)
        return "drawn", row + suffix
    before = path.read_bytes()
    write_budget_rows(path, add, True)
    subject = "loop budget(%s): %s %d/%d" % (build, cause, held["spent"] + 1, held["total"])
    if read_git(root, "commit", "-q", "--only", "-m", subject, "--", held["home"])[0] != 0:
        path.write_bytes(before)
        raise ValueError("git could not commit the draw on %s, so nothing is drawn" % held["home"])
    if merges is not None:   # TOOL-dDeclaredLoop-67 S34: the record's merge rule, read once
        merges.append((held["home"], read_merge_attribute(root, held["home"])))
    return "drawn", row


def write_budget_rows(path, rows, record):
    """`rows` appended to the file at `path`: to a log record where `record`, its first rows after one
    blank line, else to a run-state file, each after its UTC stamp."""
    text = path.read_bytes().decode("utf-8", "replace")
    if record:
        lead = "" if any(ln.startswith(("budget · ", "draw · ")) for ln in text.split("\n")) else "\n"
        body = "".join(r + "\n" for r in rows)
    else:
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime(STAMP)
        lead = "" if text.endswith("\n") or not text else "\n"
        body = "".join("%s %s\n" % (stamp, r) for r in rows)
    with open(path, "ab") as fh:
        fh.write((lead + body).encode("utf-8"))


def render_budget_fields(rows):
    """The trailer fields of a move's budget `rows`: `budget=frozen@<units>@<total>` for a freeze row and
    `draw=<cause>@<item>@<spent>+<total>` for a draw row. ValueError on a row outside the grammar, a second
    row of one kind, or a value outside `VALUE`."""
    out = {}
    for row in rows:
        hit = ROW.fullmatch(row)
        if not hit:
            raise ValueError("the budget row %r is outside its grammar" % row)
        name = "budget" if hit.group(2) is not None else "draw"
        value = "frozen@%s@%s" % hit.group(1, 2) if name == "budget" else "%s@%s@%s+%s" % hit.group(3, 4, 5, 6)
        if name in out:
            raise ValueError("the move carries a second %s row, %r, and its trailer holds one %s field" % (
                name, row, name))
        if not VALUE.fullmatch(value):
            raise ValueError("the %s field %r is outside [A-Za-z0-9._:+@-]+" % (name, value))
        out[name] = value
    return out


# ------------------------------------------------------------------------------------------ the plants
def write_budget_plant(top, case):
    """The scratch repository at `top` for `case`: the transition writer's plant, then this case's specs,
    run-state file and policy file, committed."""
    write_transition_plant(top, {"pre-spec": "pre-spec"}.get(case, "default"))
    units = {"mint-each-lap": 2, "unrecorded": 2, "re-entry": 3, "ending": 2}.get(case, 1)
    files = {FX_SPEC.replace(FX_UNIT, "TOOL-%s-%d" % (FX_BUILD, n)): PLANT_SPEC % (FX_BUILD, n)
             for n in range(2, units + 1)}
    if case == "ending":   # the second unit witnessed green, the first open, and nothing left to draw
        files[FX_SPEC.replace(FX_UNIT, "TOOL-%s-2" % FX_BUILD)] = (PLANT_SPEC % (FX_BUILD, 2)).replace("INPROGRESS", CLOSED)
        files[".governance/policy.toml"] = "[flow]\nrework-budget = 0\n"
    if case in ("pre-spec", "unrecorded", "trailer-only", "draws-survive-rotation", "confs-disagree",
                "unset-driver-root", "trailing-slash-agree", "no-confs"):
        files["memory/builds/%s/RUN.md" % FX_BUILD] = PLANT_RUN
    if case == "route-backs":
        files[".governance/policy.toml"] = "[flow]\nroute-backs = 3\nrework-budget = 6\n"
    if case in ("trailer-only", "patch-trailer-only", "patch-archived"):
        files[".governance/policy.toml"] = PLANT_TRAILER
    write_fixture_files(top, files)
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "--allow-empty", "-m", "the budget plant")


def run_budget_plant(case):
    """One plant: its lines, then `loop: fixture · <case> · held` or `MISSED <why>`; 0 held, 1 missed, 2
    where a kit does not resolve."""
    top = pathlib.Path(tempfile.mkdtemp(prefix="loop-budget-")).absolute()
    misses, here = [], os.getcwd()
    try:
        print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))

        def run_verb(argv, repo=top):
            """`(exit, output)` of this module's `main(argv)` run at `repo`'s top level, the output echoed."""
            out = io.StringIO()
            os.chdir(repo)
            try:
                with contextlib.redirect_stdout(out):
                    rc = main(argv)
            finally:
                os.chdir(here)
            print(out.getvalue().rstrip())
            return rc, out.getvalue()

        def run_move(state, item, outcome, fields=None):
            """One move of the plant's build through the transition writer, given `fields`: None, or the refusal."""
            try:
                write_transition(top, FX_BUILD, state, item, outcome, "HEAD", {}, fields or {})
            except ValueError as e:
                print("%s: fixture · move %s · refused · %s" % (SAY, state, e))
                return str(e)
            return None

        def write_spec(n):
            """The plant build's n-th unit, its spec committed."""
            write_fixture_files(top, {FX_SPEC.replace(FX_UNIT, "TOOL-%s-%d" % (FX_BUILD, n)): PLANT_SPEC % (FX_BUILD, n)})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "unit %d" % n)

        def parse_draw_id(row):
            """`(row, id)`: a budget row with its draw id cut by `ROW`'s id group, and the id, None where it
            carries none."""
            hit = ROW.fullmatch(row)
            return (row[:hit.end(6)], hit.group(7)) if hit and hit.group(7) else (row, None)

        def read_rows(build=FX_BUILD):
            """The build's rows, printed, each answered with its draw id cut; a miss where a draw row carries none."""
            rows = read_budget_rows(build, top)["rows"]
            print("%s: fixture · rows %s · %s" % (SAY, build, " | ".join(rows) or "none"))
            cut = [parse_draw_id(r) for r in rows]
            check(all(i for r, i in cut if r.startswith("draw · ")), "a draw row carries no draw id")
            return [r for r, _i in cut]

        def check(cond, why):
            """A miss named where `cond` does not hold."""
            if not cond:
                misses.append(why)

        def run_driver_case():
            """The driver plants: this tree's unattended driver run in a scratch repository through `position.py`'s
            plant and `run_driver`; the misses."""
            from position import FX_IDS, FX_SLUG, run_driver, write_position_plant
            root = next((d for d in (KIT, *KIT.parents) if (d / ".git").exists()), KIT)
            repo = write_position_plant(top, "plan-line", root)[0]
            policy = '[review.design]\nrounds = "fixed-count"\nround-count = 3\n'
            policy += "\n[flow]\nrework-budget = 0\n" if case == "spent-spec-round" else ""
            write_fixture_files(repo, {".governance/policy.toml": policy})
            with open(repo / ".unattended.conf", "a", encoding="utf-8", newline="\n") as fh:
                fh.write('\nSPEC_TOKENS_CLI=""\nRUN_CLAIMS="off"\n')
            run_fixture_git(repo, "add", "-A")
            run_fixture_git(repo, "commit", "-q", "-m", "the budget plant's policy")
            # the review bounds read the landed revision
            run_fixture_git(repo, "push", "-q", run_fixture_git(repo, "remote"), "main")
            run = repo / "memory" / "builds" / FX_SLUG / "RUN.md"
            missed = []

            def run_round(subject, blockers):
                """One `--review` round: `(exit, output)`, echoed."""
                out, rc = run_driver(repo, "--review", FX_SLUG, "--subject", subject, "--verdict", "BLOCKED", "--blockers",
                                     str(blockers))
                print("%s: fixture · review %s · exit %d · %s" % (SAY, subject, rc, out.strip().replace("\n", " / ")[:400]))
                return rc, out

            def read_count(text):
                """How many lines of the run-state file hold `text`."""
                return run.read_text(encoding="utf-8").count(text)

            if case == "driver-draws":
                unit = FX_IDS[0]
                run_round(unit, 3)
                check_one = read_count("draw · ")
                run_round(unit, 2)
                run_round("%s-spec-set-r2" % FX_SLUG, 1)
                for _n in range(2):
                    out, rc = run_driver(repo, "--dispatch", FX_SLUG, "--pass", unit, "--writes", "work/a.txt")
                    print("%s: fixture · dispatch · exit %d · %s" % (SAY, rc, out.strip().replace("\n", " / ")[:300]))
                cut = [parse_draw_id(ln.split(" ", 1)[1]) for ln in run.read_text(encoding="utf-8").split("\n")
                       if RUN_ROW.fullmatch(ln)]
                rows = [r for r, _i in cut]
                print("%s: fixture · rows %s · %s" % (SAY, FX_SLUG, " | ".join(rows) or "none"))
                if not all(i for r, i in cut if r.startswith("draw · ")):
                    missed.append("a draw row carries no draw id")
                owed = [FREEZE_ROW % (3, 10), "draw · review-round · %s · 1/10" % unit,
                        "draw · review-round · %s-spec-set-r2 · 2/10" % FX_SLUG, "draw · re-dispatch · %s · 3/10" % unit]
                if check_one != 0:
                    missed.append("the first round drew")
                if rows != owed:
                    missed.append("the rows read %s" % " | ".join(rows))
            elif case == "driver-exhausted":   # TOOL-dDeclaredLoop-31: AC2, AC3 and AC4
                before = run.read_bytes()
                out, rc = run_driver(repo, "--exhausted", FX_SLUG)
                print("%s: fixture · exhausted unspent · exit %d · %s" % (SAY, rc, out.strip().replace("\n", " / ")[:400]))
                if rc != 1 or "unfrozen" not in out or run.read_bytes() != before:
                    missed.append("--exhausted under the default budget was not refused naming unfrozen, the file unchanged")
                abort = ("--abort", FX_SLUG, "--code", "budget-exhausted", "--reason", "r")
                out, rc = run_driver(repo, *abort)
                print("%s: fixture · abort unrecorded · exit %d · %s" % (SAY, rc, out.strip().replace("\n", " / ")[:400]))
                if rc != 1 or run.read_bytes() != before:
                    missed.append("the budget-exhausted abort with no exhaustion row was not refused")
                for uid in FX_IDS[1:]:   # one unit left open, the others witnessed green
                    spec = repo / "memory" / "builds" / FX_SLUG / "spec" / ("2026-01-01-spec-%s.md" % uid)
                    text = spec.read_text(encoding="utf-8").replace("**Status:** INPROGRESS", "**Status:** " + CLOSED)
                    write_fixture_files(repo, {spec.relative_to(repo).as_posix(): text})
                write_fixture_files(repo, {".governance/policy.toml": policy + '\n[flow]\nrework-budget = 0\n'
                                                                               'on-exhausted = "close-incomplete"\n'})
                run_fixture_git(repo, "add", "-A")
                run_fixture_git(repo, "commit", "-q", "-m", "the budget spent, one unit open")
                run_fixture_git(repo, "push", "-q", run_fixture_git(repo, "remote"), "main")
                owner = "only the owner raises %s" % BUDGET_KEY
                row = "decision · item %s · reason ending close-incomplete · spent 0/0 · open %s" % (ENDING_KEY, FX_IDS[0])
                run_round(FX_SLUG, 3)
                rc, out = run_round(FX_SLUG, 2)
                if rc != 1 or "--exhausted %s" % FX_SLUG not in out:
                    missed.append("the build slug's second round was not refused naming --exhausted")
                for n in (1, 2):
                    out, rc = run_driver(repo, "--exhausted", FX_SLUG)
                    print("%s: fixture · exhausted %d · exit %d · %s" % (SAY, n, rc, out.strip().replace("\n", " / ")[:400]))
                    if rc != 0 or read_count(row) != 1 or owner not in out:
                        missed.append("--exhausted %d did not leave one row %s, naming that %s" % (n, row, owner))
                rc, out = run_round(FX_SLUG, 1)
                if rc != 1 or "close-incomplete" not in out or owner not in out:
                    missed.append("a round after the exhaustion row was not refused naming its ending")
                for _n in range(2):
                    out, rc = run_driver(repo, "--dispatch", FX_SLUG, "--pass", FX_IDS[0], "--writes", "work/a.txt")
                    print("%s: fixture · dispatch · exit %d · %s" % (SAY, rc, out.strip().replace("\n", " / ")[:300]))
                if rc != 1 or "close-incomplete" not in out or owner not in out:
                    missed.append("the second dispatch was not refused naming the ending")
                for item in ("keepalive-reaped", "parked-decisions-surfaced"):
                    run_driver(repo, "--attest", FX_SLUG, "--item", item)
                out, rc = run_driver(repo, *abort)
                print("%s: fixture · abort unfiled · exit %d · %s" % (SAY, rc, out.strip().replace("\n", " / ")[:400]))
                if rc != 1 or FX_IDS[0] not in out:
                    missed.append("the abort with %s unfiled was not refused naming it" % FX_IDS[0])
                run_driver(repo, "--rescope", FX_SLUG, "--act", "defer", "--item", FX_IDS[0], "--reason", "r")
                out, rc = run_driver(repo, *abort)
                print("%s: fixture · abort filed · exit %d · %s" % (SAY, rc, out.strip().replace("\n", " / ")[:400]))
                text = run.read_text(encoding="utf-8") if run.is_file() else ""
                if rc != 0 or "phase: ABORTED" not in text or "halt-code: budget-exhausted" not in text \
                        or read_git(repo, "rev-parse", "--verify", "main")[0] != 0:
                    missed.append("the abort with every open unit filed did not end the run ABORTED under budget-exhausted")
            else:
                run_round(FX_IDS[0], 3)
                rc, out = run_round(FX_IDS[0], 2)
                if rc != 0 or read_count("review · item %s · " % FX_IDS[0]) != 2:
                    missed.append("the spec subject's second round under a spent budget was not recorded")
                run_round(FX_SLUG, 3)
                rc, out = run_round(FX_SLUG, 2)
                if rc != 1 or ENDING_KEY not in out or read_count("review · item %s · " % FX_SLUG) != 1:
                    missed.append("the build slug's second round was not refused naming %s" % ENDING_KEY)
                if read_count("draw · ") or read_count("budget · "):
                    missed.append("a spent budget wrote a row")
            return missed

        if case in ("driver-draws", "spent-spec-round", "driver-exhausted"):
            misses += run_driver_case()
        elif case == "value":
            for value, owed in (('"4+2"', "base 4 per-unit 2"), ("6", "base 6 per-unit 0"), ('"4+"', BUDGET_KEY)):
                repo = top / ("v%d" % len(value))
                repo.mkdir()
                run_fixture_git(repo, "init", "-q", "--template=", "-b", "main")
                write_fixture_files(repo, {".governance/policy.toml": "[flow]\nrework-budget = %s\n" % value})
                run_fixture_git(repo, "add", "-A")
                run_fixture_git(repo, "commit", "-q", "-m", "policy")
                rc, out = run_verb(["value"], repo)
                check(owed in out and rc == (2 if owed == BUDGET_KEY else 0), "value %s read %r, exit %d" % (
                    value, out.strip(), rc))
        elif case == "no-own-conf-read":   # TOOL-dDeclaredLoop-76 AC1: this module's own file, no scratch tree
            own = pathlib.Path(__file__)
            try:
                bound = [f.name for f in derive_fixture_boundary(ast.parse(own.read_text(encoding="utf-8"), str(own)))]
                hits = derive_conf_reads(own)
            except SyntaxError as e:
                bound, hits = [], []
                check(False, "%s does not parse: %s" % (own.name, e))
            except LoopError as e:   # TOOL-dDeclaredLoop-86 S21: a missing loop_lib or a stale tree_lib, a miss
                bound, hits = [], []
                check(False, str(e))
            print("%s: fixture · fixture boundary: %d functions — %s" % (SAY, len(bound), ", ".join(bound) or "none"))
            for line, kind in hits:
                print("%s: fixture · conf read · %s:%d %s" % (SAY, own.name, line, kind))
            check(not hits, "%d conf read(s) in %s" % (len(hits), own.name))
            # TOOL-dDeclaredLoop-80 AC2: the boundary's lasting arm, a whole-token match over defs alone; its
            # loop_lib.py stub binds no conf name (TOOL-dDeclaredLoop-86 S15)
            staged = top / "staged.py"
            write_fixture_files(top, {staged.name: 'def check_plant_root(tree): return tree / ".unattended.conf"\n'
                                      'async def build_fixture_tree(t): return ".memory-tree.conf"\n'
                                      'def read_planted_root(t): return ".unattended.conf"\n'
                                      'class fixture_rows:\n    CONF = ".memory-tree.conf"\n',
                                      "loop_lib.py": "NOTHING = 0\n"})
            bound = [f.name for f in derive_fixture_boundary(ast.parse(staged.read_text(encoding="utf-8")))]
            try:
                hits = derive_conf_reads(staged)
            except LoopError as e:
                hits = []
                check(False, str(e))
            print("%s: fixture · %s · fixture boundary: %d functions — %s" % (SAY, staged.name, len(bound),
                                                                             ", ".join(bound) or "none"))
            for line, kind in hits:
                print("%s: fixture · conf read · %s:%d %s" % (SAY, staged.name, line, kind))
            check(bound == ["check_plant_root", "build_fixture_tree"] and hits == [(3, "conf name"), (5, "conf name")],
                  "%s answered boundary %s and hits %s, owed the first two defs and lines 3 and 5" % (
                      staged.name, bound, hits))
            # TOOL-dDeclaredLoop-90 S5: the skew of a memory-tree kit older than TOOL-dDeclaredLoop-88, a kit
            # pair whose tree_lib lacks derive_constant_charges, its loader run in a fresh process
            import subprocess
            skew = "tree_lib lacking derive_constant_charges"
            try:
                mt = pathlib.Path(load_tree_lib().__file__).parent
            except LoopError as e:
                mt = None
                check(False, "%s: %s" % (skew, e))
            if mt:
                pair = top / "skew"
                for kit, name in ((KIT, "loop_lib.py"), (mt, "tree_lib.py")):
                    (pair / kit.name).mkdir(parents=True)
                    shutil.copyfile(kit / name, pair / kit.name / name)
                with open(pair / mt.name / "tree_lib.py", "a", encoding="utf-8", newline="\n") as fh:
                    fh.write('\nglobals().pop("derive_constant_charges", None)\n')
                probe = ("import sys; sys.path.insert(0, sys.argv[1]); import loop_lib\n"
                         "try: loop_lib.load_tree_lib()\n"
                         "except loop_lib.LoopError as e: print(e); sys.exit(1)\n")
                p = subprocess.run([sys.executable, "-I", "-c", probe, str(pair / KIT.name)], capture_output=True,
                                   text=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
                print("%s: fixture · no-own-conf-read · %s · exit %d · %s" % (
                    SAY, skew, p.returncode, (p.stdout + p.stderr).strip() or "no output"))
                check(p.returncode == 1 and "derive_constant_charges" in p.stdout
                      and "govkit update --kits memory-tree" in p.stdout and "Traceback" not in p.stdout + p.stderr,
                      "%s: exit %d, owed exit 1 naming derive_constant_charges and the update command, no "
                      "traceback" % (skew, p.returncode))
        elif case == "root-source":   # TOOL-dDeclaredLoop-76 AC3: each root paired with the conf it came from
            for name, confs, owed in (("driver", {".unattended.conf": "MEMORY_ROOT=records\n"}, ("records", ".unattended.conf")),
                                      ("tree", {".memory-tree.conf": "MEMORY_ROOT=records\n"}, ("records", ".memory-tree.conf")),
                                      ("neither", {}, ("memory", "default")),
                                      # TOOL-dDeclaredLoop-82 AC15 (S15): each conf alone, the key unset
                                      ("driver-unset", {".unattended.conf": 'PHASES_EXTRA=""\n'},
                                       ("memory", ".unattended.conf")),
                                      ("tree-unset", {".memory-tree.conf": 'FAMILIES="tool:TOOL"\n'},
                                       ("memory", ".memory-tree.conf"))):
                folder = top / name
                folder.mkdir()
                run_fixture_git(folder, "init", "-q", "--template=", "-b", "main")
                write_fixture_files(folder, confs)
                try:
                    got = (resolve_memory_root_source(folder), resolve_memory_root(folder))
                except ValueError as e:   # a read_driver_conf refusal, a LoopError, is a ValueError
                    got = ("refused", str(e))
                print("%s: fixture · root-source · %s · %s · %s" % (SAY, name, got[0], got[1]))
                check(got == (owed, owed[0]), "%s answered %s, owed %s" % (name, got, owed))
        elif case == "conf-read-forms":   # TOOL-dDeclaredLoop-82 AC1, AC10, AC16 (S1, S10, S16): one row per form
            first = "import loop_lib as ll\ndef read_root(tree): return (tree / ll.UNATTENDED_CONF).read_text()\n"
            rows = (("constant", first, [(2, "conf constant")]),
                    ("fixture-code", first.replace("read_root", "check_plant_root"), []),
                    ("bash-string", "import subprocess\ndef read_root_bash():\n    return subprocess.run(['bash', "
                                    "'-c', '. \"$ROOT/.unattended.conf\"; printf %s \"$MEMORY_ROOT\"'])\n",
                     [(3, "conf name")]),
                    ("aliased-reader", "from loop_lib import read_driver_conf as rdc\n"
                                       "def read_root(tree): return rdc(tree, ['MEMORY_ROOT'])\n",
                     [(2, "reader call")]),
                    ("docstrings", '"""Names .unattended.conf."""\nclass Rows:\n    """Names .unattended.conf."""\n'
                                   'def read_rows():\n    """Names .unattended.conf."""\n'
                                   'async def read_rows_later():\n    """Names .unattended.conf."""\n', []))
            write_fixture_files(top / "with-lib", {"loop_lib.py": 'UNATTENDED_CONF = ".unattended.conf"\n'})
            for name, text, owed in rows:
                write_fixture_files(top / "with-lib", {name + ".py": text})
                got = derive_conf_reads(top / "with-lib" / (name + ".py"))
                print("%s: fixture · conf-read-forms · %s · %s" % (SAY, name, ", ".join(
                    "line %d %s" % hit for hit in got) or "no hit"))
                check(got == owed, "%s answered %s, owed %s" % (name, got, owed))
            # TOOL-dDeclaredLoop-86 S13: a Path binding, an annotated binding and a star import, each a folder
            # holding its module beside a loop_lib.py binding a conf's name in that form
            for name, lib, text in (
                    ("path-binding", 'from pathlib import Path\nUNATTENDED_CONF_PATH = Path(".unattended.conf")\n',
                     "import loop_lib as ll\ndef read_root(tree): return tree / ll.UNATTENDED_CONF_PATH\n"),
                    ("annotated-binding", 'CONF: str = ".memory-tree.conf"\n',
                     "import loop_lib as ll\ndef read_root(tree): return tree / ll.CONF\n"),
                    ("star-import", 'CONF = ".unattended.conf"\n',
                     "from loop_lib import *\ndef read_root(tree): return tree / CONF\n")):
                write_fixture_files(top / name, {"loop_lib.py": lib, name + ".py": text})
                got = derive_conf_reads(top / name / (name + ".py"))
                print("%s: fixture · conf-read-forms · %s · %s" % (SAY, name, ", ".join(
                    "line %d %s" % hit for hit in got) or "no hit"))
                check(got == [(2, "conf constant")], "%s answered %s, owed one conf constant" % (name, got))
            # TOOL-dDeclaredLoop-87 S3: the repo's own binding idioms, each inside the class and outside 86's
            # shape list, then a join naming no conf, the liveness negative
            for name, lib, opens, reads, owed in (
                    ("joined-path", 'CONF = ROOT / ".unattended.conf"\n', "import loop_lib as ll", "ll.CONF",
                     [(2, "conf constant")]),
                    ("os-path-join", 'CONF = os.path.join(ROOT, ".memory-tree.conf")\n', "import loop_lib as ll",
                     "ll.CONF", [(2, "conf constant")]),
                    ("multi-argument-path", 'CONF = Path(ROOT, "cfg", ".unattended.conf")\n',
                     "import loop_lib as ll", "ll.CONF", [(2, "conf constant")]),
                    ("aliased-from-import", 'CONF = ROOT / ".unattended.conf"\n', "from loop_lib import CONF as C",
                     "C", [(2, "conf constant")]),
                    ("non-conf-join", 'OTHER = ROOT / "other.toml"\n', "import loop_lib as ll", "ll.OTHER", []),
                    # TOOL-dDeclaredLoop-89 S3: a global loader and module-level walrus, for and with targets,
                    # then a global loader naming no conf and one naming it in its docstring alone
                    ("global-loader", 'CONF = None\ndef load(): global CONF; CONF = HERE.parent / ".unattended.conf"\n',
                     "import loop_lib as ll", "ll.CONF", [(2, "conf constant")]),
                    ("with-held-loader", 'def read_kit_conf():\n    global KIT_CONF\n'
                                         '    with open(ROOT / ".memory-tree.conf") as fh:\n'
                                         '        KIT_CONF = fh.read()\n',
                     "import loop_lib as ll", "ll.KIT_CONF", [(2, "conf constant")]),
                    ("walrus-target", 'if (WCONF := ROOT / ".unattended.conf").exists(): pass\n',
                     "import loop_lib as ll", "ll.WCONF", [(2, "conf constant")]),
                    ("for-target", 'for FCONF in (ROOT / ".memory-tree.conf",): pass\n', "import loop_lib as ll",
                     "ll.FCONF", [(2, "conf constant")]),
                    ("with-target", 'with open(ROOT / ".unattended.conf") as FH: pass\n', "import loop_lib as ll",
                     "ll.FH", [(2, "conf constant")]),
                    ("plain-global", "def reset(): global COUNTER; COUNTER = 0\n", "import loop_lib as ll",
                     "ll.COUNTER", []),
                    ("docstring-loader", 'def note(): """Reads .unattended.conf."""; global NOTE; NOTE = 1\n',
                     "import loop_lib as ll", "ll.NOTE", []),
                    # TOOL-dDeclaredLoop-90 S2: charge rule 2's whole predicate, a conf name in a value-less
                    # annotation, in a subscript target and in a module-level for body
                    ("annotation-only", 'ANNO: Literal[".unattended.conf"]\n', "import loop_lib as ll", "ll.ANNO",
                     [(2, "conf constant")]),
                    ("subscript-target", 'D[".memory-tree.conf"] = 1\n', "import loop_lib as ll", "ll.D",
                     [(2, "conf constant")]),
                    ("for-body", 'for _i in range(1): FOR_BODY = ROOT / ".unattended.conf"\n', "import loop_lib as ll",
                     "ll.FOR_BODY", [(2, "conf constant")])):
                write_fixture_files(top / name, {"loop_lib.py": lib,
                                                 name + ".py": "%s\ndef read_root(): return open(%s).read()\n" % (
                                                     opens, reads)})
                got = derive_conf_reads(top / name / (name + ".py"))
                print("%s: fixture · conf-read-forms · %s · %s" % (SAY, name, ", ".join(
                    "line %d %s" % hit for hit in got) or "no hit"))
                check(got == owed, "%s answered %s, owed %s" % (name, got, owed))
            # TOOL-dDeclaredLoop-91 S3, S4: the module-scope group, a name bound in a part of a definition Python
            # evaluates in module scope, then a walrus in a function body and one in a class body, the liveness
            # negatives; each row's loop_lib.py also runs by exec, and every name it binds to a conf's path must
            # be one derive_conf_constants answers, the over-report of the lambda row's own target aside
            for name, lib, reads, owed in (
                    ("class-global", "class Cfg:\n"
                                     "    global CONF_K\n"
                                     '    CONF_K = ROOT / ".unattended.conf"\n', "ll.CONF_K", [(2, "conf constant")]),
                    ("default-walrus", "def f(x=(DCONF := ROOT\n"
                                       '                  / ".memory-tree.conf")): pass\n', "ll.DCONF",
                     [(2, "conf constant")]),
                    ("keyword-default-walrus", "def fk(*, y=(KWCONF := ROOT\n"
                                               '                     / ".unattended.conf")): pass\n', "ll.KWCONF",
                     [(2, "conf constant")]),
                    ("lambda-default-walrus", "g = lambda x=(LCONF := ROOT\n"
                                              '              / ".unattended.conf"): x\n', "ll.LCONF",
                     [(2, "conf constant")]),
                    ("class-base-walrus", "class KB(type(BCONF :=\n"
                                          '                ".memory-tree.conf")): pass\n', "ll.BCONF",
                     [(2, "conf constant")]),
                    ("decorator-walrus", '@(lambda fn, _=(DECO := ROOT / ".unattended.conf"): fn)\n'
                                         "def h(): pass\n", "ll.DECO", [(2, "conf constant")]),
                    ("function-body-walrus", "def h2():\n"
                                             '    (HLOCAL := ".unattended.conf")\n', "ll.HLOCAL", []),
                    ("class-body-walrus", "class K2:\n"
                                          '    KATTR = (KW := ".unattended.conf")\n', "ll.KW", [])):
                write_fixture_files(top / name, {"loop_lib.py": lib,
                                                 name + ".py": "import loop_lib as ll\ndef read_root(): return open(%s)"
                                                               ".read()\n" % reads})
                got = derive_conf_reads(top / name / (name + ".py"))
                print("%s: fixture · conf-read-forms · %s · %s" % (SAY, name, ", ".join(
                    "line %d %s" % hit for hit in got) or "no hit"))
                check(got == owed, "%s answered %s, owed %s" % (name, got, owed))
                ns = {"ROOT": pathlib.PurePath(".")}
                exec(lib, ns)   # the row's own literal above, no input from outside the plant
                bound = {k for k, v in ns.items() if k != "__builtins__" and check_conf_name(ast.Constant(str(v)))}
                missed = ", ".join(sorted(bound - derive_conf_constants(top / name / "loop_lib.py")))
                print("%s: fixture · parity · %s · missed %s" % (SAY, name, missed or "none"))
                check(not missed, "%s: the rule missed %s, which the execution bound" % (name, missed))
            write_fixture_files(top / "no-lib", {"constant.py": first})
            try:
                got = "answered %s" % derive_conf_reads(top / "no-lib" / "constant.py")
            except LoopError as e:   # TOOL-dDeclaredLoop-86 S13: a missing sibling is a refusal, never an empty set
                got = "raised %s" % e
            print("%s: fixture · conf-read-forms · constant, no loop_lib beside it · %s" % (SAY, got))
            check(got.startswith("raised") and "loop_lib.py" in got, "the module with no loop_lib beside it %s" % got)
            # TOOL-dDeclaredLoop-88 S33: the route to tree_lib unlocatable, blocked from import and unparseable,
            # each a LoopError naming the update command, never a traceback
            import unittest.mock
            import loop_lib
            broken = top / "broken-tree-lib"
            write_fixture_files(broken, {"tree_lib.py": "def derive_docstring_ids(:\n"})
            # TOOL-dDeclaredLoop-94 S21: one raising at import and one lacking both names, each its own folder
            raising, lacking = top / "raising-tree-lib", top / "lacking-tree-lib"
            write_fixture_files(raising, {"tree_lib.py": 'raise RuntimeError("fx stand-in")\n'})
            write_fixture_files(lacking, {"tree_lib.py": "FX_NEITHER = 1\n"})

            def read_unlocatable(anchor):
                raise LookupError("no memory-tree kit holding %s: looked in fx-a, fx-b and fx-c" % anchor)
            for name, folder, swap, block, owed in (
                    ("unlocatable", broken, read_unlocatable, False, "looked in"),
                    ("blocked", broken, loop_lib.read_memory_tree, True, "None in sys.modules"),
                    ("unparseable", broken, lambda anchor: broken, False, "SyntaxError"),
                    ("raising", raising, lambda anchor: raising, False, "RuntimeError"),
                    ("lacking both", lacking, lambda anchor: lacking, False,
                     "derive_docstring_ids, derive_constant_charges")):
                with contextlib.ExitStack() as stack:
                    stack.enter_context(unittest.mock.patch.dict(sys.modules))
                    stack.enter_context(unittest.mock.patch.object(sys, "path", [str(folder), *sys.path]))
                    stack.enter_context(unittest.mock.patch.object(loop_lib, "read_memory_tree", swap))
                    sys.modules.pop("tree_lib", None)
                    if block:
                        sys.modules["tree_lib"] = None
                    try:
                        got = "answered %s" % derive_conf_reads(top / "with-lib" / "constant.py")
                    except LoopError as e:
                        got = "raised %s" % e
                print("%s: fixture · conf-read-forms · tree_lib %s · %s" % (SAY, name, got))
                check(got.startswith("raised") and "govkit update --kits memory-tree" in got and owed in got,
                      "tree_lib %s %s, owed a LoopError naming %r and the update command" % (name, got, owed))
            # TOOL-dDeclaredLoop-98 S1 to S3: a call of each declared conf reader in three spellings, each call
            # line owed a reader call; the tuple is read, never typed here
            members = loop_lib.CONF_READERS
            check(members, "CONF_READERS is empty")
            lines, owed = ["import loop_lib", "import loop_lib as ll"], {}
            for i, m in enumerate(members):
                lines.append("from loop_lib import %s as r%d" % (m, i))
                for tag, callee in (("a", "loop_lib." + m), ("b", "ll." + m), ("c", "r%d" % i)):
                    lines.append("def call_%d_%s(tree): return %s(tree)" % (i, tag, callee))
                    owed[len(lines)] = (m, callee)
            write_fixture_files(top / "with-lib", {"reader_calls.py": "\n".join(lines) + "\n"})
            got = {line for line, kind in derive_conf_reads(top / "with-lib" / "reader_calls.py")
                   if kind == "reader call"}
            print("%s: fixture · conf-read-forms · declared readers seen · %d/%d calls answered · %s" % (
                SAY, len(got & owed.keys()), len(owed), ", ".join(members)))
            for line, (m, callee) in owed.items():
                check(line in got, "declared reader not answered: %s as %s" % (m, callee))
        else:
            write_budget_plant(top, case)
        draw = ["draw", "--build", FX_BUILD, "--cause", "fix-pass", "--item"]
        if case == "mint-each-lap":
            run_move("designing", "item.design.exit", "recorded")
            for lap in range(1, 10):
                write_spec(lap + 2)
                rc, out = run_verb(draw + ["TOOL-%s-%d" % (FX_BUILD, lap + 2)])
                owed = (0, "drawn · draw · fix-pass") if lap < 9 else (3, "exhausted · %s · 8/8" % FX_BUILD)
                check(rc == owed[0] and owed[1] in out and ("%d/8" % lap in out or lap == 9),
                      "lap %d answered %r" % (lap, out.strip()))
            rows = read_rows()
            check(rows.count(FREEZE_ROW % (2, 8)) == 1, "the freeze row is not budget · frozen · 2 unit(s) · 8")
            check(sum(r.startswith("draw · ") for r in rows) == 8 and all(r.endswith("/8") for r in rows[1:]),
                  "the draws are not eight, each of 8")
        elif case == "before-freeze":
            run_move("planning", "item.plan.exit", "recorded")
            for _lap in range(4):
                run_move("designing", "item.design.decompose", "goal-fork")
                run_move("planning", "item.plan.exit", "recorded")
            count = len(read_transition_records(FX_BUILD, top))
            refused = run_move("designing", "item.design.decompose", "goal-fork")
            check(refused and "spent" in refused, "the fifth route back was not refused as spent")
            check(len(read_transition_records(FX_BUILD, top)) == count, "the refused move wrote a record")
            homes = [r for r in read_transition_records(FX_BUILD, top) if "draw · route-back" in pathlib.Path(
                top, r["path"]).read_text(encoding="utf-8")]
            rows = read_rows()
            check(rows == ["draw · route-back · item.design.decompose · %d/4" % n for n in range(1, 5)],
                  "the draws do not read 1/4 to 4/4")
            check(len(homes) == 4, "the four draws sit on %d record(s), not four" % len(homes))
        elif case == "stale-verdict":
            run_move("planning", "item.plan.exit", "recorded")
            before = read_rows()
            answer = classify_repeat("stale-verdict")
            print("%s: fixture · classify_repeat · stale-verdict · %s" % (SAY, answer))
            if answer != "contention":   # a repetition that is not contention draws, as the driver's sites do
                record_draw(FX_BUILD, answer, FX_UNIT, top)
            check(answer == "contention", "a verdict staled by another build's landing classified %s" % answer)
            check(read_rows() == before, "the re-verification wrote a draw row")
        elif case in ("patch-draw", "patch-trailer-only", "patch-archived"):
            head = run_fixture_git(top, "rev-parse", "HEAD")
            move = {"build": FX_BUILD, "from": "deploying", "to": "landed", "item": "item.deploy.close", "sha": head[:8]}
            files = {"memory/builds/%s/README.md" % PATCH_BUILD:
                     "---\nslug: %s\nnode: a\nopened: 2026-01-01\nstreams: tooling\nroster: TOOL\n"
                     "ids: TOOL-%s-1\nparents: %s\n---\n# %s\n" % (PATCH_BUILD, PATCH_BUILD, FX_BUILD, PATCH_BUILD)}
            if case == "patch-draw":
                write_transition_record(top, FX_UNIT, move)
            else:   # tFix lands by its trailer alone, and the patch build holds a run-state file
                files["memory/builds/%s/RUN.md" % PATCH_BUILD] = PLANT_RUN.replace(FX_BUILD, PATCH_BUILD)
            write_fixture_files(top, files)
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "landed\n\n%s" % render_transition_trailer(move))
            patch = {"build": PATCH_BUILD, "from": "planning", "to": "designing", "item": "item.plan.exit",
                     "sha": head[:8], "scenario": PATCH_SCENARIO}
            run_fixture_git(top, "commit", "-q", "--allow-empty", "-m", "patch\n\n%s" % render_transition_trailer(patch))
            patch_draw = ["draw", "--build", PATCH_BUILD, "--cause", "fix-pass", "--item", "item.deploy.close"]
            rc, out = run_verb(patch_draw)
            row = "draw · patch:%s · item.deploy.close · 1/4" % PATCH_BUILD
            check(rc == 0 and row in out, "the patch build's draw printed %r" % out.strip())
            if case == "patch-trailer-only":
                patch_run = read_run_file(top, PATCH_BUILD)
                marks = [SUFFIXED.fullmatch(hit.group(2)) for hit in map(
                    RUN_ROW.fullmatch, patch_run.read_text(encoding="utf-8").split("\n")) if hit]
                held = [parse_draw_id(m.group(1)) + (m.group(2),) for m in marks if m]
                check(len(held) == len(marks) and (row, FX_BUILD) in [(r, b) for r, _i, b in held]
                      and all(i for r, i, _b in held if r.startswith("draw · ")),
                      "the run-state file of %s does not carry %s, its draw id, then · budget %s" % (
                          PATCH_BUILD, row, FX_BUILD))
                states = (budget_state(FX_BUILD, top), budget_state(PATCH_BUILD, top))
                print("%s: fixture · budget_state · %s %s · %s %s" % (SAY, FX_BUILD, states[0], PATCH_BUILD, states[1]))
                check(states == ("unfrozen 1/4", "unfrozen 0/4"), "the states read %s and %s" % states)
                patch_run.unlink()
                rc, out = run_verb(patch_draw)
                check(rc == 2 and "refused" in out and PATCH_BUILD in out,
                      "the draw with no run-state file of %s was not refused naming it" % PATCH_BUILD)
            elif case == "patch-archived":   # the patch build's record rotated as the driver's preflight rotates it
                patch_run = read_run_file(top, PATCH_BUILD)
                shutil.move(str(patch_run), str(patch_run.with_name("RUN.ABORTED.0000bbbb.md")))
                write_fixture_files(top, {patch_run.relative_to(top).as_posix(): PLANT_RUN.replace(FX_BUILD, PATCH_BUILD)})
                states = (budget_state(FX_BUILD, top), budget_state(PATCH_BUILD, top))
                print("%s: fixture · budget_state · %s %s · %s %s" % (SAY, FX_BUILD, states[0], PATCH_BUILD, states[1]))
                check(states == ("unfrozen 1/4", "unfrozen 0/4"), "the states read %s and %s" % states)
            else:
                newest = read_transition_records(FX_BUILD, top)[-1]["path"]
                check(row in pathlib.Path(top, newest).read_text(encoding="utf-8"), "%s does not carry the row" % newest)
                state = read_transitions(FX_BUILD, top)[0]["to"]
                print("%s: fixture · %s reads %s" % (SAY, FX_BUILD, state))
                check(state == "landed", "%s reads %s after the draw" % (FX_BUILD, state))
                rc, out = run_verb(["draw", "--build", FX_BUILD, "--cause", "patch:%s" % PATCH_BUILD, "--item", "x"])
                check(rc == 2 and "derived" in out, "the derived cause given was not refused as derived")
        elif case == "route-backs":
            run_move("planning", "item.plan.exit", "recorded")
            for item in ["TOOL-%s-1" % FX_BUILD] * 4 + ["TOOL-%s-2" % FX_BUILD]:
                record_draw(FX_BUILD, "fix-pass", item, top)
            looped = count_returns(FX_BUILD, "TOOL-%s-1" % FX_BUILD, top)
            other = count_returns(FX_BUILD, "TOOL-%s-2" % FX_BUILD, top)
            targets = [promotion_target(FX_BUILD, "TOOL-%s-1" % FX_BUILD, b, top) for b in (True, False)]
            record_draw(FX_BUILD, "fix-pass", "TOOL-%s-2" % FX_BUILD, top)
            targets.append(promotion_target(FX_BUILD, "TOOL-%s-1" % FX_BUILD, True, top))
            print("%s: fixture · returns %s · %s · targets %s" % (SAY, looped, other, " ".join(targets)))
            check(looped == (4, "non-converging"), "the item returned four times reads %s" % (looped,))
            check(other == (1, "converging"), "the other item reads %s" % (other,))
            check(targets == ["unit", "ask", "on-exhausted"], "the targets read %s" % " ".join(targets))
        elif case == "unknown-cause":
            run_move("planning", "item.plan.exit", "recorded")
            rc, out = run_verb(["draw", "--build", FX_BUILD, "--cause", "retry", "--item", FX_UNIT])
            check(rc == 2 and "retry" in out and "route-back" in out, "the cause retry was not refused by name")
            check(read_rows() == [], "the refused cause wrote a row")
        elif case == "re-entry":
            run_move("designing", "item.design.exit", "recorded")
            run_move("building", "item.build.unit-pass", "spec-wrong")
            write_spec(4)
            run_move("designing", "item.design.exit", "recorded")
            rows = read_rows()
            check([r for r in rows if r.startswith("budget · ")] == [FREEZE_ROW % (3, 10)],
                  "the records do not carry one budget · frozen · 3 unit(s) · 10 row")
        elif case == "pre-spec":
            run_verb(draw + [FX_UNIT])
            run_verb(draw + [FX_UNIT])
            write_spec(1)
            run_move("planning", "item.plan.exit", "recorded")
            run_verb(draw + [FX_UNIT])
            run_text = read_run_file(top, FX_BUILD).read_text(encoding="utf-8")
            first = read_transition_records(FX_BUILD, top)[0]["path"]
            text = pathlib.Path(top, first).read_text(encoding="utf-8")
            owed = ["draw · fix-pass · %s · %d/4" % (FX_UNIT, n) for n in (1, 2, 3)]
            print("%s: fixture · first record %s" % (SAY, first))
            check(sum(r in run_text for r in owed[:2]) == 2 and owed[2] not in run_text,
                  "the run-state file does not carry the first two rows alone")
            held = [parse_draw_id(ln) for ln in text.split("\n") if ln.startswith("draw · ")]
            copied = [parse_draw_id(hit.group(2))[1] for hit in map(RUN_ROW.fullmatch, run_text.split("\n")) if hit]
            check([r for r, _i in held] == owed, "the first log record does not carry the three rows in order")
            check(all(i for _r, i in held) and [i for _r, i in held[:2]] == copied,
                  "the first log record's rows do not carry draw ids, its two copies the ids of the run-state rows")
        elif case == "trailer-only":
            run_move("designing", "item.design.exit", "recorded")
            run_verb(draw + [FX_UNIT])
            run_move("building", "item.build.unit-pass", "spec-wrong")
            trailers = [t for _c, t in read_transition_commits(FX_BUILD, top)[0]]
            for t in trailers:
                print("%s: fixture · trailer %s" % (SAY, render_transition_trailer(t).split(": ", 1)[1]))
            run_text = read_run_file(top, FX_BUILD).read_text(encoding="utf-8")
            state = budget_state(FX_BUILD, top)
            print("%s: fixture · budget_state · %s" % (SAY, state))
            check(len(trailers) == 2 and trailers[0].get("budget") == "frozen@1@6",
                  "the move into building does not carry budget=frozen@1@6")
            held = [parse_draw_id(hit.group(2)) for hit in map(RUN_ROW.fullmatch, run_text.split("\n")) if hit]
            check(any(r == "draw · fix-pass · %s · 1/6" % FX_UNIT for r, _i in held)
                  and all(i for r, i in held if r.startswith("draw · ")),
                  "RUN.md does not carry the fix-pass draw 1/6, each of its draw rows with a draw id")
            check(len(trailers) == 2 and trailers[1].get("draw") == "route-back@item.build.unit-pass@2+6",
                  "the backward move does not carry draw=route-back@item.build.unit-pass@2+6")
            check(state == "open 2/6", "budget_state answers %s" % state)
            lines, findings = check_transition_channels(FX_BUILD, top)
            for text in findings + lines:
                print("%s: fixture · check · %s" % (SAY, text))
            check(not findings and lines[-1].endswith(" 0 finding(s)"), "the channel check reads %s" % lines[-1])
            refused = run_move("designing", "item.design.exit", "recorded", {"draw": "x"})
            check(refused and "--field draw is derived" in refused, "the field draw=x was not refused as derived")
        elif case == "log-dropped":
            run_move("planning", "item.plan.exit", "recorded")
            write_fixture_files(top, {".governance/policy.toml": PLANT_TRAILER})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "transitions.record drops log")
            run_move("designing", "item.design.decompose", "goal-fork")
            newest = read_transition_records(FX_BUILD, top)[-1]["path"]
            row = "draw · route-back · item.design.decompose · 1/4"
            shown = run_fixture_git(top, "show", "--name-only", "--format=%(trailers:key=Gov-Transition,valueonly)")
            state = budget_state(FX_BUILD, top)
            print("%s: fixture · move · %s · budget_state · %s" % (SAY, " / ".join(ln for ln in shown.split("\n") if ln), state))
            held = [parse_draw_id(ln) for ln in pathlib.Path(top, newest).read_text(encoding="utf-8").split("\n")
                    if ln.startswith("draw · ")]
            check(any(r == row for r, _i in held) and all(i for _r, i in held),
                  "%s does not carry %s, each of its draw rows with a draw id" % (newest, row))
            check(newest in shown.split("\n") and "draw=" not in shown,
                  "the move's commit does not hold %s alone of the budget, its trailer free of draw=" % newest)
            check(state == "unfrozen 1/4", "budget_state answers %s" % state)
        elif case in ("parallel-append", "parallel-append-uneven"):
            run_move("planning", "item.plan.exit", "recorded")
            rel = read_transition_records(FX_BUILD, top)[0]["path"]
            # the merge attribute this tree answers for the record's path, never a literal in the plant
            rc, repo_top = read_git(KIT, "rev-parse", "--show-toplevel")
            attr = "unspecified"
            if rc == 0:
                attr = read_git(repo_top, "check-attr", "merge", "--", rel)[1].rsplit(": ", 1)[-1] or attr
            print("%s: fixture · this tree's merge attribute for %s · %s" % (SAY, rel, attr))
            if attr not in ("unspecified", "unset"):
                write_fixture_files(top, {".gitattributes": "%s merge=%s\n" % (rel, attr)})
                run_fixture_git(top, "add", "-A")
                run_fixture_git(top, "commit", "-q", "-m", "the merge attribute")
            run_fixture_git(top, "branch", "side")
            path = pathlib.Path(top, rel)
            # parallel-append draws main's item again on side, its id alone differing; the uneven case two others
            for branch, n in [("main", 1)] + [("side", n) for n in ((1,) if case == "parallel-append" else (2, 3))]:
                run_fixture_git(top, "checkout", "-q", branch)
                before = path.read_bytes()
                record_draw(FX_BUILD, "fix-pass", "TOOL-%s-%d" % (FX_BUILD, n), top)
                after = path.read_bytes()
                check(after.startswith(before) and len(after) > len(before),
                      "the draw of TOOL-%s-%d on %s rewrote %s rather than appending to it" % (FX_BUILD, n, branch, rel))
            run_fixture_git(top, "checkout", "-q", "main")
            rc = read_git(top, "merge", "--no-edit", "side")[0]
            print("%s: fixture · merge side · exit %d" % (SAY, rc))
            check(rc == 0, "the merge of side conflicted on %s, whose merge attribute here is %s" % (rel, attr))
            if rc == 0 and case == "parallel-append-uneven":
                try:
                    state, rows = budget_state(FX_BUILD, top), read_rows()
                except ValueError as e:
                    state, rows = "refused: %s" % e, []
                print("%s: fixture · budget_state · %s" % (SAY, state))
                check(len(rows) == 3 and all(r.startswith("draw · ") for r in rows) and len(set(rows)) == 3,
                      "the merged record does not carry three distinct draw rows, none twice")
                check(state == "unfrozen 3/4", "budget_state answers %s" % state)
            elif rc == 0:
                try:   # the typed-figure refusal reads as a miss, not a traceback
                    state = budget_state(FX_BUILD, top)
                    rows = read_rows()
                    ids = {parse_draw_id(r)[1] for r in read_budget_rows(FX_BUILD, top)["rows"]}
                except ValueError as e:
                    state, rows, ids = "refused: %s" % e, [], set()
                print("%s: fixture · budget_state · %s" % (SAY, state))
                check(state == "unfrozen 2/4", "budget_state answers %s" % state)
                check(rows == ["draw · fix-pass · TOOL-%s-1 · 1/4" % FX_BUILD] * 2 and len(ids) == 2 and None not in ids,
                      "the record does not carry both 1/4 rows of one item, their draw ids differing")
                rc, out = run_verb(draw + ["TOOL-%s-3" % FX_BUILD])
                lines = out.strip().split("\n")
                third = parse_draw_id(lines[0].split(" · drawn · ", 1)[-1])
                check(rc == 0 and lines[0].startswith("%s: budget · drawn · " % SAY) and third[0].endswith(" 3/4")
                      and third[1] and len(lines) == 2 and lines[1].endswith("typed 1, derived 2"),
                      "the third draw answered %r, exit %d" % (out.strip(), rc))
        elif case == "draw-id-rows":
            run_move("planning", "item.plan.exit", "recorded")
            path = pathlib.Path(top, read_transition_records(FX_BUILD, top)[-1]["path"])
            row = "draw · fix-pass · %s · %%d/4" % FX_UNIT
            bad = "%s · not-an-id" % (row % 4)
            states = []
            for add in ([row % 1] * 2, ["%s · 20261116T000000Z-0a1b2c" % (row % 3)] * 2, [bad]):
                write_budget_rows(path, add, True)
                try:
                    states.append(budget_state(FX_BUILD, top))
                except ValueError as e:
                    states.append("refused: %s" % e)
                if len(states) == 1:   # TOOL-dDeclaredLoop-75 AC2: each id-less row named, before the id-bearing step
                    rc, out = run_verb(["ending", "--build", FX_BUILD, "--explain"])
                    named = [ln for ln in out.splitlines() if ln.startswith("%s: budget · no draw id · " % SAY)]
                    check(rc == 0 and named == ["%s: budget · no draw id · %s" % (SAY, row % 1)] * 2,
                          "ending --explain over two id-less rows named %r, exit %d" % (named, rc))
            print("%s: fixture · budget_state · %s" % (SAY, " / ".join(states)))
            check(states[0] == "unfrozen 2/4", "two identical id-less rows read %s" % states[0])
            check(states[1] == "unfrozen 3/4", "one id-bearing row twice reads %s" % states[1])
            check(states[2].startswith("refused: ") and repr(bad) in states[2] and "outside its grammar" in states[2],
                  "the row ending · not-an-id reads %s" % states[2])
        elif case == "unrecorded":
            run_verb(draw + [FX_UNIT])
            run = read_run_file(top, FX_BUILD)
            rotated = run.with_name("RUN.LANDED.0000aaaa.md")
            shutil.move(str(run), str(rotated))
            write_fixture_files(top, {run.relative_to(top).as_posix(): PLANT_RUN})
            run_verb(draw + [FX_UNIT])
            old, new = rotated.read_text(encoding="utf-8"), run.read_text(encoding="utf-8")
            check(FREEZE_ROW % (2, 8) in old and "fix-pass · %s · 1/8" % FX_UNIT in old,
                  "the first file does not carry the freeze at 2 units and 1/8")
            check("fix-pass · %s · 2/8" % FX_UNIT in new and "budget · " not in new,
                  "the new file does not carry 2/8 alone")
        elif case == "ending":   # TOOL-dDeclaredLoop-31: AC1's line under a spent budget, then the default value
            read_memory_tree("build_records.py")
            from build_records import write_disposition
            write_disposition(top, FX_BUILD, FX_UNIT, EXHAUSTED_ITEM, "continue", "terminal")
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "the owner's disposition")
            rc, out = run_verb(["ending", "--build", FX_BUILD])
            owed = "%s: budget · ending · descope · spent 0/0 · open %s · disposed continue" % (SAY, FX_UNIT)
            check(rc == 0 and out.strip() == owed, "the spent build's ending read %r, exit %d" % (out.strip(), rc))
            write_fixture_files(top, {".governance/policy.toml": "[flow]\n"})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "the default value")
            rc, out = run_verb(["ending", "--build", FX_BUILD])
            check(rc == 0 and "ending · none · unfrozen" in out, "the default value's ending read %r" % out.strip())
        elif case == "draws-survive-rotation":
            run_verb(draw + [FX_UNIT])
            run_verb(draw + [FX_UNIT])
            run = read_run_file(top, FX_BUILD)
            shutil.move(str(run), str(run.with_name("RUN.ABORTED.0000aaaa.md")))   # an aborted run's record
            write_fixture_files(top, {run.relative_to(top).as_posix(): PLANT_RUN})
            run_verb(draw + [FX_UNIT])
            state = budget_state(FX_BUILD, top)
            print("%s: fixture · budget_state · %s" % (SAY, state))
            check(state == "open 3/6", "budget_state answers %s" % state)
            check("budget · " not in run.read_text(encoding="utf-8"), "the fresh RUN.md holds a budget · row")
        elif case == "unattended-root":   # TOOL-dDeclaredLoop-72 AC1: the root the driver's conf names
            run_fixture_git(top, "mv", "memory", "records")
            write_fixture_files(top, {".memory-tree.conf": 'FAMILIES="tool:TOOL"\n', ".unattended.conf": "MEMORY_ROOT=records\n",
                                      "records/builds/%s/RUN.md" % FX_BUILD: PLANT_RUN})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "the driver's records root")
            rcs = [run_verb(draw + [FX_UNIT])[0] for _n in range(2)]
            text = (top / "records" / "builds" / FX_BUILD / "RUN.md").read_text(encoding="utf-8")
            state = budget_state(FX_BUILD, top)
            print("%s: fixture · budget_state · %s" % (SAY, state))
            check(rcs == [0, 0], "the draws exited %s" % rcs)
            check(FREEZE_ROW % (1, 6) in text and all("fix-pass · %s · %d/6 · " % (FX_UNIT, n) in text for n in (1, 2)),
                  "the run-state file under records/ does not hold the freeze row and both draws")
            check(state == "open 2/6", "budget_state answers %s" % state)
        elif case == "attr-missing":   # TOOL-dDeclaredLoop-67 AC11 (S34): a log record no union line covers
            run_move("planning", "item.plan.exit", "recorded")
            notice = "%s: budget · notice · " % SAY
            for name, attrs, owed in (("no .gitattributes", None, 1), ("the union line", "merge=union", 0)):
                if attrs:
                    write_fixture_files(top, {".gitattributes": "%s/builds/*/build/*-transition-*.md %s\n" % (
                        resolve_memory_root(top), attrs)})
                    run_fixture_git(top, "add", "-A")
                    run_fixture_git(top, "commit", "-q", "-m", "the transition records merge as union")
                rc, out = run_verb(draw + [FX_UNIT])
                said = [ln for ln in out.splitlines() if ln.startswith(notice)]
                check(rc == 0 and len(said) == owed and all("merge=union to .gitattributes" in ln for ln in said),
                      "under %s the draw exited %d printing %d notice(s), owed %d: %r" % (name, rc, len(said), owed,
                                                                                         out.strip()))
        elif case in ("patch-concurrent", "patch-claims-unread"):
            # TOOL-dDeclaredLoop-67 AC24 (S35): two live patch runs of one origin; TOOL-dDeclaredLoop-75 AC28 (S28):
            # a claim read that fails refuses the draw
            import subprocess
            from loop_lib import resolve_kit_dir
            from loop_witness import HOLD_CONF, read_clean_env, resolve_bash
            driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
            bash = resolve_bash(driver)
            if bash is None:
                raise LookupError("no bash can run %s" % driver.as_posix())
            head = run_fixture_git(top, "rev-parse", "HEAD")
            landed = {"build": FX_BUILD, "from": "deploying", "to": "landed", "item": "item.deploy.close", "sha": head[:8]}
            write_transition_record(top, FX_UNIT, landed)
            peer = PATCH_BUILD + "Two"
            readme = ("---\nslug: %s\nnode: a\nopened: 2026-01-01\nstreams: tooling\nroster: TOOL\nids: TOOL-%s-1\n"
                      "parents: %s\n---\n# %s\n")
            write_fixture_files(top, dict({"%s/builds/%s/README.md" % (resolve_memory_root(top), b): readme % (
                b, b, FX_BUILD, b) for b in (PATCH_BUILD, peer)}, **{".unattended.conf": HOLD_CONF}))
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "landed\n\n%s" % render_transition_trailer(landed))
            for b in (PATCH_BUILD, peer):
                patch = {"build": b, "from": "planning", "to": "designing", "item": "item.plan.exit",
                         "sha": head[:8], "scenario": PATCH_SCENARIO}
                run_fixture_git(top, "commit", "-q", "--allow-empty", "-m", "patch\n\n%s" % render_transition_trailer(patch))
            record = pathlib.Path(top, read_transition_records(FX_BUILD, top)[-1]["path"])
            stand_in = {"patch-concurrent": 'CLAIM_ROWS=$(printf "%s\\tnode-b\\tlive\\t5\\tlive\\t-\\t-\\t-\\t-\\t-\\t-" '
                                            '"$fx_claimed"); return 0;',
                        "patch-claims-unread": 'CL_WHY="fx: the remote did not answer"; return 1;'}[case]
            script = ('load_driver_conf || exit 3; fx_claimed=$1; read_claims() { %s }; '
                      'run_budget_draw "$2" fix-pass item.deploy.close; '
                      'printf "draw · rc %%s · %%s\\n" "$_bd_rc" "$_bd_why"' % stand_in)
            row = "draw · patch:%s · item.deploy.close · 1/4" % PATCH_BUILD
            runs = (("a live patch peer", peer, True), ("a live build that is no patch", FX_BUILD, False))
            if case == "patch-claims-unread":
                runs = (("a claim read that failed", "", None),)
            for name, claimed, refused in runs:
                before = record.read_bytes()
                p = subprocess.run([bash, "-c", '. "$1" || exit 2; shift; ' + script, "_", driver.as_posix(), claimed,
                                    PATCH_BUILD], cwd=str(top), capture_output=True, text=True, encoding="utf-8",
                                   errors="replace", env=dict(read_clean_env(), GOV_DEFAULT_BRANCH="main"), timeout=600)
                said = next((ln for ln in p.stdout.splitlines() if ln.startswith("draw · rc ")), "no draw line")
                print("%s: fixture · %s · %s · exit %d · %s" % (SAY, case, name, p.returncode, said))
                if refused is None:
                    owed = "draw · rc 2 · budget: patch draw refused — claims unread: fx: the remote did not answer"
                    spent = read_budget_rows(FX_BUILD, top)["spent"]
                    check(said == owed and record.read_bytes() == before and spent == 0,
                          "the draw over an unread claim set read %r, owed %r, the record %s, %d draw(s) counted" % (
                              said + " " + p.stderr.strip()[-300:], owed,
                              "unchanged" if record.read_bytes() == before else "written", spent))
                elif refused:
                    owed = "draw · rc 2 · budget: patch draw refused — %s on node-b is a live patch run of %s" % (peer, FX_BUILD)
                    check(said == owed and record.read_bytes() == before,
                          "the second patch draw read %r, owed %r, the record %s" % (
                              said + " " + p.stderr.strip()[-300:], owed,
                              "unchanged" if record.read_bytes() == before else "written"))
                else:
                    check(said.startswith("draw · rc 0 · %s: budget · drawn · %s" % (SAY, row)) and row in record.read_text(
                        encoding="utf-8"), "the control draw read %r: %s" % (said, p.stderr.strip()[-300:]))
        elif case == "confs-disagree":   # TOOL-dDeclaredLoop-72 AC3: two confs naming two roots
            write_fixture_files(top, {".unattended.conf": "MEMORY_ROOT=records\n"})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "the driver's conf naming another root")
            run = top / "memory" / "builds" / FX_BUILD / "RUN.md"
            before = run.read_bytes()
            rc, out = run_verb(draw + [FX_UNIT])
            owed = ("%s: budget · refused · records root: .unattended.conf says records, .memory-tree.conf says memory "
                    "— the driver writes under records" % SAY)
            check(rc == 2 and out.strip() == owed, "the draw answered %r, exit %d" % (out.strip(), rc))
            check(run.read_bytes() == before, "the refused draw changed the run-state file")
        elif case == "unset-driver-root":   # TOOL-dDeclaredLoop-75 AC6, AC7 (S6, S7): the driver's default root
            write_fixture_files(top, {".unattended.conf": 'PHASES_EXTRA=""\n',
                                      ".memory-tree.conf": 'MEMORY_ROOT=records\nFAMILIES="tool:TOOL"\n'})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "the driver's conf naming no root, the memory tree's records")
            run = top / "memory" / "builds" / FX_BUILD / "RUN.md"
            before = run.read_bytes()
            rc, out = run_verb(draw + [FX_UNIT])
            owed = "records root: .unattended.conf says memory, .memory-tree.conf says records"
            check(rc == 2 and owed in out, "the draw answered %r, exit %d, owed %r" % (out.strip(), rc, owed))
            check(run.read_bytes() == before, "the refused draw changed the run-state file")
            # the second half: the build moved under records, both confs naming it; one draw, so a file gives a row
            run_fixture_git(top, "mv", "memory", "records")
            write_fixture_files(top, {".unattended.conf": "MEMORY_ROOT=records\n"})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "both confs naming records")
            drawn = run_verb(draw + [FX_UNIT])[0]
            rc, out = run_verb(["ending", "--build", FX_BUILD, "--explain"])
            lines = out.strip().split("\n")
            check(drawn == 0 and rc == 0 and lines[0] == "%s: budget · root records · from .unattended.conf" % SAY
                  and len(lines) > 1 and lines[1].startswith("%s: budget · read records/builds/%s/" % (SAY, FX_BUILD)),
                  "the agreeing tree drew exit %d and explained %r, exit %d" % (drawn, out.strip(), rc))
        elif case == "trailing-slash-agree":   # TOOL-dDeclaredLoop-79 S20: one root spelled two ways agrees
            write_fixture_files(top, {".unattended.conf": "MEMORY_ROOT=memory/\n"})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "the driver's conf naming memory/")
            run = top / "memory" / "builds" / FX_BUILD / "RUN.md"
            rc, out = run_verb(draw + [FX_UNIT])
            check(rc == 0 and "fix-pass · %s · 1/" % FX_UNIT in run.read_text(encoding="utf-8"),
                  "the draw answered %r, exit %d, its row not under memory" % (out.strip(), rc))
        elif case == "no-confs":   # TOOL-dDeclaredLoop-79 S25: neither conf, the default root, no traceback
            run_fixture_git(top, "rm", "-q", ".memory-tree.conf")
            run_fixture_git(top, "commit", "-q", "-m", "no memory tree conf")
            try:
                got = resolve_memory_root(top)
            except Exception as e:   # noqa: BLE001  any raise is the miss this plant reads
                got = "%s: %s" % (type(e).__name__, e)
            print("%s: fixture · no-confs · root %s" % (SAY, got))
            check(got == "memory", "resolve_memory_root answered %r" % got)
        elif case == "driver-root-readers":   # TOOL-dDeclaredLoop-116 AC1 to AC5: each reader follows the driver's root
            read_memory_tree("build_records.py")
            from build_records import write_acceptance, write_disposition
            from loop_lib import read_builds_dir
            from loop_parents import read_withdrawn_parents
            from position import HANDOVER, derive_position, render_handover
            from upstream import write_upstream_record
            readme = "---\nslug: %s\nnode: a\nopened: 2026-01-01\nstreams: tooling\nroster: none\nids: none\n%s---\n# %s\n"
            write_fixture_files(top, {"memory/builds/%s/README.md" % FX_BUILD: readme % (FX_BUILD, "parents: tPar\n", FX_BUILD),
                                      "memory/builds/tPar/README.md": readme % ("tPar", "", "tPar"),
                                      "memory/builds/tPar/RUN.md": "# tPar run\n\n## Run facts\nphase: ABORTED\n"})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "a pass\n\nPass: %s" % FX_UNIT)
            sha = run_fixture_git(top, "rev-parse", "HEAD")
            write_acceptance(top, FX_BUILD, FX_UNIT, sha, "stand-in", [("true", 0, "0" * 12)], today="2026-01-01")
            write_disposition(top, FX_BUILD, FX_UNIT, EXHAUSTED_ITEM, "continue", "terminal")
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "the unit's records")
            run_fixture_git(top, "mv", "memory", "records")   # the move, as unattended-root makes it
            write_fixture_files(top, {".memory-tree.conf": 'FAMILIES="tool:TOOL"\n', ".unattended.conf": "MEMORY_ROOT=records\n",
                                      "records/builds/%s/RUN.md" % FX_BUILD: PLANT_RUN})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "the driver's records root")
            said = "%s: fixture · driver-root-readers · %%s · %%s" % SAY
            rc, out = run_verb(["ending", "--build", FX_BUILD])
            print(said % ("ending", out.strip()))
            check(rc == 0 and out.strip().endswith("disposed continue"), "ending read %r, exit %d" % (out.strip(), rc))
            before = os.environ.get(HANDOVER)
            os.environ[HANDOVER] = render_handover([(FX_UNIT, "READY")])
            try:
                pos = derive_position(top, FX_BUILD)
            finally:
                if before is None:
                    os.environ.pop(HANDOVER, None)
                else:
                    os.environ[HANDOVER] = before
            print(said % ("position", "read %s · reason %s" % (" | ".join(pos["read"]) or "none", pos["reason"] or "none")))
            folder = "records/builds/%s/" % FX_BUILD
            check(any(r.startswith(folder + "README.md@") for r in pos["read"])
                  and any(r.startswith(folder + "build/") and "-acceptance-" in r for r in pos["read"]),
                  "the position engine read no README and acceptance record under records: %s" % (pos["reason"] or pos["read"]))
            try:
                parents = read_withdrawn_parents(FX_BUILD, top)
            except ValueError as e:
                parents = str(e)
            print(said % ("parents", sorted(parents) if isinstance(parents, dict) else parents))
            check(isinstance(parents, dict) and list(parents) == ["tPar"] and "phase: ABORTED" in (parents["tPar"] or ""),
                  "the withdrawn parents read %r" % parents)
            owed = "records/builds/%s/build/2026-01-01-build-%s-upstream-1.md" % (FX_BUILD, FX_UNIT)
            try:
                got = write_upstream_record(top, FX_BUILD, FX_UNIT, "item.design.unit-spec", ["a line"], today="2026-01-01")
            except ValueError as e:
                got = str(e)
            print(said % ("upstream", got))
            check(got == owed and (top / owed).is_file(), "the upstream record answered %r, owed %r" % (got, owed))
            for name, conf in (("builds-dir", 'FAMILIES="tool:TOOL"\nDESIGN_RECORD="x"\n'),
                               ("builds-dir disagree", 'FAMILIES="tool:TOOL"\nDESIGN_RECORD="x"\nMEMORY_ROOT=memory\n')):
                write_fixture_files(top, {".memory-tree.conf": conf})   # the working file alone, both readers read it
                builds, why = read_builds_dir(KIT, top)
                print(said % (name, "%s · %s" % (builds.relative_to(top).as_posix() if builds else "none", why or "none")))
                if name == "builds-dir":
                    check((builds, why) == (top / "records" / "builds", ""), "%s answered %r, %r" % (name, builds, why))
                else:
                    check(builds is None and why.startswith("records root:"), "%s answered %r, %r" % (name, builds, why))
    except LookupError as e:
        print("%s: fixture · %s · unarmed: %s" % (SAY, case, e))
        return 2
    finally:
        os.chdir(here)
        remove_tree(top)
    print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
    return 0 if not misses else 1


def run_selftest():
    """Every plant, each held."""
    cases = [(c, ["--fixture", "--plant", c], 0, "%s: fixture · %s · held" % (SAY, c), "") for c in PLANTS]
    return run_selftest_cases(main, cases, "%s: budget selftest" % SAY)


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if argv == ["--selftest"]:
        return run_selftest()
    if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
        return run_budget_plant(argv[2])
    root = pathlib.Path.cwd()
    try:
        if argv == ["value"]:
            base, per, _routes = read_budget_value(root)
            print("base %d per-unit %d" % (base, per))
            return 0
        if argv[:1] == ["draw"]:
            ap = argparse.ArgumentParser(prog="budget.py draw", description="draw one repetition on a build's budget")
            for flag in ("--build", "--cause", "--item"):
                ap.add_argument(flag, required=True)
            args = ap.parse_args(argv[1:])
            notes, merges = [], []
            answer, said = record_draw(args.build, args.cause, args.item, root, notes=notes, merges=merges)
            if answer == "exhausted":
                print("%s: budget · exhausted · %s · %s" % (SAY, said, ENDING_KEY))
            else:
                print("%s: budget · drawn · %s" % (SAY, said))
            for note in notes:   # after the verdict, which the driver keeps as the first line
                print("%s: budget · disagrees · %s" % (SAY, note))
            for record, merge in merges:
                if merge != "union":
                    print("%s: budget · notice · %s merges as %s, not union: add %s/builds/*/build/*-transition-*.md "
                          "merge=union to .gitattributes" % (SAY, record, merge, resolve_memory_root(root)))
            return 3 if answer == "exhausted" else 0
        if argv[:1] == ["target"]:
            ap = argparse.ArgumentParser(prog="budget.py target", description="where a blocking item's open work goes")
            for flag in ("--build", "--item"):
                ap.add_argument(flag, required=True)
            args = ap.parse_args(argv[1:])
            print("%s: budget · target · %s" % (SAY, promotion_target(args.build, args.item, True, root)))
            return 0
        if argv[:1] == ["origin"]:   # TOOL-dDeclaredLoop-67 S35: the build a patch build's draws land on
            ap = argparse.ArgumentParser(prog="budget.py origin", description="the build a patch build draws on")
            ap.add_argument("--build", required=True)
            print("%s: budget · origin · %s" % (SAY, derive_patch_origin(ap.parse_args(argv[1:]).build, root) or "none"))
            return 0
        if argv[:1] == ["ending"]:
            ap = argparse.ArgumentParser(prog="budget.py ending", description="the ending a spent budget takes")
            ap.add_argument("--build", required=True)
            ap.add_argument("--explain", action="store_true")
            args = ap.parse_args(argv[1:])
            said = []
            if args.explain:   # TOOL-dDeclaredLoop-75 S2, S7: the root, its source, and what was read
                said.append("%s: budget · root %s · from %s" % ((SAY,) + resolve_memory_root_source(root)))
            held = read_budget_rows(args.build, root)
            if args.explain:
                said += ["%s: budget · read %s" % (SAY, p) for p in held["read"] or ["none"]]
                said += ["%s: budget · no draw id · %s" % (SAY, r) for r in held["rows"]
                         if (m := ROW.fullmatch(r)) and m.group(3) is not None and m.group(7) is None]
            said.append(read_ending(args.build, root, held))
            print("\n".join(said))
            return 0
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    except (ValueError, OSError) as e:
        print("%s: budget · refused · %s" % (SAY, e))
        return 2
    print("usage: python budget.py draw --build <slug> --cause <%s> --item <item> | value | target --build <slug> --item <item> | ending --build <slug> [--explain] | origin --build <slug> | --fixture --plant <%s> "
          "| --selftest" % ("|".join(CAUSES), "|".join(PLANTS)), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
