# **Serves:** research TOOL-aScoutedSeam-1
"""The aScoutedSeam reuse benchmark: blinded case trees, the M0 lookup arm, collection and grading.

Every figure in `2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md` is re-derived by one of the
subcommands below from the corpus `-1-3-cases.json` and the arm outputs `-1-5-results.json`. The
agent arms themselves are the `-1-6-*.js` workflow scripts; `args` writes their Workflow args.

  trees   <corpus> <src-root> <out-root> [--only id,id] [--dry-run]
          A single-branch file:// clone per case at its recorded point, so no ref and no object
          after the point is reachable; a NicoCares case also gets the inCMS core tree. An in-build
          point has the reinventing build's own folder removed in one blinding commit.
  resolve <corpus> <src-root>                  re-derive each case's point; prints, writes nothing
  d1      <corpus> <src-root> <out-root>       a detached worktree at each reinvention's parent
                                               plus that commit's first-parent diff
  args    <corpus> <tree-root> <d1-root> <script-dir> <out-dir>   batch-<n>.json, 5 cases each
  m0      <corpus> <tree-root> <out.json> [--budget N]   the shipped reuse_lookup, no agent
  collect <corpus> <results.json> <arm> <task.output> [...]   merge task outputs into one arm
  halves  <corpus> <results.json> <workflows-dir> <run-id> [...]  M3 halves, judge removed
  collect-runs <corpus> <results.json> <suffix> <task.output> [...]  a re-run parent, arms suffixed
  grade   [--k N] <corpus> <results.json> <arm>          per-case and total, path+symbol matcher
  compare <corpus> <results.json> <arm> [<arm> ...]      paired, over cases every arm answered
  misses  <corpus> <results.json> <arm> [<arm> ...]      ground truth beside each arm's seams
  cost    <workflows-dir> [<run-id> ...]                 per-agent medians by arm label

`<src-root>` holds plain clones named gov, incms and nicocares. Nothing here writes outside the
roots it is given. The matcher grades SHAPE: a seam naming a wrapper of the ground-truth seam is a
semantic hit it cannot see, which is why `misses` exists and the record adjudicates by hand.
"""
import json
import re
import shutil
import statistics
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SLUG_RE = re.compile(r"\b([abcd][A-Z][a-z]+[A-Z][a-z]+)\b")
CODE_TOKEN = re.compile(r"-{0,2}[A-Za-z_][\w-]*")
CANDIDATE_RE = re.compile(r"^- (\S+)\s+\[[^|\]]*\|\s*([^|\]]+)")
LOOKUP_PATHS = ("tools/codebase-map/reuse_lookup.py", "scripts/codebase-map/reuse_lookup.py")


def run_git(repo, *args, check=True):
    out = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True,
                         encoding="utf-8", errors="replace")
    if check and out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} in {repo}: {out.stderr.strip()}")
    return out.stdout.strip()


