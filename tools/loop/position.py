#!/usr/bin/env python3
"""position.py — where a build is and what runs next, from witnesses alone (TOOL-dDeclaredLoop-7).

    python position.py <slug> [--json | --next-line]   # the position of <slug> in this working directory
    python position.py --fixture --plant <case>         # one fixture case
    python position.py --selftest                       # every case

`derive_position(repo, slug, definition=None)` reads only witnesses, each through the reader the tree
holds: the run branch's `--first-parent` commits and their `Pass:` trailers through the memory-tree
kit's `read_commits` and `derive_attribution` in the `replace` view; the build's recorded moves through
`loop_transition.read_transitions`, each checked by `loop_table.check_recorded_move`; the steps,
`[states]` and the transition rows through `read_transition_rows`; the items through
`loop_items.read_composition`, gov's own `[[item]]` rows where that composition is unarmed in the tree,
or the `[[item]]` rows of `definition` where a caller passes a parsed one;
the acceptance records through `build_records.read_records` with `read_acceptance`; the run-state file's
facts and parked rows; the remote-tracking tip of the default branch. No status header, README status
word or `phase:` fact decides a step.

Each unit's M2 state comes from the unattended driver's `--plan` rows, handed over in the environment
variable `GOV_POSITION_STATES`, TAB-separated lines: `unit <id> <state>` per row in build order, MISSING
rows included, `ask <id>` for the first undecided ask, `parent <slug> <derived phase>` per `parents:`
build, `bound <seconds>` for the driver's `RESUME_STALE_BOUND`, and `owed <PARK_KINDS_OWED>
<PARK_ACTS_OWED>`, the two space-joined sets. Where the variable is unset or empty, this runs the driver's
`--plan <slug>` with it set empty, which prints those lines in place of its `next:` line, so the driver
keeps the one M2 classifier and the call is not circular.

A unit's step is `none`, then `designed` when its state reads READY (a `DONE` row reading as its grade),
`built` when a pass commit attributed to it has a well-formed acceptance record naming the unit in
`Caused-by` and that commit in `Sha`, `tested` when the run-state `gates-run` fact's graded tip contains
that commit, and `deployed` when the remote-tracking tip does; each step needs the one before it. The
build's step is the step tag of the item on the unit table's forward row out of its least-advanced
unit's state, ties broken by row order, `none` once every unit is deployed. The next item is the first
item of that step, in composition order, whose witness does not hold and whose needs are witnessed. A
witness is read for three kinds of item only: a step's exit, on a recorded move out of that step's
state; the unit table's forward items, on the least-advanced unit's step; and an item a recorded move
names. Every other item's witness is unread, printed as an `evidence` claim, and a need on it is unmet.

The answer is one of `ANSWERS`, the first that holds: `invalid-input` (no build, a README that does not
parse, a read refusal, a recorded move no build row holds, or a hand-over naming no unit, no MISSING id
and no undecided ask), `stale-remote` (the remote tip's claim not `fresh`: unread, or its newest reflog
entry older than the bound), `terminal` (the state is a `[states]` terminal, or every unit is deployed
and no ask stands), `awaiting` on an owed parked entry or an unpassed hold, `blocked` on a `parents:`
build neither recorded nor derived `LANDED`, `act` with a next item, `awaiting` on an undecided ask, and
`stuck` naming the step's unwitnessed exit. Line output is §4's six line kinds; `--json` the same fields
as one object; `--next-line` the `next:` shape `render_next_line` picks from `NEXT_SHAPES`. Exit 0 for
every answer but `invalid-input`, which exits 2.

`--fixture --plant <case>` builds one scratch repository under the host temp folder, plants the case,
prints the engine's lines and one `position: fixture · <case> · held` or `· MISSED <why>` line, and
removes the scratch; it exits as the engine did where the case held, 1 where it missed, 2 where a kit it
needs does not resolve. `plan-line` and `status-line` run the unattended driver found by
`resolve_kit_dir`. `--selftest` runs every case through `loop_lib.run_selftest_cases`.

WHAT THIS DOES NOT CHECK: a witness reader for any item outside the three kinds above, which lands with
the build that arms the item; a settling row for a parked entry, which the driver's grammar does not
have yet, so every owed entry stands; the mailbox, printed `unarmed`; that a `gates-run` fact names a
green bar rather than the last bar run; that the remote-tracking ref was fetched recently rather than
moved recently, since a fetch that finds nothing new writes no reflog entry.
"""
import argparse
import copy
import datetime
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from claims import derive_claim_key, derive_claim_verdict, resolve_remote  # noqa: E402
from loop_items import read_composition  # noqa: E402
from loop_lib import (NO_STEP, LoopError, read_definition, read_item_rows, read_memory_tree,  # noqa: E402
                      resolve_kit_dir, run_selftest_cases)
