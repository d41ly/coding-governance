#!/usr/bin/env python3
"""loop_witness.py — witnesses computed rather than typed by the acting agent (TOOL-dDeclaredLoop-17).

    python loop_witness.py acceptance --build <slug> --unit <id> --sha <sha> --cmd <c> [--cmd <c>]... [--root <path>]
    python loop_witness.py rerun --sha <pinned> --cmd <c> --expect <exit>:<hash> [--cmd <c> --expect <exit>:<hash>]...
    python loop_witness.py --fixture --plant <case>
    python loop_witness.py --selftest

`run_witness_commands(repo, sha, commands, timeout)` is the re-run: a detached worktree of `sha` in a
temporary directory, each command run there through the platform shell with a timeout and every name of
the memory-tree kit's `GIT_ENV_LEAKS` unset, its exit status (or `timeout`) and the first twelve hex digits
of the SHA-256 of its combined output kept, and the worktree removed on every exit path. Output is hashed
raw, so a command whose output carries a timestamp never re-runs equal; that is reported, never normalised.

`acceptance` is the acceptance stand-in until dWellOiledMachine's executor writes the record: `--sha`
resolved to its full commit in the tree at `--root`, the commands re-run there, and the record written
through the memory-tree kit's `write_acceptance`, `Writer: stand-in`, for the caller's commit. It prints
`loop-witness: wrote <path>` and one line per run, exit 0; 2 on a usage error, no `--cmd` or a SHA that
does not resolve; 1 where the writer refuses, writing nothing.

`rerun` is the probe stand-in, run in the repository at the current directory: each `--cmd` paired in
order with one `--expect`, answered `confirmed` when its exit and hash at the pinned SHA equal the
expectation, `refuted` when either differs, and `inconclusive` on a timeout or a SHA that does not
resolve. It prints `loop-witness: rerun · <verdict> · <exit> · <hash> · <command>` per command, exit 0
when every verdict is `confirmed`, 1 otherwise, 2 on a usage error, an unpaired `--cmd` included.

`--fixture --plant <case>` runs one plant of `PLANTS` in a scratch repository under the host temp
directory, exit 0 when it holds, 1 when it does not, 2 where a kit it runs does not resolve.
`--selftest` runs every plant, then the loop reader's `computed-actor` and `computed-unserved` plants,
each owed exit 1, printing one PASS or FAIL line each; exit 0 only when every one holds.

NOT CHECKED: that the commands a caller names are the spec's acceptance commands (the record keeps them
for a reader to compare), or that an exit was the expected answer. The hold-inherited plant runs the
unattended driver, found by `resolve_kit_dir`, which requires this kit; this kit declares no edge back.
"""
import argparse
import hashlib
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
from loop_lib import resolve_kit_dir  # noqa: E402  this kit's inline copy of the sibling resolver

SAY = "loop-witness"
#: The default bound of one re-run command, in seconds.
TIMEOUT = 600
EXPECT = re.compile(r"(?P<exit>-?\d+|timeout):(?P<hash>[0-9a-f]{12})")
PLANTS = {"acceptance": "a unit's two commands re-run at its commit, an uncommitted edit beside it",
          "acceptance-malformed": "two records typed by hand: no run line, and Writer agent",
          "probe-rerun": "a command re-run at its pinned SHA, at a later commit, and at a SHA that does not resolve",
          "hold-inherited": "a preflighted run held under inherited-red over an OWN attribution, an untied bar, and "
                            "an INHERITED one with its staged set"}
#: The loop reader's plants this leg runs too, each owed exit 1 with a refusal naming the acceptance row.
READER_PLANTS = ("computed-actor", "computed-unserved")
FX_UNIT = "TOOL-tFix-1"


