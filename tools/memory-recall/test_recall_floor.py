#!/usr/bin/env python3
"""Arms for check-recall.py — one per row of the spec's degradation table, plus every refusal.

    python test_recall_floor.py        # exit 0 = the floor can still FAIL for the right reason

GOV-ONLY, and that is the point rather than an accident. These arms are keyed on THIS repo's record
ids, so they are meaningless in an adopter's tree; `kit.toml` withholds this file, `check-recall.py`
and `recall-fixture.json` through a non-landable rule. The sibling `selftest.py` is the adopter-run
leg and is deliberately untouched by this unit — an arm naming `TOOL-aWrittenMethod-4` inside a file
that ships and runs as a declared `[[gate_leg]]` would red in every adopting tree.

THE TWO ARMS THAT MATTER are the single-direction ones. A floor and a per-id assertion that always
red together are indistinguishable from one check wearing two names, so the design's whole claim is
that each can fire ALONE:

    floor alone    drop only the DECISIONS.md home of a MULTI-HOMED hitting target
                   -> the id still resolves; the question falls out of the top k
    per-id alone   retire every home of a NON-hitting target
                   -> the id stops resolving; the normalised score RISES

Each arm drives the real program as a subprocess over a filtered `--data-dir`, so what is exercised
is the shipped entry point and not a re-implementation of it.
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
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


# This suite's scratch lands in an owned root, swept if a kill leaves it (TOOL-dQuietDisk-9 S3).
init_owned_tempdir()



def derive_install_prefix() -> str:
    """The install prefix WITH its trailing slash, derived from where this file sits and empty at a
    root install. Every fixture and host path the self-test builds is spelled through it, never
    through a literal prefix (TOOL-aRepatriatedFork-28)."""
    import pathlib
    here = pathlib.Path(__file__).resolve().parent
    for anc in here.parents:
        if (anc / ".git").exists():
            rel = here.parent.relative_to(anc).as_posix()
            return "" if rel == "." else rel + "/"
    raise SystemExit(f"{pathlib.Path(__file__).name}: not inside a git repository, so there is no "
                     "install prefix to derive")


PFX = derive_install_prefix()


sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
CHECK = KIT / "check-recall.py"
FIXTURE = KIT / "recall-fixture.json"
# The repository holding this kit, found by its `.git` entry: the grandparent is the root only at
# a one-segment install prefix (TOOL-aRepatriatedFork-28, gate repair at VERIFYING).
ROOT = next(p for p in KIT.parents if (p / ".git").exists())

# BEFORE the deferred sibling import below, not after it. Written after, the insert is a no-op and
# the import resolves only because CPython seeds sys.path[0] with the script's directory -- the exact
# accident it was written not to depend on. Under `python -P` that seeding is off and 15 of 16 arms
# died on ModuleNotFoundError while the file looked correct.
sys.path.insert(0, str(KIT))

# Every scratch dir this file creates, so main() can remove them. Each is a full copy of the
# extracted corpus (~8 MB); with 15 call sites and GATE_FULL=1 on every push, leaking them grew to
# ~2 GB on one node before a review measured it. `check-recall.py` removes its own in a `finally`,
# which is the asymmetry that made this an omission rather than a convention.
_SCRATCH: list[pathlib.Path] = []

_checks: list[tuple[str, str, str]] = []


def check(name):
    def arm(fn):
        try:
            _checks.append(("ok", name, fn() or ""))
        except AssertionError as exc:
            _checks.append(("FAIL", name, str(exc)))
        except Exception as exc:  # noqa: BLE001 — a crash is a failure, not a stack trace
            _checks.append(("FAIL", name, f"{type(exc).__name__}: {exc}"))
        return fn

    return arm


# ------------------------------------------------------------------ harness

_BASE: pathlib.Path | None = None


def build_base_dir() -> pathlib.Path:
    """Extract this repo's corpus ONCE. Every arm filters a copy of it.

    Extraction is ~0.4 s and there are a dozen arms; doing it per arm would put the whole leg's cost
    into a step none of them is testing.
    """
    global _BASE
    if _BASE is None:
        out = pathlib.Path(tempfile.mkdtemp(prefix="recallarm-base-"))
        import query  # noqa: PLC0415 — imported here so a missing sibling fails as an arm, not at load

        proc = subprocess.run(
            [sys.executable, str(KIT / "extract.py"), str(ROOT), str(out),
             "--chunk-max", str(query.CHUNK_MAX)],
            capture_output=True, text=True, cwd=str(ROOT),
        )
        assert proc.returncode == 0, f"extract failed: {proc.stderr[-400:]}"
        _BASE = out
    return _BASE


def build_filtered(drop=None) -> pathlib.Path:
    """A copy of the base data dir with `records.jsonl` rows removed by a predicate."""
    src = build_base_dir()
    dst = pathlib.Path(tempfile.mkdtemp(prefix="recallarm-"))
    _SCRATCH.append(dst)
    for name in ("spine", "records", "chunks"):
        rows = [ln for ln in (src / f"{name}.jsonl").read_text(encoding="utf-8").splitlines() if ln.strip()]
        if name == "records" and drop is not None:
            rows = [ln for ln in rows if not drop(json.loads(ln))]
        (dst / f"{name}.jsonl").write_text("\n".join(rows) + ("\n" if rows else ""),
                                           encoding="utf-8", newline="\n")
    shutil.copy(src / "anchors.json", dst / "anchors.json")
    return dst


# The single-pair head. The repo's own pin is `served`, which builds its own sets and ignores a
# filtered extract dir, so every arm that grades a `--data-dir` names this head explicitly -- which
# is also what keeps the older grammar exercised now that no conf in this repo carries it.
SINGLE = 'RECALL_FLOOR="records:fts5:r@5>=0.81"'


def run_check(*args, conf_floor: str | None = None, fixture: pathlib.Path | None = None):
    """Drive the shipped program. `conf_floor` swaps the pin by pointing --repo at a stub repo."""
    argv = [sys.executable, str(CHECK), *args]
    if fixture is not None:
        argv += ["--fixture", str(fixture)]
    repo = ROOT
    tmp = None
    if conf_floor is not None:
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallconf-"))
        (tmp / ".memory-tree.conf").write_text(
            'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\n' + conf_floor,
            encoding="utf-8", newline="\n")
        repo = tmp
    argv += ["--repo", str(repo)]
    try:
        return subprocess.run(argv, capture_output=True, text=True, cwd=str(ROOT))
    finally:
        if tmp is not None:
            remove_tree(tmp)


def read_lines(proc) -> str:
    return proc.stdout + proc.stderr


# ------------------------------------------------------------------ the baseline


@check("baseline is green and prints both verdicts")
def test_baseline_green():
    d = build_filtered()
    p = run_check("--data-dir", str(d), conf_floor=SINGLE)
    out = read_lines(p)
    assert p.returncode == 0, f"expected 0, got {p.returncode}\n{out}"
    assert "per-id ok" in out, out
    assert "RECALL_FLOOR ok" in out, out
    return "per-id ok + RECALL_FLOOR ok, exit 0"


# ------------------------------------------------------------------ the two single-direction arms


# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if os.environ.get("FOREIGN_PREFIX_PROBE") == "1":
    print("foreign-prefix-probe: stopped after 1 arm")
    print("FAIL (1 assertions)" if (any(c[0] == "FAIL" for c in _checks)) else "PASS (1 assertions)")
    sys.exit(1 if (any(c[0] == "FAIL" for c in _checks)) else 0)
@check("the FLOOR reds alone (per-id stays green)")
def test_floor_reds_alone():
    # TOOL-aWrittenMethod-4 has three homes; removing only the DECISIONS.md one leaves the id
    # resolvable through the archive and build-README rows while the question falls out of the top 5.
    d = build_filtered(lambda r: r.get("id") == "TOOL-aWrittenMethod-4"
                       and r["path"] == "memory/DECISIONS.md")
    p = run_check("--data-dir", str(d), conf_floor=SINGLE)
    out = read_lines(p)
    assert p.returncode != 0, f"expected a red\n{out}"
    assert "per-id ok" in out, f"per-id should stay GREEN\n{out}"
    assert "RECALL_FLOOR RED" in out, f"floor should red\n{out}"
    assert "0.7500" in out, f"expected normalised 0.7500\n{out}"
    return "floor RED at 0.7500, per-id ok — the directions are independent"


@check("PER-ID reds alone (the floor stays green and RISES)")
def test_per_id_reds_alone():
    # TOOL-aMouldedFolio-1 is single-homed and does NOT hit today, so retiring it drops R without
    # dropping h: the normalised score goes UP while the id stops resolving.
    d = build_filtered(lambda r: r.get("id") == "TOOL-aMouldedFolio-1")
    p = run_check("--data-dir", str(d), conf_floor=SINGLE)
    out = read_lines(p)
    assert p.returncode != 0, f"expected a red\n{out}"
    assert "per-id RED" in out and "TOOL-aMouldedFolio-1" in out, f"per-id should name the id\n{out}"
    assert "RECALL_FLOOR ok" in out, f"floor should stay GREEN\n{out}"
    assert "0.9091" in out, f"expected normalised 0.9091\n{out}"
    return "per-id RED naming the id, floor ok at 0.9091 — it rose"


@check("one retirement of a HITTING target is free by construction")
def test_one_retirement_is_free():
    d = build_filtered(lambda r: r.get("id") == "TOOL-aStandingWrit-2")
    p = run_check("--data-dir", str(d), conf_floor=SINGLE)
    out = read_lines(p)
    assert "RECALL_FLOOR ok" in out, f"the derived pin must absorb one retirement\n{out}"
    assert "0.8182" in out, f"expected the (h-1)/(R-1) worst case 0.8182\n{out}"
    assert "per-id RED" in out, out
    return "normalised 0.8182 >= 0.81, floor ok — the headroom the pin is derived from"


@check("dropping the whole record file reds BOTH (the plumbing arm)")
def test_both_red_on_wholesale_drop():
    d = build_filtered(lambda r: r["path"] == "memory/DECISIONS.md")
    p = run_check("--data-dir", str(d), conf_floor=SINGLE)
    out = read_lines(p)
    assert p.returncode != 0, out
    assert "per-id RED" in out and "RECALL_FLOOR RED" in out, f"both should red\n{out}"
    # DIRECTION plus a magnitude BOUND, not a literal. This arm claims only that the score RESPONDS
    # to the corpus, and the corpus moves: a merge from origin/main took this cell 0.2000 -> 0.1000
    # with the behaviour identical. The three single-direction arms keep their literals, because
    # those encode the h/R arithmetic the pin is DERIVED from and `--audit-fixture` reds if h or R
    # moves — here there is no derivation to protect, so a literal is over-specification that reds
    # on an unrelated commit.
    m = re.search(r"normalised ([0-9.]+) <", out)
    assert m, f"expected a normalised figure in the floor's red line\n{out}"
    norm = float(m.group(1))
    assert norm < 0.5, f"a wholesale drop must fall far below the pin, got {norm}\n{out}"
    return f"both RED at {norm:.4f} — the score responds to the corpus, which is all this arm claims"


# ------------------------------------------------------------------ the refusals


@check("an ABSENT fixture reds by name and does not skip")
def test_absent_fixture_reds():
    missing = pathlib.Path(tempfile.gettempdir()) / "no-such-recall-fixture.json"
    p = run_check("--data-dir", str(build_filtered()), fixture=missing,
                  conf_floor=SINGLE)
    out = read_lines(p)
    assert p.returncode == 2, f"expected refusal 2, got {p.returncode}\n{out}"
    assert "fixture absent" in out and missing.name in out, out
    return "REFUSED naming the path"


@check("an EMPTY fixture reds at the precondition, never downstream")
def test_empty_fixture_reds():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
    fx = tmp / "empty.json"
    fx.write_text('{"queries": []}', encoding="utf-8", newline="\n")
    try:
        p = run_check("--data-dir", str(build_filtered()), fixture=fx, conf_floor=SINGLE)
        out = read_lines(p)
        assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
        assert "carries no queries" in out, out
        return "REFUSED — a question set with no questions cannot grade anything"
    finally:
        remove_tree(tmp)


@check("an ALL-MISS fixture reds on per-id and reports the floor as not evaluated")
def test_all_miss_fixture():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
    fx = tmp / "allmiss.json"
    fx.write_text(json.dumps({"queries": [
        {"query": "what colour is the boojum", "expected_ids": ["TOOL-zNoSuchThing-9"]},
    ]}), encoding="utf-8", newline="\n")
    try:
        p = run_check("--data-dir", str(build_filtered()), fixture=fx, conf_floor=SINGLE)
        out = read_lines(p)
        assert p.returncode == 1, f"expected 1, got {p.returncode}\n{out}"
        assert "per-id RED" in out, out
        assert "not evaluated" in out, f"the floor must say so, never divide 0/0\n{out}"
        return "per-id RED, floor `not evaluated` — no 0/0"
    finally:
        remove_tree(tmp)


@check("an EMPTY graded set refuses (the branch that replaced one that could not fail)")
def test_empty_graded_set_refuses():
    # The set is emptied SYNTHETICALLY, by dropping every records row. This arm used to pin a floor
    # over `spine` and lean on that set extracting to zero docs in this repo -- which was a live
    # DEFECT in `DURABLE`, not a property, so the arm passed BECAUSE of a bug and went red the
    # moment the bug was fixed. A test whose green depends on a defect elsewhere is not a test of
    # the branch it names; emptying a set on purpose exercises the same `is EMPTY` refusal and
    # cannot be un-armed by repairing something else.
    p = run_check("--data-dir", str(build_filtered(drop=lambda r: True)),
                  conf_floor='RECALL_FLOOR="records:fts5:r@5>=0.81"')
    out = read_lines(p)
    assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
    assert "is EMPTY" in out and "records" in out, out
    return "REFUSED — a synthetically emptied set grades nothing, and the floor says so"


@check("an ABSENT pin reds naming the key, with no default")
def test_absent_pin_reds():
    p = run_check("--data-dir", str(build_filtered()), conf_floor="")
    out = read_lines(p)
    assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
    assert "RECALL_FLOOR is not declared" in out, out
    return "REFUSED naming RECALL_FLOOR"


@check("a MALFORMED pin reds naming the key")
def test_malformed_pin_reds():
    p = run_check("--data-dir", str(build_filtered()), conf_floor='RECALL_FLOOR="0.81"')
    out = read_lines(p)
    assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
    assert "does not parse" in out, out
    return "REFUSED — a bare scalar names no cell"


@check("an OUT-OF-VOCABULARY pin reds at the pin, not inside bench.load")
def test_out_of_vocabulary_pin_reds():
    p = run_check("--data-dir", str(build_filtered()),
                  conf_floor='RECALL_FLOOR="record:fts5:r@5>=0.81"')
    out = read_lines(p)
    assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
    assert "names set 'record'" in out, f"a one-character typo must red HERE\n{out}"
    assert "Traceback" not in out, f"it must not raise\n{out}"
    return "REFUSED naming the key — no FileNotFoundError"


# ------------------------------------------------------------------ the anti-tautology arms


@check("--audit-fixture is green on the served pin, h and R not below the conf's record")
def test_audit_green():
    """The served audit over the real conf, measured h and R not below what the conf comment records.

    It replaced an arm asserting a literal `h` and `R`. What a not-below arm STOPS seeing is a pin
    left merely conservative after a fixture edit that RAISED h and R: the worst case rose, the pin
    did not follow, and nothing reds. A drop below the recorded figures still reds here, and a pin
    above the worst case reds in the audit itself.
    """
    conf = (ROOT / ".memory-tree.conf").read_text(encoding="utf-8")
    rec = re.search(r"all rows h=(\d+) R=(\d+)", conf)
    assert rec, "the conf comment above RECALL_FLOOR records no `all rows h=<n> R=<n>`"
    p = run_check("--audit-fixture")
    out = read_lines(p)
    assert p.returncode == 0, f"expected 0\n{out}"
    for name in ("terms", "naive_terms"):
        assert f"slice {name}: h=" in out, f"the audit must print slice {name}\n{out}"
    got = re.search(r"derivation: h=(\d+) R=(\d+)", out)
    assert got, f"the pin's own derivation must print\n{out}"
    h, R = int(got[1]), int(got[2])
    assert h >= int(rec[1]) and R >= int(rec[2]), (
        f"measured h={h} R={R} is below the conf's recorded h={rec[1]} R={rec[2]}\n{out}")
    return f"h={h} R={R}, not below the recorded h={rec[1]} R={rec[2]}"


@check("a TAUTOLOGICAL fixture reds the overlap audit")
def test_tautological_fixture_reds():
    # The exact fixture round-2 built to defeat the prose version of this property: each question IS
    # its target record's own text. It scores a perfect r@5 and proves nothing.
    base = build_base_dir()
    recs = {}
    for ln in (base / "records.jsonl").read_text(encoding="utf-8").splitlines():
        if ln.strip():
            r = json.loads(ln)
            if "id" in r:
                recs.setdefault(r["id"], r)
    picks = ["TOOL-aStandingWrit-2", "TOOL-cSteadyMetronome-1", "TOOL-aWidenedGuide-1"]
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
    fx = tmp / "tautology.json"
    fx.write_text(json.dumps({"queries": [
        {"query": recs[i]["text"], "expected_ids": [i], "from": "copied from the record"}
        for i in picks
    ]}), encoding="utf-8", newline="\n")
    try:
        p = run_check("--audit-fixture", "--data-dir", str(build_filtered()), fixture=fx,
                      conf_floor=SINGLE)
        out = read_lines(p)
        assert p.returncode == 1, f"expected the audit to RED, got {p.returncode}\n{out}"
        assert "AUDIT RED" in out and "OVERLAP_MAX" in out, out
        return "copied text overlaps ~1.0 and reds — the property is a gate, not a sentence"
    finally:
        remove_tree(tmp)


@check("a fixture whose declared `hits` disagrees with the measurement reds")
def test_hits_disagreement_reds():
    blob = json.loads(FIXTURE.read_text(encoding="utf-8"))
    flipped = False
    for q in blob["queries"]:
        if q.get("hits", {}).get("naive_terms") is False:
            q["hits"]["naive_terms"] = True          # claim a miss is a hit
            flipped = True
            break
    assert flipped, "the fixture declares no naive_terms miss, so there is nothing to lie about"
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
    fx = tmp / "lying-hits.json"
    fx.write_text(json.dumps(blob), encoding="utf-8", newline="\n")
    try:
        p = run_check("--audit-fixture", fixture=fx)
        out = read_lines(p)
        assert p.returncode == 1, f"expected a red\n{out}"
        assert "declares hits=True and measures False in slice naive_terms" in out, out
        return "the hand-kept column is documentation a gate keeps honest, per slice"
    finally:
        remove_tree(tmp)


@check("a served fixture missing a term list, or one outside TERM_BAND, REFUSES naming the question")
def test_served_term_lists_refuse():
    import query  # noqa: PLC0415

    lo = query.TERM_BAND[0]
    seen = []
    for label, edit in (("no naive_terms", lambda q: q.pop("naive_terms")),
                        ("short terms", lambda q: q.__setitem__("terms", q["terms"][:lo - 1]))):
        blob = json.loads(FIXTURE.read_text(encoding="utf-8"))
        edit(blob["queries"][3])
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
        _SCRATCH.append(tmp)
        fx = tmp / "terms.json"
        fx.write_text(json.dumps(blob), encoding="utf-8", newline="\n")
        p = run_check(fixture=fx)
        out = read_lines(p)
        assert p.returncode == 2, f"{label}: expected refusal 2, got {p.returncode}\n{out}"
        assert "REFUSED" in out and "question 4" in out, f"{label}: must name the question\n{out}"
        seen.append(label)
    return "REFUSED, naming question 4: " + ", ".join(seen)


@check("the kit payload WITHHOLDS all three gov-only files")
def test_kit_payload_withholds():
    """Asserted against the PAYLOAD, never against `selfcheck`'s exit code.

    govkit has no `exclude` key. A rule carrying one parses as TOML, passes `selfcheck` — which has
    no unknown-key arm — and ships the file anyway, which is how the first attempt at this was a
    silent no-op. The only honest observation is the resolved pool itself.
    """
    import tomllib  # noqa: PLC0415

    import extract as E  # noqa: PLC0415 — the kit's own copy of the sibling-kit resolver

    sys.path.insert(0, str(E.resolve_kit_dir("govkit", "govkit.py", KIT)))
    import govkit as G  # noqa: PLC0415

    desc = tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8"))
    home = f"{PFX}memory-recall"
    ctx = {"kit": home, "relpath": "", "memory_root": "memory"}
    wild = [r for r in desc["files"] if r.get("include") == "**"][0]
    pool = {pathlib.PurePosixPath(p).name for p in G.resolve_rule_pool(ROOT, desc, wild, ctx, home)}
    leaked = {"recall-fixture.json", "check-recall.py", "test_recall_floor.py"} & pool
    assert not leaked, f"these ship to every adopter: {sorted(leaked)}"
    # ANCHORED, not deleted. selftest.py was withheld by the 2026-08-23 ruling, so asserting
    # it ships is permanently red; but an arm that only checks for ABSENCE passes just as
    # well on a pool that resolved empty, which is the shape this whole file exists against.
    assert "adopt-memory-recall.sh" in pool, (
        "the ** pool resolved without the adopter -- it is empty or misresolved, and the\n"
        "absence assertions above would then prove nothing")
    return f"3 withheld, adopter still shipped ({len(pool)} files in the ** pool)"


@check("the overlap audit reds NOT MEASURED on an unresolvable target, never a passing 0.000")
def test_audit_reds_on_unresolved_target():
    """The liveness half of the anti-tautology guard.

    An earlier cut re-implemented target resolution records-only, so a question the run could not
    resolve scored `overlap 0.000` — the most independent row in the table, and a PASS. This arm is
    the one that would have caught it.
    """
    d = build_filtered(lambda r: r.get("id") == "TOOL-aMouldedFolio-1")
    p = run_check("--audit-fixture", "--data-dir", str(d), conf_floor=SINGLE)
    out = read_lines(p)
    assert p.returncode == 1, f"expected a red\n{out}"
    assert "NOT MEAS" in out, f"the row must report NOT MEASURED\n{out}"
    assert "DEAD PROBE" in out, f"and red as one\n{out}"
    assert "over 11/12 measured" in out, f"an unmeasured row must leave the summary\n{out}"
    return "row 10 NOT MEASURED, red, and excluded from max/mean"


@check("the overlap audit MEASURES a chunks pin instead of reading 0.000 across the board")
def test_audit_measures_chunk_targets():
    """Chunk docs carry no `id`, so a records-only resolver read 0.000 on EVERY row and passed.

    Reusing the run's own targets resolves chunks through the anchor map exactly as the scorer does,
    so the guard is live for a whole second in-vocabulary set rather than vacuous for it.
    """
    p = run_check("--audit-fixture", "--data-dir", str(build_filtered()),
                  conf_floor='RECALL_FLOOR="chunks:fts5:r@5>=0.05"')
    out = read_lines(p)
    assert "over 12/12 measured" in out, f"every chunk target must resolve\n{out}"
    assert "max 0.000" not in out, f"a whole-set 0.000 is the vacuous reading\n{out}"
    return "12/12 measured under a chunks pin — the guard is live for both sets"


@check("a failed extraction REFUSES with exit 2, not a traceback at exit 1")
def test_extract_failure_refuses():
    """The one branch no other arm reaches: every other arm passes --data-dir, but the bar's leg
    does not, so this was the gate's own path and the untested one."""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallnorepo-"))
    (tmp / ".memory-tree.conf").write_text(
        'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\nRECALL_FLOOR="records:fts5:r@5>=0.81"\n',
        encoding="utf-8", newline="\n")
    try:
        p = subprocess.run([sys.executable, str(CHECK), "--repo", str(tmp)],
                           capture_output=True, text=True, cwd=str(ROOT))
        out = read_lines(p)
        assert p.returncode == 2, f"expected refusal 2, got {p.returncode}\n{out}"
        assert "REFUSED" in out, out
        assert "Traceback" not in out, f"a refusal must not surface as a stack trace\n{out}"
        return "exit 2 and REFUSED — not exit 1, which reads as a floor regression"
    finally:
        remove_tree(tmp)