from loop_parents import read_policy_kit  # noqa: E402
from loop_table import check_recorded_move, derive_from_states, read_transition_rows  # noqa: E402
from loop_transition import read_transitions  # noqa: E402
from loop_witness import read_git, remove_tree, resolve_bash, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "position"
ANSWERS = ("act", "awaiting", "blocked", "terminal", "stuck", "invalid-input", "stale-remote")
#: The environment hand-over from the driver's `--plan`.
HANDOVER = "GOV_POSITION_STATES"
#: The reason of the one invalid-input answer that renders the nothing-graded shape.
NOTHING_GRADED = "no tracked spec grades as a unit, no roster id is MISSING and no ask is undecided"
#: The five `next:` shapes `--plan` prints, byte for byte as the driver's ladder printed them, and the
#: fall-through, which no reader matches as an all-clear.
NEXT_SHAPES = {"live-unit": "<id> (READY - build it)",
               "live-state": "<id> (<state>)",
               "missing-unit": "<id> (MISSING - spec it first)",
               "undecided-ask": "<id> (UNDECIDED - plan a unit that closes it, or dispose it)",
               "nothing-graded": "none - no tracked spec grades as a unit (see the NOT A UNIT rows above)",
               "everything-terminal": "none - every tracked spec is terminal",
               "other": "none - <answer>: <reason>"}
UNIT_ID = re.compile(r"[A-Za-z]+-[A-Za-z0-9]+-\d+")
PARKED_ROW = re.compile(r"^[0-9][0-9-]*T[0-9:]*Z (\S+) · item (\S+)")
#: `--plant`'s cases and what each owes.
PLANTS = {"steps": "unit 1 deployed, unit 2 built, unit 3 designed: act at unit 3's step",
          "typed-status": "unit 2's header typed CLOSED, no pass commit: designed, never built",
          "idempotent": "item 1 witnessed by a recorded move naming it: next is item 2, and the key moves with an input",
          "owner-decision": "an owed decision park, unsettled: awaiting",
          "parent-unlanded": "parents: names a build with no landed move and no derived LANDED: blocked",
          "terminal": "the newest recorded move enters landed: terminal",
          "stale-remote": "no remote-tracking tip: stale-remote",
          "bad-transition": "a recorded move no build row holds: invalid-input, exit 2",
          "deadlock": "the step's root item needs an item of a later step: stuck",
          "bar-wait": "every unit built, no gates-run fact, no ask: act, and the terminal next: shape",
          "plan-line": "the driver's next: line equals render_next_line's, in three states",
          "status-line": "the driver's --status prints the engine's position line"}
FX_SLUG = "tPos"
FX_IDS = ["TOOL-tPos-1", "TOOL-tPos-2", "TOOL-tPos-3"]
FX_ASK = "TOOL-tAsk-1"
FX_OWED = ("decision abort override waiver handoff", "retire supersede defer")


# ------------------------------------------------------------------------------------------ the reads
def read_blob_id(path):
    """The first eight hex digits of `path`'s git blob id, hashed here rather than by a git spawn."""
    data = pathlib.Path(path).read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()[:8]


def read_handover(repo, slug):
    """The driver's hand-over for `slug`, from `GOV_POSITION_STATES` or, where that is unset or empty,
    from the driver's `--plan` run with it set empty. ValueError where `--plan` refuses; LookupError
    where the driver or a bash to run it does not resolve."""
    text = os.environ.get(HANDOVER, "")
    if not text:
        driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
        bash = resolve_bash(driver)
        if bash is None:
            raise LookupError("no bash can run %s" % driver.as_posix())
        p = subprocess.run([bash, str(driver), "--plan", slug], cwd=str(repo), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=dict(os.environ, **{HANDOVER: ""}), timeout=900)
        if p.returncode != 0:
            said = [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]
            raise ValueError("the driver's --plan %s refused: %s" % (slug, said[-1] if said else "exit %d" % p.returncode))
        text = p.stdout
    out = {"units": [], "ask": None, "parents": {}, "bound": None, "owed": ((), ())}
    for ln in text.splitlines():
        f = ln.rstrip("\r").split("\t")
        if f[0] == "unit" and len(f) == 3:
            out["units"].append((f[1], f[2]))
        elif f[0] == "ask" and len(f) == 2 and f[1]:
            out["ask"] = f[1]
        elif f[0] == "parent" and len(f) == 3:
            out["parents"][f[1]] = f[2]
        elif f[0] == "bound" and len(f) == 2 and f[1].isdigit():
            out["bound"] = int(f[1])
        elif f[0] == "owed" and len(f) == 3:
            out["owed"] = (tuple(f[1].split()), tuple(f[2].split()))
    return out


def read_remote_claim(repo, bound, now):
    """`(sha or None, claim)` of the default branch's remote-tracking tip: the claim keyed over
    `<ref>@<sha>`, `at` its newest reflog entry, judged `remote` against `bound`."""
    remote, branch, _observed, _refusal = resolve_remote(repo)
    ref = "refs/remotes/%s/%s" % (remote, branch) if remote and branch else "refs/remotes/?"
    sha, at = None, None
    if remote and branch:
        rc, out = read_git(repo, "rev-parse", "-q", "--verify", "%s^{commit}" % ref)
        sha = out if rc == 0 and out else None
        rc, out = read_git(repo, "reflog", "show", "--date=unix", "-n1", "--format=%gd", ref)
        m = re.search(r"@\{(\d+)\}", out) if rc == 0 else None
        at = datetime.datetime.fromtimestamp(int(m.group(1)), datetime.timezone.utc) if m else None
    source = "%s@%s" % (ref, sha or "?")
    key = derive_claim_key([source])
    verdict = derive_claim_verdict(key, key, "remote", at, now, bound)
    return sha, ref, {"name": "remote tip %s" % ref, "key": key, "verdict": verdict}


