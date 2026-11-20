#!/usr/bin/env python3
"""verdict_flow.py — a red bar's reds joined to routes, the tester's judgment of a routed red, and the
selection of the legs a bar holds.

    python <this kit>/verdict_flow.py route --run <run dir>
    python <this kit>/verdict_flow.py judge --run <run dir> --leg <name> --judgment <word>
    python <this kit>/verdict_flow.py select --rev <R> --out <path>
    python <this kit>/verdict_flow.py select --check --run <run dir>|--selection <path> --rev <R>
    python <this kit>/verdict_flow.py --fixture route|red-route|selection-rows|held-keys|select|held-policy

TOOL-dWitnessedBar-3 S6, S7; `select` TOOL-dWitnessedBar-5 S5 to S7. `<run dir>` is one run record of
the runner, `<git dir>/gate-run/<run id>`. Run in the repository whose revision `--rev` names.

  route  reads `<run dir>/verdict` and `<run dir>/attribution` and writes the routing record
         `<run dir>/routing`, mode 600, one TAB row per red leg: leg · class · blocks · route ·
         judgment · next, the last two `-` until `judge` fills them. A red leg the attribution does
         not name is a row of class `-`, which blocks. The route is the class's when the row blocks,
         and `ask` when it passes:

           class               blocks  route          the `item.test.route` outcome it stands for
           OWN, MIXED          block   attribute      own
           CONTENDED           block   quiet-rerun    contended
           DEAD PROBE, -       block   probe-repair   dead-probe
           INHERITED           block   fix-unit       inherited
           any                 pass    ask            non-blocking

         The record writes the route word, never the outcome; nothing checks the join (§8 F9). Prints
         `route  <leg>  <class> · <blocks> · <route>` per row.
  judge  records the tester's judgment on a row routed `attribute`. The word must be one of the
         outcomes of the loop definition's `item.test.attribute` row, read by running the loop kit's
         `loop_lib.py items --tag item.test.attribute`, the verb TOOL-dWitnessedBar-100 asks for; its
         `next` is filled by `verdict.red-route`, read by running the policy kit's `policy.py get`,
         the catalogue default `fix-pass-or-design` where no policy kit resolves:
           fix-pass-or-design  code-miss -> fix-pass, spec-wrong -> new-unit
           always-new-unit     code-miss -> new-unit, spec-wrong -> new-unit
         Prints `judge  <leg>  <judgment> -> <next>`.
  select writes the selection record (`test.select`): a header naming the values it read, then one
         TAB row per held leg, `held · <leg> · <source> · <note>`, the source a word of
         SELECTION_SOURCES. Every input is read at R and never from the working tree: the manifest by
         `git show`, the policy by the policy kit's `policy.py get <key> --rev <R>`, the catalogue
         defaults where no policy kit resolves. One row source per SELECT_SOURCES pair; this unit
         ships `level`: a leg whose `level` is outside `tests.landing-levels`, none under
         `every-declared`, and none while `tests.without-cadence` reads `run-at-landing`, since no
         cadence is installed here. `verdict.held` decides when held legs run: `peer-or-cadence`
         needs a `HELD_CI_WORKFLOW` in `.unattended.conf` at R, else a refusal naming the value;
         `push-selected` prints the export the pre-push hook makes for its bar where the pusher set
         no `GATE_SELFTESTS`. A leg name holding ` · ` is never written; its leg runs.
         `--check` derives the record again at R and exits 1 naming each row the run record's
         `selection` adds or lacks; the hook runs it before it admits a verdict made under one.
         `--selection <path>` checks that file instead of `<run dir>/selection`, exactly one of the
         two: the hook rebuilds a per-tree verdict's `selection.<n>` rows into one
         (TOOL-dWitnessedBar-41 S4).
         The runner reads the record `GATE_SELECTION` names and copies it into the run record.

A kit imports no sibling kit: both are run as subprocesses, each found through the kit's inline copy
of the sibling-kit resolver.

EXIT 0 written · 1 `select --check` found the selection differs · 2 refused, nothing written: no
verdict, a verdict that is not RED, a malformed attribution or routing record, a leg with no routed row
or one not routed `attribute`, a word outside the outcome set, no loop kit or one whose `loop_lib.py`
does not answer the verb, a policy read that fails or answers outside its key's values, a revision or
manifest that cannot be read, or `peer-or-cadence` with no runner declared elsewhere.

`--fixture route` plants a run dir under the system temp directory whose attribution holds one row of
each class under `own-only` and whose verdict counts one more red the attribution omits.
`--fixture red-route` plants stub loop and policy kits and judges under each value, a word outside the
set, no loop kit, and a loop kit without the verb. `--fixture selection-rows` writes a selection
holding a quarantine row and a row naming a leg the manifest lacks, and re-reads it; then one holding
a `kit` row, which no selection may hold. `--fixture held-keys` reads a planted verdict's `held.<n>`
keys and refuses a result outside `unrun ok fail` and a count with a key missing. `--fixture select`
plants a repository whose manifest holds an `e2e` leg and whose policy lands `unit, integration`,
selects at R, moves the leg's level in the working tree alone, and checks a run that adds a row.
`--fixture held-policy` selects under each `verdict.held` value. Each exits 0 when every case reads as
planted, 1 naming each that does not.

WHAT IT DOES NOT CHECK. That the attribution was made against the landing base, or that its `blocks`
words were derived by `lib-verdict.sh`: the runner writes both, and the readers that land a red read
them. Spawning the tester or acting on `next`: the loop's engine runs the item the route names. That
a held leg ran anywhere else: `peer-or-cadence` checks a runner is DECLARED, never that it ran.
`select --check` compares rows, never the header, which only names what was read.
"""
import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(os.path.abspath(__file__)).parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from leg_factory import resolve_kit_dir  # noqa: E402 - the kit's inline copy of the sibling resolver

