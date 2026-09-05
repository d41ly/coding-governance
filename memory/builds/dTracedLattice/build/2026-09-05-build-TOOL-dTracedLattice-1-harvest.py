# **Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7
# Committed as evidence for the recall measurement. The root is DERIVED here; the
# scratchpad original hardcoded this session's worktree and would resolve to nothing.
"""Lens 1 harvester: pull every reuse_lookup.py invocation out of memory/builds/*/spec/*.md
SS10 Reuse audit sections, recover what each CLOSED unit actually touched from git, and emit
a scenario set.  stdlib only.  Writes JSON; prints a stderr digest.

    python harvest.py <out.json>
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import subprocess as _sp
ROOT = pathlib.Path(_sp.run(["git", "rev-parse", "--show-toplevel"],
                            capture_output=True, text=True).stdout.strip())
OUT = Path(sys.argv[1])


def git(*a):
    r = subprocess.run(
        ["git", "-C", str(ROOT).replace("\\", "/"), *a],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    return r.stdout


SPEC_ID_RE = re.compile(r"\b((?:PLAY|KICK|TOOL|DEPL)-[A-Za-z]+-\d+)\b")
# the pre-family era's spelling: a CamelCase session slug + seq, NOT already carrying a family
LEGACY_ID_RE = re.compile(
    r"(?<!PLAY-)(?<!KICK-)(?<!TOOL-)(?<!DEPL-)\b([a-z][A-Za-z]*[A-Z][A-Za-z]*-\d+)\b"
)
STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(.+)$", re.M)
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
# the invocation; markdown hard-wraps inside the quoted query are flattened before matching
# The closing delimiter must MATCH the opening one. With a character-class close, a query like
# "decide whether a spec's open questions are resolved" truncates at the apostrophe to
# "decide whether a spec", and the harvested query is then a lie about what was actually run.
INVOKE_RE = re.compile(
    r"reuse_lookup\.py\s+(?:--\S+\s+)*"
    r"(?:(?P<d>[\"'])(?P<q>.{4,400}?)(?P=d)|\u201c(?P<q2>.{4,400}?)\u201d)"
)


def queries_in(flat):
    return [unwrap(m.group("q") or m.group("q2")) for m in INVOKE_RE.finditer(flat)]
RECALL_RE = re.compile(r"Recall terms used[^:\n]*:\s*`?([^`\n][^`]{0,400}?)`?(?:\n\n|\Z)", re.S)
TICK_RE = re.compile(r"`([^`\n]{1,120})`")


def section(text, heading_pat):
    m = re.search(heading_pat, text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    n = re.search(r"^##\s", rest, re.M)
    return rest[:n.start()] if n else rest


def unwrap(s):
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- harvest specs
# `*/spec/*.md` misses three builds that shard their units into `spec/units/`; the flat glob found
# 468 files where the recursive one finds 489, and the 21 it dropped all carry a section 10.
specs = sorted((ROOT / "memory" / "builds").glob("*/spec/**/*.md"))
rows = []
stats = Counter()
for p in specs:
    stats["spec_files"] += 1
    raw = p.read_text(encoding="utf-8", errors="replace")
    sec = section(raw, r"^##\s*10\.\s*Reuse audit\s*$")
    if not sec:
        continue
    stats["with_s10"] += 1
    flat = unwrap(sec)
    invokes = queries_in(flat)
    if not invokes:
        if "reuse_lookup" in flat:
            stats["s10_names_tool_but_no_quoted_query"] += 1
        continue
    stats["with_invocation"] += 1

    h1 = re.search(r"^#\s+(.+)$", raw, re.M)
    sid = None
    if h1:
        m = SPEC_ID_RE.search(h1.group(1))
        if m:
            sid = m.group(1)
    if not sid:
        m = SPEC_ID_RE.search(p.name)
        sid = m.group(1) if m else p.stem

    st = STATUS_RE.search(raw)
    stline = st.group(1).strip() if st else ""
    status = stline.split("\u00b7")[0].strip().split()[0] if stline else "UNKNOWN"

    fd = DATE_RE.search(p.name)
    fdate = fd.group(1) if fd else ""

    rec = RECALL_RE.search(sec)
    recall_terms = unwrap(rec.group(1)) if rec else ""

    # cited seam: the clause immediately after each invocation, to the sentence end
    seams, seam_prose = [], []
    for m in INVOKE_RE.finditer(flat):
        tail = flat[m.end():m.end() + 400]
        # The invocation is usually itself inside a markdown code span, so the byte right after the
        # closing quote is that span's CLOSING backtick. Left in, it pairs with the next OPENING
        # backtick and TICK_RE then harvests the prose BETWEEN seams instead of the seams.
        tail = tail.lstrip("`")
        cut = re.split(r"(?<=[.;])\s+(?=[A-Z`])", tail, maxsplit=1)[0]
        seam_prose.append(unwrap(cut)[:320])
        seams.extend(TICK_RE.findall(cut))
    seams = [s for i, s in enumerate(seams) if s not in seams[:i]]

    rows.append(dict(
        spec_id=sid,
        spec_path=str(p.relative_to(ROOT)).replace("\\", "/"),
        status=status, status_line=stline, date=fdate,
        queries=invokes,
        cited_seams=seams, cited_prose=seam_prose, recall_terms=recall_terms,
    ))

# ---------------------------------------------------------------- git ground truth
CODE_EXT = {".py", ".sh", ".js", ".ts", ".json", ".toml", ".conf", ".md",
            ".txt", ".ps1", ".yml", ".yaml", ""}
DEF_RE = re.compile(
    r"^\+\s*(?:async\s+)?(?:def|class)\s+([A-Za-z_]\w*)"                  # python
    r"|^\+\s*(?:function\s+)?([A-Za-z_][\w]*)\s*\(\s*\)\s*\{"             # sh function
    r"|^\+\s*(?:export\s+)?(?:async\s+)?function\s+([A-Za-z_]\w*)"        # js
    r"|^\+\s*(?:const|let|var)\s+([A-Za-z_]\w*)\s*=\s*(?:async\s*)?\("    # js arrow
    r"|^\+([A-Z][A-Z0-9_]{2,})="                                          # sh/py CONSTANT
)
SWEEP_CAP = 25  # a commit touching more product files than this tells us nothing about ONE unit


# ONE history scan, not one per unit: `git log --all --grep` re-walks the whole DAG each time and
# 145 of those is minutes of process spawn for an answer a single pass already holds.
def index_history():
    """(family-id -> commits, legacy-slug-id -> commits).  `SPEC_ID_RE` is word-bounded, so
    `-1` cannot swallow `-12`.  The legacy index exists because the pre-family-prefix era wrote
    `aBatchedLintel-1` in commit subjects while the spec H1 says `TOOL-aBatchedLintel-1`."""
    raw = git("log", "--all", "--no-merges", "--date=short", "--format=%x1e%H\x1f%ad\x1f%s\x1f%B")
    by_id, by_legacy = {}, {}
    for blob in raw.split("\x1e"):
        if not blob.strip():
            continue
        parts = blob.split("\x1f")
        if len(parts) < 4:
            continue
        sha, date, subject, body = parts[0].strip(), parts[1], parts[2], "\x1f".join(parts[3:])
        msg = subject + "\n" + body
        # a commit closing four units attributes all its files to each of them; record the count so
        # a scorer can drop or down-weight the multi-unit ones instead of silently inheriting them
        named = set(SPEC_ID_RE.findall(msg)) | set(LEGACY_ID_RE.findall(msg))
        c = dict(sha=sha[:8], full=sha, date=date, subject=subject, units_named=len(named))
        for uid in set(SPEC_ID_RE.findall(msg)):
            by_id.setdefault(uid, []).append(c)
        for uid in set(LEGACY_ID_RE.findall(msg)):
            by_legacy.setdefault(uid, []).append(c)
    return by_id, by_legacy


_names_cache = {}


def names_of(sha):
    if sha not in _names_cache:
        _names_cache[sha] = [n for n in git("show", "--name-only", "--format=", sha).splitlines()
                             if n.strip()]
    return _names_cache[sha]


_sym_cache = {}


def symbols_of(sha, prod):
    key = (sha, tuple(prod))
    if key not in _sym_cache:
        out = Counter()
        diff = git("show", "--format=", "--unified=0", sha, "--", *prod)
        for line in diff.splitlines():
            m = DEF_RE.match(line)
            if m:
                nm = next(g for g in m.groups() if g)
                if len(nm) > 2:
                    out[nm] += 1
        _sym_cache[key] = out
    return _sym_cache[key]


_churn_cache = {}


def churn_of(sha, prod):
    key = (sha, tuple(prod))
    if key not in _churn_cache:
        out = Counter()
        for line in git("show", "--numstat", "--format=", sha, "--", *prod).splitlines():
            f = line.split("\t")
            if len(f) == 3 and f[0].isdigit() and f[1].isdigit():
                out[f[2]] = int(f[0]) + int(f[1])
        _churn_cache[key] = out
    return _churn_cache[key]


def files_and_symbols(commits):
    files, syms, churn, kept, dropped = Counter(), Counter(), Counter(), [], []
    sole_files = Counter()
    for c in commits:
        meta = {k: c[k] for k in ("sha", "subject", "date", "units_named")}
        names = names_of(c["full"])
        prod = [n for n in names if not n.startswith("memory/") and Path(n).suffix in CODE_EXT]
        if not prod:
            dropped.append(meta | {"drop": "records-only commit"})
            continue
        if len(prod) > SWEEP_CAP:
            dropped.append(meta | {"drop": f"sweep: {len(prod)} product files > {SWEEP_CAP}"})
            continue
        kept.append(meta | {"product_files": len(prod)})
        for n in prod:
            files[n] += 1
            if c["units_named"] == 1:
                sole_files[n] += 1
        syms.update(symbols_of(c["full"], prod))
        churn.update(churn_of(c["full"], prod))
    return files, syms, churn, sole_files, kept, dropped


HISTORY, HISTORY_LEGACY = index_history()

# A bare `aFoo-3` in an old commit is only safely attributable to `ARCH-tFixture-3` when no OTHER
# family in the whole spec corpus also owns `aFoo-3`. Otherwise the legacy hit is dropped.
_by_tail = Counter()
for _p in specs:
    _h1 = re.search(r"^#\s+(.+)$", _p.read_text(encoding="utf-8", errors="replace"), re.M)
    if _h1:
        _m = SPEC_ID_RE.search(_h1.group(1))
        if _m:
            _by_tail[_m.group(1).split("-", 1)[1]] += 1


def commits_for(unit_id):
    tail = unit_id.split("-", 1)[1]
    out = list(HISTORY.get(unit_id, []))
    legacy_used = 0
    if _by_tail[tail] == 1:
        seen = {c["full"] for c in out}
        for c in HISTORY_LEGACY.get(tail, []):
            if c["full"] not in seen:
                out.append(c)
                legacy_used += 1
    return out, legacy_used


for r in rows:
    r["_kept"] = []
    r["_dropped"] = []
    r["_files"] = Counter()
    r["_syms"] = Counter()
    r["_churn"] = Counter()
    r["_sole"] = Counter()
    if r["status"] != "CLOSED":
        r["class"] = "stability-only"
        r["_why"] = f"spec status {r['status']}: the unit is not closed, so the only recorded answer is the tool's own"
        continue
    cs, legacy_used = commits_for(r["spec_id"])
    files, syms, churn, sole, kept, dropped = files_and_symbols(cs)
    r["_files"], r["_syms"], r["_kept"], r["_dropped"] = files, syms, kept, dropped
    r["_churn"], r["_sole"] = churn, sole
    r["_legacy"] = legacy_used
    if not kept:
        r["class"] = "stability-only"
        r["_why"] = ("no commit message names this id"
                     if not cs else
                     f"{len(cs)} commit(s) name the id but none survives the product-file filter")
    else:
        r["class"] = "graded"
        r["_why"] = f"{len(kept)} attributing product commit(s), {len(files)} distinct product file(s)"

# ---------------------------------------------------------------- emit
# The map kit was adopted mid-corpus and its dossier set grew all through the graded window, so a
# replay at HEAD hands the tool a corpus that did not exist when the question was asked -- including
# dossiers written ABOUT the unit being graded. The spec's own status line records the base it was
# cut from; carry it so a scorer can replay at the right era instead of leaking the answer.
BASE_RE = re.compile(r"\bbase ([0-9a-f]{7,40})\b")
_base_ok = {}


def base_of(status_line):
    m = BASE_RE.search(status_line or "")
    if not m:
        return "", False
    sha = m.group(1)
    if sha not in _base_ok:
        r = subprocess.run(
            ["git", "-C", str(ROOT).replace("\\", "/"), "cat-file", "-e", sha + "^{commit}"],
            capture_output=True,
        )
        _base_ok[sha] = r.returncode == 0
    return sha, _base_ok[sha]


_corpus_at = {}


def map_corpus_at(sha):
    """How much map corpus the tool actually HAD when this question was asked. A scenario whose
    base carries two dossiers and no symbols.json cannot be answered by a tool that reads them, and
    a scorer that does not know this reads the tool's silence as a miss."""
    if not sha:
        return {"dossiers": None, "symbols_json": None}
    if sha not in _corpus_at:
        listing = git("ls-tree", "-r", "--name-only", sha, "--", "memory/map/").splitlines()
        _corpus_at[sha] = {
            "dossiers": sum(1 for x in listing
                            if x.startswith("memory/map/features/") and x.endswith(".md")),
            "symbols_json": "memory/map/generated/symbols.json" in listing,
        }
    return _corpus_at[sha]


