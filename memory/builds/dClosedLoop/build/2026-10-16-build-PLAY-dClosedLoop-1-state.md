# The rearchitecture's state, and what it leaves uncovered

**Serves:** research PLAY-dClosedLoop-1

The owner asked where the rearchitecture stands and what it leaves uncovered. This record answers from
the records and the history at `5e139d377`, the branch's 95th commit since its base `742957fcf`. Every
count below is derived, and `[instrument]` keeps the probes and their runs.

## [words] The owner's words, 2026-10-16

> What is the current state of this rearchitecture? What remains uncovered?

## [state] Where the build stands

- **The design is walked end to end.** It has eight layers: five core (instruction, flow, roles, memory
  and runtime) and three expansions (observability, integrations and distribution). Each layer was
  designed with the owner, reviewed twice at Tier 2 and folded.
- **What the design holds:**
  - 30 principles;
  - 149 keys in v2's policy catalogue, under four presets;
  - eight flow programs holding 75 items: Entry, the five steps, the breakpoint and the lifecycle;
  - 14 roles;
  - 193 gaps (82 HIGH, 84 MED, 27 LOW), each owned by exactly one of 15 chain builds.
- **Every directory under `tools/` has a layer home.** All 19 appear in layer-instruction's kit table.
- **The reviews:** 60 dispatches and 17 Tier-2 reports. Ten were audits that read named records whole,
  and seven were diff reviews over named ranges. No report found a blocker.
- **v2 still says the chain is unapproved,** pending the owner's revisit of the high-level architecture
  and flow.

| Deliverable | State |
|---|---|
| Research through role agents | done: every return filed under `build/` |
| The gap register | done: 193 gaps, file-cited, each owned by one chain build |
| The design rounds | every layer walked, reviewed twice and folded, though not the lexicon or the review system (`[unreviewed]`); the owner's approval is not yet recorded |
| The spec | not written: there is no `spec/` folder, and hygiene check 21 reds until a spec defines the unit |
| The declared spec audit | not run |
| The chain's folders | none open: `memory/LIVE.md` names none of the 15 builds |
| Decision rows (acceptance a) | none: `memory/DECISIONS.md` never names dClosedLoop |
| The gap join (acceptance c) | clean against v2's `[chain]`; the chain READMEs it must join do not exist yet |
| The live-build mapping | v2 adopts v1's table, made on 2026-10-14 |
| The full bar | never run on this branch: the last bar ran at `ebce889c7`, the base's parent, and every commit since is records-only |

## [unreviewed] Text no review has read

An audit's scope is the records its report names at a SHA, and a diff review's scope is its range. So
what no review has read is a fact of the history. `[instrument]` derives it, and both of its controls
are found.

- **Designs no review has read:**
  - the lexicon (`lexicon.md`, three commits from `f02d8e228` to `79d2195e7`), which dMindYourWords
    builds;
  - the review system (`review-system.md`, `5124cc67d`), which dFairHearing builds;
  - the runtime round's fold and its two settlements (`2dbf8f26f`, `e30f0acbd` and `3611a60e9`). The
    round's two audits read the design before the fold, and the first fold review came with the layers
    round, after it.
- **Folds no round has read:**
  - the layers round's follow-up fold, `1bc4883fe`, 18 items. It is the library review's base, so that
    review's diff excludes it, and the comparison record does not name it as owed.
  - the library round's fold, `0dd962724`, 19 items. It is owed, the owner deferred it on 2026-10-16,
    and layer-library `[open]` says the build does not close with it open.
  - the expansion round's follow-up fold, `5e139d377`, 14 items. A third round or a recorded debt was
    put to the owner on 2026-10-16.

  Each fold review so far confirmed 20 to 31 findings.
- **Records no review has read whole:**
  - v2 and the gap register were read only as the diffs into them;
  - foundations and flow-roles were read only through the layers round's fold;
  - no review has read the 2026-10-14 walks (coordination, flow, flow-interactions, orientation, roles,
    the session model and the walkthrough), the design rounds or the design overview.

  The declared spec audit is the first review that reads the design whole.
- **The atlas cannot show the first group.** Its progress view lists the eight layers and counts the
  reviews named for each layer's first record, so neither the lexicon nor the review system has a row.

## [undecided] What no answer settles yet

Revised 2026-10-18: the re-cut answered or applied each item below; its state is in `build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md` `[owed-state]` and `[order-review]`.

v2 `[owed]` and `[open]` carry these to the chain re-cut, and none has an answer yet:
- whether the kit confs Runtime reads (`FANOUT_CAP`, `PROCMON_REAP_MODE`, `RESUME_ATTEMPTS` and
  `RESUME_TURNS`) fold into `.governance/policy.toml`;
- the tooling order: Flow first, as dispatch 26 picked, or the instruction layer first;
- the chain's order, where v2 leaves each choice open:
  - dWellOiledMachine ahead of every stage build whose commands end with a `next —` line, or its
    `next` unit landed first;
  - dOrderedCharter's policy file, schema and reader moved into it, or its consuming units ordered
    after dDeclaredLoop, its child;
  - dTotalRecall ordered ahead of the owners of `gap-design-01` and `gap-plan-06`, or the two gaps
    moved to it;
- the roles layer's mechanical shape: each role item's agent set, effort, checklist, orientation
  template and merge, the revisit the owner set when round four opened;
- the roles layer's lower-level design: how the answered-call hook matches a Read's range, how the
  executor cuts and keys excerpts, and how a repair's ask carries the repaired fact;
- the interpretations to confirm at chain approval: positional references beyond `§`, and the
  coordination record's interpretations;
- every chain build's planned units, for the eight core points and the three expansion designs;
- dMindYourWords' second-wave packs, which wait for an adopter census and so for the owner's ask;
- `instructions.edit`'s alternatives, `flow-only` and `command-for-all`, which the owner has not
  walked: its default comes from the owner's words (layer-instruction).

