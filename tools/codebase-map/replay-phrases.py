#!/usr/bin/env python3
"""Replay the reuse probe over this repo's own recorded phrases, and grade it.

WHAT THIS IS FOR. `reuse_lookup.py` is an orientation instrument, and until this harness existed
the only way to say whether a change to it made the answers better was to run a few phrases by hand
and squint. The build records are a ready-made graded corpus: a spec that ran the probe records the
literal phrase it used, and that spec's section 10 names the seam its author actually chose. That
pairing is the ground truth -- a human picked the seam, so it grades against judgement rather than
against every file a unit happened to edit, and it needs no commit-to-id join.

ON NO MERGE-BAR LEG, BY OWNER RULING (2026-08-23, the kit-self-tests split). It grades a corpus and
costs one probe per phrase, so it is a tool you run when you change the ranker, not a gate. It is
registered as `project-owned` in `kit.toml` and removed by the copy-install runbook, because a
harness that parses THIS repo's build records is worth nothing in an adopter's tree and shipping it
is the `pin-copied-from-another-corpus` defect by another route.

THE CEILING IS ENFORCED HERE, by this script, because there is no runner to inherit it from. A suite
on no leg still owes a declared wall-clock bound in this repo -- slowness that annoys is never
fixed, slowness that fails is fixed or re-declared -- so the run is timed and a breach EXITS
NON-ZERO. `--ceiling` re-declares it for a deliberately larger corpus; there is no way to disable it.

Usage:
    {cli}            # grade every phrase, print the summary
    {cli} --json     # the same, machine-readable
    {cli} --limit 20 # grade only the first N, for a quick before/after
    {cli} --floor    # grade the FROZEN population against the recorded floors; exit 1 on a breach
    {cli} --predictors  # also grade which shortlist quantity predicts a MISS; one verdict line
    {cli}            # with no args it also prints the ceiling

`--floor` is the definition-of-done check for a change to the probe's ranking, its candidate lines
or the fan-in it reads (the codebase-map dossier's `## Constraints & why`). It is still on no leg.

`--predictors` is what earns, or refuses, a runtime miss line in `reuse_lookup.py`
(TOOL-aMendedFleet-46). It reads the PREDICTORS quantities off each shortlist, grades each by
its AUC against the hit label over two populations -- every graded phrase, and those whose truth
is reachable -- beside a shuffled-label band, and prints exactly one `miss predictor:` verdict.
Re-run it after
every ranker or corpus change; the codebase-map dossier's `## Gaps` holds the last reading.
"""

from __future__ import annotations

import argparse
import os
import json
import math
import pathlib
import random
import re
import subprocess
import sys
import time
from collections import Counter

sys.dont_write_bytecode = True  # never leave bytecode in the worktree this kit is installed in

# `abspath`, never `resolve()`: this kit is reachable through a junction, and `resolve()` follows it
# to the link target, so this entrypoint would disagree with `map_lib.kit_dir()` about the install
# prefix the two of them stamp into byte-compared artifacts. The kit's own selftest asserts it.
KIT = pathlib.Path(os.path.abspath(__file__)).parent
sys.path.insert(0, str(KIT))

import map_lib as m  # noqa: E402
import reuse_lookup as rl  # noqa: E402


def _resolve_self() -> str:
    """This script as the adopter spells it -- repo-relative when it can be.

    DERIVED, never a literal: a kit path written into shipped bytes arrives verbatim in a tree
    installed at another prefix and resolves to nothing there. `check-install-prefix.sh` bans it,
    and this file earned that refusal on its first commit.
    """
    me = pathlib.Path(os.path.abspath(__file__))
    try:
        return "python3 " + me.relative_to(m.repo_root()).as_posix()
    except (ValueError, Exception):  # noqa: B014 - repo_root can refuse outside a tree
        return "python3 " + me.name


__doc__ = (__doc__ or "").replace("{cli}", _resolve_self())

