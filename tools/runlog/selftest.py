#!/usr/bin/env python3
"""selftest.py — the runlog kit's arms. gov:kit runlog@1.0

    python <this kit>/selftest.py

Every arm reads a FIXTURE or a scratch tree it builds, never this repository's journal: the real one
is machine-local, differs per node, and a green over it would say something about this machine and
nothing about the reader. Scratch git trees are made under the system temp dir with every `GIT_*`
variable scrubbed, so an arm run from inside a hook cannot reach the tree that hook is guarding.

Refusals are graded with their NEAR MISSES beside them: a predicate that refused everything would
pass every refusal arm, and only the accepted neighbour tells the two apart.

Exit 0 = every arm passed and the assertion count met its floor · 1 = an arm failed or the count fell.
"""
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"
CLI = HERE / "runlog.py"
sys.path.insert(0, str(HERE))

import runlog_lib as rl  # noqa: E402

# The count this suite executed when it landed. A block of arms stranded behind an early return
# would still print "0 failed"; the floor is what makes that a red rather than a smaller green.
ASSERTION_FLOOR = 183

PASS = []
FAIL = []
SCRATCH = []

# A hook runs this suite with GIT_DIR and GIT_INDEX_FILE pointing at the tree it guards. Every git
# call below — the kit's own included — must see the SCRATCH tree instead, so the variables go.
for _k in [k for k in os.environ if k.startswith("GIT_")]:
    del os.environ[_k]


def check(name, got, want):
    if got == want:
        PASS.append(name)
        print("  ok   %s" % name)
    else:
        FAIL.append(name)
        print("  FAIL %s (got %r, wanted %r)" % (name, got, want), file=sys.stderr)


def check_true(name, cond, why=""):
    if cond:
        PASS.append(name)
        print("  ok   %s" % name)
    else:
        FAIL.append(name)
        print("  FAIL %s %s" % (name, why), file=sys.stderr)


def run_git(args, cwd):
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def build_scratch_clone():
    """A scratch clone: a primary tree with one commit and a LINKED worktree beside it.

    Hooks are pointed at an empty directory, so no node's configured hook runs inside the fixture.
    """
    base = pathlib.Path(tempfile.mkdtemp(prefix="runlog-selftest-"))
    SCRATCH.append(base)
    hooks = base / "nohooks"
    hooks.mkdir()
    primary = base / "primary"
    primary.mkdir()
    ident = ["-c", "user.name=runlog selftest", "-c", "user.email=selftest@runlog.invalid",
             "-c", "commit.gpgsign=false", "-c", "core.hooksPath=" + hooks.as_posix()]
    run_git(["init", "-q"], primary)
    (primary / "a.txt").write_bytes(b"a\n")
    run_git(["add", "a.txt"], primary)
    run_git([*ident, "commit", "-q", "-m", "init"], primary)
    linked = base / "linked"
    made = run_git([*ident, "worktree", "add", "-q", "-b", "side", str(linked)], primary)
    return base, primary, linked, made.returncode


def run_cli(args, cwd):
    return subprocess.run([sys.executable, str(CLI), *args], cwd=str(cwd), capture_output=True,
                          text=True, encoding="utf-8", errors="replace")


def read_fixture_keys(name):
    """The keys of each LF-terminated line of a fixture, split WITHOUT the kit's parser.

    The CLI arm compares the kit's output against this, so the expected side must not come from the
    code under test: two operands from one generator assert nothing.
    """
    raw = (FIXTURES / name).read_bytes().split(b"\n")[:-1]
    return [[f.split(b"=", 1)[0].decode() for f in ln.split(b"\t")] for ln in raw]


# ================================================================ AC2 — escaping round-trips

