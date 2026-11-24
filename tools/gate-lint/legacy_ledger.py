"""legacy_ledger -- the baseline ledger factory, as this kit carries it (TOOL-dWitnessedBar-13).

The block below is INLINED byte-identically from the canonical copy its marker line names, gov's lib
dir, which ships nothing; `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts.
This kit requires no other kit, so it carries the block itself: `sh_hygiene.py` and
`encoding_posture.py` read their four-field registries through `read_rows` and grade them through
`compare_counts`, each keeping its own messages. Four names the block calls sit outside it, so the
block stays byte-identical: `compute_coverage`, `resolve_compare_base` and `resolve_prefix_token`, from
this kit's own `coverage_join.py`, and `resolve_kit_dir`, through which `seed` finds the policy kit, carried inline
below between its own markers, which the parity table's `resolve_kit_dir` row holds to its canonical.
`scan_bash`, through which a seed argv's `bash` head resolves (TOOL-dWitnessedBar-51 S32), is carried
inline too, as the `resolve_bash_py` block the parity table's row of that name holds.
The CLI lives on the canonical copy and, for `seed` alone, on the memory-tree kit's.
"""
from __future__ import annotations

import os
import pathlib
import re
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import dataclass

from coverage_join import compute_coverage, resolve_compare_base, resolve_prefix_token  # noqa: F401  (the block below calls all three)


# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


# >>> resolve_bash_py -- canonical copy: resolve_bash.py in the gov lib dir (byte-identical; gated)
BASH_NAMES = ("bash.exe", "bash")


def wrong_shell_at(path, wsl):
    """True when `path` is a Windows checkout under WSL: `wsl` set and `path` under a single-letter
    `/mnt/<drive>/`, WSL's mount of a Windows drive (TOOL-dWitnessedBar-27). The twin of the shell
    block `refuse_wrong_shell`'s `wrong_shell_at` in `refuse-wrong-shell.sh` in the gov lib dir; a
    WSL path on its own disk, and any path where no WSL marker is set, is green."""
    p = str(path)
    return bool(wsl) and len(p) > 6 and p.startswith("/mnt/") and "a" <= p[5] <= "z" and p[6] == "/"


