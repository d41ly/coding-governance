# **Serves:** research PLAY-dClosedLoop-1
"""Stage 0 of the whole-design audit: the mechanical checks, each seen red on a plant before it is trusted.

The owner chose the audit at FQ-1 (2026-10-19); the round record `2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`
runs it, and research-final-audit `[2]` and `[5]` name the classes a table can check, K1 to K5. Five arms are new;
`reruns` runs the design's existing checks, from this folder, in the same tree.

  K1 items       every flow item has an actor of a declared kind or role, a core item no expansion role; a Needs cell,
                 a dash there only on its step's first item, every item it names existing and no cycle among them; a
                 witness; a Then cell; and an owning chain build. Expansion items carry no Needs column, and the rest
                 of K1 reads them too.
  K2 routes      every item-shaped tag a Then or Routes cell names is an item or a catalogue key; every target a branch
                 routes to has a declared form (`FORMS`); every item ends, through its own branches or an item it
                 routes to; and every item is reached from an entry. The order half, every route target built by its
                 source's owner or an ancestor, is the reconciliation probe's, run with --all-routes.
  K3 kinds       every record kind the map registers has a row in layer-memory's kind table naming a writer item, and
                 a reader: an item that waits on a writer, an item whose cells name it, or a chain clause of a build
                 other than its owner that names it.
  K4 keys        every catalogue key is read by a chain clause or an item, named in backticks, through its namespace's
                 `.*`, or as an instance of a templated key; a key with a loosening value is marked guard-bearing.
  K5 principles  every principle has one row in v2's `[enforcement]`, naming the clause ids that enforce it; every id
                 named is minted in `[chain]` and not retired; and every clause citing a principle by id is in that
                 principle's row.

A finding stands unless a row of the round record's `[stage0-classes]` names its arm, its node and a class from that
arm's closed set (`CLASSES`); a row that no finding needs, or whose class is outside the set, is itself a finding. Each
arm prints what it does not read, "left out", and the walk takes those as named targets.

Usage: python stage0.py [--root <tree>] [--arms K1,K2,K3,K4,K5,reruns] [--plant <case>]   (from the worktree root)
  --root   the tree whose records are read, such as the walk's seeded copy; every check runs inside it.
  --plant  damages one input in memory, and that arm must go red: k1-witness, k1-ghost-need, k1-cycle, k1-dash,
           k1-owner, k1-actor, k1-owning-role, k2-ghost, k2-unformed, k2-dead-end, k2-unreached, k2-deploy-land, k3-writer, k3-reader,
           k4-unread, k5-row, k5-ghost, k5-retired, k5-cited, class-stale.
Exit 1 on any finding or any red re-run.
"""
import collections
import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

ARGS = sys.argv[1:]


def opt(flag, default=None):
    return ARGS[ARGS.index(flag) + 1] if flag in ARGS else default