SAY = "verdict-flow"
BOUND = 120  # seconds, each subprocess
ROUTES = ("attribute", "quiet-rerun", "probe-repair", "fix-unit", "ask")
NEXTS = ("fix-pass", "new-unit")
CLASSES = ("OWN", "MIXED", "CONTENDED", "INHERITED", "DEAD PROBE")
RED_ROUTE_KEY = "verdict.red-route"
RED_ROUTE_DEFAULT = "fix-pass-or-design"
RED_ROUTES = {"fix-pass-or-design": {"code-miss": "fix-pass", "spec-wrong": "new-unit"},
              "always-new-unit": {"code-miss": "new-unit", "spec-wrong": "new-unit"}}
ATTRIBUTE_TAG = "item.test.attribute"
LOOP_VERB = "items --tag"
ASK_ID = "TOOL-dWitnessedBar-100"
# THE HOLD (TOOL-dWitnessedBar-5). The runner's `HOLD_SOURCES` is `kit` and these two: `kit` it derives
# from the manifest row itself, so a selection holding a `kit` row is ignored and its leg runs.
SELECTION_SOURCES = ("quarantine", "level")
HELD_RESULTS = ("unrun", "ok", "fail")
SEP = " · "
HELD_KEY = "verdict.held"
HELD_VALUES = ("peer-or-cadence", "push-selected", "on-demand")
HELD_DEFAULT = "on-demand"
HELD_EXPORT = {"push-selected": "GATE_SELFTESTS=changed"}  # the hook's export, where the pusher set none
LEVELS_KEY = "tests.landing-levels"
LEVELS_DEFAULT = ("unit", "integration")
LEVELS_EVERY = "every-declared"
CADENCE_KEY = "tests.without-cadence"
CADENCE_VALUES = ("run-at-landing", "report-unrun", "wait-for-expansion")
CADENCE_DEFAULT = "run-at-landing"
MANIFEST = "gate-legs.json"
UNATTENDED_CONF = ".unattended.conf"
HELD_RUNNER_KEY = "HELD_CI_WORKFLOW"


class Refusal(Exception):
    """Exit 2, nothing written."""


def read_verdict(run):
    """{key: value} of `<run>/verdict`, and the leg names its `tail.<n>` rows carry, in order."""
    path = run / "verdict"
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        raise Refusal(f"{path.as_posix()} is absent, so nothing says which legs failed") from None
    keys, tails = {}, []
    for ln in lines:
        k, _, v = ln.partition("\t")
        keys.setdefault(k, v)
        if k.startswith("tail.") and " " in v:
            tails.append(v.split(" ", 1)[1].strip())
    return keys, tails


def read_held_keys(keys):
    """[(leg, source, result)] of a verdict's `held.<n>` keys, `<n>` from 1 in order, as `read_verdict`
    read them. Refuses a value that is not three ` · ` fields, a result outside HELD_RESULTS, and a
    `held` count the keys do not match, which is a held leg with no key."""
    out, n = [], 1
    while f"held.{n}" in keys:
        f = keys[f"held.{n}"].split(SEP)
        if len(f) != 3 or not f[0]:
            raise Refusal(f"held.{n} reads '{keys[f'held.{n}']}', not leg · source · result")
        if f[2] not in HELD_RESULTS:
            raise Refusal(f"held.{n} reads result '{f[2]}', outside {' '.join(HELD_RESULTS)}")
        out.append(tuple(f))
        n += 1
    count = keys.get("held", "0")
    if not count.isdigit() or int(count) != len(out):
        raise Refusal(f"the verdict counts held '{count}' and names {len(out)} held leg(s) by held.<n>")
    return out


def read_selection(text, names=None):
    """(rows [(leg, source, note)], refusals [line]) of a selection record's text. A row that is not
    `held` and three fields, whose source is outside SELECTION_SOURCES, or whose leg `names` lacks is
    refused and its leg runs; `#` lines are the header."""
    rows, refusals = [], []
    for n, ln in enumerate(text.splitlines(), 1):
        if not ln.strip() or ln.startswith("#"):
            continue
        f = ln.split("\t")
        if len(f) != 4 or f[0] != "held" or not f[1]:
            refusals.append(f"selection row {n} is not `held` · leg · source · note, ignored")
        elif f[2] not in SELECTION_SOURCES:
            refusals.append(f"selection row {n} holds {f[1]} by '{f[2]}', outside "
                            f"{' '.join(SELECTION_SOURCES)}, ignored: it runs")
        elif names is not None and f[1] not in names:
            refusals.append(f"selection row {n} holds {f[1]}, which the manifest lacks, ignored")
        else:
            rows.append((f[1], f[2], f[3]))
    return rows, refusals


def read_attribution(run):
    """[(leg, class, blocks)] of `<run>/attribution`, an absent record reading as no rows. A `blocks`
    word that is not `pass` reads `block`, so a runner that wrote no ninth field blocks."""
    path = run / "attribution"
    if not path.is_file():
        return []
    rows = []
    for ln in path.read_text(encoding="utf-8", errors="replace").splitlines():
        f = ln.split("\t")
        if not f[0]:
            continue
        cls = f[1] if len(f) > 1 and f[1] in CLASSES else "-"
        rows.append((f[0], cls, "pass" if len(f) > 9 and f[8] == "pass" else "block"))
    return rows


