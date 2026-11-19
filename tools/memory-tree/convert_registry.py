#!/usr/bin/env python3
"""convert_registry.py -- a registry's legacy grammar converted in place onto the ledger grammar
(TOOL-dWitnessedBar-16).

    python <prefix>/memory-tree/convert_registry.py convert --home <home>
    python <prefix>/memory-tree/convert_registry.py up|down|witness <target> --home <home>
    python <prefix>/memory-tree/convert_registry.py read-back <population>

`convert` reads one file of a legacy grammar `LEGACY` names, by its file name, and writes its home in
the ledger grammar through the factory's `write_rows`: the header rendered from the population's
`[[ledger]]` table, then one row per key, its count, the sha `read_head_sha` names and `seeded`. A
home holding no row is written as its header and the `# unarmed · dead probe · <sha>` line the
factory's seed writes for a dead probe. Each former reason, which the row grammar has no field for,
is printed `reason · <key> · <text>` for the conversion record. A home whose first line is already a
ledger header is said so and nothing is written, so a second run never re-dates a row. The table names
each legacy file's parser and the descriptor whose `[[ledger]]` table gives its shape, so the shape is
read from that table and never typed here; the two map lists are written to their `.txt` sibling and
the TOML removed, and drift's two populations are read from the `PINS` and `BASELINES` literals of
the project layer `drift_signals.py` beside them.

`up`, `down` and `witness` are the `[[upgrade]]` step over `<target>`: `up` writes the before-image
through `upgrade_steps.write_before_image`, then the converted file; `down` restores it through
`write_from_before_image`; `witness` exits 0 when the legacy file is absent or the home's first line
is a ledger header. The step id is `<entry>/<population>-to-ledger`, `<entry>` the descriptor's own id.

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
import importlib.util
import os
import pathlib
import re
import shutil
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
TOOLS = KIT.parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
import legacy_ledger as LL  # noqa: E402  the ledger factory, this kit's copy

SAY = "convert-registry"
REASON_LEAD = "reason"
DEAD_PROBE_REASON = "dead probe"


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


# file name -> (descriptor under the tool root, population, reader, file it reads, file it writes):
# the legacy grammars this program converts, the one table `convert` and S7's transitional read share.
LEGACY = {
    "baseline.toml": ("codebase-map/kit.toml", "baseline", read_toml_rows, "baseline.toml", "baseline.txt"),
    "affordance-exempt.toml": ("codebase-map/kit.toml", "affordance-exempt", read_exempt_rows,
                               "affordance-exempt.toml", "affordance-exempt.txt"),
    "brief-recorded-waiver.txt": ("unattended/kit.toml", "brief-recorded-waiver", read_lines_with(parse_keyed_reason(1))),
    "pass-order-waiver.txt": ("unattended/kit.toml", "pass-order-waiver", read_lines_with(parse_keyed_reason(1))),
    "curation-debt.txt": ("memory-tree/kit.toml", "curation-debt", read_lines_with(parse_spaced_reason)),
    "id-orphan-waiver.txt": ("memory-tree/kit.toml", "id-orphan-waiver", read_lines_with(parse_keyed_reason(1))),
    "legacy-files.txt": ("memory-tree/kit.toml", "legacy-files", read_lines_with(parse_spaced_reason)),
    "method-carriers.txt": ("memory-tree/kit.toml", "method-carriers", read_lines_with(parse_carrier)),
    "readme-contract.txt": ("memory-tree/kit.toml", "readme-contract", read_lines_with(parse_contract)),
    "refusal-retirements.txt": ("memory-tree/kit.toml", "refusal-retirements", read_lines_with(parse_retirement)),
    "stale-header-waiver.txt": ("memory-tree/kit.toml", "stale-header-waiver", read_lines_with(parse_spaced_reason)),
    "trace-waiver.txt": ("memory-tree/kit.toml", "trace-waiver", read_lines_with(parse_keyed_reason(2))),
    "unarmed-branches.txt": ("memory-tree/kit.toml", "unarmed-branches", read_lines_with(parse_unarmed_branch)),
    "encoding-posture-sites.txt": ("gate-lint/kit.toml", "encoding-posture-sites", read_lines_with(parse_counted_reason(2))),
    "fork-ceilings.txt": ("gate-lint/kit.toml", "fork-ceilings", read_lines_with(parse_fork_ceiling)),
    "location-probe-waivers.txt": ("gate-lint/kit.toml", "location-probe-waivers", read_lines_with(parse_counted_reason(2))),
    "spawn-idiom-sites.txt": ("gate-lint/kit.toml", "spawn-idiom-sites", read_lines_with(parse_counted_reason(2))),
    "substitution-fed-loops.txt": ("gate-lint/kit.toml", "substitution-fed-loops", read_lines_with(parse_counted_reason(2))),
    "temp-name-sites.txt": ("gate-lint/kit.toml", "temp-name-sites", read_lines_with(parse_counted_reason(2))),
    "docs-undocumented.txt": ("govkit/registry.toml", "docs-undocumented", read_lines_with(parse_keyed_reason(1))),
    "spec-token-waivers.txt": ("govkit/registry.toml", "spec-token-waivers", read_lines_with(parse_keyed_reason(1))),
    "dead-path-waivers.txt": ("govkit/registry.toml", "dead-path-waivers", read_lines_with(parse_dead_path)),
    "playbook-kit-waivers.txt": ("govkit/registry.toml", "playbook-kit-waivers", read_lines_with(parse_spaced_reason)),
    "drift-pins.txt": ("drift-audit/kit.toml", "drift-pins", read_pin_rows, "drift_signals.py", "drift-pins.txt"),
    "drift-baselines.txt": ("drift-audit/kit.toml", "drift-baselines", read_baseline_rows,
                            "drift_signals.py", "drift-baselines.txt"),
}


def read_legacy_entry(home):
    """-> (descriptor, population, reader, the path it reads, the home it writes) for `home`, by name."""
    name = pathlib.PurePosixPath(home.replace("\\", "/")).name
    if name not in LEGACY:
        raise Refusal("%s: no legacy grammar of that name is known (%s)" % (home, ", ".join(sorted(LEGACY))))
    descriptor, population, reader, *names = LEGACY[name]
    parent = pathlib.PurePosixPath(home.replace("\\", "/")).parent
    reads, writes = names if names else (name, name)
    return descriptor, population, reader, (parent / reads).as_posix(), (parent / writes).as_posix()


def derive_registration(descriptor, population, home):
    """The `Registration` of `population` from its descriptor under the tool root, homed at `home`;
    with the descriptor's own id, the `<entry>` a step id carries."""
    path = TOOLS / descriptor
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise Refusal("%s: does not read as TOML: %s" % (path, exc)) from None
    tables = [t for t in data.get("ledger", []) if isinstance(t, dict) and t.get("population") == population]
    if len(tables) != 1:
        raise Refusal("%s: %d [[ledger]] tables name %r, not one" % (descriptor, len(tables), population))
    bad = LL._check_table(tables[0])
    if bad:
        raise Refusal("%s: [[ledger]] %r: %s" % (descriptor, population, "; ".join(bad)))
    t = tables[0]
    reg = LL.Registration(population, tuple(t["seed"]), t["key"], tuple(t["fields"]), t["drain"], t["direction"],
                          home, t["leg"], tuple(t.get("verbatim", [])), descriptor)
    return reg, data.get("id") or pathlib.PurePosixPath(descriptor).parent.name


