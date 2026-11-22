#!/usr/bin/env python3
"""product_tests.py — the product-test contract: which legs carrying `level` a manifest may hold.

    python <this kit>/product_tests.py check                  # grade this tree's manifest
    python <this kit>/product_tests.py check --fixture [case] # plant each case, or one, and grade it

TOOL-dWitnessedBar-9 S2. A leg carrying `level` is a product-test leg, its level one of the four
`tests.landing-levels` names in the policy kit's catalogue. A runner adapter is a `[[test_runner]]`
row of a kit descriptor: `detect` names the levels a repository's suite declares, and the leg factory
renders one row per level, `pack` `product-tests`, as `derive_product_rows` derives them here.

`tests.product`, read through the policy kit's `policy.py get` in the tree, or its catalogue default
with the reason where that reader refuses:
  none                   no row carries `level`; `check` reds on any that does.
  declared               the tree's own rows carrying `level`, no adapter row rendered; red on a level
                         outside the four, or on no row carrying one where a runner's `detect` names one.
  declared-with-runners  those rows plus one adapter row per level each detected runner declares; red
                         on a level outside the four, or on a derived adapter row the manifest lacks.
`check` prints the value and where it was read, each product-test row with its level, and the count:
a tree with no product test and no runner prints `0 product-test legs declared` and exits 0.

`--fixture` plants one scratch repository per case under the system temp directory: its policy, its
declarations, a copy of the guardrails kit's adapter, the leg factory's render, then `check`. It prints
`case <name>: red|green` for each and exits 1 where a case reads otherwise than it is planted to.

EXIT 0 green · 1 red · 2 refused: no policy kit, a value outside the catalogue row, a malformed runner
row, a `detect` that neither finds (0) nor finds nothing (1), or a manifest that does not parse.

WHAT IT DOES NOT CHECK. That a leg carrying a level runs tests of that level, or that the adapter's
legs pass: the bar runs them. An adopter's manifest reaches the adapter rows only once its legs are
rendered by the factory; `check` there reads what its manifest holds.
"""
import argparse
import json
import os
import pathlib
import shutil
import stat
import subprocess
import sys
import tempfile
import tomllib

HERE = pathlib.Path(os.path.abspath(__file__)).parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import regen  # noqa: E402 - this kit's descriptor reader, standard library only
from leg_factory import resolve_kit_dir  # noqa: E402 - the kit's inline copy of the sibling resolver
import atexit
import contextlib
import time


# >>> remove_tree_py — canonical copy: owned_scratch.py in gov's lib dir (byte-identical; gated)
# A TREE REMOVAL THAT NEVER SWALLOWS A READ-ONLY FILE (TOOL-dQuietDisk-9 S1). git writes its objects
# read-only, and on Windows an unlink of one raises, so `rmtree(..., ignore_errors=True)` left every
# fixture repository's objects in the temp folder. The hook clears the bit on the failing path and
# retries it once; a removal that still fails raises nothing and answers False, as `ignore_errors` did.
def remove_tree(path) -> bool:
    """`path` removed, read-only files included; True when it is gone. Never raises."""
    def set_writable(func, failed, _exc):
        try:
            os.chmod(failed, 0o700)
            func(failed)
        except OSError:
            pass
    try:
        shutil.rmtree(path, onexc=set_writable)
    except OSError:
        pass
    return not os.path.lexists(path)


@contextlib.contextmanager
def build_scratch_dir(prefix=None):
    """A fresh `tempfile.mkdtemp` directory for the `with` block, removed by `remove_tree` on exit."""
    made = tempfile.mkdtemp(prefix=prefix)
    try:
        yield made
    finally:
        remove_tree(made)
# <<< remove_tree_py

# >>> owned_work_py — canonical copy: owned_scratch.py in gov's lib dir (byte-identical; gated)
# THE OWNED ROOT A PROCESS SITS IN: the nearest of `path` and its parents named `gate-work.*` and
# holding an `owner` file, a bar's `$WORK` or a suite's own root (TOOL-dQuietDisk-9 S2).
def resolve_owned_work(path):
    """The owned `gate-work.*` directory at or above `path`, a pathlib.Path, or None."""
    here = pathlib.Path(path).absolute()
    for d in (here, *here.parents):
        if d.name.startswith("gate-work.") and (d / "owner").is_file():
            return d
    return None