# THE DECLARED CEILING, in seconds, for the whole run. MEASURED, not guessed: the full corpus of
# 140 phrases grades in ~3s, because the corpus is loaded ONCE and each phrase is an in-process
# rank rather than a subprocess. 60s is ~20x that -- room for the corpus to grow severalfold, and
# still low enough to FIRE if a change makes the ranker pathological.
#
# The first draft of this line said 600s "because the probe is ~1.1s and a full replay is minutes",
# which was reasoning about a subprocess-per-phrase design this file does not have. A 600s ceiling
# over a 3s run is a bound that cannot fail, which is the shape this repo gates hardest against.
# Re-declare it with --ceiling and say why; do not quietly raise it.
CEILING_S = 60.0

# THE FLOOR, over a FROZEN population (TOOL-aMendedFleet-41). The live harvest moves on record
# traffic alone -- 335 phrases at hit rate 0.672 became 378 at 0.696 with no ranker change -- so a
# floor over it reds or passes on records, not on ranking. `--floor` grades only the phrases from
# records whose FILENAME date is on or before FLOOR_CORPUS_DATE (an undated record is outside), and
# refuses at exit 2 when that population no longer counts FLOOR_PHRASES: a floor graded over a
# different population compares nothing. What is left to move the readings is the ranker and the
# symbol corpus, which is what a floor exists to grade.
#
# MEASURED 2026-10-05 on node a at base ef0995af8, after units 35 and 36 landed, over the population
# dated on or before 2026-10-04, at the default budget 24576 B: 431 graded
# phrases (439 in the live harvest), hit rate 0.842, hit@5 0.452, hit@10 0.529, hit@budget 0.833.
# Each floor below is its reading.
#
# MOVING A FLOOR. Raising one is free. Lowering one writes the old value, the new value and the
# reason on the line beside it, so the move is read in review rather than discovered later.
FLOOR_CORPUS_DATE = "2026-10-04"
FLOOR_PHRASES = 431
FLOOR = {
    "hit_rate": 0.842,
    "hit5_rate": 0.452,
    "hit10_rate": 0.529,
    "hit_at_budget": 0.833,
}
_RECORD_DATE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")

# THE MISS-PREDICTOR RULE (TOOL-aMendedFleet-46 S3). A predictor qualifies over one population only
# when its AUC is at or beyond 0.70 / 0.30, lies outside that population's shuffled-label band, and
# the population holds at least PREDICTOR_MIN_LABELS hits AND misses: a threshold fitted to eleven
# misses is a guess with a number attached. These names are the row keys `measure_predictors`
# adds, in the order they print.
PREDICTORS = ("seed_coverage", "best_overlap", "union_coverage", "n_seeds", "n_ranked",
              "idf_coverage", "best_idf", "q_len")
PREDICTOR_AUC_HIGH = 0.70
PREDICTOR_AUC_LOW = 0.30
PREDICTOR_MIN_LABELS = 30
SHUFFLE_TRIALS = 50
SHUFFLE_SEED = 0

# A probe invocation inside a build record. The phrase may WRAP across lines, which is the whole
# reason this is a parser and not a grep: the parent measurement graded 133 phrases and a
# single-line pattern reaches only about half of them.
_INVOKE = re.compile(r'reuse_lookup\.py\s+"([^"]*)"', re.S)
# A placeholder rather than a real phrase -- `"<behaviour>"`, `"<any phrase>"`.
_PLACEHOLDER = re.compile(r"^\s*<[^>]*>\s*$")
# Section 10's backticked path-shaped tokens: the seam the author chose.
_SEC10 = re.compile(r"^##\s*10\.", re.M)
_NEXTSEC = re.compile(r"^##\s+", re.M)
_PATH = re.compile(r"`([A-Za-z0-9_./-]+\.(?:py|sh|js|md|json|toml))`")


def _resolve_repo_root() -> pathlib.Path:
    return m.repo_root()


def scan_tracked_specs(root: pathlib.Path) -> list[str]:
    out = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--", "memory/builds"],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    return [p for p in out if p.endswith(".md")]


def derive_record_date(rel: str) -> str | None:
    """The `YYYY-MM-DD` a record's BASENAME opens with, or None for an undated record."""
    mo = _RECORD_DATE.match(pathlib.PurePosixPath(rel).name)
    return mo.group(1) if mo else None


