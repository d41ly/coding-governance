#!/usr/bin/env python3
"""Replay benchmark: score a review report for RECALL against a past round's confirmed findings.

Stdlib only. Every population arrives as an argument; nothing here names a path outside this kit.

    python3 review_replay.py --known <record> --candidate <report> [--window N]
    python3 review_replay.py --corpus <dir> [<dir> ...] [--repo <clone>]
    python3 review_replay.py --selftest

THE KNOWN SET is a past diff-review record's confirmed findings, in one of TWO units, and the
`replay: known` line prints which. A record carrying the appendix the harness now writes
(`## Appendix — every finding`) is read from that appendix, one known entry per RAW confirmed
finding: the appendix has a row per raw finding, so a defect two lenses confirmed counts twice. Any
other record is read from its legacy item table, one entry per ADJUDICATED ITEM, because a legacy
record lists items naming the raw ids they merged and the raw locations never reached it. Recall
from the two eras is therefore in different units. Either way the record's own stated confirmed
count must be REPRODUCED from what was extracted, or the record is refused — a parser that returns
some of a population must not read as success.

THE CANDIDATE is the appendix of a report written by the harness. Columns are found by header
name, only `confirmed` rows count, and their number must equal the report's stated confirmed count.
A confirmed row whose ref names no file and line is UNSCORABLE and counted; when confirmed rows
exist and none is scorable, the report is refused rather than scored as a recall of zero.
A table row ends at a newline only, never at another character `str.splitlines` breaks on.

THE SCORE matches a known item when any candidate is in the same file within `--window` lines
(default 10). Two paths name one file when equal, or when one ends with `/` plus the other — that
admits the basename-only refs older records carry, at a known ceiling: two files sharing a
basename can match. Upgrade, if a scored run ever shows the collision: require the longer path on
both sides.

When the known set came from an appendix, a `per-lens known:` line follows the candidate-side
`per-lens:` line, giving each known-side lens its confirmed count and how many a candidate matched.

SPEC MODE. A known record whose first non-blank line is the `**Serves:** spec-audit` binding is read
from its appendix ONLY: with none it is refused `no-appendix`, never scored as zero, and there is no
legacy fallback, because no spec-audit record carries the legacy table's raw-id column. A spec ref is
`<file>:<where>`, split at the first `:` after the path (a drive prefix handled as above). The
SECTION is the first `§<n>` or `section <n>`, case ignored; failing both, the first `S<n>`, `AC<n>`
or `F<n>` reads as §2, §6 or §8, where the spec format puts those items. An address naming none is
UNSCORABLE. A match is the same file and the same section: the window is forced to 0, `--window` is
ignored, and the candidate line prints `address section`. The known line names the kind and the
subject pins — every `<path>@<hex>` after the binding line and before the first `## ` heading — or
`subjects none-stated`; no range is read or required. A candidate opening with the OTHER kind's
binding is refused `kind-mismatch`, naming both; an unbound one is read in the known record's mode.
Spec records are not listed by `--corpus`.

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
SPEC_SERVES_PREFIX = "**Serves:** spec-audit"
SECTION_REF = re.compile(r"(?:§|\bsection\s+)\s*(\d+)", re.IGNORECASE)
ITEM_SECTION = re.compile(r"\b(S|AC|F)(\d+)\b")
#: The spec format's section for each item kind: scope §2, acceptance §6, open questions §8.
ITEM_SECTIONS = {"S": 2, "AC": 6, "F": 8}
SUBJECT_PIN = re.compile(r"([^\s`@,()]+)@([0-9a-fA-F]{7,40})\b")
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
ARMS_DECLARED = 25


def extract_line_ref(text):
    """`(path, line)` from a ref like `a/b.py:12`, `b.py:12-20` or `C:\\x\\b.py:12`, else None."""
    if text is None:
        return None
    s = text.strip().strip("`").replace("\\", "/")
    # A drive prefix keeps its absolute suffix, which check_same_file's endswith rule then matches.
    s = re.sub(r"^[A-Za-z]:/", "/", s)
    while s.startswith("./"):
        s = s[2:]
    m = LINE_REF.match(s)
    return (m.group(1), int(m.group(2))) if m else None


def extract_section_ref(text):
    """`(path, section)` from a spec ref like `x.md:§2 S5` or `C:/r/x.md:section 4`, else None."""
    if text is None:
        return None
    s = text.strip().strip("`").replace("\\", "/")
    s = re.sub(r"^[A-Za-z]:/", "/", s)
    while s.startswith("./"):
        s = s[2:]
    path, sep, where = s.partition(":")
    if not (sep and path):
        return None
    m = SECTION_REF.search(where)
    if m:
        return path, int(m.group(1))
    m = ITEM_SECTION.search(where)
    return (path, ITEM_SECTIONS[m.group(1)]) if m else None


def read_record_kind(text):
    """`spec-audit` or `diff-review` from the first non-blank line's `**Serves:**` binding, else None."""
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    for prefix in (SPEC_SERVES_PREFIX, SERVES_PREFIX):
        if first.startswith(prefix):
            return prefix.split()[-1]
    return None