def derive_route(cls, blocks):
    """The route word of one red row."""
    if blocks == "pass":
        return "ask"
    return {"OWN": "attribute", "MIXED": "attribute", "CONTENDED": "quiet-rerun",
            "INHERITED": "fix-unit"}.get(cls, "probe-repair")


def write_routing(run, rows):
    """`<run>/routing`, replaced whole, mode 600."""
    path = run / "routing"
    tmp = run / "routing.tmp"
    tmp.write_bytes("".join("\t".join(r) + "\n" for r in rows).encode("utf-8"))
    try:
        os.chmod(tmp, 0o600)
    except OSError:
        pass
    os.replace(tmp, path)


def read_routing(run):
    path = run / "routing"
    if not path.is_file():
        raise Refusal(f"{path.as_posix()} is absent: run `verdict_flow.py route --run` first")
    rows = []
    for n, ln in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        f = ln.split("\t")
        if len(f) != 6 or f[3] not in ROUTES:
            raise Refusal(f"{path.as_posix()}:{n} is not a routing row of six fields")
        rows.append(f)
    return rows


def cmd_route(run):
    """-> (rc, out lines)."""
    keys, tails = read_verdict(run)
    if keys.get("verdict") != "RED":
        raise Refusal(f"the verdict reads '{keys.get('verdict') or 'none'}', not RED, so there is no red to route")
    failed = keys.get("failed", "")
    if not failed.isdigit():
        raise Refusal(f"the verdict counts '{failed or 'none'}' failed legs, not a number")
    attributed = read_attribution(run)
    named = {leg for leg, _, _ in attributed}
    rows = [(leg, cls, blocks) for leg, cls, blocks in attributed]
    for leg in tails:
        if leg not in named:
            rows.append((leg, "-", "block"))
            named.add(leg)
    k = 0
    while len(rows) < int(failed):
        k += 1
        rows.append((f"unnamed.{k}", "-", "block"))
    out_rows = [(leg, cls, blocks, derive_route(cls, blocks), "-", "-") for leg, cls, blocks in rows]
    write_routing(run, out_rows)
    return 0, [f"route  {leg}  {cls} · {blocks} · {route}" for leg, cls, blocks, route, _, _ in out_rows]


def run_kit(here, home, anchor, args, what, cwd=None):
    """The kit `home` found from `here`, its `anchor` run with `args` in `cwd` -> the completed process."""
    try:
        kit = resolve_kit_dir(home, anchor, here)
    except LookupError as e:
        raise Refusal(f"{what}: {e}") from None
    try:
        return subprocess.run([sys.executable, str(pathlib.Path(kit, anchor)), *args], capture_output=True,
                              encoding="utf-8", errors="replace", timeout=BOUND, cwd=cwd)
    except (OSError, subprocess.TimeoutExpired) as e:
        raise Refusal(f"{what}: {anchor} did not answer: {e}") from None


def read_outcomes(here):
    """The outcomes of `item.test.attribute`, read by the loop kit's own verb."""
    p = run_kit(here, "loop", "loop_lib.py", ["items", "--tag", ATTRIBUTE_TAG],
                f"no loop kit answers {ATTRIBUTE_TAG}'s outcomes")
    said = [ln.strip() for ln in p.stdout.splitlines() if ln.strip()]
    if p.returncode != 0 or not said:
        first = (p.stdout + p.stderr).strip().splitlines()[:1]
        raise Refusal(f"the loop kit's `loop_lib.py {LOOP_VERB} {ATTRIBUTE_TAG}` exited {p.returncode} with "
                      f"no outcome set, so its read verb, which {ASK_ID} asks for, is absent or refused"
                      + (f": {first[0]}" if first else ""))
    return said


def read_red_route(here):
    """`verdict.red-route` by the policy kit's `get`, its catalogue default where no policy kit resolves."""
    try:
        resolve_kit_dir("policy", "policy.py", here)
    except LookupError:
        return RED_ROUTE_DEFAULT, "the catalogue default: no policy kit resolves"
    p = run_kit(here, "policy", "policy.py", ["get", RED_ROUTE_KEY], f"{RED_ROUTE_KEY} unread")
    value = p.stdout.strip()
    if p.returncode != 0 or value not in RED_ROUTES:
        raise Refusal(f"policy.py get {RED_ROUTE_KEY} exited {p.returncode} answering '{value}', outside "
                      f"{' '.join(RED_ROUTES)}")
    return value, "read by policy.py get"


def cmd_judge(run, leg, judgment, here=HERE):
    """-> (rc, out lines)."""
    rows = read_routing(run)
    hit = [r for r in rows if r[0] == leg]
    if not hit:
        raise Refusal(f"the routing record holds no row for leg '{leg}'")
    if hit[0][3] != "attribute":
        raise Refusal(f"leg '{leg}' is routed {hit[0][3]}, not attribute, so it takes no judgment")
    outcomes = read_outcomes(here)
    if judgment not in outcomes:
        raise Refusal(f"'{judgment}' is outside {ATTRIBUTE_TAG}'s outcomes: {' '.join(outcomes)}")
    value, where = read_red_route(here)
    nxt = RED_ROUTES[value].get(judgment)
    if nxt not in NEXTS:
        raise Refusal(f"{RED_ROUTE_KEY} {value} sends no '{judgment}' anywhere")
    hit[0][4], hit[0][5] = judgment, nxt
    write_routing(run, rows)
    return 0, [f"judge  {leg}  {judgment} -> {nxt} · {RED_ROUTE_KEY} {value}, {where}"]


