# **Serves:** research PLAY-dClosedLoop-1
"""Derive the level-0 project map of dClosedLoop's design and of the tree it governs, as the project-map
record designs it (`2026-10-17-build-PLAY-dClosedLoop-1-project-map.md` `[design]`, PM-1 to PM-7), and
check it.

Usage:
  python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --out <map.txt>    derive, check, write the map (level 0)
  python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --ns <namespace>   print one namespace whole (level 1)
  python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --check            derive and check; write nothing
  python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --check --plant <case>   damage the render, expect exit 1
      cases: drop-line, bad-count, ghost-rel, no-layer, fates-drop, fates-ghost, fates-bad, fates-unbuilt,
      fates-empty, fates-kit, census, no-owner, orphan (an item's owner emptied), two-owners,
      inferred (a point's owner kept with its declaration dropped)
  python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --pending          list the nodes whose purpose waits on the owner
  --unfold <ns>[,<ns>...] renders those namespaces node by node, as an item's declared unfolds would.

A design-time instrument, like the atlas generator beside it. The one index the design reads does not exist
yet, so each namespace is derived from the source the index will extract it from. The atlas's derivation is
imported, so the map and the atlas are two renders of one node table, and the parity check holds them
together. The map is a view: it is written where --out says, never committed.

Exit codes: 0 when every check passes and every registered namespace is armed; 1 on any finding; 2 when the
checks pass but a registered namespace is unarmed, which never reads green.
"""
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
BUDGET = 32 * 1024          # memory.map-budget, 32k (PM-4)
PURPOSE, PURPOSE_DEGRADED = 60, 40
FOLD_PAST = 40              # a namespace whose registry row says neither line nor fold folds past 40 nodes
SPLIT = " · "
# The nodes a build must build, each owning build declared once on the node (PM-8, PM-10). An owner is read only
# from a declared field, and the extractor that reads it records the node in DECLARED: the no-inference check.
OWNED = ("item", "policy-key", "point", "record-kind", "tag-namespace", "system")
DECLARED = set()
# Kits whose row in the instruction layer's kits table says "no layer"; every other kit joins a layer (the layer arm).
NO_LAYER = set()
# The fates record (night pass, point 8): each kit's declared fate, and every part's row, read for the fates arms.
FATES = HERE / "2026-10-18-build-PLAY-dClosedLoop-1-fates.md"
FATE_KITS, FATE_ROWS = {}, []
FATE_KIT_SET = {"kept", "optional", "absorbed", "retired"}
FATE_ROW_SET = {"STAYS", "RESHAPED", "MERGED", "RETIRED"}
FATE_PSEUDO = {"top-level", "skills", ".githooks", "guides"}

spec = importlib.util.spec_from_file_location("atlas", HERE / "2026-10-16-build-PLAY-dClosedLoop-1-atlas.py")
atlas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atlas)


def text(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def git(*args):
    r = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, encoding="utf-8")
    return r.stdout.strip()


def cut(s, n):
    """A purpose, verbatim but for markup and dates: a line never holds a date (the map's no-stale-facts rule)."""
    s = re.sub(r"\s*[(,]?\s*\b20\d\d-\d\d-\d\d\b\s*\)?", "", s or "")
    s = re.sub(r"\s+", " ", re.sub(r"[`*]", "", s)).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def node(key, purpose="", src="declared", counts=(), rels=()):
    return {"key": key, "purpose": purpose or "", "src": src if purpose else "pending",
            "counts": [c for c in counts if c[1] is not None], "rels": [r for r in rels if r[1]]}


def section(body, tag):
    m = re.search(r"^## \[" + re.escape(tag) + r"\]([^\n]*)\n(.*?)(?=^## |\Z)", body, flags=re.M | re.S)
    if not m:
        sys.exit(f"map: no section [{tag}]")
    return m.group(1).strip(), m.group(2)


