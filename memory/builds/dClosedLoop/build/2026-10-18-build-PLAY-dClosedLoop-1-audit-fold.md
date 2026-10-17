# The whole-design audit, folded

**Serves:** research PLAY-dClosedLoop-1

The audit the owner declared at kickoff ran as dispatch 98, step 4 of the owner's convergence order, and returned
CLEAN WITH FIXES: 28 items, 6 high, no blocker (`reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md`). Three items were the owner's to choose. This record
holds the owner's answers, how the first one cuts the chain, each item's fold, the left-shift and the
instruments.

## [words] The owner's answers, 2026-10-18

The questions went to the owner with each option's text, and the owner chose, verbatim:
- AF-1, asked as "AF-1: steps route to items and breakpoints whose owner lands later. Which fallback?": "Land the mechanism earlier", whose text read: "The stage-exit recommendation and the owner gate move to dDeclaredLoop, leaving dCalibratedLens the lenses, the ledger and the Loop Review. Re-opens PM-12a for those 8 items."
- AF-2, asked as "AF-2: what does a malformed policy file, an out-of-set value, or a stale JSON mirror do?": "Last valid, else refuse (Recommended)", whose text read: "Read the last valid landed revision and record why; with none, the push and landing gates refuse and name the line. A stale or absent mirror falls back to the TOML reader. An absent file still reads defaults (RC-1)."
- AF-3, asked as "AF-3: strict's tests.landing-levels cell says 'every declared level'. How should it read?": "Add every-declared (Recommended)", whose text read: "The catalogue row gains the value every-declared and strict uses it, so a repository is held to the levels it declares and not to ones it lacks."

Each answer is structural or names its own key, so AF-2's key, `policy.on-invalid`, takes the answer as its default
and the other option as its one other value.

## [af-1] AF-1's cut: the mechanism, earlier

The owner's AF-1 moves the stage-exit recommendation and the owner gate to dDeclaredLoop, and leaves dCalibratedLens
the lenses, the ledger and the Loop Review. v2 makes reviews and owner gates one mechanism, the breakpoint. So the
owner gate moves with the breakpoint mechanism it belongs to, or the one mechanism would split across two builds.
The cut runs along one seam: the loop's control flow at a boundary goes to dDeclaredLoop, and calibration stays
with dCalibratedLens.
- **Items, 12, to dDeclaredLoop:** `plan.recommend`, `plan.reason`, `design.recommend`, `design.reason`,
  `build.recommend`, `deploy.recommend`, `test.recommend` and `test.reason`, which PM-12a had given dCalibratedLens,
  and the breakpoint program's own `review.trigger`, `review.dispose`, `review.fold` and `review.cost`.
- **Keys, 11, to dDeclaredLoop:** `autonomy`, `review.breakpoints`, `review.<stage>`, `review.blocks`,
  `review.unverified`, `review.left-shift`, `review.follow-up`, `review.design.rounds`, `review.design.round-count`,
  `review.recommendation` and `review.recommendation.source`. The two round keys PM-12b kept with dCalibratedLens
  follow the round loop they bound.
- **The `recommendation` record kind,** and the gaps the mechanism closes, gap-flow-11 and gap-flow-12.
- **What stays with dCalibratedLens:** the stage lenses and `review.<stage>.effort`, the value ledger and the
  `review.cost` rows it prices, the Loop Review and `review.loop.*`, the caps and `budgets.*`, instruction
  effectiveness, `memory.item-budget`'s derivation, and the not-in-view cause, now added to `review.dispose`'s
  record. It keeps its other seven gaps.
- **What stays with dFairHearing:** the harness, `review.pin`, `review.lens`, `review.refute` and `review.report`. It
  lands before dDeclaredLoop, so a review breakpoint calls it from an ancestor.
- **The owner gate before dBoundRoles lands** holds for the owner's disposition. It reads `run.on-owner-question`
  only once that key is landed, and never for a ratification.

## [fold] Each item, folded