def read_json(path):
    """A committed record JSON opens with `// **Serves:**` lines the hygiene gate reads; skip them."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    while lines and lines[0].startswith("//"):
        lines.pop(0)
    return json.loads("\n".join(lines))


def write_json(path, doc):
    """Write JSON, keeping the `//` head lines an existing record carries for the hygiene gate."""
    path = Path(path)
    head = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.startswith("//"):
                break
            head.append(line)
    body = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"
    path.write_text("".join(h + "\n" for h in head) + body, encoding="utf-8", newline="\n")


def resolve_slug(repo, sha):
    """The build slug a reinventing commit belongs to: its subject, else a build path it touched."""
    hits = SLUG_RE.findall(run_git(repo, "log", "-1", "--format=%s%n%b", sha))
    if hits:
        return hits[0]
    for name in run_git(repo, "show", "--name-only", "--format=", sha).splitlines():
        m = re.match(r"memory/builds/([^/]+)/", name)
        if m:
            return m.group(1)
    return None


def resolve_kickoff(repo, slug, before):
    """The parent of the first commit that added the build's folder: the build's kickoff point."""
    first = run_git(repo, "log", "--reverse", "--diff-filter=A", "--format=%H", before, "--",
                    f"memory/builds/{slug}/", check=False).splitlines()
    return run_git(repo, "rev-parse", first[0] + "^") if first else None


def check_present(repo, sha, path, symbol=None):
    """The path exists at sha AND, when the symbol leads with a code-shaped token, the file names it."""
    if subprocess.run(["git", "-C", str(repo), "cat-file", "-e", f"{sha}:{path}"],
                      capture_output=True).returncode != 0:
        return False
    m = CODE_TOKEN.match((symbol or "").strip())
    tok = m.group(0) if m else ""
    if len(tok) < 3 or not (re.search(r"[A-Z_-]", tok) or (symbol or "").strip() == tok):
        return True
    return subprocess.run(["git", "-C", str(repo), "grep", "-q", "-F", "-e", tok, sha, "--", path],
                          capture_output=True).returncode == 0


def build_tree(src, sha, dest):
    if dest.exists():
        return
    branch = f"bench-{dest.parent.name}-{dest.name}"
    run_git(src, "update-ref", f"refs/heads/{branch}", sha)
    try:
        url = "file:///" + str(Path(src).resolve()).replace(chr(92), "/").lstrip("/")
        out = subprocess.run(["git", "clone", "-q", "--no-local", "--single-branch", "--no-tags",
                              "--branch", branch, url, str(dest)], capture_output=True, text=True)
        if out.returncode != 0:
            raise RuntimeError(f"clone {dest}: {out.stderr.strip()}")
        run_git(dest, "remote", "remove", "origin")
    finally:
        run_git(src, "update-ref", "-d", f"refs/heads/{branch}", check=False)


def cmd_trees(argv):
    corpus, src_root, out_root = read_json(argv[0]), Path(argv[1]), Path(argv[2])
    only = set(argv[argv.index("--only") + 1].split(",")) if "--only" in argv else None
    out_root.mkdir(parents=True, exist_ok=True)
    for c in corpus:
        if only and c["id"] not in only:
            continue
        tree = out_root / c["short"] / c["repo"]
        print(f"{c['short']} {c['id']:<34} point={c['point']} sha={c['sha'][:9]}")
        if "--dry-run" in argv:
            continue
        build_tree(src_root / c["repo"], c["sha"], tree)
        if c.get("core_point_sha"):
            build_tree(src_root / "incms", c["core_point_sha"], out_root / c["short"] / "incms")
        bdir = tree / "memory" / "builds" / (c.get("slug") or "-")
        if c["point"] == "in-build" and c.get("slug") and bdir.exists():
            shutil.rmtree(bdir)
            run_git(tree, "add", "-A")
            run_git(tree, "-c", "user.name=bench", "-c", "user.email=bench@local", "commit", "-q",
                    "-m", f"bench: blind {c['slug']}")


def cmd_resolve(argv):
    """Re-derive each case's point from its sha_before and reinvention, beside the recorded one."""
    corpus, src_root = read_json(argv[0]), Path(argv[1])
    for c in corpus:
        repo = src_root / c["repo"]
        before = run_git(repo, "rev-parse", c["sha_before"])
        rein = (c.get("reinvention") or {}).get("sha")
        slug = resolve_slug(repo, rein) if rein else None
        kick = resolve_kickoff(repo, slug, before) if slug else None
        own = [g for g in c.get("ground_truth") or [] if g.get("repo", c["repo"]) == c["repo"]]
        if kick and all(check_present(repo, kick, g["path"], g.get("symbol")) for g in own):
            point, sha = "kickoff", kick
        else:
            point, sha = ("in-build" if rein else "as-given"), before
        print(f"{c['short']} {c['id']:<34} recorded={c['point']}/{c['sha'][:9]} derived={point}/{sha[:9]}")