def check_is_ancestor(repo, sha, tip):
    """Whether `tip` contains `sha`."""
    return bool(sha and tip) and read_git(repo, "merge-base", "--is-ancestor", sha, tip)[0] == 0


# ------------------------------------------------------------------------------------------ the derivation
def derive_instance_key(item, pass_id, inputs):
    """`<item tag>@<pass>#<inputs>`, `<inputs>` the first eight hex digits of the SHA-1 of the ids the
    witness read, sorted and NUL-joined."""
    raw = b"\0".join(sorted(str(i).encode("utf-8") for i in inputs))
    return "%s@%s#%s" % (item, pass_id, hashlib.sha1(raw).hexdigest()[:8])


def derive_unit_step(word, passes, records, gates_tip, remote_sha, repo):
    """`(step, pass commit or None)` of one unit: `word` its hand-over state, `passes` the pass commits
    attributed to it newest first, `records` the well-formed acceptance records naming it."""
    m = re.fullmatch(r"DONE \((.+)\)", word)
    grade = m.group(1) if m else ("READY" if word == "DONE" else word)
    if grade != "READY":
        return "none", None
    held = [p for p in passes if any(r.get("Sha") == p for r in records)]
    if not held:
        return "designed", None
    if not check_is_ancestor(repo, held[0], gates_tip):
        return "built", held[0]
    if not check_is_ancestor(repo, held[0], remote_sha):
        return "tested", held[0]
    return "deployed", held[0]


def derive_next_item(step_items, read_witness, unit_id, head):
    """`(next item or None, claims)`: the first of `step_items` whose witness does not hold and whose
    needs are witnessed, and a claim per item read, `evidence` for an unread witness."""
    claims, found = [], None
    for row in step_items:
        tag = row.get("tag")
        held, inputs = read_witness(tag)
        if held is None:
            claims.append({"name": tag, "key": derive_claim_key(["item=%s" % tag]),
                           "verdict": derive_claim_verdict(derive_claim_key(["item=%s" % tag]), None, "history",
                                                           None, None, None)})
        elif held:
            sources = ["commit=%s" % i for i in inputs]
            key = derive_claim_key(sources)
            claims.append({"name": derive_instance_key(tag, unit_id, inputs), "key": key,
                           "verdict": derive_claim_verdict(key, key, "history", None, None, None)})
        if held or found:
            continue
        needs = row.get("needs") or []
        if all(any(read_witness(t)[0] for t in (n if isinstance(n, list) else [n])) for n in needs):
            found = {"item": tag, "unit": unit_id, "actor": row.get("actor", "?"),
                     "key": derive_instance_key(tag, unit_id, inputs or [head])}
    return found, claims


def derive_interrupts(text, handover, owed, parents_open, claims, now):
    """The interrupts in `[position]`'s order: owner decisions, the mailbox, invalidated witnesses,
    dependency gates, the undecided ask. `text` is the run-state file's text, `owed` the policy kit's
    `read_run_fact` where that file exists, `parents_open` the parents not landed."""
    out = []
    kinds, acts = handover["owed"]
    for ln in text.splitlines():
        m = PARKED_ROW.match(ln.rstrip("\r"))
        if m and (m.group(1) in kinds or (m.group(1) == "rescope" and m.group(2) in acts)):
            out.append({"kind": "owner-decision", "subject": "%s · item %s" % m.groups()})
    code = owed(text, "hold-code") if owed else None
    until = (owed(text, "hold-until") or "") if owed else ""
    if code:
        m = re.fullmatch(r"after (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)", until.strip())
        passed = bool(m) and now >= datetime.datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=datetime.timezone.utc)
        if not passed:
            out.append({"kind": "owner-decision", "subject": "hold %s · until %s" % (code, until or "-")})
    out.append({"kind": "mailbox", "subject": "unarmed"})
    out += [{"kind": "invalidated", "subject": c["name"]} for c in claims if c["verdict"] == "re-derived"]
    out += [{"kind": "dependency", "subject": p} for p in parents_open]
    if handover["ask"]:
        out.append({"kind": "ask", "subject": handover["ask"]})
    return out


