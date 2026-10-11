#!/usr/bin/env python3
"""held_halves.py — split the held self-test tier between a native half and a WSL half, and combine.

    python <prefix>/run-gates/held_halves.py --host
    python <prefix>/run-gates/held_halves.py --partition --half windows|wsl|all --out <file>
    python <prefix>/run-gates/held_halves.py --combine --windows <dir> --wsl <dir> --sha <S> \
        --fingerprint <fp> --manifest-blob <blob> [--paired]
    python <prefix>/run-gates/held_halves.py --selftest

TOOL-aSparedSpawn-5. `run-held-wsl.sh` beside this file is the only caller outside the self-test.

THE HELD POPULATION is the runner's own predicate: a leg whose `subject` is `kit` or whose `chunk` is
`selftests`, the legs a bar holds until `GATE_SELFTESTS=1` asks for them. The Windows-only
declaration names the held legs that must run natively; every other held leg runs in WSL. A
declaration row naming no held leg is REFUSED, so a renamed or removed leg cannot leave a row behind
that quietly sends nothing anywhere.

THE COMBINE REFUSES, exit 2, unless both halves left a verdict, both graded the pinned fingerprint at
the pinned sha, neither moved its tree, both partitioned one manifest blob, and every held leg was
reported by exactly one half on the host the declaration names. Otherwise it exits by the runner's
own precedence: 1 RED, then 4 HOST, then 3 TREE MOVED, then 0 GREEN.

`held-green` is written ONLY by a plain combine that is GREEN while the parity record holds the
declared number of consecutive paired runs, at this manifest blob, agreeing on every compared leg.
A paired run appends its rows and writes no record.

WHAT THIS DOES NOT CHECK. It does not run a leg, and it does not prove a WSL green means what a
Windows green means: that is the paired-run record's job, and the record grades only the legs both
hosts ran. No boundary reads `held-green` yet, so the record certifies nothing on its own. It reads
the halves' files as the wrapper copied them and cannot tell a forged half directory from a real one.
"""
import argparse
import contextlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

KITDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, KITDIR)
from profile_bar import parse_verdicts  # noqa: E402  the runner's verdict grammar, read in one place

# The manifest is the kit dir's SIBLING and the declaration sits in the kit dir, both derived and never
# spelled, because this kit installs at <prefix>/run-gates/ and a literal resolves at one prefix only.
MANIFEST_BESIDE = os.path.join(os.path.dirname(KITDIR), "gate-legs.json")
DECLARATION_BESIDE = os.path.join(KITDIR, "windows-only-legs.txt")
# The shim every partition row runs its leg through. `{prefix}` is the runner's own token, resolved
# per tree, and the kit dir's name is read from this file's location.
SHIM = "{prefix}/" + os.path.basename(KITDIR) + "/run-held-wsl.sh"

SHARED_FILE = ".githooks/gate-env.sh"
NODE_FILE = "gate-wsl.conf"
NODE_KEYS = ("GATE_WSL_DISTRO", "GATE_WSL_MIRROR")
STAMP_FILE = "held-green"
PARITY_FILE = "held-parity"
HOSTS = ("windows", "wsl")
# The runner's exit precedence: first match wins (`run-gates.sh` header).
EXIT_OF = {"REFUSED": 2, "RED": 1, "HOST": 4, "TREE MOVED": 3, "GREEN": 0}
PRECEDENCE = (2, 1, 4, 3, 0)
DISTRO_SHAPE = re.compile(r"^[A-Za-z0-9._-]+$")
MIRROR_SHAPE = re.compile(r"^/[A-Za-z0-9._/-]+$")


def print_refusal(msg):
    """Print one refusal line and leave with exit 2. Every precondition miss ends here."""
    print("held-halves: REFUSED — " + msg)
    raise SystemExit(2)


def test_held(leg):
    """The runner's hold predicate, one statement of it."""
    return leg.get("subject") == "kit" or leg.get("chunk") == "selftests"


def load_manifest(path):
    try:
        with open(path, encoding="utf-8") as fh:
            legs = json.load(fh)
    except (OSError, ValueError) as e:
        print_refusal(f"the manifest {path} cannot be read: {e}")
    if not isinstance(legs, list) or not all(isinstance(l, dict) and l.get("name") for l in legs):
        print_refusal(f"the manifest {path} is not a list of named legs")
    return legs