def test_ac2_escape_round_trip():
    values = ["tab\there", "line\nbreak", "cr\rhere", "back\\slash", "\\t is not a tab",
              "\\", "\\\\", "mix\t\n\r\\end\\", "", "a=b=c", "unicode \u00e9 \u2713", "\\n\\r\\t"]
    fields = {"v": "1", "t": "1757770000.5", "p": "driver", "ev": "once"}
    for i, val in enumerate(values, 1):
        fields[f"val.{i}"] = val
    line = rl.render_line(fields)
    check("AC2: a rendered line holds exactly one TAB per field boundary",
          len(line.split("\t")), len(fields))
    check_true("AC2: ...and no raw LF or CR", "\n" not in line and "\r" not in line, repr(line))
    back = rl.parse_line(line).fields
    for i, val in enumerate(values, 1):
        check(f"AC2: value {i} comes back byte-identical ({val!r})", back[f"val.{i}"], val)
    check("AC2: the whole field map round-trips, order included", list(back.items()),
          list(fields.items()))
    # The escapes read back from text a SHELL producer wrote, not only from the kit's own writer.
    hand = "v=1\tt=1\tp=driver\tev=once\tk=a\\tb\\nc\\rd\\\\e"
    check("AC2: a hand-escaped value unescapes to TAB, LF, CR and backslash",
          rl.parse_line(hand).fields["k"], "a\tb\nc\rd\\e")


# ================================================================ AC3 — a mixed journal

def test_ac3_mixed_journal():
    j = rl.read_journal(FIXTURES / "journal-mixed.txt")
    check("AC3: the mixed fixture reads as state read", j.state, "read")
    check("AC3: three good lines come back", len(j.lines), 3)
    check("AC3: the bad count is two, not zero", j.bad, 2)
    check("AC3: the bad count IS the refusal list's length", j.bad, len(j.refusals))
    dotted = [ln for ln in j.lines if "sess.CLAUDE_CODE_SESSION_ID" in ln.fields]
    check("AC3: the dotted-key line survived", len(dotted), 1)
    f = dotted[0].fields if dotted else {}
    check("AC3: ...its uppercase dotted key is kept with its value",
          f.get("sess.CLAUDE_CODE_SESSION_ID"), "00000000-0000-4000-8000-000000000000")
    check("AC3: ...its indexed keys are kept", (f.get("fail.3"), f.get("ref.12")),
          ("a leg", "a b=c"))
    check("AC3: ...and the key this reader does not know is kept", f.get("zz_unknown"), "kept")
    reasons = dict(j.refusals)
    check("AC3: the torn line (line 2) is refused for its missing ev",
          "'ev'" in reasons.get(2, ""), True)
    check("AC3: the v=2 line (line 3) is refused as an unknown version",
          "unknown grammar version" in reasons.get(3, ""), True)
    check("AC3: good lines keep their own line numbers", [ln.lineno for ln in j.lines], [1, 4, 5])


# ================================================================ AC4 — pairing, and its cost

def test_ac4_invocations():
    j = rl.read_journal(FIXTURES / "invocations.txt")
    check("AC4: the invocations fixture parses clean", (j.bad, len(j.lines)), (0, 5))
    inv = rl.build_invocations(j.lines)
    check("AC4: a `once` line is never an invocation", len(inv), 3)
    check("AC4: start+end, start alone, end alone", [i.state for i in inv],
          ["ended", "killed-or-running", "orphan-end"])
    check("AC4: ...paired on (p, n)", [i.key for i in inv],
          [("driver", "1.1"), ("driver", "2.2"), ("driver", "3.3")])
    check("AC4: the ended invocation holds both halves",
          (inv[0].start.lineno, inv[0].end.lineno) if inv else None, (1, 4))
    check("AC4: the unmatched start holds no end", inv[1].end if len(inv) > 1 else "x", None)
    check("AC4: the orphan end holds no start", inv[2].start if len(inv) > 2 else "x", None)
    check_true("AC4: every state is one the kit declares",
               all(i.state in rl.INVOCATION_STATES for i in inv))
    # The same nonce under a DIFFERENT producer is a different invocation, and a second end for an
    # already-ended key is an orphan rather than a silent re-pair.
    extra = [rl.parse_line(s) for s in (
        "v=1\tt=1\tp=gates\tev=start\tn=1.1", "v=1\tt=2\tp=driver\tev=start\tn=1.1",
        "v=1\tt=3\tp=driver\tev=end\tn=1.1", "v=1\tt=4\tp=driver\tev=end\tn=1.1")]
    check("AC4: the producer is half the pairing key, and a second end is an orphan",
          [(i.key, i.state) for i in rl.build_invocations(extra)],
          [(("gates", "1.1"), "killed-or-running"), (("driver", "1.1"), "ended"),
           (("driver", "1.1"), "orphan-end")])