def read_legacy_rows(root, home):
    """-> (registration, entry id, the path read, {key: (count, sha-less values)}, [(key, reason)]) of
    the legacy file `LEGACY` names for `home` at `root`: an ordinal registry's equal keys merged, their
    count the number of rows; any other repeated key refused, so no row is dropped or merged."""
    descriptor, population, reader, reads, writes = read_legacy_entry(home)
    reg, entry = derive_registration(descriptor, population, writes)
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


def derive_after(root, home):
    """-> ({root-relative path: bytes, or None for removed}, registration, entry id, reasons): what
    converting `home` at `root` writes; {} where the home already reads as a ledger."""
    descriptor, population, _reader, reads, writes = read_legacy_entry(home)
    if check_ledger_header(pathlib.Path(root, writes)) or not pathlib.Path(root, reads).is_file():
        reg, entry = derive_registration(descriptor, population, writes)
        return {}, reg, entry, []
    sha, why = LL.read_head_sha(root)
    if not sha:
        raise Refusal("%s: %s, so no sha can be stamped" % (home, why))
    reg, entry, reads, rows, reasons = read_legacy_rows(root, home)
    after = {writes: derive_converted_text(reg, rows, sha)}
    if reads != writes and pathlib.PurePosixPath(reads).suffix == ".toml":
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


