#!/usr/bin/env python3
"""Replay benchmark: score a review report for RECALL against a past round's confirmed findings.

Stdlib only. Every population arrives as an argument; nothing here names a path outside this kit.

    python3 review_replay.py --known <record> --candidate <report> [--window N]
    python3 review_replay.py --corpus <dir> [<dir> ...] [--repo <clone>]
    python3 review_replay.py --selftest

THE KNOWN SET is a past diff-review record's ADJUDICATED ITEMS, not its raw confirmed findings: a
record lists items, each naming the raw ids it merged, and the raw text never reached it. A record
carrying the appendix the harness now writes (`## Appendix — every finding`) is read from that
appendix; any other is read from its legacy item table. Either way the record's own stated
confirmed count must be REPRODUCED from what was extracted, or the record is refused — a parser
that returns some of a population must not read as success.

THE CANDIDATE is the appendix of a report written by the harness. Columns are found by header
name, only `confirmed` rows count, and their number must equal the report's stated confirmed count.

THE SCORE matches a known item when any candidate is in the same file within `--window` lines
(default 10). Two paths name one file when equal, or when one ends with `/` plus the other — that
admits the basename-only refs older records carry, at a known ceiling: two files sharing a
basename can match. Upgrade, if a scored run ever shows the collision: require the longer path on
both sides.

WHAT THE SCORE DOES NOT MEAN. Recall is against what ONE past review proved real, not against every
defect in the range. A candidate-only finding may be a real defect the past review missed, so it is
listed and never counted as a false positive: there is no precision figure here. The tool decides
nothing — a scored run exits 0 at any recall.

Exit: 0 scored run or listed corpus · 1 red self-test · 2 any refusal or argument error.
"""

import argparse
import contextlib
import io
import pathlib
import re
import subprocess
import sys

APPENDIX_HEADING = "## Appendix — every finding"
SERVES_PREFIX = "**Serves:** diff-review"
CELL_SPLIT = re.compile(r"(?<!\\)\|")
BACKTICKED = re.compile(r"`([^`]+)`")
LINE_REF = re.compile(r"([^\s:]*[./][^\s:]*):(\d+)")
RANGE = re.compile(r"\b([0-9a-fA-F]{7,40})\.\.\.?([0-9a-fA-F]{7,40})\b")
STATED = re.compile(r"\bconfirmed\W{0,6}(\d+)", re.IGNORECASE)
ITEM_ID = re.compile(r"[A-Za-z]{0,3}\d+(?:-\d+)?")
SEVERITY = re.compile(r"\**(?:blocker|high|medium|low)\**", re.IGNORECASE)
RAW_IDS = re.compile(r"\d+(?:\s*,\s*\d+)*")
ROUND_LINE = re.compile(r"\bRound:\W{0,4}(\d+)")
ROUND_FILE = re.compile(r"round(\d+)\.md$", re.IGNORECASE)
#: The arm count `--selftest` must reach. An arm stranded past an early exit is the one defect a
#: per-arm verdict cannot see, so the runner compares what ran against this.
ARMS_DECLARED = 14


def extract_line_ref(text):
    """`(path, line)` from a ref like `a/b.py:12` or `b.py:12-20`, else None."""
    if text is None:
        return None
    s = text.strip().strip("`").replace("\\", "/")
    while s.startswith("./"):
        s = s[2:]
    m = LINE_REF.match(s)
    return (m.group(1), int(m.group(2))) if m else None


def extract_range(text):
    """`(base, head)` from the first hex..hex or hex...hex token; a symbolic end matches nothing."""
    m = RANGE.search(text)
    return (m.group(1).lower(), m.group(2).lower()) if m else None


def extract_stated_count(text):
    """The first number after the word `confirmed`, read from the prose before any appendix."""
    m = STATED.search(text.split(APPENDIX_HEADING, 1)[0])
    return int(m.group(1)) if m else None


