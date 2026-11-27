#!/usr/bin/env python3
"""ratchet.py -- the `ratchet` leg pack: one verb per row of retrofit's `[ratchet]` table (TOOL-dWitnessedBar-14).

    python <prefix>/memory-tree/ratchet.py never-gains          # ratchet (never gains)
    python <prefix>/memory-tree/ratchet.py both-ways            # ratchet (both ways)
    python <prefix>/memory-tree/ratchet.py unarmed              # ratchet (unarmed)
    python <prefix>/memory-tree/ratchet.py populated            # ratchet (populated)
    python <prefix>/memory-tree/ratchet.py seed-laundering      # ratchet (seed laundering)
    python <prefix>/memory-tree/ratchet.py rename               # ratchet (rename)
    python <prefix>/memory-tree/ratchet.py keys-not-scalar [--measure]   # ratchet (keys, not a scalar)
    python <prefix>/memory-tree/ratchet.py measure-cutoffs      # the `date-cutoffs` seed
    python <prefix>/memory-tree/ratchet.py key-shape            # ratchet (key shape)
    python <prefix>/memory-tree/ratchet.py widen <population> --key <k> [--key <k>] --reason <text> --unit <id>
    python <prefix>/memory-tree/ratchet.py --list               # each pack row, its leg and whether it is armed
    python <prefix>/memory-tree/ratchet.py --fixture [--plant <case>]   # ratchet selftest

Every verb runs in the repository its working directory sits in and reads every registration through
the ledger factory this kit carries (`legacy_ledger.py`, unit 13): its registrations, rows, counts, base
compare and rename carry. It mints no count compare of its own. A leg prints its population count and
each finding's population and key, and exits 0 green, 1 on a finding, 2 on a refusal. With no compare
base a base leg prints `unresolved`, never green. A population the base holds nowhere, neither at its
home nor under its header at another path, is `new at <sha12>` with its row count and is graded no
further by `never gains`, `seed laundering` and `rename` (§8 F10). A population whose base file at its
home opens with no ledger header is a legacy home its own pass regrammared in place: it is
`regrammared at <sha12>` with its row count and graded no further by those three legs either
(TOOL-dWitnessedBar-16 S11); what that does not check is the legacy rows against the converted ones,
which the conversion record holds. A live leg with nothing to grade
prints one `unarmed · <leg> · <why>` line, no pass line, and exits 0 (§8 F9); the runner prints that
exit 0 as passed, so `unarmed` is read in the leg's output and in `--list`, never in the bar. The one
exception is `keys-not-scalar`, the leg an adopter receives: an unarmed `conf-scalar-pins` exits 1
naming the seed command (TOOL-dWitnessedBar-46 S3).

A RAISE IS ADMITTED ONLY THROUGH A WIDEN RECORD. `widen` is the door: it reads `retrofit.widen`, writes
the next `<date>-build-<unit>-widen-<n>.md` of the build the unit id names through the record factory's
`write_record` (Population, Keys, Reason, Caused-by), then the row `widened:<record stem>` at HEAD's sha,
count 1 for a new key and one above the row's for a key it holds; under `refuse` it writes nothing.
`never gains` grades every `widened:` row of a `shrink-only` or `ceiling` population against its record:
tracked, naming the population and the key, its Reason non-empty, and under `refuse` tracked at the base
too. `keys-not-scalar --measure` is the `conf-scalar-pins` seed: one TAB row per `.<name>.conf` and
`*_PIN` key of the root confs in the working tree, tracked or not, its count the `<KEY>=` assignments of
that key, so a conf copied before the first commit is seeded; an ignored one is never read (TOOL-dWitnessedBar-52).
`measure-cutoffs` is the `date-cutoffs` seed over the same conf walk: one TAB row per `*_CUTOFF` key, its
count the date as eight digits, a blank date `99991231` (TOOL-dWitnessedBar-17 S6), and so a value that is
no real day, `none` say, with one stderr line naming it (TOOL-dWitnessedBar-51 S37). A base leg's
`unresolved` line with no base names the remedy, and no `GATE_` knob passes it (S33).

WHAT IT DOES NOT CHECK. A widened row's count, which the record does not name. That a leg another
registration names exists in the manifest. The rows a first seed writes, which are `test.seed`'s
(unit 15). The touch join, which is `build.scope`'s (dScopedBuild) and printed unarmed by `--list`.
An empty armed population is admitted on any seen-red line naming its registration's leg, read through
`seen_red.read_seen_red_records` (unit 7): that the leg has been seen red, never that this population's
emptiness is right.
"""
from __future__ import annotations

import datetime
import json
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
import legacy_ledger as LL  # noqa: E402  the ledger factory, this kit's copy
from build_records import derive_record_name, read_record, write_record  # noqa: E402  the record factory
from tree_lib import parse_conf_line, read_policy_value  # noqa: E402  the kit's one conf line and policy read
from id_grammar import SlugPattern  # noqa: E402  the slug grammar, bound at first use
from seen_red import read_seen_red_records  # noqa: E402  the one seen-red record reader (unit 7)
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


SAY = "ratchet"
LEGS = {  # verb -> the leg it is
    "never-gains": "ratchet (never gains)",
    "both-ways": "ratchet (both ways)",
    "unarmed": "ratchet (unarmed)",
    "populated": "ratchet (populated)",
    "seed-laundering": "ratchet (seed laundering)",
    "rename": "ratchet (rename)",
    "keys-not-scalar": "ratchet (keys, not a scalar)",
    "key-shape": "ratchet (key shape)",
}
SELFTEST_LEG = "ratchet selftest"
TOUCH_JOIN = "build.scope (dScopedBuild)"
# retrofit.md's `[ratchet]` table, row by row: the row, the leg that holds it, and how
PACK_ROWS = (
    ("never gains", "never-gains"), ("both ways", "both-ways"), ("touch join", None),
    ("untouched quiet", "--fixture"), ("unarmed", "unarmed"), ("populated", "populated"),
    ("seed laundering", "seed-laundering"), ("rename", "rename"), ("merge", "--fixture"),
    ("keys, not a scalar", "keys-not-scalar"), ("key shape", "key-shape"),
)
WIDEN_KEY = "retrofit.widen"
WIDEN_VALUES = ("record-reason", "refuse")
WIDEN_DEFAULT = "record-reason"  # the catalogue default, which holds where no policy kit resolves
WIDEN_KIND = "widen"
WIDENED_LEAD = "widened:"
WIDEN_DIRECTIONS = ("shrink-only", "ceiling")  # the directions whose growth a widen record admits
SCALAR_POPULATION = "conf-scalar-pins"
PIN_RE = re.compile(r"([A-Z_]+_PIN)=")
CUTOFF_RE = re.compile(r"([A-Z0-9_]+_CUTOFF)=")
BLANK_CUTOFF = 99991231  # a blank cutoff reads as the latest date, so disarming its rule is a raise
UNIT_RE = SlugPattern(lambda g: r"[A-Za-z]+-((?:" + g.slug_class + r"))-\d+")   # the slug grammar's (TOOL-dTotalRecall-5 S7)
EMPTY_TEXT = "reads unarmed, no seen-red line names its leg"
# THE REMEDY a base leg with no compare base prints on its `unresolved` line (TOOL-dWitnessedBar-51 S33).
# No `GATE_` knob turns that line into a pass: the remedy is a base, never a waiver.
NO_BASE_REMEDY = ("remedy: fetch the default branch so a base resolves (git fetch <remote> <branch>), or name "
                  "the ref with GOV_REMOTE and GOV_DEFAULT_BRANCH")


def print_line(*parts):
    """One output line, its parts joined by ` · `."""
    print(" · ".join(str(p) for p in parts))


def render_key(key):
    """A row key as its TAB-joined fields, the row grammar's own spelling."""
    return "\t".join(key)


def resolve_root(cwd):
    """The top of the work tree `cwd` sits in; ValueError outside one."""
    rc, out = LL._run_git(cwd, "rev-parse", "--show-toplevel")
    if rc != 0 or not out.strip():
        raise ValueError("not inside a git work tree")
    return out.strip()


def read_tracked_paths(root):
    """Every path `git ls-files` names at `root`, the index's population."""
    rc, out = LL._run_git(root, "ls-files", "-z")
    if rc != 0:
        raise ValueError("git ls-files failed at %s" % root)
    return [p for p in out.split("\0") if p]


def read_widen_policy(root):
    """`retrofit.widen` at `root`'s landed revision; its default, said on stderr, where no policy kit
    resolves. A reader refusal or a value outside the catalogue's set is ValueError."""
    try:
        value = read_policy_value("retrofit.widen", root)
    except LookupError as exc:
        print("%s: %s: no policy kit resolves, so its catalogue default %s holds: %s"
              % (SAY, WIDEN_KEY, WIDEN_DEFAULT, exc), file=sys.stderr)
        return WIDEN_DEFAULT
    if value not in WIDEN_VALUES:
        raise ValueError("%s reads %r, outside %s" % (WIDEN_KEY, value, " | ".join(WIDEN_VALUES)))
    return value


def measure_rows(root, reg):
    """The rows a registration's working home holds, 0 for an absent home."""
    try:
        rows, _bad = LL.read_ledger(root, reg)
    except OSError:
        return 0
    return len(rows)