def load_declaration(path, held_names):
    """The Windows-only rows: `<held leg name> TAB <reason>`. Any row that names no held leg refuses."""
    if not os.path.isfile(path):
        print_refusal(f"no Windows-only declaration at {path}, so no leg can be placed on a host")
    native = []
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.rstrip("\r\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            name, _, reason = line.partition("\t")
            if not reason.strip():
                print_refusal(f"{path} row {n} '{name}' carries no reason after a TAB")
            if name not in held_names:
                print_refusal(f"{path} row {n} names '{name}', which is not a held leg of the manifest")
            if name in native:
                print_refusal(f"{path} row {n} names '{name}' a second time")
            native.append(name)
    return native


def build_partition(legs, native, half):
    """The held rows for one half, in manifest order, each running its leg through the shim."""
    rows = []
    for leg in legs:
        if not test_held(leg):
            continue
        if half == "windows" and leg["name"] not in native:
            continue
        if half == "wsl" and leg["name"] in native:
            continue
        row = dict(leg)
        row["argv"] = ["bash", SHIM, "--leg"] + list(leg["argv"])
        rows.append(row)
    return rows


def read_record(path):
    """A `key TAB value` file -> dict, or None when the file is absent."""
    if not os.path.isfile(path):
        return None
    out = {}
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            k, _, v = line.rstrip("\r\n").partition("\t")
            if k:
                out[k] = v
    return out


def load_half(path, host, causes):
    """One half directory -> dict. A missing piece is a cause, never a default."""
    half = {"host": host, "path": path}
    for part in ("meta", "verdict", "header"):
        half[part] = read_record(os.path.join(path, part))
        if half[part] is None:
            why = " (a `wsl --shutdown` or a reboot ends a half without one)" if part == "verdict" else ""
            causes.append(f"the {host} half left no {part} file at {path}{why}")
    try:
        with open(os.path.join(path, "stdout"), encoding="utf-8", errors="replace") as fh:
            half["legs"] = parse_verdicts(fh.read())
    except OSError:
        half["legs"] = []
        causes.append(f"the {host} half left no runner stdout at {path}")
    return half


def check_halves(halves, sha, fingerprint, blob, held, native, paired):
    """Every precondition the combine owes, as a list of causes; empty means accepted."""
    causes = []
    for h in halves.values():
        meta, verdict, header, host = h["meta"] or {}, h["verdict"] or {}, h["header"] or {}, h["host"]
        if h["meta"] is not None and meta.get("host") != host:
            causes.append(f"the {host} half's meta names host '{meta.get('host')}'")
        if h["header"] is not None and header.get("head") != sha:
            causes.append(f"the {host} half's HEAD is {header.get('head') or 'unrecorded'}, not the pinned {sha}")
        if h["verdict"] is not None:
            if verdict.get("fingerprint_end") != fingerprint:
                causes.append(f"the {host} half graded fingerprint {verdict.get('fingerprint_end') or 'none'}, "
                              f"not the pinned {fingerprint}")
            if verdict.get("tree_moved") != "no":
                causes.append(f"the {host} half moved its tree (tree_moved {verdict.get('tree_moved') or 'unrecorded'})")
            if verdict.get("verdict") not in EXIT_OF:
                causes.append(f"the {host} half's verdict '{verdict.get('verdict')}' is not one the runner writes")
    blobs = {h["host"]: (h["meta"] or {}).get("manifest_blob") for h in halves.values()}
    if any(b != blob for b in blobs.values()):
        causes.append("the halves partitioned two manifest blobs: windows "
                      f"{blobs.get('windows') or 'none'}, wsl {blobs.get('wsl') or 'none'}, pinned {blob}")
    ran = {host: [n for n, _ in h["legs"]] for host, h in halves.items()}
    for host, names in ran.items():
        for name in sorted(set(n for n in names if names.count(n) > 1)):
            causes.append(f"leg '{name}' is reported twice by the {host} half")
        for name in names:
            if name not in held:
                causes.append(f"leg '{name}' ran in the {host} half and is outside the held population")
    for name in held:
        on = [host for host in HOSTS if name in ran[host]]
        want = ["windows"] if name in native else (["windows", "wsl"] if paired else ["wsl"])
        if not on:
            causes.append(f"leg '{name}' is absent from both halves")
        elif on != want:
            causes.append(f"leg '{name}' ran on {' and '.join(on)}, where the declaration places it on "
                          f"{' and '.join(want)}")
    return causes


def render_path(base, rel):
    """A path to print: forward-slashed, so it reads as one spelling on every host."""
    return os.path.join(base, rel).replace(chr(92), "/")


def resolve_wsl_host(root, common_dir):
    """The distro, mirror and parity count, each with its source. Refuses on a key it must not take."""
    shared = render_path(root, SHARED_FILE)
    shared_vals = parse_conf(shared, ("GATE_WSL_MIRROR_DEFAULT", "GATE_WSL_PARITY_RUNS"), strict=False)
    node = render_path(common_dir, NODE_FILE)
    node_vals = parse_conf(node, NODE_KEYS, strict=True)
    host = {"node_file": node, "node_declared": os.path.isfile(node)}
    if node_vals.get("GATE_WSL_DISTRO"):
        host["distro"], host["distro_from"] = node_vals["GATE_WSL_DISTRO"], f"declared in {node}"
    else:
        host["distro"], host["distro_from"] = "", "WSL default distro"
    if node_vals.get("GATE_WSL_MIRROR"):
        host["mirror"], host["mirror_from"] = node_vals["GATE_WSL_MIRROR"], f"declared in {node}"
    elif shared_vals.get("GATE_WSL_MIRROR_DEFAULT"):
        host["mirror"], host["mirror_from"] = shared_vals["GATE_WSL_MIRROR_DEFAULT"], "shared default"
    else:
        print_refusal(f"no mirror is declared: neither {node} carries GATE_WSL_MIRROR nor {shared} "
                      "carries GATE_WSL_MIRROR_DEFAULT")
    if host["distro"] and not DISTRO_SHAPE.match(host["distro"]):
        print_refusal(f"{node} key GATE_WSL_DISTRO '{host['distro']}' is not a distro name")
    if not MIRROR_SHAPE.match(host["mirror"]) or "/../" in host["mirror"] + "/":
        src = node if host["mirror_from"] != "shared default" else shared
        print_refusal(f"{src} key GATE_WSL_MIRROR '{host['mirror']}' is not an absolute Linux path")
    k = shared_vals.get("GATE_WSL_PARITY_RUNS", "")
    if not re.fullmatch(r"[1-9][0-9]*", k):
        print_refusal(f"{shared} key GATE_WSL_PARITY_RUNS '{k}' is not a positive whole count of paired runs")
    host["parity_runs"], host["parity_from"] = int(k), f"declared in {shared}"
    return host


def parse_conf(path, keys, strict):
    """KEY=value lines, PARSED and never sourced. Strict refuses any key outside `keys`."""
    vals = {}
    if not os.path.isfile(path):
        return vals
    with open(path, encoding="utf-8", errors="replace") as fh:
        for n, line in enumerate(fh, 1):
            line = line.rstrip("\r\n").strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r"^(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=(.*)$", line)
            if not m:
                if strict:
                    print_refusal(f"{path} line {n} is not a KEY=value line")
                continue
            key, val = m.group(1), re.sub(r"\s+#.*$", "", m.group(2)).strip().strip("\"'")
            if key in keys:
                vals[key] = val
            elif strict:
                print_refusal(f"{path} key {key} is not admitted; a node declares only {' and '.join(keys)}")
    return vals