| Item | What changed | Where |
| --- | --- | --- |
| H1 | AF-1: dDeclaredLoop builds the owner gate, held until the owner's disposition record; RC-9's fallback falls back to it, and `run.on-owner-question` resolves it only once dBoundRoles lands that key, never for a ratification | v2 dDeclaredLoop, dRankedPlan; the re-cut's class table |
| H2 | AF-1: every step's recommend and reason items are dDeclaredLoop's, with the breakpoint program, its 11 keys and the recommendation kind; dCalibratedLens keeps the lenses, the ledger and the Loop Review | flow-steps' Owner cells; v2's catalogue, dDeclaredLoop, dCalibratedLens, dIndexedDesign; layer-memory; layer-flow |
| H3, M7 | the P28 check's population is every edge from a core kit to a non-core kit, by kind, each kind seen red on a planted edge; today's edges are named, each made an optional slot or moved into the core | v2 dOrderedCharter |
| H4 | the moved grammar's by-path consumers are re-pointed in the move's own unit, proven by a staged break | v2 dOrderedCharter |
| H5, M6 | the reader inventory is derived by key value; the four `read_policy_key` copies, `held_halves.py` and `roles_lib.load_policy` with its callers are re-pointed in the fold's own unit, proven on a scratch clone | v2 dConvergedCharter, [policies] |
| H6, M11 | AF-2: `policy.on-invalid`, last-valid by default and refuse allowed; each failure class planted; the mirror pinned to the landed revision with a parity leg | v2 dGroundRules, [policies], the catalogue, [presets] |
| M1 | the no-reader arm's population is scoped to landed owners, a reader is defined, and the arm is seen red and green | v2 dGroundRules |
| M2 | P1, [policies] and gap-spine-07 give the schema to dGroundRules | v2 P1, [policies]; the gap register |
| M3 | dDeclaredLoop renders the charter's preset section; the [owed] item says so | v2 dDeclaredLoop, [owed] |
| M4 | P7 and P18 name the keys that tune them, their absolute wording kept as the default | v2 P7, P18 |
| M5 | the legacy homes are derived by query, each gate-env key marked owner policy or mechanic | v2 dGroundRules, [policies] |
| M8 | `review.design.round-count` is held below the runaway ceiling; dDeclaredLoop retires `REVIEW_ROUNDS` and names its readers, so it leaves dGroundRules's list | v2 the catalogue, dDeclaredLoop, dGroundRules |
| M9 | the `map_lib` move names its consumers, re-exports for one release and re-copies the template | v2 dOrderedCharter |
| M10 | one resolution order, an override, then the preset, then the default; dDeclaredLoop adds the preset step, seen red on a strict file | v2 dGroundRules, dDeclaredLoop |
| M12 | dTotalRecall's row carries gap-mem-13's fix: the counter ref, the claimant key, claim refs never pruned | v2 dTotalRecall |
| M13 | an unreachable remote never mints a local id, as `leases.offline` says | v2 dDeclaredLoop, dTotalRecall; flow-steps `entry.claim` |
| M14, M15 | RC-9's fallback drains per harness, and the witnesses written under it stay readable | v2 dWellOiledMachine |
| M16 | lib's descriptor is marked not installable, and the `*/kit.toml` consumers are named | v2 dShippedRelease |
| L1 | the [chain] heading drops its typed count | v2 [chain] |
| L2 | AF-3: `every-declared` is allowed and strict uses it; `preset` and `policy.on-invalid` are never preset; strict's fixes are named | v2 the catalogue, [presets] |
| L3 | velocity's prose names what still refuses | v2 [presets] |
| L4 | the four answered [owed] items keep their decision, the question under "Was" | v2 [owed] |
| L5 | dOrderedCharter's duplicate reach, grammar and registry clauses and dTotalRecall's duplicate report are merged | v2 dOrderedCharter, dTotalRecall |
| L6 | the charter's budget is measured against the two existing size rows, and the raise is owed | v2 dOrderedCharter |
| C1 | dShippedRelease follows dWellOiledMachine, whose points its programs register at | v2 dShippedRelease |

## [left-shift] Each finding's gate or class

- **Built now, at design time:** the reconciliation probe reads four ways: citations, a stage's items, routes into
  the breakpoint, and an expansion's registrations. It was seen red on today's tree before the fold, with 16
  findings across H1, H2 and C1, green after it, and red on each plant (`[instrument]`). It replaces
  `ancestor_probe.py`, which read citations alone and missed all three.
- **Carried into the rows, each seen red as its row says:**
  - the core-independence check over every edge kind (H3, M7);
  - the by-path and by-value inventories (H4, H5, M6, M9, M16);
  - the reader-contract arms for each failure class and preset (H6, M10, M11);
  - the scoped no-reader arm (M1) and the derived legacy list (M5);
  - the round count's bound (M8).
- **Classes,** four new ones filed and claimed in the build-method dossier:

| Class | Its findings |
| --- | --- |
| new: `step-depends-on-a-later-build` | H1, H2, C1 |
| new: `move-inventory-misses-readers-by-path` | H4, M9, M16 |
| new: `remote-write-without-an-unreachable-outcome` | M13 |
| new: `fallback-drain-strands-its-witnesses` | M14, M15 |
| `core-depends-on-an-optional-part` | H3, M7 |
| `predicate-designed-without-a-run-over-the-tree` | H3 |
| `staged-break-substitutes-a-synthetic-value` | M7 |
| `retirement-inventory-misses-readers-by-value` | H5, M6 |
| `fallback-fabricates-the-passing-value` | H6 |
| `absence-read-from-one-of-several-homes` | M10 |
| `allocation-knob-without-a-ceiling` | M8 |
| `fixture-passes-by-finding-nothing` | M1 |
| `amendment-leaves-its-other-half-standing` | M2, M3, L4 |
| `two-answers-to-one-question` | M4, M5, M11, M12, L1, L2, L3, L5, L6 |

## [critical-path] The critical path, re-measured

- **It is 181 units, from 176:** dGroundRules, dOrderedCharter, dDeclaredLoop, dWitnessedBar, dTotalRecall,
  dWellOiledMachine, dShippedRelease and dConvergedCharter.
- **What moved it:**
  - AF-1 moved units from dCalibratedLens, 13 to 8, onto dDeclaredLoop, 37 to 43;
  - AF-2's two clauses took dGroundRules from 6 to 8;
  - L5's merges and the new clauses net to nothing in dOrderedCharter and dTotalRecall.
- **C1's edge was free before the fold, and costs 2 units after it.** With dCalibratedLens smaller, the path runs
  through dShippedRelease. Without the edge it would be 179, through dCalibratedLens. The edge stays, since
  dShippedRelease's programs cannot register at points that do not yet exist.

## [instrument] The reconciliation probe, and the checks