# ---- the selection (TOOL-dWitnessedBar-5) -----------------------------------------------------------

def run_git(repo, *args):
    """(rc, stdout) of `git -C <repo> <args>`."""
    try:
        p = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, encoding="utf-8",
                           errors="replace", timeout=BOUND)
    except (OSError, subprocess.TimeoutExpired) as e:
        raise Refusal(f"git {args[0]} did not answer: {e}") from None
    return p.returncode, p.stdout


def read_at(repo, sha, rel):
    """The text of `rel` in the commit `sha`, or None where that commit holds no such path."""
    rc, out = run_git(repo, "show", f"{sha}:{rel}")
    return out if rc == 0 else None


def read_policy_at(repo, sha, here, key, default, allowed=None):
    """[value lines] of `key` at `sha` by the policy kit's `get --rev`, `default` where no policy kit
    resolves; a read that fails, answers nothing, or answers outside `allowed` is a Refusal."""
    try:
        resolve_kit_dir("policy", "policy.py", here)
    except LookupError:
        return list(default)
    p = run_kit(here, "policy", "policy.py", ["get", key, "--rev", sha], f"{key} unread", cwd=repo)
    said = [ln.strip() for ln in p.stdout.splitlines() if ln.strip()]
    if p.returncode != 0 or not said or (allowed and said[0] not in allowed):
        raise Refusal(f"policy.py get {key} --rev {sha[:8]} exited {p.returncode} answering "
                      f"'{' '.join(said)}'" + (f", outside {' '.join(allowed)}" if allowed else ""))
    return said


def read_held_runner(repo, sha):
    """The `HELD_CI_WORKFLOW` that `.unattended.conf` declares at `sha`, its last assignment, or ''."""
    value = ""
    for ln in (read_at(repo, sha, UNATTENDED_CONF) or "").splitlines():
        s = ln.strip()
        if s.startswith(HELD_RUNNER_KEY + "="):
            value = s.split("=", 1)[1].split("#", 1)[0].strip().strip("\"'")
    return value


def derive_level_rows(ctx):
    """[(leg, note)] for each leg whose `level` is outside `tests.landing-levels`. None under
    `every-declared`, and none under `run-at-landing`: no cadence is installed here, so that value runs
    every level at landing (dTendedCadence's Maintain is what would run them instead)."""
    levels = ctx["levels"]
    if LEVELS_EVERY in levels or ctx["cadence"] == CADENCE_DEFAULT:
        return []
    return [(r["name"], f"{r['level']}, outside {LEVELS_KEY} {' '.join(levels)}") for r in ctx["legs"]
            if isinstance(r.get("level"), str) and r["level"] and r["level"] not in levels]


# (source word, reader): each reader takes the inputs read at R and answers [(leg, note)].
# TOOL-dWitnessedBar-8 adds `quarantine`.
SELECT_SOURCES = (("level", derive_level_rows),)


def derive_manifest_rel(repo):
    """The manifest beside this kit's tool root, relative to `repo`'s top level."""
    rc, top = run_git(repo, "rev-parse", "--show-toplevel")
    if rc == 0 and top.strip():
        rel = os.path.relpath(HERE.parent / MANIFEST, top.strip())
        if not rel.startswith(".."):
            return pathlib.Path(rel).as_posix()
    return MANIFEST


def derive_selection(repo, rev, here, manifest_rel):
    """(verdict.held value, header, [(leg, source, note)], [refusal line]) derived at `rev`, every input
    read in that commit and none from the working tree."""
    rc, out = run_git(repo, "rev-parse", "--verify", "-q", f"{rev}^{{commit}}")
    sha = out.strip()
    if rc != 0 or not sha or rev.startswith("-"):
        raise Refusal(f"'{rev}' names no commit, so there is no R to select at")
    text = read_at(repo, sha, manifest_rel)
    if text is None:
        raise Refusal(f"{manifest_rel} is absent at {sha[:8]}, so there is no manifest to select from")
    try:
        legs = json.loads(text)
    except ValueError as e:
        raise Refusal(f"{manifest_rel} at {sha[:8]} is not JSON: {e}") from None
    if not isinstance(legs, list):
        raise Refusal(f"{manifest_rel} at {sha[:8]} is not a list of legs")
    legs = [r for r in legs if isinstance(r, dict) and isinstance(r.get("name"), str)]
    held = read_policy_at(repo, sha, here, HELD_KEY, [HELD_DEFAULT], HELD_VALUES)[0]
    levels = read_policy_at(repo, sha, here, LEVELS_KEY, LEVELS_DEFAULT)
    cadence = read_policy_at(repo, sha, here, CADENCE_KEY, [CADENCE_DEFAULT], CADENCE_VALUES)[0]
    if held == "peer-or-cadence" and not read_held_runner(repo, sha):
        raise Refusal(f"{HELD_KEY} peer-or-cadence at {sha[:8]} declares no runner elsewhere: no "
                      f"{HELD_RUNNER_KEY} in {UNATTENDED_CONF} there and no registered peer backend, so "
                      f"the held legs would run nowhere")
    ctx = {"legs": legs, "levels": levels, "cadence": cadence}
    rows, said = [], []
    for source, reader in SELECT_SOURCES:
        for leg, note in reader(ctx):
            if SEP in leg or "\t" in leg or "\n" in leg:
                said.append(f"{SAY}: select refused a row · leg {leg!r} holds ` · `, a TAB or a newline, "
                            f"so it is not held and runs")
                continue
            rows.append((leg, source, note))
    header = (f"# {HELD_KEY} {held}{SEP}{LEVELS_KEY} {' '.join(levels)}{SEP}{CADENCE_KEY} {cadence}"
              f"{SEP}rev {sha}")
    return held, header, rows, said