def derive_floor_breaches(summary: dict, floor: dict) -> list[tuple[str, float, float]]:
    """Every (metric, reading, floor) whose reading sits under its floor. A missing reading breaches."""
    return [(k, summary.get(k), f) for k, f in floor.items()
            if summary.get(k) is None or summary[k] < f]


def extract_phrases(root: pathlib.Path, rel: str) -> list[tuple[str, list[str]]]:
    """Every (phrase, ground-truth paths) pair a spec carries.

    The ground truth is the section-10 path set for the WHOLE document, which is the seam its
    author recorded. A spec running several probes shares one section 10, and that is correct:
    the author chose one seam after running them.
    """
    try:
        text = (root / rel).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    # Join wrapped invocations: the phrase is whatever sits between the quotes, newlines and the
    # markdown continuation indent collapsed to single spaces.
    found = []
    for mo in _INVOKE.finditer(text):
        raw = mo.group(1)
        phrase = " ".join(raw.split())
        if not phrase or _PLACEHOLDER.match(phrase):
            continue
        found.append(phrase)
    if not found:
        return []
    truth = _parse_section10_paths(text)
    return [(p, truth) for p in dict.fromkeys(found)]


def _parse_section10_paths(text: str) -> list[str]:
    """Every backticked path-shaped token in a spec's section 10.

    KNOWN LIMITATION, declared rather than left for a reader to discover: this has NO notion of
    negation. A section 10 saying "the probe returned `map_lib.py`, which is NOT the seam"
    contributes that path as ground TRUTH, so a phrase whose author recorded a MISS can score as a
    hit. The corpus contains such sections -- an author writing down what the probe got wrong is
    doing the right thing, and this harvester reads it backwards.

    The effect INFLATES the hit rate, so every figure here is an upper bound on the ranker's
    quality rather than an estimate of it. That is tolerable for the BEFORE/AFTER deltas this
    harness exists to produce, because the same bias sits on both sides; it is not tolerable as an
    absolute claim, and nothing should quote it as one.

    Fixing it needs the spec set to MARK a section-10 citation as a miss -- a convention, not a
    parser -- which is a change to `TEMPLATE-SPEC` and therefore its own unit.
    """
    mo = _SEC10.search(text)
    if not mo:
        return []
    rest = text[mo.end():]
    nxt = _NEXTSEC.search(rest)
    body = rest[: nxt.start()] if nxt else rest
    return sorted(set(_PATH.findall(body)))


def check_path_match(candidate: str, target: str) -> bool:
    """Does a ranked path satisfy a ground-truth target? ONE predicate, read twice.

    `measure_phrase` uses it to find a hit and the unreachable count uses it to ask whether any
    hit is possible at all. Those two were byte-identical hand-copies for one commit, which makes
    the denominator and the numerator able to disagree about what a match IS -- and a hit rate
    whose two halves disagree is worse than no hit rate.
    """
    return (candidate == target
            or candidate.endswith("/" + target)
            or target.endswith("/" + candidate))


def check_truth_reachable(truth: list[str], corpus_files: set[str]) -> bool:
    """Can ANY ranked file satisfy this ground truth? The one reachability predicate: `main`'s
    unreachable count and `measure_predictors`' per-row field both read it."""
    return any(check_path_match(f, x) for x in truth for f in corpus_files)


def measure_phrase(corpus, ref, phrase: str, truth: list[str], budget: int = 0,
                   scan: dict | None = None, shortlist=None) -> dict:
    """Rank one phrase and locate the first ground-truth path in the shortlist.

    `shortlist` lets a caller that already assembled it reuse it rather than rank twice."""
    sl = shortlist if shortlist is not None else rl.assemble_shortlist(phrase, corpus, ref, scan)
    # hit@budget reads the cut `reuse_lookup` prints, from the function that prints it
    # (TOOL-aMendedFleet-36 S5); it never re-derives the cut here.
    shown, _ = rl.derive_budget_cut(sl, corpus, budget)
    # RANK BY CANDIDATE, NOT BY FILE, and the difference is not cosmetic. `TOOL-dTracedLattice-1` S1
    # replaced `Candidate.file` with `files`, so one candidate now contributes every definer of its
    # symbol. Counting file POSITIONS then makes a candidate with four definers cost four ranks,
    # and the shortlist a reader actually scans is ONE LINE PER CANDIDATE with the definers on it.
    # Measured over these 143 phrases at the commit S1 landed: by file position the change reads
    # hit@5 0.462 -> 0.378, and by candidate position it reads 0.385 -> 0.385 with hit@10 up from
    # 0.420 to 0.441 and the hit rate up from 0.587 to 0.615. The first reading is a metric artifact
    # of the data-model change; the second is the object the tool is for.
    rank = next((i for i, r in enumerate(sl.ranked, 1)
                 if any(check_path_match(f, t) for f in r.candidate.files for t in truth)), None)
    return {
        "phrase": phrase,
        "truth": truth,
        "n_ranked": len(sl.ranked),
        "rank": rank,
        "hit": rank is not None,
        "hit5": rank is not None and rank <= 5,
        "hit10": rank is not None and rank <= 10,
        "hit_at_budget": rank is not None and rank <= len(shown),
    }