def check_new_at_base(root, reg, sha):
    """True where the base `sha` holds the population nowhere: no file at its home (`git cat-file -e`)
    and no file whose first line is its header (one `git grep -n`, each line-1 hit read by `parse_header`).
    A base holding the header at another path is no new population."""
    rc, _out = LL._run_git(root, "cat-file", "-e", "%s:%s" % (sha, reg.home))
    if rc == 0:
        return False
    rc, out = LL._run_git(root, "grep", "-n", "-F", "-e", "# ledger · %s · " % reg.population, sha, "--")
    if rc not in (0, 1):
        return False
    for line in out.splitlines():
        rest = line[len(sha) + 1:] if line.startswith(sha + ":") else line
        m = re.match(r"(.+?):1:(.*)$", rest)
        if not m:
            continue
        try:
            if LL.parse_header(m.group(2))["population"] == reg.population:
                return False
        except ValueError:
            continue
    return True


def check_regrammared_at_base(root, reg, sha):
    """True where the base `sha` holds a file at the registration's home whose first line is no ledger
    header (`parse_header` refuses it): a legacy home the conversion's own pass regrammared in place
    (TOOL-dWitnessedBar-16 S11). A base home opening with a ledger header is graded as before."""
    rc, text = LL._run_git(root, "show", "%s:./%s" % (sha, reg.home))
    if rc != 0:
        return False
    try:
        LL.parse_header(text.split("\n", 1)[0])
    except ValueError:
        return True
    return False


def parse_widen_keys(value):
    """The keys a widen record's `Keys` field holds: each backticked span's TAB fields, or the whole value."""
    spans = re.findall(r"`([^`]+)`", value) or [value]
    return {tuple(f.strip() for f in span.split("\t")) for span in spans}


def check_widen_admitted(root, reg, key, stem, policy, sha, tracked):
    """-> (admitted, the record's path or why not) for one `widened:<stem>` row of `reg`."""
    named = derive_record_name(WIDEN_KIND)
    hits = [p for p in tracked if p.rsplit("/", 1)[-1] == stem + ".md" and named.search(p)]
    if len(hits) != 1:
        return False, "%s%s names %s tracked widen record" % (WIDENED_LEAD, stem, len(hits) or "no")
    path = hits[0]
    try:
        text = pathlib.Path(root, path).read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return False, "%s does not read: %s" % (path, exc)
    fields, bad, _name = read_record(path, text, WIDEN_KIND)
    if bad:
        return False, "%s: %s" % (path, "; ".join("%s %s" % kv for kv in bad))
    if fields["Population"].strip("`") != reg.population:
        return False, "%s names population %s, not %s" % (path, fields["Population"], reg.population)
    if key not in parse_widen_keys(fields["Keys"]):
        return False, "%s does not hold the key in its Keys" % path
    if policy == "refuse":
        rc = LL._run_git(root, "cat-file", "-e", "%s:%s" % (sha, path))[0] if sha else 1
        if rc != 0:
            return False, "%s is refuse and the base does not track %s" % (WIDEN_KEY, path)
    return True, path


def read_seed_rows(root, reg):
    """-> (measured rows, reason): the registration's seed run once through the factory's seed run, its
    stdout read as measured rows; `reason` non-empty for a failed or dead-probe seed or a bad row."""
    out, reason = LL.run_seed_argv(reg.seed, root)
    if reason:
        return {}, reason
    at = tuple(i for i, f in enumerate(reg.fields) if f in reg.verbatim)
    rows, bad = LL._parse_rows(out.split("\n"), len(reg.fields), (), at)
    if bad:
        return {}, "seed printed %s" % LL.render_malformed(bad[0]).replace("\t", " ")
    return rows, ""


def read_base_rows(root, reg, sha, why):
    """-> (the rows at the base, each `site` row re-keyed through the base range's renames, or None, why)."""
    if not sha:
        return None, why
    rc, text = LL._run_git(root, "show", "%s:./%s" % (sha, reg.home))
    if rc != 0:
        return None, "no %s at %s (%s)" % (reg.home, sha[:12], why)
    at = tuple(i for i, f in enumerate(reg.fields) if f in reg.verbatim)
    base, bad = LL._parse_rows(text.split("\n"), len(reg.fields), ("sha", "disposition"), at)
    if bad:
        return None, "%s does not parse at %s: %s" % (reg.home, sha[:12], LL.render_malformed(bad[0]))
    rows, _applied = LL._derive_rekeyed_rows(reg, base, LL.read_renames(root, sha))
    return rows, why


def derive_leg_population(regs, verb):
    """-> (the registrations `verb`'s leg grades, why it grades none)."""
    if verb == "both-ways":
        return [r for r in regs if r.leg == LEGS[verb]], "no registration names this leg"
    if verb == "rename":
        return [r for r in regs if r.key == "site"], "no site population is registered"
    if verb == "keys-not-scalar":
        return [r for r in regs if r.population == SCALAR_POPULATION], "no %s registration" % SCALAR_POPULATION
    return list(regs), "no [[ledger]] registration in this tree"


def render_unresolved(why, sha):
    """An `unresolved` line's reason: `why` alone where a base resolved, else `why` and the remedy."""
    return str(why) if sha else "%s · %s" % (why, NO_BASE_REMEDY)


def print_verdict(leg, red, graded, sha=None, why=""):
    """The leg's closing line: red, or its pass line naming what it graded. -> its exit."""
    against = " against %s (%s)" % (sha[:12], why) if sha else ""
    print_line(leg, "red" if red else "pass", "%d populations graded%s" % (graded, against))
    return 1 if red else 0


def run_never_gains(root):
    """`ratchet (never gains)`: every refusal `compare_to_base` names, and every widened row of a
    `shrink-only` or `ceiling` population `retrofit.widen` does not admit."""
    leg = LEGS["never-gains"]
    regs = LL.read_registrations(root)
    if not regs:
        print_line("unarmed", leg, derive_leg_population(regs, "never-gains")[1])
        return 0
    sha, why = LL.resolve_compare_base(root)
    policy = tracked = None
    red = 0
    for reg in regs:
        if sha and check_new_at_base(root, reg, sha):
            print_line(leg, reg.population, "new at %s" % sha[:12], "%d rows" % measure_rows(root, reg))
            continue
        if sha and check_regrammared_at_base(root, reg, sha):
            print_line(leg, reg.population, "regrammared at %s" % sha[:12], "%d rows" % measure_rows(root, reg))
            continue
        findings, why_not = LL.compare_to_base(root, reg)
        if findings is None:
            print_line(leg, reg.population, "unresolved", render_unresolved(why_not, sha))
            red = 1
            continue
        rows, _bad = LL.read_ledger(root, reg)
        admitted = {}
        for key, (_count, values, *_rest) in sorted(rows.items()):
            if reg.direction not in WIDEN_DIRECTIONS or not values[-1].startswith(WIDENED_LEAD):
                continue
            policy = read_widen_policy(root) if policy is None else policy
            tracked = read_tracked_paths(root) if tracked is None else tracked
            ok, what = check_widen_admitted(root, reg, key, values[-1][len(WIDENED_LEAD):], policy, sha, tracked)
            admitted[key] = ok
            print_line(leg, reg.population, "widened", render_key(key),
                       ("admitted by %s" % what) if ok else ("not admitted: %s" % what))
            red = red or (0 if ok else 1)
        for name, key in findings:
            if name == "above ceiling" and admitted.get(key):
                continue
            print_line(leg, reg.population, name, render_key(key))
            red = 1
        print_line(leg, reg.population, "%d rows" % len(rows))
    return print_verdict(leg, red, len(regs), sha, why)


def run_both_ways(root):
    """`ratchet (both ways)`: each registration naming this leg has its seed run at HEAD against its rows
    through `compare_counts`; one naming another leg is printed `graded by <leg>` and never run here."""
    leg = LEGS["both-ways"]
    regs = LL.read_registrations(root)
    own, why = derive_leg_population(regs, "both-ways")
    for reg in regs:
        if reg.leg != leg:
            print_line(leg, reg.population, "graded by %s" % reg.leg)
    if not own:
        print_line("unarmed", leg, why)
        return 0
    red = graded = 0
    for reg in own:
        state = LL.read_home_state(pathlib.Path(root, reg.home))
        if not reg.seed or state != "armed":
            print_line("unarmed", leg, reg.population, "seed = []" if not reg.seed else "home %s" % state)
            continue
        declared, bad = LL.read_ledger(root, reg)
        if bad:
            print_line(leg, reg.population, "unresolved", LL.render_malformed(bad[0]))
            red = 1
            continue
        measured, reason = read_seed_rows(root, reg)
        if reason:
            print_line(leg, reg.population, "unresolved", "seed %s" % reason)
            red = 1
            continue
        if not measured and not declared:
            print_line("unarmed", leg, reg.population, "empty: no row and nothing measured")
            continue
        graded += 1
        for name, key, have, want in LL.compare_counts({k: r[0] for k, r in measured.items()},
                                                        {k: r[0] for k, r in declared.items()}, reg.direction):
            print_line(leg, reg.population, name, render_key(key), "measured %s, declared %s" % (have, want))
            red = 1
        print_line(leg, reg.population, "%d rows, %d measured" % (len(declared), len(measured)))
    if red or graded:
        return print_verdict(leg, red, graded)
    return 0


def run_unarmed(root):
    """`ratchet (unarmed)`: a registration with `seed = []`, or whose home `read_home_state` reads
    unarmed, reads unarmed: red where its home holds rows, so it would read armed."""
    leg = LEGS["unarmed"]
    regs = LL.read_registrations(root)
    if not regs:
        print_line("unarmed", leg, derive_leg_population(regs, "unarmed")[1])
        return 0
    red = 0
    for reg in regs:
        state = LL.read_home_state(pathlib.Path(root, reg.home))
        why = ("seed = []" if not reg.seed else "its home records a failed seed" if state == "unarmed"
               else "no home, never seeded" if state == "absent" else "")
        if not why:
            continue
        rows = LL.read_ledger(root, reg)[0] if state != "absent" else {}
        if rows:
            print_line(leg, reg.population, "reads armed", "%s, yet its home holds %d rows" % (why, len(rows)))
            red = 1
        else:
            print_line("unarmed", reg.population, why)
    return print_verdict(leg, red, len(regs))