# >>> resolve_bash_py -- canonical copy: resolve_bash.py in the gov lib dir (byte-identical; gated)
def resolve_bash(script):
    r"""The bash that can SEE `script`, by RUNNING each candidate, or None. GOV_BASH first, then the
    bash PATH names, then Git for Windows' two paths, each kept only when `test -f` on the script
    exits 0 under it. On Windows PATH order commonly puts the System32 WSL launcher first, which
    cannot open a `C:/` path, and a stub that exits 127 can sit there too (gotcha
    subprocess-resolves-a-different-shell); being on PATH is not evidence."""
    cands = [os.environ.get("GOV_BASH", ""), shutil.which("bash") or "",
             "C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe", "bash"]
    tried = []
    for c in cands:
        if not c or c in tried:
            continue
        tried.append(c)
        try:
            r = subprocess.run([c, "-c", 'test -f "$1"', "_", str(script)], capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            continue
        if r.returncode == 0:
            return c
    return None
# <<< resolve_bash_py


def read_memory_tree(anchor):
    """The memory-tree kit's directory holding `anchor`, found from this kit and put on `sys.path`;
    LookupError naming where it looked."""
    mt_dir = resolve_kit_dir("memory-tree", anchor, KIT)
    if str(mt_dir) not in sys.path:
        sys.path.insert(0, str(mt_dir))
    return mt_dir


def read_clean_env(**put):
    """This process's environment less the memory-tree kit's `GIT_ENV_LEAKS`, with `put` set."""
    read_memory_tree("tree_lib.py")
    from tree_lib import GIT_ENV_LEAKS
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS}
    env.update(put)
    return env


def read_git(repo, *args, env=None):
    """`git -C <repo> <args>`: `(exit, stdout stripped)`, text read as UTF-8."""
    p = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env if env is not None else read_clean_env())
    return p.returncode, p.stdout.strip()


def resolve_commit(repo, sha):
    """The full commit `sha` names in `repo`, or None where it names none."""
    rc, out = read_git(repo, "rev-parse", "--verify", "--quiet", "--end-of-options", "%s^{commit}" % sha)
    return out if rc == 0 and re.fullmatch(r"[0-9a-f]{40}", out) else None


def remove_tree(path):
    """Delete a directory through the memory-tree kit's fixture helper, which makes git's read-only
    objects writable first; a refused delete is left in the temp folder."""
    read_memory_tree("deviation_join.py")
    import deviation_join
    deviation_join.remove_tree(path)


def run_witness_commands(repo, sha, commands, timeout=TIMEOUT):
    """[(command, exit, hash12)] for each command run in a detached worktree of `sha`, `exit` an int or
    `timeout`. LookupError where the worktree cannot be added, `sha` naming no commit among the causes."""
    env = read_clean_env()
    tmp = tempfile.mkdtemp(prefix="lw-")
    tree = os.path.join(tmp, "tree")
    added = False
    try:
        rc, _out = read_git(repo, "worktree", "add", "--detach", tree, sha, env=env)
        if rc != 0:
            raise LookupError("git worktree add --detach of %s failed in %s" % (sha, repo))
        added = True
        runs = []
        for command in commands:
            # ponytail: a timeout kills the shell; a grandchild it spawned may outlive it until the
            # executor's spawn bound (TOOL-dDeclaredLoop-42) replaces this.
            try:
                p = subprocess.run(command, shell=True, cwd=tree, env=env, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, timeout=timeout)
                code, output = p.returncode, p.stdout
            except subprocess.TimeoutExpired as exc:
                code, output = "timeout", exc.output or b""
            runs.append((command, code, hashlib.sha256(output).hexdigest()[:12]))
        return runs
    finally:
        if added:
            read_git(repo, "worktree", "remove", "--force", tree, env=env)
        remove_tree(tmp)
        read_git(repo, "worktree", "prune", env=env)


def run_acceptance(args):
    """The `acceptance` verb: -> its exit."""
    root = pathlib.Path(args.root).absolute()
    if not args.cmd:
        print("%s: refused · acceptance takes at least one --cmd" % SAY, file=sys.stderr)
        return 2
    sha = resolve_commit(root, args.sha)
    if sha is None:
        print("%s: refused · --sha %s names no commit in %s" % (SAY, args.sha, root.as_posix()), file=sys.stderr)
        return 2
    try:
        read_memory_tree("build_records.py")
        import build_records
    except (LookupError, ImportError) as exc:
        print("%s: refused · no memory-tree kit writes the record: %s" % (SAY, exc), file=sys.stderr)
        return 2
    try:
        runs = run_witness_commands(root, sha, args.cmd)
        rel = build_records.write_acceptance(root, args.build, args.unit, sha, "stand-in", runs)
    except LookupError as exc:
        print("%s: refused · %s" % (SAY, exc), file=sys.stderr)
        return 2
    except (ValueError, OSError) as exc:
        print("%s: refused · %s" % (SAY, exc), file=sys.stderr)
        return 1
    print("%s: wrote %s" % (SAY, rel))
    for command, code, digest in runs:
        print("%s: run · %s · %s · %s" % (SAY, code, digest, command))
    return 0