Three more are decided, and the re-cut applies them to `[chain]`:
- dTotalRecall lands ahead of dIndexedDesign and dTendedCadence, which consume what it builds.
  `[chain]` already orders dTendedCadence after it, through dWellOiledMachine, but gives dIndexedDesign
  only dDeclaredLoop as its parent.
- The deployer's and the maintainer's definitions move to the builds that deliver integrations and
  observability, and dBoundRoles keeps their registration.
- gap-orient-08 moves from dDeclaredLoop to dWellOiledMachine: orientation's rule moves it with the
  executor, and RT-3 placed the executor there. v2 `[owed]` carries it since the stale sweep.

## [stale] Records that still list settled items as open

- design-overview `[open]` says K1 awaits the owner's confirmation. The owner confirmed it on
  2026-10-15: "the violator pays".
- design-overview `[open]` and coordination `[owed]` say the executor and its checklist engine have no
  owning build. RT-3 gave them to dWellOiledMachine (v2 `[owed]`).

Revised: 2026-10-16, the stale sweep: both records now carry dated notes saying what settled and where, as do
orientation `[gaps]`, the session model, layer-instruction's two policies, and the runtime and layers
comparison records. The atlas shows the lexicon and the review system, and the two items above it
missed sit in `[undecided]`.

## [next] What remains, in order

1. The owner's approval of the design, with v2 `[open]`'s interpretations.
2. The re-cut, with `[undecided]` put to the owner.
3. The spec `PLAY-dClosedLoop-1`, through a spec writer.
4. The declared audit, folded.
5. The chain's folders, then `gen_build_index.py --write`.
6. The decision rows.
7. The acceptance joins, the gap join seen red on a planted orphan first.
8. The live-build mapping, re-derived against `memory/LIVE.md`.
9. The full bar. A merge and a push need the owner's ask.

Before the build closes, each fold in `[unreviewed]` is reviewed, or the owner records it as deferred.

## [instrument] The probes and their runs

Each probe ran from the worktree root on a clean tree at `5e139d377`, before this record existed:
- `atlas_state.py`: the atlas generator's derived state: the layers, each layer's rounds, the reviews,
  the chain and the counts `[state]` cites;
- `coverage.py`: which design text no review has read, by each report's blob set or range, with two
  commits known to be reviewed as its controls;
- `kit_coverage.py`: whether every directory under `tools/` has a layer home in layer-instruction's kit
  table.

`atlas_state.py`:

```python
"""Print the atlas's derived state: layers, each layer's rounds, the chain, the reviews and v2's open and owed.

Usage: python atlas_state.py <atlas.py>
"""
import collections
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("atlas", sys.argv[1])
atlas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atlas)
d = atlas.derive()

print("== layers")
for l in d["layers"]:
    print(f"  {l['tag']:<16} {l['kind']:<12} {l['what'][:90]}")
print("== progress")
for p in d["progress"]:
    print(f"  {p['layer']:<14} records={','.join(p['records'])} reviews={len(p['reviews'])} folded={p['folded']}")
lr = d["libraryRound"]
print(f"== library round: reviews={lr['reviews']} folded={lr['folded']}")
for o in lr["open"]:
    print(f"  - {o['label']}: {o['text'][:160]} ({len(o['items'])} items)")
print("== reviews")
for r in d["reviews"]:
    print(f"  {r['scope']:<26} {r['kind']:<12} round={r['round']} {r['intensity']:<6} raw={r['raw']:<3} conf={r['confirmed']:<3} "
          f"B{r['blocker']} H{r['high']} M{r['medium']} L{r['low']} · {r['verdict'][:40]}")
print("== chain")
for c in d["chain"]:
    print(f"  {c['build']:<20} {c['stage'][:28]:<28} parents={','.join(c['parents']) or '-'} gaps={len(c['gaps'])} units={c['units'][:60]}")
sev = collections.Counter(g["sev"] for g in d["gaps"])
print(f"== gaps: {len(d['gaps'])} {dict(sev)}")
print(f"== policies: {len(d['policies'])} · presets {d['presets']['names']} · principles {len(d['principles'])}")
print(f"== steps: {[(s['tag'], len(s['items'])) for s in d['steps']]}")
print(f"== roster: {len(d['roster'])} roles · decisions: {len(d['decisions'])} sections · events: {len(d['events'])}")
print(f"== timeline: {len(d['timeline'])} revisions, latest {d['latest']}")
for k in ("owed", "v2open"):
    v = d[k]
    print(f"== {k}: {type(v).__name__} {list(v.keys()) if isinstance(v, dict) else v}")
```

Its run:

```text
== layers
  instruction      core         everything an agent is told, levelled 0 to 7 and tagged by scope
  flow             core         a build's lifecycle: Plan, Design, Build, Test and Deploy as programs of items, review as 
  roles            core         the bound workers, and the driver
  memory           core         the trail, what happened in a build: records, transitions, witnesses, the card's truth; an
  runtime          core         what executes the cycle: the supervisor and its checklist engine, act sessions and the spa
  observability    expansion    signals about the loop and the runtime, read and filed but never deciding a position, and 
  integrations     expansion    adapters to outside services, each registered at the core point it serves under one header
  distribution     expansion    the product's delivery across a repository boundary: govkit's install by copy at a release
== progress
  instruction    records=2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md reviews=2 folded=True
  flow           records=2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md,2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md,2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md reviews=2 folded=True
  roles          records=2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md reviews=2 folded=True
  memory         records=2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md,2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md reviews=2 folded=True
  runtime        records=2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md reviews=2 folded=True
  observability  records=2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md reviews=2 folded=True
  integrations   records=2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md reviews=2 folded=True
  distribution   records=2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md reviews=2 folded=True
== library round: reviews=['2026-10-16-review-PLAY-dClosedLoop-1-library.md'] folded=True
  - A follow-up round: over `[review-fold]` (`0dd962724`) is owed. The owner deferred it on 2026-10-16: "Let's record the follow-up round debt and skip it for now". It stays owed unti (0 items)
== reviews
  flow-a                     spec-audit   round=1 full   raw=69  conf=60  B0 H6 M43 L11 · CLEAN WITH FIXES
  flow-b                     spec-audit   round=1 full   raw=46  conf=45  B0 H3 M32 L10 · CLEAN WITH FIXES
  instruction-a              spec-audit   round=1 full   raw=48  conf=44  B0 H4 M28 L12 · CLEAN WITH FIXES
  instruction-b              spec-audit   round=1 full   raw=47  conf=36  B0 H4 M21 L11 · CLEAN WITH FIXES
  memory-a                   spec-audit   round=1 full   raw=61  conf=52  B0 H1 M39 L12 · CLEAN WITH FIXES
  memory-b                   spec-audit   round=1 full   raw=58  conf=51  B0 H5 M34 L12 · CLEAN WITH FIXES
  roles-a                    spec-audit   round=1 full   raw=47  conf=37  B0 H0 M28 L9 · CLEAN WITH FIXES
  roles-b                    spec-audit   round=1 full   raw=54  conf=43  B0 H1 M32 L10 · CLEAN WITH FIXES
  runtime-a                  spec-audit   round=1 full   raw=60  conf=56  B0 H6 M45 L5 · CLEAN WITH FIXES
  runtime-b                  spec-audit   round=1 full   raw=61  conf=57  B0 H9 M44 L4 · CLEAN WITH FIXES
  expansions-a               diff-review  round=1 full   raw=45  conf=37  B0 H1 M27 L9 · CLEAN WITH FIXES
  expansions-b               diff-review  round=1 full   raw=54  conf=46  B0 H5 M27 L14 · CLEAN WITH FIXES
  expansions-fold-followup   diff-review  round=2 light  raw=35  conf=24  B0 H5 M16 L3 · CLEAN WITH FIXES
  expansions-fold            diff-review  round=1 light  raw=28  conf=20  B0 H4 M10 L6 · CLEAN WITH FIXES
  fold-followup              diff-review  round=2 light  raw=34  conf=31  B0 H2 M24 L5 · CLEAN WITH FIXES
  fold                       diff-review  round=1 light  raw=31  conf=28  B0 H3 M19 L6 · CLEAN WITH FIXES
  library                    diff-review  round=1 light  raw=31  conf=25  B0 H1 M20 L4 · CLEAN WITH FIXES
== chain
  dOrderedCharter      Foundation                   parents=dClosedLoop gaps=17 units=the practice catalogue with each practice's reach per stage,
  dFairHearing         Review harness               parents=dClosedLoop gaps=7 units=the owed replays first: the design-audit preset run blind at
  dDeclaredLoop        Spine                        parents=dOrderedCharter gaps=19 units=the loop kit and definition keyed by the stage tags, the rol
  dBoundRoles          Roles                        parents=dDeclaredLoop gaps=20 units=the roster sorted by layer: twelve core roles (orientation s
  dTotalRecall         Memory                       parents=dDeclaredLoop gaps=15 units=the memory contract: the record-kind registry (per kind: tag
  dMindYourWords       Lexicon                      parents=dTotalRecall gaps=9 units=the definition classes (conforming, forced, out of scope, no
  dWellOiledMachine    Runtime                      parents=dBoundRoles,dTotalRecall gaps=26 units=the platform spike first: a role-typed Workflow agent run in
  dWitnessedBar        Test                         parents=dDeclaredLoop gaps=15 units=gate health measured and the reliability bar; bypasses recor
  dRankedPlan          Plan                         parents=dDeclaredLoop gaps=10 units=priority beside `parents:` and the generated plan view; the 
  dIndexedDesign       Design                       parents=dDeclaredLoop gaps=8 units=the derived-READY hand-off; the design index; design review 
  dScopedBuild         Build                        parents=dIndexedDesign,dWitnessedBar,dWellOiledMachine gaps=6 units=one exit contract with a history-derived base, refusing a bu
  dShippedRelease      Deploy                       parents=dWitnessedBar gaps=16 units=the landing record; kit release notes; the deploy engine; th
  dTendedCadence       Maintain                     parents=dWitnessedBar,dRankedPlan,dWellOiledMachine gaps=10 units=the Maintain run as its step checklist on the flow's executo
  dCalibratedLens      Review                       parents=dTendedCadence,dFairHearing gaps=8 units=review by policy per stage and effort; the stage-exit recomm
  dConvergedCharter    Convergence                  parents=dScopedBuild,dShippedRelease,dCalibratedLens gaps=7 units=protocol text derived to facts only, each document in its en
== gaps: 193 {'HIGH': 82, 'MED': 84, 'LOW': 27}
== policies: 149 · presets ['velocity', 'standard', 'strict', 'guarded'] · principles 30
== steps: [('entry', 6), ('plan', 11), ('design', 12), ('build', 9), ('test', 10), ('deploy', 13), ('breakpoint', 8), ('lifecycle', 6)]
== roster: 14 roles · decisions: 144 sections · events: 66
== timeline: 37 revisions, latest 2026-10-16
== owed: dict ['path', 'id']
== v2open: dict ['path', 'id']
```

`coverage.py`:

