# **Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7
# Committed as evidence for the recall measurement. The root is DERIVED here; the
# scratchpad original hardcoded this session's worktree and would resolve to nothing.
"""Join the authored seam judgements with DERIVED numbers and emit scen-3-adversarial.json.

Every numeric field here is derived from the tree at run time. Nothing numeric is typed into
authored.json. The builder REFUSES (exit 2) if any authored expected_file::expected_symbol does
not resolve to a real def in the tracked tree -- a scenario naming a symbol that is not there is
worse than no scenario, and a builder that emitted it anyway would be a probe that cannot move.

Run from the repo root:
    python build_scen3.py <authored.json> <out.json>
"""
from __future__ import annotations

import ast
import collections
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(os.getcwd())
sys.path.insert(0, str((ROOT / "tools" / "codebase-map").resolve()))
import map_lib as m  # noqa: E402


def tracked_files(pattern: str | None = None) -> list[str]:
    argv = ["git", "ls-files"] + ([pattern] if pattern else [])
    return subprocess.run(argv, capture_output=True, text=True, check=True).stdout.split()


# ---------------------------------------------------------------- def sites (ast, all tracked py)
def collect_defs() -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = collections.defaultdict(list)
    for f in tracked_files("*.py"):
        try:
            tree = ast.parse(pathlib.Path(f).read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError, OSError):
            continue
        for n in ast.walk(tree):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                out[n.name].append({"file": f, "line": n.lineno,
                                    "kind": "class" if isinstance(n, ast.ClassDef) else "function"})
    return out


# ------------------------------------------------------- reference index (the tool's OWN measure)
SYMS = json.loads((m.map_root(ROOT) / "generated" / "symbols.json").read_text(encoding="utf-8"))["symbols"]
IDX = m.build_reference_index(sorted({s["file"] for s in SYMS}), root=ROOT)

# ------------------------------------------------------------------ text doc-frequency (all files)
TEXT_DF: dict[str, int] = collections.Counter()
for _f in tracked_files():
    try:
        _t = pathlib.Path(_f).read_text(encoding="utf-8", errors="replace")
    except OSError:
        continue
    for _tok in set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*", _t)):
        TEXT_DF[_tok] += 1

# ------------------------------------------------------------------- the proposed confidence signal
AMBIENT: set[str] = set(dir(str)) | set(dir(list)) | set(dir(pathlib.Path))
AMBIENT |= set(dir(__builtins__) if not isinstance(__builtins__, dict) else __builtins__)


def is_compound(name: str) -> bool:
    return ("_" in name.strip("_")) or bool(re.search(r"[a-z][A-Z]", name))


def confidence(name: str) -> dict:
    """The three signals as the proposal states them, each reported separately.

    The DF signal is reported TWICE on purpose, over the two corpora the proposal does not
    distinguish: the map's own identifier index (comments and string bodies stripped) and the raw
    text of every tracked file. They disagree for exactly the names this set is about.
    """
    ident_df = len(IDX.get(name, ()))
    text_df = TEXT_DF.get(name, 0)
    sig = {
        "not_ambient": name not in AMBIENT,
        "compound": is_compound(name),
        "rare_by_identifier_index": ident_df <= 15,
        "rare_by_text_corpus": text_df <= 15,
    }
    return {
        "signals": sig,
        "doc_freq_identifier_index": ident_df,
        "doc_freq_text_corpus": text_df,
        "tier_identifier_index": sum(
            (sig["not_ambient"], sig["compound"], sig["rare_by_identifier_index"])),
        "tier_text_corpus": sum(
            (sig["not_ambient"], sig["compound"], sig["rare_by_text_corpus"])),
    }