ROOT = Path(opt("--root", ".")).resolve()
os.chdir(ROOT)
B = "memory/builds/dClosedLoop/build/"
P = B + "2026-10-"
V2 = P + "14-build-PLAY-dClosedLoop-1-architecture-v2.md"
AUDIT = P + "19-build-PLAY-dClosedLoop-1-whole-audit.md"
PLANT = opt("--plant")
ARMS = opt("--arms", "K1,K2,K3,K4,K5,reruns").split(",")
KINDS = ("command", "executor", "hook", "owner")
STEP_WORDS = ("Plan", "Design", "Build", "Test", "Deploy")
LOOSENING = re.compile(r"\b(off|warn|report|none|never|skip|allow|ignore|any|author-recorded|report-only)\b")
# The closed class sets: what may accept a finding without a fix, per arm. A class the audit needs and this set lacks
# is added here with its reason in the round record, never typed into a row alone.
CLASSES = {
    "K1": {"prose need"},
    "K2": {"prose target", "external entry"},
    "K3": {"program writer", "hook writer", "external writer", "program reader", "external reader"},
    "K4": {"planned", "read through a system"},
    "K5": set(),
}
# The forms a routed target may take, each read from the target's own words (the text after a branch's arrow, or the
# whole branch where it has none). An item tag or a step name is an edge; the rest end the branch, except that the
# walk judges whether each does (S6).
FORMS = [
    ("terminal", re.compile(r"\b(closed|done|filed|relayed|retired|refused|told|rejected|reconstructed|armed|unarmed|"
                            r"landed|withdrawn|superseded|deferred|merged|answered|refuses the adoption|migration|"
                            r"nothing|skip|returned|built|reported|recorded)\b")),
    ("return", re.compile(r"`next`|\bre-entry\b|\bback to\b|item that asked|asking item|\bcontinues\b|\breleased\b|"
                          r"boundary's next item|\bre-disposed\b|\bre-run\b|\bre-tried\b|\bretry\b|\bresumes?\b|"
                          r"\bnext environment\b")),
    ("wait", re.compile(r"\bholds\b|\bwaits\b|\bparked\b|\buntil\b|\bheld\b|\bwarned\b|\bnoted\b")),
    ("owner", re.compile(r"\bowner item\b|\bowner exception\b|\bowner's disposition\b|\bthe owner\b")),
    ("ask", re.compile(r"\ban ask\b|\basks\b")),
    ("policy", re.compile(r"\bas `[a-z][a-z0-9.-]*` says\b")),
    ("program", re.compile(r"\bfix pass\b|\bclosing review\b|\bspec audit\b|\bverification round\b|\bpatch build\b|"
                           r"\bplan revision\b|\bspec writer\b|\barchitect\b|\bfresh slug\b|\bnext round\b|"
                           r"\bfurther pass\b|\bsecond independent pass\b|\bprobe repaired\b|\bpublication\b")),
]

spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)
atlas = mp.atlas
A, ns = mp.derive()
v2 = Path(V2).read_text(encoding="utf-8")
chain_names = [c["build"] for c in A["chain"]]
parents = {c["build"]: [p for p in c["parents"] if p in chain_names] for c in A["chain"]}


def owners(n):
    return [v for k, vs in n["rels"] if k == "owner" for v in vs]


def ancestors(b, acc=None):
    acc = set() if acc is None else acc
    for p in parents.get(b, []):
        if p not in acc:
            acc.add(p)
            ancestors(p, acc)
    return acc


def split_clauses(cell):
    """A chain row's clauses: split on '; ' outside backticks, parentheses and double quotes, as the clause scan reads."""
    out, cur, depth, tick, quote, i = [], [], 0, False, False, 0
    while i < len(cell):
        ch = cell[i]
        if ch == "`" and not quote:
            tick = not tick
        elif ch == '"' and not tick:
            quote = not quote
        elif not tick and ch == "(":
            depth += 1
        elif not tick and ch == ")":
            depth = max(0, depth - 1)
        if cell.startswith("; ", i) and not (depth or tick or quote):
            out.append("".join(cur))
            cur, i = [], i + 2
            continue
        cur.append(ch)
        i += 1
    out.append("".join(cur))
    return [c for c in out if c.strip()]


# ------------------------------------------------------------------------------------------------- the populations
items = {}   # tag: dict(step, first, actor, needs, does, proof, then, owner, flow)
for s in A["steps"]:
    for i, it in enumerate(s["items"]):
        items[it["tag"]] = dict(step=s["tag"], first=i == 0, actor=it["actor"], needs=it["needs"], does=it["does"],
                                proof=it["proof"], then=it["then"], owner=it["owner"], flow=True)
le = Path(P + "16-build-PLAY-dClosedLoop-1-layer-expansions.md").read_text(encoding="utf-8")
for head, rows in atlas.tables(le):
    if head[:2] != ["Item", "Actor"]:
        continue
    col = {h: i for i, h in enumerate(head)}
    for n, r in enumerate(rows):
        get = lambda h: r[col[h]].strip() if h in col and col[h] < len(r) else ""   # noqa: E731
        for tag in re.findall(r"`([a-z]+\.[a-z0-9-]+)`", r[0]):
            items.setdefault(tag, dict(step="expansion", first=n == 0, actor=get("Actor"), needs="", does=get("Does"),
                                       proof=get("Witness"), then=get("Routes"), owner=get("Owner"), flow=False))