def measure_predictors(corpus, ref, phrase: str, truth: list[str], budget: int = 0,
                       scan: dict | None = None, corpus_files: set[str] | None = None,
                       name_df: dict | None = None) -> dict:
    """`measure_phrase`'s row, plus `reachable` and every one of PREDICTORS read off ONE shortlist.

    Every value is a property of the seeds and the query's stems, because `assemble_shortlist`
    carries no score: there is no second ranker here. A seed's shared stems are its NAME stems
    shared with the query, plus the `## Shared seams` prose stems when that prose is why it seeded.
    IDF is over candidate NAMES, `log((N+1)/(df+1))`. `corpus_files` and `name_df` are per-corpus
    and are passed in by `main` so a replay does not re-derive them per phrase.
    """
    sl = rl.assemble_shortlist(phrase, corpus, ref, scan)
    row = measure_phrase(corpus, ref, phrase, truth, budget, scan, shortlist=sl)
    if corpus_files is None:
        corpus_files = {f for c in corpus.candidates.values() for f in c.files}
    if name_df is None:
        name_df = Counter(s for n in corpus.candidates for s in m.stems(n))
    n_names = len(corpus.candidates)
    row["reachable"] = check_truth_reachable(truth, corpus_files)

    qstems = m.stems(phrase)
    shared = []
    for r in sl.ranked:
        if not r.is_seed:
            continue
        s = qstems & m.stems(r.candidate.name)
        if r.reason.startswith("shared-seams prose"):
            s |= qstems & m.stems(corpus.shared_seams.get(r.candidate.detail, ""))
        shared.append(s)

    # every shared stem is a query stem, so one weight per query stem covers every seed
    idf = {s: math.log((n_names + 1) / (name_df.get(s, 0) + 1)) for s in qstems}
    q_idf = sum(idf.values())
    best_overlap = max((len(s) for s in shared), default=0)
    best_idf = max((sum(idf[x] for x in s) for s in shared), default=0.0)
    union = set().union(*shared) if shared else set()
    row.update({
        "seed_coverage": best_overlap / len(qstems) if qstems else 0.0,
        "best_overlap": best_overlap,
        "union_coverage": len(union) / len(qstems) if qstems else 0.0,
        "n_seeds": len(shared),
        "n_ranked": len(sl.ranked),
        "idf_coverage": best_idf / q_idf if q_idf else 0.0,
        "best_idf": best_idf,
        "q_len": len(qstems),
    })
    return row


def derive_auc(pos: list[float], neg: list[float]) -> float | None:
    """Mann-Whitney AUC, P(a positive outranks a negative), ties counted half. None when a side is
    empty: a population with no misses has no AUC, and 0.5 would read as a measured chance."""
    if not pos or not neg:
        return None
    vals = sorted([(v, 1) for v in pos] + [(v, 0) for v in neg])
    rank_sum = 0.0
    i = 0
    while i < len(vals):
        j = i
        while j < len(vals) and vals[j][0] == vals[i][0]:
            j += 1
        rank_sum += (i + 1 + j) / 2 * sum(lab for _, lab in vals[i:j])  # the tie group's mean rank
        i = j
    n1, n0 = len(pos), len(neg)
    return (rank_sum - n1 * (n1 + 1) / 2) / (n1 * n0)


