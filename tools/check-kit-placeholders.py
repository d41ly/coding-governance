#!/usr/bin/env python3
"""check-kit-placeholders.py — a declared placeholder is one its own adopter substitutes.

TOOL-dRetiredFork-19. A kit descriptor's `[[files]]` rule declares `placeholders = [...]`, and the
kit's adopter script is what turns those tokens into values. Nothing joined the two, so a descriptor
could declare a token its own adopter has never heard of and the unresolved `{{TOKEN}}` brace would
ship into every adopter's committed tree. That is not hypothetical: one unit in this build declared
`TOOL_ROOT` for the unattended kit, whose adopter does not substitute it, and the correction had to
be made by hand three times before it stuck. The id is deliberately not cited here — product source
naming a non-terminal spec is a drift signal this repo pins, and the dossier carries the provenance.

The data is already declared on BOTH sides. This is a join, not a heuristic.

WHAT IT DOES NOT CHECK, stated here because a structural check reads as a semantic one to everybody
who did not write it.

  It reads the adopter TEXTUALLY, grepping for the `{{TOKEN}}` spelling. It does NOT run any
  adopter — running one inside gov's own tree would write into gov. So a token substituted through
  a VARIABLE rather than through its literal spelling is invisible here and reports as
  unsubstituted. That is the ratified F1 trade: cheap and honest about its blind spot.

  It asserts ONE DIRECTION ONLY: declared is a subset of substituted. The reverse — an adopter
  substituting a token no rule declares — is legitimate, because a rule need not declare a
  placeholder list for every file the adopter touches. `--list` REPORTS the reverse; nothing gates
  on it (ratified F2).

  It grades DECLARATIONS, never rendered output. A brace that survives a real render is the
  adopter's own surviving-placeholder arm, one stage later and only for kits somebody rendered.

THE SECOND ARM, TOOL-aRepatriatedFork-10 S7: a `rendered` template may not spell `KEY=value` for a
key its own kit's configuration declares. A rendered doc becomes the ADOPTER's committed rule set,
so a value typed into the template is the shipping repo's own value stated as the adopter's — the
memory-tree HYGIENE template said `INDEX_CAP_LINES=0` into every tree that declared 500. The key
set is every key list in the descriptor's `[config]`, its `defaults`, AND every key the kit's
shipped `<config file>.example` assigns, because the caps a template cites are declared there and
in no list. `KEY={{PLACEHOLDER}}` is a render, not a leak, and passes. A key any `rendered` rule of
the same kit declares as a placeholder is EXEMPT: the kit states the adopter's value through
`{{KEY}}`, so a spelled `KEY=value` in its templates describes a value rather than claiming one (the
unattended templates' `ANCHOR_SCOPE="published"`). The cost is real and stated: once a kit renders a
key, a template of that kit re-spelling the key's value is not caught — intent, a description
versus a claim, is not textual. It does NOT check a value spelled without its key (`the cap is
250`), nor a template no `rendered` rule includes.

REFUSALS, not passes. A population of zero declaring rules REFUSES: a gate that scanned nothing
reports the same zero as a clean tree. A descriptor that is not valid TOML refuses. A descriptor
whose `[adopt]` block names no resolvable script refuses rather than skipping, because a skipped
kit is a kit this gate silently does not cover.

  python tools/check-kit-placeholders.py           # assert; exit 1 on an unsubstituted token
  python tools/check-kit-placeholders.py --list    # every pair and both directions, exit 0
"""
import pathlib
import re
import sys

KIT_PLACEHOLDERS_VERSION = "1.0"  # gov:kit kit-placeholders@1.0 — the deployer's read

#: The default subject is the tree this script ships in, so the gate leg needs no argument and
#: cannot be pointed at the wrong repository by a stray cwd. `--root` overrides it, and that flag
#: EXISTS FOR THE SELF-TEST: without it every hermetic arm silently graded the real tree instead of
#: its own fixture, and three arms passed because the real tree happens to be green — the
#: `fixture-passes-by-finding-nothing` class, inside the suite written to prevent it.
DEFAULT_ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT_GLOB = "tools/*/kit.toml"

# `{kit}` is the descriptor's own spelling for its kit directory.
_SCRIPT_IN_ARGV = re.compile(r"^\{kit\}/(?P<name>[A-Za-z0-9._-]+\.sh)$")


