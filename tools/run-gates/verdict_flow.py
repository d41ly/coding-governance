#!/usr/bin/env python3
"""verdict_flow.py — a red bar's reds joined to routes, and the tester's judgment of a routed red.

    python <this kit>/verdict_flow.py route --run <run dir>
    python <this kit>/verdict_flow.py judge --run <run dir> --leg <name> --judgment <word>
    python <this kit>/verdict_flow.py --fixture route|red-route

TOOL-dWitnessedBar-3 S6, S7. `<run dir>` is one run record of the runner, `<git dir>/gate-run/<run id>`.

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

A kit imports no sibling kit: both are run as subprocesses, each found through the kit's inline copy
of the sibling-kit resolver.

EXIT 0 written · 2 refused, nothing written: no verdict, a verdict that is not RED, a malformed
attribution or routing record, a leg with no routed row or one not routed `attribute`, a word outside
the outcome set, no loop kit or one whose `loop_lib.py` does not answer the verb, or a policy read that
fails or answers outside `verdict.red-route`'s values.

`--fixture route` plants a run dir under the system temp directory whose attribution holds one row of
each class under `own-only` and whose verdict counts one more red the attribution omits.
`--fixture red-route` plants stub loop and policy kits and judges under each value, a word outside the
set, no loop kit, and a loop kit without the verb. Each exits 0 when every case reads as planted, 1
naming each that does not.

WHAT IT DOES NOT CHECK. That the attribution was made against the landing base, or that its `blocks`
words were derived by `lib-verdict.sh`: the runner writes both, and the readers that land a red read
them. Spawning the tester or acting on `next`: the loop's engine runs the item the route names.
"""
import argparse
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


def run_kit(here, home, anchor, args, what):
    """The kit `home` found from `here`, its `anchor` run with `args` -> the completed process."""
    try:
        kit = resolve_kit_dir(home, anchor, here)
    except LookupError as e:
        raise Refusal(f"{what}: {e}") from None
    try:
        return subprocess.run([sys.executable, str(pathlib.Path(kit, anchor)), *args], capture_output=True,
                              encoding="utf-8", errors="replace", timeout=BOUND)
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


FIXTURES = {"route": run_fixture_route, "red-route": run_fixture_red_route}


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
    ap.add_argument("verb", choices=("route", "judge"))
    ap.add_argument("--run", required=True)
    ap.add_argument("--leg")
    ap.add_argument("--judgment")
    a = ap.parse_args(argv)
    run = pathlib.Path(a.run)
    try:
        if not run.is_dir():
            raise Refusal(f"{run.as_posix()} is no run record directory")
        if a.verb == "route":
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