# <<< owned_work_py

# >>> owned_tempdir_py — canonical copy: owned_scratch.py in gov's lib dir (byte-identical; gated)
# A PYTHON SUITE'S OWNED ROOT (TOOL-dQuietDisk-9 S2, S9). Nested in an owned root, a bar's or another
# suite's, it takes that temp dir and makes nothing. Otherwise it sweeps each dead `py:` owner's root
# of this repository, or of a common dir that names no directory, makes `gate-work.*` with an owner
# line and `tmp`, points `tempfile` and the `TMPDIR`, `TEMP` and `TMP` its children read there, and
# removes the whole root at exit. A kill leaves the root with its owner, for the next suite to sweep.
def read_pid_alive(pid) -> bool:
    """False only when `pid` is provably gone; any error reads as alive, so a sweep can only keep."""
    if os.name == "nt":
        # Never `os.kill` here: signal 0 on Windows is CTRL_C_EVENT, sent to the pid's console group.
        try:
            import ctypes
            k32 = ctypes.WinDLL("kernel32", use_last_error=True)
            k32.OpenProcess.restype = ctypes.c_void_p
            handle = k32.OpenProcess(0x1000, False, int(pid))  # PROCESS_QUERY_LIMITED_INFORMATION
            if not handle:
                return ctypes.get_last_error() != 87  # ERROR_INVALID_PARAMETER: no such process
            try:
                code = ctypes.c_ulong()
                if not k32.GetExitCodeProcess(ctypes.c_void_p(handle), ctypes.byref(code)):
                    return True
                return code.value == 259  # STILL_ACTIVE
            finally:
                k32.CloseHandle(ctypes.c_void_p(handle))
        except (OSError, AttributeError, ValueError):
            return True
    try:
        os.kill(int(pid), 0)
    except ProcessLookupError:
        return False
    except (OSError, ValueError):
        return True
    return True


def scan_dead_scratch(ambient, common) -> list:
    """Removes each `gate-work.*` directly under `ambient` whose owner names a dead `py:` pid and
    `common`, or an absolute common dir that names no directory; an empty `common` removes nothing.
    Returns the roots removed, and says one stderr line per root it sweeps."""
    removed = []
    if not common:
        return removed
    try:
        names = sorted(os.listdir(ambient))
    except OSError:
        return removed
    for name in names:
        root = os.path.join(ambient, name)
        if not name.startswith("gate-work.") or not os.path.isdir(root):
            continue
        try:
            with open(os.path.join(root, "owner"), encoding="utf-8") as fh:
                fields = fh.readline().rstrip("\r\n").split("\t")
        except (OSError, UnicodeDecodeError):
            continue
        pid = fields[0][3:] if fields[0].startswith("py:") else ""
        if len(fields) < 2 or not (pid.isascii() and pid.isdigit()):
            continue
        if fields[1] != common and (not os.path.isabs(fields[1]) or os.path.isdir(fields[1])):
            continue
        if read_pid_alive(int(pid)):
            continue
        print(f"owned-scratch: sweeping the scratch of a dead suite (pid {pid}): {root}", file=sys.stderr)
        if remove_tree(root):
            removed.append(root)
    return removed


