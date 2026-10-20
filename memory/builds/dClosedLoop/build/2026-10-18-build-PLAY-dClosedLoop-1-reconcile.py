# **Serves:** research PLAY-dClosedLoop-1
"""The order's reconciliation gate: what a build's row cites, what its stage's items are, where its items route,
what keys its items read, and where its expansion registers, is built by that build or one of its ancestors in
[chain]'s after relation, or carries a declared class saying why it may not be.

The one committed copy, beside the map's generator (the night pass's closing review, M7). The audit fold's
`[review-instrument]` and the night pass's instruments record hold earlier snapshots of it; records cite this file.

Usage: python reconcile_probe.py <recut-record> [plants]   (from the worktree root)

Rules, each over a population it names in its summary line:
1. cites: each backticked citation of an owned node in a [chain] row.
2. stage: each item of the plan, design, build, test and deploy steps is built by the stage's build, named by
   [chain]'s Stage column, or by an ancestor of it.
3. routes: a source that reaches the breakpoint program needs the whole program from its own build or an ancestor.
   A source is a flow item's Then cell, an expansion item's Routes cell or a [chain] row, and it reaches the
   program by naming it, in the names flow-steps [breakpoint] declares. An expansion item's Routes cell that hands
   into a stage, named by [chain]'s Stage column, also needs that stage's build.
4. reads: each backticked policy key in a flow item's cells, the Owner cell aside, is built by the item's owner or
   an ancestor of it; a key is read whole or as `policy.<key>`, the full spelling flow-steps declares legal.
5. registers: each expansion's contract names, in its "extension points used" row, the Runtime points it registers
   at; each point's owner is an ancestor of, or one of, the owners of that expansion's items. Points of another
   layer are not modelled as nodes, so the summary names each one left unread.

6. transitions: each disposition `entry.place` routes through `entry.claim` has a `none` row in flow-steps'
   [transitions], since the engine refuses any transition the table lacks (the night pass's closing review, H1).

Rule 3 also reads every route target, as the whole-design audit's Stage 0 asks (K2, final-questions `[audit]`): each
item a flow item's Then cell or an expansion item's Routes cell names in backticks, and each stage a branch names after
its arrow (`→`) by one of the five flow steps' names in STAGES, read as that step's first item, is built by the source
item's owner or an ancestor of it. A stage word with no arrow before it in its branch is prose, not a route (the
closing pair's `prose-stage-words-as-routes`). Every run reads it since the audit's fold classed the forward routes it
finds (the owner's FK-4-9, 2026-10-20); `--all-routes`, Stage 0's flag before that, is accepted and ignored.

A dependency is classed only by a row of the re-cut's [reconciled-order] table naming its build, the rule that reads
it (cites, stage, routes, reads or registers), its node and its owner, with a class from the closed set, so a
dependency one rule classes is still unclassed under another (the closing pair's `reconcile-key-no-rule`). A row whose
class is blank or outside the set, whose rule is none of the five, or that no dependency needs, is a finding, and so is
a tolerance row whose reason says "today's tool" and names no backticked path that exists
(`tolerance-rows-unnamed-tool`); a reason naming any other stand-in is not checked. Exit 1 on any finding.
What it does not read, said in its summary: systems cited in prose; points of another layer; roles, shapes and
commands, which are not owned nodes; and an owned record kind written as plain words. The plain-word count is printed:
measured 2026-10-18 at 47 mentions over 27 kinds, mostly homonyms ("landing", "scope", "code"), so a clause that
depends on another build's node cites it backticked, and this rule reads only those (the closing review's H2).
Plants, each in memory: --plant-drop <build>:<node>[:<rule>] removes that pair's class rows, every rule's or the one
named; --plant-edge-drop <child>:<parent> removes a parent edge (repeatable); --plant-class <build>:<node>=<text> sets
the class cell of that pair's rows; --plant-why <build>:<node>=<text> sets their reason cell; --plant-add
<build>:<node>:<owner>[:<rule>] adds a tolerance row, for cites unless a rule is named; --plant-item
<tag>:<step>:<owner>:<then> adds a flow item; --plant-transition-drop <disposition> removes that disposition's `none`
row from [transitions].
"""
import importlib.util
import os
import re
import sys

B = "memory/builds/dClosedLoop/build/"
CLASSES = {"tolerance", "homonym", "not a use", "moved"}
spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)
A, ns = mp.derive()
owner = {}
for kind in ("item", "policy-key", "point", "record-kind", "tag-namespace"):
    for n in ns[kind]:
        own = [v for k, vs in n["rels"] if k == "owner" for v in vs]
        if own:
            owner[(kind, n["key"])] = own[0]


