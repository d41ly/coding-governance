#!/usr/bin/env python3
# **Serves:** research TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6
# **Commissions:** TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6
"""prose-census — measure byte pressure and cross-document redundancy over this repo's
load-bearing governing prose.

    python memory/builds/aHonedRuleset/build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py

Run from the repo root. Stdlib only, no network, seconds.

WHY A SCRIPT AND NOT A TABLE IN THE REPORT. The charter forbids writing a count of a derived
population in prose (§7): a number typed beside the thing it counts is wrong on the next commit and
nobody notices. Every figure the census report cites is emitted here, so re-running it is the whole
verification. The report carries only judgment.

WHAT IT DOES NOT CHECK. It measures textual overlap and declared ceilings. It cannot tell a
duplicated RULE from a duplicated turn of phrase, and it cannot see a fact restated in different
words — the `two-answers-to-one-question` class that costs the most is exactly the one a shingle
matcher is blind to. A pair reported at 0 shared bytes is not a pair with no duplicated meaning.
"""

import os
import re
import sys
from collections import defaultdict

# --- the corpus: a DECLARED population, one row per file, reason attached -------------------------
# Declared rather than globbed because "load-bearing governing prose" is a judgement, not a path
# pattern. A file added to tools/ does not silently join the census, and a row naming a file that
# stopped existing is a refusal below, not a silent shrink.
CORPUS = [
    # the six the owner named, at their AUTHORED source (templates, where one exists)
    ("tools/memory-tree/BUILD-METHOD.template.md",        "BUILD-METHOD, authored"),
    ("tools/unattended/PLAYBOOK-TEMPLATE.template.md",    "PLAYBOOK-TEMPLATE, authored"),
    ("tools/workflows/REVIEW-PROTOCOL.template.md",       "REVIEW-PROTOCOL, authored"),
    ("tools/unattended/PROTOCOL.template.md",             "UNATTENDED-PROTOCOL, authored"),
    ("tools/unattended/VERBS.template.md",                "UNATTENDED-VERBS, authored"),
    ("memory/guides/SESSION-KICKOFF.md",                  "SESSION-KICKOFF, this repo's kickoff manifest (no template)"),
    ("skills/session-kickoff/SKILL.md",                   "the kickoff engine"),
    ("skills/session-kickoff/MANIFEST-TEMPLATE.md",       "the manifest an adopter fills"),
    # the ruleset itself
    ("coding-governance-agents.template.md",              "the governance charter template"),
    # the remaining live kit templates
    ("tools/memory-tree/HYGIENE.template.md",             "the memory-tree hygiene catalog"),
    ("tools/memory-tree/SPEC-TEMPLATE.template.md",       "the spec format"),
    ("tools/unattended/SKILL.template.md",                "the unattended skill"),
    ("tools/drift-audit/SKILL.template.md",               "the drift-audit skill"),
    ("tools/lexicon/SKILL.template.md",                   "the lexicon skill"),
    ("tools/memory-recall/SKILL.template.md",             "the memory-recall skill"),
    # the runbook: named by TOOL-aScouredKit-23 as the largest uncapped instruction doc
    ("WIRE-INTO-PROJECT.md",                              "the adopter runbook"),
]

# Rendered copies. NOT censused for redundancy — each is byte-identical to its template modulo
# placeholder substitution, so counting it would double every shared run. Measured for size only,
# because a ceiling binds the RENDERED path and not the template it came from.
RENDERED = [
    ("memory/guides/BUILD-METHOD.md",        "tools/memory-tree/BUILD-METHOD.template.md"),
    ("memory/guides/PLAYBOOK-TEMPLATE.md",   "tools/unattended/PLAYBOOK-TEMPLATE.template.md"),
    ("memory/guides/REVIEW-PROTOCOL.md",     "tools/workflows/REVIEW-PROTOCOL.template.md"),
    ("memory/guides/UNATTENDED-PROTOCOL.md", "tools/unattended/PROTOCOL.template.md"),
    ("memory/guides/UNATTENDED-VERBS.md",    "tools/unattended/VERBS.template.md"),
    ("memory/HYGIENE.md",                    "tools/memory-tree/HYGIENE.template.md"),
    ("memory/TEMPLATE-SPEC.md",              "tools/memory-tree/SPEC-TEMPLATE.template.md"),
    (".claude/skills/unattended/SKILL.md",   "tools/unattended/SKILL.template.md"),
    (".claude/skills/drift-audit/SKILL.md",  "tools/drift-audit/SKILL.template.md"),
    (".claude/skills/lexicon/SKILL.md",      "tools/lexicon/SKILL.template.md"),
    (".claude/skills/memory-recall/SKILL.md", "tools/memory-recall/SKILL.template.md"),
    ("AGENTS.md",                            "coding-governance-agents.template.md"),
]