def read_parity(path):
    rows = []
    if os.path.isfile(path):
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                f = line.rstrip("\r\n").split("\t")
                if len(f) == 6:
                    rows.append(dict(zip(("sha", "blob", "host", "leg", "verdict", "run"), f)))
    return rows


def measure_parity(rows, blob):
    """(n, disagreeing legs of the latest run that broke the streak) over the runs at this blob.

    n counts the paired runs, newest first, that agree on every compared leg, stopping at the first
    that does not. A run with one host's rows only compares nothing and breaks the streak.
    """
    runs, order = {}, []
    for r in rows:
        if r["blob"] != blob:
            continue
        if r["run"] not in runs:
            runs[r["run"]] = {"windows": {}, "wsl": {}}
            order.append(r["run"])
        if r["host"] in HOSTS:
            runs[r["run"]][r["host"]][r["leg"]] = r["verdict"]
    n = 0
    for run in reversed(order):
        win, wsl = runs[run]["windows"], runs[run]["wsl"]
        compared = [leg for leg in wsl if leg in win]
        bad = [leg for leg in compared if win[leg] != wsl[leg]]
        if not compared:
            return n, [f"(run {run} holds one host's rows only)"]
        if bad:
            return n, bad
        n += 1
    return n, []


def add_parity_rows(path, sha, blob, run, halves):
    """One row per (host, compared leg): the legs the WSL half ran, as both hosts reported them."""
    win = {n: derive_verdict(v) for n, v in halves["windows"]["legs"]}
    wsl = {n: derive_verdict(v) for n, v in halves["wsl"]["legs"]}
    with open(path, "a", encoding="utf-8", newline="\n") as fh:
        for leg in wsl:
            if leg in win:
                for host, verdicts in (("windows", win), ("wsl", wsl)):
                    fh.write("\t".join((sha, blob, host, leg, verdicts[leg], run)) + "\n")


