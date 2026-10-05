#!/usr/bin/env python3
"""Grade the committed question set against the declared recall floor, and exit non-zero below it.

    python check-recall.py [--data-dir DIR] [--repo ROOT] [--audit-fixture]

`bench.py` computes every metric this needs and ALWAYS returns 0 -- `main()` ends `return 0`, its
flag set is closed, and `verbatim.json` pins it byte-for-byte. This program is the exit code it
cannot have. It edits nothing in that file: it IMPORTS the scoring functions.

WHY NOT `bench.py --json`: that report is aggregate-only, so the per-id predicate below is not
computable from it at all -- `expected_by_target` DROPS an unresolvable target before `ceiling` is
counted, and no target-level data survives into the JSON. It also rounds to four decimals, which
turns a 0.9091 into 0.9090. One in-process path removes both problems.

THREE PRECONDITIONS stop the run; TWO PREDICATES both evaluate and both report. The split is
load-bearing: the two degradations that prove the floor and the per-id check are independent BOTH
red at per-id, so a short-circuiting program could never show the floor verdict they turn on.

  precondition 1  the fixture             absent / unparseable / no queries -> red, stop
  precondition 2  the pin                 absent / malformed / out-of-vocabulary -> red, stop
  precondition 3  the graded set          missing from the data dir, or empty -> red, stop
  predicate 4     per-id resolution       every expected id resolves, or red naming it
  predicate 5     the floor               r@k / ceiling vs the pin, or `not evaluated`

`not evaluated` is an explicit rule, not a side effect of stopping early: with a `ceiling` of 0
there is nothing to divide, and printing that beats a 0/0 or a silent skip.

TWO PIN HEADS. `<set>:<substrate>:<metric>@<k>` ranks the bare question over one extracted set
through `bench.rank_with` -- a configuration no session is served. `served:<metric>@<k>` ranks
through the CLI's own `query.query_expr` and `query.run_fusion` over sets `query.build_cache`
builds, so a change to the expression, the rollup or the fusion moves the floor. Under it every
question owes two term lists, and a graded ROW is one (question, slice) pair: `h`, `R` and the
ceiling count rows, and each slice's `h` and `R` print so a saturated slice is visible.

WHAT A `served` RUN STILL DOES NOT CHECK. Untracked files: the CLI indexes untracked-not-ignored
notes and this builds over tracked files only. The `--budget` byte cut `emit` applies to the fused
list: this grades the ranked list, not the emitted text. And the `k`: the CLI's default is 20,
the pin's is whatever it names, so a pin at `@5` grades a shallower read than a default query.

PRECONDITION 3 REPLACED A CHECK THAT COULD NOT FAIL. The spec's rev-3 had it as a predicate asking
whether the pinned `<metric>@<k>` appeared in the report. Measured while building: `score()` emits
`r@k` and `f@k` for whatever `k` it is handed, and the pin grammar admits only those two metrics, so
the branch was green for every pin it could ever see -- `fixture-passes-by-finding-nothing` shipped
inside the gate that exists to close it. The reachable state is an absent or empty document set: a
`--data-dir` built without one. `spine` used to be the standing example, because `DURABLE` required
a directory segment this repo's flat memory root does not have and the set extracted to zero docs
here; the aTunedCompass build fixed the pattern, so that example is retired and the branch is now
reached by a genuinely absent set rather than by a live bug. (The spec id is not spelled, for the
reason the paragraph below gives.)

Contract: the build folder at memory/builds/aWalkedCorpus/ (the spec id is deliberately not spelled
here -- `non_terminal_specs_cited_by_product_source` runs at tolerance 0 and `tools/` is a product
glob, so a product file naming a spec that has not closed reds the bar).
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from collections import Counter

# ABOVE the sibling imports, not below: CPython writes a module's bytecode next to its SOURCE, which
# is inside the adopter's worktree. `extract.py` carries the same line for the same reason -- it is
# the whole of the kit's "a query writes nothing in your tree" property on this file.
sys.dont_write_bytecode = True

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import bench  # noqa: E402
import extract  # noqa: E402
import query  # noqa: E402
import recall_conf  # noqa: E402

KIT = pathlib.Path(__file__).resolve().parent
FIXTURE_NAME = "recall-fixture.json"

# The vocabularies the pin may name. Constraining these is what makes a one-character typo red at
# the PIN branch naming the key, rather than raising FileNotFoundError inside `bench.load` where no
# branch names anything.
SETS = ("spine", "records", "chunks")
SUBS = tuple(bench.LEXICAL) + tuple(bench.ROLLUP) + tuple(bench.DENSE) + tuple(bench.HYBRID)
# `r` (recall@k) and `f` (full@k) are the QUALITY metrics `score()` emits per k. `b` is bytes read --
# a cost axis, where a `>=` floor is satisfied by any corpus and would be a decoration. `MRR` has no
# `@k` and so cannot be spelled in this grammar at all.
METRICS = ("r", "f")

PIN_KEY = "RECALL_FLOOR"
PIN_RE = re.compile(
    r"^(?P<set>[a-z0-9]+):(?P<sub>[a-z0-9]+):(?P<metric>[a-z]+)@(?P<k>\d+)>=(?P<value>\d*\.?\d+)$"
)
# The `served` head: no set and no substrate, because the CLI's fused ranking is neither one set nor
# one `bench` substrate. Under it the floor ranks through `query.query_expr` and `query.run_fusion`.
SERVED_RE = re.compile(r"^served:(?P<metric>[a-z]+)@(?P<k>\d+)>=(?P<value>\d*\.?\d+)$")
# The two term lists a question carries under a `served` pin, each one graded ROW: `terms` is the
# rewrite a session writes after reading the corpus, `naive_terms` one written from the question
# alone. The naive slice is where the headroom lives; strong terms saturate.
SLICES = ("terms", "naive_terms")

# The anti-tautology threshold. A question written by reading what the index returns scores ~1.0
# here; the committed fixture measures min 0.125, mean 0.362, max 0.500, with none at or above 0.60.
# So 0.60 sits one step above the observed maximum -- tight enough that copied text cannot pass,
# loose enough that today's set is not sitting on the boundary. A MODULE constant rather than a conf
# key because nothing but this gate reads it, where `RECALL_FLOOR` is a number a person edits
# between releases.
OVERLAP_MAX = 0.60


class CheckRefused(Exception):
    """A precondition failed. The message is the whole report -- it names what was missing."""


def read_fixture(path: pathlib.Path, slices: tuple = ()) -> list[dict]:
    """Precondition 1. An empty question list is refused HERE rather than downstream.

    A fixture with no questions makes the per-id predicate vacuously green and leaves `substrates`
    empty, so the failure would surface as a missing cell three branches later and name the wrong
    thing. That is the `fixture-passes-by-finding-nothing` class arriving through its own gate.

    `slices` names the term lists every question owes -- `SLICES` under a `served` pin, none under a
    single-pair one. Each list's length must sit inside `query.TERM_BAND`, the band the CLI itself
    holds a session to, so a list the CLI would refuse is never graded here.
    """
    if not path.is_file():
        raise CheckRefused(f"fixture absent: {path.as_posix()}")
    try:
        blob = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise CheckRefused(f"fixture unreadable: {path.as_posix()} ({exc})") from exc
    queries = blob.get("queries") if isinstance(blob, dict) else blob
    if not isinstance(queries, list) or not queries:
        raise CheckRefused(f"fixture carries no queries: {path.as_posix()}")
    # The ELEMENTS, not just the container. Validating only the list let a hand edit reach
    # `bench.rank_with(..., q["query"])` and die on a KeyError three branches later, reported as
    # exit 1 -- this program's "a predicate failed" code -- so a malformed fixture was
    # indistinguishable from a genuine recall regression on the bar.
    for i, q in enumerate(queries, 1):
        if not isinstance(q, dict) or not isinstance(q.get("query"), str) or not q["query"].strip():
            raise CheckRefused(f"fixture question {i} carries no `query`: {path.as_posix()}")
        ids = q.get("expected_ids", [])
        if not isinstance(ids, list) or any(not isinstance(x, str) for x in ids):
            raise CheckRefused(
                f"fixture question {i} has a non-string `expected_ids`: {path.as_posix()}")
        lo, hi = query.TERM_BAND
        for name in slices:
            words = q.get(name)
            if not isinstance(words, list) or any(not isinstance(w, str) or not w.strip()
                                                  for w in words):
                raise CheckRefused(
                    f"fixture question {i} carries no `{name}` word list: {q['query']!r}")
            if not lo <= len(words) <= hi:
                raise CheckRefused(
                    f"fixture question {i} has {len(words)} `{name}`, outside TERM_BAND "
                    f"{lo}-{hi}: {q['query']!r}")
    return queries


def parse_pin(raw: str | None) -> dict:
    """Precondition 2. `served:<metric>@<k>>=<float>` or `<set>:<sub>:<metric>@<k>>=<float>`.

    Both heads parse, so a conf still carrying the single-pair shape grades as it always did.
    """
    if raw is None:
        raise CheckRefused(f"{PIN_KEY} is not declared in {recall_conf.CONF_NAME}")
    raw = raw.strip().strip('"').strip("'")
    if not raw:
        raise CheckRefused(f"{PIN_KEY} is empty in {recall_conf.CONF_NAME} -- there is no default")
    m = SERVED_RE.match(raw) or PIN_RE.match(raw)
    if not m:
        raise CheckRefused(
            f"{PIN_KEY} does not parse: {raw!r}; want served:<metric>@<k>>=<float> "
            f"or <set>:<substrate>:<metric>@<k>>=<float>"
        )
    served = m.re is SERVED_RE
    if not served:
        if m["set"] not in SETS:
            raise CheckRefused(f"{PIN_KEY} names set {m['set']!r}; known: {' '.join(SETS)}")
        if m["sub"] not in SUBS:
            raise CheckRefused(f"{PIN_KEY} names substrate {m['sub']!r}; known: {' '.join(SUBS)}")
    if m["metric"] not in METRICS:
        raise CheckRefused(f"{PIN_KEY} names metric {m['metric']!r}; known: {' '.join(METRICS)}")
    head = "served" if served else f"{m['set']}:{m['sub']}"
    return {
        "served": served, "set": "served" if served else m["set"],
        "sub": None if served else m["sub"], "metric": m["metric"],
        "k": int(m["k"]), "value": float(m["value"]),
        "cell": f"{head}:{m['metric']}@{m['k']}", "raw": raw,
    }


def build_data_dir(root: pathlib.Path) -> pathlib.Path:
    """Extract the repo's corpus into a throwaway dir at the size the CLI actually serves.

    `query.CHUNK_MAX` is IMPORTED, not restated: `extract.CHUNK_MAX` is 2400 and the live index is
    built at 600, so a graded corpus built at the extractor's default is not the corpus any session
    is served.
    """
    out = pathlib.Path(tempfile.mkdtemp(prefix="check-recall-"))
    proc = subprocess.run(
        [sys.executable, str(KIT / "extract.py"), str(root), str(out),
         "--chunk-max", str(query.CHUNK_MAX)],
        capture_output=True, text=True, cwd=str(root),
    )
    if proc.returncode != 0:
        shutil.rmtree(out, ignore_errors=True)
        # The LAST stderr line, not the whole stream. Embedding a subprocess traceback inside a
        # refusal makes the refusal read like a crash, which is the exact confusion this branch
        # exists to remove; the full trace is one `python extract.py <root> <dir>` away and the
        # message says so.
        tail = next((ln for ln in reversed(proc.stderr.strip().splitlines()) if ln.strip()), "")
        raise CheckRefused(
            f"extract.py failed ({proc.returncode}): {tail.strip()} "
            f"-- rerun `python {(KIT / 'extract.py').as_posix()} {root.as_posix()} <dir>` for the trace"
        )
    return out


def measure_run(data: pathlib.Path, queries: list[dict], pin: dict) -> dict:
    """One in-process pass: per-question targets, per-question hit, the cell, and the ceiling."""
    try:
        docs = bench.load(data, pin["set"])
        anchors = json.loads((data / "anchors.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise CheckRefused(f"graded set {pin['set']!r} unreadable under {data.as_posix()}: {exc}") from exc
    if not docs:
        raise CheckRefused(
            f"graded set {pin['set']!r} is EMPTY under {data.as_posix()} -- nothing to grade, and a "
            f"floor over an empty set is satisfied by any corpus"
        )
    dfreq: Counter = Counter()
    for r in docs:
        dfreq.update(set(bench.terms(r["text"])[:600]))
    db = bench.build_index(docs)
    ks = [pin["k"]]
    per, unresolved = [], []
    for q in queries:
        targets = bench.expected_by_target(docs, q, anchors)
        declared = [i.strip() for i in q.get("expected_ids", []) if i.strip()]
        missing = [i for i in declared if i not in targets]
        unresolved.extend(missing)
        ranked = bench.rank_with(pin["sub"], docs, db, dfreq, q["query"], pin["k"])
        row = bench.score(docs, ranked or [], targets, ks)
        per.append({"q": q, "targets": targets, "hit": row[f"{pin['metric']}@{pin['k']}"] == 1.0,
                    "resolves": bool(targets)})
    n = len(queries)
    resolved = sum(1 for p in per if p["resolves"])
    hits = sum(1 for p in per if p["hit"])
    return {
        "docs": docs, "per": per, "n": n,
        "unresolved": unresolved, "R": resolved, "h": hits,
        "ceiling": resolved / n, "cell_value": hits / n,
    }


def build_served_dir(root: pathlib.Path) -> pathlib.Path:
    """Build the CLI's own two sqlite sets in a throwaway dir, with the CLI's own builder.

    `query.build_cache` over `extract.corpus_inputs` of the root -- tracked files only, where the
    CLI also takes untracked ones. Nothing about extraction or indexing is restated here.
    """
    out = pathlib.Path(tempfile.mkdtemp(prefix="check-recall-served-"))
    try:
        files, declared = extract.corpus_inputs(root)
        query.build_cache(root, out, files, declared)
    except (OSError, ValueError, sqlite3.Error, subprocess.SubprocessError, SystemExit) as exc:
        shutil.rmtree(out, ignore_errors=True)
        raise CheckRefused(f"building the served sets under {root.as_posix()} failed: {exc}") from exc
    return out


def measure_served(dirp: pathlib.Path, queries: list[dict], pin: dict) -> dict:
    """One graded ROW per (question, slice), ranked by the CLI's own `query_expr` and `run_fusion`.

    A fused hit satisfies an expected id by `bench.expected_by_target`'s two rules. The anchor map
    is the served `records.db` `meta` table, and a hit whose `id` column is EMPTY -- how `_write_set`
    stores a chunk with no parent record -- loses that key before it is judged, so the anchor rule
    judges it rather than an empty-string comparison.
    """
    try:
        db = sqlite3.connect(f"file:{(dirp / 'records.db').as_posix()}?mode=ro", uri=True)
        try:
            rows = db.execute("SELECT m.id, m.path, d.body FROM d JOIN meta m ON m.rowid = d.rowid "
                              "WHERE m.id != ''").fetchall()
        finally:
            db.close()
    except sqlite3.Error as exc:
        raise CheckRefused(f"served set unreadable under {dirp.as_posix()}: {exc}") from exc
    if not rows:
        raise CheckRefused(
            f"served set 'records' is EMPTY under {dirp.as_posix()} -- nothing to grade, and a "
            f"floor over an empty set is satisfied by any corpus"
        )
    docs = [{"id": i, "path": p, "text": t} for i, p, t in rows]
    anchors: dict[str, list[str]] = {}
    for d in docs:
        anchors.setdefault(d["id"], []).append(d["path"])
    key = f"{pin['metric']}@{pin['k']}"
    per, unresolved = [], []
    slices = {s: {"h": 0, "R": 0} for s in SLICES}
    for q in queries:
        # Predicate 4 and the overlap audit read the RECORD-level resolution, once per question.
        targets = bench.expected_by_target(docs, q, anchors)
        declared = [i.strip() for i in q.get("expected_ids", []) if i.strip()]
        unresolved.extend(i for i in declared if i not in targets)
        for s in SLICES:
            expr = query.query_expr(q["query"], q[s])
            fused = query.run_fusion(dirp, expr, pin["k"]) if expr else []
            judged = [{k: v for k, v in h.items() if k != "id" or v} for h in fused]
            want = bench.expected_by_target(judged, q, anchors)
            # `and targets`: a row that cannot resolve is outside R, so it may not count toward h.
            hit = bool(targets) and bench.score(
                judged, list(range(len(judged))), want, [pin["k"]])[key] == 1.0
            per.append({"q": q, "slice": s, "targets": targets, "hit": hit,
                        "resolves": bool(targets)})
            slices[s]["R"] += bool(targets)
            slices[s]["h"] += hit
    n = len(per)
    resolved = sum(1 for p in per if p["resolves"])
    hits = sum(1 for p in per if p["hit"])
    return {
        "docs": docs, "per": per, "n": n, "slices": slices,
        "unresolved": unresolved, "R": resolved, "h": hits,
        "ceiling": resolved / n, "cell_value": hits / n,
    }


def measure_overlap(run: dict) -> list[dict]:
    """Per question: how much of its vocabulary it shares with the records that answer it.

    The denominator is the QUESTION's distinct content terms; the target text is the UNION of every
    document the RUN ITSELF resolved for that question. Reusing `measure_run`'s targets is
    load-bearing rather than tidy: an earlier cut re-implemented resolution as a records-only
    `id ->  doc` map, so a question the run could not resolve scored `overlap 0.000` — a PASS, and the
    most independent row in the table. Under a `chunks:` pin, where docs carry no `id` at all, EVERY
    row read 0.000 and the anti-tautology guard was vacuous for a whole in-vocabulary set. That is
    `memory/gotchas/fixture-passes-by-finding-nothing.md` inside the gate written to close it, and
    AGENTS.md's own rule is that a probe which cannot move prints DEAD PROBE, never a reassuring 0.

    A question with no resolved target therefore reports `overlap = None` — NOT MEASURED — which
    `check_audit` reds on and excludes from the summary, rather than averaging in as a perfect row.
    `bench.terms` is imported so the audit and the index agree on what a content word is.
    """
    rows = []
    for p in run["per"]:
        q = p["q"]
        idx = {d for hs in p["targets"].values() for d in hs}
        target_terms: set[str] = set()
        for i in idx:
            target_terms |= set(bench.terms(run["docs"][i]["text"]))
        qt = list(dict.fromkeys(bench.terms(q["query"])))
        overlap = (len([x for x in qt if x in target_terms]) / max(1, len(qt))) if idx else None
        # Under a `served` pin `hits` is keyed by slice; under a single-pair pin a keyed `hits`
        # declares nothing about that cell, so it is not compared.
        declared = q.get("hits")
        if isinstance(declared, dict):
            declared = declared.get(p["slice"]) if p.get("slice") else None
        rows.append({"ids": [i.strip() for i in q.get("expected_ids", []) if i.strip()],
                     "slice": p.get("slice") or "-", "homes": len(idx), "overlap": overlap,
                     "hit": p["hit"], "declared_hit": declared})
    return rows


def check_audit(run: dict, pin: dict) -> list[str]:
    """`--audit-fixture`. Prints what the spec's Inventory table states, and reds on a disagreement.

    Three claims in that table were hand-kept before this existed -- `homes`, `hits` and the `h`/`R`
    the pin is derived from -- in a repo whose own corpus moves. Measuring them here is what turns
    the table into documentation a gate keeps honest.
    """
    rows = measure_overlap(run)
    failures = []
    print(f"{'#':>3}  {'expected id':<28} {'slice':<11} {'homes':>5} {'hits':>5} {'overlap':>8}")
    for i, row in enumerate(rows, 1):
        tag = "yes" if row["hit"] else "no"
        shown = "NOT MEAS" if row["overlap"] is None else f"{row['overlap']:.3f}"
        print(f"{i:>3}  {(row['ids'] or ['-'])[0]:<28} {row['slice']:<11} {row['homes']:>5} "
              f"{tag:>5} {shown:>8}")
        if row["overlap"] is None:
            failures.append(
                f"question {i} resolves no target in {pin['set']!r} -- overlap is NOT MEASURED, "
                f"which is a DEAD PROBE rather than a passing 0.000"
            )
        elif row["overlap"] > OVERLAP_MAX:
            failures.append(
                f"question {i} overlaps its target at {row['overlap']:.3f} > OVERLAP_MAX "
                f"{OVERLAP_MAX:.2f} -- written from the record's own text?"
            )
        if row["declared_hit"] is not None and bool(row["declared_hit"]) != row["hit"]:
            failures.append(
                f"question {i} declares hits={row['declared_hit']} and measures {row['hit']}"
                + (f" in slice {row['slice']}" if row["slice"] != "-" else "")
            )
    for name, s in run.get("slices", {}).items():
        print(f"slice {name}: h={s['h']} R={s['R']}")
    h, R = run["h"], run["R"]
    headroom = (h - 1) / (R - 1) if R > 1 else float("nan")
    # Only MEASURED rows enter the summary. Averaging an unmeasured row in as 0.000 is what made the
    # earlier cut read healthiest exactly when it was measuring nothing.
    live = [r["overlap"] for r in rows if r["overlap"] is not None]
    if live:
        print(f"\noverlap: max {max(live):.3f} mean {sum(live) / len(live):.3f}  "
              f"over {len(live)}/{len(rows)} measured  (OVERLAP_MAX {OVERLAP_MAX:.2f})")
    else:
        print(f"\noverlap: NOT MEASURED on any of {len(rows)} question(s)")
    print(f"derivation: h={h} R={R}  (h-1)/(R-1) = {headroom:.4f}  "
          f"declared {PIN_KEY} {pin['value']:.2f}")
    if headroom == headroom and headroom < pin["value"]:
        failures.append(
            f"{PIN_KEY} {pin['value']:.2f} exceeds the one-retirement worst case {headroom:.4f}; "
            f"the fixture moved h or R and the pin was not re-derived"
        )
    return failures


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True, description=__doc__.splitlines()[0])
    ap.add_argument("--data-dir", default=None,
                    help="grade an already-extracted dir instead of extracting (the arms' seam)")
    ap.add_argument("--repo", default=None, help="repo root; defaults to the kit's own")
    ap.add_argument("--fixture", default=None, help="fixture path; defaults to the kit's own")
    ap.add_argument("--audit-fixture", action="store_true",
                    help="report per-question homes, hits and overlap; red above OVERLAP_MAX")
    args = ap.parse_args()

    root = pathlib.Path(args.repo).resolve() if args.repo else recall_conf.repo_root()
    fixture_path = pathlib.Path(args.fixture) if args.fixture else KIT / FIXTURE_NAME

    scratch = None
    try:
        # The pin is read FIRST because it decides which term lists a question owes.
        pin = parse_pin(recall_conf.load_conf(root).get(PIN_KEY))
        queries = read_fixture(fixture_path, SLICES if pin["served"] else ())
    except CheckRefused as exc:
        print(f"check-recall: REFUSED -- {exc}", file=sys.stderr)
        return 2

    try:
        try:
            if args.data_dir:
                data = pathlib.Path(args.data_dir)
            elif pin["served"]:
                data = scratch = build_served_dir(root)
            else:
                data = scratch = build_data_dir(root)
            run = (measure_served if pin["served"] else measure_run)(data, queries, pin)
        except CheckRefused as exc:
            # ONE handler over BOTH preconditions. Splitting them left `build_data_dir`'s refusal
            # escaping as a traceback and exit 1, and it is the only branch the leg's own argv
            # reaches -- every arm passes --data-dir.
            print(f"check-recall: REFUSED -- {exc}", file=sys.stderr)
            return 2

        failures: list[str] = []

        if args.audit_fixture:
            failures.extend(check_audit(run, pin))
            for f in failures:
                print(f"check-recall: AUDIT RED -- {f}", file=sys.stderr)
            return 1 if failures else 0

        # -- predicate 4: per-id resolution. Reports FIRST so a retired record reads as a retired
        # record, and does NOT stop the run -- the floor still prints its own verdict below.
        if run["unresolved"]:
            failures.append("per-id")
            print(f"check-recall: per-id RED -- unresolved in {pin['set']}: "
                  f"{', '.join(sorted(set(run['unresolved'])))}")
        else:
            print(f"check-recall: per-id ok -- every expected id resolves in {pin['set']} "
                  f"({run['R']}/{run['n']} {'rows' if pin['served'] else 'questions'})")

        # -- predicate 5: the floor. `not evaluated` is a REPORTED state, never a silent skip.
        print(f"check-recall: cell {pin['cell']}  raw {run['cell_value']:.4f}  "
              f"ceiling {run['ceiling']:.4f}")
        for name, s in run.get("slices", {}).items():
            print(f"check-recall: slice {name} h={s['h']} R={s['R']}")
        if run["ceiling"] == 0:
            print(f"check-recall: {PIN_KEY} not evaluated -- ceiling is 0, nothing to divide")
        else:
            normalised = run["cell_value"] / run["ceiling"]
            if normalised + 1e-9 < pin["value"]:
                failures.append(PIN_KEY)
                print(f"check-recall: {PIN_KEY} RED -- normalised {normalised:.4f} < "
                      f"{pin['value']:.2f}")
            else:
                print(f"check-recall: {PIN_KEY} ok -- normalised {normalised:.4f} >= "
                      f"{pin['value']:.2f}")

        if failures:
            print(f"check-recall: FAILED ({', '.join(failures)})", file=sys.stderr)
            return 1
        return 0
    finally:
        if scratch is not None:
            shutil.rmtree(scratch, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
