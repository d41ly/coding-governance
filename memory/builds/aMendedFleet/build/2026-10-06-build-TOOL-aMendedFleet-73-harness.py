#!/usr/bin/env python3
# **Serves:** journal TOOL-aMendedFleet-73
#
# The harness of the vague-brief arm: P (a plan of at most 40 lines, then build) against S (a Tier-2
# spec, then a different agent builds from it), five cells each, on a three-sentence brief. Six
# verbs, run by the trial workflow's agents and by the main loop; none of them spawns an agent.
#
#     python <this> cells   [--root R] [--blind]   # the cell repos; --blind copies the built tools
#                                                  # and the exit-0 stub under salted code names
#     python <this> freeze  [--root R]             # sha256 of the hidden suite and the decision list
#     python <this> stub    [--root R]             # the suite against an exit-0 stub: every test fails
#     python <this> hidden  [--root R] [--cells C] # the suite against each cell's tool, rows recorded
#     python <this> tokens  --session SID          # output tokens per agent, joined by prompt tag
#     python <this> aggregate [--collect R]        # COMMITTED rows only, unless --collect reads R
#     python <this> --selftest                     # the permutation test and the verdict rule
#
# `R` defaults to `%TEMP%/t73`: short, because a clone under a long scratch path fails on Windows.
# Every figure the record states is printed by `aggregate` from the committed results rows, so a fresh
# clone with no `%TEMP%` state reproduces it.
#
# WHAT THIS DOES NOT CHECK: that a probe agent ran the command it reports, or that a scorer read the
# observations honestly. The planted stub (the decision-met rate of the exit-0 tool) is the only
# liveness signal for those two stages, and `aggregate` prints it beside the verdict.
import argparse
import hashlib
import itertools
import os
import pathlib
import re
import secrets
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
STEM = "2026-10-06-build-TOOL-aMendedFleet-73-"
BRIEF = HERE / (STEM + "brief.md")
SUITE = HERE / (STEM + "hidden-suite.py")
FREEZE = HERE / (STEM + "freeze.tsv")
RESULTS = HERE / (STEM + "results.tsv")
SPEC_FORMAT = REPO / "memory" / "TEMPLATE-SPEC.md"
SERVES = "# **Serves:** journal TOOL-aMendedFleet-73\n"

ARMS = {"P": ["P1", "P2", "P3", "P4", "P5"], "S": ["S1", "S2", "S3", "S4", "S5"]}
CELLS = ["pilot"] + ARMS["P"] + ARMS["S"]
TAG_RE = re.compile(r"\[t73:([A-Za-z0-9-]+)\]")
CELL_OF_TAG = re.compile(r"^(pilot|[PS][1-5])(?:-|$)")
MARKS = ("met", "unmet", "contradicted")
DOC_MARKS = ("decided-compatible", "decided-incompatible", "silent")
STUB_SOURCE = "import sys\nsys.exit(0)\n"
GIT_ID = ["-c", "user.name=trial", "-c", "user.email=trial@invalid", "-c", "commit.gpgsign=false"]


def resolve_root(arg):
    if arg:
        return pathlib.Path(arg)
    return pathlib.Path(os.environ.get("TEMP") or tempfile.gettempdir()) / "t73"


def read_vague_brief():
    """The vague brief as a builder reads it: the journal's blockquote with its `> ` markers dropped."""
    text = BRIEF.read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if ln.startswith("> ")]
    if not lines:
        raise SystemExit(f"t73: no blockquoted brief in {BRIEF.name}")
    return "\n".join(ln[2:] for ln in lines) + "\n"


def read_decisions():
    """`(bytes of every decision row, the D ids in order)` from the brief journal."""
    rows = [ln for ln in BRIEF.read_text(encoding="utf-8").splitlines() if re.match(r"^\| D[0-9]", ln)]
    ids = [ln.split("|")[1].strip() for ln in rows]
    if len(ids) < 14 or len(set(ids)) != len(ids):
        raise SystemExit(f"t73: the decision list in {BRIEF.name} has {len(ids)} rows, need >=14 distinct")
    return ("\n".join(rows) + "\n").encode("utf-8"), ids


def derive_sha(data):
    return hashlib.sha256(data).hexdigest()


def run_git(cwd, *args):
    subprocess.run(["git", *GIT_ID, *args], cwd=str(cwd), check=True, capture_output=True,
                   text=True, encoding="utf-8")


# ---------------------------------------------------------------------------------- rows