def cmd_d1(argv):
    corpus, src_root, out = read_json(argv[0]), Path(argv[1]), Path(argv[2])
    out.mkdir(parents=True, exist_ok=True)
    rows = {}
    for c in corpus:
        rein = (c.get("reinvention") or {}).get("sha")
        if not rein or not c.get("ground_truth"):
            continue
        repo = src_root / c["repo"]
        sha = run_git(repo, "rev-parse", rein)
        parent = run_git(repo, "rev-parse", sha + "^1")
        tree = out / c["short"] / "tree"
        if not tree.exists():
            run_git(repo, "worktree", "add", "-q", "--detach", str(tree), parent)
        diff = run_git(repo, "diff", "--stat", "--patch", parent, sha) + "\n"
        (out / f"{c['short']}.diff").write_text(diff, encoding="utf-8", newline="\n")
        rows[c["short"]] = {"id": c["id"], "repo": c["repo"], "tree": str(tree).replace(chr(92), "/"),
                            "diff": str(out / f"{c['short']}.diff").replace(chr(92), "/"),
                            "subject": run_git(repo, "log", "-1", "--format=%s", sha)}
        print(c["short"], c["id"], sha[:9], len(diff.encode("utf-8")), "bytes")
    write_json(out / "d1.cases.json", rows)


def cmd_args(argv):
    corpus, tree_root, d1_root = read_json(argv[0]), Path(argv[1]), Path(argv[2])
    script_dir, out_dir = argv[3].replace(chr(92), "/"), Path(argv[4])
    d1 = read_json(d1_root / "d1.cases.json") if (d1_root / "d1.cases.json").exists() else {}
    cases = {}
    for c in corpus:
        core = str(tree_root / c["short"] / "incms").replace(chr(92), "/")
        cases[c["short"]] = {"id": c["id"], "repo": c["repo"],
                             "tree": str(tree_root / c["short"] / c["repo"]).replace(chr(92), "/"),
                             "core_tree": core if c.get("core_point_sha") else None, "prompt": c["prompt"]}
    shorts = sorted(cases)
    for n in range(0, len(shorts), 5):
        ids = shorts[n:n + 5]
        doc = {"dir": script_dir, "ids": ids, "m1ids": ids, "cases": {i: cases[i] for i in ids},
               "d1": {i: {**d1[i], "core_tree": cases[i]["core_tree"]} for i in ids if i in d1}}
        write_json(out_dir / f"batch-{n // 5 + 1}.json", doc)
        print(f"batch-{n // 5 + 1}.json", ids)


def extract_first_sentence(text):
    return re.split(r"(?<=[.!?])\s", " ".join(text.split()), maxsplit=1)[0][:200]


def run_lookup(tree, tool, query, budget):
    """One reuse_lookup run; a probe predating --budget re-runs without it, as of its own revision."""
    argv = [sys.executable, tool, query] + (["--budget", str(budget)] if budget is not None else [])
    out = subprocess.run(argv, cwd=tree, capture_output=True, text=True, encoding="utf-8",
                         errors="replace", timeout=600)
    if out.returncode == 2 and "unrecognized arguments" in out.stderr:
        out = subprocess.run(argv[:3], cwd=tree, capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=600)
    rows = []
    for line in out.stdout.splitlines():
        m = CANDIDATE_RE.match(line)
        if m:
            rows.append((m.group(1), [f.strip() for f in m.group(2).split(",")]))
    return out.returncode, rows


def cmd_m0(argv):
    corpus, tree_root, dest = read_json(argv[0]), Path(argv[1]), argv[2]
    budget = int(argv[argv.index("--budget") + 1]) if "--budget" in argv else None
    out = {}
    for c in corpus:
        tree = tree_root / c["short"] / c["repo"]
        tool = next((p for p in LOOKUP_PATHS if (tree / p).exists()), None)
        if not tool:
            out[c["id"]] = {"seams": [], "tool": "absent"}
            print(f"{c['id']:<34} tool absent")
            continue
        rc, rows = run_lookup(tree, tool, extract_first_sentence(c["prompt"]), budget)
        seams = [{"repo": c["repo"], "path": f, "symbol": name, "binding": "SHOULD", "how": "", "rank": r}
                 for r, (name, files) in enumerate(rows, 1) for f in files]
        out[c["id"]] = {"seams": seams, "tool": tool, "rc": rc, "shown": len(rows)}
        print(f"{c['id']:<34} rc {rc} shown {len(rows)}")
    write_json(dest, {"m0": out})


