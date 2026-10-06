#!/usr/bin/env python3
# **Serves:** journal TOOL-aMendedFleet-71
#
# The instrument behind this unit's sweep: every sentence in a code comment that carries a COUNT and
# a PRESENT-TENSE marker and is not FROZEN by its conditions. ANNOTATION-STYLE A3 bans a present-tense
# count of a live derived population in a comment; A4 names the three dispositions that make a number
# safe. This lists the candidates. It decides nothing: a human reads each and records a disposition in
# the record beside it. It is a research instrument run by hand, never a gate (A1 records why).
#
#     python memory/builds/aMendedFleet/build/2026-10-06-build-TOOL-aMendedFleet-71-1-count-census.py
#     python memory/builds/aMendedFleet/build/2026-10-06-build-TOOL-aMendedFleet-71-1-count-census.py --selftest
#
# Comments are folded into paragraphs before sentences are split, because a line-wise grep misses a
# count whose marker wraps onto the next line, which is exactly the shape of the example that started
# this unit. Python docstrings are read through `ast`, not by pattern.
#
# LIVENESS: every population is printed with its size, product and test apart, and a walk that read
# no file of a kind exits 1 as a DEAD PROBE rather than printing an empty, clean-looking list.
import ast
import os
import re
import subprocess
import sys

ROOTS = ("tools/", "skills/", ".githooks/")
EXTS = (".sh", ".py", ".js")

# A digit run not glued to an identifier, a version, an anchor, a section, a path, a variable or a
# brace. Number words and `none` stand alone; `every` and `no` count only before a following word.
# ponytail: "before a noun" is approximated as "before a word"; a part-of-speech tagger is the upgrade.
COUNT_RE = re.compile(
    r"(?<![\w\-.#§/${])\d+"
    r"|\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen"
    r"|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|none)\b"
    r"|\b(?:every|no)\s+[A-Za-z]",
    re.I,
)
PRESENT_RE = re.compile(r"\b(?:today|currently|at present|right now)\b", re.I)
# The three markers spec rev-3 dropped. In this tree `now` narrates a change ("the check now
# refuses") and `live` and `tracked` name a population in a RULE ("every tracked file"), so with them
# the predicate printed more sentences than a sweep can read. The census still counts what they would
# add, as `wide-only`, so the narrowing is visible on every run rather than recorded once.
WIDE_RE = re.compile(r"\b(?:now|live|tracked)\b", re.I)
# `measured` alone does not freeze: "measured today" is the defect, not its cure. The hex arm and
# PINNED are case-sensitive on purpose: a sha is lowercase, and a case-blind arm would freeze any
# seven-letter word spelled from a to f.
FROZEN_RE = re.compile(
    r"\b\d{4}-\d{2}-\d{2}\b|\b[0-9a-f]{7,40}\b|\bnode\s+`?[a-z]\b|PINNED|(?i:\bat review\b|\bat base\b)"
)


def check_test_path(p):
    """A file whose comments describe a fixture's world rather than the product's, kept apart in the
    output. The same generous predicate as aKeyedAnnotation's citation census."""
    return ".test." in p or "selftest" in p or os.path.basename(p).startswith("test_")


def check_frozen(sentence):
    """True when the sentence carries its own conditions: a date, a sha, a node, a pin or a base."""
    return FROZEN_RE.search(sentence) is not None


def read_comment_blocks(path, text):
    """Paragraphs as lists of (line number, text): runs of full-line comments, and Python docstrings
    split on blank lines. A blank comment line or a code line ends a paragraph."""
    lang = "py" if path.endswith(".py") else "js" if path.endswith(".js") else "sh"
    if lang == "sh" and not path.endswith(".sh") and "python" in text.split("\n", 1)[0]:
        lang = "py"
    paras, cur, in_block = [], [], False
    for n, raw in enumerate(text.split("\n"), 1):
        line = raw.strip()
        body = None
        if lang == "js":
            if in_block or line.startswith("/*"):
                in_block = "*/" not in line
                body = re.sub(r"^/\*+|\*+/$|^\*+", "", line).strip()
            elif line.startswith("//"):
                body = line[2:].strip()
        elif line.startswith("#") and not line.startswith("#!"):
            body = line[1:].strip()
        if body:
            cur.append((n, body))
        elif cur:
            paras.append(cur)
            cur = []
    if cur:
        paras.append(cur)
    if lang == "py":
        try:
            tree = ast.parse(text)
        except (SyntaxError, ValueError):
            return paras
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                continue
            first = node.body[0] if node.body else None
            if not (isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant)
                    and isinstance(first.value.value, str)):
                continue
            cur = []
            for i, dl in enumerate(first.value.value.split("\n")):
                if dl.strip():
                    cur.append((first.value.lineno + i, dl.strip()))
                elif cur:
                    paras.append(cur)
                    cur = []
            if cur:
                paras.append(cur)
    return paras


def derive_sentences(para):
    """(line, sentence) pairs: the paragraph joined, split after `.` or `;` followed by space, each
    sentence placed on the line it starts on."""
    joined, starts = "", []
    for n, t in para:
        starts.append((len(joined), n))
        joined += t + " "
    out, pos = [], 0
    for piece in re.split(r"(?<=[.;])\s+", joined):
        line = max(n for off, n in starts if off <= joined.find(piece, pos)) if piece.strip() else 0
        pos = joined.find(piece, pos) + len(piece)
        if piece.strip():
            out.append((line, piece.strip()))
    return out