K = 8          # shingle width in words. Below ~6 ordinary English collocations match everything.
MIN_RUN = 12   # a reported run must be at least this many words — shorter is a phrase, not a rule.


def read(path):
    """Binary read, explicit decode. A text-mode read eats a bare CR and the byte count then
    disagrees with every gate that measures the file."""
    with open(path, "rb") as fh:
        raw = fh.read()
    return raw, raw.decode("utf-8")


# --- ceilings ------------------------------------------------------------------------------------
# Resolved from the files that OWN them. Nothing here is typed: a ceiling spelled in this script
# would be a fourth carrier of a number three files already argue about.

def load_declared_ceilings():
    """tools/template-size-limits.txt — `<path>\\t<bytes>`, comments are lines with no tab."""
    out = {}
    p = "tools/template-size-limits.txt"
    if not os.path.exists(p):
        return out
    for line in read(p)[1].splitlines():
        if "\t" not in line:
            continue
        path, _, val = line.partition("\t")
        out[path.strip()] = int(val.strip())
    return out


def load_guide_cap():
    """GUIDE_CAP_BYTES / GUIDE_CAP_LINES: the gate's default, then any .memory-tree.conf override.
    Read in that order because the conf is what the gate reads last."""
    # finditer, not match: the gate declares both knobs on ONE line separated by `;`, so an
    # anchored pattern silently reports the second as absent.
    caps = {}
    pat = re.compile(r'\b(GUIDE_CAP_(?:BYTES|LINES))="?(\d+)"?')
    for path in ("tools/memory-tree/check-memory-hygiene.sh", ".memory-tree.conf"):
        if not os.path.exists(path):
            continue
        for line in read(path)[1].splitlines():
            if line.lstrip().startswith("#"):
                continue
            for m in pat.finditer(line):
                caps[m.group(1)] = int(m.group(2))
    return caps.get("GUIDE_CAP_BYTES"), caps.get("GUIDE_CAP_LINES")


def load_prose_budgets():
    """Budgets a document declares about ITSELF, in its own prose, enforced by no gate.

    Found by reading, not by pattern — a self-declared budget is a sentence, and the two live
    instances spell theirs differently. They are resolved here rather than typed because the
    NUMBER still comes out of the file: the row names the file and the regex, and a budget that is
    edited away stops being reported instead of silently persisting as a stale constant.
    """
    rows = {
        # BUILD-METHOD sets its own stricter budget so that M7 can re-read it whole at every pass
        # boundary. Its own line 16 says "No gate enforces the pair".
        "tools/memory-tree/BUILD-METHOD.template.md": r"Budget:\s*≤\s*(\d+)\s*KB",
    }
    out = {}
    for path, pat in rows.items():
        if not os.path.exists(path):
            continue
        m = re.search(pat, read(path)[1])
        if m:
            out[path] = int(m.group(1)) * 1024
    return out


def ceiling_for(path, declared, guide_bytes, prose):
    if path in declared:
        return declared[path], "template-size-limits.txt"
    if path in prose:
        return prose[path], "PROSE (ungated)"
    if path.startswith("memory/guides/") and guide_bytes:
        return guide_bytes, "GUIDE_CAP_BYTES"
    return None, None


# --- shingling -----------------------------------------------------------------------------------

WORD = re.compile(r"[A-Za-z0-9_.:/-]+")


def words_of(text):
    """Words with their byte offsets. Markdown emphasis and backticks are dropped so a rule quoted
    with different decoration still matches itself."""
    stripped = re.sub(r"[`*_>#|]", " ", text)
    return [(m.group(0).lower(), m.start()) for m in WORD.finditer(stripped)]


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def runs_between(wa, wb, shared):
    """Maximal (start_a, start_b, length) runs of ≥ MIN_RUN words common to both, greedy and
    non-overlapping in A."""
    idx_b = defaultdict(list)
    for j, (w, _) in enumerate(wb):
        idx_b[w].append(j)
    out, i = [], 0
    while i < len(wa):
        if wa[i][0] not in shared:
            i += 1
            continue
        best = (0, -1)
        for j in idx_b[wa[i][0]]:
            n = 0
            while i + n < len(wa) and j + n < len(wb) and wa[i + n][0] == wb[j + n][0]:
                n += 1
            if n > best[0]:
                best = (n, j)
        if best[0] >= MIN_RUN:
            out.append((i, best[1], best[0]))
            i += best[0]
        else:
            i += 1
    return out


