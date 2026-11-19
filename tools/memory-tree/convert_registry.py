#!/usr/bin/env python3
"""convert_registry.py -- a registry's legacy grammar converted in place onto the ledger grammar
(TOOL-dWitnessedBar-16).

    python <prefix>/memory-tree/convert_registry.py convert --home <home>
    python <prefix>/memory-tree/convert_registry.py read-back <population>

`convert` reads one file of a legacy grammar `LEGACY` names, keyed by the ledger home's file name,
and writes that home in the ledger grammar through the factory's `write_rows`: the header rendered
from the population's `[[ledger]]` table, then one row per key, its count, the sha `read_head_sha`
names and `seeded`. A home holding no row is written as its header and the `# unarmed · dead probe ·
<sha>` line the factory's seed writes for a dead probe. Each former reason, which the row grammar has
no field for, is printed `reason · <key> · <text>` for the conversion record. A home whose first line
is already a ledger header is said so and nothing is written, so a second run never re-dates a row.
The table names each legacy file's parser and where it reads: the home itself, the two map homes
their TOML sibling, which the conversion removes, and drift's two the project layer whose `PINS` and
`BASELINES` literals the caller names (`convert` names none, so it refuses those two). It names no
descriptor: a population's `[[ledger]]` table is found through the factory's `read_registrations`
over the checkout holding this program, so the shape is read from that table and never typed here,
and `<entry>`, the step id's head, is the `id` of the descriptor that table sits in.

The `[[upgrade]]` step that converts an adopter's list, `up`, `down` and `witness` over `<target>`,
is gov's step program `<gov>/govkit/steps/registry_to_ledger.py`, which loads this module and calls
`derive_after`, `write_after` and `read_legacy_entry` (TOOL-dWitnessedBar-16 S10, §8 F20).

`read-back` is each registration's `seed`: it prints each row of the population's working home as its
key fields and count, TAB-joined, the measured rows the factory's seed run parses; where the home
reads absent or unarmed it prints one `dead probe: <home> holds no row` line.

Exit 0 done, 1 refused naming the file (nothing written), 2 a usage error.

WHAT IT DOES NOT CHECK. That a legacy row's key still names a live site: a conversion is a regrammar
at one sha and adds or drops no key. A legacy file an adopter edited into a shape its parser refuses
is refused, never guessed at.
"""
from __future__ import annotations

import ast
import dataclasses
import os
import pathlib
import re
import shutil
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
import legacy_ledger as LL  # noqa: E402  the ledger factory, this kit's copy

SAY = "convert-registry"
REASON_LEAD = "reason"
DEAD_PROBE_REASON = "dead probe"
# Where a legacy file sits, by the home it converts to: the home itself, its sibling of `SIBLING_SUFFIX`
# (removed once converted), or the file the caller names (the step's `--from`).
READS_HOME, READS_SIBLING, READS_NAMED = "home", "sibling", "named"
SIBLING_SUFFIX = ".toml"


class Refusal(Exception):
    """A legacy file, a descriptor or a target this program will not convert, named."""


def parse_tab_fields(line, need, what):
    """The TAB fields of one legacy row, refused below `need` of them."""
    fields = line.split("\t")
    if len(fields) < need:
        raise Refusal("%s: not %s" % (line[:80], what))
    return fields


def parse_keyed_reason(arity):
    """A parser for `<key fields> TAB <reason>` rows, count 1."""
    def parse(line):
        f = parse_tab_fields(line, arity, "%d TAB fields then a reason" % arity)
        return tuple(x.strip() for x in f[:arity]), 1, "\t".join(f[arity:]).strip()
    return parse


def parse_counted_reason(arity):
    """A parser for `<key fields> TAB <count> TAB <reason>` rows."""
    def parse(line):
        f = parse_tab_fields(line, arity + 1, "%d TAB fields, a count and a reason" % arity)
        return tuple(x.strip() for x in f[:arity]), int(f[arity].strip()), "\t".join(f[arity + 1:]).strip()
    return parse


def parse_spaced_reason(line):
    """`<key> <whitespace> <reason>`, or the key alone."""
    parts = line.strip().split(None, 1)
    return (parts[0],), 1, parts[1].strip() if len(parts) > 1 else ""