def cmd_collect(argv):
    """Merge Workflow task outputs into one arm, keyed by case id. A batch output nests its arms by
    key and its cases by short id; the corpus maps a short id to its case id. A null is a dead agent
    and is left out, so a later resume can add it without overwriting a live row."""
    shorts = {c["short"]: c["id"] for c in read_json(argv[0])}
    dest, arm = Path(argv[1]), argv[2]
    acc = read_json(dest) if dest.exists() else {}
    rows = acc.setdefault(arm, {})
    for p in argv[3:]:
        res = read_json(p).get("result") or {}
        per = res.get(arm) if arm in res else res
        for short, r in (per or {}).items():
            if r is not None:
                rows[shorts.get(short, short)] = r
    write_json(dest, acc)
    print(arm, len(rows), "cases")


def cmd_collect_runs(argv):
    """Merge a re-run parent's output, keyed `<arm>-<n>` or `m2-<short>`, into arms named `<arm><suffix>`.

    An `m3h` run returns each case's two halves; they are filed as one seam list, both halves'
    candidates at SHOULD, the same union `halves` builds, so the two efforts compare like for like.
    A null is a dead agent and is left out.
    """
    shorts = {c["short"]: c["id"] for c in read_json(argv[0])}
    dest, suffix = Path(argv[1]), argv[2]
    acc = read_json(dest) if dest.exists() else {}
    for p in argv[3:]:
        for key, per in (read_json(p).get("result") or {}).items():
            arm, _, tail = key.partition("-")
            rows = acc.setdefault(arm + suffix, {})
            if arm == "m2":
                if per:
                    rows[shorts.get(tail, tail)] = per
                continue
            for short, r in (per or {}).items():
                if r is None:
                    continue
                if arm == "m3h":
                    seams = [{**x, "binding": "SHOULD", "half": kind}
                             for kind in ("code", "design") for x in ((r.get(kind) or {}).get("candidates") or [])]
                    r = {"seams": seams, "halves": [k for k in ("code", "design") if r.get(k)]}
                rows[shorts.get(short, short)] = r
    write_json(dest, acc)
    print({a: len(v) for a, v in acc.items() if a.endswith(suffix)})


def cmd_halves(argv):
    """M3 with its judge removed: the union of the code and design halves' candidates, read from the
    journals because most judges died at a session limit while the halves had finished."""
    shorts = {c["short"]: c["id"] for c in read_json(argv[0])}
    dest, root = Path(argv[1]), Path(argv[2])
    acc = read_json(dest) if dest.exists() else {}
    union = acc.setdefault("m3u", {})
    for run in argv[3:]:
        labels, results = {}, {}
        for line in (root / run / "journal.jsonl").read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            if row.get("type") == "started":
                labels[row["key"]] = row.get("label") or ""
            elif row.get("type") == "result":
                results[row["key"]] = row.get("result")
        for key, label in labels.items():
            kind, _, case = label.partition(":")
            if kind in ("code", "design") and results.get(key):
                for x in results[key].get("candidates") or []:
                    union.setdefault(shorts.get(case, case), {"seams": []})["seams"].append(
                        {**x, "binding": "SHOULD", "half": kind})
    write_json(dest, acc)
    print("m3u", len(union), "cases")


def derive_path_key(p):
    return (p or "").replace(chr(92), "/").strip().lstrip("./").lower()


def extract_code_tokens(symbol):
    return [t.lower() for t in CODE_TOKEN.findall(symbol or "")
            if len(t) >= 3 and (re.search(r"[A-Z_-]", t) or (symbol or "").strip() == t)]


