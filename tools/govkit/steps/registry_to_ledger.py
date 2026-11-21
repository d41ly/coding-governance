#!/usr/bin/env python3
"""registry_to_ledger.py — the upgrade steps `<entry>/<population>-to-ledger` (TOOL-dWitnessedBar-16
S10, §8 F20).

    python <prefix>/govkit/steps/registry_to_ledger.py up|down|witness <target> --home <home> [--from <path>]

Each row is an `[[upgrade]]` of the descriptor whose `[[ledger]]` table registers the population, one
per list that kit's adopter seeds. This program is the thin adapter between the step grammar and the
memory-tree kit's `convert_registry.py`, which it loads from gov's own checkout through
`resolve_kit_dir`, as `docs_leg.py` loads the ledger factory; the conversion, its legacy table and its
registration lookup are that module's, and none of them is restated here.

`<home>` names the ledger home, which the conversion's table is keyed by. `--from` names the legacy
file of a home that reads a named one, drift's two populations from the project layer's `PINS` and
`BASELINES`: it is read inside the target through `upgrade_steps.check_contained`, so a `..` segment, a
link on the way or a path into the git directory is refused before anything is read or written, and
every other home refuses a `--from`.

THE UP writes the before-image through `upgrade_steps.write_before_image`, then the converted home,
removing the map lists' TOML sibling, and prints each former reason the row grammar has no field for.
A home already in the ledger grammar, or a target with no legacy file, writes nothing. A re-run over
a killed up recomputes from the image's before bytes, so it converges on the first image.
THE DOWN restores every path the image lists through `write_from_before_image`.
THE WITNESS exits 0 when the legacy file is absent or the home's first line is a ledger header.

Exit 0 done, 1 refused naming the file (nothing written) or a witness not applied, 2 a usage error.
WHAT IT DOES NOT CHECK: that the target's legacy rows still name live sites; a conversion is a
regrammar at one sha and adds or drops no key.
"""

import importlib.util
import pathlib
import shutil
import sys
import tempfile

SAY = "registry-to-ledger"
HERE = pathlib.Path(__file__).resolve().parent
CONVERT_KIT = "memory-tree"
CONVERT_ANCHOR = "convert_registry.py"


def load_steps():
    """The step reader beside this file's directory, imported by its path: the runner's `-I` drops
    a program's own directory from `sys.path`, and the before-image helpers live there."""
    path = HERE.parent / "upgrade_steps.py"
    mod = sys.modules.get("upgrade_steps")
    if mod is not None and getattr(mod, "__file__", None) and pathlib.Path(mod.__file__).resolve() == path:
        return mod
    spec = importlib.util.spec_from_file_location("upgrade_steps", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["upgrade_steps"] = mod
    spec.loader.exec_module(mod)
    return mod


STEPS = load_steps()
Refusal = STEPS.Refusal


def load_conversion():
    """gov's `convert_registry.py`, found through `resolve_kit_dir` from the deployer's directory and
    imported by its path; a kit that does not resolve is a refusal naming the places looked."""
    try:
        kit = STEPS.resolve_kit_dir(CONVERT_KIT, CONVERT_ANCHOR, HERE.parent)
    except LookupError as exc:
        raise Refusal(str(exc)) from None
    path = kit / CONVERT_ANCHOR
    spec = importlib.util.spec_from_file_location("convert_registry", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["convert_registry"] = mod
    spec.loader.exec_module(mod)
    return mod


def resolve_source(target, source):
    """`--from` as a target-relative posix path, contained in the target, or None where none is given."""
    if source is None:
        return None
    STEPS.check_contained(target, source)
    return source.replace("\\", "/")


def derive_step_id(cr, home, source):
    population, _reader, _reads, writes, _removed = cr.read_legacy_entry(home, source)
    _reg, entry = cr.derive_registration(population, writes)
    return "%s/%s-to-ledger" % (entry, population)


def cmd_up(cr, target, home, source):
    held = {}

    def derive(before):
        after, _reg, _entry, reasons = cr.derive_after(target, home, source)
        if before is not None and not after:
            # A re-run over a completed up: the image's before bytes hold the legacy state.
            scratch = tempfile.mkdtemp(prefix="rl")
            try:
                for rel, data in before.items():
                    if data is not None:
                        pathlib.Path(scratch, rel).parent.mkdir(parents=True, exist_ok=True)
                        pathlib.Path(scratch, rel).write_bytes(data)
                if source is not None and source not in before:
                    pathlib.Path(scratch, source).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(pathlib.Path(target, source), pathlib.Path(scratch, source))
                after, _reg, _entry, reasons = cr.derive_after(scratch, home, source, sha_root=target)
            finally:
                shutil.rmtree(scratch, ignore_errors=True)
        held["reasons"] = reasons
        return after

    after = STEPS.write_before_image(target, derive_step_id(cr, home, source), derive)
    cr.write_after(target, after)
    cr.print_reasons(held.get("reasons", []))
    print("%s: up · %s" % (SAY, ("%s converted" % ", ".join(sorted(after))) if after else "nothing to convert"))
    return 0


def cmd_down(cr, target, home, source):
    restored = STEPS.write_from_before_image(target, derive_step_id(cr, home, source))
    print("%s: down · restored %s" % (SAY, ", ".join(restored) or "nothing: no before-image, no up applied"))
    return 0


def cmd_witness(cr, target, home, source):
    _population, _reader, reads, writes, _removed = cr.read_legacy_entry(home, source)
    if not pathlib.Path(target, reads).is_file() or cr.check_ledger_header(pathlib.Path(target, writes)):
        print("%s: witness · %s reads as a ledger or holds no legacy file: applied" % (SAY, writes))
        return 0
    print("%s: witness · %s is in its legacy grammar: not applied" % (SAY, reads))
    return 1


USAGE = "usage: python registry_to_ledger.py up|down|witness <target> --home <home> [--from <path>]\n"


def main(argv):
    args, flags = [], {}
    it = iter(argv)
    for tok in it:
        if tok in ("--home", "--from"):
            value = next(it, None)
            if value is None or tok in flags:
                sys.stderr.write(USAGE)
                return 2
            flags[tok] = value
        else:
            args.append(tok)
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(args) != 2 or args[0] not in verbs or "--home" not in flags:
        sys.stderr.write(USAGE)
        return 2
    target = pathlib.Path(args[1]).resolve()
    try:
        cr = load_conversion()
    except (Refusal, OSError) as exc:
        sys.stderr.write("%s: %s refused · %s\n" % (SAY, args[0], exc))
        return 1
    try:
        source = resolve_source(target, flags.get("--from"))
        return verbs[args[0]](cr, target, flags["--home"], source)
    except (Refusal, cr.Refusal, OSError, UnicodeDecodeError) as exc:
        sys.stderr.write("%s: %s refused · %s\n" % (SAY, args[0], exc))
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
