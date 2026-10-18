# Seeing the whole project at once: a level-0 map for agents

**Serves:** research PLAY-dClosedLoop-1

The owner asked, once the systems and retrofit audit was folded, how an agent stays oriented in the whole
design, and whether a whole-project view is needed. This record holds the question, what orients an agent
today, the audit's items sorted by cause, a size probe, the assessment and the forks.

## [words] The owner's words, 2026-10-17

> Now that even this plan has grown to a substantial size, how do you stay oriented in the entirety of it at high level (to make sure no piece of it is lost at a glance)? As in, when a session is opened, as a question is asked, do you have an overview of the ENTIRE design, then dig deeper into specific parts of it? Previously, codebase map tool was supposed to do exactly that - allow an agent to load the entire project at a high level, so no piece of it is left out. After, an agent would dig deeper into the parts it needs and still be able to find all relations at any point. Is this even needed? Feels like an essential piece to memory layer.

The owner said the same of the codebase map in the memory round: its "purpose is to speed up codebase
orientations and see all relations at a glance" (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`
`[words]`).

## [today] What orients an agent today, measured 2026-10-17

- **A session loads the charter and its build's card.** The card is build-scoped: the task, the scope,
  a read list, the records and the bug classes. After a compaction, the session also holds a summary of
  what it was doing.
- **The card's read list names whole records.** This build's list includes its session log, 269 KB. So
  a session reads slices by grep, and finds only what it already knows to look for.
- **The design is large.** The build folder holds 100 records, 3.72 MB of text, and 31 review reports.
  v2 alone is 127 KB, and the gap register is 89 KB.
- **The code has a high-level view, and nothing loads it.**
  - The codebase map renders `memory/map/generated/MAP.md`, 19.7 KB: an inventory of every moving part
    with its claimant.
  - It also renders `memory/map/generated/CARDS.md`, 22.4 KB: one card of at most 1 KB per feature, for
    31 features.
  - No skill, hook, guide or charter line names either file. AGENTS.md sends a reader to one feature's
    dossier.
- **The design has no such view for agents.** The atlas derives one for the owner: 132 records, 2,307
  sections and 157 decision sections. It is a 6.8 MB page that no agent reads.
- **The settled rule keeps it so.**
  - layer-memory `[views]` says: "Agents never read a view to work: their work orders hand them fields."
  - The orientation scout is the one exception, and it reads one build's README.
  - The codebase map is one of memory's optional components, which P28 governs (v2).
- **That rule rests on over-reading, measured in the memory round.**
  - 96.4% of reads go past a build's README, and 77.9% never read it.
  - An id grep returns a median of 15.5 files.
  - Summaries drop identifiers, and recall's read-through is under 6% (systems `[agree-memory-structure]`).
  - None of these measures what a reader misses.
- **What an agent can do instead is query.**
  - `record find` returns at most 40 rows, and `record show` returns one section.
  - `gov tag show`, `where` and `refs` are designed, and not yet built.
  - The house index is handed to the reuse scout alone.
  - A query returns only what its asker thought to ask for.

## [sort] The audit's items, sorted by cause

Each of the 52 items of the systems and retrofit audit
(`reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md`) is sorted by one question: did the
defect need a piece that its author did not have in view?

| Cause | Items | Count |
|---|---|---|
| a part that already existed elsewhere, in the tree or in another record, was not in view | H1, H3, H4, M14, M15, M16, M18, M19, M20, M21, M24, M25, M26, M27, M28, M33, M35, L6, L8, L10 | 20 |
| a fact stated in two places was changed in one | M1, M4, M5, M6, M7, M8, M22, M29, M31, L1, L2, L3, L7, L9 | 14 |
| who builds what, and in which order | M2, M3, M10 | 3 |
| a mechanism, rule or measure was genuinely missing | H2, H5, M9, M11, M12, M13, M17, M23, M30, M32, M34, M36, L4, L5, L11 | 15 |

- **37 of the 52 items fall in the first three rows.**
- **Who wrote them.** Every one was written by a session that held the card, a summary and grep, and no
  whole view.
- **Who sorted them.** The sort is one reader's: the author's, of records the author wrote. A second
  rater would test it.

## [probe] A level-0 map of gov, sized

A one-line-per-node map, built only from sources that exist today, shows what an agent would load to see
all of gov at once:

```python
"""Size probe for a level-0 project map: one line per node, built only from sources that exist today, so
the bytes an agent would load to see all of gov at once can be read rather than guessed.

Usage: python proto_l0.py [--print]   (from the worktree root)
Nodes, each one line with its tag, its declared purpose cut at 100 characters, and its counts:
- layers, from v2's [layers] table;
- principles, from v2's `**Pn Title.**` bullets;
- chain builds, from v2's [chain] rows: stage, parents and the count of gaps each owns;
- live builds, from memory/LIVE.md's table;
- features, from the codebase map's CARDS.md: each card's heading and its first prose line;
- policy namespaces, from v2's [policies] keys, each with its key count;
- gap areas, from the register's rows, each with its gap count.
It is a size probe, not the design: a real map would be derived from the one index. Prints the bytes per
node class and in all, and with --print the map itself.
"""
import collections
import re
import sys

B = "memory/builds/dClosedLoop/build/"
V = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
G = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md", encoding="utf-8").read()
LIVE = open("memory/LIVE.md", encoding="utf-8").read()
CARDS = open("memory/map/generated/CARDS.md", encoding="utf-8").read()


def section(text, tag):
    m = re.search(r"^## \[" + re.escape(tag) + r"\].*?(?=^## \[|\Z)", text, flags=re.M | re.S)
    return m.group(0) if m else ""


def cut(s, n=100):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n - 1] + "…"


lines = collections.defaultdict(list)
for m in re.finditer(r"^\| `([a-z]+)` \| (core|expansion) \| (.+?) \|$", section(V, "layers"), re.M):
    lines["layers"].append(f"- layer {m.group(1)} — {m.group(2)} · {cut(m.group(3))}")
for m in re.finditer(r"^- \*\*(P\d+) ([^*]+?)\*\*", V, re.M):
    lines["principles"].append(f"- {m.group(1)} — {cut(m.group(2))}")
for ln in section(V, "chain").splitlines():
    if ln.startswith("| d"):
        c = [x.strip() for x in ln.strip().strip("|").split(" | ")]
        gaps = len(re.findall(r"gap-[a-z]+-\d+", c[-1]))
        lines["chain builds"].append(f"- build {c[0]} — {c[1]} · after {c[2]} · gaps {gaps}")
for ln in LIVE.splitlines():
    if ln.startswith("| [") or (ln.startswith("| ") and not ln.startswith(("| Build", "|---"))):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        slug = re.sub(r"[\[\]`]|\(.*?\)", "", c[0]).strip()
        lines["live builds"].append(f"- live {slug} — {cut(c[1], 40)} · node {c[2]} · ids {c[5]}")
for m in re.finditer(r"^## (\S+)\n\n(.+)$", CARDS, re.M):
    lines["features"].append(f"- feature {m.group(1)} — {cut(m.group(2))}")
ns = collections.Counter(re.findall(r"^\| `([a-z]+)\.", section(V, "policies"), re.M))
for n, k in ns.most_common():
    lines["policy namespaces"].append(f"- policy {n}.* — {k} keys")
areas = collections.Counter(re.findall(r"^\| gap-([a-z]+)-\d+ ", G, re.M))
for a, k in areas.most_common():
    lines["gap areas"].append(f"- gaps {a} — {k}")

total = 0
for cls, ls in lines.items():
    b = sum(len(x.encode("utf-8")) + 1 for x in ls)
    total += b
    print(f"{cls:18} {len(ls):4} nodes {b:7} B")
print(f"{'all':18} {sum(len(v) for v in lines.values()):4} nodes {total:7} B")
if "--print" in sys.argv:
    for cls, ls in lines.items():
        print(f"\n## {cls}\n" + "\n".join(ls))
```

```text
$ python proto_l0.py --print
layers                8 nodes     970 B
principles           30 nodes    1417 B
chain builds         15 nodes    1238 B
live builds          25 nodes    1350 B
features             31 nodes    3626 B
policy namespaces    50 nodes    1484 B
gap areas            17 nodes     326 B
all                 176 nodes   10411 B

## layers
- layer instruction — core · everything an agent is told, levelled 0 to 7 and tagged by scope
- layer flow — core · a build's lifecycle: Plan, Design, Build, Test and Deploy as programs of items, review as breakpoin…
- layer roles — core · the bound workers, and the driver
- layer memory — core · the trail, what happened in a build: records, transitions, witnesses, the card's truth; and the lib…
- layer runtime — core · what executes the cycle: the supervisor and its checklist engine, act sessions and the spawn harnes…
- layer observability — expansion · signals about the loop and the runtime, read and filed but never deciding a position, and the caden…
- layer integrations — expansion · adapters to outside services, each registered at the core point it serves under one header: remote …
- layer distribution — expansion · the product's delivery across a repository boundary: govkit's install by copy at a release tag and …

## principles
- P1 — One loop, declared once.
- P2 — Witnessed hand-offs.
- P3 — Local-first verdict.
- P4 — One contract, two authorizations.
- P5 — Concurrency by lease, inside the flow.
- P6 — Maintain closes the loop, as an expansion.
- P7 — Review at breakpoints.
- P8 — Every adopter is an adopter, gov included.
- P9 — Measured weight.
- P10 — Flexible and configurable.
- P11 — Everything loaded gives direction.
- P12 — Specs are structured contracts.
- P17 — Features carry the design between units.
- P18 — Decision principles outrank practices in unattended forks.
- P19 — Built work is never rewritten in place.
- P20 — The flow is the layer above the build.
- P21 — Builds coordinate before they wait.
- P22 — Position is derived, never remembered.
- P23 — Claims are trusted by key and source.
- P24 — The checklist is a program.
- P25 — Role functions live only in role agents.
- P26 — Every exchange between roles is a typed record.
- P13 — Levelled, tagged instructions.
- P14 — Practices with reach.
- P15 — The charter starts the loop; the tools continue it.
- P16 — The core cannot be built around.
- P27 — Load is precise.
- P28 — Layers are capabilities, and the core never depends on an expansion.
- P29 — A role acts on what it is handed, and verifies only what its job is to verify.
- P30 — Memory is declared once and written through one door.

## chain builds
- build dOrderedCharter — Foundation · after dClosedLoop · gaps 21
- build dFairHearing — Review harness · after dClosedLoop · gaps 4
- build dDeclaredLoop — Spine · after dOrderedCharter, dFairHearing · gaps 19
- build dBoundRoles — Roles · after dDeclaredLoop, dWitnessedBar · gaps 22
- build dTotalRecall — Memory · after dDeclaredLoop, dWitnessedBar · gaps 24
- build dMindYourWords — Lexicon · after dWellOiledMachine, dWitnessedBar · gaps 9
- build dWellOiledMachine — Runtime · after dBoundRoles, dTotalRecall · gaps 9
- build dWitnessedBar — Test · after dDeclaredLoop · gaps 19
- build dRankedPlan — Plan · after dDeclaredLoop, dTotalRecall · gaps 10
- build dIndexedDesign — Design · after dDeclaredLoop · gaps 9
- build dScopedBuild — Build · after dIndexedDesign, dWitnessedBar, dWellOiledMachine · gaps 7
- build dShippedRelease — Deploy · after dWitnessedBar, dTotalRecall · gaps 16
- build dTendedCadence — Maintain · after dWitnessedBar, dRankedPlan, dWellOiledMachine · gaps 10
- build dCalibratedLens — Review · after dTendedCadence, dFairHearing · gaps 9
- build dConvergedCharter — Convergence · after dScopedBuild, dShippedRelease, dCalibratedLens · gaps 7