def test_ac4_parse_cost():
    """100,000 lines, zero subprocess spawns and zero regex compiles, counted by patching both."""
    base = pathlib.Path(tempfile.mkdtemp(prefix="runlog-cost-"))
    SCRATCH.append(base)
    big = base / "driver.log"
    sid = "00000000-0000-4000-8000-000000000000"
    rows = [f"v=1\tt=1757770000.{i % 1000000:06d}\tp=driver\tev={'end' if i % 2 else 'start'}\t"
            f"n={i // 2}.1\tverb=--status\tslug=dLoggedFlight\tsess.CLAUDE_CODE_SESSION_ID={sid}"
            f"\tchecks=14\tval=a\\tb" for i in range(100000)]
    big.write_bytes(("\n".join(rows) + "\n").encode("utf-8"))
    counts = {"compile": 0, "spawn": 0}

    class Refused(Exception):
        pass

    real = (re.compile, re._compile, subprocess.Popen, os.system, os.popen)

    def arm_compile(*a, **k):
        counts["compile"] += 1
        return real[0](*a, **k)

    def arm_inner_compile(*a, **k):
        counts["compile"] += 1
        return real[1](*a, **k)

    def arm_spawn(*a, **k):
        counts["spawn"] += 1
        raise Refused("a spawn inside the parse arm")

    re.compile, re._compile = arm_compile, arm_inner_compile
    subprocess.Popen = arm_spawn
    os.system = arm_spawn
    os.popen = arm_spawn
    try:
        t0 = time.perf_counter()
        # A spawn inside the parser raises `Refused` out of it; caught here, so the COUNT reports it
        # rather than a traceback that names nothing.
        try:
            j = rl.read_journal(big)
            inv = rl.build_invocations(j.lines)
        except Refused:
            j, inv = rl.Journal(path=big.as_posix(), state="refused"), []
        wall = time.perf_counter() - t0
        parse_counts = dict(counts)
        # LIVENESS: the patches must be able to MOVE, or a zero above proves nothing.
        re.compile("runlog-liveness-(probe)")
        try:
            subprocess.run([sys.executable, "-c", "pass"])
        except Refused:
            pass
        live = dict(counts)
    finally:
        re.compile, re._compile, subprocess.Popen, os.system, os.popen = real
    check("AC4: 100,000 lines parse with none refused", (len(j.lines), j.bad), (100000, 0))
    check("AC4: ...and pair into 50,000 ended invocations",
          (len(inv), sum(1 for i in inv if i.state == "ended")), (50000, 50000))
    check("AC4: parsing 100,000 lines compiled no regex", parse_counts["compile"], 0)
    check("AC4: parsing 100,000 lines spawned no process", parse_counts["spawn"], 0)
    check("AC4: liveness — the compile counter can move", live["compile"] > 0, True)
    check("AC4: liveness — the spawn counter can move", live["spawn"] > 0, True)
    print("  info report-only: read and paired 100,000 lines in %.2fs (%.1f us/line)"
          % (wall, wall * 1e6 / 100000))


# ================================================================ AC5 / AC7 / AC9 — the CLI and the root

