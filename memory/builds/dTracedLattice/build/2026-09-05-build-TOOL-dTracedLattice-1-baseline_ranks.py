# **Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7
# Committed as evidence for the recall measurement. The root is DERIVED here; the
# scratchpad original hardcoded this session's worktree and would resolve to nothing.
"""Score the shipped reuse_lookup ranking against the lens-3 scenarios, and fold the result in.

Loads the corpus and the reference index ONCE and calls the pure `assemble_shortlist`, so the 28
queries cost one index build rather than 28. Records, per scenario:

  shipped_rank            1-based position of a candidate row whose NAME is the expected symbol,
                          or null when the tool never surfaces that name for that query
  shipped_points_at_file  the def file the merged candidate row carries (the tool merges by name,
                          so this is ONE arbitrary definer, not necessarily the expected one)
  shipped_file_correct    whether that file is the expected one or an also_acceptable one
  shortlist_len           how long the shortlist was, so a rank can be read as a fraction

A rank of null is a RECALL miss and is reported as such -- never silently as a large rank.
"""
from __future__ import annotations

import json
import os
import pathlib
import sys

ROOT = pathlib.Path(os.getcwd())
sys.path.insert(0, str((ROOT / "tools" / "codebase-map").resolve()))
import map_lib as m  # noqa: E402
import reuse_lookup as rl  # noqa: E402


def main(argv: list[str]) -> int:
    scen_path = pathlib.Path(argv[1])
    doc = json.loads(scen_path.read_text(encoding="utf-8"))

    corpus = rl.load_corpus(ROOT)
    idx = m.build_reference_index(corpus.symbol_files, root=ROOT)

    hits = 0
    for s in doc["scenarios"]:
        sl = rl.assemble_shortlist(s["query"], corpus, idx)
        rank = None
        points_at = None
        for i, r in enumerate(sl.ranked, 1):
            if r.candidate.name == s["expected_symbol"]:
                rank, points_at = i, (r.candidate.file or None)
                break
        ok_files = {s["expected_file"]} | {
            a.partition("::")[0] for a in s.get("also_acceptable", [])
        }
        s["shipped_rank"] = rank
        s["shipped_points_at_file"] = points_at
        s["shipped_file_correct"] = bool(points_at and points_at in ok_files)
        s["shortlist_len"] = len(sl.ranked)
        if rank is not None:
            hits += 1
        print(f"{s['id']:7s} {s['expected_symbol']:16s} rank="
              f"{'MISS' if rank is None else str(rank):>4s} / {len(sl.ranked):3d}  "
              f"file_ok={s['shipped_file_correct']!s:5s}  {s['adversarial_role']}")

    n = len(doc["scenarios"])
    doc["$shipped_baseline"] = {
        "measured_on": "the shipped assemble_shortlist, seeds-first then fan-in desc then name",
        "recall_any_rank": f"{hits}/{n}",
        "recall_at_5": sum(
            1 for s in doc["scenarios"] if s["shipped_rank"] and s["shipped_rank"] <= 5),
        "recall_at_10": sum(
            1 for s in doc["scenarios"] if s["shipped_rank"] and s["shipped_rank"] <= 10),
        "file_correct_when_surfaced": sum(1 for s in doc["scenarios"] if s["shipped_file_correct"]),
        "note": "a MISS is a recall failure upstream of any ranking; re-ordering cannot fix one",
    }
    scen_path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nsurfaced at any rank: {hits}/{n}")
    print(f"surfaced in top 5:    {doc['$shipped_baseline']['recall_at_5']}/{n}")
    print(f"surfaced in top 10:   {doc['$shipped_baseline']['recall_at_10']}/{n}")
    print(f"pointed at an acceptable file: "
          f"{doc['$shipped_baseline']['file_correct_when_surfaced']}/{n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