keys = {p["key"]: p for p in A["policies"]}
roster = {r["role"]: r for r in A["roster"]}
clauses = {}   # id: (build, text)
for c in A["chain"]:
    for cl in split_clauses(c["units"]):
        m = re.search(r"`(cl-d[A-Z]\w+-\d{4})`\s*$", cl.strip())
        clauses[m.group(1) if m else f"unminted:{c['build']}:{len(clauses)}"] = (c["build"], cl.strip())
cid = v2.split("\n## [clause-ids]", 1)[1].split("\n## ", 1)[0] if "\n## [clause-ids]" in v2 else ""
retired = set(re.findall(r"`(cl-d[A-Z]\w+-\d{4})`", cid.split("Retired:", 1)[1])) if "Retired:" in cid else set()
enforcement = v2.split("\n## [enforcement]", 1)[1].split("\n## ", 1)[0] if "\n## [enforcement]" in v2 else None
kind_rows = {}
lm = Path(P + "15-build-PLAY-dClosedLoop-1-layer-memory.md").read_text(encoding="utf-8")
for head, rows in atlas.tables(lm):
    if head == ["Kind", "Owner", "Its writer, or what names it"]:
        for r in rows:
            kind_rows[r[0].strip()] = r
kinds = {n["key"]: owners(n) for n in ns["record-kind"]}
classes = []   # (arm, node, class, reason)
if Path(AUDIT).exists():
    sec = Path(AUDIT).read_text(encoding="utf-8").split("\n## [stage0-classes]", 1)
    for ln in (sec[1].split("\n## ", 1)[0].split("\n") if len(sec) > 1 else []):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if ln.startswith("| K") and len(c) >= 4:
            classes.append((c[0], c[1].strip("`"), c[2], c[3]))

# ------------------------------------------------------------------------------------------------------ the plants
if PLANT == "k1-witness":
    items["plan.dedupe"]["proof"] = ""
elif PLANT == "k1-ghost-need":
    items["plan.record"]["needs"] += ", `plan.ghost`"
elif PLANT == "k1-cycle":
    items["plan.input"]["needs"] = "`plan.dedupe`"
elif PLANT == "k1-dash":
    items["plan.dedupe"]["needs"] = "—"
elif PLANT == "k1-owner":
    items["plan.dedupe"]["owner"] = "dNoSuchBuild"
elif PLANT == "k1-actor":
    items["plan.dedupe"]["actor"] = "wizard"
elif PLANT == "k1-owning-role":
    items["plan.dedupe"]["actor"] = "the role that answers the question"
elif PLANT == "k2-ghost":
    items["plan.dedupe"]["then"] += "; a planted outcome → `plan.ghost`"
elif PLANT == "k2-unformed":
    items["plan.dedupe"]["then"] += "; a planted outcome → somewhere unnamed"
elif PLANT == "k2-dead-end":
    for a, b in (("plan.loop-a", "plan.loop-b"), ("plan.loop-b", "plan.loop-a")):
        items[a] = dict(step="plan", first=False, actor="command", needs="`plan.input`", does="planted", proof="planted",
                        then=f"`{b}`", owner="dRankedPlan", flow=True)
elif PLANT == "k2-unreached":
    items["plan.island"] = dict(step="plan", first=False, actor="command", needs="a signal no item gives",
                                does="planted", proof="planted", then="done", owner="dRankedPlan", flow=True)
elif PLANT == "k3-writer":
    r = kind_rows["plan"]
    kind_rows["plan"] = [r[0], r[1], "writer item not named"]
elif PLANT == "k3-reader":
    kinds["planted-kind"] = ["dRankedPlan"]
    # Written by an item no other item waits on, and named nowhere else.
    kind_rows["planted kind"] = ["planted kind", "dRankedPlan", "its writer is `review.cost`"]
elif PLANT == "k4-unread":
    keys["plan.planted-knob"] = {"key": "plan.planted-knob", "values": "on, off", "default": "on", "owner": "dRankedPlan"}
elif PLANT == "class-stale":
    classes.append(("K4", "plan.no-such-key", "planned", "planted"))
