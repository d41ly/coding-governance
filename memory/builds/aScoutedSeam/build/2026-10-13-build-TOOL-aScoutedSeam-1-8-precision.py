# **Serves:** research TOOL-aScoutedSeam-1
"""Offline reading of the committed benchmark results: where the wrong MUSTs come from, which
deterministic demotion rule removes them at what cost, and why the M1c misses were missed.

No agent runs. Reads the committed corpus, results and judge verdicts, and the frozen case trees
`bench.py trees` builds (machine-local, under --tree-root) for the existence and house-index probes.

    python <this> [--tree-root <dir>] precision <arm>...
    python <this> [--tree-root <dir>] misses
    python <this> [--tree-root <dir>] expansion

What it does NOT check: the judge's verdicts are taken as given, the edit-shaped pattern is a
heuristic over `how` and `symbol` text, and a demotion is simulated on the recorded order, never
re-run through an agent.
"""
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEM = "2026-10-11-build-TOOL-aScoutedSeam-1-"
_spec = importlib.util.spec_from_file_location("bench", str(HERE / (STEM + "4-bench.py")))
bench = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bench)

EDIT_HOW = re.compile(r"^\s*(add|append|register|declare|write|create|regenerate|regen|re-render|rerender|bump|"
                      r"update|edit|insert|record|document|claim|raise|list|stage|run\b|keep|re-stamp|restamp|mirror)",
                      re.I)
EDIT_SYM = re.compile(r"(row|entry|section|heading|line|claim|pin|stamp|version|test arm|arm\b|fixture|leg\b)", re.I)
WHY_CLASSES = (
    ("edit/wiring/regen", r"edit|regen|re-render|register|wiring|add a|append|row|declare|bump|claim|update"),
    ("test/gate", r"\btest|gate|leg\b|fixture|self-test|selftest"),
    ("doc/spec/record", r"spec\b|document|record|plan|readme|charter|decision"),
    ("stale copy", r"stale|copy|duplicate"),
    ("not exist/unreachable", r"not exist|does not exist|nonexist|unreachable|absent"))
LOOKED = ("d1", "d1@medium", "m1", "m1b", "m1@medium", "m1b@medium", "m3u", "m3@medium")


def load_inputs(tree_root):
    corpus = {c["id"]: c for c in json.loads((tree_root / "cases.resolved.json").read_text(encoding="utf-8"))}
    return corpus, bench.read_json(str(HERE / (STEM + "5-results.json")))


def check_exists_at_point(tree_root, case, seam, cache):
    """`sym` when the seam's path is a file in the case tree holding its lead code token, `path` when
    the symbol carries no code token, else `nosym`, `dir` or `absent`."""
    path = (seam.get("path") or "").replace(chr(92), "/").strip().lstrip("./")
    for repo in [seam.get("repo"), case["repo"], "incms", "gov", "nicocares"]:
        if not repo:
            continue
        f = tree_root / case["short"] / repo / path
        if f.is_file():
            toks = bench.extract_code_tokens(seam.get("symbol"))
            if not toks:
                return "path"
            text = cache.setdefault(str(f), f.read_text(encoding="utf-8", errors="replace").lower())
            return "sym" if any(t in text for t in toks) else "nosym"
        if f.is_dir():
            return "dir"
    return "absent"


def derive_why_class(why):
    return next((name for name, pat in WHY_CLASSES if re.search(pat, why.lower())), "other")


def derive_seam_key(seam):
    toks = bench.extract_code_tokens(seam.get("symbol")) or [""]
    return bench.derive_path_key(seam.get("path")), toks[0]