def main():
    root_missing = [p for p, _ in CORPUS if not os.path.exists(p)]
    if root_missing:
        # vacuous-selector class: a census that silently skips its subjects reports a clean corpus.
        sys.exit("REFUSED — declared corpus rows name files that do not exist:\n  " + "\n  ".join(root_missing))

    declared = load_declared_ceilings()
    prose = load_prose_budgets()
    guide_b, guide_l = load_guide_cap()

    docs = {}
    for path, why in CORPUS:
        raw, text = read(path)
        docs[path] = {"why": why, "raw": raw, "text": text, "words": words_of(text)}

    print("# prose-census — TOOL-aHonedRuleset-1")
    print(f"# corpus {len(CORPUS)} authored + {len(RENDERED)} rendered · shingle k={K} · min run {MIN_RUN} words")
    print(f"# GUIDE_CAP_BYTES={guide_b} GUIDE_CAP_LINES={guide_l} · declared ceilings: {len(declared)}"
          f" · prose budgets: {len(prose)}")

    # --- 1. size and pressure ---------------------------------------------------------------------
    print("\n## 1. size and pressure (every measured file, authored + rendered)")
    print(f"{'bytes':>7} {'lines':>6} {'ceiling':>8} {'pct':>6} {'free':>7}  source            path")
    rows = [(p, None) for p, _ in CORPUS] + RENDERED
    measured = []
    for path, _src in rows:
        if not os.path.exists(path):
            print(f"{'MISSING':>7} {'':>6} {'':>8} {'':>6} {'':>7}  -                 {path}")
            continue
        raw, text = read(path)
        cap, src = ceiling_for(path, declared, guide_b, prose)
        n = len(raw)
        lines = text.count("\n") + (0 if text.endswith("\n") else 1)
        pct = f"{100.0 * n / cap:.1f}%" if cap else "-"
        free = str(cap - n) if cap else "-"
        measured.append((path, n, lines, cap))
        print(f"{n:>7} {lines:>6} {(cap or '-'):>8} {pct:>6} {free:>7}  {(src or 'NONE'):<17} {path}")

    uncapped = [(p, n) for p, n, _, c in measured if c is None]
    uncapped.sort(key=lambda r: -r[1])
    print(f"\n# uncapped: {len(uncapped)} of {len(measured)} measured files have no declared ceiling.")
    for p, n in uncapped[:5]:
        print(f"#   {n:>7} B  {p}")

    # --- 2. cross-document overlap ----------------------------------------------------------------
    print("\n## 2. cross-document overlap (authored corpus only; rendered copies excluded)")
    shingles = {}
    for path, d in docs.items():
        ws = [w for w, _ in d["words"]]
        shingles[path] = {tuple(ws[i:i + K]) for i in range(len(ws) - K + 1)}

    paths = [p for p, _ in CORPUS]
    pairs = []
    for a_i in range(len(paths)):
        for b_i in range(a_i + 1, len(paths)):
            a, b = paths[a_i], paths[b_i]
            common = shingles[a] & shingles[b]
            if not common:
                continue
            shared_words = {w for sh in common for w in sh}
            rs = runs_between(docs[a]["words"], docs[b]["words"], shared_words)
            if not rs:
                continue
            cost = 0
            for i, _j, n in rs:
                s = docs[a]["words"][i][1]
                e_w, e_o = docs[a]["words"][i + n - 1]
                cost += (e_o + len(e_w)) - s
            pairs.append((cost, sum(n for _, _, n in rs), len(rs), max(n for _, _, n in rs), a, b, rs))

    pairs.sort(reverse=True, key=lambda r: r[0])
    print(f"{'bytes':>7} {'words':>6} {'runs':>5} {'max':>5}  pair")
    for cost, words, nruns, longest, a, b, _ in pairs:
        print(f"{cost:>7} {words:>6} {nruns:>5} {longest:>5}  {a}\n{'':>27}  {b}")
    if not pairs:
        print("(none above the threshold)")

    total = sum(p[0] for p in pairs)
    print(f"\n# overlap total {total} B across {len(pairs)} pair(s) of {len(paths) * (len(paths) - 1) // 2} possible.")

    # --- 3. the longest shared passages, with both locations --------------------------------------
    print(f"\n## 3. longest shared passages (top 20, ≥{MIN_RUN} words)")
    flat = []
    for cost, _w, _n, _l, a, b, rs in pairs:
        for i, j, n in rs:
            flat.append((n, a, i, b, j))
    flat.sort(reverse=True, key=lambda r: r[0])
    for n, a, i, b, j in flat[:20]:
        wa, wb = docs[a]["words"], docs[b]["words"]
        s, e_w, e_o = wa[i][1], wa[i + n - 1][0], wa[i + n - 1][1]
        snippet = " ".join(w for w, _ in wa[i:i + min(n, 18)])
        print(f"\n{n:>4} words  {a}:{line_of(docs[a]['text'], s)}")
        print(f"{'':>10}  {b}:{line_of(docs[b]['text'], wb[j][1])}")
        print(f"{'':>10}  {snippet}{' …' if n > 18 else ''}")
        del e_w, e_o

    # --- 4. typed magnitudes in prose --------------------------------------------------------------
    # The charter's own §7: "NO count of a derived population is written in prose. The checker
    # derives every figure it reports; a number typed beside the thing it counts is wrong on the
    # next commit and nobody notices." This is the cheapest mechanical proxy for the restatement
    # class section 2 is blind to — a sentence carrying a magnitude is a sentence some file owns.
    #
    # HEAVILY over-inclusive on purpose: version numbers, dates, ids and byte figures inside a
    # justification are all legitimate. The output is a CANDIDATE list to read, never a verdict, and
    # the report says which candidates survived reading.
    print("\n## 4. typed magnitudes in prose (candidates for the derive-don't-type rule)")
    mag = re.compile(r"(?<![\w.-])(?:\d{1,3}(?:,\d{3})+|\d+)\s*"
                     r"(?:B\b|KiB|KB|bytes?|lines?|seconds?|s\b|checks?|legs?|rows?|files?|items?|"
                     r"agents?|words?|sections?|copies|carriers?|places?)")
    spelled = re.compile(r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
                         r"twenty|thirty|forty|fifty|sixty|seventy|ninety)\s+"
                         r"(?:checks?|legs?|rows?|files?|items?|agents?|sections?|copies|carriers?|"
                         r"places?|of\s+the)\b", re.I)
    hits = []
    for path, d in docs.items():
        fenced, n_here = False, 0
        for ln, line in enumerate(d["text"].splitlines(), 1):
            if line.lstrip().startswith("```"):
                fenced = not fenced
                continue
            if fenced:
                continue
            if mag.search(line) or spelled.search(line):
                n_here += 1
                hits.append((path, ln, line.strip()))
        if n_here:
            print(f"{n_here:>4}  {path}")
    print(f"\n# {len(hits)} candidate line(s) across {len({h[0] for h in hits})} file(s).")
    if "--magnitudes" in sys.argv:
        for path, ln, line in hits:
            print(f"{path}:{ln}: {line[:150]}")

    # --- 5. section weight, for the files with no room left ----------------------------------------
    # A cut list ranked by anything but the size of what it proposes to cut is a wish list. Sections
    # are `## ` headings; a file whose top level is `#` only reports one row, which is the honest
    # answer for a document that is not sectioned.
    print("\n## 5. section weight (files at ≥95% of a ceiling)")
    for path, n, _lines, cap in measured:
        if not cap or n / cap < 0.95:
            continue
        text = read(path)[1]
        secs, cur, start = [], None, 0
        lines_ = text.splitlines(keepends=True)
        off = 0
        for line in lines_:
            if line.startswith("## "):
                if cur is not None:
                    secs.append((cur, off - start))
                cur, start = line.strip(), off
            off += len(line.encode("utf-8"))
        if cur is not None:
            secs.append((cur, off - start))
        print(f"\n{path} — {n} B of {cap} ({cap - n} free)")
        for name, size in sorted(secs, key=lambda r: -r[1])[:8]:
            print(f"{size:>7} B  {name[:88]}")


if __name__ == "__main__":
    main()