def read_rows(path):
    """`{(kind, cell, key): value}` from a results file; comment lines are skipped."""
    out = {}
    if not path.is_file():
        return out
    for n, ln in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not ln or ln.startswith("#"):
            continue
        parts = ln.split("\t")
        if len(parts) != 4:
            raise SystemExit(f"t73: {path.name}:{n} is not a kind/cell/key/value row")
        out[tuple(parts[:3])] = parts[3]
    return out


def write_rows(path, rows):
    body = "".join("\t".join((*k, v)) + "\n" for k, v in sorted(rows.items()))
    path.write_bytes((SERVES + "# kind\tcell\tkey\tvalue\n" + body).encode("utf-8"))


def set_rows(path, new):
    rows = read_rows(path)
    rows.update(new)
    write_rows(path, rows)


# ---------------------------------------------------------------------------------- cells

def cmd_cells(a):
    root = resolve_root(a.root)
    if a.blind:
        return build_blind(root)
    cells = root / "cells"
    if cells.exists() and any(cells.iterdir()):
        raise SystemExit(f"t73: {cells} already holds cells; remove it to start again")
    brief = read_vague_brief()
    for cell in CELLS:
        d = cells / cell
        d.mkdir(parents=True)
        (d / "brief.md").write_bytes(brief.encode("utf-8"))
        if cell.startswith("S"):
            shutil.copyfile(SPEC_FORMAT, d / "SPEC-FORMAT.md")
        run_git(d, "init", "-q")
        run_git(d, "add", "-A")
        run_git(d, "commit", "-q", "-m", "brief")
        print(f"cell {cell}: {d}")
    return 0


def build_blind(root):
    """Each arm tool and the stub under a salted code name; the key stays outside the blind dir."""
    blind = root / "blind"
    if blind.exists():
        raise SystemExit(f"t73: {blind} exists; the code names are minted once")
    stub = root / "stub" / "declared.py"
    stub.parent.mkdir(parents=True, exist_ok=True)
    stub.write_text(STUB_SOURCE, encoding="utf-8")
    sources = {c: root / "cells" / c / "declared.py" for c in ARMS["P"] + ARMS["S"]}
    sources["stub"] = stub
    names = set()
    while len(names) < len(sources):
        names.add("t" + secrets.token_hex(3))
    key = []
    for (cell, src), code in zip(sorted(sources.items()), sorted(names)):
        (blind / code).mkdir(parents=True)
        if src.is_file():
            shutil.copyfile(src, blind / code / "declared.py")
        else:
            print(f"cell {cell}: NO TOOL; its code name holds an empty directory and scores 0")
        key.append(f"{code}\t{cell}\n")
    (root / "blind-key.tsv").write_text("".join(sorted(key)), encoding="utf-8")
    print(f"blind: {len(key)} tools under {blind}; key at {root / 'blind-key.tsv'}")
    return 0


# ---------------------------------------------------------------------------------- the suite

def cmd_freeze(a):
    rows, _ = read_decisions()
    FREEZE.write_bytes((SERVES + f"hidden-suite\t{derive_sha(SUITE.read_bytes())}\n"
                        f"decision-list\t{derive_sha(rows)}\n").encode("utf-8"))
    print(FREEZE.read_text(encoding="utf-8"), end="")
    return 0


def check_freeze():
    if not FREEZE.is_file():
        raise SystemExit(f"t73: {FREEZE.name} is absent; run `freeze` before grading")
    want = dict(ln.split("\t") for ln in FREEZE.read_text(encoding="utf-8").splitlines()
                if ln and not ln.startswith("#"))
    rows, _ = read_decisions()
    have = {"hidden-suite": derive_sha(SUITE.read_bytes()), "decision-list": derive_sha(rows)}
    for name, sha in have.items():
        if want.get(name) != sha:
            raise SystemExit(f"t73: the {name} hash moved since `freeze` ({want.get(name)} -> {sha}); "
                             "refusing to grade against a suite or list that changed")