def parse_carrier(line):
    """`<path> · <why>`, method-carriers' row."""
    path, _sep, why = line.partition(" · ")
    return (path.strip(),), 1, why.strip()


def parse_contract(line):
    """readme-contract's `!<path> - <reason>` exempt row or `<path>` bound row; `exempt-pin:` is dropped."""
    if line.startswith("exempt-pin:"):
        return None
    binding = "exempt" if line.startswith("!") else "bound"
    path, _sep, why = line.lstrip("!").partition(" - ")
    return (path.strip(), binding), 1, why.strip()


def parse_fork_ceiling(line):
    """`<id> TAB <bash> TAB <ceiling> TAB <base> TAB <setup> TAB <command> TAB <reason>`."""
    f = parse_tab_fields(line, 6, "id, bash, ceiling, base, setup and command, TAB-separated")
    return (f[0].strip(), f[1].strip(), f[3].strip(), f[4].strip(), f[5].strip()), int(f[2].strip()), \
        "\t".join(f[6:]).strip()


def parse_unarmed_branch(line):
    """`<gate> TAB <check> TAB <ordinal> TAB <signature> [TAB <reason>]`: the ordinal leaves the key."""
    f = parse_tab_fields(line, 4, "gate, check, ordinal and signature, TAB-separated")
    return (f[0].strip(), f[1].strip(), f[3].strip()), 1, "\t".join(f[4:]).strip()


def parse_dead_path(line):
    """`<path> TAB <ordinal> TAB <line text> TAB <reason>`: the ordinal leaves the key."""
    f = parse_tab_fields(line, 3, "path, ordinal and line text, TAB-separated")
    return (f[0].strip(), f[2].strip()), 1, "\t".join(f[3:]).strip()


RETIREMENT_RE = re.compile(
    r'(?P<unit>\S+) · RETIRES (?P<path>\S+) check (?P<check>\S+) (?P<head>.*?)'
    r' · R1 (?P<r1>.*?) · R2 (?P<r2>.*?) · R3 (?P<r3>.*?) · R4 (?P<r4>.*?)'
    r' · survivor (?P<survivor>\S+) "(?P<signature>.+?)" · replay "(?P<replay>.+?)"(?P<tail>(?: · .*)?)$')


def parse_retirement(line):
    """A retirement row of the README's old grammar: every field `check_retirements` grades is a key
    field; the signature head, sites and `supersedes` clause are the reason the record keeps."""
    m = RETIREMENT_RE.fullmatch(line.strip())
    if not m:
        raise Refusal("%s: not `<id> · RETIRES <gate> check <n> … · R1 … · R4 … · survivor <file> "
                      "\"<signature>\" · replay \"<line>\"`" % line[:80])
    key = tuple(m[k] for k in ("unit", "path", "check", "r1", "r2", "r3", "r4", "survivor", "signature", "replay"))
    return key, 1, " ".join(p for p in (m["head"].strip(), m["tail"].lstrip(" ·").strip()) if p)


def read_toml_rows(text, _name):
    """The map baseline's `<inventory> = [<key>, …]` tables as `(inventory, key)` rows."""
    data = tomllib.loads(text)
    return [((inv, key), 1, "") for inv, keys in data.items() for key in keys]


def read_exempt_rows(text, _name):
    """The affordance list's `exempt = [<dossier>, …]` as `(dossier,)` rows."""
    return [((name,), 1, "") for name in tomllib.loads(text).get("exempt", [])]


def read_layer_literal(text, name):
    """The literal assigned to `name` in a project layer, read with `ast` and never imported."""
    for node in ast.parse(text).body:
        target = node.target if isinstance(node, ast.AnnAssign) else (
            node.targets[0] if isinstance(node, ast.Assign) and len(node.targets) == 1 else None)
        if isinstance(target, ast.Name) and target.id == name and node.value is not None:
            return ast.literal_eval(node.value)
    return None


def read_pin_rows(text, _name):
    """drift's `PINS` as `(signal,)` rows; a pin of 0 writes no row, since a row's count is at least 1."""
    pins = read_layer_literal(text, "PINS") or {}
    return [((sig,), int(n), "") for sig, n in pins.items() if int(n) > 0]