def run_populated(root):
    """`ratchet (populated)`: an armed home holding no row after a live seed, unless a seen-red line
    names the registration's leg (unit 7 S10): the seen-red records are read once, at the first such
    home, and the first record listed for the leg is printed as the admission. A refused seen-red line
    is `ValueError`, which `main` exits 2 on."""
    leg = LEGS["populated"]
    regs = LL.read_registrations(root)
    if not regs:
        print_line("unarmed", leg, derive_leg_population(regs, "populated")[1])
        return 0
    red, records = 0, None
    for reg in regs:
        if not reg.seed or LL.read_home_state(pathlib.Path(root, reg.home)) != "armed":
            continue
        rows, bad = LL.read_ledger(root, reg)
        if not rows and not bad:
            if records is None:
                records = read_seen_red_records(root)
            if records.get(reg.leg):
                red_sha, _green, rel, _n = records[reg.leg][0]
                print_line(leg, reg.population, "admitted", "seen red at %s in %s" % (red_sha[:8], rel))
                continue
            print_line(leg, reg.population, "empty", EMPTY_TEXT)
            red = 1
        else:
            print_line(leg, reg.population, "%d rows" % len(rows))
    return print_verdict(leg, red, len(regs))


def read_base_paths(root, sha, seen):
    """Fill `seen` once per run: the base's tracked paths (None when the base does not list), the widen
    policy and the working tree's tracked paths, which `check_marker_repaired` and `check_widen_rewrite`
    share."""
    if "base" not in seen:
        rc, out = LL._run_git(root, "ls-tree", "-r", "-z", "--name-only", sha)
        seen.update(base=[p for p in out.split("\0") if p] if rc == 0 else None,
                    policy=read_widen_policy(root), tracked=read_tracked_paths(root))


def check_widen_rewrite(root, reg, key, was, now, sha, seen):
    """-> True when a base row's rewrite is a raise through the door: its disposition moved to a
    `widened:` marker naming a widen record the base's tree does not hold and that `check_widen_admitted`
    admits, so its sha moved with it. `widen` writes exactly this rewrite (the module docstring), and
    `never gains` admits it by the same record; a row re-dated under its base marker, or a marker turned
    back to `seeded`, stays laundering."""
    if reg.direction not in WIDEN_DIRECTIONS or now[1] == was[1] or not now[1].startswith(WIDENED_LEAD):
        return False
    read_base_paths(root, sha, seen)
    named, stem = derive_record_name(WIDEN_KIND), now[1][len(WIDENED_LEAD):]
    if seen["base"] is None or any(p.rsplit("/", 1)[-1] == stem + ".md" and named.search(p) for p in seen["base"]):
        return False
    return check_widen_admitted(root, reg, key, stem, seen["policy"], sha, seen["tracked"])[0]


def check_marker_repaired(root, reg, key, was, now, sha, seen):
    """-> True when a rewritten disposition only repairs a base `widened:` marker that names no widen
    record in the base's tree into one that admits the key now: the rewrite never gains demands, and
    no laundering, since the base row admitted nothing. `seen` caches the policy and both path sets."""
    if reg.direction not in WIDEN_DIRECTIONS or not (was.startswith(WIDENED_LEAD) and now.startswith(WIDENED_LEAD)):
        return False
    read_base_paths(root, sha, seen)
    named, stem = derive_record_name(WIDEN_KIND), was[len(WIDENED_LEAD):]
    if seen["base"] is None or any(p.rsplit("/", 1)[-1] == stem + ".md" and named.search(p) for p in seen["base"]):
        return False
    return check_widen_admitted(root, reg, key, now[len(WIDENED_LEAD):], seen["policy"], sha, seen["tracked"])[0]


def run_seed_laundering(root):
    """`ratchet (seed laundering)`: against the base, a surviving key whose sha or disposition the tree
    rewrote, or a row removed while its seed still measures the key."""
    leg = LEGS["seed-laundering"]
    regs = LL.read_registrations(root)
    if not regs:
        print_line("unarmed", leg, derive_leg_population(regs, "seed-laundering")[1])
        return 0
    sha, why = LL.resolve_compare_base(root)
    red, seen = 0, {}
    for reg in regs:
        if sha and check_new_at_base(root, reg, sha):
            print_line(leg, reg.population, "new at %s" % sha[:12], "%d rows" % measure_rows(root, reg))
            continue
        if sha and check_regrammared_at_base(root, reg, sha):
            print_line(leg, reg.population, "regrammared at %s" % sha[:12], "%d rows" % measure_rows(root, reg))
            continue
        base, why_not = read_base_rows(root, reg, sha, why)
        try:
            work, bad = LL.read_ledger(root, reg) if base is not None else ({}, [])
        except OSError as exc:
            base, why_not = None, "no %s in the working tree: %s" % (reg.home, exc)
        if base is None or bad:
            print_line(leg, reg.population, "unresolved",
                       render_unresolved(why_not, sha) if base is None else LL.render_malformed(bad[0]))
            red = 1
            continue
        removed = []
        for key, (_count, values, *_rest) in sorted(base.items()):
            if key not in work:
                removed.append(key)
                continue
            now = work[key][1]
            if check_widen_rewrite(root, reg, key, values, now, sha, seen):
                print_line(leg, reg.population, "widened", render_key(key), "%s -> %s" % (values[1], now[1]))
                continue
            if now[0] != values[0]:
                print_line(leg, reg.population, "re-dated", render_key(key), "%s -> %s" % (values[0], now[0]))
                red = 1
            if now[1] != values[1] and check_marker_repaired(root, reg, key, values[1], now[1], sha, seen):
                print_line(leg, reg.population, "marker repaired", render_key(key), "%s -> %s" % (values[1], now[1]))
            elif now[1] != values[1]:
                print_line(leg, reg.population, "disposition rewritten", render_key(key),
                           "%s -> %s" % (values[1], now[1]))
                red = 1
        if removed and reg.seed:
            measured, reason = read_seed_rows(root, reg)
            if reason:
                print_line(leg, reg.population, "unresolved", "seed %s" % reason)
                red = 1
            for key in removed if not reason else ():
                if key in measured:
                    print_line(leg, reg.population, "removed while its seed still measures it", render_key(key))
                    red = 1
        print_line(leg, reg.population, "%d rows, %d at the base" % (len(work), len(base)))
    return print_verdict(leg, red, len(regs), sha, why)


def run_rename(root):
    """`ratchet (rename)`: over the base range, a `git mv` of a file holding `site` rows that
    `carry_renames` would still re-key, so the rows read as a gain or a drain."""
    leg = LEGS["rename"]
    sites, why_none = derive_leg_population(LL.read_registrations(root), "rename")
    if not sites:
        print_line("unarmed", leg, why_none)
        return 0
    sha, why = LL.resolve_compare_base(root)
    red = 0
    for reg in sites:
        if not sha:
            print_line(leg, reg.population, "unresolved", render_unresolved(why, sha))
            red = 1
            continue
        if check_new_at_base(root, reg, sha):
            print_line(leg, reg.population, "new at %s" % sha[:12], "%d rows" % measure_rows(root, reg))
            continue
        if check_regrammared_at_base(root, reg, sha):
            print_line(leg, reg.population, "regrammared at %s" % sha[:12], "%d rows" % measure_rows(root, reg))
            continue
        try:
            rows, applied = LL.carry_renames(root, reg, sha)
        except (OSError, ValueError) as exc:
            print_line(leg, reg.population, "unresolved", exc)
            red = 1
            continue
        for old, new in applied:
            print_line(leg, reg.population, "rename %s -> %s" % (old, new), "its rows are still keyed on %s" % old)
            red = 1
        print_line(leg, reg.population, "%d rows" % len(rows))
    return print_verdict(leg, red, len(sites), sha, why)


def read_root_confs(root):
    """-> the root confs in the working tree of `root`, each a `.<name>.conf`, tracked or not: what
    `git ls-files --cached --others --exclude-standard -- ':(glob).*.conf'` lists, so a conf an adopter has
    copied but not yet committed is read before its first commit (TOOL-dWitnessedBar-52 S1). The glob
    magic keeps `*` from crossing `/`, so a nested conf is not one. Each listed path is kept once, and
    only when it is a regular file in the work tree: a staged conf removed from the work tree is
    printed `not in the work tree <path>` on stderr and not read (TOOL-dWitnessedBar-62 S23). WHAT IT
    DOES NOT CHECK: a root conf the repository ignores is never read, so a pin assigned only in a
    machine-local ignored conf is neither seeded nor held."""
    rc, out = LL._run_git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--",
                          ":(glob).*.conf")
    if rc != 0:
        raise ValueError("git ls-files of the root confs failed at %s" % root)
    kept = []
    for p in sorted({p for p in out.split("\0") if p}):
        if pathlib.Path(root, p).is_file():
            kept.append(p)
        else:
            print("not in the work tree %s" % p, file=sys.stderr)
    return kept


