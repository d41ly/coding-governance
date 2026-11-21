#!/usr/bin/env python3
"""conf_pins_to_ledger.py — the upgrade steps `<entry>/<pin>-pin-to-ledger` (TOOL-dWitnessedBar-17 S8).

    python <prefix>/govkit/steps/conf_pins_to_ledger.py up|down|witness <target> --key <KEY>

One row per conf pin a check read before its population replaced it, in the descriptor of the kit owning
the check: six in memory-tree's, `DOSSIER_DECISIONS_EMPTY_PIN` in codebase-map's. `PINS` below names
each key's conf, its population and how the key goes, and nothing else: the population's table, its
home and its seed are read through the ledger factory, so no shape is typed here. Shaped as
`review_rounds.py` takes a conf key out, over `upgrade_steps.py`'s before-image helpers, and as
`registry_to_ledger.py` loads gov's memory-tree kit through `resolve_kit_dir`.

THE UP. No conf, or no `<KEY>` line in it: exit 0, nothing written. Otherwise the before-image of the
conf, `conf-scalar-pins.txt` and the population's home is written through `write_before_image`, then:
  * a COUNTED pin's population is seeded at the target's HEAD by memory-tree's `legacy_ledger.py seed
    --population <name>`, run from gov's copy with the target as its working directory. A seed that
    does not print `armed` or `present` refuses the up, restoring the home, so the key and its row stay
    in place and the bound is never lost (exit 1, nothing written);
  * a FOLDED pin's home is removed where the conf assigns the key blank, so its checks stay off as the
    blank pin left them (S4), and kept otherwise;
  * an UNSEEDED pin's population has `seed = []`, so nothing is seeded;
and only then every `<KEY>` line leaves the conf and the key's row leaves `conf-scalar-pins.txt`,
where that home holds one, through the factory's `write_rows`: a key taken out with its row left
behind reads as an `unmeasured row` in `ratchet (keys, not a scalar)`. A re-run over a killed up
recomputes from the image's before bytes and converges on the first image or refuses.
THE DOWN restores every path the image lists through `write_from_before_image`.
THE WITNESS exits 0 when the conf assigns no `<KEY>`, or there is no conf, which is the step applied.

Exit 0 done, 1 refused naming the file or the seed (nothing written) or a witness not applied, 2 a
usage error. WHAT IT DOES NOT CHECK: that the seeded rows number what the pin did; the seed measures
the target's corpus at its HEAD, which is the bound the pin would have been measured to.
"""

import importlib.util
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

SAY = "conf-pins-to-ledger"
HERE = pathlib.Path(__file__).resolve().parent
LEDGER_KIT = "memory-tree"
LEDGER_ANCHOR = "convert_registry.py"
PINS_POPULATION = "conf-scalar-pins"
COUNTED, FOLDED, UNSEEDED = "counted", "folded", "unseeded"
# <KEY> -> (its conf, the population that replaces it, how the key goes): TOOL-dWitnessedBar-17 §4 "The pins".
PINS = {
    "ORPHAN_ID_PIN": (".memory-tree.conf", "id-orphan-waiver", FOLDED),
    "DEAD_PATH_PIN": (".memory-tree.conf", "corpus-path-unresolved", FOLDED),
    "ROW_DUPLICATE_PIN": (".memory-tree.conf", "row-duplicates", COUNTED),
    "RECORD_UNBOUND_PIN": (".memory-tree.conf", "unbound-records", COUNTED),
    "SEVERITY_UNLABELLED_PIN": (".memory-tree.conf", "severity-unlabelled", UNSEEDED),
    "LIVE_ROW_PIN": (".memory-tree.conf", "live-rows", UNSEEDED),
    "DOSSIER_DECISIONS_EMPTY_PIN": (".codebase-map.conf", "dossier-decisions-empty", COUNTED),
}
ENTRY = {".memory-tree.conf": "memory-tree", ".codebase-map.conf": "codebase-map"}


