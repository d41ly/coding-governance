#!/usr/bin/env python3
"""keep_tails.py — the keep verb: a red run's failing-leg output tails, committed as `leg-tail` records.

    python <this kit>/keep_tails.py --run <run id> --build <slug> --unit <unit id>
    python <this kit>/keep_tails.py --selftest

TOOL-dWitnessedBar-25 S5. Run in the repository whose bar ran. The runner names each failing leg's tail
in its run record's verdict as `tail.<n>` `<hash> <leg name>` and keeps the tail itself, node-locally,
at `<common-dir>/gate-tails/<hash>`. This verb reads `trace.leg-output` through the policy kit's
`policy.py get`, the catalogue default where that reader cannot run, and:
  tail-by-hash  writes one `leg-tail` record per `tail.<n>` of run `<run id>` through the memory-tree
                record factory's `write_record`, into build `<slug>`'s `build/` folder under `<unit id>`:
                fields `Leg`, `Hash`, `Run`, `Sha` (the run header's `head`) and `Cause`, then the tail in
                one fenced block, each span runlog's `scan_secrets` finds replaced by its placeholder. A
                hash a tracked `leg-tail` record already holds, or one written earlier in this call, is
                skipped. Prints `keep-tails: wrote <path> · <hash> <leg>` or `keep-tails: skipped …`
                per tail.
  node-local    writes nothing, printing `keep-tails: trace.leg-output is node-local …`.
A run whose verdict names no tail writes nothing and says so. The factory and runlog's scanner are
found by the sibling-kit resolver and imported.

EXIT 0 every tail written or skipped · 1 a tail not kept: its file is gone, its bytes do not hash to
its name, or `write_record` refused it (a line that would read as a field, or a CR), each named on
stderr with nothing written for it · 2 refused before any write: a malformed argument, no repository,
no verdict for the run, a value outside the catalogue row, or a sibling kit that does not resolve.

`--selftest` plants a scratch repository per case under the system temp directory: a run holding one
tail, kept and then kept again once tracked; the key planted `node-local`; and a tail holding a
secret-shaped line. Exit 0 when every case reads as planted, 1 naming each that does not.

WHAT IT DOES NOT CHECK. That a tail decodes or that its cut lands on a character boundary (an
undecodable byte is replaced), or that a tail line is no fence: unit 51's. Secret shapes runlog's table
does not know. That the run record belongs to this build: the caller names both.
"""
import argparse
import os
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(os.path.abspath(__file__)).parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from leg_factory import resolve_kit_dir  # noqa: E402 - the kit's inline copy of the sibling resolver
import product_tests  # noqa: E402 - the catalogue row, the GIT_*-free environment, the scratch remover
from product_tests import Refusal  # noqa: E402 - exit 2, nothing written

SAY = "keep-tails"
KEY = "trace.leg-output"
KIND = "leg-tail"
KEEP = "tail-by-hash"
RUN_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
HASH = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
TAIL_KEY = re.compile(r"tail\.([0-9]+)")
BOUND = 120  # seconds, each git call


def run_git(top, *args, data=None):
    """git in `top`, its environment free of GIT_* knobs, `data` (bytes) on its stdin -> the completed
    process, its output decoded."""
    p = subprocess.run(["git", *args], cwd=str(top), env=product_tests.derive_git_env(), capture_output=True,
                       input=b"" if data is None else data, timeout=BOUND)
    return subprocess.CompletedProcess(p.args, p.returncode, p.stdout.decode("utf-8", "replace"),
                                       p.stderr.decode("utf-8", "replace"))


def read_git_dirs(cwd):
    """(top, git dir, common dir) of the repository at `cwd`, each absolute."""
    p = run_git(cwd, "rev-parse", "--path-format=absolute", "--show-toplevel", "--git-dir", "--git-common-dir")
    said = [ln for ln in p.stdout.splitlines() if ln.strip()]
    if p.returncode != 0 or len(said) != 3:
        raise Refusal(f"{pathlib.Path(cwd).as_posix()} is in no git repository git can place")
    return tuple(pathlib.Path(s) for s in said)


def load_factory():
    """The memory-tree kit's record factory and its tree library, found by the sibling-kit resolver."""
    try:
        kit = resolve_kit_dir("memory-tree", "build_records.py", HERE)
    except LookupError as e:
        raise Refusal(f"the memory-tree record factory does not resolve, and every record is written "
                      f"through it: {e}") from None
    if str(kit) not in sys.path:
        sys.path.append(str(kit))
    import build_records  # noqa: PLC0415
    import design_lib  # noqa: PLC0415
    import tree_lib  # noqa: PLC0415
    return build_records, design_lib, tree_lib


def load_scanner():
    """runlog's `render_redacted`, the scan the run log applies to committed text."""
    try:
        kit = resolve_kit_dir("runlog", "runlog_lib.py", HERE)
    except LookupError as e:
        raise Refusal(f"runlog's secret scanner does not resolve, and no tail is committed unscanned: {e}") from None
    if str(kit) not in sys.path:
        sys.path.append(str(kit))
    import runlog_lib  # noqa: PLC0415
    return runlog_lib.render_redacted