```python
"""Which design text no Tier-2 review has read. Each report's Reviewed line is a blob set (an audit that read
named records whole) or a range (a diff review); a record or a commit outside all of them is unreviewed.

Usage: python coverage.py   (from the worktree root)
"""
import pathlib
import re
import subprocess
import sys

REV = pathlib.Path("memory/builds/dClosedLoop/reviews")
BUILD = pathlib.Path("memory/builds/dClosedLoop/build")


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True)


def inside(c, a, b):
    """True when commit c lies in the range (a, b]."""
    return (git("merge-base", "--is-ancestor", c, b).returncode == 0
            and git("merge-base", "--is-ancestor", c, a).returncode != 0)


blobs, ranges = {}, {}
for p in sorted(REV.glob("*.md")):
    m = re.search(r"^Reviewed: (.+)$", p.read_text(encoding="utf-8"), re.M)
    if not m:
        sys.exit(f"{p.name} has no Reviewed line")
    r = re.match(r"([0-9a-f]{40})\.\.\.([0-9a-f]{40})", m.group(1))
    if r:
        ranges[p.stem.split("PLAY-dClosedLoop-1-")[1]] = (r.group(1), r.group(2))
    else:
        blobs[p.stem.split("PLAY-dClosedLoop-1-")[1]] = sorted(
            {re.sub(r".*PLAY-dClosedLoop-1-", "", x.split("@")[0].strip()).removesuffix(".md")
             for x in m.group(1).split(",") if "@" in x})
if len(blobs) + len(ranges) != len(list(REV.glob("*.md"))):
    sys.exit("a report was read as neither a blob set nor a range")
read_whole = sorted({r for v in blobs.values() for r in v})
print(f"reports: {len(blobs)} blob-set audits, {len(ranges)} diff reviews")
print(f"records an audit read whole: {', '.join(read_whole)}")

touched = {s: set(git("diff", "--name-only", a, b).stdout.split()) for s, (a, b) in ranges.items()}
design = sorted(p for p in BUILD.glob("*.md") if not re.search(r"-1-(research-|session-log|compaction-)|compared|instruments", p.name))
print(f"design records, research returns, the log and the comparisons left out: {len(design)}")
for p in design:
    rec = p.stem.split("PLAY-dClosedLoop-1-")[1]
    hit = [s for s, t in touched.items() if p.as_posix() in t]
    print(f"  {rec}: read whole {'yes' if rec in read_whole else 'no'} · in diff ranges: {', '.join(hit) or 'none'}")

for what, cs in {"control, the expansion fold": ["6e0ce0a55"], "control, the library design": ["aa9639d98"],
                 "lexicon": ["f02d8e228", "178d4e805", "79d2195e7"], "review system": ["5124cc67d"],
                 "runtime fold and settlements": ["2dbf8f26f", "e30f0acbd", "3611a60e9"],
                 "layers follow-up fold": ["1bc4883fe"], "library fold": ["0dd962724"],
                 "expansions follow-up fold": ["5e139d377"]}.items():
    for c in cs:
        hit = [s for s, (a, b) in ranges.items() if inside(c, a, b)]
        print(f"{what} {c}: inside a reviewed range: {', '.join(hit) or 'none'}")
```

Its run:

```text
reports: 10 blob-set audits, 7 diff reviews
records an audit read whole: flow-steps, layer-flow, layer-instruction, layer-memory, layer-roles, layer-runtime
design records, research returns, the log and the comparisons left out: 25
  architecture-v0: read whole no · in diff ranges: none
  architecture-v1: read whole no · in diff ranges: none
  architecture-v2: read whole no · in diff ranges: expansions-a, expansions-b, expansions-fold-followup, expansions-fold, fold-followup, fold, library
  coordination: read whole no · in diff ranges: none
  design-rounds: read whole no · in diff ranges: none
  flow-interactions: read whole no · in diff ranges: none
  flow: read whole no · in diff ranges: none
  foundations: read whole no · in diff ranges: fold
  gap-register: read whole no · in diff ranges: expansions-a, expansions-b, expansions-fold-followup, expansions-fold, fold-followup, fold, library
  orientation: read whole no · in diff ranges: none
  roles: read whole no · in diff ranges: none
  session-model: read whole no · in diff ranges: none
  walkthrough: read whole no · in diff ranges: none
  design-overview: read whole no · in diff ranges: none
  flow-roles: read whole no · in diff ranges: fold-followup, fold
  flow-steps: read whole yes · in diff ranges: expansions-a, expansions-b, expansions-fold-followup, expansions-fold, fold-followup, fold, library
  layer-flow: read whole yes · in diff ranges: fold-followup, fold, library
  layer-instruction: read whole yes · in diff ranges: fold-followup, fold, library
  layer-memory: read whole yes · in diff ranges: expansions-a, expansions-b, expansions-fold, fold-followup, fold, library
  layer-roles: read whole yes · in diff ranges: expansions-a, expansions-b, expansions-fold, fold-followup, fold, library
  layer-runtime: read whole yes · in diff ranges: expansions-a, expansions-b, expansions-fold-followup, expansions-fold, fold-followup, library
  lexicon: read whole no · in diff ranges: none
  review-system: read whole no · in diff ranges: none
  layer-expansions: read whole no · in diff ranges: expansions-a, expansions-b, expansions-fold-followup, expansions-fold
  layer-library: read whole no · in diff ranges: library
control, the expansion fold 6e0ce0a55: inside a reviewed range: expansions-fold
control, the library design aa9639d98: inside a reviewed range: library
lexicon f02d8e228: inside a reviewed range: none
lexicon 178d4e805: inside a reviewed range: none
lexicon 79d2195e7: inside a reviewed range: none
review system 5124cc67d: inside a reviewed range: none
runtime fold and settlements 2dbf8f26f: inside a reviewed range: none
runtime fold and settlements e30f0acbd: inside a reviewed range: none
runtime fold and settlements 3611a60e9: inside a reviewed range: none
layers follow-up fold 1bc4883fe: inside a reviewed range: none
library fold 0dd962724: inside a reviewed range: none
expansions follow-up fold 5e139d377: inside a reviewed range: none
```

`kit_coverage.py`:

```python
"""Does every directory under tools/ have a layer home in layer-instruction's kit table, as the atlas parses it?

Usage: python kit_coverage.py <atlas.py>   (from the worktree root)
"""
import importlib.util
import pathlib
import sys

spec = importlib.util.spec_from_file_location("atlas", sys.argv[1])
atlas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atlas)
d = atlas.derive()
named = " ".join(k["kit"] for k in d["kits"]).lower()
dirs = sorted(p.name for p in pathlib.Path("tools").iterdir() if p.is_dir() and not p.name.startswith((".", "__")))
kits = [x for x in dirs if (pathlib.Path("tools") / x / "kit.toml").exists()]
print(f"tool dirs {len(dirs)}, with kit.toml {len(kits)}, kit-table rows {len(d['kits'])}")
print(f"dirs the kit table never names: {[x for x in dirs if x.lower() not in named] or 'none'}")
```

