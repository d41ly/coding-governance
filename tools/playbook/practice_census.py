#!/usr/bin/env python3
"""practice_census.py — which rows of the practice catalogue gov ships, and which are gov's own (PLAY-dOrderedCharter-34 S7).

    python practice_census.py [--target <tree>]   # one ruling per row of the catalogue, with its evidence
    python practice_census.py --plant <case>      # gov-only | no-evidence | row-kept | outside-foundation

THE PREDICATE. A row rules `gov-only` when all four hold, and `ship` otherwise:

  1. its `line` names a repository path in backticks, or a leg of `gate-legs.json` names it in `enforces`, so
     the ruling rests on evidence;
  2. every path it names is shipped by no registry entry, no descriptor's `home` holding it and no `claims`
     list naming it, or it is an `[[exempt]]` path of the registry;
  3. every leg naming it is an `[[exempt_leg]]` of the registry, a leg gov runs and ships to no adopter;
  4. no role definition cites its short name in `rules:`.

A leg names a row when its `enforces` holds the row's tag or one of its rule tags, `<tag>.<rule>` per name in
the row's `rules`: the join `core.run_meta_check` makes over the same two files. A backticked token is a path
when the tree tracks it, or a directory of tracked files; one holding a `{{...}}` placeholder is an adopter's
path and counts as shipped. A row with no evidence rules `ship`.

THE DISPOSITION, printed beside each `gov-only` ruling: `moves` for a `foundation` row no leg names, its row
and pending rows leaving with its `foundation` entry; `moves, row kept` for a `foundation` row a leg names, the
row staying as the tags' declaring source; `stays` for a row outside `foundation`, which gov's charter does not
render. Exit 0 printed, 1 a plant whose ruling is not the one it expects, 2 usage or an unreadable input.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import tomllib

sys.dont_write_bytecode = True

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import instruction_units as iu  # noqa: E402

SAY = "census"
TICK_RE = re.compile(r"`([^`\n]+)`")
ADOPTER_PATH = "an adopter's path"
SHIP, GOV_ONLY = "ship", "gov-only"
MOVES, ROW_KEPT, STAYS = "moves", "moves, row kept", "stays"


class CensusRefused(ValueError):
    """An input the census cannot read, naming it."""


def read_census_tree(root) -> dict:
    """The census's inputs under `root`: the catalogue's rows and `foundation`, every leg with an `enforces`,
    the registry's exempt legs, exempt paths, each entry's home and claims, the tracked paths and the short
    names the roles' `rules:` lines cite."""
    import core
    from tag_index import resolve_prefix_token
    root, prefix = pathlib.Path(root), iu.derive_kit_prefix()
    try:
        cat = tomllib.loads((root / prefix / KIT_DIR.name / "practices.toml").read_text(encoding="utf-8"))
        reg = tomllib.loads((root / prefix / "govkit" / "registry.toml").read_text(encoding="utf-8"))
        legs = core.read_legs(root, prefix) or []
    except (OSError, tomllib.TOMLDecodeError, core.CoreRefused) as exc:
        raise CensusRefused(f"an input is unreadable: {exc}") from None
    homes, claims = {}, {}
    for entry in reg.get("entry") or []:
        try:
            desc = tomllib.loads((root / resolve_prefix_token(entry.get("descriptor", ""), prefix)).read_text(
                encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            raise CensusRefused(f"the descriptor of {entry.get('id')} is unreadable: {exc}") from None
        home = str(desc.get("home") or ".")
        if home != ".":   # ponytail: a flat entry's home is the tool root, which holds every kit; its claims ship
            homes[home if desc.get("home_root_relative") else f"{prefix}/{home}"] = entry["id"]
        for rule in desc.get("files") or []:
            for spelled in rule.get("claims") or []:
                claims[resolve_prefix_token(spelled, prefix)] = entry["id"]
    cited = set()
    for agent in sorted((root / prefix / "roles" / "agents").glob("*.agent.md")):
        m = re.search(r"^rules:[ \t]*(.*)$", agent.read_text(encoding="utf-8"), re.M)
        cited |= {n.strip().rstrip("?") for n in (m.group(1).split(",") if m else []) if n.strip()}
    return {"rows": [r for r in cat.get("practice") or [] if isinstance(r, dict)],
            "foundation": set(cat.get("foundation") or []),
            "legs": [(leg["name"], leg.get("enforces")) for leg in legs if isinstance(leg.get("enforces"), list)],
            "exempt_legs": {r.get("name") for r in reg.get("exempt_leg") or []},
            "exempt": {resolve_prefix_token(r.get("path", ""), prefix) for r in reg.get("exempt") or []},
            "homes": homes, "claims": claims, "cited": cited,
            "tracked": set(iu.run_git(root, "ls-files").splitlines())}


def derive_shipper(path, tree) -> str | None:
    """The entry shipping `path`, ADOPTER_PATH for a placeholder, or None where it is gov's alone: an exempt
    path, or one no home holds and no claim names."""
    if "{{" in path:
        return ADOPTER_PATH
    bare = path.rstrip("/")

    def check_held(base) -> bool:
        return bare == base or bare.startswith(base + "/")

    if any(check_held(x) for x in tree["exempt"]):
        return None
    return tree["claims"].get(bare) or next((e for h, e in tree["homes"].items() if check_held(h)), None)


def derive_named_paths(line, tree) -> list:
    """The backticked tokens of `line` that are repository paths: a placeholder, a tracked file, or a
    directory of tracked files."""
    out = []
    for token in TICK_RE.findall(line or ""):
        bare = token.rstrip("/")
        if "{{" in token or bare in tree["tracked"] or any(t.startswith(bare + "/") for t in tree["tracked"]):
            out.append(token)
    return out


def derive_ruling(row, tree) -> dict:
    """One row's evidence, ruling and, where `gov-only`, its disposition."""
    tag = row.get("tag", "")
    names = {tag} | {f"{tag}.{r}" for r in row.get("rules") or []}
    legs = [(name, t) for name, enforces in tree["legs"] for t in enforces if t in names]
    paths = [(p, derive_shipper(p, tree)) for p in derive_named_paths(row.get("line"), tree)]
    short = tag.split(".", 1)[-1]
    gov_only = (bool(paths or legs) and all(s is None for _p, s in paths)
                and all(name in tree["exempt_legs"] for name, _t in legs) and short not in tree["cited"])
    found = tag in tree["foundation"]
    disposition = (ROW_KEPT if found and legs else MOVES if found else STAYS) if gov_only else None
    return {"tag": tag, "paths": paths, "legs": legs, "cited": short in tree["cited"],
            "ruling": GOV_ONLY if gov_only else SHIP, "disposition": disposition}


def render_census(rulings, tree) -> list:
    """Per row its ruling line, then a line per named path, per enforcing leg and for a cited name; then the tally."""
    out = []
    for r in rulings:
        out.append(f"{SAY}: {r['tag']} · {r['ruling']}" + (f" · {r['disposition']}" if r["disposition"] else ""))
        out += [f"{SAY}:   path `{p}` · " + (f"shipped by {s}" if s else GOV_ONLY) for p, s in r["paths"]]
        out += [f"{SAY}:   leg {name!r} · {'exempt' if name in tree['exempt_legs'] else 'ships'} · enforces {t}"
                for name, t in r["legs"]]
        out += [f"{SAY}:   cited by a role's rules"] if r["cited"] else []
        out += [f"{SAY}:   no evidence: no path and no leg"] if not (r["paths"] or r["legs"]) else []
    gone = [r for r in rulings if r["ruling"] == GOV_ONLY]
    out.append(f"{SAY}: {len(rulings)} row(s) · {SHIP} {len(rulings) - len(gone)} · {GOV_ONLY} {len(gone)}"
               + "".join(f" · {d} {sum(r['disposition'] == d for r in gone)}" for d in (MOVES, ROW_KEPT, STAYS)))
    return out


#: Each plant's one-row tree: `(row, in foundation, paths it tracks, legs, exempt legs)`, and what it expects.
PLANTS = {
    "gov-only": (({"tag": "practice.fx", "line": "Keep `tools/gov-only.txt` current."}, True,
                  {"tools/gov-only.txt"}, [], set()), (GOV_ONLY, MOVES)),
    "no-evidence": (({"tag": "practice.fx", "line": "Say it plainly."}, True, set(), [], set()), (SHIP, None)),
    "row-kept": (({"tag": "practice.fx", "rules": ["one"], "line": "Say it plainly."}, True, set(),
                  [("fixture leg", ["practice.fx.one"])], {"fixture leg"}), (GOV_ONLY, ROW_KEPT)),
    "outside-foundation": (({"tag": "practice.fx", "line": "Keep `tools/gov-only.txt` current."}, False,
                            {"tools/gov-only.txt"}, [], set()), (GOV_ONLY, STAYS)),
}


def run_plant(name) -> tuple[list, int]:
    """One plant's census over its one-row tree, and whether it ruled what the plant expects."""
    (row, found, tracked, legs, exempt_legs), want = PLANTS[name]
    tree = {"rows": [row], "foundation": {row["tag"]} if found else set(), "legs": legs, "exempt_legs": exempt_legs,
            "exempt": set(), "homes": {"tools/alpha": "alpha"}, "claims": {}, "cited": set(), "tracked": tracked}
    got = derive_ruling(row, tree)
    ok = (got["ruling"], got["disposition"]) == want
    return ([f"{SAY}: plant {name} · expects {want[0]}" + (f" · {want[1]}" if want[1] else "")]
            + render_census([got], tree) + [f"{SAY}: plant {name} · {'as expected' if ok else 'NOT as expected'}"],
            0 if ok else 1)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="practice_census.py")
    ap.add_argument("--target")
    ap.add_argument("--plant", choices=list(PLANTS))
    a = ap.parse_args(argv)
    if a.plant:
        lines, rc = run_plant(a.plant)
    else:
        try:
            root = a.target or iu.run_git(KIT_DIR, "rev-parse", "--show-toplevel").strip()
            tree = read_census_tree(root)
            lines, rc = render_census([derive_ruling(r, tree) for r in tree["rows"]], tree), 0
        except (CensusRefused, iu.LevelError) as exc:
            lines, rc = [f"{SAY}: refused · {exc}"], 2
    sys.stdout.buffer.write("".join(f"{ln}\n" for ln in lines).encode("utf-8"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