def render_selection(header, rows):
    return header + "\n" + "".join(f"held\t{leg}\t{src}\t{note}\n" for leg, src, note in rows)


def render_row(ln):
    """A selection record row as `<leg> · <source> · <note>`, its `held` word dropped."""
    return ln.split("\t", 1)[-1].replace("\t", SEP)


def derive_held_export(value, pusher):
    """The pre-push hook's export for its bar under `verdict.held` `value`, or None: `push-selected`
    exports the `changed` selection where the pusher set no `GATE_SELFTESTS`."""
    return None if pusher else HELD_EXPORT.get(value)


def cmd_select(repo, rev, out, here=HERE, manifest_rel=None, pusher=None):
    """-> (rc, out lines). Writes the selection record at `out`."""
    manifest_rel = manifest_rel or derive_manifest_rel(repo)
    pusher = os.environ.get("GATE_SELFTESTS", "") if pusher is None else pusher
    held, header, rows, said = derive_selection(repo, rev, here, manifest_rel)
    path = pathlib.Path(out)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(render_selection(header, rows).encode("utf-8"))
    os.replace(tmp, path)
    lines = said + [f"select  {leg}  {src} · {note}" for leg, src, note in rows]
    export = derive_held_export(held, pusher)
    if export:
        lines.append(f"select  export {export} · {HELD_KEY} {held} and the pusher set no GATE_SELFTESTS, "
                     f"so the pre-push hook exports it for its bar")
    lines.append(f"select  {len(rows)} held · {HELD_KEY} {held} · wrote {path.as_posix()}")
    return 0, lines


def cmd_select_check(repo, run, rev, here=HERE, manifest_rel=None, selection=None):
    """-> (rc, out lines): 1 naming each row the selection adds or lacks against R. The selection is
    `<run>/selection`, or the file `selection` names when it is given (TOOL-dWitnessedBar-41 S4)."""
    if selection is None:
        path, who = run / "selection", "the run's selection"
        if not path.is_file():
            raise Refusal(f"{path.as_posix()} is absent, so this run held nothing by a selection")
    else:
        path, who = pathlib.Path(selection), "the selection"
        if not path.is_file():
            raise Refusal(f"{path.as_posix()} is no file, so there is no selection to check")
    manifest_rel = manifest_rel or derive_manifest_rel(repo)
    _held, _header, rows, _said = derive_selection(repo, rev, here, manifest_rel)
    fresh = render_selection("", rows).splitlines()[1:]
    recorded = [ln for ln in path.read_text(encoding="utf-8", errors="replace").splitlines()
                if ln.strip() and not ln.startswith("#")]
    diff = [f"select --check  {who} adds {render_row(ln)}, which {rev} does not derive"
            for ln in recorded if ln not in fresh]
    diff += [f"select --check  {who} lacks {render_row(ln)}, which {rev} derives"
             for ln in fresh if ln not in recorded]
    if diff:
        return 1, diff
    return 0, [f"select --check  {who} is what {rev} derives: {len(rows)} row(s)"]


# ---- the fixtures ----------------------------------------------------------------------------------

def write_run(root, attribution, tails, failed):
    run = pathlib.Path(root, "run")
    run.mkdir(parents=True)
    verdict = f"verdict\tRED\nfailed\t{failed}\ntree_moved\tno\n" + "".join(
        f"tail.{n}\t{'0' * 40} {leg}\n" for n, leg in enumerate(tails, 1))
    (run / "verdict").write_text(verdict, encoding="utf-8", newline="\n")
    (run / "attribution").write_text("".join("\t".join(r) + "\n" for r in attribution), encoding="utf-8",
                                     newline="\n")
    return run


def run_fixture_route():
    out, bad = [], []
    with tempfile.TemporaryDirectory(prefix="vflow-") as root:
        r = "0" * 40
        # One row per class under own-only, the `blocks` word as the table writes it.
        att = [(leg, cls, "1", "0", r, "-", "-", "-", blocks, "planted")
               for leg, cls, blocks in (("o", "OWN", "block"), ("m", "MIXED", "pass"), ("c", "CONTENDED", "pass"),
                                        ("i", "INHERITED", "pass"), ("d", "DEAD PROBE", "block"))]
        run = write_run(root, att, ["o", "m", "c", "i", "d", "gone"], 6)
        rc, lines = cmd_route(run)
        out += lines
        want = {"o": "attribute", "m": "ask", "c": "ask", "i": "ask", "d": "probe-repair", "gone": "probe-repair"}
        got = {f[0]: f[3] for f in read_routing(run)}
        for leg, route in want.items():
            if got.get(leg) != route:
                bad.append(f"leg {leg} routed {got.get(leg)}, planted to read {route}")
        if len(got) != 6:
            bad.append(f"the routing record holds {len(got)} rows and the verdict counts 6 failed")
        if rc != 0:
            bad.append(f"route exited {rc}")
    return out, bad