def derive_verdict(v):
    # A reused leg reports what it earned before; the halves run with GATE_REUSE unset, so this is a
    # spelling fold, not a claim that reuse is fresh evidence.
    return "ok" if v in ("ok", "reuse") else v


def write_held_stamp(record_dir, fields):
    path = os.path.join(record_dir, STAMP_FILE)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        for k, v in fields:
            fh.write(f"{k}\t{v}\n")
    os.replace(tmp, path)
    return path


def read_git(args, cwd=None):
    try:
        return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True,
                              check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def run_combine(a, host):
    record_dir = a.common_dir
    parity_path = os.path.join(record_dir, PARITY_FILE)
    k = host["parity_runs"]
    legs = load_manifest(a.manifest)
    held = [l["name"] for l in legs if test_held(l)]
    native = load_declaration(a.declaration, set(held))
    causes = []
    halves = {"windows": load_half(a.windows, "windows", causes), "wsl": load_half(a.wsl, "wsl", causes)}
    for h in halves.values():
        meta, verdict = h["meta"] or {}, h["verdict"] or {}
        print(f"held-halves: {h['host']} run {meta.get('run_id') or '?'} · verdict "
              f"{verdict.get('verdict') or 'none'} · {meta.get('wall_s') or '?'}s wall")
    n, bad = measure_parity(read_parity(parity_path), a.manifest_blob)
    print(f"held-halves: parity {n}/{k} at manifest {a.manifest_blob}"
          + (f" · disagreeing: {', '.join(bad)}" if bad else ""))
    causes += check_halves(halves, a.sha, a.fingerprint, a.manifest_blob, held, native, a.paired)
    if causes:
        for c in causes:
            print("held-halves: REFUSED — " + c)
        print("held-halves: held-green NOT written — the combine refused")
        return 2
    code = next(c for c in PRECEDENCE
                if c in [EXIT_OF[h["verdict"]["verdict"]] for h in halves.values()] + [0])
    shown = {}
    for host in (("windows",) if a.paired else HOSTS):
        shown.update({name: (v, host) for name, v in halves[host]["legs"]})
    for name in held:
        v, on = shown[name]
        print(f"GATE {v:<5} {name}  ({on})")
    run = f"windows:{halves['windows']['meta'].get('run_id')},wsl:{halves['wsl']['meta'].get('run_id')}"
    if a.paired:
        add_parity_rows(parity_path, a.sha, a.manifest_blob, run, halves)
        n, bad = measure_parity(read_parity(parity_path), a.manifest_blob)
        print(f"held-halves: parity {n}/{k} after this paired run"
              + (f" · disagreeing: {', '.join(bad)}" if bad else ""))
        print("held-halves: held-green NOT written — a paired run records parity only")
        return code
    if code != 0:
        print(f"held-halves: held-green NOT written — the combined verdict exits {code}")
    elif n < k:
        print(f"held-halves: held-green NOT written — parity {n}/{k}, below the {k} agreeing paired runs declared")
    else:
        path = write_held_stamp(record_dir, (
            ("sha", a.sha), ("fingerprint", a.fingerprint), ("manifest_blob", a.manifest_blob),
            ("hosts", run), ("parity", f"{n}/{k}"),
            ("stamped", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))))
        print(f"held-halves: held-green written — {path}")
    return code