def parse_appendix_rows(text):
    """The appendix's CONFIRMED rows as dicts keyed by header name, and an error or None.

    Refused: no appendix, a missing column, or a confirmed-row count differing from the stated one.
    Cell encoding inverted: `\\|` is a literal bar, and a cell reading `-` is an absent value.
    """
    lines = text.splitlines()
    starts = [i for i, line in enumerate(lines) if line.strip() == APPENDIX_HEADING]
    if not starts:
        return None, "no-appendix: no `" + APPENDIX_HEADING + "` heading"
    table = []
    for line in lines[starts[0] + 1:]:
        if line.strip().startswith("|"):
            table.append([c.strip().replace("\\|", "|") for c in CELL_SPLIT.split(line.strip())[1:-1]])
        elif table:
            break
    if len(table) < 2:
        return None, "no-appendix: the heading carries no table"
    header = table[0]
    for col in ("id", "lens", "ref", "verdict"):
        if col not in header:
            return None, f"malformed: the appendix has no `{col}` column"
    rows = [{h: (None if c == "-" else c) for h, c in zip(header, cells)} for cells in table[2:]]
    confirmed = [r for r in rows if r.get("verdict") == "confirmed"]
    stated = extract_stated_count(text)
    if stated is None:
        return None, "no-count: no stated confirmed count"
    if len(confirmed) != stated:
        return None, f"liveness: {len(confirmed)} confirmed appendix row(s) against a stated confirmed count of {stated}"
    return confirmed, None


def parse_record_findings(text):
    """A past diff-review record's known set: `({items, range, stated}, None)` or `(None, error)`.

    Each item is `{id, path, line}`, path and line None when the item is UNSCORABLE.
    """
    rng = extract_range(text)
    if APPENDIX_HEADING in text:
        rows, err = parse_appendix_rows(text)
        if err:
            return None, err
        stated = len(rows)
        items = []
        for r in rows:
            loc = extract_line_ref(r.get("ref"))
            items.append({"id": r.get("id") or "?", "path": loc and loc[0], "line": loc and loc[1]})
    else:
        stated = extract_stated_count(text)
        if stated is None:
            return None, "no-count: no stated confirmed count"
        items, raw = [], set()
        for line in text.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in CELL_SPLIT.split(line.strip())[1:-1]]
            if (len(cells) < 3 or not ITEM_ID.fullmatch(cells[0]) or not SEVERITY.fullmatch(cells[1])
                    or not RAW_IDS.fullmatch(cells[-1])):
                continue
            raw.update(int(n) for n in re.findall(r"\d+", cells[-1]))
            loc = next((ref for ref in map(extract_line_ref, BACKTICKED.findall(line)) if ref), None)
            items.append({"id": cells[0], "path": loc and loc[0], "line": loc and loc[1]})
        if len(raw) != stated:
            return None, f"liveness: the item rows' raw ids union to {len(raw)} against a stated confirmed count of {stated}"
    if not any(i["path"] for i in items):
        return None, f"no-scorable: {len(items)} item(s), none with a file-and-line location"
    if rng is None:
        return None, "no-range: no hex..hex range token"
    return {"items": items, "range": rng, "stated": stated}, None


def check_same_file(a, b):
    """Equal, or one ends with `/` plus the other (the basename ceiling in the module docstring)."""
    return a == b or a.endswith("/" + b) or b.endswith("/" + a)


def measure_recall(items, candidates, window):
    """Match every scorable known item against the candidates; returns the score as a dict."""
    scorable = [it for it in items if it["path"]]
    pairs = [(i, j) for i, it in enumerate(scorable) for j, c in enumerate(candidates)
             if c["path"] and check_same_file(it["path"], c["path"]) and abs(it["line"] - c["line"]) <= window]
    first_hit = {}
    for i, j in pairs:
        first_hit.setdefault(i, j)
    hit_candidates = {j for _, j in pairs}
    lenses = {}
    for j, c in enumerate(candidates):
        tally = lenses.setdefault(c["lens"] or "-", [0, 0])
        tally[0] += 1
        tally[1] += j in hit_candidates
    return {
        "matched": [(scorable[i], candidates[j]) for i, j in sorted(first_hit.items())],
        "missed": [it for i, it in enumerate(scorable) if i not in first_hit],
        "unscorable": [it for it in items if not it["path"]],
        "candidate_only": [c for j, c in enumerate(candidates) if j not in hit_candidates],
        "lenses": lenses,
        "scorable": len(scorable),
    }


