#!/usr/bin/env python3
"""verdict_flow.py — a red bar's reds joined to routes, the tester's judgment of a routed red, the
selection of the legs a bar holds, and the flake record with the holds it justifies.

    python <this kit>/verdict_flow.py route --run <run dir>
    python <this kit>/verdict_flow.py judge --run <run dir> --leg <name> --judgment <word>
    python <this kit>/verdict_flow.py select --rev <R> --out <path>
    python <this kit>/verdict_flow.py select --check --run <run dir>|--selection <path> --rev <R>
    python <this kit>/verdict_flow.py flakes --run <run dir> --build <slug> --unit <id>
    python <this kit>/verdict_flow.py flakes --check
    python <this kit>/verdict_flow.py --fixture <one of FIXTURES>

TOOL-dWitnessedBar-3 S6, S7; `select` TOOL-dWitnessedBar-5 S5 to S7; `flakes`, the `flakes` route and
the `quarantine` row TOOL-dWitnessedBar-8. `<run dir>` is one run record of the runner,
`<git dir>/gate-run/<run id>`. Run in the repository whose revision `--rev` names.

  route  reads `<run dir>/verdict` and `<run dir>/attribution` and writes the routing record
         `<run dir>/routing`, mode 600, one TAB row per red leg: leg · class · blocks · route ·
         judgment · next, the last two `-` until `judge` fills them. A red leg the attribution does
         not name is a row of class `-`, which blocks. A red leg whose same-tree re-run
         (`GATE_RERUN=1`), `<i>.rerun.leg` beside the `<i>.leg` whose field 1 names it, reads `ok`
         routes `flakes`, ahead of every other row. Otherwise the route is the class's when the row
         blocks, and `ask` when it passes:

           class               blocks  route          the `item.test.route` outcome it stands for
           any, re-run ok      any     flakes         nondeterministic
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
         defaults where no policy kit resolves. One row source per SELECT_SOURCES pair: `level`, a
         leg whose `level` is outside `tests.landing-levels`, none under `every-declared`, and none
         while `tests.without-cadence` reads `run-at-landing`, since no cadence is installed here;
         and `quarantine`, a leg an OPEN held-flaky-leg ask names, its note `<count>/<window>, ask
         <id>`, the asks the `ASKS_CMD` generator `.unattended.conf` declares at R prints, run in a
         scratch worktree at R, none where R declares no generator. `verdict.held` decides when held legs run: `peer-or-cadence`
         needs a `HELD_CI_WORKFLOW` in `.unattended.conf` at R, else a refusal naming the value;
         `push-selected` prints the export the pre-push hook makes for its bar where the pusher set
         no `GATE_SELFTESTS`. A leg name holding ` · ` is never written; its leg runs.
         `--check` derives the record again at R and exits 1 naming each row the run record's
         `selection` adds or lacks; the hook runs it before it admits a verdict made under one.
         `--selection <path>` checks that file instead of `<run dir>/selection`, exactly one of the
         two: the hook rebuilds a per-tree verdict's `selection.<n>` rows into one
         (TOOL-dWitnessedBar-41 S4).
         The runner reads the record `GATE_SELECTION` names and copies it into the run record.
  flakes acts as `verdict.flakes` reads in this repository: `retry-only` writes nothing; `record` and
         `quarantine` write one `flake` record of build `<slug>` under `<unit id>` through the
         memory-tree factory's `write_record`: `Run`, `Ended`, `Tree` (the verdict's run_id, ended and
         tree), `Sha` (the header's head) and `Legs`, then one fenced TAB row per executed leg,
         `<leg> · <first rc> · <re-run rc or ->`, the first rc the retry's where one ran; a held,
         skipped or reused leg wrote no `<i>.leg` and has no row. It prints `verdict-flow: wrote
         <path>`, then runs the drift kit's gate-health measurement in the repository's top within
         HEALTH_BOUND, `drift_report.py --gate-health --write --build <slug> --unit <id> --with <that
         record>`, and prints every line it prints unchanged, so a `drift-report: wrote <path>` line is
         staged beside the flake record (TOOL-dWitnessedBar-1 S5); no drift kit, a non-zero exit or the
         bound firing prints one `flakes  gate-health · <why>` line instead. The flake body is read, and a
         row judged flaked, through the factory's `read_flake_body` and `derive_flaked`. Under
         `quarantine` it then prints `hold  <leg>  <flakes>/<window>  <record ids>`
         for each leg whose flakes in its last `<window>` rows reach the entry threshold and that no
         OPEN held-flaky-leg ask names. The threshold is `verdict.flakes.entry`: a declared
         `<count>/<window>`, or under `measured` the `Measured` of the newest `gate-health` record
         where the factory registers that kind, else 2/10, said. A leg's rows are read newest `Ended`
         first across every tracked flake record, those at or before its release not counted: the
         committer date of the oldest commit adding `- CLOSED · <id> · ` to a CLOSED held-flaky-leg
         ask of the leg, the newest such, or the newest row's `Ended` where no commit adds the row
         yet. It ends `flakes  re-entry test.verdict`, or `test.select` under `quarantine`.
         `flakes --check` reads this repository's asks and records and exits 1 naming each OPEN
         held-flaky-leg ask whose leg flaked fewer times, in its window at the ask's filing date,
         than the threshold in force then.

A kit imports no sibling kit: the loop and policy kits are run as subprocesses, each found through the
kit's inline copy of the sibling-kit resolver, and the memory-tree factory is loaded as `keep_tails.py`
loads it.

EXIT 0 written · 1 `select --check` found the selection differs, or `flakes --check` a hold below its
threshold · 2 refused, nothing written: no
verdict, a verdict that is not RED, a malformed attribution or routing record, a leg with no routed row
or one not routed `attribute`, a word outside the outcome set, no loop kit or one whose `loop_lib.py`
does not answer the verb, a policy read that fails or answers outside its key's values, a revision or
manifest that cannot be read, `peer-or-cadence` with no runner declared elsewhere, an ask generator
that fails, a factory that does not resolve, or one that refuses the record.

`--fixture route` plants a run dir under the system temp directory whose attribution holds one row of
each class under `own-only` and whose verdict counts one more red the attribution omits.
`--fixture red-route` plants stub loop and policy kits and judges under each value, a word outside the
set, no loop kit, and a loop kit without the verb. `--fixture selection-rows` writes a selection
holding a quarantine row and a row naming a leg the manifest lacks, and re-reads it; then one holding
a `kit` row, which no selection may hold. `--fixture held-keys` reads a planted verdict's `held.<n>`
keys and refuses a result outside `unrun ok fail` and a count with a key missing. `--fixture select`
plants a repository whose manifest holds an `e2e` leg and whose policy lands `unit, integration`,
selects at R, moves the leg's level in the working tree alone, and checks a run that adds a row.
`--fixture held-policy` selects under each `verdict.held` value. `--fixture route-flaky` routes an OWN
red whose re-run reads `ok` and one whose re-run reads `fail`. `--fixture flakes-record` writes a record
under `record`, reads it with the factory's `read`, and runs a stub drift kit's measurement with the
record named by `--with`; under `retry-only` it writes none and runs no stub. `--fixture
flakes-window` holds a leg at 2 flakes in 10 and not one at 1 with no gate-health record, none at a
planted `Measured` of 3/10, both legs at one of 1/10, 2/10 again with the kind taken out of the loaded
table for that case alone, and holds no leg released after its flakes. `--fixture
quarantine-source` reads a quarantine row from an ask at R and none from the working tree. `--fixture
quarantine-check` reds a hold below 2/10 and passes one at it. `--fixture measured-check` reds a hold at
2 flakes filed after a gate-health record held 3/10, and passes it with that record dated after the
filing. Each exits 0 when every case reads as planted, 1 naming each that does not.

WHAT IT DOES NOT CHECK. That the attribution was made against the landing base, or that its `blocks`
words were derived by `lib-verdict.sh`: the runner writes both, and the readers that land a red read
them. Spawning the tester or acting on `next`: the loop's engine runs the item the route names. That
a held leg ran anywhere else: `peer-or-cadence` checks a runner is DECLARED, never that it ran.
`select --check` compares rows, never the header, which only names what was read. That the flake
record's rows are true: the runner wrote the `.leg` rows, and `flakes --check` re-derives a hold from
the records, never from the runs. That a released leg's streak was run: TOOL-dWitnessedBar-30's.
"""
import argparse
import datetime
import json
import os
import pathlib
import re
import shlex
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
ROUTES = ("flakes", "attribute", "quiet-rerun", "probe-repair", "fix-unit", "ask")
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
# THE FLAKES (TOOL-dWitnessedBar-8). A flake is a row whose first rc is non-zero and whose re-run rc is 0.
ASKS_KEY = "ASKS_CMD"
FLAKES_KEY = "verdict.flakes"
FLAKES_VALUES = ("quarantine", "record", "retry-only")
FLAKES_DEFAULT = "quarantine"
ENTRY_KEY = "verdict.flakes.entry"
ENTRY_MEASURED = "measured"
ENTRY_DEFAULT = (2, 10)  # v2:1274's literal default, held until a gate-health record says otherwise
ENTRY_FORM = re.compile(r"([0-9]+)/([0-9]+)")
FLAKE_KIND = "flake"
HEALTH_KIND = "gate-health"  # registered by TOOL-dWitnessedBar-1; read only while the factory holds it
HEALTH_BOUND = 60  # seconds, the gate-health measurement `flakes` runs, inside the driver's 120 (TOOL-dWitnessedBar-1 S5)
FLAKY_FORM = "held flaky leg: leg"
FLAKY_ASK = re.compile(r"held flaky leg: leg (.+?) flaked ([0-9]+) in its last ([0-9]+) verdicts")
LEG_ROW = re.compile(r"([0-9]+)\.leg")


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