def run_suite(tool, scratch):
    """`{test name: passed?}` for one tool, read off pytest's junit XML."""
    xml = scratch / "junit.xml"
    env = dict(os.environ, TRIAL_TOOL=str(tool), PYTHONDONTWRITEBYTECODE="1")
    subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", str(SUITE),
                    f"--junitxml={xml}", f"--basetemp={scratch / 'bt'}"], env=env,
                   capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=900)
    if not xml.is_file():
        raise SystemExit(f"t73: pytest wrote no junit XML for {tool}")
    out = {}
    for tc in ET.parse(xml).getroot().iter("testcase"):
        name = tc.get("name", "")
        if not (name.startswith("test_intent_") or name.startswith("test_contract_")):
            raise SystemExit(f"t73: test {name!r} carries neither tag")
        out[name] = not any(ch.tag in ("failure", "error", "skipped") for ch in tc)
    if not out:
        raise SystemExit("t73: DEAD PROBE: the hidden suite collected no test")
    return out


def measure_tags(results):
    counts = {}
    for name, ok in results.items():
        tag = "intent" if name.startswith("test_intent_") else "contract"
        p, t = counts.get(tag, (0, 0))
        counts[tag] = (p + ok, t + 1)
    return counts


def cmd_stub(a):
    root = resolve_root(a.root)
    stub = root / "stub" / "declared.py"
    stub.parent.mkdir(parents=True, exist_ok=True)
    stub.write_text(STUB_SOURCE, encoding="utf-8")
    with tempfile.TemporaryDirectory(dir=str(root)) as tmp:
        results = run_suite(stub, pathlib.Path(tmp))
    passed = sorted(n for n, ok in results.items() if ok)
    print(f"stub: {len(results)} tests, {len(passed)} passed the exit-0 stub")
    for n in passed:
        print(f"stub: PASSES THE STUB {n}")
    return 1 if passed else 0


def cmd_hidden(a):
    check_freeze()
    root = resolve_root(a.root)
    cells = a.cells.split(",") if a.cells else CELLS
    new = {}
    for cell in cells:
        if cell not in CELLS:
            raise SystemExit(f"t73: {cell!r} is not a cell; the cells are {' '.join(CELLS)}")
        tool = root / "cells" / cell / "declared.py"
        if tool.is_file():
            with tempfile.TemporaryDirectory(dir=str(root)) as tmp:
                counts = measure_tags(run_suite(tool, pathlib.Path(tmp)))
        else:
            n = len(re.findall(r"^def test_intent_", SUITE.read_text(encoding="utf-8"), re.M))
            m = len(re.findall(r"^def test_contract_", SUITE.read_text(encoding="utf-8"), re.M))
            counts = {"intent": (0, n), "contract": (0, m)}
            print(f"cell {cell}: NO TOOL at {tool}; recorded as 0")
        for tag in ("intent", "contract"):
            p, t = counts.get(tag, (0, 0))
            new[("hidden", cell, tag + "_pass")] = str(p)
            new[("hidden", cell, tag + "_total")] = str(t)
            print(f"cell {cell}: {tag} {p}/{t} = {float(Fraction(p, t or 1)):.3f}")
    set_rows(RESULTS, new)
    return 0


# ---------------------------------------------------------------------------------- tokens

def read_first_text(rec):
    msg = rec.get("message") if isinstance(rec.get("message"), dict) else {}
    content = msg.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
    return ""


def cmd_tokens(a):
    sys.path.insert(0, str(REPO / "tools" / "runlog"))
    import extract  # the transcript seam the spec reuses: resolve_session_tree + read_records

    projects = pathlib.Path(a.projects_root) if a.projects_root else extract.resolve_projects_root()
    tree = extract.resolve_session_tree(a.session, projects)
    if tree.main is None:
        raise SystemExit(f"t73: no transcript for session {a.session} under {projects}")
    tag_of, usage = {}, {}
    for src, file_no, _, rec in extract.read_records(tree):
        if src != "workflow":
            continue
        if file_no not in tag_of and rec.get("type") == "user":
            m = TAG_RE.match(read_first_text(rec).lstrip())
            tag_of[file_no] = m.group(1) if m else None
        msg = rec.get("message") if isinstance(rec.get("message"), dict) else {}
        use = msg.get("usage")
        if rec.get("type") == "assistant" and isinstance(use, dict):
            rid = rec.get("requestId") or msg.get("id") or id(rec)
            k = (file_no, rid)
            usage[k] = max(usage.get(k, 0), int(use.get("output_tokens") or 0))
    files = sorted({f for f, _ in usage} | set(tag_of))
    untagged = [f for f in files if not tag_of.get(f)]
    per_tag = {}
    for (f, _), n in usage.items():
        if tag_of.get(f):
            per_tag[tag_of[f]] = per_tag.get(tag_of[f], 0) + n
    if not files:
        raise SystemExit("t73: DEAD PROBE: the session tree holds no workflow agent")
    set_rows(RESULTS, {("tokens", t, "out"): str(n) for t, n in per_tag.items()})
    per_cell = {}
    for t, n in per_tag.items():
        m = CELL_OF_TAG.match(t)
        if m:
            per_cell[m.group(1)] = per_cell.get(m.group(1), 0) + n
    print(f"tokens: {len(files)} workflow agents, {len(untagged)} untagged")
    for cell in CELLS:
        print(f"tokens: {cell} out={per_cell.get(cell, 'MISSING')}")
    missing = [c for c in CELLS if c not in per_cell]
    return 1 if untagged or missing else 0