def test_ac5_ac7_ac9_journal_and_root():
    base, primary, linked, made = build_scratch_clone()
    check("AC7 setup: the scratch clone has a linked worktree", made, 0)
    if made != 0:
        return
    common = pathlib.Path(run_git(["rev-parse", "--path-format=absolute", "--git-common-dir"],
                                  primary).stdout.strip())
    root_p = rl.resolve_journal_root(primary)
    root_l = rl.resolve_journal_root(linked)
    check("AC7: the primary tree and the linked worktree resolve ONE journal root", root_l, root_p)
    check("AC7: ...named runlog", root_p.name, rl.JOURNAL_DIR)
    check_true("AC7: ...directly under the clone's common dir",
               root_p.parent.samefile(primary / ".git") and root_p.parent.samefile(common),
               root_p.as_posix())
    check("AC7: ...and the linked worktree does NOT resolve under .git/worktrees/",
          "/worktrees/" in root_l.as_posix(), False)
    check_true("AC7: ...an absolute path", root_p.is_absolute(), root_p.as_posix())
    # The control: the per-worktree git dir DOES sit under .git/worktrees/, so the arm above can fail.
    gd = run_git(["rev-parse", "--path-format=absolute", "--git-dir"], linked).stdout.strip()
    check("AC7 control: the linked worktree's own git dir is under .git/worktrees/",
          "/worktrees/" in gd.replace("\\", "/"), True)

    # AC5 — an absent journal is a named state and exit 0.
    want_path = (root_p / "driver.log").as_posix()
    r = run_cli(["journal", "--producer", "driver"], primary)
    check("AC5: an absent journal exits 0", r.returncode, 0)
    check("AC5: ...prints `runlog: <path> absent` on stderr",
          f"runlog: {want_path} absent" in r.stderr, True)
    check("AC5: ...and prints nothing on stdout", r.stdout, "")

    # AC9 — two good lines and one torn one, read through the CLI from BOTH trees.
    root_p.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(FIXTURES / "driver-torn.txt", root_p / "driver.log")
    want_keys = read_fixture_keys("driver-torn.txt")
    for tree, label in ((primary, "primary"), (linked, "linked")):
        r = run_cli(["journal", "--producer", "driver"], tree)
        objs = [json.loads(s) for s in r.stdout.splitlines() if s.strip()]
        check(f"AC9 ({label}): exit 0 over a journal holding a torn line", r.returncode, 0)
        check(f"AC9 ({label}): stdout carries two JSON objects", len(objs), 2)
        check(f"AC9 ({label}): their keys match the lines' keys, in order",
              [list(o) for o in objs], want_keys)
        check(f"AC9 ({label}): stderr carries the resolved path and a bad count of 1",
              f"runlog: {want_path} lines=2 bad=1" in r.stderr, True)
        check(f"AC9 ({label}): ...and names why line 3 was refused",
              f"{want_path}:3 refused" in r.stderr and "no terminating LF" in r.stderr, True)
    check("AC9: a value comes back unescaped in the JSON",
          objs[0].get("slug") if objs else None, "dLoggedFlight")

    # An empty journal is its own named state, with the counts still printed.
    (root_p / "gates.log").write_bytes(b"")
    r = run_cli(["journal", "--producer", "gates"], primary)
    check("an empty journal exits 0 and says empty with its counts",
          (r.returncode, f"runlog: {(root_p / 'gates.log').as_posix()} empty lines=0 bad=0"
           in r.stderr), (0, True))
    r = run_cli(["journal", "--producer", "nobody"], primary)
    check("a producer outside the location contract is a usage refusal", r.returncode, 2)

    # Outside any clone, the root refuses by name — a ceiling stops git walking up into a real repo.
    lone = base / "not-a-repo"
    lone.mkdir()
    os.environ["GIT_CEILING_DIRECTORIES"] = str(base)
    try:
        try:
            rl.resolve_journal_root(lone)
            refused = ""
        except ValueError as exc:
            refused = str(exc)
        r = run_cli(["journal", "--producer", "driver"], lone)
    finally:
        del os.environ["GIT_CEILING_DIRECTORIES"]
    check("outside a git tree the journal root refuses by name",
          "not inside a git work tree" in refused, True)
    check("...and the CLI exits 2 saying so",
          (r.returncode, "not inside a git work tree" in r.stderr), (2, True))