def derive_must_rows(tree_root, corpus, res, arm):
    """One row per MUST seam of one arm: judge-wrong, ground-truth hit, existence, edit shape, the
    other M1c run's agreement, and its rank among the case's MUSTs."""
    judge, rows, whys, cache = res["judge"], [], Counter(), {}
    twin = {"m1cA@medium": "m1cB@medium", "m1cB@medium": "m1cA@medium"}.get(arm)
    for cid, r in res[arm].items():
        case = corpus.get(cid)
        if not case or not r:
            continue
        wrong = {w["seam"]: w.get("why", "") for w in (judge.get(arm, {}).get(cid) or {}).get("wrong") or []}
        twin_must = {derive_seam_key(s) for s in (res[twin].get(cid) or {}).get("seams") or []
                     if s.get("binding") == "MUST"} if twin else None
        seams = r.get("seams") or []
        for i, s in enumerate(seams):
            if s.get("binding") != "MUST":
                continue
            rows.append({"wrong": i in wrong,
                         "gt": any(bench.check_hit(g, s) for g in case.get("ground_truth") or []),
                         "exists": check_exists_at_point(tree_root, case, s, cache),
                         "edit": bool(EDIT_HOW.match(s.get("how") or "") or EDIT_SYM.search(s.get("symbol") or "")),
                         "both": None if twin_must is None else derive_seam_key(s) in twin_must,
                         "must_rank": sum(1 for t in seams[:i] if t.get("binding") == "MUST")})
            if i in wrong:
                whys[derive_why_class(wrong[i])] += 1
    return rows, whys


def measure_demotion(rows, demote):
    """What demoting the matching MUSTs to SHOULD removes: wrong ones, ground-truth ones, and what is left."""
    out = [x for x in rows if demote(x)]
    keep = [x for x in rows if not demote(x)]
    return {"demoted": len(out), "wrong": sum(x["wrong"] for x in out), "gt": sum(x["gt"] for x in out),
            "left": len(keep), "left_wrong": sum(x["wrong"] for x in keep)}


def run_precision(tree_root, arms):
    corpus, res = load_inputs(tree_root)
    rules = [("F1 path+symbol absent at the point", lambda x: x["exists"] in ("absent", "nosym", "dir")),
             ("F2 edit-shaped how or symbol", lambda x: x["edit"]),
             ("F3 MUST cap 3 per case", lambda x: x["must_rank"] >= 3),
             ("F3 MUST cap 5 per case", lambda x: x["must_rank"] >= 5),
             ("F4 MUST only where both runs bind it", lambda x: x["both"] is False)]
    for arm in arms:
        rows, whys = derive_must_rows(tree_root, corpus, res, arm)
        nw = sum(x["wrong"] for x in rows)
        print(f"=== {arm}: {len(rows)} MUSTs, judge-wrong {nw}, ground-truth hits {sum(x['gt'] for x in rows)}")
        print("  wrong by judge reason:", dict(whys.most_common()))
        print("  existence at the point:", dict(Counter(x["exists"] for x in rows)))
        for name, rule in rules:
            if name.startswith("F4") and rows and rows[0]["both"] is None:
                continue
            m = measure_demotion(rows, rule)
            print(f"  {name:<40} demotes {m['demoted']:>3}: wrong {m['wrong']:>2}, ground-truth {m['gt']:>2};"
                  f" left {m['left']:>3} MUSTs, {m['left_wrong']:>2} wrong")


def run_misses(tree_root):
    corpus, res = load_inputs(tree_root)
    judge = res["judge"]
    print("== paired judge precision, extra -> medium, over the cases both efforts answered")
    for a, b in (("m1", "m1@medium"), ("m1b", "m1b@medium")):
        common = [c for c in judge[a] if c in judge[b] and res[a].get(c) and res[b].get(c)]
        cells = []
        for arm in (a, b):
            musts = sum(1 for c in common for s in res[arm][c].get("seams") or [] if s.get("binding") == "MUST")
            wrong = sum(len(judge[arm][c].get("wrong") or []) for c in common)
            cells.append(f"{arm} MUST {musts} wrong {wrong}")
        print(f"  {len(common)} cases: " + " | ".join(cells))
    missed = [cid for cid, c in corpus.items() if c.get("ground_truth")
              and not judge["m1cA@medium"].get(cid, {}).get("primary")
              and not judge["m1cB@medium"].get(cid, {}).get("primary")]
    print("== positives neither M1c run found, by the judge:", " ".join(missed))
    for cid in missed:
        c = corpus[cid]
        g0 = c["ground_truth"][0]
        toks = bench.extract_code_tokens(g0.get("symbol")) or [Path(g0["path"]).stem.lower()]
        idx = tree_root / c["short"] / "house-index.md"
        itext = idx.read_text(encoding="utf-8", errors="replace").lower() if idx.exists() else ""
        print(f"--- {cid}: GT0 {g0['path']} :: {str(g0.get('symbol'))[:50]} · in house index "
              f"{[t for t in toks if t in itext]}")
        for arm in ("m1cA@medium", "m1cB@medium"):
            r = res[arm].get(cid) or {}
            sketch = " | ".join(r.get("sketch") or []).lower()
            same_file = [i for i, s in enumerate(r.get("seams") or []) if bench.check_path_match(g0["path"], s.get("path"))]
            print(f"  {arm}: in sketch {[t for t in toks if t in sketch]} · same-file seams at {same_file}")
        found = [a for a in LOOKED if any(bench.check_hit(g0, s) for s in ((res.get(a) or {}).get(cid) or {}).get("seams") or [])]
        print("  found by:", " ".join(found) or "no arm")