def load_descriptor(path):
    """The descriptor reader, reused rather than re-implemented (this unit's section 10).

    THE FALLBACK IS NARROW ON PURPOSE. An earlier revision caught bare `Exception` here and named a
    variable that did not exist, so every call raised `NameError`, was swallowed, and silently took
    the tomllib path — the reuse this section-10 line promises was not happening on any run, and
    nothing said so. A fallback that hides a bug in the thing it falls back FROM is the
    `fallback-fabricates-the-passing-value` class. It now catches ImportError alone: govkit absent is
    the one condition worth surviving, and any other failure is this file's bug and should raise.
    """
    try:
        sys.path.insert(0, str(DEFAULT_ROOT / "tools" / "govkit"))
        from govkit import load_toml  # the corpus's one descriptor reader
    except ImportError:
        import tomllib
        with path.open("rb") as fh:
            return tomllib.load(fh)
    return load_toml(path)


def read_bytes_as_text(path):
    """BYTES, not text-mode lines. A lone CR under universal newlines becomes a line boundary and
    can rewrite a token edge; latin-1 round-trips every byte without deciding an encoding."""
    return path.read_bytes().decode("latin-1")


def extract_declared(doc):
    """The union of `placeholders` across a descriptor's `[[files]]` rules."""
    out = set()
    for rule in doc.get("files", []) or []:
        for tok in rule.get("placeholders", []) or []:
            out.add(str(tok))
    return out


def resolve_adopter(kit_dir, doc):
    """The adopter script this kit's own descriptor names, from its `[adopt]` argv.

    Returns the path, or the string "exempt" for a descriptor that DECLARES it has no adopter via
    `why_no_adopter`, or None when neither holds. The exemption is honoured because it is DECLARED
    and carries its own reason: `tools/workflows/kit.toml` renders through the parity gate's own
    `--render` mode instead of a separate adopter, and redding it would be redding a kit for a
    design its descriptor states. An exemption is not coverage, so exempt kits are COUNTED and named
    on every run rather than silently passed."""
    adopt = doc.get("adopt") or {}
    argv = adopt.get("argv") or []
    for item in argv:
        m = _SCRIPT_IN_ARGV.match(str(item))
        if m:
            return kit_dir / m.group("name")
    if adopt.get("why_no_adopter"):
        return "exempt"
    return None


def scan_substituted(text):
    """Every `{{TOKEN}}` spelling the adopter mentions, INCLUDING the shell-escaped form.

    The braces are BACKSLASH-ESCAPED in the adopters that matter: the substitution is written
    `out=${out//\\{\\{KIT_DIR\\}\\}/"$KIT_REL"}`, because bare braces there would be shell syntax. A
    predicate matching only the bare spelling therefore finds NOTHING in the one file it exists to
    read. Measured before wiring, per section 7: the bare-only form redded 17 tokens across five
    kits, every one of them innocent."""
    return set(re.findall(r"\\?\{\\?\{([A-Z][A-Z0-9_]*)\\?\}\\?\}", text))


def build_report(root):
    """One row per kit that declares at least one placeholder."""
    rows = []
    silent = []
    for desc in sorted(root.glob(KIT_GLOB)):
        kit_dir = desc.parent
        doc = load_descriptor(desc)
        declared = extract_declared(doc)
        if not declared:
            silent.append(kit_dir.name)
            continue
        adopter = resolve_adopter(kit_dir, doc)
        if adopter == "exempt":
            rows.append({
                "kit": kit_dir.name, "declared": sorted(declared), "adopter": "(declared none)",
                "missing": [], "extra": [], "exempt": True,
            })
            continue
        if adopter is None or not adopter.exists():
            rows.append({
                "kit": kit_dir.name, "declared": sorted(declared), "adopter": None,
                "missing": sorted(declared), "extra": [], "exempt": False,
            })
            continue
        subs = scan_substituted(read_bytes_as_text(adopter))
        rows.append({
            "kit": kit_dir.name,
            "declared": sorted(declared),
            "adopter": adopter.relative_to(root).as_posix(),
            "missing": sorted(declared - subs),
            "extra": sorted(subs - declared),
            "exempt": False,
        })
    return rows, silent


_CONF_ASSIGN = re.compile(r"^\s*([A-Z][A-Z0-9_]*)=", re.M)


def extract_conf_keys(kit_dir, doc):
    """Every key this kit's configuration declares: the `[config]` key lists, its `defaults`, and
    the assignments in the shipped `<file>.example` beside the descriptor."""
    cfg = doc.get("config") or {}
    keys = set()
    for name, val in cfg.items():
        if "keys" in name and isinstance(val, list):
            keys.update(str(k) for k in val)
    keys.update(str(k) for k in (cfg.get("defaults") or {}))
    conf_file = cfg.get("file")
    if conf_file:
        example = kit_dir / (pathlib.PurePath(str(conf_file)).name + ".example")
        if example.is_file():
            keys.update(_CONF_ASSIGN.findall(read_bytes_as_text(example)))
    return keys