def derive_answer(pos, terminal, remote_fresh, every_deployed, nxt, exit_item):
    """`(answer, reason)` by §4's precedence, invalid-input already decided by the caller."""
    kinds = [i["kind"] for i in pos["interrupts"]]
    ask = next((i["subject"] for i in pos["interrupts"] if i["kind"] == "ask"), None)
    if not remote_fresh:
        return "stale-remote", "the default branch's remote-tracking tip is unread or older than its bound"
    if pos["state"] in terminal:
        return "terminal", "the build's state %s is terminal" % pos["state"]
    if every_deployed and not ask:
        return "terminal", "every unit is past its last step"
    if "owner-decision" in kinds:
        return "awaiting", "an owner decision: %s" % next(i["subject"] for i in pos["interrupts"]
                                                          if i["kind"] == "owner-decision")
    if "dependency" in kinds:
        return "blocked", "the parent %s has not landed" % " ".join(
            i["subject"] for i in pos["interrupts"] if i["kind"] == "dependency")
    if nxt:
        return "act", "%s for %s" % (nxt["item"], nxt["unit"])
    if ask:
        return "awaiting", "the undecided ask %s" % ask
    return "stuck", "no item of %s can run and its exit %s is unwitnessed" % (pos["build_step"], exit_item or "-")


def derive_position(repo, slug, definition=None):
    """The `Position` of build `slug` in the repository at `repo` (§4 Data model). `definition`, where
    given, is a parsed definition read instead of the shipped one and the composition."""
    repo = pathlib.Path(repo).absolute()
    pos = {"slug": slug, "state": "none", "build_step": NO_STEP, "units": [], "next": None, "interrupts": [],
           "answer": "invalid-input", "reason": "", "read": [], "claims": []}
    try:
        derive_position_into(pos, repo, slug, definition)
    except (LoopError, ValueError, OSError, LookupError, KeyError, subprocess.SubprocessError) as e:
        pos.update(answer="invalid-input", reason=str(e) or type(e).__name__)
    return pos


def derive_position_into(pos, repo, slug, definition):
    """The body of `derive_position`, raising on any refused read."""
    read_memory_tree("gen_build_index.py")
    from build_records import read_acceptance, read_records
    from commit_trailers import derive_attribution, read_commits
    from design_lib import read_design_conf
    from gen_build_index import Problem, parse_front_matter
    now = datetime.datetime.now(datetime.timezone.utc)
    conf = read_design_conf(repo)
    builds = repo / (conf.get("MEMORY_ROOT") or "memory").strip().strip("/") / "builds"
    folder = builds / slug
    if not (folder / "README.md").is_file():
        raise ValueError("the slug %s names no build README under %s" % (slug, builds.as_posix()))
    try:
        fm = parse_front_matter(str(folder / "README.md"), slug)
    except Problem as e:
        raise ValueError("the build README does not parse: %s" % e) from None
    pos["read"].append("%s@%s" % ((folder / "README.md").relative_to(repo).as_posix(), read_blob_id(folder / "README.md")))
    handover = read_handover(repo, slug)
    if definition is None:
        data, where = read_definition(KIT)
        rc, payload, lines = read_composition(repo)
        if rc == 1:
            raise ValueError("the item composition does not read: %s" % (lines[0] if lines else "exit 1"))
        # unarmed, exit 2: no composition in this tree, so gov's own rows alone
        items = payload["rows"] if rc == 0 else read_item_rows(data, where)
    else:
        data, where = definition, "the caller's definition"
        items = read_item_rows(data, where)
    tables = read_transition_rows(data, where)
    steps = {r["tag"]: r for r in data["step"]}
    item_step = {r.get("tag"): r.get("step") for r in items}
    moves = read_transitions(slug, repo)
    for m in moves:
        if not check_recorded_move(m, tables):
            raise ValueError("the recorded move %s -> %s on %s at %s is held by no build row" % (
                m.get("from"), m.get("to"), m.get("item"), str(m.get("commit"))[:8]))
    pos["state"] = moves[0]["to"] if moves else "none"
    rc, head = read_git(repo, "rev-parse", "HEAD")
    if rc != 0:
        raise ValueError("HEAD names no commit in %s" % repo.as_posix())
    pos["read"].append("HEAD@%s" % head[:8])
    passes = {}
    for c in read_commits(str(repo), ["--first-parent", "HEAD"], ["Pass"]):
        for uid in derive_attribution(c, "replace", UNIT_ID):
            passes.setdefault(uid, []).append(c["sha"])
    records = {}
    for r in read_records(repo, conf, "acceptance", read_acceptance):
        if r["build"] == slug and not r["malformed"]:
            records.setdefault(r.get("Caused-by", "").strip("`"), []).append(r)
            pos["read"].append("%s@%s" % (r["path"], read_blob_id(repo / r["path"])))
    run = folder / "RUN.md"
    text, owed = "", None
    if run.is_file():
        text = run.read_bytes().decode("utf-8", "replace")
        pos["read"].append("%s@%s" % (run.relative_to(repo).as_posix(), read_blob_id(run)))
        owed = read_policy_kit()[1].read_run_fact
    gates = (owed(text, "gates-run") or "").split() if owed else []
    gates_tip = None
    if len(gates) == 2:
        rc, out = read_git(repo, "rev-parse", "-q", "--verify", "%s^{commit}" % gates[1])
        gates_tip = out if rc == 0 else None
    remote_sha, ref, remote_claim = read_remote_claim(repo, handover["bound"], now)
    if remote_sha:
        pos["read"].append("%s@%s" % (ref, remote_sha[:8]))
    pos["claims"].append(remote_claim)
    order = ["none"] + list(tables["states"].get("unit", []))
    units, pass_of = [], {}
    for uid, word in handover["units"]:
        step, sha = derive_unit_step(word, passes.get(uid, []), records.get(uid, []), gates_tip, remote_sha, repo)
        units.append({"id": uid, "step": step, "state": word})
        pass_of[uid] = sha
    pos["units"] = units
    if not units and not handover["ask"]:
        raise ValueError(NOTHING_GRADED)
    forward = {}
    for row in tables["transition"]:
        if row.get("level") != "unit":
            continue
        for s in derive_from_states(row, tables["states"].get("unit", [])):
            if s in order[:-1] and row.get("to") == order[order.index(s) + 1]:
                forward.setdefault(s, row)
    least = min(units, key=lambda u: order.index(u["step"])) if units else None
    every_deployed = all(u["step"] == order[-1] for u in units)
    if least and least["step"] in forward:
        pos["build_step"] = item_step.get(forward[least["step"]]["item"], NO_STEP)
    exit_item = steps[pos["build_step"]]["exit"] if pos["build_step"] in steps else None
    named = {}
    for m in moves:
        named.setdefault(m.get("item"), m.get("commit"))
    exits = {r["exit"]: r["state"] for r in data["step"]}
    unit_items = {row["item"]: row["to"] for row in forward.values()}

    def read_witness(tag):
        """`(held, inputs)` of one item: held None where no reader exists for it."""
        if tag in unit_items and least:
            sha = pass_of.get(least["id"])
            return order.index(least["step"]) >= order.index(unit_items[tag]), [sha] if sha else []
        if tag in exits:
            out = [m["commit"] for m in moves if m.get("from") == exits[tag] != m.get("to")]
            return bool(out), out[:1]
        if tag in named:
            return True, [named[tag]]
        return None, []

    nxt, item_claims = (None, [])
    if least and pos["build_step"] != NO_STEP:
        nxt, item_claims = derive_next_item([r for r in items if r.get("step") == pos["build_step"]], read_witness,
                                            least["id"], head)
    pos["next"] = nxt
    pos["claims"] += item_claims
    parents_open = []
    for p in (fm.get("parents") or "").split():
        landed = handover["parents"].get(p) == "LANDED"
        if not landed and (builds / p).is_dir():
            landed = bool((read_transitions(p, repo) or [{}])[0].get("to") == "landed")
        if not landed:
            parents_open.append(p)
    pos["interrupts"] = derive_interrupts(text, handover, owed, parents_open, pos["claims"], now)
    pos["answer"], pos["reason"] = derive_answer(pos, tables["terminal"], remote_claim["verdict"] == "fresh",
                                                 every_deployed and bool(units), nxt, exit_item)