def read_root_conf_lines(root):
    """-> [(conf, line)]: each line of the root confs in the working tree that `read_root_confs` lists,
    the one conf walk `measure_scalar_pins` and `measure_cutoffs` share (TOOL-dWitnessedBar-17 S6)."""
    out = []
    for conf in read_root_confs(root):
        try:
            text = pathlib.Path(root, conf).read_bytes().decode("utf-8", "replace")
        except OSError:
            continue
        out.extend((conf, line) for line in text.splitlines())
    return out


def measure_scalar_pins(root):
    """-> {(conf, key): count}: every `<KEY>=` assignment of a `*_PIN` key at a line's start in the
    root confs in the working tree that `read_root_confs` lists."""
    counts = {}
    for conf, line in read_root_conf_lines(root):
        m = PIN_RE.match(line)
        if m:
            counts[(conf, m.group(1))] = counts.get((conf, m.group(1)), 0) + 1
    return counts


def measure_cutoffs(root):
    """-> {(conf, key): date}: every `*_CUTOFF` key assigned at a line's start in the
    root confs in the working tree that `read_root_confs` lists, its date the last assignment's `YYYY-MM-DD` as eight digits and a blank one
    `BLANK_CUTOFF`, the `date-cutoffs` seed (TOOL-dWitnessedBar-17 S6). A value that is neither blank
    nor a real `%Y-%m-%d` day, `none` say, reads as `BLANK_CUTOFF` too, with one stderr line naming the
    conf and key, so a malformed cutoff reads as the latest one and its row's `count rose`, never as a
    seed that died (TOOL-dWitnessedBar-51 S37)."""
    dates = {}
    for conf, line in read_root_conf_lines(root):
        if not CUTOFF_RE.match(line):
            continue
        key, value = parse_conf_line(line)
        if not value:
            dates[(conf, key)] = BLANK_CUTOFF
            continue
        try:
            dates[(conf, key)] = int(datetime.datetime.strptime(value, "%Y-%m-%d").strftime("%Y%m%d"))
        except ValueError:
            print("%s: %s: %s=%r is neither a YYYY-MM-DD date nor blank, read as %d"
                  % (SAY, conf, key, value, BLANK_CUTOFF), file=sys.stderr)
            dates[(conf, key)] = BLANK_CUTOFF
    return dates


def run_measure_cutoffs(root):
    """`measure-cutoffs`: one `<conf> TAB <key> TAB <date>` row per measured cutoff, the seed's output."""
    for (conf, key), date in sorted(measure_cutoffs(root).items()):
        print("%s\t%s\t%d" % (conf, key, date))
    return 0


def render_seed_command(root):
    """The command that seeds `conf-scalar-pins` from this kit's copy of the ledger factory, its path
    spelled from `root` (TOOL-dWitnessedBar-46 S3)."""
    try:
        kit = pathlib.Path(os.path.relpath(KIT, root)).as_posix()
    except ValueError:  # another drive on Windows
        kit = KIT.as_posix()
    return "python %s/legacy_ledger.py seed --population %s" % (kit, SCALAR_POPULATION)


def run_keys_not_scalar(root, measure=False):
    """`ratchet (keys, not a scalar)`: the measured pins against `conf-scalar-pins` at HEAD through
    `compare_counts`; `--measure` prints the measurement, the population's seed. An absent, unarmed or
    unregistered `conf-scalar-pins` is never green: it exits 1 printing `unarmed conf-scalar-pins` and
    the seed command (TOOL-dWitnessedBar-46 S3), so an adopter's failed seed reds rather than passes.
    An armed home holding zero rows while a root conf assigns a pin is an empty seed, never an unheld
    pin owed a widen record: it exits 1 printing `empty seed conf-scalar-pins` and the re-seed remedy,
    removing the home and running the seed command (TOOL-dWitnessedBar-57 S9). The home's state is read
    through the factory's `read_home_state` alone (S10)."""
    measured = measure_scalar_pins(root)
    if measure:
        for (conf, key), n in sorted(measured.items()):
            print("%s\t%s\t%d" % (conf, key, n))
        return 0
    leg = LEGS["keys-not-scalar"]
    regs, why = derive_leg_population(LL.read_registrations(root), "keys-not-scalar")
    state = LL.read_home_state(pathlib.Path(root, regs[0].home)) if regs else ""
    if state != "armed":
        print_line(leg, "unarmed %s" % SCALAR_POPULATION, why if not regs else "its home is %s" % state,
                   "seed it: %s" % render_seed_command(root))
        return 1
    reg = regs[0]
    declared, bad = LL.read_ledger(root, reg)
    if bad:
        print_line(leg, reg.population, "unresolved", LL.render_malformed(bad[0]))
        return 1
    if not declared and measured:
        print_line(leg, "empty seed %s" % SCALAR_POPULATION,
                   "its armed home %s holds no row while %d pin(s) are assigned" % (reg.home, len(measured)),
                   "re-seed it: remove %s, then run %s" % (reg.home, render_seed_command(root)))
        return 1
    for key, n in sorted(measured.items()):
        print_line(leg, "held" if key in declared else "unheld", "%s\t%d" % (render_key(key), n))
    red = 0
    for name, key, have, want in LL.compare_counts(measured, {k: r[0] for k, r in declared.items()},
                                                    reg.direction):
        print_line(leg, reg.population, name, render_key(key), "measured %s, declared %s" % (have, want))
        red = 1
    return print_verdict(leg, red, 1)


def run_key_shape(root):
    """`ratchet (key shape)`: a key field holding a number where its kind holds a label, read as the
    factory's line-number refusal over every population."""
    leg = LEGS["key-shape"]
    regs = LL.read_registrations(root)
    if not regs:
        print_line("unarmed", leg, derive_leg_population(regs, "key-shape")[1])
        return 0
    red = 0
    for reg in regs:
        if LL.read_home_state(pathlib.Path(root, reg.home)) == "absent":
            continue
        rows, bad = LL.read_ledger(root, reg)
        for entry in bad:
            if entry[1] == "line-number":
                print_line(leg, reg.population, LL.render_malformed(entry))
                red = 1
        print_line(leg, reg.population, "%d rows" % len(rows))
    return print_verdict(leg, red, len(regs))


def derive_build_slug(unit):
    """The build a unit id names, its middle segment; ValueError for no unit id."""
    m = UNIT_RE.fullmatch(unit)
    if not m:
        raise ValueError("--unit %r is not a unit id" % unit)
    return m.group(1)


def run_widen(root, args):
    """The widen door: one widen record and one `widened:<record stem>` row per key. -> exit."""
    usage = "usage: ratchet.py widen <population> --key <k> [--key <k>] --reason <text> --unit <id>"
    population, keys, reason, unit, i = (args[0] if args and not args[0].startswith("--") else None), [], None, None, 1
    while population is not None and i < len(args):
        if args[i] == "--key" and i + 1 < len(args):
            keys.append(args[i + 1])
        elif args[i] in ("--reason", "--unit") and i + 1 < len(args) and \
                (reason if args[i] == "--reason" else unit) is None:
            reason, unit = (args[i + 1], unit) if args[i] == "--reason" else (reason, args[i + 1])
        else:
            population = None
            break
        i += 2
    if population is None or not keys or reason is None or unit is None:
        print(usage, file=sys.stderr)
        return 2
    regs = [r for r in LL.read_registrations(root) if r.population == population]
    if len(regs) != 1:
        raise ValueError("%d registrations name %r; widen names exactly one" % (len(regs), population))
    reg = regs[0]
    build = derive_build_slug(unit)
    from backlog import check_line_break  # noqa: E402  the kit's one line-break rule (TOOL-dTotalRecall-43 S37)
    if not reason.strip() or check_line_break("--reason", reason):
        raise ValueError("--reason is one non-empty line")
    parsed = []
    for k in keys:
        key = tuple(f.strip() for f in k.split("\t"))
        if len(key) != len(reg.fields) or not all(key) or "`" in k or check_line_break("--key", k):
            raise ValueError("--key %r is not %d TAB-separated fields (%s) with no backtick"
                             % (k, len(reg.fields), ", ".join(reg.fields)))
        parsed.append(key)
    state = LL.read_home_state(pathlib.Path(root, reg.home))
    if state != "armed":
        raise ValueError("%s is %s; a widen raises a seeded population" % (reg.home, state))
    rows, bad = LL.read_ledger(root, reg)
    if bad:
        raise ValueError("%s: %s" % (reg.home, LL.render_malformed(bad[0])))
    if read_widen_policy(root) == "refuse":
        print("%s: %s is refuse, so no widen record and no widened row is written" % (SAY, WIDEN_KEY),
              file=sys.stderr)
        return 2
    sha, no_head = LL.read_head_sha(root)
    if sha is None:
        raise ValueError(no_head)
    fields = [("Population", population), ("Keys", ", ".join("`%s`" % render_key(k) for k in parsed)),
              ("Reason", reason.strip()), ("Caused-by", unit)]
    path = write_record(root, build, unit, WIDEN_KIND, "%s widened" % population, fields)
    stem = pathlib.PurePosixPath(path).stem
    out = {k: (r[0], r[1]) for k, r in rows.items()}
    for key in parsed:
        out[key] = (out[key][0] + 1 if key in out else 1, (sha, WIDENED_LEAD + stem))
    LL.write_rows(root, reg, out)
    print_line("widened", population, path, "%d keys" % len(parsed))
    return 0


def run_list(root):
    """Each pack row, the leg that holds it, and whether it grades anything here."""
    regs = LL.read_registrations(root)
    for row, verb in PACK_ROWS:
        if verb is None:
            print_line("unarmed", TOUCH_JOIN)
        elif verb == "--fixture":
            print_line("fixture", SELFTEST_LEG, row)
        else:
            graded, why = derive_leg_population(regs, verb)
            if graded:
                print_line("armed", LEGS[verb], "%d populations" % len(graded))
            else:
                print_line("unarmed", LEGS[verb], why)
    return 0