def plants(flag):
    return [sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == flag]


v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
rows, parents, stage_build = {}, {}, {}
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        rows[m.group(1)] = m.group(4)
        parents[m.group(1)] = [p.strip() for p in m.group(3).split(",") if p.strip() in names]
        stage_build[m.group(2).strip().lower()] = m.group(1)
for arg in plants("--plant-edge-drop"):
    child, parent = arg.split(":")
    parents[child] = [p for p in parents[child] if p != parent]


def ancestors(b, acc=None):
    acc = set() if acc is None else acc
    for p in parents[b]:
        if p not in acc:
            acc.add(p)
            ancestors(p, acc)
    return acc


def within(dep_owner, build):
    return dep_owner == build or dep_owner in ancestors(build)


def cells(ln):
    return [c.strip() for c in re.split(r"(?<!\\)\|", ln.strip().strip("|"))]


STAGES = [s for s in ("plan", "design", "build", "test", "deploy") if s in stage_build]
deps, unread = [], []   # deps: (rule, build, node, node's owner)
# 1. cites.
for b, text in rows.items():
    tokens = set(re.findall(r"`([^`\s][^`]*?)(?::[^`]*)?`", text))
    # A namespace cited through a wildcard, `<ns>.*`, cites the namespace's tag node and every policy key under it
    # (the night pass: dBoundRoles' `feature.*` read dTotalRecall's namespace, and this rule did not see it).
    wild = {t[:-2] for t in tokens if t.endswith(".*")}
    for (kind, key), own in owner.items():
        spelled = key if kind != "record-kind" else key.replace("-", " ")
        through = (kind == "tag-namespace" and key in wild) or \
            (kind == "policy-key" and any(key.startswith(w + ".") for w in wild))
        if (key in tokens or spelled in tokens or through) and not within(own, b):
            deps.append(("cites", b, key, own))