def test_read_journal_states():
    base = pathlib.Path(tempfile.mkdtemp(prefix="runlog-states-"))
    SCRATCH.append(base)
    check("an absent file is state absent", rl.read_journal(base / "none.log").state, "absent")
    (base / "empty.log").write_bytes(b"")
    j = rl.read_journal(base / "empty.log")
    check("an empty file is state empty with nothing refused", (j.state, j.bad), ("empty", 0))
    j = rl.read_journal(base)
    check_true("a directory is state unreadable, with a note, and does not raise",
               j.state == "unreadable" and j.note, repr(j))
    (base / "crlf.log").write_bytes(b"v=1\tt=1\tp=driver\tev=once\r\n")
    j = rl.read_journal(base / "crlf.log")
    check("a CRLF-converted journal refuses its line rather than reading the CR as data",
          (len(j.lines), j.bad, "CR" in (j.refusals[0][1] if j.refusals else "")), (0, 1, True))
    (base / "utf.log").write_bytes(b"v=1\tt=1\tp=driver\tev=once\tk=\xc3\n"
                                   b"v=1\tt=2\tp=driver\tev=once\tk=\xc3\xa9\n")
    j = rl.read_journal(base / "utf.log")
    check("a torn multi-byte character refuses its own line and no other",
          (j.bad, [ln.fields["k"] for ln in j.lines]), (1, ["\u00e9"]))
    prefix = "v=1\tt=1\tp=driver\tev=once\tk="
    long_ok = prefix + "x" * (rl.MAX_LINE_BYTES - len(prefix))
    (base / "cap.log").write_bytes((long_ok + "\n" + long_ok + "x\n").encode())
    j = rl.read_journal(base / "cap.log")
    check("a line of exactly the cap is read, and one byte over is refused",
          (len(long_ok.encode()), len(j.lines), j.bad), (rl.MAX_LINE_BYTES, 1, 1))


# ================================================================ AC8 — golden lines and truncation

def test_ac8_golden_lines():
    j = rl.read_journal(FIXTURES / "golden-lines.txt")
    check("AC8: the four golden lines parse with a bad count of zero", (len(j.lines), j.bad), (4, 0))
    by = {(ln.fields["p"], ln.fields["ev"]): ln.fields for ln in j.lines}
    check("AC8: one golden line per producer act", sorted(by),
          [("driver", "end"), ("driver", "start"), ("gates", "once"), ("pushes", "start")])
    ds = by.get(("driver", "start"), {})
    de = by.get(("driver", "end"), {})
    gl = by.get(("gates", "once"), {})
    ps = by.get(("pushes", "start"), {})
    check("AC8: driver START carries sess.CLAUDE_CODE_SESSION_ID",
          "sess.CLAUDE_CODE_SESSION_ID" in ds, True)
    check("AC8: driver END carries checks=14 and exit=clean",
          (de.get("checks"), de.get("exit")), ("14", "clean"))
    check("AC8: the gate line carries fail.1 and fail_more",
          ("fail.1" in gl, gl.get("fail_more")), (True, "3"))
    check("AC8: the push START carries lander=0 and ref.1",
          (ps.get("lander"), ps.get("ref.1", "").startswith("refs/heads/main ")), ("0", True))
    check("AC8: the driver pair shares one nonce", ds.get("n") == de.get("n") and bool(ds.get("n")),
          True)
    for f in (ds, de, gl, ps):
        check_true(f"AC8: every key of the {f.get('p')}/{f.get('ev')} line passes check_line alone",
                   all(rl.check_line(f"v=1\tt=1\tp=x\tev=once\t{k}=y") is None
                       for k in f if k not in ("v", "t", "p", "ev")), f)