## live builds
- live aOrientedCast — OPEN · node a · ids 33
- live aRoutedQuill — DEFERRED · node a · ids 15
- live dClosedLoop — OPEN · node d · ids 1
- live dPinnedHandoff — SPECCED · node d · ids 3
- live aBatchedLintel — INPROGRESS · node a · ids 2
- live aDeclaredBound — OPEN · node a · ids 6
- live aDeployScout — SPECCED · node a · ids 1
- live aFerriedDossier — OPEN · node a · ids 3
- live aGradedDoorway — INPROGRESS · node a · ids 10
- live aMendedLedger — SPECCED · node a · ids 9
- live aPacedTurnstile — SPECCED · node a · ids 16
- live aPortableWarden — SPECCED · node a · ids 1
- live aQuarriedLantern — INPROGRESS · node a · ids 3
- live aTetheredScratch — INPROGRESS · node a · ids 4
- live aTunedCompass — BLOCKED · node a · ids 11
- live aWalkedCorpus — DEFERRED · node a · ids 10
- live aWeighedCanon — OPEN · node a · ids 2
- live bConvergentLodestar — SPECCED · node b · ids 1
- live dLandedVerdict — INPROGRESS · node d · ids 2
- live dNarrowedAnchor — INPROGRESS · node d · ids 3
- live dPolishedVitrine — INPROGRESS · node d · ids 19
- live dPromptedSeam — DEFERRED · node d · ids 4
- live dRetiredFork — DEFERRED · node d · ids 56
- live dScaffoldedMirror — DEFERRED · node d · ids 22
- live dScriptedRepeat — SPECCED · node d · ids 15

## features
- feature agent-cap — PreToolUse guards — fan-out bounded across Workflow+Agent, scratch bounded across Bash+PowerShell
- feature annotation-style — Annotation style: what a code comment citing a governance record must carry
- feature branch-reconcile — One read-only report giving every worktree, branch and stash entry a verdict with its evidence, so …
- feature build-method — The build method: how to spec, review and build, rendered from the memory-tree kit
- feature build-readme-surface — A build README is mostly generated, and its authored slots are positional and named
- feature codebase-map — Codebase map — CI-verified inventory claims + the reuse recall index
- feature gate-lint — Three scanners for the failure modes a reader cannot see: PowerShell's decoding traps, a shell loop…
- feature govkit — govkit — a declared kit population, and the selfcheck that keeps it honest
- feature install-prefix — dead paths in shipped text — the wrong-prefix half and the deleted-file half, and the two gates tha…
- feature kit-placeholders — The join from a descriptor's declared placeholders to its adopter's substitutions
- feature lexicon — Naming predicates over a per-repo DECLARATION — a closed verb table, a banned-suffix list and a set…
- feature memory-recall — Conf-driven retrieval over the memory tree, and a merge-bar floor over a committed question set
- feature memory-tree-backlog — The backlog in both modes: authored family shards, or asks filed per build with generated family vi…
- feature memory-tree-hygiene — check-memory-hygiene.sh: the memory tree's structural gate, its per-class size caps, and the epoch …
- feature memory-tree-merge-driver — Row-keyed merge driver for the authored indexes and each build's BACKLOG.md, and its view-against-s…
- feature playbook — The governance playbook — the shipped template + companions, and the gates over their claims
- feature playbook-mode — A third authorization mode for repeatable content, and the playbook it follows
- feature process-monitor — identify, report and kill the processes an agent session launched and forgot
- feature push-main — the lander that reconciles, gates and pushes the default branch, and the pre-push hook that refuses…
- feature review-harnesses — Workflow review harnesses — one pipeline, three implementations, one hardened
- feature roles — The role catalogue: one owner-editable agent definition per role with an empty house overlay beside…
- feature row-grammar — Check 20: id collisions inside a single row document
- feature run-gates — The gate runner, its harnesses, and the adopter that keeps a target's verdict reader honest
- feature run-gates-turnstile — The host turnstile: the slots that admit gate bars, the docs key beside them, and the files two con…
- feature runlog — The line grammar the three run-log producers write, the one reader every consumer parses them throu…
- feature session-kickoff — the /session-kickoff engine, its project manifest, and the ratchet that keeps the manifest true
- feature spec-tokens — Seven joins that resolve a live spec's leg names, witness paths and line citations, refuse a bar in…
- feature testsuite-counts — Executed assertion counts, in one shape, against a shrink-only floor
- feature unattended — Unattended runs — a mandate on disk, not a block of chat
- feature unattended-mandate — The unattended run's authorization: the observed anchor and the ask mandate
- feature unattended-stops — The unattended run's stops: HELD, the lease and the process ledger

## policy namespaces
- policy review.* — 20 keys
- policy runtime.* — 11 keys
- policy retrofit.* — 11 keys
- policy maintain.* — 10 keys
- policy roles.* — 8 keys
- policy verdict.* — 8 keys
- policy instructions.* — 6 keys
- policy memory.* — 6 keys
- policy leases.* — 5 keys
- policy deps.* — 5 keys
- policy annotations.* — 5 keys
- policy lexicon.* — 5 keys
- policy plan.* — 5 keys
- policy build.* — 5 keys
- policy design.* — 4 keys
- policy card.* — 4 keys
- policy builds.* — 4 keys
- policy deploy.* — 4 keys
- policy tags.* — 4 keys
- policy policy.* — 3 keys
- policy tests.* — 3 keys
- policy kits.* — 3 keys
- policy charter.* — 2 keys
- policy core.* — 2 keys
- policy resume.* — 2 keys
- policy prompts.* — 2 keys
- policy reuse.* — 2 keys
- policy run.* — 2 keys
- policy notify.* — 2 keys
- policy context.* — 2 keys
- policy currency.* — 2 keys
- policy hooks.* — 1 keys
- policy transitions.* — 1 keys
- policy landing.* — 1 keys
- policy placement.* — 1 keys
- policy kickoff.* — 1 keys
- policy actions.* — 1 keys
- policy orient.* — 1 keys
- policy driver.* — 1 keys
- policy asks.* — 1 keys
- policy decisions.* — 1 keys
- policy mailbox.* — 1 keys
- policy notices.* — 1 keys
- policy flow.* — 1 keys
- policy install.* — 1 keys
- policy release.* — 1 keys
- policy integrations.* — 1 keys
- policy observability.* — 1 keys
- policy patch.* — 1 keys
- policy budgets.* — 1 keys

## gap areas
- gaps mem — 25
- gaps found — 23
- gaps rt — 21
- gaps roles — 20
- gaps test — 17
- gaps flow — 15
- gaps orient — 14
- gaps deploy — 13
- gaps review — 13
- gaps maint — 11
- gaps design — 10
- gaps lex — 8
- gaps tool — 7
- gaps spine — 7
- gaps plan — 7
- gaps build — 5
- gaps conc — 3
```

- **The size.** 176 nodes in 10.4 KB: 8 layers, 30 principles, 15 chain builds, 25 live builds, 31
  features, 50 policy namespaces and 17 gap areas.
- **Against today's reads.** That is about a fifth of today's median memory read per agent, 57.2 KB
  counted over every channel (systems `[ms2-instrument]`, its third run).
- **What it lacks.**
  - The record kinds, the major decisions that hold now, and this build's 100 records.
  - A purpose line for each live build. `memory/LIVE.md` holds none, so the probe shows a build's status
    where its purpose belongs.
  - Corrected 2026-10-17: both research runs found every build README declaring its purpose in its
    H1, after the slug. `LIVE.md` was the wrong source (`[agreement]`).
- **Its principle parse is loose.** It reads only the `**Pn Title.**` bullets, so a principle written
  another way is missed. It is a size probe, not the map.

## [assessment] Is it needed

- **Yes, for the roles that change structure.**
  - Those roles are orienting a session, planning, architecture, writing a spec, and reviewing for
    coherence or reuse.
  - Each of them asks what else exists, and their defects are the 37 above.
  - A query cannot answer that, since it finds only what its asker names.
- **No, for workers inside a unit.** A builder or a tester is well served by its slice and `refs`.
  Handing it the whole would bring back the over-reading the memory round measured.
- **It is an index, not a summary.** Each line keeps its tag, so the research's case against summaries,
  which drop identifiers, does not apply.
- **The shape exists for code.** CARDS.md is one derived card per feature. The design side has no
  counterpart for agents, and the atlas derives one only for the owner.
- **Drill-down and relations are designed already.** `gov tag show` returns a node's subtree, and
  `gov tag refs` every inbound reference, once dOrderedCharter builds the resolver.
- **It changes three settled things, so it is asked, not folded:**
  - layer-memory `[views]`' rule that agents never read a view;
  - P27, since the map becomes a declared unit of those roles' load sets;
  - the codebase map's optional status, for the level-0 part, which the core would derive from the one
    index.
- **Its losing test.**
  - Replay a design round's records twice: once with the map handed to its authoring and reviewing
    roles, and once without.
  - If the share of items "not in view" does not fall, the map is retired.

## [forks] To put to the owner

| Fork | The question | Options, the recommendation first |
|---|---|---|
| PM-1 | Who sees the whole project at once? | the orienting and structural roles: the orientation scout composes the card from the map, and planners, architects, spec writers and the coherence and reuse lenses get it in their work orders, while unit workers keep their slice; every agent; the owner only, as today |
| PM-2 | Where does the level-0 map live? | core memory, derived from the one index over every registered namespace, with the codebase map adding code depth where it is installed; the codebase map, so there is no map where the kit is absent |
| PM-3 | How is it designed? | as a seventh system, with two research runs like the other six; directly from this record; not now |

## [answers] The owner's answers, 2026-10-17

The three forks were asked in one round, through the question tool. Each answer is quoted verbatim.

| Fork | The owner's answer | What it settles |
|---|---|---|
| PM-1 | "Structural roles (Recommended)" | a policy, `memory.project-map`: by default the orientation scout composes the card from the map, and planners, architects, spec writers and the coherence and reuse lenses get it in their work orders, while unit workers keep their slice and `refs`. `every-role` and `owner-only` are its other allowed values |
| PM-2 | "Core memory (Recommended)" | the core derives the map from the one index over every registered namespace. The codebase map adds code depth where it is installed |
| PM-3 | "Research twice, then design (Recommended)" | a seventh system round: one handoff run twice, then the design and its forks |

- **What PM-1 amends.** It amends layer-memory `[views]`' rule that agents never read a view. The view
  is the map, and only the roles PM-1 names receive it.
- **When the key lands.** It joins v2's catalogue at the design's fold, with the budget and tier keys
  the design adds.

## [research] Dispatched, 2026-10-17

- **The method** is the retrofit round's. One handoff, `prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-2-researcher.md`, runs twice at the researcher's
  declared effort, medium, as dispatches 87 and 88. The design is based on what the two runs agree on.
- **The handoff** shares the systems round's handed facts, way of working and return shape. It differs
  in three places:
  - its context, which quotes the owner's words above;
  - its part, which hands PM-1 and PM-2 as settled, asks the researcher to re-sort two other reviews'
    items as a second rater of `[sort]`, and asks for the map's losing test;
  - the return shape's third section, which asks across the six systems.

  The script below assembles it, `handoff.py render` renders it, and `handoff.py check` passes it.
- **The returns** are filed verbatim as `build/2026-10-17-build-PLAY-dClosedLoop-1-research-project-map-<run>.md`.

### [instrument] The script that assembles the question

```python
"""Assemble the project map's research question from the systems round's shared blocks and its own part, for
the system the owner opened on 2026-10-17, then render and check its handoff.

Usage: python assemble_project_map.py <dir> <systems-dir>   (from the worktree root)
Writes <dir>/question-project-map.md, renders the handoff with handoff.py into the build's prompts/
folder, writes the spawn prompt (the marker line, a blank line and the Task section) to <dir>/prompt-28.txt,
and runs handoff.py check on the rendered file. The handed facts, the way of working and the return shape
are the systems round's, so this question differs from the retrofit's only in its context, its part, and
the return shape's third section, which asks across the six systems.
"""
import pathlib
import subprocess
import sys