def run_rerun(args):
    """The `rerun` verb, in the repository at the current directory: -> its exit."""
    cmds, expects = args.cmd or [], args.expect or []
    if not cmds or len(cmds) != len(expects):
        print("%s: refused · rerun takes one --expect per --cmd, paired in order: %d --cmd, %d --expect" % (
            SAY, len(cmds), len(expects)), file=sys.stderr)
        return 2
    wanted = [EXPECT.fullmatch(e) for e in expects]
    if not all(wanted):
        print("%s: refused · --expect is <exit>:<hash12>, the exit an integer or timeout" % SAY, file=sys.stderr)
        return 2
    root = pathlib.Path(".").absolute()
    sha = resolve_commit(root, args.sha)
    try:
        runs = run_witness_commands(root, sha, cmds) if sha else None
    except LookupError:
        runs = None
    ok = True
    for n, command in enumerate(cmds):
        if runs is None or runs[n][1] == "timeout":
            verdict, code, digest = "inconclusive", runs[n][1] if runs else "-", runs[n][2] if runs else "-"
        else:
            code, digest = runs[n][1], runs[n][2]
            verdict = "confirmed" if (str(code), digest) == (wanted[n]["exit"], wanted[n]["hash"]) else "refuted"
        ok = ok and verdict == "confirmed"
        print("%s: rerun · %s · %s · %s · %s" % (SAY, verdict, code, digest, command))
    return 0 if ok else 1


# -------------------------------------------------------------------------------- the plants
def run_fixture_git(repo, *args):
    """A git command in a fixture repository, under a fixed identity; CalledProcessError on a failure."""
    return subprocess.run(["git", "-c", "user.name=fx", "-c", "user.email=fx@example.invalid", "-c",
                           "commit.gpgsign=false", "-c", "core.autocrlf=false", *args], cwd=repo, check=True,
                          capture_output=True, text=True, encoding="utf-8", errors="replace",
                          env=read_clean_env()).stdout.strip()


def write_fixture_files(root, files):
    """Each `{repo-relative path: text}` written LF under `root`."""
    for rel, text in files.items():
        path = pathlib.Path(root, rel)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)


def write_scratch_unit(root):
    """A scratch git repository at `root` holding the build `tFix` and its unit's spec, committed."""
    run_fixture_git(root, "init", "-q", "--template=")
    write_fixture_files(root, {
        ".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tool:TOOL"\n',
        "memory/builds/tFix/spec/2026-01-01-spec-%s.md" % FX_UNIT:
            "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01 · node a · Tier-2 · base 0123abcd\n" % FX_UNIT})


def run_self(*argv, cwd=None):
    """This script as a process: `(exit, stdout and stderr)`."""
    p = subprocess.run([sys.executable, str(pathlib.Path(__file__).absolute()), *argv], cwd=cwd,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout + p.stderr).strip()