def check_path_match(a, b):
    a, b = derive_path_key(a), derive_path_key(b)
    return bool(a and b) and (a.endswith(b) or b.endswith(a))


def check_hit(gt, seam):
    if not check_path_match(gt["path"], seam.get("path")):
        return False
    toks = extract_code_tokens(gt.get("symbol"))
    lead = CODE_TOKEN.match((gt.get("symbol") or "").strip())
    if not toks or not lead or lead.group(0).lower() not in toks:
        return True
    text = ((seam.get("symbol") or "") + " " + (seam.get("how") or "")).lower()
    return any(t in text for t in toks)


def check_case(case, res, k=None):
    """One case's verdict: items hit, the primary's rank and binding, SOLVED, and decoy MUSTs.

    A decoy matches on its path AND its symbol, because one file can hold the right seam and the
    wrong one: `resolveEntryImage` and `imageField` share a file in inCMS.
    """
    seams = (res or {}).get("seams") or []
    rows = []
    for g in case.get("ground_truth") or []:
        best = next(((s.get("rank", si + 1), s.get("binding")) for si, s in enumerate(seams)
                     if check_hit(g, s)), None)
        rows.append({"rank": best[0] if best else None, "binding": best[1] if best else None})
    decoys = case.get("decoys") or []
    false_must = [s for s in seams if s.get("binding") == "MUST" and any(check_hit(d, s) for d in decoys)]
    solved = (bool(rows) and rows[0]["rank"] is not None and rows[0]["binding"] in ("MUST", "SHOULD")
              and (k is None or rows[0]["rank"] <= k))
    return {"id": case["id"], "point": case.get("point"), "n_gt": len(rows),
            "hit": sum(1 for r in rows if r["rank"] is not None), "solved": solved,
            "primary_rank": rows[0]["rank"] if rows else None, "n_seams": len(seams),
            "n_must": sum(1 for s in seams if s.get("binding") == "MUST"), "false_must": len(false_must)}


def cmd_grade(argv):
    k = None
    if "--k" in argv:
        i = argv.index("--k")
        k, argv = int(argv[i + 1]), argv[:i] + argv[i + 2:]
    corpus, arm = read_json(argv[0]), read_json(argv[1])[argv[2]]
    graded = [check_case(c, arm[c["id"]], k) for c in corpus if c["id"] in arm]
    for g in graded:
        print(f"{g['id']:<34} {g['point']:<9} gt {g['hit']}/{g['n_gt']} solved={str(g['solved'])[0]} "
              f"prim={g['primary_rank']} seams={g['n_seams']} must={g['n_must']} decoyMUST={g['false_must']}")
    pos = [g for g in graded if g["n_gt"]]
    print(f"# {argv[2]}: positives {len(pos)} solved {sum(g['solved'] for g in pos)} · items "
          f"{sum(g['hit'] for g in pos)}/{sum(g['n_gt'] for g in pos)} · controls {len(graded) - len(pos)} "
          f"decoy MUSTs {sum(g['false_must'] for g in graded)} · graded {len(graded)} of {len(corpus)}")


def cmd_compare(argv):
    corpus, results = read_json(argv[0]), read_json(argv[1])
    arms = {a: results[a] for a in argv[2:]}
    common = [c for c in corpus if all(c["id"] in rows for rows in arms.values())]
    tot = {a: [0, 0, 0, 0, 0, 0] for a in arms}
    for c in common:
        cells = []
        for a, rows in arms.items():
            g = check_case(c, rows[c["id"]])
            for i, v in enumerate((g["solved"], g["hit"], g["n_gt"], g["n_seams"], g["n_must"], g["false_must"])):
                tot[a][i] += v
            prim = "-" if g["primary_rank"] is None else g["primary_rank"]
            cells.append(f"{prim:>3} {g['hit']}/{g['n_gt']} m{g['n_must']}")
        print(f"{c['id']:<34}" + "".join(f"{x:>16}" for x in cells))
    pos = sum(1 for c in common if c.get("ground_truth"))
    print(f"# common {len(common)} ({pos} positive)")
    for a, t in tot.items():
        print(f"# {a:<4} solved {t[0]}/{pos} · items {t[1]}/{t[2]} · seams {t[3]} · MUST {t[4]} · decoy MUST {t[5]}")