d, sysd = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
head = (sysd / "head-expansions.md").read_text(encoding="utf-8").rstrip("\n") + "\n" + \
    (sysd / "head-more.md").read_text(encoding="utf-8")
tail = (sysd / "shared-tail.md").read_text(encoding="utf-8")
old = "   it; then what it needs from, and gives to, the other four systems.\n"
if tail.count(old) != 1:
    sys.exit("the return shape's third section has moved")
tail = tail.replace(old, "   it; then what it needs from, and gives to, each of the six systems the rounds designed.\n")
CONTEXT = (
    "**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development.\n"
    "The owner reviews the design layer by layer. All eight layers, the five core and the three expansions,\n"
    "are designed, reviewed and folded. Six systems that cut across every layer were then researched,\n"
    "designed, audited and folded: tags, code annotations, instruction writing, role workflow shapes, memory\n"
    "structure, and retrofitting gov's practices into an existing repository. The owner now asks, in these\n"
    "words:\n\n"
    "> Now that even this plan has grown to a substantial size, how do you stay oriented in the entirety of\n"
    "> it at high level (to make sure no piece of it is lost at a glance)? As in, when a session is opened,\n"
    "> as a question is asked, do you have an overview of the ENTIRE design, then dig deeper into specific\n"
    "> parts of it? Previously, codebase map tool was supposed to do exactly that - allow an agent to load\n"
    "> the entire project at a high level, so no piece of it is left out. After, an agent would dig deeper\n"
    "> into the parts it needs and still be able to find all relations at any point. Is this even needed?\n"
    "> Feels like an essential piece to memory layer.\n\n"
    "The owner then settled PM-1 and PM-2, handed below, and asked for this system to be researched twice,\n"
    "then designed. Yours is **the level-0 project map**. Design it to fit the architecture handed below,\n"
    "across all eight layers and the six systems. Measure what today's product does, say what the current\n"
    "design already settles and what it lacks, and say what makes your pick efficient, in numbers a check\n"
    "could hold it to.\n")
part = (d / "part-project-map.md").read_text(encoding="utf-8")
text = "\n".join([CONTEXT, head, part, tail]).rstrip("\n") + "\n"
if "\r" in text:
    sys.exit("a carriage return reached the question")
(d / "question-project-map.md").write_text(text, encoding="utf-8", newline="\n")
print(f"question-project-map.md: {len(text.split())} words, {len(text.encode('utf-8'))} bytes")

r = subprocess.run([sys.executable, "tools/roles/handoff.py", "render", "--role", "gov-researcher",
                    "--build", "dClosedLoop", "--unit", "PLAY-dClosedLoop-1", "--input", "question=" + text,
                    "--part", "task"], capture_output=True)
sys.stderr.write(r.stderr.decode("utf-8"))
if r.returncode:
    sys.exit(f"render exited {r.returncode}")
task = r.stdout.decode("utf-8")
(d / "prompt-28.txt").write_bytes(task.encode("utf-8"))
marker = task.split("\n", 1)[0]
path = marker.split(" path=", 1)[1].split(" ", 1)[0]
print(f"rendered {path}")
c = subprocess.run([sys.executable, "tools/roles/handoff.py", "check", path], capture_output=True)
print(c.stdout.decode("utf-8") + c.stderr.decode("utf-8"), end="")
sys.exit(c.returncode)
```

## [agreement] What the two runs agree on

Run A beside run B, question by question. "Both runs" holds only what each run found on its own, with
each run's line cited. The returns are filed verbatim as `research-project-map-a.md` and `-b.md` in
`build/`. A finding one run alone made, and that this record checked, says "verified" where the design
takes it.

### [agree-project-map] The level-0 project map, dispatches 87 and 88

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| Owner | core memory, kit memory-tree, chain build dTotalRecall (`research-project-map-a.md:159`, `research-project-map-b.md:148`) | — | both |
| The mechanism | a tiered map derived from the one index: a structural node gets one line, and a large population folds to one counted line with its drill verb (`research-project-map-a.md:17`, `research-project-map-b.md:15`) | A pushes a namespace's roll call to the items that declare it (`research-project-map-a.md:196`). B pulls one namespace on demand with `gov map <ns>` (`research-project-map-b.md:17`) | both: item-declared unfolds, and the pull verb (fork PM-6) |
| Its size today | about 13 to 14 KB: A's base is 13.7 KB (`research-project-map-a.md:19`), B's tier 0 is 173 lines in 13.2 KB (`research-project-map-b.md:16`) | A adds the namespaces the design declares and the index does not yet derive, for about 19 KB | about 19 KB once the designed namespaces land |
| A flat map | loses: one line for every node is far over any slot (`research-project-map-a.md:116`, `research-project-map-b.md:131`), and grows about 20 KB a month (`research-project-map-b.md:100`) | A counts 1,589 nodes at 123.8 KB, B 1,057 at 81 KB with 60-character purposes | rejected |
| Query alone | loses: structural agents already search for existence often, and most audit items were still not in view (`research-project-map-a.md:119`, `research-project-map-b.md:133`) | — | rejected; the verbs stay as the drill-down and the replay's control arm |
| Extending the codebase map | loses: the kit is optional, so the core map cannot live in it (`research-project-map-a.md:120`, `research-project-map-b.md:134`) | A finds the kit in govkit's default install, while its README calls it opt-in (`research-project-map-a.md:39`) | rejected; code depth is an optional slot. A's finding is verified: `tools/govkit/registry.toml` lists `codebase-map` in `default` |
| Declared purposes | many node classes declare none, kits among them (`research-project-map-a.md:43`, `research-project-map-b.md:46`) | A adds config keys, populations, items and design records; B adds workflow scripts, chain builds and gap areas | a purpose source per namespace, and the nodes without one held on the ledger (fork PM-5) |
| A build's purpose | every build README declares one in its H1, after the slug (`research-project-map-a.md:41`, `research-project-map-b.md:44`) | — | the H1 is a build's purpose source. `[probe]` read `memory/LIVE.md`, the wrong source |
| Delivery | the orientation scout composes the card's map cells from the map within 8 KB, structural roles get it in their work orders, and unit workers keep `refs` (`research-project-map-a.md:151`, `research-project-map-b.md:174`) | B finds the orientation scout never spawned (`research-project-map-b.md:33`). A asks what the attended main session loads (`research-project-map-a.md:218`) | both. B's finding is verified: 0 of 3,283 recorded subagents is a gov-orienter. The main session is fork PM-7 |
| The owner's view | the atlas is the owner's render of the same derivation (`research-project-map-a.md:22`, `research-project-map-b.md:20`) | — | both |
| No piece lost | a both-ways completeness check over the index and the map (`research-project-map-a.md:170`, `research-project-map-b.md:184`) | A also joins the disk census, through `compute_coverage` | A's three ways |
| The record's sort | it holds: A agrees on 49 of 52, κ 0.85 (`research-project-map-a.md:66`), and B on 50 of 52, κ 0.90 (`research-project-map-b.md:82`) | — | the sort stands |
| Two more reviews | the library review had 14 of 19 items not in view, in each run's rating (`research-project-map-a.md:62`, `research-project-map-b.md:80`) | the debt folds' review: A 16 of 20, B 17 of 20 | about three items in four were not in view |
| What a map would catch | about half to two-thirds of the items a part elsewhere caused: A 12 of 22 with unfolds (`research-project-map-a.md:109`), B about 13 of 20 (`research-project-map-b.md:87`) | A's base map alone names 5 of 22 | the unfolds carry most of the catch |
| Reads before a first act | structural roles read a median of 98 to 241 KB before acting (`research-project-map-a.md:50`, `research-project-map-b.md:69`) | — | the map adds 7 to 13% to that |
| The losing test | a replay with the map handed and without, scored on the share not in view (`research-project-map-a.md:223`, `research-project-map-b.md:200`) | A adds a cause computed at `review.dispose`, read continuously. B runs the replay before the build, at dTotalRecall's first unit | both |
| The new gap | no whole-project view reaches an agent, `gap-mem-26` (`research-project-map-a.md:203`, `research-project-map-b.md:233`) | — | registered at the fold |
| Kit descriptors | govkit and lib carry no `kit.toml` (`research-project-map-a.md:40`, `research-project-map-b.md:239`) | — | the kit factory's purpose field covers both |
| The budget | — | A 24k (`research-project-map-a.md:194`), B 16k (`research-project-map-b.md:217`) | fork PM-4 |

## [cross] Where the map meets the six systems

- **Tags.** Each namespace row gains `purpose-source` and `owner` (dOrderedCharter). The completeness
  check joins every registered namespace, so a namespace with no extractor or owner reds, which would
  have caught the audit's M10.
- **Annotations.** `gov:feature` anchors are counted on each feature's line. The `marker` namespace
  folds to one counted line.
- **Instruction writing.** A map line is a derived fact or a pointer (P11), never authored. A purpose
  that is a unit's is written through `instructions.edit`.
- **Role shapes.** An item declares its map slot and its unfolds. A shape-run row carries the map's
  bytes.
- **Memory structure.** The map is its own work-order slot, with its own budget and its own answer
  when it runs over, outside `memory.item-budget`, as the audit's M1 settled for every slot.
  layer-memory `[views]` carries PM-1.
- **Retrofit.** The nodes that declare no purpose are a ledger population, shrink-only, drained by
  each namespace's owning build. A population's count is a line the map shows.

## [design] The design

### [placement] Where it sits

- **Core memory** (PM-2): kit memory-tree, chain build dTotalRecall.
- **A view, not a record kind.** It is derived from the one index, never committed, and cached beside
  the index at `<git-common-dir>/gov/index/<tree>.map`.
- **Code depth is core** (revised 2026-10-18, the night pass, point 3). dTotalRecall's `code` record fills each
  item's `code` slot with its seed's neighbourhood, and level 0 holds one counted `code` line, never a line per file.
  The slot renders filled, derived with nothing related, not extracted for a language, with `gov code where`
  named as the fallback, or not installed, until dTotalRecall's `code` record lands (the closing review's L2). The map's owner views and the dossier's prose stay optional.

### [line] One line per node

```text
line   := "- " <key> [" — " <purpose>] [" · " <count> {", " <count>}] [" · " <rel> {" " <rel>}]
key    := <ns> "." <id> where the node has a native id, such as "chain.dTotalRecall"; its tag otherwise
purpose:= at most 60 characters, verbatim from the namespace's declared purpose source
count  := <noun> " " (<int> | "?"), derived from the index, such as "gaps 21" or "items 12"
rel    := ("layer" | "owner" | "after" | "implements") "=" (<key> {"," <key>} | "?"), at most three keys
nsline := "- " <ns> ".* — " <int> " nodes · gov map " <ns>
header := "map " <tree-id> " · nodes " <int> " · lines " <int> " · folded " <ns> {"," <ns>}
          [" · pending " <int>] [" · unowned " <int>] [" · unarmed " <ns> {"," <ns>}]
