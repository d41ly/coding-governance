#!/usr/bin/env python3
"""review_dispose.py — `review.left-shift`'s count: which of a review's classes earn a gate (TOOL-dDeclaredLoop-20).

    python <prefix>/workflows/review_dispose.py classes --builds <memory root>/builds --record <report>
                                                         --left-shift second-occurrence|every-class|owner-selects

`measure_class_occurrences` reads every `*/reviews/*.md` under `--builds` through `replay_scorer.py`'s
`parse_appendix_rows`, the appendix reader beside this file, and counts each `class:<slug>` of the
confirmed rows' disposition column once per distinct review (TOOL-dDeclaredLoop-56 S41): a record's
review is its file stem less a leading `<date>-review-` and a trailing `-round<n>`, a stem of no such
shape its own review, and every record of `--record`'s own review is skipped, so a review's earlier
round is never a prior occurrence. It answers one line per slug of `--record` that earns a gate under
the `review.left-shift` value:

    review-dispose: gate <slug> · prior <n> · <value>[ · owner]

`second-occurrence`, the default, earns a `class:` slug some prior record already disposed (a prior
count of 1 or more); `every-class` earns every `class:` and `new:` slug; `owner-selects` names every
`class:` and `new:` slug, each marked `owner`, an owner item rather than a gate. A prior record the
parser refuses counts nothing and prints `review-dispose: skipped <path> · <why>`.

Exit 0 answered, any number of gates · 2 `--record` unreadable or refused by the parser, or an
argument error.

WHAT IT DOES NOT CHECK: that a record is named by the hygiene guide's grammar, so a misnamed round counts
as its own review; that a slug names a real class; or that a gate was filed. The DISPOSAL stage files each earned
gate as an ask; this module only counts.
"""
import argparse
import pathlib
import re
import sys

sys.dont_write_bytecode = True
import replay_scorer  # noqa: E402  the appendix reader, beside this file

SAY = "review-dispose"
LEFT_SHIFTS = ("second-occurrence", "every-class", "owner-selects")
#: A record's review (TOOL-dDeclaredLoop-56 S41): its file stem less a leading `<date>-review-` and a
#: trailing `-round<n>`, each where present, so every round of one review is one review.
REVIEW_STEM = re.compile(r"(?:\d{4}-\d\d-\d\d-review-)?(.+?)(?:-round\d+)?")


def read_record_slugs(text):
    """-> ([(form, slug)] of the confirmed rows' `class:` and `new:` dispositions, error or None)."""
    rows, err = replay_scorer.parse_appendix_rows(text)
    if err:
        return None, err
    out = []
    for r in rows:
        cell = (r.get("disposition") or "").strip()
        form, _, slug = cell.partition(":")
        if form in ("class", "new") and slug:
            out.append((form, slug.split()[0]))
    return out, None


def measure_class_occurrences(builds, record, value):
    """-> (gate lines, skipped lines); ValueError naming `record` where the parser refuses it."""
    record = pathlib.Path(record).resolve()
    try:
        mine, err = read_record_slugs(record.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError) as e:
        mine, err = None, str(e)
    if err:
        raise ValueError("%s: refused · %s · %s" % (SAY, record.as_posix(), err))
    own = REVIEW_STEM.fullmatch(record.stem).group(1)
    prior, skipped = {}, []
    for path in sorted(pathlib.Path(builds).glob("*/reviews/*.md")):
        review = REVIEW_STEM.fullmatch(path.stem).group(1)
        if path.resolve() == record or review == own:
            continue
        try:
            got, why = read_record_slugs(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError) as e:
            got, why = None, str(e)
        if why:
            skipped.append("%s: skipped %s · %s" % (SAY, path.as_posix(), why))
            continue
        for form, slug in got:
            if form == "class":
                prior.setdefault(slug, set()).add(review)
    gates, seen = [], set()
    for form, slug in mine:
        if slug in seen:
            continue
        seen.add(slug)
        n = len(prior.get(slug, ()))
        if value == "second-occurrence" and not (form == "class" and n >= 1):
            continue
        gates.append("%s: gate %s · prior %d · %s%s" % (SAY, slug, n, value, " · owner" if value == "owner-selects" else ""))
    return gates, skipped


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="review_dispose.py")
    ap.add_argument("verb", choices=["classes"])
    ap.add_argument("--builds", required=True)
    ap.add_argument("--record", required=True)
    ap.add_argument("--left-shift", choices=LEFT_SHIFTS, default="second-occurrence")
    a = ap.parse_args(argv)
    try:
        gates, skipped = measure_class_occurrences(a.builds, a.record, a.left_shift)
    except ValueError as e:
        print(str(e))
        return 2
    for line in skipped + gates:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