_query_owners = {}
for _r in rows:
    for _q in _r["queries"]:
        _query_owners.setdefault(_q, []).append(_r["spec_id"])

scen = []
for r in rows:
    files = sorted(r["_files"], key=lambda f: (-r["_churn"][f], f))
    syms = sorted(r["_syms"], key=lambda s: (-r["_syms"][s], s))
    for q in r["queries"]:
        scen.append({
            "query": q,
            "expected_files": files if r["class"] == "graded" else [],
            "expected_files_sole_attribution": (
                sorted(r["_sole"], key=lambda f: (-r["_churn"][f], f))
                if r["class"] == "graded" else []),
            "expected_symbols": syms if r["class"] == "graded" else [],
            "spec_id": r["spec_id"],
            "status": r["status"],
            "date": r["date"],
            "class": r["class"],
            "base_sha": base_of(r["status_line"])[0],
            "base_sha_resolves_here": base_of(r["status_line"])[1],
            "map_corpus_at_base": (map_corpus_at(base_of(r["status_line"])[0])
                                   if base_of(r["status_line"])[1] else
                                   {"dossiers": None, "symbols_json": None}),
            "provenance": {
                "spec_path": r["spec_path"],
                "status_line": r["status_line"],
                "query_also_used_by": [x for x in _query_owners[q] if x != r["spec_id"]],
                "ground_truth": (
                    "git log --all --no-merges, commit message names the unit id (word-bounded); "
                    "product files only (memory/** excluded); commits touching >25 product files "
                    "dropped as sweeps. expected_files is ordered by churn, most-changed first."
                    if r["class"] == "graded" else
                    "none - only what the tool itself returned at authoring time"
                ),
                "why_class": r["_why"],
                "legacy_spelled_commits_folded_in": r.get("_legacy", 0),
                "attributing_commits": r["_kept"],
                "rejected_commits": r["_dropped"],
                "file_churn_lines": dict(r["_churn"]),
                "file_hit_counts": dict(r["_files"]),
                "symbol_hit_counts": dict(r["_syms"]),
                "cited_seams": r["cited_seams"],
                "cited_prose": r["cited_prose"],
                "recall_terms": r["recall_terms"],
            },
        })

