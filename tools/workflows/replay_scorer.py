#!/usr/bin/env python3
"""The replay scorer factory: one deterministic scorer re-deriving every figure from committed raw outputs.

Stdlib only. Every population arrives as an argument; nothing here names a path outside this kit but
the self-test's proof, which reads aScoutedSeam's committed records where the tree holds them.

    python3 replay_scorer.py --instance scouted-seam --cases <src> --results <src> --grade <arm>
    python3 replay_scorer.py --instance scouted-seam --cases <src> --results <src> --compare <arm> <arm> [...]
    python3 replay_scorer.py --instance scouted-seam --cases <src> --results <src> --judged <arm|a+b> [...]
    python3 replay_scorer.py --instance review-replay --known <src> --candidate <src> [--window N]
    python3 replay_scorer.py --experiment <src> [--repo <clone>]
    python3 replay_scorer.py --selftest

A `<src>` resolves in one order: an existing working-tree path; else a 40-hex blob id; else
`<rev>:<path>`, when the part before the first `:` is longer than one character, so `C:/x` is never a
rev. A git object is read by ONE `git cat-file blob` with argv, never a shell; a source opening `-` is
refused, and so is an object git cannot read, never read as an empty arm. Leading `//` lines are
skipped, as aScoutedSeam's `read_json` skips the `**Serves:**` head its records carry.

PAIRING. `derive_paired_cases` is the ONE place variants are paired with cases: the ids every variant
answered, in case order, and each variant's unanswered ids. It refuses an answer naming a case outside
the population, a variant that answered nothing, and an empty pairing, so a partial population is a
refusal and never a smaller score. Each figure line names its population first, `paired <n> of <N> ·
<variant> unanswered <ids>`, then the scores. Output follows the case file's order and the argument
order of the variants, never a set's, so two runs over the same bytes print the same bytes.

THE INSTANCES. `review-replay` is `review_replay.py`'s scoring core, moved here; that file keeps its
CLI, its printer and its corpus listing as the instance's adapter. A spec ref there is read by
`extract_tag_ref`: its first lower-case `[tag]`, else its section. `scouted-seam` is aScoutedSeam's
grader (`check_hit`, `check_case` and the `grade`, `compare` and `judged` readings), ported from the
grader blob a03896116e3c5cbf853affda241c22d8408cb945 at b0fe68f30; a result row without a `seams` list,
or a judged cell without `primary` and `covered`, is a refusal naming the arm and the case.

THE EXPERIMENT SHAPE. `check_experiment` reads one committed JSON manifest (`--experiment <src>`) and
runs every rule of aScoutedSeam's method before the first figure line, a broken one exiting 2 by name:
each case's `case_evidence` hook returns something; a `heldOut` file has exactly one commit and no id
a tuning case carries; an arm with a `base` varies exactly one declared setting from it; every arm's
parsed replies print against its `dispatched` count; a committed label key rotates; and the arms'
`union` is read per set and pooled. What none of them checks: a variable nobody declared, that no
prompt author read the held-out file, that one judge read each case, and that evidence is right.

THE CONFORMANCE ARM. `scan_pairing_sites` names every comprehension, in a tracked `*.py` under the
tool root this kit sits in (this file excepted), whose filter is `all()` over a second population with
an `in` test from the outer case to the inner variant, or an `is not None` test naming both. What it
does not see: a JavaScript harness, and a pairing written as a `for` loop building a common list.

Exit: 0 scored run · 1 red self-test · 2 any refusal or argument error.
"""

import argparse
import ast
import contextlib
import io
import json
import os
import pathlib
import re
import statistics
import subprocess
import sys
import tempfile

# ---- the review-replay instance's constants, moved from review_replay.py with its core.
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
#: The `[tag]` a design-record audit addresses a finding by, read as tier2-review.js's deriveAddressKey reads it.
TAG_REF = re.compile(r"\[[a-z][a-z0-9-]*\]")

# ---- the scouted-seam instance's constant, ported from the grader blob.
CODE_TOKEN = re.compile(r"-{0,2}[A-Za-z_][\w-]*")

HEX40 = re.compile(r"[0-9a-fA-F]{40}")
KIT_DIR = pathlib.Path(__file__).resolve().parent
#: The two instances the factory exists for; `check_instances` reds when the table lacks one.
INSTANCE_KEYS = ("review-replay", "scouted-seam")
#: The arm count `run_selftest` must reach, as review_replay.py declares its own.
ARMS_DECLARED = 13


class Refusal(Exception):
    """A population the factory will not score: an unreadable source, a malformed row, a partial pairing."""


def read_raw_output(src, repo="."):
    """The text of a committed raw output: a working-tree path, a 40-hex blob, or `<rev>:<path>`."""
    if not src or src.startswith("-"):
        raise Refusal(f"source {src!r}: a source opening `-` or empty is refused")
    path = pathlib.Path(src)
    if path.is_file():
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            raise Refusal(f"source {src}: unreadable ({exc})") from None
    elif HEX40.fullmatch(src) or len(src.partition(":")[0]) > 1 and ":" in src:
        try:
            proc = subprocess.run(["git", "-C", str(repo), "cat-file", "blob", src], capture_output=True, check=False)
        except OSError as exc:
            raise Refusal(f"object {src}: git could not run ({exc})") from None
        if proc.returncode:
            why = proc.stderr.decode("utf-8", "replace").strip().splitlines()
            raise Refusal(f"object {src}: git cannot read it ({why[0] if why else 'exit ' + str(proc.returncode)})")
        try:
            text = proc.stdout.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise Refusal(f"object {src}: not UTF-8 ({exc})") from None
    else:
        raise Refusal(f"source {src}: no such file, and not a blob id or <rev>:<path>")
    lines = text.splitlines(keepends=True)
    skip = 0
    while skip < len(lines) and lines[skip].startswith("//"):
        skip += 1
    return "".join(lines[skip:])


def derive_paired_cases(case_ids, answers):
    """`(paired, unanswered)`: the ids every variant answered in case order, and each variant's misses.

    `answers` maps each variant, in argument order, to the case ids it answered. Refused: no variant,
    an answer outside the population, a variant that answered nothing, and an empty pairing.
    """
    if not answers:
        raise Refusal("no variant to pair")
    population = set(case_ids)
    unanswered, missed = {}, set()
    for variant, ids in answers.items():
        ids = list(ids)
        foreign = [i for i in ids if i not in population]
        if foreign:
            raise Refusal(f"{variant} answers {', '.join(map(str, foreign))}, outside the population of {len(case_ids)} case(s)")
        if not ids:
            raise Refusal(f"{variant} answered no case of {len(case_ids)}")
        answered = set(ids)
        unanswered[variant] = [c for c in case_ids if c not in answered]
        missed.update(unanswered[variant])
    paired = [c for c in case_ids if c not in missed]
    if not paired:
        raise Refusal(f"empty pairing: no case of {len(case_ids)} is answered by every one of {', '.join(answers)}")
    return paired, unanswered


def render_population(paired, total, unanswered, variant):
    """The head every figure line opens with: the paired population, then this variant's misses."""
    return f"paired {len(paired)} of {total} · {variant} unanswered {', '.join(map(str, unanswered[variant])) or 'none'}"


# ---- the review-replay instance: review_replay.py's scoring core.

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


def derive_ref_parts(text):
    """`(path, where)` of a spec ref `<file>:<where>`, the path folded: `\\` to `/`, a drive to `/`, `./` dropped."""
    if text is None:
        return None
    s = text.strip().strip("`").replace("\\", "/")
    s = re.sub(r"^[A-Za-z]:/", "/", s)
    while s.startswith("./"):
        s = s[2:]
    path, sep, where = s.partition(":")
    return (path, where) if sep and path else None


