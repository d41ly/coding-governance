#!/usr/bin/env python3
"""rank_harness.py — score `reuse_lookup`'s ranking against a scenario set, with its controls.

    python <kit>/rank_harness.py --scenarios <kit>/scen-adversarial.json
    python <kit>/rank_harness.py --scenarios <path> --control shuffle --trials 200
    python <kit>/rank_harness.py --scenarios <path> --control constant

WHY THIS IS A TRACKED FILE AND NOT A SCRATCHPAD SCRIPT. `TOOL-dTracedLattice-1` S8: the numbers
that decide whether a ranking change lands were produced by scripts that lived in one session's
scratchpad, so the next reader could re-read the conclusion and not the instrument. An instrument
nobody can re-run is a remembered number.

**A MISS IS REPORTED AS A MISS.** S4, and it is the whole reason the rev-4 design mistook a recall
failure for a ranking change: a harness that folds an unfound answer in as `rank = len(shortlist)`
turns "the tool never returned the answer at any K" into "the tool returned it last", which averages
into a ranking delta and reads as one. Here an unfound answer has rank `None`, is counted in
`misses`, and is printed by id.

**AND A DEAD PROBE IS NOT A ZERO.** A scenario whose expected file is no longer in the tree cannot
be answered by any ranking, so averaging it as a 0 makes the tool look worse for a defect in the
FIXTURE. Those are reported separately and excluded from the rates, and a set where every scenario
is dead REFUSES rather than reporting 0.0 recall.

WHAT IT DOES NOT DO, stated because a harness's silence reads as coverage. It scores ONE ranking —
whatever `reuse_lookup` does in this working tree — so a before/after comparison is two runs at two
commits, not a flag. It grades FILE granularity against `expected_file` plus `also_acceptable`, and
never symbol granularity. It has no significance test: `AGENTS.md`-grade paired significance
(McNemar, the discordant-pair count) is the caller's job over two runs of this.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

import os  # noqa: E402 — abspath, never resolve(): see the kit's own selftest arm
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent))

import map_lib as m  # noqa: E402
import reuse_lookup as rl  # noqa: E402

KS = (1, 5, 10, 20)


def load_scenarios(path: Path) -> list[dict]:
    """The set, from a JSON file or from the first ```json fence of a Markdown record.

    Both spellings, because the set is AUTHORED inside a build record (which owes a binding line
    that JSON cannot carry) and SHIPPED as a fixture beside the kit. One reader, so the two cannot
    drift into two different sets.
    """
    text = path.read_text(encoding="utf-8")
    if path.suffix != ".json":
        start = text.index("```json") + len("```json")
        text = text[start:text.index("```", start)]
    doc = json.loads(text)
    rows = doc.get("scenarios") or []
    if not rows:
        raise SystemExit(f"rank_harness: {path} carries no `scenarios` array")
    return rows


def derive_targets(row: dict) -> set[str]:
    """Every file that counts as a correct answer for this row."""
    out = {row["expected_file"]}
    for alt in row.get("also_acceptable", ()):
        out.add(alt.split("::", 1)[0])
    return out


def measure_ranks(rows: list[dict], root: Path) -> tuple[list[dict], list[str]]:
    """One `(row, rank)` per scenario plus the DEAD ones, named.

    `rank` is 1-based over the shortlist's file sequence, or `None` for a miss. A dead probe — a
    scenario whose targets are all absent from the tree — is returned separately and never scored.
    """
    corpus = rl.load_corpus(root)
    scan: dict = {}
    ref_index = (m.build_reference_index(corpus.symbol_files, root=root, stats=scan)
                 if corpus.symbol_files else {})
    scored: list[dict] = []
    dead: list[str] = []
    for row in rows:
        targets = derive_targets(row)
        if not any((root / t).is_file() for t in targets):
            dead.append(row["id"])
            continue
        shortlist = rl.assemble_shortlist(row["query"], corpus, ref_index, scan)
        seen: list[str] = []
        for r in shortlist.ranked:
            for f in r.candidate.files:
                if f not in seen:
                    seen.append(f)
        rank = next((i + 1 for i, f in enumerate(seen) if f in targets), None)
        scored.append({"id": row["id"], "rank": rank, "depth": len(seen), "targets": sorted(targets)})
    return scored, dead


def derive_live_rows(rows: list[dict], scored: list[dict]) -> list[dict]:
    """The rows that were actually SCORED — the denominator `measure_recall` divides by.

    One function, two callers, so a control and the measurement cannot drift onto different
    populations. They did: the control divided by every row while the measured rate divided by the
    live ones, so a dead probe shrank one and not the other and the comparison flattered the
    ranking. A control that is not comparable is not a control.
    """
    live = {s["id"] for s in scored}
    return [r for r in rows if r["id"] in live]


