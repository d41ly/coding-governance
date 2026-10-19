# **Serves:** research PLAY-dClosedLoop-1
"""The whole-design audit's recall, scored: each run's confirmed findings read by their `[tag]` addresses against the
sealed key of the past defects planted back into the walk's copy.

Today's replay scorer refuses a design report, since it scores only `§<n>` addresses
(`tools/workflows/review_replay.py`, research-final-audit `[5]`). This one reads the address grammar the walk returns,
`<record> [<section tag>]` with the clause id or item tag that carries the defect (the round record's `[walk-table]`).

The key is JSON kept outside the repository until both runs are scored, its SHA-256 pinned in every walker's brief
before launch: `{"base": <sha>, "plants": [{"id", "record", "tag", "anchor", "words", "mechanical", "source"}]}`.
A confirmed finding hits a plant when its address names the plant's record and tag, the plant's anchor (a clause id or
an item tag, where it has one) appears in the finding, and so does one of the plant's words. A plant counts once per
run. A finding under `## Refuted` never hits.

Usage: python score.py --key <key.json> --sha256 <hex> <report-a.md> [<report-b.md>] [--plant tamper|blind|miss]
Prints each run's hits, its recall and the union's, Mills's estimate of the real defects left, from the share of
plants found, and Chapman's over the two runs' real findings, matched by full address. The bar (final-questions
`[audit]`): each run finds at least two thirds of the plants and the two together at least ten of twelve. Stage 0 must
also catch the mechanical plants on the copy itself, every time, which `stage0.py --root <copy>` shows and this script
does not. Exit 0 when the bar is met, 1 when it is not, 2 on a key whose hash moved or a report with nothing to score.

What it does not judge: whether a hit's finding describes the plant's defect rather than a neighbour at the same
address, which the round record's `[recall]` reads each hit for by hand; and whether two runs' findings at one address
are one defect, so Chapman is a trend, never the gate.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ID = r"[AB](?:[1-5]|S[1-4])-F\d+"
CONFIRMED = ("Critical", "High", "Medium", "Low")


def opt(flag):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else None


def findings(path):
    """Each confirmed finding of a report: (id, address, text), read under its severity sections."""
    text = Path(path).read_text(encoding="utf-8")
    out, section = [], None
    for block in re.split(r"(?m)^(?=## |### )", text):
        h2 = re.match(r"## (\w+)", block)
        if h2:
            section = h2.group(1)
            continue
        m = re.match(r"### (" + ID + r")\b", block)
        if m and section in CONFIRMED:
            addr = re.search(r"^- \*\*Address:\*\* (.+)$", block, flags=re.M)
            out.append((m.group(1), addr.group(1).replace("`", "").strip() if addr else "", block))
    return out


def hits(key, found):
    got = {}
    for p in key["plants"]:
        for fid, addr, text in found:
            m = re.match(r"([a-z0-9-]+) \[([a-z0-9-]+)\]", addr)
            if not m or (m.group(1), m.group(2)) != (p["record"], p["tag"]):
                continue
            if p.get("anchor") and p["anchor"] not in text:
                continue
            if not any(w.lower() in text.lower() for w in p["words"]):
                continue
            got.setdefault(p["id"], fid)
    return got


def main():
    key_path, pinned = opt("--key"), opt("--sha256")
    plant = opt("--plant")
    reports = [a for i, a in enumerate(sys.argv[1:], 1)
               if not a.startswith("--") and sys.argv[i - 1] not in ("--key", "--sha256", "--plant")]
    raw = Path(key_path).read_bytes()
    digest = hashlib.sha256(raw if plant != "tamper" else raw + b" ").hexdigest()
    if digest != pinned:
        print(f"score: REFUSED — the key's SHA-256 is {digest}, and the briefs pinned {pinned}")
        return 2
    key = json.loads(raw)
    plants = key["plants"]
    judged = [p for p in plants if not p.get("mechanical")]
    runs = []
    for r in reports:
        found = findings(r)
        if plant == "blind":
            found = [(i, "", t) for i, _, t in found]
        if plant == "miss" and runs == [] and found:
            first = hits(key, found)
            drop = next(iter(first.values()), None)
            found = [f for f in found if f[0] != drop]
        if not found or not any(a for _, a, _ in found):
            print(f"score: REFUSED — {Path(r).name}: no confirmed finding carries an address to score")
            return 2
        runs.append((Path(r).name, found, hits(key, found)))
    for name, found, h in runs:
        n = sum(1 for p in judged if p["id"] in h)
        print(f"{name}: confirmed {len(found)}, plants hit {len(h)} of {len(plants)} ({100 * len(h) / len(plants):.0f}%), "
              f"of them judgement plants {n} of {len(judged)}")
        for pid, fid in sorted(h.items()):
            print(f"  {pid} <- {fid}")
    union = set().union(*(set(h) for _, _, h in runs)) if runs else set()
    print(f"union: plants hit {len(union)} of {len(plants)}")

    def real(found, h):
        """The run's real defects: its confirmed findings that hit no plant, one per full address."""
        return {a for fid, a, _ in found if fid not in h.values()}

    # Mills: a run's real defects, scaled by the share of the plants it found.
    for name, found, h in runs:
        r = real(found, h)
        est = len(r) * len(plants) / len(h) if h else float("inf")
        print(f"mills {name}: real defects {len(r)}, estimated {est:.0f}, left {est - len(r):.0f}")
    if len(runs) == 2:
        a, b = real(runs[0][1], runs[0][2]), real(runs[1][1], runs[1][2])
        m = len(a & b)
        chapman = (len(a) + 1) * (len(b) + 1) / (m + 1) - 1
        print(f"chapman: run A {len(a)}, run B {len(b)}, both {m}, estimated {chapman:.0f}, found by neither "
              f"{chapman - len(a | b):.0f} (a trend, never the gate)")
    need, both_need = -(-2 * len(plants) // 3), -(-10 * len(plants) // 12)
    each = all(len(h) >= need for _, _, h in runs)
    both = len(union) >= both_need if len(runs) == 2 else True
    met = each and both
    print(f"bar: each run at least {need} of {len(plants)} plants, the two together at least {both_need}: "
          f"{'MET' if met else 'NOT MET'}" + (f" · plant {plant}" if plant else ""))
    return 0 if met else 1


if __name__ == "__main__":
    sys.exit(main())