STUB_LOOP = """import sys
if sys.argv[1:] == ["items", "--tag", "item.test.attribute"]:
    print("code-miss")
    print("spec-wrong")
    sys.exit(0)
print("usage: python loop_lib.py --check")
sys.exit(2)
"""
STUB_LOOP_NO_VERB = """import sys
print("usage: python loop_lib.py --check | --scopes | --selftest")
sys.exit(2)
"""
LOOP_HOME = "loop"
POLICY_HOME = "policy"

STUB_POLICY = """import pathlib, sys
print(pathlib.Path(__file__).with_name("value.txt").read_text().strip())
"""


def write_kits(root, loop, value):
    here = pathlib.Path(root, "here")
    here.mkdir(parents=True)
    if loop is not None:
        (here / LOOP_HOME).mkdir()
        (here / LOOP_HOME / "loop_lib.py").write_text(loop, encoding="utf-8")
    (here / POLICY_HOME).mkdir()
    (here / POLICY_HOME / "policy.py").write_text(STUB_POLICY, encoding="utf-8")
    (here / POLICY_HOME / "value.txt").write_text(value, encoding="utf-8")
    return here


def write_routed(root):
    r = "0" * 40
    att = [(leg, "OWN", "1", "0", r, "-", "-", "-", "block", "planted") for leg in ("a", "b")]
    att.append(("p", "INHERITED", "1", "0", r, "-", "-", "-", "pass", "planted"))
    run = write_run(root, att, ["a", "b", "p"], 3)
    cmd_route(run)
    return run


def run_judge(run, leg, word, here):
    try:
        return cmd_judge(run, leg, word, here)
    except Refusal as e:
        return 2, [f"{SAY}: refused · {e}"]


def run_fixture_red_route():
    out, bad = [], []
    for value, want in (("fix-pass-or-design", {"code-miss": "fix-pass", "spec-wrong": "new-unit"}),
                        ("always-new-unit", {"code-miss": "new-unit", "spec-wrong": "new-unit"})):
        with tempfile.TemporaryDirectory(prefix="vflow-") as root:
            here, run = write_kits(root, STUB_LOOP, value), write_routed(root)
            for leg, word in (("a", "code-miss"), ("b", "spec-wrong")):
                rc, lines = run_judge(run, leg, word, here)
                out.append(f"{value}: " + " ".join(lines))
                if rc != 0 or not lines[0].startswith(f"judge  {leg}  {word} -> {want[word]} "):
                    bad.append(f"under {value}, {word} read rc {rc}: {lines}")
                    continue
                out.append(f"{value}: {word} -> {want[word]}")
            rows = {f[0]: f for f in read_routing(run)}
            if rows["a"][4:] != ["code-miss", want["code-miss"]] or rows["b"][4:] != ["spec-wrong", want["spec-wrong"]]:
                bad.append(f"under {value} the routing record reads {rows['a']} {rows['b']}")
    refusals = (("a word outside the set", STUB_LOOP, "a", "maybe", "outside item.test.attribute's outcomes: code-miss spec-wrong"),
                ("no loop kit", None, "a", "code-miss", "no loop kit answers"),
                ("a loop kit without the verb", STUB_LOOP_NO_VERB, "a", "code-miss", "loop_lib.py items --tag"),
                ("a row not routed attribute", STUB_LOOP, "p", "code-miss", "routed ask, not attribute"))
    for what, loop, leg, word, said in refusals:
        with tempfile.TemporaryDirectory(prefix="vflow-") as root:
            here, run = write_kits(root, loop, RED_ROUTE_DEFAULT), write_routed(root)
            rc, lines = run_judge(run, leg, word, here)
            out.append(f"{what}: rc {rc} · " + " ".join(lines))
            if rc != 2 or said not in " ".join(lines):
                bad.append(f"{what} read rc {rc}, planted to exit 2 naming '{said}': {lines}")
            elif read_routing(run)[0][4:] != ["-", "-"]:
                bad.append(f"{what} wrote the routing record")
    return out, bad


def run_fixture_selection_rows():
    out, bad = [], []
    names = {"flaky leg", "steady leg", "kit suite"}
    with tempfile.TemporaryDirectory(prefix="vflow-") as root:
        path = pathlib.Path(root, "selection")
        path.write_text("# planted\nheld\tflaky leg\tquarantine\tflaked 2 of 10\n"
                        "held\tghost leg\tquarantine\tno such leg\n", encoding="utf-8", newline="\n")
        text = path.read_text(encoding="utf-8")
        rows, _ = read_selection(text)
        out += [f"row  {leg} · {src} · {note}" for leg, src, note in rows]
        if [r[0] for r in rows] != ["flaky leg", "ghost leg"]:
            bad.append(f"the file re-read as {rows}, planted with two rows")
        held, refusals = read_selection(text, names)
        out += [f"refusal  {r}" for r in refusals]
        if held != [("flaky leg", "quarantine", "flaked 2 of 10")]:
            bad.append(f"against the manifest it held {held}, planted to hold the quarantined leg alone")
        if len(refusals) != 1 or "ghost leg, which the manifest lacks" not in refusals[0]:
            bad.append(f"the leg the manifest lacks read {refusals}, planted to be one refusal")
        held, refusals = read_selection("held\tkit suite\tkit\ta selection naming the kit class\n", names)
        out += [f"kit row: refusal  {r}" for r in refusals]
        if held or len(refusals) != 1:
            bad.append(f"a `kit` row read as held {held}, refusals {refusals}: a selection holds no kit leg")
    return out, bad