def load_module(name, path):
    """A module imported by its path: the runner's `-I` drops this file's own directory from `sys.path`."""
    mod = sys.modules.get(name)
    if mod is not None and getattr(mod, "__file__", None) and pathlib.Path(mod.__file__).resolve() == path:
        return mod
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


C2P = load_module("conf_to_policy", HERE / "conf_to_policy.py")
STEPS = C2P.STEPS
Refusal = STEPS.Refusal


def load_conversion():
    """gov's `convert_registry.py`, through `resolve_kit_dir` from the deployer's directory, as
    `registry_to_ledger.py` loads it: its `LL` is memory-tree's ledger factory and its `write_after` the
    writer of an after-state."""
    try:
        kit = STEPS.resolve_kit_dir(LEDGER_KIT, LEDGER_ANCHOR, HERE.parent)
    except LookupError as exc:
        raise Refusal(str(exc)) from None
    return load_module("convert_registry", kit / LEDGER_ANCHOR)


def derive_step_id(key):
    """`<entry>/<pin>-pin-to-ledger`, the row id in the descriptor of the kit owning the key's conf."""
    conf = PINS[key][0]
    return "%s/%s-pin-to-ledger" % (ENTRY[conf], key.lower().removesuffix("_pin").replace("_", "-"))


def read_conf_blank(data: bytes, key: str) -> bool:
    """True where the conf's last `<KEY>` assignment, its comment and quotes stripped, is blank."""
    line, value = C2P.build_line_re(key), None
    for ln in data.decode("utf-8", "replace").removeprefix("﻿").split("\n"):
        m = line.match(ln.rstrip("\r"))
        if m:
            value = re.sub(r"\s+#.*$", "", m[1]).strip()
    if value is None:
        return False
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value.strip() == ""


def read_registration(cr, population):
    """The population's `Registration`, read through the factory over gov's checkout."""
    regs = [r for r in cr.LL.read_registrations(cr.resolve_checkout()) if r.population == population]
    if len(regs) != 1:
        raise Refusal("%d [[ledger]] tables name %r in gov's checkout, not one" % (len(regs), population))
    return regs[0]


def render_pins_rest(cr, data, conf, key):
    """`conf-scalar-pins.txt`'s bytes with the `(conf, key)` row drained through `write_rows`, or None
    where that home holds no such row."""
    reg = read_registration(cr, PINS_POPULATION)
    scratch = tempfile.mkdtemp(prefix="cp")
    try:
        held = pathlib.Path(scratch, "held.txt")
        held.write_bytes(data)
        rows, bad = cr.LL.read_rows(held, len(reg.fields))
        if bad:
            raise Refusal("%s: %s" % (reg.home, cr.LL.render_malformed(bad[0])))
        if (conf, key) not in rows:
            return None
        pathlib.Path(scratch, reg.home).parent.mkdir(parents=True, exist_ok=True)
        cr.LL.write_rows(scratch, reg, {k: (r[0], r[1]) for k, r in rows.items() if k != (conf, key)})
        return pathlib.Path(scratch, reg.home).read_bytes()
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


def derive_seeded_home(cr, target, reg):
    """The bytes `legacy_ledger.py seed --population <name>` writes at the target's home, the home then
    restored, so the before-image records it as it was; a seed that does not print `armed` or
    `present` is a Refusal naming its output, the home restored as well."""
    home = pathlib.Path(target, reg.home)
    was = home.read_bytes() if home.is_file() else None
    seed = [sys.executable, str(pathlib.Path(cr.KIT, "legacy_ledger.py")), "seed", "--population", reg.population]
    try:
        p = subprocess.run(seed, cwd=str(target), capture_output=True, text=True, encoding="utf-8",
                           errors="replace", stdin=subprocess.DEVNULL)
        said = (p.stdout.strip().splitlines() or [""])[-1]
        now = home.read_bytes() if home.is_file() else None
    finally:
        if was is None:
            home.unlink(missing_ok=True)
        else:
            home.write_bytes(was)
    if p.returncode != 0 or not said.startswith(("armed %s" % reg.population, "present %s" % reg.population)) \
            or now is None:
        raise Refusal("the seed of %s did not arm it, so the key and its row stay in place: %s"
                      % (reg.population, said or (p.stderr.strip().splitlines() or ["exit %d" % p.returncode])[-1]))
    return now