DEFINITION = re.compile(r"^\s*(?:export\s+)?(?:async\s+)?(?:def|class|function|const|let|var)\s+([A-Za-z_$][\w$]*)"
                        r"|^([A-Za-z_]\w*)\s*\(\)\s*\{"
                        r"|^(?:readonly\s+|declare\s+-[a-zA-Z]+\s+)?([A-Z][A-Z0-9_]{2,})=", re.M)
CODE_SUFFIXES = (".py", ".js", ".ts", ".tsx", ".sh", ".mjs")


def extract_definitions(path):
    """Top-level-looking definitions in one file, constants included: a regex, not a parser."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return set()
    return {next(g for g in m.groups() if g) for m in DEFINITION.finditer(text)}


def resolve_case_file(tree_root, case, path):
    path = (path or "").replace(chr(92), "/").strip().lstrip("./")
    for repo in (case["repo"], "incms", "gov", "nicocares"):
        f = tree_root / case["short"] / repo / path
        if f.is_file():
            return f
    return None


def run_expansion(tree_root):
    """Would listing every definition in each cited file, or in its directory, reach a missed primary?"""
    corpus, res = load_inputs(tree_root)
    per_file, per_dir, reach = [], [], {}
    for arm in ("m1cA@medium", "m1cB@medium"):
        for cid, r in res[arm].items():
            case = corpus.get(cid)
            if not case or not r:
                continue
            files = {f for f in (resolve_case_file(tree_root, case, s.get("path")) for s in r.get("seams") or []) if f}
            fdefs = {d.lower() for f in files for d in extract_definitions(f)}
            ddefs = {d.lower() for d in {f.parent for f in files} for x in d.iterdir()
                     if x.is_file() and x.suffix in CODE_SUFFIXES for d in extract_definitions(x)}
            per_file.append(len(fdefs))
            per_dir.append(len(ddefs))
            gt = case.get("ground_truth") or []
            if gt:
                tok = (bench.extract_code_tokens(gt[0].get("symbol")) or [""])[0]
                hit = any(bench.check_hit(gt[0], s) for s in r.get("seams") or [])
                reach.setdefault(cid, []).append("hit" if hit else "file" if tok in fdefs else "dir" if tok in ddefs else "-")
    per_file.sort()
    per_dir.sort()
    print(f"definitions per case, cited files expanded: median {per_file[len(per_file) // 2]} · max {per_file[-1]}")
    print(f"definitions per case, cited directories expanded: median {per_dir[len(per_dir) // 2]} · max {per_dir[-1]}")
    for cid, v in reach.items():
        if "hit" not in v:
            print(f"  {cid:<34} A {v[0]} · B {v[-1]}")


def main(argv):
    tree_root = Path("C:/Users/daily-agent/AppData/Local/Temp/rsb")
    if argv[:1] == ["--tree-root"]:
        tree_root, argv = Path(argv[1]), argv[2:]
    if argv[:1] == ["precision"] and argv[1:]:
        run_precision(tree_root, argv[1:])
    elif argv == ["misses"]:
        run_misses(tree_root)
    elif argv == ["expansion"]:
        run_expansion(tree_root)
    else:
        print(__doc__, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