def run_fixture_held_keys():
    out, bad = [], []
    planted = [("unit-heavy suite", "level", "unrun"), ("kit selftest a", "kit", "unrun"),
               ("flaky leg", "quarantine", "ok")]
    cases = (("planted", 3, planted, None),
             ("a result outside the set", 1, [("flaky leg", "quarantine", "maybe")], "outside unrun ok fail"),
             ("a held leg with no key", 3, planted[:2], "names 2 held leg(s)"))
    for what, count, held, said in cases:
        with tempfile.TemporaryDirectory(prefix="vflow-") as root:
            run = pathlib.Path(root, "run")
            run.mkdir()
            (run / "verdict").write_text(f"verdict\tGREEN\nheld\t{count}\n" + "".join(
                f"held.{n}\t{SEP.join(h)}\n" for n, h in enumerate(held, 1)), encoding="utf-8", newline="\n")
            keys, _ = read_verdict(run)
            try:
                got = read_held_keys(keys)
            except Refusal as e:
                out.append(f"{what}: refused · {e}")
                if not said or said not in str(e):
                    bad.append(f"{what} refused '{e}', planted to read" + (f" naming '{said}'" if said else ""))
                continue
            out += [f"{what}: held  {leg} · {src} · {res}" for leg, src, res in got]
            if said or got != held:
                bad.append(f"{what} read {got}, planted " + (f"to refuse naming '{said}'" if said else f"as {held}"))
    return out, bad


STUB_POLICY_AT = """import subprocess, sys, tomllib
key, rev = sys.argv[2], sys.argv[sys.argv.index("--rev") + 1]
p = subprocess.run(["git", "show", rev + ":.governance/policy.toml"], capture_output=True, text=True)
table = tomllib.loads(p.stdout) if p.returncode == 0 else {}
head, _, tail = key.partition(".")
value = (table.get(head) or {}).get(tail)
value = {"verdict.held": "on-demand", "tests.landing-levels": ["unit", "integration"],
         "tests.without-cadence": "run-at-landing"}[key] if value is None else value
for v in value if isinstance(value, list) else [value]:
    print(v)
"""
FIXTURE_LEGS = [{"name": "slow suite", "level": "e2e", "argv": ["true"]},
                {"name": "fast suite", "level": "unit", "argv": ["true"]},
                {"name": "kit selftest", "subject": "kit", "argv": ["true"]}]


def write_repo(root, policy, conf=None):
    """(repo, here, sha): a committed repository holding FIXTURE_LEGS and `policy`, and a policy kit that
    reads its values at `--rev`."""
    repo = pathlib.Path(root, "repo")
    repo.mkdir()
    (repo / MANIFEST).write_text(json.dumps(FIXTURE_LEGS, indent=2) + "\n", encoding="utf-8", newline="\n")
    (repo / ".governance").mkdir()
    (repo / ".governance" / "policy.toml").write_text(policy, encoding="utf-8", newline="\n")
    if conf is not None:
        (repo / UNATTENDED_CONF).write_text(conf, encoding="utf-8", newline="\n")
    for args in (("init", "-q"), ("add", "-A"), ("-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid",
                                                  "commit", "-q", "--no-verify", "-m", "planted")):
        rc, _ = run_git(repo, *args)
        if rc != 0:
            raise Refusal(f"the fixture's git {args[0]} exited {rc}")
    here = pathlib.Path(root, "here")
    (here / POLICY_HOME).mkdir(parents=True)
    (here / POLICY_HOME / "policy.py").write_text(STUB_POLICY_AT, encoding="utf-8")
    return repo, here, run_git(repo, "rev-parse", "HEAD")[1].strip()


def run_select(repo, rev, out, here, pusher=""):
    try:
        return cmd_select(repo, rev, out, here, MANIFEST, pusher)
    except Refusal as e:
        return 2, [f"{SAY}: select refused · {e}"]


LANDS_UNIT_INTEGRATION = '[tests]\nlanding-levels = ["unit", "integration"]\nwithout-cadence = "report-unrun"\n'


