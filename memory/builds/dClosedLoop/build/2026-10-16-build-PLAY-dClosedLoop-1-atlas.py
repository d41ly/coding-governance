# **Serves:** research PLAY-dClosedLoop-1
"""Derive the Closed Loop Atlas from dClosedLoop's records, and write the publishable page.

Usage: python 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py [--ref <rev>] [--claims cache|none] --out <page.html>
       python 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py [--ref <rev>] [--claims cache|none] --check
       python 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check --plant <case>   damage the memory view's sources,
           the record corpus, the view map, the chain state or the as-built view, expect exit 1; cases:
           kind-unplaced, kind-ghost-tag, edge-status, hop-edge, edges-split, instruments-decision, view-unread,
           state-dropped, asbuilt-dropped
       python 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check --page <page.html> [--ref <rev>]
           answer whether the tree at --ref (default HEAD) has moved an input the page was stamped with:
           exit 0 current; 1 stale, dirty, unstamped or absent; 2 a misuse, a ref that does not resolve or a
           failed git call, with one `atlas: cannot check:` line on stderr

The template beside this file is the page without its data. A run splices the derived data into a copy
written to --out, never into the template, so the repository keeps the template and this generator while
the page, which embeds every record, stays out of it. --check derives everything and writes nothing.

--out stamps the page (TOOL-dTrackedAtlas-3): the data's `stamp` holds the commit the chain state was read
at, the tracked inputs (dClosedLoop's README, build and reviews folders, .memory-tree.conf,
TOOL-dTrackedAtlas-1's module and one folder per chain build), the SHA-256 of `git ls-tree -r -z` over
them at that commit, and the inputs the working tree differs in. --check --page derives nothing: it hashes
the stamped inputs at --ref, with each chain build's landing merges read against the stamp's default_ref
(TOOL-dTrackedAtlas-10), and compares, so a page reads stale when an input or a landing it shows moved,
never because the commit alone did. It does not see run claims, the code under tools/ the derivation
reuses, a hand edit to the page, or whether the default-branch ref is current with its remote, since
nothing is fetched.

The page shows the chain's actual state (TOOL-dTrackedAtlas-2): TOOL-dTrackedAtlas-1's state document of every
chain build, read through git at --ref (default HEAD), and the as-built view's clauses, read from the working
tree as every record is. --claims cache (the default) reads the claim cache `unattended.sh --claims` fills, so a
live claim's staleness can change between two renders at one ref; --claims none reads no claim, and only then is
the page byte-identical across runs at one ref. The 2026-10-14 measurements stay on the page as the baseline.

Nothing the records hold may leave the atlas without a refusal:
- every table it reads parses whole, and each population is counted against the raw lines that carry it;
- every record splits into sections that rejoin to its exact text;
- every gap stage maps to one comparison area, and every source an area names resolves;
- every design record that records an owner's answer contributes a decision section.
"""
import fnmatch
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILD = HERE.parent
REPO = BUILD.parents[2]
REVIEWS = BUILD / "reviews"
TEMPLATE = HERE / "2026-10-16-build-PLAY-dClosedLoop-1-atlas.html"
MARK = '<script id="atlas-data" type="application/json">'
PREFIX = "-build-PLAY-dClosedLoop-1-"


def record(name):
    found = sorted(HERE.glob(f"*{PREFIX}{name}.md"))
    if len(found) != 1:
        sys.exit(f"atlas: {len(found)} records named {name}")
    return found[0]


SOURCES = {key: record(name) for key, name in {
    "v2": "architecture-v2", "gaps": "gap-register", "steps": "flow-steps", "roles": "layer-roles",
    "instruction": "layer-instruction", "library": "layer-library", "memory": "layer-memory",
    "expansions": "layer-expansions", "fates": "fates", "plan": "memory-plan"}.items()}
LAYER_RECORDS = {
    "instruction": ["layer-instruction"],
    "flow": ["layer-flow", "flow-steps", "flow-roles"],
    "roles": ["layer-roles"],
    "memory": ["layer-memory", "layer-library"],
    "runtime": ["layer-runtime"],
    "observability": ["layer-expansions"],
    "integrations": ["layer-expansions"],
    "distribution": ["layer-expansions"],
    # Two designs outside the eight layers, each audited on its own record. Their rows are keyed by no
    # layer tag, so the progress view draws them apart from the layers.
    "lexicon": ["lexicon"],
    "review system": ["review-system"],
}
STEPS = ["entry", "plan", "design", "build", "test", "deploy", "breakpoint", "probe", "lifecycle", "adopt"]
KINDS = ("command", "executor", "hook", "owner")
SEP = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")
ITEM_TAG = re.compile(r"`([a-z]+\.[a-z0-9-]+)`")
GAP_ID = re.compile(r"gap-[a-z]+-\d\d")

# The comparison of today's product with the target, one area at a time. Each names the measured
# sections that describe today, the register stages whose gaps are the change, and what the target is.
AREAS = [
    {"key": "instruction", "title": "Instruction", "layer": "instruction", "stages": ["Foundation"],
     "today": [("layer-instruction", "current")], "target": {"layer": "instruction"}},
    {"key": "entry", "title": "Entry and orientation", "layer": "flow", "stages": ["Orient"],
     "today": [("orientation", "current")], "target": {"step": "entry"}},
    {"key": "spine", "title": "The loop itself", "layer": "flow", "stages": ["Spine", "Flow"],
     "today": [("gap-register", "how-the-parts-interact-today-the-implicit-loop")], "target": {"layer": "flow", "transitions": True}},
    {"key": "plan", "title": "Plan", "layer": "flow", "stages": ["Plan"],
     "today": [("flow", "plan/current-state-measured-2026-10-14")], "target": {"step": "plan", "contract": "Plan"}},
    {"key": "design", "title": "Design", "layer": "flow", "stages": ["Design"],
     "today": [("flow", "design/current-state-measured-2026-10-14")], "target": {"step": "design", "contract": "Design"}},
    {"key": "build", "title": "Build", "layer": "flow", "stages": ["Build"],
     "today": [("flow", "build/current-state-measured-2026-10-14")], "target": {"step": "build", "contract": "Build"}},
    {"key": "test", "title": "Test", "layer": "flow", "stages": ["Test"],
     "today": [("flow", "test/current-state-measured-2026-10-14")], "target": {"step": "test", "contract": "Test"}},
    {"key": "deploy", "title": "Deploy", "layer": "flow", "stages": ["Deploy"],
     "today": [("flow", "deploy/current-state-measured-2026-10-14")], "target": {"step": "deploy", "contract": "Deploy"}},
    {"key": "review", "title": "Review", "layer": "flow", "stages": ["Review"],
     "today": [("flow", "review/current-state-measured-2026-10-14"), ("review-system", "current")], "target": {"step": "breakpoint"}},
    {"key": "maintain", "title": "Maintain", "layer": "observability", "stages": ["Maintain"],
     "today": [("flow", "maintain/current-state-measured-2026-10-14")], "target": {"layer": "observability", "contract": "Maintain"}},
    {"key": "roles", "title": "Roles", "layer": "roles", "stages": ["Roles"],
     "today": [("layer-roles", "current")], "target": {"layer": "roles"}},
    {"key": "memory", "title": "Memory: the trail", "layer": "memory", "stages": ["Memory"],
     "today": [("layer-memory", "current")], "target": {"layer": "memory"}},
    {"key": "library", "title": "Memory: the library", "layer": "memory", "stages": [], "cites": "layer-library",
     "today": [("layer-library", "current")], "target": {"layer": "memory", "library": True}},
    {"key": "runtime", "title": "Runtime", "layer": "runtime", "stages": ["Runtime"],
     "today": [("layer-runtime", "current")], "target": {"layer": "runtime"}},
    {"key": "lexicon", "title": "The lexicon", "layer": "memory", "stages": ["Lexicon"],
     "today": [("lexicon", "current")], "target": {"layer": "memory"}},
    {"key": "tooling", "title": "Tooling", "layer": "", "stages": ["Tooling"],
     "today": [("layer-memory", "tools")], "target": {"tools": True}},
]
# A decision section holds the owner's words, a fork asked, or what an answer settled. The design rounds
# record is one in every section; elsewhere a section's tag or its title says so.
DECISION_RECORDS = {"design-rounds"}
DECISION_TAGS = {"words", "directive", "owner-notes", "forks", "answers", "settled", "settled-lb",
                 "interpretations", "proposed", "closed", "deferred"}