# ------------------------------------------------------------------------------------------- the fixture
FIXTURE_ENV = {k: v for k, v in os.environ.items()
               if not k.startswith("GIT_") and k not in ("GOV_REMOTE", "GOV_DEFAULT_BRANCH")}
SHA_A, SHA_B = "a" * 12, "b" * 12
FIX_UNIT = "TOOL-dFix-1"
FIX_RECORD = "memory/builds/dFix/build/2026-01-01-build-TOOL-dFix-1-widen-1.md"


def run_git_in(top, *args):
    """One git call in a fixture repository; RuntimeError naming it on failure."""
    p = subprocess.run(["git", "-C", str(top), *args], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=FIXTURE_ENV, stdin=subprocess.DEVNULL)
    if p.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args), (p.stderr or p.stdout).strip()))
    return p.stdout


def render_table(population="fix-pop", leg=LEGS["never-gains"], seed=None, key="key", fields=("name",),
                 direction="shrink-only", home="pop/rows.txt"):
    """One `[[ledger]]` table's TOML; the seed defaults to one printing nothing."""
    table = {"population": population, "leg": leg, "seed": seed or [sys.executable, "-c", "pass"],
             "key": key, "fields": list(fields), "drain": "key", "direction": direction, "home": home}
    return "[[ledger]]\n" + "".join("%s = %s\n" % (k, json.dumps(v)) for k, v in table.items()) + "\n"


def render_seed(code):
    """A fixture seed argv: this interpreter running `code`."""
    return [sys.executable, "-c", code]


def render_rows(rows, population="fix-pop", key="key", fields=("name",), direction="shrink-only", extra=()):
    """A ledger file: its header, any `extra` lines, then `(key, count, sha, disposition)` per row."""
    reg = LL.Registration(population, (), key, tuple(fields), "key", direction, "", "")
    body = ["\t".join([*k, str(n), s, d]) for k, n, s, d in rows]
    return "\n".join([LL.render_header(reg), *extra, *body]) + "\n"


def write_files(top, files):
    """Write each `{path: text}` under `top`, a None text removing the path."""
    for rel, text in files.items():
        p = pathlib.Path(top, rel)
        if text is None:
            p.unlink(missing_ok=True)
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))


FX_REMOTE = "fx"  # the fixtures' scratch remote: a name no real remote of gov is likely to carry


def write_fixture_repo(top, tables, files):
    """A scratch repository at `top`: `kit/kit.toml` holding `tables`, a build folder, and `files`,
    committed as the base on `main`, which the scratch remote's `main` tracking ref names."""
    pathlib.Path(top).mkdir(parents=True)
    write_files(top, {"kit/kit.toml": 'id = "fix"\n\n' + "".join(tables),
                      "memory/builds/dFix/README.md": "# dFix\n", **files})
    run_git_in(top, "init", "-q", "-b", "main")
    for k, v in (("user.email", "fixture@example.invalid"), ("user.name", "fixture"), ("core.autocrlf", "false"),
                 ("commit.gpgsign", "false"), ("core.hooksPath", ".no-hooks")):
        run_git_in(top, "config", k, v)
    run_git_in(top, "add", "-A")
    run_git_in(top, "commit", "-q", "-m", "base")
    run_git_in(top, "remote", "add", FX_REMOTE, "../no-remote")
    run_git_in(top, "update-ref", f"refs/remotes/{FX_REMOTE}/main", "HEAD")
    return top


def render_widen_record(reason="the fixture admits it", key="b", population="fix-pop"):
    """A widen record as the door writes it, for the plants that hand-write one."""
    return ("# %s widen 1 — %s widened\n\n**Serves:** widen %s\n\n- **Population:** %s\n- **Keys:** `%s`\n"
            "- **Reason:** %s\n- **Caused-by:** %s\n" % (FIX_UNIT, population, FIX_UNIT, population, key, reason,
                                                       FIX_UNIT))


def run_leg_cli(top, *args):
    """-> (exit, stdout and stderr) of this file run with `args` in `top`."""
    p = subprocess.run([sys.executable, str(KIT / "ratchet.py"), *args], cwd=str(top), capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=FIXTURE_ENV, stdin=subprocess.DEVNULL)
    return p.returncode, p.stdout + p.stderr


def check_plant_case(results, case, what, top, args, want, needles=(), absent=()):
    """Run one leg in `top` and hold its exit and output; appends PASS or FAIL to `results`."""
    rc, out = run_leg_cli(top, *args)
    missing = [n for n in needles if n not in out] + ["no %r" % a for a in absent if a in out]
    ok = rc == want and not missing
    results.append(ok)
    print_line("PASS" if ok else "FAIL", case, what, "%s exit %d, expected %d" % (args[0], rc, want))
    if not ok:
        print("    missing: %s" % ", ".join(missing) if missing else "    output:")
        print("".join("    | %s\n" % ln for ln in out.splitlines()), end="")
    return out


def run_plant_gain(top, results):
    rows = [(("a",), 1, SHA_A, "seeded")]
    write_fixture_repo(top, [render_table()], {"pop/rows.txt": render_rows(rows)})
    write_files(top, {"pop/rows.txt": render_rows(rows + [(("b",), 1, SHA_A, "seeded")])})
    check_plant_case(results, "gain", "a shrink-only key gained", top, ["never-gains"], 1,
                     ["fix-pop · gained · b"])
    write_files(top, {"pop/rows.txt": render_rows([(("b",), 1, SHA_A, "seeded")])})
    check_plant_case(results, "gain", "a swapped key at an equal count", top, ["never-gains"], 1, ["gained · b"])


def run_plant_ceiling_raised(top, results):
    write_fixture_repo(top, [render_table(direction="ceiling")],
                       {"pop/rows.txt": render_rows([(("a",), 2, SHA_A, "seeded")], direction="ceiling")})
    write_files(top, {"pop/rows.txt": render_rows([(("a",), 3, SHA_A, "seeded")], direction="ceiling")})
    check_plant_case(results, "ceiling-raised", "a ceiling row raised", top, ["never-gains"], 1,
                     ["above ceiling · a"])


def run_plant_append_edited(top, results):
    write_fixture_repo(top, [render_table(direction="append-only")],
                       {"pop/rows.txt": render_rows([(("a",), 1, SHA_A, "seeded")], direction="append-only")})
    write_files(top, {"pop/rows.txt": render_rows([(("a",), 1, SHA_B, "seeded")], direction="append-only")})
    check_plant_case(results, "append-edited", "an append-only base row rewritten", top, ["never-gains"], 1,
                     ["edited · a"])


def run_plant_append_removed(top, results):
    """TOOL-dWitnessedBar-18 AC5: an append-only base row removed, as a landed step's row would be."""
    rows = [(("a",), 1, SHA_A, "seeded"), (("b",), 1, SHA_A, "seeded")]
    write_fixture_repo(top, [render_table(direction="append-only")],
                       {"pop/rows.txt": render_rows(rows, direction="append-only")})
    write_files(top, {"pop/rows.txt": render_rows(rows[:1], direction="append-only")})
    check_plant_case(results, "append-removed", "an append-only base row removed", top, ["never-gains"], 1,
                     ["removed · b"])


def read_widen_paths(top):
    """The widen records under the fixture's build folder."""
    return sorted(p.relative_to(top).as_posix() for p in pathlib.Path(top, "memory/builds/dFix").rglob("*-widen-*.md"))


def run_plant_gain_widened(top, results):
    rows = [(("a",), 1, SHA_A, "seeded")]
    write_fixture_repo(top, [render_table()], {"pop/rows.txt": render_rows(rows)})
    check_plant_case(results, "gain-widened", "the door writes a record and a row", top,
                     ["widen", "fix-pop", "--key", "b", "--reason", "a new offence the fixture admits",
                      "--unit", FIX_UNIT], 0, ["widened · fix-pop"])
    made = read_widen_paths(top)
    if made:
        run_git_in(top, "add", "--", *made)
    check_plant_case(results, "gain-widened", "a tracked record naming the key and a reason", top,
                     ["never-gains"], 0, ["admitted by", "pass"])
    for rel in made[:1]:
        write_files(top, {rel: render_widen_record(reason="")})
    check_plant_case(results, "gain-widened", "the record's Reason empty", top, ["never-gains"], 1,
                     ["not admitted"])
    write_files(top, {"pop/rows.txt": render_rows(rows + [(("b",), 1, SHA_A, "widened:2026-01-01-build-TOOL-dFix-1-widen-9")])})
    check_plant_case(results, "gain-widened", "a widened row naming no tracked record", top, ["never-gains"], 1,
                     ["names no tracked widen record"])