def read_baseline_rows(text, _name):
    """drift's `BASELINES` as `(signal, id)` rows."""
    sets = read_layer_literal(text, "BASELINES") or {}
    return [((sig, ident), 1, "") for sig, ids in sets.items() for ident in dict.fromkeys(ids)]


def read_lines_with(parse):
    """A whole-file reader over one line parser: every non-blank, non-`#` line, CR stripped."""
    def read(text, _name):
        out = []
        for raw in text.split("\n"):
            line = raw.rstrip("\r")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            row = parse(line)
            if row is not None:
                out.append(row)
        return out
    return read


# ledger home's file name -> (population, reader, where its legacy file sits): the legacy grammars this
# program converts. No descriptor is named: `derive_registration` finds each population's table.
LEGACY = {
    "baseline.txt": ("baseline", read_toml_rows, READS_SIBLING),
    "affordance-exempt.txt": ("affordance-exempt", read_exempt_rows, READS_SIBLING),
    "brief-recorded-waiver.txt": ("brief-recorded-waiver", read_lines_with(parse_keyed_reason(1)), READS_HOME),
    "pass-order-waiver.txt": ("pass-order-waiver", read_lines_with(parse_keyed_reason(1)), READS_HOME),
    "curation-debt.txt": ("curation-debt", read_lines_with(parse_spaced_reason), READS_HOME),
    "id-orphan-waiver.txt": ("id-orphan-waiver", read_lines_with(parse_keyed_reason(1)), READS_HOME),
    "legacy-files.txt": ("legacy-files", read_lines_with(parse_spaced_reason), READS_HOME),
    "method-carriers.txt": ("method-carriers", read_lines_with(parse_carrier), READS_HOME),
    "readme-contract.txt": ("readme-contract", read_lines_with(parse_contract), READS_HOME),
    "refusal-retirements.txt": ("refusal-retirements", read_lines_with(parse_retirement), READS_HOME),
    "stale-header-waiver.txt": ("stale-header-waiver", read_lines_with(parse_spaced_reason), READS_HOME),
    "trace-waiver.txt": ("trace-waiver", read_lines_with(parse_keyed_reason(2)), READS_HOME),
    "unarmed-branches.txt": ("unarmed-branches", read_lines_with(parse_unarmed_branch), READS_HOME),
    "encoding-posture-sites.txt": ("encoding-posture-sites", read_lines_with(parse_counted_reason(2)), READS_HOME),
    "fork-ceilings.txt": ("fork-ceilings", read_lines_with(parse_fork_ceiling), READS_HOME),
    "location-probe-waivers.txt": ("location-probe-waivers", read_lines_with(parse_counted_reason(2)), READS_HOME),
    "spawn-idiom-sites.txt": ("spawn-idiom-sites", read_lines_with(parse_counted_reason(2)), READS_HOME),
    "substitution-fed-loops.txt": ("substitution-fed-loops", read_lines_with(parse_counted_reason(2)), READS_HOME),
    "temp-name-sites.txt": ("temp-name-sites", read_lines_with(parse_counted_reason(2)), READS_HOME),
    # TOOL-dWitnessedBar-17 §8 F9: the `absent|moved:DEST` column is printed as the row's reason.
    "corpus-path-unresolved.txt": ("corpus-path-unresolved", read_lines_with(parse_counted_reason(2)), READS_HOME),
    "docs-undocumented.txt": ("docs-undocumented", read_lines_with(parse_keyed_reason(1)), READS_HOME),
    "spec-token-waivers.txt": ("spec-token-waivers", read_lines_with(parse_keyed_reason(1)), READS_HOME),
    "dead-path-waivers.txt": ("dead-path-waivers", read_lines_with(parse_dead_path), READS_HOME),
    "playbook-kit-waivers.txt": ("playbook-kit-waivers", read_lines_with(parse_spaced_reason), READS_HOME),
    "drift-pins.txt": ("drift-pins", read_pin_rows, READS_NAMED),
    "drift-baselines.txt": ("drift-baselines", read_baseline_rows, READS_NAMED),
}