DECISION_TITLE = re.compile(
    r"(?i)(\bforks?\b|\basked\b|\banswers(?=,|\s*$)|\banswered\b|\bsettled\b|\brulings?\b|\binterpretations\b"
    r"|\bowner(?:'s)? (?:words|directives?|answers|notes|next step)\b|\bthe owner set\b|\bto put to the owner\b"
    r"|^for the owner\b|\bquestions for the owner\b|\bwhat the owner did\b|\bdelegation\b)")
NOT_DECISION = re.compile(r"(?i)\bgaps to register\b")
DECISION_KINDS = [
    ("settled", re.compile(r"(?i)^revised\b")),
    ("words", re.compile(r"(?i)\bowner(?:'s)? (?:words|notes|directives?)\b|\bthe owner set\b|^raised when")),
    ("settled", re.compile(r"(?i)\bsettled\b|\banswers(?=,|\s*$)|\banswered\b|\bchanged\b|\bfixes\b"
                           r"|\bwhat the owner did\b|\bnext step\b|\brulings?\b|\bdelegation\b")),
    ("asked", re.compile(r"(?i)\basked\b|\bforks?\b|\bput to the owner\b|\bfor the owner\b|\bquestions\b|\binterpretations\b")),
]
# Where the atlas shows each section of the converged design, so a section v2 gains cannot go unshown.
# A kind's writer cell names a writer item, or carries one of these declared markers (the away pass's review, M4).
KIND_MARKERS = ("no writer item", "writer item not named", "every step's")
MEMORY_PLANTS = ("kind-unplaced", "kind-ghost-tag", "edge-status", "hop-edge", "edges-split")
# Plants on the record corpus and the view map, each stopping the run with its own refusal (the answers fold's
# closing review: run A's L4, run B's M4).
CORPUS_PLANTS = ("instruments-decision", "view-unread")
# Plants on the chain state and the as-built view, each damaging data in memory inside `derive_actual` before its
# refusals run (TOOL-dTrackedAtlas-2).
ACTUAL_PLANTS = ("state-dropped", "asbuilt-dropped")
STATE_PATH = REPO / "memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py"
STAMP_SCHEMA = 2
# Each stamp field's rule, the one table the page's writer and its reader both check through `check_stamp`
# (TOOL-dTrackedAtlas-12), so `--out` refuses a stamp `--check --page` would call unstamped.
STAMP_RULES = {
    "schema": lambda v: type(v) is int and v == STAMP_SCHEMA,
    "commit": lambda v: isinstance(v, str) and re.fullmatch(r"[0-9a-f]{40}", v) is not None,
    "default_ref": lambda v: isinstance(v, str) and re.fullmatch(r"[A-Za-z0-9._][A-Za-z0-9._/-]*", v) is not None,
    "landings": lambda v: isinstance(v, dict) and bool(v) and all(
        isinstance(k, str) and re.fullmatch(r"[A-Za-z0-9._-]+", k) and isinstance(shas, list) and all(
            isinstance(s, str) and re.fullmatch(r"[0-9a-f]{40}", s) for s in shas)
        for k, shas in v.items()),
    "digest": lambda v: isinstance(v, str) and re.fullmatch(r"[0-9a-f]{64}", v) is not None,
    "inputs": lambda v: isinstance(v, list) and bool(v) and all(
        isinstance(p, str) and re.fullmatch(r"[A-Za-z0-9._][A-Za-z0-9._/-]*", p) and ".." not in p.split("/")
        for p in v),
    "dirty": lambda v: isinstance(v, list) and all(isinstance(p, str) for p in v),
}
# The advice TOOL-dTrackedAtlas-1's StateError ends with, an option the Atlas does not take, and the remedy each
# relaying branch names in its place (TOOL-dTrackedAtlas-12).
STATE_ADVICE = "pass --default-ref <rev>"
DERIVE_REMEDY = "fetch the default branch, or name it with GOV_REMOTE and GOV_DEFAULT_BRANCH"
CHECK_REMEDY = "fetch the default branch the stamp names, or regenerate the page"
V2_VIEWS = {"layers": "overview", "principles": "principles", "front-door": "records", "policies": "policies",
            "presets": "policies", "floor": "records", "witnesses": "records", "contracts": "flow", "chain": "chain",
            "clause-ids": "records", "enforcement": "records", "planned": "records", "open": "progress", "owed": "progress"}


def text(path):
    return path.read_text(encoding="utf-8")


def section(body, tag):
    m = re.search(r"^## \[" + re.escape(tag) + r"\]([^\n]*)\n(.*?)(?=^## |\Z)", body, flags=re.M | re.S)
    if not m:
        sys.exit(f"atlas: no section [{tag}]")
    return m.group(1).strip(), m.group(2)


def cells(line):
    inner = line.strip()
    inner = inner[1:] if inner.startswith("|") else inner
    inner = inner[:-1] if inner.endswith("|") else inner
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", inner)]


def tables(block):
    """Every table in a block, as (header, rows). A row whose cell count differs from its header stops the run."""
    out, lines, i = [], block.split("\n"), 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and SEP.match(lines[i + 1]):
            head, rows = cells(lines[i]), []
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                row = cells(lines[i])
                if len(row) != len(head):
                    sys.exit(f"atlas: {len(row)} cells under a {len(head)}-column header: {lines[i][:90]}")
                rows.append(row)
                i += 1
            out.append((head, rows))
        else:
            i += 1
    return out


def table(block, first, where):
    found = [rows for head, rows in tables(block) if head[0] == first]
    if len(found) != 1:
        sys.exit(f"atlas: {len(found)} tables in {where} open with {first!r}")
    return found[0]


def plain(cell):
    return cell.strip("`")


def bullets(block, lead):
    if lead not in block:
        sys.exit(f"atlas: no lead-in {lead!r}")
    after = block.split(lead, 1)[1].lstrip("\n").split("\n\n", 1)[0]
    items = [ln[2:].strip() for ln in after.split("\n") if ln.startswith("- ")]
    if not items:
        sys.exit(f"atlas: no bullets after {lead!r}")
    return items


def paragraph(block, opener):
    """The block that opens with opener, up to the next blank line, its lines and lists kept for the page to render."""
    m = re.search(r"^" + re.escape(opener) + r"(.*?)(?=\n\n|\Z)", block, flags=re.M | re.S)
    return (opener + m.group(1)).strip() if m else ""