def derive_candidates(sentences):
    """Split (line, sentence) pairs into (candidates, frozen near-misses, wide-only count)."""
    cand, near, wide = [], [], 0
    for line, s in sentences:
        if not COUNT_RE.search(s):
            continue
        if PRESENT_RE.search(s):
            (near if check_frozen(s) else cand).append((line, s))
        elif WIDE_RE.search(s) and not check_frozen(s):
            wide += 1
    return cand, near, wide


def check_selftest():
    markers = ["today", "currently", "at present", "right now"]
    fails = 0
    for m in ("now", "live", "tracked"):
        cand, _, wide = derive_candidates([(1, f"Three specs carry the row {m}.")])
        if cand or wide != 1:
            print(f"FAIL wide marker {m!r} is a candidate or uncounted: {cand} wide {wide}")
            fails += 1
    for m in markers:
        cand, near, _ = derive_candidates([
            (1, f"Three specs carry the row {m}."),
            (2, f"Three specs carried the row {m} on 2026-10-04."),
        ])
        if [c[0] for c in cand] != [1] or [x[0] for x in near] != [2]:
            print(f"FAIL marker {m!r}: candidates {cand} near {near}")
            fails += 1
    for frozen in ("at 7af5f564", "on node a", "PINNED", "at review", "at base"):
        cand, near, _ = derive_candidates([(1, f"Every spec agrees today, {frozen}.")])
        if cand or len(near) != 1:
            print(f"FAIL freeze {frozen!r}: candidates {cand} near {near}")
            fails += 1
    for not_count in ("Rule #3 holds today.", "Version v1.2 holds today.", "The $1 arg holds today."):
        if derive_candidates([(1, not_count)])[0]:
            print(f"FAIL not-a-count reported: {not_count!r}")
            fails += 1
    if derive_candidates([(1, "Measured 277 specs today.")])[0] == []:
        print("FAIL `measured` alone froze a sentence")
        fails += 1
    wrapped = read_comment_blocks("x.sh", "# Zero of 277 tracked specs\n# disagree today.\nx=1\n")
    if derive_candidates(derive_sentences(wrapped[0]))[0] != [(1, "Zero of 277 tracked specs disagree today.")]:
        print(f"FAIL wrapped count not folded: {wrapped}")
        fails += 1
    doc = read_comment_blocks("x.py", 'def f():\n    """None does today.\n\n    Other."""\n')
    if [s for p in doc for s in derive_sentences(p)][:1] != [(2, "None does today.")]:
        print(f"FAIL docstring not read: {doc}")
        fails += 1
    print("selftest:", "FAIL" if fails else "ok", f"({fails} failing)")
    return 1 if fails else 0


def main(argv):
    if "--selftest" in argv:
        return check_selftest()
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                          encoding="utf-8").stdout.strip()
    tracked = subprocess.run(["git", "ls-files", "--", *ROOTS], capture_output=True, text=True,
                             encoding="utf-8", cwd=root).stdout.split("\n")
    files, kinds = [], {"sh": 0, "py": 0, "js": 0, "hook": 0}
    for p in tracked:
        if not p or "fixture" in p:
            continue
        base = os.path.basename(p)
        if p.endswith(EXTS):
            kind = p.rsplit(".", 1)[1]
        elif "." not in base:
            try:
                with open(os.path.join(root, p), encoding="utf-8", errors="replace") as fh:
                    if not fh.readline().startswith("#!"):
                        continue
            except OSError:
                continue
            kind = "hook"
        else:
            continue
        files.append(p)
        kinds[kind] += 1
    # files, paragraphs, candidates, near-misses, wide-only
    pop = {"product": [0, 0, 0, 0, 0], "test": [0, 0, 0, 0, 0]}
    cands, nears = [], []
    for p in files:
        split = "test" if check_test_path(p) else "product"
        # newline="" because a bare CR is a line break to universal-newline mode and not to git,
        # and one shell file here holds raw CR bytes: without it every line after the first is off.
        with open(os.path.join(root, p), encoding="utf-8", errors="replace", newline="") as fh:
            paras = read_comment_blocks(p, fh.read())
        sentences = [s for para in paras for s in derive_sentences(para)]
        cand, near, wide = derive_candidates(sentences)
        pop[split][0] += 1
        pop[split][1] += len(paras)
        pop[split][2] += len(cand)
        pop[split][3] += len(near)
        pop[split][4] += wide
        cands += [(p, ln, s, split) for ln, s in cand]
        nears += [(p, ln, s, split) for ln, s in near]
    print("== candidates ==")
    for p, ln, s, _ in sorted(cands):
        print(f"{p}:{ln}: {s}")
    print("== frozen near-misses ==")
    for p, ln, s, _ in sorted(nears):
        print(f"{p}:{ln}: {s}")
    print("== populations ==")
    print("files by kind: " + " · ".join(f"{k} {v}" for k, v in kinds.items()))
    for split, (f, para, c, n, w) in pop.items():
        print(f"{split}: files {f} · paragraphs {para} · candidates {c} · near-misses {n} · wide-only {w}")
    dead = [k for k, v in kinds.items() if v == 0]
    if dead:
        print("DEAD PROBE — no file of kind " + ", ".join(dead) + " was read")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
