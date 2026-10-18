# **Serves:** research PLAY-dClosedLoop-1
"""Derive the Closed Loop Atlas from dClosedLoop's records, and write the publishable page.

Usage: python 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --out <page.html>
       python 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check

The template beside this file is the page without its data. A run splices the derived data into a copy
written to --out, never into the template, so the repository keeps the template and this generator while
the page, which embeds every record, stays out of it. --check derives everything and writes nothing.

Nothing the records hold may leave the atlas without a refusal:
- every table it reads parses whole, and each population is counted against the raw lines that carry it;
- every record splits into sections that rejoin to its exact text;
- every gap stage maps to one comparison area, and every source an area names resolves;
- every design record that records an owner's answer contributes a decision section.
"""
import hashlib
import json
import re
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
    "expansions": "layer-expansions", "fates": "fates"}.items()}
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
V2_VIEWS = {"layers": "overview", "principles": "principles", "front-door": "records", "policies": "policies",
            "presets": "policies", "floor": "records", "witnesses": "records", "contracts": "flow", "chain": "chain",
            "open": "progress", "owed": "progress"}


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
    paths = [BUILD / "README.md"] + sorted(HERE.glob("*.md")) + sorted(REVIEWS.glob("*.md"))
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


def derive():
    src = {k: text(p) for k, p in SOURCES.items()}
    v2, steps_text = src["v2"], src["steps"]
    recs = corpus()

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
    if sorted(v2_ids) != sorted(V2_VIEWS):
        sys.exit(f"atlas: v2's sections and the views declared for them differ: {sorted(set(v2_ids) ^ set(V2_VIEWS))}")
    # The expansions' programs: each layer-expansions table headed `| Item | Actor |` is one program's, outside the
    # steps, and a row may name two items (PM-12).
    programs = []
    for head, rows in tables(src["expansions"]):
        if head[:2] != ["Item", "Actor"]:
            continue
        its = [{"tag": t, "actor": r[1], "does": r[2], "witness": r[3], "routes": r[4],
                "owner": r[head.index("Owner")] if "Owner" in head else ""} for r in rows for t in ITEM_TAG.findall(r[0])]
        programs.append({"program": its[0]["tag"].split(".")[0], "items": its})

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
        "events": events, "v2map": v2map, "records": recs,
        "sources": {k: p.relative_to(REPO).as_posix() for k, p in SOURCES.items()},
    }


def main(argv):
    data = derive()
    if "--check" in argv:
        n = sum(len(r["sections"]) for r in data["records"])
        print(f"atlas: derived — {len(data['records'])} records, {n} sections, {len(data['decisions'])} decision sections, "
              f"{len(data['areas'])} comparison areas, {len(data['principles'])} principles")
        return 0
    if "--out" not in argv:
        sys.exit(__doc__)
    out = Path(argv[argv.index("--out") + 1])
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