elif PLANT and PLANT.startswith("k5-") and enforcement is not None:
    rows = [ln for ln in enforcement.split("\n") if ln.startswith("| `P")]
    if PLANT == "k5-row":
        enforcement = enforcement.replace(rows[1] + "\n", "")
    elif PLANT == "k5-ghost":
        enforcement = enforcement.replace(rows[1], rows[1][:-2] + ", `cl-dClosedLoop-9999` |")
    elif PLANT == "k5-retired":
        retired.add(re.findall(r"`(cl-d[A-Z]\w+-\d{4})`", rows[1])[0])
    elif PLANT == "k5-cited":
        # A clause that cites a principle by id, dropped from that principle's row.
        cid_, _ = next((i, cl) for i, (_, cl) in clauses.items() if re.search(r"\bP\d+\b", cl) and f"`{i}`" in enforcement)
        enforcement = enforcement.replace(f"`{cid_}`", "")
elif PLANT and PLANT != "k2-deploy-land":
    sys.exit(f"stage0: unknown plant {PLANT}")

findings = collections.defaultdict(list)   # arm: [(node, what)]
left = collections.defaultdict(list)       # arm: [what it does not read]
counts = {}


def find(arm, node, what):
    findings[arm].append((node, what))


ITEM_SHAPE = re.compile(r"`([a-z]+\.[a-z0-9-]+)(?::[^`]*)?`")
PREFIXES = {t.split(".")[0] for t in items}


def item_refs(text):
    """The item tags a cell names, and the item-shaped tags that are neither an item nor a catalogue key."""
    refs, ghosts = [], []
    for t in ITEM_SHAPE.findall(text):
        if t in items:
            refs.append(t)
        elif t.split(".")[0] in PREFIXES and t not in keys:
            ghosts.append(t)
    return refs, ghosts


# ---------------------------------------------------------------------------------------------------------- K1
if "K1" in ARMS:
    flow = {t: v for t, v in items.items() if v["flow"]}
    for t, v in items.items():
        head = re.split(r"[,:(]", v["actor"].strip(), maxsplit=1)[0].strip().lower()
        if not v["actor"].strip():
            find("K1", t, "no actor")
        elif head.startswith("the role that owns"):
            pass   # one actor, the role owning the asked interface or item, per instance (layer-roles [matrix])
        elif head not in KINDS:
            role = roster.get(head)
            if role is None:
                find("K1", t, f"actor '{head}' is no kind and no declared role")
            elif role["acts"].startswith("cycle role"):
                find("K1", t, f"actor '{head}' is a cycle role, which acts in no item")
            elif v["flow"] and role["layer"] != "core":
                find("K1", t, f"a core item names the expansion role '{head}' (P28)")
        if not v["proof"].strip() or v["proof"].strip() in ("—", "-"):
            find("K1", t, "no witness")
        if not v["then"].strip():
            find("K1", t, "no Then or Routes cell")
        if v["owner"] not in chain_names:
            find("K1", t, f"owner '{v['owner']}' is no chain build")
    graph = {}
    for t, v in flow.items():
        need = v["needs"].strip()
        if not need:
            find("K1", t, "no Needs cell")
        elif need in ("—", "-") and not v["first"]:
            find("K1", t, "a dash for Needs, on an item that is not its step's first")
        refs, ghosts = item_refs(need)
        for g in ghosts:
            find("K1", t, f"needs `{g}`, which is no item")
        graph[t] = refs
    seen, cycles = {}, set()

    def walk(t, path):
        seen[t] = 1
        for u in graph.get(t, []):
            if u in path:
                cyc = path[path.index(u):] + [u]
                cycles.add(" > ".join(cyc))
            elif seen.get(u) != 2:
                walk(u, path + [u])
        seen[t] = 2

    for t in graph:
        if t not in seen:
            walk(t, [t])
    for c in sorted(cycles):
        find("K1", c.split(" > ")[0], f"a cycle among Needs: {c}")
    counts["K1"] = f"items {len(items)} ({len(flow)} flow, {len(items) - len(flow)} expansion), roles {len(roster)}"
    left["K1"].append("whether a witness is actor-typed (P2) and whether the outcome is the right one; a Needs cell's prose "
                      "beyond its item tags")