def read_leg_attempts(run):
    """{leg name: {attempt suffix: (status, rc)}} of the `<i><sfx>.leg` rows in `run`, each leg named by
    field 1 of its first attempt's `<i>.leg`; the suffix is `` for that attempt, `.retry`, `.rerun`."""
    out = {}
    for p in sorted(run.glob("*.leg")) if run.is_dir() else ():
        m = LEG_ROW.fullmatch(p.name)
        if not m:
            continue
        try:
            first = p.read_text(encoding="utf-8", errors="replace").split("\n", 1)[0].split("\t")
        except OSError:
            continue
        if len(first) < 3 or not first[0]:
            continue
        attempts = out.setdefault(first[0], {})
        for sfx in ("", ".retry", ".rerun"):
            try:
                f = run.joinpath(m.group(1) + sfx + ".leg").read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            f = f.split("\n", 1)[0].split("\t")
            if len(f) >= 3:
                attempts[sfx] = (f[1], f[2])
    return out


def derive_route(cls, blocks, rerun=None):
    """The route word of one red row; `rerun` the status its same-tree re-run's `.leg` row reads."""
    if rerun == "ok":
        return "flakes"
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
    attempts = read_leg_attempts(run)
    out_rows = [(leg, cls, blocks, derive_route(cls, blocks, attempts.get(leg, {}).get(".rerun", ("",))[0]),
                 "-", "-") for leg, cls, blocks in rows]
    write_routing(run, out_rows)
    return 0, [f"route  {leg}  {cls} · {blocks} · {route}" for leg, cls, blocks, route, _, _ in out_rows]


def run_kit(here, home, anchor, args, what, cwd=None, bound=BOUND):
    """The kit `home` found from `here`, its `anchor` run with `args` in `cwd` within `bound` seconds -> the
    completed process."""
    try:
        kit = resolve_kit_dir(home, anchor, here)
    except LookupError as e:
        raise Refusal(f"{what}: {e}") from None
    try:
        return subprocess.run([sys.executable, str(pathlib.Path(kit, anchor)), *args], capture_output=True,
                              encoding="utf-8", errors="replace", timeout=bound, cwd=cwd)
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


def read_conf_at(repo, sha, key):
    """The `key` that `.unattended.conf` declares at `sha`, its last assignment, or '': extracted from
    `read_held_runner` at its second reader, the quarantine source's `ASKS_CMD` (TOOL-dWitnessedBar-8)."""
    value = ""
    for ln in (read_at(repo, sha, UNATTENDED_CONF) or "").splitlines():
        s = ln.strip()
        if s.startswith(key + "="):
            value = s.split("=", 1)[1].split("#", 1)[0].strip().strip("\"'")
    return value


def read_held_runner(repo, sha):
    """The `HELD_CI_WORKFLOW` that `.unattended.conf` declares at `sha`, or ''."""
    return read_conf_at(repo, sha, HELD_RUNNER_KEY)