def cmd_up(cr, target, key):
    conf_rel, population, how = PINS[key]
    conf = target / conf_rel
    if not conf.is_file() or not C2P.check_assigned(conf.read_bytes(), key):
        print("%s: up · no %s in %s at %s, so there is nothing to move" % (SAY, key, conf_rel, target.as_posix()))
        return 0
    reg = read_registration(cr, population)
    pins_rel = read_registration(cr, PINS_POPULATION).home

    def derive_after(before):
        def held(rel):
            if before is not None:
                return before.get(rel)
            path = target / rel
            return path.read_bytes() if path.is_file() else None

        conf_was = held(conf_rel)
        after = {conf_rel: C2P.render_conf_rest(conf_was, key)}
        pins_was = held(pins_rel)
        if pins_was is not None:
            drained = render_pins_rest(cr, pins_was, conf_rel, key)
            if drained is not None:
                after[pins_rel] = drained
        home = target / reg.home
        if how == COUNTED:
            armed = cr.LL.read_home_state(home) == "armed"
            after[reg.home] = home.read_bytes() if before is not None and armed else derive_seeded_home(cr, target, reg)
        elif how == FOLDED and read_conf_blank(conf_was, key) and (before is not None and reg.home in before
                                                                    or home.is_file()):
            after[reg.home] = None
        return after

    after = STEPS.write_before_image(target, derive_step_id(key), derive_after)
    cr.write_after(target, after)
    print("%s: up · %s taken out of %s · %s" % (
        SAY, key, conf_rel, ", ".join("%s %s" % ("removed" if b is None else "wrote", p) for p, b in sorted(after.items()))))
    return 0


def cmd_down(_cr, target, key):
    restored = STEPS.write_from_before_image(target, derive_step_id(key))
    print("%s: down · restored %s" % (SAY, ", ".join(restored) or "nothing: no before-image, no up applied"))
    return 0


def cmd_witness(_cr, target, key):
    conf_rel = PINS[key][0]
    conf = target / conf_rel
    held = conf.is_file() and C2P.check_assigned(conf.read_bytes(), key)
    print("%s: witness · %s " % (SAY, conf_rel) + ("assigns %s: not applied" % key if held else
                                                   "assigns no %s, or is absent: applied" % key))
    return 1 if held else 0


USAGE = "usage: python conf_pins_to_ledger.py up|down|witness <target> --key <KEY>\n"


def main(argv):
    args, key = list(argv), None
    if "--key" in args:
        i = args.index("--key")
        key = args[i + 1] if i + 1 < len(args) else None
        del args[i:i + 2]
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(args) != 2 or args[0] not in verbs or key not in PINS:
        sys.stderr.write(USAGE)
        return 2
    target = pathlib.Path(args[1]).resolve()
    cr = None
    try:
        cr = load_conversion() if args[0] == "up" else None
        return verbs[args[0]](cr, target, key)
    except (Refusal, OSError, UnicodeDecodeError, ValueError) as exc:
        sys.stderr.write("%s: %s refused · %s\n" % (SAY, args[0], exc))
        return 1
    except Exception as exc:  # noqa: BLE001  the conversion module's own refusal type
        if cr is not None and isinstance(exc, cr.Refusal):
            sys.stderr.write("%s: %s refused · %s\n" % (SAY, args[0], exc))
            return 1
        raise


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