Its run:

```text
tool dirs 19, with kit.toml 17, kit-table rows 19
dirs the kit table never names: none
```

## [revisit] The state, revisited at the owner's question, 2026-10-17

The owner asked, verbatim:

> What's is the current state of this design, what parts are yet missing and unreviewed? Is it converging into a cohesive architecture?

### [revisit-state] What the design holds

|  | 2026-10-16, `[state]` | 2026-10-17 |
| --- | --- | --- |
| layers | 8 | 8 |
| principles | 30 | 30 |
| roles | 14 | 14 |
| chain builds | 15 | 15 |
| systems | 0 | 7 |
| steps, and their items | 8, holding 75 | 9, holding 81 |
| policy catalogue rows | 149 | 187 |
| gaps | 193 | 222 |
| Tier-2 reports | 17 | 31 |
| decision sections | 144 | 164 |

- **The skeleton has held.** Layers, principles, roles, chain builds and the stage set are unchanged
  since `[state]`. The joins are clean: every gap is owned by exactly one chain build, the role matrix
  reads 81 items with no finding, and the presets cover 182 of 182 presettable keys.
- **No review has found a blocker,** in 31 reports.
- **The detail has grown.** The systems round, the retrofit and the project map added the seven
  systems, 38 catalogue rows, 29 gaps, the adopt step and its 5 items.

### [revisit-unreviewed] Text no review has read

`coverage_v2.py` (`[revisit-instrument]`) attributes each current line of each design record to the
commit that last wrote it. A line is reviewed when an audit read its record at a later blob, or when
its commit lies inside a reviewed range.

- **8,961 of 18,422 lines (49%)** in 30 design records have been read by no review.
- **All of `[unreviewed]`'s list has been reviewed since.** The lexicon and the review system were
  audited, and the runtime, layers, library and expansions folds each had a follow-up round.
- **What no review has read now:**
  - v2: 849 of its 1,207 lines (70%). No audit has read it whole, only the diffs into it;
  - the gap register: 353 of 541 (65%), never read whole either;
  - the project map: all 1,618 lines;
  - the systems and retrofit audit's fold (`274085b92`), 895 lines across its records, and the closing
    review's fold (`2cb3a2c23`), 171. Each earlier fold review confirmed 18 to 31 findings;
  - the 2026-10-14 walks (the walk-through, flow, roles, orientation, coordination, the session model,
    the design rounds, the overview, flow interactions, v0 and v1). v2 consolidated them, and none of
    them was reviewed itself.
- **Its control is seen:** with the systems and retrofit audit left out, systems reads 98% unreviewed
  and retrofit 99%, from 37% and 48%.

### [revisit-recut] What the chain still owes

Revised 2026-10-18: each item's state is in `build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md` `[owed-state]` and `[order-review]`.

v2 `[owed]` and `[undecided]`, re-checked against v2's `[chain]` and the project map's `after=` and
`owner=` relations:
- **Decided on 2026-10-16, and not yet applied to `[chain]`:**
  - dTotalRecall ahead of dIndexedDesign, which uses its house index. dIndexedDesign still follows
    dDeclaredLoop alone;
  - `gap-orient-08` moved to dWellOiledMachine. It is still dDeclaredLoop's;
  - the deployer's and the maintainer's definitions moved to the builds that deliver integrations and
    observability. Neither dShippedRelease's row nor dTendedCadence's names them.
- **Still undecided:**
  - dOrderedCharter consumes `instructions.*` from a policy file, schema and reader that dDeclaredLoop,
    its child, builds;
  - `gap-design-01` is dDeclaredLoop's, and dTotalRecall, its child, builds the fix;
  - whether the kit confs that Runtime reads fold into the policy file;
  - the tooling order;
  - the roles layer's lower-level design: the answered-call hook's matching, the excerpt keys, and a
    repair's carry;
  - the interpretations to confirm at chain approval, and `instructions.edit`'s alternatives;
  - dMindYourWords' second-wave packs, which wait for an adopter census.
- **Answered since:**
  - `gap-plan-06`'s owner, dRankedPlan, now follows dTotalRecall;
  - dWellOiledMachine's row lands the `next` check with the laggards on a shrink-only list, so the
    stage builds need not follow it. `[owed]` still lists the item.