def read_legacy_entry(home, source=None):
    """-> (population, reader, the path it reads, the home it writes, whether the read file is removed)
    for `home`, by its file name. `source` names the legacy file of a home that reads a named one, and
    is refused for any other home, so a caller cannot point a list at a file its table does not name."""
    path = pathlib.PurePosixPath(home.replace("\\", "/"))
    if path.name not in LEGACY:
        raise Refusal("%s: no legacy grammar of that name is known (%s)" % (home, ", ".join(sorted(LEGACY))))
    population, reader, where = LEGACY[path.name]
    if where == READS_NAMED:
        if not source:
            raise Refusal("%s reads the legacy file its caller names, and none was named" % home)
        reads = pathlib.PurePosixPath(source.replace("\\", "/")).as_posix()
    elif source:
        raise Refusal("%s reads %s, so it takes no named legacy file (%s)"
                      % (home, "its own file" if where == READS_HOME else "its sibling", source))
    else:
        reads = (path.with_suffix(SIBLING_SUFFIX) if where == READS_SIBLING else path).as_posix()
    return population, reader, reads, path.as_posix(), where == READS_SIBLING


def resolve_checkout():
    """The work tree holding this program, whose descriptors register its populations."""
    rc, out = LL._run_git(KIT, "rev-parse", "--show-toplevel")
    if rc != 0 or not out.strip():
        raise Refusal("%s is not inside a git work tree, so no [[ledger]] table can be read" % KIT)
    return out.strip()