def slug(s):
    s = re.sub(r"`", "", s.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def split_sections(body):
    """Split a record at its level-2 and level-3 headings, fences respected; the parts rejoin to the text."""
    lines = body.split("\n")
    marks, fence = [], False
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        m = None if fence else re.match(r"^(#{2,3}) (.+)$", ln)
        if m:
            marks.append((i, len(m.group(1)), m.group(2).strip()))
    bounds = [0] + [m[0] for m in marks] + [len(lines)]
    out, seen, h2 = [], {}, "top"
    starts = {m[0]: m for m in marks}
    for a, b in zip(bounds, bounds[1:]):
        if a == b:
            continue
        if a in starts:
            _, level, title = starts[a]
            tag_m = re.match(r"^\[([a-z0-9-]+)\]\s*(.*)$", title)
            tag = tag_m.group(1) if tag_m else ""
            shown = tag_m.group(2) if tag_m else title
            sid = (tag or slug(title)) if level == 2 else f"{h2}/{tag or slug(title)}"
        else:
            level, tag, shown, sid = 1, "", "", "top"
        n = seen.get(sid, 0)
        seen[sid] = n + 1
        if n:
            sid = f"{sid}-{n + 1}"
        if level == 2:
            h2 = sid
        out.append({"id": sid, "tag": tag, "title": shown, "level": level, "md": "\n".join(lines[a:b])})
    if "\n".join(s["md"] for s in out) != body:
        sys.exit("atlas: a record's sections do not rejoin to its text")
    return out


def corpus():
    """Every record the atlas carries: the build's README, its design records, reviews and research returns."""
    recs = []
    # The whole-design audit's briefs and agent returns are snapshots of agent work, not design, and the design map
    # skips them for the same reason; their reports under reviews/ stay (2026-10-20, the page had passed 16 MB). The
    # as-built view is v2's [chain] rendered at the baseline, a copy the page carries already until a deviation
    # exists (the baseline, 2026-10-20: with it the page measured 16,001,498 bytes).
    paths = [BUILD / "README.md"] + sorted(p for p in HERE.glob("*.md") if not any(m in p.name for m in
                                                                                 ("-brief", "-return-", "-as-built"))) \
        + sorted(REVIEWS.glob("*.md"))
    for p in paths:
        name = p.stem.split(PREFIX, 1)[-1] if PREFIX in p.stem else p.stem.split("-PLAY-dClosedLoop-1-", 1)[-1]
        body = text(p)
        h1 = re.search(r"^# (.+)$", body, flags=re.M)
        date = p.name[:10]
        if p.name == "README.md":
            opened = re.search(r"^opened: (\d{4}-\d{2}-\d{2})$", body, flags=re.M)
            if not opened:
                sys.exit("atlas: the build README has no opened: date")
            group, date = "Journal", opened.group(1)
        elif p.parent == REVIEWS:
            group = "Reviews"
        elif name.startswith("research-"):
            group = "Research returns"
        elif name in ("architecture-v2", "design-overview", "architecture-v1", "architecture-v0"):
            group = "Architecture"
        elif name.startswith("layer-") or name in ("flow-steps", "flow-roles", "lexicon", "review-system"):
            group = "Layers"
        elif name == "gap-register" or "compared" in name:
            group = "Register and comparisons"
        elif name == "session-log":
            group = "Journal"
        else:
            group = "Foundations and walks"
        recs.append({"path": p.relative_to(REPO).as_posix(), "name": name, "date": date,
                     "title": h1.group(1).strip() if h1 else name, "group": group, "sections": split_sections(body)})
    # A record is keyed by the name its stem derives, so two records that derive one name would have the later one
    # read in the earlier's place, its title and its decisions with it.
    names = [r["name"] for r in recs]
    shared = sorted({n for n in names if names.count(n) > 1})
    if shared:
        sys.exit("atlas: records share a derived name, so one would be read as the other: " + ", ".join(
            f"{n} ({', '.join(r['path'].rsplit('/', 1)[-1] for r in recs if r['name'] == n)})" for n in shared))
    return recs


def find(recs, name, sid):
    hits = [r for r in recs if r["name"] == name and r["group"] not in ("Reviews",)]
    if len(hits) != 1:
        sys.exit(f"atlas: {len(hits)} records named {name}")
    sec = [s for s in hits[0]["sections"] if s["id"] == sid]
    if len(sec) != 1:
        sys.exit(f"atlas: {name} has {len(sec)} sections with id {sid!r}")
    return {"path": hits[0]["path"], "id": sid}


def plant_memory(src, plant):
    """Damage one memory-view source in memory, so `--check --plant <case>` must stop the run (the away pass's review)."""
    def swap(key, old, new):
        if old not in src[key]:
            sys.exit(f"atlas: plant {plant}: its anchor is gone")
        src[key] = src[key].replace(old, new, 1)
    lex = "\n| lexicon declaration | dMindYourWords |"
    if plant == "kind-unplaced":
        swap("memory", lex, "\n| ghost kind | dTotalRecall | a planted kind that names no writer |" + lex)
    elif plant == "kind-ghost-tag":
        swap("memory", lex, "\n| ghost kind | dTotalRecall | its writer is `plan.ghost-writer` |" + lex)
    elif plant == "edge-status":
        swap("plan", "| `made` | new |", "| `made` | nwe |")
    elif plant == "hop-edge":
        swap("plan", "| `follows` | none |", "| `follows`, `answered-by-typo` | none |")
    elif plant == "edges-split":
        swap("plan", "\n| `implements` |", "\n\n| `implements` |")
    elif plant and plant not in CORPUS_PLANTS + ACTUAL_PLANTS:
        sys.exit(f"atlas: no plant {plant}; the cases are {', '.join(MEMORY_PLANTS + CORPUS_PLANTS + ACTUAL_PLANTS)}")
    return src


def derive(plant=None):
    src = plant_memory({k: text(p) for k, p in SOURCES.items()}, plant)
    v2, steps_text = src["v2"], src["steps"]
    recs = corpus()
    if plant == "instruments-decision":
        # The retitled case: an instruments record whose section title the decision pattern reads as an answer.
        rec = next(r for r in recs if r["name"] == "night-pass-instruments")
        rec["sections"].append({"id": "answers-fold-planted", "tag": "answers-fold", "level": 2,
                                "title": "The owner's answers, folded", "md": ""})
    views = dict(V2_VIEWS, planned="chain") if plant == "view-unread" else V2_VIEWS

    _, lay = section(v2, "layers")
    layers = [{"tag": plain(r[0]), "kind": r[1], "what": r[2]} for r in table(lay, "Layer", "v2 [layers]")]
    cycle = bullets(lay, "The core is a cycle on a base:")
    contract = bullets(lay, "Every layer fills one contract, whether core or expansion:")
    one_line = re.search(r"^In one line: (.+)$", src["instruction"], flags=re.M)
    kits = [{"kit": r[0], "layer": r[1], "kind": r[2]} for r in table(src["instruction"], "Kit or tool", "layer-instruction")]

    all_tags, steps = set(), []
    for tag in STEPS:
        title, block = section(steps_text, tag)
        rows = table(block, "Item", f"flow-steps [{tag}]")
        raw = [ln for ln in block.split("\n") if ln.startswith("| `")]
        if len(raw) != len(rows):
            sys.exit(f"atlas: [{tag}] holds {len(raw)} item lines but its table parsed {len(rows)}")
        items = []
        for r in rows:
            if not ITEM_TAG.fullmatch(r[0]):
                sys.exit(f"atlas: [{tag}] has an item tag the pattern cannot read: {r[0]!r}")
            head = re.split(r"[,:(]", r[1], maxsplit=1)[0].strip().lower()
            items.append({"tag": plain(r[0]), "actor": r[1], "kind": head if head in KINDS else "role",
                          "role": "" if head in KINDS else head, "needs": r[2], "does": r[3], "proof": r[4], "then": r[5],
                          "owner": r[6] if len(r) > 6 else ""})
            all_tags.add(plain(r[0]))
        pol = re.search(r"the policies: (.+?)\.\n", block)
        steps.append({"tag": tag, "title": title.split("]")[-1].strip(), "enters": paragraph(block, "**Enters**"),
                      "exits": paragraph(block, "**Exits**"), "policies": ITEM_TAG.sub(r"\1", pol.group(1)) if pol else "",
                      "items": items})
    for s in steps:
        for it in s["items"]:
            it["needsRefs"] = [t for t in ITEM_TAG.findall(it["needs"]) if t in all_tags]
            it["thenRefs"] = [t for t in ITEM_TAG.findall(it["then"]) if t in all_tags]

    _, trans = section(steps_text, "transitions")
    transitions = [{"from": r[0], "on": r[1], "to": r[2], "witness": r[3]} for r in table(trans, "From", "[transitions]")]
    term = re.search(r"^((?:[A-Z][a-z]+)(?:, [a-z]+)* and [a-z]+) are terminal\.", trans, flags=re.M)
    if not term:
        sys.exit("atlas: no terminal-state sentence in [transitions]")
    terminal = [t.strip().lower() for t in re.split(r", | and ", term.group(1))]

    _, con = section(v2, "contracts")
    contracts = [{"stage": r[0], "takes": r[1], "hands": r[2], "witness": r[3], "gate": r[4], "review": r[5]}
                 for r in table(con, "Stage", "v2 [contracts]")]
    _, ros = section(src["roles"], "roster")
    roster = [{"role": r[0], "layer": r[1], "acts": r[2]} for r in table(ros, "Role", "layer-roles [roster]")]

    _, ch = section(v2, "chain")
    chain = []
    for r in table(ch, "Build", "v2 [chain]"):
        owned = set()
        for a, b in re.findall(r"(gap-[a-z]+-\d\d) to (gap-[a-z]+-\d\d)", r[4]):
            stem, lo, hi = a.rsplit("-", 1)[0], int(a.rsplit("-", 1)[1]), int(b.rsplit("-", 1)[1])
            owned |= {f"{stem}-{i:02d}" for i in range(lo, hi + 1)}
        owned |= set(GAP_ID.findall(re.sub(r"gap-[a-z]+-\d\d to gap-[a-z]+-\d\d", "", r[4])))
        chain.append({"build": r[0], "stage": r[1], "parents": re.findall(r"\bd[A-Z][A-Za-z]+\b", r[2]),
                      "units": r[3], "gaps": sorted(owned)})
    gap_rows = table(src["gaps"], "Key", "the gap register")
    raw_gaps = [ln for ln in src["gaps"].split("\n") if ln.startswith("| gap-")]
    if len(raw_gaps) != len(gap_rows):
        sys.exit(f"atlas: the register holds {len(raw_gaps)} gap lines but its table parsed {len(gap_rows)}")
    owner = {}
    for c in chain:
        for g in c["gaps"]:
            if g in owner:
                sys.exit(f"atlas: {g} owned by {owner[g]} and {c['build']}")
            owner[g] = c["build"]
    gaps = []
    for r in gap_rows:
        if r[0] not in owner:
            sys.exit(f"atlas: {r[0]} is owned by no chain build")
        gaps.append({"id": r[0], "stage": r[1], "sev": r[2].split()[0], "gap": r[3], "evidence": r[4], "owner": owner[r[0]]})
    phantom = sorted(set(owner) - {g["id"] for g in gaps})
    if phantom:
        sys.exit(f"atlas: chain owns gaps the register lacks: {phantom}")

    _, pol = section(v2, "policies")
    policies = [{"key": plain(r[0]), "values": r[1], "default": r[2], "source": r[3], "owner": r[4] if len(r) > 4 else ""}
                for r in table(pol, "Key", "v2 [policies]")]
    _, pre = section(v2, "presets")
    head = next(h for h, _ in tables(pre) if h[0] == "Key")
    names = [re.sub(r"\s*\(default\)", "", h) for h in head[1:]]
    presets = {"names": names, "rows": {plain(r[0]): r[1:] for r in table(pre, "Key", "v2 [presets]")}}

    # The principles, P1 onwards, each with its whole text.
    _, prin = section(v2, "principles")
    principles, cur = [], None
    for ln in prin.split("\n"):
        m = re.match(r"^- \*\*P(\d+) (.+?)\*\*\s*(.*)$", ln)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2).rstrip("."), "md": m.group(3)}
            principles.append(cur)
        elif cur is not None and (ln.startswith("  ") or ln == ""):
            cur["md"] += "\n" + ln[2:] if ln else "\n"
        elif cur is not None:
            cur = None
    nums = sorted(p["n"] for p in principles)
    if nums != list(range(1, len(nums) + 1)):
        sys.exit(f"atlas: the principles are not P1 to P{len(nums)} without a gap: {nums}")
    raw_p = re.findall(r"^- \*\*P\d+ ", prin, flags=re.M)
    if len(raw_p) != len(principles):
        sys.exit(f"atlas: {len(raw_p)} principle lines but {len(principles)} parsed")
    for p in principles:
        p["md"] = p["md"].strip()
    principles.sort(key=lambda p: p["n"])

    timeline = []
    for m in re.finditer(r"^Revised: (\d{4}-\d{2}-\d{2}), (.+?)(?=\n\n)", v2, flags=re.M | re.S):
        rest = re.sub(r"\s*\n\s*", " ", m.group(2))
        what = re.split(r" \(|: |:$", rest, maxsplit=1)[0].rstrip(".:")
        timeline.append({"date": m.group(1), "what": what, "detail": rest})
    reviews = []
    for p in sorted(REVIEWS.glob("*-review-PLAY-dClosedLoop-1-*.md")):
        body = text(p)
        shape = re.search(r"^review-shape (.+)$", body, flags=re.M)
        verdict = re.search(r"^## Verdict: (.+)$", body, flags=re.M)
        if not shape or not verdict:
            sys.exit(f"atlas: {p.name} lacks its verdict or review-shape line")
        fields = dict(kv.split("=", 1) for kv in shape.group(1).split())
        reviews.append({"file": p.name, "path": p.relative_to(REPO).as_posix(), "date": p.name[:10],
                        "scope": re.sub(r"^.*-PLAY-dClosedLoop-1-", "", p.stem), "verdict": verdict.group(1),
                        **{k: fields[k] for k in ("kind", "round", "intensity")},
                        **{k: int(fields[k]) for k in ("raw", "confirmed", "refuted", "blocker", "high", "medium", "low", "agents", "out-tokens")}})

    # Each layer's records, reviews, folds and design sections.
    progress = []
    for layer, lnames in LAYER_RECORDS.items():
        recs_l = [record(n) for n in lnames]
        progress.append({"layer": layer, "records": [r.name for r in recs_l],
                         # A layer's rounds are named for its first record: `runtime-a`, or `expansions-a`
                         # for the three expansions, which one record and one pair of rounds cover.
                         "reviews": [r["file"] for r in reviews
                                     if re.fullmatch(rf"{lnames[0].removeprefix('layer-')}-[ab]", r["scope"])],
                         # Folded: a record holds `[revised]` or a section whose tag ends in "fold", such as the
                         # debt round's `[debt-fold]`, or a `Revised:` line naming its Tier-2 rounds.
                         "folded": any(re.search(r"^## \[(?:revised|[a-z0-9-]*fold)\]", text(r), flags=re.M)
                                       or re.search(r"^Revised: .*Tier-2", text(r), flags=re.M) for r in recs_l),
                         "sections": [{"path": rec["path"], "id": s["id"], "title": s["title"], "tag": s["tag"]}
                                      for n in lnames for rec in recs if rec["name"] == n and rec["group"] != "Reviews"
                                      for s in rec["sections"] if s["level"] == 2]})
    lib_text = src["library"]
    _, op = section(lib_text, "open")
    open_items, cur = [], None
    for ln in op.split("\n"):
        m = re.match(r"^- \*\*(.+?)\*\*:?\s*(.*)$", ln)
        if m:
            cur = {"label": m.group(1).rstrip(":,.;"), "text": m.group(2), "items": []}
            open_items.append(cur)
        elif ln.startswith("  - ") and cur:
            cur["items"].append(ln[4:].strip())
        elif ln.startswith("    ") and cur and cur["items"]:
            cur["items"][-1] += " " + ln.strip()
        elif ln.startswith("  ") and cur and not cur["items"]:
            cur["text"] += " " + ln.strip()
    library_round = {"reviews": [r["file"] for r in reviews if r["scope"] == "library"],
                     "folded": "\n## [review-fold]" in lib_text, "open": open_items}

    # The library's design: its four paths, the optional components' absent states, its flow points.
    _, ldes = section(lib_text, "design")
    lib_paths = [{"path": r[0], "where": r[1], "actor": r[2], "witness": r[3]} for r in table(ldes, "Path", "layer-library [design]")]
    _, lcon = section(lib_text, "consult")
    consult = [{"component": r[0], "where": r[1], "absent": r[2]} for r in table(lcon, "Component", "layer-library [consult]")]
    library_items = sorted({t for p in lib_paths for t in ITEM_TAG.findall(p["where"] + " " + p["witness"]) if t in all_tags})

    # Each tool's fate: the fates record's kits and every part, function by function (night pass, point 8). Memory's
    # kit-level tooling map is superseded, and stays readable in its record.
    _, fk = section(src["fates"], "kits")
    kit_fates = [{"kit": r[0], "fate": r[1], "what": r[2]} for r in table(fk, "Kit", "fates [kits]")]
    _, ft = section(src["fates"], "table")
    tools = [{"verdict": r[3], "tools": f"{r[0]} · {r[1]}", "fact": f"{r[4]}; decided by {r[5]}"}
             for r in table(ft, "Kit", "fates [table]")]

    # Today against the target, area by area.
    stage_set = {g["stage"] for g in gaps}
    claimed = [s for a in AREAS for s in a["stages"]]
    if sorted(claimed) != sorted(set(claimed)):
        sys.exit("atlas: a gap stage is mapped to two comparison areas")
    if stage_set - set(claimed):
        sys.exit(f"atlas: gap stages no comparison area claims: {sorted(stage_set - set(claimed))}")
    areas = []
    for a in AREAS:
        today = [find(recs, n, sid) for n, sid in a["today"]]
        if a.get("cites"):
            body = text(record(a["cites"]))
            ids = sorted({g for g in GAP_ID.findall(body)} & {g["id"] for g in gaps})
        else:
            ids = [g["id"] for g in gaps if g["stage"] in a["stages"]]
        areas.append({"key": a["key"], "title": a["title"], "layer": a["layer"], "stages": a["stages"],
                      "today": today, "target": a["target"], "gaps": ids})
    loops = {"today": find(recs, "gap-register", "how-the-parts-interact-today-the-implicit-loop"),
             "themes": find(recs, "gap-register", "cross-cutting-themes")}
    owed = find(recs, "architecture-v2", "owed")
    v2open = find(recs, "architecture-v2", "open")

    # Every section that records the owner's words, a fork asked, an answer or a settlement.
    decisions = []
    for rec in recs:
        if rec["group"] in ("Reviews", "Research returns"):
            continue
        whole = rec["name"] in DECISION_RECORDS
        picked = [s for s in rec["sections"] if s["level"] >= 2 and not NOT_DECISION.search(s["title"]) and
                  (whole or s["title"] and (s["tag"] in DECISION_TAGS or DECISION_TITLE.search(s["title"])))]
        body = "\n".join(s["md"] for s in rec["sections"])
        if re.search(r"(?m)^\s*-?\s*\**Answers?\**:|^\s*-\s*Offered:", body) and not picked:
            sys.exit(f"atlas: {rec['name']} records an owner's answer, yet no section title marks it")
        if picked and rec["name"].endswith("instruments"):
            sys.exit(f"atlas: {rec['name']} is an instruments record, yet its section '{picked[0]['title']}' reads as "
                     f"a decision; an instruments record holds scripts and runs, so retitle the section")
        for s in picked:
            kind = "round" if whole else next((k for k, rx in DECISION_KINDS if rx.search(s["title"])), "")
            if not kind:
                kind = {"words": "words", "directive": "words", "owner-notes": "words", "forks": "asked",
                        "interpretations": "asked", "proposed": "asked"}.get(s["tag"], "settled")
            pid = s["id"].split("/")[0] if s["level"] == 3 else ""
            parent = next((x["title"] for x in rec["sections"] if x["id"] == pid), "") if pid else ""
            decisions.append({"path": rec["path"], "id": s["id"], "date": rec["date"], "record": rec["name"],
                              "title": s["title"], "tag": s["tag"], "kind": kind, "parent": parent})

    # The build's event journal, one entry per dated bullet of the session log's Events section.
    log = next(r for r in recs if r["name"] == "session-log")
    ev = [s for s in log["sections"] if s["id"] == "events"]
    if len(ev) != 1:
        sys.exit("atlas: the session log has no single Events section")
    events, cur = [], None
    for ln in ev[0]["md"].split("\n"):
        m = re.match(r"^- (\d{4}-\d{2}-\d{2}), session ([0-9a-f]{8}): (.*)$", ln)
        if m:
            cur = {"date": m.group(1), "session": m.group(2), "md": m.group(3)}
            events.append(cur)
        elif cur is not None and ln.startswith("  "):
            cur["md"] += "\n" + ln[2:]
        elif cur is not None and ln.strip():
            cur = None
    raw_ev = re.findall(r"(?m)^- \d{4}-\d{2}-\d{2}, session ", ev[0]["md"])
    if not events or len(raw_ev) != len(events):
        sys.exit(f"atlas: {len(raw_ev)} event bullets but {len(events)} parsed")

    # Each section of the converged design, and the view that shows it.
    v2_ids = [s["id"] for r in recs if r["name"] == "architecture-v2" for s in r["sections"] if s["level"] == 2]
    if sorted(v2_ids) != sorted(views):
        sys.exit(f"atlas: v2's sections and the views declared for them differ: {sorted(set(v2_ids) ^ set(views))}")
    # A view other than records shows a section only if the derivation reads that section, so the sections it reads
    # are taken from this file's own source, never typed beside it.
    own = Path(__file__).read_text(encoding="utf-8")
    read = set(re.findall(r'section\(v2, "([a-z0-9-]+)"\)', own)) | \
        set(re.findall(r'find\(recs, "architecture-v2", "([a-z0-9-]+)"\)', own))
    unread = sorted(s for s, view in views.items() if view != "records" and s not in read)
    if unread:
        sys.exit(f"atlas: v2's sections {unread} map to a view that reads none of them; map them to records or render "
                 f"them")
    # The expansions' programs: each layer-expansions table headed `| Item | Actor |` is one program's, outside the
    # steps, and a row may name two items (PM-12).
    programs = []
    for head, rows in tables(src["expansions"]):
        if head[:2] != ["Item", "Actor"]:
            continue
        its = [{"tag": t, "actor": r[1], "does": r[2], "witness": r[3], "routes": r[4],
                "owner": r[head.index("Owner")] if "Owner" in head else ""} for r in rows for t in ITEM_TAG.findall(r[0])]
        programs.append({"program": its[0]["tag"].split(".")[0], "items": its})

    # The memory layer drawn whole (the away pass, point 1): the plan's families, pockets, sites, edges and cycle; the
    # kind registry's record kinds, each placed on the step or program of the first writer item its cell names; and
    # the instruction ladder memory sits at the foot of. Every pocket and hop names a family the plan declares; every
    # pocket's status, edge's status and hop's state is read from a fixed leading word; every hop edge is a declared
    # type; every plan table is counted against its raw row lines; and every kind names a writer item or carries a
    # declared marker, its other dotted tokens resolving to a policy key or a file. Anything else stops the run. It does
    # not check that a writer item truly writes the kind, nor that a pocket's owner owns it.
    def one_table(block, first, where):
        rows = table(block, first, where)
        raw = [ln for ln in block.split("\n") if ln.startswith("| ") and not ln.startswith(f"| {first} |")]
        if len(raw) != len(rows):
            sys.exit(f"atlas: {where} holds {len(raw)} row lines but its table parsed {len(rows)}: a split table drops rows")
        return rows

    plan = src["plan"]
    _, pfr = section(plan, "frame")
    first = pfr.strip().split("\n\n", 1)[0].split("\n")
    frame = " ".join(first[:next((i for i, ln in enumerate(first) if ln.startswith("- ")), len(first))])
    _, pfam = section(plan, "families")
    families = [{"family": r[0], "level": r[1], "holds": r[2], "lifecycle": r[3]}
                for r in one_table(pfam, "Family", "memory-plan [families]")]
    fams = {f["family"] for f in families}
    _, ppoc = section(plan, "pockets")
    pockets = []
    for r in one_table(ppoc, "Pocket", "memory-plan [pockets]"):
        m = re.match(r"(node-local node|node|witness|out|edge site|folded|retired)\b", r[4])
        if r[1] not in fams or not m:
            sys.exit(f"atlas: memory-plan [pockets] row {r[0]!r}: family {r[1]!r} or status {r[4][:30]!r} unread")
        pockets.append({"pocket": r[0], "family": r[1], "where": r[2], "today": r[3], "becomes": r[4],
                        "status": {"node-local node": "node", "retired": "folded"}.get(m.group(1), m.group(1)),
                        "key": r[5], "owner": r[6]})
    _, psite = section(plan, "sites")
    sites = [{"site": r[0], "syntax": r[1], "door": r[2]} for r in one_table(psite, "Site", "memory-plan [sites]")]
    _, pedge = section(plan, "edges")
    medges = []
    for r in one_table(pedge, "Edge", "memory-plan [edges]"):
        m = re.match(r"(P33|new|derived)\b", r[4])
        if not m:
            sys.exit(f"atlas: memory-plan [edges] row {r[0]!r}: status {r[4][:30]!r} unread")
        medges.append({"edge": plain(r[0]), "fromTo": r[1], "site": r[2], "inverse": plain(r[3]), "status": m.group(1),
                       "statusText": r[4], "need": r[5]})
    names = {e["edge"] for e in medges}
    _, pcyc = section(plan, "cycle")
    hops = []
    for r in one_table(pcyc, "Hop", "memory-plan [cycle]"):
        m = re.match(r"(partly typed|typed|prose|search|none)\b", r[4])
        found = re.findall(r"`([a-z-]+)`", r[3])
        unknown = [e for e in found if e not in names]
        if r[1] not in fams or r[2] not in fams or not m or not found or unknown:
            sys.exit(f"atlas: memory-plan [cycle] hop {r[0]!r}: a family, its state or an edge is unread {unknown}")
        hops.append({"hop": r[0], "from": r[1], "to": r[2], "edges": found, "edgeText": r[3], "today": r[4],
                     "state": m.group(1), "site": r[5]})
    _, mdes = section(src["memory"], "design")
    con_blk = mdes.split("### [contract]", 1)[1].split("\n### ", 1)[0]
    place = {it["tag"]: s["tag"] for s in steps for it in s["items"]}
    place.update({it["tag"]: p["program"] for p in programs for it in p["items"]})
    keyset = {p["key"] for p in policies}
    taglike = re.compile(r"[a-z*][a-z0-9*-]*(?:\.[a-z0-9*][a-z0-9*-]*)+")
    con_rows = table(con_blk, "Kind", "layer-memory [contract]")
    raw_k = re.findall(r"(?m)^\| [a-z][a-z -]* \| d[A-Z]\w+ \| ", con_blk)
    if len(raw_k) != len(con_rows):
        sys.exit(f"atlas: layer-memory [contract] holds {len(raw_k)} kind lines but its table parsed {len(con_rows)}")
    kinds = []
    for r in con_rows:
        writers, ghosts = [], []
        for t in re.findall(r"`([^`]+)`", r[2]):
            if not taglike.fullmatch(t) or re.search(r"\.(?:toml|md|py|sh|js|json|txt|conf)$", t):
                continue   # a plain word, a path, a trailer or a file name: never a writer tag
            if "*" in t:
                hits = sorted(x for x in place if fnmatch.fnmatchcase(x, t))
                if hits:
                    writers += hits
                elif not any(fnmatch.fnmatchcase(k, t) for k in keyset):
                    ghosts.append(t)
            elif t in place:
                writers.append(t)
            elif t not in keyset:
                ghosts.append(t)
        if ghosts:
            sys.exit(f"atlas: layer-memory [contract] kind {r[0]!r} names {ghosts}, resolving to no item, key or file")
        marker = next((mk for mk in KIND_MARKERS if mk in r[2]), "")
        if not writers and not marker:
            sys.exit(f"atlas: layer-memory [contract] kind {r[0]!r} names no writer item and carries no marker")
        places = []
        for t in writers:
            if place[t] not in places:
                places.append(place[t])
        kinds.append({"kind": r[0], "owner": r[1], "writer": r[2], "items": writers, "places": places, "marker": marker})
    levels = [{"level": r[0], "what": r[1]} for r in table(src["instruction"], "Level", "layer-instruction R-G")]
    memory = {"frame": frame, "path": SOURCES["plan"].relative_to(REPO).as_posix(), "families": families,
              "pockets": pockets, "sites": sites, "edges": medges, "hops": hops, "kinds": kinds, "levels": levels}

    v2_rec = next(r for r in recs if r["name"] == "architecture-v2")
    v2map = [{"id": s["id"], "title": s["title"], "view": V2_VIEWS[s["id"]], "path": v2_rec["path"]}
             for s in v2_rec["sections"] if s["level"] == 2]

    digest = hashlib.sha256()
    for rec in recs:
        digest.update(rec["path"].encode())
        for s in rec["sections"]:
            digest.update(s["md"].encode())
    return {
        "build": "dClosedLoop", "digest": digest.hexdigest()[:12], "latest": max(t["date"] for t in timeline),
        "oneLine": one_line.group(1) if one_line else "",
        "layers": layers, "cycle": cycle, "contract": contract, "kits": kits,
        "steps": steps, "programs": programs, "transitions": transitions, "terminal": terminal, "contracts": contracts,
        "roster": roster, "chain": chain, "gaps": gaps, "policies": policies, "presets": presets,
        "principles": principles, "timeline": timeline, "reviews": reviews, "progress": progress,
        "libraryRound": library_round, "libraryPaths": lib_paths, "consult": consult, "libraryItems": library_items,
        "tools": tools, "kitFates": kit_fates, "areas": areas, "loops": loops, "owed": owed, "v2open": v2open, "decisions": decisions,
        "events": events, "v2map": v2map, "memory": memory, "records": recs,
        "sources": {k: p.relative_to(REPO).as_posix() for k, p in SOURCES.items()},
    }