#: Run INSIDE the scratch repository `build_served_fixture` makes, against its own copy of the kit,
#: so `recall_conf` binds that repository's conf. It prints the paths of the served set `check-recall`
#: grades (`load_served_index`, `untracked=False`) and of the set the CLI serves (`untracked=True`).
_SERVED_PROBE = r"""
import importlib.util, json, pathlib, sys
sys.path.insert(0, %(kit)r)
import query
spec = importlib.util.spec_from_file_location("check_recall", pathlib.Path(%(kit)r) / "check-recall.py")
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)
root = pathlib.Path(%(root)r)
con = cr.load_served_index(root)
graded = sorted(p for (p,) in con.execute("SELECT path FROM recall_view"))
con.close()
served = query.load_served_set(root, untracked=True)
served["con"].close()
print(json.dumps({"graded": graded, "served": sorted(p for p, _b in served["pairs"])}))
"""


def build_served_fixture() -> pathlib.Path:
    """A scratch repository holding this kit, the memory-tree and playbook kits it requires, a
    COMMITTED record file and an UNTRACKED one (TOOL-dTotalRecall-21 AC7): the served set is read from
    the tag index's HEAD tree, so the seed is committed, and the untracked file is what a grading
    served set must leave out."""
    import extract as E  # noqa: PLC0415 — the kit's own copy of the sibling-kit resolver

    root = pathlib.Path(tempfile.mkdtemp(prefix="recallserved-")).resolve()
    _SCRATCH.append(root)
    for src in (KIT, E.resolve_kit_dir("memory-tree", "tree_lib.py", KIT),
                E.resolve_kit_dir("playbook", "tag_index.py", KIT)):
        (root / src.name).mkdir()
        for f in sorted(src.iterdir()):
            if f.is_file() and f.suffix in (".py", ".toml", ".txt", ".json"):
                shutil.copyfile(f, root / src.name / f.name)
    (root / ".memory-tree.conf").write_text('MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\n',
                                            encoding="utf-8", newline="\n")
    disc = root / "memory" / "tooling"
    disc.mkdir(parents=True)
    (disc / "DECISIONS.md").write_text("# Tooling decisions\n\n- TOOL-aFoo-1 · the frobnicator leaks less\n",
                                       encoding="utf-8", newline="\n")
    git = ["git", "-C", str(root), "-c", "user.email=t@t", "-c", "user.name=t", "-c", "core.autocrlf=false"]
    for argv in (["init", "-q"], ["add", "-A"], ["commit", "-q", "--no-verify", "-m", "seed"]):
        subprocess.run([*git, *argv], check=True, capture_output=True)
    (disc / "fresh.md").write_text("# Fresh\n\n## TOOL-aFoo-7 — fresh\n\nthe zorblax quuxly note\n",
                                   encoding="utf-8", newline="\n")
    return root