def read_asks(cwd, cmd):
    """[ask] the ask generator `cmd`, an `ASKS_CMD` value, prints as `--json --all` run in `cwd`, its
    leading `python` the running interpreter and no `GIT_*` knob in its environment."""
    try:
        argv = shlex.split(cmd)
    except ValueError as e:
        raise Refusal(f"{ASKS_KEY} '{cmd}' does not split into a command: {e}") from None
    if argv and argv[0] in ("python", "python3"):
        argv[0] = sys.executable
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    try:
        p = subprocess.run([*argv, "--json", "--all"], cwd=str(cwd), capture_output=True, encoding="utf-8",
                           errors="replace", timeout=BOUND, env=env, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.TimeoutExpired) as e:
        raise Refusal(f"the ask generator {cmd} did not answer: {e}") from None
    try:
        asks = json.loads(p.stdout).get("asks") if p.returncode == 0 else None
    except (ValueError, AttributeError):
        asks = None
    if not isinstance(asks, list):
        first = (p.stderr or p.stdout).strip().splitlines()[-1:]
        raise Refusal(f"the ask generator {cmd} exited {p.returncode} printing no ask list"
                      + (f": {first[0]}" if first else ""))
    return [a for a in asks if isinstance(a, dict)]


def read_asks_at(repo, sha):
    """[ask] the `ASKS_CMD` generator `.unattended.conf` declares at `sha` prints, run in a scratch
    worktree at `sha` as `lib-attribute.sh#add_scratch_worktree` adds one; [] where none is declared."""
    cmd = read_conf_at(repo, sha, ASKS_KEY)
    if not cmd:
        return []
    root = tempfile.mkdtemp(prefix="vflow-r-")
    wt = pathlib.Path(root, "r")
    try:
        rc, _ = run_git(repo, "worktree", "add", "--detach", str(wt), sha)
        if rc != 0:
            raise Refusal(f"no scratch worktree could be added at {sha[:8]}, so the asks at R are unread")
        return read_asks(wt, cmd)
    finally:
        run_git(repo, "worktree", "remove", "--force", str(wt))
        shutil.rmtree(root, ignore_errors=True)


def read_flaky_asks(asks, status):
    """[(leg, flakes, window, ask)] of each `status` ask whose summary opens the held-flaky-leg form."""
    out = []
    for a in asks:
        m = FLAKY_ASK.match(str(a.get("summary", "")))
        if m and a.get("status") == status:
            out.append((m.group(1), int(m.group(2)), int(m.group(3)), a))
    return out


def derive_quarantine_rows(ctx):
    """[(leg, note)] for each leg an OPEN held-flaky-leg ask at R names, the note `<count>/<window>, ask
    <id>`: the asks the generator R declares prints at R, never the working tree's (TOOL-dWitnessedBar-8
    S6), so a branch cannot quarantine a leg it breaks."""
    rows = []
    for leg, flakes, window, a in read_flaky_asks(read_asks_at(ctx["repo"], ctx["sha"]), "OPEN"):
        if leg not in [r[0] for r in rows]:
            rows.append((leg, f"{flakes}/{window}, ask {a.get('id')}"))
    return rows


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
SELECT_SOURCES = (("quarantine", derive_quarantine_rows), ("level", derive_level_rows))


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
    ctx = {"legs": legs, "levels": levels, "cadence": cadence, "repo": repo, "sha": sha}
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


# ---- the flakes (TOOL-dWitnessedBar-8) ---------------------------------------------------------------

def load_flake_factory():
    """(build_records, design_lib, deviation_join) of the memory-tree kit, loaded as `keep_tails.py`
    loads the factory, which puts the kit on `sys.path`."""
    import keep_tails  # noqa: PLC0415 - this kit's loader of the record factory
    try:
        build_records, design_lib, _tree_lib = keep_tails.load_factory()
    except Exception as e:  # keep_tails' own Refusal class, a sibling module's
        raise Refusal(str(e)) from None
    import deviation_join  # noqa: PLC0415 - `read_row_commit`, on the path load_factory put there
    return build_records, design_lib, deviation_join


def read_instant(text):
    """An ISO-8601 instant as an aware UTC datetime, or None."""
    try:
        t = datetime.datetime.fromisoformat(str(text).strip().strip("`").replace("Z", "+00:00"))
    except ValueError:
        return None
    return (t if t.tzinfo else t.replace(tzinfo=datetime.timezone.utc)).astimezone(datetime.timezone.utc)


def read_flake_rows(run):
    """[(leg, first rc, re-run rc or -)] per leg the run executed, in leg-name order: the first rc the
    retry's where one ran. A held, skipped or reused leg wrote no `<i>.leg` and has no row."""
    rows = []
    for leg, att in sorted(read_leg_attempts(run).items()):
        first = att.get(".retry", att.get(""))
        if first is None or not first[1].lstrip("-").isdigit():
            continue
        rerun = att.get(".rerun", (None, "-"))[1]
        rows.append((leg, first[1], rerun if rerun.lstrip("-").isdigit() else "-"))
    return rows


def read_flake_record(build_records, path, text):
    """One flake record: its fields, `id` (the stem), `ended` (UTC) and `rows`, the TAB rows of its body."""
    fields, bad, name = build_records.read_record(path, text, FLAKE_KIND)
    rows = build_records.read_flake_body(text)
    return {**fields, "path": path, "id": pathlib.PurePosixPath(path).stem, "ended": read_instant(fields.get("Ended")),
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "malformed": bad, "rows": rows}


def read_flake_records(top, factory, extra=()):
    """Every tracked flake record of `top` read by the factory's `read_records`, plus each repo-relative
    path of `extra` (one written this call and not yet staged); those with no readable `Ended` dropped."""
    build_records, design_lib, _ = factory
    try:
        recs = build_records.read_records(top, design_lib.read_design_conf(top), FLAKE_KIND,
                                          lambda p, t: read_flake_record(build_records, p, t))
    except design_lib.DesignRefusal as e:
        raise Refusal(f"the tracked {FLAKE_KIND} records do not read: {e}") from None
    held = {r["path"] for r in recs}
    for rel in extra:
        if rel not in held:
            recs.append(read_flake_record(build_records, rel,
                                          pathlib.Path(top, rel).read_bytes().decode("utf-8", "replace")))
    return [r for r in recs if r["ended"] is not None]