# ------------------------------------------------------------------------------------------ the output
def render_next_line(pos):
    """The `next:` shape `--plan` prints for a position (§4 "The `next:` line")."""
    ask = next((i["subject"] for i in pos["interrupts"] if i["kind"] == "ask"), None)
    owner = any(i["kind"] == "owner-decision" for i in pos["interrupts"])
    answer = pos["answer"]
    if answer == "act" and pos["next"]:
        unit = next(u for u in pos["units"] if u["id"] == pos["next"]["unit"])
        if unit["step"] in ("built", "tested"):
            return NEXT_SHAPES["undecided-ask"].replace("<id>", ask) if ask else NEXT_SHAPES["everything-terminal"]
        if unit["state"] == "MISSING":
            return NEXT_SHAPES["missing-unit"].replace("<id>", unit["id"])
        if unit["state"] in ("READY", "DONE"):
            return NEXT_SHAPES["live-unit"].replace("<id>", unit["id"])
        m = re.fullmatch(r"DONE \((.+)\)", unit["state"])
        return NEXT_SHAPES["live-state"].replace("<id>", unit["id"]).replace("<state>", m.group(1) if m else unit["state"])
    if answer == "invalid-input" and pos["reason"] == NOTHING_GRADED:
        return NEXT_SHAPES["nothing-graded"]
    if answer == "terminal":
        return NEXT_SHAPES["everything-terminal"]
    if answer == "awaiting" and ask and not owner:
        return NEXT_SHAPES["undecided-ask"].replace("<id>", ask)
    return NEXT_SHAPES["other"].replace("<answer>", answer).replace("<reason>", pos["reason"])


def render_position_lines(pos):
    """The line output (§4 Line output)."""
    lines = ["position — %s · state %s · step %s · answer %s · %s" % (
        pos["slug"], pos["state"], pos["build_step"], pos["answer"], pos["reason"])]
    lines += ["unit — %s · %s" % (u["id"], u["step"]) for u in pos["units"]]
    if pos["next"]:
        n = pos["next"]
        lines.append("next — %s · unit %s · actor %s · key %s" % (n["item"], n["unit"], n["actor"], n["key"]))
    lines += ["interrupt — %s · %s" % (i["kind"], i["subject"]) for i in pos["interrupts"]]
    lines += ["read — %s" % r for r in pos["read"]]
    lines += ["claim — %s · key %s · %s" % (c["name"], c["key"], c["verdict"]) for c in pos["claims"]]
    return lines