@check("the served set check-recall grades holds tracked files only, where the CLI's holds untracked too")
def test_served_set_leaves_untracked_out():
    """AC7's corpus half, over the index's served set. `check-recall` grades
    `query.load_served_set(root, untracked=False)`; a served set that read untracked files there
    would grade a session's unrecorded notes, so a row's hit would move with the worktree's state.
    The CLI's own set, `untracked=True`, holding the same file is the liveness half: without it an
    untracked file the corpus walk never lists would pass this arm by being absent from both."""
    root = build_served_fixture()
    kit = root / KIT.name
    p = subprocess.run([sys.executable, "-c", _SERVED_PROBE % {"kit": str(kit), "root": str(root)}],
                       capture_output=True, text=True, encoding="utf-8", cwd=str(root))
    assert p.returncode == 0, f"the served-set probe failed:\n{p.stdout}{p.stderr[-900:]}"
    got = json.loads(p.stdout.strip().splitlines()[-1])
    fresh = "memory/tooling/fresh.md"
    assert fresh in got["served"], f"LIVENESS: the CLI's served set does not hold the untracked file: {got}"
    assert "memory/tooling/DECISIONS.md" in got["graded"], f"the graded set lost the tracked file: {got}"
    assert fresh not in got["graded"], f"check-recall grades an untracked file: {got}"
    return f"graded {len(got['graded'])} path(s), served {len(got['served'])}; the untracked one only served"