def read_flake_threshold(top, factory, entry, at=None):
    """((count, window), said) under `verdict.flakes.entry` `entry`: the declared `<count>/<window>`, or
    under `measured` the `Measured` of the newest gate-health record (dated at or before `at` where it
    is given) while the factory registers that kind, else 2/10."""
    m = ENTRY_FORM.fullmatch(entry)
    if m:
        count, window = int(m.group(1)), int(m.group(2))
        if count < 1 or window < count:
            raise Refusal(f"{ENTRY_KEY} {entry} holds no leg a flake can reach: the count is 1 or more and "
                          f"the window at least the count")
        return (count, window), f"{ENTRY_KEY} {entry}, declared"
    build_records, design_lib, _ = factory
    if HEALTH_KIND not in build_records.KINDS:
        return ENTRY_DEFAULT, (f"{ENTRY_KEY} measured, and the record factory registers no {HEALTH_KIND} kind "
                               f"yet, so no {HEALTH_KIND} record is read and the threshold is 2/10")

    def read_health(path, text):
        fields, bad, name = build_records.read_record(path, text, HEALTH_KIND)
        day = re.match(r"\d{4}-\d{2}-\d{2}", pathlib.PurePosixPath(path).name)
        return {**fields, "path": path, "day": day.group(0) if day else "", "malformed": bad,
                "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None}
    try:
        recs = build_records.read_records(top, design_lib.read_design_conf(top), HEALTH_KIND, read_health)
    except design_lib.DesignRefusal as e:
        raise Refusal(f"the tracked {HEALTH_KIND} records do not read: {e}") from None
    recs = sorted((r for r in recs if r["day"] and (at is None or r["day"] <= at)),
                  key=lambda r: (r["day"], r["n"] or 0, r["path"]))
    if not recs:
        return ENTRY_DEFAULT, f"{ENTRY_KEY} measured, and no {HEALTH_KIND} record is tracked, so the threshold is 2/10"
    newest = recs[-1]
    m = ENTRY_FORM.fullmatch(str(newest.get("Measured", "")).strip().strip("`"))
    if not m or int(m.group(1)) < 1 or int(m.group(2)) < int(m.group(1)):
        return ENTRY_DEFAULT, (f"{ENTRY_KEY} measured, and {newest['path']}'s Measured "
                               f"'{newest.get('Measured', '')}' is no <count>/<window>, so the threshold is 2/10")
    return (int(m.group(1)), int(m.group(2))), f"{ENTRY_KEY} measured, {newest['path']}'s Measured"


def read_flake_releases(top, factory, asks, records):
    """{leg: UTC instant} of each leg's release: over its CLOSED held-flaky-leg asks, the newest committer
    date (%cI) of the oldest commit at HEAD adding `- CLOSED · <id> · ` to the ask's file, found by
    `deviation_join.read_row_commit`; a CLOSED row no commit adds yet dates at the newest row's `Ended`."""
    _, _, deviation_join = factory
    newest = max((r["ended"] for r in records), default=None)
    out = {}
    for leg, _f, _w, a in read_flaky_asks(asks, "CLOSED"):
        sha = deviation_join.read_row_commit(str(top), f"- CLOSED · {a.get('id')} · ", str(a.get("file", "")))
        when = None
        if sha:
            rc, said = run_git(top, "log", "-1", "--format=%cI", sha)
            when = read_instant(said) if rc == 0 else None
        when = when or newest
        if when is not None and (leg not in out or when > out[leg]):
            out[leg] = when
    return out


def derive_flake_holds(factory, records, threshold, releases):
    """[(leg, flakes, window, [record ids])] for each leg whose flakes in its last `window` rows, newest
    `Ended` first across `records` and only those after its release, reach `count`, in leg order. A row
    flaked where the factory's `derive_flaked` says so."""
    build_records = factory[0]
    count, window = threshold
    seen = {}
    for r in sorted(records, key=lambda r: (r["ended"], r["id"]), reverse=True):
        for row in r["rows"]:
            leg, first, rerun = row
            rel = releases.get(leg)
            if rel is not None and r["ended"] <= rel:
                continue
            got = seen.setdefault(leg, [])
            if len(got) < window:
                got.append((build_records.derive_flaked(first, rerun), r["id"]))
    holds = []
    for leg in sorted(seen):
        ids = [rid for flake, rid in seen[leg] if flake]
        if len(ids) >= count:
            holds.append((leg, len(ids), window, list(dict.fromkeys(ids))))
    return holds


def derive_hold_lines(top, factory, entry, asks, extra=()):
    """The `hold` lines `flakes` prints under `quarantine`, the threshold's line first."""
    records = read_flake_records(top, factory, extra)
    threshold, said = read_flake_threshold(top, factory, entry)
    held = {leg for leg, *_ in read_flaky_asks(asks, "OPEN")}
    lines = [f"flakes  threshold {threshold[0]}/{threshold[1]} · {said}"]
    for leg, flakes, window, ids in derive_flake_holds(factory, records, threshold,
                                                       read_flake_releases(top, factory, asks, records)):
        if leg in held:
            lines.append(f"flakes  {leg} flaked {flakes} in {window}, and an OPEN held-flaky-leg ask names it")
        else:
            lines.append(f"hold  {leg}  {flakes}/{window}  {' '.join(ids)}")
    return lines


def read_repo_asks(top):
    """(asks, said) of the `ASKS_CMD` generator `.unattended.conf` declares at this repository's HEAD,
    run in its working tree; ([], why) where none is declared."""
    cmd = read_conf_at(top, "HEAD", ASKS_KEY)
    if not cmd:
        return [], f"no {ASKS_KEY} is declared in {UNATTENDED_CONF}, so no ask is read"
    return read_asks(top, cmd), f"the asks {cmd} prints"


def read_top(repo):
    rc, top = run_git(repo, "rev-parse", "--show-toplevel")
    if rc != 0 or not top.strip():
        raise Refusal(f"{pathlib.Path(repo).as_posix()} is in no git repository")
    return pathlib.Path(top.strip())


def read_flake_policy(top, here):
    """(verdict.flakes, verdict.flakes.entry) read at HEAD by the policy kit, the catalogue defaults where
    no policy kit resolves."""
    value = read_policy_at(top, "HEAD", here, FLAKES_KEY, [FLAKES_DEFAULT], FLAKES_VALUES)[0]
    entry = read_policy_at(top, "HEAD", here, ENTRY_KEY, [ENTRY_MEASURED])[0]
    if entry != ENTRY_MEASURED and not ENTRY_FORM.fullmatch(entry):
        raise Refusal(f"{ENTRY_KEY} reads '{entry}', neither measured nor <count>/<window>")
    return value, entry


def write_gate_health(top, build, unit, rel, here=HERE):
    """-> the lines the drift kit's gate-health measurement prints, run in `top` within HEALTH_BOUND over the
    tracked flake records and `rel`, the one just written (TOOL-dWitnessedBar-1 S5), each unchanged, so the
    driver stages the record a `drift-report: wrote <path>` line names. No drift kit, a non-zero exit or the
    bound firing is one `flakes  gate-health · <why>` line instead, and never a refusal of `flakes`."""
    try:
        p = run_kit(here, "drift-audit", "drift_report.py",
                    ["--gate-health", "--write", "--build", build, "--unit", unit, "--with", rel],
                    "no drift kit measures gate health", cwd=top, bound=HEALTH_BOUND)
    except Refusal as e:
        return [f"flakes  gate-health · {e}"]
    if p.returncode != 0:
        why = next((ln.strip() for ln in p.stderr.splitlines() if ln.strip()), "it printed nothing on stderr")
        return [f"flakes  gate-health · drift_report.py --gate-health exited {p.returncode}: {why}"]
    return [ln for ln in p.stdout.splitlines() if ln.strip()]


def cmd_flakes(run, build, unit, here=HERE, repo=None):
    """-> (rc, out lines). `test.flakes` over one run record, under `verdict.flakes`."""
    top = read_top(repo or pathlib.Path("."))
    value, entry = read_flake_policy(top, here)
    if value == "retry-only":
        return 0, [f"flakes  {FLAKES_KEY} retry-only · no flake record is written", "flakes  re-entry test.verdict"]
    keys, _tails = read_verdict(run)
    header = {}
    try:
        for ln in (run / "header").read_text(encoding="utf-8", errors="replace").splitlines():
            k, _, v = ln.partition("\t")
            header.setdefault(k, v)
    except OSError:
        pass
    rows = read_flake_rows(run)
    lines, extra = [], []
    if not rows:
        lines.append(f"flakes  {run.as_posix()} holds no executed leg's .leg row, so no flake record is written")
    factory = load_flake_factory()
    if rows:
        fields = [("Run", keys.get("run_id") or run.name), ("Ended", keys.get("ended") or "-"),
                  ("Sha", header.get("head") or "-"), ("Tree", keys.get("tree") or "-"), ("Legs", str(len(rows)))]
        body = ["```tsv", *("\t".join(r) for r in rows), "```"]
        try:
            rel = factory[0].write_record(top, build, unit, FLAKE_KIND, f"run {fields[0][1]} of {build}", fields,
                                          lines=body)
        except (ValueError, OSError) as e:
            raise Refusal(f"the record factory refused the flake record: {e}") from None
        flaked = sum(1 for _, first, rerun in rows if factory[0].derive_flaked(first, rerun))
        lines.append(f"{SAY}: wrote {rel} · {len(rows)} leg(s), {flaked} flake(s)")
        extra.append(rel)
        lines += write_gate_health(top, build, unit, rel, here)
    if value == "record":
        return 0, lines + ["flakes  re-entry test.verdict"]
    asks, said = read_repo_asks(top)
    lines.append(f"flakes  asks · {said}")
    lines += derive_hold_lines(top, factory, entry, asks, extra)
    return 0, lines + ["flakes  re-entry test.select"]


def cmd_flakes_check(here=HERE, repo=None):
    """-> (rc, out lines): 1 naming each OPEN held-flaky-leg ask whose leg's flakes, in its window at the
    ask's filing date, fall below the threshold in force then."""
    top = read_top(repo or pathlib.Path("."))
    _value, entry = read_flake_policy(top, here)
    factory = load_flake_factory()
    asks, said = read_repo_asks(top)
    records = read_flake_records(top, factory)
    releases = read_flake_releases(top, factory, asks, records)
    out, bad = [], []
    for leg, _f, _w, a in read_flaky_asks(asks, "OPEN"):
        day = str(a.get("filed", ""))
        (count, window), why = read_flake_threshold(top, factory, entry, day)
        then = [r for r in records if r["ended"].date().isoformat() <= day]
        flakes = {h[0]: h[1] for h in derive_flake_holds(factory, then, (1, window), releases)}.get(leg, 0)
        line = (f"flakes --check  ask {a.get('id')} holds leg {leg}, which flaked {flakes} in its last {window} at "
                f"its filing on {day}, against the entry threshold {count}/{window} ({why})")
        (bad if flakes < count else out).append(line + (", below it" if flakes < count else ""))
    if bad:
        return 1, bad
    return 0, out + [f"flakes --check  {len(out)} held-flaky-leg ask(s) each at or above its threshold · {said}"]


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
DRIFT_HOME = "drift-audit"

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
         "tests.without-cadence": "run-at-landing", "verdict.flakes": "quarantine",
         "verdict.flakes.entry": "measured"}[key] if value is None else value