def derive_registration(population, home):
    """The `Registration` of `population`, read through the factory's `read_registrations` over the
    checkout holding this program and homed at `home`; with the `id` of the descriptor its table sits
    in, the `<entry>` a step id carries."""
    checkout = resolve_checkout()
    try:
        regs = [r for r in LL.read_registrations(checkout) if r.population == population]
    except ValueError as exc:
        raise Refusal("a [[ledger]] registration is refused:\n%s" % exc) from None
    if len(regs) != 1:
        raise Refusal("%d [[ledger]] tables name %r at %s, not one" % (len(regs), population, checkout))
    reg = regs[0]
    source = pathlib.Path(checkout, reg.source)
    try:
        data = tomllib.loads(source.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise Refusal("%s: does not read as TOML: %s" % (reg.source, exc)) from None
    return dataclasses.replace(reg, home=home), data.get("id") or pathlib.PurePosixPath(reg.source).parent.name


def read_legacy_rows(root, home, source=None):
    """-> (registration, entry id, the path read, {key: count}, [(key, reason)]) of the legacy file
    `LEGACY` names for `home` at `root`: an ordinal registry's equal keys merged, their count the
    number of rows; any other repeated key refused, so no row is dropped or merged."""
    population, reader, reads, writes, _removed = read_legacy_entry(home, source)
    reg, entry = derive_registration(population, writes)
    text = pathlib.Path(root, reads).read_bytes().decode("utf-8")
    try:
        parsed = reader(text, reads)
    except (ValueError, tomllib.TOMLDecodeError, SyntaxError) as exc:
        raise Refusal("%s: %s" % (reads, exc)) from None
    if any(len(key) != len(reg.fields) for key, _n, _r in parsed):
        raise Refusal("%s: a row does not carry the %d key fields %s" % (reads, len(reg.fields), ",".join(reg.fields)))
    merges = population in ("unarmed-branches", "dead-path-waivers")
    rows, reasons = {}, []
    for key, count, reason in parsed:
        if any("\t" in f or not f.strip() for f in key[:1]):
            raise Refusal("%s: a row's first key field is empty or holds a TAB: %r" % (reads, key))
        if key in rows and not merges:
            raise Refusal("%s: the key %s is declared twice" % (reads, "\t".join(key)))
        rows[key] = rows.get(key, 0) + count
        if reason:
            reasons.append((key, reason))
    return reg, entry, reads, rows, reasons


def derive_converted_text(reg, rows, sha):
    """The home's bytes in the ledger grammar, written through the factory's `write_rows` into a scratch
    root so it stays the one writer; a population with no row is its header and the dead-probe line."""
    if not rows:
        return ("%s\n%s%s · %s\n" % (LL.render_header(reg), LL.UNARMED_LEAD, DEAD_PROBE_REASON, sha)).encode("utf-8")
    scratch = tempfile.mkdtemp(prefix="cr")
    try:
        pathlib.Path(scratch, reg.home).parent.mkdir(parents=True, exist_ok=True)
        LL.write_rows(scratch, reg, {k: (n, (sha, "seeded")) for k, n in rows.items()})
        return pathlib.Path(scratch, reg.home).read_bytes()
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


def check_ledger_header(path):
    """True where the file at `path` opens with a ledger header."""
    try:
        first = pathlib.Path(path).read_bytes().decode("utf-8").split("\n", 1)[0]
        LL.parse_header(first)
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    return True


def derive_after(root, home, source=None, sha_root=None):
    """-> ({root-relative path: bytes, or None for removed}, registration, entry id, reasons): what
    converting `home` at `root` writes; {} where the home already reads as a ledger or no legacy file
    is there. The sha stamped is HEAD's at `sha_root`, `root` where none is given."""
    population, _reader, reads, writes, removed = read_legacy_entry(home, source)
    if check_ledger_header(pathlib.Path(root, writes)) or not pathlib.Path(root, reads).is_file():
        reg, entry = derive_registration(population, writes)
        return {}, reg, entry, []
    sha, why = LL.read_head_sha(sha_root or root)
    if not sha:
        raise Refusal("%s: %s, so no sha can be stamped" % (home, why))
    reg, entry, reads, rows, reasons = read_legacy_rows(root, home, source)
    after = {writes: derive_converted_text(reg, rows, sha)}
    if removed:
        after[reads] = None
    return after, reg, entry, reasons


def write_after(root, after):
    """Write each path of `after`, a removal last."""
    for rel, data in sorted(after.items(), key=lambda kv: kv[1] is None):
        target = pathlib.Path(root, rel)
        if data is None:
            target.unlink(missing_ok=True)
        else:
            LL._write_atomic(target, data)


def print_reasons(reasons):
    for key, reason in reasons:
        print(" · ".join([REASON_LEAD, "\t".join(key), reason]))


def cmd_convert(root, home):
    after, reg, _entry, reasons = derive_after(root, home)
    if not after:
        print("%s: %s already reads as a ledger, or holds no legacy file; nothing written" % (SAY, reg.home))
        return 0
    write_after(root, after)
    print_reasons(reasons)
    print("%s: %s converted, population %s" % (SAY, reg.home, reg.population))
    return 0


def cmd_read_back(root, population):
    try:
        regs = [r for r in LL.read_registrations(root) if r.population == population]
    except ValueError as exc:
        raise Refusal(str(exc)) from None
    if len(regs) != 1:
        raise Refusal("%d registrations name %r; read-back reads exactly one" % (len(regs), population))
    reg = regs[0]
    if LL.read_home_state(pathlib.Path(root, reg.home)) != "armed":
        print("%s %s holds no row" % (LL.DEAD_PROBE_LEAD, reg.home))
        return 0
    rows, bad = LL.read_ledger(root, reg)
    if bad:
        raise Refusal("%s: %s" % (reg.home, LL.render_malformed(bad[0])))
    for key, (count, *_rest) in rows.items():
        print("\t".join([*key, str(count)]))
    return 0


USAGE = ("usage: convert_registry.py convert --home <home>\n"
         "       convert_registry.py read-back <population>")


def resolve_root(cwd):
    rc, out = LL._run_git(cwd, "rev-parse", "--show-toplevel")
    if rc != 0 or not out.strip():
        raise Refusal("not inside a git work tree")
    return out.strip()


def main(argv):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = list(argv)
    home = None
    if "--home" in args:
        i = args.index("--home")
        if i + 1 >= len(args):
            print(USAGE, file=sys.stderr)
            return 2
        home = args[i + 1]
        del args[i:i + 2]
    try:
        if args == ["convert"] and home:
            root = resolve_root(os.getcwd())
            rel = pathlib.Path(os.path.relpath(pathlib.Path(os.getcwd(), home), root)).as_posix()
            return cmd_convert(root, rel)
        if len(args) == 2 and args[0] == "read-back" and home is None:
            return cmd_read_back(resolve_root(os.getcwd()), args[1])
    except (Refusal, OSError, UnicodeDecodeError) as exc:
        print("%s: %s" % (SAY, exc), file=sys.stderr)
        return 1
    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