@check("the floor ranks through record_find's one fusion, and no copy of it is left in this kit")
def test_floor_runs_record_find_fusion():
    """TOOL-dTotalRecall-9 S4: the served floor grades `record_find.run_fusion`, the fusion `record find`
    runs, never a copy beside it. Read from the sources, so a second fusion definition left in `query.py`
    reds here even when the two copies rank alike today; and `query.run_fusion` IS the finder's, so the
    CLI's own ranking is the graded one."""
    sys.path.insert(0, str(KIT))
    import query  # noqa: PLC0415
    import record_find  # noqa: PLC0415  memory-tree's, on the path `extract` put that kit on
    copies = [f.name for f in sorted(KIT.glob("*.py"))
              if re.search(r"^def (run_fusion|query_expr)\(", f.read_text(encoding="utf-8"), re.M)]
    assert not copies, f"a fusion copy is defined in this kit beside record_find.py's: {copies}"
    assert query.run_fusion is record_find.run_fusion, "query.run_fusion is not record_find.run_fusion"
    src = CHECK.read_text(encoding="utf-8")
    for name in ("record_find.query_expr(", "record_find.run_fusion("):
        assert name in src, f"check-recall.py does not grade through {name[:-1]}"
    return f"one fusion, in {pathlib.Path(record_find.__file__).name}; check-recall grades it"