def measure_shuffle_band(rows: list[dict], trials: int = SHUFFLE_TRIALS,
                         seed: int = SHUFFLE_SEED) -> tuple[float, float] | None:
    """(min, max) AUC that ANY predictor reaches over `trials` shuffles of the hit labels, from a
    fixed seed: the noise floor of the whole table, not of one row. None when no AUC exists."""
    labels = [bool(r["hit"]) for r in rows]
    rng = random.Random(seed)
    aucs = []
    for _ in range(trials):
        rng.shuffle(labels)
        for p in PREDICTORS:
            a = derive_auc([r[p] for r, h in zip(rows, labels) if h],
                           [r[p] for r, h in zip(rows, labels) if not h])
            if a is not None:
                aucs.append(a)
    return (min(aucs), max(aucs)) if aucs else None


def measure_population(name: str, rows: list[dict], trials: int = SHUFFLE_TRIALS,
                       seed: int = SHUFFLE_SEED) -> dict:
    """One population's table: label split, one AUC per predictor (hits positive), and its band."""
    hits = [r for r in rows if r["hit"]]
    misses = [r for r in rows if not r["hit"]]
    band = measure_shuffle_band(rows, trials, seed)
    return {
        "population": name,
        "phrases": len(rows),
        "hits": len(hits),
        "misses": len(misses),
        "aucs": {p: derive_auc([r[p] for r in hits], [r[p] for r in misses]) for p in PREDICTORS},
        "band": list(band) if band else None,
    }