def run_plant_gain_refused(top, results):
    rows = [(("a",), 1, SHA_A, "seeded")]
    policy = {".governance/policy.toml": '[retrofit]\nwiden = "refuse"\n'}
    stem = pathlib.PurePosixPath(FIX_RECORD).stem
    widened = render_rows(rows + [(("b",), 1, SHA_A, WIDENED_LEAD + stem)])
    one = pathlib.Path(top, "refused")
    write_fixture_repo(one, [render_table()], {"pop/rows.txt": render_rows(rows), **policy})
    write_files(one, {FIX_RECORD: render_widen_record(), "pop/rows.txt": widened})
    run_git_in(one, "add", "--", FIX_RECORD)
    check_plant_case(results, "gain-refused", "a widened row under refuse, its record new", one, ["never-gains"], 1,
                     ["is refuse"])
    write_files(one, {FIX_RECORD: None, "pop/rows.txt": render_rows(rows)})
    run_git_in(one, "rm", "-q", "--cached", "--", FIX_RECORD)
    check_plant_case(results, "gain-refused", "the door under refuse", one,
                     ["widen", "fix-pop", "--key", "b", "--reason", "refused", "--unit", FIX_UNIT], 2, ["is refuse"])
    results.append(not read_widen_paths(one) and pathlib.Path(one, "pop/rows.txt").read_text(encoding="utf-8")
                   == render_rows(rows))
    print_line("PASS" if results[-1] else "FAIL", "gain-refused", "the door wrote nothing")
    two = pathlib.Path(top, "landed")
    write_fixture_repo(two, [render_table()], {"pop/rows.txt": render_rows(rows), FIX_RECORD: render_widen_record(),
                                               **policy})
    write_files(two, {"pop/rows.txt": widened})
    check_plant_case(results, "gain-refused", "a widened row whose record the base tracks", two, ["never-gains"], 0,
                     ["admitted by"])


def run_plant_ceiling_widened(top, results):
    write_fixture_repo(top, [render_table(direction="ceiling")],
                       {"pop/rows.txt": render_rows([(("a",), 2, SHA_A, "seeded")], direction="ceiling")})
    check_plant_case(results, "ceiling-widened", "the door raises a ceiling row", top,
                     ["widen", "fix-pop", "--key", "a", "--reason", "the fixture raises it", "--unit", FIX_UNIT], 0)
    run_git_in(top, "add", "--", *read_widen_paths(top))
    check_plant_case(results, "ceiling-widened", "a ceiling row raised with an admitted record", top,
                     ["never-gains"], 0, ["admitted by", "pass"], ["above ceiling"])


def run_plant_both_ways(top, results):
    own = render_table(leg=LEGS["both-ways"], seed=render_seed("print('a\\t1'); print('c\\t1')"))
    rows = render_rows([(("a",), 1, SHA_A, "seeded"), (("b",), 1, SHA_A, "seeded")])
    write_fixture_repo(top, [own], {"pop/rows.txt": rows})
    check_plant_case(results, "both-ways", "a key with no row and a row no seed finds", top, ["both-ways"], 1,
                     ["undeclared site · c", "unmeasured row · b"])
    own = render_table(leg=LEGS["both-ways"], seed=render_seed("print('a\\t1')"))
    other = render_table(population="other-pop", leg="other leg", home="pop/other.txt",
                         seed=render_seed("open('ran.txt', 'w').write('ran'); raise SystemExit(1)"))
    write_files(top, {"kit/kit.toml": 'id = "fix"\n\n' + own + other,
                      "pop/rows.txt": render_rows([(("a",), 1, SHA_A, "seeded")])})
    check_plant_case(results, "both-ways", "another leg's registration", top, ["both-ways"], 0,
                     ["graded by other leg", "pass"])
    results.append(not pathlib.Path(top, "ran.txt").exists())
    print_line("PASS" if results[-1] else "FAIL", "both-ways", "the other leg's seed never ran")
    write_files(top, {"kit/kit.toml": 'id = "fix"\n\n' + other})
    check_plant_case(results, "both-ways", "no registration names the leg", top, ["both-ways"], 0,
                     ["unarmed · ratchet (both ways) · no registration names this leg"], ["pass"])


def write_cutoff_fixture(top):
    """A fixture whose `ceiling` registration is seeded by `measure-cutoffs` over a tracked root conf
    holding one cutoff, its row at that date (TOOL-dWitnessedBar-17 S6)."""
    table = render_table(population="fix-cutoffs", leg=LEGS["both-ways"], key="cutoff", fields=("conf", "key"),
                         direction="ceiling", seed=[sys.executable, str(KIT / "ratchet.py"), "measure-cutoffs"])
    rows = render_rows([((".fix.conf", "FIX_CUTOFF"), 20260102, SHA_A, "seeded")], population="fix-cutoffs",
                       key="cutoff", fields=("conf", "key"), direction="ceiling")
    write_fixture_repo(top, [table], {".fix.conf": 'FIX_CUTOFF="2026-01-02"\n', "pop/rows.txt": rows})


def run_plant_cutoff_later(top, results):
    write_cutoff_fixture(top)
    check_plant_case(results, "cutoff-later", "a cutoff at its row's date", top, ["both-ways"], 0,
                     ["fix-cutoffs · 1 rows, 1 measured", "pass"])
    write_files(top, {".fix.conf": 'FIX_CUTOFF="2026-01-03"\n'})
    check_plant_case(results, "cutoff-later", "a cutoff moved a day later", top, ["both-ways"], 1,
                     ["fix-cutoffs · count rose · .fix.conf\tFIX_CUTOFF"])
    write_files(top, {".fix.conf": 'FIX_CUTOFF="2026-01-01"\n'})
    check_plant_case(results, "cutoff-later", "a cutoff moved a day earlier", top, ["both-ways"], 0,
                     ["pass"], ["count rose"])


def run_plant_cutoff_blank(top, results):
    write_cutoff_fixture(top)
    write_files(top, {".fix.conf": 'FIX_CUTOFF=""\n'})
    check_plant_case(results, "cutoff-blank", "a cutoff blanked reads as 99991231, a raise", top, ["both-ways"], 1,
                     ["fix-cutoffs · count rose · .fix.conf\tFIX_CUTOFF · measured 99991231, declared 20260102"])


def run_plant_cutoff_none(top, results):
    """TOOL-dWitnessedBar-51 S37: a cutoff set to `none`, or to no real day, reads as 99991231, a raise,
    with one stderr line naming the conf and key, where the seed used to die on it."""
    write_cutoff_fixture(top)
    for value in ("none", "2026-02-30"):
        write_files(top, {".fix.conf": 'FIX_CUTOFF="%s"\n' % value})
        check_plant_case(results, "cutoff-none", "a cutoff set to %s reads as 99991231, a raise" % value, top,
                         ["both-ways"], 1,
                         ["fix-cutoffs · count rose · .fix.conf\tFIX_CUTOFF · measured 99991231, declared 20260102"],
                         ["seed exit"])
    check_plant_case(results, "cutoff-none", "the seed names the value it read as the latest", top,
                     ["measure-cutoffs"], 0, [".fix.conf: FIX_CUTOFF='2026-02-30'", ".fix.conf\tFIX_CUTOFF\t99991231"])


def run_plant_no_base_remedy(top, results):
    """TOOL-dWitnessedBar-51 S33: a live base leg with its remote ref deleted exits 1 printing
    `unresolved`, its reason and the remedy."""
    rows = [(("a",), 1, SHA_A, "seeded")]
    write_fixture_repo(top, [render_table()], {"pop/rows.txt": render_rows(rows)})
    run_git_in(top, "update-ref", "-d", f"refs/remotes/{FX_REMOTE}/main")
    check_plant_case(results, "no-base-remedy", "never gains with no compare base", top, ["never-gains"], 1,
                     ["fix-pop · unresolved", NO_BASE_REMEDY], ["pass"])


def run_plant_unarmed_green(top, results):
    rows = [(("a",), 1, SHA_A, "seeded")]
    write_fixture_repo(top, [render_table()], {"pop/rows.txt": render_rows(rows, extra=[LL.UNARMED_LEAD + "exit 1 · "
                                                                                       + SHA_A])})
    check_plant_case(results, "unarmed-green", "a failed seed's home reading armed", top, ["unarmed"], 1,
                     ["reads armed"])
    write_files(top, {"pop/rows.txt": render_rows([], extra=[LL.UNARMED_LEAD + "exit 1 · " + SHA_A])})
    check_plant_case(results, "unarmed-green", "a failed seed's home holding no row", top, ["unarmed"], 0,
                     ["unarmed · fix-pop"])


def run_plant_populated_empty_armed(top, results):
    write_fixture_repo(top, [render_table()], {"pop/rows.txt": render_rows([])})
    check_plant_case(results, "populated-empty-armed", "an armed home holding no row", top, ["populated"], 1,
                     ["fix-pop · empty · " + EMPTY_TEXT])