@check("a question with no `query` REFUSES by index, not KeyError three branches later")
def test_malformed_question_refuses():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
    fx = tmp / "malformed.json"
    fx.write_text(json.dumps({"queries": [
        {"query": "a real one", "expected_ids": ["TOOL-aStandingWrit-2"]},
        {"expected_ids": ["TOOL-aStandingWrit-2"]},
    ]}), encoding="utf-8", newline="\n")
    try:
        p = run_check("--data-dir", str(build_filtered()), fixture=fx, conf_floor=SINGLE)
        out = read_lines(p)
        assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
        assert "question 2 carries no" in out, out
        assert "KeyError" not in out, f"the container check must reach the elements\n{out}"
        return "REFUSED naming the 1-based index"
    finally:
        remove_tree(tmp)



# ---------------------------------------------------------------- seed stability (TOOL-dTracedLattice-7)

#: The fixture is built so the EXPANSION CHOICE is observable. `RM3_DOCS` seed docs carry the query
#: terms plus 24 candidate words at IDENTICAL document frequency, so `Counter.most_common` is
#: deciding a 24-way tie and nothing but its tie-break separates them. One target doc per candidate
#: makes the chosen terms visible in the retrieved ids. Without that construction the arm passes on
#: any implementation, because a corpus with no tie has nothing for a tie-break to get wrong.
_RM3_PROBE = r"""
import json, sqlite3, sys
sys.path.insert(0, %(kit)r)
import bench
WORDS = [f"cand{i:02d}alpha" for i in range(24)]
docs = [{"id": f"seed-{i}", "path": f"seed{i}.md",
         "text": "reinvention backlog worktree " + " ".join(WORDS)} for i in range(3)]
docs += [{"id": f"target-{w}", "path": f"{w}.md", "text": f"{w} filler filler filler"} for w in WORDS]
db = bench.build_fts_rows(sqlite3.connect(":memory:"), "d", docs)
print(json.dumps([docs[i]["id"] for i in bench.run_rm3(db, docs, "reinvention backlog worktree", 12)]))
"""