def print_score(known_path, known, candidate_path, candidates, window, score):
    base, head = known["range"]
    print(f"replay: known {known_path} · range {base}..{head} · items {len(known['items'])} · "
          f"scorable {score['scorable']} · unscorable {len(score['unscorable'])}")
    print(f"replay: candidate {candidate_path} · confirmed {len(candidates)} · window {window}")
    for it, c in score["matched"]:
        print(f"MATCHED         {it['path']}:{it['line']}  <-  {c['ref']}  [{c['lens']}]")
    for it in score["missed"]:
        print(f"MISSED          {it['path']}:{it['line']}  {it['id']}")
    for it in score["unscorable"]:
        print(f"UNSCORABLE      {it['id']}")
    for c in score["candidate_only"]:
        print(f"CANDIDATE-ONLY  {c['ref']}  [{c['lens']}]")
    print("per-lens: " + " · ".join(f"{lens} confirmed {t[0]} matched {t[1]}" for lens, t in sorted(score["lenses"].items())))
    k, m = len(score["matched"]), score["scorable"]
    print(f"replay: recall {k}/{m} = {k / m:.2f}")


def resolve_commits(shas, repo):
    """The subset of `shas` naming a commit in `repo` — ONE `git cat-file --batch-check` for all.

    A spawn per record costs minutes over a few hundred records on a slow-spawn host. stderr is
    not captured, so a `GIT_TRACE` shows the one process.
    """
    shas = list(dict.fromkeys(shas))
    if not shas:
        return set()
    proc = subprocess.run(["git", "-C", repo, "cat-file", "--batch-check"], input="".join(s + "\n" for s in shas),
                          stdout=subprocess.PIPE, encoding="utf-8", check=False)
    out = proc.stdout.splitlines()
    if proc.returncode or len(out) != len(shas):
        # A dead probe, not a corpus of unresolvable ranges: refuse rather than list nothing.
        raise OSError(f"git cat-file --batch-check in {repo} exited {proc.returncode} with {len(out)} of {len(shas)} lines")
    return {s for s, line in zip(shas, out) if line.split()[1:2] == ["commit"]}