- **Ownership** (the project map's `[fixes]`, PM-8 and PM-10): 115 of 187 policy keys are cited by no
  chain row, and the ownership table is next.

### [revisit-converging] Is it converging

- **The skeleton has converged.** It has not moved across the last two rounds, its joins are clean,
  and no review has found a blocker.
- **Each surface converges under review.** A first audit confirms 36 to 62 findings, its fold review
  18 to 31, and a third round 12 to 21.
- **The whole has not.** It grows faster than it closes:
  - v2 has grown from 145 lines at its consolidation to 1,207, with 46 revision notes, and its
    catalogue from 41 rows to 187;
  - the branch's commits ran 32, 30, 44 and 54 a day;
  - each new surface opens at the first audit's rate again: the systems and retrofit audit confirmed
    62.
- **The seams are where cohesion is missing:**
  - ownership has four homes and no field;
  - the chain's order holds the conflicts above;
  - v2, the record that joins the design, has never been read whole.
- **The build's exit is untouched:**
  - there is no spec and no whole-design audit;
  - no chain build has a folder or a `memory/LIVE.md` row;
  - `memory/DECISIONS.md` names dClosedLoop 0 times;
  - no bar has run since `ebce889c7` (2026-10-13).

### [revisit-next] What closes it, in order

1. Stop adding surface until the seams close.
2. PM-10's ownership table, approved and folded.
3. The re-cut: the three decided moves applied, and the undecided put to the owner.
4. The declared audit, reading v2, the gap register and the chain whole, with the layer records as
   context, and its fold reviewed.
5. The spec, the chain's folders, the decision rows, the acceptance joins, and the full bar.

### [revisit-instrument] The probes and their runs

Each ran from the worktree root on a clean tree at `f21b63ab9`, before this section existed.

```python
"""Which lines of dClosedLoop's design records no Tier-2 review has read, line by line.

Usage: python coverage_v2.py [--plant-uncover <review-stem>]   (from the worktree root)

Each report's "Reviewed:" or "Range:" line is a blob set (an audit that read named records whole at those
blobs) or a range (a diff review over (base, head]). `git blame HEAD` gives every current line the commit that
last wrote it. A line is reviewed when an audit read its record at a blob whose commit descends from that
commit, or when that commit lies inside a reviewed range. Anything else is unreviewed.
--plant-uncover drops one report, to see the lines it covered turn unreviewed.
"""
import collections
import pathlib
import re
import subprocess
import sys

REV = pathlib.Path("memory/builds/dClosedLoop/reviews")
BUILD = pathlib.Path("memory/builds/dClosedLoop/build")
SKIP = re.compile(r"-1-(research-|session-log|compaction-)|compared|instruments")


def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True, encoding="utf-8")
    return r.stdout


drop = sys.argv[sys.argv.index("--plant-uncover") + 1] if "--plant-uncover" in sys.argv else None
audits, ranges = [], {}
for p in sorted(REV.glob("*.md")):
    stem = p.stem.split("PLAY-dClosedLoop-1-")[1]
    if stem == drop:
        continue
    m = re.search(r"^(?:Reviewed|Range|Range reviewed): (.+)$", p.read_text(encoding="utf-8"), re.M)
    if not m:
        sys.exit(f"{p.name}: no Reviewed or Range line")
    r = re.match(r"([0-9a-f]{40})\.\.\.?([0-9a-f]{40})", m.group(1))
    if r:
        ranges[stem] = set(git("rev-list", f"{r.group(1)}..{r.group(2)}").split())
        continue
    pairs = re.findall(r"(memory/builds/dClosedLoop/build/[^@,\s]+\.md)@([0-9a-f]{40})", m.group(1))
    if not pairs:
        sys.exit(f"{p.name}: a Reviewed line that is neither a range nor a blob set")
    audits += [(stem, path, blob) for path, blob in pairs]
print(f"reports read: {len(set(a[0] for a in audits))} audits over {len(audits)} record blobs, {len(ranges)} diff ranges")

# For each audited (record, blob): the commits touching the record that the audit point descends from.
# `audited` is kept apart, since a lookup in the defaultdict would add every record to it.
covered_by_audit = collections.defaultdict(set)
audited = {path for _, path, _ in audits}
for stem, path, blob in audits:
    cands = git("log", "--format=%H", f"--find-object={blob}", "--", path).split()
    points = [c for c in cands if git("rev-parse", f"{c}:{path}").strip() == blob]
    if not points:
        sys.exit(f"{stem}: blob {blob[:9]} of {path} matches no commit")
    covered_by_audit[path] |= set(git("rev-list", points[0], "--", path).split())

subject = {}
rows = []
for p in sorted(BUILD.glob("*.md")):
    if SKIP.search(p.name):
        continue
    path = p.as_posix()
    blame = git("blame", "--line-porcelain", "HEAD", "--", path)
    commits = [ln.split()[0] for ln in blame.split("\n") if re.match(r"^[0-9a-f]{40} \d+ \d+", ln)]
    unrev = collections.Counter()
    for c in commits:
        if c in covered_by_audit[path] or any(c in s for s in ranges.values()):
            continue
        unrev[c] += 1
    for c in unrev:
        if c not in subject:
            subject[c] = git("log", "-1", "--format=%h %s", c).strip()
    rows.append((p.stem.split("PLAY-dClosedLoop-1-")[1], len(commits), sum(unrev.values()),
                 path in audited, unrev))

total = sum(r[1] for r in rows)
unrev_total = sum(r[2] for r in rows)
print(f"design records {len(rows)} · lines {total} · unreviewed {unrev_total} ({100 * unrev_total / total:.0f}%)")
print()
print(f"{'record':<34} {'lines':>6} {'unrev':>6} {'share':>6}  read whole")
for name, n, u, whole, _ in sorted(rows, key=lambda r: -r[2]):
    print(f"{name:<34} {n:>6} {u:>6} {100 * u / n if n else 0:>5.0f}%  {'yes' if whole else 'no'}")
print()
by_commit = collections.Counter()
for *_, unrev in rows:
    by_commit.update(unrev)
print("unreviewed lines by the commit that wrote them, the largest 25:")
for c, n in by_commit.most_common(25):
    print(f"  {n:>5}  {subject[c][:150]}")
```

```text
$ python coverage_v2.py
reports read: 15 audits over 18 record blobs, 16 diff ranges
design records 30 · lines 18422 · unreviewed 8961 (49%)

record                              lines  unrev  share  read whole
project-map                          1618   1618   100%  no
walkthrough                           864    864   100%  no
architecture-v2                      1207    849    70%  no
flow                                  745    745   100%  no
roles                                 413    413   100%  no
state                                 389    389   100%  no
foundations                           400    380    95%  no
systems                               997    368    37%  yes
gap-register                          541    353    65%  no
orientation                           353    353   100%  no
design-rounds                         303    303   100%  no
retrofit                              608    293    48%  yes
flow-roles                            309    292    94%  no
session-model                         273    273   100%  no
design-overview                       229    229   100%  no
layer-roles                          1730    195    11%  yes
final-reviews                         186    186   100%  no
coordination                          182    182   100%  no
architecture-v1                       178    178   100%  no
flow-interactions                     170    170   100%  no
architecture-v0                       113    113   100%  no
layer-runtime                        1367     68     5%  yes
layer-expansions                      699     54     8%  no
layer-library                         429     40     9%  no
flow-steps                            781     28     4%  yes
layer-memory                         1149     11     1%  yes
review-system                         387      9     2%  yes
layer-instruction                     769      5     1%  yes
layer-flow                            363      0     0%  yes
lexicon                               670      0     0%  yes

unreviewed lines by the commit that wrote them, the largest 25:
    895  274085b92 records(dClosedLoop): the systems and retrofit audit folded — all 52 items amended, the ledger's populations kept where their checks keep th
    415  ade9e49e3 records(dClosedLoop): design rounds 1 to 4 and the converged v1 architecture
    390  e265c40c2 records(dClosedLoop): the owner asks how an agent sees the whole project at once — 37 of the audit's 52 items needed a piece not in view, a 
    364  3be2225ae records(dClosedLoop): the rearchitecture's state recorded at the owner's question — no review has read the lexicon, the review system or the
    331  55cc777f8 records(dClosedLoop): the project map designed from what both runs agree on — a tiered map in core memory, its delivery by role, its checks 
    320  93cbe65c1 records(dClosedLoop): walk-through — Concurrency, Test, Plan and Design settled, Build drafted
    283  df49d1c0b records(dClosedLoop): walk-through — Build, Deploy, Maintain and Review settled, Convergence drafted
    276  e93ce4ea3 records(dClosedLoop): both orientation interpretations confirmed; one build modelled through every step, and fourteen holes
    255  077602d0a records(dClosedLoop): the flow layer, Plan's scope and boundaries, unattended by default, Design drafted
    241  2f8829d35 records(dClosedLoop): what the map's findings say to fix — ownership has four homes and no field, lifecycle is owned after all, and forks PM
    240  17e0f7394 records(dClosedLoop): the gap register and the v0 architecture proposal
    233  5b6a11ce2 records(dClosedLoop): round 5, and the walk-through's Spine settled and Concurrency drafted
    228  b10785bd8 records(dClosedLoop): the roles layer designed — bound workers, a driver that does no role work, every checklist item mapped to its actor
    226  525b64a97 records(dClosedLoop): coordination designed in — dLeasedFleet leaves the chain, and no build outside it is counted on
    212  ca6d9b93d records(dClosedLoop): the design at this stage — an overview of the three layers, the chain and what is open
    196  b85510fa6 records(dClosedLoop): entry, orientation and progression — the measured state, the design, and ten gaps
    175  aa0d778b1 records(dClosedLoop): foundations step 1 — the ranked charter, practices with reach, a new root build
    172  b0b3f29bc records(dClosedLoop): the flow revisit settled — the request is the ratification, no fork parks a build, every hole closed
    171  2cb3a2c23 records(dClosedLoop): the folds' closing review folded — 19 of 20 items fixed, the high sent to the owner as RT-4, and update's git writes f
    161  01dcdd1ae records(dClosedLoop): the project map test-run — the whole design mapped at 2,008 nodes in 24.1 KB, every check seen red, and the atlas's dr
    159  6353ef8ac records(dClosedLoop): the core cannot be built around — principle registry, meta-check, factories
    159  c6e9d44ab records(dClosedLoop): the map reloaded after the compaction, and what only it points at — entry and lifecycle, 12 items no build owns
    156  f21b63ab9 records(dClosedLoop): the compaction summary was not verbatim — 3 of the map's 355 lines rewritten, the generator mines no README prose, and
    155  e56f13caa records(dClosedLoop): the flow revisited with roles — one item cycle, each step's role sequence and routes
    154  d56c897fc records(dClosedLoop): the walk-through completed, and architecture v2 consolidated
$ python coverage_v2.py --plant-uncover systems-retrofit
reports read: 14 audits over 16 record blobs, 16 diff ranges
design records 30 · lines 18422 · unreviewed 9886 (54%)

record                              lines  unrev  share  read whole
project-map                          1618   1618   100%  no
systems                               997    982    98%  no
walkthrough                           864    864   100%  no
architecture-v2                      1207    849    70%  no
flow                                  745    745   100%  no
retrofit                              608    604    99%  no
roles                                 413    413   100%  no
state                                 389    389   100%  no
foundations                           400    380    95%  no
gap-register                          541    353    65%  no
orientation                           353    353   100%  no
design-rounds                         303    303   100%  no
flow-roles                            309    292    94%  no
session-model                         273    273   100%  no
design-overview                       229    229   100%  no
layer-roles                          1730    195    11%  yes
final-reviews                         186    186   100%  no
coordination                          182    182   100%  no
architecture-v1                       178    178   100%  no
flow-interactions                     170    170   100%  no
architecture-v0                       113    113   100%  no
layer-runtime                        1367     68     5%  yes
layer-expansions                      699     54     8%  no
layer-library                         429     40     9%  no
flow-steps                            781     28     4%  yes
layer-memory                         1149     11     1%  yes
review-system                         387      9     2%  yes
layer-instruction                     769      5     1%  yes
layer-flow                            363      0     0%  yes
lexicon                               670      0     0%  yes

unreviewed lines by the commit that wrote them, the largest 25:
    895  274085b92 records(dClosedLoop): the systems and retrofit audit folded — all 52 items amended, the ledger's populations kept where their checks keep th
    415  ade9e49e3 records(dClosedLoop): design rounds 1 to 4 and the converged v1 architecture
    390  e265c40c2 records(dClosedLoop): the owner asks how an agent sees the whole project at once — 37 of the audit's 52 items needed a piece not in view, a 
    364  3be2225ae records(dClosedLoop): the rearchitecture's state recorded at the owner's question — no review has read the lexicon, the review system or the
    331  55cc777f8 records(dClosedLoop): the project map designed from what both runs agree on — a tiered map in core memory, its delivery by role, its checks 
    320  93cbe65c1 records(dClosedLoop): walk-through — Concurrency, Test, Plan and Design settled, Build drafted
    314  f839cb100 records(dClosedLoop): the systems round's two runs compared and its design drafted — one tag grammar and one derived index shared with memor
    283  df49d1c0b records(dClosedLoop): walk-through — Build, Deploy, Maintain and Review settled, Convergence drafted
    276  e93ce4ea3 records(dClosedLoop): both orientation interpretations confirmed; one build modelled through every step, and fourteen holes
    255  077602d0a records(dClosedLoop): the flow layer, Plan's scope and boundaries, unattended by default, Design drafted
    241  2f8829d35 records(dClosedLoop): what the map's findings say to fix — ownership has four homes and no field, lifecycle is owned after all, and forks PM
    240  17e0f7394 records(dClosedLoop): the gap register and the v0 architecture proposal
    233  5b6a11ce2 records(dClosedLoop): round 5, and the walk-through's Spine settled and Concurrency drafted
    228  b10785bd8 records(dClosedLoop): the roles layer designed — bound workers, a driver that does no role work, every checklist item mapped to its actor
    226  525b64a97 records(dClosedLoop): coordination designed in — dLeasedFleet leaves the chain, and no build outside it is counted on
    212  ca6d9b93d records(dClosedLoop): the design at this stage — an overview of the three layers, the chain and what is open
    196  b85510fa6 records(dClosedLoop): entry, orientation and progression — the measured state, the design, and ten gaps
    178  8537cc641 records(dClosedLoop): the retrofit design — a system across the layers, its ledger in the core: one baseline primitive seeded at every check
    175  aa0d778b1 records(dClosedLoop): foundations step 1 — the ranked charter, practices with reach, a new root build
    172  b0b3f29bc records(dClosedLoop): the flow revisit settled — the request is the ratification, no fork parks a build, every hole closed
    171  2cb3a2c23 records(dClosedLoop): the folds' closing review folded — 19 of 20 items fixed, the high sent to the owner as RT-4, and update's git writes f
    161  01dcdd1ae records(dClosedLoop): the project map test-run — the whole design mapped at 2,008 nodes in 24.1 KB, every check seen red, and the atlas's dr
    159  6353ef8ac records(dClosedLoop): the core cannot be built around — principle registry, meta-check, factories
    159  c6e9d44ab records(dClosedLoop): the map reloaded after the compaction, and what only it points at — entry and lifecycle, 12 items no build owns
    156  f21b63ab9 records(dClosedLoop): the compaction summary was not verbatim — 3 of the map's 355 lines rewritten, the generator mines no README prose, and
```

```bash
#!/usr/bin/env bash
# How the design has grown since v2's consolidation, and the build's state against its acceptance. Run from the
# worktree root; prints to stdout.
set -u
B=memory/builds/dClosedLoop
V=$B/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
C=d56c897fc
cat_rows() { awk '/^## \[policies\]/{f=1;next} /^## \[/{f=0} f && /^\| `/' | wc -l; }
echo "\$ v2 at its consolidation ($(git log -1 --format='%h %cs' $C)) and at HEAD ($(git log -1 --format='%h' HEAD))"
echo "lines $(git show $C:$V | wc -l) -> $(wc -l < $V)"
echo "catalogue rows $(git show $C:$V | cat_rows) -> $(cat_rows < $V)"
echo "revision notes $(git show $C:$V | grep -c '^Revised: ') -> $(grep -c '^Revised: ' $V)"
echo "\$ commits on the build's branch since its base, by day"
git log --format=%cs 742957fcf..HEAD | sort | uniq -c
echo "\$ the build's own deliverables"
echo "spec folder: $([ -d $B/spec ] && echo present || echo absent)"
n=0; for c in dOrderedCharter dFairHearing dDeclaredLoop dBoundRoles dTotalRecall dMindYourWords dWellOiledMachine \
  dWitnessedBar dRankedPlan dIndexedDesign dScopedBuild dShippedRelease dTendedCadence dCalibratedLens dConvergedCharter; do
  { [ -d memory/builds/$c ] || grep -q "$c" memory/LIVE.md; } && n=$((n + 1)); done
echo "chain builds with a folder or a LIVE.md row: $n of 15"
echo "memory/DECISIONS.md lines naming dClosedLoop: $(grep -c dClosedLoop memory/DECISIONS.md)"
echo "the last bar's commit: $(git log -1 --format='%h %cs' ebce889c7) (the kickoff card's drift line)"
```

```text
$ bash growth_probe.sh
$ v2 at its consolidation (d56c897fc 2026-10-14) and at HEAD (f21b63ab9)
lines 145 -> 1207
catalogue rows 41 -> 187
revision notes 0 -> 46
$ commits on the build's branch since its base, by day
     32 2026-10-14
     30 2026-10-15
     44 2026-10-16
     54 2026-10-17
$ the build's own deliverables
spec folder: absent
chain builds with a folder or a LIVE.md row: 0 of 15
memory/DECISIONS.md lines naming dClosedLoop: 0
the last bar's commit: ebce889c7 2026-10-13 (the kickoff card's drift line)
```

## [convergence] The owner's order, 2026-10-17

The owner said, verbatim:

> Let's take convergence steps in order, then. No new scope until 2-4 are done but we're not 'finishing the build' until this design takes full shape. Execute on The PM-10 ownership table, The chain reordering, and The review declared at kickoff.

- **Steps 2 to 4 of `[revisit-next]` run in order:**
  - PM-10's ownership table, approved and folded (`build/2026-10-17-build-PLAY-dClosedLoop-1-ownership.md`);
  - the re-cut: the three decided moves applied, and the undecided put to the owner;
  - the declared audit, reading v2, the gap register and the chain whole, and its fold reviewed.
- **No new scope until all three are done.** A review's findings are folds, not scope.
- **The build's exit waits** until the design takes its full shape: the spec, the chain's folders, the
  decision rows, the acceptance joins and the full bar. Step 5 is not started on the three's completion
  alone.