def check_acceptance_plant(root, bad):
    """AC1: the stand-in re-runs at the named commit, not in the caller's working tree."""
    py = sys.executable
    write_scratch_unit(root)
    write_fixture_files(root, {"answer.txt": "no\n"})
    run_fixture_git(root, "add", "-A")
    run_fixture_git(root, "commit", "-qm", "the scratch unit")
    sha = run_fixture_git(root, "rev-parse", "HEAD")
    write_fixture_files(root, {"answer.txt": "yes\n"})   # uncommitted: the caller's tree answers 0
    cmds = ['"%s" -c "import sys; sys.exit(0)"' % py,
            '"%s" -c "import sys; sys.exit(0 if open(\'answer.txt\').read().strip() == \'yes\' else 1)"' % py]
    rc, said = run_self("acceptance", "--build", "tFix", "--unit", FX_UNIT, "--sha", sha[:8],
                        "--cmd", cmds[0], "--cmd", cmds[1], "--root", str(root))
    print("%s: acceptance · exit %d · %s" % (SAY, rc, said.splitlines()[0] if said else "no output"))
    got = re.search(r"wrote (\S+)", said)
    if rc != 0 or not got:
        bad.append("acceptance exited %d, not 0 naming the record: %s" % (rc, said[:300]))
        return
    rel = got.group(1)
    if not re.fullmatch(r"memory/builds/tFix/build/\d{4}-\d{2}-\d{2}-build-%s-acceptance-1\.md" % FX_UNIT, rel):
        bad.append("the record is %s, not <date>-build-%s-acceptance-1.md in the build folder" % (rel, FX_UNIT))
    mt_dir = read_memory_tree("build_records.py")
    import build_records
    rec = build_records.read_acceptance(rel, pathlib.Path(root, rel).read_text(encoding="utf-8"))
    exits = [code for _c, code, _h in rec["runs"]]
    if rec.get("Writer") != "stand-in" or rec.get("Sha") != sha or exits != ["0", "1"] or rec["malformed"]:
        bad.append("the record reads Writer %s, Sha %s, exits %s, malformed %s; owed stand-in, %s, 0 then 1" % (
            rec.get("Writer"), rec.get("Sha"), exits, rec["malformed"], sha))
    p = subprocess.run([sys.executable, str(mt_dir / "build_records.py"), "read", str(pathlib.Path(root, rel))],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if p.returncode != 0:
        bad.append("build_records.py read exited %d: %s" % (p.returncode, (p.stdout + p.stderr)[:300]))
    trees = [ln for ln in run_fixture_git(root, "worktree", "list", "--porcelain").splitlines()
             if ln.startswith("worktree ")]
    if len(trees) != 1:
        bad.append("git worktree list shows %d worktrees, not the fixture's one: %s" % (len(trees), trees))
    print("%s: acceptance · %s · exits %s · %d worktree(s)" % (SAY, rel, " ".join(exits), len(trees)))


def check_malformed_plant(root, bad):
    """AC2: a record typed by hand without its run lines, or by a writer outside the set, reads malformed."""
    mt_dir = read_memory_tree("build_records.py")
    folder = "memory/builds/tFix/build/2026-01-01-build-%s-acceptance-" % FX_UNIT
    head = "# %s acceptance %%d — typed\n\n**Serves:** acceptance %s\n\n- **Sha:** %s\n- **Writer:** %%s\n" \
           "- **Caused-by:** %s\n" % (FX_UNIT, FX_UNIT, "a" * 40, FX_UNIT)
    write_fixture_files(root, {folder + "1.md": head % (1, "stand-in"),
                               folder + "2.md": head % (2, "agent") + "\nrun · 0 · 0123456789ab · true\n"})
    for n, needle in ((1, "run line is missing"), (2, "Writer agent is outside executor · stand-in")):
        p = subprocess.run([sys.executable, str(mt_dir / "build_records.py"), "read",
                            str(pathlib.Path(root, folder + "%d.md" % n))],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        said = p.stdout + p.stderr
        print("%s: acceptance-malformed · record %d · exit %d · %s" % (
            SAY, n, p.returncode, next((ln for ln in said.splitlines() if needle in ln), "no line naming it")))
        if p.returncode != 1 or needle not in said:
            bad.append("record %d read exit %d, not 1 naming %r: %s" % (n, p.returncode, needle, said[:300]))


def check_rerun_plant(root, bad):
    """AC3: the re-run reads the pinned SHA, never HEAD."""
    write_scratch_unit(root)
    write_fixture_files(root, {"out.txt": "one\n"})
    run_fixture_git(root, "add", "-A")
    run_fixture_git(root, "commit", "-qm", "the probe's commit")
    pinned = run_fixture_git(root, "rev-parse", "HEAD")
    cmd = '"%s" -c "print(open(\'out.txt\').read())"' % sys.executable
    [(_c, code, digest)] = run_witness_commands(root, pinned, [cmd])
    write_fixture_files(root, {"out.txt": "two\n"})
    run_fixture_git(root, "commit", "-qam", "a later commit")
    later = run_fixture_git(root, "rev-parse", "HEAD")
    expect = "%s:%s" % (code, digest)
    for sha, rc_owed, verdict in ((pinned, 0, "confirmed"), (later, 1, "refuted"), ("0badc0de", 1, "inconclusive")):
        rc, said = run_self("rerun", "--sha", sha, "--cmd", cmd, "--expect", expect, cwd=root)
        print("%s: probe-rerun · %s · exit %d · %s" % (SAY, sha[:8], rc, said.splitlines()[-1] if said else ""))
        if rc != rc_owed or "rerun · %s · " % verdict not in said:
            bad.append("rerun at %s exited %d, not %d answering %s: %s" % (sha[:8], rc, rc_owed, verdict, said[:300]))


#: The conf the hold-inherited plant's driver reads: every key the driver NOTEs about when blank, declared.
HOLD_CONF = """MEMORY_ROOT=memory
UNITS_REGION_CUTOFF="2026-08-19"
PROMPT_BRIEF_CUTOFF="2099-01-01"
PROMPT_BRIEF_SKELETON_CUTOFF="2099-01-01"
LANDER="echo land"
LANDER_MODE="primary"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
GATE_BOUND="3600"
GATE_WALL="21600"
UNIT_STALL_BOUND="1800"
TASK_STALL_BOUND="5400"
REVIEW_ROUNDS="7"
RESUME_STALE_BOUND="5400"
WIRING_CHECK="true"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
RESUME_SCHEDULE="on"
RESUME_SCHEDULE_CREATE="TheScheduleCreate"
RESUME_SCHEDULE_DELETE="TheScheduleDelete"
RESUME_SCHEDULE_DELAY="1800"
RESUME_SCHEDULE_LIMIT="6"
RUN_CLAIMS="off"
PHASES_EXTRA=""
DOD_EXTRA=""
"""


def check_hold_plant(root, bad):
    """AC4 and AC5: `--hold --code inherited-red` is joined to the bar's attribution and its staged set.
    -> 2 where the driver or a bash that sees it does not resolve, else None."""
    try:
        driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
    except LookupError as exc:
        print("%s: hold-inherited · unarmed · %s" % (SAY, exc))
        return 2
    bash = resolve_bash(driver)
    if bash is None:
        print("%s: hold-inherited · unarmed · no bash that can see %s, GOV_BASH, PATH and Git for Windows "
              "looked in" % (SAY, driver.as_posix()))
        return 2
    repo, origin = pathlib.Path(root, "r"), pathlib.Path(root, "o.git")
    repo.mkdir()
    env = read_clean_env(GOV_DEFAULT_BRANCH="main", CLAUDE_CODE_SESSION_ID="fixture-session",
                         CLAUDE_PID="999999999")

    def run_driver(*argv):
        p = subprocess.run([bash, str(driver), *argv], cwd=repo, env=env, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        return p.returncode, p.stdout + p.stderr

    run_fixture_git(repo, "init", "-q", "-b", "main", "--template=")
    write_fixture_files(repo, {
        ".unattended.conf": HOLD_CONF,
        "memory/builds/tRun/README.md": "---\nslug: tRun\nnode: a\nopened: 2026-08-01\nstreams: architecture\n"
                                        "roster: ARCH\nids: ARCH-tRun-1\n---\n\n# tRun\n\n<!-- gen:build-index -->\n"
                                        "**Build status:** OPEN · 1 unit(s)\n\n<!-- gen:build-units -->\n"
                                        "| Unit | Status | Rev | Last change |\n|---|---|---|---|\n"
                                        "| [ARCH-tRun-1 — the unit](spec/one.md) | OPEN | rev-1 | 2026-08-01 |\n"
                                        "<!-- /gen:build-units -->\n<!-- /gen:build-index -->\n",
        "memory/builds/tRun/RUN.md": "# tRun — run state\n\n<!-- run:generated -->\n<!-- /run:generated -->\n\n"
                                     "## Mandate\n<!-- run:mandate -->\nThe owner authorizes build tRun to merge "
                                     "to main and to push.\n<!-- /run:mandate -->\n\n## Run facts\n\n## Parked\n",
        "memory/guides/BUILD-METHOD.md": "# build method (stub)\n\n## M1\n\nExistence is what the driver tests.\n"})
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-qm", "base")
    run_fixture_git(root, "init", "-q", "--bare", str(origin))
    run_fixture_git(root, "--git-dir", str(origin), "symbolic-ref", "HEAD", "refs/heads/main")
    # an identity in each repository the driver commits in, the bare origin included: a node with no
    # global identity otherwise fails a driver commit and reads as a kit defect
    for where in (("-C", str(repo)), ("--git-dir", str(origin))):
        run_fixture_git(root, *where, "config", "user.email", "fx@example.invalid")
        run_fixture_git(root, *where, "config", "user.name", "fx")
    run_fixture_git(repo, "remote", "add", "origin", str(origin))
    run_fixture_git(repo, "push", "-q", "origin", "main")
    base = run_fixture_git(repo, "rev-parse", "HEAD")
    run_fixture_git(repo, "checkout", "-q", "-b", "unit")
    run_fixture_git(repo, "commit", "-q", "--allow-empty", "-m", "unit work")
    # a FIRST preflight refuses a carried branch, so local main stands at HEAD for that call alone
    run_fixture_git(repo, "update-ref", "refs/heads/main", "HEAD")
    rc, said = run_driver("--preflight", "tRun", "--keepalive-id", "k1")
    run_fixture_git(repo, "update-ref", "refs/heads/main", base)
    if rc != 0:
        bad.append("--preflight exited %d: %s" % (rc, said[-600:]))
        return None
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-qm", "records(tRun): preflight")
    bar = run_fixture_git(repo, "rev-parse", "HEAD")
    gate = pathlib.Path(run_fixture_git(repo, "rev-parse", "--absolute-git-dir"), "gate-run", "fx1")
    write_fixture_files(gate, {"header": "head\t%s\ntree_clean\tyes\n" % bar,
                               "verdict": "verdict\tRED\nfailed\t1\ntree_moved\tno\n",
                               "attribution": "x leg\tOWN\t1\t0\t-\t3\t0badc0de\t-\tstub\n"})
    # the close's records, committed after the bar: the gates-run fact and a BACKLOG.md row beside it
    run_md = repo / "memory/builds/tRun/RUN.md"
    text = run_md.read_text(encoding="utf-8").replace("## Run facts\n", "## Run facts\ngates-run: fx1 %s\n" % bar[:8], 1)
    backlog = "memory/builds/tRun/BACKLOG.md"
    write_fixture_files(repo, {"memory/builds/tRun/RUN.md": text, backlog: "# tRun backlog\n\n- an inherited red\n"})
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-qm", "records(tRun): the bar's fact and the staged row")
    staged = "%s@%s\n" % (backlog, run_fixture_git(repo, "rev-parse", "HEAD:" + backlog))
    hold = ("--hold", "tRun", "--code", "inherited-red", "--until", "probe gate", "--reason", "r", "--reaped", "k1")
    cases = (("an OWN leg", "OWN", True, 1, ("UNATTENDED check 83 FAILED", "its attribution reads x leg OWN")),
             ("no staged set", "INHERITED", False, 1, ("UNATTENDED check 83 FAILED", "ran at")),
             ("every leg INHERITED, the staged set recorded", "INHERITED", True, 0, ("phase HELD",)))
    for case, verdict, with_set, rc_owed, needles in cases:
        write_fixture_files(gate, {"attribution": "x leg\t%s\t1\t0\t-\t3\t0badc0de\t-\tstub\n" % verdict})
        if with_set:
            write_fixture_files(gate, {"staged": staged})
        elif (gate / "staged").exists():
            (gate / "staged").unlink()
        rc, said = run_driver(*hold)
        line = next((ln for ln in said.splitlines() if needles[-1] in ln), "no line naming it")
        print("%s: hold-inherited · %s · exit %d · %s" % (SAY, case, rc, line[:200]))
        if rc != rc_owed or not all(n in said for n in needles):
            bad.append("%s: --hold exited %d, not %d printing %s: %s" % (case, rc, rc_owed, " and ".join(needles),
                                                                         said[-600:]))
    if "phase: HELD" not in run_md.read_text(encoding="utf-8"):
        bad.append("the run-state does not read phase: HELD after the admitted hold")
    return None


def run_fixture(plant):
    """One plant in a scratch directory under the host temp directory: exit 0 PASS, 1 FAIL, 2 unarmed."""
    bad, root = [], pathlib.Path(tempfile.mkdtemp(prefix="lwf-"))
    print("%s: fixture · plant %s · %s" % (SAY, plant, PLANTS[plant]))
    try:
        rc = {"acceptance": check_acceptance_plant, "acceptance-malformed": check_malformed_plant,
              "probe-rerun": check_rerun_plant, "hold-inherited": check_hold_plant}[plant](root, bad)
    except (subprocess.CalledProcessError, OSError, LookupError, ImportError) as exc:
        detail = getattr(exc, "stderr", "") or ""
        bad.append("the fixture could not be built: %s %s" % (exc, detail.strip()[:300]))
        rc = None
    finally:
        remove_tree(root)
    if rc == 2:
        print("%s: UNARMED %s — a kit it runs does not resolve, which is never a pass" % (SAY, plant))
        return 2
    for why in bad:
        print("%s: FAIL %s · %s" % (SAY, plant, why))
    if bad:
        return 1
    print("%s: PASS %s" % (SAY, plant))
    return 0


def run_selftest():
    """Every plant in order, then the loop reader's two computed-witness plants: exit 0 when all hold."""
    failed = []
    for plant in PLANTS:
        if run_fixture(plant) != 0:
            failed.append(plant)
    for plant in READER_PLANTS:
        p = subprocess.run([sys.executable, str(KIT / "loop_lib.py"), "--fixture", "--plant", plant],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        line = next((ln for ln in p.stdout.splitlines()
                     if ln.startswith("loop: refused") and "computed-witness row" in ln and "(acceptance)" in ln), None)
        if p.returncode == 1 and line:
            print("%s: PASS %s · %s" % (SAY, plant, line[:200]))
        else:
            failed.append(plant)
            print("%s: FAIL %s · loop_lib.py exited %d with no refusal naming the acceptance row: %s" % (
                SAY, plant, p.returncode, (p.stdout + p.stderr)[-300:]))
    print("%s: %s · %d plant(s) · %d failed%s" % (SAY, "FAIL" if failed else "PASS", len(PLANTS) + len(READER_PLANTS),
                                                 len(failed), (": " + " ".join(failed)) if failed else ""))
    return 1 if failed else 0


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="loop_witness.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run one plant over a scratch repository")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--selftest", action="store_true", help="run every plant")
    sub = ap.add_subparsers(dest="verb")
    acc = sub.add_parser("acceptance", help="re-run a unit's acceptance commands at a commit and write the record")
    acc.add_argument("--build", required=True)
    acc.add_argument("--unit", required=True)
    acc.add_argument("--sha", required=True)
    acc.add_argument("--cmd", action="append")
    acc.add_argument("--root", default=".")
    rer = sub.add_parser("rerun", help="re-run a probe's commands at its pinned SHA and compare")
    rer.add_argument("--sha", required=True)
    rer.add_argument("--cmd", action="append")
    rer.add_argument("--expect", action="append")
    args = ap.parse_args(argv)
    if args.selftest:
        if args.verb or args.fixture or args.plant:
            ap.error("--selftest takes no verb and no plant")
        return run_selftest()
    if args.fixture:
        if args.verb or not args.plant:
            ap.error("--fixture takes --plant <case> and no verb")
        return run_fixture(args.plant)
    if args.plant:
        ap.error("--plant takes --fixture")
    if args.verb == "acceptance":
        return run_acceptance(args)
    if args.verb == "rerun":
        return run_rerun(args)
    ap.error("a verb, acceptance or rerun, or --fixture --plant <case>, or --selftest")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