def measure_recall(scored: list[dict], k: int) -> float:
    """Fraction of LIVE scenarios whose target appears in the top `k` files. A miss is a miss."""
    if not scored:
        return float("nan")
    return sum(1 for s in scored if s["rank"] is not None and s["rank"] <= k) / len(scored)


def run_shuffle_control(scored: list[dict], k: int, trials: int, seed: int = 0) -> list[float]:
    """AC3 — the same shortlists in random order, `trials` times.

    The control keeps each scenario's DEPTH and whether the answer was present at all, and randomises
    only the position. So it answers "would a coin toss over this shortlist have done as well", which
    is the question a ranking change has to beat; beating the SHIPPED key at depth does not.
    """
    rng = random.Random(seed)
    out = []
    for _ in range(trials):
        hits = 0
        for s in scored:
            if s["rank"] is None or s["depth"] == 0:
                continue
            if rng.randint(1, s["depth"]) <= k:
                hits += 1
        out.append(hits / len(scored))
    return sorted(out)


def run_constant_control(rows: list[dict], root: Path, k: int, since: str = "HEAD~200") -> float:
    """AC9 — ignore the query and return the K most-frequently-changed files.

    A ranking that does not beat this establishes nothing: the answer is usually in a file that
    changes a lot, so churn alone scores. Fails OPEN with `nan` where git cannot answer, and says
    so, rather than reporting a 0 that reads as "the control scored nothing".
    """
    import subprocess
    try:
        out = subprocess.run(["git", "-C", str(root), "log", "--format=", "--name-only", since + "..HEAD"],
                             capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return float("nan")
    counts: dict[str, int] = {}
    for line in out.splitlines():
        line = line.strip()
        if line:
            counts[line] = counts.get(line, 0) + 1
    top = [f for f, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:k]]
    if not top or not rows:
        return float("nan")
    hits = sum(1 for row in rows if derive_targets(row) & set(top))
    return hits / len(rows)


def render_report(rows, scored, dead, args, root) -> str:
    out = [f"# rank_harness over {len(rows)} scenario(s) from {args.scenarios}",
           f"# live {len(scored)} | dead probes {len(dead)}"]
    if dead:
        out.append("# DEAD PROBE (target absent from the tree; NOT scored as a miss): "
                   + ", ".join(dead))
    if not scored:
        raise SystemExit("rank_harness: every scenario is a dead probe, so nothing was measured. "
                         "Refusing to print a recall figure over an empty set.")
    for k in KS:
        n = sum(1 for s in scored if s["rank"] is not None and s["rank"] <= k)
        out.append(f"recall@{k}: {n}/{len(scored)} ({measure_recall(scored, k):.3f})")
    misses = [s["id"] for s in scored if s["rank"] is None]
    out.append(f"misses (answer at NO depth, not a late rank): {len(misses)}"
               + (" — " + ", ".join(misses) if misses else ""))
    if args.control == "shuffle":
        dist = run_shuffle_control(scored, args.k, args.trials)
        p95 = dist[int(0.95 * (len(dist) - 1))]
        real = measure_recall(scored, args.k)
        out.append(f"shuffle control @{args.k}, {args.trials} trials: p50={dist[len(dist)//2]:.3f} "
                   f"p95={p95:.3f} | measured={real:.3f} | "
                   + ("CLEARS the 95th percentile" if real > p95 else "DOES NOT clear the 95th percentile"))
    elif args.control == "constant":
        c = run_constant_control(derive_live_rows(rows, scored), root, args.k)
        real = measure_recall(scored, args.k)
        if c != c:  # nan
            out.append(f"constant control @{args.k}: UNAVAILABLE (git could not answer) — not a 0")
        else:
            out.append(f"constant control @{args.k} (most-changed files, query ignored): {c:.3f} | "
                       f"measured={real:.3f} | "
                       + ("beats it" if real > c else "DOES NOT beat it"))
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.replace("<kit>", m.kit_rel()))
    parser.add_argument("--scenarios", required=True, help="a .json fixture or a .md record with a json fence")
    parser.add_argument("--control", choices=("none", "shuffle", "constant"), default="none")
    parser.add_argument("--trials", type=int, default=200)
    parser.add_argument("--k", type=int, default=5)
    args = parser.parse_args(argv)

    root = m.repo_root()
    rows = load_scenarios(Path(args.scenarios))
    scored, dead = measure_ranks(rows, root)
    print(render_report(rows, scored, dead, args, root), end="")
    return 0  # a measurement, never a gate


if __name__ == "__main__":
    sys.exit(main())