# ------------------------------------------------------------------------------------------ the fixture
def render_spec(uid, status):
    """A fixture spec the driver's M2 classifier grades READY."""
    return ("# %s — a unit\n\n**Status:** %s · rev-1 · 2026-01-01 · node a · Tier-2 · base abcdef12 · streams tooling\n\n"
            "## 1. Goal\ng\n## 2. Scope (IN)\n- S1 a thing\n## 3. Non-goals (OUT)\nn\n## 4. Design\nd\n"
            "## 5. Production-readiness checklist\nc\n## 6. Acceptance criteria\n- AC1 it works\n## 7. Gates\n"
            "the bar\n## 8. Open questions\nnone\n## 9. Revision log\n- rev-1\n## 10. Reuse audit\nr\n" % (uid, status))


def render_handover(units, ask=None, parents=None):
    """The hand-over text a fixture plants where the driver does not run."""
    lines = ["bound\t5400", "owed\t%s\t%s" % FX_OWED] + ["unit\t%s\t%s" % u for u in units]
    lines += ["ask\t%s" % ask] if ask else []
    lines += ["parent\t%s\t%s" % p for p in (parents or {}).items()]
    return "\n".join(lines) + "\n"


def write_position_plant(top, case, root):
    """The scratch repository `top/r` for `case`, with its bare remote `top/o.git` where it has one;
    `(repo, definition, handover)`."""
    repo = top / "r"
    repo.mkdir()
    ids = FX_IDS[:2] if case in ("typed-status", "bar-wait") else FX_IDS
    extra = "parents: tPar\n" if case == "parent-unlanded" else ""
    rows = "".join("| [%s — u](spec/2026-01-01-spec-%s.md) | INPROGRESS | rev-1 | 2026-01-01 |\n" % (u, u) for u in ids)
    files = {".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tool:TOOL"\n',
             "memory/builds/%s/README.md" % FX_SLUG:
                 "---\nslug: %s\nnode: a\nopened: 2026-01-01\nstreams: tooling\nroster: TOOL\nids: %s\n%s---\n\n# %s\n\n"
                 "<!-- gen:build-index -->\n**Build status:** OPEN · %d unit(s)\n\n<!-- gen:build-units -->\n"
                 "| Unit | Status | Rev | Last change |\n|---|---|---|---|\n%s<!-- /gen:build-units -->\n"
                 "<!-- /gen:build-index -->\n" % (FX_SLUG, " ".join(ids), extra, FX_SLUG, len(ids), rows)}
    for n, uid in enumerate(ids):
        status = "CLOSED" if case == "typed-status" and n == 1 else "INPROGRESS"
        files["memory/builds/%s/spec/2026-01-01-spec-%s.md" % (FX_SLUG, uid)] = render_spec(uid, status)
    if case == "parent-unlanded":
        files["memory/builds/tPar/README.md"] = "---\nslug: tPar\nnode: a\nopened: 2026-01-01\nstreams: tooling\n---\n# tPar\n"
    if case in ("plan-line", "status-line"):
        for name in (".unattended.conf", ".memory-tree.conf"):
            if not (root / name).is_file():
                raise LookupError("the driver plant copies %s from %s, which holds none" % (name, root.as_posix()))
            shutil.copyfile(root / name, repo / name)
        files.pop(".memory-tree.conf")
    run_fixture_git(repo, "init", "-q", "--template=", "-b", "main")
    write_fixture_files(repo, files)
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "fixture")
    remote = None if case == "stale-remote" else top / "o.git"
    if remote:
        run_fixture_git(top, "init", "-q", "--bare", "--template=", str(remote))
        run_fixture_git(repo, "remote", "add", "origin", str(remote))

    def write_pass(uid):
        """One pass commit for `uid` and the acceptance record naming it; the pass commit's sha."""
        write_fixture_files(repo, {"work/%s.txt" % uid: uid + "\n"})
        run_fixture_git(repo, "add", "-A")
        run_fixture_git(repo, "commit", "-q", "-m", "feat: %s\n\nPass: %s" % (uid, uid))
        sha = run_fixture_git(repo, "rev-parse", "HEAD")
        read_memory_tree("build_records.py")
        from build_records import write_acceptance
        write_acceptance(repo, FX_SLUG, uid, sha, "stand-in", [("true", 0, "0" * 12)], today="2026-01-01")
        run_fixture_git(repo, "add", "-A")
        run_fixture_git(repo, "commit", "-q", "-m", "records: %s acceptance\n\nPass: none" % uid)
        return sha

    def write_move(src, to, item):
        """One recorded move, a commit carrying its `Gov-Transition` trailer."""
        head = run_fixture_git(repo, "rev-parse", "HEAD")
        run_fixture_git(repo, "commit", "-q", "--allow-empty", "-m", "move\n\nGov-Transition: %s -> %s · build=%s · item=%s · sha=%s" % (
            src, to, FX_SLUG, item, head[:8]))

    run_facts = "# %s run\n\n## Run facts\nphase: BUILDING\nbase: %s\nwitness: %s\nmode: slug\n" % (
        FX_SLUG, "0" * 40, "0" * 40)
    if case in ("steps", "plan-line", "status-line"):
        write_pass(FX_IDS[0])
        tip = run_fixture_git(repo, "rev-parse", "HEAD")
        run_facts += "gates-run: bar-1 %s\n" % tip[:8]
        run_fixture_git(repo, "push", "-q", "origin", "main")
        write_pass(FX_IDS[1])
    elif case == "bar-wait":
        for uid in ids:
            write_pass(uid)
    elif case == "idempotent":
        write_move("building", "building", "item.build.base")
    elif case == "terminal":
        write_move("deploying", "landed", "item.deploy.close")
    elif case == "bad-transition":
        write_move("planning", "landed", "item.plan.input")
    if case == "owner-decision":
        run_facts += "\n## Parked\n\n2026-01-01T00:00:00Z decision · item which-way · reason the fixture's owed decision\n"
    write_fixture_files(repo, {"memory/builds/%s/RUN.md" % FX_SLUG: run_facts})
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "run state")
    if remote and case not in ("steps", "plan-line", "status-line"):
        run_fixture_git(repo, "push", "-q", "origin", "main")
    if remote:
        run_fixture_git(repo, "remote", "set-head", "origin", "main")
    definition = None
    data = copy.deepcopy(read_definition(KIT)[0])
    if case == "idempotent":
        data["transition"].append({"level": "build", "from": ["building"], "item": "item.build.base",
                                   "outcome": "pinned", "to": "building", "witness": "the fixture's move"})
    if case == "deadlock":
        next(r for r in data["item"] if r.get("tag") == "item.build.base")["needs"] = ["item.test.merge"]
    if case not in ("plan-line", "status-line"):
        definition = data
    words = {"typed-status": ["READY", "DONE"]}.get(case, ["READY"] * len(ids))
    handover = render_handover(list(zip(ids, words)), parents={"tPar": "RUNNING"} if case == "parent-unlanded" else None)
    return repo, definition, handover


