# **Serves:** research PLAY-dClosedLoop-1
"""Whether each plant's deleted rule survives in the sealed copy where a walker could read it: for each plant, its
distinctive phrases counted in the copy's allowed design records (build/*.md but the comparison, instruments and
session-log records), in those excluded records, and in the copy's reviews/. A rule found only in excluded history
was detectable by cross-reference only through a forbidden read; found nowhere, only by reasoning.

Usage: python -X utf8 detectability.py <copy root>
"""
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1]) / "memory/builds/dClosedLoop"
EXCL = re.compile(r"compared|instruments|session-log")
PHRASES = {
    "P01 step walk's failure route": ["failed or killed step", "stopping the walk", "naming the last completed"],
    "P02 journal alias": ["read-only retired alias", "journal` alias", "journal` kept"],
    "P03 supervisor restart": ["before its first beat", "slot reservation rebuilt", "exactly one act session"],
    "P04 owner-origin intake": ["owner-origin", "marking its origin"],
    "P05 declined retirement": ["declined retirement", "declined proposal"],
    "P06 entry.claim unreachable": ["no local id minted"],
    "P07 fallback-witness drain": ["witnessed under the fallback", "fallback witness", "drain landing"],
    "P10 commit queue": ["commit queue"],
}
files = sorted(root.glob("build/*.md"))
allowed = [f for f in files if not EXCL.search(f.name)]
excluded = [f for f in files if EXCL.search(f.name)]
reviews = sorted(root.glob("reviews/*.md"))
text = {f: f.read_text(encoding="utf-8", errors="replace") for f in allowed + excluded + reviews}


def where(fs, phrase):
    hits = [(f.name.split("PLAY-dClosedLoop-1-")[-1], text[f].count(phrase)) for f in fs if phrase in text[f]]
    return sum(n for _, n in hits), [h for h, _ in hits]


for plant, phrases in PHRASES.items():
    print(plant)
    for ph in phrases:
        a, af = where(allowed, ph)
        e, _ = where(excluded, ph)
        r, _ = where(reviews, ph)
        print(f"  {ph!r}: allowed {a} ({', '.join(af[:4])}{' ...' if len(af) > 4 else ''}), excluded {e}, reviews {r}")