def scan_bash(script="", host=""):
    r"""`(found, tried, refusal)`: the bash to run, found by RUNNING each candidate, never by its name.

    GOV_BASH first, and when it is set nothing after it is tried; then Git's own `bin/bash.exe`, the
    third parent of `git --exec-path`; then each PATH directory's BASH_NAMES, a System32 or
    WindowsApps launcher reported and never run. A candidate passes when one run prints `uname -s` as
    its first line and exits 0, `test -f` on `script` included when one is given; on a `windows` host
    the answer must start MINGW or MSYS, so WSL's launcher, which answers `Linux` and drops `$1`, is
    refused under any name (gotcha subprocess-resolves-a-different-shell). Past GOV_BASH every
    candidate is run, `tried` holding one `<candidate>: <why>` for each and a repeat never twice;
    `found` is the first that passed, or "" with `refusal` naming every `tried` line, and the bare name
    `bash` is never returned. `host` is `windows` or `posix`, this host's when empty. No memo: an
    adapter keeps its own, so this stays a function a truth table can call twice. On a `posix` host
    the hosting file is judged first: WSL running it from a Windows checkout under `/mnt/` returns
    no `found`, an empty `tried` and the wrong-shell refusal, before any candidate is tried."""
    host = host or ("windows" if os.name == "nt" else "posix")
    if host == "posix":
        here = os.path.abspath(__file__)
        wsl = bool(os.environ.get("WSL_DISTRO_NAME")) or os.path.exists("/proc/sys/fs/binfmt_misc/WSLInterop")
        if wrong_shell_at(here, wsl):
            return "", [], ("WSL is running " + here + " from a Windows checkout under /mnt/; "
                            "run it with Git's bash (C:/Program Files/Git/bin/bash.exe)")
    tried, seen = [], set()

    def run_probe(cand):
        try:
            r = subprocess.run([cand, "-c", 'uname -s && { [ -z "$1" ] || test -f "$1"; }', "_", str(script)],
                               stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            return "did not run"
        u = r.stdout.decode("utf-8", "replace").replace("\x00", "").split("\n")[0].strip()
        if not u:
            return "did not run"
        if host == "windows" and not u.startswith(("MINGW", "MSYS")):
            return "answered " + u
        return "runs" if r.returncode == 0 else "cannot see " + str(script)

    def check_candidate(cand):
        key = cand.lower() if host == "windows" else cand
        if key in seen:
            return False
        seen.add(key)
        low = cand.lower()
        why = "a launcher" if "/system32/" in low or "/windowsapps/" in low else run_probe(cand)
        tried.append(cand + ": " + why)
        return why == "runs"

    gov = os.environ.get("GOV_BASH", "")
    if gov:
        why = run_probe(gov)
        tried.append(gov + ": " + why)
        if why == "runs":
            return gov, tried, ""
        return "", tried, ("GOV_BASH is set to '" + gov + "' and " + why + ", so nothing after it is tried: "
                           "an override that is set and unusable is refused, never a fall-through")
    try:
        r = subprocess.run(["git", "--exec-path"], stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        ex = r.stdout.decode("utf-8", "replace").strip().replace("\\", "/") if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        ex = ""
    found = ""
    if not ex:
        tried.append("git --exec-path: did not run")
    else:
        cand = "/".join(ex.rstrip("/").split("/")[:-3]) + "/bin/bash.exe"
        if not os.path.isfile(cand):
            tried.append(cand + ": absent")
        elif check_candidate(cand):
            found = cand
    for d in os.environ.get("PATH", "").split(os.pathsep):
        for name in BASH_NAMES:
            cand = (d.rstrip("/\\") + "/" + name).replace("\\", "/")
            if d and os.path.isfile(cand) and check_candidate(cand):
                found = found or cand
    if found:
        return found, tried, ""
    return "", tried, ("no bash runs" + (" that can see " + str(script) if script else "") + ": "
                       + "; ".join(tried) + "; set GOV_BASH to Git's bash")
# <<< resolve_bash_py


# >>> legacy_ledger_py -- canonical copy: legacy_ledger.py in the gov lib dir (byte-identical; gated)
KEY_KINDS = ("site", "key", "record", "cutoff")
DRAINS = ("hunk", "key", "none")
DIRECTIONS = ("shrink-only", "append-only", "declared-set", "ceiling")
LEDGER_FIELDS = ("population", "seed", "key", "fields", "drain", "direction", "home", "leg")
# A key field read as a line number: a bare integer, or text ending `:<digits>`. A line number moves
# on an unrelated edit, so a row keyed on one drifts off its subject (TOOL-dWitnessedBar-13 S11).
LINE_NUMBER_RE = re.compile(r"[0-9]+|.*:[0-9]+")
SHA_RE = re.compile(r"[0-9a-f]{8,40}")
DISPOSITION_RE = re.compile(r"seeded|(?:carried|deferred|keep|widened):\S+")
HEADER_RE = re.compile(r"# ledger · (.+?) · key (\S+) (\S+) · direction (\S+) · drain (\S+)")
MALFORMED_TEXT = {
    "fields": "not the key's fields, a count and every trailing field, TAB-separated",
    "line-number": "a key field reads as a line number, which moves on an unrelated edit",
    "count": "the count is not a positive integer",
    "sha": "the sha is not 8 to 40 lowercase hex digits",
    "disposition": "the disposition is not seeded, carried:<unit>, deferred:<ask>, keep:<ask> or widened:<record>",
    "duplicate": "the key is declared twice",
}


@dataclass(frozen=True)
class Registration:
    """One `[[ledger]]` table: a population, the check that measures it and the file that tolerates it."""
    population: str
    seed: tuple
    key: str
    fields: tuple
    drain: str
    direction: str
    home: str
    leg: str
    verbatim: tuple = ()
    source: str = ""


def _run_git(root, *args, with_stderr=False):
    """-> (returncode, stdout) of one `git -C root` call, the inherited-directory variables dropped;
    `with_stderr` adds its stderr as a third item. A git that cannot be spawned or that times out is exit
    127 with the text `git not runnable: <exception>` (TOOL-dWitnessedBar-65 S9). This is the block's one
    git spawn, so the 60-second bound `resolve_health_log` uses bounds every git call of the seed's SHA
    resolution (TOOL-dWitnessedBar-67 S7)."""
    env = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE")}
    try:
        p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                           encoding="utf-8", errors="surrogateescape", env=env, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as exc:
        text = "git not runnable: %s" % exc
        return (127, "", text) if with_stderr else (127, text)
    return (p.returncode, p.stdout, p.stderr) if with_stderr else (p.returncode, p.stdout)


def check_home(home):
    """The refusal for a `home` that is not a relative path inside the repository, or "" for one that is."""
    if not isinstance(home, str) or not home.strip():
        return "home is not a non-empty string"
    if home.startswith(("/", "\\")) or re.match(r"[A-Za-z]:", home) or pathlib.PurePosixPath(home).is_absolute():
        return "home %r is absolute" % home
    if ".." in re.split(r"[/\\]", home):
        return "home %r holds a '..' segment" % home
    return ""


def _check_table(table):
    """-> the refusals one `[[ledger]]` table earns, empty when it registers."""
    if not isinstance(table, dict):
        return ["a [[ledger]] entry is not a table"]
    missing = [f for f in LEDGER_FIELDS if f not in table]
    if missing:
        return ["missing " + ", ".join(missing)]
    bad = []
    for name in ("population", "key", "drain", "direction", "home", "leg"):
        if not isinstance(table[name], str) or not table[name].strip():
            bad.append("%s is not a non-empty string" % name)
    for name, allowed in (("key", KEY_KINDS), ("drain", DRAINS), ("direction", DIRECTIONS)):
        if isinstance(table[name], str) and table[name] not in allowed:
            bad.append("%s %r is outside %s" % (name, table[name], " | ".join(allowed)))
    if not isinstance(table["seed"], list) or not all(isinstance(a, str) for a in table["seed"]):
        bad.append("seed is not a list of strings")
    fields = table["fields"]
    if (not isinstance(fields, list) or not fields
            or not all(isinstance(f, str) and re.fullmatch(r"[A-Za-z0-9_-]+", f) for f in fields)
            or len(set(fields)) != len(fields)):
        bad.append("fields is not a non-empty list of distinct field names")
        fields = []
    elif table["key"] == "site" and "path" not in fields:
        bad.append("a site table's fields lack path")
    verbatim = table.get("verbatim", [])
    if not isinstance(verbatim, list) or not all(isinstance(v, str) for v in verbatim):
        bad.append("verbatim is not a list of field names")
    else:
        outside = [v for v in verbatim if v not in fields]
        if outside:
            bad.append("verbatim names %s, not in its fields" % ", ".join(outside))
    if isinstance(table["home"], str) and check_home(table["home"]):
        bad.append(check_home(table["home"]))
    return bad


DEPLOYER_HOME = "govkit"  # the deployer kit's directory name, as the policy kit's DEPLOYER_HOME spells it


def read_registrations(root):
    """-> every `Registration` at `root`, or ValueError naming each bad table, one per line.

    No tool root is derived (§8 F7): every tracked file named `kit.toml`, at any depth, and every
    tracked `registry.toml` under a directory named `DEPLOYER_HOME`, at any depth, is read where it
    sits, so a kit homed outside the
    others' parent registers as theirs do. Two govkit registries, and two tables declaring one `home`
    wherever each sits, are refused. WHAT IT DOES NOT CHECK: a tracked fixture named `kit.toml`
    holding a `[[ledger]]` table registers as a kit's would.
    """
    rc, out = _run_git(root, "ls-files", "-z")
    if rc != 0:
        raise ValueError("git ls-files failed at %s, so no descriptor could be found" % root)
    tracked = [p for p in out.split("\0") if p]
    tail = f"{DEPLOYER_HOME}/registry.toml"
    registries = [p for p in tracked if p == tail or p.endswith("/" + tail)]
    descriptors = [p for p in tracked if p.rsplit("/", 1)[-1] == "kit.toml"]
    refusals = []
    if len(registries) > 1:
        refusals.append("%s: two govkit registries are tracked, so a kit-less population has no one home"
                        % ", ".join(registries))
    regs, homes = [], {}
    for rel in sorted(descriptors) + registries:
        try:
            data = tomllib.loads(pathlib.Path(root, rel).read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as exc:
            refusals.append("%s: does not read as TOML: %s" % (rel, exc))
            continue
        tables = data.get("ledger", [])
        if not isinstance(tables, list):
            refusals.append("%s: ledger is not an array of [[ledger]] tables" % rel)
            continue
        for n, table in enumerate(tables, 1):
            name = table.get("population", "#%d" % n) if isinstance(table, dict) else "#%d" % n
            bad = _check_table(table)
            if bad:
                refusals.extend("%s: [[ledger]] %r: %s" % (rel, name, b) for b in bad)
                continue
            reg = Registration(table["population"], tuple(table["seed"]), table["key"],
                               tuple(table["fields"]), table["drain"], table["direction"],
                               table["home"], table["leg"], tuple(table.get("verbatim", [])), rel)
            if reg.home in homes:
                first = homes[reg.home]
                refusals.append("%s: [[ledger]] %r and %s: [[ledger]] %r declare one home %s"
                                % (first.source, first.population, rel, reg.population, reg.home))
                continue
            homes[reg.home] = reg
            regs.append(reg)
    if refusals:
        raise ValueError("\n".join(refusals))
    return regs


def render_header(reg):
    """The ledger file's first line, rendered from its registration: the one fact the reader compares."""
    return "# ledger · %s · key %s %s · direction %s · drain %s" % (
        reg.population, reg.key, ",".join(reg.fields), reg.direction, reg.drain)


def parse_header(line):
    """-> {population, key, fields, direction, drain} of a ledger header line; ValueError for any other."""
    m = HEADER_RE.fullmatch(line.rstrip("\r\n"))
    if not m:
        raise ValueError("not a ledger header: %r" % line[:80])
    return {"population": m.group(1), "key": m.group(2), "fields": tuple(m.group(3).split(",")),
            "direction": m.group(4), "drain": m.group(5)}


def _parse_rows(lines, arity, tail, verbatim):
    """`read_rows` over lines already read; the base compare hands it a blob's lines."""
    rows, malformed = {}, []
    for number, raw in enumerate(lines, 1):
        row = raw.rstrip("\r")
        if not row.strip() or row.lstrip().startswith("#"):
            continue
        fields = row.split("\t")
        need = arity + 1 + len(tail)
        if (len(fields) < need or (not tail and len(fields) > need)
                or not all(f.strip() for f in fields[arity + 1:need])):
            malformed.append((number, "fields", row))
            continue
        key = tuple(f.strip() for f in fields[:arity])
        if any(i not in verbatim and LINE_NUMBER_RE.fullmatch(f) for i, f in enumerate(key)):
            malformed.append((number, "line-number", row))
            continue
        count = fields[arity].strip()
        if not (count.isascii() and count.isdigit()) or int(count) < 1:
            malformed.append((number, "count", row))
            continue
        values = [f.strip() for f in fields[arity + 1:need - 1]]
        if tail:
            values.append("\t".join(fields[need - 1:]).strip())
        named = dict(zip(tail, values))
        if "sha" in named and not SHA_RE.fullmatch(named["sha"]):
            malformed.append((number, "sha", row))
            continue
        if "disposition" in named and not DISPOSITION_RE.fullmatch(named["disposition"]):
            malformed.append((number, "disposition", row))
            continue
        if key in rows:
            malformed.append((number, "duplicate", row))
            continue
        rows[key] = (int(count), tuple(values), number, row)
    return rows, malformed


def read_rows(path, arity, tail=("sha", "disposition"), verbatim=()):
    """-> (rows, malformed) of the TAB rows at `path`, its header and every other `#` or blank line skipped.

    `rows` maps each key, the first `arity` fields, to `(count, tail values, line number, row)`;
    `malformed` holds `(line number, kind, row)` per refused line, `kind` a `MALFORMED_TEXT` key.
    `tail` names the fields after the count: a ledger's `("sha", "disposition")`, today's four-field
    registries' `("reason",)`, or `()` for measured rows, the key's fields then the count, which is
    what a seed argv prints, so one parser reads ledger and measurement alike. The last tail field
    keeps any further TABs. `verbatim` holds the key positions the line-number refusal skips.
    """
    text = pathlib.Path(path).read_text(encoding="utf-8")
    return _parse_rows(text.split("\n"), arity, tuple(tail), tuple(verbatim))


def render_malformed(entry):
    """One malformed `(line number, kind, row)` as the finding text a caller prints."""
    number, kind, row = entry
    return "line %d: %s: %s" % (number, MALFORMED_TEXT.get(kind, kind), row)


def read_ledger(root, reg):
    """`read_rows` over the registration's home at `root`, with its arity and its verbatim positions."""
    at = tuple(i for i, f in enumerate(reg.fields) if f in reg.verbatim)
    return read_rows(pathlib.Path(root, reg.home), len(reg.fields), verbatim=at)


def write_rows(root, reg, rows):
    """Write the header and `rows` to `<root>/<reg.home>`, the declared home and no other path, through a
    sibling temp file and `os.replace`, so a run that dies leaves the old file or the new one."""
    refusal = check_home(reg.home)
    if refusal:
        raise ValueError("%s: [[ledger]] %r: %s" % (reg.source, reg.population, refusal))
    lines = [render_header(reg)]
    for key, (count, values, *_rest) in rows.items():
        lines.append("\t".join([*key, str(count), *values]))
    _write_atomic(pathlib.Path(root, reg.home), "\n".join(lines) + "\n")


def _write_atomic(target, data):
    """Write `data`, text or bytes, to `target` through a sibling temp file and `os.replace`, every byte
    as given: a run that dies leaves the old file or the new one, never half of either."""
    target = pathlib.Path(target)
    fd, tmp = tempfile.mkstemp(dir=str(target.parent), prefix="." + target.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data.encode("utf-8") if isinstance(data, str) else data)
        os.replace(tmp, str(target))
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def compare_counts(measured, declared, direction):
    """-> one `(finding, key, measured count, declared count)` per key that fails, in key order.

    `measured` and `declared` map each key to its count. Both ways through `compute_coverage` with no
    owners: its `unclaimed` keys are each an `undeclared site`, its `stale_baseline` keys each an
    `unmeasured row`; a key on both sides whose counts differ is `count rose` or `count fell`. Under
    `ceiling` a count below the row's is no finding.
    """
    cov = compute_coverage({"ledger": list(measured)}, {}, {"ledger": list(declared)})
    undeclared = set(cov.unclaimed.get("ledger", ()))
    unmeasured = set(cov.stale_baseline.get("ledger", ()))
    out = []
    for key in sorted(set(measured) | set(declared)):
        have, want = measured.get(key), declared.get(key)
        if key in undeclared:
            out.append(("undeclared site", key, have, want))
        elif key in unmeasured:
            out.append(("unmeasured row", key, have, want))
        elif have > want:
            out.append(("count rose", key, have, want))
        elif have < want and direction != "ceiling":
            out.append(("count fell", key, have, want))
    return out


def read_renames(root, base):
    """-> the `(old, new)` pairs `git diff -M -z --name-status <base>` names at `root`: the base against
    the working tree, so a staged `git mv` counts as a committed one does."""
    rc, out = _run_git(root, "diff", "-M", "-z", "--name-status", base, "--")
    if rc != 0:
        raise ValueError("git diff -M %s failed at %s" % (base, root))
    parts = out.split("\0")
    pairs, i = [], 0
    while i < len(parts) and parts[i]:
        status = parts[i]
        if status[:1] in ("R", "C"):
            if status[:1] == "R":
                pairs.append((parts[i + 1], parts[i + 2]))
            i += 3
        else:
            i += 2
    return pairs


def _derive_rekeyed_rows(reg, rows, pairs):
    """-> (rows with each `site` row's path re-keyed through `pairs`, the pairs applied)."""
    if reg.key != "site":
        return dict(rows), []
    at = reg.fields.index("path")
    moved = dict(pairs)
    out, applied = {}, []
    for key, row in rows.items():
        new = key
        if key[at] in moved:
            new = key[:at] + (moved[key[at]],) + key[at + 1:]
            if (key[at], moved[key[at]]) not in applied:
                applied.append((key[at], moved[key[at]]))
        if new in out:
            raise ValueError("%s: renaming %s onto %s meets a row already keyed there"
                             % (reg.population, key[at], new[at]))
        out[new] = row
    return out, applied


def carry_renames(root, reg, base):
    """-> (the working rows with each path `read_renames(root, base)` names re-keyed, keeping count,
    sha and disposition, and the `(old, new)` pairs it applied). A malformed row raises: a rewrite
    would drop it."""
    rows, malformed = read_ledger(root, reg)
    if malformed:
        raise ValueError("%s: %s" % (reg.home, render_malformed(malformed[0])))
    return _derive_rekeyed_rows(reg, rows, read_renames(root, base))


def compare_to_base(root, reg):
    """-> (findings, why): the rows at `resolve_compare_base(root)`'s sha, each `site` row re-keyed
    through `read_renames(root, <sha>)`, judged against the working rows by the direction; `findings`
    is `(name, key)` per refusal, `gained`, `raised`, `edited`, `removed` or `above ceiling`. With no
    base, no home at the base, or a row that does not parse on either side, `findings` is None and
    `why` says which: a caller prints it as unresolved and never as green.
    """
    sha, why = resolve_compare_base(root)
    if not sha:
        return None, why
    rc, text = _run_git(root, "show", "%s:./%s" % (sha, reg.home))
    if rc != 0:
        return None, "no %s at %s (%s)" % (reg.home, sha[:12], why)
    at = tuple(i for i, f in enumerate(reg.fields) if f in reg.verbatim)
    base, bad = _parse_rows(text.split("\n"), len(reg.fields), ("sha", "disposition"), at)
    if bad:
        return None, "%s does not parse at %s: %s" % (reg.home, sha[:12], render_malformed(bad[0]))
    try:
        work, bad = read_ledger(root, reg)
    except OSError as exc:
        return None, "no %s in the working tree: %s" % (reg.home, exc)
    if bad:
        return None, "%s does not parse in the working tree: %s" % (reg.home, render_malformed(bad[0]))
    base, _applied = _derive_rekeyed_rows(reg, base, read_renames(root, sha))
    findings = []
    if reg.direction == "shrink-only":
        for key, (count, values, *_rest) in work.items():
            widened = values[-1].startswith("widened:")
            if key not in base and not widened:
                findings.append(("gained", key))
            elif key in base and count > base[key][0] and not widened:
                findings.append(("raised", key))
    elif reg.direction == "append-only":
        for key, (count, values, *_rest) in base.items():
            if key not in work:
                findings.append(("removed", key))
            elif work[key][:2] != (count, values):
                findings.append(("edited", key))
    elif reg.direction == "ceiling":
        for key, (count, _values, *_rest) in work.items():
            if key in base and count > base[key][0]:
                findings.append(("above ceiling", key))
    return findings, why


# The seed (TOOL-dWitnessedBar-15). A population is seeded once, at a recorded sha, and never again over
# an armed home, so a re-seed cannot launder an offence into the baseline; a seed that failed is
# recorded unarmed in its home, never green, and a rerun seeds an unarmed home as an absent one.
SEED_TIMEOUT = 600  # PINNED 2026-11-19: the `ceiling` of five rows of gate-legs.json, the nearest measure
UNARMED_LEAD = "# unarmed · "  # the home's state line: `# unarmed · <reason> · <sha>`
DEAD_PROBE_LEAD = "dead probe:"  # a seed line saying its probe measured nothing
UNSEEDED_DEFAULT = "unarmed"  # retrofit.unseeded's catalogue default, which holds where no policy kit resolves
NULL_SHA = "0" * 40  # the sha a seed stamps where HEAD is unborn: the row was seeded before any commit
UNBORN_LINE = "seed: HEAD is unborn, rows carry the null SHA"


def read_head_sha(root):
    """-> (sha, reason) of the commit `seed` stamps where no `--sha` is given (TOOL-dWitnessedBar-61):
    HEAD's commit from `git rev-parse --verify --quiet HEAD^{commit}`, so a ref naming a missing object
    is never stamped; `NULL_SHA` only where that exits 1 printing nothing and HEAD names a branch that
    does not exist, which is an unborn HEAD in a repository with no commit yet: `git symbolic-ref -q HEAD`
    exits 0 printing one `refs/` line and nothing on stderr, and `git for-each-ref <that ref>` exits 0
    printing nothing on either stream (TOOL-dWitnessedBar-64 S1 S2). Any other outcome, a broken,
    dangling, looping or detached-missing HEAD among them, is no sha and the reason `no HEAD: <the first
    stderr line of the probe that ended the read>`, or `git <verb> exited <rc>` where it printed none, so
    a tree git refused to read is never stamped as seeded before any commit (TOOL-dWitnessedBar-63 S8,
    TOOL-dWitnessedBar-64 S3). A probe that exits 0 and still ends the read names what disqualified it:
    `git for-each-ref listed <its first stdout line>` and `git symbolic-ref printed <the line not opening
    refs/>` (TOOL-dWitnessedBar-67 S18). The recall kit's `read_worktree_head` and the overlay's `check_born` read
    every failure as unborn and neither is importable from this block. WHAT IT DOES NOT CHECK: a git
    release whose wording or exit codes differ from these on any of the three probes, or a branch ref
    that `for-each-ref` matches by prefix, such as `refs/heads/b/x` beside an unborn `refs/heads/b`,
    which reads as no HEAD."""
    rc, out, err = _run_git(root, "rev-parse", "--verify", "--quiet", "HEAD^{commit}", with_stderr=True)
    out, err = out.strip(), err.strip()
    if rc == 0 and out:
        return out, ""
    verb = "rev-parse"
    if rc == 1 and not out and not err:
        verb = "symbolic-ref"
        rc, out, err = _run_git(root, "symbolic-ref", "-q", "HEAD", with_stderr=True)
        lines = out.splitlines()
        if rc == 0 and len(lines) == 1 and lines[0].startswith("refs/") and not err.strip():
            verb = "for-each-ref"
            rc, out, err = _run_git(root, "for-each-ref", lines[0], with_stderr=True)
            if rc == 0 and not out.strip() and not err.strip():
                return NULL_SHA, ""
    what = "git %s exited %d" % (verb, rc)
    rows = [ln.strip() for ln in out.splitlines() if ln.strip()] if rc == 0 else []
    if rows and verb == "for-each-ref":
        what = "git for-each-ref listed %s" % rows[0]
    elif rows and verb == "symbolic-ref":
        what = "git symbolic-ref printed %s" % ([ln for ln in rows if not ln.startswith("refs/")] or rows)[0]
    return None, "no HEAD: %s" % (err.strip().splitlines() or [what])[0].strip()


def read_home_state(path):
    """-> "absent", "unarmed" or "armed" for the population file at `path`: unarmed when one of its first
    two lines, the header's and the next, opens `UNARMED_LEAD`. A home that cannot be read raises."""
    try:
        head = pathlib.Path(path).read_bytes().decode("utf-8").split("\n")[:2]
    except FileNotFoundError:
        return "absent"
    return "unarmed" if any(line.startswith(UNARMED_LEAD) for line in head) else "armed"


def check_home_readable(path, header):
    """The refusal for a registered home at `path` that exists and yet cannot be seeded over, or "": one
    whose bytes do not read as UTF-8, `does not read: <why>`, or whose first line is neither `header`
    nor an unarmed line, `header disagrees: <first line>`, a legacy-grammar file among them. `seed`
    meets either by doing nothing (TOOL-dWitnessedBar-51 S50); an absent home is ""."""
    try:
        first = pathlib.Path(path).read_bytes().decode("utf-8").split("\n")[0].rstrip("\r")
    except FileNotFoundError:
        return ""
    except (OSError, UnicodeDecodeError) as exc:
        return "does not read: %s" % exc
    if first == header or first.startswith(UNARMED_LEAD):
        return ""
    return "header disagrees: %r is not %r" % (first[:80], header)


def check_home_admitted(root, home):
    """The refusal for a seed home the work tree does not admit, or "" for one it does. Resolved with
    symlinks followed, the home must lie under `root`, the work tree's top, and outside the git dir, else
    `outside the tree <path>`; `git check-ignore` must not match it, else `ignored <path>`
    (TOOL-dWitnessedBar-57 S11); and its parent directory must exist in the working tree, tracked files or
    none, else `no directory <parent>` (TOOL-dWitnessedBar-47): an adopter seeds into a directory it has
    just created, before anything in the target is committed, and `seed` never creates one. An absolute
    home resolving inside the work tree is admitted. WHAT IT DOES NOT CHECK: a file name the hygiene
    check's structure check refuses inside an existing directory, which is written and reds at that
    check's next run, never silently."""
    top = os.path.realpath(str(root))
    path = os.path.realpath(os.path.join(top, str(home)))
    shown = pathlib.Path(path).as_posix()
    try:
        rel = os.path.relpath(path, top)
    except ValueError:  # another drive on Windows
        return "outside the tree %s" % shown
    parts = pathlib.PurePath(rel).parts
    if rel == os.curdir or parts[:1] == (os.pardir,) or ".git" in [p.lower() for p in parts]:
        return "outside the tree %s" % shown
    rc, git_dir = _run_git(top, "rev-parse", "--absolute-git-dir")
    if rc != 0 or not git_dir.strip():
        return "outside the tree %s: no git dir resolves at %s" % (shown, pathlib.Path(top).as_posix())
    git_dir = os.path.normcase(os.path.realpath(git_dir.strip()))
    if os.path.normcase(path) == git_dir or os.path.normcase(path).startswith(git_dir.rstrip(os.sep) + os.sep):
        return "outside the tree %s" % shown
    rel = pathlib.PurePath(rel).as_posix()
    rc, _out = _run_git(top, "check-ignore", "-q", "--", rel)
    if rc != 1:
        return "ignored %s" % rel if rc == 0 else "ignored %s: git check-ignore exited %d" % (rel, rc)
    parent = pathlib.PurePosixPath(rel).parent.as_posix()
    if pathlib.Path(top, parent).is_dir():
        return ""
    return "no directory %s" % parent


def derive_seed_prefix(root):
    """The tool root a seed argv's `{prefix}` names (TOOL-dWitnessedBar-17 S9): the directory above the
    one holding this copy, relative to `root`, or absolute where no relative path exists, as on another
    drive on Windows."""
    tools = pathlib.Path(__file__).absolute().parent.parent
    try:
        return pathlib.Path(os.path.relpath(tools, str(root))).as_posix()
    except ValueError:
        return tools.as_posix()


def resolve_seed_arg(arg, root, troot):
    """One seed argument with its `{prefix}` resolved (TOOL-aFlattenedSeed-1 S3). An argument spelled
    `{prefix}/<home>/<file>` names a file of the kit gov homes at `<home>`, found through
    `resolve_kit_dir`, so a kit an adopter installed flat, with no `<home>` directory, still resolves;
    the path is relative to `root`, or absolute where none exists. Any other argument, or a kit no
    install holds, resolves the token against `troot` through `resolve_prefix_token`."""
    parts = str(arg).split("/")
    if len(parts) == 3 and parts[0] == "{prefix}":
        try:
            kit = resolve_kit_dir(parts[1], parts[2], pathlib.Path(__file__).absolute().parent)
        except LookupError:
            kit = None
        if kit is not None:
            try:
                return pathlib.Path(os.path.relpath(kit / parts[2], str(root))).as_posix()
            except ValueError:
                return (kit / parts[2]).as_posix()
    return resolve_prefix_token(arg, troot)


def resolve_seed_head(argv):
    """-> (argv, refusal): a seed argv's head as `regen.py`'s `run_command` maps it (TOOL-dWitnessedBar-51
    S32). `python` or `python3` runs as `sys.executable`, never a PATH lookup that can reach the MS-Store
    stub; `bash` runs as the `found` of the `resolve_bash_py` block's `scan_bash`, and where none runs the
    argv is empty and `refusal` is that block's own; any other head is spelled as written."""
    argv = list(argv)
    if argv and argv[0] in ("python", "python3"):
        return [sys.executable, *argv[1:]], ""
    if argv and argv[0] == "bash":
        found, _tried, refusal = scan_bash()
        return ([found, *argv[1:]], "") if found else ([], refusal)
    return argv, ""


def run_seed_argv(argv, root):
    """-> (stdout, reason) of one seed run at `root` under `SEED_TIMEOUT`: `reason` is "" for a live
    result, else `exit <n>`, `timed out`, `dead probe`, a line of its stdout opening `DEAD_PROBE_LEAD`, or
    `refused: <why>` where `resolve_seed_head` finds no bash. Each argument resolves through
    `resolve_seed_arg`, and the head through `resolve_seed_head`."""
    env = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE")}
    troot = derive_seed_prefix(root)
    argv, refusal = resolve_seed_head([resolve_seed_arg(a, root, troot) for a in argv])
    if refusal:
        return "", "refused: %s" % refusal
    try:
        p = subprocess.run(list(argv), cwd=str(root), capture_output=True, text=True, encoding="utf-8",
                           errors="replace", stdin=subprocess.DEVNULL, env=env, timeout=SEED_TIMEOUT)
    except subprocess.TimeoutExpired:
        return "", "timed out"
    except OSError:
        return "", "exit 127"
    if p.returncode != 0:
        return p.stdout, "exit %d" % p.returncode
    if any(line.startswith(DEAD_PROBE_LEAD) for line in p.stdout.splitlines()):
        return p.stdout, "dead probe"
    return p.stdout, ""


def seed_population(root, reg, sha, widen=None):
    """-> (the one line `seed` prints for `reg`, False when the seed left it unarmed by a failure).

    Absent or unarmed: run the seed and write the header and its rows, each `<sha>` and `seeded`.
    Present and armed: nothing, or under `widen` append only the keys the file lacks, each `<sha>` and
    `widened:<widen>`, never rewriting a row. A seed that exits non-zero, times out, finds a dead probe
    or prints a row `read_rows` refuses leaves the home holding the header and one unarmed line, an
    armed home untouched; a home `check_home_admitted` refuses is never written. `seed = []` is
    reported and nothing is written: the caller asks `retrofit.unseeded` first. A home that exists but
    does not read, or whose first line is neither the header `render_header` renders nor an unarmed
    line, is refused by `check_home_readable`: nothing run, nothing written, and the second value None,
    so such a home never reads `present` or absent (TOOL-dWitnessedBar-51 S50).
    """
    name = reg.population
    if not reg.seed:
        return "unarmed %s no seed" % name, True
    home = pathlib.Path(root, reg.home)
    refusal = check_home_readable(home, render_header(reg))
    if refusal:
        return "refused %s %s" % (name, refusal), None
    state = read_home_state(home)
    if state == "armed" and widen is None:
        return "present %s" % name, True
    if state != "armed" or widen is not None:
        refusal = check_home_admitted(root, reg.home)
        if refusal:
            print("legacy_ledger: %s: %s; nothing written" % (reg.home, refusal), file=sys.stderr)
            return "unarmed %s %s" % (name, refusal), False
    out, reason = run_seed_argv(reg.seed, root)
    rows = {}
    if not reason:
        at = tuple(i for i, f in enumerate(reg.fields) if f in reg.verbatim)
        rows, bad = _parse_rows(out.split("\n"), len(reg.fields), (), at)
        if bad:
            reason = "seed printed %s" % render_malformed(bad[0]).replace("\t", " ")
    if reason and state == "armed":
        return "unarmed %s %s; the armed home is unchanged" % (name, reason), False
    if reason:
        _write_atomic(home, "%s\n%s%s · %s\n" % (render_header(reg), UNARMED_LEAD, reason, sha))
        return "unarmed %s %s" % (name, reason), False
    if state != "armed":
        write_rows(root, reg, {k: (r[0], (sha, "seeded")) for k, r in rows.items()})
        return "armed %s %d" % (name, len(rows)), True
    declared, bad = read_ledger(root, reg)
    if bad:
        raise ValueError("%s: %s" % (reg.home, render_malformed(bad[0])))
    added = [k for k in rows if k not in declared]
    if added:
        text = home.read_bytes().decode("utf-8")
        text += "" if text.endswith("\n") else "\n"
        text += "".join("\t".join([*k, str(rows[k][0]), sha, "widened:" + widen]) + "\n" for k in added)
        _write_atomic(home, text)
    return " ".join(["widened", name, ", ".join("\t".join(k) for k in added)]).rstrip(), True


def seed_home(root, home, sha, argv=None, template=None):
    """-> (line, False when left unarmed by a failure): the unregistered form for a population not yet in
    the ledger grammar. Only an absent or unarmed `home` is written: `argv`, each `{out}` in it replaced
    by a sibling temp path, writes the population there and a live run moves it into place; `template`
    is copied. Either is atomic; a failed run leaves one unarmed line, a refused home no file. A home
    `check_home_admitted` refuses, one outside the work tree or ignored included, is read and written
    by nothing (TOOL-dWitnessedBar-57 S11)."""
    refusal = check_home_admitted(root, home) or check_home(home)
    if refusal:
        print("legacy_ledger: %s: %s; nothing written" % (home, refusal), file=sys.stderr)
        return "unarmed %s %s" % (home, refusal), False
    target = pathlib.Path(root, home)
    if read_home_state(target) == "armed":
        return "present %s" % home, True
    if template is not None:
        _write_atomic(target, pathlib.Path(template).read_bytes())
        return "armed %s" % home, True
    fd, out = tempfile.mkstemp(dir=str(target.parent), prefix="." + target.name + ".", suffix=".seed")
    os.close(fd)
    try:
        _stdout, reason = run_seed_argv([a.replace("{out}", out) for a in argv], root)
        if reason:
            _write_atomic(target, "%s%s · %s\n" % (UNARMED_LEAD, reason, sha))
            return "unarmed %s %s" % (home, reason), False
        os.replace(out, str(target))
    finally:
        if os.path.exists(out):
            os.unlink(out)
    return "armed %s" % home, True


def read_seed_policy(key, root):
    """-> the value of policy key `key` at `root`, through the policy kit's reader: `policy.py get` run
    as a subprocess, the Python asker's call shape (the policy kit's README, its reader section), the kit
    found by `resolve_kit_dir` beside this file; None where no policy kit resolves, the lookup then on
    stderr. A reader refusal raises ValueError carrying the reader's own line. WHAT IT DOES NOT CHECK: a
    policy file the working tree changed and has not landed, since the reader takes the landed revision."""
    try:
        kit = resolve_kit_dir("policy", "policy.py", pathlib.Path(__file__).absolute().parent)
    except LookupError as exc:
        print("legacy_ledger: %s: no policy kit resolves, so its catalogue default holds: %s" % (key, exc),
              file=sys.stderr)
        return None
    env = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE")}
    got = subprocess.run([sys.executable, str(pathlib.Path(kit, "policy.py")), "get", key], cwd=str(root),
                         capture_output=True, text=True, encoding="utf-8", errors="replace",
                         stdin=subprocess.DEVNULL, env=env)
    if got.returncode != 0:
        raise ValueError(got.stderr.strip() or "policy.py get %s exited %d" % (key, got.returncode))
    return got.stdout.strip()


def run_seed_cli(args, cwd):
    """`seed --all | --population <name> [--widen <record>] [--sha <sha>]`, and the unregistered
    `seed --home <path> [--sha <sha>] (--copy <template> | -- <argv>...)`: one line per population, exit
    0, or 1 when a seed left one unarmed by a failure, or 2 on a refusal. `seed = []` exits 0 under
    `retrofit.unseeded: unarmed` and 2 under `refuse`, naming every such registration. With no `--sha`,
    `read_head_sha` names the sha: on an unborn HEAD the null SHA, `UNBORN_LINE` printed once on stderr,
    so stdout keeps one line per population (TOOL-dWitnessedBar-63 S32); on any other failure each
    population is `unarmed` with that reason and nothing is written, the refused-home branch whole: stderr
    carries `legacy_ledger: <population>: <reason>; nothing written` (TOOL-dWitnessedBar-63 S6). Where
    no repository root resolves, that route is taken before any registration is read, from the toplevel
    call's reason: `--population` prints its one unarmed line, `--all` prints nothing on stdout and
    `seed: no HEAD: <reason>` on stderr, each exit 1; `--home` exits 2 (TOOL-dWitnessedBar-65 S8). Where a
    root resolves and HEAD does not, `--all` over no registration prints nothing on stdout and that same
    stderr line, and exits 0, nothing being left unarmed (TOOL-dWitnessedBar-73 S23). A
    given `--sha` is folded to lowercase and stamped as the full sha of the commit it names; one naming
    none, and the null SHA outside an unborn HEAD, exits 2 (TOOL-dWitnessedBar-65 S10), and so does one
    whose commit's full sha does not start with it, a branch or tag with an all-hex name having stood in
    for the object it abbreviates (TOOL-dWitnessedBar-67 S9)."""
    usage = ("usage: legacy_ledger.py seed (--all | --population <name>) [--widen <record>] [--sha <sha>]\n"
             "       legacy_ledger.py seed --home <path> [--sha <sha>] (--copy <template> | -- <argv>...)")
    argv = None
    if "--" in args:
        argv, args = args[args.index("--") + 1:], args[:args.index("--")]
    opts, every, i = {}, False, 0
    while i < len(args):
        if args[i] == "--all":
            every, i = True, i + 1
        elif args[i] in ("--population", "--widen", "--sha", "--home", "--copy") and i + 1 < len(args) \
                and args[i] not in opts:
            opts[args[i]], i = args[i + 1], i + 2
        else:
            print(usage, file=sys.stderr)
            return 2
    homed = "--home" in opts
    if (homed and (every or "--population" in opts or "--widen" in opts
                   or ("--copy" in opts) == bool(argv))) \
            or (not homed and (every == ("--population" in opts) or argv is not None or "--copy" in opts)):
        print(usage, file=sys.stderr)
        return 2
    widen = opts.get("--widen")
    if widen is not None and not re.fullmatch(r"\S+", widen):
        print("legacy_ledger: --widen takes a record with no whitespace, as widened:<record> is written",
              file=sys.stderr)
        return 2
    rc, top, err = _run_git(cwd, "rev-parse", "--show-toplevel", with_stderr=True)
    if rc != 0 or not top.strip():
        if homed:
            print("legacy_ledger: not inside a git work tree", file=sys.stderr)
            return 2
        # No root is no HEAD, read before any registration or home (TOOL-dWitnessedBar-65 S8, §8 F6).
        no_head = "no HEAD: %s" % (err.strip().splitlines() or ["git rev-parse exited %d" % rc])[0].strip()
        if every:
            print("seed: %s" % no_head, file=sys.stderr)
        else:
            print("legacy_ledger: %s: %s; nothing written" % (opts["--population"], no_head), file=sys.stderr)
            print("unarmed %s %s" % (opts["--population"], no_head))
        return 1
    root = top.strip()
    sha, no_head = opts.get("--sha"), ""
    if sha is None:
        sha, no_head = read_head_sha(root)
    else:
        # A given sha is folded to lowercase, held to the grammar, then must name a commit, whose full sha
        # is stamped; the null SHA only where HEAD is unborn (TOOL-dWitnessedBar-65 S10, §8 F4, F7).
        sha = sha.lower()
        if not SHA_RE.fullmatch(sha):
            print("legacy_ledger: --sha %r is not 8 to 40 hex digits" % opts["--sha"], file=sys.stderr)
            return 2
        if sha == NULL_SHA:
            named = read_head_sha(root)[0] == NULL_SHA
        else:
            rc, out = _run_git(root, "rev-parse", "--verify", "--quiet", "%s^{commit}" % sha)
            named = rc == 0 and SHA_RE.fullmatch(out.strip()) is not None
            if named and not out.strip().startswith(sha):
                print("legacy_ledger: --sha %r resolves through a ref to %s, a commit it does not abbreviate, "
                      "so no home is written" % (opts["--sha"], out.strip()), file=sys.stderr)
                return 2
            sha = out.strip()
        if not named:
            print("legacy_ledger: --sha %r names no commit in this repository%s, so no home is written"
                  % (opts["--sha"], ", whose HEAD is not unborn" if sha == NULL_SHA else ""), file=sys.stderr)
            return 2
    unborn = "--sha" not in opts and sha == NULL_SHA
    try:
        if homed:
            try:
                home = pathlib.Path(os.path.relpath(pathlib.Path(cwd, opts["--home"]), root)).as_posix()
            except ValueError:  # another drive on Windows: `check_home_admitted` reads it outside the tree
                home = pathlib.Path(cwd, opts["--home"]).as_posix()
            if no_head:
                print("legacy_ledger: %s: %s; nothing written" % (home, no_head), file=sys.stderr)
                print("unarmed %s %s" % (home, no_head))
                return 1
            if unborn:
                print(UNBORN_LINE, file=sys.stderr)
            copy = str(pathlib.Path(cwd, opts["--copy"])) if "--copy" in opts else None
            line, ok = seed_home(root, home, sha, argv=argv, template=copy)
            print(line)
            return 0 if ok else 1
        regs = read_registrations(root)
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        print("legacy_ledger: %s" % exc, file=sys.stderr)
        return 2
    picked = regs if every else [r for r in regs if r.population == opts["--population"]]
    if not every and len(picked) != 1:
        print("legacy_ledger: %d registrations name %r; --population seeds exactly one"
              % (len(picked), opts["--population"]), file=sys.stderr)
        return 2
    unseeded = [r.population for r in picked if not r.seed]
    if unseeded:
        try:
            value = read_seed_policy("retrofit.unseeded", root)
        except ValueError as exc:
            print(exc, file=sys.stderr)
            return 2
        value = UNSEEDED_DEFAULT if value is None else value
        if value == "refuse":
            print("legacy_ledger: retrofit.unseeded is refuse, so each registration declaring seed = [] is "
                  "refused: %s" % ", ".join(unseeded), file=sys.stderr)
            return 2
        if value != UNSEEDED_DEFAULT:
            print("legacy_ledger: retrofit.unseeded reads %r, outside unarmed | refuse" % value, file=sys.stderr)
            return 2
    if no_head:
        # `--all` over no registration leaves nothing unarmed: the reason goes to stderr (TOOL-dWitnessedBar-73 S23).
        if not picked:
            print("seed: %s" % no_head, file=sys.stderr)
        for reg in picked:
            if reg.seed:
                print("legacy_ledger: %s: %s; nothing written" % (reg.population, no_head), file=sys.stderr)
            print("unarmed %s %s" % (reg.population, no_head if reg.seed else "no seed"))
        return 1 if any(reg.seed for reg in picked) else 0
    if unborn:
        print(UNBORN_LINE, file=sys.stderr)
    worst = 0
    for reg in picked:
        try:
            line, ok = seed_population(root, reg, sha, widen)
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            print("legacy_ledger: %s: %s" % (reg.population, exc), file=sys.stderr)
            worst = 2
            continue
        print(line)
        worst = max(worst, 2 if ok is None else 0 if ok else 1)
    return worst
# <<< legacy_ledger_py