def read_tail_value(top, tree_lib):
    """(`trace.leg-output` at `top`, where it was read): `policy.py get`, else the catalogue default."""
    _kit, row = product_tests.read_catalogue_row(KEY)
    try:
        value, where = tree_lib.read_policy_value(KEY, top), "policy.py get"
    except (LookupError, ValueError, OSError) as e:
        value, where = row.get("default"), f"the catalogue default · policy.py get did not read it: {e}"
    if value not in (row.get("allowed") or []):
        raise Refusal(f"{KEY} reads {value!r}, outside the catalogue's {row.get('allowed')!r}")
    return value, where


def read_run_tails(git_dir, run):
    """(the verdict's keys, the header's keys, [(n, hash, leg name)] in `n` order) of run `run`."""
    def read_keys(path):
        keys = {}
        for ln in path.read_bytes().decode("utf-8", "replace").splitlines():
            k, sep, v = ln.partition("\t")
            if sep and k not in keys:
                keys[k] = v
        return keys
    d = git_dir / "gate-run" / run
    try:
        verdict = read_keys(d / "verdict")
    except OSError:
        raise Refusal(f"run {run} has no verdict at {(d / 'verdict').as_posix()}, so no tail is named") from None
    try:
        header = read_keys(d / "header")
    except OSError:
        header = {}
    tails = []
    for k, v in verdict.items():
        m = TAIL_KEY.fullmatch(k)
        h, _sp, leg = v.partition(" ")
        if m:
            tails.append((int(m.group(1)), h, leg))
    return verdict, header, sorted(tails)


def read_tracked_tails(top, build_records, design_lib):
    """{hash: path} of every tracked `leg-tail` record, read through the factory's tracked reader."""
    def read_leg_tail(path, text):
        fields, bad, name = build_records.read_record(path, text, KIND)
        return {**fields, "path": path, "build": name.group("build") if name else None,
                "n": int(name.group("n")) if name else None, "malformed": bad}
    try:
        records = build_records.read_records(top, design_lib.read_design_conf(top), KIND, read_leg_tail)
    except design_lib.DesignRefusal as e:
        raise Refusal(f"the tracked {KIND} records do not read: {e}") from None
    return {r["Hash"]: r["path"] for r in records if r.get("Hash")}


def read_blob_hash(top, data):
    """git's blob name of `data` in the repository at `top`, as the runner names a tail: `hash-object
    --stdin`, which hashes the bytes as given. "" where git does not answer."""
    p = run_git(top, "hash-object", "--stdin", data=data)
    return p.stdout.strip() if p.returncode == 0 else ""


def run_keep(cwd, run, build, unit):
    """-> (exit, stdout lines, stderr lines) of one keep over run `run` in the repository at `cwd`."""
    if not RUN_ID.fullmatch(run or ""):
        raise Refusal(f"--run {run!r} is not a run id: [A-Za-z0-9][A-Za-z0-9._-]*")
    top, git_dir, common = read_git_dirs(cwd)
    build_records, design_lib, tree_lib = load_factory()
    value, where = read_tail_value(top, tree_lib)
    if value != KEEP:
        return 0, [f"{SAY}: {KEY} is {value}, so no tail is committed ({where})"], []
    verdict, header, tails = read_run_tails(git_dir, run)
    if not tails:
        return 0, [f"{SAY}: run {run} reads verdict {verdict.get('verdict', '?')} and names no failing "
                   f"leg's tail, so no record is written"], []
    render_redacted = load_scanner()
    held = read_tracked_tails(top, build_records, design_lib)
    out, err, rc = [], [], 0
    for n, h, leg in tails:
        what = f"tail.{n} {h} {leg}"
        if not HASH.fullmatch(h):
            err.append(f"{SAY}: {what} — the hash is not 40 or 64 hex digits, so no record is written")
            rc = 1
            continue
        if h in held:
            out.append(f"{SAY}: skipped {h} {leg} — {held[h]} holds it")
            continue
        src = common / "gate-tails" / h
        try:
            data = src.read_bytes()
        except OSError:
            err.append(f"{SAY}: {what} — no file holds it at {src.as_posix()}, so no record is written")
            rc = 1
            continue
        if read_blob_hash(top, data) != h:
            err.append(f"{SAY}: {what} — {src.as_posix()} does not hash to its name, so no record is written")
            rc = 1
            continue
        text = render_redacted(data.decode("utf-8", "replace"))
        body = text[:-1] if text.endswith("\n") else text
        lines = ["```", *(body.split("\n") if body else []), "```"]
        fields = [("Leg", leg), ("Hash", h), ("Run", run), ("Sha", header.get("head") or "-"),
                  ("Cause", verdict.get("cause") or "-")]
        try:
            rel = build_records.write_record(top, build, unit, KIND, f"{leg} failed in run {run}", fields,
                                             lines=lines)
        except (ValueError, OSError) as e:
            err.append(f"{SAY}: {what} — write_record refused it, so no record is written: {e}")
            rc = 1
            continue
        held[h] = rel
        out.append(f"{SAY}: wrote {rel} · {h} {leg}")
    return rc, out, err