def extract_subject_pins(text):
    """Every `(path, hex)` pin AFTER the binding line and before the first `## `, one line or one per bullet."""
    lines = text.replace("\r\n", "\n").split("\n")
    start = next((i for i, line in enumerate(lines) if line.strip()), len(lines))
    pins = []
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        pins += SUBJECT_PIN.findall(line)
    return pins


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
    Rows split on a newline ONLY: `splitlines` also breaks on U+2028, `\\x85` and others a cell may
    carry, and one cut row ends the table and drops every row after it.
    """
    lines = text.replace("\r\n", "\n").split("\n")
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


def parse_record_findings(text, mode="diff-review"):
    """A past record's known set: `({items, range, stated, unit, subjects}, None)` or `(None, error)`.

    Each item is `{id, path, line}`, path and line None when the item is UNSCORABLE; in `spec-audit`
    mode `line` holds the SECTION. `unit` names what one item is: `raw-finding` from an appendix,
    `adjudicated-item` from a legacy table. An appendix item also carries its `lens`.
    """
    spec = mode == "spec-audit"
    read_ref = extract_section_ref if spec else extract_line_ref
    rng = None if spec else extract_range(text)
    # Spec mode has no legacy fallback: a missing appendix is refused by parse_appendix_rows.
    if spec or APPENDIX_HEADING in text:
        unit = "raw-finding"
        rows, err = parse_appendix_rows(text)
        if err:
            return None, err
        stated = len(rows)
        items = []
        for r in rows:
            loc = read_ref(r.get("ref"))
            items.append({"id": r.get("id") or "?", "lens": r.get("lens") or "-", "path": loc and loc[0], "line": loc and loc[1]})
    else:
        unit = "adjudicated-item"
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
    where = "section" if spec else "line"
    if not any(i["path"] for i in items):
        return None, f"no-scorable: {len(items)} item(s), none with a file-and-{where} location"
    if rng is None and not spec:
        return None, "no-range: no hex..hex range token"
    return {"items": items, "range": rng, "stated": stated, "unit": unit,
            "subjects": extract_subject_pins(text) if spec else None}, None


def parse_candidates(text, mode="diff-review"):
    """A report's confirmed appendix rows as candidates `{lens, ref, path, line}`: `(list, None)` or `(None, error)`.

    The ONE row-to-candidate mapping, called by `main` and the self-test alike. Refused when confirmed
    rows exist and none names a file and line (a section, in `spec-audit` mode): a ref shape the
    parser cannot read would otherwise score every candidate as a miss and print a recall of zero at
    exit 0. Refused `kind-mismatch` when the report opens with the OTHER kind's binding.
    """
    kind = read_record_kind(text)
    if kind and kind != mode:
        return None, f"kind-mismatch: the known record is {mode} and the candidate opens with the {kind} binding"
    rows, err = parse_appendix_rows(text)
    if err:
        return None, err
    spec = mode == "spec-audit"
    read_ref = extract_section_ref if spec else extract_line_ref
    candidates = []
    for r in rows:
        loc = read_ref(r.get("ref"))
        candidates.append({"lens": r.get("lens"), "ref": r.get("ref") or "-", "path": loc and loc[0], "line": loc and loc[1]})
    if candidates and not any(c["path"] for c in candidates):
        return None, f"no-scorable: {len(candidates)} confirmed row(s), none with a file-and-{'section' if spec else 'line'} ref"
    return candidates, None


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


def measure_replay(known_text, cand_text, window):
    """Two texts to a score: `({mode, known, candidates, window, score}, None)` or `(None, (side, error))`.

    The ONE known-to-score path, called by `main` and the self-test alike. The mode is the known
    record's binding, `diff-review` when it states none; `spec-audit` forces the window to 0, so a
    match is the same file and the same section whatever `--window` said. `side` is `known` or
    `candidate`.
    """
    mode = read_record_kind(known_text) or "diff-review"
    known, err = parse_record_findings(known_text, mode)
    if err:
        return None, ("known", err)
    candidates, err = parse_candidates(cand_text, mode)
    if err:
        return None, ("candidate", err)
    if mode == "spec-audit":
        window = 0
    return {"mode": mode, "known": known, "candidates": candidates, "window": window,
            "score": measure_recall(known["items"], candidates, window)}, None


def print_score(known_path, known, candidate_path, candidates, window, score, mode="diff-review"):
    if mode == "spec-audit":
        pins = ", ".join(f"{p}@{h}" for p, h in known["subjects"]) or "none-stated"
        where, reach, sep = f"kind spec-audit · unit {known['unit']} · subjects {pins}", "address section", ":§"
    else:
        base, head = known["range"]
        where, reach, sep = f"unit {known['unit']} · range {base}..{head}", f"window {window}", ":"
    print(f"replay: known {known_path} · {where} · items {len(known['items'])} · "
          f"scorable {score['scorable']} · unscorable {len(score['unscorable'])}")
    print(f"replay: candidate {candidate_path} · confirmed {len(candidates)} · "
          f"unscorable {sum(1 for c in candidates if not c['path'])} · {reach}")
    for it, c in score["matched"]:
        print(f"MATCHED         {it['path']}{sep}{it['line']}  <-  {c['ref']}  [{c['lens']}]")
    for it in score["missed"]:
        print(f"MISSED          {it['path']}{sep}{it['line']}  {it['id']}")
    for it in score["unscorable"]:
        print(f"UNSCORABLE      {it['id']}")
    for c in score["candidate_only"]:
        print(f"CANDIDATE-ONLY  {c['ref']}  [{c['lens']}]")
    print("per-lens: " + " · ".join(f"{lens} confirmed {t[0]} matched {t[1]}" for lens, t in sorted(score["lenses"].items())))
    if known["unit"] == "raw-finding":
        known_lenses = {}
        for it in known["items"]:
            known_lenses.setdefault(it["lens"], [0, 0])[0] += 1
        for it, _ in score["matched"]:
            known_lenses[it["lens"]][1] += 1
        print("per-lens known: " + " · ".join(f"{lens} confirmed {t[0]} matched {t[1]}" for lens, t in sorted(known_lenses.items())))
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
        except (OSError, UnicodeDecodeError) as exc:
            # Not classifiable, so outside `scanned` — but named, never skipped in silence.
            print(f"replay: unreadable, not scanned: {path.as_posix()} ({exc})", file=sys.stderr)
            continue
        if read_record_kind(text) != "diff-review":
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
| M1 | medium | `mod/b.py:40` | the claim | 3 |
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
                  "| refuted | mod/b.py:40 | not reachable | 2 | security |\n"
                  "| confirmed | mod/c.py:7 | real | 3 | security |")

SPEC_RECORD = """{binding}