def run_driver(repo, *argv):
    """The unattended driver's output for `argv` in `repo`, with no hand-over inherited."""
    driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
    bash = resolve_bash(driver)
    if bash is None:
        raise LookupError("no bash can run %s" % driver.as_posix())
    env = {k: v for k, v in os.environ.items() if k not in (HANDOVER, "GOV_DEFAULT_BRANCH")}
    p = subprocess.run([bash, str(driver), *argv], cwd=str(repo), capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env, timeout=900)
    return p.stdout + p.stderr


def derive_plant_position(repo, definition, handover):
    """`derive_position` over a plant, its hand-over set in this process for the one call."""
    before = os.environ.get(HANDOVER)
    os.environ[HANDOVER] = handover or ""
    try:
        return derive_position(repo, FX_SLUG, definition)
    finally:
        if before is None:
            os.environ.pop(HANDOVER, None)
        else:
            os.environ[HANDOVER] = before


def check_plan_line(repo):
    """The `plan-line` case's misses: the driver's `next:` line against `render_next_line`, in the
    `steps` state, beside an undecided ask, and once every unit is deployed beside it."""
    misses = []
    readme = repo / ("memory/builds/%s/README.md" % FX_SLUG)

    def check_state(label, want):
        out = run_driver(repo, "--plan", FX_SLUG)
        line = next((ln[len("next: "):] for ln in out.splitlines() if ln.startswith("next: ")), None)
        mine = render_next_line(derive_plant_position(repo, None, ""))
        print("%s: fixture · plan-line %s · driver %r · engine %r" % (SAY, label, line, mine))
        if line != mine or not mine.startswith(want):
            misses.append("%s: driver %r, engine %r, owed %r" % (label, line, mine, want))

    check_state("steps", "%s (READY - build it)" % FX_IDS[2])
    text = readme.read_text(encoding="utf-8").replace("slug: %s\n" % FX_SLUG, "slug: %s\nasks: %s\n" % (FX_SLUG, FX_ASK), 1)
    write_fixture_files(repo, {readme.relative_to(repo).as_posix(): text})
    run_fixture_git(repo, "commit", "-q", "-am", "an undecided ask")
    check_state("ask beside READY", "%s (READY - build it)" % FX_IDS[2])
    write_fixture_files(repo, {"work/%s.txt" % FX_IDS[2]: "w\n"})
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "feat: 3\n\nPass: %s" % FX_IDS[2])
    sha = run_fixture_git(repo, "rev-parse", "HEAD")
    read_memory_tree("build_records.py")
    from build_records import write_acceptance
    write_acceptance(repo, FX_SLUG, FX_IDS[2], sha, "stand-in", [("true", 0, "0" * 12)], today="2026-01-01")
    run_path = repo / ("memory/builds/%s/RUN.md" % FX_SLUG)
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "records\n\nPass: none")
    tip = run_fixture_git(repo, "rev-parse", "HEAD")
    text = re.sub(r"gates-run: .*", "gates-run: bar-2 %s" % tip[:8], run_path.read_text(encoding="utf-8"))
    write_fixture_files(repo, {run_path.relative_to(repo).as_posix(): text})
    run_fixture_git(repo, "commit", "-q", "-am", "the bar's fact")
    run_fixture_git(repo, "push", "-q", "origin", "main")
    check_state("every unit deployed beside the ask", "%s (UNDECIDED" % FX_ASK)
    return misses