for v in value if isinstance(value, list) else [value]:
    print(v)
"""
FIXTURE_LEGS = [{"name": "slow suite", "level": "e2e", "argv": ["true"]},
                {"name": "fast suite", "level": "unit", "argv": ["true"]},
                {"name": "kit selftest", "subject": "kit", "argv": ["true"]}]


def write_repo(root, policy, conf=None, extra=None):
    """(repo, here, sha): a committed repository holding FIXTURE_LEGS, `policy` and each `{rel: text}` of
    `extra`, and a policy kit that reads its values at `--rev`."""
    repo = pathlib.Path(root, "repo")
    repo.mkdir()
    (repo / MANIFEST).write_text(json.dumps(FIXTURE_LEGS, indent=2) + "\n", encoding="utf-8", newline="\n")
    (repo / ".governance").mkdir()
    (repo / ".governance" / "policy.toml").write_text(policy, encoding="utf-8", newline="\n")
    if conf is not None:
        (repo / UNATTENDED_CONF).write_text(conf, encoding="utf-8", newline="\n")
    for rel, text in (extra or {}).items():
        repo.joinpath(rel).parent.mkdir(parents=True, exist_ok=True)
        repo.joinpath(rel).write_text(text, encoding="utf-8", newline="\n")
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


def write_leg_rows(run, legs):
    """`<i><sfx>.leg` rows in `run` for each `(leg name, {sfx: (status, rc)})` of `legs`, `<i>` its index."""
    for i, (leg, attempts) in enumerate(legs):
        for sfx, (status, rc) in attempts.items():
            run.joinpath(f"{i}{sfx}.leg").write_text(f"{leg}\t{status}\t{rc}\t1.000\t0\t1\t-\tno\n",
                                                     encoding="utf-8", newline="\n")


def run_fixture_route_flaky():
    out, bad = [], []
    with tempfile.TemporaryDirectory(prefix="vflow-") as root:
        r = "0" * 40
        att = [(leg, "OWN", "1", "0", r, "-", "-", "-", "block", "planted") for leg in ("flaky leg", "steady leg")]
        run = write_run(root, att, ["flaky leg", "steady leg"], 2)
        write_leg_rows(run, [("flaky leg", {"": ("fail", "1"), ".rerun": ("ok", "0")}),
                             ("steady leg", {"": ("fail", "1"), ".rerun": ("fail", "1")})])
        rc, lines = cmd_route(run)
        out += lines
        got = {f[0]: f[3] for f in read_routing(run)}
        for leg, route in (("flaky leg", "flakes"), ("steady leg", "attribute")):
            if got.get(leg) != route:
                bad.append(f"{leg} routed {got.get(leg)}, planted to read {route}")
        if rc != 0:
            bad.append(f"route exited {rc}")
    return out, bad


FLAKE_BUILD, FLAKE_UNIT = "tFlake", "ARCH-tFlake-1"
STUB_ASKS = """import json, pathlib, re
asks = {}
for f in sorted(pathlib.Path("memory/builds").glob("*/BACKLOG.md")):
    for ln in f.read_text(encoding="utf-8").splitlines():
        m = re.match(r"- (\\S+) · filed (\\S+) · (.*)$", ln)
        if m:
            asks[m.group(1)] = {"id": m.group(1), "filed": m.group(2), "summary": m.group(3), "status": "OPEN",
                                "file": f.as_posix()}
        m = re.match(r"- CLOSED · (\\S+) · ", ln)
        if m and m.group(1) in asks:
            asks[m.group(1)]["status"] = "CLOSED"