@check("rm3 is seed-stable (S3 / AC1)")
def test_rm3_is_seed_stable():
    """The same query under several `PYTHONHASHSEED` values returns identical rankings.

    A SUBPROCESS per seed, because the interpreter reads that variable at start-up and no in-process
    fixture can vary it. Five seeds rather than the three the criterion asks for: the pre-fix
    implementation agreed with itself across some pairs by luck, and a two-seed arm can be green on a
    broken build.
    """
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="rm3seed-"))
    _SCRATCH.append(tmp)
    probe = tmp / "probe.py"
    probe.write_text(_RM3_PROBE % {"kit": str(KIT)}, encoding="utf-8")
    seeds = ("0", "1", "7", "42", "1234")
    seen: dict[str, list[str]] = {}
    for seed in seeds:
        env = dict(os.environ, PYTHONHASHSEED=seed)
        proc = subprocess.run([sys.executable, str(probe)], capture_output=True, text=True, env=env)
        assert proc.returncode == 0, f"probe failed under PYTHONHASHSEED={seed}\n{proc.stderr}"
        seen[seed] = json.loads(proc.stdout.strip().splitlines()[-1])
    # LIVENESS: the fixture must actually exercise expansion, or every seed agrees trivially.
    first = seen[seeds[0]]
    assert any(d.startswith("target-") for d in first), (
        "the probe retrieved no expansion target, so this arm would pass on any implementation")
    distinct = {tuple(v) for v in seen.values()}
    assert len(distinct) == 1, (
        "rm3 returned different rankings under different PYTHONHASHSEED values, so a project pinning "
        f"RECALL_FLOOR to it has a gate whose verdict moves on an unchanged tree: "
        + " | ".join(f"{k}={v[3:6]}" for k, v in seen.items()))
    return f"identical across {len(seeds)} seeds"