def load_steps():
    """The upgrade-step helpers in the deployer beside this kit, imported by their path."""
    path = TOOLS / "govkit" / "upgrade_steps.py"
    mod = sys.modules.get("upgrade_steps")
    if mod is not None and getattr(mod, "__file__", None) and pathlib.Path(mod.__file__).resolve() == path:
        return mod
    if not path.is_file():
        raise Refusal("no deployer at %s, so no before-image can be written" % path.parent)
    spec = importlib.util.spec_from_file_location("upgrade_steps", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["upgrade_steps"] = mod
    spec.loader.exec_module(mod)
    return mod


def derive_step_id(home):
    descriptor, population, _reader, _reads, writes = read_legacy_entry(home)
    _reg, entry = derive_registration(descriptor, population, writes)
    return "%s/%s-to-ledger" % (entry, population)


def cmd_up(target, home):
    steps = load_steps()
    held = {}

    def derive(before):
        after, _reg, _entry, reasons = derive_after(target, home)
        if before is not None and not after:
            # A re-run over a completed up: the image's before bytes are the legacy file.
            scratch = tempfile.mkdtemp(prefix="cr")
            try:
                for rel, data in before.items():
                    if data is not None:
                        pathlib.Path(scratch, rel).parent.mkdir(parents=True, exist_ok=True)
                        pathlib.Path(scratch, rel).write_bytes(data)
                sha, why = LL.read_head_sha(target)
                if not sha:
                    raise Refusal("%s: %s" % (home, why))
                reg, _entry, reads, rows, reasons = read_legacy_rows(scratch, home)
                after = {reg.home: derive_converted_text(reg, rows, sha)}
                if reads != reg.home and pathlib.PurePosixPath(reads).suffix == ".toml":
                    after[reads] = None
            finally:
                shutil.rmtree(scratch, ignore_errors=True)
        held["reasons"] = reasons
        return after

    try:
        after = steps.write_before_image(target, derive_step_id(home), derive)
    except steps.Refusal as exc:
        raise Refusal(str(exc)) from None
    write_after(target, after)
    print_reasons(held.get("reasons", []))
    print("%s: up · %s" % (SAY, ("%s converted" % ", ".join(sorted(after))) if after else "nothing to convert"))
    return 0


def cmd_down(target, home):
    steps = load_steps()
    try:
        restored = steps.write_from_before_image(target, derive_step_id(home))
    except steps.Refusal as exc:
        raise Refusal(str(exc)) from None
    print("%s: down · restored %s" % (SAY, ", ".join(restored) or "nothing: no before-image, no up applied"))
    return 0


def cmd_witness(target, home):
    _descriptor, _population, _reader, reads, writes = read_legacy_entry(home)
    if not pathlib.Path(target, reads).is_file() or check_ledger_header(pathlib.Path(target, writes)):
        print("%s: witness · %s reads as a ledger or holds no legacy file: applied" % (SAY, writes))
        return 0
    print("%s: witness · %s is in its legacy grammar: not applied" % (SAY, reads))
    return 1


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
         "       convert_registry.py up|down|witness <target> --home <home>\n"
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
        if len(args) == 2 and args[0] in ("up", "down", "witness") and home:
            target = pathlib.Path(args[1]).resolve()
            return {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}[args[0]](target, home)
        if len(args) == 2 and args[0] == "read-back" and home is None:
            return cmd_read_back(resolve_root(os.getcwd()), args[1])
    except (Refusal, OSError, UnicodeDecodeError) as exc:
        print("%s: %s" % (SAY, exc), file=sys.stderr)
        return 1
    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