def scan_conf_leaks(root):
    """(template, key) for every `KEY=value` a `rendered` template spells for its own kit's key.

    A value is anything but whitespace, a backtick or `{` after the `=`: a bare `KEY=` in prose names
    the key, and `KEY={{...}}` is the render this arm asks for."""
    leaks = []
    templates = 0
    for desc in sorted(root.glob(KIT_GLOB)):
        kit_dir = desc.parent
        doc = load_descriptor(desc)
        keys = extract_conf_keys(kit_dir, doc)
        rendered = [r for r in (doc.get("files", []) or []) if r.get("role") == "rendered"]
        if not rendered:
            continue
        # A key the KIT renders as a placeholder is exempt: the kit states the adopter's own value
        # through `{{KEY}}`, so a `KEY=value` in its templates describes a value rather than claiming
        # one. The cost is named in the module docstring.
        rule_keys = keys - {str(p) for r in rendered for p in (r.get("placeholders", []) or [])}
        for rule in rendered:
            for pattern in rule.get("include", []) or []:
                for tpl in sorted(kit_dir.glob(str(pattern))):
                    templates += 1
                    text = read_bytes_as_text(tpl)
                    for key in sorted(rule_keys):
                        if re.search(r"(?<![A-Za-z0-9_])" + re.escape(key) + r"=[^\s`{]", text):
                            leaks.append((tpl.relative_to(root).as_posix(), key))
    return leaks, templates


def resolve_root(argv):
    """`--root <path>` if given, else the tree this script ships in."""
    if "--root" in argv:
        i = argv.index("--root")
        if i + 1 >= len(argv):
            raise SystemExit("kit-placeholders: --root needs a path")
        return pathlib.Path(argv[i + 1]).resolve()
    return DEFAULT_ROOT


def main(argv):
    listing = "--list" in argv
    root = resolve_root(argv)
    rows, silent = build_report(root)
    leaks, templates = scan_conf_leaks(root)

    if not rows:
        sys.stderr.write(
            "kit-placeholders: REFUSED — no `tools/*/kit.toml` rule declares a `placeholders` list, "
            "so this run graded NOTHING and a clean exit would report the same zero as a clean "
            "tree.\n")
        return 2

    if listing:
        for r in rows:
            print("%-16s adopter %s" % (r["kit"], r["adopter"] or "(UNRESOLVED)"))
            print("    declared    : %s" % (", ".join(r["declared"]) or "-"))
            print("    unsubstituted: %s" % (", ".join(r["missing"]) or "-"))
            print("    substituted but undeclared (reported, never gated): %s"
                  % (", ".join(r["extra"]) or "-"))
        print("kit-placeholders: %d kit(s) graded, %d declaring none: %s"
              % (len(rows), len(silent), ", ".join(silent) or "-"))
        for tpl, key in leaks:
            print("    conf value spelled: %s  %s=" % (tpl, key))
        print("kit-placeholders: %d rendered template(s) scanned for a spelled conf value, %d hit(s)"
              % (templates, len(leaks)))
        return 0

    bad = [r for r in rows if r["missing"] or r["adopter"] is None]
    for r in bad:
        if r["adopter"] is None:
            sys.stderr.write(
                "kit-placeholders: %s declares %s but its `[adopt]` block names no resolvable "
                "script, so nothing can substitute them\n" % (r["kit"], ", ".join(r["declared"])))
            continue
        for tok in r["missing"]:
            sys.stderr.write(
                "kit-placeholders: %s declares placeholder {{%s}} and its own adopter %s never "
                "substitutes it, so that brace ships unresolved to every adopter\n"
                % (r["kit"], tok, r["adopter"]))
    for tpl, key in leaks:
        sys.stderr.write(
            "kit-placeholders: %s is a rendered template and spells %s=<value>, a key its own kit's "
            "configuration declares, so the shipping repo's value ships as every adopter's — render "
            "it through a placeholder instead\n" % (tpl, key))
    if bad or leaks:
        return 1

    exempt = [r["kit"] for r in rows if r.get("exempt")]
    print("kit-placeholders: %d kit(s) graded, %d rule-token pair(s), %d kit(s) declaring none, "
          "%d exempt by a declared `why_no_adopter`%s; %d rendered template(s) spell no conf value"
          % (len(rows), sum(len(r["declared"]) for r in rows), len(silent), len(exempt),
             (": " + ", ".join(exempt)) if exempt else "", templates))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