graded = [s for s in scen if s["class"] == "graded"]
stab = [s for s in scen if s["class"] == "stability-only"]

# How often each ground-truth file shows up across ALL graded scenarios. A file present in a third
# of them is predicted by guessing, not by ranking; the scorer down-weights or excludes with this
# rather than with a hand-typed noise list.
corpus_freq = Counter()
for s in graded:
    for f in s["expected_files"]:
        corpus_freq[f] += 1

doc = {
    "_README": [
        "Lens 1 scenario set. Every reuse_lookup.py invocation recorded in a spec's `## 10. Reuse audit`,",
        "paired with what that unit ACTUALLY touched wherever that is recoverable from git.",
        "",
        "class=graded -- spec status is CLOSED and at least one non-merge commit names the unit id and",
        "  changes a non-records file. expected_files / expected_symbols are DERIVED FROM GIT and never",
        "  from the spec's own prose, so a scorer measures whether the tool's ranking PREDICTED the real",
        "  change. This is the only class that can measure correctness.",
        "class=stability-only -- the unit is not CLOSED, or nothing attributable landed. expected_* are",
        "  EMPTY on purpose; provenance.cited_seams holds what the tool said at authoring time. Scoring",
        "  these measures DRIFT against the tool's own past answers, NOT correctness. Never aggregate the",
        "  two classes into one precision or recall number.",
        "",
        "expected_symbols is the WEAKER of the two signals: it is scraped from added def/class/name()/",
        "function/CONST lines in the attributing diffs, so it holds only symbols the unit CREATED, never",
        "ones it merely called or edited in place. expected_files is the load-bearing field.",
        "",
        "Regenerate: python harvest.py <out.json>",
    ],
    "generated_from": {
        "repo": str(ROOT).replace("\\", "/"),
        "head": git("rev-parse", "HEAD").strip()[:12],
        "spec_files_scanned": stats["spec_files"],
        "specs_with_section_10": stats["with_s10"],
        "specs_with_parsed_invocation": stats["with_invocation"],
        "specs_naming_tool_but_no_quoted_query": stats["s10_names_tool_but_no_quoted_query"],
        "scenarios_graded": len(graded),
        "scenarios_stability_only": len(stab),
        "distinct_queries_all": len({s["query"] for s in scen}),
        "distinct_queries_graded": len({s["query"] for s in graded}),
        "graded_specs": len({s["spec_id"] for s in graded}),
        "stability_specs": len({s["spec_id"] for s in stab}),
        "distinct_ground_truth_files": len(corpus_freq),
        "graded_with_resolvable_base_sha": sum(1 for s in graded if s["base_sha_resolves_here"]),
        "graded_with_empty_sole_attribution": sum(
            1 for s in graded if not s["expected_files_sole_attribution"]),
        "graded_date_range": [min(s["date"] for s in graded), max(s["date"] for s in graded)]
        if graded else [],
    },
    "scoring_recipe": [
        "REPLAY AT base_sha, NOT AT HEAD. The codebase-map kit was adopted 2026-08-09 (f9cf666c) and",
        "its dossier set grew from 2 to 20 across the window these scenarios cover. Replaying at HEAD",
        "hands the tool a corpus that did not exist when the question was asked, including dossiers",
        "written about the very unit being graded -- the tool then gets credit for finding a seam the",
        "unit itself created. Every graded row carries base_sha from its spec's own status line;",
        "base_sha_resolves_here says whether this clone has it.",
        "",
        "reuse_lookup.py prints one candidate per `- ` line in two shapes:",
        "  `- <name>  [<kind> | <file> | fan-in <n>]  (...)`   -- a SYMBOL: the file is right there.",
        "  `- <name>  [<feature>]  (...)`                      -- an INVENTORY key or an AFFORDANCE",
        "     SEAM, tagged with the dossier feature that owns it, NOT a file.",
        "To score a feature-tagged candidate at file granularity, resolve the feature to its files:",
        "memory/map/features/<feature>.md carries a fenced toml block with [paths].globs. Expand those",
        "globs against the tree and treat the candidate as hitting any of them. Derive that mapping at",
        "scoring time; do not bake a copy of it into a fixture, because the dossiers move.",
        "",
        "recall@K  = |rank[:K] resolved-files INTERSECT expected_files| / |expected_files|",
        "precision@K = same numerator / K",
        "Report both AND report them again against expected_files_sole_attribution, which drops every",
        "file whose only evidence is a commit that closed several units at once.",
        "Down-weight with corpus_file_frequency: a file in a third of the scenarios is predicted by",
        "guessing. A ranking that only ever returns those scores well and has learned nothing.",
        "",
        "stability_only rows carry NO expected_*. Score them by re-running the query and diffing the",
        "result against provenance.cited_seams: agreement is stability, disagreement is drift, and",
        "NEITHER is correctness.",
    ],
    "corpus_file_frequency": dict(corpus_freq.most_common()),
    "graded": graded,
    "stability_only": stab,
}
OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(doc["generated_from"], indent=2), file=sys.stderr)