# Built by concatenation, so no id-shaped literal names a record this repo does not define.
FOREIGN = "TOOL-" + "aFixtureOther-1"
INSIDE = "TOOL-" + "aFixtureInside-1"


def build_spec_root(section_10: str) -> pathlib.Path:
    """A throwaway git repo holding ONE tracked spec whose section 10 is `section_10`."""
    import extract  # noqa: PLC0415 — the memory root is the conf's, read where the harvester reads it

    root = pathlib.Path(tempfile.mkdtemp(prefix="specprobe-"))
    _SCRATCH.append(root)
    spec = root / extract.CONF.memory_root / "builds" / "xFixtureBuild" / "spec" / "s.md"
    spec.parent.mkdir(parents=True)
    spec.write_text("# fixture\n\n## 3. Design\n\nCites " + FOREIGN + ".\n\n"
                    "## 10. Reuse audit\n\n" + section_10 + "\n", encoding="utf-8", newline="\n")
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(["git", "-C", str(root), "-c", "core.autocrlf=false", "add", "-A"], check=True)
    return root


@check("spec-probes: a root with no section-10 probe prints DEAD PROBE at the harvest")
def test_spec_probes_dead_harvest():
    root = build_spec_root("No recall probe was run here.")
    p = subprocess.run([sys.executable, str(CHECK), "--spec-probes", "--repo", str(root)],
                       capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT))
    out = read_lines(p)
    assert p.returncode == 1, f"exit {p.returncode}, want 1\n{out}"
    assert "DEAD PROBE" in out and "harvest" in out, f"no DEAD PROBE naming the harvest:\n{out}"
    assert "hit@" not in out, f"printed a hit@10 over nothing:\n{out}"
    return "exit 1, DEAD PROBE at the harvest"