def run_fixture_select():
    out, bad = [], []
    want = [("slow suite", "level", f"e2e, outside {LEVELS_KEY} unit integration")]
    with tempfile.TemporaryDirectory(prefix="vflow-") as root:
        repo, here, sha = write_repo(root, LANDS_UNIT_INTEGRATION)
        sel = pathlib.Path(root, "selection")
        rc, lines = run_select(repo, sha, sel, here)
        out += lines
        rows, _ = read_selection(sel.read_text(encoding="utf-8")) if sel.is_file() else ([], [])
        if rc != 0 or rows != want:
            bad.append(f"select at R read rc {rc}, rows {rows}, planted to hold slow suite as level")
        moved = [dict(r, level={"e2e": "unit", "unit": "e2e"}.get(r.get("level"), r.get("level"))) for r in FIXTURE_LEGS]
        (repo / MANIFEST).write_text(json.dumps(moved, indent=2) + "\n", encoding="utf-8", newline="\n")
        rc, lines = run_select(repo, sha, sel, here)
        out += [f"levels moved in the working tree alone: {ln}" for ln in lines]
        rows, _ = read_selection(sel.read_text(encoding="utf-8"))
        if rows != want:
            bad.append(f"with the levels moved in the working tree alone the selection read {rows}: select read the tree")
        run = pathlib.Path(root, "run")
        run.mkdir()
        (run / "selection").write_text(sel.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
        try:
            rc, lines = cmd_select_check(repo, run, sha, here, MANIFEST)
        except Refusal as e:
            rc, lines = 2, [str(e)]
        out += [f"control: rc {rc} · {ln}" for ln in lines]
        if rc != 0:
            bad.append(f"select --check on the selection R derives exited {rc}: {lines}")
        with (run / "selection").open("a", encoding="utf-8", newline="\n") as fh:
            fh.write("held\tfast suite\tlevel\tplanted by the branch\n")
        try:
            rc, lines = cmd_select_check(repo, run, sha, here, MANIFEST)
        except Refusal as e:
            rc, lines = 2, [str(e)]
        out += [f"a row added: rc {rc} · {ln}" for ln in lines]
        if rc != 1 or "adds fast suite" not in " ".join(lines):
            bad.append(f"select --check on a selection adding a row exited {rc}, planted to exit 1 naming it: {lines}")
    return out, bad


def run_fixture_held_policy():
    out, bad = [], []
    export = f"export {HELD_EXPORT['push-selected']}"
    cases = (("push-selected", "", None, export),
             ("push-selected", "1", None, None),
             ("on-demand", "", None, None),
             ("peer-or-cadence", "", None, "peer-or-cadence at"),
             ("peer-or-cadence", "", 'HELD_CI_WORKFLOW="remote-ci.yml"\n', None))
    for value, pusher, conf, said in cases:
        what = f"{value}, GATE_SELFTESTS '{pusher}'" + (", a HELD_CI_WORKFLOW declared" if conf else "")
        with tempfile.TemporaryDirectory(prefix="vflow-") as root:
            repo, here, sha = write_repo(root, f'[verdict]\nheld = "{value}"\n', conf)
            rc, lines = run_select(repo, sha, pathlib.Path(root, "selection"), here, pusher)
            out.append(f"{what}: rc {rc} · " + " | ".join(lines))
            text = " ".join(lines)
            want_rc = 2 if value == "peer-or-cadence" and conf is None else 0
            if rc != want_rc:
                bad.append(f"{what} exited {rc}, planted to exit {want_rc}: {lines}")
            elif said and said not in text:
                bad.append(f"{what} did not name '{said}': {lines}")
            elif not said and "export " in text:
                bad.append(f"{what} printed an export, planted to print none: {lines}")
    return out, bad


FIXTURES = {"route": run_fixture_route, "red-route": run_fixture_red_route,
            "selection-rows": run_fixture_selection_rows, "held-keys": run_fixture_held_keys,
            "select": run_fixture_select, "held-policy": run_fixture_held_policy}


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace", newline="\n")
        except (AttributeError, ValueError):
            pass
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["--fixture"]:
        if len(argv) != 2 or argv[1] not in FIXTURES:
            print(f"usage: python verdict_flow.py --fixture {'|'.join(FIXTURES)}", file=sys.stderr)
            return 2
        out, bad = FIXTURES[argv[1]]()
        for ln in out:
            print(ln)
        for ln in bad:
            print(f"{SAY}: fixture {argv[1]} FAILED · {ln}", file=sys.stderr)
        print(f"{SAY}: fixture {argv[1]} " + ("FAILED" if bad else "ok"))
        return 1 if bad else 0
    ap = argparse.ArgumentParser(prog="verdict_flow.py", description=__doc__.split("\n")[0])
    ap.add_argument("verb", choices=("route", "judge", "select"))
    ap.add_argument("--run")
    ap.add_argument("--selection")
    ap.add_argument("--leg")
    ap.add_argument("--judgment")
    ap.add_argument("--rev")
    ap.add_argument("--out")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    try:
        # `--run` is asked of route and judge, and `select --check` asks it or `--selection`, exactly one
        # (TOOL-dWitnessedBar-41 S4): `select` writes no run record.
        run = None
        if a.selection is not None and not (a.verb == "select" and a.check):
            raise Refusal("--selection is asked of select --check alone")
        if a.verb == "select" and a.check and (a.run is None) == (a.selection is None):
            raise Refusal("select --check takes exactly one of --run <run dir> and --selection <path>")
        if (a.verb != "select" or a.check) and a.selection is None:
            if not a.run:
                raise Refusal(f"{a.verb}{' --check' if a.check else ''} takes --run <run dir>")
            run = pathlib.Path(a.run)
            if not run.is_dir():
                raise Refusal(f"{run.as_posix()} is no run record directory")
        if a.verb == "select":
            if not a.rev:
                raise Refusal("select takes --rev <R>: its inputs are read there, never from the tree")
            if a.check:
                rc, out = cmd_select_check(pathlib.Path("."), run, a.rev, selection=a.selection)
            elif not a.out:
                raise Refusal("select takes --out <path>, the selection record it writes")
            else:
                rc, out = cmd_select(pathlib.Path("."), a.rev, a.out)
        elif a.verb == "route":
            rc, out = cmd_route(run)
        elif not (a.leg and a.judgment):
            raise Refusal("judge takes --leg and --judgment")
        else:
            rc, out = cmd_judge(run, a.leg, a.judgment)
    except Refusal as e:
        print(f"{SAY}: {a.verb} refused · {e}", file=sys.stderr)
        return 2
    for ln in out:
        print(ln)
    return rc


if __name__ == "__main__":
    sys.exit(main())