def init_owned_tempdir() -> str:
    """The temp dir this process's scratch lands in, owned and removed at exit; see the block's head."""
    ambient = tempfile.gettempdir()
    if resolve_owned_work(ambient) is not None:
        tempfile.tempdir = ambient
        return ambient
    try:
        got = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                             capture_output=True, text=True, encoding="utf-8", errors="replace",
                             check=False, stdin=subprocess.DEVNULL)
        common = got.stdout.strip() if got.returncode == 0 else ""
    except OSError:
        common = ""
    scan_dead_scratch(ambient, common)
    root = tempfile.mkdtemp(prefix="gate-work.", dir=ambient)
    atexit.register(remove_tree, root)
    staged = os.path.join(root, f"owner.{os.getpid()}.tmp")
    with open(staged, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(f"py:{os.getpid()}\t{common}\t{int(time.time())}\n")
    os.replace(staged, os.path.join(root, "owner"))
    tmp = os.path.join(root, "tmp")
    os.mkdir(tmp)
    tempfile.tempdir = tmp
    for name in ("TMPDIR", "TEMP", "TMP"):
        os.environ[name] = tmp
    return tmp
# <<< owned_tempdir_py


SAY = "product tests"
PRODUCT_KEY = "tests.product"
LEVELS_KEY = "tests.landing-levels"
PACK = "product-tests"
WITH_RUNNERS = "declared-with-runners"
BOUND = 120  # seconds, each policy read and each `detect`


class Refusal(Exception):
    """Exit 2: the contract cannot be read as written."""


def derive_git_env():
    """This process's environment less every GIT_* knob: a hook's GIT_DIR must not pin a child's tree."""
    return {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}


def read_catalogue_row(name):
    """The policy kit's catalogue row `name`, the schema `tests.*` is read against."""
    try:
        kit = resolve_kit_dir("policy", "policy.py", HERE)
    except LookupError as e:
        raise Refusal(str(e)) from None
    try:
        rows = tomllib.loads((kit / "catalogue.toml").read_text(encoding="utf-8")).get("key") or []
    except (OSError, tomllib.TOMLDecodeError) as e:
        raise Refusal(f"the policy kit's catalogue.toml does not read: {e}") from None
    row = next((r for r in rows if isinstance(r, dict) and r.get("name") == name), None)
    if row is None:
        raise Refusal(f"the policy kit's catalogue holds no {name} row")
    return kit, row


def read_levels():
    """The four levels, as the catalogue's `tests.landing-levels` row names them."""
    _kit, row = read_catalogue_row(LEVELS_KEY)
    of = (row.get("allowed") or {}).get("of") if isinstance(row.get("allowed"), dict) else None
    if not isinstance(of, list) or not of:
        raise Refusal(f"the catalogue's {LEVELS_KEY} row names no levels under allowed.of")
    return tuple(of)


def read_product_value(repo):
    """(`tests.product` at `repo`, where it was read): `policy.py get`, else the catalogue default."""
    kit, row = read_catalogue_row(PRODUCT_KEY)
    try:
        p = subprocess.run([sys.executable, str(kit / "policy.py"), "get", PRODUCT_KEY, "--explain"],
                           cwd=str(repo), env=derive_git_env(), capture_output=True, encoding="utf-8",
                           errors="replace", stdin=subprocess.DEVNULL, timeout=BOUND)
        said, err = p.stdout.split(), [ln for ln in p.stderr.splitlines() if ln.strip()]
        rc = p.returncode
    except (OSError, subprocess.TimeoutExpired) as e:
        said, err, rc = [], [str(e)], None
    if rc == 0 and len(said) == 1:
        value, where = said[0], (err[-1].removeprefix(f"policy: {PRODUCT_KEY} · ") if err else "policy.py get")
        where = f"read by policy.py get · {where}"
    else:
        value = row.get("default")
        where = (f"the catalogue default · policy.py get did not read it: "
                 f"{err[-1] if err else f'exit {rc}'}")
    if value not in (row.get("allowed") or []):
        raise Refusal(f"{PRODUCT_KEY} reads {value!r}, outside the catalogue's {row.get('allowed')!r}")
    return value, where


def check_runner(r, where):
    """`r`, a `[[test_runner]]` row, refused where a key the adapter needs is malformed."""
    def check_argv(v):
        return isinstance(v, list) and len(v) >= 2 and all(isinstance(x, str) and x for x in v)
    if not isinstance(r.get("runner"), str) or not r["runner"]:
        raise Refusal(f"{where}: a [[test_runner]] row carries no runner name")
    if not check_argv(r.get("detect")) or not check_argv(r.get("argv")) or "{level}" not in "".join(r["argv"]):
        raise Refusal(f"{where}: runner {r['runner']!r} needs a detect argv and an argv spelling {{level}}")
    if not isinstance(r.get("levels"), list) or not all(isinstance(x, str) for x in r["levels"]):
        raise Refusal(f"{where}: runner {r['runner']!r} carries no levels list")
    return r


def read_test_runners(root, tool_rel):
    """Every `[[test_runner]]` row of the tree's tracked descriptors, through `regen`'s reader, which
    needs no govkit: [{the row, `kit` as the row spells it, `kit_dir`, `file`}]."""
    try:
        descs = regen.read_descriptors(pathlib.Path(root), tool_rel)
    except regen.Refusal as e:
        raise Refusal(str(e)) from None
    out = []
    for kit_rel, d in descs:
        for r in d.get("test_runner") or []:
            r = check_runner(dict(r), f"{kit_rel}/kit.toml")
            out.append(dict(r, kit=kit_rel, kit_dir=pathlib.Path(root, kit_rel), file=f"{kit_rel}/kit.toml"))
    return out


def read_detected(repo, runners):
    """{runner: [each of its levels its `detect` names in `repo`]}, `detect` run with `{kit}` as the
    kit's directory and a `python`/`python3` launcher as this interpreter."""
    out = {}
    for r in runners:
        argv = [a.replace("{kit}", pathlib.Path(r["kit_dir"]).as_posix()) for a in r["detect"]]
        if "{" in "".join(argv):
            raise Refusal(f"{r['file']}: runner {r['runner']!r} detect {argv!r} carries a token besides {{kit}}")
        if argv[0] in ("python", "python3"):
            argv[0] = sys.executable
        try:
            p = subprocess.run(argv, cwd=str(repo), env=derive_git_env(), capture_output=True,
                               encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL, timeout=BOUND)
        except (OSError, subprocess.TimeoutExpired) as e:
            raise Refusal(f"runner {r['runner']!r} detect did not run: {e}") from None
        if p.returncode not in (0, 1):
            tail = [ln for ln in p.stderr.splitlines() if ln.strip()]
            raise Refusal(f"runner {r['runner']!r} detect exited {p.returncode}: "
                          f"{tail[-1] if tail else 'no reason given'}")
        said = set(p.stdout.split()) if p.returncode == 0 else set()
        out[r["runner"]] = [lv for lv in r["levels"] if lv in said]
    return out


def derive_adapter_row(r, level):
    """The manifest row runner `r` renders for `level`: tag `leg.<runner>.<level>`, pack `product-tests`."""
    return {"name": f"{r['runner']} {level} tests", "tag": f"leg.{r['runner']}.{level}",
            "purpose": f"runs the {level} level of the {r['runner']} suite",
            "argv": [a.replace("{kit}", r["kit"]).replace("{level}", level) for a in r["argv"]],
            "subject": "repo", "pack": PACK, "level": level, "enforces": ["practice.verify"]}


def derive_product_rows(repo, value, runners=None, rows=None, detected=None):
    """The product-test rows `repo`'s manifest may hold under `tests.product` = `value`: none under
    `none`; its own rows carrying `level` under `declared`; those plus one adapter row per level each
    detected runner declares under `declared-with-runners`. `runners`, `rows` (the manifest) and
    `detected` are read from `repo` where not given; the leg factory passes no rows, for adapter rows."""
    if value == "none":
        return []
    if runners is None:
        runners = read_test_runners(repo, derive_tool_rel(repo))
    adapter = []
    if value == WITH_RUNNERS:
        detected = read_detected(repo, runners) if detected is None else detected
        adapter = [derive_adapter_row(r, lv) for r in runners for lv in detected.get(r["runner"], [])]
    if rows is None:
        rows = read_manifest_rows(derive_manifest_path())
    names = {a["name"] for a in adapter}
    return [r for r in rows if "level" in r and r.get("name") not in names] + adapter


def derive_tool_rel(repo):
    """This kit's tool root relative to `repo`: "" where the kits sit at its top."""
    rel = pathlib.Path(os.path.relpath(HERE.parent, repo)).as_posix()
    return "" if rel == "." else rel


def derive_manifest_path():
    """The manifest beside this kit's tool root, the one run-gates.sh reads."""
    return HERE.parent / "gate-legs.json"


def read_manifest_rows(path):
    """The manifest's rows, refused where the file is absent or is no list of objects."""
    try:
        rows = json.loads(pathlib.Path(path).read_bytes().decode("utf-8"))
    except (OSError, ValueError) as e:
        raise Refusal(f"{pathlib.Path(path).as_posix()} does not read as JSON: {e}") from None
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise Refusal(f"{pathlib.Path(path).as_posix()} is no list of leg rows")
    return rows


def check_product_rows(repo, manifest, tool_rel):
    """(lines, findings) for `repo`'s manifest at `manifest` graded against its `tests.product`."""
    value, where = read_product_value(repo)
    levels = read_levels()
    rows = read_manifest_rows(manifest)
    runners = read_test_runners(repo, tool_rel)
    detected = read_detected(repo, runners)
    own = [r for r in rows if "level" in r]
    lines = [f"{SAY}: {PRODUCT_KEY} = {value} · {where}"]
    lines += [f"  {r.get('name')!r} · level {r['level']}" for r in own]
    lines.append(f"{len(own)} product-test legs declared")
    found = []
    if value == "none":
        found += [f"row {r.get('name')!r} carries level {r['level']!r}, and {PRODUCT_KEY} = none admits "
                  f"no product-test row" for r in own]
    else:
        found += [f"row {r.get('name')!r} carries level {r['level']!r}, outside {', '.join(levels)}"
                  for r in own if r["level"] not in levels]
    if value == "declared" and not own:
        found += [f"runner {n!r} declares level(s) {', '.join(lv)}, and no row carries a level"
                  for n, lv in detected.items() if lv]
    if value == WITH_RUNNERS:
        have = {(r.get("name"), r.get("level")) for r in own}
        for a in derive_product_rows(repo, value, runners, [], detected):
            if (a["name"], a["level"]) not in have:
                found.append(f"runner row {a['name']!r} (level {a['level']}) is missing from the "
                             f"manifest: render it with the leg factory")
    return lines, found


def run_check(repo):
    lines, found = check_product_rows(repo, derive_manifest_path(), derive_tool_rel(repo))
    lines += [f"{SAY}: red · {f}" for f in found]
    lines.append(f"{SAY}: {'red' if found else 'green'}")
    return (1 if found else 0), lines


# ------------------------------------------------------------------------------------------- fixture
MARKERS = '[tool.pytest.ini_options]\nmarkers = ["unit: fast tests"]\n'
# (case, label, tests.product, the level planted on the fixture's own leg or None, a pytest table,
#  the colour `check` must read, whether the render must hold the adapter row `leg.pytest.unit`)
CASES = (
    ("none-with-level", "none-with-level", "none", "unit", False, "red", False),
    ("none-with-level", "none-with-level, level removed", "none", None, False, "green", False),
    ("declared", "declared", "declared", None, True, "red", False),
    ("declared", "declared, level unit declared", "declared", "unit", True, "green", False),
    ("declared", "declared, level smoke declared", "declared", "smoke", True, "red", False),
    ("declared-with-runners", "declared-with-runners", WITH_RUNNERS, None, True, "green", True),
    ("declared-with-runners", "declared-with-runners, pytest table removed", WITH_RUNNERS, None, False,
     "green", False),
)


def run_git(top, *args):
    """git in the planted repository, signing off, its environment free of GIT_* knobs."""
    p = subprocess.run(["git", "-c", "commit.gpgsign=false", "-c", "user.name=fixture",
                        "-c", "user.email=fixture@invalid", *args], cwd=str(top), env=derive_git_env(),
                       capture_output=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL,
                       timeout=BOUND)
    if p.returncode != 0:
        raise Refusal(f"git {' '.join(args)} failed in the fixture: {p.stderr.strip()}")


def write_fixture_repo(top, value, level, pytest_table):
    """The leg factory's own fixture tree at `top`, plus the guardrails kit's adapter row and script,
    its policy and pytest table, committed on `main` so the policy reader reads it."""
    import leg_factory  # noqa: PLC0415 - its fixture and its renderer, gov's alone
    leg_factory.write_fixture(top)
    guard = resolve_kit_dir("pytest-parallel-guardrails", "run_level.py", HERE)
    real = tomllib.loads((guard / "kit.toml").read_text(encoding="utf-8"))
    kit = pathlib.Path(top, "kits", guard.name)
    kit.mkdir(parents=True)
    text = f'id = "{guard.name}"\nhome = "{guard.name}"\n'
    for r in real.get("test_runner") or []:
        text += "\n[[test_runner]]\n" + "".join(f"{k} = {leg_factory.render_toml_value(v)}\n" for k, v in r.items())
    (kit / "kit.toml").write_bytes(text.encode("utf-8"))
    shutil.copyfile(guard / "run_level.py", kit / "run_level.py")
    reg = pathlib.Path(top, "kits", leg_factory.GOVKIT_HOME, "registry.toml")
    reg.write_bytes(reg.read_bytes() + (f'\n[[entry]]\nid = "{guard.name}"\n'
                                        f'descriptor = "{{prefix}}/{guard.name}/kit.toml"\n').encode("utf-8"))
    if level is not None:
        leg_factory.write_planted(top, "kits/alpha/kit.toml", 'subject = "repo"\n',
                                  f'subject = "repo"\nlevel = "{level}"\n')
    pathlib.Path(top, ".governance").mkdir()
    pathlib.Path(top, ".governance", "policy.toml").write_bytes(f'[tests]\nproduct = "{value}"\n'.encode("utf-8"))
    if pytest_table:
        pathlib.Path(top, "pyproject.toml").write_bytes(MARKERS.encode("utf-8"))
    run_git(top, "init", "-q", "-b", "main")
    run_git(top, "add", "-A")
    run_git(top, "commit", "-q", "--no-verify", "-m", "fixture")
    rc, out = leg_factory.run_write(top)
    if rc != 0:
        raise Refusal(f"the leg factory did not render the fixture: {'; '.join(out)}")
    return top / "kits" / "gate-legs.json"


def run_fixture(only):
    """Each planted case of CASES, or those of the case `only`, graded by `check`."""
    picked = [c for c in CASES if only in (None, c[0])]
    if not picked:
        return 2, [f"{SAY}: refused · no fixture case {only!r}: {', '.join(dict.fromkeys(c[0] for c in CASES))}"]
    lines, failed = [], 0
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="pt9-"))
    try:
        for i, (_case, label, value, level, table, want, adapter) in enumerate(picked):
            top = scratch / str(i)
            manifest = write_fixture_repo(top, value, level, table)
            _l, found = check_product_rows(top, manifest, "kits")
            got = "red" if found else "green"
            lines.append(f"case {label}: {got}" + "".join(f"\n    {f}" for f in found))
            held = [r for r in read_manifest_rows(manifest) if r.get("pack") == PACK]
            ok = [r for r in held if r.get("tag") == "leg.pytest.unit" and r.get("level") == "unit"]
            why = []
            if got != want:
                why.append(f"wanted {want}, read {got}")
            if adapter and not ok:
                why.append("the render holds no adapter row leg.pytest.unit at level unit")
            if not adapter and held:
                why.append(f"the render holds adapter row(s) {', '.join(r.get('name', '?') for r in held)}")
            if why:
                failed += 1
                lines.append(f"  FAIL case {label}: {'; '.join(why)}")
    finally:
        remove_tree(scratch)
    lines.append(f"{SAY}: fixture · {len(picked) - failed} of {len(picked)} cases read as planted")
    return (1 if failed else 0), lines


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(prog="product_tests.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    ck = sub.add_parser("check", help="grade the manifest against tests.product")
    ck.add_argument("--fixture", nargs="?", const="", default=None, metavar="case",
                    help="plant each case, or the one named, and grade it")
    a = ap.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if a.fixture is not None:
            init_owned_tempdir()
            rc, lines = run_fixture(a.fixture or None)
        else:
            rc, lines = run_check(regen.derive_repo_root(HERE))
    except (Refusal, regen.Refusal, LookupError) as e:
        rc, lines = 2, [f"{SAY}: refused · {e}"]
    except Exception as e:  # noqa: BLE001 - the leg factory's own Refusal is a refusal here too
        if type(e).__name__ != "Refusal":
            raise
        rc, lines = 2, [f"{SAY}: refused · {e}"]
    for ln in lines:
        print(ln)
    return rc


if __name__ == "__main__":
    sys.exit(main())