```

- **A node with no purpose** renders `—` in its place.
- **A required field that is missing renders `?`** (revised 2026-10-17, `[fixes]`):
  - `owner=?` on a node a build must build, or `items ?` on a core item role that acts in no item;
  - the header counts the missing owners as `unowned`;
  - a field the node does not require is omitted, so an omitted field is never a finding, and a `?`
    always is.
- **A line reads declared fields only** (PM-8). The renderer infers no relation: no owner from a
  stage, from a literal or from a default. The owners of a step, a system and a namespace are derived
  from their members' declared owners, so a step can have several.
- **The key is the native id where one exists** (PM-11), as for chain builds, live and closed builds,
  principles and gaps: the ids agents already search for. The resolver accepts both forms. Where a
  native id is not unique, as a decision row's is today, the row's key stays open (`[fixes-concept]`,
  6).
- **A line never holds:**
  - section content;
  - dates or ages;
  - typed status words. The only status allowed is one the index derives, such as a live build's.
  - line numbers, summaries, render provenance or judgments.

### [tiers] What an agent holds, and how it digs

- **The map, level 0.**
  - It opens with the header.
  - Then come the bounded namespaces, one line per node, in a declared order: layer, principle,
    chain build, step, role, feature, kit, live build, point, hook, record kind, tag namespace,
    policy namespace, gap area.
  - Then comes one counted line per unbounded namespace: legs, bug classes, closed builds, decision
    rows, gaps, config keys, populations, markers, items and design records.
  - A namespace's registry row says which it is, `map: line` or `map: fold`. A row that says neither
    folds past 40 nodes.
- **Unfolds.** An item declares the namespaces whose roll call it needs. Its work order's map slot
  then lists those namespaces node by node, as `memory.map-unfold` says (fork PM-6).
  - `design.inventory` unfolds legs, checks, config keys, populations, markers and kits, which costs
    12.3 KB.
  - In run A's hit test, the base map named 5 of 22 audit items a missing part caused, and the
    architect's unfolds named 12.
- **The pull, level 1.** `gov map <ns>[.<seg>]` returns one namespace in the same grammar, for an
  agent that knows which namespace it needs.
- **Content, level 2.** `gov tag show <tag>` or `record show <id>#<tag>`.
- **Relations, both ways.** Outbound relations are the line's own keys, and `gov tag refs <tag>`
  returns the inbound ones.

### [fit] Over its budget, no node is dropped

- **Under `memory.map-overflow: degrade`,** the default, the map degrades in a fixed order:
  1. Purposes are cut to 40 characters.
  2. The lowest-ordered bounded namespaces fold to their counted lines, one at a time, until the map
     fits.

  The header names each step it took.
- **Under `refuse`,** a map over its budget is refused at render, as strict may want.
- **Either way, every node stays on the map,** as a line or inside a count.

### [delivery] Who receives it

| Reader | What it receives, under `memory.project-map: structural-roles` (PM-1) |
|---|---|
| the orientation scout, at `entry.orient` | the whole map. It composes the card's map cell from it within the card's 8 KB: the header, and the build's neighbourhood, which is its layer, its chain build's line, its features, its gap areas and the live builds that overlap its write set |
| the planner, at `plan.triage-judge` and `plan.reason` | the map, as the work order's `map` slot |
| the architect, at `design.inventory`, `design.decompose` and `design.reason` | the map, with `design.inventory`'s unfolds, and the `code` slot of its scope paths (night pass, point 3) |
| the reuse scout, at `design.seams` | the map, inside the house index |
| the spec writer, at `design.unit-spec` and `review.fold` | the map, and the `code` slot of its unit's write set (night pass, point 3) |
| the reviewer, at `review.lens` under the coherence and reuse lenses | the map, and the `code` slot of the pinned range (night pass, point 3) |
| unit workers: the builder, the tester and the rest | no map. They get their slice and the `refs` rows of their write set, and since the night pass the builder and the tester get their write set's `code` slot (point 3). A `gov map` call from one is journaled as a read outside its slice |
| the researcher, at `plan.research` and `design.research` | the map, and the `code` slot of its question's paths (night pass, point 3) |
| the prompt writer | its actor's `map` and `code` slots, through the work order it frames (night pass, point 3) |
| the owner's session | the card and the whole map when it opens, and again at a resume and a compaction, under `memory.default-load: card-and-map` (PM-7; night pass, point 5) |

- **The slot.** dBoundRoles declares the `map` slot in the work order, beside `reuse`
  (`tools/roles/handoff.py:97`), and dTotalRecall's renderer fills it. The slot is hashed with the
  work order.
- **Until the renderer lands,** the slot renders "not installed".
- **The scout has never run.** The card today is written by a command, and 0 of 3,283 recorded
  subagents is an orientation scout. dBoundRoles builds the scout, so PM-1's card cell lands with it.

### [purpose] Where each node's purpose comes from

Each namespace row declares its purpose source (dOrderedCharter adds the field). Where a source exists
today, the map reads it. Where none exists, the namespace's owning build adds one.

| Namespace | Its purpose source | Today |
|---|---|---|
| layer | v2 `[layers]`' definition column | declared |
| principle | its title | declared |
| build | the README H1, after the slug | declared, 167 of 167 |
| feature | the dossier's `title` | declared |
| skill, role | the `description` of the skill or the agent file | declared |
| bug class | the gotcha's `description` | declared |
| item | flow-steps' `does` column | declared |
| chain build | its stage word only | a purpose field, dOrderedCharter's chain registry |
| kit | none; govkit and lib carry no `kit.toml` | `purpose` in `kit.toml`, dShippedRelease's kit factory |
| leg | none: the leg has a name only | `purpose` in `gate-legs.json`, dWitnessedBar |
| hook, point | none | `purpose` on the pack and point registrations, dWellOiledMachine |
| record kind | none | `purpose` in the kind registry, dTotalRecall |
| tag namespace, policy namespace, gap area | none | `purpose` on the namespace row, dOrderedCharter; the policy namespace's dDeclaredLoop's, the gap area's dTotalRecall's |
| design record | its H1 | declared |

- **A node with no purpose,** under `memory.map-purpose: review` (PM-5):
  - A new node must declare one. Its registration refuses it otherwise.
  - Each existing node is reviewed by the unit that adds its namespace's purpose field. The unit
    derives the purpose from what the node already carries: its README or H1, its docstring or header
    comment, its doc field, or the record that introduced it. It cites that source in its own
    record.
  - A node that carries nothing to derive from is put to the owner, in one ask per namespace that
    lists each such node with what was found.
  - Until the owner answers, the node renders `—`, and the header counts it as pending.
- **Builds after dTotalRecall.** A namespace whose owning build lands after dTotalRecall, kits and
  hooks among them, renders `—` until then. No chain edge is added for it.

### [checks] The `map` leg pack

| Check | Red on |
|---|---|
| complete, three ways | a planted `tools/newkit/` with no `kit` node, found by the disk census through `compute_coverage`; a planted index node on no line and in no count |
| resolves | a line naming `feature.ghost`, or a relation key whose target resolves nowhere |
| count | a counted line one off from the index's count, planted by an extractor that drops a row |
| owner | a node a build must build with no declared owner, or with two: an item, a policy key, a point, a record kind, a tag namespace or a system (revised 2026-10-17, PM-8); planted, an item whose owner field is emptied |
| extractor | a namespace registered with no extractor, such as `doc` |
| no inference | a relation rendered from no declared field; planted, a namespace whose owner comes from a default |
| purpose | under `required`, a new `kit.toml` with no purpose |
| budget | under `refuse`, a planted map over the budget; under `degrade`, a degraded render whose header omits a step |
| freshness | a work order whose map tree id is not the served index's, outside the rows marked `dirty` |
| delivery | a structural item's work order without the slot, or a unit worker's with it |
| render parity | a node in the atlas that is not on the map, or the reverse |
| no stale facts | a line holding a date or a typed status |
| populated | fewer namespaces present than registered, which reads unarmed, never green |

### [test] Its losing test

- **Before the build.** At dTotalRecall's first unit, a map derived from today's sources is replayed,
  as the runs' size probes derived theirs.
  - **The replay.** The coherence and reuse lenses run twice with the map and the architect's unfolds
    handed, and twice without. They run at the base commits of the systems and retrofit, library and
    debt-folds audits.
  - **The scoring.** `tools/workflows/review_replay.py` scores the runs against the known set of
    those audits' not-in-view items, counting each defect once.
  - **The map loses, and is not built, if any of these holds:**
    - the recall of the known set rises by less than the twin runs' difference plus 5 items;
    - the median of existence searches per lens falls by less than one;
    - the bytes read before the first act rise by more than the map's own bytes.
- **After landing.**
  - `review.dispose` computes each confirmed finding's cause. It is "not in view" when the address
    the finding's fix needs is in neither the author's slice manifest nor the map.
  - The Loop Review reads that share over the next 38 confirmed findings. That is enough to detect a
    fall from 74% to 55%, at α 0.05 and power 0.8.
  - If the share has not fallen by 15 points, the Loop Review proposes setting `memory.project-map` to
    `owner-only`.

### [owners] Owners

| Chain build | Its part |
|---|---|
| dTotalRecall | the renderer and `gov map`; the three-way completeness check and the `map` leg pack; the atlas re-rendered from the same node table; the purposeless-node population; the record-kind registry's purpose and owner fields; the owner and no-inference checks (PM-8); the replay at its first unit |
| dOrderedCharter | the namespace row's `purpose-source` and `owner` fields, the chain registry's purpose field, and the resolver's native-id keys (PM-11) |
| dBoundRoles | the work order's `map` slot and the per-item unfolds; the orientation scout composing the card's map cell |
| dDeclaredLoop | the items' declarations of the slot and their unfolds, the policy namespaces' purposes, and the owner fields of the items and the policy catalogue (PM-8) |
| dWitnessedBar | the leg's purpose field |
| dWellOiledMachine | the hook and point purposes, the points' owner field (PM-8), and the journal's count of map reads outside a slice |
| dShippedRelease | the kit factory's purpose field, and `kit.toml` for govkit and lib |
| dCalibratedLens | the not-in-view cause `review.dispose` computes from the author's slice manifest and the map, and the Loop Review's reading of its share. It descends from dTotalRecall and dBoundRoles, which produce both inputs; dFairHearing, at the chain's root, does not |

### [keys] Keys

| Key | Values | Default |
|---|---|---|
| `memory.project-map` | structural-roles, every-role, owner-only | structural-roles (PM-1) |
| `memory.map-budget` | 16k, 24k, 32k | 32k (PM-4) |
| `memory.map-overflow` | degrade, refuse | degrade |
| `memory.map-unfold` | item-declared, none, all | item-declared (PM-6) |
| `memory.map-purpose` | review, ledger, derive, refuse | review (PM-5) |
| `memory.default-load` | card, card-and-live, card-and-map | card-and-map (PM-7), read by the owner's session at startup, resume and a compaction (night pass, point 5); an act session loads its work order |

## [forks-design] The design's forks, to put to the owner

| Fork | The question | Options, the recommendation first |
|---|---|---|
| PM-4 | What is the map's budget? | 24k, which holds about 19 KB once the designed namespaces land; 16k, which fits today's 13.2 to 13.7 KB and folds as namespaces land; 32k |
| PM-5 | What happens to a node with no declared purpose? | a new node must declare one, and today's purposeless nodes sit on a shrink-only ledger population each owning build drains; the purpose is derived from the node's first comment or README line; the map is refused until every node declares one |
| PM-6 | How does a role see a whole namespace? | each item declares the namespaces it unfolds, pushed into its work order; no unfolds, only the pull verb; every structural role gets every roll call, about 55 KB |
| PM-7 | What does an attended session load when it opens? | the card and the map, about 19 KB more per session start; the card, whose map cell holds the build's neighbourhood and a pointer to `gov map`; the card only |

