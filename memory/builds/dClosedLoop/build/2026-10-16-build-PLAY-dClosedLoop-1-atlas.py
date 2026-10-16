"""Derive the Closed Loop Atlas's data from dClosedLoop's design records, and write it into the page.

Usage: python 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py [--check]

Paths resolve beside this file. The run writes the derived JSON between the page's data markers; with
--check it writes nothing and exits 1 when the page's data differs from a fresh derivation. Every table
it reads must parse whole, and every population it reads is counted against the raw lines that carry
it, so a row it cannot place stops the run instead of leaving the atlas.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REVIEWS = HERE.parent / "reviews"
PAGE = HERE / "2026-10-16-build-PLAY-dClosedLoop-1-atlas.html"
MARK = '<script id="atlas-data" type="application/json">'


def record(name):
    found = sorted(HERE.glob(f"*-build-PLAY-dClosedLoop-1-{name}.md"))
    if len(found) != 1:
        sys.exit(f"atlas: {len(found)} records named {name}")
    return found[0]


SOURCES = {key: record(name) for key, name in {
    "v2": "architecture-v2", "gaps": "gap-register", "steps": "flow-steps", "roles": "layer-roles",
    "instruction": "layer-instruction", "library": "layer-library"}.items()}
LAYER_RECORDS = {
    "instruction": ["layer-instruction"],
    "flow": ["layer-flow", "flow-steps", "flow-roles"],
    "roles": ["layer-roles"],
    "memory": ["layer-memory", "layer-library"],
    "runtime": ["layer-runtime"],
}
STEPS = ["entry", "plan", "design", "build", "test", "deploy", "breakpoint", "lifecycle"]
KINDS = ("command", "executor", "hook", "owner")
SEP = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")
ITEM_TAG = re.compile(r"`([a-z]+\.[a-z0-9-]+)`")
GAP_ID = re.compile(r"gap-[a-z]+-\d\d")


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
    """The `- ` lines that follow a lead-in line, up to the first blank line."""
    if lead not in block:
        sys.exit(f"atlas: no lead-in {lead!r}")
    after = block.split(lead, 1)[1].lstrip("\n").split("\n\n", 1)[0]
    items = [ln[2:].strip() for ln in after.split("\n") if ln.startswith("- ")]
    if not items:
        sys.exit(f"atlas: no bullets after {lead!r}")
    return items


def paragraph(block, opener):
    m = re.search(r"^" + re.escape(opener) + r"(.*?)(?=\n\n|\Z)", block, flags=re.M | re.S)
    return re.sub(r"\s*\n\s*", " ", (opener + m.group(1))).strip() if m else ""


def derive():
    src = {k: text(p) for k, p in SOURCES.items()}
    v2, steps_text = src["v2"], src["steps"]

    # The layers, their cycle and their contract (v2 [layers]); the kits (layer-instruction).
    _, lay = section(v2, "layers")
    layers = [{"tag": plain(r[0]), "kind": r[1], "what": r[2]} for r in table(lay, "Layer", "v2 [layers]")]
    cycle = bullets(lay, "The core is a cycle on a base:")
    contract = bullets(lay, "Every layer fills one contract, whether core or expansion:")
    one_line = re.search(r"^In one line: (.+)$", src["instruction"], flags=re.M)
    kits = [{"kit": r[0], "layer": r[1], "kind": r[2]}
            for r in table(src["instruction"], "Kit or tool", "layer-instruction")]

    # The steps and their items (flow-steps), each table body row an item, counted against the raw rows.
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
                          "role": "" if head in KINDS else head, "needs": r[2], "does": r[3],
                          "proof": r[4], "then": r[5]})
            all_tags.add(plain(r[0]))
        steps.append({"tag": tag, "title": title.split("]")[-1].strip(),
                      "enters": paragraph(block, "**Enters**"), "exits": paragraph(block, "**Exits**"),
                      "items": items})
    for s in steps:
        for it in s["items"]:
            it["needsRefs"] = [t for t in ITEM_TAG.findall(it["needs"]) if t in all_tags]
            it["thenRefs"] = [t for t in ITEM_TAG.findall(it["then"]) if t in all_tags]

    # The build's states (flow-steps [transitions]).
    _, trans = section(steps_text, "transitions")
    transitions = [{"from": r[0], "on": r[1], "to": r[2], "witness": r[3]} for r in table(trans, "From", "[transitions]")]
    term = re.search(r"^((?:[A-Z][a-z]+)(?:, [a-z]+)* and [a-z]+) are terminal\.", trans, flags=re.M)
    if not term:
        sys.exit("atlas: no terminal-state sentence in [transitions]")
    terminal = [t.strip().lower() for t in re.split(r", | and ", term.group(1))]

    # The stage contracts (v2 [contracts]) and the roster (layer-roles [roster]).
    _, con = section(v2, "contracts")
    contracts = [{"stage": r[0], "takes": r[1], "hands": r[2], "witness": r[3], "gate": r[4], "review": r[5]}
                 for r in table(con, "Stage", "v2 [contracts]")]
    _, ros = section(src["roles"], "roster")
    roster = [{"role": r[0], "layer": r[1], "acts": r[2]} for r in table(ros, "Role", "layer-roles [roster]")]

    # The chain (v2 [chain]) and the gaps it owns (the gap register), joined both ways.
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

    # The policy catalogue and the presets (v2 [policies], [presets]).
    _, pol = section(v2, "policies")
    policies = [{"key": plain(r[0]), "values": r[1], "default": r[2], "source": r[3]} for r in table(pol, "Key", "v2 [policies]")]
    _, pre = section(v2, "presets")
    head = next(h for h, _ in tables(pre) if h[0] == "Key")
    names = [re.sub(r"\s*\(default\)", "", h) for h in head[1:]]
    presets = {"names": names, "rows": {plain(r[0]): r[1:] for r in table(pre, "Key", "v2 [presets]")}}

    # The design's own history: v2's revision lines, the reviews, each layer's records.
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
        scope = re.sub(r"^.*-PLAY-dClosedLoop-1-", "", p.stem)
        reviews.append({"file": p.name, "date": p.name[:10], "scope": scope, "verdict": verdict.group(1),
                        **{k: fields[k] for k in ("kind", "round", "intensity")},
                        **{k: int(fields[k]) for k in ("raw", "confirmed", "refuted", "blocker", "high", "medium", "low", "agents", "out-tokens")}})
    progress = []
    for layer, names in LAYER_RECORDS.items():
        recs = [record(n) for n in names]
        progress.append({"layer": layer, "records": [r.name for r in recs],
                         "reviews": [r["file"] for r in reviews if re.fullmatch(rf"{layer}-[ab]", r["scope"])],
                         "folded": any("\n## [revised]" in text(r) or re.search(r"^Revised: .*Tier-2", text(r), flags=re.M)
                                       for r in recs)})
    _, op = section(src["library"], "open")
    open_items, cur = [], None
    for ln in op.split("\n"):
        m = re.match(r"^- \*\*(.+?)\*\*:?\s*(.*)$", ln)
        if m:
            cur = {"label": m.group(1).rstrip(":"), "text": m.group(2), "items": []}
            open_items.append(cur)
        elif ln.startswith("  - ") and cur:
            cur["items"].append(ln[4:].strip())
        elif ln.startswith("    ") and cur and cur["items"]:
            cur["items"][-1] += " " + ln.strip()
        elif ln.startswith("  ") and cur and not cur["items"]:
            cur["text"] += " " + ln.strip()

    digest = hashlib.sha256()
    for p in [*SOURCES.values(), *sorted(REVIEWS.glob("*.md"))]:
        digest.update(p.read_bytes())
    return {
        "build": "dClosedLoop", "digest": digest.hexdigest()[:12],
        "latest": max(t["date"] for t in timeline),
        "oneLine": one_line.group(1) if one_line else "",
        "layers": layers, "cycle": cycle, "contract": contract, "kits": kits,
        "steps": steps, "transitions": transitions, "terminal": terminal, "contracts": contracts,
        "roster": roster, "chain": chain, "gaps": gaps, "policies": policies, "presets": presets,
        "timeline": timeline, "reviews": reviews, "progress": progress, "open": open_items,
        "sources": {k: p.name for k, p in SOURCES.items()},
    }


def main(argv):
    data = json.dumps(derive(), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = PAGE.read_text(encoding="utf-8")
    if page.count(MARK) != 1:
        sys.exit("atlas: the page has no single data marker")
    head, rest = page.split(MARK, 1)
    _, tail = rest.split("</script>", 1)
    fresh = head + MARK + data + "</script>" + tail
    if "--check" in argv:
        if fresh != page:
            print("atlas: STALE — the page's data differs from the records; run without --check")
            return 1
        print("atlas: current")
        return 0
    if fresh != page:
        PAGE.write_text(fresh, encoding="utf-8", newline="\n")
        print(f"atlas: wrote {PAGE.name}")
    else:
        print("atlas: unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