def scan_corpus(dirs, repo):
    """Every diff-review record under `dirs`: `(listed, refused, scanned)`."""
    pending, refused, scanned = [], {}, 0
    for path in sorted(p for d in dirs for p in pathlib.Path(d).rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        first = next((line.strip() for line in text.splitlines() if line.strip()), "")
        if not first.startswith(SERVES_PREFIX):
            continue
        scanned += 1
        known, err = parse_record_findings(text)
        if err:
            reason = err.split(":", 1)[0]
            refused[reason] = refused.get(reason, 0) + 1
            continue
        m = ROUND_LINE.search(text) or ROUND_FILE.search(path.name)
        pending.append((path.as_posix(), m.group(1) if m else "?", known))
    resolved = resolve_commits([s for _, _, k in pending for s in k["range"]], repo)
    listed = []
    for path, rnd, known in pending:
        if set(known["range"]) <= resolved:
            listed.append((path, rnd, known))
        else:
            refused["unresolved-range"] = refused.get("unresolved-range", 0) + 1
    return listed, refused, scanned


def print_corpus(listed, refused, scanned):
    for path, rnd, known in listed:
        base, head = known["range"]
        print(f"{path} · round {rnd} · {base}..{head} · scorable {sum(1 for i in known['items'] if i['path'])}")
    tail = "".join(f" · refused {reason} {n}" for reason, n in sorted(refused.items()))
    print(f"corpus: scanned {scanned} · listed {len(listed)}{tail}")


# ---- self-test fixtures: inline, no file or git access. No path here leaves a fixture namespace.
LEGACY = """**Serves:** diff-review X-1

**Range reviewed: `1234567...89abcde`** · Raw 5, confirmed {stated}, refuted 2

| # | Sev | Where | What | Raw ids |
|---|---|---|---|---|
| F1 | **BLOCKER** | `src/a.sh:10` | the claim, quoting `spec/s.md:4` | 1, 2 |
| M1 | medium | `lib/b.py:40` | the claim | 3 |
| B1 | BLOCKER | 8 | §2 S6, §6 AC6 | the claim |
{extra}"""

APPENDIX = """Review shape: raw 3, confirmed {stated}, refuted 1. Range `1234567..89abcde`.

## Appendix — every finding

| verdict | ref | reason | id | lens |
|---|---|---|---|---|
{rows}

## After
"""

CANDIDATE_ROWS = ("| confirmed | src/a.sh:14 | real \\| reached | 1 | correctness |\n"
                  "| refuted | lib/b.py:40 | not reachable | 2 | security |\n"
                  "| confirmed | lib/c.py:7 | real | 3 | security |")


def run_selftest():
    legacy3 = LEGACY.format(stated=3, extra="")
    cand_rows, _ = parse_appendix_rows(APPENDIX.format(stated=2, rows=CANDIDATE_ROWS))
    candidates = [{"lens": r["lens"], "ref": r["ref"], "path": (extract_line_ref(r["ref"]) or (None, None))[0],
                   "line": (extract_line_ref(r["ref"]) or (None, None))[1]} for r in cand_rows or []]
    known3, _ = parse_record_findings(legacy3)
    score = measure_recall(known3["items"], candidates, 10) if known3 else None
    printed = io.StringIO()
    if score:
        with contextlib.redirect_stdout(printed):
            print_score("k.md", known3, "c.md", candidates, 10, score)
    edge = [{"id": "E", "path": "src/e.py", "line": 20}]
    arms = [
        ("known-legacy-parse", lambda: None if known3 and [i["id"] for i in known3["items"]] == ["F1", "M1"]
            and known3["items"][0]["path"] == "src/a.sh" else f"got {known3!r}"),
        ("known-liveness-refuses", lambda: (lambda r: None if r[0] is None and r[1] and "3" in r[1] and "4" in r[1]
            else f"not refused with both numbers: {r!r}")(parse_record_findings(LEGACY.format(stated=4, extra="")))),
        ("known-non-item-row", lambda: None if known3 and "B1" not in [i["id"] for i in known3["items"]]
            else "the prose-tailed row was read as an item"),
        ("known-unscorable", lambda: (lambda r: None if r[0] and len(r[0]["items"]) == 3
            and measure_recall(r[0]["items"], [], 10)["scorable"] == 2
            and len(measure_recall(r[0]["items"], [], 10)["unscorable"]) == 1 else f"got {r!r}")(
            parse_record_findings(LEGACY.format(stated=4, extra="| L1 | low | prose, no location | 4 |")))),
        ("known-range", lambda: None if extract_range("a 1234567..89abcde b") == ("1234567", "89abcde")
            and extract_range("x 1234567...89abcdef y") == ("1234567", "89abcdef")
            and extract_range("abc1234..HEAD") is None
            and (parse_record_findings(legacy3.replace("1234567...89abcde", "1234567..HEAD"))[1] or "").startswith("no-range")
            else "a range form was misread"),
        ("appendix-by-header", lambda: None if cand_rows and cand_rows[0]["ref"] == "src/a.sh:14"
            and cand_rows[0]["lens"] == "correctness" and cand_rows[1]["id"] == "3" else f"got {cand_rows!r}"),
        ("appendix-cell-encoding", lambda: (lambda r: None if cand_rows and cand_rows[0]["reason"] == "real | reached"
            and r[0] and r[0]["items"][1]["path"] is None else f"escaped bar split, or `-` read as a ref: {r!r}")(
            parse_record_findings(APPENDIX.format(stated=2, rows="| confirmed | src/a.sh:1 | x | 1 | l |\n| confirmed | - | y | 2 | l |")))),
        ("appendix-liveness-refuses", lambda: (lambda r: None if r[0] is None and (r[1] or "").startswith("liveness")
            else f"not refused: {r!r}")(parse_appendix_rows(APPENDIX.format(stated=3, rows=CANDIDATE_ROWS)))),
        ("appendix-absent-refuses", lambda: (lambda r: None if r[0] is None and (r[1] or "").startswith("no-appendix")
            else f"not refused: {r!r}")(parse_appendix_rows(legacy3))),
        ("score-miss", lambda: None if score and len(score["matched"]) == 1 and score["scorable"] == 2
            and "replay: recall 1/2 = 0.50" in printed.getvalue() and "MISSED          lib/b.py:40  M1" in printed.getvalue()
            else f"got {printed.getvalue()!r}"),
        ("score-refuted-ignored", lambda: None if score and [it["id"] for it in score["missed"]] == ["M1"]
            else "a refuted row at a known location matched it"),
        ("window-edge", lambda: None if measure_recall(edge, [{"lens": "l", "ref": "r", "path": "src/e.py", "line": 30}], 10)["matched"]
            and not measure_recall(edge, [{"lens": "l", "ref": "r", "path": "src/e.py", "line": 31}], 10)["matched"]
            else "the window edge is off by one"),
        ("path-suffix", lambda: None if check_same_file("pkg/lib/kit.toml", "kit.toml") and check_same_file("kit.toml", "pkg/lib/kit.toml")
            and not check_same_file("a/kit.toml", "b/kit.toml") and not check_same_file("pkg/akit.toml", "kit.toml")
            else "the path-suffix rule is wrong"),
        ("candidate-only", lambda: None if score and [c["ref"] for c in score["candidate_only"]] == ["lib/c.py:7"]
            and "CANDIDATE-ONLY  lib/c.py:7  [security]" in printed.getvalue() else f"got {score!r}"),
    ]
    passed = ran = 0
    for name, arm in arms:
        ran += 1
        try:
            why = arm()
        except Exception as exc:  # an arm that crashes is a red arm, never a dead runner
            why = f"raised {exc!r}"
        print(f"ok {name}" if why is None else f"FAIL {name}: {why}")
        passed += why is None
    print(f"selftest: {passed}/{ARMS_DECLARED} arms")
    if ran != ARMS_DECLARED:
        print(f"FAIL selftest: {ran} arm(s) ran against {ARMS_DECLARED} declared")
    return 0 if passed == ran == ARMS_DECLARED else 1


def main(argv):
    ap = argparse.ArgumentParser(prog="review_replay.py", description="Score a review report for recall against a past round.")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--known", metavar="RECORD")
    ap.add_argument("--candidate", metavar="REPORT")
    ap.add_argument("--corpus", nargs="+", metavar="DIR")
    ap.add_argument("--window", type=int, default=10)
    ap.add_argument("--repo", default=".")
    args = ap.parse_args(argv)
    if args.selftest:
        return run_selftest()
    if args.window < 0:
        ap.error("--window must be 0 or more")
    if args.corpus:
        missing = [d for d in args.corpus if not pathlib.Path(d).is_dir()]
        if missing:
            ap.error("not a directory: " + ", ".join(missing))
        try:
            listed, refused, scanned = scan_corpus(args.corpus, args.repo)
        except OSError as exc:
            print(f"replay: REFUSED — {exc}", file=sys.stderr)
            return 2
        if scanned == 0:
            # A scan that saw nothing must not read as a corpus with nothing replayable.
            print("replay: REFUSED — no diff-review record under " + ", ".join(args.corpus), file=sys.stderr)
            return 2
        print_corpus(listed, refused, scanned)
        return 0
    if not (args.known and args.candidate):
        ap.error("give --known and --candidate, or --corpus, or --selftest")
    try:
        known_text = pathlib.Path(args.known).read_text(encoding="utf-8")
        cand_text = pathlib.Path(args.candidate).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"replay: REFUSED — {exc}", file=sys.stderr)
        return 2
    known, err = parse_record_findings(known_text)
    if err:
        print(f"replay: REFUSED known {args.known} — {err}", file=sys.stderr)
        return 2
    rows, err = parse_appendix_rows(cand_text)
    if err:
        print(f"replay: REFUSED candidate {args.candidate} — {err}", file=sys.stderr)
        return 2
    candidates = []
    for r in rows:
        loc = extract_line_ref(r.get("ref"))
        candidates.append({"lens": r.get("lens"), "ref": r.get("ref") or "-", "path": loc and loc[0], "line": loc and loc[1]})
    print_score(args.known, known, args.candidate, candidates, args.window, measure_recall(known["items"], candidates, args.window))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