def first_comment(path):
    """A script's first comment line after its shebang: the purpose its author wrote, derived (PM-5)."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").split("\n")[:40]
    except OSError:
        return ""
    for ln in lines:
        s = ln.strip()
        if s.startswith("#!") or not s:
            continue
        m = re.match(r"^(?:#+|//+|/\*+|\*+)\s*(.+?)\s*(?:\*/)?$", s)
        if m and len(m.group(1)) > 8 and not re.match(r"(?i)^(eslint|@ts-|-\*-|shellcheck|use strict)", m.group(1)):
            return m.group(1)
        if not s.startswith(("#", "//", "/*", "*", "'use strict'", '"use strict"')):
            return ""
    return ""


# ---------------------------------------------------------------------------------------------- the node table
def derive():
    A = atlas.derive()
    ns = {}
    DECLARED.clear()
    chain_names = {c["build"] for c in A["chain"]}

    kits_by_layer = {}
    for k in A["kits"]:
        kits_by_layer[k["layer"]] = kits_by_layer.get(k["layer"], 0) + 1
    ns["layer"] = [node(l["tag"], l["what"], counts=[("kits", kits_by_layer.get(l["tag"]))]) for l in A["layers"]]
    ns["principle"] = [node(f"P{p['n']}", p["title"]) for p in A["principles"]]

    # The seven systems: five in the systems record's [design], retrofit and the project map in their own.
    sysrec = text("memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md")
    _, sdesign = section(sysrec, "design")
    systems = []
    for m in re.finditer(r"^### \[design-([a-z-]+)\] ([^\n]+)\n(.*?)(?=^### |\Z)", sdesign, flags=re.M | re.S):
        owner = re.search(r"\*\*Owners\.\*\*.*?\b(d[A-Z][a-z]+[A-Z]\w+)", m.group(3), flags=re.S)
        keys = len(re.findall(r"^\s*\| `[a-z]+\.[a-z0-9.-]+` \|", m.group(3), flags=re.M))
        if owner:
            DECLARED.add(("system", m.group(1)))
        systems.append(node(m.group(1), m.group(2), counts=[("keys", keys or None)],
                            rels=[("owner", [owner.group(1)] if owner else [])]))
    for name, rel, own_from in (("retrofit", "2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md", "owners"),
                                ("project-map", "2026-10-17-build-PLAY-dClosedLoop-1-project-map.md", "placement")):
        body = text("memory/builds/dClosedLoop/build/" + rel)
        h1 = re.search(r"^# (.+)$", body, flags=re.M).group(1)
        purpose = h1.split(": ", 1)[1] if ": " in h1 else h1
        own = re.search(r"\| (d[A-Z]\w+) \|" if own_from == "owners" else r"chain build (d[A-Z]\w+)", body.split(f"[{own_from}]", 1)[1])
        keys = len(re.findall(r"^\| `[a-z]+\.[a-z0-9.-]+` \|", section(body, "design")[1] if "## [design]" in body else "", flags=re.M))
        if own:
            DECLARED.add(("system", name))
        systems.append(node(name, purpose, counts=[("keys", keys or None)], rels=[("owner", [own.group(1)] if own else [])]))
    ns["system"] = systems

    ns["chain"] = [node(c["build"], c["stage"], counts=[("units", len([u for u in c["units"].split("; ") if u.strip()])),
                                                       ("gaps", len(c["gaps"]))],
                        rels=[("after", [p for p in c["parents"] if p in chain_names])]) for c in A["chain"]]

    # Steps and items read straight from flow-steps: every section whose table opens with "Item".
    # An item's owner is its table's Owner column; a step's owners are its items' owners, derived (PM-8).
    steps_text = text("memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")
    steps, items = [], []
    for m in re.finditer(r"^## \[([a-z-]+)\] ([^\n]+)\n(.*?)(?=^## |\Z)", steps_text, flags=re.M | re.S):
        rows = [atlas.cells(ln) for ln in m.group(3).split("\n") if ln.startswith("| `")]
        heads = [h for h, _ in atlas.tables(m.group(3)) if h and h[0] == "Item"]
        if not heads:
            continue
        owners = []
        for r in rows:
            own = r[6].strip() if len(r) > 6 else ""
            if own:
                DECLARED.add(("item", atlas.plain(r[0])))
                owners.append(own)
            items.append(node(atlas.plain(r[0]), r[3], rels=[("owner", [own] if own else [])]))
        steps.append(node(m.group(1), m.group(2), counts=[("items", len(rows))], rels=[("owner", sorted(set(owners)))]))
    ns["step"] = steps
    # The expansions' items: each layer-expansions table headed `| Item | Actor |` is one program's, outside the steps
    # (PM-12). A row may name two items, and each takes the row's Owner cell.
    expansions = text("memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md")
    for head, rows in atlas.tables(expansions):
        if head[:2] != ["Item", "Actor"]:
            continue
        oc = head.index("Owner") if "Owner" in head else None
        for r in rows:
            own = r[oc].strip() if oc is not None else ""
            for tag in re.findall(r"`([a-z]+\.[a-z0-9-]+)`", r[0]):
                if own:
                    DECLARED.add(("item", tag))
                items.append(node(tag, r[2], rels=[("owner", [own] if own else [])]))

    agents = {}
    for p in sorted((REPO / "tools/roles/agents").glob("gov-*.agent.md")):
        d = re.search(r"^description:\s*(.+)$", p.read_text(encoding="utf-8"), flags=re.M)
        agents[p.name.split(".")[0]] = d.group(1).strip().strip('"') if d else ""
    role_agent = {"orientation scout": "gov-orienter", "reuse scout": "gov-reuse-scout", "spec writer": "gov-spec-writer",
                  "builder": "gov-builder", "skeptic": "gov-skeptic", "synthesizer": "gov-synthesizer",
                  "researcher": "gov-researcher"}
    acts = {}
    for s in A["steps"]:
        for it in s["items"]:
            if it["role"]:
                acts[it["role"]] = acts.get(it["role"], 0) + 1
    roles = []
    for r in A["roster"]:
        purpose = agents.get(role_agent.get(r["role"], ""), "")
        roles.append(node(atlas.slug(r["role"]), purpose, src="derived", counts=[("items", acts.get(r["role"]))]))
    ns["role"] = roles

    cards = text("memory/map/generated/CARDS.md")
    feats = []
    for m in re.finditer(r"^## (\S+)\n\n(.+?)\n\n(.*?)(?=^## |\Z)", cards, flags=re.M | re.S):
        legs = re.search(r"^- gate-legs (\d+):", m.group(3), flags=re.M)
        feats.append(node(m.group(1), m.group(2), counts=[("legs", int(legs.group(1)) if legs else None)]))
    ns["feature"] = feats

    mapmd = text("memory/map/generated/MAP.md")
    kits_block = mapmd.split("\n## kits\n", 1)[1].split("\n## ", 1)[0]
    kit_names = [atlas.plain(atlas.cells(ln)[0]) for ln in kits_block.split("\n") if ln.startswith("| `")]
    # The instruction layer's kits table names one kit, or several joined by ", " or " and ", and opens its layer cell
    # with a layer's name, or two joined by " and ". A row whose kind cell says "no layer" places its kits on none.
    kit_layer = {}
    for row in A["kits"]:
        lead = re.match(r"\s*([A-Za-z]+(?:\s+and\s+[A-Za-z]+)?)", row["layer"])
        lays = [w.lower() for w in re.split(r"\s+and\s+", lead.group(1))] if lead else []
        for name in re.split(r",\s*|\s+and\s+", row["kit"]):
            name = name.strip().strip("`").split("/")[-1].strip()
            kit_layer.setdefault(name, lays)
            if row["kind"].strip() == "no layer":
                NO_LAYER.add(name)
    layer_tags = {l["tag"] for l in A["layers"]}
    kits = []
    for k in kit_names:
        readme = REPO / "tools" / k / "README.md"
        purpose = ""
        if readme.exists():
            body = readme.read_text(encoding="utf-8")
            h1 = re.search(r"^# (.+)$", body, flags=re.M)
            purpose = h1.group(1).split(" — ", 1)[1] if h1 and " — " in h1.group(1) else ""
            # A README's prose is never mined for a purpose. Its first prose line was, three kits in three, the middle
            # of a sentence or a disclaimer (the project-map record's [reload-summary]). PM-5's review derives those
            # purposes, citing its source, and until then the kit renders as pending.
        main_py = REPO / "tools" / k / f"{k}.py"
        if not purpose and main_py.exists():
            # No README: the kit's main script's docstring, its first line after the kit's name (PM-5).
            doc = re.search(r'"""(.+?)$', main_py.read_text(encoding="utf-8"), flags=re.M)
            purpose = doc.group(1).split(" — ", 1)[-1].strip() if doc else ""
        if not purpose:
            # Neither: the charter's own fact about the directory, where it states one (PM-5).
            fact = re.search(r"tools/" + re.escape(k) + r"/ — ([^.;]+)", text("AGENTS.md"))
            purpose = fact.group(1) if fact else ""
        kits.append(node(k, purpose, src="derived", rels=[("layer", [l for l in kit_layer.get(k, []) if l in layer_tags])]))
    if FATES.exists():
        body = FATES.read_text(encoding="utf-8")
        for tag, width, sink in (("kits", 3, "kits"), ("table", 6, "rows")):
            _, block = section(body, tag)
            for ln in block.split("\n"):
                c = atlas.cells(ln) if ln.startswith("| ") else []
                if len(c) == width and c[0] != "Kit" and not set(c[0]) <= set("-"):
                    if sink == "kits":
                        FATE_KITS[c[0]] = c[1]
                    else:
                        FATE_ROWS.append(c)
        for n in kits:
            if n["key"] in FATE_KITS:
                n["rels"].append(("fate", [FATE_KITS[n["key"]]]))
    ns["kit"] = kits

    live = text("memory/LIVE.md")
    live_rows = [atlas.cells(ln) for ln in live.split("\n") if ln.startswith("| [")]
    live_slugs = []
    builds_live = []
    for r in live_rows:
        slug = re.match(r"\[([^\]]+)\]", r[0]).group(1)
        live_slugs.append(slug)
        h1 = re.search(r"^# (.+)$", text(f"memory/builds/{slug}/README.md"), flags=re.M)
        purpose = h1.group(1).split(" — ", 1)[1] if h1 and " — " in h1.group(1) else ""
        builds_live.append(node(slug, purpose, counts=[("ids", int(r[5]) if r[5].isdigit() else None)]))
    ns["live-build"] = builds_live

    rt = text("memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md")
    ext = rt.split("### [extend]", 1)[1]
    points = []
    for r in atlas.table(ext.split("\n### ", 1)[0], "Extension point", "layer-runtime [extend]"):
        own = r[3].strip() if len(r) > 3 else ""
        if own:
            DECLARED.add(("point", atlas.slug(r[0])))
        points.append(node(atlas.slug(r[0]), r[1], rels=[("owner", [own] if own else [])]))
    ns["point"] = points

    settings = json.loads(text(".claude/settings.json"))
    entries = []
    for event, arr in settings.get("hooks", {}).items():
        for m in arr:
            for h in m.get("hooks", []):
                script = re.search(r"\}/([^\"]+?\.(?:js|sh|py))", h.get("command", ""))
                entries.append((event.lower(), Path(script.group(1)).stem if script else "command",
                                (m.get("matcher") or "any").split("|")[0].lower(), script))
    repeated = {(e, s) for e, s, _, _ in entries if sum(1 for x in entries if x[:2] == (e, s)) > 1}
    hooks = []
    for event, stem, matcher, script in entries:
        key = f"{event}.{stem}" + (f".{matcher}" if (event, stem) in repeated else "")
        hooks.append(node(key, first_comment(REPO / script.group(1)) if script else "", src="derived"))
    for g in ("commit-msg", "pre-commit", "pre-push", "pre-rebase"):
        hooks.append(node(f"git.{g}", first_comment(REPO / ".githooks" / g), src="derived"))
    ns["hook"] = hooks

    # The record kinds: layer-memory [contract]'s table, the design-time stand-in for the kind registry (PM-10).
    lm = text("memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md")
    contract = lm.split("### [contract]", 1)[1].split("\n### ", 1)[0]
    kinds = []
    for r in atlas.table(contract, "Kind", "layer-memory [contract]"):
        own = r[1].strip()
        if own:
            DECLARED.add(("record-kind", atlas.slug(r[0])))
        kinds.append(node(atlas.slug(r[0]), "", rels=[("owner", [own] if own else [])]))
    ns["record-kind"] = kinds

    tags_text = sdesign.split("### [design-tags]", 1)[1].split("\n### ", 1)[0]
    v2 = text("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
    rb = re.search(r"namespaced tag system \(([a-z, ]+)\)", v2)
    plus = re.search(r"\*\*Namespaces\.\*\* R-B's twelve, plus (.+?)\. Each namespace", tags_text, flags=re.S)
    names = [n.strip() for n in rb.group(1).split(",")] + re.findall(r"`([a-z]+)`", plus.group(1))
    # Each namespace's owner is declared on one of the Owners bullet's lines; none is defaulted (PM-8).
    owner_of = {}
    for m in re.finditer(r"^  - (d[A-Z]\w+)(?: registers)? (.+?)[;.]$", tags_text, flags=re.M):
        for t in re.findall(r"`([a-z]+)`", m.group(2)):
            owner_of[t] = m.group(1)
    seen, tagns = set(), []
    for n in names:
        if n in seen:
            continue
        seen.add(n)
        own = owner_of.get(n, "")
        if own:
            DECLARED.add(("tag-namespace", n))
        tagns.append(node(n, "", rels=[("owner", [own] if own else [])]))
    ns["tag-namespace"] = tagns

    # A policy namespace's owners are its keys' owners, derived.
    pol_ns, pol_own = {}, {}
    for p in A["policies"]:
        k = p["key"].split(".", 1)[0]
        pol_ns[k] = pol_ns.get(k, 0) + 1
        if p.get("owner"):
            pol_own.setdefault(k, set()).add(p["owner"])
    ns["policy-namespace"] = [node(k, "", counts=[("keys", v)], rels=[("owner", sorted(pol_own.get(k, ())))])
                              for k, v in sorted(pol_ns.items())]

    area_title = {}
    for a in atlas.AREAS:
        for st in a["stages"]:
            area_title[st] = a["title"]
    areas = {}
    for g in A["gaps"]:
        e = areas.setdefault(g["stage"], {"n": 0, "high": 0})
        e["n"] += 1
        e["high"] += g["sev"] == "HIGH"
    ns["gap-area"] = [node(k, area_title.get(k, ""), src="derived", counts=[("gaps", v["n"]), ("high", v["high"])])
                      for k, v in sorted(areas.items())]

    rounds = {}
    for d in A["decisions"]:
        rounds.setdefault(d["record"], []).append(d)
    rec_by_name = {r["name"]: r for r in A["records"]}
    rnodes = []
    for name, ds in sorted(rounds.items()):
        r = rec_by_name[name]
        md = "\n".join(s["md"] for s in r["sections"] if s["id"] in {d["id"] for d in ds})
        forks = sorted(set(re.findall(r"\b([A-Z]{2,3}-\d{1,2})\b", md)))
        rnodes.append(node(name, r["title"], counts=[("decisions", len(ds)), ("forks", len(forks) or None)]))
    ns["round"] = rnodes

    # The unbounded namespaces: each folds to one counted line, and --ns lists it whole.
    ns["item"] = items
    pkeys = []
    for p in A["policies"]:
        own = p.get("owner", "")
        if own:
            DECLARED.add(("policy-key", p["key"]))
        pkeys.append(node(p["key"], p["values"], src="derived", rels=[("owner", [own] if own else [])]))
    ns["policy-key"] = pkeys
    ns["gap"] = [node(g["id"], g["gap"], rels=[("owner", [g["owner"]])]) for g in A["gaps"]]
    legs = json.loads(text("tools/gate-legs.json"))
    ns["leg"] = [node(l["name"], l.get("doc", "") or "") for l in legs]
    classes = []
    for p in sorted((REPO / "memory/gotchas").glob("*.md")):
        b = p.read_text(encoding="utf-8")
        if re.search(r"^kind: class$", b, flags=re.M):
            d = re.search(r"^description: (.+)$", b, flags=re.M)
            classes.append(node(p.stem, d.group(1) if d else ""))
    ns["bug-class"] = classes
    closed = []
    for p in sorted((REPO / "memory/builds").glob("*/README.md")):
        slug = p.parent.name
        if slug in live_slugs:
            continue
        h1 = re.search(r"^# (.+)$", p.read_text(encoding="utf-8"), flags=re.M)
        closed.append(node(slug, h1.group(1).split(" — ", 1)[1] if h1 and " — " in h1.group(1) else ""))
    ns["closed-build"] = closed
    # A decision row's id names its unit, and one unit may record several decisions, so a repeated id is
    # keyed by its ordinal, as a repeated heading is (the systems record's [design-memory-structure]).
    rows = re.findall(r"^- \**([A-Z]+-[A-Za-z0-9]+-\d+)\**\s*[·—-]\s*(.+)$", text("memory/DECISIONS.md"), flags=re.M)
    total, nth = {}, {}
    for i, _ in rows:
        total[i] = total.get(i, 0) + 1
    drows = []
    for i, d in rows:
        nth[i] = nth.get(i, 0) + 1
        drows.append(node(f"{i}#{nth[i]}" if total[i] > 1 else i, d))
    ns["decision-row"] = drows
    ns["design-record"] = [node(r["name"], r["title"]) for r in A["records"] if r["group"] != "Reviews"]
    ns["review"] = [node(r["scope"], f"{r['kind']} round {r['round']}, {r['verdict']}") for r in A["reviews"]]
    ns["decision-section"] = [node(f"{d['record']}#{d['id']}", d["title"]) for d in A["decisions"]]
    ns["event"] = [node(f"{i + 1}", e["md"].split("\n", 1)[0]) for i, e in enumerate(A["events"])]
    pop = sorted(n for n in git("ls-files").split("\n")
                 if (n.startswith("memory/project/") and n.endswith(".txt") and n.count("/") == 2)
                 or (n.startswith("tools/") and "waivers" in n.rsplit("/", 1)[-1] and n.endswith(".txt"))
                 or n in ("memory/map/baseline.toml", "memory/map/affordance-exempt.toml"))
    ns["population"] = [node(p, "") for p in pop]
    markers = sorted(set(re.findall(r"gov:[a-z][a-z-]*", git("grep", "-h", "-o", "-E", "gov:[a-z][a-z-]*", "--", ":!memory/", ":!*.md"))))
    ns["marker"] = [node(m, "") for m in markers]
    confs = []
    for c in (".memory-tree.conf", ".codebase-map.conf", ".lexicon.conf", ".unattended.conf"):
        for ln in text(c).split("\n"):
            m = re.match(r"^([A-Z][A-Z0-9_]*)=", ln)
            if m:
                confs.append(node(f"{c.strip('.')}:{m.group(1)}", ""))
    ns["conf-key"] = confs
    return A, ns


# The namespace registry: the declared order, each namespace's map mode, and where the design owns it.
REGISTRY = [
    ("layer", "line"), ("principle", "line"), ("system", "line"), ("chain", "line"), ("step", "line"),
    ("role", "line"), ("feature", "line"), ("kit", "line"), ("live-build", "line"), ("point", "line"),
    ("hook", "line"), ("record-kind", "line"), ("tag-namespace", "line"), ("policy-namespace", "line"),
    ("gap-area", "line"), ("round", "line"),
    ("item", "fold"), ("policy-key", "fold"), ("gap", "fold"), ("leg", "fold"), ("bug-class", "fold"),
    ("closed-build", "fold"), ("decision-row", "fold"), ("design-record", "fold"), ("review", "fold"),
    ("decision-section", "fold"), ("event", "fold"), ("population", "fold"), ("marker", "fold"), ("conf-key", "fold"),
]
REL_NS = {"after": "chain", "owner": "chain", "layer": "layer"}


def unowned(ns):
    return [(name, n["key"]) for name in OWNED for n in (ns.get(name) or []) if not any(k == "owner" for k, _ in n["rels"])]


# ------------------------------------------------------------------------------------------------- rendering
def line(ns, n, width):
    parts = [f"- {ns}.{n['key']} — {cut(n['purpose'], width) if n['purpose'] else '—'}"]
    if n["counts"]:
        parts.append(", ".join(f"{k} {v}" for k, v in n["counts"]))
    rels = list(n["rels"])
    if ns in OWNED and not any(k == "owner" for k, _ in rels):
        rels.append(("owner", ["?"]))   # a required field that is missing renders ?, never a blank
    if rels:
        parts.append(" ".join(f"{k}={','.join(v)}" for k, v in rels))
    return SPLIT.join(parts)


def render(ns, unfold=(), width=PURPOSE, folded_extra=()):
    tree = git("rev-parse", "HEAD^{tree}")[:8]
    dirty = bool(git("status", "--porcelain", "--", "memory/", "tools/", ".claude/"))
    body, folded, unarmed = [], [], []
    for name, mode in REGISTRY:
        nodes = ns.get(name)
        if nodes is None:
            unarmed.append(name)
            continue
        fold = name not in unfold and (mode == "fold" or name in folded_extra or (mode == "auto" and len(nodes) > FOLD_PAST))
        if fold:
            folded.append(name)
            body.append(f"- {name}.* — {len(nodes)} nodes · gov map {name}")
        else:
            body.extend(line(name, n, width) for n in nodes)
        body.append("")
    pending = sum(1 for name, _ in REGISTRY if ns.get(name) for n in ns[name] if not n["purpose"] and name not in folded)
    head = (f"map {tree}{' dirty' if dirty else ''} · nodes {sum(len(v) for v in ns.values() if v)} · lines "
            f"{sum(1 for b in body if b)} · folded {','.join(folded) or 'none'} · pending {pending}")
    if unowned(ns):
        head += f" · unowned {len(unowned(ns))}"
    if unarmed:
        head += f" · unarmed {','.join(unarmed)}"
    if width != PURPOSE:
        head += f" · purposes cut to {width}"
    return "\n".join([head, ""] + body).rstrip("\n") + "\n", folded, unarmed


def fit(ns, unfold=()):
    """Render within the budget, degrading in the design's fixed order, never dropping a node."""
    out, folded, unarmed = render(ns, unfold)
    if len(out.encode("utf-8")) <= BUDGET:
        return out, folded, unarmed, []
    steps = [f"purposes {PURPOSE_DEGRADED}"]
    out, folded, unarmed = render(ns, unfold, PURPOSE_DEGRADED)
    extra = []
    for name, mode in reversed(REGISTRY):
        if len(out.encode("utf-8")) <= BUDGET:
            break
        if mode == "line" and ns.get(name) and name not in unfold:
            extra.append(name)
            steps.append(f"fold {name}")
            out, folded, unarmed = render(ns, unfold, PURPOSE_DEGRADED, extra)
    return out, folded, unarmed, steps


# --------------------------------------------------------------------------------------------------- checks
LINE = re.compile(r"^- ([a-z-]+)\.(.+?) — (.+)$")
NSLINE = re.compile(r"^- ([a-z-]+)\.\* — (\d+) nodes · gov map ([a-z-]+)$")


def expansion_items(le):
    """The expansions' item tags, counted from the raw lines under each `| Item | Actor |` header."""
    n = 0
    for block in le.split("\n| Item | Actor |")[1:]:
        for ln in block.split("\n")[2:]:      # past the header's rest and its separator
            if not ln.startswith("| `"):
                break
            n += len(re.findall(r"`[a-z]+\.[a-z0-9-]+`", ln.split(" | ", 1)[0]))
    return n


def census():
    """Each population counted from disk by a route that shares nothing with the builders above."""
    v2 = text("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
    steps = text("memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")
    reg = text("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md")
    pol = v2.split("\n## [policies]", 1)[1].split("\n## ", 1)[0]
    ch = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    lm = text("memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md")
    contract = lm.split("\n### [contract]", 1)[1].split("\n### ", 1)[0]
    return {
        "record-kind": len(re.findall(r"(?m)^\| [a-z][a-z -]* \| d[A-Z]\w+ \| ", contract)),
        "principle": len(re.findall(r"(?m)^- \*\*P\d+ ", v2)),
        "chain": len(re.findall(r"(?m)^\| d[A-Z]", ch)),
        "item": len(re.findall(r"(?m)^\| `[a-z]+\.[a-z0-9-]+` \|", steps)) + expansion_items(
            text("memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md")),
        "gap": len(re.findall(r"(?m)^\| gap-[a-z]+-\d\d \|", reg)),
        "policy-key": len(re.findall(r"(?m)^\| `[a-z]", pol)),
        "leg": text("tools/gate-legs.json").count('"name"'),
        "bug-class": sum(1 for p in (REPO / "memory/gotchas").glob("*.md") if "\nkind: class\n" in p.read_text(encoding="utf-8")),
        "feature": len(re.findall(r"(?m)^## ", text("memory/map/generated/CARDS.md"))),
        "live-build": len(re.findall(r"(?m)^\| \[", text("memory/LIVE.md"))),
        "kit-dirs": sorted(p.parent.name for p in (REPO / "tools").glob("*/kit.toml")),
        "hook": len(re.findall(r'"command"\s*:', text(".claude/settings.json"))) + len(
            [p for p in (REPO / ".githooks").iterdir() if p.name in ("commit-msg", "pre-commit", "pre-push", "pre-rebase")]),
        "decision-row": len(re.findall(r"(?m)^- \**[A-Z]+-[A-Za-z0-9]+-\d+", text("memory/DECISIONS.md"))),
    }


def check(A, ns, out, folded, plant=None):
    findings = []
    lines = out.split("\n")
    if plant == "drop-line":
        i = next(i for i, ln in enumerate(lines) if LINE.match(ln) and not NSLINE.match(ln))
        lines = lines[:i] + lines[i + 1:]
    elif plant == "bad-count":
        i = next(i for i, ln in enumerate(lines) if NSLINE.match(ln))
        m = NSLINE.match(lines[i])
        lines[i] = lines[i].replace(f" — {m.group(2)} nodes", f" — {int(m.group(2)) + 1} nodes")
    elif plant == "ghost-rel":
        i = next(i for i, ln in enumerate(lines) if ln.startswith("- chain."))
        lines[i] += " owner=dGhostBuild"
    elif plant == "no-layer":
        i = next(i for i, ln in enumerate(lines) if ln.startswith("- kit.") and " layer=" in ln)
        lines[i] = re.sub(r" · layer=\S+", "", lines[i])
    seen, counts = {}, {}
    for ln in lines[2:]:
        if not ln.strip():
            continue
        m = NSLINE.match(ln)
        if m:
            counts[m.group(1)] = int(m.group(2))
            continue
        m = LINE.match(ln)
        if not m:
            findings.append(f"complete: a line the grammar cannot read: {ln[:80]}")
            continue
        seen.setdefault(m.group(1), set()).add(m.group(2))
        for rel in re.findall(r"\b(after|owner|layer)=([^\s·]+)", m.group(3)):
            for target in rel[1].split(","):
                if target == "?":
                    continue   # a missing owner: the owner check below reports it
                pool = {n["key"] for n in ns[REL_NS[rel[0]]]}
                if target not in pool:
                    findings.append(f"resolves: {m.group(1)}.{m.group(2)} names {rel[0]}={target}, which resolves nowhere")
    for name, _ in REGISTRY:
        nodes = ns.get(name)
        if nodes is None:
            continue
        keys = {n["key"] for n in nodes}
        if len(keys) != len(nodes):
            findings.append(f"complete: {name} holds a key twice")
        if name in folded:
            if counts.get(name) != len(nodes):
                findings.append(f"count: {name}.* counts {counts.get(name)}, the table holds {len(nodes)}")
        elif seen.get(name, set()) != keys:
            missing = sorted(keys - seen.get(name, set()))[:3]
            findings.append(f"complete: {name} has nodes on no line and in no count: {missing}")
    c = census()
    if plant == "census":
        c["kit-dirs"] = c["kit-dirs"] + ["newkit"]
    for name in ("principle", "chain", "item", "gap", "policy-key", "leg", "bug-class", "feature", "live-build", "hook",
                 "decision-row", "record-kind"):
        if c[name] != len(ns[name]):
            findings.append(f"census: {name} counts {c[name]} on disk, the map holds {len(ns[name])}")
    for k in c["kit-dirs"]:
        if k not in {n["key"] for n in ns["kit"]}:
            findings.append(f"census: tools/{k}/kit.toml is on disk with no kit node")
    a_steps = {s["tag"] for s in A["steps"]}
    a_items = {it["tag"] for s in A["steps"] for it in s["items"]} | {it["tag"] for p in A["programs"] for it in p["items"]}
    for kind, a_set, m_set in (("step", a_steps, {n["key"] for n in ns["step"]}), ("item", a_items, {n["key"] for n in ns["item"]}),
                               ("layer", {l["tag"] for l in A["layers"]}, {n["key"] for n in ns["layer"]}),
                               ("chain", {c["build"] for c in A["chain"]}, {n["key"] for n in ns["chain"]}),
                               ("gap", {g["id"] for g in A["gaps"]}, {n["key"] for n in ns["gap"]})):
        if a_set != m_set:
            findings.append(f"parity: {kind} on the map and not in the atlas {sorted(m_set - a_set)[:6]}, "
                            f"in the atlas and not on the map {sorted(a_set - m_set)[:6]}")
    # Fates: every kit has a declared fate and rows, every row a known kit, a fate in its set and a destination.
    if FATE_KITS or FATE_ROWS:
        rows_, kits_ = [list(r) for r in FATE_ROWS], dict(FATE_KITS)
        if plant == "fates-drop":
            rows_ = [r for r in rows_ if r[0] != rows_[0][0]]
        elif plant == "fates-ghost":
            rows_.append(["ghostkit", "a part", "a job", "STAYS", "kept (dGroundRules)", "a plant"])
        elif plant == "fates-bad":
            rows_[0][3] = "MAYBE"
        elif plant == "fates-unbuilt":
            i = next(i for i, r in enumerate(rows_) if r[3] == "RESHAPED")
            rows_[i][4] = "somewhere"
        elif plant == "fates-empty":
            i = next(i for i, r in enumerate(rows_) if r[3] == "RETIRED")
            rows_[i][4] = ""
        elif plant == "fates-kit":
            kits_[next(iter(kits_))] = "maybe"
        kitkeys, chainkeys = {n["key"] for n in ns["kit"]}, {n["key"] for n in ns["chain"]}
        for k in sorted(kitkeys):
            if k not in kits_:
                findings.append(f"fates: kit.{k} has no [kits] row")
            if not any(r[0] == k for r in rows_):
                findings.append(f"fates: kit.{k} has no [table] row")
        for k, f in kits_.items():
            if f not in FATE_KIT_SET:
                findings.append(f"fates: kit.{k}'s fate {f} is outside the set")
            if k not in kitkeys:
                findings.append(f"fates: [kits] names {k}, which is no kit node")
        for r in rows_:
            if r[0] not in kitkeys and r[0] not in FATE_PSEUDO:
                findings.append(f"fates: a row names {r[0]}, which is no kit")
            if r[3] not in FATE_ROW_SET:
                findings.append(f"fates: {r[0]} · {r[1]} has the fate {r[3]}, outside the set")
            elif r[3] != "RETIRED" and not set(re.findall(r"\bd[A-Z]\w+", r[4])) & chainkeys:
                findings.append(f"fates: {r[0]} · {r[1]} names no chain build where it goes")
            elif r[3] == "RETIRED" and not r[4].strip():
                findings.append(f"fates: {r[0]} · {r[1]} retires with no replacement named")
    # Layer: every kit line joins a layer, unless its kits-table row says "no layer" (dispatch 104 found all 19 empty).
    for ln in lines[2:]:
        m = LINE.match(ln)
        if m and m.group(1) == "kit" and m.group(2) not in NO_LAYER and " layer=" not in ln:
            findings.append(f"layer: kit.{m.group(2)} joins no layer")
    if any(re.search(r"\b20\d\d-\d\d-\d\d\b", ln) for ln in lines[2:]):
        findings.append("no stale facts: a line holds a date")
    # Owner: every node a build must build names exactly one chain build, read from a declared field (PM-8).
    chain = {n["key"] for n in ns["chain"]}
    for name in OWNED:
        for n in ns.get(name) or []:
            owners = [v for k, vs in n["rels"] if k == "owner" for v in vs]
            if not owners:
                findings.append(f"owner: {name}.{n['key']} names no owning build")
            elif len(owners) > 1:
                findings.append(f"owner: {name}.{n['key']} names {len(owners)} owning builds")
            elif owners[0] not in chain:
                findings.append(f"owner: {name}.{n['key']} names {owners[0]}, which is no chain build")
            elif (name, n["key"]) not in DECLARED:
                findings.append(f"no inference: {name}.{n['key']}'s owner comes from no declared field")
    return findings


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    A, ns = derive()
    unfold = ()
    if "--unfold" in argv:
        unfold = tuple(argv[argv.index("--unfold") + 1].split(","))
    if "--ns" in argv:
        name = argv[argv.index("--ns") + 1]
        if name not in ns or ns[name] is None:
            sys.exit(f"map: no armed namespace {name}")
        print("\n".join(line(name, n, PURPOSE) for n in ns[name]))
        return 0
    if "--pending" in argv:
        for name, _ in REGISTRY:
            pend = [n["key"] for n in (ns.get(name) or []) if not n["purpose"]]
            if pend:
                print(f"{name}: {len(pend)} — {', '.join(pend)}")
        return 0
    out, folded, unarmed, steps = fit(ns, unfold)
    plant = argv[argv.index("--plant") + 1] if "--plant" in argv else None
    if plant == "no-owner":
        ns["tag-namespace"][0]["rels"] = []
    elif plant == "orphan":
        ns["item"][0]["rels"] = []
    elif plant == "two-owners":
        ns["policy-key"][0]["rels"] = [("owner", ["dDeclaredLoop", "dTotalRecall"])]
    elif plant == "inferred":
        DECLARED.discard(("point", ns["point"][0]["key"]))
    findings = check(A, ns, out, folded, plant)
    size = len(out.encode("utf-8"))
    src = {}
    for name, _ in REGISTRY:
        for n in ns.get(name) or []:
            src[n["src"]] = src.get(n["src"], 0) + 1
    print(f"map: {sum(len(v) for v in ns.values() if v)} nodes in {len(REGISTRY)} namespaces; {size} B of {BUDGET} "
          f"({'degraded: ' + ', '.join(steps) if steps else 'no degrade'}); folded {len(folded)}; unarmed {', '.join(unarmed) or 'none'}")
    print(f"map: purposes declared {src.get('declared', 0)}, derived {src.get('derived', 0)}, pending {src.get('pending', 0)}")
    for f in findings:
        print(f"FINDING {f}")
    if "--out" in argv and not plant:
        Path(argv[argv.index("--out") + 1]).write_text(out, encoding="utf-8", newline="\n")
        print(f"map: wrote {argv[argv.index('--out') + 1]}")
    if findings:
        return 1
    if unarmed:
        print(f"map: every check passes, and {', '.join(unarmed)} is registered with no extractor: unarmed, never green")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
