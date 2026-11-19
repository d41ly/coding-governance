"""legacy_ledger -- the baseline ledger factory, as this kit carries it (TOOL-dWitnessedBar-13).

The block below is INLINED byte-identically from the canonical copy its marker line names, gov's lib
dir, which ships nothing; `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts.
This kit requires no other kit, so it carries the block itself: `sh_hygiene.py` and
`encoding_posture.py` read their four-field registries through `read_rows` and grade them through
`compare_counts`, each keeping its own messages. The two names the block calls, `compute_coverage` and
`resolve_compare_base`, come from this kit's own `coverage_join.py`, imported outside the block so the
block stays byte-identical. The CLI lives on the canonical copy only.
"""
from __future__ import annotations

import os
import pathlib
import re
import subprocess
import tempfile
import tomllib
from dataclasses import dataclass

from coverage_join import compute_coverage, resolve_compare_base  # noqa: F401  (the block below calls both)


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


def _run_git(root, *args):
    """-> (returncode, stdout) of one `git -C root` call, the inherited-directory variables dropped."""
    env = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE")}
    try:
        p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                           encoding="utf-8", errors="surrogateescape", env=env)
    except OSError as exc:
        return 127, str(exc)
    return p.returncode, p.stdout


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


def read_registrations(root):
    """-> every `Registration` at `root`, or ValueError naming each bad table, one per line.

    No tool root is derived (§8 F7): every tracked file named `kit.toml`, at any depth, and every
    tracked `govkit/registry.toml`, at any depth, is read where it sits, so a kit homed outside the
    others' parent registers as theirs do. Two govkit registries, and two tables declaring one `home`
    wherever each sits, are refused. WHAT IT DOES NOT CHECK: a tracked fixture named `kit.toml`
    holding a `[[ledger]]` table registers as a kit's would.
    """
    rc, out = _run_git(root, "ls-files", "-z")
    if rc != 0:
        raise ValueError("git ls-files failed at %s, so no descriptor could be found" % root)
    tracked = [p for p in out.split("\0") if p]
    registries = [p for p in tracked if p == "govkit/registry.toml" or p.endswith("/govkit/registry.toml")]
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
    target = pathlib.Path(root, reg.home)
    lines = [render_header(reg)]
    for key, (count, values, *_rest) in rows.items():
        lines.append("\t".join([*key, str(count), *values]))
    fd, tmp = tempfile.mkstemp(dir=str(target.parent), prefix="." + target.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines) + "\n")
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
# <<< legacy_ledger_py