# ------------------------------------------------------------------------------------------ selftest
def write_fixture_repo(top, value, tail):
    """A scratch repository at `top`: `trace.leg-output` = `value` committed on `main`, build `x`, and run
    `fx-1` whose verdict names one tail, `tail` (bytes), kept in the common dir by its hash. -> the hash."""
    def run_git(*args):
        p = run_git(top, "-c", "commit.gpgsign=false", "-c", "user.name=fixture", "-c",
                    "user.email=fixture@invalid", *args)
        if p.returncode != 0:
            raise Refusal(f"git {' '.join(args)} failed in the fixture: {p.stderr.strip()}")
        return p.stdout.strip()
    pathlib.Path(top, ".governance").mkdir(parents=True)
    pathlib.Path(top, ".governance", "policy.toml").write_bytes(f'[trace]\nleg-output = "{value}"\n'.encode())
    pathlib.Path(top, "memory", "builds", "x").mkdir(parents=True)
    pathlib.Path(top, "memory", "builds", "x", "README.md").write_bytes(b"# x\n")
    run_git("init", "-q", "-b", "main")
    run_git("add", "-A")
    run_git("commit", "-q", "--no-verify", "-m", "fixture")
    h = read_blob_hash(top, tail)
    gd = pathlib.Path(top, ".git")
    (gd / "gate-tails").mkdir()
    (gd / "gate-tails" / h).write_bytes(tail)
    run = gd / "gate-run" / "fx-1"
    run.mkdir(parents=True)
    (run / "header").write_bytes(f"run_id\tfx-1\nhead\t{run_git('rev-parse', 'HEAD')}\n".encode())
    (run / "verdict").write_bytes(f"verdict\tRED\nrun_id\tfx-1\ncause\tpush:fixture\ntail.1\t{h} fixture leg\n".encode())
    return h


def run_selftest():
    """Each planted case, graded by what `run_keep` writes and prints."""
    lines, failed = [], 0
    # assembled here, so no committed byte of this kit reads as a secret to runlog's table
    secret = "AKIA" + "Q7" * 8
    cases = (("kept once", KEEP, b"line 1\nFAIL the fixture leg\n"),
             ("node-local", "node-local", b"FAIL the fixture leg\n"),
             ("secret masked", KEEP, f"aws configure set aws_access_key_id {secret}\n".encode()))
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="kt25-"))
    try:
        for i, (label, value, tail) in enumerate(cases):
            top = scratch / str(i)
            top.mkdir()
            why = []
            try:
                h = write_fixture_repo(top, value, tail)
                rc, out, err = run_keep(top, "fx-1", "x", "TOOL-x-1")
                made = sorted(top.glob("memory/builds/x/build/*-leg-tail-*.md"))
                text = made[0].read_bytes().decode("utf-8") if made else ""
                if label == "node-local":
                    if made:
                        why.append(f"node-local wrote {len(made)} record(s)")
                    if not any(f"{KEY} is node-local" in ln for ln in out):
                        why.append(f"no line says {KEY} is node-local: {out + err}")
                elif rc != 0 or len(made) != 1:
                    why.append(f"exit {rc}, {len(made)} record(s) written: {out + err}")
                elif f"- **Hash:** {h}" not in text or "```\n" not in text:
                    why.append("the record holds no Hash field naming the tail's hash, or no fenced block")
                elif label == "kept once":
                    run_git(top, "add", "-A")
                    rc2, out2, err2 = run_keep(top, "fx-1", "x", "TOOL-x-1")
                    again = sorted(top.glob("memory/builds/x/build/*-leg-tail-*.md"))
                    if rc2 != 0 or len(again) != 1 or not any(ln.startswith(f"{SAY}: skipped {h}") for ln in out2):
                        why.append(f"a second keep over a tracked hash wrote {len(again) - 1} record(s) "
                                   f"or did not skip it: {out2 + err2}")
                elif secret in text or "<redacted:aws-key>" not in text:
                    why.append("the record carries the secret, or not its placeholder")
            except Refusal as e:
                why.append(f"refused: {e}")
            lines.append(f"case {label}: {'FAIL — ' + '; '.join(why) if why else 'ok'}")
            failed += bool(why)
    finally:
        product_tests.remove_tree(scratch)
    lines.append(f"{SAY}: selftest · {len(cases) - failed} of {len(cases)} cases read as planted")
    return (1 if failed else 0), lines, []


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace", newline="\n")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(prog="keep_tails.py", description=__doc__.split("\n")[0])
    ap.add_argument("--run")
    ap.add_argument("--build")
    ap.add_argument("--unit")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if a.selftest:
            rc, out, err = run_selftest()
        elif not (a.run and a.build and a.unit):
            raise Refusal("--run, --build and --unit are each required")
        else:
            rc, out, err = run_keep(pathlib.Path.cwd(), a.run, a.build, a.unit)
    except Refusal as e:
        rc, out, err = 2, [], [f"{SAY}: refused · {e}"]
    for ln in out:
        print(ln)
    for ln in err:
        print(ln, file=sys.stderr)
    return rc


if __name__ == "__main__":
    sys.exit(main())