def check_plant(case, pos, rc, repo):
    """The misses of `case` against the position it derived."""
    steps = [u["step"] for u in pos["units"]]
    claims = {c["name"]: c for c in pos["claims"]}
    kinds = {i["kind"]: i["subject"] for i in pos["interrupts"]}
    want = {"steps": lambda: steps == ["deployed", "built", "designed"] and pos["answer"] == "act"
            and pos["build_step"] == "step.build" and any(r.startswith("memory/") for r in pos["read"])
            and any(c["name"].startswith("remote tip") and c["key"].startswith("k1:") and c["verdict"] == "fresh"
                    for c in pos["claims"]),
            "typed-status": lambda: steps[1] == "designed",
            "idempotent": lambda: pos["next"] and pos["next"]["item"] == "item.build.unit-lease"
            and any(n.startswith("item.build.base@") and c["verdict"] == "fresh" for n, c in claims.items()),
            "owner-decision": lambda: pos["answer"] == "awaiting" and "which-way" in kinds.get("owner-decision", ""),
            "parent-unlanded": lambda: pos["answer"] == "blocked" and "tPar" in pos["reason"],
            "terminal": lambda: pos["answer"] == "terminal",
            "stale-remote": lambda: pos["answer"] == "stale-remote",
            "bad-transition": lambda: pos["answer"] == "invalid-input" and rc == 2,
            "deadlock": lambda: pos["answer"] == "stuck" and "item.build.exit" in pos["reason"],
            "bar-wait": lambda: pos["answer"] == "act" and pos["build_step"] == "step.test"
            and render_next_line(pos) == NEXT_SHAPES["everything-terminal"]}
    misses = [] if want[case]() else ["the position was %s" % json.dumps(pos)[:600]]
    if case == "idempotent":
        k1 = derive_instance_key("item.build.base", FX_IDS[0], ["a" * 40])
        k2 = derive_instance_key("item.build.base", FX_IDS[0], ["b" * 40])
        print("%s: fixture · key %s · one input moved %s" % (SAY, k1, k2))
        if k1.split("#")[1] == k2.split("#")[1]:
            misses.append("an input SHA left the key unchanged")
    return misses


def run_plant(case):
    """One fixture case: its lines, then `held` or `MISSED`; the engine's exit where it held."""
    top = pathlib.Path(tempfile.mkdtemp(prefix="pos-"))
    try:
        root = next((d for d in (KIT, *KIT.parents) if (d / ".git").exists()), KIT)
        repo, definition, handover = write_position_plant(top, case, root)
        if case == "plan-line":
            misses, rc = check_plan_line(repo), 0
        elif case == "status-line":
            out = run_driver(repo, "--status", FX_SLUG)
            print(out.rstrip())
            rc = 0
            misses = [] if any(ln.startswith("position — %s · " % FX_SLUG) for ln in out.splitlines()) else [
                "--status printed no position line"]
        else:
            pos = derive_plant_position(repo, definition, handover)
            rc = 2 if pos["answer"] == "invalid-input" else 0
            for line in render_position_lines(pos):
                print(line)
            print("next: %s" % render_next_line(pos))
            misses = check_plant(case, pos, rc, repo)
    except LookupError as e:
        print("%s: fixture · %s · unarmed: %s" % (SAY, case, e))
        return 2
    finally:
        remove_tree(top)
    print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
    return rc if not misses else 1


def run_selftest():
    """Every plant through `run_selftest_cases`."""
    cases = [(c, ["--fixture", "--plant", c], 2 if c == "bad-transition" else 0, "%s: fixture · %s · held" % (SAY, c), "")
             for c in PLANTS]
    return run_selftest_cases(main, cases, "%s: selftest" % SAY)


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="position.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("slug", nargs="?")
    out = ap.add_mutually_exclusive_group()
    out.add_argument("--json", action="store_true", help="one JSON object")
    out.add_argument("--next-line", action="store_true", help="the next: shape alone")
    ap.add_argument("--fixture", action="store_true", help="run one fixture case")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--selftest", action="store_true", help="run every fixture case")
    args = ap.parse_args(argv)
    if args.selftest:
        if args.fixture or args.slug:
            ap.error("--selftest takes no slug and no --fixture")
        return run_selftest()
    if args.fixture != bool(args.plant) or (args.fixture and args.slug):
        ap.error("--fixture takes --plant <case> and no slug")
    if args.fixture:
        return run_plant(args.plant)
    if not args.slug:
        ap.error("a slug, or --fixture --plant <case>, or --selftest")
    rc, top = read_git(".", "rev-parse", "--show-toplevel")
    pos = derive_position(top if rc == 0 and top else ".", args.slug)
    if args.json:
        print(json.dumps(pos, ensure_ascii=False))
    elif args.next_line:
        print(render_next_line(pos))
    else:
        for line in render_position_lines(pos):
            print(line)
    return 2 if pos["answer"] == "invalid-input" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