## [gaps-proposed] Gaps to register once the forks settle

| Gap | Severity | Owner |
|---|---|---|
| no whole-project view reaches an agent: 37 of 52 audit items, and 30 of 39 in two more reviews, needed a piece their author did not have in view; `MAP.md` and `CARDS.md` reach no agent (`research-project-map-a.md:203`, `research-project-map-b.md:233`) | HIGH | dTotalRecall |
| nodes carry no declared purpose: kits, legs, hooks, points, record kinds and the tag and policy namespaces have no purpose field, and govkit and lib no `kit.toml` | MED | dTotalRecall |
| the orientation scout the design relies on has never run: 0 of 3,283 recorded subagents is a gov-orienter, and a command writes today's card | MED | dBoundRoles |

## [instrument-agreement] The citations, and the both-runs probe over `[agreement]`

Every line `[agreement]` cites was read from the filed returns by this helper, never typed. Its two
missing phrases were then found by hand at `research-project-map-a.md:22` and `research-project-map-b.md:33`,
the lines the table cites:

```python
"""Print the line, in each filed project-map return, of each phrase the agreement table cites, so every
citation is read from the record, never typed. Exits 1 when a phrase is missing or matches more than once.

Usage: python cite_lines.py   (from the worktree root)
"""
import sys

B = "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-research-project-map-"
PHRASES = {
    "owner": ("builds the renderer, the check and the atlas re-render", "**Owner.** The memory layer, kit memory-tree"),
    "mechanism": ("a tiered map that folds to fit", "two-tier project map that core memory derives"),
    "size": ("The base map is 13.7 KB today", "Today that is 173 lines and 13.2 KB"),
    "flat": ("| **A. Flat** |", "| **A. Flat map** |"),
    "purpose": ("It is declared for **0%** of kits", "| kit | 19 | 1,397 |"),
    "builds": ("all 167 build READMEs declare one in their H1", "the README H1 after the slug (167 of 167 have one)"),
    "delivery": ("`entry.orient` gets L0 and cuts the card", "| orientation scout (`entry.orient`) | tier 0 whole."),
    "query": ("| **D. Query only** |", "| **C. Query only** |"),
    "codemap": ("| **E. Extend the codebase map** |", "| **D. Extend an existing generator (the seam)** |"),
    "atlas": ("the atlas becomes the owner's render of the same node table", "the atlas is the owner's render of the same derivation"),
    "closure": ("| complete, three ways", "| closure, forward |"),
    "rater": ("**Agreement on the 52 is 49 of 52 (94.2%), κ = 0.85.**", "agree on 50 of 52, kappa 0.90"),
    "library": ("| library (`reviews/2026-10-16-…-library.md`), 19 items |", "| library (`reviews/2026-10-16-…-library.md`, 19 items) |"),
    "ceiling": ("Barch  26002 B  hits 12/22", "That sets the map's ceiling at about 13 of 20."),
    "reads": ("| spec writer | 76 | 20.5 |", "| spec writer | 76 | 149.9 |"),
    "losing": ("**The map is retired if** the share does not fall", "**The map loses** if any of these holds:"),
    "growth": ("grows about 20 KB a month", "**Flat:** about 21 KB a month."),
    "gap26": ("**gap-mem-26 (HIGH): no whole-project view reaches an agent.**", "| gap-mem-26 |"),
    "kittoml": ("**Two kit directories have no descriptor.**", "there are 17 kit.toml files against MAP.md's 19 kits"),
    "budget": ("| `memory.map-budget` | 16k, 24k, 32k | 24k |", "| `memory.map-budget` | 8k, 16k, 32k | 16k |"),
    "unfold": ("| `memory.map-unfold` |", "**Tier 1** is `gov map <ns>`"),
    "scout": (None, "| orientation scout | per PM-1, it composes the card |"),
    "default": ("**The codebase map is installed by default.**", None),
    "mainsession": ("| PM-7: the attended main session |", None),
}
bad = 0
for key, pair in PHRASES.items():
    out = []
    for run, phrase in zip("ab", pair):
        if phrase is None:
            out.append(f"{run}:-")
            continue
        lines = open(B + run + ".md", encoding="utf-8").read().split("\n")
        hits = [i + 1 for i, ln in enumerate(lines) if phrase in ln]
        if len(hits) != 1:
            bad += 1
            out.append(f"{run}:{hits or 'MISSING'}")
        else:
            out.append(f"{run}:{hits[0]}")
    print(f"{key:12} {' '.join(out)}")
sys.exit(1 if bad else 0)
```

```text
$ python cite_lines.py
owner        a:159 b:148
mechanism    a:17 b:15
size         a:19 b:16
flat         a:116 b:131
purpose      a:43 b:46
builds       a:41 b:44
delivery     a:151 b:174
query        a:119 b:133
codemap      a:120 b:134
atlas        a:MISSING b:20
closure      a:170 b:184
rater        a:66 b:82
library      a:62 b:80
ceiling      a:109 b:87
reads        a:50 b:69
losing       a:223 b:200
growth       a:116 b:100
gap26        a:203 b:233
kittoml      a:40 b:239
budget       a:194 b:217
unfold       a:196 b:17
scout        a:- b:MISSING
default      a:39 b:-
mainsession  a:218 b:-
exit 1
```

The both-runs probe is the systems record's variant (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`
`[instrument-agreement]`) with its layer list changed to this record's one subsection,
`LAYERS = ("project-map",)`. It reads the table clean:

```text
$ python both_runs_probe_v4_pm.py build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md
rows read: 19; rows the predicate matched and checked: 18; exempt, their crediting cell re-measured: 0
findings: 0
exit 0
```

On a copy whose owner row cites run A alone, it fails on that row:

```text
$ python both_runs_probe_v4_pm.py pm-planted.md
rows read: 19; rows the predicate matched and checked: 18; exempt, their crediting cell re-measured: 0
[agreement] Owner: credits project-map A, project-map B; no line cited for project-map B
findings: 1
exit 1
```

## [answers-design] The owner's answers to PM-4 to PM-7, 2026-10-17

The four forks were asked in one round, through the question tool. Each answer is quoted verbatim.

| Fork | The owner's answer | What it settles |
|---|---|---|
| PM-4 | "32k" | `memory.map-budget` defaults to 32k, against the recommended 24k. The map rarely folds, and a structural spawn pays up to 32 KB for it |
| PM-5 | "Required for new nodes, review all the existing nodes and either derive from available information or consult with the owner" | `memory.map-purpose` defaults to `review`. A new node must declare a purpose. Each existing node is reviewed when its namespace's purpose field lands: its purpose is derived from what it already carries, or the owner is consulted (`[purpose]`). `ledger`, `derive` and `refuse` are the offered options, kept as allowed values |
| PM-6 | "Item-declared (Recommended)" | `memory.map-unfold` defaults to `item-declared`. An item declares the namespaces it unfolds, and `gov map <ns>` pulls any other |
| PM-7 | "Card and map (Recommended)" | `memory.default-load` gains `card-and-map` and defaults to it for attended sessions. A session opens with the card and the whole map, about 19 KB more. An act session still loads its work order, as PM-1 says |

- **Against the recommendation.** PM-4 went against it.
- **In the owner's own words.** PM-5 is a value the owner wrote: required for new nodes, as
  recommended, with an active review of the existing nodes in place of the recommended passive
  ledger.
- **Each answer is a policy.** The answer is the default, and the offered options are the allowed
  values. All four keys keep the owner's answer in every preset.
- **Registered.** The three gaps of `[gaps-proposed]` are `gap-mem-26`, `gap-mem-27` and
  `gap-orient-15`.

## [test-run] The map, derived for this design, 2026-10-17

The owner asked, verbatim:

> Let's run a test - map this design fully now by the design we finalized, and keep our session oriented with it.