def test_ac8_truncation():
    head = {"v": "1", "t": "1757770000.5", "p": "pushes", "ev": "start", "n": "1.1",
            "note": "N" * 300}
    fields = dict(head)
    for i in range(1, 31):
        fields[f"ref.{i}"] = f"refs/heads/b{i:02d} " + "a" * 40 + f" refs/heads/b{i:02d} " + "b" * 40
    line = rl.render_line(fields)
    got = rl.parse_line(line).fields
    kept = sorted(int(k.split(".")[1]) for k in got if k.startswith("ref."))
    check_true("AC8: a 30-indexed-field line renders at or under 2048 bytes",
               len(line.encode()) <= rl.MAX_LINE_BYTES, str(len(line.encode())))
    check_true("AC8: ...and the renderer did have to drop something", len(kept) < 30, str(kept))
    check("AC8: ...the drops are counted as ref_more", int(got.get("ref_more", "0")), 30 - len(kept))
    check("AC8: ...highest index first, so what is left is ref.1..ref.k", kept,
          list(range(1, len(kept) + 1)))
    check("AC8: ...and no value was cut while an indexed field could still drop",
          (got.get("note"), [got[f"ref.{i}"] for i in kept]),
          (fields["note"], [fields[f"ref.{i}"] for i in kept]))
    # A producer's own `<base>_more` is ADDED to, never overwritten.
    f2 = {"v": "1", "t": "1", "p": "gates", "ev": "once", "fail_more": "3"}
    for i in range(1, 41):
        f2[f"fail.{i}"] = "leg name " + "z" * 60
    g2 = rl.parse_line(rl.render_line(f2)).fields
    n2 = sum(1 for k in g2 if k.startswith("fail."))
    check("AC8: an existing fail_more is added to", int(g2["fail_more"]), 3 + 40 - n2)
    check_true("AC8: ...the drop count lives in the existing field, not a second one",
               list(g2).count("fail_more") == 1 and list(g2).index("fail_more") == 4, list(g2)[:6])
    # Two families: the highest index across BOTH drops first.
    f3 = {"v": "1", "t": "1", "p": "x", "ev": "once"}
    for i in range(1, 16):
        f3[f"a.{i}"] = "A" * 70
        f3[f"b.{i + 10}"] = "B" * 70
    g3 = rl.parse_line(rl.render_line(f3)).fields
    check_true("AC8: across two families the higher indexes go first",
               max(int(k.split(".")[1]) for k in g3 if k.startswith("b.")) >=
               max(int(k.split(".")[1]) for k in g3 if k.startswith("a.")) and "b_more" in g3
               and "a_more" not in g3, sorted(g3))
    # A line under the cap is untouched: no `_more`, no reorder.
    small = {"v": "1", "t": "1", "p": "x", "ev": "once", "fail.1": "a", "k": "b"}
    check("a line under the cap renders unchanged",
          rl.render_line(small), "v=1\tt=1\tp=x\tev=once\tfail.1=a\tk=b")
    # Only when NO indexed field is left may a value be cut, and a cut never splits an escape.
    f4 = {"v": "1", "t": "1", "p": "x", "ev": "once", "blob": "\\" * 3000, "small": "keep me"}
    l4 = rl.render_line(f4)
    g4 = rl.parse_line(l4).fields
    check_true("a value is cut to fit when nothing indexed is left, never mid-escape",
               len(l4.encode()) <= rl.MAX_LINE_BYTES and set(g4["blob"]) == {"\\"}
               and g4["small"] == "keep me", str(len(l4.encode())))
    check_true("...and it cuts the LONGEST value, not the first", len(g4["blob"]) > 900,
               str(len(g4["blob"])))
    for bad, why in (({"t": "1", "v": "1", "p": "x", "ev": "once"}, "field 1 must be v"),
                     ({"v": "1", "t": "1", "p": "x", "ev": "once", "Bad": "1"}, "key grammar")):
        try:
            rl.render_line(bad)
            msg = ""
        except ValueError as exc:
            msg = str(exc)
        check(f"render_line refuses: {why}", why in msg, True)


# ================================================================ the grammar's refusals