print(json.dumps({"asks": list(asks.values())}))
"""
BACKLOG_HEAD = "# tFlake — asks\n\n## Asks\n"


def write_flake_repo(root, policy, backlog=""):
    """(repo, here, sha): `write_repo`'s repository holding a memory tree with build `tFlake`, whose
    BACKLOG.md holds `backlog`, and `ASKS_CMD` declared as a planted generator reading every BACKLOG.md."""
    extra = {"asks.py": STUB_ASKS, ".memory-tree.conf": "MEMORY_ROOT=memory\n",
             f"memory/builds/{FLAKE_BUILD}/BACKLOG.md": BACKLOG_HEAD + backlog}
    return write_repo(root, policy, f'{ASKS_KEY}="python asks.py"\n', extra)


def write_fixture_commit(repo, message):
    for args in (("add", "-A"), ("-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid",
                                 "commit", "-q", "--no-verify", "-m", message)):
        rc, _ = run_git(repo, *args)
        if rc != 0:
            raise Refusal(f"the fixture's git {' '.join(args[-4:])} exited {rc}")


def write_flake_rows(factory, repo, ended, rows):
    """One flake record of the fixture build, `Ended` `ended`, its `rows` -> its id."""
    rel = factory[0].write_record(repo, FLAKE_BUILD, FLAKE_UNIT, FLAKE_KIND, "planted",
                                  [("Run", "planted"), ("Ended", ended), ("Sha", "-"), ("Tree", "-"),
                                   ("Legs", str(len(rows)))], lines=["```tsv", *("\t".join(r) for r in rows), "```"])
    return pathlib.PurePosixPath(rel).stem


def write_flake_ask(leg, n, filed, flakes=2, window=10):
    return (f"- ARCH-tFlake-{n} · filed {filed} · {FLAKY_FORM} {leg} flaked {flakes} in its last {window} verdicts · "
            f"seen planted · accept the leg is released after its streak, or its flake is fixed\n")


STUB_DRIFT = """import sys
print("stub-drift: argv " + " ".join(sys.argv[1:]))
"""


def run_fixture_flakes_record():
    out, bad = [], []
    for value in ("record", "retry-only"):
        with tempfile.TemporaryDirectory(prefix="vflow-") as root:
            repo, here, sha = write_flake_repo(root, f'[verdict]\nflakes = "{value}"\n')
            # a stub drift kit beside the kits, printing the argv the gate-health measurement is run with
            (here / DRIFT_HOME).mkdir()
            (here / DRIFT_HOME / "drift_report.py").write_text(STUB_DRIFT, encoding="utf-8")
            run = pathlib.Path(root, "run")
            run.mkdir()
            (run / "verdict").write_text("ended\t2026-01-02T03:04:05Z\nverdict\tRED\nfailed\t2\ntree\t" + "a" * 40
                                         + "\nrun_id\tfx-1\n", encoding="utf-8", newline="\n")
            (run / "header").write_text(f"head\t{sha}\n", encoding="utf-8", newline="\n")
            # a flaky leg, a green one, and one whose ceiling fired and whose retry failed; a held,
            # skipped or reused leg writes no `.leg`, so the record holds three rows
            write_leg_rows(run, [("flaky leg", {"": ("fail", "1"), ".rerun": ("ok", "0")}),
                                 ("steady leg", {"": ("ok", "0")}),
                                 ("slow leg", {"": ("timeout", "124"), ".retry": ("fail", "1")})])
            try:
                rc, lines = cmd_flakes(run, FLAKE_BUILD, FLAKE_UNIT, here, repo)
            except Refusal as e:
                rc, lines = 2, [f"refused · {e}"]
            out += [f"{value}: {ln}" for ln in lines]
            written = sorted(repo.joinpath("memory/builds", FLAKE_BUILD, "build").glob(f"*-{FLAKE_KIND}-*.md"))
            stub = [ln for ln in lines if ln.startswith("stub-drift: argv ")]
            if value == "retry-only":
                if rc != 0 or written:
                    bad.append(f"under retry-only flakes exited {rc} writing {len(written)} record(s), planted to write none")
                if stub:
                    bad.append(f"under retry-only the gate-health measurement ran: {stub}")
                continue
            if rc != 0 or len(written) != 1:
                bad.append(f"under record flakes exited {rc} writing {len(written)} record(s), planted to write one: {lines}")
                continue
            rel = written[0].relative_to(repo).as_posix()
            want = f"--gate-health --write --build {FLAKE_BUILD} --unit {FLAKE_UNIT} --with {rel}"
            if stub != [f"stub-drift: argv {want}"]:
                bad.append(f"under record the gate-health measurement printed {stub}, planted one run with {want}")
            factory = load_flake_factory()
            rec = read_flake_record(factory[0], written[0].relative_to(repo).as_posix(),
                                    written[0].read_text(encoding="utf-8"))
            missing = [k for k in ("Run", "Ended", "Sha", "Tree", "Legs") if not rec.get(k)]
            want = [("flaky leg", "1", "0"), ("slow leg", "1", "-"), ("steady leg", "0", "-")]
            if missing or sorted(rec["rows"]) != want or rec.get("Legs") != "3":
                bad.append(f"the record lacks {missing} or holds rows {rec['rows']}, planted {want}")
            p = subprocess.run([sys.executable, factory[0].__file__, "read", str(written[0])], capture_output=True,
                               encoding="utf-8", errors="replace", timeout=BOUND)
            out.append(f"{value}: build_records.py read exit {p.returncode}")
            if p.returncode != 0 or "malformed" in p.stdout:
                bad.append(f"the factory's read graded the record exit {p.returncode}: {p.stdout.strip()[:300]}")
    return out, bad


def run_fixture_flakes_window():
    out, bad = [], []
    with tempfile.TemporaryDirectory(prefix="vflow-") as root:
        repo, here, _ = write_flake_repo(root, "")
        factory = load_flake_factory()
        kinds = factory[0].KINDS
        ids = []
        # Eleven runs, oldest first: A flaked in the oldest, outside its window, and twice in its last ten;
        # B flaked once and was red, unflaked, once more.
        for k in range(11):
            a = ("A", "1", "0") if k in (0, 3, 7) else ("A", "0", "-")
            b = ("B", "1", "0") if k == 5 else ("B", "1", "1") if k == 6 else ("B", "0", "-")
            ids.append(write_flake_rows(factory, repo, f"2026-01-{k + 1:02d}T00:00:00Z", [a, b]))
        write_fixture_commit(repo, "eleven flake records")
        want = f"hold  A  2/10  {ids[7]} {ids[3]}"

        def read_holds(what):
            asks, _ = read_repo_asks(repo)
            lines = derive_hold_lines(repo, factory, ENTRY_MEASURED, asks)
            out.extend(f"{what}: {ln}" for ln in lines)
            return [ln for ln in lines if ln.startswith("hold  ")]
        got = read_holds("no gate-health record")
        if got != [want]:
            bad.append(f"with no gate-health record the holds read {got}, planted [{want}]")
        # TOOL-dWitnessedBar-1 S8: the factory registers the kind, so the records are planted as the drift kit
        # writes them; the unregistered case takes the kind out of the loaded table for itself alone.
        if kinds.get(HEALTH_KIND) is None:
            bad.append(f"the factory registers no {HEALTH_KIND} kind, so no Measured case is a case")
            return out, bad
        health = [("Verdicts", "planted"), ("Legs", "2/2")]
        factory[0].write_record(repo, FLAKE_BUILD, FLAKE_UNIT, HEALTH_KIND, "planted", [("Measured", "3/10"), *health])
        write_fixture_commit(repo, "a gate-health record above A's flakes")
        got = read_holds("Measured 3/10")
        if got:
            bad.append(f"with Measured 3/10 the holds read {got}, planted none")
        factory[0].write_record(repo, FLAKE_BUILD, FLAKE_UNIT, HEALTH_KIND, "planted", [("Measured", "1/10"), *health])
        write_fixture_commit(repo, "a newer gate-health record at one in ten")
        want_one = [f"hold  A  2/10  {ids[7]} {ids[3]}", f"hold  B  1/10  {ids[5]}"]
        got = read_holds("Measured 1/10")
        if got != want_one:
            bad.append(f"with Measured 1/10 the holds read {got}, planted {want_one}")
        entry = kinds.pop(HEALTH_KIND)
        try:
            got = read_holds("the records planted, the kind out of the table")
        finally:
            kinds[HEALTH_KIND] = entry
        if got != [want]:
            bad.append(f"with no gate-health kind registered the holds read {got}, planted [{want}]")
        if kinds.get(HEALTH_KIND) is not entry:
            bad.append(f"the {HEALTH_KIND} kind is not back in the table after the unregistered case")
        # the release case reads at 2/10, so its gate-health records leave the tree first
        for p in sorted(repo.joinpath("memory/builds", FLAKE_BUILD, "build").glob(f"*-{HEALTH_KIND}-*.md")):
            p.unlink()
        write_fixture_commit(repo, "the gate-health records removed")
        bl = repo.joinpath("memory/builds", FLAKE_BUILD, "BACKLOG.md")
        with bl.open("a", encoding="utf-8", newline="\n") as fh:
            fh.write(write_flake_ask("A", 9, "2026-01-12"))
        write_fixture_commit(repo, "A's ask")
        with bl.open("a", encoding="utf-8", newline="\n") as fh:
            fh.write("- CLOSED · ARCH-tFlake-9 · by planted · released\n")
        write_fixture_commit(repo, "A's ask closed")
        asks, _ = read_repo_asks(repo)
        records = read_flake_records(repo, factory)
        rel = read_flake_releases(repo, factory, asks, records).get("A")
        out.append(f"A released at {rel}")
        if rel is None or rel <= max(r["ended"] for r in records):
            bad.append(f"A's release read {rel}, planted after its flakes")
        got = read_holds("A's ask closed after its flakes")
        if got:
            bad.append(f"with A released after its flakes the holds read {got}, planted none")
    return out, bad


def run_fixture_quarantine_source():
    out, bad = [], []
    with tempfile.TemporaryDirectory(prefix="vflow-") as root:
        repo, here, sha = write_flake_repo(root, "", write_flake_ask("A", 2, "2026-01-12"))
        bl = repo.joinpath("memory/builds", FLAKE_BUILD, "BACKLOG.md")
        with bl.open("a", encoding="utf-8", newline="\n") as fh:
            fh.write(write_flake_ask("B", 3, "2026-01-13"))
        tree = [leg for leg, *_ in read_flaky_asks(read_asks(repo, "python asks.py"), "OPEN")]
        out.append(f"the working tree's generator reads OPEN asks for {tree}")
        if tree != ["A", "B"]:
            bad.append(f"the working tree's asks read {tree}, planted A and B, so the case is no case")
        try:
            _held, _header, rows, said = derive_selection(repo, sha, here, MANIFEST)
        except Refusal as e:
            rows, said = [], [f"refused · {e}"]
        out += said + [f"select  {leg}  {src} · {note}" for leg, src, note in rows]
        got = [r for r in rows if r[1] == "quarantine"]
        if got != [("A", "quarantine", "2/10, ask ARCH-tFlake-2")]:
            bad.append(f"the quarantine rows at R read {got}, planted A's alone")
    return out, bad


def run_fixture_quarantine_check():
    out, bad = [], []
    with tempfile.TemporaryDirectory(prefix="vflow-") as root:
        repo, here, _ = write_flake_repo(root, "", write_flake_ask("C", 4, "2026-02-01"))
        factory = load_flake_factory()
        for k in range(10):
            write_flake_rows(factory, repo, f"2026-01-{k + 1:02d}T00:00:00Z", [("C", "1", "0") if k == 4 else ("C", "0", "-")])
        # a flake after the ask's filing date, which its window at that date does not hold
        write_flake_rows(factory, repo, "2026-03-01T00:00:00Z", [("C", "1", "0")])
        write_fixture_commit(repo, "C's records")
        for what, want in (("1 flake in 10 at the filing", 1), ("2 flakes in 10 at the filing", 0)):
            if want == 0:
                write_flake_rows(factory, repo, "2026-01-20T00:00:00Z", [("C", "1", "0")])
                write_fixture_commit(repo, "a second flake before the filing")
            try:
                rc, lines = cmd_flakes_check(here, repo)
            except Refusal as e:
                rc, lines = 2, [f"refused · {e}"]
            out += [f"{what}: rc {rc} · {ln}" for ln in lines]
            text = " ".join(lines)
            if rc != want or (want and not all(s in text for s in ("leg C", "flaked 1 ", "2/10"))):
                bad.append(f"{what}: flakes --check exited {rc}, planted {want}: {lines}")
    return out, bad


def run_fixture_measured_check():
    """TOOL-dWitnessedBar-1 S6: a hold at two in ten, its ask filed after a gate-health record held 3/10, reds
    `flakes --check`; the same record dated after the ask leaves 2/10 in force at the filing, and passes."""
    out, bad = [], []
    for what, dated, want in (("Measured 3/10 dated before the ask", "2026-01-20", 1),
                              ("Measured 3/10 dated after the ask", "2026-02-10", 0)):
        with tempfile.TemporaryDirectory(prefix="vflow-") as root:
            repo, here, _ = write_flake_repo(root, "", write_flake_ask("D", 5, "2026-02-01"))
            factory = load_flake_factory()
            for k in range(10):
                write_flake_rows(factory, repo, f"2026-01-{k + 1:02d}T00:00:00Z",
                                 [("D", "1", "0") if k in (2, 6) else ("D", "0", "-")])
            factory[0].write_record(repo, FLAKE_BUILD, FLAKE_UNIT, HEALTH_KIND, "planted",
                                    [("Measured", "3/10"), ("Verdicts", "planted"), ("Legs", "1/1")], today=dated)
            write_fixture_commit(repo, "D's records and a gate-health record")
            try:
                rc, lines = cmd_flakes_check(here, repo)
            except Refusal as e:
                rc, lines = 2, [f"refused · {e}"]
            out += [f"{what}: rc {rc} · {ln}" for ln in lines]
            text = " ".join(lines)
            if rc != want or (want and not all(s in text for s in ("leg D", "flaked 2 ", "3/10"))):
                bad.append(f"{what}: flakes --check exited {rc}, planted {want}: {lines}")
    return out, bad


FIXTURES = {"route": run_fixture_route, "red-route": run_fixture_red_route,
            "selection-rows": run_fixture_selection_rows, "held-keys": run_fixture_held_keys,
            "select": run_fixture_select, "held-policy": run_fixture_held_policy,
            "route-flaky": run_fixture_route_flaky, "flakes-record": run_fixture_flakes_record,
            "flakes-window": run_fixture_flakes_window, "quarantine-source": run_fixture_quarantine_source,
            "quarantine-check": run_fixture_quarantine_check, "measured-check": run_fixture_measured_check}


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
        try:
            out, bad = FIXTURES[argv[1]]()
        except Refusal as e:
            out, bad = [], [f"refused · {e}"]
        for ln in out:
            print(ln)
        for ln in bad:
            print(f"{SAY}: fixture {argv[1]} FAILED · {ln}", file=sys.stderr)
        print(f"{SAY}: fixture {argv[1]} " + ("FAILED" if bad else "ok"))
        return 1 if bad else 0
    ap = argparse.ArgumentParser(prog="verdict_flow.py", description=__doc__.split("\n")[0])
    ap.add_argument("verb", choices=("route", "judge", "select", "flakes"))
    ap.add_argument("--run")
    ap.add_argument("--selection")
    ap.add_argument("--build")
    ap.add_argument("--unit")
    ap.add_argument("--leg")
    ap.add_argument("--judgment")
    ap.add_argument("--rev")
    ap.add_argument("--out")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    try:
        # `--run` is asked of route, judge and flakes, and `select --check` asks it or `--selection`, exactly
        # one (TOOL-dWitnessedBar-41 S4): `select` writes no run record. `flakes --check` reads the
        # repository it runs in and takes none of the three (TOOL-dWitnessedBar-8 §8 F10).
        run = None
        if a.selection is not None and not (a.verb == "select" and a.check):
            raise Refusal("--selection is asked of select --check alone")
        if (a.build is not None or a.unit is not None) and not (a.verb == "flakes" and not a.check):
            raise Refusal("--build and --unit are asked of flakes alone, never of flakes --check")
        if a.verb == "flakes" and a.check and a.run is not None:
            raise Refusal("flakes --check takes no --run: it reads the asks and records of this repository")
        if a.verb == "select" and a.check and (a.run is None) == (a.selection is None):
            raise Refusal("select --check takes exactly one of --run <run dir> and --selection <path>")
        if a.verb == "flakes" and not a.check and not (a.build and a.unit):
            raise Refusal("flakes takes --build <slug> and --unit <id>, the record's build and unit")
        if (a.verb != "select" or a.check) and a.selection is None and not (a.verb == "flakes" and a.check):
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
        elif a.verb == "flakes":
            rc, out = cmd_flakes_check() if a.check else cmd_flakes(run, a.build, a.unit)
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