```python
"""The order's reconciliation gate, four ways: what a build's row cites, what its stage's items are, where its
items route, and where its expansion registers, is built by that build or one of its ancestors in [chain]'s after
relation, or carries a declared class saying why it may not be.

Usage: python reconcile_probe.py <recut-record> [--plant-drop <build>:<node>] [--plant-edge-drop <child>:<parent>]
       (from the worktree root)

1. cites: each backticked citation of an owned node in a [chain] row, as `ancestor_probe.py` read it.
2. stage (the design audit's H2): a stage step is usable only once every item on it is built, so each item of the
   plan, design, build, test and deploy steps is built by the stage's build, named by [chain]'s Stage column, or by
   an ancestor of it.
3. routes (H1): an item whose Then cell, or a build whose row, names the breakpoint (a breakpoint, an owner gate,
   the spec audit or the gate review) needs the whole breakpoint program, so each breakpoint item is built by that
   build or an ancestor of it. It is read once per build, on the program's entry item, `review.trigger`.
4. registers (the main loop's C1): each expansion's contract in layer-expansions names, in its "extension points
   used" row, the Runtime points it registers at. Each point is built by every owner of that expansion's items, or
   by an ancestor of each.

Owners are read from the declared fields through the map's derivation. The classes live in the re-cut record's
[reconciled-order] table: Row, Node, Owner, Class, Why. A dependency on a non-ancestor's node with no class row, or
a class row no dependency needs, is a finding. Exit 1 on any finding.
--plant-drop removes one class row in memory; --plant-edge-drop removes one parent edge in memory, to see it red.
"""
import importlib.util
import re
import sys

B = "memory/builds/dClosedLoop/build/"
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
for i, arg in enumerate(sys.argv):
    if arg == "--plant-edge-drop":
        child, parent = sys.argv[i + 1].split(":")
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


deps = []   # (kind, build, node, node's owner)
# 1. cites.
for b, text in rows.items():
    tokens = set(re.findall(r"`([^`\s][^`]*?)(?::[^`]*)?`", text))
    for (kind, key), own in owner.items():
        spelled = key if kind != "record-kind" else key.replace("-", " ")
        if (key in tokens or spelled in tokens) and not within(own, b):
            deps.append(("cites", b, key, own))
# 2 and 3. stage and routes, over flow-steps' item tables.
items = {}   # tag: (step, owner, Then cell)
fs = open(B + "2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md", encoding="utf-8").read()
for m in re.finditer(r"^## \[([a-z-]+)\][^\n]*\n(.*?)(?=^## |\Z)", fs, flags=re.M | re.S):
    for ln in m.group(2).split("\n"):
        if ln.startswith("| `"):
            c = cells(ln)
            if len(c) == 7:
                for tag in re.findall(r"`([a-z]+\.[a-z0-9-]+)`", c[0]):
                    items[tag] = (m.group(1), c[6], c[5])
STAGES = [s for s in ("plan", "design", "build", "test", "deploy") if s in stage_build]
for tag, (step, own, _) in items.items():
    if step in STAGES and own and not within(own, stage_build[step]):
        deps.append(("stage", stage_build[step], tag, own))
BREAK = re.compile(r"breakpoint|owner gate|spec audit|gate review", re.I)
program = {(t, o) for t, (s, o, _) in items.items() if s == "breakpoint" and o}
# A source that names the breakpoint, an item's Then cell or a build's row, needs the whole program: one dependency
# per source build, on the program's entry item, naming the owners outside the source's ancestry.
sources = {own for tag, (step, own, then) in items.items() if own and step != "breakpoint" and BREAK.search(then)}
sources |= {b for b, text in rows.items() if BREAK.search(text)}
for src in sorted(sources):
    outside = sorted({o for _, o in program if not within(o, src)})
    if outside:
        deps.append(("routes", src, "review.trigger", ",".join(outside)))
# 4. registers, over layer-expansions' contracts and the item tables that follow each.
le = open(B + "2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md", encoding="utf-8").read()
points = {n["key"]: owner.get(("point", n["key"])) for n in ns["point"]}
contracts = 0
for sec in re.split(r"(?m)^\| Contract field \|", le)[1:]:
    contracts += 1
    used = next((cells(ln)[1] for ln in sec.split("\n") if ln.startswith("| extension points used |")), "")
    owners = set()
    for blk in sec.split("\n| Item | Actor |")[1:]:
        head = cells("| Item | Actor |" + blk.split("\n", 1)[0])
        oc = head.index("Owner") if "Owner" in head else None
        for ln in blk.split("\n")[2:]:
            if not ln.startswith("| `"):
                break
            c = cells(ln)
            if oc is not None and oc < len(c) and c[oc]:
                owners.add(c[oc])
    runtime = re.search(r"Runtime's ([^;]+)", used)
    words = set(re.findall(r"[a-z]+", runtime.group(1))) if runtime else set()
    for key, pown in points.items():
        if pown and key.split("-")[0] in words:
            for o in owners:
                if not within(pown, o):
                    deps.append(("registers", o, key, pown))
recut = open(sys.argv[1], encoding="utf-8").read()
section = recut.split("### [reconciled-order]", 1)[1].split("\n## ", 1)[0] if "### [reconciled-order]" in recut else ""
classes = {}
for ln in section.split("\n"):
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    if ln.startswith("| d") and len(c) >= 5:
        classes[(c[0], c[1].strip("`"))] = c[3]
if "--plant-drop" in sys.argv:
    row, node = sys.argv[sys.argv.index("--plant-drop") + 1].split(":")
    classes.pop((row, node), None)
deps = sorted(set(deps))
count = {k: sum(d[0] == k for d in deps) for k in ("cites", "stage", "routes", "registers")}
print(f"chain rows {len(rows)} · owned nodes read {len(owner)} · flow items read {len(items)} · stages {len(STAGES)} · "
      f"breakpoint items {len(program)} · contracts read {contracts} · on a non-ancestor's node {len(deps)} "
      f"({', '.join(f'{k} {v}' for k, v in count.items())}); systems are cited in prose and left out")
findings = 0
for kind, b, key, own in deps:
    cls = classes.get((b, key))
    print(f"  {b} {kind} `{key}` ({own}'s, not an ancestor): {cls or 'UNCLASSED'}")
    findings += cls is None
needed = {(b, key) for _, b, key, _ in deps}
for (b, key), cls in sorted(classes.items()):
    if (b, key) not in needed:
        print(f"  class row with no dependency: {b} `{key}` ({cls})")
        findings += 1
print(f"findings {findings}")
sys.exit(1 if findings else 0)
```

Before the fold, on the tree at `dc97a1b25`:

```text
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md
chain rows 16 · owned nodes read 396 · flow items read 81 · stages 5 · breakpoint items 8 · contracts read 3 · on a non-ancestor's node 26 (cites 10, stage 8, routes 2, registers 6); systems are cited in prose and left out
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): homonym
  dShippedRelease registers `cadence-items` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `command-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `harness-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `host-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `journal-readers` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `notification-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dFairHearing routes `review.trigger` (dCalibratedLens's, not an ancestor): UNCLASSED
  dRankedPlan routes `review.trigger` (dCalibratedLens's, not an ancestor): UNCLASSED
  dIndexedDesign stage `design.reason` (dCalibratedLens's, not an ancestor): UNCLASSED
  dIndexedDesign stage `design.recommend` (dCalibratedLens's, not an ancestor): UNCLASSED
  dRankedPlan stage `plan.reason` (dCalibratedLens's, not an ancestor): UNCLASSED
  dRankedPlan stage `plan.recommend` (dCalibratedLens's, not an ancestor): UNCLASSED
  dScopedBuild stage `build.recommend` (dCalibratedLens's, not an ancestor): UNCLASSED
  dShippedRelease stage `deploy.recommend` (dCalibratedLens's, not an ancestor): UNCLASSED
  dWitnessedBar stage `test.reason` (dCalibratedLens's, not an ancestor): UNCLASSED
  dWitnessedBar stage `test.recommend` (dCalibratedLens's, not an ancestor): UNCLASSED
findings 16
```

After the fold, every check, the probe's plants among them:

```text
$ python 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check
atlas: derived — 144 records, 2505 sections, 170 decision sections, 16 comparison areas, 30 principles
rc 0
$ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --check
map: 2149 nodes in 30 namespaces; 29794 B of 32768 (no degrade); folded 14; unarmed none
map: purposes declared 1428, derived 244, pending 477
rc 0
$ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --check --plant <case>, for each case
orphan: FINDING owner: item.entry.intake names no owning build rc 1
two-owners: FINDING owner: policy-key.preset names 2 owning builds rc 1
inferred: FINDING no inference: point.actor-kinds's owner comes from no declared field rc 1
no-owner: FINDING owner: tag-namespace.reader names no owning build rc 1
drop-line: FINDING complete: layer has nodes on no line and in no count: ['instruction'] rc 1
bad-count: FINDING count: item.* counts 108, the table holds 107 rc 1
ghost-rel: FINDING resolves: chain.dGroundRules names owner=dGhostBuild, which resolves nowhere rc 1
census: FINDING census: tools/newkit/kit.toml is on disk with no kit node rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md
chain rows 16 · owned nodes read 397 · flow items read 81 · stages 5 · breakpoint items 8 · contracts read 3 · on a non-ancestor's node 13 (cites 12, stage 0, routes 1, registers 0); systems are cited in prose and left out
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `hooks.bypass` (dWitnessedBar's, not an ancestor): not a use
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dDeclaredLoop cites `run.on-owner-question` (dBoundRoles's, not an ancestor): tolerance
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): homonym
  dFairHearing routes `review.trigger` (dDeclaredLoop's, not an ancestor): not a use
findings 0
rc 0
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-edge-drop dShippedRelease:dWellOiledMachine
  dShippedRelease registers `cadence-items` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `command-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `harness-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `host-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `journal-readers` (dWellOiledMachine's, not an ancestor): UNCLASSED
  dShippedRelease registers `notification-adapters` (dWellOiledMachine's, not an ancestor): UNCLASSED
findings 6
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-drop dFairHearing:review.trigger
  dFairHearing routes `review.trigger` (dDeclaredLoop's, not an ancestor): UNCLASSED
findings 1
rc 1
$ python reconcile_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-edge-drop dRankedPlan:dDeclaredLoop --plant-edge-drop dRankedPlan:dTotalRecall
  dRankedPlan routes `review.trigger` (dDeclaredLoop,dFairHearing's, not an ancestor): UNCLASSED
  dRankedPlan stage `plan.reason` (dDeclaredLoop's, not an ancestor): UNCLASSED
  dRankedPlan stage `plan.recommend` (dDeclaredLoop's, not an ancestor): UNCLASSED
findings 3
rc 1
$ python critical_path.py
critical path: 181 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dShippedRelease > dConvergedCharter
each build's earliest finish, in units: dGroundRules 8, dFairHearing 23, dOrderedCharter 30, dDeclaredLoop 73, dWitnessedBar 93, dBoundRoles 123, dTotalRecall 125, dIndexedDesign 134, dRankedPlan 136, dWellOiledMachine 149, dScopedBuild 158, dTendedCadence 159, dMindYourWords 165, dCalibratedLens 167, dShippedRelease 169, dConvergedCharter 181
rc 0
$ python role_matrix_v5.py flow-steps layer-roles
items 81 of 81 body rows; actor-item pairs 81; actors 15; items with a role 20; cycle roles 1; findings 0
rc 0
$ python gap_join_filed.py gap-register architecture-v2
owned twice or more: none
owned but not in the register: none
builds owning nothing: none
rc 0
$ python preset_check_canonical.py architecture-v2
catalogue keys 193 · presettable 182 · preset rows 182
no findings
rc 0
```

- **The first plant for dRankedPlan proved nothing.** Dropping only its edge to dDeclaredLoop still reads green,
  since dTotalRecall carries dDeclaredLoop as an ancestor. The plant above cuts both parents, so the stage and route
  rules each go red.
- **The role matrix reads flow-steps' 81 items alone,** and the expansions' items name no role.