def test_refusals_named():
    ok = "v=1\tt=1757770000.5\tp=driver\tev=once"
    cases = [
        ("field 1 is not v", "t=1\tv=1\tp=driver\tev=once", "field 1"),
        ("an unknown version", "v=9\tt=1\tp=driver\tev=once", "unknown grammar version"),
        ("a missing t", "v=1\tp=driver\tev=once", "'t'"),
        ("an empty p", "v=1\tt=1\tp=\tev=once", "'p'"),
        ("a missing ev", "v=1\tt=1\tp=driver", "'ev'"),
        ("an unknown ev", ok.replace("ev=once", "ev=begin"), "unknown event"),
        ("a start with no n", ok.replace("ev=once", "ev=start"), "no nonce"),
        ("an end with an empty n", ok.replace("ev=once", "ev=end") + "\tn=", "no nonce"),
        ("t with seven fraction digits", ok.replace("t=1757770000.5", "t=1.1234567"), "epoch"),
        ("t with a comma radix", ok.replace("t=1757770000.5", "t=1757770000,5"), "epoch"),
        ("t with a dangling radix", ok.replace("t=1757770000.5", "t=1757770000."), "epoch"),
        ("an uppercase key base", ok + "\tVerb=x", "key grammar"),
        ("a key led by a digit", ok + "\t9x=1", "key grammar"),
        ("a two-dot key", ok + "\ta.b.c=1", "key grammar"),
        ("a dash in a suffix", ok + "\tsess.A-B=1", "key grammar"),
        ("a field with no =", ok + "\tnoequals", "no '='"),
        ("an empty field", ok + "\t\tk=1", "no '='"),
        ("a trailing TAB", ok + "\t", "no '='"),
        ("a duplicate key", ok + "\tt=2", "twice"),
        ("a raw CR in a value", ok + "\tk=a\rb", "CR"),
        ("a raw LF in a value", ok + "\tk=a\nb", "LF"),
        ("an unknown escape", ok + "\tk=a\\qb", "unknown escape"),
        ("a lone trailing backslash", ok + "\tk=ab\\", "lone backslash"),
        ("a line over the cap", ok + "\tk=" + "x" * rl.MAX_LINE_BYTES, "line cap"),
        ("a multi-byte line over the cap", ok + "\tk=" + "\u00e9" * 1100, "line cap"),
    ]
    for label, raw, needle in cases:
        why = rl.check_line(raw)
        check(f"refused, and named: {label}", needle in (why or ""), True)
        try:
            rl.parse_line(raw)
            raised = False
        except ValueError:
            raised = True
        check(f"...parse_line raises on it: {label}", raised, True)
    near = [
        ("the plain line", ok),
        ("an uppercase dotted suffix", ok + "\tsess.CLAUDE_CODE_SESSION_ID=abc"),
        ("an indexed key", ok + "\tfail.1=x\tref.10=y"),
        ("an underscore key", ok + "\tphase_from=BUILDING\tdur_us=5"),
        ("an empty value on a non-required key", ok + "\tsess_bad="),
        ("t with no fraction", ok.replace("t=1757770000.5", "t=1757770000")),
        ("t with six fraction digits", ok.replace("t=1757770000.5", "t=1.123456")),
        ("a value carrying = and spaces", ok + "\tref.1=a b=c d"),
        ("a start with its nonce", ok.replace("ev=once", "ev=start") + "\tn=1.1"),
        ("an end with its nonce", ok.replace("ev=once", "ev=end") + "\tn=1.1"),
        ("a once with a nonce it does not need", ok + "\tn=1.1"),
        ("every escape at once", ok + "\tk=\\\\\\t\\n\\r"),
        ("a multi-byte value just under the cap", ok + "\tk=" + "\u00e9" * 1000),
    ]
    for label, raw in near:
        check(f"accepted, the near miss beside the refusals: {label}", rl.check_line(raw), None)


# ================================================================ AC10 — the memory root