# ------------------------------------------------------------- bare / attribute / kwarg edge split
def edge_split(names: set[str]) -> dict[str, dict]:
    bare = collections.defaultdict(set)
    attr = collections.defaultdict(collections.Counter)
    kwarg = collections.defaultdict(set)
    for f in tracked_files("*.py"):
        try:
            tree = ast.parse(pathlib.Path(f).read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError, OSError):
            continue
        for n in ast.walk(tree):
            if isinstance(n, ast.Name) and n.id in names and isinstance(n.ctx, ast.Load):
                bare[n.id].add(f)
            elif isinstance(n, ast.Attribute) and n.attr in names:
                who = n.value.id if isinstance(n.value, ast.Name) else ast.unparse(n.value)[:28]
                attr[n.attr][who] += 1
            elif isinstance(n, ast.keyword) and n.arg in names:
                kwarg[n.arg].add(f)
    return {
        nm: {
            "bare_name_files": len(bare[nm]),
            "kwarg_label_files": len(kwarg[nm]),
            "attribute_receivers": dict(attr[nm].most_common(6)),
        }
        for nm in names
    }


def main(argv: list[str]) -> int:
    authored = json.loads(pathlib.Path(argv[1]).read_text(encoding="utf-8"))
    defs = collect_defs()
    names = {row["expected_symbol"] for row in authored}
    edges = edge_split(names)

    refusals: list[str] = []
    scenarios = []
    for row in authored:
        name, want_file = row["expected_symbol"], row["expected_file"]
        sites = defs.get(name, [])
        here = [s for s in sites if s["file"] == want_file]
        if not here:
            refusals.append(f"{row['id']}: no def of `{name}` in {want_file}")
            continue
        for alt in row.get("also_acceptable", []):
            af, _, an = alt.partition("::")
            if not any(s["file"] == af for s in defs.get(an, [])):
                refusals.append(f"{row['id']}: also_acceptable {alt} does not resolve")
        fanin = m.fan_in(IDX, name, want_file)
        conf = confidence(name)
        scenarios.append({
            # ---- the five fields the lens asked for, first and in order
            "query": row["query"],
            "expected_file": want_file,
            "expected_symbol": name,
            "why_it_is_a_real_seam": row["why_it_is_a_real_seam"],
            "name_class": row["name_class"],
            # ---- everything below is derived or provenance; a consumer may ignore it
            "id": row["id"],
            "adversarial_role": row["role"],
            "expected_line": here[0]["line"],
            "also_acceptable": row.get("also_acceptable", []),
            "same_name_definers": len(sites),
            "same_name_definer_files": sorted({s["file"] for s in sites}),
            "shipped_fan_in": fanin,
            "seam_by_shipped_threshold": fanin >= m.seam_fanin_threshold(ROOT),
            "confidence": conf,
            "edge_split": edges[name],
            "established_by": row["established_by"],
        })

    if refusals:
        print("REFUSED - authored rows that do not resolve against the tree:", file=sys.stderr)
        for r in refusals:
            print("  " + r, file=sys.stderr)
        return 2

    out = {
        "$schema_note": "lens-3 adversarial scenarios for reuse_lookup ranking; see the .md companion",
        "$generated_by": "build_scen3.py over the tracked tree",
        "$repo_head": subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                                     text=True, check=True).stdout.strip(),
        "$tree_dirty": bool(subprocess.run(["git", "status", "--porcelain"], capture_output=True,
                                           text=True, check=True).stdout.strip()),
        "$seam_fanin_threshold": m.seam_fanin_threshold(ROOT),
        "$n_scenarios": len(scenarios),
        "$corpus": {
            "tracked_py_files": len(tracked_files("*.py")),
            "symbols_json_entries": len(SYMS),
            "reference_index_tokens": len(IDX),
        },
        "scenarios": scenarios,
    }
    pathlib.Path(argv[2]).write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                                     encoding="utf-8")
    print(f"wrote {argv[2]}: {len(scenarios)} scenarios, 0 refusals")
    # a compact console table so the numbers are visible without opening the file
    print(f"{'id':7s} {'symbol':16s} {'fanin':>5s} {'identdf':>7s} {'textdf':>6s} "
          f"{'tI':>2s} {'tT':>2s}  role")
    for s in scenarios:
        c = s["confidence"]
        print(f"{s['id']:7s} {s['expected_symbol']:16s} {s['shipped_fan_in']:5d} "
              f"{c['doc_freq_identifier_index']:7d} {c['doc_freq_text_corpus']:6d} "
              f"{c['tier_identifier_index']:2d} {c['tier_text_corpus']:2d}  {s['adversarial_role']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