def print_host(host):
    print(f"wsl host: distro {host['distro'] or '-'} ({host['distro_from']})")
    print(f"wsl host: mirror {host['mirror']} ({host['mirror_from']})")
    print(f"wsl host: parity-runs {host['parity_runs']} ({host['parity_from']})")
    if host["node_declared"]:
        print(f"wsl host: node conf {host['node_file']} (declared)")
    else:
        print(f"wsl host: node conf {host['node_file']} (absent), so the values above are fallbacks")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--host", action="store_true")
    mode.add_argument("--partition", action="store_true")
    mode.add_argument("--combine", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    p.add_argument("--half", choices=("windows", "wsl", "all"))
    p.add_argument("--out")
    p.add_argument("--windows")
    p.add_argument("--wsl")
    p.add_argument("--sha")
    p.add_argument("--fingerprint")
    p.add_argument("--manifest-blob")
    p.add_argument("--paired", action="store_true")
    p.add_argument("--manifest", default=MANIFEST_BESIDE)
    p.add_argument("--declaration", default=DECLARATION_BESIDE)
    p.add_argument("--root")
    p.add_argument("--common-dir")
    a = p.parse_args(argv)
    if a.selftest:
        return run_selftest()
    if a.partition:
        if not a.half or not a.out:
            print_refusal("--partition needs --half and --out")
        legs = load_manifest(a.manifest)
        native = load_declaration(a.declaration, {l["name"] for l in legs if test_held(l)})
        rows = build_partition(legs, native, a.half)
        with open(a.out, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(rows, fh, indent=2)
            fh.write("\n")
        print(f"held-halves: partition {a.half} · {len(rows)} leg(s) · {len(native)} declared Windows-only")
        return 0
    a.root = a.root or read_git(["rev-parse", "--show-toplevel"])
    a.common_dir = a.common_dir or read_git(["rev-parse", "--path-format=absolute", "--git-common-dir"])
    if not a.root or not a.common_dir:
        print_refusal("not inside a git repository, and neither --root nor --common-dir was given")
    host = resolve_wsl_host(a.root, a.common_dir)
    if a.host:
        print_host(host)
        return 0
    for need in ("windows", "wsl", "sha", "fingerprint", "manifest_blob"):
        if not getattr(a, need):
            print_refusal(f"--combine needs --{need.replace('_', '-')}")
    return run_combine(a, host)


# ---- the self-test --------------------------------------------------------------------------------
# Synthetic manifests, declarations, halves and git dirs, all under one temp dir. It spawns nothing,
# so it grades this file and no host. ARMS_DECLARED is the liveness assertion: an arm stranded past an
# early return lowers the count and reds the run.
ARMS_DECLARED = 33


def seed_half(root, host, legs, verdict="GREEN", sha="s" * 40, fp="f" * 40, blob="b" * 40,
              tree_moved="no", omit=()):
    d = os.path.join(root, host)
    os.makedirs(d, exist_ok=True)
    parts = {
        "meta": f"host\t{host}\nrun_id\t{host}-1\nmanifest_blob\t{blob}\nwall_s\t7\n",
        "verdict": f"verdict\t{verdict}\nfingerprint_end\t{fp}\ntree_moved\t{tree_moved}\n",
        "header": f"head\t{sha}\n",
        "stdout": "".join(f"GATE {v:<5} {n}\n" for n, v in legs),
    }
    for name, text in parts.items():
        if name not in omit:
            with open(os.path.join(d, name), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
    return d


def run_selftest():
    tmp = tempfile.mkdtemp(prefix="held-halves-")
    passed, ran, fails = 0, 0, []

    def arm_case(label, ok):
        nonlocal passed, ran
        ran += 1
        if ok:
            passed += 1
        else:
            fails.append(label)

    def run_main(args):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try:
                code = main(args)
            except SystemExit as e:
                code = e.code
            except Exception as e:  # an arm must red by its own name, never as a traceback
                code = f"crash {e!r}"
        return code, buf.getvalue()

    try:
        manifest = os.path.join(tmp, "legs.json")
        legs = [{"name": "A", "argv": ["bash", "a.test.sh"], "subject": "kit", "chunk": "selftests"},
                {"name": "B", "argv": ["python3", "b.py"], "subject": "repo", "chunk": "selftests"},
                {"name": "C", "argv": ["bash", "c.test.sh"], "subject": "kit", "chunk": "wiring"},
                {"name": "D", "argv": ["bash", "d.sh"], "subject": "repo", "chunk": "product"},
                {"name": "E", "argv": ["bash", "e.test.sh"], "subject": "kit", "chunk": "selftests"}]
        with open(manifest, "w", encoding="utf-8") as fh:
            json.dump(legs, fh)
        decl = os.path.join(tmp, "native.txt")
        with open(decl, "w", encoding="utf-8") as fh:
            fh.write("# comment\nC\treads MSYS spellings\n")
        held = ["A", "B", "C", "E"]

        # AC1 — every held leg lands in exactly one half; a non-held leg in neither; `all` is the lot.
        parts = {}
        for half in ("windows", "wsl", "all"):
            out = os.path.join(tmp, f"part-{half}.json")
            code, _ = run_main(["--partition", "--half", half, "--out", out,
                                "--manifest", manifest, "--declaration", decl])
            with open(out, encoding="utf-8") as fh:
                parts[half] = json.load(fh)
            arm_case(f"AC1 partition {half} exits 0", code == 0)
        names = {h: [r["name"] for r in parts[h]] for h in parts}
        arm_case("AC1 windows half is the declared leg", names["windows"] == ["C"])
        arm_case("AC1 wsl half is every other held leg, in manifest order", names["wsl"] == ["A", "B", "E"])
        arm_case("AC1 the halves are disjoint and cover the held set",
                 sorted(names["windows"] + names["wsl"]) == held and names["all"] == held)
        arm_case("AC1 every row runs through the --leg shim, argv kept",
                 parts["wsl"][1]["argv"] == ["bash", SHIM, "--leg", "python3", "b.py"])
        for label, row in (("a repo leg outside the hold", "D\tstale\n"), ("an absent leg", "Z\tgone\n")):
            stale = os.path.join(tmp, "stale.txt")
            with open(stale, "w", encoding="utf-8") as fh:
                fh.write(row)
            code, out = run_main(["--partition", "--half", "wsl", "--out", os.path.join(tmp, "x.json"),
                                  "--manifest", manifest, "--declaration", stale])
            arm_case(f"AC1 a row naming {label} is refused naming the row",
                     code == 2 and f"row 1 names '{row.split(chr(9))[0]}'" in out)
        # The real manifest beside this kit, where its declaration is present. An adopter holds no
        # declaration (the kit withholds it), and the arm says it did not run rather than passing.
        if os.path.isfile(DECLARATION_BESIDE) and os.path.isfile(MANIFEST_BESIDE):
            real_held = [l["name"] for l in load_manifest(MANIFEST_BESIDE) if test_held(l)]
            got = {}
            for half in ("windows", "wsl"):
                out = os.path.join(tmp, f"real-{half}.json")
                code, text = run_main(["--partition", "--half", half, "--out", out])
                if code != 0:
                    print(text, end="")
                    got[half] = None
                    continue
                with open(out, encoding="utf-8") as fh:
                    got[half] = [r["name"] for r in json.load(fh)]
            w, l = got["windows"], got["wsl"]
            arm_case("AC1 the real manifest's held legs land in exactly one half",
                     w is not None and l is not None and len(real_held) > 0 and len(w) > 0
                     and sorted(w + l) == sorted(real_held) and not set(w) & set(l))
        else:
            print(f"held-halves selftest: SKIP the real-manifest arm — no declaration at {DECLARATION_BESIDE}")
            arm_case("AC1 real-manifest arm announced its skip", True)

        # AC8 and AC6's key refusal — the host, from a scratch root and scratch common dirs.
        root = os.path.join(tmp, "root")
        os.makedirs(os.path.join(root, ".githooks"))
        with open(os.path.join(root, SHARED_FILE), "w", encoding="utf-8") as fh:
            fh.write("GOV_KITROOT=tools\nGATE_WSL_MIRROR_DEFAULT=/c/projects/coding-governance\n"
                     "GATE_WSL_PARITY_RUNS=3\n")
        bare = os.path.join(tmp, "gd-bare")
        os.makedirs(bare)
        code, out = run_main(["--host", "--root", root, "--common-dir", bare])
        arm_case("AC8 undeclared: the shared default mirror, named as such",
                 code == 0 and "mirror /c/projects/coding-governance (shared default)" in out)
        arm_case("AC8 undeclared: no -d distro, named as WSL's default", "distro - (WSL default distro)" in out)
        arm_case("AC8 undeclared: the fallback is announced",
                 f"node conf {render_path(bare, NODE_FILE)} (absent), so the values above are fallbacks" in out)
        declared = os.path.join(tmp, "gd-declared")
        os.makedirs(declared)
        conf = render_path(declared, NODE_FILE)
        with open(conf, "w", encoding="utf-8") as fh:
            fh.write("# node a\nGATE_WSL_DISTRO=claude-u26\nGATE_WSL_MIRROR=/home/u/gov-mirror\n")
        code, out = run_main(["--host", "--root", root, "--common-dir", declared])
        arm_case("AC8 declared: the distro and its file",
                 code == 0 and f"distro claude-u26 (declared in {conf})" in out)
        arm_case("AC8 declared: the mirror beats the shared default",
                 f"mirror /home/u/gov-mirror (declared in {conf})" in out and "shared default" not in out)
        with open(conf, "a", encoding="utf-8") as fh:
            fh.write("GATE_WSL_PARITY_RUNS=1\n")
        code, out = run_main(["--host", "--root", root, "--common-dir", declared])
        arm_case("AC6 a node key outside the two is refused naming file and key",
                 code == 2 and f"{conf} key GATE_WSL_PARITY_RUNS is not admitted" in out)
        with open(conf, "w", encoding="utf-8") as fh:
            fh.write("GATE_WSL_MIRROR=/c/x;rm\n")
        code, out = run_main(["--host", "--root", root, "--common-dir", declared])
        arm_case("AC8 a mirror that is no plain absolute path is refused", code == 2 and "GATE_WSL_MIRROR" in out)

        # AC2 — the combine refusals, one precondition broken per case, against a green control.
        sha, fp, blob = "s" * 40, "f" * 40, "b" * 40
        good_win = [("C", "ok")]
        good_wsl = [("A", "ok"), ("B", "ok"), ("E", "ok")]
        agree = "".join(f"{sha}\t{blob}\t{h}\t{n}\tok\tr{i}\n"
                        for i in range(3) for n in ("A", "B", "E") for h in HOSTS)

        def run_case(case, win=good_win, wsl=good_wsl, win_kw=None, wsl_kw=None, parity=agree, extra=()):
            d = os.path.join(tmp, "case-" + case)
            gd = os.path.join(d, "gd")
            os.makedirs(gd)
            with open(os.path.join(gd, PARITY_FILE), "w", encoding="utf-8") as fh:
                fh.write(parity)
            w = seed_half(d, "windows", win, **(win_kw or {}))
            l = seed_half(d, "wsl", wsl, **(wsl_kw or {}))
            code, out = run_main(["--combine", "--windows", w, "--wsl", l, "--sha", sha, "--fingerprint", fp,
                                  "--manifest-blob", blob, "--manifest", manifest, "--declaration", decl,
                                  "--root", root, "--common-dir", gd] + list(extra))
            return code, out, os.path.isfile(os.path.join(gd, STAMP_FILE)), gd

        code, out, stamped, gd = run_case("green")
        arm_case("AC2 control: a green pair with parity proven exits 0 and writes held-green",
                 code == 0 and stamped and "parity 3/3" in out)
        stamp = read_record(os.path.join(gd, STAMP_FILE)) or {}
        arm_case("AC2 control: held-green carries the pinned sha, both run ids and the parity",
                 stamp.get("sha") == sha and stamp.get("hosts") == "windows:windows-1,wsl:wsl-1"
                 and stamp.get("parity") == "3/3" and stamp.get("manifest_blob") == blob)
        for case, kw, needle in (
                ("no-verdict", {"wsl_kw": {"omit": ("verdict",)}}, "the wsl half left no verdict file"),
                ("fingerprint", {"wsl_kw": {"fp": "e" * 40}}, "graded fingerprint " + "e" * 40),
                ("head", {"wsl_kw": {"sha": "h" * 40}}, "the wsl half's HEAD is " + "h" * 40),
                ("moved", {"win_kw": {"tree_moved": "yes"}}, "the windows half moved its tree"),
                ("two-blobs", {"wsl_kw": {"blob": "c" * 40}}, "partitioned two manifest blobs"),
                ("absent", {"wsl": [("A", "ok"), ("B", "ok")]}, "leg 'E' is absent from both halves")):
            code, out, stamped, _ = run_case(case, **kw)
            arm_case(f"AC2 {case}: refused, exit 2, cause named, no record",
                     code == 2 and needle in out and not stamped)
        code, out, stamped, _ = run_case("red-host", win=[("C", "FAIL")], win_kw={"verdict": "RED"},
                                        wsl_kw={"verdict": "HOST"})
        arm_case("AC2 one RED half and one HOST half exit 1, no record", code == 1 and not stamped)
        code, out, stamped, _ = run_case("host", wsl_kw={"verdict": "HOST"})
        arm_case("AC2 a HOST half beside a GREEN one exits 4", code == 4 and not stamped)
        code, out, stamped, _ = run_case("misplaced", win=[("C", "ok"), ("A", "ok")], wsl=[("B", "ok"), ("E", "ok")])
        arm_case("AC2 a leg on the host the declaration does not name is refused",
                 code == 2 and "leg 'A' ran on windows" in out)

        # AC5 — parity: one disagreeing leg in the latest paired run, and too few runs.
        broken = agree + f"{sha}\t{blob}\twindows\tB\tok\tr9\n{sha}\t{blob}\twsl\tB\tFAIL\tr9\n"
        code, out, stamped, _ = run_case("disagree", parity=broken)
        arm_case("AC5 a disagreeing leg: green verdict, no record, the leg named, parity below the count",
                 code == 0 and not stamped and "disagreeing: B" in out and "parity 0/3" in out)
        code, out, stamped, _ = run_case("too-few", parity="".join(
            f"{sha}\t{blob}\t{h}\tA\tok\tr{i}\n" for i in range(2) for h in HOSTS))
        arm_case("AC5 two agreeing runs of three: no record", code == 0 and not stamped and "parity 2/3" in out)
        code, out, stamped, _ = run_case("other-blob", parity=agree.replace(blob, "c" * 40))
        arm_case("AC5 runs at another manifest blob do not count", not stamped and "parity 0/3" in out)
        code, out, stamped, gd = run_case("paired", win=[("A", "ok"), ("B", "ok"), ("C", "ok"), ("E", "FAIL")],
                                         win_kw={"verdict": "RED"}, parity="", extra=("--paired",))
        rows = read_parity(os.path.join(gd, PARITY_FILE))
        arm_case("AC5 a paired run appends one row per host per compared leg and writes no record",
                 len(rows) == 6 and not stamped and code == 1 and "disagreeing: E" in out)
        code, out, stamped, _ = run_case("paired-gap", win=[("C", "ok"), ("A", "ok")], extra=("--paired",))
        arm_case("AC5 a paired Windows half missing a WSL leg is refused", code == 2 and "leg 'B' ran on wsl" in out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for f in fails:
        print(f"FAIL held-halves selftest: {f}")
    if ran != ARMS_DECLARED:
        print(f"FAIL held-halves selftest: {ran} arm(s) ran against {ARMS_DECLARED} declared")
    print(f"held-halves selftest: {passed}/{ARMS_DECLARED} arms")
    return 0 if not fails and ran == ARMS_DECLARED else 1


if __name__ == "__main__":
    sys.exit(main())