# ---------------------------------------------------------------------------------- aggregate

def read_marks(path, allowed):
    out = {}
    for n, ln in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not ln.strip() or ln.startswith("#"):
            continue
        parts = [p.strip() for p in ln.split("\t")]
        if len(parts) < 3 or parts[2] not in allowed:
            raise SystemExit(f"t73: {path}:{n} is not `<subject>\\t<D>\\t<{'|'.join(allowed)}>`")
        out[(parts[0], parts[1])] = parts[2]
    return out


def write_scored_rows(root):
    """Unblind the scorers' marks and record them with the judges' marks as committed rows."""
    key = dict(ln.split("\t") for ln in (root / "blind-key.tsv").read_text(encoding="utf-8").splitlines()
               if ln)
    new = {}
    for f in sorted((root / "scores").glob("*.tsv")):
        for (code, d), mark in read_marks(f, MARKS).items():
            if code not in key:
                raise SystemExit(f"t73: {f.name} scores {code!r}, which is no code name")
            new[("score", key[code], d)] = mark
    for f in sorted((root / "judges").glob("*.tsv")):
        for (cell, d), mark in read_marks(f, DOC_MARKS).items():
            new[("doc", cell, d)] = mark
    if not new:
        raise SystemExit(f"t73: DEAD PROBE: no score or judge row under {root}")
    set_rows(RESULTS, new)
    print(f"collect: {len(new)} rows into {RESULTS.name}")


def derive_permutation_p(p_vals, s_vals):
    """Exact two-sided p over every way to label 5 of the 10 values S: |mean S - mean P| as extreme."""
    pool = list(p_vals) + list(s_vals)
    k = len(s_vals)
    obs = abs(Fraction(sum(s_vals), k) - Fraction(sum(p_vals), len(p_vals)))
    splits = list(itertools.combinations(range(len(pool)), k))
    hits = 0
    for idx in splits:
        s = sum(pool[i] for i in idx)
        rest = sum(pool) - s
        if abs(Fraction(s, k) - Fraction(rest, len(pool) - k)) >= obs:
            hits += 1
    return Fraction(hits, len(splits)), len(splits)


def derive_verdict(diff, p):
    if diff >= Fraction(1, 10) and p <= Fraction(5, 100):
        return "S-BETTER"
    if -diff >= Fraction(1, 10) and p <= Fraction(5, 100):
        return "P-BETTER"
    if abs(diff) < Fraction(1, 10) and p > Fraction(5, 100):
        return "NO-DIFFERENCE"
    return "INCONCLUSIVE"


def render_rate(x):
    return "-" if x is None else f"{float(x):.3f}"