# The flow items, and the breakpoint program's declared names.
items = {}   # tag: (step, owner, cells but Item, Actor and Owner, Then cell)
first = {}   # step: its table's first item, which a route naming the step reaches
fs = open(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md", encoding="utf-8").read()
for m in re.finditer(r"^## \[([a-z-]+)\][^\n]*\n(.*?)(?=^## |\Z)", fs, flags=re.M | re.S):
    for ln in m.group(2).split("\n"):
        if ln.startswith("| `"):
            c = cells(ln)
            if len(c) == 7:
                for tag in re.findall(r"`([a-z]+\.[a-z0-9-]+)`", c[0]):
                    items[tag] = (m.group(1), c[6], " ".join(c[2:6]), c[5])
                    first.setdefault(m.group(1), tag)
for arg in plants("--plant-item"):
    tag, step, own, then = arg.split(":", 3)
    items[tag] = (step, own, then, then)
bp = fs.split("\n## [breakpoint]", 1)[1].split("\n## ", 1)[0]
names_line = next((ln for ln in bp.split("\n") if ln.startswith("- **Its names**")), "")
vocab = re.findall(r"`([a-z][a-z ]+)`", names_line)
if not vocab:
    sys.exit("flow-steps [breakpoint] declares no names line, so the routes rule would read nothing")
BREAK = re.compile("|".join(re.escape(v) for v in sorted(vocab, key=len, reverse=True)), re.I)
STAGE_WORD = re.compile(r"\b(" + "|".join(s.capitalize() for s in STAGES) + r")\b")
# 2. stage.
for tag, (step, own, _, _) in items.items():
    if step in STAGES and own and not within(own, stage_build[step]):
        deps.append(("stage", stage_build[step], tag, own))
# 3. routes: into the breakpoint program, from flow items, expansion items and rows; and into a stage, from expansion
# items.
program = {(t, o) for t, (s, o, _, _) in items.items() if s == "breakpoint" and o}
sources = {own for tag, (step, own, _, then) in items.items() if own and step != "breakpoint" and BREAK.search(then)}
sources |= {b for b, text in rows.items() if BREAK.search(text)}
le = open(B + "2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md", encoding="utf-8").read()
contracts = []   # (expansion's entry, its "extension points used" cell, the owners of its items)
expansion_routes = []   # (owner, Routes cell) of each expansion item, read by rule 3's route targets
for sec in re.split(r"(?m)^\| Contract field \|", le)[1:]:
    entry = sec.split("|", 1)[0].strip()
    used = next((cells(ln)[1] for ln in sec.split("\n") if ln.startswith("| extension points used |")), "")
    owners = set()
    for blk in sec.split("\n| Item | Actor |")[1:]:
        head = cells("| Item | Actor |" + blk.split("\n", 1)[0])
        oc = head.index("Owner") if "Owner" in head else None
        rc = head.index("Routes") if "Routes" in head else None
        for ln in blk.split("\n")[2:]:
            if not ln.startswith("| `"):
                break
            c = cells(ln)
            own = c[oc] if oc is not None and oc < len(c) else ""
            if not own:
                continue
            owners.add(own)
            routes = c[rc] if rc is not None and rc < len(c) else ""
            expansion_routes.append((own, routes))
            if BREAK.search(routes):
                sources.add(own)
            for stage in STAGE_WORD.findall(routes):
                sb = stage_build[stage.lower()]
                if not within(sb, own):
                    deps.append(("routes", own, stage.lower() + " step", sb))
    contracts.append((entry, used, owners))
for src in sorted(sources):
    outside = sorted({o for _, o in program if not within(o, src)})
    if outside:
        deps.append(("routes", src, "review.trigger", ",".join(outside)))
# Every item a route names in backticks, and every stage a branch names after its arrow, from flow items and expansion
# items alike, in every run since the audit's fold. A stage word with no arrow before it in its branch is prose.
STEP_NAME = re.compile(r"\b(" + "|".join(s.capitalize() for s in STAGES) + r")\b")


def routed_stages(text):
    return [w for branch in re.split(r";\s*", text) if "→" in branch
            for w in STEP_NAME.findall(branch.split("→", 1)[1])]


route_edges = 0
item_owner = {tag: v[1] for tag, v in items.items()}
item_owner.update({key: o for (kind, key), o in owner.items() if kind == "item" and key not in item_owner})
route_sources = [(own, then) for _, (_, own, _, then) in items.items() if own] + \
                [(own, routes) for own, routes in expansion_routes if own]
for own, text in route_sources:
    targets = {t for t in re.findall(r"`([a-z]+\.[a-z0-9-]+)`", text) if t in item_owner}
    targets |= {first[w.lower()] for w in routed_stages(text)}
    for t in sorted(targets):
        route_edges += 1
        town = item_owner[t]
        if town and not within(town, own):
            deps.append(("routes", own, t, town))
# 4. reads.
keys = {n["key"]: owner.get(("policy-key", n["key"])) for n in ns["policy-key"]}
templated = {re.sub(r"<stage>", "(" + "|".join(STAGES) + ")", re.escape(k).replace(r"\<stage\>", "<stage>")): o
             for k, o in keys.items() if "<stage>" in k}
for tag, (step, own, text, _) in items.items():
    if not own:
        continue
    for tok in set(re.findall(r"`([a-z][a-z0-9.<>-]*\.[a-z0-9<>-]+)(?::[^`]*)?`", text)):
        # flow-steps declares the full spelling, `policy.<key>`, legal (the closing pair's `policy-prefix-unread`).
        tok = tok[len("policy."):] if tok.startswith("policy.") else tok
        kown = keys.get(tok)
        if kown is None:
            kown = next((o for pat, o in templated.items() if re.fullmatch(pat, tok)), None)
        if kown and not within(kown, own):
            deps.append(("reads", own, tok, kown))
# 5. registers.
points = {n["key"]: owner.get(("point", n["key"])) for n in ns["point"]}
for entry, used, owners in contracts:
    for seg in re.split(r";\s*", used):
        layer = re.match(r"(?:and\s+)?([A-Z][a-z]+)'s\b", seg.strip())
        if layer and layer.group(1) != "Runtime":
            unread.append(f"{entry}: {seg.strip()}")
    runtime = re.search(r"Runtime's ([^;]+)", used)
    words = set(re.findall(r"[a-z]+", runtime.group(1))) if runtime else set()
    for key, pown in points.items():
        if pown and key.split("-")[0] in words:
            for o in owners:
                if not within(pown, o):
                    deps.append(("registers", o, key, pown))
# 6. transitions: a disposition entry.place routes through entry.claim needs a `none` row in [transitions].
tr = fs.split("\n## [transitions]", 1)[1].split("\n## ", 1)[0] if "\n## [transitions]" in fs else ""
none_rows = [cells(ln) for ln in tr.split("\n") if ln.startswith("| none |")]
for arg in plants("--plant-transition-drop"):
    none_rows = [c for c in none_rows if f"`{arg}`" not in c[1]]
routed = re.findall(r"(?:^|; )([a-z]+) → `entry\.claim`", items.get("entry.place", ("", "", "", ""))[3])
untransitioned = [d for d in routed if not any(f"`{d}`" in c[1] for c in none_rows)]
# Unread, and counted: an owned record kind written as plain words in a row whose build is not its owner or a
# descendant of it.
plain_hits = 0
for b, text in rows.items():
    bare = re.sub(r"`[^`]*`", " ", text)
    for (kind, key), own in owner.items():
        if kind == "record-kind" and not within(own, b) and \
                re.search(r"(?<![\w-])" + re.escape(key.replace("-", " ")) + r"(?![\w-])", bare):
            plain_hits += 1
# The classes: (rule, build, node) -> (owner, class, reason), from the re-cut's table, whose rows name the rule that
# reads each dependency (the closing pair's `reconcile-key-no-rule`).
RULES = ("cites", "stage", "routes", "reads", "registers")
recut = open(sys.argv[1], encoding="utf-8").read()
section = recut.split("### [reconciled-order]", 1)[1].split("\n## ", 1)[0] if "### [reconciled-order]" in recut else ""
classes, bad_rule = {}, []
for ln in section.split("\n"):
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    if ln.startswith("| d") and len(c) >= 6:
        if c[1] not in RULES:
            bad_rule.append((c[0], c[1], c[2].strip("`")))
            continue
        classes[(c[1], c[0], c[2].strip("`"))] = (c[3], c[4], c[5])
for arg in plants("--plant-drop"):
    parts = arg.split(":")
    for k in [k for k in classes if k[1:] == (parts[0], parts[1]) and (len(parts) < 3 or k[0] == parts[2])]:
        del classes[k]
for flag, field in (("--plant-class", 1), ("--plant-why", 2)):
    for arg in plants(flag):
        key, text = arg.split("=", 1)
        b, node = key.split(":", 1)
        for k in [k for k in classes if k[1:] == (b, node)] or [("cites", b, node)]:
            row = list(classes.get(k, ("", "", "")))
            row[field] = text
            classes[k] = tuple(row)
for arg in plants("--plant-add"):
    parts = arg.split(":")
    classes[(parts[3] if len(parts) > 3 else "cites", parts[0], parts[1])] = (parts[2], "tolerance", "planted")
deps = sorted(set(deps))
count = {k: sum(d[0] == k for d in deps) for k in ("cites", "stage", "routes", "reads", "registers")}
print(f"chain rows {len(rows)} · owned nodes read {len(owner)} · flow items read {len(items)} · stages {len(STAGES)} · "
      f"breakpoint items {len(program)}, names {len(vocab)} · contracts read {len(contracts)} · on a non-ancestor's node "
      f"{len(deps)} ({', '.join(f'{k} {v}' for k, v in count.items())})")
print(f"left out: systems, cited in prose; roles, shapes and commands, not owned nodes; {plain_hits} plain-word "
      f"mentions of a record kind a non-ancestor owns, mostly homonyms; stage words other than the {len(STAGES)} flow "
      f"steps' names, and any no arrow precedes in its branch, read as prose; points of another layer, not modelled as "
      f"nodes ({len(unread)}): " + "; ".join(unread))
print(f"transitions: {len(routed)} dispositions routed through entry.claim, {len(none_rows)} `none` rows")
print(f"all routes: {route_edges} route edges read from flow and expansion items")
findings = 0
for d in untransitioned:
    print(f"  transitions: the disposition `{d}` routes through `entry.claim`, and [transitions] has no `none` row for it")
    findings += 1
for rule, b, key, own in deps:
    row = classes.get((rule, b, key))
    ok = row is not None and row[1] in CLASSES and row[0] == own
    label = row[1] if ok else ("UNCLASSED" if row is None else f"BAD CLASS ROW (owner {row[0] or '-'}, class {row[1] or '-'})")
    print(f"  {b} {rule} `{key}` ({own}'s, not an ancestor): {label}")
    findings += not ok
needed = {(rule, b, key) for rule, b, key, _ in deps}
for (rule, b, key), (own, cls, why) in sorted(classes.items()):
    if (rule, b, key) not in needed:
        print(f"  class row with no dependency: {b} {rule} `{key}` ({own}, {cls or '-'})")
        findings += 1
    elif cls not in CLASSES:
        print(f"  class row outside the closed set: {b} {rule} `{key}` ({cls or 'blank'})")
    elif cls == "tolerance" and "today's tool" in why and not any(
            "/" in path and os.path.exists(path) for path in re.findall(r"`([^`]+)`", why)):
        print(f"  tolerance row names no stand-in: {b} {rule} `{key}` says today's tool and names no path that exists")
        findings += 1
for b, rule, key in bad_rule:
    print(f"  class row with a rule outside the five: {b} `{key}` ({rule or 'blank'})")
    findings += 1
print(f"findings {findings}")
sys.exit(1 if findings else 0)