# ---------------------------------------------------------------------------------------------------------- K2
if "K2" in ARMS:
    first = {}
    for t, v in items.items():
        if v["flow"] and v["first"]:
            first[v["step"]] = t
    edges, form_counts, callers = collections.defaultdict(set), collections.Counter(), collections.defaultdict(set)
    ends_alone = set()
    for t, v in items.items():
        refs, ghosts = item_refs(v["then"])
        for g in ghosts:
            find("K2", t, f"routes to `{g}`, which is no item and no key")
        for branch in re.split(r";\s+(?![^(]*\))", v["then"]):
            parts = re.split(r"\s+→\s+", branch)
            targets = parts[1:] if len(parts) > 1 else parts
            for tgt in targets:
                tr, _ = item_refs(tgt)
                steps = [w for w in STEP_WORDS if re.search(r"\b" + w + r"\b", tgt)]
                for u in tr:
                    edges[t].add(u)
                    callers[u].add(t)
                for w in steps:
                    edges[t].add(first[w.lower()])
                    callers[first[w.lower()]].add(t)
                if tr or steps:
                    form_counts["edge"] += 1
                    continue
                form = next((name for name, pat in FORMS if pat.search(tgt)), None)
                if form is None:
                    find("K2", t, f"a target in no declared form: \"{tgt.strip()[:90]}\"")
                    continue
                form_counts[form] += 1
                ends_alone.add(t)
    ends = set(ends_alone)
    changed = True
    while changed:
        changed = False
        for t in items:
            if t not in ends and any(u in ends for u in edges[t]):
                ends.add(t)
                changed = True
    for t in sorted(set(items) - ends):
        find("K2", t, "ends nowhere: every route it takes leads only to items that never end")
    roots = {t for t, v in items.items() if (v["flow"] and v["needs"].strip() in ("—", "-")) or
             (not v["flow"] and v["first"])}
    reached = set(roots)
    changed = True
    while changed:
        changed = False
        for t, v in items.items():
            if t in reached:
                continue
            refs, _ = item_refs(v["needs"])
            if callers[t] & reached or (refs and any(r in reached for r in refs)):
                reached.add(t)
                changed = True
    for t in sorted(set(items) - reached):
        find("K2", t, "reached from no entry: no reached item routes to it, and no item it needs is reached")
    order_args = [sys.executable, "-X", "utf8", B + "2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py",
                  P + "18-build-PLAY-dClosedLoop-1-recut.md", "--all-routes"]
    if PLANT == "k2-deploy-land":
        order_args += ["--plant-item", "plan.planted:plan:dRankedPlan:a planted outcome → `deploy.land`"]
    r = subprocess.run(order_args, capture_output=True, text=True, encoding="utf-8")
    for ln in r.stdout.split("\n"):
        m = re.match(r"^  (d[A-Z]\w+) (routes|cites|stage|reads|registers) `([^`]+)` \((.+?)\): (UNCLASSED|BAD CLASS ROW.*)$",
                     ln)
        if m:
            find("K2", f"{m.group(1)}→{m.group(3)}", f"order: {m.group(2)} `{m.group(3)}`, {m.group(4)}, {m.group(5)}")
    if r.returncode not in (0, 1):
        find("K2", "reconcile.py", f"the order run failed: {r.stderr.strip()[-200:]}")
    counts["K2"] = (f"targets by form: {', '.join(f'{k} {v}' for k, v in sorted(form_counts.items()))}; roots {len(roots)}, "
                    f"reached {len(reached)}, ending {len(ends)}")
    left["K2"].append("whether a branch that ends by a terminal, return, wait, owner, ask, policy or program form does "
                      "end (the walk's S6); a policy's routes per value; the [transitions] join gap-flow-15 owes; "
                      "the conditions before each arrow")