def run_plant_populated_seen_red(top, results):
    """Unit 7 S10, one fixture three ways: a journal record's seen-red line naming the registration's leg
    admits its empty armed population, exit 0; the line removed, it reads `empty`, exit 1; the line's red
    SHA dropped, the reader refuses it naming the record, exit 2."""
    ledger = "memory/builds/dFix/build/2026-01-01-build-TOOL-dFix-1-1-acceptance-ledger.md"

    def render_ledger(line):
        return ("# %s — acceptance ledger\n\n**Serves:** journal %s\n\n**Evidences:** %s\n"  # census: kept cause-writer fixture: a record head its fixture plants
                "- AC1 — `ratchet.py populated` — observed\n%s\n" % (FIX_UNIT, FIX_UNIT, FIX_UNIT, line))
    seen = "- seen-red — `%s` — red `%s` — green `%s` — the population drained" % (LEGS["never-gains"], SHA_A, SHA_A)
    write_fixture_repo(top, [render_table()], {"pop/rows.txt": render_rows([]), ledger: render_ledger(seen),
                                               ".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\n'})
    check_plant_case(results, "populated-seen-red", "a seen-red line names the leg", top, ["populated"], 0,
                     ["fix-pop · admitted · seen red at %s in %s" % (SHA_A[:8], ledger)], ["empty"])
    write_files(top, {ledger: render_ledger("")})
    check_plant_case(results, "populated-seen-red", "the seen-red line removed", top, ["populated"], 1,
                     ["fix-pop · empty · " + EMPTY_TEXT], ["admitted"])
    write_files(top, {ledger: render_ledger(seen.replace("red `%s` — green" % SHA_A, "green"))})
    check_plant_case(results, "populated-seen-red", "the seen-red line's red SHA dropped", top, ["populated"], 2,
                     [ledger], ["admitted"])


def run_plant_laundering(top, results):
    def build_row(name, sha=SHA_A, disposition="seeded"):
        return ((name,), 1, sha, disposition)
    base = [build_row("alpha"), build_row("beta", disposition="keep:ASK-1"), build_row("gamma"), build_row("nul", sha=LL.NULL_SHA)]
    seed = render_seed("print('alpha\\t1'); print('beta\\t1'); print('nul\\t1')")
    write_fixture_repo(top, [render_table(seed=seed)], {"pop/rows.txt": render_rows(base)})
    write_files(top, {"pop/rows.txt": render_rows([build_row("alpha", sha=SHA_B), build_row("beta"), build_row("gamma"),
                                                   build_row("nul", sha=SHA_B)])})
    check_plant_case(results, "laundering", "a re-dated row and a disposition turned back to seeded", top,
                     ["seed-laundering"], 1, ["re-dated · alpha", "disposition rewritten · beta", "re-dated · nul"])
    write_files(top, {"pop/rows.txt": render_rows([base[0], base[1], base[3]])})
    check_plant_case(results, "laundering", "a row drained because its seed no longer measures it", top,
                     ["seed-laundering"], 0, ["pass"])
    write_files(top, {"pop/rows.txt": render_rows(base[1:])})
    check_plant_case(results, "laundering", "a row removed while its seed still measures it", top,
                     ["seed-laundering"], 1, ["removed while its seed still measures it · alpha"])
    stem = pathlib.PurePosixPath(FIX_RECORD).stem
    widened = render_rows([build_row("alpha", sha=SHA_B, disposition=WIDENED_LEAD + stem)] + base[1:])
    write_files(top, {FIX_RECORD: render_widen_record(key="alpha"), "pop/rows.txt": widened})
    run_git_in(top, "add", "--", FIX_RECORD)
    check_plant_case(results, "laundering", "a row raised through a tracked widen record", top,
                     ["seed-laundering"], 0, ["widened · alpha"], ["re-dated · alpha"])
    write_files(top, {FIX_RECORD: None})
    run_git_in(top, "rm", "-q", "--cached", "--", FIX_RECORD)
    check_plant_case(results, "laundering", "the same rewrite with its widen record gone", top,
                     ["seed-laundering"], 1, ["re-dated · alpha", "disposition rewritten · alpha"])


def run_plant_rename(top, results):
    def render_case_rows(path):
        return render_rows([((path, "r1"), 1, SHA_A, "seeded")], key="site", fields=("path", "rule"))
    write_fixture_repo(top, [render_table(leg=LEGS["rename"], key="site", fields=("path", "rule"))],
                       {"pop/rows.txt": render_case_rows("src/x.sh"), "src/x.sh": "".join("echo line %d\n" % n for n in range(20))})
    run_git_in(top, "mv", "src/x.sh", "src/y.sh")
    write_files(top, {"pop/rows.txt": render_case_rows("src/y.sh")})
    check_plant_case(results, "rename", "a staged git mv with its rows re-keyed", top, ["rename"], 0, ["pass"])
    write_files(top, {"pop/rows.txt": render_case_rows("src/x.sh")})
    check_plant_case(results, "rename", "the rows left on the old path", top, ["rename"], 1,
                     ["rename src/x.sh -> src/y.sh"])


def run_plant_key_number(top, results):
    write_fixture_repo(top, [render_table()], {"pop/rows.txt": render_rows([(("412",), 1, SHA_A, "seeded")])})
    check_plant_case(results, "key-number", "a key field holding 412", top, ["key-shape"], 1, ["412"])


def run_plant_untouched_quiet(top, results):
    site = {"key": "site", "fields": ("path", "rule")}
    base = [(("src/old.sh", "r1"), 1, SHA_A, "seeded")]
    write_fixture_repo(top, [render_table(**site)], {"pop/rows.txt": render_rows(base, **site),
                                                     "src/old.sh": "old\n", "src/new.sh": "new\n"})
    write_files(top, {"src/new.sh": "new\nedited in the unit's hunk\n"})
    check_plant_case(results, "untouched-quiet", "a baselined offence outside the unit's hunks", top,
                     ["never-gains"], 0, ["pass"])
    write_files(top, {"pop/rows.txt": render_rows(base + [(("src/new.sh", "r1"), 1, SHA_B, "seeded")], **site)})
    check_plant_case(results, "untouched-quiet", "an unbaselined offence planted in the unit's hunk", top,
                     ["never-gains"], 1, ["gained · src/new.sh"])


def run_plant_merge(top, results):
    seed = render_seed("import os; [print(n + '\\t1') for n in sorted(os.listdir('off'))]")
    names = ("a", "b", "c")
    def render_case_rows(keep):
        return render_rows([((n,), 1, SHA_A, "seeded") for n in keep])
    write_fixture_repo(top, [render_table(leg=LEGS["both-ways"], seed=seed)],
                       {"pop/rows.txt": render_case_rows(names), ".gitattributes": "pop/rows.txt merge=rows\n",
                        **{"off/" + n: "offence %s\n" % n for n in names}})
    run_git_in(top, "config", "merge.rows.driver", "bash '%s/merge-rows.sh' %%O %%A %%B %%P" % KIT.as_posix())
    for branch, drained in (("x", "a"), ("y", "b")):
        run_git_in(top, "checkout", "-q", "-b", branch, "main")
        write_files(top, {"off/" + drained: None, "pop/rows.txt": render_case_rows([n for n in names if n != drained])})
        run_git_in(top, "commit", "-q", "-a", "-m", "drain " + drained)
    run_git_in(top, "checkout", "-q", "x")
    try:
        run_git_in(top, "merge", "-q", "--no-edit", "y")
        merged = pathlib.Path(top, "pop/rows.txt").read_bytes().decode("utf-8") == render_case_rows(["c"])
    except RuntimeError as exc:
        print("    | %s" % exc)
        merged = False
    results.append(merged)
    print_line("PASS" if merged else "FAIL", "merge", "two drains merge through merge-rows.sh to one row")
    check_plant_case(results, "merge", "never gains over the merge", top, ["never-gains"], 0, ["pass"])
    check_plant_case(results, "merge", "both ways over the merge", top, ["both-ways"], 0, ["pass"])


def run_plant_new_population(top, results):
    write_fixture_repo(top, [], {})
    write_files(top, {"kit/kit.toml": 'id = "fix"\n\n' + render_table(),
                      "pop/rows.txt": render_rows([(("a",), 1, SHA_A, "seeded"), (("b",), 1, SHA_A, "seeded")])})
    check_plant_case(results, "new-population", "never gains over a population the base lacks", top,
                     ["never-gains"], 0, ["new at", "2 rows"])
    check_plant_case(results, "new-population", "seed laundering over it", top, ["seed-laundering"], 0, ["new at"])


def run_plant_home_moved(top, results):
    write_fixture_repo(top, [render_table(home="old/rows.txt")],
                       {"old/rows.txt": render_rows([(("a",), 1, SHA_A, "seeded")])})
    pathlib.Path(top, "pop").mkdir()
    run_git_in(top, "mv", "old/rows.txt", "pop/rows.txt")
    write_files(top, {"kit/kit.toml": 'id = "fix"\n\n' + render_table()})
    check_plant_case(results, "home-moved", "the base holds the header at another path", top, ["never-gains"], 1,
                     ["unresolved"], ["new at"])


def run_plant_regrammared(top, results):
    """S11 (TOOL-dWitnessedBar-16): a registration whose home the base holds in a legacy grammar reads
    `regrammared at` with its row count under `never gains` and `seed laundering`, never `unresolved`;
    the same home whose base opens with a ledger header is graded, and its gained key reds."""
    write_fixture_repo(top, [], {"pop/rows.txt": "a\tthe legacy grammar, a reason column\n"})
    write_files(top, {"kit/kit.toml": 'id = "fix"\n\n' + render_table(),
                      "pop/rows.txt": render_rows([(("a",), 1, SHA_A, "seeded"), (("b",), 1, SHA_A, "seeded")])})
    check_plant_case(results, "regrammared", "never gains over a legacy base home", top, ["never-gains"], 0,
                     ["regrammared at", "2 rows"], ["unresolved"])
    check_plant_case(results, "regrammared", "seed laundering over it", top, ["seed-laundering"], 0,
                     ["regrammared at"], ["unresolved"])
    run_git_in(top, "add", "-A")
    run_git_in(top, "commit", "-q", "-m", "the base home regrammared")
    run_git_in(top, "update-ref", f"refs/remotes/{FX_REMOTE}/main", "HEAD")
    write_files(top, {"pop/rows.txt": render_rows([(("a",), 1, SHA_A, "seeded"), (("b",), 1, SHA_A, "seeded"),
                                                   (("c",), 1, SHA_A, "seeded")])})
    check_plant_case(results, "regrammared", "a ledger-headed base home is graded, not regrammared", top,
                     ["never-gains"], 1, ["gained · c"], ["regrammared at"])


def write_scalar_fixture(top):
    """A fixture registering `conf-scalar-pins`, its seed `keys-not-scalar --measure`, over a tracked root
    `.fix.conf` assigning `BAR_PIN`, the conf every measure must still read, its one row holding that pin."""
    table = render_table(population=SCALAR_POPULATION, leg=LEGS["keys-not-scalar"], fields=("conf", "key"),
                         seed=[sys.executable, str(KIT / "ratchet.py"), "keys-not-scalar", "--measure"])
    rows = render_rows([((".fix.conf", "BAR_PIN"), 1, SHA_A, "seeded")], population=SCALAR_POPULATION,
                       fields=("conf", "key"))
    write_fixture_repo(top, [table], {".fix.conf": 'BAR_PIN="1"\n', "pop/rows.txt": rows})


def run_plant_untracked_conf(top, results):
    """S1 (TOOL-dWitnessedBar-52): an untracked root conf is measured, by the seed and by the leg."""
    write_scalar_fixture(top)
    write_files(top, {".x.conf": 'FOO_PIN="3"\n'})
    check_plant_case(results, "untracked-conf", "an untracked root conf in the seed's measure", top,
                     ["keys-not-scalar", "--measure"], 0, [".x.conf\tFOO_PIN\t1", ".fix.conf\tBAR_PIN\t1"])
    check_plant_case(results, "untracked-conf", "its pin with no population row", top, ["keys-not-scalar"], 1,
                     ["undeclared site · .x.conf\tFOO_PIN"], ["undeclared site · .fix.conf"])


def run_plant_deleted_conf(top, results):
    """S23 (TOOL-dWitnessedBar-62): a root conf staged and then removed from the work tree is named
    `not in the work tree` and never opened, by the seed's measure and by the leg."""
    write_scalar_fixture(top)
    write_files(top, {".x.conf": 'FOO_PIN="3"\n'})
    run_git_in(top, "add", "--", ".x.conf")
    write_files(top, {".x.conf": None})
    check_plant_case(results, "deleted-conf", "a staged root conf absent from the work tree, measured", top,
                     ["keys-not-scalar", "--measure"], 0, ["not in the work tree .x.conf", ".fix.conf\tBAR_PIN\t1"],
                     ["Traceback", "FOO_PIN"])
    check_plant_case(results, "deleted-conf", "the leg over it", top, ["keys-not-scalar"], 0,
                     ["not in the work tree .x.conf", "· held · .fix.conf\tBAR_PIN"], ["Traceback", "FOO_PIN"])


def run_plant_ignored_conf(top, results):
    """S3 (TOOL-dWitnessedBar-52): a root conf the repository ignores is never measured."""
    write_scalar_fixture(top)
    write_files(top, {".x.conf": 'FOO_PIN="3"\n', ".git/info/exclude": ".x.conf\n"})
    check_plant_case(results, "ignored-conf", "a root conf named in .git/info/exclude", top,
                     ["keys-not-scalar", "--measure"], 0, [".fix.conf\tBAR_PIN\t1"], [".x.conf"])
    check_plant_case(results, "ignored-conf", "its pin neither held nor graded", top, ["keys-not-scalar"], 0,
                     ["· held · .fix.conf\tBAR_PIN", "pass"], [".x.conf"])


def run_plant_empty_seed(top, results):
    """S9 (TOOL-dWitnessedBar-57): an armed `conf-scalar-pins` holding zero rows beside a conf assigning a
    pin is an empty seed naming the re-seed remedy, never an unheld pin owed a widen record."""
    write_scalar_fixture(top)
    write_files(top, {".fix.conf": 'ROW_DUPLICATE_PIN="0"\n',
                      "pop/rows.txt": render_rows([], population=SCALAR_POPULATION, fields=("conf", "key"))})
    check_plant_case(results, "empty-seed", "an armed empty home beside an assigned pin", top, ["keys-not-scalar"],
                     1, ["empty seed %s" % SCALAR_POPULATION, "re-seed it: remove pop/rows.txt, then run python "],
                     ["unheld", "undeclared site"])


def run_plant_unarmed_home(top, results):
    """S10 (TOOL-dWitnessedBar-57): a `conf-scalar-pins` home opening the factory's `UNARMED_LEAD` reads
    unarmed through its `read_home_state`, and `keys-not-scalar` exits 1 naming it."""
    write_scalar_fixture(top)
    write_files(top, {"pop/rows.txt": LL.UNARMED_LEAD + "exit 1 · " + SHA_A + "\n"})
    check_plant_case(results, "unarmed-home", "a home opening the unarmed line", top, ["keys-not-scalar"], 1,
                     ["unarmed %s" % SCALAR_POPULATION, "its home is unarmed"], ["pass"])


def run_plant_flat_seed(top, results):
    """TOOL-aFlattenedSeed-1 S3: on an install that lands this kit FLAT, a seed argv's `{prefix}/<home>/<file>`
    runs the file its receipt row places, never `<tool root>/<home>/<file>`, which no flat install holds."""
    write_fixture_repo(top, [], {"flat/fxflat.py": 'print("f\\t1")\n', ".governance/install.json": json.dumps(
        {"files": [{"path": "flat/fxflat.py", "source": "tools/fx2/fxflat.py"}]})})
    scripts = pathlib.Path(top, "scripts")
    scripts.mkdir()
    for src in KIT.glob("*.py"):
        shutil.copyfile(src, scripts / src.name)
    code = "import legacy_ledger as L; print(L.run_seed_argv(['python', '{prefix}/fx2/fxflat.py'], '.'))"
    p = subprocess.run([sys.executable, "-c", code], cwd=str(top), capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env={**FIXTURE_ENV, "PYTHONPATH": str(scripts)}, stdin=subprocess.DEVNULL)
    ok = p.returncode == 0 and p.stdout.strip() == repr(("f\t1\n", ""))
    results.append(ok)
    print_line("PASS" if ok else "FAIL", "flat-seed", "a flat install's receipt places a seed argv's kit file",
               "exit %d: %s" % (p.returncode, (p.stdout + p.stderr).strip()[-300:]))


PLANTS = {
    "flat-seed": run_plant_flat_seed,
    "gain": run_plant_gain, "ceiling-raised": run_plant_ceiling_raised, "append-edited": run_plant_append_edited,
    "append-removed": run_plant_append_removed, "gain-widened": run_plant_gain_widened, "gain-refused": run_plant_gain_refused,
    "ceiling-widened": run_plant_ceiling_widened, "both-ways": run_plant_both_ways,
    "cutoff-later": run_plant_cutoff_later, "cutoff-blank": run_plant_cutoff_blank,
    "cutoff-none": run_plant_cutoff_none, "no-base-remedy": run_plant_no_base_remedy,
    "unarmed-green": run_plant_unarmed_green, "populated-empty-armed": run_plant_populated_empty_armed,
    "populated-seen-red": run_plant_populated_seen_red,
    "laundering": run_plant_laundering, "rename": run_plant_rename, "key-number": run_plant_key_number,
    "untouched-quiet": run_plant_untouched_quiet, "merge": run_plant_merge,
    "new-population": run_plant_new_population, "home-moved": run_plant_home_moved,
    "regrammared": run_plant_regrammared, "untracked-conf": run_plant_untracked_conf,
    "ignored-conf": run_plant_ignored_conf, "deleted-conf": run_plant_deleted_conf, "empty-seed": run_plant_empty_seed,
    "unarmed-home": run_plant_unarmed_home,
}


def run_fixture(cases):
    """Each named plant in its own scratch repository. -> 0 when every check held, else 1."""
    results = []
    scratch = tempfile.mkdtemp(prefix="rt")
    try:
        for case in cases:
            try:
                PLANTS[case](pathlib.Path(scratch, case), results)
            except (OSError, RuntimeError, ValueError) as exc:
                results.append(False)
                print_line("FAIL", case, "the plant did not build: %s" % exc)
    finally:
        remove_tree(scratch)
    failed = results.count(False)
    print_line(SELFTEST_LEG, "FAIL" if failed or not results else "PASS",
               "%d cases, %d checks, %d failed" % (len(cases), len(results), failed))
    return 1 if failed or not results else 0


USAGE = ("usage: ratchet.py (%s) | keys-not-scalar --measure | measure-cutoffs | widen <population> --key <k> --reason <text> "
         "--unit <id> | --list | --fixture [--plant <case>]" % " | ".join(LEGS))


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = list(sys.argv[1:] if argv is None else argv)
    if args[:1] == ["--fixture"]:
        init_owned_tempdir()
        if len(args) == 1:
            return run_fixture(list(PLANTS))
        if len(args) == 3 and args[1] == "--plant" and args[2] in PLANTS:
            return run_fixture([args[2]])
        print("%s: --fixture [--plant <case>], the cases: %s" % (SAY, ", ".join(PLANTS)), file=sys.stderr)
        return 2
    verb = args[0] if args else ""
    if not (args == ["--list"] or args == ["measure-cutoffs"]
            or (verb in LEGS and (len(args) == 1 or args == ["keys-not-scalar", "--measure"])) or verb == "widen"):
        print(USAGE, file=sys.stderr)
        return 2
    try:
        root = resolve_root(os.getcwd())
        if verb == "--list":
            return run_list(root)
        if verb == "widen":
            return run_widen(root, args[1:])
        if verb == "measure-cutoffs":
            return run_measure_cutoffs(root)
        if verb == "keys-not-scalar":
            return run_keys_not_scalar(root, measure=len(args) == 2)
        return {"never-gains": run_never_gains, "both-ways": run_both_ways, "unarmed": run_unarmed,
                "populated": run_populated, "seed-laundering": run_seed_laundering, "rename": run_rename,
                "key-shape": run_key_shape}[verb](root)
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        print("%s: %s" % (SAY, exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
