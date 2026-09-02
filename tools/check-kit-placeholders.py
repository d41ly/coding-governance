#!/usr/bin/env python3
"""check-kit-placeholders.py — a declared placeholder is one its own adopter substitutes.

TOOL-dRetiredFork-19. A kit descriptor's `[[files]]` rule declares `placeholders = [...]`, and the
kit's adopter script is what turns those tokens into values. Nothing joined the two, so a descriptor
could declare a token its own adopter has never heard of and the unresolved `{{TOKEN}}` brace would
ship into every adopter's committed tree. That is not hypothetical: `TOOL-dRetiredFork-12` declared
`TOOL_ROOT` for the unattended kit, whose adopter does not substitute it, and the correction had to
be made by hand three times before it stuck.

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
    """The descriptor reader, reused rather than re-implemented (this unit's section 10)."""
    try:
        sys.path.insert(0, str(ROOT / "tools" / "govkit"))
        from govkit import load_toml  # the corpus's one descriptor reader
        return load_toml(path)
    except Exception:
        import tomllib
        with path.open("rb") as fh:
            return tomllib.load(fh)


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
    if bad:
        return 1

    exempt = [r["kit"] for r in rows if r.get("exempt")]
    print("kit-placeholders: %d kit(s) graded, %d rule-token pair(s), %d kit(s) declaring none, "
          "%d exempt by a declared `why_no_adopter`%s"
          % (len(rows), sum(len(r["declared"]) for r in rows), len(silent), len(exempt),
             (": " + ", ".join(exempt)) if exempt else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