# ---------------------------------------------------------------------------------------------------------- K3
if "K3" in ARMS:
    by_name = {k.replace("-", " "): k for k in kinds}
    rows_by_key = {}
    for name, r in kind_rows.items():
        k = by_name.get(name) or (name if name in kinds else None)
        if k:
            rows_by_key[k] = r
    clause_text = [(b, t) for b, t in clauses.values()]
    for k, own in sorted(kinds.items()):
        row = rows_by_key.get(k)
        if row is None:
            find("K3", k, "registered by the map, with no row in layer-memory's kind table")
            continue
        writers = [t for t in ITEM_SHAPE.findall(row[2]) if t in items]
        writers += [t for t in items if "`*.recommend`" in row[2] and t.endswith(".recommend")]
        if not writers:
            find("K3", k, f"no writer item: \"{row[2][:80]}\"")
        spelled = k.replace("-", " ")
        pat = re.compile(r"`" + re.escape(k) + r"`|(?<![\w-])" + re.escape(spelled) + r"s? records?\b", re.I)
        # A reader waits on a writer's witness, which is the kind's record, or names the kind in its own cells.
        readers = [t for t, v in items.items() if t not in writers and
                   (set(item_refs(v["needs"])[0]) & set(writers) or pat.search(" ".join((v["needs"], v["does"], v["then"]))))]
        readers += [b for b, text in clause_text if b not in own and pat.search(text)]
        if not readers:
            find("K3", k, "no reader: no item waits on its writer or names it, and no clause of another build names it")
    counts["K3"] = f"kinds {len(kinds)}, table rows {len(kind_rows)}"
    left["K3"].append("a reader or writer that is a gate, a renderer or a hook rather than an item; a kind named in plain "
                      "words other than '<kind> record'; whether a non-item writer is real")

# ---------------------------------------------------------------------------------------------------------- K4
if "K4" in ARMS:
    text = "\n".join(t for _, t in clauses.values()) + "\n" + "\n".join(
        " ".join((v["needs"], v["does"], v["proof"], v["then"])) for v in items.values())
    toks = set(re.findall(r"`([a-z][a-z0-9.<>*-]*)(?::[^`]*)?`", text))
    wild = {t[:-2] for t in toks if t.endswith(".*")}
    for k, row in sorted(keys.items()):
        if k in toks or any(k.startswith(w + ".") or k == w for w in wild):
            continue
        if "<" in k:
            pat = re.compile(re.sub(r"\\<[a-z-]+\\>", "[a-z0-9-]+", re.escape(k)))
            if any(pat.fullmatch(t) for t in toks):
                continue
        guard = " (guard-bearing)" if LOOSENING.search(row.get("values", "")) else ""
        find("K4", k, f"read by no chain clause and no item{guard}")
    counts["K4"] = f"keys {len(keys)}"
    left["K4"].append("a key read in a layer or system record but built by no clause; whether an unread key is "
                      "guard-bearing beyond its values' words")

# ---------------------------------------------------------------------------------------------------------- K5
if "K5" in ARMS:
    prin = [f"P{p['n']}" for p in A["principles"]]
    if enforcement is None:
        for p in prin:
            find("K5", p, "v2 has no [enforcement] section, so no principle names a clause that enforces it")
    else:
        rows = {}
        for ln in enforcement.split("\n"):
            m = re.match(r"^\| `(P\d+)` \| (.*?) \|", ln)
            if m:
                if m.group(1) in rows:
                    find("K5", m.group(1), "two rows")
                rows[m.group(1)] = re.findall(r"`(cl-d[A-Z]\w+-\d{4})`", m.group(2))
        for p in prin:
            if p not in rows:
                find("K5", p, "no row in [enforcement]")
            elif not rows[p]:
                find("K5", p, "a row naming no clause")
        for p, ids in rows.items():
            if p not in prin:
                find("K5", p, "a row for no principle")
            for i in ids:
                if i in retired:
                    find("K5", p, f"names `{i}`, a retired id")
                elif i not in clauses:
                    find("K5", p, f"names `{i}`, which no clause carries")
        for i, (b, cl) in clauses.items():
            for p in sorted(set(re.findall(r"\b(P\d+)\b", cl))):
                if p in prin and i not in rows.get(p, []):
                    find("K5", p, f"`{i}` ({b}) cites {p} by id, and {p}'s row does not name it")
    counts["K5"] = f"principles {len(A['principles'])}, clauses {len(clauses)}, retired {len(retired)}"
    left["K5"].append("whether a named clause enforces its principle, which only a reader judges")