def cmd_misses(argv):
    corpus, results = read_json(argv[0]), read_json(argv[1])
    arms = {a: results[a] for a in argv[2:] if a != "--all"}
    for c in corpus:
        graded = {a: check_case(c, rows[c["id"]]) for a, rows in arms.items() if c["id"] in rows}
        if not graded or ("--all" not in argv and all(g["solved"] for g in graded.values())):
            continue
        print(f"=== {c['id']}")
        for i, g in enumerate(c.get("ground_truth") or []):
            print(f"  GT{i} {g['path']} :: {str(g.get('symbol'))[:70]}")
        for a, rows in arms.items():
            if c["id"] not in rows:
                continue
            print(f"  -- {a} solved={graded[a]['solved']}")
            for si, s in enumerate(rows[c["id"]].get("seams") or []):
                print(f"    {si + 1:>2} {str(s.get('binding'))[:1]} {str(s.get('path'))[-60:]} :: "
                      f"{str(s.get('symbol'))[:60]}")


def measure_agent(meta):
    """One agent's spend from its transcript: output, input and cache-read tokens, tool calls, wall
    seconds, and whether it returned a structured result at all, since a dead agent bought nothing."""
    out_t = in_t = cache_t = tools = 0
    first = last = None
    returned = False
    for line in meta.with_name(meta.name.replace(".meta.json", ".jsonl")).read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if row.get("timestamp"):
            t = datetime.fromisoformat(row["timestamp"].replace("Z", "+00:00"))
            first, last = first or t, t
        msg = row.get("message") or {}
        if row.get("type") != "assistant":
            continue
        u = msg.get("usage") or {}
        out_t += u.get("output_tokens", 0)
        in_t += u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
        cache_t += u.get("cache_read_input_tokens", 0)
        for part in msg.get("content") or []:
            if isinstance(part, dict) and part.get("type") == "tool_use":
                tools += 1
                returned = returned or part.get("name") == "StructuredOutput"
    wall = (last - first).total_seconds() if first and last else 0
    return returned, (out_t, in_t, cache_t, tools, wall)


def cmd_cost(argv):
    root = Path(argv[0])
    runs = argv[1:] or sorted(p.name for p in root.iterdir() if p.is_dir())
    rows = {}
    for run in runs:
        for meta in (root / run).glob("agent-*.meta.json"):
            arm = (read_json(meta).get("description") or "").split(":", 1)[0]
            returned, figures = measure_agent(meta)
            rows.setdefault((arm, returned), []).append(figures)
    print(f"{'arm':<8}{'ok':>4}{'n':>4}{'out med':>9}{'in med':>9}{'cache med':>11}{'tools med':>10}{'wall med s':>11}")
    for (arm, ok), v in sorted(rows.items()):
        med = [statistics.median(x[i] for x in v) for i in range(5)]
        print(f"{arm:<8}{str(ok)[0]:>4}{len(v):>4}{med[0]:>9.0f}{med[1]:>9.0f}{med[2]:>11.0f}{med[3]:>10.0f}{med[4]:>11.0f}")


COMMANDS = {"trees": cmd_trees, "resolve": cmd_resolve, "d1": cmd_d1, "args": cmd_args, "m0": cmd_m0,
            "collect": cmd_collect, "collect-runs": cmd_collect_runs, "halves": cmd_halves, "grade": cmd_grade, "compare": cmd_compare,
            "misses": cmd_misses, "cost": cmd_cost}


def main(argv):
    if len(argv) < 2 or argv[1] not in COMMANDS:
        print(__doc__)
        return 2
    return COMMANDS[argv[1]](argv[2:]) or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