def cmd_aggregate(a):
    if a.collect:
        write_scored_rows(pathlib.Path(a.collect))
    rows = read_rows(pathlib.Path(a.rows) if a.rows else RESULTS)
    _, ids = read_decisions()
    if not any(k[0] == "score" for k in rows):
        print("t73: DEAD PROBE: no score row in the results; nothing to aggregate")
        return 1

    def derive_rate(kind, cell, good):
        marks = [rows.get((kind, cell, d)) for d in ids]
        if not any(marks):
            return None
        return Fraction(sum(m == good for m in marks), len(ids))

    def derive_hidden(cell, tag):
        p, t = rows.get(("hidden", cell, tag + "_pass")), rows.get(("hidden", cell, tag + "_total"))
        return None if p is None or not int(t) else Fraction(int(p), int(t))

    def measure_tokens(cell):
        vals = [int(v) for (k, t, _), v in rows.items() if k == "tokens" and CELL_OF_TAG.match(t)
                and CELL_OF_TAG.match(t).group(1) == cell]
        return sum(vals) if vals else None

    print(f"decisions: {len(ids)} ({ids[0]}..{ids[-1]})")
    print("| cell | arm | intent | contract | decision-met | doc coverage | output tokens |")
    print("|---|---|---|---|---|---|---|")
    for cell in CELLS + ["stub"]:
        arm = "pilot" if cell == "pilot" else ("stub" if cell == "stub" else cell[0])
        print(f"| {cell} | {arm} | {render_rate(derive_hidden(cell, 'intent'))} | "
              f"{render_rate(derive_hidden(cell, 'contract'))} | {render_rate(derive_rate('score', cell, 'met'))} | "
              f"{render_rate(derive_rate('doc', cell, 'decided-compatible'))} | {measure_tokens(cell) or '-'} |")
    unscored = [c for c in ARMS["P"] + ARMS["S"] if derive_rate("score", c, "met") is None]
    for c in unscored:
        print(f"unscored: {c} counts as 0")
    met = {c: derive_rate("score", c, "met") or Fraction(0) for c in ARMS["P"] + ARMS["S"]}
    p_vals = [met[c] for c in ARMS["P"]]
    s_vals = [met[c] for c in ARMS["S"]]
    diff = Fraction(sum(s_vals), 5) - Fraction(sum(p_vals), 5)
    p, n = derive_permutation_p(p_vals, s_vals)
    print(f"mean decision-met: P {render_rate(Fraction(sum(p_vals), 5))} · S {render_rate(Fraction(sum(s_vals), 5))}"
          f" · S-P {float(diff):+.3f}")
    print(f"exact two-sided p over {n} splits: {p.numerator}/{p.denominator} = {float(p):.4f}")
    stub = derive_rate("score", "stub", "met")
    print(f"planted stub decision-met: {render_rate(stub)} (liveness: at most 0.250)")
    tp = [measure_tokens(c) for c in ARMS["P"]]
    ts = [measure_tokens(c) for c in ARMS["S"]]
    if all(tp) and all(ts):
        print(f"output tokens S/P: {sum(ts) / sum(tp):.2f}")
    else:
        print("output tokens S/P: - (a cell has no tokens row)")
    print(f"verdict: {derive_verdict(diff, p)}")
    if stub is None or stub > Fraction(1, 4):
        print("t73: LIVENESS RED: the planted stub is unscored or above 0.250")
        return 1
    return 0


# ---------------------------------------------------------------------------------- selftest

def check_selftest():
    one, zero = Fraction(1), Fraction(0)
    p, n = derive_permutation_p([zero] * 5, [one] * 5)
    assert n == 252 and p == Fraction(2, 252), p
    assert derive_verdict(Fraction(1), p) == "S-BETTER"
    assert derive_verdict(Fraction(-1), p) == "P-BETTER"
    p, _ = derive_permutation_p([one] * 5, [one] * 5)
    assert p == 1 and derive_verdict(Fraction(0), p) == "NO-DIFFERENCE"
    # a 0.2 gap carried by one cell: large mean difference, weak p -> INCONCLUSIVE, never S-BETTER
    p, _ = derive_permutation_p([zero] * 5, [one] + [zero] * 4)
    assert p > Fraction(5, 100) and derive_verdict(Fraction(1, 5), p) == "INCONCLUSIVE"
    # a small difference with a strong p is INCONCLUSIVE too: the rule needs BOTH size and p
    assert derive_verdict(Fraction(1, 20), Fraction(2, 252)) == "INCONCLUSIVE"
    print("selftest: 7 assertions passed")
    return 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1:] == ["--selftest"]:
        return check_selftest()
    ap = argparse.ArgumentParser(prog="t73")
    sub = ap.add_subparsers(dest="verb", required=True)
    for verb in ("cells", "freeze", "stub", "hidden", "tokens", "aggregate"):
        s = sub.add_parser(verb)
        s.add_argument("--root")
    sub.choices["cells"].add_argument("--blind", action="store_true")
    sub.choices["hidden"].add_argument("--cells")
    sub.choices["tokens"].add_argument("--session", required=True)
    sub.choices["tokens"].add_argument("--projects-root")
    sub.choices["aggregate"].add_argument("--collect")
    sub.choices["aggregate"].add_argument("--rows")
    a = ap.parse_args()
    return {"cells": cmd_cells, "freeze": cmd_freeze, "stub": cmd_stub, "hidden": cmd_hidden,
            "tokens": cmd_tokens, "aggregate": cmd_aggregate}[a.verb](a)


if __name__ == "__main__":
    sys.exit(main())