def load_build_state():
    """TOOL-dTrackedAtlas-1's module at STATE_PATH, loaded on first use and cached: the one loader `derive_actual`,
    `read_git` and `read_landings` share (TOOL-dTrackedAtlas-10)."""
    if not hasattr(load_build_state, "module"):
        import importlib.util
        spec = importlib.util.spec_from_file_location("atlas_build_state", STATE_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        load_build_state.module = module
    return load_build_state.module


def render_state_error(error, remedy):
    """The text of `error`, TOOL-dTrackedAtlas-1's StateError, with a trailing STATE_ADVICE, an option the Atlas does
    not take, rewritten as `remedy`; any other text unchanged (TOOL-dTrackedAtlas-12)."""
    said = str(error)
    if said.endswith(STATE_ADVICE):
        return said[:-len(STATE_ADVICE)] + remedy
    return said


def derive_actual(data, ref="HEAD", claims=True, plant=None):
    """`data`, `derive`'s result, with the chain's actual state added (TOOL-dTrackedAtlas-2): `state`, the state
    document of TOOL-dTrackedAtlas-1's `derive` at `ref`, whole; `asBuilt`, the as-built view's rows per chain build;
    `baseline`, the measured dates and the design keys; and each area's `landed` and `measured`.

    The chain state is read at `ref` through git; dClosedLoop's records and the as-built view are read from the
    working tree, as `derive` reads everything. A state document or a view whose builds differ from `data["chain"]`
    is a refusal. What it does not check: that a landed build closed every gap it owns, that the working tree and
    `ref` describe one commit, and that the view is current with its deviation records."""
    build_state = load_build_state()
    kit = str(REPO / "tools/memory-tree")
    if kit not in sys.path:
        sys.path.insert(0, kit)
    import design_lib

    chain = [c["build"] for c in data["chain"]]

    def check_builds(name, held, same):
        """Refuse, naming each side, when `held` is not the chain's builds."""
        if same:
            return
        lacks = [b for b in chain if b not in held] or ["none"]
        extra = [b for b in held if b not in chain] or ["none"]
        sys.exit(f"atlas: {name} lacks {', '.join(lacks)} and holds {', '.join(extra)} the chain does not")

    try:
        state = build_state.derive(ref, root=str(REPO), claims=claims, detail=True)
    except build_state.StateError as e:
        sys.exit(f"atlas: chain state: {render_state_error(e, DERIVE_REMEDY)}")
    except build_state.ChainError as e:
        sys.exit(f"atlas: chain state: {e}")
    anchor = state["landed"][-1] if state["landed"] else None
    if plant in ACTUAL_PLANTS and anchor is None:
        sys.exit(f"atlas: plant {plant}: its anchor is gone")
    if plant == "state-dropped":
        state["builds"] = [b for b in state["builds"] if b["slug"] != anchor]
        state["landed"] = [s for s in state["landed"] if s != anchor]
    held = [b["slug"] for b in state["builds"]]
    check_builds("the chain state", held, held == chain)

    try:
        keys = design_lib.read_design_keys(str(REPO), design_lib.read_design_conf(str(REPO)))
        if keys is None:
            sys.exit("atlas: the design keys are blank, so there is no as-built view to read")
        rows = design_lib.read_design_view(keys["DESIGN_VIEW"], root=str(REPO))
    except design_lib.DesignRefusal as e:
        sys.exit(f"atlas: as-built view: {e}")
    if plant == "asbuilt-dropped":
        rows = [r for r in rows if r[0] != anchor]
    viewed = list(dict.fromkeys(r[0] for r in rows))
    check_builds("the as-built view", viewed, set(viewed) == set(chain))
    as_built = {b: [] for b in chain}
    for build, cid, body, _, since in rows:
        as_built[build].append({"clause": cid, "text": body, "since": since})

    owner = {g["id"]: g["owner"] for g in data["gaps"]}
    dated = {r["path"]: r["date"] for r in data["records"]}
    for a in data["areas"]:
        owners = {owner[g] for g in a["gaps"]}
        a["landed"] = [b for b in chain if b in state["landed"] and b in owners]
        a["measured"] = sorted({dated[s["path"]] for s in a["today"]})
    measured = sorted({d for a in data["areas"] for d in a["measured"]})
    data["state"] = state
    data["baseline"] = {"measured": [measured[0], measured[-1]], "design": keys["DESIGN_BASELINE"],
                        "view": keys["DESIGN_VIEW"]}
    data["asBuilt"] = as_built
    return data


class StampError(Exception):
    """A git call failed or timed out, the ref does not resolve, or a stamp fails a rule of STAMP_RULES."""


def check_stamp(stamp, fields=None):
    """The reason `the stamp's <field> field fails its rule:<value>` for the first field of `fields` (None: every
    field of STAMP_RULES, in the table's order) whose rule `stamp.get(field)` fails, else None (TOOL-dTrackedAtlas-12).
    """
    for field in STAMP_RULES if fields is None else fields:
        if not STAMP_RULES[field](stamp.get(field)):
            return f"the stamp's {field} field fails its rule:{json.dumps(stamp.get(field))[:80]}"
    return None


def read_git(*args):
    """The stdout bytes of `git <args>` run in REPO under TOOL-dTrackedAtlas-1's GIT_TIMEOUT, read through
    `load_build_state`; StampError naming the call when it fails, cannot start or outlives the bound."""
    timeout = load_build_state().GIT_TIMEOUT
    call = "git " + " ".join(args[:args.index("--")] if "--" in args else args)
    try:
        done = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise StampError(f"{call} gave no answer within {timeout} s") from None
    except OSError as e:
        raise StampError(f"{call} did not start: {e}") from None
    if done.returncode:
        said = done.stderr.decode("utf-8", "replace").strip()[:200]
        raise StampError(f"{call} failed: {said or f'exit {done.returncode}, nothing on stderr'}")
    return done.stdout


def read_landings(commit, builds, default_ref, default_commit=None):
    """{slug: [merge sha, ...]}, oldest first, for each slug of `builds`: the landing candidates TOOL-dTrackedAtlas-1's
    `derive_landings` reads at `commit` on the first-parent line of `default_commit`, which is `default_ref` resolved
    now when not passed (TOOL-dTrackedAtlas-10). StampError carrying the text of the module's StateError, its advice
    rewritten as CHECK_REMEDY by `render_state_error` (TOOL-dTrackedAtlas-12)."""
    build_state = load_build_state()
    memory_root = BUILD.parent.parent.relative_to(REPO).as_posix()
    try:
        if default_commit is None:
            _, default_commit = build_state.resolve_default_ref(str(REPO), default_ref)
        found = build_state.derive_landings(str(REPO), commit, default_commit, memory_root, tuple(builds))
    except build_state.StateError as e:
        raise StampError(render_state_error(e, CHECK_REMEDY)) from None
    return {b: [sha for sha, _, _ in found[b]] for b in builds}


def derive_input_digest(commit, inputs, default_ref, landings):
    """The 64-hex SHA-256 of the raw stdout of `git ls-tree -r -z <commit> -- <inputs>`, a NUL byte, and the compact
    sorted JSON of `default_ref` and `landings` (TOOL-dTrackedAtlas-10), so a landing merge that moves no input file
    still moves the digest; `-z` keeps it independent of core.quotePath."""
    history = json.dumps({"default_ref": default_ref, "landings": landings},
                         sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(read_git("ls-tree", "-r", "-z", commit, "--", *inputs) + b"\0" + history).hexdigest()


def build_stamp(data):
    """The page's stamp (TOOL-dTrackedAtlas-3): the commit the chain state was read at, the tracked inputs the page
    derives from, the default-branch ref and each chain build's landing candidates (TOOL-dTrackedAtlas-10), their
    digest at that commit, and the inputs the working tree differs in. StampError when the state's commit or
    default_ref fails its STAMP_RULES row before any git call, its default_commit fails the commit row, a git call
    fails, or the stamp it would return fails a row, so it never writes a stamp `read_stamp` refuses
    (TOOL-dTrackedAtlas-12)."""
    state = data.get("state") or {}
    commit, default_ref, default_commit = state.get("commit"), state.get("default_ref"), state.get("default_commit")
    reason = check_stamp({"commit": commit, "default_ref": default_ref}, ("commit", "default_ref"))
    if reason:
        raise StampError(reason)
    if not STAMP_RULES["commit"](default_commit):
        raise StampError(f"the chain state carries no 40-hex default_commit, but {default_commit!r}")
    fixed = [(BUILD / "README.md").relative_to(REPO).as_posix(), HERE.relative_to(REPO).as_posix() + "/",
             REVIEWS.relative_to(REPO).as_posix() + "/", (REPO / ".memory-tree.conf").relative_to(REPO).as_posix(),
             STATE_PATH.relative_to(REPO).as_posix()]
    slugs = [b["slug"] for b in state.get("builds", [])]
    builds = [(BUILD.parent / b).relative_to(REPO).as_posix() + "/" for b in slugs]
    inputs = sorted(set(fixed + builds))
    landings = read_landings(commit, slugs, default_ref, default_commit)
    dirty = set()
    for listing in (read_git("diff", "--name-only", "-z", commit, "--", *inputs),
                    read_git("ls-files", "--others", "--exclude-standard", "-z", "--", *inputs)):
        dirty.update(p for p in listing.decode("utf-8", "replace").split("\0") if p)
    stamp = {"schema": STAMP_SCHEMA, "commit": commit, "default_ref": default_ref, "landings": landings,
             "digest": derive_input_digest(commit, inputs, default_ref, landings), "inputs": inputs,
             "dirty": sorted(dirty)}
    reason = check_stamp(stamp)
    if reason:
        raise StampError(reason)
    return stamp


def read_stamp(page):
    """`(stamp, None)` for a page whose data carries a stamp passing every field's rule, else `(None, reason)`: no
    data marker, data that does not parse, no stamp, or a field outside its rule. This is the read boundary."""
    try:
        body = Path(page).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return None, f"the page does not read as UTF-8 text: {e}"
    if MARK not in body:
        return None, "no data marker"
    try:
        data = json.loads(body.split(MARK, 1)[1].split("</script>", 1)[0])
    except ValueError as e:
        return None, f"its data does not parse: {e}"
    stamp = data.get("stamp") if isinstance(data, dict) else None
    if not isinstance(stamp, dict):
        return None, "its data carries no stamp"
    reason = check_stamp(stamp)
    return (None, reason) if reason else (stamp, None)


def check_page(page, ref="HEAD"):
    """Print whether the tree at `ref` has moved an input `page` was stamped with, or a landing it shows, read
    against the stamp's default_ref resolved now (TOOL-dTrackedAtlas-10), and return the exit code: 0 current, 1
    stale, dirty, unstamped or absent, 2 when it cannot answer. Reads the page and git, writes nothing and derives
    nothing. The order is absent, unstamped, the ref and the digest at it, dirty, stale, current."""
    def print_refusal(reason):
        print(f"atlas: cannot check: {reason}", file=sys.stderr)
        return 2

    if not Path(page).is_file():
        print(f"atlas: absent — no page at {page}")
        return 1
    stamp, reason = read_stamp(page)
    if stamp is None:
        print(f"atlas: unstamped — {page}: {reason}")
        return 1
    try:
        try:
            at = read_git("rev-parse", "--verify", "-q", f"{ref}^{{commit}}").decode().strip()
        except StampError as e:
            return print_refusal(f"{ref} resolves to no commit: {e}")
        landings = read_landings(at, sorted(stamp["landings"]), stamp["default_ref"])
        digest = derive_input_digest(at, stamp["inputs"], stamp["default_ref"], landings)
        c12, r12 = stamp["commit"][:12], at[:12]
        if stamp["dirty"]:
            print(f"atlas: dirty — {page}: generated with {len(stamp['dirty'])} uncommitted input(s), "
                  f"first {stamp['dirty'][0]}")
            return 1
        if digest == stamp["digest"]:
            print(f"atlas: current — {page}: inputs {digest[:12]} at {ref} ({r12}) match the stamp of {c12}")
            return 0
        print(f"atlas: stale — {page}: the inputs stamped at {c12} moved by {ref} ({r12})")
        for b in sorted(landings):
            if landings[b] != stamp["landings"][b]:
                print(f"  landings of {b} moved: {landings[b][-1][:12] if landings[b] else 'none'}")
        try:
            read_git("cat-file", "-e", f"{stamp['commit']}^{{commit}}")
        except StampError:
            print(f"  the stamp's commit {c12} is not in this repository")
            return 1
        moved = [ln.partition("\t") for ln in read_git(
            "log", "--first-parent", "--format=%H%x09%s", f"{stamp['commit']}..{at}", "--", *stamp["inputs"]
        ).decode("utf-8", "replace").splitlines() if ln]
        for h, _, subject in moved[:20]:
            print(f"  {h[:12]} {subject}")
        if len(moved) > 20:
            print(f"  and {len(moved) - 20} more")
        return 1
    except StampError as e:
        return print_refusal(str(e))


VALUED_OPTIONS = ("--page", "--ref", "--claims", "--plant", "--out")


def read_options(argv):
    """({option: value} for each option of VALUED_OPTIONS present in argv, None), or
    (None, "<option> takes a value") for the first option of VALUED_OPTIONS, in that tuple's order,
    that is the last argument or whose next argument starts with "-". An option present more than once
    reads its first occurrence. This is the one place in the generator that indexes argv."""
    values = {}
    for option in VALUED_OPTIONS:
        if option not in argv:
            continue
        at = argv.index(option) + 1
        if at >= len(argv) or argv[at].startswith("-"):
            return None, f"{option} takes a value"
        values[option] = argv[at]
    return values, None


def main(argv):
    values, reason = read_options(argv)
    if "--page" in argv:
        if reason:
            print(f"atlas: cannot check: {reason}", file=sys.stderr)
            return 2
        mixed = [o for o in ("--plant", "--out", "--claims") if o in argv]
        if "--check" not in argv or mixed:
            print(f"atlas: cannot check: --page takes a page path and runs with --check and an optional --ref alone"
                  f"{', not ' + ' '.join(mixed) if mixed else ''}", file=sys.stderr)
            return 2
        return check_page(values["--page"], values.get("--ref", "HEAD"))
    if reason:
        sys.exit(f"atlas: {reason}")
    ref = values.get("--ref", "HEAD")
    claims = values.get("--claims", "cache")
    if claims not in ("cache", "none"):
        sys.exit(f"atlas: --claims takes cache or none, not {claims}")
    plant = values.get("--plant")
    data = derive_actual(derive(plant), ref, claims == "cache", plant)
    if "--check" in argv:
        n = sum(len(r["sections"]) for r in data["records"])
        print(f"atlas: derived — {len(data['records'])} records, {n} sections, {len(data['decisions'])} decision sections, "
              f"{len(data['areas'])} comparison areas, {len(data['principles'])} principles")
        return 0
    if "--out" not in argv:
        sys.exit(__doc__)
    out = Path(values["--out"])
    try:
        data["stamp"] = build_stamp(data)
    except StampError as e:
        sys.exit(f"atlas: cannot stamp the page: {e}")
    # Every "<" is escaped, so no record text can open a comment or close the script that carries it.
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    page = TEMPLATE.read_text(encoding="utf-8")
    if page.count(MARK) != 1:
        sys.exit("atlas: the template has no single data marker")
    head, rest = page.split(MARK, 1)
    _, tail = rest.split("</script>", 1)
    out.write_text(head + MARK + blob + "</script>" + tail, encoding="utf-8", newline="\n")
    print(f"atlas: wrote {out} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
