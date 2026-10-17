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