@check("spec-probes: a question with an apostrophe across a wrap parses whole")
def test_spec_probes_matched_delimiter():
    import importlib.util  # noqa: PLC0415

    root = build_spec_root('`python query.py "why does the gate refuse a\n'
                           "caller's bound\" --terms \"alpha beta gamma delta epsilon zeta eta\n"
                           'theta"` returned ' + INSIDE + '.')
    spec = importlib.util.spec_from_file_location("check_recall_arm", CHECK)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    specs = mod.read_spec_probes(root)
    # LIVENESS: a harvest that found nothing would make every assertion below vacuous.
    assert len(specs) == 1 and len(specs[0]["probes"]) == 1, f"harvested {specs!r}"
    probe = specs[0]["probes"][0]
    assert probe["question"] == "why does the gate refuse a caller's bound", probe["question"]
    assert len(probe["terms"]) == 8, probe["terms"]
    labels = mod.derive_probe_labels(specs[0])
    assert labels == [FOREIGN], f"labels {labels}"
    return "question whole through the apostrophe; section-10 id excluded"


def main() -> int:
    for state, name, detail in _checks:
        mark = {"ok": "ok  ", "FAIL": "FAIL"}[state]
        print(f"{mark} {name}" + (f" — {detail}" if detail else ""))
    bad = [c for c in _checks if c[0] == "FAIL"]
    print(f"\n{len(_checks) - len(bad)}/{len(_checks)} arms green")
    for d in _SCRATCH:
        # A fixture repo's git objects are read-only, and rmtree cannot unlink those on Windows.
        if (d / ".git").is_dir():
            for f in (d / ".git").rglob("*"):
                if f.is_file():
                    f.chmod(0o666)
        remove_tree(d)
    if _BASE is not None:
        remove_tree(_BASE)
    leaked = [d for d in _SCRATCH if d.exists()]
    if leaked:
        print(f"FAIL scratch cleanup — {len(leaked)} dir(s) survived: {leaked[0]}")
        return 1
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