- **What runs it.** `build/2026-10-17-build-PLAY-dClosedLoop-1-map.py` is a design-time instrument,
  beside the atlas generator.
  - It imports the atlas's derivation, so the map and the atlas are two renders of one node table
    (`[design]`'s "one derivation and two renders").
  - The one index does not exist yet, so each namespace is derived from the source the index will
    extract it from.
  - It writes the map where `--out` says, never into the repository. `--ns <namespace>` prints one
    namespace whole (level 1), and `--pending` lists the purposes awaiting the owner.
- **The map's header** at the run's tree:

  ```text
  map 8a10fcc8 dirty · nodes 2008 · lines 325 · folded item,policy-key,gap,leg,bug-class,closed-build,decision-row,design-record,review,decision-section,event,population,marker,conf-key · pending 85 · unarmed record-kind
  ```

### [test-run-numbers] What the map holds

```text
$ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --out design-map.txt
map: 2008 nodes in 30 namespaces; 24063 B of 32768 (no degrade); folded 14; unarmed record-kind
map: purposes declared 1355, derived 246, pending 407
map: wrote C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/projectmap/design-map.txt
map: every check passes, and record-kind is registered with no extractor: unarmed, never green
exit 2
```

- **The whole design at level 0.** 325 lines in 24.1 KB, under the 32k budget with no degrading. That
  is 2,008 nodes in 30 namespaces: 16 namespaces one line per node, and 14 folded to a counted line.
- **It exits 2, never 0.** Every check passes. The record-kind namespace is registered with no
  extractor, since layer-memory lists the kinds in prose. So it reads unarmed, never green, and the
  header says so.
- **Purposes:** 1,355 declared, 246 derived and 407 pending.
  - The 85 pending at level 0 are the review list PM-5 hands the owner when each namespace's purpose
    field lands. They are 7 roles with no agent file, 25 tag namespaces and 53 policy namespaces.
  - The other 322 pending purposes sit in folded namespaces: legs, populations, markers and config
    keys.

```text
$ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --pending
role: 7 — prompt-writer, planner, architect, tester, reviewer, deployer, maintainer
tag-namespace: 25 — reader, level, layer, step, item, role, policy, practice, principle, kind, record, kit, section, doc, unit, field, leg
policy-namespace: 53 — actions, annotations, asks, autonomy, budgets, build, builds, card, charter, context, core, currency, decisions, de
leg: 140 — kickoff-manifest ratchet, template size <=48KiB, charter size, micro-format definitions, micro-format gate selftest, line lengt
population: 27 — memory/map/affordance-exempt.toml, memory/map/baseline.toml, memory/project/brief-recorded-waiver.txt, memory/project/cor
marker: 20 — gov:argv, gov:argv-begin, gov:argv-end, gov:bounded-fanout, gov:conf-allow-, gov:conf-allow-begin, gov:conf-allow-end, gov:fi
conf-key: 135 — memory-tree.conf:MEMORY_ROOT, memory-tree.conf:ROUTED_PATHS, memory-tree.conf:ROUTED_COMMIT_CUTOFF, memory-tree.conf:ROUTE
```

### [test-run-checks] Each check, seen red

Each plant damages one thing, either the render or the node table, and each turns the run red with
the finding it names:

```text
$ python map.py --check --plant drop-line
FINDING complete: layer has nodes on no line and in no count: ['instruction']
exit 1
$ python map.py --check --plant bad-count
FINDING count: item.* counts 82, the table holds 81
exit 1
$ python map.py --check --plant ghost-rel
FINDING resolves: chain.dOrderedCharter names owner=dGhostBuild, which resolves nowhere
exit 1
$ python map.py --check --plant census
FINDING census: tools/newkit/kit.toml is on disk with no kit node
exit 1
$ python map.py --check --plant no-owner
FINDING owner: tag-namespace.reader names no owning build
exit 1
```

### [test-run-found] What the test found

1. **The atlas had dropped the `[adopt]` step and its five items** since review 86's fold. Its step
   list stopped at `lifecycle`, so it lost the step silently.
   - The map's parity check caught it on its first run.
   - The atlas now reads `[adopt]`, and its page gives the step a badge, a colour token in each theme
     and a stripe span.
   - The probe below checks that the page draws every step its data carries, and it reds on a
     planted missing badge.
2. **The decision log has no unique row key.** `TOOL-aWrittenMethod-1` labels four rows, and
   `TOOL-aUnmannedHelm-5` and `-6` two rows each. An id names a unit, and one unit records several
   decisions. The map keys a repeated id by its ordinal, as the systems record's M35 fix does for a
   repeated heading.
3. **A purpose can carry a date.** The aDeployScout README's title holds one. A line never holds a
   date, so the renderer strips dates from purposes.
4. **One hook script is registered twice under one event.** `manifest-check.sh` hangs off
   SessionStart once per matcher, so a hook's key carries its matcher.
5. **The header needs an unarmed field.** The design's populated check implies one, and the header
   grammar has none. The test adds `unarmed <namespace>`.
6. **A node's key is not always a tag.** Chain builds, live builds and principles keep their native
   ids, such as `dTotalRecall` and `P27`, which the tag grammar's lowercase segments cannot spell. The
   design must say whether a line opens with the node's tag or its id.
7. **The checks caught the instrument's own first-run bugs** before any output was used:
   - a title pattern under DOTALL swallowed every step;
   - the census counted each settings hook twice;
   - two Owners bullets the parser misread.

   The census and key-uniqueness checks found them.

```python
"""Check that a written atlas page can draw every step its data carries: a STEP_META badge and a colour token
in each of the three theme blocks, and a stripe span per step. Exit 1 on any gap.

Usage: python atlas_step_probe.py <page.html> [--drop-meta <tag>]
--drop-meta removes one step's badge from a copy in memory, to see the probe red.
"""
import json
import re
import sys

page = open(sys.argv[1], encoding="utf-8").read()
if "--drop-meta" in sys.argv:
    tag = sys.argv[sys.argv.index("--drop-meta") + 1]
    page = re.sub(r",?\s*" + re.escape(tag) + r": \{ badge: '[^']*' \}", "", page, count=1)
data = json.loads(page.split('<script id="atlas-data" type="application/json">', 1)[1].split("</script>", 1)[0])
steps = [s["tag"] for s in data["steps"]]
meta = re.search(r"var STEP_META = \{(.*?)\};", page, flags=re.S).group(1)
badges = set(re.findall(r"([a-z]+): \{ badge:", meta))
blocks = re.findall(r"--l-entry:[^\n]*", page)
stripe = re.search(r'<div class="stripe"[^>]*>(.*?)</div>', page).group(1).count("<span>")
cols = re.search(r"\.stripe \{[^}]*repeat\((\d+), 1fr\)", page).group(1)
bad = []
for t in steps:
    if t not in badges:
        bad.append(f"{t}: no STEP_META badge")
    for i, b in enumerate(blocks):
        if f"--l-{t}:" not in b:
            bad.append(f"{t}: no colour token in theme block {i + 1}")
if stripe != len(steps) or int(cols) != len(steps):
    bad.append(f"stripe: {stripe} spans in {cols} columns for {len(steps)} steps")
print(f"steps {len(steps)} ({', '.join(steps)}); badges {len(badges)}; theme blocks {len(blocks)}; stripe {stripe} in {cols}")
for b in bad:
    print("FINDING", b)
sys.exit(1 if bad else 0)
```

```text
$ python atlas_step_probe.py closed-loop-atlas.html
steps 9 (entry, plan, design, build, test, deploy, breakpoint, lifecycle, adopt); badges 9; theme blocks 3; stripe 9 in 9
exit 0
$ python atlas_step_probe.py closed-loop-atlas.html --drop-meta adopt
steps 9 (entry, plan, design, build, test, deploy, breakpoint, lifecycle, adopt); badges 8; theme blocks 3; stripe 9 in 9
FINDING adopt: no STEP_META badge
exit 1
```

### [test-run-session] Keeping the session oriented

- **This session now holds the map.** It was regenerated with `--out` and read whole, as PM-7 designs
  for an attended session.
- **It is regenerated after every design change** and read again at session start and after each
  compaction. The owner's standing ask is recorded in the session's memory, beside the atlas's.
- **The product version is dWellOiledMachine's.** Its session-start hook loads the card and the map
  (PM-7). This test touches neither `.claude/` nor `tools/`.

## [reload] The map after the compaction, 2026-10-17

The owner said, verbatim, before compacting the session:

> Just to confirm, the context is it 90% now, after this message I will compact it. Need to check afterwards if the map's still loaded.

and, after it:

> so, answer me something that only the map can directly point at

- **The map came through the compaction.** The compaction's summary carried the level-0 map verbatim,
  though the last message before it had said it would not. The standing ask was followed anyway: the
  map was regenerated with `--out` and read whole.
  Corrected 2026-10-17 in `[reload-summary]`: the summary rewrote 3 of the map's 355 lines.
- **It matches the map read before the compaction**, but for its header, now at a clean tree, and one
  event, the test run's own session-log entry:

  ```text
  $ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --out design-map.txt
  map: 2009 nodes in 30 namespaces; 24057 B of 32768 (no degrade); folded 14; unarmed record-kind
  map: purposes declared 1356, derived 246, pending 407
  map: wrote C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/projectmap/design-map.txt
  map: every check passes, and record-kind is registered with no extractor: unarmed, never green
  exit 2
  $ diff design-map-precompact.txt design-map.txt
  1c1
  < map 8a10fcc8 dirty · nodes 2008 · lines 325 · folded item,policy-key,gap,leg,bug-class,closed-build,decision-row,design-record,review,decision-section,event,population,marker,conf-key · pending 85 · unarmed record-kind
  ---
  > map 72acbd77 · nodes 2009 · lines 325 · folded item,policy-key,gap,leg,bug-class,closed-build,decision-row,design-record,review,decision-section,event,population,marker,conf-key · pending 85 · unarmed record-kind
  349c349
  < - event.* — 109 nodes · gov map event
  ---
  > - event.* — 110 nodes · gov map event
  ```

### [reload-pointer] What only the map points at: two steps no build owns

Corrected 2026-10-17 in `[fixes-correction]`: lifecycle's own section names its owner, so only entry
is owned by no build.

- **The pointer.** At level 0, two of the nine steps carry no `owner=`: `step.entry` and
  `step.lifecycle`, 6 items each. One level down, `--ns item` gives each of their 12 items its step as
  owner, and nothing further.
- **Why only the map shows it.** Each step's record lists its items, and each chain row lists what its
  build builds. Nothing lists what no build claims. The map puts every step beside its owner, so the
  absence is a blank on a line.
- **The probe.** A step reaches a build one of two ways: through its stage's build, or through chain
  rows that cite its items by tag. The probe joins the item namespace to v2's 15 chain rows.

```python
"""Which chain build owns each flow step's items? Joins the map's item namespace (level 1) to v2's chain rows.

Usage: python step_owner_probe.py <item-ns.txt> <design-map.txt> <architecture-v2.md>

<item-ns.txt> is `map.py --ns item`; <design-map.txt> is the level-0 map. A chain row claims an item when it
cites the item's tag in backticks. The adopt step's claims are the probe's positive control: v2's rows cite
them, so a probe that reads none of them is blind.
"""
import re
import sys


def read(path):
    return open(path, encoding="utf-8", newline="").read().replace("\r\n", "\n")


items = re.findall(r"^- item\.(\S+) — .*· owner=(\S+)$", read(sys.argv[1]), flags=re.M)
owner = dict(re.findall(r"^- step\.(\S+) — .*?(?:· owner=(\S+))?$", read(sys.argv[2]), flags=re.M))
v2 = read(sys.argv[3])
rows = dict(re.findall(r"^\| (d[A-Z][a-z]+[A-Z]\w+) \|(.*)$", v2, flags=re.M))
print(f"items {len(items)} · steps {len(owner)} · chain rows {len(rows)}")
print()
for step in owner:
    tags = [t for t, s in items if s == step]
    claimed = [t for t in tags if any(f"`{t}`" in r for r in rows.values())]
    print(f"{step:<11} items {len(tags):>2} · claimed by tag in a chain row {len(claimed):>2} · map owner {owner[step] or '—'}")
for step in ("entry", "lifecycle", "adopt"):
    print()
    print(f"[{step}]")
    for t, s in items:
        if s == step:
            by = [b for b, r in rows.items() if f"`{t}`" in r]
            print(f"  {t:<18} rows {','.join(by) or '—'} · cited in v2 {v2.count(f'`{t}`')}x")
print()
print("prose homes, by the words the items' work goes by:")
for label, pat in (("placement", r"\bplacement\b"), ("intake log", r"intake log"),
                   ("orientation card", r"orientation card"),
                   ("pause, resume, withdraw, supersede", r"pause, resume, withdraw and supersede"),
                   ("terminal states", r"terminal states"), ("quiesce", r"quiesc")):
    hit = [b for b, r in rows.items() if re.search(pat, r, flags=re.I)]
    print(f"  {label:<36} {','.join(hit) or '—'}")
```

```text
$ python step_owner_probe.py item-ns.txt design-map.txt 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
items 81 · steps 9 · chain rows 15

entry       items  6 · claimed by tag in a chain row  0 · map owner —
plan        items 11 · claimed by tag in a chain row  0 · map owner dRankedPlan
design      items 12 · claimed by tag in a chain row  1 · map owner dIndexedDesign
build       items 10 · claimed by tag in a chain row  2 · map owner dScopedBuild
test        items 10 · claimed by tag in a chain row  0 · map owner dWitnessedBar
deploy      items 13 · claimed by tag in a chain row  0 · map owner dShippedRelease
breakpoint  items  8 · claimed by tag in a chain row  4 · map owner dCalibratedLens
lifecycle   items  6 · claimed by tag in a chain row  0 · map owner —
adopt       items  5 · claimed by tag in a chain row  5 · map owner —

[entry]
  entry.intake       rows — · cited in v2 0x
  entry.orient       rows — · cited in v2 0x
  entry.place        rows — · cited in v2 0x
  entry.place-check  rows — · cited in v2 0x
  entry.place-owner  rows — · cited in v2 0x
  entry.claim        rows — · cited in v2 0x

[lifecycle]
  life.request       rows — · cited in v2 0x
  life.quiesce       rows — · cited in v2 0x
  life.notify        rows — · cited in v2 0x
  life.snapshot      rows — · cited in v2 0x
  life.unlease       rows — · cited in v2 1x
  life.close         rows — · cited in v2 0x

[adopt]
  adopt.census       rows dTotalRecall · cited in v2 1x
  test.seed          rows dWitnessedBar,dShippedRelease · cited in v2 3x
  adopt.practices    rows dTotalRecall · cited in v2 2x
  adopt.decisions    rows dTotalRecall · cited in v2 1x
  adopt.reconstruct  rows dTotalRecall · cited in v2 3x

prose homes, by the words the items' work goes by:
  placement                            dBoundRoles,dRankedPlan
  intake log                           dRankedPlan
  orientation card                     dDeclaredLoop
  pause, resume, withdraw, supersede   dWellOiledMachine
  terminal states                      dDeclaredLoop
  quiesce                              —
```

- **What it shows:**
  - The stage steps reach their builds through their stage. Their items are rarely cited by tag: plan
    0 of 11, test 0 of 10, deploy 0 of 13.
  - Adopt has no stage, and v2's rows cite all five of its items. Four sit in dTotalRecall's row, and
    `test.seed` in dWitnessedBar's. dShippedRelease's row cites `test.seed` only as something its
    install and update hooks call.
  - The probe reads a citation as a claim, so it can only over-count. Adopt's five are its positive
    control.
  - Entry and lifecycle have neither route. No chain row cites any of their 12 items. The only tag
    citation of any of them in v2 is the rename note for `life.unlease`, at its line 293.
  - Their work is described, but in prose split across builds:
    - placement sits in dRankedPlan's and dBoundRoles' rows, the intake log in dRankedPlan's, and the
      orientation card in dDeclaredLoop's;
    - the owner's pause, resume, withdraw and supersede sit in dWellOiledMachine's row, and the
      terminal states in dDeclaredLoop's;
    - no chain row says "quiesce", the word `life.quiesce` is named for.
- **The map's own miss.** The adopt line shows no owner either, but there the design is right and the
  generator is wrong. It derives a step's owner only from the step's stage, through `step_stage`, so a
  step owned through its items' claims reads unowned.
- **Proposed, not asked:**
  - a fork on how entry and lifecycle reach a build: an owning build per step, or each item claimed by
    tag in its build's chain row;
  - the generator reading the items' claims, so the adopt line reads `owner=dTotalRecall,dWitnessedBar`.

## [fixes] What the findings say to fix, 2026-10-17

The owner asked, verbatim:

> Based on these findings, what needs to be fixed to improve the concept?

### [fixes-correction] Lifecycle is owned, and entry is not

`[reload-pointer]` reported that no build owns entry or lifecycle. Half of that was wrong.
- **Lifecycle names its owner in its own section.** flow-steps' `[lifecycle]` opens: "Runtime executes
  the owner's controls (dWellOiledMachine, RT-3)". The probe read only v2's chain rows, so it missed
  that statement the way the generator misses adopt's claims.
- **Entry names none.** Its section says only that the intake hook is Runtime's, and that hook's gap,
  `gap-rt-14`, is dWellOiledMachine's. Its other five items have no owner statement anywhere. The
  `[adopt]` match below is a record path the section cites, not an owner.
- **The register leans one way.** dDeclaredLoop owns 7 of the 15 Orient gaps, the area entry's work
  falls in.

### [fixes-cause] One relation, four homes, read from one

Who owns a node is stated in four places, and none of them is a declared field:
- v2's chain table, whose stage column gives each stage step its build;
- chain-row prose, which cites some items and keys by tag;
- step-section prose, as lifecycle's does;
- the systems' owner tables.

The generator reads one home per kind of node, and renders a blank where that home is silent. So a
blank means one of three things, and the reader cannot tell which:
- a real gap, as entry is;
- a fact stated in a home the generator does not read, as adopt's and lifecycle's are;
- nothing, by design: the prompt writer is a cycle role and acts in no item, and the deployer and the
  maintainer act in expansion layers (layer-roles `[roster]`, P28).

The checks passed through all three. The run exits 2, never 1, because the owner check covers only the
tag namespaces and the systems.

The policy keys show the scale.
- The catalogue's columns are key, allowed values, default and source, and its source names the round
  that decided the key, not a build.
- 115 of 187 keys are cited by no chain row, so their owner can only be inferred, from a namespace's
  name, a system's owner table or a row's prose.
- The map renders no owner field on a policy namespace at all, so this blank is not even visible.

```bash
#!/usr/bin/env bash
# The probes behind the project map's [fixes] section. Run from the worktree root; writes into the directory $1.
set -u
OUT=$1
H=$(dirname "$0")
B=memory/builds/dClosedLoop/build
V=$B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
M=$B/2026-10-17-build-PLAY-dClosedLoop-1-map.py
python $M --ns policy-key > "$OUT/policy-key-ns.txt"
python $M --ns gap > "$OUT/gap-ns.txt"
{
  echo '$ step sections that name a chain build in their first eight lines'
  awk '/^## \[(entry|plan|design|build|test|deploy|breakpoint|lifecycle|adopt)\]/{s=$2; n=0} s && n<8 {n++; if (match($0, /d[A-Z][a-z]+[A-Z][A-Za-z]+/)) print s, substr($0, RSTART, RLENGTH)}' \
    $B/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md | sort -u
  echo '$ the Orient gaps by owning build, and gap-rt-14'
  grep -oE '^- gap\.gap-orient-[0-9]+ .*owner=\S+' "$OUT/gap-ns.txt" | grep -oE 'owner=\S+' | sort | uniq -c
  grep -E '^- gap\.gap-rt-14 ' "$OUT/gap-ns.txt" | grep -oE 'gap-rt-14|owner=\S+' | paste -sd' '
  echo '$ the policy catalogue header'
  grep -nE '^\| Key \| Allowed values' $V
  echo '$ python key_owner_probe.py policy-key-ns.txt architecture-v2.md'
  python "$H/key_owner_probe.py" "$OUT/policy-key-ns.txt" $V
  echo '$ python key_owner_probe.py policy-key-ns.txt architecture-v2.md --plant floor'
  python "$H/key_owner_probe.py" "$OUT/policy-key-ns.txt" $V --plant floor | head -1
} > "$OUT/fixes-probes.txt" 2>&1
```

```python
"""How many of a namespace's nodes does some chain row cite? Joins `map.py --ns <namespace>` to v2's chain rows.

Usage: python key_owner_probe.py <ns.txt> <architecture-v2.md> [--plant <key>]

A row cites a node when it holds the node's key in backticks. A citation is not always a claim (a row may
name a key it only calls), so the 1-row and 2+-row counts over-state ownership; the 0-row count is exact.
--plant appends a citation of <key> to the first chain row, in memory, to see a 0-row key leave the list.
"""
import re
import sys


def read(path):
    return open(path, encoding="utf-8", newline="").read().replace("\r\n", "\n")


nodes = re.findall(r"^- ([a-z-]+)\.(\S+) — ", read(sys.argv[1]), flags=re.M)
v2 = read(sys.argv[2])
rows = dict(re.findall(r"^\| (d[A-Z][a-z]+[A-Z]\w+) \|(.*)$", v2, flags=re.M))
if "--plant" in sys.argv:
    first = next(iter(rows))
    rows[first] += f" `{sys.argv[sys.argv.index('--plant') + 1]}`"
by = {key: [b for b, r in rows.items() if f"`{key}`" in r] for _, key in nodes}
zero = [k for k in by if not by[k]]
one = [k for k in by if len(by[k]) == 1]
many = [k for k in by if len(by[k]) > 1]
print(f"{nodes[0][0] if nodes else '?'}: {len(nodes)} nodes · chain rows {len(rows)} · "
      f"cited by no row {len(zero)} · one row {len(one)} · two or more {len(many)}")
groups = {}
for k in zero:
    groups.setdefault(k.split(".")[0], []).append(k)
print("cited by no row, by namespace:")
for g in sorted(groups):
    print(f"  {g} {len(groups[g])}: {', '.join(groups[g])}")
print("cited by two or more rows:")
for k in many:
    print(f"  {k}: {', '.join(by[k])}")
```

```text
$ step sections that name a chain build in their first eight lines
[adopt] dClosedLoop
[lifecycle] dWellOiledMachine
$ the Orient gaps by owning build, and gap-rt-14
      3 owner=dBoundRoles
      7 owner=dDeclaredLoop
      1 owner=dOrderedCharter
      1 owner=dRankedPlan
      1 owner=dTendedCadence
      2 owner=dWellOiledMachine
gap-rt-14 owner=dWellOiledMachine
$ the policy catalogue header
636:| Key | Allowed values | Default | Source |
$ python key_owner_probe.py policy-key-ns.txt architecture-v2.md
policy-key: 187 nodes · chain rows 15 · cited by no row 115 · one row 68 · two or more 4
cited by no row, by namespace:
  annotations 4: annotations.lookup, annotations.budget, annotations.resolve-scope, annotations.delivery
  budgets 1: budgets.*
  build 1: build.release-hold
  card 1: card.follows
  core 2: core.bypass, core.exceptions
  currency 2: currency.max-behind, currency.on-behind
  decisions 1: decisions.major
  deploy 4: deploy.runs, deploy.promotion, deploy.on-verify-fail, deploy.currency
  deps 3: deps.coordination, deps.early-build, deps.messaging
  design 2: design.handoff, design.overlap
  floor 1: floor
  flow 1: flow.route-backs
  hooks 1: hooks.bypass
  install 1: install.from
  instructions 3: instructions.slices, instructions.legacy, instructions.task-charter
  integrations 1: integrations.tracker
  kits 3: kits.cadence, kits.host, kits.watch-cadence
  landing 1: landing.order
  leases 6: leases, leases.granularity, leases.renewal, leases.expiry-hours, leases.overlap, leases.offline
  maintain 10: maintain.host, maintain.cadence, maintain.fixes, maintain.on-breach, maintain.events, maintain.reading-tree, maintain.node-readings, maintain.reading-admission, maintain.dead-after, maintain.record-when
  memory 6: memory.default-load, memory.over-budget, memory.map-overflow, memory.map-unfold, memory.legacy-anchors, memory.superseded-slices
  notify 1: notify.channel
  observability 1: observability.run-record
  orient 1: orient.budget
  patch 1: patch.ratify
  plan 4: plan.authority, plan.unplaced, plan.triage, plan.kickoff
  policy 3: policy.guard, policy.proof, policy.on-missing-expansion
  release 1: release.environments
  retrofit 6: retrofit.drain, retrofit.claim-on-touch, retrofit.widen, retrofit.unseeded, retrofit.cadence, retrofit.slot-bytes
  reuse 1: reuse.propose
  review 13: review.design.rounds, review.design.round-count, review.unverified, review.<stage>.effort, review.recommendation, review.build.when, review.blocks, review.left-shift, review.recommendation.source, review.loop.cadence, review.loop.retire, review.loop.window-days, review.loop.catch-source
  roles 2: roles.shape-enforce, roles.orientation.house-index
  runtime 9: runtime.spawn-backend, runtime.relaunch, runtime.act-ceiling, runtime.hold-ceiling, runtime.hook-failure, runtime.attended-allowance, runtime.harnesses, runtime.secret-home, runtime.secret-scan
  tags 4: tags.slice, tags.retired-cites, tags.positional, tags.bare-refs
  tests 3: tests.without-cadence, tests.product, tests.landing-levels
  transitions 1: transitions.record
  verdict 9: verdict, verdict.blocks, verdict.held, verdict.flakes, verdict.tree, verdict.red-route, verdict.remote.trust, verdict.remote.pin-scope, verdict.remote.pin
cited by two or more rows:
  placement.check: dBoundRoles, dRankedPlan
  instructions.edit: dOrderedCharter, dTotalRecall, dMindYourWords
  memory.item-budget: dTotalRecall, dCalibratedLens
  memory.map-purpose: dOrderedCharter, dTotalRecall
$ python key_owner_probe.py policy-key-ns.txt architecture-v2.md --plant floor
policy-key: 187 nodes · chain rows 15 · cited by no row 114 · one row 69 · two or more 4
```

The class is new, and is filed as `absence-read-from-one-of-several-homes` in `memory/gotchas/`. It has
no machine gate yet. The owner check, `[fixes-concept]`'s second fix, is the gate it owes.

### [fixes-concept] What to fix in the concept

1. **One home for ownership.** Every node a build must build declares its owning build once, in a field:
   - items, beside their actor in flow-steps;
   - keys, in a catalogue column;
   - points, in their table;
   - record kinds, in their registry.

   The owners of a step, a system and a namespace are derived from their members, so a step can have
   several. Prose stops being a source of ownership.
2. **The owner check covers everything a build must build.** Items, keys, points, record kinds, tag
   namespaces and systems are each owned by exactly one build, and the check is seen red on a planted
   orphan. It is acceptance check (c)'s gap join, widened from gaps.
3. **The generator never infers a relation.** Today it infers three:
   - a step's owner, from its stage (`step_stage`);
   - every point's owner, dWellOiledMachine, from a literal;
   - a tag namespace's owner, defaulted from the Owners bullet.

   An inferred owner reads exactly like a declared one, so a default hides the gap the map exists to
   show.
4. **Typed blanks, and the debt in the header.**
   - A line tells "nothing, by design" from "not declared". A role line carries the roster's layer and
     mode, so the three by-design blanks explain themselves.
   - A required relation that is missing is a finding. The header counts it beside `pending` and
     `unarmed`, as `unowned N`.
5. **Arm what prose holds.** record-kind stays unarmed while layer-memory lists the kinds in prose. A
   design-time table arms it now, and dTotalRecall's registry replaces the table in the product.
6. **Stable keys.**
   - A decision row keyed by its ordinal changes key when a row is inserted above it, so every citation
     of it goes stale.
   - Whether a line opens with a node's tag or its native id is still open (`[test-run-found]`, 6).

### [fixes-design] What the fixes leave in the design

- **Entry's six items need an owner.** Their work sits in prose across four builds:
  - placement and the intake log, in dRankedPlan's row;
  - the scout's placement return, in dBoundRoles' row;
  - the card, in dDeclaredLoop's row;
  - the intake hook, in Runtime's section.
- **115 policy keys need an owner.** Four keys that two or three rows cite need one of those builds
  named: `placement.check`, `instructions.edit`, `memory.item-budget` and `memory.map-purpose`.
- **Lifecycle and adopt are owned already.** Their owners move into the field.
- **The 85 purposes pending at level 0** are PM-5's review, queued since `[test-run]`.

### [forks-fixes] Asked, 2026-10-17

- **PM-8, ownership's home:**
  - a field on each node, with the owners of steps and namespaces derived (recommended);
  - a field per step and per namespace, inherited by their nodes;
  - chain rows claiming by tag.
- **PM-9, entry's owner:**
  - dDeclaredLoop, with the intake hook kept by dWellOiledMachine (recommended);
  - each item to the build whose row describes its work;
  - dRankedPlan.
- **PM-10, the 115 keys:**
  - a proposed owner for each key, with its evidence, approved in one pass (recommended);
  - one owner per namespace, inherited by its keys;
  - two research runs, with their disagreements put to the owner.
- **PM-11, a line's key:**
  - the native id where one exists (recommended);
  - always a tag, with the id as an alias.

## [answers-fixes] The owner's answers to PM-8 to PM-11, 2026-10-17

The owner chose, verbatim:
- PM-8: "A field on each node (Recommended)"
- PM-9: "dDeclaredLoop (Recommended)"
- PM-10: "I propose, you approve (Recommended)"
- PM-11: "Native id where one exists (Recommended)"

All four are structural, so none adds a policy key.

- **Folded:**
  - `[line]` gains the native-id key, `?` for a missing required field, the header's `pending`,
    `unowned` and `unarmed` fields, and the rule that a line reads declared fields only;
  - `[checks]` splits owner from extractor, widens the owner check to every node a build must build,
    and adds the no-inference check;
  - `[owners]` gives the owner fields to dDeclaredLoop, dWellOiledMachine and dTotalRecall, and the
    native-id keys to dOrderedCharter;
  - v2 gains a revision note, flow-steps' `[entry]` its owner, and the systems record's
    `[design-tags]` the map keys.
- **Next, under PM-10:** a table proposing an owner for every item, policy key, point and tag
  namespace, each with its evidence, for the owner to approve in one pass. Its fold adds the owner
  columns.
- **The generator keeps today's derivation until then.** Once the columns land, it reads them and
  infers nothing, and its owner check is seen red on a planted orphan.

## [reload-summary] The summary was not verbatim, 2026-10-17

`[reload]` says the compaction's summary carried the level-0 map verbatim. It did not.
- **3 of its 355 lines were rewritten.** They are the three kits whose derived purposes were fragments,
  and the summary replaced each with plausible text. The diff reads the summary from the session's own
  transcript:

```python
"""Diff the level-0 map the compaction summary carried against the map file read before the compaction.

Usage: python -I summary_map_diff.py <session.jsonl> <design-map-precompact.txt>

The summary arrives as a user message that opens "This session is being continued". Its map is the fenced
text block that starts with the map's header line, indented under a list item.
"""
import difflib
import json
import re
import sys

summary = None
for line in open(sys.argv[1], encoding="utf-8"):
    rec = json.loads(line)
    if rec.get("type") != "user":
        continue
    content = rec.get("message", {}).get("content")
    parts = [content] if isinstance(content, str) else [c.get("text", "") for c in content or [] if isinstance(c, dict)]
    for text in parts:
        if text.startswith("This session is being continued") and "map 8a10fcc8" in text:
            summary = text
if summary is None:
    sys.exit("no summary carrying the map found")
FENCE = "`" * 3  # spelled out, so this source can sit inside a record's fence
m = re.search(FENCE + r"text\n( *)(map 8a10fcc8.*?)\n\1" + FENCE, summary, flags=re.S)
if not m:
    sys.exit("the summary's map block was not found")
indent = len(m.group(1))
carried = [ln[indent:] if ln.startswith(" " * indent) else ln for ln in m.group(2).split("\n")]
filed = open(sys.argv[2], encoding="utf-8", newline="").read().replace("\r\n", "\n").rstrip("\n").split("\n")
print(f"carried {len(carried)} lines · filed {len(filed)} lines")
changed = [d for d in difflib.unified_diff(filed, carried, "filed", "carried", n=0, lineterm="")
           if d[:1] in "+-" and not d.startswith(("+++", "---"))]
print(f"differing lines {len(changed)}")
for d in changed:
    print(d)
```

```text
$ python -X utf8 -I summary_map_diff.py <session.jsonl> design-map-precompact.txt
carried 355 lines · filed 355 lines
differing lines 6
-- kit.drift-audit — harness's own meta.version to the same number.
+- kit.drift-audit — drift-audit kit
-- kit.run-gates — agreement between a marker and a constant, and this repo ha…
+- kit.run-gates — run-gates kit
-- kit.unattended — The binding contract is not here. It is UNATTENDED-PROTOCOL…
+- kit.unattended — The unattended-run kit
```

- **So the regeneration was no ritual.** It restored the map as derived, defects included, where the
  summary had hidden them. A summary does not carry anything that must stay exact, and that is the
  reason for the standing ask to regenerate after a compaction. The class is filed as
  `summary-rewrites-the-text-it-carries`.
- **The fragments were the generator's.** With no purpose in a README's title, it took the README's
  first prose line:
  - for drift-audit and run-gates, that line continued a sentence whose first line opens with a
    backtick, which the pattern skips;
  - for unattended, it was a disclaimer, "The binding contract is not here".

  The generator now mines no prose. The three kits render as pending, so the level-0 pending count is 88
  and the derived purposes are 243. PM-5's review derives theirs, citing its source.

```text
$ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --out design-map.txt
map: 2015 nodes in 30 namespaces; 23903 B of 32768 (no degrade); folded 14; unarmed record-kind
map: purposes declared 1362, derived 243, pending 410
map: wrote C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/projectmap/design-map.txt
map: every check passes, and record-kind is registered with no extractor: unarmed, never green
rc 2
$ diff design-map-before-kitfix.txt design-map.txt
1c1
< map 21211c64 · nodes 2015 · lines 325 · folded item,policy-key,gap,leg,bug-class,closed-build,decision-row,design-record,review,decision-section,event,population,marker,conf-key · pending 85 · unarmed record-kind
---
> map 21211c64 dirty · nodes 2015 · lines 325 · folded item,policy-key,gap,leg,bug-class,closed-build,decision-row,design-record,review,decision-section,event,population,marker,conf-key · pending 88 · unarmed record-kind
127c127
< - kit.drift-audit — harness's own meta.version to the same number.
---
> - kit.drift-audit — —
139c139
< - kit.run-gates — agreement between a marker and a constant, and this repo ha…
---
> - kit.run-gates — —
141c141
< - kit.unattended — The binding contract is not here. It is UNATTENDED-PROTOCOL…
---
> - kit.unattended — —
```

- **The atlas step probe matched its own source.** The page embeds every record, and `[test-run-found]`
  embeds the probe, so the probe's theme-block pattern matched itself as a fourth block, with no step
  tokens, and reported eight findings against a page that drew every step. The probe now reads only the
  page's style elements. The class is filed as `instrument-recorded-into-the-corpus-it-scans`.

```python
"""Check that a written atlas page can draw every step its data carries: a STEP_META badge and a colour token
in each of the three theme blocks, and a stripe span per step. Exit 1 on any gap.

Usage: python atlas_step_probe.py <page.html> [--drop-meta <tag>]
--drop-meta removes one step's badge from a copy in memory, to see the probe red.
"""
import json
import re
import sys

page = open(sys.argv[1], encoding="utf-8").read()
if "--drop-meta" in sys.argv:
    tag = sys.argv[sys.argv.index("--drop-meta") + 1]
    page = re.sub(r",?\s*" + re.escape(tag) + r": \{ badge: '[^']*' \}", "", page, count=1)
data = json.loads(page.split('<script id="atlas-data" type="application/json">', 1)[1].split("</script>", 1)[0])
steps = [s["tag"] for s in data["steps"]]
meta = re.search(r"var STEP_META = \{(.*?)\};", page, flags=re.S).group(1)
badges = set(re.findall(r"([a-z]+): \{ badge:", meta))
# Theme blocks are read from the page's <style> elements only: the page embeds every record, and the record
# that carries this probe's source would otherwise match the pattern below as a fourth block.
css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", page, flags=re.S))
blocks = re.findall(r"--l-entry:[^\n]*", css)
stripe = re.search(r'<div class="stripe"[^>]*>(.*?)</div>', page).group(1).count("<span>")
cols = re.search(r"\.stripe \{[^}]*repeat\((\d+), 1fr\)", page).group(1)
bad = []
for t in steps:
    if t not in badges:
        bad.append(f"{t}: no STEP_META badge")
    for i, b in enumerate(blocks):
        if f"--l-{t}:" not in b:
            bad.append(f"{t}: no colour token in theme block {i + 1}")
if stripe != len(steps) or int(cols) != len(steps):
    bad.append(f"stripe: {stripe} spans in {cols} columns for {len(steps)} steps")
print(f"steps {len(steps)} ({', '.join(steps)}); badges {len(badges)}; theme blocks {len(blocks)}; stripe {stripe} in {cols}")
for b in bad:
    print("FINDING", b)
sys.exit(1 if bad else 0)
```

```text
$ python atlas_step_probe.py closed-loop-atlas.html
steps 9 (entry, plan, design, build, test, deploy, breakpoint, lifecycle, adopt); badges 9; theme blocks 3; stripe 9 in 9
rc 0
$ python atlas_step_probe.py closed-loop-atlas.html --drop-meta adopt
steps 9 (entry, plan, design, build, test, deploy, breakpoint, lifecycle, adopt); badges 8; theme blocks 3; stripe 9 in 9
FINDING adopt: no STEP_META badge
rc 1
```

- **The atlas is at version 28**, republished after PM-8 to PM-11's fold.