# ------------------------------------------------------------------------------------------------- the classes
accepted, needed = collections.Counter(), set()
for arm, node, cls, reason in classes:
    if arm in findings and any(n == node for n, _ in findings[arm]):
        needed.add((arm, node))
for arm in list(findings):
    kept = []
    for node, what in findings[arm]:
        row = next((c for c in classes if c[0] == arm and c[1] == node), None)
        if row and row[2] in CLASSES.get(arm, set()):
            accepted[arm] += 1
            continue
        kept.append((node, what + (f" [class row '{row[2]}' outside {arm}'s set]" if row else "")))
    findings[arm] = kept
for arm, node, cls, reason in classes:
    if (arm, node) not in needed:
        findings["classes"].append((node, f"a {arm} class row that no finding needs ({cls})"))

# ------------------------------------------------------------------------------------------------------ re-runs
RERUNS = [("design map", [B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py", "--check"]),
          ("atlas", [B + "2026-10-16-build-PLAY-dClosedLoop-1-atlas.py", "--check"]),
          ("fold state", [P + "19-build-PLAY-dClosedLoop-1-fold-state.py"]),
          ("reconciliation probe", [B + "2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py",
                                    P + "18-build-PLAY-dClosedLoop-1-recut.md"]),
          ("clause scan", [P + "19-build-PLAY-dClosedLoop-1-clause-scan.py"]),
          ("clause ids", [P + "19-build-PLAY-dClosedLoop-1-clause-ids.py"]),
          ("gap join", [P + "19-build-PLAY-dClosedLoop-1-gap-join.py", P + "14-build-PLAY-dClosedLoop-1-gap-register.md",
                        V2]),
          ("preset check", [P + "19-build-PLAY-dClosedLoop-1-preset-check.py", V2]),
          ("critical path", [P + "19-build-PLAY-dClosedLoop-1-critical-path.py"]),
          ("line coverage", [P + "19-build-PLAY-dClosedLoop-1-line-coverage.py"]),
          ("review debt", [P + "19-build-PLAY-dClosedLoop-1-review-debt.py"])]
SUMMARY = {"line coverage": re.compile(r"^design records "), "review debt": re.compile(r"^design commits after|^  [0-9a-f]{9}"),
           "critical path": re.compile(r"^critical path:")}
reruns = []
if "reruns" in ARMS:
    for label, argv in RERUNS:
        r = subprocess.run([sys.executable, "-X", "utf8", *argv], capture_output=True, text=True, encoding="utf-8")
        out = (r.stdout + r.stderr).strip().split("\n")
        keep = [ln for ln in out if SUMMARY[label].search(ln)] if label in SUMMARY else out[-1:]
        reruns.append((label, r.returncode, keep))

# ------------------------------------------------------------------------------------------------------- report
total = 0
for arm in ("K1", "K2", "K3", "K4", "K5", "classes"):
    if arm not in ARMS and arm != "classes":
        continue
    if arm == "classes" and not findings["classes"]:
        continue
    fs = findings[arm]
    total += len(fs)
    print(f"{arm}: {counts.get(arm, '')} · findings {len(fs)}" + (f" · classed {accepted[arm]}" if accepted[arm] else ""))
    for node, what in fs:
        print(f"  {arm} {node}: {what}")
    for what in left[arm]:
        print(f"  left out: {what}")
red_reruns = [label for label, rc, _ in reruns if rc != 0]
for label, rc, keep in reruns:
    print(f"rerun {label}: rc {rc}" + ("".join(f"\n  {ln}" for ln in keep) if keep else ""))
print(f"stage0: arms {','.join(a for a in ARMS)} · findings {total} · classed {sum(accepted.values())} · "
      f"reruns red {len(red_reruns)}" + (f" ({', '.join(red_reruns)})" if red_reruns else "") +
      (f" · plant {PLANT}" if PLANT else ""))
sys.exit(1 if total or red_reruns else 0)