# x — spec audit, round 1

{pins}

Review shape: raw 4, confirmed {stated}, refuted 1.

## Verdict: CLEAN WITH FIXES

## Appendix — every finding

| id | lens | ref | verdict |
|---|---|---|---|
{rows}
"""

# The head of reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md in the
# aEvidencedLens build, copied: the binding line first, then one pin per bullet under the round line.
ROUND1_PINS = "**Round: 1.** Range reviewed: the eleven subjects below, each pinned at the blob it was read at, plus the tree they cite.\n\n" + "\n".join(
    f"- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-{n}.md@{blob}`" for n, blob in (
        (1, "de140c3ea4acd5571eb7ee42f9cf4ebbb669e34c"), (2, "1ea5a3a513b452f2072c8ab8825d2ba371e8c87e"),
        (3, "075af74ddcb7603efee1e08d2eb2cbb5955616f9"), (4, "099033058fe14bfe3407d038ddd4efaf0af34895"),
        (6, "3f4fafd20ffdec3b119b9f4ab319f51e654717e0"), (10, "88b6a0f1477ab70a89d33b09b05cf89c824a9b66"),
        (5, "6d1c0773338495d741eccfa96cb18b2573507948"), (7, "7d4dce07d8899d54bfff2a1e1515aa297b090950"),
        (9, "9e4e4704eaa6dd5ea1795bcce1019ac1ea03e28a"), (8, "629cc42227ce6bb803160f25f74a9ce1fc3db2c4"),
        (11, "69275b8ac283e870a83a368db20a8222fa0263fc")))
ROUND1_BINDING = "**Serves:** spec-audit " + " ".join(f"TOOL-aEvidencedLens-{n}" for n in range(1, 12))


def run_selftest():
    legacy3 = LEGACY.format(stated=3, extra="")
    cand_rows, _ = parse_appendix_rows(APPENDIX.format(stated=2, rows=CANDIDATE_ROWS))
    candidates = parse_candidates(APPENDIX.format(stated=2, rows=CANDIDATE_ROWS))[0] or []
    known3, _ = parse_record_findings(legacy3)
    score = measure_recall(known3["items"], candidates, 10) if known3 else None
    printed = io.StringIO()
    if score:
        with contextlib.redirect_stdout(printed):
            print_score("k.md", known3, "c.md", candidates, 10, score)
    edge = [{"id": "E", "path": "src/e.py", "line": 20}]

    def render_score(known, cands):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            print_score("k.md", known, "c.md", cands, 10, measure_recall(known["items"], cands, 10))
        return out.getvalue()

    twin = APPENDIX.format(stated=2, rows="| confirmed | src/a.sh:12 | x | 1 | correctness |\n| confirmed | src/a.sh:12 | y | 2 | seams |")
    drive_cands = APPENDIX.format(stated=2, rows="| confirmed | C:/projects/x/src/a.sh:12 | x | 1 | l |\n| confirmed | D:\\w\\mod\\c.py:7 | y | 2 | l |")
    none_scorable = APPENDIX.format(stated=2, rows="| confirmed | - | x | 1 | l |\n| confirmed | x.js:undefined | y | 2 | l |")
    one_scorable = APPENDIX.format(stated=2, rows="| confirmed | src/a.sh:1 | x | 1 | l |\n| confirmed | x.js:undefined | y | 2 | l |")
    # chr(), never a typed escape: the character itself is the fixture. CRLF pins the normalisation.
    split_cell = APPENDIX.format(stated=2, rows="| confirmed | src/a.sh:1 | a" + chr(0x2028) + "b | 1 | l |\r\n| confirmed | mod/c.py:7 | y | 2 | l |")

    def render_replay(known_text, cand_text):
        """`measure_replay` at `--window 10`, then its printed score: `(replay, refusal, output)`."""
        replay, refusal = measure_replay(known_text, cand_text, 10)
        out = io.StringIO()
        if replay:
            with contextlib.redirect_stdout(out):
                print_score("k.md", replay["known"], "c.md", replay["candidates"], replay["window"], replay["score"], replay["mode"])
        return replay, refusal, out.getvalue()

    def build_spec_record(rows, stated, pins="", binding=SPEC_SERVES_PREFIX + " X-1"):
        return SPEC_RECORD.format(binding=binding, pins=pins, stated=stated, rows=rows)

    spec_known = build_spec_record("| 1 | coherence | x.md:§2 S1 | confirmed |", 1)
    spec_rows2 = "| 1 | coherence | x.md:section 2, S4 | confirmed |\n| 2 | reuse | x.md:§3 | confirmed |"
    spec_cand = build_spec_record(spec_rows2, 2)
    # The same rows with no binding line: the diff fixture's shape, which carries none.
    unbound_cand = APPENDIX.format(stated=2, rows="| confirmed | x.md:section 2, S4 | a | 1 | coherence |\n| confirmed | x.md:§3 | b | 2 | reuse |")
    section_refs = [("x.md:§2 S5", ("x.md", 2)), ("x.md:section 2, S5", ("x.md", 2)), ("x.md:S5", ("x.md", 2)),
                    ("x.md:AC3", ("x.md", 6)), ("x.md:F1", ("x.md", 8)), ("C:/r/x.md:§4 Design", ("/r/x.md", 4)),
                    ("x.md:status header", None)]
    lens_known = build_spec_record("| 1 | coherence | x.md:§2 S1 | confirmed |\n| 2 | coherence | x.md:AC1 | confirmed |\n"
                                   "| 3 | reuse | x.md:§4 | confirmed |", 3)
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
            and "replay: recall 1/2 = 0.50" in printed.getvalue() and "MISSED          mod/b.py:40  M1" in printed.getvalue()
            else f"got {printed.getvalue()!r}"),
        ("score-refuted-ignored", lambda: None if score and [it["id"] for it in score["missed"]] == ["M1"]
            else "a refuted row at a known location matched it"),
        ("window-edge", lambda: None if measure_recall(edge, [{"lens": "l", "ref": "r", "path": "src/e.py", "line": 30}], 10)["matched"]
            and not measure_recall(edge, [{"lens": "l", "ref": "r", "path": "src/e.py", "line": 31}], 10)["matched"]
            else "the window edge is off by one"),
        ("path-suffix", lambda: None if check_same_file("pkg/sub/kit.toml", "kit.toml") and check_same_file("kit.toml", "pkg/sub/kit.toml")
            and not check_same_file("a/kit.toml", "b/kit.toml") and not check_same_file("pkg/akit.toml", "kit.toml")
            else "the path-suffix rule is wrong"),
        ("candidate-only", lambda: None if score and [c["ref"] for c in score["candidate_only"]] == ["mod/c.py:7"]
            and "CANDIDATE-ONLY  mod/c.py:7  [security]" in printed.getvalue() else f"got {score!r}"),
        ("known-unit-raw", lambda: (lambda r: None if r[0] and r[0]["unit"] == "raw-finding" and len(r[0]["items"]) == 2
            and {(i["path"], i["line"]) for i in r[0]["items"]} == {("src/a.sh", 12)}
            and "· unit raw-finding ·" in render_score(r[0], []) and "· unit adjudicated-item ·" in printed.getvalue()
            else f"two raw rows at one location are not two raw-finding entries, or the header hides the unit: {r!r}")(
            parse_record_findings(twin))),
        ("drive-ref-candidate", lambda: (lambda c: None if c and [x["path"] for x in c] == ["/projects/x/src/a.sh", "/w/mod/c.py"]
            and known3 and [it["id"] for it, _ in measure_recall(known3["items"], c, 10)["matched"]] == ["F1"]
            else f"a drive-lettered candidate ref did not score: {c!r}")(parse_candidates(drive_cands)[0])),
        ("drive-ref-known", lambda: (lambda r: None if r[0] and r[0]["items"][0]["path"] == "/projects/x/mod/b.py"
            and measure_recall(r[0]["items"], [{"lens": "l", "ref": "r", "path": "mod/b.py", "line": 40}], 10)["matched"]
            else f"a drive-lettered known ref did not score: {r!r}")(
            parse_record_findings(APPENDIX.format(stated=1, rows="| confirmed | C:/projects/x/mod/b.py:41 | x | 1 | l |")))),
        ("candidate-unscorable-refuses", lambda: (lambda r, mixed: None if r[0] is None and (r[1] or "").startswith("no-scorable")
            and mixed[0] and "· unscorable 1 ·" in render_score(known3, mixed[0]).split("\n")[1]
            else f"got {r!r} and {mixed!r}")(parse_candidates(none_scorable), parse_candidates(one_scorable))),
        ("appendix-u2028-row", lambda: (lambda r: None if r[0] and [x["id"] for x in r[0]] == ["1", "2"] and chr(0x2028) in r[0][0]["reason"]
            else f"a U+2028 in a cell cut the table: {r!r}")(parse_appendix_rows(split_cell))),
        # The legacy fixture under a spec binding: diff mode scores it (known3), so a fallback would too.
        ("no-appendix", lambda: (lambda r: None if r[0] is None and r[1][0] == "known" and r[1][1].startswith("no-appendix")
            else f"a spec record with no appendix was not refused no-appendix: {r[:2]!r}")(
            render_replay(legacy3.replace(SERVES_PREFIX, SPEC_SERVES_PREFIX), spec_cand))),
        ("section-ref", lambda: next((f"{ref!r} read as {extract_section_ref(ref)!r}, not {want!r}"
            for ref, want in section_refs if extract_section_ref(ref) != want), None)),
        ("window-0", lambda: (lambda r: None if r[0] and r[0]["window"] == 0
            and [c["ref"] for _, c in r[0]["score"]["matched"]] == ["x.md:section 2, S4"]
            and [c["ref"] for c in r[0]["score"]["candidate_only"]] == ["x.md:§3"]
            and "· address section" in r[2] and "MATCHED         x.md:§2  <-  x.md:section 2, S4" in r[2]
            else f"a §3 candidate matched a §2 item under --window 10, or the line kept its window: {r!r}")(
            render_replay(spec_known, spec_cand))),
        ("kind-mismatch", lambda: (lambda spec_diff, diff_spec, unbound: None
            if all(r[0] is None and r[1][0] == "candidate" and r[1][1].startswith("kind-mismatch")
                   and "spec-audit" in r[1][1] and "diff-review" in r[1][1] for r in (spec_diff, diff_spec))
            and unbound[0] and unbound[0]["mode"] == "spec-audit" and len(unbound[0]["score"]["matched"]) == 1
            else f"got {spec_diff[:2]!r} / {diff_spec[:2]!r} / {unbound[:2]!r}")(
            render_replay(spec_known, SERVES_PREFIX + " X-1\n\n" + unbound_cand),
            render_replay(legacy3, spec_cand), render_replay(spec_known, unbound_cand))),
        ("subject-pins", lambda: (lambda one, bullets, none: None
            if "· kind spec-audit · unit raw-finding · subjects a.md@abc1234, b.md@def5678 ·" in one[2]
            and bullets[0] and len(bullets[0]["known"]["subjects"]) == 11
            and "TOOL-aEvidencedLens-11.md@69275b8ac283e870a83a368db20a8222fa0263fc ·" in bullets[2]
            and "· subjects none-stated ·" in none[2] and "replay: recall 1/1 = 1.00" in none[2] and "range" not in none[2]
            else f"got {one[2]!r} / {bullets[:2]!r} / {none[2]!r}")(
            render_replay(build_spec_record("| 1 | coherence | x.md:§2 S1 | confirmed |", 1, "a.md@abc1234, b.md@def5678",
                                            SPEC_SERVES_PREFIX + " x"), spec_cand),
            render_replay(build_spec_record("| 1 | coherence | x.md:§2 S1 | confirmed |", 1, ROUND1_PINS, ROUND1_BINDING), spec_cand),
            # A pin-shaped token ON the binding line must not be read: the binding line is never the pin line.
            render_replay(build_spec_record("| 1 | coherence | x.md:§2 S1 | confirmed |", 1, "", SPEC_SERVES_PREFIX + " z.md@1234567"),
                          spec_cand))),
        ("per-lens-known", lambda: (lambda spec, raw: None
            if "\nper-lens known: coherence confirmed 2 matched 1 · reuse confirmed 1 matched 0\n" in spec[2]
            and "\nper-lens: coherence confirmed 1 matched 1 · reuse confirmed 1 matched 0\n" in spec[2]
            and "\nper-lens known: correctness confirmed 1 matched 0 · seams confirmed 1 matched 0\n" in raw
            and "\nper-lens: correctness confirmed 1 matched 1 · security confirmed 1 matched 0\n" in printed.getvalue()
            and "per-lens known:" not in printed.getvalue()
            else f"got {spec[2]!r} / {raw!r} / {printed.getvalue()!r}")(
            render_replay(lens_known, spec_cand), render_score(parse_record_findings(twin)[0], []))),
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
    replay, refusal = measure_replay(known_text, cand_text, args.window)
    if refusal:
        side, err = refusal
        print(f"replay: REFUSED {side} {args.known if side == 'known' else args.candidate} — {err}", file=sys.stderr)
        return 2
    print_score(args.known, replay["known"], args.candidate, replay["candidates"], replay["window"], replay["score"], replay["mode"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