def derive_predictor_verdict(populations: list[dict]) -> str:
    """S3's rule over `measure_population` tables: the strongest qualifying predictor, or
    `none qualifies — <why, per population>`. Too few hits or misses is a reason, never an AUC."""
    best = None
    reasons = []
    for pop in populations:
        name = pop["population"]
        if pop["misses"] < PREDICTOR_MIN_LABELS or pop["hits"] < PREDICTOR_MIN_LABELS:
            side = "misses" if pop["misses"] < PREDICTOR_MIN_LABELS else "hits"
            reasons.append(f"{name}: too few {side} ({pop['hits']} hits, {pop['misses']} misses; "
                           f"{PREDICTOR_MIN_LABELS} of each needed)")
            continue
        if not pop["band"]:
            reasons.append(f"{name}: no shuffle band, so no AUC can be read against noise")
            continue
        lo, hi = pop["band"]
        ok = [(abs(a - 0.5), p, a) for p, a in pop["aucs"].items()
              if a is not None and (a >= PREDICTOR_AUC_HIGH or a <= PREDICTOR_AUC_LOW)
              and not lo <= a <= hi]
        if not ok:
            reasons.append(f"{name}: no AUC at or beyond {PREDICTOR_AUC_HIGH:.2f} / "
                           f"{PREDICTOR_AUC_LOW:.2f} outside the band {lo:.3f}-{hi:.3f}")
            continue
        top = max(ok)
        if best is None or top[0] > best[0]:
            best = (top[0], top[1], top[2], name)
    if best:
        return f"{best[1]} ({best[3]} population, AUC {best[2]:.3f})"
    return "none qualifies — " + "; ".join(reasons)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--limit", type=int, default=0, help="grade only the first N phrases")
    ap.add_argument("--ceiling", type=float, default=CEILING_S,
                    help=f"wall-clock ceiling in seconds (declared: {CEILING_S:g})")
    ap.add_argument("--budget", type=int, default=rl.DEFAULT_BUDGET,
                    help=f"byte budget hit@budget is read at (default {rl.DEFAULT_BUDGET}); "
                         "0 = unbounded")
    ap.add_argument("--floor", action="store_true",
                    help=f"grade the population dated on or before {FLOOR_CORPUS_DATE} against "
                         "the recorded floors; exit 1 on a breach, 2 if the population moved")
    ap.add_argument("--predictors", action="store_true",
                    help="also grade which shortlist quantity predicts a miss, and print one "
                         "`miss predictor:` verdict (TOOL-aMendedFleet-46)")
    args = ap.parse_args()

    if args.floor and args.limit:
        print("replay-phrases: REFUSING — --floor with --limit: a partial population cannot be "
              "graded against a floor of the whole.", file=sys.stderr)
        return 2
    if args.floor and args.budget != rl.DEFAULT_BUDGET:
        print(f"replay-phrases: REFUSING — --floor at --budget {args.budget}: the hit_at_budget "
              f"floor was read at the default {rl.DEFAULT_BUDGET}.", file=sys.stderr)
        return 2

    if not args.json:
        print(f"# replay-phrases: declared wall-clock ceiling {args.ceiling:g}s "
              f"(default {CEILING_S:g}s) — a breach EXITS NON-ZERO")

    t0 = time.monotonic()
    root = _resolve_repo_root()
    pairs: list[tuple[str, list[str]]] = []
    for rel in scan_tracked_specs(root):
        # the date cut runs BEFORE the de-duplication, so no ground truth comes from a later record
        if args.floor and (derive_record_date(rel) or "9999") > FLOOR_CORPUS_DATE:
            continue
        pairs.extend(extract_phrases(root, rel))
    # de-duplicate on the phrase, keeping the first ground truth seen
    seen: dict[str, list[str]] = {}
    for p, t in pairs:
        seen.setdefault(p, t)
    graded = [(p, t) for p, t in seen.items() if t]
    ungraded = len(seen) - len(graded)
    if args.limit:
        graded = graded[: args.limit]
    if args.floor and len(graded) != FLOOR_PHRASES:
        print(f"replay-phrases: REFUSING — the floor population dated on or before "
              f"{FLOOR_CORPUS_DATE} counts {len(graded)} graded phrase(s), pinned at "
              f"{FLOOR_PHRASES}; a floor graded over a different population compares nothing.",
              file=sys.stderr)
        return 2

    corpus = rl.load_corpus()
    # The scan stats ride each shortlist so its header -- which the budget charges -- carries the
    # bytes a real lookup prints.
    scan: dict = {}
    ref = m.build_reference_index(corpus.symbol_files, stats=scan)
    corpus_files = {f for c in corpus.candidates.values() for f in c.files}
    if args.predictors:
        name_df = Counter(s for n in corpus.candidates for s in m.stems(n))
        rows = [measure_predictors(corpus, ref, p, t, args.budget, scan, corpus_files, name_df)
                for p, t in graded]
    else:
        rows = [measure_phrase(corpus, ref, p, t, args.budget, scan) for p, t in graded]

    # THE DENOMINATOR IS DECLARED. A phrase whose ground-truth paths are not in the ranked corpus
    # at all -- a spec citing a file the symbol index does not carry -- can never register a hit,
    # so it depresses `hit_rate` for a reason that has nothing to do with the ranker. It is counted
    # and REPORTED rather than silently dropped: dropping it would flatter the figure, and hiding
    # it would leave two ranker changes measured against an undeclared floor.
    unreachable = sum(1 for _, t in graded if not check_truth_reachable(t, corpus_files))
    hits = [r for r in rows if r["hit"]]
    ranks = sorted(r["rank"] for r in hits)
    # The UPPER of the two middle values on an even count. Named honestly rather than averaged:
    # a rank is an ordinal position, so the mean of two ranks is not a rank.
    median = ranks[len(ranks) // 2] if ranks else None
    elapsed = time.monotonic() - t0

    summary = {
        "phrases_graded": len(rows),
        "phrases_without_ground_truth": ungraded,
        "phrases_truth_unreachable": unreachable,
        "hit_rate": round(len(hits) / len(rows), 3) if rows else None,
        "hit5_rate": round(sum(r["hit5"] for r in rows) / len(rows), 3) if rows else None,
        "hit10_rate": round(sum(r["hit10"] for r in rows) / len(rows), 3) if rows else None,
        "budget": args.budget,
        "hit_at_budget": (round(sum(r["hit_at_budget"] for r in rows) / len(rows), 3)
                          if rows else None),
        "upper_median_rank_of_first_correct": median,
        "elapsed_s": round(elapsed, 1),
        "ceiling_s": args.ceiling,
        "corpus_symbols": measure_corpus_symbols(corpus),
    }

    if args.predictors:
        populations = [measure_population("all", rows),
                       measure_population("reachable", [r for r in rows if r["reachable"]])]
        summary["predictors"] = {
            "populations": populations,
            "trials": SHUFFLE_TRIALS,
            "seed": SHUFFLE_SEED,
            "rule": {"auc_high": PREDICTOR_AUC_HIGH, "auc_low": PREDICTOR_AUC_LOW,
                     "min_labels": PREDICTOR_MIN_LABELS},
            "verdict": derive_predictor_verdict(populations),
        }
        elapsed = time.monotonic() - t0  # the shuffles are inside the ceiling, not after it
        summary["elapsed_s"] = round(elapsed, 1)

    breaches = derive_floor_breaches(summary, FLOOR) if args.floor else []
    floor_obj = {
        "corpus_date": FLOOR_CORPUS_DATE,
        "phrases": len(rows),
        "phrases_pinned": FLOOR_PHRASES,
        "budget": args.budget,
        "metrics": {k: {"reading": summary[k], "floor": f} for k, f in FLOOR.items()},
        "breaches": [k for k, _, _ in breaches],
    }

    if args.json:
        out = {"summary": summary, "rows": rows}
        if args.floor:
            out["floor"] = floor_obj
        print(json.dumps(out, indent=2, sort_keys=True))
    else:
        print(f"# graded {summary['phrases_graded']} phrase(s); "
              f"{summary['phrases_without_ground_truth']} carried no section-10 ground truth")
        print(f"hit rate                    {summary['hit_rate']}")
        print(f"hit@5                       {summary['hit5_rate']}")
        print(f"hit@10                      {summary['hit10_rate']}")
        print(f"hit@budget ({args.budget} B)    {summary['hit_at_budget']}")
        print(f"upper-median rank of first correct {summary['upper_median_rank_of_first_correct']}")
        print(f"phrases that CANNOT hit (truth outside the corpus) "
              f"{summary['phrases_truth_unreachable']}")
        print(f"elapsed                     {summary['elapsed_s']}s against a {args.ceiling:g}s ceiling")
        if args.floor:
            print(f"# floor: population dated on or before {FLOOR_CORPUS_DATE} · "
                  f"{len(rows)} phrase(s), pinned {FLOOR_PHRASES} · budget {args.budget} B")
            for k, f in FLOOR.items():
                print(f"floor {k:<14} {summary[k]}  floor {f}")
        if args.predictors:
            pred = summary["predictors"]
            print(f"# miss predictors: AUC of each value, hits against misses; 0.5 is chance. "
                  f"Qualifies at >= {PREDICTOR_AUC_HIGH:.2f} or <= {PREDICTOR_AUC_LOW:.2f}, "
                  f"outside the band, with {PREDICTOR_MIN_LABELS}+ hits and misses")
            for pop in pred["populations"]:
                band = ("{:.3f}-{:.3f}".format(*pop["band"]) if pop["band"] else "none")
                print(f"population {pop['population']}: {pop['phrases']} phrase(s), "
                      f"{pop['hits']} hit(s), {pop['misses']} miss(es); shuffle band {band} "
                      f"over {pred['trials']} trials, seed {pred['seed']}")
                for p, a in pop["aucs"].items():
                    print(f"  {p:<16} {'n/a' if a is None else f'{a:.3f}'}")
            print(f"miss predictor: {pred['verdict']}")

    if not rows:
        print("replay-phrases: REFUSING — graded 0 phrases, so every figure above is vacuous. "
              "A run that finds nothing is not a passing run.", file=sys.stderr)
        return 2
    for k, reading, f in breaches:
        print(f"replay-phrases: FLOOR BREACHED — {k} {reading} under its floor {f}", file=sys.stderr)
    if elapsed > args.ceiling:
        print(f"replay-phrases: CEILING BREACHED — {elapsed:.1f}s against {args.ceiling:g}s. "
              "Fix the cost or re-declare the ceiling with a reason; do not raise it quietly.",
              file=sys.stderr)
        return 1
    return 1 if breaches else 0


def measure_corpus_symbols(corpus) -> int:
    return sum(1 for c in corpus.candidates.values() if c.kind)


if __name__ == "__main__":
    raise SystemExit(main())