def extract_section_ref(text):
    """`(path, section)` from a spec ref like `x.md:§2 S5` or `C:/r/x.md:section 4`, else None."""
    parts = derive_ref_parts(text)
    if parts is None:
        return None
    path, where = parts
    m = SECTION_REF.search(where)
    if m:
        return path, int(m.group(1))
    m = ITEM_SECTION.search(where)
    return (path, ITEM_SECTIONS[m.group(1)]) if m else None


def extract_tag_ref(text):
    """`(path, key)` from a spec ref: `key` is the first `[tag]` in `<where>`, else the integer section.

    The section is `extract_section_ref`'s, so a ref with no tag keys exactly as before; None when
    the address names neither. A tag key is a string, so a matcher compares it by equality only.
    """
    parts = derive_ref_parts(text)
    if parts is None:
        return None
    m = TAG_REF.search(parts[1])
    return (parts[0], m.group(0)) if m else extract_section_ref(text)


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
    mode `line` holds the `[tag]` or the SECTION. `unit` names what one item is: `raw-finding` from an
    appendix, `adjudicated-item` from a legacy table. An appendix item also carries its `lens`.
    """
    spec = mode == "spec-audit"
    read_ref = extract_tag_ref if spec else extract_line_ref
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
    read_ref = extract_tag_ref if spec else extract_line_ref
    candidates = []
    for r in rows:
        loc = read_ref(r.get("ref"))
        candidates.append({"lens": r.get("lens"), "ref": r.get("ref") or "-", "path": loc and loc[0], "line": loc and loc[1]})
    if candidates and not any(c["path"] for c in candidates):
        return None, f"no-scorable: {len(candidates)} confirmed row(s), none with a file-and-{'section' if spec else 'line'} ref"
    return candidates, None


def check_same_file(a, b):
    """Equal, or one ends with `/` plus the other (the basename ceiling in review_replay.py's docstring)."""
    return a == b or a.endswith("/" + b) or b.endswith("/" + a)


def measure_recall(items, candidates, window):
    """Match every scorable known item against the candidates; returns the score as a dict.

    At window 0 a match is EQUALITY, never a subtraction, so a `[tag]` key is compared and never
    subtracted from a section.
    """
    scorable = [it for it in items if it["path"]]
    pairs = [(i, j) for i, it in enumerate(scorable) for j, c in enumerate(candidates)
             if c["path"] and check_same_file(it["path"], c["path"])
             and (it["line"] == c["line"] if window == 0 else abs(it["line"] - c["line"]) <= window)]
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


# ---- the scouted-seam instance: aScoutedSeam's grader, ported from blob a0389611 at b0fe68f30.

def derive_path_key(p):
    return (p or "").replace(chr(92), "/").strip().lstrip("./").lower()


def extract_code_tokens(symbol):
    return [t.lower() for t in CODE_TOKEN.findall(symbol or "")
            if len(t) >= 3 and (re.search(r"[A-Z_-]", t) or (symbol or "").strip() == t)]


def check_path_match(a, b):
    a, b = derive_path_key(a), derive_path_key(b)
    return bool(a and b) and (a.endswith(b) or b.endswith(a))


def check_hit(gt, seam):
    if not check_path_match(gt["path"], seam.get("path")):
        return False
    toks = extract_code_tokens(gt.get("symbol"))
    lead = CODE_TOKEN.match((gt.get("symbol") or "").strip())
    if not toks or not lead or lead.group(0).lower() not in toks:
        return True
    text = ((seam.get("symbol") or "") + " " + (seam.get("how") or "")).lower()
    return any(t in text for t in toks)


def check_case(case, res, k=None):
    """One case's verdict: items hit, the primary's rank and binding, SOLVED, and decoy MUSTs.

    A decoy matches on its path AND its symbol, because one file can hold the right seam and the
    wrong one: `resolveEntryImage` and `imageField` share a file in inCMS.
    """
    seams = (res or {}).get("seams") or []
    rows = []
    for g in case.get("ground_truth") or []:
        best = next(((s.get("rank", si + 1), s.get("binding")) for si, s in enumerate(seams)
                     if check_hit(g, s)), None)
        rows.append({"rank": best[0] if best else None, "binding": best[1] if best else None})
    decoys = case.get("decoys") or []
    false_must = [s for s in seams if s.get("binding") == "MUST" and any(check_hit(d, s) for d in decoys)]
    solved = (bool(rows) and rows[0]["rank"] is not None and rows[0]["binding"] in ("MUST", "SHOULD")
              and (k is None or rows[0]["rank"] <= k))
    return {"id": case["id"], "point": case.get("point"), "n_gt": len(rows),
            "hit": sum(1 for r in rows if r["rank"] is not None), "solved": solved,
            "primary_rank": rows[0]["rank"] if rows else None, "n_seams": len(seams),
            "n_must": sum(1 for s in seams if s.get("binding") == "MUST"), "false_must": len(false_must)}


def read_case_list(src, repo="."):
    """A cases file through `read_raw_output`: a non-empty JSON list of cases, each carrying an `id`."""
    try:
        cases = json.loads(read_raw_output(src, repo))
    except ValueError as exc:
        raise Refusal(f"source {src}: not JSON ({exc})") from None
    if not isinstance(cases, list) or not cases or not all(isinstance(c, dict) and "id" in c for c in cases):
        raise Refusal(f"source {src}: not a non-empty list of cases each carrying an `id`")
    return cases


def read_scouted_population(cases_src, results_src, repo="."):
    """`(corpus, results)` from the cases file and the results file, each through `read_raw_output`."""
    corpus = read_case_list(cases_src, repo)
    try:
        results = json.loads(read_raw_output(results_src, repo))
    except ValueError as exc:
        raise Refusal(f"source {results_src}: not JSON ({exc})") from None
    if not isinstance(results, dict):
        raise Refusal(f"source {results_src}: not an object of arms")
    return corpus, results


def read_arm_rows(results, arm):
    """One arm's rows by case id; refused when the results carry no such arm."""
    rows = results.get(arm)
    if arm == "judge" or not isinstance(rows, dict):
        raise Refusal(f"no arm {arm!r} in the results")
    return rows


def read_seam_row(arm, cid, row):
    """A result row, refused naming the arm and the case when it carries no `seams` list."""
    if not isinstance(row, dict) or not isinstance(row.get("seams"), list):
        raise Refusal(f"arm {arm} case {cid}: the result row carries no `seams` list")
    return row


def read_judge_cell(arm, cid, cell):
    """A judged cell, refused naming the arm and the case when it lacks `primary` or `covered`."""
    if not isinstance(cell, dict) or "primary" not in cell or "covered" not in cell:
        raise Refusal(f"judged arm {arm} case {cid}: the cell carries no `primary` and `covered`")
    return cell


def measure_scouted_grade(corpus, results, arm, k=None):
    """`grade`: per-case rows and the arm's total, over the cases it answered."""
    ids = [c["id"] for c in corpus]
    by_id = {c["id"]: c for c in corpus}
    rows = read_arm_rows(results, arm)
    paired, unanswered = derive_paired_cases(ids, {arm: list(rows)})
    graded = [check_case(by_id[cid], read_seam_row(arm, cid, rows[cid]), k) for cid in paired]
    lines = [f"{g['id']:<34} {g['point']:<9} gt {g['hit']}/{g['n_gt']} solved={str(g['solved'])[0]} "
             f"prim={g['primary_rank']} seams={g['n_seams']} must={g['n_must']} decoyMUST={g['false_must']}" for g in graded]
    pos = [g for g in graded if g["n_gt"]]
    lines.append(f"{render_population(paired, len(ids), unanswered, arm)} · positives {len(pos)} solved "
                 f"{sum(g['solved'] for g in pos)} · items {sum(g['hit'] for g in pos)}/{sum(g['n_gt'] for g in pos)} · "
                 f"controls {len(graded) - len(pos)} decoy MUSTs {sum(g['false_must'] for g in graded)} · "
                 f"graded {len(graded)} of {len(corpus)}")
    return lines


def measure_scouted_compare(corpus, results, arms):
    """`compare`: the arms side by side over the cases every one of them answered."""
    ids = [c["id"] for c in corpus]
    by_id = {c["id"]: c for c in corpus}
    arm_rows = {a: read_arm_rows(results, a) for a in arms}
    paired, unanswered = derive_paired_cases(ids, {a: list(rows) for a, rows in arm_rows.items()})
    tot = {a: [0, 0, 0, 0, 0, 0] for a in arm_rows}
    lines = []
    for cid in paired:
        cells = []
        for a, rows in arm_rows.items():
            g = check_case(by_id[cid], read_seam_row(a, cid, rows[cid]))
            for i, v in enumerate((g["solved"], g["hit"], g["n_gt"], g["n_seams"], g["n_must"], g["false_must"])):
                tot[a][i] += v
            prim = "-" if g["primary_rank"] is None else g["primary_rank"]
            cells.append(f"{prim:>3} {g['hit']}/{g['n_gt']} m{g['n_must']}")
        lines.append(f"{cid:<34}" + "".join(f"{x:>16}" for x in cells))
    pos = sum(1 for cid in paired if by_id[cid].get("ground_truth"))
    lines.append(f"common {len(paired)} ({pos} positive)")
    for a, t in tot.items():
        lines.append(f"{render_population(paired, len(ids), unanswered, a)} · solved {t[0]}/{pos} · items {t[1]}/{t[2]} · "
                     f"seams {t[3]} · MUST {t[4]} · decoy MUST {t[5]}")
    return lines


def measure_scouted_judged(corpus, results, arms):
    """`judged`: the judge's semantic reading over the cases it read for every arm; `a+b` is a union."""
    ids = [c["id"] for c in corpus]
    by_id = {c["id"]: c for c in corpus}
    judge = results.get("judge")
    if not isinstance(judge, dict):
        raise Refusal("the results carry no `judge` verdicts")
    answers = {}
    for a in arms:
        parts = a.split("+")
        absent = [p for p in parts if not isinstance(judge.get(p), dict)]
        if absent:
            raise Refusal(f"no judged arm {', '.join(absent)} in the results")
        # A union answers a case when every part was judged on it: a pairing, so it goes through the one pairer.
        answers[a] = derive_paired_cases(ids, {p: list(judge[p]) for p in parts})[0]
    paired, unanswered = derive_paired_cases(ids, answers)

    def derive_judged_cell(arm, cid):
        vs = [read_judge_cell(p, cid, judge[p][cid]) for p in arm.split("+")]
        return {"primary": any(v.get("primary") for v in vs),
                "covered": set().union(*[set(v.get("covered") or []) for v in vs]),
                "wrong": sum(len(v.get("wrong") or []) for v in vs),
                "extra": sum(v.get("valid_extra") or 0 for v in vs),
                "score": max(v.get("score") or 0 for v in vs)}

    pos = [cid for cid in paired if by_id[cid].get("ground_truth")]
    lines = [f"judged common {len(paired)} ({len(pos)} positive)"]
    for a in arms:
        cs = [derive_judged_cell(a, cid) for cid in pos]
        ctl = [derive_judged_cell(a, cid) for cid in paired if not by_id[cid].get("ground_truth")]
        mean = f"{statistics.mean(x['score'] for x in cs):.2f}" if cs else "-"
        lines.append(f"{render_population(paired, len(ids), unanswered, a)} · primary {sum(x['primary'] for x in cs)}/{len(pos)} · "
                     f"items {sum(len(x['covered']) for x in cs)}/{sum(len(by_id[cid]['ground_truth']) for cid in pos)} · "
                     f"wrong MUST {sum(x['wrong'] for x in cs + ctl)} · valid extra {sum(x['extra'] for x in cs)} · "
                     f"mean score {mean}")
    return lines


# ---- the experiment shape (TOOL-dFairHearing-14): the method's rules, enforced where committed outputs show them.
ARM_KEYS = {"name", "base", "settings", "dispatched"}
#: The union's sets, as the manifest spells them and as the figure line prints them.
UNION_SETS = {"tuning": "tuning", "heldOut": "held-out"}


def derive_scouted_evidence(case):
    """A scouted-seam case's objective evidence: its `sha`, then each ground-truth item's `path` and `why`; empty when any is missing."""
    items = case.get("ground_truth") or []
    if not case.get("sha") or not isinstance(items, list):
        return []
    if not all(isinstance(g, dict) and g.get("path") and g.get("why") for g in items):
        return []
    return [str(case["sha"])] + [f"{g['path']}: {g['why']}" for g in items]


def derive_replay_evidence(case):
    """A review-replay case's evidence: the known item's ref and the record it came from; empty when either is missing."""
    return [f"{case['path']}:{case['line']}", case["record"]] if case.get("path") and case.get("record") else []


def check_case_evidence(instance, cases):
    """Refused naming the first case whose instance's `case_evidence` hook returns nothing."""
    hook = INSTANCES[instance]["case_evidence"]
    bare = next((c["id"] for c in cases if not hook(c)), None)
    if bare is not None:
        raise Refusal(f"case {bare}: `case_evidence` returns nothing for it under {instance}, so it carries no objective evidence to grade")


def check_held_out_frozen(path, tuning_ids, repo="."):
    """`(line, cases)`: the freeze line and the held-out cases.

    Refused: a path opening `-`, outside the repository or not a working-tree file; a history of other
    than exactly one commit, read by ONE `git log --format=%H` with argv; and an id that is also a
    tuning case's. "Never read to change a prompt" is printed as recorded: no committed output shows it.
    """
    if not path or not isinstance(path, str) or path.startswith("-"):
        raise Refusal(f"heldOut {path!r}: a path opening `-` or empty is refused")
    try:
        top = subprocess.run(["git", "-C", str(repo), "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=False)
    except OSError as exc:
        raise Refusal(f"heldOut {path}: git could not run ({exc})") from None
    if top.returncode:
        raise Refusal(f"heldOut {path}: {repo} is not a git checkout, so no freeze can be read")
    root = pathlib.Path(top.stdout.strip()).resolve()
    try:
        rel = pathlib.Path(path).resolve().relative_to(root).as_posix()
    except ValueError:
        raise Refusal(f"heldOut {path}: outside the repository {root.as_posix()}") from None
    if not pathlib.Path(path).is_file():
        raise Refusal(f"heldOut {path}: not a working-tree file")
    log = subprocess.run(["git", "-C", str(root), "log", "--format=%H", "--", rel], capture_output=True, text=True, check=False)
    shas = log.stdout.split()
    if log.returncode or not shas:
        raise Refusal(f"heldOut {rel}: no commit in its history, so it was never frozen")
    if len(shas) > 1:
        raise Refusal(f"heldOut {rel}: {len(shas)} commits, frozen at {shas[-1]} and changed after it at {', '.join(reversed(shas[:-1]))}")
    cases = read_case_list(path, repo)
    tuning = set(tuning_ids)
    shared = [c["id"] for c in cases if c["id"] in tuning]
    if shared:
        raise Refusal(f"heldOut {rel}: case id(s) {', '.join(map(str, shared))} are tuning cases too")
    return f"held-out: frozen at {shas[0]} · {len(cases)} case(s) · never read to change a prompt — recorded, not checked", cases


def check_one_variable(arms):
    """One line per arm: `base`, or the ONE settings key it varies from its base, compared as JSON values."""
    by_name = {a["name"]: a for a in arms}
    lines = []
    for a in arms:
        base = a.get("base")
        if base is None:
            lines.append(f"arm {a['name']}: base")
            continue
        if base not in by_name or base == a["name"]:
            raise Refusal(f"arm {a['name']}: base {base!r} is not another declared arm")
        mine, theirs = a["settings"], by_name[base]["settings"]
        varied = [k for k in sorted(set(mine) | set(theirs)) if k not in mine or k not in theirs
                  or json.dumps(mine[k], sort_keys=True) != json.dumps(theirs[k], sort_keys=True)]
        if not varied:
            raise Refusal(f"arm {a['name']}: its settings equal its base {base}'s, so it varies no variable")
        if len(varied) > 1:
            raise Refusal(f"arm {a['name']}: varies {', '.join(varied)} from {base}; one variable per arm")
        lines.append(f"arm {a['name']}: varies {varied[0]} from {base}")
    return lines


def measure_parsed(arms, parsed):
    """One `parsed <arm>: <n> of <dispatched>` line per arm; refused when `dispatched` is undeclared or below `n`."""
    lines = []
    for a in arms:
        sent = a.get("dispatched")
        if isinstance(sent, bool) or not isinstance(sent, int) or sent < 0:
            raise Refusal(f"arm {a['name']}: `dispatched` is {sent!r}, not a count, so its parsed replies have nothing to be counted against")
        n = len(parsed[a["name"]])
        if n > sent:
            raise Refusal(f"arm {a['name']}: {n} parsed against {sent} dispatched")
        lines.append(f"parsed {a['name']}: {n} of {sent}")
    return lines


def check_judge_rotation(judge, repo="."):
    """The judge line. A committed key `{<case>: {<label>: <arm>}}` gives each judged arm one label per case,
    and with two or more arms over two or more cases no arm holds one label on every case. No key:
    recorded, not checked."""
    src = (judge or {}).get("key")
    if src is None:
        return "labels rotated — recorded, not checked: no committed key"
    try:
        key = json.loads(read_raw_output(src, repo))
    except ValueError as exc:
        raise Refusal(f"judge key {src}: not JSON ({exc})") from None
    if not isinstance(key, dict) or not key or not all(
            isinstance(v, dict) and v and all(isinstance(arm, str) for arm in v.values()) for v in key.values()):
        raise Refusal(f"judge key {src}: not a non-empty object of {{<case>: {{<label>: <arm>}}}}")
    arms = list(dict.fromkeys(arm for labels in key.values() for arm in labels.values()))
    for case, labels in key.items():
        held = list(labels.values())
        unlabelled = [a for a in arms if a not in held]
        doubled = [a for a in arms if held.count(a) > 1]
        if unlabelled or doubled:
            raise Refusal(f"judge key case {case}: arm(s) {', '.join(unlabelled + doubled)} hold "
                          f"{'no label' if unlabelled else 'more than one label'}; each judged arm takes one")
    if len(arms) < 2 or len(key) < 2:
        return f"labels rotated — recorded, not checked: {len(arms)} arm(s) over {len(key)} case(s) leave nothing to rotate"
    for arm in arms:
        worn = {next(label for label, a in labels.items() if a == arm) for labels in key.values()}
        if len(worn) == 1:
            raise Refusal(f"judge key {src}: arm {arm} holds label {worn.pop()} on every one of {len(key)} case(s), so its label is not rotated")
    return f"labels rotated — checked: {len(arms)} arm(s) over {len(key)} case(s) in {src}"


def measure_union(sets, verdicts):
    """aScoutedSeam's system reading per set, then pooled: a positive case one of the set's arms was judged on
    is covered when any of them covered its primary; a case none was judged on is outside the population."""
    lines, hit, total = [], 0, 0
    for name, cases, arms in sets:
        cells = {a: verdicts[a] for a in arms}
        ids = [c["id"] for c in cases if c.get("ground_truth") and any(cells[a].get(c["id"]) for a in arms)]
        covered = sum(1 for cid in ids if any(read_judge_cell(a, cid, cells[a][cid]).get("primary")
                                              for a in arms if cells[a].get(cid)))
        lines.append(f"system {name} {covered}/{len(ids)} · {' + '.join(arms)}")
        hit, total = hit + covered, total + len(ids)
    if len(sets) > 1:
        lines.append(f"system pooled {hit}/{total} · {' + '.join(name for name, _, _ in sets)}")
    return lines


def measure_scouted_experiment(manifest, arms, repo="."):
    """The scouted-seam experiment's lines: the four rule lines, then the paired figures and the union."""
    corpus, results = read_scouted_population(manifest["cases"], manifest["results"], repo)
    sets, head = [("tuning", corpus)], []
    if "heldOut" in manifest:
        line, held = check_held_out_frozen(manifest["heldOut"], [c["id"] for c in corpus], repo)
        head.append(line)
        sets.append(("held-out", held))
    for _, cases in sets:
        check_case_evidence("scouted-seam", cases)
    head += check_one_variable(arms)
    population = [c["id"] for _, cases in sets for c in cases]
    parsed = {}
    for a in arms:
        rows = results.get(a["name"]) if a["name"] != "judge" else None
        rows = rows if isinstance(rows, dict) else {}
        parsed[a["name"]] = {cid: rows[cid] for cid in population
                             if isinstance(rows.get(cid), dict) and isinstance(rows[cid].get("seams"), list)}
    head += measure_parsed(arms, parsed)
    judge = manifest.get("judge")
    if judge is not None and (not isinstance(judge, dict) or set(judge) - {"verdicts", "key"} or not isinstance(judge.get("verdicts"), str)):
        raise Refusal(f"judge {judge!r}: not an object naming `verdicts` and optionally `key`")
    head.append(check_judge_rotation(judge, repo))
    figures = []
    # Figures pair the PARSED rows only, so an unparsed reply is counted above and never scored here.
    for name, cases in sets:
        ids = {c["id"] for c in cases}
        answered = {a: {cid: row for cid, row in rows.items() if cid in ids} for a, rows in parsed.items()}
        answered = {a: rows for a, rows in answered.items() if rows}
        if answered:
            figures.append(f"figures {name}")
            figures += measure_scouted_compare(cases, answered, list(answered))
    union = manifest.get("union")
    if union is not None:
        want = [k for k in UNION_SETS if k == "tuning" or "heldOut" in manifest]
        if (not isinstance(union, dict) or sorted(union) != sorted(want)
                or not all(isinstance(v, list) and v and all(isinstance(a, str) for a in v) for v in union.values())):
            raise Refusal(f"union {union!r}: not an object naming a non-empty arm list for each of {', '.join(want)}")
        if judge is None:
            raise Refusal("union: declared with no `judge.verdicts` to read coverage from")
        verdicts = results.get(judge["verdicts"])
        if not isinstance(verdicts, dict):
            raise Refusal(f"judge.verdicts {judge['verdicts']!r}: no such verdicts object in the results")
        absent = [a for v in union.values() for a in v if not isinstance(verdicts.get(a), dict)]
        if absent:
            raise Refusal(f"union: no judged arm {', '.join(absent)} in {judge['verdicts']}")
        figures += measure_union([(UNION_SETS[k], cases, union[k]) for k, (_, cases) in zip(want, sets)], verdicts)
    return head + figures


def measure_replay_experiment(manifest, arms, repo="."):
    """The review-replay experiment's lines: the known record's scorable items are its cases, each arm one candidate."""
    candidates = manifest["candidates"]
    if not isinstance(candidates, dict) or set(candidates) - {a["name"] for a in arms}:
        raise Refusal(f"candidates {candidates!r}: not an object of <declared arm>: <src>")
    known_text = read_raw_output(manifest["known"], repo)
    mode = read_record_kind(known_text) or "diff-review"
    known, err = parse_record_findings(known_text, mode)
    if err:
        raise Refusal(f"known {manifest['known']}: {err}")
    check_case_evidence("review-replay", [{**it, "record": manifest["known"]} for it in known["items"] if it["path"]])
    head = check_one_variable(arms)
    scores = {}
    for a in arms:
        src = candidates.get(a["name"])
        replay = measure_replay(known_text, read_raw_output(src, repo), 10)[0] if src else None
        scores[a["name"]] = [replay["score"]] if replay else []
    head += measure_parsed(arms, scores)
    head.append(check_judge_rotation(None))
    figures = [f"recall {name}: {len(s[0]['matched'])} of {s[0]['scorable']} scorable · unscorable {len(s[0]['unscorable'])} "
               f"· candidate-only {len(s[0]['candidate_only'])}" for name, s in scores.items() if s]
    return head + figures


def check_experiment(manifest, repo="."):
    """An experiment's lines, every rule before the first figure; a broken rule is a Refusal naming the rule, the arm or case, and the value."""
    why = check_instances()
    if why:
        raise Refusal(why)
    if not isinstance(manifest, dict):
        raise Refusal("manifest: not a JSON object")
    instance = manifest.get("instance")
    if instance not in INSTANCES:
        raise Refusal(f"manifest instance {instance!r}: not one of {', '.join(INSTANCES)}")
    required, optional = INSTANCES[instance]["manifest"]
    unknown, missing = sorted(set(manifest) - required - optional), sorted(required - set(manifest))
    if unknown or missing:
        raise Refusal(f"manifest: {'unknown key(s) ' + ', '.join(unknown) if unknown else ''}"
                      f"{'; ' if unknown and missing else ''}{'missing key(s) ' + ', '.join(missing) if missing else ''}")
    arms = manifest["arms"]
    if not isinstance(arms, list) or not arms:
        raise Refusal("manifest arms: no arm declared")
    seen = set()
    for a in arms:
        if not isinstance(a, dict) or not isinstance(a.get("name"), str) or not a["name"]:
            raise Refusal(f"arm {a!r}: not an object with a `name`")
        if set(a) - ARM_KEYS:
            raise Refusal(f"arm {a['name']}: unknown key(s) {', '.join(sorted(set(a) - ARM_KEYS))}")
        if not isinstance(a.get("settings"), dict):
            raise Refusal(f"arm {a['name']}: no `settings` object, so the variable it varies is undeclared")
        if a["name"] in seen:
            raise Refusal(f"arm {a['name']}: declared twice")
        seen.add(a["name"])
    return INSTANCES[instance]["experiment"](manifest, arms, repo)


#: Each instance: its readers, its measures, its `case_evidence` hook, and its experiment manifest's
#: keys, required then optional; any other key is refused, so a misspelt rule is never skipped.
INSTANCES = {
    "review-replay": {"readers": (read_raw_output, parse_record_findings, parse_candidates), "measure": measure_replay,
                      "case_evidence": derive_replay_evidence, "experiment": measure_replay_experiment,
                      "manifest": ({"instance", "known", "candidates", "arms"}, set())},
    "scouted-seam": {"readers": (read_raw_output, read_scouted_population, read_seam_row, read_judge_cell),
                     "measure": {"grade": measure_scouted_grade, "compare": measure_scouted_compare,
                                 "judged": measure_scouted_judged},
                     "case_evidence": derive_scouted_evidence, "experiment": measure_scouted_experiment,
                     "manifest": ({"instance", "cases", "results", "arms"}, {"heldOut", "judge", "union"})},
}


def check_instances():
    """None when the table holds every instance the factory exists for, each with its `case_evidence` hook, else a refusal naming the gap."""
    missing = [k for k in INSTANCE_KEYS if k not in INSTANCES]
    if missing:
        return f"INSTANCES lacks {', '.join(missing)}: the factory needs both of {', '.join(INSTANCE_KEYS)}"
    hookless = [k for k, v in INSTANCES.items() if not callable(v.get("case_evidence"))]
    return f"INSTANCES entry {', '.join(hookless)} declares no `case_evidence` hook, so its cases' evidence is unread" if hookless else None


# ---- the conformance arm: no second scorer pairs variants with cases outside this factory.
ALL_CALL = re.compile(rb"\ball\s*\(")
COMPREHENSIONS = (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)


def scan_pairing_sites(root):
    """`<path>:<line>` of each pairing comprehension in the tracked `*.py` under `root`, this file excepted.

    A pairing comprehension filters on `all()` over a generator ranging over a second population whose
    element is `<outer case> in <inner variant>`, or an `is not None` test naming both. Outside a git
    checkout every `*.py` is the population. A file that does not parse is named too: it is unread.
    """
    root = pathlib.Path(root)
    try:
        proc = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--", "*.py"], capture_output=True, check=False)
        files = [f for f in proc.stdout.decode("utf-8").split("\0") if f] if proc.returncode == 0 else None
    except OSError:
        files = None
    if files is None:
        files = [p.relative_to(root).as_posix() for p in root.rglob("*.py")]

    def names(node):
        return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}

    sites = []
    for rel in sorted(files):
        if pathlib.PurePosixPath(rel).name == pathlib.Path(__file__).name:
            continue
        data = (root / rel).read_bytes()
        if not ALL_CALL.search(data):
            continue
        try:
            tree = ast.parse(data)
        except SyntaxError as exc:
            sites.append(f"{rel}:{exc.lineno or 0} unparseable")
            continue
        for node in ast.walk(tree):
            if not isinstance(node, COMPREHENSIONS):
                continue
            outer = set().union(*(names(g.target) for g in node.generators))
            outer_iters = {ast.dump(g.iter) for g in node.generators}
            for cond in (c for g in node.generators for c in g.ifs):
                for call in ast.walk(cond):
                    if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id == "all"
                            and len(call.args) == 1 and isinstance(call.args[0], ast.GeneratorExp)):
                        continue
                    gen = call.args[0]
                    if any(ast.dump(g.iter) in outer_iters for g in gen.generators):
                        continue
                    inner = set().union(*(names(g.target) for g in gen.generators))
                    test = gen.elt
                    if not (isinstance(test, ast.Compare) and len(test.ops) == 1):
                        continue
                    left, right = names(test.left), names(test.comparators[0])
                    member = isinstance(test.ops[0], ast.In) and left & outer and right & inner
                    present = (isinstance(test.ops[0], ast.IsNot) and isinstance(test.comparators[0], ast.Constant)
                               and test.comparators[0].value is None and left & outer and left & inner)
                    if member or present:
                        sites.append(f"{rel}:{node.lineno}")
    return list(dict.fromkeys(sites))


# ---- self-test. The proof reads aScoutedSeam's committed blobs; the rest are inline fixtures.
PROOF_COMMIT = "b0fe68f30"
PROOF_DIR = "memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-"
GRADER_BLOB = "a03896116e3c5cbf853affda241c22d8408cb945"
PLANTED = 'def pair(cases, arms):\n    return [c for c in cases if all(c["id"] in rows for rows in arms.values())]\n'
FIXTURE_CASES = [{"id": "a", "point": "p", "ground_truth": [{"path": "x.py", "symbol": "f"}]},
                 {"id": "b", "point": "p", "ground_truth": []}, {"id": "c", "point": "p", "ground_truth": []}]
FIXTURE_RESULTS = {v: {"a": {"seams": [{"path": "x.py", "symbol": "f", "binding": "MUST"}]}, "b": {"seams": []}}
                   for v in ("v1", "v2", "v3", "v4")}
EXPERIMENT_CASES = [{"id": "a", "point": "p", "sha": "a" * 40, "ground_truth": [{"path": "x.py", "symbol": "f", "why": "the seam"}]},
                    {"id": "b", "point": "p", "sha": "b" * 40, "ground_truth": [{"path": "y.py", "symbol": "g", "why": "the seam"}]},
                    {"id": "c", "point": "p", "sha": "c" * 40, "ground_truth": []}]
EXPERIMENT_HELD = [{"id": "h", "point": "p", "sha": "d" * 40, "ground_truth": [{"path": "w.py", "symbol": "k", "why": "the seam"}]}]
EXPERIMENT_SEAMS = {cid: {"seams": [{"path": p, "symbol": s, "binding": "MUST"}]} for cid, p, s in
                    (("a", "x.py", "f"), ("b", "y.py", "g"), ("c", "z.py", "h"), ("h", "w.py", "k"))}
# m1b's reply on `c` did not parse; m1b@medium was judged on `b` alone, so the union reads `a` from m1b only.
EXPERIMENT_RESULTS = {"m1b": {**EXPERIMENT_SEAMS, "c": {"error": "no reply"}}, "m1b@medium": EXPERIMENT_SEAMS,
                      "judge2": {"m1b": {"a": {"primary": True, "covered": [0]}, "b": {"primary": False, "covered": []},
                                         "h": {"primary": True, "covered": [0]}},
                                 "m1b@medium": {"b": {"primary": True, "covered": [0]}}}}
EXPERIMENT_KEY = {"a": {"ARM-A": "m1b", "ARM-B": "m1b@medium"}, "b": {"ARM-A": "m1b@medium", "ARM-B": "m1b"},
                  "c": {"ARM-A": "m1b", "ARM-B": "m1b@medium"}}
#: The method's own experiment: the cases and results at this commit, and the held-out file frozen at b6c828a92.
UNION_PROOF_COMMIT = "5f8ef021d"
HELD_OUT_FILE = "memory/builds/aScoutedSeam/build/2026-10-18-build-TOOL-aScoutedSeam-1-13-held-out-cases.json"


def read_proof_tree():
    """The checkout holding aScoutedSeam's records, or None: the proof's population exists only there."""
    try:
        proc = subprocess.run(["git", "-C", str(KIT_DIR), "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=False)
    except OSError:
        return None
    top = pathlib.Path(proc.stdout.strip()) if proc.returncode == 0 else None
    return top if top and (top / "memory" / "builds" / "aScoutedSeam").is_dir() else None


def run_selftest():
    top = read_proof_tree()
    no_tree = ("skip", "no aScoutedSeam records in this tree")

    def check_refused(fn, *needles):
        try:
            fn()
        except Refusal as exc:
            return None if all(n in str(exc) for n in needles) else f"refused without naming {needles}: {exc}"
        return f"not refused; wanted a refusal naming {needles}"

    def check_paired_refuses():
        return (check_refused(lambda: derive_paired_cases(["a", "b"], {"x": ["a"], "y": ["b"]}), "empty pairing", "x", "y")
                or check_refused(lambda: derive_paired_cases(["a", "b"], {"x": ["a", "z"]}), "x", "z", "outside")
                or check_refused(lambda: derive_paired_cases(["a", "b"], {"x": ["a"], "y": []}), "y", "no case")
                or (None if derive_paired_cases(["c", "a", "b"], {"y": ["b", "a"], "x": ["a", "b", "c"]})
                    == (["a", "b"], {"y": ["c"], "x": []}) else "the pairing left case order or argument order"))

    def check_row_refuses():
        rows = {"v": {"a": {"seams": []}, "b": {"why": "no seams"}}}
        return check_refused(lambda: measure_scouted_grade(FIXTURE_CASES, rows, "v"), "arm v", "case b", "seams")

    def check_tag_section():
        want = [("x.md:[supervise] Relaunch, [spawn] first bullet", ("x.md", "[supervise]")), ("x.md:§2 [act]", ("x.md", "[act]")),
                ("x.md:§2 S5", ("x.md", 2)), ("x.md:status header", None)]
        bad = next((f"{ref!r} read as {extract_tag_ref(ref)!r}, not {w!r}" for ref, w in want if extract_tag_ref(ref) != w), None)
        if bad:
            return bad
        known = [{"id": "1", "path": "x.md", "line": "[supervise]"}]
        cands = [{"lens": "l", "ref": "x.md:[supervise]", "path": "x.md", "line": "[supervise]"},
                 {"lens": "l", "ref": "x.md:[spawn]", "path": "x.md", "line": "[spawn]"}]
        score = measure_recall(known, cands, 0)
        return None if [c["ref"] for _, c in score["matched"]] == ["x.md:[supervise]"] else f"window 0 over tags: {score!r}"

    def check_instances_arm():
        if check_instances() is not None:
            return f"refused with both entries present: {check_instances()}"
        held = INSTANCES.pop("scouted-seam")
        try:
            why = check_instances()
        finally:
            INSTANCES["scouted-seam"] = held
        return None if why and "scouted-seam" in why else f"the review-replay entry alone passed: {why!r}"

    def check_scouted_proof():
        if top is None:
            return no_tree
        corpus, results = read_scouted_population(f"{PROOF_COMMIT}:{PROOF_DIR}3-cases.json", f"{PROOF_COMMIT}:{PROOF_DIR}5-results.json", top)
        grade = measure_scouted_grade(corpus, results, "m1b")[-1]
        compare = "\n".join(measure_scouted_compare(corpus, results, ["m1b", "m1b@medium"]))
        judged = "\n".join(measure_scouted_judged(corpus, results, ["m1cA@medium"]))
        want = [(grade, "paired 19 of 30 · m1b unanswered "), (grade, "· positives 15 solved 10 · items 17/40 ·"),
                (grade, "· graded 19 of 30"), (compare, "\ncommon 19 (15 positive)\n"),
                (compare, "· m1b unanswered "), (compare, "solved 10/15 · items 17/40 · seams 175 · MUST 97 ·"),
                (compare, "· m1b@medium unanswered none · solved 9/15 · items 17/40 · seams 164 · MUST 114 ·"),
                (judged, "judged common 30 (24 positive)\n"), (judged, "primary 17/24 · items 39/59 ·")]
        return next((f"{w!r} not in {text!r}" for text, w in want if w not in text), None)

    def check_conformance():
        live = scan_pairing_sites(KIT_DIR.parent)
        if live:
            return f"a pairing outside the factory: {', '.join(live)}"
        with tempfile.TemporaryDirectory() as tmp:
            (pathlib.Path(tmp, "kit", "sub")).mkdir(parents=True)
            pathlib.Path(tmp, "kit", "sub", "planted.py").write_text(PLANTED, encoding="utf-8")
            pathlib.Path(tmp, "kit", "replay_scorer.py").write_text(PLANTED, encoding="utf-8")
            pathlib.Path(tmp, "kit", "replay_scorer_twin.py").write_text(KIT_DIR.joinpath("replay_scorer.py").read_text(encoding="utf-8"), encoding="utf-8")
            planted = scan_pairing_sites(pathlib.Path(tmp, "kit"))
            if planted != ["sub/planted.py:2"]:
                return f"the planted module, and only it, should be named: {planted!r}"
            if top is None:
                return no_tree
            pathlib.Path(tmp, "grader").mkdir()
            pathlib.Path(tmp, "grader", "bench.py").write_text(read_raw_output(GRADER_BLOB, top), encoding="utf-8")
            grader = scan_pairing_sites(pathlib.Path(tmp, "grader"))
        return None if grader == ["bench.py:384", "bench.py:647"] else f"the grader blob read as {grader!r}"

    def check_deterministic():
        with tempfile.TemporaryDirectory() as tmp:
            cases, res = pathlib.Path(tmp, "cases.json"), pathlib.Path(tmp, "results.json")
            cases.write_text("// a head line the reader skips\n" + json.dumps(FIXTURE_CASES), encoding="utf-8")
            res.write_text(json.dumps(FIXTURE_RESULTS), encoding="utf-8")
            argv = [sys.executable, str(KIT_DIR / "replay_scorer.py"), "--instance", "scouted-seam", "--cases", str(cases),
                    "--results", str(res), "--compare", "v3", "v1", "v4", "v2"]
            outs = [subprocess.run(argv, capture_output=True, check=False, env={**os.environ, "PYTHONHASHSEED": seed}) for seed in ("1", "2")]
        if any(o.returncode for o in outs) or outs[0].stdout != outs[1].stdout:
            return f"two runs differ: {[(o.returncode, o.stdout, o.stderr) for o in outs]!r}"
        heads = [line.split(" · ")[1] for line in outs[0].stdout.decode("utf-8").splitlines() if line.startswith("paired ")]
        return None if heads == [f"{v} unanswered c" for v in ("v3", "v1", "v4", "v2")] else f"variant lines out of argument order: {heads!r}"

    # ---- the experiment shape's arms: a valid fixture manifest, then one planted break per rule.
    def derive_fixture_manifest(tmp, **over):
        """A valid two-arm experiment over fixture files written into `tmp`; `over` replaces top-level keys."""
        cases, res = pathlib.Path(tmp, "cases.json"), pathlib.Path(tmp, "results.json")
        cases.write_text(json.dumps(EXPERIMENT_CASES), encoding="utf-8")
        res.write_text(json.dumps(EXPERIMENT_RESULTS), encoding="utf-8")
        manifest = {"instance": "scouted-seam", "cases": str(cases), "results": str(res),
                    "arms": [{"name": "m1b", "base": None, "settings": {"model": "m1b", "effort": "high"}, "dispatched": 3},
                             {"name": "m1b@medium", "base": "m1b", "settings": {"model": "m1b", "effort": "medium"}, "dispatched": 4}],
                    "judge": {"verdicts": "judge2", "key": None}, "union": {"tuning": ["m1b", "m1b@medium"]}}
        return json.loads(json.dumps({**manifest, **over}))

    def derive_frozen_repo(tmp):
        """A fixture repository at `tmp` whose held-out file has ONE commit: its path, that commit, and a git runner."""
        def run_git(*argv):
            return subprocess.run(["git", "-C", tmp, "-c", "user.name=selftest", "-c", "user.email=selftest@invalid",
                                   "-c", "commit.gpgsign=false", *argv], capture_output=True, text=True, check=True).stdout.strip()
        run_git("init", "-q")
        held = pathlib.Path(tmp, "held.json")
        held.write_text(json.dumps(EXPERIMENT_HELD), encoding="utf-8")
        run_git("add", "held.json")
        run_git("commit", "-q", "--no-verify", "-m", "freeze the held-out set")
        return held, run_git("rev-parse", "HEAD"), run_git

    def check_evidence_arm():
        with tempfile.TemporaryDirectory() as tmp:
            manifest = derive_fixture_manifest(tmp)
            check_experiment(manifest)
            bare = json.loads(json.dumps(EXPERIMENT_CASES))
            bare[1]["sha"] = ""
            pathlib.Path(tmp, "bare.json").write_text(json.dumps(bare), encoding="utf-8")
            why = check_refused(lambda: check_experiment({**manifest, "cases": str(pathlib.Path(tmp, "bare.json"))}), "case b", "case_evidence")
            if why:
                return why
            hook = INSTANCES["scouted-seam"].pop("case_evidence")
            try:
                return check_refused(lambda: check_experiment(manifest), "scouted-seam", "case_evidence")
            finally:
                INSTANCES["scouted-seam"]["case_evidence"] = hook

    def check_freeze_arm():
        with tempfile.TemporaryDirectory() as tmp:
            held, freeze, run_git = derive_frozen_repo(tmp)
            manifest = derive_fixture_manifest(tmp, heldOut=str(held), union={"tuning": ["m1b"], "heldOut": ["m1b"]})
            first = check_experiment(manifest, tmp)[0]
            if not first.startswith(f"held-out: frozen at {freeze} · 1 case(s) · never read to change a prompt — recorded, not checked"):
                return f"the first line reads {first!r}"
            shared = pathlib.Path(tmp, "shared.json")
            shared.write_text(json.dumps(EXPERIMENT_CASES + EXPERIMENT_HELD), encoding="utf-8")
            why = (check_refused(lambda: check_experiment({**manifest, "cases": str(shared)}, tmp), "heldOut", "h", "tuning")
                   or check_refused(lambda: check_experiment({**manifest, "heldOut": "-held.json"}, tmp), "heldOut", "`-`")
                   or check_refused(lambda: check_experiment({**manifest, "heldOut": str(pathlib.Path(tmp).parent / "held.json")}, tmp), "outside"))
            if why:
                return why
            held.write_text(json.dumps(EXPERIMENT_HELD, indent=1), encoding="utf-8")
            run_git("commit", "-q", "--no-verify", "-am", "tune after the freeze")
            second = run_git("rev-parse", "HEAD")
            return check_refused(lambda: check_experiment(manifest, tmp), "2 commits", f"frozen at {freeze}", second)

    def check_variable_arm():
        with tempfile.TemporaryDirectory() as tmp:
            lines = check_experiment(derive_fixture_manifest(tmp))
            if not {"arm m1b: base", "arm m1b@medium: varies effort from m1b"} <= set(lines):
                return f"the arm lines read {[line for line in lines if line.startswith('arm ')]!r}"
            two, none = derive_fixture_manifest(tmp), derive_fixture_manifest(tmp)
            two["arms"][1]["settings"]["model"] = "m1c"
            none["arms"][1]["settings"]["effort"] = "high"
            return (check_refused(lambda: check_experiment(two), "arm m1b@medium", "effort, model")
                    or check_refused(lambda: check_experiment(none), "arm m1b@medium", "varies no variable"))

    def check_parsed_arm():
        with tempfile.TemporaryDirectory() as tmp:
            lines = check_experiment(derive_fixture_manifest(tmp))
            counts = [i for i, line in enumerate(lines) if line.startswith("parsed ")]
            figure = next((i for i, line in enumerate(lines) if line.startswith(("figures ", "system "))), None)
            if [lines[i] for i in counts] != ["parsed m1b: 2 of 3", "parsed m1b@medium: 3 of 4"] or figure is None or max(counts) > figure:
                return f"the parsed counts do not all precede the first figure: {lines!r}"
            if "paired 2 of 3 · m1b unanswered c" not in "\n".join(lines):
                return f"the unparsed reply was scored: {lines!r}"
            undeclared, over = derive_fixture_manifest(tmp), derive_fixture_manifest(tmp)
            del undeclared["arms"][1]["dispatched"]
            over["arms"][0]["dispatched"] = 1
            return (check_refused(lambda: check_experiment(undeclared), "arm m1b@medium", "dispatched")
                    or check_refused(lambda: check_experiment(over), "arm m1b", "2 parsed against 1 dispatched"))

    def check_judge_arm():
        with tempfile.TemporaryDirectory() as tmp:
            key = pathlib.Path(tmp, "key.json")
            key.write_text(json.dumps(EXPERIMENT_KEY), encoding="utf-8")
            manifest = derive_fixture_manifest(tmp, judge={"verdicts": "judge2", "key": str(key)})
            lines = check_experiment(manifest)
            if not any(line.startswith("labels rotated — checked: 2 arm(s) over 3 case(s)") for line in lines):
                return f"a rotating key did not read checked: {lines!r}"
            if "labels rotated — recorded, not checked: no committed key" not in check_experiment(derive_fixture_manifest(tmp)):
                return "a null key did not print as recorded"
            key.write_text(json.dumps({c: {"ARM-A": "m1b", "ARM-B": "m1b@medium"} for c in EXPERIMENT_KEY}), encoding="utf-8")
            return check_refused(lambda: check_experiment(manifest), "arm m1b", "ARM-A", "every one of 3")

    def check_union_arm():
        with tempfile.TemporaryDirectory() as tmp:
            held, _, _ = derive_frozen_repo(tmp)
            manifest = derive_fixture_manifest(tmp, heldOut=str(held), union={"tuning": ["m1b", "m1b@medium"], "heldOut": ["m1b"]})
            text = "\n".join(check_experiment(manifest, tmp))
            want = ["system tuning 2/2 · m1b + m1b@medium", "system held-out 1/1 · m1b", "system pooled 3/3 · tuning + held-out"]
            bad = next((f"{w!r} not in {text!r}" for w in want if w not in text), None)
            if bad:
                return bad
            why = check_refused(lambda: check_experiment({**manifest, "union": {"tuning": ["m1b"]}}, tmp), "union", "heldOut")
            if why:
                return why
        if top is None:
            return no_tree
        proof = {"instance": "scouted-seam", "cases": f"{UNION_PROOF_COMMIT}:{PROOF_DIR}3-cases.json",
                 "results": f"{UNION_PROOF_COMMIT}:{PROOF_DIR}5-results.json", "heldOut": str(top / HELD_OUT_FILE),
                 "arms": [{"name": a, "base": None, "settings": {"prompt": a}, "dispatched": n}
                          for a, n in (("m1cA@medium", 30), ("t1r@medium", 35), ("m1c@medium", 12))],
                 "judge": {"verdicts": "judge2", "key": None},
                 "union": {"tuning": ["m1cA@medium", "t1r@medium"], "heldOut": ["m1c@medium", "t1r@medium"]}}
        text = "\n".join(check_experiment(proof, top))
        want = ["system tuning 21/23 ·", "system held-out 12/12 ·", "system pooled 33/35 ·"]
        return next((f"{w!r} not in {text!r}" for w in want if w not in text), None)

    arms = [("paired-refuses", check_paired_refuses), ("row-refuses", check_row_refuses), ("tag-section", check_tag_section),
            ("instances", check_instances_arm), ("scouted-proof", check_scouted_proof), ("conformance", check_conformance),
            ("deterministic", check_deterministic), ("experiment-evidence", check_evidence_arm),
            ("experiment-freeze", check_freeze_arm), ("experiment-variable", check_variable_arm),
            ("experiment-parsed", check_parsed_arm), ("experiment-judge", check_judge_arm), ("experiment-union", check_union_arm)]
    passed = skipped = ran = 0
    for name, arm in arms:
        ran += 1
        try:
            why = arm()
        except Exception as exc:  # an arm that crashes is a red arm, never a dead runner
            why = f"raised {exc!r}"
        if isinstance(why, tuple):
            print(f"SKIP {name}: {why[1]}")
            skipped += 1
            continue
        print(f"ok {name}" if why is None else f"FAIL {name}: {why}")
        passed += why is None
    print(f"replay_scorer selftest: {passed}/{ARMS_DECLARED} arms" + (f" · {skipped} skipped" if skipped else ""))
    if ran != ARMS_DECLARED:
        print(f"FAIL replay_scorer selftest: {ran} arm(s) ran against {ARMS_DECLARED} declared")
    return 0 if passed + skipped == ran == ARMS_DECLARED else 1


def main(argv):
    ap = argparse.ArgumentParser(prog="replay_scorer.py", description="Score committed replay outputs through one instance.")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--instance", metavar="KEY")
    ap.add_argument("--cases", metavar="SRC")
    ap.add_argument("--results", metavar="SRC")
    verbs = ap.add_mutually_exclusive_group()
    verbs.add_argument("--grade", metavar="ARM")
    verbs.add_argument("--compare", nargs="+", metavar="ARM")
    verbs.add_argument("--judged", nargs="+", metavar="ARM")
    ap.add_argument("--known", metavar="SRC")
    ap.add_argument("--candidate", metavar="SRC")
    ap.add_argument("--window", type=int, default=10)
    ap.add_argument("--experiment", metavar="SRC")
    ap.add_argument("--repo", default=".")
    args = ap.parse_args(argv)
    if args.selftest:
        return run_selftest()
    if args.experiment:
        # Every line is derived before the first prints, so a refusal leaves no figure on stdout.
        try:
            try:
                manifest = json.loads(read_raw_output(args.experiment, args.repo))
            except ValueError as exc:
                raise Refusal(f"manifest {args.experiment}: not JSON ({exc})") from None
            lines = check_experiment(manifest, args.repo)
        except Refusal as exc:
            print(f"replay_scorer: REFUSED — {exc}", file=sys.stderr)
            return 2
        print("\n".join(lines))
        return 0
    instance = INSTANCES.get(args.instance)
    if instance is None:
        ap.error(f"--instance must name one of {', '.join(INSTANCES)}, not {args.instance!r}")
    try:
        if args.instance == "scouted-seam":
            verb = next((v for v in ("grade", "compare", "judged") if getattr(args, v)), None)
            if not (args.cases and args.results and verb):
                ap.error("scouted-seam needs --cases, --results and one of --grade, --compare or --judged")
            corpus, results = read_scouted_population(args.cases, args.results, args.repo)
            print("\n".join(instance["measure"][verb](corpus, results, getattr(args, verb))))
            return 0
        if not (args.known and args.candidate):
            ap.error("review-replay needs --known and --candidate")
        if args.window < 0:
            ap.error("--window must be 0 or more")
        known_text = read_raw_output(args.known, args.repo)
        cand_text = read_raw_output(args.candidate, args.repo)
    except Refusal as exc:
        print(f"replay_scorer: REFUSED — {exc}", file=sys.stderr)
        return 2
    replay, refusal = instance["measure"](known_text, cand_text, args.window)
    if refusal:
        side, err = refusal
        print(f"replay_scorer: REFUSED {side} {args.known if side == 'known' else args.candidate} — {err}", file=sys.stderr)
        return 2
    # The printer stays in the instance's adapter (it imports this module), so it is imported here, at use.
    from review_replay import print_score
    print_score(args.known, replay["known"], args.candidate, replay["candidates"], replay["window"], replay["score"], replay["mode"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