def test_ac10_memory_root():
    base = pathlib.Path(tempfile.mkdtemp(prefix="runlog-memroot-"))
    SCRATCH.append(base)

    def build_tree(name, conf):
        d = base / name
        d.mkdir()
        if conf is not None:
            (d / rl.CONF_NAME).write_bytes(conf.encode("utf-8"))
        return d

    def resolve_or_refusal(d):
        try:
            return rl.resolve_memory_root(d)
        except ValueError as exc:
            return "REFUSED: " + str(exc)

    check("AC10: MEMORY_ROOT=docs/mem/ reads as docs/mem",
          resolve_or_refusal(build_tree("docs", "MEMORY_ROOT=docs/mem/\n")), "docs/mem")
    check("AC10: a conf setting no MEMORY_ROOT reads as the kit default",
          resolve_or_refusal(build_tree("unset", "DISCIPLINES=\"a b\"\nOTHER=1\n")), "memory")
    check("AC10: an absent conf reads as the kit default",
          resolve_or_refusal(build_tree("noconf", None)), "memory")
    for name, conf, needle in (
            ("slash", "MEMORY_ROOT=/\n", "names no directory"),
            ("empty", "MEMORY_ROOT=\n", "names no directory"),
            ("quoted-empty", "MEMORY_ROOT=\"\"\n", "names no directory"),
            ("dotdot", "MEMORY_ROOT=../x\n", "leaves the repository"),
            ("inner-dotdot", "MEMORY_ROOT=docs/../../x\n", "leaves the repository"),
            ("drive", "MEMORY_ROOT=C:/x\n", "leaves the repository"),
            ("backslash", "MEMORY_ROOT=docs\\\\mem\n", "leaves the repository")):
        got = resolve_or_refusal(build_tree(name, conf))
        check(f"AC10: MEMORY_ROOT refused by name ({name})",
              got.startswith("REFUSED: ") and "MEMORY_ROOT" in got and needle in got, True)
    # The sourcing rules that change a value, each beside the value it must produce.
    for name, conf, want in (
            ("export", "export MEMORY_ROOT=\"docs/m2\"\n", "docs/m2"),
            ("comment", "MEMORY_ROOT=docs/m3  # a note\n", "docs/m3"),
            ("bom", "\ufeffMEMORY_ROOT=docs/m4\n", "docs/m4"),
            ("crlf", "MEMORY_ROOT=docs/m5\r\n", "docs/m5"),
            ("last-wins", "MEMORY_ROOT=first\nMEMORY_ROOT=second\n", "second"),
            ("commented-out", "# MEMORY_ROOT=nope\nMEMORY_ROOT=yes\n", "yes"),
            ("dotted-name", "MEMORY_ROOT=docs/.mem..x\n", "docs/.mem..x")):
        check(f"AC10: the conf grammar reads ({name})",
              resolve_or_refusal(build_tree(name, conf)), want)


# ================================================================ the kit's own declarations

def test_kit_declarations():
    src = (HERE / "runlog_lib.py").read_text(encoding="utf-8")
    rows = [ln for ln in src.splitlines() if ln.startswith("KIT_RUNLOG_VERSION = ")]
    check("exactly one KIT_RUNLOG_VERSION line, the one version_from reads", len(rows), 1)
    marker = re.search(r"gov:kit runlog@([0-9.]+)", rows[0]) if rows else None
    check("...and its gov:kit marker agrees with the constant",
          marker.group(1) if marker else None, rl.KIT_RUNLOG_VERSION)
    check("the location contract: one file per producer",
          rl.PRODUCER_FILES, {"driver": "driver.log", "gates": "gates.log", "pushes": "pushes.log"})
    # AC1's third red condition, at the declaration. A list include claims LITERAL paths only, so a
    # fixture the list does not name falls to the `**` engine rule and ships. The population is read
    # off the filesystem, never off the list it is compared against.
    import tomllib
    desc = tomllib.loads((HERE / "kit.toml").read_text(encoding="utf-8"))
    owned = set()
    for rule in desc.get("files", []):
        inc = rule.get("include")
        if rule.get("role") == "project-owned" and isinstance(inc, list):
            owned.update(inc)
    on_disk = {p.relative_to(HERE).as_posix() for p in FIXTURES.rglob("*") if p.is_file()}
    check_true("AC1: the fixture population is non-empty, so the comparison below can fail",
               len(on_disk) >= 4, str(sorted(on_disk)))
    check("AC1: every fixture, and only fixtures, is named project-owned beside selftest.py",
          sorted(owned), sorted(on_disk | {"selftest.py"}))
    check_true("AC1: no project-owned element carries a glob, which a list include would drop",
               not any(ch in s for s in owned for ch in "*?["), str(sorted(owned)))


def main():
    print("runlog: arms")
    try:
        for name, fn in sorted(globals().items()):
            if name.startswith("test_") and callable(fn):
                fn()
    finally:
        for d in SCRATCH:
            shutil.rmtree(d, ignore_errors=True)
    total = len(PASS) + len(FAIL)
    print("\nrunlog: %d passed, %d failed (%d assertions, floor %d)"
          % (len(PASS), len(FAIL), total, ASSERTION_FLOOR))
    if total < ASSERTION_FLOOR:
        print("runlog: FAIL the suite executed %d assertions, under its floor of %d — an arm went "
              "missing" % (total, ASSERTION_FLOOR), file=sys.stderr)
        return 1
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
